# BẢN XEM TRƯỚC DỮ LIỆU CẤU TRÚC VĂN BẢN: 07_2025_QĐ-KTNN_175504
- **Thể loại**: `quyet_dinh`
- **Độ dài văn bản**: 2,127 ký tự (19 đoạn văn)
- **Tổng số thực thể**: 7 (Metadata: 5, Chương: 0, Mục: 0, Điều: 2, Khoản: 0, Điểm: 0)
- **Tổng số quan hệ**: 6

---

## I. THỰC THỂ THUỘC TÍNH PHÁP LÝ (METADATA)
- **LOAI_VB** (`e_loai_vb`): `'Quyết định'` (vị trí: `[0:10]`)
- **SO_HIEU** (`e_so_hieu`): `'07/2025/QĐ-KTNN'` (vị trí: `[14:29]`)
- **CO_QUAN** (`e_co_quan`): `'Kiểm toán nhà nước'` (vị trí: `[77:95]`)
- **NGAY** (`e_ngay_bh`): `'ngày 25 tháng 2 năm 2025'` (vị trí: `[206:230]`)
- **NGUOI** (`e_nguoi_ky`): `'Ngô Văn Tuấn'` (vị trí: `[2114:2126]`)

---

## II. NỘI DUNG TOÀN BỘ CÁC CHƯƠNG, ĐIỀU, KHOẢN, ĐIỂM

### [ĐIỀU 1] Điều 1. Bãi bỏ một văn bản quy phạm pháp luật của Tổng Kiểm toán nhà nước
- **ID**: `e_dieu_1` | **Vị trí**: `[1659:1879]` (220 ký tự)
> **Toàn văn nội dung Điều 1**:
> ```
> Điều 1. Bãi bỏ một văn bản quy phạm pháp luật của Tổng Kiểm toán nhà nước
> Bãi bỏ toàn bộ Quyết định số 04/2010/QĐ-KTNN ngày 02 tháng 6 năm 2010 của Tổng Kiểm toán nhà nước ban hành Quy chế kiểm soát chất lượng kiểm toán.
> ```

---

### [ĐIỀU 2] Điều 2. Điều khoản thi hành
- **ID**: `e_dieu_2` | **Vị trí**: `[1880:2126]` (246 ký tự)
> **Toàn văn nội dung Điều 2**:
> ```
> Điều 2. Điều khoản thi hành
> Quyết định này có hiệu lực thi hành kể từ ngày ký. Thủ trưởng các đơn vị trực thuộc Kiểm toán nhà nước và các tổ chức, cá nhân có liên quan chịu trách nhiệm thi hành Quyết định này.
> TỔNG KIỂM TOÁN NHÀ NƯỚC
> Ngô Văn Tuấn
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
