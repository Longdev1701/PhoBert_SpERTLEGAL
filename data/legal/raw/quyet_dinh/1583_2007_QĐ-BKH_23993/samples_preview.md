# BẢN XEM TRƯỚC DỮ LIỆU CẤU TRÚC VĂN BẢN: 1583_2007_QĐ-BKH_23993
- **Thể loại**: `quyet_dinh`
- **Độ dài văn bản**: 977 ký tự (12 đoạn văn)
- **Tổng số thực thể**: 7 (Metadata: 4, Chương: 0, Mục: 0, Điều: 3, Khoản: 0, Điểm: 0)
- **Tổng số quan hệ**: 6

---

## I. THỰC THỂ THUỘC TÍNH PHÁP LÝ (METADATA)
- **LOAI_VB** (`e_loai_vb`): `'Quyết định'` (vị trí: `[0:10]`)
- **SO_HIEU** (`e_so_hieu`): `'1583/2007/QĐ-BKH'` (vị trí: `[14:30]`)
- **CO_QUAN** (`e_co_quan`): `'BỘ KẾ HOẠCH VÀ ĐẦU TƯ'` (vị trí: `[138:159]`)
- **NGAY** (`e_ngay_bh`): `'ngày 29 tháng 11 năm 2005'` (vị trí: `[197:222]`)

---

## II. NỘI DUNG TOÀN BỘ CÁC CHƯƠNG, ĐIỀU, KHOẢN, ĐIỂM

### [ĐIỀU 1] Điều 1. Ban hành kèm theo Quyết định này "Mẫu hồ sơ mời thầu dịch vụ tư vấn".
- **ID**: `e_dieu_1` | **Vị trí**: `[630:707]` (77 ký tự)
> **Toàn văn nội dung Điều 1**:
> ```
> Điều 1. Ban hành kèm theo Quyết định này "Mẫu hồ sơ mời thầu dịch vụ tư vấn".
> ```

---

### [ĐIỀU 2] Điều 2. Quyết định này có hiệu lực thi hành sau 15 ngày kể từ ngày đăng Công báo.
- **ID**: `e_dieu_2` | **Vị trí**: `[708:789]` (81 ký tự)
> **Toàn văn nội dung Điều 2**:
> ```
> Điều 2. Quyết định này có hiệu lực thi hành sau 15 ngày kể từ ngày đăng Công báo.
> ```

---

### [ĐIỀU 3] Điều 3. Các Bộ, cơ quan ngang Bộ, cơ quan thuộc Chính phủ, cơ quan khác ở Trung ương, Ủy ban nhân dân các cấp và tổ chức, cá nhân có liên quan chịu trách nhiệm thi hành Quyết định này./.
- **ID**: `e_dieu_3` | **Vị trí**: `[790:976]` (186 ký tự)
> **Toàn văn nội dung Điều 3**:
> ```
> Điều 3. Các Bộ, cơ quan ngang Bộ, cơ quan thuộc Chính phủ, cơ quan khác ở Trung ương, Ủy ban nhân dân các cấp và tổ chức, cá nhân có liên quan chịu trách nhiệm thi hành Quyết định này./.
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
