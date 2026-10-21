# BẢN XEM TRƯỚC DỮ LIỆU CẤU TRÚC VĂN BẢN: 121_2009_TT-BTC_11892
- **Thể loại**: `thong_tu`
- **Độ dài văn bản**: 2,150 ký tự (21 đoạn văn)
- **Tổng số thực thể**: 7 (Metadata: 5, Chương: 0, Mục: 0, Điều: 2, Khoản: 0, Điểm: 0)
- **Tổng số quan hệ**: 6

---

## I. THỰC THỂ THUỘC TÍNH PHÁP LÝ (METADATA)
- **LOAI_VB** (`e_loai_vb`): `'Thông tư'` (vị trí: `[0:8]`)
- **SO_HIEU** (`e_so_hieu`): `'121/2009/TT-BTC'` (vị trí: `[12:27]`)
- **CO_QUAN** (`e_co_quan`): `'BỘ TÀI CHÍNH'` (vị trí: `[183:195]`)
- **NGAY** (`e_ngay_bh`): `'ngày 17 tháng 6 năm 2009'` (vị trí: `[287:311]`)
- **NGUOI** (`e_nguoi_ky`): `'Đỗ Hoàng Anh Tuấn'` (vị trí: `[2132:2149]`)

---

## II. NỘI DUNG TOÀN BỘ CÁC CHƯƠNG, ĐIỀU, KHOẢN, ĐIỂM

### [ĐIỀU 1] Điều 1. Thuế suất mặt hàng quặng Apatit
- **ID**: `e_dieu_1` | **Vị trí**: `[1441:1929]` (488 ký tự)
> **Toàn văn nội dung Điều 1**:
> ```
> Điều 1. Thuế suất mặt hàng quặng Apatit
> Điều chỉnh giảm mức thuế suất thuế xuất khẩu của mặt hàng quặng Apatit thuộc nhóm 2510 quy định tại Danh mục sửa đổi Biểu thuế xuất khẩu ban hành kèm theo Quyết định số 123/2008/QĐ-BTC ngày 26/12/2008 của Bộ trưởng Bộ Tài chính về việc điều chỉnh mức thuế suất thuế xuất khẩu, mức thuế suất thuế nhập khẩu ưu đãi đối với một số nhóm hàng trong Biểu thuế xuất khẩu, Biểu thuế nhập khẩu ưu đãi từ mức 10% thành mức thuế suất thuế xuất khẩu mới là 7%.
> ```

---

### [ĐIỀU 2] Điều 2. Hiệu lực thi hành.
- **ID**: `e_dieu_2` | **Vị trí**: `[1930:2098]` (168 ký tự)
> **Toàn văn nội dung Điều 2**:
> ```
> Điều 2. Hiệu lực thi hành.
> Thông tư này có hiệu lực và áp dụng đối với các Tờ khai hải quan hàng hóa xuất khẩu đăng ký với cơ quan Hải quan sau 45 ngày kể từ ngày ký./.
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
