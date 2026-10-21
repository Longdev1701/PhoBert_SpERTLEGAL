"""
Schema nhãn cho bộ dữ liệu Đồ thị Tri thức Pháp luật (Legal Knowledge Graph - Joint Nested NER + RE)
huấn luyện trên kiến trúc PhoBERT-SpERT nâng cấp:
  1. Nhóm Thực thể & Quan hệ Thuộc tính / Cấu trúc văn bản (Metadata & Hierarchy)
  2. Nhóm Thực thể & Quan hệ Ngữ nghĩa Nội câu (Intra-Sentence Hub-Centered Schema, hỗ trợ Thực thể Lồng nhau - Nested Entities)
  Toàn bộ nhãn được chuẩn hóa 100% TIẾNG VIỆT (UPPERCASE_SNAKE_CASE).
"""

# ---- 1. Thực thể Thuộc tính & Cấu trúc Văn bản ----
META_ENTITY_TYPES = [
    "SO_HIEU",             # Số hiệu văn bản: 45/2019/QH14, 04/2013/NĐ-CP
    "LOAI_VAN_BAN",        # Loại văn bản: BỘ LUẬT, LUẬT, NGHỊ ĐỊNH, THÔNG TƯ, QUYẾT ĐỊNH
    "CO_QUAN_BAN_HANH",    # Cơ quan ban hành: Quốc hội, Chính phủ, Bộ Tư pháp
    "NGAY_BAN_HANH",       # Ngày ban hành của CHÍNH văn bản hiện hành: ngày 20 tháng 11 năm 2019
    "NGUOI_KY",            # Người ký: Nguyễn Thị Kim Ngân, Nguyễn Xuân Phúc
    "CHUC_DANH_NGUOI_KY",  # Chức danh người ký: Chủ tịch Quốc hội, Thủ tướng Chính phủ
]

BODY_ENTITY_TYPES = [
    "CHUONG",              # Chương của văn bản: Chương I, Chương II
    "DIEU",                # Điều của văn bản: Điều 1, Điều 15
    "KHOAN",               # Khoản của văn bản: Khoản 1, 1.
    "DIEM",                # Điểm của văn bản: Điểm a, a), (i)
]


# ---- 2. Thực thể Ngữ nghĩa Nội câu (Hỗ trợ Nested Entities: Thực thể Tâm & Thực thể Vệ tinh) ----
OUTER_HUB_ENTITY_TYPES = [
    "HANH_VI_VI_PHAM",     # Hành vi vi phạm (Hub): [giữ bản chính giấy tờ tùy thân của người lao động]
    "NGHIA_VU_QUYEN",      # Nghĩa vụ / Quyền / Thủ tục (Hub): [nộp hồ sơ kê khai thuế]
    "HINH_PHAT_CHE_TAI",   # Chế tài / Hình phạt (Hub): [Phạt tiền từ 10.000.000 đồng đến 20.000.000 đồng]
    "BIEN_PHAP_KHAC_PHUC", # Biện pháp khắc phục hậu quả (Hub): [buộc trả lại giấy tờ tùy thân]
]

INNER_SATELLITE_ENTITY_TYPES = [
    "CHU_THE_CA_NHAN",      # Chủ thể cá nhân / Vai trò: [người sử dụng lao động], [người lao động]
    "TO_CHUC_DOANH_NGHIEP", # Tổ chức / Pháp nhân / Doanh nghiệp: [doanh nghiệp], [quỹ tín dụng]
    "CO_QUAN_THAM_QUYEN",   # Cơ quan / Chức danh có thẩm quyền nội câu: [Chủ tịch UBND cấp tỉnh]
    "GIAY_TO_HO_SO",        # Giấy tờ / Hồ sơ hành chính: [bản chính giấy tờ tùy thân], [Giấy phép lái xe]
    "TAI_SAN_VAT_CHAT",     # Tài sản / Phương tiện / Tiền lương: [tiền lương], [phương tiện vi phạm]
    "MUC_TIEN",             # Mức tiền (thường lồng trong HINH_PHAT_CHE_TAI): [10.000.000 đồng]
    "NGUONG_DINH_LUONG",    # Ngưỡng số lượng / Tỷ lệ: [từ 05% đến 20%], [dưới 18 tuổi]
    "THOI_HAN",             # Thời hạn / Khoảng thời gian: [trong thời hạn 15 ngày], [từ 06 tháng đến 03 năm]
    "DIA_DIEM",             # Địa điểm / Không gian pháp lý: [trên phần đường dành cho người đi bộ]
    "THAM_CHIEU_PHAP_LY",   # Điều khoản đối chiếu / Viện dẫn: [điểm a khoản 2 Điều 4], [Luật Doanh nghiệp số 59/2020/QH14]
    "NGAY_THAM_CHIEU",      # Ngày ban hành của văn bản tham chiếu: [ngày 16 tháng 6 năm 2010] (Tách bạch với NGAY_BAN_HANH!)
    "TU_KHOA_PHAP_LY",      # Từ khóa / Động từ lập pháp dẫn chiếu: [Căn cứ], [Sửa đổi, bổ sung], [Bổ sung], [Bãi bỏ], [theo quy định tại]
    "LINH_VUC",             # Lĩnh vực pháp lý / Ngành điều chỉnh: [lĩnh vực chứng khoán và thị trường chứng khoán], [lĩnh vực bổ trợ tư pháp]
]

INTRA_SENTENCE_ENTITY_TYPES = OUTER_HUB_ENTITY_TYPES + INNER_SATELLITE_ENTITY_TYPES

ENTITY_TYPES = META_ENTITY_TYPES + BODY_ENTITY_TYPES + INTRA_SENTENCE_ENTITY_TYPES

# ---- 3. Quan hệ (head -> tail) ----
STRUCTURAL_RELATION_TYPES = [
    "BAN_HANH_BOI",            # SO_HIEU -> CO_QUAN_BAN_HANH
    "BAN_HANH_NGAY",           # SO_HIEU -> NGAY_BAN_HANH (Ngày của chính văn bản hiện hành)
    "KY_BOI",                  # SO_HIEU -> NGUOI_KY
    "LA_LOAI_VAN_BAN",         # SO_HIEU -> LOAI_VAN_BAN
    "GIU_CHUC_VU",             # NGUOI_KY -> CHUC_DANH_NGUOI_KY
    "THUOC_VE",                # DIEM -> KHOAN, KHOAN -> DIEU, DIEU -> SO_HIEU
]

# Bộ 13 nhãn quan hệ nội câu lấy Hành vi & Chế tài làm tâm + Đối chiếu điều khoản & Lĩnh vực (Hub-Centered Legal KG Schema)
INTRA_SENTENCE_RELATION_TYPES = [
    # Nhóm 1: Chủ thể - Hành vi
    "THUC_HIEN_VI_PHAM",       # CHU_THE_CA_NHAN / TO_CHUC_DOANH_NGHIEP -> HANH_VI_VI_PHAM
    "CO_NGHIA_VU_QUYEN",       # CHU_THE_CA_NHAN / TO_CHUC_DOANH_NGHIEP -> NGHIA_VU_QUYEN
    "CO_THAM_QUYEN",           # CO_QUAN_THAM_QUYEN -> HINH_PHAT_CHE_TAI / BIEN_PHAP_KHAC_PHUC / NGHIA_VU_QUYEN

    # Nhóm 2: Hành vi - Đối tượng
    "TAC_DONG_DOI_TUONG",      # HANH_VI_VI_PHAM / NGHIA_VU_QUYEN / BIEN_PHAP_KHAC_PHUC / HINH_PHAT_CHE_TAI -> GIAY_TO_HO_SO / TAI_SAN_VAT_CHAT
    "TAC_DONG_CHU_THE",        # HANH_VI_VI_PHAM / NGHIA_VU_QUYEN / BIEN_PHAP_KHAC_PHUC -> CHU_THE_CA_NHAN / TO_CHUC_DOANH_NGHIEP / CO_QUAN_THAM_QUYEN

    # Nhóm 3: Nhân quả Pháp lý - Chế tài
    "DAN_DEN_CHE_TAI",         # HANH_VI_VI_PHAM -> HINH_PHAT_CHE_TAI / BIEN_PHAP_KHAC_PHUC
    "CHIU_CHE_TAI",            # CHU_THE_CA_NHAN / TO_CHUC_DOANH_NGHIEP -> HINH_PHAT_CHE_TAI / BIEN_PHAP_KHAC_PHUC

    # Nhóm 4: Bối cảnh, Định lượng, Đối chiếu điều khoản & Lĩnh vực pháp lý
    "CO_MUC_DINH_LUONG",       # HINH_PHAT_CHE_TAI / BIEN_PHAP_KHAC_PHUC / HANH_VI_VI_PHAM / NGHIA_VU_QUYEN / TAI_SAN_VAT_CHAT -> MUC_TIEN / NGUONG_DINH_LUONG
    "TRONG_THOI_HAN",          # NGHIA_VU_QUYEN / HANH_VI_VI_PHAM / HINH_PHAT_CHE_TAI / BIEN_PHAP_KHAC_PHUC -> THOI_HAN
    "DIEN_RA_TAI",             # HANH_VI_VI_PHAM / NGHIA_VU_QUYEN / TO_CHUC_DOANH_NGHIEP / HINH_PHAT_CHE_TAI -> DIA_DIEM
    "VIEN_DAN_THAM_CHIEU",     # TU_KHOA_PHAP_LY / DIEU / KHOAN / DIEM / SO_HIEU / HANH_VI_VI_PHAM / ... -> THAM_CHIEU_PHAP_LY
    "NGAY_BAN_HANH_THAM_CHIEU",# THAM_CHIEU_PHAP_LY -> NGAY_THAM_CHIEU
    "THUOC_LINH_VUC",          # SO_HIEU / THAM_CHIEU_PHAP_LY / DIEU / KHOAN / DIEM / HANH_VI_VI_PHAM / ... -> LINH_VUC
]

RELATION_TYPES = STRUCTURAL_RELATION_TYPES + INTRA_SENTENCE_RELATION_TYPES

# Cặp (head_type, tail_type) hợp lệ cho từng quan hệ
RELATION_CONSTRAINTS = {
    # Quan hệ thuộc tính & cấu trúc
    "BAN_HANH_BOI": {("SO_HIEU", "CO_QUAN_BAN_HANH")},
    "BAN_HANH_NGAY": {("SO_HIEU", "NGAY_BAN_HANH")},
    "KY_BOI": {("SO_HIEU", "NGUOI_KY")},
    "LA_LOAI_VAN_BAN": {("SO_HIEU", "LOAI_VAN_BAN")},
    "GIU_CHUC_VU": {("NGUOI_KY", "CHUC_DANH_NGUOI_KY")},
    "THUOC_VE": {
        ("DIEM", "KHOAN"),
        ("KHOAN", "DIEU"),
        ("DIEU", "CHUONG"),
        ("DIEU", "SO_HIEU"),
        ("CHUONG", "SO_HIEU"),
    },

    # Nhóm 1: Chủ thể - Hành vi
    "THUC_HIEN_VI_PHAM": {
        ("CHU_THE_CA_NHAN", "HANH_VI_VI_PHAM"),
        ("TO_CHUC_DOANH_NGHIEP", "HANH_VI_VI_PHAM"),
    },
    "CO_NGHIA_VU_QUYEN": {
        ("CHU_THE_CA_NHAN", "NGHIA_VU_QUYEN"),
        ("TO_CHUC_DOANH_NGHIEP", "NGHIA_VU_QUYEN"),
    },
    "CO_THAM_QUYEN": {
        ("CO_QUAN_THAM_QUYEN", "HINH_PHAT_CHE_TAI"),
        ("CO_QUAN_THAM_QUYEN", "BIEN_PHAP_KHAC_PHUC"),
        ("CO_QUAN_THAM_QUYEN", "NGHIA_VU_QUYEN"),
    },

    # Nhóm 2: Hành vi - Đối tượng
    "TAC_DONG_DOI_TUONG": {
        ("HANH_VI_VI_PHAM", "GIAY_TO_HO_SO"),
        ("HANH_VI_VI_PHAM", "TAI_SAN_VAT_CHAT"),
        ("NGHIA_VU_QUYEN", "GIAY_TO_HO_SO"),
        ("NGHIA_VU_QUYEN", "TAI_SAN_VAT_CHAT"),
        ("BIEN_PHAP_KHAC_PHUC", "GIAY_TO_HO_SO"),
        ("BIEN_PHAP_KHAC_PHUC", "TAI_SAN_VAT_CHAT"),
        ("HINH_PHAT_CHE_TAI", "GIAY_TO_HO_SO"),
        ("HINH_PHAT_CHE_TAI", "TAI_SAN_VAT_CHAT"),
    },
    "TAC_DONG_CHU_THE": {
        ("HANH_VI_VI_PHAM", "CHU_THE_CA_NHAN"),
        ("HANH_VI_VI_PHAM", "TO_CHUC_DOANH_NGHIEP"),
        ("HANH_VI_VI_PHAM", "CO_QUAN_THAM_QUYEN"),
        ("NGHIA_VU_QUYEN", "CHU_THE_CA_NHAN"),
        ("NGHIA_VU_QUYEN", "TO_CHUC_DOANH_NGHIEP"),
        ("NGHIA_VU_QUYEN", "CO_QUAN_THAM_QUYEN"),
        ("BIEN_PHAP_KHAC_PHUC", "CHU_THE_CA_NHAN"),
        ("BIEN_PHAP_KHAC_PHUC", "TO_CHUC_DOANH_NGHIEP"),
        ("BIEN_PHAP_KHAC_PHUC", "CO_QUAN_THAM_QUYEN"),
    },

    # Nhóm 3: Nhân quả Pháp lý - Chế tài
    "DAN_DEN_CHE_TAI": {
        ("HANH_VI_VI_PHAM", "HINH_PHAT_CHE_TAI"),
        ("HANH_VI_VI_PHAM", "BIEN_PHAP_KHAC_PHUC"),
    },
    "CHIU_CHE_TAI": {
        ("CHU_THE_CA_NHAN", "HINH_PHAT_CHE_TAI"),
        ("CHU_THE_CA_NHAN", "BIEN_PHAP_KHAC_PHUC"),
        ("TO_CHUC_DOANH_NGHIEP", "HINH_PHAT_CHE_TAI"),
        ("TO_CHUC_DOANH_NGHIEP", "BIEN_PHAP_KHAC_PHUC"),
    },

    # Nhóm 4: Bối cảnh, Định lượng, Đối chiếu điều khoản & Lĩnh vực
    "CO_MUC_DINH_LUONG": {
        ("HINH_PHAT_CHE_TAI", "MUC_TIEN"),
        ("HINH_PHAT_CHE_TAI", "NGUONG_DINH_LUONG"),
        ("HANH_VI_VI_PHAM", "MUC_TIEN"),
        ("HANH_VI_VI_PHAM", "NGUONG_DINH_LUONG"),
        ("NGHIA_VU_QUYEN", "MUC_TIEN"),
        ("NGHIA_VU_QUYEN", "NGUONG_DINH_LUONG"),
        ("BIEN_PHAP_KHAC_PHUC", "MUC_TIEN"),
        ("BIEN_PHAP_KHAC_PHUC", "NGUONG_DINH_LUONG"),
        ("TAI_SAN_VAT_CHAT", "MUC_TIEN"),
        ("TAI_SAN_VAT_CHAT", "NGUONG_DINH_LUONG"),
    },
    "TRONG_THOI_HAN": {
        ("NGHIA_VU_QUYEN", "THOI_HAN"),
        ("HANH_VI_VI_PHAM", "THOI_HAN"),
        ("HINH_PHAT_CHE_TAI", "THOI_HAN"),
        ("BIEN_PHAP_KHAC_PHUC", "THOI_HAN"),
    },
    "DIEN_RA_TAI": {
        ("HANH_VI_VI_PHAM", "DIA_DIEM"),
        ("NGHIA_VU_QUYEN", "DIA_DIEM"),
        ("TO_CHUC_DOANH_NGHIEP", "DIA_DIEM"),
        ("HINH_PHAT_CHE_TAI", "DIA_DIEM"),
    },
    "VIEN_DAN_THAM_CHIEU": {
        ("TU_KHOA_PHAP_LY", "THAM_CHIEU_PHAP_LY"),
        ("HANH_VI_VI_PHAM", "THAM_CHIEU_PHAP_LY"),
        ("NGHIA_VU_QUYEN", "THAM_CHIEU_PHAP_LY"),
        ("HINH_PHAT_CHE_TAI", "THAM_CHIEU_PHAP_LY"),
        ("BIEN_PHAP_KHAC_PHUC", "THAM_CHIEU_PHAP_LY"),
        ("CHUONG", "THAM_CHIEU_PHAP_LY"),
        ("DIEU", "THAM_CHIEU_PHAP_LY"),
        ("KHOAN", "THAM_CHIEU_PHAP_LY"),
        ("DIEM", "THAM_CHIEU_PHAP_LY"),
        ("SO_HIEU", "THAM_CHIEU_PHAP_LY"),
        ("LOAI_VAN_BAN", "THAM_CHIEU_PHAP_LY"),
        ("CO_QUAN_THAM_QUYEN", "THAM_CHIEU_PHAP_LY"),
        ("TO_CHUC_DOANH_NGHIEP", "THAM_CHIEU_PHAP_LY"),
        ("CHU_THE_CA_NHAN", "THAM_CHIEU_PHAP_LY"),
        ("GIAY_TO_HO_SO", "THAM_CHIEU_PHAP_LY"),
    },
    "NGAY_BAN_HANH_THAM_CHIEU": {
        ("THAM_CHIEU_PHAP_LY", "NGAY_THAM_CHIEU"),
    },
    "THUOC_LINH_VUC": {
        ("SO_HIEU", "LINH_VUC"),
        ("LOAI_VAN_BAN", "LINH_VUC"),
        ("THAM_CHIEU_PHAP_LY", "LINH_VUC"),
        ("CHUONG", "LINH_VUC"),
        ("DIEU", "LINH_VUC"),
        ("KHOAN", "LINH_VUC"),
        ("DIEM", "LINH_VUC"),
        ("HANH_VI_VI_PHAM", "LINH_VUC"),
        ("NGHIA_VU_QUYEN", "LINH_VUC"),
        ("HINH_PHAT_CHE_TAI", "LINH_VUC"),
        ("BIEN_PHAP_KHAC_PHUC", "LINH_VUC"),
        ("CO_QUAN_THAM_QUYEN", "LINH_VUC"),
        ("TO_CHUC_DOANH_NGHIEP", "LINH_VUC"),
        ("CHU_THE_CA_NHAN", "LINH_VUC"),
        ("GIAY_TO_HO_SO", "LINH_VUC"),
    },
}

# Nhóm văn bản được chọn
SELECTED_CATEGORIES = ["nghi_dinh", "thong_tu", "quyet_dinh", "bo_luat"]
MIN_YEAR = 2006
