# BẢN XEM TRƯỚC DỮ LIỆU CẤU TRÚC VĂN BẢN: 17_2008_QĐ-BTC_24286
- **Thể loại**: `quyet_dinh`
- **Độ dài văn bản**: 2,134 ký tự (21 đoạn văn)
- **Tổng số thực thể**: 7 (Metadata: 5, Chương: 0, Mục: 0, Điều: 2, Khoản: 0, Điểm: 0)
- **Tổng số quan hệ**: 6

---

## I. THỰC THỂ THUỘC TÍNH PHÁP LÝ (METADATA)
- **LOAI_VB** (`e_loai_vb`): `'Quyết định'` (vị trí: `[0:10]`)
- **SO_HIEU** (`e_so_hieu`): `'17/2008/QĐ-BTC'` (vị trí: `[14:28]`)
- **CO_QUAN** (`e_co_quan`): `'BỘ TÀI CHÍNH'` (vị trí: `[194:206]`)
- **NGAY** (`e_ngay_bh`): `'Ngày 17 tháng 4 năm 2008'` (vị trí: `[289:313]`)
- **NGUOI** (`e_nguoi_ky`): `'Đỗ Hoàng Anh Tuấn'` (vị trí: `[2116:2133]`)

---

## II. NỘI DUNG TOÀN BỘ CÁC CHƯƠNG, ĐIỀU, KHOẢN, ĐIỂM

### [ĐIỀU 1] Điều 1. Sửa đổi mức thuế suất thuế xuất khẩu, mức thuế suất thuế nhập khẩu ưu đãi của một số nhóm mặt hàng quy định tại Quyết định số 106/2007/QĐ-BTC ngày 20 tháng 12 năm 2007, đã được sửa đổi tại Quyết định số 13/2008/QĐ-BTC ngày 11 tháng 3 năm 2008 của Bộ trưởng Bộ Tài chính thành mức thuế suất thuế xuất khẩu, mức thuế suất thuế nhập khẩu ưu đãi mới quy định tại Danh mục 1 và Danh mục 2 ban hành kèm theo Quyết định này.
- **ID**: `e_dieu_1` | **Vị trí**: `[1449:1874]` (425 ký tự)
> **Toàn văn nội dung Điều 1**:
> ```
> Điều 1. Sửa đổi mức thuế suất thuế xuất khẩu, mức thuế suất thuế nhập khẩu ưu đãi của một số nhóm mặt hàng quy định tại Quyết định số 106/2007/QĐ-BTC ngày 20 tháng 12 năm 2007, đã được sửa đổi tại Quyết định số 13/2008/QĐ-BTC ngày 11 tháng 3 năm 2008 của Bộ trưởng Bộ Tài chính thành mức thuế suất thuế xuất khẩu, mức thuế suất thuế nhập khẩu ưu đãi mới quy định tại Danh mục 1 và Danh mục 2 ban hành kèm theo Quyết định này.
> ```

---

### [ĐIỀU 2] Điều 2. Quyết định này có hiệu lực thi hành sau 15 ngày kể từ ngày đăng Công báo và áp dụng cho các Tờ khai hải quan hàng hoá xuất khẩu, nhập khẩu đăng ký với cơ quan Hải quan kể từ ngày 22 tháng 4 năm 2008.
- **ID**: `e_dieu_2` | **Vị trí**: `[1875:2082]` (207 ký tự)
> **Toàn văn nội dung Điều 2**:
> ```
> Điều 2. Quyết định này có hiệu lực thi hành sau 15 ngày kể từ ngày đăng Công báo và áp dụng cho các Tờ khai hải quan hàng hoá xuất khẩu, nhập khẩu đăng ký với cơ quan Hải quan kể từ ngày 22 tháng 4 năm 2008.
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
