# BẢN XEM TRƯỚC DỮ LIỆU CẤU TRÚC VĂN BẢN: 173_2008_QĐ-TTg_12572
- **Thể loại**: `quyet_dinh`
- **Độ dài văn bản**: 1,621 ký tự (21 đoạn văn)
- **Tổng số thực thể**: 8 (Metadata: 5, Chương: 0, Mục: 0, Điều: 3, Khoản: 0, Điểm: 0)
- **Tổng số quan hệ**: 7

---

## I. THỰC THỂ THUỘC TÍNH PHÁP LÝ (METADATA)
- **LOAI_VB** (`e_loai_vb`): `'Quyết định'` (vị trí: `[0:10]`)
- **SO_HIEU** (`e_so_hieu`): `'173/2008/QĐ-TTg'` (vị trí: `[14:29]`)
- **CO_QUAN** (`e_co_quan`): `'THỦ TƯỚNG CHÍNH PHỦ'` (vị trí: `[141:160]`)
- **NGAY** (`e_ngay_bh`): `'ngày 25 tháng 12 năm 2008'` (vị trí: `[252:277]`)
- **NGUOI** (`e_nguoi_ky`): `'Nguyễn Thiện Nhân'` (vị trí: `[1603:1620]`)

---

## II. NỘI DUNG TOÀN BỘ CÁC CHƯƠNG, ĐIỀU, KHOẢN, ĐIỂM

### [ĐIỀU 1] Điều 1. Ban hành kèm theo Quyết định này "Quy định áp dụng các biện pháp cần thiết đáp ứng yêu cầu về thuốc kháng HIV trong trường hợp khẩn cấp".
- **ID**: `e_dieu_1` | **Vị trí**: `[1089:1234]` (145 ký tự)
> **Toàn văn nội dung Điều 1**:
> ```
> Điều 1. Ban hành kèm theo Quyết định này "Quy định áp dụng các biện pháp cần thiết đáp ứng yêu cầu về thuốc kháng HIV trong trường hợp khẩn cấp".
> ```

---

### [ĐIỀU 2] Điều 2. Quyết định này có hiệu lực thi hành sau 15 ngày, kể từ ngày đăng Công báo.
- **ID**: `e_dieu_2` | **Vị trí**: `[1235:1317]` (82 ký tự)
> **Toàn văn nội dung Điều 2**:
> ```
> Điều 2. Quyết định này có hiệu lực thi hành sau 15 ngày, kể từ ngày đăng Công báo.
> ```

---

### [ĐIỀU 3] Điều 3. Bộ trưởng Bộ Y tế chịu trách nhiệm hướng dẫn, thi hành Quyết định này.
- **ID**: `e_dieu_3` | **Vị trí**: `[1318:1620]` (302 ký tự)
> **Toàn văn nội dung Điều 3**:
> ```
> Điều 3. Bộ trưởng Bộ Y tế chịu trách nhiệm hướng dẫn, thi hành Quyết định này.
> Các Bộ trưởng, Thủ trưởng cơ quan ngang Bộ, Thủ trưởng cơ quan thuộc Chính phủ, Chủ tịch Ủy ban nhân dân tỉnh, thành phố trực thuộc Trung ương chịu trách nhiệm thi hành Quyết định này./.PHÓ THỦ TƯỚNG(Đã ký)Nguyễn Thiện Nhân
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
