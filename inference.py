"""
Script chay Suy luan (Inference) va Trich xuat Thuc the - Quan he Phap luat (Joint NER & RE)
bang mo hinh PhoBERT-SpERT da duoc huan luyen tren Legal Dataset.
"""
import os
import torch
from transformers import AutoTokenizer

from models.spert_phobert import PhoBERTSpeRT
from data.legal.vi_tokenize import vi_tokenize
from data.legal.schema import ENTITY_TYPES, RELATION_TYPES


STRUCT_CONTAINER_SET = {"DIEU", "KHOAN", "DIEM"}
OUTER_HUB_SET = {"HANH_VI_VI_PHAM", "NGHIA_VU_QUYEN", "HINH_PHAT_CHE_TAI", "BIEN_PHAP_KHAC_PHUC"}


def _nest_level(ent_type: str) -> int:
    if ent_type in STRUCT_CONTAINER_SET:
        return 2
    if ent_type in OUTER_HUB_SET:
        return 1
    return 0


def non_max_suppression(entities):
    """
    3-Level Nested-Aware Non-Maximum Suppression (NMS):
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


_CACHED_MODEL = None
_CACHED_TOKENIZER = None
_CACHED_META = None


def get_model(checkpoint_path="checkpoints/best_spert_phobert.pt"):
    global _CACHED_MODEL, _CACHED_TOKENIZER, _CACHED_META
    if _CACHED_MODEL is not None:
        return _CACHED_MODEL, _CACHED_TOKENIZER, _CACHED_META

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model_name = "vinai/phobert-base-v2"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    max_span_length = 110

    entity_types = ENTITY_TYPES
    relation_types = RELATION_TYPES

    checkpoint_data = None
    if os.path.exists(checkpoint_path):
        checkpoint_data = torch.load(checkpoint_path, map_location=device)
        entity_types = checkpoint_data.get("entity_types", ENTITY_TYPES)
        relation_types = checkpoint_data.get("relation_types", RELATION_TYPES)
        if "model_state_dict" in checkpoint_data and "size_embeddings.weight" in checkpoint_data["model_state_dict"]:
            max_span_length = checkpoint_data["model_state_dict"]["size_embeddings.weight"].shape[0] - 1

    id2entity = {i + 1: t for i, t in enumerate(entity_types)}
    id2rel = {i + 1: t for i, t in enumerate(relation_types)}

    model = PhoBERTSpeRT(
        model_name=model_name,
        num_entity_types=len(entity_types),
        num_relation_types=len(relation_types),
        max_span_length=max_span_length,
        size_embedding_dim=25
    ).to(device)

    if checkpoint_data:
        model.load_state_dict(checkpoint_data["model_state_dict"])
        print(f"[+] Đã nạp thành công checkpoint (Epoch {checkpoint_data.get('epoch', '?')})")
    else:
        print(f"[CANH BAO] Khong tim thay {checkpoint_path}, su dung trong so khoi tao!")

    model.eval()
    _CACHED_MODEL = model
    _CACHED_TOKENIZER = tokenizer
    _CACHED_META = (device, id2entity, id2rel, max_span_length)
    return _CACHED_MODEL, _CACHED_TOKENIZER, _CACHED_META


def run_inference(
    text: str,
    checkpoint_path: str = "checkpoints/best_spert_phobert.pt",
    entity_threshold: float = 0.35,
    relation_threshold: float = 0.50
):
    model, tokenizer, (device, id2entity, id2rel, max_span_length) = get_model(checkpoint_path)


    # 2. Tien xu ly tach tu tieng Viet bao toan so hieu van ban
    words = vi_tokenize(text)
    segmented_text = " ".join(words)
    print(f"\n[Cau goc]: {text}")
    print(f"[Tach tu]: {segmented_text}")
    print(f"[So tu]  : {len(words)}")

    # 3. Anh xa tu sang subwords
    subword_ids = [tokenizer.bos_token_id]
    word_to_subword = []
    for word in words:
        tokens = tokenizer.encode(word, add_special_tokens=False)
        if not tokens:
            tokens = [tokenizer.unk_token_id]
        start_idx = len(subword_ids)
        subword_ids.extend(tokens)
        end_idx = len(subword_ids)
        word_to_subword.append((start_idx, end_idx))
    subword_ids.append(tokenizer.eos_token_id)

    input_ids = torch.tensor([subword_ids], dtype=torch.long, device=device)
    attention_mask = torch.ones_like(input_ids, device=device)

    # 4. Sinh toan bo cac candidate spans
    from data.dataset import generate_candidate_spans
    candidate_word_spans = generate_candidate_spans(words, max_span_length)
    subword_spans = []
    span_lengths = []
    for w_start, w_end in candidate_word_spans:
        sw_start = word_to_subword[w_start][0]
        sw_end = word_to_subword[w_end - 1][1]
        subword_spans.append((sw_start, sw_end))
        span_lengths.append(w_end - w_start)

    if not subword_spans:
        print("Không tạo được span nào từ văn bản.")
        return

    spans_tensor = torch.tensor([subword_spans], dtype=torch.long, device=device)
    lengths_tensor = torch.tensor([span_lengths], dtype=torch.long, device=device)

    # 5. Du doan thuc the (Entity Prediction)
    with torch.no_grad():
        with torch.amp.autocast('cuda' if torch.cuda.is_available() else 'cpu'):
            outputs = model(
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
            ent_type = id2entity.get(best_cls, "UNKNOWN")
            raw_entities.append({
                "span_idx": idx,
                "text": ent_text,
                "type": ent_type,
                "span": (w_start, w_end),
                "confidence": conf
            })

    # Ap dung NMS loai bo span trung lap
    detected_entities = non_max_suppression(raw_entities)

    # 6. Du doan quan he giua cac cap thuc the da trich xuat (Sigmoid doc lap - BCEWithLogitsLoss)
    detected_relations = []
    if len(detected_entities) >= 2:
        rel_pairs = []
        pair_ent_map = []
        for i, e1 in enumerate(detected_entities):
            for j, e2 in enumerate(detected_entities):
                if i != j:
                    rel_pairs.append((e1["span_idx"], e2["span_idx"]))
                    pair_ent_map.append((e1, e2))

        rel_pairs_tensor = torch.tensor([rel_pairs], dtype=torch.long, device=device)

        with torch.no_grad():
            with torch.amp.autocast('cuda' if torch.cuda.is_available() else 'cpu'):
                rel_outputs = model(
                    input_ids=input_ids,
                    attention_mask=attention_mask,
                    spans=spans_tensor,
                    span_lengths=lengths_tensor,
                    rel_pairs=rel_pairs_tensor
                )
                rel_logits = rel_outputs["relation_logits"][0]  # (Num_Pairs, |R|)
                rel_probs = torch.sigmoid(rel_logits)           # (Num_Pairs, |R|)

        num_rel_classes = rel_probs.shape[-1]
        for p_idx in range(len(rel_pairs)):
            e1, e2 = pair_ent_map[p_idx]
            for r_offset in range(num_rel_classes):
                conf = rel_probs[p_idx, r_offset].item()
                if conf >= relation_threshold:
                    best_r_cls = r_offset + 1
                    rel_type = id2rel.get(best_r_cls, "UNKNOWN")
                    detected_relations.append({
                        "head": e1["text"],
                        "head_type": e1["type"],
                        "relation": rel_type,
                        "tail": e2["text"],
                        "tail_type": e2["type"],
                        "confidence": conf
                    })

    # 7. Hau xu ly chuan hoa ranh gioi thuc the chuyen nganh (GIAY_TO_HO_SO, TO_CHUC_DOANH_NGHIEP...)
    from data.legal.intra_sentence_kg import extract_intra_sentence_spans
    intra_cands = extract_intra_sentence_spans(text)
    entity_remap = {}
    for cs, ce, ctype in intra_cands:
        ctxt = text[cs:ce]
        if ctype not in {
            "LINH_VUC", "TU_KHOA_PHAP_LY", "THAM_CHIEU_PHAP_LY", "NGAY_THAM_CHIEU",
            "CO_QUAN_THAM_QUYEN", "TO_CHUC_DOANH_NGHIEP", "CHU_THE_CA_NHAN",
            "GIAY_TO_HO_SO", "TAI_SAN_VAT_CHAT"
        }:
            continue
        cand_words = vi_tokenize(ctxt)
        if not cand_words:
            continue
        cand_tok_s = len(vi_tokenize(text[:cs]))
        cand_tok_e = cand_tok_s + len(cand_words)
        cand_norm = " ".join(cand_words).replace("_", " ")

        encl = [
            be for be in detected_entities
            if be["type"] not in OUTER_HUB_SET and be["type"] not in STRUCT_CONTAINER_SET
            and max(be["span"][0], cand_tok_s) < min(be["span"][1], cand_tok_e)
            and (
                (be["span"][0] >= cand_tok_s and be["span"][1] <= cand_tok_e)
                or (
                    ctype in {"GIAY_TO_HO_SO", "TO_CHUC_DOANH_NGHIEP", "CO_QUAN_THAM_QUYEN", "THAM_CHIEU_PHAP_LY", "LINH_VUC"}
                    and be["span"][0] >= cand_tok_s
                    and len(cand_norm) > len(be["text"])
                )
            )
        ]
        if any(be["type"] == ctype and be["span"] == (cand_tok_s, cand_tok_e) for be in encl):
            continue
        for be in encl:
            entity_remap[(be["text"], be["type"])] = (cand_norm, ctype)
            detected_entities.remove(be)
        for hub in detected_entities:
            if hub["type"] in OUTER_HUB_SET and hub["span"][0] <= cand_tok_s < hub["span"][1] < cand_tok_e:
                old_hub = (hub["text"], hub["type"])
                hub["span"] = (hub["span"][0], cand_tok_e)
                hub["text"] = " ".join(words[hub["span"][0]:cand_tok_e]).replace("_", " ")
                entity_remap[old_hub] = (hub["text"], hub["type"])
        detected_entities.append({
            "span_idx": -1,
            "text": cand_norm,
            "type": ctype,
            "span": (cand_tok_s, cand_tok_e),
            "confidence": max([be["confidence"] for be in encl], default=0.92)
        })

    if entity_remap:
        for r in detected_relations:
            hk = (r["head"], r["head_type"])
            while hk in entity_remap and entity_remap[hk] != hk:
                hk = entity_remap[hk]
            r["head"], r["head_type"] = hk
            tk = (r["tail"], r["tail_type"])
            while tk in entity_remap and entity_remap[tk] != tk:
                tk = entity_remap[tk]
            r["tail"], r["tail_type"] = tk

    detected_entities = sorted(detected_entities, key=lambda x: (x["span"][0], -x["span"][1]))

    print("\n" + "=" * 65)
    print("KET QUA TRICH XUAT THUC THE (ENTITIES):")
    print("=" * 65)
    if not detected_entities:
        print("  Không tìm thấy thực thể nào đạt ngưỡng tin cậy.")
    else:
        for i, ent in enumerate(detected_entities):
            print(f"  [{i+1:02d}] {ent['text']:<30} | Loại: {ent['type']:<10} | Span: {str(ent['span']):<8} | Conf: {ent['confidence']:.2%}")

    print("\n" + "=" * 65)
    print("KET QUA TRICH XUAT QUAN HE (RELATIONS):")
    print("=" * 65)
    if not detected_relations:
        print("  Không phát hiện quan hệ nào giữa các cặp thực thể.")
    else:
        for i, r in enumerate(detected_relations):
            print(f"  [{i+1:02d}] ({r['head']} [{r['head_type']}]) ==[ {r['relation']} ]==> ({r['tail']} [{r['tail_type']}]) | Conf: {r['confidence']:.2%}")
    print("=" * 65 + "\n")


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Chạy nhận dạng Thực thể và Quan hệ văn bản pháp luật bằng PhoBERT-SpERT")
    parser.add_argument("--text", type=str, default="", help="Câu hoặc đoạn văn bản pháp luật cần nhận dạng")
    parser.add_argument("--checkpoint", type=str, default="checkpoints/best_spert_phobert.pt", help="Đường dẫn file checkpoint")
    args = parser.parse_args()

    if args.text:
        run_inference(args.text, checkpoint_path=args.checkpoint)
    else:
        test_cases = [
            "Phạt tiền từ 10.000.000 đồng đến 20.000.000 đồng đối với người sử dụng lao động có hành vi giữ bản chính giấy tờ tùy thân của người lao động tại doanh nghiệp trong thời hạn 15 ngày.",
            "Chủ tịch UBND cấp tỉnh có thẩm quyền phạt tiền đến 50.000.000 đồng và buộc nộp lại số lợi bất hợp pháp đối với doanh nghiệp có hành vi sử dụng trái phép tài sản nhà nước.",
            "Nghị định số 04/2013/NĐ-CP ngày 07 tháng 01 năm 2013 của Chính phủ do Phó Thủ tướng Nguyễn Xuân Phúc ký ban hành.",
            "Doanh nghiệp có nghĩa vụ nộp hồ sơ kê khai thuế cho cơ quan có thẩm quyền trong thời hạn 30 ngày tại địa phương."
        ]
        for s in test_cases:
            run_inference(s, checkpoint_path=args.checkpoint)

