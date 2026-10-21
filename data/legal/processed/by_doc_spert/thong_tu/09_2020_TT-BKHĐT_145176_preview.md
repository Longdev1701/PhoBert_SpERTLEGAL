# Dữ liệu gán nhãn văn bản: 09_2020_TT-BKHĐT_145176
- **Thể loại**: `thong_tu`
- **Phân vùng dữ liệu**: `TRAIN`
- **Tổng số mẫu**: 82 mẫu
- **Tổng số thực thể**: 473
- **Tổng số quan hệ**: 277

---

### Mẫu #09_2020_TT-BKHĐT_145176#header_0 (Loại: `header`)
> **[BỘ KẾ HOẠCH VÀ ĐẦU TƯ]`<CO_QUAN_BAN_HANH>`** . Số : **[09/2020/TT-BKHĐT]`<SO_HIEU>`** . CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM Độc lập – Tự do – Hạnh phúc . Hà Nội , **[ngày 27 tháng 11 năm 2020]`<NGAY_BAN_HANH>`** . **[THÔNG TƯ]`<LOAI_VAN_BAN>`**

**Thực thể:**
- `[e0]` **09/2020/TT-BKHĐT** → `SO_HIEU` (span: `[7:8]`)
- `[e1]` **ngày 27 tháng 11 năm 2020** → `NGAY_BAN_HANH` (span: `[23:29]`)
- `[e2]` **BỘ KẾ HOẠCH VÀ ĐẦU TƯ** → `CO_QUAN_BAN_HANH` (span: `[0:4]`)
- `[e3]` **THÔNG TƯ** → `LOAI_VAN_BAN` (span: `[30:31]`)

**Quan hệ:**
- (`e0` 09/2020/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` BỘ KẾ HOẠCH VÀ ĐẦU TƯ `[CO_QUAN_BAN_HANH]`)
- (`e0` 09/2020/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e1` ngày 27 tháng 11 năm 2020 `[NGAY_BAN_HANH]`)
- (`e0` 09/2020/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e3` THÔNG TƯ `[LOAI_VAN_BAN]`)


---

### Mẫu #09_2020_TT-BKHĐT_145176#signature_1 (Loại: `signature`)
> **[BỘ TRƯỞNG]`<CHUC_DANH_NGUOI_KY>`** . ( Đã ký ) . **[Nguyễn Chí Dũng]`<NGUOI_KY>`**

**Thực thể:**
- `[e0]` **Nguyễn Chí Dũng** → `NGUOI_KY` (span: `[7:8]`)
- `[e1]` **BỘ TRƯỞNG** → `CHUC_DANH_NGUOI_KY` (span: `[0:1]`)

**Quan hệ:**
- (`e0` Nguyễn Chí Dũng `[NGUOI_KY]`) ==[ **GIU_CHUC_VU** ]==> (`e1` BỘ TRƯỞNG `[CHUC_DANH_NGUOI_KY]`)


---

### Mẫu #09_2020_TT-BKHĐT_145176#meta_2 (Loại: `meta`)
> **[BỘ KẾ HOẠCH VÀ ĐẦU TƯ]`<CO_QUAN_BAN_HANH>`** . Số : **[09/2020/TT-BKHĐT]`<SO_HIEU>`** . CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM Độc lập – Tự do – Hạnh phúc . Hà Nội , ngày 27 tháng 11 năm 2020 . **[THÔNG TƯ]`<LOAI_VAN_BAN>`** . **[BỘ TRƯỞNG]`<CHUC_DANH_NGUOI_KY>`** . ( Đã ký ) . **[Nguyễn Chí Dũng]`<NGUOI_KY>`**

**Thực thể:**
- `[e0]` **09/2020/TT-BKHĐT** → `SO_HIEU` (span: `[7:8]`)
- `[e1]` **BỘ KẾ HOẠCH VÀ ĐẦU TƯ** → `CO_QUAN_BAN_HANH` (span: `[0:4]`)
- `[e2]` **THÔNG TƯ** → `LOAI_VAN_BAN` (span: `[30:31]`)
- `[e3]` **Nguyễn Chí Dũng** → `NGUOI_KY` (span: `[39:40]`)
- `[e4]` **BỘ TRƯỞNG** → `CHUC_DANH_NGUOI_KY` (span: `[32:33]`)

**Quan hệ:**
- (`e0` 09/2020/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e1` BỘ KẾ HOẠCH VÀ ĐẦU TƯ `[CO_QUAN_BAN_HANH]`)
- (`e0` 09/2020/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e2` THÔNG TƯ `[LOAI_VAN_BAN]`)
- (`e0` 09/2020/TT-BKHĐT `[SO_HIEU]`) ==[ **KY_BOI** ]==> (`e3` Nguyễn Chí Dũng `[NGUOI_KY]`)
- (`e3` Nguyễn Chí Dũng `[NGUOI_KY]`) ==[ **GIU_CHUC_VU** ]==> (`e4` BỘ TRƯỞNG `[CHUC_DANH_NGUOI_KY]`)


---

### Mẫu #09_2020_TT-BKHĐT_145176#preamble_context_3 (Loại: `preamble_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[09/2020/TT-BKHĐT]`<SO_HIEU>`** của **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** . Quy định chi tiết lập **[hồ sơ mời thầu mua sắm hàng hoá]`<GIAY_TO_HO_SO>`** đối với gói thầu thuộc phạm vi điều chỉnh của Hiệp định Đối tác Toàn diện và Tiến bộ xuyên Thái Bình Dương

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **09/2020/TT-BKHĐT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[4:8]`)
- `[e3]` **hồ sơ mời thầu mua sắm hàng hoá** → `GIAY_TO_HO_SO` (span: `[12:16]`)

**Quan hệ:**
- (`e1` 09/2020/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 09/2020/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)


---

### Mẫu #09_2020_TT-BKHĐT_145176#preamble_standalone_4 (Loại: `preamble_standalone`)
> Quy định chi tiết lập **[hồ sơ mời thầu mua sắm hàng hoá]`<GIAY_TO_HO_SO>`** đối với gói thầu thuộc phạm vi điều chỉnh của Hiệp định Đối tác Toàn diện và Tiến bộ xuyên Thái Bình Dương

**Thực thể:**
- `[e0]` **hồ sơ mời thầu mua sắm hàng hoá** → `GIAY_TO_HO_SO` (span: `[3:7]`)


---

### Mẫu #09_2020_TT-BKHĐT_145176#preamble_context_5 (Loại: `preamble_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[09/2020/TT-BKHĐT]`<SO_HIEU>`** của **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** . **[Căn cứ]`<TU_KHOA_PHAP_LY>`** **[Luật Đấu thầu]`<THAM_CHIEU_PHAP_LY>`** **[ngày 26 tháng 11 năm 2013]`<NGAY_THAM_CHIEU>`** ;

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **09/2020/TT-BKHĐT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[4:8]`)
- `[e3]` **Luật Đấu thầu** → `THAM_CHIEU_PHAP_LY` (span: `[10:11]`)
- `[e4]` **Căn cứ** → `TU_KHOA_PHAP_LY` (span: `[9:10]`)
- `[e5]` **ngày 26 tháng 11 năm 2013** → `NGAY_THAM_CHIEU` (span: `[11:17]`)

**Quan hệ:**
- (`e1` 09/2020/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 09/2020/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e4` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Luật Đấu thầu `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 09/2020/TT-BKHĐT `[SO_HIEU]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Luật Đấu thầu `[THAM_CHIEU_PHAP_LY]`)
- (`e3` Luật Đấu thầu `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e5` ngày 26 tháng 11 năm 2013 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #09_2020_TT-BKHĐT_145176#preamble_standalone_6 (Loại: `preamble_standalone`)
> **[Căn cứ]`<TU_KHOA_PHAP_LY>`** **[Luật Đấu thầu]`<THAM_CHIEU_PHAP_LY>`** **[ngày 26 tháng 11 năm 2013]`<NGAY_THAM_CHIEU>`** ;

**Thực thể:**
- `[e0]` **Luật Đấu thầu** → `THAM_CHIEU_PHAP_LY` (span: `[1:2]`)
- `[e1]` **Căn cứ** → `TU_KHOA_PHAP_LY` (span: `[0:1]`)
- `[e2]` **ngày 26 tháng 11 năm 2013** → `NGAY_THAM_CHIEU` (span: `[2:8]`)

**Quan hệ:**
- (`e1` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e0` Luật Đấu thầu `[THAM_CHIEU_PHAP_LY]`)
- (`e0` Luật Đấu thầu `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e2` ngày 26 tháng 11 năm 2013 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #09_2020_TT-BKHĐT_145176#preamble_context_7 (Loại: `preamble_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[09/2020/TT-BKHĐT]`<SO_HIEU>`** của **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** . **[Căn cứ]`<TU_KHOA_PHAP_LY>`** **[Nghị quyết số 72/2018/QH14]`<THAM_CHIEU_PHAP_LY>`** **[ngày 12 tháng 11 năm 2018]`<NGAY_THAM_CHIEU>`** của **[Quốc hội]`<CO_QUAN_THAM_QUYEN>`** phê chuẩn Hiệp định Đối tác Toàn diện và Tiến bộ xuyên Thái Bình Dương cùng các văn kiện liên quan ;

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **09/2020/TT-BKHĐT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[4:8]`)
- `[e3]` **Nghị quyết số 72/2018/QH14** → `THAM_CHIEU_PHAP_LY` (span: `[10:13]`)
- `[e4]` **Căn cứ** → `TU_KHOA_PHAP_LY` (span: `[9:10]`)
- `[e5]` **ngày 12 tháng 11 năm 2018** → `NGAY_THAM_CHIEU` (span: `[13:19]`)
- `[e6]` **Quốc hội** → `CO_QUAN_THAM_QUYEN` (span: `[20:21]`)

**Quan hệ:**
- (`e1` 09/2020/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 09/2020/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e4` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Nghị quyết số 72/2018/QH14 `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 09/2020/TT-BKHĐT `[SO_HIEU]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Nghị quyết số 72/2018/QH14 `[THAM_CHIEU_PHAP_LY]`)
- (`e3` Nghị quyết số 72/2018/QH14 `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e5` ngày 12 tháng 11 năm 2018 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #09_2020_TT-BKHĐT_145176#preamble_standalone_8 (Loại: `preamble_standalone`)
> **[Căn cứ]`<TU_KHOA_PHAP_LY>`** **[Nghị quyết số 72/2018/QH14]`<THAM_CHIEU_PHAP_LY>`** **[ngày 12 tháng 11 năm 2018]`<NGAY_THAM_CHIEU>`** của **[Quốc hội]`<CO_QUAN_THAM_QUYEN>`** phê chuẩn Hiệp định Đối tác Toàn diện và Tiến bộ xuyên Thái Bình Dương cùng các văn kiện liên quan ;

**Thực thể:**
- `[e0]` **Nghị quyết số 72/2018/QH14** → `THAM_CHIEU_PHAP_LY` (span: `[1:4]`)
- `[e1]` **Căn cứ** → `TU_KHOA_PHAP_LY` (span: `[0:1]`)
- `[e2]` **ngày 12 tháng 11 năm 2018** → `NGAY_THAM_CHIEU` (span: `[4:10]`)
- `[e3]` **Quốc hội** → `CO_QUAN_THAM_QUYEN` (span: `[11:12]`)

**Quan hệ:**
- (`e1` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e0` Nghị quyết số 72/2018/QH14 `[THAM_CHIEU_PHAP_LY]`)
- (`e3` Quốc hội `[CO_QUAN_THAM_QUYEN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e0` Nghị quyết số 72/2018/QH14 `[THAM_CHIEU_PHAP_LY]`)
- (`e0` Nghị quyết số 72/2018/QH14 `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e2` ngày 12 tháng 11 năm 2018 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #09_2020_TT-BKHĐT_145176#preamble_context_9 (Loại: `preamble_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[09/2020/TT-BKHĐT]`<SO_HIEU>`** của **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** . **[Căn cứ]`<TU_KHOA_PHAP_LY>`** **[Nghị định số 95/2020/NĐ-CP]`<THAM_CHIEU_PHAP_LY>`** **[ngày 24 tháng 8 năm 2020]`<NGAY_THAM_CHIEU>`** của **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** hướng dẫn thực hiện về đấu thầu mua sắm theo Hiệp định Đối tác Toàn diện và Tiến bộ xuyên Thái Bình Dương ;

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **09/2020/TT-BKHĐT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[4:8]`)
- `[e3]` **Nghị định số 95/2020/NĐ-CP** → `THAM_CHIEU_PHAP_LY` (span: `[10:13]`)
- `[e4]` **Căn cứ** → `TU_KHOA_PHAP_LY` (span: `[9:10]`)
- `[e5]` **ngày 24 tháng 8 năm 2020** → `NGAY_THAM_CHIEU` (span: `[13:19]`)
- `[e6]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[20:21]`)

**Quan hệ:**
- (`e1` 09/2020/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 09/2020/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e4` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Nghị định số 95/2020/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 09/2020/TT-BKHĐT `[SO_HIEU]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Nghị định số 95/2020/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e3` Nghị định số 95/2020/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e5` ngày 24 tháng 8 năm 2020 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #09_2020_TT-BKHĐT_145176#preamble_standalone_10 (Loại: `preamble_standalone`)
> **[Căn cứ]`<TU_KHOA_PHAP_LY>`** **[Nghị định số 95/2020/NĐ-CP]`<THAM_CHIEU_PHAP_LY>`** **[ngày 24 tháng 8 năm 2020]`<NGAY_THAM_CHIEU>`** của **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** hướng dẫn thực hiện về đấu thầu mua sắm theo Hiệp định Đối tác Toàn diện và Tiến bộ xuyên Thái Bình Dương ;

**Thực thể:**
- `[e0]` **Nghị định số 95/2020/NĐ-CP** → `THAM_CHIEU_PHAP_LY` (span: `[1:4]`)
- `[e1]` **Căn cứ** → `TU_KHOA_PHAP_LY` (span: `[0:1]`)
- `[e2]` **ngày 24 tháng 8 năm 2020** → `NGAY_THAM_CHIEU` (span: `[4:10]`)
- `[e3]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[11:12]`)

**Quan hệ:**
- (`e1` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e0` Nghị định số 95/2020/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e3` Chính phủ `[CO_QUAN_THAM_QUYEN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e0` Nghị định số 95/2020/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e0` Nghị định số 95/2020/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e2` ngày 24 tháng 8 năm 2020 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #09_2020_TT-BKHĐT_145176#preamble_context_11 (Loại: `preamble_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[09/2020/TT-BKHĐT]`<SO_HIEU>`** của **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** . **[Căn cứ]`<TU_KHOA_PHAP_LY>`** **[Nghị định số 86/2017/NĐ-CP]`<THAM_CHIEU_PHAP_LY>`** **[ngày 25 tháng 7 năm 2017]`<NGAY_THAM_CHIEU>`** của **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** quy định chức năng , nhiệm vụ , quyền hạn và cơ cấu tổ chức của **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_THAM_QUYEN>`** ;

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **09/2020/TT-BKHĐT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[4:8]`)
- `[e3]` **Nghị định số 86/2017/NĐ-CP** → `THAM_CHIEU_PHAP_LY` (span: `[10:13]`)
- `[e4]` **Căn cứ** → `TU_KHOA_PHAP_LY` (span: `[9:10]`)
- `[e5]` **ngày 25 tháng 7 năm 2017** → `NGAY_THAM_CHIEU` (span: `[13:19]`)
- `[e6]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[20:21]`)
- `[e7]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_THAM_QUYEN` (span: `[31:35]`)

**Quan hệ:**
- (`e1` 09/2020/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 09/2020/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e4` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Nghị định số 86/2017/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 09/2020/TT-BKHĐT `[SO_HIEU]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Nghị định số 86/2017/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e3` Nghị định số 86/2017/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e5` ngày 25 tháng 7 năm 2017 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #09_2020_TT-BKHĐT_145176#preamble_standalone_12 (Loại: `preamble_standalone`)
> **[Căn cứ]`<TU_KHOA_PHAP_LY>`** **[Nghị định số 86/2017/NĐ-CP]`<THAM_CHIEU_PHAP_LY>`** **[ngày 25 tháng 7 năm 2017]`<NGAY_THAM_CHIEU>`** của **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** quy định chức năng , nhiệm vụ , quyền hạn và cơ cấu tổ chức của **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_THAM_QUYEN>`** ;

**Thực thể:**
- `[e0]` **Nghị định số 86/2017/NĐ-CP** → `THAM_CHIEU_PHAP_LY` (span: `[1:4]`)
- `[e1]` **Căn cứ** → `TU_KHOA_PHAP_LY` (span: `[0:1]`)
- `[e2]` **ngày 25 tháng 7 năm 2017** → `NGAY_THAM_CHIEU` (span: `[4:10]`)
- `[e3]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[11:12]`)
- `[e4]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_THAM_QUYEN` (span: `[22:26]`)

**Quan hệ:**
- (`e1` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e0` Nghị định số 86/2017/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e3` Chính phủ `[CO_QUAN_THAM_QUYEN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e0` Nghị định số 86/2017/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e0` Nghị định số 86/2017/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e2` ngày 25 tháng 7 năm 2017 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #09_2020_TT-BKHĐT_145176#preamble_context_13 (Loại: `preamble_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[09/2020/TT-BKHĐT]`<SO_HIEU>`** của **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** . **[Bộ trưởng Bộ Kế hoạch và Đầu tư]`<CO_QUAN_THAM_QUYEN>`** ban hành Thông tư quy định chi tiết lập **[hồ sơ mời thầu mua sắm hàng hóa]`<GIAY_TO_HO_SO>`** đối với gói thầu thuộc phạm vi điều chỉnh của Hiệp định Đối tác Toàn diện và Tiến bộ xuyên Thái Bình Dương .

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **09/2020/TT-BKHĐT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[4:8]`)
- `[e3]` **Bộ trưởng Bộ Kế hoạch và Đầu tư** → `CO_QUAN_THAM_QUYEN` (span: `[9:14]`)
- `[e4]` **hồ sơ mời thầu mua sắm hàng hóa** → `GIAY_TO_HO_SO` (span: `[19:23]`)

**Quan hệ:**
- (`e1` 09/2020/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 09/2020/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)


---

### Mẫu #09_2020_TT-BKHĐT_145176#preamble_standalone_14 (Loại: `preamble_standalone`)
> **[Bộ trưởng Bộ Kế hoạch và Đầu tư]`<CO_QUAN_THAM_QUYEN>`** ban hành Thông tư quy định chi tiết lập **[hồ sơ mời thầu mua sắm hàng hóa]`<GIAY_TO_HO_SO>`** đối với gói thầu thuộc phạm vi điều chỉnh của Hiệp định Đối tác Toàn diện và Tiến bộ xuyên Thái Bình Dương .

**Thực thể:**
- `[e0]` **Bộ trưởng Bộ Kế hoạch và Đầu tư** → `CO_QUAN_THAM_QUYEN` (span: `[0:5]`)
- `[e1]` **hồ sơ mời thầu mua sắm hàng hóa** → `GIAY_TO_HO_SO` (span: `[10:14]`)


---

### Mẫu #09_2020_TT-BKHĐT_145176#body_context_15 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[09/2020/TT-BKHĐT]`<SO_HIEU>`** của **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** . **[Điều 1 . Phạm vi điều chỉnh . Thông tư này quy định chi tiết về lập **[hồ sơ mời thầu mua sắm hàng hoá]`<GIAY_TO_HO_SO>`** đối với gói thầu thuộc phạm vi điều chỉnh **[quy định tại]`<TU_KHOA_PHAP_LY>`** **[Điều 1 của Nghị định số 95/2020/NĐ-CP]`<THAM_CHIEU_PHAP_LY>`** **[ngày 24 tháng 8 năm 2020]`<NGAY_THAM_CHIEU>`** của **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** hướng dẫn thực hiện về đấu thầu mua sắm theo Hiệp định Đối tác Toàn diện và Tiến bộ xuyên Thái Bình Dương ( sau đây gọi là **[Nghị định số 95/2020/NĐ-CP]`<THAM_CHIEU_PHAP_LY>`** ) . [ 1 ]]`<DIEU>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **09/2020/TT-BKHĐT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[4:8]`)
- `[e3]` **Điều 1 . Phạm vi điều chỉnh . Thông tư này quy định chi tiết về lập hồ sơ mời thầu mua sắm hàng hoá đối với gói thầu thuộc phạm vi điều chỉnh quy định tại Điều 1 của Nghị định số 95/2020/NĐ-CP ngày 24 tháng 8 năm 2020 của Chính phủ hướng dẫn thực hiện về đấu thầu mua sắm theo Hiệp định Đối tác Toàn diện và Tiến bộ xuyên Thái Bình Dương ( sau đây gọi là Nghị định số 95/2020/NĐ-CP ) . [ 1 ]** → `DIEU` (span: `[9:72]`)
- `[e4]` **Điều 1 của Nghị định số 95/2020/NĐ-CP** → `THAM_CHIEU_PHAP_LY` (span: `[32:38]`) *(lồng trong `e3` (`DIEU`))*
- `[e5]` **Nghị định số 95/2020/NĐ-CP** → `THAM_CHIEU_PHAP_LY` (span: `[64:67]`) *(lồng trong `e3` (`DIEU`))*
- `[e6]` **quy định tại** → `TU_KHOA_PHAP_LY` (span: `[30:32]`) *(lồng trong `e3` (`DIEU`))*
- `[e7]` **ngày 24 tháng 8 năm 2020** → `NGAY_THAM_CHIEU` (span: `[38:44]`) *(lồng trong `e3` (`DIEU`))*
- `[e8]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[45:46]`) *(lồng trong `e3` (`DIEU`))*
- `[e9]` **hồ sơ mời thầu mua sắm hàng hoá** → `GIAY_TO_HO_SO` (span: `[21:25]`) *(lồng trong `e3` (`DIEU`))*

**Quan hệ:**
- (`e1` 09/2020/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 09/2020/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 1 . Phạm vi điều chỉnh . Thông tư này quy định chi tiết về lập hồ sơ mời thầu mua sắm hàng hoá đối với gói thầu thuộc phạm vi điều chỉnh quy định tại Điều 1 của Nghị định số 95/2020/NĐ-CP ngày 24 tháng 8 năm 2020 của Chính phủ hướng dẫn thực hiện về đấu thầu mua sắm theo Hiệp định Đối tác Toàn diện và Tiến bộ xuyên Thái Bình Dương ( sau đây gọi là Nghị định số 95/2020/NĐ-CP ) . [ 1 ] `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 09/2020/TT-BKHĐT `[SO_HIEU]`)
- (`e6` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e4` Điều 1 của Nghị định số 95/2020/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e3` Điều 1 . Phạm vi điều chỉnh . Thông tư này quy định chi tiết về lập hồ sơ mời thầu mua sắm hàng hoá đối với gói thầu thuộc phạm vi điều chỉnh quy định tại Điều 1 của Nghị định số 95/2020/NĐ-CP ngày 24 tháng 8 năm 2020 của Chính phủ hướng dẫn thực hiện về đấu thầu mua sắm theo Hiệp định Đối tác Toàn diện và Tiến bộ xuyên Thái Bình Dương ( sau đây gọi là Nghị định số 95/2020/NĐ-CP ) . [ 1 ] `[DIEU]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e4` Điều 1 của Nghị định số 95/2020/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e6` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e5` Nghị định số 95/2020/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e3` Điều 1 . Phạm vi điều chỉnh . Thông tư này quy định chi tiết về lập hồ sơ mời thầu mua sắm hàng hoá đối với gói thầu thuộc phạm vi điều chỉnh quy định tại Điều 1 của Nghị định số 95/2020/NĐ-CP ngày 24 tháng 8 năm 2020 của Chính phủ hướng dẫn thực hiện về đấu thầu mua sắm theo Hiệp định Đối tác Toàn diện và Tiến bộ xuyên Thái Bình Dương ( sau đây gọi là Nghị định số 95/2020/NĐ-CP ) . [ 1 ] `[DIEU]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e5` Nghị định số 95/2020/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e4` Điều 1 của Nghị định số 95/2020/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e7` ngày 24 tháng 8 năm 2020 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #09_2020_TT-BKHĐT_145176#body_standalone_16 (Loại: `body_standalone`)
> **[Điều 1 . Phạm vi điều chỉnh . Thông tư này quy định chi tiết về lập **[hồ sơ mời thầu mua sắm hàng hoá]`<GIAY_TO_HO_SO>`** đối với gói thầu thuộc phạm vi điều chỉnh **[quy định tại]`<TU_KHOA_PHAP_LY>`** **[Điều 1 của Nghị định số 95/2020/NĐ-CP]`<THAM_CHIEU_PHAP_LY>`** **[ngày 24 tháng 8 năm 2020]`<NGAY_THAM_CHIEU>`** của **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** hướng dẫn thực hiện về đấu thầu mua sắm theo Hiệp định Đối tác Toàn diện và Tiến bộ xuyên Thái Bình Dương ( sau đây gọi là **[Nghị định số 95/2020/NĐ-CP]`<THAM_CHIEU_PHAP_LY>`** ) . [ 1 ]]`<DIEU>`**

**Thực thể:**
- `[e0]` **Điều 1 . Phạm vi điều chỉnh . Thông tư này quy định chi tiết về lập hồ sơ mời thầu mua sắm hàng hoá đối với gói thầu thuộc phạm vi điều chỉnh quy định tại Điều 1 của Nghị định số 95/2020/NĐ-CP ngày 24 tháng 8 năm 2020 của Chính phủ hướng dẫn thực hiện về đấu thầu mua sắm theo Hiệp định Đối tác Toàn diện và Tiến bộ xuyên Thái Bình Dương ( sau đây gọi là Nghị định số 95/2020/NĐ-CP ) . [ 1 ]** → `DIEU` (span: `[0:63]`)
- `[e1]` **Điều 1 của Nghị định số 95/2020/NĐ-CP** → `THAM_CHIEU_PHAP_LY` (span: `[23:29]`) *(lồng trong `e0` (`DIEU`))*
- `[e2]` **Nghị định số 95/2020/NĐ-CP** → `THAM_CHIEU_PHAP_LY` (span: `[55:58]`) *(lồng trong `e0` (`DIEU`))*
- `[e3]` **quy định tại** → `TU_KHOA_PHAP_LY` (span: `[21:23]`) *(lồng trong `e0` (`DIEU`))*
- `[e4]` **ngày 24 tháng 8 năm 2020** → `NGAY_THAM_CHIEU` (span: `[29:35]`) *(lồng trong `e0` (`DIEU`))*
- `[e5]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[36:37]`) *(lồng trong `e0` (`DIEU`))*
- `[e6]` **hồ sơ mời thầu mua sắm hàng hoá** → `GIAY_TO_HO_SO` (span: `[12:16]`) *(lồng trong `e0` (`DIEU`))*

**Quan hệ:**
- (`e3` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e1` Điều 1 của Nghị định số 95/2020/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e0` Điều 1 . Phạm vi điều chỉnh . Thông tư này quy định chi tiết về lập hồ sơ mời thầu mua sắm hàng hoá đối với gói thầu thuộc phạm vi điều chỉnh quy định tại Điều 1 của Nghị định số 95/2020/NĐ-CP ngày 24 tháng 8 năm 2020 của Chính phủ hướng dẫn thực hiện về đấu thầu mua sắm theo Hiệp định Đối tác Toàn diện và Tiến bộ xuyên Thái Bình Dương ( sau đây gọi là Nghị định số 95/2020/NĐ-CP ) . [ 1 ] `[DIEU]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e1` Điều 1 của Nghị định số 95/2020/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e3` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e2` Nghị định số 95/2020/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e0` Điều 1 . Phạm vi điều chỉnh . Thông tư này quy định chi tiết về lập hồ sơ mời thầu mua sắm hàng hoá đối với gói thầu thuộc phạm vi điều chỉnh quy định tại Điều 1 của Nghị định số 95/2020/NĐ-CP ngày 24 tháng 8 năm 2020 của Chính phủ hướng dẫn thực hiện về đấu thầu mua sắm theo Hiệp định Đối tác Toàn diện và Tiến bộ xuyên Thái Bình Dương ( sau đây gọi là Nghị định số 95/2020/NĐ-CP ) . [ 1 ] `[DIEU]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e2` Nghị định số 95/2020/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e1` Điều 1 của Nghị định số 95/2020/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e4` ngày 24 tháng 8 năm 2020 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #09_2020_TT-BKHĐT_145176#body_context_17 (Loại: `body_context`)
> **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[09/2020/TT-BKHĐT]`<SO_HIEU>`** . **[Điều 2 . Đối tượng áp dụng . Thông tư này áp dụng đối với tổ chức , cá nhân tham gia hoặc có liên quan đến hoạt động lựa chọn nhà thầu gói thầu mua sắm hàng hoá thuộc phạm vi điều chỉnh **[quy định tại]`<TU_KHOA_PHAP_LY>`** **[Điều 1 của Thông tư này]`<THAM_CHIEU_PHAP_LY>`** .]`<DIEU>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[5:6]`)
- `[e1]` **09/2020/TT-BKHĐT** → `SO_HIEU` (span: `[7:8]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[0:4]`)
- `[e3]` **Điều 2 . Đối tượng áp dụng . Thông tư này áp dụng đối với tổ chức , cá nhân tham gia hoặc có liên quan đến hoạt động lựa chọn nhà thầu gói thầu mua sắm hàng hoá thuộc phạm vi điều chỉnh quy định tại Điều 1 của Thông tư này .** → `DIEU` (span: `[9:44]`)
- `[e4]` **Điều 1 của Thông tư này** → `THAM_CHIEU_PHAP_LY` (span: `[38:43]`) *(lồng trong `e3` (`DIEU`))*
- `[e5]` **quy định tại** → `TU_KHOA_PHAP_LY` (span: `[36:38]`) *(lồng trong `e3` (`DIEU`))*

**Quan hệ:**
- (`e1` 09/2020/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 09/2020/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 2 . Đối tượng áp dụng . Thông tư này áp dụng đối với tổ chức , cá nhân tham gia hoặc có liên quan đến hoạt động lựa chọn nhà thầu gói thầu mua sắm hàng hoá thuộc phạm vi điều chỉnh quy định tại Điều 1 của Thông tư này . `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 09/2020/TT-BKHĐT `[SO_HIEU]`)
- (`e5` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e4` Điều 1 của Thông tư này `[THAM_CHIEU_PHAP_LY]`)
- (`e3` Điều 2 . Đối tượng áp dụng . Thông tư này áp dụng đối với tổ chức , cá nhân tham gia hoặc có liên quan đến hoạt động lựa chọn nhà thầu gói thầu mua sắm hàng hoá thuộc phạm vi điều chỉnh quy định tại Điều 1 của Thông tư này . `[DIEU]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e4` Điều 1 của Thông tư này `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #09_2020_TT-BKHĐT_145176#body_standalone_18 (Loại: `body_standalone`)
> **[Điều 2 . Đối tượng áp dụng . Thông tư này áp dụng đối với tổ chức , cá nhân tham gia hoặc có liên quan đến hoạt động lựa chọn nhà thầu gói thầu mua sắm hàng hoá thuộc phạm vi điều chỉnh **[quy định tại]`<TU_KHOA_PHAP_LY>`** **[Điều 1 của Thông tư này]`<THAM_CHIEU_PHAP_LY>`** .]`<DIEU>`**

**Thực thể:**
- `[e0]` **Điều 2 . Đối tượng áp dụng . Thông tư này áp dụng đối với tổ chức , cá nhân tham gia hoặc có liên quan đến hoạt động lựa chọn nhà thầu gói thầu mua sắm hàng hoá thuộc phạm vi điều chỉnh quy định tại Điều 1 của Thông tư này .** → `DIEU` (span: `[0:35]`)
- `[e1]` **Điều 1 của Thông tư này** → `THAM_CHIEU_PHAP_LY` (span: `[29:34]`) *(lồng trong `e0` (`DIEU`))*
- `[e2]` **quy định tại** → `TU_KHOA_PHAP_LY` (span: `[27:29]`) *(lồng trong `e0` (`DIEU`))*

**Quan hệ:**
- (`e2` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e1` Điều 1 của Thông tư này `[THAM_CHIEU_PHAP_LY]`)
- (`e0` Điều 2 . Đối tượng áp dụng . Thông tư này áp dụng đối với tổ chức , cá nhân tham gia hoặc có liên quan đến hoạt động lựa chọn nhà thầu gói thầu mua sắm hàng hoá thuộc phạm vi điều chỉnh quy định tại Điều 1 của Thông tư này . `[DIEU]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e1` Điều 1 của Thông tư này `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #09_2020_TT-BKHĐT_145176#body_context_19 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[09/2020/TT-BKHĐT]`<SO_HIEU>`** ban hành **[ngày 27 tháng 11 năm 2020]`<NGAY_BAN_HANH>`** bởi **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** . **[Điều 3 . Áp dụng Mẫu **[hồ sơ mời thầu mua sắm hàng hoá]`<GIAY_TO_HO_SO>`**]`<DIEU>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **09/2020/TT-BKHĐT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[11:15]`)
- `[e3]` **ngày 27 tháng 11 năm 2020** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 3 . Áp dụng Mẫu hồ sơ mời thầu mua sắm hàng hoá** → `DIEU` (span: `[16:25]`)
- `[e5]` **hồ sơ mời thầu mua sắm hàng hoá** → `GIAY_TO_HO_SO` (span: `[21:25]`) *(lồng trong `e4` (`DIEU`))*

**Quan hệ:**
- (`e1` 09/2020/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 09/2020/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 09/2020/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 27 tháng 11 năm 2020 `[NGAY_BAN_HANH]`)
- (`e4` Điều 3 . Áp dụng Mẫu hồ sơ mời thầu mua sắm hàng hoá `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 09/2020/TT-BKHĐT `[SO_HIEU]`)


---

### Mẫu #09_2020_TT-BKHĐT_145176#body_context_20 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[09/2020/TT-BKHĐT]`<SO_HIEU>`** của **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** . **[Điều 3]`<DIEU>`** . **[1 . Áp dụng Mẫu **[hồ sơ mời thầu]`<GIAY_TO_HO_SO>`** :]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **09/2020/TT-BKHĐT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[4:8]`)
- `[e3]` **Điều 3** → `DIEU` (span: `[9:11]`)
- `[e4]` **1 . Áp dụng Mẫu hồ sơ mời thầu :** → `KHOAN` (span: `[12:19]`)
- `[e5]` **hồ sơ mời thầu** → `GIAY_TO_HO_SO` (span: `[16:18]`) *(lồng trong `e4` (`KHOAN`))*

**Quan hệ:**
- (`e1` 09/2020/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 09/2020/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 3 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 09/2020/TT-BKHĐT `[SO_HIEU]`)
- (`e4` 1 . Áp dụng Mẫu hồ sơ mời thầu : `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 3 `[DIEU]`)


---

### Mẫu #09_2020_TT-BKHĐT_145176#body_context_21 (Loại: `body_context`)
> **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[09/2020/TT-BKHĐT]`<SO_HIEU>`** . **[Điều 3]`<DIEU>`** . **[Khoản 1]`<KHOAN>`** . **[a ) Mẫu **[hồ sơ mời thầu mua sắm hàng hoá số 01]`<GIAY_TO_HO_SO>`** ( **[Mẫu số 01]`<THAM_CHIEU_PHAP_LY>`** ) áp dụng cho gói thầu đấu thầu rộng rãi theo phương thức lựa chọn nhà thầu một giai đoạn một túi hồ sơ ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[5:6]`)
- `[e1]` **09/2020/TT-BKHĐT** → `SO_HIEU` (span: `[7:8]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[0:4]`)
- `[e3]` **Điều 3** → `DIEU` (span: `[9:11]`)
- `[e4]` **Khoản 1** → `KHOAN` (span: `[12:14]`)
- `[e5]` **a ) Mẫu hồ sơ mời thầu mua sắm hàng hoá số 01 ( Mẫu số 01 ) áp dụng cho gói thầu đấu thầu rộng rãi theo phương thức lựa chọn nhà thầu một giai đoạn một túi hồ sơ ;** → `DIEM` (span: `[15:43]`)
- `[e6]` **Mẫu số 01** → `THAM_CHIEU_PHAP_LY` (span: `[25:27]`) *(lồng trong `e5` (`DIEM`))*
- `[e7]` **hồ sơ mời thầu mua sắm hàng hoá số 01** → `GIAY_TO_HO_SO` (span: `[18:24]`) *(lồng trong `e5` (`DIEM`))*

**Quan hệ:**
- (`e1` 09/2020/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 09/2020/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 3 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 09/2020/TT-BKHĐT `[SO_HIEU]`)
- (`e4` Khoản 1 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 3 `[DIEU]`)
- (`e5` a ) Mẫu hồ sơ mời thầu mua sắm hàng hoá số 01 ( Mẫu số 01 ) áp dụng cho gói thầu đấu thầu rộng rãi theo phương thức lựa chọn nhà thầu một giai đoạn một túi hồ sơ ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e4` Khoản 1 `[KHOAN]`)
- (`e5` a ) Mẫu hồ sơ mời thầu mua sắm hàng hoá số 01 ( Mẫu số 01 ) áp dụng cho gói thầu đấu thầu rộng rãi theo phương thức lựa chọn nhà thầu một giai đoạn một túi hồ sơ ; `[DIEM]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e6` Mẫu số 01 `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #09_2020_TT-BKHĐT_145176#body_standalone_22 (Loại: `body_standalone`)
> **[Điều 3]`<DIEU>`** . **[Khoản 1]`<KHOAN>`** . **[a ) Mẫu **[hồ sơ mời thầu mua sắm hàng hoá số 01]`<GIAY_TO_HO_SO>`** ( **[Mẫu số 01]`<THAM_CHIEU_PHAP_LY>`** ) áp dụng cho gói thầu đấu thầu rộng rãi theo phương thức lựa chọn nhà thầu một giai đoạn một túi hồ sơ ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Điều 3** → `DIEU` (span: `[0:2]`)
- `[e1]` **Khoản 1** → `KHOAN` (span: `[3:5]`)
- `[e2]` **a ) Mẫu hồ sơ mời thầu mua sắm hàng hoá số 01 ( Mẫu số 01 ) áp dụng cho gói thầu đấu thầu rộng rãi theo phương thức lựa chọn nhà thầu một giai đoạn một túi hồ sơ ;** → `DIEM` (span: `[6:34]`)
- `[e3]` **Mẫu số 01** → `THAM_CHIEU_PHAP_LY` (span: `[16:18]`) *(lồng trong `e2` (`DIEM`))*
- `[e4]` **hồ sơ mời thầu mua sắm hàng hoá số 01** → `GIAY_TO_HO_SO` (span: `[9:15]`) *(lồng trong `e2` (`DIEM`))*

**Quan hệ:**
- (`e1` Khoản 1 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 3 `[DIEU]`)
- (`e2` a ) Mẫu hồ sơ mời thầu mua sắm hàng hoá số 01 ( Mẫu số 01 ) áp dụng cho gói thầu đấu thầu rộng rãi theo phương thức lựa chọn nhà thầu một giai đoạn một túi hồ sơ ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e1` Khoản 1 `[KHOAN]`)
- (`e2` a ) Mẫu hồ sơ mời thầu mua sắm hàng hoá số 01 ( Mẫu số 01 ) áp dụng cho gói thầu đấu thầu rộng rãi theo phương thức lựa chọn nhà thầu một giai đoạn một túi hồ sơ ; `[DIEM]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Mẫu số 01 `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #09_2020_TT-BKHĐT_145176#body_context_23 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[09/2020/TT-BKHĐT]`<SO_HIEU>`** ban hành **[ngày 27 tháng 11 năm 2020]`<NGAY_BAN_HANH>`** bởi **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** . **[Điều 3]`<DIEU>`** . **[Khoản 1]`<KHOAN>`** . **[b ) Mẫu **[hồ sơ mời thầu mua sắm hàng hoá số 02]`<GIAY_TO_HO_SO>`** ( **[Mẫu số 02]`<THAM_CHIEU_PHAP_LY>`** ) áp dụng cho gói thầu đấu thầu rộng rãi theo phương thức lựa chọn nhà thầu một giai đoạn hai túi hồ sơ .]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **09/2020/TT-BKHĐT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[11:15]`)
- `[e3]` **ngày 27 tháng 11 năm 2020** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 3** → `DIEU` (span: `[16:18]`)
- `[e5]` **Khoản 1** → `KHOAN` (span: `[19:21]`)
- `[e6]` **b ) Mẫu hồ sơ mời thầu mua sắm hàng hoá số 02 ( Mẫu số 02 ) áp dụng cho gói thầu đấu thầu rộng rãi theo phương thức lựa chọn nhà thầu một giai đoạn hai túi hồ sơ .** → `DIEM` (span: `[22:50]`)
- `[e7]` **Mẫu số 02** → `THAM_CHIEU_PHAP_LY` (span: `[32:34]`) *(lồng trong `e6` (`DIEM`))*
- `[e8]` **hồ sơ mời thầu mua sắm hàng hoá số 02** → `GIAY_TO_HO_SO` (span: `[25:31]`) *(lồng trong `e6` (`DIEM`))*

**Quan hệ:**
- (`e1` 09/2020/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 09/2020/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 09/2020/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 27 tháng 11 năm 2020 `[NGAY_BAN_HANH]`)
- (`e4` Điều 3 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 09/2020/TT-BKHĐT `[SO_HIEU]`)
- (`e5` Khoản 1 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 3 `[DIEU]`)
- (`e6` b ) Mẫu hồ sơ mời thầu mua sắm hàng hoá số 02 ( Mẫu số 02 ) áp dụng cho gói thầu đấu thầu rộng rãi theo phương thức lựa chọn nhà thầu một giai đoạn hai túi hồ sơ . `[DIEM]`) ==[ **THUOC_VE** ]==> (`e5` Khoản 1 `[KHOAN]`)
- (`e6` b ) Mẫu hồ sơ mời thầu mua sắm hàng hoá số 02 ( Mẫu số 02 ) áp dụng cho gói thầu đấu thầu rộng rãi theo phương thức lựa chọn nhà thầu một giai đoạn hai túi hồ sơ . `[DIEM]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e7` Mẫu số 02 `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #09_2020_TT-BKHĐT_145176#body_standalone_24 (Loại: `body_standalone`)
> **[Điều 3]`<DIEU>`** . **[Khoản 1]`<KHOAN>`** . **[b ) Mẫu **[hồ sơ mời thầu mua sắm hàng hoá số 02]`<GIAY_TO_HO_SO>`** ( **[Mẫu số 02]`<THAM_CHIEU_PHAP_LY>`** ) áp dụng cho gói thầu đấu thầu rộng rãi theo phương thức lựa chọn nhà thầu một giai đoạn hai túi hồ sơ .]`<DIEM>`**

**Thực thể:**
- `[e0]` **Điều 3** → `DIEU` (span: `[0:2]`)
- `[e1]` **Khoản 1** → `KHOAN` (span: `[3:5]`)
- `[e2]` **b ) Mẫu hồ sơ mời thầu mua sắm hàng hoá số 02 ( Mẫu số 02 ) áp dụng cho gói thầu đấu thầu rộng rãi theo phương thức lựa chọn nhà thầu một giai đoạn hai túi hồ sơ .** → `DIEM` (span: `[6:34]`)
- `[e3]` **Mẫu số 02** → `THAM_CHIEU_PHAP_LY` (span: `[16:18]`) *(lồng trong `e2` (`DIEM`))*
- `[e4]` **hồ sơ mời thầu mua sắm hàng hoá số 02** → `GIAY_TO_HO_SO` (span: `[9:15]`) *(lồng trong `e2` (`DIEM`))*

**Quan hệ:**
- (`e1` Khoản 1 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 3 `[DIEU]`)
- (`e2` b ) Mẫu hồ sơ mời thầu mua sắm hàng hoá số 02 ( Mẫu số 02 ) áp dụng cho gói thầu đấu thầu rộng rãi theo phương thức lựa chọn nhà thầu một giai đoạn hai túi hồ sơ . `[DIEM]`) ==[ **THUOC_VE** ]==> (`e1` Khoản 1 `[KHOAN]`)
- (`e2` b ) Mẫu hồ sơ mời thầu mua sắm hàng hoá số 02 ( Mẫu số 02 ) áp dụng cho gói thầu đấu thầu rộng rãi theo phương thức lựa chọn nhà thầu một giai đoạn hai túi hồ sơ . `[DIEM]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Mẫu số 02 `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #09_2020_TT-BKHĐT_145176#body_context_25 (Loại: `body_context`)
> **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[09/2020/TT-BKHĐT]`<SO_HIEU>`** . **[Điều 3]`<DIEU>`** . **[2 . Khi lập , thẩm định , phê duyệt **[hồ sơ mời thầu gói thầu mua sắm hàng hoá]`<GIAY_TO_HO_SO>`** , tổ chức , cá nhân phải :]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[5:6]`)
- `[e1]` **09/2020/TT-BKHĐT** → `SO_HIEU` (span: `[7:8]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[0:4]`)
- `[e3]` **Điều 3** → `DIEU` (span: `[9:11]`)
- `[e4]` **2 . Khi lập , thẩm định , phê duyệt hồ sơ mời thầu gói thầu mua sắm hàng hoá , tổ chức , cá nhân phải :** → `KHOAN` (span: `[12:31]`)
- `[e5]` **hồ sơ mời thầu gói thầu mua sắm hàng hoá** → `GIAY_TO_HO_SO` (span: `[20:25]`) *(lồng trong `e4` (`KHOAN`))*

**Quan hệ:**
- (`e1` 09/2020/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 09/2020/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 3 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 09/2020/TT-BKHĐT `[SO_HIEU]`)
- (`e4` 2 . Khi lập , thẩm định , phê duyệt hồ sơ mời thầu gói thầu mua sắm hàng hoá , tổ chức , cá nhân phải : `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 3 `[DIEU]`)


---

### Mẫu #09_2020_TT-BKHĐT_145176#body_context_26 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[09/2020/TT-BKHĐT]`<SO_HIEU>`** của **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** . **[Điều 3]`<DIEU>`** . **[Khoản 2]`<KHOAN>`** . **[a ) Căn cứ vào quy mô , tính chất của từng gói thầu cụ thể để đưa ra các yêu cầu phù hợp trên cơ sở bảo đảm nguyên tắc cạnh tranh , công bằng , minh bạch và hiệu quả kinh tế ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **09/2020/TT-BKHĐT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[4:8]`)
- `[e3]` **Điều 3** → `DIEU` (span: `[9:11]`)
- `[e4]` **Khoản 2** → `KHOAN` (span: `[12:14]`)
- `[e5]` **a ) Căn cứ vào quy mô , tính chất của từng gói thầu cụ thể để đưa ra các yêu cầu phù hợp trên cơ sở bảo đảm nguyên tắc cạnh tranh , công bằng , minh bạch và hiệu quả kinh tế ;** → `DIEM` (span: `[15:45]`)

**Quan hệ:**
- (`e1` 09/2020/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 09/2020/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 3 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 09/2020/TT-BKHĐT `[SO_HIEU]`)
- (`e4` Khoản 2 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 3 `[DIEU]`)
- (`e5` a ) Căn cứ vào quy mô , tính chất của từng gói thầu cụ thể để đưa ra các yêu cầu phù hợp trên cơ sở bảo đảm nguyên tắc cạnh tranh , công bằng , minh bạch và hiệu quả kinh tế ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e4` Khoản 2 `[KHOAN]`)


---

### Mẫu #09_2020_TT-BKHĐT_145176#body_context_27 (Loại: `body_context`)
> **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[09/2020/TT-BKHĐT]`<SO_HIEU>`** . **[Điều 3]`<DIEU>`** . **[Khoản 2]`<KHOAN>`** . **[b ) Căn cứ nhu cầu sử dụng của hàng hoá để đưa ra các yêu cầu về kỹ thuật ( đặc tính , thông số kỹ thuật … ) bảo đảm đáp ứng về công năng , phù hợp với nhu cầu sử dụng thực tế cũng như điều kiện của thị trường ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[5:6]`)
- `[e1]` **09/2020/TT-BKHĐT** → `SO_HIEU` (span: `[7:8]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[0:4]`)
- `[e3]` **Điều 3** → `DIEU` (span: `[9:11]`)
- `[e4]` **Khoản 2** → `KHOAN` (span: `[12:14]`)
- `[e5]` **b ) Căn cứ nhu cầu sử dụng của hàng hoá để đưa ra các yêu cầu về kỹ thuật ( đặc tính , thông số kỹ thuật … ) bảo đảm đáp ứng về công năng , phù hợp với nhu cầu sử dụng thực tế cũng như điều kiện của thị trường ;** → `DIEM` (span: `[15:52]`)

**Quan hệ:**
- (`e1` 09/2020/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 09/2020/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 3 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 09/2020/TT-BKHĐT `[SO_HIEU]`)
- (`e4` Khoản 2 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 3 `[DIEU]`)
- (`e5` b ) Căn cứ nhu cầu sử dụng của hàng hoá để đưa ra các yêu cầu về kỹ thuật ( đặc tính , thông số kỹ thuật … ) bảo đảm đáp ứng về công năng , phù hợp với nhu cầu sử dụng thực tế cũng như điều kiện của thị trường ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e4` Khoản 2 `[KHOAN]`)


---

### Mẫu #09_2020_TT-BKHĐT_145176#body_context_28 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[09/2020/TT-BKHĐT]`<SO_HIEU>`** ban hành **[ngày 27 tháng 11 năm 2020]`<NGAY_BAN_HANH>`** bởi **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** . **[Điều 3]`<DIEU>`** . **[Khoản 2]`<KHOAN>`** . **[c ) Trường hợp đấu thầu nội khối , trong **[hồ sơ mời thầu ghi rõ chỉ]`<GIAY_TO_HO_SO>`** cho phép nhà thầu nội khối chào **[hàng hóa]`<TAI_SAN_VAT_CHAT>`** có xuất xứ từ các Nước thành viên tham dự thầu . Nước thành viên là nước thỏa mãn các điều kiện sau : - Ký kết Hiệp định Đối tác Toàn diện và Tiến bộ xuyên Thái Bình Dương ( sau đây gọi là Hiệp định CPTPP ) ngày 08 tháng 3 năm 2018 ; - Tại thời điểm phê duyệt **[hồ sơ mời thầu của gói thầu]`<GIAY_TO_HO_SO>`** , Hiệp]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **09/2020/TT-BKHĐT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[11:15]`)
- `[e3]` **ngày 27 tháng 11 năm 2020** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 3** → `DIEU` (span: `[16:18]`)
- `[e5]` **Khoản 2** → `KHOAN` (span: `[19:21]`)
- `[e6]` **c ) Trường hợp đấu thầu nội khối , trong hồ sơ mời thầu ghi rõ chỉ cho phép nhà thầu nội khối chào hàng hóa có xuất xứ từ các Nước thành viên tham dự thầu . Nước thành viên là nước thỏa mãn các điều kiện sau : - Ký kết Hiệp định Đối tác Toàn diện và Tiến bộ xuyên Thái Bình Dương ( sau đây gọi là Hiệp định CPTPP ) ngày 08 tháng 3 năm 2018 ; - Tại thời điểm phê duyệt hồ sơ mời thầu của gói thầu , Hiệp** → `DIEM` (span: `[22:93]`)
- `[e7]` **hàng hóa** → `TAI_SAN_VAT_CHAT` (span: `[41:42]`) *(lồng trong `e6` (`DIEM`))*
- `[e8]` **hồ sơ mời thầu ghi rõ chỉ** → `GIAY_TO_HO_SO` (span: `[30:35]`) *(lồng trong `e6` (`DIEM`))*
- `[e9]` **hồ sơ mời thầu của gói thầu** → `GIAY_TO_HO_SO` (span: `[87:91]`) *(lồng trong `e6` (`DIEM`))*

**Quan hệ:**
- (`e1` 09/2020/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 09/2020/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 09/2020/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 27 tháng 11 năm 2020 `[NGAY_BAN_HANH]`)
- (`e4` Điều 3 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 09/2020/TT-BKHĐT `[SO_HIEU]`)
- (`e5` Khoản 2 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 3 `[DIEU]`)
- (`e6` c ) Trường hợp đấu thầu nội khối , trong hồ sơ mời thầu ghi rõ chỉ cho phép nhà thầu nội khối chào hàng hóa có xuất xứ từ các Nước thành viên tham dự thầu . Nước thành viên là nước thỏa mãn các điều kiện sau : - Ký kết Hiệp định Đối tác Toàn diện và Tiến bộ xuyên Thái Bình Dương ( sau đây gọi là Hiệp định CPTPP ) ngày 08 tháng 3 năm 2018 ; - Tại thời điểm phê duyệt hồ sơ mời thầu của gói thầu , Hiệp `[DIEM]`) ==[ **THUOC_VE** ]==> (`e5` Khoản 2 `[KHOAN]`)


---

### Mẫu #09_2020_TT-BKHĐT_145176#body_standalone_29 (Loại: `body_standalone`)
> **[Điều 3]`<DIEU>`** . **[Khoản 2]`<KHOAN>`** . **[c ) Trường hợp đấu thầu nội khối , trong **[hồ sơ mời thầu ghi rõ chỉ]`<GIAY_TO_HO_SO>`** cho phép nhà thầu nội khối chào **[hàng hóa]`<TAI_SAN_VAT_CHAT>`** có xuất xứ từ các Nước thành viên tham dự thầu . Nước thành viên là nước thỏa mãn các điều kiện sau : - Ký kết Hiệp định Đối tác Toàn diện và Tiến bộ xuyên Thái Bình Dương ( sau đây gọi là Hiệp định CPTPP ) ngày 08 tháng 3 năm 2018 ; - Tại thời điểm phê duyệt **[hồ sơ mời thầu của gói thầu]`<GIAY_TO_HO_SO>`** , Hiệp]`<DIEM>`**

**Thực thể:**
- `[e0]` **Điều 3** → `DIEU` (span: `[0:2]`)
- `[e1]` **Khoản 2** → `KHOAN` (span: `[3:5]`)
- `[e2]` **c ) Trường hợp đấu thầu nội khối , trong hồ sơ mời thầu ghi rõ chỉ cho phép nhà thầu nội khối chào hàng hóa có xuất xứ từ các Nước thành viên tham dự thầu . Nước thành viên là nước thỏa mãn các điều kiện sau : - Ký kết Hiệp định Đối tác Toàn diện và Tiến bộ xuyên Thái Bình Dương ( sau đây gọi là Hiệp định CPTPP ) ngày 08 tháng 3 năm 2018 ; - Tại thời điểm phê duyệt hồ sơ mời thầu của gói thầu , Hiệp** → `DIEM` (span: `[6:77]`)
- `[e3]` **hàng hóa** → `TAI_SAN_VAT_CHAT` (span: `[25:26]`) *(lồng trong `e2` (`DIEM`))*
- `[e4]` **hồ sơ mời thầu ghi rõ chỉ** → `GIAY_TO_HO_SO` (span: `[14:19]`) *(lồng trong `e2` (`DIEM`))*
- `[e5]` **hồ sơ mời thầu của gói thầu** → `GIAY_TO_HO_SO` (span: `[71:75]`) *(lồng trong `e2` (`DIEM`))*

**Quan hệ:**
- (`e1` Khoản 2 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 3 `[DIEU]`)
- (`e2` c ) Trường hợp đấu thầu nội khối , trong hồ sơ mời thầu ghi rõ chỉ cho phép nhà thầu nội khối chào hàng hóa có xuất xứ từ các Nước thành viên tham dự thầu . Nước thành viên là nước thỏa mãn các điều kiện sau : - Ký kết Hiệp định Đối tác Toàn diện và Tiến bộ xuyên Thái Bình Dương ( sau đây gọi là Hiệp định CPTPP ) ngày 08 tháng 3 năm 2018 ; - Tại thời điểm phê duyệt hồ sơ mời thầu của gói thầu , Hiệp `[DIEM]`) ==[ **THUOC_VE** ]==> (`e1` Khoản 2 `[KHOAN]`)


---

### Mẫu #09_2020_TT-BKHĐT_145176#body_context_30 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[09/2020/TT-BKHĐT]`<SO_HIEU>`** ban hành **[ngày 27 tháng 11 năm 2020]`<NGAY_BAN_HANH>`** bởi **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** . **[Điều 3]`<DIEU>`** . **[Khoản 2]`<KHOAN>`** . **[d ) Không được đưa ra các điều kiện nhằm hạn chế sự tham gia của nhà thầu hoặc nhằm tạo lợi thế cho một hoặc một số nhà thầu gây ra sự cạnh tranh không bình đẳng như nêu nhãn hiệu , xuất xứ cụ thể của hàng hoá , kể cả việc nêu tên nước , nhóm nước , vùng lãnh thổ gây ra sự phân biệt đối xử , trừ trường hợp đấu thầu nội khối **[theo quy định tại]`<TU_KHOA_PHAP_LY>`** **[Điều 4 và Điều 15 của Nghị định số 95/2020/NĐ-CP]`<THAM_CHIEU_PHAP_LY>`** và điểm]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **09/2020/TT-BKHĐT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[11:15]`)
- `[e3]` **ngày 27 tháng 11 năm 2020** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 3** → `DIEU` (span: `[16:18]`)
- `[e5]` **Khoản 2** → `KHOAN` (span: `[19:21]`)
- `[e6]` **d ) Không được đưa ra các điều kiện nhằm hạn chế sự tham gia của nhà thầu hoặc nhằm tạo lợi thế cho một hoặc một số nhà thầu gây ra sự cạnh tranh không bình đẳng như nêu nhãn hiệu , xuất xứ cụ thể của hàng hoá , kể cả việc nêu tên nước , nhóm nước , vùng lãnh thổ gây ra sự phân biệt đối xử , trừ trường hợp đấu thầu nội khối theo quy định tại Điều 4 và Điều 15 của Nghị định số 95/2020/NĐ-CP và điểm** → `DIEM` (span: `[22:96]`)
- `[e7]` **Điều 4 và Điều 15 của Nghị định số 95/2020/NĐ-CP** → `THAM_CHIEU_PHAP_LY` (span: `[85:94]`) *(lồng trong `e6` (`DIEM`))*
- `[e8]` **theo quy định tại** → `TU_KHOA_PHAP_LY` (span: `[82:85]`) *(lồng trong `e6` (`DIEM`))*

**Quan hệ:**
- (`e1` 09/2020/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 09/2020/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 09/2020/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 27 tháng 11 năm 2020 `[NGAY_BAN_HANH]`)
- (`e4` Điều 3 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 09/2020/TT-BKHĐT `[SO_HIEU]`)
- (`e5` Khoản 2 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 3 `[DIEU]`)
- (`e6` d ) Không được đưa ra các điều kiện nhằm hạn chế sự tham gia của nhà thầu hoặc nhằm tạo lợi thế cho một hoặc một số nhà thầu gây ra sự cạnh tranh không bình đẳng như nêu nhãn hiệu , xuất xứ cụ thể của hàng hoá , kể cả việc nêu tên nước , nhóm nước , vùng lãnh thổ gây ra sự phân biệt đối xử , trừ trường hợp đấu thầu nội khối theo quy định tại Điều 4 và Điều 15 của Nghị định số 95/2020/NĐ-CP và điểm `[DIEM]`) ==[ **THUOC_VE** ]==> (`e5` Khoản 2 `[KHOAN]`)
- (`e8` theo quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e7` Điều 4 và Điều 15 của Nghị định số 95/2020/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e6` d ) Không được đưa ra các điều kiện nhằm hạn chế sự tham gia của nhà thầu hoặc nhằm tạo lợi thế cho một hoặc một số nhà thầu gây ra sự cạnh tranh không bình đẳng như nêu nhãn hiệu , xuất xứ cụ thể của hàng hoá , kể cả việc nêu tên nước , nhóm nước , vùng lãnh thổ gây ra sự phân biệt đối xử , trừ trường hợp đấu thầu nội khối theo quy định tại Điều 4 và Điều 15 của Nghị định số 95/2020/NĐ-CP và điểm `[DIEM]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e7` Điều 4 và Điều 15 của Nghị định số 95/2020/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #09_2020_TT-BKHĐT_145176#body_standalone_31 (Loại: `body_standalone`)
> **[Điều 3]`<DIEU>`** . **[Khoản 2]`<KHOAN>`** . **[d ) Không được đưa ra các điều kiện nhằm hạn chế sự tham gia của nhà thầu hoặc nhằm tạo lợi thế cho một hoặc một số nhà thầu gây ra sự cạnh tranh không bình đẳng như nêu nhãn hiệu , xuất xứ cụ thể của hàng hoá , kể cả việc nêu tên nước , nhóm nước , vùng lãnh thổ gây ra sự phân biệt đối xử , trừ trường hợp đấu thầu nội khối **[theo quy định tại]`<TU_KHOA_PHAP_LY>`** **[Điều 4 và Điều 15 của Nghị định số 95/2020/NĐ-CP]`<THAM_CHIEU_PHAP_LY>`** và điểm]`<DIEM>`**

**Thực thể:**
- `[e0]` **Điều 3** → `DIEU` (span: `[0:2]`)
- `[e1]` **Khoản 2** → `KHOAN` (span: `[3:5]`)
- `[e2]` **d ) Không được đưa ra các điều kiện nhằm hạn chế sự tham gia của nhà thầu hoặc nhằm tạo lợi thế cho một hoặc một số nhà thầu gây ra sự cạnh tranh không bình đẳng như nêu nhãn hiệu , xuất xứ cụ thể của hàng hoá , kể cả việc nêu tên nước , nhóm nước , vùng lãnh thổ gây ra sự phân biệt đối xử , trừ trường hợp đấu thầu nội khối theo quy định tại Điều 4 và Điều 15 của Nghị định số 95/2020/NĐ-CP và điểm** → `DIEM` (span: `[6:80]`)
- `[e3]` **Điều 4 và Điều 15 của Nghị định số 95/2020/NĐ-CP** → `THAM_CHIEU_PHAP_LY` (span: `[69:78]`) *(lồng trong `e2` (`DIEM`))*
- `[e4]` **theo quy định tại** → `TU_KHOA_PHAP_LY` (span: `[66:69]`) *(lồng trong `e2` (`DIEM`))*

**Quan hệ:**
- (`e1` Khoản 2 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 3 `[DIEU]`)
- (`e2` d ) Không được đưa ra các điều kiện nhằm hạn chế sự tham gia của nhà thầu hoặc nhằm tạo lợi thế cho một hoặc một số nhà thầu gây ra sự cạnh tranh không bình đẳng như nêu nhãn hiệu , xuất xứ cụ thể của hàng hoá , kể cả việc nêu tên nước , nhóm nước , vùng lãnh thổ gây ra sự phân biệt đối xử , trừ trường hợp đấu thầu nội khối theo quy định tại Điều 4 và Điều 15 của Nghị định số 95/2020/NĐ-CP và điểm `[DIEM]`) ==[ **THUOC_VE** ]==> (`e1` Khoản 2 `[KHOAN]`)
- (`e4` theo quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Điều 4 và Điều 15 của Nghị định số 95/2020/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e2` d ) Không được đưa ra các điều kiện nhằm hạn chế sự tham gia của nhà thầu hoặc nhằm tạo lợi thế cho một hoặc một số nhà thầu gây ra sự cạnh tranh không bình đẳng như nêu nhãn hiệu , xuất xứ cụ thể của hàng hoá , kể cả việc nêu tên nước , nhóm nước , vùng lãnh thổ gây ra sự phân biệt đối xử , trừ trường hợp đấu thầu nội khối theo quy định tại Điều 4 và Điều 15 của Nghị định số 95/2020/NĐ-CP và điểm `[DIEM]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Điều 4 và Điều 15 của Nghị định số 95/2020/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #09_2020_TT-BKHĐT_145176#body_context_32 (Loại: `body_context`)
> **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[09/2020/TT-BKHĐT]`<SO_HIEU>`** . **[Điều 3]`<DIEU>`** . **[Khoản 2]`<KHOAN>`** . **[đ ) Trường hợp có chỉnh sửa các quy định nêu trong Mẫu **[hồ sơ mời thầu]`<GIAY_TO_HO_SO>`** thì tổ chức , cá nhân thực hiện việc lập , thẩm định , phê duyệt **[hồ sơ mời thầu]`<GIAY_TO_HO_SO>`** phải bảo đảm việc chỉnh sửa đó là phù hợp , khoa học , chặt chẽ hơn so với quy định nêu trong Mẫu **[hồ sơ mời thầu]`<GIAY_TO_HO_SO>`** và không trái với quy định của Hiệp định CPTPP. Trong tờ trình đề nghị phê duyệt **[hồ sơ mời thầu]`<GIAY_TO_HO_SO>`** phải nêu rõ các nội dung chỉnh sửa so]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[5:6]`)
- `[e1]` **09/2020/TT-BKHĐT** → `SO_HIEU` (span: `[7:8]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[0:4]`)
- `[e3]` **Điều 3** → `DIEU` (span: `[9:11]`)
- `[e4]` **Khoản 2** → `KHOAN` (span: `[12:14]`)
- `[e5]` **đ ) Trường hợp có chỉnh sửa các quy định nêu trong Mẫu hồ sơ mời thầu thì tổ chức , cá nhân thực hiện việc lập , thẩm định , phê duyệt hồ sơ mời thầu phải bảo đảm việc chỉnh sửa đó là phù hợp , khoa học , chặt chẽ hơn so với quy định nêu trong Mẫu hồ sơ mời thầu và không trái với quy định của Hiệp định CPTPP. Trong tờ trình đề nghị phê duyệt hồ sơ mời thầu phải nêu rõ các nội dung chỉnh sửa so** → `DIEM` (span: `[15:81]`)
- `[e6]` **hồ sơ mời thầu** → `GIAY_TO_HO_SO` (span: `[25:27]`) *(lồng trong `e5` (`DIEM`))*
- `[e7]` **hồ sơ mời thầu** → `GIAY_TO_HO_SO` (span: `[38:40]`) *(lồng trong `e5` (`DIEM`))*
- `[e8]` **hồ sơ mời thầu** → `GIAY_TO_HO_SO` (span: `[58:60]`) *(lồng trong `e5` (`DIEM`))*
- `[e9]` **hồ sơ mời thầu** → `GIAY_TO_HO_SO` (span: `[72:74]`) *(lồng trong `e5` (`DIEM`))*

**Quan hệ:**
- (`e1` 09/2020/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 09/2020/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 3 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 09/2020/TT-BKHĐT `[SO_HIEU]`)
- (`e4` Khoản 2 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 3 `[DIEU]`)
- (`e5` đ ) Trường hợp có chỉnh sửa các quy định nêu trong Mẫu hồ sơ mời thầu thì tổ chức , cá nhân thực hiện việc lập , thẩm định , phê duyệt hồ sơ mời thầu phải bảo đảm việc chỉnh sửa đó là phù hợp , khoa học , chặt chẽ hơn so với quy định nêu trong Mẫu hồ sơ mời thầu và không trái với quy định của Hiệp định CPTPP. Trong tờ trình đề nghị phê duyệt hồ sơ mời thầu phải nêu rõ các nội dung chỉnh sửa so `[DIEM]`) ==[ **THUOC_VE** ]==> (`e4` Khoản 2 `[KHOAN]`)


---

### Mẫu #09_2020_TT-BKHĐT_145176#body_standalone_33 (Loại: `body_standalone`)
> **[Điều 3]`<DIEU>`** . **[Khoản 2]`<KHOAN>`** . **[đ ) Trường hợp có chỉnh sửa các quy định nêu trong Mẫu **[hồ sơ mời thầu]`<GIAY_TO_HO_SO>`** thì tổ chức , cá nhân thực hiện việc lập , thẩm định , phê duyệt **[hồ sơ mời thầu]`<GIAY_TO_HO_SO>`** phải bảo đảm việc chỉnh sửa đó là phù hợp , khoa học , chặt chẽ hơn so với quy định nêu trong Mẫu **[hồ sơ mời thầu]`<GIAY_TO_HO_SO>`** và không trái với quy định của Hiệp định CPTPP. Trong tờ trình đề nghị phê duyệt **[hồ sơ mời thầu]`<GIAY_TO_HO_SO>`** phải nêu rõ các nội dung chỉnh sửa so]`<DIEM>`**

**Thực thể:**
- `[e0]` **Điều 3** → `DIEU` (span: `[0:2]`)
- `[e1]` **Khoản 2** → `KHOAN` (span: `[3:5]`)
- `[e2]` **đ ) Trường hợp có chỉnh sửa các quy định nêu trong Mẫu hồ sơ mời thầu thì tổ chức , cá nhân thực hiện việc lập , thẩm định , phê duyệt hồ sơ mời thầu phải bảo đảm việc chỉnh sửa đó là phù hợp , khoa học , chặt chẽ hơn so với quy định nêu trong Mẫu hồ sơ mời thầu và không trái với quy định của Hiệp định CPTPP. Trong tờ trình đề nghị phê duyệt hồ sơ mời thầu phải nêu rõ các nội dung chỉnh sửa so** → `DIEM` (span: `[6:72]`)
- `[e3]` **hồ sơ mời thầu** → `GIAY_TO_HO_SO` (span: `[16:18]`) *(lồng trong `e2` (`DIEM`))*
- `[e4]` **hồ sơ mời thầu** → `GIAY_TO_HO_SO` (span: `[29:31]`) *(lồng trong `e2` (`DIEM`))*
- `[e5]` **hồ sơ mời thầu** → `GIAY_TO_HO_SO` (span: `[49:51]`) *(lồng trong `e2` (`DIEM`))*
- `[e6]` **hồ sơ mời thầu** → `GIAY_TO_HO_SO` (span: `[63:65]`) *(lồng trong `e2` (`DIEM`))*

**Quan hệ:**
- (`e1` Khoản 2 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 3 `[DIEU]`)
- (`e2` đ ) Trường hợp có chỉnh sửa các quy định nêu trong Mẫu hồ sơ mời thầu thì tổ chức , cá nhân thực hiện việc lập , thẩm định , phê duyệt hồ sơ mời thầu phải bảo đảm việc chỉnh sửa đó là phù hợp , khoa học , chặt chẽ hơn so với quy định nêu trong Mẫu hồ sơ mời thầu và không trái với quy định của Hiệp định CPTPP. Trong tờ trình đề nghị phê duyệt hồ sơ mời thầu phải nêu rõ các nội dung chỉnh sửa so `[DIEM]`) ==[ **THUOC_VE** ]==> (`e1` Khoản 2 `[KHOAN]`)


---

### Mẫu #09_2020_TT-BKHĐT_145176#body_context_34 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[09/2020/TT-BKHĐT]`<SO_HIEU>`** ban hành **[ngày 27 tháng 11 năm 2020]`<NGAY_BAN_HANH>`** bởi **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** . **[Điều 3]`<DIEU>`** . **[3 . Đối với gói thầu mua sắm hàng hoá áp dụng hình thức chỉ định thầu , có thể tham khảo , chỉnh sửa các Mẫu **[hồ sơ mời thầu]`<GIAY_TO_HO_SO>`** để áp dụng cho phù hợp .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **09/2020/TT-BKHĐT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[11:15]`)
- `[e3]` **ngày 27 tháng 11 năm 2020** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 3** → `DIEU` (span: `[16:18]`)
- `[e5]` **3 . Đối với gói thầu mua sắm hàng hoá áp dụng hình thức chỉ định thầu , có thể tham khảo , chỉnh sửa các Mẫu hồ sơ mời thầu để áp dụng cho phù hợp .** → `KHOAN` (span: `[19:43]`)
- `[e6]` **hồ sơ mời thầu** → `GIAY_TO_HO_SO` (span: `[36:38]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 09/2020/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 09/2020/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 09/2020/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 27 tháng 11 năm 2020 `[NGAY_BAN_HANH]`)
- (`e4` Điều 3 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 09/2020/TT-BKHĐT `[SO_HIEU]`)
- (`e5` 3 . Đối với gói thầu mua sắm hàng hoá áp dụng hình thức chỉ định thầu , có thể tham khảo , chỉnh sửa các Mẫu hồ sơ mời thầu để áp dụng cho phù hợp . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 3 `[DIEU]`)


---

### Mẫu #09_2020_TT-BKHĐT_145176#body_context_35 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[09/2020/TT-BKHĐT]`<SO_HIEU>`** ban hành **[ngày 27 tháng 11 năm 2020]`<NGAY_BAN_HANH>`** bởi **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** . **[Điều 4 . **[Giấy phép bán hàng của nhà sản xuất]`<GIAY_TO_HO_SO>`**]`<DIEU>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **09/2020/TT-BKHĐT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[11:15]`)
- `[e3]` **ngày 27 tháng 11 năm 2020** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 4 . Giấy phép bán hàng của nhà sản xuất** → `DIEU` (span: `[16:25]`)
- `[e5]` **Giấy phép bán hàng của nhà sản xuất** → `GIAY_TO_HO_SO` (span: `[19:25]`) *(lồng trong `e4` (`DIEU`))*

**Quan hệ:**
- (`e1` 09/2020/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 09/2020/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 09/2020/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 27 tháng 11 năm 2020 `[NGAY_BAN_HANH]`)
- (`e4` Điều 4 . Giấy phép bán hàng của nhà sản xuất `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 09/2020/TT-BKHĐT `[SO_HIEU]`)


---

### Mẫu #09_2020_TT-BKHĐT_145176#body_context_36 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[09/2020/TT-BKHĐT]`<SO_HIEU>`** của **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** . **[Điều 4]`<DIEU>`** . **[1 . Đối với **[hàng hóa]`<TAI_SAN_VAT_CHAT>`** thông thường , thông dụng , sẵn có trên thị trường , đã được tiêu chuẩn hóa và được bảo hành theo quy định của nhà sản xuất thì không yêu cầu nhà thầu phải nộp Giấy phép hoặc **[Giấy ủy quyền]`<GIAY_TO_HO_SO>`** bán hàng của nhà sản xuất , đại lý phân phối hoặc **[Giấy chứng nhận quan hệ đối tác]`<GIAY_TO_HO_SO>`** hoặc tài liệu khác có giá trị tương đương ( sau đây gọi chung là **[Giấy phép bán hàng]`<GIAY_TO_HO_SO>`** ) .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **09/2020/TT-BKHĐT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[4:8]`)
- `[e3]` **Điều 4** → `DIEU` (span: `[9:11]`)
- `[e4]` **1 . Đối với hàng hóa thông thường , thông dụng , sẵn có trên thị trường , đã được tiêu chuẩn hóa và được bảo hành theo quy định của nhà sản xuất thì không yêu cầu nhà thầu phải nộp Giấy phép hoặc Giấy ủy quyền bán hàng của nhà sản xuất , đại lý phân phối hoặc Giấy chứng nhận quan hệ đối tác hoặc tài liệu khác có giá trị tương đương ( sau đây gọi chung là Giấy phép bán hàng ) .** → `KHOAN` (span: `[12:75]`)
- `[e5]` **Giấy phép bán hàng** → `GIAY_TO_HO_SO` (span: `[70:73]`) *(lồng trong `e4` (`KHOAN`))*
- `[e6]` **Giấy ủy quyền** → `GIAY_TO_HO_SO` (span: `[44:45]`) *(lồng trong `e4` (`KHOAN`))*
- `[e7]` **hàng hóa** → `TAI_SAN_VAT_CHAT` (span: `[15:16]`) *(lồng trong `e4` (`KHOAN`))*
- `[e8]` **Giấy chứng nhận quan hệ đối tác** → `GIAY_TO_HO_SO` (span: `[54:58]`) *(lồng trong `e4` (`KHOAN`))*

**Quan hệ:**
- (`e1` 09/2020/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 09/2020/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 4 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 09/2020/TT-BKHĐT `[SO_HIEU]`)
- (`e4` 1 . Đối với hàng hóa thông thường , thông dụng , sẵn có trên thị trường , đã được tiêu chuẩn hóa và được bảo hành theo quy định của nhà sản xuất thì không yêu cầu nhà thầu phải nộp Giấy phép hoặc Giấy ủy quyền bán hàng của nhà sản xuất , đại lý phân phối hoặc Giấy chứng nhận quan hệ đối tác hoặc tài liệu khác có giá trị tương đương ( sau đây gọi chung là Giấy phép bán hàng ) . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 4 `[DIEU]`)


---

### Mẫu #09_2020_TT-BKHĐT_145176#body_standalone_37 (Loại: `body_standalone`)
> **[Điều 4]`<DIEU>`** . **[1 . Đối với **[hàng hóa]`<TAI_SAN_VAT_CHAT>`** thông thường , thông dụng , sẵn có trên thị trường , đã được tiêu chuẩn hóa và được bảo hành theo quy định của nhà sản xuất thì không yêu cầu nhà thầu phải nộp Giấy phép hoặc **[Giấy ủy quyền]`<GIAY_TO_HO_SO>`** bán hàng của nhà sản xuất , đại lý phân phối hoặc **[Giấy chứng nhận quan hệ đối tác]`<GIAY_TO_HO_SO>`** hoặc tài liệu khác có giá trị tương đương ( sau đây gọi chung là **[Giấy phép bán hàng]`<GIAY_TO_HO_SO>`** ) .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 4** → `DIEU` (span: `[0:2]`)
- `[e1]` **1 . Đối với hàng hóa thông thường , thông dụng , sẵn có trên thị trường , đã được tiêu chuẩn hóa và được bảo hành theo quy định của nhà sản xuất thì không yêu cầu nhà thầu phải nộp Giấy phép hoặc Giấy ủy quyền bán hàng của nhà sản xuất , đại lý phân phối hoặc Giấy chứng nhận quan hệ đối tác hoặc tài liệu khác có giá trị tương đương ( sau đây gọi chung là Giấy phép bán hàng ) .** → `KHOAN` (span: `[3:66]`)
- `[e2]` **Giấy phép bán hàng** → `GIAY_TO_HO_SO` (span: `[61:64]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **Giấy ủy quyền** → `GIAY_TO_HO_SO` (span: `[35:36]`) *(lồng trong `e1` (`KHOAN`))*
- `[e4]` **hàng hóa** → `TAI_SAN_VAT_CHAT` (span: `[6:7]`) *(lồng trong `e1` (`KHOAN`))*
- `[e5]` **Giấy chứng nhận quan hệ đối tác** → `GIAY_TO_HO_SO` (span: `[45:49]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 1 . Đối với hàng hóa thông thường , thông dụng , sẵn có trên thị trường , đã được tiêu chuẩn hóa và được bảo hành theo quy định của nhà sản xuất thì không yêu cầu nhà thầu phải nộp Giấy phép hoặc Giấy ủy quyền bán hàng của nhà sản xuất , đại lý phân phối hoặc Giấy chứng nhận quan hệ đối tác hoặc tài liệu khác có giá trị tương đương ( sau đây gọi chung là Giấy phép bán hàng ) . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 4 `[DIEU]`)


---

### Mẫu #09_2020_TT-BKHĐT_145176#body_context_38 (Loại: `body_context`)
> **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[09/2020/TT-BKHĐT]`<SO_HIEU>`** . **[Điều 4]`<DIEU>`** . **[2 . Đối với **[hàng hóa]`<TAI_SAN_VAT_CHAT>`** đặc thù , phức tạp cần sự khẳng định của nhà sản xuất , nhà cung cấp để đảm bảo tính khả thi trong việc cung cấp **[hàng hóa]`<TAI_SAN_VAT_CHAT>`** khi nhà thầu trúng thầu và cần gắn với trách nhiệm của nhà sản xuất trong việc cung cấp các dịch vụ sau bán hàng như lắp đặt , bảo trì , đào tạo và các dịch vụ liên quan khác , trong **[hồ sơ mời thầu]`<GIAY_TO_HO_SO>`** có thể yêu cầu nhà thầu tham dự thầu phải cung **[cấp **[Giấy phép bán hàng]`<GIAY_TO_HO_SO>`**]`<NGHIA_VU_QUYEN>`** .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[5:6]`)
- `[e1]` **09/2020/TT-BKHĐT** → `SO_HIEU` (span: `[7:8]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[0:4]`)
- `[e3]` **Điều 4** → `DIEU` (span: `[9:11]`)
- `[e4]` **2 . Đối với hàng hóa đặc thù , phức tạp cần sự khẳng định của nhà sản xuất , nhà cung cấp để đảm bảo tính khả thi trong việc cung cấp hàng hóa khi nhà thầu trúng thầu và cần gắn với trách nhiệm của nhà sản xuất trong việc cung cấp các dịch vụ sau bán hàng như lắp đặt , bảo trì , đào tạo và các dịch vụ liên quan khác , trong hồ sơ mời thầu có thể yêu cầu nhà thầu tham dự thầu phải cung cấp Giấy phép bán hàng .** → `KHOAN` (span: `[12:80]`)
- `[e5]` **cấp Giấy phép bán hàng** → `NGHIA_VU_QUYEN` (span: `[75:79]`) *(lồng trong `e4` (`KHOAN`))*
- `[e6]` **Giấy phép bán hàng** → `GIAY_TO_HO_SO` (span: `[76:79]`) *(lồng trong `e4` (`KHOAN`), `e5` (`NGHIA_VU_QUYEN`))*
- `[e7]` **hồ sơ mời thầu** → `GIAY_TO_HO_SO` (span: `[67:69]`) *(lồng trong `e4` (`KHOAN`))*
- `[e8]` **hàng hóa** → `TAI_SAN_VAT_CHAT` (span: `[15:16]`) *(lồng trong `e4` (`KHOAN`))*
- `[e9]` **hàng hóa** → `TAI_SAN_VAT_CHAT` (span: `[35:36]`) *(lồng trong `e4` (`KHOAN`))*

**Quan hệ:**
- (`e1` 09/2020/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 09/2020/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 4 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 09/2020/TT-BKHĐT `[SO_HIEU]`)
- (`e4` 2 . Đối với hàng hóa đặc thù , phức tạp cần sự khẳng định của nhà sản xuất , nhà cung cấp để đảm bảo tính khả thi trong việc cung cấp hàng hóa khi nhà thầu trúng thầu và cần gắn với trách nhiệm của nhà sản xuất trong việc cung cấp các dịch vụ sau bán hàng như lắp đặt , bảo trì , đào tạo và các dịch vụ liên quan khác , trong hồ sơ mời thầu có thể yêu cầu nhà thầu tham dự thầu phải cung cấp Giấy phép bán hàng . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 4 `[DIEU]`)
- (`e5` cấp Giấy phép bán hàng `[NGHIA_VU_QUYEN]`) ==[ **TAC_DONG_DOI_TUONG** ]==> (`e6` Giấy phép bán hàng `[GIAY_TO_HO_SO]`) *(Quan hệ lồng nhau)*
- (`e5` cấp Giấy phép bán hàng `[NGHIA_VU_QUYEN]`) ==[ **TAC_DONG_DOI_TUONG** ]==> (`e7` hồ sơ mời thầu `[GIAY_TO_HO_SO]`)
- (`e5` cấp Giấy phép bán hàng `[NGHIA_VU_QUYEN]`) ==[ **TAC_DONG_DOI_TUONG** ]==> (`e8` hàng hóa `[TAI_SAN_VAT_CHAT]`)
- (`e5` cấp Giấy phép bán hàng `[NGHIA_VU_QUYEN]`) ==[ **TAC_DONG_DOI_TUONG** ]==> (`e9` hàng hóa `[TAI_SAN_VAT_CHAT]`)


---

### Mẫu #09_2020_TT-BKHĐT_145176#body_standalone_39 (Loại: `body_standalone`)
> **[Điều 4]`<DIEU>`** . **[2 . Đối với **[hàng hóa]`<TAI_SAN_VAT_CHAT>`** đặc thù , phức tạp cần sự khẳng định của nhà sản xuất , nhà cung cấp để đảm bảo tính khả thi trong việc cung cấp **[hàng hóa]`<TAI_SAN_VAT_CHAT>`** khi nhà thầu trúng thầu và cần gắn với trách nhiệm của nhà sản xuất trong việc cung cấp các dịch vụ sau bán hàng như lắp đặt , bảo trì , đào tạo và các dịch vụ liên quan khác , trong **[hồ sơ mời thầu]`<GIAY_TO_HO_SO>`** có thể yêu cầu nhà thầu tham dự thầu phải cung **[cấp **[Giấy phép bán hàng]`<GIAY_TO_HO_SO>`**]`<NGHIA_VU_QUYEN>`** .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 4** → `DIEU` (span: `[0:2]`)
- `[e1]` **2 . Đối với hàng hóa đặc thù , phức tạp cần sự khẳng định của nhà sản xuất , nhà cung cấp để đảm bảo tính khả thi trong việc cung cấp hàng hóa khi nhà thầu trúng thầu và cần gắn với trách nhiệm của nhà sản xuất trong việc cung cấp các dịch vụ sau bán hàng như lắp đặt , bảo trì , đào tạo và các dịch vụ liên quan khác , trong hồ sơ mời thầu có thể yêu cầu nhà thầu tham dự thầu phải cung cấp Giấy phép bán hàng .** → `KHOAN` (span: `[3:71]`)
- `[e2]` **cấp Giấy phép bán hàng** → `NGHIA_VU_QUYEN` (span: `[66:70]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **Giấy phép bán hàng** → `GIAY_TO_HO_SO` (span: `[67:70]`) *(lồng trong `e1` (`KHOAN`), `e2` (`NGHIA_VU_QUYEN`))*
- `[e4]` **hồ sơ mời thầu** → `GIAY_TO_HO_SO` (span: `[58:60]`) *(lồng trong `e1` (`KHOAN`))*
- `[e5]` **hàng hóa** → `TAI_SAN_VAT_CHAT` (span: `[6:7]`) *(lồng trong `e1` (`KHOAN`))*
- `[e6]` **hàng hóa** → `TAI_SAN_VAT_CHAT` (span: `[26:27]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 2 . Đối với hàng hóa đặc thù , phức tạp cần sự khẳng định của nhà sản xuất , nhà cung cấp để đảm bảo tính khả thi trong việc cung cấp hàng hóa khi nhà thầu trúng thầu và cần gắn với trách nhiệm của nhà sản xuất trong việc cung cấp các dịch vụ sau bán hàng như lắp đặt , bảo trì , đào tạo và các dịch vụ liên quan khác , trong hồ sơ mời thầu có thể yêu cầu nhà thầu tham dự thầu phải cung cấp Giấy phép bán hàng . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 4 `[DIEU]`)
- (`e2` cấp Giấy phép bán hàng `[NGHIA_VU_QUYEN]`) ==[ **TAC_DONG_DOI_TUONG** ]==> (`e3` Giấy phép bán hàng `[GIAY_TO_HO_SO]`) *(Quan hệ lồng nhau)*
- (`e2` cấp Giấy phép bán hàng `[NGHIA_VU_QUYEN]`) ==[ **TAC_DONG_DOI_TUONG** ]==> (`e4` hồ sơ mời thầu `[GIAY_TO_HO_SO]`)
- (`e2` cấp Giấy phép bán hàng `[NGHIA_VU_QUYEN]`) ==[ **TAC_DONG_DOI_TUONG** ]==> (`e5` hàng hóa `[TAI_SAN_VAT_CHAT]`)
- (`e2` cấp Giấy phép bán hàng `[NGHIA_VU_QUYEN]`) ==[ **TAC_DONG_DOI_TUONG** ]==> (`e6` hàng hóa `[TAI_SAN_VAT_CHAT]`)


---

### Mẫu #09_2020_TT-BKHĐT_145176#body_context_40 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[09/2020/TT-BKHĐT]`<SO_HIEU>`** ban hành **[ngày 27 tháng 11 năm 2020]`<NGAY_BAN_HANH>`** bởi **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** . **[Điều 4]`<DIEU>`** . **[3 . Trường hợp nội dung **[Giấy phép bán hàng]`<GIAY_TO_HO_SO>`** chưa đáp ứng đầy đủ các điều kiện theo yêu cầu của **[hồ sơ mời thầu]`<GIAY_TO_HO_SO>`** thì bên mời thầu phải yêu cầu nhà thầu làm rõ về các nội dung này để có đầy đủ thông tin phục vụ việc trao hợp đồng , bao gồm cho phép nhà thầu thay thế hoặc bổ sung thông tin về **[Giấy phép bán hàng]`<GIAY_TO_HO_SO>`** .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **09/2020/TT-BKHĐT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[11:15]`)
- `[e3]` **ngày 27 tháng 11 năm 2020** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 4** → `DIEU` (span: `[16:18]`)
- `[e5]` **3 . Trường hợp nội dung Giấy phép bán hàng chưa đáp ứng đầy đủ các điều kiện theo yêu cầu của hồ sơ mời thầu thì bên mời thầu phải yêu cầu nhà thầu làm rõ về các nội dung này để có đầy đủ thông tin phục vụ việc trao hợp đồng , bao gồm cho phép nhà thầu thay thế hoặc bổ sung thông tin về Giấy phép bán hàng .** → `KHOAN` (span: `[19:69]`)
- `[e6]` **Giấy phép bán hàng** → `GIAY_TO_HO_SO` (span: `[23:26]`) *(lồng trong `e5` (`KHOAN`))*
- `[e7]` **Giấy phép bán hàng** → `GIAY_TO_HO_SO` (span: `[65:68]`) *(lồng trong `e5` (`KHOAN`))*
- `[e8]` **hồ sơ mời thầu** → `GIAY_TO_HO_SO` (span: `[34:36]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 09/2020/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 09/2020/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 09/2020/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 27 tháng 11 năm 2020 `[NGAY_BAN_HANH]`)
- (`e4` Điều 4 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 09/2020/TT-BKHĐT `[SO_HIEU]`)
- (`e5` 3 . Trường hợp nội dung Giấy phép bán hàng chưa đáp ứng đầy đủ các điều kiện theo yêu cầu của hồ sơ mời thầu thì bên mời thầu phải yêu cầu nhà thầu làm rõ về các nội dung này để có đầy đủ thông tin phục vụ việc trao hợp đồng , bao gồm cho phép nhà thầu thay thế hoặc bổ sung thông tin về Giấy phép bán hàng . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 4 `[DIEU]`)


---

### Mẫu #09_2020_TT-BKHĐT_145176#body_standalone_41 (Loại: `body_standalone`)
> **[Điều 4]`<DIEU>`** . **[3 . Trường hợp nội dung **[Giấy phép bán hàng]`<GIAY_TO_HO_SO>`** chưa đáp ứng đầy đủ các điều kiện theo yêu cầu của **[hồ sơ mời thầu]`<GIAY_TO_HO_SO>`** thì bên mời thầu phải yêu cầu nhà thầu làm rõ về các nội dung này để có đầy đủ thông tin phục vụ việc trao hợp đồng , bao gồm cho phép nhà thầu thay thế hoặc bổ sung thông tin về **[Giấy phép bán hàng]`<GIAY_TO_HO_SO>`** .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 4** → `DIEU` (span: `[0:2]`)
- `[e1]` **3 . Trường hợp nội dung Giấy phép bán hàng chưa đáp ứng đầy đủ các điều kiện theo yêu cầu của hồ sơ mời thầu thì bên mời thầu phải yêu cầu nhà thầu làm rõ về các nội dung này để có đầy đủ thông tin phục vụ việc trao hợp đồng , bao gồm cho phép nhà thầu thay thế hoặc bổ sung thông tin về Giấy phép bán hàng .** → `KHOAN` (span: `[3:53]`)
- `[e2]` **Giấy phép bán hàng** → `GIAY_TO_HO_SO` (span: `[7:10]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **Giấy phép bán hàng** → `GIAY_TO_HO_SO` (span: `[49:52]`) *(lồng trong `e1` (`KHOAN`))*
- `[e4]` **hồ sơ mời thầu** → `GIAY_TO_HO_SO` (span: `[18:20]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 3 . Trường hợp nội dung Giấy phép bán hàng chưa đáp ứng đầy đủ các điều kiện theo yêu cầu của hồ sơ mời thầu thì bên mời thầu phải yêu cầu nhà thầu làm rõ về các nội dung này để có đầy đủ thông tin phục vụ việc trao hợp đồng , bao gồm cho phép nhà thầu thay thế hoặc bổ sung thông tin về Giấy phép bán hàng . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 4 `[DIEU]`)


---

### Mẫu #09_2020_TT-BKHĐT_145176#body_context_42 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[09/2020/TT-BKHĐT]`<SO_HIEU>`** của **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** . **[Điều 4]`<DIEU>`** . **[4 . Trường hợp các nhà sản xuất , đại lý phân phối trong lãnh thổ Việt Nam cố tình không cung cấp cho nhà thầu **[Giấy phép bán hàng]`<GIAY_TO_HO_SO>`** mà không có lý do chính đáng , không tuân thủ các quy định của pháp luật về thương mại và cạnh tranh , dẫn đến tạo lợi thế hoặc tạo sự độc quyền cho nhà thầu khác thì nhà thầu phản ánh đến **[Bộ Công Thương]`<CO_QUAN_THAM_QUYEN>`** để kịp thời xử lý .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **09/2020/TT-BKHĐT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[4:8]`)
- `[e3]` **Điều 4** → `DIEU` (span: `[9:11]`)
- `[e4]` **4 . Trường hợp các nhà sản xuất , đại lý phân phối trong lãnh thổ Việt Nam cố tình không cung cấp cho nhà thầu Giấy phép bán hàng mà không có lý do chính đáng , không tuân thủ các quy định của pháp luật về thương mại và cạnh tranh , dẫn đến tạo lợi thế hoặc tạo sự độc quyền cho nhà thầu khác thì nhà thầu phản ánh đến Bộ Công Thương để kịp thời xử lý .** → `KHOAN` (span: `[12:69]`)
- `[e5]` **Giấy phép bán hàng** → `GIAY_TO_HO_SO` (span: `[29:32]`) *(lồng trong `e4` (`KHOAN`))*
- `[e6]` **Bộ Công Thương** → `CO_QUAN_THAM_QUYEN` (span: `[63:65]`) *(lồng trong `e4` (`KHOAN`))*

**Quan hệ:**
- (`e1` 09/2020/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 09/2020/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 4 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 09/2020/TT-BKHĐT `[SO_HIEU]`)
- (`e4` 4 . Trường hợp các nhà sản xuất , đại lý phân phối trong lãnh thổ Việt Nam cố tình không cung cấp cho nhà thầu Giấy phép bán hàng mà không có lý do chính đáng , không tuân thủ các quy định của pháp luật về thương mại và cạnh tranh , dẫn đến tạo lợi thế hoặc tạo sự độc quyền cho nhà thầu khác thì nhà thầu phản ánh đến Bộ Công Thương để kịp thời xử lý . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 4 `[DIEU]`)


---

### Mẫu #09_2020_TT-BKHĐT_145176#body_standalone_43 (Loại: `body_standalone`)
> **[Điều 4]`<DIEU>`** . **[4 . Trường hợp các nhà sản xuất , đại lý phân phối trong lãnh thổ Việt Nam cố tình không cung cấp cho nhà thầu **[Giấy phép bán hàng]`<GIAY_TO_HO_SO>`** mà không có lý do chính đáng , không tuân thủ các quy định của pháp luật về thương mại và cạnh tranh , dẫn đến tạo lợi thế hoặc tạo sự độc quyền cho nhà thầu khác thì nhà thầu phản ánh đến **[Bộ Công Thương]`<CO_QUAN_THAM_QUYEN>`** để kịp thời xử lý .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 4** → `DIEU` (span: `[0:2]`)
- `[e1]` **4 . Trường hợp các nhà sản xuất , đại lý phân phối trong lãnh thổ Việt Nam cố tình không cung cấp cho nhà thầu Giấy phép bán hàng mà không có lý do chính đáng , không tuân thủ các quy định của pháp luật về thương mại và cạnh tranh , dẫn đến tạo lợi thế hoặc tạo sự độc quyền cho nhà thầu khác thì nhà thầu phản ánh đến Bộ Công Thương để kịp thời xử lý .** → `KHOAN` (span: `[3:60]`)
- `[e2]` **Giấy phép bán hàng** → `GIAY_TO_HO_SO` (span: `[20:23]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **Bộ Công Thương** → `CO_QUAN_THAM_QUYEN` (span: `[54:56]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 4 . Trường hợp các nhà sản xuất , đại lý phân phối trong lãnh thổ Việt Nam cố tình không cung cấp cho nhà thầu Giấy phép bán hàng mà không có lý do chính đáng , không tuân thủ các quy định của pháp luật về thương mại và cạnh tranh , dẫn đến tạo lợi thế hoặc tạo sự độc quyền cho nhà thầu khác thì nhà thầu phản ánh đến Bộ Công Thương để kịp thời xử lý . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 4 `[DIEU]`)


---

### Mẫu #09_2020_TT-BKHĐT_145176#body_context_44 (Loại: `body_context`)
> **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[09/2020/TT-BKHĐT]`<SO_HIEU>`** . **[Điều 5 . Yêu cầu về cung cấp hàng mẫu]`<DIEU>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[5:6]`)
- `[e1]` **09/2020/TT-BKHĐT** → `SO_HIEU` (span: `[7:8]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[0:4]`)
- `[e3]` **Điều 5 . Yêu cầu về cung cấp hàng mẫu** → `DIEU` (span: `[9:17]`)

**Quan hệ:**
- (`e1` 09/2020/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 09/2020/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 5 . Yêu cầu về cung cấp hàng mẫu `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 09/2020/TT-BKHĐT `[SO_HIEU]`)


---

### Mẫu #09_2020_TT-BKHĐT_145176#body_context_45 (Loại: `body_context`)
> **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[09/2020/TT-BKHĐT]`<SO_HIEU>`** . **[Điều 5]`<DIEU>`** . **[1 . Đối với **[hàng hóa]`<TAI_SAN_VAT_CHAT>`** thông thường , thông dụng , sẵn có trên thị trường , đã được tiêu chuẩn hóa thì không yêu cầu nhà thầu cung cấp hàng mẫu .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[5:6]`)
- `[e1]` **09/2020/TT-BKHĐT** → `SO_HIEU` (span: `[7:8]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[0:4]`)
- `[e3]` **Điều 5** → `DIEU` (span: `[9:11]`)
- `[e4]` **1 . Đối với hàng hóa thông thường , thông dụng , sẵn có trên thị trường , đã được tiêu chuẩn hóa thì không yêu cầu nhà thầu cung cấp hàng mẫu .** → `KHOAN` (span: `[12:36]`)
- `[e5]` **hàng hóa** → `TAI_SAN_VAT_CHAT` (span: `[15:16]`) *(lồng trong `e4` (`KHOAN`))*

**Quan hệ:**
- (`e1` 09/2020/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 09/2020/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 5 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 09/2020/TT-BKHĐT `[SO_HIEU]`)
- (`e4` 1 . Đối với hàng hóa thông thường , thông dụng , sẵn có trên thị trường , đã được tiêu chuẩn hóa thì không yêu cầu nhà thầu cung cấp hàng mẫu . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 5 `[DIEU]`)


---

### Mẫu #09_2020_TT-BKHĐT_145176#body_standalone_46 (Loại: `body_standalone`)
> **[Điều 5]`<DIEU>`** . **[1 . Đối với **[hàng hóa]`<TAI_SAN_VAT_CHAT>`** thông thường , thông dụng , sẵn có trên thị trường , đã được tiêu chuẩn hóa thì không yêu cầu nhà thầu cung cấp hàng mẫu .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 5** → `DIEU` (span: `[0:2]`)
- `[e1]` **1 . Đối với hàng hóa thông thường , thông dụng , sẵn có trên thị trường , đã được tiêu chuẩn hóa thì không yêu cầu nhà thầu cung cấp hàng mẫu .** → `KHOAN` (span: `[3:27]`)
- `[e2]` **hàng hóa** → `TAI_SAN_VAT_CHAT` (span: `[6:7]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 1 . Đối với hàng hóa thông thường , thông dụng , sẵn có trên thị trường , đã được tiêu chuẩn hóa thì không yêu cầu nhà thầu cung cấp hàng mẫu . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 5 `[DIEU]`)


---

### Mẫu #09_2020_TT-BKHĐT_145176#body_context_47 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[09/2020/TT-BKHĐT]`<SO_HIEU>`** ban hành **[ngày 27 tháng 11 năm 2020]`<NGAY_BAN_HANH>`** bởi **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** . **[Điều 5]`<DIEU>`** . **[2 . Trường hợp **[hàng hóa]`<TAI_SAN_VAT_CHAT>`** của gói thầu là đặc thù , phức tạp , **[chủ đầu tư]`<CHU_THE_CA_NHAN>`** , bên mời thầu không thể xác định được cụ thể hình dáng , mẫu mã của **[hàng hóa]`<TAI_SAN_VAT_CHAT>`** , cần chế tạo , sản xuất đơn lẻ , riêng biệt thì có thể yêu cầu nhà thầu cung cấp hàng mẫu để chứng minh thông số kỹ thuật của **[hàng hóa]`<TAI_SAN_VAT_CHAT>`** . Trường hợp yêu cầu nhà thầu cung cấp hàng mẫu , trong tờ trình đề nghị phê duyệt **[hồ sơ mời thầu]`<GIAY_TO_HO_SO>`** phải nêu rõ lý do để chủ đầu]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **09/2020/TT-BKHĐT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[11:15]`)
- `[e3]` **ngày 27 tháng 11 năm 2020** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 5** → `DIEU` (span: `[16:18]`)
- `[e5]` **2 . Trường hợp hàng hóa của gói thầu là đặc thù , phức tạp , chủ đầu tư , bên mời thầu không thể xác định được cụ thể hình dáng , mẫu mã của hàng hóa , cần chế tạo , sản xuất đơn lẻ , riêng biệt thì có thể yêu cầu nhà thầu cung cấp hàng mẫu để chứng minh thông số kỹ thuật của hàng hóa . Trường hợp yêu cầu nhà thầu cung cấp hàng mẫu , trong tờ trình đề nghị phê duyệt hồ sơ mời thầu phải nêu rõ lý do để chủ đầu** → `KHOAN` (span: `[19:86]`)
- `[e6]` **hồ sơ mời thầu** → `GIAY_TO_HO_SO` (span: `[77:79]`) *(lồng trong `e5` (`KHOAN`))*
- `[e7]` **chủ đầu tư** → `CHU_THE_CA_NHAN` (span: `[30:32]`) *(lồng trong `e5` (`KHOAN`))*
- `[e8]` **hàng hóa** → `TAI_SAN_VAT_CHAT` (span: `[22:23]`) *(lồng trong `e5` (`KHOAN`))*
- `[e9]` **hàng hóa** → `TAI_SAN_VAT_CHAT` (span: `[43:44]`) *(lồng trong `e5` (`KHOAN`))*
- `[e10]` **hàng hóa** → `TAI_SAN_VAT_CHAT` (span: `[64:65]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 09/2020/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 09/2020/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 09/2020/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 27 tháng 11 năm 2020 `[NGAY_BAN_HANH]`)
- (`e4` Điều 5 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 09/2020/TT-BKHĐT `[SO_HIEU]`)
- (`e5` 2 . Trường hợp hàng hóa của gói thầu là đặc thù , phức tạp , chủ đầu tư , bên mời thầu không thể xác định được cụ thể hình dáng , mẫu mã của hàng hóa , cần chế tạo , sản xuất đơn lẻ , riêng biệt thì có thể yêu cầu nhà thầu cung cấp hàng mẫu để chứng minh thông số kỹ thuật của hàng hóa . Trường hợp yêu cầu nhà thầu cung cấp hàng mẫu , trong tờ trình đề nghị phê duyệt hồ sơ mời thầu phải nêu rõ lý do để chủ đầu `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 5 `[DIEU]`)


---

### Mẫu #09_2020_TT-BKHĐT_145176#body_standalone_48 (Loại: `body_standalone`)
> **[Điều 5]`<DIEU>`** . **[2 . Trường hợp **[hàng hóa]`<TAI_SAN_VAT_CHAT>`** của gói thầu là đặc thù , phức tạp , **[chủ đầu tư]`<CHU_THE_CA_NHAN>`** , bên mời thầu không thể xác định được cụ thể hình dáng , mẫu mã của **[hàng hóa]`<TAI_SAN_VAT_CHAT>`** , cần chế tạo , sản xuất đơn lẻ , riêng biệt thì có thể yêu cầu nhà thầu cung cấp hàng mẫu để chứng minh thông số kỹ thuật của **[hàng hóa]`<TAI_SAN_VAT_CHAT>`** . Trường hợp yêu cầu nhà thầu cung cấp hàng mẫu , trong tờ trình đề nghị phê duyệt **[hồ sơ mời thầu]`<GIAY_TO_HO_SO>`** phải nêu rõ lý do để chủ đầu]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 5** → `DIEU` (span: `[0:2]`)
- `[e1]` **2 . Trường hợp hàng hóa của gói thầu là đặc thù , phức tạp , chủ đầu tư , bên mời thầu không thể xác định được cụ thể hình dáng , mẫu mã của hàng hóa , cần chế tạo , sản xuất đơn lẻ , riêng biệt thì có thể yêu cầu nhà thầu cung cấp hàng mẫu để chứng minh thông số kỹ thuật của hàng hóa . Trường hợp yêu cầu nhà thầu cung cấp hàng mẫu , trong tờ trình đề nghị phê duyệt hồ sơ mời thầu phải nêu rõ lý do để chủ đầu** → `KHOAN` (span: `[3:70]`)
- `[e2]` **hồ sơ mời thầu** → `GIAY_TO_HO_SO` (span: `[61:63]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **chủ đầu tư** → `CHU_THE_CA_NHAN` (span: `[14:16]`) *(lồng trong `e1` (`KHOAN`))*
- `[e4]` **hàng hóa** → `TAI_SAN_VAT_CHAT` (span: `[6:7]`) *(lồng trong `e1` (`KHOAN`))*
- `[e5]` **hàng hóa** → `TAI_SAN_VAT_CHAT` (span: `[27:28]`) *(lồng trong `e1` (`KHOAN`))*
- `[e6]` **hàng hóa** → `TAI_SAN_VAT_CHAT` (span: `[48:49]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 2 . Trường hợp hàng hóa của gói thầu là đặc thù , phức tạp , chủ đầu tư , bên mời thầu không thể xác định được cụ thể hình dáng , mẫu mã của hàng hóa , cần chế tạo , sản xuất đơn lẻ , riêng biệt thì có thể yêu cầu nhà thầu cung cấp hàng mẫu để chứng minh thông số kỹ thuật của hàng hóa . Trường hợp yêu cầu nhà thầu cung cấp hàng mẫu , trong tờ trình đề nghị phê duyệt hồ sơ mời thầu phải nêu rõ lý do để chủ đầu `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 5 `[DIEU]`)


---

### Mẫu #09_2020_TT-BKHĐT_145176#body_context_49 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[09/2020/TT-BKHĐT]`<SO_HIEU>`** của **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** . **[Điều 5]`<DIEU>`** . **[3 . Trường hợp **[hồ sơ mời thầu]`<GIAY_TO_HO_SO>`** có yêu cầu cung cấp hàng mẫu , nhà có thể nộp bổ sung hàng mẫu sau thời điểm đóng thầu .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **09/2020/TT-BKHĐT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[4:8]`)
- `[e3]` **Điều 5** → `DIEU` (span: `[9:11]`)
- `[e4]` **3 . Trường hợp hồ sơ mời thầu có yêu cầu cung cấp hàng mẫu , nhà có thể nộp bổ sung hàng mẫu sau thời điểm đóng thầu .** → `KHOAN` (span: `[12:34]`)
- `[e5]` **hồ sơ mời thầu** → `GIAY_TO_HO_SO` (span: `[15:17]`) *(lồng trong `e4` (`KHOAN`))*

**Quan hệ:**
- (`e1` 09/2020/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 09/2020/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 5 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 09/2020/TT-BKHĐT `[SO_HIEU]`)
- (`e4` 3 . Trường hợp hồ sơ mời thầu có yêu cầu cung cấp hàng mẫu , nhà có thể nộp bổ sung hàng mẫu sau thời điểm đóng thầu . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 5 `[DIEU]`)


---

### Mẫu #09_2020_TT-BKHĐT_145176#body_context_50 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[09/2020/TT-BKHĐT]`<SO_HIEU>`** ban hành **[ngày 27 tháng 11 năm 2020]`<NGAY_BAN_HANH>`** bởi **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** . **[Điều 6 . Yêu cầu về huy động nhân sự thực hiện gói thầu]`<DIEU>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **09/2020/TT-BKHĐT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[11:15]`)
- `[e3]` **ngày 27 tháng 11 năm 2020** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 6 . Yêu cầu về huy động nhân sự thực hiện gói thầu** → `DIEU` (span: `[16:25]`)

**Quan hệ:**
- (`e1` 09/2020/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 09/2020/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 09/2020/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 27 tháng 11 năm 2020 `[NGAY_BAN_HANH]`)
- (`e4` Điều 6 . Yêu cầu về huy động nhân sự thực hiện gói thầu `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 09/2020/TT-BKHĐT `[SO_HIEU]`)


---

### Mẫu #09_2020_TT-BKHĐT_145176#body_context_51 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[09/2020/TT-BKHĐT]`<SO_HIEU>`** ban hành **[ngày 27 tháng 11 năm 2020]`<NGAY_BAN_HANH>`** bởi **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** . **[Điều 6]`<DIEU>`** . **[1 . Đối với phần công việc cung cấp **[hàng hóa]`<TAI_SAN_VAT_CHAT>`** , **[hồ sơ mời thầu]`<GIAY_TO_HO_SO>`** không được đưa ra yêu cầu về huy động nhân sự chủ chốt .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **09/2020/TT-BKHĐT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[11:15]`)
- `[e3]` **ngày 27 tháng 11 năm 2020** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 6** → `DIEU` (span: `[16:18]`)
- `[e5]` **1 . Đối với phần công việc cung cấp hàng hóa , hồ sơ mời thầu không được đưa ra yêu cầu về huy động nhân sự chủ chốt .** → `KHOAN` (span: `[19:39]`)
- `[e6]` **hồ sơ mời thầu** → `GIAY_TO_HO_SO` (span: `[27:29]`) *(lồng trong `e5` (`KHOAN`))*
- `[e7]` **hàng hóa** → `TAI_SAN_VAT_CHAT` (span: `[25:26]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 09/2020/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 09/2020/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 09/2020/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 27 tháng 11 năm 2020 `[NGAY_BAN_HANH]`)
- (`e4` Điều 6 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 09/2020/TT-BKHĐT `[SO_HIEU]`)
- (`e5` 1 . Đối với phần công việc cung cấp hàng hóa , hồ sơ mời thầu không được đưa ra yêu cầu về huy động nhân sự chủ chốt . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 6 `[DIEU]`)


---

### Mẫu #09_2020_TT-BKHĐT_145176#body_standalone_52 (Loại: `body_standalone`)
> **[Điều 6]`<DIEU>`** . **[1 . Đối với phần công việc cung cấp **[hàng hóa]`<TAI_SAN_VAT_CHAT>`** , **[hồ sơ mời thầu]`<GIAY_TO_HO_SO>`** không được đưa ra yêu cầu về huy động nhân sự chủ chốt .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 6** → `DIEU` (span: `[0:2]`)
- `[e1]` **1 . Đối với phần công việc cung cấp hàng hóa , hồ sơ mời thầu không được đưa ra yêu cầu về huy động nhân sự chủ chốt .** → `KHOAN` (span: `[3:23]`)
- `[e2]` **hồ sơ mời thầu** → `GIAY_TO_HO_SO` (span: `[11:13]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **hàng hóa** → `TAI_SAN_VAT_CHAT` (span: `[9:10]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 1 . Đối với phần công việc cung cấp hàng hóa , hồ sơ mời thầu không được đưa ra yêu cầu về huy động nhân sự chủ chốt . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 6 `[DIEU]`)


---

### Mẫu #09_2020_TT-BKHĐT_145176#body_context_53 (Loại: `body_context`)
> **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[09/2020/TT-BKHĐT]`<SO_HIEU>`** . **[Điều 6]`<DIEU>`** . **[2 . Đối với **[hàng hóa]`<TAI_SAN_VAT_CHAT>`** thông dụng , sẵn có trên thị trường , không đòi hỏi nhân sự thực hiện dịch vụ liên quan phải có trình độ cao thì không yêu cầu về nhân sự chủ chốt . Trường hợp các dịch vụ liên quan có yếu tố đặc thù , phức tạp cần thiết phải do nhân sự có hiểu biết , nhiều kinh nghiệm đảm nhận thì có thể đưa ra yêu cầu về huy động nhân sự chủ chốt để thực hiện các công việc đặc thù , phức tạp này . Trường hợp]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[5:6]`)
- `[e1]` **09/2020/TT-BKHĐT** → `SO_HIEU` (span: `[7:8]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[0:4]`)
- `[e3]` **Điều 6** → `DIEU` (span: `[9:11]`)
- `[e4]` **2 . Đối với hàng hóa thông dụng , sẵn có trên thị trường , không đòi hỏi nhân sự thực hiện dịch vụ liên quan phải có trình độ cao thì không yêu cầu về nhân sự chủ chốt . Trường hợp các dịch vụ liên quan có yếu tố đặc thù , phức tạp cần thiết phải do nhân sự có hiểu biết , nhiều kinh nghiệm đảm nhận thì có thể đưa ra yêu cầu về huy động nhân sự chủ chốt để thực hiện các công việc đặc thù , phức tạp này . Trường hợp** → `KHOAN` (span: `[12:78]`)
- `[e5]` **hàng hóa** → `TAI_SAN_VAT_CHAT` (span: `[15:16]`) *(lồng trong `e4` (`KHOAN`))*

**Quan hệ:**
- (`e1` 09/2020/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 09/2020/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 6 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 09/2020/TT-BKHĐT `[SO_HIEU]`)
- (`e4` 2 . Đối với hàng hóa thông dụng , sẵn có trên thị trường , không đòi hỏi nhân sự thực hiện dịch vụ liên quan phải có trình độ cao thì không yêu cầu về nhân sự chủ chốt . Trường hợp các dịch vụ liên quan có yếu tố đặc thù , phức tạp cần thiết phải do nhân sự có hiểu biết , nhiều kinh nghiệm đảm nhận thì có thể đưa ra yêu cầu về huy động nhân sự chủ chốt để thực hiện các công việc đặc thù , phức tạp này . Trường hợp `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 6 `[DIEU]`)


---

### Mẫu #09_2020_TT-BKHĐT_145176#body_context_54 (Loại: `body_context`)
> **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[09/2020/TT-BKHĐT]`<SO_HIEU>`** . **[Điều 6]`<DIEU>`** . **[3 . Trường hợp **[hồ sơ mời thầu]`<GIAY_TO_HO_SO>`** có yêu cầu huy động nhân sự chủ chốt , trong **[hồ sơ dự thầu]`<GIAY_TO_HO_SO>`** , nhà thầu phải chứng minh khả năng sẵn sàng huy động các nhân sự chủ chốt đã đề xuất để tham gia thực hiện gói thầu đáp ứng yêu cầu của **[hồ sơ mời thầu]`<GIAY_TO_HO_SO>`** . Nhân sự chủ chốt có thể thuộc biên chế của nhà thầu hoặc do nhà thầu huy động . Trường hợp nhân sự chủ chốt do nhà thầu đề xuất chưa đáp ứng yêu cầu của hồ]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[5:6]`)
- `[e1]` **09/2020/TT-BKHĐT** → `SO_HIEU` (span: `[7:8]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[0:4]`)
- `[e3]` **Điều 6** → `DIEU` (span: `[9:11]`)
- `[e4]` **3 . Trường hợp hồ sơ mời thầu có yêu cầu huy động nhân sự chủ chốt , trong hồ sơ dự thầu , nhà thầu phải chứng minh khả năng sẵn sàng huy động các nhân sự chủ chốt đã đề xuất để tham gia thực hiện gói thầu đáp ứng yêu cầu của hồ sơ mời thầu . Nhân sự chủ chốt có thể thuộc biên chế của nhà thầu hoặc do nhà thầu huy động . Trường hợp nhân sự chủ chốt do nhà thầu đề xuất chưa đáp ứng yêu cầu của hồ** → `KHOAN` (span: `[12:71]`)
- `[e5]` **hồ sơ mời thầu** → `GIAY_TO_HO_SO` (span: `[15:17]`) *(lồng trong `e4` (`KHOAN`))*
- `[e6]` **hồ sơ dự thầu** → `GIAY_TO_HO_SO` (span: `[24:26]`) *(lồng trong `e4` (`KHOAN`))*
- `[e7]` **hồ sơ mời thầu** → `GIAY_TO_HO_SO` (span: `[45:47]`) *(lồng trong `e4` (`KHOAN`))*

**Quan hệ:**
- (`e1` 09/2020/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 09/2020/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 6 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 09/2020/TT-BKHĐT `[SO_HIEU]`)
- (`e4` 3 . Trường hợp hồ sơ mời thầu có yêu cầu huy động nhân sự chủ chốt , trong hồ sơ dự thầu , nhà thầu phải chứng minh khả năng sẵn sàng huy động các nhân sự chủ chốt đã đề xuất để tham gia thực hiện gói thầu đáp ứng yêu cầu của hồ sơ mời thầu . Nhân sự chủ chốt có thể thuộc biên chế của nhà thầu hoặc do nhà thầu huy động . Trường hợp nhân sự chủ chốt do nhà thầu đề xuất chưa đáp ứng yêu cầu của hồ `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 6 `[DIEU]`)


---

### Mẫu #09_2020_TT-BKHĐT_145176#body_standalone_55 (Loại: `body_standalone`)
> **[Điều 6]`<DIEU>`** . **[3 . Trường hợp **[hồ sơ mời thầu]`<GIAY_TO_HO_SO>`** có yêu cầu huy động nhân sự chủ chốt , trong **[hồ sơ dự thầu]`<GIAY_TO_HO_SO>`** , nhà thầu phải chứng minh khả năng sẵn sàng huy động các nhân sự chủ chốt đã đề xuất để tham gia thực hiện gói thầu đáp ứng yêu cầu của **[hồ sơ mời thầu]`<GIAY_TO_HO_SO>`** . Nhân sự chủ chốt có thể thuộc biên chế của nhà thầu hoặc do nhà thầu huy động . Trường hợp nhân sự chủ chốt do nhà thầu đề xuất chưa đáp ứng yêu cầu của hồ]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 6** → `DIEU` (span: `[0:2]`)
- `[e1]` **3 . Trường hợp hồ sơ mời thầu có yêu cầu huy động nhân sự chủ chốt , trong hồ sơ dự thầu , nhà thầu phải chứng minh khả năng sẵn sàng huy động các nhân sự chủ chốt đã đề xuất để tham gia thực hiện gói thầu đáp ứng yêu cầu của hồ sơ mời thầu . Nhân sự chủ chốt có thể thuộc biên chế của nhà thầu hoặc do nhà thầu huy động . Trường hợp nhân sự chủ chốt do nhà thầu đề xuất chưa đáp ứng yêu cầu của hồ** → `KHOAN` (span: `[3:62]`)
- `[e2]` **hồ sơ mời thầu** → `GIAY_TO_HO_SO` (span: `[6:8]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **hồ sơ dự thầu** → `GIAY_TO_HO_SO` (span: `[15:17]`) *(lồng trong `e1` (`KHOAN`))*
- `[e4]` **hồ sơ mời thầu** → `GIAY_TO_HO_SO` (span: `[36:38]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 3 . Trường hợp hồ sơ mời thầu có yêu cầu huy động nhân sự chủ chốt , trong hồ sơ dự thầu , nhà thầu phải chứng minh khả năng sẵn sàng huy động các nhân sự chủ chốt đã đề xuất để tham gia thực hiện gói thầu đáp ứng yêu cầu của hồ sơ mời thầu . Nhân sự chủ chốt có thể thuộc biên chế của nhà thầu hoặc do nhà thầu huy động . Trường hợp nhân sự chủ chốt do nhà thầu đề xuất chưa đáp ứng yêu cầu của hồ `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 6 `[DIEU]`)


---

### Mẫu #09_2020_TT-BKHĐT_145176#body_context_56 (Loại: `body_context`)
> **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[09/2020/TT-BKHĐT]`<SO_HIEU>`** . **[Điều 7 . Hợp đồng]`<DIEU>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[5:6]`)
- `[e1]` **09/2020/TT-BKHĐT** → `SO_HIEU` (span: `[7:8]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[0:4]`)
- `[e3]` **Điều 7 . Hợp đồng** → `DIEU` (span: `[9:13]`)

**Quan hệ:**
- (`e1` 09/2020/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 09/2020/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 7 . Hợp đồng `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 09/2020/TT-BKHĐT `[SO_HIEU]`)


---

### Mẫu #09_2020_TT-BKHĐT_145176#body_context_57 (Loại: `body_context`)
> **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[09/2020/TT-BKHĐT]`<SO_HIEU>`** . **[Điều 7]`<DIEU>`** . **[1 . Loại hợp đồng áp dụng chủ yếu cho gói thầu mua sắm **[hàng hóa]`<TAI_SAN_VAT_CHAT>`** là hợp đồng trọn gói . Trường hợp **[hàng hóa]`<TAI_SAN_VAT_CHAT>`** có tính đặc thù , phức tạp , quy mô lớn và thời gian thực hiện hợp đồng **[trên 18 tháng]`<THOI_HAN>`** thì có thể áp dụng loại hợp đồng theo đơn giá điều chỉnh . Khi áp dụng loại hợp đồng theo đơn giá điều chỉnh , **[hồ sơ mời thầu]`<GIAY_TO_HO_SO>`** phải quy định rõ công thức điều chỉnh giá ; trong quá trình thực hiện hợp đồng , trường hợp có thay đổi]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[5:6]`)
- `[e1]` **09/2020/TT-BKHĐT** → `SO_HIEU` (span: `[7:8]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[0:4]`)
- `[e3]` **Điều 7** → `DIEU` (span: `[9:11]`)
- `[e4]` **1 . Loại hợp đồng áp dụng chủ yếu cho gói thầu mua sắm hàng hóa là hợp đồng trọn gói . Trường hợp hàng hóa có tính đặc thù , phức tạp , quy mô lớn và thời gian thực hiện hợp đồng trên 18 tháng thì có thể áp dụng loại hợp đồng theo đơn giá điều chỉnh . Khi áp dụng loại hợp đồng theo đơn giá điều chỉnh , hồ sơ mời thầu phải quy định rõ công thức điều chỉnh giá ; trong quá trình thực hiện hợp đồng , trường hợp có thay đổi** → `KHOAN` (span: `[12:77]`)
- `[e5]` **trên 18 tháng** → `THOI_HAN` (span: `[40:43]`) *(lồng trong `e4` (`KHOAN`))*
- `[e6]` **hồ sơ mời thầu** → `GIAY_TO_HO_SO` (span: `[60:62]`) *(lồng trong `e4` (`KHOAN`))*
- `[e7]` **hàng hóa** → `TAI_SAN_VAT_CHAT` (span: `[21:22]`) *(lồng trong `e4` (`KHOAN`))*
- `[e8]` **hàng hóa** → `TAI_SAN_VAT_CHAT` (span: `[27:28]`) *(lồng trong `e4` (`KHOAN`))*

**Quan hệ:**
- (`e1` 09/2020/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 09/2020/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 7 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 09/2020/TT-BKHĐT `[SO_HIEU]`)
- (`e4` 1 . Loại hợp đồng áp dụng chủ yếu cho gói thầu mua sắm hàng hóa là hợp đồng trọn gói . Trường hợp hàng hóa có tính đặc thù , phức tạp , quy mô lớn và thời gian thực hiện hợp đồng trên 18 tháng thì có thể áp dụng loại hợp đồng theo đơn giá điều chỉnh . Khi áp dụng loại hợp đồng theo đơn giá điều chỉnh , hồ sơ mời thầu phải quy định rõ công thức điều chỉnh giá ; trong quá trình thực hiện hợp đồng , trường hợp có thay đổi `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 7 `[DIEU]`)


---

### Mẫu #09_2020_TT-BKHĐT_145176#body_standalone_58 (Loại: `body_standalone`)
> **[Điều 7]`<DIEU>`** . **[1 . Loại hợp đồng áp dụng chủ yếu cho gói thầu mua sắm **[hàng hóa]`<TAI_SAN_VAT_CHAT>`** là hợp đồng trọn gói . Trường hợp **[hàng hóa]`<TAI_SAN_VAT_CHAT>`** có tính đặc thù , phức tạp , quy mô lớn và thời gian thực hiện hợp đồng **[trên 18 tháng]`<THOI_HAN>`** thì có thể áp dụng loại hợp đồng theo đơn giá điều chỉnh . Khi áp dụng loại hợp đồng theo đơn giá điều chỉnh , **[hồ sơ mời thầu]`<GIAY_TO_HO_SO>`** phải quy định rõ công thức điều chỉnh giá ; trong quá trình thực hiện hợp đồng , trường hợp có thay đổi]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 7** → `DIEU` (span: `[0:2]`)
- `[e1]` **1 . Loại hợp đồng áp dụng chủ yếu cho gói thầu mua sắm hàng hóa là hợp đồng trọn gói . Trường hợp hàng hóa có tính đặc thù , phức tạp , quy mô lớn và thời gian thực hiện hợp đồng trên 18 tháng thì có thể áp dụng loại hợp đồng theo đơn giá điều chỉnh . Khi áp dụng loại hợp đồng theo đơn giá điều chỉnh , hồ sơ mời thầu phải quy định rõ công thức điều chỉnh giá ; trong quá trình thực hiện hợp đồng , trường hợp có thay đổi** → `KHOAN` (span: `[3:68]`)
- `[e2]` **trên 18 tháng** → `THOI_HAN` (span: `[31:34]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **hồ sơ mời thầu** → `GIAY_TO_HO_SO` (span: `[51:53]`) *(lồng trong `e1` (`KHOAN`))*
- `[e4]` **hàng hóa** → `TAI_SAN_VAT_CHAT` (span: `[12:13]`) *(lồng trong `e1` (`KHOAN`))*
- `[e5]` **hàng hóa** → `TAI_SAN_VAT_CHAT` (span: `[18:19]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 1 . Loại hợp đồng áp dụng chủ yếu cho gói thầu mua sắm hàng hóa là hợp đồng trọn gói . Trường hợp hàng hóa có tính đặc thù , phức tạp , quy mô lớn và thời gian thực hiện hợp đồng trên 18 tháng thì có thể áp dụng loại hợp đồng theo đơn giá điều chỉnh . Khi áp dụng loại hợp đồng theo đơn giá điều chỉnh , hồ sơ mời thầu phải quy định rõ công thức điều chỉnh giá ; trong quá trình thực hiện hợp đồng , trường hợp có thay đổi `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 7 `[DIEU]`)


---

### Mẫu #09_2020_TT-BKHĐT_145176#body_context_59 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[09/2020/TT-BKHĐT]`<SO_HIEU>`** của **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** . **[Điều 7]`<DIEU>`** . **[2 . **[Hồ sơ mời thầu]`<GIAY_TO_HO_SO>`** phải bao gồm Mẫu hợp đồng và quy định chi tiết các điều , khoản của hợp đồng để nhà thầu làm cơ sở chào thầu và để các bên làm cơ sở thương thảo , hoàn thiện , ký kết hợp đồng .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **09/2020/TT-BKHĐT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[4:8]`)
- `[e3]` **Điều 7** → `DIEU` (span: `[9:11]`)
- `[e4]` **2 . Hồ sơ mời thầu phải bao gồm Mẫu hợp đồng và quy định chi tiết các điều , khoản của hợp đồng để nhà thầu làm cơ sở chào thầu và để các bên làm cơ sở thương thảo , hoàn thiện , ký kết hợp đồng .** → `KHOAN` (span: `[12:46]`)
- `[e5]` **Hồ sơ mời thầu** → `GIAY_TO_HO_SO` (span: `[14:16]`) *(lồng trong `e4` (`KHOAN`))*

**Quan hệ:**
- (`e1` 09/2020/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 09/2020/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 7 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 09/2020/TT-BKHĐT `[SO_HIEU]`)
- (`e4` 2 . Hồ sơ mời thầu phải bao gồm Mẫu hợp đồng và quy định chi tiết các điều , khoản của hợp đồng để nhà thầu làm cơ sở chào thầu và để các bên làm cơ sở thương thảo , hoàn thiện , ký kết hợp đồng . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 7 `[DIEU]`)


---

### Mẫu #09_2020_TT-BKHĐT_145176#body_context_60 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[09/2020/TT-BKHĐT]`<SO_HIEU>`** của **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** . **[Điều 7]`<DIEU>`** . **[3 . Việc chấm dứt hợp đồng tùy ý **[nêu tại]`<TU_KHOA_PHAP_LY>`** Mục 29.3 Điều kiện chung của Hợp đồng trong Mẫu **[hồ sơ mời thầu]`<GIAY_TO_HO_SO>`** ban hành kèm theo Thông tư này chỉ được thực hiện khi được người có thẩm quyền cho phép với lý do hợp lý .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **09/2020/TT-BKHĐT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[4:8]`)
- `[e3]` **Điều 7** → `DIEU` (span: `[9:11]`)
- `[e4]` **3 . Việc chấm dứt hợp đồng tùy ý nêu tại Mục 29.3 Điều kiện chung của Hợp đồng trong Mẫu hồ sơ mời thầu ban hành kèm theo Thông tư này chỉ được thực hiện khi được người có thẩm quyền cho phép với lý do hợp lý .** → `KHOAN` (span: `[12:49]`)
- `[e5]` **nêu tại** → `TU_KHOA_PHAP_LY` (span: `[18:20]`) *(lồng trong `e4` (`KHOAN`))*
- `[e6]` **hồ sơ mời thầu** → `GIAY_TO_HO_SO` (span: `[28:30]`) *(lồng trong `e4` (`KHOAN`))*

**Quan hệ:**
- (`e1` 09/2020/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 09/2020/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 7 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 09/2020/TT-BKHĐT `[SO_HIEU]`)
- (`e4` 3 . Việc chấm dứt hợp đồng tùy ý nêu tại Mục 29.3 Điều kiện chung của Hợp đồng trong Mẫu hồ sơ mời thầu ban hành kèm theo Thông tư này chỉ được thực hiện khi được người có thẩm quyền cho phép với lý do hợp lý . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 7 `[DIEU]`)


---

### Mẫu #09_2020_TT-BKHĐT_145176#body_standalone_61 (Loại: `body_standalone`)
> **[Điều 7]`<DIEU>`** . **[3 . Việc chấm dứt hợp đồng tùy ý **[nêu tại]`<TU_KHOA_PHAP_LY>`** Mục 29.3 Điều kiện chung của Hợp đồng trong Mẫu **[hồ sơ mời thầu]`<GIAY_TO_HO_SO>`** ban hành kèm theo Thông tư này chỉ được thực hiện khi được người có thẩm quyền cho phép với lý do hợp lý .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 7** → `DIEU` (span: `[0:2]`)
- `[e1]` **3 . Việc chấm dứt hợp đồng tùy ý nêu tại Mục 29.3 Điều kiện chung của Hợp đồng trong Mẫu hồ sơ mời thầu ban hành kèm theo Thông tư này chỉ được thực hiện khi được người có thẩm quyền cho phép với lý do hợp lý .** → `KHOAN` (span: `[3:40]`)
- `[e2]` **nêu tại** → `TU_KHOA_PHAP_LY` (span: `[9:11]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **hồ sơ mời thầu** → `GIAY_TO_HO_SO` (span: `[19:21]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 3 . Việc chấm dứt hợp đồng tùy ý nêu tại Mục 29.3 Điều kiện chung của Hợp đồng trong Mẫu hồ sơ mời thầu ban hành kèm theo Thông tư này chỉ được thực hiện khi được người có thẩm quyền cho phép với lý do hợp lý . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 7 `[DIEU]`)


---

### Mẫu #09_2020_TT-BKHĐT_145176#body_context_62 (Loại: `body_context`)
> **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[09/2020/TT-BKHĐT]`<SO_HIEU>`** . **[Điều 7]`<DIEU>`** . **[4 . Hợp đồng ký kết giữa **[chủ đầu tư]`<CHU_THE_CA_NHAN>`** với nhà thầu phải tuân thủ theo Mẫu hợp đồng , các điều kiện hợp đồng quy định trong **[hồ sơ mời thầu]`<GIAY_TO_HO_SO>`** và các hiệu chỉnh , bổ sung do nhà thầu đề xuất được **[chủ đầu tư]`<CHU_THE_CA_NHAN>`** chấp thuận trong quá trình thương thảo , hoàn thiện hợp đồng nhưng bảo đảm không trái với quy định của pháp luật về đấu thầu , quy định của Hiệp định CPTPP và quy định khác của pháp luật có liên quan .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[5:6]`)
- `[e1]` **09/2020/TT-BKHĐT** → `SO_HIEU` (span: `[7:8]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[0:4]`)
- `[e3]` **Điều 7** → `DIEU` (span: `[9:11]`)
- `[e4]` **4 . Hợp đồng ký kết giữa chủ đầu tư với nhà thầu phải tuân thủ theo Mẫu hợp đồng , các điều kiện hợp đồng quy định trong hồ sơ mời thầu và các hiệu chỉnh , bổ sung do nhà thầu đề xuất được chủ đầu tư chấp thuận trong quá trình thương thảo , hoàn thiện hợp đồng nhưng bảo đảm không trái với quy định của pháp luật về đấu thầu , quy định của Hiệp định CPTPP và quy định khác của pháp luật có liên quan .** → `KHOAN` (span: `[12:74]`)
- `[e5]` **hồ sơ mời thầu** → `GIAY_TO_HO_SO` (span: `[31:33]`) *(lồng trong `e4` (`KHOAN`))*
- `[e6]` **chủ đầu tư** → `CHU_THE_CA_NHAN` (span: `[17:19]`) *(lồng trong `e4` (`KHOAN`))*
- `[e7]` **chủ đầu tư** → `CHU_THE_CA_NHAN` (span: `[42:44]`) *(lồng trong `e4` (`KHOAN`))*

**Quan hệ:**
- (`e1` 09/2020/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 09/2020/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 7 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 09/2020/TT-BKHĐT `[SO_HIEU]`)
- (`e4` 4 . Hợp đồng ký kết giữa chủ đầu tư với nhà thầu phải tuân thủ theo Mẫu hợp đồng , các điều kiện hợp đồng quy định trong hồ sơ mời thầu và các hiệu chỉnh , bổ sung do nhà thầu đề xuất được chủ đầu tư chấp thuận trong quá trình thương thảo , hoàn thiện hợp đồng nhưng bảo đảm không trái với quy định của pháp luật về đấu thầu , quy định của Hiệp định CPTPP và quy định khác của pháp luật có liên quan . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 7 `[DIEU]`)


---

### Mẫu #09_2020_TT-BKHĐT_145176#body_standalone_63 (Loại: `body_standalone`)
> **[Điều 7]`<DIEU>`** . **[4 . Hợp đồng ký kết giữa **[chủ đầu tư]`<CHU_THE_CA_NHAN>`** với nhà thầu phải tuân thủ theo Mẫu hợp đồng , các điều kiện hợp đồng quy định trong **[hồ sơ mời thầu]`<GIAY_TO_HO_SO>`** và các hiệu chỉnh , bổ sung do nhà thầu đề xuất được **[chủ đầu tư]`<CHU_THE_CA_NHAN>`** chấp thuận trong quá trình thương thảo , hoàn thiện hợp đồng nhưng bảo đảm không trái với quy định của pháp luật về đấu thầu , quy định của Hiệp định CPTPP và quy định khác của pháp luật có liên quan .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 7** → `DIEU` (span: `[0:2]`)
- `[e1]` **4 . Hợp đồng ký kết giữa chủ đầu tư với nhà thầu phải tuân thủ theo Mẫu hợp đồng , các điều kiện hợp đồng quy định trong hồ sơ mời thầu và các hiệu chỉnh , bổ sung do nhà thầu đề xuất được chủ đầu tư chấp thuận trong quá trình thương thảo , hoàn thiện hợp đồng nhưng bảo đảm không trái với quy định của pháp luật về đấu thầu , quy định của Hiệp định CPTPP và quy định khác của pháp luật có liên quan .** → `KHOAN` (span: `[3:65]`)
- `[e2]` **hồ sơ mời thầu** → `GIAY_TO_HO_SO` (span: `[22:24]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **chủ đầu tư** → `CHU_THE_CA_NHAN` (span: `[8:10]`) *(lồng trong `e1` (`KHOAN`))*
- `[e4]` **chủ đầu tư** → `CHU_THE_CA_NHAN` (span: `[33:35]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 4 . Hợp đồng ký kết giữa chủ đầu tư với nhà thầu phải tuân thủ theo Mẫu hợp đồng , các điều kiện hợp đồng quy định trong hồ sơ mời thầu và các hiệu chỉnh , bổ sung do nhà thầu đề xuất được chủ đầu tư chấp thuận trong quá trình thương thảo , hoàn thiện hợp đồng nhưng bảo đảm không trái với quy định của pháp luật về đấu thầu , quy định của Hiệp định CPTPP và quy định khác của pháp luật có liên quan . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 7 `[DIEU]`)


---

### Mẫu #09_2020_TT-BKHĐT_145176#body_context_64 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[09/2020/TT-BKHĐT]`<SO_HIEU>`** của **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** . **[Điều 8 . Tổ chức thực hiện]`<DIEU>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **09/2020/TT-BKHĐT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[4:8]`)
- `[e3]` **Điều 8 . Tổ chức thực hiện** → `DIEU` (span: `[9:14]`)

**Quan hệ:**
- (`e1` 09/2020/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 09/2020/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 8 . Tổ chức thực hiện `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 09/2020/TT-BKHĐT `[SO_HIEU]`)


---

### Mẫu #09_2020_TT-BKHĐT_145176#body_context_65 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[09/2020/TT-BKHĐT]`<SO_HIEU>`** của **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** . **[Điều 8]`<DIEU>`** . **[1 . Thông tư này có hiệu lực thi hành kể từ ngày 15 tháng 01 năm 2021 .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **09/2020/TT-BKHĐT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[4:8]`)
- `[e3]` **Điều 8** → `DIEU` (span: `[9:11]`)
- `[e4]` **1 . Thông tư này có hiệu lực thi hành kể từ ngày 15 tháng 01 năm 2021 .** → `KHOAN` (span: `[12:28]`)

**Quan hệ:**
- (`e1` 09/2020/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 09/2020/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 8 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 09/2020/TT-BKHĐT `[SO_HIEU]`)
- (`e4` 1 . Thông tư này có hiệu lực thi hành kể từ ngày 15 tháng 01 năm 2021 . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 8 `[DIEU]`)


---

### Mẫu #09_2020_TT-BKHĐT_145176#body_standalone_66 (Loại: `body_standalone`)
> **[Điều 8]`<DIEU>`** . **[1 . Thông tư này có hiệu lực thi hành kể từ ngày 15 tháng 01 năm 2021 .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 8** → `DIEU` (span: `[0:2]`)
- `[e1]` **1 . Thông tư này có hiệu lực thi hành kể từ ngày 15 tháng 01 năm 2021 .** → `KHOAN` (span: `[3:19]`)

**Quan hệ:**
- (`e1` 1 . Thông tư này có hiệu lực thi hành kể từ ngày 15 tháng 01 năm 2021 . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 8 `[DIEU]`)


---

### Mẫu #09_2020_TT-BKHĐT_145176#body_context_67 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[09/2020/TT-BKHĐT]`<SO_HIEU>`** ban hành **[ngày 27 tháng 11 năm 2020]`<NGAY_BAN_HANH>`** bởi **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** . **[Điều 8]`<DIEU>`** . **[2 . Đối với các gói thầu thuộc phạm vi điều chỉnh của Hiệp định CPTPP đã mở thầu trước ngày Thông tư này có hiệu lực thi hành , việc đánh giá **[hồ sơ dự thầu]`<GIAY_TO_HO_SO>`** và xét duyệt trúng thầu thực hiện theo quy định nêu trong **[hồ sơ mời thầu]`<GIAY_TO_HO_SO>`** nhưng phải bảo đảm không trái với quy định của Hiệp định CPTPP.]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **09/2020/TT-BKHĐT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[11:15]`)
- `[e3]` **ngày 27 tháng 11 năm 2020** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 8** → `DIEU` (span: `[16:18]`)
- `[e5]` **2 . Đối với các gói thầu thuộc phạm vi điều chỉnh của Hiệp định CPTPP đã mở thầu trước ngày Thông tư này có hiệu lực thi hành , việc đánh giá hồ sơ dự thầu và xét duyệt trúng thầu thực hiện theo quy định nêu trong hồ sơ mời thầu nhưng phải bảo đảm không trái với quy định của Hiệp định CPTPP.** → `KHOAN` (span: `[19:64]`)
- `[e6]` **hồ sơ dự thầu** → `GIAY_TO_HO_SO` (span: `[42:44]`) *(lồng trong `e5` (`KHOAN`))*
- `[e7]` **hồ sơ mời thầu** → `GIAY_TO_HO_SO` (span: `[52:54]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 09/2020/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 09/2020/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 09/2020/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 27 tháng 11 năm 2020 `[NGAY_BAN_HANH]`)
- (`e4` Điều 8 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 09/2020/TT-BKHĐT `[SO_HIEU]`)
- (`e5` 2 . Đối với các gói thầu thuộc phạm vi điều chỉnh của Hiệp định CPTPP đã mở thầu trước ngày Thông tư này có hiệu lực thi hành , việc đánh giá hồ sơ dự thầu và xét duyệt trúng thầu thực hiện theo quy định nêu trong hồ sơ mời thầu nhưng phải bảo đảm không trái với quy định của Hiệp định CPTPP. `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 8 `[DIEU]`)


---

### Mẫu #09_2020_TT-BKHĐT_145176#body_standalone_68 (Loại: `body_standalone`)
> **[Điều 8]`<DIEU>`** . **[2 . Đối với các gói thầu thuộc phạm vi điều chỉnh của Hiệp định CPTPP đã mở thầu trước ngày Thông tư này có hiệu lực thi hành , việc đánh giá **[hồ sơ dự thầu]`<GIAY_TO_HO_SO>`** và xét duyệt trúng thầu thực hiện theo quy định nêu trong **[hồ sơ mời thầu]`<GIAY_TO_HO_SO>`** nhưng phải bảo đảm không trái với quy định của Hiệp định CPTPP.]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 8** → `DIEU` (span: `[0:2]`)
- `[e1]` **2 . Đối với các gói thầu thuộc phạm vi điều chỉnh của Hiệp định CPTPP đã mở thầu trước ngày Thông tư này có hiệu lực thi hành , việc đánh giá hồ sơ dự thầu và xét duyệt trúng thầu thực hiện theo quy định nêu trong hồ sơ mời thầu nhưng phải bảo đảm không trái với quy định của Hiệp định CPTPP.** → `KHOAN` (span: `[3:48]`)
- `[e2]` **hồ sơ dự thầu** → `GIAY_TO_HO_SO` (span: `[26:28]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **hồ sơ mời thầu** → `GIAY_TO_HO_SO` (span: `[36:38]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 2 . Đối với các gói thầu thuộc phạm vi điều chỉnh của Hiệp định CPTPP đã mở thầu trước ngày Thông tư này có hiệu lực thi hành , việc đánh giá hồ sơ dự thầu và xét duyệt trúng thầu thực hiện theo quy định nêu trong hồ sơ mời thầu nhưng phải bảo đảm không trái với quy định của Hiệp định CPTPP. `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 8 `[DIEU]`)


---

### Mẫu #09_2020_TT-BKHĐT_145176#body_context_69 (Loại: `body_context`)
> **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[09/2020/TT-BKHĐT]`<SO_HIEU>`** . **[Điều 8]`<DIEU>`** . **[3 . Đối với các gói thầu thuộc phạm vi điều chỉnh của Hiệp định CPTPP đã phê duyệt , phát hành **[hồ sơ mời thầu]`<GIAY_TO_HO_SO>`** trước ngày Thông tư này có hiệu lực thi hành nhưng có thời điểm đóng thầu sau ngày Thông tư này có hiệu lực thi hành và chưa đến thời điểm đóng thầu , trường hợp có nội dung không phù hợp hoặc trái với hướng dẫn **[nêu tại]`<TU_KHOA_PHAP_LY>`** các Mẫu **[hồ sơ mời thầu]`<GIAY_TO_HO_SO>`** ban hành kèm theo Thông tư này thì phải sửa đổi cho phù hợp .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[5:6]`)
- `[e1]` **09/2020/TT-BKHĐT** → `SO_HIEU` (span: `[7:8]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[0:4]`)
- `[e3]` **Điều 8** → `DIEU` (span: `[9:11]`)
- `[e4]` **3 . Đối với các gói thầu thuộc phạm vi điều chỉnh của Hiệp định CPTPP đã phê duyệt , phát hành hồ sơ mời thầu trước ngày Thông tư này có hiệu lực thi hành nhưng có thời điểm đóng thầu sau ngày Thông tư này có hiệu lực thi hành và chưa đến thời điểm đóng thầu , trường hợp có nội dung không phù hợp hoặc trái với hướng dẫn nêu tại các Mẫu hồ sơ mời thầu ban hành kèm theo Thông tư này thì phải sửa đổi cho phù hợp .** → `KHOAN` (span: `[12:81]`)
- `[e5]` **nêu tại** → `TU_KHOA_PHAP_LY` (span: `[64:66]`) *(lồng trong `e4` (`KHOAN`))*
- `[e6]` **hồ sơ mời thầu** → `GIAY_TO_HO_SO` (span: `[27:29]`) *(lồng trong `e4` (`KHOAN`))*
- `[e7]` **hồ sơ mời thầu** → `GIAY_TO_HO_SO` (span: `[68:70]`) *(lồng trong `e4` (`KHOAN`))*

**Quan hệ:**
- (`e1` 09/2020/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 09/2020/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 8 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 09/2020/TT-BKHĐT `[SO_HIEU]`)
- (`e4` 3 . Đối với các gói thầu thuộc phạm vi điều chỉnh của Hiệp định CPTPP đã phê duyệt , phát hành hồ sơ mời thầu trước ngày Thông tư này có hiệu lực thi hành nhưng có thời điểm đóng thầu sau ngày Thông tư này có hiệu lực thi hành và chưa đến thời điểm đóng thầu , trường hợp có nội dung không phù hợp hoặc trái với hướng dẫn nêu tại các Mẫu hồ sơ mời thầu ban hành kèm theo Thông tư này thì phải sửa đổi cho phù hợp . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 8 `[DIEU]`)


---

### Mẫu #09_2020_TT-BKHĐT_145176#body_standalone_70 (Loại: `body_standalone`)
> **[Điều 8]`<DIEU>`** . **[3 . Đối với các gói thầu thuộc phạm vi điều chỉnh của Hiệp định CPTPP đã phê duyệt , phát hành **[hồ sơ mời thầu]`<GIAY_TO_HO_SO>`** trước ngày Thông tư này có hiệu lực thi hành nhưng có thời điểm đóng thầu sau ngày Thông tư này có hiệu lực thi hành và chưa đến thời điểm đóng thầu , trường hợp có nội dung không phù hợp hoặc trái với hướng dẫn **[nêu tại]`<TU_KHOA_PHAP_LY>`** các Mẫu **[hồ sơ mời thầu]`<GIAY_TO_HO_SO>`** ban hành kèm theo Thông tư này thì phải sửa đổi cho phù hợp .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 8** → `DIEU` (span: `[0:2]`)
- `[e1]` **3 . Đối với các gói thầu thuộc phạm vi điều chỉnh của Hiệp định CPTPP đã phê duyệt , phát hành hồ sơ mời thầu trước ngày Thông tư này có hiệu lực thi hành nhưng có thời điểm đóng thầu sau ngày Thông tư này có hiệu lực thi hành và chưa đến thời điểm đóng thầu , trường hợp có nội dung không phù hợp hoặc trái với hướng dẫn nêu tại các Mẫu hồ sơ mời thầu ban hành kèm theo Thông tư này thì phải sửa đổi cho phù hợp .** → `KHOAN` (span: `[3:72]`)
- `[e2]` **nêu tại** → `TU_KHOA_PHAP_LY` (span: `[55:57]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **hồ sơ mời thầu** → `GIAY_TO_HO_SO` (span: `[18:20]`) *(lồng trong `e1` (`KHOAN`))*
- `[e4]` **hồ sơ mời thầu** → `GIAY_TO_HO_SO` (span: `[59:61]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 3 . Đối với các gói thầu thuộc phạm vi điều chỉnh của Hiệp định CPTPP đã phê duyệt , phát hành hồ sơ mời thầu trước ngày Thông tư này có hiệu lực thi hành nhưng có thời điểm đóng thầu sau ngày Thông tư này có hiệu lực thi hành và chưa đến thời điểm đóng thầu , trường hợp có nội dung không phù hợp hoặc trái với hướng dẫn nêu tại các Mẫu hồ sơ mời thầu ban hành kèm theo Thông tư này thì phải sửa đổi cho phù hợp . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 8 `[DIEU]`)


---

### Mẫu #09_2020_TT-BKHĐT_145176#body_context_71 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[09/2020/TT-BKHĐT]`<SO_HIEU>`** ban hành **[ngày 27 tháng 11 năm 2020]`<NGAY_BAN_HANH>`** bởi **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** . **[Điều 8]`<DIEU>`** . **[4 . Đối với các gói thầu thuộc phạm vi điều chỉnh của Hiệp định CPTPP đã phê duyệt **[hồ sơ mời thầu]`<GIAY_TO_HO_SO>`** trước ngày Thông tư này có hiệu lực thi hành nhưng chưa phát hành **[hồ sơ mời thầu]`<GIAY_TO_HO_SO>`** thì phải sửa đổi theo các Mẫu **[hồ sơ mời thầu]`<GIAY_TO_HO_SO>`** ban hành kèm theo Thông tư này .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **09/2020/TT-BKHĐT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[11:15]`)
- `[e3]` **ngày 27 tháng 11 năm 2020** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 8** → `DIEU` (span: `[16:18]`)
- `[e5]` **4 . Đối với các gói thầu thuộc phạm vi điều chỉnh của Hiệp định CPTPP đã phê duyệt hồ sơ mời thầu trước ngày Thông tư này có hiệu lực thi hành nhưng chưa phát hành hồ sơ mời thầu thì phải sửa đổi theo các Mẫu hồ sơ mời thầu ban hành kèm theo Thông tư này .** → `KHOAN` (span: `[19:60]`)
- `[e6]` **hồ sơ mời thầu** → `GIAY_TO_HO_SO` (span: `[32:34]`) *(lồng trong `e5` (`KHOAN`))*
- `[e7]` **hồ sơ mời thầu** → `GIAY_TO_HO_SO` (span: `[44:46]`) *(lồng trong `e5` (`KHOAN`))*
- `[e8]` **hồ sơ mời thầu** → `GIAY_TO_HO_SO` (span: `[52:54]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 09/2020/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 09/2020/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 09/2020/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 27 tháng 11 năm 2020 `[NGAY_BAN_HANH]`)
- (`e4` Điều 8 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 09/2020/TT-BKHĐT `[SO_HIEU]`)
- (`e5` 4 . Đối với các gói thầu thuộc phạm vi điều chỉnh của Hiệp định CPTPP đã phê duyệt hồ sơ mời thầu trước ngày Thông tư này có hiệu lực thi hành nhưng chưa phát hành hồ sơ mời thầu thì phải sửa đổi theo các Mẫu hồ sơ mời thầu ban hành kèm theo Thông tư này . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 8 `[DIEU]`)


---

### Mẫu #09_2020_TT-BKHĐT_145176#body_standalone_72 (Loại: `body_standalone`)
> **[Điều 8]`<DIEU>`** . **[4 . Đối với các gói thầu thuộc phạm vi điều chỉnh của Hiệp định CPTPP đã phê duyệt **[hồ sơ mời thầu]`<GIAY_TO_HO_SO>`** trước ngày Thông tư này có hiệu lực thi hành nhưng chưa phát hành **[hồ sơ mời thầu]`<GIAY_TO_HO_SO>`** thì phải sửa đổi theo các Mẫu **[hồ sơ mời thầu]`<GIAY_TO_HO_SO>`** ban hành kèm theo Thông tư này .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 8** → `DIEU` (span: `[0:2]`)
- `[e1]` **4 . Đối với các gói thầu thuộc phạm vi điều chỉnh của Hiệp định CPTPP đã phê duyệt hồ sơ mời thầu trước ngày Thông tư này có hiệu lực thi hành nhưng chưa phát hành hồ sơ mời thầu thì phải sửa đổi theo các Mẫu hồ sơ mời thầu ban hành kèm theo Thông tư này .** → `KHOAN` (span: `[3:44]`)
- `[e2]` **hồ sơ mời thầu** → `GIAY_TO_HO_SO` (span: `[16:18]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **hồ sơ mời thầu** → `GIAY_TO_HO_SO` (span: `[28:30]`) *(lồng trong `e1` (`KHOAN`))*
- `[e4]` **hồ sơ mời thầu** → `GIAY_TO_HO_SO` (span: `[36:38]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 4 . Đối với các gói thầu thuộc phạm vi điều chỉnh của Hiệp định CPTPP đã phê duyệt hồ sơ mời thầu trước ngày Thông tư này có hiệu lực thi hành nhưng chưa phát hành hồ sơ mời thầu thì phải sửa đổi theo các Mẫu hồ sơ mời thầu ban hành kèm theo Thông tư này . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 8 `[DIEU]`)


---

### Mẫu #09_2020_TT-BKHĐT_145176#body_context_73 (Loại: `body_context`)
> **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[09/2020/TT-BKHĐT]`<SO_HIEU>`** . **[Điều 8]`<DIEU>`** . **[5 . Các tổ chức được liệt kê tại phụ lục kèm theo **[Nghị định số 95/2020/NĐ-CP]`<THAM_CHIEU_PHAP_LY>`** và các tổ chức , cá nhân có liên quan chịu trách nhiệm thi hành Thông tư này . Trong quá trình thực hiện , nếu có vướng mắc , đề nghị gửi ý kiến về **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_THAM_QUYEN>`** để kịp thời hướng dẫn .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[5:6]`)
- `[e1]` **09/2020/TT-BKHĐT** → `SO_HIEU` (span: `[7:8]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[0:4]`)
- `[e3]` **Điều 8** → `DIEU` (span: `[9:11]`)
- `[e4]` **5 . Các tổ chức được liệt kê tại phụ lục kèm theo Nghị định số 95/2020/NĐ-CP và các tổ chức , cá nhân có liên quan chịu trách nhiệm thi hành Thông tư này . Trong quá trình thực hiện , nếu có vướng mắc , đề nghị gửi ý kiến về Bộ Kế hoạch và Đầu tư để kịp thời hướng dẫn .** → `KHOAN` (span: `[12:58]`)
- `[e5]` **Nghị định số 95/2020/NĐ-CP** → `THAM_CHIEU_PHAP_LY` (span: `[22:25]`) *(lồng trong `e4` (`KHOAN`))*
- `[e6]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_THAM_QUYEN` (span: `[50:54]`) *(lồng trong `e4` (`KHOAN`))*

**Quan hệ:**
- (`e1` 09/2020/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 09/2020/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 8 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 09/2020/TT-BKHĐT `[SO_HIEU]`)
- (`e4` 5 . Các tổ chức được liệt kê tại phụ lục kèm theo Nghị định số 95/2020/NĐ-CP và các tổ chức , cá nhân có liên quan chịu trách nhiệm thi hành Thông tư này . Trong quá trình thực hiện , nếu có vướng mắc , đề nghị gửi ý kiến về Bộ Kế hoạch và Đầu tư để kịp thời hướng dẫn . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 8 `[DIEU]`)
- (`e4` 5 . Các tổ chức được liệt kê tại phụ lục kèm theo Nghị định số 95/2020/NĐ-CP và các tổ chức , cá nhân có liên quan chịu trách nhiệm thi hành Thông tư này . Trong quá trình thực hiện , nếu có vướng mắc , đề nghị gửi ý kiến về Bộ Kế hoạch và Đầu tư để kịp thời hướng dẫn . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e5` Nghị định số 95/2020/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #09_2020_TT-BKHĐT_145176#body_standalone_74 (Loại: `body_standalone`)
> **[Điều 8]`<DIEU>`** . **[5 . Các tổ chức được liệt kê tại phụ lục kèm theo **[Nghị định số 95/2020/NĐ-CP]`<THAM_CHIEU_PHAP_LY>`** và các tổ chức , cá nhân có liên quan chịu trách nhiệm thi hành Thông tư này . Trong quá trình thực hiện , nếu có vướng mắc , đề nghị gửi ý kiến về **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_THAM_QUYEN>`** để kịp thời hướng dẫn .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 8** → `DIEU` (span: `[0:2]`)
- `[e1]` **5 . Các tổ chức được liệt kê tại phụ lục kèm theo Nghị định số 95/2020/NĐ-CP và các tổ chức , cá nhân có liên quan chịu trách nhiệm thi hành Thông tư này . Trong quá trình thực hiện , nếu có vướng mắc , đề nghị gửi ý kiến về Bộ Kế hoạch và Đầu tư để kịp thời hướng dẫn .** → `KHOAN` (span: `[3:49]`)
- `[e2]` **Nghị định số 95/2020/NĐ-CP** → `THAM_CHIEU_PHAP_LY` (span: `[13:16]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_THAM_QUYEN` (span: `[41:45]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 5 . Các tổ chức được liệt kê tại phụ lục kèm theo Nghị định số 95/2020/NĐ-CP và các tổ chức , cá nhân có liên quan chịu trách nhiệm thi hành Thông tư này . Trong quá trình thực hiện , nếu có vướng mắc , đề nghị gửi ý kiến về Bộ Kế hoạch và Đầu tư để kịp thời hướng dẫn . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 8 `[DIEU]`)
- (`e1` 5 . Các tổ chức được liệt kê tại phụ lục kèm theo Nghị định số 95/2020/NĐ-CP và các tổ chức , cá nhân có liên quan chịu trách nhiệm thi hành Thông tư này . Trong quá trình thực hiện , nếu có vướng mắc , đề nghị gửi ý kiến về Bộ Kế hoạch và Đầu tư để kịp thời hướng dẫn . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e2` Nghị định số 95/2020/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #09_2020_TT-BKHĐT_145176#body_context_75 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[09/2020/TT-BKHĐT]`<SO_HIEU>`** ban hành **[ngày 27 tháng 11 năm 2020]`<NGAY_BAN_HANH>`** bởi **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** . **[Điều 1 . Phạm vi điều chỉnh]`<DIEU>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **09/2020/TT-BKHĐT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[11:15]`)
- `[e3]` **ngày 27 tháng 11 năm 2020** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 1 . Phạm vi điều chỉnh** → `DIEU` (span: `[16:21]`)

**Quan hệ:**
- (`e1` 09/2020/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 09/2020/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 09/2020/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 27 tháng 11 năm 2020 `[NGAY_BAN_HANH]`)
- (`e4` Điều 1 . Phạm vi điều chỉnh `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 09/2020/TT-BKHĐT `[SO_HIEU]`)


---

### Mẫu #09_2020_TT-BKHĐT_145176#body_context_76 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[09/2020/TT-BKHĐT]`<SO_HIEU>`** của **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** . **[Điều 2 . Đối tượng áp dụng]`<DIEU>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **09/2020/TT-BKHĐT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[4:8]`)
- `[e3]` **Điều 2 . Đối tượng áp dụng** → `DIEU` (span: `[9:14]`)

**Quan hệ:**
- (`e1` 09/2020/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 09/2020/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 2 . Đối tượng áp dụng `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 09/2020/TT-BKHĐT `[SO_HIEU]`)


---

### Mẫu #09_2020_TT-BKHĐT_145176#body_context_77 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[09/2020/TT-BKHĐT]`<SO_HIEU>`** của **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** . **[Điều 3]`<DIEU>`** . **[1 . Áp dụng Mẫu **[hồ sơ mời thầu]`<GIAY_TO_HO_SO>`** :]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **09/2020/TT-BKHĐT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[4:8]`)
- `[e3]` **Điều 3** → `DIEU` (span: `[9:11]`)
- `[e4]` **1 . Áp dụng Mẫu hồ sơ mời thầu :** → `KHOAN` (span: `[12:19]`)
- `[e5]` **hồ sơ mời thầu** → `GIAY_TO_HO_SO` (span: `[16:18]`) *(lồng trong `e4` (`KHOAN`))*

**Quan hệ:**
- (`e1` 09/2020/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 09/2020/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 3 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 09/2020/TT-BKHĐT `[SO_HIEU]`)
- (`e4` 1 . Áp dụng Mẫu hồ sơ mời thầu : `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 3 `[DIEU]`)


---

### Mẫu #09_2020_TT-BKHĐT_145176#body_context_78 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[09/2020/TT-BKHĐT]`<SO_HIEU>`** của **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** . **[Điều 7 . Hợp đồng]`<DIEU>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **09/2020/TT-BKHĐT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[4:8]`)
- `[e3]` **Điều 7 . Hợp đồng** → `DIEU` (span: `[9:13]`)

**Quan hệ:**
- (`e1` 09/2020/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 09/2020/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 7 . Hợp đồng `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 09/2020/TT-BKHĐT `[SO_HIEU]`)


---

### Mẫu #09_2020_TT-BKHĐT_145176#body_context_79 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[09/2020/TT-BKHĐT]`<SO_HIEU>`** của **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** . **[Điều 8 . Tổ chức thực hiện]`<DIEU>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **09/2020/TT-BKHĐT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[4:8]`)
- `[e3]` **Điều 8 . Tổ chức thực hiện** → `DIEU` (span: `[9:14]`)

**Quan hệ:**
- (`e1` 09/2020/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 09/2020/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 8 . Tổ chức thực hiện `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 09/2020/TT-BKHĐT `[SO_HIEU]`)


---

### Mẫu #09_2020_TT-BKHĐT_145176#hard_negative_80 (Loại: `hard_negative`)
> CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM Độc lập – Tự do – Hạnh phúc


---

### Mẫu #09_2020_TT-BKHĐT_145176#hard_negative_81 (Loại: `hard_negative`)
> Nơi nhận :


---
