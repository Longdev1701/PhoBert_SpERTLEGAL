"""
Sinh dữ liệu Joint NER + RE (định dạng SpERT) từ thuoc_tinh.json + muc_luc.json + noi_dung.docx.

Các loại mẫu (sample types):
  1. "header": Trích xuất khối tiêu đề (CO_QUAN_BAN_HANH, SO_HIEU, LOAI_VAN_BAN, NGAY_BAN_HANH)
     -> quan hệ BAN_HANH_BOI, LA_LOAI_VAN_BAN, BAN_HANH_NGAY
  2. "signature": Trích xuất khối chữ ký (CHUC_DANH_NGUOI_KY, NGUOI_KY)
     -> quan hệ GIU_CHUC_VU
  3. "meta": Khối kết hợp tiêu đề + chữ ký
     -> quan hệ BAN_HANH_BOI, LA_LOAI_VAN_BAN, BAN_HANH_NGAY, KY_BOI, GIU_CHUC_VU
  4. "body_context": Mẫu chính gắn kết THUỘC TÍNH VĂN BẢN cùng cấu trúc ĐIỀU / KHOẢN / ĐIỂM
     -> thực thể SO_HIEU, LOAI_VAN_BAN, CO_QUAN_BAN_HANH, (NGAY_BAN_HANH), DIEU, KHOAN, DIEM
     -> quan hệ BAN_HANH_BOI, LA_LOAI_VAN_BAN, (BAN_HANH_NGAY), THUOC_VE (DIEM->KHOAN, KHOAN->DIEU, DIEU->SO_HIEU)
  5. "body_standalone": Mẫu điều khoản điểm nguyên bản không có tiền tố metadata (để mô hình nhận diện khi gặp đoạn văn độc lập)
     -> thực thể DIEU, KHOAN, DIEM; quan hệ THUOC_VE
  6. "hard_negative": Mẫu âm tiêu đề chương (NHỮNG QUY ĐỊNH CHUNG), tiêu ngữ, nơi nhận (0 thực thể, 0 quan hệ)
     -> triệt tiêu dứt điểm lỗi nhận diện nhầm "quy định" thành LOAI_VAN_BAN.

Chạy: python -m data.legal.build_dataset
"""
import os
import re
import json
import glob
import random
import zipfile
import argparse
import unicodedata
from collections import Counter, defaultdict

from data.legal.vi_tokenize import vi_tokenize
from data.legal.schema import ENTITY_TYPES, RELATION_TYPES, RELATION_CONSTRAINTS, OUTER_HUB_ENTITY_TYPES
from data.legal.intra_sentence_kg import (
    extract_intra_sentence_spans,
    extract_document_self_lexicon,
    build_intra_sentence_relations,
)

HERE = os.path.dirname(__file__)
RAW_DIR = os.path.join(HERE, "raw")
OUT_DIR = os.path.join(HERE, "processed")

MAX_WORDS_BODY = 115     # số từ tối đa trong một mẫu
MAX_SUBWORDS = 250       # PhoBERT-base-v2 tối đa 256 token
MAX_BODY_PER_DOC = 55    # Số mẫu body tối đa mỗi văn bản (để cân bằng dữ liệu)

RANK_PREFIXES = [
    "Đại tướng", "Thượng tướng", "Trung tướng", "Thiếu tướng", "Đại tá", "Thượng tá",
    "Trung tá", "Thiếu tá", "GS.TS.", "PGS.TS.", "GS.", "PGS.", "TS.", "ThS."
]

DATE_RES = [
    re.compile(r"ngày\s+(\d{1,2})\s+tháng\s+(\d{1,2})\s+năm\s+(\d{4})", re.I),
    re.compile(r"(?<!\d)(\d{1,2})\s*/\s*(\d{1,2})\s*/\s*(\d{4})(?!\d)"),
]

HEADER_STOP = re.compile(r"^(Căn cứ|Theo đề nghị|Xét đề nghị|Điều 1\b|Chương [IVX1]|Để |Phần [IVX1])", re.I)
LOAI_VB_LINE = re.compile(r"^(BỘ LUẬT|LUẬT|NGHỊ ĐỊNH|QUYẾT ĐỊNH|THÔNG TƯ|NGHỊ QUYẾT|CHỈ THỊ|PHÁP LỆNH)\b", re.I)
SIGN_MARK = re.compile(r"^(KT\.|TM\.|TL\.|TUQ\.|Q\.|K/T|T/M|\(Đã ký\)|\(đã ký\)|Đã ký:)", re.I)


# ======================================================================
# 1. Tiền xử lý văn bản
# ======================================================================
def norm_text(s):
    s = unicodedata.normalize("NFC", s or "")
    s = s.replace("\u00d0", "\u0110").replace("\u00f0", "\u0111")
    s = s.replace("\u00a0", " ").replace("\u200b", "").replace("\u00ad", "")
    return re.sub(r"\s+", " ", s).strip()


_VOWELS = "aăâeêioôơuưyáắấéếíóốớúứýàằầèềìòồờùừỳảẳẩẻểỉỏổởủửỷãẵẫẽễĩõỗỡũữỹạặậẹệịọộợụựỵ"
_LOWER = "a-zđ" + _VOWELS
_BROKEN_HEAD = re.compile(rf"(?<![\w])([BCDĐGHKLMNPQRSTVX]) ([{_VOWELS}][{_LOWER}]*)(?![\w])")
_BROKEN_RUN = re.compile(rf"(?<![\w,])([A-ZĐ{_LOWER.upper()}{_LOWER}](?: [{_LOWER}]){{2,}})(?![\w])")


def fix_broken_syllables(s):
    s2, _ = _BROKEN_RUN.subn(lambda m: m.group(1).replace(" ", ""), s)
    s2, _ = _BROKEN_HEAD.subn(r"\1\2", s2)
    return s2


def read_docx_paras(path):
    try:
        x = zipfile.ZipFile(path).read("word/document.xml").decode("utf-8")
    except Exception:
        return []
    x = re.sub(r"<w:(?:br|tab|cr)\b[^>]*/>", "<w:t> </w:t>", x)
    paras = []
    for p in re.findall(r"<w:p[ >].*?</w:p>", x, re.S):
        t = "".join(re.findall(r"<w:t[^>]*>([^<]*)</w:t>", p))
        t = re.sub(r"(?:[-_=*.…]\s*){3,}", " ", t)
        t = fix_broken_syllables(norm_text(t))
        if t and re.search(r"[A-Za-zÀ-ỹ0-9]", t):
            if paras and re.search(r"\bý$", paras[-1], re.I) and re.match(r"^\([ivx]+\)", t, re.I):
                paras[-1] = paras[-1] + " " + t
            else:
                paras.append(t)
    return paras


def strip_crawler_title(paras, attrs):
    while paras and paras[0] in ("Document Content",):
        paras = paras[1:]
    if paras and paras[0].lower().startswith(attrs.get("loai_van_ban", "#").lower()) \
            and attrs.get("so_hieu", "#") in paras[0]:
        paras = paras[1:]
    return paras


def n_words(s):
    return len(s.split())


def find_all(text, needle, ignore_case=True):
    if not needle:
        return []
    hay, ndl = (text.lower(), needle.lower()) if ignore_case else (text, needle)
    if len(hay) != len(text):
        hay, ndl = text, needle
    out, i = [], hay.find(ndl)
    while i != -1:
        j = i + len(ndl)
        left_ok = i == 0 or not text[i - 1].isalnum()
        right_ok = j == len(text) or not text[j].isalnum()
        if left_ok and right_ok:
            out.append((i, j))
        i = hay.find(ndl, i + 1)
    return out


def overlaps(span, spans):
    return any(span[0] < e and s < span[1] for s, e, _ in spans)


def tokenize_with_spans(text, spans):
    """
    Tách từ tiếng Việt bằng PyVi hỗ trợ đầy đủ cả Thực thể Độc lập và Thực thể Lồng nhau (Nested Spans).
    Sử dụng tập các điểm cắt ký tự nguyên tử (atomic cut points) để câu chỉ được tách từ đúng 1 lần
    và mọi span (dù bao ngoài hay lồng bên trong) đều ánh xạ chính xác tuyệt đối sang chỉ số token [ts, te).
    """
    if not spans:
        return vi_tokenize(text.strip()) if text.strip() else [], []

    cut_points = sorted({0, len(text)} | {s for s, _, _ in spans} | {e for _, e, _ in spans})
    tokens = []
    char_to_tok = {0: 0}

    for i in range(len(cut_points) - 1):
        c_start, c_end = cut_points[i], cut_points[i + 1]
        seg = text[c_start:c_end].strip()
        if seg:
            tokens.extend(vi_tokenize(seg))
        char_to_tok[c_end] = len(tokens)

    result = []
    for s, e, t in spans:
        ts = char_to_tok[s]
        te = char_to_tok[e]
        result.append((ts, te, t))
    return tokens, result


def clean_person(name):
    name = (name or "").strip()
    for r in RANK_PREFIXES:
        if name.startswith(r + " "):
            return name[len(r) + 1:].strip()
    return name


def extract_header(paras):
    head = []
    for idx, p in enumerate(paras[:14]):
        if HEADER_STOP.match(p):
            break
        if n_words(p) <= 40:
            head.append(p)
        if idx >= 1 and n_words(p) <= 4 and LOAI_VB_LINE.match(p.strip()):
            break
    return head


def extract_signature_paras(paras, names):
    tail = paras[-25:]
    target_idx = None
    for i, p in enumerate(tail):
        for n in names:
            if n and find_all(p, n):
                target_idx = i
                break
    if target_idx is not None:
        start_i = max(0, target_idx - 2)
        end_i = min(len(tail), target_idx + 1)
        res = [p for p in tail[start_i:end_i] if n_words(p) <= 25 and not HEADER_STOP.match(p)]
        return res
    # Fallback
    keep = []
    for p in paras[-12:]:
        if n_words(p) <= 15 and re.search(r"[A-Za-zÀ-ỹ]", p) and not re.match(r"^(-|\+|•|Nơi nhận)", p):
            keep.append(p)
    has_sign = any(SIGN_MARK.match(p) for p in keep) or any(find_all(" ".join(keep), n) for n in names if n)
    return keep[-4:] if has_sign else []


# ======================================================================
# 2. Xây dựng các loại mẫu cho 1 văn bản
# ======================================================================
def build_samples_for_document(dpath, rng):
    attrs_raw = json.load(open(os.path.join(dpath, "thuoc_tinh.json"), encoding="utf-8"))["attributes"]
    attrs = {k: norm_text(str(v)) for k, v in attrs_raw.items()}
    paras = strip_crawler_title(read_docx_paras(os.path.join(dpath, "noi_dung.docx")), attrs)
    ml_path = os.path.join(dpath, "muc_luc.json")
    muc_luc = json.load(open(ml_path, encoding="utf-8")) if os.path.exists(ml_path) else None

    samples = []

    names_raw = [x for x in (attrs.get("nguoi_ky") or "").split(",") if x.strip() and x.strip() != "--"]
    names = [clean_person(n) for n in names_raw]
    titles_raw = [x.strip() for x in (attrs.get("chuc_danh_nguoi_ky") or "").split(",") if x.strip() and x.strip() != "--"]
    titles = [re.sub(r"^(Nữ|Nam)\s+", "", t, flags=re.I).strip() for t in titles_raw]

    header_paras = extract_header(paras)
    sig_paras = extract_signature_paras(paras, names)
    doc_lexicon = extract_document_self_lexicon(paras)

    # ----------------------------------------------------
    # (1) Mẫu Header
    # ----------------------------------------------------
    if header_paras:
        head_text = " . ".join(header_paras)
        spans, found = [], {}

        so_hieu = attrs.get("so_hieu", "")
        if so_hieu and so_hieu not in ("--", "Không số"):
            pat = r"\s*".join(re.escape(ch) for ch in so_hieu.replace(" ", ""))
            cands = [(m.start(), m.end()) for m in re.finditer(pat, head_text, re.I)]
            for c in cands:
                if not overlaps(c, spans):
                    spans.append((c[0], c[1], "SO_HIEU"))
                    found["SO_HIEU"] = len(spans) - 1
                    break

        nbh = attrs.get("ngay_ban_hanh", "")
        if re.match(r"\d{4}-\d{2}-\d{2}$", nbh):
            y, m, d = map(int, nbh.split("-"))
            cands = []
            for rgx in DATE_RES:
                for mm in rgx.finditer(head_text):
                    if (int(mm.group(1)), int(mm.group(2)), int(mm.group(3))) == (d, m, y):
                        cands.append((mm.start(), mm.end()))
            for c in sorted(cands):
                if not overlaps(c, spans):
                    spans.append((c[0], c[1], "NGAY_BAN_HANH"))
                    found["NGAY_BAN_HANH"] = len(spans) - 1
                    break

        co_quan = attrs.get("co_quan_ban_hanh", "")
        if co_quan and co_quan != "--":
            for c in find_all(head_text, co_quan):
                if not overlaps(c, spans):
                    spans.append((c[0], c[1], "CO_QUAN_BAN_HANH"))
                    found["CO_QUAN_BAN_HANH"] = len(spans) - 1
                    break

        loai = attrs.get("loai_van_ban", "")
        if loai and loai != "--":
            for c in find_all(head_text, loai):
                if not overlaps(c, spans):
                    spans.append((c[0], c[1], "LOAI_VAN_BAN"))
                    found["LOAI_VAN_BAN"] = len(spans) - 1
                    break

        for cs, ce, ctp in extract_intra_sentence_spans(head_text, base_offset=0, existing_spans=spans):
            if ctp == "LINH_VUC" and not overlaps((cs, ce), spans):
                spans.append((cs, ce, "LINH_VUC"))
                found["LINH_VUC"] = len(spans) - 1
                break

        if len(spans) >= 2 and "SO_HIEU" in found:
            tokens, tok_spans = tokenize_with_spans(head_text, spans)
            rels = []
            h = found["SO_HIEU"]
            for key, rtype in [
                ("CO_QUAN_BAN_HANH", "BAN_HANH_BOI"),
                ("NGAY_BAN_HANH", "BAN_HANH_NGAY"),
                ("LOAI_VAN_BAN", "LA_LOAI_VAN_BAN"),
                ("LINH_VUC", "THUOC_LINH_VUC"),
            ]:
                if key in found:
                    rels.append({"type": rtype, "head": h, "tail": found[key]})
            samples.append({
                "kind": "header",
                "tokens": tokens,
                "entities": [{"type": t, "start": s, "end": e} for s, e, t in tok_spans],
                "relations": rels
            })

    # ----------------------------------------------------
    # (2) Mẫu Signature
    # ----------------------------------------------------
    if sig_paras:
        sig_text = " . ".join(sig_paras)
        spans, found = [], {}
        for idx, name in enumerate(names):
            cands = sorted(find_all(sig_text, name), reverse=True)
            for c in cands:
                if not overlaps(c, spans):
                    spans.append((c[0], c[1], "NGUOI_KY"))
                    found[f"NGUOI_KY_{idx}"] = len(spans) - 1
                    break

            if f"NGUOI_KY_{idx}" in found:
                npos = spans[found[f"NGUOI_KY_{idx}"]][0]
                title = titles[idx] if idx < len(titles) else (titles[0] if titles else "")
                tw = title.split()
                tc = []
                for L in range(len(tw), min(2, len(tw)) - 1, -1):
                    tc = [c for c in find_all(sig_text, " ".join(tw[:L])) if c[0] < npos]
                    if tc:
                        break
                for c in sorted(tc, key=lambda x: -x[0]):
                    if not overlaps(c, spans):
                        spans.append((c[0], c[1], "CHUC_DANH_NGUOI_KY"))
                        found[f"CHUC_DANH_NGUOI_KY_{idx}"] = len(spans) - 1
                        break

        if len(spans) >= 2:
            tokens, tok_spans = tokenize_with_spans(sig_text, spans)
            rels = []
            for idx in range(len(names)):
                if f"NGUOI_KY_{idx}" in found and f"CHUC_DANH_NGUOI_KY_{idx}" in found:
                    rels.append({"type": "GIU_CHUC_VU", "head": found[f"NGUOI_KY_{idx}"], "tail": found[f"CHUC_DANH_NGUOI_KY_{idx}"]})
            if rels:
                samples.append({
                    "kind": "signature",
                    "tokens": tokens,
                    "entities": [{"type": t, "start": s, "end": e} for s, e, t in tok_spans],
                    "relations": rels
                })

    # ----------------------------------------------------
    # (3) Mẫu Meta Kết Hợp (Header + Signature -> KY_BOI)
    # ----------------------------------------------------
    if header_paras and sig_paras:
        head_compact = " . ".join(header_paras[:6])
        sig_compact = " . ".join(sig_paras[-3:])
        full_meta = head_compact + " . " + sig_compact
        if n_words(full_meta) <= 150:
            spans, found = [], {}
            sig_offset = len(head_compact) + 3

            so_hieu = attrs.get("so_hieu", "")
            if so_hieu and so_hieu not in ("--", "Không số"):
                pat = r"\s*".join(re.escape(ch) for ch in so_hieu.replace(" ", ""))
                cands = [(m.start(), m.end()) for m in re.finditer(pat, full_meta, re.I)]
                for c in cands:
                    if c[0] < sig_offset and not overlaps(c, spans):
                        spans.append((c[0], c[1], "SO_HIEU"))
                        found["SO_HIEU"] = len(spans) - 1
                        break

            co_quan = attrs.get("co_quan_ban_hanh", "")
            if co_quan and co_quan != "--":
                for c in find_all(full_meta, co_quan):
                    if c[0] < sig_offset and not overlaps(c, spans):
                        spans.append((c[0], c[1], "CO_QUAN_BAN_HANH"))
                        found["CO_QUAN_BAN_HANH"] = len(spans) - 1
                        break

            loai = attrs.get("loai_van_ban", "")
            if loai and loai != "--":
                for c in find_all(full_meta, loai):
                    if c[0] < sig_offset and not overlaps(c, spans):
                        spans.append((c[0], c[1], "LOAI_VAN_BAN"))
                        found["LOAI_VAN_BAN"] = len(spans) - 1
                        break

            for idx, name in enumerate(names):
                cands = sorted(find_all(full_meta, name), reverse=True)
                for c in cands:
                    if c[0] >= sig_offset and not overlaps(c, spans):
                        spans.append((c[0], c[1], "NGUOI_KY"))
                        found[f"NGUOI_KY_{idx}"] = len(spans) - 1
                        break

                if f"NGUOI_KY_{idx}" in found:
                    npos = spans[found[f"NGUOI_KY_{idx}"]][0]
                    title = titles[idx] if idx < len(titles) else (titles[0] if titles else "")
                    tw = title.split()
                    tc = []
                    for L in range(len(tw), min(2, len(tw)) - 1, -1):
                        tc = [c for c in find_all(full_meta, " ".join(tw[:L])) if sig_offset <= c[0] < npos]
                        if tc:
                            break
                    for c in sorted(tc, key=lambda x: -x[0]):
                        if not overlaps(c, spans):
                            spans.append((c[0], c[1], "CHUC_DANH_NGUOI_KY"))
                            found[f"CHUC_DANH_NGUOI_KY_{idx}"] = len(spans) - 1
                            break

            if len(spans) >= 2 and "SO_HIEU" in found:
                tokens, tok_spans = tokenize_with_spans(full_meta, spans)
                rels = []
                h = found["SO_HIEU"]
                if "CO_QUAN_BAN_HANH" in found:
                    rels.append({"type": "BAN_HANH_BOI", "head": h, "tail": found["CO_QUAN_BAN_HANH"]})
                if "LOAI_VAN_BAN" in found:
                    rels.append({"type": "LA_LOAI_VAN_BAN", "head": h, "tail": found["LOAI_VAN_BAN"]})
                for idx in range(len(names)):
                    if f"NGUOI_KY_{idx}" in found:
                        rels.append({"type": "KY_BOI", "head": h, "tail": found[f"NGUOI_KY_{idx}"]})
                        if f"CHUC_DANH_NGUOI_KY_{idx}" in found:
                            rels.append({"type": "GIU_CHUC_VU", "head": found[f"NGUOI_KY_{idx}"], "tail": found[f"CHUC_DANH_NGUOI_KY_{idx}"]})
                if rels:
                    samples.append({
                        "kind": "meta",
                        "tokens": tokens,
                        "entities": [{"type": t, "start": s, "end": e} for s, e, t in tok_spans],
                        "relations": rels
                    })

    # Thuộc tính văn bản gắn vào tiền tố
    so_hieu = attrs.get("so_hieu", "")
    loai_vb = attrs.get("loai_van_ban", "")
    co_quan = attrs.get("co_quan_ban_hanh", "")
    ngay_raw = attrs.get("ngay_ban_hanh", "")
    ngay_str = ""
    if re.match(r"\d{4}-\d{2}-\d{2}$", ngay_raw):
        y, m, d = map(int, ngay_raw.split("-"))
        ngay_str = f"ngày {d:02d} tháng {m:02d} năm {y}"

    bad_lv = {"", "--", "Chưa phân loại", "Khác"}
    lv_raw = attrs.get("linh_vuc", "").strip(" ;.")
    ng_raw = attrs.get("nganh", "").strip(" ;.")
    linh_vuc_meta = lv_raw if lv_raw not in bad_lv else (ng_raw if ng_raw not in bad_lv else "")
    if linh_vuc_meta and len(vi_tokenize(linh_vuc_meta)) > 12:
        linh_vuc_meta = ""

    has_valid_meta = bool(so_hieu and so_hieu not in ("--", "Không số") and loai_vb and co_quan and co_quan != "--")

    # ----------------------------------------------------
    # (3B) Mẫu Preamble: Trích yếu & Căn cứ ban hành (trước Điều 1 / Chương I)
    # ----------------------------------------------------
    preamble_stop_re = re.compile(r"^(?:(?:Điều|Đỉều)\s+1\b|(?:Chương|Phần)\s+[IVX1]\b)", re.I)
    header_set = set(header_paras)
    preamble_paras = []
    for p in paras[:25]:
        if preamble_stop_re.match(p.strip()):
            break
        if p in header_set:
            continue
        if len(p.split()) >= 5:
            preamble_paras.append(p)

    preamble_count = 0
    for p_raw in preamble_paras:
        if preamble_count >= 7:
            break
        p_words = p_raw.split()
        p_txt = " ".join(p_words[:90]) if len(p_words) > 90 else p_raw
        intra_p = extract_intra_sentence_spans(p_txt, base_offset=0, existing_spans=[], doc_lexicon=doc_lexicon)
        if not intra_p:
            continue
        preamble_count += 1

        # (3B-1) Preamble có gắn tiền tố Metadata văn bản -> học quan hệ SO_HIEU --[REFERS_TO]--> LEGAL_REFERENCE
        if has_valid_meta:
            prefix = f"{loai_vb} số {so_hieu} của {co_quan} . "
            full_p = prefix + p_txt
            spans, found = [], {}
            for c in find_all(full_p, loai_vb):
                if c[0] < len(prefix) and not overlaps(c, spans):
                    spans.append((c[0], c[1], "LOAI_VAN_BAN"))
                    found["LOAI_VAN_BAN"] = len(spans) - 1
                    break
            for c in find_all(full_p, so_hieu):
                if c[0] < len(prefix) and not overlaps(c, spans):
                    spans.append((c[0], c[1], "SO_HIEU"))
                    found["SO_HIEU"] = len(spans) - 1
                    break
            for c in find_all(full_p, co_quan):
                if c[0] < len(prefix) and not overlaps(c, spans):
                    spans.append((c[0], c[1], "CO_QUAN_BAN_HANH"))
                    found["CO_QUAN_BAN_HANH"] = len(spans) - 1
                    break
            spans.extend(extract_intra_sentence_spans(full_p, base_offset=len(prefix), existing_spans=spans, doc_lexicon=doc_lexicon))
            if len(spans) >= 2:
                tokens, tok_spans = tokenize_with_spans(full_p, spans)
                rels = []
                if "SO_HIEU" in found and "CO_QUAN_BAN_HANH" in found:
                    rels.append({"type": "BAN_HANH_BOI", "head": found["SO_HIEU"], "tail": found["CO_QUAN_BAN_HANH"]})
                if "SO_HIEU" in found and "LOAI_VAN_BAN" in found:
                    rels.append({"type": "LA_LOAI_VAN_BAN", "head": found["SO_HIEU"], "tail": found["LOAI_VAN_BAN"]})
                rels.extend(build_intra_sentence_relations(tok_spans))
                samples.append({
                    "kind": "preamble_context",
                    "tokens": tokens,
                    "entities": [{"type": t, "start": s, "end": e} for s, e, t in tok_spans],
                    "relations": rels
                })

        # (3B-2) Preamble độc lập (không có tiền tố) -> giúp mô hình bắt trực tiếp LEGAL_REFERENCE ở các câu "Căn cứ...", "Sửa đổi, bổ sung..."
        tokens_st, tok_spans_st = tokenize_with_spans(p_txt, intra_p)
        rels_st = build_intra_sentence_relations(tok_spans_st)
        samples.append({
            "kind": "preamble_standalone",
            "tokens": tokens_st,
            "entities": [{"type": t, "start": s, "end": e} for s, e, t in tok_spans_st],
            "relations": rels_st
        })

    # ----------------------------------------------------
    # (4) Duyệt mục lục Chương / Điều / Khoản / Điểm thực tế của văn bản
    # ----------------------------------------------------
    units = []
    def traverse_ml(nodes, cur_chuong=None, cur_dieu=None, cur_khoan=None, cur_khoan_text=""):
        for nd in nodes:
            lvl = nd.get("level", "")
            num = str(nd.get("number", "")).strip()
            ttl = norm_text(nd.get("title", ""))
            raw_cnt = nd.get("content", "") or ""
            cnt_lines = [norm_text(ln) for ln in raw_cnt.splitlines() if norm_text(ln)]
            cnt = cnt_lines[0] if cnt_lines else ""
            children = nd.get("children", [])
            chuong = cur_chuong
            dieu = cur_dieu
            khoan = cur_khoan
            khoan_text = cur_khoan_text
            if lvl == "Chương":
                chuong = num
                dieu = None
                khoan = None
                khoan_text = ""
            elif lvl == "Điều":
                dieu = num
                khoan = None
                khoan_text = ""
            elif lvl == "Khoản":
                khoan = num
                khoan_text = cnt

            if lvl in ("Chương", "Điều", "Khoản", "Điểm"):
                units.append({
                    "level": lvl,
                    "num": num,
                    "title": ttl,
                    "content": cnt,
                    "parent_chuong": chuong if lvl != "Chương" else None,
                    "parent_dieu": dieu,
                    "parent_khoan": khoan,
                    "parent_khoan_text": cur_khoan_text if lvl == "Điểm" else "",
                    "children": children
                })
                # Nếu content có nhiều dòng con (ví dụ các ý (i), (ii), (iii), (iv)), tách thành các unit riêng để không bị cắt cụt ở 85 từ
                for extra_ln in cnt_lines[1:]:
                    if len(extra_ln.split()) >= 5:
                        m_sub = re.match(r"^(\([ivx]+\))\s+(.*)$", extra_ln, re.I)
                        units.append({
                            "level": "Điểm" if m_sub else lvl,
                            "num": m_sub.group(1) if m_sub else num,
                            "title": m_sub.group(1) if m_sub else ttl,
                            "content": m_sub.group(2) if m_sub else extra_ln,
                            "parent_chuong": chuong,
                            "parent_dieu": dieu,
                            "parent_khoan": khoan,
                            "parent_khoan_text": "",
                            "children": []
                        })
            if children:
                traverse_ml(children, chuong, dieu, khoan, khoan_text)

    if muc_luc:
        traverse_ml(muc_luc)

    # Bổ sung từ paras (noi_dung.docx) các Chương/Điều/Khoản/Điểm chưa có trong muc_luc.json (hoặc khi không có muc_luc.json)
    existing_sigs = {(u["level"], u.get("parent_chuong"), u["parent_dieu"], u["num"], (u["title"] + " " + u["content"])[:35]) for u in units}
    chuong_re = re.compile(r'^[“"]?(?:Chương|Phần)\s+([IVX0-9]+[a-z]?)\.?\s*(.*)$', re.I)
    dieu_re = re.compile(r'^[“"]?(?:Điều|Đỉều)\s+(\d+[a-z]?)\.?\s*(.*)$', re.I)
    khoan_re = re.compile(r'^[“"]?(\d+[a-z]?)\.\s+(.*)$')
    diem_re = re.compile(r'^[“"]?(?:([a-zđ])[),]|(\([ivx]+\)))\s+(.*)$', re.I)
    cur_ch = None
    cur_d = None
    cur_k = None
    cur_k_text = ""
    for p in paras:
        mc = chuong_re.match(p)
        if mc and not p.startswith(("“", '"')) and len(p.split()) <= 25:
            cur_ch = mc.group(1)
            cur_d = None
            cur_k = None
            cur_k_text = ""
            u_cand = {
                "level": "Chương", "num": cur_ch, "title": f"Chương {cur_ch}.", "content": mc.group(2),
                "parent_chuong": None, "parent_dieu": None, "parent_khoan": None, "parent_khoan_text": "", "children": []
            }
            sig = (u_cand["level"], u_cand["parent_chuong"], u_cand["parent_dieu"], u_cand["num"], (u_cand["title"] + " " + u_cand["content"])[:35])
            if sig not in existing_sigs:
                existing_sigs.add(sig)
                units.append(u_cand)
            continue
        m = dieu_re.match(p)
        if m and not p.startswith(("“", '"')):
            cur_d = m.group(1)
            cur_k = None
            cur_k_text = ""
            u_cand = {
                "level": "Điều", "num": cur_d, "title": f"Điều {cur_d}.", "content": m.group(2),
                "parent_chuong": cur_ch, "parent_dieu": cur_d, "parent_khoan": None, "parent_khoan_text": "", "children": []
            }
            sig = (u_cand["level"], u_cand["parent_chuong"], u_cand["parent_dieu"], u_cand["num"], (u_cand["title"] + " " + u_cand["content"])[:35])
            if sig not in existing_sigs:
                existing_sigs.add(sig)
                units.append(u_cand)
            continue
        mk = khoan_re.match(p)
        if mk and cur_d:
            cur_k = mk.group(1)
            cur_k_text = mk.group(2)
            u_cand = {
                "level": "Khoản", "num": cur_k, "title": f"{cur_k}.", "content": cur_k_text,
                "parent_chuong": cur_ch, "parent_dieu": cur_d, "parent_khoan": cur_k, "parent_khoan_text": "", "children": []
            }
            sig = (u_cand["level"], u_cand["parent_chuong"], u_cand["parent_dieu"], u_cand["num"], (u_cand["title"] + " " + u_cand["content"])[:35])
            if sig not in existing_sigs:
                existing_sigs.add(sig)
                units.append(u_cand)
            continue
        md = diem_re.match(p)
        if md and cur_d:
            d_num = md.group(1) or md.group(2)
            d_ttl = f"{md.group(1)})" if md.group(1) else md.group(2)
            u_cand = {
                "level": "Điểm", "num": d_num, "title": d_ttl, "content": md.group(3),
                "parent_chuong": cur_ch, "parent_dieu": cur_d, "parent_khoan": cur_k, "parent_khoan_text": cur_k_text, "children": []
            }
            sig = (u_cand["level"], u_cand["parent_chuong"], u_cand["parent_dieu"], u_cand["num"], (u_cand["title"] + " " + u_cand["content"])[:35])
            if sig not in existing_sigs:
                existing_sigs.add(sig)
                units.append(u_cand)

    def build_unit_body_text(u):
        lvl = u["level"]
        num = u["num"]
        ttl = u["title"]
        cnt = u["content"]
        dieu = u["parent_dieu"]
        khoan = u["parent_khoan"]
        pk_text = u.get("parent_khoan_text", "")

        if lvl == "Chương":
            chuong_anchor = f"Chương {num}"
            if cnt:
                b_txt = f"{ttl} . {cnt}" if not ttl.endswith(".") else f"{ttl} {cnt}"
            else:
                b_txt = ttl
            a_str = chuong_anchor
        elif lvl == "Điều":
            dieu_anchor = f"Điều {num}"
            if cnt:
                b_txt = f"{ttl} . {cnt}" if not ttl.endswith(".") else f"{ttl} {cnt}"
            else:
                b_txt = ttl
            a_str = dieu_anchor
        elif lvl == "Khoản":
            dieu_prefix = f"Điều {dieu} . " if dieu else ""
            b_txt = f"{dieu_prefix}{ttl} {cnt}".strip()
            a_str = f"Khoản {num}" if f"Khoản {num}" in ttl else f"{num}."
        else:  # Điểm
            dieu_prefix = f"Điều {dieu} . " if dieu else ""
            khoan_prefix = f"Khoản {khoan} . " if khoan else ""
            # Nếu Khoản cha có câu dẫn ngắn (ví dụ: "Phạt tiền từ ... đến ... đối với hành vi sau đây:"),
            # giữ lại câu dẫn thực tế của Khoản cha để nối liền mạch Chế tài (ở Khoản) với Hành vi (ở Điểm)
            pk_words = pk_text.split()
            if pk_text and 3 <= len(pk_words) <= 28:
                pk_clean = pk_text.rstrip(" :;.")
                b_txt = f"{dieu_prefix}{khoan_prefix}{pk_clean} : {ttl} {cnt}".strip()
            else:
                b_txt = f"{dieu_prefix}{khoan_prefix}{ttl} {cnt}".strip()
            if num.startswith("("):
                a_str = num
            else:
                a_str = f"Điểm {num}" if f"Điểm {num}" in ttl else f"{num})"
        return b_txt, a_str

    # Ưu tiên chọn các điều/khoản/điểm trong văn bản có chứa nhiều thực thể nội câu & thực thể lồng nhau thực tế
    if len(units) > MAX_BODY_PER_DOC:
        scored_indices = []
        for idx_u, u in enumerate(units):
            b_txt, _ = build_unit_body_text(u)
            w_list = b_txt.split()
            if len(w_list) > 95:
                b_txt = " ".join(w_list[:95])
            intra_sp = extract_intra_sentence_spans(b_txt, base_offset=0, existing_spans=[], doc_lexicon=doc_lexicon)
            n_hubs = sum(1 for _, _, tp in intra_sp if tp in OUTER_HUB_ENTITY_TYPES)
            n_refs = sum(1 for _, _, tp in intra_sp if tp == "THAM_CHIEU_PHAP_LY")
            n_lvs = sum(1 for _, _, tp in intra_sp if tp == "LINH_VUC")
            score = n_hubs * 4 + n_refs * 3 + n_lvs * 5 + len(intra_sp)
            scored_indices.append((score, idx_u))

        # Lấy tối đa 2/3 số lượng từ các điều khoản giàu thực thể nhất trong văn bản, 1/3 còn lại trải đều toàn văn bản
        rich_quota = int(MAX_BODY_PER_DOC * 0.7)
        top_rich = sorted(scored_indices, key=lambda x: (-x[0], x[1]))
        chosen_set = {idx_u for sc, idx_u in top_rich[:rich_quota] if sc > 0}

        remaining_needed = MAX_BODY_PER_DOC - len(chosen_set)
        if remaining_needed > 0:
            rem_indices = [i for i in range(len(units)) if i not in chosen_set]
            step = max(1.0, len(rem_indices) / remaining_needed)
            for k in range(min(remaining_needed, len(rem_indices))):
                chosen_set.add(rem_indices[int(k * step)])

        sampled_units = [units[i] for i in sorted(chosen_set)]
    else:
        sampled_units = units

    for u in sampled_units:
        lvl = u["level"]
        num = u["num"]
        chuong = u.get("parent_chuong")
        dieu = u["parent_dieu"]
        khoan = u["parent_khoan"]
        body_text, anchor_str = build_unit_body_text(u)

        if len(body_text.split()) < 4:
            continue

        words = body_text.split()
        if len(words) > 95:
            body_text = " ".join(words[:95])

        # (4A) Mẫu Contextual Body (có metadata prefix của chính văn bản đó)
        if has_valid_meta:
            p_choice = rng.random()
            has_ngay = False
            has_lv = False
            if ngay_str and p_choice < 0.35:
                prefix = f"{loai_vb} số {so_hieu} ban hành {ngay_str} bởi {co_quan} . "
                has_ngay = True
            elif linh_vuc_meta and p_choice < 0.70:
                prefix = f"{loai_vb} số {so_hieu} của {co_quan} trong lĩnh vực {linh_vuc_meta} . "
                has_lv = True
            elif p_choice < 0.70:
                prefix = f"{loai_vb} số {so_hieu} của {co_quan} . "
            else:
                prefix = f"{co_quan} ban hành {loai_vb} số {so_hieu} . "

            ch_cand = f"Chương {chuong} . " if (chuong and lvl == "Điều" and p_choice < 0.40) else ""
            full_text = prefix + ch_cand + body_text
            spans, found = [], {}

            for c in find_all(full_text, loai_vb):
                if c[0] < len(prefix) and not overlaps(c, spans):
                    spans.append((c[0], c[1], "LOAI_VAN_BAN"))
                    found["LOAI_VAN_BAN"] = len(spans) - 1
                    break
            for c in find_all(full_text, so_hieu):
                if c[0] < len(prefix) and not overlaps(c, spans):
                    spans.append((c[0], c[1], "SO_HIEU"))
                    found["SO_HIEU"] = len(spans) - 1
                    break
            for c in find_all(full_text, co_quan):
                if c[0] < len(prefix) and not overlaps(c, spans):
                    spans.append((c[0], c[1], "CO_QUAN_BAN_HANH"))
                    found["CO_QUAN_BAN_HANH"] = len(spans) - 1
                    break
            if has_ngay:
                for c in find_all(full_text, ngay_str):
                    if c[0] < len(prefix) and not overlaps(c, spans):
                        spans.append((c[0], c[1], "NGAY_BAN_HANH"))
                        found["NGAY_BAN_HANH"] = len(spans) - 1
                        break
            if has_lv and linh_vuc_meta:
                for c in find_all(full_text, linh_vuc_meta):
                    if c[0] < len(prefix) and not overlaps(c, spans):
                        spans.append((c[0], c[1], "LINH_VUC"))
                        found["LINH_VUC"] = len(spans) - 1
                        break

            # Body spans: Lấy trọn vẹn toàn bộ đoạn văn của Chương / Điều / Khoản / Điểm hiện tại (Outer Structural Span),
            # đồng thời dùng marker_spans ngắn để extract_intra_sentence_spans vẫn trích xuất đầy đủ các thực thể lồng bên trong.
            marker_spans = list(spans)

            if lvl == "Chương":
                for c in find_all(full_text, anchor_str):
                    if c[0] >= len(prefix) and not overlaps(c, marker_spans):
                        marker_spans.append((c[0], c[1], "CHUONG"))
                        spans.append((c[0], len(full_text), "CHUONG"))
                        found["CHUONG"] = len(spans) - 1
                        break
            elif ch_cand:
                for c in find_all(full_text, f"Chương {chuong}"):
                    if len(prefix) <= c[0] < len(prefix) + len(ch_cand) and not overlaps(c, marker_spans):
                        marker_spans.append((c[0], c[1], "CHUONG"))
                        spans.append((c[0], c[1], "CHUONG"))
                        found["CHUONG"] = len(spans) - 1
                        break

            eff_body_offset = len(prefix) + len(ch_cand)
            if dieu:
                for c in find_all(full_text, f"Điều {dieu}"):
                    if c[0] >= eff_body_offset and not overlaps(c, marker_spans):
                        marker_spans.append((c[0], c[1], "DIEU"))
                        if lvl == "Điều":
                            spans.append((c[0], len(full_text), "DIEU"))
                        else:
                            spans.append((c[0], c[1], "DIEU"))
                        found["DIEU"] = len(spans) - 1
                        break

            if lvl == "Khoản":
                for c in find_all(full_text, anchor_str):
                    if c[0] >= eff_body_offset and not overlaps(c, marker_spans):
                        marker_spans.append((c[0], c[1], "KHOAN"))
                        spans.append((c[0], len(full_text), "KHOAN"))
                        found["KHOAN"] = len(spans) - 1
                        break
            elif lvl == "Điểm":
                diem_char_start = None
                for c in find_all(full_text, anchor_str):
                    if c[0] >= eff_body_offset and not overlaps(c, marker_spans):
                        diem_char_start = c[0]
                        break
                if khoan:
                    for c in find_all(full_text, f"Khoản {khoan}"):
                        if c[0] >= eff_body_offset and not overlaps(c, marker_spans):
                            marker_spans.append((c[0], c[1], "KHOAN"))
                            k_end = c[1]
                            if diem_char_start and diem_char_start > c[1]:
                                seg_k = full_text[c[0]:diem_char_start].rstrip(" :;.")
                                if len(seg_k) > (c[1] - c[0]):
                                    k_end = c[0] + len(seg_k)
                            spans.append((c[0], k_end, "KHOAN"))
                            found["KHOAN"] = len(spans) - 1
                            break
                for c in find_all(full_text, anchor_str):
                    if c[0] >= eff_body_offset and not overlaps(c, marker_spans):
                        marker_spans.append((c[0], c[1], "DIEM"))
                        spans.append((c[0], len(full_text), "DIEM"))
                        found["DIEM"] = len(spans) - 1
                        break

            # Bổ sung các Thực thể Ngữ nghĩa Nội câu (Outer Hubs & Inner Nested Spans) trực tiếp từ câu thực tế
            intra_spans = extract_intra_sentence_spans(full_text, base_offset=eff_body_offset, existing_spans=marker_spans, doc_lexicon=doc_lexicon)
            spans.extend(intra_spans)

            if len(spans) >= 2:
                tokens, tok_spans = tokenize_with_spans(full_text, spans)
                rels = []
                if "SO_HIEU" in found and "CO_QUAN_BAN_HANH" in found:
                    rels.append({"type": "BAN_HANH_BOI", "head": found["SO_HIEU"], "tail": found["CO_QUAN_BAN_HANH"]})
                if "SO_HIEU" in found and "LOAI_VAN_BAN" in found:
                    rels.append({"type": "LA_LOAI_VAN_BAN", "head": found["SO_HIEU"], "tail": found["LOAI_VAN_BAN"]})
                if "SO_HIEU" in found and "NGAY_BAN_HANH" in found:
                    rels.append({"type": "BAN_HANH_NGAY", "head": found["SO_HIEU"], "tail": found["NGAY_BAN_HANH"]})
                if "SO_HIEU" in found and "LINH_VUC" in found:
                    rels.append({"type": "THUOC_LINH_VUC", "head": found["SO_HIEU"], "tail": found["LINH_VUC"]})
                if "CHUONG" in found and "SO_HIEU" in found:
                    rels.append({"type": "THUOC_VE", "head": found["CHUONG"], "tail": found["SO_HIEU"]})
                if "DIEU" in found and "CHUONG" in found:
                    rels.append({"type": "THUOC_VE", "head": found["DIEU"], "tail": found["CHUONG"]})
                elif "DIEU" in found and "SO_HIEU" in found:
                    rels.append({"type": "THUOC_VE", "head": found["DIEU"], "tail": found["SO_HIEU"]})
                if "KHOAN" in found and "DIEU" in found:
                    rels.append({"type": "THUOC_VE", "head": found["KHOAN"], "tail": found["DIEU"]})
                if "DIEM" in found and "KHOAN" in found:
                    rels.append({"type": "THUOC_VE", "head": found["DIEM"], "tail": found["KHOAN"]})

                # Bổ sung 13 nhãn quan hệ nội câu thực tế
                rels.extend(build_intra_sentence_relations(tok_spans))

                samples.append({
                    "kind": "body_context",
                    "tokens": tokens,
                    "entities": [{"type": t, "start": s, "end": e} for s, e, t in tok_spans],
                    "relations": rels
                })

        # (4B) Mẫu Standalone Body (~25% units hoặc khi có thực thể nội câu)
        intra_standalone = extract_intra_sentence_spans(body_text, base_offset=0, existing_spans=[], doc_lexicon=doc_lexicon)
        if rng.random() < 0.25 or len(intra_standalone) >= 2 or lvl == "Chương":
            spans, marker_spans, found = [], [], {}
            if lvl == "Chương":
                for c in find_all(body_text, anchor_str):
                    if not overlaps(c, marker_spans):
                        marker_spans.append((c[0], c[1], "CHUONG"))
                        spans.append((c[0], len(body_text), "CHUONG"))
                        found["CHUONG"] = len(spans) - 1
                        break
            if dieu:
                for c in find_all(body_text, f"Điều {dieu}"):
                    if not overlaps(c, marker_spans):
                        marker_spans.append((c[0], c[1], "DIEU"))
                        if lvl == "Điều":
                            spans.append((c[0], len(body_text), "DIEU"))
                        else:
                            spans.append((c[0], c[1], "DIEU"))
                        found["DIEU"] = len(spans) - 1
                        break
            if lvl == "Khoản":
                for c in find_all(body_text, anchor_str):
                    if not overlaps(c, marker_spans):
                        marker_spans.append((c[0], c[1], "KHOAN"))
                        spans.append((c[0], len(body_text), "KHOAN"))
                        found["KHOAN"] = len(spans) - 1
                        break
            elif lvl == "Điểm":
                diem_char_start = None
                for c in find_all(body_text, anchor_str):
                    if not overlaps(c, marker_spans):
                        diem_char_start = c[0]
                        break
                if khoan:
                    for c in find_all(body_text, f"Khoản {khoan}"):
                        if not overlaps(c, marker_spans):
                            marker_spans.append((c[0], c[1], "KHOAN"))
                            k_end = c[1]
                            if diem_char_start and diem_char_start > c[1]:
                                seg_k = body_text[c[0]:diem_char_start].rstrip(" :;.")
                                if len(seg_k) > (c[1] - c[0]):
                                    k_end = c[0] + len(seg_k)
                            spans.append((c[0], k_end, "KHOAN"))
                            found["KHOAN"] = len(spans) - 1
                            break
                for c in find_all(body_text, anchor_str):
                    if not overlaps(c, marker_spans):
                        marker_spans.append((c[0], c[1], "DIEM"))
                        spans.append((c[0], len(body_text), "DIEM"))
                        found["DIEM"] = len(spans) - 1
                        break

            spans.extend(extract_intra_sentence_spans(body_text, base_offset=0, existing_spans=marker_spans, doc_lexicon=doc_lexicon))

            if len(spans) >= 2:
                tokens, tok_spans = tokenize_with_spans(body_text, spans)
                rels = []
                if "DIEU" in found and "CHUONG" in found:
                    rels.append({"type": "THUOC_VE", "head": found["DIEU"], "tail": found["CHUONG"]})
                if "KHOAN" in found and "DIEU" in found:
                    rels.append({"type": "THUOC_VE", "head": found["KHOAN"], "tail": found["DIEU"]})
                if "DIEM" in found and "KHOAN" in found:
                    rels.append({"type": "THUOC_VE", "head": found["DIEM"], "tail": found["KHOAN"]})
                rels.extend(build_intra_sentence_relations(tok_spans))
                if rels:
                    samples.append({
                        "kind": "body_standalone",
                        "tokens": tokens,
                        "entities": [{"type": t, "start": s, "end": e} for s, e, t in tok_spans],
                        "relations": rels
                    })

    # ----------------------------------------------------
    # (5) Mẫu Hard Negative (Tiêu ngữ, Nơi nhận, Mục)
    # ----------------------------------------------------
    for p in paras:
        if re.match(r"^(\bMục\s+\d+|CỘNG HÒA XÃ HỘI CHỦ NGHĨA|Độc lập - Tự do|Nơi nhận:)", p, re.I):
            if n_words(p) <= 20:
                p_tok = vi_tokenize(p)
                if p_tok:
                    samples.append({
                        "kind": "hard_negative",
                        "tokens": p_tok,
                        "entities": [],
                        "relations": []
                    })
                    if len([s for s in samples if s["kind"] == "hard_negative"]) >= 6:
                        break

    return samples


# ======================================================================
# 3. Kiểm tra tính hợp lệ & Xuất dữ liệu
# ======================================================================
def check_sample(s):
    n = len(s["tokens"])
    for e in s["entities"]:
        assert 0 <= e["start"] < e["end"] <= n, e
        assert e["type"] in ENTITY_TYPES, f"Unknown entity: {e['type']}"
    for r in s["relations"]:
        assert r["type"] in RELATION_TYPES, f"Unknown relation: {r['type']}"
        ht = (s["entities"][r["head"]]["type"], s["entities"][r["tail"]]["type"])
        assert ht in RELATION_CONSTRAINTS[r["type"]], f"Invalid relation: {r}, types: {ht}"


def subword_len(tokens, tokenizer):
    return 2 + sum(len(tokenizer.encode(w, add_special_tokens=False)) for w in tokens)


def render_sample_markdown(s):
    tokens = list(s["tokens"])
    entities = s.get("entities", [])
    n_tok = len(tokens)

    # Dùng prefix/suffix trên biên token để hỗ trợ hiển thị cả thực thể lồng nhau (Nested Entities)
    prefixes = [[] for _ in range(n_tok)]
    suffixes = [[] for _ in range(n_tok)]
    for e in sorted(entities, key=lambda x: -(x["end"] - x["start"])):
        st, ed, tp = e["start"], e["end"], e["type"]
        if 0 <= st < ed <= n_tok:
            prefixes[st].append("**[")
            suffixes[ed - 1].insert(0, f"]`<{tp}>`**")

    rendered_tokens = []
    for i, tok in enumerate(tokens):
        clean_tok = tok.replace("_", " ")
        p_str = "".join(prefixes[i])
        s_str = "".join(suffixes[i])
        rendered_tokens.append(f"{p_str}{clean_tok}{s_str}")
    tagged_text = " ".join(rendered_tokens)

    lines = [
        f"### Mẫu #{s.get('id', '')} (Loại: `{s.get('kind', '')}`)",
        f"> {tagged_text}\n"
    ]
    if entities:
        lines.append("**Thực thể:**")
        for idx, e in enumerate(entities):
            ent_txt = " ".join(tokens[e["start"]:e["end"]]).replace("_", " ")
            # Kiểm tra xem thực thể này có nằm lồng bên trong thực thể khác không
            parents = [
                f"`e{p_idx}` (`{p['type']}`)"
                for p_idx, p in enumerate(entities)
                if p_idx != idx and e["start"] >= p["start"] and e["end"] <= p["end"] and (e["start"], e["end"]) != (p["start"], p["end"])
            ]
            nest_note = f" *(lồng trong {', '.join(parents)})*" if parents else ""
            lines.append(f"- `[e{idx}]` **{ent_txt}** → `{e['type']}` (span: `[{e['start']}:{e['end']}]`){nest_note}")
        lines.append("")
    if s.get("relations"):
        lines.append("**Quan hệ:**")
        for r in s["relations"]:
            h = entities[r["head"]]
            t = entities[r["tail"]]
            h_txt = " ".join(tokens[h["start"]:h["end"]]).replace("_", " ")
            t_txt = " ".join(tokens[t["start"]:t["end"]]).replace("_", " ")
            is_nested_rel = (
                (t["start"] >= h["start"] and t["end"] <= h["end"])
                or (h["start"] >= t["start"] and h["end"] <= t["end"])
            ) and (h["start"], h["end"]) != (t["start"], t["end"])
            rel_note = " *(Quan hệ lồng nhau)*" if is_nested_rel else ""
            lines.append(f"- (`e{r['head']}` {h_txt} `[{h['type']}]`) ==[ **{r['type']}** ]==> (`e{r['tail']}` {t_txt} `[{t['type']}]`){rel_note}")
        lines.append("")
    return "\n".join(lines)


def export_per_doc_data(per_doc, doc_split_map, out_dir):
    by_doc_dir = os.path.join(out_dir, "by_doc_spert")
    os.makedirs(by_doc_dir, exist_ok=True)
    index_rows = []
    order = ["id", "doc", "category", "kind", "text", "tokens", "entities", "relations"]

    for (cat, dname), samples in sorted(per_doc.items(), key=lambda x: (x[0][0], x[0][1])):
        split_name = doc_split_map.get((cat, dname), "train")
        cat_dir = os.path.join(by_doc_dir, cat)
        os.makedirs(cat_dir, exist_ok=True)

        clean_samples = [{k: s[k] for k in order if k in s} for s in samples]
        doc_data = {
            "doc": dname,
            "category": cat,
            "split": split_name,
            "total_samples": len(clean_samples),
            "total_entities": sum(len(s["entities"]) for s in clean_samples),
            "total_relations": sum(len(s["relations"]) for s in clean_samples),
            "samples": clean_samples
        }

        json_file = os.path.join(cat_dir, f"{dname}.json")
        with open(json_file, "w", encoding="utf-8") as f:
            json.dump(doc_data, f, ensure_ascii=False, indent=1)

        preview_file = os.path.join(cat_dir, f"{dname}_preview.md")
        md_content = [
            f"# Dữ liệu gán nhãn văn bản: {dname}",
            f"- **Thể loại**: `{cat}`",
            f"- **Phân vùng dữ liệu**: `{split_name.upper()}`",
            f"- **Tổng số mẫu**: {len(clean_samples)} mẫu",
            f"- **Tổng số thực thể**: {doc_data['total_entities']}",
            f"- **Tổng số quan hệ**: {doc_data['total_relations']}",
            "\n---\n"
        ]
        for s in clean_samples:
            md_content.append(render_sample_markdown(s))
            md_content.append("\n---\n")

        with open(preview_file, "w", encoding="utf-8") as f:
            f.write("\n".join(md_content))

        index_rows.append({
            "doc": dname,
            "cat": cat,
            "split": split_name.upper(),
            "samples": len(clean_samples),
            "entities": doc_data["total_entities"],
            "relations": doc_data["total_relations"],
            "rel_path": f"{cat}/{dname}_preview.md"
        })

    index_md = [
        "# MỤC LỤC TẬP DỮ LIỆU ĐÃ TÁCH THEO TỪNG VĂN BẢN (PER-DOCUMENT DATASET)",
        "",
        "Bảng tổng hợp toàn bộ các văn bản pháp luật, phân chia tập huấn luyện và liên kết tới bản kiểm tra trực quan chi tiết:",
        "",
        "| STT | Văn bản | Thể loại | Phân vùng | Số mẫu | Thực thể | Quan hệ | Chi tiết |",
        "| :---: | :--- | :---: | :---: | :---: | :---: | :---: | :---: |"
    ]
    for idx, row in enumerate(index_rows, 1):
        index_md.append(
            f"| {idx} | **{row['doc']}** | `{row['cat']}` | `{row['split']}` | {row['samples']} | {row['entities']} | {row['relations']} | [Xem Preview]({row['rel_path']}) |"
        )
    with open(os.path.join(by_doc_dir, "INDEX.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(index_md))
    print(f"[*] Đã xuất {len(index_rows)} văn bản vào {by_doc_dir} kèm INDEX.md và Preview.")


# ======================================================================
# 3B. Nhân bản Đa Lĩnh Vực trên Tập Train (Cross-Domain Slot Augmentation)
# ======================================================================
CROSS_DOMAIN_SLOTS = {
    "GIAY_TO_HO_SO": [
        # Y tế & Dược
        "Giấy chứng nhận đủ điều kiện kinh doanh dược",
        "chứng chỉ hành nghề khám bệnh, chữa bệnh",
        "hồ sơ đề nghị cấp chứng chỉ hành nghề dược",
        "Giấy phép hoạt động khám bệnh, chữa bệnh",
        "Giấy đăng ký lưu hành thuốc và nguyên liệu làm thuốc",
        # Đất đai, Nhà ở & Xây dựng
        "Giấy chứng nhận quyền sử dụng đất, quyền sở hữu nhà ở",
        "hồ sơ đề nghị cấp Giấy chứng nhận quyền sử dụng đất",
        "Giấy phép xây dựng công trình",
        "chứng chỉ hành nghề hoạt động xây dựng",
        "Báo cáo nghiên cứu khả thi đầu tư xây dựng",
        # Tài nguyên & Môi trường
        "Giấy phép môi trường",
        "hồ sơ đề nghị cấp giấy phép môi trường",
        "Báo cáo đánh giá tác động môi trường",
        "Giấy phép khai thác khoáng sản",
        "Giấy phép thăm dò khoáng sản",
        # Tư pháp, Luật sư, Công chứng, Đấu giá
        "hồ sơ đề nghị bổ nhiệm công chứng viên",
        "hồ sơ đề nghị thành lập Văn phòng công chứng",
        "Giấy đăng ký hoạt động của Văn phòng công chứng",
        "Giấy đăng ký hành nghề luật sư",
        "Giấy xác nhận đã nộp lại Giấy đăng ký hành nghề luật sư",
        "chứng chỉ hành nghề đấu giá",
        "Thẻ công chứng viên",
        "Điều lệ của tổ chức xã hội nghề nghiệp của công chứng viên",
        # Tài chính, Ngân hàng, Chứng khoán, Kiểm toán
        "hồ sơ đăng ký chào bán, phát hành chứng khoán",
        "hồ sơ đăng ký chào bán, phát hành cổ phiếu",
        "Giấy chứng nhận đủ điều kiện kinh doanh chứng khoán",
        "Báo cáo tỷ lệ an toàn tài chính",
        "Báo cáo tài chính năm đã được kiểm toán",
        "Quy chế kiểm soát chất lượng kiểm toán",
        "Điều lệ quỹ tín dụng nhân dân",
        # Thương mại, An toàn thực phẩm, Hải quan, Giao thông, Nội vụ
        "Giấy chứng nhận cơ sở đủ điều kiện an toàn thực phẩm",
        "Giấy xác nhận nội dung quảng cáo",
        "Giấy chứng nhận xuất xứ hàng hóa",
        "tờ khai hải quan hàng hóa xuất khẩu, nhập khẩu",
        "Giấy phép kinh doanh vận tải bằng xe ô tô",
        "Giấy chứng nhận kiểm định an toàn kỹ thuật và bảo vệ môi trường",
        "Hồ sơ trình đề nghị bổ nhiệm",
        "Quy chế xét tặng Kỷ niệm chương",
        "Quy chế thông tin cảnh báo, dự báo thiên tai trên biển",
    ],
    "TO_CHUC_DOANH_NGHIEP": [
        # Y tế, Giáo dục & Khoa học công nghệ
        "cơ sở khám bệnh, chữa bệnh",
        "doanh nghiệp kinh doanh dược",
        "cơ sở giáo dục nghề nghiệp",
        "tổ chức khoa học và công nghệ",
        "tổ chức đánh giá sự phù hợp",
        # Tư pháp & Bổ trợ tư pháp
        "Văn phòng công chứng",
        "Phòng công chứng",
        "Tổ chức hành nghề công chứng",
        "tổ chức hành nghề luật sư",
        "Văn phòng luật sư",
        "Công ty luật trách nhiệm hữu hạn một thành viên",
        "Công ty luật trách nhiệm hữu hạn hai thành viên trở lên",
        "Công ty luật hợp danh",
        "Ban chủ nhiệm Đoàn luật sư",
        "tổ chức đấu giá tài sản",
        "Văn phòng thừa phát lại",
        # Tài chính, Ngân hàng & Chứng khoán
        "Tổng công ty lưu ký và bù trừ chứng khoán Việt Nam",
        "Tổng công ty lưu ký và bù trừ chứng khoán Việt Nam và công ty con",
        "Sở giao dịch chứng khoán Việt Nam và công ty con",
        "công ty quản lý quỹ đầu tư chứng khoán",
        "công ty đầu tư chứng khoán",
        "tổ chức kiểm toán được chấp thuận",
        "thành viên lưu ký",
        "thành viên bù trừ",
        "Ngân hàng Hợp tác xã Việt Nam",
        "ngân hàng hợp tác xã",
        "Quỹ bảo đảm an toàn hệ thống quỹ tín dụng nhân dân",
        "quỹ tín dụng nhân dân thành viên",
        "doanh nghiệp thẩm định giá",
        "doanh nghiệp kinh doanh bảo hiểm",
        # Đất đai, Xây dựng, Giao thông, Thương mại
        "Văn phòng đăng ký đất đai",
        "Trung tâm phát triển quỹ đất",
        "doanh nghiệp kinh doanh bất động sản",
        "hợp tác xã kinh doanh vận tải",
        "Trung tâm sát hạch lái xe",
        "tập đoàn xuyên quốc gia",
    ],
}


def augment_train_cross_domain_samples(train_samples, tokenizer, rng, max_aug_samples=950):
    """
    Nhân bản Đa Lĩnh Vực (Cross-Domain Slot Augmentation) chỉ trên tập Train:
    Thay thế các thực thể GIAY_TO_HO_SO và TO_CHUC_DOANH_NGHIEP trong các câu mẫu thực tế
    bằng thuật ngữ chuyên ngành của 12 lĩnh vực pháp luật khác nhau, tự động dịch chuyển
    chính xác tọa độ token (start, end) của thực thể vệ tinh, thực thể lồng bên ngoài (Outer Hub / Điều / Khoản)
    và giữ nguyên toàn bộ liên kết quan hệ.
    """
    tokenized_slots = {
        etype: [vi_tokenize(phrase) for phrase in phrases if 2 <= len(vi_tokenize(phrase)) <= 12]
        for etype, phrases in CROSS_DOMAIN_SLOTS.items()
    }
    candidates = [
        s for s in train_samples
        if s.get("kind") in ("body_context", "body_standalone")
        and any(e["type"] in ("GIAY_TO_HO_SO", "TO_CHUC_DOANH_NGHIEP") for e in s.get("entities", []))
    ]
    rng.shuffle(candidates)
    augmented = []
    slot_cursors = {"GIAY_TO_HO_SO": 0, "TO_CHUC_DOANH_NGHIEP": 0}

    for s in candidates:
        if len(augmented) >= max_aug_samples:
            break
        ents = s["entities"]
        # Chọn các thực thể vệ tinh nguyên tử (không chứa thực thể khác bên trong) thuộc GIAY_TO_HO_SO / TO_CHUC_DOANH_NGHIEP
        replaceable = []
        for idx_e, e in enumerate(ents):
            if e["type"] not in ("GIAY_TO_HO_SO", "TO_CHUC_DOANH_NGHIEP"):
                continue
            st, ed = e["start"], e["end"]
            # Đảm bảo không có thực thể nào cắt ngang hoặc nằm lồng bên trong e
            has_inner_or_partial = False
            for idx_o, o in enumerate(ents):
                if idx_o == idx_e:
                    continue
                if o["start"] < ed and st < o["end"]:
                    if not (o["start"] <= st and o["end"] >= ed):
                        has_inner_or_partial = True
                        break
                    if (o["start"], o["end"]) == (st, ed):
                        has_inner_or_partial = True
                        break
            if not has_inner_or_partial:
                replaceable.append((idx_e, e))

        if not replaceable:
            continue

        # Chọn thực thể đầu tiên (hoặc ngẫu nhiên) để hoán đổi sang lĩnh vực mới
        target_idx, target_ent = rng.choice(replaceable)
        etype = target_ent["type"]
        pool = tokenized_slots[etype]
        new_ent_tokens = pool[slot_cursors[etype] % len(pool)]
        slot_cursors[etype] += 1

        st, ed = target_ent["start"], target_ent["end"]
        old_len = ed - st
        new_len = len(new_ent_tokens)
        delta = new_len - old_len

        new_tokens = list(s["tokens"][:st]) + list(new_ent_tokens) + list(s["tokens"][ed:])
        if len(new_tokens) > MAX_WORDS_BODY:
            continue
        if tokenizer is not None and subword_len(new_tokens, tokenizer) > MAX_SUBWORDS:
            continue

        new_entities = []
        for idx_e, e in enumerate(ents):
            e_copy = dict(e)
            if idx_e == target_idx:
                e_copy["start"] = st
                e_copy["end"] = st + new_len
            elif e["end"] <= st:
                pass
            elif e["start"] >= ed:
                e_copy["start"] = e["start"] + delta
                e_copy["end"] = e["end"] + delta
            elif e["start"] <= st and e["end"] >= ed:
                # Thực thể bao ngoài (Outer Hub / DIEU / KHOAN / DIEM)
                e_copy["end"] = e["end"] + delta
            e_copy["text"] = " ".join(new_tokens[e_copy["start"]:e_copy["end"]])
            new_entities.append(e_copy)

        aug_sample = {
            "id": f"{s['id']}_aug{len(augmented)}",
            "doc": s["doc"],
            "category": s["category"],
            "kind": s["kind"],
            "text": " ".join(new_tokens),
            "tokens": new_tokens,
            "entities": new_entities,
            "relations": [dict(r) for r in s["relations"]],
        }
        try:
            check_sample(aug_sample)
            augmented.append(aug_sample)
        except AssertionError:
            continue

    return augmented


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--seed", type=int, default=42)
    ap.add_argument("--split", type=str, default="0.8,0.1,0.1")
    ap.add_argument("--no-tokenizer-check", action="store_true")
    args = ap.parse_args()
    rng = random.Random(args.seed)

    tokenizer = None
    if not args.no_tokenizer_check:
        from transformers import AutoTokenizer
        print("[*] Đang nạp tokenizer vinai/phobert-base-v2...")
        tokenizer = AutoTokenizer.from_pretrained("vinai/phobert-base-v2")

    stats = Counter()
    per_doc = defaultdict(list)
    doc_dirs = sorted(glob.glob(os.path.join(RAW_DIR, "*", "*")))
    doc_dirs = [d for d in doc_dirs if os.path.isdir(d)]
    print(f"[*] Tìm thấy {len(doc_dirs)} thư mục văn bản trong {RAW_DIR}.")

    for ddir in doc_dirs:
        cat = os.path.basename(os.path.dirname(ddir))
        dname = os.path.basename(ddir)
        try:
            samples = build_samples_for_document(ddir, rng)
        except Exception as ex:
            stats["docs_error"] += 1
            print(f"[!] Lỗi khi xử lý {dname}: {ex}")
            continue

        if not samples:
            stats["docs_empty"] += 1
            continue

        stats["docs_processed"] += 1
        valid_samples = []
        for i, s in enumerate(samples):
            s["text"] = " ".join(s["tokens"])
            for e in s["entities"]:
                e["text"] = " ".join(s["tokens"][e["start"]:e["end"]])
            check_sample(s)
            if tokenizer is not None and subword_len(s["tokens"], tokenizer) > MAX_SUBWORDS:
                stats["dropped_too_long"] += 1
                continue
            s["id"] = f"{dname}#{s['kind']}_{i}"
            s["doc"] = dname
            s["category"] = cat
            valid_samples.append(s)

        per_doc[(cat, dname)] = valid_samples

    # Chia train/dev/test THEO VĂN BẢN (tránh rò rỉ dữ liệu)
    # Lưu ý: 45_2019_QH14_139264 được chỉ định vào train để mô hình học trực tiếp đặc tính Bộ luật Lao động
    ratios = [float(x) for x in args.split.split(",")]
    splits = {"train": [], "dev": [], "test": []}
    doc_split_map = {}
    by_cat = defaultdict(list)
    for key in per_doc:
        by_cat[key[0]].append(key)

    for cat, keys in by_cat.items():
        keys.sort()
        rng.shuffle(keys)
        # Đảm bảo 45_2019 luôn nằm trong train
        if cat == "bo_luat":
            target_key = ("bo_luat", "45_2019_QH14_139264")
            if target_key in keys:
                keys.remove(target_key)
                keys.insert(0, target_key)

        n = len(keys)
        n_tr = int(round(n * ratios[0]))
        n_dev = int(round(n * ratios[1]))
        if n_tr == 0:
            n_tr = 1

        for j, k in enumerate(keys):
            name = "train" if j < n_tr else ("dev" if j < n_tr + n_dev else "test")
            splits[name].extend(per_doc[k])
            doc_split_map[k] = name

    # Nhân bản Đa Lĩnh Vực (Cross-Domain Slot Augmentation) trên tập TRAIN (giữ nguyên DEV và TEST)
    aug_train = augment_train_cross_domain_samples(splits["train"], tokenizer, rng, max_aug_samples=950)
    splits["train"].extend(aug_train)
    stats["augmented_cross_domain"] = len(aug_train)
    print(f"[+] Đã sinh thêm {len(aug_train)} mẫu nhân bản đa lĩnh vực (Cross-Domain Slot Augmentation) cho tập TRAIN.")

    os.makedirs(OUT_DIR, exist_ok=True)
    order = ["id", "doc", "category", "kind", "text", "tokens", "entities", "relations"]
    for name, data in splits.items():
        clean_data = [{k: s[k] for k in order} for s in data]
        out_file = os.path.join(OUT_DIR, f"{name}.json")
        with open(out_file, "w", encoding="utf-8") as f:
            json.dump(clean_data, f, ensure_ascii=False, indent=1)
        print(f"[+] Đã ghi tập {name.upper()}: {len(clean_data)} mẫu ({len({s['doc'] for s in clean_data})} văn bản) -> {out_file}")

    # Xuất dữ liệu preview từng văn bản
    export_per_doc_data(per_doc, doc_split_map, OUT_DIR)

    # Thống kê tổng hợp
    report = {
        "pipeline": dict(stats),
        "splits": {}
    }
    for name, data in splits.items():
        ent_c, rel_c, kind_c = Counter(), Counter(), Counter()
        for s in data:
            kind_c[s["kind"]] += 1
            for e in s["entities"]:
                ent_c[e["type"]] += 1
            for r in s["relations"]:
                rel_c[r["type"]] += 1
        report["splits"][name] = {
            "docs": len({s["doc"] for s in data}),
            "samples": len(data),
            "kinds": dict(kind_c),
            "entities": dict(ent_c.most_common()),
            "relations": dict(rel_c.most_common()),
        }

    stats_path = os.path.join(OUT_DIR, "stats.json")
    with open(stats_path, "w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=1)
    print(f"\n[+] Thống kê tổng hợp đã lưu vào {stats_path}:")
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
