# Dữ liệu gán nhãn văn bản: 11_2013_TT-BTTTT_46726
- **Thể loại**: `thong_tu`
- **Phân vùng dữ liệu**: `TRAIN`
- **Tổng số mẫu**: 17 mẫu
- **Tổng số thực thể**: 88
- **Tổng số quan hệ**: 61

---

### Mẫu #11_2013_TT-BTTTT_46726#header_0 (Loại: `header`)
> **[BỘ THÔNG TIN VÀ TRUYỀN THÔNG]`<CO_QUAN_BAN_HANH>`** . CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM . Độc lập – Tự do – Hạnh phúc . Số : **[11/2013/TT-BTTTT]`<SO_HIEU>`** . **[Ngày 13 tháng 5 năm 2013]`<NGAY_BAN_HANH>`** . **[THÔNG TƯ]`<LOAI_VAN_BAN>`**

**Thực thể:**
- `[e0]` **11/2013/TT-BTTTT** → `SO_HIEU` (span: `[20:21]`)
- `[e1]` **Ngày 13 tháng 5 năm 2013** → `NGAY_BAN_HANH` (span: `[22:28]`)
- `[e2]` **BỘ THÔNG TIN VÀ TRUYỀN THÔNG** → `CO_QUAN_BAN_HANH` (span: `[0:4]`)
- `[e3]` **THÔNG TƯ** → `LOAI_VAN_BAN` (span: `[29:30]`)

**Quan hệ:**
- (`e0` 11/2013/TT-BTTTT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` BỘ THÔNG TIN VÀ TRUYỀN THÔNG `[CO_QUAN_BAN_HANH]`)
- (`e0` 11/2013/TT-BTTTT `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e1` Ngày 13 tháng 5 năm 2013 `[NGAY_BAN_HANH]`)
- (`e0` 11/2013/TT-BTTTT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e3` THÔNG TƯ `[LOAI_VAN_BAN]`)


---

### Mẫu #11_2013_TT-BTTTT_46726#signature_1 (Loại: `signature`)
> **[BỘ TRƯỞNG]`<CHUC_DANH_NGUOI_KY>`** . ( Đã ký ) . **[Nguyễn Bắc Son]`<NGUOI_KY>`**

**Thực thể:**
- `[e0]` **Nguyễn Bắc Son** → `NGUOI_KY` (span: `[7:9]`)
- `[e1]` **BỘ TRƯỞNG** → `CHUC_DANH_NGUOI_KY` (span: `[0:1]`)

**Quan hệ:**
- (`e0` Nguyễn Bắc Son `[NGUOI_KY]`) ==[ **GIU_CHUC_VU** ]==> (`e1` BỘ TRƯỞNG `[CHUC_DANH_NGUOI_KY]`)


---

### Mẫu #11_2013_TT-BTTTT_46726#meta_2 (Loại: `meta`)
> **[BỘ THÔNG TIN VÀ TRUYỀN THÔNG]`<CO_QUAN_BAN_HANH>`** . CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM . Độc lập – Tự do – Hạnh phúc . Số : **[11/2013/TT-BTTTT]`<SO_HIEU>`** . Ngày 13 tháng 5 năm 2013 . **[THÔNG TƯ]`<LOAI_VAN_BAN>`** . **[BỘ TRƯỞNG]`<CHUC_DANH_NGUOI_KY>`** . ( Đã ký ) . **[Nguyễn Bắc Son]`<NGUOI_KY>`**

**Thực thể:**
- `[e0]` **11/2013/TT-BTTTT** → `SO_HIEU` (span: `[20:21]`)
- `[e1]` **BỘ THÔNG TIN VÀ TRUYỀN THÔNG** → `CO_QUAN_BAN_HANH` (span: `[0:4]`)
- `[e2]` **THÔNG TƯ** → `LOAI_VAN_BAN` (span: `[29:30]`)
- `[e3]` **Nguyễn Bắc Son** → `NGUOI_KY` (span: `[38:40]`)
- `[e4]` **BỘ TRƯỞNG** → `CHUC_DANH_NGUOI_KY` (span: `[31:32]`)

**Quan hệ:**
- (`e0` 11/2013/TT-BTTTT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e1` BỘ THÔNG TIN VÀ TRUYỀN THÔNG `[CO_QUAN_BAN_HANH]`)
- (`e0` 11/2013/TT-BTTTT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e2` THÔNG TƯ `[LOAI_VAN_BAN]`)
- (`e0` 11/2013/TT-BTTTT `[SO_HIEU]`) ==[ **KY_BOI** ]==> (`e3` Nguyễn Bắc Son `[NGUOI_KY]`)
- (`e3` Nguyễn Bắc Son `[NGUOI_KY]`) ==[ **GIU_CHUC_VU** ]==> (`e4` BỘ TRƯỞNG `[CHUC_DANH_NGUOI_KY]`)


---

### Mẫu #11_2013_TT-BTTTT_46726#preamble_context_3 (Loại: `preamble_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[11/2013/TT-BTTTT]`<SO_HIEU>`** của **[Bộ Thông tin và Truyền thông]`<CO_QUAN_BAN_HANH>`** . **[Căn cứ]`<TU_KHOA_PHAP_LY>`** **[Luật Viễn thông]`<THAM_CHIEU_PHAP_LY>`** **[ngày 23 tháng 11 năm 2009]`<NGAY_THAM_CHIEU>`** ;

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **11/2013/TT-BTTTT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Thông tin và Truyền thông** → `CO_QUAN_BAN_HANH` (span: `[4:8]`)
- `[e3]` **Luật Viễn thông** → `THAM_CHIEU_PHAP_LY` (span: `[10:12]`)
- `[e4]` **Căn cứ** → `TU_KHOA_PHAP_LY` (span: `[9:10]`)
- `[e5]` **ngày 23 tháng 11 năm 2009** → `NGAY_THAM_CHIEU` (span: `[12:18]`)

**Quan hệ:**
- (`e1` 11/2013/TT-BTTTT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Thông tin và Truyền thông `[CO_QUAN_BAN_HANH]`)
- (`e1` 11/2013/TT-BTTTT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e4` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Luật Viễn thông `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 11/2013/TT-BTTTT `[SO_HIEU]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Luật Viễn thông `[THAM_CHIEU_PHAP_LY]`)
- (`e3` Luật Viễn thông `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e5` ngày 23 tháng 11 năm 2009 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #11_2013_TT-BTTTT_46726#preamble_standalone_4 (Loại: `preamble_standalone`)
> **[Căn cứ]`<TU_KHOA_PHAP_LY>`** **[Luật Viễn thông]`<THAM_CHIEU_PHAP_LY>`** **[ngày 23 tháng 11 năm 2009]`<NGAY_THAM_CHIEU>`** ;

**Thực thể:**
- `[e0]` **Luật Viễn thông** → `THAM_CHIEU_PHAP_LY` (span: `[1:3]`)
- `[e1]` **Căn cứ** → `TU_KHOA_PHAP_LY` (span: `[0:1]`)
- `[e2]` **ngày 23 tháng 11 năm 2009** → `NGAY_THAM_CHIEU` (span: `[3:9]`)

**Quan hệ:**
- (`e1` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e0` Luật Viễn thông `[THAM_CHIEU_PHAP_LY]`)
- (`e0` Luật Viễn thông `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e2` ngày 23 tháng 11 năm 2009 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #11_2013_TT-BTTTT_46726#preamble_context_5 (Loại: `preamble_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[11/2013/TT-BTTTT]`<SO_HIEU>`** của **[Bộ Thông tin và Truyền thông]`<CO_QUAN_BAN_HANH>`** . **[Căn cứ]`<TU_KHOA_PHAP_LY>`** **[Nghị định số 187/2007/NĐ-CP]`<THAM_CHIEU_PHAP_LY>`** **[ngày 25 tháng 12 năm 2007]`<NGAY_THAM_CHIEU>`** của **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** quy định chức năng , nhiệm vụ , quyền hạn và cơ cấu tổ chức của **[Bộ Thông tin và Truyền thông]`<CO_QUAN_THAM_QUYEN>`** ;

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **11/2013/TT-BTTTT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Thông tin và Truyền thông** → `CO_QUAN_BAN_HANH` (span: `[4:8]`)
- `[e3]` **Nghị định số 187/2007/NĐ-CP** → `THAM_CHIEU_PHAP_LY` (span: `[10:13]`)
- `[e4]` **Căn cứ** → `TU_KHOA_PHAP_LY` (span: `[9:10]`)
- `[e5]` **ngày 25 tháng 12 năm 2007** → `NGAY_THAM_CHIEU` (span: `[13:19]`)
- `[e6]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[20:21]`)
- `[e7]` **Bộ Thông tin và Truyền thông** → `CO_QUAN_THAM_QUYEN` (span: `[31:35]`)

**Quan hệ:**
- (`e1` 11/2013/TT-BTTTT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Thông tin và Truyền thông `[CO_QUAN_BAN_HANH]`)
- (`e1` 11/2013/TT-BTTTT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e4` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Nghị định số 187/2007/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 11/2013/TT-BTTTT `[SO_HIEU]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Nghị định số 187/2007/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e3` Nghị định số 187/2007/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e5` ngày 25 tháng 12 năm 2007 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #11_2013_TT-BTTTT_46726#preamble_standalone_6 (Loại: `preamble_standalone`)
> **[Căn cứ]`<TU_KHOA_PHAP_LY>`** **[Nghị định số 187/2007/NĐ-CP]`<THAM_CHIEU_PHAP_LY>`** **[ngày 25 tháng 12 năm 2007]`<NGAY_THAM_CHIEU>`** của **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** quy định chức năng , nhiệm vụ , quyền hạn và cơ cấu tổ chức của **[Bộ Thông tin và Truyền thông]`<CO_QUAN_THAM_QUYEN>`** ;

**Thực thể:**
- `[e0]` **Nghị định số 187/2007/NĐ-CP** → `THAM_CHIEU_PHAP_LY` (span: `[1:4]`)
- `[e1]` **Căn cứ** → `TU_KHOA_PHAP_LY` (span: `[0:1]`)
- `[e2]` **ngày 25 tháng 12 năm 2007** → `NGAY_THAM_CHIEU` (span: `[4:10]`)
- `[e3]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[11:12]`)
- `[e4]` **Bộ Thông tin và Truyền thông** → `CO_QUAN_THAM_QUYEN` (span: `[22:26]`)

**Quan hệ:**
- (`e1` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e0` Nghị định số 187/2007/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e3` Chính phủ `[CO_QUAN_THAM_QUYEN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e0` Nghị định số 187/2007/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e0` Nghị định số 187/2007/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e2` ngày 25 tháng 12 năm 2007 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #11_2013_TT-BTTTT_46726#preamble_context_7 (Loại: `preamble_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[11/2013/TT-BTTTT]`<SO_HIEU>`** của **[Bộ Thông tin và Truyền thông]`<CO_QUAN_BAN_HANH>`** . **[Căn cứ]`<TU_KHOA_PHAP_LY>`** **[Nghị định số 50/2011/NĐ-CP]`<THAM_CHIEU_PHAP_LY>`** **[ngày 24 tháng 6 năm 2011]`<NGAY_THAM_CHIEU>`** của **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** **[sửa đổi]`<TU_KHOA_PHAP_LY>`** **[Nghị định số 187/2007/NĐ-CP]`<THAM_CHIEU_PHAP_LY>`** **[ngày 25 tháng 12 năm 2007]`<NGAY_THAM_CHIEU>`** của **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** quy định chức năng , nhiệm vụ , quyền hạn và cơ cấu tổ chức của **[Bộ Thông tin và Truyền thông]`<CO_QUAN_THAM_QUYEN>`** ;

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **11/2013/TT-BTTTT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Thông tin và Truyền thông** → `CO_QUAN_BAN_HANH` (span: `[4:8]`)
- `[e3]` **Nghị định số 50/2011/NĐ-CP** → `THAM_CHIEU_PHAP_LY` (span: `[10:13]`)
- `[e4]` **Nghị định số 187/2007/NĐ-CP** → `THAM_CHIEU_PHAP_LY` (span: `[22:25]`)
- `[e5]` **Căn cứ** → `TU_KHOA_PHAP_LY` (span: `[9:10]`)
- `[e6]` **sửa đổi** → `TU_KHOA_PHAP_LY` (span: `[21:22]`)
- `[e7]` **ngày 24 tháng 6 năm 2011** → `NGAY_THAM_CHIEU` (span: `[13:19]`)
- `[e8]` **ngày 25 tháng 12 năm 2007** → `NGAY_THAM_CHIEU` (span: `[25:31]`)
- `[e9]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[20:21]`)
- `[e10]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[32:33]`)
- `[e11]` **Bộ Thông tin và Truyền thông** → `CO_QUAN_THAM_QUYEN` (span: `[43:47]`)

**Quan hệ:**
- (`e1` 11/2013/TT-BTTTT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Thông tin và Truyền thông `[CO_QUAN_BAN_HANH]`)
- (`e1` 11/2013/TT-BTTTT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e5` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Nghị định số 50/2011/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 11/2013/TT-BTTTT `[SO_HIEU]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Nghị định số 50/2011/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e6` sửa đổi `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e4` Nghị định số 187/2007/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 11/2013/TT-BTTTT `[SO_HIEU]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e4` Nghị định số 187/2007/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e3` Nghị định số 50/2011/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e7` ngày 24 tháng 6 năm 2011 `[NGAY_THAM_CHIEU]`)
- (`e4` Nghị định số 187/2007/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e8` ngày 25 tháng 12 năm 2007 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #11_2013_TT-BTTTT_46726#preamble_standalone_8 (Loại: `preamble_standalone`)
> **[Căn cứ]`<TU_KHOA_PHAP_LY>`** **[Nghị định số 50/2011/NĐ-CP]`<THAM_CHIEU_PHAP_LY>`** **[ngày 24 tháng 6 năm 2011]`<NGAY_THAM_CHIEU>`** của **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** **[sửa đổi]`<TU_KHOA_PHAP_LY>`** **[Nghị định số 187/2007/NĐ-CP]`<THAM_CHIEU_PHAP_LY>`** **[ngày 25 tháng 12 năm 2007]`<NGAY_THAM_CHIEU>`** của **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** quy định chức năng , nhiệm vụ , quyền hạn và cơ cấu tổ chức của **[Bộ Thông tin và Truyền thông]`<CO_QUAN_THAM_QUYEN>`** ;

**Thực thể:**
- `[e0]` **Nghị định số 50/2011/NĐ-CP** → `THAM_CHIEU_PHAP_LY` (span: `[1:4]`)
- `[e1]` **Nghị định số 187/2007/NĐ-CP** → `THAM_CHIEU_PHAP_LY` (span: `[13:16]`)
- `[e2]` **Căn cứ** → `TU_KHOA_PHAP_LY` (span: `[0:1]`)
- `[e3]` **sửa đổi** → `TU_KHOA_PHAP_LY` (span: `[12:13]`)
- `[e4]` **ngày 24 tháng 6 năm 2011** → `NGAY_THAM_CHIEU` (span: `[4:10]`)
- `[e5]` **ngày 25 tháng 12 năm 2007** → `NGAY_THAM_CHIEU` (span: `[16:22]`)
- `[e6]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[11:12]`)
- `[e7]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[23:24]`)
- `[e8]` **Bộ Thông tin và Truyền thông** → `CO_QUAN_THAM_QUYEN` (span: `[34:38]`)

**Quan hệ:**
- (`e2` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e0` Nghị định số 50/2011/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e6` Chính phủ `[CO_QUAN_THAM_QUYEN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e0` Nghị định số 50/2011/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e3` sửa đổi `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e1` Nghị định số 187/2007/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e6` Chính phủ `[CO_QUAN_THAM_QUYEN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e1` Nghị định số 187/2007/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e0` Nghị định số 50/2011/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e4` ngày 24 tháng 6 năm 2011 `[NGAY_THAM_CHIEU]`)
- (`e1` Nghị định số 187/2007/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e5` ngày 25 tháng 12 năm 2007 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #11_2013_TT-BTTTT_46726#preamble_context_9 (Loại: `preamble_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[11/2013/TT-BTTTT]`<SO_HIEU>`** của **[Bộ Thông tin và Truyền thông]`<CO_QUAN_BAN_HANH>`** . **[Căn cứ]`<TU_KHOA_PHAP_LY>`** **[Nghị định số 25/2011/NĐ-CP]`<THAM_CHIEU_PHAP_LY>`** **[ngày 06 tháng 4 năm 2011]`<NGAY_THAM_CHIEU>`** của **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** quy định chi tiết và hướng dẫn thi hành một số điều của Luật Viễn thông ;

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **11/2013/TT-BTTTT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Thông tin và Truyền thông** → `CO_QUAN_BAN_HANH` (span: `[4:8]`)
- `[e3]` **Nghị định số 25/2011/NĐ-CP** → `THAM_CHIEU_PHAP_LY` (span: `[10:13]`)
- `[e4]` **Căn cứ** → `TU_KHOA_PHAP_LY` (span: `[9:10]`)
- `[e5]` **ngày 06 tháng 4 năm 2011** → `NGAY_THAM_CHIEU` (span: `[13:19]`)
- `[e6]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[20:21]`)

**Quan hệ:**
- (`e1` 11/2013/TT-BTTTT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Thông tin và Truyền thông `[CO_QUAN_BAN_HANH]`)
- (`e1` 11/2013/TT-BTTTT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e4` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Nghị định số 25/2011/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 11/2013/TT-BTTTT `[SO_HIEU]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Nghị định số 25/2011/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e3` Nghị định số 25/2011/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e5` ngày 06 tháng 4 năm 2011 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #11_2013_TT-BTTTT_46726#preamble_standalone_10 (Loại: `preamble_standalone`)
> **[Căn cứ]`<TU_KHOA_PHAP_LY>`** **[Nghị định số 25/2011/NĐ-CP]`<THAM_CHIEU_PHAP_LY>`** **[ngày 06 tháng 4 năm 2011]`<NGAY_THAM_CHIEU>`** của **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** quy định chi tiết và hướng dẫn thi hành một số điều của Luật Viễn thông ;

**Thực thể:**
- `[e0]` **Nghị định số 25/2011/NĐ-CP** → `THAM_CHIEU_PHAP_LY` (span: `[1:4]`)
- `[e1]` **Căn cứ** → `TU_KHOA_PHAP_LY` (span: `[0:1]`)
- `[e2]` **ngày 06 tháng 4 năm 2011** → `NGAY_THAM_CHIEU` (span: `[4:10]`)
- `[e3]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[11:12]`)

**Quan hệ:**
- (`e1` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e0` Nghị định số 25/2011/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e3` Chính phủ `[CO_QUAN_THAM_QUYEN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e0` Nghị định số 25/2011/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e0` Nghị định số 25/2011/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e2` ngày 06 tháng 4 năm 2011 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #11_2013_TT-BTTTT_46726#preamble_context_11 (Loại: `preamble_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[11/2013/TT-BTTTT]`<SO_HIEU>`** của **[Bộ Thông tin và Truyền thông]`<CO_QUAN_BAN_HANH>`** . **[Bộ trưởng Bộ Thông tin và Truyền thông]`<CO_QUAN_THAM_QUYEN>`** ban hành Thông tư Danh mục dịch vụ viễn thông thực hiện báo cáo giá thành thực tế , giá thành kế hoạch .

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **11/2013/TT-BTTTT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Thông tin và Truyền thông** → `CO_QUAN_BAN_HANH` (span: `[4:8]`)
- `[e3]` **Bộ trưởng Bộ Thông tin và Truyền thông** → `CO_QUAN_THAM_QUYEN` (span: `[9:14]`)

**Quan hệ:**
- (`e1` 11/2013/TT-BTTTT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Thông tin và Truyền thông `[CO_QUAN_BAN_HANH]`)
- (`e1` 11/2013/TT-BTTTT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)


---

### Mẫu #11_2013_TT-BTTTT_46726#preamble_standalone_12 (Loại: `preamble_standalone`)
> **[Bộ trưởng Bộ Thông tin và Truyền thông]`<CO_QUAN_THAM_QUYEN>`** ban hành Thông tư Danh mục dịch vụ viễn thông thực hiện báo cáo giá thành thực tế , giá thành kế hoạch .

**Thực thể:**
- `[e0]` **Bộ trưởng Bộ Thông tin và Truyền thông** → `CO_QUAN_THAM_QUYEN` (span: `[0:5]`)


---

### Mẫu #11_2013_TT-BTTTT_46726#body_context_13 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[11/2013/TT-BTTTT]`<SO_HIEU>`** ban hành **[ngày 13 tháng 05 năm 2013]`<NGAY_BAN_HANH>`** bởi **[Bộ Thông tin và Truyền thông]`<CO_QUAN_BAN_HANH>`** . **[Điều 1 . Ban hành kèm theo Thông tư này Danh mục dịch vụ viễn thông thực hiện báo cáo giá thành thực tế , giá thành kế hoạch .]`<DIEU>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **11/2013/TT-BTTTT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Thông tin và Truyền thông** → `CO_QUAN_BAN_HANH` (span: `[11:15]`)
- `[e3]` **ngày 13 tháng 05 năm 2013** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 1 . Ban hành kèm theo Thông tư này Danh mục dịch vụ viễn thông thực hiện báo cáo giá thành thực tế , giá thành kế hoạch .** → `DIEU` (span: `[16:34]`)

**Quan hệ:**
- (`e1` 11/2013/TT-BTTTT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Thông tin và Truyền thông `[CO_QUAN_BAN_HANH]`)
- (`e1` 11/2013/TT-BTTTT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 11/2013/TT-BTTTT `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 13 tháng 05 năm 2013 `[NGAY_BAN_HANH]`)
- (`e4` Điều 1 . Ban hành kèm theo Thông tư này Danh mục dịch vụ viễn thông thực hiện báo cáo giá thành thực tế , giá thành kế hoạch . `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 11/2013/TT-BTTTT `[SO_HIEU]`)


---

### Mẫu #11_2013_TT-BTTTT_46726#body_context_14 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[11/2013/TT-BTTTT]`<SO_HIEU>`** ban hành **[ngày 13 tháng 05 năm 2013]`<NGAY_BAN_HANH>`** bởi **[Bộ Thông tin và Truyền thông]`<CO_QUAN_BAN_HANH>`** . **[Điều 2 . Thông tư này có hiệu lực thi hành kể từ ngày 13 tháng 5 năm 2013 .]`<DIEU>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **11/2013/TT-BTTTT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Thông tin và Truyền thông** → `CO_QUAN_BAN_HANH` (span: `[11:15]`)
- `[e3]` **ngày 13 tháng 05 năm 2013** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 2 . Thông tư này có hiệu lực thi hành kể từ ngày 13 tháng 5 năm 2013 .** → `DIEU` (span: `[16:33]`)

**Quan hệ:**
- (`e1` 11/2013/TT-BTTTT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Thông tin và Truyền thông `[CO_QUAN_BAN_HANH]`)
- (`e1` 11/2013/TT-BTTTT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 11/2013/TT-BTTTT `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 13 tháng 05 năm 2013 `[NGAY_BAN_HANH]`)
- (`e4` Điều 2 . Thông tư này có hiệu lực thi hành kể từ ngày 13 tháng 5 năm 2013 . `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 11/2013/TT-BTTTT `[SO_HIEU]`)


---

### Mẫu #11_2013_TT-BTTTT_46726#body_context_15 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[11/2013/TT-BTTTT]`<SO_HIEU>`** của **[Bộ Thông tin và Truyền thông]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Viễn thông và Internet]`<LINH_VUC>`** . **[Điều 3 . Chánh Văn phòng , Thủ trưởng các cơ quan , đơn vị thuộc Bộ , Cục trưởng Cục Viễn thông , **[Tổng giám đốc]`<CHU_THE_CA_NHAN>`** , **[Giám đốc]`<CHU_THE_CA_NHAN>`** các **[doanh nghiệp viễn thông]`<TO_CHUC_DOANH_NGHIEP>`** . và các tổ chức , cá nhân có liên quan chịu trách nhiệm thi hành Thông tư này . / .]`<DIEU>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **11/2013/TT-BTTTT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Thông tin và Truyền thông** → `CO_QUAN_BAN_HANH` (span: `[4:8]`)
- `[e3]` **Viễn thông và Internet** → `LINH_VUC` (span: `[10:13]`)
- `[e4]` **Điều 3 . Chánh Văn phòng , Thủ trưởng các cơ quan , đơn vị thuộc Bộ , Cục trưởng Cục Viễn thông , Tổng giám đốc , Giám đốc các doanh nghiệp viễn thông . và các tổ chức , cá nhân có liên quan chịu trách nhiệm thi hành Thông tư này . / .** → `DIEU` (span: `[14:54]`)
- `[e5]` **doanh nghiệp viễn thông** → `TO_CHUC_DOANH_NGHIEP` (span: `[36:38]`) *(lồng trong `e4` (`DIEU`))*
- `[e6]` **Tổng giám đốc** → `CHU_THE_CA_NHAN` (span: `[32:33]`) *(lồng trong `e4` (`DIEU`))*
- `[e7]` **Giám đốc** → `CHU_THE_CA_NHAN` (span: `[34:35]`) *(lồng trong `e4` (`DIEU`))*

**Quan hệ:**
- (`e1` 11/2013/TT-BTTTT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Thông tin và Truyền thông `[CO_QUAN_BAN_HANH]`)
- (`e1` 11/2013/TT-BTTTT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 11/2013/TT-BTTTT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Viễn thông và Internet `[LINH_VUC]`)
- (`e4` Điều 3 . Chánh Văn phòng , Thủ trưởng các cơ quan , đơn vị thuộc Bộ , Cục trưởng Cục Viễn thông , Tổng giám đốc , Giám đốc các doanh nghiệp viễn thông . và các tổ chức , cá nhân có liên quan chịu trách nhiệm thi hành Thông tư này . / . `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 11/2013/TT-BTTTT `[SO_HIEU]`)
- (`e1` 11/2013/TT-BTTTT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Viễn thông và Internet `[LINH_VUC]`)
- (`e4` Điều 3 . Chánh Văn phòng , Thủ trưởng các cơ quan , đơn vị thuộc Bộ , Cục trưởng Cục Viễn thông , Tổng giám đốc , Giám đốc các doanh nghiệp viễn thông . và các tổ chức , cá nhân có liên quan chịu trách nhiệm thi hành Thông tư này . / . `[DIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Viễn thông và Internet `[LINH_VUC]`)


---

### Mẫu #11_2013_TT-BTTTT_46726#hard_negative_16 (Loại: `hard_negative`)
> CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM


---
