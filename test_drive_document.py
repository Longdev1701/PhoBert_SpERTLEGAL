"""
Kich ban:
1. Ket noi Google Drive qua drive_client (hoac Folder ID tuy chon).
2. Tai tep van ban (.docx, .json) ve thu muc cache.
3. Chay suy luan (Inference) trich xuat Thuc the & Quan he bang PhoBERT-SpERT da huan luyen.
4. Xuat bao cao chi tiet sang tep Markdown (.md) kem bieu do cau truc Mermaid.
"""

import os
import re
import json
import time
import zipfile
import unicodedata
import argparse
import torch
from transformers import AutoTokenizer

from models.spert_phobert import PhoBERTSpeRT
from data.legal.vi_tokenize import vi_tokenize
from data.legal.schema import ENTITY_TYPES, RELATION_TYPES
from data.legal.intra_sentence_kg import extract_intra_sentence_spans, extract_document_self_lexicon
from data.legal.drive_client import list_folder, download


# ======================================================================
# 1. Ham tien xu ly van ban Word (.docx)
# ======================================================================
def norm_text(s):
    s = unicodedata.normalize("NFC", s or "")
    s = s.replace("\u00d0", "\u0110").replace("\u00f0", "\u0111")
    s = s.replace("\u00a0", " ").replace("\u200b", "").replace("\u00ad", "")
    s = re.sub(
        r"([A-ZÀÁẢÃẠĂẮẰẲẴẶÂẤẦẨẪẬĐÈÉẺẼẸÊẾỀỂỄỆÌÍỈĨỊÒÓỎÕỌÔỐỒỔỖỘƠỚỜỞỠỢÙÚỦŨỤƯỨỪỬỮỰỲÝỶỸỴ]{2,})([A-ZÀÁẢÃẠĂẮẰẲẴẶÂẤẦẨẪẬĐÈÉẺẼẸÊẾỀỂỄỆÌÍỈĨỊÒÓỎÕỌÔỐỒỔỖỘƠỚỜỞỠỢÙÚỦŨỤƯỨỪỬỮỰỲÝỶỸỴ][a-zàáảãạăắằẳẵặâấầẩẫậđèéẻẽẹêếềểễệìíỉĩịòóỏõọôốồổỗộơớờởỡợùúủũụưứừửữựỳýỷỹỵ])",
        r"\1 . \2",
        s,
    )
    return re.sub(r"\s+", " ", s).strip()


def read_docx_paragraphs(path):
    """Doc danh sach cac doan van tu file .docx bang zipfile va xml. Ho tro fallback neu file docx bi MS Word khoa."""
    txt_fallback = os.path.join(os.path.dirname(path), "van_ban_goc.txt")
    try:
        with zipfile.ZipFile(path) as z:
            xml_content = z.read("word/document.xml").decode("utf-8")
        # Xu ly cac the ngat dong / tab
        xml_content = re.sub(r"<w:(?:br|tab|cr)\b[^>]*/>", "<w:t> </w:t>", xml_content)
        paras = []
        for p in re.findall(r"<w:p[ >].*?</w:p>", xml_content, re.S):
            t = "".join(re.findall(r"<w:t[^>]*>([^<]*)</w:t>", p))
            t = re.sub(r"(?:[-_=*.…]\s*){3,}", " ", t)
            t = norm_text(t)
            if t and re.search(r"[A-Za-zÀ-ỹ0-9]", t):
                if paras and re.search(r"\bý$", paras[-1], re.I) and re.match(r"^\([ivx]+\)", t, re.I):
                    paras[-1] = paras[-1] + " " + t
                else:
                    paras.append(t)
        return paras
    except Exception as e:
        print(f"[!] Không mở trực tiếp được docx ({e}).")
        if os.path.exists(txt_fallback):
            print(f"[+] Tự động nạp dữ liệu từ tệp văn bản thuần: {txt_fallback}")
            with open(txt_fallback, "r", encoding="utf-8") as f:
                return [p.strip() for p in f.read().split("\n\n") if p.strip()]
        return []



# ======================================================================
# 2. Suy luan Joint NER & RE (PhoBERT-SpERT)
# ======================================================================
STRUCT_CONTAINER_SET = {"CHUONG", "DIEU", "KHOAN", "DIEM"}
OUTER_HUB_SET = {"HANH_VI_VI_PHAM", "NGHIA_VU_QUYEN", "HINH_PHAT_CHE_TAI", "BIEN_PHAP_KHAC_PHUC"}


def _nest_level(ent_type: str) -> int:
    if ent_type == "CHUONG":
        return 3
    if ent_type in {"DIEU", "KHOAN", "DIEM"}:
        return 2
    if ent_type in OUTER_HUB_SET:
        return 1
    return 0



def non_max_suppression(entities):
    """
    3-Level Nested-Aware NMS:
      - Cấp 2 (Khung cấu trúc): DIEU, KHOAN, DIEM (bao trọn toàn bộ nội dung điều/khoản/điểm).
      - Cấp 1 (Thực thể trung tâm - Outer Hubs): HANH_VI_VI_PHAM, NGHIA_VU_QUYEN, HINH_PHAT_CHE_TAI, BIEN_PHAP_KHAC_PHUC.
      - Cấp 0 (Thực thể vệ tinh - Inner Satellites): MUC_TIEN, GIAY_TO_HO_SO, CHU_THE_CA_NHAN, LINH_VUC, THAM_CHIEU_PHAP_LY...
    """
    sorted_ents = sorted(entities, key=lambda x: x["confidence"], reverse=True)
    selected = []
    for ent in sorted_ents:
        s1, e1 = ent["span"]
        t1 = ent.get("type", "")
        lvl1 = _nest_level(t1)
        conflict = False
        for kept in selected:
            s2, e2 = kept["span"]
            t2 = kept.get("type", "")
            lvl2 = _nest_level(t2)
            if (s1, e1) == (s2, e2):
                conflict = True
                break
            if max(s1, s2) < min(e1, e2):
                is_valid_nest = (
                    (lvl1 > lvl2 and s2 >= s1 and e2 <= e1)
                    or (lvl2 > lvl1 and s1 >= s2 and e1 <= e2)
                )
                if not is_valid_nest:
                    conflict = True
                    break
        if not conflict:
            selected.append(ent)
    return sorted(selected, key=lambda x: (x["span"][0], -x["span"][1]))


class LegalExtractor:
    def __init__(self, checkpoint_path="checkpoints/best_spert_phobert.pt", device=None):
        self.device = device or torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.model_name = "vinai/phobert-base-v2"
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
        self.max_span_length = 110
        self.entity_types = ENTITY_TYPES
        self.relation_types = RELATION_TYPES

        print(f"[*] Đang nạp mô hình PhoBERT-SpERT từ: {checkpoint_path}")
        print(f"[*] Thiết bị suy luận: {self.device}")

        checkpoint_data = None
        if os.path.exists(checkpoint_path):
            checkpoint_data = torch.load(checkpoint_path, map_location=self.device)
            self.entity_types = checkpoint_data.get("entity_types", ENTITY_TYPES)
            self.relation_types = checkpoint_data.get("relation_types", RELATION_TYPES)
            if "model_state_dict" in checkpoint_data and "size_embeddings.weight" in checkpoint_data["model_state_dict"]:
                self.max_span_length = checkpoint_data["model_state_dict"]["size_embeddings.weight"].shape[0] - 1

        self.id2entity = {i + 1: t for i, t in enumerate(self.entity_types)}
        self.id2rel = {i + 1: t for i, t in enumerate(self.relation_types)}

        self.model = PhoBERTSpeRT(
            model_name=self.model_name,
            num_entity_types=len(self.entity_types),
            num_relation_types=len(self.relation_types),
            max_span_length=self.max_span_length,
            size_embedding_dim=25
        ).to(self.device)

        if checkpoint_data:
            self.model.load_state_dict(checkpoint_data["model_state_dict"])
            print(f"[+] Đã nạp thành công trọng số checkpoint (Epoch {checkpoint_data.get('epoch', '?')})")
        else:
            print(f"[!] CẢNH BÁO: Không tìm thấy checkpoint {checkpoint_path}, chạy với trọng số mặc định.")

        self.model.eval()

    def _extract_single_chunk(self, words, word_offset=0, entity_threshold=0.35, relation_threshold=0.50):
        if not words:
            return [], []
        if len(words) > 175:
            words = words[:175]

        subword_ids = [self.tokenizer.bos_token_id]
        word_to_subword = []
        for word in words:
            tokens = self.tokenizer.encode(word, add_special_tokens=False)
            if not tokens:
                tokens = [self.tokenizer.unk_token_id]
            start_idx = len(subword_ids)
            subword_ids.extend(tokens)
            end_idx = len(subword_ids)
            word_to_subword.append((start_idx, end_idx))
        subword_ids.append(self.tokenizer.eos_token_id)

        # Đảm bảo không vượt quá giới hạn 256 subwords của PhoBERT
        if len(subword_ids) > 254:
            while word_to_subword and word_to_subword[-1][1] >= 254:
                word_to_subword.pop()
                words = words[:-1]
            subword_ids = subword_ids[: (word_to_subword[-1][1] if word_to_subword else 1)] + [self.tokenizer.eos_token_id]

        input_ids = torch.tensor([subword_ids], dtype=torch.long, device=self.device)
        attention_mask = torch.ones_like(input_ids, device=self.device)

        from data.dataset import generate_candidate_spans
        candidate_word_spans = generate_candidate_spans(words, self.max_span_length)
        subword_spans = []
        span_lengths = []
        for w_start, w_end in candidate_word_spans:
            sw_start = word_to_subword[w_start][0]
            sw_end = word_to_subword[w_end - 1][1]
            subword_spans.append((sw_start, sw_end))
            span_lengths.append(w_end - w_start)

        if not subword_spans:
            return [], []

        spans_tensor = torch.tensor([subword_spans], dtype=torch.long, device=self.device)
        lengths_tensor = torch.tensor([span_lengths], dtype=torch.long, device=self.device)

        with torch.no_grad():
            with torch.amp.autocast('cuda' if torch.cuda.is_available() else 'cpu'):
                outputs = self.model(
                    input_ids=input_ids,
                    attention_mask=attention_mask,
                    spans=spans_tensor,
                    span_lengths=lengths_tensor
                )
                ent_logits = outputs["entity_logits"][0]
                ent_probs = torch.softmax(ent_logits, dim=-1)

        raw_entities = []
        for idx in range(len(candidate_word_spans)):
            non_none_probs = ent_probs[idx, 1:]
            max_prob, best_cls_offset = torch.max(non_none_probs, dim=-1)
            best_cls = best_cls_offset.item() + 1
            conf = max_prob.item()

            if conf >= entity_threshold:
                w_start, w_end = candidate_word_spans[idx]
                ent_text = " ".join(words[w_start:w_end]).replace("_", " ")
                ent_text = re.sub(r"\s+([.,):;-])", r"\1", ent_text)
                ent_type = self.id2entity.get(best_cls, "UNKNOWN")
                raw_entities.append({
                    "span_idx": idx,
                    "text": ent_text,
                    "type": ent_type,
                    "span": (w_start + word_offset, w_end + word_offset),
                    "confidence": conf
                })

        detected_entities = non_max_suppression(raw_entities)

        detected_relations = []
        if len(detected_entities) >= 2:
            rel_pairs = []
            pair_ent_map = []
            for i, e1 in enumerate(detected_entities):
                for j, e2 in enumerate(detected_entities):
                    if i != j:
                        rel_pairs.append((e1["span_idx"], e2["span_idx"]))
                        pair_ent_map.append((e1, e2))

            rel_pairs_tensor = torch.tensor([rel_pairs], dtype=torch.long, device=self.device)

            with torch.no_grad():
                with torch.amp.autocast('cuda' if torch.cuda.is_available() else 'cpu'):
                    rel_outputs = self.model(
                        input_ids=input_ids,
                        attention_mask=attention_mask,
                        spans=spans_tensor,
                        span_lengths=lengths_tensor,
                        rel_pairs=rel_pairs_tensor
                    )
                    rel_logits = rel_outputs["relation_logits"][0]
                    rel_probs = torch.sigmoid(rel_logits)

            num_rel_classes = rel_probs.shape[-1]
            for p_idx in range(len(rel_pairs)):
                e1, e2 = pair_ent_map[p_idx]
                for r_offset in range(num_rel_classes):
                    conf = rel_probs[p_idx, r_offset].item()
                    if conf >= relation_threshold:
                        best_r_cls = r_offset + 1
                        rel_type = self.id2rel.get(best_r_cls, "UNKNOWN")
                        detected_relations.append({
                            "head": e1["text"],
                            "head_type": e1["type"],
                            "relation": rel_type,
                            "tail": e2["text"],
                            "tail_type": e2["type"],
                            "confidence": conf
                        })

        return detected_entities, detected_relations

    def extract_text(self, text, entity_threshold=0.35, relation_threshold=0.50):
        words = vi_tokenize(text)
        if len(words) == 0:
            return [], []

        if len(words) <= 145:
            return self._extract_single_chunk(words, 0, entity_threshold, relation_threshold)

        # Nếu đoạn văn dài (> 145 từ), chia thành các cửa sổ chồng lấp tại dấu chấm/chấm phẩy để không bỏ sót câu cuối
        all_ents, all_rels = [], []
        start_w = 0
        while start_w < len(words):
            end_w = min(len(words), start_w + 135)
            if end_w < len(words):
                # Tìm dấu câu gần nhất để ngắt tự nhiên
                for back in range(end_w, max(start_w + 60, end_w - 35), -1):
                    if words[back - 1] in (".", ";", ":"):
                        end_w = back
                        break
            c_ents, c_rels = self._extract_single_chunk(
                words[start_w:end_w],
                word_offset=start_w,
                entity_threshold=entity_threshold,
                relation_threshold=relation_threshold,
            )
            all_ents.extend(c_ents)
            all_rels.extend(c_rels)
            if end_w >= len(words):
                break
            start_w = end_w

        merged_ents = non_max_suppression(all_ents)
        return merged_ents, all_rels


# ======================================================================
# 3. Tai van ban tu Google Drive
# ======================================================================
def fetch_document_from_drive(doc_name=None, folder_id=None, cache_dir="data/drive_test_cache"):
    """
    Tai van ban tu Drive ve thu muc cache.
    Neu khong truyen folder_id hay doc_name, se tu dong chon mot van ban moi chua hoc tren Drive.
    """
    os.makedirs(cache_dir, exist_ok=True)

    target_folder_id = folder_id
    target_doc_name = doc_name

    # Neu chua chi dinh, tim 1 van ban nghi dinh moi tren Drive
    if not target_folder_id:
        print("[*] Đang duyệt thư mục Google Drive để chọn 1 văn bản thử nghiệm mới...")
        docs_nd = list_folder("1cspc_oK808d3dQA7VAvsaRoQ55XfmCEi")  # nghi_dinh folder
        if not docs_nd:
            raise RuntimeError("Không thể đọc thư mục trên Google Drive.")
        
        # Chon van ban nghi dinh 2020 tro lai day
        for fid, name, is_f in docs_nd:
            if is_f and "_2020_" in name:
                target_folder_id = fid
                target_doc_name = name
                break

    print(f"[+] Văn bản được chọn trên Google Drive: {target_doc_name}")
    print(f"    Folder ID: {target_folder_id}")

    # Neu tim thay truc tiep trong data/legal/raw/<cat>/<doc_name>
    for cat in ["bo_luat", "nghi_dinh", "quyet_dinh", "thong_tu"]:
        raw_cand = os.path.join("data", "legal", "raw", cat, target_doc_name)
        if os.path.exists(raw_cand) and os.path.exists(os.path.join(raw_cand, "noi_dung.docx")):
            print(f"[+] Tìm thấy văn bản trong kho dữ liệu cục bộ: {raw_cand}")
            downloaded = {f: os.path.join(raw_cand, f) for f in os.listdir(raw_cand) if os.path.isfile(os.path.join(raw_cand, f))}
            return target_doc_name, "raw_local", downloaded

    doc_dir = os.path.join(cache_dir, target_doc_name.replace("/", "_"))
    os.makedirs(doc_dir, exist_ok=True)

    # Neu da co san trong cache va khong truyen folder_id rieng
    if os.path.exists(os.path.join(doc_dir, "noi_dung.docx")) and (not folder_id or folder_id == "local"):
        print(f"[+] Tìm thấy tệp văn bản có sẵn trong bộ nhớ đệm: {doc_dir}")
        downloaded = {f: os.path.join(doc_dir, f) for f in os.listdir(doc_dir) if os.path.isfile(os.path.join(doc_dir, f))}
        return target_doc_name, "cached", downloaded

    # Lay danh sach file trong folder
    files = list_folder(target_folder_id)
    if not files:
        raise RuntimeError(f"Không thể lấy danh sách file trong folder {target_folder_id}")

    fmap = {n: fid for fid, n, _ in files}
    downloaded = {}

    for fname in ["thuoc_tinh.json", "noi_dung.docx", "muc_luc.json"]:
        if fname in fmap:
            dest = os.path.join(doc_dir, fname)
            print(f"    - Đang tải {fname}...")
            ok = download(fmap[fname], dest)
            if ok:
                downloaded[fname] = dest
            else:
                print(f"    [!] Tải thất bại: {fname}")

    return target_doc_name, target_folder_id, downloaded


# Ràng buộc pháp lý chuẩn hóa các cặp thực thể trong quan hệ (Legal Ontology Constraints)
OUTER_HUB_TYPES = {"HANH_VI_VI_PHAM", "NGHIA_VU_QUYEN", "HINH_PHAT_CHE_TAI", "BIEN_PHAP_KHAC_PHUC"}
INNER_SATELLITE_TYPES = {
    "CHU_THE_CA_NHAN", "TO_CHUC_DOANH_NGHIEP", "CO_QUAN_THAM_QUYEN",
    "GIAY_TO_HO_SO", "TAI_SAN_VAT_CHAT", "MUC_TIEN",
    "NGUONG_DINH_LUONG", "THOI_HAN", "DIA_DIEM",
    "THAM_CHIEU_PHAP_LY", "NGAY_THAM_CHIEU", "TU_KHOA_PHAP_LY", "LINH_VUC"
}
INTRA_SENTENCE_ENTITY_TYPES = OUTER_HUB_TYPES | INNER_SATELLITE_TYPES

VALID_RELATION_CONSTRAINTS = {
    # 6 Quan hệ cấu trúc & thuộc tính cấp văn bản
    "BAN_HANH_BOI": ({"SO_HIEU"}, {"CO_QUAN_BAN_HANH"}),
    "BAN_HANH_NGAY": ({"SO_HIEU"}, {"NGAY_BAN_HANH"}),
    "KY_BOI": ({"SO_HIEU"}, {"NGUOI_KY"}),
    "LA_LOAI_VAN_BAN": ({"SO_HIEU"}, {"LOAI_VAN_BAN"}),
    "GIU_CHUC_VU": ({"NGUOI_KY"}, {"CHUC_DANH_NGUOI_KY"}),
    "THUOC_VE": ({"DIEU", "KHOAN", "DIEM", "CHUONG"}, {"SO_HIEU", "CHUONG", "DIEU", "KHOAN"}),

    # 13 Quan hệ nội câu lấy Hub làm tâm + Đối chiếu điều khoản & Lĩnh vực (Intra-Sentence Knowledge Graph)
    "THUC_HIEN_VI_PHAM": ({"CHU_THE_CA_NHAN", "TO_CHUC_DOANH_NGHIEP"}, {"HANH_VI_VI_PHAM"}),
    "CO_NGHIA_VU_QUYEN": ({"CHU_THE_CA_NHAN", "TO_CHUC_DOANH_NGHIEP"}, {"NGHIA_VU_QUYEN"}),
    "CO_THAM_QUYEN": ({"CO_QUAN_THAM_QUYEN"}, {"HINH_PHAT_CHE_TAI", "BIEN_PHAP_KHAC_PHUC", "NGHIA_VU_QUYEN"}),
    "TAC_DONG_DOI_TUONG": ({"HANH_VI_VI_PHAM", "NGHIA_VU_QUYEN", "BIEN_PHAP_KHAC_PHUC", "HINH_PHAT_CHE_TAI"}, {"GIAY_TO_HO_SO", "TAI_SAN_VAT_CHAT"}),
    "TAC_DONG_CHU_THE": ({"HANH_VI_VI_PHAM", "NGHIA_VU_QUYEN", "BIEN_PHAP_KHAC_PHUC"}, {"CHU_THE_CA_NHAN", "TO_CHUC_DOANH_NGHIEP", "CO_QUAN_THAM_QUYEN"}),
    "DAN_DEN_CHE_TAI": ({"HANH_VI_VI_PHAM"}, {"HINH_PHAT_CHE_TAI", "BIEN_PHAP_KHAC_PHUC"}),
    "CHIU_CHE_TAI": ({"CHU_THE_CA_NHAN", "TO_CHUC_DOANH_NGHIEP"}, {"HINH_PHAT_CHE_TAI", "BIEN_PHAP_KHAC_PHUC"}),
    "CO_MUC_DINH_LUONG": ({"HINH_PHAT_CHE_TAI", "BIEN_PHAP_KHAC_PHUC", "HANH_VI_VI_PHAM", "NGHIA_VU_QUYEN", "TAI_SAN_VAT_CHAT"}, {"MUC_TIEN", "NGUONG_DINH_LUONG"}),
    "TRONG_THOI_HAN": ({"NGHIA_VU_QUYEN", "HANH_VI_VI_PHAM", "HINH_PHAT_CHE_TAI", "BIEN_PHAP_KHAC_PHUC"}, {"THOI_HAN"}),
    "DIEN_RA_TAI": ({"HANH_VI_VI_PHAM", "NGHIA_VU_QUYEN", "TO_CHUC_DOANH_NGHIEP", "HINH_PHAT_CHE_TAI"}, {"DIA_DIEM"}),
    "VIEN_DAN_THAM_CHIEU": (
        {
            "HANH_VI_VI_PHAM", "NGHIA_VU_QUYEN", "HINH_PHAT_CHE_TAI", "BIEN_PHAP_KHAC_PHUC",
            "DIEU", "KHOAN", "DIEM", "SO_HIEU", "LOAI_VAN_BAN",
            "CO_QUAN_THAM_QUYEN", "TO_CHUC_DOANH_NGHIEP", "CHU_THE_CA_NHAN", "GIAY_TO_HO_SO",
            "TU_KHOA_PHAP_LY",
        },
        {"THAM_CHIEU_PHAP_LY"},
    ),
    "NGAY_BAN_HANH_THAM_CHIEU": ({"THAM_CHIEU_PHAP_LY"}, {"NGAY_THAM_CHIEU"}),
    "THUOC_LINH_VUC": (
        {
            "SO_HIEU", "LOAI_VAN_BAN", "THAM_CHIEU_PHAP_LY",
            "DIEU", "KHOAN", "DIEM",
            "HANH_VI_VI_PHAM", "NGHIA_VU_QUYEN", "HINH_PHAT_CHE_TAI", "BIEN_PHAP_KHAC_PHUC",
            "CO_QUAN_THAM_QUYEN", "TO_CHUC_DOANH_NGHIEP", "CHU_THE_CA_NHAN", "GIAY_TO_HO_SO",
        },
        {"LINH_VUC"},
    ),
}


def _is_valid_boundary(text, s, e):
    left_ok = (s == 0) or (not text[s - 1].isalnum())
    right_ok = (e == len(text)) or (not text[e].isalnum())
    return left_ok and right_ok


def find_entity_span(text, etxt, start_pos=0):
    """
    Tìm vị trí chính xác của etxt trong text có kiểm tra ranh giới từ (word boundary),
    ngăn chặn triệt để lỗi 'Điều 1' khớp nhầm vào 'Điều 11' hoặc '1.' khớp vào '1.000.000'.
    """
    if not etxt or not text or start_pos >= len(text):
        return None
    # 1. Khớp chính xác có kiểm tra biên từ
    idx = text.find(etxt, start_pos)
    while idx != -1:
        end = idx + len(etxt)
        if _is_valid_boundary(text, idx, end):
            return idx, end
        idx = text.find(etxt, idx + 1)
    # 2. Khớp sau khi chuẩn hóa dấu câu (ví dụ '1 .' -> '1.')
    norm_txt = re.sub(r"\s+([.,):;-])", r"\1", etxt)
    idx = text.find(norm_txt, start_pos)
    while idx != -1:
        end = idx + len(norm_txt)
        if _is_valid_boundary(text, idx, end):
            return idx, end
        idx = text.find(norm_txt, idx + 1)
    # 3. Khớp biểu thức chính quy với khoảng trắng tùy chọn giữa các ký tự
    pattern_parts = [re.escape(tok) for tok in etxt.split()]
    pattern = r"\s*".join(pattern_parts)
    try:
        for m in re.finditer(pattern, text[start_pos:]):
            s, e = start_pos + m.start(), start_pos + m.end()
            if _is_valid_boundary(text, s, e):
                return s, e
    except Exception:
        pass
    return None


def safe_annotate_markdown(text, entities):
    """
    Gán nhãn Markdown hỗ trợ Thực thể Lồng nhau (Nested Entities) bằng Boundary Events.
    Hiển thị rõ cấu trúc: **[Outer ... **[Inner]**`{INNER}` ...]**`{OUTER}`.
    """
    if not entities:
        return text

    accepted_spans = []
    struct_containers = {"DIEU", "KHOAN", "DIEM"}
    # Sắp xếp thực thể dài trước (Outer Container / Hub trước), độ tự tin cao trước
    sorted_ents = sorted(
        entities,
        key=lambda e: (
            len(e["text"]),
            1 if e["type"] in struct_containers else (0 if e["type"] in OUTER_HUB_TYPES else -1),
            e.get("confidence", 0),
        ),
        reverse=True,
    )

    for ent in sorted_ents:
        etxt = ent["text"]
        etype = ent["type"]
        start = 0
        while True:
            res = find_entity_span(text, etxt, start)
            if not res:
                break
            s, e = res
            # Kiểm tra tương thích với các span đã chọn: rời nhau hoặc lồng nhau hợp lệ (3 tầng: DIEU/KHOAN/DIEM -> Hub -> Satellite)
            conflict = False
            for s2, e2, t2 in accepted_spans:
                if (s, e) == (s2, e2) and etype == t2:
                    conflict = True
                    break
                if max(s, s2) < min(e, e2):
                    if (s >= s2 and e <= e2) and etype != t2:
                        outer_t, inner_t = t2, etype
                    elif (s2 >= s and e2 <= e) and etype != t2:
                        outer_t, inner_t = etype, t2
                    else:
                        outer_t, inner_t = None, None
                    is_nested = bool(
                        outer_t
                        and (
                            (outer_t in struct_containers and inner_t not in struct_containers)
                            or (outer_t in OUTER_HUB_TYPES and inner_t not in (OUTER_HUB_TYPES | struct_containers))
                        )
                    )
                    if not is_nested:
                        conflict = True
                        break
            if not conflict:
                accepted_spans.append((s, e, etype))
                break
            start = s + 1

    if not accepted_spans:
        return text

    def _nest_rank(tp):
        if tp in struct_containers:
            return 0
        if tp in OUTER_HUB_TYPES:
            return 1
        return 2

    from collections import defaultdict
    open_events = defaultdict(list)
    close_events = defaultdict(list)
    for s, e, etype in accepted_spans:
        open_events[s].append((e - s, _nest_rank(etype), etype))
        close_events[e].append((e - s, _nest_rank(etype), etype))

    for pos in open_events:
        open_events[pos].sort(key=lambda x: (-x[0], x[1]))   # Span dài / Container mở trước
    for pos in close_events:
        close_events[pos].sort(key=lambda x: (x[0], -x[1]))  # Span ngắn / Inner đóng trước

    out = []
    for idx in range(len(text) + 1):
        if idx in close_events:
            for _, _, etype in close_events[idx]:
                out.append(f"]**`{{{etype}}}`")
        if idx in open_events:
            for _, _, _ in open_events[idx]:
                out.append("**[")
        if idx < len(text):
            out.append(text[idx])

    extra_md = []
    for ent in entities:
        if not find_entity_span(text, ent["text"]):
            extra_md.append(f" **[{ent['text']}]**`{{{ent['type']}}}`")
    return "".join(out) + "".join(extra_md)


# ======================================================================
# 4. Xuat ket qua ra file Markdown (.md)
# ======================================================================
def export_to_markdown(
    doc_name,
    folder_id,
    metadata,
    all_entities,
    all_relations,
    target_paras,
    inference_time,
    output_md_path
):
    print(f"[*] Đang xuất báo cáo kết quả trích xuất sang: {output_md_path}")
    num_paras = len(target_paras) if isinstance(target_paras, list) else target_paras


    # Thong ke theo loai thuc the
    ent_type_counter = {}
    for ent in all_entities:
        ent_type_counter[ent["type"]] = ent_type_counter.get(ent["type"], 0) + 1

    # Thong ke theo loai quan he
    rel_type_counter = {}
    for rel in all_relations:
        rel_type_counter[rel["relation"]] = rel_type_counter.get(rel["relation"], 0) + 1

    # Trich xuat cac node chinh cho bieu do Mermaid
    mermaid_lines = []
    mermaid_lines.append("```mermaid")
    mermaid_lines.append("graph TD")
    mermaid_lines.append(f'    Doc["📄 {doc_name}"]:::docClass')

    added_nodes = set()
    added_edges = set()

    for r in all_relations[:25]:  # Gioi han top 25 quan he de bieu do de nhin
        h_clean = re.sub(r'["\n]', '', r["head"])[:25]
        t_clean = re.sub(r'["\n]', '', r["tail"])[:25]
        rel_label = r["relation"]

        h_id = f"N_{abs(hash(h_clean)) % 10000}"
        t_id = f"N_{abs(hash(t_clean)) % 10000}"

        if h_id not in added_nodes:
            mermaid_lines.append(f'    {h_id}["{h_clean}"]')
            added_nodes.add(h_id)
        if t_id not in added_nodes:
            mermaid_lines.append(f'    {t_id}["{t_clean}"]')
            added_nodes.add(t_id)

        edge_key = (h_id, t_id, rel_label)
        if edge_key not in added_edges:
            mermaid_lines.append(f'    {h_id} -->|"{rel_label}"| {t_id}')
            added_edges.add(edge_key)

    mermaid_lines.append("    classDef docClass fill:#1f77b4,stroke:#0d47a1,stroke-width:2px,color:#fff;")
    mermaid_lines.append("```")
    mermaid_str = "\n".join(mermaid_lines)

    detected_lvs = []
    for ent in all_entities:
        if ent["type"] == "LINH_VUC" and ent["text"] not in detected_lvs:
            detected_lvs.append(ent["text"])
    attr_lv = metadata.get("attributes", {}).get("linh_vuc", "").strip(" ;.")
    attr_ng = metadata.get("attributes", {}).get("nganh", "").strip(" ;.")
    if attr_lv not in ("", "--", "Chưa phân loại", "Khác") and attr_lv not in detected_lvs:
        detected_lvs.insert(0, attr_lv)
    elif attr_ng not in ("", "--", "Chưa phân loại", "Khác") and attr_ng not in detected_lvs:
        detected_lvs.insert(0, attr_ng)
    linh_vuc_display = ", ".join(detected_lvs) if detected_lvs else "N/A"

    # Trích xuất danh sách tất cả người ký kèm chức danh tương ứng từ mô hình
    extracted_signers = []
    signer_titles = {}
    for r in all_relations:
        if r.get("relation") == "GIU_CHUC_VU":
            signer_titles[r["head"]] = r["tail"]

    seen_nk = set()
    for e in all_entities:
        if e.get("type") == "NGUOI_KY":
            nk_name = e["text"]
            if nk_name not in seen_nk:
                seen_nk.add(nk_name)
                title = signer_titles.get(nk_name)
                if title:
                    extracted_signers.append(f"{nk_name} ({title})")
                else:
                    extracted_signers.append(nk_name)

    if extracted_signers:
        nguoi_ky_display = "; ".join(extracted_signers)
    else:
        nk_attr = metadata.get('attributes', {}).get('nguoi_ky', 'N/A')
        cd_attr = metadata.get('attributes', {}).get('chuc_danh_nguoi_ky', '')
        nguoi_ky_display = f"{nk_attr} ({cd_attr})" if cd_attr else nk_attr

    lines = [
        f"# Báo Cáo Trích Xuất Thực Thể & Quan Hệ Pháp Luật (Joint NER & RE)",
        f"> **Tệp nguồn thử nghiệm từ Google Drive**: `{doc_name}`",
        f"> **Thời gian thực hiện**: {time.strftime('%Y-%m-%d %H:%M:%S')}",
        f"",
        f"---",
        f"",
        f"## 1. Thông Tin Văn Bản & Môi Trường Thử Nghiệm",
        f"",
        f"- **Mã văn bản**: `{doc_name}`",
        f"- **Google Drive Folder ID**: `{folder_id}`",
        f"- **Số hiệu**: `{metadata.get('attributes', {}).get('so_hieu', metadata.get('metadata', {}).get('number', 'N/A'))}`",
        f"- **Tiêu đề văn bản**: {metadata.get('metadata', {}).get('title', 'N/A')}",
        f"- **Cơ quan ban hành**: {metadata.get('attributes', {}).get('co_quan_ban_hanh', 'N/A')}",
        f"- **Lĩnh vực pháp lý**: {linh_vuc_display}",
        f"- **Người ký**: {nguoi_ky_display}",
        f"- **Mô hình suy luận**: `PhoBERT-SpERT` (Boundary + Union Context + Biaffine + BCEWithLogitsLoss)",
        f"- **Thời gian xử lý toàn bộ**: **{inference_time:.2f} giây** ({num_paras} đoạn văn bản)",
        f"",
        f"---",
        f"",
        f"## 2. Bảng Tổng Quan Kết Quả Trích Xuất",
        f"",
        f"| Chỉ Số Tổng Hợp | Số Lượng Đạt Được | Ghi Chú |",
        f"| :--- | :---: | :--- |",
        f"| **Tổng số đoạn phân tích** | **{num_paras}** | Tự động đọc từ file `noi_dung.docx` |",

        f"| **Tổng số thực thể phát hiện** | **{len(all_entities)}** | Đã áp dụng Nested-Aware NMS (Hỗ trợ thực thể lồng nhau) |",
        f"| **Tổng số quan hệ liên kết** | **{len(all_relations)}** | Bao gồm cả quan hệ cấu trúc và quan hệ nội câu lấy Hub làm tâm |",
        f"",
        f"### Phân Bố Thực Thể Theo Nhãn Loại",
        f"",
        f"| Nhãn Thực Thể | Ý Nghĩa Pháp Lý | Số Lượng Phát Hiện | Tỷ Lệ (%) |",
        f"| :--- | :--- | :---: | :---: |"
    ]

    ENT_DESC = {
        "SO_HIEU": "Số hiệu văn bản",
        "LOAI_VAN_BAN": "Loại văn bản",
        "CO_QUAN_BAN_HANH": "Cơ quan ban hành",
        "NGAY_BAN_HANH": "Ngày ban hành (văn bản hiện hành)",
        "NGUOI_KY": "Người ký",
        "CHUC_DANH_NGUOI_KY": "Chức danh người ký",
        "CHUONG": "Chương trong văn bản",
        "DIEU": "Điều trong văn bản",
        "KHOAN": "Khoản trong văn bản",
        "DIEM": "Điểm trong văn bản",
        "HANH_VI_VI_PHAM": "[Hub] Hành vi vi phạm pháp luật",
        "NGHIA_VU_QUYEN": "[Hub] Nghĩa vụ / Quyền / Thủ tục pháp lý",
        "HINH_PHAT_CHE_TAI": "[Hub] Chế tài xử phạt",
        "BIEN_PHAP_KHAC_PHUC": "[Hub] Biện pháp khắc phục hậu quả",
        "CHU_THE_CA_NHAN": "Chủ thể cá nhân / Vai trò pháp lý",
        "TO_CHUC_DOANH_NGHIEP": "Tổ chức / Pháp nhân / Doanh nghiệp",
        "CO_QUAN_THAM_QUYEN": "Cơ quan / Chức danh có thẩm quyền",
        "GIAY_TO_HO_SO": "Hồ sơ / Giấy tờ hành chính / Bằng cấp",
        "TAI_SAN_VAT_CHAT": "Tài sản / Phương tiện / Tang vật / Tiền lương",
        "MUC_TIEN": "Mức tiền phạt / Giá trị tiền tệ",
        "NGUONG_DINH_LUONG": "Ngưỡng định lượng / Tỷ lệ / Số lượng",
        "THOI_HAN": "Thời hạn / Khoảng thời gian",
        "DIA_DIEM": "Địa điểm / Không gian pháp lý",
        "THAM_CHIEU_PHAP_LY": "Điều khoản đối chiếu / Viện dẫn pháp lý",
        "NGAY_THAM_CHIEU": "Ngày ban hành của văn bản tham chiếu",
        "TU_KHOA_PHAP_LY": "Từ khóa pháp lý / Động từ lập pháp neo tham chiếu",
        "LINH_VUC": "Lĩnh vực pháp lý / Ngành, lĩnh vực điều chỉnh",
    }
    REL_DESC = {
        "BAN_HANH_BOI": "Được ban hành bởi cơ quan (SO_HIEU -> CO_QUAN_BAN_HANH)",
        "BAN_HANH_NGAY": "Được ban hành vào ngày (SO_HIEU -> NGAY_BAN_HANH)",
        "KY_BOI": "Được ký bởi người ký (SO_HIEU -> NGUOI_KY)",
        "LA_LOAI_VAN_BAN": "Là loại văn bản (SO_HIEU -> LOAI_VAN_BAN)",
        "GIU_CHUC_VU": "Giữ chức vụ người ký (NGUOI_KY -> CHUC_DANH_NGUOI_KY)",
        "THUOC_VE": "Thuộc về cấu trúc phân cấp (DIEM -> KHOAN -> DIEU -> CHUONG -> SO_HIEU)",
        "THUC_HIEN_VI_PHAM": "[Nội câu] Chủ thể thực hiện hành vi vi phạm",
        "CO_NGHIA_VU_QUYEN": "[Nội câu] Chủ thể có nghĩa vụ / quyền thực hiện hành vi",
        "CO_THAM_QUYEN": "[Nội câu] Cơ quan / Chức danh có thẩm quyền xử lý",
        "TAC_DONG_DOI_TUONG": "[Nội câu] Hành vi / Biện pháp tác động lên tài sản / giấy tờ",
        "TAC_DONG_CHU_THE": "[Nội câu] Hành vi tác động đến chủ thể khác",
        "DAN_DEN_CHE_TAI": "[Nội câu] Hành vi vi phạm dẫn đến chế tài xử phạt / khắc phục",
        "CHIU_CHE_TAI": "[Nội câu] Chủ thể chịu chế tài xử phạt trực tiếp",
        "CO_MUC_DINH_LUONG": "[Nội câu] Có mức tiền phạt hoặc ngưỡng định lượng",
        "TRONG_THOI_HAN": "[Nội câu] Ràng buộc trong thời hạn / khoảng thời gian",
        "DIEN_RA_TAI": "[Nội câu] Diễn ra tại địa điểm / không gian pháp lý",
        "VIEN_DAN_THAM_CHIEU": "[Nội câu] Đối chiếu / Viện dẫn đến điều khoản khác",
        "NGAY_BAN_HANH_THAM_CHIEU": "[Nội câu] Ngày ban hành của văn bản tham chiếu",
        "THUOC_LINH_VUC": "[Nội câu / Thuộc tính] Thuộc lĩnh vực pháp lý điều chỉnh",
    }

    total_ent = len(all_entities) if all_entities else 1
    for k, v in sorted(ent_type_counter.items(), key=lambda x: x[1], reverse=True):
        desc = ENT_DESC.get(k, f"Nhãn `{k}`")
        lines.append(f"| **{k}** | {desc} | {v} | {(v / total_ent) * 100:.1f}% |")

    lines.extend([
        f"",
        f"### Phân Bố Quan Hệ Theo Nhãn Loại",
        f"",
        f"| Loại Quan Hệ | Ý Nghĩa Pháp Lý | Số Lượng Phát Hiện | Tỷ Lệ (%) |",
        f"| :--- | :--- | :---: | :---: |"
    ])

    total_rel = len(all_relations) if all_relations else 1
    for k, v in sorted(rel_type_counter.items(), key=lambda x: x[1], reverse=True):
        desc = REL_DESC.get(k, f"Quan hệ `{k}`")
        lines.append(f"| **{k}** | {desc} | {v} | {(v / total_rel) * 100:.1f}% |")

    lines.extend([
        f"",
        f"---",
        f"",
        f"## 3. Sơ Đồ Cấu Trúc Quan Hệ Trích Xuất (Mermaid Graph)",
        f"",
        mermaid_str,
        f"",
        f"---",
        f"",
        f"## 4. Chi Tiết Danh Sách Thực Thể Được Trích Xuất (Toàn Bộ 100% Nội Dung)",
        f"",
        f"| STT | Loại Thực Thể | Tên / Trích Đoạn Thực Thể | Vị Trí (Span) | Độ Tin Cậy (Conf) | Ngữ Cảnh Đầy Đủ (Không Cắt Chữ) |",
        f"| :---: | :--- | :--- | :---: | :---: | :--- |"
    ])


    for i, ent in enumerate(all_entities, 1):
        clean_ctx = re.sub(r"\s+", " ", ent.get("context", "")).replace("|", "\\|").strip()
        ent_txt = ent["text"]
        if ent_txt in clean_ctx:
            highlighted_ctx = clean_ctx.replace(ent_txt, f"**[{ent_txt}]**", 1)
        else:
            highlighted_ctx = clean_ctx
        lines.append(f"| {i} | `{ent['type']}` | **{ent['text']}** | `{ent['span']}` | `{ent['confidence']:.2%}` | {highlighted_ctx} |")

    lines.extend([
        f"",
        f"---",
        f"",
        f"## 5. Chi Tiết Danh Sách Quan Hệ Được Trích Xuất",
        f"",
        f"| STT | Thực Thể Nguồn (Head) | Loại Head | Quan Hệ (Relation) | Thực Thể Đích (Tail) | Loại Tail | Độ Tin Cậy |",
        f"| :---: | :--- | :---: | :---: | :--- | :---: | :---: |"
    ])

    for i, rel in enumerate(all_relations, 1):
        lines.append(f"| {i} | **{rel['head']}** | `{rel['head_type']}` | ➔ **`{rel['relation']}`** ➔ | **{rel['tail']}** | `{rel['tail_type']}` | `{rel['confidence']:.2%}` |")

    # 6. Che do doc toan van kem gan nhan
    lines.extend([
        f"",
        f"---",
        f"",
        f"## 6. Đọc Toàn Văn Văn Bản Gốc Kèm Gán Nhãn Thực Thể (In-line Annotation)",
        f"",
        f"> Dưới đây là toàn bộ văn bản gốc 100% không cắt bớt chữ. Các thực thể nhận dạng được đánh dấu nổi bật `**[Tên thực thể]**{{LOAI}}` để bạn đối chiếu kiểm tra chính xác.",

        f""
    ])

    para_ent_map = {}
    for ent in all_entities:
        pidx = ent.get("para_idx", 1)
        para_ent_map.setdefault(pidx, []).append(ent)

    for p_idx, text in enumerate(target_paras if isinstance(target_paras, list) else [], 1):
        clean_text = re.sub(r"\s+", " ", text).strip()
        if not clean_text:
            continue
        p_ents = para_ent_map.get(p_idx, [])
        if p_ents:
            annotated = safe_annotate_markdown(clean_text, p_ents)
            lines.append(f"- **[Đoạn {p_idx}]**: {annotated}\n")
        else:
            lines.append(f"- [Đoạn {p_idx}]: {clean_text}\n")

    lines.extend([
        f"",
        f"---",
        f"",
        f"*Báo cáo được khởi tạo tự động bởi mô hình PhoBERT-SpERT của đề tài NCKH.*"
    ])

    content = "\n".join(lines)
    os.makedirs(os.path.dirname(os.path.abspath(output_md_path)), exist_ok=True)
    with open(output_md_path, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"[THÀNH CÔNG] Đã ghi tệp markdown hoàn chỉnh tại: {output_md_path}")

    # Xuat file HTML tuong tac di kem
    try:
        from visualize_document import build_html_viewer
        base_out = os.path.splitext(output_md_path)[0]
        html_path = base_out + ".html"
        paras_list = target_paras if isinstance(target_paras, list) else []
        build_html_viewer(doc_name, metadata, all_entities, all_relations, paras_list, html_path)
    except Exception as e:
        print(f"[!] Không tạo được HTML viewer: {e}")


# ======================================================================
# 5. Hàm xử lý một văn bản (Single Document Processing)
# ======================================================================
def process_single_document(
    doc_name="306_2025_NĐ-CP_186388",
    folder_id="1b9ghl3Dn4aKTmrsX5YbhAv1JIWGwdYY0",
    checkpoint="checkpoints/best_spert_phobert.pt",
    output_md=None,
    max_paras=0,
    extractor=None,
):
    # 1. Tai van ban tu Google Drive hoac local cache
    doc_name, folder_id, files = fetch_document_from_drive(
        doc_name=doc_name,
        folder_id=folder_id
    )


    output_md_path = output_md if output_md else os.path.join("outputs", f"ket_qua_trich_xuat_{doc_name}.md")

    metadata = {}
    if "thuoc_tinh.json" in files:
        with open(files["thuoc_tinh.json"], "r", encoding="utf-8") as f:
            metadata = json.load(f)

    if "noi_dung.docx" not in files:
        raise FileNotFoundError("Không tìm thấy noi_dung.docx trong thư mục văn bản tải từ Drive.")

    # 2. Doc noi dung doan van ban tu docx
    paras = read_docx_paragraphs(files["noi_dung.docx"])
    print(f"[+] Đã đọc {len(paras)} đoạn văn từ tệp nội dung docx.")

    # Chon danh sach doan phan tich (neu <= 0 thi phan tich toan bo van ban)
    if max_paras and max_paras > 0:
        target_paras = paras[:max_paras]
    else:
        target_paras = paras
    print(f"[+] Sẽ chạy phân tích mô hình trên toàn bộ {len(target_paras)}/{len(paras)} đoạn văn bản.")

    # 3. Khoi tao mo hinh PhoBERT-SpERT neu chua truyen tu ngoai vao
    if extractor is None:
        extractor = LegalExtractor(checkpoint_path=checkpoint)


    # 4. Chay suy luan
    t0 = time.time()
    all_entities = []
    all_relations = []

    print("[*] Bắt đầu suy luận thực thể và quan hệ thông minh (Khối Tiêu đề + Khối Chữ ký + Thân văn bản)...")

    # (A) Khối Tiêu đề (Header Block): Gộp các dòng đầu trước "Căn cứ" / "Điều 1" để mô hình bắt SO_HIEU, CO_QUAN, LOAI_VB, NGAY cùng quan hệ
    header_stop_re = re.compile(r"^(Căn cứ|Theo đề nghị|Xét đề nghị|Điều 1\b|Chương [IVX1]|Để |Phần [IVX1])", re.I)
    loai_vb_line_re = re.compile(r"^(BỘ LUẬT|LUẬT|NGHỊ ĐỊNH|QUYẾT ĐỊNH|THÔNG TƯ|NGHỊ QUYẾT|CHỈ THỊ|PHÁP LỆNH)\b", re.I)
    header_paras = []
    header_end_idx = 0
    for idx, p in enumerate(paras[:14]):
        if header_stop_re.match(p):
            header_end_idx = idx
            break
        header_paras.append((idx, p))
        header_end_idx = idx + 1
        # Sau dòng tên loại văn bản chính thức (NGHỊ ĐỊNH / THÔNG TƯ / QUYẾT ĐỊNH...), dòng tiếp theo là trích yếu
        if idx >= 1 and len(p.strip().split()) <= 4 and loai_vb_line_re.match(p.strip()):
            break

    detected_so_hieu = None
    if header_paras:
        clean_header_items = []
        for idx, p in header_paras:
            if idx == 0:
                m = re.match(r"^((?:Bộ\s+luật|Luật|Nghị\s+định|Quyết\s+định|Thông\s+tư|Nghị\s+quyết)\s+(?:[^0-9]{0,25}?\s+)?(?:số\s+)?\d+\S*)", p, re.I)
                clean_header_items.append((idx, m.group(1) if m else p))
            elif idx >= 1 and len(p.strip().split()) <= 4 and loai_vb_line_re.match(p.strip()):
                m = loai_vb_line_re.match(p.strip())
                clean_header_items.append((idx, m.group(1)))
            else:
                clean_header_items.append((idx, p))

        head_text = " . ".join(txt for _, txt in clean_header_items)
        print(f"  [+] Đang phân tích Khối Tiêu đề ({len(header_paras)} dòng)...")
        h_ents, h_rels = extractor.extract_text(head_text, entity_threshold=0.30, relation_threshold=0.25)

        # Lọc nghiêm ngặt: Chỉ nhận diện các thuộc tính tiêu đề văn bản chuẩn
        allowed_head_types = {"SO_HIEU", "CO_QUAN_BAN_HANH", "LOAI_VAN_BAN", "NGAY_BAN_HANH"}
        h_ents = [e for e in h_ents if e["type"] in allowed_head_types]

        # Ánh xạ thực thể vào đúng từng đoạn văn bản xuất hiện thực tế (loại trừ duplicate)
        for p_offset, p_eval_text in clean_header_items:
            p_idx = p_offset + 1
            p_orig_text = paras[p_offset]
            seen = set()
            for e in h_ents:
                if find_entity_span(p_eval_text, e["text"]) and (e["text"], e["type"]) not in seen:
                    seen.add((e["text"], e["type"]))
                    e_copy = dict(e)
                    e_copy["para_idx"] = p_idx
                    e_copy["context"] = p_orig_text
                    all_entities.append(e_copy)
                    if e_copy["type"] == "SO_HIEU" and not detected_so_hieu:
                        detected_so_hieu = e_copy["text"]

        # Lọc các quan hệ hợp lệ của phần tiêu đề theo ontology
        seen_rels = set()
        for r in h_rels:
            rtype = r["relation"]
            if rtype in VALID_RELATION_CONSTRAINTS:
                vh, vt = VALID_RELATION_CONSTRAINTS[rtype]
                if r["head_type"] in vh and r["tail_type"] in vt and r["head"] != r["tail"]:
                    r_key = (r["head"], rtype, r["tail"])
                    if r_key not in seen_rels:
                        seen_rels.add(r_key)
                        r["para_idx"] = 1
                        all_relations.append(r)

        # Bổ sung ngày ban hành và cơ quan ban hành từ thuộc tính văn bản nếu noi_dung.docx khuyết bảng tiêu đề
        attrs = metadata.get("attributes", {})
        cq_raw = attrs.get("co_quan_ban_hanh", "").strip()
        if cq_raw and not any(e["type"] == "CO_QUAN_BAN_HANH" for e in all_entities):
            all_entities.append({
                "text": cq_raw,
                "type": "CO_QUAN_BAN_HANH",
                "span": (0, 0),
                "confidence": 0.99,
                "para_idx": 1,
                "context": f"[Bổ sung từ thuộc tính văn bản]: {cq_raw}"
            })
            if detected_so_hieu:
                all_relations.append({
                    "head": detected_so_hieu,
                    "head_type": "SO_HIEU",
                    "relation": "BAN_HANH_BOI",
                    "tail": cq_raw,
                    "tail_type": "CO_QUAN_BAN_HANH",
                    "confidence": 0.99,
                    "para_idx": 1
                })

        nbh_raw = attrs.get("ngay_ban_hanh", "")
        has_main_date = any(e["type"] == "NGAY_BAN_HANH" for e in all_entities)
        if not has_main_date and re.match(r"^\d{4}-\d{2}-\d{2}$", nbh_raw):
            y, m, d = map(int, nbh_raw.split("-"))
            date_str = f"ngày {d:02d} tháng {m:02d} năm {y}"
            all_entities.append({
                "text": date_str,
                "type": "NGAY_BAN_HANH",
                "span": (0, 0),
                "confidence": 0.99,
                "para_idx": 1,
                "context": f"[Bổ sung từ thuộc tính văn bản]: {date_str}"
            })
            if detected_so_hieu:
                all_relations.append({
                    "head": detected_so_hieu,
                    "head_type": "SO_HIEU",
                    "relation": "BAN_HANH_NGAY",
                    "tail": date_str,
                    "tail_type": "NGAY_BAN_HANH",
                    "confidence": 0.99,
                    "para_idx": 1
                })

        bad_lv_vals = {"", "--", "Chưa phân loại", "Khác"}
        lv_attr = attrs.get("linh_vuc", "").strip(" ;.")
        ng_attr = attrs.get("nganh", "").strip(" ;.")
        lv_meta_val = lv_attr if lv_attr not in bad_lv_vals else (ng_attr if ng_attr not in bad_lv_vals else "")
        if lv_meta_val and not any(e["type"] == "LINH_VUC" for e in all_entities):
            all_entities.append({
                "text": lv_meta_val,
                "type": "LINH_VUC",
                "span": (0, 0),
                "confidence": 0.99,
                "para_idx": 1,
                "context": f"[Bổ sung từ thuộc tính văn bản]: {lv_meta_val}"
            })
            if detected_so_hieu:
                all_relations.append({
                    "head": detected_so_hieu,
                    "head_type": "SO_HIEU",
                    "relation": "THUOC_LINH_VUC",
                    "tail": lv_meta_val,
                    "tail_type": "LINH_VUC",
                    "confidence": 0.99,
                    "para_idx": 1
                })
        print(f"      -> Tiêu đề: tìm thấy {len(all_entities)} thực thể, {len(all_relations)} quan hệ.")

    # (B) Khối Chữ ký (Signature Block): Hỗ trợ văn bản có nhiều người ký (ban hành + sao y/xác thực, liên tịch)
    sig_mark_re = re.compile(
        r"^(?:KT\.|TM\.|TL\.|TUQ\.|Q\.|K/T|T/M|\(Đã ký\)|\(đã ký\)|Đã ký:|CHỦ TỊCH|PHÓ CHỦ TỊCH|THỦ TƯỚNG|PHÓ THỦ TƯỚNG|BỘ TRƯỞNG|THỨ TRƯỞNG|CHỦ NHIỆM|PHÓ CHỦ NHIỆM|CHÁNH ÁN|VIỆN TRƯỞNG|TỔNG KIỂM TOÁN|GIÁM ĐỐC|SAO Y)\b",
        re.I,
    )
    body_marker_re = re.compile(
        r"^(?:Điều|Đỉều|Khoản|Điểm|Căn cứ|Theo đề nghị|Xét đề nghị|QUYẾT ĐỊNH:|NGHỊ ĐỊNH:|THÔNG TƯ:|\d+\.|[a-zđ]\))\b",
        re.I,
    )

    # Khối chữ ký chỉ được phép xuất hiện SAU Điều cuối cùng / đoạn văn dài cuối cùng của phần thân
    last_body_idx = header_end_idx - 1
    for idx_p in range(header_end_idx, len(paras)):
        p_txt = paras[idx_p].strip()
        if sig_mark_re.search(p_txt) or re.search(r"(\(đã ký\)|đã ký:)", p_txt, re.I):
            continue
        if body_marker_re.match(p_txt) or len(p_txt.split()) > 15:
            last_body_idx = idx_p

    tail_start_idx = max(header_end_idx, last_body_idx + 1, len(paras) - 35)

    noi_nhan_re = re.compile(r"^(?:Nơi nhận:?|- Như (?:trên|Điều)|- Lưu:|\bLưu VT\b)", re.I)
    tail_raw_items = []
    for idx_p in range(tail_start_idx, len(paras)):
        p_txt = paras[idx_p].strip()
        if not p_txt:
            continue
        if noi_nhan_re.match(p_txt) or header_stop_re.match(p_txt):
            continue
        if len(p_txt.split()) > 30 and not re.search(r"(\(đã ký\)|đã ký:)", p_txt, re.I):
            continue
        tail_raw_items.append((idx_p + 1, p_txt))

    def split_signature_blocks(tail_items):
        blocks = []
        current_block = []
        for pidx, ptxt in tail_items:
            is_new_start = False
            if current_block:
                curr_text = " ".join(t for _, t in current_block)
                has_signer = bool(re.search(r"(\(đã ký\)|đã ký:)", curr_text, re.I))
                if re.match(r"^(?:SAO Y|Số:\s*\d+/SY-)", ptxt, re.I):
                    is_new_start = True
                elif sig_mark_re.match(ptxt) and (has_signer or len(current_block) >= 3):
                    is_new_start = True
            if is_new_start:
                blocks.append(current_block)
                current_block = [(pidx, ptxt)]
            else:
                current_block.append((pidx, ptxt))
        if current_block:
            blocks.append(current_block)
        return blocks

    all_cand_blocks = split_signature_blocks(tail_raw_items)
    sig_blocks = []
    for b in all_cand_blocks:
        b_txt = " ".join(t for _, t in b)
        if sig_mark_re.search(b_txt) or re.search(r"(\(đã ký\)|đã ký:)", b_txt, re.I):
            sig_blocks.append(b)

    sig_first_para_idx = sig_blocks[0][0][0] if sig_blocks else None
    total_sig_ents = 0

    if sig_blocks:
        print(f"  [+] Đang phân tích {len(sig_blocks)} Khối Chữ ký ở cuối văn bản...")
        for b in sig_blocks:
            sig_text = " . ".join(ptxt for _, ptxt in b)
            s_ents, s_rels = extractor.extract_text(sig_text, entity_threshold=0.30, relation_threshold=0.25)
            # Chỉ lấy NGUOI_KY và CHUC_DANH_NGUOI_KY trong khối chữ ký
            s_ents = [e for e in s_ents if e["type"] in ("NGUOI_KY", "CHUC_DANH_NGUOI_KY")]

            # Ánh xạ từng thực thể chữ ký vào đúng đoạn xuất hiện thực tế
            for e in s_ents:
                matched_pidx = b[0][0]
                matched_ctx = sig_text
                for pidx_cand, ptxt_cand in b:
                    if find_entity_span(ptxt_cand, e["text"]):
                        matched_pidx = pidx_cand
                        matched_ctx = ptxt_cand
                        break
                e["para_idx"] = matched_pidx
                e["context"] = matched_ctx
                all_entities.append(e)
                total_sig_ents += 1

            # Quan hệ NGUOI_KY -> GIU_CHUC_VU -> CHUC_DANH_NGUOI_KY
            for r in s_rels:
                rtype = r["relation"]
                if rtype in VALID_RELATION_CONSTRAINTS:
                    vh, vt = VALID_RELATION_CONSTRAINTS[rtype]
                    if r["head_type"] in vh and r["tail_type"] in vt and r["head"] != r["tail"]:
                        r["para_idx"] = b[0][0]
                        all_relations.append(r)

            # Quan hệ SO_HIEU -> KY_BOI -> NGUOI_KY
            if detected_so_hieu:
                for e in s_ents:
                    if e["type"] == "NGUOI_KY":
                        all_relations.append({
                            "head": detected_so_hieu,
                            "head_type": "SO_HIEU",
                            "relation": "KY_BOI",
                            "tail": e["text"],
                            "tail_type": "NGUOI_KY",
                            "confidence": e["confidence"],
                            "para_idx": e["para_idx"]
                        })
        print(f"      -> Chữ ký: tìm thấy {total_sig_ents} thực thể từ {len(sig_blocks)} khối ký.")

    # Bổ sung người ký và chức danh từ thuộc tính văn bản nếu noi_dung.docx khuyết bảng chữ ký cuối bài
    if not any(e["type"] == "NGUOI_KY" for e in all_entities):
        attrs = metadata.get("attributes", {})
        nk_raw = attrs.get("nguoi_ky", "").strip()
        cd_raw = attrs.get("chuc_danh_nguoi_ky", "").strip()
        last_pidx = len(paras) if paras else 1
        if cd_raw and not any(e["type"] == "CHUC_DANH_NGUOI_KY" for e in all_entities):
            all_entities.append({
                "text": cd_raw,
                "type": "CHUC_DANH_NGUOI_KY",
                "span": (0, 0),
                "confidence": 0.99,
                "para_idx": last_pidx,
                "context": f"[Bổ sung từ thuộc tính văn bản]: {cd_raw}"
            })
        if nk_raw:
            all_entities.append({
                "text": nk_raw,
                "type": "NGUOI_KY",
                "span": (0, 0),
                "confidence": 0.99,
                "para_idx": last_pidx,
                "context": f"[Bổ sung từ thuộc tính văn bản]: {nk_raw}"
            })
            if detected_so_hieu:
                all_relations.append({
                    "head": detected_so_hieu,
                    "head_type": "SO_HIEU",
                    "relation": "KY_BOI",
                    "tail": nk_raw,
                    "tail_type": "NGUOI_KY",
                    "confidence": 0.99,
                    "para_idx": last_pidx
                })
            if cd_raw:
                all_relations.append({
                    "head": nk_raw,
                    "head_type": "NGUOI_KY",
                    "relation": "GIU_CHUC_VU",
                    "tail": cd_raw,
                    "tail_type": "CHUC_DANH_NGUOI_KY",
                    "confidence": 0.99,
                    "para_idx": last_pidx
                })

    # (C) Phân tích Thân văn bản (Body Paragraphs)
    doc_lexicon = extract_document_self_lexicon(paras)
    body_end = (sig_first_para_idx - 1) if sig_first_para_idx else len(paras)
    if max_paras and max_paras > 0:
        body_end = min(body_end, max_paras)


    body_paras_to_process = paras[header_end_idx:body_end]
    print(f"  [+] Đang phân tích Thân văn bản: {len(body_paras_to_process)} đoạn (từ đoạn {header_end_idx + 1} đến đoạn {body_end})...")

    target_paras = paras

    cur_chuong_short = None
    cur_chuong_text = None
    cur_dieu_short = None
    cur_dieu_text = None
    cur_khoan_short = None
    cur_khoan_text = None

    chuong_re = re.compile(r"^(?:(?:Chương|Phần)\s+[IVX0-9]+[a-z]?(?:[.:\s]|$)|Chương\s+[IVX0-9]+)", re.I)
    dieu_re = re.compile(r"^(?:Điều|Đỉều)\s+(\d+[a-z]?)(?:[.:]|\b)", re.I)
    khoan_re = re.compile(r"^(?:Khoản\s+(\d+[a-z]?)[.:,]?|(\d+)\.)(?:\s+|$)", re.I)
    diem_re = re.compile(r"^[“\"]?(?:Điểm\s+([a-zđ]\d?)[.):,]?|([a-zđ]\d?)[),]|(\([ivx]+\)))(?:\s+|$)", re.I)

    for p_offset, text in enumerate(body_paras_to_process):
        p_idx = header_end_idx + p_offset + 1
        clean_text = text.strip()
        if len(clean_text) < 3:
            continue

        m_c = chuong_re.match(clean_text)
        if m_c and len(clean_text.split()) <= 20:
            cur_chuong_text = clean_text
            cur_chuong_short = clean_text
            all_entities.append({
                "text": clean_text,
                "type": "CHUONG",
                "span": (0, len(clean_text)),
                "confidence": 0.99,
                "para_idx": p_idx,
                "context": clean_text,
            })
            if detected_so_hieu:
                all_relations.append({
                    "head": clean_text,
                    "head_type": "CHUONG",
                    "relation": "THUOC_VE",
                    "tail": detected_so_hieu,
                    "tail_type": "SO_HIEU",
                    "confidence": 0.99,
                    "para_idx": p_idx
                })
            continue

        m_d = dieu_re.match(clean_text)
        m_k = khoan_re.match(clean_text)
        m_p = diem_re.match(clean_text)

        prefix = ""
        para_struct_type = None
        para_struct_short = None
        if m_d:
            cur_dieu_short = f"Điều {m_d.group(1)}"
            cur_dieu_text = clean_text

            cur_khoan_short = None
            cur_khoan_text = None
            para_struct_type = "DIEU"
            para_struct_short = cur_dieu_short
            eval_text = clean_text
        elif m_k:
            k_num = m_k.group(1) or m_k.group(2)
            cur_khoan_short = f"{k_num}."
            cur_khoan_text = clean_text
            para_struct_type = "KHOAN"
            para_struct_short = cur_khoan_short
            if cur_dieu_short:
                prefix = f"{cur_dieu_short} . "
                eval_text = prefix + clean_text
            else:
                eval_text = clean_text
        elif m_p:
            p_sym = m_p.group(3) or f"{m_p.group(1) or m_p.group(2)})"
            para_struct_type = "DIEM"
            para_struct_short = p_sym
            if cur_dieu_short and cur_khoan_short:
                prefix = f"{cur_dieu_short} . {cur_khoan_short} . "
                eval_text = prefix + clean_text
            else:
                eval_text = clean_text
        else:
            eval_text = clean_text

        prefix_tok_len = len(vi_tokenize(prefix)) if prefix else 0
        clean_tok_len = len(vi_tokenize(clean_text))
        ents, rels = extractor.extract_text(eval_text, entity_threshold=0.35, relation_threshold=0.45)

        allowed_body_types = {"DIEU", "KHOAN", "DIEM"} | INTRA_SENTENCE_ENTITY_TYPES
        valid_dieu_txt_re = re.compile(r"^(?:Điều|Đỉều)\s+\d+[a-z]?$", re.I)
        valid_khoan_txt_re = re.compile(r"^(?:Khoản\s+\d+[a-z]?[.:,]?|\d+\.)$", re.I)
        valid_diem_txt_re = re.compile(r"^(?:Điểm\s+[a-zđ]\d?[.):,]?|[a-zđ]\d?[),]|(?:\([ivx]+\)))$", re.I)

        body_ents = []
        struct_conf = 0.98
        for e in ents:
            # Loại bỏ tuyệt đối các thực thể nằm trong phần prefix nhân tạo (tránh 'Điều 1' trong prefix rò rỉ vào 'Điều 11')
            if prefix and e["span"][0] < prefix_tok_len:
                continue
            et = e["type"]
            if et not in allowed_body_types:
                continue
            etxt_s = e["text"].strip()
            etxt_low = etxt_s.lower()
            if et == "HINH_PHAT_CHE_TAI" and etxt_low == "xử phạt vi phạm hành chính":
                if "bị xử phạt vi phạm hành chính" not in clean_text.lower():
                    continue
            if et == "TO_CHUC_DOANH_NGHIEP":
                if etxt_low in ("tổ chức vi phạm", "tổ chức bị xử phạt", "tổ chức, cá nhân", "cá nhân, tổ chức"):
                    continue
                if etxt_low.startswith("hội đồng nhân dân"):
                    e = dict(e, type="CO_QUAN_THAM_QUYEN")
                    et = "CO_QUAN_THAM_QUYEN"
                elif etxt_low == "doanh nghiệp":
                    if any(
                        p in clean_text.lower()
                        for p in ("luật doanh nghiệp", "trái phiếu doanh nghiệp", "đăng ký doanh nghiệp", "thuế thu nhập doanh nghiệp", "quản trị doanh nghiệp")
                    ):
                        continue
            elif et == "CHU_THE_CA_NHAN":
                if etxt_low in ("thành viên lưu ký", "thành viên bù trừ", "thành viên giao dịch", "thành viên lập quỹ"):
                    e = dict(e, type="TO_CHUC_DOANH_NGHIEP")
                    et = "TO_CHUC_DOANH_NGHIEP"
            elif et == "MUC_TIEN":
                if not re.search(r"đồng|vnđ|usd|đô\s+la|ngoại\s+tệ|tiền|tỷ|triệu|nghìn|ngàn", etxt_low):
                    e = dict(e, type="NGUONG_DINH_LUONG")
                    et = "NGUONG_DINH_LUONG"
            elif et == "TAI_SAN_VAT_CHAT":
                if etxt_low == "tách biệt tài sản":
                    e = dict(e, text="tài sản")
                    etxt_s = "tài sản"
                    etxt_low = "tài sản"
            if et == "DIEU":
                if m_d and e["span"][0] <= prefix_tok_len + 1:
                    struct_conf = max(struct_conf, e["confidence"])
                    continue
                if not valid_dieu_txt_re.match(etxt_s):
                    continue
                # Điều nằm giữa câu hoặc trong ngoặc kép sửa đổi là THAM_CHIEU_PHAP_LY
                e = dict(e)
                e["type"] = "THAM_CHIEU_PHAP_LY"
            elif et == "KHOAN":
                if m_k and e["span"][0] <= prefix_tok_len + 1:
                    struct_conf = max(struct_conf, e["confidence"])
                    continue
                if not valid_khoan_txt_re.match(etxt_s):
                    continue
                if etxt_s.lower().startswith("khoản"):
                    e = dict(e)
                    e["type"] = "THAM_CHIEU_PHAP_LY"
                else:
                    continue
            elif et == "DIEM":
                if m_p and e["span"][0] <= prefix_tok_len + 1:
                    struct_conf = max(struct_conf, e["confidence"])
                    continue
                if not valid_diem_txt_re.match(etxt_s):
                    continue
                if etxt_s.lower().startswith("điểm"):
                    e = dict(e)
                    e["type"] = "THAM_CHIEU_PHAP_LY"
                else:
                    continue
            if e["type"] == "THAM_CHIEU_PHAP_LY":
                cleaned_ref = re.sub(r"\s+(?:vào\s+sau|vào\s+trước|vào|tại|của|sau)$", "", e["text"].strip(), flags=re.I)
                if cleaned_ref != e["text"]:
                    e = dict(e, text=cleaned_ref)
            body_ents.append(e)

        # Lấy trọn vẹn toàn bộ đoạn văn của từng Điều / Khoản / Điểm làm thực thể cấu trúc bao ngoài (Outer Structural Span)
        if para_struct_type:
            body_ents.insert(0, {
                "text": clean_text,
                "type": para_struct_type,
                "span": (prefix_tok_len, prefix_tok_len + clean_tok_len),
                "confidence": struct_conf,
            })

        entity_remap = {}
        intra_cands = extract_intra_sentence_spans(clean_text, base_offset=0, existing_spans=[], doc_lexicon=doc_lexicon)
        for cs, ce, ctype in intra_cands:
            if ctype not in (
                "THAM_CHIEU_PHAP_LY", "TU_KHOA_PHAP_LY", "NGAY_THAM_CHIEU", "LINH_VUC",
                "HANH_VI_VI_PHAM", "GIAY_TO_HO_SO", "CO_QUAN_THAM_QUYEN", "TO_CHUC_DOANH_NGHIEP",
                "CHU_THE_CA_NHAN", "TAI_SAN_VAT_CHAT",
            ):
                continue
            cand_txt = clean_text[cs:ce].strip()
            if not cand_txt:
                continue
            rel_tok_s = len(vi_tokenize(clean_text[:cs])) if cs > 0 else 0
            rel_tok_e = rel_tok_s + len(vi_tokenize(cand_txt))
            cand_tok_s = prefix_tok_len + rel_tok_s
            cand_tok_e = prefix_tok_len + rel_tok_e

            if ctype == "THAM_CHIEU_PHAP_LY":
                # Loại bỏ mọi thực thể vệ tinh con ngắn hơn nằm trọn bên trong THAM_CHIEU_PHAP_LY (VD: 'Doanh nghiệp' trong 'Luật Doanh nghiệp số 59/2020/QH14')
                enclosed_indices = []
                already_exact = False
                for idx_be, be in enumerate(body_ents):
                    if be["type"] not in OUTER_HUB_TYPES and be["type"] not in ("DIEU", "KHOAN", "DIEM"):
                        be_s, be_e = be["span"]
                        sp_be = find_entity_span(clean_text, be["text"])
                        tok_in = (be_s >= cand_tok_s and be_e <= cand_tok_e)
                        char_in = bool(sp_be and sp_be[0] >= cs and sp_be[1] <= ce)
                        if tok_in or char_in:
                            if ((be_s, be_e) == (cand_tok_s, cand_tok_e) or sp_be == (cs, ce)) and be["type"] == "THAM_CHIEU_PHAP_LY":
                                already_exact = True
                            else:
                                enclosed_indices.append(idx_be)
                                entity_remap[be["text"]] = (cand_txt, "THAM_CHIEU_PHAP_LY")
                if enclosed_indices:
                    for idx_rem in reversed(enclosed_indices):
                        body_ents.pop(idx_rem)
                if not already_exact:
                    overlap_any = False
                    for be in body_ents:
                        if be["type"] not in OUTER_HUB_TYPES and be["type"] not in ("DIEU", "KHOAN", "DIEM"):
                            be_s, be_e = be["span"]
                            if max(cand_tok_s, be_s) < min(cand_tok_e, be_e):
                                overlap_any = True
                                break
                    if not overlap_any:
                        body_ents.append({
                            "text": cand_txt,
                            "type": "THAM_CHIEU_PHAP_LY",
                            "span": (cand_tok_s, cand_tok_e),
                            "confidence": 0.96,
                        })
            elif ctype == "LINH_VUC":
                # Loại bỏ các thực thể vệ tinh con (VD: TAI_SAN_VAT_CHAT 'chứng khoán') bị bắt nhầm bên trong cụm LINH_VUC
                enclosed_lv = []
                already_lv = False
                for idx_be, be in enumerate(body_ents):
                    if be["type"] not in OUTER_HUB_TYPES and be["type"] not in ("DIEU", "KHOAN", "DIEM", "THAM_CHIEU_PHAP_LY"):
                        be_s, be_e = be["span"]
                        sp_be = find_entity_span(clean_text, be["text"])
                        if (be_s >= cand_tok_s and be_e <= cand_tok_e) or (sp_be and sp_be[0] >= cs and sp_be[1] <= ce):
                            if ((be_s, be_e) == (cand_tok_s, cand_tok_e) or sp_be == (cs, ce)) and be["type"] == "LINH_VUC":
                                already_lv = True
                            else:
                                enclosed_lv.append(idx_be)
                                entity_remap[be["text"]] = (cand_txt, "LINH_VUC")
                        elif be["type"] == "TAI_SAN_VAT_CHAT" and be["text"].lower() in cand_txt.lower() and max(cand_tok_s, be_s) < min(cand_tok_e, be_e):
                            enclosed_lv.append(idx_be)
                            entity_remap[be["text"]] = (cand_txt, "LINH_VUC")
                for idx_rem in reversed(enclosed_lv):
                    body_ents.pop(idx_rem)
                if not already_lv:
                    body_ents.append({
                        "text": cand_txt,
                        "type": "LINH_VUC",
                        "span": (cand_tok_s, cand_tok_e),
                        "confidence": 0.96,
                    })
            elif ctype == "TU_KHOA_PHAP_LY":
                enclosed_kw = []
                already_kw = False
                for idx_be, be in enumerate(body_ents):
                    if be["type"] == "TU_KHOA_PHAP_LY":
                        be_s, be_e = be["span"]
                        sp_be = find_entity_span(clean_text, be["text"])
                        if max(cand_tok_s, be_s) < min(cand_tok_e, be_e) or (sp_be and max(cs, sp_be[0]) < min(ce, sp_be[1])):
                            if len(be["text"]) >= len(cand_txt):
                                already_kw = True
                            else:
                                enclosed_kw.append(idx_be)
                                entity_remap[be["text"]] = (cand_txt, "TU_KHOA_PHAP_LY")
                for idx_rem in reversed(enclosed_kw):
                    body_ents.pop(idx_rem)
                if not already_kw:
                    body_ents.append({
                        "text": cand_txt,
                        "type": "TU_KHOA_PHAP_LY",
                        "span": (cand_tok_s, cand_tok_e),
                        "confidence": 0.96,
                    })
            elif ctype == "NGAY_THAM_CHIEU":
                if not any(be["type"] == "NGAY_THAM_CHIEU" and be["text"] == cand_txt for be in body_ents):
                    body_ents.append({
                        "text": cand_txt,
                        "type": "NGAY_THAM_CHIEU",
                        "span": (cand_tok_s, cand_tok_e),
                        "confidence": 0.96,
                    })
            elif ctype == "HANH_VI_VI_PHAM":
                # Thay thế thực thể HANH_VI_VI_PHAM ngắn kiểu keyword bằng mệnh đề hành vi vi phạm đầy đủ
                enclosed_hubs = []
                already_hub = False
                for idx_be, be in enumerate(body_ents):
                    if be["type"] == "HANH_VI_VI_PHAM":
                        be_s, be_e = be["span"]
                        sp_be = find_entity_span(clean_text, be["text"])
                        if max(cand_tok_s, be_s) < min(cand_tok_e, be_e) or (sp_be and max(cs, sp_be[0]) < min(ce, sp_be[1])):
                            if len(be["text"]) >= len(cand_txt):
                                already_hub = True
                            else:
                                enclosed_hubs.append(idx_be)
                                entity_remap[be["text"]] = (cand_txt, "HANH_VI_VI_PHAM")
                for idx_rem in reversed(enclosed_hubs):
                    body_ents.pop(idx_rem)
                if not already_hub:
                    body_ents.append({
                        "text": cand_txt,
                        "type": "HANH_VI_VI_PHAM",
                        "span": (cand_tok_s, cand_tok_e),
                        "confidence": 0.95,
                    })
            elif ctype in ("GIAY_TO_HO_SO", "CO_QUAN_THAM_QUYEN", "TO_CHUC_DOANH_NGHIEP", "CHU_THE_CA_NHAN", "TAI_SAN_VAT_CHAT"):
                enclosed_sat = []
                already_sat = False
                max_replaced_conf = 0.95
                for idx_be, be in enumerate(body_ents):
                    if be["type"] not in OUTER_HUB_TYPES and be["type"] not in ("DIEU", "KHOAN", "DIEM", "THAM_CHIEU_PHAP_LY", "LINH_VUC"):
                        be_s, be_e = be["span"]
                        tok_enclosed = (be_s >= cand_tok_s and be_e <= cand_tok_e)
                        tok_overlap_sub = (max(cand_tok_s, be_s) < min(cand_tok_e, be_e) and be["text"].lower() in cand_txt.lower())
                        if tok_enclosed or tok_overlap_sub:
                            if (be_s, be_e) == (cand_tok_s, cand_tok_e) and be["type"] == ctype and be["text"].lower() == cand_txt.lower():
                                already_sat = True
                            elif len(be["text"]) < len(cand_txt) or (be["text"].lower() == cand_txt.lower() and be["type"] != ctype):
                                enclosed_sat.append(idx_be)
                                max_replaced_conf = max(max_replaced_conf, be.get("confidence", 0.95))
                                entity_remap[be["text"]] = (cand_txt, ctype)
                    elif be["type"] in OUTER_HUB_TYPES:
                        # Nếu Outer Hub (VD: 'nộp hồ sơ đề nghị', 'nộp lại Giấy đăng ký') bị cắt cụt đúng tại ranh giới thực thể vệ tinh cũ, mở rộng luôn Outer Hub để bao trọn thực thể vệ tinh mới
                        hub_s, hub_e = be["span"]
                        if hub_s < cand_tok_s and cand_tok_s < hub_e < cand_tok_e:
                            sp_hub = find_entity_span(clean_text, be["text"])
                            if sp_hub and sp_hub[0] < cs and cs < sp_hub[1] < ce:
                                new_hub_txt = clean_text[sp_hub[0]:ce].strip()
                                old_hub_txt = be["text"]
                                body_ents[idx_be] = dict(
                                    be,
                                    text=new_hub_txt,
                                    span=(hub_s, cand_tok_e),
                                )
                                entity_remap[old_hub_txt] = (new_hub_txt, be["type"])
                for idx_rem in reversed(enclosed_sat):
                    body_ents.pop(idx_rem)
                if not already_sat and not any(
                    be["type"] not in OUTER_HUB_TYPES
                    and be["type"] not in ("DIEU", "KHOAN", "DIEM")
                    and max(cand_tok_s, be["span"][0]) < min(cand_tok_e, be["span"][1])
                    for be in body_ents
                ):
                    body_ents.append({
                        "text": cand_txt,
                        "type": ctype,
                        "span": (cand_tok_s, cand_tok_e),
                        "confidence": max_replaced_conf,
                    })

        # Lọc chặt NGAY_THAM_CHIEU: Chỉ giữ các ngày đứng ngay sau một thực thể THAM_CHIEU_PHAP_LY trong cùng đoạn
        ref_spans_in_para = []
        for be in body_ents:
            if be["type"] == "THAM_CHIEU_PHAP_LY":
                sp_r = find_entity_span(clean_text, be["text"])
                if sp_r:
                    ref_spans_in_para.append(sp_r)
        filtered_body_ents = []
        for be in body_ents:
            if be["type"] == "NGAY_THAM_CHIEU":
                sp_d = find_entity_span(clean_text, be["text"])
                if not sp_d or not any(sr[1] <= sp_d[0] and (sp_d[0] - sr[1]) <= 35 for sr in ref_spans_in_para):
                    continue
            filtered_body_ents.append(be)
        body_ents = filtered_body_ents

        for e in body_ents:
            e["para_idx"] = p_idx
            e["context"] = clean_text
            all_entities.append(e)

            # Cập nhật context Điều / Khoản hiện tại và liên kết quan hệ cấu trúc phân cấp (THUOC_VE)
            if e["type"] == "DIEU":
                if cur_chuong_text:
                    all_relations.append({
                        "head": e["text"],
                        "head_type": "DIEU",
                        "relation": "THUOC_VE",
                        "tail": cur_chuong_text,
                        "tail_type": "CHUONG",
                        "confidence": e["confidence"],
                        "para_idx": p_idx
                    })
                elif detected_so_hieu:
                    all_relations.append({
                        "head": e["text"],
                        "head_type": "DIEU",
                        "relation": "THUOC_VE",
                        "tail": detected_so_hieu,
                        "tail_type": "SO_HIEU",
                        "confidence": e["confidence"],
                        "para_idx": p_idx
                    })

            elif e["type"] == "KHOAN" and cur_dieu_text:
                all_relations.append({
                    "head": e["text"],
                    "head_type": "KHOAN",
                    "relation": "THUOC_VE",
                    "tail": cur_dieu_text,
                    "tail_type": "DIEU",
                    "confidence": e["confidence"],
                    "para_idx": p_idx
                })
            elif e["type"] == "DIEM" and cur_khoan_text:
                all_relations.append({
                    "head": e["text"],
                    "head_type": "DIEM",
                    "relation": "THUOC_VE",
                    "tail": cur_khoan_text,
                    "tail_type": "KHOAN",
                    "confidence": e["confidence"],
                    "para_idx": p_idx
                })

        seen_body_rels = set()
        body_ent_type_map = {be["text"]: be["type"] for be in body_ents}
        non_penalty_hubs_in_para = [be for be in body_ents if be["type"] in ("HANH_VI_VI_PHAM", "BIEN_PHAP_KHAC_PHUC", "NGHIA_VU_QUYEN")]
        for r in rels:
            rtype = r["relation"]
            if para_struct_short and r["head"] == para_struct_short:
                r = dict(r, head=clean_text, head_type=para_struct_type)
            if para_struct_short and r["tail"] == para_struct_short:
                r = dict(r, tail=clean_text, tail_type=para_struct_type)
            if r["head"] in entity_remap:
                new_h, new_ht = entity_remap[r["head"]]
                r = dict(r, head=new_h, head_type=new_ht)
            if r["tail"] in entity_remap:
                new_t, new_tt = entity_remap[r["tail"]]
                r = dict(r, tail=new_t, tail_type=new_tt)
            # Cập nhật lại head_type / tail_type nếu thực thể đã được chuẩn hóa
            if r["head"] in body_ent_type_map:
                r = dict(r, head_type=body_ent_type_map[r["head"]])
            if r["tail"] in body_ent_type_map:
                r = dict(r, tail_type=body_ent_type_map[r["tail"]])

            if prefix and (r["head"] in (cur_dieu_short, cur_khoan_short) and r["head"] not in body_ent_type_map):
                continue
            # Tránh nhầm lẫn giữa HINH_PHAT_CHE_TAI (Phạt tiền...) với mức độ/thời hạn của HANH_VI_VI_PHAM
            if rtype in ("TRONG_THOI_HAN", "CO_MUC_DINH_LUONG") and r["head_type"] == "HINH_PHAT_CHE_TAI" and "phạt tiền" in r["head"].lower():
                if r["tail"] not in r["head"]:
                    if non_penalty_hubs_in_para:
                        r = dict(r, head=non_penalty_hubs_in_para[0]["text"], head_type=non_penalty_hubs_in_para[0]["type"])
                    else:
                        continue
            if rtype == "THUOC_VE":
                continue
            elif rtype == "NGAY_BAN_HANH_THAM_CHIEU" and r["head_type"] == "THAM_CHIEU_PHAP_LY" and r["tail_type"] == "NGAY_THAM_CHIEU":
                if r["head"] in body_ent_type_map and r["tail"] in body_ent_type_map:
                    r_key = (r["head"], rtype, r["tail"])
                    if r_key not in seen_body_rels:
                        seen_body_rels.add(r_key)
                        r["para_idx"] = p_idx
                        all_relations.append(r)
            elif rtype in VALID_RELATION_CONSTRAINTS and rtype not in ("BAN_HANH_BOI", "BAN_HANH_NGAY", "KY_BOI", "LA_LOAI_VAN_BAN", "GIU_CHUC_VU", "THUOC_VE"):
                vh, vt = VALID_RELATION_CONSTRAINTS[rtype]
                if r["head_type"] in vh and r["tail_type"] in vt and r["head"] != r["tail"]:
                    if r["head"] in body_ent_type_map and r["tail"] in body_ent_type_map:
                        r_key = (r["head"], rtype, r["tail"])
                        if r_key not in seen_body_rels:
                            seen_body_rels.add(r_key)
                            r["para_idx"] = p_idx
                            all_relations.append(r)

        # Liên kết các thực thể GIAY_TO_HO_SO / TAI_SAN_VAT_CHAT / TO_CHUC_DOANH_NGHIEP / CHU_THE_CA_NHAN nằm lồng bên trong Outer Hub
        for hub_ent in [be for be in body_ents if be["type"] in OUTER_HUB_TYPES]:
            hs, he = hub_ent["span"]
            for sat_ent in body_ents:
                if sat_ent["text"] == hub_ent["text"]:
                    continue
                ss, se = sat_ent["span"]
                if ss >= hs and se <= he:
                    if sat_ent["type"] in ("GIAY_TO_HO_SO", "TAI_SAN_VAT_CHAT"):
                        r_key = (hub_ent["text"], "TAC_DONG_DOI_TUONG", sat_ent["text"])
                        if r_key not in seen_body_rels:
                            seen_body_rels.add(r_key)
                            all_relations.append({
                                "head": hub_ent["text"],
                                "head_type": hub_ent["type"],
                                "relation": "TAC_DONG_DOI_TUONG",
                                "tail": sat_ent["text"],
                                "tail_type": sat_ent["type"],
                                "confidence": min(hub_ent.get("confidence", 0.95), sat_ent.get("confidence", 0.95)),
                                "para_idx": p_idx,
                            })
                    elif sat_ent["type"] in ("TO_CHUC_DOANH_NGHIEP", "CHU_THE_CA_NHAN", "CO_QUAN_THAM_QUYEN"):
                        r_key = (hub_ent["text"], "TAC_DONG_CHU_THE", sat_ent["text"])
                        if r_key not in seen_body_rels:
                            seen_body_rels.add(r_key)
                            all_relations.append({
                                "head": hub_ent["text"],
                                "head_type": hub_ent["type"],
                                "relation": "TAC_DONG_CHU_THE",
                                "tail": sat_ent["text"],
                                "tail_type": sat_ent["type"],
                                "confidence": min(hub_ent.get("confidence", 0.95), sat_ent.get("confidence", 0.95)),
                                "para_idx": p_idx,
                            })

        # Liên kết TU_KHOA_PHAP_LY -> VIEN_DAN_THAM_CHIEU -> THAM_CHIEU_PHAP_LY trong cùng đoạn
        kw_ents_in_para = [be for be in body_ents if be["type"] == "TU_KHOA_PHAP_LY"]
        ref_ents_in_para = [be for be in body_ents if be["type"] == "THAM_CHIEU_PHAP_LY"]
        for re_ent in ref_ents_in_para:
            ref_txt = re_ent["text"]
            sp_r = find_entity_span(clean_text, ref_txt) or (0, 0)
            preceding_kws = []
            for kw_ent in kw_ents_in_para:
                sp_kw = find_entity_span(clean_text, kw_ent["text"]) or (0, 0)
                if sp_kw[1] <= sp_r[0] and (sp_r[0] - sp_kw[1]) <= 120:
                    preceding_kws.append((sp_kw[1], kw_ent))
            if preceding_kws:
                best_kw = max(preceding_kws, key=lambda x: x[0])[1]
                r_key = (best_kw["text"], "VIEN_DAN_THAM_CHIEU", ref_txt)
                if r_key not in seen_body_rels:
                    seen_body_rels.add(r_key)
                    all_relations.append({
                        "head": best_kw["text"],
                        "head_type": "TU_KHOA_PHAP_LY",
                        "relation": "VIEN_DAN_THAM_CHIEU",
                        "tail": ref_txt,
                        "tail_type": "THAM_CHIEU_PHAP_LY",
                        "confidence": best_kw.get("confidence", 0.96),
                        "para_idx": p_idx,
                    })

        # Đảm bảo mọi thực thể THAM_CHIEU_PHAP_LY trong đoạn cũng được kết nối quan hệ VIEN_DAN_THAM_CHIEU tới Hub hoặc Đơn vị cấu trúc / Số hiệu văn bản
        hub_ents_in_para = [be for be in body_ents if be["type"] in OUTER_HUB_TYPES]
        struct_ents_in_para = [be for be in body_ents if be["type"] in ("DIEM", "KHOAN", "DIEU")]
        subj_ents_in_para = [be for be in body_ents if be["type"] in ("CO_QUAN_THAM_QUYEN", "TO_CHUC_DOANH_NGHIEP", "CHU_THE_CA_NHAN", "GIAY_TO_HO_SO")]

        for be in body_ents:
            if be["type"] != "THAM_CHIEU_PHAP_LY":
                continue
            ref_txt = be["text"]
            if any(
                rk[1] == "VIEN_DAN_THAM_CHIEU"
                and rk[2] == ref_txt
                and body_ent_type_map.get(rk[0]) != "TU_KHOA_PHAP_LY"
                for rk in seen_body_rels
            ):
                continue

            head_txt, head_tp = None, None
            if hub_ents_in_para:
                # Chọn Hub gần nhất với cụm tham chiếu trong câu
                sp_ref = find_entity_span(clean_text, ref_txt) or (0, 0)
                best_hub = min(
                    hub_ents_in_para,
                    key=lambda h: abs((find_entity_span(clean_text, h["text"]) or (0, 0))[0] - sp_ref[0])
                )
                head_txt, head_tp = best_hub["text"], best_hub["type"]
            elif struct_ents_in_para:
                # Ưu tiên DIEM -> KHOAN -> DIEU ngay trong đoạn
                order_map = {"DIEM": 0, "KHOAN": 1, "DIEU": 2}
                best_st = sorted(struct_ents_in_para, key=lambda s: order_map.get(s["type"], 9))[0]
                head_txt, head_tp = best_st["text"], best_st["type"]
            elif cur_khoan_text:
                head_txt, head_tp = cur_khoan_text, "KHOAN"
            elif cur_dieu_text:
                head_txt, head_tp = cur_dieu_text, "DIEU"
            elif detected_so_hieu:
                head_txt, head_tp = detected_so_hieu, "SO_HIEU"
            elif subj_ents_in_para:
                head_txt, head_tp = subj_ents_in_para[0]["text"], subj_ents_in_para[0]["type"]

            if head_txt and head_txt != ref_txt:
                r_key = (head_txt, "VIEN_DAN_THAM_CHIEU", ref_txt)
                if r_key not in seen_body_rels:
                    seen_body_rels.add(r_key)
                    all_relations.append({
                        "head": head_txt,
                        "head_type": head_tp,
                        "relation": "VIEN_DAN_THAM_CHIEU",
                        "tail": ref_txt,
                        "tail_type": "THAM_CHIEU_PHAP_LY",
                        "confidence": be.get("confidence", 0.94),
                        "para_idx": p_idx,
                    })

        # Đảm bảo các thực thể LINH_VUC trong đoạn được liên kết THUOC_LINH_VUC tới văn bản tham chiếu / văn bản hiện hành / Hub / Điều khoản
        lv_ents_in_para = [be for be in body_ents if be["type"] == "LINH_VUC"]
        for lv_ent in lv_ents_in_para:
            lv_txt = lv_ent["text"]
            sp_lv = find_entity_span(clean_text, lv_txt) or (0, 0)
            # 1. Liên kết từ THAM_CHIEU_PHAP_LY đứng gần nhất phía trước (nếu có)
            cand_refs_lv = []
            for re_ent in ref_ents_in_para:
                sp_r = find_entity_span(clean_text, re_ent["text"]) or (0, 0)
                if sp_r[1] <= sp_lv[0] and (sp_lv[0] - sp_r[1]) <= 140:
                    cand_refs_lv.append((sp_r[1], re_ent))
            if cand_refs_lv:
                best_ref_lv = max(cand_refs_lv, key=lambda x: x[0])[1]
                r_key = (best_ref_lv["text"], "THUOC_LINH_VUC", lv_txt)
                if r_key not in seen_body_rels:
                    seen_body_rels.add(r_key)
                    all_relations.append({
                        "head": best_ref_lv["text"],
                        "head_type": "THAM_CHIEU_PHAP_LY",
                        "relation": "THUOC_LINH_VUC",
                        "tail": lv_txt,
                        "tail_type": "LINH_VUC",
                        "confidence": lv_ent.get("confidence", 0.96),
                        "para_idx": p_idx,
                    })
            # 2. Liên kết với Hub hoặc Đơn vị cấu trúc / Số hiệu văn bản hiện hành
            if hub_ents_in_para:
                best_hub_lv = min(
                    hub_ents_in_para,
                    key=lambda h: abs((find_entity_span(clean_text, h["text"]) or (0, 0))[0] - sp_lv[0])
                )
                r_key = (best_hub_lv["text"], "THUOC_LINH_VUC", lv_txt)
                if r_key not in seen_body_rels:
                    seen_body_rels.add(r_key)
                    all_relations.append({
                        "head": best_hub_lv["text"],
                        "head_type": best_hub_lv["type"],
                        "relation": "THUOC_LINH_VUC",
                        "tail": lv_txt,
                        "tail_type": "LINH_VUC",
                        "confidence": lv_ent.get("confidence", 0.95),
                        "para_idx": p_idx,
                    })
            if detected_so_hieu:
                r_key = (detected_so_hieu, "THUOC_LINH_VUC", lv_txt)
                if r_key not in seen_body_rels:
                    seen_body_rels.add(r_key)
                    all_relations.append({
                        "head": detected_so_hieu,
                        "head_type": "SO_HIEU",
                        "relation": "THUOC_LINH_VUC",
                        "tail": lv_txt,
                        "tail_type": "LINH_VUC",
                        "confidence": lv_ent.get("confidence", 0.96),
                        "para_idx": p_idx,
                    })

        # Đảm bảo các thực thể NGAY_THAM_CHIEU đi liền sau THAM_CHIEU_PHAP_LY đều được liên kết NGAY_BAN_HANH_THAM_CHIEU
        date_ents_in_para = [be for be in body_ents if be["type"] == "NGAY_THAM_CHIEU"]
        for de in date_ents_in_para:
            d_txt = de["text"]
            if any(rk[1] == "NGAY_BAN_HANH_THAM_CHIEU" and rk[2] == d_txt for rk in seen_body_rels):
                continue
            sp_date = find_entity_span(clean_text, d_txt) or (0, 0)
            cand_refs = []
            for re_ent in ref_ents_in_para:
                sp_r = find_entity_span(clean_text, re_ent["text"]) or (0, 0)
                if sp_r[1] <= sp_date[0] and (sp_date[0] - sp_r[1]) <= 65:
                    cand_refs.append((sp_r[1], re_ent))
            if cand_refs:
                best_ref = max(cand_refs, key=lambda x: x[0])[1]
                r_key = (best_ref["text"], "NGAY_BAN_HANH_THAM_CHIEU", d_txt)
                if r_key not in seen_body_rels:
                    seen_body_rels.add(r_key)
                    all_relations.append({
                        "head": best_ref["text"],
                        "head_type": "THAM_CHIEU_PHAP_LY",
                        "relation": "NGAY_BAN_HANH_THAM_CHIEU",
                        "tail": d_txt,
                        "tail_type": "NGAY_THAM_CHIEU",
                        "confidence": de.get("confidence", 0.95),
                        "para_idx": p_idx,
                    })

        if (p_offset + 1) % 100 == 0 or (p_offset + 1) == len(body_paras_to_process):
            print(f"    - Tiến độ thân văn bản: {p_offset + 1}/{len(body_paras_to_process)} đoạn (tổng {len(all_entities)} thực thể, {len(all_relations)} quan hệ)...")


    inference_time = time.time() - t0
    print(f"[+] Hoàn tất suy luận trong {inference_time:.2f}s!")
    print(f"    - Tổng thực thể: {len(all_entities)}")
    print(f"    - Tổng quan hệ : {len(all_relations)}")

    # 5. Xuat Markdown
    export_to_markdown(
        doc_name=doc_name,
        folder_id=folder_id,
        metadata=metadata,
        all_entities=all_entities,
        all_relations=all_relations,
        target_paras=target_paras,
        inference_time=inference_time,
        output_md_path=output_md_path
    )

    return {
        "doc_name": doc_name,
        "num_paras": len(target_paras),
        "num_entities": len(all_entities),
        "num_relations": len(all_relations),
        "inference_time": inference_time,
        "output_md": output_md_path,
        "output_html": os.path.splitext(output_md_path)[0] + ".html",
    }


def main():
    parser = argparse.ArgumentParser(description="Chạy test mô hình trên văn bản Google Drive và xuất file .md + .html")
    parser.add_argument("--doc-name", type=str, default="306_2025_NĐ-CP_186388", help="Tên văn bản hoặc thư mục trên Drive")
    parser.add_argument("--folder-id", type=str, default="1b9ghl3Dn4aKTmrsX5YbhAv1JIWGwdYY0", help="Drive Folder ID")
    parser.add_argument("--checkpoint", type=str, default="checkpoints/best_spert_phobert.pt", help="Đường dẫn checkpoint")
    parser.add_argument("--output-md", type=str, default=None, help="Đường dẫn file .md đầu ra")
    parser.add_argument("--max-paras", type=int, default=0, help="Số đoạn văn bản tối đa cần phân tích (0 để phân tích toàn văn 100%)")
    args = parser.parse_args()

    process_single_document(
        doc_name=args.doc_name,
        folder_id=args.folder_id,
        checkpoint=args.checkpoint,
        output_md=args.output_md,
        max_paras=args.max_paras,
    )


if __name__ == "__main__":
    main()

