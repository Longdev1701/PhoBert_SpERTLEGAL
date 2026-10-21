# Dữ liệu gán nhãn văn bản: 06_2023_TT-BKHĐT_163394
- **Thể loại**: `thong_tu`
- **Phân vùng dữ liệu**: `TRAIN`
- **Tổng số mẫu**: 41 mẫu
- **Tổng số thực thể**: 204
- **Tổng số quan hệ**: 159

---

### Mẫu #06_2023_TT-BKHĐT_163394#header_0 (Loại: `header`)
> **[BỘ KẾ HOẠCH VÀ ĐẦU TƯ]`<CO_QUAN_BAN_HANH>`** . Số : **[06/2023/TT-BKHĐT]`<SO_HIEU>`** . CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM . Độc lập - Tự do - Hạnh phúc . Hà Nội , **[ngày 02 tháng 10 năm 2023]`<NGAY_BAN_HANH>`** . **[THÔNG TƯ]`<LOAI_VAN_BAN>`**

**Thực thể:**
- `[e0]` **06/2023/TT-BKHĐT** → `SO_HIEU` (span: `[7:8]`)
- `[e1]` **ngày 02 tháng 10 năm 2023** → `NGAY_BAN_HANH` (span: `[24:30]`)
- `[e2]` **BỘ KẾ HOẠCH VÀ ĐẦU TƯ** → `CO_QUAN_BAN_HANH` (span: `[0:4]`)
- `[e3]` **THÔNG TƯ** → `LOAI_VAN_BAN` (span: `[31:32]`)

**Quan hệ:**
- (`e0` 06/2023/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` BỘ KẾ HOẠCH VÀ ĐẦU TƯ `[CO_QUAN_BAN_HANH]`)
- (`e0` 06/2023/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e1` ngày 02 tháng 10 năm 2023 `[NGAY_BAN_HANH]`)
- (`e0` 06/2023/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e3` THÔNG TƯ `[LOAI_VAN_BAN]`)


---

### Mẫu #06_2023_TT-BKHĐT_163394#signature_1 (Loại: `signature`)
> **[BỘ TRƯỞNG]`<CHUC_DANH_NGUOI_KY>`** . ( Đã ký ) . **[Nguyễn Chí Dũng]`<NGUOI_KY>`**

**Thực thể:**
- `[e0]` **Nguyễn Chí Dũng** → `NGUOI_KY` (span: `[7:8]`)
- `[e1]` **BỘ TRƯỞNG** → `CHUC_DANH_NGUOI_KY` (span: `[0:1]`)

**Quan hệ:**
- (`e0` Nguyễn Chí Dũng `[NGUOI_KY]`) ==[ **GIU_CHUC_VU** ]==> (`e1` BỘ TRƯỞNG `[CHUC_DANH_NGUOI_KY]`)


---

### Mẫu #06_2023_TT-BKHĐT_163394#meta_2 (Loại: `meta`)
> **[BỘ KẾ HOẠCH VÀ ĐẦU TƯ]`<CO_QUAN_BAN_HANH>`** . Số : **[06/2023/TT-BKHĐT]`<SO_HIEU>`** . CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM . Độc lập - Tự do - Hạnh phúc . Hà Nội , ngày 02 tháng 10 năm 2023 . **[THÔNG TƯ]`<LOAI_VAN_BAN>`** . **[BỘ TRƯỞNG]`<CHUC_DANH_NGUOI_KY>`** . ( Đã ký ) . **[Nguyễn Chí Dũng]`<NGUOI_KY>`**

**Thực thể:**
- `[e0]` **06/2023/TT-BKHĐT** → `SO_HIEU` (span: `[7:8]`)
- `[e1]` **BỘ KẾ HOẠCH VÀ ĐẦU TƯ** → `CO_QUAN_BAN_HANH` (span: `[0:4]`)
- `[e2]` **THÔNG TƯ** → `LOAI_VAN_BAN` (span: `[31:32]`)
- `[e3]` **Nguyễn Chí Dũng** → `NGUOI_KY` (span: `[40:41]`)
- `[e4]` **BỘ TRƯỞNG** → `CHUC_DANH_NGUOI_KY` (span: `[33:34]`)

**Quan hệ:**
- (`e0` 06/2023/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e1` BỘ KẾ HOẠCH VÀ ĐẦU TƯ `[CO_QUAN_BAN_HANH]`)
- (`e0` 06/2023/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e2` THÔNG TƯ `[LOAI_VAN_BAN]`)
- (`e0` 06/2023/TT-BKHĐT `[SO_HIEU]`) ==[ **KY_BOI** ]==> (`e3` Nguyễn Chí Dũng `[NGUOI_KY]`)
- (`e3` Nguyễn Chí Dũng `[NGUOI_KY]`) ==[ **GIU_CHUC_VU** ]==> (`e4` BỘ TRƯỞNG `[CHUC_DANH_NGUOI_KY]`)


---

### Mẫu #06_2023_TT-BKHĐT_163394#preamble_context_3 (Loại: `preamble_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[06/2023/TT-BKHĐT]`<SO_HIEU>`** của **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** . Quy định hệ thống chỉ tiêu thống kê **[ngành Thống kê]`<LINH_VUC>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **06/2023/TT-BKHĐT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[4:8]`)
- `[e3]` **ngành Thống kê** → `LINH_VUC` (span: `[13:15]`)

**Quan hệ:**
- (`e1` 06/2023/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 06/2023/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 06/2023/TT-BKHĐT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` ngành Thống kê `[LINH_VUC]`)


---

### Mẫu #06_2023_TT-BKHĐT_163394#preamble_standalone_4 (Loại: `preamble_standalone`)
> Quy định hệ thống chỉ tiêu thống kê **[ngành Thống kê]`<LINH_VUC>`**

**Thực thể:**
- `[e0]` **ngành Thống kê** → `LINH_VUC` (span: `[4:6]`)


---

### Mẫu #06_2023_TT-BKHĐT_163394#preamble_context_5 (Loại: `preamble_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[06/2023/TT-BKHĐT]`<SO_HIEU>`** của **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** . **[Căn cứ]`<TU_KHOA_PHAP_LY>`** **[Luật Thống kê]`<THAM_CHIEU_PHAP_LY>`** **[ngày 23 tháng 11 năm 2015]`<NGAY_THAM_CHIEU>`** ; Luật **[sửa đổi , bổ sung]`<TU_KHOA_PHAP_LY>`** một số điều và Phụ lục Danh mục chỉ tiêu thống kê quốc gia của Luật Thống kê ngày 12 tháng 11 năm 2021 ;

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **06/2023/TT-BKHĐT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[4:8]`)
- `[e3]` **Luật Thống kê** → `THAM_CHIEU_PHAP_LY` (span: `[10:12]`)
- `[e4]` **Căn cứ** → `TU_KHOA_PHAP_LY` (span: `[9:10]`)
- `[e5]` **sửa đổi , bổ sung** → `TU_KHOA_PHAP_LY` (span: `[20:23]`)
- `[e6]` **ngày 23 tháng 11 năm 2015** → `NGAY_THAM_CHIEU` (span: `[12:18]`)

**Quan hệ:**
- (`e1` 06/2023/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 06/2023/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e4` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Luật Thống kê `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 06/2023/TT-BKHĐT `[SO_HIEU]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Luật Thống kê `[THAM_CHIEU_PHAP_LY]`)
- (`e3` Luật Thống kê `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e6` ngày 23 tháng 11 năm 2015 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #06_2023_TT-BKHĐT_163394#preamble_standalone_6 (Loại: `preamble_standalone`)
> **[Căn cứ]`<TU_KHOA_PHAP_LY>`** **[Luật Thống kê]`<THAM_CHIEU_PHAP_LY>`** **[ngày 23 tháng 11 năm 2015]`<NGAY_THAM_CHIEU>`** ; Luật **[sửa đổi , bổ sung]`<TU_KHOA_PHAP_LY>`** một số điều và Phụ lục Danh mục chỉ tiêu thống kê quốc gia của Luật Thống kê ngày 12 tháng 11 năm 2021 ;

**Thực thể:**
- `[e0]` **Luật Thống kê** → `THAM_CHIEU_PHAP_LY` (span: `[1:3]`)
- `[e1]` **Căn cứ** → `TU_KHOA_PHAP_LY` (span: `[0:1]`)
- `[e2]` **sửa đổi , bổ sung** → `TU_KHOA_PHAP_LY` (span: `[11:14]`)
- `[e3]` **ngày 23 tháng 11 năm 2015** → `NGAY_THAM_CHIEU` (span: `[3:9]`)

**Quan hệ:**
- (`e1` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e0` Luật Thống kê `[THAM_CHIEU_PHAP_LY]`)
- (`e0` Luật Thống kê `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e3` ngày 23 tháng 11 năm 2015 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #06_2023_TT-BKHĐT_163394#preamble_context_7 (Loại: `preamble_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[06/2023/TT-BKHĐT]`<SO_HIEU>`** của **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** . **[Căn cứ]`<TU_KHOA_PHAP_LY>`** **[Nghị định số 94/2016/NĐ-CP]`<THAM_CHIEU_PHAP_LY>`** **[ngày 01 tháng 7 năm 2016]`<NGAY_THAM_CHIEU>`** của **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** quy định chi tiết và hướng dẫn thi hành một số điều của Luật Thống kê ;

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **06/2023/TT-BKHĐT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[4:8]`)
- `[e3]` **Nghị định số 94/2016/NĐ-CP** → `THAM_CHIEU_PHAP_LY` (span: `[10:13]`)
- `[e4]` **Căn cứ** → `TU_KHOA_PHAP_LY` (span: `[9:10]`)
- `[e5]` **ngày 01 tháng 7 năm 2016** → `NGAY_THAM_CHIEU` (span: `[13:19]`)
- `[e6]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[20:21]`)

**Quan hệ:**
- (`e1` 06/2023/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 06/2023/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e4` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Nghị định số 94/2016/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 06/2023/TT-BKHĐT `[SO_HIEU]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Nghị định số 94/2016/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e3` Nghị định số 94/2016/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e5` ngày 01 tháng 7 năm 2016 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #06_2023_TT-BKHĐT_163394#preamble_standalone_8 (Loại: `preamble_standalone`)
> **[Căn cứ]`<TU_KHOA_PHAP_LY>`** **[Nghị định số 94/2016/NĐ-CP]`<THAM_CHIEU_PHAP_LY>`** **[ngày 01 tháng 7 năm 2016]`<NGAY_THAM_CHIEU>`** của **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** quy định chi tiết và hướng dẫn thi hành một số điều của Luật Thống kê ;

**Thực thể:**
- `[e0]` **Nghị định số 94/2016/NĐ-CP** → `THAM_CHIEU_PHAP_LY` (span: `[1:4]`)
- `[e1]` **Căn cứ** → `TU_KHOA_PHAP_LY` (span: `[0:1]`)
- `[e2]` **ngày 01 tháng 7 năm 2016** → `NGAY_THAM_CHIEU` (span: `[4:10]`)
- `[e3]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[11:12]`)

**Quan hệ:**
- (`e1` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e0` Nghị định số 94/2016/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e3` Chính phủ `[CO_QUAN_THAM_QUYEN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e0` Nghị định số 94/2016/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e0` Nghị định số 94/2016/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e2` ngày 01 tháng 7 năm 2016 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #06_2023_TT-BKHĐT_163394#preamble_context_9 (Loại: `preamble_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[06/2023/TT-BKHĐT]`<SO_HIEU>`** của **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** . **[Căn cứ]`<TU_KHOA_PHAP_LY>`** **[Nghị định số 89/2022/NĐ-CP]`<THAM_CHIEU_PHAP_LY>`** **[ngày 28 tháng 10 năm 2022]`<NGAY_THAM_CHIEU>`** của **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** quy định chức năng , nhiệm vụ , quyền hạn và cơ cấu tổ chức của **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_THAM_QUYEN>`** ;

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **06/2023/TT-BKHĐT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[4:8]`)
- `[e3]` **Nghị định số 89/2022/NĐ-CP** → `THAM_CHIEU_PHAP_LY` (span: `[10:13]`)
- `[e4]` **Căn cứ** → `TU_KHOA_PHAP_LY` (span: `[9:10]`)
- `[e5]` **ngày 28 tháng 10 năm 2022** → `NGAY_THAM_CHIEU` (span: `[13:19]`)
- `[e6]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[20:21]`)
- `[e7]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_THAM_QUYEN` (span: `[31:35]`)

**Quan hệ:**
- (`e1` 06/2023/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 06/2023/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e4` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Nghị định số 89/2022/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 06/2023/TT-BKHĐT `[SO_HIEU]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Nghị định số 89/2022/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e3` Nghị định số 89/2022/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e5` ngày 28 tháng 10 năm 2022 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #06_2023_TT-BKHĐT_163394#preamble_standalone_10 (Loại: `preamble_standalone`)
> **[Căn cứ]`<TU_KHOA_PHAP_LY>`** **[Nghị định số 89/2022/NĐ-CP]`<THAM_CHIEU_PHAP_LY>`** **[ngày 28 tháng 10 năm 2022]`<NGAY_THAM_CHIEU>`** của **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** quy định chức năng , nhiệm vụ , quyền hạn và cơ cấu tổ chức của **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_THAM_QUYEN>`** ;

**Thực thể:**
- `[e0]` **Nghị định số 89/2022/NĐ-CP** → `THAM_CHIEU_PHAP_LY` (span: `[1:4]`)
- `[e1]` **Căn cứ** → `TU_KHOA_PHAP_LY` (span: `[0:1]`)
- `[e2]` **ngày 28 tháng 10 năm 2022** → `NGAY_THAM_CHIEU` (span: `[4:10]`)
- `[e3]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[11:12]`)
- `[e4]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_THAM_QUYEN` (span: `[22:26]`)

**Quan hệ:**
- (`e1` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e0` Nghị định số 89/2022/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e3` Chính phủ `[CO_QUAN_THAM_QUYEN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e0` Nghị định số 89/2022/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e0` Nghị định số 89/2022/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e2` ngày 28 tháng 10 năm 2022 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #06_2023_TT-BKHĐT_163394#preamble_context_11 (Loại: `preamble_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[06/2023/TT-BKHĐT]`<SO_HIEU>`** của **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** . **[Bộ trưởng Bộ Kế hoạch và Đầu tư]`<CO_QUAN_THAM_QUYEN>`** ban hành Thông tư quy định hệ thống chỉ tiêu thống kê **[ngành Thống kê]`<LINH_VUC>`** .

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **06/2023/TT-BKHĐT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[4:8]`)
- `[e3]` **ngành Thống kê** → `LINH_VUC` (span: `[20:22]`)
- `[e4]` **Bộ trưởng Bộ Kế hoạch và Đầu tư** → `CO_QUAN_THAM_QUYEN` (span: `[9:14]`)

**Quan hệ:**
- (`e1` 06/2023/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 06/2023/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 06/2023/TT-BKHĐT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` ngành Thống kê `[LINH_VUC]`)


---

### Mẫu #06_2023_TT-BKHĐT_163394#preamble_standalone_12 (Loại: `preamble_standalone`)
> **[Bộ trưởng Bộ Kế hoạch và Đầu tư]`<CO_QUAN_THAM_QUYEN>`** ban hành Thông tư quy định hệ thống chỉ tiêu thống kê **[ngành Thống kê]`<LINH_VUC>`** .

**Thực thể:**
- `[e0]` **ngành Thống kê** → `LINH_VUC` (span: `[11:13]`)
- `[e1]` **Bộ trưởng Bộ Kế hoạch và Đầu tư** → `CO_QUAN_THAM_QUYEN` (span: `[0:5]`)

**Quan hệ:**
- (`e1` Bộ trưởng Bộ Kế hoạch và Đầu tư `[CO_QUAN_THAM_QUYEN]`) ==[ **THUOC_LINH_VUC** ]==> (`e0` ngành Thống kê `[LINH_VUC]`)


---

### Mẫu #06_2023_TT-BKHĐT_163394#body_context_13 (Loại: `body_context`)
> **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[06/2023/TT-BKHĐT]`<SO_HIEU>`** . **[Điều 1 . Phạm vi điều chỉnh . Thông tư này quy định hệ thống chỉ tiêu thống kê **[ngành Thống kê]`<LINH_VUC>`** .]`<DIEU>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[5:6]`)
- `[e1]` **06/2023/TT-BKHĐT** → `SO_HIEU` (span: `[7:8]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[0:4]`)
- `[e3]` **Điều 1 . Phạm vi điều chỉnh . Thông tư này quy định hệ thống chỉ tiêu thống kê ngành Thống kê .** → `DIEU` (span: `[9:24]`)
- `[e4]` **ngành Thống kê** → `LINH_VUC` (span: `[21:23]`) *(lồng trong `e3` (`DIEU`))*

**Quan hệ:**
- (`e1` 06/2023/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 06/2023/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 1 . Phạm vi điều chỉnh . Thông tư này quy định hệ thống chỉ tiêu thống kê ngành Thống kê . `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 06/2023/TT-BKHĐT `[SO_HIEU]`)
- (`e1` 06/2023/TT-BKHĐT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e4` ngành Thống kê `[LINH_VUC]`)
- (`e3` Điều 1 . Phạm vi điều chỉnh . Thông tư này quy định hệ thống chỉ tiêu thống kê ngành Thống kê . `[DIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e4` ngành Thống kê `[LINH_VUC]`) *(Quan hệ lồng nhau)*


---

### Mẫu #06_2023_TT-BKHĐT_163394#body_context_14 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[06/2023/TT-BKHĐT]`<SO_HIEU>`** của **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** . **[Điều 2 . Đối tượng áp dụng]`<DIEU>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **06/2023/TT-BKHĐT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[4:8]`)
- `[e3]` **Điều 2 . Đối tượng áp dụng** → `DIEU` (span: `[9:14]`)

**Quan hệ:**
- (`e1` 06/2023/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 06/2023/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 2 . Đối tượng áp dụng `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 06/2023/TT-BKHĐT `[SO_HIEU]`)


---

### Mẫu #06_2023_TT-BKHĐT_163394#body_context_15 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[06/2023/TT-BKHĐT]`<SO_HIEU>`** ban hành **[ngày 02 tháng 10 năm 2023]`<NGAY_BAN_HANH>`** bởi **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** . **[Điều 2]`<DIEU>`** . **[1 . Cơ quan thống kê Trung ương .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **06/2023/TT-BKHĐT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[11:15]`)
- `[e3]` **ngày 02 tháng 10 năm 2023** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 2** → `DIEU` (span: `[16:18]`)
- `[e5]` **1 . Cơ quan thống kê Trung ương .** → `KHOAN` (span: `[19:25]`)

**Quan hệ:**
- (`e1` 06/2023/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 06/2023/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 06/2023/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 02 tháng 10 năm 2023 `[NGAY_BAN_HANH]`)
- (`e4` Điều 2 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 06/2023/TT-BKHĐT `[SO_HIEU]`)
- (`e5` 1 . Cơ quan thống kê Trung ương . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 2 `[DIEU]`)


---

### Mẫu #06_2023_TT-BKHĐT_163394#body_context_16 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[06/2023/TT-BKHĐT]`<SO_HIEU>`** của **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** . **[Điều 2]`<DIEU>`** . **[2 . Cơ quan thống kê địa phương .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **06/2023/TT-BKHĐT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[4:8]`)
- `[e3]` **Điều 2** → `DIEU` (span: `[9:11]`)
- `[e4]` **2 . Cơ quan thống kê địa phương .** → `KHOAN` (span: `[12:18]`)

**Quan hệ:**
- (`e1` 06/2023/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 06/2023/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 2 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 06/2023/TT-BKHĐT `[SO_HIEU]`)
- (`e4` 2 . Cơ quan thống kê địa phương . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 2 `[DIEU]`)


---

### Mẫu #06_2023_TT-BKHĐT_163394#body_context_17 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[06/2023/TT-BKHĐT]`<SO_HIEU>`** của **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** . **[Điều 2]`<DIEU>`** . **[3 . Các cơ quan , tổ chức khác có liên quan đến hệ thống chỉ tiêu thống kê **[ngành Thống kê]`<LINH_VUC>`** .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **06/2023/TT-BKHĐT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[4:8]`)
- `[e3]` **Điều 2** → `DIEU` (span: `[9:11]`)
- `[e4]` **3 . Các cơ quan , tổ chức khác có liên quan đến hệ thống chỉ tiêu thống kê ngành Thống kê .** → `KHOAN` (span: `[12:28]`)
- `[e5]` **ngành Thống kê** → `LINH_VUC` (span: `[25:27]`) *(lồng trong `e4` (`KHOAN`))*

**Quan hệ:**
- (`e1` 06/2023/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 06/2023/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 2 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 06/2023/TT-BKHĐT `[SO_HIEU]`)
- (`e4` 3 . Các cơ quan , tổ chức khác có liên quan đến hệ thống chỉ tiêu thống kê ngành Thống kê . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 2 `[DIEU]`)
- (`e1` 06/2023/TT-BKHĐT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e5` ngành Thống kê `[LINH_VUC]`)
- (`e4` 3 . Các cơ quan , tổ chức khác có liên quan đến hệ thống chỉ tiêu thống kê ngành Thống kê . `[KHOAN]`) ==[ **THUOC_LINH_VUC** ]==> (`e5` ngành Thống kê `[LINH_VUC]`) *(Quan hệ lồng nhau)*


---

### Mẫu #06_2023_TT-BKHĐT_163394#body_context_18 (Loại: `body_context`)
> **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[06/2023/TT-BKHĐT]`<SO_HIEU>`** . **[Điều 3 . Hệ thống chỉ tiêu thống kê **[ngành Thống kê]`<LINH_VUC>`** . Hệ thống chỉ tiêu thống kê **[ngành Thống kê]`<LINH_VUC>`** là tập hợp các chỉ tiêu thống kê do Hệ thống thống kê tập trung thực hiện phục vụ hoạt động thống kê và công tác quản lý chung của **[ngành Thống kê]`<LINH_VUC>`** . Hệ thống chỉ tiêu thống kê **[ngành Thống kê]`<LINH_VUC>`** gồm :]`<DIEU>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[5:6]`)
- `[e1]` **06/2023/TT-BKHĐT** → `SO_HIEU` (span: `[7:8]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[0:4]`)
- `[e3]` **Điều 3 . Hệ thống chỉ tiêu thống kê ngành Thống kê . Hệ thống chỉ tiêu thống kê ngành Thống kê là tập hợp các chỉ tiêu thống kê do Hệ thống thống kê tập trung thực hiện phục vụ hoạt động thống kê và công tác quản lý chung của ngành Thống kê . Hệ thống chỉ tiêu thống kê ngành Thống kê gồm :** → `DIEU` (span: `[9:50]`)
- `[e4]` **ngành Thống kê** → `LINH_VUC` (span: `[15:17]`) *(lồng trong `e3` (`DIEU`))*
- `[e5]` **ngành Thống kê** → `LINH_VUC` (span: `[21:23]`) *(lồng trong `e3` (`DIEU`))*
- `[e6]` **ngành Thống kê** → `LINH_VUC` (span: `[40:42]`) *(lồng trong `e3` (`DIEU`))*
- `[e7]` **ngành Thống kê** → `LINH_VUC` (span: `[46:48]`) *(lồng trong `e3` (`DIEU`))*

**Quan hệ:**
- (`e1` 06/2023/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 06/2023/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 3 . Hệ thống chỉ tiêu thống kê ngành Thống kê . Hệ thống chỉ tiêu thống kê ngành Thống kê là tập hợp các chỉ tiêu thống kê do Hệ thống thống kê tập trung thực hiện phục vụ hoạt động thống kê và công tác quản lý chung của ngành Thống kê . Hệ thống chỉ tiêu thống kê ngành Thống kê gồm : `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 06/2023/TT-BKHĐT `[SO_HIEU]`)
- (`e1` 06/2023/TT-BKHĐT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e4` ngành Thống kê `[LINH_VUC]`)
- (`e3` Điều 3 . Hệ thống chỉ tiêu thống kê ngành Thống kê . Hệ thống chỉ tiêu thống kê ngành Thống kê là tập hợp các chỉ tiêu thống kê do Hệ thống thống kê tập trung thực hiện phục vụ hoạt động thống kê và công tác quản lý chung của ngành Thống kê . Hệ thống chỉ tiêu thống kê ngành Thống kê gồm : `[DIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e4` ngành Thống kê `[LINH_VUC]`) *(Quan hệ lồng nhau)*
- (`e1` 06/2023/TT-BKHĐT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e5` ngành Thống kê `[LINH_VUC]`)
- (`e3` Điều 3 . Hệ thống chỉ tiêu thống kê ngành Thống kê . Hệ thống chỉ tiêu thống kê ngành Thống kê là tập hợp các chỉ tiêu thống kê do Hệ thống thống kê tập trung thực hiện phục vụ hoạt động thống kê và công tác quản lý chung của ngành Thống kê . Hệ thống chỉ tiêu thống kê ngành Thống kê gồm : `[DIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e5` ngành Thống kê `[LINH_VUC]`) *(Quan hệ lồng nhau)*
- (`e1` 06/2023/TT-BKHĐT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e6` ngành Thống kê `[LINH_VUC]`)
- (`e3` Điều 3 . Hệ thống chỉ tiêu thống kê ngành Thống kê . Hệ thống chỉ tiêu thống kê ngành Thống kê là tập hợp các chỉ tiêu thống kê do Hệ thống thống kê tập trung thực hiện phục vụ hoạt động thống kê và công tác quản lý chung của ngành Thống kê . Hệ thống chỉ tiêu thống kê ngành Thống kê gồm : `[DIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e6` ngành Thống kê `[LINH_VUC]`) *(Quan hệ lồng nhau)*
- (`e1` 06/2023/TT-BKHĐT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e7` ngành Thống kê `[LINH_VUC]`)
- (`e3` Điều 3 . Hệ thống chỉ tiêu thống kê ngành Thống kê . Hệ thống chỉ tiêu thống kê ngành Thống kê là tập hợp các chỉ tiêu thống kê do Hệ thống thống kê tập trung thực hiện phục vụ hoạt động thống kê và công tác quản lý chung của ngành Thống kê . Hệ thống chỉ tiêu thống kê ngành Thống kê gồm : `[DIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e7` ngành Thống kê `[LINH_VUC]`) *(Quan hệ lồng nhau)*


---

### Mẫu #06_2023_TT-BKHĐT_163394#body_standalone_19 (Loại: `body_standalone`)
> **[Điều 3 . Hệ thống chỉ tiêu thống kê **[ngành Thống kê]`<LINH_VUC>`** . Hệ thống chỉ tiêu thống kê **[ngành Thống kê]`<LINH_VUC>`** là tập hợp các chỉ tiêu thống kê do Hệ thống thống kê tập trung thực hiện phục vụ hoạt động thống kê và công tác quản lý chung của **[ngành Thống kê]`<LINH_VUC>`** . Hệ thống chỉ tiêu thống kê **[ngành Thống kê]`<LINH_VUC>`** gồm :]`<DIEU>`**

**Thực thể:**
- `[e0]` **Điều 3 . Hệ thống chỉ tiêu thống kê ngành Thống kê . Hệ thống chỉ tiêu thống kê ngành Thống kê là tập hợp các chỉ tiêu thống kê do Hệ thống thống kê tập trung thực hiện phục vụ hoạt động thống kê và công tác quản lý chung của ngành Thống kê . Hệ thống chỉ tiêu thống kê ngành Thống kê gồm :** → `DIEU` (span: `[0:41]`)
- `[e1]` **ngành Thống kê** → `LINH_VUC` (span: `[6:8]`) *(lồng trong `e0` (`DIEU`))*
- `[e2]` **ngành Thống kê** → `LINH_VUC` (span: `[12:14]`) *(lồng trong `e0` (`DIEU`))*
- `[e3]` **ngành Thống kê** → `LINH_VUC` (span: `[31:33]`) *(lồng trong `e0` (`DIEU`))*
- `[e4]` **ngành Thống kê** → `LINH_VUC` (span: `[37:39]`) *(lồng trong `e0` (`DIEU`))*

**Quan hệ:**
- (`e0` Điều 3 . Hệ thống chỉ tiêu thống kê ngành Thống kê . Hệ thống chỉ tiêu thống kê ngành Thống kê là tập hợp các chỉ tiêu thống kê do Hệ thống thống kê tập trung thực hiện phục vụ hoạt động thống kê và công tác quản lý chung của ngành Thống kê . Hệ thống chỉ tiêu thống kê ngành Thống kê gồm : `[DIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e1` ngành Thống kê `[LINH_VUC]`) *(Quan hệ lồng nhau)*
- (`e0` Điều 3 . Hệ thống chỉ tiêu thống kê ngành Thống kê . Hệ thống chỉ tiêu thống kê ngành Thống kê là tập hợp các chỉ tiêu thống kê do Hệ thống thống kê tập trung thực hiện phục vụ hoạt động thống kê và công tác quản lý chung của ngành Thống kê . Hệ thống chỉ tiêu thống kê ngành Thống kê gồm : `[DIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e2` ngành Thống kê `[LINH_VUC]`) *(Quan hệ lồng nhau)*
- (`e0` Điều 3 . Hệ thống chỉ tiêu thống kê ngành Thống kê . Hệ thống chỉ tiêu thống kê ngành Thống kê là tập hợp các chỉ tiêu thống kê do Hệ thống thống kê tập trung thực hiện phục vụ hoạt động thống kê và công tác quản lý chung của ngành Thống kê . Hệ thống chỉ tiêu thống kê ngành Thống kê gồm : `[DIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` ngành Thống kê `[LINH_VUC]`) *(Quan hệ lồng nhau)*
- (`e0` Điều 3 . Hệ thống chỉ tiêu thống kê ngành Thống kê . Hệ thống chỉ tiêu thống kê ngành Thống kê là tập hợp các chỉ tiêu thống kê do Hệ thống thống kê tập trung thực hiện phục vụ hoạt động thống kê và công tác quản lý chung của ngành Thống kê . Hệ thống chỉ tiêu thống kê ngành Thống kê gồm : `[DIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e4` ngành Thống kê `[LINH_VUC]`) *(Quan hệ lồng nhau)*


---

### Mẫu #06_2023_TT-BKHĐT_163394#body_context_20 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[06/2023/TT-BKHĐT]`<SO_HIEU>`** của **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** . **[Điều 3]`<DIEU>`** . **[a ) Danh mục chỉ tiêu thống kê **[ngành Thống kê]`<LINH_VUC>`** gồm số thứ tự ; mã số ; nhóm , tên chỉ tiêu được **[quy định tại]`<TU_KHOA_PHAP_LY>`** **[Phụ lục I ban hành kèm theo Thông tư này]`<THAM_CHIEU_PHAP_LY>`** .]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **06/2023/TT-BKHĐT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[4:8]`)
- `[e3]` **Điều 3** → `DIEU` (span: `[9:11]`)
- `[e4]` **a ) Danh mục chỉ tiêu thống kê ngành Thống kê gồm số thứ tự ; mã số ; nhóm , tên chỉ tiêu được quy định tại Phụ lục I ban hành kèm theo Thông tư này .** → `DIEM` (span: `[12:40]`)
- `[e5]` **Phụ lục I ban hành kèm theo Thông tư này** → `THAM_CHIEU_PHAP_LY` (span: `[32:39]`) *(lồng trong `e4` (`DIEM`))*
- `[e6]` **quy định tại** → `TU_KHOA_PHAP_LY` (span: `[30:32]`) *(lồng trong `e4` (`DIEM`))*
- `[e7]` **ngành Thống kê** → `LINH_VUC` (span: `[17:19]`) *(lồng trong `e4` (`DIEM`))*

**Quan hệ:**
- (`e1` 06/2023/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 06/2023/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 3 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 06/2023/TT-BKHĐT `[SO_HIEU]`)
- (`e6` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e5` Phụ lục I ban hành kèm theo Thông tư này `[THAM_CHIEU_PHAP_LY]`)
- (`e4` a ) Danh mục chỉ tiêu thống kê ngành Thống kê gồm số thứ tự ; mã số ; nhóm , tên chỉ tiêu được quy định tại Phụ lục I ban hành kèm theo Thông tư này . `[DIEM]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e5` Phụ lục I ban hành kèm theo Thông tư này `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e1` 06/2023/TT-BKHĐT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e7` ngành Thống kê `[LINH_VUC]`)
- (`e4` a ) Danh mục chỉ tiêu thống kê ngành Thống kê gồm số thứ tự ; mã số ; nhóm , tên chỉ tiêu được quy định tại Phụ lục I ban hành kèm theo Thông tư này . `[DIEM]`) ==[ **THUOC_LINH_VUC** ]==> (`e7` ngành Thống kê `[LINH_VUC]`) *(Quan hệ lồng nhau)*


---

### Mẫu #06_2023_TT-BKHĐT_163394#body_standalone_21 (Loại: `body_standalone`)
> **[Điều 3]`<DIEU>`** . **[a ) Danh mục chỉ tiêu thống kê **[ngành Thống kê]`<LINH_VUC>`** gồm số thứ tự ; mã số ; nhóm , tên chỉ tiêu được **[quy định tại]`<TU_KHOA_PHAP_LY>`** **[Phụ lục I ban hành kèm theo Thông tư này]`<THAM_CHIEU_PHAP_LY>`** .]`<DIEM>`**

**Thực thể:**
- `[e0]` **Điều 3** → `DIEU` (span: `[0:2]`)
- `[e1]` **a ) Danh mục chỉ tiêu thống kê ngành Thống kê gồm số thứ tự ; mã số ; nhóm , tên chỉ tiêu được quy định tại Phụ lục I ban hành kèm theo Thông tư này .** → `DIEM` (span: `[3:31]`)
- `[e2]` **Phụ lục I ban hành kèm theo Thông tư này** → `THAM_CHIEU_PHAP_LY` (span: `[23:30]`) *(lồng trong `e1` (`DIEM`))*
- `[e3]` **quy định tại** → `TU_KHOA_PHAP_LY` (span: `[21:23]`) *(lồng trong `e1` (`DIEM`))*
- `[e4]` **ngành Thống kê** → `LINH_VUC` (span: `[8:10]`) *(lồng trong `e1` (`DIEM`))*

**Quan hệ:**
- (`e3` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e2` Phụ lục I ban hành kèm theo Thông tư này `[THAM_CHIEU_PHAP_LY]`)
- (`e1` a ) Danh mục chỉ tiêu thống kê ngành Thống kê gồm số thứ tự ; mã số ; nhóm , tên chỉ tiêu được quy định tại Phụ lục I ban hành kèm theo Thông tư này . `[DIEM]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e2` Phụ lục I ban hành kèm theo Thông tư này `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e1` a ) Danh mục chỉ tiêu thống kê ngành Thống kê gồm số thứ tự ; mã số ; nhóm , tên chỉ tiêu được quy định tại Phụ lục I ban hành kèm theo Thông tư này . `[DIEM]`) ==[ **THUOC_LINH_VUC** ]==> (`e4` ngành Thống kê `[LINH_VUC]`) *(Quan hệ lồng nhau)*


---

### Mẫu #06_2023_TT-BKHĐT_163394#body_context_22 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[06/2023/TT-BKHĐT]`<SO_HIEU>`** của **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** . **[Điều 3]`<DIEU>`** . **[b ) Nội dung chỉ tiêu thống kê **[ngành Thống kê]`<LINH_VUC>`** gồm khái niệm , phương pháp tính , phân tổ chủ yếu , kỳ công bố , nguồn số liệu và đơn vị chịu trách nhiệm thu thập , tổng hợp được **[quy định tại]`<TU_KHOA_PHAP_LY>`** **[Phụ lục II ban hành kèm theo Thông tư này]`<THAM_CHIEU_PHAP_LY>`** . "]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **06/2023/TT-BKHĐT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[4:8]`)
- `[e3]` **Điều 3** → `DIEU` (span: `[9:11]`)
- `[e4]` **b ) Nội dung chỉ tiêu thống kê ngành Thống kê gồm khái niệm , phương pháp tính , phân tổ chủ yếu , kỳ công bố , nguồn số liệu và đơn vị chịu trách nhiệm thu thập , tổng hợp được quy định tại Phụ lục II ban hành kèm theo Thông tư này . "** → `DIEM` (span: `[12:52]`)
- `[e5]` **Phụ lục II ban hành kèm theo Thông tư này** → `THAM_CHIEU_PHAP_LY` (span: `[43:50]`) *(lồng trong `e4` (`DIEM`))*
- `[e6]` **quy định tại** → `TU_KHOA_PHAP_LY` (span: `[41:43]`) *(lồng trong `e4` (`DIEM`))*
- `[e7]` **ngành Thống kê** → `LINH_VUC` (span: `[17:19]`) *(lồng trong `e4` (`DIEM`))*

**Quan hệ:**
- (`e1` 06/2023/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 06/2023/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 3 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 06/2023/TT-BKHĐT `[SO_HIEU]`)
- (`e6` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e5` Phụ lục II ban hành kèm theo Thông tư này `[THAM_CHIEU_PHAP_LY]`)
- (`e4` b ) Nội dung chỉ tiêu thống kê ngành Thống kê gồm khái niệm , phương pháp tính , phân tổ chủ yếu , kỳ công bố , nguồn số liệu và đơn vị chịu trách nhiệm thu thập , tổng hợp được quy định tại Phụ lục II ban hành kèm theo Thông tư này . " `[DIEM]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e5` Phụ lục II ban hành kèm theo Thông tư này `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e1` 06/2023/TT-BKHĐT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e7` ngành Thống kê `[LINH_VUC]`)
- (`e4` b ) Nội dung chỉ tiêu thống kê ngành Thống kê gồm khái niệm , phương pháp tính , phân tổ chủ yếu , kỳ công bố , nguồn số liệu và đơn vị chịu trách nhiệm thu thập , tổng hợp được quy định tại Phụ lục II ban hành kèm theo Thông tư này . " `[DIEM]`) ==[ **THUOC_LINH_VUC** ]==> (`e7` ngành Thống kê `[LINH_VUC]`) *(Quan hệ lồng nhau)*


---

### Mẫu #06_2023_TT-BKHĐT_163394#body_standalone_23 (Loại: `body_standalone`)
> **[Điều 3]`<DIEU>`** . **[b ) Nội dung chỉ tiêu thống kê **[ngành Thống kê]`<LINH_VUC>`** gồm khái niệm , phương pháp tính , phân tổ chủ yếu , kỳ công bố , nguồn số liệu và đơn vị chịu trách nhiệm thu thập , tổng hợp được **[quy định tại]`<TU_KHOA_PHAP_LY>`** **[Phụ lục II ban hành kèm theo Thông tư này]`<THAM_CHIEU_PHAP_LY>`** . "]`<DIEM>`**

**Thực thể:**
- `[e0]` **Điều 3** → `DIEU` (span: `[0:2]`)
- `[e1]` **b ) Nội dung chỉ tiêu thống kê ngành Thống kê gồm khái niệm , phương pháp tính , phân tổ chủ yếu , kỳ công bố , nguồn số liệu và đơn vị chịu trách nhiệm thu thập , tổng hợp được quy định tại Phụ lục II ban hành kèm theo Thông tư này . "** → `DIEM` (span: `[3:43]`)
- `[e2]` **Phụ lục II ban hành kèm theo Thông tư này** → `THAM_CHIEU_PHAP_LY` (span: `[34:41]`) *(lồng trong `e1` (`DIEM`))*
- `[e3]` **quy định tại** → `TU_KHOA_PHAP_LY` (span: `[32:34]`) *(lồng trong `e1` (`DIEM`))*
- `[e4]` **ngành Thống kê** → `LINH_VUC` (span: `[8:10]`) *(lồng trong `e1` (`DIEM`))*

**Quan hệ:**
- (`e3` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e2` Phụ lục II ban hành kèm theo Thông tư này `[THAM_CHIEU_PHAP_LY]`)
- (`e1` b ) Nội dung chỉ tiêu thống kê ngành Thống kê gồm khái niệm , phương pháp tính , phân tổ chủ yếu , kỳ công bố , nguồn số liệu và đơn vị chịu trách nhiệm thu thập , tổng hợp được quy định tại Phụ lục II ban hành kèm theo Thông tư này . " `[DIEM]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e2` Phụ lục II ban hành kèm theo Thông tư này `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e1` b ) Nội dung chỉ tiêu thống kê ngành Thống kê gồm khái niệm , phương pháp tính , phân tổ chủ yếu , kỳ công bố , nguồn số liệu và đơn vị chịu trách nhiệm thu thập , tổng hợp được quy định tại Phụ lục II ban hành kèm theo Thông tư này . " `[DIEM]`) ==[ **THUOC_LINH_VUC** ]==> (`e4` ngành Thống kê `[LINH_VUC]`) *(Quan hệ lồng nhau)*


---

### Mẫu #06_2023_TT-BKHĐT_163394#body_context_24 (Loại: `body_context`)
> **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[06/2023/TT-BKHĐT]`<SO_HIEU>`** . **[Điều 4 . Tổ chức thực hiện]`<DIEU>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[5:6]`)
- `[e1]` **06/2023/TT-BKHĐT** → `SO_HIEU` (span: `[7:8]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[0:4]`)
- `[e3]` **Điều 4 . Tổ chức thực hiện** → `DIEU` (span: `[9:14]`)

**Quan hệ:**
- (`e1` 06/2023/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 06/2023/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 4 . Tổ chức thực hiện `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 06/2023/TT-BKHĐT `[SO_HIEU]`)


---

### Mẫu #06_2023_TT-BKHĐT_163394#body_context_25 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[06/2023/TT-BKHĐT]`<SO_HIEU>`** ban hành **[ngày 02 tháng 10 năm 2023]`<NGAY_BAN_HANH>`** bởi **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** . **[Điều 4]`<DIEU>`** . **[1 . Tổng cục Thống kê chủ trì , phối hợp với các đơn vị liên quan lồng ghép việc thu thập chỉ tiêu vào chế độ báo cáo thống kê **[ngành Thống kê]`<LINH_VUC>`** trình Bộ trưởng ban hành ; chủ trì tổ chức các cuộc điều tra thống kê và phối hợp với các đơn vị liên quan sử dụng dữ liệu hành chính thuộc phạm vi quản lý của Bộ nhằm phục vụ thu thập , tổng hợp thông tin thống kê thuộc các chỉ tiêu thống kê **[ngành Thống kê]`<LINH_VUC>`** ; chủ trì tổng]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **06/2023/TT-BKHĐT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[11:15]`)
- `[e3]` **ngày 02 tháng 10 năm 2023** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 4** → `DIEU` (span: `[16:18]`)
- `[e5]` **1 . Tổng cục Thống kê chủ trì , phối hợp với các đơn vị liên quan lồng ghép việc thu thập chỉ tiêu vào chế độ báo cáo thống kê ngành Thống kê trình Bộ trưởng ban hành ; chủ trì tổ chức các cuộc điều tra thống kê và phối hợp với các đơn vị liên quan sử dụng dữ liệu hành chính thuộc phạm vi quản lý của Bộ nhằm phục vụ thu thập , tổng hợp thông tin thống kê thuộc các chỉ tiêu thống kê ngành Thống kê ; chủ trì tổng** → `KHOAN` (span: `[19:80]`)
- `[e6]` **ngành Thống kê** → `LINH_VUC` (span: `[38:40]`) *(lồng trong `e5` (`KHOAN`))*
- `[e7]` **ngành Thống kê** → `LINH_VUC` (span: `[75:77]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 06/2023/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 06/2023/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 06/2023/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 02 tháng 10 năm 2023 `[NGAY_BAN_HANH]`)
- (`e4` Điều 4 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 06/2023/TT-BKHĐT `[SO_HIEU]`)
- (`e5` 1 . Tổng cục Thống kê chủ trì , phối hợp với các đơn vị liên quan lồng ghép việc thu thập chỉ tiêu vào chế độ báo cáo thống kê ngành Thống kê trình Bộ trưởng ban hành ; chủ trì tổ chức các cuộc điều tra thống kê và phối hợp với các đơn vị liên quan sử dụng dữ liệu hành chính thuộc phạm vi quản lý của Bộ nhằm phục vụ thu thập , tổng hợp thông tin thống kê thuộc các chỉ tiêu thống kê ngành Thống kê ; chủ trì tổng `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 4 `[DIEU]`)
- (`e1` 06/2023/TT-BKHĐT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e6` ngành Thống kê `[LINH_VUC]`)
- (`e5` 1 . Tổng cục Thống kê chủ trì , phối hợp với các đơn vị liên quan lồng ghép việc thu thập chỉ tiêu vào chế độ báo cáo thống kê ngành Thống kê trình Bộ trưởng ban hành ; chủ trì tổ chức các cuộc điều tra thống kê và phối hợp với các đơn vị liên quan sử dụng dữ liệu hành chính thuộc phạm vi quản lý của Bộ nhằm phục vụ thu thập , tổng hợp thông tin thống kê thuộc các chỉ tiêu thống kê ngành Thống kê ; chủ trì tổng `[KHOAN]`) ==[ **THUOC_LINH_VUC** ]==> (`e6` ngành Thống kê `[LINH_VUC]`) *(Quan hệ lồng nhau)*
- (`e1` 06/2023/TT-BKHĐT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e7` ngành Thống kê `[LINH_VUC]`)
- (`e5` 1 . Tổng cục Thống kê chủ trì , phối hợp với các đơn vị liên quan lồng ghép việc thu thập chỉ tiêu vào chế độ báo cáo thống kê ngành Thống kê trình Bộ trưởng ban hành ; chủ trì tổ chức các cuộc điều tra thống kê và phối hợp với các đơn vị liên quan sử dụng dữ liệu hành chính thuộc phạm vi quản lý của Bộ nhằm phục vụ thu thập , tổng hợp thông tin thống kê thuộc các chỉ tiêu thống kê ngành Thống kê ; chủ trì tổng `[KHOAN]`) ==[ **THUOC_LINH_VUC** ]==> (`e7` ngành Thống kê `[LINH_VUC]`) *(Quan hệ lồng nhau)*


---

### Mẫu #06_2023_TT-BKHĐT_163394#body_standalone_26 (Loại: `body_standalone`)
> **[Điều 4]`<DIEU>`** . **[1 . Tổng cục Thống kê chủ trì , phối hợp với các đơn vị liên quan lồng ghép việc thu thập chỉ tiêu vào chế độ báo cáo thống kê **[ngành Thống kê]`<LINH_VUC>`** trình Bộ trưởng ban hành ; chủ trì tổ chức các cuộc điều tra thống kê và phối hợp với các đơn vị liên quan sử dụng dữ liệu hành chính thuộc phạm vi quản lý của Bộ nhằm phục vụ thu thập , tổng hợp thông tin thống kê thuộc các chỉ tiêu thống kê **[ngành Thống kê]`<LINH_VUC>`** ; chủ trì tổng]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 4** → `DIEU` (span: `[0:2]`)
- `[e1]` **1 . Tổng cục Thống kê chủ trì , phối hợp với các đơn vị liên quan lồng ghép việc thu thập chỉ tiêu vào chế độ báo cáo thống kê ngành Thống kê trình Bộ trưởng ban hành ; chủ trì tổ chức các cuộc điều tra thống kê và phối hợp với các đơn vị liên quan sử dụng dữ liệu hành chính thuộc phạm vi quản lý của Bộ nhằm phục vụ thu thập , tổng hợp thông tin thống kê thuộc các chỉ tiêu thống kê ngành Thống kê ; chủ trì tổng** → `KHOAN` (span: `[3:64]`)
- `[e2]` **ngành Thống kê** → `LINH_VUC` (span: `[22:24]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **ngành Thống kê** → `LINH_VUC` (span: `[59:61]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 1 . Tổng cục Thống kê chủ trì , phối hợp với các đơn vị liên quan lồng ghép việc thu thập chỉ tiêu vào chế độ báo cáo thống kê ngành Thống kê trình Bộ trưởng ban hành ; chủ trì tổ chức các cuộc điều tra thống kê và phối hợp với các đơn vị liên quan sử dụng dữ liệu hành chính thuộc phạm vi quản lý của Bộ nhằm phục vụ thu thập , tổng hợp thông tin thống kê thuộc các chỉ tiêu thống kê ngành Thống kê ; chủ trì tổng `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 4 `[DIEU]`)
- (`e1` 1 . Tổng cục Thống kê chủ trì , phối hợp với các đơn vị liên quan lồng ghép việc thu thập chỉ tiêu vào chế độ báo cáo thống kê ngành Thống kê trình Bộ trưởng ban hành ; chủ trì tổ chức các cuộc điều tra thống kê và phối hợp với các đơn vị liên quan sử dụng dữ liệu hành chính thuộc phạm vi quản lý của Bộ nhằm phục vụ thu thập , tổng hợp thông tin thống kê thuộc các chỉ tiêu thống kê ngành Thống kê ; chủ trì tổng `[KHOAN]`) ==[ **THUOC_LINH_VUC** ]==> (`e2` ngành Thống kê `[LINH_VUC]`) *(Quan hệ lồng nhau)*
- (`e1` 1 . Tổng cục Thống kê chủ trì , phối hợp với các đơn vị liên quan lồng ghép việc thu thập chỉ tiêu vào chế độ báo cáo thống kê ngành Thống kê trình Bộ trưởng ban hành ; chủ trì tổ chức các cuộc điều tra thống kê và phối hợp với các đơn vị liên quan sử dụng dữ liệu hành chính thuộc phạm vi quản lý của Bộ nhằm phục vụ thu thập , tổng hợp thông tin thống kê thuộc các chỉ tiêu thống kê ngành Thống kê ; chủ trì tổng `[KHOAN]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` ngành Thống kê `[LINH_VUC]`) *(Quan hệ lồng nhau)*


---

### Mẫu #06_2023_TT-BKHĐT_163394#body_context_27 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[06/2023/TT-BKHĐT]`<SO_HIEU>`** ban hành **[ngày 02 tháng 10 năm 2023]`<NGAY_BAN_HANH>`** bởi **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** . **[Điều 4]`<DIEU>`** . **[2 . Thủ trưởng các đơn vị thuộc **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_THAM_QUYEN>`** ( Tổng cục Thống kê ) và các đơn vị có liên quan chịu trách nhiệm thi hành Thông tư này .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **06/2023/TT-BKHĐT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[11:15]`)
- `[e3]` **ngày 02 tháng 10 năm 2023** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 4** → `DIEU` (span: `[16:18]`)
- `[e5]` **2 . Thủ trưởng các đơn vị thuộc Bộ Kế hoạch và Đầu tư ( Tổng cục Thống kê ) và các đơn vị có liên quan chịu trách nhiệm thi hành Thông tư này .** → `KHOAN` (span: `[19:44]`)
- `[e6]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_THAM_QUYEN` (span: `[25:29]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 06/2023/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 06/2023/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 06/2023/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 02 tháng 10 năm 2023 `[NGAY_BAN_HANH]`)
- (`e4` Điều 4 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 06/2023/TT-BKHĐT `[SO_HIEU]`)
- (`e5` 2 . Thủ trưởng các đơn vị thuộc Bộ Kế hoạch và Đầu tư ( Tổng cục Thống kê ) và các đơn vị có liên quan chịu trách nhiệm thi hành Thông tư này . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 4 `[DIEU]`)


---

### Mẫu #06_2023_TT-BKHĐT_163394#body_standalone_28 (Loại: `body_standalone`)
> **[Điều 4]`<DIEU>`** . **[2 . Thủ trưởng các đơn vị thuộc **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_THAM_QUYEN>`** ( Tổng cục Thống kê ) và các đơn vị có liên quan chịu trách nhiệm thi hành Thông tư này .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 4** → `DIEU` (span: `[0:2]`)
- `[e1]` **2 . Thủ trưởng các đơn vị thuộc Bộ Kế hoạch và Đầu tư ( Tổng cục Thống kê ) và các đơn vị có liên quan chịu trách nhiệm thi hành Thông tư này .** → `KHOAN` (span: `[3:28]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_THAM_QUYEN` (span: `[9:13]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 2 . Thủ trưởng các đơn vị thuộc Bộ Kế hoạch và Đầu tư ( Tổng cục Thống kê ) và các đơn vị có liên quan chịu trách nhiệm thi hành Thông tư này . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 4 `[DIEU]`)


---

### Mẫu #06_2023_TT-BKHĐT_163394#body_context_29 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[06/2023/TT-BKHĐT]`<SO_HIEU>`** ban hành **[ngày 02 tháng 10 năm 2023]`<NGAY_BAN_HANH>`** bởi **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** . **[Điều 5 . Hiệu lực thi hành]`<DIEU>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **06/2023/TT-BKHĐT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[11:15]`)
- `[e3]` **ngày 02 tháng 10 năm 2023** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 5 . Hiệu lực thi hành** → `DIEU` (span: `[16:21]`)

**Quan hệ:**
- (`e1` 06/2023/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 06/2023/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 06/2023/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 02 tháng 10 năm 2023 `[NGAY_BAN_HANH]`)
- (`e4` Điều 5 . Hiệu lực thi hành `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 06/2023/TT-BKHĐT `[SO_HIEU]`)


---

### Mẫu #06_2023_TT-BKHĐT_163394#body_context_30 (Loại: `body_context`)
> **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[06/2023/TT-BKHĐT]`<SO_HIEU>`** . **[Điều 5]`<DIEU>`** . **[1 . Thông tư này có hiệu lực thi hành kể từ ngày 01 tháng 01 năm 2024 . Những chỉ tiêu phân công cho Tổng cục Thống kê chủ trì thu thập **[quy định tại]`<TU_KHOA_PHAP_LY>`** **[Thông tư số 05/2017/TT-BKHĐT]`<THAM_CHIEU_PHAP_LY>`** **[ngày 30/11/2017]`<NGAY_THAM_CHIEU>`** của **[Bộ trưởng Bộ Kế hoạch và Đầu tư]`<CO_QUAN_THAM_QUYEN>`** hết hiệu lực kể từ khi Thông tư này có hiệu lực .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[5:6]`)
- `[e1]` **06/2023/TT-BKHĐT** → `SO_HIEU` (span: `[7:8]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[0:4]`)
- `[e3]` **Điều 5** → `DIEU` (span: `[9:11]`)
- `[e4]` **1 . Thông tư này có hiệu lực thi hành kể từ ngày 01 tháng 01 năm 2024 . Những chỉ tiêu phân công cho Tổng cục Thống kê chủ trì thu thập quy định tại Thông tư số 05/2017/TT-BKHĐT ngày 30/11/2017 của Bộ trưởng Bộ Kế hoạch và Đầu tư hết hiệu lực kể từ khi Thông tư này có hiệu lực .** → `KHOAN` (span: `[12:59]`)
- `[e5]` **Thông tư số 05/2017/TT-BKHĐT** → `THAM_CHIEU_PHAP_LY` (span: `[38:41]`) *(lồng trong `e4` (`KHOAN`))*
- `[e6]` **quy định tại** → `TU_KHOA_PHAP_LY` (span: `[36:38]`) *(lồng trong `e4` (`KHOAN`))*
- `[e7]` **ngày 30/11/2017** → `NGAY_THAM_CHIEU` (span: `[41:43]`) *(lồng trong `e4` (`KHOAN`))*
- `[e8]` **Bộ trưởng Bộ Kế hoạch và Đầu tư** → `CO_QUAN_THAM_QUYEN` (span: `[44:49]`) *(lồng trong `e4` (`KHOAN`))*

**Quan hệ:**
- (`e1` 06/2023/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 06/2023/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 5 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 06/2023/TT-BKHĐT `[SO_HIEU]`)
- (`e4` 1 . Thông tư này có hiệu lực thi hành kể từ ngày 01 tháng 01 năm 2024 . Những chỉ tiêu phân công cho Tổng cục Thống kê chủ trì thu thập quy định tại Thông tư số 05/2017/TT-BKHĐT ngày 30/11/2017 của Bộ trưởng Bộ Kế hoạch và Đầu tư hết hiệu lực kể từ khi Thông tư này có hiệu lực . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 5 `[DIEU]`)
- (`e6` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e5` Thông tư số 05/2017/TT-BKHĐT `[THAM_CHIEU_PHAP_LY]`)
- (`e4` 1 . Thông tư này có hiệu lực thi hành kể từ ngày 01 tháng 01 năm 2024 . Những chỉ tiêu phân công cho Tổng cục Thống kê chủ trì thu thập quy định tại Thông tư số 05/2017/TT-BKHĐT ngày 30/11/2017 của Bộ trưởng Bộ Kế hoạch và Đầu tư hết hiệu lực kể từ khi Thông tư này có hiệu lực . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e5` Thông tư số 05/2017/TT-BKHĐT `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e5` Thông tư số 05/2017/TT-BKHĐT `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e7` ngày 30/11/2017 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #06_2023_TT-BKHĐT_163394#body_standalone_31 (Loại: `body_standalone`)
> **[Điều 5]`<DIEU>`** . **[1 . Thông tư này có hiệu lực thi hành kể từ ngày 01 tháng 01 năm 2024 . Những chỉ tiêu phân công cho Tổng cục Thống kê chủ trì thu thập **[quy định tại]`<TU_KHOA_PHAP_LY>`** **[Thông tư số 05/2017/TT-BKHĐT]`<THAM_CHIEU_PHAP_LY>`** **[ngày 30/11/2017]`<NGAY_THAM_CHIEU>`** của **[Bộ trưởng Bộ Kế hoạch và Đầu tư]`<CO_QUAN_THAM_QUYEN>`** hết hiệu lực kể từ khi Thông tư này có hiệu lực .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 5** → `DIEU` (span: `[0:2]`)
- `[e1]` **1 . Thông tư này có hiệu lực thi hành kể từ ngày 01 tháng 01 năm 2024 . Những chỉ tiêu phân công cho Tổng cục Thống kê chủ trì thu thập quy định tại Thông tư số 05/2017/TT-BKHĐT ngày 30/11/2017 của Bộ trưởng Bộ Kế hoạch và Đầu tư hết hiệu lực kể từ khi Thông tư này có hiệu lực .** → `KHOAN` (span: `[3:50]`)
- `[e2]` **Thông tư số 05/2017/TT-BKHĐT** → `THAM_CHIEU_PHAP_LY` (span: `[29:32]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **quy định tại** → `TU_KHOA_PHAP_LY` (span: `[27:29]`) *(lồng trong `e1` (`KHOAN`))*
- `[e4]` **ngày 30/11/2017** → `NGAY_THAM_CHIEU` (span: `[32:34]`) *(lồng trong `e1` (`KHOAN`))*
- `[e5]` **Bộ trưởng Bộ Kế hoạch và Đầu tư** → `CO_QUAN_THAM_QUYEN` (span: `[35:40]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 1 . Thông tư này có hiệu lực thi hành kể từ ngày 01 tháng 01 năm 2024 . Những chỉ tiêu phân công cho Tổng cục Thống kê chủ trì thu thập quy định tại Thông tư số 05/2017/TT-BKHĐT ngày 30/11/2017 của Bộ trưởng Bộ Kế hoạch và Đầu tư hết hiệu lực kể từ khi Thông tư này có hiệu lực . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 5 `[DIEU]`)
- (`e3` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e2` Thông tư số 05/2017/TT-BKHĐT `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 1 . Thông tư này có hiệu lực thi hành kể từ ngày 01 tháng 01 năm 2024 . Những chỉ tiêu phân công cho Tổng cục Thống kê chủ trì thu thập quy định tại Thông tư số 05/2017/TT-BKHĐT ngày 30/11/2017 của Bộ trưởng Bộ Kế hoạch và Đầu tư hết hiệu lực kể từ khi Thông tư này có hiệu lực . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e2` Thông tư số 05/2017/TT-BKHĐT `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e2` Thông tư số 05/2017/TT-BKHĐT `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e4` ngày 30/11/2017 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #06_2023_TT-BKHĐT_163394#body_context_32 (Loại: `body_context`)
> **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[06/2023/TT-BKHĐT]`<SO_HIEU>`** . **[Điều 5]`<DIEU>`** . **[2 . Trong quá trình thực hiện , nếu có vướng mắc , đề nghị các đơn vị gửi ý kiến về **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_THAM_QUYEN>`** ( Tổng cục Thống kê ) để kịp thời có hướng dẫn , nghiên cứu sửa đổi , bổ sung . / .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[5:6]`)
- `[e1]` **06/2023/TT-BKHĐT** → `SO_HIEU` (span: `[7:8]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[0:4]`)
- `[e3]` **Điều 5** → `DIEU` (span: `[9:11]`)
- `[e4]` **2 . Trong quá trình thực hiện , nếu có vướng mắc , đề nghị các đơn vị gửi ý kiến về Bộ Kế hoạch và Đầu tư ( Tổng cục Thống kê ) để kịp thời có hướng dẫn , nghiên cứu sửa đổi , bổ sung . / .** → `KHOAN` (span: `[12:48]`)
- `[e5]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_THAM_QUYEN` (span: `[28:32]`) *(lồng trong `e4` (`KHOAN`))*

**Quan hệ:**
- (`e1` 06/2023/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 06/2023/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 5 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 06/2023/TT-BKHĐT `[SO_HIEU]`)
- (`e4` 2 . Trong quá trình thực hiện , nếu có vướng mắc , đề nghị các đơn vị gửi ý kiến về Bộ Kế hoạch và Đầu tư ( Tổng cục Thống kê ) để kịp thời có hướng dẫn , nghiên cứu sửa đổi , bổ sung . / . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 5 `[DIEU]`)


---

### Mẫu #06_2023_TT-BKHĐT_163394#body_context_33 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[06/2023/TT-BKHĐT]`<SO_HIEU>`** ban hành **[ngày 02 tháng 10 năm 2023]`<NGAY_BAN_HANH>`** bởi **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** . **[Điều 1 . Phạm vi điều chỉnh]`<DIEU>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **06/2023/TT-BKHĐT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[11:15]`)
- `[e3]` **ngày 02 tháng 10 năm 2023** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 1 . Phạm vi điều chỉnh** → `DIEU` (span: `[16:21]`)

**Quan hệ:**
- (`e1` 06/2023/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 06/2023/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 06/2023/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 02 tháng 10 năm 2023 `[NGAY_BAN_HANH]`)
- (`e4` Điều 1 . Phạm vi điều chỉnh `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 06/2023/TT-BKHĐT `[SO_HIEU]`)


---

### Mẫu #06_2023_TT-BKHĐT_163394#body_context_34 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[06/2023/TT-BKHĐT]`<SO_HIEU>`** của **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** . **[Điều 2 . Đối tượng áp dụng]`<DIEU>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **06/2023/TT-BKHĐT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[4:8]`)
- `[e3]` **Điều 2 . Đối tượng áp dụng** → `DIEU` (span: `[9:14]`)

**Quan hệ:**
- (`e1` 06/2023/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 06/2023/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 2 . Đối tượng áp dụng `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 06/2023/TT-BKHĐT `[SO_HIEU]`)


---

### Mẫu #06_2023_TT-BKHĐT_163394#body_context_35 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[06/2023/TT-BKHĐT]`<SO_HIEU>`** ban hành **[ngày 02 tháng 10 năm 2023]`<NGAY_BAN_HANH>`** bởi **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** . **[Điều 2]`<DIEU>`** . **[1 . Cơ quan thống kê Trung ương .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **06/2023/TT-BKHĐT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[11:15]`)
- `[e3]` **ngày 02 tháng 10 năm 2023** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 2** → `DIEU` (span: `[16:18]`)
- `[e5]` **1 . Cơ quan thống kê Trung ương .** → `KHOAN` (span: `[19:25]`)

**Quan hệ:**
- (`e1` 06/2023/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 06/2023/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 06/2023/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 02 tháng 10 năm 2023 `[NGAY_BAN_HANH]`)
- (`e4` Điều 2 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 06/2023/TT-BKHĐT `[SO_HIEU]`)
- (`e5` 1 . Cơ quan thống kê Trung ương . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 2 `[DIEU]`)


---

### Mẫu #06_2023_TT-BKHĐT_163394#body_context_36 (Loại: `body_context`)
> **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[06/2023/TT-BKHĐT]`<SO_HIEU>`** . **[Điều 2]`<DIEU>`** . **[2 . Cơ quan thống kê địa phương .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[5:6]`)
- `[e1]` **06/2023/TT-BKHĐT** → `SO_HIEU` (span: `[7:8]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[0:4]`)
- `[e3]` **Điều 2** → `DIEU` (span: `[9:11]`)
- `[e4]` **2 . Cơ quan thống kê địa phương .** → `KHOAN` (span: `[12:18]`)

**Quan hệ:**
- (`e1` 06/2023/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 06/2023/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 2 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 06/2023/TT-BKHĐT `[SO_HIEU]`)
- (`e4` 2 . Cơ quan thống kê địa phương . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 2 `[DIEU]`)


---

### Mẫu #06_2023_TT-BKHĐT_163394#body_context_37 (Loại: `body_context`)
> **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[06/2023/TT-BKHĐT]`<SO_HIEU>`** . **[Điều 4 . Tổ chức thực hiện]`<DIEU>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[5:6]`)
- `[e1]` **06/2023/TT-BKHĐT** → `SO_HIEU` (span: `[7:8]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[0:4]`)
- `[e3]` **Điều 4 . Tổ chức thực hiện** → `DIEU` (span: `[9:14]`)

**Quan hệ:**
- (`e1` 06/2023/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 06/2023/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 4 . Tổ chức thực hiện `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 06/2023/TT-BKHĐT `[SO_HIEU]`)


---

### Mẫu #06_2023_TT-BKHĐT_163394#body_context_38 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[06/2023/TT-BKHĐT]`<SO_HIEU>`** ban hành **[ngày 02 tháng 10 năm 2023]`<NGAY_BAN_HANH>`** bởi **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** . **[Điều 5 . Hiệu lực thi hành]`<DIEU>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **06/2023/TT-BKHĐT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[11:15]`)
- `[e3]` **ngày 02 tháng 10 năm 2023** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 5 . Hiệu lực thi hành** → `DIEU` (span: `[16:21]`)

**Quan hệ:**
- (`e1` 06/2023/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 06/2023/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 06/2023/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 02 tháng 10 năm 2023 `[NGAY_BAN_HANH]`)
- (`e4` Điều 5 . Hiệu lực thi hành `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 06/2023/TT-BKHĐT `[SO_HIEU]`)


---

### Mẫu #06_2023_TT-BKHĐT_163394#hard_negative_39 (Loại: `hard_negative`)
> CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM


---

### Mẫu #06_2023_TT-BKHĐT_163394#hard_negative_40 (Loại: `hard_negative`)
> Độc lập - Tự do - Hạnh phúc


---
