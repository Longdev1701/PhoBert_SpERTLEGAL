# Dữ liệu gán nhãn văn bản: 06_2012_TT-BKHĐT_27861
- **Thể loại**: `thong_tu`
- **Phân vùng dữ liệu**: `TRAIN`
- **Tổng số mẫu**: 101 mẫu
- **Tổng số thực thể**: 765
- **Tổng số quan hệ**: 591

---

### Mẫu #06_2012_TT-BKHĐT_27861#preamble_context_0 (Loại: `preamble_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[06/2012/TT-BKHĐT]`<SO_HIEU>`** của **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** . **[Căn cứ]`<TU_KHOA_PHAP_LY>`** **[Luật Thi đua]`<THAM_CHIEU_PHAP_LY>`** , Khen thưởng **[ngày 25 tháng 12 năm 2003]`<NGAY_THAM_CHIEU>`** và Luật **[sửa đổi , bổ sung một số điều của]`<TU_KHOA_PHAP_LY>`** Luật Thi đua , Khen thưởng ngày 14 tháng 6 năm 2005 ;

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **06/2012/TT-BKHĐT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[4:8]`)
- `[e3]` **Luật Thi đua** → `THAM_CHIEU_PHAP_LY` (span: `[10:12]`)
- `[e4]` **Căn cứ** → `TU_KHOA_PHAP_LY` (span: `[9:10]`)
- `[e5]` **sửa đổi , bổ sung một số điều của** → `TU_KHOA_PHAP_LY` (span: `[22:28]`)
- `[e6]` **ngày 25 tháng 12 năm 2003** → `NGAY_THAM_CHIEU` (span: `[14:20]`)

**Quan hệ:**
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e4` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Luật Thi đua `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Luật Thi đua `[THAM_CHIEU_PHAP_LY]`)
- (`e3` Luật Thi đua `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e6` ngày 25 tháng 12 năm 2003 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #06_2012_TT-BKHĐT_27861#preamble_standalone_1 (Loại: `preamble_standalone`)
> **[Căn cứ]`<TU_KHOA_PHAP_LY>`** **[Luật Thi đua]`<THAM_CHIEU_PHAP_LY>`** , Khen thưởng **[ngày 25 tháng 12 năm 2003]`<NGAY_THAM_CHIEU>`** và Luật **[sửa đổi , bổ sung một số điều của]`<TU_KHOA_PHAP_LY>`** Luật Thi đua , Khen thưởng ngày 14 tháng 6 năm 2005 ;

**Thực thể:**
- `[e0]` **Luật Thi đua** → `THAM_CHIEU_PHAP_LY` (span: `[1:3]`)
- `[e1]` **Căn cứ** → `TU_KHOA_PHAP_LY` (span: `[0:1]`)
- `[e2]` **sửa đổi , bổ sung một số điều của** → `TU_KHOA_PHAP_LY` (span: `[13:19]`)
- `[e3]` **ngày 25 tháng 12 năm 2003** → `NGAY_THAM_CHIEU` (span: `[5:11]`)

**Quan hệ:**
- (`e1` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e0` Luật Thi đua `[THAM_CHIEU_PHAP_LY]`)
- (`e0` Luật Thi đua `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e3` ngày 25 tháng 12 năm 2003 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #06_2012_TT-BKHĐT_27861#preamble_context_2 (Loại: `preamble_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[06/2012/TT-BKHĐT]`<SO_HIEU>`** của **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** . **[Căn cứ]`<TU_KHOA_PHAP_LY>`** **[Nghị định số 42/2010/NĐ-CP]`<THAM_CHIEU_PHAP_LY>`** **[ngày 15 tháng 4 năm 2010]`<NGAY_THAM_CHIEU>`** của **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** Quy định chi tiết và hướng dẫn thi hành một số điều của Luật Thi đua , Khen thưởng và Luật **[sửa đổi , bổ sung một số điều của]`<TU_KHOA_PHAP_LY>`** Luật Thi đua , Khen thưởng ;

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **06/2012/TT-BKHĐT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[4:8]`)
- `[e3]` **Nghị định số 42/2010/NĐ-CP** → `THAM_CHIEU_PHAP_LY` (span: `[10:13]`)
- `[e4]` **Căn cứ** → `TU_KHOA_PHAP_LY` (span: `[9:10]`)
- `[e5]` **sửa đổi , bổ sung một số điều của** → `TU_KHOA_PHAP_LY` (span: `[35:41]`)
- `[e6]` **ngày 15 tháng 4 năm 2010** → `NGAY_THAM_CHIEU` (span: `[13:19]`)
- `[e7]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[20:21]`)

**Quan hệ:**
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e4` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Nghị định số 42/2010/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Nghị định số 42/2010/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e3` Nghị định số 42/2010/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e6` ngày 15 tháng 4 năm 2010 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #06_2012_TT-BKHĐT_27861#preamble_standalone_3 (Loại: `preamble_standalone`)
> **[Căn cứ]`<TU_KHOA_PHAP_LY>`** **[Nghị định số 42/2010/NĐ-CP]`<THAM_CHIEU_PHAP_LY>`** **[ngày 15 tháng 4 năm 2010]`<NGAY_THAM_CHIEU>`** của **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** Quy định chi tiết và hướng dẫn thi hành một số điều của Luật Thi đua , Khen thưởng và Luật **[sửa đổi , bổ sung một số điều của]`<TU_KHOA_PHAP_LY>`** Luật Thi đua , Khen thưởng ;

**Thực thể:**
- `[e0]` **Nghị định số 42/2010/NĐ-CP** → `THAM_CHIEU_PHAP_LY` (span: `[1:4]`)
- `[e1]` **Căn cứ** → `TU_KHOA_PHAP_LY` (span: `[0:1]`)
- `[e2]` **sửa đổi , bổ sung một số điều của** → `TU_KHOA_PHAP_LY` (span: `[26:32]`)
- `[e3]` **ngày 15 tháng 4 năm 2010** → `NGAY_THAM_CHIEU` (span: `[4:10]`)
- `[e4]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[11:12]`)

**Quan hệ:**
- (`e1` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e0` Nghị định số 42/2010/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e4` Chính phủ `[CO_QUAN_THAM_QUYEN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e0` Nghị định số 42/2010/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e0` Nghị định số 42/2010/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e3` ngày 15 tháng 4 năm 2010 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #06_2012_TT-BKHĐT_27861#preamble_context_4 (Loại: `preamble_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[06/2012/TT-BKHĐT]`<SO_HIEU>`** của **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** . **[Căn cứ]`<TU_KHOA_PHAP_LY>`** **[Nghị định số 39/2012/NĐ-CP]`<THAM_CHIEU_PHAP_LY>`** **[ngày 27 tháng 4 năm 2012]`<NGAY_THAM_CHIEU>`** của **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** **[Sửa đổi , bổ sung một số điều của]`<TU_KHOA_PHAP_LY>`** **[Nghị định số 42/2010/NĐ-CP]`<THAM_CHIEU_PHAP_LY>`** **[ngày 15 tháng 4 năm 2010]`<NGAY_THAM_CHIEU>`** của **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** Quy định chi tiết và hướng dẫn thi hành một số điều của Luật Thi đua , Khen thưởng và Luật **[sửa đổi , bổ sung một số điều của]`<TU_KHOA_PHAP_LY>`** Luật Thi đua , Khen thưởng ;

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **06/2012/TT-BKHĐT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[4:8]`)
- `[e3]` **Nghị định số 39/2012/NĐ-CP** → `THAM_CHIEU_PHAP_LY` (span: `[10:13]`)
- `[e4]` **Nghị định số 42/2010/NĐ-CP** → `THAM_CHIEU_PHAP_LY` (span: `[27:30]`)
- `[e5]` **Căn cứ** → `TU_KHOA_PHAP_LY` (span: `[9:10]`)
- `[e6]` **Sửa đổi , bổ sung một số điều của** → `TU_KHOA_PHAP_LY` (span: `[21:27]`)
- `[e7]` **sửa đổi , bổ sung một số điều của** → `TU_KHOA_PHAP_LY` (span: `[52:58]`)
- `[e8]` **ngày 27 tháng 4 năm 2012** → `NGAY_THAM_CHIEU` (span: `[13:19]`)
- `[e9]` **ngày 15 tháng 4 năm 2010** → `NGAY_THAM_CHIEU` (span: `[30:36]`)
- `[e10]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[20:21]`)
- `[e11]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[37:38]`)

**Quan hệ:**
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e5` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Nghị định số 39/2012/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Nghị định số 39/2012/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e6` Sửa đổi , bổ sung một số điều của `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e4` Nghị định số 42/2010/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e4` Nghị định số 42/2010/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e3` Nghị định số 39/2012/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e8` ngày 27 tháng 4 năm 2012 `[NGAY_THAM_CHIEU]`)
- (`e4` Nghị định số 42/2010/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e9` ngày 15 tháng 4 năm 2010 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #06_2012_TT-BKHĐT_27861#preamble_standalone_5 (Loại: `preamble_standalone`)
> **[Căn cứ]`<TU_KHOA_PHAP_LY>`** **[Nghị định số 39/2012/NĐ-CP]`<THAM_CHIEU_PHAP_LY>`** **[ngày 27 tháng 4 năm 2012]`<NGAY_THAM_CHIEU>`** của **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** **[Sửa đổi , bổ sung một số điều của]`<TU_KHOA_PHAP_LY>`** **[Nghị định số 42/2010/NĐ-CP]`<THAM_CHIEU_PHAP_LY>`** **[ngày 15 tháng 4 năm 2010]`<NGAY_THAM_CHIEU>`** của **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** Quy định chi tiết và hướng dẫn thi hành một số điều của Luật Thi đua , Khen thưởng và Luật **[sửa đổi , bổ sung một số điều của]`<TU_KHOA_PHAP_LY>`** Luật Thi đua , Khen thưởng ;

**Thực thể:**
- `[e0]` **Nghị định số 39/2012/NĐ-CP** → `THAM_CHIEU_PHAP_LY` (span: `[1:4]`)
- `[e1]` **Nghị định số 42/2010/NĐ-CP** → `THAM_CHIEU_PHAP_LY` (span: `[18:21]`)
- `[e2]` **Căn cứ** → `TU_KHOA_PHAP_LY` (span: `[0:1]`)
- `[e3]` **Sửa đổi , bổ sung một số điều của** → `TU_KHOA_PHAP_LY` (span: `[12:18]`)
- `[e4]` **sửa đổi , bổ sung một số điều của** → `TU_KHOA_PHAP_LY` (span: `[43:49]`)
- `[e5]` **ngày 27 tháng 4 năm 2012** → `NGAY_THAM_CHIEU` (span: `[4:10]`)
- `[e6]` **ngày 15 tháng 4 năm 2010** → `NGAY_THAM_CHIEU` (span: `[21:27]`)
- `[e7]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[11:12]`)
- `[e8]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[28:29]`)

**Quan hệ:**
- (`e2` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e0` Nghị định số 39/2012/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e7` Chính phủ `[CO_QUAN_THAM_QUYEN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e0` Nghị định số 39/2012/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e3` Sửa đổi , bổ sung một số điều của `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e1` Nghị định số 42/2010/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e7` Chính phủ `[CO_QUAN_THAM_QUYEN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e1` Nghị định số 42/2010/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e0` Nghị định số 39/2012/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e5` ngày 27 tháng 4 năm 2012 `[NGAY_THAM_CHIEU]`)
- (`e1` Nghị định số 42/2010/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e6` ngày 15 tháng 4 năm 2010 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #06_2012_TT-BKHĐT_27861#preamble_context_6 (Loại: `preamble_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[06/2012/TT-BKHĐT]`<SO_HIEU>`** của **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** . **[Căn cứ]`<TU_KHOA_PHAP_LY>`** **[Nghị định số 116/2008/NĐ-CP]`<THAM_CHIEU_PHAP_LY>`** **[ngày 14 tháng 11 năm 2008]`<NGAY_THAM_CHIEU>`** của **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** quy định chức năng , nhiệm vụ , quyền hạn và cơ cấu tổ chức của **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_THAM_QUYEN>`** ;

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **06/2012/TT-BKHĐT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[4:8]`)
- `[e3]` **Nghị định số 116/2008/NĐ-CP** → `THAM_CHIEU_PHAP_LY` (span: `[10:13]`)
- `[e4]` **Căn cứ** → `TU_KHOA_PHAP_LY` (span: `[9:10]`)
- `[e5]` **ngày 14 tháng 11 năm 2008** → `NGAY_THAM_CHIEU` (span: `[13:19]`)
- `[e6]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[20:21]`)
- `[e7]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_THAM_QUYEN` (span: `[31:35]`)

**Quan hệ:**
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e4` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Nghị định số 116/2008/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Nghị định số 116/2008/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e3` Nghị định số 116/2008/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e5` ngày 14 tháng 11 năm 2008 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #06_2012_TT-BKHĐT_27861#preamble_standalone_7 (Loại: `preamble_standalone`)
> **[Căn cứ]`<TU_KHOA_PHAP_LY>`** **[Nghị định số 116/2008/NĐ-CP]`<THAM_CHIEU_PHAP_LY>`** **[ngày 14 tháng 11 năm 2008]`<NGAY_THAM_CHIEU>`** của **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** quy định chức năng , nhiệm vụ , quyền hạn và cơ cấu tổ chức của **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_THAM_QUYEN>`** ;

**Thực thể:**
- `[e0]` **Nghị định số 116/2008/NĐ-CP** → `THAM_CHIEU_PHAP_LY` (span: `[1:4]`)
- `[e1]` **Căn cứ** → `TU_KHOA_PHAP_LY` (span: `[0:1]`)
- `[e2]` **ngày 14 tháng 11 năm 2008** → `NGAY_THAM_CHIEU` (span: `[4:10]`)
- `[e3]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[11:12]`)
- `[e4]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_THAM_QUYEN` (span: `[22:26]`)

**Quan hệ:**
- (`e1` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e0` Nghị định số 116/2008/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e3` Chính phủ `[CO_QUAN_THAM_QUYEN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e0` Nghị định số 116/2008/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e0` Nghị định số 116/2008/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e2` ngày 14 tháng 11 năm 2008 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #06_2012_TT-BKHĐT_27861#preamble_context_8 (Loại: `preamble_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[06/2012/TT-BKHĐT]`<SO_HIEU>`** của **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** . **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_THAM_QUYEN>`** ban hành Thông tư hướng dẫn công tác thi đua , khen thưởng **[ngành Kế hoạch và Đầu tư]`<LINH_VUC>`** như sau :

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **06/2012/TT-BKHĐT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[4:8]`)
- `[e3]` **ngành Kế hoạch và Đầu tư** → `LINH_VUC` (span: `[20:24]`)
- `[e4]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_THAM_QUYEN` (span: `[9:13]`)

**Quan hệ:**
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` ngành Kế hoạch và Đầu tư `[LINH_VUC]`)


---

### Mẫu #06_2012_TT-BKHĐT_27861#preamble_standalone_9 (Loại: `preamble_standalone`)
> **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_THAM_QUYEN>`** ban hành Thông tư hướng dẫn công tác thi đua , khen thưởng **[ngành Kế hoạch và Đầu tư]`<LINH_VUC>`** như sau :

**Thực thể:**
- `[e0]` **ngành Kế hoạch và Đầu tư** → `LINH_VUC` (span: `[11:15]`)
- `[e1]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_THAM_QUYEN` (span: `[0:4]`)

**Quan hệ:**
- (`e1` Bộ Kế hoạch và Đầu tư `[CO_QUAN_THAM_QUYEN]`) ==[ **THUOC_LINH_VUC** ]==> (`e0` ngành Kế hoạch và Đầu tư `[LINH_VUC]`)


---

### Mẫu #06_2012_TT-BKHĐT_27861#body_context_10 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[06/2012/TT-BKHĐT]`<SO_HIEU>`** ban hành **[ngày 19 tháng 10 năm 2012]`<NGAY_BAN_HANH>`** bởi **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** . **[Chương I. QUY ĐỊNH CHUNG]`<CHUONG>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **06/2012/TT-BKHĐT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[11:15]`)
- `[e3]` **ngày 19 tháng 10 năm 2012** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Chương I. QUY ĐỊNH CHUNG** → `CHUONG` (span: `[16:20]`)

**Quan hệ:**
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 19 tháng 10 năm 2012 `[NGAY_BAN_HANH]`)
- (`e4` Chương I. QUY ĐỊNH CHUNG `[CHUONG]`) ==[ **THUOC_VE** ]==> (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`)


---

### Mẫu #06_2012_TT-BKHĐT_27861#body_context_11 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[06/2012/TT-BKHĐT]`<SO_HIEU>`** ban hành **[ngày 19 tháng 10 năm 2012]`<NGAY_BAN_HANH>`** bởi **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** . **[Điều 2]`<DIEU>`** . **[Khoản 2]`<KHOAN>`** . **[c ) Các **[doanh nghiệp]`<TO_CHUC_DOANH_NGHIEP>`** Việt Nam đầu tư ra nước ngoài ; các **[doanh nghiệp]`<TO_CHUC_DOANH_NGHIEP>`** có vốn đ ầ u tư nước ngoài hoạt động **[tại Việt Nam]`<DIA_DIEM>`** ; các **[doanh nghiệp]`<TO_CHUC_DOANH_NGHIEP>`** thuộc phạm vi qu ả n lý c ủ a các Ban Quản lý các **[doanh nghiệp]`<TO_CHUC_DOANH_NGHIEP>`** hoạt động theo Lu ậ t Đ ầ u tư , Luật **[Doanh nghiệp]`<TO_CHUC_DOANH_NGHIEP>`** , Luật **[Hợp tác xã]`<TO_CHUC_DOANH_NGHIEP>`** .]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **06/2012/TT-BKHĐT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[11:15]`)
- `[e3]` **ngày 19 tháng 10 năm 2012** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 2** → `DIEU` (span: `[16:18]`)
- `[e5]` **Khoản 2** → `KHOAN` (span: `[19:21]`)
- `[e6]` **c ) Các doanh nghiệp Việt Nam đầu tư ra nước ngoài ; các doanh nghiệp có vốn đ ầ u tư nước ngoài hoạt động tại Việt Nam ; các doanh nghiệp thuộc phạm vi qu ả n lý c ủ a các Ban Quản lý các doanh nghiệp hoạt động theo Lu ậ t Đ ầ u tư , Luật Doanh nghiệp , Luật Hợp tác xã .** → `DIEM` (span: `[22:74]`)
- `[e7]` **doanh nghiệp** → `TO_CHUC_DOANH_NGHIEP` (span: `[25:26]`) *(lồng trong `e6` (`DIEM`))*
- `[e8]` **doanh nghiệp** → `TO_CHUC_DOANH_NGHIEP` (span: `[32:33]`) *(lồng trong `e6` (`DIEM`))*
- `[e9]` **doanh nghiệp** → `TO_CHUC_DOANH_NGHIEP` (span: `[44:45]`) *(lồng trong `e6` (`DIEM`))*
- `[e10]` **doanh nghiệp** → `TO_CHUC_DOANH_NGHIEP` (span: `[58:59]`) *(lồng trong `e6` (`DIEM`))*
- `[e11]` **Doanh nghiệp** → `TO_CHUC_DOANH_NGHIEP` (span: `[69:70]`) *(lồng trong `e6` (`DIEM`))*
- `[e12]` **Hợp tác xã** → `TO_CHUC_DOANH_NGHIEP` (span: `[72:73]`) *(lồng trong `e6` (`DIEM`))*
- `[e13]` **tại Việt Nam** → `DIA_DIEM` (span: `[40:42]`) *(lồng trong `e6` (`DIEM`))*

**Quan hệ:**
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 19 tháng 10 năm 2012 `[NGAY_BAN_HANH]`)
- (`e4` Điều 2 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`)
- (`e5` Khoản 2 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 2 `[DIEU]`)
- (`e6` c ) Các doanh nghiệp Việt Nam đầu tư ra nước ngoài ; các doanh nghiệp có vốn đ ầ u tư nước ngoài hoạt động tại Việt Nam ; các doanh nghiệp thuộc phạm vi qu ả n lý c ủ a các Ban Quản lý các doanh nghiệp hoạt động theo Lu ậ t Đ ầ u tư , Luật Doanh nghiệp , Luật Hợp tác xã . `[DIEM]`) ==[ **THUOC_VE** ]==> (`e5` Khoản 2 `[KHOAN]`)


---

### Mẫu #06_2012_TT-BKHĐT_27861#body_standalone_12 (Loại: `body_standalone`)
> **[Điều 2]`<DIEU>`** . **[Khoản 2]`<KHOAN>`** . **[c ) Các **[doanh nghiệp]`<TO_CHUC_DOANH_NGHIEP>`** Việt Nam đầu tư ra nước ngoài ; các **[doanh nghiệp]`<TO_CHUC_DOANH_NGHIEP>`** có vốn đ ầ u tư nước ngoài hoạt động **[tại Việt Nam]`<DIA_DIEM>`** ; các **[doanh nghiệp]`<TO_CHUC_DOANH_NGHIEP>`** thuộc phạm vi qu ả n lý c ủ a các Ban Quản lý các **[doanh nghiệp]`<TO_CHUC_DOANH_NGHIEP>`** hoạt động theo Lu ậ t Đ ầ u tư , Luật **[Doanh nghiệp]`<TO_CHUC_DOANH_NGHIEP>`** , Luật **[Hợp tác xã]`<TO_CHUC_DOANH_NGHIEP>`** .]`<DIEM>`**

**Thực thể:**
- `[e0]` **Điều 2** → `DIEU` (span: `[0:2]`)
- `[e1]` **Khoản 2** → `KHOAN` (span: `[3:5]`)
- `[e2]` **c ) Các doanh nghiệp Việt Nam đầu tư ra nước ngoài ; các doanh nghiệp có vốn đ ầ u tư nước ngoài hoạt động tại Việt Nam ; các doanh nghiệp thuộc phạm vi qu ả n lý c ủ a các Ban Quản lý các doanh nghiệp hoạt động theo Lu ậ t Đ ầ u tư , Luật Doanh nghiệp , Luật Hợp tác xã .** → `DIEM` (span: `[6:58]`)
- `[e3]` **doanh nghiệp** → `TO_CHUC_DOANH_NGHIEP` (span: `[9:10]`) *(lồng trong `e2` (`DIEM`))*
- `[e4]` **doanh nghiệp** → `TO_CHUC_DOANH_NGHIEP` (span: `[16:17]`) *(lồng trong `e2` (`DIEM`))*
- `[e5]` **doanh nghiệp** → `TO_CHUC_DOANH_NGHIEP` (span: `[28:29]`) *(lồng trong `e2` (`DIEM`))*
- `[e6]` **doanh nghiệp** → `TO_CHUC_DOANH_NGHIEP` (span: `[42:43]`) *(lồng trong `e2` (`DIEM`))*
- `[e7]` **Doanh nghiệp** → `TO_CHUC_DOANH_NGHIEP` (span: `[53:54]`) *(lồng trong `e2` (`DIEM`))*
- `[e8]` **Hợp tác xã** → `TO_CHUC_DOANH_NGHIEP` (span: `[56:57]`) *(lồng trong `e2` (`DIEM`))*
- `[e9]` **tại Việt Nam** → `DIA_DIEM` (span: `[24:26]`) *(lồng trong `e2` (`DIEM`))*

**Quan hệ:**
- (`e1` Khoản 2 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 2 `[DIEU]`)
- (`e2` c ) Các doanh nghiệp Việt Nam đầu tư ra nước ngoài ; các doanh nghiệp có vốn đ ầ u tư nước ngoài hoạt động tại Việt Nam ; các doanh nghiệp thuộc phạm vi qu ả n lý c ủ a các Ban Quản lý các doanh nghiệp hoạt động theo Lu ậ t Đ ầ u tư , Luật Doanh nghiệp , Luật Hợp tác xã . `[DIEM]`) ==[ **THUOC_VE** ]==> (`e1` Khoản 2 `[KHOAN]`)


---

### Mẫu #06_2012_TT-BKHĐT_27861#body_context_13 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[06/2012/TT-BKHĐT]`<SO_HIEU>`** ban hành **[ngày 19 tháng 10 năm 2012]`<NGAY_BAN_HANH>`** bởi **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** . **[Điều 2]`<DIEU>`** . **[3 . Riêng các cá nhân , tập thể thuộc T ổ ng cục Thống kê thực hiện theo Quy chế Thi đua , Khen thưởng **[ngành Thống kê]`<LINH_VUC>`** kèm **[Quyết định số 718/QĐ-TCTK]`<THAM_CHIEU_PHAP_LY>`** **[ngày 02/11/2011]`<NGAY_THAM_CHIEU>`** của Tổ ng cục trưởng Tổng cục Thống kê .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **06/2012/TT-BKHĐT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[11:15]`)
- `[e3]` **ngày 19 tháng 10 năm 2012** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 2** → `DIEU` (span: `[16:18]`)
- `[e5]` **3 . Riêng các cá nhân , tập thể thuộc T ổ ng cục Thống kê thực hiện theo Quy chế Thi đua , Khen thưởng ngành Thống kê kèm Quyết định số 718/QĐ-TCTK ngày 02/11/2011 của Tổ ng cục trưởng Tổng cục Thống kê .** → `KHOAN` (span: `[19:51]`)
- `[e6]` **Quyết định số 718/QĐ-TCTK** → `THAM_CHIEU_PHAP_LY` (span: `[40:43]`) *(lồng trong `e5` (`KHOAN`))*
- `[e7]` **ngày 02/11/2011** → `NGAY_THAM_CHIEU` (span: `[43:45]`) *(lồng trong `e5` (`KHOAN`))*
- `[e8]` **ngành Thống kê** → `LINH_VUC` (span: `[37:39]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 19 tháng 10 năm 2012 `[NGAY_BAN_HANH]`)
- (`e4` Điều 2 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`)
- (`e5` 3 . Riêng các cá nhân , tập thể thuộc T ổ ng cục Thống kê thực hiện theo Quy chế Thi đua , Khen thưởng ngành Thống kê kèm Quyết định số 718/QĐ-TCTK ngày 02/11/2011 của Tổ ng cục trưởng Tổng cục Thống kê . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 2 `[DIEU]`)
- (`e5` 3 . Riêng các cá nhân , tập thể thuộc T ổ ng cục Thống kê thực hiện theo Quy chế Thi đua , Khen thưởng ngành Thống kê kèm Quyết định số 718/QĐ-TCTK ngày 02/11/2011 của Tổ ng cục trưởng Tổng cục Thống kê . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e6` Quyết định số 718/QĐ-TCTK `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e8` ngành Thống kê `[LINH_VUC]`)
- (`e5` 3 . Riêng các cá nhân , tập thể thuộc T ổ ng cục Thống kê thực hiện theo Quy chế Thi đua , Khen thưởng ngành Thống kê kèm Quyết định số 718/QĐ-TCTK ngày 02/11/2011 của Tổ ng cục trưởng Tổng cục Thống kê . `[KHOAN]`) ==[ **THUOC_LINH_VUC** ]==> (`e8` ngành Thống kê `[LINH_VUC]`) *(Quan hệ lồng nhau)*
- (`e6` Quyết định số 718/QĐ-TCTK `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e7` ngày 02/11/2011 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #06_2012_TT-BKHĐT_27861#body_standalone_14 (Loại: `body_standalone`)
> **[Điều 2]`<DIEU>`** . **[3 . Riêng các cá nhân , tập thể thuộc T ổ ng cục Thống kê thực hiện theo Quy chế Thi đua , Khen thưởng **[ngành Thống kê]`<LINH_VUC>`** kèm **[Quyết định số 718/QĐ-TCTK]`<THAM_CHIEU_PHAP_LY>`** **[ngày 02/11/2011]`<NGAY_THAM_CHIEU>`** của Tổ ng cục trưởng Tổng cục Thống kê .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 2** → `DIEU` (span: `[0:2]`)
- `[e1]` **3 . Riêng các cá nhân , tập thể thuộc T ổ ng cục Thống kê thực hiện theo Quy chế Thi đua , Khen thưởng ngành Thống kê kèm Quyết định số 718/QĐ-TCTK ngày 02/11/2011 của Tổ ng cục trưởng Tổng cục Thống kê .** → `KHOAN` (span: `[3:35]`)
- `[e2]` **Quyết định số 718/QĐ-TCTK** → `THAM_CHIEU_PHAP_LY` (span: `[24:27]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **ngày 02/11/2011** → `NGAY_THAM_CHIEU` (span: `[27:29]`) *(lồng trong `e1` (`KHOAN`))*
- `[e4]` **ngành Thống kê** → `LINH_VUC` (span: `[21:23]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 3 . Riêng các cá nhân , tập thể thuộc T ổ ng cục Thống kê thực hiện theo Quy chế Thi đua , Khen thưởng ngành Thống kê kèm Quyết định số 718/QĐ-TCTK ngày 02/11/2011 của Tổ ng cục trưởng Tổng cục Thống kê . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 2 `[DIEU]`)
- (`e1` 3 . Riêng các cá nhân , tập thể thuộc T ổ ng cục Thống kê thực hiện theo Quy chế Thi đua , Khen thưởng ngành Thống kê kèm Quyết định số 718/QĐ-TCTK ngày 02/11/2011 của Tổ ng cục trưởng Tổng cục Thống kê . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e2` Quyết định số 718/QĐ-TCTK `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e1` 3 . Riêng các cá nhân , tập thể thuộc T ổ ng cục Thống kê thực hiện theo Quy chế Thi đua , Khen thưởng ngành Thống kê kèm Quyết định số 718/QĐ-TCTK ngày 02/11/2011 của Tổ ng cục trưởng Tổng cục Thống kê . `[KHOAN]`) ==[ **THUOC_LINH_VUC** ]==> (`e4` ngành Thống kê `[LINH_VUC]`) *(Quan hệ lồng nhau)*
- (`e2` Quyết định số 718/QĐ-TCTK `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e3` ngày 02/11/2011 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #06_2012_TT-BKHĐT_27861#body_context_15 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[06/2012/TT-BKHĐT]`<SO_HIEU>`** của **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Khoa học và công nghệ]`<LINH_VUC>`** . **[Điều 2]`<DIEU>`** . **[Khoản 4 . Trong Thông tư hướng dẫn này , các từ ngữ dưới đây được hiểu như sau]`<KHOAN>`** : **[g ) Các đ ơn vị thuộc Bộ : Được hiểu là các đơn vị trực thuộc Bộ K ế hoạch và Đầu tư được **[quy định tại]`<TU_KHOA_PHAP_LY>`** **[Điều 3]`<THAM_CHIEU_PHAP_LY>`** , Nghị định 116/2008/NĐ-CP ng à y **[14/11/2008]`<NGAY_THAM_CHIEU>`** của **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** quy định về chức năng , nhiệm vụ , quyền hạn và c ơ c ấ u t ổ chức của Bộ K ế hoạch và Đ ầ u tư và Cục Quản lý Đăng ký kinh]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **06/2012/TT-BKHĐT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[4:8]`)
- `[e3]` **Khoa học và công nghệ** → `LINH_VUC` (span: `[10:13]`)
- `[e4]` **Điều 2** → `DIEU` (span: `[14:16]`)
- `[e5]` **Khoản 4 . Trong Thông tư hướng dẫn này , các từ ngữ dưới đây được hiểu như sau** → `KHOAN` (span: `[17:33]`)
- `[e6]` **g ) Các đ ơn vị thuộc Bộ : Được hiểu là các đơn vị trực thuộc Bộ K ế hoạch và Đầu tư được quy định tại Điều 3 , Nghị định 116/2008/NĐ-CP ng à y 14/11/2008 của Chính phủ quy định về chức năng , nhiệm vụ , quyền hạn và c ơ c ấ u t ổ chức của Bộ K ế hoạch và Đ ầ u tư và Cục Quản lý Đăng ký kinh** → `DIEM` (span: `[34:98]`)
- `[e7]` **Điều 3** → `THAM_CHIEU_PHAP_LY` (span: `[58:60]`) *(lồng trong `e6` (`DIEM`))*
- `[e8]` **quy định tại** → `TU_KHOA_PHAP_LY` (span: `[56:58]`) *(lồng trong `e6` (`DIEM`))*
- `[e9]` **14/11/2008** → `NGAY_THAM_CHIEU` (span: `[66:67]`) *(lồng trong `e6` (`DIEM`))*
- `[e10]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[68:69]`) *(lồng trong `e6` (`DIEM`))*

**Quan hệ:**
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Khoa học và công nghệ `[LINH_VUC]`)
- (`e4` Điều 2 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`)
- (`e5` Khoản 4 . Trong Thông tư hướng dẫn này , các từ ngữ dưới đây được hiểu như sau `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 2 `[DIEU]`)
- (`e6` g ) Các đ ơn vị thuộc Bộ : Được hiểu là các đơn vị trực thuộc Bộ K ế hoạch và Đầu tư được quy định tại Điều 3 , Nghị định 116/2008/NĐ-CP ng à y 14/11/2008 của Chính phủ quy định về chức năng , nhiệm vụ , quyền hạn và c ơ c ấ u t ổ chức của Bộ K ế hoạch và Đ ầ u tư và Cục Quản lý Đăng ký kinh `[DIEM]`) ==[ **THUOC_VE** ]==> (`e5` Khoản 4 . Trong Thông tư hướng dẫn này , các từ ngữ dưới đây được hiểu như sau `[KHOAN]`)
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Khoa học và công nghệ `[LINH_VUC]`)
- (`e6` g ) Các đ ơn vị thuộc Bộ : Được hiểu là các đơn vị trực thuộc Bộ K ế hoạch và Đầu tư được quy định tại Điều 3 , Nghị định 116/2008/NĐ-CP ng à y 14/11/2008 của Chính phủ quy định về chức năng , nhiệm vụ , quyền hạn và c ơ c ấ u t ổ chức của Bộ K ế hoạch và Đ ầ u tư và Cục Quản lý Đăng ký kinh `[DIEM]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Khoa học và công nghệ `[LINH_VUC]`)
- (`e8` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e7` Điều 3 `[THAM_CHIEU_PHAP_LY]`)
- (`e6` g ) Các đ ơn vị thuộc Bộ : Được hiểu là các đơn vị trực thuộc Bộ K ế hoạch và Đầu tư được quy định tại Điều 3 , Nghị định 116/2008/NĐ-CP ng à y 14/11/2008 của Chính phủ quy định về chức năng , nhiệm vụ , quyền hạn và c ơ c ấ u t ổ chức của Bộ K ế hoạch và Đ ầ u tư và Cục Quản lý Đăng ký kinh `[DIEM]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e7` Điều 3 `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e7` Điều 3 `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e9` 14/11/2008 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #06_2012_TT-BKHĐT_27861#body_standalone_16 (Loại: `body_standalone`)
> **[Điều 2]`<DIEU>`** . **[Khoản 4 . Trong Thông tư hướng dẫn này , các từ ngữ dưới đây được hiểu như sau]`<KHOAN>`** : **[g ) Các đ ơn vị thuộc Bộ : Được hiểu là các đơn vị trực thuộc Bộ K ế hoạch và Đầu tư được **[quy định tại]`<TU_KHOA_PHAP_LY>`** **[Điều 3]`<THAM_CHIEU_PHAP_LY>`** , Nghị định 116/2008/NĐ-CP ng à y **[14/11/2008]`<NGAY_THAM_CHIEU>`** của **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** quy định về chức năng , nhiệm vụ , quyền hạn và c ơ c ấ u t ổ chức của Bộ K ế hoạch và Đ ầ u tư và Cục Quản lý Đăng ký kinh]`<DIEM>`**

**Thực thể:**
- `[e0]` **Điều 2** → `DIEU` (span: `[0:2]`)
- `[e1]` **Khoản 4 . Trong Thông tư hướng dẫn này , các từ ngữ dưới đây được hiểu như sau** → `KHOAN` (span: `[3:19]`)
- `[e2]` **g ) Các đ ơn vị thuộc Bộ : Được hiểu là các đơn vị trực thuộc Bộ K ế hoạch và Đầu tư được quy định tại Điều 3 , Nghị định 116/2008/NĐ-CP ng à y 14/11/2008 của Chính phủ quy định về chức năng , nhiệm vụ , quyền hạn và c ơ c ấ u t ổ chức của Bộ K ế hoạch và Đ ầ u tư và Cục Quản lý Đăng ký kinh** → `DIEM` (span: `[20:84]`)
- `[e3]` **Điều 3** → `THAM_CHIEU_PHAP_LY` (span: `[44:46]`) *(lồng trong `e2` (`DIEM`))*
- `[e4]` **quy định tại** → `TU_KHOA_PHAP_LY` (span: `[42:44]`) *(lồng trong `e2` (`DIEM`))*
- `[e5]` **14/11/2008** → `NGAY_THAM_CHIEU` (span: `[52:53]`) *(lồng trong `e2` (`DIEM`))*
- `[e6]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[54:55]`) *(lồng trong `e2` (`DIEM`))*

**Quan hệ:**
- (`e1` Khoản 4 . Trong Thông tư hướng dẫn này , các từ ngữ dưới đây được hiểu như sau `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 2 `[DIEU]`)
- (`e2` g ) Các đ ơn vị thuộc Bộ : Được hiểu là các đơn vị trực thuộc Bộ K ế hoạch và Đầu tư được quy định tại Điều 3 , Nghị định 116/2008/NĐ-CP ng à y 14/11/2008 của Chính phủ quy định về chức năng , nhiệm vụ , quyền hạn và c ơ c ấ u t ổ chức của Bộ K ế hoạch và Đ ầ u tư và Cục Quản lý Đăng ký kinh `[DIEM]`) ==[ **THUOC_VE** ]==> (`e1` Khoản 4 . Trong Thông tư hướng dẫn này , các từ ngữ dưới đây được hiểu như sau `[KHOAN]`)
- (`e4` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Điều 3 `[THAM_CHIEU_PHAP_LY]`)
- (`e2` g ) Các đ ơn vị thuộc Bộ : Được hiểu là các đơn vị trực thuộc Bộ K ế hoạch và Đầu tư được quy định tại Điều 3 , Nghị định 116/2008/NĐ-CP ng à y 14/11/2008 của Chính phủ quy định về chức năng , nhiệm vụ , quyền hạn và c ơ c ấ u t ổ chức của Bộ K ế hoạch và Đ ầ u tư và Cục Quản lý Đăng ký kinh `[DIEM]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Điều 3 `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e3` Điều 3 `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e5` 14/11/2008 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #06_2012_TT-BKHĐT_27861#body_context_17 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[06/2012/TT-BKHĐT]`<SO_HIEU>`** của **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Khoa học và công nghệ]`<LINH_VUC>`** . **[Điều 4]`<DIEU>`** . **[Khoản 2]`<KHOAN>`** . **[c ) Mộ t hình thức khen thưởng có thể tặng nhiều l ầ n cho một đối t ư ợng trong các lần thi đua khác nhau ; một đ ố i tượng chỉ được nhận một hình thức khen thưởng trong cùng một nội dung thi đua ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **06/2012/TT-BKHĐT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[4:8]`)
- `[e3]` **Khoa học và công nghệ** → `LINH_VUC` (span: `[10:13]`)
- `[e4]` **Điều 4** → `DIEU` (span: `[14:16]`)
- `[e5]` **Khoản 2** → `KHOAN` (span: `[17:19]`)
- `[e6]` **c ) Mộ t hình thức khen thưởng có thể tặng nhiều l ầ n cho một đối t ư ợng trong các lần thi đua khác nhau ; một đ ố i tượng chỉ được nhận một hình thức khen thưởng trong cùng một nội dung thi đua ;** → `DIEM` (span: `[20:60]`)

**Quan hệ:**
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Khoa học và công nghệ `[LINH_VUC]`)
- (`e4` Điều 4 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`)
- (`e5` Khoản 2 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 4 `[DIEU]`)
- (`e6` c ) Mộ t hình thức khen thưởng có thể tặng nhiều l ầ n cho một đối t ư ợng trong các lần thi đua khác nhau ; một đ ố i tượng chỉ được nhận một hình thức khen thưởng trong cùng một nội dung thi đua ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e5` Khoản 2 `[KHOAN]`)
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Khoa học và công nghệ `[LINH_VUC]`)
- (`e6` c ) Mộ t hình thức khen thưởng có thể tặng nhiều l ầ n cho một đối t ư ợng trong các lần thi đua khác nhau ; một đ ố i tượng chỉ được nhận một hình thức khen thưởng trong cùng một nội dung thi đua ; `[DIEM]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Khoa học và công nghệ `[LINH_VUC]`)


---

### Mẫu #06_2012_TT-BKHĐT_27861#body_context_18 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[06/2012/TT-BKHĐT]`<SO_HIEU>`** của **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Khoa học và công nghệ]`<LINH_VUC>`** . **[Điều 8]`<DIEU>`** . **[2 . Tập thể được tặng các danh hiệu th i đua , các hình thức khen thưởng được nhận Qu yế t đị nh khen thưởng và hiện vật ( **[theo quy định tại]`<TU_KHOA_PHAP_LY>`** **[Thông tư này]`<THAM_CHIEU_PHAP_LY>`** ) cấp gi ấ y khen , b ằ ng khen , **[giấy chứng nhận]`<GIAY_TO_HO_SO>`** và tiền thư ở ng theo quy định ; có quyền lưu giữ , trưng bày hiện vật được khen thư ở ng , được kê khai thành tích trong các văn bản , tài liệu của cơ quan , đơn vị .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **06/2012/TT-BKHĐT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[4:8]`)
- `[e3]` **Khoa học và công nghệ** → `LINH_VUC` (span: `[10:13]`)
- `[e4]` **Điều 8** → `DIEU` (span: `[14:16]`)
- `[e5]` **2 . Tập thể được tặng các danh hiệu th i đua , các hình thức khen thưởng được nhận Qu yế t đị nh khen thưởng và hiện vật ( theo quy định tại Thông tư này ) cấp gi ấ y khen , b ằ ng khen , giấy chứng nhận và tiền thư ở ng theo quy định ; có quyền lưu giữ , trưng bày hiện vật được khen thư ở ng , được kê khai thành tích trong các văn bản , tài liệu của cơ quan , đơn vị .** → `KHOAN` (span: `[17:93]`)
- `[e6]` **Thông tư này** → `THAM_CHIEU_PHAP_LY` (span: `[45:47]`) *(lồng trong `e5` (`KHOAN`))*
- `[e7]` **theo quy định tại** → `TU_KHOA_PHAP_LY` (span: `[42:45]`) *(lồng trong `e5` (`KHOAN`))*
- `[e8]` **giấy chứng nhận** → `GIAY_TO_HO_SO` (span: `[58:60]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Khoa học và công nghệ `[LINH_VUC]`)
- (`e4` Điều 8 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`)
- (`e5` 2 . Tập thể được tặng các danh hiệu th i đua , các hình thức khen thưởng được nhận Qu yế t đị nh khen thưởng và hiện vật ( theo quy định tại Thông tư này ) cấp gi ấ y khen , b ằ ng khen , giấy chứng nhận và tiền thư ở ng theo quy định ; có quyền lưu giữ , trưng bày hiện vật được khen thư ở ng , được kê khai thành tích trong các văn bản , tài liệu của cơ quan , đơn vị . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 8 `[DIEU]`)
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Khoa học và công nghệ `[LINH_VUC]`)
- (`e5` 2 . Tập thể được tặng các danh hiệu th i đua , các hình thức khen thưởng được nhận Qu yế t đị nh khen thưởng và hiện vật ( theo quy định tại Thông tư này ) cấp gi ấ y khen , b ằ ng khen , giấy chứng nhận và tiền thư ở ng theo quy định ; có quyền lưu giữ , trưng bày hiện vật được khen thư ở ng , được kê khai thành tích trong các văn bản , tài liệu của cơ quan , đơn vị . `[KHOAN]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Khoa học và công nghệ `[LINH_VUC]`)
- (`e7` theo quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e6` Thông tư này `[THAM_CHIEU_PHAP_LY]`)
- (`e5` 2 . Tập thể được tặng các danh hiệu th i đua , các hình thức khen thưởng được nhận Qu yế t đị nh khen thưởng và hiện vật ( theo quy định tại Thông tư này ) cấp gi ấ y khen , b ằ ng khen , giấy chứng nhận và tiền thư ở ng theo quy định ; có quyền lưu giữ , trưng bày hiện vật được khen thư ở ng , được kê khai thành tích trong các văn bản , tài liệu của cơ quan , đơn vị . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e6` Thông tư này `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #06_2012_TT-BKHĐT_27861#body_standalone_19 (Loại: `body_standalone`)
> **[Điều 8]`<DIEU>`** . **[2 . Tập thể được tặng các danh hiệu th i đua , các hình thức khen thưởng được nhận Qu yế t đị nh khen thưởng và hiện vật ( **[theo quy định tại]`<TU_KHOA_PHAP_LY>`** **[Thông tư này]`<THAM_CHIEU_PHAP_LY>`** ) cấp gi ấ y khen , b ằ ng khen , **[giấy chứng nhận]`<GIAY_TO_HO_SO>`** và tiền thư ở ng theo quy định ; có quyền lưu giữ , trưng bày hiện vật được khen thư ở ng , được kê khai thành tích trong các văn bản , tài liệu của cơ quan , đơn vị .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 8** → `DIEU` (span: `[0:2]`)
- `[e1]` **2 . Tập thể được tặng các danh hiệu th i đua , các hình thức khen thưởng được nhận Qu yế t đị nh khen thưởng và hiện vật ( theo quy định tại Thông tư này ) cấp gi ấ y khen , b ằ ng khen , giấy chứng nhận và tiền thư ở ng theo quy định ; có quyền lưu giữ , trưng bày hiện vật được khen thư ở ng , được kê khai thành tích trong các văn bản , tài liệu của cơ quan , đơn vị .** → `KHOAN` (span: `[3:79]`)
- `[e2]` **Thông tư này** → `THAM_CHIEU_PHAP_LY` (span: `[31:33]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **theo quy định tại** → `TU_KHOA_PHAP_LY` (span: `[28:31]`) *(lồng trong `e1` (`KHOAN`))*
- `[e4]` **giấy chứng nhận** → `GIAY_TO_HO_SO` (span: `[44:46]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 2 . Tập thể được tặng các danh hiệu th i đua , các hình thức khen thưởng được nhận Qu yế t đị nh khen thưởng và hiện vật ( theo quy định tại Thông tư này ) cấp gi ấ y khen , b ằ ng khen , giấy chứng nhận và tiền thư ở ng theo quy định ; có quyền lưu giữ , trưng bày hiện vật được khen thư ở ng , được kê khai thành tích trong các văn bản , tài liệu của cơ quan , đơn vị . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 8 `[DIEU]`)
- (`e3` theo quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e2` Thông tư này `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 2 . Tập thể được tặng các danh hiệu th i đua , các hình thức khen thưởng được nhận Qu yế t đị nh khen thưởng và hiện vật ( theo quy định tại Thông tư này ) cấp gi ấ y khen , b ằ ng khen , giấy chứng nhận và tiền thư ở ng theo quy định ; có quyền lưu giữ , trưng bày hiện vật được khen thư ở ng , được kê khai thành tích trong các văn bản , tài liệu của cơ quan , đơn vị . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e2` Thông tư này `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #06_2012_TT-BKHĐT_27861#body_context_20 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[06/2012/TT-BKHĐT]`<SO_HIEU>`** ban hành **[ngày 19 tháng 10 năm 2012]`<NGAY_BAN_HANH>`** bởi **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** . **[Điều 11]`<DIEU>`** . **[2 . Đối với chương trình , đề án lớn , các cuộc T ổ ng điều tra , các đơn vị chủ động xây dựng kế hoạch và đ ă ng ký cụ th ể số lượng các hình thức khen thưởng ( cấp Bộ , cấp Nhà nước ) với Vụ Thi đua - Khen thưởng .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **06/2012/TT-BKHĐT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[11:15]`)
- `[e3]` **ngày 19 tháng 10 năm 2012** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 11** → `DIEU` (span: `[16:18]`)
- `[e5]` **2 . Đối với chương trình , đề án lớn , các cuộc T ổ ng điều tra , các đơn vị chủ động xây dựng kế hoạch và đ ă ng ký cụ th ể số lượng các hình thức khen thưởng ( cấp Bộ , cấp Nhà nước ) với Vụ Thi đua - Khen thưởng .** → `KHOAN` (span: `[19:63]`)

**Quan hệ:**
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 19 tháng 10 năm 2012 `[NGAY_BAN_HANH]`)
- (`e4` Điều 11 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`)
- (`e5` 2 . Đối với chương trình , đề án lớn , các cuộc T ổ ng điều tra , các đơn vị chủ động xây dựng kế hoạch và đ ă ng ký cụ th ể số lượng các hình thức khen thưởng ( cấp Bộ , cấp Nhà nước ) với Vụ Thi đua - Khen thưởng . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 11 `[DIEU]`)


---

### Mẫu #06_2012_TT-BKHĐT_27861#body_standalone_21 (Loại: `body_standalone`)
> **[Điều 11]`<DIEU>`** . **[2 . Đối với chương trình , đề án lớn , các cuộc T ổ ng điều tra , các đơn vị chủ động xây dựng kế hoạch và đ ă ng ký cụ th ể số lượng các hình thức khen thưởng ( cấp Bộ , cấp Nhà nước ) với Vụ Thi đua - Khen thưởng .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 11** → `DIEU` (span: `[0:2]`)
- `[e1]` **2 . Đối với chương trình , đề án lớn , các cuộc T ổ ng điều tra , các đơn vị chủ động xây dựng kế hoạch và đ ă ng ký cụ th ể số lượng các hình thức khen thưởng ( cấp Bộ , cấp Nhà nước ) với Vụ Thi đua - Khen thưởng .** → `KHOAN` (span: `[3:47]`)

**Quan hệ:**
- (`e1` 2 . Đối với chương trình , đề án lớn , các cuộc T ổ ng điều tra , các đơn vị chủ động xây dựng kế hoạch và đ ă ng ký cụ th ể số lượng các hình thức khen thưởng ( cấp Bộ , cấp Nhà nước ) với Vụ Thi đua - Khen thưởng . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 11 `[DIEU]`)


---

### Mẫu #06_2012_TT-BKHĐT_27861#body_context_22 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[06/2012/TT-BKHĐT]`<SO_HIEU>`** ban hành **[ngày 19 tháng 10 năm 2012]`<NGAY_BAN_HANH>`** bởi **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** . **[Điều 14]`<DIEU>`** . **[c ) Các cá nhân đ ược c ử đi học , bồi dưỡng ngắn hạn d ư ới 01 năm , nếu đạt kết quả học t ậ p từ loại khá trở lên , chấp hành tốt các quy định của các **[cơ sở đào tạo]`<TO_CHUC_DOANH_NGHIEP>`** , bồi dư ỡ ng thì lấy kết quả học tập với kết quả công tác tại cơ quan , đ ơn vị đ ể bình xét danh hiệu “ Lao động tiên tiến ” . Trường hợp đi học tập , đ ào tạo từ 01 năm tr ở lên , có kết]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **06/2012/TT-BKHĐT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[11:15]`)
- `[e3]` **ngày 19 tháng 10 năm 2012** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 14** → `DIEU` (span: `[16:18]`)
- `[e5]` **c ) Các cá nhân đ ược c ử đi học , bồi dưỡng ngắn hạn d ư ới 01 năm , nếu đạt kết quả học t ậ p từ loại khá trở lên , chấp hành tốt các quy định của các cơ sở đào tạo , bồi dư ỡ ng thì lấy kết quả học tập với kết quả công tác tại cơ quan , đ ơn vị đ ể bình xét danh hiệu “ Lao động tiên tiến ” . Trường hợp đi học tập , đ ào tạo từ 01 năm tr ở lên , có kết** → `DIEM` (span: `[19:101]`)
- `[e6]` **cơ sở đào tạo** → `TO_CHUC_DOANH_NGHIEP` (span: `[56:58]`) *(lồng trong `e5` (`DIEM`))*

**Quan hệ:**
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 19 tháng 10 năm 2012 `[NGAY_BAN_HANH]`)
- (`e4` Điều 14 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`)


---

### Mẫu #06_2012_TT-BKHĐT_27861#body_context_23 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[06/2012/TT-BKHĐT]`<SO_HIEU>`** của **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Khoa học và công nghệ]`<LINH_VUC>`** . **[Điều 14]`<DIEU>`** . **[e ) Không xét danh hiệu “ Lao động tiên tiến ” cho các trường hợp **[không đăng ký thi đua]`<HANH_VI_VI_PHAM>`** ; mới tuyển d ụ ng **[dưới 10 tháng]`<THOI_HAN>`** ; ngh ỉ việc **[từ 40 ngày làm việc trở lên]`<THOI_HAN>`** ; bị xử phạt hành chính ; bị kỷ luật từ khiển trách trở l ê n .]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **06/2012/TT-BKHĐT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[4:8]`)
- `[e3]` **Khoa học và công nghệ** → `LINH_VUC` (span: `[10:13]`)
- `[e4]` **Điều 14** → `DIEU` (span: `[14:16]`)
- `[e5]` **e ) Không xét danh hiệu “ Lao động tiên tiến ” cho các trường hợp không đăng ký thi đua ; mới tuyển d ụ ng dưới 10 tháng ; ngh ỉ việc từ 40 ngày làm việc trở lên ; bị xử phạt hành chính ; bị kỷ luật từ khiển trách trở l ê n .** → `DIEM` (span: `[17:63]`)
- `[e6]` **không đăng ký thi đua** → `HANH_VI_VI_PHAM` (span: `[29:32]`) *(lồng trong `e5` (`DIEM`))*
- `[e7]` **dưới 10 tháng** → `THOI_HAN` (span: `[38:41]`) *(lồng trong `e5` (`DIEM`))*
- `[e8]` **từ 40 ngày làm việc trở lên** → `THOI_HAN` (span: `[45:50]`) *(lồng trong `e5` (`DIEM`))*

**Quan hệ:**
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Khoa học và công nghệ `[LINH_VUC]`)
- (`e4` Điều 14 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`)
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Khoa học và công nghệ `[LINH_VUC]`)
- (`e6` không đăng ký thi đua `[HANH_VI_VI_PHAM]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Khoa học và công nghệ `[LINH_VUC]`)
- (`e6` không đăng ký thi đua `[HANH_VI_VI_PHAM]`) ==[ **TRONG_THOI_HAN** ]==> (`e7` dưới 10 tháng `[THOI_HAN]`)
- (`e6` không đăng ký thi đua `[HANH_VI_VI_PHAM]`) ==[ **TRONG_THOI_HAN** ]==> (`e8` từ 40 ngày làm việc trở lên `[THOI_HAN]`)


---

### Mẫu #06_2012_TT-BKHĐT_27861#body_standalone_24 (Loại: `body_standalone`)
> **[Điều 14]`<DIEU>`** . **[e ) Không xét danh hiệu “ Lao động tiên tiến ” cho các trường hợp **[không đăng ký thi đua]`<HANH_VI_VI_PHAM>`** ; mới tuyển d ụ ng **[dưới 10 tháng]`<THOI_HAN>`** ; ngh ỉ việc **[từ 40 ngày làm việc trở lên]`<THOI_HAN>`** ; bị xử phạt hành chính ; bị kỷ luật từ khiển trách trở l ê n .]`<DIEM>`**

**Thực thể:**
- `[e0]` **Điều 14** → `DIEU` (span: `[0:2]`)
- `[e1]` **e ) Không xét danh hiệu “ Lao động tiên tiến ” cho các trường hợp không đăng ký thi đua ; mới tuyển d ụ ng dưới 10 tháng ; ngh ỉ việc từ 40 ngày làm việc trở lên ; bị xử phạt hành chính ; bị kỷ luật từ khiển trách trở l ê n .** → `DIEM` (span: `[3:49]`)
- `[e2]` **không đăng ký thi đua** → `HANH_VI_VI_PHAM` (span: `[15:18]`) *(lồng trong `e1` (`DIEM`))*
- `[e3]` **dưới 10 tháng** → `THOI_HAN` (span: `[24:27]`) *(lồng trong `e1` (`DIEM`))*
- `[e4]` **từ 40 ngày làm việc trở lên** → `THOI_HAN` (span: `[31:36]`) *(lồng trong `e1` (`DIEM`))*

**Quan hệ:**
- (`e2` không đăng ký thi đua `[HANH_VI_VI_PHAM]`) ==[ **TRONG_THOI_HAN** ]==> (`e3` dưới 10 tháng `[THOI_HAN]`)
- (`e2` không đăng ký thi đua `[HANH_VI_VI_PHAM]`) ==[ **TRONG_THOI_HAN** ]==> (`e4` từ 40 ngày làm việc trở lên `[THOI_HAN]`)


---

### Mẫu #06_2012_TT-BKHĐT_27861#body_context_25 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[06/2012/TT-BKHĐT]`<SO_HIEU>`** của **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Khoa học và công nghệ]`<LINH_VUC>`** . **[Điều 15]`<DIEU>`** . **[Khoản 2]`<KHOAN>`** . **[a ) Ti ê u chuẩn chung - Có cá nhân đạt danh hiệu " Chiến sỹ thi đ ua cơ sở " và không có cá nhân bị kỷ luật từ hình thức c ả nh cáo tr ở lên ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **06/2012/TT-BKHĐT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[4:8]`)
- `[e3]` **Khoa học và công nghệ** → `LINH_VUC` (span: `[10:13]`)
- `[e4]` **Điều 15** → `DIEU` (span: `[14:16]`)
- `[e5]` **Khoản 2** → `KHOAN` (span: `[17:19]`)
- `[e6]` **a ) Ti ê u chuẩn chung - Có cá nhân đạt danh hiệu " Chiến sỹ thi đ ua cơ sở " và không có cá nhân bị kỷ luật từ hình thức c ả nh cáo tr ở lên ;** → `DIEM` (span: `[20:55]`)

**Quan hệ:**
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Khoa học và công nghệ `[LINH_VUC]`)
- (`e4` Điều 15 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`)
- (`e5` Khoản 2 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 15 `[DIEU]`)
- (`e6` a ) Ti ê u chuẩn chung - Có cá nhân đạt danh hiệu " Chiến sỹ thi đ ua cơ sở " và không có cá nhân bị kỷ luật từ hình thức c ả nh cáo tr ở lên ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e5` Khoản 2 `[KHOAN]`)
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Khoa học và công nghệ `[LINH_VUC]`)
- (`e6` a ) Ti ê u chuẩn chung - Có cá nhân đạt danh hiệu " Chiến sỹ thi đ ua cơ sở " và không có cá nhân bị kỷ luật từ hình thức c ả nh cáo tr ở lên ; `[DIEM]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Khoa học và công nghệ `[LINH_VUC]`)


---

### Mẫu #06_2012_TT-BKHĐT_27861#body_context_26 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[06/2012/TT-BKHĐT]`<SO_HIEU>`** ban hành **[ngày 19 tháng 10 năm 2012]`<NGAY_BAN_HANH>`** bởi **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** . **[Điều 17]`<DIEU>`** . **[2 . Hình thức khen thưởng của Bộ :]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **06/2012/TT-BKHĐT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[11:15]`)
- `[e3]` **ngày 19 tháng 10 năm 2012** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 17** → `DIEU` (span: `[16:18]`)
- `[e5]` **2 . Hình thức khen thưởng của Bộ :** → `KHOAN` (span: `[19:26]`)

**Quan hệ:**
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 19 tháng 10 năm 2012 `[NGAY_BAN_HANH]`)
- (`e4` Điều 17 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`)
- (`e5` 2 . Hình thức khen thưởng của Bộ : `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 17 `[DIEU]`)


---

### Mẫu #06_2012_TT-BKHĐT_27861#body_standalone_27 (Loại: `body_standalone`)
> **[Điều 17]`<DIEU>`** . **[2 . Hình thức khen thưởng của Bộ :]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 17** → `DIEU` (span: `[0:2]`)
- `[e1]` **2 . Hình thức khen thưởng của Bộ :** → `KHOAN` (span: `[3:10]`)

**Quan hệ:**
- (`e1` 2 . Hình thức khen thưởng của Bộ : `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 17 `[DIEU]`)


---

### Mẫu #06_2012_TT-BKHĐT_27861#body_context_28 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[06/2012/TT-BKHĐT]`<SO_HIEU>`** ban hành **[ngày 19 tháng 10 năm 2012]`<NGAY_BAN_HANH>`** bởi **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** . **[Điều 17]`<DIEU>`** . **[Khoản 2]`<KHOAN>`** . **[b ) **[Kỷ niệm chương]`<GIAY_TO_HO_SO>`** " Vì sự nghiệp **[ngành Kế hoạch và Đầu tư Việt Nam]`<LINH_VUC>`** ” và **[kỷ niệm chương]`<GIAY_TO_HO_SO>`** " Vì sự nghiệp Th ố ng kê Việt Nam ” .]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **06/2012/TT-BKHĐT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[11:15]`)
- `[e3]` **ngày 19 tháng 10 năm 2012** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 17** → `DIEU` (span: `[16:18]`)
- `[e5]` **Khoản 2** → `KHOAN` (span: `[19:21]`)
- `[e6]` **b ) Kỷ niệm chương " Vì sự nghiệp ngành Kế hoạch và Đầu tư Việt Nam ” và kỷ niệm chương " Vì sự nghiệp Th ố ng kê Việt Nam ” .** → `DIEM` (span: `[22:48]`)
- `[e7]` **ngành Kế hoạch và Đầu tư Việt Nam** → `LINH_VUC` (span: `[29:34]`) *(lồng trong `e6` (`DIEM`))*
- `[e8]` **Kỷ niệm chương** → `GIAY_TO_HO_SO` (span: `[24:26]`) *(lồng trong `e6` (`DIEM`))*
- `[e9]` **kỷ niệm chương** → `GIAY_TO_HO_SO` (span: `[36:38]`) *(lồng trong `e6` (`DIEM`))*

**Quan hệ:**
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 19 tháng 10 năm 2012 `[NGAY_BAN_HANH]`)
- (`e4` Điều 17 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`)
- (`e5` Khoản 2 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 17 `[DIEU]`)
- (`e6` b ) Kỷ niệm chương " Vì sự nghiệp ngành Kế hoạch và Đầu tư Việt Nam ” và kỷ niệm chương " Vì sự nghiệp Th ố ng kê Việt Nam ” . `[DIEM]`) ==[ **THUOC_VE** ]==> (`e5` Khoản 2 `[KHOAN]`)
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e7` ngành Kế hoạch và Đầu tư Việt Nam `[LINH_VUC]`)
- (`e6` b ) Kỷ niệm chương " Vì sự nghiệp ngành Kế hoạch và Đầu tư Việt Nam ” và kỷ niệm chương " Vì sự nghiệp Th ố ng kê Việt Nam ” . `[DIEM]`) ==[ **THUOC_LINH_VUC** ]==> (`e7` ngành Kế hoạch và Đầu tư Việt Nam `[LINH_VUC]`) *(Quan hệ lồng nhau)*


---

### Mẫu #06_2012_TT-BKHĐT_27861#body_standalone_29 (Loại: `body_standalone`)
> **[Điều 17]`<DIEU>`** . **[Khoản 2]`<KHOAN>`** . **[b ) **[Kỷ niệm chương]`<GIAY_TO_HO_SO>`** " Vì sự nghiệp **[ngành Kế hoạch và Đầu tư Việt Nam]`<LINH_VUC>`** ” và **[kỷ niệm chương]`<GIAY_TO_HO_SO>`** " Vì sự nghiệp Th ố ng kê Việt Nam ” .]`<DIEM>`**

**Thực thể:**
- `[e0]` **Điều 17** → `DIEU` (span: `[0:2]`)
- `[e1]` **Khoản 2** → `KHOAN` (span: `[3:5]`)
- `[e2]` **b ) Kỷ niệm chương " Vì sự nghiệp ngành Kế hoạch và Đầu tư Việt Nam ” và kỷ niệm chương " Vì sự nghiệp Th ố ng kê Việt Nam ” .** → `DIEM` (span: `[6:32]`)
- `[e3]` **ngành Kế hoạch và Đầu tư Việt Nam** → `LINH_VUC` (span: `[13:18]`) *(lồng trong `e2` (`DIEM`))*
- `[e4]` **Kỷ niệm chương** → `GIAY_TO_HO_SO` (span: `[8:10]`) *(lồng trong `e2` (`DIEM`))*
- `[e5]` **kỷ niệm chương** → `GIAY_TO_HO_SO` (span: `[20:22]`) *(lồng trong `e2` (`DIEM`))*

**Quan hệ:**
- (`e1` Khoản 2 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 17 `[DIEU]`)
- (`e2` b ) Kỷ niệm chương " Vì sự nghiệp ngành Kế hoạch và Đầu tư Việt Nam ” và kỷ niệm chương " Vì sự nghiệp Th ố ng kê Việt Nam ” . `[DIEM]`) ==[ **THUOC_VE** ]==> (`e1` Khoản 2 `[KHOAN]`)
- (`e2` b ) Kỷ niệm chương " Vì sự nghiệp ngành Kế hoạch và Đầu tư Việt Nam ” và kỷ niệm chương " Vì sự nghiệp Th ố ng kê Việt Nam ” . `[DIEM]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` ngành Kế hoạch và Đầu tư Việt Nam `[LINH_VUC]`) *(Quan hệ lồng nhau)*


---

### Mẫu #06_2012_TT-BKHĐT_27861#body_context_30 (Loại: `body_context`)
> **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[06/2012/TT-BKHĐT]`<SO_HIEU>`** . **[Điều 18 . . Tiêu chu ẩ n các hình thức khen thư ở ng cấp Nhà nước . “ Huân chương Sao vàng ” , “ Huân chương Hồ Chí Minh " , “ H uy chương Hữ u nghị ” , “ Danh hiệu vinh dự Nhà nước ” , “ Giải thưởng Hồ Chí Minh ” , “ Giải thưởng Nhà nước ” , H uân chương lao động ” , “ B ằ ng khen của **[Thủ tướng Chính phủ]`<CO_QUAN_THAM_QUYEN>`** " thực hiện **[theo quy định tại]`<TU_KHOA_PHAP_LY>`** **[Chương III]`<THAM_CHIEU_PHAP_LY>`** Luật Thi đua , Khen thưởng và Chương III **[Nghị định số 42/2010/N]`<THAM_CHIEU_PHAP_LY>`** Đ - CP **[ngày 15 tháng 4 năm 2010]`<NGAY_THAM_CHIEU>`** của **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** quy]`<DIEU>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[5:6]`)
- `[e1]` **06/2012/TT-BKHĐT** → `SO_HIEU` (span: `[7:8]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[0:4]`)
- `[e3]` **Điều 18 . . Tiêu chu ẩ n các hình thức khen thư ở ng cấp Nhà nước . “ Huân chương Sao vàng ” , “ Huân chương Hồ Chí Minh " , “ H uy chương Hữ u nghị ” , “ Danh hiệu vinh dự Nhà nước ” , “ Giải thưởng Hồ Chí Minh ” , “ Giải thưởng Nhà nước ” , H uân chương lao động ” , “ B ằ ng khen của Thủ tướng Chính phủ " thực hiện theo quy định tại Chương III Luật Thi đua , Khen thưởng và Chương III Nghị định số 42/2010/N Đ - CP ngày 15 tháng 4 năm 2010 của Chính phủ quy** → `DIEU` (span: `[9:102]`)
- `[e4]` **Chương III** → `THAM_CHIEU_PHAP_LY` (span: `[78:80]`) *(lồng trong `e3` (`DIEU`))*
- `[e5]` **Nghị định số 42/2010/N** → `THAM_CHIEU_PHAP_LY` (span: `[87:90]`) *(lồng trong `e3` (`DIEU`))*
- `[e6]` **theo quy định tại** → `TU_KHOA_PHAP_LY` (span: `[75:78]`) *(lồng trong `e3` (`DIEU`))*
- `[e7]` **ngày 15 tháng 4 năm 2010** → `NGAY_THAM_CHIEU` (span: `[93:99]`) *(lồng trong `e3` (`DIEU`))*
- `[e8]` **Thủ tướng Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[71:73]`) *(lồng trong `e3` (`DIEU`))*
- `[e9]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[100:101]`) *(lồng trong `e3` (`DIEU`))*

**Quan hệ:**
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 18 . . Tiêu chu ẩ n các hình thức khen thư ở ng cấp Nhà nước . “ Huân chương Sao vàng ” , “ Huân chương Hồ Chí Minh " , “ H uy chương Hữ u nghị ” , “ Danh hiệu vinh dự Nhà nước ” , “ Giải thưởng Hồ Chí Minh ” , “ Giải thưởng Nhà nước ” , H uân chương lao động ” , “ B ằ ng khen của Thủ tướng Chính phủ " thực hiện theo quy định tại Chương III Luật Thi đua , Khen thưởng và Chương III Nghị định số 42/2010/N Đ - CP ngày 15 tháng 4 năm 2010 của Chính phủ quy `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`)
- (`e6` theo quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e4` Chương III `[THAM_CHIEU_PHAP_LY]`)
- (`e3` Điều 18 . . Tiêu chu ẩ n các hình thức khen thư ở ng cấp Nhà nước . “ Huân chương Sao vàng ” , “ Huân chương Hồ Chí Minh " , “ H uy chương Hữ u nghị ” , “ Danh hiệu vinh dự Nhà nước ” , “ Giải thưởng Hồ Chí Minh ” , “ Giải thưởng Nhà nước ” , H uân chương lao động ” , “ B ằ ng khen của Thủ tướng Chính phủ " thực hiện theo quy định tại Chương III Luật Thi đua , Khen thưởng và Chương III Nghị định số 42/2010/N Đ - CP ngày 15 tháng 4 năm 2010 của Chính phủ quy `[DIEU]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e4` Chương III `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e6` theo quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e5` Nghị định số 42/2010/N `[THAM_CHIEU_PHAP_LY]`)
- (`e3` Điều 18 . . Tiêu chu ẩ n các hình thức khen thư ở ng cấp Nhà nước . “ Huân chương Sao vàng ” , “ Huân chương Hồ Chí Minh " , “ H uy chương Hữ u nghị ” , “ Danh hiệu vinh dự Nhà nước ” , “ Giải thưởng Hồ Chí Minh ” , “ Giải thưởng Nhà nước ” , H uân chương lao động ” , “ B ằ ng khen của Thủ tướng Chính phủ " thực hiện theo quy định tại Chương III Luật Thi đua , Khen thưởng và Chương III Nghị định số 42/2010/N Đ - CP ngày 15 tháng 4 năm 2010 của Chính phủ quy `[DIEU]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e5` Nghị định số 42/2010/N `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e5` Nghị định số 42/2010/N `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e7` ngày 15 tháng 4 năm 2010 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #06_2012_TT-BKHĐT_27861#body_standalone_31 (Loại: `body_standalone`)
> **[Điều 18 . . Tiêu chu ẩ n các hình thức khen thư ở ng cấp Nhà nước . “ Huân chương Sao vàng ” , “ Huân chương Hồ Chí Minh " , “ H uy chương Hữ u nghị ” , “ Danh hiệu vinh dự Nhà nước ” , “ Giải thưởng Hồ Chí Minh ” , “ Giải thưởng Nhà nước ” , H uân chương lao động ” , “ B ằ ng khen của **[Thủ tướng Chính phủ]`<CO_QUAN_THAM_QUYEN>`** " thực hiện **[theo quy định tại]`<TU_KHOA_PHAP_LY>`** **[Chương III]`<THAM_CHIEU_PHAP_LY>`** Luật Thi đua , Khen thưởng và Chương III **[Nghị định số 42/2010/N]`<THAM_CHIEU_PHAP_LY>`** Đ - CP **[ngày 15 tháng 4 năm 2010]`<NGAY_THAM_CHIEU>`** của **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** quy]`<DIEU>`**

**Thực thể:**
- `[e0]` **Điều 18 . . Tiêu chu ẩ n các hình thức khen thư ở ng cấp Nhà nước . “ Huân chương Sao vàng ” , “ Huân chương Hồ Chí Minh " , “ H uy chương Hữ u nghị ” , “ Danh hiệu vinh dự Nhà nước ” , “ Giải thưởng Hồ Chí Minh ” , “ Giải thưởng Nhà nước ” , H uân chương lao động ” , “ B ằ ng khen của Thủ tướng Chính phủ " thực hiện theo quy định tại Chương III Luật Thi đua , Khen thưởng và Chương III Nghị định số 42/2010/N Đ - CP ngày 15 tháng 4 năm 2010 của Chính phủ quy** → `DIEU` (span: `[0:93]`)
- `[e1]` **Chương III** → `THAM_CHIEU_PHAP_LY` (span: `[69:71]`) *(lồng trong `e0` (`DIEU`))*
- `[e2]` **Nghị định số 42/2010/N** → `THAM_CHIEU_PHAP_LY` (span: `[78:81]`) *(lồng trong `e0` (`DIEU`))*
- `[e3]` **theo quy định tại** → `TU_KHOA_PHAP_LY` (span: `[66:69]`) *(lồng trong `e0` (`DIEU`))*
- `[e4]` **ngày 15 tháng 4 năm 2010** → `NGAY_THAM_CHIEU` (span: `[84:90]`) *(lồng trong `e0` (`DIEU`))*
- `[e5]` **Thủ tướng Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[62:64]`) *(lồng trong `e0` (`DIEU`))*
- `[e6]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[91:92]`) *(lồng trong `e0` (`DIEU`))*

**Quan hệ:**
- (`e3` theo quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e1` Chương III `[THAM_CHIEU_PHAP_LY]`)
- (`e0` Điều 18 . . Tiêu chu ẩ n các hình thức khen thư ở ng cấp Nhà nước . “ Huân chương Sao vàng ” , “ Huân chương Hồ Chí Minh " , “ H uy chương Hữ u nghị ” , “ Danh hiệu vinh dự Nhà nước ” , “ Giải thưởng Hồ Chí Minh ” , “ Giải thưởng Nhà nước ” , H uân chương lao động ” , “ B ằ ng khen của Thủ tướng Chính phủ " thực hiện theo quy định tại Chương III Luật Thi đua , Khen thưởng và Chương III Nghị định số 42/2010/N Đ - CP ngày 15 tháng 4 năm 2010 của Chính phủ quy `[DIEU]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e1` Chương III `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e3` theo quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e2` Nghị định số 42/2010/N `[THAM_CHIEU_PHAP_LY]`)
- (`e0` Điều 18 . . Tiêu chu ẩ n các hình thức khen thư ở ng cấp Nhà nước . “ Huân chương Sao vàng ” , “ Huân chương Hồ Chí Minh " , “ H uy chương Hữ u nghị ” , “ Danh hiệu vinh dự Nhà nước ” , “ Giải thưởng Hồ Chí Minh ” , “ Giải thưởng Nhà nước ” , H uân chương lao động ” , “ B ằ ng khen của Thủ tướng Chính phủ " thực hiện theo quy định tại Chương III Luật Thi đua , Khen thưởng và Chương III Nghị định số 42/2010/N Đ - CP ngày 15 tháng 4 năm 2010 của Chính phủ quy `[DIEU]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e2` Nghị định số 42/2010/N `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e2` Nghị định số 42/2010/N `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e4` ngày 15 tháng 4 năm 2010 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #06_2012_TT-BKHĐT_27861#body_context_32 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[06/2012/TT-BKHĐT]`<SO_HIEU>`** ban hành **[ngày 19 tháng 10 năm 2012]`<NGAY_BAN_HANH>`** bởi **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** . **[Điều 19]`<DIEU>`** . **[Khoản 1]`<KHOAN>`** . **[đ ) Tặng cho các tập thể , cá nhân thuộc các Hiệp hội , H ội nghề nghiệp tr ự c thuộc Bộ ( về lĩnh vực t ổ chức và lĩnh vực chuyên môn ) đ ã có thành tích xu ấ t sắc đóng góp cho sự nghiệp xây dựng và phát triển của **[ngành Kế hoạch và Đầu tư]`<LINH_VUC>`** .]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **06/2012/TT-BKHĐT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[11:15]`)
- `[e3]` **ngày 19 tháng 10 năm 2012** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 19** → `DIEU` (span: `[16:18]`)
- `[e5]` **Khoản 1** → `KHOAN` (span: `[19:21]`)
- `[e6]` **đ ) Tặng cho các tập thể , cá nhân thuộc các Hiệp hội , H ội nghề nghiệp tr ự c thuộc Bộ ( về lĩnh vực t ổ chức và lĩnh vực chuyên môn ) đ ã có thành tích xu ấ t sắc đóng góp cho sự nghiệp xây dựng và phát triển của ngành Kế hoạch và Đầu tư .** → `DIEM` (span: `[22:71]`)
- `[e7]` **ngành Kế hoạch và Đầu tư** → `LINH_VUC` (span: `[66:70]`) *(lồng trong `e6` (`DIEM`))*

**Quan hệ:**
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 19 tháng 10 năm 2012 `[NGAY_BAN_HANH]`)
- (`e4` Điều 19 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`)
- (`e5` Khoản 1 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 19 `[DIEU]`)
- (`e6` đ ) Tặng cho các tập thể , cá nhân thuộc các Hiệp hội , H ội nghề nghiệp tr ự c thuộc Bộ ( về lĩnh vực t ổ chức và lĩnh vực chuyên môn ) đ ã có thành tích xu ấ t sắc đóng góp cho sự nghiệp xây dựng và phát triển của ngành Kế hoạch và Đầu tư . `[DIEM]`) ==[ **THUOC_VE** ]==> (`e5` Khoản 1 `[KHOAN]`)
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e7` ngành Kế hoạch và Đầu tư `[LINH_VUC]`)
- (`e6` đ ) Tặng cho các tập thể , cá nhân thuộc các Hiệp hội , H ội nghề nghiệp tr ự c thuộc Bộ ( về lĩnh vực t ổ chức và lĩnh vực chuyên môn ) đ ã có thành tích xu ấ t sắc đóng góp cho sự nghiệp xây dựng và phát triển của ngành Kế hoạch và Đầu tư . `[DIEM]`) ==[ **THUOC_LINH_VUC** ]==> (`e7` ngành Kế hoạch và Đầu tư `[LINH_VUC]`) *(Quan hệ lồng nhau)*


---

### Mẫu #06_2012_TT-BKHĐT_27861#body_context_33 (Loại: `body_context`)
> **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[06/2012/TT-BKHĐT]`<SO_HIEU>`** . **[Điều 19]`<DIEU>`** . **[Khoản 1]`<KHOAN>`** . **[e ) Tặng cho các tập thể , cá nhân ngoài **[ngành Kế hoạch và Đầu tư]`<LINH_VUC>`** ( trong và ngoài nước ) có thành tích xuất sắc , đón g góp cho sự nghi ệ p xây dựng và phát triển ngành K ế hoạch và Đầu tư .]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[5:6]`)
- `[e1]` **06/2012/TT-BKHĐT** → `SO_HIEU` (span: `[7:8]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[0:4]`)
- `[e3]` **Điều 19** → `DIEU` (span: `[9:11]`)
- `[e4]` **Khoản 1** → `KHOAN` (span: `[12:14]`)
- `[e5]` **e ) Tặng cho các tập thể , cá nhân ngoài ngành Kế hoạch và Đầu tư ( trong và ngoài nước ) có thành tích xuất sắc , đón g góp cho sự nghi ệ p xây dựng và phát triển ngành K ế hoạch và Đầu tư .** → `DIEM` (span: `[15:56]`)
- `[e6]` **ngành Kế hoạch và Đầu tư** → `LINH_VUC` (span: `[24:28]`) *(lồng trong `e5` (`DIEM`))*

**Quan hệ:**
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 19 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`)
- (`e4` Khoản 1 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 19 `[DIEU]`)
- (`e5` e ) Tặng cho các tập thể , cá nhân ngoài ngành Kế hoạch và Đầu tư ( trong và ngoài nước ) có thành tích xuất sắc , đón g góp cho sự nghi ệ p xây dựng và phát triển ngành K ế hoạch và Đầu tư . `[DIEM]`) ==[ **THUOC_VE** ]==> (`e4` Khoản 1 `[KHOAN]`)
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e6` ngành Kế hoạch và Đầu tư `[LINH_VUC]`)
- (`e5` e ) Tặng cho các tập thể , cá nhân ngoài ngành Kế hoạch và Đầu tư ( trong và ngoài nước ) có thành tích xuất sắc , đón g góp cho sự nghi ệ p xây dựng và phát triển ngành K ế hoạch và Đầu tư . `[DIEM]`) ==[ **THUOC_LINH_VUC** ]==> (`e6` ngành Kế hoạch và Đầu tư `[LINH_VUC]`) *(Quan hệ lồng nhau)*


---

### Mẫu #06_2012_TT-BKHĐT_27861#body_context_34 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[06/2012/TT-BKHĐT]`<SO_HIEU>`** ban hành **[ngày 19 tháng 10 năm 2012]`<NGAY_BAN_HANH>`** bởi **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** . **[Điều 19]`<DIEU>`** . **[3 . Giấy khen của thủ trưởng đơn vị thuộc Bộ ( đã phân cấp ) Tiêu chuẩn Giấy khen của Thủ trưởng cơ quan , đ ơn vị thực hiện theo quy định tại Đ iều 75 Luật Thi đua , Khen t hưởng và Đi ề u 50 N g hị định số 42/2010/NĐ-CP ngày 15 tháng 4 năm 2010 của **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** quy định chi tiết và hướng d ẫn thi hành một số điều của Luật Thi đua , Khen thưởng và Luật sửa đổi , b ổ sung một s ố điều của Luật]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **06/2012/TT-BKHĐT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[11:15]`)
- `[e3]` **ngày 19 tháng 10 năm 2012** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 19** → `DIEU` (span: `[16:18]`)
- `[e5]` **3 . Giấy khen của thủ trưởng đơn vị thuộc Bộ ( đã phân cấp ) Tiêu chuẩn Giấy khen của Thủ trưởng cơ quan , đ ơn vị thực hiện theo quy định tại Đ iều 75 Luật Thi đua , Khen t hưởng và Đi ề u 50 N g hị định số 42/2010/NĐ-CP ngày 15 tháng 4 năm 2010 của Chính phủ quy định chi tiết và hướng d ẫn thi hành một số điều của Luật Thi đua , Khen thưởng và Luật sửa đổi , b ổ sung một s ố điều của Luật** → `KHOAN` (span: `[19:98]`)
- `[e6]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[70:71]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 19 tháng 10 năm 2012 `[NGAY_BAN_HANH]`)
- (`e4` Điều 19 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`)
- (`e5` 3 . Giấy khen của thủ trưởng đơn vị thuộc Bộ ( đã phân cấp ) Tiêu chuẩn Giấy khen của Thủ trưởng cơ quan , đ ơn vị thực hiện theo quy định tại Đ iều 75 Luật Thi đua , Khen t hưởng và Đi ề u 50 N g hị định số 42/2010/NĐ-CP ngày 15 tháng 4 năm 2010 của Chính phủ quy định chi tiết và hướng d ẫn thi hành một số điều của Luật Thi đua , Khen thưởng và Luật sửa đổi , b ổ sung một s ố điều của Luật `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 19 `[DIEU]`)


---

### Mẫu #06_2012_TT-BKHĐT_27861#body_context_35 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[06/2012/TT-BKHĐT]`<SO_HIEU>`** ban hành **[ngày 19 tháng 10 năm 2012]`<NGAY_BAN_HANH>`** bởi **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** . **[Điều 21]`<DIEU>`** . **[5 . Đ ố i với các đơn vị trực thuộc T ổ ng cục Thống kê : Tổ chức họp , bình b ầ u theo Quy chế Thi đua - Khen thưởng của **[ngành Thống kê]`<LINH_VUC>`** . Quyết định các danh hiệu thi đua theo thẩm quyền quy định ; trình Hội đồng Thi đ ua - Khen thưởng Bộ ( qua Vụ Th i đua - Khen thưởng ) xem xét , quyết định đối v ớ i các danh hiệu thi đua và hình thức khen thư ở ng bậc cao .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **06/2012/TT-BKHĐT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[11:15]`)
- `[e3]` **ngày 19 tháng 10 năm 2012** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 21** → `DIEU` (span: `[16:18]`)
- `[e5]` **5 . Đ ố i với các đơn vị trực thuộc T ổ ng cục Thống kê : Tổ chức họp , bình b ầ u theo Quy chế Thi đua - Khen thưởng của ngành Thống kê . Quyết định các danh hiệu thi đua theo thẩm quyền quy định ; trình Hội đồng Thi đ ua - Khen thưởng Bộ ( qua Vụ Th i đua - Khen thưởng ) xem xét , quyết định đối v ớ i các danh hiệu thi đua và hình thức khen thư ở ng bậc cao .** → `KHOAN` (span: `[19:93]`)
- `[e6]` **ngành Thống kê** → `LINH_VUC` (span: `[46:48]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 19 tháng 10 năm 2012 `[NGAY_BAN_HANH]`)
- (`e4` Điều 21 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`)
- (`e5` 5 . Đ ố i với các đơn vị trực thuộc T ổ ng cục Thống kê : Tổ chức họp , bình b ầ u theo Quy chế Thi đua - Khen thưởng của ngành Thống kê . Quyết định các danh hiệu thi đua theo thẩm quyền quy định ; trình Hội đồng Thi đ ua - Khen thưởng Bộ ( qua Vụ Th i đua - Khen thưởng ) xem xét , quyết định đối v ớ i các danh hiệu thi đua và hình thức khen thư ở ng bậc cao . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 21 `[DIEU]`)
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e6` ngành Thống kê `[LINH_VUC]`)
- (`e5` 5 . Đ ố i với các đơn vị trực thuộc T ổ ng cục Thống kê : Tổ chức họp , bình b ầ u theo Quy chế Thi đua - Khen thưởng của ngành Thống kê . Quyết định các danh hiệu thi đua theo thẩm quyền quy định ; trình Hội đồng Thi đ ua - Khen thưởng Bộ ( qua Vụ Th i đua - Khen thưởng ) xem xét , quyết định đối v ớ i các danh hiệu thi đua và hình thức khen thư ở ng bậc cao . `[KHOAN]`) ==[ **THUOC_LINH_VUC** ]==> (`e6` ngành Thống kê `[LINH_VUC]`) *(Quan hệ lồng nhau)*


---

### Mẫu #06_2012_TT-BKHĐT_27861#body_context_36 (Loại: `body_context`)
> **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[06/2012/TT-BKHĐT]`<SO_HIEU>`** . **[Điều 22]`<DIEU>`** . **[1 . Chủ tịch nước và Th ủ tướng **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** quyết định tặng : ' ‘ Huân chương ” , “ Huy chương ” , " Giải thưởng Hồ Chí Minh " , " Giải thư ở ng Nhà nước " , “ Danh hiệu vinh dự Nhà nước ” ; danh hiệu " Cờ thi đua của **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** " , danh hiệu " Chiến sĩ thi đua toàn qu ố c " , " B ằ ng khen c ủ a **[Thủ tướng Chính phủ]`<CO_QUAN_THAM_QUYEN>`** " đ ược thực hi ệ n **[theo quy định tại]`<TU_KHOA_PHAP_LY>`** **[các Điều 77 và 78]`<THAM_CHIEU_PHAP_LY>`** c ủ a Luật Thi đua , Khen thưởng .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[5:6]`)
- `[e1]` **06/2012/TT-BKHĐT** → `SO_HIEU` (span: `[7:8]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[0:4]`)
- `[e3]` **Điều 22** → `DIEU` (span: `[9:11]`)
- `[e4]` **1 . Chủ tịch nước và Th ủ tướng Chính phủ quyết định tặng : ' ‘ Huân chương ” , “ Huy chương ” , " Giải thưởng Hồ Chí Minh " , " Giải thư ở ng Nhà nước " , “ Danh hiệu vinh dự Nhà nước ” ; danh hiệu " Cờ thi đua của Chính phủ " , danh hiệu " Chiến sĩ thi đua toàn qu ố c " , " B ằ ng khen c ủ a Thủ tướng Chính phủ " đ ược thực hi ệ n theo quy định tại các Điều 77 và 78 c ủ a Luật Thi đua , Khen thưởng .** → `KHOAN` (span: `[12:103]`)
- `[e5]` **các Điều 77 và 78** → `THAM_CHIEU_PHAP_LY` (span: `[90:95]`) *(lồng trong `e4` (`KHOAN`))*
- `[e6]` **theo quy định tại** → `TU_KHOA_PHAP_LY` (span: `[87:90]`) *(lồng trong `e4` (`KHOAN`))*
- `[e7]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[20:21]`) *(lồng trong `e4` (`KHOAN`))*
- `[e8]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[57:58]`) *(lồng trong `e4` (`KHOAN`))*
- `[e9]` **Thủ tướng Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[78:80]`) *(lồng trong `e4` (`KHOAN`))*

**Quan hệ:**
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 22 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`)
- (`e4` 1 . Chủ tịch nước và Th ủ tướng Chính phủ quyết định tặng : ' ‘ Huân chương ” , “ Huy chương ” , " Giải thưởng Hồ Chí Minh " , " Giải thư ở ng Nhà nước " , “ Danh hiệu vinh dự Nhà nước ” ; danh hiệu " Cờ thi đua của Chính phủ " , danh hiệu " Chiến sĩ thi đua toàn qu ố c " , " B ằ ng khen c ủ a Thủ tướng Chính phủ " đ ược thực hi ệ n theo quy định tại các Điều 77 và 78 c ủ a Luật Thi đua , Khen thưởng . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 22 `[DIEU]`)
- (`e6` theo quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e5` các Điều 77 và 78 `[THAM_CHIEU_PHAP_LY]`)
- (`e4` 1 . Chủ tịch nước và Th ủ tướng Chính phủ quyết định tặng : ' ‘ Huân chương ” , “ Huy chương ” , " Giải thưởng Hồ Chí Minh " , " Giải thư ở ng Nhà nước " , “ Danh hiệu vinh dự Nhà nước ” ; danh hiệu " Cờ thi đua của Chính phủ " , danh hiệu " Chiến sĩ thi đua toàn qu ố c " , " B ằ ng khen c ủ a Thủ tướng Chính phủ " đ ược thực hi ệ n theo quy định tại các Điều 77 và 78 c ủ a Luật Thi đua , Khen thưởng . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e5` các Điều 77 và 78 `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #06_2012_TT-BKHĐT_27861#body_standalone_37 (Loại: `body_standalone`)
> **[Điều 22]`<DIEU>`** . **[1 . Chủ tịch nước và Th ủ tướng **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** quyết định tặng : ' ‘ Huân chương ” , “ Huy chương ” , " Giải thưởng Hồ Chí Minh " , " Giải thư ở ng Nhà nước " , “ Danh hiệu vinh dự Nhà nước ” ; danh hiệu " Cờ thi đua của **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** " , danh hiệu " Chiến sĩ thi đua toàn qu ố c " , " B ằ ng khen c ủ a **[Thủ tướng Chính phủ]`<CO_QUAN_THAM_QUYEN>`** " đ ược thực hi ệ n **[theo quy định tại]`<TU_KHOA_PHAP_LY>`** **[các Điều 77 và 78]`<THAM_CHIEU_PHAP_LY>`** c ủ a Luật Thi đua , Khen thưởng .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 22** → `DIEU` (span: `[0:2]`)
- `[e1]` **1 . Chủ tịch nước và Th ủ tướng Chính phủ quyết định tặng : ' ‘ Huân chương ” , “ Huy chương ” , " Giải thưởng Hồ Chí Minh " , " Giải thư ở ng Nhà nước " , “ Danh hiệu vinh dự Nhà nước ” ; danh hiệu " Cờ thi đua của Chính phủ " , danh hiệu " Chiến sĩ thi đua toàn qu ố c " , " B ằ ng khen c ủ a Thủ tướng Chính phủ " đ ược thực hi ệ n theo quy định tại các Điều 77 và 78 c ủ a Luật Thi đua , Khen thưởng .** → `KHOAN` (span: `[3:94]`)
- `[e2]` **các Điều 77 và 78** → `THAM_CHIEU_PHAP_LY` (span: `[81:86]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **theo quy định tại** → `TU_KHOA_PHAP_LY` (span: `[78:81]`) *(lồng trong `e1` (`KHOAN`))*
- `[e4]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[11:12]`) *(lồng trong `e1` (`KHOAN`))*
- `[e5]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[48:49]`) *(lồng trong `e1` (`KHOAN`))*
- `[e6]` **Thủ tướng Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[69:71]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 1 . Chủ tịch nước và Th ủ tướng Chính phủ quyết định tặng : ' ‘ Huân chương ” , “ Huy chương ” , " Giải thưởng Hồ Chí Minh " , " Giải thư ở ng Nhà nước " , “ Danh hiệu vinh dự Nhà nước ” ; danh hiệu " Cờ thi đua của Chính phủ " , danh hiệu " Chiến sĩ thi đua toàn qu ố c " , " B ằ ng khen c ủ a Thủ tướng Chính phủ " đ ược thực hi ệ n theo quy định tại các Điều 77 và 78 c ủ a Luật Thi đua , Khen thưởng . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 22 `[DIEU]`)
- (`e3` theo quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e2` các Điều 77 và 78 `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 1 . Chủ tịch nước và Th ủ tướng Chính phủ quyết định tặng : ' ‘ Huân chương ” , “ Huy chương ” , " Giải thưởng Hồ Chí Minh " , " Giải thư ở ng Nhà nước " , “ Danh hiệu vinh dự Nhà nước ” ; danh hiệu " Cờ thi đua của Chính phủ " , danh hiệu " Chiến sĩ thi đua toàn qu ố c " , " B ằ ng khen c ủ a Thủ tướng Chính phủ " đ ược thực hi ệ n theo quy định tại các Điều 77 và 78 c ủ a Luật Thi đua , Khen thưởng . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e2` các Điều 77 và 78 `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #06_2012_TT-BKHĐT_27861#body_context_38 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[06/2012/TT-BKHĐT]`<SO_HIEU>`** của **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Khoa học và công nghệ]`<LINH_VUC>`** . **[Điều 22]`<DIEU>`** . **[Khoản 2]`<KHOAN>`** . **[d ) Tặng danh hiệu “ Cờ thi đua cấp Bộ ” cho các S ở và Ban Quản lý các tỉnh , thành phố trực thuộc Trung ương ; tặng “ B ằ ng khen của Bộ trưởng ” cho các tập thể , cá nhân thuộc các S ở , Ban Quản lý và tặng “ **[Kỷ niệm chương]`<GIAY_TO_HO_SO>`** “ V ì sự nghiệp **[ngành Kế hoạch và Đầu tư Việt Nam]`<LINH_VUC>`** ” cho cá nhân thuộc các S ở , Ban Quản lý .]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **06/2012/TT-BKHĐT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[4:8]`)
- `[e3]` **Khoa học và công nghệ** → `LINH_VUC` (span: `[10:13]`)
- `[e4]` **Điều 22** → `DIEU` (span: `[14:16]`)
- `[e5]` **Khoản 2** → `KHOAN` (span: `[17:19]`)
- `[e6]` **d ) Tặng danh hiệu “ Cờ thi đua cấp Bộ ” cho các S ở và Ban Quản lý các tỉnh , thành phố trực thuộc Trung ương ; tặng “ B ằ ng khen của Bộ trưởng ” cho các tập thể , cá nhân thuộc các S ở , Ban Quản lý và tặng “ Kỷ niệm chương “ V ì sự nghiệp ngành Kế hoạch và Đầu tư Việt Nam ” cho cá nhân thuộc các S ở , Ban Quản lý .** → `DIEM` (span: `[20:90]`)
- `[e7]` **ngành Kế hoạch và Đầu tư Việt Nam** → `LINH_VUC` (span: `[74:79]`) *(lồng trong `e6` (`DIEM`))*
- `[e8]` **Kỷ niệm chương** → `GIAY_TO_HO_SO` (span: `[68:70]`) *(lồng trong `e6` (`DIEM`))*

**Quan hệ:**
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Khoa học và công nghệ `[LINH_VUC]`)
- (`e4` Điều 22 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`)
- (`e5` Khoản 2 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 22 `[DIEU]`)
- (`e6` d ) Tặng danh hiệu “ Cờ thi đua cấp Bộ ” cho các S ở và Ban Quản lý các tỉnh , thành phố trực thuộc Trung ương ; tặng “ B ằ ng khen của Bộ trưởng ” cho các tập thể , cá nhân thuộc các S ở , Ban Quản lý và tặng “ Kỷ niệm chương “ V ì sự nghiệp ngành Kế hoạch và Đầu tư Việt Nam ” cho cá nhân thuộc các S ở , Ban Quản lý . `[DIEM]`) ==[ **THUOC_VE** ]==> (`e5` Khoản 2 `[KHOAN]`)
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Khoa học và công nghệ `[LINH_VUC]`)
- (`e6` d ) Tặng danh hiệu “ Cờ thi đua cấp Bộ ” cho các S ở và Ban Quản lý các tỉnh , thành phố trực thuộc Trung ương ; tặng “ B ằ ng khen của Bộ trưởng ” cho các tập thể , cá nhân thuộc các S ở , Ban Quản lý và tặng “ Kỷ niệm chương “ V ì sự nghiệp ngành Kế hoạch và Đầu tư Việt Nam ” cho cá nhân thuộc các S ở , Ban Quản lý . `[DIEM]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Khoa học và công nghệ `[LINH_VUC]`)
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e7` ngành Kế hoạch và Đầu tư Việt Nam `[LINH_VUC]`)
- (`e6` d ) Tặng danh hiệu “ Cờ thi đua cấp Bộ ” cho các S ở và Ban Quản lý các tỉnh , thành phố trực thuộc Trung ương ; tặng “ B ằ ng khen của Bộ trưởng ” cho các tập thể , cá nhân thuộc các S ở , Ban Quản lý và tặng “ Kỷ niệm chương “ V ì sự nghiệp ngành Kế hoạch và Đầu tư Việt Nam ” cho cá nhân thuộc các S ở , Ban Quản lý . `[DIEM]`) ==[ **THUOC_LINH_VUC** ]==> (`e7` ngành Kế hoạch và Đầu tư Việt Nam `[LINH_VUC]`) *(Quan hệ lồng nhau)*


---

### Mẫu #06_2012_TT-BKHĐT_27861#body_standalone_39 (Loại: `body_standalone`)
> **[Điều 22]`<DIEU>`** . **[Khoản 2]`<KHOAN>`** . **[d ) Tặng danh hiệu “ Cờ thi đua cấp Bộ ” cho các S ở và Ban Quản lý các tỉnh , thành phố trực thuộc Trung ương ; tặng “ B ằ ng khen của Bộ trưởng ” cho các tập thể , cá nhân thuộc các S ở , Ban Quản lý và tặng “ **[Kỷ niệm chương]`<GIAY_TO_HO_SO>`** “ V ì sự nghiệp **[ngành Kế hoạch và Đầu tư Việt Nam]`<LINH_VUC>`** ” cho cá nhân thuộc các S ở , Ban Quản lý .]`<DIEM>`**

**Thực thể:**
- `[e0]` **Điều 22** → `DIEU` (span: `[0:2]`)
- `[e1]` **Khoản 2** → `KHOAN` (span: `[3:5]`)
- `[e2]` **d ) Tặng danh hiệu “ Cờ thi đua cấp Bộ ” cho các S ở và Ban Quản lý các tỉnh , thành phố trực thuộc Trung ương ; tặng “ B ằ ng khen của Bộ trưởng ” cho các tập thể , cá nhân thuộc các S ở , Ban Quản lý và tặng “ Kỷ niệm chương “ V ì sự nghiệp ngành Kế hoạch và Đầu tư Việt Nam ” cho cá nhân thuộc các S ở , Ban Quản lý .** → `DIEM` (span: `[6:76]`)
- `[e3]` **ngành Kế hoạch và Đầu tư Việt Nam** → `LINH_VUC` (span: `[60:65]`) *(lồng trong `e2` (`DIEM`))*
- `[e4]` **Kỷ niệm chương** → `GIAY_TO_HO_SO` (span: `[54:56]`) *(lồng trong `e2` (`DIEM`))*

**Quan hệ:**
- (`e1` Khoản 2 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 22 `[DIEU]`)
- (`e2` d ) Tặng danh hiệu “ Cờ thi đua cấp Bộ ” cho các S ở và Ban Quản lý các tỉnh , thành phố trực thuộc Trung ương ; tặng “ B ằ ng khen của Bộ trưởng ” cho các tập thể , cá nhân thuộc các S ở , Ban Quản lý và tặng “ Kỷ niệm chương “ V ì sự nghiệp ngành Kế hoạch và Đầu tư Việt Nam ” cho cá nhân thuộc các S ở , Ban Quản lý . `[DIEM]`) ==[ **THUOC_VE** ]==> (`e1` Khoản 2 `[KHOAN]`)
- (`e2` d ) Tặng danh hiệu “ Cờ thi đua cấp Bộ ” cho các S ở và Ban Quản lý các tỉnh , thành phố trực thuộc Trung ương ; tặng “ B ằ ng khen của Bộ trưởng ” cho các tập thể , cá nhân thuộc các S ở , Ban Quản lý và tặng “ Kỷ niệm chương “ V ì sự nghiệp ngành Kế hoạch và Đầu tư Việt Nam ” cho cá nhân thuộc các S ở , Ban Quản lý . `[DIEM]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` ngành Kế hoạch và Đầu tư Việt Nam `[LINH_VUC]`) *(Quan hệ lồng nhau)*


---

### Mẫu #06_2012_TT-BKHĐT_27861#body_context_40 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[06/2012/TT-BKHĐT]`<SO_HIEU>`** của **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Khoa học và công nghệ]`<LINH_VUC>`** . **[Điều 23 . . Tổ c h ức trao tặng dan h hiệu thi đua và hình thức khen thưởng]`<DIEU>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **06/2012/TT-BKHĐT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[4:8]`)
- `[e3]` **Khoa học và công nghệ** → `LINH_VUC` (span: `[10:13]`)
- `[e4]` **Điều 23 . . Tổ c h ức trao tặng dan h hiệu thi đua và hình thức khen thưởng** → `DIEU` (span: `[14:29]`)

**Quan hệ:**
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Khoa học và công nghệ `[LINH_VUC]`)
- (`e4` Điều 23 . . Tổ c h ức trao tặng dan h hiệu thi đua và hình thức khen thưởng `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`)
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Khoa học và công nghệ `[LINH_VUC]`)
- (`e4` Điều 23 . . Tổ c h ức trao tặng dan h hiệu thi đua và hình thức khen thưởng `[DIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Khoa học và công nghệ `[LINH_VUC]`)


---

### Mẫu #06_2012_TT-BKHĐT_27861#body_context_41 (Loại: `body_context`)
> **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[06/2012/TT-BKHĐT]`<SO_HIEU>`** . **[Điều 24]`<DIEU>`** . **[Khoản 2]`<KHOAN>`** . **[c ) **[Giám đốc]`<CHU_THE_CA_NHAN>`** các S ở , Trưởng ban các Ban Qu ả n l ý : Trình Hội đồng Thi đua - Khen thưởng Bộ xem xét , quyết định tặng : - **[Kỷ niệm chương]`<GIAY_TO_HO_SO>`** " Vì sự nghiệp **[ngành Kế hoạch và Đầu tư Việt Nam]`<LINH_VUC>`** ” thực hiện theo Thông tư s ố 05/2012/TT-BKHĐT ngày 19 tháng 10 n ă m 2012 c ủ a **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_THAM_QUYEN>`** .]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[5:6]`)
- `[e1]` **06/2012/TT-BKHĐT** → `SO_HIEU` (span: `[7:8]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[0:4]`)
- `[e3]` **Điều 24** → `DIEU` (span: `[9:11]`)
- `[e4]` **Khoản 2** → `KHOAN` (span: `[12:14]`)
- `[e5]` **c ) Giám đốc các S ở , Trưởng ban các Ban Qu ả n l ý : Trình Hội đồng Thi đua - Khen thưởng Bộ xem xét , quyết định tặng : - Kỷ niệm chương " Vì sự nghiệp ngành Kế hoạch và Đầu tư Việt Nam ” thực hiện theo Thông tư s ố 05/2012/TT-BKHĐT ngày 19 tháng 10 n ă m 2012 c ủ a Bộ Kế hoạch và Đầu tư .** → `DIEM` (span: `[15:76]`)
- `[e6]` **ngành Kế hoạch và Đầu tư Việt Nam** → `LINH_VUC` (span: `[48:53]`) *(lồng trong `e5` (`DIEM`))*
- `[e7]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_THAM_QUYEN` (span: `[71:75]`) *(lồng trong `e5` (`DIEM`))*
- `[e8]` **Kỷ niệm chương** → `GIAY_TO_HO_SO` (span: `[43:45]`) *(lồng trong `e5` (`DIEM`))*
- `[e9]` **Giám đốc** → `CHU_THE_CA_NHAN` (span: `[17:18]`) *(lồng trong `e5` (`DIEM`))*

**Quan hệ:**
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 24 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`)
- (`e4` Khoản 2 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 24 `[DIEU]`)
- (`e5` c ) Giám đốc các S ở , Trưởng ban các Ban Qu ả n l ý : Trình Hội đồng Thi đua - Khen thưởng Bộ xem xét , quyết định tặng : - Kỷ niệm chương " Vì sự nghiệp ngành Kế hoạch và Đầu tư Việt Nam ” thực hiện theo Thông tư s ố 05/2012/TT-BKHĐT ngày 19 tháng 10 n ă m 2012 c ủ a Bộ Kế hoạch và Đầu tư . `[DIEM]`) ==[ **THUOC_VE** ]==> (`e4` Khoản 2 `[KHOAN]`)
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e6` ngành Kế hoạch và Đầu tư Việt Nam `[LINH_VUC]`)
- (`e5` c ) Giám đốc các S ở , Trưởng ban các Ban Qu ả n l ý : Trình Hội đồng Thi đua - Khen thưởng Bộ xem xét , quyết định tặng : - Kỷ niệm chương " Vì sự nghiệp ngành Kế hoạch và Đầu tư Việt Nam ” thực hiện theo Thông tư s ố 05/2012/TT-BKHĐT ngày 19 tháng 10 n ă m 2012 c ủ a Bộ Kế hoạch và Đầu tư . `[DIEM]`) ==[ **THUOC_LINH_VUC** ]==> (`e6` ngành Kế hoạch và Đầu tư Việt Nam `[LINH_VUC]`) *(Quan hệ lồng nhau)*


---

### Mẫu #06_2012_TT-BKHĐT_27861#body_standalone_42 (Loại: `body_standalone`)
> **[Điều 24]`<DIEU>`** . **[Khoản 2]`<KHOAN>`** . **[c ) **[Giám đốc]`<CHU_THE_CA_NHAN>`** các S ở , Trưởng ban các Ban Qu ả n l ý : Trình Hội đồng Thi đua - Khen thưởng Bộ xem xét , quyết định tặng : - **[Kỷ niệm chương]`<GIAY_TO_HO_SO>`** " Vì sự nghiệp **[ngành Kế hoạch và Đầu tư Việt Nam]`<LINH_VUC>`** ” thực hiện theo Thông tư s ố 05/2012/TT-BKHĐT ngày 19 tháng 10 n ă m 2012 c ủ a **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_THAM_QUYEN>`** .]`<DIEM>`**

**Thực thể:**
- `[e0]` **Điều 24** → `DIEU` (span: `[0:2]`)
- `[e1]` **Khoản 2** → `KHOAN` (span: `[3:5]`)
- `[e2]` **c ) Giám đốc các S ở , Trưởng ban các Ban Qu ả n l ý : Trình Hội đồng Thi đua - Khen thưởng Bộ xem xét , quyết định tặng : - Kỷ niệm chương " Vì sự nghiệp ngành Kế hoạch và Đầu tư Việt Nam ” thực hiện theo Thông tư s ố 05/2012/TT-BKHĐT ngày 19 tháng 10 n ă m 2012 c ủ a Bộ Kế hoạch và Đầu tư .** → `DIEM` (span: `[6:67]`)
- `[e3]` **ngành Kế hoạch và Đầu tư Việt Nam** → `LINH_VUC` (span: `[39:44]`) *(lồng trong `e2` (`DIEM`))*
- `[e4]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_THAM_QUYEN` (span: `[62:66]`) *(lồng trong `e2` (`DIEM`))*
- `[e5]` **Kỷ niệm chương** → `GIAY_TO_HO_SO` (span: `[34:36]`) *(lồng trong `e2` (`DIEM`))*
- `[e6]` **Giám đốc** → `CHU_THE_CA_NHAN` (span: `[8:9]`) *(lồng trong `e2` (`DIEM`))*

**Quan hệ:**
- (`e1` Khoản 2 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 24 `[DIEU]`)
- (`e2` c ) Giám đốc các S ở , Trưởng ban các Ban Qu ả n l ý : Trình Hội đồng Thi đua - Khen thưởng Bộ xem xét , quyết định tặng : - Kỷ niệm chương " Vì sự nghiệp ngành Kế hoạch và Đầu tư Việt Nam ” thực hiện theo Thông tư s ố 05/2012/TT-BKHĐT ngày 19 tháng 10 n ă m 2012 c ủ a Bộ Kế hoạch và Đầu tư . `[DIEM]`) ==[ **THUOC_VE** ]==> (`e1` Khoản 2 `[KHOAN]`)
- (`e2` c ) Giám đốc các S ở , Trưởng ban các Ban Qu ả n l ý : Trình Hội đồng Thi đua - Khen thưởng Bộ xem xét , quyết định tặng : - Kỷ niệm chương " Vì sự nghiệp ngành Kế hoạch và Đầu tư Việt Nam ” thực hiện theo Thông tư s ố 05/2012/TT-BKHĐT ngày 19 tháng 10 n ă m 2012 c ủ a Bộ Kế hoạch và Đầu tư . `[DIEM]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` ngành Kế hoạch và Đầu tư Việt Nam `[LINH_VUC]`) *(Quan hệ lồng nhau)*


---

### Mẫu #06_2012_TT-BKHĐT_27861#body_context_43 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[06/2012/TT-BKHĐT]`<SO_HIEU>`** ban hành **[ngày 19 tháng 10 năm 2012]`<NGAY_BAN_HANH>`** bởi **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** . **[Điều 24]`<DIEU>`** . **[Khoản 2]`<KHOAN>`** . **[c ) **[Giám đốc]`<CHU_THE_CA_NHAN>`** các S ở , Trưởng ban các Ban Qu ả n l ý : Trình Hội đồng Thi đua - Khen thưởng Bộ xem xét , quyết định tặng : d ) Đối với các **[Doanh nghiệp]`<TO_CHUC_DOANH_NGHIEP>`** ( **[quy định tại]`<TU_KHOA_PHAP_LY>`** **[Điều 2]`<THAM_CHIEU_PHAP_LY>`** , Khoản 2 , Mục c ) : C ấp nào **[quyết định thành lập]`<GIAY_TO_HO_SO>`** , **[cấp **[giấy phép kinh doanh]`<GIAY_TO_HO_SO>`**]`<NGHIA_VU_QUYEN>`** , cấp giấy chứng nh ậ n đ ầ u tư ra nước ngoài hoặc quyết định c ổ ph ầ n hóa cho **[doanh nghiệp]`<TO_CHUC_DOANH_NGHIEP>`** đó thì cấp đó]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **06/2012/TT-BKHĐT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[11:15]`)
- `[e3]` **ngày 19 tháng 10 năm 2012** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 24** → `DIEU` (span: `[16:18]`)
- `[e5]` **Khoản 2** → `KHOAN` (span: `[19:21]`)
- `[e6]` **c ) Giám đốc các S ở , Trưởng ban các Ban Qu ả n l ý : Trình Hội đồng Thi đua - Khen thưởng Bộ xem xét , quyết định tặng : d ) Đối với các Doanh nghiệp ( quy định tại Điều 2 , Khoản 2 , Mục c ) : C ấp nào quyết định thành lập , cấp giấy phép kinh doanh , cấp giấy chứng nh ậ n đ ầ u tư ra nước ngoài hoặc quyết định c ổ ph ầ n hóa cho doanh nghiệp đó thì cấp đó** → `DIEM` (span: `[22:101]`)
- `[e7]` **cấp giấy phép kinh doanh** → `NGHIA_VU_QUYEN` (span: `[72:75]`) *(lồng trong `e6` (`DIEM`))*
- `[e8]` **Điều 2** → `THAM_CHIEU_PHAP_LY` (span: `[57:59]`) *(lồng trong `e6` (`DIEM`))*
- `[e9]` **quy định tại** → `TU_KHOA_PHAP_LY` (span: `[55:57]`) *(lồng trong `e6` (`DIEM`))*
- `[e10]` **quyết định thành lập** → `GIAY_TO_HO_SO` (span: `[69:71]`) *(lồng trong `e6` (`DIEM`))*
- `[e11]` **giấy phép kinh doanh** → `GIAY_TO_HO_SO` (span: `[73:75]`) *(lồng trong `e6` (`DIEM`), `e7` (`NGHIA_VU_QUYEN`))*
- `[e12]` **Doanh nghiệp** → `TO_CHUC_DOANH_NGHIEP` (span: `[53:54]`) *(lồng trong `e6` (`DIEM`))*
- `[e13]` **doanh nghiệp** → `TO_CHUC_DOANH_NGHIEP` (span: `[96:97]`) *(lồng trong `e6` (`DIEM`))*
- `[e14]` **Giám đốc** → `CHU_THE_CA_NHAN` (span: `[24:25]`) *(lồng trong `e6` (`DIEM`))*

**Quan hệ:**
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 19 tháng 10 năm 2012 `[NGAY_BAN_HANH]`)
- (`e4` Điều 24 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`)
- (`e5` Khoản 2 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 24 `[DIEU]`)
- (`e6` c ) Giám đốc các S ở , Trưởng ban các Ban Qu ả n l ý : Trình Hội đồng Thi đua - Khen thưởng Bộ xem xét , quyết định tặng : d ) Đối với các Doanh nghiệp ( quy định tại Điều 2 , Khoản 2 , Mục c ) : C ấp nào quyết định thành lập , cấp giấy phép kinh doanh , cấp giấy chứng nh ậ n đ ầ u tư ra nước ngoài hoặc quyết định c ổ ph ầ n hóa cho doanh nghiệp đó thì cấp đó `[DIEM]`) ==[ **THUOC_VE** ]==> (`e5` Khoản 2 `[KHOAN]`)
- (`e7` cấp giấy phép kinh doanh `[NGHIA_VU_QUYEN]`) ==[ **TAC_DONG_DOI_TUONG** ]==> (`e11` giấy phép kinh doanh `[GIAY_TO_HO_SO]`) *(Quan hệ lồng nhau)*
- (`e12` Doanh nghiệp `[TO_CHUC_DOANH_NGHIEP]`) ==[ **CO_NGHIA_VU_QUYEN** ]==> (`e7` cấp giấy phép kinh doanh `[NGHIA_VU_QUYEN]`)
- (`e7` cấp giấy phép kinh doanh `[NGHIA_VU_QUYEN]`) ==[ **TAC_DONG_CHU_THE** ]==> (`e13` doanh nghiệp `[TO_CHUC_DOANH_NGHIEP]`)
- (`e14` Giám đốc `[CHU_THE_CA_NHAN]`) ==[ **CO_NGHIA_VU_QUYEN** ]==> (`e7` cấp giấy phép kinh doanh `[NGHIA_VU_QUYEN]`)
- (`e9` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e8` Điều 2 `[THAM_CHIEU_PHAP_LY]`)
- (`e7` cấp giấy phép kinh doanh `[NGHIA_VU_QUYEN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e8` Điều 2 `[THAM_CHIEU_PHAP_LY]`)
- (`e7` cấp giấy phép kinh doanh `[NGHIA_VU_QUYEN]`) ==[ **TAC_DONG_DOI_TUONG** ]==> (`e10` quyết định thành lập `[GIAY_TO_HO_SO]`)


---

### Mẫu #06_2012_TT-BKHĐT_27861#body_standalone_44 (Loại: `body_standalone`)
> **[Điều 24]`<DIEU>`** . **[Khoản 2]`<KHOAN>`** . **[c ) **[Giám đốc]`<CHU_THE_CA_NHAN>`** các S ở , Trưởng ban các Ban Qu ả n l ý : Trình Hội đồng Thi đua - Khen thưởng Bộ xem xét , quyết định tặng : d ) Đối với các **[Doanh nghiệp]`<TO_CHUC_DOANH_NGHIEP>`** ( **[quy định tại]`<TU_KHOA_PHAP_LY>`** **[Điều 2]`<THAM_CHIEU_PHAP_LY>`** , Khoản 2 , Mục c ) : C ấp nào **[quyết định thành lập]`<GIAY_TO_HO_SO>`** , **[cấp **[giấy phép kinh doanh]`<GIAY_TO_HO_SO>`**]`<NGHIA_VU_QUYEN>`** , cấp giấy chứng nh ậ n đ ầ u tư ra nước ngoài hoặc quyết định c ổ ph ầ n hóa cho **[doanh nghiệp]`<TO_CHUC_DOANH_NGHIEP>`** đó thì cấp đó]`<DIEM>`**

**Thực thể:**
- `[e0]` **Điều 24** → `DIEU` (span: `[0:2]`)
- `[e1]` **Khoản 2** → `KHOAN` (span: `[3:5]`)
- `[e2]` **c ) Giám đốc các S ở , Trưởng ban các Ban Qu ả n l ý : Trình Hội đồng Thi đua - Khen thưởng Bộ xem xét , quyết định tặng : d ) Đối với các Doanh nghiệp ( quy định tại Điều 2 , Khoản 2 , Mục c ) : C ấp nào quyết định thành lập , cấp giấy phép kinh doanh , cấp giấy chứng nh ậ n đ ầ u tư ra nước ngoài hoặc quyết định c ổ ph ầ n hóa cho doanh nghiệp đó thì cấp đó** → `DIEM` (span: `[6:85]`)
- `[e3]` **cấp giấy phép kinh doanh** → `NGHIA_VU_QUYEN` (span: `[56:59]`) *(lồng trong `e2` (`DIEM`))*
- `[e4]` **Điều 2** → `THAM_CHIEU_PHAP_LY` (span: `[41:43]`) *(lồng trong `e2` (`DIEM`))*
- `[e5]` **quy định tại** → `TU_KHOA_PHAP_LY` (span: `[39:41]`) *(lồng trong `e2` (`DIEM`))*
- `[e6]` **quyết định thành lập** → `GIAY_TO_HO_SO` (span: `[53:55]`) *(lồng trong `e2` (`DIEM`))*
- `[e7]` **giấy phép kinh doanh** → `GIAY_TO_HO_SO` (span: `[57:59]`) *(lồng trong `e2` (`DIEM`), `e3` (`NGHIA_VU_QUYEN`))*
- `[e8]` **Doanh nghiệp** → `TO_CHUC_DOANH_NGHIEP` (span: `[37:38]`) *(lồng trong `e2` (`DIEM`))*
- `[e9]` **doanh nghiệp** → `TO_CHUC_DOANH_NGHIEP` (span: `[80:81]`) *(lồng trong `e2` (`DIEM`))*
- `[e10]` **Giám đốc** → `CHU_THE_CA_NHAN` (span: `[8:9]`) *(lồng trong `e2` (`DIEM`))*

**Quan hệ:**
- (`e1` Khoản 2 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 24 `[DIEU]`)
- (`e2` c ) Giám đốc các S ở , Trưởng ban các Ban Qu ả n l ý : Trình Hội đồng Thi đua - Khen thưởng Bộ xem xét , quyết định tặng : d ) Đối với các Doanh nghiệp ( quy định tại Điều 2 , Khoản 2 , Mục c ) : C ấp nào quyết định thành lập , cấp giấy phép kinh doanh , cấp giấy chứng nh ậ n đ ầ u tư ra nước ngoài hoặc quyết định c ổ ph ầ n hóa cho doanh nghiệp đó thì cấp đó `[DIEM]`) ==[ **THUOC_VE** ]==> (`e1` Khoản 2 `[KHOAN]`)
- (`e3` cấp giấy phép kinh doanh `[NGHIA_VU_QUYEN]`) ==[ **TAC_DONG_DOI_TUONG** ]==> (`e7` giấy phép kinh doanh `[GIAY_TO_HO_SO]`) *(Quan hệ lồng nhau)*
- (`e8` Doanh nghiệp `[TO_CHUC_DOANH_NGHIEP]`) ==[ **CO_NGHIA_VU_QUYEN** ]==> (`e3` cấp giấy phép kinh doanh `[NGHIA_VU_QUYEN]`)
- (`e3` cấp giấy phép kinh doanh `[NGHIA_VU_QUYEN]`) ==[ **TAC_DONG_CHU_THE** ]==> (`e9` doanh nghiệp `[TO_CHUC_DOANH_NGHIEP]`)
- (`e10` Giám đốc `[CHU_THE_CA_NHAN]`) ==[ **CO_NGHIA_VU_QUYEN** ]==> (`e3` cấp giấy phép kinh doanh `[NGHIA_VU_QUYEN]`)
- (`e5` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e4` Điều 2 `[THAM_CHIEU_PHAP_LY]`)
- (`e3` cấp giấy phép kinh doanh `[NGHIA_VU_QUYEN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e4` Điều 2 `[THAM_CHIEU_PHAP_LY]`)
- (`e3` cấp giấy phép kinh doanh `[NGHIA_VU_QUYEN]`) ==[ **TAC_DONG_DOI_TUONG** ]==> (`e6` quyết định thành lập `[GIAY_TO_HO_SO]`)


---

### Mẫu #06_2012_TT-BKHĐT_27861#body_context_45 (Loại: `body_context`)
> **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[06/2012/TT-BKHĐT]`<SO_HIEU>`** . **[Điều 25]`<DIEU>`** . **[Khoản 1]`<KHOAN>`** . **[a ) Các đơn vị thuộc Bộ ( không phân cấp ) : **[Lập **[hồ sơ đề nghị khen thưởng]`<GIAY_TO_HO_SO>`**]`<NGHIA_VU_QUYEN>`** cho tập thể , cá nhân thuộc đ ơn vị gửi về Vụ Thi đua - Khen thư ở ng ( theo đ ú ng **[mẫu v]`<THAM_CHIEU_PHAP_LY>`** à thời gian qu y định ) .]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[5:6]`)
- `[e1]` **06/2012/TT-BKHĐT** → `SO_HIEU` (span: `[7:8]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[0:4]`)
- `[e3]` **Điều 25** → `DIEU` (span: `[9:11]`)
- `[e4]` **Khoản 1** → `KHOAN` (span: `[12:14]`)
- `[e5]` **a ) Các đơn vị thuộc Bộ ( không phân cấp ) : Lập hồ sơ đề nghị khen thưởng cho tập thể , cá nhân thuộc đ ơn vị gửi về Vụ Thi đua - Khen thư ở ng ( theo đ ú ng mẫu v à thời gian qu y định ) .** → `DIEM` (span: `[15:61]`)
- `[e6]` **Lập hồ sơ đề nghị khen thưởng** → `NGHIA_VU_QUYEN` (span: `[26:30]`) *(lồng trong `e5` (`DIEM`))*
- `[e7]` **mẫu v** → `THAM_CHIEU_PHAP_LY` (span: `[52:54]`) *(lồng trong `e5` (`DIEM`))*
- `[e8]` **hồ sơ đề nghị khen thưởng** → `GIAY_TO_HO_SO` (span: `[27:30]`) *(lồng trong `e5` (`DIEM`), `e6` (`NGHIA_VU_QUYEN`))*

**Quan hệ:**
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 25 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`)
- (`e4` Khoản 1 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 25 `[DIEU]`)
- (`e5` a ) Các đơn vị thuộc Bộ ( không phân cấp ) : Lập hồ sơ đề nghị khen thưởng cho tập thể , cá nhân thuộc đ ơn vị gửi về Vụ Thi đua - Khen thư ở ng ( theo đ ú ng mẫu v à thời gian qu y định ) . `[DIEM]`) ==[ **THUOC_VE** ]==> (`e4` Khoản 1 `[KHOAN]`)
- (`e6` Lập hồ sơ đề nghị khen thưởng `[NGHIA_VU_QUYEN]`) ==[ **TAC_DONG_DOI_TUONG** ]==> (`e8` hồ sơ đề nghị khen thưởng `[GIAY_TO_HO_SO]`) *(Quan hệ lồng nhau)*
- (`e6` Lập hồ sơ đề nghị khen thưởng `[NGHIA_VU_QUYEN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e7` mẫu v `[THAM_CHIEU_PHAP_LY]`)


---

### Mẫu #06_2012_TT-BKHĐT_27861#body_standalone_46 (Loại: `body_standalone`)
> **[Điều 25]`<DIEU>`** . **[Khoản 1]`<KHOAN>`** . **[a ) Các đơn vị thuộc Bộ ( không phân cấp ) : **[Lập **[hồ sơ đề nghị khen thưởng]`<GIAY_TO_HO_SO>`**]`<NGHIA_VU_QUYEN>`** cho tập thể , cá nhân thuộc đ ơn vị gửi về Vụ Thi đua - Khen thư ở ng ( theo đ ú ng **[mẫu v]`<THAM_CHIEU_PHAP_LY>`** à thời gian qu y định ) .]`<DIEM>`**

**Thực thể:**
- `[e0]` **Điều 25** → `DIEU` (span: `[0:2]`)
- `[e1]` **Khoản 1** → `KHOAN` (span: `[3:5]`)
- `[e2]` **a ) Các đơn vị thuộc Bộ ( không phân cấp ) : Lập hồ sơ đề nghị khen thưởng cho tập thể , cá nhân thuộc đ ơn vị gửi về Vụ Thi đua - Khen thư ở ng ( theo đ ú ng mẫu v à thời gian qu y định ) .** → `DIEM` (span: `[6:52]`)
- `[e3]` **Lập hồ sơ đề nghị khen thưởng** → `NGHIA_VU_QUYEN` (span: `[17:21]`) *(lồng trong `e2` (`DIEM`))*
- `[e4]` **mẫu v** → `THAM_CHIEU_PHAP_LY` (span: `[43:45]`) *(lồng trong `e2` (`DIEM`))*
- `[e5]` **hồ sơ đề nghị khen thưởng** → `GIAY_TO_HO_SO` (span: `[18:21]`) *(lồng trong `e2` (`DIEM`), `e3` (`NGHIA_VU_QUYEN`))*

**Quan hệ:**
- (`e1` Khoản 1 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 25 `[DIEU]`)
- (`e2` a ) Các đơn vị thuộc Bộ ( không phân cấp ) : Lập hồ sơ đề nghị khen thưởng cho tập thể , cá nhân thuộc đ ơn vị gửi về Vụ Thi đua - Khen thư ở ng ( theo đ ú ng mẫu v à thời gian qu y định ) . `[DIEM]`) ==[ **THUOC_VE** ]==> (`e1` Khoản 1 `[KHOAN]`)
- (`e3` Lập hồ sơ đề nghị khen thưởng `[NGHIA_VU_QUYEN]`) ==[ **TAC_DONG_DOI_TUONG** ]==> (`e5` hồ sơ đề nghị khen thưởng `[GIAY_TO_HO_SO]`) *(Quan hệ lồng nhau)*
- (`e3` Lập hồ sơ đề nghị khen thưởng `[NGHIA_VU_QUYEN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e4` mẫu v `[THAM_CHIEU_PHAP_LY]`)


---

### Mẫu #06_2012_TT-BKHĐT_27861#body_context_47 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[06/2012/TT-BKHĐT]`<SO_HIEU>`** của **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Khoa học và công nghệ]`<LINH_VUC>`** . **[Điều 25]`<DIEU>`** . **[Khoản 1]`<KHOAN>`** . **[b ) Các đơn vị thuộc Bộ ( đ ã phân c ấ p ) : - **[Lập **[hồ sơ đề nghị khen thưởng]`<GIAY_TO_HO_SO>`**]`<NGHIA_VU_QUYEN>`** ( từ c ấ p Bộ trở l ê n ) cho t ập th ể , cá nhân thuộc đ ơn vị gửi về Vụ Th i đua - Khen thưởng theo đúng **[mẫu v]`<THAM_CHIEU_PHAP_LY>`** à th ờ i gian quy định .]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **06/2012/TT-BKHĐT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[4:8]`)
- `[e3]` **Khoa học và công nghệ** → `LINH_VUC` (span: `[10:13]`)
- `[e4]` **Điều 25** → `DIEU` (span: `[14:16]`)
- `[e5]` **Khoản 1** → `KHOAN` (span: `[17:19]`)
- `[e6]` **b ) Các đơn vị thuộc Bộ ( đ ã phân c ấ p ) : - Lập hồ sơ đề nghị khen thưởng ( từ c ấ p Bộ trở l ê n ) cho t ập th ể , cá nhân thuộc đ ơn vị gửi về Vụ Th i đua - Khen thưởng theo đúng mẫu v à th ờ i gian quy định .** → `DIEM` (span: `[20:80]`)
- `[e7]` **Lập hồ sơ đề nghị khen thưởng** → `NGHIA_VU_QUYEN` (span: `[36:40]`) *(lồng trong `e6` (`DIEM`))*
- `[e8]` **mẫu v** → `THAM_CHIEU_PHAP_LY` (span: `[71:73]`) *(lồng trong `e6` (`DIEM`))*
- `[e9]` **hồ sơ đề nghị khen thưởng** → `GIAY_TO_HO_SO` (span: `[37:40]`) *(lồng trong `e6` (`DIEM`), `e7` (`NGHIA_VU_QUYEN`))*

**Quan hệ:**
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Khoa học và công nghệ `[LINH_VUC]`)
- (`e4` Điều 25 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`)
- (`e5` Khoản 1 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 25 `[DIEU]`)
- (`e6` b ) Các đơn vị thuộc Bộ ( đ ã phân c ấ p ) : - Lập hồ sơ đề nghị khen thưởng ( từ c ấ p Bộ trở l ê n ) cho t ập th ể , cá nhân thuộc đ ơn vị gửi về Vụ Th i đua - Khen thưởng theo đúng mẫu v à th ờ i gian quy định . `[DIEM]`) ==[ **THUOC_VE** ]==> (`e5` Khoản 1 `[KHOAN]`)
- (`e7` Lập hồ sơ đề nghị khen thưởng `[NGHIA_VU_QUYEN]`) ==[ **TAC_DONG_DOI_TUONG** ]==> (`e9` hồ sơ đề nghị khen thưởng `[GIAY_TO_HO_SO]`) *(Quan hệ lồng nhau)*
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Khoa học và công nghệ `[LINH_VUC]`)
- (`e7` Lập hồ sơ đề nghị khen thưởng `[NGHIA_VU_QUYEN]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Khoa học và công nghệ `[LINH_VUC]`)
- (`e7` Lập hồ sơ đề nghị khen thưởng `[NGHIA_VU_QUYEN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e8` mẫu v `[THAM_CHIEU_PHAP_LY]`)


---

### Mẫu #06_2012_TT-BKHĐT_27861#body_standalone_48 (Loại: `body_standalone`)
> **[Điều 25]`<DIEU>`** . **[Khoản 1]`<KHOAN>`** . **[b ) Các đơn vị thuộc Bộ ( đ ã phân c ấ p ) : - **[Lập **[hồ sơ đề nghị khen thưởng]`<GIAY_TO_HO_SO>`**]`<NGHIA_VU_QUYEN>`** ( từ c ấ p Bộ trở l ê n ) cho t ập th ể , cá nhân thuộc đ ơn vị gửi về Vụ Th i đua - Khen thưởng theo đúng **[mẫu v]`<THAM_CHIEU_PHAP_LY>`** à th ờ i gian quy định .]`<DIEM>`**

**Thực thể:**
- `[e0]` **Điều 25** → `DIEU` (span: `[0:2]`)
- `[e1]` **Khoản 1** → `KHOAN` (span: `[3:5]`)
- `[e2]` **b ) Các đơn vị thuộc Bộ ( đ ã phân c ấ p ) : - Lập hồ sơ đề nghị khen thưởng ( từ c ấ p Bộ trở l ê n ) cho t ập th ể , cá nhân thuộc đ ơn vị gửi về Vụ Th i đua - Khen thưởng theo đúng mẫu v à th ờ i gian quy định .** → `DIEM` (span: `[6:66]`)
- `[e3]` **Lập hồ sơ đề nghị khen thưởng** → `NGHIA_VU_QUYEN` (span: `[22:26]`) *(lồng trong `e2` (`DIEM`))*
- `[e4]` **mẫu v** → `THAM_CHIEU_PHAP_LY` (span: `[57:59]`) *(lồng trong `e2` (`DIEM`))*
- `[e5]` **hồ sơ đề nghị khen thưởng** → `GIAY_TO_HO_SO` (span: `[23:26]`) *(lồng trong `e2` (`DIEM`), `e3` (`NGHIA_VU_QUYEN`))*

**Quan hệ:**
- (`e1` Khoản 1 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 25 `[DIEU]`)
- (`e2` b ) Các đơn vị thuộc Bộ ( đ ã phân c ấ p ) : - Lập hồ sơ đề nghị khen thưởng ( từ c ấ p Bộ trở l ê n ) cho t ập th ể , cá nhân thuộc đ ơn vị gửi về Vụ Th i đua - Khen thưởng theo đúng mẫu v à th ờ i gian quy định . `[DIEM]`) ==[ **THUOC_VE** ]==> (`e1` Khoản 1 `[KHOAN]`)
- (`e3` Lập hồ sơ đề nghị khen thưởng `[NGHIA_VU_QUYEN]`) ==[ **TAC_DONG_DOI_TUONG** ]==> (`e5` hồ sơ đề nghị khen thưởng `[GIAY_TO_HO_SO]`) *(Quan hệ lồng nhau)*
- (`e3` Lập hồ sơ đề nghị khen thưởng `[NGHIA_VU_QUYEN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e4` mẫu v `[THAM_CHIEU_PHAP_LY]`)


---

### Mẫu #06_2012_TT-BKHĐT_27861#body_context_49 (Loại: `body_context`)
> **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[06/2012/TT-BKHĐT]`<SO_HIEU>`** . **[Điều 25]`<DIEU>`** . **[Khoản 1]`<KHOAN>`** . **[c ) Khối Sở , Ban Quản lý : **[Lập **[hồ sơ đề nghị khen thưởng]`<GIAY_TO_HO_SO>`**]`<NGHIA_VU_QUYEN>`** cho tập th ể , cá nhân thuộc đ ơn vị gửi về Vụ Thi đua - Khen thưởng theo đúng **[mẫu v]`<THAM_CHIEU_PHAP_LY>`** à thời gian quy định .]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[5:6]`)
- `[e1]` **06/2012/TT-BKHĐT** → `SO_HIEU` (span: `[7:8]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[0:4]`)
- `[e3]` **Điều 25** → `DIEU` (span: `[9:11]`)
- `[e4]` **Khoản 1** → `KHOAN` (span: `[12:14]`)
- `[e5]` **c ) Khối Sở , Ban Quản lý : Lập hồ sơ đề nghị khen thưởng cho tập th ể , cá nhân thuộc đ ơn vị gửi về Vụ Thi đua - Khen thưởng theo đúng mẫu v à thời gian quy định .** → `DIEM` (span: `[15:50]`)
- `[e6]` **Lập hồ sơ đề nghị khen thưởng** → `NGHIA_VU_QUYEN` (span: `[22:26]`) *(lồng trong `e5` (`DIEM`))*
- `[e7]` **mẫu v** → `THAM_CHIEU_PHAP_LY` (span: `[44:46]`) *(lồng trong `e5` (`DIEM`))*
- `[e8]` **hồ sơ đề nghị khen thưởng** → `GIAY_TO_HO_SO` (span: `[23:26]`) *(lồng trong `e5` (`DIEM`), `e6` (`NGHIA_VU_QUYEN`))*

**Quan hệ:**
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 25 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`)
- (`e4` Khoản 1 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 25 `[DIEU]`)
- (`e5` c ) Khối Sở , Ban Quản lý : Lập hồ sơ đề nghị khen thưởng cho tập th ể , cá nhân thuộc đ ơn vị gửi về Vụ Thi đua - Khen thưởng theo đúng mẫu v à thời gian quy định . `[DIEM]`) ==[ **THUOC_VE** ]==> (`e4` Khoản 1 `[KHOAN]`)
- (`e6` Lập hồ sơ đề nghị khen thưởng `[NGHIA_VU_QUYEN]`) ==[ **TAC_DONG_DOI_TUONG** ]==> (`e8` hồ sơ đề nghị khen thưởng `[GIAY_TO_HO_SO]`) *(Quan hệ lồng nhau)*
- (`e6` Lập hồ sơ đề nghị khen thưởng `[NGHIA_VU_QUYEN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e7` mẫu v `[THAM_CHIEU_PHAP_LY]`)


---

### Mẫu #06_2012_TT-BKHĐT_27861#body_standalone_50 (Loại: `body_standalone`)
> **[Điều 25]`<DIEU>`** . **[Khoản 1]`<KHOAN>`** . **[c ) Khối Sở , Ban Quản lý : **[Lập **[hồ sơ đề nghị khen thưởng]`<GIAY_TO_HO_SO>`**]`<NGHIA_VU_QUYEN>`** cho tập th ể , cá nhân thuộc đ ơn vị gửi về Vụ Thi đua - Khen thưởng theo đúng **[mẫu v]`<THAM_CHIEU_PHAP_LY>`** à thời gian quy định .]`<DIEM>`**

**Thực thể:**
- `[e0]` **Điều 25** → `DIEU` (span: `[0:2]`)
- `[e1]` **Khoản 1** → `KHOAN` (span: `[3:5]`)
- `[e2]` **c ) Khối Sở , Ban Quản lý : Lập hồ sơ đề nghị khen thưởng cho tập th ể , cá nhân thuộc đ ơn vị gửi về Vụ Thi đua - Khen thưởng theo đúng mẫu v à thời gian quy định .** → `DIEM` (span: `[6:41]`)
- `[e3]` **Lập hồ sơ đề nghị khen thưởng** → `NGHIA_VU_QUYEN` (span: `[13:17]`) *(lồng trong `e2` (`DIEM`))*
- `[e4]` **mẫu v** → `THAM_CHIEU_PHAP_LY` (span: `[35:37]`) *(lồng trong `e2` (`DIEM`))*
- `[e5]` **hồ sơ đề nghị khen thưởng** → `GIAY_TO_HO_SO` (span: `[14:17]`) *(lồng trong `e2` (`DIEM`), `e3` (`NGHIA_VU_QUYEN`))*

**Quan hệ:**
- (`e1` Khoản 1 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 25 `[DIEU]`)
- (`e2` c ) Khối Sở , Ban Quản lý : Lập hồ sơ đề nghị khen thưởng cho tập th ể , cá nhân thuộc đ ơn vị gửi về Vụ Thi đua - Khen thưởng theo đúng mẫu v à thời gian quy định . `[DIEM]`) ==[ **THUOC_VE** ]==> (`e1` Khoản 1 `[KHOAN]`)
- (`e3` Lập hồ sơ đề nghị khen thưởng `[NGHIA_VU_QUYEN]`) ==[ **TAC_DONG_DOI_TUONG** ]==> (`e5` hồ sơ đề nghị khen thưởng `[GIAY_TO_HO_SO]`) *(Quan hệ lồng nhau)*
- (`e3` Lập hồ sơ đề nghị khen thưởng `[NGHIA_VU_QUYEN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e4` mẫu v `[THAM_CHIEU_PHAP_LY]`)


---

### Mẫu #06_2012_TT-BKHĐT_27861#body_context_51 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[06/2012/TT-BKHĐT]`<SO_HIEU>`** ban hành **[ngày 19 tháng 10 năm 2012]`<NGAY_BAN_HANH>`** bởi **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** . **[Điều 25]`<DIEU>`** . **[Khoản 2]`<KHOAN>`** . **[đ ) **[Trong thời hạn 10 ngày làm việc]`<THOI_HAN>`** k ể từ ngày k ý quyết định khen thưởng thuộc th ẩ m quy ề n của B ộ trưởng và nhận được Quyết định khen thưởng của các c ấ p có thẩm quyền , Vụ Thi đua - Khen thưởng ph ố i h ợ p với các đ ơn vị liên quan c ó trách nhiệm thông báo quyết định khen thưởng trên “ Cổng Thông tin điện tử ” của **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_THAM_QUYEN>`** .]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **06/2012/TT-BKHĐT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[11:15]`)
- `[e3]` **ngày 19 tháng 10 năm 2012** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 25** → `DIEU` (span: `[16:18]`)
- `[e5]` **Khoản 2** → `KHOAN` (span: `[19:21]`)
- `[e6]` **đ ) Trong thời hạn 10 ngày làm việc k ể từ ngày k ý quyết định khen thưởng thuộc th ẩ m quy ề n của B ộ trưởng và nhận được Quyết định khen thưởng của các c ấ p có thẩm quyền , Vụ Thi đua - Khen thưởng ph ố i h ợ p với các đ ơn vị liên quan c ó trách nhiệm thông báo quyết định khen thưởng trên “ Cổng Thông tin điện tử ” của Bộ Kế hoạch và Đầu tư .** → `DIEM` (span: `[22:95]`)
- `[e7]` **Trong thời hạn 10 ngày làm việc** → `THOI_HAN` (span: `[24:29]`) *(lồng trong `e6` (`DIEM`))*
- `[e8]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_THAM_QUYEN` (span: `[90:94]`) *(lồng trong `e6` (`DIEM`))*

**Quan hệ:**
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 19 tháng 10 năm 2012 `[NGAY_BAN_HANH]`)
- (`e4` Điều 25 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`)
- (`e5` Khoản 2 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 25 `[DIEU]`)
- (`e6` đ ) Trong thời hạn 10 ngày làm việc k ể từ ngày k ý quyết định khen thưởng thuộc th ẩ m quy ề n của B ộ trưởng và nhận được Quyết định khen thưởng của các c ấ p có thẩm quyền , Vụ Thi đua - Khen thưởng ph ố i h ợ p với các đ ơn vị liên quan c ó trách nhiệm thông báo quyết định khen thưởng trên “ Cổng Thông tin điện tử ” của Bộ Kế hoạch và Đầu tư . `[DIEM]`) ==[ **THUOC_VE** ]==> (`e5` Khoản 2 `[KHOAN]`)


---

### Mẫu #06_2012_TT-BKHĐT_27861#body_standalone_52 (Loại: `body_standalone`)
> **[Điều 25]`<DIEU>`** . **[Khoản 2]`<KHOAN>`** . **[đ ) **[Trong thời hạn 10 ngày làm việc]`<THOI_HAN>`** k ể từ ngày k ý quyết định khen thưởng thuộc th ẩ m quy ề n của B ộ trưởng và nhận được Quyết định khen thưởng của các c ấ p có thẩm quyền , Vụ Thi đua - Khen thưởng ph ố i h ợ p với các đ ơn vị liên quan c ó trách nhiệm thông báo quyết định khen thưởng trên “ Cổng Thông tin điện tử ” của **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_THAM_QUYEN>`** .]`<DIEM>`**

**Thực thể:**
- `[e0]` **Điều 25** → `DIEU` (span: `[0:2]`)
- `[e1]` **Khoản 2** → `KHOAN` (span: `[3:5]`)
- `[e2]` **đ ) Trong thời hạn 10 ngày làm việc k ể từ ngày k ý quyết định khen thưởng thuộc th ẩ m quy ề n của B ộ trưởng và nhận được Quyết định khen thưởng của các c ấ p có thẩm quyền , Vụ Thi đua - Khen thưởng ph ố i h ợ p với các đ ơn vị liên quan c ó trách nhiệm thông báo quyết định khen thưởng trên “ Cổng Thông tin điện tử ” của Bộ Kế hoạch và Đầu tư .** → `DIEM` (span: `[6:79]`)
- `[e3]` **Trong thời hạn 10 ngày làm việc** → `THOI_HAN` (span: `[8:13]`) *(lồng trong `e2` (`DIEM`))*
- `[e4]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_THAM_QUYEN` (span: `[74:78]`) *(lồng trong `e2` (`DIEM`))*

**Quan hệ:**
- (`e1` Khoản 2 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 25 `[DIEU]`)
- (`e2` đ ) Trong thời hạn 10 ngày làm việc k ể từ ngày k ý quyết định khen thưởng thuộc th ẩ m quy ề n của B ộ trưởng và nhận được Quyết định khen thưởng của các c ấ p có thẩm quyền , Vụ Thi đua - Khen thưởng ph ố i h ợ p với các đ ơn vị liên quan c ó trách nhiệm thông báo quyết định khen thưởng trên “ Cổng Thông tin điện tử ” của Bộ Kế hoạch và Đầu tư . `[DIEM]`) ==[ **THUOC_VE** ]==> (`e1` Khoản 2 `[KHOAN]`)


---

### Mẫu #06_2012_TT-BKHĐT_27861#body_context_53 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[06/2012/TT-BKHĐT]`<SO_HIEU>`** ban hành **[ngày 19 tháng 10 năm 2012]`<NGAY_BAN_HANH>`** bởi **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** . **[Điều 27]`<DIEU>`** . **[Khoản 1]`<KHOAN>`** . **[a ) Các đơn vị thuộc cơ quan Bộ : Ngày 15/1 hàng năm ( gửi trực tiếp ) . Riêng T ổ ng cục Thống kê đ ợ t 1 : Ngà y 31/12 ; đợi 2 ngày 15/1 h àng năm . - Riêng các danh hiệu thi đua , hình thức khen thưởng thuộc th ẩ m quyền của Th ủ trưởng các đ ơ n vị ( đã phân c ấ p ) : Giao Thủ trư ở ng các đơn vị quy định .]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **06/2012/TT-BKHĐT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[11:15]`)
- `[e3]` **ngày 19 tháng 10 năm 2012** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 27** → `DIEU` (span: `[16:18]`)
- `[e5]` **Khoản 1** → `KHOAN` (span: `[19:21]`)
- `[e6]` **a ) Các đơn vị thuộc cơ quan Bộ : Ngày 15/1 hàng năm ( gửi trực tiếp ) . Riêng T ổ ng cục Thống kê đ ợ t 1 : Ngà y 31/12 ; đợi 2 ngày 15/1 h àng năm . - Riêng các danh hiệu thi đua , hình thức khen thưởng thuộc th ẩ m quyền của Th ủ trưởng các đ ơ n vị ( đã phân c ấ p ) : Giao Thủ trư ở ng các đơn vị quy định .** → `DIEM` (span: `[22:98]`)

**Quan hệ:**
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 19 tháng 10 năm 2012 `[NGAY_BAN_HANH]`)
- (`e4` Điều 27 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`)
- (`e5` Khoản 1 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 27 `[DIEU]`)
- (`e6` a ) Các đơn vị thuộc cơ quan Bộ : Ngày 15/1 hàng năm ( gửi trực tiếp ) . Riêng T ổ ng cục Thống kê đ ợ t 1 : Ngà y 31/12 ; đợi 2 ngày 15/1 h àng năm . - Riêng các danh hiệu thi đua , hình thức khen thưởng thuộc th ẩ m quyền của Th ủ trưởng các đ ơ n vị ( đã phân c ấ p ) : Giao Thủ trư ở ng các đơn vị quy định . `[DIEM]`) ==[ **THUOC_VE** ]==> (`e5` Khoản 1 `[KHOAN]`)


---

### Mẫu #06_2012_TT-BKHĐT_27861#body_standalone_54 (Loại: `body_standalone`)
> **[Điều 27]`<DIEU>`** . **[Khoản 1]`<KHOAN>`** . **[a ) Các đơn vị thuộc cơ quan Bộ : Ngày 15/1 hàng năm ( gửi trực tiếp ) . Riêng T ổ ng cục Thống kê đ ợ t 1 : Ngà y 31/12 ; đợi 2 ngày 15/1 h àng năm . - Riêng các danh hiệu thi đua , hình thức khen thưởng thuộc th ẩ m quyền của Th ủ trưởng các đ ơ n vị ( đã phân c ấ p ) : Giao Thủ trư ở ng các đơn vị quy định .]`<DIEM>`**

**Thực thể:**
- `[e0]` **Điều 27** → `DIEU` (span: `[0:2]`)
- `[e1]` **Khoản 1** → `KHOAN` (span: `[3:5]`)
- `[e2]` **a ) Các đơn vị thuộc cơ quan Bộ : Ngày 15/1 hàng năm ( gửi trực tiếp ) . Riêng T ổ ng cục Thống kê đ ợ t 1 : Ngà y 31/12 ; đợi 2 ngày 15/1 h àng năm . - Riêng các danh hiệu thi đua , hình thức khen thưởng thuộc th ẩ m quyền của Th ủ trưởng các đ ơ n vị ( đã phân c ấ p ) : Giao Thủ trư ở ng các đơn vị quy định .** → `DIEM` (span: `[6:82]`)

**Quan hệ:**
- (`e1` Khoản 1 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 27 `[DIEU]`)
- (`e2` a ) Các đơn vị thuộc cơ quan Bộ : Ngày 15/1 hàng năm ( gửi trực tiếp ) . Riêng T ổ ng cục Thống kê đ ợ t 1 : Ngà y 31/12 ; đợi 2 ngày 15/1 h àng năm . - Riêng các danh hiệu thi đua , hình thức khen thưởng thuộc th ẩ m quyền của Th ủ trưởng các đ ơ n vị ( đã phân c ấ p ) : Giao Thủ trư ở ng các đơn vị quy định . `[DIEM]`) ==[ **THUOC_VE** ]==> (`e1` Khoản 1 `[KHOAN]`)


---

### Mẫu #06_2012_TT-BKHĐT_27861#body_context_55 (Loại: `body_context`)
> **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[06/2012/TT-BKHĐT]`<SO_HIEU>`** . **[Điều 31]`<DIEU>`** . **[1 . Hằng năm , V ă n phòng Bộ K ế hoạch và Đầu tư có trách nhiệm b ố trí kinh phí phục vụ cho công t ác thi đua , khen thưởng của Bộ theo q u y định tại khoản 1 , Đi ề u 67 , Nghị định s ố 42/2010/NĐ-CP ngày 15/4/20 10 của **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** và **[Thông tư số 71/2011]`<THAM_CHIEU_PHAP_LY>`** / T T - BTC **[ngày 24/5/2011]`<NGAY_THAM_CHIEU>`** c ủ a **[Bộ Tài chính]`<CO_QUAN_THAM_QUYEN>`** Hướng dẫn việc trích lập , quản lý và sử dụng Qu ỹ thi đua , khen thưởng .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[5:6]`)
- `[e1]` **06/2012/TT-BKHĐT** → `SO_HIEU` (span: `[7:8]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[0:4]`)
- `[e3]` **Điều 31** → `DIEU` (span: `[9:11]`)
- `[e4]` **1 . Hằng năm , V ă n phòng Bộ K ế hoạch và Đầu tư có trách nhiệm b ố trí kinh phí phục vụ cho công t ác thi đua , khen thưởng của Bộ theo q u y định tại khoản 1 , Đi ề u 67 , Nghị định s ố 42/2010/NĐ-CP ngày 15/4/20 10 của Chính phủ và Thông tư số 71/2011 / T T - BTC ngày 24/5/2011 c ủ a Bộ Tài chính Hướng dẫn việc trích lập , quản lý và sử dụng Qu ỹ thi đua , khen thưởng .** → `KHOAN` (span: `[12:93]`)
- `[e5]` **Thông tư số 71/2011** → `THAM_CHIEU_PHAP_LY` (span: `[66:69]`) *(lồng trong `e4` (`KHOAN`))*
- `[e6]` **ngày 24/5/2011** → `NGAY_THAM_CHIEU` (span: `[73:75]`) *(lồng trong `e4` (`KHOAN`))*
- `[e7]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[64:65]`) *(lồng trong `e4` (`KHOAN`))*
- `[e8]` **Bộ Tài chính** → `CO_QUAN_THAM_QUYEN` (span: `[78:80]`) *(lồng trong `e4` (`KHOAN`))*

**Quan hệ:**
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 31 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`)
- (`e4` 1 . Hằng năm , V ă n phòng Bộ K ế hoạch và Đầu tư có trách nhiệm b ố trí kinh phí phục vụ cho công t ác thi đua , khen thưởng của Bộ theo q u y định tại khoản 1 , Đi ề u 67 , Nghị định s ố 42/2010/NĐ-CP ngày 15/4/20 10 của Chính phủ và Thông tư số 71/2011 / T T - BTC ngày 24/5/2011 c ủ a Bộ Tài chính Hướng dẫn việc trích lập , quản lý và sử dụng Qu ỹ thi đua , khen thưởng . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 31 `[DIEU]`)
- (`e4` 1 . Hằng năm , V ă n phòng Bộ K ế hoạch và Đầu tư có trách nhiệm b ố trí kinh phí phục vụ cho công t ác thi đua , khen thưởng của Bộ theo q u y định tại khoản 1 , Đi ề u 67 , Nghị định s ố 42/2010/NĐ-CP ngày 15/4/20 10 của Chính phủ và Thông tư số 71/2011 / T T - BTC ngày 24/5/2011 c ủ a Bộ Tài chính Hướng dẫn việc trích lập , quản lý và sử dụng Qu ỹ thi đua , khen thưởng . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e5` Thông tư số 71/2011 `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e5` Thông tư số 71/2011 `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e6` ngày 24/5/2011 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #06_2012_TT-BKHĐT_27861#body_standalone_56 (Loại: `body_standalone`)
> **[Điều 31]`<DIEU>`** . **[1 . Hằng năm , V ă n phòng Bộ K ế hoạch và Đầu tư có trách nhiệm b ố trí kinh phí phục vụ cho công t ác thi đua , khen thưởng của Bộ theo q u y định tại khoản 1 , Đi ề u 67 , Nghị định s ố 42/2010/NĐ-CP ngày 15/4/20 10 của **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** và **[Thông tư số 71/2011]`<THAM_CHIEU_PHAP_LY>`** / T T - BTC **[ngày 24/5/2011]`<NGAY_THAM_CHIEU>`** c ủ a **[Bộ Tài chính]`<CO_QUAN_THAM_QUYEN>`** Hướng dẫn việc trích lập , quản lý và sử dụng Qu ỹ thi đua , khen thưởng .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 31** → `DIEU` (span: `[0:2]`)
- `[e1]` **1 . Hằng năm , V ă n phòng Bộ K ế hoạch và Đầu tư có trách nhiệm b ố trí kinh phí phục vụ cho công t ác thi đua , khen thưởng của Bộ theo q u y định tại khoản 1 , Đi ề u 67 , Nghị định s ố 42/2010/NĐ-CP ngày 15/4/20 10 của Chính phủ và Thông tư số 71/2011 / T T - BTC ngày 24/5/2011 c ủ a Bộ Tài chính Hướng dẫn việc trích lập , quản lý và sử dụng Qu ỹ thi đua , khen thưởng .** → `KHOAN` (span: `[3:84]`)
- `[e2]` **Thông tư số 71/2011** → `THAM_CHIEU_PHAP_LY` (span: `[57:60]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **ngày 24/5/2011** → `NGAY_THAM_CHIEU` (span: `[64:66]`) *(lồng trong `e1` (`KHOAN`))*
- `[e4]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[55:56]`) *(lồng trong `e1` (`KHOAN`))*
- `[e5]` **Bộ Tài chính** → `CO_QUAN_THAM_QUYEN` (span: `[69:71]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 1 . Hằng năm , V ă n phòng Bộ K ế hoạch và Đầu tư có trách nhiệm b ố trí kinh phí phục vụ cho công t ác thi đua , khen thưởng của Bộ theo q u y định tại khoản 1 , Đi ề u 67 , Nghị định s ố 42/2010/NĐ-CP ngày 15/4/20 10 của Chính phủ và Thông tư số 71/2011 / T T - BTC ngày 24/5/2011 c ủ a Bộ Tài chính Hướng dẫn việc trích lập , quản lý và sử dụng Qu ỹ thi đua , khen thưởng . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 31 `[DIEU]`)
- (`e1` 1 . Hằng năm , V ă n phòng Bộ K ế hoạch và Đầu tư có trách nhiệm b ố trí kinh phí phục vụ cho công t ác thi đua , khen thưởng của Bộ theo q u y định tại khoản 1 , Đi ề u 67 , Nghị định s ố 42/2010/NĐ-CP ngày 15/4/20 10 của Chính phủ và Thông tư số 71/2011 / T T - BTC ngày 24/5/2011 c ủ a Bộ Tài chính Hướng dẫn việc trích lập , quản lý và sử dụng Qu ỹ thi đua , khen thưởng . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e2` Thông tư số 71/2011 `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e2` Thông tư số 71/2011 `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e3` ngày 24/5/2011 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #06_2012_TT-BKHĐT_27861#body_context_57 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[06/2012/TT-BKHĐT]`<SO_HIEU>`** của **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Khoa học và công nghệ]`<LINH_VUC>`** . **[Điều 32]`<DIEU>`** . **[Khoản 1]`<KHOAN>`** . **[b ) Quỹ thi đua , khen thưởng c ủ a Bộ K ế hoạch và Đ ầ u tư được sử dụng : + Tổ chức các cuộc họp Hội đồng Thi đua - Khen thưởng ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **06/2012/TT-BKHĐT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[4:8]`)
- `[e3]` **Khoa học và công nghệ** → `LINH_VUC` (span: `[10:13]`)
- `[e4]` **Điều 32** → `DIEU` (span: `[14:16]`)
- `[e5]` **Khoản 1** → `KHOAN` (span: `[17:19]`)
- `[e6]` **b ) Quỹ thi đua , khen thưởng c ủ a Bộ K ế hoạch và Đ ầ u tư được sử dụng : + Tổ chức các cuộc họp Hội đồng Thi đua - Khen thưởng ;** → `DIEM` (span: `[20:50]`)

**Quan hệ:**
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Khoa học và công nghệ `[LINH_VUC]`)
- (`e4` Điều 32 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`)
- (`e5` Khoản 1 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 32 `[DIEU]`)
- (`e6` b ) Quỹ thi đua , khen thưởng c ủ a Bộ K ế hoạch và Đ ầ u tư được sử dụng : + Tổ chức các cuộc họp Hội đồng Thi đua - Khen thưởng ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e5` Khoản 1 `[KHOAN]`)
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Khoa học và công nghệ `[LINH_VUC]`)
- (`e6` b ) Quỹ thi đua , khen thưởng c ủ a Bộ K ế hoạch và Đ ầ u tư được sử dụng : + Tổ chức các cuộc họp Hội đồng Thi đua - Khen thưởng ; `[DIEM]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Khoa học và công nghệ `[LINH_VUC]`)


---

### Mẫu #06_2012_TT-BKHĐT_27861#body_context_58 (Loại: `body_context`)
> **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[06/2012/TT-BKHĐT]`<SO_HIEU>`** . **[Điều 32]`<DIEU>`** . **[2 . Quỹ thi đua , khen thưởng của các đơn vị thuộc Bộ ( đã được ph â n c ấ p ) : Do các đơn vị qu ả n lý và sử dụng theo đú ng **[quy định tại]`<TU_KHOA_PHAP_LY>`** Nghị định s ố 42/2010/NĐ-CP ngày 15/4/2010 của **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** ; **[Thông tư số 71/2011/TT-BTC]`<THAM_CHIEU_PHAP_LY>`** **[ngày 24/5/2011]`<NGAY_THAM_CHIEU>`** của **[Bộ Tài chính]`<CO_QUAN_THAM_QUYEN>`** cụ thể :]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[5:6]`)
- `[e1]` **06/2012/TT-BKHĐT** → `SO_HIEU` (span: `[7:8]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[0:4]`)
- `[e3]` **Điều 32** → `DIEU` (span: `[9:11]`)
- `[e4]` **2 . Quỹ thi đua , khen thưởng của các đơn vị thuộc Bộ ( đã được ph â n c ấ p ) : Do các đơn vị qu ả n lý và sử dụng theo đú ng quy định tại Nghị định s ố 42/2010/NĐ-CP ngày 15/4/2010 của Chính phủ ; Thông tư số 71/2011/TT-BTC ngày 24/5/2011 của Bộ Tài chính cụ thể :** → `KHOAN` (span: `[12:67]`)
- `[e5]` **Thông tư số 71/2011/TT-BTC** → `THAM_CHIEU_PHAP_LY` (span: `[57:60]`) *(lồng trong `e4` (`KHOAN`))*
- `[e6]` **quy định tại** → `TU_KHOA_PHAP_LY` (span: `[46:48]`) *(lồng trong `e4` (`KHOAN`))*
- `[e7]` **ngày 24/5/2011** → `NGAY_THAM_CHIEU` (span: `[60:62]`) *(lồng trong `e4` (`KHOAN`))*
- `[e8]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[55:56]`) *(lồng trong `e4` (`KHOAN`))*
- `[e9]` **Bộ Tài chính** → `CO_QUAN_THAM_QUYEN` (span: `[63:65]`) *(lồng trong `e4` (`KHOAN`))*

**Quan hệ:**
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 32 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`)
- (`e4` 2 . Quỹ thi đua , khen thưởng của các đơn vị thuộc Bộ ( đã được ph â n c ấ p ) : Do các đơn vị qu ả n lý và sử dụng theo đú ng quy định tại Nghị định s ố 42/2010/NĐ-CP ngày 15/4/2010 của Chính phủ ; Thông tư số 71/2011/TT-BTC ngày 24/5/2011 của Bộ Tài chính cụ thể : `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 32 `[DIEU]`)
- (`e6` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e5` Thông tư số 71/2011/TT-BTC `[THAM_CHIEU_PHAP_LY]`)
- (`e4` 2 . Quỹ thi đua , khen thưởng của các đơn vị thuộc Bộ ( đã được ph â n c ấ p ) : Do các đơn vị qu ả n lý và sử dụng theo đú ng quy định tại Nghị định s ố 42/2010/NĐ-CP ngày 15/4/2010 của Chính phủ ; Thông tư số 71/2011/TT-BTC ngày 24/5/2011 của Bộ Tài chính cụ thể : `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e5` Thông tư số 71/2011/TT-BTC `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e5` Thông tư số 71/2011/TT-BTC `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e7` ngày 24/5/2011 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #06_2012_TT-BKHĐT_27861#body_standalone_59 (Loại: `body_standalone`)
> **[Điều 32]`<DIEU>`** . **[2 . Quỹ thi đua , khen thưởng của các đơn vị thuộc Bộ ( đã được ph â n c ấ p ) : Do các đơn vị qu ả n lý và sử dụng theo đú ng **[quy định tại]`<TU_KHOA_PHAP_LY>`** Nghị định s ố 42/2010/NĐ-CP ngày 15/4/2010 của **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** ; **[Thông tư số 71/2011/TT-BTC]`<THAM_CHIEU_PHAP_LY>`** **[ngày 24/5/2011]`<NGAY_THAM_CHIEU>`** của **[Bộ Tài chính]`<CO_QUAN_THAM_QUYEN>`** cụ thể :]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 32** → `DIEU` (span: `[0:2]`)
- `[e1]` **2 . Quỹ thi đua , khen thưởng của các đơn vị thuộc Bộ ( đã được ph â n c ấ p ) : Do các đơn vị qu ả n lý và sử dụng theo đú ng quy định tại Nghị định s ố 42/2010/NĐ-CP ngày 15/4/2010 của Chính phủ ; Thông tư số 71/2011/TT-BTC ngày 24/5/2011 của Bộ Tài chính cụ thể :** → `KHOAN` (span: `[3:58]`)
- `[e2]` **Thông tư số 71/2011/TT-BTC** → `THAM_CHIEU_PHAP_LY` (span: `[48:51]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **quy định tại** → `TU_KHOA_PHAP_LY` (span: `[37:39]`) *(lồng trong `e1` (`KHOAN`))*
- `[e4]` **ngày 24/5/2011** → `NGAY_THAM_CHIEU` (span: `[51:53]`) *(lồng trong `e1` (`KHOAN`))*
- `[e5]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[46:47]`) *(lồng trong `e1` (`KHOAN`))*
- `[e6]` **Bộ Tài chính** → `CO_QUAN_THAM_QUYEN` (span: `[54:56]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 2 . Quỹ thi đua , khen thưởng của các đơn vị thuộc Bộ ( đã được ph â n c ấ p ) : Do các đơn vị qu ả n lý và sử dụng theo đú ng quy định tại Nghị định s ố 42/2010/NĐ-CP ngày 15/4/2010 của Chính phủ ; Thông tư số 71/2011/TT-BTC ngày 24/5/2011 của Bộ Tài chính cụ thể : `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 32 `[DIEU]`)
- (`e3` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e2` Thông tư số 71/2011/TT-BTC `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 2 . Quỹ thi đua , khen thưởng của các đơn vị thuộc Bộ ( đã được ph â n c ấ p ) : Do các đơn vị qu ả n lý và sử dụng theo đú ng quy định tại Nghị định s ố 42/2010/NĐ-CP ngày 15/4/2010 của Chính phủ ; Thông tư số 71/2011/TT-BTC ngày 24/5/2011 của Bộ Tài chính cụ thể : `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e2` Thông tư số 71/2011/TT-BTC `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e2` Thông tư số 71/2011/TT-BTC `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e4` ngày 24/5/2011 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #06_2012_TT-BKHĐT_27861#body_context_60 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[06/2012/TT-BKHĐT]`<SO_HIEU>`** của **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Khoa học và công nghệ]`<LINH_VUC>`** . **[Điều 32]`<DIEU>`** . **[4 . Mức tiền thư ở ng kèm theo các d anh hiệu thi đua , các hình thức khen thưởng được thực h iện **[theo quy định tại]`<TU_KHOA_PHAP_LY>`** **[Nghị định số 42/2010/NĐ-CP]`<THAM_CHIEU_PHAP_LY>`** **[ngày 15 tháng 4 năm 2010]`<NGAY_THAM_CHIEU>`** của **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **06/2012/TT-BKHĐT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[4:8]`)
- `[e3]` **Khoa học và công nghệ** → `LINH_VUC` (span: `[10:13]`)
- `[e4]` **Điều 32** → `DIEU` (span: `[14:16]`)
- `[e5]` **4 . Mức tiền thư ở ng kèm theo các d anh hiệu thi đua , các hình thức khen thưởng được thực h iện theo quy định tại Nghị định số 42/2010/NĐ-CP ngày 15 tháng 4 năm 2010 của Chính phủ .** → `KHOAN` (span: `[17:53]`)
- `[e6]` **Nghị định số 42/2010/NĐ-CP** → `THAM_CHIEU_PHAP_LY` (span: `[41:44]`) *(lồng trong `e5` (`KHOAN`))*
- `[e7]` **theo quy định tại** → `TU_KHOA_PHAP_LY` (span: `[38:41]`) *(lồng trong `e5` (`KHOAN`))*
- `[e8]` **ngày 15 tháng 4 năm 2010** → `NGAY_THAM_CHIEU` (span: `[44:50]`) *(lồng trong `e5` (`KHOAN`))*
- `[e9]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[51:52]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Khoa học và công nghệ `[LINH_VUC]`)
- (`e4` Điều 32 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`)
- (`e5` 4 . Mức tiền thư ở ng kèm theo các d anh hiệu thi đua , các hình thức khen thưởng được thực h iện theo quy định tại Nghị định số 42/2010/NĐ-CP ngày 15 tháng 4 năm 2010 của Chính phủ . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 32 `[DIEU]`)
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Khoa học và công nghệ `[LINH_VUC]`)
- (`e5` 4 . Mức tiền thư ở ng kèm theo các d anh hiệu thi đua , các hình thức khen thưởng được thực h iện theo quy định tại Nghị định số 42/2010/NĐ-CP ngày 15 tháng 4 năm 2010 của Chính phủ . `[KHOAN]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Khoa học và công nghệ `[LINH_VUC]`)
- (`e7` theo quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e6` Nghị định số 42/2010/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e5` 4 . Mức tiền thư ở ng kèm theo các d anh hiệu thi đua , các hình thức khen thưởng được thực h iện theo quy định tại Nghị định số 42/2010/NĐ-CP ngày 15 tháng 4 năm 2010 của Chính phủ . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e6` Nghị định số 42/2010/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e6` Nghị định số 42/2010/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e8` ngày 15 tháng 4 năm 2010 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #06_2012_TT-BKHĐT_27861#body_standalone_61 (Loại: `body_standalone`)
> **[Điều 32]`<DIEU>`** . **[4 . Mức tiền thư ở ng kèm theo các d anh hiệu thi đua , các hình thức khen thưởng được thực h iện **[theo quy định tại]`<TU_KHOA_PHAP_LY>`** **[Nghị định số 42/2010/NĐ-CP]`<THAM_CHIEU_PHAP_LY>`** **[ngày 15 tháng 4 năm 2010]`<NGAY_THAM_CHIEU>`** của **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 32** → `DIEU` (span: `[0:2]`)
- `[e1]` **4 . Mức tiền thư ở ng kèm theo các d anh hiệu thi đua , các hình thức khen thưởng được thực h iện theo quy định tại Nghị định số 42/2010/NĐ-CP ngày 15 tháng 4 năm 2010 của Chính phủ .** → `KHOAN` (span: `[3:39]`)
- `[e2]` **Nghị định số 42/2010/NĐ-CP** → `THAM_CHIEU_PHAP_LY` (span: `[27:30]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **theo quy định tại** → `TU_KHOA_PHAP_LY` (span: `[24:27]`) *(lồng trong `e1` (`KHOAN`))*
- `[e4]` **ngày 15 tháng 4 năm 2010** → `NGAY_THAM_CHIEU` (span: `[30:36]`) *(lồng trong `e1` (`KHOAN`))*
- `[e5]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[37:38]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 4 . Mức tiền thư ở ng kèm theo các d anh hiệu thi đua , các hình thức khen thưởng được thực h iện theo quy định tại Nghị định số 42/2010/NĐ-CP ngày 15 tháng 4 năm 2010 của Chính phủ . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 32 `[DIEU]`)
- (`e3` theo quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e2` Nghị định số 42/2010/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 4 . Mức tiền thư ở ng kèm theo các d anh hiệu thi đua , các hình thức khen thưởng được thực h iện theo quy định tại Nghị định số 42/2010/NĐ-CP ngày 15 tháng 4 năm 2010 của Chính phủ . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e2` Nghị định số 42/2010/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e2` Nghị định số 42/2010/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e4` ngày 15 tháng 4 năm 2010 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #06_2012_TT-BKHĐT_27861#body_context_62 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[06/2012/TT-BKHĐT]`<SO_HIEU>`** ban hành **[ngày 19 tháng 10 năm 2012]`<NGAY_BAN_HANH>`** bởi **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** . **[Điều 2]`<DIEU>`** . **[Khoản 4 . Giải thích từ ngữ]`<KHOAN>`** : **[d ) Khối thi đua : Là việc tổ chức phân chia các đơn vị thuộc Bộ thành từng Khối có tính đặc thù riêng để ký kết giao ước thi đua , xây dựng mục tiêu chung và phấn đấu , thi đua hoàn thành mục tiêu đã đề ra .]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **06/2012/TT-BKHĐT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[11:15]`)
- `[e3]` **ngày 19 tháng 10 năm 2012** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 2** → `DIEU` (span: `[16:18]`)
- `[e5]` **Khoản 4 . Giải thích từ ngữ** → `KHOAN` (span: `[19:24]`)
- `[e6]` **d ) Khối thi đua : Là việc tổ chức phân chia các đơn vị thuộc Bộ thành từng Khối có tính đặc thù riêng để ký kết giao ước thi đua , xây dựng mục tiêu chung và phấn đấu , thi đua hoàn thành mục tiêu đã đề ra .** → `DIEM` (span: `[25:63]`)

**Quan hệ:**
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 19 tháng 10 năm 2012 `[NGAY_BAN_HANH]`)
- (`e4` Điều 2 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`)
- (`e5` Khoản 4 . Giải thích từ ngữ `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 2 `[DIEU]`)
- (`e6` d ) Khối thi đua : Là việc tổ chức phân chia các đơn vị thuộc Bộ thành từng Khối có tính đặc thù riêng để ký kết giao ước thi đua , xây dựng mục tiêu chung và phấn đấu , thi đua hoàn thành mục tiêu đã đề ra . `[DIEM]`) ==[ **THUOC_VE** ]==> (`e5` Khoản 4 . Giải thích từ ngữ `[KHOAN]`)


---

### Mẫu #06_2012_TT-BKHĐT_27861#body_context_63 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[06/2012/TT-BKHĐT]`<SO_HIEU>`** của **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Khoa học và công nghệ]`<LINH_VUC>`** . **[Điều 2]`<DIEU>`** . **[Khoản 4 . Giải thích từ ngữ]`<KHOAN>`** : **[g ) Các đơn vị thuộc Bộ : Được hiểu là các đơn vị trực thuộc **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_THAM_QUYEN>`** được **[quy định tại]`<TU_KHOA_PHAP_LY>`** **[Điều 3]`<THAM_CHIEU_PHAP_LY>`** , Nghị định 116/2008/NĐ-CP **[ngày 14/11/2008]`<NGAY_THAM_CHIEU>`** của **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** quy định về chức năng , nhiệm vụ , quyền hạn và cơ cấu tổ chức của **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_THAM_QUYEN>`** và Cục Quản lý Đăng ký kinh doanh , Trường Cao Đẳng Kinh tế Kế hoạch Đà Nẵng .]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **06/2012/TT-BKHĐT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[4:8]`)
- `[e3]` **Khoa học và công nghệ** → `LINH_VUC` (span: `[10:13]`)
- `[e4]` **Điều 2** → `DIEU` (span: `[14:16]`)
- `[e5]` **Khoản 4 . Giải thích từ ngữ** → `KHOAN` (span: `[17:22]`)
- `[e6]` **g ) Các đơn vị thuộc Bộ : Được hiểu là các đơn vị trực thuộc Bộ Kế hoạch và Đầu tư được quy định tại Điều 3 , Nghị định 116/2008/NĐ-CP ngày 14/11/2008 của Chính phủ quy định về chức năng , nhiệm vụ , quyền hạn và cơ cấu tổ chức của Bộ Kế hoạch và Đầu tư và Cục Quản lý Đăng ký kinh doanh , Trường Cao Đẳng Kinh tế Kế hoạch Đà Nẵng .** → `DIEM` (span: `[23:79]`)
- `[e7]` **Điều 3** → `THAM_CHIEU_PHAP_LY` (span: `[43:45]`) *(lồng trong `e6` (`DIEM`))*
- `[e8]` **quy định tại** → `TU_KHOA_PHAP_LY` (span: `[41:43]`) *(lồng trong `e6` (`DIEM`))*
- `[e9]` **ngày 14/11/2008** → `NGAY_THAM_CHIEU` (span: `[48:50]`) *(lồng trong `e6` (`DIEM`))*
- `[e10]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_THAM_QUYEN` (span: `[36:40]`) *(lồng trong `e6` (`DIEM`))*
- `[e11]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[51:52]`) *(lồng trong `e6` (`DIEM`))*
- `[e12]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_THAM_QUYEN` (span: `[63:67]`) *(lồng trong `e6` (`DIEM`))*

**Quan hệ:**
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Khoa học và công nghệ `[LINH_VUC]`)
- (`e4` Điều 2 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`)
- (`e5` Khoản 4 . Giải thích từ ngữ `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 2 `[DIEU]`)
- (`e6` g ) Các đơn vị thuộc Bộ : Được hiểu là các đơn vị trực thuộc Bộ Kế hoạch và Đầu tư được quy định tại Điều 3 , Nghị định 116/2008/NĐ-CP ngày 14/11/2008 của Chính phủ quy định về chức năng , nhiệm vụ , quyền hạn và cơ cấu tổ chức của Bộ Kế hoạch và Đầu tư và Cục Quản lý Đăng ký kinh doanh , Trường Cao Đẳng Kinh tế Kế hoạch Đà Nẵng . `[DIEM]`) ==[ **THUOC_VE** ]==> (`e5` Khoản 4 . Giải thích từ ngữ `[KHOAN]`)
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Khoa học và công nghệ `[LINH_VUC]`)
- (`e6` g ) Các đơn vị thuộc Bộ : Được hiểu là các đơn vị trực thuộc Bộ Kế hoạch và Đầu tư được quy định tại Điều 3 , Nghị định 116/2008/NĐ-CP ngày 14/11/2008 của Chính phủ quy định về chức năng , nhiệm vụ , quyền hạn và cơ cấu tổ chức của Bộ Kế hoạch và Đầu tư và Cục Quản lý Đăng ký kinh doanh , Trường Cao Đẳng Kinh tế Kế hoạch Đà Nẵng . `[DIEM]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Khoa học và công nghệ `[LINH_VUC]`)
- (`e8` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e7` Điều 3 `[THAM_CHIEU_PHAP_LY]`)
- (`e6` g ) Các đơn vị thuộc Bộ : Được hiểu là các đơn vị trực thuộc Bộ Kế hoạch và Đầu tư được quy định tại Điều 3 , Nghị định 116/2008/NĐ-CP ngày 14/11/2008 của Chính phủ quy định về chức năng , nhiệm vụ , quyền hạn và cơ cấu tổ chức của Bộ Kế hoạch và Đầu tư và Cục Quản lý Đăng ký kinh doanh , Trường Cao Đẳng Kinh tế Kế hoạch Đà Nẵng . `[DIEM]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e7` Điều 3 `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e7` Điều 3 `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e9` ngày 14/11/2008 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #06_2012_TT-BKHĐT_27861#body_standalone_64 (Loại: `body_standalone`)
> **[Điều 2]`<DIEU>`** . **[Khoản 4 . Giải thích từ ngữ]`<KHOAN>`** : **[g ) Các đơn vị thuộc Bộ : Được hiểu là các đơn vị trực thuộc **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_THAM_QUYEN>`** được **[quy định tại]`<TU_KHOA_PHAP_LY>`** **[Điều 3]`<THAM_CHIEU_PHAP_LY>`** , Nghị định 116/2008/NĐ-CP **[ngày 14/11/2008]`<NGAY_THAM_CHIEU>`** của **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** quy định về chức năng , nhiệm vụ , quyền hạn và cơ cấu tổ chức của **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_THAM_QUYEN>`** và Cục Quản lý Đăng ký kinh doanh , Trường Cao Đẳng Kinh tế Kế hoạch Đà Nẵng .]`<DIEM>`**

**Thực thể:**
- `[e0]` **Điều 2** → `DIEU` (span: `[0:2]`)
- `[e1]` **Khoản 4 . Giải thích từ ngữ** → `KHOAN` (span: `[3:8]`)
- `[e2]` **g ) Các đơn vị thuộc Bộ : Được hiểu là các đơn vị trực thuộc Bộ Kế hoạch và Đầu tư được quy định tại Điều 3 , Nghị định 116/2008/NĐ-CP ngày 14/11/2008 của Chính phủ quy định về chức năng , nhiệm vụ , quyền hạn và cơ cấu tổ chức của Bộ Kế hoạch và Đầu tư và Cục Quản lý Đăng ký kinh doanh , Trường Cao Đẳng Kinh tế Kế hoạch Đà Nẵng .** → `DIEM` (span: `[9:65]`)
- `[e3]` **Điều 3** → `THAM_CHIEU_PHAP_LY` (span: `[29:31]`) *(lồng trong `e2` (`DIEM`))*
- `[e4]` **quy định tại** → `TU_KHOA_PHAP_LY` (span: `[27:29]`) *(lồng trong `e2` (`DIEM`))*
- `[e5]` **ngày 14/11/2008** → `NGAY_THAM_CHIEU` (span: `[34:36]`) *(lồng trong `e2` (`DIEM`))*
- `[e6]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_THAM_QUYEN` (span: `[22:26]`) *(lồng trong `e2` (`DIEM`))*
- `[e7]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[37:38]`) *(lồng trong `e2` (`DIEM`))*
- `[e8]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_THAM_QUYEN` (span: `[49:53]`) *(lồng trong `e2` (`DIEM`))*

**Quan hệ:**
- (`e1` Khoản 4 . Giải thích từ ngữ `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 2 `[DIEU]`)
- (`e2` g ) Các đơn vị thuộc Bộ : Được hiểu là các đơn vị trực thuộc Bộ Kế hoạch và Đầu tư được quy định tại Điều 3 , Nghị định 116/2008/NĐ-CP ngày 14/11/2008 của Chính phủ quy định về chức năng , nhiệm vụ , quyền hạn và cơ cấu tổ chức của Bộ Kế hoạch và Đầu tư và Cục Quản lý Đăng ký kinh doanh , Trường Cao Đẳng Kinh tế Kế hoạch Đà Nẵng . `[DIEM]`) ==[ **THUOC_VE** ]==> (`e1` Khoản 4 . Giải thích từ ngữ `[KHOAN]`)
- (`e4` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Điều 3 `[THAM_CHIEU_PHAP_LY]`)
- (`e2` g ) Các đơn vị thuộc Bộ : Được hiểu là các đơn vị trực thuộc Bộ Kế hoạch và Đầu tư được quy định tại Điều 3 , Nghị định 116/2008/NĐ-CP ngày 14/11/2008 của Chính phủ quy định về chức năng , nhiệm vụ , quyền hạn và cơ cấu tổ chức của Bộ Kế hoạch và Đầu tư và Cục Quản lý Đăng ký kinh doanh , Trường Cao Đẳng Kinh tế Kế hoạch Đà Nẵng . `[DIEM]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Điều 3 `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e3` Điều 3 `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e5` ngày 14/11/2008 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #06_2012_TT-BKHĐT_27861#body_context_65 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[06/2012/TT-BKHĐT]`<SO_HIEU>`** của **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Khoa học và công nghệ]`<LINH_VUC>`** . **[Điều 5]`<DIEU>`** . **[1 . **[Bộ trưởng Bộ Kế hoạch và Đầu tư]`<CO_QUAN_THAM_QUYEN>`** chịu trách nhiệm về công tác thi đua , khen thưởng **[ngành Kế hoạch và Đầu tư]`<LINH_VUC>`** ; phát động và chỉ đạo phong trào thi đua trong phạm vi toàn Ngành .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **06/2012/TT-BKHĐT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[4:8]`)
- `[e3]` **Khoa học và công nghệ** → `LINH_VUC` (span: `[10:13]`)
- `[e4]` **Điều 5** → `DIEU` (span: `[14:16]`)
- `[e5]` **1 . Bộ trưởng Bộ Kế hoạch và Đầu tư chịu trách nhiệm về công tác thi đua , khen thưởng ngành Kế hoạch và Đầu tư ; phát động và chỉ đạo phong trào thi đua trong phạm vi toàn Ngành .** → `KHOAN` (span: `[17:46]`)
- `[e6]` **ngành Kế hoạch và Đầu tư** → `LINH_VUC` (span: `[31:35]`) *(lồng trong `e5` (`KHOAN`))*
- `[e7]` **Bộ trưởng Bộ Kế hoạch và Đầu tư** → `CO_QUAN_THAM_QUYEN` (span: `[19:24]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Khoa học và công nghệ `[LINH_VUC]`)
- (`e4` Điều 5 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`)
- (`e5` 1 . Bộ trưởng Bộ Kế hoạch và Đầu tư chịu trách nhiệm về công tác thi đua , khen thưởng ngành Kế hoạch và Đầu tư ; phát động và chỉ đạo phong trào thi đua trong phạm vi toàn Ngành . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 5 `[DIEU]`)
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Khoa học và công nghệ `[LINH_VUC]`)
- (`e5` 1 . Bộ trưởng Bộ Kế hoạch và Đầu tư chịu trách nhiệm về công tác thi đua , khen thưởng ngành Kế hoạch và Đầu tư ; phát động và chỉ đạo phong trào thi đua trong phạm vi toàn Ngành . `[KHOAN]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Khoa học và công nghệ `[LINH_VUC]`)
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e6` ngành Kế hoạch và Đầu tư `[LINH_VUC]`)
- (`e5` 1 . Bộ trưởng Bộ Kế hoạch và Đầu tư chịu trách nhiệm về công tác thi đua , khen thưởng ngành Kế hoạch và Đầu tư ; phát động và chỉ đạo phong trào thi đua trong phạm vi toàn Ngành . `[KHOAN]`) ==[ **THUOC_LINH_VUC** ]==> (`e6` ngành Kế hoạch và Đầu tư `[LINH_VUC]`) *(Quan hệ lồng nhau)*


---

### Mẫu #06_2012_TT-BKHĐT_27861#body_standalone_66 (Loại: `body_standalone`)
> **[Điều 5]`<DIEU>`** . **[1 . **[Bộ trưởng Bộ Kế hoạch và Đầu tư]`<CO_QUAN_THAM_QUYEN>`** chịu trách nhiệm về công tác thi đua , khen thưởng **[ngành Kế hoạch và Đầu tư]`<LINH_VUC>`** ; phát động và chỉ đạo phong trào thi đua trong phạm vi toàn Ngành .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 5** → `DIEU` (span: `[0:2]`)
- `[e1]` **1 . Bộ trưởng Bộ Kế hoạch và Đầu tư chịu trách nhiệm về công tác thi đua , khen thưởng ngành Kế hoạch và Đầu tư ; phát động và chỉ đạo phong trào thi đua trong phạm vi toàn Ngành .** → `KHOAN` (span: `[3:32]`)
- `[e2]` **ngành Kế hoạch và Đầu tư** → `LINH_VUC` (span: `[17:21]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **Bộ trưởng Bộ Kế hoạch và Đầu tư** → `CO_QUAN_THAM_QUYEN` (span: `[5:10]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 1 . Bộ trưởng Bộ Kế hoạch và Đầu tư chịu trách nhiệm về công tác thi đua , khen thưởng ngành Kế hoạch và Đầu tư ; phát động và chỉ đạo phong trào thi đua trong phạm vi toàn Ngành . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 5 `[DIEU]`)
- (`e1` 1 . Bộ trưởng Bộ Kế hoạch và Đầu tư chịu trách nhiệm về công tác thi đua , khen thưởng ngành Kế hoạch và Đầu tư ; phát động và chỉ đạo phong trào thi đua trong phạm vi toàn Ngành . `[KHOAN]`) ==[ **THUOC_LINH_VUC** ]==> (`e2` ngành Kế hoạch và Đầu tư `[LINH_VUC]`) *(Quan hệ lồng nhau)*


---

### Mẫu #06_2012_TT-BKHĐT_27861#body_context_67 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[06/2012/TT-BKHĐT]`<SO_HIEU>`** của **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Khoa học và công nghệ]`<LINH_VUC>`** . **[Điều 6]`<DIEU>`** . **[3 . Là đầu mối tiếp nhận **[hồ sơ đăng ký thi đua]`<GIAY_TO_HO_SO>`** và đề nghị khen thưởng ; tổng hợp , thẩm định và trình Hội đồng Thi đua - Khen thưởng Bộ xem xét , quyết định các danh hiệu thi đua , hình thức khen thưởng cho các tập thể , cá nhân trong toàn Ngành và các đối tượng **[quy định tại]`<TU_KHOA_PHAP_LY>`** **[Điều 2]`<THAM_CHIEU_PHAP_LY>`** , Khoản 2 , Mục b , c , d , đ và Khoản 3 .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **06/2012/TT-BKHĐT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[4:8]`)
- `[e3]` **Khoa học và công nghệ** → `LINH_VUC` (span: `[10:13]`)
- `[e4]` **Điều 6** → `DIEU` (span: `[14:16]`)
- `[e5]` **3 . Là đầu mối tiếp nhận hồ sơ đăng ký thi đua và đề nghị khen thưởng ; tổng hợp , thẩm định và trình Hội đồng Thi đua - Khen thưởng Bộ xem xét , quyết định các danh hiệu thi đua , hình thức khen thưởng cho các tập thể , cá nhân trong toàn Ngành và các đối tượng quy định tại Điều 2 , Khoản 2 , Mục b , c , d , đ và Khoản 3 .** → `KHOAN` (span: `[17:78]`)
- `[e6]` **Điều 2** → `THAM_CHIEU_PHAP_LY` (span: `[61:63]`) *(lồng trong `e5` (`KHOAN`))*
- `[e7]` **quy định tại** → `TU_KHOA_PHAP_LY` (span: `[59:61]`) *(lồng trong `e5` (`KHOAN`))*
- `[e8]` **hồ sơ đăng ký thi đua** → `GIAY_TO_HO_SO` (span: `[22:25]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Khoa học và công nghệ `[LINH_VUC]`)
- (`e4` Điều 6 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`)
- (`e5` 3 . Là đầu mối tiếp nhận hồ sơ đăng ký thi đua và đề nghị khen thưởng ; tổng hợp , thẩm định và trình Hội đồng Thi đua - Khen thưởng Bộ xem xét , quyết định các danh hiệu thi đua , hình thức khen thưởng cho các tập thể , cá nhân trong toàn Ngành và các đối tượng quy định tại Điều 2 , Khoản 2 , Mục b , c , d , đ và Khoản 3 . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 6 `[DIEU]`)
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Khoa học và công nghệ `[LINH_VUC]`)
- (`e5` 3 . Là đầu mối tiếp nhận hồ sơ đăng ký thi đua và đề nghị khen thưởng ; tổng hợp , thẩm định và trình Hội đồng Thi đua - Khen thưởng Bộ xem xét , quyết định các danh hiệu thi đua , hình thức khen thưởng cho các tập thể , cá nhân trong toàn Ngành và các đối tượng quy định tại Điều 2 , Khoản 2 , Mục b , c , d , đ và Khoản 3 . `[KHOAN]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Khoa học và công nghệ `[LINH_VUC]`)
- (`e7` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e6` Điều 2 `[THAM_CHIEU_PHAP_LY]`)
- (`e5` 3 . Là đầu mối tiếp nhận hồ sơ đăng ký thi đua và đề nghị khen thưởng ; tổng hợp , thẩm định và trình Hội đồng Thi đua - Khen thưởng Bộ xem xét , quyết định các danh hiệu thi đua , hình thức khen thưởng cho các tập thể , cá nhân trong toàn Ngành và các đối tượng quy định tại Điều 2 , Khoản 2 , Mục b , c , d , đ và Khoản 3 . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e6` Điều 2 `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #06_2012_TT-BKHĐT_27861#body_standalone_68 (Loại: `body_standalone`)
> **[Điều 6]`<DIEU>`** . **[3 . Là đầu mối tiếp nhận **[hồ sơ đăng ký thi đua]`<GIAY_TO_HO_SO>`** và đề nghị khen thưởng ; tổng hợp , thẩm định và trình Hội đồng Thi đua - Khen thưởng Bộ xem xét , quyết định các danh hiệu thi đua , hình thức khen thưởng cho các tập thể , cá nhân trong toàn Ngành và các đối tượng **[quy định tại]`<TU_KHOA_PHAP_LY>`** **[Điều 2]`<THAM_CHIEU_PHAP_LY>`** , Khoản 2 , Mục b , c , d , đ và Khoản 3 .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 6** → `DIEU` (span: `[0:2]`)
- `[e1]` **3 . Là đầu mối tiếp nhận hồ sơ đăng ký thi đua và đề nghị khen thưởng ; tổng hợp , thẩm định và trình Hội đồng Thi đua - Khen thưởng Bộ xem xét , quyết định các danh hiệu thi đua , hình thức khen thưởng cho các tập thể , cá nhân trong toàn Ngành và các đối tượng quy định tại Điều 2 , Khoản 2 , Mục b , c , d , đ và Khoản 3 .** → `KHOAN` (span: `[3:64]`)
- `[e2]` **Điều 2** → `THAM_CHIEU_PHAP_LY` (span: `[47:49]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **quy định tại** → `TU_KHOA_PHAP_LY` (span: `[45:47]`) *(lồng trong `e1` (`KHOAN`))*
- `[e4]` **hồ sơ đăng ký thi đua** → `GIAY_TO_HO_SO` (span: `[8:11]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 3 . Là đầu mối tiếp nhận hồ sơ đăng ký thi đua và đề nghị khen thưởng ; tổng hợp , thẩm định và trình Hội đồng Thi đua - Khen thưởng Bộ xem xét , quyết định các danh hiệu thi đua , hình thức khen thưởng cho các tập thể , cá nhân trong toàn Ngành và các đối tượng quy định tại Điều 2 , Khoản 2 , Mục b , c , d , đ và Khoản 3 . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 6 `[DIEU]`)
- (`e3` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e2` Điều 2 `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 3 . Là đầu mối tiếp nhận hồ sơ đăng ký thi đua và đề nghị khen thưởng ; tổng hợp , thẩm định và trình Hội đồng Thi đua - Khen thưởng Bộ xem xét , quyết định các danh hiệu thi đua , hình thức khen thưởng cho các tập thể , cá nhân trong toàn Ngành và các đối tượng quy định tại Điều 2 , Khoản 2 , Mục b , c , d , đ và Khoản 3 . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e2` Điều 2 `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #06_2012_TT-BKHĐT_27861#body_context_69 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[06/2012/TT-BKHĐT]`<SO_HIEU>`** ban hành **[ngày 19 tháng 10 năm 2012]`<NGAY_BAN_HANH>`** bởi **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** . **[Chương II]`<CHUONG>`** . **[Điều 7 . Trách nhiệm của các Báo , Tạp chí trong **[ngành Kế hoạch và Đầu tư]`<LINH_VUC>`**]`<DIEU>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **06/2012/TT-BKHĐT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[11:15]`)
- `[e3]` **ngày 19 tháng 10 năm 2012** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Chương II** → `CHUONG` (span: `[16:18]`)
- `[e5]` **Điều 7 . Trách nhiệm của các Báo , Tạp chí trong ngành Kế hoạch và Đầu tư** → `DIEU` (span: `[19:33]`)
- `[e6]` **ngành Kế hoạch và Đầu tư** → `LINH_VUC` (span: `[29:33]`) *(lồng trong `e5` (`DIEU`))*

**Quan hệ:**
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 19 tháng 10 năm 2012 `[NGAY_BAN_HANH]`)
- (`e4` Chương II `[CHUONG]`) ==[ **THUOC_VE** ]==> (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`)
- (`e5` Điều 7 . Trách nhiệm của các Báo , Tạp chí trong ngành Kế hoạch và Đầu tư `[DIEU]`) ==[ **THUOC_VE** ]==> (`e4` Chương II `[CHUONG]`)
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e6` ngành Kế hoạch và Đầu tư `[LINH_VUC]`)
- (`e5` Điều 7 . Trách nhiệm của các Báo , Tạp chí trong ngành Kế hoạch và Đầu tư `[DIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e6` ngành Kế hoạch và Đầu tư `[LINH_VUC]`) *(Quan hệ lồng nhau)*


---

### Mẫu #06_2012_TT-BKHĐT_27861#body_context_70 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[06/2012/TT-BKHĐT]`<SO_HIEU>`** của **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Khoa học và công nghệ]`<LINH_VUC>`** . **[Điều 10]`<DIEU>`** . **[4 . Sơ kết , tổng kết thi đua để đánh giá kết quả , tác dụng của phong trào thi đua ; công khai lựa chọn , bình xét , biểu dương , khen thưởng cá nhân , tập thể đạt thành tích xuất sắc ; tuyên truyền , phổ biến , nhân rộng các gương điển hình tiên tiến trong **[ngành Kế hoạch và Đầu tư]`<LINH_VUC>`** .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **06/2012/TT-BKHĐT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[4:8]`)
- `[e3]` **Khoa học và công nghệ** → `LINH_VUC` (span: `[10:13]`)
- `[e4]` **Điều 10** → `DIEU` (span: `[14:16]`)
- `[e5]` **4 . Sơ kết , tổng kết thi đua để đánh giá kết quả , tác dụng của phong trào thi đua ; công khai lựa chọn , bình xét , biểu dương , khen thưởng cá nhân , tập thể đạt thành tích xuất sắc ; tuyên truyền , phổ biến , nhân rộng các gương điển hình tiên tiến trong ngành Kế hoạch và Đầu tư .** → `KHOAN` (span: `[17:63]`)
- `[e6]` **ngành Kế hoạch và Đầu tư** → `LINH_VUC` (span: `[58:62]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Khoa học và công nghệ `[LINH_VUC]`)
- (`e4` Điều 10 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`)
- (`e5` 4 . Sơ kết , tổng kết thi đua để đánh giá kết quả , tác dụng của phong trào thi đua ; công khai lựa chọn , bình xét , biểu dương , khen thưởng cá nhân , tập thể đạt thành tích xuất sắc ; tuyên truyền , phổ biến , nhân rộng các gương điển hình tiên tiến trong ngành Kế hoạch và Đầu tư . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 10 `[DIEU]`)
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Khoa học và công nghệ `[LINH_VUC]`)
- (`e5` 4 . Sơ kết , tổng kết thi đua để đánh giá kết quả , tác dụng của phong trào thi đua ; công khai lựa chọn , bình xét , biểu dương , khen thưởng cá nhân , tập thể đạt thành tích xuất sắc ; tuyên truyền , phổ biến , nhân rộng các gương điển hình tiên tiến trong ngành Kế hoạch và Đầu tư . `[KHOAN]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Khoa học và công nghệ `[LINH_VUC]`)
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e6` ngành Kế hoạch và Đầu tư `[LINH_VUC]`)
- (`e5` 4 . Sơ kết , tổng kết thi đua để đánh giá kết quả , tác dụng của phong trào thi đua ; công khai lựa chọn , bình xét , biểu dương , khen thưởng cá nhân , tập thể đạt thành tích xuất sắc ; tuyên truyền , phổ biến , nhân rộng các gương điển hình tiên tiến trong ngành Kế hoạch và Đầu tư . `[KHOAN]`) ==[ **THUOC_LINH_VUC** ]==> (`e6` ngành Kế hoạch và Đầu tư `[LINH_VUC]`) *(Quan hệ lồng nhau)*


---

### Mẫu #06_2012_TT-BKHĐT_27861#body_context_71 (Loại: `body_context`)
> **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[06/2012/TT-BKHĐT]`<SO_HIEU>`** . **[Điều 11 . Đăng ký danh hiệu thi đua ; ký giao ước thi đua]`<DIEU>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[5:6]`)
- `[e1]` **06/2012/TT-BKHĐT** → `SO_HIEU` (span: `[7:8]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[0:4]`)
- `[e3]` **Điều 11 . Đăng ký danh hiệu thi đua ; ký giao ước thi đua** → `DIEU` (span: `[9:19]`)

**Quan hệ:**
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 11 . Đăng ký danh hiệu thi đua ; ký giao ước thi đua `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`)


---

### Mẫu #06_2012_TT-BKHĐT_27861#body_context_72 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[06/2012/TT-BKHĐT]`<SO_HIEU>`** của **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Khoa học và công nghệ]`<LINH_VUC>`** . **[Chương III]`<CHUONG>`** . **[Điều 12 . Khối , Cụm , Vùng , Nhóm thi đua **[ngành Kế hoạch và Đầu tư]`<LINH_VUC>`**]`<DIEU>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **06/2012/TT-BKHĐT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[4:8]`)
- `[e3]` **Khoa học và công nghệ** → `LINH_VUC` (span: `[10:13]`)
- `[e4]` **Chương III** → `CHUONG` (span: `[14:16]`)
- `[e5]` **Điều 12 . Khối , Cụm , Vùng , Nhóm thi đua ngành Kế hoạch và Đầu tư** → `DIEU` (span: `[17:32]`)
- `[e6]` **ngành Kế hoạch và Đầu tư** → `LINH_VUC` (span: `[28:32]`) *(lồng trong `e5` (`DIEU`))*

**Quan hệ:**
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Khoa học và công nghệ `[LINH_VUC]`)
- (`e4` Chương III `[CHUONG]`) ==[ **THUOC_VE** ]==> (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`)
- (`e5` Điều 12 . Khối , Cụm , Vùng , Nhóm thi đua ngành Kế hoạch và Đầu tư `[DIEU]`) ==[ **THUOC_VE** ]==> (`e4` Chương III `[CHUONG]`)
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Khoa học và công nghệ `[LINH_VUC]`)
- (`e5` Điều 12 . Khối , Cụm , Vùng , Nhóm thi đua ngành Kế hoạch và Đầu tư `[DIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Khoa học và công nghệ `[LINH_VUC]`)
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e6` ngành Kế hoạch và Đầu tư `[LINH_VUC]`)
- (`e5` Điều 12 . Khối , Cụm , Vùng , Nhóm thi đua ngành Kế hoạch và Đầu tư `[DIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e6` ngành Kế hoạch và Đầu tư `[LINH_VUC]`) *(Quan hệ lồng nhau)*


---

### Mẫu #06_2012_TT-BKHĐT_27861#body_context_73 (Loại: `body_context`)
> **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[06/2012/TT-BKHĐT]`<SO_HIEU>`** . **[Điều 12]`<DIEU>`** . **[Khoản 1 . Các Khối , Cụm , Vùng , Nhóm thi đua trong **[ngành Kế hoạch và Đầu tư]`<LINH_VUC>`** được tổ chức như sau]`<KHOAN>`** : **[a ) Khối thi đua các đơn vị thuộc Bộ : Gồm 04 khối .]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[5:6]`)
- `[e1]` **06/2012/TT-BKHĐT** → `SO_HIEU` (span: `[7:8]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[0:4]`)
- `[e3]` **Điều 12** → `DIEU` (span: `[9:11]`)
- `[e4]` **Khoản 1 . Các Khối , Cụm , Vùng , Nhóm thi đua trong ngành Kế hoạch và Đầu tư được tổ chức như sau** → `KHOAN` (span: `[12:33]`)
- `[e5]` **a ) Khối thi đua các đơn vị thuộc Bộ : Gồm 04 khối .** → `DIEM` (span: `[34:47]`)
- `[e6]` **ngành Kế hoạch và Đầu tư** → `LINH_VUC` (span: `[25:29]`) *(lồng trong `e4` (`KHOAN`))*

**Quan hệ:**
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 12 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`)
- (`e4` Khoản 1 . Các Khối , Cụm , Vùng , Nhóm thi đua trong ngành Kế hoạch và Đầu tư được tổ chức như sau `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 12 `[DIEU]`)
- (`e5` a ) Khối thi đua các đơn vị thuộc Bộ : Gồm 04 khối . `[DIEM]`) ==[ **THUOC_VE** ]==> (`e4` Khoản 1 . Các Khối , Cụm , Vùng , Nhóm thi đua trong ngành Kế hoạch và Đầu tư được tổ chức như sau `[KHOAN]`)
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e6` ngành Kế hoạch và Đầu tư `[LINH_VUC]`)
- (`e5` a ) Khối thi đua các đơn vị thuộc Bộ : Gồm 04 khối . `[DIEM]`) ==[ **THUOC_LINH_VUC** ]==> (`e6` ngành Kế hoạch và Đầu tư `[LINH_VUC]`)


---

### Mẫu #06_2012_TT-BKHĐT_27861#body_standalone_74 (Loại: `body_standalone`)
> **[Điều 12]`<DIEU>`** . **[Khoản 1 . Các Khối , Cụm , Vùng , Nhóm thi đua trong **[ngành Kế hoạch và Đầu tư]`<LINH_VUC>`** được tổ chức như sau]`<KHOAN>`** : **[a ) Khối thi đua các đơn vị thuộc Bộ : Gồm 04 khối .]`<DIEM>`**

**Thực thể:**
- `[e0]` **Điều 12** → `DIEU` (span: `[0:2]`)
- `[e1]` **Khoản 1 . Các Khối , Cụm , Vùng , Nhóm thi đua trong ngành Kế hoạch và Đầu tư được tổ chức như sau** → `KHOAN` (span: `[3:24]`)
- `[e2]` **a ) Khối thi đua các đơn vị thuộc Bộ : Gồm 04 khối .** → `DIEM` (span: `[25:38]`)
- `[e3]` **ngành Kế hoạch và Đầu tư** → `LINH_VUC` (span: `[16:20]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` Khoản 1 . Các Khối , Cụm , Vùng , Nhóm thi đua trong ngành Kế hoạch và Đầu tư được tổ chức như sau `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 12 `[DIEU]`)
- (`e2` a ) Khối thi đua các đơn vị thuộc Bộ : Gồm 04 khối . `[DIEM]`) ==[ **THUOC_VE** ]==> (`e1` Khoản 1 . Các Khối , Cụm , Vùng , Nhóm thi đua trong ngành Kế hoạch và Đầu tư được tổ chức như sau `[KHOAN]`)
- (`e2` a ) Khối thi đua các đơn vị thuộc Bộ : Gồm 04 khối . `[DIEM]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` ngành Kế hoạch và Đầu tư `[LINH_VUC]`)


---

### Mẫu #06_2012_TT-BKHĐT_27861#body_context_75 (Loại: `body_context`)
> **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[06/2012/TT-BKHĐT]`<SO_HIEU>`** . **[Điều 12]`<DIEU>`** . **[Khoản 1 . Các Khối , Cụm , Vùng , Nhóm thi đua trong **[ngành Kế hoạch và Đầu tư]`<LINH_VUC>`** được tổ chức như sau]`<KHOAN>`** : **[b ) Cụm thi đua các Sở : Gồm 09 cụm .]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[5:6]`)
- `[e1]` **06/2012/TT-BKHĐT** → `SO_HIEU` (span: `[7:8]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[0:4]`)
- `[e3]` **Điều 12** → `DIEU` (span: `[9:11]`)
- `[e4]` **Khoản 1 . Các Khối , Cụm , Vùng , Nhóm thi đua trong ngành Kế hoạch và Đầu tư được tổ chức như sau** → `KHOAN` (span: `[12:33]`)
- `[e5]` **b ) Cụm thi đua các Sở : Gồm 09 cụm .** → `DIEM` (span: `[34:45]`)
- `[e6]` **ngành Kế hoạch và Đầu tư** → `LINH_VUC` (span: `[25:29]`) *(lồng trong `e4` (`KHOAN`))*

**Quan hệ:**
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 12 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`)
- (`e4` Khoản 1 . Các Khối , Cụm , Vùng , Nhóm thi đua trong ngành Kế hoạch và Đầu tư được tổ chức như sau `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 12 `[DIEU]`)
- (`e5` b ) Cụm thi đua các Sở : Gồm 09 cụm . `[DIEM]`) ==[ **THUOC_VE** ]==> (`e4` Khoản 1 . Các Khối , Cụm , Vùng , Nhóm thi đua trong ngành Kế hoạch và Đầu tư được tổ chức như sau `[KHOAN]`)
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e6` ngành Kế hoạch và Đầu tư `[LINH_VUC]`)
- (`e5` b ) Cụm thi đua các Sở : Gồm 09 cụm . `[DIEM]`) ==[ **THUOC_LINH_VUC** ]==> (`e6` ngành Kế hoạch và Đầu tư `[LINH_VUC]`)


---

### Mẫu #06_2012_TT-BKHĐT_27861#body_context_76 (Loại: `body_context`)
> **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[06/2012/TT-BKHĐT]`<SO_HIEU>`** . **[Điều 15]`<DIEU>`** . **[Khoản 4 . Danh hiệu “ Cờ thi đua của **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** ”]`<KHOAN>`** : **[b ) Nội bộ đoàn kết , đi đầu trong thực hành tiết kiệm , chống lãng phí , tham nhũng và các tệ nạn xã hội khác .]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[5:6]`)
- `[e1]` **06/2012/TT-BKHĐT** → `SO_HIEU` (span: `[7:8]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[0:4]`)
- `[e3]` **Điều 15** → `DIEU` (span: `[9:11]`)
- `[e4]` **Khoản 4 . Danh hiệu “ Cờ thi đua của Chính phủ ”** → `KHOAN` (span: `[12:22]`)
- `[e5]` **b ) Nội bộ đoàn kết , đi đầu trong thực hành tiết kiệm , chống lãng phí , tham nhũng và các tệ nạn xã hội khác .** → `DIEM` (span: `[23:44]`)
- `[e6]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[20:21]`) *(lồng trong `e4` (`KHOAN`))*

**Quan hệ:**
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 15 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`)
- (`e4` Khoản 4 . Danh hiệu “ Cờ thi đua của Chính phủ ” `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 15 `[DIEU]`)
- (`e5` b ) Nội bộ đoàn kết , đi đầu trong thực hành tiết kiệm , chống lãng phí , tham nhũng và các tệ nạn xã hội khác . `[DIEM]`) ==[ **THUOC_VE** ]==> (`e4` Khoản 4 . Danh hiệu “ Cờ thi đua của Chính phủ ” `[KHOAN]`)


---

### Mẫu #06_2012_TT-BKHĐT_27861#body_context_77 (Loại: `body_context`)
> **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[06/2012/TT-BKHĐT]`<SO_HIEU>`** . **[Điều 17]`<DIEU>`** . **[Khoản 2 . Hình thức khen thưởng của Bộ]`<KHOAN>`** : **[b ) **[Kỷ niệm chương]`<GIAY_TO_HO_SO>`** " Vì sự nghiệp **[ngành Kế hoạch và Đầu tư Việt Nam]`<LINH_VUC>`** ” và **[kỷ niệm chương]`<GIAY_TO_HO_SO>`** " Vì sự nghiệp Thống kê Việt Nam ” .]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[5:6]`)
- `[e1]` **06/2012/TT-BKHĐT** → `SO_HIEU` (span: `[7:8]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[0:4]`)
- `[e3]` **Điều 17** → `DIEU` (span: `[9:11]`)
- `[e4]` **Khoản 2 . Hình thức khen thưởng của Bộ** → `KHOAN` (span: `[12:19]`)
- `[e5]` **b ) Kỷ niệm chương " Vì sự nghiệp ngành Kế hoạch và Đầu tư Việt Nam ” và kỷ niệm chương " Vì sự nghiệp Thống kê Việt Nam ” .** → `DIEM` (span: `[20:43]`)
- `[e6]` **ngành Kế hoạch và Đầu tư Việt Nam** → `LINH_VUC` (span: `[27:32]`) *(lồng trong `e5` (`DIEM`))*
- `[e7]` **Kỷ niệm chương** → `GIAY_TO_HO_SO` (span: `[22:24]`) *(lồng trong `e5` (`DIEM`))*
- `[e8]` **kỷ niệm chương** → `GIAY_TO_HO_SO` (span: `[34:36]`) *(lồng trong `e5` (`DIEM`))*

**Quan hệ:**
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 17 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`)
- (`e4` Khoản 2 . Hình thức khen thưởng của Bộ `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 17 `[DIEU]`)
- (`e5` b ) Kỷ niệm chương " Vì sự nghiệp ngành Kế hoạch và Đầu tư Việt Nam ” và kỷ niệm chương " Vì sự nghiệp Thống kê Việt Nam ” . `[DIEM]`) ==[ **THUOC_VE** ]==> (`e4` Khoản 2 . Hình thức khen thưởng của Bộ `[KHOAN]`)
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e6` ngành Kế hoạch và Đầu tư Việt Nam `[LINH_VUC]`)
- (`e5` b ) Kỷ niệm chương " Vì sự nghiệp ngành Kế hoạch và Đầu tư Việt Nam ” và kỷ niệm chương " Vì sự nghiệp Thống kê Việt Nam ” . `[DIEM]`) ==[ **THUOC_LINH_VUC** ]==> (`e6` ngành Kế hoạch và Đầu tư Việt Nam `[LINH_VUC]`) *(Quan hệ lồng nhau)*


---

### Mẫu #06_2012_TT-BKHĐT_27861#body_standalone_78 (Loại: `body_standalone`)
> **[Điều 17]`<DIEU>`** . **[Khoản 2 . Hình thức khen thưởng của Bộ]`<KHOAN>`** : **[b ) **[Kỷ niệm chương]`<GIAY_TO_HO_SO>`** " Vì sự nghiệp **[ngành Kế hoạch và Đầu tư Việt Nam]`<LINH_VUC>`** ” và **[kỷ niệm chương]`<GIAY_TO_HO_SO>`** " Vì sự nghiệp Thống kê Việt Nam ” .]`<DIEM>`**

**Thực thể:**
- `[e0]` **Điều 17** → `DIEU` (span: `[0:2]`)
- `[e1]` **Khoản 2 . Hình thức khen thưởng của Bộ** → `KHOAN` (span: `[3:10]`)
- `[e2]` **b ) Kỷ niệm chương " Vì sự nghiệp ngành Kế hoạch và Đầu tư Việt Nam ” và kỷ niệm chương " Vì sự nghiệp Thống kê Việt Nam ” .** → `DIEM` (span: `[11:34]`)
- `[e3]` **ngành Kế hoạch và Đầu tư Việt Nam** → `LINH_VUC` (span: `[18:23]`) *(lồng trong `e2` (`DIEM`))*
- `[e4]` **Kỷ niệm chương** → `GIAY_TO_HO_SO` (span: `[13:15]`) *(lồng trong `e2` (`DIEM`))*
- `[e5]` **kỷ niệm chương** → `GIAY_TO_HO_SO` (span: `[25:27]`) *(lồng trong `e2` (`DIEM`))*

**Quan hệ:**
- (`e1` Khoản 2 . Hình thức khen thưởng của Bộ `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 17 `[DIEU]`)
- (`e2` b ) Kỷ niệm chương " Vì sự nghiệp ngành Kế hoạch và Đầu tư Việt Nam ” và kỷ niệm chương " Vì sự nghiệp Thống kê Việt Nam ” . `[DIEM]`) ==[ **THUOC_VE** ]==> (`e1` Khoản 2 . Hình thức khen thưởng của Bộ `[KHOAN]`)
- (`e2` b ) Kỷ niệm chương " Vì sự nghiệp ngành Kế hoạch và Đầu tư Việt Nam ” và kỷ niệm chương " Vì sự nghiệp Thống kê Việt Nam ” . `[DIEM]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` ngành Kế hoạch và Đầu tư Việt Nam `[LINH_VUC]`) *(Quan hệ lồng nhau)*


---

### Mẫu #06_2012_TT-BKHĐT_27861#body_context_79 (Loại: `body_context`)
> **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[06/2012/TT-BKHĐT]`<SO_HIEU>`** . **[Điều 19]`<DIEU>`** . **[Khoản 1 . " Bằng khen của Bộ trưởng "]`<KHOAN>`** : **[e ) Tặng cho các tập thể , cá nhân ngoài **[ngành Kế hoạch và Đầu tư]`<LINH_VUC>`** ( trong và ngoài nước ) có thành tích xuất sắc , đóng góp cho sự nghiệp xây dựng và phát triển **[ngành Kế hoạch và Đầu tư]`<LINH_VUC>`** .]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[5:6]`)
- `[e1]` **06/2012/TT-BKHĐT** → `SO_HIEU` (span: `[7:8]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[0:4]`)
- `[e3]` **Điều 19** → `DIEU` (span: `[9:11]`)
- `[e4]` **Khoản 1 . " Bằng khen của Bộ trưởng "** → `KHOAN` (span: `[12:20]`)
- `[e5]` **e ) Tặng cho các tập thể , cá nhân ngoài ngành Kế hoạch và Đầu tư ( trong và ngoài nước ) có thành tích xuất sắc , đóng góp cho sự nghiệp xây dựng và phát triển ngành Kế hoạch và Đầu tư .** → `DIEM` (span: `[21:55]`)
- `[e6]` **ngành Kế hoạch và Đầu tư** → `LINH_VUC` (span: `[30:34]`) *(lồng trong `e5` (`DIEM`))*
- `[e7]` **ngành Kế hoạch và Đầu tư** → `LINH_VUC` (span: `[50:54]`) *(lồng trong `e5` (`DIEM`))*

**Quan hệ:**
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 19 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`)
- (`e4` Khoản 1 . " Bằng khen của Bộ trưởng " `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 19 `[DIEU]`)
- (`e5` e ) Tặng cho các tập thể , cá nhân ngoài ngành Kế hoạch và Đầu tư ( trong và ngoài nước ) có thành tích xuất sắc , đóng góp cho sự nghiệp xây dựng và phát triển ngành Kế hoạch và Đầu tư . `[DIEM]`) ==[ **THUOC_VE** ]==> (`e4` Khoản 1 . " Bằng khen của Bộ trưởng " `[KHOAN]`)
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e6` ngành Kế hoạch và Đầu tư `[LINH_VUC]`)
- (`e5` e ) Tặng cho các tập thể , cá nhân ngoài ngành Kế hoạch và Đầu tư ( trong và ngoài nước ) có thành tích xuất sắc , đóng góp cho sự nghiệp xây dựng và phát triển ngành Kế hoạch và Đầu tư . `[DIEM]`) ==[ **THUOC_LINH_VUC** ]==> (`e6` ngành Kế hoạch và Đầu tư `[LINH_VUC]`) *(Quan hệ lồng nhau)*
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e7` ngành Kế hoạch và Đầu tư `[LINH_VUC]`)
- (`e5` e ) Tặng cho các tập thể , cá nhân ngoài ngành Kế hoạch và Đầu tư ( trong và ngoài nước ) có thành tích xuất sắc , đóng góp cho sự nghiệp xây dựng và phát triển ngành Kế hoạch và Đầu tư . `[DIEM]`) ==[ **THUOC_LINH_VUC** ]==> (`e7` ngành Kế hoạch và Đầu tư `[LINH_VUC]`) *(Quan hệ lồng nhau)*


---

### Mẫu #06_2012_TT-BKHĐT_27861#body_standalone_80 (Loại: `body_standalone`)
> **[Điều 19]`<DIEU>`** . **[Khoản 1 . " Bằng khen của Bộ trưởng "]`<KHOAN>`** : **[e ) Tặng cho các tập thể , cá nhân ngoài **[ngành Kế hoạch và Đầu tư]`<LINH_VUC>`** ( trong và ngoài nước ) có thành tích xuất sắc , đóng góp cho sự nghiệp xây dựng và phát triển **[ngành Kế hoạch và Đầu tư]`<LINH_VUC>`** .]`<DIEM>`**

**Thực thể:**
- `[e0]` **Điều 19** → `DIEU` (span: `[0:2]`)
- `[e1]` **Khoản 1 . " Bằng khen của Bộ trưởng "** → `KHOAN` (span: `[3:11]`)
- `[e2]` **e ) Tặng cho các tập thể , cá nhân ngoài ngành Kế hoạch và Đầu tư ( trong và ngoài nước ) có thành tích xuất sắc , đóng góp cho sự nghiệp xây dựng và phát triển ngành Kế hoạch và Đầu tư .** → `DIEM` (span: `[12:46]`)
- `[e3]` **ngành Kế hoạch và Đầu tư** → `LINH_VUC` (span: `[21:25]`) *(lồng trong `e2` (`DIEM`))*
- `[e4]` **ngành Kế hoạch và Đầu tư** → `LINH_VUC` (span: `[41:45]`) *(lồng trong `e2` (`DIEM`))*

**Quan hệ:**
- (`e1` Khoản 1 . " Bằng khen của Bộ trưởng " `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 19 `[DIEU]`)
- (`e2` e ) Tặng cho các tập thể , cá nhân ngoài ngành Kế hoạch và Đầu tư ( trong và ngoài nước ) có thành tích xuất sắc , đóng góp cho sự nghiệp xây dựng và phát triển ngành Kế hoạch và Đầu tư . `[DIEM]`) ==[ **THUOC_VE** ]==> (`e1` Khoản 1 . " Bằng khen của Bộ trưởng " `[KHOAN]`)
- (`e2` e ) Tặng cho các tập thể , cá nhân ngoài ngành Kế hoạch và Đầu tư ( trong và ngoài nước ) có thành tích xuất sắc , đóng góp cho sự nghiệp xây dựng và phát triển ngành Kế hoạch và Đầu tư . `[DIEM]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` ngành Kế hoạch và Đầu tư `[LINH_VUC]`) *(Quan hệ lồng nhau)*
- (`e2` e ) Tặng cho các tập thể , cá nhân ngoài ngành Kế hoạch và Đầu tư ( trong và ngoài nước ) có thành tích xuất sắc , đóng góp cho sự nghiệp xây dựng và phát triển ngành Kế hoạch và Đầu tư . `[DIEM]`) ==[ **THUOC_LINH_VUC** ]==> (`e4` ngành Kế hoạch và Đầu tư `[LINH_VUC]`) *(Quan hệ lồng nhau)*


---

### Mẫu #06_2012_TT-BKHĐT_27861#body_context_81 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[06/2012/TT-BKHĐT]`<SO_HIEU>`** của **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Khoa học và công nghệ]`<LINH_VUC>`** . **[Điều 21]`<DIEU>`** . **[5 . Đối với các đơn vị trực thuộc Tổng cục Thống kê : Tổ chức họp , bình bầu theo Quy chế Thi đua - Khen thưởng của **[ngành Thống kê]`<LINH_VUC>`** . Quyết định các danh hiệu thi đua theo thẩm quyền quy định ; trình Hội đồng Thi đua - Khen thưởng Bộ ( qua Vụ Thi đua - Khen thưởng ) xem xét , quyết định đối với các danh hiệu thi đua và hình thức khen thưởng bậc cao .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **06/2012/TT-BKHĐT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[4:8]`)
- `[e3]` **Khoa học và công nghệ** → `LINH_VUC` (span: `[10:13]`)
- `[e4]` **Điều 21** → `DIEU` (span: `[14:16]`)
- `[e5]` **5 . Đối với các đơn vị trực thuộc Tổng cục Thống kê : Tổ chức họp , bình bầu theo Quy chế Thi đua - Khen thưởng của ngành Thống kê . Quyết định các danh hiệu thi đua theo thẩm quyền quy định ; trình Hội đồng Thi đua - Khen thưởng Bộ ( qua Vụ Thi đua - Khen thưởng ) xem xét , quyết định đối với các danh hiệu thi đua và hình thức khen thưởng bậc cao .** → `KHOAN` (span: `[17:73]`)
- `[e6]` **ngành Thống kê** → `LINH_VUC` (span: `[36:38]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Khoa học và công nghệ `[LINH_VUC]`)
- (`e4` Điều 21 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`)
- (`e5` 5 . Đối với các đơn vị trực thuộc Tổng cục Thống kê : Tổ chức họp , bình bầu theo Quy chế Thi đua - Khen thưởng của ngành Thống kê . Quyết định các danh hiệu thi đua theo thẩm quyền quy định ; trình Hội đồng Thi đua - Khen thưởng Bộ ( qua Vụ Thi đua - Khen thưởng ) xem xét , quyết định đối với các danh hiệu thi đua và hình thức khen thưởng bậc cao . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 21 `[DIEU]`)
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Khoa học và công nghệ `[LINH_VUC]`)
- (`e5` 5 . Đối với các đơn vị trực thuộc Tổng cục Thống kê : Tổ chức họp , bình bầu theo Quy chế Thi đua - Khen thưởng của ngành Thống kê . Quyết định các danh hiệu thi đua theo thẩm quyền quy định ; trình Hội đồng Thi đua - Khen thưởng Bộ ( qua Vụ Thi đua - Khen thưởng ) xem xét , quyết định đối với các danh hiệu thi đua và hình thức khen thưởng bậc cao . `[KHOAN]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Khoa học và công nghệ `[LINH_VUC]`)
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e6` ngành Thống kê `[LINH_VUC]`)
- (`e5` 5 . Đối với các đơn vị trực thuộc Tổng cục Thống kê : Tổ chức họp , bình bầu theo Quy chế Thi đua - Khen thưởng của ngành Thống kê . Quyết định các danh hiệu thi đua theo thẩm quyền quy định ; trình Hội đồng Thi đua - Khen thưởng Bộ ( qua Vụ Thi đua - Khen thưởng ) xem xét , quyết định đối với các danh hiệu thi đua và hình thức khen thưởng bậc cao . `[KHOAN]`) ==[ **THUOC_LINH_VUC** ]==> (`e6` ngành Thống kê `[LINH_VUC]`) *(Quan hệ lồng nhau)*


---

### Mẫu #06_2012_TT-BKHĐT_27861#body_context_82 (Loại: `body_context`)
> **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[06/2012/TT-BKHĐT]`<SO_HIEU>`** . **[Điều 22]`<DIEU>`** . **[1 . Chủ tịch nước và **[Thủ tướng Chính phủ]`<CO_QUAN_THAM_QUYEN>`** quyết định tặng : ' ‘ Huân chương ” , “ Huy chương ” , " Giải thưởng Hồ Chí Minh " , " Giải thưởng Nhà nước " , “ Danh hiệu vinh dự Nhà nước ” ; danh hiệu " Cờ thi đua của **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** " , danh hiệu " Chiến sĩ thi đua toàn quốc " , " Bằng khen của **[Thủ tướng Chính phủ]`<CO_QUAN_THAM_QUYEN>`** " được thực hiện **[theo quy định tại]`<TU_KHOA_PHAP_LY>`** **[các Điều 77 và 78]`<THAM_CHIEU_PHAP_LY>`** của Luật Thi đua , Khen thưởng .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[5:6]`)
- `[e1]` **06/2012/TT-BKHĐT** → `SO_HIEU` (span: `[7:8]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[0:4]`)
- `[e3]` **Điều 22** → `DIEU` (span: `[9:11]`)
- `[e4]` **1 . Chủ tịch nước và Thủ tướng Chính phủ quyết định tặng : ' ‘ Huân chương ” , “ Huy chương ” , " Giải thưởng Hồ Chí Minh " , " Giải thưởng Nhà nước " , “ Danh hiệu vinh dự Nhà nước ” ; danh hiệu " Cờ thi đua của Chính phủ " , danh hiệu " Chiến sĩ thi đua toàn quốc " , " Bằng khen của Thủ tướng Chính phủ " được thực hiện theo quy định tại các Điều 77 và 78 của Luật Thi đua , Khen thưởng .** → `KHOAN` (span: `[12:84]`)
- `[e5]` **các Điều 77 và 78** → `THAM_CHIEU_PHAP_LY` (span: `[73:78]`) *(lồng trong `e4` (`KHOAN`))*
- `[e6]` **theo quy định tại** → `TU_KHOA_PHAP_LY` (span: `[70:73]`) *(lồng trong `e4` (`KHOAN`))*
- `[e7]` **Thủ tướng Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[17:19]`) *(lồng trong `e4` (`KHOAN`))*
- `[e8]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[52:53]`) *(lồng trong `e4` (`KHOAN`))*
- `[e9]` **Thủ tướng Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[65:67]`) *(lồng trong `e4` (`KHOAN`))*

**Quan hệ:**
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 22 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`)
- (`e4` 1 . Chủ tịch nước và Thủ tướng Chính phủ quyết định tặng : ' ‘ Huân chương ” , “ Huy chương ” , " Giải thưởng Hồ Chí Minh " , " Giải thưởng Nhà nước " , “ Danh hiệu vinh dự Nhà nước ” ; danh hiệu " Cờ thi đua của Chính phủ " , danh hiệu " Chiến sĩ thi đua toàn quốc " , " Bằng khen của Thủ tướng Chính phủ " được thực hiện theo quy định tại các Điều 77 và 78 của Luật Thi đua , Khen thưởng . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 22 `[DIEU]`)
- (`e6` theo quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e5` các Điều 77 và 78 `[THAM_CHIEU_PHAP_LY]`)
- (`e4` 1 . Chủ tịch nước và Thủ tướng Chính phủ quyết định tặng : ' ‘ Huân chương ” , “ Huy chương ” , " Giải thưởng Hồ Chí Minh " , " Giải thưởng Nhà nước " , “ Danh hiệu vinh dự Nhà nước ” ; danh hiệu " Cờ thi đua của Chính phủ " , danh hiệu " Chiến sĩ thi đua toàn quốc " , " Bằng khen của Thủ tướng Chính phủ " được thực hiện theo quy định tại các Điều 77 và 78 của Luật Thi đua , Khen thưởng . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e5` các Điều 77 và 78 `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #06_2012_TT-BKHĐT_27861#body_standalone_83 (Loại: `body_standalone`)
> **[Điều 22]`<DIEU>`** . **[1 . Chủ tịch nước và **[Thủ tướng Chính phủ]`<CO_QUAN_THAM_QUYEN>`** quyết định tặng : ' ‘ Huân chương ” , “ Huy chương ” , " Giải thưởng Hồ Chí Minh " , " Giải thưởng Nhà nước " , “ Danh hiệu vinh dự Nhà nước ” ; danh hiệu " Cờ thi đua của **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** " , danh hiệu " Chiến sĩ thi đua toàn quốc " , " Bằng khen của **[Thủ tướng Chính phủ]`<CO_QUAN_THAM_QUYEN>`** " được thực hiện **[theo quy định tại]`<TU_KHOA_PHAP_LY>`** **[các Điều 77 và 78]`<THAM_CHIEU_PHAP_LY>`** của Luật Thi đua , Khen thưởng .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 22** → `DIEU` (span: `[0:2]`)
- `[e1]` **1 . Chủ tịch nước và Thủ tướng Chính phủ quyết định tặng : ' ‘ Huân chương ” , “ Huy chương ” , " Giải thưởng Hồ Chí Minh " , " Giải thưởng Nhà nước " , “ Danh hiệu vinh dự Nhà nước ” ; danh hiệu " Cờ thi đua của Chính phủ " , danh hiệu " Chiến sĩ thi đua toàn quốc " , " Bằng khen của Thủ tướng Chính phủ " được thực hiện theo quy định tại các Điều 77 và 78 của Luật Thi đua , Khen thưởng .** → `KHOAN` (span: `[3:75]`)
- `[e2]` **các Điều 77 và 78** → `THAM_CHIEU_PHAP_LY` (span: `[64:69]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **theo quy định tại** → `TU_KHOA_PHAP_LY` (span: `[61:64]`) *(lồng trong `e1` (`KHOAN`))*
- `[e4]` **Thủ tướng Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[8:10]`) *(lồng trong `e1` (`KHOAN`))*
- `[e5]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[43:44]`) *(lồng trong `e1` (`KHOAN`))*
- `[e6]` **Thủ tướng Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[56:58]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 1 . Chủ tịch nước và Thủ tướng Chính phủ quyết định tặng : ' ‘ Huân chương ” , “ Huy chương ” , " Giải thưởng Hồ Chí Minh " , " Giải thưởng Nhà nước " , “ Danh hiệu vinh dự Nhà nước ” ; danh hiệu " Cờ thi đua của Chính phủ " , danh hiệu " Chiến sĩ thi đua toàn quốc " , " Bằng khen của Thủ tướng Chính phủ " được thực hiện theo quy định tại các Điều 77 và 78 của Luật Thi đua , Khen thưởng . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 22 `[DIEU]`)
- (`e3` theo quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e2` các Điều 77 và 78 `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 1 . Chủ tịch nước và Thủ tướng Chính phủ quyết định tặng : ' ‘ Huân chương ” , “ Huy chương ” , " Giải thưởng Hồ Chí Minh " , " Giải thưởng Nhà nước " , “ Danh hiệu vinh dự Nhà nước ” ; danh hiệu " Cờ thi đua của Chính phủ " , danh hiệu " Chiến sĩ thi đua toàn quốc " , " Bằng khen của Thủ tướng Chính phủ " được thực hiện theo quy định tại các Điều 77 và 78 của Luật Thi đua , Khen thưởng . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e2` các Điều 77 và 78 `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #06_2012_TT-BKHĐT_27861#body_context_84 (Loại: `body_context`)
> **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[06/2012/TT-BKHĐT]`<SO_HIEU>`** . **[Điều 22]`<DIEU>`** . **[Khoản 2 . Bộ trưởng quyết định]`<KHOAN>`** : **[f ) Tặng “ Bằng khen của Bộ trưởng ” và “ **[Kỷ niệm chương]`<GIAY_TO_HO_SO>`** “ Vì sự nghiệp **[ngành Kế hoạch và Đầu tư Việt Nam]`<LINH_VUC>`** ” ; **[Kỷ niệm chương]`<GIAY_TO_HO_SO>`** “ Vì sự nghiệp Thống kê Việt Nam cho các tập thể , cá nhân ngoài ngành ( khen đối ngoại ) .]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[5:6]`)
- `[e1]` **06/2012/TT-BKHĐT** → `SO_HIEU` (span: `[7:8]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[0:4]`)
- `[e3]` **Điều 22** → `DIEU` (span: `[9:11]`)
- `[e4]` **Khoản 2 . Bộ trưởng quyết định** → `KHOAN` (span: `[12:17]`)
- `[e5]` **f ) Tặng “ Bằng khen của Bộ trưởng ” và “ Kỷ niệm chương “ Vì sự nghiệp ngành Kế hoạch và Đầu tư Việt Nam ” ; Kỷ niệm chương “ Vì sự nghiệp Thống kê Việt Nam cho các tập thể , cá nhân ngoài ngành ( khen đối ngoại ) .** → `DIEM` (span: `[18:59]`)
- `[e6]` **ngành Kế hoạch và Đầu tư Việt Nam** → `LINH_VUC` (span: `[33:38]`) *(lồng trong `e5` (`DIEM`))*
- `[e7]` **Kỷ niệm chương** → `GIAY_TO_HO_SO` (span: `[28:30]`) *(lồng trong `e5` (`DIEM`))*
- `[e8]` **Kỷ niệm chương** → `GIAY_TO_HO_SO` (span: `[40:42]`) *(lồng trong `e5` (`DIEM`))*

**Quan hệ:**
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 22 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`)
- (`e4` Khoản 2 . Bộ trưởng quyết định `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 22 `[DIEU]`)
- (`e5` f ) Tặng “ Bằng khen của Bộ trưởng ” và “ Kỷ niệm chương “ Vì sự nghiệp ngành Kế hoạch và Đầu tư Việt Nam ” ; Kỷ niệm chương “ Vì sự nghiệp Thống kê Việt Nam cho các tập thể , cá nhân ngoài ngành ( khen đối ngoại ) . `[DIEM]`) ==[ **THUOC_VE** ]==> (`e4` Khoản 2 . Bộ trưởng quyết định `[KHOAN]`)
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e6` ngành Kế hoạch và Đầu tư Việt Nam `[LINH_VUC]`)
- (`e5` f ) Tặng “ Bằng khen của Bộ trưởng ” và “ Kỷ niệm chương “ Vì sự nghiệp ngành Kế hoạch và Đầu tư Việt Nam ” ; Kỷ niệm chương “ Vì sự nghiệp Thống kê Việt Nam cho các tập thể , cá nhân ngoài ngành ( khen đối ngoại ) . `[DIEM]`) ==[ **THUOC_LINH_VUC** ]==> (`e6` ngành Kế hoạch và Đầu tư Việt Nam `[LINH_VUC]`) *(Quan hệ lồng nhau)*


---

### Mẫu #06_2012_TT-BKHĐT_27861#body_standalone_85 (Loại: `body_standalone`)
> **[Điều 22]`<DIEU>`** . **[Khoản 2 . Bộ trưởng quyết định]`<KHOAN>`** : **[f ) Tặng “ Bằng khen của Bộ trưởng ” và “ **[Kỷ niệm chương]`<GIAY_TO_HO_SO>`** “ Vì sự nghiệp **[ngành Kế hoạch và Đầu tư Việt Nam]`<LINH_VUC>`** ” ; **[Kỷ niệm chương]`<GIAY_TO_HO_SO>`** “ Vì sự nghiệp Thống kê Việt Nam cho các tập thể , cá nhân ngoài ngành ( khen đối ngoại ) .]`<DIEM>`**

**Thực thể:**
- `[e0]` **Điều 22** → `DIEU` (span: `[0:2]`)
- `[e1]` **Khoản 2 . Bộ trưởng quyết định** → `KHOAN` (span: `[3:8]`)
- `[e2]` **f ) Tặng “ Bằng khen của Bộ trưởng ” và “ Kỷ niệm chương “ Vì sự nghiệp ngành Kế hoạch và Đầu tư Việt Nam ” ; Kỷ niệm chương “ Vì sự nghiệp Thống kê Việt Nam cho các tập thể , cá nhân ngoài ngành ( khen đối ngoại ) .** → `DIEM` (span: `[9:50]`)
- `[e3]` **ngành Kế hoạch và Đầu tư Việt Nam** → `LINH_VUC` (span: `[24:29]`) *(lồng trong `e2` (`DIEM`))*
- `[e4]` **Kỷ niệm chương** → `GIAY_TO_HO_SO` (span: `[19:21]`) *(lồng trong `e2` (`DIEM`))*
- `[e5]` **Kỷ niệm chương** → `GIAY_TO_HO_SO` (span: `[31:33]`) *(lồng trong `e2` (`DIEM`))*

**Quan hệ:**
- (`e1` Khoản 2 . Bộ trưởng quyết định `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 22 `[DIEU]`)
- (`e2` f ) Tặng “ Bằng khen của Bộ trưởng ” và “ Kỷ niệm chương “ Vì sự nghiệp ngành Kế hoạch và Đầu tư Việt Nam ” ; Kỷ niệm chương “ Vì sự nghiệp Thống kê Việt Nam cho các tập thể , cá nhân ngoài ngành ( khen đối ngoại ) . `[DIEM]`) ==[ **THUOC_VE** ]==> (`e1` Khoản 2 . Bộ trưởng quyết định `[KHOAN]`)
- (`e2` f ) Tặng “ Bằng khen của Bộ trưởng ” và “ Kỷ niệm chương “ Vì sự nghiệp ngành Kế hoạch và Đầu tư Việt Nam ” ; Kỷ niệm chương “ Vì sự nghiệp Thống kê Việt Nam cho các tập thể , cá nhân ngoài ngành ( khen đối ngoại ) . `[DIEM]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` ngành Kế hoạch và Đầu tư Việt Nam `[LINH_VUC]`) *(Quan hệ lồng nhau)*


---

### Mẫu #06_2012_TT-BKHĐT_27861#body_context_86 (Loại: `body_context`)
> **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[06/2012/TT-BKHĐT]`<SO_HIEU>`** . **[Điều 24]`<DIEU>`** . **[Khoản 2 . Các cấp trình khen]`<KHOAN>`** : **[d ) Đối với các **[Doanh nghiệp]`<TO_CHUC_DOANH_NGHIEP>`** ( **[quy định tại]`<TU_KHOA_PHAP_LY>`** **[Điều 2]`<THAM_CHIEU_PHAP_LY>`** , Khoản 2 , Mục c ) : Cấp nào **[quyết định thành lập]`<GIAY_TO_HO_SO>`** , **[cấp **[giấy phép kinh doanh]`<GIAY_TO_HO_SO>`**]`<NGHIA_VU_QUYEN>`** , **[cấp **[giấy chứng nhận đầu tư]`<GIAY_TO_HO_SO>`**]`<NGHIA_VU_QUYEN>`** ra nước ngoài hoặc quyết định cổ phần hóa cho **[doanh nghiệp]`<TO_CHUC_DOANH_NGHIEP>`** đó thì cấp đó trình khen thưởng .]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[5:6]`)
- `[e1]` **06/2012/TT-BKHĐT** → `SO_HIEU` (span: `[7:8]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[0:4]`)
- `[e3]` **Điều 24** → `DIEU` (span: `[9:11]`)
- `[e4]` **Khoản 2 . Các cấp trình khen** → `KHOAN` (span: `[12:19]`)
- `[e5]` **d ) Đối với các Doanh nghiệp ( quy định tại Điều 2 , Khoản 2 , Mục c ) : Cấp nào quyết định thành lập , cấp giấy phép kinh doanh , cấp giấy chứng nhận đầu tư ra nước ngoài hoặc quyết định cổ phần hóa cho doanh nghiệp đó thì cấp đó trình khen thưởng .** → `DIEM` (span: `[20:64]`)
- `[e6]` **cấp giấy phép kinh doanh** → `NGHIA_VU_QUYEN` (span: `[42:45]`) *(lồng trong `e5` (`DIEM`))*
- `[e7]` **cấp giấy chứng nhận đầu tư** → `NGHIA_VU_QUYEN` (span: `[46:50]`) *(lồng trong `e5` (`DIEM`))*
- `[e8]` **Điều 2** → `THAM_CHIEU_PHAP_LY` (span: `[28:30]`) *(lồng trong `e5` (`DIEM`))*
- `[e9]` **quy định tại** → `TU_KHOA_PHAP_LY` (span: `[26:28]`) *(lồng trong `e5` (`DIEM`))*
- `[e10]` **quyết định thành lập** → `GIAY_TO_HO_SO` (span: `[39:41]`) *(lồng trong `e5` (`DIEM`))*
- `[e11]` **giấy phép kinh doanh** → `GIAY_TO_HO_SO` (span: `[43:45]`) *(lồng trong `e5` (`DIEM`), `e6` (`NGHIA_VU_QUYEN`))*
- `[e12]` **giấy chứng nhận đầu tư** → `GIAY_TO_HO_SO` (span: `[47:50]`) *(lồng trong `e5` (`DIEM`), `e7` (`NGHIA_VU_QUYEN`))*
- `[e13]` **Doanh nghiệp** → `TO_CHUC_DOANH_NGHIEP` (span: `[24:25]`) *(lồng trong `e5` (`DIEM`))*
- `[e14]` **doanh nghiệp** → `TO_CHUC_DOANH_NGHIEP` (span: `[56:57]`) *(lồng trong `e5` (`DIEM`))*

**Quan hệ:**
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 24 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`)
- (`e4` Khoản 2 . Các cấp trình khen `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 24 `[DIEU]`)
- (`e5` d ) Đối với các Doanh nghiệp ( quy định tại Điều 2 , Khoản 2 , Mục c ) : Cấp nào quyết định thành lập , cấp giấy phép kinh doanh , cấp giấy chứng nhận đầu tư ra nước ngoài hoặc quyết định cổ phần hóa cho doanh nghiệp đó thì cấp đó trình khen thưởng . `[DIEM]`) ==[ **THUOC_VE** ]==> (`e4` Khoản 2 . Các cấp trình khen `[KHOAN]`)
- (`e6` cấp giấy phép kinh doanh `[NGHIA_VU_QUYEN]`) ==[ **TAC_DONG_DOI_TUONG** ]==> (`e11` giấy phép kinh doanh `[GIAY_TO_HO_SO]`) *(Quan hệ lồng nhau)*
- (`e7` cấp giấy chứng nhận đầu tư `[NGHIA_VU_QUYEN]`) ==[ **TAC_DONG_DOI_TUONG** ]==> (`e12` giấy chứng nhận đầu tư `[GIAY_TO_HO_SO]`) *(Quan hệ lồng nhau)*
- (`e13` Doanh nghiệp `[TO_CHUC_DOANH_NGHIEP]`) ==[ **CO_NGHIA_VU_QUYEN** ]==> (`e6` cấp giấy phép kinh doanh `[NGHIA_VU_QUYEN]`)
- (`e7` cấp giấy chứng nhận đầu tư `[NGHIA_VU_QUYEN]`) ==[ **TAC_DONG_CHU_THE** ]==> (`e14` doanh nghiệp `[TO_CHUC_DOANH_NGHIEP]`)
- (`e9` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e8` Điều 2 `[THAM_CHIEU_PHAP_LY]`)
- (`e6` cấp giấy phép kinh doanh `[NGHIA_VU_QUYEN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e8` Điều 2 `[THAM_CHIEU_PHAP_LY]`)
- (`e6` cấp giấy phép kinh doanh `[NGHIA_VU_QUYEN]`) ==[ **TAC_DONG_DOI_TUONG** ]==> (`e10` quyết định thành lập `[GIAY_TO_HO_SO]`)


---

### Mẫu #06_2012_TT-BKHĐT_27861#body_standalone_87 (Loại: `body_standalone`)
> **[Điều 24]`<DIEU>`** . **[Khoản 2 . Các cấp trình khen]`<KHOAN>`** : **[d ) Đối với các **[Doanh nghiệp]`<TO_CHUC_DOANH_NGHIEP>`** ( **[quy định tại]`<TU_KHOA_PHAP_LY>`** **[Điều 2]`<THAM_CHIEU_PHAP_LY>`** , Khoản 2 , Mục c ) : Cấp nào **[quyết định thành lập]`<GIAY_TO_HO_SO>`** , **[cấp **[giấy phép kinh doanh]`<GIAY_TO_HO_SO>`**]`<NGHIA_VU_QUYEN>`** , **[cấp **[giấy chứng nhận đầu tư]`<GIAY_TO_HO_SO>`**]`<NGHIA_VU_QUYEN>`** ra nước ngoài hoặc quyết định cổ phần hóa cho **[doanh nghiệp]`<TO_CHUC_DOANH_NGHIEP>`** đó thì cấp đó trình khen thưởng .]`<DIEM>`**

**Thực thể:**
- `[e0]` **Điều 24** → `DIEU` (span: `[0:2]`)
- `[e1]` **Khoản 2 . Các cấp trình khen** → `KHOAN` (span: `[3:10]`)
- `[e2]` **d ) Đối với các Doanh nghiệp ( quy định tại Điều 2 , Khoản 2 , Mục c ) : Cấp nào quyết định thành lập , cấp giấy phép kinh doanh , cấp giấy chứng nhận đầu tư ra nước ngoài hoặc quyết định cổ phần hóa cho doanh nghiệp đó thì cấp đó trình khen thưởng .** → `DIEM` (span: `[11:55]`)
- `[e3]` **cấp giấy phép kinh doanh** → `NGHIA_VU_QUYEN` (span: `[33:36]`) *(lồng trong `e2` (`DIEM`))*
- `[e4]` **cấp giấy chứng nhận đầu tư** → `NGHIA_VU_QUYEN` (span: `[37:41]`) *(lồng trong `e2` (`DIEM`))*
- `[e5]` **Điều 2** → `THAM_CHIEU_PHAP_LY` (span: `[19:21]`) *(lồng trong `e2` (`DIEM`))*
- `[e6]` **quy định tại** → `TU_KHOA_PHAP_LY` (span: `[17:19]`) *(lồng trong `e2` (`DIEM`))*
- `[e7]` **quyết định thành lập** → `GIAY_TO_HO_SO` (span: `[30:32]`) *(lồng trong `e2` (`DIEM`))*
- `[e8]` **giấy phép kinh doanh** → `GIAY_TO_HO_SO` (span: `[34:36]`) *(lồng trong `e2` (`DIEM`), `e3` (`NGHIA_VU_QUYEN`))*
- `[e9]` **giấy chứng nhận đầu tư** → `GIAY_TO_HO_SO` (span: `[38:41]`) *(lồng trong `e2` (`DIEM`), `e4` (`NGHIA_VU_QUYEN`))*
- `[e10]` **Doanh nghiệp** → `TO_CHUC_DOANH_NGHIEP` (span: `[15:16]`) *(lồng trong `e2` (`DIEM`))*
- `[e11]` **doanh nghiệp** → `TO_CHUC_DOANH_NGHIEP` (span: `[47:48]`) *(lồng trong `e2` (`DIEM`))*

**Quan hệ:**
- (`e1` Khoản 2 . Các cấp trình khen `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 24 `[DIEU]`)
- (`e2` d ) Đối với các Doanh nghiệp ( quy định tại Điều 2 , Khoản 2 , Mục c ) : Cấp nào quyết định thành lập , cấp giấy phép kinh doanh , cấp giấy chứng nhận đầu tư ra nước ngoài hoặc quyết định cổ phần hóa cho doanh nghiệp đó thì cấp đó trình khen thưởng . `[DIEM]`) ==[ **THUOC_VE** ]==> (`e1` Khoản 2 . Các cấp trình khen `[KHOAN]`)
- (`e3` cấp giấy phép kinh doanh `[NGHIA_VU_QUYEN]`) ==[ **TAC_DONG_DOI_TUONG** ]==> (`e8` giấy phép kinh doanh `[GIAY_TO_HO_SO]`) *(Quan hệ lồng nhau)*
- (`e4` cấp giấy chứng nhận đầu tư `[NGHIA_VU_QUYEN]`) ==[ **TAC_DONG_DOI_TUONG** ]==> (`e9` giấy chứng nhận đầu tư `[GIAY_TO_HO_SO]`) *(Quan hệ lồng nhau)*
- (`e10` Doanh nghiệp `[TO_CHUC_DOANH_NGHIEP]`) ==[ **CO_NGHIA_VU_QUYEN** ]==> (`e3` cấp giấy phép kinh doanh `[NGHIA_VU_QUYEN]`)
- (`e4` cấp giấy chứng nhận đầu tư `[NGHIA_VU_QUYEN]`) ==[ **TAC_DONG_CHU_THE** ]==> (`e11` doanh nghiệp `[TO_CHUC_DOANH_NGHIEP]`)
- (`e6` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e5` Điều 2 `[THAM_CHIEU_PHAP_LY]`)
- (`e3` cấp giấy phép kinh doanh `[NGHIA_VU_QUYEN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e5` Điều 2 `[THAM_CHIEU_PHAP_LY]`)
- (`e3` cấp giấy phép kinh doanh `[NGHIA_VU_QUYEN]`) ==[ **TAC_DONG_DOI_TUONG** ]==> (`e7` quyết định thành lập `[GIAY_TO_HO_SO]`)


---

### Mẫu #06_2012_TT-BKHĐT_27861#body_context_88 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[06/2012/TT-BKHĐT]`<SO_HIEU>`** của **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Khoa học và công nghệ]`<LINH_VUC>`** . **[Điều 25]`<DIEU>`** . **[Khoản 1 . Đối với đơn vị trình khen]`<KHOAN>`** : **[d ) Khen thưởng ngoài ngành ( khen đối ngoại ) : Thủ trưởng cơ quan , đơn vị được **[quy định tại]`<TU_KHOA_PHAP_LY>`** **[Điều 24]`<THAM_CHIEU_PHAP_LY>`** , Khoản 2 , Mục e lập hồ sơ cho tập thể , cá nhân đề nghị khen thưởng gửi về Vụ Thi đua - Khen thưởng theo đúng **[mẫu v]`<THAM_CHIEU_PHAP_LY>`** à thời gian quy định .]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **06/2012/TT-BKHĐT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[4:8]`)
- `[e3]` **Khoa học và công nghệ** → `LINH_VUC` (span: `[10:13]`)
- `[e4]` **Điều 25** → `DIEU` (span: `[14:16]`)
- `[e5]` **Khoản 1 . Đối với đơn vị trình khen** → `KHOAN` (span: `[17:24]`)
- `[e6]` **d ) Khen thưởng ngoài ngành ( khen đối ngoại ) : Thủ trưởng cơ quan , đơn vị được quy định tại Điều 24 , Khoản 2 , Mục e lập hồ sơ cho tập thể , cá nhân đề nghị khen thưởng gửi về Vụ Thi đua - Khen thưởng theo đúng mẫu v à thời gian quy định .** → `DIEM` (span: `[25:71]`)
- `[e7]` **Điều 24** → `THAM_CHIEU_PHAP_LY` (span: `[42:44]`) *(lồng trong `e6` (`DIEM`))*
- `[e8]` **mẫu v** → `THAM_CHIEU_PHAP_LY` (span: `[65:67]`) *(lồng trong `e6` (`DIEM`))*
- `[e9]` **quy định tại** → `TU_KHOA_PHAP_LY` (span: `[40:42]`) *(lồng trong `e6` (`DIEM`))*

**Quan hệ:**
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Khoa học và công nghệ `[LINH_VUC]`)
- (`e4` Điều 25 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`)
- (`e5` Khoản 1 . Đối với đơn vị trình khen `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 25 `[DIEU]`)
- (`e6` d ) Khen thưởng ngoài ngành ( khen đối ngoại ) : Thủ trưởng cơ quan , đơn vị được quy định tại Điều 24 , Khoản 2 , Mục e lập hồ sơ cho tập thể , cá nhân đề nghị khen thưởng gửi về Vụ Thi đua - Khen thưởng theo đúng mẫu v à thời gian quy định . `[DIEM]`) ==[ **THUOC_VE** ]==> (`e5` Khoản 1 . Đối với đơn vị trình khen `[KHOAN]`)
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Khoa học và công nghệ `[LINH_VUC]`)
- (`e6` d ) Khen thưởng ngoài ngành ( khen đối ngoại ) : Thủ trưởng cơ quan , đơn vị được quy định tại Điều 24 , Khoản 2 , Mục e lập hồ sơ cho tập thể , cá nhân đề nghị khen thưởng gửi về Vụ Thi đua - Khen thưởng theo đúng mẫu v à thời gian quy định . `[DIEM]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Khoa học và công nghệ `[LINH_VUC]`)
- (`e9` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e7` Điều 24 `[THAM_CHIEU_PHAP_LY]`)
- (`e6` d ) Khen thưởng ngoài ngành ( khen đối ngoại ) : Thủ trưởng cơ quan , đơn vị được quy định tại Điều 24 , Khoản 2 , Mục e lập hồ sơ cho tập thể , cá nhân đề nghị khen thưởng gửi về Vụ Thi đua - Khen thưởng theo đúng mẫu v à thời gian quy định . `[DIEM]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e7` Điều 24 `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e9` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e8` mẫu v `[THAM_CHIEU_PHAP_LY]`)
- (`e6` d ) Khen thưởng ngoài ngành ( khen đối ngoại ) : Thủ trưởng cơ quan , đơn vị được quy định tại Điều 24 , Khoản 2 , Mục e lập hồ sơ cho tập thể , cá nhân đề nghị khen thưởng gửi về Vụ Thi đua - Khen thưởng theo đúng mẫu v à thời gian quy định . `[DIEM]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e8` mẫu v `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #06_2012_TT-BKHĐT_27861#body_standalone_89 (Loại: `body_standalone`)
> **[Điều 25]`<DIEU>`** . **[Khoản 1 . Đối với đơn vị trình khen]`<KHOAN>`** : **[d ) Khen thưởng ngoài ngành ( khen đối ngoại ) : Thủ trưởng cơ quan , đơn vị được **[quy định tại]`<TU_KHOA_PHAP_LY>`** **[Điều 24]`<THAM_CHIEU_PHAP_LY>`** , Khoản 2 , Mục e lập hồ sơ cho tập thể , cá nhân đề nghị khen thưởng gửi về Vụ Thi đua - Khen thưởng theo đúng **[mẫu v]`<THAM_CHIEU_PHAP_LY>`** à thời gian quy định .]`<DIEM>`**

**Thực thể:**
- `[e0]` **Điều 25** → `DIEU` (span: `[0:2]`)
- `[e1]` **Khoản 1 . Đối với đơn vị trình khen** → `KHOAN` (span: `[3:10]`)
- `[e2]` **d ) Khen thưởng ngoài ngành ( khen đối ngoại ) : Thủ trưởng cơ quan , đơn vị được quy định tại Điều 24 , Khoản 2 , Mục e lập hồ sơ cho tập thể , cá nhân đề nghị khen thưởng gửi về Vụ Thi đua - Khen thưởng theo đúng mẫu v à thời gian quy định .** → `DIEM` (span: `[11:57]`)
- `[e3]` **Điều 24** → `THAM_CHIEU_PHAP_LY` (span: `[28:30]`) *(lồng trong `e2` (`DIEM`))*
- `[e4]` **mẫu v** → `THAM_CHIEU_PHAP_LY` (span: `[51:53]`) *(lồng trong `e2` (`DIEM`))*
- `[e5]` **quy định tại** → `TU_KHOA_PHAP_LY` (span: `[26:28]`) *(lồng trong `e2` (`DIEM`))*

**Quan hệ:**
- (`e1` Khoản 1 . Đối với đơn vị trình khen `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 25 `[DIEU]`)
- (`e2` d ) Khen thưởng ngoài ngành ( khen đối ngoại ) : Thủ trưởng cơ quan , đơn vị được quy định tại Điều 24 , Khoản 2 , Mục e lập hồ sơ cho tập thể , cá nhân đề nghị khen thưởng gửi về Vụ Thi đua - Khen thưởng theo đúng mẫu v à thời gian quy định . `[DIEM]`) ==[ **THUOC_VE** ]==> (`e1` Khoản 1 . Đối với đơn vị trình khen `[KHOAN]`)
- (`e5` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Điều 24 `[THAM_CHIEU_PHAP_LY]`)
- (`e2` d ) Khen thưởng ngoài ngành ( khen đối ngoại ) : Thủ trưởng cơ quan , đơn vị được quy định tại Điều 24 , Khoản 2 , Mục e lập hồ sơ cho tập thể , cá nhân đề nghị khen thưởng gửi về Vụ Thi đua - Khen thưởng theo đúng mẫu v à thời gian quy định . `[DIEM]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Điều 24 `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e5` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e4` mẫu v `[THAM_CHIEU_PHAP_LY]`)
- (`e2` d ) Khen thưởng ngoài ngành ( khen đối ngoại ) : Thủ trưởng cơ quan , đơn vị được quy định tại Điều 24 , Khoản 2 , Mục e lập hồ sơ cho tập thể , cá nhân đề nghị khen thưởng gửi về Vụ Thi đua - Khen thưởng theo đúng mẫu v à thời gian quy định . `[DIEM]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e4` mẫu v `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #06_2012_TT-BKHĐT_27861#body_context_90 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[06/2012/TT-BKHĐT]`<SO_HIEU>`** của **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Khoa học và công nghệ]`<LINH_VUC>`** . **[Điều 26]`<DIEU>`** . **[1 . Đối với các đơn vị thuộc Bộ :]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **06/2012/TT-BKHĐT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[4:8]`)
- `[e3]` **Khoa học và công nghệ** → `LINH_VUC` (span: `[10:13]`)
- `[e4]` **Điều 26** → `DIEU` (span: `[14:16]`)
- `[e5]` **1 . Đối với các đơn vị thuộc Bộ :** → `KHOAN` (span: `[17:25]`)

**Quan hệ:**
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Khoa học và công nghệ `[LINH_VUC]`)
- (`e4` Điều 26 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`)
- (`e5` 1 . Đối với các đơn vị thuộc Bộ : `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 26 `[DIEU]`)
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Khoa học và công nghệ `[LINH_VUC]`)
- (`e5` 1 . Đối với các đơn vị thuộc Bộ : `[KHOAN]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Khoa học và công nghệ `[LINH_VUC]`)


---

### Mẫu #06_2012_TT-BKHĐT_27861#body_context_91 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[06/2012/TT-BKHĐT]`<SO_HIEU>`** ban hành **[ngày 19 tháng 10 năm 2012]`<NGAY_BAN_HANH>`** bởi **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** . **[Điều 27]`<DIEU>`** . **[5 . Đối với danh hiệu " Anh hùng Lao động " , " Nhà giáo nhân dân " , " Nhà giáo ưu tú " , " Giải thưởng Hồ Chí Minh " , " Giải thưởng Nhà nước " : Thực hiện theo quy định của Luật Thi đua - Khen thưởng , **[Nghị định số 42/2010/NĐ-CP]`<THAM_CHIEU_PHAP_LY>`** **[ngày 15 tháng 4 năm 2010]`<NGAY_THAM_CHIEU>`** của **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** và các văn bản của **[cơ quan Nhà nước có thẩm quyền]`<CO_QUAN_THAM_QUYEN>`** .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **06/2012/TT-BKHĐT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[11:15]`)
- `[e3]` **ngày 19 tháng 10 năm 2012** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 27** → `DIEU` (span: `[16:18]`)
- `[e5]` **5 . Đối với danh hiệu " Anh hùng Lao động " , " Nhà giáo nhân dân " , " Nhà giáo ưu tú " , " Giải thưởng Hồ Chí Minh " , " Giải thưởng Nhà nước " : Thực hiện theo quy định của Luật Thi đua - Khen thưởng , Nghị định số 42/2010/NĐ-CP ngày 15 tháng 4 năm 2010 của Chính phủ và các văn bản của cơ quan Nhà nước có thẩm quyền .** → `KHOAN` (span: `[19:77]`)
- `[e6]` **Nghị định số 42/2010/NĐ-CP** → `THAM_CHIEU_PHAP_LY` (span: `[57:60]`) *(lồng trong `e5` (`KHOAN`))*
- `[e7]` **ngày 15 tháng 4 năm 2010** → `NGAY_THAM_CHIEU` (span: `[60:66]`) *(lồng trong `e5` (`KHOAN`))*
- `[e8]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[67:68]`) *(lồng trong `e5` (`KHOAN`))*
- `[e9]` **cơ quan Nhà nước có thẩm quyền** → `CO_QUAN_THAM_QUYEN` (span: `[72:76]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 19 tháng 10 năm 2012 `[NGAY_BAN_HANH]`)
- (`e4` Điều 27 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`)
- (`e5` 5 . Đối với danh hiệu " Anh hùng Lao động " , " Nhà giáo nhân dân " , " Nhà giáo ưu tú " , " Giải thưởng Hồ Chí Minh " , " Giải thưởng Nhà nước " : Thực hiện theo quy định của Luật Thi đua - Khen thưởng , Nghị định số 42/2010/NĐ-CP ngày 15 tháng 4 năm 2010 của Chính phủ và các văn bản của cơ quan Nhà nước có thẩm quyền . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 27 `[DIEU]`)
- (`e5` 5 . Đối với danh hiệu " Anh hùng Lao động " , " Nhà giáo nhân dân " , " Nhà giáo ưu tú " , " Giải thưởng Hồ Chí Minh " , " Giải thưởng Nhà nước " : Thực hiện theo quy định của Luật Thi đua - Khen thưởng , Nghị định số 42/2010/NĐ-CP ngày 15 tháng 4 năm 2010 của Chính phủ và các văn bản của cơ quan Nhà nước có thẩm quyền . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e6` Nghị định số 42/2010/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e6` Nghị định số 42/2010/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e7` ngày 15 tháng 4 năm 2010 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #06_2012_TT-BKHĐT_27861#body_standalone_92 (Loại: `body_standalone`)
> **[Điều 27]`<DIEU>`** . **[5 . Đối với danh hiệu " Anh hùng Lao động " , " Nhà giáo nhân dân " , " Nhà giáo ưu tú " , " Giải thưởng Hồ Chí Minh " , " Giải thưởng Nhà nước " : Thực hiện theo quy định của Luật Thi đua - Khen thưởng , **[Nghị định số 42/2010/NĐ-CP]`<THAM_CHIEU_PHAP_LY>`** **[ngày 15 tháng 4 năm 2010]`<NGAY_THAM_CHIEU>`** của **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** và các văn bản của **[cơ quan Nhà nước có thẩm quyền]`<CO_QUAN_THAM_QUYEN>`** .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 27** → `DIEU` (span: `[0:2]`)
- `[e1]` **5 . Đối với danh hiệu " Anh hùng Lao động " , " Nhà giáo nhân dân " , " Nhà giáo ưu tú " , " Giải thưởng Hồ Chí Minh " , " Giải thưởng Nhà nước " : Thực hiện theo quy định của Luật Thi đua - Khen thưởng , Nghị định số 42/2010/NĐ-CP ngày 15 tháng 4 năm 2010 của Chính phủ và các văn bản của cơ quan Nhà nước có thẩm quyền .** → `KHOAN` (span: `[3:61]`)
- `[e2]` **Nghị định số 42/2010/NĐ-CP** → `THAM_CHIEU_PHAP_LY` (span: `[41:44]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **ngày 15 tháng 4 năm 2010** → `NGAY_THAM_CHIEU` (span: `[44:50]`) *(lồng trong `e1` (`KHOAN`))*
- `[e4]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[51:52]`) *(lồng trong `e1` (`KHOAN`))*
- `[e5]` **cơ quan Nhà nước có thẩm quyền** → `CO_QUAN_THAM_QUYEN` (span: `[56:60]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 5 . Đối với danh hiệu " Anh hùng Lao động " , " Nhà giáo nhân dân " , " Nhà giáo ưu tú " , " Giải thưởng Hồ Chí Minh " , " Giải thưởng Nhà nước " : Thực hiện theo quy định của Luật Thi đua - Khen thưởng , Nghị định số 42/2010/NĐ-CP ngày 15 tháng 4 năm 2010 của Chính phủ và các văn bản của cơ quan Nhà nước có thẩm quyền . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 27 `[DIEU]`)
- (`e1` 5 . Đối với danh hiệu " Anh hùng Lao động " , " Nhà giáo nhân dân " , " Nhà giáo ưu tú " , " Giải thưởng Hồ Chí Minh " , " Giải thưởng Nhà nước " : Thực hiện theo quy định của Luật Thi đua - Khen thưởng , Nghị định số 42/2010/NĐ-CP ngày 15 tháng 4 năm 2010 của Chính phủ và các văn bản của cơ quan Nhà nước có thẩm quyền . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e2` Nghị định số 42/2010/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e2` Nghị định số 42/2010/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e3` ngày 15 tháng 4 năm 2010 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #06_2012_TT-BKHĐT_27861#body_context_93 (Loại: `body_context`)
> **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[06/2012/TT-BKHĐT]`<SO_HIEU>`** . **[Điều 31]`<DIEU>`** . **[1 . Hằng năm , Văn phòng **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_THAM_QUYEN>`** có trách nhiệm bố trí kinh phí phục vụ cho công tác thi đua , khen thưởng của Bộ **[theo quy định tại]`<TU_KHOA_PHAP_LY>`** **[khoản 1 , Điều 67]`<THAM_CHIEU_PHAP_LY>`** , **[Nghị định số 42/2010/NĐ-CP]`<THAM_CHIEU_PHAP_LY>`** **[ngày 15/4/2010]`<NGAY_THAM_CHIEU>`** của **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** và **[Thông tư số 71/2011/TT-BTC]`<THAM_CHIEU_PHAP_LY>`** **[ngày 24/5/2011]`<NGAY_THAM_CHIEU>`** của **[Bộ Tài chính]`<CO_QUAN_THAM_QUYEN>`** Hướng dẫn việc trích lập , quản lý và sử dụng Quỹ thi đua , khen thưởng .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[5:6]`)
- `[e1]` **06/2012/TT-BKHĐT** → `SO_HIEU` (span: `[7:8]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[0:4]`)
- `[e3]` **Điều 31** → `DIEU` (span: `[9:11]`)
- `[e4]` **1 . Hằng năm , Văn phòng Bộ Kế hoạch và Đầu tư có trách nhiệm bố trí kinh phí phục vụ cho công tác thi đua , khen thưởng của Bộ theo quy định tại khoản 1 , Điều 67 , Nghị định số 42/2010/NĐ-CP ngày 15/4/2010 của Chính phủ và Thông tư số 71/2011/TT-BTC ngày 24/5/2011 của Bộ Tài chính Hướng dẫn việc trích lập , quản lý và sử dụng Quỹ thi đua , khen thưởng .** → `KHOAN` (span: `[12:71]`)
- `[e5]` **khoản 1 , Điều 67** → `THAM_CHIEU_PHAP_LY` (span: `[37:42]`) *(lồng trong `e4` (`KHOAN`))*
- `[e6]` **Nghị định số 42/2010/NĐ-CP** → `THAM_CHIEU_PHAP_LY` (span: `[43:46]`) *(lồng trong `e4` (`KHOAN`))*
- `[e7]` **Thông tư số 71/2011/TT-BTC** → `THAM_CHIEU_PHAP_LY` (span: `[51:54]`) *(lồng trong `e4` (`KHOAN`))*
- `[e8]` **theo quy định tại** → `TU_KHOA_PHAP_LY` (span: `[34:37]`) *(lồng trong `e4` (`KHOAN`))*
- `[e9]` **ngày 15/4/2010** → `NGAY_THAM_CHIEU` (span: `[46:48]`) *(lồng trong `e4` (`KHOAN`))*
- `[e10]` **ngày 24/5/2011** → `NGAY_THAM_CHIEU` (span: `[54:56]`) *(lồng trong `e4` (`KHOAN`))*
- `[e11]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_THAM_QUYEN` (span: `[18:22]`) *(lồng trong `e4` (`KHOAN`))*
- `[e12]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[49:50]`) *(lồng trong `e4` (`KHOAN`))*
- `[e13]` **Bộ Tài chính** → `CO_QUAN_THAM_QUYEN` (span: `[57:59]`) *(lồng trong `e4` (`KHOAN`))*

**Quan hệ:**
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 31 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`)
- (`e4` 1 . Hằng năm , Văn phòng Bộ Kế hoạch và Đầu tư có trách nhiệm bố trí kinh phí phục vụ cho công tác thi đua , khen thưởng của Bộ theo quy định tại khoản 1 , Điều 67 , Nghị định số 42/2010/NĐ-CP ngày 15/4/2010 của Chính phủ và Thông tư số 71/2011/TT-BTC ngày 24/5/2011 của Bộ Tài chính Hướng dẫn việc trích lập , quản lý và sử dụng Quỹ thi đua , khen thưởng . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 31 `[DIEU]`)
- (`e8` theo quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e5` khoản 1 , Điều 67 `[THAM_CHIEU_PHAP_LY]`)
- (`e4` 1 . Hằng năm , Văn phòng Bộ Kế hoạch và Đầu tư có trách nhiệm bố trí kinh phí phục vụ cho công tác thi đua , khen thưởng của Bộ theo quy định tại khoản 1 , Điều 67 , Nghị định số 42/2010/NĐ-CP ngày 15/4/2010 của Chính phủ và Thông tư số 71/2011/TT-BTC ngày 24/5/2011 của Bộ Tài chính Hướng dẫn việc trích lập , quản lý và sử dụng Quỹ thi đua , khen thưởng . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e5` khoản 1 , Điều 67 `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e8` theo quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e6` Nghị định số 42/2010/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e4` 1 . Hằng năm , Văn phòng Bộ Kế hoạch và Đầu tư có trách nhiệm bố trí kinh phí phục vụ cho công tác thi đua , khen thưởng của Bộ theo quy định tại khoản 1 , Điều 67 , Nghị định số 42/2010/NĐ-CP ngày 15/4/2010 của Chính phủ và Thông tư số 71/2011/TT-BTC ngày 24/5/2011 của Bộ Tài chính Hướng dẫn việc trích lập , quản lý và sử dụng Quỹ thi đua , khen thưởng . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e6` Nghị định số 42/2010/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e8` theo quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e7` Thông tư số 71/2011/TT-BTC `[THAM_CHIEU_PHAP_LY]`)
- (`e4` 1 . Hằng năm , Văn phòng Bộ Kế hoạch và Đầu tư có trách nhiệm bố trí kinh phí phục vụ cho công tác thi đua , khen thưởng của Bộ theo quy định tại khoản 1 , Điều 67 , Nghị định số 42/2010/NĐ-CP ngày 15/4/2010 của Chính phủ và Thông tư số 71/2011/TT-BTC ngày 24/5/2011 của Bộ Tài chính Hướng dẫn việc trích lập , quản lý và sử dụng Quỹ thi đua , khen thưởng . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e7` Thông tư số 71/2011/TT-BTC `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e6` Nghị định số 42/2010/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e9` ngày 15/4/2010 `[NGAY_THAM_CHIEU]`)
- (`e7` Thông tư số 71/2011/TT-BTC `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e10` ngày 24/5/2011 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #06_2012_TT-BKHĐT_27861#body_standalone_94 (Loại: `body_standalone`)
> **[Điều 31]`<DIEU>`** . **[1 . Hằng năm , Văn phòng **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_THAM_QUYEN>`** có trách nhiệm bố trí kinh phí phục vụ cho công tác thi đua , khen thưởng của Bộ **[theo quy định tại]`<TU_KHOA_PHAP_LY>`** **[khoản 1 , Điều 67]`<THAM_CHIEU_PHAP_LY>`** , **[Nghị định số 42/2010/NĐ-CP]`<THAM_CHIEU_PHAP_LY>`** **[ngày 15/4/2010]`<NGAY_THAM_CHIEU>`** của **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** và **[Thông tư số 71/2011/TT-BTC]`<THAM_CHIEU_PHAP_LY>`** **[ngày 24/5/2011]`<NGAY_THAM_CHIEU>`** của **[Bộ Tài chính]`<CO_QUAN_THAM_QUYEN>`** Hướng dẫn việc trích lập , quản lý và sử dụng Quỹ thi đua , khen thưởng .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 31** → `DIEU` (span: `[0:2]`)
- `[e1]` **1 . Hằng năm , Văn phòng Bộ Kế hoạch và Đầu tư có trách nhiệm bố trí kinh phí phục vụ cho công tác thi đua , khen thưởng của Bộ theo quy định tại khoản 1 , Điều 67 , Nghị định số 42/2010/NĐ-CP ngày 15/4/2010 của Chính phủ và Thông tư số 71/2011/TT-BTC ngày 24/5/2011 của Bộ Tài chính Hướng dẫn việc trích lập , quản lý và sử dụng Quỹ thi đua , khen thưởng .** → `KHOAN` (span: `[3:62]`)
- `[e2]` **khoản 1 , Điều 67** → `THAM_CHIEU_PHAP_LY` (span: `[28:33]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **Nghị định số 42/2010/NĐ-CP** → `THAM_CHIEU_PHAP_LY` (span: `[34:37]`) *(lồng trong `e1` (`KHOAN`))*
- `[e4]` **Thông tư số 71/2011/TT-BTC** → `THAM_CHIEU_PHAP_LY` (span: `[42:45]`) *(lồng trong `e1` (`KHOAN`))*
- `[e5]` **theo quy định tại** → `TU_KHOA_PHAP_LY` (span: `[25:28]`) *(lồng trong `e1` (`KHOAN`))*
- `[e6]` **ngày 15/4/2010** → `NGAY_THAM_CHIEU` (span: `[37:39]`) *(lồng trong `e1` (`KHOAN`))*
- `[e7]` **ngày 24/5/2011** → `NGAY_THAM_CHIEU` (span: `[45:47]`) *(lồng trong `e1` (`KHOAN`))*
- `[e8]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_THAM_QUYEN` (span: `[9:13]`) *(lồng trong `e1` (`KHOAN`))*
- `[e9]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[40:41]`) *(lồng trong `e1` (`KHOAN`))*
- `[e10]` **Bộ Tài chính** → `CO_QUAN_THAM_QUYEN` (span: `[48:50]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 1 . Hằng năm , Văn phòng Bộ Kế hoạch và Đầu tư có trách nhiệm bố trí kinh phí phục vụ cho công tác thi đua , khen thưởng của Bộ theo quy định tại khoản 1 , Điều 67 , Nghị định số 42/2010/NĐ-CP ngày 15/4/2010 của Chính phủ và Thông tư số 71/2011/TT-BTC ngày 24/5/2011 của Bộ Tài chính Hướng dẫn việc trích lập , quản lý và sử dụng Quỹ thi đua , khen thưởng . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 31 `[DIEU]`)
- (`e5` theo quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e2` khoản 1 , Điều 67 `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 1 . Hằng năm , Văn phòng Bộ Kế hoạch và Đầu tư có trách nhiệm bố trí kinh phí phục vụ cho công tác thi đua , khen thưởng của Bộ theo quy định tại khoản 1 , Điều 67 , Nghị định số 42/2010/NĐ-CP ngày 15/4/2010 của Chính phủ và Thông tư số 71/2011/TT-BTC ngày 24/5/2011 của Bộ Tài chính Hướng dẫn việc trích lập , quản lý và sử dụng Quỹ thi đua , khen thưởng . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e2` khoản 1 , Điều 67 `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e5` theo quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Nghị định số 42/2010/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 1 . Hằng năm , Văn phòng Bộ Kế hoạch và Đầu tư có trách nhiệm bố trí kinh phí phục vụ cho công tác thi đua , khen thưởng của Bộ theo quy định tại khoản 1 , Điều 67 , Nghị định số 42/2010/NĐ-CP ngày 15/4/2010 của Chính phủ và Thông tư số 71/2011/TT-BTC ngày 24/5/2011 của Bộ Tài chính Hướng dẫn việc trích lập , quản lý và sử dụng Quỹ thi đua , khen thưởng . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Nghị định số 42/2010/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e5` theo quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e4` Thông tư số 71/2011/TT-BTC `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 1 . Hằng năm , Văn phòng Bộ Kế hoạch và Đầu tư có trách nhiệm bố trí kinh phí phục vụ cho công tác thi đua , khen thưởng của Bộ theo quy định tại khoản 1 , Điều 67 , Nghị định số 42/2010/NĐ-CP ngày 15/4/2010 của Chính phủ và Thông tư số 71/2011/TT-BTC ngày 24/5/2011 của Bộ Tài chính Hướng dẫn việc trích lập , quản lý và sử dụng Quỹ thi đua , khen thưởng . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e4` Thông tư số 71/2011/TT-BTC `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e3` Nghị định số 42/2010/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e6` ngày 15/4/2010 `[NGAY_THAM_CHIEU]`)
- (`e4` Thông tư số 71/2011/TT-BTC `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e7` ngày 24/5/2011 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #06_2012_TT-BKHĐT_27861#body_context_95 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[06/2012/TT-BKHĐT]`<SO_HIEU>`** ban hành **[ngày 19 tháng 10 năm 2012]`<NGAY_BAN_HANH>`** bởi **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** . **[Điều 32]`<DIEU>`** . **[Khoản 1 . Quỹ thi đua , khen thưởng của cơ quan **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_THAM_QUYEN>`**]`<KHOAN>`** : **[b ) Quỹ thi đua , khen thưởng của **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_THAM_QUYEN>`** được sử dụng :]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **06/2012/TT-BKHĐT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[11:15]`)
- `[e3]` **ngày 19 tháng 10 năm 2012** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 32** → `DIEU` (span: `[16:18]`)
- `[e5]` **Khoản 1 . Quỹ thi đua , khen thưởng của cơ quan Bộ Kế hoạch và Đầu tư** → `KHOAN` (span: `[19:32]`)
- `[e6]` **b ) Quỹ thi đua , khen thưởng của Bộ Kế hoạch và Đầu tư được sử dụng :** → `DIEM` (span: `[33:47]`)
- `[e7]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_THAM_QUYEN` (span: `[28:32]`) *(lồng trong `e5` (`KHOAN`))*
- `[e8]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_THAM_QUYEN` (span: `[40:44]`) *(lồng trong `e6` (`DIEM`))*

**Quan hệ:**
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 19 tháng 10 năm 2012 `[NGAY_BAN_HANH]`)
- (`e4` Điều 32 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`)
- (`e5` Khoản 1 . Quỹ thi đua , khen thưởng của cơ quan Bộ Kế hoạch và Đầu tư `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 32 `[DIEU]`)
- (`e6` b ) Quỹ thi đua , khen thưởng của Bộ Kế hoạch và Đầu tư được sử dụng : `[DIEM]`) ==[ **THUOC_VE** ]==> (`e5` Khoản 1 . Quỹ thi đua , khen thưởng của cơ quan Bộ Kế hoạch và Đầu tư `[KHOAN]`)


---

### Mẫu #06_2012_TT-BKHĐT_27861#body_standalone_96 (Loại: `body_standalone`)
> **[Điều 32]`<DIEU>`** . **[Khoản 1 . Quỹ thi đua , khen thưởng của cơ quan **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_THAM_QUYEN>`**]`<KHOAN>`** : **[b ) Quỹ thi đua , khen thưởng của **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_THAM_QUYEN>`** được sử dụng :]`<DIEM>`**

**Thực thể:**
- `[e0]` **Điều 32** → `DIEU` (span: `[0:2]`)
- `[e1]` **Khoản 1 . Quỹ thi đua , khen thưởng của cơ quan Bộ Kế hoạch và Đầu tư** → `KHOAN` (span: `[3:16]`)
- `[e2]` **b ) Quỹ thi đua , khen thưởng của Bộ Kế hoạch và Đầu tư được sử dụng :** → `DIEM` (span: `[17:31]`)
- `[e3]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_THAM_QUYEN` (span: `[12:16]`) *(lồng trong `e1` (`KHOAN`))*
- `[e4]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_THAM_QUYEN` (span: `[24:28]`) *(lồng trong `e2` (`DIEM`))*

**Quan hệ:**
- (`e1` Khoản 1 . Quỹ thi đua , khen thưởng của cơ quan Bộ Kế hoạch và Đầu tư `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 32 `[DIEU]`)
- (`e2` b ) Quỹ thi đua , khen thưởng của Bộ Kế hoạch và Đầu tư được sử dụng : `[DIEM]`) ==[ **THUOC_VE** ]==> (`e1` Khoản 1 . Quỹ thi đua , khen thưởng của cơ quan Bộ Kế hoạch và Đầu tư `[KHOAN]`)


---

### Mẫu #06_2012_TT-BKHĐT_27861#body_context_97 (Loại: `body_context`)
> **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[06/2012/TT-BKHĐT]`<SO_HIEU>`** . **[Điều 32]`<DIEU>`** . **[3 . Đối với các Sở , Ban Quản lý : Đơn vị tự chi **[tiền thưởng]`<TAI_SAN_VAT_CHAT>`** đối với các quyết định khen thưởng của **[Bộ trưởng Bộ Kế hoạch và Đầu tư]`<CO_QUAN_THAM_QUYEN>`** “ Cờ thi đua cấp Bộ ” , “ Bằng khen của Bộ trưởng ” , “ **[Kỷ niệm chương]`<GIAY_TO_HO_SO>`** “ Vì sự nghiệp **[ngành Kế hoạch và Đầu tư Việt Nam]`<LINH_VUC>`** ” cho các tập thể , cá nhân do đơn vị quản lý và trình khen .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[5:6]`)
- `[e1]` **06/2012/TT-BKHĐT** → `SO_HIEU` (span: `[7:8]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[0:4]`)
- `[e3]` **Điều 32** → `DIEU` (span: `[9:11]`)
- `[e4]` **3 . Đối với các Sở , Ban Quản lý : Đơn vị tự chi tiền thưởng đối với các quyết định khen thưởng của Bộ trưởng Bộ Kế hoạch và Đầu tư “ Cờ thi đua cấp Bộ ” , “ Bằng khen của Bộ trưởng ” , “ Kỷ niệm chương “ Vì sự nghiệp ngành Kế hoạch và Đầu tư Việt Nam ” cho các tập thể , cá nhân do đơn vị quản lý và trình khen .** → `KHOAN` (span: `[12:73]`)
- `[e5]` **ngành Kế hoạch và Đầu tư Việt Nam** → `LINH_VUC` (span: `[55:60]`) *(lồng trong `e4` (`KHOAN`))*
- `[e6]` **Bộ trưởng Bộ Kế hoạch và Đầu tư** → `CO_QUAN_THAM_QUYEN` (span: `[31:36]`) *(lồng trong `e4` (`KHOAN`))*
- `[e7]` **Kỷ niệm chương** → `GIAY_TO_HO_SO` (span: `[50:52]`) *(lồng trong `e4` (`KHOAN`))*
- `[e8]` **tiền thưởng** → `TAI_SAN_VAT_CHAT` (span: `[24:26]`) *(lồng trong `e4` (`KHOAN`))*

**Quan hệ:**
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 32 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`)
- (`e4` 3 . Đối với các Sở , Ban Quản lý : Đơn vị tự chi tiền thưởng đối với các quyết định khen thưởng của Bộ trưởng Bộ Kế hoạch và Đầu tư “ Cờ thi đua cấp Bộ ” , “ Bằng khen của Bộ trưởng ” , “ Kỷ niệm chương “ Vì sự nghiệp ngành Kế hoạch và Đầu tư Việt Nam ” cho các tập thể , cá nhân do đơn vị quản lý và trình khen . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 32 `[DIEU]`)
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e5` ngành Kế hoạch và Đầu tư Việt Nam `[LINH_VUC]`)
- (`e4` 3 . Đối với các Sở , Ban Quản lý : Đơn vị tự chi tiền thưởng đối với các quyết định khen thưởng của Bộ trưởng Bộ Kế hoạch và Đầu tư “ Cờ thi đua cấp Bộ ” , “ Bằng khen của Bộ trưởng ” , “ Kỷ niệm chương “ Vì sự nghiệp ngành Kế hoạch và Đầu tư Việt Nam ” cho các tập thể , cá nhân do đơn vị quản lý và trình khen . `[KHOAN]`) ==[ **THUOC_LINH_VUC** ]==> (`e5` ngành Kế hoạch và Đầu tư Việt Nam `[LINH_VUC]`) *(Quan hệ lồng nhau)*


---

### Mẫu #06_2012_TT-BKHĐT_27861#body_standalone_98 (Loại: `body_standalone`)
> **[Điều 32]`<DIEU>`** . **[3 . Đối với các Sở , Ban Quản lý : Đơn vị tự chi **[tiền thưởng]`<TAI_SAN_VAT_CHAT>`** đối với các quyết định khen thưởng của **[Bộ trưởng Bộ Kế hoạch và Đầu tư]`<CO_QUAN_THAM_QUYEN>`** “ Cờ thi đua cấp Bộ ” , “ Bằng khen của Bộ trưởng ” , “ **[Kỷ niệm chương]`<GIAY_TO_HO_SO>`** “ Vì sự nghiệp **[ngành Kế hoạch và Đầu tư Việt Nam]`<LINH_VUC>`** ” cho các tập thể , cá nhân do đơn vị quản lý và trình khen .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 32** → `DIEU` (span: `[0:2]`)
- `[e1]` **3 . Đối với các Sở , Ban Quản lý : Đơn vị tự chi tiền thưởng đối với các quyết định khen thưởng của Bộ trưởng Bộ Kế hoạch và Đầu tư “ Cờ thi đua cấp Bộ ” , “ Bằng khen của Bộ trưởng ” , “ Kỷ niệm chương “ Vì sự nghiệp ngành Kế hoạch và Đầu tư Việt Nam ” cho các tập thể , cá nhân do đơn vị quản lý và trình khen .** → `KHOAN` (span: `[3:64]`)
- `[e2]` **ngành Kế hoạch và Đầu tư Việt Nam** → `LINH_VUC` (span: `[46:51]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **Bộ trưởng Bộ Kế hoạch và Đầu tư** → `CO_QUAN_THAM_QUYEN` (span: `[22:27]`) *(lồng trong `e1` (`KHOAN`))*
- `[e4]` **Kỷ niệm chương** → `GIAY_TO_HO_SO` (span: `[41:43]`) *(lồng trong `e1` (`KHOAN`))*
- `[e5]` **tiền thưởng** → `TAI_SAN_VAT_CHAT` (span: `[15:17]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 3 . Đối với các Sở , Ban Quản lý : Đơn vị tự chi tiền thưởng đối với các quyết định khen thưởng của Bộ trưởng Bộ Kế hoạch và Đầu tư “ Cờ thi đua cấp Bộ ” , “ Bằng khen của Bộ trưởng ” , “ Kỷ niệm chương “ Vì sự nghiệp ngành Kế hoạch và Đầu tư Việt Nam ” cho các tập thể , cá nhân do đơn vị quản lý và trình khen . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 32 `[DIEU]`)
- (`e1` 3 . Đối với các Sở , Ban Quản lý : Đơn vị tự chi tiền thưởng đối với các quyết định khen thưởng của Bộ trưởng Bộ Kế hoạch và Đầu tư “ Cờ thi đua cấp Bộ ” , “ Bằng khen của Bộ trưởng ” , “ Kỷ niệm chương “ Vì sự nghiệp ngành Kế hoạch và Đầu tư Việt Nam ” cho các tập thể , cá nhân do đơn vị quản lý và trình khen . `[KHOAN]`) ==[ **THUOC_LINH_VUC** ]==> (`e2` ngành Kế hoạch và Đầu tư Việt Nam `[LINH_VUC]`) *(Quan hệ lồng nhau)*


---

### Mẫu #06_2012_TT-BKHĐT_27861#body_context_99 (Loại: `body_context`)
> **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[06/2012/TT-BKHĐT]`<SO_HIEU>`** . **[Điều 32]`<DIEU>`** . **[4 . Mức **[tiền thưởng]`<TAI_SAN_VAT_CHAT>`** kèm theo các danh hiệu thi đua , các hình thức khen thưởng được thực hiện **[theo quy định tại]`<TU_KHOA_PHAP_LY>`** **[Nghị định số 42/2010/NĐ-CP]`<THAM_CHIEU_PHAP_LY>`** **[ngày 15 tháng 4 năm 2010]`<NGAY_THAM_CHIEU>`** của **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[5:6]`)
- `[e1]` **06/2012/TT-BKHĐT** → `SO_HIEU` (span: `[7:8]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[0:4]`)
- `[e3]` **Điều 32** → `DIEU` (span: `[9:11]`)
- `[e4]` **4 . Mức tiền thưởng kèm theo các danh hiệu thi đua , các hình thức khen thưởng được thực hiện theo quy định tại Nghị định số 42/2010/NĐ-CP ngày 15 tháng 4 năm 2010 của Chính phủ .** → `KHOAN` (span: `[12:43]`)
- `[e5]` **Nghị định số 42/2010/NĐ-CP** → `THAM_CHIEU_PHAP_LY` (span: `[31:34]`) *(lồng trong `e4` (`KHOAN`))*
- `[e6]` **theo quy định tại** → `TU_KHOA_PHAP_LY` (span: `[28:31]`) *(lồng trong `e4` (`KHOAN`))*
- `[e7]` **ngày 15 tháng 4 năm 2010** → `NGAY_THAM_CHIEU` (span: `[34:40]`) *(lồng trong `e4` (`KHOAN`))*
- `[e8]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[41:42]`) *(lồng trong `e4` (`KHOAN`))*
- `[e9]` **tiền thưởng** → `TAI_SAN_VAT_CHAT` (span: `[15:17]`) *(lồng trong `e4` (`KHOAN`))*

**Quan hệ:**
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 32 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 06/2012/TT-BKHĐT `[SO_HIEU]`)
- (`e4` 4 . Mức tiền thưởng kèm theo các danh hiệu thi đua , các hình thức khen thưởng được thực hiện theo quy định tại Nghị định số 42/2010/NĐ-CP ngày 15 tháng 4 năm 2010 của Chính phủ . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 32 `[DIEU]`)
- (`e6` theo quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e5` Nghị định số 42/2010/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e4` 4 . Mức tiền thưởng kèm theo các danh hiệu thi đua , các hình thức khen thưởng được thực hiện theo quy định tại Nghị định số 42/2010/NĐ-CP ngày 15 tháng 4 năm 2010 của Chính phủ . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e5` Nghị định số 42/2010/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e5` Nghị định số 42/2010/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e7` ngày 15 tháng 4 năm 2010 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #06_2012_TT-BKHĐT_27861#body_standalone_100 (Loại: `body_standalone`)
> **[Điều 32]`<DIEU>`** . **[4 . Mức **[tiền thưởng]`<TAI_SAN_VAT_CHAT>`** kèm theo các danh hiệu thi đua , các hình thức khen thưởng được thực hiện **[theo quy định tại]`<TU_KHOA_PHAP_LY>`** **[Nghị định số 42/2010/NĐ-CP]`<THAM_CHIEU_PHAP_LY>`** **[ngày 15 tháng 4 năm 2010]`<NGAY_THAM_CHIEU>`** của **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 32** → `DIEU` (span: `[0:2]`)
- `[e1]` **4 . Mức tiền thưởng kèm theo các danh hiệu thi đua , các hình thức khen thưởng được thực hiện theo quy định tại Nghị định số 42/2010/NĐ-CP ngày 15 tháng 4 năm 2010 của Chính phủ .** → `KHOAN` (span: `[3:34]`)
- `[e2]` **Nghị định số 42/2010/NĐ-CP** → `THAM_CHIEU_PHAP_LY` (span: `[22:25]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **theo quy định tại** → `TU_KHOA_PHAP_LY` (span: `[19:22]`) *(lồng trong `e1` (`KHOAN`))*
- `[e4]` **ngày 15 tháng 4 năm 2010** → `NGAY_THAM_CHIEU` (span: `[25:31]`) *(lồng trong `e1` (`KHOAN`))*
- `[e5]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[32:33]`) *(lồng trong `e1` (`KHOAN`))*
- `[e6]` **tiền thưởng** → `TAI_SAN_VAT_CHAT` (span: `[6:8]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 4 . Mức tiền thưởng kèm theo các danh hiệu thi đua , các hình thức khen thưởng được thực hiện theo quy định tại Nghị định số 42/2010/NĐ-CP ngày 15 tháng 4 năm 2010 của Chính phủ . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 32 `[DIEU]`)
- (`e3` theo quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e2` Nghị định số 42/2010/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 4 . Mức tiền thưởng kèm theo các danh hiệu thi đua , các hình thức khen thưởng được thực hiện theo quy định tại Nghị định số 42/2010/NĐ-CP ngày 15 tháng 4 năm 2010 của Chính phủ . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e2` Nghị định số 42/2010/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e2` Nghị định số 42/2010/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e4` ngày 15 tháng 4 năm 2010 `[NGAY_THAM_CHIEU]`)


---
