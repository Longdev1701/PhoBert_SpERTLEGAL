# BẢN XEM TRƯỚC DỮ LIỆU CẤU TRÚC VĂN BẢN: 17_2006_QĐ-BCN_15916
- **Thể loại**: `quyet_dinh`
- **Độ dài văn bản**: 1,308 ký tự (18 đoạn văn)
- **Tổng số thực thể**: 8 (Metadata: 5, Chương: 0, Mục: 0, Điều: 3, Khoản: 0, Điểm: 0)
- **Tổng số quan hệ**: 7

---

## I. THỰC THỂ THUỘC TÍNH PHÁP LÝ (METADATA)
- **LOAI_VB** (`e_loai_vb`): `'Quyết định'` (vị trí: `[0:10]`)
- **SO_HIEU** (`e_so_hieu`): `'17/2006/QĐ-BCN'` (vị trí: `[14:28]`)
- **CO_QUAN** (`e_co_quan`): `'BỘ CÔNG NGHIỆP'` (vị trí: `[110:124]`)
- **NGAY** (`e_ngay_bh`): `'ngày 8 tháng 6 năm 2006'` (vị trí: `[214:237]`)
- **NGUOI** (`e_nguoi_ky`): `'Đỗ Hữu Hào'` (vị trí: `[1297:1307]`)

---

## II. NỘI DUNG TOÀN BỘ CÁC CHƯƠNG, ĐIỀU, KHOẢN, ĐIỂM

### [ĐIỀU 1] Điều 1. Ban hành kèm theo Quyết định này Quy chế Tổ chức và Hoạt động của Trường Cao đẳng Công nghiệp Việt - Đức.
- **ID**: `e_dieu_1` | **Vị trí**: `[874:987]` (113 ký tự)
> **Toàn văn nội dung Điều 1**:
> ```
> Điều 1. Ban hành kèm theo Quyết định này Quy chế Tổ chức và Hoạt động của Trường Cao đẳng Công nghiệp Việt - Đức.
> ```

---

### [ĐIỀU 2] Điều 2. Quyết định này có hiệu lực sau 15 ngày, kể từ ngày đăng Công báo.
- **ID**: `e_dieu_2` | **Vị trí**: `[988:1061]` (73 ký tự)
> **Toàn văn nội dung Điều 2**:
> ```
> Điều 2. Quyết định này có hiệu lực sau 15 ngày, kể từ ngày đăng Công báo.
> ```

---

### [ĐIỀU 3] Điều 3. Chánh Văn phòng Bộ, Chánh Thanh tra Bộ, Vụ trưởng, Cục trưởng, Thủ trưởng cơ quan, đơn vị thuộc Bộ và Hiệu trưởng Trường Cao đẳng Công nghiệp Việt - Đức chịu trách nhiệm thi hành Quyết định này./.KT. BỘ TRƯỞNG THỨ TRƯỞNG(Đã ký)Đỗ Hữu Hào
- **ID**: `e_dieu_3` | **Vị trí**: `[1062:1307]` (245 ký tự)
> **Toàn văn nội dung Điều 3**:
> ```
> Điều 3. Chánh Văn phòng Bộ, Chánh Thanh tra Bộ, Vụ trưởng, Cục trưởng, Thủ trưởng cơ quan, đơn vị thuộc Bộ và Hiệu trưởng Trường Cao đẳng Công nghiệp Việt - Đức chịu trách nhiệm thi hành Quyết định này./.KT. BỘ TRƯỞNG THỨ TRƯỞNG(Đã ký)Đỗ Hữu Hào
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
