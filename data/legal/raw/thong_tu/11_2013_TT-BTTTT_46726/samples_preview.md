# BẢN XEM TRƯỚC DỮ LIỆU CẤU TRÚC VĂN BẢN: 11_2013_TT-BTTTT_46726
- **Thể loại**: `thong_tu`
- **Độ dài văn bản**: 1,589 ký tự (21 đoạn văn)
- **Tổng số thực thể**: 8 (Metadata: 5, Chương: 0, Mục: 0, Điều: 3, Khoản: 0, Điểm: 0)
- **Tổng số quan hệ**: 7

---

## I. THỰC THỂ THUỘC TÍNH PHÁP LÝ (METADATA)
- **LOAI_VB** (`e_loai_vb`): `'Thông tư'` (vị trí: `[0:8]`)
- **SO_HIEU** (`e_so_hieu`): `'11/2013/TT-BTTTT'` (vị trí: `[12:28]`)
- **CO_QUAN** (`e_co_quan`): `'BỘ THÔNG TIN VÀ TRUYỀN THÔNG'` (vị trí: `[113:141]`)
- **NGAY** (`e_ngay_bh`): `'Ngày 13 tháng 5 năm 2013'` (vị trí: `[226:250]`)
- **NGUOI** (`e_nguoi_ky`): `'Nguyễn Bắc Son'` (vị trí: `[1574:1588]`)

---

## II. NỘI DUNG TOÀN BỘ CÁC CHƯƠNG, ĐIỀU, KHOẢN, ĐIỂM

### [ĐIỀU 1] Điều 1. Ban hành kèm theo Thông tư này Danh mục dịch vụ viễn thông thực hiện báo cáo giá thành thực tế, giá thành kế hoạch.
- **ID**: `e_dieu_1` | **Vị trí**: `[1134:1257]` (123 ký tự)
> **Toàn văn nội dung Điều 1**:
> ```
> Điều 1. Ban hành kèm theo Thông tư này Danh mục dịch vụ viễn thông thực hiện báo cáo giá thành thực tế, giá thành kế hoạch.
> ```

---

### [ĐIỀU 2] Điều 2. Thông tư này có hiệu lực thi hành kể từ ngày 13 tháng 5 năm 2013.
- **ID**: `e_dieu_2` | **Vị trí**: `[1258:1331]` (73 ký tự)
> **Toàn văn nội dung Điều 2**:
> ```
> Điều 2. Thông tư này có hiệu lực thi hành kể từ ngày 13 tháng 5 năm 2013.
> ```

---

### [ĐIỀU 3] Điều 3. Chánh Văn phòng, Thủ trưởng các cơ quan, đơn vị thuộc Bộ, Cục trưởng Cục Viễn thông, Tổng giám đốc, Giám đốc các doanh nghiệp viễn thông
- **ID**: `e_dieu_3` | **Vị trí**: `[1332:1555]` (223 ký tự)
> **Toàn văn nội dung Điều 3**:
> ```
> Điều 3. Chánh Văn phòng, Thủ trưởng các cơ quan, đơn vị thuộc Bộ, Cục trưởng Cục Viễn thông, Tổng giám đốc, Giám đốc các doanh nghiệp viễn thông
> và các tổ chức, cá nhân có liên quan chịu trách nhiệm thi hành Thông tư này./.
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
