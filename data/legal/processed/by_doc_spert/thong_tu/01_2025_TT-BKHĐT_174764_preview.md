# Dữ liệu gán nhãn văn bản: 01_2025_TT-BKHĐT_174764
- **Thể loại**: `thong_tu`
- **Phân vùng dữ liệu**: `TRAIN`
- **Tổng số mẫu**: 89 mẫu
- **Tổng số thực thể**: 519
- **Tổng số quan hệ**: 422

---

### Mẫu #01_2025_TT-BKHĐT_174764#header_0 (Loại: `header`)
> **[BỘ KẾ HOẠCH VÀ ĐẦU TƯ]`<CO_QUAN_BAN_HANH>`** . CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM Độc lập - Tự do - Hạnh phúc . Số : **[01/2025/TT-BKHĐT]`<SO_HIEU>`** . Hà Nội , **[ngày 02 tháng 01 năm 2025]`<NGAY_BAN_HANH>`** . **[THÔNG TƯ]`<LOAI_VAN_BAN>`**

**Thực thể:**
- `[e0]` **01/2025/TT-BKHĐT** → `SO_HIEU` (span: `[19:20]`)
- `[e1]` **ngày 02 tháng 01 năm 2025** → `NGAY_BAN_HANH` (span: `[23:29]`)
- `[e2]` **BỘ KẾ HOẠCH VÀ ĐẦU TƯ** → `CO_QUAN_BAN_HANH` (span: `[0:4]`)
- `[e3]` **THÔNG TƯ** → `LOAI_VAN_BAN` (span: `[30:31]`)

**Quan hệ:**
- (`e0` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` BỘ KẾ HOẠCH VÀ ĐẦU TƯ `[CO_QUAN_BAN_HANH]`)
- (`e0` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e1` ngày 02 tháng 01 năm 2025 `[NGAY_BAN_HANH]`)
- (`e0` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e3` THÔNG TƯ `[LOAI_VAN_BAN]`)


---

### Mẫu #01_2025_TT-BKHĐT_174764#preamble_context_1 (Loại: `preamble_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[01/2025/TT-BKHĐT]`<SO_HIEU>`** của **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** . **[Căn cứ]`<TU_KHOA_PHAP_LY>`** **[Luật Thống kê]`<THAM_CHIEU_PHAP_LY>`** **[ngày 23 tháng 11 năm 2015]`<NGAY_THAM_CHIEU>`** ; Luật **[sửa đổi , bổ sung]`<TU_KHOA_PHAP_LY>`** một số điều và Phụ lục Danh mục chỉ tiêu thống kê quốc gia của Luật Thống kê ngày 12 tháng 11 năm 2021 ;

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **01/2025/TT-BKHĐT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[4:8]`)
- `[e3]` **Luật Thống kê** → `THAM_CHIEU_PHAP_LY` (span: `[10:12]`)
- `[e4]` **Căn cứ** → `TU_KHOA_PHAP_LY` (span: `[9:10]`)
- `[e5]` **sửa đổi , bổ sung** → `TU_KHOA_PHAP_LY` (span: `[20:23]`)
- `[e6]` **ngày 23 tháng 11 năm 2015** → `NGAY_THAM_CHIEU` (span: `[12:18]`)

**Quan hệ:**
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e4` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Luật Thống kê `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Luật Thống kê `[THAM_CHIEU_PHAP_LY]`)
- (`e3` Luật Thống kê `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e6` ngày 23 tháng 11 năm 2015 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #01_2025_TT-BKHĐT_174764#preamble_standalone_2 (Loại: `preamble_standalone`)
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

### Mẫu #01_2025_TT-BKHĐT_174764#preamble_context_3 (Loại: `preamble_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[01/2025/TT-BKHĐT]`<SO_HIEU>`** của **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** . **[Căn cứ]`<TU_KHOA_PHAP_LY>`** **[Luật Tài nguyên]`<THAM_CHIEU_PHAP_LY>`** , môi trường biển và hải đảo **[ngày 25 tháng 6 năm 2015]`<NGAY_THAM_CHIEU>`** ;

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **01/2025/TT-BKHĐT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[4:8]`)
- `[e3]` **Luật Tài nguyên** → `THAM_CHIEU_PHAP_LY` (span: `[10:12]`)
- `[e4]` **Căn cứ** → `TU_KHOA_PHAP_LY` (span: `[9:10]`)
- `[e5]` **ngày 25 tháng 6 năm 2015** → `NGAY_THAM_CHIEU` (span: `[17:23]`)

**Quan hệ:**
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e4` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Luật Tài nguyên `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Luật Tài nguyên `[THAM_CHIEU_PHAP_LY]`)
- (`e3` Luật Tài nguyên `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e5` ngày 25 tháng 6 năm 2015 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #01_2025_TT-BKHĐT_174764#preamble_standalone_4 (Loại: `preamble_standalone`)
> **[Căn cứ]`<TU_KHOA_PHAP_LY>`** **[Luật Tài nguyên]`<THAM_CHIEU_PHAP_LY>`** , môi trường biển và hải đảo **[ngày 25 tháng 6 năm 2015]`<NGAY_THAM_CHIEU>`** ;

**Thực thể:**
- `[e0]` **Luật Tài nguyên** → `THAM_CHIEU_PHAP_LY` (span: `[1:3]`)
- `[e1]` **Căn cứ** → `TU_KHOA_PHAP_LY` (span: `[0:1]`)
- `[e2]` **ngày 25 tháng 6 năm 2015** → `NGAY_THAM_CHIEU` (span: `[8:14]`)

**Quan hệ:**
- (`e1` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e0` Luật Tài nguyên `[THAM_CHIEU_PHAP_LY]`)
- (`e0` Luật Tài nguyên `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e2` ngày 25 tháng 6 năm 2015 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #01_2025_TT-BKHĐT_174764#preamble_context_5 (Loại: `preamble_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[01/2025/TT-BKHĐT]`<SO_HIEU>`** của **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** . **[Căn cứ]`<TU_KHOA_PHAP_LY>`** **[Luật sửa đổi , bổ sung một số điều của 37 Luật có liên quan đến quy hoạch]`<THAM_CHIEU_PHAP_LY>`** **[ngày 20 tháng 11 năm 2018]`<NGAY_THAM_CHIEU>`** ;

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **01/2025/TT-BKHĐT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[4:8]`)
- `[e3]` **Luật sửa đổi , bổ sung một số điều của 37 Luật có liên quan đến quy hoạch** → `THAM_CHIEU_PHAP_LY` (span: `[10:23]`)
- `[e4]` **Căn cứ** → `TU_KHOA_PHAP_LY` (span: `[9:10]`)
- `[e5]` **ngày 20 tháng 11 năm 2018** → `NGAY_THAM_CHIEU` (span: `[23:29]`)

**Quan hệ:**
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e4` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Luật sửa đổi , bổ sung một số điều của 37 Luật có liên quan đến quy hoạch `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Luật sửa đổi , bổ sung một số điều của 37 Luật có liên quan đến quy hoạch `[THAM_CHIEU_PHAP_LY]`)
- (`e3` Luật sửa đổi , bổ sung một số điều của 37 Luật có liên quan đến quy hoạch `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e5` ngày 20 tháng 11 năm 2018 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #01_2025_TT-BKHĐT_174764#preamble_standalone_6 (Loại: `preamble_standalone`)
> **[Căn cứ]`<TU_KHOA_PHAP_LY>`** **[Luật sửa đổi , bổ sung một số điều của 37 Luật có liên quan đến quy hoạch]`<THAM_CHIEU_PHAP_LY>`** **[ngày 20 tháng 11 năm 2018]`<NGAY_THAM_CHIEU>`** ;

**Thực thể:**
- `[e0]` **Luật sửa đổi , bổ sung một số điều của 37 Luật có liên quan đến quy hoạch** → `THAM_CHIEU_PHAP_LY` (span: `[1:14]`)
- `[e1]` **Căn cứ** → `TU_KHOA_PHAP_LY` (span: `[0:1]`)
- `[e2]` **ngày 20 tháng 11 năm 2018** → `NGAY_THAM_CHIEU` (span: `[14:20]`)

**Quan hệ:**
- (`e1` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e0` Luật sửa đổi , bổ sung một số điều của 37 Luật có liên quan đến quy hoạch `[THAM_CHIEU_PHAP_LY]`)
- (`e0` Luật sửa đổi , bổ sung một số điều của 37 Luật có liên quan đến quy hoạch `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e2` ngày 20 tháng 11 năm 2018 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #01_2025_TT-BKHĐT_174764#preamble_context_7 (Loại: `preamble_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[01/2025/TT-BKHĐT]`<SO_HIEU>`** của **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** . **[Căn cứ]`<TU_KHOA_PHAP_LY>`** **[Nghị định số 40/2016/NĐ-CP]`<THAM_CHIEU_PHAP_LY>`** **[ngày 15 tháng 5 năm 2016]`<NGAY_THAM_CHIEU>`** của **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** quy định chi tiết thi hành một số điều của Luật Tài nguyên , môi trường biển và hải đảo ;

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **01/2025/TT-BKHĐT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[4:8]`)
- `[e3]` **Nghị định số 40/2016/NĐ-CP** → `THAM_CHIEU_PHAP_LY` (span: `[10:13]`)
- `[e4]` **Căn cứ** → `TU_KHOA_PHAP_LY` (span: `[9:10]`)
- `[e5]` **ngày 15 tháng 5 năm 2016** → `NGAY_THAM_CHIEU` (span: `[13:19]`)
- `[e6]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[20:21]`)

**Quan hệ:**
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e4` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Nghị định số 40/2016/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Nghị định số 40/2016/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e3` Nghị định số 40/2016/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e5` ngày 15 tháng 5 năm 2016 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #01_2025_TT-BKHĐT_174764#preamble_standalone_8 (Loại: `preamble_standalone`)
> **[Căn cứ]`<TU_KHOA_PHAP_LY>`** **[Nghị định số 40/2016/NĐ-CP]`<THAM_CHIEU_PHAP_LY>`** **[ngày 15 tháng 5 năm 2016]`<NGAY_THAM_CHIEU>`** của **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** quy định chi tiết thi hành một số điều của Luật Tài nguyên , môi trường biển và hải đảo ;

**Thực thể:**
- `[e0]` **Nghị định số 40/2016/NĐ-CP** → `THAM_CHIEU_PHAP_LY` (span: `[1:4]`)
- `[e1]` **Căn cứ** → `TU_KHOA_PHAP_LY` (span: `[0:1]`)
- `[e2]` **ngày 15 tháng 5 năm 2016** → `NGAY_THAM_CHIEU` (span: `[4:10]`)
- `[e3]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[11:12]`)

**Quan hệ:**
- (`e1` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e0` Nghị định số 40/2016/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e3` Chính phủ `[CO_QUAN_THAM_QUYEN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e0` Nghị định số 40/2016/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e0` Nghị định số 40/2016/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e2` ngày 15 tháng 5 năm 2016 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #01_2025_TT-BKHĐT_174764#preamble_context_9 (Loại: `preamble_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[01/2025/TT-BKHĐT]`<SO_HIEU>`** của **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** . **[Căn cứ]`<TU_KHOA_PHAP_LY>`** **[Nghị định số 94/2016/NĐ-CP]`<THAM_CHIEU_PHAP_LY>`** **[ngày 01 tháng 7 năm 2016]`<NGAY_THAM_CHIEU>`** của **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** quy định chi tiết và hướng dẫn thi hành một số điều của Luật Thống kê ;

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **01/2025/TT-BKHĐT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[4:8]`)
- `[e3]` **Nghị định số 94/2016/NĐ-CP** → `THAM_CHIEU_PHAP_LY` (span: `[10:13]`)
- `[e4]` **Căn cứ** → `TU_KHOA_PHAP_LY` (span: `[9:10]`)
- `[e5]` **ngày 01 tháng 7 năm 2016** → `NGAY_THAM_CHIEU` (span: `[13:19]`)
- `[e6]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[20:21]`)

**Quan hệ:**
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e4` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Nghị định số 94/2016/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Nghị định số 94/2016/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e3` Nghị định số 94/2016/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e5` ngày 01 tháng 7 năm 2016 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #01_2025_TT-BKHĐT_174764#preamble_standalone_10 (Loại: `preamble_standalone`)
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

### Mẫu #01_2025_TT-BKHĐT_174764#preamble_context_11 (Loại: `preamble_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[01/2025/TT-BKHĐT]`<SO_HIEU>`** của **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** . **[Căn cứ]`<TU_KHOA_PHAP_LY>`** **[Nghị định số 94/2022/NĐ-CP]`<THAM_CHIEU_PHAP_LY>`** **[ngày 07 tháng 11 năm 2022]`<NGAY_THAM_CHIEU>`** của **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** quy định nội dung chỉ tiêu thống kê thuộc hệ thống chỉ tiêu thống kê quốc gia và quy trình biên soạn chỉ tiêu tổng sản phẩm trong nước , chỉ tiêu tổng sản phẩm **[trên địa bàn tỉnh]`<DIA_DIEM>`** , thành phố trực thuộc trung ương ;

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **01/2025/TT-BKHĐT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[4:8]`)
- `[e3]` **Nghị định số 94/2022/NĐ-CP** → `THAM_CHIEU_PHAP_LY` (span: `[10:13]`)
- `[e4]` **Căn cứ** → `TU_KHOA_PHAP_LY` (span: `[9:10]`)
- `[e5]` **ngày 07 tháng 11 năm 2022** → `NGAY_THAM_CHIEU` (span: `[13:19]`)
- `[e6]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[20:21]`)
- `[e7]` **trên địa bàn tỉnh** → `DIA_DIEM` (span: `[40:43]`)

**Quan hệ:**
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e4` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Nghị định số 94/2022/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Nghị định số 94/2022/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e3` Nghị định số 94/2022/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e5` ngày 07 tháng 11 năm 2022 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #01_2025_TT-BKHĐT_174764#preamble_standalone_12 (Loại: `preamble_standalone`)
> **[Căn cứ]`<TU_KHOA_PHAP_LY>`** **[Nghị định số 94/2022/NĐ-CP]`<THAM_CHIEU_PHAP_LY>`** **[ngày 07 tháng 11 năm 2022]`<NGAY_THAM_CHIEU>`** của **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** quy định nội dung chỉ tiêu thống kê thuộc hệ thống chỉ tiêu thống kê quốc gia và quy trình biên soạn chỉ tiêu tổng sản phẩm trong nước , chỉ tiêu tổng sản phẩm **[trên địa bàn tỉnh]`<DIA_DIEM>`** , thành phố trực thuộc trung ương ;

**Thực thể:**
- `[e0]` **Nghị định số 94/2022/NĐ-CP** → `THAM_CHIEU_PHAP_LY` (span: `[1:4]`)
- `[e1]` **Căn cứ** → `TU_KHOA_PHAP_LY` (span: `[0:1]`)
- `[e2]` **ngày 07 tháng 11 năm 2022** → `NGAY_THAM_CHIEU` (span: `[4:10]`)
- `[e3]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[11:12]`)
- `[e4]` **trên địa bàn tỉnh** → `DIA_DIEM` (span: `[31:34]`)

**Quan hệ:**
- (`e1` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e0` Nghị định số 94/2022/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e3` Chính phủ `[CO_QUAN_THAM_QUYEN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e0` Nghị định số 94/2022/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e0` Nghị định số 94/2022/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e2` ngày 07 tháng 11 năm 2022 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #01_2025_TT-BKHĐT_174764#preamble_context_13 (Loại: `preamble_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[01/2025/TT-BKHĐT]`<SO_HIEU>`** của **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** . **[Căn cứ]`<TU_KHOA_PHAP_LY>`** **[Nghị định số 62/2024/NĐ-CP]`<THAM_CHIEU_PHAP_LY>`** **[ngày 07 tháng 6 năm 2024]`<NGAY_THAM_CHIEU>`** của **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** về việc **[sửa đổi , bổ sung]`<TU_KHOA_PHAP_LY>`** một số điều , phụ lục của **[Nghị định số 94/2016/NĐ-CP]`<THAM_CHIEU_PHAP_LY>`** **[ngày 01 tháng 7 năm 2016]`<NGAY_THAM_CHIEU>`** của **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** quy định chi tiết và hướng dẫn thi hành một số điều của Luật Thống kê và **[Nghị định số 94/2022/NĐ-CP]`<THAM_CHIEU_PHAP_LY>`** **[ngày 07 tháng 11 năm 2022]`<NGAY_THAM_CHIEU>`** của **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** quy định nội dung chỉ tiêu thống kê thuộc hệ thống chỉ tiêu thống kê quốc gia và quy trình

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **01/2025/TT-BKHĐT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[4:8]`)
- `[e3]` **Nghị định số 62/2024/NĐ-CP** → `THAM_CHIEU_PHAP_LY` (span: `[10:13]`)
- `[e4]` **Nghị định số 94/2016/NĐ-CP** → `THAM_CHIEU_PHAP_LY` (span: `[31:34]`)
- `[e5]` **Nghị định số 94/2022/NĐ-CP** → `THAM_CHIEU_PHAP_LY` (span: `[53:56]`)
- `[e6]` **Căn cứ** → `TU_KHOA_PHAP_LY` (span: `[9:10]`)
- `[e7]` **sửa đổi , bổ sung** → `TU_KHOA_PHAP_LY` (span: `[23:26]`)
- `[e8]` **ngày 07 tháng 6 năm 2024** → `NGAY_THAM_CHIEU` (span: `[13:19]`)
- `[e9]` **ngày 01 tháng 7 năm 2016** → `NGAY_THAM_CHIEU` (span: `[34:40]`)
- `[e10]` **ngày 07 tháng 11 năm 2022** → `NGAY_THAM_CHIEU` (span: `[56:62]`)
- `[e11]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[20:21]`)
- `[e12]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[41:42]`)
- `[e13]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[63:64]`)

**Quan hệ:**
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e6` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Nghị định số 62/2024/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Nghị định số 62/2024/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e7` sửa đổi , bổ sung `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e4` Nghị định số 94/2016/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e4` Nghị định số 94/2016/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e7` sửa đổi , bổ sung `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e5` Nghị định số 94/2022/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e5` Nghị định số 94/2022/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e3` Nghị định số 62/2024/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e8` ngày 07 tháng 6 năm 2024 `[NGAY_THAM_CHIEU]`)
- (`e4` Nghị định số 94/2016/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e9` ngày 01 tháng 7 năm 2016 `[NGAY_THAM_CHIEU]`)
- (`e5` Nghị định số 94/2022/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e10` ngày 07 tháng 11 năm 2022 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #01_2025_TT-BKHĐT_174764#preamble_standalone_14 (Loại: `preamble_standalone`)
> **[Căn cứ]`<TU_KHOA_PHAP_LY>`** **[Nghị định số 62/2024/NĐ-CP]`<THAM_CHIEU_PHAP_LY>`** **[ngày 07 tháng 6 năm 2024]`<NGAY_THAM_CHIEU>`** của **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** về việc **[sửa đổi , bổ sung]`<TU_KHOA_PHAP_LY>`** một số điều , phụ lục của **[Nghị định số 94/2016/NĐ-CP]`<THAM_CHIEU_PHAP_LY>`** **[ngày 01 tháng 7 năm 2016]`<NGAY_THAM_CHIEU>`** của **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** quy định chi tiết và hướng dẫn thi hành một số điều của Luật Thống kê và **[Nghị định số 94/2022/NĐ-CP]`<THAM_CHIEU_PHAP_LY>`** **[ngày 07 tháng 11 năm 2022]`<NGAY_THAM_CHIEU>`** của **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** quy định nội dung chỉ tiêu thống kê thuộc hệ thống chỉ tiêu thống kê quốc gia và quy trình

**Thực thể:**
- `[e0]` **Nghị định số 62/2024/NĐ-CP** → `THAM_CHIEU_PHAP_LY` (span: `[1:4]`)
- `[e1]` **Nghị định số 94/2016/NĐ-CP** → `THAM_CHIEU_PHAP_LY` (span: `[22:25]`)
- `[e2]` **Nghị định số 94/2022/NĐ-CP** → `THAM_CHIEU_PHAP_LY` (span: `[44:47]`)
- `[e3]` **Căn cứ** → `TU_KHOA_PHAP_LY` (span: `[0:1]`)
- `[e4]` **sửa đổi , bổ sung** → `TU_KHOA_PHAP_LY` (span: `[14:17]`)
- `[e5]` **ngày 07 tháng 6 năm 2024** → `NGAY_THAM_CHIEU` (span: `[4:10]`)
- `[e6]` **ngày 01 tháng 7 năm 2016** → `NGAY_THAM_CHIEU` (span: `[25:31]`)
- `[e7]` **ngày 07 tháng 11 năm 2022** → `NGAY_THAM_CHIEU` (span: `[47:53]`)
- `[e8]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[11:12]`)
- `[e9]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[32:33]`)
- `[e10]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[54:55]`)

**Quan hệ:**
- (`e3` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e0` Nghị định số 62/2024/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e8` Chính phủ `[CO_QUAN_THAM_QUYEN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e0` Nghị định số 62/2024/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e4` sửa đổi , bổ sung `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e1` Nghị định số 94/2016/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e9` Chính phủ `[CO_QUAN_THAM_QUYEN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e1` Nghị định số 94/2016/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e4` sửa đổi , bổ sung `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e2` Nghị định số 94/2022/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e10` Chính phủ `[CO_QUAN_THAM_QUYEN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e2` Nghị định số 94/2022/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e0` Nghị định số 62/2024/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e5` ngày 07 tháng 6 năm 2024 `[NGAY_THAM_CHIEU]`)
- (`e1` Nghị định số 94/2016/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e6` ngày 01 tháng 7 năm 2016 `[NGAY_THAM_CHIEU]`)
- (`e2` Nghị định số 94/2022/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e7` ngày 07 tháng 11 năm 2022 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #01_2025_TT-BKHĐT_174764#body_context_15 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[01/2025/TT-BKHĐT]`<SO_HIEU>`** ban hành **[ngày 02 tháng 01 năm 2025]`<NGAY_BAN_HANH>`** bởi **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** . **[Điều 1 . Phạm vi điều chỉnh . Thông tư này quy định bộ chỉ tiêu thống kê quốc gia về biển và hải đảo và bộ chỉ tiêu đánh giá quốc gia biển mạnh của Việt Nam .]`<DIEU>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **01/2025/TT-BKHĐT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[11:15]`)
- `[e3]` **ngày 02 tháng 01 năm 2025** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 1 . Phạm vi điều chỉnh . Thông tư này quy định bộ chỉ tiêu thống kê quốc gia về biển và hải đảo và bộ chỉ tiêu đánh giá quốc gia biển mạnh của Việt Nam .** → `DIEU` (span: `[16:43]`)

**Quan hệ:**
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 02 tháng 01 năm 2025 `[NGAY_BAN_HANH]`)
- (`e4` Điều 1 . Phạm vi điều chỉnh . Thông tư này quy định bộ chỉ tiêu thống kê quốc gia về biển và hải đảo và bộ chỉ tiêu đánh giá quốc gia biển mạnh của Việt Nam . `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`)


---

### Mẫu #01_2025_TT-BKHĐT_174764#body_context_16 (Loại: `body_context`)
> **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[01/2025/TT-BKHĐT]`<SO_HIEU>`** . **[Điều 3]`<DIEU>`** . **[1 . Danh mục chỉ tiêu thống kê quốc gia về biển và hải đảo gồm 53 chỉ tiêu thống kê **[quy định tại]`<TU_KHOA_PHAP_LY>`** **[Phụ lục I]`<THAM_CHIEU_PHAP_LY>`** kèm theo Thông tư này .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[5:6]`)
- `[e1]` **01/2025/TT-BKHĐT** → `SO_HIEU` (span: `[7:8]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[0:4]`)
- `[e3]` **Điều 3** → `DIEU` (span: `[9:11]`)
- `[e4]` **1 . Danh mục chỉ tiêu thống kê quốc gia về biển và hải đảo gồm 53 chỉ tiêu thống kê quy định tại Phụ lục I kèm theo Thông tư này .** → `KHOAN` (span: `[12:35]`)
- `[e5]` **Phụ lục I** → `THAM_CHIEU_PHAP_LY` (span: `[28:30]`) *(lồng trong `e4` (`KHOAN`))*
- `[e6]` **quy định tại** → `TU_KHOA_PHAP_LY` (span: `[26:28]`) *(lồng trong `e4` (`KHOAN`))*

**Quan hệ:**
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 3 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`)
- (`e4` 1 . Danh mục chỉ tiêu thống kê quốc gia về biển và hải đảo gồm 53 chỉ tiêu thống kê quy định tại Phụ lục I kèm theo Thông tư này . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 3 `[DIEU]`)
- (`e6` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e5` Phụ lục I `[THAM_CHIEU_PHAP_LY]`)
- (`e4` 1 . Danh mục chỉ tiêu thống kê quốc gia về biển và hải đảo gồm 53 chỉ tiêu thống kê quy định tại Phụ lục I kèm theo Thông tư này . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e5` Phụ lục I `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #01_2025_TT-BKHĐT_174764#body_standalone_17 (Loại: `body_standalone`)
> **[Điều 3]`<DIEU>`** . **[1 . Danh mục chỉ tiêu thống kê quốc gia về biển và hải đảo gồm 53 chỉ tiêu thống kê **[quy định tại]`<TU_KHOA_PHAP_LY>`** **[Phụ lục I]`<THAM_CHIEU_PHAP_LY>`** kèm theo Thông tư này .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 3** → `DIEU` (span: `[0:2]`)
- `[e1]` **1 . Danh mục chỉ tiêu thống kê quốc gia về biển và hải đảo gồm 53 chỉ tiêu thống kê quy định tại Phụ lục I kèm theo Thông tư này .** → `KHOAN` (span: `[3:26]`)
- `[e2]` **Phụ lục I** → `THAM_CHIEU_PHAP_LY` (span: `[19:21]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **quy định tại** → `TU_KHOA_PHAP_LY` (span: `[17:19]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 1 . Danh mục chỉ tiêu thống kê quốc gia về biển và hải đảo gồm 53 chỉ tiêu thống kê quy định tại Phụ lục I kèm theo Thông tư này . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 3 `[DIEU]`)
- (`e3` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e2` Phụ lục I `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 1 . Danh mục chỉ tiêu thống kê quốc gia về biển và hải đảo gồm 53 chỉ tiêu thống kê quy định tại Phụ lục I kèm theo Thông tư này . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e2` Phụ lục I `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #01_2025_TT-BKHĐT_174764#body_context_18 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[01/2025/TT-BKHĐT]`<SO_HIEU>`** của **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Lao động - Thương binh và Xã hội]`<LINH_VUC>`** . **[Điều 3]`<DIEU>`** . **[2 . Danh mục chỉ tiêu đánh giá quốc gia biển mạnh gồm 28 chỉ tiêu thống kê được đánh dấu tích tại cột “ chỉ tiêu đánh giá quốc gia biển mạnh ” **[quy định tại]`<TU_KHOA_PHAP_LY>`** **[Phụ lục I]`<THAM_CHIEU_PHAP_LY>`** kèm theo Thông tư này .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **01/2025/TT-BKHĐT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[4:8]`)
- `[e3]` **Lao động - Thương binh và Xã hội** → `LINH_VUC` (span: `[10:15]`)
- `[e4]` **Điều 3** → `DIEU` (span: `[16:18]`)
- `[e5]` **2 . Danh mục chỉ tiêu đánh giá quốc gia biển mạnh gồm 28 chỉ tiêu thống kê được đánh dấu tích tại cột “ chỉ tiêu đánh giá quốc gia biển mạnh ” quy định tại Phụ lục I kèm theo Thông tư này .** → `KHOAN` (span: `[19:52]`)
- `[e6]` **Phụ lục I** → `THAM_CHIEU_PHAP_LY` (span: `[45:47]`) *(lồng trong `e5` (`KHOAN`))*
- `[e7]` **quy định tại** → `TU_KHOA_PHAP_LY` (span: `[43:45]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Lao động - Thương binh và Xã hội `[LINH_VUC]`)
- (`e4` Điều 3 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`)
- (`e5` 2 . Danh mục chỉ tiêu đánh giá quốc gia biển mạnh gồm 28 chỉ tiêu thống kê được đánh dấu tích tại cột “ chỉ tiêu đánh giá quốc gia biển mạnh ” quy định tại Phụ lục I kèm theo Thông tư này . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 3 `[DIEU]`)
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Lao động - Thương binh và Xã hội `[LINH_VUC]`)
- (`e5` 2 . Danh mục chỉ tiêu đánh giá quốc gia biển mạnh gồm 28 chỉ tiêu thống kê được đánh dấu tích tại cột “ chỉ tiêu đánh giá quốc gia biển mạnh ” quy định tại Phụ lục I kèm theo Thông tư này . `[KHOAN]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Lao động - Thương binh và Xã hội `[LINH_VUC]`)
- (`e7` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e6` Phụ lục I `[THAM_CHIEU_PHAP_LY]`)
- (`e5` 2 . Danh mục chỉ tiêu đánh giá quốc gia biển mạnh gồm 28 chỉ tiêu thống kê được đánh dấu tích tại cột “ chỉ tiêu đánh giá quốc gia biển mạnh ” quy định tại Phụ lục I kèm theo Thông tư này . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e6` Phụ lục I `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #01_2025_TT-BKHĐT_174764#body_standalone_19 (Loại: `body_standalone`)
> **[Điều 3]`<DIEU>`** . **[2 . Danh mục chỉ tiêu đánh giá quốc gia biển mạnh gồm 28 chỉ tiêu thống kê được đánh dấu tích tại cột “ chỉ tiêu đánh giá quốc gia biển mạnh ” **[quy định tại]`<TU_KHOA_PHAP_LY>`** **[Phụ lục I]`<THAM_CHIEU_PHAP_LY>`** kèm theo Thông tư này .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 3** → `DIEU` (span: `[0:2]`)
- `[e1]` **2 . Danh mục chỉ tiêu đánh giá quốc gia biển mạnh gồm 28 chỉ tiêu thống kê được đánh dấu tích tại cột “ chỉ tiêu đánh giá quốc gia biển mạnh ” quy định tại Phụ lục I kèm theo Thông tư này .** → `KHOAN` (span: `[3:36]`)
- `[e2]` **Phụ lục I** → `THAM_CHIEU_PHAP_LY` (span: `[29:31]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **quy định tại** → `TU_KHOA_PHAP_LY` (span: `[27:29]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 2 . Danh mục chỉ tiêu đánh giá quốc gia biển mạnh gồm 28 chỉ tiêu thống kê được đánh dấu tích tại cột “ chỉ tiêu đánh giá quốc gia biển mạnh ” quy định tại Phụ lục I kèm theo Thông tư này . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 3 `[DIEU]`)
- (`e3` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e2` Phụ lục I `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 2 . Danh mục chỉ tiêu đánh giá quốc gia biển mạnh gồm 28 chỉ tiêu thống kê được đánh dấu tích tại cột “ chỉ tiêu đánh giá quốc gia biển mạnh ” quy định tại Phụ lục I kèm theo Thông tư này . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e2` Phụ lục I `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #01_2025_TT-BKHĐT_174764#body_context_20 (Loại: `body_context`)
> **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[01/2025/TT-BKHĐT]`<SO_HIEU>`** . **[Điều 3]`<DIEU>`** . **[3 . Nội dung chỉ tiêu thống kê quốc gia về biển và hải đảo và chỉ tiêu đánh giá quốc gia biển mạnh **[quy định tại]`<TU_KHOA_PHAP_LY>`** **[Phụ lục II]`<THAM_CHIEU_PHAP_LY>`** kèm theo Thông tư này .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[5:6]`)
- `[e1]` **01/2025/TT-BKHĐT** → `SO_HIEU` (span: `[7:8]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[0:4]`)
- `[e3]` **Điều 3** → `DIEU` (span: `[9:11]`)
- `[e4]` **3 . Nội dung chỉ tiêu thống kê quốc gia về biển và hải đảo và chỉ tiêu đánh giá quốc gia biển mạnh quy định tại Phụ lục II kèm theo Thông tư này .** → `KHOAN` (span: `[12:37]`)
- `[e5]` **Phụ lục II** → `THAM_CHIEU_PHAP_LY` (span: `[30:32]`) *(lồng trong `e4` (`KHOAN`))*
- `[e6]` **quy định tại** → `TU_KHOA_PHAP_LY` (span: `[28:30]`) *(lồng trong `e4` (`KHOAN`))*

**Quan hệ:**
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 3 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`)
- (`e4` 3 . Nội dung chỉ tiêu thống kê quốc gia về biển và hải đảo và chỉ tiêu đánh giá quốc gia biển mạnh quy định tại Phụ lục II kèm theo Thông tư này . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 3 `[DIEU]`)
- (`e6` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e5` Phụ lục II `[THAM_CHIEU_PHAP_LY]`)
- (`e4` 3 . Nội dung chỉ tiêu thống kê quốc gia về biển và hải đảo và chỉ tiêu đánh giá quốc gia biển mạnh quy định tại Phụ lục II kèm theo Thông tư này . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e5` Phụ lục II `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #01_2025_TT-BKHĐT_174764#body_standalone_21 (Loại: `body_standalone`)
> **[Điều 3]`<DIEU>`** . **[3 . Nội dung chỉ tiêu thống kê quốc gia về biển và hải đảo và chỉ tiêu đánh giá quốc gia biển mạnh **[quy định tại]`<TU_KHOA_PHAP_LY>`** **[Phụ lục II]`<THAM_CHIEU_PHAP_LY>`** kèm theo Thông tư này .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 3** → `DIEU` (span: `[0:2]`)
- `[e1]` **3 . Nội dung chỉ tiêu thống kê quốc gia về biển và hải đảo và chỉ tiêu đánh giá quốc gia biển mạnh quy định tại Phụ lục II kèm theo Thông tư này .** → `KHOAN` (span: `[3:28]`)
- `[e2]` **Phụ lục II** → `THAM_CHIEU_PHAP_LY` (span: `[21:23]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **quy định tại** → `TU_KHOA_PHAP_LY` (span: `[19:21]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 3 . Nội dung chỉ tiêu thống kê quốc gia về biển và hải đảo và chỉ tiêu đánh giá quốc gia biển mạnh quy định tại Phụ lục II kèm theo Thông tư này . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 3 `[DIEU]`)
- (`e3` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e2` Phụ lục II `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 3 . Nội dung chỉ tiêu thống kê quốc gia về biển và hải đảo và chỉ tiêu đánh giá quốc gia biển mạnh quy định tại Phụ lục II kèm theo Thông tư này . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e2` Phụ lục II `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #01_2025_TT-BKHĐT_174764#body_context_22 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[01/2025/TT-BKHĐT]`<SO_HIEU>`** của **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Lao động - Thương binh và Xã hội]`<LINH_VUC>`** . **[Điều 4 . Tổ chức thực hiện]`<DIEU>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **01/2025/TT-BKHĐT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[4:8]`)
- `[e3]` **Lao động - Thương binh và Xã hội** → `LINH_VUC` (span: `[10:15]`)
- `[e4]` **Điều 4 . Tổ chức thực hiện** → `DIEU` (span: `[16:21]`)

**Quan hệ:**
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Lao động - Thương binh và Xã hội `[LINH_VUC]`)
- (`e4` Điều 4 . Tổ chức thực hiện `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`)
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Lao động - Thương binh và Xã hội `[LINH_VUC]`)
- (`e4` Điều 4 . Tổ chức thực hiện `[DIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Lao động - Thương binh và Xã hội `[LINH_VUC]`)


---

### Mẫu #01_2025_TT-BKHĐT_174764#body_context_23 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[01/2025/TT-BKHĐT]`<SO_HIEU>`** ban hành **[ngày 02 tháng 01 năm 2025]`<NGAY_BAN_HANH>`** bởi **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** . **[Điều 4]`<DIEU>`** . **[1 . **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_THAM_QUYEN>`** ( Tổng cục Thống kê ) chủ trì , phối hợp với các đơn vị liên quan :]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **01/2025/TT-BKHĐT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[11:15]`)
- `[e3]` **ngày 02 tháng 01 năm 2025** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 4** → `DIEU` (span: `[16:18]`)
- `[e5]` **1 . Bộ Kế hoạch và Đầu tư ( Tổng cục Thống kê ) chủ trì , phối hợp với các đơn vị liên quan :** → `KHOAN` (span: `[19:37]`)
- `[e6]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_THAM_QUYEN` (span: `[21:25]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 02 tháng 01 năm 2025 `[NGAY_BAN_HANH]`)
- (`e4` Điều 4 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`)
- (`e5` 1 . Bộ Kế hoạch và Đầu tư ( Tổng cục Thống kê ) chủ trì , phối hợp với các đơn vị liên quan : `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 4 `[DIEU]`)


---

### Mẫu #01_2025_TT-BKHĐT_174764#body_standalone_24 (Loại: `body_standalone`)
> **[Điều 4]`<DIEU>`** . **[1 . **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_THAM_QUYEN>`** ( Tổng cục Thống kê ) chủ trì , phối hợp với các đơn vị liên quan :]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 4** → `DIEU` (span: `[0:2]`)
- `[e1]` **1 . Bộ Kế hoạch và Đầu tư ( Tổng cục Thống kê ) chủ trì , phối hợp với các đơn vị liên quan :** → `KHOAN` (span: `[3:21]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_THAM_QUYEN` (span: `[5:9]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 1 . Bộ Kế hoạch và Đầu tư ( Tổng cục Thống kê ) chủ trì , phối hợp với các đơn vị liên quan : `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 4 `[DIEU]`)


---

### Mẫu #01_2025_TT-BKHĐT_174764#body_context_25 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[01/2025/TT-BKHĐT]`<SO_HIEU>`** của **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Lao động - Thương binh và Xã hội]`<LINH_VUC>`** . **[Điều 4]`<DIEU>`** . **[Khoản 1]`<KHOAN>`** . **[d ) Tổng hợp thông tin thống kê thuộc bộ chỉ tiêu thống kê quốc gia về biển và hải đảo và bộ chỉ tiêu đánh giá quốc gia biển mạnh ; theo dõi , hướng dẫn , **[báo cáo tình hình]`<GIAY_TO_HO_SO>`** thực hiện Thông tư này .]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **01/2025/TT-BKHĐT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[4:8]`)
- `[e3]` **Lao động - Thương binh và Xã hội** → `LINH_VUC` (span: `[10:15]`)
- `[e4]` **Điều 4** → `DIEU` (span: `[16:18]`)
- `[e5]` **Khoản 1** → `KHOAN` (span: `[19:21]`)
- `[e6]` **d ) Tổng hợp thông tin thống kê thuộc bộ chỉ tiêu thống kê quốc gia về biển và hải đảo và bộ chỉ tiêu đánh giá quốc gia biển mạnh ; theo dõi , hướng dẫn , báo cáo tình hình thực hiện Thông tư này .** → `DIEM` (span: `[22:54]`)
- `[e7]` **báo cáo tình hình** → `GIAY_TO_HO_SO` (span: `[48:50]`) *(lồng trong `e6` (`DIEM`))*

**Quan hệ:**
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Lao động - Thương binh và Xã hội `[LINH_VUC]`)
- (`e4` Điều 4 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`)
- (`e5` Khoản 1 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 4 `[DIEU]`)
- (`e6` d ) Tổng hợp thông tin thống kê thuộc bộ chỉ tiêu thống kê quốc gia về biển và hải đảo và bộ chỉ tiêu đánh giá quốc gia biển mạnh ; theo dõi , hướng dẫn , báo cáo tình hình thực hiện Thông tư này . `[DIEM]`) ==[ **THUOC_VE** ]==> (`e5` Khoản 1 `[KHOAN]`)
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Lao động - Thương binh và Xã hội `[LINH_VUC]`)
- (`e6` d ) Tổng hợp thông tin thống kê thuộc bộ chỉ tiêu thống kê quốc gia về biển và hải đảo và bộ chỉ tiêu đánh giá quốc gia biển mạnh ; theo dõi , hướng dẫn , báo cáo tình hình thực hiện Thông tư này . `[DIEM]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Lao động - Thương binh và Xã hội `[LINH_VUC]`)


---

### Mẫu #01_2025_TT-BKHĐT_174764#body_context_26 (Loại: `body_context`)
> **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[01/2025/TT-BKHĐT]`<SO_HIEU>`** . **[Điều 4]`<DIEU>`** . **[2 . Bộ , cơ quan ngang Bộ , cơ quan thuộc **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** , **[Ủy ban nhân dân tỉnh , thành phố trực thuộc trung ương]`<CO_QUAN_THAM_QUYEN>`** và các cơ quan có liên quan căn cứ vào bộ chỉ tiêu thống kê quốc gia về biển và hải đảo và bộ chỉ tiêu đánh giá quốc gia biển mạnh thực hiện lồng ghép , thu thập , tổng hợp những chỉ tiêu được phân công , cung cấp cho **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_THAM_QUYEN>`** ( Tổng cục Thống kê ) để tổng hợp , biên soạn .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[5:6]`)
- `[e1]` **01/2025/TT-BKHĐT** → `SO_HIEU` (span: `[7:8]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[0:4]`)
- `[e3]` **Điều 4** → `DIEU` (span: `[9:11]`)
- `[e4]` **2 . Bộ , cơ quan ngang Bộ , cơ quan thuộc Chính phủ , Ủy ban nhân dân tỉnh , thành phố trực thuộc trung ương và các cơ quan có liên quan căn cứ vào bộ chỉ tiêu thống kê quốc gia về biển và hải đảo và bộ chỉ tiêu đánh giá quốc gia biển mạnh thực hiện lồng ghép , thu thập , tổng hợp những chỉ tiêu được phân công , cung cấp cho Bộ Kế hoạch và Đầu tư ( Tổng cục Thống kê ) để tổng hợp , biên soạn .** → `KHOAN` (span: `[12:79]`)
- `[e5]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[22:23]`) *(lồng trong `e4` (`KHOAN`))*
- `[e6]` **Ủy ban nhân dân tỉnh , thành phố trực thuộc trung ương** → `CO_QUAN_THAM_QUYEN` (span: `[24:31]`) *(lồng trong `e4` (`KHOAN`))*
- `[e7]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_THAM_QUYEN` (span: `[66:70]`) *(lồng trong `e4` (`KHOAN`))*

**Quan hệ:**
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 4 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`)
- (`e4` 2 . Bộ , cơ quan ngang Bộ , cơ quan thuộc Chính phủ , Ủy ban nhân dân tỉnh , thành phố trực thuộc trung ương và các cơ quan có liên quan căn cứ vào bộ chỉ tiêu thống kê quốc gia về biển và hải đảo và bộ chỉ tiêu đánh giá quốc gia biển mạnh thực hiện lồng ghép , thu thập , tổng hợp những chỉ tiêu được phân công , cung cấp cho Bộ Kế hoạch và Đầu tư ( Tổng cục Thống kê ) để tổng hợp , biên soạn . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 4 `[DIEU]`)


---

### Mẫu #01_2025_TT-BKHĐT_174764#body_standalone_27 (Loại: `body_standalone`)
> **[Điều 4]`<DIEU>`** . **[2 . Bộ , cơ quan ngang Bộ , cơ quan thuộc **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** , **[Ủy ban nhân dân tỉnh , thành phố trực thuộc trung ương]`<CO_QUAN_THAM_QUYEN>`** và các cơ quan có liên quan căn cứ vào bộ chỉ tiêu thống kê quốc gia về biển và hải đảo và bộ chỉ tiêu đánh giá quốc gia biển mạnh thực hiện lồng ghép , thu thập , tổng hợp những chỉ tiêu được phân công , cung cấp cho **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_THAM_QUYEN>`** ( Tổng cục Thống kê ) để tổng hợp , biên soạn .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 4** → `DIEU` (span: `[0:2]`)
- `[e1]` **2 . Bộ , cơ quan ngang Bộ , cơ quan thuộc Chính phủ , Ủy ban nhân dân tỉnh , thành phố trực thuộc trung ương và các cơ quan có liên quan căn cứ vào bộ chỉ tiêu thống kê quốc gia về biển và hải đảo và bộ chỉ tiêu đánh giá quốc gia biển mạnh thực hiện lồng ghép , thu thập , tổng hợp những chỉ tiêu được phân công , cung cấp cho Bộ Kế hoạch và Đầu tư ( Tổng cục Thống kê ) để tổng hợp , biên soạn .** → `KHOAN` (span: `[3:70]`)
- `[e2]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[13:14]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **Ủy ban nhân dân tỉnh , thành phố trực thuộc trung ương** → `CO_QUAN_THAM_QUYEN` (span: `[15:22]`) *(lồng trong `e1` (`KHOAN`))*
- `[e4]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_THAM_QUYEN` (span: `[57:61]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 2 . Bộ , cơ quan ngang Bộ , cơ quan thuộc Chính phủ , Ủy ban nhân dân tỉnh , thành phố trực thuộc trung ương và các cơ quan có liên quan căn cứ vào bộ chỉ tiêu thống kê quốc gia về biển và hải đảo và bộ chỉ tiêu đánh giá quốc gia biển mạnh thực hiện lồng ghép , thu thập , tổng hợp những chỉ tiêu được phân công , cung cấp cho Bộ Kế hoạch và Đầu tư ( Tổng cục Thống kê ) để tổng hợp , biên soạn . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 4 `[DIEU]`)


---

### Mẫu #01_2025_TT-BKHĐT_174764#body_context_28 (Loại: `body_context`)
> **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[01/2025/TT-BKHĐT]`<SO_HIEU>`** . **[Điều 5 . Hiệu lực thi hành]`<DIEU>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[5:6]`)
- `[e1]` **01/2025/TT-BKHĐT** → `SO_HIEU` (span: `[7:8]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[0:4]`)
- `[e3]` **Điều 5 . Hiệu lực thi hành** → `DIEU` (span: `[9:14]`)

**Quan hệ:**
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 5 . Hiệu lực thi hành `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`)


---

### Mẫu #01_2025_TT-BKHĐT_174764#body_context_29 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[01/2025/TT-BKHĐT]`<SO_HIEU>`** ban hành **[ngày 02 tháng 01 năm 2025]`<NGAY_BAN_HANH>`** bởi **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** . **[Điều 5]`<DIEU>`** . **[2 . Trong quá trình thực hiện , nếu có vướng mắc các cơ quan , tổ chức , cá nhân gửi ý kiến về **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_THAM_QUYEN>`** ( Tổng cục Thống kê ) để kịp thời có hướng dẫn , nghiên cứu sửa đổi , bổ sung . / .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **01/2025/TT-BKHĐT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[11:15]`)
- `[e3]` **ngày 02 tháng 01 năm 2025** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 5** → `DIEU` (span: `[16:18]`)
- `[e5]` **2 . Trong quá trình thực hiện , nếu có vướng mắc các cơ quan , tổ chức , cá nhân gửi ý kiến về Bộ Kế hoạch và Đầu tư ( Tổng cục Thống kê ) để kịp thời có hướng dẫn , nghiên cứu sửa đổi , bổ sung . / .** → `KHOAN` (span: `[19:57]`)
- `[e6]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_THAM_QUYEN` (span: `[37:41]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 02 tháng 01 năm 2025 `[NGAY_BAN_HANH]`)
- (`e4` Điều 5 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`)
- (`e5` 2 . Trong quá trình thực hiện , nếu có vướng mắc các cơ quan , tổ chức , cá nhân gửi ý kiến về Bộ Kế hoạch và Đầu tư ( Tổng cục Thống kê ) để kịp thời có hướng dẫn , nghiên cứu sửa đổi , bổ sung . / . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 5 `[DIEU]`)


---

### Mẫu #01_2025_TT-BKHĐT_174764#body_standalone_30 (Loại: `body_standalone`)
> **[Điều 5]`<DIEU>`** . **[2 . Trong quá trình thực hiện , nếu có vướng mắc các cơ quan , tổ chức , cá nhân gửi ý kiến về **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_THAM_QUYEN>`** ( Tổng cục Thống kê ) để kịp thời có hướng dẫn , nghiên cứu sửa đổi , bổ sung . / .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 5** → `DIEU` (span: `[0:2]`)
- `[e1]` **2 . Trong quá trình thực hiện , nếu có vướng mắc các cơ quan , tổ chức , cá nhân gửi ý kiến về Bộ Kế hoạch và Đầu tư ( Tổng cục Thống kê ) để kịp thời có hướng dẫn , nghiên cứu sửa đổi , bổ sung . / .** → `KHOAN` (span: `[3:41]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_THAM_QUYEN` (span: `[21:25]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 2 . Trong quá trình thực hiện , nếu có vướng mắc các cơ quan , tổ chức , cá nhân gửi ý kiến về Bộ Kế hoạch và Đầu tư ( Tổng cục Thống kê ) để kịp thời có hướng dẫn , nghiên cứu sửa đổi , bổ sung . / . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 5 `[DIEU]`)


---

### Mẫu #01_2025_TT-BKHĐT_174764#body_context_31 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[01/2025/TT-BKHĐT]`<SO_HIEU>`** ban hành **[ngày 02 tháng 01 năm 2025]`<NGAY_BAN_HANH>`** bởi **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** . **[Điều 4 . Tổ chức thực hiện]`<DIEU>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **01/2025/TT-BKHĐT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[11:15]`)
- `[e3]` **ngày 02 tháng 01 năm 2025** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 4 . Tổ chức thực hiện** → `DIEU` (span: `[16:21]`)

**Quan hệ:**
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 02 tháng 01 năm 2025 `[NGAY_BAN_HANH]`)
- (`e4` Điều 4 . Tổ chức thực hiện `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`)


---

### Mẫu #01_2025_TT-BKHĐT_174764#body_context_32 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[01/2025/TT-BKHĐT]`<SO_HIEU>`** của **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Lao động - Thương binh và Xã hội]`<LINH_VUC>`** . **[Điều 5]`<DIEU>`** . **[03 . Xã hội]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **01/2025/TT-BKHĐT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[4:8]`)
- `[e3]` **Lao động - Thương binh và Xã hội** → `LINH_VUC` (span: `[10:15]`)
- `[e4]` **Điều 5** → `DIEU` (span: `[16:18]`)
- `[e5]` **03 . Xã hội** → `KHOAN` (span: `[19:22]`)

**Quan hệ:**
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Lao động - Thương binh và Xã hội `[LINH_VUC]`)
- (`e4` Điều 5 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`)
- (`e5` 03 . Xã hội `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 5 `[DIEU]`)
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Lao động - Thương binh và Xã hội `[LINH_VUC]`)
- (`e5` 03 . Xã hội `[KHOAN]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Lao động - Thương binh và Xã hội `[LINH_VUC]`)


---

### Mẫu #01_2025_TT-BKHĐT_174764#body_standalone_33 (Loại: `body_standalone`)
> **[Điều 5]`<DIEU>`** . **[03 . Xã hội]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 5** → `DIEU` (span: `[0:2]`)
- `[e1]` **03 . Xã hội** → `KHOAN` (span: `[3:6]`)

**Quan hệ:**
- (`e1` 03 . Xã hội `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 5 `[DIEU]`)


---

### Mẫu #01_2025_TT-BKHĐT_174764#body_context_34 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[01/2025/TT-BKHĐT]`<SO_HIEU>`** của **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Lao động - Thương binh và Xã hội]`<LINH_VUC>`** . **[Điều 5]`<DIEU>`** . **[2 . Kỳ công bố : Năm .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **01/2025/TT-BKHĐT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[4:8]`)
- `[e3]` **Lao động - Thương binh và Xã hội** → `LINH_VUC` (span: `[10:15]`)
- `[e4]` **Điều 5** → `DIEU` (span: `[16:18]`)
- `[e5]` **2 . Kỳ công bố : Năm .** → `KHOAN` (span: `[19:25]`)

**Quan hệ:**
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Lao động - Thương binh và Xã hội `[LINH_VUC]`)
- (`e4` Điều 5 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`)
- (`e5` 2 . Kỳ công bố : Năm . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 5 `[DIEU]`)
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Lao động - Thương binh và Xã hội `[LINH_VUC]`)
- (`e5` 2 . Kỳ công bố : Năm . `[KHOAN]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Lao động - Thương binh và Xã hội `[LINH_VUC]`)


---

### Mẫu #01_2025_TT-BKHĐT_174764#body_context_35 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[01/2025/TT-BKHĐT]`<SO_HIEU>`** ban hành **[ngày 02 tháng 01 năm 2025]`<NGAY_BAN_HANH>`** bởi **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** . **[Điều 5]`<DIEU>`** . **[4 . Cơ quan chịu trách nhiệm thu thập , tổng hợp : **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_THAM_QUYEN>`** ( Tổng cục Thống kê ) .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **01/2025/TT-BKHĐT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[11:15]`)
- `[e3]` **ngày 02 tháng 01 năm 2025** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 5** → `DIEU` (span: `[16:18]`)
- `[e5]` **4 . Cơ quan chịu trách nhiệm thu thập , tổng hợp : Bộ Kế hoạch và Đầu tư ( Tổng cục Thống kê ) .** → `KHOAN` (span: `[19:37]`)
- `[e6]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_THAM_QUYEN` (span: `[28:32]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 02 tháng 01 năm 2025 `[NGAY_BAN_HANH]`)
- (`e4` Điều 5 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`)
- (`e5` 4 . Cơ quan chịu trách nhiệm thu thập , tổng hợp : Bộ Kế hoạch và Đầu tư ( Tổng cục Thống kê ) . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 5 `[DIEU]`)


---

### Mẫu #01_2025_TT-BKHĐT_174764#body_context_36 (Loại: `body_context`)
> **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[01/2025/TT-BKHĐT]`<SO_HIEU>`** . **[Điều 5]`<DIEU>`** . **[Khoản 1 . Khái niệm , phương pháp tính]`<KHOAN>`** : **[b ) Chỉ số giáo dục]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[5:6]`)
- `[e1]` **01/2025/TT-BKHĐT** → `SO_HIEU` (span: `[7:8]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[0:4]`)
- `[e3]` **Điều 5** → `DIEU` (span: `[9:11]`)
- `[e4]` **Khoản 1 . Khái niệm , phương pháp tính** → `KHOAN` (span: `[12:19]`)
- `[e5]` **b ) Chỉ số giáo dục** → `DIEM` (span: `[20:24]`)

**Quan hệ:**
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 5 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`)
- (`e4` Khoản 1 . Khái niệm , phương pháp tính `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 5 `[DIEU]`)
- (`e5` b ) Chỉ số giáo dục `[DIEM]`) ==[ **THUOC_VE** ]==> (`e4` Khoản 1 . Khái niệm , phương pháp tính `[KHOAN]`)


---

### Mẫu #01_2025_TT-BKHĐT_174764#body_standalone_37 (Loại: `body_standalone`)
> **[Điều 5]`<DIEU>`** . **[Khoản 1 . Khái niệm , phương pháp tính]`<KHOAN>`** : **[b ) Chỉ số giáo dục]`<DIEM>`**

**Thực thể:**
- `[e0]` **Điều 5** → `DIEU` (span: `[0:2]`)
- `[e1]` **Khoản 1 . Khái niệm , phương pháp tính** → `KHOAN` (span: `[3:10]`)
- `[e2]` **b ) Chỉ số giáo dục** → `DIEM` (span: `[11:15]`)

**Quan hệ:**
- (`e1` Khoản 1 . Khái niệm , phương pháp tính `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 5 `[DIEU]`)
- (`e2` b ) Chỉ số giáo dục `[DIEM]`) ==[ **THUOC_VE** ]==> (`e1` Khoản 1 . Khái niệm , phương pháp tính `[KHOAN]`)


---

### Mẫu #01_2025_TT-BKHĐT_174764#body_context_38 (Loại: `body_context`)
> **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[01/2025/TT-BKHĐT]`<SO_HIEU>`** . **[Điều 5]`<DIEU>`** . **[Khoản 1 . Khái niệm , phương pháp tính]`<KHOAN>`** : **[c ) Chỉ số **[thu nhập]`<TAI_SAN_VAT_CHAT>`**]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[5:6]`)
- `[e1]` **01/2025/TT-BKHĐT** → `SO_HIEU` (span: `[7:8]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[0:4]`)
- `[e3]` **Điều 5** → `DIEU` (span: `[9:11]`)
- `[e4]` **Khoản 1 . Khái niệm , phương pháp tính** → `KHOAN` (span: `[12:19]`)
- `[e5]` **c ) Chỉ số thu nhập** → `DIEM` (span: `[20:24]`)
- `[e6]` **thu nhập** → `TAI_SAN_VAT_CHAT` (span: `[23:24]`) *(lồng trong `e5` (`DIEM`))*

**Quan hệ:**
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 5 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`)
- (`e4` Khoản 1 . Khái niệm , phương pháp tính `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 5 `[DIEU]`)
- (`e5` c ) Chỉ số thu nhập `[DIEM]`) ==[ **THUOC_VE** ]==> (`e4` Khoản 1 . Khái niệm , phương pháp tính `[KHOAN]`)


---

### Mẫu #01_2025_TT-BKHĐT_174764#body_context_39 (Loại: `body_context`)
> **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[01/2025/TT-BKHĐT]`<SO_HIEU>`** . **[Điều 5]`<DIEU>`** . **[4 . Nguồn số liệu]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[5:6]`)
- `[e1]` **01/2025/TT-BKHĐT** → `SO_HIEU` (span: `[7:8]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[0:4]`)
- `[e3]` **Điều 5** → `DIEU` (span: `[9:11]`)
- `[e4]` **4 . Nguồn số liệu** → `KHOAN` (span: `[12:16]`)

**Quan hệ:**
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 5 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`)
- (`e4` 4 . Nguồn số liệu `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 5 `[DIEU]`)


---

### Mẫu #01_2025_TT-BKHĐT_174764#body_context_40 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[01/2025/TT-BKHĐT]`<SO_HIEU>`** của **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Lao động - Thương binh và Xã hội]`<LINH_VUC>`** . **[Điều 5]`<DIEU>`** . **[5 . Cơ quan chịu trách nhiệm thu thập , tổng hợp : **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_THAM_QUYEN>`** ( Tổng cục Thống kê ) .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **01/2025/TT-BKHĐT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[4:8]`)
- `[e3]` **Lao động - Thương binh và Xã hội** → `LINH_VUC` (span: `[10:15]`)
- `[e4]` **Điều 5** → `DIEU` (span: `[16:18]`)
- `[e5]` **5 . Cơ quan chịu trách nhiệm thu thập , tổng hợp : Bộ Kế hoạch và Đầu tư ( Tổng cục Thống kê ) .** → `KHOAN` (span: `[19:37]`)
- `[e6]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_THAM_QUYEN` (span: `[28:32]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Lao động - Thương binh và Xã hội `[LINH_VUC]`)
- (`e4` Điều 5 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`)
- (`e5` 5 . Cơ quan chịu trách nhiệm thu thập , tổng hợp : Bộ Kế hoạch và Đầu tư ( Tổng cục Thống kê ) . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 5 `[DIEU]`)
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Lao động - Thương binh và Xã hội `[LINH_VUC]`)
- (`e5` 5 . Cơ quan chịu trách nhiệm thu thập , tổng hợp : Bộ Kế hoạch và Đầu tư ( Tổng cục Thống kê ) . `[KHOAN]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Lao động - Thương binh và Xã hội `[LINH_VUC]`)


---

### Mẫu #01_2025_TT-BKHĐT_174764#body_context_41 (Loại: `body_context`)
> **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[01/2025/TT-BKHĐT]`<SO_HIEU>`** . **[Điều 5]`<DIEU>`** . **[0202 . Số lượng **[cơ sở dịch vụ hậu cần nghề cá]`<TO_CHUC_DOANH_NGHIEP>`**]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[5:6]`)
- `[e1]` **01/2025/TT-BKHĐT** → `SO_HIEU` (span: `[7:8]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[0:4]`)
- `[e3]` **Điều 5** → `DIEU` (span: `[9:11]`)
- `[e4]` **0202 . Số lượng cơ sở dịch vụ hậu cần nghề cá** → `KHOAN` (span: `[12:20]`)
- `[e5]` **cơ sở dịch vụ hậu cần nghề cá** → `TO_CHUC_DOANH_NGHIEP` (span: `[15:20]`) *(lồng trong `e4` (`KHOAN`))*

**Quan hệ:**
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 5 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`)
- (`e4` 0202 . Số lượng cơ sở dịch vụ hậu cần nghề cá `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 5 `[DIEU]`)


---

### Mẫu #01_2025_TT-BKHĐT_174764#body_context_42 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[01/2025/TT-BKHĐT]`<SO_HIEU>`** ban hành **[ngày 02 tháng 01 năm 2025]`<NGAY_BAN_HANH>`** bởi **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** . **[Điều 5]`<DIEU>`** . **[5 . Đơn vị chịu trách nhiệm thu thập , tổng hợp : **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_THAM_QUYEN>`** ( Tổng cục Thống kê ) .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **01/2025/TT-BKHĐT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[11:15]`)
- `[e3]` **ngày 02 tháng 01 năm 2025** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 5** → `DIEU` (span: `[16:18]`)
- `[e5]` **5 . Đơn vị chịu trách nhiệm thu thập , tổng hợp : Bộ Kế hoạch và Đầu tư ( Tổng cục Thống kê ) .** → `KHOAN` (span: `[19:37]`)
- `[e6]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_THAM_QUYEN` (span: `[28:32]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 02 tháng 01 năm 2025 `[NGAY_BAN_HANH]`)
- (`e4` Điều 5 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`)
- (`e5` 5 . Đơn vị chịu trách nhiệm thu thập , tổng hợp : Bộ Kế hoạch và Đầu tư ( Tổng cục Thống kê ) . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 5 `[DIEU]`)


---

### Mẫu #01_2025_TT-BKHĐT_174764#body_context_43 (Loại: `body_context`)
> **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[01/2025/TT-BKHĐT]`<SO_HIEU>`** . **[Điều 5]`<DIEU>`** . **[0204 . Số lượng tàu khai thác thủy sản biển có động cơ]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[5:6]`)
- `[e1]` **01/2025/TT-BKHĐT** → `SO_HIEU` (span: `[7:8]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[0:4]`)
- `[e3]` **Điều 5** → `DIEU` (span: `[9:11]`)
- `[e4]` **0204 . Số lượng tàu khai thác thủy sản biển có động cơ** → `KHOAN` (span: `[12:21]`)

**Quan hệ:**
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 5 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`)
- (`e4` 0204 . Số lượng tàu khai thác thủy sản biển có động cơ `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 5 `[DIEU]`)


---

### Mẫu #01_2025_TT-BKHĐT_174764#body_context_44 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[01/2025/TT-BKHĐT]`<SO_HIEU>`** của **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Lao động - Thương binh và Xã hội]`<LINH_VUC>`** . **[Điều 5]`<DIEU>`** . **[0206 . Số lượng **[tàu biển]`<TAI_SAN_VAT_CHAT>`**]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **01/2025/TT-BKHĐT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[4:8]`)
- `[e3]` **Lao động - Thương binh và Xã hội** → `LINH_VUC` (span: `[10:15]`)
- `[e4]` **Điều 5** → `DIEU` (span: `[16:18]`)
- `[e5]` **0206 . Số lượng tàu biển** → `KHOAN` (span: `[19:23]`)
- `[e6]` **tàu biển** → `TAI_SAN_VAT_CHAT` (span: `[22:23]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Lao động - Thương binh và Xã hội `[LINH_VUC]`)
- (`e4` Điều 5 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`)
- (`e5` 0206 . Số lượng tàu biển `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 5 `[DIEU]`)
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Lao động - Thương binh và Xã hội `[LINH_VUC]`)
- (`e5` 0206 . Số lượng tàu biển `[KHOAN]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Lao động - Thương binh và Xã hội `[LINH_VUC]`)


---

### Mẫu #01_2025_TT-BKHĐT_174764#body_context_45 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[01/2025/TT-BKHĐT]`<SO_HIEU>`** ban hành **[ngày 02 tháng 01 năm 2025]`<NGAY_BAN_HANH>`** bởi **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** . **[Điều 5]`<DIEU>`** . **[4 . Nguồn số liệu : Chế độ báo cáo thống kê **[ngành giao thông vận tải]`<LINH_VUC>`** .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **01/2025/TT-BKHĐT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[11:15]`)
- `[e3]` **ngày 02 tháng 01 năm 2025** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 5** → `DIEU` (span: `[16:18]`)
- `[e5]` **4 . Nguồn số liệu : Chế độ báo cáo thống kê ngành giao thông vận tải .** → `KHOAN` (span: `[19:31]`)
- `[e6]` **ngành giao thông vận tải** → `LINH_VUC` (span: `[27:30]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 02 tháng 01 năm 2025 `[NGAY_BAN_HANH]`)
- (`e4` Điều 5 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`)
- (`e5` 4 . Nguồn số liệu : Chế độ báo cáo thống kê ngành giao thông vận tải . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 5 `[DIEU]`)
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e6` ngành giao thông vận tải `[LINH_VUC]`)
- (`e5` 4 . Nguồn số liệu : Chế độ báo cáo thống kê ngành giao thông vận tải . `[KHOAN]`) ==[ **THUOC_LINH_VUC** ]==> (`e6` ngành giao thông vận tải `[LINH_VUC]`) *(Quan hệ lồng nhau)*


---

### Mẫu #01_2025_TT-BKHĐT_174764#body_standalone_46 (Loại: `body_standalone`)
> **[Điều 5]`<DIEU>`** . **[4 . Nguồn số liệu : Chế độ báo cáo thống kê **[ngành giao thông vận tải]`<LINH_VUC>`** .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 5** → `DIEU` (span: `[0:2]`)
- `[e1]` **4 . Nguồn số liệu : Chế độ báo cáo thống kê ngành giao thông vận tải .** → `KHOAN` (span: `[3:15]`)
- `[e2]` **ngành giao thông vận tải** → `LINH_VUC` (span: `[11:14]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 4 . Nguồn số liệu : Chế độ báo cáo thống kê ngành giao thông vận tải . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 5 `[DIEU]`)
- (`e1` 4 . Nguồn số liệu : Chế độ báo cáo thống kê ngành giao thông vận tải . `[KHOAN]`) ==[ **THUOC_LINH_VUC** ]==> (`e2` ngành giao thông vận tải `[LINH_VUC]`) *(Quan hệ lồng nhau)*


---

### Mẫu #01_2025_TT-BKHĐT_174764#body_context_47 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[01/2025/TT-BKHĐT]`<SO_HIEU>`** của **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Lao động - Thương binh và Xã hội]`<LINH_VUC>`** . **[Điều 5]`<DIEU>`** . **[2 . Phân tổ chủ yếu : Loại cảng biển .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **01/2025/TT-BKHĐT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[4:8]`)
- `[e3]` **Lao động - Thương binh và Xã hội** → `LINH_VUC` (span: `[10:15]`)
- `[e4]` **Điều 5** → `DIEU` (span: `[16:18]`)
- `[e5]` **2 . Phân tổ chủ yếu : Loại cảng biển .** → `KHOAN` (span: `[19:29]`)

**Quan hệ:**
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Lao động - Thương binh và Xã hội `[LINH_VUC]`)
- (`e4` Điều 5 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`)
- (`e5` 2 . Phân tổ chủ yếu : Loại cảng biển . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 5 `[DIEU]`)
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Lao động - Thương binh và Xã hội `[LINH_VUC]`)
- (`e5` 2 . Phân tổ chủ yếu : Loại cảng biển . `[KHOAN]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Lao động - Thương binh và Xã hội `[LINH_VUC]`)


---

### Mẫu #01_2025_TT-BKHĐT_174764#body_context_48 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[01/2025/TT-BKHĐT]`<SO_HIEU>`** của **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Lao động - Thương binh và Xã hội]`<LINH_VUC>`** . **[Điều 5]`<DIEU>`** . **[0208 . Số **[cơ sở lưu trú du lịch biển]`<TO_CHUC_DOANH_NGHIEP>`**]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **01/2025/TT-BKHĐT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[4:8]`)
- `[e3]` **Lao động - Thương binh và Xã hội** → `LINH_VUC` (span: `[10:15]`)
- `[e4]` **Điều 5** → `DIEU` (span: `[16:18]`)
- `[e5]` **0208 . Số cơ sở lưu trú du lịch biển** → `KHOAN` (span: `[19:26]`)
- `[e6]` **cơ sở lưu trú du lịch biển** → `TO_CHUC_DOANH_NGHIEP` (span: `[22:26]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Lao động - Thương binh và Xã hội `[LINH_VUC]`)
- (`e4` Điều 5 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`)
- (`e5` 0208 . Số cơ sở lưu trú du lịch biển `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 5 `[DIEU]`)
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Lao động - Thương binh và Xã hội `[LINH_VUC]`)
- (`e5` 0208 . Số cơ sở lưu trú du lịch biển `[KHOAN]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Lao động - Thương binh và Xã hội `[LINH_VUC]`)


---

### Mẫu #01_2025_TT-BKHĐT_174764#body_context_49 (Loại: `body_context`)
> **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[01/2025/TT-BKHĐT]`<SO_HIEU>`** . **[Điều 5]`<DIEU>`** . **[0209 . Số buồng của **[cơ sở lưu trú du lịch biển]`<TO_CHUC_DOANH_NGHIEP>`**]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[5:6]`)
- `[e1]` **01/2025/TT-BKHĐT** → `SO_HIEU` (span: `[7:8]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[0:4]`)
- `[e3]` **Điều 5** → `DIEU` (span: `[9:11]`)
- `[e4]` **0209 . Số buồng của cơ sở lưu trú du lịch biển** → `KHOAN` (span: `[12:21]`)
- `[e5]` **cơ sở lưu trú du lịch biển** → `TO_CHUC_DOANH_NGHIEP` (span: `[17:21]`) *(lồng trong `e4` (`KHOAN`))*

**Quan hệ:**
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 5 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`)
- (`e4` 0209 . Số buồng của cơ sở lưu trú du lịch biển `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 5 `[DIEU]`)


---

### Mẫu #01_2025_TT-BKHĐT_174764#body_standalone_50 (Loại: `body_standalone`)
> **[Điều 5]`<DIEU>`** . **[0209 . Số buồng của **[cơ sở lưu trú du lịch biển]`<TO_CHUC_DOANH_NGHIEP>`**]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 5** → `DIEU` (span: `[0:2]`)
- `[e1]` **0209 . Số buồng của cơ sở lưu trú du lịch biển** → `KHOAN` (span: `[3:12]`)
- `[e2]` **cơ sở lưu trú du lịch biển** → `TO_CHUC_DOANH_NGHIEP` (span: `[8:12]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 0209 . Số buồng của cơ sở lưu trú du lịch biển `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 5 `[DIEU]`)


---

### Mẫu #01_2025_TT-BKHĐT_174764#body_context_51 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[01/2025/TT-BKHĐT]`<SO_HIEU>`** ban hành **[ngày 02 tháng 01 năm 2025]`<NGAY_BAN_HANH>`** bởi **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** . **[Điều 5]`<DIEU>`** . **[Khoản 1 . Khái niệm , phương pháp tính]`<KHOAN>`** : **[a ) Số lượt hành khách vận chuyển đường biển]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **01/2025/TT-BKHĐT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[11:15]`)
- `[e3]` **ngày 02 tháng 01 năm 2025** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 5** → `DIEU` (span: `[16:18]`)
- `[e5]` **Khoản 1 . Khái niệm , phương pháp tính** → `KHOAN` (span: `[19:26]`)
- `[e6]` **a ) Số lượt hành khách vận chuyển đường biển** → `DIEM` (span: `[27:34]`)

**Quan hệ:**
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 02 tháng 01 năm 2025 `[NGAY_BAN_HANH]`)
- (`e4` Điều 5 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`)
- (`e5` Khoản 1 . Khái niệm , phương pháp tính `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 5 `[DIEU]`)
- (`e6` a ) Số lượt hành khách vận chuyển đường biển `[DIEM]`) ==[ **THUOC_VE** ]==> (`e5` Khoản 1 . Khái niệm , phương pháp tính `[KHOAN]`)


---

### Mẫu #01_2025_TT-BKHĐT_174764#body_context_52 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[01/2025/TT-BKHĐT]`<SO_HIEU>`** của **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Lao động - Thương binh và Xã hội]`<LINH_VUC>`** . **[Điều 5]`<DIEU>`** . **[0212 . Khối lượng **[hàng hóa]`<TAI_SAN_VAT_CHAT>`** vận chuyển và luân chuyển đường biển]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **01/2025/TT-BKHĐT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[4:8]`)
- `[e3]` **Lao động - Thương binh và Xã hội** → `LINH_VUC` (span: `[10:15]`)
- `[e4]` **Điều 5** → `DIEU` (span: `[16:18]`)
- `[e5]` **0212 . Khối lượng hàng hóa vận chuyển và luân chuyển đường biển** → `KHOAN` (span: `[19:27]`)
- `[e6]` **hàng hóa** → `TAI_SAN_VAT_CHAT` (span: `[22:23]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Lao động - Thương binh và Xã hội `[LINH_VUC]`)
- (`e4` Điều 5 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`)
- (`e5` 0212 . Khối lượng hàng hóa vận chuyển và luân chuyển đường biển `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 5 `[DIEU]`)
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Lao động - Thương binh và Xã hội `[LINH_VUC]`)
- (`e5` 0212 . Khối lượng hàng hóa vận chuyển và luân chuyển đường biển `[KHOAN]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Lao động - Thương binh và Xã hội `[LINH_VUC]`)


---

### Mẫu #01_2025_TT-BKHĐT_174764#body_context_53 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[01/2025/TT-BKHĐT]`<SO_HIEU>`** ban hành **[ngày 02 tháng 01 năm 2025]`<NGAY_BAN_HANH>`** bởi **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** . **[Điều 5]`<DIEU>`** . **[Khoản 1 . Khái niệm , phương pháp tính]`<KHOAN>`** : **[b ) Khối lượng **[hàng hóa]`<TAI_SAN_VAT_CHAT>`** luân chuyển đường biển]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **01/2025/TT-BKHĐT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[11:15]`)
- `[e3]` **ngày 02 tháng 01 năm 2025** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 5** → `DIEU` (span: `[16:18]`)
- `[e5]` **Khoản 1 . Khái niệm , phương pháp tính** → `KHOAN` (span: `[19:26]`)
- `[e6]` **b ) Khối lượng hàng hóa luân chuyển đường biển** → `DIEM` (span: `[27:33]`)
- `[e7]` **hàng hóa** → `TAI_SAN_VAT_CHAT` (span: `[30:31]`) *(lồng trong `e6` (`DIEM`))*

**Quan hệ:**
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 02 tháng 01 năm 2025 `[NGAY_BAN_HANH]`)
- (`e4` Điều 5 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`)
- (`e5` Khoản 1 . Khái niệm , phương pháp tính `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 5 `[DIEU]`)
- (`e6` b ) Khối lượng hàng hóa luân chuyển đường biển `[DIEM]`) ==[ **THUOC_VE** ]==> (`e5` Khoản 1 . Khái niệm , phương pháp tính `[KHOAN]`)


---

### Mẫu #01_2025_TT-BKHĐT_174764#body_context_54 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[01/2025/TT-BKHĐT]`<SO_HIEU>`** ban hành **[ngày 02 tháng 01 năm 2025]`<NGAY_BAN_HANH>`** bởi **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** . **[Điều 5]`<DIEU>`** . **[0213 . Khối lượng **[hàng hóa]`<TAI_SAN_VAT_CHAT>`** thông qua cảng biển]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **01/2025/TT-BKHĐT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[11:15]`)
- `[e3]` **ngày 02 tháng 01 năm 2025** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 5** → `DIEU` (span: `[16:18]`)
- `[e5]` **0213 . Khối lượng hàng hóa thông qua cảng biển** → `KHOAN` (span: `[19:26]`)
- `[e6]` **hàng hóa** → `TAI_SAN_VAT_CHAT` (span: `[22:23]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 02 tháng 01 năm 2025 `[NGAY_BAN_HANH]`)
- (`e4` Điều 5 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`)
- (`e5` 0213 . Khối lượng hàng hóa thông qua cảng biển `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 5 `[DIEU]`)


---

### Mẫu #01_2025_TT-BKHĐT_174764#body_standalone_55 (Loại: `body_standalone`)
> **[Điều 5]`<DIEU>`** . **[0213 . Khối lượng **[hàng hóa]`<TAI_SAN_VAT_CHAT>`** thông qua cảng biển]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 5** → `DIEU` (span: `[0:2]`)
- `[e1]` **0213 . Khối lượng hàng hóa thông qua cảng biển** → `KHOAN` (span: `[3:10]`)
- `[e2]` **hàng hóa** → `TAI_SAN_VAT_CHAT` (span: `[6:7]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 0213 . Khối lượng hàng hóa thông qua cảng biển `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 5 `[DIEU]`)


---

### Mẫu #01_2025_TT-BKHĐT_174764#body_context_56 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[01/2025/TT-BKHĐT]`<SO_HIEU>`** ban hành **[ngày 02 tháng 01 năm 2025]`<NGAY_BAN_HANH>`** bởi **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** . **[Điều 5]`<DIEU>`** . **[0214 . Diện tích mặt nước nuôi trồng thủy sản biển]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **01/2025/TT-BKHĐT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[11:15]`)
- `[e3]` **ngày 02 tháng 01 năm 2025** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 5** → `DIEU` (span: `[16:18]`)
- `[e5]` **0214 . Diện tích mặt nước nuôi trồng thủy sản biển** → `KHOAN` (span: `[19:26]`)

**Quan hệ:**
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 02 tháng 01 năm 2025 `[NGAY_BAN_HANH]`)
- (`e4` Điều 5 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`)
- (`e5` 0214 . Diện tích mặt nước nuôi trồng thủy sản biển `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 5 `[DIEU]`)


---

### Mẫu #01_2025_TT-BKHĐT_174764#body_context_57 (Loại: `body_context`)
> **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[01/2025/TT-BKHĐT]`<SO_HIEU>`** . **[Điều 5]`<DIEU>`** . **[4 . Nguồn số liệu : Điều tra thuỷ sản .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[5:6]`)
- `[e1]` **01/2025/TT-BKHĐT** → `SO_HIEU` (span: `[7:8]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[0:4]`)
- `[e3]` **Điều 5** → `DIEU` (span: `[9:11]`)
- `[e4]` **4 . Nguồn số liệu : Điều tra thuỷ sản .** → `KHOAN` (span: `[12:20]`)

**Quan hệ:**
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 5 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`)
- (`e4` 4 . Nguồn số liệu : Điều tra thuỷ sản . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 5 `[DIEU]`)


---

### Mẫu #01_2025_TT-BKHĐT_174764#body_context_58 (Loại: `body_context`)
> **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[01/2025/TT-BKHĐT]`<SO_HIEU>`** . **[Điều 5]`<DIEU>`** . **[0221 . Trị giá xuất khẩu thủy sản biển]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[5:6]`)
- `[e1]` **01/2025/TT-BKHĐT** → `SO_HIEU` (span: `[7:8]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[0:4]`)
- `[e3]` **Điều 5** → `DIEU` (span: `[9:11]`)
- `[e4]` **0221 . Trị giá xuất khẩu thủy sản biển** → `KHOAN` (span: `[12:18]`)

**Quan hệ:**
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 5 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`)
- (`e4` 0221 . Trị giá xuất khẩu thủy sản biển `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 5 `[DIEU]`)


---

### Mẫu #01_2025_TT-BKHĐT_174764#body_context_59 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[01/2025/TT-BKHĐT]`<SO_HIEU>`** của **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Lao động - Thương binh và Xã hội]`<LINH_VUC>`** . **[Điều 5]`<DIEU>`** . **[0223 . Doanh thu từ điện gió , điện thủy triều]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **01/2025/TT-BKHĐT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[4:8]`)
- `[e3]` **Lao động - Thương binh và Xã hội** → `LINH_VUC` (span: `[10:15]`)
- `[e4]` **Điều 5** → `DIEU` (span: `[16:18]`)
- `[e5]` **0223 . Doanh thu từ điện gió , điện thủy triều** → `KHOAN` (span: `[19:28]`)

**Quan hệ:**
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Lao động - Thương binh và Xã hội `[LINH_VUC]`)
- (`e4` Điều 5 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`)
- (`e5` 0223 . Doanh thu từ điện gió , điện thủy triều `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 5 `[DIEU]`)
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Lao động - Thương binh và Xã hội `[LINH_VUC]`)
- (`e5` 0223 . Doanh thu từ điện gió , điện thủy triều `[KHOAN]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Lao động - Thương binh và Xã hội `[LINH_VUC]`)


---

### Mẫu #01_2025_TT-BKHĐT_174764#body_standalone_60 (Loại: `body_standalone`)
> **[Điều 5]`<DIEU>`** . **[0223 . Doanh thu từ điện gió , điện thủy triều]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 5** → `DIEU` (span: `[0:2]`)
- `[e1]` **0223 . Doanh thu từ điện gió , điện thủy triều** → `KHOAN` (span: `[3:12]`)

**Quan hệ:**
- (`e1` 0223 . Doanh thu từ điện gió , điện thủy triều `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 5 `[DIEU]`)


---

### Mẫu #01_2025_TT-BKHĐT_174764#body_context_61 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[01/2025/TT-BKHĐT]`<SO_HIEU>`** của **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Lao động - Thương binh và Xã hội]`<LINH_VUC>`** . **[Điều 5]`<DIEU>`** . **[Khoản 1 . Khái niệm , phương pháp tính]`<KHOAN>`** : **[a ) Công suất lắp đặt và sản lượng điện từ năng lượng gió]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **01/2025/TT-BKHĐT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[4:8]`)
- `[e3]` **Lao động - Thương binh và Xã hội** → `LINH_VUC` (span: `[10:15]`)
- `[e4]` **Điều 5** → `DIEU` (span: `[16:18]`)
- `[e5]` **Khoản 1 . Khái niệm , phương pháp tính** → `KHOAN` (span: `[19:26]`)
- `[e6]` **a ) Công suất lắp đặt và sản lượng điện từ năng lượng gió** → `DIEM` (span: `[27:37]`)

**Quan hệ:**
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Lao động - Thương binh và Xã hội `[LINH_VUC]`)
- (`e4` Điều 5 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`)
- (`e5` Khoản 1 . Khái niệm , phương pháp tính `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 5 `[DIEU]`)
- (`e6` a ) Công suất lắp đặt và sản lượng điện từ năng lượng gió `[DIEM]`) ==[ **THUOC_VE** ]==> (`e5` Khoản 1 . Khái niệm , phương pháp tính `[KHOAN]`)
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Lao động - Thương binh và Xã hội `[LINH_VUC]`)
- (`e6` a ) Công suất lắp đặt và sản lượng điện từ năng lượng gió `[DIEM]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Lao động - Thương binh và Xã hội `[LINH_VUC]`)


---

### Mẫu #01_2025_TT-BKHĐT_174764#body_context_62 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[01/2025/TT-BKHĐT]`<SO_HIEU>`** của **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Lao động - Thương binh và Xã hội]`<LINH_VUC>`** . **[Điều 5]`<DIEU>`** . **[0225 . Tỷ lệ năng lượng từ gió , thủy triều trong tổng cung năng lượng sơ cấp]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **01/2025/TT-BKHĐT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[4:8]`)
- `[e3]` **Lao động - Thương binh và Xã hội** → `LINH_VUC` (span: `[10:15]`)
- `[e4]` **Điều 5** → `DIEU` (span: `[16:18]`)
- `[e5]` **0225 . Tỷ lệ năng lượng từ gió , thủy triều trong tổng cung năng lượng sơ cấp** → `KHOAN` (span: `[19:31]`)

**Quan hệ:**
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Lao động - Thương binh và Xã hội `[LINH_VUC]`)
- (`e4` Điều 5 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`)
- (`e5` 0225 . Tỷ lệ năng lượng từ gió , thủy triều trong tổng cung năng lượng sơ cấp `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 5 `[DIEU]`)
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Lao động - Thương binh và Xã hội `[LINH_VUC]`)
- (`e5` 0225 . Tỷ lệ năng lượng từ gió , thủy triều trong tổng cung năng lượng sơ cấp `[KHOAN]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Lao động - Thương binh và Xã hội `[LINH_VUC]`)


---

### Mẫu #01_2025_TT-BKHĐT_174764#body_context_63 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[01/2025/TT-BKHĐT]`<SO_HIEU>`** của **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Lao động - Thương binh và Xã hội]`<LINH_VUC>`** . **[Điều 5]`<DIEU>`** . **[0228 . Tỷ lệ đóng góp tổng sản phẩm trên địa bàn của các tỉnh , thành phố trực thuộc trung ương có biển trong tổng sản phẩm trong nước]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **01/2025/TT-BKHĐT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[4:8]`)
- `[e3]` **Lao động - Thương binh và Xã hội** → `LINH_VUC` (span: `[10:15]`)
- `[e4]` **Điều 5** → `DIEU` (span: `[16:18]`)
- `[e5]` **0228 . Tỷ lệ đóng góp tổng sản phẩm trên địa bàn của các tỉnh , thành phố trực thuộc trung ương có biển trong tổng sản phẩm trong nước** → `KHOAN` (span: `[19:39]`)

**Quan hệ:**
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Lao động - Thương binh và Xã hội `[LINH_VUC]`)
- (`e4` Điều 5 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`)
- (`e5` 0228 . Tỷ lệ đóng góp tổng sản phẩm trên địa bàn của các tỉnh , thành phố trực thuộc trung ương có biển trong tổng sản phẩm trong nước `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 5 `[DIEU]`)
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Lao động - Thương binh và Xã hội `[LINH_VUC]`)
- (`e5` 0228 . Tỷ lệ đóng góp tổng sản phẩm trên địa bàn của các tỉnh , thành phố trực thuộc trung ương có biển trong tổng sản phẩm trong nước `[KHOAN]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Lao động - Thương binh và Xã hội `[LINH_VUC]`)


---

### Mẫu #01_2025_TT-BKHĐT_174764#body_standalone_64 (Loại: `body_standalone`)
> **[Điều 5]`<DIEU>`** . **[0228 . Tỷ lệ đóng góp tổng sản phẩm trên địa bàn của các tỉnh , thành phố trực thuộc trung ương có biển trong tổng sản phẩm trong nước]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 5** → `DIEU` (span: `[0:2]`)
- `[e1]` **0228 . Tỷ lệ đóng góp tổng sản phẩm trên địa bàn của các tỉnh , thành phố trực thuộc trung ương có biển trong tổng sản phẩm trong nước** → `KHOAN` (span: `[3:23]`)

**Quan hệ:**
- (`e1` 0228 . Tỷ lệ đóng góp tổng sản phẩm trên địa bàn của các tỉnh , thành phố trực thuộc trung ương có biển trong tổng sản phẩm trong nước `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 5 `[DIEU]`)


---

### Mẫu #01_2025_TT-BKHĐT_174764#body_context_65 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[01/2025/TT-BKHĐT]`<SO_HIEU>`** ban hành **[ngày 02 tháng 01 năm 2025]`<NGAY_BAN_HANH>`** bởi **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** . **[Điều 5]`<DIEU>`** . **[0301 . **[Thu nhập]`<TAI_SAN_VAT_CHAT>`** bình quân đầu người 01 tháng của các tỉnh , thành phố trực thuộc trung ương có biển]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **01/2025/TT-BKHĐT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[11:15]`)
- `[e3]` **ngày 02 tháng 01 năm 2025** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 5** → `DIEU` (span: `[16:18]`)
- `[e5]` **0301 . Thu nhập bình quân đầu người 01 tháng của các tỉnh , thành phố trực thuộc trung ương có biển** → `KHOAN` (span: `[19:36]`)
- `[e6]` **Thu nhập** → `TAI_SAN_VAT_CHAT` (span: `[21:22]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 02 tháng 01 năm 2025 `[NGAY_BAN_HANH]`)
- (`e4` Điều 5 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`)
- (`e5` 0301 . Thu nhập bình quân đầu người 01 tháng của các tỉnh , thành phố trực thuộc trung ương có biển `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 5 `[DIEU]`)


---

### Mẫu #01_2025_TT-BKHĐT_174764#body_context_66 (Loại: `body_context`)
> **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[01/2025/TT-BKHĐT]`<SO_HIEU>`** . **[Điều 5]`<DIEU>`** . **[Khoản 1 . Khái niệm , phương pháp tính]`<KHOAN>`** : **[b ) Người học việc , tập sự ( kể cả bác sỹ thực tập ) làm việc trong các ngành kinh tế biển và có nhận được **[tiền lương]`<TAI_SAN_VAT_CHAT>`** , tiền công ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[5:6]`)
- `[e1]` **01/2025/TT-BKHĐT** → `SO_HIEU` (span: `[7:8]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[0:4]`)
- `[e3]` **Điều 5** → `DIEU` (span: `[9:11]`)
- `[e4]` **Khoản 1 . Khái niệm , phương pháp tính** → `KHOAN` (span: `[12:19]`)
- `[e5]` **b ) Người học việc , tập sự ( kể cả bác sỹ thực tập ) làm việc trong các ngành kinh tế biển và có nhận được tiền lương , tiền công ;** → `DIEM` (span: `[20:46]`)
- `[e6]` **tiền lương** → `TAI_SAN_VAT_CHAT` (span: `[41:42]`) *(lồng trong `e5` (`DIEM`))*

**Quan hệ:**
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 5 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`)
- (`e4` Khoản 1 . Khái niệm , phương pháp tính `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 5 `[DIEU]`)
- (`e5` b ) Người học việc , tập sự ( kể cả bác sỹ thực tập ) làm việc trong các ngành kinh tế biển và có nhận được tiền lương , tiền công ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e4` Khoản 1 . Khái niệm , phương pháp tính `[KHOAN]`)


---

### Mẫu #01_2025_TT-BKHĐT_174764#body_context_67 (Loại: `body_context`)
> **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[01/2025/TT-BKHĐT]`<SO_HIEU>`** . **[Điều 5]`<DIEU>`** . **[Khoản 1 . Khái niệm , phương pháp tính]`<KHOAN>`** : **[c ) Sinh viên / học sinh / người nghỉ hưu trong thời kỳ tham chiếu có làm một công việc trong các ngành kinh tế biển ( không bao gồm công việc tự sản tự tiêu ) từ 01 giờ trở lên để tạo **[thu nhập]`<TAI_SAN_VAT_CHAT>`** ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[5:6]`)
- `[e1]` **01/2025/TT-BKHĐT** → `SO_HIEU` (span: `[7:8]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[0:4]`)
- `[e3]` **Điều 5** → `DIEU` (span: `[9:11]`)
- `[e4]` **Khoản 1 . Khái niệm , phương pháp tính** → `KHOAN` (span: `[12:19]`)
- `[e5]` **c ) Sinh viên / học sinh / người nghỉ hưu trong thời kỳ tham chiếu có làm một công việc trong các ngành kinh tế biển ( không bao gồm công việc tự sản tự tiêu ) từ 01 giờ trở lên để tạo thu nhập ;** → `DIEM` (span: `[20:59]`)
- `[e6]` **thu nhập** → `TAI_SAN_VAT_CHAT` (span: `[57:58]`) *(lồng trong `e5` (`DIEM`))*

**Quan hệ:**
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 5 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`)
- (`e4` Khoản 1 . Khái niệm , phương pháp tính `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 5 `[DIEU]`)
- (`e5` c ) Sinh viên / học sinh / người nghỉ hưu trong thời kỳ tham chiếu có làm một công việc trong các ngành kinh tế biển ( không bao gồm công việc tự sản tự tiêu ) từ 01 giờ trở lên để tạo thu nhập ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e4` Khoản 1 . Khái niệm , phương pháp tính `[KHOAN]`)


---

### Mẫu #01_2025_TT-BKHĐT_174764#body_context_68 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[01/2025/TT-BKHĐT]`<SO_HIEU>`** ban hành **[ngày 02 tháng 01 năm 2025]`<NGAY_BAN_HANH>`** bởi **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** . **[Điều 5]`<DIEU>`** . **[Khoản 1 . Khái niệm , phương pháp tính]`<KHOAN>`** : **[d ) Người đang tìm kiếm việc làm / người đăng ký hoặc người nhận bảo hiểm thất nghiệp nhưng trong thời kỳ tham chiếu có làm một công việc trong các ngành kinh tế biển ( không bao gồm công việc tự sản tự tiêu ) từ 01 giờ trở lên để tạo **[thu nhập]`<TAI_SAN_VAT_CHAT>`** ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **01/2025/TT-BKHĐT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[11:15]`)
- `[e3]` **ngày 02 tháng 01 năm 2025** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 5** → `DIEU` (span: `[16:18]`)
- `[e5]` **Khoản 1 . Khái niệm , phương pháp tính** → `KHOAN` (span: `[19:26]`)
- `[e6]` **d ) Người đang tìm kiếm việc làm / người đăng ký hoặc người nhận bảo hiểm thất nghiệp nhưng trong thời kỳ tham chiếu có làm một công việc trong các ngành kinh tế biển ( không bao gồm công việc tự sản tự tiêu ) từ 01 giờ trở lên để tạo thu nhập ;** → `DIEM` (span: `[27:71]`)
- `[e7]` **thu nhập** → `TAI_SAN_VAT_CHAT` (span: `[69:70]`) *(lồng trong `e6` (`DIEM`))*

**Quan hệ:**
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 02 tháng 01 năm 2025 `[NGAY_BAN_HANH]`)
- (`e4` Điều 5 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`)
- (`e5` Khoản 1 . Khái niệm , phương pháp tính `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 5 `[DIEU]`)
- (`e6` d ) Người đang tìm kiếm việc làm / người đăng ký hoặc người nhận bảo hiểm thất nghiệp nhưng trong thời kỳ tham chiếu có làm một công việc trong các ngành kinh tế biển ( không bao gồm công việc tự sản tự tiêu ) từ 01 giờ trở lên để tạo thu nhập ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e5` Khoản 1 . Khái niệm , phương pháp tính `[KHOAN]`)


---

### Mẫu #01_2025_TT-BKHĐT_174764#body_standalone_69 (Loại: `body_standalone`)
> **[Điều 5]`<DIEU>`** . **[Khoản 1 . Khái niệm , phương pháp tính]`<KHOAN>`** : **[d ) Người đang tìm kiếm việc làm / người đăng ký hoặc người nhận bảo hiểm thất nghiệp nhưng trong thời kỳ tham chiếu có làm một công việc trong các ngành kinh tế biển ( không bao gồm công việc tự sản tự tiêu ) từ 01 giờ trở lên để tạo **[thu nhập]`<TAI_SAN_VAT_CHAT>`** ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Điều 5** → `DIEU` (span: `[0:2]`)
- `[e1]` **Khoản 1 . Khái niệm , phương pháp tính** → `KHOAN` (span: `[3:10]`)
- `[e2]` **d ) Người đang tìm kiếm việc làm / người đăng ký hoặc người nhận bảo hiểm thất nghiệp nhưng trong thời kỳ tham chiếu có làm một công việc trong các ngành kinh tế biển ( không bao gồm công việc tự sản tự tiêu ) từ 01 giờ trở lên để tạo thu nhập ;** → `DIEM` (span: `[11:55]`)
- `[e3]` **thu nhập** → `TAI_SAN_VAT_CHAT` (span: `[53:54]`) *(lồng trong `e2` (`DIEM`))*

**Quan hệ:**
- (`e1` Khoản 1 . Khái niệm , phương pháp tính `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 5 `[DIEU]`)
- (`e2` d ) Người đang tìm kiếm việc làm / người đăng ký hoặc người nhận bảo hiểm thất nghiệp nhưng trong thời kỳ tham chiếu có làm một công việc trong các ngành kinh tế biển ( không bao gồm công việc tự sản tự tiêu ) từ 01 giờ trở lên để tạo thu nhập ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e1` Khoản 1 . Khái niệm , phương pháp tính `[KHOAN]`)


---

### Mẫu #01_2025_TT-BKHĐT_174764#body_context_70 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[01/2025/TT-BKHĐT]`<SO_HIEU>`** ban hành **[ngày 02 tháng 01 năm 2025]`<NGAY_BAN_HANH>`** bởi **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** . **[Điều 5]`<DIEU>`** . **[Khoản 1 . Khái niệm , phương pháp tính]`<KHOAN>`** : **[đ ) Lao động gia đình trong các ngành kinh tế biển : Những người làm việc vì mục đích để nhận tiền công , **[tiền lương]`<TAI_SAN_VAT_CHAT>`** hoặc lợi nhuận nhưng các khoản **[tiền lương]`<TAI_SAN_VAT_CHAT>`** , tiền công và lợi nhuận đó có thể **[không trả trực tiếp]`<HANH_VI_VI_PHAM>`** mà được tích lũy vào **[thu nhập]`<TAI_SAN_VAT_CHAT>`** chung của gia đình .]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **01/2025/TT-BKHĐT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[11:15]`)
- `[e3]` **ngày 02 tháng 01 năm 2025** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 5** → `DIEU` (span: `[16:18]`)
- `[e5]` **Khoản 1 . Khái niệm , phương pháp tính** → `KHOAN` (span: `[19:26]`)
- `[e6]` **đ ) Lao động gia đình trong các ngành kinh tế biển : Những người làm việc vì mục đích để nhận tiền công , tiền lương hoặc lợi nhuận nhưng các khoản tiền lương , tiền công và lợi nhuận đó có thể không trả trực tiếp mà được tích lũy vào thu nhập chung của gia đình .** → `DIEM` (span: `[27:73]`)
- `[e7]` **không trả trực tiếp** → `HANH_VI_VI_PHAM` (span: `[61:64]`) *(lồng trong `e6` (`DIEM`))*
- `[e8]` **tiền lương** → `TAI_SAN_VAT_CHAT` (span: `[47:48]`) *(lồng trong `e6` (`DIEM`))*
- `[e9]` **tiền lương** → `TAI_SAN_VAT_CHAT` (span: `[53:54]`) *(lồng trong `e6` (`DIEM`))*
- `[e10]` **thu nhập** → `TAI_SAN_VAT_CHAT` (span: `[68:69]`) *(lồng trong `e6` (`DIEM`))*

**Quan hệ:**
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 02 tháng 01 năm 2025 `[NGAY_BAN_HANH]`)
- (`e4` Điều 5 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`)
- (`e5` Khoản 1 . Khái niệm , phương pháp tính `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 5 `[DIEU]`)
- (`e6` đ ) Lao động gia đình trong các ngành kinh tế biển : Những người làm việc vì mục đích để nhận tiền công , tiền lương hoặc lợi nhuận nhưng các khoản tiền lương , tiền công và lợi nhuận đó có thể không trả trực tiếp mà được tích lũy vào thu nhập chung của gia đình . `[DIEM]`) ==[ **THUOC_VE** ]==> (`e5` Khoản 1 . Khái niệm , phương pháp tính `[KHOAN]`)
- (`e7` không trả trực tiếp `[HANH_VI_VI_PHAM]`) ==[ **TAC_DONG_DOI_TUONG** ]==> (`e8` tiền lương `[TAI_SAN_VAT_CHAT]`)
- (`e7` không trả trực tiếp `[HANH_VI_VI_PHAM]`) ==[ **TAC_DONG_DOI_TUONG** ]==> (`e9` tiền lương `[TAI_SAN_VAT_CHAT]`)
- (`e7` không trả trực tiếp `[HANH_VI_VI_PHAM]`) ==[ **TAC_DONG_DOI_TUONG** ]==> (`e10` thu nhập `[TAI_SAN_VAT_CHAT]`)


---

### Mẫu #01_2025_TT-BKHĐT_174764#body_standalone_71 (Loại: `body_standalone`)
> **[Điều 5]`<DIEU>`** . **[Khoản 1 . Khái niệm , phương pháp tính]`<KHOAN>`** : **[đ ) Lao động gia đình trong các ngành kinh tế biển : Những người làm việc vì mục đích để nhận tiền công , **[tiền lương]`<TAI_SAN_VAT_CHAT>`** hoặc lợi nhuận nhưng các khoản **[tiền lương]`<TAI_SAN_VAT_CHAT>`** , tiền công và lợi nhuận đó có thể **[không trả trực tiếp]`<HANH_VI_VI_PHAM>`** mà được tích lũy vào **[thu nhập]`<TAI_SAN_VAT_CHAT>`** chung của gia đình .]`<DIEM>`**

**Thực thể:**
- `[e0]` **Điều 5** → `DIEU` (span: `[0:2]`)
- `[e1]` **Khoản 1 . Khái niệm , phương pháp tính** → `KHOAN` (span: `[3:10]`)
- `[e2]` **đ ) Lao động gia đình trong các ngành kinh tế biển : Những người làm việc vì mục đích để nhận tiền công , tiền lương hoặc lợi nhuận nhưng các khoản tiền lương , tiền công và lợi nhuận đó có thể không trả trực tiếp mà được tích lũy vào thu nhập chung của gia đình .** → `DIEM` (span: `[11:57]`)
- `[e3]` **không trả trực tiếp** → `HANH_VI_VI_PHAM` (span: `[45:48]`) *(lồng trong `e2` (`DIEM`))*
- `[e4]` **tiền lương** → `TAI_SAN_VAT_CHAT` (span: `[31:32]`) *(lồng trong `e2` (`DIEM`))*
- `[e5]` **tiền lương** → `TAI_SAN_VAT_CHAT` (span: `[37:38]`) *(lồng trong `e2` (`DIEM`))*
- `[e6]` **thu nhập** → `TAI_SAN_VAT_CHAT` (span: `[52:53]`) *(lồng trong `e2` (`DIEM`))*

**Quan hệ:**
- (`e1` Khoản 1 . Khái niệm , phương pháp tính `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 5 `[DIEU]`)
- (`e2` đ ) Lao động gia đình trong các ngành kinh tế biển : Những người làm việc vì mục đích để nhận tiền công , tiền lương hoặc lợi nhuận nhưng các khoản tiền lương , tiền công và lợi nhuận đó có thể không trả trực tiếp mà được tích lũy vào thu nhập chung của gia đình . `[DIEM]`) ==[ **THUOC_VE** ]==> (`e1` Khoản 1 . Khái niệm , phương pháp tính `[KHOAN]`)
- (`e3` không trả trực tiếp `[HANH_VI_VI_PHAM]`) ==[ **TAC_DONG_DOI_TUONG** ]==> (`e4` tiền lương `[TAI_SAN_VAT_CHAT]`)
- (`e3` không trả trực tiếp `[HANH_VI_VI_PHAM]`) ==[ **TAC_DONG_DOI_TUONG** ]==> (`e5` tiền lương `[TAI_SAN_VAT_CHAT]`)
- (`e3` không trả trực tiếp `[HANH_VI_VI_PHAM]`) ==[ **TAC_DONG_DOI_TUONG** ]==> (`e6` thu nhập `[TAI_SAN_VAT_CHAT]`)


---

### Mẫu #01_2025_TT-BKHĐT_174764#body_context_72 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[01/2025/TT-BKHĐT]`<SO_HIEU>`** ban hành **[ngày 02 tháng 01 năm 2025]`<NGAY_BAN_HANH>`** bởi **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** . **[Điều 5]`<DIEU>`** . **[4 . Nguồn số liệu : Điều tra lao động và việc làm .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **01/2025/TT-BKHĐT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[11:15]`)
- `[e3]` **ngày 02 tháng 01 năm 2025** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 5** → `DIEU` (span: `[16:18]`)
- `[e5]` **4 . Nguồn số liệu : Điều tra lao động và việc làm .** → `KHOAN` (span: `[19:29]`)

**Quan hệ:**
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 02 tháng 01 năm 2025 `[NGAY_BAN_HANH]`)
- (`e4` Điều 5 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`)
- (`e5` 4 . Nguồn số liệu : Điều tra lao động và việc làm . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 5 `[DIEU]`)


---

### Mẫu #01_2025_TT-BKHĐT_174764#body_context_73 (Loại: `body_context`)
> **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[01/2025/TT-BKHĐT]`<SO_HIEU>`** . **[Điều 5]`<DIEU>`** . **[0303 . **[Thu nhập]`<TAI_SAN_VAT_CHAT>`** bình quân một lao động đang làm việc trong các ngành kinh tế biển]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[5:6]`)
- `[e1]` **01/2025/TT-BKHĐT** → `SO_HIEU` (span: `[7:8]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[0:4]`)
- `[e3]` **Điều 5** → `DIEU` (span: `[9:11]`)
- `[e4]` **0303 . Thu nhập bình quân một lao động đang làm việc trong các ngành kinh tế biển** → `KHOAN` (span: `[12:25]`)
- `[e5]` **Thu nhập** → `TAI_SAN_VAT_CHAT` (span: `[14:15]`) *(lồng trong `e4` (`KHOAN`))*

**Quan hệ:**
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 5 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`)
- (`e4` 0303 . Thu nhập bình quân một lao động đang làm việc trong các ngành kinh tế biển `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 5 `[DIEU]`)


---

### Mẫu #01_2025_TT-BKHĐT_174764#body_context_74 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[01/2025/TT-BKHĐT]`<SO_HIEU>`** ban hành **[ngày 02 tháng 01 năm 2025]`<NGAY_BAN_HANH>`** bởi **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** . **[Điều 5]`<DIEU>`** . **[3 . Nguồn số liệu : Chế độ báo cáo thống kê **[ngành y tế]`<LINH_VUC>`** .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **01/2025/TT-BKHĐT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[11:15]`)
- `[e3]` **ngày 02 tháng 01 năm 2025** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 5** → `DIEU` (span: `[16:18]`)
- `[e5]` **3 . Nguồn số liệu : Chế độ báo cáo thống kê ngành y tế .** → `KHOAN` (span: `[19:30]`)
- `[e6]` **ngành y tế** → `LINH_VUC` (span: `[27:29]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 02 tháng 01 năm 2025 `[NGAY_BAN_HANH]`)
- (`e4` Điều 5 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`)
- (`e5` 3 . Nguồn số liệu : Chế độ báo cáo thống kê ngành y tế . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 5 `[DIEU]`)
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e6` ngành y tế `[LINH_VUC]`)
- (`e5` 3 . Nguồn số liệu : Chế độ báo cáo thống kê ngành y tế . `[KHOAN]`) ==[ **THUOC_LINH_VUC** ]==> (`e6` ngành y tế `[LINH_VUC]`) *(Quan hệ lồng nhau)*


---

### Mẫu #01_2025_TT-BKHĐT_174764#body_context_75 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[01/2025/TT-BKHĐT]`<SO_HIEU>`** của **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Lao động - Thương binh và Xã hội]`<LINH_VUC>`** . **[Điều 5]`<DIEU>`** . **[2 . Phân tổ chủ yếu : Công dụng , hình thức sở hữu .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **01/2025/TT-BKHĐT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[4:8]`)
- `[e3]` **Lao động - Thương binh và Xã hội** → `LINH_VUC` (span: `[10:15]`)
- `[e4]` **Điều 5** → `DIEU` (span: `[16:18]`)
- `[e5]` **2 . Phân tổ chủ yếu : Công dụng , hình thức sở hữu .** → `KHOAN` (span: `[19:30]`)

**Quan hệ:**
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Lao động - Thương binh và Xã hội `[LINH_VUC]`)
- (`e4` Điều 5 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`)
- (`e5` 2 . Phân tổ chủ yếu : Công dụng , hình thức sở hữu . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 5 `[DIEU]`)
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Lao động - Thương binh và Xã hội `[LINH_VUC]`)
- (`e5` 2 . Phân tổ chủ yếu : Công dụng , hình thức sở hữu . `[KHOAN]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Lao động - Thương binh và Xã hội `[LINH_VUC]`)


---

### Mẫu #01_2025_TT-BKHĐT_174764#body_context_76 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[01/2025/TT-BKHĐT]`<SO_HIEU>`** ban hành **[ngày 02 tháng 01 năm 2025]`<NGAY_BAN_HANH>`** bởi **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** . **[Điều 5]`<DIEU>`** . **[0307 . Số lượng thuyền viên có **[văn bằng , chứng chỉ]`<GIAY_TO_HO_SO>`** chuyên môn đang làm việc trên tàu vận tải biển]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **01/2025/TT-BKHĐT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[11:15]`)
- `[e3]` **ngày 02 tháng 01 năm 2025** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 5** → `DIEU` (span: `[16:18]`)
- `[e5]` **0307 . Số lượng thuyền viên có văn bằng , chứng chỉ chuyên môn đang làm việc trên tàu vận tải biển** → `KHOAN` (span: `[19:34]`)
- `[e6]` **văn bằng , chứng chỉ** → `GIAY_TO_HO_SO` (span: `[24:27]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 02 tháng 01 năm 2025 `[NGAY_BAN_HANH]`)
- (`e4` Điều 5 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`)
- (`e5` 0307 . Số lượng thuyền viên có văn bằng , chứng chỉ chuyên môn đang làm việc trên tàu vận tải biển `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 5 `[DIEU]`)


---

### Mẫu #01_2025_TT-BKHĐT_174764#body_context_77 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[01/2025/TT-BKHĐT]`<SO_HIEU>`** của **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Lao động - Thương binh và Xã hội]`<LINH_VUC>`** . **[Điều 5]`<DIEU>`** . **[0308 . Số học viên , sinh viên tốt nghiệp các ngành học liên quan đến kinh tế biển trong các **[cơ sở giáo dục nghề nghiệp]`<TO_CHUC_DOANH_NGHIEP>`**]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **01/2025/TT-BKHĐT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[4:8]`)
- `[e3]` **Lao động - Thương binh và Xã hội** → `LINH_VUC` (span: `[10:15]`)
- `[e4]` **Điều 5** → `DIEU` (span: `[16:18]`)
- `[e5]` **0308 . Số học viên , sinh viên tốt nghiệp các ngành học liên quan đến kinh tế biển trong các cơ sở giáo dục nghề nghiệp** → `KHOAN` (span: `[19:37]`)
- `[e6]` **cơ sở giáo dục nghề nghiệp** → `TO_CHUC_DOANH_NGHIEP` (span: `[34:37]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Lao động - Thương binh và Xã hội `[LINH_VUC]`)
- (`e4` Điều 5 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`)
- (`e5` 0308 . Số học viên , sinh viên tốt nghiệp các ngành học liên quan đến kinh tế biển trong các cơ sở giáo dục nghề nghiệp `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 5 `[DIEU]`)
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Lao động - Thương binh và Xã hội `[LINH_VUC]`)
- (`e5` 0308 . Số học viên , sinh viên tốt nghiệp các ngành học liên quan đến kinh tế biển trong các cơ sở giáo dục nghề nghiệp `[KHOAN]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Lao động - Thương binh và Xã hội `[LINH_VUC]`)


---

### Mẫu #01_2025_TT-BKHĐT_174764#body_context_78 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[01/2025/TT-BKHĐT]`<SO_HIEU>`** của **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Lao động - Thương binh và Xã hội]`<LINH_VUC>`** . **[Điều 5]`<DIEU>`** . **[0401 . Số lượng **[giấy phép nhận chìm ở biển]`<GIAY_TO_HO_SO>`** được cấp]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **01/2025/TT-BKHĐT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[4:8]`)
- `[e3]` **Lao động - Thương binh và Xã hội** → `LINH_VUC` (span: `[10:15]`)
- `[e4]` **Điều 5** → `DIEU` (span: `[16:18]`)
- `[e5]` **0401 . Số lượng giấy phép nhận chìm ở biển được cấp** → `KHOAN` (span: `[19:29]`)
- `[e6]` **giấy phép nhận chìm ở biển** → `GIAY_TO_HO_SO` (span: `[22:27]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Lao động - Thương binh và Xã hội `[LINH_VUC]`)
- (`e4` Điều 5 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`)
- (`e5` 0401 . Số lượng giấy phép nhận chìm ở biển được cấp `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 5 `[DIEU]`)
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Lao động - Thương binh và Xã hội `[LINH_VUC]`)
- (`e5` 0401 . Số lượng giấy phép nhận chìm ở biển được cấp `[KHOAN]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Lao động - Thương binh và Xã hội `[LINH_VUC]`)


---

### Mẫu #01_2025_TT-BKHĐT_174764#body_standalone_79 (Loại: `body_standalone`)
> **[Điều 5]`<DIEU>`** . **[0401 . Số lượng **[giấy phép nhận chìm ở biển]`<GIAY_TO_HO_SO>`** được cấp]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 5** → `DIEU` (span: `[0:2]`)
- `[e1]` **0401 . Số lượng giấy phép nhận chìm ở biển được cấp** → `KHOAN` (span: `[3:13]`)
- `[e2]` **giấy phép nhận chìm ở biển** → `GIAY_TO_HO_SO` (span: `[6:11]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 0401 . Số lượng giấy phép nhận chìm ở biển được cấp `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 5 `[DIEU]`)


---

### Mẫu #01_2025_TT-BKHĐT_174764#body_context_80 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[01/2025/TT-BKHĐT]`<SO_HIEU>`** của **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Lao động - Thương binh và Xã hội]`<LINH_VUC>`** . **[Điều 5]`<DIEU>`** . **[Khoản 1 . Khái niệm , phương pháp tính]`<KHOAN>`** : **[a ) Sự cố tràn dầu là hiện tượng dầu từ các **[phương tiện]`<TAI_SAN_VAT_CHAT>`** chứa , vận chuyển khác nhau , từ các công trình và các mỏ dầu thoát ra ngoài môi trường tự nhiên do sự cố kỹ thuật , thiên tai hoặc do con người gây ra ( **[khoản 2 Điều 3 Quyết định số 12/2021/QĐ-TTg]`<THAM_CHIEU_PHAP_LY>`** **[ngày 24/3/2021]`<NGAY_THAM_CHIEU>`** của **[Thủ tướng Chính phủ]`<CO_QUAN_THAM_QUYEN>`** ) .]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **01/2025/TT-BKHĐT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[4:8]`)
- `[e3]` **Lao động - Thương binh và Xã hội** → `LINH_VUC` (span: `[10:15]`)
- `[e4]` **Điều 5** → `DIEU` (span: `[16:18]`)
- `[e5]` **Khoản 1 . Khái niệm , phương pháp tính** → `KHOAN` (span: `[19:26]`)
- `[e6]` **a ) Sự cố tràn dầu là hiện tượng dầu từ các phương tiện chứa , vận chuyển khác nhau , từ các công trình và các mỏ dầu thoát ra ngoài môi trường tự nhiên do sự cố kỹ thuật , thiên tai hoặc do con người gây ra ( khoản 2 Điều 3 Quyết định số 12/2021/QĐ-TTg ngày 24/3/2021 của Thủ tướng Chính phủ ) .** → `DIEM` (span: `[27:81]`)
- `[e7]` **khoản 2 Điều 3 Quyết định số 12/2021/QĐ-TTg** → `THAM_CHIEU_PHAP_LY` (span: `[67:74]`) *(lồng trong `e6` (`DIEM`))*
- `[e8]` **ngày 24/3/2021** → `NGAY_THAM_CHIEU` (span: `[74:76]`) *(lồng trong `e6` (`DIEM`))*
- `[e9]` **Thủ tướng Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[77:79]`) *(lồng trong `e6` (`DIEM`))*
- `[e10]` **phương tiện** → `TAI_SAN_VAT_CHAT` (span: `[37:38]`) *(lồng trong `e6` (`DIEM`))*

**Quan hệ:**
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Lao động - Thương binh và Xã hội `[LINH_VUC]`)
- (`e4` Điều 5 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`)
- (`e5` Khoản 1 . Khái niệm , phương pháp tính `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 5 `[DIEU]`)
- (`e6` a ) Sự cố tràn dầu là hiện tượng dầu từ các phương tiện chứa , vận chuyển khác nhau , từ các công trình và các mỏ dầu thoát ra ngoài môi trường tự nhiên do sự cố kỹ thuật , thiên tai hoặc do con người gây ra ( khoản 2 Điều 3 Quyết định số 12/2021/QĐ-TTg ngày 24/3/2021 của Thủ tướng Chính phủ ) . `[DIEM]`) ==[ **THUOC_VE** ]==> (`e5` Khoản 1 . Khái niệm , phương pháp tính `[KHOAN]`)
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Lao động - Thương binh và Xã hội `[LINH_VUC]`)
- (`e6` a ) Sự cố tràn dầu là hiện tượng dầu từ các phương tiện chứa , vận chuyển khác nhau , từ các công trình và các mỏ dầu thoát ra ngoài môi trường tự nhiên do sự cố kỹ thuật , thiên tai hoặc do con người gây ra ( khoản 2 Điều 3 Quyết định số 12/2021/QĐ-TTg ngày 24/3/2021 của Thủ tướng Chính phủ ) . `[DIEM]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Lao động - Thương binh và Xã hội `[LINH_VUC]`)
- (`e6` a ) Sự cố tràn dầu là hiện tượng dầu từ các phương tiện chứa , vận chuyển khác nhau , từ các công trình và các mỏ dầu thoát ra ngoài môi trường tự nhiên do sự cố kỹ thuật , thiên tai hoặc do con người gây ra ( khoản 2 Điều 3 Quyết định số 12/2021/QĐ-TTg ngày 24/3/2021 của Thủ tướng Chính phủ ) . `[DIEM]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e7` khoản 2 Điều 3 Quyết định số 12/2021/QĐ-TTg `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e7` khoản 2 Điều 3 Quyết định số 12/2021/QĐ-TTg `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e8` ngày 24/3/2021 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #01_2025_TT-BKHĐT_174764#body_standalone_81 (Loại: `body_standalone`)
> **[Điều 5]`<DIEU>`** . **[Khoản 1 . Khái niệm , phương pháp tính]`<KHOAN>`** : **[a ) Sự cố tràn dầu là hiện tượng dầu từ các **[phương tiện]`<TAI_SAN_VAT_CHAT>`** chứa , vận chuyển khác nhau , từ các công trình và các mỏ dầu thoát ra ngoài môi trường tự nhiên do sự cố kỹ thuật , thiên tai hoặc do con người gây ra ( **[khoản 2 Điều 3 Quyết định số 12/2021/QĐ-TTg]`<THAM_CHIEU_PHAP_LY>`** **[ngày 24/3/2021]`<NGAY_THAM_CHIEU>`** của **[Thủ tướng Chính phủ]`<CO_QUAN_THAM_QUYEN>`** ) .]`<DIEM>`**

**Thực thể:**
- `[e0]` **Điều 5** → `DIEU` (span: `[0:2]`)
- `[e1]` **Khoản 1 . Khái niệm , phương pháp tính** → `KHOAN` (span: `[3:10]`)
- `[e2]` **a ) Sự cố tràn dầu là hiện tượng dầu từ các phương tiện chứa , vận chuyển khác nhau , từ các công trình và các mỏ dầu thoát ra ngoài môi trường tự nhiên do sự cố kỹ thuật , thiên tai hoặc do con người gây ra ( khoản 2 Điều 3 Quyết định số 12/2021/QĐ-TTg ngày 24/3/2021 của Thủ tướng Chính phủ ) .** → `DIEM` (span: `[11:65]`)
- `[e3]` **khoản 2 Điều 3 Quyết định số 12/2021/QĐ-TTg** → `THAM_CHIEU_PHAP_LY` (span: `[51:58]`) *(lồng trong `e2` (`DIEM`))*
- `[e4]` **ngày 24/3/2021** → `NGAY_THAM_CHIEU` (span: `[58:60]`) *(lồng trong `e2` (`DIEM`))*
- `[e5]` **Thủ tướng Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[61:63]`) *(lồng trong `e2` (`DIEM`))*
- `[e6]` **phương tiện** → `TAI_SAN_VAT_CHAT` (span: `[21:22]`) *(lồng trong `e2` (`DIEM`))*

**Quan hệ:**
- (`e1` Khoản 1 . Khái niệm , phương pháp tính `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 5 `[DIEU]`)
- (`e2` a ) Sự cố tràn dầu là hiện tượng dầu từ các phương tiện chứa , vận chuyển khác nhau , từ các công trình và các mỏ dầu thoát ra ngoài môi trường tự nhiên do sự cố kỹ thuật , thiên tai hoặc do con người gây ra ( khoản 2 Điều 3 Quyết định số 12/2021/QĐ-TTg ngày 24/3/2021 của Thủ tướng Chính phủ ) . `[DIEM]`) ==[ **THUOC_VE** ]==> (`e1` Khoản 1 . Khái niệm , phương pháp tính `[KHOAN]`)
- (`e2` a ) Sự cố tràn dầu là hiện tượng dầu từ các phương tiện chứa , vận chuyển khác nhau , từ các công trình và các mỏ dầu thoát ra ngoài môi trường tự nhiên do sự cố kỹ thuật , thiên tai hoặc do con người gây ra ( khoản 2 Điều 3 Quyết định số 12/2021/QĐ-TTg ngày 24/3/2021 của Thủ tướng Chính phủ ) . `[DIEM]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` khoản 2 Điều 3 Quyết định số 12/2021/QĐ-TTg `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e3` khoản 2 Điều 3 Quyết định số 12/2021/QĐ-TTg `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e4` ngày 24/3/2021 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #01_2025_TT-BKHĐT_174764#body_context_82 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[01/2025/TT-BKHĐT]`<SO_HIEU>`** của **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Lao động - Thương binh và Xã hội]`<LINH_VUC>`** . **[Điều 5]`<DIEU>`** . **[0404 . Số lượng loài thủy sản trong Danh mục loài thủy sản nguy cấp , quý , hiếm được sinh sản nhân tạo , ương nuôi thành công]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **01/2025/TT-BKHĐT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[4:8]`)
- `[e3]` **Lao động - Thương binh và Xã hội** → `LINH_VUC` (span: `[10:15]`)
- `[e4]` **Điều 5** → `DIEU` (span: `[16:18]`)
- `[e5]` **0404 . Số lượng loài thủy sản trong Danh mục loài thủy sản nguy cấp , quý , hiếm được sinh sản nhân tạo , ương nuôi thành công** → `KHOAN` (span: `[19:40]`)

**Quan hệ:**
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Lao động - Thương binh và Xã hội `[LINH_VUC]`)
- (`e4` Điều 5 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`)
- (`e5` 0404 . Số lượng loài thủy sản trong Danh mục loài thủy sản nguy cấp , quý , hiếm được sinh sản nhân tạo , ương nuôi thành công `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 5 `[DIEU]`)
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Lao động - Thương binh và Xã hội `[LINH_VUC]`)
- (`e5` 0404 . Số lượng loài thủy sản trong Danh mục loài thủy sản nguy cấp , quý , hiếm được sinh sản nhân tạo , ương nuôi thành công `[KHOAN]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Lao động - Thương binh và Xã hội `[LINH_VUC]`)


---

### Mẫu #01_2025_TT-BKHĐT_174764#body_context_83 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[01/2025/TT-BKHĐT]`<SO_HIEU>`** của **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Lao động - Thương binh và Xã hội]`<LINH_VUC>`** . **[Điều 5]`<DIEU>`** . **[0407 . Số khu , diện tích và tỷ lệ diện tích các khu bảo vệ nguồn lợi thủy sản ở vùng biển]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **01/2025/TT-BKHĐT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[4:8]`)
- `[e3]` **Lao động - Thương binh và Xã hội** → `LINH_VUC` (span: `[10:15]`)
- `[e4]` **Điều 5** → `DIEU` (span: `[16:18]`)
- `[e5]` **0407 . Số khu , diện tích và tỷ lệ diện tích các khu bảo vệ nguồn lợi thủy sản ở vùng biển** → `KHOAN` (span: `[19:36]`)

**Quan hệ:**
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Lao động - Thương binh và Xã hội `[LINH_VUC]`)
- (`e4` Điều 5 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`)
- (`e5` 0407 . Số khu , diện tích và tỷ lệ diện tích các khu bảo vệ nguồn lợi thủy sản ở vùng biển `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 5 `[DIEU]`)
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Lao động - Thương binh và Xã hội `[LINH_VUC]`)
- (`e5` 0407 . Số khu , diện tích và tỷ lệ diện tích các khu bảo vệ nguồn lợi thủy sản ở vùng biển `[KHOAN]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Lao động - Thương binh và Xã hội `[LINH_VUC]`)


---

### Mẫu #01_2025_TT-BKHĐT_174764#body_context_84 (Loại: `body_context`)
> **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[01/2025/TT-BKHĐT]`<SO_HIEU>`** . **[Điều 5]`<DIEU>`** . **[4 . Đơn vị chịu trách nhiệm thu thập , tổng hợp : **[Bộ Nông nghiệp và Phát triển nông thôn]`<CO_QUAN_THAM_QUYEN>`** .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[5:6]`)
- `[e1]` **01/2025/TT-BKHĐT** → `SO_HIEU` (span: `[7:8]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[0:4]`)
- `[e3]` **Điều 5** → `DIEU` (span: `[9:11]`)
- `[e4]` **4 . Đơn vị chịu trách nhiệm thu thập , tổng hợp : Bộ Nông nghiệp và Phát triển nông thôn .** → `KHOAN` (span: `[12:27]`)
- `[e5]` **Bộ Nông nghiệp và Phát triển nông thôn** → `CO_QUAN_THAM_QUYEN` (span: `[21:26]`) *(lồng trong `e4` (`KHOAN`))*

**Quan hệ:**
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 5 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`)
- (`e4` 4 . Đơn vị chịu trách nhiệm thu thập , tổng hợp : Bộ Nông nghiệp và Phát triển nông thôn . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 5 `[DIEU]`)


---

### Mẫu #01_2025_TT-BKHĐT_174764#body_context_85 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[01/2025/TT-BKHĐT]`<SO_HIEU>`** ban hành **[ngày 02 tháng 01 năm 2025]`<NGAY_BAN_HANH>`** bởi **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** . **[Điều 5]`<DIEU>`** . **[0411 . Diện tích các khu vực biển được giao , cho thuê đang khai thác , sử dụng]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **01/2025/TT-BKHĐT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[11:15]`)
- `[e3]` **ngày 02 tháng 01 năm 2025** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 5** → `DIEU` (span: `[16:18]`)
- `[e5]` **0411 . Diện tích các khu vực biển được giao , cho thuê đang khai thác , sử dụng** → `KHOAN` (span: `[19:34]`)

**Quan hệ:**
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 02 tháng 01 năm 2025 `[NGAY_BAN_HANH]`)
- (`e4` Điều 5 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`)
- (`e5` 0411 . Diện tích các khu vực biển được giao , cho thuê đang khai thác , sử dụng `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 5 `[DIEU]`)


---

### Mẫu #01_2025_TT-BKHĐT_174764#body_context_86 (Loại: `body_context`)
> **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[01/2025/TT-BKHĐT]`<SO_HIEU>`** . **[Điều 5]`<DIEU>`** . **[2 . Phân tổ chủ yếu : Hệ sinh thái biển .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[5:6]`)
- `[e1]` **01/2025/TT-BKHĐT** → `SO_HIEU` (span: `[7:8]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[0:4]`)
- `[e3]` **Điều 5** → `DIEU` (span: `[9:11]`)
- `[e4]` **2 . Phân tổ chủ yếu : Hệ sinh thái biển .** → `KHOAN` (span: `[12:22]`)

**Quan hệ:**
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 5 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 01/2025/TT-BKHĐT `[SO_HIEU]`)
- (`e4` 2 . Phân tổ chủ yếu : Hệ sinh thái biển . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 5 `[DIEU]`)


---

### Mẫu #01_2025_TT-BKHĐT_174764#body_standalone_87 (Loại: `body_standalone`)
> **[Điều 5]`<DIEU>`** . **[2 . Phân tổ chủ yếu : Hệ sinh thái biển .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 5** → `DIEU` (span: `[0:2]`)
- `[e1]` **2 . Phân tổ chủ yếu : Hệ sinh thái biển .** → `KHOAN` (span: `[3:13]`)

**Quan hệ:**
- (`e1` 2 . Phân tổ chủ yếu : Hệ sinh thái biển . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 5 `[DIEU]`)


---

### Mẫu #01_2025_TT-BKHĐT_174764#hard_negative_88 (Loại: `hard_negative`)
> CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM Độc lập - Tự do - Hạnh phúc


---
