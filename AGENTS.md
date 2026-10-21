# AGENTS.md — Hướng Dẫn Kiến Trúc & Quy Trình Dự Án Trích Xuất Đồ Thị Tri Thức Pháp Luật Việt Nam (PhoBERT-SpERT)

Tài liệu này cung cấp hướng dẫn chuẩn về kiến trúc, hệ thống nhãn (Ontology 26 Thực thể & 19 Quan hệ 100% Tiếng Việt), cấu trúc mã nguồn, bộ dữ liệu, kết quả huấn luyện và quy trình chạy thực nghiệm cho các AI Agent và nhà phát triển làm việc trên dự án.

---

## 1. Tổng Quan Dự Án (Project Overview)

Dự án xây dựng hệ thống **Joint Entity and Relation Extraction (Trích xuất đồng thời Thực thể & Quan hệ)** trên văn bản quy phạm pháp luật Việt Nam (Luật, Bộ luật, Nghị định, Thông tư, Quyết định, Nghị quyết...) dựa trên kiến trúc **PhoBERT-SpERT** (`vinai/phobert-base-v2` kết hợp Span-based Joint Entity & Relation Extraction).

### Điểm nổi bật của kiến trúc:
- **Mô hình**: [`PhoBERTSpERT`](file:///C:/Users/A.Long/OneDrive/Desktop/NCKH/models/spert_phobert.py) hỗ trợ nhận diện **Thực thể lồng nhau (Nested Entities)**:
  - **Outer Span (Thực thể trung tâm / Mệnh đề - Hub)**: Nhận diện toàn bộ mệnh đề hành vi vi phạm (`HANH_VI_VI_PHAM`), nghĩa vụ/quyền hạn (`NGHIA_VU_QUYEN`), chế tài xử phạt (`HINH_PHAT_CHE_TAI`), biện pháp khắc phục hậu quả (`BIEN_PHAP_KHAC_PHUC`) với độ dài span tối đa `max_span_size = 60` từ.
  - **Inner Span (Thực thể vệ tinh - Satellite)**: Nhận diện các thành phần chi tiết nằm bên trong hoặc xung quanh mệnh đề như chủ thể cá nhân (`CHU_THE_CA_NHAN`), tổ chức/doanh nghiệp (`TO_CHUC_DOANH_NGHIEP`), cơ quan thẩm quyền (`CO_QUAN_THAM_QUYEN`), mức tiền (`MUC_TIEN`), thời hạn (`THOI_HAN`), lĩnh vực (`LINH_VUC`), từ khóa pháp lý (`TU_KHOA_PHAP_LY`), tham chiếu pháp lý (`THAM_CHIEU_PHAP_LY`)...
- **Hệ nhãn 100% Tiếng Việt (`UPPERCASE_SNAKE_CASE`)**: Gồm **26 loại thực thể** và **19 loại quan hệ** không pha trộn tiếng Anh.
- **Tách biệt ngữ cảnh ngày tháng & văn bản**:
  - Phân biệt rõ `NGAY_BAN_HANH` (ngày ban hành của chính văn bản hiện hành) với `NGAY_THAM_CHIEU` (ngày ban hành của văn bản được viện dẫn/sửa đổi).
  - Sử dụng thực thể neo `TU_KHOA_PHAP_LY` (`Căn cứ`, `Sửa đổi, bổ sung`, `Bãi bỏ`, `theo quy định tại`...) kết nối qua quan hệ `VIEN_DAN_THAM_CHIEU` tới `THAM_CHIEU_PHAP_LY` để tránh bỏ sót hoặc cắt cụt tên Luật/Nghị định tham chiếu.
  - Tách biệt thực thể `LINH_VUC` (`lĩnh vực chứng khoán và thị trường chứng khoán`, `lĩnh vực bổ trợ tư pháp`...) kết nối qua quan hệ `THUOC_LINH_VUC` khỏi thực thể `TAI_SAN_VAT_CHAT`.

---

## 2. Cấu Trúc Thư Mục Mã Nguồn (Repository Structure)

```text
NCKH/
├── AGENTS.md                           # Tài liệu hướng dẫn kiến trúc & quy trình cho AI Agents
├── requirements.txt                    # Danh sách thư viện phụ thuộc
├── train.py                            # Script huấn luyện & đánh giá mô hình PhoBERT-SpERT (hỗ trợ FP16 AMP)
├── inference.py                        # Script suy luận nhanh cho câu / đoạn văn bản pháp luật bất kỳ
├── test_drive_document.py              # Script trích xuất & xuất báo cáo Markdown + HTML cho văn bản bất kỳ
├── visualize_document.py               # Module sinh giao diện trực quan hóa HTML (Tương tác + Toàn văn)
├── checkpoints/
│   ├── best_spert_phobert.pt           # Trọng số mô hình tốt nhất (Epoch 5 - 26 Entities, 19 Relations)
│   └── evaluation_results.json         # Kết quả đánh giá chi tiết trên tập Dev và Test
├── models/
│   ├── __init__.py
│   └── spert_phobert.py                # Kiến trúc mạng PhoBERTSpeRT (Span Classifier + Relation Classifier)
├── data/
│   ├── dataset.py                      # Dataset & DataLoader chuyển đổi từ tiếng Việt sang subword PhoBERT
│   └── legal/
│       ├── README.md                   # Tài liệu mô tả cấu trúc bộ dữ liệu pháp luật
│       ├── schema.py                   # Định nghĩa 26 nhãn Thực thể, 19 nhãn Quan hệ & Regex nền tảng
│       ├── law_lexicon.txt             # Từ điển tên các Luật / Bộ luật Việt Nam
│       ├── vi_tokenize.py              # Bộ tách từ tiếng Việt bảo toàn số hiệu văn bản pháp luật
│       ├── intra_sentence_kg.py        # Bộ trích xuất Nested Span, Hub-Satellite, Lĩnh vực & Viện dẫn nội câu
│       ├── build_dataset.py            # Pipeline xử lý 111 văn bản raw -> train.json, dev.json, test.json
│       ├── drive_client.py             # Client kết nối Google Drive API
│       ├── download_docs.py            # Script tải văn bản pháp luật từ Google Drive
│       ├── raw/                        # 111 văn bản pháp luật gốc (.doc / .docx)
│       └── processed/
│           ├── train.json              # Tập huấn luyện (89 văn bản - 6.181 mẫu)
│           ├── dev.json                # Tập kiểm định (13 văn bản - 1.088 mẫu)
│           ├── test.json               # Tập kiểm thử (9 văn bản - 547 mẫu)
│           ├── stats.json              # Thống kê chi tiết số lượng từng loại thực thể và quan hệ
│           └── by_doc_spert/           # Dữ liệu SpERT (.json & _preview.md) xuất riêng cho từng văn bản
├── utils/
│   ├── __init__.py
│   └── evaluation.py                   # Hàm tính Precision, Recall, Micro-F1 cho Entity và Relation
└── outputs/                            # Thư mục lưu báo cáo trích xuất (.md và .html) của các văn bản kiểm thử
```

---

## 3. Hệ Thống Nhãn Chuẩn (27 Thực Thể & 19 Quan Hệ — 100% Tiếng Việt)

Định nghĩa tại [`data/legal/schema.py`](file:///C:/Users/A.Long/OneDrive/Desktop/NCKH/data/legal/schema.py):

### 3.1. Danh mục 27 Nhãn Thực Thể (`ENTITY_TYPES`)

| Nhóm Thực Thể | Mã Nhãn (`ENTITY_TYPES`) | Ý Nghĩa & Ví Dụ Điển Hình |
| :--- | :--- | :--- |
| **A. Siêu dữ liệu văn bản (6 nhãn)** | `SO_HIEU` | Số hiệu văn bản hiện hành (`306/2025/NĐ-CP`, `156/2020/NĐ-CP`) |
| | `LOAI_VAN_BAN` | Loại văn bản (`NGHỊ ĐỊNH`, `THÔNG TƯ`, `LUẬT`, `QUYẾT ĐỊNH`) |
| | `CO_QUAN_BAN_HANH` | Cơ quan ban hành văn bản hiện hành (`CHÍNH PHỦ`, `BỘ TÀI CHÍNH`) |
| | `NGAY_BAN_HANH` | Ngày ban hành của chính văn bản hiện hành (`ngày 25 tháng 11 năm 2025`) |
| | `NGUOI_KY` | Người ký ban hành văn bản (`Hồ Đức Phớc`) |
| | `CHUC_DANH_NGUOI_KY` | Chức danh người ký (`PHÓ THỦ TƯỚNG`, `THỦ TƯỚNG`, `BỘ TRƯỞNG`) |
| **B. Cấu trúc phân cấp (4 nhãn)** | `CHUONG` | Chương trong văn bản hiện hành (`Chương I`, `Chương II`, `Chương 1`) |
| | `DIEU` | Điều trong văn bản hiện hành (`Điều 1`, `Điều 2`) |
| | `KHOAN` | Khoản trong văn bản hiện hành (`1.`, `2.`) |
| | `DIEM` | Điểm / Ý nhỏ trong khoản (`a)`, `b)`, `đ)`) |
| **C. Thực thể Trung tâm - Outer Hubs (4 nhãn)** | `HANH_VI_VI_PHAM` | Mệnh đề hành vi vi phạm pháp luật (Outer Span) |
| | `NGHIA_VU_QUYEN` | Mệnh đề nghĩa vụ, quyền hạn, trách nhiệm, thủ tục pháp lý (Outer Span) |
| | `HINH_PHAT_CHE_TAI` | Mệnh đề hình phạt / chế tài xử lý (`Phạt tiền từ ... đến ...`, `Tước quyền sử dụng...`) |
| | `BIEN_PHAP_KHAC_PHUC` | Mệnh đề biện pháp khắc phục hậu quả (`Buộc thu hồi...`, `Buộc nộp lại số lợi bất hợp pháp...`) |
| **D. Thực thể Vệ tinh & Đối chiếu - Inner Satellites (13 nhãn)** | `CHU_THE_CA_NHAN` | Chủ thể cá nhân / Vai trò pháp lý (`nhà đầu tư chứng khoán chuyên nghiệp`, `người hành nghề`) |
| | `TO_CHUC_DOANH_NGHIEP` | Tổ chức / Pháp nhân / Doanh nghiệp (`công ty đại chúng`, `công ty chứng khoán`) |
| | `CO_QUAN_THAM_QUYEN` | Cơ quan quản lý / Chức danh có thẩm quyền (`Ủy ban Chứng khoán Nhà nước`, `Chủ tịch UBND cấp tỉnh`) |
| | `GIAY_TO_HO_SO` | Hồ sơ / Giấy tờ / Giấy phép / Báo cáo (`hồ sơ đăng ký chào bán`, `giấy chứng nhận đăng ký`) |
| | `TAI_SAN_VAT_CHAT` | Tài sản / Chứng khoán / Trái phiếu / Tang vật (`cổ phiếu riêng lẻ`, `trái phiếu chuyển đổi`) |
| | `MUC_TIEN` | Mức tiền phạt / Giá trị tiền tệ (`50.000.000 đồng`, `1.000.000.000 đồng`) |
| | `NGUONG_DINH_LUONG` | Ngưỡng định lượng / Tỷ lệ / Số lượng (`từ 10% trở lên`, `từ 100 nhà đầu tư`) |
| | `THOI_HAN` | Thời hạn / Khoảng thời gian (`từ 01 tháng đến 03 tháng`, `trong thời hạn 10 ngày`) |
| | `DIA_DIEM` | Địa điểm / Phạm vi không gian (`tại Việt Nam`, `ra thị trường quốc tế`) |
| | `LINH_VUC` | Lĩnh vực quản lý nhà nước / phạm vi điều chỉnh (`lĩnh vực chứng khoán và thị trường chứng khoán`, `lĩnh vực bổ trợ tư pháp`) |
| | `THAM_CHIEU_PHAP_LY` | Văn bản hoặc điều khoản được viện dẫn, căn cứ, sửa đổi, bổ sung (`Luật Doanh nghiệp số 59/2020/QH14`, `khoản 3 Điều 5`) |
| | `NGAY_THAM_CHIEU` | Ngày ban hành của văn bản được viện dẫn/tham chiếu (`ngày 17 tháng 6 năm 2020`) |
| | `TU_KHOA_PHAP_LY` | Từ khóa / Động từ lập pháp neo tham chiếu (`Căn cứ`, `Sửa đổi, bổ sung`, `Bổ sung`, `Bãi bỏ`, `quy định tại`) |

---

### 3.2. Danh mục 19 Nhãn Quan Hệ (`RELATION_TYPES`)

| Nhóm Quan Hệ | Mã Quan Hệ (`RELATION_TYPES`) | Chiều Liên Kết (`Head` ➔ `Tail`) |
| :--- | :--- | :--- |
| **A. Quan hệ Cấu trúc & Metadata (6 nhãn)** | `BAN_HANH_BOI` | `SO_HIEU` ➔ `CO_QUAN_BAN_HANH` |
| | `BAN_HANH_NGAY` | `SO_HIEU` ➔ `NGAY_BAN_HANH` |
| | `KY_BOI` | `SO_HIEU` ➔ `NGUOI_KY` |
| | `LA_LOAI_VAN_BAN` | `SO_HIEU` ➔ `LOAI_VAN_BAN` |
| | `GIU_CHUC_VU` | `NGUOI_KY` ➔ `CHUC_DANH_NGUOI_KY` |
| | `THUOC_VE` | `DIEM` ➔ `KHOAN`, `KHOAN` ➔ `DIEU`, `DIEU` ➔ `CHUONG`, `DIEU` ➔ `SO_HIEU`, `CHUONG` ➔ `SO_HIEU` |
| **B. Quan hệ Nội câu, Lĩnh vực & Viện dẫn (13 nhãn)** | `THUC_HIEN_VI_PHAM` | `CHU_THE_CA_NHAN / TO_CHUC_DOANH_NGHIEP` ➔ `HANH_VI_VI_PHAM` |
| | `CO_NGHIA_VU_QUYEN` | `CHU_THE_CA_NHAN / TO_CHUC_DOANH_NGHIEP` ➔ `NGHIA_VU_QUYEN` |
| | `CO_THAM_QUYEN` | `CO_QUAN_THAM_QUYEN` ➔ `HINH_PHAT_CHE_TAI / BIEN_PHAP_KHAC_PHUC / NGHIA_VU_QUYEN` |
| | `TAC_DONG_DOI_TUONG` | `Hub` ➔ `GIAY_TO_HO_SO / TAI_SAN_VAT_CHAT` |
| | `TAC_DONG_CHU_THE` | `Hub` ➔ `CHU_THE_CA_NHAN / TO_CHUC_DOANH_NGHIEP / CO_QUAN_THAM_QUYEN` |
| | `DAN_DEN_CHE_TAI` | `HANH_VI_VI_PHAM` ➔ `HINH_PHAT_CHE_TAI / BIEN_PHAP_KHAC_PHUC` |
| | `CHIU_CHE_TAI` | `CHU_THE_CA_NHAN / TO_CHUC_DOANH_NGHIEP` ➔ `HINH_PHAT_CHE_TAI / BIEN_PHAP_KHAC_PHUC` |
| | `CO_MUC_DINH_LUONG` | `Hub / TAI_SAN_VAT_CHAT` ➔ `MUC_TIEN / NGUONG_DINH_LUONG` |
| | `TRONG_THOI_HAN` | `Hub` ➔ `THOI_HAN` |
| | `DIEN_RA_TAI` | `Hub / TO_CHUC_DOANH_NGHIEP` ➔ `DIA_DIEM` |
| | `THUOC_LINH_VUC` | `SO_HIEU / THAM_CHIEU_PHAP_LY / DIEU / KHOAN / DIEM / Hub` ➔ `LINH_VUC` |
| | `VIEN_DAN_THAM_CHIEU` | `TU_KHOA_PHAP_LY / Hub / DIEU / KHOAN / DIEM / SO_HIEU` ➔ `THAM_CHIEU_PHAP_LY` |
| | `NGAY_BAN_HANH_THAM_CHIEU` | `THAM_CHIEU_PHAP_LY` ➔ `NGAY_THAM_CHIEU` |

---

## 4. Kết Quả Huấn Luyện & Đánh Giá Hiện Tại (Benchmark Results)

Mô hình [`checkpoints/best_spert_phobert.pt`](file:///C:/Users/A.Long/OneDrive/Desktop/NCKH/checkpoints/best_spert_phobert.pt) được huấn luyện trên **111 văn bản pháp luật** (`7.402` mẫu Train / `738` mẫu Dev / `755` mẫu Test) với **5 Epochs** (FP16 Mixed Precision, `max_span_size = 60`, 4-Level Nested NMS bao gồm `CHUONG`/`DIEU`/`KHOAN`/`DIEM` toàn đoạn).

### 4.1. Tiến trình hội tụ qua 5 Epochs (trên tập Dev)
| Epoch | Train Loss | Dev Entity P | Dev Entity R | **Dev Entity F1** | Dev Relation P | Dev Relation R | **Dev Relation F1** | **Dev Joint F1** |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **1** | `0.0199` | 89.80% | 95.06% | `92.35%` | 86.39% | 89.38% | `87.86%` | `90.11%` |
| **2** | `0.0075` | 87.15% | 95.06% | `90.93%` | 86.35% | 89.79% | `88.03%` | `89.48%` |
| **3** | `0.0058` | 91.78% | 94.96% | `93.34%` | 89.87% | 89.53% | `89.70%` | `91.52%` |
| **4** | `0.0041` | 94.27% | 95.33% | `94.79%` | 93.05% | 90.31% | `91.66%` | `93.23%` |
| **5 (Best)** | **`0.0029`** | **94.90%** | **95.36%** | **`95.13%`** | **94.26%** | **90.31%** | **`92.24%`** | **`93.69%`** |

### 4.2. Kết quả kiểm thử độc lập (trên tập Test — [`checkpoints/evaluation_results.json`](file:///C:/Users/A.Long/OneDrive/Desktop/NCKH/checkpoints/evaluation_results.json))
- **Test Entity (27 nhãn gồm `CHUONG`)**:
  - **Precision**: `92.20%` | **Recall**: `91.91%` | **Micro-F1**: **`92.06%`** (`5.308 / 5.775` thực thể chuẩn)
- **Test Relation (19 nhãn)**:
  - **Precision**: `90.77%` | **Recall**: `86.15%` | **Micro-F1**: **`88.40%`** (`3.283 / 3.811` quan hệ chuẩn)
- **Test Joint F1**: **`90.23%`** (vượt mốc 90% toàn diện trên tập kiểm thử độc lập)

---

## 5. Hướng Dẫn Lệnh Thực Thi (CLI Commands)

### 5.1. Tái tạo bộ dữ liệu từ 111 văn bản gốc
Khi chỉnh sửa quy tắc nhận diện tại [`data/legal/schema.py`](file:///C:/Users/A.Long/OneDrive/Desktop/NCKH/data/legal/schema.py) hoặc [`data/legal/intra_sentence_kg.py`](file:///C:/Users/A.Long/OneDrive/Desktop/NCKH/data/legal/intra_sentence_kg.py), chạy lệnh sau để cập nhật tập dữ liệu:
```powershell
python -m data.legal.build_dataset
```

### 5.2. Huấn luyện mô hình `PhoBERT-SpERT`
```powershell
python train.py --epochs 5 --batch-size 2 --grad-accum 4 --max-span-size 60
```

### 5.3. Trích xuất & Trực quan hóa Đồ thị Tri thức cho một văn bản cụ thể
Để trích xuất toàn bộ thực thể, quan hệ và sinh báo cáo `.md` kèm giao diện `.html` vào thư mục `outputs/` (ví dụ cho Nghị định `306_2025_NĐ-CP_186388`):
```powershell
python test_drive_document.py --doc-name 306_2025_NĐ-CP_186388
```
Các file đầu ra sẽ được tự động cập nhật trong `outputs/`:
- Báo cáo chi tiết Markdown: [`outputs/ket_qua_trich_xuat_306_2025_NĐ-CP_186388.md`](file:///C:/Users/A.Long/OneDrive/Desktop/NCKH/outputs/ket_qua_trich_xuat_306_2025_NĐ-CP_186388.md)
- Giao diện trực quan hóa tương tác toàn văn: [`outputs/ket_qua_trich_xuat_306_2025_NĐ-CP_186388.html`](file:///C:/Users/A.Long/OneDrive/Desktop/NCKH/outputs/ket_qua_trich_xuat_306_2025_NĐ-CP_186388.html)

---

## 6. Quy Tắc Dành Cho AI Agent (Agent Guidelines)

1. **Nhất quán nhãn 100% Tiếng Việt**: Tuyệt đối không thêm bất kỳ nhãn tiếng Anh nào vào [`ENTITY_TYPES`](file:///C:/Users/A.Long/OneDrive/Desktop/NCKH/data/legal/schema.py#L14-L50) hoặc [`RELATION_TYPES`](file:///C:/Users/A.Long/OneDrive/Desktop/NCKH/data/legal/schema.py#L52-L81).
2. **Thứ tự ưu tiên khi trích xuất Span nội câu ([`intra_sentence_kg.py`](file:///C:/Users/A.Long/OneDrive/Desktop/NCKH/data/legal/intra_sentence_kg.py))**:
   - Trích xuất `LINH_VUC` trước `TAI_SAN_VAT_CHAT` để cụm `"lĩnh vực chứng khoán và thị trường chứng khoán"` được gán đúng nhãn `LINH_VUC`, không bị cắt rời thành `"chứng khoán"` (`TAI_SAN_VAT_CHAT`).
   - Trích xuất `TU_KHOA_PHAP_LY` và `THAM_CHIEU_PHAP_LY` trước `TO_CHUC_DOANH_NGHIEP` để các tên luật như `"Luật Doanh nghiệp"` được nhận diện trọn vẹn là `THAM_CHIEU_PHAP_LY`.
   - Mọi ngày tháng đi ngay sau `THAM_CHIEU_PHAP_LY` phải được gán nhãn `NGAY_THAM_CHIEU` (quan hệ `NGAY_BAN_HANH_THAM_CHIEU`), không được nhầm với `NGAY_BAN_HANH` của văn bản hiện hành.
3. **Đồng bộ hóa mô hình và dữ liệu**: Nếu số lượng nhãn trong [`schema.py`](file:///C:/Users/A.Long/OneDrive/Desktop/NCKH/data/legal/schema.py) thay đổi, bắt buộc phải chạy lại `python -m data.legal.build_dataset` và huấn luyện lại `python train.py` để kích thước tầng phân loại của [`PhoBERTSpERT`](file:///C:/Users/A.Long/OneDrive/Desktop/NCKH/models/spert_phobert.py) khớp với bộ nhãn mới.
