# BẢN XEM TRƯỚC DỮ LIỆU CẤU TRÚC VĂN BẢN: 09_2024_TT-BXD_169706
- **Thể loại**: `thong_tu`
- **Độ dài văn bản**: 2,635 ký tự (40 đoạn văn)
- **Tổng số thực thể**: 8 (Metadata: 5, Chương: 0, Mục: 0, Điều: 3, Khoản: 0, Điểm: 0)
- **Tổng số quan hệ**: 7

---

## I. THỰC THỂ THUỘC TÍNH PHÁP LÝ (METADATA)
- **LOAI_VB** (`e_loai_vb`): `'Thông tư'` (vị trí: `[0:8]`)
- **SO_HIEU** (`e_so_hieu`): `'09/2024/TT-BXD'` (vị trí: `[12:26]`)
- **NGAY** (`e_ngay_bh`): `'ngày 31 tháng 8 năm 2021'` (vị trí: `[109:133]`)
- **CO_QUAN** (`e_co_quan`): `'Bộ Xây dựng'` (vị trí: `[148:159]`)
- **NGUOI** (`e_nguoi_ky`): `'Bùi Xuân Dũng'` (vị trí: `[2621:2634]`)

---

## II. NỘI DUNG TOÀN BỘ CÁC CHƯƠNG, ĐIỀU, KHOẢN, ĐIỂM

### [ĐIỀU 1] Điều 1. Sửa đổi, bổ sung một số định mức xây dựng gồm: Định mức dự toán xây dựng công trình, Định mức dự toán lắp đặt máy và thiết bị công nghệ, Định mức dự toán sửa chữa và bảo dưỡng công trình xây dựng, Định mức sử dụng vật liệu xây dựng, Định mức chi phí quản lý dự án và tư vấn đầu tư xây dựng đã ban hành tại Thông tư số 12/2021/TT-BXD ngày 31 tháng 8 năm 2021 của Bộ trưởng Bộ Xây dựng. Chi tiết cụ thể tại các Phụ lục kèm theo Thông tư này.
- **ID**: `e_dieu_1` | **Vị trí**: `[1206:1653]` (447 ký tự)
> **Toàn văn nội dung Điều 1**:
> ```
> Điều 1. Sửa đổi, bổ sung một số định mức xây dựng gồm: Định mức dự toán xây dựng công trình, Định mức dự toán lắp đặt máy và thiết bị công nghệ, Định mức dự toán sửa chữa và bảo dưỡng công trình xây dựng, Định mức sử dụng vật liệu xây dựng, Định mức chi phí quản lý dự án và tư vấn đầu tư xây dựng đã ban hành tại Thông tư số 12/2021/TT-BXD ngày 31 tháng 8 năm 2021 của Bộ trưởng Bộ Xây dựng. Chi tiết cụ thể tại các Phụ lục kèm theo Thông tư này.
> ```

---

### [ĐIỀU 2] Điều 2. Quy định chuyển tiếp
- **ID**: `e_dieu_2` | **Vị trí**: `[1654:1909]` (255 ký tự)
> **Toàn văn nội dung Điều 2**:
> ```
> Điều 2. Quy định chuyển tiếp
> Việc chuyển tiếp áp dụng định mức xây dựng sửa đổi, bổ sung ban hành tại Thông tư này thực hiện theo quy định tại khoản 8 Điều 44 của Nghị định số 10/2021/NĐ-CP ngày 09/02/2021 của Chính phủ về quản lý chi phí đầu tư xây dựng.
> ```

---

### [ĐIỀU 3] Điều 3. Điều khoản thi hành
- **ID**: `e_dieu_3` | **Vị trí**: `[1910:2006]` (96 ký tự)
> **Toàn văn nội dung Điều 3**:
> ```
> Điều 3. Điều khoản thi hành
> Thông tư này có hiệu lực thi hành kể từ ngày 15 tháng 10 năm 2024./.
> ```

---

## III. DANH SÁCH QUAN HỆ ĐÃ SUY DIỄN

### 1. Quan hệ Thuộc tính Pháp lý:
- `e_so_hieu` ==[ **LA_LOAI** ]==> `e_loai_vb`
- `e_so_hieu` ==[ **NGAY_BAN_HANH** ]==> `e_ngay_bh`
- `e_so_hieu` ==[ **BAN_HANH_BOI** ]==> `e_co_quan`
- `e_so_hieu` ==[ **KY_BOI** ]==> `e_nguoi_ky`

### 2. Quan hệ Phân cấp Thứ bậc (3 quan hệ THUOC):
- `e_dieu_1` ==[ **THUOC** ]==> `e_so_hieu`
- `e_dieu_2` ==[ **THUOC** ]==> `e_so_hieu`
- `e_dieu_3` ==[ **THUOC** ]==> `e_so_hieu`
