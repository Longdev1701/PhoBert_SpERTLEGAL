# BẢN XEM TRƯỚC DỮ LIỆU CẤU TRÚC VĂN BẢN: 73_2025_NĐ-CP_177755
- **Thể loại**: `nghi_dinh`
- **Độ dài văn bản**: 2,972 ký tự (25 đoạn văn)
- **Tổng số thực thể**: 8 (Metadata: 4, Chương: 0, Mục: 0, Điều: 2, Khoản: 2, Điểm: 0)
- **Tổng số quan hệ**: 7

---

## I. THỰC THỂ THUỘC TÍNH PHÁP LÝ (METADATA)
- **LOAI_VB** (`e_loai_vb`): `'Nghị định'` (vị trí: `[0:9]`)
- **SO_HIEU** (`e_so_hieu`): `'73/2025/NĐ-CP'` (vị trí: `[13:26]`)
- **NGAY** (`e_ngay_bh`): `'ngày 31 tháng 5 năm 2023'` (vị trí: `[209:233]`)
- **CO_QUAN** (`e_co_quan`): `'Chính phủ'` (vị trí: `[238:247]`)

---

## II. NỘI DUNG TOÀN BỘ CÁC CHƯƠNG, ĐIỀU, KHOẢN, ĐIỂM

### [ĐIỀU 1] Điều 1. Sửa đổi, bổ sung mức thuế suất thuế nhập khẩu ưu đãi của một số mặt hàng quy định tại Phụ lục II - Biểu thuế nhập khẩu ưu đãi theo Danh mục mặt hàng chịu thuế quy định tại Điều 3 Nghị định số 26/2023/NĐ-CP
- **ID**: `e_dieu_1` | **Vị trí**: `[2043:2605]` (562 ký tự)
> **Toàn văn nội dung Điều 1**:
> ```
> Điều 1. Sửa đổi, bổ sung mức thuế suất thuế nhập khẩu ưu đãi của một số mặt hàng quy định tại Phụ lục II - Biểu thuế nhập khẩu ưu đãi theo Danh mục mặt hàng chịu thuế quy định tại Điều 3 Nghị định số 26/2023/NĐ-CP
> Sửa đổi, bổ sung mức thuế suất thuế nhập khẩu ưu đãi của một số mặt hàng quy định tại Phụ lục II - Biểu thuế nhập khẩu ưu đãi theo Danh mục mặt hàng chịu thuế quy định tại Điều 3 Nghị định số 26/2023/NĐ-CP ngày 31 tháng 5 năm 2023 của Chính phủ thành các mức thuế suất thuế nhập khẩu ưu đãi mới quy định tại Phụ lục ban hành kèm theo Nghị định này.
> ```

---

### [ĐIỀU 2] Điều 2. Hiệu lực thi hành
- **ID**: `e_dieu_2` | **Vị trí**: `[2606:2971]` (365 ký tự)
> **Toàn văn nội dung Điều 2**:
> ```
> Điều 2. Hiệu lực thi hành
> 1. Nghị định này có hiệu lực thi hành kể từ ngày ký ban hành.
> 2. Các Bộ trưởng, Thủ trưởng cơ quan ngang bộ, Thủ trưởng cơ quan thuộc Chính phủ, Chủ tịch Ủy ban nhân dân tỉnh, thành phố trực thuộc Trung ương và các tổ chức, cá nhân có liên quan chịu trách nhiệm thi hành Nghị định này./.TM. CHÍNH PHỦ KT. THỦ TƯỚNG PHÓ THỦ TƯỚNGHồ Đức Phớc
> ```

**Các Khoản trong Điều 2** (2 khoản):
- **Khoản 1** (`e_khoan_2_1`, `[2632:2693]`):
  > '1. Nghị định này có hiệu lực thi hành kể từ ngày ký ban hành.'...
- **Khoản 2** (`e_khoan_2_2`, `[2694:2971]`):
  > '2. Các Bộ trưởng, Thủ trưởng cơ quan ngang bộ, Thủ trưởng cơ quan thuộc Chính phủ, Chủ tịch Ủy ban nhân dân tỉnh, thành phố trực thuộc Trung'...

---

## III. DANH SÁCH QUAN HỆ ĐÃ SUY DIỄN

### 1. Quan hệ Thuộc tính Pháp lý:
- `e_so_hieu` ==[ **LA_LOAI** ]==> `e_loai_vb`
- `e_so_hieu` ==[ **NGAY_BAN_HANH** ]==> `e_ngay_bh`
- `e_so_hieu` ==[ **BAN_HANH_BOI** ]==> `e_co_quan`

### 2. Quan hệ Phân cấp Thứ bậc (4 quan hệ THUOC):
- `e_dieu_1` ==[ **THUOC** ]==> `e_so_hieu`
- `e_dieu_2` ==[ **THUOC** ]==> `e_so_hieu`
- `e_khoan_2_1` ==[ **THUOC** ]==> `e_dieu_2`
- `e_khoan_2_2` ==[ **THUOC** ]==> `e_dieu_2`
