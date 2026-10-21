# BẢN XEM TRƯỚC DỮ LIỆU CẤU TRÚC VĂN BẢN: 10_2006_QĐ-BGTVT_16426
- **Thể loại**: `quyet_dinh`
- **Độ dài văn bản**: 1,580 ký tự (20 đoạn văn)
- **Tổng số thực thể**: 8 (Metadata: 5, Chương: 0, Mục: 0, Điều: 3, Khoản: 0, Điểm: 0)
- **Tổng số quan hệ**: 7

---

## I. THỰC THỂ THUỘC TÍNH PHÁP LÝ (METADATA)
- **LOAI_VB** (`e_loai_vb`): `'Quyết định'` (vị trí: `[0:10]`)
- **SO_HIEU** (`e_so_hieu`): `'10/2006/QĐ-BGTVT'` (vị trí: `[14:30]`)
- **CO_QUAN** (`e_co_quan`): `'BỘ GIAO THÔNG VẬN TẢI'` (vị trí: `[139:160]`)
- **NGAY** (`e_ngay_bh`): `'Ngày 20 tháng 2 năm 2006'` (vị trí: `[245:269]`)
- **NGUOI** (`e_nguoi_ky`): `'Nguyễn Việt Tiến'` (vị trí: `[1563:1579]`)

---

## II. NỘI DUNG TOÀN BỘ CÁC CHƯƠNG, ĐIỀU, KHOẢN, ĐIỂM

### [ĐIỀU 1] Điều 1. Ban hành kèm theo Quyết định này Tiêu chuẩn Ngành "Quy trình thí nghiệm xác định chỉ số CBR của đất, đá dăm trong phòng thí nghiệm".
- **ID**: `e_dieu_1` | **Vị trí**: `[1000:1168]` (168 ký tự)
> **Toàn văn nội dung Điều 1**:
> ```
> Điều 1. Ban hành kèm theo Quyết định này Tiêu chuẩn Ngành "Quy trình thí nghiệm xác định chỉ số CBR của đất, đá dăm trong phòng thí nghiệm".
> Số đăng ký: 22 TCN 332 - 06
> ```

---

### [ĐIỀU 2] Điều 2. Quyết định này có hiệu lực thi hành sau 15 ngày, kể từ ngày đăng Công báo.
- **ID**: `e_dieu_2` | **Vị trí**: `[1169:1251]` (82 ký tự)
> **Toàn văn nội dung Điều 2**:
> ```
> Điều 2. Quyết định này có hiệu lực thi hành sau 15 ngày, kể từ ngày đăng Công báo.
> ```

---

### [ĐIỀU 3] Điều 3. Chánh Văn phòng Bộ, Chánh Thanh tra Bộ, Vụ trưởng Vụ Khoa học - Công nghệ, Viện trưởng Viện Khoa học và công nghệ giao thông vận tải, Giám đốc Sở Giao thông vận tải, Sở Giao thông công chính và Thủ trưởng các đơn vị có liên quan chịu trách nhiệm thi hành Quyết định này./.KT. BỘ TRƯỞNG THỨ TRƯỞNG(Đã ký)Nguyễn Việt Tiến
- **ID**: `e_dieu_3` | **Vị trí**: `[1252:1579]` (327 ký tự)
> **Toàn văn nội dung Điều 3**:
> ```
> Điều 3. Chánh Văn phòng Bộ, Chánh Thanh tra Bộ, Vụ trưởng Vụ Khoa học - Công nghệ, Viện trưởng Viện Khoa học và công nghệ giao thông vận tải, Giám đốc Sở Giao thông vận tải, Sở Giao thông công chính và Thủ trưởng các đơn vị có liên quan chịu trách nhiệm thi hành Quyết định này./.KT. BỘ TRƯỞNG THỨ TRƯỞNG(Đã ký)Nguyễn Việt Tiến
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
