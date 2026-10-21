# BẢN XEM TRƯỚC DỮ LIỆU CẤU TRÚC VĂN BẢN: 03_2007_QĐ-BTC_14250
- **Thể loại**: `quyet_dinh`
- **Độ dài văn bản**: 1,934 ký tự (22 đoạn văn)
- **Tổng số thực thể**: 8 (Metadata: 5, Chương: 0, Mục: 0, Điều: 3, Khoản: 0, Điểm: 0)
- **Tổng số quan hệ**: 7

---

## I. THỰC THỂ THUỘC TÍNH PHÁP LÝ (METADATA)
- **LOAI_VB** (`e_loai_vb`): `'Quyết định'` (vị trí: `[0:10]`)
- **SO_HIEU** (`e_so_hieu`): `'03/2007/QĐ-BTC'` (vị trí: `[14:28]`)
- **CO_QUAN** (`e_co_quan`): `'BỘ TÀI CHÍNH'` (vị trí: `[134:146]`)
- **NGAY** (`e_ngay_bh`): `'ngày 08 tháng 01 năm 2007'` (vị trí: `[237:262]`)
- **NGUOI** (`e_nguoi_ky`): `'Đỗ Hoàng Anh Tuấn'` (vị trí: `[1916:1933]`)

---

## II. NỘI DUNG TOÀN BỘ CÁC CHƯƠNG, ĐIỀU, KHOẢN, ĐIỂM

### [ĐIỀU 1] Điều 1. Ban hành kèm theo Quyết định này định mức hao hụt thóc bảo quản dự trữ quốc gia do Cục Dự trữ quốc gia trực tiếp quản lý (có phụ lục kèm theo).
- **ID**: `e_dieu_1` | **Vị trí**: `[901:1377]` (476 ký tự)
> **Toàn văn nội dung Điều 1**:
> ```
> Điều 1. Ban hành kèm theo Quyết định này định mức hao hụt thóc bảo quản dự trữ quốc gia do Cục Dự trữ quốc gia trực tiếp quản lý (có phụ lục kèm theo).
> Các định mức trên căn cứ theo tiêu chuẩn chất lượng thóc nhập kho dự trữ quốc gia tại tiêu chuẩn ngành TCN 04-2004: Thóc dự trữ quốc gia - Yêu cầu kỹ thuật ban hành theo Quyết định số 35/2004/QĐ-BTC ngày 14/4/2004 và quy phạm bảo quản thóc ban hành tại Quyết định số 34/2004/QĐ-BTC ngày 14/4/2004 của Bộ trưởng Bộ Tài chính.
> ```

---

### [ĐIỀU 2] Điều 2. Quyết định này có hiệu lực thi hành sau 15 ngày kể từ ngày đăng công báo và thay thế phần nội dung quy định về định mức hao hụt thóc tại Điều 1 Quyết định số 91/2004/QĐ-BTC ngày 29/11/2004 của Bộ trưởng Bộ Tài chính về việc ban hành định mức bảo quản hàng hóa dự trữ quốc gia.
- **ID**: `e_dieu_2` | **Vị trí**: `[1378:1662]` (284 ký tự)
> **Toàn văn nội dung Điều 2**:
> ```
> Điều 2. Quyết định này có hiệu lực thi hành sau 15 ngày kể từ ngày đăng công báo và thay thế phần nội dung quy định về định mức hao hụt thóc tại Điều 1 Quyết định số 91/2004/QĐ-BTC ngày 29/11/2004 của Bộ trưởng Bộ Tài chính về việc ban hành định mức bảo quản hàng hóa dự trữ quốc gia.
> ```

---

### [ĐIỀU 3] Điều 3. Cục trưởng Cục Dự trữ quốc gia, Chánh Văn phòng Bộ và Thủ trưởng các đơn vị thuộc Bộ Tài chính trong phạm vi chức năng, quyền hạn của mình có trách nhiệm tổ chức thực hiện và kiểm tra thi hành quyết định này ./.
- **ID**: `e_dieu_3` | **Vị trí**: `[1663:1882]` (219 ký tự)
> **Toàn văn nội dung Điều 3**:
> ```
> Điều 3. Cục trưởng Cục Dự trữ quốc gia, Chánh Văn phòng Bộ và Thủ trưởng các đơn vị thuộc Bộ Tài chính trong phạm vi chức năng, quyền hạn của mình có trách nhiệm tổ chức thực hiện và kiểm tra thi hành quyết định này ./.
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
