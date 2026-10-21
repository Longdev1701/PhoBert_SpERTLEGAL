# BẢN XEM TRƯỚC DỮ LIỆU CẤU TRÚC VĂN BẢN: 1371_2006_QĐ-CTN_14154
- **Thể loại**: `quyet_dinh`
- **Độ dài văn bản**: 1,705 ký tự (18 đoạn văn)
- **Tổng số thực thể**: 7 (Metadata: 5, Chương: 0, Mục: 0, Điều: 2, Khoản: 0, Điểm: 0)
- **Tổng số quan hệ**: 6

---

## I. THỰC THỂ THUỘC TÍNH PHÁP LÝ (METADATA)
- **LOAI_VB** (`e_loai_vb`): `'Quyết định'` (vị trí: `[0:10]`)
- **SO_HIEU** (`e_so_hieu`): `'1371/2006/QĐ-CTN'` (vị trí: `[14:30]`)
- **CO_QUAN** (`e_co_quan`): `'CHỦ TỊCH NƯỚC'` (vị trí: `[67:80]`)
- **NGAY** (`e_ngay_bh`): `'ngày 18 tháng 12 năm 2006'` (vị trí: `[173:198]`)
- **NGUOI** (`e_nguoi_ky`): `'Nguyễn Minh Triết'` (vị trí: `[1687:1704]`)

---

## II. NỘI DUNG TOÀN BỘ CÁC CHƯƠNG, ĐIỀU, KHOẢN, ĐIỂM

### [ĐIỀU 1] Điều 1. Cho thôi quốc tịch Việt Nam đối với: 102 công dân hiện đang cư trú tại Hàn Quốc; 245 công dân hiện đang cư trú tại Cộng hoà liên bang Đức; 270 công dân hiện đang cư trú tại Cộng hoà dân chủ nhân dân Lào; 24 công dân hiện đang cư trú tại Cộng hoà Ba Lan; 13 công dân hiện đang cư trú tại Cộng hoà Séc; 29 công dân hiện đang cư trú tại Cộng hoà Áo; 1 công dân hiện đang cư trú tại Canada; 1 công dân hiện đang cư trú tại Thái Lan; 16 công dân hiện đang cư trú tại Singapore; 4 công dân hiện đang cư trú tại Hoa Kỳ; 1 công dân hiện đang cư trú tại Slovakia; 12 công dân hiện đang cư trú tại Hà Lan; 17 công dân hiện đang cư trú tại Vương quốc Đan Mạch; 3 công dân hiện đang cư trú tại Nhật Bản; 24 công dân hiện đang cư trú tại Hồng Kông (có tên trong danh sách kèm theo).
- **ID**: `e_dieu_1` | **Vị trí**: `[638:1415]` (777 ký tự)
> **Toàn văn nội dung Điều 1**:
> ```
> Điều 1. Cho thôi quốc tịch Việt Nam đối với: 102 công dân hiện đang cư trú tại Hàn Quốc; 245 công dân hiện đang cư trú tại Cộng hoà liên bang Đức; 270 công dân hiện đang cư trú tại Cộng hoà dân chủ nhân dân Lào; 24 công dân hiện đang cư trú tại Cộng hoà Ba Lan; 13 công dân hiện đang cư trú tại Cộng hoà Séc; 29 công dân hiện đang cư trú tại Cộng hoà Áo; 1 công dân hiện đang cư trú tại Canada; 1 công dân hiện đang cư trú tại Thái Lan; 16 công dân hiện đang cư trú tại Singapore; 4 công dân hiện đang cư trú tại Hoa Kỳ; 1 công dân hiện đang cư trú tại Slovakia; 12 công dân hiện đang cư trú tại Hà Lan; 17 công dân hiện đang cư trú tại Vương quốc Đan Mạch; 3 công dân hiện đang cư trú tại Nhật Bản; 24 công dân hiện đang cư trú tại Hồng Kông (có tên trong danh sách kèm theo).
> ```

---

### [ĐIỀU 2] Điều 2. Quyết định có hiệu lực kể từ ngày ký.
- **ID**: `e_dieu_2` | **Vị trí**: `[1416:1461]` (45 ký tự)
> **Toàn văn nội dung Điều 2**:
> ```
> Điều 2. Quyết định có hiệu lực kể từ ngày ký.
> ```

---

## III. DANH SÁCH QUAN HỆ ĐÃ SUY DIỄN

### 1. Quan hệ Thuộc tính Pháp lý:
- `e_so_hieu` ==[ **LA_LOAI** ]==> `e_loai_vb`
- `e_so_hieu` ==[ **BAN_HANH_BOI** ]==> `e_co_quan`
- `e_so_hieu` ==[ **NGAY_BAN_HANH** ]==> `e_ngay_bh`
- `e_so_hieu` ==[ **KY_BOI** ]==> `e_nguoi_ky`

### 2. Quan hệ Phân cấp Thứ bậc (2 quan hệ THUOC):
- `e_dieu_1` ==[ **THUOC** ]==> `e_so_hieu`
- `e_dieu_2` ==[ **THUOC** ]==> `e_so_hieu`
