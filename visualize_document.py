"""
Mô-đun trực quan hóa toàn văn văn bản pháp luật (Interactive Entity & Relation Visualizer)
- Xuất HTML tương tác cao cấp:
  + Tab 1: Đọc toàn văn 100% không cắt chữ, highlight nổi bật Điều, Khoản, Điểm và các thuộc tính
  + Tab 2: Cây cấu trúc phân cấp tương tác (Điều ➔ Khoản ➔ Điểm) có thể đóng/mở và nhảy đến đoạn
  + Tab 3: Bảng chi tiết toàn bộ các Khoản và Điểm với trích đoạn, cấp bậc và liên kết cha-con
  + Tab 4: Bảng dữ liệu toàn bộ thực thể được trích xuất
  + Tab 5: Bảng dữ liệu toàn bộ quan hệ pháp lý (THUOC, BAN_HANH_BOI, NGAY_BAN_HANH, KY_BOI,...)
"""

import os
import re
import html

COLOR_MAP = {
    # 6 Thực thể Metadata
    "SO_HIEU": {"bg": "#edf2ff", "color": "#364fc7", "border": "#91a7ff"},
    "LOAI_VAN_BAN": {"bg": "#f3d9fa", "color": "#ae3ec9", "border": "#e599f7"},
    "CO_QUAN_BAN_HANH": {"bg": "#d3f9d8", "color": "#2b8a3e", "border": "#8ce99a"},
    "NGAY_BAN_HANH": {"bg": "#ffe8cc", "color": "#d9480f", "border": "#ffb366"},
    "NGUOI_KY": {"bg": "#fcc2d7", "color": "#c2255c", "border": "#f783ac"},
    "CHUC_DANH_NGUOI_KY": {"bg": "#c3fae8", "color": "#0ca678", "border": "#63e6be"},
    # 4 Thực thể Cấu trúc (Outer Structural Containers)
    "CHUONG": {"bg": "#e0e7ff", "color": "#1e3a8a", "border": "#60a5fa"},
    "DIEU": {"bg": "#eff6ff", "color": "#1971c2", "border": "#74c0fc"},
    "KHOAN": {"bg": "#fffbeb", "color": "#d97706", "border": "#fcd34d"},
    "DIEM": {"bg": "#f0fdf9", "color": "#087f5b", "border": "#63e6be"},

    # 4 Thực thể Hub (Outer Spans)
    "HANH_VI_VI_PHAM": {"bg": "#fff5f5", "color": "#c92a2a", "border": "#ff8787"},
    "NGHIA_VU_QUYEN": {"bg": "#f0fdf4", "color": "#15803d", "border": "#86efac"},
    "HINH_PHAT_CHE_TAI": {"bg": "#fef2f2", "color": "#991b1b", "border": "#f87171"},
    "BIEN_PHAP_KHAC_PHUC": {"bg": "#fff7ed", "color": "#c2410c", "border": "#fdba74"},
    # 13 Thực thể Vệ tinh / Lồng bên trong (Inner Satellite Spans)
    "CHU_THE_CA_NHAN": {"bg": "#e0f2fe", "color": "#0369a1", "border": "#7dd3fc"},
    "TO_CHUC_DOANH_NGHIEP": {"bg": "#ede9fe", "color": "#6d28d9", "border": "#c4b5fd"},
    "CO_QUAN_THAM_QUYEN": {"bg": "#dcfce7", "color": "#166534", "border": "#86efac"},
    "GIAY_TO_HO_SO": {"bg": "#fef9c3", "color": "#854d0e", "border": "#fde047"},
    "TAI_SAN_VAT_CHAT": {"bg": "#f3e8ff", "color": "#7e22ce", "border": "#d8b4fe"},
    "MUC_TIEN": {"bg": "#fee2e2", "color": "#b91c1c", "border": "#fca5a5"},
    "NGUONG_DINH_LUONG": {"bg": "#ffedd5", "color": "#9a3412", "border": "#fdba74"},
    "THOI_HAN": {"bg": "#ecfeff", "color": "#0e7490", "border": "#67e8f9"},
    "DIA_DIEM": {"bg": "#f1f5f9", "color": "#334155", "border": "#cbd5e1"},
    "THAM_CHIEU_PHAP_LY": {"bg": "#e0e7ff", "color": "#3730a3", "border": "#a5b4fc"},
    "NGAY_THAM_CHIEU": {"bg": "#ffedd5", "color": "#ea580c", "border": "#fb923c"},
    "TU_KHOA_PHAP_LY": {"bg": "#f3e8ff", "color": "#6b21a8", "border": "#c084fc"},
    "LINH_VUC": {"bg": "#ccfbf1", "color": "#0f766e", "border": "#5eead4"},
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
    # 2. Khớp sau khi chuẩn hóa dấu câu
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


def safe_annotate_html(text, entities, color_map, parent_info=None):
    """
    Gán nhãn HTML hỗ trợ Thực thể Lồng nhau 3 tầng (DIEU/KHOAN/DIEM -> Hub -> Satellite) bằng Boundary Events.
    Đảm bảo đóng/mở thẻ <span> theo đúng thứ tự LIFO không làm vỡ HTML markup.
    """
    if not entities:
        return html.escape(text)

    accepted_spans = []
    struct_containers = {"DIEU", "KHOAN", "DIEM"}
    outer_hubs = {"HANH_VI_VI_PHAM", "NGHIA_VU_QUYEN", "HINH_PHAT_CHE_TAI", "BIEN_PHAP_KHAC_PHUC"}

    # Sắp xếp thực thể dài trước (Outer Container / Hub trước), độ tự tin cao trước
    sorted_ents = sorted(
        entities,
        key=lambda e: (
            len(e["text"]),
            1 if e["type"] in struct_containers else (0 if e["type"] in outer_hubs else -1),
            e.get("confidence", 0),
        ),
        reverse=True,
    )

    for ent in sorted_ents:
        etxt = ent["text"]
        etype = ent["type"]
        conf = ent.get("confidence", 1.0)
        start = 0
        while True:
            res = find_entity_span(text, etxt, start)
            if not res:
                break
            s, e = res
            conflict = False
            for s2, e2, t2, c2 in accepted_spans:
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
                            or (outer_t in outer_hubs and inner_t not in (outer_hubs | struct_containers))
                        )
                    )
                    if not is_nested:
                        conflict = True
                        break
            if not conflict:
                accepted_spans.append((s, e, etype, conf))
                break
            start = s + 1

    if not accepted_spans:
        return html.escape(text)

    def _nest_rank(tp):
        if tp in struct_containers:
            return 0
        if tp in outer_hubs:
            return 1
        return 2

    from collections import defaultdict
    open_events = defaultdict(list)
    close_events = defaultdict(list)

    for s, e, etype, conf in accepted_spans:
        open_events[s].append((e - s, _nest_rank(etype), etype, conf))
        close_events[e].append((e - s, _nest_rank(etype), etype, conf))

    for pos in open_events:
        open_events[pos].sort(key=lambda x: (-x[0], x[1]))   # Outer span mở trước
    for pos in close_events:
        close_events[pos].sort(key=lambda x: (x[0], -x[1]))  # Inner span đóng trước

    out = []
    for idx in range(len(text) + 1):
        if idx in close_events:
            for length, _, etype, conf in close_events[idx]:
                out.append(f'<span class="ent-type-label">{etype}</span></span>')
        if idx in open_events:
            for length, _, etype, conf in open_events[idx]:
                c_info = color_map.get(etype, {"bg": "#f1f3f5", "color": "#212529", "border": "#dee2e6"})
                extra_tooltip = ""
                if parent_info:
                    if etype == "DIEM" and parent_info.get("khoan"):
                        extra_tooltip = f" | Thuộc: {parent_info['khoan']} ({parent_info.get('dieu', '')})"
                    elif etype == "KHOAN" and parent_info.get("dieu"):
                        extra_tooltip = f" | Thuộc: {parent_info['dieu']}"
                is_hub = etype in ("HANH_VI_VI_PHAM", "NGHIA_VU_QUYEN", "HINH_PHAT_CHE_TAI", "BIEN_PHAP_KHAC_PHUC")
                is_struct = etype in ("DIEU", "KHOAN", "DIEM")
                border_style = (
                    f"2px dashed {c_info['border']}"
                    if is_hub
                    else (f"1.5px solid {c_info['border']}" if is_struct else f"1px solid {c_info['border']}")
                )
                out.append(
                    f'<span class="entity-badge ent-{etype}" '
                    f'style="background:{c_info["bg"]}; color:{c_info["color"]}; border:{border_style};" '
                    f'data-type="{etype}" title="{etype}{extra_tooltip} | Độ tin cậy: {conf:.1%}">'
                )
        if idx < len(text):
            out.append(html.escape(text[idx]))

    # Hiển thị bổ sung các thực thể lấy từ metadata (ví dụ NGAY_BAN_HANH khi văn bản docx khuyết dòng ngày)
    matched_texts = {text[s:e] for s, e, _, _ in accepted_spans}
    extra_badges = []
    for ent in entities:
        if ent["text"] not in matched_texts and not find_entity_span(text, ent["text"]):
            etype = ent["type"]
            conf = ent.get("confidence", 1.0)
            c_info = color_map.get(etype, {"bg": "#f1f3f5", "color": "#212529", "border": "#dee2e6"})
            extra_badges.append(
                f' <span class="entity-badge ent-{etype}" '
                f'style="background:{c_info["bg"]}; color:{c_info["color"]}; border:1px solid {c_info["border"]};" '
                f'data-type="{etype}" title="{etype} (Thuộc tính văn bản) | Độ tin cậy: {conf:.1%}">'
                f'{html.escape(ent["text"])}<span class="ent-type-label">{etype}</span></span>'
            )

    return "".join(out) + "".join(extra_badges)


def build_html_viewer(doc_name, metadata, all_entities, all_relations, paragraphs, output_html_path):
    """
    Sinh tệp HTML tương tác hiển thị 100% toàn văn văn bản gốc,
    highlight đầy đủ Điều, Khoản, Điểm và cung cấp Cây cấu trúc, Bảng chi tiết Khoản/Điểm.
    """
    para_map = {}
    for ent in all_entities:
        pidx = ent.get("para_idx", 1)
        para_map.setdefault(pidx, []).append(ent)

    para_rel_map = {}
    rel_stats = {}
    for rel in all_relations:
        pidx = rel.get("para_idx", 1)
        if isinstance(pidx, int):
            para_rel_map.setdefault(pidx, []).append(rel)
        rtype = rel.get("relation", "UNKNOWN")
        rel_stats[rtype] = rel_stats.get(rtype, 0) + 1

    # Thống kê thực thể
    stats = {}
    for e in all_entities:
        stats[e["type"]] = stats.get(e["type"], 0) + 1

    so_hieu = metadata.get('attributes', {}).get('so_hieu', metadata.get('metadata', {}).get('number', doc_name))
    title = metadata.get('metadata', {}).get('title', doc_name)
    co_quan = metadata.get('attributes', {}).get('co_quan_ban_hanh', 'N/A')
    ngay_ban_hanh = metadata.get('attributes', {}).get('ngay_ban_hanh', 'N/A')

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

    # Trích xuất cấu trúc phân cấp Chương -> Điều -> Khoản -> Điểm cho từng đoạn văn bản
    chuong_re = re.compile(r"^(?:(?:Chương|Phần)\s+([IVX0-9]+[a-z]?)(?:[.:\s]|$)|Chương\s+[IVX0-9]+)", re.I)
    dieu_re = re.compile(r"^(?:Điều|Đỉều)\s+(\d+[a-z]?)(?:[.:]|\b)", re.I)
    khoan_re = re.compile(r"^(?:Khoản\s+(\d+[a-z]?)[.:,]?|(\d+)\.)(?:\s+|$)", re.I)
    diem_re = re.compile(r"^[“\"]?(?:Điểm\s+([a-zđ]\d?)[.):,]?|([a-zđ]\d?)[),]|(\([ivx]+\)))(?:\s+|$)", re.I)

    para_hierarchy = {}
    hierarchy_tree = []
    clauses_and_points_list = []

    cur_chuong_obj = None
    cur_chuong_name = None
    cur_dieu_obj = None
    cur_khoan_obj = None
    cur_dieu_name = None
    cur_khoan_name = None

    for p_idx, text in enumerate(paragraphs, 1):
        clean_text = re.sub(r"\s+", " ", text).strip()
        if not clean_text:
            continue

        m_c = chuong_re.match(clean_text)
        m_d = dieu_re.match(clean_text)
        m_k = khoan_re.match(clean_text)
        m_p = diem_re.match(clean_text)

        if m_c and len(clean_text.split()) <= 20:
            c_num = m_c.group(1) if m_c.group(1) else ""
            cur_chuong_name = f"Chương {c_num}" if c_num else clean_text
            cur_dieu_name = None
            cur_khoan_name = None
            cur_dieu_obj = None
            cur_khoan_obj = None
            cur_chuong_obj = {
                "type": "CHUONG",
                "id": cur_chuong_name,
                "title": clean_text,
                "para_idx": p_idx,
                "dieus": []
            }
            hierarchy_tree.append(cur_chuong_obj)
            para_hierarchy[p_idx] = {"chuong": cur_chuong_name, "dieu": None, "khoan": None, "diem": None}

        elif m_d:
            cur_dieu_name = f"Điều {m_d.group(1)}"
            cur_khoan_name = None
            cur_khoan_obj = None
            cur_dieu_obj = {
                "type": "DIEU",
                "id": cur_dieu_name,
                "title": clean_text,
                "para_idx": p_idx,
                "parent_chuong": cur_chuong_name,
                "khoans": []
            }
            if cur_chuong_obj:
                cur_chuong_obj["dieus"].append(cur_dieu_obj)
            else:
                hierarchy_tree.append(cur_dieu_obj)
            para_hierarchy[p_idx] = {"chuong": cur_chuong_name, "dieu": cur_dieu_name, "khoan": None, "diem": None}

        elif m_k and cur_dieu_name:
            k_num = m_k.group(1) or m_k.group(2)
            cur_khoan_name = f"Khoản {k_num}"
            cur_khoan_obj = {
                "id": cur_khoan_name,
                "num": f"{k_num}.",
                "text": clean_text,
                "para_idx": p_idx,
                "parent_chuong": cur_chuong_name,
                "parent_dieu": cur_dieu_name,
                "diems": []
            }
            if cur_dieu_obj:
                cur_dieu_obj["khoans"].append(cur_khoan_obj)
            para_hierarchy[p_idx] = {"chuong": cur_chuong_name, "dieu": cur_dieu_name, "khoan": cur_khoan_name, "diem": None}

            # Thêm vào bảng Khoản & Điểm
            conf_val = 1.0
            p_ents = para_map.get(p_idx, [])
            for pe in p_ents:
                if pe["type"] == "KHOAN":
                    conf_val = pe.get("confidence", 1.0)
                    break
            clauses_and_points_list.append({
                "type": "KHOAN",
                "label": f"Khoản {k_num}",
                "symbol": f"{k_num}.",
                "chuong": cur_chuong_name or "-",
                "dieu": cur_dieu_name,
                "khoan": "-",
                "para_idx": p_idx,
                "conf": conf_val,
                "text": clean_text
            })
        elif m_p and cur_khoan_name:
            p_char = m_p.group(1) or m_p.group(2) or m_p.group(3)
            diem_name = f"Ý {p_char}" if p_char.startswith("(") else f"Điểm {p_char}"
            diem_sym = p_char if p_char.startswith("(") else f"{p_char})"
            diem_obj = {
                "id": diem_name,
                "char": diem_sym,
                "text": clean_text,
                "para_idx": p_idx,
                "parent_chuong": cur_chuong_name,
                "parent_dieu": cur_dieu_name,
                "parent_khoan": cur_khoan_name
            }
            if cur_khoan_obj:
                cur_khoan_obj["diems"].append(diem_obj)
            para_hierarchy[p_idx] = {"chuong": cur_chuong_name, "dieu": cur_dieu_name, "khoan": cur_khoan_name, "diem": diem_name}

            # Thêm vào bảng Khoản & Điểm
            conf_val = 1.0
            p_ents = para_map.get(p_idx, [])
            for pe in p_ents:
                if pe["type"] == "DIEM":
                    conf_val = pe.get("confidence", 1.0)
                    break
            clauses_and_points_list.append({
                "type": "DIEM",
                "label": diem_name,
                "symbol": diem_sym,
                "chuong": cur_chuong_name or "-",
                "dieu": cur_dieu_name,
                "khoan": cur_khoan_name,
                "para_idx": p_idx,
                "conf": conf_val,
                "text": clean_text
            })
        elif cur_dieu_name:
            para_hierarchy[p_idx] = {"chuong": cur_chuong_name, "dieu": cur_dieu_name, "khoan": cur_khoan_name, "diem": None}
        elif cur_chuong_name:
            para_hierarchy[p_idx] = {"chuong": cur_chuong_name, "dieu": None, "khoan": None, "diem": None}
        else:
            para_hierarchy[p_idx] = {"chuong": None, "dieu": None, "khoan": None, "diem": None}

    # 1. Xây dựng HTML danh sách đoạn văn (Tab 1) - KÈM HIỂN THỊ TRỰC TIẾP QUAN HỆ TRONG TỪNG ĐOẠN
    STRUCTURAL_RELS = {"THUOC_VE", "BAN_HANH_BOI", "BAN_HANH_NGAY", "KY_BOI", "LA_LOAI_VAN_BAN", "GIU_CHUC_VU"}
    paras_html = []
    for p_idx, text in enumerate(paragraphs, 1):
        clean_text = re.sub(r"\s+", " ", text).strip()
        if not clean_text:
            continue
        ents = para_map.get(p_idx, [])
        rels = para_rel_map.get(p_idx, [])
        hier = para_hierarchy.get(p_idx, {})

        breadcrumb_parts = []
        if hier.get("chuong"):
            breadcrumb_parts.append(hier["chuong"])
        if hier.get("dieu"):
            breadcrumb_parts.append(hier["dieu"])
        if hier.get("khoan"):
            breadcrumb_parts.append(hier["khoan"])
        if hier.get("diem"):
            breadcrumb_parts.append(hier["diem"])
        breadcrumb_str = " › ".join(breadcrumb_parts)

        breadcrumb_html = f'<span class="badge-hierarchy" title="Vị trí cấu trúc phân cấp">{html.escape(breadcrumb_str)}</span>' if breadcrumb_str else ''

        if not ents and not rels:
            paras_html.append(f"""
            <div class="para-card" id="p-{p_idx}">
                <div class="para-meta">
                    <span class="badge-idx">Đoạn {p_idx}</span>
                    {breadcrumb_html}
                </div>
                <div class="para-content">{html.escape(clean_text)}</div>
            </div>
            """)
            continue

        highlighted = safe_annotate_html(clean_text, ents, COLOR_MAP, hier) if ents else html.escape(clean_text)

        # Render danh sách các Quan hệ được trích xuất ngay bên dưới đoạn văn
        rels_block_html = ""
        rel_count_badge = ""
        has_intra_rel = any(r["relation"] not in STRUCTURAL_RELS for r in rels)
        if rels:
            rel_count_badge = f'<span class="badge-rel-count">🔗 {len(rels)} quan hệ</span>'
            rel_chips = []
            # Ưu tiên hiển thị các quan hệ Nội câu & Đối chiếu trước, quan hệ cấu trúc sau
            sorted_p_rels = sorted(rels, key=lambda r: (0 if r["relation"] not in STRUCTURAL_RELS else 1, -r.get("confidence", 1.0)))
            for r in sorted_p_rels:
                hc = COLOR_MAP.get(r["head_type"], {"bg": "#f1f3f5", "color": "#212529", "border": "#dee2e6"})
                tc = COLOR_MAP.get(r["tail_type"], {"bg": "#f1f3f5", "color": "#212529", "border": "#dee2e6"})
                is_intra = r["relation"] not in STRUCTURAL_RELS
                chip_cls = "rel-chip-intra" if is_intra else "rel-chip-struct"
                rel_chips.append(
                    f'<div class="para-rel-chip {chip_cls} rel-item-{r["relation"]}" data-rel="{r["relation"]}">'
                    f'<span class="rel-ent-pill" style="background:{hc["bg"]}; color:{hc["color"]}; border:1px solid {hc["border"]};">'
                    f'{html.escape(r["head"])} <small>{r["head_type"]}</small></span>'
                    f'<span class="rel-edge-arrow">──▶ <strong>{r["relation"]}</strong> <em>({r["confidence"]:.0%})</em> ──▶</span>'
                    f'<span class="rel-ent-pill" style="background:{tc["bg"]}; color:{tc["color"]}; border:1px solid {tc["border"]};">'
                    f'{html.escape(r["tail"])} <small>{r["tail_type"]}</small></span>'
                    f'</div>'
                )
            rels_block_html = (
                f'<div class="para-relations-box">'
                f'<div class="para-relations-header">🔗 Quan hệ trích xuất trong đoạn ({len(rels)}):</div>'
                f'<div class="para-relations-list">{"".join(rel_chips)}</div>'
                f'</div>'
            )

        intra_cls = "has-intra-rel" if has_intra_rel else ""
        paras_html.append(f"""
        <div class="para-card has-entity {intra_cls}" id="p-{p_idx}">
            <div class="para-meta">
                <span class="badge-idx">Đoạn {p_idx}</span>
                {breadcrumb_html}
                <span class="badge-count">🏷️ {len(ents)} thực thể</span>
                {rel_count_badge}
            </div>
            <div class="para-content">{highlighted}</div>
            {rels_block_html}
        </div>
        """)

    # 2. Xây dựng Cây phân cấp Chương - Điều - Khoản - Điểm (Tab 2)
    def render_dieu_html(d):
        d_id = d["id"]
        d_title = d["title"]
        d_pidx = d["para_idx"]
        num_k = len(d["khoans"])
        num_diem = sum(len(k["diems"]) for k in d["khoans"])

        khoans_html = []
        for k in d["khoans"]:
            k_id = k["id"]
            k_text = k["text"]
            k_pidx = k["para_idx"]
            diems_in_k = k["diems"]

            diems_html = []
            for dm in diems_in_k:
                dm_id = dm["id"]
                dm_text = dm["text"]
                dm_pidx = dm["para_idx"]
                diems_html.append(f"""
                <div class="tree-item tree-diem" id="tree-p-{dm_pidx}">
                    <div class="tree-header">
                        <span class="tree-badge badge-diem">{html.escape(dm_id)}</span>
                        <span class="tree-text">{html.escape(dm_text)}</span>
                        <button class="btn-jump" onclick="jumpToPara({dm_pidx})">Xem Đoạn {dm_pidx}</button>
                    </div>
                </div>
                """)

            diems_block = f'<div class="tree-children">{"".join(diems_html)}</div>' if diems_html else ''
            diem_count_tag = f'<span class="badge-subcount">{len(diems_in_k)} Điểm</span>' if diems_in_k else ''

            khoans_html.append(f"""
            <div class="tree-item tree-khoan" id="tree-p-{k_pidx}">
                <div class="tree-header" onclick="toggleTreeItem(this)">
                    <span class="tree-toggle">{"▼" if diems_in_k else "•"}</span>
                    <span class="tree-badge badge-khoan">{html.escape(k_id)}</span>
                    {diem_count_tag}
                    <span class="tree-text">{html.escape(k_text)}</span>
                    <button class="btn-jump" onclick="event.stopPropagation(); jumpToPara({k_pidx})">Xem Đoạn {k_pidx}</button>
                </div>
                {diems_block}
            </div>
            """)

        khoans_block = f'<div class="tree-children">{"".join(khoans_html)}</div>' if khoans_html else ''
        sub_info = f'<span class="badge-subcount">{num_k} Khoản | {num_diem} Điểm</span>' if (num_k or num_diem) else ''

        return f"""
        <div class="tree-item tree-dieu" id="tree-p-{d_pidx}">
            <div class="tree-header" onclick="toggleTreeItem(this)">
                <span class="tree-toggle">{"▼" if khoans_html else "•"}</span>
                <span class="tree-badge badge-dieu">{html.escape(d_id)}</span>
                {sub_info}
                <span class="tree-title">{html.escape(d_title)}</span>
                <button class="btn-jump" onclick="event.stopPropagation(); jumpToPara({d_pidx})">Xem Đoạn {d_pidx}</button>
            </div>
            {khoans_block}
        </div>
        """

    tree_html_items = []
    for item in hierarchy_tree:
        if item.get("type") == "CHUONG":
            ch_id = item["id"]
            ch_title = item["title"]
            ch_pidx = item["para_idx"]
            dieus_in_ch = item.get("dieus", [])
            num_d = len(dieus_in_ch)
            num_k = sum(len(d["khoans"]) for d in dieus_in_ch)
            num_diem = sum(sum(len(k["diems"]) for k in d["khoans"]) for d in dieus_in_ch)

            dieus_html = [render_dieu_html(d) for d in dieus_in_ch]
            dieus_block = f'<div class="tree-children">{"".join(dieus_html)}</div>' if dieus_html else ''
            sub_info = f'<span class="badge-subcount">{num_d} Điều | {num_k} Khoản | {num_diem} Điểm</span>'

            tree_html_items.append(f"""
            <div class="tree-item tree-chuong" id="tree-p-{ch_pidx}">
                <div class="tree-header" onclick="toggleTreeItem(this)">
                    <span class="tree-toggle">{"▼" if dieus_html else "•"}</span>
                    <span class="tree-badge badge-chuong">{html.escape(ch_id)}</span>
                    {sub_info}
                    <span class="tree-title-chuong">{html.escape(ch_title)}</span>
                    <button class="btn-jump" onclick="event.stopPropagation(); jumpToPara({ch_pidx})">Xem Đoạn {ch_pidx}</button>
                </div>
                {dieus_block}
            </div>
            """)
        else:
            tree_html_items.append(render_dieu_html(item))

    # 3. Xây dựng Bảng Chi Tiết Toàn Bộ Khoản & Điểm (Tab 3)
    kd_table_rows = []
    for i, item in enumerate(clauses_and_points_list, 1):
        c_badge = "badge-khoan" if item["type"] == "KHOAN" else "badge-diem"
        kd_table_rows.append(f"""
        <tr class="kd-row kd-{item['type']}">
            <td class="text-center">{i}</td>
            <td><span class="tree-badge {c_badge}">{item['type']}</span></td>
            <td><strong>{html.escape(item['label'])}</strong></td>
            <td><span class="tree-badge badge-chuong">{html.escape(item.get('chuong', '-'))}</span></td>
            <td><span class="tree-badge badge-dieu">{html.escape(item['dieu'])}</span></td>
            <td>{html.escape(item['khoan'])}</td>
            <td class="text-center"><span class="badge-idx">Đoạn {item['para_idx']}</span></td>
            <td class="text-center">{item['conf']:.1%}</td>
            <td class="cell-text">{html.escape(item['text'])}</td>
            <td class="text-center"><button class="btn-jump" onclick="jumpToPara({item['para_idx']})">Xem</button></td>
        </tr>
        """)

    # 4. Xây dựng Bảng Dữ Liệu Tất Cả Thực Thể (Tab 4)
    ent_table_rows = []
    for i, ent in enumerate(all_entities, 1):
        c_info = COLOR_MAP.get(ent["type"], {"bg": "#f1f3f5", "color": "#212529", "border": "#dee2e6"})
        pidx = ent.get("para_idx", "-")
        ctx = ent.get("context", "")
        ent_table_rows.append(f"""
        <tr class="ent-row ent-type-{ent['type']}">
            <td class="text-center">{i}</td>
            <td class="cell-nowrap"><span class="type-pill" style="background:{c_info['bg']}; color:{c_info['color']}; border:1px solid {c_info['border']}">{ent['type']}</span></td>
            <td class="cell-text"><strong>{html.escape(ent['text'])}</strong></td>
            <td class="text-center cell-nowrap"><span class="badge-idx">Đoạn {pidx}</span></td>
            <td class="text-center cell-nowrap">{ent['confidence']:.1%}</td>
            <td class="cell-text">{html.escape(ctx)}</td>
            <td class="text-center cell-nowrap">{f'<button class="btn-jump" onclick="jumpToPara({pidx})">Xem</button>' if isinstance(pidx, int) else ''}</td>
        </tr>
        """)

    # 5. Xây dựng Bảng Dữ Liệu Quan Hệ (Tab 5)
    rel_table_rows = []
    for i, rel in enumerate(all_relations, 1):
        pidx = rel.get("para_idx", "-")
        hc = COLOR_MAP.get(rel["head_type"], {"bg": "#f1f3f5", "color": "#212529", "border": "#dee2e6"})
        tc = COLOR_MAP.get(rel["tail_type"], {"bg": "#f1f3f5", "color": "#212529", "border": "#dee2e6"})
        is_intra = rel["relation"] not in STRUCTURAL_RELS
        rel_badge_cls = "badge-relation-intra" if is_intra else "badge-relation"
        rel_table_rows.append(f"""
        <tr class="rel-row rel-type-{rel['relation']}">
            <td class="text-center">{i}</td>
            <td class="cell-rel-ent"><div class="rel-table-box" style="background:{hc['bg']}; color:{hc['color']}; border:1px solid {hc['border']}">{html.escape(rel['head'])} <span class="ent-type-label">{rel['head_type']}</span></div></td>
            <td class="text-center cell-nowrap"><span class="{rel_badge_cls}">➔ {rel['relation']} ➔</span></td>
            <td class="cell-rel-ent"><div class="rel-table-box" style="background:{tc['bg']}; color:{tc['color']}; border:1px solid {tc['border']}">{html.escape(rel['tail'])} <span class="ent-type-label">{rel['tail_type']}</span></div></td>
            <td class="text-center cell-nowrap"><span class="badge-idx">Đoạn {pidx}</span></td>
            <td class="text-center cell-nowrap">{rel['confidence']:.1%}</td>
            <td class="text-center cell-nowrap">{f'<button class="btn-jump" onclick="jumpToPara({pidx})">Xem</button>' if isinstance(pidx, int) else ''}</td>
        </tr>
        """)

    # Filter buttons for Tab 1 (Entities + Relations)
    filter_btns = ['<button class="filter-btn active" data-filter="ALL">Tất cả đoạn</button>']
    intra_rel_total = sum(v for k, v in rel_stats.items() if k not in STRUCTURAL_RELS)
    if intra_rel_total > 0:
        filter_btns.append(
            f'<button class="filter-btn" data-filter="REL_INTRA" style="border-left: 4px solid #0ca678; background:#e6fcf5; color:#087f5b;">'
            f'🔗 Đoạn có Quan hệ Nội câu ({intra_rel_total})</button>'
        )
    for rtype, rcount in sorted(rel_stats.items(), key=lambda x: x[1], reverse=True):
        if rtype not in STRUCTURAL_RELS:
            filter_btns.append(
                f'<button class="filter-btn" data-filter="REL:{rtype}" style="border-left: 4px solid #1971c2;">'
                f'🔗 {rtype} ({rcount})</button>'
            )
    for etype, count in sorted(stats.items(), key=lambda x: x[1], reverse=True):
        c_info = COLOR_MAP.get(etype, {"bg": "#f1f3f5", "color": "#212529", "border": "#dee2e6"})
        filter_btns.append(
            f'<button class="filter-btn" data-filter="{etype}" style="border-left: 4px solid {c_info["color"]}">'
            f'🏷️ {etype} ({count})</button>'
        )

    # Filter buttons for Tab 5 (Relation Table)
    rel_filter_btns = [f'<button class="filter-btn active" data-rel-table-filter="ALL" onclick="filterRelTable(\'ALL\', this)">Tất cả ({len(all_relations)})</button>']
    if intra_rel_total > 0:
        rel_filter_btns.append(
            f'<button class="filter-btn" data-rel-table-filter="INTRA_ONLY" onclick="filterRelTable(\'INTRA_ONLY\', this)" style="border-left: 4px solid #0ca678;">'
            f'Chỉ Quan hệ Nội câu & Đối chiếu ({intra_rel_total})</button>'
        )
    for rtype, rcount in sorted(rel_stats.items(), key=lambda x: x[1], reverse=True):
        rel_filter_btns.append(
            f'<button class="filter-btn" data-rel-table-filter="{rtype}" onclick="filterRelTable(\'{rtype}\', this)">'
            f'{rtype} ({rcount})</button>'
        )

    total_ch_count = len([x for x in hierarchy_tree if x.get("type") == "CHUONG"])
    total_d_count_tree = sum(len(x.get("dieus", [])) for x in hierarchy_tree if x.get("type") == "CHUONG") + len([x for x in hierarchy_tree if x.get("type") == "DIEU"])
    total_k_count = len([x for x in clauses_and_points_list if x["type"] == "KHOAN"])
    total_d_count = len([x for x in clauses_and_points_list if x["type"] == "DIEM"])

    html_content = f"""<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Khảo Sát Thực Thể & Quan Hệ: {html.escape(so_hieu)}</title>
    <style>
        :root {{
            --primary: #1971c2;
            --primary-dark: #155799;
            --primary-light: #e7f5ff;
            --bg: #f8f9fa;
            --card-bg: #ffffff;
            --text: #212529;
            --text-muted: #6c757d;
            --border: #dee2e6;
            --success: #2b8a3e;
            --warning: #d97706;
            --danger: #c92a2a;
        }}
        * {{ box-sizing: border-box; margin: 0; padding: 0; }}
        body {{
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
            background: var(--bg);
            color: var(--text);
            line-height: 1.6;
            padding: 24px;
            overflow-x: hidden;
        }}
        .container {{
            max-width: 1380px;
            width: 100%;
            margin: 0 auto;
        }}
        /* Header Hero */
        .header {{
            background: var(--card-bg);
            border-radius: 12px;
            padding: 24px 30px;
            margin-bottom: 20px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.05);
            border: 1px solid var(--border);
        }}
        .header h1 {{ font-size: 24px; color: var(--primary); margin-bottom: 12px; display: flex; align-items: center; gap: 10px; flex-wrap: wrap; }}
        .meta-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 12px;
            margin-bottom: 18px;
        }}
        .meta-item {{
            background: #f8f9fa;
            padding: 10px 14px;
            border-radius: 8px;
            border-left: 3px solid var(--primary);
            font-size: 14px;
            overflow-wrap: anywhere;
            word-break: break-word;
        }}
        .meta-item strong {{ color: #495057; }}
        .stats-pills {{
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
            padding-top: 12px;
            border-top: 1px solid var(--border);
        }}
        .pill {{
            background: var(--primary-light);
            color: var(--primary);
            padding: 6px 14px;
            border-radius: 20px;
            font-size: 13px;
            font-weight: 600;
        }}
        .pill-gold {{ background: #fff3bf; color: #d97706; }}
        .pill-green {{ background: #e6fcf5; color: #087f5b; }}
        .pill-blue {{ background: #d0ebff; color: #1971c2; }}

        /* Tab Navigation */
        .tab-bar {{
            display: flex;
            gap: 6px;
            background: var(--card-bg);
            padding: 8px 12px;
            border-radius: 10px;
            margin-bottom: 20px;
            border: 1px solid var(--border);
            box-shadow: 0 2px 6px rgba(0,0,0,0.03);
            overflow-x: auto;
        }}
        .tab-btn {{
            background: transparent;
            border: none;
            padding: 10px 18px;
            font-size: 14px;
            font-weight: 600;
            color: #495057;
            cursor: pointer;
            border-radius: 8px;
            transition: all 0.2s;
            display: flex;
            align-items: center;
            gap: 8px;
            white-space: nowrap;
        }}
        .tab-btn:hover {{ background: #f1f3f5; color: var(--primary); }}
        .tab-btn.active {{
            background: var(--primary);
            color: #ffffff;
            box-shadow: 0 2px 6px rgba(25, 113, 194, 0.3);
        }}
        .tab-count {{
            background: rgba(0,0,0,0.12);
            padding: 2px 7px;
            border-radius: 12px;
            font-size: 11px;
        }}
        .tab-btn.active .tab-count {{ background: rgba(255,255,255,0.25); color: #fff; }}

        /* Tab Content */
        .tab-pane {{ display: block; width: 100%; max-width: 100%; }}
        .tab-pane.hidden-pane {{ display: none !important; }}

        /* Toolbar */
        .toolbar {{
            position: sticky;
            top: 12px;
            z-index: 100;
            background: var(--card-bg);
            border-radius: 10px;
            padding: 14px 20px;
            margin-bottom: 20px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.08);
            border: 1px solid var(--border);
            display: flex;
            flex-wrap: wrap;
            gap: 8px;
            align-items: center;
            max-height: 220px;
            overflow-y: auto;
        }}
        .search-box {{
            flex: 1 1 280px;
            min-width: 240px;
            padding: 9px 14px;
            border: 1px solid #ced4da;
            border-radius: 6px;
            font-size: 14px;
            outline: none;
        }}
        .search-box:focus {{ border-color: var(--primary); box-shadow: 0 0 0 3px rgba(25,113,194,0.15); }}
        .filter-btn {{
            background: #f1f3f5;
            border: 1px solid #ced4da;
            padding: 6px 12px;
            border-radius: 6px;
            font-size: 13px;
            font-weight: 500;
            cursor: pointer;
            transition: all 0.15s;
        }}
        .filter-btn:hover, .filter-btn.active {{
            background: var(--primary);
            color: #fff;
            border-color: var(--primary);
        }}

        /* Paragraph Cards */
        .para-list {{ display: flex; flex-direction: column; gap: 14px; width: 100%; }}
        .para-card {{
            background: var(--card-bg);
            border-radius: 8px;
            padding: 16px 20px;
            border: 1px solid var(--border);
            box-shadow: 0 1px 3px rgba(0,0,0,0.03);
            transition: border-color 0.2s, background-color 0.5s;
            width: 100%;
            max-width: 100%;
            overflow: hidden;
        }}
        .para-card:hover {{ border-color: #adb5bd; }}
        .para-card.para-highlight-pulse {{
            background-color: #fff9db !important;
            border-color: #f59f00 !important;
            box-shadow: 0 0 15px rgba(245, 159, 0, 0.4);
        }}
        .para-meta {{
            display: flex;
            align-items: center;
            gap: 10px;
            margin-bottom: 10px;
            font-size: 12px;
            flex-wrap: wrap;
        }}
        .badge-idx {{
            background: #e9ecef;
            color: #495057;
            padding: 2px 8px;
            border-radius: 4px;
            font-weight: bold;
            white-space: nowrap;
        }}
        .badge-hierarchy {{
            background: #e7f5ff;
            color: #1971c2;
            padding: 2px 10px;
            border-radius: 4px;
            font-weight: 600;
            border: 1px solid #a5d8ff;
        }}
        .badge-count {{
            background: #f8f9fa;
            color: #868e96;
            padding: 2px 8px;
            border-radius: 4px;
            font-weight: 500;
            border: 1px solid #dee2e6;
        }}
        .para-content {{
            font-size: 15px;
            color: #212529;
            overflow-wrap: anywhere;
            word-break: break-word;
            line-height: 2.25;
            width: 100%;
            max-width: 100%;
        }}
        /* Dùng display: inline + box-decoration-break: clone để thực thể dài & lồng nhau tự xuống dòng mượt mà, tuyệt đối không tràn ngang */
        .entity-badge {{
            display: inline;
            padding: 3px 7px;
            margin: 0 2px;
            border-radius: 5px;
            border: 1px solid transparent;
            font-weight: 600;
            cursor: pointer;
            line-height: 2.15;
            box-decoration-break: clone;
            -webkit-box-decoration-break: clone;
            overflow-wrap: anywhere;
            word-break: break-word;
            transition: box-shadow 0.15s;
        }}
        .para-content > .ent-DIEU,
        .para-content > .ent-KHOAN,
        .para-content > .ent-DIEM {{
            display: block;
            padding: 12px 16px;
            margin: 4px 0;
            border-radius: 8px;
            line-height: 2.3;
            width: 100%;
            max-width: 100%;
        }}
        .entity-badge:hover {{
            box-shadow: 0 2px 8px rgba(0,0,0,0.16);
        }}
        .ent-type-label {{
            display: inline-block;
            font-size: 10px;
            background: rgba(0,0,0,0.09);
            padding: 1px 5px;
            border-radius: 3px;
            margin-left: 5px;
            font-weight: 700;
            vertical-align: middle;
            line-height: 1.3;
            white-space: nowrap;
        }}
        .hidden-para {{ display: none !important; }}

        /* Tree Styles (Tab 2) */
        .tree-container {{
            background: var(--card-bg);
            border-radius: 12px;
            padding: 24px;
            border: 1px solid var(--border);
            box-shadow: 0 2px 8px rgba(0,0,0,0.04);
            width: 100%;
            max-width: 100%;
            overflow: hidden;
        }}
        .tree-toolbar {{
            display: flex;
            gap: 12px;
            align-items: center;
            margin-bottom: 20px;
            flex-wrap: wrap;
        }}
        .tree-item {{
            margin-bottom: 8px;
            border-radius: 6px;
            transition: background 0.15s;
            max-width: 100%;
        }}
        .tree-dieu {{
            border: 1px solid #d0ebff;
            background: #f8faff;
            margin-bottom: 12px;
        }}
        .tree-header {{
            display: flex;
            align-items: flex-start;
            flex-wrap: wrap;
            gap: 10px;
            padding: 10px 14px;
            cursor: pointer;
            user-select: none;
        }}
        .tree-header:hover {{ background: rgba(0,0,0,0.03); }}
        .tree-toggle {{
            font-size: 11px;
            color: #868e96;
            width: 16px;
            text-align: center;
            cursor: pointer;
            margin-top: 4px;
        }}
        .tree-badge {{
            padding: 2px 8px;
            border-radius: 4px;
            font-size: 12px;
            font-weight: bold;
            white-space: nowrap;
        }}
        .tree-chuong {{
            border: 1.5px solid #a5b4fc;
            background: #f8faff;
            margin-bottom: 16px;
            border-radius: 8px;
            box-shadow: 0 1px 4px rgba(30, 58, 138, 0.05);
        }}
        .tree-chuong > .tree-header {{
            background: #eef2ff;
            border-bottom: 1px solid #e0e7ff;
            padding: 12px 16px;
            border-top-left-radius: 7px;
            border-top-right-radius: 7px;
        }}
        .tree-chuong > .tree-header:hover {{
            background: #e0e7ff;
        }}
        .tree-title-chuong {{
            font-weight: 700;
            color: #1e3a8a;
            font-size: 15px;
            flex: 1 1 300px;
            white-space: normal;
            overflow-wrap: anywhere;
            word-break: break-word;
            line-height: 1.5;
        }}
        .badge-chuong {{ background: #e0e7ff; color: #1e3a8a; border: 1px solid #60a5fa; }}
        .badge-dieu {{ background: #d0ebff; color: #1971c2; border: 1px solid #74c0fc; }}
        .badge-khoan {{ background: #fff3bf; color: #d97706; border: 1px solid #fcd34d; }}
        .badge-diem {{ background: #e6fcf5; color: #087f5b; border: 1px solid #63e6be; }}
        .badge-subcount {{
            font-size: 11px;
            color: #6c757d;
            background: #fff;
            padding: 1px 6px;
            border-radius: 4px;
            border: 1px solid #dee2e6;
            white-space: nowrap;
        }}
        .tree-title {{
            font-weight: 600;
            color: #1971c2;
            flex: 1 1 300px;
            white-space: normal;
            overflow-wrap: anywhere;
            word-break: break-word;
            line-height: 1.55;
        }}
        .tree-text {{
            color: #343a40;
            font-size: 14px;
            flex: 1 1 300px;
            white-space: normal;
            overflow-wrap: anywhere;
            word-break: break-word;
            line-height: 1.55;
        }}
        .tree-children {{
            padding-left: 24px;
            padding-right: 10px;
            padding-bottom: 8px;
            border-top: 1px dashed #e9ecef;
        }}
        .tree-children.collapsed {{ display: none !important; }}
        .tree-khoan {{
            border-left: 3px solid #f59f00;
            background: #fffdf5;
            margin: 6px 0;
            border-radius: 4px;
        }}
        .tree-diem {{
            border-left: 3px solid #20c997;
            background: #f0fdf4;
            margin: 4px 0;
            border-radius: 4px;
        }}
        .btn-jump {{
            background: #fff;
            border: 1px solid #ced4da;
            padding: 3px 10px;
            border-radius: 4px;
            font-size: 12px;
            cursor: pointer;
            color: var(--primary);
            font-weight: 500;
            transition: all 0.15s;
            margin-left: auto;
            white-space: nowrap;
        }}
        .btn-jump:hover {{
            background: var(--primary);
            color: #fff;
            border-color: var(--primary);
        }}

        /* Table Styles (Tab 3, 4, 5) */
        .table-container {{
            background: var(--card-bg);
            border-radius: 12px;
            padding: 20px;
            border: 1px solid var(--border);
            box-shadow: 0 2px 8px rgba(0,0,0,0.04);
            width: 100%;
            max-width: 100%;
            overflow-x: auto;
        }}
        .data-table {{
            width: 100%;
            border-collapse: collapse;
            font-size: 14px;
        }}
        .data-table th {{
            background: #f8f9fa;
            color: #495057;
            font-weight: 600;
            text-align: left;
            padding: 12px 14px;
            border-bottom: 2px solid var(--border);
            white-space: nowrap;
        }}
        .data-table td {{
            padding: 10px 14px;
            border-bottom: 1px solid #f1f3f5;
            vertical-align: top;
        }}
        .data-table tr:hover td {{ background: #f8faff; }}
        .text-center {{ text-align: center; }}
        .cell-nowrap {{ white-space: nowrap; }}
        .cell-text {{
            max-width: 440px;
            min-width: 200px;
            white-space: normal;
            overflow-wrap: anywhere;
            word-break: break-word;
            line-height: 1.55;
            color: #343a40;
        }}
        .cell-rel-ent {{
            max-width: 390px;
            min-width: 180px;
            white-space: normal;
            overflow-wrap: anywhere;
            word-break: break-word;
        }}
        .type-pill {{
            display: inline-block;
            padding: 3px 8px;
            border-radius: 5px;
            font-weight: 700;
            font-size: 12px;
            white-space: nowrap;
        }}
        .rel-table-box {{
            display: inline-block;
            padding: 5px 10px;
            border-radius: 6px;
            font-weight: 600;
            font-size: 13px;
            line-height: 1.5;
            max-width: 100%;
            white-space: normal;
            overflow-wrap: anywhere;
            word-break: break-word;
        }}
        .badge-relation {{
            display: inline-block;
            background: #f1f3f5;
            color: #1971c2;
            padding: 3px 8px;
            border-radius: 4px;
            font-weight: 600;
            font-size: 12px;
            white-space: nowrap;
        }}
        .badge-relation-intra {{
            display: inline-block;
            background: #e6fcf5;
            color: #087f5b;
            border: 1px solid #63e6be;
            padding: 3px 8px;
            border-radius: 4px;
            font-weight: 700;
            font-size: 12px;
            white-space: nowrap;
        }}
        .badge-rel-count {{
            background: #e6fcf5;
            color: #087f5b;
            padding: 2px 8px;
            border-radius: 4px;
            font-weight: 600;
            border: 1px solid #96f2d7;
            white-space: nowrap;
        }}
        /* Per-paragraph Relations Box in Tab 1 */
        .para-relations-box {{
            margin-top: 12px;
            padding: 10px 14px;
            background: #f8fafc;
            border-top: 1px dashed #cbd5e1;
            border-radius: 6px;
            width: 100%;
            max-width: 100%;
            overflow: hidden;
        }}
        .para-relations-header {{
            font-size: 12px;
            font-weight: 700;
            color: #475569;
            margin-bottom: 8px;
            text-transform: uppercase;
            letter-spacing: 0.3px;
        }}
        .para-relations-list {{
            display: flex;
            flex-direction: column;
            gap: 8px;
            width: 100%;
        }}
        .para-rel-chip {{
            display: flex;
            flex-wrap: wrap;
            align-items: flex-start;
            gap: 8px;
            padding: 7px 12px;
            border-radius: 6px;
            font-size: 13px;
            background: #ffffff;
            border: 1px solid #e2e8f0;
            width: 100%;
            max-width: 100%;
        }}
        .para-rel-chip.rel-chip-intra {{
            background: #f0fdf4;
            border-color: #bbf7d0;
        }}
        .rel-ent-pill {{
            display: inline-block;
            padding: 4px 9px;
            border-radius: 5px;
            font-weight: 600;
            font-size: 12.5px;
            line-height: 1.5;
            max-width: 100%;
            white-space: normal;
            overflow-wrap: anywhere;
            word-break: break-word;
        }}
        .rel-ent-pill small {{
            display: inline-block;
            font-size: 10px;
            background: rgba(0,0,0,0.09);
            padding: 1px 5px;
            border-radius: 3px;
            font-weight: 700;
            margin-left: 4px;
            white-space: nowrap;
        }}
        .rel-edge-arrow {{
            color: #0f766e;
            font-size: 12px;
            font-family: monospace;
            white-space: nowrap;
            align-self: center;
        }}
        .rel-edge-arrow strong {{
            background: #ccfbf1;
            color: #115e59;
            padding: 2px 6px;
            border-radius: 4px;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
        }}
    </style>
</head>
<body>
    <div class="container">
        <!-- Header Info -->
        <div class="header">
            <h1>📄 Khảo Sát Toàn Văn Thực Thể & Quan Hệ Pháp Luật</h1>
            <div class="meta-grid">
                <div class="meta-item"><strong>Văn bản:</strong> {html.escape(title)}</div>
                <div class="meta-item"><strong>Số hiệu:</strong> <span style="color:var(--primary); font-weight:bold;">{html.escape(so_hieu)}</span></div>
                <div class="meta-item"><strong>Cơ quan ban hành:</strong> {html.escape(co_quan)}</div>
                <div class="meta-item"><strong>Ngày ban hành:</strong> {html.escape(ngay_ban_hanh)}</div>
                <div class="meta-item"><strong>Người ký:</strong> {html.escape(nguoi_ky_display)}</div>
                <div class="meta-item"><strong>Mô hình AI:</strong> PhoBERT-SpERT (Boundary + Union Context + Biaffine)</div>
            </div>
            <div class="stats-pills">
                <span class="pill pill-blue">📄 {len(paragraphs)} Đoạn văn bản</span>
                <span class="pill pill-blue">🏷️ {len(all_entities)} Tổng thực thể</span>
                <span class="pill pill-green">🔗 {len(all_relations)} Tổng quan hệ ({intra_rel_total} quan hệ nội câu)</span>
                {f'<span class="pill pill-blue" style="background:#e0e7ff; color:#1e3a8a;">📖 {total_ch_count} Chương</span>' if total_ch_count else ''}
                <span class="pill pill-blue">⚖️ {total_d_count_tree if total_d_count_tree else stats.get('DIEU', 0)} Điều</span>
                <span class="pill pill-gold">📑 {total_k_count} Khoản ({stats.get('KHOAN', 0)} thực thể)</span>
                <span class="pill pill-green">📌 {total_d_count} Điểm ({stats.get('DIEM', 0)} thực thể)</span>
            </div>
        </div>

        <!-- Navigation Tabs -->
        <div class="tab-bar">
            <button class="tab-btn active" onclick="switchTab('tab-fulltext')">
                📄 Toàn Văn Gán Nhãn & Quan Hệ <span class="tab-count">{len(paragraphs)}</span>
            </button>
            <button class="tab-btn" onclick="switchTab('tab-tree')">
                🌳 Cây Cấu Trúc {f'{total_ch_count} Chương › ' if total_ch_count else ''}{total_d_count_tree} Điều <span class="tab-count">{f'{total_ch_count} Chương | ' if total_ch_count else ''}{total_d_count_tree} Điều</span>
            </button>
            <button class="tab-btn" onclick="switchTab('tab-kd')">
                📋 Chi Tiết Khoản & Điểm <span class="tab-count">{len(clauses_and_points_list)}</span>
            </button>
            <button class="tab-btn" onclick="switchTab('tab-entities')">
                📊 Tất Cả Thực Thể <span class="tab-count">{len(all_entities)}</span>
            </button>
            <button class="tab-btn" onclick="switchTab('tab-relations')">
                🔗 Quan Hệ Pháp Lý <span class="tab-count">{len(all_relations)}</span>
            </button>
        </div>

        <!-- TAB 1: TOÀN VĂN GÁN NHÃN -->
        <div id="tab-fulltext" class="tab-pane">
            <div class="toolbar">
                <input type="text" id="searchInput" class="search-box" placeholder="🔍 Nhập từ khóa tìm kiếm (ví dụ: 'phạt tiền', 'khoản 2', 'Điều 5', 'VIEN_DAN_THAM_CHIEU')...">
                {''.join(filter_btns)}
            </div>
            <div class="para-list" id="paraList">
                {''.join(paras_html)}
            </div>
        </div>

        <!-- TAB 2: CÂY CẤU TRÚC PHÂN CẤP -->
        <div id="tab-tree" class="tab-pane hidden-pane">
            <div class="tree-container">
                <div class="tree-toolbar">
                    <input type="text" id="treeSearchInput" class="search-box" placeholder="🔍 Lọc Chương / Điều / Khoản / Điểm trong cây cấu trúc (ví dụ: 'Chương I', 'Điều 1')...">
                    <button class="filter-btn" onclick="expandAllTree(true)">Mở rộng tất cả</button>
                    <button class="filter-btn" onclick="expandAllTree(false)">Thu gọn tất cả</button>
                </div>
                <div id="treeContent">
                    {''.join(tree_html_items)}
                </div>
            </div>
        </div>

        <!-- TAB 3: BẢNG CHI TIẾT KHOẢN & ĐIỂM -->
        <div id="tab-kd" class="tab-pane hidden-pane">
            <div class="table-container">
                <div class="tree-toolbar">
                    <input type="text" id="kdSearchInput" class="search-box" placeholder="🔍 Tìm kiếm trong bảng Khoản & Điểm...">
                    <button class="filter-btn active" data-kd-filter="ALL" onclick="filterKDTable('ALL', this)">Tất cả ({len(clauses_and_points_list)})</button>
                    <button class="filter-btn" data-kd-filter="KHOAN" onclick="filterKDTable('KHOAN', this)">Chỉ Khoản ({total_k_count})</button>
                    <button class="filter-btn" data-kd-filter="DIEM" onclick="filterKDTable('DIEM', this)">Chỉ Điểm ({total_d_count})</button>
                </div>
                <table class="data-table" id="kdTable">
                    <thead>
                        <tr>
                            <th class="text-center">STT</th>
                            <th>Cấp Bậc</th>
                            <th>Ký Hiệu</th>
                            <th>Thuộc Chương</th>
                            <th>Thuộc Điều</th>
                            <th>Thuộc Khoản</th>
                            <th class="text-center">Đoạn</th>
                            <th class="text-center">Độ Tin Cậy</th>
                            <th>Trích Đoạn Nội Dung</th>
                            <th class="text-center">Thao Tác</th>
                        </tr>
                    </thead>
                    <tbody>
                        {''.join(kd_table_rows)}
                    </tbody>
                </table>
            </div>
        </div>

        <!-- TAB 4: BẢNG TẤT CẢ THỰC THỂ -->
        <div id="tab-entities" class="tab-pane hidden-pane">
            <div class="table-container">
                <div class="tree-toolbar">
                    <input type="text" id="entSearchInput" class="search-box" placeholder="🔍 Tìm kiếm thực thể theo tên, loại, nội dung...">
                </div>
                <table class="data-table" id="entTable">
                    <thead>
                        <tr>
                            <th class="text-center">STT</th>
                            <th>Loại Thực Thể</th>
                            <th>Tên / Ký Hiệu</th>
                            <th class="text-center">Vị Trí Đoạn</th>
                            <th class="text-center">Độ Tin Cậy</th>
                            <th>Ngữ Cảnh Câu Văn</th>
                            <th class="text-center">Thao Tác</th>
                        </tr>
                    </thead>
                    <tbody>
                        {''.join(ent_table_rows)}
                    </tbody>
                </table>
            </div>
        </div>

        <!-- TAB 5: BẢNG QUAN HỆ PHÁP LÝ -->
        <div id="tab-relations" class="tab-pane hidden-pane">
            <div class="table-container">
                <div class="tree-toolbar">
                    <input type="text" id="relSearchInput" class="search-box" placeholder="🔍 Tìm kiếm quan hệ (Head, Relation, Tail)...">
                    {''.join(rel_filter_btns)}
                </div>
                <table class="data-table" id="relTable">
                    <thead>
                        <tr>
                            <th class="text-center">STT</th>
                            <th>Thực Thể Nguồn (Head)</th>
                            <th>Loại Quan Hệ</th>
                            <th>Thực Thể Đích (Tail)</th>
                            <th class="text-center">Đoạn Số</th>
                            <th class="text-center">Độ Tin Cậy</th>
                            <th class="text-center">Thao Tác</th>
                        </tr>
                    </thead>
                    <tbody>
                        {''.join(rel_table_rows)}
                    </tbody>
                </table>
            </div>
        </div>
    </div>

    <script>
        // 1. Chuyển Tab
        function switchTab(tabId) {{
            document.querySelectorAll('.tab-pane').forEach(p => p.classList.add('hidden-pane'));
            document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
            
            const targetPane = document.getElementById(tabId);
            if (targetPane) targetPane.classList.remove('hidden-pane');

            const activeBtn = Array.from(document.querySelectorAll('.tab-btn')).find(b => b.getAttribute('onclick').includes(tabId));
            if (activeBtn) activeBtn.classList.add('active');
        }}

        // 2. Nhảy đến đoạn văn trong Tab Toàn Văn
        function jumpToPara(pIdx) {{
            switchTab('tab-fulltext');
            const targetCard = document.getElementById('p-' + pIdx);
            if (targetCard) {{
                targetCard.classList.remove('hidden-para');
                targetCard.scrollIntoView({{ behavior: 'smooth', block: 'center' }});
                targetCard.classList.add('para-highlight-pulse');
                setTimeout(() => targetCard.classList.remove('para-highlight-pulse'), 2500);
            }}
        }}

        // 3. Bộ lọc Tab 1 (Toàn văn - Lọc theo Thực thể hoặc Quan hệ)
        const searchInput = document.getElementById('searchInput');
        const filterBtns = document.querySelectorAll('.filter-btn[data-filter]');
        const paraCards = document.querySelectorAll('.para-card');
        let currentFilter = 'ALL';

        function applyParaFilters() {{
            const query = searchInput.value.toLowerCase().trim();
            paraCards.forEach(card => {{
                const fullText = card.textContent.toLowerCase();
                const matchesSearch = query === '' || fullText.includes(query);

                let matchesFilter = true;
                if (currentFilter === 'REL_INTRA') {{
                    matchesFilter = card.classList.contains('has-intra-rel');
                }} else if (currentFilter.startsWith('REL:')) {{
                    const rType = currentFilter.slice(4);
                    matchesFilter = !!card.querySelector(`.rel-item-${{rType}}`);
                }} else if (currentFilter !== 'ALL') {{
                    const badge = card.querySelector(`.entity-badge.ent-${{currentFilter}}`);
                    matchesFilter = !!badge;
                }}

                if (matchesSearch && matchesFilter) {{
                    card.classList.remove('hidden-para');
                }} else {{
                    card.classList.add('hidden-para');
                }}
            }});
        }}

        if (searchInput) searchInput.addEventListener('input', applyParaFilters);

        filterBtns.forEach(btn => {{
            btn.addEventListener('click', () => {{
                filterBtns.forEach(b => b.classList.remove('active'));
                btn.classList.add('active');
                currentFilter = btn.dataset.filter;
                applyParaFilters();
            }});
        }});

        // 4. Cây cấu trúc (Tab 2)
        function toggleTreeItem(headerEl) {{
            const childrenEl = headerEl.parentElement.querySelector(':scope > .tree-children');
            const toggleEl = headerEl.querySelector('.tree-toggle');
            if (childrenEl) {{
                const isCollapsed = childrenEl.classList.toggle('collapsed');
                if (toggleEl) toggleEl.textContent = isCollapsed ? '▶' : '▼';
            }}
        }}

        function expandAllTree(expand) {{
            document.querySelectorAll('.tree-children').forEach(c => {{
                if (expand) {{
                    c.classList.remove('collapsed');
                }} else {{
                    c.classList.add('collapsed');
                }}
            }});
            document.querySelectorAll('.tree-toggle').forEach(t => {{
                if (t.textContent === '▶' || t.textContent === '▼') {{
                    t.textContent = expand ? '▼' : '▶';
                }}
            }});
        }}

        const treeSearch = document.getElementById('treeSearchInput');
        if (treeSearch) {{
            treeSearch.addEventListener('input', () => {{
                const q = treeSearch.value.toLowerCase().trim();
                document.querySelectorAll('.tree-chuong, .tree-container > .tree-dieu').forEach(topEl => {{
                    const text = topEl.textContent.toLowerCase();
                    if (q === '' || text.includes(q)) {{
                        topEl.style.display = 'block';
                        if (q !== '') {{
                            topEl.querySelectorAll('.tree-children').forEach(c => c.classList.remove('collapsed'));
                        }}
                    }} else {{
                        topEl.style.display = 'none';
                    }}
                }});
            }});
        }}

        // 5. Bảng Khoản & Điểm (Tab 3)
        let currentKDFilter = 'ALL';
        function filterKDTable(type, btn) {{
            document.querySelectorAll('[data-kd-filter]').forEach(b => b.classList.remove('active'));
            if (btn) btn.classList.add('active');
            currentKDFilter = type;
            applyKDTableFilter();
        }}

        function applyKDTableFilter() {{
            const q = (document.getElementById('kdSearchInput')?.value || '').toLowerCase().trim();
            document.querySelectorAll('#kdTable tbody tr').forEach(row => {{
                const text = row.textContent.toLowerCase();
                const matchesQ = q === '' || text.includes(q);
                let matchesType = true;
                if (currentKDFilter !== 'ALL') {{
                    matchesType = row.classList.contains(`kd-${{currentKDFilter}}`);
                }}
                row.style.display = (matchesQ && matchesType) ? '' : 'none';
            }});
        }}
        document.getElementById('kdSearchInput')?.addEventListener('input', applyKDTableFilter);

        // 6. Tìm kiếm Tab 4 (Thực thể)
        document.getElementById('entSearchInput')?.addEventListener('input', (e) => {{
            const q = e.target.value.toLowerCase().trim();
            document.querySelectorAll('#entTable tbody tr').forEach(row => {{
                row.style.display = (q === '' || row.textContent.toLowerCase().includes(q)) ? '' : 'none';
            }});
        }});

        // 7. Tìm kiếm & Lọc Tab 5 (Quan hệ)
        let currentRelTableFilter = 'ALL';
        const STRUCTURAL_REL_SET = new Set(['THUOC', 'BAN_HANH_BOI', 'NGAY_BAN_HANH', 'KY_BOI', 'LA_LOAI', 'GIU_CHUC_VU']);
        function filterRelTable(type, btn) {{
            document.querySelectorAll('[data-rel-table-filter]').forEach(b => b.classList.remove('active'));
            if (btn) btn.classList.add('active');
            currentRelTableFilter = type;
            applyRelTableFilter();
        }}

        function applyRelTableFilter() {{
            const q = (document.getElementById('relSearchInput')?.value || '').toLowerCase().trim();
            document.querySelectorAll('#relTable tbody tr').forEach(row => {{
                const text = row.textContent.toLowerCase();
                const matchesQ = q === '' || text.includes(q);
                let matchesType = true;
                if (currentRelTableFilter === 'INTRA_ONLY') {{
                    matchesType = !Array.from(STRUCTURAL_REL_SET).some(sr => row.classList.contains(`rel-type-${{sr}}`));
                }} else if (currentRelTableFilter !== 'ALL') {{
                    matchesType = row.classList.contains(`rel-type-${{currentRelTableFilter}}`);
                }}
                row.style.display = (matchesQ && matchesType) ? '' : 'none';
            }});
        }}
        document.getElementById('relSearchInput')?.addEventListener('input', applyRelTableFilter);
    </script>
</body>
</html>
"""

    os.makedirs(os.path.dirname(os.path.abspath(output_html_path)), exist_ok=True)
    with open(output_html_path, "w", encoding="utf-8") as f:
        f.write(html_content)

    print(f"[THÀNH CÔNG] Đã tạo tệp HTML trực quan hóa tương tác hoàn chỉnh tại: {output_html_path}")
