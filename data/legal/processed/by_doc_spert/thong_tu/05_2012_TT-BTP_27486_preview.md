# Dữ liệu gán nhãn văn bản: 05_2012_TT-BTP_27486
- **Thể loại**: `thong_tu`
- **Phân vùng dữ liệu**: `TRAIN`
- **Tổng số mẫu**: 36 mẫu
- **Tổng số thực thể**: 186
- **Tổng số quan hệ**: 144

---

### Mẫu #05_2012_TT-BTP_27486#header_0 (Loại: `header`)
> **[BỘ TƯ PHÁP]`<CO_QUAN_BAN_HANH>`** . CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM . Độc lập – Tự do – Hạnh phúc . Số : **[05/2012/TT-BTP]`<SO_HIEU>`** . Hà Nội , **[Ngày 23 tháng 5 năm 2012]`<NGAY_BAN_HANH>`** . **[THÔNG TƯ]`<LOAI_VAN_BAN>`**

**Thực thể:**
- `[e0]` **05/2012/TT-BTP** → `SO_HIEU` (span: `[18:19]`)
- `[e1]` **Ngày 23 tháng 5 năm 2012** → `NGAY_BAN_HANH` (span: `[22:28]`)
- `[e2]` **BỘ TƯ PHÁP** → `CO_QUAN_BAN_HANH` (span: `[0:2]`)
- `[e3]` **THÔNG TƯ** → `LOAI_VAN_BAN` (span: `[29:30]`)

**Quan hệ:**
- (`e0` 05/2012/TT-BTP `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` BỘ TƯ PHÁP `[CO_QUAN_BAN_HANH]`)
- (`e0` 05/2012/TT-BTP `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e1` Ngày 23 tháng 5 năm 2012 `[NGAY_BAN_HANH]`)
- (`e0` 05/2012/TT-BTP `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e3` THÔNG TƯ `[LOAI_VAN_BAN]`)


---

### Mẫu #05_2012_TT-BTP_27486#signature_1 (Loại: `signature`)
> KT. BỘ TRƯỞNG **[THỨ TRƯỞNG]`<CHUC_DANH_NGUOI_KY>`** . **[Đinh Trung Tụng]`<NGUOI_KY>`**

**Thực thể:**
- `[e0]` **Đinh Trung Tụng** → `NGUOI_KY` (span: `[4:5]`)
- `[e1]` **THỨ TRƯỞNG** → `CHUC_DANH_NGUOI_KY` (span: `[2:3]`)

**Quan hệ:**
- (`e0` Đinh Trung Tụng `[NGUOI_KY]`) ==[ **GIU_CHUC_VU** ]==> (`e1` THỨ TRƯỞNG `[CHUC_DANH_NGUOI_KY]`)


---

### Mẫu #05_2012_TT-BTP_27486#meta_2 (Loại: `meta`)
> **[BỘ TƯ PHÁP]`<CO_QUAN_BAN_HANH>`** . CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM . Độc lập – Tự do – Hạnh phúc . Số : **[05/2012/TT-BTP]`<SO_HIEU>`** . Hà Nội , Ngày 23 tháng 5 năm 2012 . **[THÔNG TƯ]`<LOAI_VAN_BAN>`** . KT. BỘ TRƯỞNG **[THỨ TRƯỞNG]`<CHUC_DANH_NGUOI_KY>`** . **[Đinh Trung Tụng]`<NGUOI_KY>`**

**Thực thể:**
- `[e0]` **05/2012/TT-BTP** → `SO_HIEU` (span: `[18:19]`)
- `[e1]` **BỘ TƯ PHÁP** → `CO_QUAN_BAN_HANH` (span: `[0:2]`)
- `[e2]` **THÔNG TƯ** → `LOAI_VAN_BAN` (span: `[29:30]`)
- `[e3]` **Đinh Trung Tụng** → `NGUOI_KY` (span: `[35:36]`)
- `[e4]` **THỨ TRƯỞNG** → `CHUC_DANH_NGUOI_KY` (span: `[33:34]`)

**Quan hệ:**
- (`e0` 05/2012/TT-BTP `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e1` BỘ TƯ PHÁP `[CO_QUAN_BAN_HANH]`)
- (`e0` 05/2012/TT-BTP `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e2` THÔNG TƯ `[LOAI_VAN_BAN]`)
- (`e0` 05/2012/TT-BTP `[SO_HIEU]`) ==[ **KY_BOI** ]==> (`e3` Đinh Trung Tụng `[NGUOI_KY]`)
- (`e3` Đinh Trung Tụng `[NGUOI_KY]`) ==[ **GIU_CHUC_VU** ]==> (`e4` THỨ TRƯỞNG `[CHUC_DANH_NGUOI_KY]`)


---

### Mẫu #05_2012_TT-BTP_27486#preamble_context_3 (Loại: `preamble_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[05/2012/TT-BTP]`<SO_HIEU>`** của **[Bộ Tư pháp]`<CO_QUAN_BAN_HANH>`** . **[Sửa đổi , bổ sung một số điều của]`<TU_KHOA_PHAP_LY>`** Thông tư số 08.a/2010/TT-BTP

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **05/2012/TT-BTP** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Tư pháp** → `CO_QUAN_BAN_HANH` (span: `[4:6]`)
- `[e3]` **Sửa đổi , bổ sung một số điều của** → `TU_KHOA_PHAP_LY` (span: `[7:13]`)

**Quan hệ:**
- (`e1` 05/2012/TT-BTP `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Tư pháp `[CO_QUAN_BAN_HANH]`)
- (`e1` 05/2012/TT-BTP `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)


---

### Mẫu #05_2012_TT-BTP_27486#preamble_standalone_4 (Loại: `preamble_standalone`)
> **[Sửa đổi , bổ sung một số điều của]`<TU_KHOA_PHAP_LY>`** Thông tư số 08.a/2010/TT-BTP

**Thực thể:**
- `[e0]` **Sửa đổi , bổ sung một số điều của** → `TU_KHOA_PHAP_LY` (span: `[0:6]`)


---

### Mẫu #05_2012_TT-BTP_27486#preamble_context_5 (Loại: `preamble_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[05/2012/TT-BTP]`<SO_HIEU>`** của **[Bộ Tư pháp]`<CO_QUAN_BAN_HANH>`** . ngày 25 tháng 3 năm 2010 của **[Bộ Tư pháp]`<CO_QUAN_THAM_QUYEN>`** về việc ban hành và hướng dẫn

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **05/2012/TT-BTP** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Tư pháp** → `CO_QUAN_BAN_HANH` (span: `[4:6]`)
- `[e3]` **Bộ Tư pháp** → `CO_QUAN_THAM_QUYEN` (span: `[14:16]`)

**Quan hệ:**
- (`e1` 05/2012/TT-BTP `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Tư pháp `[CO_QUAN_BAN_HANH]`)
- (`e1` 05/2012/TT-BTP `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)


---

### Mẫu #05_2012_TT-BTP_27486#preamble_standalone_6 (Loại: `preamble_standalone`)
> ngày 25 tháng 3 năm 2010 của **[Bộ Tư pháp]`<CO_QUAN_THAM_QUYEN>`** về việc ban hành và hướng dẫn

**Thực thể:**
- `[e0]` **Bộ Tư pháp** → `CO_QUAN_THAM_QUYEN` (span: `[7:9]`)


---

### Mẫu #05_2012_TT-BTP_27486#preamble_context_7 (Loại: `preamble_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[05/2012/TT-BTP]`<SO_HIEU>`** của **[Bộ Tư pháp]`<CO_QUAN_BAN_HANH>`** . **[Căn cứ]`<TU_KHOA_PHAP_LY>`** **[Nghị định số 158/2005/NĐ-CP]`<THAM_CHIEU_PHAP_LY>`** **[ngày 27 tháng 12 năm 2005]`<NGAY_THAM_CHIEU>`** của **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** về đăng ký và quản lý hộ tịch ;

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **05/2012/TT-BTP** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Tư pháp** → `CO_QUAN_BAN_HANH` (span: `[4:6]`)
- `[e3]` **Nghị định số 158/2005/NĐ-CP** → `THAM_CHIEU_PHAP_LY` (span: `[8:11]`)
- `[e4]` **Căn cứ** → `TU_KHOA_PHAP_LY` (span: `[7:8]`)
- `[e5]` **ngày 27 tháng 12 năm 2005** → `NGAY_THAM_CHIEU` (span: `[11:17]`)
- `[e6]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[18:19]`)

**Quan hệ:**
- (`e1` 05/2012/TT-BTP `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Tư pháp `[CO_QUAN_BAN_HANH]`)
- (`e1` 05/2012/TT-BTP `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e4` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Nghị định số 158/2005/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 05/2012/TT-BTP `[SO_HIEU]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Nghị định số 158/2005/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e3` Nghị định số 158/2005/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e5` ngày 27 tháng 12 năm 2005 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #05_2012_TT-BTP_27486#preamble_standalone_8 (Loại: `preamble_standalone`)
> **[Căn cứ]`<TU_KHOA_PHAP_LY>`** **[Nghị định số 158/2005/NĐ-CP]`<THAM_CHIEU_PHAP_LY>`** **[ngày 27 tháng 12 năm 2005]`<NGAY_THAM_CHIEU>`** của **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** về đăng ký và quản lý hộ tịch ;

**Thực thể:**
- `[e0]` **Nghị định số 158/2005/NĐ-CP** → `THAM_CHIEU_PHAP_LY` (span: `[1:4]`)
- `[e1]` **Căn cứ** → `TU_KHOA_PHAP_LY` (span: `[0:1]`)
- `[e2]` **ngày 27 tháng 12 năm 2005** → `NGAY_THAM_CHIEU` (span: `[4:10]`)
- `[e3]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[11:12]`)

**Quan hệ:**
- (`e1` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e0` Nghị định số 158/2005/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e3` Chính phủ `[CO_QUAN_THAM_QUYEN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e0` Nghị định số 158/2005/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e0` Nghị định số 158/2005/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e2` ngày 27 tháng 12 năm 2005 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #05_2012_TT-BTP_27486#preamble_context_9 (Loại: `preamble_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[05/2012/TT-BTP]`<SO_HIEU>`** của **[Bộ Tư pháp]`<CO_QUAN_BAN_HANH>`** . **[Căn cứ]`<TU_KHOA_PHAP_LY>`** **[Nghị định số 68/2002/NĐ-CP]`<THAM_CHIEU_PHAP_LY>`** **[ngày 10 tháng 7 năm 2002]`<NGAY_THAM_CHIEU>`** của **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** quy định chi tiết thi hành một số điều của Luật Hôn nhân và gia đình về quan hệ hôn nhân và gia đình có yếu tố nước ngoài và **[Nghị định số 69/2006/NĐ-CP]`<THAM_CHIEU_PHAP_LY>`** **[ngày 21 tháng 7 năm 2006]`<NGAY_THAM_CHIEU>`** của **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** **[sửa đổi , bổ sung một số điều của]`<TU_KHOA_PHAP_LY>`** **[Nghị định số 68/2002/NĐ-CP]`<THAM_CHIEU_PHAP_LY>`** ;

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **05/2012/TT-BTP** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Tư pháp** → `CO_QUAN_BAN_HANH` (span: `[4:6]`)
- `[e3]` **Nghị định số 68/2002/NĐ-CP** → `THAM_CHIEU_PHAP_LY` (span: `[8:11]`)
- `[e4]` **Nghị định số 69/2006/NĐ-CP** → `THAM_CHIEU_PHAP_LY` (span: `[38:41]`)
- `[e5]` **Nghị định số 68/2002/NĐ-CP** → `THAM_CHIEU_PHAP_LY` (span: `[55:58]`)
- `[e6]` **Căn cứ** → `TU_KHOA_PHAP_LY` (span: `[7:8]`)
- `[e7]` **sửa đổi , bổ sung một số điều của** → `TU_KHOA_PHAP_LY` (span: `[49:55]`)
- `[e8]` **ngày 10 tháng 7 năm 2002** → `NGAY_THAM_CHIEU` (span: `[11:17]`)
- `[e9]` **ngày 21 tháng 7 năm 2006** → `NGAY_THAM_CHIEU` (span: `[41:47]`)
- `[e10]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[18:19]`)
- `[e11]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[48:49]`)

**Quan hệ:**
- (`e1` 05/2012/TT-BTP `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Tư pháp `[CO_QUAN_BAN_HANH]`)
- (`e1` 05/2012/TT-BTP `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e6` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Nghị định số 68/2002/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 05/2012/TT-BTP `[SO_HIEU]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Nghị định số 68/2002/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e6` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e4` Nghị định số 69/2006/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 05/2012/TT-BTP `[SO_HIEU]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e4` Nghị định số 69/2006/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e7` sửa đổi , bổ sung một số điều của `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e5` Nghị định số 68/2002/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 05/2012/TT-BTP `[SO_HIEU]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e5` Nghị định số 68/2002/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e3` Nghị định số 68/2002/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e8` ngày 10 tháng 7 năm 2002 `[NGAY_THAM_CHIEU]`)
- (`e4` Nghị định số 69/2006/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e9` ngày 21 tháng 7 năm 2006 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #05_2012_TT-BTP_27486#preamble_standalone_10 (Loại: `preamble_standalone`)
> **[Căn cứ]`<TU_KHOA_PHAP_LY>`** **[Nghị định số 68/2002/NĐ-CP]`<THAM_CHIEU_PHAP_LY>`** **[ngày 10 tháng 7 năm 2002]`<NGAY_THAM_CHIEU>`** của **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** quy định chi tiết thi hành một số điều của Luật Hôn nhân và gia đình về quan hệ hôn nhân và gia đình có yếu tố nước ngoài và **[Nghị định số 69/2006/NĐ-CP]`<THAM_CHIEU_PHAP_LY>`** **[ngày 21 tháng 7 năm 2006]`<NGAY_THAM_CHIEU>`** của **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** **[sửa đổi , bổ sung một số điều của]`<TU_KHOA_PHAP_LY>`** **[Nghị định số 68/2002/NĐ-CP]`<THAM_CHIEU_PHAP_LY>`** ;

**Thực thể:**
- `[e0]` **Nghị định số 68/2002/NĐ-CP** → `THAM_CHIEU_PHAP_LY` (span: `[1:4]`)
- `[e1]` **Nghị định số 69/2006/NĐ-CP** → `THAM_CHIEU_PHAP_LY` (span: `[31:34]`)
- `[e2]` **Nghị định số 68/2002/NĐ-CP** → `THAM_CHIEU_PHAP_LY` (span: `[48:51]`)
- `[e3]` **Căn cứ** → `TU_KHOA_PHAP_LY` (span: `[0:1]`)
- `[e4]` **sửa đổi , bổ sung một số điều của** → `TU_KHOA_PHAP_LY` (span: `[42:48]`)
- `[e5]` **ngày 10 tháng 7 năm 2002** → `NGAY_THAM_CHIEU` (span: `[4:10]`)
- `[e6]` **ngày 21 tháng 7 năm 2006** → `NGAY_THAM_CHIEU` (span: `[34:40]`)
- `[e7]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[11:12]`)
- `[e8]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[41:42]`)

**Quan hệ:**
- (`e3` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e0` Nghị định số 68/2002/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e7` Chính phủ `[CO_QUAN_THAM_QUYEN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e0` Nghị định số 68/2002/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e3` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e1` Nghị định số 69/2006/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e8` Chính phủ `[CO_QUAN_THAM_QUYEN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e1` Nghị định số 69/2006/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e4` sửa đổi , bổ sung một số điều của `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e2` Nghị định số 68/2002/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e8` Chính phủ `[CO_QUAN_THAM_QUYEN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e2` Nghị định số 68/2002/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e0` Nghị định số 68/2002/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e5` ngày 10 tháng 7 năm 2002 `[NGAY_THAM_CHIEU]`)
- (`e1` Nghị định số 69/2006/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e6` ngày 21 tháng 7 năm 2006 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #05_2012_TT-BTP_27486#preamble_context_11 (Loại: `preamble_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[05/2012/TT-BTP]`<SO_HIEU>`** của **[Bộ Tư pháp]`<CO_QUAN_BAN_HANH>`** . **[Căn cứ]`<TU_KHOA_PHAP_LY>`** **[Nghị định số 06/2012/NĐ-CP]`<THAM_CHIEU_PHAP_LY>`** **[ngày 02 tháng 02 năm 2012]`<NGAY_THAM_CHIEU>`** **[sửa đổi , bổ sung một số điều của]`<TU_KHOA_PHAP_LY>`** các Nghị định về hộ tịch , hôn nhân và gia đình và chứng thực ;

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **05/2012/TT-BTP** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Tư pháp** → `CO_QUAN_BAN_HANH` (span: `[4:6]`)
- `[e3]` **Nghị định số 06/2012/NĐ-CP** → `THAM_CHIEU_PHAP_LY` (span: `[8:11]`)
- `[e4]` **Căn cứ** → `TU_KHOA_PHAP_LY` (span: `[7:8]`)
- `[e5]` **sửa đổi , bổ sung một số điều của** → `TU_KHOA_PHAP_LY` (span: `[17:23]`)
- `[e6]` **ngày 02 tháng 02 năm 2012** → `NGAY_THAM_CHIEU` (span: `[11:17]`)

**Quan hệ:**
- (`e1` 05/2012/TT-BTP `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Tư pháp `[CO_QUAN_BAN_HANH]`)
- (`e1` 05/2012/TT-BTP `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e4` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Nghị định số 06/2012/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 05/2012/TT-BTP `[SO_HIEU]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Nghị định số 06/2012/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e3` Nghị định số 06/2012/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e6` ngày 02 tháng 02 năm 2012 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #05_2012_TT-BTP_27486#preamble_standalone_12 (Loại: `preamble_standalone`)
> **[Căn cứ]`<TU_KHOA_PHAP_LY>`** **[Nghị định số 06/2012/NĐ-CP]`<THAM_CHIEU_PHAP_LY>`** **[ngày 02 tháng 02 năm 2012]`<NGAY_THAM_CHIEU>`** **[sửa đổi , bổ sung một số điều của]`<TU_KHOA_PHAP_LY>`** các Nghị định về hộ tịch , hôn nhân và gia đình và chứng thực ;

**Thực thể:**
- `[e0]` **Nghị định số 06/2012/NĐ-CP** → `THAM_CHIEU_PHAP_LY` (span: `[1:4]`)
- `[e1]` **Căn cứ** → `TU_KHOA_PHAP_LY` (span: `[0:1]`)
- `[e2]` **sửa đổi , bổ sung một số điều của** → `TU_KHOA_PHAP_LY` (span: `[10:16]`)
- `[e3]` **ngày 02 tháng 02 năm 2012** → `NGAY_THAM_CHIEU` (span: `[4:10]`)

**Quan hệ:**
- (`e1` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e0` Nghị định số 06/2012/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e0` Nghị định số 06/2012/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e3` ngày 02 tháng 02 năm 2012 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #05_2012_TT-BTP_27486#preamble_context_13 (Loại: `preamble_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[05/2012/TT-BTP]`<SO_HIEU>`** của **[Bộ Tư pháp]`<CO_QUAN_BAN_HANH>`** . **[Căn cứ]`<TU_KHOA_PHAP_LY>`** **[Nghị định số 93/2008/NĐ-CP]`<THAM_CHIEU_PHAP_LY>`** **[ngày 22 tháng 8 năm 2008]`<NGAY_THAM_CHIEU>`** của **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** quy định chức năng , nhiệm vụ , quyền hạn và cơ cấu tổ chức của **[Bộ Tư pháp]`<CO_QUAN_THAM_QUYEN>`** ;

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **05/2012/TT-BTP** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Tư pháp** → `CO_QUAN_BAN_HANH` (span: `[4:6]`)
- `[e3]` **Nghị định số 93/2008/NĐ-CP** → `THAM_CHIEU_PHAP_LY` (span: `[8:11]`)
- `[e4]` **Căn cứ** → `TU_KHOA_PHAP_LY` (span: `[7:8]`)
- `[e5]` **ngày 22 tháng 8 năm 2008** → `NGAY_THAM_CHIEU` (span: `[11:17]`)
- `[e6]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[18:19]`)
- `[e7]` **Bộ Tư pháp** → `CO_QUAN_THAM_QUYEN` (span: `[29:31]`)

**Quan hệ:**
- (`e1` 05/2012/TT-BTP `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Tư pháp `[CO_QUAN_BAN_HANH]`)
- (`e1` 05/2012/TT-BTP `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e4` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Nghị định số 93/2008/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 05/2012/TT-BTP `[SO_HIEU]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Nghị định số 93/2008/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e3` Nghị định số 93/2008/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e5` ngày 22 tháng 8 năm 2008 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #05_2012_TT-BTP_27486#preamble_standalone_14 (Loại: `preamble_standalone`)
> **[Căn cứ]`<TU_KHOA_PHAP_LY>`** **[Nghị định số 93/2008/NĐ-CP]`<THAM_CHIEU_PHAP_LY>`** **[ngày 22 tháng 8 năm 2008]`<NGAY_THAM_CHIEU>`** của **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** quy định chức năng , nhiệm vụ , quyền hạn và cơ cấu tổ chức của **[Bộ Tư pháp]`<CO_QUAN_THAM_QUYEN>`** ;

**Thực thể:**
- `[e0]` **Nghị định số 93/2008/NĐ-CP** → `THAM_CHIEU_PHAP_LY` (span: `[1:4]`)
- `[e1]` **Căn cứ** → `TU_KHOA_PHAP_LY` (span: `[0:1]`)
- `[e2]` **ngày 22 tháng 8 năm 2008** → `NGAY_THAM_CHIEU` (span: `[4:10]`)
- `[e3]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[11:12]`)
- `[e4]` **Bộ Tư pháp** → `CO_QUAN_THAM_QUYEN` (span: `[22:24]`)

**Quan hệ:**
- (`e1` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e0` Nghị định số 93/2008/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e3` Chính phủ `[CO_QUAN_THAM_QUYEN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e0` Nghị định số 93/2008/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e0` Nghị định số 93/2008/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e2` ngày 22 tháng 8 năm 2008 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #05_2012_TT-BTP_27486#preamble_context_15 (Loại: `preamble_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[05/2012/TT-BTP]`<SO_HIEU>`** của **[Bộ Tư pháp]`<CO_QUAN_BAN_HANH>`** . **[Bộ trưởng Bộ Tư pháp]`<CO_QUAN_THAM_QUYEN>`** ban hành Thông tư **[sửa đổi , bổ sung một số điều của]`<TU_KHOA_PHAP_LY>`** Thông tư số 08.a/2010/TT-BTP ngày 25 tháng 3 năm 2010 về việc ban hành và hướng dẫn việc ghi chép , lưu trữ , sử dụng sổ , biểu mẫu hộ tịch như sau .

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **05/2012/TT-BTP** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Tư pháp** → `CO_QUAN_BAN_HANH` (span: `[4:6]`)
- `[e3]` **sửa đổi , bổ sung một số điều của** → `TU_KHOA_PHAP_LY` (span: `[12:18]`)
- `[e4]` **Bộ trưởng Bộ Tư pháp** → `CO_QUAN_THAM_QUYEN` (span: `[7:10]`)

**Quan hệ:**
- (`e1` 05/2012/TT-BTP `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Tư pháp `[CO_QUAN_BAN_HANH]`)
- (`e1` 05/2012/TT-BTP `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)


---

### Mẫu #05_2012_TT-BTP_27486#preamble_standalone_16 (Loại: `preamble_standalone`)
> **[Bộ trưởng Bộ Tư pháp]`<CO_QUAN_THAM_QUYEN>`** ban hành Thông tư **[sửa đổi , bổ sung một số điều của]`<TU_KHOA_PHAP_LY>`** Thông tư số 08.a/2010/TT-BTP ngày 25 tháng 3 năm 2010 về việc ban hành và hướng dẫn việc ghi chép , lưu trữ , sử dụng sổ , biểu mẫu hộ tịch như sau .

**Thực thể:**
- `[e0]` **sửa đổi , bổ sung một số điều của** → `TU_KHOA_PHAP_LY` (span: `[5:11]`)
- `[e1]` **Bộ trưởng Bộ Tư pháp** → `CO_QUAN_THAM_QUYEN` (span: `[0:3]`)


---

### Mẫu #05_2012_TT-BTP_27486#body_context_17 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[05/2012/TT-BTP]`<SO_HIEU>`** ban hành **[ngày 23 tháng 05 năm 2012]`<NGAY_BAN_HANH>`** bởi **[Bộ Tư pháp]`<CO_QUAN_BAN_HANH>`** . **[Điều 1 . Những nội dung sửa đổi , bổ sung]`<DIEU>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **05/2012/TT-BTP** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Tư pháp** → `CO_QUAN_BAN_HANH` (span: `[11:13]`)
- `[e3]` **ngày 23 tháng 05 năm 2012** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 1 . Những nội dung sửa đổi , bổ sung** → `DIEU` (span: `[14:22]`)

**Quan hệ:**
- (`e1` 05/2012/TT-BTP `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Tư pháp `[CO_QUAN_BAN_HANH]`)
- (`e1` 05/2012/TT-BTP `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 05/2012/TT-BTP `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 23 tháng 05 năm 2012 `[NGAY_BAN_HANH]`)
- (`e4` Điều 1 . Những nội dung sửa đổi , bổ sung `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 05/2012/TT-BTP `[SO_HIEU]`)


---

### Mẫu #05_2012_TT-BTP_27486#body_context_18 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[05/2012/TT-BTP]`<SO_HIEU>`** của **[Bộ Tư pháp]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Hộ tịch , quốc tịch , chứng thực]`<LINH_VUC>`** . **[Điều 1]`<DIEU>`** . **[1 . Điều 3 được sửa đổi như sau : " Điều 3 . Ban hành sổ , biểu mẫu hộ tịch]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **05/2012/TT-BTP** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Tư pháp** → `CO_QUAN_BAN_HANH` (span: `[4:6]`)
- `[e3]` **Hộ tịch , quốc tịch , chứng thực** → `LINH_VUC` (span: `[8:13]`)
- `[e4]` **Điều 1** → `DIEU` (span: `[14:16]`)
- `[e5]` **1 . Điều 3 được sửa đổi như sau : " Điều 3 . Ban hành sổ , biểu mẫu hộ tịch** → `KHOAN` (span: `[17:35]`)

**Quan hệ:**
- (`e1` 05/2012/TT-BTP `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Tư pháp `[CO_QUAN_BAN_HANH]`)
- (`e1` 05/2012/TT-BTP `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 05/2012/TT-BTP `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Hộ tịch , quốc tịch , chứng thực `[LINH_VUC]`)
- (`e4` Điều 1 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 05/2012/TT-BTP `[SO_HIEU]`)
- (`e5` 1 . Điều 3 được sửa đổi như sau : " Điều 3 . Ban hành sổ , biểu mẫu hộ tịch `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 1 `[DIEU]`)
- (`e1` 05/2012/TT-BTP `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Hộ tịch , quốc tịch , chứng thực `[LINH_VUC]`)
- (`e5` 1 . Điều 3 được sửa đổi như sau : " Điều 3 . Ban hành sổ , biểu mẫu hộ tịch `[KHOAN]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Hộ tịch , quốc tịch , chứng thực `[LINH_VUC]`)


---

### Mẫu #05_2012_TT-BTP_27486#body_context_19 (Loại: `body_context`)
> **[Bộ Tư pháp]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[05/2012/TT-BTP]`<SO_HIEU>`** . **[Điều 1]`<DIEU>`** . **[1 . Điều 3 được sửa đổi như sau : Ban hành 05 loại sổ hộ tịch và 66 loại biểu mẫu hộ tịch theo danh mục kèm theo Thông tư này .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[3:4]`)
- `[e1]` **05/2012/TT-BTP** → `SO_HIEU` (span: `[5:6]`)
- `[e2]` **Bộ Tư pháp** → `CO_QUAN_BAN_HANH` (span: `[0:2]`)
- `[e3]` **Điều 1** → `DIEU` (span: `[7:9]`)
- `[e4]` **1 . Điều 3 được sửa đổi như sau : Ban hành 05 loại sổ hộ tịch và 66 loại biểu mẫu hộ tịch theo danh mục kèm theo Thông tư này .** → `KHOAN` (span: `[10:36]`)

**Quan hệ:**
- (`e1` 05/2012/TT-BTP `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Tư pháp `[CO_QUAN_BAN_HANH]`)
- (`e1` 05/2012/TT-BTP `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 1 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 05/2012/TT-BTP `[SO_HIEU]`)
- (`e4` 1 . Điều 3 được sửa đổi như sau : Ban hành 05 loại sổ hộ tịch và 66 loại biểu mẫu hộ tịch theo danh mục kèm theo Thông tư này . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 1 `[DIEU]`)


---

### Mẫu #05_2012_TT-BTP_27486#body_standalone_20 (Loại: `body_standalone`)
> **[Điều 1]`<DIEU>`** . **[1 . Điều 3 được sửa đổi như sau : Ban hành 05 loại sổ hộ tịch và 66 loại biểu mẫu hộ tịch theo danh mục kèm theo Thông tư này .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 1** → `DIEU` (span: `[0:2]`)
- `[e1]` **1 . Điều 3 được sửa đổi như sau : Ban hành 05 loại sổ hộ tịch và 66 loại biểu mẫu hộ tịch theo danh mục kèm theo Thông tư này .** → `KHOAN` (span: `[3:29]`)

**Quan hệ:**
- (`e1` 1 . Điều 3 được sửa đổi như sau : Ban hành 05 loại sổ hộ tịch và 66 loại biểu mẫu hộ tịch theo danh mục kèm theo Thông tư này . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 1 `[DIEU]`)


---

### Mẫu #05_2012_TT-BTP_27486#body_context_21 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[05/2012/TT-BTP]`<SO_HIEU>`** ban hành **[ngày 23 tháng 05 năm 2012]`<NGAY_BAN_HANH>`** bởi **[Bộ Tư pháp]`<CO_QUAN_BAN_HANH>`** . **[Điều 1]`<DIEU>`** . **[1 . Điều 3 được sửa đổi như sau : Kích cỡ của 05 loại sổ hộ tịch và 66 loại biểu mẫu hộ tịch được thống nhất sử dụng khổ giấy ( 210 x 297mm ) " .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **05/2012/TT-BTP** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Tư pháp** → `CO_QUAN_BAN_HANH` (span: `[11:13]`)
- `[e3]` **ngày 23 tháng 05 năm 2012** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 1** → `DIEU` (span: `[14:16]`)
- `[e5]` **1 . Điều 3 được sửa đổi như sau : Kích cỡ của 05 loại sổ hộ tịch và 66 loại biểu mẫu hộ tịch được thống nhất sử dụng khổ giấy ( 210 x 297mm ) " .** → `KHOAN` (span: `[17:49]`)

**Quan hệ:**
- (`e1` 05/2012/TT-BTP `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Tư pháp `[CO_QUAN_BAN_HANH]`)
- (`e1` 05/2012/TT-BTP `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 05/2012/TT-BTP `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 23 tháng 05 năm 2012 `[NGAY_BAN_HANH]`)
- (`e4` Điều 1 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 05/2012/TT-BTP `[SO_HIEU]`)
- (`e5` 1 . Điều 3 được sửa đổi như sau : Kích cỡ của 05 loại sổ hộ tịch và 66 loại biểu mẫu hộ tịch được thống nhất sử dụng khổ giấy ( 210 x 297mm ) " . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 1 `[DIEU]`)


---

### Mẫu #05_2012_TT-BTP_27486#body_context_22 (Loại: `body_context`)
> **[Bộ Tư pháp]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[05/2012/TT-BTP]`<SO_HIEU>`** . **[Điều 1]`<DIEU>`** . 2 . **[Khoản 2 Điều 4 được sửa đổi như sau : " 2 . Đăng tải trên Cổng thông tin điện tử **[Bộ Tư pháp]`<CO_QUAN_THAM_QUYEN>`** 61 biểu mẫu hộ tịch đen trắng , không có hoa văn ( bao gồm các biểu mẫu bản chính còn lại ; tất cả các biểu mẫu bản sao , biểu mẫu tờ khai và biểu mẫu khác ) , bao gồm :]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[3:4]`)
- `[e1]` **05/2012/TT-BTP** → `SO_HIEU` (span: `[5:6]`)
- `[e2]` **Bộ Tư pháp** → `CO_QUAN_BAN_HANH` (span: `[0:2]`)
- `[e3]` **Điều 1** → `DIEU` (span: `[7:9]`)
- `[e4]` **Khoản 2 Điều 4 được sửa đổi như sau : " 2 . Đăng tải trên Cổng thông tin điện tử Bộ Tư pháp 61 biểu mẫu hộ tịch đen trắng , không có hoa văn ( bao gồm các biểu mẫu bản chính còn lại ; tất cả các biểu mẫu bản sao , biểu mẫu tờ khai và biểu mẫu khác ) , bao gồm :** → `KHOAN` (span: `[12:63]`)
- `[e5]` **Bộ Tư pháp** → `CO_QUAN_THAM_QUYEN` (span: `[29:31]`) *(lồng trong `e4` (`KHOAN`))*

**Quan hệ:**
- (`e1` 05/2012/TT-BTP `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Tư pháp `[CO_QUAN_BAN_HANH]`)
- (`e1` 05/2012/TT-BTP `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 1 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 05/2012/TT-BTP `[SO_HIEU]`)
- (`e4` Khoản 2 Điều 4 được sửa đổi như sau : " 2 . Đăng tải trên Cổng thông tin điện tử Bộ Tư pháp 61 biểu mẫu hộ tịch đen trắng , không có hoa văn ( bao gồm các biểu mẫu bản chính còn lại ; tất cả các biểu mẫu bản sao , biểu mẫu tờ khai và biểu mẫu khác ) , bao gồm : `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 1 `[DIEU]`)


---

### Mẫu #05_2012_TT-BTP_27486#body_standalone_23 (Loại: `body_standalone`)
> **[Điều 1]`<DIEU>`** . 2 . **[Khoản 2 Điều 4 được sửa đổi như sau : " 2 . Đăng tải trên Cổng thông tin điện tử **[Bộ Tư pháp]`<CO_QUAN_THAM_QUYEN>`** 61 biểu mẫu hộ tịch đen trắng , không có hoa văn ( bao gồm các biểu mẫu bản chính còn lại ; tất cả các biểu mẫu bản sao , biểu mẫu tờ khai và biểu mẫu khác ) , bao gồm :]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 1** → `DIEU` (span: `[0:2]`)
- `[e1]` **Khoản 2 Điều 4 được sửa đổi như sau : " 2 . Đăng tải trên Cổng thông tin điện tử Bộ Tư pháp 61 biểu mẫu hộ tịch đen trắng , không có hoa văn ( bao gồm các biểu mẫu bản chính còn lại ; tất cả các biểu mẫu bản sao , biểu mẫu tờ khai và biểu mẫu khác ) , bao gồm :** → `KHOAN` (span: `[5:56]`)
- `[e2]` **Bộ Tư pháp** → `CO_QUAN_THAM_QUYEN` (span: `[22:24]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` Khoản 2 Điều 4 được sửa đổi như sau : " 2 . Đăng tải trên Cổng thông tin điện tử Bộ Tư pháp 61 biểu mẫu hộ tịch đen trắng , không có hoa văn ( bao gồm các biểu mẫu bản chính còn lại ; tất cả các biểu mẫu bản sao , biểu mẫu tờ khai và biểu mẫu khác ) , bao gồm : `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 1 `[DIEU]`)


---

### Mẫu #05_2012_TT-BTP_27486#body_context_24 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[05/2012/TT-BTP]`<SO_HIEU>`** ban hành **[ngày 23 tháng 05 năm 2012]`<NGAY_BAN_HANH>`** bởi **[Bộ Tư pháp]`<CO_QUAN_BAN_HANH>`** . **[Điều 1]`<DIEU>`** . **[Khoản 2]`<KHOAN>`** . **[a ) 55 biểu mẫu hộ tịch sử dụng để đăng ký các sự kiện hộ tịch **[theo quy định tại]`<TU_KHOA_PHAP_LY>`** **[Nghị định số 158/2005/NĐ-CP]`<THAM_CHIEU_PHAP_LY>`** , theo Mục A Danh mục II kèm theo Thông tư này .]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **05/2012/TT-BTP** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Tư pháp** → `CO_QUAN_BAN_HANH` (span: `[11:13]`)
- `[e3]` **ngày 23 tháng 05 năm 2012** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 1** → `DIEU` (span: `[14:16]`)
- `[e5]` **Khoản 2** → `KHOAN` (span: `[17:19]`)
- `[e6]` **a ) 55 biểu mẫu hộ tịch sử dụng để đăng ký các sự kiện hộ tịch theo quy định tại Nghị định số 158/2005/NĐ-CP , theo Mục A Danh mục II kèm theo Thông tư này .** → `DIEM` (span: `[20:47]`)
- `[e7]` **Nghị định số 158/2005/NĐ-CP** → `THAM_CHIEU_PHAP_LY` (span: `[34:37]`) *(lồng trong `e6` (`DIEM`))*
- `[e8]` **theo quy định tại** → `TU_KHOA_PHAP_LY` (span: `[31:34]`) *(lồng trong `e6` (`DIEM`))*

**Quan hệ:**
- (`e1` 05/2012/TT-BTP `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Tư pháp `[CO_QUAN_BAN_HANH]`)
- (`e1` 05/2012/TT-BTP `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 05/2012/TT-BTP `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 23 tháng 05 năm 2012 `[NGAY_BAN_HANH]`)
- (`e4` Điều 1 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 05/2012/TT-BTP `[SO_HIEU]`)
- (`e5` Khoản 2 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 1 `[DIEU]`)
- (`e6` a ) 55 biểu mẫu hộ tịch sử dụng để đăng ký các sự kiện hộ tịch theo quy định tại Nghị định số 158/2005/NĐ-CP , theo Mục A Danh mục II kèm theo Thông tư này . `[DIEM]`) ==[ **THUOC_VE** ]==> (`e5` Khoản 2 `[KHOAN]`)
- (`e8` theo quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e7` Nghị định số 158/2005/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e6` a ) 55 biểu mẫu hộ tịch sử dụng để đăng ký các sự kiện hộ tịch theo quy định tại Nghị định số 158/2005/NĐ-CP , theo Mục A Danh mục II kèm theo Thông tư này . `[DIEM]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e7` Nghị định số 158/2005/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #05_2012_TT-BTP_27486#body_standalone_25 (Loại: `body_standalone`)
> **[Điều 1]`<DIEU>`** . **[Khoản 2]`<KHOAN>`** . **[a ) 55 biểu mẫu hộ tịch sử dụng để đăng ký các sự kiện hộ tịch **[theo quy định tại]`<TU_KHOA_PHAP_LY>`** **[Nghị định số 158/2005/NĐ-CP]`<THAM_CHIEU_PHAP_LY>`** , theo Mục A Danh mục II kèm theo Thông tư này .]`<DIEM>`**

**Thực thể:**
- `[e0]` **Điều 1** → `DIEU` (span: `[0:2]`)
- `[e1]` **Khoản 2** → `KHOAN` (span: `[3:5]`)
- `[e2]` **a ) 55 biểu mẫu hộ tịch sử dụng để đăng ký các sự kiện hộ tịch theo quy định tại Nghị định số 158/2005/NĐ-CP , theo Mục A Danh mục II kèm theo Thông tư này .** → `DIEM` (span: `[6:33]`)
- `[e3]` **Nghị định số 158/2005/NĐ-CP** → `THAM_CHIEU_PHAP_LY` (span: `[20:23]`) *(lồng trong `e2` (`DIEM`))*
- `[e4]` **theo quy định tại** → `TU_KHOA_PHAP_LY` (span: `[17:20]`) *(lồng trong `e2` (`DIEM`))*

**Quan hệ:**
- (`e1` Khoản 2 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 1 `[DIEU]`)
- (`e2` a ) 55 biểu mẫu hộ tịch sử dụng để đăng ký các sự kiện hộ tịch theo quy định tại Nghị định số 158/2005/NĐ-CP , theo Mục A Danh mục II kèm theo Thông tư này . `[DIEM]`) ==[ **THUOC_VE** ]==> (`e1` Khoản 2 `[KHOAN]`)
- (`e4` theo quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Nghị định số 158/2005/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e2` a ) 55 biểu mẫu hộ tịch sử dụng để đăng ký các sự kiện hộ tịch theo quy định tại Nghị định số 158/2005/NĐ-CP , theo Mục A Danh mục II kèm theo Thông tư này . `[DIEM]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Nghị định số 158/2005/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #05_2012_TT-BTP_27486#body_context_26 (Loại: `body_context`)
> **[Bộ Tư pháp]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[05/2012/TT-BTP]`<SO_HIEU>`** . **[Điều 1]`<DIEU>`** . **[Khoản 2]`<KHOAN>`** . **[b ) 06 biểu mẫu hộ tịch sử dụng để đăng ký các sự kiện hộ tịch **[theo quy định tại]`<TU_KHOA_PHAP_LY>`** **[Nghị định số 68/2002/NĐ-CP]`<THAM_CHIEU_PHAP_LY>`** và **[Nghị định số 69/2006/NĐ-CP]`<THAM_CHIEU_PHAP_LY>`** , theo Mục B Danh mục II kèm theo Thông tư này . Cơ quan đăng ký hộ tịch và người có yêu cầu đăng ký hộ tịch được tự truy cập trên Cổng thông tin điện tử của **[Bộ Tư pháp]`<CO_QUAN_THAM_QUYEN>`** ( www . moj . gov . vn ) để in và sử dụng miễn phí 61 biểu mẫu theo hướng dẫn tại điểm a và điểm b]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[3:4]`)
- `[e1]` **05/2012/TT-BTP** → `SO_HIEU` (span: `[5:6]`)
- `[e2]` **Bộ Tư pháp** → `CO_QUAN_BAN_HANH` (span: `[0:2]`)
- `[e3]` **Điều 1** → `DIEU` (span: `[7:9]`)
- `[e4]` **Khoản 2** → `KHOAN` (span: `[10:12]`)
- `[e5]` **b ) 06 biểu mẫu hộ tịch sử dụng để đăng ký các sự kiện hộ tịch theo quy định tại Nghị định số 68/2002/NĐ-CP và Nghị định số 69/2006/NĐ-CP , theo Mục B Danh mục II kèm theo Thông tư này . Cơ quan đăng ký hộ tịch và người có yêu cầu đăng ký hộ tịch được tự truy cập trên Cổng thông tin điện tử của Bộ Tư pháp ( www . moj . gov . vn ) để in và sử dụng miễn phí 61 biểu mẫu theo hướng dẫn tại điểm a và điểm b** → `DIEM` (span: `[13:87]`)
- `[e6]` **Nghị định số 68/2002/NĐ-CP** → `THAM_CHIEU_PHAP_LY` (span: `[27:30]`) *(lồng trong `e5` (`DIEM`))*
- `[e7]` **Nghị định số 69/2006/NĐ-CP** → `THAM_CHIEU_PHAP_LY` (span: `[31:34]`) *(lồng trong `e5` (`DIEM`))*
- `[e8]` **theo quy định tại** → `TU_KHOA_PHAP_LY` (span: `[24:27]`) *(lồng trong `e5` (`DIEM`))*
- `[e9]` **Bộ Tư pháp** → `CO_QUAN_THAM_QUYEN` (span: `[61:63]`) *(lồng trong `e5` (`DIEM`))*

**Quan hệ:**
- (`e1` 05/2012/TT-BTP `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Tư pháp `[CO_QUAN_BAN_HANH]`)
- (`e1` 05/2012/TT-BTP `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 1 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 05/2012/TT-BTP `[SO_HIEU]`)
- (`e4` Khoản 2 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 1 `[DIEU]`)
- (`e5` b ) 06 biểu mẫu hộ tịch sử dụng để đăng ký các sự kiện hộ tịch theo quy định tại Nghị định số 68/2002/NĐ-CP và Nghị định số 69/2006/NĐ-CP , theo Mục B Danh mục II kèm theo Thông tư này . Cơ quan đăng ký hộ tịch và người có yêu cầu đăng ký hộ tịch được tự truy cập trên Cổng thông tin điện tử của Bộ Tư pháp ( www . moj . gov . vn ) để in và sử dụng miễn phí 61 biểu mẫu theo hướng dẫn tại điểm a và điểm b `[DIEM]`) ==[ **THUOC_VE** ]==> (`e4` Khoản 2 `[KHOAN]`)
- (`e8` theo quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e6` Nghị định số 68/2002/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e5` b ) 06 biểu mẫu hộ tịch sử dụng để đăng ký các sự kiện hộ tịch theo quy định tại Nghị định số 68/2002/NĐ-CP và Nghị định số 69/2006/NĐ-CP , theo Mục B Danh mục II kèm theo Thông tư này . Cơ quan đăng ký hộ tịch và người có yêu cầu đăng ký hộ tịch được tự truy cập trên Cổng thông tin điện tử của Bộ Tư pháp ( www . moj . gov . vn ) để in và sử dụng miễn phí 61 biểu mẫu theo hướng dẫn tại điểm a và điểm b `[DIEM]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e6` Nghị định số 68/2002/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e8` theo quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e7` Nghị định số 69/2006/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e5` b ) 06 biểu mẫu hộ tịch sử dụng để đăng ký các sự kiện hộ tịch theo quy định tại Nghị định số 68/2002/NĐ-CP và Nghị định số 69/2006/NĐ-CP , theo Mục B Danh mục II kèm theo Thông tư này . Cơ quan đăng ký hộ tịch và người có yêu cầu đăng ký hộ tịch được tự truy cập trên Cổng thông tin điện tử của Bộ Tư pháp ( www . moj . gov . vn ) để in và sử dụng miễn phí 61 biểu mẫu theo hướng dẫn tại điểm a và điểm b `[DIEM]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e7` Nghị định số 69/2006/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #05_2012_TT-BTP_27486#body_standalone_27 (Loại: `body_standalone`)
> **[Điều 1]`<DIEU>`** . **[Khoản 2]`<KHOAN>`** . **[b ) 06 biểu mẫu hộ tịch sử dụng để đăng ký các sự kiện hộ tịch **[theo quy định tại]`<TU_KHOA_PHAP_LY>`** **[Nghị định số 68/2002/NĐ-CP]`<THAM_CHIEU_PHAP_LY>`** và **[Nghị định số 69/2006/NĐ-CP]`<THAM_CHIEU_PHAP_LY>`** , theo Mục B Danh mục II kèm theo Thông tư này . Cơ quan đăng ký hộ tịch và người có yêu cầu đăng ký hộ tịch được tự truy cập trên Cổng thông tin điện tử của **[Bộ Tư pháp]`<CO_QUAN_THAM_QUYEN>`** ( www . moj . gov . vn ) để in và sử dụng miễn phí 61 biểu mẫu theo hướng dẫn tại điểm a và điểm b]`<DIEM>`**

**Thực thể:**
- `[e0]` **Điều 1** → `DIEU` (span: `[0:2]`)
- `[e1]` **Khoản 2** → `KHOAN` (span: `[3:5]`)
- `[e2]` **b ) 06 biểu mẫu hộ tịch sử dụng để đăng ký các sự kiện hộ tịch theo quy định tại Nghị định số 68/2002/NĐ-CP và Nghị định số 69/2006/NĐ-CP , theo Mục B Danh mục II kèm theo Thông tư này . Cơ quan đăng ký hộ tịch và người có yêu cầu đăng ký hộ tịch được tự truy cập trên Cổng thông tin điện tử của Bộ Tư pháp ( www . moj . gov . vn ) để in và sử dụng miễn phí 61 biểu mẫu theo hướng dẫn tại điểm a và điểm b** → `DIEM` (span: `[6:80]`)
- `[e3]` **Nghị định số 68/2002/NĐ-CP** → `THAM_CHIEU_PHAP_LY` (span: `[20:23]`) *(lồng trong `e2` (`DIEM`))*
- `[e4]` **Nghị định số 69/2006/NĐ-CP** → `THAM_CHIEU_PHAP_LY` (span: `[24:27]`) *(lồng trong `e2` (`DIEM`))*
- `[e5]` **theo quy định tại** → `TU_KHOA_PHAP_LY` (span: `[17:20]`) *(lồng trong `e2` (`DIEM`))*
- `[e6]` **Bộ Tư pháp** → `CO_QUAN_THAM_QUYEN` (span: `[54:56]`) *(lồng trong `e2` (`DIEM`))*

**Quan hệ:**
- (`e1` Khoản 2 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 1 `[DIEU]`)
- (`e2` b ) 06 biểu mẫu hộ tịch sử dụng để đăng ký các sự kiện hộ tịch theo quy định tại Nghị định số 68/2002/NĐ-CP và Nghị định số 69/2006/NĐ-CP , theo Mục B Danh mục II kèm theo Thông tư này . Cơ quan đăng ký hộ tịch và người có yêu cầu đăng ký hộ tịch được tự truy cập trên Cổng thông tin điện tử của Bộ Tư pháp ( www . moj . gov . vn ) để in và sử dụng miễn phí 61 biểu mẫu theo hướng dẫn tại điểm a và điểm b `[DIEM]`) ==[ **THUOC_VE** ]==> (`e1` Khoản 2 `[KHOAN]`)
- (`e5` theo quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Nghị định số 68/2002/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e2` b ) 06 biểu mẫu hộ tịch sử dụng để đăng ký các sự kiện hộ tịch theo quy định tại Nghị định số 68/2002/NĐ-CP và Nghị định số 69/2006/NĐ-CP , theo Mục B Danh mục II kèm theo Thông tư này . Cơ quan đăng ký hộ tịch và người có yêu cầu đăng ký hộ tịch được tự truy cập trên Cổng thông tin điện tử của Bộ Tư pháp ( www . moj . gov . vn ) để in và sử dụng miễn phí 61 biểu mẫu theo hướng dẫn tại điểm a và điểm b `[DIEM]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Nghị định số 68/2002/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e5` theo quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e4` Nghị định số 69/2006/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e2` b ) 06 biểu mẫu hộ tịch sử dụng để đăng ký các sự kiện hộ tịch theo quy định tại Nghị định số 68/2002/NĐ-CP và Nghị định số 69/2006/NĐ-CP , theo Mục B Danh mục II kèm theo Thông tư này . Cơ quan đăng ký hộ tịch và người có yêu cầu đăng ký hộ tịch được tự truy cập trên Cổng thông tin điện tử của Bộ Tư pháp ( www . moj . gov . vn ) để in và sử dụng miễn phí 61 biểu mẫu theo hướng dẫn tại điểm a và điểm b `[DIEM]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e4` Nghị định số 69/2006/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #05_2012_TT-BTP_27486#body_context_28 (Loại: `body_context`)
> **[Bộ Tư pháp]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[05/2012/TT-BTP]`<SO_HIEU>`** . **[Điều 2 . Điều khoản thi hành]`<DIEU>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[3:4]`)
- `[e1]` **05/2012/TT-BTP** → `SO_HIEU` (span: `[5:6]`)
- `[e2]` **Bộ Tư pháp** → `CO_QUAN_BAN_HANH` (span: `[0:2]`)
- `[e3]` **Điều 2 . Điều khoản thi hành** → `DIEU` (span: `[7:12]`)

**Quan hệ:**
- (`e1` 05/2012/TT-BTP `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Tư pháp `[CO_QUAN_BAN_HANH]`)
- (`e1` 05/2012/TT-BTP `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 2 . Điều khoản thi hành `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 05/2012/TT-BTP `[SO_HIEU]`)


---

### Mẫu #05_2012_TT-BTP_27486#body_context_29 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[05/2012/TT-BTP]`<SO_HIEU>`** của **[Bộ Tư pháp]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Hộ tịch , quốc tịch , chứng thực]`<LINH_VUC>`** . **[Điều 2]`<DIEU>`** . **[1 . Thông tư này có hiệu lực thi hành từ ngày 10 tháng 7 năm 2012 .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **05/2012/TT-BTP** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Tư pháp** → `CO_QUAN_BAN_HANH` (span: `[4:6]`)
- `[e3]` **Hộ tịch , quốc tịch , chứng thực** → `LINH_VUC` (span: `[8:13]`)
- `[e4]` **Điều 2** → `DIEU` (span: `[14:16]`)
- `[e5]` **1 . Thông tư này có hiệu lực thi hành từ ngày 10 tháng 7 năm 2012 .** → `KHOAN` (span: `[17:32]`)

**Quan hệ:**
- (`e1` 05/2012/TT-BTP `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Tư pháp `[CO_QUAN_BAN_HANH]`)
- (`e1` 05/2012/TT-BTP `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 05/2012/TT-BTP `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Hộ tịch , quốc tịch , chứng thực `[LINH_VUC]`)
- (`e4` Điều 2 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 05/2012/TT-BTP `[SO_HIEU]`)
- (`e5` 1 . Thông tư này có hiệu lực thi hành từ ngày 10 tháng 7 năm 2012 . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 2 `[DIEU]`)
- (`e1` 05/2012/TT-BTP `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Hộ tịch , quốc tịch , chứng thực `[LINH_VUC]`)
- (`e5` 1 . Thông tư này có hiệu lực thi hành từ ngày 10 tháng 7 năm 2012 . `[KHOAN]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Hộ tịch , quốc tịch , chứng thực `[LINH_VUC]`)


---

### Mẫu #05_2012_TT-BTP_27486#body_context_30 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[05/2012/TT-BTP]`<SO_HIEU>`** của **[Bộ Tư pháp]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Hộ tịch , quốc tịch , chứng thực]`<LINH_VUC>`** . **[Điều 2]`<DIEU>`** . **[2 . Trong quá trình triển khai thực hiện , nếu có vướng mắc , đề nghị phản ánh kịp thời về **[Bộ Tư pháp]`<CO_QUAN_THAM_QUYEN>`** để nghiên cứu sửa đổi , bổ sung .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **05/2012/TT-BTP** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Tư pháp** → `CO_QUAN_BAN_HANH` (span: `[4:6]`)
- `[e3]` **Hộ tịch , quốc tịch , chứng thực** → `LINH_VUC` (span: `[8:13]`)
- `[e4]` **Điều 2** → `DIEU` (span: `[14:16]`)
- `[e5]` **2 . Trong quá trình triển khai thực hiện , nếu có vướng mắc , đề nghị phản ánh kịp thời về Bộ Tư pháp để nghiên cứu sửa đổi , bổ sung .** → `KHOAN` (span: `[17:40]`)
- `[e6]` **Bộ Tư pháp** → `CO_QUAN_THAM_QUYEN` (span: `[32:34]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 05/2012/TT-BTP `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Tư pháp `[CO_QUAN_BAN_HANH]`)
- (`e1` 05/2012/TT-BTP `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 05/2012/TT-BTP `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Hộ tịch , quốc tịch , chứng thực `[LINH_VUC]`)
- (`e4` Điều 2 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 05/2012/TT-BTP `[SO_HIEU]`)
- (`e5` 2 . Trong quá trình triển khai thực hiện , nếu có vướng mắc , đề nghị phản ánh kịp thời về Bộ Tư pháp để nghiên cứu sửa đổi , bổ sung . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 2 `[DIEU]`)
- (`e1` 05/2012/TT-BTP `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Hộ tịch , quốc tịch , chứng thực `[LINH_VUC]`)
- (`e5` 2 . Trong quá trình triển khai thực hiện , nếu có vướng mắc , đề nghị phản ánh kịp thời về Bộ Tư pháp để nghiên cứu sửa đổi , bổ sung . `[KHOAN]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Hộ tịch , quốc tịch , chứng thực `[LINH_VUC]`)


---

### Mẫu #05_2012_TT-BTP_27486#body_context_31 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[05/2012/TT-BTP]`<SO_HIEU>`** của **[Bộ Tư pháp]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Hộ tịch , quốc tịch , chứng thực]`<LINH_VUC>`** . **[Điều 1]`<DIEU>`** . **[1 . Điều 3 được sửa đổi như sau :]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **05/2012/TT-BTP** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Tư pháp** → `CO_QUAN_BAN_HANH` (span: `[4:6]`)
- `[e3]` **Hộ tịch , quốc tịch , chứng thực** → `LINH_VUC` (span: `[8:13]`)
- `[e4]` **Điều 1** → `DIEU` (span: `[14:16]`)
- `[e5]` **1 . Điều 3 được sửa đổi như sau :** → `KHOAN` (span: `[17:26]`)

**Quan hệ:**
- (`e1` 05/2012/TT-BTP `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Tư pháp `[CO_QUAN_BAN_HANH]`)
- (`e1` 05/2012/TT-BTP `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 05/2012/TT-BTP `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Hộ tịch , quốc tịch , chứng thực `[LINH_VUC]`)
- (`e4` Điều 1 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 05/2012/TT-BTP `[SO_HIEU]`)
- (`e5` 1 . Điều 3 được sửa đổi như sau : `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 1 `[DIEU]`)
- (`e1` 05/2012/TT-BTP `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Hộ tịch , quốc tịch , chứng thực `[LINH_VUC]`)
- (`e5` 1 . Điều 3 được sửa đổi như sau : `[KHOAN]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Hộ tịch , quốc tịch , chứng thực `[LINH_VUC]`)


---

### Mẫu #05_2012_TT-BTP_27486#body_context_32 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[05/2012/TT-BTP]`<SO_HIEU>`** của **[Bộ Tư pháp]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Hộ tịch , quốc tịch , chứng thực]`<LINH_VUC>`** . **[Điều 1]`<DIEU>`** . **[2 . Đăng tải trên Cổng thông tin điện tử **[Bộ Tư pháp]`<CO_QUAN_THAM_QUYEN>`** 61 biểu mẫu hộ tịch đen trắng , không có hoa văn ( bao gồm các biểu mẫu bản chính còn lại ; tất cả các biểu mẫu bản sao , biểu mẫu tờ khai và biểu mẫu khác ) , bao gồm :]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **05/2012/TT-BTP** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Tư pháp** → `CO_QUAN_BAN_HANH` (span: `[4:6]`)
- `[e3]` **Hộ tịch , quốc tịch , chứng thực** → `LINH_VUC` (span: `[8:13]`)
- `[e4]` **Điều 1** → `DIEU` (span: `[14:16]`)
- `[e5]` **2 . Đăng tải trên Cổng thông tin điện tử Bộ Tư pháp 61 biểu mẫu hộ tịch đen trắng , không có hoa văn ( bao gồm các biểu mẫu bản chính còn lại ; tất cả các biểu mẫu bản sao , biểu mẫu tờ khai và biểu mẫu khác ) , bao gồm :** → `KHOAN` (span: `[17:58]`)
- `[e6]` **Bộ Tư pháp** → `CO_QUAN_THAM_QUYEN` (span: `[24:26]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 05/2012/TT-BTP `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Tư pháp `[CO_QUAN_BAN_HANH]`)
- (`e1` 05/2012/TT-BTP `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 05/2012/TT-BTP `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Hộ tịch , quốc tịch , chứng thực `[LINH_VUC]`)
- (`e4` Điều 1 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 05/2012/TT-BTP `[SO_HIEU]`)
- (`e5` 2 . Đăng tải trên Cổng thông tin điện tử Bộ Tư pháp 61 biểu mẫu hộ tịch đen trắng , không có hoa văn ( bao gồm các biểu mẫu bản chính còn lại ; tất cả các biểu mẫu bản sao , biểu mẫu tờ khai và biểu mẫu khác ) , bao gồm : `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 1 `[DIEU]`)
- (`e1` 05/2012/TT-BTP `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Hộ tịch , quốc tịch , chứng thực `[LINH_VUC]`)
- (`e5` 2 . Đăng tải trên Cổng thông tin điện tử Bộ Tư pháp 61 biểu mẫu hộ tịch đen trắng , không có hoa văn ( bao gồm các biểu mẫu bản chính còn lại ; tất cả các biểu mẫu bản sao , biểu mẫu tờ khai và biểu mẫu khác ) , bao gồm : `[KHOAN]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Hộ tịch , quốc tịch , chứng thực `[LINH_VUC]`)


---

### Mẫu #05_2012_TT-BTP_27486#body_standalone_33 (Loại: `body_standalone`)
> **[Điều 1]`<DIEU>`** . **[2 . Đăng tải trên Cổng thông tin điện tử **[Bộ Tư pháp]`<CO_QUAN_THAM_QUYEN>`** 61 biểu mẫu hộ tịch đen trắng , không có hoa văn ( bao gồm các biểu mẫu bản chính còn lại ; tất cả các biểu mẫu bản sao , biểu mẫu tờ khai và biểu mẫu khác ) , bao gồm :]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 1** → `DIEU` (span: `[0:2]`)
- `[e1]` **2 . Đăng tải trên Cổng thông tin điện tử Bộ Tư pháp 61 biểu mẫu hộ tịch đen trắng , không có hoa văn ( bao gồm các biểu mẫu bản chính còn lại ; tất cả các biểu mẫu bản sao , biểu mẫu tờ khai và biểu mẫu khác ) , bao gồm :** → `KHOAN` (span: `[3:44]`)
- `[e2]` **Bộ Tư pháp** → `CO_QUAN_THAM_QUYEN` (span: `[10:12]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 2 . Đăng tải trên Cổng thông tin điện tử Bộ Tư pháp 61 biểu mẫu hộ tịch đen trắng , không có hoa văn ( bao gồm các biểu mẫu bản chính còn lại ; tất cả các biểu mẫu bản sao , biểu mẫu tờ khai và biểu mẫu khác ) , bao gồm : `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 1 `[DIEU]`)


---

### Mẫu #05_2012_TT-BTP_27486#body_context_34 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[05/2012/TT-BTP]`<SO_HIEU>`** ban hành **[ngày 23 tháng 05 năm 2012]`<NGAY_BAN_HANH>`** bởi **[Bộ Tư pháp]`<CO_QUAN_BAN_HANH>`** . **[Điều 2 . Điều khoản thi hành]`<DIEU>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **05/2012/TT-BTP** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Tư pháp** → `CO_QUAN_BAN_HANH` (span: `[11:13]`)
- `[e3]` **ngày 23 tháng 05 năm 2012** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 2 . Điều khoản thi hành** → `DIEU` (span: `[14:19]`)

**Quan hệ:**
- (`e1` 05/2012/TT-BTP `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Tư pháp `[CO_QUAN_BAN_HANH]`)
- (`e1` 05/2012/TT-BTP `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 05/2012/TT-BTP `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 23 tháng 05 năm 2012 `[NGAY_BAN_HANH]`)
- (`e4` Điều 2 . Điều khoản thi hành `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 05/2012/TT-BTP `[SO_HIEU]`)


---

### Mẫu #05_2012_TT-BTP_27486#hard_negative_35 (Loại: `hard_negative`)
> CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM


---
