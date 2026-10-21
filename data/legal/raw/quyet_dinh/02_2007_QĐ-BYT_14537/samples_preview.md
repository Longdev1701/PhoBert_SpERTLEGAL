# BẢN XEM TRƯỚC DỮ LIỆU CẤU TRÚC VĂN BẢN: 02_2007_QĐ-BYT_14537
- **Thể loại**: `quyet_dinh`
- **Độ dài văn bản**: 1,784 ký tự (14 đoạn văn)
- **Tổng số thực thể**: 7 (Metadata: 4, Chương: 0, Mục: 0, Điều: 3, Khoản: 0, Điểm: 0)
- **Tổng số quan hệ**: 6

---

## I. THỰC THỂ THUỘC TÍNH PHÁP LÝ (METADATA)
- **LOAI_VB** (`e_loai_vb`): `'Quyết định'` (vị trí: `[0:10]`)
- **SO_HIEU** (`e_so_hieu`): `'02/2007/QĐ-BYT'` (vị trí: `[14:28]`)
- **CO_QUAN** (`e_co_quan`): `'BỘ Y TẾ'` (vị trí: `[184:191]`)
- **NGAY** (`e_ngay_bh`): `'ngày 15 tháng 5 năm 2003'` (vị trí: `[226:250]`)

---

## II. NỘI DUNG TOÀN BỘ CÁC CHƯƠNG, ĐIỀU, KHOẢN, ĐIỂM

### [ĐIỀU 1] Điều 1. Ban hành kèm theo Quyết định này “Quy định vệ sinh an toàn đối với sản phẩm thuốc lá”
- **ID**: `e_dieu_1` | **Vị trí**: `[1167:1260]` (93 ký tự)
> **Toàn văn nội dung Điều 1**:
> ```
> Điều 1. Ban hành kèm theo Quyết định này “Quy định vệ sinh an toàn đối với sản phẩm thuốc lá”
> ```

---

### [ĐIỀU 2] Điều 2. Quyết định này có hiệu lực sau 15 ngày kể từ ngày đăng Công báo.Bãi bỏ Quyết định số 2019/2000/QĐ-BYT ngày 30/6/2000 của Bộ trưởng Bộ Y tế về “Quy định tạm thời về vệ sinh thuốc lá điếu”.
- **ID**: `e_dieu_2` | **Vị trí**: `[1261:1456]` (195 ký tự)
> **Toàn văn nội dung Điều 2**:
> ```
> Điều 2. Quyết định này có hiệu lực sau 15 ngày kể từ ngày đăng Công báo.Bãi bỏ Quyết định số 2019/2000/QĐ-BYT ngày 30/6/2000 của Bộ trưởng Bộ Y tế về “Quy định tạm thời về vệ sinh thuốc lá điếu”.
> ```

---

### [ĐIỀU 3] Điều 3. Các ông, bà: Chánh Văn phòng, Chánh Thanh tra Bộ Y tế, Vụ trưởng các Vụ: Pháp chế, Khoa học và Đào tạo; Cục trưởng Cục An toàn vệ sinh thực phẩm, Giám đốc Sở Y tế tỉnh, thành phố trực thuộc Trung ương, Thủ trưởng các đơn vị liên quan thuộc Bộ Y tế, Thủ trưởng Y tế các ngành chịu trách nhiệm thi hành Quyết định này./.
- **ID**: `e_dieu_3` | **Vị trí**: `[1457:1783]` (326 ký tự)
> **Toàn văn nội dung Điều 3**:
> ```
> Điều 3. Các ông, bà: Chánh Văn phòng, Chánh Thanh tra Bộ Y tế, Vụ trưởng các Vụ: Pháp chế, Khoa học và Đào tạo; Cục trưởng Cục An toàn vệ sinh thực phẩm, Giám đốc Sở Y tế tỉnh, thành phố trực thuộc Trung ương, Thủ trưởng các đơn vị liên quan thuộc Bộ Y tế, Thủ trưởng Y tế các ngành chịu trách nhiệm thi hành Quyết định này./.
> ```

---

## III. DANH SÁCH QUAN HỆ ĐÃ SUY DIỄN

### 1. Quan hệ Thuộc tính Pháp lý:
- `e_so_hieu` ==[ **LA_LOAI** ]==> `e_loai_vb`
- `e_so_hieu` ==[ **BAN_HANH_BOI** ]==> `e_co_quan`
- `e_so_hieu` ==[ **NGAY_BAN_HANH** ]==> `e_ngay_bh`

### 2. Quan hệ Phân cấp Thứ bậc (3 quan hệ THUOC):
- `e_dieu_1` ==[ **THUOC** ]==> `e_so_hieu`
- `e_dieu_2` ==[ **THUOC** ]==> `e_so_hieu`
- `e_dieu_3` ==[ **THUOC** ]==> `e_so_hieu`
