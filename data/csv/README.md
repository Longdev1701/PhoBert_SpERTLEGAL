# Dữ Liệu Đồ Thị Tri Thức Pháp Luật Việt Nam (Định dạng CSV)

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
