# BẢN XEM TRƯỚC DỮ LIỆU CẤU TRÚC VĂN BẢN: 16_2006_QĐ-BKHCN_15269
- **Thể loại**: `quyet_dinh`
- **Độ dài văn bản**: 1,641 ký tự (19 đoạn văn)
- **Tổng số thực thể**: 8 (Metadata: 5, Chương: 0, Mục: 0, Điều: 3, Khoản: 0, Điểm: 0)
- **Tổng số quan hệ**: 7

---

## I. THỰC THỂ THUỘC TÍNH PHÁP LÝ (METADATA)
- **LOAI_VB** (`e_loai_vb`): `'Quyết định'` (vị trí: `[0:10]`)
- **SO_HIEU** (`e_so_hieu`): `'16/2006/QĐ-BKHCN'` (vị trí: `[14:30]`)
- **CO_QUAN** (`e_co_quan`): `'BỘ KHOA HỌC VÀ CÔNG NGHỆ'` (vị trí: `[190:214]`)
- **NGAY** (`e_ngay_bh`): `'ngày 23 tháng 8 năm 2006'` (vị trí: `[307:331]`)
- **NGUOI** (`e_nguoi_ky`): `'Bùi Mạnh Hải'` (vị trí: `[1628:1640]`)

---

## II. NỘI DUNG TOÀN BỘ CÁC CHƯƠNG, ĐIỀU, KHOẢN, ĐIỂM

### [ĐIỀU 1] Điều 1. Ban hành kèm theo Quyết định này "Quy định về việc tổ chức thực hiện các nhiệm vụ thuộc Đề án triển khai thực hiện Hiệp định hàng rào kỹ thuật trong thương mại giai đoạn 2006 - 2010".
- **ID**: `e_dieu_1` | **Vị trí**: `[1093:1284]` (191 ký tự)
> **Toàn văn nội dung Điều 1**:
> ```
> Điều 1. Ban hành kèm theo Quyết định này "Quy định về việc tổ chức thực hiện các nhiệm vụ thuộc Đề án triển khai thực hiện Hiệp định hàng rào kỹ thuật trong thương mại giai đoạn 2006 - 2010".
> ```

---

### [ĐIỀU 2] Điều 2. Quyết định này có hiệu lực sau 15 ngày, kể từ ngày đăng Công báo.
- **ID**: `e_dieu_2` | **Vị trí**: `[1285:1358]` (73 ký tự)
> **Toàn văn nội dung Điều 2**:
> ```
> Điều 2. Quyết định này có hiệu lực sau 15 ngày, kể từ ngày đăng Công báo.
> ```

---

### [ĐIỀU 3] Điều 3. Chánh Văn phòng, Vụ trưởng Vụ Kế hoạch - Tài chính, Tổng cục trưởng Tổng cục Tiêu chuẩn Đo lường Chất lượng, Thủ trưởng các đơn vị thuộc Bộ và các cơ quan, tổ chức, cá nhân có liên quan chịu trách nhiệm thi hành Quyết định này.
- **ID**: `e_dieu_3` | **Vị trí**: `[1359:1594]` (235 ký tự)
> **Toàn văn nội dung Điều 3**:
> ```
> Điều 3. Chánh Văn phòng, Vụ trưởng Vụ Kế hoạch - Tài chính, Tổng cục trưởng Tổng cục Tiêu chuẩn Đo lường Chất lượng, Thủ trưởng các đơn vị thuộc Bộ và các cơ quan, tổ chức, cá nhân có liên quan chịu trách nhiệm thi hành Quyết định này.
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
