# Dữ liệu gán nhãn văn bản: 03_2021_TT-BGTVT_147344
- **Thể loại**: `thong_tu`
- **Phân vùng dữ liệu**: `TRAIN`
- **Tổng số mẫu**: 107 mẫu
- **Tổng số thực thể**: 728
- **Tổng số quan hệ**: 516

---

### Mẫu #03_2021_TT-BGTVT_147344#preamble_context_0 (Loại: `preamble_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[03/2021/TT-BGTVT]`<SO_HIEU>`** của **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** . **[Căn cứ]`<TU_KHOA_PHAP_LY>`** **[Luật Xây dựng 2014]`<THAM_CHIEU_PHAP_LY>`** ; Luật **[sửa đổi , bổ sung một số điều của]`<TU_KHOA_PHAP_LY>`** Luật Xây dựng năm 2020 ;

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **03/2021/TT-BGTVT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[4:7]`)
- `[e3]` **Luật Xây dựng 2014** → `THAM_CHIEU_PHAP_LY` (span: `[9:12]`)
- `[e4]` **Căn cứ** → `TU_KHOA_PHAP_LY` (span: `[8:9]`)
- `[e5]` **sửa đổi , bổ sung một số điều của** → `TU_KHOA_PHAP_LY` (span: `[14:20]`)

**Quan hệ:**
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e4` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Luật Xây dựng 2014 `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Luật Xây dựng 2014 `[THAM_CHIEU_PHAP_LY]`)


---

### Mẫu #03_2021_TT-BGTVT_147344#preamble_standalone_1 (Loại: `preamble_standalone`)
> **[Căn cứ]`<TU_KHOA_PHAP_LY>`** **[Luật Xây dựng 2014]`<THAM_CHIEU_PHAP_LY>`** ; Luật **[sửa đổi , bổ sung một số điều của]`<TU_KHOA_PHAP_LY>`** Luật Xây dựng năm 2020 ;

**Thực thể:**
- `[e0]` **Luật Xây dựng 2014** → `THAM_CHIEU_PHAP_LY` (span: `[1:4]`)
- `[e1]` **Căn cứ** → `TU_KHOA_PHAP_LY` (span: `[0:1]`)
- `[e2]` **sửa đổi , bổ sung một số điều của** → `TU_KHOA_PHAP_LY` (span: `[6:12]`)

**Quan hệ:**
- (`e1` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e0` Luật Xây dựng 2014 `[THAM_CHIEU_PHAP_LY]`)


---

### Mẫu #03_2021_TT-BGTVT_147344#preamble_context_2 (Loại: `preamble_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[03/2021/TT-BGTVT]`<SO_HIEU>`** của **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** . **[Căn cứ]`<TU_KHOA_PHAP_LY>`** **[Luật Đường sắt năm 2017]`<THAM_CHIEU_PHAP_LY>`** ;

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **03/2021/TT-BGTVT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[4:7]`)
- `[e3]` **Luật Đường sắt năm 2017** → `THAM_CHIEU_PHAP_LY` (span: `[9:13]`)
- `[e4]` **Căn cứ** → `TU_KHOA_PHAP_LY` (span: `[8:9]`)

**Quan hệ:**
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e4` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Luật Đường sắt năm 2017 `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Luật Đường sắt năm 2017 `[THAM_CHIEU_PHAP_LY]`)


---

### Mẫu #03_2021_TT-BGTVT_147344#preamble_standalone_3 (Loại: `preamble_standalone`)
> **[Căn cứ]`<TU_KHOA_PHAP_LY>`** **[Luật Đường sắt năm 2017]`<THAM_CHIEU_PHAP_LY>`** ;

**Thực thể:**
- `[e0]` **Luật Đường sắt năm 2017** → `THAM_CHIEU_PHAP_LY` (span: `[1:5]`)
- `[e1]` **Căn cứ** → `TU_KHOA_PHAP_LY` (span: `[0:1]`)

**Quan hệ:**
- (`e1` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e0` Luật Đường sắt năm 2017 `[THAM_CHIEU_PHAP_LY]`)


---

### Mẫu #03_2021_TT-BGTVT_147344#preamble_context_4 (Loại: `preamble_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[03/2021/TT-BGTVT]`<SO_HIEU>`** của **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** . **[Căn cứ]`<TU_KHOA_PHAP_LY>`** **[Nghị định số 46/2015/NĐ-CP]`<THAM_CHIEU_PHAP_LY>`** **[ngày 12 tháng 5 năm 2015]`<NGAY_THAM_CHIEU>`** của **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** về quản lý chất lượng và bảo trì công trình xây dựng ;

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **03/2021/TT-BGTVT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[4:7]`)
- `[e3]` **Nghị định số 46/2015/NĐ-CP** → `THAM_CHIEU_PHAP_LY` (span: `[9:12]`)
- `[e4]` **Căn cứ** → `TU_KHOA_PHAP_LY` (span: `[8:9]`)
- `[e5]` **ngày 12 tháng 5 năm 2015** → `NGAY_THAM_CHIEU` (span: `[12:18]`)
- `[e6]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[19:20]`)

**Quan hệ:**
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e4` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Nghị định số 46/2015/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Nghị định số 46/2015/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e3` Nghị định số 46/2015/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e5` ngày 12 tháng 5 năm 2015 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #03_2021_TT-BGTVT_147344#preamble_standalone_5 (Loại: `preamble_standalone`)
> **[Căn cứ]`<TU_KHOA_PHAP_LY>`** **[Nghị định số 46/2015/NĐ-CP]`<THAM_CHIEU_PHAP_LY>`** **[ngày 12 tháng 5 năm 2015]`<NGAY_THAM_CHIEU>`** của **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** về quản lý chất lượng và bảo trì công trình xây dựng ;

**Thực thể:**
- `[e0]` **Nghị định số 46/2015/NĐ-CP** → `THAM_CHIEU_PHAP_LY` (span: `[1:4]`)
- `[e1]` **Căn cứ** → `TU_KHOA_PHAP_LY` (span: `[0:1]`)
- `[e2]` **ngày 12 tháng 5 năm 2015** → `NGAY_THAM_CHIEU` (span: `[4:10]`)
- `[e3]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[11:12]`)

**Quan hệ:**
- (`e1` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e0` Nghị định số 46/2015/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e3` Chính phủ `[CO_QUAN_THAM_QUYEN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e0` Nghị định số 46/2015/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e0` Nghị định số 46/2015/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e2` ngày 12 tháng 5 năm 2015 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #03_2021_TT-BGTVT_147344#preamble_context_6 (Loại: `preamble_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[03/2021/TT-BGTVT]`<SO_HIEU>`** của **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** . **[Căn cứ]`<TU_KHOA_PHAP_LY>`** **[Nghị định số 59/2015/NĐ-CP]`<THAM_CHIEU_PHAP_LY>`** **[ngày 18 tháng 6 năm 2015]`<NGAY_THAM_CHIEU>`** của **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** về quản lý dự án đầu tư xây dựng ;

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **03/2021/TT-BGTVT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[4:7]`)
- `[e3]` **Nghị định số 59/2015/NĐ-CP** → `THAM_CHIEU_PHAP_LY` (span: `[9:12]`)
- `[e4]` **Căn cứ** → `TU_KHOA_PHAP_LY` (span: `[8:9]`)
- `[e5]` **ngày 18 tháng 6 năm 2015** → `NGAY_THAM_CHIEU` (span: `[12:18]`)
- `[e6]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[19:20]`)

**Quan hệ:**
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e4` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Nghị định số 59/2015/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Nghị định số 59/2015/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e3` Nghị định số 59/2015/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e5` ngày 18 tháng 6 năm 2015 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #03_2021_TT-BGTVT_147344#preamble_standalone_7 (Loại: `preamble_standalone`)
> **[Căn cứ]`<TU_KHOA_PHAP_LY>`** **[Nghị định số 59/2015/NĐ-CP]`<THAM_CHIEU_PHAP_LY>`** **[ngày 18 tháng 6 năm 2015]`<NGAY_THAM_CHIEU>`** của **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** về quản lý dự án đầu tư xây dựng ;

**Thực thể:**
- `[e0]` **Nghị định số 59/2015/NĐ-CP** → `THAM_CHIEU_PHAP_LY` (span: `[1:4]`)
- `[e1]` **Căn cứ** → `TU_KHOA_PHAP_LY` (span: `[0:1]`)
- `[e2]` **ngày 18 tháng 6 năm 2015** → `NGAY_THAM_CHIEU` (span: `[4:10]`)
- `[e3]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[11:12]`)

**Quan hệ:**
- (`e1` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e0` Nghị định số 59/2015/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e3` Chính phủ `[CO_QUAN_THAM_QUYEN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e0` Nghị định số 59/2015/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e0` Nghị định số 59/2015/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e2` ngày 18 tháng 6 năm 2015 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #03_2021_TT-BGTVT_147344#preamble_context_8 (Loại: `preamble_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[03/2021/TT-BGTVT]`<SO_HIEU>`** của **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** . **[Căn cứ]`<TU_KHOA_PHAP_LY>`** **[Nghị định số 42/2017/NĐ-CP]`<THAM_CHIEU_PHAP_LY>`** **[ngày 05 tháng 4 năm 2017]`<NGAY_THAM_CHIEU>`** của **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** về **[sửa đổi , bổ sung]`<TU_KHOA_PHAP_LY>`** một số Điều **[Nghị định số 59/2015/NĐ-CP]`<THAM_CHIEU_PHAP_LY>`** **[ngày 18 tháng 6 năm 2015]`<NGAY_THAM_CHIEU>`** của **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** về quản lý dự án đầu tư xây dựng ;

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **03/2021/TT-BGTVT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[4:7]`)
- `[e3]` **Nghị định số 42/2017/NĐ-CP** → `THAM_CHIEU_PHAP_LY` (span: `[9:12]`)
- `[e4]` **Nghị định số 59/2015/NĐ-CP** → `THAM_CHIEU_PHAP_LY` (span: `[26:29]`)
- `[e5]` **Căn cứ** → `TU_KHOA_PHAP_LY` (span: `[8:9]`)
- `[e6]` **sửa đổi , bổ sung** → `TU_KHOA_PHAP_LY` (span: `[21:24]`)
- `[e7]` **ngày 05 tháng 4 năm 2017** → `NGAY_THAM_CHIEU` (span: `[12:18]`)
- `[e8]` **ngày 18 tháng 6 năm 2015** → `NGAY_THAM_CHIEU` (span: `[29:35]`)
- `[e9]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[19:20]`)
- `[e10]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[36:37]`)

**Quan hệ:**
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e5` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Nghị định số 42/2017/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Nghị định số 42/2017/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e6` sửa đổi , bổ sung `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e4` Nghị định số 59/2015/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e4` Nghị định số 59/2015/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e3` Nghị định số 42/2017/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e7` ngày 05 tháng 4 năm 2017 `[NGAY_THAM_CHIEU]`)
- (`e4` Nghị định số 59/2015/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e8` ngày 18 tháng 6 năm 2015 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #03_2021_TT-BGTVT_147344#preamble_standalone_9 (Loại: `preamble_standalone`)
> **[Căn cứ]`<TU_KHOA_PHAP_LY>`** **[Nghị định số 42/2017/NĐ-CP]`<THAM_CHIEU_PHAP_LY>`** **[ngày 05 tháng 4 năm 2017]`<NGAY_THAM_CHIEU>`** của **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** về **[sửa đổi , bổ sung]`<TU_KHOA_PHAP_LY>`** một số Điều **[Nghị định số 59/2015/NĐ-CP]`<THAM_CHIEU_PHAP_LY>`** **[ngày 18 tháng 6 năm 2015]`<NGAY_THAM_CHIEU>`** của **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** về quản lý dự án đầu tư xây dựng ;

**Thực thể:**
- `[e0]` **Nghị định số 42/2017/NĐ-CP** → `THAM_CHIEU_PHAP_LY` (span: `[1:4]`)
- `[e1]` **Nghị định số 59/2015/NĐ-CP** → `THAM_CHIEU_PHAP_LY` (span: `[18:21]`)
- `[e2]` **Căn cứ** → `TU_KHOA_PHAP_LY` (span: `[0:1]`)
- `[e3]` **sửa đổi , bổ sung** → `TU_KHOA_PHAP_LY` (span: `[13:16]`)
- `[e4]` **ngày 05 tháng 4 năm 2017** → `NGAY_THAM_CHIEU` (span: `[4:10]`)
- `[e5]` **ngày 18 tháng 6 năm 2015** → `NGAY_THAM_CHIEU` (span: `[21:27]`)
- `[e6]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[11:12]`)
- `[e7]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[28:29]`)

**Quan hệ:**
- (`e2` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e0` Nghị định số 42/2017/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e6` Chính phủ `[CO_QUAN_THAM_QUYEN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e0` Nghị định số 42/2017/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e3` sửa đổi , bổ sung `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e1` Nghị định số 59/2015/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e6` Chính phủ `[CO_QUAN_THAM_QUYEN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e1` Nghị định số 59/2015/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e0` Nghị định số 42/2017/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e4` ngày 05 tháng 4 năm 2017 `[NGAY_THAM_CHIEU]`)
- (`e1` Nghị định số 59/2015/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e5` ngày 18 tháng 6 năm 2015 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #03_2021_TT-BGTVT_147344#preamble_context_10 (Loại: `preamble_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[03/2021/TT-BGTVT]`<SO_HIEU>`** của **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** . **[Căn cứ]`<TU_KHOA_PHAP_LY>`** **[Nghị định số 32/2019/NĐ-CP]`<THAM_CHIEU_PHAP_LY>`** **[ngày 10 tháng 4 năm 2019]`<NGAY_THAM_CHIEU>`** của **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** quy định giao nhiệm vụ , đặt hàng hoặc đấu thầu cung cấp sản phẩm , dịch vụ công sử dụng **[ngân sách nhà nước]`<TAI_SAN_VAT_CHAT>`** từ nguồn kinh phí chi thường xuyên .

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **03/2021/TT-BGTVT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[4:7]`)
- `[e3]` **Nghị định số 32/2019/NĐ-CP** → `THAM_CHIEU_PHAP_LY` (span: `[9:12]`)
- `[e4]` **Căn cứ** → `TU_KHOA_PHAP_LY` (span: `[8:9]`)
- `[e5]` **ngày 10 tháng 4 năm 2019** → `NGAY_THAM_CHIEU` (span: `[12:18]`)
- `[e6]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[19:20]`)
- `[e7]` **ngân sách nhà nước** → `TAI_SAN_VAT_CHAT` (span: `[33:35]`)

**Quan hệ:**
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e4` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Nghị định số 32/2019/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Nghị định số 32/2019/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e3` Nghị định số 32/2019/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e5` ngày 10 tháng 4 năm 2019 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #03_2021_TT-BGTVT_147344#preamble_standalone_11 (Loại: `preamble_standalone`)
> **[Căn cứ]`<TU_KHOA_PHAP_LY>`** **[Nghị định số 32/2019/NĐ-CP]`<THAM_CHIEU_PHAP_LY>`** **[ngày 10 tháng 4 năm 2019]`<NGAY_THAM_CHIEU>`** của **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** quy định giao nhiệm vụ , đặt hàng hoặc đấu thầu cung cấp sản phẩm , dịch vụ công sử dụng **[ngân sách nhà nước]`<TAI_SAN_VAT_CHAT>`** từ nguồn kinh phí chi thường xuyên .

**Thực thể:**
- `[e0]` **Nghị định số 32/2019/NĐ-CP** → `THAM_CHIEU_PHAP_LY` (span: `[1:4]`)
- `[e1]` **Căn cứ** → `TU_KHOA_PHAP_LY` (span: `[0:1]`)
- `[e2]` **ngày 10 tháng 4 năm 2019** → `NGAY_THAM_CHIEU` (span: `[4:10]`)
- `[e3]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[11:12]`)
- `[e4]` **ngân sách nhà nước** → `TAI_SAN_VAT_CHAT` (span: `[25:27]`)

**Quan hệ:**
- (`e1` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e0` Nghị định số 32/2019/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e3` Chính phủ `[CO_QUAN_THAM_QUYEN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e0` Nghị định số 32/2019/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e0` Nghị định số 32/2019/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e2` ngày 10 tháng 4 năm 2019 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #03_2021_TT-BGTVT_147344#preamble_context_12 (Loại: `preamble_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[03/2021/TT-BGTVT]`<SO_HIEU>`** của **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** . **[Căn cứ]`<TU_KHOA_PHAP_LY>`** **[Nghị định số 12/2017/NĐ-CP]`<THAM_CHIEU_PHAP_LY>`** **[ngày 10 tháng 02 năm 2017]`<NGAY_THAM_CHIEU>`** của **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** quy định chức năng , nhiệm vụ , quyền hạn và cơ cấu tổ chức của **[Bộ Giao thông vận tải]`<CO_QUAN_THAM_QUYEN>`** ;

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **03/2021/TT-BGTVT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[4:7]`)
- `[e3]` **Nghị định số 12/2017/NĐ-CP** → `THAM_CHIEU_PHAP_LY` (span: `[9:12]`)
- `[e4]` **Căn cứ** → `TU_KHOA_PHAP_LY` (span: `[8:9]`)
- `[e5]` **ngày 10 tháng 02 năm 2017** → `NGAY_THAM_CHIEU` (span: `[12:18]`)
- `[e6]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[19:20]`)
- `[e7]` **Bộ Giao thông vận tải** → `CO_QUAN_THAM_QUYEN` (span: `[30:33]`)

**Quan hệ:**
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e4` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Nghị định số 12/2017/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Nghị định số 12/2017/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e3` Nghị định số 12/2017/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e5` ngày 10 tháng 02 năm 2017 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #03_2021_TT-BGTVT_147344#preamble_standalone_13 (Loại: `preamble_standalone`)
> **[Căn cứ]`<TU_KHOA_PHAP_LY>`** **[Nghị định số 12/2017/NĐ-CP]`<THAM_CHIEU_PHAP_LY>`** **[ngày 10 tháng 02 năm 2017]`<NGAY_THAM_CHIEU>`** của **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** quy định chức năng , nhiệm vụ , quyền hạn và cơ cấu tổ chức của **[Bộ Giao thông vận tải]`<CO_QUAN_THAM_QUYEN>`** ;

**Thực thể:**
- `[e0]` **Nghị định số 12/2017/NĐ-CP** → `THAM_CHIEU_PHAP_LY` (span: `[1:4]`)
- `[e1]` **Căn cứ** → `TU_KHOA_PHAP_LY` (span: `[0:1]`)
- `[e2]` **ngày 10 tháng 02 năm 2017** → `NGAY_THAM_CHIEU` (span: `[4:10]`)
- `[e3]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[11:12]`)
- `[e4]` **Bộ Giao thông vận tải** → `CO_QUAN_THAM_QUYEN` (span: `[22:25]`)

**Quan hệ:**
- (`e1` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e0` Nghị định số 12/2017/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e3` Chính phủ `[CO_QUAN_THAM_QUYEN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e0` Nghị định số 12/2017/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e0` Nghị định số 12/2017/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e2` ngày 10 tháng 02 năm 2017 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #03_2021_TT-BGTVT_147344#body_context_14 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[03/2021/TT-BGTVT]`<SO_HIEU>`** ban hành **[ngày 08 tháng 02 năm 2021]`<NGAY_BAN_HANH>`** bởi **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** . **[Chương I. QUY ĐỊNH CHUNG]`<CHUONG>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **03/2021/TT-BGTVT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[11:14]`)
- `[e3]` **ngày 08 tháng 02 năm 2021** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Chương I. QUY ĐỊNH CHUNG** → `CHUONG` (span: `[15:19]`)

**Quan hệ:**
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 08 tháng 02 năm 2021 `[NGAY_BAN_HANH]`)
- (`e4` Chương I. QUY ĐỊNH CHUNG `[CHUONG]`) ==[ **THUOC_VE** ]==> (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`)


---

### Mẫu #03_2021_TT-BGTVT_147344#body_context_15 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[03/2021/TT-BGTVT]`<SO_HIEU>`** ban hành **[ngày 08 tháng 02 năm 2021]`<NGAY_BAN_HANH>`** bởi **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** . **[Điều 1]`<DIEU>`** . **[2 . Đối với công tác cứu chữa , khắc phục hậu quả bão lũ , thực hiện theo quy định của **[Bộ Giao thông vận tải]`<CO_QUAN_THAM_QUYEN>`** về phòng , chống , khắc phục hậu quả lụt , bão , ứng phó sự cố thiên tai và cứu nạn trong hoạt động đường sắt .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **03/2021/TT-BGTVT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[11:14]`)
- `[e3]` **ngày 08 tháng 02 năm 2021** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 1** → `DIEU` (span: `[15:17]`)
- `[e5]` **2 . Đối với công tác cứu chữa , khắc phục hậu quả bão lũ , thực hiện theo quy định của Bộ Giao thông vận tải về phòng , chống , khắc phục hậu quả lụt , bão , ứng phó sự cố thiên tai và cứu nạn trong hoạt động đường sắt .** → `KHOAN` (span: `[18:57]`)
- `[e6]` **Bộ Giao thông vận tải** → `CO_QUAN_THAM_QUYEN` (span: `[33:36]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 08 tháng 02 năm 2021 `[NGAY_BAN_HANH]`)
- (`e4` Điều 1 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`)
- (`e5` 2 . Đối với công tác cứu chữa , khắc phục hậu quả bão lũ , thực hiện theo quy định của Bộ Giao thông vận tải về phòng , chống , khắc phục hậu quả lụt , bão , ứng phó sự cố thiên tai và cứu nạn trong hoạt động đường sắt . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 1 `[DIEU]`)


---

### Mẫu #03_2021_TT-BGTVT_147344#body_context_16 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[03/2021/TT-BGTVT]`<SO_HIEU>`** ban hành **[ngày 08 tháng 02 năm 2021]`<NGAY_BAN_HANH>`** bởi **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** . **[Điều 3]`<DIEU>`** . **[6 . Bảo dưỡng công trình đường sắt là hoạt động theo dõi , chăm sóc , sửa chữa những hư hỏng nhỏ của công trình và thiết bị lắp đặt vào công trình , được tiến hành thường xuyên , định kỳ để duy trì công trình ở trạng thái khai thác , sử dụng bình thường và hạn chế phát sinh các hư hỏng công trình .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **03/2021/TT-BGTVT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[11:14]`)
- `[e3]` **ngày 08 tháng 02 năm 2021** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 3** → `DIEU` (span: `[15:17]`)
- `[e5]` **6 . Bảo dưỡng công trình đường sắt là hoạt động theo dõi , chăm sóc , sửa chữa những hư hỏng nhỏ của công trình và thiết bị lắp đặt vào công trình , được tiến hành thường xuyên , định kỳ để duy trì công trình ở trạng thái khai thác , sử dụng bình thường và hạn chế phát sinh các hư hỏng công trình .** → `KHOAN` (span: `[18:62]`)

**Quan hệ:**
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 08 tháng 02 năm 2021 `[NGAY_BAN_HANH]`)
- (`e4` Điều 3 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`)
- (`e5` 6 . Bảo dưỡng công trình đường sắt là hoạt động theo dõi , chăm sóc , sửa chữa những hư hỏng nhỏ của công trình và thiết bị lắp đặt vào công trình , được tiến hành thường xuyên , định kỳ để duy trì công trình ở trạng thái khai thác , sử dụng bình thường và hạn chế phát sinh các hư hỏng công trình . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 3 `[DIEU]`)


---

### Mẫu #03_2021_TT-BGTVT_147344#body_context_17 (Loại: `body_context`)
> **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[03/2021/TT-BGTVT]`<SO_HIEU>`** . **[Điều 3]`<DIEU>`** . **[8 . Nhà cung cấp dịch vụ sự nghiệp công sử dụng kinh phí **[ngân sách nhà nước]`<TAI_SAN_VAT_CHAT>`** là **[doanh nghiệp]`<TO_CHUC_DOANH_NGHIEP>`** , tổ chức thực hiện một hoặc một số nhiệm vụ quản lý , bảo trì kết cấu hạ tầng đường sắt theo hợp đồng đặt hàng với **[cơ quan nhà nước có thẩm quyền]`<CO_QUAN_THAM_QUYEN>`** .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[4:5]`)
- `[e1]` **03/2021/TT-BGTVT** → `SO_HIEU` (span: `[6:7]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[0:3]`)
- `[e3]` **Điều 3** → `DIEU` (span: `[8:10]`)
- `[e4]` **8 . Nhà cung cấp dịch vụ sự nghiệp công sử dụng kinh phí ngân sách nhà nước là doanh nghiệp , tổ chức thực hiện một hoặc một số nhiệm vụ quản lý , bảo trì kết cấu hạ tầng đường sắt theo hợp đồng đặt hàng với cơ quan nhà nước có thẩm quyền .** → `KHOAN` (span: `[11:45]`)
- `[e5]` **cơ quan nhà nước có thẩm quyền** → `CO_QUAN_THAM_QUYEN` (span: `[40:44]`) *(lồng trong `e4` (`KHOAN`))*
- `[e6]` **doanh nghiệp** → `TO_CHUC_DOANH_NGHIEP` (span: `[23:24]`) *(lồng trong `e4` (`KHOAN`))*
- `[e7]` **ngân sách nhà nước** → `TAI_SAN_VAT_CHAT` (span: `[20:22]`) *(lồng trong `e4` (`KHOAN`))*

**Quan hệ:**
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 3 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`)
- (`e4` 8 . Nhà cung cấp dịch vụ sự nghiệp công sử dụng kinh phí ngân sách nhà nước là doanh nghiệp , tổ chức thực hiện một hoặc một số nhiệm vụ quản lý , bảo trì kết cấu hạ tầng đường sắt theo hợp đồng đặt hàng với cơ quan nhà nước có thẩm quyền . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 3 `[DIEU]`)


---

### Mẫu #03_2021_TT-BGTVT_147344#body_standalone_18 (Loại: `body_standalone`)
> **[Điều 3]`<DIEU>`** . **[8 . Nhà cung cấp dịch vụ sự nghiệp công sử dụng kinh phí **[ngân sách nhà nước]`<TAI_SAN_VAT_CHAT>`** là **[doanh nghiệp]`<TO_CHUC_DOANH_NGHIEP>`** , tổ chức thực hiện một hoặc một số nhiệm vụ quản lý , bảo trì kết cấu hạ tầng đường sắt theo hợp đồng đặt hàng với **[cơ quan nhà nước có thẩm quyền]`<CO_QUAN_THAM_QUYEN>`** .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 3** → `DIEU` (span: `[0:2]`)
- `[e1]` **8 . Nhà cung cấp dịch vụ sự nghiệp công sử dụng kinh phí ngân sách nhà nước là doanh nghiệp , tổ chức thực hiện một hoặc một số nhiệm vụ quản lý , bảo trì kết cấu hạ tầng đường sắt theo hợp đồng đặt hàng với cơ quan nhà nước có thẩm quyền .** → `KHOAN` (span: `[3:37]`)
- `[e2]` **cơ quan nhà nước có thẩm quyền** → `CO_QUAN_THAM_QUYEN` (span: `[32:36]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **doanh nghiệp** → `TO_CHUC_DOANH_NGHIEP` (span: `[15:16]`) *(lồng trong `e1` (`KHOAN`))*
- `[e4]` **ngân sách nhà nước** → `TAI_SAN_VAT_CHAT` (span: `[12:14]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 8 . Nhà cung cấp dịch vụ sự nghiệp công sử dụng kinh phí ngân sách nhà nước là doanh nghiệp , tổ chức thực hiện một hoặc một số nhiệm vụ quản lý , bảo trì kết cấu hạ tầng đường sắt theo hợp đồng đặt hàng với cơ quan nhà nước có thẩm quyền . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 3 `[DIEU]`)


---

### Mẫu #03_2021_TT-BGTVT_147344#body_context_19 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[03/2021/TT-BGTVT]`<SO_HIEU>`** ban hành **[ngày 08 tháng 02 năm 2021]`<NGAY_BAN_HANH>`** bởi **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** . **[Điều 3]`<DIEU>`** . **[9 . **[Doanh nghiệp kinh doanh kết cấu hạ tầng đường sắt quốc gia]`<TO_CHUC_DOANH_NGHIEP>`** là đơn vị được nhà nước giao , cho thuê hoặc chuyển nhượng kết cấu hạ tầng đường sắt quốc gia theo quy định của pháp luật .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **03/2021/TT-BGTVT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[11:14]`)
- `[e3]` **ngày 08 tháng 02 năm 2021** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 3** → `DIEU` (span: `[15:17]`)
- `[e5]` **9 . Doanh nghiệp kinh doanh kết cấu hạ tầng đường sắt quốc gia là đơn vị được nhà nước giao , cho thuê hoặc chuyển nhượng kết cấu hạ tầng đường sắt quốc gia theo quy định của pháp luật .** → `KHOAN` (span: `[18:43]`)
- `[e6]` **Doanh nghiệp kinh doanh kết cấu hạ tầng đường sắt quốc gia** → `TO_CHUC_DOANH_NGHIEP` (span: `[20:25]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 08 tháng 02 năm 2021 `[NGAY_BAN_HANH]`)
- (`e4` Điều 3 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`)
- (`e5` 9 . Doanh nghiệp kinh doanh kết cấu hạ tầng đường sắt quốc gia là đơn vị được nhà nước giao , cho thuê hoặc chuyển nhượng kết cấu hạ tầng đường sắt quốc gia theo quy định của pháp luật . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 3 `[DIEU]`)


---

### Mẫu #03_2021_TT-BGTVT_147344#body_standalone_20 (Loại: `body_standalone`)
> **[Điều 3]`<DIEU>`** . **[9 . **[Doanh nghiệp kinh doanh kết cấu hạ tầng đường sắt quốc gia]`<TO_CHUC_DOANH_NGHIEP>`** là đơn vị được nhà nước giao , cho thuê hoặc chuyển nhượng kết cấu hạ tầng đường sắt quốc gia theo quy định của pháp luật .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 3** → `DIEU` (span: `[0:2]`)
- `[e1]` **9 . Doanh nghiệp kinh doanh kết cấu hạ tầng đường sắt quốc gia là đơn vị được nhà nước giao , cho thuê hoặc chuyển nhượng kết cấu hạ tầng đường sắt quốc gia theo quy định của pháp luật .** → `KHOAN` (span: `[3:28]`)
- `[e2]` **Doanh nghiệp kinh doanh kết cấu hạ tầng đường sắt quốc gia** → `TO_CHUC_DOANH_NGHIEP` (span: `[5:10]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 9 . Doanh nghiệp kinh doanh kết cấu hạ tầng đường sắt quốc gia là đơn vị được nhà nước giao , cho thuê hoặc chuyển nhượng kết cấu hạ tầng đường sắt quốc gia theo quy định của pháp luật . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 3 `[DIEU]`)


---

### Mẫu #03_2021_TT-BGTVT_147344#body_context_21 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[03/2021/TT-BGTVT]`<SO_HIEU>`** của **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Đường sắt]`<LINH_VUC>`** . **[Điều 5]`<DIEU>`** . **[1 . Quản lý **[tài sản kết cấu hạ tầng]`<TAI_SAN_VAT_CHAT>`** đường sắt theo quy định của pháp luật .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **03/2021/TT-BGTVT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[4:7]`)
- `[e3]` **Đường sắt** → `LINH_VUC` (span: `[9:10]`)
- `[e4]` **Điều 5** → `DIEU` (span: `[11:13]`)
- `[e5]` **1 . Quản lý tài sản kết cấu hạ tầng đường sắt theo quy định của pháp luật .** → `KHOAN` (span: `[14:25]`)
- `[e6]` **tài sản kết cấu hạ tầng** → `TAI_SAN_VAT_CHAT` (span: `[17:19]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Đường sắt `[LINH_VUC]`)
- (`e4` Điều 5 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`)
- (`e5` 1 . Quản lý tài sản kết cấu hạ tầng đường sắt theo quy định của pháp luật . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 5 `[DIEU]`)
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Đường sắt `[LINH_VUC]`)
- (`e5` 1 . Quản lý tài sản kết cấu hạ tầng đường sắt theo quy định của pháp luật . `[KHOAN]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Đường sắt `[LINH_VUC]`)


---

### Mẫu #03_2021_TT-BGTVT_147344#body_context_22 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[03/2021/TT-BGTVT]`<SO_HIEU>`** ban hành **[ngày 08 tháng 02 năm 2021]`<NGAY_BAN_HANH>`** bởi **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** . **[Điều 5]`<DIEU>`** . **[8 . Cập nhật hồ sơ quản lý kết cấu hạ tầng đường sắt vào hệ thống cơ sở dữ liệu để theo dõi , quản lý ; thành phần và nội dung hồ sơ **[theo quy định tại]`<TU_KHOA_PHAP_LY>`** **[Điều 6 của Thông tư này]`<THAM_CHIEU_PHAP_LY>`** .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **03/2021/TT-BGTVT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[11:14]`)
- `[e3]` **ngày 08 tháng 02 năm 2021** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 5** → `DIEU` (span: `[15:17]`)
- `[e5]` **8 . Cập nhật hồ sơ quản lý kết cấu hạ tầng đường sắt vào hệ thống cơ sở dữ liệu để theo dõi , quản lý ; thành phần và nội dung hồ sơ theo quy định tại Điều 6 của Thông tư này .** → `KHOAN` (span: `[18:47]`)
- `[e6]` **Điều 6 của Thông tư này** → `THAM_CHIEU_PHAP_LY` (span: `[41:46]`) *(lồng trong `e5` (`KHOAN`))*
- `[e7]` **theo quy định tại** → `TU_KHOA_PHAP_LY` (span: `[38:41]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 08 tháng 02 năm 2021 `[NGAY_BAN_HANH]`)
- (`e4` Điều 5 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`)
- (`e5` 8 . Cập nhật hồ sơ quản lý kết cấu hạ tầng đường sắt vào hệ thống cơ sở dữ liệu để theo dõi , quản lý ; thành phần và nội dung hồ sơ theo quy định tại Điều 6 của Thông tư này . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 5 `[DIEU]`)
- (`e7` theo quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e6` Điều 6 của Thông tư này `[THAM_CHIEU_PHAP_LY]`)
- (`e5` 8 . Cập nhật hồ sơ quản lý kết cấu hạ tầng đường sắt vào hệ thống cơ sở dữ liệu để theo dõi , quản lý ; thành phần và nội dung hồ sơ theo quy định tại Điều 6 của Thông tư này . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e6` Điều 6 của Thông tư này `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #03_2021_TT-BGTVT_147344#body_standalone_23 (Loại: `body_standalone`)
> **[Điều 5]`<DIEU>`** . **[8 . Cập nhật hồ sơ quản lý kết cấu hạ tầng đường sắt vào hệ thống cơ sở dữ liệu để theo dõi , quản lý ; thành phần và nội dung hồ sơ **[theo quy định tại]`<TU_KHOA_PHAP_LY>`** **[Điều 6 của Thông tư này]`<THAM_CHIEU_PHAP_LY>`** .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 5** → `DIEU` (span: `[0:2]`)
- `[e1]` **8 . Cập nhật hồ sơ quản lý kết cấu hạ tầng đường sắt vào hệ thống cơ sở dữ liệu để theo dõi , quản lý ; thành phần và nội dung hồ sơ theo quy định tại Điều 6 của Thông tư này .** → `KHOAN` (span: `[3:32]`)
- `[e2]` **Điều 6 của Thông tư này** → `THAM_CHIEU_PHAP_LY` (span: `[26:31]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **theo quy định tại** → `TU_KHOA_PHAP_LY` (span: `[23:26]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 8 . Cập nhật hồ sơ quản lý kết cấu hạ tầng đường sắt vào hệ thống cơ sở dữ liệu để theo dõi , quản lý ; thành phần và nội dung hồ sơ theo quy định tại Điều 6 của Thông tư này . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 5 `[DIEU]`)
- (`e3` theo quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e2` Điều 6 của Thông tư này `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 8 . Cập nhật hồ sơ quản lý kết cấu hạ tầng đường sắt vào hệ thống cơ sở dữ liệu để theo dõi , quản lý ; thành phần và nội dung hồ sơ theo quy định tại Điều 6 của Thông tư này . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e2` Điều 6 của Thông tư này `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #03_2021_TT-BGTVT_147344#body_context_24 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[03/2021/TT-BGTVT]`<SO_HIEU>`** ban hành **[ngày 08 tháng 02 năm 2021]`<NGAY_BAN_HANH>`** bởi **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** . **[Chương II]`<CHUONG>`** . **[Điều 6 . Hồ sơ quản lý kết cấu hạ tầng đường sắt]`<DIEU>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **03/2021/TT-BGTVT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[11:14]`)
- `[e3]` **ngày 08 tháng 02 năm 2021** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Chương II** → `CHUONG` (span: `[15:17]`)
- `[e5]` **Điều 6 . Hồ sơ quản lý kết cấu hạ tầng đường sắt** → `DIEU` (span: `[18:25]`)

**Quan hệ:**
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 08 tháng 02 năm 2021 `[NGAY_BAN_HANH]`)
- (`e4` Chương II `[CHUONG]`) ==[ **THUOC_VE** ]==> (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`)
- (`e5` Điều 6 . Hồ sơ quản lý kết cấu hạ tầng đường sắt `[DIEU]`) ==[ **THUOC_VE** ]==> (`e4` Chương II `[CHUONG]`)


---

### Mẫu #03_2021_TT-BGTVT_147344#body_context_25 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[03/2021/TT-BGTVT]`<SO_HIEU>`** ban hành **[ngày 08 tháng 02 năm 2021]`<NGAY_BAN_HANH>`** bởi **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** . **[Điều 6]`<DIEU>`** . **[2 . Hồ sơ quản lý kỹ thuật công trình được lập cho từng công trình , hạng Mục công trình theo từng tuyến đường sắt và theo từng phạm vi quản lý ( khu gian , khu đoạn ) . Hồ sơ quản lý kỹ thuật công trình đường sắt bao gồm : hồ sơ phục vụ quản lý , vận hành , bảo trì công trình theo đúng **[quy định tại]`<TU_KHOA_PHAP_LY>`** **[Khoản 3 Điều 12]`<THAM_CHIEU_PHAP_LY>`** của Thông tư 26/2016/TT-BXD **[ngày 26 tháng 10 năm 2016]`<NGAY_THAM_CHIEU>`** của **[Bộ Xây Dựng]`<CO_QUAN_THAM_QUYEN>`** ; hồ sơ hoàn thành bảo trì công trình và các]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **03/2021/TT-BGTVT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[11:14]`)
- `[e3]` **ngày 08 tháng 02 năm 2021** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 6** → `DIEU` (span: `[15:17]`)
- `[e5]` **2 . Hồ sơ quản lý kỹ thuật công trình được lập cho từng công trình , hạng Mục công trình theo từng tuyến đường sắt và theo từng phạm vi quản lý ( khu gian , khu đoạn ) . Hồ sơ quản lý kỹ thuật công trình đường sắt bao gồm : hồ sơ phục vụ quản lý , vận hành , bảo trì công trình theo đúng quy định tại Khoản 3 Điều 12 của Thông tư 26/2016/TT-BXD ngày 26 tháng 10 năm 2016 của Bộ Xây Dựng ; hồ sơ hoàn thành bảo trì công trình và các** → `KHOAN` (span: `[18:92]`)
- `[e6]` **Khoản 3 Điều 12** → `THAM_CHIEU_PHAP_LY` (span: `[69:73]`) *(lồng trong `e5` (`KHOAN`))*
- `[e7]` **quy định tại** → `TU_KHOA_PHAP_LY` (span: `[67:69]`) *(lồng trong `e5` (`KHOAN`))*
- `[e8]` **ngày 26 tháng 10 năm 2016** → `NGAY_THAM_CHIEU` (span: `[76:82]`) *(lồng trong `e5` (`KHOAN`))*
- `[e9]` **Bộ Xây Dựng** → `CO_QUAN_THAM_QUYEN` (span: `[83:85]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 08 tháng 02 năm 2021 `[NGAY_BAN_HANH]`)
- (`e4` Điều 6 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`)
- (`e5` 2 . Hồ sơ quản lý kỹ thuật công trình được lập cho từng công trình , hạng Mục công trình theo từng tuyến đường sắt và theo từng phạm vi quản lý ( khu gian , khu đoạn ) . Hồ sơ quản lý kỹ thuật công trình đường sắt bao gồm : hồ sơ phục vụ quản lý , vận hành , bảo trì công trình theo đúng quy định tại Khoản 3 Điều 12 của Thông tư 26/2016/TT-BXD ngày 26 tháng 10 năm 2016 của Bộ Xây Dựng ; hồ sơ hoàn thành bảo trì công trình và các `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 6 `[DIEU]`)
- (`e7` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e6` Khoản 3 Điều 12 `[THAM_CHIEU_PHAP_LY]`)
- (`e5` 2 . Hồ sơ quản lý kỹ thuật công trình được lập cho từng công trình , hạng Mục công trình theo từng tuyến đường sắt và theo từng phạm vi quản lý ( khu gian , khu đoạn ) . Hồ sơ quản lý kỹ thuật công trình đường sắt bao gồm : hồ sơ phục vụ quản lý , vận hành , bảo trì công trình theo đúng quy định tại Khoản 3 Điều 12 của Thông tư 26/2016/TT-BXD ngày 26 tháng 10 năm 2016 của Bộ Xây Dựng ; hồ sơ hoàn thành bảo trì công trình và các `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e6` Khoản 3 Điều 12 `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e6` Khoản 3 Điều 12 `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e8` ngày 26 tháng 10 năm 2016 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #03_2021_TT-BGTVT_147344#body_standalone_26 (Loại: `body_standalone`)
> **[Điều 6]`<DIEU>`** . **[2 . Hồ sơ quản lý kỹ thuật công trình được lập cho từng công trình , hạng Mục công trình theo từng tuyến đường sắt và theo từng phạm vi quản lý ( khu gian , khu đoạn ) . Hồ sơ quản lý kỹ thuật công trình đường sắt bao gồm : hồ sơ phục vụ quản lý , vận hành , bảo trì công trình theo đúng **[quy định tại]`<TU_KHOA_PHAP_LY>`** **[Khoản 3 Điều 12]`<THAM_CHIEU_PHAP_LY>`** của Thông tư 26/2016/TT-BXD **[ngày 26 tháng 10 năm 2016]`<NGAY_THAM_CHIEU>`** của **[Bộ Xây Dựng]`<CO_QUAN_THAM_QUYEN>`** ; hồ sơ hoàn thành bảo trì công trình và các]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 6** → `DIEU` (span: `[0:2]`)
- `[e1]` **2 . Hồ sơ quản lý kỹ thuật công trình được lập cho từng công trình , hạng Mục công trình theo từng tuyến đường sắt và theo từng phạm vi quản lý ( khu gian , khu đoạn ) . Hồ sơ quản lý kỹ thuật công trình đường sắt bao gồm : hồ sơ phục vụ quản lý , vận hành , bảo trì công trình theo đúng quy định tại Khoản 3 Điều 12 của Thông tư 26/2016/TT-BXD ngày 26 tháng 10 năm 2016 của Bộ Xây Dựng ; hồ sơ hoàn thành bảo trì công trình và các** → `KHOAN` (span: `[3:77]`)
- `[e2]` **Khoản 3 Điều 12** → `THAM_CHIEU_PHAP_LY` (span: `[54:58]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **quy định tại** → `TU_KHOA_PHAP_LY` (span: `[52:54]`) *(lồng trong `e1` (`KHOAN`))*
- `[e4]` **ngày 26 tháng 10 năm 2016** → `NGAY_THAM_CHIEU` (span: `[61:67]`) *(lồng trong `e1` (`KHOAN`))*
- `[e5]` **Bộ Xây Dựng** → `CO_QUAN_THAM_QUYEN` (span: `[68:70]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 2 . Hồ sơ quản lý kỹ thuật công trình được lập cho từng công trình , hạng Mục công trình theo từng tuyến đường sắt và theo từng phạm vi quản lý ( khu gian , khu đoạn ) . Hồ sơ quản lý kỹ thuật công trình đường sắt bao gồm : hồ sơ phục vụ quản lý , vận hành , bảo trì công trình theo đúng quy định tại Khoản 3 Điều 12 của Thông tư 26/2016/TT-BXD ngày 26 tháng 10 năm 2016 của Bộ Xây Dựng ; hồ sơ hoàn thành bảo trì công trình và các `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 6 `[DIEU]`)
- (`e3` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e2` Khoản 3 Điều 12 `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 2 . Hồ sơ quản lý kỹ thuật công trình được lập cho từng công trình , hạng Mục công trình theo từng tuyến đường sắt và theo từng phạm vi quản lý ( khu gian , khu đoạn ) . Hồ sơ quản lý kỹ thuật công trình đường sắt bao gồm : hồ sơ phục vụ quản lý , vận hành , bảo trì công trình theo đúng quy định tại Khoản 3 Điều 12 của Thông tư 26/2016/TT-BXD ngày 26 tháng 10 năm 2016 của Bộ Xây Dựng ; hồ sơ hoàn thành bảo trì công trình và các `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e2` Khoản 3 Điều 12 `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e2` Khoản 3 Điều 12 `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e4` ngày 26 tháng 10 năm 2016 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #03_2021_TT-BGTVT_147344#body_context_27 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[03/2021/TT-BGTVT]`<SO_HIEU>`** ban hành **[ngày 08 tháng 02 năm 2021]`<NGAY_BAN_HANH>`** bởi **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** . **[Điều 6]`<DIEU>`** . **[Khoản 2]`<KHOAN>`** . **[a ) Hồ sơ quản lý , vận hành , bảo trì công trình đường sắt : **[Quyết định phê duyệt]`<GIAY_TO_HO_SO>`** dự án đầu tư xây dựng công trình và **[báo cáo nghiên cứu khả thi]`<GIAY_TO_HO_SO>`** đầu tư xây dựng hoặc **[báo cáo kinh tế - kỹ thuật]`<GIAY_TO_HO_SO>`** đầu tư xây dựng ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **03/2021/TT-BGTVT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[11:14]`)
- `[e3]` **ngày 08 tháng 02 năm 2021** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 6** → `DIEU` (span: `[15:17]`)
- `[e5]` **Khoản 2** → `KHOAN` (span: `[18:20]`)
- `[e6]` **a ) Hồ sơ quản lý , vận hành , bảo trì công trình đường sắt : Quyết định phê duyệt dự án đầu tư xây dựng công trình và báo cáo nghiên cứu khả thi đầu tư xây dựng hoặc báo cáo kinh tế - kỹ thuật đầu tư xây dựng ;** → `DIEM` (span: `[21:52]`)
- `[e7]` **Quyết định phê duyệt** → `GIAY_TO_HO_SO` (span: `[32:34]`) *(lồng trong `e6` (`DIEM`))*
- `[e8]` **báo cáo nghiên cứu khả thi** → `GIAY_TO_HO_SO` (span: `[39:42]`) *(lồng trong `e6` (`DIEM`))*
- `[e9]` **báo cáo kinh tế - kỹ thuật** → `GIAY_TO_HO_SO` (span: `[45:49]`) *(lồng trong `e6` (`DIEM`))*

**Quan hệ:**
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 08 tháng 02 năm 2021 `[NGAY_BAN_HANH]`)
- (`e4` Điều 6 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`)
- (`e5` Khoản 2 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 6 `[DIEU]`)
- (`e6` a ) Hồ sơ quản lý , vận hành , bảo trì công trình đường sắt : Quyết định phê duyệt dự án đầu tư xây dựng công trình và báo cáo nghiên cứu khả thi đầu tư xây dựng hoặc báo cáo kinh tế - kỹ thuật đầu tư xây dựng ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e5` Khoản 2 `[KHOAN]`)


---

### Mẫu #03_2021_TT-BGTVT_147344#body_standalone_28 (Loại: `body_standalone`)
> **[Điều 6]`<DIEU>`** . **[Khoản 2]`<KHOAN>`** . **[a ) Hồ sơ quản lý , vận hành , bảo trì công trình đường sắt : **[Quyết định phê duyệt]`<GIAY_TO_HO_SO>`** dự án đầu tư xây dựng công trình và **[báo cáo nghiên cứu khả thi]`<GIAY_TO_HO_SO>`** đầu tư xây dựng hoặc **[báo cáo kinh tế - kỹ thuật]`<GIAY_TO_HO_SO>`** đầu tư xây dựng ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Điều 6** → `DIEU` (span: `[0:2]`)
- `[e1]` **Khoản 2** → `KHOAN` (span: `[3:5]`)
- `[e2]` **a ) Hồ sơ quản lý , vận hành , bảo trì công trình đường sắt : Quyết định phê duyệt dự án đầu tư xây dựng công trình và báo cáo nghiên cứu khả thi đầu tư xây dựng hoặc báo cáo kinh tế - kỹ thuật đầu tư xây dựng ;** → `DIEM` (span: `[6:37]`)
- `[e3]` **Quyết định phê duyệt** → `GIAY_TO_HO_SO` (span: `[17:19]`) *(lồng trong `e2` (`DIEM`))*
- `[e4]` **báo cáo nghiên cứu khả thi** → `GIAY_TO_HO_SO` (span: `[24:27]`) *(lồng trong `e2` (`DIEM`))*
- `[e5]` **báo cáo kinh tế - kỹ thuật** → `GIAY_TO_HO_SO` (span: `[30:34]`) *(lồng trong `e2` (`DIEM`))*

**Quan hệ:**
- (`e1` Khoản 2 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 6 `[DIEU]`)
- (`e2` a ) Hồ sơ quản lý , vận hành , bảo trì công trình đường sắt : Quyết định phê duyệt dự án đầu tư xây dựng công trình và báo cáo nghiên cứu khả thi đầu tư xây dựng hoặc báo cáo kinh tế - kỹ thuật đầu tư xây dựng ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e1` Khoản 2 `[KHOAN]`)


---

### Mẫu #03_2021_TT-BGTVT_147344#body_context_29 (Loại: `body_context`)
> **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[03/2021/TT-BGTVT]`<SO_HIEU>`** . **[Điều 6]`<DIEU>`** . **[Khoản 2]`<KHOAN>`** . **[a ) Hồ sơ quản lý , vận hành , bảo trì công trình đường sắt : **[Hồ sơ thiết kế bản vẽ thi công]`<GIAY_TO_HO_SO>`** đã được **[chủ đầu tư]`<CHU_THE_CA_NHAN>`** xác nhận ( có danh Mục bản vẽ kèm theo ) và các thay đổi thiết kế trong quá trình thi công ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[4:5]`)
- `[e1]` **03/2021/TT-BGTVT** → `SO_HIEU` (span: `[6:7]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[0:3]`)
- `[e3]` **Điều 6** → `DIEU` (span: `[8:10]`)
- `[e4]` **Khoản 2** → `KHOAN` (span: `[11:13]`)
- `[e5]` **a ) Hồ sơ quản lý , vận hành , bảo trì công trình đường sắt : Hồ sơ thiết kế bản vẽ thi công đã được chủ đầu tư xác nhận ( có danh Mục bản vẽ kèm theo ) và các thay đổi thiết kế trong quá trình thi công ;** → `DIEM` (span: `[14:50]`)
- `[e6]` **Hồ sơ thiết kế bản vẽ thi công** → `GIAY_TO_HO_SO` (span: `[25:29]`) *(lồng trong `e5` (`DIEM`))*
- `[e7]` **chủ đầu tư** → `CHU_THE_CA_NHAN` (span: `[31:33]`) *(lồng trong `e5` (`DIEM`))*

**Quan hệ:**
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 6 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`)
- (`e4` Khoản 2 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 6 `[DIEU]`)
- (`e5` a ) Hồ sơ quản lý , vận hành , bảo trì công trình đường sắt : Hồ sơ thiết kế bản vẽ thi công đã được chủ đầu tư xác nhận ( có danh Mục bản vẽ kèm theo ) và các thay đổi thiết kế trong quá trình thi công ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e4` Khoản 2 `[KHOAN]`)


---

### Mẫu #03_2021_TT-BGTVT_147344#body_standalone_30 (Loại: `body_standalone`)
> **[Điều 6]`<DIEU>`** . **[Khoản 2]`<KHOAN>`** . **[a ) Hồ sơ quản lý , vận hành , bảo trì công trình đường sắt : **[Hồ sơ thiết kế bản vẽ thi công]`<GIAY_TO_HO_SO>`** đã được **[chủ đầu tư]`<CHU_THE_CA_NHAN>`** xác nhận ( có danh Mục bản vẽ kèm theo ) và các thay đổi thiết kế trong quá trình thi công ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Điều 6** → `DIEU` (span: `[0:2]`)
- `[e1]` **Khoản 2** → `KHOAN` (span: `[3:5]`)
- `[e2]` **a ) Hồ sơ quản lý , vận hành , bảo trì công trình đường sắt : Hồ sơ thiết kế bản vẽ thi công đã được chủ đầu tư xác nhận ( có danh Mục bản vẽ kèm theo ) và các thay đổi thiết kế trong quá trình thi công ;** → `DIEM` (span: `[6:42]`)
- `[e3]` **Hồ sơ thiết kế bản vẽ thi công** → `GIAY_TO_HO_SO` (span: `[17:21]`) *(lồng trong `e2` (`DIEM`))*
- `[e4]` **chủ đầu tư** → `CHU_THE_CA_NHAN` (span: `[23:25]`) *(lồng trong `e2` (`DIEM`))*

**Quan hệ:**
- (`e1` Khoản 2 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 6 `[DIEU]`)
- (`e2` a ) Hồ sơ quản lý , vận hành , bảo trì công trình đường sắt : Hồ sơ thiết kế bản vẽ thi công đã được chủ đầu tư xác nhận ( có danh Mục bản vẽ kèm theo ) và các thay đổi thiết kế trong quá trình thi công ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e1` Khoản 2 `[KHOAN]`)


---

### Mẫu #03_2021_TT-BGTVT_147344#body_context_31 (Loại: `body_context`)
> **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[03/2021/TT-BGTVT]`<SO_HIEU>`** . **[Điều 6]`<DIEU>`** . **[Khoản 2]`<KHOAN>`** . **[a ) Hồ sơ quản lý , vận hành , bảo trì công trình đường sắt : **[Biên bản nghiệm thu]`<GIAY_TO_HO_SO>`** hoàn thành hạng Mục công trình , công trình xây dựng đưa vào sử dụng của **[chủ đầu tư]`<CHU_THE_CA_NHAN>`** ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[4:5]`)
- `[e1]` **03/2021/TT-BGTVT** → `SO_HIEU` (span: `[6:7]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[0:3]`)
- `[e3]` **Điều 6** → `DIEU` (span: `[8:10]`)
- `[e4]` **Khoản 2** → `KHOAN` (span: `[11:13]`)
- `[e5]` **a ) Hồ sơ quản lý , vận hành , bảo trì công trình đường sắt : Biên bản nghiệm thu hoàn thành hạng Mục công trình , công trình xây dựng đưa vào sử dụng của chủ đầu tư ;** → `DIEM` (span: `[14:41]`)
- `[e6]` **Biên bản nghiệm thu** → `GIAY_TO_HO_SO` (span: `[25:27]`) *(lồng trong `e5` (`DIEM`))*
- `[e7]` **chủ đầu tư** → `CHU_THE_CA_NHAN` (span: `[38:40]`) *(lồng trong `e5` (`DIEM`))*

**Quan hệ:**
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 6 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`)
- (`e4` Khoản 2 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 6 `[DIEU]`)
- (`e5` a ) Hồ sơ quản lý , vận hành , bảo trì công trình đường sắt : Biên bản nghiệm thu hoàn thành hạng Mục công trình , công trình xây dựng đưa vào sử dụng của chủ đầu tư ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e4` Khoản 2 `[KHOAN]`)


---

### Mẫu #03_2021_TT-BGTVT_147344#body_standalone_32 (Loại: `body_standalone`)
> **[Điều 6]`<DIEU>`** . **[Khoản 2]`<KHOAN>`** . **[a ) Hồ sơ quản lý , vận hành , bảo trì công trình đường sắt : **[Biên bản nghiệm thu]`<GIAY_TO_HO_SO>`** hoàn thành hạng Mục công trình , công trình xây dựng đưa vào sử dụng của **[chủ đầu tư]`<CHU_THE_CA_NHAN>`** ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Điều 6** → `DIEU` (span: `[0:2]`)
- `[e1]` **Khoản 2** → `KHOAN` (span: `[3:5]`)
- `[e2]` **a ) Hồ sơ quản lý , vận hành , bảo trì công trình đường sắt : Biên bản nghiệm thu hoàn thành hạng Mục công trình , công trình xây dựng đưa vào sử dụng của chủ đầu tư ;** → `DIEM` (span: `[6:33]`)
- `[e3]` **Biên bản nghiệm thu** → `GIAY_TO_HO_SO` (span: `[17:19]`) *(lồng trong `e2` (`DIEM`))*
- `[e4]` **chủ đầu tư** → `CHU_THE_CA_NHAN` (span: `[30:32]`) *(lồng trong `e2` (`DIEM`))*

**Quan hệ:**
- (`e1` Khoản 2 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 6 `[DIEU]`)
- (`e2` a ) Hồ sơ quản lý , vận hành , bảo trì công trình đường sắt : Biên bản nghiệm thu hoàn thành hạng Mục công trình , công trình xây dựng đưa vào sử dụng của chủ đầu tư ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e1` Khoản 2 `[KHOAN]`)


---

### Mẫu #03_2021_TT-BGTVT_147344#body_context_33 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[03/2021/TT-BGTVT]`<SO_HIEU>`** ban hành **[ngày 08 tháng 02 năm 2021]`<NGAY_BAN_HANH>`** bởi **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** . **[Điều 6]`<DIEU>`** . **[Khoản 2]`<KHOAN>`** . **[b ) Hồ sơ hoàn thành bảo trì công trình đường sắt bao gồm : Hồ sơ hoàn thành bảo dưỡng công trình : Nội dung , thành phần hồ sơ **[theo quy định tại]`<TU_KHOA_PHAP_LY>`** **[Điều 53]`<THAM_CHIEU_PHAP_LY>`** của Quy trình bảo trì công trình đường sắt đã được **[Bộ Giao thông vận tải]`<CO_QUAN_THAM_QUYEN>`** phê duyệt tại **[Quyết định số 2320/QĐ-BGTVT]`<THAM_CHIEU_PHAP_LY>`** **[ngày 30 tháng 6 năm 2015]`<NGAY_THAM_CHIEU>`** ; hồ sơ xác nhận hoàn thành công tác bảo dưỡng công trình đường sắt ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **03/2021/TT-BGTVT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[11:14]`)
- `[e3]` **ngày 08 tháng 02 năm 2021** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 6** → `DIEU` (span: `[15:17]`)
- `[e5]` **Khoản 2** → `KHOAN` (span: `[18:20]`)
- `[e6]` **b ) Hồ sơ hoàn thành bảo trì công trình đường sắt bao gồm : Hồ sơ hoàn thành bảo dưỡng công trình : Nội dung , thành phần hồ sơ theo quy định tại Điều 53 của Quy trình bảo trì công trình đường sắt đã được Bộ Giao thông vận tải phê duyệt tại Quyết định số 2320/QĐ-BGTVT ngày 30 tháng 6 năm 2015 ; hồ sơ xác nhận hoàn thành công tác bảo dưỡng công trình đường sắt ;** → `DIEM` (span: `[21:73]`)
- `[e7]` **Điều 53** → `THAM_CHIEU_PHAP_LY` (span: `[42:44]`) *(lồng trong `e6` (`DIEM`))*
- `[e8]` **Quyết định số 2320/QĐ-BGTVT** → `THAM_CHIEU_PHAP_LY` (span: `[56:59]`) *(lồng trong `e6` (`DIEM`))*
- `[e9]` **theo quy định tại** → `TU_KHOA_PHAP_LY` (span: `[39:42]`) *(lồng trong `e6` (`DIEM`))*
- `[e10]` **ngày 30 tháng 6 năm 2015** → `NGAY_THAM_CHIEU` (span: `[59:65]`) *(lồng trong `e6` (`DIEM`))*
- `[e11]` **Bộ Giao thông vận tải** → `CO_QUAN_THAM_QUYEN` (span: `[51:54]`) *(lồng trong `e6` (`DIEM`))*

**Quan hệ:**
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 08 tháng 02 năm 2021 `[NGAY_BAN_HANH]`)
- (`e4` Điều 6 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`)
- (`e5` Khoản 2 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 6 `[DIEU]`)
- (`e6` b ) Hồ sơ hoàn thành bảo trì công trình đường sắt bao gồm : Hồ sơ hoàn thành bảo dưỡng công trình : Nội dung , thành phần hồ sơ theo quy định tại Điều 53 của Quy trình bảo trì công trình đường sắt đã được Bộ Giao thông vận tải phê duyệt tại Quyết định số 2320/QĐ-BGTVT ngày 30 tháng 6 năm 2015 ; hồ sơ xác nhận hoàn thành công tác bảo dưỡng công trình đường sắt ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e5` Khoản 2 `[KHOAN]`)
- (`e9` theo quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e7` Điều 53 `[THAM_CHIEU_PHAP_LY]`)
- (`e6` b ) Hồ sơ hoàn thành bảo trì công trình đường sắt bao gồm : Hồ sơ hoàn thành bảo dưỡng công trình : Nội dung , thành phần hồ sơ theo quy định tại Điều 53 của Quy trình bảo trì công trình đường sắt đã được Bộ Giao thông vận tải phê duyệt tại Quyết định số 2320/QĐ-BGTVT ngày 30 tháng 6 năm 2015 ; hồ sơ xác nhận hoàn thành công tác bảo dưỡng công trình đường sắt ; `[DIEM]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e7` Điều 53 `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e9` theo quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e8` Quyết định số 2320/QĐ-BGTVT `[THAM_CHIEU_PHAP_LY]`)
- (`e6` b ) Hồ sơ hoàn thành bảo trì công trình đường sắt bao gồm : Hồ sơ hoàn thành bảo dưỡng công trình : Nội dung , thành phần hồ sơ theo quy định tại Điều 53 của Quy trình bảo trì công trình đường sắt đã được Bộ Giao thông vận tải phê duyệt tại Quyết định số 2320/QĐ-BGTVT ngày 30 tháng 6 năm 2015 ; hồ sơ xác nhận hoàn thành công tác bảo dưỡng công trình đường sắt ; `[DIEM]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e8` Quyết định số 2320/QĐ-BGTVT `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e8` Quyết định số 2320/QĐ-BGTVT `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e10` ngày 30 tháng 6 năm 2015 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #03_2021_TT-BGTVT_147344#body_standalone_34 (Loại: `body_standalone`)
> **[Điều 6]`<DIEU>`** . **[Khoản 2]`<KHOAN>`** . **[b ) Hồ sơ hoàn thành bảo trì công trình đường sắt bao gồm : Hồ sơ hoàn thành bảo dưỡng công trình : Nội dung , thành phần hồ sơ **[theo quy định tại]`<TU_KHOA_PHAP_LY>`** **[Điều 53]`<THAM_CHIEU_PHAP_LY>`** của Quy trình bảo trì công trình đường sắt đã được **[Bộ Giao thông vận tải]`<CO_QUAN_THAM_QUYEN>`** phê duyệt tại **[Quyết định số 2320/QĐ-BGTVT]`<THAM_CHIEU_PHAP_LY>`** **[ngày 30 tháng 6 năm 2015]`<NGAY_THAM_CHIEU>`** ; hồ sơ xác nhận hoàn thành công tác bảo dưỡng công trình đường sắt ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Điều 6** → `DIEU` (span: `[0:2]`)
- `[e1]` **Khoản 2** → `KHOAN` (span: `[3:5]`)
- `[e2]` **b ) Hồ sơ hoàn thành bảo trì công trình đường sắt bao gồm : Hồ sơ hoàn thành bảo dưỡng công trình : Nội dung , thành phần hồ sơ theo quy định tại Điều 53 của Quy trình bảo trì công trình đường sắt đã được Bộ Giao thông vận tải phê duyệt tại Quyết định số 2320/QĐ-BGTVT ngày 30 tháng 6 năm 2015 ; hồ sơ xác nhận hoàn thành công tác bảo dưỡng công trình đường sắt ;** → `DIEM` (span: `[6:58]`)
- `[e3]` **Điều 53** → `THAM_CHIEU_PHAP_LY` (span: `[27:29]`) *(lồng trong `e2` (`DIEM`))*
- `[e4]` **Quyết định số 2320/QĐ-BGTVT** → `THAM_CHIEU_PHAP_LY` (span: `[41:44]`) *(lồng trong `e2` (`DIEM`))*
- `[e5]` **theo quy định tại** → `TU_KHOA_PHAP_LY` (span: `[24:27]`) *(lồng trong `e2` (`DIEM`))*
- `[e6]` **ngày 30 tháng 6 năm 2015** → `NGAY_THAM_CHIEU` (span: `[44:50]`) *(lồng trong `e2` (`DIEM`))*
- `[e7]` **Bộ Giao thông vận tải** → `CO_QUAN_THAM_QUYEN` (span: `[36:39]`) *(lồng trong `e2` (`DIEM`))*

**Quan hệ:**
- (`e1` Khoản 2 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 6 `[DIEU]`)
- (`e2` b ) Hồ sơ hoàn thành bảo trì công trình đường sắt bao gồm : Hồ sơ hoàn thành bảo dưỡng công trình : Nội dung , thành phần hồ sơ theo quy định tại Điều 53 của Quy trình bảo trì công trình đường sắt đã được Bộ Giao thông vận tải phê duyệt tại Quyết định số 2320/QĐ-BGTVT ngày 30 tháng 6 năm 2015 ; hồ sơ xác nhận hoàn thành công tác bảo dưỡng công trình đường sắt ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e1` Khoản 2 `[KHOAN]`)
- (`e5` theo quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Điều 53 `[THAM_CHIEU_PHAP_LY]`)
- (`e2` b ) Hồ sơ hoàn thành bảo trì công trình đường sắt bao gồm : Hồ sơ hoàn thành bảo dưỡng công trình : Nội dung , thành phần hồ sơ theo quy định tại Điều 53 của Quy trình bảo trì công trình đường sắt đã được Bộ Giao thông vận tải phê duyệt tại Quyết định số 2320/QĐ-BGTVT ngày 30 tháng 6 năm 2015 ; hồ sơ xác nhận hoàn thành công tác bảo dưỡng công trình đường sắt ; `[DIEM]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Điều 53 `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e5` theo quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e4` Quyết định số 2320/QĐ-BGTVT `[THAM_CHIEU_PHAP_LY]`)
- (`e2` b ) Hồ sơ hoàn thành bảo trì công trình đường sắt bao gồm : Hồ sơ hoàn thành bảo dưỡng công trình : Nội dung , thành phần hồ sơ theo quy định tại Điều 53 của Quy trình bảo trì công trình đường sắt đã được Bộ Giao thông vận tải phê duyệt tại Quyết định số 2320/QĐ-BGTVT ngày 30 tháng 6 năm 2015 ; hồ sơ xác nhận hoàn thành công tác bảo dưỡng công trình đường sắt ; `[DIEM]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e4` Quyết định số 2320/QĐ-BGTVT `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e4` Quyết định số 2320/QĐ-BGTVT `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e6` ngày 30 tháng 6 năm 2015 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #03_2021_TT-BGTVT_147344#body_context_35 (Loại: `body_context`)
> **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[03/2021/TT-BGTVT]`<SO_HIEU>`** . **[Điều 6]`<DIEU>`** . **[Khoản 2]`<KHOAN>`** . **[b ) Hồ sơ hoàn thành bảo trì công trình đường sắt bao gồm : Hồ sơ hoàn thành sửa chữa định kỳ công trình : Nội dung , thành phần hồ sơ **[theo quy định tại]`<TU_KHOA_PHAP_LY>`** **[Điều 54]`<THAM_CHIEU_PHAP_LY>`** của Quy trình bảo trì công trình đường sắt đã được **[Bộ Giao thông vận tải]`<CO_QUAN_THAM_QUYEN>`** phê duyệt tại **[Quyết định số 2320/QĐ-BGTVT]`<THAM_CHIEU_PHAP_LY>`** **[ngày 30 tháng 6 năm 2015]`<NGAY_THAM_CHIEU>`** ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[4:5]`)
- `[e1]` **03/2021/TT-BGTVT** → `SO_HIEU` (span: `[6:7]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[0:3]`)
- `[e3]` **Điều 6** → `DIEU` (span: `[8:10]`)
- `[e4]` **Khoản 2** → `KHOAN` (span: `[11:13]`)
- `[e5]` **b ) Hồ sơ hoàn thành bảo trì công trình đường sắt bao gồm : Hồ sơ hoàn thành sửa chữa định kỳ công trình : Nội dung , thành phần hồ sơ theo quy định tại Điều 54 của Quy trình bảo trì công trình đường sắt đã được Bộ Giao thông vận tải phê duyệt tại Quyết định số 2320/QĐ-BGTVT ngày 30 tháng 6 năm 2015 ;** → `DIEM` (span: `[14:59]`)
- `[e6]` **Điều 54** → `THAM_CHIEU_PHAP_LY` (span: `[35:37]`) *(lồng trong `e5` (`DIEM`))*
- `[e7]` **Quyết định số 2320/QĐ-BGTVT** → `THAM_CHIEU_PHAP_LY` (span: `[49:52]`) *(lồng trong `e5` (`DIEM`))*
- `[e8]` **theo quy định tại** → `TU_KHOA_PHAP_LY` (span: `[32:35]`) *(lồng trong `e5` (`DIEM`))*
- `[e9]` **ngày 30 tháng 6 năm 2015** → `NGAY_THAM_CHIEU` (span: `[52:58]`) *(lồng trong `e5` (`DIEM`))*
- `[e10]` **Bộ Giao thông vận tải** → `CO_QUAN_THAM_QUYEN` (span: `[44:47]`) *(lồng trong `e5` (`DIEM`))*

**Quan hệ:**
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 6 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`)
- (`e4` Khoản 2 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 6 `[DIEU]`)
- (`e5` b ) Hồ sơ hoàn thành bảo trì công trình đường sắt bao gồm : Hồ sơ hoàn thành sửa chữa định kỳ công trình : Nội dung , thành phần hồ sơ theo quy định tại Điều 54 của Quy trình bảo trì công trình đường sắt đã được Bộ Giao thông vận tải phê duyệt tại Quyết định số 2320/QĐ-BGTVT ngày 30 tháng 6 năm 2015 ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e4` Khoản 2 `[KHOAN]`)
- (`e8` theo quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e6` Điều 54 `[THAM_CHIEU_PHAP_LY]`)
- (`e5` b ) Hồ sơ hoàn thành bảo trì công trình đường sắt bao gồm : Hồ sơ hoàn thành sửa chữa định kỳ công trình : Nội dung , thành phần hồ sơ theo quy định tại Điều 54 của Quy trình bảo trì công trình đường sắt đã được Bộ Giao thông vận tải phê duyệt tại Quyết định số 2320/QĐ-BGTVT ngày 30 tháng 6 năm 2015 ; `[DIEM]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e6` Điều 54 `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e8` theo quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e7` Quyết định số 2320/QĐ-BGTVT `[THAM_CHIEU_PHAP_LY]`)
- (`e5` b ) Hồ sơ hoàn thành bảo trì công trình đường sắt bao gồm : Hồ sơ hoàn thành sửa chữa định kỳ công trình : Nội dung , thành phần hồ sơ theo quy định tại Điều 54 của Quy trình bảo trì công trình đường sắt đã được Bộ Giao thông vận tải phê duyệt tại Quyết định số 2320/QĐ-BGTVT ngày 30 tháng 6 năm 2015 ; `[DIEM]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e7` Quyết định số 2320/QĐ-BGTVT `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e7` Quyết định số 2320/QĐ-BGTVT `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e9` ngày 30 tháng 6 năm 2015 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #03_2021_TT-BGTVT_147344#body_standalone_36 (Loại: `body_standalone`)
> **[Điều 6]`<DIEU>`** . **[Khoản 2]`<KHOAN>`** . **[b ) Hồ sơ hoàn thành bảo trì công trình đường sắt bao gồm : Hồ sơ hoàn thành sửa chữa định kỳ công trình : Nội dung , thành phần hồ sơ **[theo quy định tại]`<TU_KHOA_PHAP_LY>`** **[Điều 54]`<THAM_CHIEU_PHAP_LY>`** của Quy trình bảo trì công trình đường sắt đã được **[Bộ Giao thông vận tải]`<CO_QUAN_THAM_QUYEN>`** phê duyệt tại **[Quyết định số 2320/QĐ-BGTVT]`<THAM_CHIEU_PHAP_LY>`** **[ngày 30 tháng 6 năm 2015]`<NGAY_THAM_CHIEU>`** ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Điều 6** → `DIEU` (span: `[0:2]`)
- `[e1]` **Khoản 2** → `KHOAN` (span: `[3:5]`)
- `[e2]` **b ) Hồ sơ hoàn thành bảo trì công trình đường sắt bao gồm : Hồ sơ hoàn thành sửa chữa định kỳ công trình : Nội dung , thành phần hồ sơ theo quy định tại Điều 54 của Quy trình bảo trì công trình đường sắt đã được Bộ Giao thông vận tải phê duyệt tại Quyết định số 2320/QĐ-BGTVT ngày 30 tháng 6 năm 2015 ;** → `DIEM` (span: `[6:51]`)
- `[e3]` **Điều 54** → `THAM_CHIEU_PHAP_LY` (span: `[27:29]`) *(lồng trong `e2` (`DIEM`))*
- `[e4]` **Quyết định số 2320/QĐ-BGTVT** → `THAM_CHIEU_PHAP_LY` (span: `[41:44]`) *(lồng trong `e2` (`DIEM`))*
- `[e5]` **theo quy định tại** → `TU_KHOA_PHAP_LY` (span: `[24:27]`) *(lồng trong `e2` (`DIEM`))*
- `[e6]` **ngày 30 tháng 6 năm 2015** → `NGAY_THAM_CHIEU` (span: `[44:50]`) *(lồng trong `e2` (`DIEM`))*
- `[e7]` **Bộ Giao thông vận tải** → `CO_QUAN_THAM_QUYEN` (span: `[36:39]`) *(lồng trong `e2` (`DIEM`))*

**Quan hệ:**
- (`e1` Khoản 2 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 6 `[DIEU]`)
- (`e2` b ) Hồ sơ hoàn thành bảo trì công trình đường sắt bao gồm : Hồ sơ hoàn thành sửa chữa định kỳ công trình : Nội dung , thành phần hồ sơ theo quy định tại Điều 54 của Quy trình bảo trì công trình đường sắt đã được Bộ Giao thông vận tải phê duyệt tại Quyết định số 2320/QĐ-BGTVT ngày 30 tháng 6 năm 2015 ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e1` Khoản 2 `[KHOAN]`)
- (`e5` theo quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Điều 54 `[THAM_CHIEU_PHAP_LY]`)
- (`e2` b ) Hồ sơ hoàn thành bảo trì công trình đường sắt bao gồm : Hồ sơ hoàn thành sửa chữa định kỳ công trình : Nội dung , thành phần hồ sơ theo quy định tại Điều 54 của Quy trình bảo trì công trình đường sắt đã được Bộ Giao thông vận tải phê duyệt tại Quyết định số 2320/QĐ-BGTVT ngày 30 tháng 6 năm 2015 ; `[DIEM]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Điều 54 `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e5` theo quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e4` Quyết định số 2320/QĐ-BGTVT `[THAM_CHIEU_PHAP_LY]`)
- (`e2` b ) Hồ sơ hoàn thành bảo trì công trình đường sắt bao gồm : Hồ sơ hoàn thành sửa chữa định kỳ công trình : Nội dung , thành phần hồ sơ theo quy định tại Điều 54 của Quy trình bảo trì công trình đường sắt đã được Bộ Giao thông vận tải phê duyệt tại Quyết định số 2320/QĐ-BGTVT ngày 30 tháng 6 năm 2015 ; `[DIEM]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e4` Quyết định số 2320/QĐ-BGTVT `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e4` Quyết định số 2320/QĐ-BGTVT `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e6` ngày 30 tháng 6 năm 2015 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #03_2021_TT-BGTVT_147344#body_context_37 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[03/2021/TT-BGTVT]`<SO_HIEU>`** của **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Đường sắt]`<LINH_VUC>`** . **[Điều 6]`<DIEU>`** . **[Khoản 2]`<KHOAN>`** . **[b ) Hồ sơ hoàn thành bảo trì công trình đường sắt bao gồm : Hồ sơ hoàn thành sửa chữa đột xuất công trình : nội dung , thành phần hồ sơ **[theo quy định tại]`<TU_KHOA_PHAP_LY>`** **[Điều 55]`<THAM_CHIEU_PHAP_LY>`** của Quy trình bảo trì công trình đường sắt đã được **[Bộ Giao thông vận tải]`<CO_QUAN_THAM_QUYEN>`** phê duyệt tại **[Quyết định số 2320/QĐ-BGTVT]`<THAM_CHIEU_PHAP_LY>`** **[ngày 30 tháng 6 năm 2015]`<NGAY_THAM_CHIEU>`** ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **03/2021/TT-BGTVT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[4:7]`)
- `[e3]` **Đường sắt** → `LINH_VUC` (span: `[9:10]`)
- `[e4]` **Điều 6** → `DIEU` (span: `[11:13]`)
- `[e5]` **Khoản 2** → `KHOAN` (span: `[14:16]`)
- `[e6]` **b ) Hồ sơ hoàn thành bảo trì công trình đường sắt bao gồm : Hồ sơ hoàn thành sửa chữa đột xuất công trình : nội dung , thành phần hồ sơ theo quy định tại Điều 55 của Quy trình bảo trì công trình đường sắt đã được Bộ Giao thông vận tải phê duyệt tại Quyết định số 2320/QĐ-BGTVT ngày 30 tháng 6 năm 2015 ;** → `DIEM` (span: `[17:63]`)
- `[e7]` **Điều 55** → `THAM_CHIEU_PHAP_LY` (span: `[39:41]`) *(lồng trong `e6` (`DIEM`))*
- `[e8]` **Quyết định số 2320/QĐ-BGTVT** → `THAM_CHIEU_PHAP_LY` (span: `[53:56]`) *(lồng trong `e6` (`DIEM`))*
- `[e9]` **theo quy định tại** → `TU_KHOA_PHAP_LY` (span: `[36:39]`) *(lồng trong `e6` (`DIEM`))*
- `[e10]` **ngày 30 tháng 6 năm 2015** → `NGAY_THAM_CHIEU` (span: `[56:62]`) *(lồng trong `e6` (`DIEM`))*
- `[e11]` **Bộ Giao thông vận tải** → `CO_QUAN_THAM_QUYEN` (span: `[48:51]`) *(lồng trong `e6` (`DIEM`))*

**Quan hệ:**
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Đường sắt `[LINH_VUC]`)
- (`e4` Điều 6 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`)
- (`e5` Khoản 2 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 6 `[DIEU]`)
- (`e6` b ) Hồ sơ hoàn thành bảo trì công trình đường sắt bao gồm : Hồ sơ hoàn thành sửa chữa đột xuất công trình : nội dung , thành phần hồ sơ theo quy định tại Điều 55 của Quy trình bảo trì công trình đường sắt đã được Bộ Giao thông vận tải phê duyệt tại Quyết định số 2320/QĐ-BGTVT ngày 30 tháng 6 năm 2015 ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e5` Khoản 2 `[KHOAN]`)
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Đường sắt `[LINH_VUC]`)
- (`e6` b ) Hồ sơ hoàn thành bảo trì công trình đường sắt bao gồm : Hồ sơ hoàn thành sửa chữa đột xuất công trình : nội dung , thành phần hồ sơ theo quy định tại Điều 55 của Quy trình bảo trì công trình đường sắt đã được Bộ Giao thông vận tải phê duyệt tại Quyết định số 2320/QĐ-BGTVT ngày 30 tháng 6 năm 2015 ; `[DIEM]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Đường sắt `[LINH_VUC]`)
- (`e9` theo quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e7` Điều 55 `[THAM_CHIEU_PHAP_LY]`)
- (`e6` b ) Hồ sơ hoàn thành bảo trì công trình đường sắt bao gồm : Hồ sơ hoàn thành sửa chữa đột xuất công trình : nội dung , thành phần hồ sơ theo quy định tại Điều 55 của Quy trình bảo trì công trình đường sắt đã được Bộ Giao thông vận tải phê duyệt tại Quyết định số 2320/QĐ-BGTVT ngày 30 tháng 6 năm 2015 ; `[DIEM]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e7` Điều 55 `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e9` theo quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e8` Quyết định số 2320/QĐ-BGTVT `[THAM_CHIEU_PHAP_LY]`)
- (`e6` b ) Hồ sơ hoàn thành bảo trì công trình đường sắt bao gồm : Hồ sơ hoàn thành sửa chữa đột xuất công trình : nội dung , thành phần hồ sơ theo quy định tại Điều 55 của Quy trình bảo trì công trình đường sắt đã được Bộ Giao thông vận tải phê duyệt tại Quyết định số 2320/QĐ-BGTVT ngày 30 tháng 6 năm 2015 ; `[DIEM]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e8` Quyết định số 2320/QĐ-BGTVT `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e8` Quyết định số 2320/QĐ-BGTVT `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e10` ngày 30 tháng 6 năm 2015 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #03_2021_TT-BGTVT_147344#body_standalone_38 (Loại: `body_standalone`)
> **[Điều 6]`<DIEU>`** . **[Khoản 2]`<KHOAN>`** . **[b ) Hồ sơ hoàn thành bảo trì công trình đường sắt bao gồm : Hồ sơ hoàn thành sửa chữa đột xuất công trình : nội dung , thành phần hồ sơ **[theo quy định tại]`<TU_KHOA_PHAP_LY>`** **[Điều 55]`<THAM_CHIEU_PHAP_LY>`** của Quy trình bảo trì công trình đường sắt đã được **[Bộ Giao thông vận tải]`<CO_QUAN_THAM_QUYEN>`** phê duyệt tại **[Quyết định số 2320/QĐ-BGTVT]`<THAM_CHIEU_PHAP_LY>`** **[ngày 30 tháng 6 năm 2015]`<NGAY_THAM_CHIEU>`** ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Điều 6** → `DIEU` (span: `[0:2]`)
- `[e1]` **Khoản 2** → `KHOAN` (span: `[3:5]`)
- `[e2]` **b ) Hồ sơ hoàn thành bảo trì công trình đường sắt bao gồm : Hồ sơ hoàn thành sửa chữa đột xuất công trình : nội dung , thành phần hồ sơ theo quy định tại Điều 55 của Quy trình bảo trì công trình đường sắt đã được Bộ Giao thông vận tải phê duyệt tại Quyết định số 2320/QĐ-BGTVT ngày 30 tháng 6 năm 2015 ;** → `DIEM` (span: `[6:52]`)
- `[e3]` **Điều 55** → `THAM_CHIEU_PHAP_LY` (span: `[28:30]`) *(lồng trong `e2` (`DIEM`))*
- `[e4]` **Quyết định số 2320/QĐ-BGTVT** → `THAM_CHIEU_PHAP_LY` (span: `[42:45]`) *(lồng trong `e2` (`DIEM`))*
- `[e5]` **theo quy định tại** → `TU_KHOA_PHAP_LY` (span: `[25:28]`) *(lồng trong `e2` (`DIEM`))*
- `[e6]` **ngày 30 tháng 6 năm 2015** → `NGAY_THAM_CHIEU` (span: `[45:51]`) *(lồng trong `e2` (`DIEM`))*
- `[e7]` **Bộ Giao thông vận tải** → `CO_QUAN_THAM_QUYEN` (span: `[37:40]`) *(lồng trong `e2` (`DIEM`))*

**Quan hệ:**
- (`e1` Khoản 2 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 6 `[DIEU]`)
- (`e2` b ) Hồ sơ hoàn thành bảo trì công trình đường sắt bao gồm : Hồ sơ hoàn thành sửa chữa đột xuất công trình : nội dung , thành phần hồ sơ theo quy định tại Điều 55 của Quy trình bảo trì công trình đường sắt đã được Bộ Giao thông vận tải phê duyệt tại Quyết định số 2320/QĐ-BGTVT ngày 30 tháng 6 năm 2015 ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e1` Khoản 2 `[KHOAN]`)
- (`e5` theo quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Điều 55 `[THAM_CHIEU_PHAP_LY]`)
- (`e2` b ) Hồ sơ hoàn thành bảo trì công trình đường sắt bao gồm : Hồ sơ hoàn thành sửa chữa đột xuất công trình : nội dung , thành phần hồ sơ theo quy định tại Điều 55 của Quy trình bảo trì công trình đường sắt đã được Bộ Giao thông vận tải phê duyệt tại Quyết định số 2320/QĐ-BGTVT ngày 30 tháng 6 năm 2015 ; `[DIEM]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Điều 55 `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e5` theo quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e4` Quyết định số 2320/QĐ-BGTVT `[THAM_CHIEU_PHAP_LY]`)
- (`e2` b ) Hồ sơ hoàn thành bảo trì công trình đường sắt bao gồm : Hồ sơ hoàn thành sửa chữa đột xuất công trình : nội dung , thành phần hồ sơ theo quy định tại Điều 55 của Quy trình bảo trì công trình đường sắt đã được Bộ Giao thông vận tải phê duyệt tại Quyết định số 2320/QĐ-BGTVT ngày 30 tháng 6 năm 2015 ; `[DIEM]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e4` Quyết định số 2320/QĐ-BGTVT `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e4` Quyết định số 2320/QĐ-BGTVT `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e6` ngày 30 tháng 6 năm 2015 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #03_2021_TT-BGTVT_147344#body_context_39 (Loại: `body_context`)
> **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[03/2021/TT-BGTVT]`<SO_HIEU>`** . **[Điều 6]`<DIEU>`** . **[Khoản 2]`<KHOAN>`** . **[b ) Hồ sơ hoàn thành bảo trì công trình đường sắt bao gồm : Hồ sơ quản lý chung : hồ sơ quản lý chung công bao gồm , bình đồ duỗi thẳng tuyến đường sắt ; mặt bằng bố trí chung ga đường sắt và trắc dọc rút gọn đường sắt ( Bình đồ duỗi thẳng tuyến đường sắt : bình đồ duỗi thẳng có tỷ lệ 1/500 . Phạm vi lập bình đồ duỗi thẳng : chiều dài theo phạm vi tuyến ; chiều rộng tối thiểu hết phạm vi đất dành cho đường sắt và]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[4:5]`)
- `[e1]` **03/2021/TT-BGTVT** → `SO_HIEU` (span: `[6:7]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[0:3]`)
- `[e3]` **Điều 6** → `DIEU` (span: `[8:10]`)
- `[e4]` **Khoản 2** → `KHOAN` (span: `[11:13]`)
- `[e5]` **b ) Hồ sơ hoàn thành bảo trì công trình đường sắt bao gồm : Hồ sơ quản lý chung : hồ sơ quản lý chung công bao gồm , bình đồ duỗi thẳng tuyến đường sắt ; mặt bằng bố trí chung ga đường sắt và trắc dọc rút gọn đường sắt ( Bình đồ duỗi thẳng tuyến đường sắt : bình đồ duỗi thẳng có tỷ lệ 1/500 . Phạm vi lập bình đồ duỗi thẳng : chiều dài theo phạm vi tuyến ; chiều rộng tối thiểu hết phạm vi đất dành cho đường sắt và** → `DIEM` (span: `[14:85]`)

**Quan hệ:**
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 6 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`)
- (`e4` Khoản 2 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 6 `[DIEU]`)
- (`e5` b ) Hồ sơ hoàn thành bảo trì công trình đường sắt bao gồm : Hồ sơ quản lý chung : hồ sơ quản lý chung công bao gồm , bình đồ duỗi thẳng tuyến đường sắt ; mặt bằng bố trí chung ga đường sắt và trắc dọc rút gọn đường sắt ( Bình đồ duỗi thẳng tuyến đường sắt : bình đồ duỗi thẳng có tỷ lệ 1/500 . Phạm vi lập bình đồ duỗi thẳng : chiều dài theo phạm vi tuyến ; chiều rộng tối thiểu hết phạm vi đất dành cho đường sắt và `[DIEM]`) ==[ **THUOC_VE** ]==> (`e4` Khoản 2 `[KHOAN]`)


---

### Mẫu #03_2021_TT-BGTVT_147344#body_standalone_40 (Loại: `body_standalone`)
> **[Điều 6]`<DIEU>`** . **[Khoản 2]`<KHOAN>`** . **[b ) Hồ sơ hoàn thành bảo trì công trình đường sắt bao gồm : Hồ sơ quản lý chung : hồ sơ quản lý chung công bao gồm , bình đồ duỗi thẳng tuyến đường sắt ; mặt bằng bố trí chung ga đường sắt và trắc dọc rút gọn đường sắt ( Bình đồ duỗi thẳng tuyến đường sắt : bình đồ duỗi thẳng có tỷ lệ 1/500 . Phạm vi lập bình đồ duỗi thẳng : chiều dài theo phạm vi tuyến ; chiều rộng tối thiểu hết phạm vi đất dành cho đường sắt và]`<DIEM>`**

**Thực thể:**
- `[e0]` **Điều 6** → `DIEU` (span: `[0:2]`)
- `[e1]` **Khoản 2** → `KHOAN` (span: `[3:5]`)
- `[e2]` **b ) Hồ sơ hoàn thành bảo trì công trình đường sắt bao gồm : Hồ sơ quản lý chung : hồ sơ quản lý chung công bao gồm , bình đồ duỗi thẳng tuyến đường sắt ; mặt bằng bố trí chung ga đường sắt và trắc dọc rút gọn đường sắt ( Bình đồ duỗi thẳng tuyến đường sắt : bình đồ duỗi thẳng có tỷ lệ 1/500 . Phạm vi lập bình đồ duỗi thẳng : chiều dài theo phạm vi tuyến ; chiều rộng tối thiểu hết phạm vi đất dành cho đường sắt và** → `DIEM` (span: `[6:77]`)

**Quan hệ:**
- (`e1` Khoản 2 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 6 `[DIEU]`)
- (`e2` b ) Hồ sơ hoàn thành bảo trì công trình đường sắt bao gồm : Hồ sơ quản lý chung : hồ sơ quản lý chung công bao gồm , bình đồ duỗi thẳng tuyến đường sắt ; mặt bằng bố trí chung ga đường sắt và trắc dọc rút gọn đường sắt ( Bình đồ duỗi thẳng tuyến đường sắt : bình đồ duỗi thẳng có tỷ lệ 1/500 . Phạm vi lập bình đồ duỗi thẳng : chiều dài theo phạm vi tuyến ; chiều rộng tối thiểu hết phạm vi đất dành cho đường sắt và `[DIEM]`) ==[ **THUOC_VE** ]==> (`e1` Khoản 2 `[KHOAN]`)


---

### Mẫu #03_2021_TT-BGTVT_147344#body_context_41 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[03/2021/TT-BGTVT]`<SO_HIEU>`** của **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Đường sắt]`<LINH_VUC>`** . **[Điều 6]`<DIEU>`** . **[Khoản 3]`<KHOAN>`** . **[c ) Hồ sơ quản lý đường gom nằm trong hành lang an toàn giao thông đường sắt bao gồm **[hồ sơ hoàn công]`<GIAY_TO_HO_SO>`** , **[hồ sơ thiết kế]`<GIAY_TO_HO_SO>`** , **[giấy phép thi công]`<GIAY_TO_HO_SO>`** và các văn bản liên quan khác ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **03/2021/TT-BGTVT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[4:7]`)
- `[e3]` **Đường sắt** → `LINH_VUC` (span: `[9:10]`)
- `[e4]` **Điều 6** → `DIEU` (span: `[11:13]`)
- `[e5]` **Khoản 3** → `KHOAN` (span: `[14:16]`)
- `[e6]` **c ) Hồ sơ quản lý đường gom nằm trong hành lang an toàn giao thông đường sắt bao gồm hồ sơ hoàn công , hồ sơ thiết kế , giấy phép thi công và các văn bản liên quan khác ;** → `DIEM` (span: `[17:44]`)
- `[e7]` **hồ sơ hoàn công** → `GIAY_TO_HO_SO` (span: `[30:32]`) *(lồng trong `e6` (`DIEM`))*
- `[e8]` **hồ sơ thiết kế** → `GIAY_TO_HO_SO` (span: `[33:35]`) *(lồng trong `e6` (`DIEM`))*
- `[e9]` **giấy phép thi công** → `GIAY_TO_HO_SO` (span: `[36:38]`) *(lồng trong `e6` (`DIEM`))*

**Quan hệ:**
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Đường sắt `[LINH_VUC]`)
- (`e4` Điều 6 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`)
- (`e5` Khoản 3 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 6 `[DIEU]`)
- (`e6` c ) Hồ sơ quản lý đường gom nằm trong hành lang an toàn giao thông đường sắt bao gồm hồ sơ hoàn công , hồ sơ thiết kế , giấy phép thi công và các văn bản liên quan khác ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e5` Khoản 3 `[KHOAN]`)
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Đường sắt `[LINH_VUC]`)
- (`e6` c ) Hồ sơ quản lý đường gom nằm trong hành lang an toàn giao thông đường sắt bao gồm hồ sơ hoàn công , hồ sơ thiết kế , giấy phép thi công và các văn bản liên quan khác ; `[DIEM]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Đường sắt `[LINH_VUC]`)


---

### Mẫu #03_2021_TT-BGTVT_147344#body_standalone_42 (Loại: `body_standalone`)
> **[Điều 6]`<DIEU>`** . **[Khoản 3]`<KHOAN>`** . **[c ) Hồ sơ quản lý đường gom nằm trong hành lang an toàn giao thông đường sắt bao gồm **[hồ sơ hoàn công]`<GIAY_TO_HO_SO>`** , **[hồ sơ thiết kế]`<GIAY_TO_HO_SO>`** , **[giấy phép thi công]`<GIAY_TO_HO_SO>`** và các văn bản liên quan khác ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Điều 6** → `DIEU` (span: `[0:2]`)
- `[e1]` **Khoản 3** → `KHOAN` (span: `[3:5]`)
- `[e2]` **c ) Hồ sơ quản lý đường gom nằm trong hành lang an toàn giao thông đường sắt bao gồm hồ sơ hoàn công , hồ sơ thiết kế , giấy phép thi công và các văn bản liên quan khác ;** → `DIEM` (span: `[6:33]`)
- `[e3]` **hồ sơ hoàn công** → `GIAY_TO_HO_SO` (span: `[19:21]`) *(lồng trong `e2` (`DIEM`))*
- `[e4]` **hồ sơ thiết kế** → `GIAY_TO_HO_SO` (span: `[22:24]`) *(lồng trong `e2` (`DIEM`))*
- `[e5]` **giấy phép thi công** → `GIAY_TO_HO_SO` (span: `[25:27]`) *(lồng trong `e2` (`DIEM`))*

**Quan hệ:**
- (`e1` Khoản 3 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 6 `[DIEU]`)
- (`e2` c ) Hồ sơ quản lý đường gom nằm trong hành lang an toàn giao thông đường sắt bao gồm hồ sơ hoàn công , hồ sơ thiết kế , giấy phép thi công và các văn bản liên quan khác ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e1` Khoản 3 `[KHOAN]`)


---

### Mẫu #03_2021_TT-BGTVT_147344#body_context_43 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[03/2021/TT-BGTVT]`<SO_HIEU>`** ban hành **[ngày 08 tháng 02 năm 2021]`<NGAY_BAN_HANH>`** bởi **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** . **[Điều 6]`<DIEU>`** . **[Khoản 3]`<KHOAN>`** . **[d ) Hồ sơ quản lý hàng rào ngăn cách giữa đường sắt với đường bộ bao gồm **[hồ sơ hoàn công]`<GIAY_TO_HO_SO>`** , **[hồ sơ thiết kế]`<GIAY_TO_HO_SO>`** và các văn bản liên quan khác ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **03/2021/TT-BGTVT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[11:14]`)
- `[e3]` **ngày 08 tháng 02 năm 2021** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 6** → `DIEU` (span: `[15:17]`)
- `[e5]` **Khoản 3** → `KHOAN` (span: `[18:20]`)
- `[e6]` **d ) Hồ sơ quản lý hàng rào ngăn cách giữa đường sắt với đường bộ bao gồm hồ sơ hoàn công , hồ sơ thiết kế và các văn bản liên quan khác ;** → `DIEM` (span: `[21:43]`)
- `[e7]` **hồ sơ hoàn công** → `GIAY_TO_HO_SO` (span: `[32:34]`) *(lồng trong `e6` (`DIEM`))*
- `[e8]` **hồ sơ thiết kế** → `GIAY_TO_HO_SO` (span: `[35:37]`) *(lồng trong `e6` (`DIEM`))*

**Quan hệ:**
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 08 tháng 02 năm 2021 `[NGAY_BAN_HANH]`)
- (`e4` Điều 6 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`)
- (`e5` Khoản 3 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 6 `[DIEU]`)
- (`e6` d ) Hồ sơ quản lý hàng rào ngăn cách giữa đường sắt với đường bộ bao gồm hồ sơ hoàn công , hồ sơ thiết kế và các văn bản liên quan khác ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e5` Khoản 3 `[KHOAN]`)


---

### Mẫu #03_2021_TT-BGTVT_147344#body_standalone_44 (Loại: `body_standalone`)
> **[Điều 6]`<DIEU>`** . **[Khoản 3]`<KHOAN>`** . **[d ) Hồ sơ quản lý hàng rào ngăn cách giữa đường sắt với đường bộ bao gồm **[hồ sơ hoàn công]`<GIAY_TO_HO_SO>`** , **[hồ sơ thiết kế]`<GIAY_TO_HO_SO>`** và các văn bản liên quan khác ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Điều 6** → `DIEU` (span: `[0:2]`)
- `[e1]` **Khoản 3** → `KHOAN` (span: `[3:5]`)
- `[e2]` **d ) Hồ sơ quản lý hàng rào ngăn cách giữa đường sắt với đường bộ bao gồm hồ sơ hoàn công , hồ sơ thiết kế và các văn bản liên quan khác ;** → `DIEM` (span: `[6:28]`)
- `[e3]` **hồ sơ hoàn công** → `GIAY_TO_HO_SO` (span: `[17:19]`) *(lồng trong `e2` (`DIEM`))*
- `[e4]` **hồ sơ thiết kế** → `GIAY_TO_HO_SO` (span: `[20:22]`) *(lồng trong `e2` (`DIEM`))*

**Quan hệ:**
- (`e1` Khoản 3 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 6 `[DIEU]`)
- (`e2` d ) Hồ sơ quản lý hàng rào ngăn cách giữa đường sắt với đường bộ bao gồm hồ sơ hoàn công , hồ sơ thiết kế và các văn bản liên quan khác ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e1` Khoản 3 `[KHOAN]`)


---

### Mẫu #03_2021_TT-BGTVT_147344#body_context_45 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[03/2021/TT-BGTVT]`<SO_HIEU>`** ban hành **[ngày 08 tháng 02 năm 2021]`<NGAY_BAN_HANH>`** bởi **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** . **[Điều 7]`<DIEU>`** . **[3 . Việc bảo trì công trình đường sắt phải được thực hiện theo quy chuẩn , tiêu chuẩn kỹ thuật và quy trình bảo trì công trình tương ứng đối với loại công trình đó được **[cấp có thẩm quyền]`<CO_QUAN_THAM_QUYEN>`** phê duyệt .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **03/2021/TT-BGTVT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[11:14]`)
- `[e3]` **ngày 08 tháng 02 năm 2021** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 7** → `DIEU` (span: `[15:17]`)
- `[e5]` **3 . Việc bảo trì công trình đường sắt phải được thực hiện theo quy chuẩn , tiêu chuẩn kỹ thuật và quy trình bảo trì công trình tương ứng đối với loại công trình đó được cấp có thẩm quyền phê duyệt .** → `KHOAN` (span: `[18:46]`)
- `[e6]` **cấp có thẩm quyền** → `CO_QUAN_THAM_QUYEN` (span: `[41:44]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 08 tháng 02 năm 2021 `[NGAY_BAN_HANH]`)
- (`e4` Điều 7 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`)
- (`e5` 3 . Việc bảo trì công trình đường sắt phải được thực hiện theo quy chuẩn , tiêu chuẩn kỹ thuật và quy trình bảo trì công trình tương ứng đối với loại công trình đó được cấp có thẩm quyền phê duyệt . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 7 `[DIEU]`)


---

### Mẫu #03_2021_TT-BGTVT_147344#body_context_46 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[03/2021/TT-BGTVT]`<SO_HIEU>`** ban hành **[ngày 08 tháng 02 năm 2021]`<NGAY_BAN_HANH>`** bởi **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** . **[Điều 9]`<DIEU>`** . **[7 . Các hồ sơ , tài liệu khác có liên quan đến bảo trì công trình đường sắt .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **03/2021/TT-BGTVT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[11:14]`)
- `[e3]` **ngày 08 tháng 02 năm 2021** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 9** → `DIEU` (span: `[15:17]`)
- `[e5]` **7 . Các hồ sơ , tài liệu khác có liên quan đến bảo trì công trình đường sắt .** → `KHOAN` (span: `[18:32]`)

**Quan hệ:**
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 08 tháng 02 năm 2021 `[NGAY_BAN_HANH]`)
- (`e4` Điều 9 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`)
- (`e5` 7 . Các hồ sơ , tài liệu khác có liên quan đến bảo trì công trình đường sắt . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 9 `[DIEU]`)


---

### Mẫu #03_2021_TT-BGTVT_147344#body_standalone_47 (Loại: `body_standalone`)
> **[Điều 9]`<DIEU>`** . **[7 . Các hồ sơ , tài liệu khác có liên quan đến bảo trì công trình đường sắt .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 9** → `DIEU` (span: `[0:2]`)
- `[e1]` **7 . Các hồ sơ , tài liệu khác có liên quan đến bảo trì công trình đường sắt .** → `KHOAN` (span: `[3:17]`)

**Quan hệ:**
- (`e1` 7 . Các hồ sơ , tài liệu khác có liên quan đến bảo trì công trình đường sắt . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 9 `[DIEU]`)


---

### Mẫu #03_2021_TT-BGTVT_147344#body_context_48 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[03/2021/TT-BGTVT]`<SO_HIEU>`** ban hành **[ngày 08 tháng 02 năm 2021]`<NGAY_BAN_HANH>`** bởi **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** . **[Chương II]`<CHUONG>`** . **[Điều 11 . Xử lý đối với công trình đường sắt có dấu hiệu nguy hiểm , **[không đảm bảo an toàn cho khai thác , sử dụng]`<HANH_VI_VI_PHAM>`**]`<DIEU>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **03/2021/TT-BGTVT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[11:14]`)
- `[e3]` **ngày 08 tháng 02 năm 2021** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Chương II** → `CHUONG` (span: `[15:17]`)
- `[e5]` **Điều 11 . Xử lý đối với công trình đường sắt có dấu hiệu nguy hiểm , không đảm bảo an toàn cho khai thác , sử dụng** → `DIEU` (span: `[18:35]`)
- `[e6]` **không đảm bảo an toàn cho khai thác , sử dụng** → `HANH_VI_VI_PHAM` (span: `[29:35]`) *(lồng trong `e5` (`DIEU`))*

**Quan hệ:**
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 08 tháng 02 năm 2021 `[NGAY_BAN_HANH]`)
- (`e4` Chương II `[CHUONG]`) ==[ **THUOC_VE** ]==> (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`)
- (`e5` Điều 11 . Xử lý đối với công trình đường sắt có dấu hiệu nguy hiểm , không đảm bảo an toàn cho khai thác , sử dụng `[DIEU]`) ==[ **THUOC_VE** ]==> (`e4` Chương II `[CHUONG]`)


---

### Mẫu #03_2021_TT-BGTVT_147344#body_context_49 (Loại: `body_context`)
> **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[03/2021/TT-BGTVT]`<SO_HIEU>`** . **[Điều 11]`<DIEU>`** . **[Khoản 1]`<KHOAN>`** . **[a ) Thường xuyên theo dõi , tuần , gác , kiểm tra , quan trắc để kịp thời phát hiện công trình , bộ phận công trình , thiết bị lắp đặt vào công trình hư hỏng , xuống cấp về chất lượng , **[không đảm bảo an toàn cho việc khai thác , sử dụng]`<HANH_VI_VI_PHAM>`** ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[4:5]`)
- `[e1]` **03/2021/TT-BGTVT** → `SO_HIEU` (span: `[6:7]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[0:3]`)
- `[e3]` **Điều 11** → `DIEU` (span: `[8:10]`)
- `[e4]` **Khoản 1** → `KHOAN` (span: `[11:13]`)
- `[e5]` **a ) Thường xuyên theo dõi , tuần , gác , kiểm tra , quan trắc để kịp thời phát hiện công trình , bộ phận công trình , thiết bị lắp đặt vào công trình hư hỏng , xuống cấp về chất lượng , không đảm bảo an toàn cho việc khai thác , sử dụng ;** → `DIEM` (span: `[14:52]`)
- `[e6]` **không đảm bảo an toàn cho việc khai thác , sử dụng** → `HANH_VI_VI_PHAM` (span: `[44:51]`) *(lồng trong `e5` (`DIEM`))*

**Quan hệ:**
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 11 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`)
- (`e4` Khoản 1 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 11 `[DIEU]`)
- (`e5` a ) Thường xuyên theo dõi , tuần , gác , kiểm tra , quan trắc để kịp thời phát hiện công trình , bộ phận công trình , thiết bị lắp đặt vào công trình hư hỏng , xuống cấp về chất lượng , không đảm bảo an toàn cho việc khai thác , sử dụng ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e4` Khoản 1 `[KHOAN]`)


---

### Mẫu #03_2021_TT-BGTVT_147344#body_context_50 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[03/2021/TT-BGTVT]`<SO_HIEU>`** ban hành **[ngày 08 tháng 02 năm 2021]`<NGAY_BAN_HANH>`** bởi **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** . **[Điều 11]`<DIEU>`** . **[Khoản 1]`<KHOAN>`** . **[b ) Khi phát hiện công trình đường sắt có dấu hiệu nguy hiểm , **[không đảm bảo an toàn cho việc khai thác , sử dụng phải có trách nhiệm báo cáo ngay về Cục Đường sắt Việt Nam]`<HANH_VI_VI_PHAM>`** ; đồng thời thực hiện các **[quy định tại]`<TU_KHOA_PHAP_LY>`** **[khoản 1 Điều 44 Nghị định số 46/2015/NĐ-CP]`<THAM_CHIEU_PHAP_LY>`** của **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** .]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **03/2021/TT-BGTVT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[11:14]`)
- `[e3]` **ngày 08 tháng 02 năm 2021** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 11** → `DIEU` (span: `[15:17]`)
- `[e5]` **Khoản 1** → `KHOAN` (span: `[18:20]`)
- `[e6]` **b ) Khi phát hiện công trình đường sắt có dấu hiệu nguy hiểm , không đảm bảo an toàn cho việc khai thác , sử dụng phải có trách nhiệm báo cáo ngay về Cục Đường sắt Việt Nam ; đồng thời thực hiện các quy định tại khoản 1 Điều 44 Nghị định số 46/2015/NĐ-CP của Chính phủ .** → `DIEM` (span: `[21:63]`)
- `[e7]` **không đảm bảo an toàn cho việc khai thác , sử dụng phải có trách nhiệm báo cáo ngay về Cục Đường sắt Việt Nam** → `HANH_VI_VI_PHAM` (span: `[31:47]`) *(lồng trong `e6` (`DIEM`))*
- `[e8]` **khoản 1 Điều 44 Nghị định số 46/2015/NĐ-CP** → `THAM_CHIEU_PHAP_LY` (span: `[53:60]`) *(lồng trong `e6` (`DIEM`))*
- `[e9]` **quy định tại** → `TU_KHOA_PHAP_LY` (span: `[51:53]`) *(lồng trong `e6` (`DIEM`))*
- `[e10]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[61:62]`) *(lồng trong `e6` (`DIEM`))*

**Quan hệ:**
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 08 tháng 02 năm 2021 `[NGAY_BAN_HANH]`)
- (`e4` Điều 11 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`)
- (`e5` Khoản 1 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 11 `[DIEU]`)
- (`e6` b ) Khi phát hiện công trình đường sắt có dấu hiệu nguy hiểm , không đảm bảo an toàn cho việc khai thác , sử dụng phải có trách nhiệm báo cáo ngay về Cục Đường sắt Việt Nam ; đồng thời thực hiện các quy định tại khoản 1 Điều 44 Nghị định số 46/2015/NĐ-CP của Chính phủ . `[DIEM]`) ==[ **THUOC_VE** ]==> (`e5` Khoản 1 `[KHOAN]`)
- (`e9` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e8` khoản 1 Điều 44 Nghị định số 46/2015/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e7` không đảm bảo an toàn cho việc khai thác , sử dụng phải có trách nhiệm báo cáo ngay về Cục Đường sắt Việt Nam `[HANH_VI_VI_PHAM]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e8` khoản 1 Điều 44 Nghị định số 46/2015/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)


---

### Mẫu #03_2021_TT-BGTVT_147344#body_standalone_51 (Loại: `body_standalone`)
> **[Điều 11]`<DIEU>`** . **[Khoản 1]`<KHOAN>`** . **[b ) Khi phát hiện công trình đường sắt có dấu hiệu nguy hiểm , **[không đảm bảo an toàn cho việc khai thác , sử dụng phải có trách nhiệm báo cáo ngay về Cục Đường sắt Việt Nam]`<HANH_VI_VI_PHAM>`** ; đồng thời thực hiện các **[quy định tại]`<TU_KHOA_PHAP_LY>`** **[khoản 1 Điều 44 Nghị định số 46/2015/NĐ-CP]`<THAM_CHIEU_PHAP_LY>`** của **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** .]`<DIEM>`**

**Thực thể:**
- `[e0]` **Điều 11** → `DIEU` (span: `[0:2]`)
- `[e1]` **Khoản 1** → `KHOAN` (span: `[3:5]`)
- `[e2]` **b ) Khi phát hiện công trình đường sắt có dấu hiệu nguy hiểm , không đảm bảo an toàn cho việc khai thác , sử dụng phải có trách nhiệm báo cáo ngay về Cục Đường sắt Việt Nam ; đồng thời thực hiện các quy định tại khoản 1 Điều 44 Nghị định số 46/2015/NĐ-CP của Chính phủ .** → `DIEM` (span: `[6:48]`)
- `[e3]` **không đảm bảo an toàn cho việc khai thác , sử dụng phải có trách nhiệm báo cáo ngay về Cục Đường sắt Việt Nam** → `HANH_VI_VI_PHAM` (span: `[16:32]`) *(lồng trong `e2` (`DIEM`))*
- `[e4]` **khoản 1 Điều 44 Nghị định số 46/2015/NĐ-CP** → `THAM_CHIEU_PHAP_LY` (span: `[38:45]`) *(lồng trong `e2` (`DIEM`))*
- `[e5]` **quy định tại** → `TU_KHOA_PHAP_LY` (span: `[36:38]`) *(lồng trong `e2` (`DIEM`))*
- `[e6]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[46:47]`) *(lồng trong `e2` (`DIEM`))*

**Quan hệ:**
- (`e1` Khoản 1 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 11 `[DIEU]`)
- (`e2` b ) Khi phát hiện công trình đường sắt có dấu hiệu nguy hiểm , không đảm bảo an toàn cho việc khai thác , sử dụng phải có trách nhiệm báo cáo ngay về Cục Đường sắt Việt Nam ; đồng thời thực hiện các quy định tại khoản 1 Điều 44 Nghị định số 46/2015/NĐ-CP của Chính phủ . `[DIEM]`) ==[ **THUOC_VE** ]==> (`e1` Khoản 1 `[KHOAN]`)
- (`e5` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e4` khoản 1 Điều 44 Nghị định số 46/2015/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e3` không đảm bảo an toàn cho việc khai thác , sử dụng phải có trách nhiệm báo cáo ngay về Cục Đường sắt Việt Nam `[HANH_VI_VI_PHAM]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e4` khoản 1 Điều 44 Nghị định số 46/2015/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)


---

### Mẫu #03_2021_TT-BGTVT_147344#body_context_52 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[03/2021/TT-BGTVT]`<SO_HIEU>`** ban hành **[ngày 08 tháng 02 năm 2021]`<NGAY_BAN_HANH>`** bởi **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** . **[Điều 11]`<DIEU>`** . **[2 . Khi phát hiện hoặc nhận được báo cáo về công trình đường sắt có dấu hiệu nguy hiểm , **[không đảm bảo an toàn cho việc khai thác , sử dụng , Cục Đường sắt Việt Nam kiểm tra , đề xuất biện pháp xử lý]`<HANH_VI_VI_PHAM>`** để **[Bộ Giao thông vận tải]`<CO_QUAN_THAM_QUYEN>`** quyết định .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **03/2021/TT-BGTVT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[11:14]`)
- `[e3]` **ngày 08 tháng 02 năm 2021** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 11** → `DIEU` (span: `[15:17]`)
- `[e5]` **2 . Khi phát hiện hoặc nhận được báo cáo về công trình đường sắt có dấu hiệu nguy hiểm , không đảm bảo an toàn cho việc khai thác , sử dụng , Cục Đường sắt Việt Nam kiểm tra , đề xuất biện pháp xử lý để Bộ Giao thông vận tải quyết định .** → `KHOAN` (span: `[18:55]`)
- `[e6]` **không đảm bảo an toàn cho việc khai thác , sử dụng , Cục Đường sắt Việt Nam kiểm tra , đề xuất biện pháp xử lý** → `HANH_VI_VI_PHAM` (span: `[33:49]`) *(lồng trong `e5` (`KHOAN`))*
- `[e7]` **Bộ Giao thông vận tải** → `CO_QUAN_THAM_QUYEN` (span: `[50:53]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 08 tháng 02 năm 2021 `[NGAY_BAN_HANH]`)
- (`e4` Điều 11 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`)
- (`e5` 2 . Khi phát hiện hoặc nhận được báo cáo về công trình đường sắt có dấu hiệu nguy hiểm , không đảm bảo an toàn cho việc khai thác , sử dụng , Cục Đường sắt Việt Nam kiểm tra , đề xuất biện pháp xử lý để Bộ Giao thông vận tải quyết định . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 11 `[DIEU]`)


---

### Mẫu #03_2021_TT-BGTVT_147344#body_standalone_53 (Loại: `body_standalone`)
> **[Điều 11]`<DIEU>`** . **[2 . Khi phát hiện hoặc nhận được báo cáo về công trình đường sắt có dấu hiệu nguy hiểm , **[không đảm bảo an toàn cho việc khai thác , sử dụng , Cục Đường sắt Việt Nam kiểm tra , đề xuất biện pháp xử lý]`<HANH_VI_VI_PHAM>`** để **[Bộ Giao thông vận tải]`<CO_QUAN_THAM_QUYEN>`** quyết định .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 11** → `DIEU` (span: `[0:2]`)
- `[e1]` **2 . Khi phát hiện hoặc nhận được báo cáo về công trình đường sắt có dấu hiệu nguy hiểm , không đảm bảo an toàn cho việc khai thác , sử dụng , Cục Đường sắt Việt Nam kiểm tra , đề xuất biện pháp xử lý để Bộ Giao thông vận tải quyết định .** → `KHOAN` (span: `[3:40]`)
- `[e2]` **không đảm bảo an toàn cho việc khai thác , sử dụng , Cục Đường sắt Việt Nam kiểm tra , đề xuất biện pháp xử lý** → `HANH_VI_VI_PHAM` (span: `[18:34]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **Bộ Giao thông vận tải** → `CO_QUAN_THAM_QUYEN` (span: `[35:38]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 2 . Khi phát hiện hoặc nhận được báo cáo về công trình đường sắt có dấu hiệu nguy hiểm , không đảm bảo an toàn cho việc khai thác , sử dụng , Cục Đường sắt Việt Nam kiểm tra , đề xuất biện pháp xử lý để Bộ Giao thông vận tải quyết định . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 11 `[DIEU]`)


---

### Mẫu #03_2021_TT-BGTVT_147344#body_context_54 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[03/2021/TT-BGTVT]`<SO_HIEU>`** của **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Đường sắt]`<LINH_VUC>`** . **[Điều 11]`<DIEU>`** . **[3 . Trường hợp công trình đường sắt xảy ra sự cố trong quá trình khai thác , sử dụng , việc giải quyết sự cố thực hiện **[theo quy định tại]`<TU_KHOA_PHAP_LY>`** **[Chương VI]`<THAM_CHIEU_PHAP_LY>`** **[Nghị định số 46/2015/NĐ-CP]`<THAM_CHIEU_PHAP_LY>`** của **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **03/2021/TT-BGTVT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[4:7]`)
- `[e3]` **Đường sắt** → `LINH_VUC` (span: `[9:10]`)
- `[e4]` **Điều 11** → `DIEU` (span: `[11:13]`)
- `[e5]` **3 . Trường hợp công trình đường sắt xảy ra sự cố trong quá trình khai thác , sử dụng , việc giải quyết sự cố thực hiện theo quy định tại Chương VI Nghị định số 46/2015/NĐ-CP của Chính phủ .** → `KHOAN` (span: `[14:42]`)
- `[e6]` **Chương VI** → `THAM_CHIEU_PHAP_LY` (span: `[35:36]`) *(lồng trong `e5` (`KHOAN`))*
- `[e7]` **Nghị định số 46/2015/NĐ-CP** → `THAM_CHIEU_PHAP_LY` (span: `[36:39]`) *(lồng trong `e5` (`KHOAN`))*
- `[e8]` **theo quy định tại** → `TU_KHOA_PHAP_LY` (span: `[32:35]`) *(lồng trong `e5` (`KHOAN`))*
- `[e9]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[40:41]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Đường sắt `[LINH_VUC]`)
- (`e4` Điều 11 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`)
- (`e5` 3 . Trường hợp công trình đường sắt xảy ra sự cố trong quá trình khai thác , sử dụng , việc giải quyết sự cố thực hiện theo quy định tại Chương VI Nghị định số 46/2015/NĐ-CP của Chính phủ . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 11 `[DIEU]`)
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Đường sắt `[LINH_VUC]`)
- (`e5` 3 . Trường hợp công trình đường sắt xảy ra sự cố trong quá trình khai thác , sử dụng , việc giải quyết sự cố thực hiện theo quy định tại Chương VI Nghị định số 46/2015/NĐ-CP của Chính phủ . `[KHOAN]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Đường sắt `[LINH_VUC]`)
- (`e8` theo quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e6` Chương VI `[THAM_CHIEU_PHAP_LY]`)
- (`e5` 3 . Trường hợp công trình đường sắt xảy ra sự cố trong quá trình khai thác , sử dụng , việc giải quyết sự cố thực hiện theo quy định tại Chương VI Nghị định số 46/2015/NĐ-CP của Chính phủ . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e6` Chương VI `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e8` theo quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e7` Nghị định số 46/2015/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e5` 3 . Trường hợp công trình đường sắt xảy ra sự cố trong quá trình khai thác , sử dụng , việc giải quyết sự cố thực hiện theo quy định tại Chương VI Nghị định số 46/2015/NĐ-CP của Chính phủ . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e7` Nghị định số 46/2015/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #03_2021_TT-BGTVT_147344#body_standalone_55 (Loại: `body_standalone`)
> **[Điều 11]`<DIEU>`** . **[3 . Trường hợp công trình đường sắt xảy ra sự cố trong quá trình khai thác , sử dụng , việc giải quyết sự cố thực hiện **[theo quy định tại]`<TU_KHOA_PHAP_LY>`** **[Chương VI]`<THAM_CHIEU_PHAP_LY>`** **[Nghị định số 46/2015/NĐ-CP]`<THAM_CHIEU_PHAP_LY>`** của **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 11** → `DIEU` (span: `[0:2]`)
- `[e1]` **3 . Trường hợp công trình đường sắt xảy ra sự cố trong quá trình khai thác , sử dụng , việc giải quyết sự cố thực hiện theo quy định tại Chương VI Nghị định số 46/2015/NĐ-CP của Chính phủ .** → `KHOAN` (span: `[3:31]`)
- `[e2]` **Chương VI** → `THAM_CHIEU_PHAP_LY` (span: `[24:25]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **Nghị định số 46/2015/NĐ-CP** → `THAM_CHIEU_PHAP_LY` (span: `[25:28]`) *(lồng trong `e1` (`KHOAN`))*
- `[e4]` **theo quy định tại** → `TU_KHOA_PHAP_LY` (span: `[21:24]`) *(lồng trong `e1` (`KHOAN`))*
- `[e5]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[29:30]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 3 . Trường hợp công trình đường sắt xảy ra sự cố trong quá trình khai thác , sử dụng , việc giải quyết sự cố thực hiện theo quy định tại Chương VI Nghị định số 46/2015/NĐ-CP của Chính phủ . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 11 `[DIEU]`)
- (`e4` theo quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e2` Chương VI `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 3 . Trường hợp công trình đường sắt xảy ra sự cố trong quá trình khai thác , sử dụng , việc giải quyết sự cố thực hiện theo quy định tại Chương VI Nghị định số 46/2015/NĐ-CP của Chính phủ . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e2` Chương VI `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e4` theo quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Nghị định số 46/2015/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 3 . Trường hợp công trình đường sắt xảy ra sự cố trong quá trình khai thác , sử dụng , việc giải quyết sự cố thực hiện theo quy định tại Chương VI Nghị định số 46/2015/NĐ-CP của Chính phủ . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Nghị định số 46/2015/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #03_2021_TT-BGTVT_147344#body_context_56 (Loại: `body_context`)
> **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[03/2021/TT-BGTVT]`<SO_HIEU>`** . **[Điều 12]`<DIEU>`** . **[2 . Công trình đường sắt hết thời hạn sử dụng là công trình đã có thời gian khai thác , sử dụng lớn hơn thời hạn sử dụng theo **[hồ sơ thiết kế]`<GIAY_TO_HO_SO>`** của công trình . Trường hợp **[hồ sơ thiết kế]`<GIAY_TO_HO_SO>`** của công trình bị mất hoặc không quy định thời hạn sử dụng , thời hạn sử dụng của công trình được xác định theo tiêu chuẩn , quy chuẩn kỹ thuật có liên quan hoặc theo kết quả kiểm định chất lượng công trình .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[4:5]`)
- `[e1]` **03/2021/TT-BGTVT** → `SO_HIEU` (span: `[6:7]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[0:3]`)
- `[e3]` **Điều 12** → `DIEU` (span: `[8:10]`)
- `[e4]` **2 . Công trình đường sắt hết thời hạn sử dụng là công trình đã có thời gian khai thác , sử dụng lớn hơn thời hạn sử dụng theo hồ sơ thiết kế của công trình . Trường hợp hồ sơ thiết kế của công trình bị mất hoặc không quy định thời hạn sử dụng , thời hạn sử dụng của công trình được xác định theo tiêu chuẩn , quy chuẩn kỹ thuật có liên quan hoặc theo kết quả kiểm định chất lượng công trình .** → `KHOAN` (span: `[11:69]`)
- `[e5]` **hồ sơ thiết kế** → `GIAY_TO_HO_SO` (span: `[31:33]`) *(lồng trong `e4` (`KHOAN`))*
- `[e6]` **hồ sơ thiết kế** → `GIAY_TO_HO_SO` (span: `[37:39]`) *(lồng trong `e4` (`KHOAN`))*

**Quan hệ:**
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 12 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`)
- (`e4` 2 . Công trình đường sắt hết thời hạn sử dụng là công trình đã có thời gian khai thác , sử dụng lớn hơn thời hạn sử dụng theo hồ sơ thiết kế của công trình . Trường hợp hồ sơ thiết kế của công trình bị mất hoặc không quy định thời hạn sử dụng , thời hạn sử dụng của công trình được xác định theo tiêu chuẩn , quy chuẩn kỹ thuật có liên quan hoặc theo kết quả kiểm định chất lượng công trình . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 12 `[DIEU]`)


---

### Mẫu #03_2021_TT-BGTVT_147344#body_standalone_57 (Loại: `body_standalone`)
> **[Điều 12]`<DIEU>`** . **[2 . Công trình đường sắt hết thời hạn sử dụng là công trình đã có thời gian khai thác , sử dụng lớn hơn thời hạn sử dụng theo **[hồ sơ thiết kế]`<GIAY_TO_HO_SO>`** của công trình . Trường hợp **[hồ sơ thiết kế]`<GIAY_TO_HO_SO>`** của công trình bị mất hoặc không quy định thời hạn sử dụng , thời hạn sử dụng của công trình được xác định theo tiêu chuẩn , quy chuẩn kỹ thuật có liên quan hoặc theo kết quả kiểm định chất lượng công trình .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 12** → `DIEU` (span: `[0:2]`)
- `[e1]` **2 . Công trình đường sắt hết thời hạn sử dụng là công trình đã có thời gian khai thác , sử dụng lớn hơn thời hạn sử dụng theo hồ sơ thiết kế của công trình . Trường hợp hồ sơ thiết kế của công trình bị mất hoặc không quy định thời hạn sử dụng , thời hạn sử dụng của công trình được xác định theo tiêu chuẩn , quy chuẩn kỹ thuật có liên quan hoặc theo kết quả kiểm định chất lượng công trình .** → `KHOAN` (span: `[3:61]`)
- `[e2]` **hồ sơ thiết kế** → `GIAY_TO_HO_SO` (span: `[23:25]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **hồ sơ thiết kế** → `GIAY_TO_HO_SO` (span: `[29:31]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 2 . Công trình đường sắt hết thời hạn sử dụng là công trình đã có thời gian khai thác , sử dụng lớn hơn thời hạn sử dụng theo hồ sơ thiết kế của công trình . Trường hợp hồ sơ thiết kế của công trình bị mất hoặc không quy định thời hạn sử dụng , thời hạn sử dụng của công trình được xác định theo tiêu chuẩn , quy chuẩn kỹ thuật có liên quan hoặc theo kết quả kiểm định chất lượng công trình . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 12 `[DIEU]`)


---

### Mẫu #03_2021_TT-BGTVT_147344#body_context_58 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[03/2021/TT-BGTVT]`<SO_HIEU>`** của **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Đường sắt]`<LINH_VUC>`** . **[Điều 12]`<DIEU>`** . **[3 . **[Tối thiểu một năm]`<THOI_HAN>`** trước khi công trình đường sắt hết thời hạn sử dụng , nếu có nhu cầu tiếp tục sử dụng , **[doanh nghiệp kinh doanh kết cấu hạ tầng đường sắt]`<TO_CHUC_DOANH_NGHIEP>`** , tổ chức , cá nhân nhận chuyển nhượng có thời hạn , thuê quyền khai thác , kinh doanh kết cấu hạ tầng đường sắt quốc gia do nhà nước đầu tư phải báo cáo **[Bộ Giao thông vận tải]`<CO_QUAN_THAM_QUYEN>`** , Cục Đường sắt Việt Nam để tổ chức thực hiện kiểm tra , kiểm định , đánh giá chất lượng hiện trạng của]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **03/2021/TT-BGTVT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[4:7]`)
- `[e3]` **Đường sắt** → `LINH_VUC` (span: `[9:10]`)
- `[e4]` **Điều 12** → `DIEU` (span: `[11:13]`)
- `[e5]` **3 . Tối thiểu một năm trước khi công trình đường sắt hết thời hạn sử dụng , nếu có nhu cầu tiếp tục sử dụng , doanh nghiệp kinh doanh kết cấu hạ tầng đường sắt , tổ chức , cá nhân nhận chuyển nhượng có thời hạn , thuê quyền khai thác , kinh doanh kết cấu hạ tầng đường sắt quốc gia do nhà nước đầu tư phải báo cáo Bộ Giao thông vận tải , Cục Đường sắt Việt Nam để tổ chức thực hiện kiểm tra , kiểm định , đánh giá chất lượng hiện trạng của** → `KHOAN` (span: `[14:77]`)
- `[e6]` **Tối thiểu một năm** → `THOI_HAN` (span: `[16:19]`) *(lồng trong `e5` (`KHOAN`))*
- `[e7]` **Bộ Giao thông vận tải** → `CO_QUAN_THAM_QUYEN` (span: `[59:62]`) *(lồng trong `e5` (`KHOAN`))*
- `[e8]` **doanh nghiệp kinh doanh kết cấu hạ tầng đường sắt** → `TO_CHUC_DOANH_NGHIEP` (span: `[33:37]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Đường sắt `[LINH_VUC]`)
- (`e4` Điều 12 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`)
- (`e5` 3 . Tối thiểu một năm trước khi công trình đường sắt hết thời hạn sử dụng , nếu có nhu cầu tiếp tục sử dụng , doanh nghiệp kinh doanh kết cấu hạ tầng đường sắt , tổ chức , cá nhân nhận chuyển nhượng có thời hạn , thuê quyền khai thác , kinh doanh kết cấu hạ tầng đường sắt quốc gia do nhà nước đầu tư phải báo cáo Bộ Giao thông vận tải , Cục Đường sắt Việt Nam để tổ chức thực hiện kiểm tra , kiểm định , đánh giá chất lượng hiện trạng của `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 12 `[DIEU]`)
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Đường sắt `[LINH_VUC]`)
- (`e5` 3 . Tối thiểu một năm trước khi công trình đường sắt hết thời hạn sử dụng , nếu có nhu cầu tiếp tục sử dụng , doanh nghiệp kinh doanh kết cấu hạ tầng đường sắt , tổ chức , cá nhân nhận chuyển nhượng có thời hạn , thuê quyền khai thác , kinh doanh kết cấu hạ tầng đường sắt quốc gia do nhà nước đầu tư phải báo cáo Bộ Giao thông vận tải , Cục Đường sắt Việt Nam để tổ chức thực hiện kiểm tra , kiểm định , đánh giá chất lượng hiện trạng của `[KHOAN]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Đường sắt `[LINH_VUC]`)


---

### Mẫu #03_2021_TT-BGTVT_147344#body_standalone_59 (Loại: `body_standalone`)
> **[Điều 12]`<DIEU>`** . **[3 . **[Tối thiểu một năm]`<THOI_HAN>`** trước khi công trình đường sắt hết thời hạn sử dụng , nếu có nhu cầu tiếp tục sử dụng , **[doanh nghiệp kinh doanh kết cấu hạ tầng đường sắt]`<TO_CHUC_DOANH_NGHIEP>`** , tổ chức , cá nhân nhận chuyển nhượng có thời hạn , thuê quyền khai thác , kinh doanh kết cấu hạ tầng đường sắt quốc gia do nhà nước đầu tư phải báo cáo **[Bộ Giao thông vận tải]`<CO_QUAN_THAM_QUYEN>`** , Cục Đường sắt Việt Nam để tổ chức thực hiện kiểm tra , kiểm định , đánh giá chất lượng hiện trạng của]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 12** → `DIEU` (span: `[0:2]`)
- `[e1]` **3 . Tối thiểu một năm trước khi công trình đường sắt hết thời hạn sử dụng , nếu có nhu cầu tiếp tục sử dụng , doanh nghiệp kinh doanh kết cấu hạ tầng đường sắt , tổ chức , cá nhân nhận chuyển nhượng có thời hạn , thuê quyền khai thác , kinh doanh kết cấu hạ tầng đường sắt quốc gia do nhà nước đầu tư phải báo cáo Bộ Giao thông vận tải , Cục Đường sắt Việt Nam để tổ chức thực hiện kiểm tra , kiểm định , đánh giá chất lượng hiện trạng của** → `KHOAN` (span: `[3:66]`)
- `[e2]` **Tối thiểu một năm** → `THOI_HAN` (span: `[5:8]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **Bộ Giao thông vận tải** → `CO_QUAN_THAM_QUYEN` (span: `[48:51]`) *(lồng trong `e1` (`KHOAN`))*
- `[e4]` **doanh nghiệp kinh doanh kết cấu hạ tầng đường sắt** → `TO_CHUC_DOANH_NGHIEP` (span: `[22:26]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 3 . Tối thiểu một năm trước khi công trình đường sắt hết thời hạn sử dụng , nếu có nhu cầu tiếp tục sử dụng , doanh nghiệp kinh doanh kết cấu hạ tầng đường sắt , tổ chức , cá nhân nhận chuyển nhượng có thời hạn , thuê quyền khai thác , kinh doanh kết cấu hạ tầng đường sắt quốc gia do nhà nước đầu tư phải báo cáo Bộ Giao thông vận tải , Cục Đường sắt Việt Nam để tổ chức thực hiện kiểm tra , kiểm định , đánh giá chất lượng hiện trạng của `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 12 `[DIEU]`)


---

### Mẫu #03_2021_TT-BGTVT_147344#body_context_60 (Loại: `body_context`)
> **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[03/2021/TT-BGTVT]`<SO_HIEU>`** . **[Điều 12]`<DIEU>`** . **[4 . Cục Đường sắt Việt Nam chịu trách nhiệm tổ chức thực hiện và báo cáo , đề xuất **[phương án xử lý]`<GIAY_TO_HO_SO>`** , lộ trình thực hiện theo quy định của pháp luật về **[Bộ Giao thông vận tải]`<CO_QUAN_THAM_QUYEN>`** để được xem xét quyết định .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[4:5]`)
- `[e1]` **03/2021/TT-BGTVT** → `SO_HIEU` (span: `[6:7]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[0:3]`)
- `[e3]` **Điều 12** → `DIEU` (span: `[8:10]`)
- `[e4]` **4 . Cục Đường sắt Việt Nam chịu trách nhiệm tổ chức thực hiện và báo cáo , đề xuất phương án xử lý , lộ trình thực hiện theo quy định của pháp luật về Bộ Giao thông vận tải để được xem xét quyết định .** → `KHOAN` (span: `[11:42]`)
- `[e5]` **Bộ Giao thông vận tải** → `CO_QUAN_THAM_QUYEN` (span: `[34:37]`) *(lồng trong `e4` (`KHOAN`))*
- `[e6]` **phương án xử lý** → `GIAY_TO_HO_SO` (span: `[24:26]`) *(lồng trong `e4` (`KHOAN`))*

**Quan hệ:**
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 12 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`)
- (`e4` 4 . Cục Đường sắt Việt Nam chịu trách nhiệm tổ chức thực hiện và báo cáo , đề xuất phương án xử lý , lộ trình thực hiện theo quy định của pháp luật về Bộ Giao thông vận tải để được xem xét quyết định . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 12 `[DIEU]`)


---

### Mẫu #03_2021_TT-BGTVT_147344#body_standalone_61 (Loại: `body_standalone`)
> **[Điều 12]`<DIEU>`** . **[4 . Cục Đường sắt Việt Nam chịu trách nhiệm tổ chức thực hiện và báo cáo , đề xuất **[phương án xử lý]`<GIAY_TO_HO_SO>`** , lộ trình thực hiện theo quy định của pháp luật về **[Bộ Giao thông vận tải]`<CO_QUAN_THAM_QUYEN>`** để được xem xét quyết định .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 12** → `DIEU` (span: `[0:2]`)
- `[e1]` **4 . Cục Đường sắt Việt Nam chịu trách nhiệm tổ chức thực hiện và báo cáo , đề xuất phương án xử lý , lộ trình thực hiện theo quy định của pháp luật về Bộ Giao thông vận tải để được xem xét quyết định .** → `KHOAN` (span: `[3:34]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_THAM_QUYEN` (span: `[26:29]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **phương án xử lý** → `GIAY_TO_HO_SO` (span: `[16:18]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 4 . Cục Đường sắt Việt Nam chịu trách nhiệm tổ chức thực hiện và báo cáo , đề xuất phương án xử lý , lộ trình thực hiện theo quy định của pháp luật về Bộ Giao thông vận tải để được xem xét quyết định . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 12 `[DIEU]`)


---

### Mẫu #03_2021_TT-BGTVT_147344#body_context_62 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[03/2021/TT-BGTVT]`<SO_HIEU>`** ban hành **[ngày 08 tháng 02 năm 2021]`<NGAY_BAN_HANH>`** bởi **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** . **[Điều 13]`<DIEU>`** . **[Khoản 1]`<KHOAN>`** . **[a ) Các công trình đường sắt theo quy định của pháp luật về quản lý chất lượng và bảo trì công trình xây dựng ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **03/2021/TT-BGTVT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[11:14]`)
- `[e3]` **ngày 08 tháng 02 năm 2021** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 13** → `DIEU` (span: `[15:17]`)
- `[e5]` **Khoản 1** → `KHOAN` (span: `[18:20]`)
- `[e6]` **a ) Các công trình đường sắt theo quy định của pháp luật về quản lý chất lượng và bảo trì công trình xây dựng ;** → `DIEM` (span: `[21:38]`)

**Quan hệ:**
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 08 tháng 02 năm 2021 `[NGAY_BAN_HANH]`)
- (`e4` Điều 13 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`)
- (`e5` Khoản 1 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 13 `[DIEU]`)
- (`e6` a ) Các công trình đường sắt theo quy định của pháp luật về quản lý chất lượng và bảo trì công trình xây dựng ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e5` Khoản 1 `[KHOAN]`)


---

### Mẫu #03_2021_TT-BGTVT_147344#body_context_63 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[03/2021/TT-BGTVT]`<SO_HIEU>`** của **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Đường sắt]`<LINH_VUC>`** . **[Điều 13]`<DIEU>`** . **[Khoản 5]`<KHOAN>`** . **[b ) **[Báo cáo kết quả quan trắc]`<GIAY_TO_HO_SO>`** , đề xuất kiến nghị **[Bộ Giao thông vận tải]`<CO_QUAN_THAM_QUYEN>`** có biện pháp xử lý kịp thời đối với trường hợp số liệu quan trắc vượt quá giá trị cho phép hoặc có dấu hiệu bất thường .]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **03/2021/TT-BGTVT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[4:7]`)
- `[e3]` **Đường sắt** → `LINH_VUC` (span: `[9:10]`)
- `[e4]` **Điều 13** → `DIEU` (span: `[11:13]`)
- `[e5]` **Khoản 5** → `KHOAN` (span: `[14:16]`)
- `[e6]` **b ) Báo cáo kết quả quan trắc , đề xuất kiến nghị Bộ Giao thông vận tải có biện pháp xử lý kịp thời đối với trường hợp số liệu quan trắc vượt quá giá trị cho phép hoặc có dấu hiệu bất thường .** → `DIEM` (span: `[17:45]`)
- `[e7]` **Bộ Giao thông vận tải** → `CO_QUAN_THAM_QUYEN` (span: `[25:28]`) *(lồng trong `e6` (`DIEM`))*
- `[e8]` **Báo cáo kết quả quan trắc** → `GIAY_TO_HO_SO` (span: `[19:22]`) *(lồng trong `e6` (`DIEM`))*

**Quan hệ:**
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Đường sắt `[LINH_VUC]`)
- (`e4` Điều 13 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`)
- (`e5` Khoản 5 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 13 `[DIEU]`)
- (`e6` b ) Báo cáo kết quả quan trắc , đề xuất kiến nghị Bộ Giao thông vận tải có biện pháp xử lý kịp thời đối với trường hợp số liệu quan trắc vượt quá giá trị cho phép hoặc có dấu hiệu bất thường . `[DIEM]`) ==[ **THUOC_VE** ]==> (`e5` Khoản 5 `[KHOAN]`)
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Đường sắt `[LINH_VUC]`)
- (`e6` b ) Báo cáo kết quả quan trắc , đề xuất kiến nghị Bộ Giao thông vận tải có biện pháp xử lý kịp thời đối với trường hợp số liệu quan trắc vượt quá giá trị cho phép hoặc có dấu hiệu bất thường . `[DIEM]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Đường sắt `[LINH_VUC]`)


---

### Mẫu #03_2021_TT-BGTVT_147344#body_standalone_64 (Loại: `body_standalone`)
> **[Điều 13]`<DIEU>`** . **[Khoản 5]`<KHOAN>`** . **[b ) **[Báo cáo kết quả quan trắc]`<GIAY_TO_HO_SO>`** , đề xuất kiến nghị **[Bộ Giao thông vận tải]`<CO_QUAN_THAM_QUYEN>`** có biện pháp xử lý kịp thời đối với trường hợp số liệu quan trắc vượt quá giá trị cho phép hoặc có dấu hiệu bất thường .]`<DIEM>`**

**Thực thể:**
- `[e0]` **Điều 13** → `DIEU` (span: `[0:2]`)
- `[e1]` **Khoản 5** → `KHOAN` (span: `[3:5]`)
- `[e2]` **b ) Báo cáo kết quả quan trắc , đề xuất kiến nghị Bộ Giao thông vận tải có biện pháp xử lý kịp thời đối với trường hợp số liệu quan trắc vượt quá giá trị cho phép hoặc có dấu hiệu bất thường .** → `DIEM` (span: `[6:34]`)
- `[e3]` **Bộ Giao thông vận tải** → `CO_QUAN_THAM_QUYEN` (span: `[14:17]`) *(lồng trong `e2` (`DIEM`))*
- `[e4]` **Báo cáo kết quả quan trắc** → `GIAY_TO_HO_SO` (span: `[8:11]`) *(lồng trong `e2` (`DIEM`))*

**Quan hệ:**
- (`e1` Khoản 5 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 13 `[DIEU]`)
- (`e2` b ) Báo cáo kết quả quan trắc , đề xuất kiến nghị Bộ Giao thông vận tải có biện pháp xử lý kịp thời đối với trường hợp số liệu quan trắc vượt quá giá trị cho phép hoặc có dấu hiệu bất thường . `[DIEM]`) ==[ **THUOC_VE** ]==> (`e1` Khoản 5 `[KHOAN]`)


---

### Mẫu #03_2021_TT-BGTVT_147344#body_context_65 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[03/2021/TT-BGTVT]`<SO_HIEU>`** ban hành **[ngày 08 tháng 02 năm 2021]`<NGAY_BAN_HANH>`** bởi **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** . **[Điều 13]`<DIEU>`** . **[6 . Tổ chức , cá nhân nhận chuyển nhượng có thời hạn , thuê quyền khai thác , kinh doanh kết cấu hạ tầng đường sắt quốc gia do nhà nước đầu tư tổ chức lập đề cương , trình Cục Đường sắt Việt Nam thẩm định , phê duyệt ; tự phê duyệt dự toán , tổ chức thực hiện và lập báo cáo **[theo quy định tại]`<TU_KHOA_PHAP_LY>`** **[điểm a khoản 5 Điều này]`<THAM_CHIEU_PHAP_LY>`** .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **03/2021/TT-BGTVT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[11:14]`)
- `[e3]` **ngày 08 tháng 02 năm 2021** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 13** → `DIEU` (span: `[15:17]`)
- `[e5]` **6 . Tổ chức , cá nhân nhận chuyển nhượng có thời hạn , thuê quyền khai thác , kinh doanh kết cấu hạ tầng đường sắt quốc gia do nhà nước đầu tư tổ chức lập đề cương , trình Cục Đường sắt Việt Nam thẩm định , phê duyệt ; tự phê duyệt dự toán , tổ chức thực hiện và lập báo cáo theo quy định tại điểm a khoản 5 Điều này .** → `KHOAN` (span: `[18:70]`)
- `[e6]` **điểm a khoản 5 Điều này** → `THAM_CHIEU_PHAP_LY` (span: `[63:69]`) *(lồng trong `e5` (`KHOAN`))*
- `[e7]` **theo quy định tại** → `TU_KHOA_PHAP_LY` (span: `[60:63]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 08 tháng 02 năm 2021 `[NGAY_BAN_HANH]`)
- (`e4` Điều 13 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`)
- (`e5` 6 . Tổ chức , cá nhân nhận chuyển nhượng có thời hạn , thuê quyền khai thác , kinh doanh kết cấu hạ tầng đường sắt quốc gia do nhà nước đầu tư tổ chức lập đề cương , trình Cục Đường sắt Việt Nam thẩm định , phê duyệt ; tự phê duyệt dự toán , tổ chức thực hiện và lập báo cáo theo quy định tại điểm a khoản 5 Điều này . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 13 `[DIEU]`)
- (`e7` theo quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e6` điểm a khoản 5 Điều này `[THAM_CHIEU_PHAP_LY]`)
- (`e5` 6 . Tổ chức , cá nhân nhận chuyển nhượng có thời hạn , thuê quyền khai thác , kinh doanh kết cấu hạ tầng đường sắt quốc gia do nhà nước đầu tư tổ chức lập đề cương , trình Cục Đường sắt Việt Nam thẩm định , phê duyệt ; tự phê duyệt dự toán , tổ chức thực hiện và lập báo cáo theo quy định tại điểm a khoản 5 Điều này . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e6` điểm a khoản 5 Điều này `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #03_2021_TT-BGTVT_147344#body_standalone_66 (Loại: `body_standalone`)
> **[Điều 13]`<DIEU>`** . **[6 . Tổ chức , cá nhân nhận chuyển nhượng có thời hạn , thuê quyền khai thác , kinh doanh kết cấu hạ tầng đường sắt quốc gia do nhà nước đầu tư tổ chức lập đề cương , trình Cục Đường sắt Việt Nam thẩm định , phê duyệt ; tự phê duyệt dự toán , tổ chức thực hiện và lập báo cáo **[theo quy định tại]`<TU_KHOA_PHAP_LY>`** **[điểm a khoản 5 Điều này]`<THAM_CHIEU_PHAP_LY>`** .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 13** → `DIEU` (span: `[0:2]`)
- `[e1]` **6 . Tổ chức , cá nhân nhận chuyển nhượng có thời hạn , thuê quyền khai thác , kinh doanh kết cấu hạ tầng đường sắt quốc gia do nhà nước đầu tư tổ chức lập đề cương , trình Cục Đường sắt Việt Nam thẩm định , phê duyệt ; tự phê duyệt dự toán , tổ chức thực hiện và lập báo cáo theo quy định tại điểm a khoản 5 Điều này .** → `KHOAN` (span: `[3:55]`)
- `[e2]` **điểm a khoản 5 Điều này** → `THAM_CHIEU_PHAP_LY` (span: `[48:54]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **theo quy định tại** → `TU_KHOA_PHAP_LY` (span: `[45:48]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 6 . Tổ chức , cá nhân nhận chuyển nhượng có thời hạn , thuê quyền khai thác , kinh doanh kết cấu hạ tầng đường sắt quốc gia do nhà nước đầu tư tổ chức lập đề cương , trình Cục Đường sắt Việt Nam thẩm định , phê duyệt ; tự phê duyệt dự toán , tổ chức thực hiện và lập báo cáo theo quy định tại điểm a khoản 5 Điều này . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 13 `[DIEU]`)
- (`e3` theo quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e2` điểm a khoản 5 Điều này `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 6 . Tổ chức , cá nhân nhận chuyển nhượng có thời hạn , thuê quyền khai thác , kinh doanh kết cấu hạ tầng đường sắt quốc gia do nhà nước đầu tư tổ chức lập đề cương , trình Cục Đường sắt Việt Nam thẩm định , phê duyệt ; tự phê duyệt dự toán , tổ chức thực hiện và lập báo cáo theo quy định tại điểm a khoản 5 Điều này . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e2` điểm a khoản 5 Điều này `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #03_2021_TT-BGTVT_147344#body_context_67 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[03/2021/TT-BGTVT]`<SO_HIEU>`** của **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Đường sắt]`<LINH_VUC>`** . **[Điều 14 . Áp dụng tiêu chuẩn , quy chuẩn kỹ thuật , định mức kinh tế - kỹ thuật trong công tác bảo trì công trình đường sắt]`<DIEU>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **03/2021/TT-BGTVT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[4:7]`)
- `[e3]` **Đường sắt** → `LINH_VUC` (span: `[9:10]`)
- `[e4]` **Điều 14 . Áp dụng tiêu chuẩn , quy chuẩn kỹ thuật , định mức kinh tế - kỹ thuật trong công tác bảo trì công trình đường sắt** → `DIEU` (span: `[11:30]`)

**Quan hệ:**
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Đường sắt `[LINH_VUC]`)
- (`e4` Điều 14 . Áp dụng tiêu chuẩn , quy chuẩn kỹ thuật , định mức kinh tế - kỹ thuật trong công tác bảo trì công trình đường sắt `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`)
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Đường sắt `[LINH_VUC]`)
- (`e4` Điều 14 . Áp dụng tiêu chuẩn , quy chuẩn kỹ thuật , định mức kinh tế - kỹ thuật trong công tác bảo trì công trình đường sắt `[DIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Đường sắt `[LINH_VUC]`)


---

### Mẫu #03_2021_TT-BGTVT_147344#body_context_68 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[03/2021/TT-BGTVT]`<SO_HIEU>`** của **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Đường sắt]`<LINH_VUC>`** . **[Điều 14]`<DIEU>`** . **[Khoản 1]`<KHOAN>`** . **[b ) Đối với các hạng mục công trình chưa có định mức kinh tế - kỹ thuật , áp dụng các định mức tương ứng của các ngành hoặc của địa phương đã được **[cơ quan có thẩm quyền]`<CO_QUAN_THAM_QUYEN>`** ban hành sau khi có ý kiến chấp thuận của **[Bộ Giao thông vận tải]`<CO_QUAN_THAM_QUYEN>`** .]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **03/2021/TT-BGTVT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[4:7]`)
- `[e3]` **Đường sắt** → `LINH_VUC` (span: `[9:10]`)
- `[e4]` **Điều 14** → `DIEU` (span: `[11:13]`)
- `[e5]` **Khoản 1** → `KHOAN` (span: `[14:16]`)
- `[e6]` **b ) Đối với các hạng mục công trình chưa có định mức kinh tế - kỹ thuật , áp dụng các định mức tương ứng của các ngành hoặc của địa phương đã được cơ quan có thẩm quyền ban hành sau khi có ý kiến chấp thuận của Bộ Giao thông vận tải .** → `DIEM` (span: `[17:57]`)
- `[e7]` **cơ quan có thẩm quyền** → `CO_QUAN_THAM_QUYEN` (span: `[43:46]`) *(lồng trong `e6` (`DIEM`))*
- `[e8]` **Bộ Giao thông vận tải** → `CO_QUAN_THAM_QUYEN` (span: `[53:56]`) *(lồng trong `e6` (`DIEM`))*

**Quan hệ:**
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Đường sắt `[LINH_VUC]`)
- (`e4` Điều 14 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`)
- (`e5` Khoản 1 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 14 `[DIEU]`)
- (`e6` b ) Đối với các hạng mục công trình chưa có định mức kinh tế - kỹ thuật , áp dụng các định mức tương ứng của các ngành hoặc của địa phương đã được cơ quan có thẩm quyền ban hành sau khi có ý kiến chấp thuận của Bộ Giao thông vận tải . `[DIEM]`) ==[ **THUOC_VE** ]==> (`e5` Khoản 1 `[KHOAN]`)
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Đường sắt `[LINH_VUC]`)
- (`e6` b ) Đối với các hạng mục công trình chưa có định mức kinh tế - kỹ thuật , áp dụng các định mức tương ứng của các ngành hoặc của địa phương đã được cơ quan có thẩm quyền ban hành sau khi có ý kiến chấp thuận của Bộ Giao thông vận tải . `[DIEM]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Đường sắt `[LINH_VUC]`)


---

### Mẫu #03_2021_TT-BGTVT_147344#body_standalone_69 (Loại: `body_standalone`)
> **[Điều 14]`<DIEU>`** . **[Khoản 1]`<KHOAN>`** . **[b ) Đối với các hạng mục công trình chưa có định mức kinh tế - kỹ thuật , áp dụng các định mức tương ứng của các ngành hoặc của địa phương đã được **[cơ quan có thẩm quyền]`<CO_QUAN_THAM_QUYEN>`** ban hành sau khi có ý kiến chấp thuận của **[Bộ Giao thông vận tải]`<CO_QUAN_THAM_QUYEN>`** .]`<DIEM>`**

**Thực thể:**
- `[e0]` **Điều 14** → `DIEU` (span: `[0:2]`)
- `[e1]` **Khoản 1** → `KHOAN` (span: `[3:5]`)
- `[e2]` **b ) Đối với các hạng mục công trình chưa có định mức kinh tế - kỹ thuật , áp dụng các định mức tương ứng của các ngành hoặc của địa phương đã được cơ quan có thẩm quyền ban hành sau khi có ý kiến chấp thuận của Bộ Giao thông vận tải .** → `DIEM` (span: `[6:46]`)
- `[e3]` **cơ quan có thẩm quyền** → `CO_QUAN_THAM_QUYEN` (span: `[32:35]`) *(lồng trong `e2` (`DIEM`))*
- `[e4]` **Bộ Giao thông vận tải** → `CO_QUAN_THAM_QUYEN` (span: `[42:45]`) *(lồng trong `e2` (`DIEM`))*

**Quan hệ:**
- (`e1` Khoản 1 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 14 `[DIEU]`)
- (`e2` b ) Đối với các hạng mục công trình chưa có định mức kinh tế - kỹ thuật , áp dụng các định mức tương ứng của các ngành hoặc của địa phương đã được cơ quan có thẩm quyền ban hành sau khi có ý kiến chấp thuận của Bộ Giao thông vận tải . `[DIEM]`) ==[ **THUOC_VE** ]==> (`e1` Khoản 1 `[KHOAN]`)


---

### Mẫu #03_2021_TT-BGTVT_147344#body_context_70 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[03/2021/TT-BGTVT]`<SO_HIEU>`** ban hành **[ngày 08 tháng 02 năm 2021]`<NGAY_BAN_HANH>`** bởi **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** . **[Điều 15]`<DIEU>`** . **[Khoản 1]`<KHOAN>`** . **[b ) Kế hoạch bảo trì công trình đường sắt được lập kèm theo bảng tổng hợp trạng thái kỹ thuật của công trình đường sắt ( theo mẫu **[quy định tại]`<TU_KHOA_PHAP_LY>`** **[Phụ lục 2]`<THAM_CHIEU_PHAP_LY>`** của Thông tư này ) , gửi về Cục Đường sắt Việt Nam trước ngày 15 tháng 6 hàng năm để kiểm tra , rà soát kế hoạch bảo trì và trình **[Bộ Giao thông vận tải]`<CO_QUAN_THAM_QUYEN>`** ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **03/2021/TT-BGTVT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[11:14]`)
- `[e3]` **ngày 08 tháng 02 năm 2021** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 15** → `DIEU` (span: `[15:17]`)
- `[e5]` **Khoản 1** → `KHOAN` (span: `[18:20]`)
- `[e6]` **b ) Kế hoạch bảo trì công trình đường sắt được lập kèm theo bảng tổng hợp trạng thái kỹ thuật của công trình đường sắt ( theo mẫu quy định tại Phụ lục 2 của Thông tư này ) , gửi về Cục Đường sắt Việt Nam trước ngày 15 tháng 6 hàng năm để kiểm tra , rà soát kế hoạch bảo trì và trình Bộ Giao thông vận tải ;** → `DIEM` (span: `[21:74]`)
- `[e7]` **Phụ lục 2** → `THAM_CHIEU_PHAP_LY` (span: `[43:45]`) *(lồng trong `e6` (`DIEM`))*
- `[e8]` **quy định tại** → `TU_KHOA_PHAP_LY` (span: `[41:43]`) *(lồng trong `e6` (`DIEM`))*
- `[e9]` **Bộ Giao thông vận tải** → `CO_QUAN_THAM_QUYEN` (span: `[70:73]`) *(lồng trong `e6` (`DIEM`))*

**Quan hệ:**
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 08 tháng 02 năm 2021 `[NGAY_BAN_HANH]`)
- (`e4` Điều 15 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`)
- (`e5` Khoản 1 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 15 `[DIEU]`)
- (`e6` b ) Kế hoạch bảo trì công trình đường sắt được lập kèm theo bảng tổng hợp trạng thái kỹ thuật của công trình đường sắt ( theo mẫu quy định tại Phụ lục 2 của Thông tư này ) , gửi về Cục Đường sắt Việt Nam trước ngày 15 tháng 6 hàng năm để kiểm tra , rà soát kế hoạch bảo trì và trình Bộ Giao thông vận tải ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e5` Khoản 1 `[KHOAN]`)
- (`e8` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e7` Phụ lục 2 `[THAM_CHIEU_PHAP_LY]`)
- (`e6` b ) Kế hoạch bảo trì công trình đường sắt được lập kèm theo bảng tổng hợp trạng thái kỹ thuật của công trình đường sắt ( theo mẫu quy định tại Phụ lục 2 của Thông tư này ) , gửi về Cục Đường sắt Việt Nam trước ngày 15 tháng 6 hàng năm để kiểm tra , rà soát kế hoạch bảo trì và trình Bộ Giao thông vận tải ; `[DIEM]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e7` Phụ lục 2 `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #03_2021_TT-BGTVT_147344#body_standalone_71 (Loại: `body_standalone`)
> **[Điều 15]`<DIEU>`** . **[Khoản 1]`<KHOAN>`** . **[b ) Kế hoạch bảo trì công trình đường sắt được lập kèm theo bảng tổng hợp trạng thái kỹ thuật của công trình đường sắt ( theo mẫu **[quy định tại]`<TU_KHOA_PHAP_LY>`** **[Phụ lục 2]`<THAM_CHIEU_PHAP_LY>`** của Thông tư này ) , gửi về Cục Đường sắt Việt Nam trước ngày 15 tháng 6 hàng năm để kiểm tra , rà soát kế hoạch bảo trì và trình **[Bộ Giao thông vận tải]`<CO_QUAN_THAM_QUYEN>`** ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Điều 15** → `DIEU` (span: `[0:2]`)
- `[e1]` **Khoản 1** → `KHOAN` (span: `[3:5]`)
- `[e2]` **b ) Kế hoạch bảo trì công trình đường sắt được lập kèm theo bảng tổng hợp trạng thái kỹ thuật của công trình đường sắt ( theo mẫu quy định tại Phụ lục 2 của Thông tư này ) , gửi về Cục Đường sắt Việt Nam trước ngày 15 tháng 6 hàng năm để kiểm tra , rà soát kế hoạch bảo trì và trình Bộ Giao thông vận tải ;** → `DIEM` (span: `[6:59]`)
- `[e3]` **Phụ lục 2** → `THAM_CHIEU_PHAP_LY` (span: `[28:30]`) *(lồng trong `e2` (`DIEM`))*
- `[e4]` **quy định tại** → `TU_KHOA_PHAP_LY` (span: `[26:28]`) *(lồng trong `e2` (`DIEM`))*
- `[e5]` **Bộ Giao thông vận tải** → `CO_QUAN_THAM_QUYEN` (span: `[55:58]`) *(lồng trong `e2` (`DIEM`))*

**Quan hệ:**
- (`e1` Khoản 1 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 15 `[DIEU]`)
- (`e2` b ) Kế hoạch bảo trì công trình đường sắt được lập kèm theo bảng tổng hợp trạng thái kỹ thuật của công trình đường sắt ( theo mẫu quy định tại Phụ lục 2 của Thông tư này ) , gửi về Cục Đường sắt Việt Nam trước ngày 15 tháng 6 hàng năm để kiểm tra , rà soát kế hoạch bảo trì và trình Bộ Giao thông vận tải ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e1` Khoản 1 `[KHOAN]`)
- (`e4` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Phụ lục 2 `[THAM_CHIEU_PHAP_LY]`)
- (`e2` b ) Kế hoạch bảo trì công trình đường sắt được lập kèm theo bảng tổng hợp trạng thái kỹ thuật của công trình đường sắt ( theo mẫu quy định tại Phụ lục 2 của Thông tư này ) , gửi về Cục Đường sắt Việt Nam trước ngày 15 tháng 6 hàng năm để kiểm tra , rà soát kế hoạch bảo trì và trình Bộ Giao thông vận tải ; `[DIEM]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Phụ lục 2 `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #03_2021_TT-BGTVT_147344#body_context_72 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[03/2021/TT-BGTVT]`<SO_HIEU>`** của **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Đường sắt]`<LINH_VUC>`** . **[Điều 15]`<DIEU>`** . **[Khoản 2]`<KHOAN>`** . **[a ) **[Trong thời gian 10 ngày làm việc]`<THOI_HAN>`** kể từ ngày nhận đủ hồ sơ , Cục Đường sắt Việt Nam chịu trách nhiệm kiểm tra , rà soát và trình **[Bộ Giao thông vận tải]`<CO_QUAN_THAM_QUYEN>`** kế hoạch bảo trì công trình đường sắt ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **03/2021/TT-BGTVT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[4:7]`)
- `[e3]` **Đường sắt** → `LINH_VUC` (span: `[9:10]`)
- `[e4]` **Điều 15** → `DIEU` (span: `[11:13]`)
- `[e5]` **Khoản 2** → `KHOAN` (span: `[14:16]`)
- `[e6]` **a ) Trong thời gian 10 ngày làm việc kể từ ngày nhận đủ hồ sơ , Cục Đường sắt Việt Nam chịu trách nhiệm kiểm tra , rà soát và trình Bộ Giao thông vận tải kế hoạch bảo trì công trình đường sắt ;** → `DIEM` (span: `[17:49]`)
- `[e7]` **Trong thời gian 10 ngày làm việc** → `THOI_HAN` (span: `[19:24]`) *(lồng trong `e6` (`DIEM`))*
- `[e8]` **Bộ Giao thông vận tải** → `CO_QUAN_THAM_QUYEN` (span: `[41:44]`) *(lồng trong `e6` (`DIEM`))*

**Quan hệ:**
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Đường sắt `[LINH_VUC]`)
- (`e4` Điều 15 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`)
- (`e5` Khoản 2 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 15 `[DIEU]`)
- (`e6` a ) Trong thời gian 10 ngày làm việc kể từ ngày nhận đủ hồ sơ , Cục Đường sắt Việt Nam chịu trách nhiệm kiểm tra , rà soát và trình Bộ Giao thông vận tải kế hoạch bảo trì công trình đường sắt ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e5` Khoản 2 `[KHOAN]`)
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Đường sắt `[LINH_VUC]`)
- (`e6` a ) Trong thời gian 10 ngày làm việc kể từ ngày nhận đủ hồ sơ , Cục Đường sắt Việt Nam chịu trách nhiệm kiểm tra , rà soát và trình Bộ Giao thông vận tải kế hoạch bảo trì công trình đường sắt ; `[DIEM]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Đường sắt `[LINH_VUC]`)


---

### Mẫu #03_2021_TT-BGTVT_147344#body_standalone_73 (Loại: `body_standalone`)
> **[Điều 15]`<DIEU>`** . **[Khoản 2]`<KHOAN>`** . **[a ) **[Trong thời gian 10 ngày làm việc]`<THOI_HAN>`** kể từ ngày nhận đủ hồ sơ , Cục Đường sắt Việt Nam chịu trách nhiệm kiểm tra , rà soát và trình **[Bộ Giao thông vận tải]`<CO_QUAN_THAM_QUYEN>`** kế hoạch bảo trì công trình đường sắt ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Điều 15** → `DIEU` (span: `[0:2]`)
- `[e1]` **Khoản 2** → `KHOAN` (span: `[3:5]`)
- `[e2]` **a ) Trong thời gian 10 ngày làm việc kể từ ngày nhận đủ hồ sơ , Cục Đường sắt Việt Nam chịu trách nhiệm kiểm tra , rà soát và trình Bộ Giao thông vận tải kế hoạch bảo trì công trình đường sắt ;** → `DIEM` (span: `[6:38]`)
- `[e3]` **Trong thời gian 10 ngày làm việc** → `THOI_HAN` (span: `[8:13]`) *(lồng trong `e2` (`DIEM`))*
- `[e4]` **Bộ Giao thông vận tải** → `CO_QUAN_THAM_QUYEN` (span: `[30:33]`) *(lồng trong `e2` (`DIEM`))*

**Quan hệ:**
- (`e1` Khoản 2 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 15 `[DIEU]`)
- (`e2` a ) Trong thời gian 10 ngày làm việc kể từ ngày nhận đủ hồ sơ , Cục Đường sắt Việt Nam chịu trách nhiệm kiểm tra , rà soát và trình Bộ Giao thông vận tải kế hoạch bảo trì công trình đường sắt ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e1` Khoản 2 `[KHOAN]`)


---

### Mẫu #03_2021_TT-BGTVT_147344#body_context_74 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[03/2021/TT-BGTVT]`<SO_HIEU>`** ban hành **[ngày 08 tháng 02 năm 2021]`<NGAY_BAN_HANH>`** bởi **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** . **[Điều 15]`<DIEU>`** . **[Khoản 2]`<KHOAN>`** . **[b ) Trên cơ sở kế hoạch bảo trì công trình đường sắt do Cục Đường sắt Việt Nam trình , **[Bộ Giao thông vận tải]`<CO_QUAN_THAM_QUYEN>`** rà soát , tổng hợp kế hoạch và dự toán kinh phí bảo trì công trình đường sắt vào dự toán thu , chi **[ngân sách nhà nước]`<TAI_SAN_VAT_CHAT>`** hàng năm của **[Bộ Giao thông vận tải]`<CO_QUAN_THAM_QUYEN>`** , gửi **[Bộ Tài chính]`<CO_QUAN_THAM_QUYEN>`** trước ngày 20 tháng 7 hàng năm ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **03/2021/TT-BGTVT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[11:14]`)
- `[e3]` **ngày 08 tháng 02 năm 2021** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 15** → `DIEU` (span: `[15:17]`)
- `[e5]` **Khoản 2** → `KHOAN` (span: `[18:20]`)
- `[e6]` **b ) Trên cơ sở kế hoạch bảo trì công trình đường sắt do Cục Đường sắt Việt Nam trình , Bộ Giao thông vận tải rà soát , tổng hợp kế hoạch và dự toán kinh phí bảo trì công trình đường sắt vào dự toán thu , chi ngân sách nhà nước hàng năm của Bộ Giao thông vận tải , gửi Bộ Tài chính trước ngày 20 tháng 7 hàng năm ;** → `DIEM` (span: `[21:71]`)
- `[e7]` **Bộ Giao thông vận tải** → `CO_QUAN_THAM_QUYEN` (span: `[33:36]`) *(lồng trong `e6` (`DIEM`))*
- `[e8]` **Bộ Giao thông vận tải** → `CO_QUAN_THAM_QUYEN` (span: `[56:59]`) *(lồng trong `e6` (`DIEM`))*
- `[e9]` **Bộ Tài chính** → `CO_QUAN_THAM_QUYEN` (span: `[61:63]`) *(lồng trong `e6` (`DIEM`))*
- `[e10]` **ngân sách nhà nước** → `TAI_SAN_VAT_CHAT` (span: `[51:53]`) *(lồng trong `e6` (`DIEM`))*

**Quan hệ:**
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 08 tháng 02 năm 2021 `[NGAY_BAN_HANH]`)
- (`e4` Điều 15 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`)
- (`e5` Khoản 2 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 15 `[DIEU]`)
- (`e6` b ) Trên cơ sở kế hoạch bảo trì công trình đường sắt do Cục Đường sắt Việt Nam trình , Bộ Giao thông vận tải rà soát , tổng hợp kế hoạch và dự toán kinh phí bảo trì công trình đường sắt vào dự toán thu , chi ngân sách nhà nước hàng năm của Bộ Giao thông vận tải , gửi Bộ Tài chính trước ngày 20 tháng 7 hàng năm ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e5` Khoản 2 `[KHOAN]`)


---

### Mẫu #03_2021_TT-BGTVT_147344#body_standalone_75 (Loại: `body_standalone`)
> **[Điều 15]`<DIEU>`** . **[Khoản 2]`<KHOAN>`** . **[b ) Trên cơ sở kế hoạch bảo trì công trình đường sắt do Cục Đường sắt Việt Nam trình , **[Bộ Giao thông vận tải]`<CO_QUAN_THAM_QUYEN>`** rà soát , tổng hợp kế hoạch và dự toán kinh phí bảo trì công trình đường sắt vào dự toán thu , chi **[ngân sách nhà nước]`<TAI_SAN_VAT_CHAT>`** hàng năm của **[Bộ Giao thông vận tải]`<CO_QUAN_THAM_QUYEN>`** , gửi **[Bộ Tài chính]`<CO_QUAN_THAM_QUYEN>`** trước ngày 20 tháng 7 hàng năm ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Điều 15** → `DIEU` (span: `[0:2]`)
- `[e1]` **Khoản 2** → `KHOAN` (span: `[3:5]`)
- `[e2]` **b ) Trên cơ sở kế hoạch bảo trì công trình đường sắt do Cục Đường sắt Việt Nam trình , Bộ Giao thông vận tải rà soát , tổng hợp kế hoạch và dự toán kinh phí bảo trì công trình đường sắt vào dự toán thu , chi ngân sách nhà nước hàng năm của Bộ Giao thông vận tải , gửi Bộ Tài chính trước ngày 20 tháng 7 hàng năm ;** → `DIEM` (span: `[6:56]`)
- `[e3]` **Bộ Giao thông vận tải** → `CO_QUAN_THAM_QUYEN` (span: `[18:21]`) *(lồng trong `e2` (`DIEM`))*
- `[e4]` **Bộ Giao thông vận tải** → `CO_QUAN_THAM_QUYEN` (span: `[41:44]`) *(lồng trong `e2` (`DIEM`))*
- `[e5]` **Bộ Tài chính** → `CO_QUAN_THAM_QUYEN` (span: `[46:48]`) *(lồng trong `e2` (`DIEM`))*
- `[e6]` **ngân sách nhà nước** → `TAI_SAN_VAT_CHAT` (span: `[36:38]`) *(lồng trong `e2` (`DIEM`))*

**Quan hệ:**
- (`e1` Khoản 2 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 15 `[DIEU]`)
- (`e2` b ) Trên cơ sở kế hoạch bảo trì công trình đường sắt do Cục Đường sắt Việt Nam trình , Bộ Giao thông vận tải rà soát , tổng hợp kế hoạch và dự toán kinh phí bảo trì công trình đường sắt vào dự toán thu , chi ngân sách nhà nước hàng năm của Bộ Giao thông vận tải , gửi Bộ Tài chính trước ngày 20 tháng 7 hàng năm ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e1` Khoản 2 `[KHOAN]`)


---

### Mẫu #03_2021_TT-BGTVT_147344#body_context_76 (Loại: `body_context`)
> **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[03/2021/TT-BGTVT]`<SO_HIEU>`** . **[Điều 15]`<DIEU>`** . **[Khoản 2]`<KHOAN>`** . **[c ) Sau khi có thông báo của **[Bộ Tài chính]`<CO_QUAN_THAM_QUYEN>`** về dự toán thu , chi ngân sách hàng năm và thông báo số dự toán thu , chi **[ngân sách nhà nước]`<TAI_SAN_VAT_CHAT>`** của **[Bộ Giao thông vận tải]`<CO_QUAN_THAM_QUYEN>`** , **[doanh nghiệp kinh doanh kết cấu hạ tầng đường sắt rà soát]`<TO_CHUC_DOANH_NGHIEP>`** , điều chỉnh kế hoạch và dự toán kinh phí bảo trì công trình đường sắt phù hợp với nguồn kinh phí được thông báo ; lập hồ sơ và gửi đến Cục Đường sắt Việt Nam để kiểm tra , rà soát]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[4:5]`)
- `[e1]` **03/2021/TT-BGTVT** → `SO_HIEU` (span: `[6:7]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[0:3]`)
- `[e3]` **Điều 15** → `DIEU` (span: `[8:10]`)
- `[e4]` **Khoản 2** → `KHOAN` (span: `[11:13]`)
- `[e5]` **c ) Sau khi có thông báo của Bộ Tài chính về dự toán thu , chi ngân sách hàng năm và thông báo số dự toán thu , chi ngân sách nhà nước của Bộ Giao thông vận tải , doanh nghiệp kinh doanh kết cấu hạ tầng đường sắt rà soát , điều chỉnh kế hoạch và dự toán kinh phí bảo trì công trình đường sắt phù hợp với nguồn kinh phí được thông báo ; lập hồ sơ và gửi đến Cục Đường sắt Việt Nam để kiểm tra , rà soát** → `DIEM` (span: `[14:78]`)
- `[e6]` **Bộ Tài chính** → `CO_QUAN_THAM_QUYEN` (span: `[21:23]`) *(lồng trong `e5` (`DIEM`))*
- `[e7]` **Bộ Giao thông vận tải** → `CO_QUAN_THAM_QUYEN` (span: `[41:44]`) *(lồng trong `e5` (`DIEM`))*
- `[e8]` **ngân sách nhà nước** → `TAI_SAN_VAT_CHAT` (span: `[38:40]`) *(lồng trong `e5` (`DIEM`))*
- `[e9]` **doanh nghiệp kinh doanh kết cấu hạ tầng đường sắt rà soát** → `TO_CHUC_DOANH_NGHIEP` (span: `[45:50]`) *(lồng trong `e5` (`DIEM`))*

**Quan hệ:**
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 15 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`)
- (`e4` Khoản 2 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 15 `[DIEU]`)
- (`e5` c ) Sau khi có thông báo của Bộ Tài chính về dự toán thu , chi ngân sách hàng năm và thông báo số dự toán thu , chi ngân sách nhà nước của Bộ Giao thông vận tải , doanh nghiệp kinh doanh kết cấu hạ tầng đường sắt rà soát , điều chỉnh kế hoạch và dự toán kinh phí bảo trì công trình đường sắt phù hợp với nguồn kinh phí được thông báo ; lập hồ sơ và gửi đến Cục Đường sắt Việt Nam để kiểm tra , rà soát `[DIEM]`) ==[ **THUOC_VE** ]==> (`e4` Khoản 2 `[KHOAN]`)


---

### Mẫu #03_2021_TT-BGTVT_147344#body_standalone_77 (Loại: `body_standalone`)
> **[Điều 15]`<DIEU>`** . **[Khoản 2]`<KHOAN>`** . **[c ) Sau khi có thông báo của **[Bộ Tài chính]`<CO_QUAN_THAM_QUYEN>`** về dự toán thu , chi ngân sách hàng năm và thông báo số dự toán thu , chi **[ngân sách nhà nước]`<TAI_SAN_VAT_CHAT>`** của **[Bộ Giao thông vận tải]`<CO_QUAN_THAM_QUYEN>`** , **[doanh nghiệp kinh doanh kết cấu hạ tầng đường sắt rà soát]`<TO_CHUC_DOANH_NGHIEP>`** , điều chỉnh kế hoạch và dự toán kinh phí bảo trì công trình đường sắt phù hợp với nguồn kinh phí được thông báo ; lập hồ sơ và gửi đến Cục Đường sắt Việt Nam để kiểm tra , rà soát]`<DIEM>`**

**Thực thể:**
- `[e0]` **Điều 15** → `DIEU` (span: `[0:2]`)
- `[e1]` **Khoản 2** → `KHOAN` (span: `[3:5]`)
- `[e2]` **c ) Sau khi có thông báo của Bộ Tài chính về dự toán thu , chi ngân sách hàng năm và thông báo số dự toán thu , chi ngân sách nhà nước của Bộ Giao thông vận tải , doanh nghiệp kinh doanh kết cấu hạ tầng đường sắt rà soát , điều chỉnh kế hoạch và dự toán kinh phí bảo trì công trình đường sắt phù hợp với nguồn kinh phí được thông báo ; lập hồ sơ và gửi đến Cục Đường sắt Việt Nam để kiểm tra , rà soát** → `DIEM` (span: `[6:70]`)
- `[e3]` **Bộ Tài chính** → `CO_QUAN_THAM_QUYEN` (span: `[13:15]`) *(lồng trong `e2` (`DIEM`))*
- `[e4]` **Bộ Giao thông vận tải** → `CO_QUAN_THAM_QUYEN` (span: `[33:36]`) *(lồng trong `e2` (`DIEM`))*
- `[e5]` **ngân sách nhà nước** → `TAI_SAN_VAT_CHAT` (span: `[30:32]`) *(lồng trong `e2` (`DIEM`))*
- `[e6]` **doanh nghiệp kinh doanh kết cấu hạ tầng đường sắt rà soát** → `TO_CHUC_DOANH_NGHIEP` (span: `[37:42]`) *(lồng trong `e2` (`DIEM`))*

**Quan hệ:**
- (`e1` Khoản 2 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 15 `[DIEU]`)
- (`e2` c ) Sau khi có thông báo của Bộ Tài chính về dự toán thu , chi ngân sách hàng năm và thông báo số dự toán thu , chi ngân sách nhà nước của Bộ Giao thông vận tải , doanh nghiệp kinh doanh kết cấu hạ tầng đường sắt rà soát , điều chỉnh kế hoạch và dự toán kinh phí bảo trì công trình đường sắt phù hợp với nguồn kinh phí được thông báo ; lập hồ sơ và gửi đến Cục Đường sắt Việt Nam để kiểm tra , rà soát `[DIEM]`) ==[ **THUOC_VE** ]==> (`e1` Khoản 2 `[KHOAN]`)


---

### Mẫu #03_2021_TT-BGTVT_147344#body_context_78 (Loại: `body_context`)
> **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[03/2021/TT-BGTVT]`<SO_HIEU>`** . **[Điều 15]`<DIEU>`** . **[Khoản 2]`<KHOAN>`** . **[d ) **[Bộ Giao thông vận tải]`<CO_QUAN_THAM_QUYEN>`** thẩm định , phê duyệt kế hoạch , dự toán kinh phí bảo trì công trình đường sắt sau khi nhận đầy đủ hồ sơ kế hoạch bảo trì công trình đường sắt , báo cáo thẩm tra và ý kiến góp ý của các cơ quan , đơn vị liên quan ( nếu có ) .]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[4:5]`)
- `[e1]` **03/2021/TT-BGTVT** → `SO_HIEU` (span: `[6:7]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[0:3]`)
- `[e3]` **Điều 15** → `DIEU` (span: `[8:10]`)
- `[e4]` **Khoản 2** → `KHOAN` (span: `[11:13]`)
- `[e5]` **d ) Bộ Giao thông vận tải thẩm định , phê duyệt kế hoạch , dự toán kinh phí bảo trì công trình đường sắt sau khi nhận đầy đủ hồ sơ kế hoạch bảo trì công trình đường sắt , báo cáo thẩm tra và ý kiến góp ý của các cơ quan , đơn vị liên quan ( nếu có ) .** → `DIEM` (span: `[14:55]`)
- `[e6]` **Bộ Giao thông vận tải** → `CO_QUAN_THAM_QUYEN` (span: `[16:19]`) *(lồng trong `e5` (`DIEM`))*

**Quan hệ:**
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 15 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`)
- (`e4` Khoản 2 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 15 `[DIEU]`)
- (`e5` d ) Bộ Giao thông vận tải thẩm định , phê duyệt kế hoạch , dự toán kinh phí bảo trì công trình đường sắt sau khi nhận đầy đủ hồ sơ kế hoạch bảo trì công trình đường sắt , báo cáo thẩm tra và ý kiến góp ý của các cơ quan , đơn vị liên quan ( nếu có ) . `[DIEM]`) ==[ **THUOC_VE** ]==> (`e4` Khoản 2 `[KHOAN]`)


---

### Mẫu #03_2021_TT-BGTVT_147344#body_context_79 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[03/2021/TT-BGTVT]`<SO_HIEU>`** của **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Đường sắt]`<LINH_VUC>`** . **[Điều 15]`<DIEU>`** . **[Khoản 3]`<KHOAN>`** . **[b ) **[Doanh nghiệp kinh doanh kết cấu hạ tầng đường sắt lập hồ sơ điều chỉn]`<TO_CHUC_DOANH_NGHIEP>`** h kế hoạch bảo trì công trình đường sắt , gửi về Cục Đường sắt Việt Nam trước ngày 01 tháng 10 hàng năm . Cục Đường sắt Việt Nam kiểm tra , rà soát , trình **[Bộ Giao thông vận tải]`<CO_QUAN_THAM_QUYEN>`** trước ngày 15 tháng 10 hàng năm để xem xét , quyết định ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **03/2021/TT-BGTVT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[4:7]`)
- `[e3]` **Đường sắt** → `LINH_VUC` (span: `[9:10]`)
- `[e4]` **Điều 15** → `DIEU` (span: `[11:13]`)
- `[e5]` **Khoản 3** → `KHOAN` (span: `[14:16]`)
- `[e6]` **b ) Doanh nghiệp kinh doanh kết cấu hạ tầng đường sắt lập hồ sơ điều chỉn h kế hoạch bảo trì công trình đường sắt , gửi về Cục Đường sắt Việt Nam trước ngày 01 tháng 10 hàng năm . Cục Đường sắt Việt Nam kiểm tra , rà soát , trình Bộ Giao thông vận tải trước ngày 15 tháng 10 hàng năm để xem xét , quyết định ;** → `DIEM` (span: `[17:69]`)
- `[e7]` **Bộ Giao thông vận tải** → `CO_QUAN_THAM_QUYEN` (span: `[54:57]`) *(lồng trong `e6` (`DIEM`))*
- `[e8]` **Doanh nghiệp kinh doanh kết cấu hạ tầng đường sắt lập hồ sơ điều chỉn** → `TO_CHUC_DOANH_NGHIEP` (span: `[19:27]`) *(lồng trong `e6` (`DIEM`))*

**Quan hệ:**
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Đường sắt `[LINH_VUC]`)
- (`e4` Điều 15 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`)
- (`e5` Khoản 3 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 15 `[DIEU]`)
- (`e6` b ) Doanh nghiệp kinh doanh kết cấu hạ tầng đường sắt lập hồ sơ điều chỉn h kế hoạch bảo trì công trình đường sắt , gửi về Cục Đường sắt Việt Nam trước ngày 01 tháng 10 hàng năm . Cục Đường sắt Việt Nam kiểm tra , rà soát , trình Bộ Giao thông vận tải trước ngày 15 tháng 10 hàng năm để xem xét , quyết định ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e5` Khoản 3 `[KHOAN]`)
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Đường sắt `[LINH_VUC]`)
- (`e6` b ) Doanh nghiệp kinh doanh kết cấu hạ tầng đường sắt lập hồ sơ điều chỉn h kế hoạch bảo trì công trình đường sắt , gửi về Cục Đường sắt Việt Nam trước ngày 01 tháng 10 hàng năm . Cục Đường sắt Việt Nam kiểm tra , rà soát , trình Bộ Giao thông vận tải trước ngày 15 tháng 10 hàng năm để xem xét , quyết định ; `[DIEM]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Đường sắt `[LINH_VUC]`)


---

### Mẫu #03_2021_TT-BGTVT_147344#body_standalone_80 (Loại: `body_standalone`)
> **[Điều 15]`<DIEU>`** . **[Khoản 3]`<KHOAN>`** . **[b ) **[Doanh nghiệp kinh doanh kết cấu hạ tầng đường sắt lập hồ sơ điều chỉn]`<TO_CHUC_DOANH_NGHIEP>`** h kế hoạch bảo trì công trình đường sắt , gửi về Cục Đường sắt Việt Nam trước ngày 01 tháng 10 hàng năm . Cục Đường sắt Việt Nam kiểm tra , rà soát , trình **[Bộ Giao thông vận tải]`<CO_QUAN_THAM_QUYEN>`** trước ngày 15 tháng 10 hàng năm để xem xét , quyết định ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Điều 15** → `DIEU` (span: `[0:2]`)
- `[e1]` **Khoản 3** → `KHOAN` (span: `[3:5]`)
- `[e2]` **b ) Doanh nghiệp kinh doanh kết cấu hạ tầng đường sắt lập hồ sơ điều chỉn h kế hoạch bảo trì công trình đường sắt , gửi về Cục Đường sắt Việt Nam trước ngày 01 tháng 10 hàng năm . Cục Đường sắt Việt Nam kiểm tra , rà soát , trình Bộ Giao thông vận tải trước ngày 15 tháng 10 hàng năm để xem xét , quyết định ;** → `DIEM` (span: `[6:58]`)
- `[e3]` **Bộ Giao thông vận tải** → `CO_QUAN_THAM_QUYEN` (span: `[43:46]`) *(lồng trong `e2` (`DIEM`))*
- `[e4]` **Doanh nghiệp kinh doanh kết cấu hạ tầng đường sắt lập hồ sơ điều chỉn** → `TO_CHUC_DOANH_NGHIEP` (span: `[8:16]`) *(lồng trong `e2` (`DIEM`))*

**Quan hệ:**
- (`e1` Khoản 3 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 15 `[DIEU]`)
- (`e2` b ) Doanh nghiệp kinh doanh kết cấu hạ tầng đường sắt lập hồ sơ điều chỉn h kế hoạch bảo trì công trình đường sắt , gửi về Cục Đường sắt Việt Nam trước ngày 01 tháng 10 hàng năm . Cục Đường sắt Việt Nam kiểm tra , rà soát , trình Bộ Giao thông vận tải trước ngày 15 tháng 10 hàng năm để xem xét , quyết định ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e1` Khoản 3 `[KHOAN]`)


---

### Mẫu #03_2021_TT-BGTVT_147344#body_context_81 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[03/2021/TT-BGTVT]`<SO_HIEU>`** ban hành **[ngày 08 tháng 02 năm 2021]`<NGAY_BAN_HANH>`** bởi **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** . **[Chương I]`<CHUONG>`** . **[Điều 1 . Phạm vi Điều chỉnh]`<DIEU>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **03/2021/TT-BGTVT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[11:14]`)
- `[e3]` **ngày 08 tháng 02 năm 2021** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Chương I** → `CHUONG` (span: `[15:17]`)
- `[e5]` **Điều 1 . Phạm vi Điều chỉnh** → `DIEU` (span: `[18:23]`)

**Quan hệ:**
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 08 tháng 02 năm 2021 `[NGAY_BAN_HANH]`)
- (`e4` Chương I `[CHUONG]`) ==[ **THUOC_VE** ]==> (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`)
- (`e5` Điều 1 . Phạm vi Điều chỉnh `[DIEU]`) ==[ **THUOC_VE** ]==> (`e4` Chương I `[CHUONG]`)


---

### Mẫu #03_2021_TT-BGTVT_147344#body_context_82 (Loại: `body_context`)
> **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[03/2021/TT-BGTVT]`<SO_HIEU>`** . **[Điều 17 . Kiểm tra , bảo dưỡng , sửa chữa và đánh giá sự an toàn công trình đường sắt]`<DIEU>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[4:5]`)
- `[e1]` **03/2021/TT-BGTVT** → `SO_HIEU` (span: `[6:7]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[0:3]`)
- `[e3]` **Điều 17 . Kiểm tra , bảo dưỡng , sửa chữa và đánh giá sự an toàn công trình đường sắt** → `DIEU` (span: `[8:22]`)

**Quan hệ:**
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 17 . Kiểm tra , bảo dưỡng , sửa chữa và đánh giá sự an toàn công trình đường sắt `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`)


---

### Mẫu #03_2021_TT-BGTVT_147344#body_context_83 (Loại: `body_context`)
> **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[03/2021/TT-BGTVT]`<SO_HIEU>`** . **[Điều 17]`<DIEU>`** . **[2 . Việc kiểm tra , bảo dưỡng , sửa chữa công trình đường sắt ; đánh giá an toàn công trình đường sắt trong quá trình khai thác , sử dụng bao gồm an toàn chịu lực và an toàn vận hành được thực hiện theo quy định của pháp luật về quản lý chất lượng và bảo trì công trình xây dựng và **[quy định tại]`<TU_KHOA_PHAP_LY>`** **[Thông tư này]`<THAM_CHIEU_PHAP_LY>`** .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[4:5]`)
- `[e1]` **03/2021/TT-BGTVT** → `SO_HIEU` (span: `[6:7]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[0:3]`)
- `[e3]` **Điều 17** → `DIEU` (span: `[8:10]`)
- `[e4]` **2 . Việc kiểm tra , bảo dưỡng , sửa chữa công trình đường sắt ; đánh giá an toàn công trình đường sắt trong quá trình khai thác , sử dụng bao gồm an toàn chịu lực và an toàn vận hành được thực hiện theo quy định của pháp luật về quản lý chất lượng và bảo trì công trình xây dựng và quy định tại Thông tư này .** → `KHOAN` (span: `[11:57]`)
- `[e5]` **Thông tư này** → `THAM_CHIEU_PHAP_LY` (span: `[54:56]`) *(lồng trong `e4` (`KHOAN`))*
- `[e6]` **quy định tại** → `TU_KHOA_PHAP_LY` (span: `[52:54]`) *(lồng trong `e4` (`KHOAN`))*

**Quan hệ:**
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 17 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`)
- (`e4` 2 . Việc kiểm tra , bảo dưỡng , sửa chữa công trình đường sắt ; đánh giá an toàn công trình đường sắt trong quá trình khai thác , sử dụng bao gồm an toàn chịu lực và an toàn vận hành được thực hiện theo quy định của pháp luật về quản lý chất lượng và bảo trì công trình xây dựng và quy định tại Thông tư này . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 17 `[DIEU]`)
- (`e6` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e5` Thông tư này `[THAM_CHIEU_PHAP_LY]`)
- (`e4` 2 . Việc kiểm tra , bảo dưỡng , sửa chữa công trình đường sắt ; đánh giá an toàn công trình đường sắt trong quá trình khai thác , sử dụng bao gồm an toàn chịu lực và an toàn vận hành được thực hiện theo quy định của pháp luật về quản lý chất lượng và bảo trì công trình xây dựng và quy định tại Thông tư này . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e5` Thông tư này `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #03_2021_TT-BGTVT_147344#body_standalone_84 (Loại: `body_standalone`)
> **[Điều 17]`<DIEU>`** . **[2 . Việc kiểm tra , bảo dưỡng , sửa chữa công trình đường sắt ; đánh giá an toàn công trình đường sắt trong quá trình khai thác , sử dụng bao gồm an toàn chịu lực và an toàn vận hành được thực hiện theo quy định của pháp luật về quản lý chất lượng và bảo trì công trình xây dựng và **[quy định tại]`<TU_KHOA_PHAP_LY>`** **[Thông tư này]`<THAM_CHIEU_PHAP_LY>`** .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 17** → `DIEU` (span: `[0:2]`)
- `[e1]` **2 . Việc kiểm tra , bảo dưỡng , sửa chữa công trình đường sắt ; đánh giá an toàn công trình đường sắt trong quá trình khai thác , sử dụng bao gồm an toàn chịu lực và an toàn vận hành được thực hiện theo quy định của pháp luật về quản lý chất lượng và bảo trì công trình xây dựng và quy định tại Thông tư này .** → `KHOAN` (span: `[3:49]`)
- `[e2]` **Thông tư này** → `THAM_CHIEU_PHAP_LY` (span: `[46:48]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **quy định tại** → `TU_KHOA_PHAP_LY` (span: `[44:46]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 2 . Việc kiểm tra , bảo dưỡng , sửa chữa công trình đường sắt ; đánh giá an toàn công trình đường sắt trong quá trình khai thác , sử dụng bao gồm an toàn chịu lực và an toàn vận hành được thực hiện theo quy định của pháp luật về quản lý chất lượng và bảo trì công trình xây dựng và quy định tại Thông tư này . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 17 `[DIEU]`)
- (`e3` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e2` Thông tư này `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 2 . Việc kiểm tra , bảo dưỡng , sửa chữa công trình đường sắt ; đánh giá an toàn công trình đường sắt trong quá trình khai thác , sử dụng bao gồm an toàn chịu lực và an toàn vận hành được thực hiện theo quy định của pháp luật về quản lý chất lượng và bảo trì công trình xây dựng và quy định tại Thông tư này . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e2` Thông tư này `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #03_2021_TT-BGTVT_147344#body_context_85 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[03/2021/TT-BGTVT]`<SO_HIEU>`** ban hành **[ngày 08 tháng 02 năm 2021]`<NGAY_BAN_HANH>`** bởi **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** . **[Điều 18]`<DIEU>`** . **[1 . Cục Đường sắt Việt Nam , **[Doanh nghiệp kinh doanh kết cấu hạ tầng đường sắt]`<TO_CHUC_DOANH_NGHIEP>`** , tổ chức , cá nhân nhận chuyển nhượng có thời hạn , thuê quyền khai thác , kinh doanh kết cấu hạ tầng đường sắt quốc gia do nhà nước đầu tư , nhà cung cấp dịch vụ sự nghiệp công sử dụng kinh phí **[ngân sách nhà nước]`<TAI_SAN_VAT_CHAT>`** và các tổ chức , cá nhân có liên quan đến công tác bảo trì công trình đường sắt chịu trách nhiệm thực hiện quản lý chất lượng theo quy định của]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **03/2021/TT-BGTVT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[11:14]`)
- `[e3]` **ngày 08 tháng 02 năm 2021** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 18** → `DIEU` (span: `[15:17]`)
- `[e5]` **1 . Cục Đường sắt Việt Nam , Doanh nghiệp kinh doanh kết cấu hạ tầng đường sắt , tổ chức , cá nhân nhận chuyển nhượng có thời hạn , thuê quyền khai thác , kinh doanh kết cấu hạ tầng đường sắt quốc gia do nhà nước đầu tư , nhà cung cấp dịch vụ sự nghiệp công sử dụng kinh phí ngân sách nhà nước và các tổ chức , cá nhân có liên quan đến công tác bảo trì công trình đường sắt chịu trách nhiệm thực hiện quản lý chất lượng theo quy định của** → `KHOAN` (span: `[18:78]`)
- `[e6]` **ngân sách nhà nước** → `TAI_SAN_VAT_CHAT` (span: `[56:58]`) *(lồng trong `e5` (`KHOAN`))*
- `[e7]` **Doanh nghiệp kinh doanh kết cấu hạ tầng đường sắt** → `TO_CHUC_DOANH_NGHIEP` (span: `[24:28]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 08 tháng 02 năm 2021 `[NGAY_BAN_HANH]`)
- (`e4` Điều 18 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`)
- (`e5` 1 . Cục Đường sắt Việt Nam , Doanh nghiệp kinh doanh kết cấu hạ tầng đường sắt , tổ chức , cá nhân nhận chuyển nhượng có thời hạn , thuê quyền khai thác , kinh doanh kết cấu hạ tầng đường sắt quốc gia do nhà nước đầu tư , nhà cung cấp dịch vụ sự nghiệp công sử dụng kinh phí ngân sách nhà nước và các tổ chức , cá nhân có liên quan đến công tác bảo trì công trình đường sắt chịu trách nhiệm thực hiện quản lý chất lượng theo quy định của `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 18 `[DIEU]`)


---

### Mẫu #03_2021_TT-BGTVT_147344#body_standalone_86 (Loại: `body_standalone`)
> **[Điều 18]`<DIEU>`** . **[1 . Cục Đường sắt Việt Nam , **[Doanh nghiệp kinh doanh kết cấu hạ tầng đường sắt]`<TO_CHUC_DOANH_NGHIEP>`** , tổ chức , cá nhân nhận chuyển nhượng có thời hạn , thuê quyền khai thác , kinh doanh kết cấu hạ tầng đường sắt quốc gia do nhà nước đầu tư , nhà cung cấp dịch vụ sự nghiệp công sử dụng kinh phí **[ngân sách nhà nước]`<TAI_SAN_VAT_CHAT>`** và các tổ chức , cá nhân có liên quan đến công tác bảo trì công trình đường sắt chịu trách nhiệm thực hiện quản lý chất lượng theo quy định của]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 18** → `DIEU` (span: `[0:2]`)
- `[e1]` **1 . Cục Đường sắt Việt Nam , Doanh nghiệp kinh doanh kết cấu hạ tầng đường sắt , tổ chức , cá nhân nhận chuyển nhượng có thời hạn , thuê quyền khai thác , kinh doanh kết cấu hạ tầng đường sắt quốc gia do nhà nước đầu tư , nhà cung cấp dịch vụ sự nghiệp công sử dụng kinh phí ngân sách nhà nước và các tổ chức , cá nhân có liên quan đến công tác bảo trì công trình đường sắt chịu trách nhiệm thực hiện quản lý chất lượng theo quy định của** → `KHOAN` (span: `[3:63]`)
- `[e2]` **ngân sách nhà nước** → `TAI_SAN_VAT_CHAT` (span: `[41:43]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **Doanh nghiệp kinh doanh kết cấu hạ tầng đường sắt** → `TO_CHUC_DOANH_NGHIEP` (span: `[9:13]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 1 . Cục Đường sắt Việt Nam , Doanh nghiệp kinh doanh kết cấu hạ tầng đường sắt , tổ chức , cá nhân nhận chuyển nhượng có thời hạn , thuê quyền khai thác , kinh doanh kết cấu hạ tầng đường sắt quốc gia do nhà nước đầu tư , nhà cung cấp dịch vụ sự nghiệp công sử dụng kinh phí ngân sách nhà nước và các tổ chức , cá nhân có liên quan đến công tác bảo trì công trình đường sắt chịu trách nhiệm thực hiện quản lý chất lượng theo quy định của `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 18 `[DIEU]`)


---

### Mẫu #03_2021_TT-BGTVT_147344#body_context_87 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[03/2021/TT-BGTVT]`<SO_HIEU>`** của **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Đường sắt]`<LINH_VUC>`** . **[Điều 18]`<DIEU>`** . **[6 . Quản lý chất lượng công tác bảo trì công trình đường sắt quốc gia phải thực hiện theo quy chuẩn , tiêu chuẩn kỹ thuật áp dụng và quy định về tiêu chí giám sát , nghiệm thu kết quả bảo trì **[tài sản kết cấu hạ tầng]`<TAI_SAN_VAT_CHAT>`** đường sắt quốc gia của **[Bộ Giao thông vận tải]`<CO_QUAN_THAM_QUYEN>`** .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **03/2021/TT-BGTVT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[4:7]`)
- `[e3]` **Đường sắt** → `LINH_VUC` (span: `[9:10]`)
- `[e4]` **Điều 18** → `DIEU` (span: `[11:13]`)
- `[e5]` **6 . Quản lý chất lượng công tác bảo trì công trình đường sắt quốc gia phải thực hiện theo quy chuẩn , tiêu chuẩn kỹ thuật áp dụng và quy định về tiêu chí giám sát , nghiệm thu kết quả bảo trì tài sản kết cấu hạ tầng đường sắt quốc gia của Bộ Giao thông vận tải .** → `KHOAN` (span: `[14:49]`)
- `[e6]` **Bộ Giao thông vận tải** → `CO_QUAN_THAM_QUYEN` (span: `[45:48]`) *(lồng trong `e5` (`KHOAN`))*
- `[e7]` **tài sản kết cấu hạ tầng** → `TAI_SAN_VAT_CHAT` (span: `[40:42]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Đường sắt `[LINH_VUC]`)
- (`e4` Điều 18 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`)
- (`e5` 6 . Quản lý chất lượng công tác bảo trì công trình đường sắt quốc gia phải thực hiện theo quy chuẩn , tiêu chuẩn kỹ thuật áp dụng và quy định về tiêu chí giám sát , nghiệm thu kết quả bảo trì tài sản kết cấu hạ tầng đường sắt quốc gia của Bộ Giao thông vận tải . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 18 `[DIEU]`)
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Đường sắt `[LINH_VUC]`)
- (`e5` 6 . Quản lý chất lượng công tác bảo trì công trình đường sắt quốc gia phải thực hiện theo quy chuẩn , tiêu chuẩn kỹ thuật áp dụng và quy định về tiêu chí giám sát , nghiệm thu kết quả bảo trì tài sản kết cấu hạ tầng đường sắt quốc gia của Bộ Giao thông vận tải . `[KHOAN]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Đường sắt `[LINH_VUC]`)


---

### Mẫu #03_2021_TT-BGTVT_147344#body_standalone_88 (Loại: `body_standalone`)
> **[Điều 18]`<DIEU>`** . **[6 . Quản lý chất lượng công tác bảo trì công trình đường sắt quốc gia phải thực hiện theo quy chuẩn , tiêu chuẩn kỹ thuật áp dụng và quy định về tiêu chí giám sát , nghiệm thu kết quả bảo trì **[tài sản kết cấu hạ tầng]`<TAI_SAN_VAT_CHAT>`** đường sắt quốc gia của **[Bộ Giao thông vận tải]`<CO_QUAN_THAM_QUYEN>`** .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 18** → `DIEU` (span: `[0:2]`)
- `[e1]` **6 . Quản lý chất lượng công tác bảo trì công trình đường sắt quốc gia phải thực hiện theo quy chuẩn , tiêu chuẩn kỹ thuật áp dụng và quy định về tiêu chí giám sát , nghiệm thu kết quả bảo trì tài sản kết cấu hạ tầng đường sắt quốc gia của Bộ Giao thông vận tải .** → `KHOAN` (span: `[3:38]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_THAM_QUYEN` (span: `[34:37]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **tài sản kết cấu hạ tầng** → `TAI_SAN_VAT_CHAT` (span: `[29:31]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 6 . Quản lý chất lượng công tác bảo trì công trình đường sắt quốc gia phải thực hiện theo quy chuẩn , tiêu chuẩn kỹ thuật áp dụng và quy định về tiêu chí giám sát , nghiệm thu kết quả bảo trì tài sản kết cấu hạ tầng đường sắt quốc gia của Bộ Giao thông vận tải . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 18 `[DIEU]`)


---

### Mẫu #03_2021_TT-BGTVT_147344#body_context_89 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[03/2021/TT-BGTVT]`<SO_HIEU>`** của **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Đường sắt]`<LINH_VUC>`** . **[Điều 19 . Báo cáo định kỳ trong quá trình quản lý , bảo trì kết cấu hạ tầng đường sắt]`<DIEU>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **03/2021/TT-BGTVT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[4:7]`)
- `[e3]` **Đường sắt** → `LINH_VUC` (span: `[9:10]`)
- `[e4]` **Điều 19 . Báo cáo định kỳ trong quá trình quản lý , bảo trì kết cấu hạ tầng đường sắt** → `DIEU` (span: `[11:23]`)

**Quan hệ:**
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Đường sắt `[LINH_VUC]`)
- (`e4` Điều 19 . Báo cáo định kỳ trong quá trình quản lý , bảo trì kết cấu hạ tầng đường sắt `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`)
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Đường sắt `[LINH_VUC]`)
- (`e4` Điều 19 . Báo cáo định kỳ trong quá trình quản lý , bảo trì kết cấu hạ tầng đường sắt `[DIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Đường sắt `[LINH_VUC]`)


---

### Mẫu #03_2021_TT-BGTVT_147344#body_context_90 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[03/2021/TT-BGTVT]`<SO_HIEU>`** của **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Đường sắt]`<LINH_VUC>`** . **[Điều 19]`<DIEU>`** . **[1 . **[Doanh nghiệp kinh doanh kết cấu hạ tầng đường sắt]`<TO_CHUC_DOANH_NGHIEP>`** , nhà cung cấp dịch vụ sự nghiệp công , tổ chức , cá nhân nhận chuyển nhượng có thời hạn , thuê quyền khai thác , kinh doanh kết cấu hạ tầng đường sắt quốc gia do nhà nước đầu tư thực hiện báo cáo định kỳ các nội dung thực hiện thuộc trách nhiệm của mình **[theo quy định tại]`<TU_KHOA_PHAP_LY>`** **[Thông tư này]`<THAM_CHIEU_PHAP_LY>`** và quy định của pháp luật về đường sắt :]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **03/2021/TT-BGTVT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[4:7]`)
- `[e3]` **Đường sắt** → `LINH_VUC` (span: `[9:10]`)
- `[e4]` **Điều 19** → `DIEU` (span: `[11:13]`)
- `[e5]` **1 . Doanh nghiệp kinh doanh kết cấu hạ tầng đường sắt , nhà cung cấp dịch vụ sự nghiệp công , tổ chức , cá nhân nhận chuyển nhượng có thời hạn , thuê quyền khai thác , kinh doanh kết cấu hạ tầng đường sắt quốc gia do nhà nước đầu tư thực hiện báo cáo định kỳ các nội dung thực hiện thuộc trách nhiệm của mình theo quy định tại Thông tư này và quy định của pháp luật về đường sắt :** → `KHOAN` (span: `[14:68]`)
- `[e6]` **Thông tư này** → `THAM_CHIEU_PHAP_LY` (span: `[59:61]`) *(lồng trong `e5` (`KHOAN`))*
- `[e7]` **theo quy định tại** → `TU_KHOA_PHAP_LY` (span: `[56:59]`) *(lồng trong `e5` (`KHOAN`))*
- `[e8]` **Doanh nghiệp kinh doanh kết cấu hạ tầng đường sắt** → `TO_CHUC_DOANH_NGHIEP` (span: `[16:20]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Đường sắt `[LINH_VUC]`)
- (`e4` Điều 19 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`)
- (`e5` 1 . Doanh nghiệp kinh doanh kết cấu hạ tầng đường sắt , nhà cung cấp dịch vụ sự nghiệp công , tổ chức , cá nhân nhận chuyển nhượng có thời hạn , thuê quyền khai thác , kinh doanh kết cấu hạ tầng đường sắt quốc gia do nhà nước đầu tư thực hiện báo cáo định kỳ các nội dung thực hiện thuộc trách nhiệm của mình theo quy định tại Thông tư này và quy định của pháp luật về đường sắt : `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 19 `[DIEU]`)
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Đường sắt `[LINH_VUC]`)
- (`e5` 1 . Doanh nghiệp kinh doanh kết cấu hạ tầng đường sắt , nhà cung cấp dịch vụ sự nghiệp công , tổ chức , cá nhân nhận chuyển nhượng có thời hạn , thuê quyền khai thác , kinh doanh kết cấu hạ tầng đường sắt quốc gia do nhà nước đầu tư thực hiện báo cáo định kỳ các nội dung thực hiện thuộc trách nhiệm của mình theo quy định tại Thông tư này và quy định của pháp luật về đường sắt : `[KHOAN]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Đường sắt `[LINH_VUC]`)
- (`e7` theo quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e6` Thông tư này `[THAM_CHIEU_PHAP_LY]`)
- (`e5` 1 . Doanh nghiệp kinh doanh kết cấu hạ tầng đường sắt , nhà cung cấp dịch vụ sự nghiệp công , tổ chức , cá nhân nhận chuyển nhượng có thời hạn , thuê quyền khai thác , kinh doanh kết cấu hạ tầng đường sắt quốc gia do nhà nước đầu tư thực hiện báo cáo định kỳ các nội dung thực hiện thuộc trách nhiệm của mình theo quy định tại Thông tư này và quy định của pháp luật về đường sắt : `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e6` Thông tư này `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #03_2021_TT-BGTVT_147344#body_standalone_91 (Loại: `body_standalone`)
> **[Điều 19]`<DIEU>`** . **[1 . **[Doanh nghiệp kinh doanh kết cấu hạ tầng đường sắt]`<TO_CHUC_DOANH_NGHIEP>`** , nhà cung cấp dịch vụ sự nghiệp công , tổ chức , cá nhân nhận chuyển nhượng có thời hạn , thuê quyền khai thác , kinh doanh kết cấu hạ tầng đường sắt quốc gia do nhà nước đầu tư thực hiện báo cáo định kỳ các nội dung thực hiện thuộc trách nhiệm của mình **[theo quy định tại]`<TU_KHOA_PHAP_LY>`** **[Thông tư này]`<THAM_CHIEU_PHAP_LY>`** và quy định của pháp luật về đường sắt :]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 19** → `DIEU` (span: `[0:2]`)
- `[e1]` **1 . Doanh nghiệp kinh doanh kết cấu hạ tầng đường sắt , nhà cung cấp dịch vụ sự nghiệp công , tổ chức , cá nhân nhận chuyển nhượng có thời hạn , thuê quyền khai thác , kinh doanh kết cấu hạ tầng đường sắt quốc gia do nhà nước đầu tư thực hiện báo cáo định kỳ các nội dung thực hiện thuộc trách nhiệm của mình theo quy định tại Thông tư này và quy định của pháp luật về đường sắt :** → `KHOAN` (span: `[3:57]`)
- `[e2]` **Thông tư này** → `THAM_CHIEU_PHAP_LY` (span: `[48:50]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **theo quy định tại** → `TU_KHOA_PHAP_LY` (span: `[45:48]`) *(lồng trong `e1` (`KHOAN`))*
- `[e4]` **Doanh nghiệp kinh doanh kết cấu hạ tầng đường sắt** → `TO_CHUC_DOANH_NGHIEP` (span: `[5:9]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 1 . Doanh nghiệp kinh doanh kết cấu hạ tầng đường sắt , nhà cung cấp dịch vụ sự nghiệp công , tổ chức , cá nhân nhận chuyển nhượng có thời hạn , thuê quyền khai thác , kinh doanh kết cấu hạ tầng đường sắt quốc gia do nhà nước đầu tư thực hiện báo cáo định kỳ các nội dung thực hiện thuộc trách nhiệm của mình theo quy định tại Thông tư này và quy định của pháp luật về đường sắt : `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 19 `[DIEU]`)
- (`e3` theo quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e2` Thông tư này `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 1 . Doanh nghiệp kinh doanh kết cấu hạ tầng đường sắt , nhà cung cấp dịch vụ sự nghiệp công , tổ chức , cá nhân nhận chuyển nhượng có thời hạn , thuê quyền khai thác , kinh doanh kết cấu hạ tầng đường sắt quốc gia do nhà nước đầu tư thực hiện báo cáo định kỳ các nội dung thực hiện thuộc trách nhiệm của mình theo quy định tại Thông tư này và quy định của pháp luật về đường sắt : `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e2` Thông tư này `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #03_2021_TT-BGTVT_147344#body_context_92 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[03/2021/TT-BGTVT]`<SO_HIEU>`** ban hành **[ngày 08 tháng 02 năm 2021]`<NGAY_BAN_HANH>`** bởi **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** . **[Điều 19]`<DIEU>`** . **[Khoản 1]`<KHOAN>`** . **[i ) Biểu mẫu báo cáo theo mẫu tại **[Mẫu số 01]`<THAM_CHIEU_PHAP_LY>`** **[Phụ lục 03 ban hành kèm theo Thông tư này]`<THAM_CHIEU_PHAP_LY>`** .]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **03/2021/TT-BGTVT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[11:14]`)
- `[e3]` **ngày 08 tháng 02 năm 2021** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 19** → `DIEU` (span: `[15:17]`)
- `[e5]` **Khoản 1** → `KHOAN` (span: `[18:20]`)
- `[e6]` **i ) Biểu mẫu báo cáo theo mẫu tại Mẫu số 01 Phụ lục 03 ban hành kèm theo Thông tư này .** → `DIEM` (span: `[21:38]`)
- `[e7]` **Mẫu số 01** → `THAM_CHIEU_PHAP_LY` (span: `[28:30]`) *(lồng trong `e6` (`DIEM`))*
- `[e8]` **Phụ lục 03 ban hành kèm theo Thông tư này** → `THAM_CHIEU_PHAP_LY` (span: `[30:37]`) *(lồng trong `e6` (`DIEM`))*

**Quan hệ:**
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 08 tháng 02 năm 2021 `[NGAY_BAN_HANH]`)
- (`e4` Điều 19 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`)
- (`e5` Khoản 1 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 19 `[DIEU]`)
- (`e6` i ) Biểu mẫu báo cáo theo mẫu tại Mẫu số 01 Phụ lục 03 ban hành kèm theo Thông tư này . `[DIEM]`) ==[ **THUOC_VE** ]==> (`e5` Khoản 1 `[KHOAN]`)
- (`e6` i ) Biểu mẫu báo cáo theo mẫu tại Mẫu số 01 Phụ lục 03 ban hành kèm theo Thông tư này . `[DIEM]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e7` Mẫu số 01 `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e6` i ) Biểu mẫu báo cáo theo mẫu tại Mẫu số 01 Phụ lục 03 ban hành kèm theo Thông tư này . `[DIEM]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e8` Phụ lục 03 ban hành kèm theo Thông tư này `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #03_2021_TT-BGTVT_147344#body_standalone_93 (Loại: `body_standalone`)
> **[Điều 19]`<DIEU>`** . **[Khoản 1]`<KHOAN>`** . **[i ) Biểu mẫu báo cáo theo mẫu tại **[Mẫu số 01]`<THAM_CHIEU_PHAP_LY>`** **[Phụ lục 03 ban hành kèm theo Thông tư này]`<THAM_CHIEU_PHAP_LY>`** .]`<DIEM>`**

**Thực thể:**
- `[e0]` **Điều 19** → `DIEU` (span: `[0:2]`)
- `[e1]` **Khoản 1** → `KHOAN` (span: `[3:5]`)
- `[e2]` **i ) Biểu mẫu báo cáo theo mẫu tại Mẫu số 01 Phụ lục 03 ban hành kèm theo Thông tư này .** → `DIEM` (span: `[6:23]`)
- `[e3]` **Mẫu số 01** → `THAM_CHIEU_PHAP_LY` (span: `[13:15]`) *(lồng trong `e2` (`DIEM`))*
- `[e4]` **Phụ lục 03 ban hành kèm theo Thông tư này** → `THAM_CHIEU_PHAP_LY` (span: `[15:22]`) *(lồng trong `e2` (`DIEM`))*

**Quan hệ:**
- (`e1` Khoản 1 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 19 `[DIEU]`)
- (`e2` i ) Biểu mẫu báo cáo theo mẫu tại Mẫu số 01 Phụ lục 03 ban hành kèm theo Thông tư này . `[DIEM]`) ==[ **THUOC_VE** ]==> (`e1` Khoản 1 `[KHOAN]`)
- (`e2` i ) Biểu mẫu báo cáo theo mẫu tại Mẫu số 01 Phụ lục 03 ban hành kèm theo Thông tư này . `[DIEM]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Mẫu số 01 `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e2` i ) Biểu mẫu báo cáo theo mẫu tại Mẫu số 01 Phụ lục 03 ban hành kèm theo Thông tư này . `[DIEM]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e4` Phụ lục 03 ban hành kèm theo Thông tư này `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #03_2021_TT-BGTVT_147344#body_context_94 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[03/2021/TT-BGTVT]`<SO_HIEU>`** ban hành **[ngày 08 tháng 02 năm 2021]`<NGAY_BAN_HANH>`** bởi **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** . **[Điều 19]`<DIEU>`** . **[Khoản 2]`<KHOAN>`** . **[c ) Đối tượng thực hiện báo cáo : Cục Đường sắt Viêt Nam .]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **03/2021/TT-BGTVT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[11:14]`)
- `[e3]` **ngày 08 tháng 02 năm 2021** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 19** → `DIEU` (span: `[15:17]`)
- `[e5]` **Khoản 2** → `KHOAN` (span: `[18:20]`)
- `[e6]` **c ) Đối tượng thực hiện báo cáo : Cục Đường sắt Viêt Nam .** → `DIEM` (span: `[21:31]`)

**Quan hệ:**
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 08 tháng 02 năm 2021 `[NGAY_BAN_HANH]`)
- (`e4` Điều 19 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`)
- (`e5` Khoản 2 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 19 `[DIEU]`)
- (`e6` c ) Đối tượng thực hiện báo cáo : Cục Đường sắt Viêt Nam . `[DIEM]`) ==[ **THUOC_VE** ]==> (`e5` Khoản 2 `[KHOAN]`)


---

### Mẫu #03_2021_TT-BGTVT_147344#body_context_95 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[03/2021/TT-BGTVT]`<SO_HIEU>`** của **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Đường sắt]`<LINH_VUC>`** . **[Điều 20]`<DIEU>`** . **[Khoản 1 . **[Cơ quan quản lý nhà nước]`<CO_QUAN_THAM_QUYEN>`** chuyên ngành đường sắt]`<KHOAN>`** : **[d ) Thực hiện các nội dung quy định khác thuộc trách nhiệm của **[cơ quan quản lý nhà nước]`<CO_QUAN_THAM_QUYEN>`** chuyên ngành đường sắt liên quan đến quản lý , bảo trì công trình đường sắt theo quy định của pháp luật .]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **03/2021/TT-BGTVT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[4:7]`)
- `[e3]` **Đường sắt** → `LINH_VUC` (span: `[9:10]`)
- `[e4]` **Điều 20** → `DIEU` (span: `[11:13]`)
- `[e5]` **Khoản 1 . Cơ quan quản lý nhà nước chuyên ngành đường sắt** → `KHOAN` (span: `[14:22]`)
- `[e6]` **d ) Thực hiện các nội dung quy định khác thuộc trách nhiệm của cơ quan quản lý nhà nước chuyên ngành đường sắt liên quan đến quản lý , bảo trì công trình đường sắt theo quy định của pháp luật .** → `DIEM` (span: `[23:50]`)
- `[e7]` **Cơ quan quản lý nhà nước** → `CO_QUAN_THAM_QUYEN` (span: `[17:20]`) *(lồng trong `e5` (`KHOAN`))*
- `[e8]` **cơ quan quản lý nhà nước** → `CO_QUAN_THAM_QUYEN` (span: `[33:36]`) *(lồng trong `e6` (`DIEM`))*

**Quan hệ:**
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Đường sắt `[LINH_VUC]`)
- (`e4` Điều 20 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`)
- (`e5` Khoản 1 . Cơ quan quản lý nhà nước chuyên ngành đường sắt `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 20 `[DIEU]`)
- (`e6` d ) Thực hiện các nội dung quy định khác thuộc trách nhiệm của cơ quan quản lý nhà nước chuyên ngành đường sắt liên quan đến quản lý , bảo trì công trình đường sắt theo quy định của pháp luật . `[DIEM]`) ==[ **THUOC_VE** ]==> (`e5` Khoản 1 . Cơ quan quản lý nhà nước chuyên ngành đường sắt `[KHOAN]`)
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Đường sắt `[LINH_VUC]`)
- (`e6` d ) Thực hiện các nội dung quy định khác thuộc trách nhiệm của cơ quan quản lý nhà nước chuyên ngành đường sắt liên quan đến quản lý , bảo trì công trình đường sắt theo quy định của pháp luật . `[DIEM]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Đường sắt `[LINH_VUC]`)


---

### Mẫu #03_2021_TT-BGTVT_147344#body_standalone_96 (Loại: `body_standalone`)
> **[Điều 20]`<DIEU>`** . **[Khoản 1 . **[Cơ quan quản lý nhà nước]`<CO_QUAN_THAM_QUYEN>`** chuyên ngành đường sắt]`<KHOAN>`** : **[d ) Thực hiện các nội dung quy định khác thuộc trách nhiệm của **[cơ quan quản lý nhà nước]`<CO_QUAN_THAM_QUYEN>`** chuyên ngành đường sắt liên quan đến quản lý , bảo trì công trình đường sắt theo quy định của pháp luật .]`<DIEM>`**

**Thực thể:**
- `[e0]` **Điều 20** → `DIEU` (span: `[0:2]`)
- `[e1]` **Khoản 1 . Cơ quan quản lý nhà nước chuyên ngành đường sắt** → `KHOAN` (span: `[3:11]`)
- `[e2]` **d ) Thực hiện các nội dung quy định khác thuộc trách nhiệm của cơ quan quản lý nhà nước chuyên ngành đường sắt liên quan đến quản lý , bảo trì công trình đường sắt theo quy định của pháp luật .** → `DIEM` (span: `[12:39]`)
- `[e3]` **Cơ quan quản lý nhà nước** → `CO_QUAN_THAM_QUYEN` (span: `[6:9]`) *(lồng trong `e1` (`KHOAN`))*
- `[e4]` **cơ quan quản lý nhà nước** → `CO_QUAN_THAM_QUYEN` (span: `[22:25]`) *(lồng trong `e2` (`DIEM`))*

**Quan hệ:**
- (`e1` Khoản 1 . Cơ quan quản lý nhà nước chuyên ngành đường sắt `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 20 `[DIEU]`)
- (`e2` d ) Thực hiện các nội dung quy định khác thuộc trách nhiệm của cơ quan quản lý nhà nước chuyên ngành đường sắt liên quan đến quản lý , bảo trì công trình đường sắt theo quy định của pháp luật . `[DIEM]`) ==[ **THUOC_VE** ]==> (`e1` Khoản 1 . Cơ quan quản lý nhà nước chuyên ngành đường sắt `[KHOAN]`)


---

### Mẫu #03_2021_TT-BGTVT_147344#body_context_97 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[03/2021/TT-BGTVT]`<SO_HIEU>`** ban hành **[ngày 08 tháng 02 năm 2021]`<NGAY_BAN_HANH>`** bởi **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** . **[Điều 20]`<DIEU>`** . **[Khoản 2 . **[Doanh nghiệp kinh doanh kết cấu hạ tầng đường sắt]`<TO_CHUC_DOANH_NGHIEP>`**]`<KHOAN>`** : **[b ) Sử dụng , khai thác kết cấu hạ tầng đường sắt theo quy định ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **03/2021/TT-BGTVT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[11:14]`)
- `[e3]` **ngày 08 tháng 02 năm 2021** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 20** → `DIEU` (span: `[15:17]`)
- `[e5]` **Khoản 2 . Doanh nghiệp kinh doanh kết cấu hạ tầng đường sắt** → `KHOAN` (span: `[18:25]`)
- `[e6]` **b ) Sử dụng , khai thác kết cấu hạ tầng đường sắt theo quy định ;** → `DIEM` (span: `[26:36]`)
- `[e7]` **Doanh nghiệp kinh doanh kết cấu hạ tầng đường sắt** → `TO_CHUC_DOANH_NGHIEP` (span: `[21:25]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 08 tháng 02 năm 2021 `[NGAY_BAN_HANH]`)
- (`e4` Điều 20 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`)
- (`e5` Khoản 2 . Doanh nghiệp kinh doanh kết cấu hạ tầng đường sắt `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 20 `[DIEU]`)
- (`e6` b ) Sử dụng , khai thác kết cấu hạ tầng đường sắt theo quy định ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e5` Khoản 2 . Doanh nghiệp kinh doanh kết cấu hạ tầng đường sắt `[KHOAN]`)


---

### Mẫu #03_2021_TT-BGTVT_147344#body_standalone_98 (Loại: `body_standalone`)
> **[Điều 20]`<DIEU>`** . **[Khoản 2 . **[Doanh nghiệp kinh doanh kết cấu hạ tầng đường sắt]`<TO_CHUC_DOANH_NGHIEP>`**]`<KHOAN>`** : **[b ) Sử dụng , khai thác kết cấu hạ tầng đường sắt theo quy định ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Điều 20** → `DIEU` (span: `[0:2]`)
- `[e1]` **Khoản 2 . Doanh nghiệp kinh doanh kết cấu hạ tầng đường sắt** → `KHOAN` (span: `[3:10]`)
- `[e2]` **b ) Sử dụng , khai thác kết cấu hạ tầng đường sắt theo quy định ;** → `DIEM` (span: `[11:21]`)
- `[e3]` **Doanh nghiệp kinh doanh kết cấu hạ tầng đường sắt** → `TO_CHUC_DOANH_NGHIEP` (span: `[6:10]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` Khoản 2 . Doanh nghiệp kinh doanh kết cấu hạ tầng đường sắt `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 20 `[DIEU]`)
- (`e2` b ) Sử dụng , khai thác kết cấu hạ tầng đường sắt theo quy định ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e1` Khoản 2 . Doanh nghiệp kinh doanh kết cấu hạ tầng đường sắt `[KHOAN]`)


---

### Mẫu #03_2021_TT-BGTVT_147344#body_context_99 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[03/2021/TT-BGTVT]`<SO_HIEU>`** ban hành **[ngày 08 tháng 02 năm 2021]`<NGAY_BAN_HANH>`** bởi **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** . **[Điều 20]`<DIEU>`** . **[Khoản 2 . **[Doanh nghiệp kinh doanh kết cấu hạ tầng đường sắt]`<TO_CHUC_DOANH_NGHIEP>`**]`<KHOAN>`** : **[đ ) Thực hiện các nội dung quy định khác thuộc trách nhiệm của **[doanh nghiệp]`<TO_CHUC_DOANH_NGHIEP>`** liên quan đến quản lý kết cấu hạ tầng , bảo trì công trình đường sắt theo quy định của pháp luật .]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **03/2021/TT-BGTVT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[11:14]`)
- `[e3]` **ngày 08 tháng 02 năm 2021** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 20** → `DIEU` (span: `[15:17]`)
- `[e5]` **Khoản 2 . Doanh nghiệp kinh doanh kết cấu hạ tầng đường sắt** → `KHOAN` (span: `[18:25]`)
- `[e6]` **đ ) Thực hiện các nội dung quy định khác thuộc trách nhiệm của doanh nghiệp liên quan đến quản lý kết cấu hạ tầng , bảo trì công trình đường sắt theo quy định của pháp luật .** → `DIEM` (span: `[26:50]`)
- `[e7]` **doanh nghiệp** → `TO_CHUC_DOANH_NGHIEP` (span: `[36:37]`) *(lồng trong `e6` (`DIEM`))*
- `[e8]` **Doanh nghiệp kinh doanh kết cấu hạ tầng đường sắt** → `TO_CHUC_DOANH_NGHIEP` (span: `[21:25]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 08 tháng 02 năm 2021 `[NGAY_BAN_HANH]`)
- (`e4` Điều 20 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`)
- (`e5` Khoản 2 . Doanh nghiệp kinh doanh kết cấu hạ tầng đường sắt `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 20 `[DIEU]`)
- (`e6` đ ) Thực hiện các nội dung quy định khác thuộc trách nhiệm của doanh nghiệp liên quan đến quản lý kết cấu hạ tầng , bảo trì công trình đường sắt theo quy định của pháp luật . `[DIEM]`) ==[ **THUOC_VE** ]==> (`e5` Khoản 2 . Doanh nghiệp kinh doanh kết cấu hạ tầng đường sắt `[KHOAN]`)


---

### Mẫu #03_2021_TT-BGTVT_147344#body_standalone_100 (Loại: `body_standalone`)
> **[Điều 20]`<DIEU>`** . **[Khoản 2 . **[Doanh nghiệp kinh doanh kết cấu hạ tầng đường sắt]`<TO_CHUC_DOANH_NGHIEP>`**]`<KHOAN>`** : **[đ ) Thực hiện các nội dung quy định khác thuộc trách nhiệm của **[doanh nghiệp]`<TO_CHUC_DOANH_NGHIEP>`** liên quan đến quản lý kết cấu hạ tầng , bảo trì công trình đường sắt theo quy định của pháp luật .]`<DIEM>`**

**Thực thể:**
- `[e0]` **Điều 20** → `DIEU` (span: `[0:2]`)
- `[e1]` **Khoản 2 . Doanh nghiệp kinh doanh kết cấu hạ tầng đường sắt** → `KHOAN` (span: `[3:10]`)
- `[e2]` **đ ) Thực hiện các nội dung quy định khác thuộc trách nhiệm của doanh nghiệp liên quan đến quản lý kết cấu hạ tầng , bảo trì công trình đường sắt theo quy định của pháp luật .** → `DIEM` (span: `[11:35]`)
- `[e3]` **doanh nghiệp** → `TO_CHUC_DOANH_NGHIEP` (span: `[21:22]`) *(lồng trong `e2` (`DIEM`))*
- `[e4]` **Doanh nghiệp kinh doanh kết cấu hạ tầng đường sắt** → `TO_CHUC_DOANH_NGHIEP` (span: `[6:10]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` Khoản 2 . Doanh nghiệp kinh doanh kết cấu hạ tầng đường sắt `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 20 `[DIEU]`)
- (`e2` đ ) Thực hiện các nội dung quy định khác thuộc trách nhiệm của doanh nghiệp liên quan đến quản lý kết cấu hạ tầng , bảo trì công trình đường sắt theo quy định của pháp luật . `[DIEM]`) ==[ **THUOC_VE** ]==> (`e1` Khoản 2 . Doanh nghiệp kinh doanh kết cấu hạ tầng đường sắt `[KHOAN]`)


---

### Mẫu #03_2021_TT-BGTVT_147344#body_context_101 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[03/2021/TT-BGTVT]`<SO_HIEU>`** của **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Đường sắt]`<LINH_VUC>`** . **[Điều 20]`<DIEU>`** . **[3 . Nhà cung cấp dịch vụ sự nghiệp công sử dụng kinh phí **[ngân sách nhà nước]`<TAI_SAN_VAT_CHAT>`** thực hiện quyền , nghĩa vụ **[theo quy định tại]`<TU_KHOA_PHAP_LY>`** **[Điều 27 Nghị định số 32/2019/NĐ-CP]`<THAM_CHIEU_PHAP_LY>`** **[ngày 10 tháng 4 năm 2019]`<NGAY_THAM_CHIEU>`** của **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** quy định giao nhiệm vụ , đặt hàng hoặc đấu thầu cung cấp sản phẩm , dịch vụ công sử dụng **[ngân sách nhà nước]`<TAI_SAN_VAT_CHAT>`** từ nguồn kinh phí chi thường xuyên .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **03/2021/TT-BGTVT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[4:7]`)
- `[e3]` **Đường sắt** → `LINH_VUC` (span: `[9:10]`)
- `[e4]` **Điều 20** → `DIEU` (span: `[11:13]`)
- `[e5]` **3 . Nhà cung cấp dịch vụ sự nghiệp công sử dụng kinh phí ngân sách nhà nước thực hiện quyền , nghĩa vụ theo quy định tại Điều 27 Nghị định số 32/2019/NĐ-CP ngày 10 tháng 4 năm 2019 của Chính phủ quy định giao nhiệm vụ , đặt hàng hoặc đấu thầu cung cấp sản phẩm , dịch vụ công sử dụng ngân sách nhà nước từ nguồn kinh phí chi thường xuyên .** → `KHOAN` (span: `[14:66]`)
- `[e6]` **Điều 27 Nghị định số 32/2019/NĐ-CP** → `THAM_CHIEU_PHAP_LY` (span: `[32:37]`) *(lồng trong `e5` (`KHOAN`))*
- `[e7]` **theo quy định tại** → `TU_KHOA_PHAP_LY` (span: `[29:32]`) *(lồng trong `e5` (`KHOAN`))*
- `[e8]` **ngày 10 tháng 4 năm 2019** → `NGAY_THAM_CHIEU` (span: `[37:43]`) *(lồng trong `e5` (`KHOAN`))*
- `[e9]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[44:45]`) *(lồng trong `e5` (`KHOAN`))*
- `[e10]` **ngân sách nhà nước** → `TAI_SAN_VAT_CHAT` (span: `[23:25]`) *(lồng trong `e5` (`KHOAN`))*
- `[e11]` **ngân sách nhà nước** → `TAI_SAN_VAT_CHAT` (span: `[58:60]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Đường sắt `[LINH_VUC]`)
- (`e4` Điều 20 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`)
- (`e5` 3 . Nhà cung cấp dịch vụ sự nghiệp công sử dụng kinh phí ngân sách nhà nước thực hiện quyền , nghĩa vụ theo quy định tại Điều 27 Nghị định số 32/2019/NĐ-CP ngày 10 tháng 4 năm 2019 của Chính phủ quy định giao nhiệm vụ , đặt hàng hoặc đấu thầu cung cấp sản phẩm , dịch vụ công sử dụng ngân sách nhà nước từ nguồn kinh phí chi thường xuyên . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 20 `[DIEU]`)
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Đường sắt `[LINH_VUC]`)
- (`e5` 3 . Nhà cung cấp dịch vụ sự nghiệp công sử dụng kinh phí ngân sách nhà nước thực hiện quyền , nghĩa vụ theo quy định tại Điều 27 Nghị định số 32/2019/NĐ-CP ngày 10 tháng 4 năm 2019 của Chính phủ quy định giao nhiệm vụ , đặt hàng hoặc đấu thầu cung cấp sản phẩm , dịch vụ công sử dụng ngân sách nhà nước từ nguồn kinh phí chi thường xuyên . `[KHOAN]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Đường sắt `[LINH_VUC]`)
- (`e7` theo quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e6` Điều 27 Nghị định số 32/2019/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e5` 3 . Nhà cung cấp dịch vụ sự nghiệp công sử dụng kinh phí ngân sách nhà nước thực hiện quyền , nghĩa vụ theo quy định tại Điều 27 Nghị định số 32/2019/NĐ-CP ngày 10 tháng 4 năm 2019 của Chính phủ quy định giao nhiệm vụ , đặt hàng hoặc đấu thầu cung cấp sản phẩm , dịch vụ công sử dụng ngân sách nhà nước từ nguồn kinh phí chi thường xuyên . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e6` Điều 27 Nghị định số 32/2019/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e6` Điều 27 Nghị định số 32/2019/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e8` ngày 10 tháng 4 năm 2019 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #03_2021_TT-BGTVT_147344#body_standalone_102 (Loại: `body_standalone`)
> **[Điều 20]`<DIEU>`** . **[3 . Nhà cung cấp dịch vụ sự nghiệp công sử dụng kinh phí **[ngân sách nhà nước]`<TAI_SAN_VAT_CHAT>`** thực hiện quyền , nghĩa vụ **[theo quy định tại]`<TU_KHOA_PHAP_LY>`** **[Điều 27 Nghị định số 32/2019/NĐ-CP]`<THAM_CHIEU_PHAP_LY>`** **[ngày 10 tháng 4 năm 2019]`<NGAY_THAM_CHIEU>`** của **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** quy định giao nhiệm vụ , đặt hàng hoặc đấu thầu cung cấp sản phẩm , dịch vụ công sử dụng **[ngân sách nhà nước]`<TAI_SAN_VAT_CHAT>`** từ nguồn kinh phí chi thường xuyên .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 20** → `DIEU` (span: `[0:2]`)
- `[e1]` **3 . Nhà cung cấp dịch vụ sự nghiệp công sử dụng kinh phí ngân sách nhà nước thực hiện quyền , nghĩa vụ theo quy định tại Điều 27 Nghị định số 32/2019/NĐ-CP ngày 10 tháng 4 năm 2019 của Chính phủ quy định giao nhiệm vụ , đặt hàng hoặc đấu thầu cung cấp sản phẩm , dịch vụ công sử dụng ngân sách nhà nước từ nguồn kinh phí chi thường xuyên .** → `KHOAN` (span: `[3:55]`)
- `[e2]` **Điều 27 Nghị định số 32/2019/NĐ-CP** → `THAM_CHIEU_PHAP_LY` (span: `[21:26]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **theo quy định tại** → `TU_KHOA_PHAP_LY` (span: `[18:21]`) *(lồng trong `e1` (`KHOAN`))*
- `[e4]` **ngày 10 tháng 4 năm 2019** → `NGAY_THAM_CHIEU` (span: `[26:32]`) *(lồng trong `e1` (`KHOAN`))*
- `[e5]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[33:34]`) *(lồng trong `e1` (`KHOAN`))*
- `[e6]` **ngân sách nhà nước** → `TAI_SAN_VAT_CHAT` (span: `[12:14]`) *(lồng trong `e1` (`KHOAN`))*
- `[e7]` **ngân sách nhà nước** → `TAI_SAN_VAT_CHAT` (span: `[47:49]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 3 . Nhà cung cấp dịch vụ sự nghiệp công sử dụng kinh phí ngân sách nhà nước thực hiện quyền , nghĩa vụ theo quy định tại Điều 27 Nghị định số 32/2019/NĐ-CP ngày 10 tháng 4 năm 2019 của Chính phủ quy định giao nhiệm vụ , đặt hàng hoặc đấu thầu cung cấp sản phẩm , dịch vụ công sử dụng ngân sách nhà nước từ nguồn kinh phí chi thường xuyên . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 20 `[DIEU]`)
- (`e3` theo quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e2` Điều 27 Nghị định số 32/2019/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 3 . Nhà cung cấp dịch vụ sự nghiệp công sử dụng kinh phí ngân sách nhà nước thực hiện quyền , nghĩa vụ theo quy định tại Điều 27 Nghị định số 32/2019/NĐ-CP ngày 10 tháng 4 năm 2019 của Chính phủ quy định giao nhiệm vụ , đặt hàng hoặc đấu thầu cung cấp sản phẩm , dịch vụ công sử dụng ngân sách nhà nước từ nguồn kinh phí chi thường xuyên . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e2` Điều 27 Nghị định số 32/2019/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e2` Điều 27 Nghị định số 32/2019/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e4` ngày 10 tháng 4 năm 2019 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #03_2021_TT-BGTVT_147344#body_context_103 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[03/2021/TT-BGTVT]`<SO_HIEU>`** của **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Đường sắt]`<LINH_VUC>`** . **[Điều 21]`<DIEU>`** . **[3 . Việc quản lý , sử dụng kinh phí bảo trì công trình đường sắt thực hiện theo các quy định của pháp luật hiện hành .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **03/2021/TT-BGTVT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[4:7]`)
- `[e3]` **Đường sắt** → `LINH_VUC` (span: `[9:10]`)
- `[e4]` **Điều 21** → `DIEU` (span: `[11:13]`)
- `[e5]` **3 . Việc quản lý , sử dụng kinh phí bảo trì công trình đường sắt thực hiện theo các quy định của pháp luật hiện hành .** → `KHOAN` (span: `[14:32]`)

**Quan hệ:**
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Đường sắt `[LINH_VUC]`)
- (`e4` Điều 21 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`)
- (`e5` 3 . Việc quản lý , sử dụng kinh phí bảo trì công trình đường sắt thực hiện theo các quy định của pháp luật hiện hành . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 21 `[DIEU]`)
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Đường sắt `[LINH_VUC]`)
- (`e5` 3 . Việc quản lý , sử dụng kinh phí bảo trì công trình đường sắt thực hiện theo các quy định của pháp luật hiện hành . `[KHOAN]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Đường sắt `[LINH_VUC]`)


---

### Mẫu #03_2021_TT-BGTVT_147344#body_context_104 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[03/2021/TT-BGTVT]`<SO_HIEU>`** ban hành **[ngày 08 tháng 02 năm 2021]`<NGAY_BAN_HANH>`** bởi **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** . **[Điều 22]`<DIEU>`** . **[Khoản 1 . Nội dung các khoản mục chi phí liên quan đến thực hiện bảo trì công trình đường sắt bao gồm]`<KHOAN>`** : **[g ) Chi phí quan trắc công trình đường sắt ; chi phí đánh giá an toàn chịu lực và an toàn vận hành công trình trong quá trình khai thác sử dụng ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **03/2021/TT-BGTVT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[11:14]`)
- `[e3]` **ngày 08 tháng 02 năm 2021** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 22** → `DIEU` (span: `[15:17]`)
- `[e5]` **Khoản 1 . Nội dung các khoản mục chi phí liên quan đến thực hiện bảo trì công trình đường sắt bao gồm** → `KHOAN` (span: `[18:33]`)
- `[e6]` **g ) Chi phí quan trắc công trình đường sắt ; chi phí đánh giá an toàn chịu lực và an toàn vận hành công trình trong quá trình khai thác sử dụng ;** → `DIEM` (span: `[34:55]`)

**Quan hệ:**
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 08 tháng 02 năm 2021 `[NGAY_BAN_HANH]`)
- (`e4` Điều 22 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`)
- (`e5` Khoản 1 . Nội dung các khoản mục chi phí liên quan đến thực hiện bảo trì công trình đường sắt bao gồm `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 22 `[DIEU]`)
- (`e6` g ) Chi phí quan trắc công trình đường sắt ; chi phí đánh giá an toàn chịu lực và an toàn vận hành công trình trong quá trình khai thác sử dụng ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e5` Khoản 1 . Nội dung các khoản mục chi phí liên quan đến thực hiện bảo trì công trình đường sắt bao gồm `[KHOAN]`)


---

### Mẫu #03_2021_TT-BGTVT_147344#body_context_105 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[03/2021/TT-BGTVT]`<SO_HIEU>`** ban hành **[ngày 08 tháng 02 năm 2021]`<NGAY_BAN_HANH>`** bởi **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** . **[Điều 24]`<DIEU>`** . **[1 . Các công trình , nhiệm vụ đã được phê duyệt và đang triển khai thực hiện đến ngày Thông tư này có hiệu lực vẫn chưa hoàn thành thì tiếp tục thực hiện **[theo quy định tại]`<TU_KHOA_PHAP_LY>`** **[Thông tư số 16/2018/TT-BGTVT]`<THAM_CHIEU_PHAP_LY>`** **[ngày 04 tháng 4 năm 2018]`<NGAY_THAM_CHIEU>`** của **[Bộ trưởng Bộ Giao thông vận tải]`<CO_QUAN_THAM_QUYEN>`** .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **03/2021/TT-BGTVT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[11:14]`)
- `[e3]` **ngày 08 tháng 02 năm 2021** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 24** → `DIEU` (span: `[15:17]`)
- `[e5]` **1 . Các công trình , nhiệm vụ đã được phê duyệt và đang triển khai thực hiện đến ngày Thông tư này có hiệu lực vẫn chưa hoàn thành thì tiếp tục thực hiện theo quy định tại Thông tư số 16/2018/TT-BGTVT ngày 04 tháng 4 năm 2018 của Bộ trưởng Bộ Giao thông vận tải .** → `KHOAN` (span: `[18:61]`)
- `[e6]` **Thông tư số 16/2018/TT-BGTVT** → `THAM_CHIEU_PHAP_LY` (span: `[46:49]`) *(lồng trong `e5` (`KHOAN`))*
- `[e7]` **theo quy định tại** → `TU_KHOA_PHAP_LY` (span: `[43:46]`) *(lồng trong `e5` (`KHOAN`))*
- `[e8]` **ngày 04 tháng 4 năm 2018** → `NGAY_THAM_CHIEU` (span: `[49:55]`) *(lồng trong `e5` (`KHOAN`))*
- `[e9]` **Bộ trưởng Bộ Giao thông vận tải** → `CO_QUAN_THAM_QUYEN` (span: `[56:60]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 08 tháng 02 năm 2021 `[NGAY_BAN_HANH]`)
- (`e4` Điều 24 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 03/2021/TT-BGTVT `[SO_HIEU]`)
- (`e5` 1 . Các công trình , nhiệm vụ đã được phê duyệt và đang triển khai thực hiện đến ngày Thông tư này có hiệu lực vẫn chưa hoàn thành thì tiếp tục thực hiện theo quy định tại Thông tư số 16/2018/TT-BGTVT ngày 04 tháng 4 năm 2018 của Bộ trưởng Bộ Giao thông vận tải . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 24 `[DIEU]`)
- (`e7` theo quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e6` Thông tư số 16/2018/TT-BGTVT `[THAM_CHIEU_PHAP_LY]`)
- (`e5` 1 . Các công trình , nhiệm vụ đã được phê duyệt và đang triển khai thực hiện đến ngày Thông tư này có hiệu lực vẫn chưa hoàn thành thì tiếp tục thực hiện theo quy định tại Thông tư số 16/2018/TT-BGTVT ngày 04 tháng 4 năm 2018 của Bộ trưởng Bộ Giao thông vận tải . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e6` Thông tư số 16/2018/TT-BGTVT `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e6` Thông tư số 16/2018/TT-BGTVT `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e8` ngày 04 tháng 4 năm 2018 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #03_2021_TT-BGTVT_147344#body_standalone_106 (Loại: `body_standalone`)
> **[Điều 24]`<DIEU>`** . **[1 . Các công trình , nhiệm vụ đã được phê duyệt và đang triển khai thực hiện đến ngày Thông tư này có hiệu lực vẫn chưa hoàn thành thì tiếp tục thực hiện **[theo quy định tại]`<TU_KHOA_PHAP_LY>`** **[Thông tư số 16/2018/TT-BGTVT]`<THAM_CHIEU_PHAP_LY>`** **[ngày 04 tháng 4 năm 2018]`<NGAY_THAM_CHIEU>`** của **[Bộ trưởng Bộ Giao thông vận tải]`<CO_QUAN_THAM_QUYEN>`** .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 24** → `DIEU` (span: `[0:2]`)
- `[e1]` **1 . Các công trình , nhiệm vụ đã được phê duyệt và đang triển khai thực hiện đến ngày Thông tư này có hiệu lực vẫn chưa hoàn thành thì tiếp tục thực hiện theo quy định tại Thông tư số 16/2018/TT-BGTVT ngày 04 tháng 4 năm 2018 của Bộ trưởng Bộ Giao thông vận tải .** → `KHOAN` (span: `[3:46]`)
- `[e2]` **Thông tư số 16/2018/TT-BGTVT** → `THAM_CHIEU_PHAP_LY` (span: `[31:34]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **theo quy định tại** → `TU_KHOA_PHAP_LY` (span: `[28:31]`) *(lồng trong `e1` (`KHOAN`))*
- `[e4]` **ngày 04 tháng 4 năm 2018** → `NGAY_THAM_CHIEU` (span: `[34:40]`) *(lồng trong `e1` (`KHOAN`))*
- `[e5]` **Bộ trưởng Bộ Giao thông vận tải** → `CO_QUAN_THAM_QUYEN` (span: `[41:45]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 1 . Các công trình , nhiệm vụ đã được phê duyệt và đang triển khai thực hiện đến ngày Thông tư này có hiệu lực vẫn chưa hoàn thành thì tiếp tục thực hiện theo quy định tại Thông tư số 16/2018/TT-BGTVT ngày 04 tháng 4 năm 2018 của Bộ trưởng Bộ Giao thông vận tải . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 24 `[DIEU]`)
- (`e3` theo quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e2` Thông tư số 16/2018/TT-BGTVT `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 1 . Các công trình , nhiệm vụ đã được phê duyệt và đang triển khai thực hiện đến ngày Thông tư này có hiệu lực vẫn chưa hoàn thành thì tiếp tục thực hiện theo quy định tại Thông tư số 16/2018/TT-BGTVT ngày 04 tháng 4 năm 2018 của Bộ trưởng Bộ Giao thông vận tải . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e2` Thông tư số 16/2018/TT-BGTVT `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e2` Thông tư số 16/2018/TT-BGTVT `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e4` ngày 04 tháng 4 năm 2018 `[NGAY_THAM_CHIEU]`)


---
