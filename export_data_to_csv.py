"""
Script trích xuất toàn bộ dữ liệu Đồ thị Tri thức Pháp luật Việt Nam (PhoBERT-SpERT) sang định dạng CSV.
Bao gồm:
1. documents.csv: Danh mục 111 văn bản pháp luật và toàn bộ thuộc tính metadata.
2. entities.csv: Toàn bộ 70.197 thực thể đã chuẩn hóa nhãn (27 loại thực thể).
3. relations.csv: Toàn bộ 48.743 quan hệ / bộ ba tri thức (Knowledge Graph Triples - 19 loại quan hệ).
4. samples.csv: Toàn bộ 8.895 mẫu văn bản (Train, Dev, Test).
5. entities_summary.csv: Thống kê số lượng từng loại thực thể qua các tập.
6. relations_summary.csv: Thống kê số lượng từng loại quan hệ qua các tập.
7. real_test_extracted_entities.csv & real_test_extracted_relations.csv: Kết quả mô hình chạy suy luận trên các văn bản thực tế.
"""

import os
import re
import csv
import json
import glob
from collections import defaultdict


def load_all_documents_metadata(raw_dir="data/legal/raw"):
    docs = {}
    for doc_path in glob.glob(os.path.join(raw_dir, "*/*")):
        if not os.path.isdir(doc_path):
            continue
        doc_name = os.path.basename(doc_path)
        cat_name = os.path.basename(os.path.dirname(doc_path))
        
        tt_file = os.path.join(doc_path, "thuoc_tinh.json")
        vb_file = os.path.join(doc_path, "van_ban_goc.txt")
        
        meta = {}
        attrs = {}
        if os.path.exists(tt_file):
            try:
                with open(tt_file, "r", encoding="utf-8") as f:
                    d = json.load(f)
                    meta = d.get("metadata", {})
                    attrs = d.get("attributes", {})
            except Exception:
                pass
                
        num_paras = 0
        if os.path.exists(vb_file):
            try:
                with open(vb_file, "r", encoding="utf-8") as f:
                    num_paras = len([l for l in f if l.strip()])
            except Exception:
                pass
                
        docs[doc_name] = {
            "doc_id": doc_name,
            "category": cat_name,
            "item_id": meta.get("item_id", ""),
            "title": meta.get("title", ""),
            "url_toanvan": meta.get("url_toanvan", ""),
            "so_hieu": attrs.get("so_hieu", ""),
            "loai_van_ban": attrs.get("loai_van_ban", ""),
            "co_quan_ban_hanh": attrs.get("co_quan_ban_hanh", ""),
            "ngay_ban_hanh": attrs.get("ngay_ban_hanh", ""),
            "ngay_co_hieu_luc": attrs.get("ngay_co_hieu_luc", ""),
            "ngay_het_hieu_luc": attrs.get("ngay_het_hieu_luc", ""),
            "tinh_trang_hieu_luc": attrs.get("tinh_trang_hieu_luc", ""),
            "linh_vuc": attrs.get("linh_vuc", ""),
            "nganh": attrs.get("nganh", ""),
            "nguoi_ky": attrs.get("nguoi_ky", ""),
            "chuc_danh_nguoi_ky": attrs.get("chuc_danh_nguoi_ky", ""),
            "num_paragraphs": num_paras,
            "split": "unknown",
            "num_samples": 0,
            "num_entities": 0,
            "num_relations": 0,
        }
    return docs


def export_dataset_to_csv(output_dir="data/csv"):
    os.makedirs(output_dir, exist_ok=True)
    print(f"[*] Đang khởi tạo trích xuất toàn bộ dữ liệu ra thư mục: {output_dir}")

    docs_metadata = load_all_documents_metadata()
    print(f"  [+] Đã tải metadata của {len(docs_metadata)} văn bản pháp luật gốc.")

    splits = ["train", "dev", "test"]
    all_samples = []
    all_entities = []
    all_relations = []

    ent_summary = defaultdict(lambda: {"train": 0, "dev": 0, "test": 0, "total": 0})
    rel_summary = defaultdict(lambda: {"train": 0, "dev": 0, "test": 0, "total": 0})

    ent_global_id = 1
    rel_global_id = 1

    for split in splits:
        split_path = f"data/legal/processed/{split}.json"
        if not os.path.exists(split_path):
            print(f"  [!] Không tìm thấy {split_path}")
            continue

        with open(split_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        print(f"  [+] Đang xử lý tập {split.upper()} ({len(data)} mẫu)...")
        for sample in data:
            s_id = sample.get("id", "")
            doc_id = sample.get("doc", "")
            category = sample.get("category", "")
            kind = sample.get("kind", "")
            raw_text = sample.get("text", "")
            tokens = sample.get("tokens", [])
            entities = sample.get("entities", [])
            relations = sample.get("relations", [])

            # Cập nhật metadata văn bản
            if doc_id in docs_metadata:
                docs_metadata[doc_id]["split"] = split.upper()
                docs_metadata[doc_id]["num_samples"] += 1
                docs_metadata[doc_id]["num_entities"] += len(entities)
                docs_metadata[doc_id]["num_relations"] += len(relations)

            # Record mẫu
            all_samples.append({
                "sample_id": s_id,
                "doc_id": doc_id,
                "category": category,
                "split": split.upper(),
                "kind": kind,
                "text": raw_text,
                "token_count": len(tokens),
                "entity_count": len(entities),
                "relation_count": len(relations),
            })

            # Record thực thể
            sample_ent_objs = []
            for e_idx, e in enumerate(entities):
                etype = e.get("type", "")
                etext = e.get("text", "")
                token_start = e.get("start", -1)
                token_end = e.get("end", -1)

                ent_summary[etype][split] += 1
                ent_summary[etype]["total"] += 1

                ent_row = {
                    "entity_id": f"ENT_{ent_global_id:06d}",
                    "sample_id": s_id,
                    "doc_id": doc_id,
                    "split": split.upper(),
                    "category": category,
                    "kind": kind,
                    "entity_type": etype,
                    "text": etext,
                    "token_start": token_start,
                    "token_end": token_end,
                    "context_text": raw_text,
                }
                all_entities.append(ent_row)
                sample_ent_objs.append((etext, etype))
                ent_global_id += 1

            # Record quan hệ
            for r in relations:
                rtype = r.get("type", "")
                h_idx = r.get("head", -1)
                t_idx = r.get("tail", -1)

                head_text = sample_ent_objs[h_idx][0] if 0 <= h_idx < len(sample_ent_objs) else ""
                head_type = sample_ent_objs[h_idx][1] if 0 <= h_idx < len(sample_ent_objs) else ""
                tail_text = sample_ent_objs[t_idx][0] if 0 <= t_idx < len(sample_ent_objs) else ""
                tail_type = sample_ent_objs[t_idx][1] if 0 <= t_idx < len(sample_ent_objs) else ""

                rel_summary[rtype][split] += 1
                rel_summary[rtype]["total"] += 1

                rel_row = {
                    "relation_id": f"REL_{rel_global_id:06d}",
                    "sample_id": s_id,
                    "doc_id": doc_id,
                    "split": split.upper(),
                    "category": category,
                    "relation_type": rtype,
                    "head_text": head_text,
                    "head_type": head_type,
                    "tail_text": tail_text,
                    "tail_type": tail_type,
                    "context_text": raw_text,
                }
                all_relations.append(rel_row)
                rel_global_id += 1

    # 1. Xuất documents.csv
    docs_csv = os.path.join(output_dir, "documents.csv")
    with open(docs_csv, "w", encoding="utf-8-sig", newline="") as f:
        fields = [
            "doc_id", "item_id", "so_hieu", "loai_van_ban", "co_quan_ban_hanh", "category", "split",
            "ngay_ban_hanh", "ngay_co_hieu_luc", "ngay_het_hieu_luc", "tinh_trang_hieu_luc",
            "nguoi_ky", "chuc_danh_nguoi_ky", "linh_vuc", "nganh", "title", "url_toanvan",
            "num_paragraphs", "num_samples", "num_entities", "num_relations"
        ]
        writer = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        for d in sorted(docs_metadata.values(), key=lambda x: (x["category"], x["doc_id"])):
            writer.writerow(d)
    print(f"  [✓] Đã xuất {len(docs_metadata)} văn bản sang: {docs_csv}")

    # 2. Xuất samples.csv
    samples_csv = os.path.join(output_dir, "samples.csv")
    with open(samples_csv, "w", encoding="utf-8-sig", newline="") as f:
        fields = ["sample_id", "doc_id", "category", "split", "kind", "text", "token_count", "entity_count", "relation_count"]
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(all_samples)
    print(f"  [✓] Đã xuất {len(all_samples):,} mẫu văn bản sang: {samples_csv}")

    # 3. Xuất entities.csv
    entities_csv = os.path.join(output_dir, "entities.csv")
    with open(entities_csv, "w", encoding="utf-8-sig", newline="") as f:
        fields = ["entity_id", "doc_id", "split", "category", "kind", "entity_type", "text", "token_start", "token_end", "sample_id", "context_text"]
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(all_entities)
    print(f"  [✓] Đã xuất {len(all_entities):,} thực thể sang: {entities_csv}")

    # 4. Xuất relations.csv (Knowledge Graph Triples)
    relations_csv = os.path.join(output_dir, "relations.csv")
    with open(relations_csv, "w", encoding="utf-8-sig", newline="") as f:
        fields = ["relation_id", "doc_id", "split", "category", "relation_type", "head_text", "head_type", "tail_text", "tail_type", "sample_id", "context_text"]
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(all_relations)
    print(f"  [✓] Đã xuất {len(all_relations):,} quan hệ đồ thị sang: {relations_csv}")

    # 5. Xuất entities_summary.csv
    ent_sum_csv = os.path.join(output_dir, "entities_summary.csv")
    with open(ent_sum_csv, "w", encoding="utf-8-sig", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["entity_type", "train", "dev", "test", "total", "percentage"])
        total_e = sum(v["total"] for v in ent_summary.values()) or 1
        for etype, cnt in sorted(ent_summary.items(), key=lambda x: x[1]["total"], reverse=True):
            pct = f"{(cnt['total'] / total_e) * 100:.2f}%"
            writer.writerow([etype, cnt["train"], cnt["dev"], cnt["test"], cnt["total"], pct])
    print(f"  [✓] Đã xuất bảng thống kê 27 nhãn thực thể sang: {ent_sum_csv}")

    # 6. Xuất relations_summary.csv
    rel_sum_csv = os.path.join(output_dir, "relations_summary.csv")
    with open(rel_sum_csv, "w", encoding="utf-8-sig", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["relation_type", "train", "dev", "test", "total", "percentage"])
        total_r = sum(v["total"] for v in rel_summary.values()) or 1
        for rtype, cnt in sorted(rel_summary.items(), key=lambda x: x[1]["total"], reverse=True):
            pct = f"{(cnt['total'] / total_r) * 100:.2f}%"
            writer.writerow([rtype, cnt["train"], cnt["dev"], cnt["test"], cnt["total"], pct])
    print(f"  [✓] Đã xuất bảng thống kê 19 nhãn quan hệ sang: {rel_sum_csv}")

    # 7. Xuất các file CSV riêng theo từng tập (train / dev / test) để người dùng tiện sử dụng
    for sp in ["train", "dev", "test"]:
        sp_upper = sp.upper()
        # Entities per split
        sp_ent_file = os.path.join(output_dir, f"entities_{sp}.csv")
        with open(sp_ent_file, "w", encoding="utf-8-sig", newline="") as f:
            fields = ["entity_id", "doc_id", "category", "kind", "entity_type", "text", "token_start", "token_end", "sample_id", "context_text"]
            writer = csv.DictWriter(f, fieldnames=fields)
            writer.writeheader()
            for row in all_entities:
                if row["split"] == sp_upper:
                    row_copy = dict(row)
                    row_copy.pop("split", None)
                    writer.writerow(row_copy)
                    
        # Relations per split
        sp_rel_file = os.path.join(output_dir, f"relations_{sp}.csv")
        with open(sp_rel_file, "w", encoding="utf-8-sig", newline="") as f:
            fields = ["relation_id", "doc_id", "category", "relation_type", "head_text", "head_type", "tail_text", "tail_type", "sample_id", "context_text"]
            writer = csv.DictWriter(f, fieldnames=fields)
            writer.writeheader()
            for row in all_relations:
                if row["split"] == sp_upper:
                    row_copy = dict(row)
                    row_copy.pop("split", None)
                    writer.writerow(row_copy)

    # 8. Xuất bảng tổng hợp kết quả kiểm thử trên các văn bản thực tế
    export_real_documents_tested(output_dir=output_dir)

    # 9. Sinh tài liệu README.md mô tả cấu trúc dữ liệu CSV
    generate_csv_readme(output_dir=output_dir)

    print(f"\n[HOÀN TẤT] Toàn bộ dữ liệu đã được xuất CSV thành công vào: {output_dir}")


def export_real_documents_tested(output_dir="data/csv", outputs_dir="outputs"):
    records = []
    for md_file in glob.glob(os.path.join(outputs_dir, "ket_qua_trich_xuat_*.md")):
        doc_name = os.path.basename(md_file).replace("ket_qua_trich_xuat_", "").replace(".md", "")
        html_file = os.path.join(outputs_dir, f"ket_qua_trich_xuat_{doc_name}.html")
        
        info = {
            "doc_name": doc_name,
            "so_hieu": "",
            "title": "",
            "co_quan_ban_hanh": "",
            "nguoi_ky": "",
            "linh_vuc": "",
            "num_paras": 0,
            "num_entities": 0,
            "num_relations": 0,
            "inference_time_seconds": 0.0,
            "output_md": md_file,
            "output_html": html_file if os.path.exists(html_file) else "",
        }
        try:
            with open(md_file, "r", encoding="utf-8") as f:
                content = f.read()
            m_sh = re.search(r"\- \*\*Số hiệu\*\*:\s*`?([^`\n]+)`?", content)
            if m_sh: info["so_hieu"] = m_sh.group(1).strip()
            m_tt = re.search(r"\- \*\*Tiêu đề văn bản\*\*:\s*([^\n]+)", content)
            if m_tt: info["title"] = m_tt.group(1).strip()
            m_cq = re.search(r"\- \*\*Cơ quan ban hành\*\*:\s*([^\n]+)", content)
            if m_cq: info["co_quan_ban_hanh"] = m_cq.group(1).strip()
            m_nk = re.search(r"\- \*\*Người ký\*\*:\s*([^\n]+)", content)
            if m_nk: info["nguoi_ky"] = m_nk.group(1).strip()
            m_lv = re.search(r"\- \*\*Lĩnh vực pháp lý\*\*:\s*([^\n]+)", content)
            if m_lv: info["linh_vuc"] = m_lv.group(1).strip()
            m_time = re.search(r"\- \*\*Thời gian xử lý toàn bộ\*\*:\s*\*\*([\d\.]+) giây\*\*\s*\((\d+) đoạn văn bản\)", content)
            if m_time:
                info["inference_time_seconds"] = float(m_time.group(1))
                info["num_paras"] = int(m_time.group(2))
            m_ent = re.search(r"\|\s*\*\*Tổng số thực thể phát hiện\*\*\s*\|\s*\*\*(\d+)\*\*", content)
            if m_ent: info["num_entities"] = int(m_ent.group(1))
            m_rel = re.search(r"\|\s*\*\*Tổng số quan hệ liên kết\*\*\s*\|\s*\*\*(\d+)\*\*", content)
            if m_rel: info["num_relations"] = int(m_rel.group(1))
        except Exception as e:
            print(f"  [!] Lỗi khi đọc {md_file}: {e}")
        records.append(info)
        
    out_file = os.path.join(output_dir, "real_documents_tested.csv")
    with open(out_file, "w", encoding="utf-8-sig", newline="") as f:
        fields = [
            "doc_name", "so_hieu", "title", "co_quan_ban_hanh", "nguoi_ky", "linh_vuc",
            "num_paras", "num_entities", "num_relations", "inference_time_seconds",
            "output_md", "output_html"
        ]
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        for r in sorted(records, key=lambda x: -x["num_paras"]):
            writer.writerow(r)
    print(f"  [✓] Đã xuất {len(records)} văn bản kiểm thử thực tế sang: {out_file}")


def generate_csv_readme(output_dir="data/csv"):
    readme_path = os.path.join(output_dir, "README.md")
    content = """# Dữ Liệu Đồ Thị Tri Thức Pháp Luật Việt Nam (Định dạng CSV)

Thư mục này chứa toàn bộ dữ liệu của đề tài NCKH đã được trích xuất sang định dạng **CSV chuẩn UTF-8-BOM** (tương thích tuyệt đối với Microsoft Excel, Google Sheets, Pandas, PowerBI, SPSS, Neo4j, PostgreSQL...).

---

## 1. Danh Sách Các File CSV

| Tên Tệp CSV | Số Dòng | Dung Lượng | Mô Tả Ý Nghĩa Pháp Lý |
| :--- | :---: | :---: | :--- |
| **`documents.csv`** | 111 văn bản | ~68 KB | Bảng danh mục 111 văn bản quy phạm pháp luật (Luật, Bộ luật, Nghị định, Thông tư, Quyết định...) kèm siêu dữ liệu đầy đủ (Số hiệu, Cơ quan ban hành, Ngày ban hành, Ngày hiệu lực, Người ký, Chức danh, Lĩnh vực, Số đoạn...). |
| **`entities.csv`** | 70.197 thực thể | ~40.6 MB | Bảng dữ liệu toàn bộ thực thể được gán nhãn chuẩn hóa theo Ontology 27 nhãn (bao gồm mã thực thể, nhãn, chuỗi văn bản, vị trí token, câu ngữ cảnh và phân vùng train/dev/test). |
| **`relations.csv`** | 48.743 bộ ba | ~31.6 MB | Bảng đồ thị tri thức (Knowledge Graph Triples) gồm 19 loại quan hệ pháp lý liên kết giữa các cặp thực thể (Head Entity ➔ Relation ➔ Tail Entity). |
| **`samples.csv`** | 8.895 mẫu | ~3.9 MB | Bảng các đoạn/câu văn bản quy phạm pháp luật huấn luyện và đánh giá (Text, Category, Kind, Số token, Số thực thể, Số quan hệ). |
| **`entities_summary.csv`** | 27 loại nhãn | ~1 KB | Thống kê số lượng từng loại thực thể (27 nhãn) qua các tập Train, Dev, Test và tỷ lệ phân bố. |
| **`relations_summary.csv`** | 19 loại nhãn | ~1 KB | Thống kê số lượng từng loại quan hệ (19 nhãn) qua các tập Train, Dev, Test và tỷ lệ phân bố. |
| **`real_documents_tested.csv`** | 10 văn bản | ~3 KB | Kết quả thực tế khi chạy mô hình PhoBERT-SpERT trên các văn bản độc lập (Số đoạn, Số thực thể phát hiện, Số quan hệ phát hiện, Thời gian suy luận). |
| **`entities_train.csv`** / **`dev`** / **`test`** | - | - | Các file thực thể được tách riêng theo từng tập để phục vụ huấn luyện và kiểm thử độc lập. |
| **`relations_train.csv`** / **`dev`** / **`test`** | - | - | Các file quan hệ được tách riêng theo từng tập tương ứng. |

---

## 2. Hướng Dẫn Sử Dụng Nhanh

### Đọc dữ liệu bằng Python (Pandas)
```python
import pandas as pd

# 1. Đọc danh mục văn bản
df_docs = pd.read_csv("data/csv/documents.csv", encoding="utf-8-sig")
print("Tổng số văn bản:", len(df_docs))

# 2. Đọc toàn bộ thực thể
df_entities = pd.read_csv("data/csv/entities.csv", encoding="utf-8-sig")
print(df_entities["entity_type"].value_counts())

# 3. Đọc đồ thị tri thức (Triples)
df_relations = pd.read_csv("data/csv/relations.csv", encoding="utf-8-sig")
print(df_relations[["head_text", "relation_type", "tail_text"]].head())
```

### Mở bằng Microsoft Excel
- File được lưu mã hóa `utf-8-sig` (UTF-8 with BOM), do đó bạn chỉ cần **nhấp đúp chuột** vào bất kỳ file `.csv` nào là Microsoft Excel sẽ tự động hiển thị đúng 100% tiếng Việt có dấu mà không cần chỉnh mã trang.
"""
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")
    print(f"  [✓] Đã tạo tài liệu hướng dẫn: {readme_path}")


if __name__ == "__main__":
    export_dataset_to_csv()

