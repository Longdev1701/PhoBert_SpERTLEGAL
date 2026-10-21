# Checkpoints PhoBERT-SpERT

Thư mục này lưu trữ các checkpoint trọng số mô hình đã được huấn luyện cho bài toán Trích xuất đồng thời Thực thể và Quan hệ Pháp luật (Joint NER & Relation Extraction).

## 1. Trọng số mô hình chính (`best_spert_phobert.pt`)
- **Tập dữ liệu**: Huấn luyện trên 111 văn bản pháp luật quy phạm Việt Nam (7.402 mẫu Train / 738 mẫu Dev / 755 mẫu Test).
- **Hệ Ontology**: 27 loại Thực thể & 19 loại Quan hệ 100% Tiếng Việt.
- **Backbone**: `vinai/phobert-base-v2`.
- **Cấu hình**: 5 Epochs, Mixed Precision FP16, `max_span_size = 60`, 4-Level Nested-Aware NMS.
- **Kích thước file**: ~1.63 GB.

*Lưu ý: Do giới hạn kích thước file của GitHub (< 100 MB), các file trọng số nhị phân (`*.pt`) được quản lý riêng và không đẩy trực tiếp lên Git repository.*

## 2. Kết quả đánh giá trên tập Test độc lập
Được lưu chi tiết tại [`evaluation_results.json`](evaluation_results.json):
- **Test Entity Micro-F1**: `92.06%` (Precision: 92.20%, Recall: 91.91%)
- **Test Relation Micro-F1**: `88.40%` (Precision: 90.77%, Recall: 86.15%)
- **Test Joint Micro-F1**: `90.23%`
