# BẢN XEM TRƯỚC DỮ LIỆU CẤU TRÚC VĂN BẢN: 07_2018_TT-BCT_128982
- **Thể loại**: `thong_tu`
- **Độ dài văn bản**: 1,811 ký tự (21 đoạn văn)
- **Tổng số thực thể**: 7 (Metadata: 5, Chương: 0, Mục: 0, Điều: 2, Khoản: 0, Điểm: 0)
- **Tổng số quan hệ**: 6

---

## I. THỰC THỂ THUỘC TÍNH PHÁP LÝ (METADATA)
- **LOAI_VB** (`e_loai_vb`): `'Thông tư'` (vị trí: `[0:8]`)
- **SO_HIEU** (`e_so_hieu`): `'07/2018/TT-BCT'` (vị trí: `[12:26]`)
- **NGAY** (`e_ngay_bh`): `'ngày 23 tháng 10 năm 2017'` (vị trí: `[62:87]`)
- **CO_QUAN** (`e_co_quan`): `'Bộ Công Thương'` (vị trí: `[102:116]`)
- **NGUOI** (`e_nguoi_ky`): `'Trần Tuấn Anh'` (vị trí: `[1797:1810]`)

---

## II. NỘI DUNG TOÀN BỘ CÁC CHƯƠNG, ĐIỀU, KHOẢN, ĐIỂM

### [ĐIỀU 1] Điều 1. Điều 2 Thông tư số 21/2017/TT-BCT được sửa đổi như sau: "Thông tư này có hiệu lực thi hành kể từ ngày 01 tháng 01 năm 2019".
- **ID**: `e_dieu_1` | **Vị trí**: `[1569:1701]` (132 ký tự)
> **Toàn văn nội dung Điều 1**:
> ```
> Điều 1. Điều 2 Thông tư số 21/2017/TT-BCT được sửa đổi như sau: "Thông tư này có hiệu lực thi hành kể từ ngày 01 tháng 01 năm 2019".
> ```

---

### [ĐIỀU 2] Điều 2. Hiệu lực thi hành
- **ID**: `e_dieu_2` | **Vị trí**: `[1702:1778]` (76 ký tự)
> **Toàn văn nội dung Điều 2**:
> ```
> Điều 2. Hiệu lực thi hành
> Thông tư này có hiệu lực thi hành kể từ ngày ký./.
> ```

---

## III. DANH SÁCH QUAN HỆ ĐÃ SUY DIỄN

### 1. Quan hệ Thuộc tính Pháp lý:
- `e_so_hieu` ==[ **LA_LOAI** ]==> `e_loai_vb`
- `e_so_hieu` ==[ **NGAY_BAN_HANH** ]==> `e_ngay_bh`
- `e_so_hieu` ==[ **BAN_HANH_BOI** ]==> `e_co_quan`
- `e_so_hieu` ==[ **KY_BOI** ]==> `e_nguoi_ky`

### 2. Quan hệ Phân cấp Thứ bậc (2 quan hệ THUOC):
- `e_dieu_1` ==[ **THUOC** ]==> `e_so_hieu`
- `e_dieu_2` ==[ **THUOC** ]==> `e_so_hieu`
