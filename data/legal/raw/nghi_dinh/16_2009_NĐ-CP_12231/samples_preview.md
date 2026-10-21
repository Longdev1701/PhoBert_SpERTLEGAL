# BẢN XEM TRƯỚC DỮ LIỆU CẤU TRÚC VĂN BẢN: 16_2009_NĐ-CP_12231
- **Thể loại**: `nghi_dinh`
- **Độ dài văn bản**: 1,947 ký tự (24 đoạn văn)
- **Tổng số thực thể**: 10 (Metadata: 5, Chương: 0, Mục: 0, Điều: 3, Khoản: 2, Điểm: 0)
- **Tổng số quan hệ**: 9

---

## I. THỰC THỂ THUỘC TÍNH PHÁP LÝ (METADATA)
- **LOAI_VB** (`e_loai_vb`): `'Nghị định'` (vị trí: `[0:9]`)
- **SO_HIEU** (`e_so_hieu`): `'16/2009/NĐ-CP'` (vị trí: `[13:26]`)
- **NGAY** (`e_ngay_bh`): `'ngày 04 tháng 02 năm 2008'` (vị trí: `[86:111]`)
- **CO_QUAN** (`e_co_quan`): `'Chính phủ'` (vị trí: `[116:125]`)
- **NGUOI** (`e_nguoi_ky`): `'Nguyễn Tấn Dũng'` (vị trí: `[1931:1946]`)

---

## II. NỘI DUNG TOÀN BỘ CÁC CHƯƠNG, ĐIỀU, KHOẢN, ĐIỂM

### [ĐIỀU 1] Điều 1. Sửa đổi, bổ sung khoản 2 Điều 8 Nghị định số 13/2008/NĐ-CP ngày 04 tháng 02 năm 2008 của Chính phủ quy định tổ chức các cơ quan chuyên môn thuộc Ủy ban nhân dân tỉnh, thành phố trực thuộc Trung ương như sau:
- **ID**: `e_dieu_1` | **Vị trí**: `[750:1490]` (740 ký tự)
> **Toàn văn nội dung Điều 1**:
> ```
> Điều 1. Sửa đổi, bổ sung khoản 2 Điều 8 Nghị định số 13/2008/NĐ-CP ngày 04 tháng 02 năm 2008 của Chính phủ quy định tổ chức các cơ quan chuyên môn thuộc Ủy ban nhân dân tỉnh, thành phố trực thuộc Trung ương như sau:
> "2. Sở Tư pháp:
> Tham mưu, giúp Ủy ban nhân dân cấp tỉnh thực hiện chức năng quản lý nhà nước về: công tác xây dựng và thi hành văn bản quy phạm pháp luật; kiểm tra, xử lý văn bản quy phạm pháp luật; phổ biến, giáo dục pháp luật; thi hành án dân sự; công chứng; chứng thực; nuôi con nuôi có yếu tố nước ngoài; trọng tài thương mại; hộ tịch; quốc tịch; lý lịch tư pháp; luật sư; tư vấn pháp luật; trợ giúp pháp lý; giám định tư pháp; hòa giải ở cơ sở; bán đấu giá tài sản và công tác tư pháp khác theo quy định của pháp luật".
> ```

---

### [ĐIỀU 2] Điều 2. Hiệu lực thi hành
- **ID**: `e_dieu_2` | **Vị trí**: `[1491:1643]` (152 ký tự)
> **Toàn văn nội dung Điều 2**:
> ```
> Điều 2. Hiệu lực thi hành
> 1. Nghị định này có hiệu lực thi hành kể từ ngày 02 tháng 4 năm 2009.
> 2. Bãi bỏ các quy định trước đây trái với Nghị định này.
> ```

**Các Khoản trong Điều 2** (2 khoản):
- **Khoản 1** (`e_khoan_2_1`, `[1517:1586]`):
  > '1. Nghị định này có hiệu lực thi hành kể từ ngày 02 tháng 4 năm 2009.'...
- **Khoản 2** (`e_khoan_2_2`, `[1587:1643]`):
  > '2. Bãi bỏ các quy định trước đây trái với Nghị định này.'...

---

### [ĐIỀU 3] Điều 3. Trách nhiệm thi hành
- **ID**: `e_dieu_3` | **Vị trí**: `[1644:1888]` (244 ký tự)
> **Toàn văn nội dung Điều 3**:
> ```
> Điều 3. Trách nhiệm thi hành
> Các Bộ trưởng, Thủ trưởng cơ quan ngang Bộ, Thủ trưởng cơ quan thuộc Chính phủ, Chủ tịch Hội đồng nhân dân và Chủ tịch Ủy ban nhân dân tỉnh, thành phố trực thuộc Trung ương chịu trách nhiệm thi hành Nghị định này./.
> ```

---

## III. DANH SÁCH QUAN HỆ ĐÃ SUY DIỄN

### 1. Quan hệ Thuộc tính Pháp lý:
- `e_so_hieu` ==[ **LA_LOAI** ]==> `e_loai_vb`
- `e_so_hieu` ==[ **NGAY_BAN_HANH** ]==> `e_ngay_bh`
- `e_so_hieu` ==[ **BAN_HANH_BOI** ]==> `e_co_quan`
- `e_so_hieu` ==[ **KY_BOI** ]==> `e_nguoi_ky`

### 2. Quan hệ Phân cấp Thứ bậc (5 quan hệ THUOC):
- `e_dieu_1` ==[ **THUOC** ]==> `e_so_hieu`
- `e_dieu_2` ==[ **THUOC** ]==> `e_so_hieu`
- `e_khoan_2_1` ==[ **THUOC** ]==> `e_dieu_2`
- `e_khoan_2_2` ==[ **THUOC** ]==> `e_dieu_2`
- `e_dieu_3` ==[ **THUOC** ]==> `e_so_hieu`
