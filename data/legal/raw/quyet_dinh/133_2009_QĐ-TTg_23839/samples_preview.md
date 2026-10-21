# BẢN XEM TRƯỚC DỮ LIỆU CẤU TRÚC VĂN BẢN: 133_2009_QĐ-TTg_23839
- **Thể loại**: `quyet_dinh`
- **Độ dài văn bản**: 1,606 ký tự (20 đoạn văn)
- **Tổng số thực thể**: 7 (Metadata: 4, Chương: 0, Mục: 0, Điều: 3, Khoản: 0, Điểm: 0)
- **Tổng số quan hệ**: 6

---

## I. THỰC THỂ THUỘC TÍNH PHÁP LÝ (METADATA)
- **LOAI_VB** (`e_loai_vb`): `'Quyết định'` (vị trí: `[0:10]`)
- **SO_HIEU** (`e_so_hieu`): `'133/2009/QĐ-TTg'` (vị trí: `[14:29]`)
- **CO_QUAN** (`e_co_quan`): `'THỦ TƯỚNG CHÍNH PHỦ'` (vị trí: `[94:113]`)
- **NGAY** (`e_ngay_bh`): `'ngày 03 tháng 11 năm 2009'` (vị trí: `[205:230]`)

---

## II. NỘI DUNG TOÀN BỘ CÁC CHƯƠNG, ĐIỀU, KHOẢN, ĐIỂM

### [ĐIỀU 1] Điều 1. Ban hành kèm theo Quyết định này Quy chế thông tin cảnh báo, dự báo thiên tai trên biển.
- **ID**: `e_dieu_1` | **Vị trí**: `[968:1064]` (96 ký tự)
> **Toàn văn nội dung Điều 1**:
> ```
> Điều 1. Ban hành kèm theo Quyết định này Quy chế thông tin cảnh báo, dự báo thiên tai trên biển.
> ```

---

### [ĐIỀU 2] Điều 2. Quyết định này có hiệu lực thi hành kể từ ngày 20 tháng 12 năm 2009.
- **ID**: `e_dieu_2` | **Vị trí**: `[1065:1141]` (76 ký tự)
> **Toàn văn nội dung Điều 2**:
> ```
> Điều 2. Quyết định này có hiệu lực thi hành kể từ ngày 20 tháng 12 năm 2009.
> ```

---

### [ĐIỀU 3] Điều 3. Bộ trưởng Bộ Tài nguyên và Môi trường chịu trách nhiệm chủ trì hướng dẫn, tổ chức, chỉ đạo và kiểm tra việc thực hiện Quyết định này.
- **ID**: `e_dieu_3` | **Vị trí**: `[1142:1570]` (428 ký tự)
> **Toàn văn nội dung Điều 3**:
> ```
> Điều 3. Bộ trưởng Bộ Tài nguyên và Môi trường chịu trách nhiệm chủ trì hướng dẫn, tổ chức, chỉ đạo và kiểm tra việc thực hiện Quyết định này.
> Các Bộ trưởng, Thủ trưởng cơ quan ngang Bộ, Thủ trưởng cơ quan thuộc Chính phủ, Trưởng ban Ban Chỉ đạo phòng, chống lụt, bão Trung ương, Chủ tịch Ủy ban quốc gia Tìm kiếm Cứu nạn, Chủ tịch Ủy ban nhân dân tỉnh, thành phố trực thuộc Trung ương chịu trách nhiệm thi hành Quyết định này./.
> ```

---

## III. DANH SÁCH QUAN HỆ ĐÃ SUY DIỄN

### 1. Quan hệ Thuộc tính Pháp lý:
- `e_so_hieu` ==[ **LA_LOAI** ]==> `e_loai_vb`
- `e_so_hieu` ==[ **BAN_HANH_BOI** ]==> `e_co_quan`
- `e_so_hieu` ==[ **NGAY_BAN_HANH** ]==> `e_ngay_bh`

### 2. Quan hệ Phân cấp Thứ bậc (3 quan hệ THUOC):
- `e_dieu_1` ==[ **THUOC** ]==> `e_so_hieu`
- `e_dieu_2` ==[ **THUOC** ]==> `e_so_hieu`
- `e_dieu_3` ==[ **THUOC** ]==> `e_so_hieu`
