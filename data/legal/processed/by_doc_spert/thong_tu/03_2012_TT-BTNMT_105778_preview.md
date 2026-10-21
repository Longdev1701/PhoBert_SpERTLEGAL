# Dữ liệu gán nhãn văn bản: 03_2012_TT-BTNMT_105778
- **Thể loại**: `thong_tu`
- **Phân vùng dữ liệu**: `TRAIN`
- **Tổng số mẫu**: 93 mẫu
- **Tổng số thực thể**: 600
- **Tổng số quan hệ**: 416

---

### Mẫu #03_2012_TT-BTNMT_105778#header_0 (Loại: `header`)
> **[BỘ TÀI NGUYÊN VÀ MÔI TRƯỜNG]`<CO_QUAN_BAN_HANH>`** . CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM Độc lập - Tự do - Hạnh phúc . Số : **[03/2012/TT-BTNMT]`<SO_HIEU>`** . Hà Nội , **[ngày 12 tháng 4 năm 2012]`<NGAY_BAN_HANH>`** . **[THÔNG TƯ]`<LOAI_VAN_BAN>`**

**Thực thể:**
- `[e0]` **03/2012/TT-BTNMT** → `SO_HIEU` (span: `[19:20]`)
- `[e1]` **ngày 12 tháng 4 năm 2012** → `NGAY_BAN_HANH` (span: `[23:29]`)
- `[e2]` **BỘ TÀI NGUYÊN VÀ MÔI TRƯỜNG** → `CO_QUAN_BAN_HANH` (span: `[0:4]`)
- `[e3]` **THÔNG TƯ** → `LOAI_VAN_BAN` (span: `[30:31]`)

**Quan hệ:**
- (`e0` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` BỘ TÀI NGUYÊN VÀ MÔI TRƯỜNG `[CO_QUAN_BAN_HANH]`)
- (`e0` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e1` ngày 12 tháng 4 năm 2012 `[NGAY_BAN_HANH]`)
- (`e0` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e3` THÔNG TƯ `[LOAI_VAN_BAN]`)


---

### Mẫu #03_2012_TT-BTNMT_105778#signature_1 (Loại: `signature`)
> KT. BỘ TRƯỞNG **[THỨ TRƯỞNG]`<CHUC_DANH_NGUOI_KY>`** ( Đã ký ) **[Nguyễn Mạnh Hiển]`<NGUOI_KY>`**

**Thực thể:**
- `[e0]` **Nguyễn Mạnh Hiển** → `NGUOI_KY` (span: `[7:9]`)
- `[e1]` **THỨ TRƯỞNG** → `CHUC_DANH_NGUOI_KY` (span: `[2:3]`)

**Quan hệ:**
- (`e0` Nguyễn Mạnh Hiển `[NGUOI_KY]`) ==[ **GIU_CHUC_VU** ]==> (`e1` THỨ TRƯỞNG `[CHUC_DANH_NGUOI_KY]`)


---

### Mẫu #03_2012_TT-BTNMT_105778#meta_2 (Loại: `meta`)
> **[BỘ TÀI NGUYÊN VÀ MÔI TRƯỜNG]`<CO_QUAN_BAN_HANH>`** . CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM Độc lập - Tự do - Hạnh phúc . Số : **[03/2012/TT-BTNMT]`<SO_HIEU>`** . Hà Nội , ngày 12 tháng 4 năm 2012 . **[THÔNG TƯ]`<LOAI_VAN_BAN>`** . KT. BỘ TRƯỞNG **[THỨ TRƯỞNG]`<CHUC_DANH_NGUOI_KY>`** ( Đã ký ) **[Nguyễn Mạnh Hiển]`<NGUOI_KY>`**

**Thực thể:**
- `[e0]` **03/2012/TT-BTNMT** → `SO_HIEU` (span: `[19:20]`)
- `[e1]` **BỘ TÀI NGUYÊN VÀ MÔI TRƯỜNG** → `CO_QUAN_BAN_HANH` (span: `[0:4]`)
- `[e2]` **THÔNG TƯ** → `LOAI_VAN_BAN` (span: `[30:31]`)
- `[e3]` **Nguyễn Mạnh Hiển** → `NGUOI_KY` (span: `[39:41]`)
- `[e4]` **THỨ TRƯỞNG** → `CHUC_DANH_NGUOI_KY` (span: `[34:35]`)

**Quan hệ:**
- (`e0` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e1` BỘ TÀI NGUYÊN VÀ MÔI TRƯỜNG `[CO_QUAN_BAN_HANH]`)
- (`e0` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e2` THÔNG TƯ `[LOAI_VAN_BAN]`)
- (`e0` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **KY_BOI** ]==> (`e3` Nguyễn Mạnh Hiển `[NGUOI_KY]`)
- (`e3` Nguyễn Mạnh Hiển `[NGUOI_KY]`) ==[ **GIU_CHUC_VU** ]==> (`e4` THỨ TRƯỞNG `[CHUC_DANH_NGUOI_KY]`)


---

### Mẫu #03_2012_TT-BTNMT_105778#preamble_context_3 (Loại: `preamble_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[03/2012/TT-BTNMT]`<SO_HIEU>`** của **[Bộ Tài nguyên và Môi trường]`<CO_QUAN_BAN_HANH>`** . **[Căn cứ]`<TU_KHOA_PHAP_LY>`** **[Luật Đất đai]`<THAM_CHIEU_PHAP_LY>`** **[ngày 26 tháng 11 năm 2003]`<NGAY_THAM_CHIEU>`** ;

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **03/2012/TT-BTNMT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Tài nguyên và Môi trường** → `CO_QUAN_BAN_HANH` (span: `[4:8]`)
- `[e3]` **Luật Đất đai** → `THAM_CHIEU_PHAP_LY` (span: `[10:12]`)
- `[e4]` **Căn cứ** → `TU_KHOA_PHAP_LY` (span: `[9:10]`)
- `[e5]` **ngày 26 tháng 11 năm 2003** → `NGAY_THAM_CHIEU` (span: `[12:18]`)

**Quan hệ:**
- (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Tài nguyên và Môi trường `[CO_QUAN_BAN_HANH]`)
- (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e4` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Luật Đất đai `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Luật Đất đai `[THAM_CHIEU_PHAP_LY]`)
- (`e3` Luật Đất đai `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e5` ngày 26 tháng 11 năm 2003 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #03_2012_TT-BTNMT_105778#preamble_standalone_4 (Loại: `preamble_standalone`)
> **[Căn cứ]`<TU_KHOA_PHAP_LY>`** **[Luật Đất đai]`<THAM_CHIEU_PHAP_LY>`** **[ngày 26 tháng 11 năm 2003]`<NGAY_THAM_CHIEU>`** ;

**Thực thể:**
- `[e0]` **Luật Đất đai** → `THAM_CHIEU_PHAP_LY` (span: `[1:3]`)
- `[e1]` **Căn cứ** → `TU_KHOA_PHAP_LY` (span: `[0:1]`)
- `[e2]` **ngày 26 tháng 11 năm 2003** → `NGAY_THAM_CHIEU` (span: `[3:9]`)

**Quan hệ:**
- (`e1` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e0` Luật Đất đai `[THAM_CHIEU_PHAP_LY]`)
- (`e0` Luật Đất đai `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e2` ngày 26 tháng 11 năm 2003 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #03_2012_TT-BTNMT_105778#preamble_context_5 (Loại: `preamble_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[03/2012/TT-BTNMT]`<SO_HIEU>`** của **[Bộ Tài nguyên và Môi trường]`<CO_QUAN_BAN_HANH>`** . **[Căn cứ]`<TU_KHOA_PHAP_LY>`** **[Nghị định số 181/2004/NĐ-CP]`<THAM_CHIEU_PHAP_LY>`** **[ngày 29 tháng 10 năm 2004]`<NGAY_THAM_CHIEU>`** của **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** hướng dẫn thi hành Luật Đất đai ;

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **03/2012/TT-BTNMT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Tài nguyên và Môi trường** → `CO_QUAN_BAN_HANH` (span: `[4:8]`)
- `[e3]` **Nghị định số 181/2004/NĐ-CP** → `THAM_CHIEU_PHAP_LY` (span: `[10:13]`)
- `[e4]` **Căn cứ** → `TU_KHOA_PHAP_LY` (span: `[9:10]`)
- `[e5]` **ngày 29 tháng 10 năm 2004** → `NGAY_THAM_CHIEU` (span: `[13:19]`)
- `[e6]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[20:21]`)

**Quan hệ:**
- (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Tài nguyên và Môi trường `[CO_QUAN_BAN_HANH]`)
- (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e4` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Nghị định số 181/2004/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Nghị định số 181/2004/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e3` Nghị định số 181/2004/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e5` ngày 29 tháng 10 năm 2004 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #03_2012_TT-BTNMT_105778#preamble_standalone_6 (Loại: `preamble_standalone`)
> **[Căn cứ]`<TU_KHOA_PHAP_LY>`** **[Nghị định số 181/2004/NĐ-CP]`<THAM_CHIEU_PHAP_LY>`** **[ngày 29 tháng 10 năm 2004]`<NGAY_THAM_CHIEU>`** của **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** hướng dẫn thi hành Luật Đất đai ;

**Thực thể:**
- `[e0]` **Nghị định số 181/2004/NĐ-CP** → `THAM_CHIEU_PHAP_LY` (span: `[1:4]`)
- `[e1]` **Căn cứ** → `TU_KHOA_PHAP_LY` (span: `[0:1]`)
- `[e2]` **ngày 29 tháng 10 năm 2004** → `NGAY_THAM_CHIEU` (span: `[4:10]`)
- `[e3]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[11:12]`)

**Quan hệ:**
- (`e1` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e0` Nghị định số 181/2004/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e3` Chính phủ `[CO_QUAN_THAM_QUYEN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e0` Nghị định số 181/2004/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e0` Nghị định số 181/2004/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e2` ngày 29 tháng 10 năm 2004 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #03_2012_TT-BTNMT_105778#preamble_context_7 (Loại: `preamble_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[03/2012/TT-BTNMT]`<SO_HIEU>`** của **[Bộ Tài nguyên và Môi trường]`<CO_QUAN_BAN_HANH>`** . **[Căn cứ]`<TU_KHOA_PHAP_LY>`** **[Nghị định số 25/2008/NĐ-CP]`<THAM_CHIEU_PHAP_LY>`** **[ngày 04 tháng 3 năm 2008]`<NGAY_THAM_CHIEU>`** của **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** quy định chức năng , nhiệm vụ , quyền hạn và cơ cấu tổ chức của **[Bộ Tài nguyên và Môi trường]`<CO_QUAN_THAM_QUYEN>`** ; **[Nghị định số 19/2010/NĐ-CP]`<THAM_CHIEU_PHAP_LY>`** **[ngày 05 tháng 3 năm 2010]`<NGAY_THAM_CHIEU>`** của **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** **[sửa đổi , bổ sung]`<TU_KHOA_PHAP_LY>`** các điểm c , d , g , h và i khoản 5 Điều 2 Nghị định số 25/2008/NĐ-CP ngày 04 tháng 3 năm 2008 của **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** quy định chức năng , nhiệm vụ , quyền hạn và cơ cấu tổ chức

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **03/2012/TT-BTNMT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Tài nguyên và Môi trường** → `CO_QUAN_BAN_HANH` (span: `[4:8]`)
- `[e3]` **Nghị định số 25/2008/NĐ-CP** → `THAM_CHIEU_PHAP_LY` (span: `[10:13]`)
- `[e4]` **Nghị định số 19/2010/NĐ-CP** → `THAM_CHIEU_PHAP_LY` (span: `[36:39]`)
- `[e5]` **Căn cứ** → `TU_KHOA_PHAP_LY` (span: `[9:10]`)
- `[e6]` **sửa đổi , bổ sung** → `TU_KHOA_PHAP_LY` (span: `[47:50]`)
- `[e7]` **ngày 04 tháng 3 năm 2008** → `NGAY_THAM_CHIEU` (span: `[13:19]`)
- `[e8]` **ngày 05 tháng 3 năm 2010** → `NGAY_THAM_CHIEU` (span: `[39:45]`)
- `[e9]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[20:21]`)
- `[e10]` **Bộ Tài nguyên và Môi trường** → `CO_QUAN_THAM_QUYEN` (span: `[31:35]`)
- `[e11]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[46:47]`)
- `[e12]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[75:76]`)

**Quan hệ:**
- (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Tài nguyên và Môi trường `[CO_QUAN_BAN_HANH]`)
- (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e5` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Nghị định số 25/2008/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Nghị định số 25/2008/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e5` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e4` Nghị định số 19/2010/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e4` Nghị định số 19/2010/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e3` Nghị định số 25/2008/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e7` ngày 04 tháng 3 năm 2008 `[NGAY_THAM_CHIEU]`)
- (`e4` Nghị định số 19/2010/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e8` ngày 05 tháng 3 năm 2010 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #03_2012_TT-BTNMT_105778#preamble_standalone_8 (Loại: `preamble_standalone`)
> **[Căn cứ]`<TU_KHOA_PHAP_LY>`** **[Nghị định số 25/2008/NĐ-CP]`<THAM_CHIEU_PHAP_LY>`** **[ngày 04 tháng 3 năm 2008]`<NGAY_THAM_CHIEU>`** của **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** quy định chức năng , nhiệm vụ , quyền hạn và cơ cấu tổ chức của **[Bộ Tài nguyên và Môi trường]`<CO_QUAN_THAM_QUYEN>`** ; **[Nghị định số 19/2010/NĐ-CP]`<THAM_CHIEU_PHAP_LY>`** **[ngày 05 tháng 3 năm 2010]`<NGAY_THAM_CHIEU>`** của **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** **[sửa đổi , bổ sung]`<TU_KHOA_PHAP_LY>`** các điểm c , d , g , h và i khoản 5 Điều 2 Nghị định số 25/2008/NĐ-CP ngày 04 tháng 3 năm 2008 của **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** quy định chức năng , nhiệm vụ , quyền hạn và cơ cấu tổ chức

**Thực thể:**
- `[e0]` **Nghị định số 25/2008/NĐ-CP** → `THAM_CHIEU_PHAP_LY` (span: `[1:4]`)
- `[e1]` **Nghị định số 19/2010/NĐ-CP** → `THAM_CHIEU_PHAP_LY` (span: `[27:30]`)
- `[e2]` **Căn cứ** → `TU_KHOA_PHAP_LY` (span: `[0:1]`)
- `[e3]` **sửa đổi , bổ sung** → `TU_KHOA_PHAP_LY` (span: `[38:41]`)
- `[e4]` **ngày 04 tháng 3 năm 2008** → `NGAY_THAM_CHIEU` (span: `[4:10]`)
- `[e5]` **ngày 05 tháng 3 năm 2010** → `NGAY_THAM_CHIEU` (span: `[30:36]`)
- `[e6]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[11:12]`)
- `[e7]` **Bộ Tài nguyên và Môi trường** → `CO_QUAN_THAM_QUYEN` (span: `[22:26]`)
- `[e8]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[37:38]`)
- `[e9]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[66:67]`)

**Quan hệ:**
- (`e2` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e0` Nghị định số 25/2008/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e6` Chính phủ `[CO_QUAN_THAM_QUYEN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e0` Nghị định số 25/2008/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e2` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e1` Nghị định số 19/2010/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e7` Bộ Tài nguyên và Môi trường `[CO_QUAN_THAM_QUYEN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e1` Nghị định số 19/2010/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e0` Nghị định số 25/2008/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e4` ngày 04 tháng 3 năm 2008 `[NGAY_THAM_CHIEU]`)
- (`e1` Nghị định số 19/2010/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e5` ngày 05 tháng 3 năm 2010 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #03_2012_TT-BTNMT_105778#preamble_context_9 (Loại: `preamble_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[03/2012/TT-BTNMT]`<SO_HIEU>`** của **[Bộ Tài nguyên và Môi trường]`<CO_QUAN_BAN_HANH>`** . **[Căn cứ]`<TU_KHOA_PHAP_LY>`** **[Nghị định số 112/2008/NĐ-CP]`<THAM_CHIEU_PHAP_LY>`** **[ngày 20 tháng 10 năm 2008]`<NGAY_THAM_CHIEU>`** của **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** về quản lý , bảo vệ , khai thác tổng hợp tài nguyên và môi trường các hồ chứa thủy điện , thủy lợi ;

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **03/2012/TT-BTNMT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Tài nguyên và Môi trường** → `CO_QUAN_BAN_HANH` (span: `[4:8]`)
- `[e3]` **Nghị định số 112/2008/NĐ-CP** → `THAM_CHIEU_PHAP_LY` (span: `[10:13]`)
- `[e4]` **Căn cứ** → `TU_KHOA_PHAP_LY` (span: `[9:10]`)
- `[e5]` **ngày 20 tháng 10 năm 2008** → `NGAY_THAM_CHIEU` (span: `[13:19]`)
- `[e6]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[20:21]`)

**Quan hệ:**
- (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Tài nguyên và Môi trường `[CO_QUAN_BAN_HANH]`)
- (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e4` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Nghị định số 112/2008/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Nghị định số 112/2008/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e3` Nghị định số 112/2008/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e5` ngày 20 tháng 10 năm 2008 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #03_2012_TT-BTNMT_105778#preamble_standalone_10 (Loại: `preamble_standalone`)
> **[Căn cứ]`<TU_KHOA_PHAP_LY>`** **[Nghị định số 112/2008/NĐ-CP]`<THAM_CHIEU_PHAP_LY>`** **[ngày 20 tháng 10 năm 2008]`<NGAY_THAM_CHIEU>`** của **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** về quản lý , bảo vệ , khai thác tổng hợp tài nguyên và môi trường các hồ chứa thủy điện , thủy lợi ;

**Thực thể:**
- `[e0]` **Nghị định số 112/2008/NĐ-CP** → `THAM_CHIEU_PHAP_LY` (span: `[1:4]`)
- `[e1]` **Căn cứ** → `TU_KHOA_PHAP_LY` (span: `[0:1]`)
- `[e2]` **ngày 20 tháng 10 năm 2008** → `NGAY_THAM_CHIEU` (span: `[4:10]`)
- `[e3]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[11:12]`)

**Quan hệ:**
- (`e1` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e0` Nghị định số 112/2008/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e3` Chính phủ `[CO_QUAN_THAM_QUYEN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e0` Nghị định số 112/2008/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e0` Nghị định số 112/2008/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e2` ngày 20 tháng 10 năm 2008 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #03_2012_TT-BTNMT_105778#body_context_11 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[03/2012/TT-BTNMT]`<SO_HIEU>`** ban hành **[ngày 12 tháng 04 năm 2012]`<NGAY_BAN_HANH>`** bởi **[Bộ Tài nguyên và Môi trường]`<CO_QUAN_BAN_HANH>`** . **[Chương I. QUY ĐỊNH CHUNG]`<CHUONG>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **03/2012/TT-BTNMT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Tài nguyên và Môi trường** → `CO_QUAN_BAN_HANH` (span: `[11:15]`)
- `[e3]` **ngày 12 tháng 04 năm 2012** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Chương I. QUY ĐỊNH CHUNG** → `CHUONG` (span: `[16:20]`)

**Quan hệ:**
- (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Tài nguyên và Môi trường `[CO_QUAN_BAN_HANH]`)
- (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 12 tháng 04 năm 2012 `[NGAY_BAN_HANH]`)
- (`e4` Chương I. QUY ĐỊNH CHUNG `[CHUONG]`) ==[ **THUOC_VE** ]==> (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`)


---

### Mẫu #03_2012_TT-BTNMT_105778#body_context_12 (Loại: `body_context`)
> **[Bộ Tài nguyên và Môi trường]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[03/2012/TT-BTNMT]`<SO_HIEU>`** . **[Điều 2 . Đối tượng áp dụng . Thông tư này áp dụng đối với các cơ quan , tổ chức , **[hộ gia đình]`<TO_CHUC_DOANH_NGHIEP>`** , cá nhân trong nước và tổ chức , cá nhân nước ngoài có các hoạt động liên quan đến quản lý , sử dụng đất vùng bán ngập lòng hồ thủy điện , thủy lợi .]`<DIEU>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[5:6]`)
- `[e1]` **03/2012/TT-BTNMT** → `SO_HIEU` (span: `[7:8]`)
- `[e2]` **Bộ Tài nguyên và Môi trường** → `CO_QUAN_BAN_HANH` (span: `[0:4]`)
- `[e3]` **Điều 2 . Đối tượng áp dụng . Thông tư này áp dụng đối với các cơ quan , tổ chức , hộ gia đình , cá nhân trong nước và tổ chức , cá nhân nước ngoài có các hoạt động liên quan đến quản lý , sử dụng đất vùng bán ngập lòng hồ thủy điện , thủy lợi .** → `DIEU` (span: `[9:53]`)
- `[e4]` **hộ gia đình** → `TO_CHUC_DOANH_NGHIEP` (span: `[24:26]`) *(lồng trong `e3` (`DIEU`))*

**Quan hệ:**
- (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Tài nguyên và Môi trường `[CO_QUAN_BAN_HANH]`)
- (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 2 . Đối tượng áp dụng . Thông tư này áp dụng đối với các cơ quan , tổ chức , hộ gia đình , cá nhân trong nước và tổ chức , cá nhân nước ngoài có các hoạt động liên quan đến quản lý , sử dụng đất vùng bán ngập lòng hồ thủy điện , thủy lợi . `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`)


---

### Mẫu #03_2012_TT-BTNMT_105778#body_context_13 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[03/2012/TT-BTNMT]`<SO_HIEU>`** của **[Bộ Tài nguyên và Môi trường]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Lao động - Thương binh và Xã hội]`<LINH_VUC>`** . **[Điều 3 . Giải thích từ ngữ . Trong Thông tư này , các từ ngữ dưới đây được hiểu như sau :]`<DIEU>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **03/2012/TT-BTNMT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Tài nguyên và Môi trường** → `CO_QUAN_BAN_HANH` (span: `[4:8]`)
- `[e3]` **Lao động - Thương binh và Xã hội** → `LINH_VUC` (span: `[10:15]`)
- `[e4]` **Điều 3 . Giải thích từ ngữ . Trong Thông tư này , các từ ngữ dưới đây được hiểu như sau :** → `DIEU` (span: `[16:35]`)

**Quan hệ:**
- (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Tài nguyên và Môi trường `[CO_QUAN_BAN_HANH]`)
- (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Lao động - Thương binh và Xã hội `[LINH_VUC]`)
- (`e4` Điều 3 . Giải thích từ ngữ . Trong Thông tư này , các từ ngữ dưới đây được hiểu như sau : `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`)
- (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Lao động - Thương binh và Xã hội `[LINH_VUC]`)
- (`e4` Điều 3 . Giải thích từ ngữ . Trong Thông tư này , các từ ngữ dưới đây được hiểu như sau : `[DIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Lao động - Thương binh và Xã hội `[LINH_VUC]`)


---

### Mẫu #03_2012_TT-BTNMT_105778#body_context_14 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[03/2012/TT-BTNMT]`<SO_HIEU>`** của **[Bộ Tài nguyên và Môi trường]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Lao động - Thương binh và Xã hội]`<LINH_VUC>`** . **[Điều 3]`<DIEU>`** . **[1 . Chủ đập là tổ chức , cá nhân sở hữu đập để khai thác lợi ích của hồ chứa nước hoặc được **[cơ quan nhà nước có thẩm quyền]`<CO_QUAN_THAM_QUYEN>`** giao quản lý , vận hành khai thác hồ chứa nước .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **03/2012/TT-BTNMT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Tài nguyên và Môi trường** → `CO_QUAN_BAN_HANH` (span: `[4:8]`)
- `[e3]` **Lao động - Thương binh và Xã hội** → `LINH_VUC` (span: `[10:15]`)
- `[e4]` **Điều 3** → `DIEU` (span: `[16:18]`)
- `[e5]` **1 . Chủ đập là tổ chức , cá nhân sở hữu đập để khai thác lợi ích của hồ chứa nước hoặc được cơ quan nhà nước có thẩm quyền giao quản lý , vận hành khai thác hồ chứa nước .** → `KHOAN` (span: `[19:49]`)
- `[e6]` **cơ quan nhà nước có thẩm quyền** → `CO_QUAN_THAM_QUYEN` (span: `[37:41]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Tài nguyên và Môi trường `[CO_QUAN_BAN_HANH]`)
- (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Lao động - Thương binh và Xã hội `[LINH_VUC]`)
- (`e4` Điều 3 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`)
- (`e5` 1 . Chủ đập là tổ chức , cá nhân sở hữu đập để khai thác lợi ích của hồ chứa nước hoặc được cơ quan nhà nước có thẩm quyền giao quản lý , vận hành khai thác hồ chứa nước . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 3 `[DIEU]`)
- (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Lao động - Thương binh và Xã hội `[LINH_VUC]`)
- (`e5` 1 . Chủ đập là tổ chức , cá nhân sở hữu đập để khai thác lợi ích của hồ chứa nước hoặc được cơ quan nhà nước có thẩm quyền giao quản lý , vận hành khai thác hồ chứa nước . `[KHOAN]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Lao động - Thương binh và Xã hội `[LINH_VUC]`)


---

### Mẫu #03_2012_TT-BTNMT_105778#body_context_15 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[03/2012/TT-BTNMT]`<SO_HIEU>`** của **[Bộ Tài nguyên và Môi trường]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Lao động - Thương binh và Xã hội]`<LINH_VUC>`** . **[Chương II. QUẢN LÝ , SỬ DỤNG ĐẤT VÙNG BÁN NGẬP]`<CHUONG>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **03/2012/TT-BTNMT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Tài nguyên và Môi trường** → `CO_QUAN_BAN_HANH` (span: `[4:8]`)
- `[e3]` **Lao động - Thương binh và Xã hội** → `LINH_VUC` (span: `[10:15]`)
- `[e4]` **Chương II. QUẢN LÝ , SỬ DỤNG ĐẤT VÙNG BÁN NGẬP** → `CHUONG` (span: `[16:25]`)

**Quan hệ:**
- (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Tài nguyên và Môi trường `[CO_QUAN_BAN_HANH]`)
- (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Lao động - Thương binh và Xã hội `[LINH_VUC]`)
- (`e4` Chương II. QUẢN LÝ , SỬ DỤNG ĐẤT VÙNG BÁN NGẬP `[CHUONG]`) ==[ **THUOC_VE** ]==> (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`)
- (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Lao động - Thương binh và Xã hội `[LINH_VUC]`)


---

### Mẫu #03_2012_TT-BTNMT_105778#body_context_16 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[03/2012/TT-BTNMT]`<SO_HIEU>`** ban hành **[ngày 12 tháng 04 năm 2012]`<NGAY_BAN_HANH>`** bởi **[Bộ Tài nguyên và Môi trường]`<CO_QUAN_BAN_HANH>`** . **[Điều 4]`<DIEU>`** . **[1 . Chủ trì , phối hợp với **[Sở Tài nguyên và Môi trường]`<CO_QUAN_THAM_QUYEN>`** , **[Ủy ban nhân dân huyện , quận]`<CO_QUAN_THAM_QUYEN>`** , thị xã thuộc tỉnh , thành phố ( gọi chung là **[UBND cấp huyện]`<CO_QUAN_THAM_QUYEN>`** ) , **[Ủy ban nhân dân xã , phường , thị trấn]`<CO_QUAN_THAM_QUYEN>`** ( gọi chung là **[UBND cấp xã]`<CO_QUAN_THAM_QUYEN>`** ) nơi có đất vùng bán ngập xây dựng phương án cắm mốc giới xác định vùng bán ngập trình **[Ủy ban nhân dân tỉnh , thành phố trực thuộc Trung ương]`<CO_QUAN_THAM_QUYEN>`** ( gọi chung là **[UBND cấp tỉnh]`<CO_QUAN_THAM_QUYEN>`** ) xét duyệt .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **03/2012/TT-BTNMT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Tài nguyên và Môi trường** → `CO_QUAN_BAN_HANH` (span: `[11:15]`)
- `[e3]` **ngày 12 tháng 04 năm 2012** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 4** → `DIEU` (span: `[16:18]`)
- `[e5]` **1 . Chủ trì , phối hợp với Sở Tài nguyên và Môi trường , Ủy ban nhân dân huyện , quận , thị xã thuộc tỉnh , thành phố ( gọi chung là UBND cấp huyện ) , Ủy ban nhân dân xã , phường , thị trấn ( gọi chung là UBND cấp xã ) nơi có đất vùng bán ngập xây dựng phương án cắm mốc giới xác định vùng bán ngập trình Ủy ban nhân dân tỉnh , thành phố trực thuộc Trung ương ( gọi chung là UBND cấp tỉnh ) xét duyệt .** → `KHOAN` (span: `[19:96]`)
- `[e6]` **Sở Tài nguyên và Môi trường** → `CO_QUAN_THAM_QUYEN` (span: `[25:29]`) *(lồng trong `e5` (`KHOAN`))*
- `[e7]` **Ủy ban nhân dân huyện , quận** → `CO_QUAN_THAM_QUYEN` (span: `[30:35]`) *(lồng trong `e5` (`KHOAN`))*
- `[e8]` **UBND cấp huyện** → `CO_QUAN_THAM_QUYEN` (span: `[45:48]`) *(lồng trong `e5` (`KHOAN`))*
- `[e9]` **Ủy ban nhân dân xã , phường , thị trấn** → `CO_QUAN_THAM_QUYEN` (span: `[50:57]`) *(lồng trong `e5` (`KHOAN`))*
- `[e10]` **UBND cấp xã** → `CO_QUAN_THAM_QUYEN` (span: `[61:64]`) *(lồng trong `e5` (`KHOAN`))*
- `[e11]` **Ủy ban nhân dân tỉnh , thành phố trực thuộc Trung ương** → `CO_QUAN_THAM_QUYEN` (span: `[79:86]`) *(lồng trong `e5` (`KHOAN`))*
- `[e12]` **UBND cấp tỉnh** → `CO_QUAN_THAM_QUYEN` (span: `[90:93]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Tài nguyên và Môi trường `[CO_QUAN_BAN_HANH]`)
- (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 12 tháng 04 năm 2012 `[NGAY_BAN_HANH]`)
- (`e4` Điều 4 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`)
- (`e5` 1 . Chủ trì , phối hợp với Sở Tài nguyên và Môi trường , Ủy ban nhân dân huyện , quận , thị xã thuộc tỉnh , thành phố ( gọi chung là UBND cấp huyện ) , Ủy ban nhân dân xã , phường , thị trấn ( gọi chung là UBND cấp xã ) nơi có đất vùng bán ngập xây dựng phương án cắm mốc giới xác định vùng bán ngập trình Ủy ban nhân dân tỉnh , thành phố trực thuộc Trung ương ( gọi chung là UBND cấp tỉnh ) xét duyệt . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 4 `[DIEU]`)


---

### Mẫu #03_2012_TT-BTNMT_105778#body_standalone_17 (Loại: `body_standalone`)
> **[Điều 4]`<DIEU>`** . **[1 . Chủ trì , phối hợp với **[Sở Tài nguyên và Môi trường]`<CO_QUAN_THAM_QUYEN>`** , **[Ủy ban nhân dân huyện , quận]`<CO_QUAN_THAM_QUYEN>`** , thị xã thuộc tỉnh , thành phố ( gọi chung là **[UBND cấp huyện]`<CO_QUAN_THAM_QUYEN>`** ) , **[Ủy ban nhân dân xã , phường , thị trấn]`<CO_QUAN_THAM_QUYEN>`** ( gọi chung là **[UBND cấp xã]`<CO_QUAN_THAM_QUYEN>`** ) nơi có đất vùng bán ngập xây dựng phương án cắm mốc giới xác định vùng bán ngập trình **[Ủy ban nhân dân tỉnh , thành phố trực thuộc Trung ương]`<CO_QUAN_THAM_QUYEN>`** ( gọi chung là **[UBND cấp tỉnh]`<CO_QUAN_THAM_QUYEN>`** ) xét duyệt .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 4** → `DIEU` (span: `[0:2]`)
- `[e1]` **1 . Chủ trì , phối hợp với Sở Tài nguyên và Môi trường , Ủy ban nhân dân huyện , quận , thị xã thuộc tỉnh , thành phố ( gọi chung là UBND cấp huyện ) , Ủy ban nhân dân xã , phường , thị trấn ( gọi chung là UBND cấp xã ) nơi có đất vùng bán ngập xây dựng phương án cắm mốc giới xác định vùng bán ngập trình Ủy ban nhân dân tỉnh , thành phố trực thuộc Trung ương ( gọi chung là UBND cấp tỉnh ) xét duyệt .** → `KHOAN` (span: `[3:80]`)
- `[e2]` **Sở Tài nguyên và Môi trường** → `CO_QUAN_THAM_QUYEN` (span: `[9:13]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **Ủy ban nhân dân huyện , quận** → `CO_QUAN_THAM_QUYEN` (span: `[14:19]`) *(lồng trong `e1` (`KHOAN`))*
- `[e4]` **UBND cấp huyện** → `CO_QUAN_THAM_QUYEN` (span: `[29:32]`) *(lồng trong `e1` (`KHOAN`))*
- `[e5]` **Ủy ban nhân dân xã , phường , thị trấn** → `CO_QUAN_THAM_QUYEN` (span: `[34:41]`) *(lồng trong `e1` (`KHOAN`))*
- `[e6]` **UBND cấp xã** → `CO_QUAN_THAM_QUYEN` (span: `[45:48]`) *(lồng trong `e1` (`KHOAN`))*
- `[e7]` **Ủy ban nhân dân tỉnh , thành phố trực thuộc Trung ương** → `CO_QUAN_THAM_QUYEN` (span: `[63:70]`) *(lồng trong `e1` (`KHOAN`))*
- `[e8]` **UBND cấp tỉnh** → `CO_QUAN_THAM_QUYEN` (span: `[74:77]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 1 . Chủ trì , phối hợp với Sở Tài nguyên và Môi trường , Ủy ban nhân dân huyện , quận , thị xã thuộc tỉnh , thành phố ( gọi chung là UBND cấp huyện ) , Ủy ban nhân dân xã , phường , thị trấn ( gọi chung là UBND cấp xã ) nơi có đất vùng bán ngập xây dựng phương án cắm mốc giới xác định vùng bán ngập trình Ủy ban nhân dân tỉnh , thành phố trực thuộc Trung ương ( gọi chung là UBND cấp tỉnh ) xét duyệt . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 4 `[DIEU]`)


---

### Mẫu #03_2012_TT-BTNMT_105778#body_context_18 (Loại: `body_context`)
> **[Bộ Tài nguyên và Môi trường]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[03/2012/TT-BTNMT]`<SO_HIEU>`** . **[Điều 4]`<DIEU>`** . **[2 . Chủ trì , phối hợp với **[Ủy ban nhân dân cấp huyện]`<CO_QUAN_THAM_QUYEN>`** , **[Ủy ban nhân dân cấp xã]`<CO_QUAN_THAM_QUYEN>`** nơi có đất vùng bán ngập thực hiện việc cắm mốc giới trên thực địa sau khi phương án cắm mốc giới vùng bán ngập được xét duyệt .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[5:6]`)
- `[e1]` **03/2012/TT-BTNMT** → `SO_HIEU` (span: `[7:8]`)
- `[e2]` **Bộ Tài nguyên và Môi trường** → `CO_QUAN_BAN_HANH` (span: `[0:4]`)
- `[e3]` **Điều 4** → `DIEU` (span: `[9:11]`)
- `[e4]` **2 . Chủ trì , phối hợp với Ủy ban nhân dân cấp huyện , Ủy ban nhân dân cấp xã nơi có đất vùng bán ngập thực hiện việc cắm mốc giới trên thực địa sau khi phương án cắm mốc giới vùng bán ngập được xét duyệt .** → `KHOAN` (span: `[12:50]`)
- `[e5]` **Ủy ban nhân dân cấp huyện** → `CO_QUAN_THAM_QUYEN` (span: `[18:22]`) *(lồng trong `e4` (`KHOAN`))*
- `[e6]` **Ủy ban nhân dân cấp xã** → `CO_QUAN_THAM_QUYEN` (span: `[23:27]`) *(lồng trong `e4` (`KHOAN`))*

**Quan hệ:**
- (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Tài nguyên và Môi trường `[CO_QUAN_BAN_HANH]`)
- (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 4 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`)
- (`e4` 2 . Chủ trì , phối hợp với Ủy ban nhân dân cấp huyện , Ủy ban nhân dân cấp xã nơi có đất vùng bán ngập thực hiện việc cắm mốc giới trên thực địa sau khi phương án cắm mốc giới vùng bán ngập được xét duyệt . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 4 `[DIEU]`)


---

### Mẫu #03_2012_TT-BTNMT_105778#body_standalone_19 (Loại: `body_standalone`)
> **[Điều 4]`<DIEU>`** . **[2 . Chủ trì , phối hợp với **[Ủy ban nhân dân cấp huyện]`<CO_QUAN_THAM_QUYEN>`** , **[Ủy ban nhân dân cấp xã]`<CO_QUAN_THAM_QUYEN>`** nơi có đất vùng bán ngập thực hiện việc cắm mốc giới trên thực địa sau khi phương án cắm mốc giới vùng bán ngập được xét duyệt .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 4** → `DIEU` (span: `[0:2]`)
- `[e1]` **2 . Chủ trì , phối hợp với Ủy ban nhân dân cấp huyện , Ủy ban nhân dân cấp xã nơi có đất vùng bán ngập thực hiện việc cắm mốc giới trên thực địa sau khi phương án cắm mốc giới vùng bán ngập được xét duyệt .** → `KHOAN` (span: `[3:41]`)
- `[e2]` **Ủy ban nhân dân cấp huyện** → `CO_QUAN_THAM_QUYEN` (span: `[9:13]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **Ủy ban nhân dân cấp xã** → `CO_QUAN_THAM_QUYEN` (span: `[14:18]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 2 . Chủ trì , phối hợp với Ủy ban nhân dân cấp huyện , Ủy ban nhân dân cấp xã nơi có đất vùng bán ngập thực hiện việc cắm mốc giới trên thực địa sau khi phương án cắm mốc giới vùng bán ngập được xét duyệt . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 4 `[DIEU]`)


---

### Mẫu #03_2012_TT-BTNMT_105778#body_context_20 (Loại: `body_context`)
> **[Bộ Tài nguyên và Môi trường]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[03/2012/TT-BTNMT]`<SO_HIEU>`** . **[Điều 4]`<DIEU>`** . **[3 . Bàn giao mốc giới cho **[Ủy ban nhân dân cấp xã]`<CO_QUAN_THAM_QUYEN>`** nơi đất có vùng bán ngập để quản lý .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[5:6]`)
- `[e1]` **03/2012/TT-BTNMT** → `SO_HIEU` (span: `[7:8]`)
- `[e2]` **Bộ Tài nguyên và Môi trường** → `CO_QUAN_BAN_HANH` (span: `[0:4]`)
- `[e3]` **Điều 4** → `DIEU` (span: `[9:11]`)
- `[e4]` **3 . Bàn giao mốc giới cho Ủy ban nhân dân cấp xã nơi đất có vùng bán ngập để quản lý .** → `KHOAN` (span: `[12:30]`)
- `[e5]` **Ủy ban nhân dân cấp xã** → `CO_QUAN_THAM_QUYEN` (span: `[17:21]`) *(lồng trong `e4` (`KHOAN`))*

**Quan hệ:**
- (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Tài nguyên và Môi trường `[CO_QUAN_BAN_HANH]`)
- (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 4 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`)
- (`e4` 3 . Bàn giao mốc giới cho Ủy ban nhân dân cấp xã nơi đất có vùng bán ngập để quản lý . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 4 `[DIEU]`)


---

### Mẫu #03_2012_TT-BTNMT_105778#body_context_21 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[03/2012/TT-BTNMT]`<SO_HIEU>`** của **[Bộ Tài nguyên và Môi trường]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Lao động - Thương binh và Xã hội]`<LINH_VUC>`** . **[Điều 4]`<DIEU>`** . **[4 . Hồ sơ mốc giới đất vùng bán ngập lưu tại **[Sở Tài nguyên và Môi trường]`<CO_QUAN_THAM_QUYEN>`** ( bản gốc ) và **[Ủy ban nhân dân cấp xã]`<CO_QUAN_THAM_QUYEN>`** , **[Phòng Tài nguyên và Môi trường]`<CO_QUAN_THAM_QUYEN>`** , Chủ đập ( bản sao ) ; trường hợp có bản số thì hồ sơ mốc giới được lưu trong cơ sở dữ liệu đất đai của **[Sở Tài nguyên và Môi trường]`<CO_QUAN_THAM_QUYEN>`** .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **03/2012/TT-BTNMT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Tài nguyên và Môi trường** → `CO_QUAN_BAN_HANH` (span: `[4:8]`)
- `[e3]` **Lao động - Thương binh và Xã hội** → `LINH_VUC` (span: `[10:15]`)
- `[e4]` **Điều 4** → `DIEU` (span: `[16:18]`)
- `[e5]` **4 . Hồ sơ mốc giới đất vùng bán ngập lưu tại Sở Tài nguyên và Môi trường ( bản gốc ) và Ủy ban nhân dân cấp xã , Phòng Tài nguyên và Môi trường , Chủ đập ( bản sao ) ; trường hợp có bản số thì hồ sơ mốc giới được lưu trong cơ sở dữ liệu đất đai của Sở Tài nguyên và Môi trường .** → `KHOAN` (span: `[19:72]`)
- `[e6]` **Sở Tài nguyên và Môi trường** → `CO_QUAN_THAM_QUYEN` (span: `[29:33]`) *(lồng trong `e5` (`KHOAN`))*
- `[e7]` **Ủy ban nhân dân cấp xã** → `CO_QUAN_THAM_QUYEN` (span: `[37:41]`) *(lồng trong `e5` (`KHOAN`))*
- `[e8]` **Phòng Tài nguyên và Môi trường** → `CO_QUAN_THAM_QUYEN` (span: `[42:46]`) *(lồng trong `e5` (`KHOAN`))*
- `[e9]` **Sở Tài nguyên và Môi trường** → `CO_QUAN_THAM_QUYEN` (span: `[67:71]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Tài nguyên và Môi trường `[CO_QUAN_BAN_HANH]`)
- (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Lao động - Thương binh và Xã hội `[LINH_VUC]`)
- (`e4` Điều 4 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`)
- (`e5` 4 . Hồ sơ mốc giới đất vùng bán ngập lưu tại Sở Tài nguyên và Môi trường ( bản gốc ) và Ủy ban nhân dân cấp xã , Phòng Tài nguyên và Môi trường , Chủ đập ( bản sao ) ; trường hợp có bản số thì hồ sơ mốc giới được lưu trong cơ sở dữ liệu đất đai của Sở Tài nguyên và Môi trường . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 4 `[DIEU]`)
- (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Lao động - Thương binh và Xã hội `[LINH_VUC]`)
- (`e5` 4 . Hồ sơ mốc giới đất vùng bán ngập lưu tại Sở Tài nguyên và Môi trường ( bản gốc ) và Ủy ban nhân dân cấp xã , Phòng Tài nguyên và Môi trường , Chủ đập ( bản sao ) ; trường hợp có bản số thì hồ sơ mốc giới được lưu trong cơ sở dữ liệu đất đai của Sở Tài nguyên và Môi trường . `[KHOAN]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Lao động - Thương binh và Xã hội `[LINH_VUC]`)


---

### Mẫu #03_2012_TT-BTNMT_105778#body_standalone_22 (Loại: `body_standalone`)
> **[Điều 4]`<DIEU>`** . **[4 . Hồ sơ mốc giới đất vùng bán ngập lưu tại **[Sở Tài nguyên và Môi trường]`<CO_QUAN_THAM_QUYEN>`** ( bản gốc ) và **[Ủy ban nhân dân cấp xã]`<CO_QUAN_THAM_QUYEN>`** , **[Phòng Tài nguyên và Môi trường]`<CO_QUAN_THAM_QUYEN>`** , Chủ đập ( bản sao ) ; trường hợp có bản số thì hồ sơ mốc giới được lưu trong cơ sở dữ liệu đất đai của **[Sở Tài nguyên và Môi trường]`<CO_QUAN_THAM_QUYEN>`** .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 4** → `DIEU` (span: `[0:2]`)
- `[e1]` **4 . Hồ sơ mốc giới đất vùng bán ngập lưu tại Sở Tài nguyên và Môi trường ( bản gốc ) và Ủy ban nhân dân cấp xã , Phòng Tài nguyên và Môi trường , Chủ đập ( bản sao ) ; trường hợp có bản số thì hồ sơ mốc giới được lưu trong cơ sở dữ liệu đất đai của Sở Tài nguyên và Môi trường .** → `KHOAN` (span: `[3:56]`)
- `[e2]` **Sở Tài nguyên và Môi trường** → `CO_QUAN_THAM_QUYEN` (span: `[13:17]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **Ủy ban nhân dân cấp xã** → `CO_QUAN_THAM_QUYEN` (span: `[21:25]`) *(lồng trong `e1` (`KHOAN`))*
- `[e4]` **Phòng Tài nguyên và Môi trường** → `CO_QUAN_THAM_QUYEN` (span: `[26:30]`) *(lồng trong `e1` (`KHOAN`))*
- `[e5]` **Sở Tài nguyên và Môi trường** → `CO_QUAN_THAM_QUYEN` (span: `[51:55]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 4 . Hồ sơ mốc giới đất vùng bán ngập lưu tại Sở Tài nguyên và Môi trường ( bản gốc ) và Ủy ban nhân dân cấp xã , Phòng Tài nguyên và Môi trường , Chủ đập ( bản sao ) ; trường hợp có bản số thì hồ sơ mốc giới được lưu trong cơ sở dữ liệu đất đai của Sở Tài nguyên và Môi trường . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 4 `[DIEU]`)


---

### Mẫu #03_2012_TT-BTNMT_105778#body_context_23 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[03/2012/TT-BTNMT]`<SO_HIEU>`** của **[Bộ Tài nguyên và Môi trường]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Lao động - Thương binh và Xã hội]`<LINH_VUC>`** . **[Điều 5 . Xây dựng **[phương án sử dụng đất]`<GIAY_TO_HO_SO>`** vùng bán ngập phục vụ sản xuất nông , lâm nghiệp]`<DIEU>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **03/2012/TT-BTNMT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Tài nguyên và Môi trường** → `CO_QUAN_BAN_HANH` (span: `[4:8]`)
- `[e3]` **Lao động - Thương binh và Xã hội** → `LINH_VUC` (span: `[10:15]`)
- `[e4]` **Điều 5 . Xây dựng phương án sử dụng đất vùng bán ngập phục vụ sản xuất nông , lâm nghiệp** → `DIEU` (span: `[16:31]`)
- `[e5]` **phương án sử dụng đất** → `GIAY_TO_HO_SO` (span: `[20:23]`) *(lồng trong `e4` (`DIEU`))*

**Quan hệ:**
- (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Tài nguyên và Môi trường `[CO_QUAN_BAN_HANH]`)
- (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Lao động - Thương binh và Xã hội `[LINH_VUC]`)
- (`e4` Điều 5 . Xây dựng phương án sử dụng đất vùng bán ngập phục vụ sản xuất nông , lâm nghiệp `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`)
- (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Lao động - Thương binh và Xã hội `[LINH_VUC]`)
- (`e4` Điều 5 . Xây dựng phương án sử dụng đất vùng bán ngập phục vụ sản xuất nông , lâm nghiệp `[DIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Lao động - Thương binh và Xã hội `[LINH_VUC]`)


---

### Mẫu #03_2012_TT-BTNMT_105778#body_context_24 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[03/2012/TT-BTNMT]`<SO_HIEU>`** của **[Bộ Tài nguyên và Môi trường]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Lao động - Thương binh và Xã hội]`<LINH_VUC>`** . **[Điều 5]`<DIEU>`** . **[1 . **[Phương án sử dụng đất vùng bán ngập phải đảm bảo mục đích chính]`<GIAY_TO_HO_SO>`** là thủy điện , thủy lợi , kết hợp với mục đích sản xuất nông , lâm nghiệp được **[quy định tại]`<TU_KHOA_PHAP_LY>`** **[Nghị định số 112/2008/NĐ-CP]`<THAM_CHIEU_PHAP_LY>`** **[ngày 20 tháng 10 năm 2008]`<NGAY_THAM_CHIEU>`** của **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** về quản lý , bảo vệ , khai thác tổng hợp tài nguyên và môi trường các hồ chứa thủy điện , thủy lợi , gồm : phát triển rừng , trồng cây lâu năm , trồng cây hàng năm , nuôi trồng thủy sản theo mùa vụ .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **03/2012/TT-BTNMT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Tài nguyên và Môi trường** → `CO_QUAN_BAN_HANH` (span: `[4:8]`)
- `[e3]` **Lao động - Thương binh và Xã hội** → `LINH_VUC` (span: `[10:15]`)
- `[e4]` **Điều 5** → `DIEU` (span: `[16:18]`)
- `[e5]` **1 . Phương án sử dụng đất vùng bán ngập phải đảm bảo mục đích chính là thủy điện , thủy lợi , kết hợp với mục đích sản xuất nông , lâm nghiệp được quy định tại Nghị định số 112/2008/NĐ-CP ngày 20 tháng 10 năm 2008 của Chính phủ về quản lý , bảo vệ , khai thác tổng hợp tài nguyên và môi trường các hồ chứa thủy điện , thủy lợi , gồm : phát triển rừng , trồng cây lâu năm , trồng cây hàng năm , nuôi trồng thủy sản theo mùa vụ .** → `KHOAN` (span: `[19:93]`)
- `[e6]` **Phương án sử dụng đất vùng bán ngập phải đảm bảo mục đích chính** → `GIAY_TO_HO_SO` (span: `[21:31]`) *(lồng trong `e5` (`KHOAN`))*
- `[e7]` **Nghị định số 112/2008/NĐ-CP** → `THAM_CHIEU_PHAP_LY` (span: `[46:49]`) *(lồng trong `e5` (`KHOAN`))*
- `[e8]` **quy định tại** → `TU_KHOA_PHAP_LY` (span: `[44:46]`) *(lồng trong `e5` (`KHOAN`))*
- `[e9]` **ngày 20 tháng 10 năm 2008** → `NGAY_THAM_CHIEU` (span: `[49:55]`) *(lồng trong `e5` (`KHOAN`))*
- `[e10]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[56:57]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Tài nguyên và Môi trường `[CO_QUAN_BAN_HANH]`)
- (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Lao động - Thương binh và Xã hội `[LINH_VUC]`)
- (`e4` Điều 5 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`)
- (`e5` 1 . Phương án sử dụng đất vùng bán ngập phải đảm bảo mục đích chính là thủy điện , thủy lợi , kết hợp với mục đích sản xuất nông , lâm nghiệp được quy định tại Nghị định số 112/2008/NĐ-CP ngày 20 tháng 10 năm 2008 của Chính phủ về quản lý , bảo vệ , khai thác tổng hợp tài nguyên và môi trường các hồ chứa thủy điện , thủy lợi , gồm : phát triển rừng , trồng cây lâu năm , trồng cây hàng năm , nuôi trồng thủy sản theo mùa vụ . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 5 `[DIEU]`)
- (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Lao động - Thương binh và Xã hội `[LINH_VUC]`)
- (`e5` 1 . Phương án sử dụng đất vùng bán ngập phải đảm bảo mục đích chính là thủy điện , thủy lợi , kết hợp với mục đích sản xuất nông , lâm nghiệp được quy định tại Nghị định số 112/2008/NĐ-CP ngày 20 tháng 10 năm 2008 của Chính phủ về quản lý , bảo vệ , khai thác tổng hợp tài nguyên và môi trường các hồ chứa thủy điện , thủy lợi , gồm : phát triển rừng , trồng cây lâu năm , trồng cây hàng năm , nuôi trồng thủy sản theo mùa vụ . `[KHOAN]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Lao động - Thương binh và Xã hội `[LINH_VUC]`)
- (`e8` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e7` Nghị định số 112/2008/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e5` 1 . Phương án sử dụng đất vùng bán ngập phải đảm bảo mục đích chính là thủy điện , thủy lợi , kết hợp với mục đích sản xuất nông , lâm nghiệp được quy định tại Nghị định số 112/2008/NĐ-CP ngày 20 tháng 10 năm 2008 của Chính phủ về quản lý , bảo vệ , khai thác tổng hợp tài nguyên và môi trường các hồ chứa thủy điện , thủy lợi , gồm : phát triển rừng , trồng cây lâu năm , trồng cây hàng năm , nuôi trồng thủy sản theo mùa vụ . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e7` Nghị định số 112/2008/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e7` Nghị định số 112/2008/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e9` ngày 20 tháng 10 năm 2008 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #03_2012_TT-BTNMT_105778#body_standalone_25 (Loại: `body_standalone`)
> **[Điều 5]`<DIEU>`** . **[1 . **[Phương án sử dụng đất vùng bán ngập phải đảm bảo mục đích chính]`<GIAY_TO_HO_SO>`** là thủy điện , thủy lợi , kết hợp với mục đích sản xuất nông , lâm nghiệp được **[quy định tại]`<TU_KHOA_PHAP_LY>`** **[Nghị định số 112/2008/NĐ-CP]`<THAM_CHIEU_PHAP_LY>`** **[ngày 20 tháng 10 năm 2008]`<NGAY_THAM_CHIEU>`** của **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** về quản lý , bảo vệ , khai thác tổng hợp tài nguyên và môi trường các hồ chứa thủy điện , thủy lợi , gồm : phát triển rừng , trồng cây lâu năm , trồng cây hàng năm , nuôi trồng thủy sản theo mùa vụ .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 5** → `DIEU` (span: `[0:2]`)
- `[e1]` **1 . Phương án sử dụng đất vùng bán ngập phải đảm bảo mục đích chính là thủy điện , thủy lợi , kết hợp với mục đích sản xuất nông , lâm nghiệp được quy định tại Nghị định số 112/2008/NĐ-CP ngày 20 tháng 10 năm 2008 của Chính phủ về quản lý , bảo vệ , khai thác tổng hợp tài nguyên và môi trường các hồ chứa thủy điện , thủy lợi , gồm : phát triển rừng , trồng cây lâu năm , trồng cây hàng năm , nuôi trồng thủy sản theo mùa vụ .** → `KHOAN` (span: `[3:77]`)
- `[e2]` **Phương án sử dụng đất vùng bán ngập phải đảm bảo mục đích chính** → `GIAY_TO_HO_SO` (span: `[5:15]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **Nghị định số 112/2008/NĐ-CP** → `THAM_CHIEU_PHAP_LY` (span: `[30:33]`) *(lồng trong `e1` (`KHOAN`))*
- `[e4]` **quy định tại** → `TU_KHOA_PHAP_LY` (span: `[28:30]`) *(lồng trong `e1` (`KHOAN`))*
- `[e5]` **ngày 20 tháng 10 năm 2008** → `NGAY_THAM_CHIEU` (span: `[33:39]`) *(lồng trong `e1` (`KHOAN`))*
- `[e6]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[40:41]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 1 . Phương án sử dụng đất vùng bán ngập phải đảm bảo mục đích chính là thủy điện , thủy lợi , kết hợp với mục đích sản xuất nông , lâm nghiệp được quy định tại Nghị định số 112/2008/NĐ-CP ngày 20 tháng 10 năm 2008 của Chính phủ về quản lý , bảo vệ , khai thác tổng hợp tài nguyên và môi trường các hồ chứa thủy điện , thủy lợi , gồm : phát triển rừng , trồng cây lâu năm , trồng cây hàng năm , nuôi trồng thủy sản theo mùa vụ . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 5 `[DIEU]`)
- (`e4` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Nghị định số 112/2008/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 1 . Phương án sử dụng đất vùng bán ngập phải đảm bảo mục đích chính là thủy điện , thủy lợi , kết hợp với mục đích sản xuất nông , lâm nghiệp được quy định tại Nghị định số 112/2008/NĐ-CP ngày 20 tháng 10 năm 2008 của Chính phủ về quản lý , bảo vệ , khai thác tổng hợp tài nguyên và môi trường các hồ chứa thủy điện , thủy lợi , gồm : phát triển rừng , trồng cây lâu năm , trồng cây hàng năm , nuôi trồng thủy sản theo mùa vụ . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Nghị định số 112/2008/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e3` Nghị định số 112/2008/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e5` ngày 20 tháng 10 năm 2008 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #03_2012_TT-BTNMT_105778#body_context_26 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[03/2012/TT-BTNMT]`<SO_HIEU>`** của **[Bộ Tài nguyên và Môi trường]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Lao động - Thương binh và Xã hội]`<LINH_VUC>`** . **[Điều 5]`<DIEU>`** . **[2 . **[Phương án sử dụng đất]`<GIAY_TO_HO_SO>`** vùng bán ngập phải khoanh định được diện tích đất sử dụng vào từng mục đích : phát triển rừng , trồng cây lâu năm , trồng cây hàng năm , nuôi trồng thủy sản theo mùa vụ và do **[Ủy ban nhân dân cấp xã]`<CO_QUAN_THAM_QUYEN>`** nơi có đất vùng bán ngập chủ trì , phối hợp với Chủ đập xây dựng , trình **[Ủy ban nhân dân cấp huyện]`<CO_QUAN_THAM_QUYEN>`** xét duyệt .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **03/2012/TT-BTNMT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Tài nguyên và Môi trường** → `CO_QUAN_BAN_HANH` (span: `[4:8]`)
- `[e3]` **Lao động - Thương binh và Xã hội** → `LINH_VUC` (span: `[10:15]`)
- `[e4]` **Điều 5** → `DIEU` (span: `[16:18]`)
- `[e5]` **2 . Phương án sử dụng đất vùng bán ngập phải khoanh định được diện tích đất sử dụng vào từng mục đích : phát triển rừng , trồng cây lâu năm , trồng cây hàng năm , nuôi trồng thủy sản theo mùa vụ và do Ủy ban nhân dân cấp xã nơi có đất vùng bán ngập chủ trì , phối hợp với Chủ đập xây dựng , trình Ủy ban nhân dân cấp huyện xét duyệt .** → `KHOAN` (span: `[19:81]`)
- `[e6]` **Ủy ban nhân dân cấp xã** → `CO_QUAN_THAM_QUYEN` (span: `[56:60]`) *(lồng trong `e5` (`KHOAN`))*
- `[e7]` **Ủy ban nhân dân cấp huyện** → `CO_QUAN_THAM_QUYEN` (span: `[75:79]`) *(lồng trong `e5` (`KHOAN`))*
- `[e8]` **Phương án sử dụng đất** → `GIAY_TO_HO_SO` (span: `[21:24]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Tài nguyên và Môi trường `[CO_QUAN_BAN_HANH]`)
- (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Lao động - Thương binh và Xã hội `[LINH_VUC]`)
- (`e4` Điều 5 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`)
- (`e5` 2 . Phương án sử dụng đất vùng bán ngập phải khoanh định được diện tích đất sử dụng vào từng mục đích : phát triển rừng , trồng cây lâu năm , trồng cây hàng năm , nuôi trồng thủy sản theo mùa vụ và do Ủy ban nhân dân cấp xã nơi có đất vùng bán ngập chủ trì , phối hợp với Chủ đập xây dựng , trình Ủy ban nhân dân cấp huyện xét duyệt . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 5 `[DIEU]`)
- (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Lao động - Thương binh và Xã hội `[LINH_VUC]`)
- (`e5` 2 . Phương án sử dụng đất vùng bán ngập phải khoanh định được diện tích đất sử dụng vào từng mục đích : phát triển rừng , trồng cây lâu năm , trồng cây hàng năm , nuôi trồng thủy sản theo mùa vụ và do Ủy ban nhân dân cấp xã nơi có đất vùng bán ngập chủ trì , phối hợp với Chủ đập xây dựng , trình Ủy ban nhân dân cấp huyện xét duyệt . `[KHOAN]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Lao động - Thương binh và Xã hội `[LINH_VUC]`)


---

### Mẫu #03_2012_TT-BTNMT_105778#body_standalone_27 (Loại: `body_standalone`)
> **[Điều 5]`<DIEU>`** . **[2 . **[Phương án sử dụng đất]`<GIAY_TO_HO_SO>`** vùng bán ngập phải khoanh định được diện tích đất sử dụng vào từng mục đích : phát triển rừng , trồng cây lâu năm , trồng cây hàng năm , nuôi trồng thủy sản theo mùa vụ và do **[Ủy ban nhân dân cấp xã]`<CO_QUAN_THAM_QUYEN>`** nơi có đất vùng bán ngập chủ trì , phối hợp với Chủ đập xây dựng , trình **[Ủy ban nhân dân cấp huyện]`<CO_QUAN_THAM_QUYEN>`** xét duyệt .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 5** → `DIEU` (span: `[0:2]`)
- `[e1]` **2 . Phương án sử dụng đất vùng bán ngập phải khoanh định được diện tích đất sử dụng vào từng mục đích : phát triển rừng , trồng cây lâu năm , trồng cây hàng năm , nuôi trồng thủy sản theo mùa vụ và do Ủy ban nhân dân cấp xã nơi có đất vùng bán ngập chủ trì , phối hợp với Chủ đập xây dựng , trình Ủy ban nhân dân cấp huyện xét duyệt .** → `KHOAN` (span: `[3:65]`)
- `[e2]` **Ủy ban nhân dân cấp xã** → `CO_QUAN_THAM_QUYEN` (span: `[40:44]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **Ủy ban nhân dân cấp huyện** → `CO_QUAN_THAM_QUYEN` (span: `[59:63]`) *(lồng trong `e1` (`KHOAN`))*
- `[e4]` **Phương án sử dụng đất** → `GIAY_TO_HO_SO` (span: `[5:8]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 2 . Phương án sử dụng đất vùng bán ngập phải khoanh định được diện tích đất sử dụng vào từng mục đích : phát triển rừng , trồng cây lâu năm , trồng cây hàng năm , nuôi trồng thủy sản theo mùa vụ và do Ủy ban nhân dân cấp xã nơi có đất vùng bán ngập chủ trì , phối hợp với Chủ đập xây dựng , trình Ủy ban nhân dân cấp huyện xét duyệt . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 5 `[DIEU]`)


---

### Mẫu #03_2012_TT-BTNMT_105778#body_context_28 (Loại: `body_context`)
> **[Bộ Tài nguyên và Môi trường]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[03/2012/TT-BTNMT]`<SO_HIEU>`** . **[Điều 5]`<DIEU>`** . **[3 . Dự thảo **[phương án sử dụng đất]`<GIAY_TO_HO_SO>`** vùng bán ngập phải được niêm yết công khai tại trụ sở **[Ủy ban nhân dân cấp xã]`<CO_QUAN_THAM_QUYEN>`** nơi có đất vùng bán ngập trong thời hạn ba mươi ( 30 ) ngày để lấy ý kiến đóng góp của nhân dân , trước khi trình **[Ủy ban nhân dân cấp huyện]`<CO_QUAN_THAM_QUYEN>`** xét duyệt .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[5:6]`)
- `[e1]` **03/2012/TT-BTNMT** → `SO_HIEU` (span: `[7:8]`)
- `[e2]` **Bộ Tài nguyên và Môi trường** → `CO_QUAN_BAN_HANH` (span: `[0:4]`)
- `[e3]` **Điều 5** → `DIEU` (span: `[9:11]`)
- `[e4]` **3 . Dự thảo phương án sử dụng đất vùng bán ngập phải được niêm yết công khai tại trụ sở Ủy ban nhân dân cấp xã nơi có đất vùng bán ngập trong thời hạn ba mươi ( 30 ) ngày để lấy ý kiến đóng góp của nhân dân , trước khi trình Ủy ban nhân dân cấp huyện xét duyệt .** → `KHOAN` (span: `[12:60]`)
- `[e5]` **Ủy ban nhân dân cấp xã** → `CO_QUAN_THAM_QUYEN` (span: `[27:31]`) *(lồng trong `e4` (`KHOAN`))*
- `[e6]` **Ủy ban nhân dân cấp huyện** → `CO_QUAN_THAM_QUYEN` (span: `[54:58]`) *(lồng trong `e4` (`KHOAN`))*
- `[e7]` **phương án sử dụng đất** → `GIAY_TO_HO_SO` (span: `[15:18]`) *(lồng trong `e4` (`KHOAN`))*

**Quan hệ:**
- (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Tài nguyên và Môi trường `[CO_QUAN_BAN_HANH]`)
- (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 5 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`)
- (`e4` 3 . Dự thảo phương án sử dụng đất vùng bán ngập phải được niêm yết công khai tại trụ sở Ủy ban nhân dân cấp xã nơi có đất vùng bán ngập trong thời hạn ba mươi ( 30 ) ngày để lấy ý kiến đóng góp của nhân dân , trước khi trình Ủy ban nhân dân cấp huyện xét duyệt . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 5 `[DIEU]`)


---

### Mẫu #03_2012_TT-BTNMT_105778#body_standalone_29 (Loại: `body_standalone`)
> **[Điều 5]`<DIEU>`** . **[3 . Dự thảo **[phương án sử dụng đất]`<GIAY_TO_HO_SO>`** vùng bán ngập phải được niêm yết công khai tại trụ sở **[Ủy ban nhân dân cấp xã]`<CO_QUAN_THAM_QUYEN>`** nơi có đất vùng bán ngập trong thời hạn ba mươi ( 30 ) ngày để lấy ý kiến đóng góp của nhân dân , trước khi trình **[Ủy ban nhân dân cấp huyện]`<CO_QUAN_THAM_QUYEN>`** xét duyệt .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 5** → `DIEU` (span: `[0:2]`)
- `[e1]` **3 . Dự thảo phương án sử dụng đất vùng bán ngập phải được niêm yết công khai tại trụ sở Ủy ban nhân dân cấp xã nơi có đất vùng bán ngập trong thời hạn ba mươi ( 30 ) ngày để lấy ý kiến đóng góp của nhân dân , trước khi trình Ủy ban nhân dân cấp huyện xét duyệt .** → `KHOAN` (span: `[3:51]`)
- `[e2]` **Ủy ban nhân dân cấp xã** → `CO_QUAN_THAM_QUYEN` (span: `[18:22]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **Ủy ban nhân dân cấp huyện** → `CO_QUAN_THAM_QUYEN` (span: `[45:49]`) *(lồng trong `e1` (`KHOAN`))*
- `[e4]` **phương án sử dụng đất** → `GIAY_TO_HO_SO` (span: `[6:9]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 3 . Dự thảo phương án sử dụng đất vùng bán ngập phải được niêm yết công khai tại trụ sở Ủy ban nhân dân cấp xã nơi có đất vùng bán ngập trong thời hạn ba mươi ( 30 ) ngày để lấy ý kiến đóng góp của nhân dân , trước khi trình Ủy ban nhân dân cấp huyện xét duyệt . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 5 `[DIEU]`)


---

### Mẫu #03_2012_TT-BTNMT_105778#body_context_30 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[03/2012/TT-BTNMT]`<SO_HIEU>`** ban hành **[ngày 12 tháng 04 năm 2012]`<NGAY_BAN_HANH>`** bởi **[Bộ Tài nguyên và Môi trường]`<CO_QUAN_BAN_HANH>`** . **[Điều 5]`<DIEU>`** . **[4 . **[Phương án sử dụng đất]`<GIAY_TO_HO_SO>`** vùng bán ngập sau khi được **[Ủy ban nhân dân cấp huyện]`<CO_QUAN_THAM_QUYEN>`** xét duyệt phải được công bố công khai tại trụ sở **[Ủy ban nhân dân cấp xã]`<CO_QUAN_THAM_QUYEN>`** nơi có đất vùng bán ngập .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **03/2012/TT-BTNMT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Tài nguyên và Môi trường** → `CO_QUAN_BAN_HANH` (span: `[11:15]`)
- `[e3]` **ngày 12 tháng 04 năm 2012** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 5** → `DIEU` (span: `[16:18]`)
- `[e5]` **4 . Phương án sử dụng đất vùng bán ngập sau khi được Ủy ban nhân dân cấp huyện xét duyệt phải được công bố công khai tại trụ sở Ủy ban nhân dân cấp xã nơi có đất vùng bán ngập .** → `KHOAN` (span: `[19:52]`)
- `[e6]` **Ủy ban nhân dân cấp huyện** → `CO_QUAN_THAM_QUYEN` (span: `[30:34]`) *(lồng trong `e5` (`KHOAN`))*
- `[e7]` **Ủy ban nhân dân cấp xã** → `CO_QUAN_THAM_QUYEN` (span: `[41:45]`) *(lồng trong `e5` (`KHOAN`))*
- `[e8]` **Phương án sử dụng đất** → `GIAY_TO_HO_SO` (span: `[21:24]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Tài nguyên và Môi trường `[CO_QUAN_BAN_HANH]`)
- (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 12 tháng 04 năm 2012 `[NGAY_BAN_HANH]`)
- (`e4` Điều 5 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`)
- (`e5` 4 . Phương án sử dụng đất vùng bán ngập sau khi được Ủy ban nhân dân cấp huyện xét duyệt phải được công bố công khai tại trụ sở Ủy ban nhân dân cấp xã nơi có đất vùng bán ngập . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 5 `[DIEU]`)


---

### Mẫu #03_2012_TT-BTNMT_105778#body_standalone_31 (Loại: `body_standalone`)
> **[Điều 5]`<DIEU>`** . **[4 . **[Phương án sử dụng đất]`<GIAY_TO_HO_SO>`** vùng bán ngập sau khi được **[Ủy ban nhân dân cấp huyện]`<CO_QUAN_THAM_QUYEN>`** xét duyệt phải được công bố công khai tại trụ sở **[Ủy ban nhân dân cấp xã]`<CO_QUAN_THAM_QUYEN>`** nơi có đất vùng bán ngập .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 5** → `DIEU` (span: `[0:2]`)
- `[e1]` **4 . Phương án sử dụng đất vùng bán ngập sau khi được Ủy ban nhân dân cấp huyện xét duyệt phải được công bố công khai tại trụ sở Ủy ban nhân dân cấp xã nơi có đất vùng bán ngập .** → `KHOAN` (span: `[3:36]`)
- `[e2]` **Ủy ban nhân dân cấp huyện** → `CO_QUAN_THAM_QUYEN` (span: `[14:18]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **Ủy ban nhân dân cấp xã** → `CO_QUAN_THAM_QUYEN` (span: `[25:29]`) *(lồng trong `e1` (`KHOAN`))*
- `[e4]` **Phương án sử dụng đất** → `GIAY_TO_HO_SO` (span: `[5:8]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 4 . Phương án sử dụng đất vùng bán ngập sau khi được Ủy ban nhân dân cấp huyện xét duyệt phải được công bố công khai tại trụ sở Ủy ban nhân dân cấp xã nơi có đất vùng bán ngập . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 5 `[DIEU]`)


---

### Mẫu #03_2012_TT-BTNMT_105778#body_context_32 (Loại: `body_context`)
> **[Bộ Tài nguyên và Môi trường]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[03/2012/TT-BTNMT]`<SO_HIEU>`** . **[Điều 6]`<DIEU>`** . **[1 . Việc giao khoán đất vùng bán ngập thuộc thẩm quyền của **[Ủy ban nhân dân cấp xã]`<CO_QUAN_THAM_QUYEN>`** nơi có đất vùng bán ngập ( sau đây gọi là bên giao khoán ) .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[5:6]`)
- `[e1]` **03/2012/TT-BTNMT** → `SO_HIEU` (span: `[7:8]`)
- `[e2]` **Bộ Tài nguyên và Môi trường** → `CO_QUAN_BAN_HANH` (span: `[0:4]`)
- `[e3]` **Điều 6** → `DIEU` (span: `[9:11]`)
- `[e4]` **1 . Việc giao khoán đất vùng bán ngập thuộc thẩm quyền của Ủy ban nhân dân cấp xã nơi có đất vùng bán ngập ( sau đây gọi là bên giao khoán ) .** → `KHOAN` (span: `[12:42]`)
- `[e5]` **Ủy ban nhân dân cấp xã** → `CO_QUAN_THAM_QUYEN` (span: `[23:27]`) *(lồng trong `e4` (`KHOAN`))*

**Quan hệ:**
- (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Tài nguyên và Môi trường `[CO_QUAN_BAN_HANH]`)
- (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 6 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`)
- (`e4` 1 . Việc giao khoán đất vùng bán ngập thuộc thẩm quyền của Ủy ban nhân dân cấp xã nơi có đất vùng bán ngập ( sau đây gọi là bên giao khoán ) . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 6 `[DIEU]`)


---

### Mẫu #03_2012_TT-BTNMT_105778#body_standalone_33 (Loại: `body_standalone`)
> **[Điều 6]`<DIEU>`** . **[1 . Việc giao khoán đất vùng bán ngập thuộc thẩm quyền của **[Ủy ban nhân dân cấp xã]`<CO_QUAN_THAM_QUYEN>`** nơi có đất vùng bán ngập ( sau đây gọi là bên giao khoán ) .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 6** → `DIEU` (span: `[0:2]`)
- `[e1]` **1 . Việc giao khoán đất vùng bán ngập thuộc thẩm quyền của Ủy ban nhân dân cấp xã nơi có đất vùng bán ngập ( sau đây gọi là bên giao khoán ) .** → `KHOAN` (span: `[3:33]`)
- `[e2]` **Ủy ban nhân dân cấp xã** → `CO_QUAN_THAM_QUYEN` (span: `[14:18]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 1 . Việc giao khoán đất vùng bán ngập thuộc thẩm quyền của Ủy ban nhân dân cấp xã nơi có đất vùng bán ngập ( sau đây gọi là bên giao khoán ) . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 6 `[DIEU]`)


---

### Mẫu #03_2012_TT-BTNMT_105778#body_context_34 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[03/2012/TT-BTNMT]`<SO_HIEU>`** ban hành **[ngày 12 tháng 04 năm 2012]`<NGAY_BAN_HANH>`** bởi **[Bộ Tài nguyên và Môi trường]`<CO_QUAN_BAN_HANH>`** . **[Điều 6]`<DIEU>`** . **[2 . Đối tượng nhận khoán đất vùng bán ngập là các tổ chức , **[hộ gia đình]`<TO_CHUC_DOANH_NGHIEP>`** và cá nhân ( sau đây gọi là bên nhận khoán ) . Diện tích đất vùng bán ngập được giao khoán cho **[hộ gia đình]`<TO_CHUC_DOANH_NGHIEP>`** , cá nhân trực tiếp sản xuất nông , lâm nghiệp đang cư trú hợp pháp trên địa bàn xã , phường , thị trấn có đất vùng bán ngập , trong đó ưu tiên **[hộ gia đình]`<TO_CHUC_DOANH_NGHIEP>`** , cá nhân bị thu hồi đất sản xuất nông , lâm nghiệp sử dụng vào mục đích thủy điện , thủy lợi ;]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **03/2012/TT-BTNMT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Tài nguyên và Môi trường** → `CO_QUAN_BAN_HANH` (span: `[11:15]`)
- `[e3]` **ngày 12 tháng 04 năm 2012** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 6** → `DIEU` (span: `[16:18]`)
- `[e5]` **2 . Đối tượng nhận khoán đất vùng bán ngập là các tổ chức , hộ gia đình và cá nhân ( sau đây gọi là bên nhận khoán ) . Diện tích đất vùng bán ngập được giao khoán cho hộ gia đình , cá nhân trực tiếp sản xuất nông , lâm nghiệp đang cư trú hợp pháp trên địa bàn xã , phường , thị trấn có đất vùng bán ngập , trong đó ưu tiên hộ gia đình , cá nhân bị thu hồi đất sản xuất nông , lâm nghiệp sử dụng vào mục đích thủy điện , thủy lợi ;** → `KHOAN` (span: `[19:100]`)
- `[e6]` **hộ gia đình** → `TO_CHUC_DOANH_NGHIEP` (span: `[32:34]`) *(lồng trong `e5` (`KHOAN`))*
- `[e7]` **hộ gia đình** → `TO_CHUC_DOANH_NGHIEP` (span: `[54:56]`) *(lồng trong `e5` (`KHOAN`))*
- `[e8]` **hộ gia đình** → `TO_CHUC_DOANH_NGHIEP` (span: `[82:84]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Tài nguyên và Môi trường `[CO_QUAN_BAN_HANH]`)
- (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 12 tháng 04 năm 2012 `[NGAY_BAN_HANH]`)
- (`e4` Điều 6 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`)
- (`e5` 2 . Đối tượng nhận khoán đất vùng bán ngập là các tổ chức , hộ gia đình và cá nhân ( sau đây gọi là bên nhận khoán ) . Diện tích đất vùng bán ngập được giao khoán cho hộ gia đình , cá nhân trực tiếp sản xuất nông , lâm nghiệp đang cư trú hợp pháp trên địa bàn xã , phường , thị trấn có đất vùng bán ngập , trong đó ưu tiên hộ gia đình , cá nhân bị thu hồi đất sản xuất nông , lâm nghiệp sử dụng vào mục đích thủy điện , thủy lợi ; `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 6 `[DIEU]`)


---

### Mẫu #03_2012_TT-BTNMT_105778#body_standalone_35 (Loại: `body_standalone`)
> **[Điều 6]`<DIEU>`** . **[2 . Đối tượng nhận khoán đất vùng bán ngập là các tổ chức , **[hộ gia đình]`<TO_CHUC_DOANH_NGHIEP>`** và cá nhân ( sau đây gọi là bên nhận khoán ) . Diện tích đất vùng bán ngập được giao khoán cho **[hộ gia đình]`<TO_CHUC_DOANH_NGHIEP>`** , cá nhân trực tiếp sản xuất nông , lâm nghiệp đang cư trú hợp pháp trên địa bàn xã , phường , thị trấn có đất vùng bán ngập , trong đó ưu tiên **[hộ gia đình]`<TO_CHUC_DOANH_NGHIEP>`** , cá nhân bị thu hồi đất sản xuất nông , lâm nghiệp sử dụng vào mục đích thủy điện , thủy lợi ;]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 6** → `DIEU` (span: `[0:2]`)
- `[e1]` **2 . Đối tượng nhận khoán đất vùng bán ngập là các tổ chức , hộ gia đình và cá nhân ( sau đây gọi là bên nhận khoán ) . Diện tích đất vùng bán ngập được giao khoán cho hộ gia đình , cá nhân trực tiếp sản xuất nông , lâm nghiệp đang cư trú hợp pháp trên địa bàn xã , phường , thị trấn có đất vùng bán ngập , trong đó ưu tiên hộ gia đình , cá nhân bị thu hồi đất sản xuất nông , lâm nghiệp sử dụng vào mục đích thủy điện , thủy lợi ;** → `KHOAN` (span: `[3:84]`)
- `[e2]` **hộ gia đình** → `TO_CHUC_DOANH_NGHIEP` (span: `[16:18]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **hộ gia đình** → `TO_CHUC_DOANH_NGHIEP` (span: `[38:40]`) *(lồng trong `e1` (`KHOAN`))*
- `[e4]` **hộ gia đình** → `TO_CHUC_DOANH_NGHIEP` (span: `[66:68]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 2 . Đối tượng nhận khoán đất vùng bán ngập là các tổ chức , hộ gia đình và cá nhân ( sau đây gọi là bên nhận khoán ) . Diện tích đất vùng bán ngập được giao khoán cho hộ gia đình , cá nhân trực tiếp sản xuất nông , lâm nghiệp đang cư trú hợp pháp trên địa bàn xã , phường , thị trấn có đất vùng bán ngập , trong đó ưu tiên hộ gia đình , cá nhân bị thu hồi đất sản xuất nông , lâm nghiệp sử dụng vào mục đích thủy điện , thủy lợi ; `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 6 `[DIEU]`)


---

### Mẫu #03_2012_TT-BTNMT_105778#body_context_36 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[03/2012/TT-BTNMT]`<SO_HIEU>`** của **[Bộ Tài nguyên và Môi trường]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Lao động - Thương binh và Xã hội]`<LINH_VUC>`** . **[Điều 6]`<DIEU>`** . **[3 . Đơn giá giao khoán đất vùng bán ngập do **[Ủy ban nhân dân cấp huyện]`<CO_QUAN_THAM_QUYEN>`** quy định trên cơ sở giá đất nông nghiệp của địa phương . Tiền giao khoán đất vùng bán ngập được quản lý , sử dụng như tiền thu được từ việc cho thuê đất thuộc quỹ đất công ích của xã , phường , thị trấn .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **03/2012/TT-BTNMT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Tài nguyên và Môi trường** → `CO_QUAN_BAN_HANH` (span: `[4:8]`)
- `[e3]` **Lao động - Thương binh và Xã hội** → `LINH_VUC` (span: `[10:15]`)
- `[e4]` **Điều 6** → `DIEU` (span: `[16:18]`)
- `[e5]` **3 . Đơn giá giao khoán đất vùng bán ngập do Ủy ban nhân dân cấp huyện quy định trên cơ sở giá đất nông nghiệp của địa phương . Tiền giao khoán đất vùng bán ngập được quản lý , sử dụng như tiền thu được từ việc cho thuê đất thuộc quỹ đất công ích của xã , phường , thị trấn .** → `KHOAN` (span: `[19:71]`)
- `[e6]` **Ủy ban nhân dân cấp huyện** → `CO_QUAN_THAM_QUYEN` (span: `[28:32]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Tài nguyên và Môi trường `[CO_QUAN_BAN_HANH]`)
- (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Lao động - Thương binh và Xã hội `[LINH_VUC]`)
- (`e4` Điều 6 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`)
- (`e5` 3 . Đơn giá giao khoán đất vùng bán ngập do Ủy ban nhân dân cấp huyện quy định trên cơ sở giá đất nông nghiệp của địa phương . Tiền giao khoán đất vùng bán ngập được quản lý , sử dụng như tiền thu được từ việc cho thuê đất thuộc quỹ đất công ích của xã , phường , thị trấn . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 6 `[DIEU]`)
- (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Lao động - Thương binh và Xã hội `[LINH_VUC]`)
- (`e5` 3 . Đơn giá giao khoán đất vùng bán ngập do Ủy ban nhân dân cấp huyện quy định trên cơ sở giá đất nông nghiệp của địa phương . Tiền giao khoán đất vùng bán ngập được quản lý , sử dụng như tiền thu được từ việc cho thuê đất thuộc quỹ đất công ích của xã , phường , thị trấn . `[KHOAN]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Lao động - Thương binh và Xã hội `[LINH_VUC]`)


---

### Mẫu #03_2012_TT-BTNMT_105778#body_context_37 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[03/2012/TT-BTNMT]`<SO_HIEU>`** của **[Bộ Tài nguyên và Môi trường]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Lao động - Thương binh và Xã hội]`<LINH_VUC>`** . **[Chương II]`<CHUONG>`** . **[Điều 7 . Hình thức giao khoán đất vùng bán ngập]`<DIEU>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **03/2012/TT-BTNMT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Tài nguyên và Môi trường** → `CO_QUAN_BAN_HANH` (span: `[4:8]`)
- `[e3]` **Lao động - Thương binh và Xã hội** → `LINH_VUC` (span: `[10:15]`)
- `[e4]` **Chương II** → `CHUONG` (span: `[16:18]`)
- `[e5]` **Điều 7 . Hình thức giao khoán đất vùng bán ngập** → `DIEU` (span: `[19:28]`)

**Quan hệ:**
- (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Tài nguyên và Môi trường `[CO_QUAN_BAN_HANH]`)
- (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Lao động - Thương binh và Xã hội `[LINH_VUC]`)
- (`e4` Chương II `[CHUONG]`) ==[ **THUOC_VE** ]==> (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`)
- (`e5` Điều 7 . Hình thức giao khoán đất vùng bán ngập `[DIEU]`) ==[ **THUOC_VE** ]==> (`e4` Chương II `[CHUONG]`)
- (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Lao động - Thương binh và Xã hội `[LINH_VUC]`)
- (`e5` Điều 7 . Hình thức giao khoán đất vùng bán ngập `[DIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Lao động - Thương binh và Xã hội `[LINH_VUC]`)


---

### Mẫu #03_2012_TT-BTNMT_105778#body_context_38 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[03/2012/TT-BTNMT]`<SO_HIEU>`** của **[Bộ Tài nguyên và Môi trường]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Lao động - Thương binh và Xã hội]`<LINH_VUC>`** . **[Điều 7]`<DIEU>`** . **[2 . Giao khoán ổn định theo chu kỳ cây trồng hoặc chu kỳ kinh doanh đối với đất trồng cây lâu năm hoặc rừng trồng với tổng thời gian **[tối đa là 50 năm]`<THOI_HAN>`** .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **03/2012/TT-BTNMT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Tài nguyên và Môi trường** → `CO_QUAN_BAN_HANH` (span: `[4:8]`)
- `[e3]` **Lao động - Thương binh và Xã hội** → `LINH_VUC` (span: `[10:15]`)
- `[e4]` **Điều 7** → `DIEU` (span: `[16:18]`)
- `[e5]` **2 . Giao khoán ổn định theo chu kỳ cây trồng hoặc chu kỳ kinh doanh đối với đất trồng cây lâu năm hoặc rừng trồng với tổng thời gian tối đa là 50 năm .** → `KHOAN` (span: `[19:44]`)
- `[e6]` **tối đa là 50 năm** → `THOI_HAN` (span: `[39:43]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Tài nguyên và Môi trường `[CO_QUAN_BAN_HANH]`)
- (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Lao động - Thương binh và Xã hội `[LINH_VUC]`)
- (`e4` Điều 7 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`)
- (`e5` 2 . Giao khoán ổn định theo chu kỳ cây trồng hoặc chu kỳ kinh doanh đối với đất trồng cây lâu năm hoặc rừng trồng với tổng thời gian tối đa là 50 năm . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 7 `[DIEU]`)
- (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Lao động - Thương binh và Xã hội `[LINH_VUC]`)
- (`e5` 2 . Giao khoán ổn định theo chu kỳ cây trồng hoặc chu kỳ kinh doanh đối với đất trồng cây lâu năm hoặc rừng trồng với tổng thời gian tối đa là 50 năm . `[KHOAN]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Lao động - Thương binh và Xã hội `[LINH_VUC]`)


---

### Mẫu #03_2012_TT-BTNMT_105778#body_context_39 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[03/2012/TT-BTNMT]`<SO_HIEU>`** của **[Bộ Tài nguyên và Môi trường]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Lao động - Thương binh và Xã hội]`<LINH_VUC>`** . **[Điều 7]`<DIEU>`** . **[3 . Giao khoán theo vụ hoặc theo năm đối với đất có mặt nước nuôi trồng thuỷ sản với tổng thời gian là 05 năm .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **03/2012/TT-BTNMT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Tài nguyên và Môi trường** → `CO_QUAN_BAN_HANH` (span: `[4:8]`)
- `[e3]` **Lao động - Thương binh và Xã hội** → `LINH_VUC` (span: `[10:15]`)
- `[e4]` **Điều 7** → `DIEU` (span: `[16:18]`)
- `[e5]` **3 . Giao khoán theo vụ hoặc theo năm đối với đất có mặt nước nuôi trồng thuỷ sản với tổng thời gian là 05 năm .** → `KHOAN` (span: `[19:39]`)

**Quan hệ:**
- (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Tài nguyên và Môi trường `[CO_QUAN_BAN_HANH]`)
- (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Lao động - Thương binh và Xã hội `[LINH_VUC]`)
- (`e4` Điều 7 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`)
- (`e5` 3 . Giao khoán theo vụ hoặc theo năm đối với đất có mặt nước nuôi trồng thuỷ sản với tổng thời gian là 05 năm . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 7 `[DIEU]`)
- (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Lao động - Thương binh và Xã hội `[LINH_VUC]`)
- (`e5` 3 . Giao khoán theo vụ hoặc theo năm đối với đất có mặt nước nuôi trồng thuỷ sản với tổng thời gian là 05 năm . `[KHOAN]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Lao động - Thương binh và Xã hội `[LINH_VUC]`)


---

### Mẫu #03_2012_TT-BTNMT_105778#body_context_40 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[03/2012/TT-BTNMT]`<SO_HIEU>`** ban hành **[ngày 12 tháng 04 năm 2012]`<NGAY_BAN_HANH>`** bởi **[Bộ Tài nguyên và Môi trường]`<CO_QUAN_BAN_HANH>`** . **[Điều 8]`<DIEU>`** . **[1 . Việc sử dụng đất vùng bán ngập theo **[phương án sử dụng đất]`<GIAY_TO_HO_SO>`** đã được **[cấp có thẩm quyền]`<CO_QUAN_THAM_QUYEN>`** xét duyệt bảo đảm không ảnh hưởng đến mục đích chính là thủy điện , thủy lợi ; tuân thủ các quy định về kỹ thuật của ngành , lĩnh vực liên quan và các quy định về bảo vệ cảnh quan , môi trường ; không làm ảnh hưởng đến các đặc trưng kỹ thuật của hồ chứa , không làm cản trở đến dòng chảy đến hồ .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **03/2012/TT-BTNMT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Tài nguyên và Môi trường** → `CO_QUAN_BAN_HANH` (span: `[11:15]`)
- `[e3]` **ngày 12 tháng 04 năm 2012** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 8** → `DIEU` (span: `[16:18]`)
- `[e5]` **1 . Việc sử dụng đất vùng bán ngập theo phương án sử dụng đất đã được cấp có thẩm quyền xét duyệt bảo đảm không ảnh hưởng đến mục đích chính là thủy điện , thủy lợi ; tuân thủ các quy định về kỹ thuật của ngành , lĩnh vực liên quan và các quy định về bảo vệ cảnh quan , môi trường ; không làm ảnh hưởng đến các đặc trưng kỹ thuật của hồ chứa , không làm cản trở đến dòng chảy đến hồ .** → `KHOAN` (span: `[19:86]`)
- `[e6]` **cấp có thẩm quyền** → `CO_QUAN_THAM_QUYEN` (span: `[33:36]`) *(lồng trong `e5` (`KHOAN`))*
- `[e7]` **phương án sử dụng đất** → `GIAY_TO_HO_SO` (span: `[28:31]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Tài nguyên và Môi trường `[CO_QUAN_BAN_HANH]`)
- (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 12 tháng 04 năm 2012 `[NGAY_BAN_HANH]`)
- (`e4` Điều 8 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`)
- (`e5` 1 . Việc sử dụng đất vùng bán ngập theo phương án sử dụng đất đã được cấp có thẩm quyền xét duyệt bảo đảm không ảnh hưởng đến mục đích chính là thủy điện , thủy lợi ; tuân thủ các quy định về kỹ thuật của ngành , lĩnh vực liên quan và các quy định về bảo vệ cảnh quan , môi trường ; không làm ảnh hưởng đến các đặc trưng kỹ thuật của hồ chứa , không làm cản trở đến dòng chảy đến hồ . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 8 `[DIEU]`)


---

### Mẫu #03_2012_TT-BTNMT_105778#body_standalone_41 (Loại: `body_standalone`)
> **[Điều 8]`<DIEU>`** . **[1 . Việc sử dụng đất vùng bán ngập theo **[phương án sử dụng đất]`<GIAY_TO_HO_SO>`** đã được **[cấp có thẩm quyền]`<CO_QUAN_THAM_QUYEN>`** xét duyệt bảo đảm không ảnh hưởng đến mục đích chính là thủy điện , thủy lợi ; tuân thủ các quy định về kỹ thuật của ngành , lĩnh vực liên quan và các quy định về bảo vệ cảnh quan , môi trường ; không làm ảnh hưởng đến các đặc trưng kỹ thuật của hồ chứa , không làm cản trở đến dòng chảy đến hồ .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 8** → `DIEU` (span: `[0:2]`)
- `[e1]` **1 . Việc sử dụng đất vùng bán ngập theo phương án sử dụng đất đã được cấp có thẩm quyền xét duyệt bảo đảm không ảnh hưởng đến mục đích chính là thủy điện , thủy lợi ; tuân thủ các quy định về kỹ thuật của ngành , lĩnh vực liên quan và các quy định về bảo vệ cảnh quan , môi trường ; không làm ảnh hưởng đến các đặc trưng kỹ thuật của hồ chứa , không làm cản trở đến dòng chảy đến hồ .** → `KHOAN` (span: `[3:70]`)
- `[e2]` **cấp có thẩm quyền** → `CO_QUAN_THAM_QUYEN` (span: `[17:20]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **phương án sử dụng đất** → `GIAY_TO_HO_SO` (span: `[12:15]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 1 . Việc sử dụng đất vùng bán ngập theo phương án sử dụng đất đã được cấp có thẩm quyền xét duyệt bảo đảm không ảnh hưởng đến mục đích chính là thủy điện , thủy lợi ; tuân thủ các quy định về kỹ thuật của ngành , lĩnh vực liên quan và các quy định về bảo vệ cảnh quan , môi trường ; không làm ảnh hưởng đến các đặc trưng kỹ thuật của hồ chứa , không làm cản trở đến dòng chảy đến hồ . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 8 `[DIEU]`)


---

### Mẫu #03_2012_TT-BTNMT_105778#body_context_42 (Loại: `body_context`)
> **[Bộ Tài nguyên và Môi trường]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[03/2012/TT-BTNMT]`<SO_HIEU>`** . **[Điều 8]`<DIEU>`** . **[2 . Việc sử dụng đất vùng bán ngập phải thực hiện theo đúng **[quy định tại]`<TU_KHOA_PHAP_LY>`** **[Điều 5]`<THAM_CHIEU_PHAP_LY>`** và **[các khoản 4 , 5 Điều 8 Nghị định số 112/2008/NĐ-CP]`<THAM_CHIEU_PHAP_LY>`** **[ngày 20 tháng 10 năm 2008]`<NGAY_THAM_CHIEU>`** của **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** về quản lý , bảo vệ , khai thác tổng hợp tài nguyên và môi trường các hồ chứa thủy điện , thủy lợi .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[5:6]`)
- `[e1]` **03/2012/TT-BTNMT** → `SO_HIEU` (span: `[7:8]`)
- `[e2]` **Bộ Tài nguyên và Môi trường** → `CO_QUAN_BAN_HANH` (span: `[0:4]`)
- `[e3]` **Điều 8** → `DIEU` (span: `[9:11]`)
- `[e4]` **2 . Việc sử dụng đất vùng bán ngập phải thực hiện theo đúng quy định tại Điều 5 và các khoản 4 , 5 Điều 8 Nghị định số 112/2008/NĐ-CP ngày 20 tháng 10 năm 2008 của Chính phủ về quản lý , bảo vệ , khai thác tổng hợp tài nguyên và môi trường các hồ chứa thủy điện , thủy lợi .** → `KHOAN` (span: `[12:64]`)
- `[e5]` **Điều 5** → `THAM_CHIEU_PHAP_LY` (span: `[26:28]`) *(lồng trong `e4` (`KHOAN`))*
- `[e6]` **các khoản 4 , 5 Điều 8 Nghị định số 112/2008/NĐ-CP** → `THAM_CHIEU_PHAP_LY` (span: `[29:39]`) *(lồng trong `e4` (`KHOAN`))*
- `[e7]` **quy định tại** → `TU_KHOA_PHAP_LY` (span: `[24:26]`) *(lồng trong `e4` (`KHOAN`))*
- `[e8]` **ngày 20 tháng 10 năm 2008** → `NGAY_THAM_CHIEU` (span: `[39:45]`) *(lồng trong `e4` (`KHOAN`))*
- `[e9]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[46:47]`) *(lồng trong `e4` (`KHOAN`))*

**Quan hệ:**
- (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Tài nguyên và Môi trường `[CO_QUAN_BAN_HANH]`)
- (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 8 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`)
- (`e4` 2 . Việc sử dụng đất vùng bán ngập phải thực hiện theo đúng quy định tại Điều 5 và các khoản 4 , 5 Điều 8 Nghị định số 112/2008/NĐ-CP ngày 20 tháng 10 năm 2008 của Chính phủ về quản lý , bảo vệ , khai thác tổng hợp tài nguyên và môi trường các hồ chứa thủy điện , thủy lợi . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 8 `[DIEU]`)
- (`e7` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e5` Điều 5 `[THAM_CHIEU_PHAP_LY]`)
- (`e4` 2 . Việc sử dụng đất vùng bán ngập phải thực hiện theo đúng quy định tại Điều 5 và các khoản 4 , 5 Điều 8 Nghị định số 112/2008/NĐ-CP ngày 20 tháng 10 năm 2008 của Chính phủ về quản lý , bảo vệ , khai thác tổng hợp tài nguyên và môi trường các hồ chứa thủy điện , thủy lợi . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e5` Điều 5 `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e7` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e6` các khoản 4 , 5 Điều 8 Nghị định số 112/2008/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e4` 2 . Việc sử dụng đất vùng bán ngập phải thực hiện theo đúng quy định tại Điều 5 và các khoản 4 , 5 Điều 8 Nghị định số 112/2008/NĐ-CP ngày 20 tháng 10 năm 2008 của Chính phủ về quản lý , bảo vệ , khai thác tổng hợp tài nguyên và môi trường các hồ chứa thủy điện , thủy lợi . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e6` các khoản 4 , 5 Điều 8 Nghị định số 112/2008/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e6` các khoản 4 , 5 Điều 8 Nghị định số 112/2008/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e8` ngày 20 tháng 10 năm 2008 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #03_2012_TT-BTNMT_105778#body_standalone_43 (Loại: `body_standalone`)
> **[Điều 8]`<DIEU>`** . **[2 . Việc sử dụng đất vùng bán ngập phải thực hiện theo đúng **[quy định tại]`<TU_KHOA_PHAP_LY>`** **[Điều 5]`<THAM_CHIEU_PHAP_LY>`** và **[các khoản 4 , 5 Điều 8 Nghị định số 112/2008/NĐ-CP]`<THAM_CHIEU_PHAP_LY>`** **[ngày 20 tháng 10 năm 2008]`<NGAY_THAM_CHIEU>`** của **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** về quản lý , bảo vệ , khai thác tổng hợp tài nguyên và môi trường các hồ chứa thủy điện , thủy lợi .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 8** → `DIEU` (span: `[0:2]`)
- `[e1]` **2 . Việc sử dụng đất vùng bán ngập phải thực hiện theo đúng quy định tại Điều 5 và các khoản 4 , 5 Điều 8 Nghị định số 112/2008/NĐ-CP ngày 20 tháng 10 năm 2008 của Chính phủ về quản lý , bảo vệ , khai thác tổng hợp tài nguyên và môi trường các hồ chứa thủy điện , thủy lợi .** → `KHOAN` (span: `[3:55]`)
- `[e2]` **Điều 5** → `THAM_CHIEU_PHAP_LY` (span: `[17:19]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **các khoản 4 , 5 Điều 8 Nghị định số 112/2008/NĐ-CP** → `THAM_CHIEU_PHAP_LY` (span: `[20:30]`) *(lồng trong `e1` (`KHOAN`))*
- `[e4]` **quy định tại** → `TU_KHOA_PHAP_LY` (span: `[15:17]`) *(lồng trong `e1` (`KHOAN`))*
- `[e5]` **ngày 20 tháng 10 năm 2008** → `NGAY_THAM_CHIEU` (span: `[30:36]`) *(lồng trong `e1` (`KHOAN`))*
- `[e6]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[37:38]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 2 . Việc sử dụng đất vùng bán ngập phải thực hiện theo đúng quy định tại Điều 5 và các khoản 4 , 5 Điều 8 Nghị định số 112/2008/NĐ-CP ngày 20 tháng 10 năm 2008 của Chính phủ về quản lý , bảo vệ , khai thác tổng hợp tài nguyên và môi trường các hồ chứa thủy điện , thủy lợi . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 8 `[DIEU]`)
- (`e4` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e2` Điều 5 `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 2 . Việc sử dụng đất vùng bán ngập phải thực hiện theo đúng quy định tại Điều 5 và các khoản 4 , 5 Điều 8 Nghị định số 112/2008/NĐ-CP ngày 20 tháng 10 năm 2008 của Chính phủ về quản lý , bảo vệ , khai thác tổng hợp tài nguyên và môi trường các hồ chứa thủy điện , thủy lợi . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e2` Điều 5 `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e4` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` các khoản 4 , 5 Điều 8 Nghị định số 112/2008/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 2 . Việc sử dụng đất vùng bán ngập phải thực hiện theo đúng quy định tại Điều 5 và các khoản 4 , 5 Điều 8 Nghị định số 112/2008/NĐ-CP ngày 20 tháng 10 năm 2008 của Chính phủ về quản lý , bảo vệ , khai thác tổng hợp tài nguyên và môi trường các hồ chứa thủy điện , thủy lợi . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` các khoản 4 , 5 Điều 8 Nghị định số 112/2008/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e3` các khoản 4 , 5 Điều 8 Nghị định số 112/2008/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e5` ngày 20 tháng 10 năm 2008 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #03_2012_TT-BTNMT_105778#body_context_44 (Loại: `body_context`)
> **[Bộ Tài nguyên và Môi trường]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[03/2012/TT-BTNMT]`<SO_HIEU>`** . **[Điều 8]`<DIEU>`** . **[3 . **[Ủy ban nhân dân cấp xã]`<CO_QUAN_THAM_QUYEN>`** tổ chức , chỉ đạo thực hiện **[phương án sử dụng đất]`<GIAY_TO_HO_SO>`** vùng bán ngập của địa phương mình , kiểm tra phát hiện , ngăn chặn kịp thời các hành vi vi phạm . **[Ủy ban nhân dân cấp huyện]`<CO_QUAN_THAM_QUYEN>`** có trách nhiệm kiểm tra việc thực hiện **[phương án sử dụng đất]`<GIAY_TO_HO_SO>`** vùng bán ngập đã được xét duyệt .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[5:6]`)
- `[e1]` **03/2012/TT-BTNMT** → `SO_HIEU` (span: `[7:8]`)
- `[e2]` **Bộ Tài nguyên và Môi trường** → `CO_QUAN_BAN_HANH` (span: `[0:4]`)
- `[e3]` **Điều 8** → `DIEU` (span: `[9:11]`)
- `[e4]` **3 . Ủy ban nhân dân cấp xã tổ chức , chỉ đạo thực hiện phương án sử dụng đất vùng bán ngập của địa phương mình , kiểm tra phát hiện , ngăn chặn kịp thời các hành vi vi phạm . Ủy ban nhân dân cấp huyện có trách nhiệm kiểm tra việc thực hiện phương án sử dụng đất vùng bán ngập đã được xét duyệt .** → `KHOAN` (span: `[12:60]`)
- `[e5]` **Ủy ban nhân dân cấp xã** → `CO_QUAN_THAM_QUYEN` (span: `[14:18]`) *(lồng trong `e4` (`KHOAN`))*
- `[e6]` **Ủy ban nhân dân cấp huyện** → `CO_QUAN_THAM_QUYEN` (span: `[41:45]`) *(lồng trong `e4` (`KHOAN`))*
- `[e7]` **phương án sử dụng đất** → `GIAY_TO_HO_SO` (span: `[22:25]`) *(lồng trong `e4` (`KHOAN`))*
- `[e8]` **phương án sử dụng đất** → `GIAY_TO_HO_SO` (span: `[50:53]`) *(lồng trong `e4` (`KHOAN`))*

**Quan hệ:**
- (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Tài nguyên và Môi trường `[CO_QUAN_BAN_HANH]`)
- (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 8 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`)
- (`e4` 3 . Ủy ban nhân dân cấp xã tổ chức , chỉ đạo thực hiện phương án sử dụng đất vùng bán ngập của địa phương mình , kiểm tra phát hiện , ngăn chặn kịp thời các hành vi vi phạm . Ủy ban nhân dân cấp huyện có trách nhiệm kiểm tra việc thực hiện phương án sử dụng đất vùng bán ngập đã được xét duyệt . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 8 `[DIEU]`)


---

### Mẫu #03_2012_TT-BTNMT_105778#body_standalone_45 (Loại: `body_standalone`)
> **[Điều 8]`<DIEU>`** . **[3 . **[Ủy ban nhân dân cấp xã]`<CO_QUAN_THAM_QUYEN>`** tổ chức , chỉ đạo thực hiện **[phương án sử dụng đất]`<GIAY_TO_HO_SO>`** vùng bán ngập của địa phương mình , kiểm tra phát hiện , ngăn chặn kịp thời các hành vi vi phạm . **[Ủy ban nhân dân cấp huyện]`<CO_QUAN_THAM_QUYEN>`** có trách nhiệm kiểm tra việc thực hiện **[phương án sử dụng đất]`<GIAY_TO_HO_SO>`** vùng bán ngập đã được xét duyệt .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 8** → `DIEU` (span: `[0:2]`)
- `[e1]` **3 . Ủy ban nhân dân cấp xã tổ chức , chỉ đạo thực hiện phương án sử dụng đất vùng bán ngập của địa phương mình , kiểm tra phát hiện , ngăn chặn kịp thời các hành vi vi phạm . Ủy ban nhân dân cấp huyện có trách nhiệm kiểm tra việc thực hiện phương án sử dụng đất vùng bán ngập đã được xét duyệt .** → `KHOAN` (span: `[3:51]`)
- `[e2]` **Ủy ban nhân dân cấp xã** → `CO_QUAN_THAM_QUYEN` (span: `[5:9]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **Ủy ban nhân dân cấp huyện** → `CO_QUAN_THAM_QUYEN` (span: `[32:36]`) *(lồng trong `e1` (`KHOAN`))*
- `[e4]` **phương án sử dụng đất** → `GIAY_TO_HO_SO` (span: `[13:16]`) *(lồng trong `e1` (`KHOAN`))*
- `[e5]` **phương án sử dụng đất** → `GIAY_TO_HO_SO` (span: `[41:44]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 3 . Ủy ban nhân dân cấp xã tổ chức , chỉ đạo thực hiện phương án sử dụng đất vùng bán ngập của địa phương mình , kiểm tra phát hiện , ngăn chặn kịp thời các hành vi vi phạm . Ủy ban nhân dân cấp huyện có trách nhiệm kiểm tra việc thực hiện phương án sử dụng đất vùng bán ngập đã được xét duyệt . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 8 `[DIEU]`)


---

### Mẫu #03_2012_TT-BTNMT_105778#body_context_46 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[03/2012/TT-BTNMT]`<SO_HIEU>`** của **[Bộ Tài nguyên và Môi trường]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Lao động - Thương binh và Xã hội]`<LINH_VUC>`** . **[Chương III. TRÁCH NHIỆM , QUYỀN HẠN CỦA BÊN GIAO KHOÁN . VÀ QUYỀN LỢI , NGHĨA VỤ CỦA BÊN NHẬN KHOÁN]`<CHUONG>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **03/2012/TT-BTNMT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Tài nguyên và Môi trường** → `CO_QUAN_BAN_HANH` (span: `[4:8]`)
- `[e3]` **Lao động - Thương binh và Xã hội** → `LINH_VUC` (span: `[10:15]`)
- `[e4]` **Chương III. TRÁCH NHIỆM , QUYỀN HẠN CỦA BÊN GIAO KHOÁN . VÀ QUYỀN LỢI , NGHĨA VỤ CỦA BÊN NHẬN KHOÁN** → `CHUONG` (span: `[16:33]`)

**Quan hệ:**
- (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Tài nguyên và Môi trường `[CO_QUAN_BAN_HANH]`)
- (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Lao động - Thương binh và Xã hội `[LINH_VUC]`)
- (`e4` Chương III. TRÁCH NHIỆM , QUYỀN HẠN CỦA BÊN GIAO KHOÁN . VÀ QUYỀN LỢI , NGHĨA VỤ CỦA BÊN NHẬN KHOÁN `[CHUONG]`) ==[ **THUOC_VE** ]==> (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`)
- (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Lao động - Thương binh và Xã hội `[LINH_VUC]`)


---

### Mẫu #03_2012_TT-BTNMT_105778#body_context_47 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[03/2012/TT-BTNMT]`<SO_HIEU>`** của **[Bộ Tài nguyên và Môi trường]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Lao động - Thương binh và Xã hội]`<LINH_VUC>`** . **[Điều 9]`<DIEU>`** . **[Khoản 1]`<KHOAN>`** . **[a ) Chịu trách nhiệm trước **[cơ quan nhà nước có thẩm quyền]`<CO_QUAN_THAM_QUYEN>`** về quản lý và sử dụng đất vùng bán ngập theo **[phương án sử dụng đất]`<GIAY_TO_HO_SO>`** đã được **[cấp có thẩm quyền]`<CO_QUAN_THAM_QUYEN>`** xét duyệt ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **03/2012/TT-BTNMT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Tài nguyên và Môi trường** → `CO_QUAN_BAN_HANH` (span: `[4:8]`)
- `[e3]` **Lao động - Thương binh và Xã hội** → `LINH_VUC` (span: `[10:15]`)
- `[e4]` **Điều 9** → `DIEU` (span: `[16:18]`)
- `[e5]` **Khoản 1** → `KHOAN` (span: `[19:21]`)
- `[e6]` **a ) Chịu trách nhiệm trước cơ quan nhà nước có thẩm quyền về quản lý và sử dụng đất vùng bán ngập theo phương án sử dụng đất đã được cấp có thẩm quyền xét duyệt ;** → `DIEM` (span: `[22:50]`)
- `[e7]` **cơ quan nhà nước có thẩm quyền** → `CO_QUAN_THAM_QUYEN` (span: `[27:31]`) *(lồng trong `e6` (`DIEM`))*
- `[e8]` **cấp có thẩm quyền** → `CO_QUAN_THAM_QUYEN` (span: `[45:48]`) *(lồng trong `e6` (`DIEM`))*
- `[e9]` **phương án sử dụng đất** → `GIAY_TO_HO_SO` (span: `[40:43]`) *(lồng trong `e6` (`DIEM`))*

**Quan hệ:**
- (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Tài nguyên và Môi trường `[CO_QUAN_BAN_HANH]`)
- (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Lao động - Thương binh và Xã hội `[LINH_VUC]`)
- (`e4` Điều 9 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`)
- (`e5` Khoản 1 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 9 `[DIEU]`)
- (`e6` a ) Chịu trách nhiệm trước cơ quan nhà nước có thẩm quyền về quản lý và sử dụng đất vùng bán ngập theo phương án sử dụng đất đã được cấp có thẩm quyền xét duyệt ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e5` Khoản 1 `[KHOAN]`)
- (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Lao động - Thương binh và Xã hội `[LINH_VUC]`)
- (`e6` a ) Chịu trách nhiệm trước cơ quan nhà nước có thẩm quyền về quản lý và sử dụng đất vùng bán ngập theo phương án sử dụng đất đã được cấp có thẩm quyền xét duyệt ; `[DIEM]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Lao động - Thương binh và Xã hội `[LINH_VUC]`)


---

### Mẫu #03_2012_TT-BTNMT_105778#body_standalone_48 (Loại: `body_standalone`)
> **[Điều 9]`<DIEU>`** . **[Khoản 1]`<KHOAN>`** . **[a ) Chịu trách nhiệm trước **[cơ quan nhà nước có thẩm quyền]`<CO_QUAN_THAM_QUYEN>`** về quản lý và sử dụng đất vùng bán ngập theo **[phương án sử dụng đất]`<GIAY_TO_HO_SO>`** đã được **[cấp có thẩm quyền]`<CO_QUAN_THAM_QUYEN>`** xét duyệt ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Điều 9** → `DIEU` (span: `[0:2]`)
- `[e1]` **Khoản 1** → `KHOAN` (span: `[3:5]`)
- `[e2]` **a ) Chịu trách nhiệm trước cơ quan nhà nước có thẩm quyền về quản lý và sử dụng đất vùng bán ngập theo phương án sử dụng đất đã được cấp có thẩm quyền xét duyệt ;** → `DIEM` (span: `[6:34]`)
- `[e3]` **cơ quan nhà nước có thẩm quyền** → `CO_QUAN_THAM_QUYEN` (span: `[11:15]`) *(lồng trong `e2` (`DIEM`))*
- `[e4]` **cấp có thẩm quyền** → `CO_QUAN_THAM_QUYEN` (span: `[29:32]`) *(lồng trong `e2` (`DIEM`))*
- `[e5]` **phương án sử dụng đất** → `GIAY_TO_HO_SO` (span: `[24:27]`) *(lồng trong `e2` (`DIEM`))*

**Quan hệ:**
- (`e1` Khoản 1 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 9 `[DIEU]`)
- (`e2` a ) Chịu trách nhiệm trước cơ quan nhà nước có thẩm quyền về quản lý và sử dụng đất vùng bán ngập theo phương án sử dụng đất đã được cấp có thẩm quyền xét duyệt ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e1` Khoản 1 `[KHOAN]`)


---

### Mẫu #03_2012_TT-BTNMT_105778#body_context_49 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[03/2012/TT-BTNMT]`<SO_HIEU>`** ban hành **[ngày 12 tháng 04 năm 2012]`<NGAY_BAN_HANH>`** bởi **[Bộ Tài nguyên và Môi trường]`<CO_QUAN_BAN_HANH>`** . **[Điều 9]`<DIEU>`** . **[Khoản 1]`<KHOAN>`** . **[b ) Xác định đúng diện tích , vị trí ranh giới đất vùng bán ngập giao khoán trên bản đồ và thực địa ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **03/2012/TT-BTNMT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Tài nguyên và Môi trường** → `CO_QUAN_BAN_HANH` (span: `[11:15]`)
- `[e3]` **ngày 12 tháng 04 năm 2012** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 9** → `DIEU` (span: `[16:18]`)
- `[e5]` **Khoản 1** → `KHOAN` (span: `[19:21]`)
- `[e6]` **b ) Xác định đúng diện tích , vị trí ranh giới đất vùng bán ngập giao khoán trên bản đồ và thực địa ;** → `DIEM` (span: `[22:40]`)

**Quan hệ:**
- (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Tài nguyên và Môi trường `[CO_QUAN_BAN_HANH]`)
- (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 12 tháng 04 năm 2012 `[NGAY_BAN_HANH]`)
- (`e4` Điều 9 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`)
- (`e5` Khoản 1 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 9 `[DIEU]`)
- (`e6` b ) Xác định đúng diện tích , vị trí ranh giới đất vùng bán ngập giao khoán trên bản đồ và thực địa ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e5` Khoản 1 `[KHOAN]`)


---

### Mẫu #03_2012_TT-BTNMT_105778#body_context_50 (Loại: `body_context`)
> **[Bộ Tài nguyên và Môi trường]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[03/2012/TT-BTNMT]`<SO_HIEU>`** . **[Điều 9]`<DIEU>`** . **[Khoản 1]`<KHOAN>`** . **[d ) Xem xét miễn giảm các khoản phải nộp cho bên nhận khoán theo hợp đồng khi có rủi ro xảy ra thiệt hại ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[5:6]`)
- `[e1]` **03/2012/TT-BTNMT** → `SO_HIEU` (span: `[7:8]`)
- `[e2]` **Bộ Tài nguyên và Môi trường** → `CO_QUAN_BAN_HANH` (span: `[0:4]`)
- `[e3]` **Điều 9** → `DIEU` (span: `[9:11]`)
- `[e4]` **Khoản 1** → `KHOAN` (span: `[12:14]`)
- `[e5]` **d ) Xem xét miễn giảm các khoản phải nộp cho bên nhận khoán theo hợp đồng khi có rủi ro xảy ra thiệt hại ;** → `DIEM` (span: `[15:36]`)

**Quan hệ:**
- (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Tài nguyên và Môi trường `[CO_QUAN_BAN_HANH]`)
- (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 9 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`)
- (`e4` Khoản 1 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 9 `[DIEU]`)
- (`e5` d ) Xem xét miễn giảm các khoản phải nộp cho bên nhận khoán theo hợp đồng khi có rủi ro xảy ra thiệt hại ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e4` Khoản 1 `[KHOAN]`)


---

### Mẫu #03_2012_TT-BTNMT_105778#body_standalone_51 (Loại: `body_standalone`)
> **[Điều 9]`<DIEU>`** . **[Khoản 1]`<KHOAN>`** . **[d ) Xem xét miễn giảm các khoản phải nộp cho bên nhận khoán theo hợp đồng khi có rủi ro xảy ra thiệt hại ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Điều 9** → `DIEU` (span: `[0:2]`)
- `[e1]` **Khoản 1** → `KHOAN` (span: `[3:5]`)
- `[e2]` **d ) Xem xét miễn giảm các khoản phải nộp cho bên nhận khoán theo hợp đồng khi có rủi ro xảy ra thiệt hại ;** → `DIEM` (span: `[6:27]`)

**Quan hệ:**
- (`e1` Khoản 1 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 9 `[DIEU]`)
- (`e2` d ) Xem xét miễn giảm các khoản phải nộp cho bên nhận khoán theo hợp đồng khi có rủi ro xảy ra thiệt hại ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e1` Khoản 1 `[KHOAN]`)


---

### Mẫu #03_2012_TT-BTNMT_105778#body_context_52 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[03/2012/TT-BTNMT]`<SO_HIEU>`** của **[Bộ Tài nguyên và Môi trường]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Lao động - Thương binh và Xã hội]`<LINH_VUC>`** . **[Điều 9]`<DIEU>`** . **[2 . Quyền hạn :]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **03/2012/TT-BTNMT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Tài nguyên và Môi trường** → `CO_QUAN_BAN_HANH` (span: `[4:8]`)
- `[e3]` **Lao động - Thương binh và Xã hội** → `LINH_VUC` (span: `[10:15]`)
- `[e4]` **Điều 9** → `DIEU` (span: `[16:18]`)
- `[e5]` **2 . Quyền hạn :** → `KHOAN` (span: `[19:23]`)

**Quan hệ:**
- (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Tài nguyên và Môi trường `[CO_QUAN_BAN_HANH]`)
- (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Lao động - Thương binh và Xã hội `[LINH_VUC]`)
- (`e4` Điều 9 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`)
- (`e5` 2 . Quyền hạn : `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 9 `[DIEU]`)
- (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Lao động - Thương binh và Xã hội `[LINH_VUC]`)
- (`e5` 2 . Quyền hạn : `[KHOAN]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Lao động - Thương binh và Xã hội `[LINH_VUC]`)


---

### Mẫu #03_2012_TT-BTNMT_105778#body_context_53 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[03/2012/TT-BTNMT]`<SO_HIEU>`** của **[Bộ Tài nguyên và Môi trường]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Lao động - Thương binh và Xã hội]`<LINH_VUC>`** . **[Điều 9]`<DIEU>`** . **[Khoản 2]`<KHOAN>`** . **[a ) Huỷ bỏ **[hợp đồng giao khoán]`<GIAY_TO_HO_SO>`** khi bên nhận khoán vi phạm hợp đồng và yêu cầu bên nhận khoán bồi thường thiệt hại theo quy định của pháp luật ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **03/2012/TT-BTNMT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Tài nguyên và Môi trường** → `CO_QUAN_BAN_HANH` (span: `[4:8]`)
- `[e3]` **Lao động - Thương binh và Xã hội** → `LINH_VUC` (span: `[10:15]`)
- `[e4]` **Điều 9** → `DIEU` (span: `[16:18]`)
- `[e5]` **Khoản 2** → `KHOAN` (span: `[19:21]`)
- `[e6]` **a ) Huỷ bỏ hợp đồng giao khoán khi bên nhận khoán vi phạm hợp đồng và yêu cầu bên nhận khoán bồi thường thiệt hại theo quy định của pháp luật ;** → `DIEM` (span: `[22:45]`)
- `[e7]` **hợp đồng giao khoán** → `GIAY_TO_HO_SO` (span: `[25:27]`) *(lồng trong `e6` (`DIEM`))*

**Quan hệ:**
- (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Tài nguyên và Môi trường `[CO_QUAN_BAN_HANH]`)
- (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Lao động - Thương binh và Xã hội `[LINH_VUC]`)
- (`e4` Điều 9 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`)
- (`e5` Khoản 2 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 9 `[DIEU]`)
- (`e6` a ) Huỷ bỏ hợp đồng giao khoán khi bên nhận khoán vi phạm hợp đồng và yêu cầu bên nhận khoán bồi thường thiệt hại theo quy định của pháp luật ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e5` Khoản 2 `[KHOAN]`)
- (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Lao động - Thương binh và Xã hội `[LINH_VUC]`)
- (`e6` a ) Huỷ bỏ hợp đồng giao khoán khi bên nhận khoán vi phạm hợp đồng và yêu cầu bên nhận khoán bồi thường thiệt hại theo quy định của pháp luật ; `[DIEM]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Lao động - Thương binh và Xã hội `[LINH_VUC]`)


---

### Mẫu #03_2012_TT-BTNMT_105778#body_context_54 (Loại: `body_context`)
> **[Bộ Tài nguyên và Môi trường]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[03/2012/TT-BTNMT]`<SO_HIEU>`** . **[Điều 9]`<DIEU>`** . **[Khoản 2]`<KHOAN>`** . **[c ) Thu nộp và quản lý , sử dụng tiền giao khoán **[theo quy định tại]`<TU_KHOA_PHAP_LY>`** **[khoản 3 Điều 6 của Thông tư này]`<THAM_CHIEU_PHAP_LY>`** ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[5:6]`)
- `[e1]` **03/2012/TT-BTNMT** → `SO_HIEU` (span: `[7:8]`)
- `[e2]` **Bộ Tài nguyên và Môi trường** → `CO_QUAN_BAN_HANH` (span: `[0:4]`)
- `[e3]` **Điều 9** → `DIEU` (span: `[9:11]`)
- `[e4]` **Khoản 2** → `KHOAN` (span: `[12:14]`)
- `[e5]` **c ) Thu nộp và quản lý , sử dụng tiền giao khoán theo quy định tại khoản 3 Điều 6 của Thông tư này ;** → `DIEM` (span: `[15:36]`)
- `[e6]` **khoản 3 Điều 6 của Thông tư này** → `THAM_CHIEU_PHAP_LY` (span: `[28:35]`) *(lồng trong `e5` (`DIEM`))*
- `[e7]` **theo quy định tại** → `TU_KHOA_PHAP_LY` (span: `[25:28]`) *(lồng trong `e5` (`DIEM`))*

**Quan hệ:**
- (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Tài nguyên và Môi trường `[CO_QUAN_BAN_HANH]`)
- (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 9 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`)
- (`e4` Khoản 2 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 9 `[DIEU]`)
- (`e5` c ) Thu nộp và quản lý , sử dụng tiền giao khoán theo quy định tại khoản 3 Điều 6 của Thông tư này ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e4` Khoản 2 `[KHOAN]`)
- (`e7` theo quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e6` khoản 3 Điều 6 của Thông tư này `[THAM_CHIEU_PHAP_LY]`)
- (`e5` c ) Thu nộp và quản lý , sử dụng tiền giao khoán theo quy định tại khoản 3 Điều 6 của Thông tư này ; `[DIEM]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e6` khoản 3 Điều 6 của Thông tư này `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #03_2012_TT-BTNMT_105778#body_standalone_55 (Loại: `body_standalone`)
> **[Điều 9]`<DIEU>`** . **[Khoản 2]`<KHOAN>`** . **[c ) Thu nộp và quản lý , sử dụng tiền giao khoán **[theo quy định tại]`<TU_KHOA_PHAP_LY>`** **[khoản 3 Điều 6 của Thông tư này]`<THAM_CHIEU_PHAP_LY>`** ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Điều 9** → `DIEU` (span: `[0:2]`)
- `[e1]` **Khoản 2** → `KHOAN` (span: `[3:5]`)
- `[e2]` **c ) Thu nộp và quản lý , sử dụng tiền giao khoán theo quy định tại khoản 3 Điều 6 của Thông tư này ;** → `DIEM` (span: `[6:27]`)
- `[e3]` **khoản 3 Điều 6 của Thông tư này** → `THAM_CHIEU_PHAP_LY` (span: `[19:26]`) *(lồng trong `e2` (`DIEM`))*
- `[e4]` **theo quy định tại** → `TU_KHOA_PHAP_LY` (span: `[16:19]`) *(lồng trong `e2` (`DIEM`))*

**Quan hệ:**
- (`e1` Khoản 2 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 9 `[DIEU]`)
- (`e2` c ) Thu nộp và quản lý , sử dụng tiền giao khoán theo quy định tại khoản 3 Điều 6 của Thông tư này ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e1` Khoản 2 `[KHOAN]`)
- (`e4` theo quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` khoản 3 Điều 6 của Thông tư này `[THAM_CHIEU_PHAP_LY]`)
- (`e2` c ) Thu nộp và quản lý , sử dụng tiền giao khoán theo quy định tại khoản 3 Điều 6 của Thông tư này ; `[DIEM]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` khoản 3 Điều 6 của Thông tư này `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #03_2012_TT-BTNMT_105778#body_context_56 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[03/2012/TT-BTNMT]`<SO_HIEU>`** ban hành **[ngày 12 tháng 04 năm 2012]`<NGAY_BAN_HANH>`** bởi **[Bộ Tài nguyên và Môi trường]`<CO_QUAN_BAN_HANH>`** . **[Điều 9]`<DIEU>`** . **[Khoản 2]`<KHOAN>`** . **[d ) Kiểm tra , giám sát việc thực hiện **[hợp đồng giao khoán]`<GIAY_TO_HO_SO>`** , đảm bảo thực hiện theo đúng quy định của pháp luật hiện hành .]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **03/2012/TT-BTNMT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Tài nguyên và Môi trường** → `CO_QUAN_BAN_HANH` (span: `[11:15]`)
- `[e3]` **ngày 12 tháng 04 năm 2012** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 9** → `DIEU` (span: `[16:18]`)
- `[e5]` **Khoản 2** → `KHOAN` (span: `[19:21]`)
- `[e6]` **d ) Kiểm tra , giám sát việc thực hiện hợp đồng giao khoán , đảm bảo thực hiện theo đúng quy định của pháp luật hiện hành .** → `DIEM` (span: `[22:41]`)
- `[e7]` **hợp đồng giao khoán** → `GIAY_TO_HO_SO` (span: `[29:31]`) *(lồng trong `e6` (`DIEM`))*

**Quan hệ:**
- (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Tài nguyên và Môi trường `[CO_QUAN_BAN_HANH]`)
- (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 12 tháng 04 năm 2012 `[NGAY_BAN_HANH]`)
- (`e4` Điều 9 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`)
- (`e5` Khoản 2 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 9 `[DIEU]`)
- (`e6` d ) Kiểm tra , giám sát việc thực hiện hợp đồng giao khoán , đảm bảo thực hiện theo đúng quy định của pháp luật hiện hành . `[DIEM]`) ==[ **THUOC_VE** ]==> (`e5` Khoản 2 `[KHOAN]`)


---

### Mẫu #03_2012_TT-BTNMT_105778#body_standalone_57 (Loại: `body_standalone`)
> **[Điều 9]`<DIEU>`** . **[Khoản 2]`<KHOAN>`** . **[d ) Kiểm tra , giám sát việc thực hiện **[hợp đồng giao khoán]`<GIAY_TO_HO_SO>`** , đảm bảo thực hiện theo đúng quy định của pháp luật hiện hành .]`<DIEM>`**

**Thực thể:**
- `[e0]` **Điều 9** → `DIEU` (span: `[0:2]`)
- `[e1]` **Khoản 2** → `KHOAN` (span: `[3:5]`)
- `[e2]` **d ) Kiểm tra , giám sát việc thực hiện hợp đồng giao khoán , đảm bảo thực hiện theo đúng quy định của pháp luật hiện hành .** → `DIEM` (span: `[6:25]`)
- `[e3]` **hợp đồng giao khoán** → `GIAY_TO_HO_SO` (span: `[13:15]`) *(lồng trong `e2` (`DIEM`))*

**Quan hệ:**
- (`e1` Khoản 2 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 9 `[DIEU]`)
- (`e2` d ) Kiểm tra , giám sát việc thực hiện hợp đồng giao khoán , đảm bảo thực hiện theo đúng quy định của pháp luật hiện hành . `[DIEM]`) ==[ **THUOC_VE** ]==> (`e1` Khoản 2 `[KHOAN]`)


---

### Mẫu #03_2012_TT-BTNMT_105778#body_context_58 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[03/2012/TT-BTNMT]`<SO_HIEU>`** ban hành **[ngày 12 tháng 04 năm 2012]`<NGAY_BAN_HANH>`** bởi **[Bộ Tài nguyên và Môi trường]`<CO_QUAN_BAN_HANH>`** . **[Điều 10]`<DIEU>`** . **[1 . Nghĩa vụ :]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **03/2012/TT-BTNMT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Tài nguyên và Môi trường** → `CO_QUAN_BAN_HANH` (span: `[11:15]`)
- `[e3]` **ngày 12 tháng 04 năm 2012** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 10** → `DIEU` (span: `[16:18]`)
- `[e5]` **1 . Nghĩa vụ :** → `KHOAN` (span: `[19:23]`)

**Quan hệ:**
- (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Tài nguyên và Môi trường `[CO_QUAN_BAN_HANH]`)
- (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 12 tháng 04 năm 2012 `[NGAY_BAN_HANH]`)
- (`e4` Điều 10 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`)
- (`e5` 1 . Nghĩa vụ : `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 10 `[DIEU]`)


---

### Mẫu #03_2012_TT-BTNMT_105778#body_context_59 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[03/2012/TT-BTNMT]`<SO_HIEU>`** của **[Bộ Tài nguyên và Môi trường]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Lao động - Thương binh và Xã hội]`<LINH_VUC>`** . **[Điều 10]`<DIEU>`** . **[Khoản 1]`<KHOAN>`** . **[a ) Sử dụng đất vùng bán ngập theo đúng **[phương án sử dụng đất]`<GIAY_TO_HO_SO>`** đã được **[cấp có thẩm quyền]`<CO_QUAN_THAM_QUYEN>`** xét duyệt và quy định của pháp luật ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **03/2012/TT-BTNMT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Tài nguyên và Môi trường** → `CO_QUAN_BAN_HANH` (span: `[4:8]`)
- `[e3]` **Lao động - Thương binh và Xã hội** → `LINH_VUC` (span: `[10:15]`)
- `[e4]` **Điều 10** → `DIEU` (span: `[16:18]`)
- `[e5]` **Khoản 1** → `KHOAN` (span: `[19:21]`)
- `[e6]` **a ) Sử dụng đất vùng bán ngập theo đúng phương án sử dụng đất đã được cấp có thẩm quyền xét duyệt và quy định của pháp luật ;** → `DIEM` (span: `[22:45]`)
- `[e7]` **cấp có thẩm quyền** → `CO_QUAN_THAM_QUYEN` (span: `[36:39]`) *(lồng trong `e6` (`DIEM`))*
- `[e8]` **phương án sử dụng đất** → `GIAY_TO_HO_SO` (span: `[31:34]`) *(lồng trong `e6` (`DIEM`))*

**Quan hệ:**
- (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Tài nguyên và Môi trường `[CO_QUAN_BAN_HANH]`)
- (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Lao động - Thương binh và Xã hội `[LINH_VUC]`)
- (`e4` Điều 10 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`)
- (`e5` Khoản 1 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 10 `[DIEU]`)
- (`e6` a ) Sử dụng đất vùng bán ngập theo đúng phương án sử dụng đất đã được cấp có thẩm quyền xét duyệt và quy định của pháp luật ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e5` Khoản 1 `[KHOAN]`)
- (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Lao động - Thương binh và Xã hội `[LINH_VUC]`)
- (`e6` a ) Sử dụng đất vùng bán ngập theo đúng phương án sử dụng đất đã được cấp có thẩm quyền xét duyệt và quy định của pháp luật ; `[DIEM]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Lao động - Thương binh và Xã hội `[LINH_VUC]`)


---

### Mẫu #03_2012_TT-BTNMT_105778#body_standalone_60 (Loại: `body_standalone`)
> **[Điều 10]`<DIEU>`** . **[Khoản 1]`<KHOAN>`** . **[a ) Sử dụng đất vùng bán ngập theo đúng **[phương án sử dụng đất]`<GIAY_TO_HO_SO>`** đã được **[cấp có thẩm quyền]`<CO_QUAN_THAM_QUYEN>`** xét duyệt và quy định của pháp luật ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Điều 10** → `DIEU` (span: `[0:2]`)
- `[e1]` **Khoản 1** → `KHOAN` (span: `[3:5]`)
- `[e2]` **a ) Sử dụng đất vùng bán ngập theo đúng phương án sử dụng đất đã được cấp có thẩm quyền xét duyệt và quy định của pháp luật ;** → `DIEM` (span: `[6:29]`)
- `[e3]` **cấp có thẩm quyền** → `CO_QUAN_THAM_QUYEN` (span: `[20:23]`) *(lồng trong `e2` (`DIEM`))*
- `[e4]` **phương án sử dụng đất** → `GIAY_TO_HO_SO` (span: `[15:18]`) *(lồng trong `e2` (`DIEM`))*

**Quan hệ:**
- (`e1` Khoản 1 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 10 `[DIEU]`)
- (`e2` a ) Sử dụng đất vùng bán ngập theo đúng phương án sử dụng đất đã được cấp có thẩm quyền xét duyệt và quy định của pháp luật ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e1` Khoản 1 `[KHOAN]`)


---

### Mẫu #03_2012_TT-BTNMT_105778#body_context_61 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[03/2012/TT-BTNMT]`<SO_HIEU>`** của **[Bộ Tài nguyên và Môi trường]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Lao động - Thương binh và Xã hội]`<LINH_VUC>`** . **[Chương I. QUY ĐỊNH CHUNG]`<CHUONG>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **03/2012/TT-BTNMT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Tài nguyên và Môi trường** → `CO_QUAN_BAN_HANH` (span: `[4:8]`)
- `[e3]` **Lao động - Thương binh và Xã hội** → `LINH_VUC` (span: `[10:15]`)
- `[e4]` **Chương I. QUY ĐỊNH CHUNG** → `CHUONG` (span: `[16:20]`)

**Quan hệ:**
- (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Tài nguyên và Môi trường `[CO_QUAN_BAN_HANH]`)
- (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Lao động - Thương binh và Xã hội `[LINH_VUC]`)
- (`e4` Chương I. QUY ĐỊNH CHUNG `[CHUONG]`) ==[ **THUOC_VE** ]==> (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`)
- (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Lao động - Thương binh và Xã hội `[LINH_VUC]`)


---

### Mẫu #03_2012_TT-BTNMT_105778#body_context_62 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[03/2012/TT-BTNMT]`<SO_HIEU>`** của **[Bộ Tài nguyên và Môi trường]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Lao động - Thương binh và Xã hội]`<LINH_VUC>`** . **[Điều 3 . Giải thích từ ngữ]`<DIEU>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **03/2012/TT-BTNMT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Tài nguyên và Môi trường** → `CO_QUAN_BAN_HANH` (span: `[4:8]`)
- `[e3]` **Lao động - Thương binh và Xã hội** → `LINH_VUC` (span: `[10:15]`)
- `[e4]` **Điều 3 . Giải thích từ ngữ** → `DIEU` (span: `[16:21]`)

**Quan hệ:**
- (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Tài nguyên và Môi trường `[CO_QUAN_BAN_HANH]`)
- (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Lao động - Thương binh và Xã hội `[LINH_VUC]`)
- (`e4` Điều 3 . Giải thích từ ngữ `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`)
- (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Lao động - Thương binh và Xã hội `[LINH_VUC]`)
- (`e4` Điều 3 . Giải thích từ ngữ `[DIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Lao động - Thương binh và Xã hội `[LINH_VUC]`)


---

### Mẫu #03_2012_TT-BTNMT_105778#body_context_63 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[03/2012/TT-BTNMT]`<SO_HIEU>`** ban hành **[ngày 12 tháng 04 năm 2012]`<NGAY_BAN_HANH>`** bởi **[Bộ Tài nguyên và Môi trường]`<CO_QUAN_BAN_HANH>`** . **[Điều 9]`<DIEU>`** . **[1 . Trách nhiệm :]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **03/2012/TT-BTNMT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Tài nguyên và Môi trường** → `CO_QUAN_BAN_HANH` (span: `[11:15]`)
- `[e3]` **ngày 12 tháng 04 năm 2012** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 9** → `DIEU` (span: `[16:18]`)
- `[e5]` **1 . Trách nhiệm :** → `KHOAN` (span: `[19:23]`)

**Quan hệ:**
- (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Tài nguyên và Môi trường `[CO_QUAN_BAN_HANH]`)
- (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 12 tháng 04 năm 2012 `[NGAY_BAN_HANH]`)
- (`e4` Điều 9 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`)
- (`e5` 1 . Trách nhiệm : `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 9 `[DIEU]`)


---

### Mẫu #03_2012_TT-BTNMT_105778#body_context_64 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[03/2012/TT-BTNMT]`<SO_HIEU>`** ban hành **[ngày 12 tháng 04 năm 2012]`<NGAY_BAN_HANH>`** bởi **[Bộ Tài nguyên và Môi trường]`<CO_QUAN_BAN_HANH>`** . **[Điều 10]`<DIEU>`** . **[1 . Nghĩa vụ :]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **03/2012/TT-BTNMT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Tài nguyên và Môi trường** → `CO_QUAN_BAN_HANH` (span: `[11:15]`)
- `[e3]` **ngày 12 tháng 04 năm 2012** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 10** → `DIEU` (span: `[16:18]`)
- `[e5]` **1 . Nghĩa vụ :** → `KHOAN` (span: `[19:23]`)

**Quan hệ:**
- (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Tài nguyên và Môi trường `[CO_QUAN_BAN_HANH]`)
- (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 12 tháng 04 năm 2012 `[NGAY_BAN_HANH]`)
- (`e4` Điều 10 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`)
- (`e5` 1 . Nghĩa vụ : `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 10 `[DIEU]`)


---

### Mẫu #03_2012_TT-BTNMT_105778#body_context_65 (Loại: `body_context`)
> **[Bộ Tài nguyên và Môi trường]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[03/2012/TT-BTNMT]`<SO_HIEU>`** . **[Điều 10]`<DIEU>`** . **[Khoản 1]`<KHOAN>`** . **[d ) Trả lại đất vùng bán ngập nhận khoán khi **[cơ quan nhà nước có thẩm quyền]`<CO_QUAN_THAM_QUYEN>`** thu hồi theo quy định của pháp luật ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[5:6]`)
- `[e1]` **03/2012/TT-BTNMT** → `SO_HIEU` (span: `[7:8]`)
- `[e2]` **Bộ Tài nguyên và Môi trường** → `CO_QUAN_BAN_HANH` (span: `[0:4]`)
- `[e3]` **Điều 10** → `DIEU` (span: `[9:11]`)
- `[e4]` **Khoản 1** → `KHOAN` (span: `[12:14]`)
- `[e5]` **d ) Trả lại đất vùng bán ngập nhận khoán khi cơ quan nhà nước có thẩm quyền thu hồi theo quy định của pháp luật ;** → `DIEM` (span: `[15:36]`)
- `[e6]` **cơ quan nhà nước có thẩm quyền** → `CO_QUAN_THAM_QUYEN` (span: `[26:30]`) *(lồng trong `e5` (`DIEM`))*

**Quan hệ:**
- (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Tài nguyên và Môi trường `[CO_QUAN_BAN_HANH]`)
- (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 10 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`)
- (`e4` Khoản 1 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 10 `[DIEU]`)
- (`e5` d ) Trả lại đất vùng bán ngập nhận khoán khi cơ quan nhà nước có thẩm quyền thu hồi theo quy định của pháp luật ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e4` Khoản 1 `[KHOAN]`)


---

### Mẫu #03_2012_TT-BTNMT_105778#body_context_66 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[03/2012/TT-BTNMT]`<SO_HIEU>`** ban hành **[ngày 12 tháng 04 năm 2012]`<NGAY_BAN_HANH>`** bởi **[Bộ Tài nguyên và Môi trường]`<CO_QUAN_BAN_HANH>`** . **[Điều 10]`<DIEU>`** . **[Khoản 1]`<KHOAN>`** . **[e ) Chịu sự kiểm tra , giám sát của cơ quan nhà nước trong việc sử dụng đất vùng bán ngập . Bồi thường thiệt hại cho bên giao khoán nếu vi phạm hợp đồng ; bị xử phạt hành chính hoặc **[truy cứu trách nhiệm hình sự]`<HINH_PHAT_CHE_TAI>`** nếu vi phạm pháp luật trong việc sử dụng đất vùng bán ngập .]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **03/2012/TT-BTNMT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Tài nguyên và Môi trường** → `CO_QUAN_BAN_HANH` (span: `[11:15]`)
- `[e3]` **ngày 12 tháng 04 năm 2012** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 10** → `DIEU` (span: `[16:18]`)
- `[e5]` **Khoản 1** → `KHOAN` (span: `[19:21]`)
- `[e6]` **e ) Chịu sự kiểm tra , giám sát của cơ quan nhà nước trong việc sử dụng đất vùng bán ngập . Bồi thường thiệt hại cho bên giao khoán nếu vi phạm hợp đồng ; bị xử phạt hành chính hoặc truy cứu trách nhiệm hình sự nếu vi phạm pháp luật trong việc sử dụng đất vùng bán ngập .** → `DIEM` (span: `[22:66]`)
- `[e7]` **truy cứu trách nhiệm hình sự** → `HINH_PHAT_CHE_TAI` (span: `[53:56]`) *(lồng trong `e6` (`DIEM`))*

**Quan hệ:**
- (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Tài nguyên và Môi trường `[CO_QUAN_BAN_HANH]`)
- (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 12 tháng 04 năm 2012 `[NGAY_BAN_HANH]`)
- (`e4` Điều 10 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`)
- (`e5` Khoản 1 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 10 `[DIEU]`)
- (`e6` e ) Chịu sự kiểm tra , giám sát của cơ quan nhà nước trong việc sử dụng đất vùng bán ngập . Bồi thường thiệt hại cho bên giao khoán nếu vi phạm hợp đồng ; bị xử phạt hành chính hoặc truy cứu trách nhiệm hình sự nếu vi phạm pháp luật trong việc sử dụng đất vùng bán ngập . `[DIEM]`) ==[ **THUOC_VE** ]==> (`e5` Khoản 1 `[KHOAN]`)


---

### Mẫu #03_2012_TT-BTNMT_105778#body_context_67 (Loại: `body_context`)
> **[Bộ Tài nguyên và Môi trường]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[03/2012/TT-BTNMT]`<SO_HIEU>`** . **[Điều 10]`<DIEU>`** . **[2 . Quyền lợi :]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[5:6]`)
- `[e1]` **03/2012/TT-BTNMT** → `SO_HIEU` (span: `[7:8]`)
- `[e2]` **Bộ Tài nguyên và Môi trường** → `CO_QUAN_BAN_HANH` (span: `[0:4]`)
- `[e3]` **Điều 10** → `DIEU` (span: `[9:11]`)
- `[e4]` **2 . Quyền lợi :** → `KHOAN` (span: `[12:16]`)

**Quan hệ:**
- (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Tài nguyên và Môi trường `[CO_QUAN_BAN_HANH]`)
- (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 10 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`)
- (`e4` 2 . Quyền lợi : `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 10 `[DIEU]`)


---

### Mẫu #03_2012_TT-BTNMT_105778#body_context_68 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[03/2012/TT-BTNMT]`<SO_HIEU>`** của **[Bộ Tài nguyên và Môi trường]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Lao động - Thương binh và Xã hội]`<LINH_VUC>`** . **[Điều 10]`<DIEU>`** . **[Khoản 2]`<KHOAN>`** . **[a ) Chủ động sản xuất trên diện tích đất nhận khoán , được hưởng thành quả đầu tư trên đất nhận khoán theo **[hợp đồng giao khoán]`<GIAY_TO_HO_SO>`** đất vùng bán ngập ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **03/2012/TT-BTNMT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Tài nguyên và Môi trường** → `CO_QUAN_BAN_HANH` (span: `[4:8]`)
- `[e3]` **Lao động - Thương binh và Xã hội** → `LINH_VUC` (span: `[10:15]`)
- `[e4]` **Điều 10** → `DIEU` (span: `[16:18]`)
- `[e5]` **Khoản 2** → `KHOAN` (span: `[19:21]`)
- `[e6]` **a ) Chủ động sản xuất trên diện tích đất nhận khoán , được hưởng thành quả đầu tư trên đất nhận khoán theo hợp đồng giao khoán đất vùng bán ngập ;** → `DIEM` (span: `[22:47]`)
- `[e7]` **hợp đồng giao khoán** → `GIAY_TO_HO_SO` (span: `[40:42]`) *(lồng trong `e6` (`DIEM`))*

**Quan hệ:**
- (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Tài nguyên và Môi trường `[CO_QUAN_BAN_HANH]`)
- (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Lao động - Thương binh và Xã hội `[LINH_VUC]`)
- (`e4` Điều 10 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`)
- (`e5` Khoản 2 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 10 `[DIEU]`)
- (`e6` a ) Chủ động sản xuất trên diện tích đất nhận khoán , được hưởng thành quả đầu tư trên đất nhận khoán theo hợp đồng giao khoán đất vùng bán ngập ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e5` Khoản 2 `[KHOAN]`)
- (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Lao động - Thương binh và Xã hội `[LINH_VUC]`)
- (`e6` a ) Chủ động sản xuất trên diện tích đất nhận khoán , được hưởng thành quả đầu tư trên đất nhận khoán theo hợp đồng giao khoán đất vùng bán ngập ; `[DIEM]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Lao động - Thương binh và Xã hội `[LINH_VUC]`)


---

### Mẫu #03_2012_TT-BTNMT_105778#body_context_69 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[03/2012/TT-BTNMT]`<SO_HIEU>`** ban hành **[ngày 12 tháng 04 năm 2012]`<NGAY_BAN_HANH>`** bởi **[Bộ Tài nguyên và Môi trường]`<CO_QUAN_BAN_HANH>`** . **[Điều 10]`<DIEU>`** . **[Khoản 2]`<KHOAN>`** . **[c ) Được bồi thường , hỗ trợ về **[tài sản]`<TAI_SAN_VAT_CHAT>`** gắn liền với đất theo quy định của pháp luật khi **[cơ quan nhà nước có thẩm quyền]`<CO_QUAN_THAM_QUYEN>`** thu hồi đất đã nhận khoán để sử dụng vào mục đích khác ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **03/2012/TT-BTNMT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Tài nguyên và Môi trường** → `CO_QUAN_BAN_HANH` (span: `[11:15]`)
- `[e3]` **ngày 12 tháng 04 năm 2012** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 10** → `DIEU` (span: `[16:18]`)
- `[e5]` **Khoản 2** → `KHOAN` (span: `[19:21]`)
- `[e6]` **c ) Được bồi thường , hỗ trợ về tài sản gắn liền với đất theo quy định của pháp luật khi cơ quan nhà nước có thẩm quyền thu hồi đất đã nhận khoán để sử dụng vào mục đích khác ;** → `DIEM` (span: `[22:54]`)
- `[e7]` **cơ quan nhà nước có thẩm quyền** → `CO_QUAN_THAM_QUYEN` (span: `[39:43]`) *(lồng trong `e6` (`DIEM`))*
- `[e8]` **tài sản** → `TAI_SAN_VAT_CHAT` (span: `[29:30]`) *(lồng trong `e6` (`DIEM`))*

**Quan hệ:**
- (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Tài nguyên và Môi trường `[CO_QUAN_BAN_HANH]`)
- (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 12 tháng 04 năm 2012 `[NGAY_BAN_HANH]`)
- (`e4` Điều 10 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`)
- (`e5` Khoản 2 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 10 `[DIEU]`)
- (`e6` c ) Được bồi thường , hỗ trợ về tài sản gắn liền với đất theo quy định của pháp luật khi cơ quan nhà nước có thẩm quyền thu hồi đất đã nhận khoán để sử dụng vào mục đích khác ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e5` Khoản 2 `[KHOAN]`)


---

### Mẫu #03_2012_TT-BTNMT_105778#body_standalone_70 (Loại: `body_standalone`)
> **[Điều 10]`<DIEU>`** . **[Khoản 2]`<KHOAN>`** . **[c ) Được bồi thường , hỗ trợ về **[tài sản]`<TAI_SAN_VAT_CHAT>`** gắn liền với đất theo quy định của pháp luật khi **[cơ quan nhà nước có thẩm quyền]`<CO_QUAN_THAM_QUYEN>`** thu hồi đất đã nhận khoán để sử dụng vào mục đích khác ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Điều 10** → `DIEU` (span: `[0:2]`)
- `[e1]` **Khoản 2** → `KHOAN` (span: `[3:5]`)
- `[e2]` **c ) Được bồi thường , hỗ trợ về tài sản gắn liền với đất theo quy định của pháp luật khi cơ quan nhà nước có thẩm quyền thu hồi đất đã nhận khoán để sử dụng vào mục đích khác ;** → `DIEM` (span: `[6:38]`)
- `[e3]` **cơ quan nhà nước có thẩm quyền** → `CO_QUAN_THAM_QUYEN` (span: `[23:27]`) *(lồng trong `e2` (`DIEM`))*
- `[e4]` **tài sản** → `TAI_SAN_VAT_CHAT` (span: `[13:14]`) *(lồng trong `e2` (`DIEM`))*

**Quan hệ:**
- (`e1` Khoản 2 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 10 `[DIEU]`)
- (`e2` c ) Được bồi thường , hỗ trợ về tài sản gắn liền với đất theo quy định của pháp luật khi cơ quan nhà nước có thẩm quyền thu hồi đất đã nhận khoán để sử dụng vào mục đích khác ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e1` Khoản 2 `[KHOAN]`)


---

### Mẫu #03_2012_TT-BTNMT_105778#body_context_71 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[03/2012/TT-BTNMT]`<SO_HIEU>`** ban hành **[ngày 12 tháng 04 năm 2012]`<NGAY_BAN_HANH>`** bởi **[Bộ Tài nguyên và Môi trường]`<CO_QUAN_BAN_HANH>`** . **[Điều 10]`<DIEU>`** . **[Khoản 2]`<KHOAN>`** . **[d ) Được giảm các khoản phải nộp cho bên giao khoán theo quy định của pháp luật trong trường hợp bị thiên tai hoặc rủi ro do quá trình vận hành hồ chứa gây ra .]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **03/2012/TT-BTNMT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Tài nguyên và Môi trường** → `CO_QUAN_BAN_HANH` (span: `[11:15]`)
- `[e3]` **ngày 12 tháng 04 năm 2012** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 10** → `DIEU` (span: `[16:18]`)
- `[e5]` **Khoản 2** → `KHOAN` (span: `[19:21]`)
- `[e6]` **d ) Được giảm các khoản phải nộp cho bên giao khoán theo quy định của pháp luật trong trường hợp bị thiên tai hoặc rủi ro do quá trình vận hành hồ chứa gây ra .** → `DIEM` (span: `[22:51]`)

**Quan hệ:**
- (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Tài nguyên và Môi trường `[CO_QUAN_BAN_HANH]`)
- (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 12 tháng 04 năm 2012 `[NGAY_BAN_HANH]`)
- (`e4` Điều 10 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`)
- (`e5` Khoản 2 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 10 `[DIEU]`)
- (`e6` d ) Được giảm các khoản phải nộp cho bên giao khoán theo quy định của pháp luật trong trường hợp bị thiên tai hoặc rủi ro do quá trình vận hành hồ chứa gây ra . `[DIEM]`) ==[ **THUOC_VE** ]==> (`e5` Khoản 2 `[KHOAN]`)


---

### Mẫu #03_2012_TT-BTNMT_105778#body_context_72 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[03/2012/TT-BTNMT]`<SO_HIEU>`** ban hành **[ngày 12 tháng 04 năm 2012]`<NGAY_BAN_HANH>`** bởi **[Bộ Tài nguyên và Môi trường]`<CO_QUAN_BAN_HANH>`** . **[Chương IV]`<CHUONG>`** . **[Điều 11 . Hồ sơ giao , nhận khoán đất vùng bán ngập được lập theo mẫu ban hành kèm theo Thông tư này , gồm :]`<DIEU>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **03/2012/TT-BTNMT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Tài nguyên và Môi trường** → `CO_QUAN_BAN_HANH` (span: `[11:15]`)
- `[e3]` **ngày 12 tháng 04 năm 2012** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Chương IV** → `CHUONG` (span: `[16:18]`)
- `[e5]` **Điều 11 . Hồ sơ giao , nhận khoán đất vùng bán ngập được lập theo mẫu ban hành kèm theo Thông tư này , gồm :** → `DIEU` (span: `[19:43]`)

**Quan hệ:**
- (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Tài nguyên và Môi trường `[CO_QUAN_BAN_HANH]`)
- (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 12 tháng 04 năm 2012 `[NGAY_BAN_HANH]`)
- (`e4` Chương IV `[CHUONG]`) ==[ **THUOC_VE** ]==> (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`)
- (`e5` Điều 11 . Hồ sơ giao , nhận khoán đất vùng bán ngập được lập theo mẫu ban hành kèm theo Thông tư này , gồm : `[DIEU]`) ==[ **THUOC_VE** ]==> (`e4` Chương IV `[CHUONG]`)


---

### Mẫu #03_2012_TT-BTNMT_105778#body_context_73 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[03/2012/TT-BTNMT]`<SO_HIEU>`** ban hành **[ngày 12 tháng 04 năm 2012]`<NGAY_BAN_HANH>`** bởi **[Bộ Tài nguyên và Môi trường]`<CO_QUAN_BAN_HANH>`** . **[Điều 11]`<DIEU>`** . **[1 . **[Đơn đề nghị nhận giao khoán đất vùng bán ngập]`<GIAY_TO_HO_SO>`** ( theo **[mẫu số 01]`<THAM_CHIEU_PHAP_LY>`** ) ;]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **03/2012/TT-BTNMT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Tài nguyên và Môi trường** → `CO_QUAN_BAN_HANH` (span: `[11:15]`)
- `[e3]` **ngày 12 tháng 04 năm 2012** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 11** → `DIEU` (span: `[16:18]`)
- `[e5]` **1 . Đơn đề nghị nhận giao khoán đất vùng bán ngập ( theo mẫu số 01 ) ;** → `KHOAN` (span: `[19:35]`)
- `[e6]` **mẫu số 01** → `THAM_CHIEU_PHAP_LY` (span: `[31:33]`) *(lồng trong `e5` (`KHOAN`))*
- `[e7]` **Đơn đề nghị nhận giao khoán đất vùng bán ngập** → `GIAY_TO_HO_SO` (span: `[21:29]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Tài nguyên và Môi trường `[CO_QUAN_BAN_HANH]`)
- (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 12 tháng 04 năm 2012 `[NGAY_BAN_HANH]`)
- (`e4` Điều 11 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`)
- (`e5` 1 . Đơn đề nghị nhận giao khoán đất vùng bán ngập ( theo mẫu số 01 ) ; `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 11 `[DIEU]`)
- (`e5` 1 . Đơn đề nghị nhận giao khoán đất vùng bán ngập ( theo mẫu số 01 ) ; `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e6` mẫu số 01 `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #03_2012_TT-BTNMT_105778#body_standalone_74 (Loại: `body_standalone`)
> **[Điều 11]`<DIEU>`** . **[1 . **[Đơn đề nghị nhận giao khoán đất vùng bán ngập]`<GIAY_TO_HO_SO>`** ( theo **[mẫu số 01]`<THAM_CHIEU_PHAP_LY>`** ) ;]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 11** → `DIEU` (span: `[0:2]`)
- `[e1]` **1 . Đơn đề nghị nhận giao khoán đất vùng bán ngập ( theo mẫu số 01 ) ;** → `KHOAN` (span: `[3:19]`)
- `[e2]` **mẫu số 01** → `THAM_CHIEU_PHAP_LY` (span: `[15:17]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **Đơn đề nghị nhận giao khoán đất vùng bán ngập** → `GIAY_TO_HO_SO` (span: `[5:13]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 1 . Đơn đề nghị nhận giao khoán đất vùng bán ngập ( theo mẫu số 01 ) ; `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 11 `[DIEU]`)
- (`e1` 1 . Đơn đề nghị nhận giao khoán đất vùng bán ngập ( theo mẫu số 01 ) ; `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e2` mẫu số 01 `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #03_2012_TT-BTNMT_105778#body_context_75 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[03/2012/TT-BTNMT]`<SO_HIEU>`** ban hành **[ngày 12 tháng 04 năm 2012]`<NGAY_BAN_HANH>`** bởi **[Bộ Tài nguyên và Môi trường]`<CO_QUAN_BAN_HANH>`** . **[Điều 11]`<DIEU>`** . **[2 . Sơ đồ thửa đất vùng bán ngập ( theo **[mẫu số 02]`<THAM_CHIEU_PHAP_LY>`** ) ;]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **03/2012/TT-BTNMT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Tài nguyên và Môi trường** → `CO_QUAN_BAN_HANH` (span: `[11:15]`)
- `[e3]` **ngày 12 tháng 04 năm 2012** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 11** → `DIEU` (span: `[16:18]`)
- `[e5]` **2 . Sơ đồ thửa đất vùng bán ngập ( theo mẫu số 02 ) ;** → `KHOAN` (span: `[19:33]`)
- `[e6]` **mẫu số 02** → `THAM_CHIEU_PHAP_LY` (span: `[29:31]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Tài nguyên và Môi trường `[CO_QUAN_BAN_HANH]`)
- (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 12 tháng 04 năm 2012 `[NGAY_BAN_HANH]`)
- (`e4` Điều 11 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`)
- (`e5` 2 . Sơ đồ thửa đất vùng bán ngập ( theo mẫu số 02 ) ; `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 11 `[DIEU]`)
- (`e5` 2 . Sơ đồ thửa đất vùng bán ngập ( theo mẫu số 02 ) ; `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e6` mẫu số 02 `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #03_2012_TT-BTNMT_105778#body_standalone_76 (Loại: `body_standalone`)
> **[Điều 11]`<DIEU>`** . **[2 . Sơ đồ thửa đất vùng bán ngập ( theo **[mẫu số 02]`<THAM_CHIEU_PHAP_LY>`** ) ;]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 11** → `DIEU` (span: `[0:2]`)
- `[e1]` **2 . Sơ đồ thửa đất vùng bán ngập ( theo mẫu số 02 ) ;** → `KHOAN` (span: `[3:17]`)
- `[e2]` **mẫu số 02** → `THAM_CHIEU_PHAP_LY` (span: `[13:15]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 2 . Sơ đồ thửa đất vùng bán ngập ( theo mẫu số 02 ) ; `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 11 `[DIEU]`)
- (`e1` 2 . Sơ đồ thửa đất vùng bán ngập ( theo mẫu số 02 ) ; `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e2` mẫu số 02 `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #03_2012_TT-BTNMT_105778#body_context_77 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[03/2012/TT-BTNMT]`<SO_HIEU>`** ban hành **[ngày 12 tháng 04 năm 2012]`<NGAY_BAN_HANH>`** bởi **[Bộ Tài nguyên và Môi trường]`<CO_QUAN_BAN_HANH>`** . **[Điều 11]`<DIEU>`** . **[3 . Hợp đồng giao , nhận khoán đất vùng bán ngập ( theo **[mẫu số 03]`<THAM_CHIEU_PHAP_LY>`** ) ;]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **03/2012/TT-BTNMT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Tài nguyên và Môi trường** → `CO_QUAN_BAN_HANH` (span: `[11:15]`)
- `[e3]` **ngày 12 tháng 04 năm 2012** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 11** → `DIEU` (span: `[16:18]`)
- `[e5]` **3 . Hợp đồng giao , nhận khoán đất vùng bán ngập ( theo mẫu số 03 ) ;** → `KHOAN` (span: `[19:36]`)
- `[e6]` **mẫu số 03** → `THAM_CHIEU_PHAP_LY` (span: `[32:34]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Tài nguyên và Môi trường `[CO_QUAN_BAN_HANH]`)
- (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 12 tháng 04 năm 2012 `[NGAY_BAN_HANH]`)
- (`e4` Điều 11 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`)
- (`e5` 3 . Hợp đồng giao , nhận khoán đất vùng bán ngập ( theo mẫu số 03 ) ; `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 11 `[DIEU]`)
- (`e5` 3 . Hợp đồng giao , nhận khoán đất vùng bán ngập ( theo mẫu số 03 ) ; `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e6` mẫu số 03 `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #03_2012_TT-BTNMT_105778#body_context_78 (Loại: `body_context`)
> **[Bộ Tài nguyên và Môi trường]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[03/2012/TT-BTNMT]`<SO_HIEU>`** . **[Điều 11]`<DIEU>`** . **[4 . Biên bản giao đất vùng bán ngập ngoài thực địa ( theo **[mẫu số 04]`<THAM_CHIEU_PHAP_LY>`** ) .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[5:6]`)
- `[e1]` **03/2012/TT-BTNMT** → `SO_HIEU` (span: `[7:8]`)
- `[e2]` **Bộ Tài nguyên và Môi trường** → `CO_QUAN_BAN_HANH` (span: `[0:4]`)
- `[e3]` **Điều 11** → `DIEU` (span: `[9:11]`)
- `[e4]` **4 . Biên bản giao đất vùng bán ngập ngoài thực địa ( theo mẫu số 04 ) .** → `KHOAN` (span: `[12:28]`)
- `[e5]` **mẫu số 04** → `THAM_CHIEU_PHAP_LY` (span: `[24:26]`) *(lồng trong `e4` (`KHOAN`))*

**Quan hệ:**
- (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Tài nguyên và Môi trường `[CO_QUAN_BAN_HANH]`)
- (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 11 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`)
- (`e4` 4 . Biên bản giao đất vùng bán ngập ngoài thực địa ( theo mẫu số 04 ) . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 11 `[DIEU]`)
- (`e4` 4 . Biên bản giao đất vùng bán ngập ngoài thực địa ( theo mẫu số 04 ) . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e5` mẫu số 04 `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #03_2012_TT-BTNMT_105778#body_standalone_79 (Loại: `body_standalone`)
> **[Điều 11]`<DIEU>`** . **[4 . Biên bản giao đất vùng bán ngập ngoài thực địa ( theo **[mẫu số 04]`<THAM_CHIEU_PHAP_LY>`** ) .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 11** → `DIEU` (span: `[0:2]`)
- `[e1]` **4 . Biên bản giao đất vùng bán ngập ngoài thực địa ( theo mẫu số 04 ) .** → `KHOAN` (span: `[3:19]`)
- `[e2]` **mẫu số 04** → `THAM_CHIEU_PHAP_LY` (span: `[15:17]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 4 . Biên bản giao đất vùng bán ngập ngoài thực địa ( theo mẫu số 04 ) . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 11 `[DIEU]`)
- (`e1` 4 . Biên bản giao đất vùng bán ngập ngoài thực địa ( theo mẫu số 04 ) . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e2` mẫu số 04 `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #03_2012_TT-BTNMT_105778#body_context_80 (Loại: `body_context`)
> **[Bộ Tài nguyên và Môi trường]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[03/2012/TT-BTNMT]`<SO_HIEU>`** . **[Điều 12]`<DIEU>`** . **[2 . Bên giao khoán có trách nhiệm xem xét đơn xin giao khoán đất vùng bán ngập , nếu đủ điều kiện phải thông báo cho bên nhận khoán và thực hiện việc trích lục bản đồ hoặc trích đo địa chính khu đất ; chuẩn bị hợp đồng giao , nhận khoán đất vùng bán ngập .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[5:6]`)
- `[e1]` **03/2012/TT-BTNMT** → `SO_HIEU` (span: `[7:8]`)
- `[e2]` **Bộ Tài nguyên và Môi trường** → `CO_QUAN_BAN_HANH` (span: `[0:4]`)
- `[e3]` **Điều 12** → `DIEU` (span: `[9:11]`)
- `[e4]` **2 . Bên giao khoán có trách nhiệm xem xét đơn xin giao khoán đất vùng bán ngập , nếu đủ điều kiện phải thông báo cho bên nhận khoán và thực hiện việc trích lục bản đồ hoặc trích đo địa chính khu đất ; chuẩn bị hợp đồng giao , nhận khoán đất vùng bán ngập .** → `KHOAN` (span: `[12:60]`)

**Quan hệ:**
- (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Tài nguyên và Môi trường `[CO_QUAN_BAN_HANH]`)
- (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 12 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`)
- (`e4` 2 . Bên giao khoán có trách nhiệm xem xét đơn xin giao khoán đất vùng bán ngập , nếu đủ điều kiện phải thông báo cho bên nhận khoán và thực hiện việc trích lục bản đồ hoặc trích đo địa chính khu đất ; chuẩn bị hợp đồng giao , nhận khoán đất vùng bán ngập . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 12 `[DIEU]`)


---

### Mẫu #03_2012_TT-BTNMT_105778#body_context_81 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[03/2012/TT-BTNMT]`<SO_HIEU>`** ban hành **[ngày 12 tháng 04 năm 2012]`<NGAY_BAN_HANH>`** bởi **[Bộ Tài nguyên và Môi trường]`<CO_QUAN_BAN_HANH>`** . **[Điều 12]`<DIEU>`** . **[4 . Thời gian thực hiện các công việc **[quy định tại]`<TU_KHOA_PHAP_LY>`** **[các khoản 1 , 2 và 3 Điều này]`<THAM_CHIEU_PHAP_LY>`** không quá năm mươi ( 50 ) ngày làm việc kể từ ngày bên giao khoán nhận đủ hồ sơ hợp lệ .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **03/2012/TT-BTNMT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Tài nguyên và Môi trường** → `CO_QUAN_BAN_HANH` (span: `[11:15]`)
- `[e3]` **ngày 12 tháng 04 năm 2012** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 12** → `DIEU` (span: `[16:18]`)
- `[e5]` **4 . Thời gian thực hiện các công việc quy định tại các khoản 1 , 2 và 3 Điều này không quá năm mươi ( 50 ) ngày làm việc kể từ ngày bên giao khoán nhận đủ hồ sơ hợp lệ .** → `KHOAN` (span: `[19:54]`)
- `[e6]` **các khoản 1 , 2 và 3 Điều này** → `THAM_CHIEU_PHAP_LY` (span: `[27:36]`) *(lồng trong `e5` (`KHOAN`))*
- `[e7]` **quy định tại** → `TU_KHOA_PHAP_LY` (span: `[25:27]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Tài nguyên và Môi trường `[CO_QUAN_BAN_HANH]`)
- (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 12 tháng 04 năm 2012 `[NGAY_BAN_HANH]`)
- (`e4` Điều 12 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`)
- (`e5` 4 . Thời gian thực hiện các công việc quy định tại các khoản 1 , 2 và 3 Điều này không quá năm mươi ( 50 ) ngày làm việc kể từ ngày bên giao khoán nhận đủ hồ sơ hợp lệ . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 12 `[DIEU]`)
- (`e7` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e6` các khoản 1 , 2 và 3 Điều này `[THAM_CHIEU_PHAP_LY]`)
- (`e5` 4 . Thời gian thực hiện các công việc quy định tại các khoản 1 , 2 và 3 Điều này không quá năm mươi ( 50 ) ngày làm việc kể từ ngày bên giao khoán nhận đủ hồ sơ hợp lệ . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e6` các khoản 1 , 2 và 3 Điều này `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #03_2012_TT-BTNMT_105778#body_standalone_82 (Loại: `body_standalone`)
> **[Điều 12]`<DIEU>`** . **[4 . Thời gian thực hiện các công việc **[quy định tại]`<TU_KHOA_PHAP_LY>`** **[các khoản 1 , 2 và 3 Điều này]`<THAM_CHIEU_PHAP_LY>`** không quá năm mươi ( 50 ) ngày làm việc kể từ ngày bên giao khoán nhận đủ hồ sơ hợp lệ .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 12** → `DIEU` (span: `[0:2]`)
- `[e1]` **4 . Thời gian thực hiện các công việc quy định tại các khoản 1 , 2 và 3 Điều này không quá năm mươi ( 50 ) ngày làm việc kể từ ngày bên giao khoán nhận đủ hồ sơ hợp lệ .** → `KHOAN` (span: `[3:38]`)
- `[e2]` **các khoản 1 , 2 và 3 Điều này** → `THAM_CHIEU_PHAP_LY` (span: `[11:20]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **quy định tại** → `TU_KHOA_PHAP_LY` (span: `[9:11]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 4 . Thời gian thực hiện các công việc quy định tại các khoản 1 , 2 và 3 Điều này không quá năm mươi ( 50 ) ngày làm việc kể từ ngày bên giao khoán nhận đủ hồ sơ hợp lệ . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 12 `[DIEU]`)
- (`e3` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e2` các khoản 1 , 2 và 3 Điều này `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 4 . Thời gian thực hiện các công việc quy định tại các khoản 1 , 2 và 3 Điều này không quá năm mươi ( 50 ) ngày làm việc kể từ ngày bên giao khoán nhận đủ hồ sơ hợp lệ . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e2` các khoản 1 , 2 và 3 Điều này `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #03_2012_TT-BTNMT_105778#body_context_83 (Loại: `body_context`)
> **[Bộ Tài nguyên và Môi trường]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[03/2012/TT-BTNMT]`<SO_HIEU>`** . **[Chương V. TỔ CHỨC THỰC HIỆN]`<CHUONG>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[5:6]`)
- `[e1]` **03/2012/TT-BTNMT** → `SO_HIEU` (span: `[7:8]`)
- `[e2]` **Bộ Tài nguyên và Môi trường** → `CO_QUAN_BAN_HANH` (span: `[0:4]`)
- `[e3]` **Chương V. TỔ CHỨC THỰC HIỆN** → `CHUONG` (span: `[9:13]`)

**Quan hệ:**
- (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Tài nguyên và Môi trường `[CO_QUAN_BAN_HANH]`)
- (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Chương V. TỔ CHỨC THỰC HIỆN `[CHUONG]`) ==[ **THUOC_VE** ]==> (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`)


---

### Mẫu #03_2012_TT-BTNMT_105778#body_context_84 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[03/2012/TT-BTNMT]`<SO_HIEU>`** ban hành **[ngày 12 tháng 04 năm 2012]`<NGAY_BAN_HANH>`** bởi **[Bộ Tài nguyên và Môi trường]`<CO_QUAN_BAN_HANH>`** . **[Điều 14]`<DIEU>`** . **[1 . Tổng cục trưởng Tổng cục Quản lý đất đai có trách nhiệm hướng dẫn , kiểm tra , đôn đốc thực hiện Thông tư này và tổng hợp báo cáo **[Bộ Tài nguyên và Môi trường]`<CO_QUAN_THAM_QUYEN>`** vào thời điểm **[báo cáo kết quả thống kê đất đai hàng năm]`<GIAY_TO_HO_SO>`** .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **03/2012/TT-BTNMT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Tài nguyên và Môi trường** → `CO_QUAN_BAN_HANH` (span: `[11:15]`)
- `[e3]` **ngày 12 tháng 04 năm 2012** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 14** → `DIEU` (span: `[16:18]`)
- `[e5]` **1 . Tổng cục trưởng Tổng cục Quản lý đất đai có trách nhiệm hướng dẫn , kiểm tra , đôn đốc thực hiện Thông tư này và tổng hợp báo cáo Bộ Tài nguyên và Môi trường vào thời điểm báo cáo kết quả thống kê đất đai hàng năm .** → `KHOAN` (span: `[19:51]`)
- `[e6]` **Bộ Tài nguyên và Môi trường** → `CO_QUAN_THAM_QUYEN` (span: `[38:42]`) *(lồng trong `e5` (`KHOAN`))*
- `[e7]` **báo cáo kết quả thống kê đất đai hàng năm** → `GIAY_TO_HO_SO` (span: `[44:50]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Tài nguyên và Môi trường `[CO_QUAN_BAN_HANH]`)
- (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 12 tháng 04 năm 2012 `[NGAY_BAN_HANH]`)
- (`e4` Điều 14 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`)
- (`e5` 1 . Tổng cục trưởng Tổng cục Quản lý đất đai có trách nhiệm hướng dẫn , kiểm tra , đôn đốc thực hiện Thông tư này và tổng hợp báo cáo Bộ Tài nguyên và Môi trường vào thời điểm báo cáo kết quả thống kê đất đai hàng năm . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 14 `[DIEU]`)


---

### Mẫu #03_2012_TT-BTNMT_105778#body_standalone_85 (Loại: `body_standalone`)
> **[Điều 14]`<DIEU>`** . **[1 . Tổng cục trưởng Tổng cục Quản lý đất đai có trách nhiệm hướng dẫn , kiểm tra , đôn đốc thực hiện Thông tư này và tổng hợp báo cáo **[Bộ Tài nguyên và Môi trường]`<CO_QUAN_THAM_QUYEN>`** vào thời điểm **[báo cáo kết quả thống kê đất đai hàng năm]`<GIAY_TO_HO_SO>`** .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 14** → `DIEU` (span: `[0:2]`)
- `[e1]` **1 . Tổng cục trưởng Tổng cục Quản lý đất đai có trách nhiệm hướng dẫn , kiểm tra , đôn đốc thực hiện Thông tư này và tổng hợp báo cáo Bộ Tài nguyên và Môi trường vào thời điểm báo cáo kết quả thống kê đất đai hàng năm .** → `KHOAN` (span: `[3:35]`)
- `[e2]` **Bộ Tài nguyên và Môi trường** → `CO_QUAN_THAM_QUYEN` (span: `[22:26]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **báo cáo kết quả thống kê đất đai hàng năm** → `GIAY_TO_HO_SO` (span: `[28:34]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 1 . Tổng cục trưởng Tổng cục Quản lý đất đai có trách nhiệm hướng dẫn , kiểm tra , đôn đốc thực hiện Thông tư này và tổng hợp báo cáo Bộ Tài nguyên và Môi trường vào thời điểm báo cáo kết quả thống kê đất đai hàng năm . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 14 `[DIEU]`)


---

### Mẫu #03_2012_TT-BTNMT_105778#body_context_86 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[03/2012/TT-BTNMT]`<SO_HIEU>`** ban hành **[ngày 12 tháng 04 năm 2012]`<NGAY_BAN_HANH>`** bởi **[Bộ Tài nguyên và Môi trường]`<CO_QUAN_BAN_HANH>`** . **[Điều 14]`<DIEU>`** . **[2 . **[Chủ tịch Ủy ban nhân dân cấp tỉnh]`<CO_QUAN_THAM_QUYEN>`** chỉ đạo các cấp , các ngành trong tỉnh quản lý , sử dụng đất vùng bán ngập **[tại địa phương]`<DIA_DIEM>`** **[theo quy định tại]`<TU_KHOA_PHAP_LY>`** **[Thông tư này]`<THAM_CHIEU_PHAP_LY>`** .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **03/2012/TT-BTNMT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Tài nguyên và Môi trường** → `CO_QUAN_BAN_HANH` (span: `[11:15]`)
- `[e3]` **ngày 12 tháng 04 năm 2012** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 14** → `DIEU` (span: `[16:18]`)
- `[e5]` **2 . Chủ tịch Ủy ban nhân dân cấp tỉnh chỉ đạo các cấp , các ngành trong tỉnh quản lý , sử dụng đất vùng bán ngập tại địa phương theo quy định tại Thông tư này .** → `KHOAN` (span: `[19:49]`)
- `[e6]` **Thông tư này** → `THAM_CHIEU_PHAP_LY` (span: `[46:48]`) *(lồng trong `e5` (`KHOAN`))*
- `[e7]` **theo quy định tại** → `TU_KHOA_PHAP_LY` (span: `[43:46]`) *(lồng trong `e5` (`KHOAN`))*
- `[e8]` **Chủ tịch Ủy ban nhân dân cấp tỉnh** → `CO_QUAN_THAM_QUYEN` (span: `[21:26]`) *(lồng trong `e5` (`KHOAN`))*
- `[e9]` **tại địa phương** → `DIA_DIEM` (span: `[41:43]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Tài nguyên và Môi trường `[CO_QUAN_BAN_HANH]`)
- (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 12 tháng 04 năm 2012 `[NGAY_BAN_HANH]`)
- (`e4` Điều 14 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`)
- (`e5` 2 . Chủ tịch Ủy ban nhân dân cấp tỉnh chỉ đạo các cấp , các ngành trong tỉnh quản lý , sử dụng đất vùng bán ngập tại địa phương theo quy định tại Thông tư này . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 14 `[DIEU]`)
- (`e7` theo quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e6` Thông tư này `[THAM_CHIEU_PHAP_LY]`)
- (`e5` 2 . Chủ tịch Ủy ban nhân dân cấp tỉnh chỉ đạo các cấp , các ngành trong tỉnh quản lý , sử dụng đất vùng bán ngập tại địa phương theo quy định tại Thông tư này . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e6` Thông tư này `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #03_2012_TT-BTNMT_105778#body_standalone_87 (Loại: `body_standalone`)
> **[Điều 14]`<DIEU>`** . **[2 . **[Chủ tịch Ủy ban nhân dân cấp tỉnh]`<CO_QUAN_THAM_QUYEN>`** chỉ đạo các cấp , các ngành trong tỉnh quản lý , sử dụng đất vùng bán ngập **[tại địa phương]`<DIA_DIEM>`** **[theo quy định tại]`<TU_KHOA_PHAP_LY>`** **[Thông tư này]`<THAM_CHIEU_PHAP_LY>`** .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 14** → `DIEU` (span: `[0:2]`)
- `[e1]` **2 . Chủ tịch Ủy ban nhân dân cấp tỉnh chỉ đạo các cấp , các ngành trong tỉnh quản lý , sử dụng đất vùng bán ngập tại địa phương theo quy định tại Thông tư này .** → `KHOAN` (span: `[3:33]`)
- `[e2]` **Thông tư này** → `THAM_CHIEU_PHAP_LY` (span: `[30:32]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **theo quy định tại** → `TU_KHOA_PHAP_LY` (span: `[27:30]`) *(lồng trong `e1` (`KHOAN`))*
- `[e4]` **Chủ tịch Ủy ban nhân dân cấp tỉnh** → `CO_QUAN_THAM_QUYEN` (span: `[5:10]`) *(lồng trong `e1` (`KHOAN`))*
- `[e5]` **tại địa phương** → `DIA_DIEM` (span: `[25:27]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 2 . Chủ tịch Ủy ban nhân dân cấp tỉnh chỉ đạo các cấp , các ngành trong tỉnh quản lý , sử dụng đất vùng bán ngập tại địa phương theo quy định tại Thông tư này . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 14 `[DIEU]`)
- (`e3` theo quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e2` Thông tư này `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 2 . Chủ tịch Ủy ban nhân dân cấp tỉnh chỉ đạo các cấp , các ngành trong tỉnh quản lý , sử dụng đất vùng bán ngập tại địa phương theo quy định tại Thông tư này . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e2` Thông tư này `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #03_2012_TT-BTNMT_105778#body_context_88 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[03/2012/TT-BTNMT]`<SO_HIEU>`** của **[Bộ Tài nguyên và Môi trường]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Lao động - Thương binh và Xã hội]`<LINH_VUC>`** . **[Điều 14]`<DIEU>`** . **[3 . **[Giám đốc Sở Tài nguyên và Môi trường]`<CO_QUAN_THAM_QUYEN>`** có trách nhiệm giúp **[Ủy ban nhân dân cấp tỉnh]`<CO_QUAN_THAM_QUYEN>`** ; Trưởng **[Phòng Tài nguyên và Môi trường]`<CO_QUAN_THAM_QUYEN>`** có trách nhiệm giúp **[Ủy ban nhân dân cấp huyện]`<CO_QUAN_THAM_QUYEN>`** ; **[cán bộ]`<CHU_THE_CA_NHAN>`** địa chính cấp xã có trách nhiệm giúp **[Ủy ban nhân dân cấp xã]`<CO_QUAN_THAM_QUYEN>`** trong việc tổ chức triển khai thực hiện Thông tư này .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **03/2012/TT-BTNMT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Tài nguyên và Môi trường** → `CO_QUAN_BAN_HANH` (span: `[4:8]`)
- `[e3]` **Lao động - Thương binh và Xã hội** → `LINH_VUC` (span: `[10:15]`)
- `[e4]` **Điều 14** → `DIEU` (span: `[16:18]`)
- `[e5]` **3 . Giám đốc Sở Tài nguyên và Môi trường có trách nhiệm giúp Ủy ban nhân dân cấp tỉnh ; Trưởng Phòng Tài nguyên và Môi trường có trách nhiệm giúp Ủy ban nhân dân cấp huyện ; cán bộ địa chính cấp xã có trách nhiệm giúp Ủy ban nhân dân cấp xã trong việc tổ chức triển khai thực hiện Thông tư này .** → `KHOAN` (span: `[19:66]`)
- `[e6]` **Giám đốc Sở Tài nguyên và Môi trường** → `CO_QUAN_THAM_QUYEN` (span: `[21:26]`) *(lồng trong `e5` (`KHOAN`))*
- `[e7]` **Ủy ban nhân dân cấp tỉnh** → `CO_QUAN_THAM_QUYEN` (span: `[29:33]`) *(lồng trong `e5` (`KHOAN`))*
- `[e8]` **Phòng Tài nguyên và Môi trường** → `CO_QUAN_THAM_QUYEN` (span: `[35:39]`) *(lồng trong `e5` (`KHOAN`))*
- `[e9]` **Ủy ban nhân dân cấp huyện** → `CO_QUAN_THAM_QUYEN` (span: `[42:46]`) *(lồng trong `e5` (`KHOAN`))*
- `[e10]` **Ủy ban nhân dân cấp xã** → `CO_QUAN_THAM_QUYEN` (span: `[54:58]`) *(lồng trong `e5` (`KHOAN`))*
- `[e11]` **cán bộ** → `CHU_THE_CA_NHAN` (span: `[47:48]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Tài nguyên và Môi trường `[CO_QUAN_BAN_HANH]`)
- (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Lao động - Thương binh và Xã hội `[LINH_VUC]`)
- (`e4` Điều 14 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`)
- (`e5` 3 . Giám đốc Sở Tài nguyên và Môi trường có trách nhiệm giúp Ủy ban nhân dân cấp tỉnh ; Trưởng Phòng Tài nguyên và Môi trường có trách nhiệm giúp Ủy ban nhân dân cấp huyện ; cán bộ địa chính cấp xã có trách nhiệm giúp Ủy ban nhân dân cấp xã trong việc tổ chức triển khai thực hiện Thông tư này . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 14 `[DIEU]`)
- (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Lao động - Thương binh và Xã hội `[LINH_VUC]`)
- (`e5` 3 . Giám đốc Sở Tài nguyên và Môi trường có trách nhiệm giúp Ủy ban nhân dân cấp tỉnh ; Trưởng Phòng Tài nguyên và Môi trường có trách nhiệm giúp Ủy ban nhân dân cấp huyện ; cán bộ địa chính cấp xã có trách nhiệm giúp Ủy ban nhân dân cấp xã trong việc tổ chức triển khai thực hiện Thông tư này . `[KHOAN]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Lao động - Thương binh và Xã hội `[LINH_VUC]`)


---

### Mẫu #03_2012_TT-BTNMT_105778#body_standalone_89 (Loại: `body_standalone`)
> **[Điều 14]`<DIEU>`** . **[3 . **[Giám đốc Sở Tài nguyên và Môi trường]`<CO_QUAN_THAM_QUYEN>`** có trách nhiệm giúp **[Ủy ban nhân dân cấp tỉnh]`<CO_QUAN_THAM_QUYEN>`** ; Trưởng **[Phòng Tài nguyên và Môi trường]`<CO_QUAN_THAM_QUYEN>`** có trách nhiệm giúp **[Ủy ban nhân dân cấp huyện]`<CO_QUAN_THAM_QUYEN>`** ; **[cán bộ]`<CHU_THE_CA_NHAN>`** địa chính cấp xã có trách nhiệm giúp **[Ủy ban nhân dân cấp xã]`<CO_QUAN_THAM_QUYEN>`** trong việc tổ chức triển khai thực hiện Thông tư này .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 14** → `DIEU` (span: `[0:2]`)
- `[e1]` **3 . Giám đốc Sở Tài nguyên và Môi trường có trách nhiệm giúp Ủy ban nhân dân cấp tỉnh ; Trưởng Phòng Tài nguyên và Môi trường có trách nhiệm giúp Ủy ban nhân dân cấp huyện ; cán bộ địa chính cấp xã có trách nhiệm giúp Ủy ban nhân dân cấp xã trong việc tổ chức triển khai thực hiện Thông tư này .** → `KHOAN` (span: `[3:50]`)
- `[e2]` **Giám đốc Sở Tài nguyên và Môi trường** → `CO_QUAN_THAM_QUYEN` (span: `[5:10]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **Ủy ban nhân dân cấp tỉnh** → `CO_QUAN_THAM_QUYEN` (span: `[13:17]`) *(lồng trong `e1` (`KHOAN`))*
- `[e4]` **Phòng Tài nguyên và Môi trường** → `CO_QUAN_THAM_QUYEN` (span: `[19:23]`) *(lồng trong `e1` (`KHOAN`))*
- `[e5]` **Ủy ban nhân dân cấp huyện** → `CO_QUAN_THAM_QUYEN` (span: `[26:30]`) *(lồng trong `e1` (`KHOAN`))*
- `[e6]` **Ủy ban nhân dân cấp xã** → `CO_QUAN_THAM_QUYEN` (span: `[38:42]`) *(lồng trong `e1` (`KHOAN`))*
- `[e7]` **cán bộ** → `CHU_THE_CA_NHAN` (span: `[31:32]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 3 . Giám đốc Sở Tài nguyên và Môi trường có trách nhiệm giúp Ủy ban nhân dân cấp tỉnh ; Trưởng Phòng Tài nguyên và Môi trường có trách nhiệm giúp Ủy ban nhân dân cấp huyện ; cán bộ địa chính cấp xã có trách nhiệm giúp Ủy ban nhân dân cấp xã trong việc tổ chức triển khai thực hiện Thông tư này . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 14 `[DIEU]`)


---

### Mẫu #03_2012_TT-BTNMT_105778#body_context_90 (Loại: `body_context`)
> **[Bộ Tài nguyên và Môi trường]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[03/2012/TT-BTNMT]`<SO_HIEU>`** . **[Điều 14]`<DIEU>`** . **[4 . Chủ đập có trách nhiệm phối hợp với **[Sở Tài nguyên và Môi trường]`<CO_QUAN_THAM_QUYEN>`** , **[Ủy ban nhân dân cấp huyện]`<CO_QUAN_THAM_QUYEN>`** , cấp xã để quản lý , sử dụng đất vùng bán ngập **[theo quy định tại]`<TU_KHOA_PHAP_LY>`** **[Thông tư này]`<THAM_CHIEU_PHAP_LY>`** .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[5:6]`)
- `[e1]` **03/2012/TT-BTNMT** → `SO_HIEU` (span: `[7:8]`)
- `[e2]` **Bộ Tài nguyên và Môi trường** → `CO_QUAN_BAN_HANH` (span: `[0:4]`)
- `[e3]` **Điều 14** → `DIEU` (span: `[9:11]`)
- `[e4]` **4 . Chủ đập có trách nhiệm phối hợp với Sở Tài nguyên và Môi trường , Ủy ban nhân dân cấp huyện , cấp xã để quản lý , sử dụng đất vùng bán ngập theo quy định tại Thông tư này .** → `KHOAN` (span: `[12:46]`)
- `[e5]` **Thông tư này** → `THAM_CHIEU_PHAP_LY` (span: `[43:45]`) *(lồng trong `e4` (`KHOAN`))*
- `[e6]` **theo quy định tại** → `TU_KHOA_PHAP_LY` (span: `[40:43]`) *(lồng trong `e4` (`KHOAN`))*
- `[e7]` **Sở Tài nguyên và Môi trường** → `CO_QUAN_THAM_QUYEN` (span: `[20:24]`) *(lồng trong `e4` (`KHOAN`))*
- `[e8]` **Ủy ban nhân dân cấp huyện** → `CO_QUAN_THAM_QUYEN` (span: `[25:29]`) *(lồng trong `e4` (`KHOAN`))*

**Quan hệ:**
- (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Tài nguyên và Môi trường `[CO_QUAN_BAN_HANH]`)
- (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 14 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 03/2012/TT-BTNMT `[SO_HIEU]`)
- (`e4` 4 . Chủ đập có trách nhiệm phối hợp với Sở Tài nguyên và Môi trường , Ủy ban nhân dân cấp huyện , cấp xã để quản lý , sử dụng đất vùng bán ngập theo quy định tại Thông tư này . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 14 `[DIEU]`)
- (`e6` theo quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e5` Thông tư này `[THAM_CHIEU_PHAP_LY]`)
- (`e4` 4 . Chủ đập có trách nhiệm phối hợp với Sở Tài nguyên và Môi trường , Ủy ban nhân dân cấp huyện , cấp xã để quản lý , sử dụng đất vùng bán ngập theo quy định tại Thông tư này . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e5` Thông tư này `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #03_2012_TT-BTNMT_105778#body_standalone_91 (Loại: `body_standalone`)
> **[Điều 14]`<DIEU>`** . **[4 . Chủ đập có trách nhiệm phối hợp với **[Sở Tài nguyên và Môi trường]`<CO_QUAN_THAM_QUYEN>`** , **[Ủy ban nhân dân cấp huyện]`<CO_QUAN_THAM_QUYEN>`** , cấp xã để quản lý , sử dụng đất vùng bán ngập **[theo quy định tại]`<TU_KHOA_PHAP_LY>`** **[Thông tư này]`<THAM_CHIEU_PHAP_LY>`** .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 14** → `DIEU` (span: `[0:2]`)
- `[e1]` **4 . Chủ đập có trách nhiệm phối hợp với Sở Tài nguyên và Môi trường , Ủy ban nhân dân cấp huyện , cấp xã để quản lý , sử dụng đất vùng bán ngập theo quy định tại Thông tư này .** → `KHOAN` (span: `[3:37]`)
- `[e2]` **Thông tư này** → `THAM_CHIEU_PHAP_LY` (span: `[34:36]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **theo quy định tại** → `TU_KHOA_PHAP_LY` (span: `[31:34]`) *(lồng trong `e1` (`KHOAN`))*
- `[e4]` **Sở Tài nguyên và Môi trường** → `CO_QUAN_THAM_QUYEN` (span: `[11:15]`) *(lồng trong `e1` (`KHOAN`))*
- `[e5]` **Ủy ban nhân dân cấp huyện** → `CO_QUAN_THAM_QUYEN` (span: `[16:20]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 4 . Chủ đập có trách nhiệm phối hợp với Sở Tài nguyên và Môi trường , Ủy ban nhân dân cấp huyện , cấp xã để quản lý , sử dụng đất vùng bán ngập theo quy định tại Thông tư này . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 14 `[DIEU]`)
- (`e3` theo quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e2` Thông tư này `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 4 . Chủ đập có trách nhiệm phối hợp với Sở Tài nguyên và Môi trường , Ủy ban nhân dân cấp huyện , cấp xã để quản lý , sử dụng đất vùng bán ngập theo quy định tại Thông tư này . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e2` Thông tư này `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #03_2012_TT-BTNMT_105778#hard_negative_92 (Loại: `hard_negative`)
> CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM Độc lập - Tự do - Hạnh phúc


---
