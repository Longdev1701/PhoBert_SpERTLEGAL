# Dữ liệu gán nhãn văn bản: 02_2015_TT-TTCP_58849
- **Thể loại**: `thong_tu`
- **Phân vùng dữ liệu**: `TEST`
- **Tổng số mẫu**: 91 mẫu
- **Tổng số thực thể**: 574
- **Tổng số quan hệ**: 400

---

### Mẫu #02_2015_TT-TTCP_58849#preamble_context_0 (Loại: `preamble_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[02/2015/TT-TTCP]`<SO_HIEU>`** của **[Thanh tra Chính phủ]`<CO_QUAN_BAN_HANH>`** . **[Căn cứ]`<TU_KHOA_PHAP_LY>`** **[Luật thanh tra]`<THAM_CHIEU_PHAP_LY>`** **[ngày 15 tháng 11 năm 2010]`<NGAY_THAM_CHIEU>`** ;

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **02/2015/TT-TTCP** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Thanh tra Chính phủ** → `CO_QUAN_BAN_HANH` (span: `[4:6]`)
- `[e3]` **Luật thanh tra** → `THAM_CHIEU_PHAP_LY` (span: `[8:10]`)
- `[e4]` **Căn cứ** → `TU_KHOA_PHAP_LY` (span: `[7:8]`)
- `[e5]` **ngày 15 tháng 11 năm 2010** → `NGAY_THAM_CHIEU` (span: `[10:16]`)

**Quan hệ:**
- (`e1` 02/2015/TT-TTCP `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Thanh tra Chính phủ `[CO_QUAN_BAN_HANH]`)
- (`e1` 02/2015/TT-TTCP `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e4` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Luật thanh tra `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 02/2015/TT-TTCP `[SO_HIEU]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Luật thanh tra `[THAM_CHIEU_PHAP_LY]`)
- (`e3` Luật thanh tra `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e5` ngày 15 tháng 11 năm 2010 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #02_2015_TT-TTCP_58849#preamble_standalone_1 (Loại: `preamble_standalone`)
> **[Căn cứ]`<TU_KHOA_PHAP_LY>`** **[Luật thanh tra]`<THAM_CHIEU_PHAP_LY>`** **[ngày 15 tháng 11 năm 2010]`<NGAY_THAM_CHIEU>`** ;

**Thực thể:**
- `[e0]` **Luật thanh tra** → `THAM_CHIEU_PHAP_LY` (span: `[1:3]`)
- `[e1]` **Căn cứ** → `TU_KHOA_PHAP_LY` (span: `[0:1]`)
- `[e2]` **ngày 15 tháng 11 năm 2010** → `NGAY_THAM_CHIEU` (span: `[3:9]`)

**Quan hệ:**
- (`e1` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e0` Luật thanh tra `[THAM_CHIEU_PHAP_LY]`)
- (`e0` Luật thanh tra `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e2` ngày 15 tháng 11 năm 2010 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #02_2015_TT-TTCP_58849#preamble_context_2 (Loại: `preamble_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[02/2015/TT-TTCP]`<SO_HIEU>`** của **[Thanh tra Chính phủ]`<CO_QUAN_BAN_HANH>`** . **[Căn cứ]`<TU_KHOA_PHAP_LY>`** **[Nghị định số 83/2012/NĐ-CP]`<THAM_CHIEU_PHAP_LY>`** **[ngày 09 tháng 10 năm 2012]`<NGAY_THAM_CHIEU>`** của **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** quy định chức năng , nhiệm vụ , quyền hạn và cơ cấu tổ chức của **[Thanh tra Chính phủ]`<CO_QUAN_THAM_QUYEN>`** ;

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **02/2015/TT-TTCP** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Thanh tra Chính phủ** → `CO_QUAN_BAN_HANH` (span: `[4:6]`)
- `[e3]` **Nghị định số 83/2012/NĐ-CP** → `THAM_CHIEU_PHAP_LY` (span: `[8:11]`)
- `[e4]` **Căn cứ** → `TU_KHOA_PHAP_LY` (span: `[7:8]`)
- `[e5]` **ngày 09 tháng 10 năm 2012** → `NGAY_THAM_CHIEU` (span: `[11:17]`)
- `[e6]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[18:19]`)
- `[e7]` **Thanh tra Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[29:31]`)

**Quan hệ:**
- (`e1` 02/2015/TT-TTCP `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Thanh tra Chính phủ `[CO_QUAN_BAN_HANH]`)
- (`e1` 02/2015/TT-TTCP `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e4` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Nghị định số 83/2012/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 02/2015/TT-TTCP `[SO_HIEU]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Nghị định số 83/2012/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e3` Nghị định số 83/2012/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e5` ngày 09 tháng 10 năm 2012 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #02_2015_TT-TTCP_58849#preamble_standalone_3 (Loại: `preamble_standalone`)
> **[Căn cứ]`<TU_KHOA_PHAP_LY>`** **[Nghị định số 83/2012/NĐ-CP]`<THAM_CHIEU_PHAP_LY>`** **[ngày 09 tháng 10 năm 2012]`<NGAY_THAM_CHIEU>`** của **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** quy định chức năng , nhiệm vụ , quyền hạn và cơ cấu tổ chức của **[Thanh tra Chính phủ]`<CO_QUAN_THAM_QUYEN>`** ;

**Thực thể:**
- `[e0]` **Nghị định số 83/2012/NĐ-CP** → `THAM_CHIEU_PHAP_LY` (span: `[1:4]`)
- `[e1]` **Căn cứ** → `TU_KHOA_PHAP_LY` (span: `[0:1]`)
- `[e2]` **ngày 09 tháng 10 năm 2012** → `NGAY_THAM_CHIEU` (span: `[4:10]`)
- `[e3]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[11:12]`)
- `[e4]` **Thanh tra Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[22:24]`)

**Quan hệ:**
- (`e1` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e0` Nghị định số 83/2012/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e3` Chính phủ `[CO_QUAN_THAM_QUYEN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e0` Nghị định số 83/2012/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e0` Nghị định số 83/2012/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e2` ngày 09 tháng 10 năm 2012 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #02_2015_TT-TTCP_58849#preamble_context_4 (Loại: `preamble_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[02/2015/TT-TTCP]`<SO_HIEU>`** của **[Thanh tra Chính phủ]`<CO_QUAN_BAN_HANH>`** . **[Căn cứ]`<TU_KHOA_PHAP_LY>`** **[Nghị định số 97/2011/NĐ-CP]`<THAM_CHIEU_PHAP_LY>`** **[ngày 21 tháng 10 năm 2011]`<NGAY_THAM_CHIEU>`** của **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** quy định về thanh tra viên và cộng tác viên thanh tra ;

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **02/2015/TT-TTCP** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Thanh tra Chính phủ** → `CO_QUAN_BAN_HANH` (span: `[4:6]`)
- `[e3]` **Nghị định số 97/2011/NĐ-CP** → `THAM_CHIEU_PHAP_LY` (span: `[8:11]`)
- `[e4]` **Căn cứ** → `TU_KHOA_PHAP_LY` (span: `[7:8]`)
- `[e5]` **ngày 21 tháng 10 năm 2011** → `NGAY_THAM_CHIEU` (span: `[11:17]`)
- `[e6]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[18:19]`)

**Quan hệ:**
- (`e1` 02/2015/TT-TTCP `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Thanh tra Chính phủ `[CO_QUAN_BAN_HANH]`)
- (`e1` 02/2015/TT-TTCP `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e4` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Nghị định số 97/2011/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 02/2015/TT-TTCP `[SO_HIEU]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Nghị định số 97/2011/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e3` Nghị định số 97/2011/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e5` ngày 21 tháng 10 năm 2011 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #02_2015_TT-TTCP_58849#preamble_standalone_5 (Loại: `preamble_standalone`)
> **[Căn cứ]`<TU_KHOA_PHAP_LY>`** **[Nghị định số 97/2011/NĐ-CP]`<THAM_CHIEU_PHAP_LY>`** **[ngày 21 tháng 10 năm 2011]`<NGAY_THAM_CHIEU>`** của **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** quy định về thanh tra viên và cộng tác viên thanh tra ;

**Thực thể:**
- `[e0]` **Nghị định số 97/2011/NĐ-CP** → `THAM_CHIEU_PHAP_LY` (span: `[1:4]`)
- `[e1]` **Căn cứ** → `TU_KHOA_PHAP_LY` (span: `[0:1]`)
- `[e2]` **ngày 21 tháng 10 năm 2011** → `NGAY_THAM_CHIEU` (span: `[4:10]`)
- `[e3]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[11:12]`)

**Quan hệ:**
- (`e1` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e0` Nghị định số 97/2011/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e3` Chính phủ `[CO_QUAN_THAM_QUYEN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e0` Nghị định số 97/2011/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e0` Nghị định số 97/2011/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e2` ngày 21 tháng 10 năm 2011 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #02_2015_TT-TTCP_58849#preamble_context_6 (Loại: `preamble_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[02/2015/TT-TTCP]`<SO_HIEU>`** của **[Thanh tra Chính phủ]`<CO_QUAN_BAN_HANH>`** . **[Căn cứ]`<TU_KHOA_PHAP_LY>`** **[Nghị định số 92/2014/NĐ-CP]`<THAM_CHIEU_PHAP_LY>`** **[ngày 08 tháng 10 năm 2014]`<NGAY_THAM_CHIEU>`** của **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** **[sửa đổi , bổ sung]`<TU_KHOA_PHAP_LY>`** **[khoản 1 Điều 16 Nghị định số 97/2011/NĐ-CP]`<THAM_CHIEU_PHAP_LY>`** **[ngày 21 tháng 10 năm 2011]`<NGAY_THAM_CHIEU>`** của **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** quy định về thanh tra viên và cộng tác viên thanh tra ;

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **02/2015/TT-TTCP** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Thanh tra Chính phủ** → `CO_QUAN_BAN_HANH` (span: `[4:6]`)
- `[e3]` **Nghị định số 92/2014/NĐ-CP** → `THAM_CHIEU_PHAP_LY` (span: `[8:11]`)
- `[e4]` **khoản 1 Điều 16 Nghị định số 97/2011/NĐ-CP** → `THAM_CHIEU_PHAP_LY` (span: `[22:29]`)
- `[e5]` **Căn cứ** → `TU_KHOA_PHAP_LY` (span: `[7:8]`)
- `[e6]` **sửa đổi , bổ sung** → `TU_KHOA_PHAP_LY` (span: `[19:22]`)
- `[e7]` **ngày 08 tháng 10 năm 2014** → `NGAY_THAM_CHIEU` (span: `[11:17]`)
- `[e8]` **ngày 21 tháng 10 năm 2011** → `NGAY_THAM_CHIEU` (span: `[29:35]`)
- `[e9]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[18:19]`)
- `[e10]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[36:37]`)

**Quan hệ:**
- (`e1` 02/2015/TT-TTCP `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Thanh tra Chính phủ `[CO_QUAN_BAN_HANH]`)
- (`e1` 02/2015/TT-TTCP `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e5` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Nghị định số 92/2014/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 02/2015/TT-TTCP `[SO_HIEU]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Nghị định số 92/2014/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e6` sửa đổi , bổ sung `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e4` khoản 1 Điều 16 Nghị định số 97/2011/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 02/2015/TT-TTCP `[SO_HIEU]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e4` khoản 1 Điều 16 Nghị định số 97/2011/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e3` Nghị định số 92/2014/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e7` ngày 08 tháng 10 năm 2014 `[NGAY_THAM_CHIEU]`)
- (`e4` khoản 1 Điều 16 Nghị định số 97/2011/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e8` ngày 21 tháng 10 năm 2011 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #02_2015_TT-TTCP_58849#preamble_standalone_7 (Loại: `preamble_standalone`)
> **[Căn cứ]`<TU_KHOA_PHAP_LY>`** **[Nghị định số 92/2014/NĐ-CP]`<THAM_CHIEU_PHAP_LY>`** **[ngày 08 tháng 10 năm 2014]`<NGAY_THAM_CHIEU>`** của **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** **[sửa đổi , bổ sung]`<TU_KHOA_PHAP_LY>`** **[khoản 1 Điều 16 Nghị định số 97/2011/NĐ-CP]`<THAM_CHIEU_PHAP_LY>`** **[ngày 21 tháng 10 năm 2011]`<NGAY_THAM_CHIEU>`** của **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** quy định về thanh tra viên và cộng tác viên thanh tra ;

**Thực thể:**
- `[e0]` **Nghị định số 92/2014/NĐ-CP** → `THAM_CHIEU_PHAP_LY` (span: `[1:4]`)
- `[e1]` **khoản 1 Điều 16 Nghị định số 97/2011/NĐ-CP** → `THAM_CHIEU_PHAP_LY` (span: `[15:22]`)
- `[e2]` **Căn cứ** → `TU_KHOA_PHAP_LY` (span: `[0:1]`)
- `[e3]` **sửa đổi , bổ sung** → `TU_KHOA_PHAP_LY` (span: `[12:15]`)
- `[e4]` **ngày 08 tháng 10 năm 2014** → `NGAY_THAM_CHIEU` (span: `[4:10]`)
- `[e5]` **ngày 21 tháng 10 năm 2011** → `NGAY_THAM_CHIEU` (span: `[22:28]`)
- `[e6]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[11:12]`)
- `[e7]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[29:30]`)

**Quan hệ:**
- (`e2` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e0` Nghị định số 92/2014/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e6` Chính phủ `[CO_QUAN_THAM_QUYEN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e0` Nghị định số 92/2014/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e3` sửa đổi , bổ sung `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e1` khoản 1 Điều 16 Nghị định số 97/2011/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e6` Chính phủ `[CO_QUAN_THAM_QUYEN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e1` khoản 1 Điều 16 Nghị định số 97/2011/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e0` Nghị định số 92/2014/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e4` ngày 08 tháng 10 năm 2014 `[NGAY_THAM_CHIEU]`)
- (`e1` khoản 1 Điều 16 Nghị định số 97/2011/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e5` ngày 21 tháng 10 năm 2011 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #02_2015_TT-TTCP_58849#preamble_context_8 (Loại: `preamble_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[02/2015/TT-TTCP]`<SO_HIEU>`** của **[Thanh tra Chính phủ]`<CO_QUAN_BAN_HANH>`** . Xét đề nghị của Vụ trưởng Vụ Tổ chức **[Cán bộ]`<CHU_THE_CA_NHAN>`** ,

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **02/2015/TT-TTCP** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Thanh tra Chính phủ** → `CO_QUAN_BAN_HANH` (span: `[4:6]`)
- `[e3]` **Cán bộ** → `CHU_THE_CA_NHAN` (span: `[13:14]`)

**Quan hệ:**
- (`e1` 02/2015/TT-TTCP `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Thanh tra Chính phủ `[CO_QUAN_BAN_HANH]`)
- (`e1` 02/2015/TT-TTCP `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)


---

### Mẫu #02_2015_TT-TTCP_58849#preamble_standalone_9 (Loại: `preamble_standalone`)
> Xét đề nghị của Vụ trưởng Vụ Tổ chức **[Cán bộ]`<CHU_THE_CA_NHAN>`** ,

**Thực thể:**
- `[e0]` **Cán bộ** → `CHU_THE_CA_NHAN` (span: `[6:7]`)


---

### Mẫu #02_2015_TT-TTCP_58849#preamble_context_10 (Loại: `preamble_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[02/2015/TT-TTCP]`<SO_HIEU>`** của **[Thanh tra Chính phủ]`<CO_QUAN_BAN_HANH>`** . Tổng **[Thanh tra Chính phủ]`<CO_QUAN_THAM_QUYEN>`** ban hành Thông tư quy định về trang phục của **[cán bộ]`<CHU_THE_CA_NHAN>`** , thanh tra viên , **[công chức]`<CHU_THE_CA_NHAN>`** , **[viên chức]`<CHU_THE_CA_NHAN>`** thuộc các cơ quan thanh tra nhà nước .

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **02/2015/TT-TTCP** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Thanh tra Chính phủ** → `CO_QUAN_BAN_HANH` (span: `[4:6]`)
- `[e3]` **Thanh tra Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[8:10]`)
- `[e4]` **cán bộ** → `CHU_THE_CA_NHAN` (span: `[16:17]`)
- `[e5]` **công chức** → `CHU_THE_CA_NHAN` (span: `[21:22]`)
- `[e6]` **viên chức** → `CHU_THE_CA_NHAN` (span: `[23:24]`)

**Quan hệ:**
- (`e1` 02/2015/TT-TTCP `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Thanh tra Chính phủ `[CO_QUAN_BAN_HANH]`)
- (`e1` 02/2015/TT-TTCP `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)


---

### Mẫu #02_2015_TT-TTCP_58849#preamble_standalone_11 (Loại: `preamble_standalone`)
> Tổng **[Thanh tra Chính phủ]`<CO_QUAN_THAM_QUYEN>`** ban hành Thông tư quy định về trang phục của **[cán bộ]`<CHU_THE_CA_NHAN>`** , thanh tra viên , **[công chức]`<CHU_THE_CA_NHAN>`** , **[viên chức]`<CHU_THE_CA_NHAN>`** thuộc các cơ quan thanh tra nhà nước .

**Thực thể:**
- `[e0]` **Thanh tra Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[1:3]`)
- `[e1]` **cán bộ** → `CHU_THE_CA_NHAN` (span: `[9:10]`)
- `[e2]` **công chức** → `CHU_THE_CA_NHAN` (span: `[14:15]`)
- `[e3]` **viên chức** → `CHU_THE_CA_NHAN` (span: `[16:17]`)


---

### Mẫu #02_2015_TT-TTCP_58849#body_context_12 (Loại: `body_context`)
> **[Thanh tra Chính phủ]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[02/2015/TT-TTCP]`<SO_HIEU>`** . **[Chương I. QUY ĐỊNH CHUNG]`<CHUONG>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[3:4]`)
- `[e1]` **02/2015/TT-TTCP** → `SO_HIEU` (span: `[5:6]`)
- `[e2]` **Thanh tra Chính phủ** → `CO_QUAN_BAN_HANH` (span: `[0:2]`)
- `[e3]` **Chương I. QUY ĐỊNH CHUNG** → `CHUONG` (span: `[7:11]`)

**Quan hệ:**
- (`e1` 02/2015/TT-TTCP `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Thanh tra Chính phủ `[CO_QUAN_BAN_HANH]`)
- (`e1` 02/2015/TT-TTCP `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Chương I. QUY ĐỊNH CHUNG `[CHUONG]`) ==[ **THUOC_VE** ]==> (`e1` 02/2015/TT-TTCP `[SO_HIEU]`)


---

### Mẫu #02_2015_TT-TTCP_58849#body_context_13 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[02/2015/TT-TTCP]`<SO_HIEU>`** ban hành **[ngày 16 tháng 03 năm 2015]`<NGAY_BAN_HANH>`** bởi **[Thanh tra Chính phủ]`<CO_QUAN_BAN_HANH>`** . **[Chương I]`<CHUONG>`** . **[Điều 1 . Phạm vi điều chỉnh . Thông tư này quy định về quản lý , sử dụng trang phục , màu sắc , chất liệu , quy cách trang phục của **[cán bộ]`<CHU_THE_CA_NHAN>`** , thanh tra viên , **[công chức]`<CHU_THE_CA_NHAN>`** , **[viên chức]`<CHU_THE_CA_NHAN>`** thuộc các cơ quan thanh tra nhà nước .]`<DIEU>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **02/2015/TT-TTCP** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Thanh tra Chính phủ** → `CO_QUAN_BAN_HANH` (span: `[11:13]`)
- `[e3]` **ngày 16 tháng 03 năm 2015** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Chương I** → `CHUONG` (span: `[14:16]`)
- `[e5]` **Điều 1 . Phạm vi điều chỉnh . Thông tư này quy định về quản lý , sử dụng trang phục , màu sắc , chất liệu , quy cách trang phục của cán bộ , thanh tra viên , công chức , viên chức thuộc các cơ quan thanh tra nhà nước .** → `DIEU` (span: `[17:53]`)
- `[e6]` **cán bộ** → `CHU_THE_CA_NHAN` (span: `[39:40]`) *(lồng trong `e5` (`DIEU`))*
- `[e7]` **công chức** → `CHU_THE_CA_NHAN` (span: `[44:45]`) *(lồng trong `e5` (`DIEU`))*
- `[e8]` **viên chức** → `CHU_THE_CA_NHAN` (span: `[46:47]`) *(lồng trong `e5` (`DIEU`))*

**Quan hệ:**
- (`e1` 02/2015/TT-TTCP `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Thanh tra Chính phủ `[CO_QUAN_BAN_HANH]`)
- (`e1` 02/2015/TT-TTCP `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 02/2015/TT-TTCP `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 16 tháng 03 năm 2015 `[NGAY_BAN_HANH]`)
- (`e4` Chương I `[CHUONG]`) ==[ **THUOC_VE** ]==> (`e1` 02/2015/TT-TTCP `[SO_HIEU]`)
- (`e5` Điều 1 . Phạm vi điều chỉnh . Thông tư này quy định về quản lý , sử dụng trang phục , màu sắc , chất liệu , quy cách trang phục của cán bộ , thanh tra viên , công chức , viên chức thuộc các cơ quan thanh tra nhà nước . `[DIEU]`) ==[ **THUOC_VE** ]==> (`e4` Chương I `[CHUONG]`)


---

### Mẫu #02_2015_TT-TTCP_58849#body_context_14 (Loại: `body_context`)
> **[Thanh tra Chính phủ]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[02/2015/TT-TTCP]`<SO_HIEU>`** . **[Điều 2]`<DIEU>`** . **[1 . Đối tượng được cấp trang phục là **[cán bộ]`<CHU_THE_CA_NHAN>`** , thanh tra viên , **[công chức]`<CHU_THE_CA_NHAN>`** , **[viên chức]`<CHU_THE_CA_NHAN>`** thuộc các cơ quan thanh tra nhà nước .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[3:4]`)
- `[e1]` **02/2015/TT-TTCP** → `SO_HIEU` (span: `[5:6]`)
- `[e2]` **Thanh tra Chính phủ** → `CO_QUAN_BAN_HANH` (span: `[0:2]`)
- `[e3]` **Điều 2** → `DIEU` (span: `[7:9]`)
- `[e4]` **1 . Đối tượng được cấp trang phục là cán bộ , thanh tra viên , công chức , viên chức thuộc các cơ quan thanh tra nhà nước .** → `KHOAN` (span: `[10:31]`)
- `[e5]` **cán bộ** → `CHU_THE_CA_NHAN` (span: `[17:18]`) *(lồng trong `e4` (`KHOAN`))*
- `[e6]` **công chức** → `CHU_THE_CA_NHAN` (span: `[22:23]`) *(lồng trong `e4` (`KHOAN`))*
- `[e7]` **viên chức** → `CHU_THE_CA_NHAN` (span: `[24:25]`) *(lồng trong `e4` (`KHOAN`))*

**Quan hệ:**
- (`e1` 02/2015/TT-TTCP `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Thanh tra Chính phủ `[CO_QUAN_BAN_HANH]`)
- (`e1` 02/2015/TT-TTCP `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 2 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 02/2015/TT-TTCP `[SO_HIEU]`)
- (`e4` 1 . Đối tượng được cấp trang phục là cán bộ , thanh tra viên , công chức , viên chức thuộc các cơ quan thanh tra nhà nước . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 2 `[DIEU]`)


---

### Mẫu #02_2015_TT-TTCP_58849#body_standalone_15 (Loại: `body_standalone`)
> **[Điều 2]`<DIEU>`** . **[1 . Đối tượng được cấp trang phục là **[cán bộ]`<CHU_THE_CA_NHAN>`** , thanh tra viên , **[công chức]`<CHU_THE_CA_NHAN>`** , **[viên chức]`<CHU_THE_CA_NHAN>`** thuộc các cơ quan thanh tra nhà nước .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 2** → `DIEU` (span: `[0:2]`)
- `[e1]` **1 . Đối tượng được cấp trang phục là cán bộ , thanh tra viên , công chức , viên chức thuộc các cơ quan thanh tra nhà nước .** → `KHOAN` (span: `[3:24]`)
- `[e2]` **cán bộ** → `CHU_THE_CA_NHAN` (span: `[10:11]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **công chức** → `CHU_THE_CA_NHAN` (span: `[15:16]`) *(lồng trong `e1` (`KHOAN`))*
- `[e4]` **viên chức** → `CHU_THE_CA_NHAN` (span: `[17:18]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 1 . Đối tượng được cấp trang phục là cán bộ , thanh tra viên , công chức , viên chức thuộc các cơ quan thanh tra nhà nước . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 2 `[DIEU]`)


---

### Mẫu #02_2015_TT-TTCP_58849#body_context_16 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[02/2015/TT-TTCP]`<SO_HIEU>`** ban hành **[ngày 16 tháng 03 năm 2015]`<NGAY_BAN_HANH>`** bởi **[Thanh tra Chính phủ]`<CO_QUAN_BAN_HANH>`** . **[Điều 2]`<DIEU>`** . **[2 . Đối với ngành , lĩnh vực cần có trang phục thanh tra riêng thì Bộ trưởng , Thủ trưởng cơ quan ngang bộ quản lý ngành , lĩnh vực thống nhất với Tổng **[Thanh tra Chính phủ]`<CO_QUAN_THAM_QUYEN>`** quy định trang phục thanh tra cho thanh tra viên của cơ quan thanh tra thuộc ngành , lĩnh vực đó .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **02/2015/TT-TTCP** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Thanh tra Chính phủ** → `CO_QUAN_BAN_HANH` (span: `[11:13]`)
- `[e3]` **ngày 16 tháng 03 năm 2015** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 2** → `DIEU` (span: `[14:16]`)
- `[e5]` **2 . Đối với ngành , lĩnh vực cần có trang phục thanh tra riêng thì Bộ trưởng , Thủ trưởng cơ quan ngang bộ quản lý ngành , lĩnh vực thống nhất với Tổng Thanh tra Chính phủ quy định trang phục thanh tra cho thanh tra viên của cơ quan thanh tra thuộc ngành , lĩnh vực đó .** → `KHOAN` (span: `[17:59]`)
- `[e6]` **Thanh tra Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[42:44]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 02/2015/TT-TTCP `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Thanh tra Chính phủ `[CO_QUAN_BAN_HANH]`)
- (`e1` 02/2015/TT-TTCP `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 02/2015/TT-TTCP `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 16 tháng 03 năm 2015 `[NGAY_BAN_HANH]`)
- (`e4` Điều 2 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 02/2015/TT-TTCP `[SO_HIEU]`)
- (`e5` 2 . Đối với ngành , lĩnh vực cần có trang phục thanh tra riêng thì Bộ trưởng , Thủ trưởng cơ quan ngang bộ quản lý ngành , lĩnh vực thống nhất với Tổng Thanh tra Chính phủ quy định trang phục thanh tra cho thanh tra viên của cơ quan thanh tra thuộc ngành , lĩnh vực đó . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 2 `[DIEU]`)


---

### Mẫu #02_2015_TT-TTCP_58849#body_standalone_17 (Loại: `body_standalone`)
> **[Điều 2]`<DIEU>`** . **[2 . Đối với ngành , lĩnh vực cần có trang phục thanh tra riêng thì Bộ trưởng , Thủ trưởng cơ quan ngang bộ quản lý ngành , lĩnh vực thống nhất với Tổng **[Thanh tra Chính phủ]`<CO_QUAN_THAM_QUYEN>`** quy định trang phục thanh tra cho thanh tra viên của cơ quan thanh tra thuộc ngành , lĩnh vực đó .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 2** → `DIEU` (span: `[0:2]`)
- `[e1]` **2 . Đối với ngành , lĩnh vực cần có trang phục thanh tra riêng thì Bộ trưởng , Thủ trưởng cơ quan ngang bộ quản lý ngành , lĩnh vực thống nhất với Tổng Thanh tra Chính phủ quy định trang phục thanh tra cho thanh tra viên của cơ quan thanh tra thuộc ngành , lĩnh vực đó .** → `KHOAN` (span: `[3:45]`)
- `[e2]` **Thanh tra Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[28:30]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 2 . Đối với ngành , lĩnh vực cần có trang phục thanh tra riêng thì Bộ trưởng , Thủ trưởng cơ quan ngang bộ quản lý ngành , lĩnh vực thống nhất với Tổng Thanh tra Chính phủ quy định trang phục thanh tra cho thanh tra viên của cơ quan thanh tra thuộc ngành , lĩnh vực đó . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 2 `[DIEU]`)


---

### Mẫu #02_2015_TT-TTCP_58849#body_context_18 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[02/2015/TT-TTCP]`<SO_HIEU>`** của **[Thanh tra Chính phủ]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Thanh tra]`<LINH_VUC>`** . **[Điều 2]`<DIEU>`** . **[3 . Trang phục của thanh tra viên Quốc phòng , thanh tra viên Công an thực hiện theo quy định của **[Bộ trưởng Bộ Quốc phòng]`<CO_QUAN_THAM_QUYEN>`** và **[Bộ trưởng Bộ Công an]`<CO_QUAN_THAM_QUYEN>`** .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **02/2015/TT-TTCP** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Thanh tra Chính phủ** → `CO_QUAN_BAN_HANH` (span: `[4:6]`)
- `[e3]` **Thanh tra** → `LINH_VUC` (span: `[8:9]`)
- `[e4]` **Điều 2** → `DIEU` (span: `[10:12]`)
- `[e5]` **3 . Trang phục của thanh tra viên Quốc phòng , thanh tra viên Công an thực hiện theo quy định của Bộ trưởng Bộ Quốc phòng và Bộ trưởng Bộ Công an .** → `KHOAN` (span: `[13:36]`)
- `[e6]` **Bộ trưởng Bộ Quốc phòng** → `CO_QUAN_THAM_QUYEN` (span: `[28:31]`) *(lồng trong `e5` (`KHOAN`))*
- `[e7]` **Bộ trưởng Bộ Công an** → `CO_QUAN_THAM_QUYEN` (span: `[32:35]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 02/2015/TT-TTCP `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Thanh tra Chính phủ `[CO_QUAN_BAN_HANH]`)
- (`e1` 02/2015/TT-TTCP `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 02/2015/TT-TTCP `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Thanh tra `[LINH_VUC]`)
- (`e4` Điều 2 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 02/2015/TT-TTCP `[SO_HIEU]`)
- (`e5` 3 . Trang phục của thanh tra viên Quốc phòng , thanh tra viên Công an thực hiện theo quy định của Bộ trưởng Bộ Quốc phòng và Bộ trưởng Bộ Công an . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 2 `[DIEU]`)
- (`e1` 02/2015/TT-TTCP `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Thanh tra `[LINH_VUC]`)
- (`e5` 3 . Trang phục của thanh tra viên Quốc phòng , thanh tra viên Công an thực hiện theo quy định của Bộ trưởng Bộ Quốc phòng và Bộ trưởng Bộ Công an . `[KHOAN]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Thanh tra `[LINH_VUC]`)


---

### Mẫu #02_2015_TT-TTCP_58849#body_standalone_19 (Loại: `body_standalone`)
> **[Điều 2]`<DIEU>`** . **[3 . Trang phục của thanh tra viên Quốc phòng , thanh tra viên Công an thực hiện theo quy định của **[Bộ trưởng Bộ Quốc phòng]`<CO_QUAN_THAM_QUYEN>`** và **[Bộ trưởng Bộ Công an]`<CO_QUAN_THAM_QUYEN>`** .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 2** → `DIEU` (span: `[0:2]`)
- `[e1]` **3 . Trang phục của thanh tra viên Quốc phòng , thanh tra viên Công an thực hiện theo quy định của Bộ trưởng Bộ Quốc phòng và Bộ trưởng Bộ Công an .** → `KHOAN` (span: `[3:26]`)
- `[e2]` **Bộ trưởng Bộ Quốc phòng** → `CO_QUAN_THAM_QUYEN` (span: `[18:21]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **Bộ trưởng Bộ Công an** → `CO_QUAN_THAM_QUYEN` (span: `[22:25]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 3 . Trang phục của thanh tra viên Quốc phòng , thanh tra viên Công an thực hiện theo quy định của Bộ trưởng Bộ Quốc phòng và Bộ trưởng Bộ Công an . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 2 `[DIEU]`)


---

### Mẫu #02_2015_TT-TTCP_58849#body_context_20 (Loại: `body_context`)
> **[Thanh tra Chính phủ]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[02/2015/TT-TTCP]`<SO_HIEU>`** . **[Điều 2]`<DIEU>`** . **[4 . Đối với các tỉnh phía Nam , do điều kiện thời tiết và trong phạm vi dự toán ngân sách được giao để may sắm trang phục , Thủ trưởng cơ quan thanh tra nhà nước cấp bộ , cấp tỉnh báo cáo Thủ trưởng cùng cấp xem xét , **[quyết định chuyển đổi]`<GIAY_TO_HO_SO>`** trang phục một áo măng tô thành hai áo xuân hè .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[3:4]`)
- `[e1]` **02/2015/TT-TTCP** → `SO_HIEU` (span: `[5:6]`)
- `[e2]` **Thanh tra Chính phủ** → `CO_QUAN_BAN_HANH` (span: `[0:2]`)
- `[e3]` **Điều 2** → `DIEU` (span: `[7:9]`)
- `[e4]` **4 . Đối với các tỉnh phía Nam , do điều kiện thời tiết và trong phạm vi dự toán ngân sách được giao để may sắm trang phục , Thủ trưởng cơ quan thanh tra nhà nước cấp bộ , cấp tỉnh báo cáo Thủ trưởng cùng cấp xem xét , quyết định chuyển đổi trang phục một áo măng tô thành hai áo xuân hè .** → `KHOAN` (span: `[10:59]`)
- `[e5]` **quyết định chuyển đổi** → `GIAY_TO_HO_SO` (span: `[47:49]`) *(lồng trong `e4` (`KHOAN`))*

**Quan hệ:**
- (`e1` 02/2015/TT-TTCP `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Thanh tra Chính phủ `[CO_QUAN_BAN_HANH]`)
- (`e1` 02/2015/TT-TTCP `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 2 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 02/2015/TT-TTCP `[SO_HIEU]`)
- (`e4` 4 . Đối với các tỉnh phía Nam , do điều kiện thời tiết và trong phạm vi dự toán ngân sách được giao để may sắm trang phục , Thủ trưởng cơ quan thanh tra nhà nước cấp bộ , cấp tỉnh báo cáo Thủ trưởng cùng cấp xem xét , quyết định chuyển đổi trang phục một áo măng tô thành hai áo xuân hè . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 2 `[DIEU]`)


---

### Mẫu #02_2015_TT-TTCP_58849#body_context_21 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[02/2015/TT-TTCP]`<SO_HIEU>`** ban hành **[ngày 16 tháng 03 năm 2015]`<NGAY_BAN_HANH>`** bởi **[Thanh tra Chính phủ]`<CO_QUAN_BAN_HANH>`** . **[Chương II]`<CHUONG>`** . **[Điều 3 . Về trang phục . Trang phục **[quy định tại]`<TU_KHOA_PHAP_LY>`** **[Thông tư này]`<THAM_CHIEU_PHAP_LY>`** bao gồm : quần áo thu đông , áo măng tô , áo sơ mi dài tay , quần xuân hè , áo xuân hè ngắn tay , áo xuân hè dài tay , **[mũ bảo hiểm]`<TAI_SAN_VAT_CHAT>`** , thắt lưng da , giầy da , dép quai hậu , bít tất , cà vạt , quần áo mưa , cặp tài liệu , mũ kêpi , sao mũ , cành tùng , cúc cấp hiệu , cầu vai , cấp hàm .]`<DIEU>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **02/2015/TT-TTCP** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Thanh tra Chính phủ** → `CO_QUAN_BAN_HANH` (span: `[11:13]`)
- `[e3]` **ngày 16 tháng 03 năm 2015** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Chương II** → `CHUONG` (span: `[14:16]`)
- `[e5]` **Điều 3 . Về trang phục . Trang phục quy định tại Thông tư này bao gồm : quần áo thu đông , áo măng tô , áo sơ mi dài tay , quần xuân hè , áo xuân hè ngắn tay , áo xuân hè dài tay , mũ bảo hiểm , thắt lưng da , giầy da , dép quai hậu , bít tất , cà vạt , quần áo mưa , cặp tài liệu , mũ kêpi , sao mũ , cành tùng , cúc cấp hiệu , cầu vai , cấp hàm .** → `DIEU` (span: `[17:95]`)
- `[e6]` **Thông tư này** → `THAM_CHIEU_PHAP_LY` (span: `[26:28]`) *(lồng trong `e5` (`DIEU`))*
- `[e7]` **quy định tại** → `TU_KHOA_PHAP_LY` (span: `[24:26]`) *(lồng trong `e5` (`DIEU`))*
- `[e8]` **mũ bảo hiểm** → `TAI_SAN_VAT_CHAT` (span: `[58:60]`) *(lồng trong `e5` (`DIEU`))*

**Quan hệ:**
- (`e1` 02/2015/TT-TTCP `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Thanh tra Chính phủ `[CO_QUAN_BAN_HANH]`)
- (`e1` 02/2015/TT-TTCP `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 02/2015/TT-TTCP `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 16 tháng 03 năm 2015 `[NGAY_BAN_HANH]`)
- (`e4` Chương II `[CHUONG]`) ==[ **THUOC_VE** ]==> (`e1` 02/2015/TT-TTCP `[SO_HIEU]`)
- (`e5` Điều 3 . Về trang phục . Trang phục quy định tại Thông tư này bao gồm : quần áo thu đông , áo măng tô , áo sơ mi dài tay , quần xuân hè , áo xuân hè ngắn tay , áo xuân hè dài tay , mũ bảo hiểm , thắt lưng da , giầy da , dép quai hậu , bít tất , cà vạt , quần áo mưa , cặp tài liệu , mũ kêpi , sao mũ , cành tùng , cúc cấp hiệu , cầu vai , cấp hàm . `[DIEU]`) ==[ **THUOC_VE** ]==> (`e4` Chương II `[CHUONG]`)
- (`e7` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e6` Thông tư này `[THAM_CHIEU_PHAP_LY]`)
- (`e5` Điều 3 . Về trang phục . Trang phục quy định tại Thông tư này bao gồm : quần áo thu đông , áo măng tô , áo sơ mi dài tay , quần xuân hè , áo xuân hè ngắn tay , áo xuân hè dài tay , mũ bảo hiểm , thắt lưng da , giầy da , dép quai hậu , bít tất , cà vạt , quần áo mưa , cặp tài liệu , mũ kêpi , sao mũ , cành tùng , cúc cấp hiệu , cầu vai , cấp hàm . `[DIEU]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e6` Thông tư này `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #02_2015_TT-TTCP_58849#body_standalone_22 (Loại: `body_standalone`)
> **[Điều 3 . Về trang phục . Trang phục **[quy định tại]`<TU_KHOA_PHAP_LY>`** **[Thông tư này]`<THAM_CHIEU_PHAP_LY>`** bao gồm : quần áo thu đông , áo măng tô , áo sơ mi dài tay , quần xuân hè , áo xuân hè ngắn tay , áo xuân hè dài tay , **[mũ bảo hiểm]`<TAI_SAN_VAT_CHAT>`** , thắt lưng da , giầy da , dép quai hậu , bít tất , cà vạt , quần áo mưa , cặp tài liệu , mũ kêpi , sao mũ , cành tùng , cúc cấp hiệu , cầu vai , cấp hàm .]`<DIEU>`**

**Thực thể:**
- `[e0]` **Điều 3 . Về trang phục . Trang phục quy định tại Thông tư này bao gồm : quần áo thu đông , áo măng tô , áo sơ mi dài tay , quần xuân hè , áo xuân hè ngắn tay , áo xuân hè dài tay , mũ bảo hiểm , thắt lưng da , giầy da , dép quai hậu , bít tất , cà vạt , quần áo mưa , cặp tài liệu , mũ kêpi , sao mũ , cành tùng , cúc cấp hiệu , cầu vai , cấp hàm .** → `DIEU` (span: `[0:78]`)
- `[e1]` **Thông tư này** → `THAM_CHIEU_PHAP_LY` (span: `[9:11]`) *(lồng trong `e0` (`DIEU`))*
- `[e2]` **quy định tại** → `TU_KHOA_PHAP_LY` (span: `[7:9]`) *(lồng trong `e0` (`DIEU`))*
- `[e3]` **mũ bảo hiểm** → `TAI_SAN_VAT_CHAT` (span: `[41:43]`) *(lồng trong `e0` (`DIEU`))*

**Quan hệ:**
- (`e2` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e1` Thông tư này `[THAM_CHIEU_PHAP_LY]`)
- (`e0` Điều 3 . Về trang phục . Trang phục quy định tại Thông tư này bao gồm : quần áo thu đông , áo măng tô , áo sơ mi dài tay , quần xuân hè , áo xuân hè ngắn tay , áo xuân hè dài tay , mũ bảo hiểm , thắt lưng da , giầy da , dép quai hậu , bít tất , cà vạt , quần áo mưa , cặp tài liệu , mũ kêpi , sao mũ , cành tùng , cúc cấp hiệu , cầu vai , cấp hàm . `[DIEU]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e1` Thông tư này `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #02_2015_TT-TTCP_58849#body_context_23 (Loại: `body_context`)
> **[Thanh tra Chính phủ]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[02/2015/TT-TTCP]`<SO_HIEU>`** . **[Điều 4]`<DIEU>`** . **[Khoản 1]`<KHOAN>`** . **[a ) Chất liệu : - Trọng lượng : 245g/m 2 .]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[3:4]`)
- `[e1]` **02/2015/TT-TTCP** → `SO_HIEU` (span: `[5:6]`)
- `[e2]` **Thanh tra Chính phủ** → `CO_QUAN_BAN_HANH` (span: `[0:2]`)
- `[e3]` **Điều 4** → `DIEU` (span: `[7:9]`)
- `[e4]` **Khoản 1** → `KHOAN` (span: `[10:12]`)
- `[e5]` **a ) Chất liệu : - Trọng lượng : 245g/m 2 .** → `DIEM` (span: `[13:23]`)

**Quan hệ:**
- (`e1` 02/2015/TT-TTCP `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Thanh tra Chính phủ `[CO_QUAN_BAN_HANH]`)
- (`e1` 02/2015/TT-TTCP `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 4 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 02/2015/TT-TTCP `[SO_HIEU]`)
- (`e4` Khoản 1 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 4 `[DIEU]`)
- (`e5` a ) Chất liệu : - Trọng lượng : 245g/m 2 . `[DIEM]`) ==[ **THUOC_VE** ]==> (`e4` Khoản 1 `[KHOAN]`)


---

### Mẫu #02_2015_TT-TTCP_58849#body_context_24 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[02/2015/TT-TTCP]`<SO_HIEU>`** ban hành **[ngày 16 tháng 03 năm 2015]`<NGAY_BAN_HANH>`** bởi **[Thanh tra Chính phủ]`<CO_QUAN_BAN_HANH>`** . **[Điều 4]`<DIEU>`** . **[Khoản 2]`<KHOAN>`** . **[b ) Màu sắc : xanh rêu đậm .]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **02/2015/TT-TTCP** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Thanh tra Chính phủ** → `CO_QUAN_BAN_HANH` (span: `[11:13]`)
- `[e3]` **ngày 16 tháng 03 năm 2015** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 4** → `DIEU` (span: `[14:16]`)
- `[e5]` **Khoản 2** → `KHOAN` (span: `[17:19]`)
- `[e6]` **b ) Màu sắc : xanh rêu đậm .** → `DIEM` (span: `[20:28]`)

**Quan hệ:**
- (`e1` 02/2015/TT-TTCP `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Thanh tra Chính phủ `[CO_QUAN_BAN_HANH]`)
- (`e1` 02/2015/TT-TTCP `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 02/2015/TT-TTCP `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 16 tháng 03 năm 2015 `[NGAY_BAN_HANH]`)
- (`e4` Điều 4 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 02/2015/TT-TTCP `[SO_HIEU]`)
- (`e5` Khoản 2 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 4 `[DIEU]`)
- (`e6` b ) Màu sắc : xanh rêu đậm . `[DIEM]`) ==[ **THUOC_VE** ]==> (`e5` Khoản 2 `[KHOAN]`)


---

### Mẫu #02_2015_TT-TTCP_58849#body_context_25 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[02/2015/TT-TTCP]`<SO_HIEU>`** của **[Thanh tra Chính phủ]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Thanh tra]`<LINH_VUC>`** . **[Điều 4]`<DIEU>`** . **[4 . Áo sơmi dài tay]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **02/2015/TT-TTCP** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Thanh tra Chính phủ** → `CO_QUAN_BAN_HANH` (span: `[4:6]`)
- `[e3]` **Thanh tra** → `LINH_VUC` (span: `[8:9]`)
- `[e4]` **Điều 4** → `DIEU` (span: `[10:12]`)
- `[e5]` **4 . Áo sơmi dài tay** → `KHOAN` (span: `[13:19]`)

**Quan hệ:**
- (`e1` 02/2015/TT-TTCP `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Thanh tra Chính phủ `[CO_QUAN_BAN_HANH]`)
- (`e1` 02/2015/TT-TTCP `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 02/2015/TT-TTCP `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Thanh tra `[LINH_VUC]`)
- (`e4` Điều 4 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 02/2015/TT-TTCP `[SO_HIEU]`)
- (`e5` 4 . Áo sơmi dài tay `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 4 `[DIEU]`)
- (`e1` 02/2015/TT-TTCP `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Thanh tra `[LINH_VUC]`)
- (`e5` 4 . Áo sơmi dài tay `[KHOAN]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Thanh tra `[LINH_VUC]`)


---

### Mẫu #02_2015_TT-TTCP_58849#body_context_26 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[02/2015/TT-TTCP]`<SO_HIEU>`** ban hành **[ngày 16 tháng 03 năm 2015]`<NGAY_BAN_HANH>`** bởi **[Thanh tra Chính phủ]`<CO_QUAN_BAN_HANH>`** . **[Điều 4]`<DIEU>`** . **[Khoản 5]`<KHOAN>`** . **[a ) Chất liệu : - Mật độ : dọc 320s/cm ; ngang 286s/cm ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **02/2015/TT-TTCP** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Thanh tra Chính phủ** → `CO_QUAN_BAN_HANH` (span: `[11:13]`)
- `[e3]` **ngày 16 tháng 03 năm 2015** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 4** → `DIEU` (span: `[14:16]`)
- `[e5]` **Khoản 5** → `KHOAN` (span: `[17:19]`)
- `[e6]` **a ) Chất liệu : - Mật độ : dọc 320s/cm ; ngang 286s/cm ;** → `DIEM` (span: `[20:33]`)

**Quan hệ:**
- (`e1` 02/2015/TT-TTCP `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Thanh tra Chính phủ `[CO_QUAN_BAN_HANH]`)
- (`e1` 02/2015/TT-TTCP `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 02/2015/TT-TTCP `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 16 tháng 03 năm 2015 `[NGAY_BAN_HANH]`)
- (`e4` Điều 4 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 02/2015/TT-TTCP `[SO_HIEU]`)
- (`e5` Khoản 5 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 4 `[DIEU]`)
- (`e6` a ) Chất liệu : - Mật độ : dọc 320s/cm ; ngang 286s/cm ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e5` Khoản 5 `[KHOAN]`)


---

### Mẫu #02_2015_TT-TTCP_58849#body_context_27 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[02/2015/TT-TTCP]`<SO_HIEU>`** của **[Thanh tra Chính phủ]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Thanh tra]`<LINH_VUC>`** . **[Điều 4]`<DIEU>`** . **[Khoản 6]`<KHOAN>`** . **[b ) Màu sắc : xanh nhạt .]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **02/2015/TT-TTCP** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Thanh tra Chính phủ** → `CO_QUAN_BAN_HANH` (span: `[4:6]`)
- `[e3]` **Thanh tra** → `LINH_VUC` (span: `[8:9]`)
- `[e4]` **Điều 4** → `DIEU` (span: `[10:12]`)
- `[e5]` **Khoản 6** → `KHOAN` (span: `[13:15]`)
- `[e6]` **b ) Màu sắc : xanh nhạt .** → `DIEM` (span: `[16:23]`)

**Quan hệ:**
- (`e1` 02/2015/TT-TTCP `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Thanh tra Chính phủ `[CO_QUAN_BAN_HANH]`)
- (`e1` 02/2015/TT-TTCP `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 02/2015/TT-TTCP `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Thanh tra `[LINH_VUC]`)
- (`e4` Điều 4 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 02/2015/TT-TTCP `[SO_HIEU]`)
- (`e5` Khoản 6 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 4 `[DIEU]`)
- (`e6` b ) Màu sắc : xanh nhạt . `[DIEM]`) ==[ **THUOC_VE** ]==> (`e5` Khoản 6 `[KHOAN]`)
- (`e1` 02/2015/TT-TTCP `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Thanh tra `[LINH_VUC]`)
- (`e6` b ) Màu sắc : xanh nhạt . `[DIEM]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Thanh tra `[LINH_VUC]`)


---

### Mẫu #02_2015_TT-TTCP_58849#body_context_28 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[02/2015/TT-TTCP]`<SO_HIEU>`** ban hành **[ngày 16 tháng 03 năm 2015]`<NGAY_BAN_HANH>`** bởi **[Thanh tra Chính phủ]`<CO_QUAN_BAN_HANH>`** . **[Điều 4]`<DIEU>`** . **[8 . Dép quai hậu - Độ bền kéo đứt : ( Mpa ) ≥ 18 ; ( N / cm 2 ) ≥ 3 ;]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **02/2015/TT-TTCP** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Thanh tra Chính phủ** → `CO_QUAN_BAN_HANH` (span: `[11:13]`)
- `[e3]` **ngày 16 tháng 03 năm 2015** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 4** → `DIEU` (span: `[14:16]`)
- `[e5]` **8 . Dép quai hậu - Độ bền kéo đứt : ( Mpa ) ≥ 18 ; ( N / cm 2 ) ≥ 3 ;** → `KHOAN` (span: `[17:42]`)

**Quan hệ:**
- (`e1` 02/2015/TT-TTCP `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Thanh tra Chính phủ `[CO_QUAN_BAN_HANH]`)
- (`e1` 02/2015/TT-TTCP `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 02/2015/TT-TTCP `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 16 tháng 03 năm 2015 `[NGAY_BAN_HANH]`)
- (`e4` Điều 4 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 02/2015/TT-TTCP `[SO_HIEU]`)
- (`e5` 8 . Dép quai hậu - Độ bền kéo đứt : ( Mpa ) ≥ 18 ; ( N / cm 2 ) ≥ 3 ; `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 4 `[DIEU]`)


---

### Mẫu #02_2015_TT-TTCP_58849#body_context_29 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[02/2015/TT-TTCP]`<SO_HIEU>`** của **[Thanh tra Chính phủ]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Thanh tra]`<LINH_VUC>`** . **[Điều 5]`<DIEU>`** . **[Khoản 1]`<KHOAN>`** . **[a ) Chất liệu : - Trọng lượng : 245g/m 2 .]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **02/2015/TT-TTCP** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Thanh tra Chính phủ** → `CO_QUAN_BAN_HANH` (span: `[4:6]`)
- `[e3]` **Thanh tra** → `LINH_VUC` (span: `[8:9]`)
- `[e4]` **Điều 5** → `DIEU` (span: `[10:12]`)
- `[e5]` **Khoản 1** → `KHOAN` (span: `[13:15]`)
- `[e6]` **a ) Chất liệu : - Trọng lượng : 245g/m 2 .** → `DIEM` (span: `[16:26]`)

**Quan hệ:**
- (`e1` 02/2015/TT-TTCP `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Thanh tra Chính phủ `[CO_QUAN_BAN_HANH]`)
- (`e1` 02/2015/TT-TTCP `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 02/2015/TT-TTCP `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Thanh tra `[LINH_VUC]`)
- (`e4` Điều 5 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 02/2015/TT-TTCP `[SO_HIEU]`)
- (`e5` Khoản 1 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 5 `[DIEU]`)
- (`e6` a ) Chất liệu : - Trọng lượng : 245g/m 2 . `[DIEM]`) ==[ **THUOC_VE** ]==> (`e5` Khoản 1 `[KHOAN]`)
- (`e1` 02/2015/TT-TTCP `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Thanh tra `[LINH_VUC]`)
- (`e6` a ) Chất liệu : - Trọng lượng : 245g/m 2 . `[DIEM]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Thanh tra `[LINH_VUC]`)


---

### Mẫu #02_2015_TT-TTCP_58849#body_context_30 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[02/2015/TT-TTCP]`<SO_HIEU>`** ban hành **[ngày 16 tháng 03 năm 2015]`<NGAY_BAN_HANH>`** bởi **[Thanh tra Chính phủ]`<CO_QUAN_BAN_HANH>`** . **[Điều 5]`<DIEU>`** . **[Khoản 2]`<KHOAN>`** . **[b ) Màu sắc : xanh rêu đậm .]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **02/2015/TT-TTCP** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Thanh tra Chính phủ** → `CO_QUAN_BAN_HANH` (span: `[11:13]`)
- `[e3]` **ngày 16 tháng 03 năm 2015** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 5** → `DIEU` (span: `[14:16]`)
- `[e5]` **Khoản 2** → `KHOAN` (span: `[17:19]`)
- `[e6]` **b ) Màu sắc : xanh rêu đậm .** → `DIEM` (span: `[20:28]`)

**Quan hệ:**
- (`e1` 02/2015/TT-TTCP `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Thanh tra Chính phủ `[CO_QUAN_BAN_HANH]`)
- (`e1` 02/2015/TT-TTCP `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 02/2015/TT-TTCP `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 16 tháng 03 năm 2015 `[NGAY_BAN_HANH]`)
- (`e4` Điều 5 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 02/2015/TT-TTCP `[SO_HIEU]`)
- (`e5` Khoản 2 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 5 `[DIEU]`)
- (`e6` b ) Màu sắc : xanh rêu đậm . `[DIEM]`) ==[ **THUOC_VE** ]==> (`e5` Khoản 2 `[KHOAN]`)


---

### Mẫu #02_2015_TT-TTCP_58849#body_standalone_31 (Loại: `body_standalone`)
> **[Điều 5]`<DIEU>`** . **[Khoản 2]`<KHOAN>`** . **[b ) Màu sắc : xanh rêu đậm .]`<DIEM>`**

**Thực thể:**
- `[e0]` **Điều 5** → `DIEU` (span: `[0:2]`)
- `[e1]` **Khoản 2** → `KHOAN` (span: `[3:5]`)
- `[e2]` **b ) Màu sắc : xanh rêu đậm .** → `DIEM` (span: `[6:14]`)

**Quan hệ:**
- (`e1` Khoản 2 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 5 `[DIEU]`)
- (`e2` b ) Màu sắc : xanh rêu đậm . `[DIEM]`) ==[ **THUOC_VE** ]==> (`e1` Khoản 2 `[KHOAN]`)


---

### Mẫu #02_2015_TT-TTCP_58849#body_context_32 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[02/2015/TT-TTCP]`<SO_HIEU>`** của **[Thanh tra Chính phủ]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Thanh tra]`<LINH_VUC>`** . **[Điều 5]`<DIEU>`** . **[4 . Juyp]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **02/2015/TT-TTCP** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Thanh tra Chính phủ** → `CO_QUAN_BAN_HANH` (span: `[4:6]`)
- `[e3]` **Thanh tra** → `LINH_VUC` (span: `[8:9]`)
- `[e4]` **Điều 5** → `DIEU` (span: `[10:12]`)
- `[e5]` **4 . Juyp** → `KHOAN` (span: `[13:16]`)

**Quan hệ:**
- (`e1` 02/2015/TT-TTCP `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Thanh tra Chính phủ `[CO_QUAN_BAN_HANH]`)
- (`e1` 02/2015/TT-TTCP `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 02/2015/TT-TTCP `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Thanh tra `[LINH_VUC]`)
- (`e4` Điều 5 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 02/2015/TT-TTCP `[SO_HIEU]`)
- (`e5` 4 . Juyp `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 5 `[DIEU]`)
- (`e1` 02/2015/TT-TTCP `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Thanh tra `[LINH_VUC]`)
- (`e5` 4 . Juyp `[KHOAN]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Thanh tra `[LINH_VUC]`)


---

### Mẫu #02_2015_TT-TTCP_58849#body_standalone_33 (Loại: `body_standalone`)
> **[Điều 5]`<DIEU>`** . **[4 . Juyp]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 5** → `DIEU` (span: `[0:2]`)
- `[e1]` **4 . Juyp** → `KHOAN` (span: `[3:6]`)

**Quan hệ:**
- (`e1` 4 . Juyp `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 5 `[DIEU]`)


---

### Mẫu #02_2015_TT-TTCP_58849#body_context_34 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[02/2015/TT-TTCP]`<SO_HIEU>`** ban hành **[ngày 16 tháng 03 năm 2015]`<NGAY_BAN_HANH>`** bởi **[Thanh tra Chính phủ]`<CO_QUAN_BAN_HANH>`** . **[Điều 5]`<DIEU>`** . **[Khoản 5]`<KHOAN>`** . **[a ) Chất liệu : - Vải pôpơlin 8151 PE / VIS ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **02/2015/TT-TTCP** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Thanh tra Chính phủ** → `CO_QUAN_BAN_HANH` (span: `[11:13]`)
- `[e3]` **ngày 16 tháng 03 năm 2015** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 5** → `DIEU` (span: `[14:16]`)
- `[e5]` **Khoản 5** → `KHOAN` (span: `[17:19]`)
- `[e6]` **a ) Chất liệu : - Vải pôpơlin 8151 PE / VIS ;** → `DIEM` (span: `[20:32]`)

**Quan hệ:**
- (`e1` 02/2015/TT-TTCP `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Thanh tra Chính phủ `[CO_QUAN_BAN_HANH]`)
- (`e1` 02/2015/TT-TTCP `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 02/2015/TT-TTCP `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 16 tháng 03 năm 2015 `[NGAY_BAN_HANH]`)
- (`e4` Điều 5 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 02/2015/TT-TTCP `[SO_HIEU]`)
- (`e5` Khoản 5 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 5 `[DIEU]`)
- (`e6` a ) Chất liệu : - Vải pôpơlin 8151 PE / VIS ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e5` Khoản 5 `[KHOAN]`)


---

### Mẫu #02_2015_TT-TTCP_58849#body_context_35 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[02/2015/TT-TTCP]`<SO_HIEU>`** của **[Thanh tra Chính phủ]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Thanh tra]`<LINH_VUC>`** . **[Điều 5]`<DIEU>`** . **[Khoản 6]`<KHOAN>`** . **[a ) Chất liệu : - Trọng lượng : 145g/m 2 .]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **02/2015/TT-TTCP** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Thanh tra Chính phủ** → `CO_QUAN_BAN_HANH` (span: `[4:6]`)
- `[e3]` **Thanh tra** → `LINH_VUC` (span: `[8:9]`)
- `[e4]` **Điều 5** → `DIEU` (span: `[10:12]`)
- `[e5]` **Khoản 6** → `KHOAN` (span: `[13:15]`)
- `[e6]` **a ) Chất liệu : - Trọng lượng : 145g/m 2 .** → `DIEM` (span: `[16:26]`)

**Quan hệ:**
- (`e1` 02/2015/TT-TTCP `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Thanh tra Chính phủ `[CO_QUAN_BAN_HANH]`)
- (`e1` 02/2015/TT-TTCP `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 02/2015/TT-TTCP `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Thanh tra `[LINH_VUC]`)
- (`e4` Điều 5 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 02/2015/TT-TTCP `[SO_HIEU]`)
- (`e5` Khoản 6 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 5 `[DIEU]`)
- (`e6` a ) Chất liệu : - Trọng lượng : 145g/m 2 . `[DIEM]`) ==[ **THUOC_VE** ]==> (`e5` Khoản 6 `[KHOAN]`)
- (`e1` 02/2015/TT-TTCP `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Thanh tra `[LINH_VUC]`)
- (`e6` a ) Chất liệu : - Trọng lượng : 145g/m 2 . `[DIEM]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Thanh tra `[LINH_VUC]`)


---

### Mẫu #02_2015_TT-TTCP_58849#body_standalone_36 (Loại: `body_standalone`)
> **[Điều 5]`<DIEU>`** . **[Khoản 6]`<KHOAN>`** . **[a ) Chất liệu : - Trọng lượng : 145g/m 2 .]`<DIEM>`**

**Thực thể:**
- `[e0]` **Điều 5** → `DIEU` (span: `[0:2]`)
- `[e1]` **Khoản 6** → `KHOAN` (span: `[3:5]`)
- `[e2]` **a ) Chất liệu : - Trọng lượng : 145g/m 2 .** → `DIEM` (span: `[6:16]`)

**Quan hệ:**
- (`e1` Khoản 6 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 5 `[DIEU]`)
- (`e2` a ) Chất liệu : - Trọng lượng : 145g/m 2 . `[DIEM]`) ==[ **THUOC_VE** ]==> (`e1` Khoản 6 `[KHOAN]`)


---

### Mẫu #02_2015_TT-TTCP_58849#body_context_37 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[02/2015/TT-TTCP]`<SO_HIEU>`** ban hành **[ngày 16 tháng 03 năm 2015]`<NGAY_BAN_HANH>`** bởi **[Thanh tra Chính phủ]`<CO_QUAN_BAN_HANH>`** . **[Điều 5]`<DIEU>`** . **[8 . Giầy da - Da : nappa màu đen ;]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **02/2015/TT-TTCP** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Thanh tra Chính phủ** → `CO_QUAN_BAN_HANH` (span: `[11:13]`)
- `[e3]` **ngày 16 tháng 03 năm 2015** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 5** → `DIEU` (span: `[14:16]`)
- `[e5]` **8 . Giầy da - Da : nappa màu đen ;** → `KHOAN` (span: `[17:28]`)

**Quan hệ:**
- (`e1` 02/2015/TT-TTCP `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Thanh tra Chính phủ `[CO_QUAN_BAN_HANH]`)
- (`e1` 02/2015/TT-TTCP `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 02/2015/TT-TTCP `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 16 tháng 03 năm 2015 `[NGAY_BAN_HANH]`)
- (`e4` Điều 5 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 02/2015/TT-TTCP `[SO_HIEU]`)
- (`e5` 8 . Giầy da - Da : nappa màu đen ; `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 5 `[DIEU]`)


---

### Mẫu #02_2015_TT-TTCP_58849#body_context_38 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[02/2015/TT-TTCP]`<SO_HIEU>`** của **[Thanh tra Chính phủ]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Thanh tra]`<LINH_VUC>`** . **[Điều 5]`<DIEU>`** . **[9 . Dép quai hậu - Kiểu dáng : quai ngang ;]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **02/2015/TT-TTCP** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Thanh tra Chính phủ** → `CO_QUAN_BAN_HANH` (span: `[4:6]`)
- `[e3]` **Thanh tra** → `LINH_VUC` (span: `[8:9]`)
- `[e4]` **Điều 5** → `DIEU` (span: `[10:12]`)
- `[e5]` **9 . Dép quai hậu - Kiểu dáng : quai ngang ;** → `KHOAN` (span: `[13:23]`)

**Quan hệ:**
- (`e1` 02/2015/TT-TTCP `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Thanh tra Chính phủ `[CO_QUAN_BAN_HANH]`)
- (`e1` 02/2015/TT-TTCP `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 02/2015/TT-TTCP `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Thanh tra `[LINH_VUC]`)
- (`e4` Điều 5 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 02/2015/TT-TTCP `[SO_HIEU]`)
- (`e5` 9 . Dép quai hậu - Kiểu dáng : quai ngang ; `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 5 `[DIEU]`)
- (`e1` 02/2015/TT-TTCP `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Thanh tra `[LINH_VUC]`)
- (`e5` 9 . Dép quai hậu - Kiểu dáng : quai ngang ; `[KHOAN]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Thanh tra `[LINH_VUC]`)


---

### Mẫu #02_2015_TT-TTCP_58849#body_context_39 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[02/2015/TT-TTCP]`<SO_HIEU>`** của **[Thanh tra Chính phủ]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Thanh tra]`<LINH_VUC>`** . **[Điều 6]`<DIEU>`** . **[Khoản 2]`<KHOAN>`** . **[a ) Chất liệu : - Vải Tuytsi pha len , ký hiệu : TW8058 - 1 ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **02/2015/TT-TTCP** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Thanh tra Chính phủ** → `CO_QUAN_BAN_HANH` (span: `[4:6]`)
- `[e3]` **Thanh tra** → `LINH_VUC` (span: `[8:9]`)
- `[e4]` **Điều 6** → `DIEU` (span: `[10:12]`)
- `[e5]` **Khoản 2** → `KHOAN` (span: `[13:15]`)
- `[e6]` **a ) Chất liệu : - Vải Tuytsi pha len , ký hiệu : TW8058 - 1 ;** → `DIEM` (span: `[16:32]`)

**Quan hệ:**
- (`e1` 02/2015/TT-TTCP `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Thanh tra Chính phủ `[CO_QUAN_BAN_HANH]`)
- (`e1` 02/2015/TT-TTCP `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 02/2015/TT-TTCP `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Thanh tra `[LINH_VUC]`)
- (`e4` Điều 6 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 02/2015/TT-TTCP `[SO_HIEU]`)
- (`e5` Khoản 2 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 6 `[DIEU]`)
- (`e6` a ) Chất liệu : - Vải Tuytsi pha len , ký hiệu : TW8058 - 1 ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e5` Khoản 2 `[KHOAN]`)
- (`e1` 02/2015/TT-TTCP `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Thanh tra `[LINH_VUC]`)
- (`e6` a ) Chất liệu : - Vải Tuytsi pha len , ký hiệu : TW8058 - 1 ; `[DIEM]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Thanh tra `[LINH_VUC]`)


---

### Mẫu #02_2015_TT-TTCP_58849#body_context_40 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[02/2015/TT-TTCP]`<SO_HIEU>`** ban hành **[ngày 16 tháng 03 năm 2015]`<NGAY_BAN_HANH>`** bởi **[Thanh tra Chính phủ]`<CO_QUAN_BAN_HANH>`** . **[Điều 6]`<DIEU>`** . **[3 . Bít tất - Chất liệu : sợi cotton tổng hợp : cotton **[40 %]`<NGUONG_DINH_LUONG>`** ; acrylic **[23 %]`<NGUONG_DINH_LUONG>`** ; spandex **[37 %]`<NGUONG_DINH_LUONG>`** ;]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **02/2015/TT-TTCP** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Thanh tra Chính phủ** → `CO_QUAN_BAN_HANH` (span: `[11:13]`)
- `[e3]` **ngày 16 tháng 03 năm 2015** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 6** → `DIEU` (span: `[14:16]`)
- `[e5]` **3 . Bít tất - Chất liệu : sợi cotton tổng hợp : cotton 40 % ; acrylic 23 % ; spandex 37 % ;** → `KHOAN` (span: `[17:39]`)
- `[e6]` **40 %** → `NGUONG_DINH_LUONG` (span: `[28:30]`) *(lồng trong `e5` (`KHOAN`))*
- `[e7]` **23 %** → `NGUONG_DINH_LUONG` (span: `[32:34]`) *(lồng trong `e5` (`KHOAN`))*
- `[e8]` **37 %** → `NGUONG_DINH_LUONG` (span: `[36:38]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 02/2015/TT-TTCP `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Thanh tra Chính phủ `[CO_QUAN_BAN_HANH]`)
- (`e1` 02/2015/TT-TTCP `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 02/2015/TT-TTCP `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 16 tháng 03 năm 2015 `[NGAY_BAN_HANH]`)
- (`e4` Điều 6 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 02/2015/TT-TTCP `[SO_HIEU]`)
- (`e5` 3 . Bít tất - Chất liệu : sợi cotton tổng hợp : cotton 40 % ; acrylic 23 % ; spandex 37 % ; `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 6 `[DIEU]`)


---

### Mẫu #02_2015_TT-TTCP_58849#body_standalone_41 (Loại: `body_standalone`)
> **[Điều 6]`<DIEU>`** . **[3 . Bít tất - Chất liệu : sợi cotton tổng hợp : cotton **[40 %]`<NGUONG_DINH_LUONG>`** ; acrylic **[23 %]`<NGUONG_DINH_LUONG>`** ; spandex **[37 %]`<NGUONG_DINH_LUONG>`** ;]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 6** → `DIEU` (span: `[0:2]`)
- `[e1]` **3 . Bít tất - Chất liệu : sợi cotton tổng hợp : cotton 40 % ; acrylic 23 % ; spandex 37 % ;** → `KHOAN` (span: `[3:25]`)
- `[e2]` **40 %** → `NGUONG_DINH_LUONG` (span: `[14:16]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **23 %** → `NGUONG_DINH_LUONG` (span: `[18:20]`) *(lồng trong `e1` (`KHOAN`))*
- `[e4]` **37 %** → `NGUONG_DINH_LUONG` (span: `[22:24]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 3 . Bít tất - Chất liệu : sợi cotton tổng hợp : cotton 40 % ; acrylic 23 % ; spandex 37 % ; `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 6 `[DIEU]`)


---

### Mẫu #02_2015_TT-TTCP_58849#body_context_42 (Loại: `body_context`)
> **[Thanh tra Chính phủ]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[02/2015/TT-TTCP]`<SO_HIEU>`** . **[Điều 6]`<DIEU>`** . **[3 . Bít tất - Màu lông chuột , chất dệt kim len co giãn , cổ tất lửng .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[3:4]`)
- `[e1]` **02/2015/TT-TTCP** → `SO_HIEU` (span: `[5:6]`)
- `[e2]` **Thanh tra Chính phủ** → `CO_QUAN_BAN_HANH` (span: `[0:2]`)
- `[e3]` **Điều 6** → `DIEU` (span: `[7:9]`)
- `[e4]` **3 . Bít tất - Màu lông chuột , chất dệt kim len co giãn , cổ tất lửng .** → `KHOAN` (span: `[10:27]`)

**Quan hệ:**
- (`e1` 02/2015/TT-TTCP `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Thanh tra Chính phủ `[CO_QUAN_BAN_HANH]`)
- (`e1` 02/2015/TT-TTCP `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 6 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 02/2015/TT-TTCP `[SO_HIEU]`)
- (`e4` 3 . Bít tất - Màu lông chuột , chất dệt kim len co giãn , cổ tất lửng . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 6 `[DIEU]`)


---

### Mẫu #02_2015_TT-TTCP_58849#body_standalone_43 (Loại: `body_standalone`)
> **[Điều 6]`<DIEU>`** . **[3 . Bít tất - Màu lông chuột , chất dệt kim len co giãn , cổ tất lửng .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 6** → `DIEU` (span: `[0:2]`)
- `[e1]` **3 . Bít tất - Màu lông chuột , chất dệt kim len co giãn , cổ tất lửng .** → `KHOAN` (span: `[3:20]`)

**Quan hệ:**
- (`e1` 3 . Bít tất - Màu lông chuột , chất dệt kim len co giãn , cổ tất lửng . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 6 `[DIEU]`)


---

### Mẫu #02_2015_TT-TTCP_58849#body_context_44 (Loại: `body_context`)
> **[Thanh tra Chính phủ]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[02/2015/TT-TTCP]`<SO_HIEU>`** . **[Điều 6]`<DIEU>`** . **[Khoản 5]`<KHOAN>`** . **[a ) Chất liệu : - Kim cài bằng hợp kim không gỉ ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[3:4]`)
- `[e1]` **02/2015/TT-TTCP** → `SO_HIEU` (span: `[5:6]`)
- `[e2]` **Thanh tra Chính phủ** → `CO_QUAN_BAN_HANH` (span: `[0:2]`)
- `[e3]` **Điều 6** → `DIEU` (span: `[7:9]`)
- `[e4]` **Khoản 5** → `KHOAN` (span: `[10:12]`)
- `[e5]` **a ) Chất liệu : - Kim cài bằng hợp kim không gỉ ;** → `DIEM` (span: `[13:25]`)

**Quan hệ:**
- (`e1` 02/2015/TT-TTCP `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Thanh tra Chính phủ `[CO_QUAN_BAN_HANH]`)
- (`e1` 02/2015/TT-TTCP `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 6 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 02/2015/TT-TTCP `[SO_HIEU]`)
- (`e4` Khoản 5 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 6 `[DIEU]`)
- (`e5` a ) Chất liệu : - Kim cài bằng hợp kim không gỉ ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e4` Khoản 5 `[KHOAN]`)


---

### Mẫu #02_2015_TT-TTCP_58849#body_context_45 (Loại: `body_context`)
> **[Thanh tra Chính phủ]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[02/2015/TT-TTCP]`<SO_HIEU>`** . **[Điều 6]`<DIEU>`** . **[Khoản 7]`<KHOAN>`** . **[a ) Chất liệu : - Đồng vàng tấm dầy 0.3 mm ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[3:4]`)
- `[e1]` **02/2015/TT-TTCP** → `SO_HIEU` (span: `[5:6]`)
- `[e2]` **Thanh tra Chính phủ** → `CO_QUAN_BAN_HANH` (span: `[0:2]`)
- `[e3]` **Điều 6** → `DIEU` (span: `[7:9]`)
- `[e4]` **Khoản 7** → `KHOAN` (span: `[10:12]`)
- `[e5]` **a ) Chất liệu : - Đồng vàng tấm dầy 0.3 mm ;** → `DIEM` (span: `[13:25]`)

**Quan hệ:**
- (`e1` 02/2015/TT-TTCP `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Thanh tra Chính phủ `[CO_QUAN_BAN_HANH]`)
- (`e1` 02/2015/TT-TTCP `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 6 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 02/2015/TT-TTCP `[SO_HIEU]`)
- (`e4` Khoản 7 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 6 `[DIEU]`)
- (`e5` a ) Chất liệu : - Đồng vàng tấm dầy 0.3 mm ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e4` Khoản 7 `[KHOAN]`)


---

### Mẫu #02_2015_TT-TTCP_58849#body_context_46 (Loại: `body_context`)
> **[Thanh tra Chính phủ]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[02/2015/TT-TTCP]`<SO_HIEU>`** . **[Điều 6]`<DIEU>`** . **[Khoản 8]`<KHOAN>`** . **[b ) Màu sắc và quy trình mạ - Mạ màu trắng bóng ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[3:4]`)
- `[e1]` **02/2015/TT-TTCP** → `SO_HIEU` (span: `[5:6]`)
- `[e2]` **Thanh tra Chính phủ** → `CO_QUAN_BAN_HANH` (span: `[0:2]`)
- `[e3]` **Điều 6** → `DIEU` (span: `[7:9]`)
- `[e4]` **Khoản 8** → `KHOAN` (span: `[10:12]`)
- `[e5]` **b ) Màu sắc và quy trình mạ - Mạ màu trắng bóng ;** → `DIEM` (span: `[13:25]`)

**Quan hệ:**
- (`e1` 02/2015/TT-TTCP `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Thanh tra Chính phủ `[CO_QUAN_BAN_HANH]`)
- (`e1` 02/2015/TT-TTCP `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 6 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 02/2015/TT-TTCP `[SO_HIEU]`)
- (`e4` Khoản 8 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 6 `[DIEU]`)
- (`e5` b ) Màu sắc và quy trình mạ - Mạ màu trắng bóng ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e4` Khoản 8 `[KHOAN]`)


---

### Mẫu #02_2015_TT-TTCP_58849#body_context_47 (Loại: `body_context`)
> **[Thanh tra Chính phủ]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[02/2015/TT-TTCP]`<SO_HIEU>`** . **[Điều 6]`<DIEU>`** . **[Khoản 9]`<KHOAN>`** . **[b ) Màu sắc và quy trình mạ - Trọng lượng 1 cái : 6g ± 0.4 .]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[3:4]`)
- `[e1]` **02/2015/TT-TTCP** → `SO_HIEU` (span: `[5:6]`)
- `[e2]` **Thanh tra Chính phủ** → `CO_QUAN_BAN_HANH` (span: `[0:2]`)
- `[e3]` **Điều 6** → `DIEU` (span: `[7:9]`)
- `[e4]` **Khoản 9** → `KHOAN` (span: `[10:12]`)
- `[e5]` **b ) Màu sắc và quy trình mạ - Trọng lượng 1 cái : 6g ± 0.4 .** → `DIEM` (span: `[13:28]`)

**Quan hệ:**
- (`e1` 02/2015/TT-TTCP `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Thanh tra Chính phủ `[CO_QUAN_BAN_HANH]`)
- (`e1` 02/2015/TT-TTCP `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 6 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 02/2015/TT-TTCP `[SO_HIEU]`)
- (`e4` Khoản 9 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 6 `[DIEU]`)
- (`e5` b ) Màu sắc và quy trình mạ - Trọng lượng 1 cái : 6g ± 0.4 . `[DIEM]`) ==[ **THUOC_VE** ]==> (`e4` Khoản 9 `[KHOAN]`)


---

### Mẫu #02_2015_TT-TTCP_58849#body_context_48 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[02/2015/TT-TTCP]`<SO_HIEU>`** ban hành **[ngày 16 tháng 03 năm 2015]`<NGAY_BAN_HANH>`** bởi **[Thanh tra Chính phủ]`<CO_QUAN_BAN_HANH>`** . **[Điều 6]`<DIEU>`** . **[11 . Mũ kêpi]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **02/2015/TT-TTCP** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Thanh tra Chính phủ** → `CO_QUAN_BAN_HANH` (span: `[11:13]`)
- `[e3]` **ngày 16 tháng 03 năm 2015** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 6** → `DIEU` (span: `[14:16]`)
- `[e5]` **11 . Mũ kêpi** → `KHOAN` (span: `[17:20]`)

**Quan hệ:**
- (`e1` 02/2015/TT-TTCP `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Thanh tra Chính phủ `[CO_QUAN_BAN_HANH]`)
- (`e1` 02/2015/TT-TTCP `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 02/2015/TT-TTCP `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 16 tháng 03 năm 2015 `[NGAY_BAN_HANH]`)
- (`e4` Điều 6 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 02/2015/TT-TTCP `[SO_HIEU]`)
- (`e5` 11 . Mũ kêpi `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 6 `[DIEU]`)


---

### Mẫu #02_2015_TT-TTCP_58849#body_context_49 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[02/2015/TT-TTCP]`<SO_HIEU>`** của **[Thanh tra Chính phủ]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Thanh tra]`<LINH_VUC>`** . **[Điều 6]`<DIEU>`** . **[12 . **[Mũ bảo hiểm]`<TAI_SAN_VAT_CHAT>`**]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **02/2015/TT-TTCP** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Thanh tra Chính phủ** → `CO_QUAN_BAN_HANH` (span: `[4:6]`)
- `[e3]` **Thanh tra** → `LINH_VUC` (span: `[8:9]`)
- `[e4]` **Điều 6** → `DIEU` (span: `[10:12]`)
- `[e5]` **12 . Mũ bảo hiểm** → `KHOAN` (span: `[13:16]`)
- `[e6]` **Mũ bảo hiểm** → `TAI_SAN_VAT_CHAT` (span: `[15:16]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 02/2015/TT-TTCP `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Thanh tra Chính phủ `[CO_QUAN_BAN_HANH]`)
- (`e1` 02/2015/TT-TTCP `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 02/2015/TT-TTCP `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Thanh tra `[LINH_VUC]`)
- (`e4` Điều 6 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 02/2015/TT-TTCP `[SO_HIEU]`)
- (`e5` 12 . Mũ bảo hiểm `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 6 `[DIEU]`)
- (`e1` 02/2015/TT-TTCP `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Thanh tra `[LINH_VUC]`)
- (`e5` 12 . Mũ bảo hiểm `[KHOAN]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Thanh tra `[LINH_VUC]`)


---

### Mẫu #02_2015_TT-TTCP_58849#body_context_50 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[02/2015/TT-TTCP]`<SO_HIEU>`** của **[Thanh tra Chính phủ]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Thanh tra]`<LINH_VUC>`** . **[Điều 6]`<DIEU>`** . **[Khoản 12]`<KHOAN>`** . **[a ) Chất liệu : vỏ mũ bằng nhựa poliamit 6 ( PA6 ) . Kính mũ bằng nhựa polycacbonat ( PC ) , đệm bảo vệ : xốp Polyxtyren ( EPS ) ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **02/2015/TT-TTCP** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Thanh tra Chính phủ** → `CO_QUAN_BAN_HANH` (span: `[4:6]`)
- `[e3]` **Thanh tra** → `LINH_VUC` (span: `[8:9]`)
- `[e4]` **Điều 6** → `DIEU` (span: `[10:12]`)
- `[e5]` **Khoản 12** → `KHOAN` (span: `[13:15]`)
- `[e6]` **a ) Chất liệu : vỏ mũ bằng nhựa poliamit 6 ( PA6 ) . Kính mũ bằng nhựa polycacbonat ( PC ) , đệm bảo vệ : xốp Polyxtyren ( EPS ) ;** → `DIEM` (span: `[16:48]`)

**Quan hệ:**
- (`e1` 02/2015/TT-TTCP `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Thanh tra Chính phủ `[CO_QUAN_BAN_HANH]`)
- (`e1` 02/2015/TT-TTCP `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 02/2015/TT-TTCP `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Thanh tra `[LINH_VUC]`)
- (`e4` Điều 6 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 02/2015/TT-TTCP `[SO_HIEU]`)
- (`e5` Khoản 12 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 6 `[DIEU]`)
- (`e6` a ) Chất liệu : vỏ mũ bằng nhựa poliamit 6 ( PA6 ) . Kính mũ bằng nhựa polycacbonat ( PC ) , đệm bảo vệ : xốp Polyxtyren ( EPS ) ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e5` Khoản 12 `[KHOAN]`)
- (`e1` 02/2015/TT-TTCP `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Thanh tra `[LINH_VUC]`)
- (`e6` a ) Chất liệu : vỏ mũ bằng nhựa poliamit 6 ( PA6 ) . Kính mũ bằng nhựa polycacbonat ( PC ) , đệm bảo vệ : xốp Polyxtyren ( EPS ) ; `[DIEM]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Thanh tra `[LINH_VUC]`)


---

### Mẫu #02_2015_TT-TTCP_58849#body_standalone_51 (Loại: `body_standalone`)
> **[Điều 6]`<DIEU>`** . **[Khoản 12]`<KHOAN>`** . **[a ) Chất liệu : vỏ mũ bằng nhựa poliamit 6 ( PA6 ) . Kính mũ bằng nhựa polycacbonat ( PC ) , đệm bảo vệ : xốp Polyxtyren ( EPS ) ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Điều 6** → `DIEU` (span: `[0:2]`)
- `[e1]` **Khoản 12** → `KHOAN` (span: `[3:5]`)
- `[e2]` **a ) Chất liệu : vỏ mũ bằng nhựa poliamit 6 ( PA6 ) . Kính mũ bằng nhựa polycacbonat ( PC ) , đệm bảo vệ : xốp Polyxtyren ( EPS ) ;** → `DIEM` (span: `[6:38]`)

**Quan hệ:**
- (`e1` Khoản 12 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 6 `[DIEU]`)
- (`e2` a ) Chất liệu : vỏ mũ bằng nhựa poliamit 6 ( PA6 ) . Kính mũ bằng nhựa polycacbonat ( PC ) , đệm bảo vệ : xốp Polyxtyren ( EPS ) ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e1` Khoản 12 `[KHOAN]`)


---

### Mẫu #02_2015_TT-TTCP_58849#body_context_52 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[02/2015/TT-TTCP]`<SO_HIEU>`** của **[Thanh tra Chính phủ]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Thanh tra]`<LINH_VUC>`** . **[Điều 6]`<DIEU>`** . **[Khoản 13]`<KHOAN>`** . **[a ) Cầu vai , cấp hàm đối với **[cán bộ]`<CHU_THE_CA_NHAN>`** , thanh tra viên giữ chức vụ lãnh đạo quản lý - Tổng **[Thanh tra Chính phủ]`<CO_QUAN_THAM_QUYEN>`** : cầu vai có chiều dài 13cm , phần đầu nhọn rộng 4cm , phần đuôi rộng 5cm , nền cấp hiệu bằng vải nỉ màu đỏ , cốt cấp hiệu bằng nhựa nguyên chất màu trắng ; sao và viền cấp hiệu bằng đồng tấm , viền kim loại mạ màu trắng bóng ; cúc cấp hiệu hình tròn có ngôi sao ở giữa 2 cành tùng , gắn 4 sao 23mm]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **02/2015/TT-TTCP** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Thanh tra Chính phủ** → `CO_QUAN_BAN_HANH` (span: `[4:6]`)
- `[e3]` **Thanh tra** → `LINH_VUC` (span: `[8:9]`)
- `[e4]` **Điều 6** → `DIEU` (span: `[10:12]`)
- `[e5]` **Khoản 13** → `KHOAN` (span: `[13:15]`)
- `[e6]` **a ) Cầu vai , cấp hàm đối với cán bộ , thanh tra viên giữ chức vụ lãnh đạo quản lý - Tổng Thanh tra Chính phủ : cầu vai có chiều dài 13cm , phần đầu nhọn rộng 4cm , phần đuôi rộng 5cm , nền cấp hiệu bằng vải nỉ màu đỏ , cốt cấp hiệu bằng nhựa nguyên chất màu trắng ; sao và viền cấp hiệu bằng đồng tấm , viền kim loại mạ màu trắng bóng ; cúc cấp hiệu hình tròn có ngôi sao ở giữa 2 cành tùng , gắn 4 sao 23mm** → `DIEM` (span: `[16:99]`)
- `[e7]` **Thanh tra Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[33:35]`) *(lồng trong `e6` (`DIEM`))*
- `[e8]` **cán bộ** → `CHU_THE_CA_NHAN` (span: `[23:24]`) *(lồng trong `e6` (`DIEM`))*

**Quan hệ:**
- (`e1` 02/2015/TT-TTCP `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Thanh tra Chính phủ `[CO_QUAN_BAN_HANH]`)
- (`e1` 02/2015/TT-TTCP `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 02/2015/TT-TTCP `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Thanh tra `[LINH_VUC]`)
- (`e4` Điều 6 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 02/2015/TT-TTCP `[SO_HIEU]`)
- (`e5` Khoản 13 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 6 `[DIEU]`)
- (`e6` a ) Cầu vai , cấp hàm đối với cán bộ , thanh tra viên giữ chức vụ lãnh đạo quản lý - Tổng Thanh tra Chính phủ : cầu vai có chiều dài 13cm , phần đầu nhọn rộng 4cm , phần đuôi rộng 5cm , nền cấp hiệu bằng vải nỉ màu đỏ , cốt cấp hiệu bằng nhựa nguyên chất màu trắng ; sao và viền cấp hiệu bằng đồng tấm , viền kim loại mạ màu trắng bóng ; cúc cấp hiệu hình tròn có ngôi sao ở giữa 2 cành tùng , gắn 4 sao 23mm `[DIEM]`) ==[ **THUOC_VE** ]==> (`e5` Khoản 13 `[KHOAN]`)
- (`e1` 02/2015/TT-TTCP `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Thanh tra `[LINH_VUC]`)
- (`e6` a ) Cầu vai , cấp hàm đối với cán bộ , thanh tra viên giữ chức vụ lãnh đạo quản lý - Tổng Thanh tra Chính phủ : cầu vai có chiều dài 13cm , phần đầu nhọn rộng 4cm , phần đuôi rộng 5cm , nền cấp hiệu bằng vải nỉ màu đỏ , cốt cấp hiệu bằng nhựa nguyên chất màu trắng ; sao và viền cấp hiệu bằng đồng tấm , viền kim loại mạ màu trắng bóng ; cúc cấp hiệu hình tròn có ngôi sao ở giữa 2 cành tùng , gắn 4 sao 23mm `[DIEM]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Thanh tra `[LINH_VUC]`)


---

### Mẫu #02_2015_TT-TTCP_58849#body_standalone_53 (Loại: `body_standalone`)
> **[Điều 6]`<DIEU>`** . **[Khoản 13]`<KHOAN>`** . **[a ) Cầu vai , cấp hàm đối với **[cán bộ]`<CHU_THE_CA_NHAN>`** , thanh tra viên giữ chức vụ lãnh đạo quản lý - Tổng **[Thanh tra Chính phủ]`<CO_QUAN_THAM_QUYEN>`** : cầu vai có chiều dài 13cm , phần đầu nhọn rộng 4cm , phần đuôi rộng 5cm , nền cấp hiệu bằng vải nỉ màu đỏ , cốt cấp hiệu bằng nhựa nguyên chất màu trắng ; sao và viền cấp hiệu bằng đồng tấm , viền kim loại mạ màu trắng bóng ; cúc cấp hiệu hình tròn có ngôi sao ở giữa 2 cành tùng , gắn 4 sao 23mm]`<DIEM>`**

**Thực thể:**
- `[e0]` **Điều 6** → `DIEU` (span: `[0:2]`)
- `[e1]` **Khoản 13** → `KHOAN` (span: `[3:5]`)
- `[e2]` **a ) Cầu vai , cấp hàm đối với cán bộ , thanh tra viên giữ chức vụ lãnh đạo quản lý - Tổng Thanh tra Chính phủ : cầu vai có chiều dài 13cm , phần đầu nhọn rộng 4cm , phần đuôi rộng 5cm , nền cấp hiệu bằng vải nỉ màu đỏ , cốt cấp hiệu bằng nhựa nguyên chất màu trắng ; sao và viền cấp hiệu bằng đồng tấm , viền kim loại mạ màu trắng bóng ; cúc cấp hiệu hình tròn có ngôi sao ở giữa 2 cành tùng , gắn 4 sao 23mm** → `DIEM` (span: `[6:89]`)
- `[e3]` **Thanh tra Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[23:25]`) *(lồng trong `e2` (`DIEM`))*
- `[e4]` **cán bộ** → `CHU_THE_CA_NHAN` (span: `[13:14]`) *(lồng trong `e2` (`DIEM`))*

**Quan hệ:**
- (`e1` Khoản 13 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 6 `[DIEU]`)
- (`e2` a ) Cầu vai , cấp hàm đối với cán bộ , thanh tra viên giữ chức vụ lãnh đạo quản lý - Tổng Thanh tra Chính phủ : cầu vai có chiều dài 13cm , phần đầu nhọn rộng 4cm , phần đuôi rộng 5cm , nền cấp hiệu bằng vải nỉ màu đỏ , cốt cấp hiệu bằng nhựa nguyên chất màu trắng ; sao và viền cấp hiệu bằng đồng tấm , viền kim loại mạ màu trắng bóng ; cúc cấp hiệu hình tròn có ngôi sao ở giữa 2 cành tùng , gắn 4 sao 23mm `[DIEM]`) ==[ **THUOC_VE** ]==> (`e1` Khoản 13 `[KHOAN]`)


---

### Mẫu #02_2015_TT-TTCP_58849#body_context_54 (Loại: `body_context`)
> **[Thanh tra Chính phủ]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[02/2015/TT-TTCP]`<SO_HIEU>`** . **[Điều 6]`<DIEU>`** . **[Khoản 13]`<KHOAN>`** . **[a ) Cầu vai , cấp hàm đối với **[cán bộ]`<CHU_THE_CA_NHAN>`** , thanh tra viên giữ chức vụ lãnh đạo quản lý - Phó Tổng **[Thanh tra Chính phủ]`<CO_QUAN_THAM_QUYEN>`** : cầu vai có chiều dài 13cm , phần đầu nhọn rộng 4cm , phần đuôi rộng 5cm , nền cấp hiệu bằng vải nỉ màu đỏ , cốt cấp hiệu bằng nhựa nguyên chất màu trắng ; sao và viền cấp hiệu bằng đồng tấm , viền kim loại mạ màu trắng bóng ; cúc cấp hiệu hình tròn có ngôi sao ở giữa 2 cành tùng ; nhiệm kỳ 1]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[3:4]`)
- `[e1]` **02/2015/TT-TTCP** → `SO_HIEU` (span: `[5:6]`)
- `[e2]` **Thanh tra Chính phủ** → `CO_QUAN_BAN_HANH` (span: `[0:2]`)
- `[e3]` **Điều 6** → `DIEU` (span: `[7:9]`)
- `[e4]` **Khoản 13** → `KHOAN` (span: `[10:12]`)
- `[e5]` **a ) Cầu vai , cấp hàm đối với cán bộ , thanh tra viên giữ chức vụ lãnh đạo quản lý - Phó Tổng Thanh tra Chính phủ : cầu vai có chiều dài 13cm , phần đầu nhọn rộng 4cm , phần đuôi rộng 5cm , nền cấp hiệu bằng vải nỉ màu đỏ , cốt cấp hiệu bằng nhựa nguyên chất màu trắng ; sao và viền cấp hiệu bằng đồng tấm , viền kim loại mạ màu trắng bóng ; cúc cấp hiệu hình tròn có ngôi sao ở giữa 2 cành tùng ; nhiệm kỳ 1** → `DIEM` (span: `[13:94]`)
- `[e6]` **Thanh tra Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[30:32]`) *(lồng trong `e5` (`DIEM`))*
- `[e7]` **cán bộ** → `CHU_THE_CA_NHAN` (span: `[20:21]`) *(lồng trong `e5` (`DIEM`))*

**Quan hệ:**
- (`e1` 02/2015/TT-TTCP `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Thanh tra Chính phủ `[CO_QUAN_BAN_HANH]`)
- (`e1` 02/2015/TT-TTCP `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 6 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 02/2015/TT-TTCP `[SO_HIEU]`)
- (`e4` Khoản 13 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 6 `[DIEU]`)
- (`e5` a ) Cầu vai , cấp hàm đối với cán bộ , thanh tra viên giữ chức vụ lãnh đạo quản lý - Phó Tổng Thanh tra Chính phủ : cầu vai có chiều dài 13cm , phần đầu nhọn rộng 4cm , phần đuôi rộng 5cm , nền cấp hiệu bằng vải nỉ màu đỏ , cốt cấp hiệu bằng nhựa nguyên chất màu trắng ; sao và viền cấp hiệu bằng đồng tấm , viền kim loại mạ màu trắng bóng ; cúc cấp hiệu hình tròn có ngôi sao ở giữa 2 cành tùng ; nhiệm kỳ 1 `[DIEM]`) ==[ **THUOC_VE** ]==> (`e4` Khoản 13 `[KHOAN]`)


---

### Mẫu #02_2015_TT-TTCP_58849#body_standalone_55 (Loại: `body_standalone`)
> **[Điều 6]`<DIEU>`** . **[Khoản 13]`<KHOAN>`** . **[a ) Cầu vai , cấp hàm đối với **[cán bộ]`<CHU_THE_CA_NHAN>`** , thanh tra viên giữ chức vụ lãnh đạo quản lý - Phó Tổng **[Thanh tra Chính phủ]`<CO_QUAN_THAM_QUYEN>`** : cầu vai có chiều dài 13cm , phần đầu nhọn rộng 4cm , phần đuôi rộng 5cm , nền cấp hiệu bằng vải nỉ màu đỏ , cốt cấp hiệu bằng nhựa nguyên chất màu trắng ; sao và viền cấp hiệu bằng đồng tấm , viền kim loại mạ màu trắng bóng ; cúc cấp hiệu hình tròn có ngôi sao ở giữa 2 cành tùng ; nhiệm kỳ 1]`<DIEM>`**

**Thực thể:**
- `[e0]` **Điều 6** → `DIEU` (span: `[0:2]`)
- `[e1]` **Khoản 13** → `KHOAN` (span: `[3:5]`)
- `[e2]` **a ) Cầu vai , cấp hàm đối với cán bộ , thanh tra viên giữ chức vụ lãnh đạo quản lý - Phó Tổng Thanh tra Chính phủ : cầu vai có chiều dài 13cm , phần đầu nhọn rộng 4cm , phần đuôi rộng 5cm , nền cấp hiệu bằng vải nỉ màu đỏ , cốt cấp hiệu bằng nhựa nguyên chất màu trắng ; sao và viền cấp hiệu bằng đồng tấm , viền kim loại mạ màu trắng bóng ; cúc cấp hiệu hình tròn có ngôi sao ở giữa 2 cành tùng ; nhiệm kỳ 1** → `DIEM` (span: `[6:87]`)
- `[e3]` **Thanh tra Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[23:25]`) *(lồng trong `e2` (`DIEM`))*
- `[e4]` **cán bộ** → `CHU_THE_CA_NHAN` (span: `[13:14]`) *(lồng trong `e2` (`DIEM`))*

**Quan hệ:**
- (`e1` Khoản 13 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 6 `[DIEU]`)
- (`e2` a ) Cầu vai , cấp hàm đối với cán bộ , thanh tra viên giữ chức vụ lãnh đạo quản lý - Phó Tổng Thanh tra Chính phủ : cầu vai có chiều dài 13cm , phần đầu nhọn rộng 4cm , phần đuôi rộng 5cm , nền cấp hiệu bằng vải nỉ màu đỏ , cốt cấp hiệu bằng nhựa nguyên chất màu trắng ; sao và viền cấp hiệu bằng đồng tấm , viền kim loại mạ màu trắng bóng ; cúc cấp hiệu hình tròn có ngôi sao ở giữa 2 cành tùng ; nhiệm kỳ 1 `[DIEM]`) ==[ **THUOC_VE** ]==> (`e1` Khoản 13 `[KHOAN]`)


---

### Mẫu #02_2015_TT-TTCP_58849#body_context_56 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[02/2015/TT-TTCP]`<SO_HIEU>`** của **[Thanh tra Chính phủ]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Thanh tra]`<LINH_VUC>`** . **[Điều 6]`<DIEU>`** . **[Khoản 13]`<KHOAN>`** . **[a ) Cầu vai , cấp hàm đối với **[cán bộ]`<CHU_THE_CA_NHAN>`** , thanh tra viên giữ chức vụ lãnh đạo quản lý - Vụ trưởng và tương đương thuộc **[Thanh tra Chính phủ]`<CO_QUAN_THAM_QUYEN>`** ; **[Chánh thanh tra Bộ]`<CO_QUAN_THAM_QUYEN>`** , ngành : cầu vai có chiều dài 13cm , phần đầu nhọn rộng 4cm , phần đuôi rộng 5cm , nền cấp hiệu bằng vải nỉ màu đỏ , cốt cấp hiệu bằng nhựa nguyên chất màu trắng ; sao và viền cấp hiệu bằng đồng tấm , viền kim loại mạ màu trắng bóng ; cúc cấp hiệu hình tròn có ngôi]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **02/2015/TT-TTCP** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Thanh tra Chính phủ** → `CO_QUAN_BAN_HANH` (span: `[4:6]`)
- `[e3]` **Thanh tra** → `LINH_VUC` (span: `[8:9]`)
- `[e4]` **Điều 6** → `DIEU` (span: `[10:12]`)
- `[e5]` **Khoản 13** → `KHOAN` (span: `[13:15]`)
- `[e6]` **a ) Cầu vai , cấp hàm đối với cán bộ , thanh tra viên giữ chức vụ lãnh đạo quản lý - Vụ trưởng và tương đương thuộc Thanh tra Chính phủ ; Chánh thanh tra Bộ , ngành : cầu vai có chiều dài 13cm , phần đầu nhọn rộng 4cm , phần đuôi rộng 5cm , nền cấp hiệu bằng vải nỉ màu đỏ , cốt cấp hiệu bằng nhựa nguyên chất màu trắng ; sao và viền cấp hiệu bằng đồng tấm , viền kim loại mạ màu trắng bóng ; cúc cấp hiệu hình tròn có ngôi** → `DIEM` (span: `[16:98]`)
- `[e7]` **Thanh tra Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[36:38]`) *(lồng trong `e6` (`DIEM`))*
- `[e8]` **Chánh thanh tra Bộ** → `CO_QUAN_THAM_QUYEN` (span: `[39:42]`) *(lồng trong `e6` (`DIEM`))*
- `[e9]` **cán bộ** → `CHU_THE_CA_NHAN` (span: `[23:24]`) *(lồng trong `e6` (`DIEM`))*

**Quan hệ:**
- (`e1` 02/2015/TT-TTCP `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Thanh tra Chính phủ `[CO_QUAN_BAN_HANH]`)
- (`e1` 02/2015/TT-TTCP `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 02/2015/TT-TTCP `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Thanh tra `[LINH_VUC]`)
- (`e4` Điều 6 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 02/2015/TT-TTCP `[SO_HIEU]`)
- (`e5` Khoản 13 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 6 `[DIEU]`)
- (`e6` a ) Cầu vai , cấp hàm đối với cán bộ , thanh tra viên giữ chức vụ lãnh đạo quản lý - Vụ trưởng và tương đương thuộc Thanh tra Chính phủ ; Chánh thanh tra Bộ , ngành : cầu vai có chiều dài 13cm , phần đầu nhọn rộng 4cm , phần đuôi rộng 5cm , nền cấp hiệu bằng vải nỉ màu đỏ , cốt cấp hiệu bằng nhựa nguyên chất màu trắng ; sao và viền cấp hiệu bằng đồng tấm , viền kim loại mạ màu trắng bóng ; cúc cấp hiệu hình tròn có ngôi `[DIEM]`) ==[ **THUOC_VE** ]==> (`e5` Khoản 13 `[KHOAN]`)
- (`e1` 02/2015/TT-TTCP `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Thanh tra `[LINH_VUC]`)
- (`e6` a ) Cầu vai , cấp hàm đối với cán bộ , thanh tra viên giữ chức vụ lãnh đạo quản lý - Vụ trưởng và tương đương thuộc Thanh tra Chính phủ ; Chánh thanh tra Bộ , ngành : cầu vai có chiều dài 13cm , phần đầu nhọn rộng 4cm , phần đuôi rộng 5cm , nền cấp hiệu bằng vải nỉ màu đỏ , cốt cấp hiệu bằng nhựa nguyên chất màu trắng ; sao và viền cấp hiệu bằng đồng tấm , viền kim loại mạ màu trắng bóng ; cúc cấp hiệu hình tròn có ngôi `[DIEM]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Thanh tra `[LINH_VUC]`)


---

### Mẫu #02_2015_TT-TTCP_58849#body_standalone_57 (Loại: `body_standalone`)
> **[Điều 6]`<DIEU>`** . **[Khoản 13]`<KHOAN>`** . **[a ) Cầu vai , cấp hàm đối với **[cán bộ]`<CHU_THE_CA_NHAN>`** , thanh tra viên giữ chức vụ lãnh đạo quản lý - Vụ trưởng và tương đương thuộc **[Thanh tra Chính phủ]`<CO_QUAN_THAM_QUYEN>`** ; **[Chánh thanh tra Bộ]`<CO_QUAN_THAM_QUYEN>`** , ngành : cầu vai có chiều dài 13cm , phần đầu nhọn rộng 4cm , phần đuôi rộng 5cm , nền cấp hiệu bằng vải nỉ màu đỏ , cốt cấp hiệu bằng nhựa nguyên chất màu trắng ; sao và viền cấp hiệu bằng đồng tấm , viền kim loại mạ màu trắng bóng ; cúc cấp hiệu hình tròn có ngôi]`<DIEM>`**

**Thực thể:**
- `[e0]` **Điều 6** → `DIEU` (span: `[0:2]`)
- `[e1]` **Khoản 13** → `KHOAN` (span: `[3:5]`)
- `[e2]` **a ) Cầu vai , cấp hàm đối với cán bộ , thanh tra viên giữ chức vụ lãnh đạo quản lý - Vụ trưởng và tương đương thuộc Thanh tra Chính phủ ; Chánh thanh tra Bộ , ngành : cầu vai có chiều dài 13cm , phần đầu nhọn rộng 4cm , phần đuôi rộng 5cm , nền cấp hiệu bằng vải nỉ màu đỏ , cốt cấp hiệu bằng nhựa nguyên chất màu trắng ; sao và viền cấp hiệu bằng đồng tấm , viền kim loại mạ màu trắng bóng ; cúc cấp hiệu hình tròn có ngôi** → `DIEM` (span: `[6:88]`)
- `[e3]` **Thanh tra Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[26:28]`) *(lồng trong `e2` (`DIEM`))*
- `[e4]` **Chánh thanh tra Bộ** → `CO_QUAN_THAM_QUYEN` (span: `[29:32]`) *(lồng trong `e2` (`DIEM`))*
- `[e5]` **cán bộ** → `CHU_THE_CA_NHAN` (span: `[13:14]`) *(lồng trong `e2` (`DIEM`))*

**Quan hệ:**
- (`e1` Khoản 13 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 6 `[DIEU]`)
- (`e2` a ) Cầu vai , cấp hàm đối với cán bộ , thanh tra viên giữ chức vụ lãnh đạo quản lý - Vụ trưởng và tương đương thuộc Thanh tra Chính phủ ; Chánh thanh tra Bộ , ngành : cầu vai có chiều dài 13cm , phần đầu nhọn rộng 4cm , phần đuôi rộng 5cm , nền cấp hiệu bằng vải nỉ màu đỏ , cốt cấp hiệu bằng nhựa nguyên chất màu trắng ; sao và viền cấp hiệu bằng đồng tấm , viền kim loại mạ màu trắng bóng ; cúc cấp hiệu hình tròn có ngôi `[DIEM]`) ==[ **THUOC_VE** ]==> (`e1` Khoản 13 `[KHOAN]`)


---

### Mẫu #02_2015_TT-TTCP_58849#body_context_58 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[02/2015/TT-TTCP]`<SO_HIEU>`** ban hành **[ngày 16 tháng 03 năm 2015]`<NGAY_BAN_HANH>`** bởi **[Thanh tra Chính phủ]`<CO_QUAN_BAN_HANH>`** . **[Điều 6]`<DIEU>`** . **[Khoản 13]`<KHOAN>`** . **[a ) Cầu vai , cấp hàm đối với **[cán bộ]`<CHU_THE_CA_NHAN>`** , thanh tra viên giữ chức vụ lãnh đạo quản lý - Phó Vụ trưởng và tương đương thuộc **[Thanh tra Chính phủ]`<CO_QUAN_THAM_QUYEN>`** ; Phó **[Chánh thanh tra Bộ]`<CO_QUAN_THAM_QUYEN>`** , ngành : cầu vai có chiều dài 13cm , phần đầu nhọn rộng 4cm , phần đuôi rộng 5cm , nền cấp hiệu bằng vải nỉ màu đỏ , cốt cấp hiệu bằng nhựa nguyên chất màu trắng ; sao cấp hiệu bằng đồng tấm mạ màu trắng bóng ; có lé bằng vải màu xanh rộng 3mm ; cúc cấp]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **02/2015/TT-TTCP** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Thanh tra Chính phủ** → `CO_QUAN_BAN_HANH` (span: `[11:13]`)
- `[e3]` **ngày 16 tháng 03 năm 2015** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 6** → `DIEU` (span: `[14:16]`)
- `[e5]` **Khoản 13** → `KHOAN` (span: `[17:19]`)
- `[e6]` **a ) Cầu vai , cấp hàm đối với cán bộ , thanh tra viên giữ chức vụ lãnh đạo quản lý - Phó Vụ trưởng và tương đương thuộc Thanh tra Chính phủ ; Phó Chánh thanh tra Bộ , ngành : cầu vai có chiều dài 13cm , phần đầu nhọn rộng 4cm , phần đuôi rộng 5cm , nền cấp hiệu bằng vải nỉ màu đỏ , cốt cấp hiệu bằng nhựa nguyên chất màu trắng ; sao cấp hiệu bằng đồng tấm mạ màu trắng bóng ; có lé bằng vải màu xanh rộng 3mm ; cúc cấp** → `DIEM` (span: `[20:104]`)
- `[e7]` **Thanh tra Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[40:42]`) *(lồng trong `e6` (`DIEM`))*
- `[e8]` **Chánh thanh tra Bộ** → `CO_QUAN_THAM_QUYEN` (span: `[44:47]`) *(lồng trong `e6` (`DIEM`))*
- `[e9]` **cán bộ** → `CHU_THE_CA_NHAN` (span: `[27:28]`) *(lồng trong `e6` (`DIEM`))*

**Quan hệ:**
- (`e1` 02/2015/TT-TTCP `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Thanh tra Chính phủ `[CO_QUAN_BAN_HANH]`)
- (`e1` 02/2015/TT-TTCP `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 02/2015/TT-TTCP `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 16 tháng 03 năm 2015 `[NGAY_BAN_HANH]`)
- (`e4` Điều 6 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 02/2015/TT-TTCP `[SO_HIEU]`)
- (`e5` Khoản 13 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 6 `[DIEU]`)
- (`e6` a ) Cầu vai , cấp hàm đối với cán bộ , thanh tra viên giữ chức vụ lãnh đạo quản lý - Phó Vụ trưởng và tương đương thuộc Thanh tra Chính phủ ; Phó Chánh thanh tra Bộ , ngành : cầu vai có chiều dài 13cm , phần đầu nhọn rộng 4cm , phần đuôi rộng 5cm , nền cấp hiệu bằng vải nỉ màu đỏ , cốt cấp hiệu bằng nhựa nguyên chất màu trắng ; sao cấp hiệu bằng đồng tấm mạ màu trắng bóng ; có lé bằng vải màu xanh rộng 3mm ; cúc cấp `[DIEM]`) ==[ **THUOC_VE** ]==> (`e5` Khoản 13 `[KHOAN]`)


---

### Mẫu #02_2015_TT-TTCP_58849#body_standalone_59 (Loại: `body_standalone`)
> **[Điều 6]`<DIEU>`** . **[Khoản 13]`<KHOAN>`** . **[a ) Cầu vai , cấp hàm đối với **[cán bộ]`<CHU_THE_CA_NHAN>`** , thanh tra viên giữ chức vụ lãnh đạo quản lý - Phó Vụ trưởng và tương đương thuộc **[Thanh tra Chính phủ]`<CO_QUAN_THAM_QUYEN>`** ; Phó **[Chánh thanh tra Bộ]`<CO_QUAN_THAM_QUYEN>`** , ngành : cầu vai có chiều dài 13cm , phần đầu nhọn rộng 4cm , phần đuôi rộng 5cm , nền cấp hiệu bằng vải nỉ màu đỏ , cốt cấp hiệu bằng nhựa nguyên chất màu trắng ; sao cấp hiệu bằng đồng tấm mạ màu trắng bóng ; có lé bằng vải màu xanh rộng 3mm ; cúc cấp]`<DIEM>`**

**Thực thể:**
- `[e0]` **Điều 6** → `DIEU` (span: `[0:2]`)
- `[e1]` **Khoản 13** → `KHOAN` (span: `[3:5]`)
- `[e2]` **a ) Cầu vai , cấp hàm đối với cán bộ , thanh tra viên giữ chức vụ lãnh đạo quản lý - Phó Vụ trưởng và tương đương thuộc Thanh tra Chính phủ ; Phó Chánh thanh tra Bộ , ngành : cầu vai có chiều dài 13cm , phần đầu nhọn rộng 4cm , phần đuôi rộng 5cm , nền cấp hiệu bằng vải nỉ màu đỏ , cốt cấp hiệu bằng nhựa nguyên chất màu trắng ; sao cấp hiệu bằng đồng tấm mạ màu trắng bóng ; có lé bằng vải màu xanh rộng 3mm ; cúc cấp** → `DIEM` (span: `[6:90]`)
- `[e3]` **Thanh tra Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[26:28]`) *(lồng trong `e2` (`DIEM`))*
- `[e4]` **Chánh thanh tra Bộ** → `CO_QUAN_THAM_QUYEN` (span: `[30:33]`) *(lồng trong `e2` (`DIEM`))*
- `[e5]` **cán bộ** → `CHU_THE_CA_NHAN` (span: `[13:14]`) *(lồng trong `e2` (`DIEM`))*

**Quan hệ:**
- (`e1` Khoản 13 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 6 `[DIEU]`)
- (`e2` a ) Cầu vai , cấp hàm đối với cán bộ , thanh tra viên giữ chức vụ lãnh đạo quản lý - Phó Vụ trưởng và tương đương thuộc Thanh tra Chính phủ ; Phó Chánh thanh tra Bộ , ngành : cầu vai có chiều dài 13cm , phần đầu nhọn rộng 4cm , phần đuôi rộng 5cm , nền cấp hiệu bằng vải nỉ màu đỏ , cốt cấp hiệu bằng nhựa nguyên chất màu trắng ; sao cấp hiệu bằng đồng tấm mạ màu trắng bóng ; có lé bằng vải màu xanh rộng 3mm ; cúc cấp `[DIEM]`) ==[ **THUOC_VE** ]==> (`e1` Khoản 13 `[KHOAN]`)


---

### Mẫu #02_2015_TT-TTCP_58849#body_context_60 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[02/2015/TT-TTCP]`<SO_HIEU>`** của **[Thanh tra Chính phủ]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Thanh tra]`<LINH_VUC>`** . **[Điều 6]`<DIEU>`** . **[Khoản 13]`<KHOAN>`** . **[a ) Cầu vai , cấp hàm đối với **[cán bộ]`<CHU_THE_CA_NHAN>`** , thanh tra viên giữ chức vụ lãnh đạo quản lý - Trưởng phòng và tương đương thuộc **[Thanh tra Chính phủ]`<CO_QUAN_THAM_QUYEN>`** ; Trưởng phòng và tương đương thuộc **[Thanh tra Bộ]`<CO_QUAN_THAM_QUYEN>`** , ngành : cầu vai có chiều dài 13cm , phần đầu nhọn rộng 4cm , phần đuôi rộng 5cm , nền cấp hiệu bằng vải nỉ màu đỏ , cốt cấp hiệu bằng nhựa nguyên chất màu trắng ; sao cấp hiệu bằng đồng tấm mạ màu trắng bóng ; có lé bằng vải màu xanh rộng]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **02/2015/TT-TTCP** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Thanh tra Chính phủ** → `CO_QUAN_BAN_HANH` (span: `[4:6]`)
- `[e3]` **Thanh tra** → `LINH_VUC` (span: `[8:9]`)
- `[e4]` **Điều 6** → `DIEU` (span: `[10:12]`)
- `[e5]` **Khoản 13** → `KHOAN` (span: `[13:15]`)
- `[e6]` **a ) Cầu vai , cấp hàm đối với cán bộ , thanh tra viên giữ chức vụ lãnh đạo quản lý - Trưởng phòng và tương đương thuộc Thanh tra Chính phủ ; Trưởng phòng và tương đương thuộc Thanh tra Bộ , ngành : cầu vai có chiều dài 13cm , phần đầu nhọn rộng 4cm , phần đuôi rộng 5cm , nền cấp hiệu bằng vải nỉ màu đỏ , cốt cấp hiệu bằng nhựa nguyên chất màu trắng ; sao cấp hiệu bằng đồng tấm mạ màu trắng bóng ; có lé bằng vải màu xanh rộng** → `DIEM` (span: `[16:98]`)
- `[e7]` **Thanh tra Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[36:38]`) *(lồng trong `e6` (`DIEM`))*
- `[e8]` **Thanh tra Bộ** → `CO_QUAN_THAM_QUYEN` (span: `[43:45]`) *(lồng trong `e6` (`DIEM`))*
- `[e9]` **cán bộ** → `CHU_THE_CA_NHAN` (span: `[23:24]`) *(lồng trong `e6` (`DIEM`))*

**Quan hệ:**
- (`e1` 02/2015/TT-TTCP `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Thanh tra Chính phủ `[CO_QUAN_BAN_HANH]`)
- (`e1` 02/2015/TT-TTCP `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 02/2015/TT-TTCP `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Thanh tra `[LINH_VUC]`)
- (`e4` Điều 6 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 02/2015/TT-TTCP `[SO_HIEU]`)
- (`e5` Khoản 13 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 6 `[DIEU]`)
- (`e6` a ) Cầu vai , cấp hàm đối với cán bộ , thanh tra viên giữ chức vụ lãnh đạo quản lý - Trưởng phòng và tương đương thuộc Thanh tra Chính phủ ; Trưởng phòng và tương đương thuộc Thanh tra Bộ , ngành : cầu vai có chiều dài 13cm , phần đầu nhọn rộng 4cm , phần đuôi rộng 5cm , nền cấp hiệu bằng vải nỉ màu đỏ , cốt cấp hiệu bằng nhựa nguyên chất màu trắng ; sao cấp hiệu bằng đồng tấm mạ màu trắng bóng ; có lé bằng vải màu xanh rộng `[DIEM]`) ==[ **THUOC_VE** ]==> (`e5` Khoản 13 `[KHOAN]`)
- (`e1` 02/2015/TT-TTCP `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Thanh tra `[LINH_VUC]`)
- (`e6` a ) Cầu vai , cấp hàm đối với cán bộ , thanh tra viên giữ chức vụ lãnh đạo quản lý - Trưởng phòng và tương đương thuộc Thanh tra Chính phủ ; Trưởng phòng và tương đương thuộc Thanh tra Bộ , ngành : cầu vai có chiều dài 13cm , phần đầu nhọn rộng 4cm , phần đuôi rộng 5cm , nền cấp hiệu bằng vải nỉ màu đỏ , cốt cấp hiệu bằng nhựa nguyên chất màu trắng ; sao cấp hiệu bằng đồng tấm mạ màu trắng bóng ; có lé bằng vải màu xanh rộng `[DIEM]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Thanh tra `[LINH_VUC]`)


---

### Mẫu #02_2015_TT-TTCP_58849#body_standalone_61 (Loại: `body_standalone`)
> **[Điều 6]`<DIEU>`** . **[Khoản 13]`<KHOAN>`** . **[a ) Cầu vai , cấp hàm đối với **[cán bộ]`<CHU_THE_CA_NHAN>`** , thanh tra viên giữ chức vụ lãnh đạo quản lý - Trưởng phòng và tương đương thuộc **[Thanh tra Chính phủ]`<CO_QUAN_THAM_QUYEN>`** ; Trưởng phòng và tương đương thuộc **[Thanh tra Bộ]`<CO_QUAN_THAM_QUYEN>`** , ngành : cầu vai có chiều dài 13cm , phần đầu nhọn rộng 4cm , phần đuôi rộng 5cm , nền cấp hiệu bằng vải nỉ màu đỏ , cốt cấp hiệu bằng nhựa nguyên chất màu trắng ; sao cấp hiệu bằng đồng tấm mạ màu trắng bóng ; có lé bằng vải màu xanh rộng]`<DIEM>`**

**Thực thể:**
- `[e0]` **Điều 6** → `DIEU` (span: `[0:2]`)
- `[e1]` **Khoản 13** → `KHOAN` (span: `[3:5]`)
- `[e2]` **a ) Cầu vai , cấp hàm đối với cán bộ , thanh tra viên giữ chức vụ lãnh đạo quản lý - Trưởng phòng và tương đương thuộc Thanh tra Chính phủ ; Trưởng phòng và tương đương thuộc Thanh tra Bộ , ngành : cầu vai có chiều dài 13cm , phần đầu nhọn rộng 4cm , phần đuôi rộng 5cm , nền cấp hiệu bằng vải nỉ màu đỏ , cốt cấp hiệu bằng nhựa nguyên chất màu trắng ; sao cấp hiệu bằng đồng tấm mạ màu trắng bóng ; có lé bằng vải màu xanh rộng** → `DIEM` (span: `[6:88]`)
- `[e3]` **Thanh tra Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[26:28]`) *(lồng trong `e2` (`DIEM`))*
- `[e4]` **Thanh tra Bộ** → `CO_QUAN_THAM_QUYEN` (span: `[33:35]`) *(lồng trong `e2` (`DIEM`))*
- `[e5]` **cán bộ** → `CHU_THE_CA_NHAN` (span: `[13:14]`) *(lồng trong `e2` (`DIEM`))*

**Quan hệ:**
- (`e1` Khoản 13 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 6 `[DIEU]`)
- (`e2` a ) Cầu vai , cấp hàm đối với cán bộ , thanh tra viên giữ chức vụ lãnh đạo quản lý - Trưởng phòng và tương đương thuộc Thanh tra Chính phủ ; Trưởng phòng và tương đương thuộc Thanh tra Bộ , ngành : cầu vai có chiều dài 13cm , phần đầu nhọn rộng 4cm , phần đuôi rộng 5cm , nền cấp hiệu bằng vải nỉ màu đỏ , cốt cấp hiệu bằng nhựa nguyên chất màu trắng ; sao cấp hiệu bằng đồng tấm mạ màu trắng bóng ; có lé bằng vải màu xanh rộng `[DIEM]`) ==[ **THUOC_VE** ]==> (`e1` Khoản 13 `[KHOAN]`)


---

### Mẫu #02_2015_TT-TTCP_58849#body_context_62 (Loại: `body_context`)
> **[Thanh tra Chính phủ]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[02/2015/TT-TTCP]`<SO_HIEU>`** . **[Điều 6]`<DIEU>`** . **[Khoản 13]`<KHOAN>`** . **[a ) Cầu vai , cấp hàm đối với **[cán bộ]`<CHU_THE_CA_NHAN>`** , thanh tra viên giữ chức vụ lãnh đạo quản lý - Phó trưởng phòng và tương đương thuộc **[Thanh tra Chính phủ]`<CO_QUAN_THAM_QUYEN>`** ; Phó trưởng phòng và tương đương thuộc **[Thanh tra Bộ]`<CO_QUAN_THAM_QUYEN>`** , ngành : cầu vai có chiều dài 13cm , phần đầu nhọn rộng 4cm , phần đuôi rộng 5cm , nền cấp hiệu bằng vải nỉ màu đỏ , cốt cấp hiệu bằng nhựa nguyên chất màu trắng ; sao cấp hiệu bằng đồng tấm mạ màu trắng bóng ; có lé bằng vải màu]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[3:4]`)
- `[e1]` **02/2015/TT-TTCP** → `SO_HIEU` (span: `[5:6]`)
- `[e2]` **Thanh tra Chính phủ** → `CO_QUAN_BAN_HANH` (span: `[0:2]`)
- `[e3]` **Điều 6** → `DIEU` (span: `[7:9]`)
- `[e4]` **Khoản 13** → `KHOAN` (span: `[10:12]`)
- `[e5]` **a ) Cầu vai , cấp hàm đối với cán bộ , thanh tra viên giữ chức vụ lãnh đạo quản lý - Phó trưởng phòng và tương đương thuộc Thanh tra Chính phủ ; Phó trưởng phòng và tương đương thuộc Thanh tra Bộ , ngành : cầu vai có chiều dài 13cm , phần đầu nhọn rộng 4cm , phần đuôi rộng 5cm , nền cấp hiệu bằng vải nỉ màu đỏ , cốt cấp hiệu bằng nhựa nguyên chất màu trắng ; sao cấp hiệu bằng đồng tấm mạ màu trắng bóng ; có lé bằng vải màu** → `DIEM` (span: `[13:93]`)
- `[e6]` **Thanh tra Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[33:35]`) *(lồng trong `e5` (`DIEM`))*
- `[e7]` **Thanh tra Bộ** → `CO_QUAN_THAM_QUYEN` (span: `[40:42]`) *(lồng trong `e5` (`DIEM`))*
- `[e8]` **cán bộ** → `CHU_THE_CA_NHAN` (span: `[20:21]`) *(lồng trong `e5` (`DIEM`))*

**Quan hệ:**
- (`e1` 02/2015/TT-TTCP `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Thanh tra Chính phủ `[CO_QUAN_BAN_HANH]`)
- (`e1` 02/2015/TT-TTCP `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 6 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 02/2015/TT-TTCP `[SO_HIEU]`)
- (`e4` Khoản 13 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 6 `[DIEU]`)
- (`e5` a ) Cầu vai , cấp hàm đối với cán bộ , thanh tra viên giữ chức vụ lãnh đạo quản lý - Phó trưởng phòng và tương đương thuộc Thanh tra Chính phủ ; Phó trưởng phòng và tương đương thuộc Thanh tra Bộ , ngành : cầu vai có chiều dài 13cm , phần đầu nhọn rộng 4cm , phần đuôi rộng 5cm , nền cấp hiệu bằng vải nỉ màu đỏ , cốt cấp hiệu bằng nhựa nguyên chất màu trắng ; sao cấp hiệu bằng đồng tấm mạ màu trắng bóng ; có lé bằng vải màu `[DIEM]`) ==[ **THUOC_VE** ]==> (`e4` Khoản 13 `[KHOAN]`)


---

### Mẫu #02_2015_TT-TTCP_58849#body_standalone_63 (Loại: `body_standalone`)
> **[Điều 6]`<DIEU>`** . **[Khoản 13]`<KHOAN>`** . **[a ) Cầu vai , cấp hàm đối với **[cán bộ]`<CHU_THE_CA_NHAN>`** , thanh tra viên giữ chức vụ lãnh đạo quản lý - Phó trưởng phòng và tương đương thuộc **[Thanh tra Chính phủ]`<CO_QUAN_THAM_QUYEN>`** ; Phó trưởng phòng và tương đương thuộc **[Thanh tra Bộ]`<CO_QUAN_THAM_QUYEN>`** , ngành : cầu vai có chiều dài 13cm , phần đầu nhọn rộng 4cm , phần đuôi rộng 5cm , nền cấp hiệu bằng vải nỉ màu đỏ , cốt cấp hiệu bằng nhựa nguyên chất màu trắng ; sao cấp hiệu bằng đồng tấm mạ màu trắng bóng ; có lé bằng vải màu]`<DIEM>`**

**Thực thể:**
- `[e0]` **Điều 6** → `DIEU` (span: `[0:2]`)
- `[e1]` **Khoản 13** → `KHOAN` (span: `[3:5]`)
- `[e2]` **a ) Cầu vai , cấp hàm đối với cán bộ , thanh tra viên giữ chức vụ lãnh đạo quản lý - Phó trưởng phòng và tương đương thuộc Thanh tra Chính phủ ; Phó trưởng phòng và tương đương thuộc Thanh tra Bộ , ngành : cầu vai có chiều dài 13cm , phần đầu nhọn rộng 4cm , phần đuôi rộng 5cm , nền cấp hiệu bằng vải nỉ màu đỏ , cốt cấp hiệu bằng nhựa nguyên chất màu trắng ; sao cấp hiệu bằng đồng tấm mạ màu trắng bóng ; có lé bằng vải màu** → `DIEM` (span: `[6:86]`)
- `[e3]` **Thanh tra Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[26:28]`) *(lồng trong `e2` (`DIEM`))*
- `[e4]` **Thanh tra Bộ** → `CO_QUAN_THAM_QUYEN` (span: `[33:35]`) *(lồng trong `e2` (`DIEM`))*
- `[e5]` **cán bộ** → `CHU_THE_CA_NHAN` (span: `[13:14]`) *(lồng trong `e2` (`DIEM`))*

**Quan hệ:**
- (`e1` Khoản 13 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 6 `[DIEU]`)
- (`e2` a ) Cầu vai , cấp hàm đối với cán bộ , thanh tra viên giữ chức vụ lãnh đạo quản lý - Phó trưởng phòng và tương đương thuộc Thanh tra Chính phủ ; Phó trưởng phòng và tương đương thuộc Thanh tra Bộ , ngành : cầu vai có chiều dài 13cm , phần đầu nhọn rộng 4cm , phần đuôi rộng 5cm , nền cấp hiệu bằng vải nỉ màu đỏ , cốt cấp hiệu bằng nhựa nguyên chất màu trắng ; sao cấp hiệu bằng đồng tấm mạ màu trắng bóng ; có lé bằng vải màu `[DIEM]`) ==[ **THUOC_VE** ]==> (`e1` Khoản 13 `[KHOAN]`)


---

### Mẫu #02_2015_TT-TTCP_58849#body_context_64 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[02/2015/TT-TTCP]`<SO_HIEU>`** ban hành **[ngày 16 tháng 03 năm 2015]`<NGAY_BAN_HANH>`** bởi **[Thanh tra Chính phủ]`<CO_QUAN_BAN_HANH>`** . **[Điều 6]`<DIEU>`** . **[Khoản 13]`<KHOAN>`** . **[a ) Cầu vai , cấp hàm đối với **[cán bộ]`<CHU_THE_CA_NHAN>`** , thanh tra viên giữ chức vụ lãnh đạo quản lý - Chánh Thanh tra tỉnh , thành phố trực thuộc Trung ương : cầu vai có chiều dài 13cm , phần đầu nhọn rộng 4cm , phần đuôi rộng 5cm , nền cấp hiệu bằng vải nỉ màu đỏ , cốt cấp hiệu bằng nhựa nguyên chất màu trắng ; sao cấp hiệu bằng đồng tấm mạ màu trắng bóng ; có lé bằng vải màu xanh rộng 3mm ; cúc cấp hiệu hình tròn có ngôi sao ở]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **02/2015/TT-TTCP** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Thanh tra Chính phủ** → `CO_QUAN_BAN_HANH` (span: `[11:13]`)
- `[e3]` **ngày 16 tháng 03 năm 2015** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 6** → `DIEU` (span: `[14:16]`)
- `[e5]` **Khoản 13** → `KHOAN` (span: `[17:19]`)
- `[e6]` **a ) Cầu vai , cấp hàm đối với cán bộ , thanh tra viên giữ chức vụ lãnh đạo quản lý - Chánh Thanh tra tỉnh , thành phố trực thuộc Trung ương : cầu vai có chiều dài 13cm , phần đầu nhọn rộng 4cm , phần đuôi rộng 5cm , nền cấp hiệu bằng vải nỉ màu đỏ , cốt cấp hiệu bằng nhựa nguyên chất màu trắng ; sao cấp hiệu bằng đồng tấm mạ màu trắng bóng ; có lé bằng vải màu xanh rộng 3mm ; cúc cấp hiệu hình tròn có ngôi sao ở** → `DIEM` (span: `[20:102]`)
- `[e7]` **cán bộ** → `CHU_THE_CA_NHAN` (span: `[27:28]`) *(lồng trong `e6` (`DIEM`))*

**Quan hệ:**
- (`e1` 02/2015/TT-TTCP `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Thanh tra Chính phủ `[CO_QUAN_BAN_HANH]`)
- (`e1` 02/2015/TT-TTCP `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 02/2015/TT-TTCP `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 16 tháng 03 năm 2015 `[NGAY_BAN_HANH]`)
- (`e4` Điều 6 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 02/2015/TT-TTCP `[SO_HIEU]`)
- (`e5` Khoản 13 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 6 `[DIEU]`)
- (`e6` a ) Cầu vai , cấp hàm đối với cán bộ , thanh tra viên giữ chức vụ lãnh đạo quản lý - Chánh Thanh tra tỉnh , thành phố trực thuộc Trung ương : cầu vai có chiều dài 13cm , phần đầu nhọn rộng 4cm , phần đuôi rộng 5cm , nền cấp hiệu bằng vải nỉ màu đỏ , cốt cấp hiệu bằng nhựa nguyên chất màu trắng ; sao cấp hiệu bằng đồng tấm mạ màu trắng bóng ; có lé bằng vải màu xanh rộng 3mm ; cúc cấp hiệu hình tròn có ngôi sao ở `[DIEM]`) ==[ **THUOC_VE** ]==> (`e5` Khoản 13 `[KHOAN]`)


---

### Mẫu #02_2015_TT-TTCP_58849#body_context_65 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[02/2015/TT-TTCP]`<SO_HIEU>`** ban hành **[ngày 16 tháng 03 năm 2015]`<NGAY_BAN_HANH>`** bởi **[Thanh tra Chính phủ]`<CO_QUAN_BAN_HANH>`** . **[Điều 6]`<DIEU>`** . **[Khoản 13]`<KHOAN>`** . **[a ) Cầu vai , cấp hàm đối với **[cán bộ]`<CHU_THE_CA_NHAN>`** , thanh tra viên giữ chức vụ lãnh đạo quản lý - Phó Chánh Thanh tra tỉnh , thành phố trực thuộc Trung ương : cầu vai có chiều dài 13cm , phần đầu nhọn rộng 4cm , phần đuôi rộng 5cm , nền cấp hiệu bằng vải nỉ màu đỏ , cốt cấp hiệu bằng nhựa nguyên chất màu trắng ; sao cấp hiệu bằng đồng tấm mạ màu trắng bóng ; có lé bằng vải màu xanh rộng 3mm ; cúc cấp hiệu hình tròn có ngôi sao]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **02/2015/TT-TTCP** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Thanh tra Chính phủ** → `CO_QUAN_BAN_HANH` (span: `[11:13]`)
- `[e3]` **ngày 16 tháng 03 năm 2015** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 6** → `DIEU` (span: `[14:16]`)
- `[e5]` **Khoản 13** → `KHOAN` (span: `[17:19]`)
- `[e6]` **a ) Cầu vai , cấp hàm đối với cán bộ , thanh tra viên giữ chức vụ lãnh đạo quản lý - Phó Chánh Thanh tra tỉnh , thành phố trực thuộc Trung ương : cầu vai có chiều dài 13cm , phần đầu nhọn rộng 4cm , phần đuôi rộng 5cm , nền cấp hiệu bằng vải nỉ màu đỏ , cốt cấp hiệu bằng nhựa nguyên chất màu trắng ; sao cấp hiệu bằng đồng tấm mạ màu trắng bóng ; có lé bằng vải màu xanh rộng 3mm ; cúc cấp hiệu hình tròn có ngôi sao** → `DIEM` (span: `[20:101]`)
- `[e7]` **cán bộ** → `CHU_THE_CA_NHAN` (span: `[27:28]`) *(lồng trong `e6` (`DIEM`))*

**Quan hệ:**
- (`e1` 02/2015/TT-TTCP `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Thanh tra Chính phủ `[CO_QUAN_BAN_HANH]`)
- (`e1` 02/2015/TT-TTCP `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 02/2015/TT-TTCP `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 16 tháng 03 năm 2015 `[NGAY_BAN_HANH]`)
- (`e4` Điều 6 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 02/2015/TT-TTCP `[SO_HIEU]`)
- (`e5` Khoản 13 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 6 `[DIEU]`)
- (`e6` a ) Cầu vai , cấp hàm đối với cán bộ , thanh tra viên giữ chức vụ lãnh đạo quản lý - Phó Chánh Thanh tra tỉnh , thành phố trực thuộc Trung ương : cầu vai có chiều dài 13cm , phần đầu nhọn rộng 4cm , phần đuôi rộng 5cm , nền cấp hiệu bằng vải nỉ màu đỏ , cốt cấp hiệu bằng nhựa nguyên chất màu trắng ; sao cấp hiệu bằng đồng tấm mạ màu trắng bóng ; có lé bằng vải màu xanh rộng 3mm ; cúc cấp hiệu hình tròn có ngôi sao `[DIEM]`) ==[ **THUOC_VE** ]==> (`e5` Khoản 13 `[KHOAN]`)


---

### Mẫu #02_2015_TT-TTCP_58849#body_context_66 (Loại: `body_context`)
> **[Thanh tra Chính phủ]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[02/2015/TT-TTCP]`<SO_HIEU>`** . **[Điều 6]`<DIEU>`** . **[Khoản 13]`<KHOAN>`** . **[a ) Cầu vai , cấp hàm đối với **[cán bộ]`<CHU_THE_CA_NHAN>`** , thanh tra viên giữ chức vụ lãnh đạo quản lý - Trưởng phòng và tương đương thuộc Thanh tra tỉnh , thành phố trực thuộc Trung ương ; **[Chánh Thanh tra sở]`<CO_QUAN_THAM_QUYEN>`** , ngành : cầu vai có chiều dài 13cm , phần đầu nhọn rộng 4cm , phần đuôi rộng 5cm , nền cấp hiệu bằng vải nỉ màu đỏ , cốt cấp hiệu bằng nhựa nguyên chất màu trắng ; sao cấp hiệu bằng đồng tấm mạ màu trắng bóng ; có lé bằng vải màu xanh rộng]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[3:4]`)
- `[e1]` **02/2015/TT-TTCP** → `SO_HIEU` (span: `[5:6]`)
- `[e2]` **Thanh tra Chính phủ** → `CO_QUAN_BAN_HANH` (span: `[0:2]`)
- `[e3]` **Điều 6** → `DIEU` (span: `[7:9]`)
- `[e4]` **Khoản 13** → `KHOAN` (span: `[10:12]`)
- `[e5]` **a ) Cầu vai , cấp hàm đối với cán bộ , thanh tra viên giữ chức vụ lãnh đạo quản lý - Trưởng phòng và tương đương thuộc Thanh tra tỉnh , thành phố trực thuộc Trung ương ; Chánh Thanh tra sở , ngành : cầu vai có chiều dài 13cm , phần đầu nhọn rộng 4cm , phần đuôi rộng 5cm , nền cấp hiệu bằng vải nỉ màu đỏ , cốt cấp hiệu bằng nhựa nguyên chất màu trắng ; sao cấp hiệu bằng đồng tấm mạ màu trắng bóng ; có lé bằng vải màu xanh rộng** → `DIEM` (span: `[13:96]`)
- `[e6]` **Chánh Thanh tra sở** → `CO_QUAN_THAM_QUYEN` (span: `[40:43]`) *(lồng trong `e5` (`DIEM`))*
- `[e7]` **cán bộ** → `CHU_THE_CA_NHAN` (span: `[20:21]`) *(lồng trong `e5` (`DIEM`))*

**Quan hệ:**
- (`e1` 02/2015/TT-TTCP `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Thanh tra Chính phủ `[CO_QUAN_BAN_HANH]`)
- (`e1` 02/2015/TT-TTCP `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 6 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 02/2015/TT-TTCP `[SO_HIEU]`)
- (`e4` Khoản 13 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 6 `[DIEU]`)
- (`e5` a ) Cầu vai , cấp hàm đối với cán bộ , thanh tra viên giữ chức vụ lãnh đạo quản lý - Trưởng phòng và tương đương thuộc Thanh tra tỉnh , thành phố trực thuộc Trung ương ; Chánh Thanh tra sở , ngành : cầu vai có chiều dài 13cm , phần đầu nhọn rộng 4cm , phần đuôi rộng 5cm , nền cấp hiệu bằng vải nỉ màu đỏ , cốt cấp hiệu bằng nhựa nguyên chất màu trắng ; sao cấp hiệu bằng đồng tấm mạ màu trắng bóng ; có lé bằng vải màu xanh rộng `[DIEM]`) ==[ **THUOC_VE** ]==> (`e4` Khoản 13 `[KHOAN]`)


---

### Mẫu #02_2015_TT-TTCP_58849#body_standalone_67 (Loại: `body_standalone`)
> **[Điều 6]`<DIEU>`** . **[Khoản 13]`<KHOAN>`** . **[a ) Cầu vai , cấp hàm đối với **[cán bộ]`<CHU_THE_CA_NHAN>`** , thanh tra viên giữ chức vụ lãnh đạo quản lý - Trưởng phòng và tương đương thuộc Thanh tra tỉnh , thành phố trực thuộc Trung ương ; **[Chánh Thanh tra sở]`<CO_QUAN_THAM_QUYEN>`** , ngành : cầu vai có chiều dài 13cm , phần đầu nhọn rộng 4cm , phần đuôi rộng 5cm , nền cấp hiệu bằng vải nỉ màu đỏ , cốt cấp hiệu bằng nhựa nguyên chất màu trắng ; sao cấp hiệu bằng đồng tấm mạ màu trắng bóng ; có lé bằng vải màu xanh rộng]`<DIEM>`**

**Thực thể:**
- `[e0]` **Điều 6** → `DIEU` (span: `[0:2]`)
- `[e1]` **Khoản 13** → `KHOAN` (span: `[3:5]`)
- `[e2]` **a ) Cầu vai , cấp hàm đối với cán bộ , thanh tra viên giữ chức vụ lãnh đạo quản lý - Trưởng phòng và tương đương thuộc Thanh tra tỉnh , thành phố trực thuộc Trung ương ; Chánh Thanh tra sở , ngành : cầu vai có chiều dài 13cm , phần đầu nhọn rộng 4cm , phần đuôi rộng 5cm , nền cấp hiệu bằng vải nỉ màu đỏ , cốt cấp hiệu bằng nhựa nguyên chất màu trắng ; sao cấp hiệu bằng đồng tấm mạ màu trắng bóng ; có lé bằng vải màu xanh rộng** → `DIEM` (span: `[6:89]`)
- `[e3]` **Chánh Thanh tra sở** → `CO_QUAN_THAM_QUYEN` (span: `[33:36]`) *(lồng trong `e2` (`DIEM`))*
- `[e4]` **cán bộ** → `CHU_THE_CA_NHAN` (span: `[13:14]`) *(lồng trong `e2` (`DIEM`))*

**Quan hệ:**
- (`e1` Khoản 13 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 6 `[DIEU]`)
- (`e2` a ) Cầu vai , cấp hàm đối với cán bộ , thanh tra viên giữ chức vụ lãnh đạo quản lý - Trưởng phòng và tương đương thuộc Thanh tra tỉnh , thành phố trực thuộc Trung ương ; Chánh Thanh tra sở , ngành : cầu vai có chiều dài 13cm , phần đầu nhọn rộng 4cm , phần đuôi rộng 5cm , nền cấp hiệu bằng vải nỉ màu đỏ , cốt cấp hiệu bằng nhựa nguyên chất màu trắng ; sao cấp hiệu bằng đồng tấm mạ màu trắng bóng ; có lé bằng vải màu xanh rộng `[DIEM]`) ==[ **THUOC_VE** ]==> (`e1` Khoản 13 `[KHOAN]`)


---

### Mẫu #02_2015_TT-TTCP_58849#body_context_68 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[02/2015/TT-TTCP]`<SO_HIEU>`** ban hành **[ngày 16 tháng 03 năm 2015]`<NGAY_BAN_HANH>`** bởi **[Thanh tra Chính phủ]`<CO_QUAN_BAN_HANH>`** . **[Điều 6]`<DIEU>`** . **[Khoản 13]`<KHOAN>`** . **[a ) Cầu vai , cấp hàm đối với **[cán bộ]`<CHU_THE_CA_NHAN>`** , thanh tra viên giữ chức vụ lãnh đạo quản lý - Phó trưởng phòng và tương đương thuộc Thanh tra tỉnh , thành phố trực thuộc Trung ương ; Phó **[chánh Thanh tra sở]`<CO_QUAN_THAM_QUYEN>`** , ngành ; Chánh Thanh tra huyện , quận , thị xã , thành phố thuộc tỉnh : cầu vai có chiều dài 13cm , phần đầu nhọn rộng 4cm , phần đuôi rộng 5cm , nền cấp hiệu bằng vải nỉ màu đỏ , cốt cấp hiệu bằng nhựa nguyên chất màu trắng ; sao cấp hiệu bằng]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **02/2015/TT-TTCP** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Thanh tra Chính phủ** → `CO_QUAN_BAN_HANH` (span: `[11:13]`)
- `[e3]` **ngày 16 tháng 03 năm 2015** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 6** → `DIEU` (span: `[14:16]`)
- `[e5]` **Khoản 13** → `KHOAN` (span: `[17:19]`)
- `[e6]` **a ) Cầu vai , cấp hàm đối với cán bộ , thanh tra viên giữ chức vụ lãnh đạo quản lý - Phó trưởng phòng và tương đương thuộc Thanh tra tỉnh , thành phố trực thuộc Trung ương ; Phó chánh Thanh tra sở , ngành ; Chánh Thanh tra huyện , quận , thị xã , thành phố thuộc tỉnh : cầu vai có chiều dài 13cm , phần đầu nhọn rộng 4cm , phần đuôi rộng 5cm , nền cấp hiệu bằng vải nỉ màu đỏ , cốt cấp hiệu bằng nhựa nguyên chất màu trắng ; sao cấp hiệu bằng** → `DIEM` (span: `[20:102]`)
- `[e7]` **chánh Thanh tra sở** → `CO_QUAN_THAM_QUYEN` (span: `[48:51]`) *(lồng trong `e6` (`DIEM`))*
- `[e8]` **cán bộ** → `CHU_THE_CA_NHAN` (span: `[27:28]`) *(lồng trong `e6` (`DIEM`))*

**Quan hệ:**
- (`e1` 02/2015/TT-TTCP `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Thanh tra Chính phủ `[CO_QUAN_BAN_HANH]`)
- (`e1` 02/2015/TT-TTCP `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 02/2015/TT-TTCP `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 16 tháng 03 năm 2015 `[NGAY_BAN_HANH]`)
- (`e4` Điều 6 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 02/2015/TT-TTCP `[SO_HIEU]`)
- (`e5` Khoản 13 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 6 `[DIEU]`)
- (`e6` a ) Cầu vai , cấp hàm đối với cán bộ , thanh tra viên giữ chức vụ lãnh đạo quản lý - Phó trưởng phòng và tương đương thuộc Thanh tra tỉnh , thành phố trực thuộc Trung ương ; Phó chánh Thanh tra sở , ngành ; Chánh Thanh tra huyện , quận , thị xã , thành phố thuộc tỉnh : cầu vai có chiều dài 13cm , phần đầu nhọn rộng 4cm , phần đuôi rộng 5cm , nền cấp hiệu bằng vải nỉ màu đỏ , cốt cấp hiệu bằng nhựa nguyên chất màu trắng ; sao cấp hiệu bằng `[DIEM]`) ==[ **THUOC_VE** ]==> (`e5` Khoản 13 `[KHOAN]`)


---

### Mẫu #02_2015_TT-TTCP_58849#body_standalone_69 (Loại: `body_standalone`)
> **[Điều 6]`<DIEU>`** . **[Khoản 13]`<KHOAN>`** . **[a ) Cầu vai , cấp hàm đối với **[cán bộ]`<CHU_THE_CA_NHAN>`** , thanh tra viên giữ chức vụ lãnh đạo quản lý - Phó trưởng phòng và tương đương thuộc Thanh tra tỉnh , thành phố trực thuộc Trung ương ; Phó **[chánh Thanh tra sở]`<CO_QUAN_THAM_QUYEN>`** , ngành ; Chánh Thanh tra huyện , quận , thị xã , thành phố thuộc tỉnh : cầu vai có chiều dài 13cm , phần đầu nhọn rộng 4cm , phần đuôi rộng 5cm , nền cấp hiệu bằng vải nỉ màu đỏ , cốt cấp hiệu bằng nhựa nguyên chất màu trắng ; sao cấp hiệu bằng]`<DIEM>`**

**Thực thể:**
- `[e0]` **Điều 6** → `DIEU` (span: `[0:2]`)
- `[e1]` **Khoản 13** → `KHOAN` (span: `[3:5]`)
- `[e2]` **a ) Cầu vai , cấp hàm đối với cán bộ , thanh tra viên giữ chức vụ lãnh đạo quản lý - Phó trưởng phòng và tương đương thuộc Thanh tra tỉnh , thành phố trực thuộc Trung ương ; Phó chánh Thanh tra sở , ngành ; Chánh Thanh tra huyện , quận , thị xã , thành phố thuộc tỉnh : cầu vai có chiều dài 13cm , phần đầu nhọn rộng 4cm , phần đuôi rộng 5cm , nền cấp hiệu bằng vải nỉ màu đỏ , cốt cấp hiệu bằng nhựa nguyên chất màu trắng ; sao cấp hiệu bằng** → `DIEM` (span: `[6:88]`)
- `[e3]` **chánh Thanh tra sở** → `CO_QUAN_THAM_QUYEN` (span: `[34:37]`) *(lồng trong `e2` (`DIEM`))*
- `[e4]` **cán bộ** → `CHU_THE_CA_NHAN` (span: `[13:14]`) *(lồng trong `e2` (`DIEM`))*

**Quan hệ:**
- (`e1` Khoản 13 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 6 `[DIEU]`)
- (`e2` a ) Cầu vai , cấp hàm đối với cán bộ , thanh tra viên giữ chức vụ lãnh đạo quản lý - Phó trưởng phòng và tương đương thuộc Thanh tra tỉnh , thành phố trực thuộc Trung ương ; Phó chánh Thanh tra sở , ngành ; Chánh Thanh tra huyện , quận , thị xã , thành phố thuộc tỉnh : cầu vai có chiều dài 13cm , phần đầu nhọn rộng 4cm , phần đuôi rộng 5cm , nền cấp hiệu bằng vải nỉ màu đỏ , cốt cấp hiệu bằng nhựa nguyên chất màu trắng ; sao cấp hiệu bằng `[DIEM]`) ==[ **THUOC_VE** ]==> (`e1` Khoản 13 `[KHOAN]`)


---

### Mẫu #02_2015_TT-TTCP_58849#body_context_70 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[02/2015/TT-TTCP]`<SO_HIEU>`** ban hành **[ngày 16 tháng 03 năm 2015]`<NGAY_BAN_HANH>`** bởi **[Thanh tra Chính phủ]`<CO_QUAN_BAN_HANH>`** . **[Điều 6]`<DIEU>`** . **[Khoản 13]`<KHOAN>`** . **[a ) Cầu vai , cấp hàm đối với **[cán bộ]`<CHU_THE_CA_NHAN>`** , thanh tra viên giữ chức vụ lãnh đạo quản lý - Phó chánh Thanh tra huyện , quận , thị xã , thành phố thuộc tỉnh : cầu vai có chiều dài 13cm , phần đầu nhọn rộng 4cm , phần đuôi rộng 5cm , nền cấp hiệu bằng vải nỉ màu đỏ , cốt cấp hiệu bằng nhựa nguyên chất màu trắng ; sao cấp hiệu bằng đồng tấm mạ màu trắng bóng ; có lé bằng vải màu xanh rộng 3mm ; cúc cấp hiệu hình tròn có ngôi]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **02/2015/TT-TTCP** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Thanh tra Chính phủ** → `CO_QUAN_BAN_HANH` (span: `[11:13]`)
- `[e3]` **ngày 16 tháng 03 năm 2015** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 6** → `DIEU` (span: `[14:16]`)
- `[e5]` **Khoản 13** → `KHOAN` (span: `[17:19]`)
- `[e6]` **a ) Cầu vai , cấp hàm đối với cán bộ , thanh tra viên giữ chức vụ lãnh đạo quản lý - Phó chánh Thanh tra huyện , quận , thị xã , thành phố thuộc tỉnh : cầu vai có chiều dài 13cm , phần đầu nhọn rộng 4cm , phần đuôi rộng 5cm , nền cấp hiệu bằng vải nỉ màu đỏ , cốt cấp hiệu bằng nhựa nguyên chất màu trắng ; sao cấp hiệu bằng đồng tấm mạ màu trắng bóng ; có lé bằng vải màu xanh rộng 3mm ; cúc cấp hiệu hình tròn có ngôi** → `DIEM` (span: `[20:105]`)
- `[e7]` **cán bộ** → `CHU_THE_CA_NHAN` (span: `[27:28]`) *(lồng trong `e6` (`DIEM`))*

**Quan hệ:**
- (`e1` 02/2015/TT-TTCP `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Thanh tra Chính phủ `[CO_QUAN_BAN_HANH]`)
- (`e1` 02/2015/TT-TTCP `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 02/2015/TT-TTCP `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 16 tháng 03 năm 2015 `[NGAY_BAN_HANH]`)
- (`e4` Điều 6 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 02/2015/TT-TTCP `[SO_HIEU]`)
- (`e5` Khoản 13 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 6 `[DIEU]`)
- (`e6` a ) Cầu vai , cấp hàm đối với cán bộ , thanh tra viên giữ chức vụ lãnh đạo quản lý - Phó chánh Thanh tra huyện , quận , thị xã , thành phố thuộc tỉnh : cầu vai có chiều dài 13cm , phần đầu nhọn rộng 4cm , phần đuôi rộng 5cm , nền cấp hiệu bằng vải nỉ màu đỏ , cốt cấp hiệu bằng nhựa nguyên chất màu trắng ; sao cấp hiệu bằng đồng tấm mạ màu trắng bóng ; có lé bằng vải màu xanh rộng 3mm ; cúc cấp hiệu hình tròn có ngôi `[DIEM]`) ==[ **THUOC_VE** ]==> (`e5` Khoản 13 `[KHOAN]`)


---

### Mẫu #02_2015_TT-TTCP_58849#body_context_71 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[02/2015/TT-TTCP]`<SO_HIEU>`** ban hành **[ngày 16 tháng 03 năm 2015]`<NGAY_BAN_HANH>`** bởi **[Thanh tra Chính phủ]`<CO_QUAN_BAN_HANH>`** . **[Chương II]`<CHUONG>`** . **[Điều 7 . Trang phục đối với **[công chức]`<CHU_THE_CA_NHAN>`** , **[viên chức]`<CHU_THE_CA_NHAN>`** chưa phải là thanh tra viên . **[Công chức]`<CHU_THE_CA_NHAN>`** , **[viên chức]`<CHU_THE_CA_NHAN>`** thuộc các cơ quan thanh tra nhà nước được cấp trang phục như đối với thanh tra viên ( trừ mũ kêpi , cấp hiệu , cầu vai , cấp hàm ) .]`<DIEU>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **02/2015/TT-TTCP** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Thanh tra Chính phủ** → `CO_QUAN_BAN_HANH` (span: `[11:13]`)
- `[e3]` **ngày 16 tháng 03 năm 2015** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Chương II** → `CHUONG` (span: `[14:16]`)
- `[e5]` **Điều 7 . Trang phục đối với công chức , viên chức chưa phải là thanh tra viên . Công chức , viên chức thuộc các cơ quan thanh tra nhà nước được cấp trang phục như đối với thanh tra viên ( trừ mũ kêpi , cấp hiệu , cầu vai , cấp hàm ) .** → `DIEU` (span: `[17:58]`)
- `[e6]` **công chức** → `CHU_THE_CA_NHAN` (span: `[22:23]`) *(lồng trong `e5` (`DIEU`))*
- `[e7]` **viên chức** → `CHU_THE_CA_NHAN` (span: `[24:25]`) *(lồng trong `e5` (`DIEU`))*
- `[e8]` **Công chức** → `CHU_THE_CA_NHAN` (span: `[31:32]`) *(lồng trong `e5` (`DIEU`))*
- `[e9]` **viên chức** → `CHU_THE_CA_NHAN` (span: `[33:34]`) *(lồng trong `e5` (`DIEU`))*

**Quan hệ:**
- (`e1` 02/2015/TT-TTCP `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Thanh tra Chính phủ `[CO_QUAN_BAN_HANH]`)
- (`e1` 02/2015/TT-TTCP `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 02/2015/TT-TTCP `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 16 tháng 03 năm 2015 `[NGAY_BAN_HANH]`)
- (`e4` Chương II `[CHUONG]`) ==[ **THUOC_VE** ]==> (`e1` 02/2015/TT-TTCP `[SO_HIEU]`)
- (`e5` Điều 7 . Trang phục đối với công chức , viên chức chưa phải là thanh tra viên . Công chức , viên chức thuộc các cơ quan thanh tra nhà nước được cấp trang phục như đối với thanh tra viên ( trừ mũ kêpi , cấp hiệu , cầu vai , cấp hàm ) . `[DIEU]`) ==[ **THUOC_VE** ]==> (`e4` Chương II `[CHUONG]`)


---

### Mẫu #02_2015_TT-TTCP_58849#body_context_72 (Loại: `body_context`)
> **[Thanh tra Chính phủ]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[02/2015/TT-TTCP]`<SO_HIEU>`** . **[Điều 8]`<DIEU>`** . **[1 . Việc quản lý , cấp phát , niên hạn sử dụng trang phục của **[cán bộ]`<CHU_THE_CA_NHAN>`** , thanh tra viên , **[công chức]`<CHU_THE_CA_NHAN>`** , **[viên chức]`<CHU_THE_CA_NHAN>`** thuộc các cơ quan thanh tra nhà nước được thực hiện theo quy định của văn bản liên tịch giữa **[Thanh tra Chính phủ]`<CO_QUAN_THAM_QUYEN>`** và **[Bộ Tài chính]`<CO_QUAN_THAM_QUYEN>`** .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[3:4]`)
- `[e1]` **02/2015/TT-TTCP** → `SO_HIEU` (span: `[5:6]`)
- `[e2]` **Thanh tra Chính phủ** → `CO_QUAN_BAN_HANH` (span: `[0:2]`)
- `[e3]` **Điều 8** → `DIEU` (span: `[7:9]`)
- `[e4]` **1 . Việc quản lý , cấp phát , niên hạn sử dụng trang phục của cán bộ , thanh tra viên , công chức , viên chức thuộc các cơ quan thanh tra nhà nước được thực hiện theo quy định của văn bản liên tịch giữa Thanh tra Chính phủ và Bộ Tài chính .** → `KHOAN` (span: `[10:48]`)
- `[e5]` **Thanh tra Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[42:44]`) *(lồng trong `e4` (`KHOAN`))*
- `[e6]` **Bộ Tài chính** → `CO_QUAN_THAM_QUYEN` (span: `[45:47]`) *(lồng trong `e4` (`KHOAN`))*
- `[e7]` **cán bộ** → `CHU_THE_CA_NHAN` (span: `[21:22]`) *(lồng trong `e4` (`KHOAN`))*
- `[e8]` **công chức** → `CHU_THE_CA_NHAN` (span: `[26:27]`) *(lồng trong `e4` (`KHOAN`))*
- `[e9]` **viên chức** → `CHU_THE_CA_NHAN` (span: `[28:29]`) *(lồng trong `e4` (`KHOAN`))*

**Quan hệ:**
- (`e1` 02/2015/TT-TTCP `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Thanh tra Chính phủ `[CO_QUAN_BAN_HANH]`)
- (`e1` 02/2015/TT-TTCP `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 8 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 02/2015/TT-TTCP `[SO_HIEU]`)
- (`e4` 1 . Việc quản lý , cấp phát , niên hạn sử dụng trang phục của cán bộ , thanh tra viên , công chức , viên chức thuộc các cơ quan thanh tra nhà nước được thực hiện theo quy định của văn bản liên tịch giữa Thanh tra Chính phủ và Bộ Tài chính . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 8 `[DIEU]`)


---

### Mẫu #02_2015_TT-TTCP_58849#body_standalone_73 (Loại: `body_standalone`)
> **[Điều 8]`<DIEU>`** . **[1 . Việc quản lý , cấp phát , niên hạn sử dụng trang phục của **[cán bộ]`<CHU_THE_CA_NHAN>`** , thanh tra viên , **[công chức]`<CHU_THE_CA_NHAN>`** , **[viên chức]`<CHU_THE_CA_NHAN>`** thuộc các cơ quan thanh tra nhà nước được thực hiện theo quy định của văn bản liên tịch giữa **[Thanh tra Chính phủ]`<CO_QUAN_THAM_QUYEN>`** và **[Bộ Tài chính]`<CO_QUAN_THAM_QUYEN>`** .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 8** → `DIEU` (span: `[0:2]`)
- `[e1]` **1 . Việc quản lý , cấp phát , niên hạn sử dụng trang phục của cán bộ , thanh tra viên , công chức , viên chức thuộc các cơ quan thanh tra nhà nước được thực hiện theo quy định của văn bản liên tịch giữa Thanh tra Chính phủ và Bộ Tài chính .** → `KHOAN` (span: `[3:41]`)
- `[e2]` **Thanh tra Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[35:37]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **Bộ Tài chính** → `CO_QUAN_THAM_QUYEN` (span: `[38:40]`) *(lồng trong `e1` (`KHOAN`))*
- `[e4]` **cán bộ** → `CHU_THE_CA_NHAN` (span: `[14:15]`) *(lồng trong `e1` (`KHOAN`))*
- `[e5]` **công chức** → `CHU_THE_CA_NHAN` (span: `[19:20]`) *(lồng trong `e1` (`KHOAN`))*
- `[e6]` **viên chức** → `CHU_THE_CA_NHAN` (span: `[21:22]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 1 . Việc quản lý , cấp phát , niên hạn sử dụng trang phục của cán bộ , thanh tra viên , công chức , viên chức thuộc các cơ quan thanh tra nhà nước được thực hiện theo quy định của văn bản liên tịch giữa Thanh tra Chính phủ và Bộ Tài chính . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 8 `[DIEU]`)


---

### Mẫu #02_2015_TT-TTCP_58849#body_context_74 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[02/2015/TT-TTCP]`<SO_HIEU>`** ban hành **[ngày 16 tháng 03 năm 2015]`<NGAY_BAN_HANH>`** bởi **[Thanh tra Chính phủ]`<CO_QUAN_BAN_HANH>`** . **[Điều 8]`<DIEU>`** . **[2 . Người được cấp trang phục để sử dụng khi thi hành công vụ , ngày lễ , ngày truyền thống ; có trách nhiệm giữ gìn , bảo quản trang phục theo quy định của Nhà nước ; nghiêm cấm **[sử dụng trang phục không đúng]`<HANH_VI_VI_PHAM>`** mục đích , để vụ lợi .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **02/2015/TT-TTCP** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Thanh tra Chính phủ** → `CO_QUAN_BAN_HANH` (span: `[11:13]`)
- `[e3]` **ngày 16 tháng 03 năm 2015** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 8** → `DIEU` (span: `[14:16]`)
- `[e5]` **2 . Người được cấp trang phục để sử dụng khi thi hành công vụ , ngày lễ , ngày truyền thống ; có trách nhiệm giữ gìn , bảo quản trang phục theo quy định của Nhà nước ; nghiêm cấm sử dụng trang phục không đúng mục đích , để vụ lợi .** → `KHOAN` (span: `[17:55]`)
- `[e6]` **sử dụng trang phục không đúng** → `HANH_VI_VI_PHAM` (span: `[46:50]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 02/2015/TT-TTCP `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Thanh tra Chính phủ `[CO_QUAN_BAN_HANH]`)
- (`e1` 02/2015/TT-TTCP `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 02/2015/TT-TTCP `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 16 tháng 03 năm 2015 `[NGAY_BAN_HANH]`)
- (`e4` Điều 8 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 02/2015/TT-TTCP `[SO_HIEU]`)
- (`e5` 2 . Người được cấp trang phục để sử dụng khi thi hành công vụ , ngày lễ , ngày truyền thống ; có trách nhiệm giữ gìn , bảo quản trang phục theo quy định của Nhà nước ; nghiêm cấm sử dụng trang phục không đúng mục đích , để vụ lợi . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 8 `[DIEU]`)


---

### Mẫu #02_2015_TT-TTCP_58849#body_context_75 (Loại: `body_context`)
> **[Thanh tra Chính phủ]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[02/2015/TT-TTCP]`<SO_HIEU>`** . **[Chương III. ĐIỀU KHOẢN THI HÀNH]`<CHUONG>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[3:4]`)
- `[e1]` **02/2015/TT-TTCP** → `SO_HIEU` (span: `[5:6]`)
- `[e2]` **Thanh tra Chính phủ** → `CO_QUAN_BAN_HANH` (span: `[0:2]`)
- `[e3]` **Chương III. ĐIỀU KHOẢN THI HÀNH** → `CHUONG` (span: `[7:11]`)

**Quan hệ:**
- (`e1` 02/2015/TT-TTCP `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Thanh tra Chính phủ `[CO_QUAN_BAN_HANH]`)
- (`e1` 02/2015/TT-TTCP `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Chương III. ĐIỀU KHOẢN THI HÀNH `[CHUONG]`) ==[ **THUOC_VE** ]==> (`e1` 02/2015/TT-TTCP `[SO_HIEU]`)


---

### Mẫu #02_2015_TT-TTCP_58849#body_context_76 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[02/2015/TT-TTCP]`<SO_HIEU>`** của **[Thanh tra Chính phủ]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Thanh tra]`<LINH_VUC>`** . **[Điều 9 . Hiệu lực thi hành . Thông tư này có hiệu lực thi hành từ ngày 04 tháng 5 năm 2015 và thay thế **[Thông tư số 03/2010/TT-TTCP]`<THAM_CHIEU_PHAP_LY>`** **[ngày 16 tháng 7 năm 2010]`<NGAY_THAM_CHIEU>`** của **[Thanh tra Chính phủ]`<CO_QUAN_THAM_QUYEN>`** hướng dẫn về màu sắc , chất liệu , quy cách và quản lý , sử dụng trang phục của thanh tra viên , **[cán bộ]`<CHU_THE_CA_NHAN>`** thuộc các cơ quan thanh tra nhà nước .]`<DIEU>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **02/2015/TT-TTCP** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Thanh tra Chính phủ** → `CO_QUAN_BAN_HANH` (span: `[4:6]`)
- `[e3]` **Thanh tra** → `LINH_VUC` (span: `[8:9]`)
- `[e4]` **Điều 9 . Hiệu lực thi hành . Thông tư này có hiệu lực thi hành từ ngày 04 tháng 5 năm 2015 và thay thế Thông tư số 03/2010/TT-TTCP ngày 16 tháng 7 năm 2010 của Thanh tra Chính phủ hướng dẫn về màu sắc , chất liệu , quy cách và quản lý , sử dụng trang phục của thanh tra viên , cán bộ thuộc các cơ quan thanh tra nhà nước .** → `DIEU` (span: `[10:65]`)
- `[e5]` **Thông tư số 03/2010/TT-TTCP** → `THAM_CHIEU_PHAP_LY` (span: `[30:33]`) *(lồng trong `e4` (`DIEU`))*
- `[e6]` **ngày 16 tháng 7 năm 2010** → `NGAY_THAM_CHIEU` (span: `[33:39]`) *(lồng trong `e4` (`DIEU`))*
- `[e7]` **Thanh tra Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[40:42]`) *(lồng trong `e4` (`DIEU`))*
- `[e8]` **cán bộ** → `CHU_THE_CA_NHAN` (span: `[58:59]`) *(lồng trong `e4` (`DIEU`))*

**Quan hệ:**
- (`e1` 02/2015/TT-TTCP `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Thanh tra Chính phủ `[CO_QUAN_BAN_HANH]`)
- (`e1` 02/2015/TT-TTCP `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 02/2015/TT-TTCP `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Thanh tra `[LINH_VUC]`)
- (`e4` Điều 9 . Hiệu lực thi hành . Thông tư này có hiệu lực thi hành từ ngày 04 tháng 5 năm 2015 và thay thế Thông tư số 03/2010/TT-TTCP ngày 16 tháng 7 năm 2010 của Thanh tra Chính phủ hướng dẫn về màu sắc , chất liệu , quy cách và quản lý , sử dụng trang phục của thanh tra viên , cán bộ thuộc các cơ quan thanh tra nhà nước . `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 02/2015/TT-TTCP `[SO_HIEU]`)
- (`e1` 02/2015/TT-TTCP `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Thanh tra `[LINH_VUC]`)
- (`e4` Điều 9 . Hiệu lực thi hành . Thông tư này có hiệu lực thi hành từ ngày 04 tháng 5 năm 2015 và thay thế Thông tư số 03/2010/TT-TTCP ngày 16 tháng 7 năm 2010 của Thanh tra Chính phủ hướng dẫn về màu sắc , chất liệu , quy cách và quản lý , sử dụng trang phục của thanh tra viên , cán bộ thuộc các cơ quan thanh tra nhà nước . `[DIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Thanh tra `[LINH_VUC]`)
- (`e4` Điều 9 . Hiệu lực thi hành . Thông tư này có hiệu lực thi hành từ ngày 04 tháng 5 năm 2015 và thay thế Thông tư số 03/2010/TT-TTCP ngày 16 tháng 7 năm 2010 của Thanh tra Chính phủ hướng dẫn về màu sắc , chất liệu , quy cách và quản lý , sử dụng trang phục của thanh tra viên , cán bộ thuộc các cơ quan thanh tra nhà nước . `[DIEU]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e5` Thông tư số 03/2010/TT-TTCP `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e5` Thông tư số 03/2010/TT-TTCP `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e6` ngày 16 tháng 7 năm 2010 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #02_2015_TT-TTCP_58849#body_standalone_77 (Loại: `body_standalone`)
> **[Điều 9 . Hiệu lực thi hành . Thông tư này có hiệu lực thi hành từ ngày 04 tháng 5 năm 2015 và thay thế **[Thông tư số 03/2010/TT-TTCP]`<THAM_CHIEU_PHAP_LY>`** **[ngày 16 tháng 7 năm 2010]`<NGAY_THAM_CHIEU>`** của **[Thanh tra Chính phủ]`<CO_QUAN_THAM_QUYEN>`** hướng dẫn về màu sắc , chất liệu , quy cách và quản lý , sử dụng trang phục của thanh tra viên , **[cán bộ]`<CHU_THE_CA_NHAN>`** thuộc các cơ quan thanh tra nhà nước .]`<DIEU>`**

**Thực thể:**
- `[e0]` **Điều 9 . Hiệu lực thi hành . Thông tư này có hiệu lực thi hành từ ngày 04 tháng 5 năm 2015 và thay thế Thông tư số 03/2010/TT-TTCP ngày 16 tháng 7 năm 2010 của Thanh tra Chính phủ hướng dẫn về màu sắc , chất liệu , quy cách và quản lý , sử dụng trang phục của thanh tra viên , cán bộ thuộc các cơ quan thanh tra nhà nước .** → `DIEU` (span: `[0:55]`)
- `[e1]` **Thông tư số 03/2010/TT-TTCP** → `THAM_CHIEU_PHAP_LY` (span: `[20:23]`) *(lồng trong `e0` (`DIEU`))*
- `[e2]` **ngày 16 tháng 7 năm 2010** → `NGAY_THAM_CHIEU` (span: `[23:29]`) *(lồng trong `e0` (`DIEU`))*
- `[e3]` **Thanh tra Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[30:32]`) *(lồng trong `e0` (`DIEU`))*
- `[e4]` **cán bộ** → `CHU_THE_CA_NHAN` (span: `[48:49]`) *(lồng trong `e0` (`DIEU`))*

**Quan hệ:**
- (`e0` Điều 9 . Hiệu lực thi hành . Thông tư này có hiệu lực thi hành từ ngày 04 tháng 5 năm 2015 và thay thế Thông tư số 03/2010/TT-TTCP ngày 16 tháng 7 năm 2010 của Thanh tra Chính phủ hướng dẫn về màu sắc , chất liệu , quy cách và quản lý , sử dụng trang phục của thanh tra viên , cán bộ thuộc các cơ quan thanh tra nhà nước . `[DIEU]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e1` Thông tư số 03/2010/TT-TTCP `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e1` Thông tư số 03/2010/TT-TTCP `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e2` ngày 16 tháng 7 năm 2010 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #02_2015_TT-TTCP_58849#body_context_78 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[02/2015/TT-TTCP]`<SO_HIEU>`** của **[Thanh tra Chính phủ]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Thanh tra]`<LINH_VUC>`** . **[Điều 10]`<DIEU>`** . **[1 . Vụ Tổ chức **[Cán bộ]`<CHU_THE_CA_NHAN>`** **[Thanh tra Chính phủ]`<CO_QUAN_THAM_QUYEN>`** làm đầu mối giúp Tổng **[Thanh tra Chính phủ]`<CO_QUAN_THAM_QUYEN>`** tổ chức thực hiện Thông tư này .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **02/2015/TT-TTCP** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Thanh tra Chính phủ** → `CO_QUAN_BAN_HANH` (span: `[4:6]`)
- `[e3]` **Thanh tra** → `LINH_VUC` (span: `[8:9]`)
- `[e4]` **Điều 10** → `DIEU` (span: `[10:12]`)
- `[e5]` **1 . Vụ Tổ chức Cán bộ Thanh tra Chính phủ làm đầu mối giúp Tổng Thanh tra Chính phủ tổ chức thực hiện Thông tư này .** → `KHOAN` (span: `[13:31]`)
- `[e6]` **Thanh tra Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[18:20]`) *(lồng trong `e5` (`KHOAN`))*
- `[e7]` **Thanh tra Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[24:26]`) *(lồng trong `e5` (`KHOAN`))*
- `[e8]` **Cán bộ** → `CHU_THE_CA_NHAN` (span: `[17:18]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 02/2015/TT-TTCP `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Thanh tra Chính phủ `[CO_QUAN_BAN_HANH]`)
- (`e1` 02/2015/TT-TTCP `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 02/2015/TT-TTCP `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Thanh tra `[LINH_VUC]`)
- (`e4` Điều 10 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 02/2015/TT-TTCP `[SO_HIEU]`)
- (`e5` 1 . Vụ Tổ chức Cán bộ Thanh tra Chính phủ làm đầu mối giúp Tổng Thanh tra Chính phủ tổ chức thực hiện Thông tư này . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 10 `[DIEU]`)
- (`e1` 02/2015/TT-TTCP `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Thanh tra `[LINH_VUC]`)
- (`e5` 1 . Vụ Tổ chức Cán bộ Thanh tra Chính phủ làm đầu mối giúp Tổng Thanh tra Chính phủ tổ chức thực hiện Thông tư này . `[KHOAN]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Thanh tra `[LINH_VUC]`)


---

### Mẫu #02_2015_TT-TTCP_58849#body_standalone_79 (Loại: `body_standalone`)
> **[Điều 10]`<DIEU>`** . **[1 . Vụ Tổ chức **[Cán bộ]`<CHU_THE_CA_NHAN>`** **[Thanh tra Chính phủ]`<CO_QUAN_THAM_QUYEN>`** làm đầu mối giúp Tổng **[Thanh tra Chính phủ]`<CO_QUAN_THAM_QUYEN>`** tổ chức thực hiện Thông tư này .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 10** → `DIEU` (span: `[0:2]`)
- `[e1]` **1 . Vụ Tổ chức Cán bộ Thanh tra Chính phủ làm đầu mối giúp Tổng Thanh tra Chính phủ tổ chức thực hiện Thông tư này .** → `KHOAN` (span: `[3:21]`)
- `[e2]` **Thanh tra Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[8:10]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **Thanh tra Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[14:16]`) *(lồng trong `e1` (`KHOAN`))*
- `[e4]` **Cán bộ** → `CHU_THE_CA_NHAN` (span: `[7:8]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 1 . Vụ Tổ chức Cán bộ Thanh tra Chính phủ làm đầu mối giúp Tổng Thanh tra Chính phủ tổ chức thực hiện Thông tư này . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 10 `[DIEU]`)


---

### Mẫu #02_2015_TT-TTCP_58849#body_context_80 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[02/2015/TT-TTCP]`<SO_HIEU>`** của **[Thanh tra Chính phủ]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Thanh tra]`<LINH_VUC>`** . **[Điều 10]`<DIEU>`** . **[2 . Bộ trưởng , Thủ trưởng cơ quan ngang Bộ , **[Chủ tịch Ủy ban nhân dân tỉnh , thành phố trực thuộc Trung ương]`<CO_QUAN_THAM_QUYEN>`** có trách nhiệm triển khai , thực hiện các quy định về trang phục đối với thanh tra viên , **[công chức]`<CHU_THE_CA_NHAN>`** , **[viên chức]`<CHU_THE_CA_NHAN>`** của cơ quan thanh tra nhà nước trong thẩm quyền quản lý .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **02/2015/TT-TTCP** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Thanh tra Chính phủ** → `CO_QUAN_BAN_HANH` (span: `[4:6]`)
- `[e3]` **Thanh tra** → `LINH_VUC` (span: `[8:9]`)
- `[e4]` **Điều 10** → `DIEU` (span: `[10:12]`)
- `[e5]` **2 . Bộ trưởng , Thủ trưởng cơ quan ngang Bộ , Chủ tịch Ủy ban nhân dân tỉnh , thành phố trực thuộc Trung ương có trách nhiệm triển khai , thực hiện các quy định về trang phục đối với thanh tra viên , công chức , viên chức của cơ quan thanh tra nhà nước trong thẩm quyền quản lý .** → `KHOAN` (span: `[13:54]`)
- `[e6]` **Chủ tịch Ủy ban nhân dân tỉnh , thành phố trực thuộc Trung ương** → `CO_QUAN_THAM_QUYEN` (span: `[22:30]`) *(lồng trong `e5` (`KHOAN`))*
- `[e7]` **công chức** → `CHU_THE_CA_NHAN` (span: `[43:44]`) *(lồng trong `e5` (`KHOAN`))*
- `[e8]` **viên chức** → `CHU_THE_CA_NHAN` (span: `[45:46]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 02/2015/TT-TTCP `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Thanh tra Chính phủ `[CO_QUAN_BAN_HANH]`)
- (`e1` 02/2015/TT-TTCP `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 02/2015/TT-TTCP `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Thanh tra `[LINH_VUC]`)
- (`e4` Điều 10 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 02/2015/TT-TTCP `[SO_HIEU]`)
- (`e5` 2 . Bộ trưởng , Thủ trưởng cơ quan ngang Bộ , Chủ tịch Ủy ban nhân dân tỉnh , thành phố trực thuộc Trung ương có trách nhiệm triển khai , thực hiện các quy định về trang phục đối với thanh tra viên , công chức , viên chức của cơ quan thanh tra nhà nước trong thẩm quyền quản lý . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 10 `[DIEU]`)
- (`e1` 02/2015/TT-TTCP `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Thanh tra `[LINH_VUC]`)
- (`e5` 2 . Bộ trưởng , Thủ trưởng cơ quan ngang Bộ , Chủ tịch Ủy ban nhân dân tỉnh , thành phố trực thuộc Trung ương có trách nhiệm triển khai , thực hiện các quy định về trang phục đối với thanh tra viên , công chức , viên chức của cơ quan thanh tra nhà nước trong thẩm quyền quản lý . `[KHOAN]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Thanh tra `[LINH_VUC]`)


---

### Mẫu #02_2015_TT-TTCP_58849#body_standalone_81 (Loại: `body_standalone`)
> **[Điều 10]`<DIEU>`** . **[2 . Bộ trưởng , Thủ trưởng cơ quan ngang Bộ , **[Chủ tịch Ủy ban nhân dân tỉnh , thành phố trực thuộc Trung ương]`<CO_QUAN_THAM_QUYEN>`** có trách nhiệm triển khai , thực hiện các quy định về trang phục đối với thanh tra viên , **[công chức]`<CHU_THE_CA_NHAN>`** , **[viên chức]`<CHU_THE_CA_NHAN>`** của cơ quan thanh tra nhà nước trong thẩm quyền quản lý .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 10** → `DIEU` (span: `[0:2]`)
- `[e1]` **2 . Bộ trưởng , Thủ trưởng cơ quan ngang Bộ , Chủ tịch Ủy ban nhân dân tỉnh , thành phố trực thuộc Trung ương có trách nhiệm triển khai , thực hiện các quy định về trang phục đối với thanh tra viên , công chức , viên chức của cơ quan thanh tra nhà nước trong thẩm quyền quản lý .** → `KHOAN` (span: `[3:44]`)
- `[e2]` **Chủ tịch Ủy ban nhân dân tỉnh , thành phố trực thuộc Trung ương** → `CO_QUAN_THAM_QUYEN` (span: `[12:20]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **công chức** → `CHU_THE_CA_NHAN` (span: `[33:34]`) *(lồng trong `e1` (`KHOAN`))*
- `[e4]` **viên chức** → `CHU_THE_CA_NHAN` (span: `[35:36]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 2 . Bộ trưởng , Thủ trưởng cơ quan ngang Bộ , Chủ tịch Ủy ban nhân dân tỉnh , thành phố trực thuộc Trung ương có trách nhiệm triển khai , thực hiện các quy định về trang phục đối với thanh tra viên , công chức , viên chức của cơ quan thanh tra nhà nước trong thẩm quyền quản lý . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 10 `[DIEU]`)


---

### Mẫu #02_2015_TT-TTCP_58849#body_context_82 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[02/2015/TT-TTCP]`<SO_HIEU>`** ban hành **[ngày 16 tháng 03 năm 2015]`<NGAY_BAN_HANH>`** bởi **[Thanh tra Chính phủ]`<CO_QUAN_BAN_HANH>`** . **[Điều 10]`<DIEU>`** . **[3 . Trong quá trình thực hiện , nếu có các vấn đề phát sinh hoặc khó khăn , vướng mắc , đề nghị các cơ quan , tổ chức , đơn vị , cá nhân phản ánh kịp thời về **[thanh tra Chính phủ]`<CO_QUAN_THAM_QUYEN>`** để nghiên cứu , sửa đổi , bổ sung cho phù hợp . / .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **02/2015/TT-TTCP** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Thanh tra Chính phủ** → `CO_QUAN_BAN_HANH` (span: `[11:13]`)
- `[e3]` **ngày 16 tháng 03 năm 2015** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 10** → `DIEU` (span: `[14:16]`)
- `[e5]` **3 . Trong quá trình thực hiện , nếu có các vấn đề phát sinh hoặc khó khăn , vướng mắc , đề nghị các cơ quan , tổ chức , đơn vị , cá nhân phản ánh kịp thời về thanh tra Chính phủ để nghiên cứu , sửa đổi , bổ sung cho phù hợp . / .** → `KHOAN` (span: `[17:58]`)
- `[e6]` **thanh tra Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[45:47]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 02/2015/TT-TTCP `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Thanh tra Chính phủ `[CO_QUAN_BAN_HANH]`)
- (`e1` 02/2015/TT-TTCP `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 02/2015/TT-TTCP `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 16 tháng 03 năm 2015 `[NGAY_BAN_HANH]`)
- (`e4` Điều 10 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 02/2015/TT-TTCP `[SO_HIEU]`)
- (`e5` 3 . Trong quá trình thực hiện , nếu có các vấn đề phát sinh hoặc khó khăn , vướng mắc , đề nghị các cơ quan , tổ chức , đơn vị , cá nhân phản ánh kịp thời về thanh tra Chính phủ để nghiên cứu , sửa đổi , bổ sung cho phù hợp . / . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 10 `[DIEU]`)


---

### Mẫu #02_2015_TT-TTCP_58849#body_context_83 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[02/2015/TT-TTCP]`<SO_HIEU>`** ban hành **[ngày 16 tháng 03 năm 2015]`<NGAY_BAN_HANH>`** bởi **[Thanh tra Chính phủ]`<CO_QUAN_BAN_HANH>`** . **[Điều 4]`<DIEU>`** . **[Khoản 1 . Áo măng tô]`<KHOAN>`** : **[b ) Màu sắc : xanh rêu đậm .]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **02/2015/TT-TTCP** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Thanh tra Chính phủ** → `CO_QUAN_BAN_HANH` (span: `[11:13]`)
- `[e3]` **ngày 16 tháng 03 năm 2015** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 4** → `DIEU` (span: `[14:16]`)
- `[e5]` **Khoản 1 . Áo măng tô** → `KHOAN` (span: `[17:22]`)
- `[e6]` **b ) Màu sắc : xanh rêu đậm .** → `DIEM` (span: `[23:31]`)

**Quan hệ:**
- (`e1` 02/2015/TT-TTCP `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Thanh tra Chính phủ `[CO_QUAN_BAN_HANH]`)
- (`e1` 02/2015/TT-TTCP `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 02/2015/TT-TTCP `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 16 tháng 03 năm 2015 `[NGAY_BAN_HANH]`)
- (`e4` Điều 4 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 02/2015/TT-TTCP `[SO_HIEU]`)
- (`e5` Khoản 1 . Áo măng tô `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 4 `[DIEU]`)
- (`e6` b ) Màu sắc : xanh rêu đậm . `[DIEM]`) ==[ **THUOC_VE** ]==> (`e5` Khoản 1 . Áo măng tô `[KHOAN]`)


---

### Mẫu #02_2015_TT-TTCP_58849#body_standalone_84 (Loại: `body_standalone`)
> **[Điều 4]`<DIEU>`** . **[Khoản 1 . Áo măng tô]`<KHOAN>`** : **[b ) Màu sắc : xanh rêu đậm .]`<DIEM>`**

**Thực thể:**
- `[e0]` **Điều 4** → `DIEU` (span: `[0:2]`)
- `[e1]` **Khoản 1 . Áo măng tô** → `KHOAN` (span: `[3:8]`)
- `[e2]` **b ) Màu sắc : xanh rêu đậm .** → `DIEM` (span: `[9:17]`)

**Quan hệ:**
- (`e1` Khoản 1 . Áo măng tô `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 4 `[DIEU]`)
- (`e2` b ) Màu sắc : xanh rêu đậm . `[DIEM]`) ==[ **THUOC_VE** ]==> (`e1` Khoản 1 . Áo măng tô `[KHOAN]`)


---

### Mẫu #02_2015_TT-TTCP_58849#body_context_85 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[02/2015/TT-TTCP]`<SO_HIEU>`** của **[Thanh tra Chính phủ]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Thanh tra]`<LINH_VUC>`** . **[Điều 4]`<DIEU>`** . **[8 . Dép quai hậu]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **02/2015/TT-TTCP** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Thanh tra Chính phủ** → `CO_QUAN_BAN_HANH` (span: `[4:6]`)
- `[e3]` **Thanh tra** → `LINH_VUC` (span: `[8:9]`)
- `[e4]` **Điều 4** → `DIEU` (span: `[10:12]`)
- `[e5]` **8 . Dép quai hậu** → `KHOAN` (span: `[13:17]`)

**Quan hệ:**
- (`e1` 02/2015/TT-TTCP `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Thanh tra Chính phủ `[CO_QUAN_BAN_HANH]`)
- (`e1` 02/2015/TT-TTCP `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 02/2015/TT-TTCP `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Thanh tra `[LINH_VUC]`)
- (`e4` Điều 4 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 02/2015/TT-TTCP `[SO_HIEU]`)
- (`e5` 8 . Dép quai hậu `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 4 `[DIEU]`)
- (`e1` 02/2015/TT-TTCP `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Thanh tra `[LINH_VUC]`)
- (`e5` 8 . Dép quai hậu `[KHOAN]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Thanh tra `[LINH_VUC]`)


---

### Mẫu #02_2015_TT-TTCP_58849#body_context_86 (Loại: `body_context`)
> **[Thanh tra Chính phủ]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[02/2015/TT-TTCP]`<SO_HIEU>`** . **[Điều 5]`<DIEU>`** . **[Khoản 5 . Áo sơmi dài tay]`<KHOAN>`** : **[b ) Màu sắc : xanh nhạt .]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[3:4]`)
- `[e1]` **02/2015/TT-TTCP** → `SO_HIEU` (span: `[5:6]`)
- `[e2]` **Thanh tra Chính phủ** → `CO_QUAN_BAN_HANH` (span: `[0:2]`)
- `[e3]` **Điều 5** → `DIEU` (span: `[7:9]`)
- `[e4]` **Khoản 5 . Áo sơmi dài tay** → `KHOAN` (span: `[10:17]`)
- `[e5]` **b ) Màu sắc : xanh nhạt .** → `DIEM` (span: `[18:25]`)

**Quan hệ:**
- (`e1` 02/2015/TT-TTCP `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Thanh tra Chính phủ `[CO_QUAN_BAN_HANH]`)
- (`e1` 02/2015/TT-TTCP `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 5 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 02/2015/TT-TTCP `[SO_HIEU]`)
- (`e4` Khoản 5 . Áo sơmi dài tay `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 5 `[DIEU]`)
- (`e5` b ) Màu sắc : xanh nhạt . `[DIEM]`) ==[ **THUOC_VE** ]==> (`e4` Khoản 5 . Áo sơmi dài tay `[KHOAN]`)


---

### Mẫu #02_2015_TT-TTCP_58849#body_context_87 (Loại: `body_context`)
> **[Thanh tra Chính phủ]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[02/2015/TT-TTCP]`<SO_HIEU>`** . **[Điều 6]`<DIEU>`** . **[Khoản 2]`<KHOAN>`** . **[b ) Màu sắc : xanh rêu đậm .]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[3:4]`)
- `[e1]` **02/2015/TT-TTCP** → `SO_HIEU` (span: `[5:6]`)
- `[e2]` **Thanh tra Chính phủ** → `CO_QUAN_BAN_HANH` (span: `[0:2]`)
- `[e3]` **Điều 6** → `DIEU` (span: `[7:9]`)
- `[e4]` **Khoản 2** → `KHOAN` (span: `[10:12]`)
- `[e5]` **b ) Màu sắc : xanh rêu đậm .** → `DIEM` (span: `[13:21]`)

**Quan hệ:**
- (`e1` 02/2015/TT-TTCP `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Thanh tra Chính phủ `[CO_QUAN_BAN_HANH]`)
- (`e1` 02/2015/TT-TTCP `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 6 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 02/2015/TT-TTCP `[SO_HIEU]`)
- (`e4` Khoản 2 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 6 `[DIEU]`)
- (`e5` b ) Màu sắc : xanh rêu đậm . `[DIEM]`) ==[ **THUOC_VE** ]==> (`e4` Khoản 2 `[KHOAN]`)


---

### Mẫu #02_2015_TT-TTCP_58849#body_context_88 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[02/2015/TT-TTCP]`<SO_HIEU>`** ban hành **[ngày 16 tháng 03 năm 2015]`<NGAY_BAN_HANH>`** bởi **[Thanh tra Chính phủ]`<CO_QUAN_BAN_HANH>`** . **[Điều 6]`<DIEU>`** . **[8 . Cúc cấp hiệu]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **02/2015/TT-TTCP** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Thanh tra Chính phủ** → `CO_QUAN_BAN_HANH` (span: `[11:13]`)
- `[e3]` **ngày 16 tháng 03 năm 2015** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 6** → `DIEU` (span: `[14:16]`)
- `[e5]` **8 . Cúc cấp hiệu** → `KHOAN` (span: `[17:21]`)

**Quan hệ:**
- (`e1` 02/2015/TT-TTCP `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Thanh tra Chính phủ `[CO_QUAN_BAN_HANH]`)
- (`e1` 02/2015/TT-TTCP `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 02/2015/TT-TTCP `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 16 tháng 03 năm 2015 `[NGAY_BAN_HANH]`)
- (`e4` Điều 6 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 02/2015/TT-TTCP `[SO_HIEU]`)
- (`e5` 8 . Cúc cấp hiệu `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 6 `[DIEU]`)


---

### Mẫu #02_2015_TT-TTCP_58849#body_context_89 (Loại: `body_context`)
> **[Thanh tra Chính phủ]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[02/2015/TT-TTCP]`<SO_HIEU>`** . **[Điều 6]`<DIEU>`** . **[12 . **[Mũ bảo hiểm]`<TAI_SAN_VAT_CHAT>`**]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[3:4]`)
- `[e1]` **02/2015/TT-TTCP** → `SO_HIEU` (span: `[5:6]`)
- `[e2]` **Thanh tra Chính phủ** → `CO_QUAN_BAN_HANH` (span: `[0:2]`)
- `[e3]` **Điều 6** → `DIEU` (span: `[7:9]`)
- `[e4]` **12 . Mũ bảo hiểm** → `KHOAN` (span: `[10:13]`)
- `[e5]` **Mũ bảo hiểm** → `TAI_SAN_VAT_CHAT` (span: `[12:13]`) *(lồng trong `e4` (`KHOAN`))*

**Quan hệ:**
- (`e1` 02/2015/TT-TTCP `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Thanh tra Chính phủ `[CO_QUAN_BAN_HANH]`)
- (`e1` 02/2015/TT-TTCP `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 6 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 02/2015/TT-TTCP `[SO_HIEU]`)
- (`e4` 12 . Mũ bảo hiểm `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 6 `[DIEU]`)


---

### Mẫu #02_2015_TT-TTCP_58849#body_standalone_90 (Loại: `body_standalone`)
> **[Điều 6]`<DIEU>`** . **[12 . **[Mũ bảo hiểm]`<TAI_SAN_VAT_CHAT>`**]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 6** → `DIEU` (span: `[0:2]`)
- `[e1]` **12 . Mũ bảo hiểm** → `KHOAN` (span: `[3:6]`)
- `[e2]` **Mũ bảo hiểm** → `TAI_SAN_VAT_CHAT` (span: `[5:6]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 12 . Mũ bảo hiểm `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 6 `[DIEU]`)


---
