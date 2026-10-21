# BẢN XEM TRƯỚC DỮ LIỆU CẤU TRÚC VĂN BẢN: 03_2010_QĐ-KTNN_25853
- **Thể loại**: `quyet_dinh`
- **Độ dài văn bản**: 1,273 ký tự (21 đoạn văn)
- **Tổng số thực thể**: 8 (Metadata: 5, Chương: 0, Mục: 0, Điều: 3, Khoản: 0, Điểm: 0)
- **Tổng số quan hệ**: 7

---

## I. THỰC THỂ THUỘC TÍNH PHÁP LÝ (METADATA)
- **LOAI_VB** (`e_loai_vb`): `'Quyết định'` (vị trí: `[0:10]`)
- **SO_HIEU** (`e_so_hieu`): `'03/2010/QĐ-KTNN'` (vị trí: `[14:29]`)
- **CO_QUAN** (`e_co_quan`): `'KIỂM TOÁN NHÀ NƯỚC'` (vị trí: `[98:116]`)
- **NGAY** (`e_ngay_bh`): `'ngày 10 tháng 02 năm 2010'` (vị trí: `[208:233]`)
- **NGUOI** (`e_nguoi_ky`): `'Vương Đình Huệ'` (vị trí: `[1258:1272]`)

---

## II. NỘI DUNG TOÀN BỘ CÁC CHƯƠNG, ĐIỀU, KHOẢN, ĐIỂM

### [ĐIỀU 1] Điều 1. Ban hành kèm theo Quyết định này Quy trình kiểm toán Các tổ chức tài chính - ngân hàng.
- **ID**: `e_dieu_1` | **Vị trí**: `[917:1012]` (95 ký tự)
> **Toàn văn nội dung Điều 1**:
> ```
> Điều 1. Ban hành kèm theo Quyết định này Quy trình kiểm toán Các tổ chức tài chính - ngân hàng.
> ```

---

### [ĐIỀU 2] Điều 2. Quyết định này có hiệu lực thi hành sau 45 ngày, kể từ ngày ký.
- **ID**: `e_dieu_2` | **Vị trí**: `[1013:1084]` (71 ký tự)
> **Toàn văn nội dung Điều 2**:
> ```
> Điều 2. Quyết định này có hiệu lực thi hành sau 45 ngày, kể từ ngày ký.
> ```

---

### [ĐIỀU 3] Điều 3. Thủ trưởng các đơn vị trực thuộc Kiểm toán Nhà nước, các tổ chức và cá nhân có liên quan chịu trách nhiệm thi hành Quyết định này./.
- **ID**: `e_dieu_3` | **Vị trí**: `[1085:1272]` (187 ký tự)
> **Toàn văn nội dung Điều 3**:
> ```
> Điều 3. Thủ trưởng các đơn vị trực thuộc Kiểm toán Nhà nước, các tổ chức và cá nhân có liên quan chịu trách nhiệm thi hành Quyết định này./.
> TỔNG KIỂM TOÁN NHÀ NƯỚC
> (Đã ký)
> Vương Đình Huệ
> ```

---

## III. DANH SÁCH QUAN HỆ ĐÃ SUY DIỄN

### 1. Quan hệ Thuộc tính Pháp lý:
- `e_so_hieu` ==[ **LA_LOAI** ]==> `e_loai_vb`
- `e_so_hieu` ==[ **BAN_HANH_BOI** ]==> `e_co_quan`
- `e_so_hieu` ==[ **NGAY_BAN_HANH** ]==> `e_ngay_bh`
- `e_so_hieu` ==[ **KY_BOI** ]==> `e_nguoi_ky`

### 2. Quan hệ Phân cấp Thứ bậc (3 quan hệ THUOC):
- `e_dieu_1` ==[ **THUOC** ]==> `e_so_hieu`
- `e_dieu_2` ==[ **THUOC** ]==> `e_so_hieu`
- `e_dieu_3` ==[ **THUOC** ]==> `e_so_hieu`
