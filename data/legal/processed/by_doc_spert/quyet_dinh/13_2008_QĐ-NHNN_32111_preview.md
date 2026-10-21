# Dữ liệu gán nhãn văn bản: 13_2008_QĐ-NHNN_32111
- **Thể loại**: `quyet_dinh`
- **Phân vùng dữ liệu**: `TRAIN`
- **Tổng số mẫu**: 123 mẫu
- **Tổng số thực thể**: 1171
- **Tổng số quan hệ**: 590

---

### Mẫu #13_2008_QĐ-NHNN_32111#header_0 (Loại: `header`)
> **[NGÂN HÀNG NHÀ NƯỚC VIỆT NAM]`<CO_QUAN_BAN_HANH>`** . CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM . Độc lập – Tự do – Hạnh phúc . Số : **[13/2008/QĐ-NHNN]`<SO_HIEU>`** . **[Ngày 29 tháng 4 năm 2008]`<NGAY_BAN_HANH>`** . **[QUYẾT ĐỊNH]`<LOAI_VAN_BAN>`**

**Thực thể:**
- `[e0]` **13/2008/QĐ-NHNN** → `SO_HIEU` (span: `[19:20]`)
- `[e1]` **Ngày 29 tháng 4 năm 2008** → `NGAY_BAN_HANH` (span: `[21:27]`)
- `[e2]` **NGÂN HÀNG NHÀ NƯỚC VIỆT NAM** → `CO_QUAN_BAN_HANH` (span: `[0:3]`)
- `[e3]` **QUYẾT ĐỊNH** → `LOAI_VAN_BAN` (span: `[28:29]`)

**Quan hệ:**
- (`e0` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` NGÂN HÀNG NHÀ NƯỚC VIỆT NAM `[CO_QUAN_BAN_HANH]`)
- (`e0` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e1` Ngày 29 tháng 4 năm 2008 `[NGAY_BAN_HANH]`)
- (`e0` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e3` QUYẾT ĐỊNH `[LOAI_VAN_BAN]`)


---

### Mẫu #13_2008_QĐ-NHNN_32111#signature_1 (Loại: `signature`)
> KT. THỐNG ĐỐC **[PHÓ THỐNG ĐỐC]`<CHUC_DANH_NGUOI_KY>`** . ( Đã ký ) . **[Trần Minh Tuấn]`<NGUOI_KY>`**

**Thực thể:**
- `[e0]` **Trần Minh Tuấn** → `NGUOI_KY` (span: `[10:11]`)
- `[e1]` **PHÓ THỐNG ĐỐC** → `CHUC_DANH_NGUOI_KY` (span: `[2:4]`)

**Quan hệ:**
- (`e0` Trần Minh Tuấn `[NGUOI_KY]`) ==[ **GIU_CHUC_VU** ]==> (`e1` PHÓ THỐNG ĐỐC `[CHUC_DANH_NGUOI_KY]`)


---

### Mẫu #13_2008_QĐ-NHNN_32111#meta_2 (Loại: `meta`)
> **[NGÂN HÀNG NHÀ NƯỚC VIỆT NAM]`<CO_QUAN_BAN_HANH>`** . CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM . Độc lập – Tự do – Hạnh phúc . Số : **[13/2008/QĐ-NHNN]`<SO_HIEU>`** . Ngày 29 tháng 4 năm 2008 . **[QUYẾT ĐỊNH]`<LOAI_VAN_BAN>`** . KT. THỐNG ĐỐC **[PHÓ THỐNG ĐỐC]`<CHUC_DANH_NGUOI_KY>`** . ( Đã ký ) . **[Trần Minh Tuấn]`<NGUOI_KY>`**

**Thực thể:**
- `[e0]` **13/2008/QĐ-NHNN** → `SO_HIEU` (span: `[19:20]`)
- `[e1]` **NGÂN HÀNG NHÀ NƯỚC VIỆT NAM** → `CO_QUAN_BAN_HANH` (span: `[0:3]`)
- `[e2]` **QUYẾT ĐỊNH** → `LOAI_VAN_BAN` (span: `[28:29]`)
- `[e3]` **Trần Minh Tuấn** → `NGUOI_KY` (span: `[40:41]`)
- `[e4]` **PHÓ THỐNG ĐỐC** → `CHUC_DANH_NGUOI_KY` (span: `[32:34]`)

**Quan hệ:**
- (`e0` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e1` NGÂN HÀNG NHÀ NƯỚC VIỆT NAM `[CO_QUAN_BAN_HANH]`)
- (`e0` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e2` QUYẾT ĐỊNH `[LOAI_VAN_BAN]`)
- (`e0` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **KY_BOI** ]==> (`e3` Trần Minh Tuấn `[NGUOI_KY]`)
- (`e3` Trần Minh Tuấn `[NGUOI_KY]`) ==[ **GIU_CHUC_VU** ]==> (`e4` PHÓ THỐNG ĐỐC `[CHUC_DANH_NGUOI_KY]`)


---

### Mẫu #13_2008_QĐ-NHNN_32111#preamble_context_3 (Loại: `preamble_context`)
> **[Quyết định]`<LOAI_VAN_BAN>`** số **[13/2008/QĐ-NHNN]`<SO_HIEU>`** của **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_BAN_HANH>`** . Ban hành Quy định về mạng lưới hoạt động của **[ngân hàng thương mại]`<TO_CHUC_DOANH_NGHIEP>`**

**Thực thể:**
- `[e0]` **Quyết định** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **13/2008/QĐ-NHNN** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_BAN_HANH` (span: `[4:7]`)
- `[e3]` **ngân hàng thương mại** → `TO_CHUC_DOANH_NGHIEP` (span: `[14:16]`)

**Quan hệ:**
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Ngân hàng Nhà nước Việt Nam `[CO_QUAN_BAN_HANH]`)
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Quyết định `[LOAI_VAN_BAN]`)


---

### Mẫu #13_2008_QĐ-NHNN_32111#preamble_standalone_4 (Loại: `preamble_standalone`)
> Ban hành Quy định về mạng lưới hoạt động của **[ngân hàng thương mại]`<TO_CHUC_DOANH_NGHIEP>`**

**Thực thể:**
- `[e0]` **ngân hàng thương mại** → `TO_CHUC_DOANH_NGHIEP` (span: `[6:8]`)


---

### Mẫu #13_2008_QĐ-NHNN_32111#preamble_context_5 (Loại: `preamble_context`)
> **[Quyết định]`<LOAI_VAN_BAN>`** số **[13/2008/QĐ-NHNN]`<SO_HIEU>`** của **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_BAN_HANH>`** . **[THỐNG ĐỐC NGÂN HÀNG NHÀ NƯỚC]`<CO_QUAN_THAM_QUYEN>`**

**Thực thể:**
- `[e0]` **Quyết định** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **13/2008/QĐ-NHNN** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_BAN_HANH` (span: `[4:7]`)
- `[e3]` **THỐNG ĐỐC NGÂN HÀNG NHÀ NƯỚC** → `CO_QUAN_THAM_QUYEN` (span: `[8:11]`)

**Quan hệ:**
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Ngân hàng Nhà nước Việt Nam `[CO_QUAN_BAN_HANH]`)
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Quyết định `[LOAI_VAN_BAN]`)


---

### Mẫu #13_2008_QĐ-NHNN_32111#preamble_standalone_6 (Loại: `preamble_standalone`)
> **[THỐNG ĐỐC NGÂN HÀNG NHÀ NƯỚC]`<CO_QUAN_THAM_QUYEN>`**

**Thực thể:**
- `[e0]` **THỐNG ĐỐC NGÂN HÀNG NHÀ NƯỚC** → `CO_QUAN_THAM_QUYEN` (span: `[0:3]`)


---

### Mẫu #13_2008_QĐ-NHNN_32111#preamble_context_7 (Loại: `preamble_context`)
> **[Quyết định]`<LOAI_VAN_BAN>`** số **[13/2008/QĐ-NHNN]`<SO_HIEU>`** của **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_BAN_HANH>`** . **[Căn cứ]`<TU_KHOA_PHAP_LY>`** **[Luật Ngân hàng Nhà nước Việt Nam năm 1997]`<THAM_CHIEU_PHAP_LY>`** , Luật **[sửa đổi , bổ sung một số điều của]`<TU_KHOA_PHAP_LY>`** Luật **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_THAM_QUYEN>`** năm 2003 ;

**Thực thể:**
- `[e0]` **Quyết định** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **13/2008/QĐ-NHNN** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_BAN_HANH` (span: `[4:7]`)
- `[e3]` **Luật Ngân hàng Nhà nước Việt Nam năm 1997** → `THAM_CHIEU_PHAP_LY` (span: `[9:15]`)
- `[e4]` **Căn cứ** → `TU_KHOA_PHAP_LY` (span: `[8:9]`)
- `[e5]` **sửa đổi , bổ sung một số điều của** → `TU_KHOA_PHAP_LY` (span: `[17:23]`)
- `[e6]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_THAM_QUYEN` (span: `[24:27]`)

**Quan hệ:**
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Ngân hàng Nhà nước Việt Nam `[CO_QUAN_BAN_HANH]`)
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Quyết định `[LOAI_VAN_BAN]`)
- (`e4` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Luật Ngân hàng Nhà nước Việt Nam năm 1997 `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Luật Ngân hàng Nhà nước Việt Nam năm 1997 `[THAM_CHIEU_PHAP_LY]`)


---

### Mẫu #13_2008_QĐ-NHNN_32111#preamble_standalone_8 (Loại: `preamble_standalone`)
> **[Căn cứ]`<TU_KHOA_PHAP_LY>`** **[Luật Ngân hàng Nhà nước Việt Nam năm 1997]`<THAM_CHIEU_PHAP_LY>`** , Luật **[sửa đổi , bổ sung một số điều của]`<TU_KHOA_PHAP_LY>`** Luật **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_THAM_QUYEN>`** năm 2003 ;

**Thực thể:**
- `[e0]` **Luật Ngân hàng Nhà nước Việt Nam năm 1997** → `THAM_CHIEU_PHAP_LY` (span: `[1:7]`)
- `[e1]` **Căn cứ** → `TU_KHOA_PHAP_LY` (span: `[0:1]`)
- `[e2]` **sửa đổi , bổ sung một số điều của** → `TU_KHOA_PHAP_LY` (span: `[9:15]`)
- `[e3]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_THAM_QUYEN` (span: `[16:19]`)

**Quan hệ:**
- (`e1` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e0` Luật Ngân hàng Nhà nước Việt Nam năm 1997 `[THAM_CHIEU_PHAP_LY]`)
- (`e3` Ngân hàng Nhà nước Việt Nam `[CO_QUAN_THAM_QUYEN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e0` Luật Ngân hàng Nhà nước Việt Nam năm 1997 `[THAM_CHIEU_PHAP_LY]`)


---

### Mẫu #13_2008_QĐ-NHNN_32111#preamble_context_9 (Loại: `preamble_context`)
> **[Quyết định]`<LOAI_VAN_BAN>`** số **[13/2008/QĐ-NHNN]`<SO_HIEU>`** của **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_BAN_HANH>`** . **[Căn cứ]`<TU_KHOA_PHAP_LY>`** **[Luật các tổ chức tín dụng năm 1997]`<THAM_CHIEU_PHAP_LY>`** , Luật **[sửa đổi , bổ sung một số điều của]`<TU_KHOA_PHAP_LY>`** Luật các **[tổ chức tín dụng năm 2004]`<TO_CHUC_DOANH_NGHIEP>`** ;

**Thực thể:**
- `[e0]` **Quyết định** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **13/2008/QĐ-NHNN** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_BAN_HANH` (span: `[4:7]`)
- `[e3]` **Luật các tổ chức tín dụng năm 1997** → `THAM_CHIEU_PHAP_LY` (span: `[9:15]`)
- `[e4]` **Căn cứ** → `TU_KHOA_PHAP_LY` (span: `[8:9]`)
- `[e5]` **sửa đổi , bổ sung một số điều của** → `TU_KHOA_PHAP_LY` (span: `[17:23]`)
- `[e6]` **tổ chức tín dụng năm 2004** → `TO_CHUC_DOANH_NGHIEP` (span: `[25:29]`)

**Quan hệ:**
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Ngân hàng Nhà nước Việt Nam `[CO_QUAN_BAN_HANH]`)
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Quyết định `[LOAI_VAN_BAN]`)
- (`e4` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Luật các tổ chức tín dụng năm 1997 `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Luật các tổ chức tín dụng năm 1997 `[THAM_CHIEU_PHAP_LY]`)


---

### Mẫu #13_2008_QĐ-NHNN_32111#preamble_standalone_10 (Loại: `preamble_standalone`)
> **[Căn cứ]`<TU_KHOA_PHAP_LY>`** **[Luật các tổ chức tín dụng năm 1997]`<THAM_CHIEU_PHAP_LY>`** , Luật **[sửa đổi , bổ sung một số điều của]`<TU_KHOA_PHAP_LY>`** Luật các **[tổ chức tín dụng năm 2004]`<TO_CHUC_DOANH_NGHIEP>`** ;

**Thực thể:**
- `[e0]` **Luật các tổ chức tín dụng năm 1997** → `THAM_CHIEU_PHAP_LY` (span: `[1:7]`)
- `[e1]` **Căn cứ** → `TU_KHOA_PHAP_LY` (span: `[0:1]`)
- `[e2]` **sửa đổi , bổ sung một số điều của** → `TU_KHOA_PHAP_LY` (span: `[9:15]`)
- `[e3]` **tổ chức tín dụng năm 2004** → `TO_CHUC_DOANH_NGHIEP` (span: `[17:21]`)

**Quan hệ:**
- (`e1` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e0` Luật các tổ chức tín dụng năm 1997 `[THAM_CHIEU_PHAP_LY]`)
- (`e3` tổ chức tín dụng năm 2004 `[TO_CHUC_DOANH_NGHIEP]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e0` Luật các tổ chức tín dụng năm 1997 `[THAM_CHIEU_PHAP_LY]`)


---

### Mẫu #13_2008_QĐ-NHNN_32111#preamble_context_11 (Loại: `preamble_context`)
> **[Quyết định]`<LOAI_VAN_BAN>`** số **[13/2008/QĐ-NHNN]`<SO_HIEU>`** của **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_BAN_HANH>`** . **[Căn cứ]`<TU_KHOA_PHAP_LY>`** **[Nghị định số 52/2003/NĐ-CP]`<THAM_CHIEU_PHAP_LY>`** **[ngày 19/5/2003]`<NGAY_THAM_CHIEU>`** của **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** quy định chức năng , nhiệm vụ , quyền hạn và cơ cấu tổ chức của **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_THAM_QUYEN>`** ;

**Thực thể:**
- `[e0]` **Quyết định** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **13/2008/QĐ-NHNN** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_BAN_HANH` (span: `[4:7]`)
- `[e3]` **Nghị định số 52/2003/NĐ-CP** → `THAM_CHIEU_PHAP_LY` (span: `[9:12]`)
- `[e4]` **Căn cứ** → `TU_KHOA_PHAP_LY` (span: `[8:9]`)
- `[e5]` **ngày 19/5/2003** → `NGAY_THAM_CHIEU` (span: `[12:14]`)
- `[e6]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[15:16]`)
- `[e7]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_THAM_QUYEN` (span: `[26:29]`)

**Quan hệ:**
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Ngân hàng Nhà nước Việt Nam `[CO_QUAN_BAN_HANH]`)
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Quyết định `[LOAI_VAN_BAN]`)
- (`e4` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Nghị định số 52/2003/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Nghị định số 52/2003/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e3` Nghị định số 52/2003/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e5` ngày 19/5/2003 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #13_2008_QĐ-NHNN_32111#preamble_standalone_12 (Loại: `preamble_standalone`)
> **[Căn cứ]`<TU_KHOA_PHAP_LY>`** **[Nghị định số 52/2003/NĐ-CP]`<THAM_CHIEU_PHAP_LY>`** **[ngày 19/5/2003]`<NGAY_THAM_CHIEU>`** của **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** quy định chức năng , nhiệm vụ , quyền hạn và cơ cấu tổ chức của **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_THAM_QUYEN>`** ;

**Thực thể:**
- `[e0]` **Nghị định số 52/2003/NĐ-CP** → `THAM_CHIEU_PHAP_LY` (span: `[1:4]`)
- `[e1]` **Căn cứ** → `TU_KHOA_PHAP_LY` (span: `[0:1]`)
- `[e2]` **ngày 19/5/2003** → `NGAY_THAM_CHIEU` (span: `[4:6]`)
- `[e3]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[7:8]`)
- `[e4]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_THAM_QUYEN` (span: `[18:21]`)

**Quan hệ:**
- (`e1` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e0` Nghị định số 52/2003/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e3` Chính phủ `[CO_QUAN_THAM_QUYEN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e0` Nghị định số 52/2003/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e0` Nghị định số 52/2003/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e2` ngày 19/5/2003 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #13_2008_QĐ-NHNN_32111#preamble_context_13 (Loại: `preamble_context`)
> **[Quyết định]`<LOAI_VAN_BAN>`** số **[13/2008/QĐ-NHNN]`<SO_HIEU>`** của **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_BAN_HANH>`** . **[Căn cứ]`<TU_KHOA_PHAP_LY>`** **[Nghị định số 49/2000/NĐ-CP]`<THAM_CHIEU_PHAP_LY>`** **[ngày 12/9/2000]`<NGAY_THAM_CHIEU>`** của **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** về tổ chức và hoạt động của **[ngân hàng thương mại]`<TO_CHUC_DOANH_NGHIEP>`** ;

**Thực thể:**
- `[e0]` **Quyết định** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **13/2008/QĐ-NHNN** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_BAN_HANH` (span: `[4:7]`)
- `[e3]` **ngân hàng thương mại** → `TO_CHUC_DOANH_NGHIEP` (span: `[21:23]`)
- `[e4]` **Nghị định số 49/2000/NĐ-CP** → `THAM_CHIEU_PHAP_LY` (span: `[9:12]`)
- `[e5]` **Căn cứ** → `TU_KHOA_PHAP_LY` (span: `[8:9]`)
- `[e6]` **ngày 12/9/2000** → `NGAY_THAM_CHIEU` (span: `[12:14]`)
- `[e7]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[15:16]`)

**Quan hệ:**
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Ngân hàng Nhà nước Việt Nam `[CO_QUAN_BAN_HANH]`)
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Quyết định `[LOAI_VAN_BAN]`)
- (`e5` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e4` Nghị định số 49/2000/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e4` Nghị định số 49/2000/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e4` Nghị định số 49/2000/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e6` ngày 12/9/2000 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #13_2008_QĐ-NHNN_32111#preamble_standalone_14 (Loại: `preamble_standalone`)
> **[Căn cứ]`<TU_KHOA_PHAP_LY>`** **[Nghị định số 49/2000/NĐ-CP]`<THAM_CHIEU_PHAP_LY>`** **[ngày 12/9/2000]`<NGAY_THAM_CHIEU>`** của **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** về tổ chức và hoạt động của **[ngân hàng thương mại]`<TO_CHUC_DOANH_NGHIEP>`** ;

**Thực thể:**
- `[e0]` **ngân hàng thương mại** → `TO_CHUC_DOANH_NGHIEP` (span: `[13:15]`)
- `[e1]` **Nghị định số 49/2000/NĐ-CP** → `THAM_CHIEU_PHAP_LY` (span: `[1:4]`)
- `[e2]` **Căn cứ** → `TU_KHOA_PHAP_LY` (span: `[0:1]`)
- `[e3]` **ngày 12/9/2000** → `NGAY_THAM_CHIEU` (span: `[4:6]`)
- `[e4]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[7:8]`)

**Quan hệ:**
- (`e2` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e1` Nghị định số 49/2000/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e4` Chính phủ `[CO_QUAN_THAM_QUYEN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e1` Nghị định số 49/2000/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e1` Nghị định số 49/2000/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e3` ngày 12/9/2000 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #13_2008_QĐ-NHNN_32111#preamble_context_15 (Loại: `preamble_context`)
> **[Quyết định]`<LOAI_VAN_BAN>`** số **[13/2008/QĐ-NHNN]`<SO_HIEU>`** của **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_BAN_HANH>`** . **[Căn cứ]`<TU_KHOA_PHAP_LY>`** **[Nghị định số 22/2006/NĐ-CP]`<THAM_CHIEU_PHAP_LY>`** **[ngày 28/02/2006]`<NGAY_THAM_CHIEU>`** của **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** về tổ chức và hoạt động của **[chi nhánh ngân hàng nước ngoài]`<TO_CHUC_DOANH_NGHIEP>`** , ngân hàng liên doanh , ngân hàng **[100 %]`<NGUONG_DINH_LUONG>`** vốn nước ngoài , **[văn phòng đại diện]`<TO_CHUC_DOANH_NGHIEP>`** **[tổ chức tín dụng nước ngoài]`<TO_CHUC_DOANH_NGHIEP>`** **[tại Việt Nam]`<DIA_DIEM>`** ;

**Thực thể:**
- `[e0]` **Quyết định** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **13/2008/QĐ-NHNN** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_BAN_HANH` (span: `[4:7]`)
- `[e3]` **văn phòng đại diện** → `TO_CHUC_DOANH_NGHIEP` (span: `[34:36]`)
- `[e4]` **Nghị định số 22/2006/NĐ-CP** → `THAM_CHIEU_PHAP_LY` (span: `[9:12]`)
- `[e5]` **Căn cứ** → `TU_KHOA_PHAP_LY` (span: `[8:9]`)
- `[e6]` **ngày 28/02/2006** → `NGAY_THAM_CHIEU` (span: `[12:14]`)
- `[e7]` **100 %** → `NGUONG_DINH_LUONG` (span: `[29:31]`)
- `[e8]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[15:16]`)
- `[e9]` **chi nhánh ngân hàng nước ngoài** → `TO_CHUC_DOANH_NGHIEP` (span: `[21:24]`)
- `[e10]` **tại Việt Nam** → `DIA_DIEM` (span: `[39:41]`)
- `[e11]` **tổ chức tín dụng nước ngoài** → `TO_CHUC_DOANH_NGHIEP` (span: `[36:39]`)

**Quan hệ:**
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Ngân hàng Nhà nước Việt Nam `[CO_QUAN_BAN_HANH]`)
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Quyết định `[LOAI_VAN_BAN]`)
- (`e5` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e4` Nghị định số 22/2006/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e4` Nghị định số 22/2006/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e4` Nghị định số 22/2006/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e6` ngày 28/02/2006 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #13_2008_QĐ-NHNN_32111#preamble_standalone_16 (Loại: `preamble_standalone`)
> **[Căn cứ]`<TU_KHOA_PHAP_LY>`** **[Nghị định số 22/2006/NĐ-CP]`<THAM_CHIEU_PHAP_LY>`** **[ngày 28/02/2006]`<NGAY_THAM_CHIEU>`** của **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** về tổ chức và hoạt động của **[chi nhánh ngân hàng nước ngoài]`<TO_CHUC_DOANH_NGHIEP>`** , ngân hàng liên doanh , ngân hàng **[100 %]`<NGUONG_DINH_LUONG>`** vốn nước ngoài , **[văn phòng đại diện]`<TO_CHUC_DOANH_NGHIEP>`** **[tổ chức tín dụng nước ngoài]`<TO_CHUC_DOANH_NGHIEP>`** **[tại Việt Nam]`<DIA_DIEM>`** ;

**Thực thể:**
- `[e0]` **văn phòng đại diện** → `TO_CHUC_DOANH_NGHIEP` (span: `[26:28]`)
- `[e1]` **Nghị định số 22/2006/NĐ-CP** → `THAM_CHIEU_PHAP_LY` (span: `[1:4]`)
- `[e2]` **Căn cứ** → `TU_KHOA_PHAP_LY` (span: `[0:1]`)
- `[e3]` **ngày 28/02/2006** → `NGAY_THAM_CHIEU` (span: `[4:6]`)
- `[e4]` **100 %** → `NGUONG_DINH_LUONG` (span: `[21:23]`)
- `[e5]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[7:8]`)
- `[e6]` **chi nhánh ngân hàng nước ngoài** → `TO_CHUC_DOANH_NGHIEP` (span: `[13:16]`)
- `[e7]` **tại Việt Nam** → `DIA_DIEM` (span: `[31:33]`)
- `[e8]` **tổ chức tín dụng nước ngoài** → `TO_CHUC_DOANH_NGHIEP` (span: `[28:31]`)

**Quan hệ:**
- (`e2` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e1` Nghị định số 22/2006/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e5` Chính phủ `[CO_QUAN_THAM_QUYEN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e1` Nghị định số 22/2006/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e1` Nghị định số 22/2006/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e3` ngày 28/02/2006 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #13_2008_QĐ-NHNN_32111#body_context_17 (Loại: `body_context`)
> **[Quyết định]`<LOAI_VAN_BAN>`** số **[13/2008/QĐ-NHNN]`<SO_HIEU>`** ban hành **[ngày 29 tháng 04 năm 2008]`<NGAY_BAN_HANH>`** bởi **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_BAN_HANH>`** . **[Điều 1 . Ban hành kèm theo Quyết định này Quy định về mạng lưới hoạt động của **[ngân hàng thương mại]`<TO_CHUC_DOANH_NGHIEP>`** .]`<DIEU>`**

**Thực thể:**
- `[e0]` **Quyết định** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **13/2008/QĐ-NHNN** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_BAN_HANH` (span: `[11:14]`)
- `[e3]` **ngày 29 tháng 04 năm 2008** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 1 . Ban hành kèm theo Quyết định này Quy định về mạng lưới hoạt động của ngân hàng thương mại .** → `DIEU` (span: `[15:31]`)
- `[e5]` **ngân hàng thương mại** → `TO_CHUC_DOANH_NGHIEP` (span: `[28:30]`) *(lồng trong `e4` (`DIEU`))*

**Quan hệ:**
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Ngân hàng Nhà nước Việt Nam `[CO_QUAN_BAN_HANH]`)
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Quyết định `[LOAI_VAN_BAN]`)
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 29 tháng 04 năm 2008 `[NGAY_BAN_HANH]`)
- (`e4` Điều 1 . Ban hành kèm theo Quyết định này Quy định về mạng lưới hoạt động của ngân hàng thương mại . `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`)


---

### Mẫu #13_2008_QĐ-NHNN_32111#body_context_18 (Loại: `body_context`)
> **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_BAN_HANH>`** ban hành **[Quyết định]`<LOAI_VAN_BAN>`** số **[13/2008/QĐ-NHNN]`<SO_HIEU>`** . **[Điều 2 . Quyết định này có hiệu lực thi hành **[sau 15 ngày]`<THOI_HAN>`** kể từ ngày đăng Công báo . **[Quyết định số 888/2005/QĐ-NHNN]`<THAM_CHIEU_PHAP_LY>`** **[ngày 16/6/2005]`<NGAY_THAM_CHIEU>`** của **[Thống đốc Ngân hàng Nhà nước]`<CO_QUAN_THAM_QUYEN>`** ban hành Quy định về việc mở , thành lập và chấm dứt hoạt động **[sở giao dịch]`<CO_QUAN_THAM_QUYEN>`** , chi nhánh , **[văn phòng đại diện]`<TO_CHUC_DOANH_NGHIEP>`** , **[đơn vị sự nghiệp]`<TO_CHUC_DOANH_NGHIEP>`** của **[ngân hàng thương mại]`<TO_CHUC_DOANH_NGHIEP>`** , **[Quyết định số 1090/2003/QĐ-NHNN]`<THAM_CHIEU_PHAP_LY>`** **[ngày 17/9/2003]`<NGAY_THAM_CHIEU>`** của **[Thống đốc Ngân hàng Nhà nước]`<CO_QUAN_THAM_QUYEN>`** ban hành Quy định về việc mở và chấm dứt hoạt động **[sở giao dịch]`<CO_QUAN_THAM_QUYEN>`** , chi nhánh , phòng]`<DIEU>`**

**Thực thể:**
- `[e0]` **Quyết định** → `LOAI_VAN_BAN` (span: `[4:5]`)
- `[e1]` **13/2008/QĐ-NHNN** → `SO_HIEU` (span: `[6:7]`)
- `[e2]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_BAN_HANH` (span: `[0:3]`)
- `[e3]` **Điều 2 . Quyết định này có hiệu lực thi hành sau 15 ngày kể từ ngày đăng Công báo . Quyết định số 888/2005/QĐ-NHNN ngày 16/6/2005 của Thống đốc Ngân hàng Nhà nước ban hành Quy định về việc mở , thành lập và chấm dứt hoạt động sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp của ngân hàng thương mại , Quyết định số 1090/2003/QĐ-NHNN ngày 17/9/2003 của Thống đốc Ngân hàng Nhà nước ban hành Quy định về việc mở và chấm dứt hoạt động sở giao dịch , chi nhánh , phòng** → `DIEU` (span: `[8:81]`)
- `[e4]` **sở giao dịch** → `CO_QUAN_THAM_QUYEN` (span: `[44:46]`) *(lồng trong `e3` (`DIEU`))*
- `[e5]` **sở giao dịch** → `CO_QUAN_THAM_QUYEN` (span: `[75:77]`) *(lồng trong `e3` (`DIEU`))*
- `[e6]` **ngân hàng thương mại** → `TO_CHUC_DOANH_NGHIEP` (span: `[55:57]`) *(lồng trong `e3` (`DIEU`))*
- `[e7]` **văn phòng đại diện** → `TO_CHUC_DOANH_NGHIEP` (span: `[49:51]`) *(lồng trong `e3` (`DIEU`))*
- `[e8]` **đơn vị sự nghiệp** → `TO_CHUC_DOANH_NGHIEP` (span: `[52:54]`) *(lồng trong `e3` (`DIEU`))*
- `[e9]` **Quyết định số 888/2005/QĐ-NHNN** → `THAM_CHIEU_PHAP_LY` (span: `[25:28]`) *(lồng trong `e3` (`DIEU`))*
- `[e10]` **Quyết định số 1090/2003/QĐ-NHNN** → `THAM_CHIEU_PHAP_LY` (span: `[58:61]`) *(lồng trong `e3` (`DIEU`))*
- `[e11]` **ngày 16/6/2005** → `NGAY_THAM_CHIEU` (span: `[28:30]`) *(lồng trong `e3` (`DIEU`))*
- `[e12]` **ngày 17/9/2003** → `NGAY_THAM_CHIEU` (span: `[61:63]`) *(lồng trong `e3` (`DIEU`))*
- `[e13]` **sau 15 ngày** → `THOI_HAN` (span: `[16:19]`) *(lồng trong `e3` (`DIEU`))*
- `[e14]` **Thống đốc Ngân hàng Nhà nước** → `CO_QUAN_THAM_QUYEN` (span: `[31:34]`) *(lồng trong `e3` (`DIEU`))*
- `[e15]` **Thống đốc Ngân hàng Nhà nước** → `CO_QUAN_THAM_QUYEN` (span: `[64:67]`) *(lồng trong `e3` (`DIEU`))*

**Quan hệ:**
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Ngân hàng Nhà nước Việt Nam `[CO_QUAN_BAN_HANH]`)
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Quyết định `[LOAI_VAN_BAN]`)
- (`e3` Điều 2 . Quyết định này có hiệu lực thi hành sau 15 ngày kể từ ngày đăng Công báo . Quyết định số 888/2005/QĐ-NHNN ngày 16/6/2005 của Thống đốc Ngân hàng Nhà nước ban hành Quy định về việc mở , thành lập và chấm dứt hoạt động sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp của ngân hàng thương mại , Quyết định số 1090/2003/QĐ-NHNN ngày 17/9/2003 của Thống đốc Ngân hàng Nhà nước ban hành Quy định về việc mở và chấm dứt hoạt động sở giao dịch , chi nhánh , phòng `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`)
- (`e3` Điều 2 . Quyết định này có hiệu lực thi hành sau 15 ngày kể từ ngày đăng Công báo . Quyết định số 888/2005/QĐ-NHNN ngày 16/6/2005 của Thống đốc Ngân hàng Nhà nước ban hành Quy định về việc mở , thành lập và chấm dứt hoạt động sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp của ngân hàng thương mại , Quyết định số 1090/2003/QĐ-NHNN ngày 17/9/2003 của Thống đốc Ngân hàng Nhà nước ban hành Quy định về việc mở và chấm dứt hoạt động sở giao dịch , chi nhánh , phòng `[DIEU]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e9` Quyết định số 888/2005/QĐ-NHNN `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e3` Điều 2 . Quyết định này có hiệu lực thi hành sau 15 ngày kể từ ngày đăng Công báo . Quyết định số 888/2005/QĐ-NHNN ngày 16/6/2005 của Thống đốc Ngân hàng Nhà nước ban hành Quy định về việc mở , thành lập và chấm dứt hoạt động sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp của ngân hàng thương mại , Quyết định số 1090/2003/QĐ-NHNN ngày 17/9/2003 của Thống đốc Ngân hàng Nhà nước ban hành Quy định về việc mở và chấm dứt hoạt động sở giao dịch , chi nhánh , phòng `[DIEU]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e10` Quyết định số 1090/2003/QĐ-NHNN `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e9` Quyết định số 888/2005/QĐ-NHNN `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e11` ngày 16/6/2005 `[NGAY_THAM_CHIEU]`)
- (`e10` Quyết định số 1090/2003/QĐ-NHNN `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e12` ngày 17/9/2003 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #13_2008_QĐ-NHNN_32111#body_standalone_19 (Loại: `body_standalone`)
> **[Điều 2 . Quyết định này có hiệu lực thi hành **[sau 15 ngày]`<THOI_HAN>`** kể từ ngày đăng Công báo . **[Quyết định số 888/2005/QĐ-NHNN]`<THAM_CHIEU_PHAP_LY>`** **[ngày 16/6/2005]`<NGAY_THAM_CHIEU>`** của **[Thống đốc Ngân hàng Nhà nước]`<CO_QUAN_THAM_QUYEN>`** ban hành Quy định về việc mở , thành lập và chấm dứt hoạt động **[sở giao dịch]`<CO_QUAN_THAM_QUYEN>`** , chi nhánh , **[văn phòng đại diện]`<TO_CHUC_DOANH_NGHIEP>`** , **[đơn vị sự nghiệp]`<TO_CHUC_DOANH_NGHIEP>`** của **[ngân hàng thương mại]`<TO_CHUC_DOANH_NGHIEP>`** , **[Quyết định số 1090/2003/QĐ-NHNN]`<THAM_CHIEU_PHAP_LY>`** **[ngày 17/9/2003]`<NGAY_THAM_CHIEU>`** của **[Thống đốc Ngân hàng Nhà nước]`<CO_QUAN_THAM_QUYEN>`** ban hành Quy định về việc mở và chấm dứt hoạt động **[sở giao dịch]`<CO_QUAN_THAM_QUYEN>`** , chi nhánh , phòng]`<DIEU>`**

**Thực thể:**
- `[e0]` **Điều 2 . Quyết định này có hiệu lực thi hành sau 15 ngày kể từ ngày đăng Công báo . Quyết định số 888/2005/QĐ-NHNN ngày 16/6/2005 của Thống đốc Ngân hàng Nhà nước ban hành Quy định về việc mở , thành lập và chấm dứt hoạt động sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp của ngân hàng thương mại , Quyết định số 1090/2003/QĐ-NHNN ngày 17/9/2003 của Thống đốc Ngân hàng Nhà nước ban hành Quy định về việc mở và chấm dứt hoạt động sở giao dịch , chi nhánh , phòng** → `DIEU` (span: `[0:73]`)
- `[e1]` **sở giao dịch** → `CO_QUAN_THAM_QUYEN` (span: `[36:38]`) *(lồng trong `e0` (`DIEU`))*
- `[e2]` **sở giao dịch** → `CO_QUAN_THAM_QUYEN` (span: `[67:69]`) *(lồng trong `e0` (`DIEU`))*
- `[e3]` **ngân hàng thương mại** → `TO_CHUC_DOANH_NGHIEP` (span: `[47:49]`) *(lồng trong `e0` (`DIEU`))*
- `[e4]` **văn phòng đại diện** → `TO_CHUC_DOANH_NGHIEP` (span: `[41:43]`) *(lồng trong `e0` (`DIEU`))*
- `[e5]` **đơn vị sự nghiệp** → `TO_CHUC_DOANH_NGHIEP` (span: `[44:46]`) *(lồng trong `e0` (`DIEU`))*
- `[e6]` **Quyết định số 888/2005/QĐ-NHNN** → `THAM_CHIEU_PHAP_LY` (span: `[17:20]`) *(lồng trong `e0` (`DIEU`))*
- `[e7]` **Quyết định số 1090/2003/QĐ-NHNN** → `THAM_CHIEU_PHAP_LY` (span: `[50:53]`) *(lồng trong `e0` (`DIEU`))*
- `[e8]` **ngày 16/6/2005** → `NGAY_THAM_CHIEU` (span: `[20:22]`) *(lồng trong `e0` (`DIEU`))*
- `[e9]` **ngày 17/9/2003** → `NGAY_THAM_CHIEU` (span: `[53:55]`) *(lồng trong `e0` (`DIEU`))*
- `[e10]` **sau 15 ngày** → `THOI_HAN` (span: `[8:11]`) *(lồng trong `e0` (`DIEU`))*
- `[e11]` **Thống đốc Ngân hàng Nhà nước** → `CO_QUAN_THAM_QUYEN` (span: `[23:26]`) *(lồng trong `e0` (`DIEU`))*
- `[e12]` **Thống đốc Ngân hàng Nhà nước** → `CO_QUAN_THAM_QUYEN` (span: `[56:59]`) *(lồng trong `e0` (`DIEU`))*

**Quan hệ:**
- (`e0` Điều 2 . Quyết định này có hiệu lực thi hành sau 15 ngày kể từ ngày đăng Công báo . Quyết định số 888/2005/QĐ-NHNN ngày 16/6/2005 của Thống đốc Ngân hàng Nhà nước ban hành Quy định về việc mở , thành lập và chấm dứt hoạt động sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp của ngân hàng thương mại , Quyết định số 1090/2003/QĐ-NHNN ngày 17/9/2003 của Thống đốc Ngân hàng Nhà nước ban hành Quy định về việc mở và chấm dứt hoạt động sở giao dịch , chi nhánh , phòng `[DIEU]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e6` Quyết định số 888/2005/QĐ-NHNN `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e0` Điều 2 . Quyết định này có hiệu lực thi hành sau 15 ngày kể từ ngày đăng Công báo . Quyết định số 888/2005/QĐ-NHNN ngày 16/6/2005 của Thống đốc Ngân hàng Nhà nước ban hành Quy định về việc mở , thành lập và chấm dứt hoạt động sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp của ngân hàng thương mại , Quyết định số 1090/2003/QĐ-NHNN ngày 17/9/2003 của Thống đốc Ngân hàng Nhà nước ban hành Quy định về việc mở và chấm dứt hoạt động sở giao dịch , chi nhánh , phòng `[DIEU]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e7` Quyết định số 1090/2003/QĐ-NHNN `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e6` Quyết định số 888/2005/QĐ-NHNN `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e8` ngày 16/6/2005 `[NGAY_THAM_CHIEU]`)
- (`e7` Quyết định số 1090/2003/QĐ-NHNN `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e9` ngày 17/9/2003 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #13_2008_QĐ-NHNN_32111#body_context_20 (Loại: `body_context`)
> **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_BAN_HANH>`** ban hành **[Quyết định]`<LOAI_VAN_BAN>`** số **[13/2008/QĐ-NHNN]`<SO_HIEU>`** . **[Điều 3 . Chánh Văn phòng , Vụ trưởng Vụ Các Ngân hàng và **[tổ chức tín dụng phi ngân hàng]`<TO_CHUC_DOANH_NGHIEP>`** , Thủ trưởng các đơn vị có liên quan thuộc **[Ngân hàng nhà nước Việt Nam]`<CO_QUAN_THAM_QUYEN>`** , **[Giám đốc]`<CHU_THE_CA_NHAN>`** **[Ngân hàng Nhà nước]`<CO_QUAN_THAM_QUYEN>`** chi nhánh các tỉnh , thành phố trực thuộc trung ương và Chủ tịch **[Hội đồng quản trị]`<TO_CHUC_DOANH_NGHIEP>`** , **[Tổng Giám đốc]`<CHU_THE_CA_NHAN>`** ( **[Giám đốc]`<CHU_THE_CA_NHAN>`** ) các **[ngân hàng thương mại]`<TO_CHUC_DOANH_NGHIEP>`** có trách nhiệm thi hành Quyết định này .]`<DIEU>`**

**Thực thể:**
- `[e0]` **Quyết định** → `LOAI_VAN_BAN` (span: `[4:5]`)
- `[e1]` **13/2008/QĐ-NHNN** → `SO_HIEU` (span: `[6:7]`)
- `[e2]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_BAN_HANH` (span: `[0:3]`)
- `[e3]` **Điều 3 . Chánh Văn phòng , Vụ trưởng Vụ Các Ngân hàng và tổ chức tín dụng phi ngân hàng , Thủ trưởng các đơn vị có liên quan thuộc Ngân hàng nhà nước Việt Nam , Giám đốc Ngân hàng Nhà nước chi nhánh các tỉnh , thành phố trực thuộc trung ương và Chủ tịch Hội đồng quản trị , Tổng Giám đốc ( Giám đốc ) các ngân hàng thương mại có trách nhiệm thi hành Quyết định này .** → `DIEU` (span: `[8:62]`)
- `[e4]` **ngân hàng thương mại** → `TO_CHUC_DOANH_NGHIEP` (span: `[54:56]`) *(lồng trong `e3` (`DIEU`))*
- `[e5]` **Ngân hàng nhà nước Việt Nam** → `CO_QUAN_THAM_QUYEN` (span: `[30:33]`) *(lồng trong `e3` (`DIEU`))*
- `[e6]` **Ngân hàng Nhà nước** → `CO_QUAN_THAM_QUYEN` (span: `[35:37]`) *(lồng trong `e3` (`DIEU`))*
- `[e7]` **tổ chức tín dụng phi ngân hàng** → `TO_CHUC_DOANH_NGHIEP` (span: `[19:23]`) *(lồng trong `e3` (`DIEU`))*
- `[e8]` **Hội đồng quản trị** → `TO_CHUC_DOANH_NGHIEP` (span: `[46:48]`) *(lồng trong `e3` (`DIEU`))*
- `[e9]` **Giám đốc** → `CHU_THE_CA_NHAN` (span: `[34:35]`) *(lồng trong `e3` (`DIEU`))*
- `[e10]` **Tổng Giám đốc** → `CHU_THE_CA_NHAN` (span: `[49:50]`) *(lồng trong `e3` (`DIEU`))*
- `[e11]` **Giám đốc** → `CHU_THE_CA_NHAN` (span: `[51:52]`) *(lồng trong `e3` (`DIEU`))*

**Quan hệ:**
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Ngân hàng Nhà nước Việt Nam `[CO_QUAN_BAN_HANH]`)
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Quyết định `[LOAI_VAN_BAN]`)
- (`e3` Điều 3 . Chánh Văn phòng , Vụ trưởng Vụ Các Ngân hàng và tổ chức tín dụng phi ngân hàng , Thủ trưởng các đơn vị có liên quan thuộc Ngân hàng nhà nước Việt Nam , Giám đốc Ngân hàng Nhà nước chi nhánh các tỉnh , thành phố trực thuộc trung ương và Chủ tịch Hội đồng quản trị , Tổng Giám đốc ( Giám đốc ) các ngân hàng thương mại có trách nhiệm thi hành Quyết định này . `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`)


---

### Mẫu #13_2008_QĐ-NHNN_32111#body_context_21 (Loại: `body_context`)
> **[Quyết định]`<LOAI_VAN_BAN>`** số **[13/2008/QĐ-NHNN]`<SO_HIEU>`** ban hành **[ngày 29 tháng 04 năm 2008]`<NGAY_BAN_HANH>`** bởi **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_BAN_HANH>`** . **[Điều 2]`<DIEU>`** . **[5 . Chi nhánh là đơn vị phụ thuộc **[ngân hàng thương mại]`<TO_CHUC_DOANH_NGHIEP>`** , có con dấu , thực hiện hoạt động kinh doanh theo ủy quyền của **[ngân hàng thương mại]`<TO_CHUC_DOANH_NGHIEP>`** .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Quyết định** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **13/2008/QĐ-NHNN** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_BAN_HANH` (span: `[11:14]`)
- `[e3]` **ngày 29 tháng 04 năm 2008** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 2** → `DIEU` (span: `[15:17]`)
- `[e5]` **5 . Chi nhánh là đơn vị phụ thuộc ngân hàng thương mại , có con dấu , thực hiện hoạt động kinh doanh theo ủy quyền của ngân hàng thương mại .** → `KHOAN` (span: `[18:39]`)
- `[e6]` **ngân hàng thương mại** → `TO_CHUC_DOANH_NGHIEP` (span: `[24:26]`) *(lồng trong `e5` (`KHOAN`))*
- `[e7]` **ngân hàng thương mại** → `TO_CHUC_DOANH_NGHIEP` (span: `[36:38]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Ngân hàng Nhà nước Việt Nam `[CO_QUAN_BAN_HANH]`)
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Quyết định `[LOAI_VAN_BAN]`)
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 29 tháng 04 năm 2008 `[NGAY_BAN_HANH]`)
- (`e4` Điều 2 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`)
- (`e5` 5 . Chi nhánh là đơn vị phụ thuộc ngân hàng thương mại , có con dấu , thực hiện hoạt động kinh doanh theo ủy quyền của ngân hàng thương mại . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 2 `[DIEU]`)


---

### Mẫu #13_2008_QĐ-NHNN_32111#body_standalone_22 (Loại: `body_standalone`)
> **[Điều 2]`<DIEU>`** . **[5 . Chi nhánh là đơn vị phụ thuộc **[ngân hàng thương mại]`<TO_CHUC_DOANH_NGHIEP>`** , có con dấu , thực hiện hoạt động kinh doanh theo ủy quyền của **[ngân hàng thương mại]`<TO_CHUC_DOANH_NGHIEP>`** .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 2** → `DIEU` (span: `[0:2]`)
- `[e1]` **5 . Chi nhánh là đơn vị phụ thuộc ngân hàng thương mại , có con dấu , thực hiện hoạt động kinh doanh theo ủy quyền của ngân hàng thương mại .** → `KHOAN` (span: `[3:24]`)
- `[e2]` **ngân hàng thương mại** → `TO_CHUC_DOANH_NGHIEP` (span: `[9:11]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **ngân hàng thương mại** → `TO_CHUC_DOANH_NGHIEP` (span: `[21:23]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 5 . Chi nhánh là đơn vị phụ thuộc ngân hàng thương mại , có con dấu , thực hiện hoạt động kinh doanh theo ủy quyền của ngân hàng thương mại . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 2 `[DIEU]`)


---

### Mẫu #13_2008_QĐ-NHNN_32111#body_context_23 (Loại: `body_context`)
> **[Quyết định]`<LOAI_VAN_BAN>`** số **[13/2008/QĐ-NHNN]`<SO_HIEU>`** của **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Ngân hàng]`<LINH_VUC>`** . **[Điều 2]`<DIEU>`** . **[Khoản 8]`<KHOAN>`** . **[a ) Cấp tín dụng cho một **[khách hàng]`<CHU_THE_CA_NHAN>`** vượt quá hai tỷ Đồng Việt Nam hoặc ngoại tệ quy đổi tương đương , trừ trường hợp khoản cấp tín dụng được bảo đảm toàn bộ bằng : tiền , vàng , thẻ tiết kiệm , **[giấy tờ có giá]`<GIAY_TO_HO_SO>`** do chính **[ngân hàng thương mại]`<TO_CHUC_DOANH_NGHIEP>`** phát hành , **[trái phiếu]`<TAI_SAN_VAT_CHAT>`** **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** , tín phiếu **[Kho bạc Nhà nước]`<CO_QUAN_THAM_QUYEN>`** ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Quyết định** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **13/2008/QĐ-NHNN** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_BAN_HANH` (span: `[4:7]`)
- `[e3]` **Ngân hàng** → `LINH_VUC` (span: `[9:10]`)
- `[e4]` **Điều 2** → `DIEU` (span: `[11:13]`)
- `[e5]` **Khoản 8** → `KHOAN` (span: `[14:16]`)
- `[e6]` **a ) Cấp tín dụng cho một khách hàng vượt quá hai tỷ Đồng Việt Nam hoặc ngoại tệ quy đổi tương đương , trừ trường hợp khoản cấp tín dụng được bảo đảm toàn bộ bằng : tiền , vàng , thẻ tiết kiệm , giấy tờ có giá do chính ngân hàng thương mại phát hành , trái phiếu Chính phủ , tín phiếu Kho bạc Nhà nước ;** → `DIEM` (span: `[17:67]`)
- `[e7]` **ngân hàng thương mại** → `TO_CHUC_DOANH_NGHIEP` (span: `[56:58]`) *(lồng trong `e6` (`DIEM`))*
- `[e8]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[61:62]`) *(lồng trong `e6` (`DIEM`))*
- `[e9]` **Kho bạc Nhà nước** → `CO_QUAN_THAM_QUYEN` (span: `[64:66]`) *(lồng trong `e6` (`DIEM`))*
- `[e10]` **giấy tờ có giá** → `GIAY_TO_HO_SO` (span: `[52:54]`) *(lồng trong `e6` (`DIEM`))*
- `[e11]` **khách hàng** → `CHU_THE_CA_NHAN` (span: `[23:24]`) *(lồng trong `e6` (`DIEM`))*
- `[e12]` **trái phiếu** → `TAI_SAN_VAT_CHAT` (span: `[60:61]`) *(lồng trong `e6` (`DIEM`))*

**Quan hệ:**
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Ngân hàng Nhà nước Việt Nam `[CO_QUAN_BAN_HANH]`)
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Quyết định `[LOAI_VAN_BAN]`)
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Ngân hàng `[LINH_VUC]`)
- (`e4` Điều 2 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`)
- (`e5` Khoản 8 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 2 `[DIEU]`)
- (`e6` a ) Cấp tín dụng cho một khách hàng vượt quá hai tỷ Đồng Việt Nam hoặc ngoại tệ quy đổi tương đương , trừ trường hợp khoản cấp tín dụng được bảo đảm toàn bộ bằng : tiền , vàng , thẻ tiết kiệm , giấy tờ có giá do chính ngân hàng thương mại phát hành , trái phiếu Chính phủ , tín phiếu Kho bạc Nhà nước ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e5` Khoản 8 `[KHOAN]`)
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Ngân hàng `[LINH_VUC]`)
- (`e6` a ) Cấp tín dụng cho một khách hàng vượt quá hai tỷ Đồng Việt Nam hoặc ngoại tệ quy đổi tương đương , trừ trường hợp khoản cấp tín dụng được bảo đảm toàn bộ bằng : tiền , vàng , thẻ tiết kiệm , giấy tờ có giá do chính ngân hàng thương mại phát hành , trái phiếu Chính phủ , tín phiếu Kho bạc Nhà nước ; `[DIEM]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Ngân hàng `[LINH_VUC]`)


---

### Mẫu #13_2008_QĐ-NHNN_32111#body_standalone_24 (Loại: `body_standalone`)
> **[Điều 2]`<DIEU>`** . **[Khoản 8]`<KHOAN>`** . **[a ) Cấp tín dụng cho một **[khách hàng]`<CHU_THE_CA_NHAN>`** vượt quá hai tỷ Đồng Việt Nam hoặc ngoại tệ quy đổi tương đương , trừ trường hợp khoản cấp tín dụng được bảo đảm toàn bộ bằng : tiền , vàng , thẻ tiết kiệm , **[giấy tờ có giá]`<GIAY_TO_HO_SO>`** do chính **[ngân hàng thương mại]`<TO_CHUC_DOANH_NGHIEP>`** phát hành , **[trái phiếu]`<TAI_SAN_VAT_CHAT>`** **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** , tín phiếu **[Kho bạc Nhà nước]`<CO_QUAN_THAM_QUYEN>`** ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Điều 2** → `DIEU` (span: `[0:2]`)
- `[e1]` **Khoản 8** → `KHOAN` (span: `[3:5]`)
- `[e2]` **a ) Cấp tín dụng cho một khách hàng vượt quá hai tỷ Đồng Việt Nam hoặc ngoại tệ quy đổi tương đương , trừ trường hợp khoản cấp tín dụng được bảo đảm toàn bộ bằng : tiền , vàng , thẻ tiết kiệm , giấy tờ có giá do chính ngân hàng thương mại phát hành , trái phiếu Chính phủ , tín phiếu Kho bạc Nhà nước ;** → `DIEM` (span: `[6:56]`)
- `[e3]` **ngân hàng thương mại** → `TO_CHUC_DOANH_NGHIEP` (span: `[45:47]`) *(lồng trong `e2` (`DIEM`))*
- `[e4]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[50:51]`) *(lồng trong `e2` (`DIEM`))*
- `[e5]` **Kho bạc Nhà nước** → `CO_QUAN_THAM_QUYEN` (span: `[53:55]`) *(lồng trong `e2` (`DIEM`))*
- `[e6]` **giấy tờ có giá** → `GIAY_TO_HO_SO` (span: `[41:43]`) *(lồng trong `e2` (`DIEM`))*
- `[e7]` **khách hàng** → `CHU_THE_CA_NHAN` (span: `[12:13]`) *(lồng trong `e2` (`DIEM`))*
- `[e8]` **trái phiếu** → `TAI_SAN_VAT_CHAT` (span: `[49:50]`) *(lồng trong `e2` (`DIEM`))*

**Quan hệ:**
- (`e1` Khoản 8 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 2 `[DIEU]`)
- (`e2` a ) Cấp tín dụng cho một khách hàng vượt quá hai tỷ Đồng Việt Nam hoặc ngoại tệ quy đổi tương đương , trừ trường hợp khoản cấp tín dụng được bảo đảm toàn bộ bằng : tiền , vàng , thẻ tiết kiệm , giấy tờ có giá do chính ngân hàng thương mại phát hành , trái phiếu Chính phủ , tín phiếu Kho bạc Nhà nước ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e1` Khoản 8 `[KHOAN]`)


---

### Mẫu #13_2008_QĐ-NHNN_32111#body_context_25 (Loại: `body_context`)
> **[Quyết định]`<LOAI_VAN_BAN>`** số **[13/2008/QĐ-NHNN]`<SO_HIEU>`** ban hành **[ngày 29 tháng 04 năm 2008]`<NGAY_BAN_HANH>`** bởi **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_BAN_HANH>`** . **[Chương I]`<CHUONG>`** . **[Điều 4 . Quyền tự chủ của **[ngân hàng thương mại]`<TO_CHUC_DOANH_NGHIEP>`**]`<DIEU>`**

**Thực thể:**
- `[e0]` **Quyết định** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **13/2008/QĐ-NHNN** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_BAN_HANH` (span: `[11:14]`)
- `[e3]` **ngày 29 tháng 04 năm 2008** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Chương I** → `CHUONG` (span: `[15:17]`)
- `[e5]` **Điều 4 . Quyền tự chủ của ngân hàng thương mại** → `DIEU` (span: `[18:26]`)
- `[e6]` **ngân hàng thương mại** → `TO_CHUC_DOANH_NGHIEP` (span: `[24:26]`) *(lồng trong `e5` (`DIEU`))*

**Quan hệ:**
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Ngân hàng Nhà nước Việt Nam `[CO_QUAN_BAN_HANH]`)
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Quyết định `[LOAI_VAN_BAN]`)
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 29 tháng 04 năm 2008 `[NGAY_BAN_HANH]`)
- (`e4` Chương I `[CHUONG]`) ==[ **THUOC_VE** ]==> (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`)
- (`e5` Điều 4 . Quyền tự chủ của ngân hàng thương mại `[DIEU]`) ==[ **THUOC_VE** ]==> (`e4` Chương I `[CHUONG]`)


---

### Mẫu #13_2008_QĐ-NHNN_32111#body_context_26 (Loại: `body_context`)
> **[Quyết định]`<LOAI_VAN_BAN>`** số **[13/2008/QĐ-NHNN]`<SO_HIEU>`** của **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Ngân hàng]`<LINH_VUC>`** . **[Điều 6]`<DIEU>`** . **[1 . Trong vòng một năm kể từ ngày khai trương hoạt động , theo phương án mở **[sở giao dịch]`<CO_QUAN_THAM_QUYEN>`** , chi nhánh nêu tại **[Hồ sơ đề nghị cấp giấy phép thành lập]`<GIAY_TO_HO_SO>`** và hoạt động , **[ngân hàng thương mại]`<TO_CHUC_DOANH_NGHIEP>`** được mở **[sở giao dịch]`<CO_QUAN_THAM_QUYEN>`** và tối đa hai chi nhánh khi đáp ứng đủ các điều kiện sau :]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Quyết định** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **13/2008/QĐ-NHNN** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_BAN_HANH` (span: `[4:7]`)
- `[e3]` **Ngân hàng** → `LINH_VUC` (span: `[9:10]`)
- `[e4]` **Điều 6** → `DIEU` (span: `[11:13]`)
- `[e5]` **1 . Trong vòng một năm kể từ ngày khai trương hoạt động , theo phương án mở sở giao dịch , chi nhánh nêu tại Hồ sơ đề nghị cấp giấy phép thành lập và hoạt động , ngân hàng thương mại được mở sở giao dịch và tối đa hai chi nhánh khi đáp ứng đủ các điều kiện sau :** → `KHOAN` (span: `[14:60]`)
- `[e6]` **sở giao dịch** → `CO_QUAN_THAM_QUYEN` (span: `[29:31]`) *(lồng trong `e5` (`KHOAN`))*
- `[e7]` **sở giao dịch** → `CO_QUAN_THAM_QUYEN` (span: `[47:49]`) *(lồng trong `e5` (`KHOAN`))*
- `[e8]` **ngân hàng thương mại** → `TO_CHUC_DOANH_NGHIEP` (span: `[43:45]`) *(lồng trong `e5` (`KHOAN`))*
- `[e9]` **Hồ sơ đề nghị cấp giấy phép thành lập** → `GIAY_TO_HO_SO` (span: `[35:40]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Ngân hàng Nhà nước Việt Nam `[CO_QUAN_BAN_HANH]`)
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Quyết định `[LOAI_VAN_BAN]`)
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Ngân hàng `[LINH_VUC]`)
- (`e4` Điều 6 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`)
- (`e5` 1 . Trong vòng một năm kể từ ngày khai trương hoạt động , theo phương án mở sở giao dịch , chi nhánh nêu tại Hồ sơ đề nghị cấp giấy phép thành lập và hoạt động , ngân hàng thương mại được mở sở giao dịch và tối đa hai chi nhánh khi đáp ứng đủ các điều kiện sau : `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 6 `[DIEU]`)
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Ngân hàng `[LINH_VUC]`)
- (`e5` 1 . Trong vòng một năm kể từ ngày khai trương hoạt động , theo phương án mở sở giao dịch , chi nhánh nêu tại Hồ sơ đề nghị cấp giấy phép thành lập và hoạt động , ngân hàng thương mại được mở sở giao dịch và tối đa hai chi nhánh khi đáp ứng đủ các điều kiện sau : `[KHOAN]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Ngân hàng `[LINH_VUC]`)


---

### Mẫu #13_2008_QĐ-NHNN_32111#body_standalone_27 (Loại: `body_standalone`)
> **[Điều 6]`<DIEU>`** . **[1 . Trong vòng một năm kể từ ngày khai trương hoạt động , theo phương án mở **[sở giao dịch]`<CO_QUAN_THAM_QUYEN>`** , chi nhánh nêu tại **[Hồ sơ đề nghị cấp giấy phép thành lập]`<GIAY_TO_HO_SO>`** và hoạt động , **[ngân hàng thương mại]`<TO_CHUC_DOANH_NGHIEP>`** được mở **[sở giao dịch]`<CO_QUAN_THAM_QUYEN>`** và tối đa hai chi nhánh khi đáp ứng đủ các điều kiện sau :]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 6** → `DIEU` (span: `[0:2]`)
- `[e1]` **1 . Trong vòng một năm kể từ ngày khai trương hoạt động , theo phương án mở sở giao dịch , chi nhánh nêu tại Hồ sơ đề nghị cấp giấy phép thành lập và hoạt động , ngân hàng thương mại được mở sở giao dịch và tối đa hai chi nhánh khi đáp ứng đủ các điều kiện sau :** → `KHOAN` (span: `[3:49]`)
- `[e2]` **sở giao dịch** → `CO_QUAN_THAM_QUYEN` (span: `[18:20]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **sở giao dịch** → `CO_QUAN_THAM_QUYEN` (span: `[36:38]`) *(lồng trong `e1` (`KHOAN`))*
- `[e4]` **ngân hàng thương mại** → `TO_CHUC_DOANH_NGHIEP` (span: `[32:34]`) *(lồng trong `e1` (`KHOAN`))*
- `[e5]` **Hồ sơ đề nghị cấp giấy phép thành lập** → `GIAY_TO_HO_SO` (span: `[24:29]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 1 . Trong vòng một năm kể từ ngày khai trương hoạt động , theo phương án mở sở giao dịch , chi nhánh nêu tại Hồ sơ đề nghị cấp giấy phép thành lập và hoạt động , ngân hàng thương mại được mở sở giao dịch và tối đa hai chi nhánh khi đáp ứng đủ các điều kiện sau : `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 6 `[DIEU]`)


---

### Mẫu #13_2008_QĐ-NHNN_32111#body_context_28 (Loại: `body_context`)
> **[Quyết định]`<LOAI_VAN_BAN>`** số **[13/2008/QĐ-NHNN]`<SO_HIEU>`** của **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Ngân hàng]`<LINH_VUC>`** . **[Điều 6]`<DIEU>`** . **[Khoản 2]`<KHOAN>`** . **[e ) Không bị Thanh tra Ngân hàng xử phạt hành chính tổng cộng từ ba mươi triệu đồng trở lên trong thời gian một năm tính đến thời điểm đề nghị mở **[sở giao dịch]`<CO_QUAN_THAM_QUYEN>`** , chi nhánh ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Quyết định** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **13/2008/QĐ-NHNN** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_BAN_HANH` (span: `[4:7]`)
- `[e3]` **Ngân hàng** → `LINH_VUC` (span: `[9:10]`)
- `[e4]` **Điều 6** → `DIEU` (span: `[11:13]`)
- `[e5]` **Khoản 2** → `KHOAN` (span: `[14:16]`)
- `[e6]` **e ) Không bị Thanh tra Ngân hàng xử phạt hành chính tổng cộng từ ba mươi triệu đồng trở lên trong thời gian một năm tính đến thời điểm đề nghị mở sở giao dịch , chi nhánh ;** → `DIEM` (span: `[17:47]`)
- `[e7]` **sở giao dịch** → `CO_QUAN_THAM_QUYEN` (span: `[42:44]`) *(lồng trong `e6` (`DIEM`))*

**Quan hệ:**
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Ngân hàng Nhà nước Việt Nam `[CO_QUAN_BAN_HANH]`)
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Quyết định `[LOAI_VAN_BAN]`)
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Ngân hàng `[LINH_VUC]`)
- (`e4` Điều 6 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`)
- (`e5` Khoản 2 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 6 `[DIEU]`)
- (`e6` e ) Không bị Thanh tra Ngân hàng xử phạt hành chính tổng cộng từ ba mươi triệu đồng trở lên trong thời gian một năm tính đến thời điểm đề nghị mở sở giao dịch , chi nhánh ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e5` Khoản 2 `[KHOAN]`)
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Ngân hàng `[LINH_VUC]`)
- (`e6` e ) Không bị Thanh tra Ngân hàng xử phạt hành chính tổng cộng từ ba mươi triệu đồng trở lên trong thời gian một năm tính đến thời điểm đề nghị mở sở giao dịch , chi nhánh ; `[DIEM]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Ngân hàng `[LINH_VUC]`)


---

### Mẫu #13_2008_QĐ-NHNN_32111#body_context_29 (Loại: `body_context`)
> **[Quyết định]`<LOAI_VAN_BAN>`** số **[13/2008/QĐ-NHNN]`<SO_HIEU>`** ban hành **[ngày 29 tháng 04 năm 2008]`<NGAY_BAN_HANH>`** bởi **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_BAN_HANH>`** . **[Chương II]`<CHUONG>`** . **[Điều 8 . Hồ sơ , trình tự mở **[sở giao dịch]`<CO_QUAN_THAM_QUYEN>`** , chi nhánh , **[văn phòng đại diện]`<TO_CHUC_DOANH_NGHIEP>`** , **[đơn vị sự nghiệp]`<TO_CHUC_DOANH_NGHIEP>`** ở trong nước]`<DIEU>`**

**Thực thể:**
- `[e0]` **Quyết định** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **13/2008/QĐ-NHNN** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_BAN_HANH` (span: `[11:14]`)
- `[e3]` **ngày 29 tháng 04 năm 2008** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Chương II** → `CHUONG` (span: `[15:17]`)
- `[e5]` **Điều 8 . Hồ sơ , trình tự mở sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp ở trong nước** → `DIEU` (span: `[18:38]`)
- `[e6]` **sở giao dịch** → `CO_QUAN_THAM_QUYEN` (span: `[25:27]`) *(lồng trong `e5` (`DIEU`))*
- `[e7]` **văn phòng đại diện** → `TO_CHUC_DOANH_NGHIEP` (span: `[30:32]`) *(lồng trong `e5` (`DIEU`))*
- `[e8]` **đơn vị sự nghiệp** → `TO_CHUC_DOANH_NGHIEP` (span: `[33:35]`) *(lồng trong `e5` (`DIEU`))*

**Quan hệ:**
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Ngân hàng Nhà nước Việt Nam `[CO_QUAN_BAN_HANH]`)
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Quyết định `[LOAI_VAN_BAN]`)
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 29 tháng 04 năm 2008 `[NGAY_BAN_HANH]`)
- (`e4` Chương II `[CHUONG]`) ==[ **THUOC_VE** ]==> (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`)
- (`e5` Điều 8 . Hồ sơ , trình tự mở sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp ở trong nước `[DIEU]`) ==[ **THUOC_VE** ]==> (`e4` Chương II `[CHUONG]`)


---

### Mẫu #13_2008_QĐ-NHNN_32111#body_context_30 (Loại: `body_context`)
> **[Quyết định]`<LOAI_VAN_BAN>`** số **[13/2008/QĐ-NHNN]`<SO_HIEU>`** ban hành **[ngày 29 tháng 04 năm 2008]`<NGAY_BAN_HANH>`** bởi **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_BAN_HANH>`** . **[Điều 8]`<DIEU>`** . **[1 . **[Hồ sơ đề nghị]`<GIAY_TO_HO_SO>`** mở **[sở giao dịch]`<CO_QUAN_THAM_QUYEN>`** , chi nhánh , **[văn phòng đại diện]`<TO_CHUC_DOANH_NGHIEP>`** , **[đơn vị sự nghiệp]`<TO_CHUC_DOANH_NGHIEP>`** của **[ngân hàng thương mại]`<TO_CHUC_DOANH_NGHIEP>`** gửi về **[Ngân hàng Nhà nước chi nhánh tỉnh , thành phố]`<CO_QUAN_THAM_QUYEN>`** nơi **[ngân hàng thương mại]`<TO_CHUC_DOANH_NGHIEP>`** đặt trụ sở chính gồm :]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Quyết định** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **13/2008/QĐ-NHNN** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_BAN_HANH` (span: `[11:14]`)
- `[e3]` **ngày 29 tháng 04 năm 2008** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 8** → `DIEU` (span: `[15:17]`)
- `[e5]` **1 . Hồ sơ đề nghị mở sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp của ngân hàng thương mại gửi về Ngân hàng Nhà nước chi nhánh tỉnh , thành phố nơi ngân hàng thương mại đặt trụ sở chính gồm :** → `KHOAN` (span: `[18:52]`)
- `[e6]` **sở giao dịch** → `CO_QUAN_THAM_QUYEN` (span: `[23:25]`) *(lồng trong `e5` (`KHOAN`))*
- `[e7]` **ngân hàng thương mại** → `TO_CHUC_DOANH_NGHIEP` (span: `[34:36]`) *(lồng trong `e5` (`KHOAN`))*
- `[e8]` **ngân hàng thương mại** → `TO_CHUC_DOANH_NGHIEP` (span: `[45:47]`) *(lồng trong `e5` (`KHOAN`))*
- `[e9]` **văn phòng đại diện** → `TO_CHUC_DOANH_NGHIEP` (span: `[28:30]`) *(lồng trong `e5` (`KHOAN`))*
- `[e10]` **đơn vị sự nghiệp** → `TO_CHUC_DOANH_NGHIEP` (span: `[31:33]`) *(lồng trong `e5` (`KHOAN`))*
- `[e11]` **Ngân hàng Nhà nước chi nhánh tỉnh , thành phố** → `CO_QUAN_THAM_QUYEN` (span: `[38:44]`) *(lồng trong `e5` (`KHOAN`))*
- `[e12]` **Hồ sơ đề nghị** → `GIAY_TO_HO_SO` (span: `[20:22]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Ngân hàng Nhà nước Việt Nam `[CO_QUAN_BAN_HANH]`)
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Quyết định `[LOAI_VAN_BAN]`)
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 29 tháng 04 năm 2008 `[NGAY_BAN_HANH]`)
- (`e4` Điều 8 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`)
- (`e5` 1 . Hồ sơ đề nghị mở sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp của ngân hàng thương mại gửi về Ngân hàng Nhà nước chi nhánh tỉnh , thành phố nơi ngân hàng thương mại đặt trụ sở chính gồm : `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 8 `[DIEU]`)


---

### Mẫu #13_2008_QĐ-NHNN_32111#body_standalone_31 (Loại: `body_standalone`)
> **[Điều 8]`<DIEU>`** . **[1 . **[Hồ sơ đề nghị]`<GIAY_TO_HO_SO>`** mở **[sở giao dịch]`<CO_QUAN_THAM_QUYEN>`** , chi nhánh , **[văn phòng đại diện]`<TO_CHUC_DOANH_NGHIEP>`** , **[đơn vị sự nghiệp]`<TO_CHUC_DOANH_NGHIEP>`** của **[ngân hàng thương mại]`<TO_CHUC_DOANH_NGHIEP>`** gửi về **[Ngân hàng Nhà nước chi nhánh tỉnh , thành phố]`<CO_QUAN_THAM_QUYEN>`** nơi **[ngân hàng thương mại]`<TO_CHUC_DOANH_NGHIEP>`** đặt trụ sở chính gồm :]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 8** → `DIEU` (span: `[0:2]`)
- `[e1]` **1 . Hồ sơ đề nghị mở sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp của ngân hàng thương mại gửi về Ngân hàng Nhà nước chi nhánh tỉnh , thành phố nơi ngân hàng thương mại đặt trụ sở chính gồm :** → `KHOAN` (span: `[3:37]`)
- `[e2]` **sở giao dịch** → `CO_QUAN_THAM_QUYEN` (span: `[8:10]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **ngân hàng thương mại** → `TO_CHUC_DOANH_NGHIEP` (span: `[19:21]`) *(lồng trong `e1` (`KHOAN`))*
- `[e4]` **ngân hàng thương mại** → `TO_CHUC_DOANH_NGHIEP` (span: `[30:32]`) *(lồng trong `e1` (`KHOAN`))*
- `[e5]` **văn phòng đại diện** → `TO_CHUC_DOANH_NGHIEP` (span: `[13:15]`) *(lồng trong `e1` (`KHOAN`))*
- `[e6]` **đơn vị sự nghiệp** → `TO_CHUC_DOANH_NGHIEP` (span: `[16:18]`) *(lồng trong `e1` (`KHOAN`))*
- `[e7]` **Ngân hàng Nhà nước chi nhánh tỉnh , thành phố** → `CO_QUAN_THAM_QUYEN` (span: `[23:29]`) *(lồng trong `e1` (`KHOAN`))*
- `[e8]` **Hồ sơ đề nghị** → `GIAY_TO_HO_SO` (span: `[5:7]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 1 . Hồ sơ đề nghị mở sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp của ngân hàng thương mại gửi về Ngân hàng Nhà nước chi nhánh tỉnh , thành phố nơi ngân hàng thương mại đặt trụ sở chính gồm : `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 8 `[DIEU]`)


---

### Mẫu #13_2008_QĐ-NHNN_32111#body_context_32 (Loại: `body_context`)
> **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_BAN_HANH>`** ban hành **[Quyết định]`<LOAI_VAN_BAN>`** số **[13/2008/QĐ-NHNN]`<SO_HIEU>`** . **[Điều 8]`<DIEU>`** . **[Khoản 1]`<KHOAN>`** . **[a ) Văn bản của Chủ tịch **[Hội đồng quản trị]`<TO_CHUC_DOANH_NGHIEP>`** **[ngân hàng thương mại]`<TO_CHUC_DOANH_NGHIEP>`** đề nghị mở **[sở giao dịch]`<CO_QUAN_THAM_QUYEN>`** , chi nhánh , **[văn phòng đại diện]`<TO_CHUC_DOANH_NGHIEP>`** , **[đơn vị sự nghiệp]`<TO_CHUC_DOANH_NGHIEP>`** theo **[Phụ lục 01]`<THAM_CHIEU_PHAP_LY>`** kèm theo Quy định này ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Quyết định** → `LOAI_VAN_BAN` (span: `[4:5]`)
- `[e1]` **13/2008/QĐ-NHNN** → `SO_HIEU` (span: `[6:7]`)
- `[e2]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_BAN_HANH` (span: `[0:3]`)
- `[e3]` **Điều 8** → `DIEU` (span: `[8:10]`)
- `[e4]` **Khoản 1** → `KHOAN` (span: `[11:13]`)
- `[e5]` **a ) Văn bản của Chủ tịch Hội đồng quản trị ngân hàng thương mại đề nghị mở sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp theo Phụ lục 01 kèm theo Quy định này ;** → `DIEM` (span: `[14:43]`)
- `[e6]` **sở giao dịch** → `CO_QUAN_THAM_QUYEN` (span: `[25:27]`) *(lồng trong `e5` (`DIEM`))*
- `[e7]` **ngân hàng thương mại** → `TO_CHUC_DOANH_NGHIEP` (span: `[21:23]`) *(lồng trong `e5` (`DIEM`))*
- `[e8]` **văn phòng đại diện** → `TO_CHUC_DOANH_NGHIEP` (span: `[30:32]`) *(lồng trong `e5` (`DIEM`))*
- `[e9]` **đơn vị sự nghiệp** → `TO_CHUC_DOANH_NGHIEP` (span: `[33:35]`) *(lồng trong `e5` (`DIEM`))*
- `[e10]` **Phụ lục 01** → `THAM_CHIEU_PHAP_LY` (span: `[36:38]`) *(lồng trong `e5` (`DIEM`))*
- `[e11]` **Hội đồng quản trị** → `TO_CHUC_DOANH_NGHIEP` (span: `[19:21]`) *(lồng trong `e5` (`DIEM`))*

**Quan hệ:**
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Ngân hàng Nhà nước Việt Nam `[CO_QUAN_BAN_HANH]`)
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Quyết định `[LOAI_VAN_BAN]`)
- (`e3` Điều 8 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`)
- (`e4` Khoản 1 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 8 `[DIEU]`)
- (`e5` a ) Văn bản của Chủ tịch Hội đồng quản trị ngân hàng thương mại đề nghị mở sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp theo Phụ lục 01 kèm theo Quy định này ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e4` Khoản 1 `[KHOAN]`)
- (`e5` a ) Văn bản của Chủ tịch Hội đồng quản trị ngân hàng thương mại đề nghị mở sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp theo Phụ lục 01 kèm theo Quy định này ; `[DIEM]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e10` Phụ lục 01 `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #13_2008_QĐ-NHNN_32111#body_standalone_33 (Loại: `body_standalone`)
> **[Điều 8]`<DIEU>`** . **[Khoản 1]`<KHOAN>`** . **[a ) Văn bản của Chủ tịch **[Hội đồng quản trị]`<TO_CHUC_DOANH_NGHIEP>`** **[ngân hàng thương mại]`<TO_CHUC_DOANH_NGHIEP>`** đề nghị mở **[sở giao dịch]`<CO_QUAN_THAM_QUYEN>`** , chi nhánh , **[văn phòng đại diện]`<TO_CHUC_DOANH_NGHIEP>`** , **[đơn vị sự nghiệp]`<TO_CHUC_DOANH_NGHIEP>`** theo **[Phụ lục 01]`<THAM_CHIEU_PHAP_LY>`** kèm theo Quy định này ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Điều 8** → `DIEU` (span: `[0:2]`)
- `[e1]` **Khoản 1** → `KHOAN` (span: `[3:5]`)
- `[e2]` **a ) Văn bản của Chủ tịch Hội đồng quản trị ngân hàng thương mại đề nghị mở sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp theo Phụ lục 01 kèm theo Quy định này ;** → `DIEM` (span: `[6:35]`)
- `[e3]` **sở giao dịch** → `CO_QUAN_THAM_QUYEN` (span: `[17:19]`) *(lồng trong `e2` (`DIEM`))*
- `[e4]` **ngân hàng thương mại** → `TO_CHUC_DOANH_NGHIEP` (span: `[13:15]`) *(lồng trong `e2` (`DIEM`))*
- `[e5]` **văn phòng đại diện** → `TO_CHUC_DOANH_NGHIEP` (span: `[22:24]`) *(lồng trong `e2` (`DIEM`))*
- `[e6]` **đơn vị sự nghiệp** → `TO_CHUC_DOANH_NGHIEP` (span: `[25:27]`) *(lồng trong `e2` (`DIEM`))*
- `[e7]` **Phụ lục 01** → `THAM_CHIEU_PHAP_LY` (span: `[28:30]`) *(lồng trong `e2` (`DIEM`))*
- `[e8]` **Hội đồng quản trị** → `TO_CHUC_DOANH_NGHIEP` (span: `[11:13]`) *(lồng trong `e2` (`DIEM`))*

**Quan hệ:**
- (`e1` Khoản 1 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 8 `[DIEU]`)
- (`e2` a ) Văn bản của Chủ tịch Hội đồng quản trị ngân hàng thương mại đề nghị mở sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp theo Phụ lục 01 kèm theo Quy định này ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e1` Khoản 1 `[KHOAN]`)
- (`e2` a ) Văn bản của Chủ tịch Hội đồng quản trị ngân hàng thương mại đề nghị mở sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp theo Phụ lục 01 kèm theo Quy định này ; `[DIEM]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e7` Phụ lục 01 `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #13_2008_QĐ-NHNN_32111#body_context_34 (Loại: `body_context`)
> **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_BAN_HANH>`** ban hành **[Quyết định]`<LOAI_VAN_BAN>`** số **[13/2008/QĐ-NHNN]`<SO_HIEU>`** . **[Điều 8]`<DIEU>`** . **[2 . Trong thời hạn mười ngày làm việc kể từ ngày nhận đủ hồ sơ **[theo quy định tại]`<TU_KHOA_PHAP_LY>`** **[Khoản 1 Điều này]`<THAM_CHIEU_PHAP_LY>`** , **[Ngân hàng Nhà nước chi nhánh tỉnh , thành phố]`<CO_QUAN_THAM_QUYEN>`** nơi **[ngân hàng thương mại]`<TO_CHUC_DOANH_NGHIEP>`** đặt trụ sở chính gửi hồ sơ và báo cáo **[Ngân hàng Nhà nước]`<CO_QUAN_THAM_QUYEN>`** việc **[ngân hàng thương mại]`<TO_CHUC_DOANH_NGHIEP>`** đáp ứng các điều kiện mở **[sở giao dịch]`<CO_QUAN_THAM_QUYEN>`** , chi nhánh , **[văn phòng đại diện]`<TO_CHUC_DOANH_NGHIEP>`** , **[đơn vị sự nghiệp]`<TO_CHUC_DOANH_NGHIEP>`** và có ý kiến nêu rõ đồng ý hoặc không đồng ý việc mở **[sở giao dịch]`<CO_QUAN_THAM_QUYEN>`** ,]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Quyết định** → `LOAI_VAN_BAN` (span: `[4:5]`)
- `[e1]` **13/2008/QĐ-NHNN** → `SO_HIEU` (span: `[6:7]`)
- `[e2]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_BAN_HANH` (span: `[0:3]`)
- `[e3]` **Điều 8** → `DIEU` (span: `[8:10]`)
- `[e4]` **2 . Trong thời hạn mười ngày làm việc kể từ ngày nhận đủ hồ sơ theo quy định tại Khoản 1 Điều này , Ngân hàng Nhà nước chi nhánh tỉnh , thành phố nơi ngân hàng thương mại đặt trụ sở chính gửi hồ sơ và báo cáo Ngân hàng Nhà nước việc ngân hàng thương mại đáp ứng các điều kiện mở sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp và có ý kiến nêu rõ đồng ý hoặc không đồng ý việc mở sở giao dịch ,** → `KHOAN` (span: `[11:81]`)
- `[e5]` **sở giao dịch** → `CO_QUAN_THAM_QUYEN` (span: `[57:59]`) *(lồng trong `e4` (`KHOAN`))*
- `[e6]` **sở giao dịch** → `CO_QUAN_THAM_QUYEN` (span: `[78:80]`) *(lồng trong `e4` (`KHOAN`))*
- `[e7]` **ngân hàng thương mại** → `TO_CHUC_DOANH_NGHIEP` (span: `[39:41]`) *(lồng trong `e4` (`KHOAN`))*
- `[e8]` **ngân hàng thương mại** → `TO_CHUC_DOANH_NGHIEP` (span: `[51:53]`) *(lồng trong `e4` (`KHOAN`))*
- `[e9]` **văn phòng đại diện** → `TO_CHUC_DOANH_NGHIEP` (span: `[62:64]`) *(lồng trong `e4` (`KHOAN`))*
- `[e10]` **đơn vị sự nghiệp** → `TO_CHUC_DOANH_NGHIEP` (span: `[65:67]`) *(lồng trong `e4` (`KHOAN`))*
- `[e11]` **Khoản 1 Điều này** → `THAM_CHIEU_PHAP_LY` (span: `[27:31]`) *(lồng trong `e4` (`KHOAN`))*
- `[e12]` **theo quy định tại** → `TU_KHOA_PHAP_LY` (span: `[24:27]`) *(lồng trong `e4` (`KHOAN`))*
- `[e13]` **Ngân hàng Nhà nước chi nhánh tỉnh , thành phố** → `CO_QUAN_THAM_QUYEN` (span: `[32:38]`) *(lồng trong `e4` (`KHOAN`))*
- `[e14]` **Ngân hàng Nhà nước** → `CO_QUAN_THAM_QUYEN` (span: `[48:50]`) *(lồng trong `e4` (`KHOAN`))*

**Quan hệ:**
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Ngân hàng Nhà nước Việt Nam `[CO_QUAN_BAN_HANH]`)
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Quyết định `[LOAI_VAN_BAN]`)
- (`e3` Điều 8 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`)
- (`e4` 2 . Trong thời hạn mười ngày làm việc kể từ ngày nhận đủ hồ sơ theo quy định tại Khoản 1 Điều này , Ngân hàng Nhà nước chi nhánh tỉnh , thành phố nơi ngân hàng thương mại đặt trụ sở chính gửi hồ sơ và báo cáo Ngân hàng Nhà nước việc ngân hàng thương mại đáp ứng các điều kiện mở sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp và có ý kiến nêu rõ đồng ý hoặc không đồng ý việc mở sở giao dịch , `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 8 `[DIEU]`)
- (`e12` theo quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e11` Khoản 1 Điều này `[THAM_CHIEU_PHAP_LY]`)
- (`e4` 2 . Trong thời hạn mười ngày làm việc kể từ ngày nhận đủ hồ sơ theo quy định tại Khoản 1 Điều này , Ngân hàng Nhà nước chi nhánh tỉnh , thành phố nơi ngân hàng thương mại đặt trụ sở chính gửi hồ sơ và báo cáo Ngân hàng Nhà nước việc ngân hàng thương mại đáp ứng các điều kiện mở sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp và có ý kiến nêu rõ đồng ý hoặc không đồng ý việc mở sở giao dịch , `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e11` Khoản 1 Điều này `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #13_2008_QĐ-NHNN_32111#body_standalone_35 (Loại: `body_standalone`)
> **[Điều 8]`<DIEU>`** . **[2 . Trong thời hạn mười ngày làm việc kể từ ngày nhận đủ hồ sơ **[theo quy định tại]`<TU_KHOA_PHAP_LY>`** **[Khoản 1 Điều này]`<THAM_CHIEU_PHAP_LY>`** , **[Ngân hàng Nhà nước chi nhánh tỉnh , thành phố]`<CO_QUAN_THAM_QUYEN>`** nơi **[ngân hàng thương mại]`<TO_CHUC_DOANH_NGHIEP>`** đặt trụ sở chính gửi hồ sơ và báo cáo **[Ngân hàng Nhà nước]`<CO_QUAN_THAM_QUYEN>`** việc **[ngân hàng thương mại]`<TO_CHUC_DOANH_NGHIEP>`** đáp ứng các điều kiện mở **[sở giao dịch]`<CO_QUAN_THAM_QUYEN>`** , chi nhánh , **[văn phòng đại diện]`<TO_CHUC_DOANH_NGHIEP>`** , **[đơn vị sự nghiệp]`<TO_CHUC_DOANH_NGHIEP>`** và có ý kiến nêu rõ đồng ý hoặc không đồng ý việc mở **[sở giao dịch]`<CO_QUAN_THAM_QUYEN>`** ,]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 8** → `DIEU` (span: `[0:2]`)
- `[e1]` **2 . Trong thời hạn mười ngày làm việc kể từ ngày nhận đủ hồ sơ theo quy định tại Khoản 1 Điều này , Ngân hàng Nhà nước chi nhánh tỉnh , thành phố nơi ngân hàng thương mại đặt trụ sở chính gửi hồ sơ và báo cáo Ngân hàng Nhà nước việc ngân hàng thương mại đáp ứng các điều kiện mở sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp và có ý kiến nêu rõ đồng ý hoặc không đồng ý việc mở sở giao dịch ,** → `KHOAN` (span: `[3:73]`)
- `[e2]` **sở giao dịch** → `CO_QUAN_THAM_QUYEN` (span: `[49:51]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **sở giao dịch** → `CO_QUAN_THAM_QUYEN` (span: `[70:72]`) *(lồng trong `e1` (`KHOAN`))*
- `[e4]` **ngân hàng thương mại** → `TO_CHUC_DOANH_NGHIEP` (span: `[31:33]`) *(lồng trong `e1` (`KHOAN`))*
- `[e5]` **ngân hàng thương mại** → `TO_CHUC_DOANH_NGHIEP` (span: `[43:45]`) *(lồng trong `e1` (`KHOAN`))*
- `[e6]` **văn phòng đại diện** → `TO_CHUC_DOANH_NGHIEP` (span: `[54:56]`) *(lồng trong `e1` (`KHOAN`))*
- `[e7]` **đơn vị sự nghiệp** → `TO_CHUC_DOANH_NGHIEP` (span: `[57:59]`) *(lồng trong `e1` (`KHOAN`))*
- `[e8]` **Khoản 1 Điều này** → `THAM_CHIEU_PHAP_LY` (span: `[19:23]`) *(lồng trong `e1` (`KHOAN`))*
- `[e9]` **theo quy định tại** → `TU_KHOA_PHAP_LY` (span: `[16:19]`) *(lồng trong `e1` (`KHOAN`))*
- `[e10]` **Ngân hàng Nhà nước chi nhánh tỉnh , thành phố** → `CO_QUAN_THAM_QUYEN` (span: `[24:30]`) *(lồng trong `e1` (`KHOAN`))*
- `[e11]` **Ngân hàng Nhà nước** → `CO_QUAN_THAM_QUYEN` (span: `[40:42]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 2 . Trong thời hạn mười ngày làm việc kể từ ngày nhận đủ hồ sơ theo quy định tại Khoản 1 Điều này , Ngân hàng Nhà nước chi nhánh tỉnh , thành phố nơi ngân hàng thương mại đặt trụ sở chính gửi hồ sơ và báo cáo Ngân hàng Nhà nước việc ngân hàng thương mại đáp ứng các điều kiện mở sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp và có ý kiến nêu rõ đồng ý hoặc không đồng ý việc mở sở giao dịch , `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 8 `[DIEU]`)
- (`e9` theo quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e8` Khoản 1 Điều này `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 2 . Trong thời hạn mười ngày làm việc kể từ ngày nhận đủ hồ sơ theo quy định tại Khoản 1 Điều này , Ngân hàng Nhà nước chi nhánh tỉnh , thành phố nơi ngân hàng thương mại đặt trụ sở chính gửi hồ sơ và báo cáo Ngân hàng Nhà nước việc ngân hàng thương mại đáp ứng các điều kiện mở sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp và có ý kiến nêu rõ đồng ý hoặc không đồng ý việc mở sở giao dịch , `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e8` Khoản 1 Điều này `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #13_2008_QĐ-NHNN_32111#body_context_36 (Loại: `body_context`)
> **[Quyết định]`<LOAI_VAN_BAN>`** số **[13/2008/QĐ-NHNN]`<SO_HIEU>`** ban hành **[ngày 29 tháng 04 năm 2008]`<NGAY_BAN_HANH>`** bởi **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_BAN_HANH>`** . **[Điều 8]`<DIEU>`** . **[3 . Trong thời hạn ba mươi ngày làm việc kể từ ngày nhận được hồ sơ và báo cáo của **[Ngân hàng Nhà nước chi nhánh tỉnh , thành phố]`<CO_QUAN_THAM_QUYEN>`** nơi **[ngân hàng thương mại]`<TO_CHUC_DOANH_NGHIEP>`** đặt trụ sở chính **[quy định tại]`<TU_KHOA_PHAP_LY>`** **[Khoản 2 Điều này]`<THAM_CHIEU_PHAP_LY>`** , **[Ngân hàng Nhà nước]`<CO_QUAN_THAM_QUYEN>`** có **[văn bản chấp thuận]`<GIAY_TO_HO_SO>`** đề nghị mở **[sở giao dịch]`<CO_QUAN_THAM_QUYEN>`** , chi nhánh , **[văn phòng đại diện]`<TO_CHUC_DOANH_NGHIEP>`** , **[đơn vị sự nghiệp]`<TO_CHUC_DOANH_NGHIEP>`** theo **[Phụ lục 02]`<THAM_CHIEU_PHAP_LY>`** kèm theo Quy định này ; trường hợp không chấp thuận , có văn bản nêu rõ lý do hoặc]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Quyết định** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **13/2008/QĐ-NHNN** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_BAN_HANH` (span: `[11:14]`)
- `[e3]` **ngày 29 tháng 04 năm 2008** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 8** → `DIEU` (span: `[15:17]`)
- `[e5]` **3 . Trong thời hạn ba mươi ngày làm việc kể từ ngày nhận được hồ sơ và báo cáo của Ngân hàng Nhà nước chi nhánh tỉnh , thành phố nơi ngân hàng thương mại đặt trụ sở chính quy định tại Khoản 2 Điều này , Ngân hàng Nhà nước có văn bản chấp thuận đề nghị mở sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp theo Phụ lục 02 kèm theo Quy định này ; trường hợp không chấp thuận , có văn bản nêu rõ lý do hoặc** → `KHOAN` (span: `[18:89]`)
- `[e6]` **sở giao dịch** → `CO_QUAN_THAM_QUYEN` (span: `[61:63]`) *(lồng trong `e5` (`KHOAN`))*
- `[e7]` **ngân hàng thương mại** → `TO_CHUC_DOANH_NGHIEP` (span: `[42:44]`) *(lồng trong `e5` (`KHOAN`))*
- `[e8]` **văn phòng đại diện** → `TO_CHUC_DOANH_NGHIEP` (span: `[66:68]`) *(lồng trong `e5` (`KHOAN`))*
- `[e9]` **đơn vị sự nghiệp** → `TO_CHUC_DOANH_NGHIEP` (span: `[69:71]`) *(lồng trong `e5` (`KHOAN`))*
- `[e10]` **Khoản 2 Điều này** → `THAM_CHIEU_PHAP_LY` (span: `[49:53]`) *(lồng trong `e5` (`KHOAN`))*
- `[e11]` **Phụ lục 02** → `THAM_CHIEU_PHAP_LY` (span: `[72:74]`) *(lồng trong `e5` (`KHOAN`))*
- `[e12]` **quy định tại** → `TU_KHOA_PHAP_LY` (span: `[47:49]`) *(lồng trong `e5` (`KHOAN`))*
- `[e13]` **Ngân hàng Nhà nước chi nhánh tỉnh , thành phố** → `CO_QUAN_THAM_QUYEN` (span: `[35:41]`) *(lồng trong `e5` (`KHOAN`))*
- `[e14]` **Ngân hàng Nhà nước** → `CO_QUAN_THAM_QUYEN` (span: `[54:56]`) *(lồng trong `e5` (`KHOAN`))*
- `[e15]` **văn bản chấp thuận** → `GIAY_TO_HO_SO` (span: `[57:59]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Ngân hàng Nhà nước Việt Nam `[CO_QUAN_BAN_HANH]`)
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Quyết định `[LOAI_VAN_BAN]`)
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 29 tháng 04 năm 2008 `[NGAY_BAN_HANH]`)
- (`e4` Điều 8 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`)
- (`e5` 3 . Trong thời hạn ba mươi ngày làm việc kể từ ngày nhận được hồ sơ và báo cáo của Ngân hàng Nhà nước chi nhánh tỉnh , thành phố nơi ngân hàng thương mại đặt trụ sở chính quy định tại Khoản 2 Điều này , Ngân hàng Nhà nước có văn bản chấp thuận đề nghị mở sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp theo Phụ lục 02 kèm theo Quy định này ; trường hợp không chấp thuận , có văn bản nêu rõ lý do hoặc `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 8 `[DIEU]`)
- (`e12` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e10` Khoản 2 Điều này `[THAM_CHIEU_PHAP_LY]`)
- (`e5` 3 . Trong thời hạn ba mươi ngày làm việc kể từ ngày nhận được hồ sơ và báo cáo của Ngân hàng Nhà nước chi nhánh tỉnh , thành phố nơi ngân hàng thương mại đặt trụ sở chính quy định tại Khoản 2 Điều này , Ngân hàng Nhà nước có văn bản chấp thuận đề nghị mở sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp theo Phụ lục 02 kèm theo Quy định này ; trường hợp không chấp thuận , có văn bản nêu rõ lý do hoặc `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e10` Khoản 2 Điều này `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e12` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e11` Phụ lục 02 `[THAM_CHIEU_PHAP_LY]`)
- (`e5` 3 . Trong thời hạn ba mươi ngày làm việc kể từ ngày nhận được hồ sơ và báo cáo của Ngân hàng Nhà nước chi nhánh tỉnh , thành phố nơi ngân hàng thương mại đặt trụ sở chính quy định tại Khoản 2 Điều này , Ngân hàng Nhà nước có văn bản chấp thuận đề nghị mở sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp theo Phụ lục 02 kèm theo Quy định này ; trường hợp không chấp thuận , có văn bản nêu rõ lý do hoặc `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e11` Phụ lục 02 `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #13_2008_QĐ-NHNN_32111#body_standalone_37 (Loại: `body_standalone`)
> **[Điều 8]`<DIEU>`** . **[3 . Trong thời hạn ba mươi ngày làm việc kể từ ngày nhận được hồ sơ và báo cáo của **[Ngân hàng Nhà nước chi nhánh tỉnh , thành phố]`<CO_QUAN_THAM_QUYEN>`** nơi **[ngân hàng thương mại]`<TO_CHUC_DOANH_NGHIEP>`** đặt trụ sở chính **[quy định tại]`<TU_KHOA_PHAP_LY>`** **[Khoản 2 Điều này]`<THAM_CHIEU_PHAP_LY>`** , **[Ngân hàng Nhà nước]`<CO_QUAN_THAM_QUYEN>`** có **[văn bản chấp thuận]`<GIAY_TO_HO_SO>`** đề nghị mở **[sở giao dịch]`<CO_QUAN_THAM_QUYEN>`** , chi nhánh , **[văn phòng đại diện]`<TO_CHUC_DOANH_NGHIEP>`** , **[đơn vị sự nghiệp]`<TO_CHUC_DOANH_NGHIEP>`** theo **[Phụ lục 02]`<THAM_CHIEU_PHAP_LY>`** kèm theo Quy định này ; trường hợp không chấp thuận , có văn bản nêu rõ lý do hoặc]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 8** → `DIEU` (span: `[0:2]`)
- `[e1]` **3 . Trong thời hạn ba mươi ngày làm việc kể từ ngày nhận được hồ sơ và báo cáo của Ngân hàng Nhà nước chi nhánh tỉnh , thành phố nơi ngân hàng thương mại đặt trụ sở chính quy định tại Khoản 2 Điều này , Ngân hàng Nhà nước có văn bản chấp thuận đề nghị mở sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp theo Phụ lục 02 kèm theo Quy định này ; trường hợp không chấp thuận , có văn bản nêu rõ lý do hoặc** → `KHOAN` (span: `[3:74]`)
- `[e2]` **sở giao dịch** → `CO_QUAN_THAM_QUYEN` (span: `[46:48]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **ngân hàng thương mại** → `TO_CHUC_DOANH_NGHIEP` (span: `[27:29]`) *(lồng trong `e1` (`KHOAN`))*
- `[e4]` **văn phòng đại diện** → `TO_CHUC_DOANH_NGHIEP` (span: `[51:53]`) *(lồng trong `e1` (`KHOAN`))*
- `[e5]` **đơn vị sự nghiệp** → `TO_CHUC_DOANH_NGHIEP` (span: `[54:56]`) *(lồng trong `e1` (`KHOAN`))*
- `[e6]` **Khoản 2 Điều này** → `THAM_CHIEU_PHAP_LY` (span: `[34:38]`) *(lồng trong `e1` (`KHOAN`))*
- `[e7]` **Phụ lục 02** → `THAM_CHIEU_PHAP_LY` (span: `[57:59]`) *(lồng trong `e1` (`KHOAN`))*
- `[e8]` **quy định tại** → `TU_KHOA_PHAP_LY` (span: `[32:34]`) *(lồng trong `e1` (`KHOAN`))*
- `[e9]` **Ngân hàng Nhà nước chi nhánh tỉnh , thành phố** → `CO_QUAN_THAM_QUYEN` (span: `[20:26]`) *(lồng trong `e1` (`KHOAN`))*
- `[e10]` **Ngân hàng Nhà nước** → `CO_QUAN_THAM_QUYEN` (span: `[39:41]`) *(lồng trong `e1` (`KHOAN`))*
- `[e11]` **văn bản chấp thuận** → `GIAY_TO_HO_SO` (span: `[42:44]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 3 . Trong thời hạn ba mươi ngày làm việc kể từ ngày nhận được hồ sơ và báo cáo của Ngân hàng Nhà nước chi nhánh tỉnh , thành phố nơi ngân hàng thương mại đặt trụ sở chính quy định tại Khoản 2 Điều này , Ngân hàng Nhà nước có văn bản chấp thuận đề nghị mở sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp theo Phụ lục 02 kèm theo Quy định này ; trường hợp không chấp thuận , có văn bản nêu rõ lý do hoặc `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 8 `[DIEU]`)
- (`e8` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e6` Khoản 2 Điều này `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 3 . Trong thời hạn ba mươi ngày làm việc kể từ ngày nhận được hồ sơ và báo cáo của Ngân hàng Nhà nước chi nhánh tỉnh , thành phố nơi ngân hàng thương mại đặt trụ sở chính quy định tại Khoản 2 Điều này , Ngân hàng Nhà nước có văn bản chấp thuận đề nghị mở sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp theo Phụ lục 02 kèm theo Quy định này ; trường hợp không chấp thuận , có văn bản nêu rõ lý do hoặc `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e6` Khoản 2 Điều này `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e8` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e7` Phụ lục 02 `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 3 . Trong thời hạn ba mươi ngày làm việc kể từ ngày nhận được hồ sơ và báo cáo của Ngân hàng Nhà nước chi nhánh tỉnh , thành phố nơi ngân hàng thương mại đặt trụ sở chính quy định tại Khoản 2 Điều này , Ngân hàng Nhà nước có văn bản chấp thuận đề nghị mở sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp theo Phụ lục 02 kèm theo Quy định này ; trường hợp không chấp thuận , có văn bản nêu rõ lý do hoặc `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e7` Phụ lục 02 `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #13_2008_QĐ-NHNN_32111#body_context_38 (Loại: `body_context`)
> **[Quyết định]`<LOAI_VAN_BAN>`** số **[13/2008/QĐ-NHNN]`<SO_HIEU>`** của **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Ngân hàng]`<LINH_VUC>`** . **[Điều 8]`<DIEU>`** . **[4 . Trong thời hạn mười lăm ngày làm việc kể từ ngày có **[văn bản chấp thuận]`<GIAY_TO_HO_SO>`** của **[Ngân hàng Nhà nước]`<CO_QUAN_THAM_QUYEN>`** , Chủ tịch **[Hội đồng quản trị]`<TO_CHUC_DOANH_NGHIEP>`** **[ngân hàng thương mại]`<TO_CHUC_DOANH_NGHIEP>`** phải ra quyết định mở **[sở giao dịch]`<CO_QUAN_THAM_QUYEN>`** , chi nhánh , **[văn phòng đại diện]`<TO_CHUC_DOANH_NGHIEP>`** , **[đơn vị sự nghiệp]`<TO_CHUC_DOANH_NGHIEP>`** .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Quyết định** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **13/2008/QĐ-NHNN** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_BAN_HANH` (span: `[4:7]`)
- `[e3]` **Ngân hàng** → `LINH_VUC` (span: `[9:10]`)
- `[e4]` **Điều 8** → `DIEU` (span: `[11:13]`)
- `[e5]` **4 . Trong thời hạn mười lăm ngày làm việc kể từ ngày có văn bản chấp thuận của Ngân hàng Nhà nước , Chủ tịch Hội đồng quản trị ngân hàng thương mại phải ra quyết định mở sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp .** → `KHOAN` (span: `[14:52]`)
- `[e6]` **sở giao dịch** → `CO_QUAN_THAM_QUYEN` (span: `[41:43]`) *(lồng trong `e5` (`KHOAN`))*
- `[e7]` **ngân hàng thương mại** → `TO_CHUC_DOANH_NGHIEP` (span: `[35:37]`) *(lồng trong `e5` (`KHOAN`))*
- `[e8]` **văn phòng đại diện** → `TO_CHUC_DOANH_NGHIEP` (span: `[46:48]`) *(lồng trong `e5` (`KHOAN`))*
- `[e9]` **đơn vị sự nghiệp** → `TO_CHUC_DOANH_NGHIEP` (span: `[49:51]`) *(lồng trong `e5` (`KHOAN`))*
- `[e10]` **Ngân hàng Nhà nước** → `CO_QUAN_THAM_QUYEN` (span: `[29:31]`) *(lồng trong `e5` (`KHOAN`))*
- `[e11]` **văn bản chấp thuận** → `GIAY_TO_HO_SO` (span: `[26:28]`) *(lồng trong `e5` (`KHOAN`))*
- `[e12]` **Hội đồng quản trị** → `TO_CHUC_DOANH_NGHIEP` (span: `[33:35]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Ngân hàng Nhà nước Việt Nam `[CO_QUAN_BAN_HANH]`)
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Quyết định `[LOAI_VAN_BAN]`)
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Ngân hàng `[LINH_VUC]`)
- (`e4` Điều 8 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`)
- (`e5` 4 . Trong thời hạn mười lăm ngày làm việc kể từ ngày có văn bản chấp thuận của Ngân hàng Nhà nước , Chủ tịch Hội đồng quản trị ngân hàng thương mại phải ra quyết định mở sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 8 `[DIEU]`)
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Ngân hàng `[LINH_VUC]`)
- (`e5` 4 . Trong thời hạn mười lăm ngày làm việc kể từ ngày có văn bản chấp thuận của Ngân hàng Nhà nước , Chủ tịch Hội đồng quản trị ngân hàng thương mại phải ra quyết định mở sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp . `[KHOAN]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Ngân hàng `[LINH_VUC]`)


---

### Mẫu #13_2008_QĐ-NHNN_32111#body_standalone_39 (Loại: `body_standalone`)
> **[Điều 8]`<DIEU>`** . **[4 . Trong thời hạn mười lăm ngày làm việc kể từ ngày có **[văn bản chấp thuận]`<GIAY_TO_HO_SO>`** của **[Ngân hàng Nhà nước]`<CO_QUAN_THAM_QUYEN>`** , Chủ tịch **[Hội đồng quản trị]`<TO_CHUC_DOANH_NGHIEP>`** **[ngân hàng thương mại]`<TO_CHUC_DOANH_NGHIEP>`** phải ra quyết định mở **[sở giao dịch]`<CO_QUAN_THAM_QUYEN>`** , chi nhánh , **[văn phòng đại diện]`<TO_CHUC_DOANH_NGHIEP>`** , **[đơn vị sự nghiệp]`<TO_CHUC_DOANH_NGHIEP>`** .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 8** → `DIEU` (span: `[0:2]`)
- `[e1]` **4 . Trong thời hạn mười lăm ngày làm việc kể từ ngày có văn bản chấp thuận của Ngân hàng Nhà nước , Chủ tịch Hội đồng quản trị ngân hàng thương mại phải ra quyết định mở sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp .** → `KHOAN` (span: `[3:41]`)
- `[e2]` **sở giao dịch** → `CO_QUAN_THAM_QUYEN` (span: `[30:32]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **ngân hàng thương mại** → `TO_CHUC_DOANH_NGHIEP` (span: `[24:26]`) *(lồng trong `e1` (`KHOAN`))*
- `[e4]` **văn phòng đại diện** → `TO_CHUC_DOANH_NGHIEP` (span: `[35:37]`) *(lồng trong `e1` (`KHOAN`))*
- `[e5]` **đơn vị sự nghiệp** → `TO_CHUC_DOANH_NGHIEP` (span: `[38:40]`) *(lồng trong `e1` (`KHOAN`))*
- `[e6]` **Ngân hàng Nhà nước** → `CO_QUAN_THAM_QUYEN` (span: `[18:20]`) *(lồng trong `e1` (`KHOAN`))*
- `[e7]` **văn bản chấp thuận** → `GIAY_TO_HO_SO` (span: `[15:17]`) *(lồng trong `e1` (`KHOAN`))*
- `[e8]` **Hội đồng quản trị** → `TO_CHUC_DOANH_NGHIEP` (span: `[22:24]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 4 . Trong thời hạn mười lăm ngày làm việc kể từ ngày có văn bản chấp thuận của Ngân hàng Nhà nước , Chủ tịch Hội đồng quản trị ngân hàng thương mại phải ra quyết định mở sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 8 `[DIEU]`)


---

### Mẫu #13_2008_QĐ-NHNN_32111#body_context_40 (Loại: `body_context`)
> **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_BAN_HANH>`** ban hành **[Quyết định]`<LOAI_VAN_BAN>`** số **[13/2008/QĐ-NHNN]`<SO_HIEU>`** . **[Điều 9]`<DIEU>`** . **[Khoản 1]`<KHOAN>`** . **[b ) Có đủ cơ sở vật chất đáp ứng yêu cầu hoạt động : có trụ sở , kho quỹ , hệ thống thông tin quản lý , **[phương tiện]`<TAI_SAN_VAT_CHAT>`** điều chuyển tiền theo quy định của **[Ngân hàng Nhà nước]`<CO_QUAN_THAM_QUYEN>`** ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Quyết định** → `LOAI_VAN_BAN` (span: `[4:5]`)
- `[e1]` **13/2008/QĐ-NHNN** → `SO_HIEU` (span: `[6:7]`)
- `[e2]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_BAN_HANH` (span: `[0:3]`)
- `[e3]` **Điều 9** → `DIEU` (span: `[8:10]`)
- `[e4]` **Khoản 1** → `KHOAN` (span: `[11:13]`)
- `[e5]` **b ) Có đủ cơ sở vật chất đáp ứng yêu cầu hoạt động : có trụ sở , kho quỹ , hệ thống thông tin quản lý , phương tiện điều chuyển tiền theo quy định của Ngân hàng Nhà nước ;** → `DIEM` (span: `[14:42]`)
- `[e6]` **Ngân hàng Nhà nước** → `CO_QUAN_THAM_QUYEN` (span: `[39:41]`) *(lồng trong `e5` (`DIEM`))*
- `[e7]` **phương tiện** → `TAI_SAN_VAT_CHAT` (span: `[33:34]`) *(lồng trong `e5` (`DIEM`))*

**Quan hệ:**
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Ngân hàng Nhà nước Việt Nam `[CO_QUAN_BAN_HANH]`)
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Quyết định `[LOAI_VAN_BAN]`)
- (`e3` Điều 9 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`)
- (`e4` Khoản 1 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 9 `[DIEU]`)
- (`e5` b ) Có đủ cơ sở vật chất đáp ứng yêu cầu hoạt động : có trụ sở , kho quỹ , hệ thống thông tin quản lý , phương tiện điều chuyển tiền theo quy định của Ngân hàng Nhà nước ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e4` Khoản 1 `[KHOAN]`)


---

### Mẫu #13_2008_QĐ-NHNN_32111#body_standalone_41 (Loại: `body_standalone`)
> **[Điều 9]`<DIEU>`** . **[Khoản 1]`<KHOAN>`** . **[b ) Có đủ cơ sở vật chất đáp ứng yêu cầu hoạt động : có trụ sở , kho quỹ , hệ thống thông tin quản lý , **[phương tiện]`<TAI_SAN_VAT_CHAT>`** điều chuyển tiền theo quy định của **[Ngân hàng Nhà nước]`<CO_QUAN_THAM_QUYEN>`** ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Điều 9** → `DIEU` (span: `[0:2]`)
- `[e1]` **Khoản 1** → `KHOAN` (span: `[3:5]`)
- `[e2]` **b ) Có đủ cơ sở vật chất đáp ứng yêu cầu hoạt động : có trụ sở , kho quỹ , hệ thống thông tin quản lý , phương tiện điều chuyển tiền theo quy định của Ngân hàng Nhà nước ;** → `DIEM` (span: `[6:34]`)
- `[e3]` **Ngân hàng Nhà nước** → `CO_QUAN_THAM_QUYEN` (span: `[31:33]`) *(lồng trong `e2` (`DIEM`))*
- `[e4]` **phương tiện** → `TAI_SAN_VAT_CHAT` (span: `[25:26]`) *(lồng trong `e2` (`DIEM`))*

**Quan hệ:**
- (`e1` Khoản 1 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 9 `[DIEU]`)
- (`e2` b ) Có đủ cơ sở vật chất đáp ứng yêu cầu hoạt động : có trụ sở , kho quỹ , hệ thống thông tin quản lý , phương tiện điều chuyển tiền theo quy định của Ngân hàng Nhà nước ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e1` Khoản 1 `[KHOAN]`)


---

### Mẫu #13_2008_QĐ-NHNN_32111#body_context_42 (Loại: `body_context`)
> **[Quyết định]`<LOAI_VAN_BAN>`** số **[13/2008/QĐ-NHNN]`<SO_HIEU>`** ban hành **[ngày 29 tháng 04 năm 2008]`<NGAY_BAN_HANH>`** bởi **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_BAN_HANH>`** . **[Điều 9]`<DIEU>`** . **[2 . Trước ngày khai trương hoạt động **[sở giao dịch]`<CO_QUAN_THAM_QUYEN>`** , chi nhánh , **[văn phòng đại diện]`<TO_CHUC_DOANH_NGHIEP>`** , **[đơn vị sự nghiệp]`<TO_CHUC_DOANH_NGHIEP>`** mười lăm ngày làm việc , **[ngân hàng thương mại]`<TO_CHUC_DOANH_NGHIEP>`** phải đăng báo theo quy định của pháp luật ; có văn bản gửi **[Ngân hàng Nhà nước]`<CO_QUAN_THAM_QUYEN>`** và **[Ngân hàng Nhà nước chi nhánh tỉnh , thành phố]`<CO_QUAN_THAM_QUYEN>`** nơi mở **[sở giao dịch]`<CO_QUAN_THAM_QUYEN>`** , chi nhánh , **[văn phòng đại diện]`<TO_CHUC_DOANH_NGHIEP>`** , **[đơn vị sự nghiệp]`<TO_CHUC_DOANH_NGHIEP>`** báo cáo việc đáp ứng các điều kiện **[quy định tại]`<TU_KHOA_PHAP_LY>`** **[khoản 1 Điều này]`<THAM_CHIEU_PHAP_LY>`** kèm theo bản sao đăng ký]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Quyết định** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **13/2008/QĐ-NHNN** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_BAN_HANH` (span: `[11:14]`)
- `[e3]` **ngày 29 tháng 04 năm 2008** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 9** → `DIEU` (span: `[15:17]`)
- `[e5]` **2 . Trước ngày khai trương hoạt động sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp mười lăm ngày làm việc , ngân hàng thương mại phải đăng báo theo quy định của pháp luật ; có văn bản gửi Ngân hàng Nhà nước và Ngân hàng Nhà nước chi nhánh tỉnh , thành phố nơi mở sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp báo cáo việc đáp ứng các điều kiện quy định tại khoản 1 Điều này kèm theo bản sao đăng ký** → `KHOAN` (span: `[18:88]`)
- `[e6]` **sở giao dịch** → `CO_QUAN_THAM_QUYEN` (span: `[24:26]`) *(lồng trong `e5` (`KHOAN`))*
- `[e7]` **sở giao dịch** → `CO_QUAN_THAM_QUYEN` (span: `[63:65]`) *(lồng trong `e5` (`KHOAN`))*
- `[e8]` **ngân hàng thương mại** → `TO_CHUC_DOANH_NGHIEP` (span: `[39:41]`) *(lồng trong `e5` (`KHOAN`))*
- `[e9]` **văn phòng đại diện** → `TO_CHUC_DOANH_NGHIEP` (span: `[29:31]`) *(lồng trong `e5` (`KHOAN`))*
- `[e10]` **văn phòng đại diện** → `TO_CHUC_DOANH_NGHIEP` (span: `[68:70]`) *(lồng trong `e5` (`KHOAN`))*
- `[e11]` **đơn vị sự nghiệp** → `TO_CHUC_DOANH_NGHIEP` (span: `[32:34]`) *(lồng trong `e5` (`KHOAN`))*
- `[e12]` **đơn vị sự nghiệp** → `TO_CHUC_DOANH_NGHIEP` (span: `[71:73]`) *(lồng trong `e5` (`KHOAN`))*
- `[e13]` **khoản 1 Điều này** → `THAM_CHIEU_PHAP_LY` (span: `[80:84]`) *(lồng trong `e5` (`KHOAN`))*
- `[e14]` **quy định tại** → `TU_KHOA_PHAP_LY` (span: `[78:80]`) *(lồng trong `e5` (`KHOAN`))*
- `[e15]` **Ngân hàng Nhà nước** → `CO_QUAN_THAM_QUYEN` (span: `[52:54]`) *(lồng trong `e5` (`KHOAN`))*
- `[e16]` **Ngân hàng Nhà nước chi nhánh tỉnh , thành phố** → `CO_QUAN_THAM_QUYEN` (span: `[55:61]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Ngân hàng Nhà nước Việt Nam `[CO_QUAN_BAN_HANH]`)
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Quyết định `[LOAI_VAN_BAN]`)
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 29 tháng 04 năm 2008 `[NGAY_BAN_HANH]`)
- (`e4` Điều 9 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`)
- (`e5` 2 . Trước ngày khai trương hoạt động sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp mười lăm ngày làm việc , ngân hàng thương mại phải đăng báo theo quy định của pháp luật ; có văn bản gửi Ngân hàng Nhà nước và Ngân hàng Nhà nước chi nhánh tỉnh , thành phố nơi mở sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp báo cáo việc đáp ứng các điều kiện quy định tại khoản 1 Điều này kèm theo bản sao đăng ký `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 9 `[DIEU]`)
- (`e14` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e13` khoản 1 Điều này `[THAM_CHIEU_PHAP_LY]`)
- (`e5` 2 . Trước ngày khai trương hoạt động sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp mười lăm ngày làm việc , ngân hàng thương mại phải đăng báo theo quy định của pháp luật ; có văn bản gửi Ngân hàng Nhà nước và Ngân hàng Nhà nước chi nhánh tỉnh , thành phố nơi mở sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp báo cáo việc đáp ứng các điều kiện quy định tại khoản 1 Điều này kèm theo bản sao đăng ký `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e13` khoản 1 Điều này `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #13_2008_QĐ-NHNN_32111#body_standalone_43 (Loại: `body_standalone`)
> **[Điều 9]`<DIEU>`** . **[2 . Trước ngày khai trương hoạt động **[sở giao dịch]`<CO_QUAN_THAM_QUYEN>`** , chi nhánh , **[văn phòng đại diện]`<TO_CHUC_DOANH_NGHIEP>`** , **[đơn vị sự nghiệp]`<TO_CHUC_DOANH_NGHIEP>`** mười lăm ngày làm việc , **[ngân hàng thương mại]`<TO_CHUC_DOANH_NGHIEP>`** phải đăng báo theo quy định của pháp luật ; có văn bản gửi **[Ngân hàng Nhà nước]`<CO_QUAN_THAM_QUYEN>`** và **[Ngân hàng Nhà nước chi nhánh tỉnh , thành phố]`<CO_QUAN_THAM_QUYEN>`** nơi mở **[sở giao dịch]`<CO_QUAN_THAM_QUYEN>`** , chi nhánh , **[văn phòng đại diện]`<TO_CHUC_DOANH_NGHIEP>`** , **[đơn vị sự nghiệp]`<TO_CHUC_DOANH_NGHIEP>`** báo cáo việc đáp ứng các điều kiện **[quy định tại]`<TU_KHOA_PHAP_LY>`** **[khoản 1 Điều này]`<THAM_CHIEU_PHAP_LY>`** kèm theo bản sao đăng ký]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 9** → `DIEU` (span: `[0:2]`)
- `[e1]` **2 . Trước ngày khai trương hoạt động sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp mười lăm ngày làm việc , ngân hàng thương mại phải đăng báo theo quy định của pháp luật ; có văn bản gửi Ngân hàng Nhà nước và Ngân hàng Nhà nước chi nhánh tỉnh , thành phố nơi mở sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp báo cáo việc đáp ứng các điều kiện quy định tại khoản 1 Điều này kèm theo bản sao đăng ký** → `KHOAN` (span: `[3:73]`)
- `[e2]` **sở giao dịch** → `CO_QUAN_THAM_QUYEN` (span: `[9:11]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **sở giao dịch** → `CO_QUAN_THAM_QUYEN` (span: `[48:50]`) *(lồng trong `e1` (`KHOAN`))*
- `[e4]` **ngân hàng thương mại** → `TO_CHUC_DOANH_NGHIEP` (span: `[24:26]`) *(lồng trong `e1` (`KHOAN`))*
- `[e5]` **văn phòng đại diện** → `TO_CHUC_DOANH_NGHIEP` (span: `[14:16]`) *(lồng trong `e1` (`KHOAN`))*
- `[e6]` **văn phòng đại diện** → `TO_CHUC_DOANH_NGHIEP` (span: `[53:55]`) *(lồng trong `e1` (`KHOAN`))*
- `[e7]` **đơn vị sự nghiệp** → `TO_CHUC_DOANH_NGHIEP` (span: `[17:19]`) *(lồng trong `e1` (`KHOAN`))*
- `[e8]` **đơn vị sự nghiệp** → `TO_CHUC_DOANH_NGHIEP` (span: `[56:58]`) *(lồng trong `e1` (`KHOAN`))*
- `[e9]` **khoản 1 Điều này** → `THAM_CHIEU_PHAP_LY` (span: `[65:69]`) *(lồng trong `e1` (`KHOAN`))*
- `[e10]` **quy định tại** → `TU_KHOA_PHAP_LY` (span: `[63:65]`) *(lồng trong `e1` (`KHOAN`))*
- `[e11]` **Ngân hàng Nhà nước** → `CO_QUAN_THAM_QUYEN` (span: `[37:39]`) *(lồng trong `e1` (`KHOAN`))*
- `[e12]` **Ngân hàng Nhà nước chi nhánh tỉnh , thành phố** → `CO_QUAN_THAM_QUYEN` (span: `[40:46]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 2 . Trước ngày khai trương hoạt động sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp mười lăm ngày làm việc , ngân hàng thương mại phải đăng báo theo quy định của pháp luật ; có văn bản gửi Ngân hàng Nhà nước và Ngân hàng Nhà nước chi nhánh tỉnh , thành phố nơi mở sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp báo cáo việc đáp ứng các điều kiện quy định tại khoản 1 Điều này kèm theo bản sao đăng ký `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 9 `[DIEU]`)
- (`e10` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e9` khoản 1 Điều này `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 2 . Trước ngày khai trương hoạt động sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp mười lăm ngày làm việc , ngân hàng thương mại phải đăng báo theo quy định của pháp luật ; có văn bản gửi Ngân hàng Nhà nước và Ngân hàng Nhà nước chi nhánh tỉnh , thành phố nơi mở sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp báo cáo việc đáp ứng các điều kiện quy định tại khoản 1 Điều này kèm theo bản sao đăng ký `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e9` khoản 1 Điều này `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #13_2008_QĐ-NHNN_32111#body_context_44 (Loại: `body_context`)
> **[Quyết định]`<LOAI_VAN_BAN>`** số **[13/2008/QĐ-NHNN]`<SO_HIEU>`** của **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Ngân hàng]`<LINH_VUC>`** . **[Điều 9]`<DIEU>`** . **[3 . Trường hợp có nhu cầu gia hạn thời hạn khai trương hoạt động **[quy định tại]`<TU_KHOA_PHAP_LY>`** **[Khoản 1 Điều này]`<THAM_CHIEU_PHAP_LY>`** , trước ngày hết thời hạn khai trương hoạt động hai mươi ngày làm việc , **[ngân hàng thương mại]`<TO_CHUC_DOANH_NGHIEP>`** có **[văn bản đề nghị]`<GIAY_TO_HO_SO>`** gia hạn thời hạn khai trương hoạt động **[sở giao dịch]`<CO_QUAN_THAM_QUYEN>`** , chi nhánh , **[văn phòng đại diện]`<TO_CHUC_DOANH_NGHIEP>`** , **[đơn vị sự nghiệp]`<TO_CHUC_DOANH_NGHIEP>`** gửi **[Ngân hàng Nhà nước]`<CO_QUAN_THAM_QUYEN>`** , trong đó nêu rõ lý do .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Quyết định** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **13/2008/QĐ-NHNN** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_BAN_HANH` (span: `[4:7]`)
- `[e3]` **Ngân hàng** → `LINH_VUC` (span: `[9:10]`)
- `[e4]` **Điều 9** → `DIEU` (span: `[11:13]`)
- `[e5]` **3 . Trường hợp có nhu cầu gia hạn thời hạn khai trương hoạt động quy định tại Khoản 1 Điều này , trước ngày hết thời hạn khai trương hoạt động hai mươi ngày làm việc , ngân hàng thương mại có văn bản đề nghị gia hạn thời hạn khai trương hoạt động sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp gửi Ngân hàng Nhà nước , trong đó nêu rõ lý do .** → `KHOAN` (span: `[14:70]`)
- `[e6]` **sở giao dịch** → `CO_QUAN_THAM_QUYEN` (span: `[50:52]`) *(lồng trong `e5` (`KHOAN`))*
- `[e7]` **ngân hàng thương mại** → `TO_CHUC_DOANH_NGHIEP` (span: `[41:43]`) *(lồng trong `e5` (`KHOAN`))*
- `[e8]` **văn phòng đại diện** → `TO_CHUC_DOANH_NGHIEP` (span: `[55:57]`) *(lồng trong `e5` (`KHOAN`))*
- `[e9]` **đơn vị sự nghiệp** → `TO_CHUC_DOANH_NGHIEP` (span: `[58:60]`) *(lồng trong `e5` (`KHOAN`))*
- `[e10]` **Khoản 1 Điều này** → `THAM_CHIEU_PHAP_LY` (span: `[25:29]`) *(lồng trong `e5` (`KHOAN`))*
- `[e11]` **quy định tại** → `TU_KHOA_PHAP_LY` (span: `[23:25]`) *(lồng trong `e5` (`KHOAN`))*
- `[e12]` **Ngân hàng Nhà nước** → `CO_QUAN_THAM_QUYEN` (span: `[61:63]`) *(lồng trong `e5` (`KHOAN`))*
- `[e13]` **văn bản đề nghị** → `GIAY_TO_HO_SO` (span: `[44:46]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Ngân hàng Nhà nước Việt Nam `[CO_QUAN_BAN_HANH]`)
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Quyết định `[LOAI_VAN_BAN]`)
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Ngân hàng `[LINH_VUC]`)
- (`e4` Điều 9 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`)
- (`e5` 3 . Trường hợp có nhu cầu gia hạn thời hạn khai trương hoạt động quy định tại Khoản 1 Điều này , trước ngày hết thời hạn khai trương hoạt động hai mươi ngày làm việc , ngân hàng thương mại có văn bản đề nghị gia hạn thời hạn khai trương hoạt động sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp gửi Ngân hàng Nhà nước , trong đó nêu rõ lý do . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 9 `[DIEU]`)
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Ngân hàng `[LINH_VUC]`)
- (`e5` 3 . Trường hợp có nhu cầu gia hạn thời hạn khai trương hoạt động quy định tại Khoản 1 Điều này , trước ngày hết thời hạn khai trương hoạt động hai mươi ngày làm việc , ngân hàng thương mại có văn bản đề nghị gia hạn thời hạn khai trương hoạt động sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp gửi Ngân hàng Nhà nước , trong đó nêu rõ lý do . `[KHOAN]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Ngân hàng `[LINH_VUC]`)
- (`e11` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e10` Khoản 1 Điều này `[THAM_CHIEU_PHAP_LY]`)
- (`e5` 3 . Trường hợp có nhu cầu gia hạn thời hạn khai trương hoạt động quy định tại Khoản 1 Điều này , trước ngày hết thời hạn khai trương hoạt động hai mươi ngày làm việc , ngân hàng thương mại có văn bản đề nghị gia hạn thời hạn khai trương hoạt động sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp gửi Ngân hàng Nhà nước , trong đó nêu rõ lý do . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e10` Khoản 1 Điều này `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #13_2008_QĐ-NHNN_32111#body_standalone_45 (Loại: `body_standalone`)
> **[Điều 9]`<DIEU>`** . **[3 . Trường hợp có nhu cầu gia hạn thời hạn khai trương hoạt động **[quy định tại]`<TU_KHOA_PHAP_LY>`** **[Khoản 1 Điều này]`<THAM_CHIEU_PHAP_LY>`** , trước ngày hết thời hạn khai trương hoạt động hai mươi ngày làm việc , **[ngân hàng thương mại]`<TO_CHUC_DOANH_NGHIEP>`** có **[văn bản đề nghị]`<GIAY_TO_HO_SO>`** gia hạn thời hạn khai trương hoạt động **[sở giao dịch]`<CO_QUAN_THAM_QUYEN>`** , chi nhánh , **[văn phòng đại diện]`<TO_CHUC_DOANH_NGHIEP>`** , **[đơn vị sự nghiệp]`<TO_CHUC_DOANH_NGHIEP>`** gửi **[Ngân hàng Nhà nước]`<CO_QUAN_THAM_QUYEN>`** , trong đó nêu rõ lý do .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 9** → `DIEU` (span: `[0:2]`)
- `[e1]` **3 . Trường hợp có nhu cầu gia hạn thời hạn khai trương hoạt động quy định tại Khoản 1 Điều này , trước ngày hết thời hạn khai trương hoạt động hai mươi ngày làm việc , ngân hàng thương mại có văn bản đề nghị gia hạn thời hạn khai trương hoạt động sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp gửi Ngân hàng Nhà nước , trong đó nêu rõ lý do .** → `KHOAN` (span: `[3:59]`)
- `[e2]` **sở giao dịch** → `CO_QUAN_THAM_QUYEN` (span: `[39:41]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **ngân hàng thương mại** → `TO_CHUC_DOANH_NGHIEP` (span: `[30:32]`) *(lồng trong `e1` (`KHOAN`))*
- `[e4]` **văn phòng đại diện** → `TO_CHUC_DOANH_NGHIEP` (span: `[44:46]`) *(lồng trong `e1` (`KHOAN`))*
- `[e5]` **đơn vị sự nghiệp** → `TO_CHUC_DOANH_NGHIEP` (span: `[47:49]`) *(lồng trong `e1` (`KHOAN`))*
- `[e6]` **Khoản 1 Điều này** → `THAM_CHIEU_PHAP_LY` (span: `[14:18]`) *(lồng trong `e1` (`KHOAN`))*
- `[e7]` **quy định tại** → `TU_KHOA_PHAP_LY` (span: `[12:14]`) *(lồng trong `e1` (`KHOAN`))*
- `[e8]` **Ngân hàng Nhà nước** → `CO_QUAN_THAM_QUYEN` (span: `[50:52]`) *(lồng trong `e1` (`KHOAN`))*
- `[e9]` **văn bản đề nghị** → `GIAY_TO_HO_SO` (span: `[33:35]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 3 . Trường hợp có nhu cầu gia hạn thời hạn khai trương hoạt động quy định tại Khoản 1 Điều này , trước ngày hết thời hạn khai trương hoạt động hai mươi ngày làm việc , ngân hàng thương mại có văn bản đề nghị gia hạn thời hạn khai trương hoạt động sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp gửi Ngân hàng Nhà nước , trong đó nêu rõ lý do . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 9 `[DIEU]`)
- (`e7` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e6` Khoản 1 Điều này `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 3 . Trường hợp có nhu cầu gia hạn thời hạn khai trương hoạt động quy định tại Khoản 1 Điều này , trước ngày hết thời hạn khai trương hoạt động hai mươi ngày làm việc , ngân hàng thương mại có văn bản đề nghị gia hạn thời hạn khai trương hoạt động sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp gửi Ngân hàng Nhà nước , trong đó nêu rõ lý do . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e6` Khoản 1 Điều này `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #13_2008_QĐ-NHNN_32111#body_context_46 (Loại: `body_context`)
> **[Quyết định]`<LOAI_VAN_BAN>`** số **[13/2008/QĐ-NHNN]`<SO_HIEU>`** ban hành **[ngày 29 tháng 04 năm 2008]`<NGAY_BAN_HANH>`** bởi **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_BAN_HANH>`** . **[Điều 10]`<DIEU>`** . **[1 . **[Thống đốc Ngân hàng Nhà nước]`<CO_QUAN_THAM_QUYEN>`** ủy quyền cho **[Giám đốc]`<CHU_THE_CA_NHAN>`** **[Ngân hàng Nhà nước chi nhánh tỉnh , thành phố]`<CO_QUAN_THAM_QUYEN>`** xem xét chấp thuận đề nghị thay đổi tên , địa điểm của **[sở giao dịch]`<CO_QUAN_THAM_QUYEN>`** , chi nhánh , **[văn phòng đại diện]`<TO_CHUC_DOANH_NGHIEP>`** , **[đơn vị sự nghiệp]`<TO_CHUC_DOANH_NGHIEP>`** của **[ngân hàng thương mại]`<TO_CHUC_DOANH_NGHIEP>`** trên địa bàn .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Quyết định** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **13/2008/QĐ-NHNN** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_BAN_HANH` (span: `[11:14]`)
- `[e3]` **ngày 29 tháng 04 năm 2008** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 10** → `DIEU` (span: `[15:17]`)
- `[e5]` **1 . Thống đốc Ngân hàng Nhà nước ủy quyền cho Giám đốc Ngân hàng Nhà nước chi nhánh tỉnh , thành phố xem xét chấp thuận đề nghị thay đổi tên , địa điểm của sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp của ngân hàng thương mại trên địa bàn .** → `KHOAN` (span: `[18:57]`)
- `[e6]` **sở giao dịch** → `CO_QUAN_THAM_QUYEN` (span: `[41:43]`) *(lồng trong `e5` (`KHOAN`))*
- `[e7]` **ngân hàng thương mại** → `TO_CHUC_DOANH_NGHIEP` (span: `[52:54]`) *(lồng trong `e5` (`KHOAN`))*
- `[e8]` **văn phòng đại diện** → `TO_CHUC_DOANH_NGHIEP` (span: `[46:48]`) *(lồng trong `e5` (`KHOAN`))*
- `[e9]` **đơn vị sự nghiệp** → `TO_CHUC_DOANH_NGHIEP` (span: `[49:51]`) *(lồng trong `e5` (`KHOAN`))*
- `[e10]` **Thống đốc Ngân hàng Nhà nước** → `CO_QUAN_THAM_QUYEN` (span: `[20:23]`) *(lồng trong `e5` (`KHOAN`))*
- `[e11]` **Ngân hàng Nhà nước chi nhánh tỉnh , thành phố** → `CO_QUAN_THAM_QUYEN` (span: `[27:33]`) *(lồng trong `e5` (`KHOAN`))*
- `[e12]` **Giám đốc** → `CHU_THE_CA_NHAN` (span: `[26:27]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Ngân hàng Nhà nước Việt Nam `[CO_QUAN_BAN_HANH]`)
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Quyết định `[LOAI_VAN_BAN]`)
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 29 tháng 04 năm 2008 `[NGAY_BAN_HANH]`)
- (`e4` Điều 10 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`)
- (`e5` 1 . Thống đốc Ngân hàng Nhà nước ủy quyền cho Giám đốc Ngân hàng Nhà nước chi nhánh tỉnh , thành phố xem xét chấp thuận đề nghị thay đổi tên , địa điểm của sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp của ngân hàng thương mại trên địa bàn . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 10 `[DIEU]`)


---

### Mẫu #13_2008_QĐ-NHNN_32111#body_standalone_47 (Loại: `body_standalone`)
> **[Điều 10]`<DIEU>`** . **[1 . **[Thống đốc Ngân hàng Nhà nước]`<CO_QUAN_THAM_QUYEN>`** ủy quyền cho **[Giám đốc]`<CHU_THE_CA_NHAN>`** **[Ngân hàng Nhà nước chi nhánh tỉnh , thành phố]`<CO_QUAN_THAM_QUYEN>`** xem xét chấp thuận đề nghị thay đổi tên , địa điểm của **[sở giao dịch]`<CO_QUAN_THAM_QUYEN>`** , chi nhánh , **[văn phòng đại diện]`<TO_CHUC_DOANH_NGHIEP>`** , **[đơn vị sự nghiệp]`<TO_CHUC_DOANH_NGHIEP>`** của **[ngân hàng thương mại]`<TO_CHUC_DOANH_NGHIEP>`** trên địa bàn .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 10** → `DIEU` (span: `[0:2]`)
- `[e1]` **1 . Thống đốc Ngân hàng Nhà nước ủy quyền cho Giám đốc Ngân hàng Nhà nước chi nhánh tỉnh , thành phố xem xét chấp thuận đề nghị thay đổi tên , địa điểm của sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp của ngân hàng thương mại trên địa bàn .** → `KHOAN` (span: `[3:42]`)
- `[e2]` **sở giao dịch** → `CO_QUAN_THAM_QUYEN` (span: `[26:28]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **ngân hàng thương mại** → `TO_CHUC_DOANH_NGHIEP` (span: `[37:39]`) *(lồng trong `e1` (`KHOAN`))*
- `[e4]` **văn phòng đại diện** → `TO_CHUC_DOANH_NGHIEP` (span: `[31:33]`) *(lồng trong `e1` (`KHOAN`))*
- `[e5]` **đơn vị sự nghiệp** → `TO_CHUC_DOANH_NGHIEP` (span: `[34:36]`) *(lồng trong `e1` (`KHOAN`))*
- `[e6]` **Thống đốc Ngân hàng Nhà nước** → `CO_QUAN_THAM_QUYEN` (span: `[5:8]`) *(lồng trong `e1` (`KHOAN`))*
- `[e7]` **Ngân hàng Nhà nước chi nhánh tỉnh , thành phố** → `CO_QUAN_THAM_QUYEN` (span: `[12:18]`) *(lồng trong `e1` (`KHOAN`))*
- `[e8]` **Giám đốc** → `CHU_THE_CA_NHAN` (span: `[11:12]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 1 . Thống đốc Ngân hàng Nhà nước ủy quyền cho Giám đốc Ngân hàng Nhà nước chi nhánh tỉnh , thành phố xem xét chấp thuận đề nghị thay đổi tên , địa điểm của sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp của ngân hàng thương mại trên địa bàn . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 10 `[DIEU]`)


---

### Mẫu #13_2008_QĐ-NHNN_32111#body_context_48 (Loại: `body_context`)
> **[Quyết định]`<LOAI_VAN_BAN>`** số **[13/2008/QĐ-NHNN]`<SO_HIEU>`** ban hành **[ngày 29 tháng 04 năm 2008]`<NGAY_BAN_HANH>`** bởi **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_BAN_HANH>`** . **[Điều 10]`<DIEU>`** . **[Khoản 2]`<KHOAN>`** . **[a ) Văn bản của Chủ tịch **[Hội đồng quản trị]`<TO_CHUC_DOANH_NGHIEP>`** **[ngân hàng thương mại]`<TO_CHUC_DOANH_NGHIEP>`** đề nghị chấp thuận thay đổi tên , địa điểm của **[sở giao dịch]`<CO_QUAN_THAM_QUYEN>`** , chi nhánh , **[văn phòng đại diện]`<TO_CHUC_DOANH_NGHIEP>`** , **[đơn vị sự nghiệp]`<TO_CHUC_DOANH_NGHIEP>`** theo **[Phụ lục 03]`<THAM_CHIEU_PHAP_LY>`** kèm theo Quy định này ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Quyết định** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **13/2008/QĐ-NHNN** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_BAN_HANH` (span: `[11:14]`)
- `[e3]` **ngày 29 tháng 04 năm 2008** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 10** → `DIEU` (span: `[15:17]`)
- `[e5]` **Khoản 2** → `KHOAN` (span: `[18:20]`)
- `[e6]` **a ) Văn bản của Chủ tịch Hội đồng quản trị ngân hàng thương mại đề nghị chấp thuận thay đổi tên , địa điểm của sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp theo Phụ lục 03 kèm theo Quy định này ;** → `DIEM` (span: `[21:55]`)
- `[e7]` **sở giao dịch** → `CO_QUAN_THAM_QUYEN` (span: `[37:39]`) *(lồng trong `e6` (`DIEM`))*
- `[e8]` **ngân hàng thương mại** → `TO_CHUC_DOANH_NGHIEP` (span: `[28:30]`) *(lồng trong `e6` (`DIEM`))*
- `[e9]` **văn phòng đại diện** → `TO_CHUC_DOANH_NGHIEP` (span: `[42:44]`) *(lồng trong `e6` (`DIEM`))*
- `[e10]` **đơn vị sự nghiệp** → `TO_CHUC_DOANH_NGHIEP` (span: `[45:47]`) *(lồng trong `e6` (`DIEM`))*
- `[e11]` **Phụ lục 03** → `THAM_CHIEU_PHAP_LY` (span: `[48:50]`) *(lồng trong `e6` (`DIEM`))*
- `[e12]` **Hội đồng quản trị** → `TO_CHUC_DOANH_NGHIEP` (span: `[26:28]`) *(lồng trong `e6` (`DIEM`))*

**Quan hệ:**
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Ngân hàng Nhà nước Việt Nam `[CO_QUAN_BAN_HANH]`)
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Quyết định `[LOAI_VAN_BAN]`)
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 29 tháng 04 năm 2008 `[NGAY_BAN_HANH]`)
- (`e4` Điều 10 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`)
- (`e5` Khoản 2 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 10 `[DIEU]`)
- (`e6` a ) Văn bản của Chủ tịch Hội đồng quản trị ngân hàng thương mại đề nghị chấp thuận thay đổi tên , địa điểm của sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp theo Phụ lục 03 kèm theo Quy định này ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e5` Khoản 2 `[KHOAN]`)
- (`e6` a ) Văn bản của Chủ tịch Hội đồng quản trị ngân hàng thương mại đề nghị chấp thuận thay đổi tên , địa điểm của sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp theo Phụ lục 03 kèm theo Quy định này ; `[DIEM]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e11` Phụ lục 03 `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #13_2008_QĐ-NHNN_32111#body_standalone_49 (Loại: `body_standalone`)
> **[Điều 10]`<DIEU>`** . **[Khoản 2]`<KHOAN>`** . **[a ) Văn bản của Chủ tịch **[Hội đồng quản trị]`<TO_CHUC_DOANH_NGHIEP>`** **[ngân hàng thương mại]`<TO_CHUC_DOANH_NGHIEP>`** đề nghị chấp thuận thay đổi tên , địa điểm của **[sở giao dịch]`<CO_QUAN_THAM_QUYEN>`** , chi nhánh , **[văn phòng đại diện]`<TO_CHUC_DOANH_NGHIEP>`** , **[đơn vị sự nghiệp]`<TO_CHUC_DOANH_NGHIEP>`** theo **[Phụ lục 03]`<THAM_CHIEU_PHAP_LY>`** kèm theo Quy định này ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Điều 10** → `DIEU` (span: `[0:2]`)
- `[e1]` **Khoản 2** → `KHOAN` (span: `[3:5]`)
- `[e2]` **a ) Văn bản của Chủ tịch Hội đồng quản trị ngân hàng thương mại đề nghị chấp thuận thay đổi tên , địa điểm của sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp theo Phụ lục 03 kèm theo Quy định này ;** → `DIEM` (span: `[6:40]`)
- `[e3]` **sở giao dịch** → `CO_QUAN_THAM_QUYEN` (span: `[22:24]`) *(lồng trong `e2` (`DIEM`))*
- `[e4]` **ngân hàng thương mại** → `TO_CHUC_DOANH_NGHIEP` (span: `[13:15]`) *(lồng trong `e2` (`DIEM`))*
- `[e5]` **văn phòng đại diện** → `TO_CHUC_DOANH_NGHIEP` (span: `[27:29]`) *(lồng trong `e2` (`DIEM`))*
- `[e6]` **đơn vị sự nghiệp** → `TO_CHUC_DOANH_NGHIEP` (span: `[30:32]`) *(lồng trong `e2` (`DIEM`))*
- `[e7]` **Phụ lục 03** → `THAM_CHIEU_PHAP_LY` (span: `[33:35]`) *(lồng trong `e2` (`DIEM`))*
- `[e8]` **Hội đồng quản trị** → `TO_CHUC_DOANH_NGHIEP` (span: `[11:13]`) *(lồng trong `e2` (`DIEM`))*

**Quan hệ:**
- (`e1` Khoản 2 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 10 `[DIEU]`)
- (`e2` a ) Văn bản của Chủ tịch Hội đồng quản trị ngân hàng thương mại đề nghị chấp thuận thay đổi tên , địa điểm của sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp theo Phụ lục 03 kèm theo Quy định này ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e1` Khoản 2 `[KHOAN]`)
- (`e2` a ) Văn bản của Chủ tịch Hội đồng quản trị ngân hàng thương mại đề nghị chấp thuận thay đổi tên , địa điểm của sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp theo Phụ lục 03 kèm theo Quy định này ; `[DIEM]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e7` Phụ lục 03 `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #13_2008_QĐ-NHNN_32111#body_context_50 (Loại: `body_context`)
> **[Quyết định]`<LOAI_VAN_BAN>`** số **[13/2008/QĐ-NHNN]`<SO_HIEU>`** của **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Ngân hàng]`<LINH_VUC>`** . **[Điều 10]`<DIEU>`** . **[3 . Trong thời hạn hai mươi ngày làm việc kể từ ngày nhận đủ hồ sơ **[theo quy định tại]`<TU_KHOA_PHAP_LY>`** **[Khoản 2 Điều này]`<THAM_CHIEU_PHAP_LY>`** , **[Giám đốc]`<CHU_THE_CA_NHAN>`** **[Ngân hàng Nhà nước chi nhánh tỉnh , thành phố]`<CO_QUAN_THAM_QUYEN>`** có **[văn bản chấp thuận]`<GIAY_TO_HO_SO>`** đề nghị thay đổi tên , địa điểm của **[sở giao dịch]`<CO_QUAN_THAM_QUYEN>`** , chi nhánh , **[văn phòng đại diện]`<TO_CHUC_DOANH_NGHIEP>`** , **[đơn vị sự nghiệp]`<TO_CHUC_DOANH_NGHIEP>`** của **[ngân hàng thương mại]`<TO_CHUC_DOANH_NGHIEP>`** theo **[Phụ lục 04]`<THAM_CHIEU_PHAP_LY>`** kèm theo Quy định này ; trường hợp không chấp thuận , có văn bản nêu rõ lý do hoặc các yêu cầu ( nếu]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Quyết định** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **13/2008/QĐ-NHNN** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_BAN_HANH` (span: `[4:7]`)
- `[e3]` **Ngân hàng** → `LINH_VUC` (span: `[9:10]`)
- `[e4]` **Điều 10** → `DIEU` (span: `[11:13]`)
- `[e5]` **3 . Trong thời hạn hai mươi ngày làm việc kể từ ngày nhận đủ hồ sơ theo quy định tại Khoản 2 Điều này , Giám đốc Ngân hàng Nhà nước chi nhánh tỉnh , thành phố có văn bản chấp thuận đề nghị thay đổi tên , địa điểm của sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp của ngân hàng thương mại theo Phụ lục 04 kèm theo Quy định này ; trường hợp không chấp thuận , có văn bản nêu rõ lý do hoặc các yêu cầu ( nếu** → `KHOAN` (span: `[14:87]`)
- `[e6]` **sở giao dịch** → `CO_QUAN_THAM_QUYEN` (span: `[52:54]`) *(lồng trong `e5` (`KHOAN`))*
- `[e7]` **ngân hàng thương mại** → `TO_CHUC_DOANH_NGHIEP` (span: `[63:65]`) *(lồng trong `e5` (`KHOAN`))*
- `[e8]` **văn phòng đại diện** → `TO_CHUC_DOANH_NGHIEP` (span: `[57:59]`) *(lồng trong `e5` (`KHOAN`))*
- `[e9]` **đơn vị sự nghiệp** → `TO_CHUC_DOANH_NGHIEP` (span: `[60:62]`) *(lồng trong `e5` (`KHOAN`))*
- `[e10]` **Khoản 2 Điều này** → `THAM_CHIEU_PHAP_LY` (span: `[31:35]`) *(lồng trong `e5` (`KHOAN`))*
- `[e11]` **Phụ lục 04** → `THAM_CHIEU_PHAP_LY` (span: `[66:68]`) *(lồng trong `e5` (`KHOAN`))*
- `[e12]` **theo quy định tại** → `TU_KHOA_PHAP_LY` (span: `[28:31]`) *(lồng trong `e5` (`KHOAN`))*
- `[e13]` **Ngân hàng Nhà nước chi nhánh tỉnh , thành phố** → `CO_QUAN_THAM_QUYEN` (span: `[37:43]`) *(lồng trong `e5` (`KHOAN`))*
- `[e14]` **văn bản chấp thuận** → `GIAY_TO_HO_SO` (span: `[44:46]`) *(lồng trong `e5` (`KHOAN`))*
- `[e15]` **Giám đốc** → `CHU_THE_CA_NHAN` (span: `[36:37]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Ngân hàng Nhà nước Việt Nam `[CO_QUAN_BAN_HANH]`)
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Quyết định `[LOAI_VAN_BAN]`)
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Ngân hàng `[LINH_VUC]`)
- (`e4` Điều 10 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`)
- (`e5` 3 . Trong thời hạn hai mươi ngày làm việc kể từ ngày nhận đủ hồ sơ theo quy định tại Khoản 2 Điều này , Giám đốc Ngân hàng Nhà nước chi nhánh tỉnh , thành phố có văn bản chấp thuận đề nghị thay đổi tên , địa điểm của sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp của ngân hàng thương mại theo Phụ lục 04 kèm theo Quy định này ; trường hợp không chấp thuận , có văn bản nêu rõ lý do hoặc các yêu cầu ( nếu `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 10 `[DIEU]`)
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Ngân hàng `[LINH_VUC]`)
- (`e5` 3 . Trong thời hạn hai mươi ngày làm việc kể từ ngày nhận đủ hồ sơ theo quy định tại Khoản 2 Điều này , Giám đốc Ngân hàng Nhà nước chi nhánh tỉnh , thành phố có văn bản chấp thuận đề nghị thay đổi tên , địa điểm của sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp của ngân hàng thương mại theo Phụ lục 04 kèm theo Quy định này ; trường hợp không chấp thuận , có văn bản nêu rõ lý do hoặc các yêu cầu ( nếu `[KHOAN]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Ngân hàng `[LINH_VUC]`)
- (`e12` theo quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e10` Khoản 2 Điều này `[THAM_CHIEU_PHAP_LY]`)
- (`e5` 3 . Trong thời hạn hai mươi ngày làm việc kể từ ngày nhận đủ hồ sơ theo quy định tại Khoản 2 Điều này , Giám đốc Ngân hàng Nhà nước chi nhánh tỉnh , thành phố có văn bản chấp thuận đề nghị thay đổi tên , địa điểm của sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp của ngân hàng thương mại theo Phụ lục 04 kèm theo Quy định này ; trường hợp không chấp thuận , có văn bản nêu rõ lý do hoặc các yêu cầu ( nếu `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e10` Khoản 2 Điều này `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e12` theo quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e11` Phụ lục 04 `[THAM_CHIEU_PHAP_LY]`)
- (`e5` 3 . Trong thời hạn hai mươi ngày làm việc kể từ ngày nhận đủ hồ sơ theo quy định tại Khoản 2 Điều này , Giám đốc Ngân hàng Nhà nước chi nhánh tỉnh , thành phố có văn bản chấp thuận đề nghị thay đổi tên , địa điểm của sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp của ngân hàng thương mại theo Phụ lục 04 kèm theo Quy định này ; trường hợp không chấp thuận , có văn bản nêu rõ lý do hoặc các yêu cầu ( nếu `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e11` Phụ lục 04 `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #13_2008_QĐ-NHNN_32111#body_standalone_51 (Loại: `body_standalone`)
> **[Điều 10]`<DIEU>`** . **[3 . Trong thời hạn hai mươi ngày làm việc kể từ ngày nhận đủ hồ sơ **[theo quy định tại]`<TU_KHOA_PHAP_LY>`** **[Khoản 2 Điều này]`<THAM_CHIEU_PHAP_LY>`** , **[Giám đốc]`<CHU_THE_CA_NHAN>`** **[Ngân hàng Nhà nước chi nhánh tỉnh , thành phố]`<CO_QUAN_THAM_QUYEN>`** có **[văn bản chấp thuận]`<GIAY_TO_HO_SO>`** đề nghị thay đổi tên , địa điểm của **[sở giao dịch]`<CO_QUAN_THAM_QUYEN>`** , chi nhánh , **[văn phòng đại diện]`<TO_CHUC_DOANH_NGHIEP>`** , **[đơn vị sự nghiệp]`<TO_CHUC_DOANH_NGHIEP>`** của **[ngân hàng thương mại]`<TO_CHUC_DOANH_NGHIEP>`** theo **[Phụ lục 04]`<THAM_CHIEU_PHAP_LY>`** kèm theo Quy định này ; trường hợp không chấp thuận , có văn bản nêu rõ lý do hoặc các yêu cầu ( nếu]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 10** → `DIEU` (span: `[0:2]`)
- `[e1]` **3 . Trong thời hạn hai mươi ngày làm việc kể từ ngày nhận đủ hồ sơ theo quy định tại Khoản 2 Điều này , Giám đốc Ngân hàng Nhà nước chi nhánh tỉnh , thành phố có văn bản chấp thuận đề nghị thay đổi tên , địa điểm của sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp của ngân hàng thương mại theo Phụ lục 04 kèm theo Quy định này ; trường hợp không chấp thuận , có văn bản nêu rõ lý do hoặc các yêu cầu ( nếu** → `KHOAN` (span: `[3:76]`)
- `[e2]` **sở giao dịch** → `CO_QUAN_THAM_QUYEN` (span: `[41:43]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **ngân hàng thương mại** → `TO_CHUC_DOANH_NGHIEP` (span: `[52:54]`) *(lồng trong `e1` (`KHOAN`))*
- `[e4]` **văn phòng đại diện** → `TO_CHUC_DOANH_NGHIEP` (span: `[46:48]`) *(lồng trong `e1` (`KHOAN`))*
- `[e5]` **đơn vị sự nghiệp** → `TO_CHUC_DOANH_NGHIEP` (span: `[49:51]`) *(lồng trong `e1` (`KHOAN`))*
- `[e6]` **Khoản 2 Điều này** → `THAM_CHIEU_PHAP_LY` (span: `[20:24]`) *(lồng trong `e1` (`KHOAN`))*
- `[e7]` **Phụ lục 04** → `THAM_CHIEU_PHAP_LY` (span: `[55:57]`) *(lồng trong `e1` (`KHOAN`))*
- `[e8]` **theo quy định tại** → `TU_KHOA_PHAP_LY` (span: `[17:20]`) *(lồng trong `e1` (`KHOAN`))*
- `[e9]` **Ngân hàng Nhà nước chi nhánh tỉnh , thành phố** → `CO_QUAN_THAM_QUYEN` (span: `[26:32]`) *(lồng trong `e1` (`KHOAN`))*
- `[e10]` **văn bản chấp thuận** → `GIAY_TO_HO_SO` (span: `[33:35]`) *(lồng trong `e1` (`KHOAN`))*
- `[e11]` **Giám đốc** → `CHU_THE_CA_NHAN` (span: `[25:26]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 3 . Trong thời hạn hai mươi ngày làm việc kể từ ngày nhận đủ hồ sơ theo quy định tại Khoản 2 Điều này , Giám đốc Ngân hàng Nhà nước chi nhánh tỉnh , thành phố có văn bản chấp thuận đề nghị thay đổi tên , địa điểm của sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp của ngân hàng thương mại theo Phụ lục 04 kèm theo Quy định này ; trường hợp không chấp thuận , có văn bản nêu rõ lý do hoặc các yêu cầu ( nếu `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 10 `[DIEU]`)
- (`e8` theo quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e6` Khoản 2 Điều này `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 3 . Trong thời hạn hai mươi ngày làm việc kể từ ngày nhận đủ hồ sơ theo quy định tại Khoản 2 Điều này , Giám đốc Ngân hàng Nhà nước chi nhánh tỉnh , thành phố có văn bản chấp thuận đề nghị thay đổi tên , địa điểm của sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp của ngân hàng thương mại theo Phụ lục 04 kèm theo Quy định này ; trường hợp không chấp thuận , có văn bản nêu rõ lý do hoặc các yêu cầu ( nếu `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e6` Khoản 2 Điều này `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e8` theo quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e7` Phụ lục 04 `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 3 . Trong thời hạn hai mươi ngày làm việc kể từ ngày nhận đủ hồ sơ theo quy định tại Khoản 2 Điều này , Giám đốc Ngân hàng Nhà nước chi nhánh tỉnh , thành phố có văn bản chấp thuận đề nghị thay đổi tên , địa điểm của sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp của ngân hàng thương mại theo Phụ lục 04 kèm theo Quy định này ; trường hợp không chấp thuận , có văn bản nêu rõ lý do hoặc các yêu cầu ( nếu `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e7` Phụ lục 04 `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #13_2008_QĐ-NHNN_32111#body_context_52 (Loại: `body_context`)
> **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_BAN_HANH>`** ban hành **[Quyết định]`<LOAI_VAN_BAN>`** số **[13/2008/QĐ-NHNN]`<SO_HIEU>`** . **[Điều 10]`<DIEU>`** . **[5 . Kết thúc thời hạn **[quy định tại]`<TU_KHOA_PHAP_LY>`** **[Khoản 4 Điều này]`<THAM_CHIEU_PHAP_LY>`** , **[sở giao dịch]`<CO_QUAN_THAM_QUYEN>`** , chi nhánh , **[văn phòng đại diện]`<TO_CHUC_DOANH_NGHIEP>`** , **[đơn vị sự nghiệp]`<TO_CHUC_DOANH_NGHIEP>`** không hoạt động theo tên , địa điểm đã được chấp thuận , **[văn bản chấp thuận]`<GIAY_TO_HO_SO>`** của **[Ngân hàng Nhà nước chi nhánh tỉnh , thành phố]`<CO_QUAN_THAM_QUYEN>`** không còn giá trị .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Quyết định** → `LOAI_VAN_BAN` (span: `[4:5]`)
- `[e1]` **13/2008/QĐ-NHNN** → `SO_HIEU` (span: `[6:7]`)
- `[e2]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_BAN_HANH` (span: `[0:3]`)
- `[e3]` **Điều 10** → `DIEU` (span: `[8:10]`)
- `[e4]` **5 . Kết thúc thời hạn quy định tại Khoản 4 Điều này , sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp không hoạt động theo tên , địa điểm đã được chấp thuận , văn bản chấp thuận của Ngân hàng Nhà nước chi nhánh tỉnh , thành phố không còn giá trị .** → `KHOAN` (span: `[11:55]`)
- `[e5]` **sở giao dịch** → `CO_QUAN_THAM_QUYEN` (span: `[22:24]`) *(lồng trong `e4` (`KHOAN`))*
- `[e6]` **văn phòng đại diện** → `TO_CHUC_DOANH_NGHIEP` (span: `[27:29]`) *(lồng trong `e4` (`KHOAN`))*
- `[e7]` **đơn vị sự nghiệp** → `TO_CHUC_DOANH_NGHIEP` (span: `[30:32]`) *(lồng trong `e4` (`KHOAN`))*
- `[e8]` **Khoản 4 Điều này** → `THAM_CHIEU_PHAP_LY` (span: `[17:21]`) *(lồng trong `e4` (`KHOAN`))*
- `[e9]` **quy định tại** → `TU_KHOA_PHAP_LY` (span: `[15:17]`) *(lồng trong `e4` (`KHOAN`))*
- `[e10]` **Ngân hàng Nhà nước chi nhánh tỉnh , thành phố** → `CO_QUAN_THAM_QUYEN` (span: `[45:51]`) *(lồng trong `e4` (`KHOAN`))*
- `[e11]` **văn bản chấp thuận** → `GIAY_TO_HO_SO` (span: `[42:44]`) *(lồng trong `e4` (`KHOAN`))*

**Quan hệ:**
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Ngân hàng Nhà nước Việt Nam `[CO_QUAN_BAN_HANH]`)
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Quyết định `[LOAI_VAN_BAN]`)
- (`e3` Điều 10 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`)
- (`e4` 5 . Kết thúc thời hạn quy định tại Khoản 4 Điều này , sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp không hoạt động theo tên , địa điểm đã được chấp thuận , văn bản chấp thuận của Ngân hàng Nhà nước chi nhánh tỉnh , thành phố không còn giá trị . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 10 `[DIEU]`)
- (`e9` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e8` Khoản 4 Điều này `[THAM_CHIEU_PHAP_LY]`)
- (`e4` 5 . Kết thúc thời hạn quy định tại Khoản 4 Điều này , sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp không hoạt động theo tên , địa điểm đã được chấp thuận , văn bản chấp thuận của Ngân hàng Nhà nước chi nhánh tỉnh , thành phố không còn giá trị . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e8` Khoản 4 Điều này `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #13_2008_QĐ-NHNN_32111#body_standalone_53 (Loại: `body_standalone`)
> **[Điều 10]`<DIEU>`** . **[5 . Kết thúc thời hạn **[quy định tại]`<TU_KHOA_PHAP_LY>`** **[Khoản 4 Điều này]`<THAM_CHIEU_PHAP_LY>`** , **[sở giao dịch]`<CO_QUAN_THAM_QUYEN>`** , chi nhánh , **[văn phòng đại diện]`<TO_CHUC_DOANH_NGHIEP>`** , **[đơn vị sự nghiệp]`<TO_CHUC_DOANH_NGHIEP>`** không hoạt động theo tên , địa điểm đã được chấp thuận , **[văn bản chấp thuận]`<GIAY_TO_HO_SO>`** của **[Ngân hàng Nhà nước chi nhánh tỉnh , thành phố]`<CO_QUAN_THAM_QUYEN>`** không còn giá trị .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 10** → `DIEU` (span: `[0:2]`)
- `[e1]` **5 . Kết thúc thời hạn quy định tại Khoản 4 Điều này , sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp không hoạt động theo tên , địa điểm đã được chấp thuận , văn bản chấp thuận của Ngân hàng Nhà nước chi nhánh tỉnh , thành phố không còn giá trị .** → `KHOAN` (span: `[3:47]`)
- `[e2]` **sở giao dịch** → `CO_QUAN_THAM_QUYEN` (span: `[14:16]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **văn phòng đại diện** → `TO_CHUC_DOANH_NGHIEP` (span: `[19:21]`) *(lồng trong `e1` (`KHOAN`))*
- `[e4]` **đơn vị sự nghiệp** → `TO_CHUC_DOANH_NGHIEP` (span: `[22:24]`) *(lồng trong `e1` (`KHOAN`))*
- `[e5]` **Khoản 4 Điều này** → `THAM_CHIEU_PHAP_LY` (span: `[9:13]`) *(lồng trong `e1` (`KHOAN`))*
- `[e6]` **quy định tại** → `TU_KHOA_PHAP_LY` (span: `[7:9]`) *(lồng trong `e1` (`KHOAN`))*
- `[e7]` **Ngân hàng Nhà nước chi nhánh tỉnh , thành phố** → `CO_QUAN_THAM_QUYEN` (span: `[37:43]`) *(lồng trong `e1` (`KHOAN`))*
- `[e8]` **văn bản chấp thuận** → `GIAY_TO_HO_SO` (span: `[34:36]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 5 . Kết thúc thời hạn quy định tại Khoản 4 Điều này , sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp không hoạt động theo tên , địa điểm đã được chấp thuận , văn bản chấp thuận của Ngân hàng Nhà nước chi nhánh tỉnh , thành phố không còn giá trị . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 10 `[DIEU]`)
- (`e6` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e5` Khoản 4 Điều này `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 5 . Kết thúc thời hạn quy định tại Khoản 4 Điều này , sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp không hoạt động theo tên , địa điểm đã được chấp thuận , văn bản chấp thuận của Ngân hàng Nhà nước chi nhánh tỉnh , thành phố không còn giá trị . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e5` Khoản 4 Điều này `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #13_2008_QĐ-NHNN_32111#body_context_54 (Loại: `body_context`)
> **[Quyết định]`<LOAI_VAN_BAN>`** số **[13/2008/QĐ-NHNN]`<SO_HIEU>`** của **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Ngân hàng]`<LINH_VUC>`** . **[Điều 11]`<DIEU>`** . **[1 . **[Thống đốc Ngân hàng Nhà nước]`<CO_QUAN_THAM_QUYEN>`** ủy quyền cho **[Giám đốc]`<CHU_THE_CA_NHAN>`** **[Ngân hàng Nhà nước chi nhánh tỉnh , thành phố]`<CO_QUAN_THAM_QUYEN>`** xác nhận đăng ký việc mở , thay đổi tên và / hoặc địa điểm , chấm dứt hoạt động phòng giao dịch , **[quỹ tiết kiệm]`<TO_CHUC_DOANH_NGHIEP>`** , ATM của **[ngân hàng thương mại]`<TO_CHUC_DOANH_NGHIEP>`** trên địa bàn .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Quyết định** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **13/2008/QĐ-NHNN** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_BAN_HANH` (span: `[4:7]`)
- `[e3]` **Ngân hàng** → `LINH_VUC` (span: `[9:10]`)
- `[e4]` **Điều 11** → `DIEU` (span: `[11:13]`)
- `[e5]` **1 . Thống đốc Ngân hàng Nhà nước ủy quyền cho Giám đốc Ngân hàng Nhà nước chi nhánh tỉnh , thành phố xác nhận đăng ký việc mở , thay đổi tên và / hoặc địa điểm , chấm dứt hoạt động phòng giao dịch , quỹ tiết kiệm , ATM của ngân hàng thương mại trên địa bàn .** → `KHOAN` (span: `[14:56]`)
- `[e6]` **ngân hàng thương mại** → `TO_CHUC_DOANH_NGHIEP` (span: `[51:53]`) *(lồng trong `e5` (`KHOAN`))*
- `[e7]` **quỹ tiết kiệm** → `TO_CHUC_DOANH_NGHIEP` (span: `[46:48]`) *(lồng trong `e5` (`KHOAN`))*
- `[e8]` **Thống đốc Ngân hàng Nhà nước** → `CO_QUAN_THAM_QUYEN` (span: `[16:19]`) *(lồng trong `e5` (`KHOAN`))*
- `[e9]` **Ngân hàng Nhà nước chi nhánh tỉnh , thành phố** → `CO_QUAN_THAM_QUYEN` (span: `[23:29]`) *(lồng trong `e5` (`KHOAN`))*
- `[e10]` **Giám đốc** → `CHU_THE_CA_NHAN` (span: `[22:23]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Ngân hàng Nhà nước Việt Nam `[CO_QUAN_BAN_HANH]`)
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Quyết định `[LOAI_VAN_BAN]`)
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Ngân hàng `[LINH_VUC]`)
- (`e4` Điều 11 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`)
- (`e5` 1 . Thống đốc Ngân hàng Nhà nước ủy quyền cho Giám đốc Ngân hàng Nhà nước chi nhánh tỉnh , thành phố xác nhận đăng ký việc mở , thay đổi tên và / hoặc địa điểm , chấm dứt hoạt động phòng giao dịch , quỹ tiết kiệm , ATM của ngân hàng thương mại trên địa bàn . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 11 `[DIEU]`)
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Ngân hàng `[LINH_VUC]`)
- (`e5` 1 . Thống đốc Ngân hàng Nhà nước ủy quyền cho Giám đốc Ngân hàng Nhà nước chi nhánh tỉnh , thành phố xác nhận đăng ký việc mở , thay đổi tên và / hoặc địa điểm , chấm dứt hoạt động phòng giao dịch , quỹ tiết kiệm , ATM của ngân hàng thương mại trên địa bàn . `[KHOAN]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Ngân hàng `[LINH_VUC]`)


---

### Mẫu #13_2008_QĐ-NHNN_32111#body_standalone_55 (Loại: `body_standalone`)
> **[Điều 11]`<DIEU>`** . **[1 . **[Thống đốc Ngân hàng Nhà nước]`<CO_QUAN_THAM_QUYEN>`** ủy quyền cho **[Giám đốc]`<CHU_THE_CA_NHAN>`** **[Ngân hàng Nhà nước chi nhánh tỉnh , thành phố]`<CO_QUAN_THAM_QUYEN>`** xác nhận đăng ký việc mở , thay đổi tên và / hoặc địa điểm , chấm dứt hoạt động phòng giao dịch , **[quỹ tiết kiệm]`<TO_CHUC_DOANH_NGHIEP>`** , ATM của **[ngân hàng thương mại]`<TO_CHUC_DOANH_NGHIEP>`** trên địa bàn .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 11** → `DIEU` (span: `[0:2]`)
- `[e1]` **1 . Thống đốc Ngân hàng Nhà nước ủy quyền cho Giám đốc Ngân hàng Nhà nước chi nhánh tỉnh , thành phố xác nhận đăng ký việc mở , thay đổi tên và / hoặc địa điểm , chấm dứt hoạt động phòng giao dịch , quỹ tiết kiệm , ATM của ngân hàng thương mại trên địa bàn .** → `KHOAN` (span: `[3:45]`)
- `[e2]` **ngân hàng thương mại** → `TO_CHUC_DOANH_NGHIEP` (span: `[40:42]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **quỹ tiết kiệm** → `TO_CHUC_DOANH_NGHIEP` (span: `[35:37]`) *(lồng trong `e1` (`KHOAN`))*
- `[e4]` **Thống đốc Ngân hàng Nhà nước** → `CO_QUAN_THAM_QUYEN` (span: `[5:8]`) *(lồng trong `e1` (`KHOAN`))*
- `[e5]` **Ngân hàng Nhà nước chi nhánh tỉnh , thành phố** → `CO_QUAN_THAM_QUYEN` (span: `[12:18]`) *(lồng trong `e1` (`KHOAN`))*
- `[e6]` **Giám đốc** → `CHU_THE_CA_NHAN` (span: `[11:12]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 1 . Thống đốc Ngân hàng Nhà nước ủy quyền cho Giám đốc Ngân hàng Nhà nước chi nhánh tỉnh , thành phố xác nhận đăng ký việc mở , thay đổi tên và / hoặc địa điểm , chấm dứt hoạt động phòng giao dịch , quỹ tiết kiệm , ATM của ngân hàng thương mại trên địa bàn . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 11 `[DIEU]`)


---

### Mẫu #13_2008_QĐ-NHNN_32111#body_context_56 (Loại: `body_context`)
> **[Quyết định]`<LOAI_VAN_BAN>`** số **[13/2008/QĐ-NHNN]`<SO_HIEU>`** ban hành **[ngày 29 tháng 04 năm 2008]`<NGAY_BAN_HANH>`** bởi **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_BAN_HANH>`** . **[Điều 11]`<DIEU>`** . **[3 . **[Ngân hàng thương mại]`<TO_CHUC_DOANH_NGHIEP>`** phải có văn bản đăng ký việc mở , thay đổi tên và / hoặc địa điểm , chấm dứt hoạt động phòng giao dịch , **[quỹ tiết kiệm]`<TO_CHUC_DOANH_NGHIEP>`** , ATM gửi **[Ngân hàng Nhà nước chi nhánh tỉnh , thành phố]`<CO_QUAN_THAM_QUYEN>`** theo **[Phụ lục 05]`<THAM_CHIEU_PHAP_LY>`** kèm theo Quy định này .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Quyết định** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **13/2008/QĐ-NHNN** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_BAN_HANH` (span: `[11:14]`)
- `[e3]` **ngày 29 tháng 04 năm 2008** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 11** → `DIEU` (span: `[15:17]`)
- `[e5]` **3 . Ngân hàng thương mại phải có văn bản đăng ký việc mở , thay đổi tên và / hoặc địa điểm , chấm dứt hoạt động phòng giao dịch , quỹ tiết kiệm , ATM gửi Ngân hàng Nhà nước chi nhánh tỉnh , thành phố theo Phụ lục 05 kèm theo Quy định này .** → `KHOAN` (span: `[18:60]`)
- `[e6]` **Ngân hàng thương mại** → `TO_CHUC_DOANH_NGHIEP` (span: `[20:22]`) *(lồng trong `e5` (`KHOAN`))*
- `[e7]` **quỹ tiết kiệm** → `TO_CHUC_DOANH_NGHIEP` (span: `[41:43]`) *(lồng trong `e5` (`KHOAN`))*
- `[e8]` **Phụ lục 05** → `THAM_CHIEU_PHAP_LY` (span: `[53:55]`) *(lồng trong `e5` (`KHOAN`))*
- `[e9]` **Ngân hàng Nhà nước chi nhánh tỉnh , thành phố** → `CO_QUAN_THAM_QUYEN` (span: `[46:52]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Ngân hàng Nhà nước Việt Nam `[CO_QUAN_BAN_HANH]`)
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Quyết định `[LOAI_VAN_BAN]`)
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 29 tháng 04 năm 2008 `[NGAY_BAN_HANH]`)
- (`e4` Điều 11 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`)
- (`e5` 3 . Ngân hàng thương mại phải có văn bản đăng ký việc mở , thay đổi tên và / hoặc địa điểm , chấm dứt hoạt động phòng giao dịch , quỹ tiết kiệm , ATM gửi Ngân hàng Nhà nước chi nhánh tỉnh , thành phố theo Phụ lục 05 kèm theo Quy định này . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 11 `[DIEU]`)
- (`e5` 3 . Ngân hàng thương mại phải có văn bản đăng ký việc mở , thay đổi tên và / hoặc địa điểm , chấm dứt hoạt động phòng giao dịch , quỹ tiết kiệm , ATM gửi Ngân hàng Nhà nước chi nhánh tỉnh , thành phố theo Phụ lục 05 kèm theo Quy định này . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e8` Phụ lục 05 `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #13_2008_QĐ-NHNN_32111#body_standalone_57 (Loại: `body_standalone`)
> **[Điều 11]`<DIEU>`** . **[3 . **[Ngân hàng thương mại]`<TO_CHUC_DOANH_NGHIEP>`** phải có văn bản đăng ký việc mở , thay đổi tên và / hoặc địa điểm , chấm dứt hoạt động phòng giao dịch , **[quỹ tiết kiệm]`<TO_CHUC_DOANH_NGHIEP>`** , ATM gửi **[Ngân hàng Nhà nước chi nhánh tỉnh , thành phố]`<CO_QUAN_THAM_QUYEN>`** theo **[Phụ lục 05]`<THAM_CHIEU_PHAP_LY>`** kèm theo Quy định này .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 11** → `DIEU` (span: `[0:2]`)
- `[e1]` **3 . Ngân hàng thương mại phải có văn bản đăng ký việc mở , thay đổi tên và / hoặc địa điểm , chấm dứt hoạt động phòng giao dịch , quỹ tiết kiệm , ATM gửi Ngân hàng Nhà nước chi nhánh tỉnh , thành phố theo Phụ lục 05 kèm theo Quy định này .** → `KHOAN` (span: `[3:45]`)
- `[e2]` **Ngân hàng thương mại** → `TO_CHUC_DOANH_NGHIEP` (span: `[5:7]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **quỹ tiết kiệm** → `TO_CHUC_DOANH_NGHIEP` (span: `[26:28]`) *(lồng trong `e1` (`KHOAN`))*
- `[e4]` **Phụ lục 05** → `THAM_CHIEU_PHAP_LY` (span: `[38:40]`) *(lồng trong `e1` (`KHOAN`))*
- `[e5]` **Ngân hàng Nhà nước chi nhánh tỉnh , thành phố** → `CO_QUAN_THAM_QUYEN` (span: `[31:37]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 3 . Ngân hàng thương mại phải có văn bản đăng ký việc mở , thay đổi tên và / hoặc địa điểm , chấm dứt hoạt động phòng giao dịch , quỹ tiết kiệm , ATM gửi Ngân hàng Nhà nước chi nhánh tỉnh , thành phố theo Phụ lục 05 kèm theo Quy định này . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 11 `[DIEU]`)
- (`e1` 3 . Ngân hàng thương mại phải có văn bản đăng ký việc mở , thay đổi tên và / hoặc địa điểm , chấm dứt hoạt động phòng giao dịch , quỹ tiết kiệm , ATM gửi Ngân hàng Nhà nước chi nhánh tỉnh , thành phố theo Phụ lục 05 kèm theo Quy định này . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e4` Phụ lục 05 `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #13_2008_QĐ-NHNN_32111#body_context_58 (Loại: `body_context`)
> **[Quyết định]`<LOAI_VAN_BAN>`** số **[13/2008/QĐ-NHNN]`<SO_HIEU>`** của **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Ngân hàng]`<LINH_VUC>`** . **[Điều 11]`<DIEU>`** . **[4 . Trong thời hạn năm ngày làm việc kể từ ngày nhận được văn bản đăng ký của **[ngân hàng thương mại]`<TO_CHUC_DOANH_NGHIEP>`** , **[Ngân hàng Nhà nước chi nhánh tỉnh , thành phố]`<CO_QUAN_THAM_QUYEN>`** có **[văn bản xác nhận]`<GIAY_TO_HO_SO>`** đăng ký mở , thay đổi tên và / hoặc địa điểm , chấm dứt hoạt động phòng giao dịch , **[quỹ tiết kiệm]`<TO_CHUC_DOANH_NGHIEP>`** , ATM theo **[Phụ lục 06]`<THAM_CHIEU_PHAP_LY>`** kèm theo Quy định này .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Quyết định** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **13/2008/QĐ-NHNN** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_BAN_HANH` (span: `[4:7]`)
- `[e3]` **Ngân hàng** → `LINH_VUC` (span: `[9:10]`)
- `[e4]` **Điều 11** → `DIEU` (span: `[11:13]`)
- `[e5]` **4 . Trong thời hạn năm ngày làm việc kể từ ngày nhận được văn bản đăng ký của ngân hàng thương mại , Ngân hàng Nhà nước chi nhánh tỉnh , thành phố có văn bản xác nhận đăng ký mở , thay đổi tên và / hoặc địa điểm , chấm dứt hoạt động phòng giao dịch , quỹ tiết kiệm , ATM theo Phụ lục 06 kèm theo Quy định này .** → `KHOAN` (span: `[14:68]`)
- `[e6]` **ngân hàng thương mại** → `TO_CHUC_DOANH_NGHIEP` (span: `[29:31]`) *(lồng trong `e5` (`KHOAN`))*
- `[e7]` **quỹ tiết kiệm** → `TO_CHUC_DOANH_NGHIEP` (span: `[56:58]`) *(lồng trong `e5` (`KHOAN`))*
- `[e8]` **Phụ lục 06** → `THAM_CHIEU_PHAP_LY` (span: `[61:63]`) *(lồng trong `e5` (`KHOAN`))*
- `[e9]` **Ngân hàng Nhà nước chi nhánh tỉnh , thành phố** → `CO_QUAN_THAM_QUYEN` (span: `[32:38]`) *(lồng trong `e5` (`KHOAN`))*
- `[e10]` **văn bản xác nhận** → `GIAY_TO_HO_SO` (span: `[39:41]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Ngân hàng Nhà nước Việt Nam `[CO_QUAN_BAN_HANH]`)
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Quyết định `[LOAI_VAN_BAN]`)
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Ngân hàng `[LINH_VUC]`)
- (`e4` Điều 11 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`)
- (`e5` 4 . Trong thời hạn năm ngày làm việc kể từ ngày nhận được văn bản đăng ký của ngân hàng thương mại , Ngân hàng Nhà nước chi nhánh tỉnh , thành phố có văn bản xác nhận đăng ký mở , thay đổi tên và / hoặc địa điểm , chấm dứt hoạt động phòng giao dịch , quỹ tiết kiệm , ATM theo Phụ lục 06 kèm theo Quy định này . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 11 `[DIEU]`)
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Ngân hàng `[LINH_VUC]`)
- (`e5` 4 . Trong thời hạn năm ngày làm việc kể từ ngày nhận được văn bản đăng ký của ngân hàng thương mại , Ngân hàng Nhà nước chi nhánh tỉnh , thành phố có văn bản xác nhận đăng ký mở , thay đổi tên và / hoặc địa điểm , chấm dứt hoạt động phòng giao dịch , quỹ tiết kiệm , ATM theo Phụ lục 06 kèm theo Quy định này . `[KHOAN]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Ngân hàng `[LINH_VUC]`)
- (`e5` 4 . Trong thời hạn năm ngày làm việc kể từ ngày nhận được văn bản đăng ký của ngân hàng thương mại , Ngân hàng Nhà nước chi nhánh tỉnh , thành phố có văn bản xác nhận đăng ký mở , thay đổi tên và / hoặc địa điểm , chấm dứt hoạt động phòng giao dịch , quỹ tiết kiệm , ATM theo Phụ lục 06 kèm theo Quy định này . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e8` Phụ lục 06 `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #13_2008_QĐ-NHNN_32111#body_standalone_59 (Loại: `body_standalone`)
> **[Điều 11]`<DIEU>`** . **[4 . Trong thời hạn năm ngày làm việc kể từ ngày nhận được văn bản đăng ký của **[ngân hàng thương mại]`<TO_CHUC_DOANH_NGHIEP>`** , **[Ngân hàng Nhà nước chi nhánh tỉnh , thành phố]`<CO_QUAN_THAM_QUYEN>`** có **[văn bản xác nhận]`<GIAY_TO_HO_SO>`** đăng ký mở , thay đổi tên và / hoặc địa điểm , chấm dứt hoạt động phòng giao dịch , **[quỹ tiết kiệm]`<TO_CHUC_DOANH_NGHIEP>`** , ATM theo **[Phụ lục 06]`<THAM_CHIEU_PHAP_LY>`** kèm theo Quy định này .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 11** → `DIEU` (span: `[0:2]`)
- `[e1]` **4 . Trong thời hạn năm ngày làm việc kể từ ngày nhận được văn bản đăng ký của ngân hàng thương mại , Ngân hàng Nhà nước chi nhánh tỉnh , thành phố có văn bản xác nhận đăng ký mở , thay đổi tên và / hoặc địa điểm , chấm dứt hoạt động phòng giao dịch , quỹ tiết kiệm , ATM theo Phụ lục 06 kèm theo Quy định này .** → `KHOAN` (span: `[3:57]`)
- `[e2]` **ngân hàng thương mại** → `TO_CHUC_DOANH_NGHIEP` (span: `[18:20]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **quỹ tiết kiệm** → `TO_CHUC_DOANH_NGHIEP` (span: `[45:47]`) *(lồng trong `e1` (`KHOAN`))*
- `[e4]` **Phụ lục 06** → `THAM_CHIEU_PHAP_LY` (span: `[50:52]`) *(lồng trong `e1` (`KHOAN`))*
- `[e5]` **Ngân hàng Nhà nước chi nhánh tỉnh , thành phố** → `CO_QUAN_THAM_QUYEN` (span: `[21:27]`) *(lồng trong `e1` (`KHOAN`))*
- `[e6]` **văn bản xác nhận** → `GIAY_TO_HO_SO` (span: `[28:30]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 4 . Trong thời hạn năm ngày làm việc kể từ ngày nhận được văn bản đăng ký của ngân hàng thương mại , Ngân hàng Nhà nước chi nhánh tỉnh , thành phố có văn bản xác nhận đăng ký mở , thay đổi tên và / hoặc địa điểm , chấm dứt hoạt động phòng giao dịch , quỹ tiết kiệm , ATM theo Phụ lục 06 kèm theo Quy định này . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 11 `[DIEU]`)
- (`e1` 4 . Trong thời hạn năm ngày làm việc kể từ ngày nhận được văn bản đăng ký của ngân hàng thương mại , Ngân hàng Nhà nước chi nhánh tỉnh , thành phố có văn bản xác nhận đăng ký mở , thay đổi tên và / hoặc địa điểm , chấm dứt hoạt động phòng giao dịch , quỹ tiết kiệm , ATM theo Phụ lục 06 kèm theo Quy định này . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e4` Phụ lục 06 `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #13_2008_QĐ-NHNN_32111#body_context_60 (Loại: `body_context`)
> **[Quyết định]`<LOAI_VAN_BAN>`** số **[13/2008/QĐ-NHNN]`<SO_HIEU>`** ban hành **[ngày 29 tháng 04 năm 2008]`<NGAY_BAN_HANH>`** bởi **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_BAN_HANH>`** . **[Điều 12]`<DIEU>`** . **[Khoản 1]`<KHOAN>`** . **[a ) Tự nguyện chấm dứt hoạt động .]`<DIEM>`**

**Thực thể:**
- `[e0]` **Quyết định** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **13/2008/QĐ-NHNN** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_BAN_HANH` (span: `[11:14]`)
- `[e3]` **ngày 29 tháng 04 năm 2008** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 12** → `DIEU` (span: `[15:17]`)
- `[e5]` **Khoản 1** → `KHOAN` (span: `[18:20]`)
- `[e6]` **a ) Tự nguyện chấm dứt hoạt động .** → `DIEM` (span: `[21:27]`)

**Quan hệ:**
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Ngân hàng Nhà nước Việt Nam `[CO_QUAN_BAN_HANH]`)
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Quyết định `[LOAI_VAN_BAN]`)
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 29 tháng 04 năm 2008 `[NGAY_BAN_HANH]`)
- (`e4` Điều 12 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`)
- (`e5` Khoản 1 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 12 `[DIEU]`)
- (`e6` a ) Tự nguyện chấm dứt hoạt động . `[DIEM]`) ==[ **THUOC_VE** ]==> (`e5` Khoản 1 `[KHOAN]`)


---

### Mẫu #13_2008_QĐ-NHNN_32111#body_context_61 (Loại: `body_context`)
> **[Quyết định]`<LOAI_VAN_BAN>`** số **[13/2008/QĐ-NHNN]`<SO_HIEU>`** ban hành **[ngày 29 tháng 04 năm 2008]`<NGAY_BAN_HANH>`** bởi **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_BAN_HANH>`** . **[Điều 13]`<DIEU>`** . **[Khoản 1]`<KHOAN>`** . **[a ) Văn bản của Chủ tịch **[Hội đồng quản trị]`<TO_CHUC_DOANH_NGHIEP>`** **[ngân hàng thương mại]`<TO_CHUC_DOANH_NGHIEP>`** đề nghị chấm dứt hoạt động **[sở giao dịch]`<CO_QUAN_THAM_QUYEN>`** , chi nhánh , **[văn phòng đại diện]`<TO_CHUC_DOANH_NGHIEP>`** , **[đơn vị sự nghiệp]`<TO_CHUC_DOANH_NGHIEP>`** theo **[Phụ lục 07]`<THAM_CHIEU_PHAP_LY>`** kèm theo Quy định này ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Quyết định** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **13/2008/QĐ-NHNN** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_BAN_HANH` (span: `[11:14]`)
- `[e3]` **ngày 29 tháng 04 năm 2008** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 13** → `DIEU` (span: `[15:17]`)
- `[e5]` **Khoản 1** → `KHOAN` (span: `[18:20]`)
- `[e6]` **a ) Văn bản của Chủ tịch Hội đồng quản trị ngân hàng thương mại đề nghị chấm dứt hoạt động sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp theo Phụ lục 07 kèm theo Quy định này ;** → `DIEM` (span: `[21:51]`)
- `[e7]` **sở giao dịch** → `CO_QUAN_THAM_QUYEN` (span: `[33:35]`) *(lồng trong `e6` (`DIEM`))*
- `[e8]` **ngân hàng thương mại** → `TO_CHUC_DOANH_NGHIEP` (span: `[28:30]`) *(lồng trong `e6` (`DIEM`))*
- `[e9]` **văn phòng đại diện** → `TO_CHUC_DOANH_NGHIEP` (span: `[38:40]`) *(lồng trong `e6` (`DIEM`))*
- `[e10]` **đơn vị sự nghiệp** → `TO_CHUC_DOANH_NGHIEP` (span: `[41:43]`) *(lồng trong `e6` (`DIEM`))*
- `[e11]` **Phụ lục 07** → `THAM_CHIEU_PHAP_LY` (span: `[44:46]`) *(lồng trong `e6` (`DIEM`))*
- `[e12]` **Hội đồng quản trị** → `TO_CHUC_DOANH_NGHIEP` (span: `[26:28]`) *(lồng trong `e6` (`DIEM`))*

**Quan hệ:**
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Ngân hàng Nhà nước Việt Nam `[CO_QUAN_BAN_HANH]`)
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Quyết định `[LOAI_VAN_BAN]`)
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 29 tháng 04 năm 2008 `[NGAY_BAN_HANH]`)
- (`e4` Điều 13 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`)
- (`e5` Khoản 1 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 13 `[DIEU]`)
- (`e6` a ) Văn bản của Chủ tịch Hội đồng quản trị ngân hàng thương mại đề nghị chấm dứt hoạt động sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp theo Phụ lục 07 kèm theo Quy định này ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e5` Khoản 1 `[KHOAN]`)
- (`e6` a ) Văn bản của Chủ tịch Hội đồng quản trị ngân hàng thương mại đề nghị chấm dứt hoạt động sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp theo Phụ lục 07 kèm theo Quy định này ; `[DIEM]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e11` Phụ lục 07 `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #13_2008_QĐ-NHNN_32111#body_standalone_62 (Loại: `body_standalone`)
> **[Điều 13]`<DIEU>`** . **[Khoản 1]`<KHOAN>`** . **[a ) Văn bản của Chủ tịch **[Hội đồng quản trị]`<TO_CHUC_DOANH_NGHIEP>`** **[ngân hàng thương mại]`<TO_CHUC_DOANH_NGHIEP>`** đề nghị chấm dứt hoạt động **[sở giao dịch]`<CO_QUAN_THAM_QUYEN>`** , chi nhánh , **[văn phòng đại diện]`<TO_CHUC_DOANH_NGHIEP>`** , **[đơn vị sự nghiệp]`<TO_CHUC_DOANH_NGHIEP>`** theo **[Phụ lục 07]`<THAM_CHIEU_PHAP_LY>`** kèm theo Quy định này ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Điều 13** → `DIEU` (span: `[0:2]`)
- `[e1]` **Khoản 1** → `KHOAN` (span: `[3:5]`)
- `[e2]` **a ) Văn bản của Chủ tịch Hội đồng quản trị ngân hàng thương mại đề nghị chấm dứt hoạt động sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp theo Phụ lục 07 kèm theo Quy định này ;** → `DIEM` (span: `[6:36]`)
- `[e3]` **sở giao dịch** → `CO_QUAN_THAM_QUYEN` (span: `[18:20]`) *(lồng trong `e2` (`DIEM`))*
- `[e4]` **ngân hàng thương mại** → `TO_CHUC_DOANH_NGHIEP` (span: `[13:15]`) *(lồng trong `e2` (`DIEM`))*
- `[e5]` **văn phòng đại diện** → `TO_CHUC_DOANH_NGHIEP` (span: `[23:25]`) *(lồng trong `e2` (`DIEM`))*
- `[e6]` **đơn vị sự nghiệp** → `TO_CHUC_DOANH_NGHIEP` (span: `[26:28]`) *(lồng trong `e2` (`DIEM`))*
- `[e7]` **Phụ lục 07** → `THAM_CHIEU_PHAP_LY` (span: `[29:31]`) *(lồng trong `e2` (`DIEM`))*
- `[e8]` **Hội đồng quản trị** → `TO_CHUC_DOANH_NGHIEP` (span: `[11:13]`) *(lồng trong `e2` (`DIEM`))*

**Quan hệ:**
- (`e1` Khoản 1 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 13 `[DIEU]`)
- (`e2` a ) Văn bản của Chủ tịch Hội đồng quản trị ngân hàng thương mại đề nghị chấm dứt hoạt động sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp theo Phụ lục 07 kèm theo Quy định này ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e1` Khoản 1 `[KHOAN]`)
- (`e2` a ) Văn bản của Chủ tịch Hội đồng quản trị ngân hàng thương mại đề nghị chấm dứt hoạt động sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp theo Phụ lục 07 kèm theo Quy định này ; `[DIEM]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e7` Phụ lục 07 `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #13_2008_QĐ-NHNN_32111#body_context_63 (Loại: `body_context`)
> **[Quyết định]`<LOAI_VAN_BAN>`** số **[13/2008/QĐ-NHNN]`<SO_HIEU>`** ban hành **[ngày 29 tháng 04 năm 2008]`<NGAY_BAN_HANH>`** bởi **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_BAN_HANH>`** . **[Điều 13]`<DIEU>`** . **[2 . Trong thời hạn ba mươi ngày làm việc kể từ ngày nhận đủ hồ sơ **[quy định tại]`<TU_KHOA_PHAP_LY>`** **[Khoản 1 Điều này]`<THAM_CHIEU_PHAP_LY>`** , **[Ngân hàng Nhà nước]`<CO_QUAN_THAM_QUYEN>`** có **[văn bản chấp thuận]`<GIAY_TO_HO_SO>`** đề nghị chấm dứt hoạt động **[sở giao dịch]`<CO_QUAN_THAM_QUYEN>`** , chi nhánh , **[văn phòng đại diện]`<TO_CHUC_DOANH_NGHIEP>`** , **[đơn vị sự nghiệp]`<TO_CHUC_DOANH_NGHIEP>`** của **[ngân hàng thương mại]`<TO_CHUC_DOANH_NGHIEP>`** theo **[Phụ lục 08]`<THAM_CHIEU_PHAP_LY>`** kèm theo Quy định này ; trường hợp không chấp thuận , có văn bản nêu rõ lý do hoặc các yêu cầu ( nếu có ) để chấm dứt hoạt động .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Quyết định** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **13/2008/QĐ-NHNN** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_BAN_HANH` (span: `[11:14]`)
- `[e3]` **ngày 29 tháng 04 năm 2008** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 13** → `DIEU` (span: `[15:17]`)
- `[e5]` **2 . Trong thời hạn ba mươi ngày làm việc kể từ ngày nhận đủ hồ sơ quy định tại Khoản 1 Điều này , Ngân hàng Nhà nước có văn bản chấp thuận đề nghị chấm dứt hoạt động sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp của ngân hàng thương mại theo Phụ lục 08 kèm theo Quy định này ; trường hợp không chấp thuận , có văn bản nêu rõ lý do hoặc các yêu cầu ( nếu có ) để chấm dứt hoạt động .** → `KHOAN` (span: `[18:88]`)
- `[e6]` **sở giao dịch** → `CO_QUAN_THAM_QUYEN` (span: `[47:49]`) *(lồng trong `e5` (`KHOAN`))*
- `[e7]` **ngân hàng thương mại** → `TO_CHUC_DOANH_NGHIEP` (span: `[58:60]`) *(lồng trong `e5` (`KHOAN`))*
- `[e8]` **văn phòng đại diện** → `TO_CHUC_DOANH_NGHIEP` (span: `[52:54]`) *(lồng trong `e5` (`KHOAN`))*
- `[e9]` **đơn vị sự nghiệp** → `TO_CHUC_DOANH_NGHIEP` (span: `[55:57]`) *(lồng trong `e5` (`KHOAN`))*
- `[e10]` **Khoản 1 Điều này** → `THAM_CHIEU_PHAP_LY` (span: `[34:38]`) *(lồng trong `e5` (`KHOAN`))*
- `[e11]` **Phụ lục 08** → `THAM_CHIEU_PHAP_LY` (span: `[61:63]`) *(lồng trong `e5` (`KHOAN`))*
- `[e12]` **quy định tại** → `TU_KHOA_PHAP_LY` (span: `[32:34]`) *(lồng trong `e5` (`KHOAN`))*
- `[e13]` **Ngân hàng Nhà nước** → `CO_QUAN_THAM_QUYEN` (span: `[39:41]`) *(lồng trong `e5` (`KHOAN`))*
- `[e14]` **văn bản chấp thuận** → `GIAY_TO_HO_SO` (span: `[42:44]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Ngân hàng Nhà nước Việt Nam `[CO_QUAN_BAN_HANH]`)
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Quyết định `[LOAI_VAN_BAN]`)
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 29 tháng 04 năm 2008 `[NGAY_BAN_HANH]`)
- (`e4` Điều 13 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`)
- (`e5` 2 . Trong thời hạn ba mươi ngày làm việc kể từ ngày nhận đủ hồ sơ quy định tại Khoản 1 Điều này , Ngân hàng Nhà nước có văn bản chấp thuận đề nghị chấm dứt hoạt động sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp của ngân hàng thương mại theo Phụ lục 08 kèm theo Quy định này ; trường hợp không chấp thuận , có văn bản nêu rõ lý do hoặc các yêu cầu ( nếu có ) để chấm dứt hoạt động . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 13 `[DIEU]`)
- (`e12` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e10` Khoản 1 Điều này `[THAM_CHIEU_PHAP_LY]`)
- (`e5` 2 . Trong thời hạn ba mươi ngày làm việc kể từ ngày nhận đủ hồ sơ quy định tại Khoản 1 Điều này , Ngân hàng Nhà nước có văn bản chấp thuận đề nghị chấm dứt hoạt động sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp của ngân hàng thương mại theo Phụ lục 08 kèm theo Quy định này ; trường hợp không chấp thuận , có văn bản nêu rõ lý do hoặc các yêu cầu ( nếu có ) để chấm dứt hoạt động . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e10` Khoản 1 Điều này `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e12` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e11` Phụ lục 08 `[THAM_CHIEU_PHAP_LY]`)
- (`e5` 2 . Trong thời hạn ba mươi ngày làm việc kể từ ngày nhận đủ hồ sơ quy định tại Khoản 1 Điều này , Ngân hàng Nhà nước có văn bản chấp thuận đề nghị chấm dứt hoạt động sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp của ngân hàng thương mại theo Phụ lục 08 kèm theo Quy định này ; trường hợp không chấp thuận , có văn bản nêu rõ lý do hoặc các yêu cầu ( nếu có ) để chấm dứt hoạt động . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e11` Phụ lục 08 `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #13_2008_QĐ-NHNN_32111#body_standalone_64 (Loại: `body_standalone`)
> **[Điều 13]`<DIEU>`** . **[2 . Trong thời hạn ba mươi ngày làm việc kể từ ngày nhận đủ hồ sơ **[quy định tại]`<TU_KHOA_PHAP_LY>`** **[Khoản 1 Điều này]`<THAM_CHIEU_PHAP_LY>`** , **[Ngân hàng Nhà nước]`<CO_QUAN_THAM_QUYEN>`** có **[văn bản chấp thuận]`<GIAY_TO_HO_SO>`** đề nghị chấm dứt hoạt động **[sở giao dịch]`<CO_QUAN_THAM_QUYEN>`** , chi nhánh , **[văn phòng đại diện]`<TO_CHUC_DOANH_NGHIEP>`** , **[đơn vị sự nghiệp]`<TO_CHUC_DOANH_NGHIEP>`** của **[ngân hàng thương mại]`<TO_CHUC_DOANH_NGHIEP>`** theo **[Phụ lục 08]`<THAM_CHIEU_PHAP_LY>`** kèm theo Quy định này ; trường hợp không chấp thuận , có văn bản nêu rõ lý do hoặc các yêu cầu ( nếu có ) để chấm dứt hoạt động .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 13** → `DIEU` (span: `[0:2]`)
- `[e1]` **2 . Trong thời hạn ba mươi ngày làm việc kể từ ngày nhận đủ hồ sơ quy định tại Khoản 1 Điều này , Ngân hàng Nhà nước có văn bản chấp thuận đề nghị chấm dứt hoạt động sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp của ngân hàng thương mại theo Phụ lục 08 kèm theo Quy định này ; trường hợp không chấp thuận , có văn bản nêu rõ lý do hoặc các yêu cầu ( nếu có ) để chấm dứt hoạt động .** → `KHOAN` (span: `[3:73]`)
- `[e2]` **sở giao dịch** → `CO_QUAN_THAM_QUYEN` (span: `[32:34]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **ngân hàng thương mại** → `TO_CHUC_DOANH_NGHIEP` (span: `[43:45]`) *(lồng trong `e1` (`KHOAN`))*
- `[e4]` **văn phòng đại diện** → `TO_CHUC_DOANH_NGHIEP` (span: `[37:39]`) *(lồng trong `e1` (`KHOAN`))*
- `[e5]` **đơn vị sự nghiệp** → `TO_CHUC_DOANH_NGHIEP` (span: `[40:42]`) *(lồng trong `e1` (`KHOAN`))*
- `[e6]` **Khoản 1 Điều này** → `THAM_CHIEU_PHAP_LY` (span: `[19:23]`) *(lồng trong `e1` (`KHOAN`))*
- `[e7]` **Phụ lục 08** → `THAM_CHIEU_PHAP_LY` (span: `[46:48]`) *(lồng trong `e1` (`KHOAN`))*
- `[e8]` **quy định tại** → `TU_KHOA_PHAP_LY` (span: `[17:19]`) *(lồng trong `e1` (`KHOAN`))*
- `[e9]` **Ngân hàng Nhà nước** → `CO_QUAN_THAM_QUYEN` (span: `[24:26]`) *(lồng trong `e1` (`KHOAN`))*
- `[e10]` **văn bản chấp thuận** → `GIAY_TO_HO_SO` (span: `[27:29]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 2 . Trong thời hạn ba mươi ngày làm việc kể từ ngày nhận đủ hồ sơ quy định tại Khoản 1 Điều này , Ngân hàng Nhà nước có văn bản chấp thuận đề nghị chấm dứt hoạt động sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp của ngân hàng thương mại theo Phụ lục 08 kèm theo Quy định này ; trường hợp không chấp thuận , có văn bản nêu rõ lý do hoặc các yêu cầu ( nếu có ) để chấm dứt hoạt động . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 13 `[DIEU]`)
- (`e8` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e6` Khoản 1 Điều này `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 2 . Trong thời hạn ba mươi ngày làm việc kể từ ngày nhận đủ hồ sơ quy định tại Khoản 1 Điều này , Ngân hàng Nhà nước có văn bản chấp thuận đề nghị chấm dứt hoạt động sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp của ngân hàng thương mại theo Phụ lục 08 kèm theo Quy định này ; trường hợp không chấp thuận , có văn bản nêu rõ lý do hoặc các yêu cầu ( nếu có ) để chấm dứt hoạt động . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e6` Khoản 1 Điều này `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e8` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e7` Phụ lục 08 `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 2 . Trong thời hạn ba mươi ngày làm việc kể từ ngày nhận đủ hồ sơ quy định tại Khoản 1 Điều này , Ngân hàng Nhà nước có văn bản chấp thuận đề nghị chấm dứt hoạt động sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp của ngân hàng thương mại theo Phụ lục 08 kèm theo Quy định này ; trường hợp không chấp thuận , có văn bản nêu rõ lý do hoặc các yêu cầu ( nếu có ) để chấm dứt hoạt động . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e7` Phụ lục 08 `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #13_2008_QĐ-NHNN_32111#body_context_65 (Loại: `body_context`)
> **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_BAN_HANH>`** ban hành **[Quyết định]`<LOAI_VAN_BAN>`** số **[13/2008/QĐ-NHNN]`<SO_HIEU>`** . **[Điều 13]`<DIEU>`** . **[3 . Trong thời hạn mười lăm ngày làm việc kể từ ngày có **[văn bản chấp thuận]`<GIAY_TO_HO_SO>`** của **[Ngân hàng Nhà nước]`<CO_QUAN_THAM_QUYEN>`** , Chủ tịch **[Hội đồng quản trị]`<TO_CHUC_DOANH_NGHIEP>`** **[ngân hàng thương mại]`<TO_CHUC_DOANH_NGHIEP>`** phải ra quyết định chấm dứt hoạt động **[sở giao dịch]`<CO_QUAN_THAM_QUYEN>`** , chi nhánh , **[văn phòng đại diện]`<TO_CHUC_DOANH_NGHIEP>`** , **[đơn vị sự nghiệp]`<TO_CHUC_DOANH_NGHIEP>`** và thực hiện các thủ tục pháp lý theo quy định của pháp luật .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Quyết định** → `LOAI_VAN_BAN` (span: `[4:5]`)
- `[e1]` **13/2008/QĐ-NHNN** → `SO_HIEU` (span: `[6:7]`)
- `[e2]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_BAN_HANH` (span: `[0:3]`)
- `[e3]` **Điều 13** → `DIEU` (span: `[8:10]`)
- `[e4]` **3 . Trong thời hạn mười lăm ngày làm việc kể từ ngày có văn bản chấp thuận của Ngân hàng Nhà nước , Chủ tịch Hội đồng quản trị ngân hàng thương mại phải ra quyết định chấm dứt hoạt động sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp và thực hiện các thủ tục pháp lý theo quy định của pháp luật .** → `KHOAN` (span: `[11:59]`)
- `[e5]` **sở giao dịch** → `CO_QUAN_THAM_QUYEN` (span: `[39:41]`) *(lồng trong `e4` (`KHOAN`))*
- `[e6]` **ngân hàng thương mại** → `TO_CHUC_DOANH_NGHIEP` (span: `[32:34]`) *(lồng trong `e4` (`KHOAN`))*
- `[e7]` **văn phòng đại diện** → `TO_CHUC_DOANH_NGHIEP` (span: `[44:46]`) *(lồng trong `e4` (`KHOAN`))*
- `[e8]` **đơn vị sự nghiệp** → `TO_CHUC_DOANH_NGHIEP` (span: `[47:49]`) *(lồng trong `e4` (`KHOAN`))*
- `[e9]` **Ngân hàng Nhà nước** → `CO_QUAN_THAM_QUYEN` (span: `[26:28]`) *(lồng trong `e4` (`KHOAN`))*
- `[e10]` **văn bản chấp thuận** → `GIAY_TO_HO_SO` (span: `[23:25]`) *(lồng trong `e4` (`KHOAN`))*
- `[e11]` **Hội đồng quản trị** → `TO_CHUC_DOANH_NGHIEP` (span: `[30:32]`) *(lồng trong `e4` (`KHOAN`))*

**Quan hệ:**
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Ngân hàng Nhà nước Việt Nam `[CO_QUAN_BAN_HANH]`)
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Quyết định `[LOAI_VAN_BAN]`)
- (`e3` Điều 13 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`)
- (`e4` 3 . Trong thời hạn mười lăm ngày làm việc kể từ ngày có văn bản chấp thuận của Ngân hàng Nhà nước , Chủ tịch Hội đồng quản trị ngân hàng thương mại phải ra quyết định chấm dứt hoạt động sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp và thực hiện các thủ tục pháp lý theo quy định của pháp luật . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 13 `[DIEU]`)


---

### Mẫu #13_2008_QĐ-NHNN_32111#body_standalone_66 (Loại: `body_standalone`)
> **[Điều 13]`<DIEU>`** . **[3 . Trong thời hạn mười lăm ngày làm việc kể từ ngày có **[văn bản chấp thuận]`<GIAY_TO_HO_SO>`** của **[Ngân hàng Nhà nước]`<CO_QUAN_THAM_QUYEN>`** , Chủ tịch **[Hội đồng quản trị]`<TO_CHUC_DOANH_NGHIEP>`** **[ngân hàng thương mại]`<TO_CHUC_DOANH_NGHIEP>`** phải ra quyết định chấm dứt hoạt động **[sở giao dịch]`<CO_QUAN_THAM_QUYEN>`** , chi nhánh , **[văn phòng đại diện]`<TO_CHUC_DOANH_NGHIEP>`** , **[đơn vị sự nghiệp]`<TO_CHUC_DOANH_NGHIEP>`** và thực hiện các thủ tục pháp lý theo quy định của pháp luật .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 13** → `DIEU` (span: `[0:2]`)
- `[e1]` **3 . Trong thời hạn mười lăm ngày làm việc kể từ ngày có văn bản chấp thuận của Ngân hàng Nhà nước , Chủ tịch Hội đồng quản trị ngân hàng thương mại phải ra quyết định chấm dứt hoạt động sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp và thực hiện các thủ tục pháp lý theo quy định của pháp luật .** → `KHOAN` (span: `[3:51]`)
- `[e2]` **sở giao dịch** → `CO_QUAN_THAM_QUYEN` (span: `[31:33]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **ngân hàng thương mại** → `TO_CHUC_DOANH_NGHIEP` (span: `[24:26]`) *(lồng trong `e1` (`KHOAN`))*
- `[e4]` **văn phòng đại diện** → `TO_CHUC_DOANH_NGHIEP` (span: `[36:38]`) *(lồng trong `e1` (`KHOAN`))*
- `[e5]` **đơn vị sự nghiệp** → `TO_CHUC_DOANH_NGHIEP` (span: `[39:41]`) *(lồng trong `e1` (`KHOAN`))*
- `[e6]` **Ngân hàng Nhà nước** → `CO_QUAN_THAM_QUYEN` (span: `[18:20]`) *(lồng trong `e1` (`KHOAN`))*
- `[e7]` **văn bản chấp thuận** → `GIAY_TO_HO_SO` (span: `[15:17]`) *(lồng trong `e1` (`KHOAN`))*
- `[e8]` **Hội đồng quản trị** → `TO_CHUC_DOANH_NGHIEP` (span: `[22:24]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 3 . Trong thời hạn mười lăm ngày làm việc kể từ ngày có văn bản chấp thuận của Ngân hàng Nhà nước , Chủ tịch Hội đồng quản trị ngân hàng thương mại phải ra quyết định chấm dứt hoạt động sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp và thực hiện các thủ tục pháp lý theo quy định của pháp luật . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 13 `[DIEU]`)


---

### Mẫu #13_2008_QĐ-NHNN_32111#body_context_67 (Loại: `body_context`)
> **[Quyết định]`<LOAI_VAN_BAN>`** số **[13/2008/QĐ-NHNN]`<SO_HIEU>`** của **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Ngân hàng]`<LINH_VUC>`** . **[Điều 13]`<DIEU>`** . **[Khoản 3]`<KHOAN>`** . **[b ) Lý do chấm dứt hoạt động **[sở giao dịch]`<CO_QUAN_THAM_QUYEN>`** , chi nhánh , **[văn phòng đại diện]`<TO_CHUC_DOANH_NGHIEP>`** , **[đơn vị sự nghiệp]`<TO_CHUC_DOANH_NGHIEP>`** ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Quyết định** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **13/2008/QĐ-NHNN** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_BAN_HANH` (span: `[4:7]`)
- `[e3]` **Ngân hàng** → `LINH_VUC` (span: `[9:10]`)
- `[e4]` **Điều 13** → `DIEU` (span: `[11:13]`)
- `[e5]` **Khoản 3** → `KHOAN` (span: `[14:16]`)
- `[e6]` **b ) Lý do chấm dứt hoạt động sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp ;** → `DIEM` (span: `[17:33]`)
- `[e7]` **sở giao dịch** → `CO_QUAN_THAM_QUYEN` (span: `[22:24]`) *(lồng trong `e6` (`DIEM`))*
- `[e8]` **văn phòng đại diện** → `TO_CHUC_DOANH_NGHIEP` (span: `[27:29]`) *(lồng trong `e6` (`DIEM`))*
- `[e9]` **đơn vị sự nghiệp** → `TO_CHUC_DOANH_NGHIEP` (span: `[30:32]`) *(lồng trong `e6` (`DIEM`))*

**Quan hệ:**
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Ngân hàng Nhà nước Việt Nam `[CO_QUAN_BAN_HANH]`)
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Quyết định `[LOAI_VAN_BAN]`)
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Ngân hàng `[LINH_VUC]`)
- (`e4` Điều 13 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`)
- (`e5` Khoản 3 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 13 `[DIEU]`)
- (`e6` b ) Lý do chấm dứt hoạt động sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e5` Khoản 3 `[KHOAN]`)
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Ngân hàng `[LINH_VUC]`)
- (`e6` b ) Lý do chấm dứt hoạt động sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp ; `[DIEM]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Ngân hàng `[LINH_VUC]`)


---

### Mẫu #13_2008_QĐ-NHNN_32111#body_standalone_68 (Loại: `body_standalone`)
> **[Điều 13]`<DIEU>`** . **[Khoản 3]`<KHOAN>`** . **[b ) Lý do chấm dứt hoạt động **[sở giao dịch]`<CO_QUAN_THAM_QUYEN>`** , chi nhánh , **[văn phòng đại diện]`<TO_CHUC_DOANH_NGHIEP>`** , **[đơn vị sự nghiệp]`<TO_CHUC_DOANH_NGHIEP>`** ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Điều 13** → `DIEU` (span: `[0:2]`)
- `[e1]` **Khoản 3** → `KHOAN` (span: `[3:5]`)
- `[e2]` **b ) Lý do chấm dứt hoạt động sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp ;** → `DIEM` (span: `[6:22]`)
- `[e3]` **sở giao dịch** → `CO_QUAN_THAM_QUYEN` (span: `[11:13]`) *(lồng trong `e2` (`DIEM`))*
- `[e4]` **văn phòng đại diện** → `TO_CHUC_DOANH_NGHIEP` (span: `[16:18]`) *(lồng trong `e2` (`DIEM`))*
- `[e5]` **đơn vị sự nghiệp** → `TO_CHUC_DOANH_NGHIEP` (span: `[19:21]`) *(lồng trong `e2` (`DIEM`))*

**Quan hệ:**
- (`e1` Khoản 3 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 13 `[DIEU]`)
- (`e2` b ) Lý do chấm dứt hoạt động sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e1` Khoản 3 `[KHOAN]`)


---

### Mẫu #13_2008_QĐ-NHNN_32111#body_context_69 (Loại: `body_context`)
> **[Quyết định]`<LOAI_VAN_BAN>`** số **[13/2008/QĐ-NHNN]`<SO_HIEU>`** của **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Ngân hàng]`<LINH_VUC>`** . **[Điều 14 . Bắt **[buộc chấm dứt hoạt động **[sở giao dịch]`<CO_QUAN_THAM_QUYEN>`**]`<BIEN_PHAP_KHAC_PHUC>`** , chi nhánh , **[văn phòng đại diện]`<TO_CHUC_DOANH_NGHIEP>`** , **[đơn vị sự nghiệp]`<TO_CHUC_DOANH_NGHIEP>`** ở trong nước]`<DIEU>`**

**Thực thể:**
- `[e0]` **Quyết định** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **13/2008/QĐ-NHNN** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_BAN_HANH` (span: `[4:7]`)
- `[e3]` **Ngân hàng** → `LINH_VUC` (span: `[9:10]`)
- `[e4]` **Điều 14 . Bắt buộc chấm dứt hoạt động sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp ở trong nước** → `DIEU` (span: `[11:31]`)
- `[e5]` **buộc chấm dứt hoạt động sở giao dịch** → `BIEN_PHAP_KHAC_PHUC` (span: `[15:20]`) *(lồng trong `e4` (`DIEU`))*
- `[e6]` **sở giao dịch** → `CO_QUAN_THAM_QUYEN` (span: `[18:20]`) *(lồng trong `e4` (`DIEU`), `e5` (`BIEN_PHAP_KHAC_PHUC`))*
- `[e7]` **văn phòng đại diện** → `TO_CHUC_DOANH_NGHIEP` (span: `[23:25]`) *(lồng trong `e4` (`DIEU`))*
- `[e8]` **đơn vị sự nghiệp** → `TO_CHUC_DOANH_NGHIEP` (span: `[26:28]`) *(lồng trong `e4` (`DIEU`))*

**Quan hệ:**
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Ngân hàng Nhà nước Việt Nam `[CO_QUAN_BAN_HANH]`)
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Quyết định `[LOAI_VAN_BAN]`)
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Ngân hàng `[LINH_VUC]`)
- (`e4` Điều 14 . Bắt buộc chấm dứt hoạt động sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp ở trong nước `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`)
- (`e5` buộc chấm dứt hoạt động sở giao dịch `[BIEN_PHAP_KHAC_PHUC]`) ==[ **TAC_DONG_CHU_THE** ]==> (`e6` sở giao dịch `[CO_QUAN_THAM_QUYEN]`) *(Quan hệ lồng nhau)*
- (`e7` văn phòng đại diện `[TO_CHUC_DOANH_NGHIEP]`) ==[ **CHIU_CHE_TAI** ]==> (`e5` buộc chấm dứt hoạt động sở giao dịch `[BIEN_PHAP_KHAC_PHUC]`)
- (`e8` đơn vị sự nghiệp `[TO_CHUC_DOANH_NGHIEP]`) ==[ **CHIU_CHE_TAI** ]==> (`e5` buộc chấm dứt hoạt động sở giao dịch `[BIEN_PHAP_KHAC_PHUC]`)
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Ngân hàng `[LINH_VUC]`)
- (`e5` buộc chấm dứt hoạt động sở giao dịch `[BIEN_PHAP_KHAC_PHUC]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Ngân hàng `[LINH_VUC]`)


---

### Mẫu #13_2008_QĐ-NHNN_32111#body_standalone_70 (Loại: `body_standalone`)
> **[Điều 14 . Bắt **[buộc chấm dứt hoạt động **[sở giao dịch]`<CO_QUAN_THAM_QUYEN>`**]`<BIEN_PHAP_KHAC_PHUC>`** , chi nhánh , **[văn phòng đại diện]`<TO_CHUC_DOANH_NGHIEP>`** , **[đơn vị sự nghiệp]`<TO_CHUC_DOANH_NGHIEP>`** ở trong nước]`<DIEU>`**

**Thực thể:**
- `[e0]` **Điều 14 . Bắt buộc chấm dứt hoạt động sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp ở trong nước** → `DIEU` (span: `[0:20]`)
- `[e1]` **buộc chấm dứt hoạt động sở giao dịch** → `BIEN_PHAP_KHAC_PHUC` (span: `[4:9]`) *(lồng trong `e0` (`DIEU`))*
- `[e2]` **sở giao dịch** → `CO_QUAN_THAM_QUYEN` (span: `[7:9]`) *(lồng trong `e0` (`DIEU`), `e1` (`BIEN_PHAP_KHAC_PHUC`))*
- `[e3]` **văn phòng đại diện** → `TO_CHUC_DOANH_NGHIEP` (span: `[12:14]`) *(lồng trong `e0` (`DIEU`))*
- `[e4]` **đơn vị sự nghiệp** → `TO_CHUC_DOANH_NGHIEP` (span: `[15:17]`) *(lồng trong `e0` (`DIEU`))*

**Quan hệ:**
- (`e1` buộc chấm dứt hoạt động sở giao dịch `[BIEN_PHAP_KHAC_PHUC]`) ==[ **TAC_DONG_CHU_THE** ]==> (`e2` sở giao dịch `[CO_QUAN_THAM_QUYEN]`) *(Quan hệ lồng nhau)*
- (`e3` văn phòng đại diện `[TO_CHUC_DOANH_NGHIEP]`) ==[ **CHIU_CHE_TAI** ]==> (`e1` buộc chấm dứt hoạt động sở giao dịch `[BIEN_PHAP_KHAC_PHUC]`)
- (`e4` đơn vị sự nghiệp `[TO_CHUC_DOANH_NGHIEP]`) ==[ **CHIU_CHE_TAI** ]==> (`e1` buộc chấm dứt hoạt động sở giao dịch `[BIEN_PHAP_KHAC_PHUC]`)


---

### Mẫu #13_2008_QĐ-NHNN_32111#body_context_71 (Loại: `body_context`)
> **[Quyết định]`<LOAI_VAN_BAN>`** số **[13/2008/QĐ-NHNN]`<SO_HIEU>`** ban hành **[ngày 29 tháng 04 năm 2008]`<NGAY_BAN_HANH>`** bởi **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_BAN_HANH>`** . **[Điều 14]`<DIEU>`** . **[1 . **[Sở giao dịch]`<CO_QUAN_THAM_QUYEN>`** , chi nhánh , **[văn phòng đại diện]`<TO_CHUC_DOANH_NGHIEP>`** , **[đơn vị sự nghiệp]`<TO_CHUC_DOANH_NGHIEP>`** của **[ngân hàng thương mại]`<TO_CHUC_DOANH_NGHIEP>`** bị bắt **[buộc chấm dứt hoạt động]`<BIEN_PHAP_KHAC_PHUC>`** khi xảy ra một trong các trường hợp sau :]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Quyết định** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **13/2008/QĐ-NHNN** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_BAN_HANH` (span: `[11:14]`)
- `[e3]` **ngày 29 tháng 04 năm 2008** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 14** → `DIEU` (span: `[15:17]`)
- `[e5]` **1 . Sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp của ngân hàng thương mại bị bắt buộc chấm dứt hoạt động khi xảy ra một trong các trường hợp sau :** → `KHOAN` (span: `[18:47]`)
- `[e6]` **buộc chấm dứt hoạt động** → `BIEN_PHAP_KHAC_PHUC` (span: `[35:38]`) *(lồng trong `e5` (`KHOAN`))*
- `[e7]` **Sở giao dịch** → `CO_QUAN_THAM_QUYEN` (span: `[20:22]`) *(lồng trong `e5` (`KHOAN`))*
- `[e8]` **ngân hàng thương mại** → `TO_CHUC_DOANH_NGHIEP` (span: `[31:33]`) *(lồng trong `e5` (`KHOAN`))*
- `[e9]` **văn phòng đại diện** → `TO_CHUC_DOANH_NGHIEP` (span: `[25:27]`) *(lồng trong `e5` (`KHOAN`))*
- `[e10]` **đơn vị sự nghiệp** → `TO_CHUC_DOANH_NGHIEP` (span: `[28:30]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Ngân hàng Nhà nước Việt Nam `[CO_QUAN_BAN_HANH]`)
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Quyết định `[LOAI_VAN_BAN]`)
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 29 tháng 04 năm 2008 `[NGAY_BAN_HANH]`)
- (`e4` Điều 14 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`)
- (`e5` 1 . Sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp của ngân hàng thương mại bị bắt buộc chấm dứt hoạt động khi xảy ra một trong các trường hợp sau : `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 14 `[DIEU]`)
- (`e7` Sở giao dịch `[CO_QUAN_THAM_QUYEN]`) ==[ **CO_THAM_QUYEN** ]==> (`e6` buộc chấm dứt hoạt động `[BIEN_PHAP_KHAC_PHUC]`)
- (`e8` ngân hàng thương mại `[TO_CHUC_DOANH_NGHIEP]`) ==[ **CHIU_CHE_TAI** ]==> (`e6` buộc chấm dứt hoạt động `[BIEN_PHAP_KHAC_PHUC]`)
- (`e9` văn phòng đại diện `[TO_CHUC_DOANH_NGHIEP]`) ==[ **CHIU_CHE_TAI** ]==> (`e6` buộc chấm dứt hoạt động `[BIEN_PHAP_KHAC_PHUC]`)
- (`e10` đơn vị sự nghiệp `[TO_CHUC_DOANH_NGHIEP]`) ==[ **CHIU_CHE_TAI** ]==> (`e6` buộc chấm dứt hoạt động `[BIEN_PHAP_KHAC_PHUC]`)


---

### Mẫu #13_2008_QĐ-NHNN_32111#body_standalone_72 (Loại: `body_standalone`)
> **[Điều 14]`<DIEU>`** . **[1 . **[Sở giao dịch]`<CO_QUAN_THAM_QUYEN>`** , chi nhánh , **[văn phòng đại diện]`<TO_CHUC_DOANH_NGHIEP>`** , **[đơn vị sự nghiệp]`<TO_CHUC_DOANH_NGHIEP>`** của **[ngân hàng thương mại]`<TO_CHUC_DOANH_NGHIEP>`** bị bắt **[buộc chấm dứt hoạt động]`<BIEN_PHAP_KHAC_PHUC>`** khi xảy ra một trong các trường hợp sau :]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 14** → `DIEU` (span: `[0:2]`)
- `[e1]` **1 . Sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp của ngân hàng thương mại bị bắt buộc chấm dứt hoạt động khi xảy ra một trong các trường hợp sau :** → `KHOAN` (span: `[3:32]`)
- `[e2]` **buộc chấm dứt hoạt động** → `BIEN_PHAP_KHAC_PHUC` (span: `[20:23]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **Sở giao dịch** → `CO_QUAN_THAM_QUYEN` (span: `[5:7]`) *(lồng trong `e1` (`KHOAN`))*
- `[e4]` **ngân hàng thương mại** → `TO_CHUC_DOANH_NGHIEP` (span: `[16:18]`) *(lồng trong `e1` (`KHOAN`))*
- `[e5]` **văn phòng đại diện** → `TO_CHUC_DOANH_NGHIEP` (span: `[10:12]`) *(lồng trong `e1` (`KHOAN`))*
- `[e6]` **đơn vị sự nghiệp** → `TO_CHUC_DOANH_NGHIEP` (span: `[13:15]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 1 . Sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp của ngân hàng thương mại bị bắt buộc chấm dứt hoạt động khi xảy ra một trong các trường hợp sau : `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 14 `[DIEU]`)
- (`e3` Sở giao dịch `[CO_QUAN_THAM_QUYEN]`) ==[ **CO_THAM_QUYEN** ]==> (`e2` buộc chấm dứt hoạt động `[BIEN_PHAP_KHAC_PHUC]`)
- (`e4` ngân hàng thương mại `[TO_CHUC_DOANH_NGHIEP]`) ==[ **CHIU_CHE_TAI** ]==> (`e2` buộc chấm dứt hoạt động `[BIEN_PHAP_KHAC_PHUC]`)
- (`e5` văn phòng đại diện `[TO_CHUC_DOANH_NGHIEP]`) ==[ **CHIU_CHE_TAI** ]==> (`e2` buộc chấm dứt hoạt động `[BIEN_PHAP_KHAC_PHUC]`)
- (`e6` đơn vị sự nghiệp `[TO_CHUC_DOANH_NGHIEP]`) ==[ **CHIU_CHE_TAI** ]==> (`e2` buộc chấm dứt hoạt động `[BIEN_PHAP_KHAC_PHUC]`)


---

### Mẫu #13_2008_QĐ-NHNN_32111#body_context_73 (Loại: `body_context`)
> **[Quyết định]`<LOAI_VAN_BAN>`** số **[13/2008/QĐ-NHNN]`<SO_HIEU>`** ban hành **[ngày 29 tháng 04 năm 2008]`<NGAY_BAN_HANH>`** bởi **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_BAN_HANH>`** . **[Điều 14]`<DIEU>`** . **[2 . Căn cứ các trường hợp **[quy định tại]`<TU_KHOA_PHAP_LY>`** **[Khoản 1 Điều này]`<THAM_CHIEU_PHAP_LY>`** , **[Ngân hàng Nhà nước]`<CO_QUAN_THAM_QUYEN>`** có văn bản yêu cầu **[ngân hàng thương mại]`<TO_CHUC_DOANH_NGHIEP>`** chấm dứt hoạt động **[sở giao dịch]`<CO_QUAN_THAM_QUYEN>`** , chi nhánh , **[văn phòng đại diện]`<TO_CHUC_DOANH_NGHIEP>`** , **[đơn vị sự nghiệp]`<TO_CHUC_DOANH_NGHIEP>`** theo **[Phụ lục 08]`<THAM_CHIEU_PHAP_LY>`** kèm theo Quy định này .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Quyết định** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **13/2008/QĐ-NHNN** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_BAN_HANH` (span: `[11:14]`)
- `[e3]` **ngày 29 tháng 04 năm 2008** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 14** → `DIEU` (span: `[15:17]`)
- `[e5]` **2 . Căn cứ các trường hợp quy định tại Khoản 1 Điều này , Ngân hàng Nhà nước có văn bản yêu cầu ngân hàng thương mại chấm dứt hoạt động sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp theo Phụ lục 08 kèm theo Quy định này .** → `KHOAN` (span: `[18:57]`)
- `[e6]` **sở giao dịch** → `CO_QUAN_THAM_QUYEN` (span: `[39:41]`) *(lồng trong `e5` (`KHOAN`))*
- `[e7]` **ngân hàng thương mại** → `TO_CHUC_DOANH_NGHIEP` (span: `[35:37]`) *(lồng trong `e5` (`KHOAN`))*
- `[e8]` **văn phòng đại diện** → `TO_CHUC_DOANH_NGHIEP` (span: `[44:46]`) *(lồng trong `e5` (`KHOAN`))*
- `[e9]` **đơn vị sự nghiệp** → `TO_CHUC_DOANH_NGHIEP` (span: `[47:49]`) *(lồng trong `e5` (`KHOAN`))*
- `[e10]` **Khoản 1 Điều này** → `THAM_CHIEU_PHAP_LY` (span: `[25:29]`) *(lồng trong `e5` (`KHOAN`))*
- `[e11]` **Phụ lục 08** → `THAM_CHIEU_PHAP_LY` (span: `[50:52]`) *(lồng trong `e5` (`KHOAN`))*
- `[e12]` **quy định tại** → `TU_KHOA_PHAP_LY` (span: `[23:25]`) *(lồng trong `e5` (`KHOAN`))*
- `[e13]` **Ngân hàng Nhà nước** → `CO_QUAN_THAM_QUYEN` (span: `[30:32]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Ngân hàng Nhà nước Việt Nam `[CO_QUAN_BAN_HANH]`)
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Quyết định `[LOAI_VAN_BAN]`)
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 29 tháng 04 năm 2008 `[NGAY_BAN_HANH]`)
- (`e4` Điều 14 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`)
- (`e5` 2 . Căn cứ các trường hợp quy định tại Khoản 1 Điều này , Ngân hàng Nhà nước có văn bản yêu cầu ngân hàng thương mại chấm dứt hoạt động sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp theo Phụ lục 08 kèm theo Quy định này . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 14 `[DIEU]`)
- (`e12` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e10` Khoản 1 Điều này `[THAM_CHIEU_PHAP_LY]`)
- (`e5` 2 . Căn cứ các trường hợp quy định tại Khoản 1 Điều này , Ngân hàng Nhà nước có văn bản yêu cầu ngân hàng thương mại chấm dứt hoạt động sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp theo Phụ lục 08 kèm theo Quy định này . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e10` Khoản 1 Điều này `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e12` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e11` Phụ lục 08 `[THAM_CHIEU_PHAP_LY]`)
- (`e5` 2 . Căn cứ các trường hợp quy định tại Khoản 1 Điều này , Ngân hàng Nhà nước có văn bản yêu cầu ngân hàng thương mại chấm dứt hoạt động sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp theo Phụ lục 08 kèm theo Quy định này . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e11` Phụ lục 08 `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #13_2008_QĐ-NHNN_32111#body_standalone_74 (Loại: `body_standalone`)
> **[Điều 14]`<DIEU>`** . **[2 . Căn cứ các trường hợp **[quy định tại]`<TU_KHOA_PHAP_LY>`** **[Khoản 1 Điều này]`<THAM_CHIEU_PHAP_LY>`** , **[Ngân hàng Nhà nước]`<CO_QUAN_THAM_QUYEN>`** có văn bản yêu cầu **[ngân hàng thương mại]`<TO_CHUC_DOANH_NGHIEP>`** chấm dứt hoạt động **[sở giao dịch]`<CO_QUAN_THAM_QUYEN>`** , chi nhánh , **[văn phòng đại diện]`<TO_CHUC_DOANH_NGHIEP>`** , **[đơn vị sự nghiệp]`<TO_CHUC_DOANH_NGHIEP>`** theo **[Phụ lục 08]`<THAM_CHIEU_PHAP_LY>`** kèm theo Quy định này .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 14** → `DIEU` (span: `[0:2]`)
- `[e1]` **2 . Căn cứ các trường hợp quy định tại Khoản 1 Điều này , Ngân hàng Nhà nước có văn bản yêu cầu ngân hàng thương mại chấm dứt hoạt động sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp theo Phụ lục 08 kèm theo Quy định này .** → `KHOAN` (span: `[3:42]`)
- `[e2]` **sở giao dịch** → `CO_QUAN_THAM_QUYEN` (span: `[24:26]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **ngân hàng thương mại** → `TO_CHUC_DOANH_NGHIEP` (span: `[20:22]`) *(lồng trong `e1` (`KHOAN`))*
- `[e4]` **văn phòng đại diện** → `TO_CHUC_DOANH_NGHIEP` (span: `[29:31]`) *(lồng trong `e1` (`KHOAN`))*
- `[e5]` **đơn vị sự nghiệp** → `TO_CHUC_DOANH_NGHIEP` (span: `[32:34]`) *(lồng trong `e1` (`KHOAN`))*
- `[e6]` **Khoản 1 Điều này** → `THAM_CHIEU_PHAP_LY` (span: `[10:14]`) *(lồng trong `e1` (`KHOAN`))*
- `[e7]` **Phụ lục 08** → `THAM_CHIEU_PHAP_LY` (span: `[35:37]`) *(lồng trong `e1` (`KHOAN`))*
- `[e8]` **quy định tại** → `TU_KHOA_PHAP_LY` (span: `[8:10]`) *(lồng trong `e1` (`KHOAN`))*
- `[e9]` **Ngân hàng Nhà nước** → `CO_QUAN_THAM_QUYEN` (span: `[15:17]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 2 . Căn cứ các trường hợp quy định tại Khoản 1 Điều này , Ngân hàng Nhà nước có văn bản yêu cầu ngân hàng thương mại chấm dứt hoạt động sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp theo Phụ lục 08 kèm theo Quy định này . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 14 `[DIEU]`)
- (`e8` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e6` Khoản 1 Điều này `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 2 . Căn cứ các trường hợp quy định tại Khoản 1 Điều này , Ngân hàng Nhà nước có văn bản yêu cầu ngân hàng thương mại chấm dứt hoạt động sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp theo Phụ lục 08 kèm theo Quy định này . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e6` Khoản 1 Điều này `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e8` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e7` Phụ lục 08 `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 2 . Căn cứ các trường hợp quy định tại Khoản 1 Điều này , Ngân hàng Nhà nước có văn bản yêu cầu ngân hàng thương mại chấm dứt hoạt động sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp theo Phụ lục 08 kèm theo Quy định này . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e7` Phụ lục 08 `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #13_2008_QĐ-NHNN_32111#body_context_75 (Loại: `body_context`)
> **[Quyết định]`<LOAI_VAN_BAN>`** số **[13/2008/QĐ-NHNN]`<SO_HIEU>`** của **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Ngân hàng]`<LINH_VUC>`** . **[Điều 14]`<DIEU>`** . **[3 . Trường hợp **[ngân hàng thương mại]`<TO_CHUC_DOANH_NGHIEP>`** khiếu nại văn bản của **[Ngân hàng Nhà nước]`<CO_QUAN_THAM_QUYEN>`** **[nêu tại]`<TU_KHOA_PHAP_LY>`** **[Khoản 2 Điều này]`<THAM_CHIEU_PHAP_LY>`** , trong vòng năm ngày làm việc kể từ ngày nhận được văn bản yêu cầu của **[Ngân hàng Nhà nước]`<CO_QUAN_THAM_QUYEN>`** , Chủ tịch **[Hội đồng quản trị]`<TO_CHUC_DOANH_NGHIEP>`** **[ngân hàng thương mại]`<TO_CHUC_DOANH_NGHIEP>`** có văn bản gửi **[Ngân hàng Nhà nước]`<CO_QUAN_THAM_QUYEN>`** để giải quyết theo quy định của pháp luật .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Quyết định** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **13/2008/QĐ-NHNN** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_BAN_HANH` (span: `[4:7]`)
- `[e3]` **Ngân hàng** → `LINH_VUC` (span: `[9:10]`)
- `[e4]` **Điều 14** → `DIEU` (span: `[11:13]`)
- `[e5]` **3 . Trường hợp ngân hàng thương mại khiếu nại văn bản của Ngân hàng Nhà nước nêu tại Khoản 2 Điều này , trong vòng năm ngày làm việc kể từ ngày nhận được văn bản yêu cầu của Ngân hàng Nhà nước , Chủ tịch Hội đồng quản trị ngân hàng thương mại có văn bản gửi Ngân hàng Nhà nước để giải quyết theo quy định của pháp luật .** → `KHOAN` (span: `[14:64]`)
- `[e6]` **ngân hàng thương mại** → `TO_CHUC_DOANH_NGHIEP` (span: `[17:19]`) *(lồng trong `e5` (`KHOAN`))*
- `[e7]` **ngân hàng thương mại** → `TO_CHUC_DOANH_NGHIEP` (span: `[50:52]`) *(lồng trong `e5` (`KHOAN`))*
- `[e8]` **Khoản 2 Điều này** → `THAM_CHIEU_PHAP_LY` (span: `[26:30]`) *(lồng trong `e5` (`KHOAN`))*
- `[e9]` **nêu tại** → `TU_KHOA_PHAP_LY` (span: `[24:26]`) *(lồng trong `e5` (`KHOAN`))*
- `[e10]` **Ngân hàng Nhà nước** → `CO_QUAN_THAM_QUYEN` (span: `[22:24]`) *(lồng trong `e5` (`KHOAN`))*
- `[e11]` **Ngân hàng Nhà nước** → `CO_QUAN_THAM_QUYEN` (span: `[44:46]`) *(lồng trong `e5` (`KHOAN`))*
- `[e12]` **Ngân hàng Nhà nước** → `CO_QUAN_THAM_QUYEN` (span: `[55:57]`) *(lồng trong `e5` (`KHOAN`))*
- `[e13]` **Hội đồng quản trị** → `TO_CHUC_DOANH_NGHIEP` (span: `[48:50]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Ngân hàng Nhà nước Việt Nam `[CO_QUAN_BAN_HANH]`)
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Quyết định `[LOAI_VAN_BAN]`)
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Ngân hàng `[LINH_VUC]`)
- (`e4` Điều 14 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`)
- (`e5` 3 . Trường hợp ngân hàng thương mại khiếu nại văn bản của Ngân hàng Nhà nước nêu tại Khoản 2 Điều này , trong vòng năm ngày làm việc kể từ ngày nhận được văn bản yêu cầu của Ngân hàng Nhà nước , Chủ tịch Hội đồng quản trị ngân hàng thương mại có văn bản gửi Ngân hàng Nhà nước để giải quyết theo quy định của pháp luật . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 14 `[DIEU]`)
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Ngân hàng `[LINH_VUC]`)
- (`e5` 3 . Trường hợp ngân hàng thương mại khiếu nại văn bản của Ngân hàng Nhà nước nêu tại Khoản 2 Điều này , trong vòng năm ngày làm việc kể từ ngày nhận được văn bản yêu cầu của Ngân hàng Nhà nước , Chủ tịch Hội đồng quản trị ngân hàng thương mại có văn bản gửi Ngân hàng Nhà nước để giải quyết theo quy định của pháp luật . `[KHOAN]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Ngân hàng `[LINH_VUC]`)
- (`e9` nêu tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e8` Khoản 2 Điều này `[THAM_CHIEU_PHAP_LY]`)
- (`e5` 3 . Trường hợp ngân hàng thương mại khiếu nại văn bản của Ngân hàng Nhà nước nêu tại Khoản 2 Điều này , trong vòng năm ngày làm việc kể từ ngày nhận được văn bản yêu cầu của Ngân hàng Nhà nước , Chủ tịch Hội đồng quản trị ngân hàng thương mại có văn bản gửi Ngân hàng Nhà nước để giải quyết theo quy định của pháp luật . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e8` Khoản 2 Điều này `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #13_2008_QĐ-NHNN_32111#body_standalone_76 (Loại: `body_standalone`)
> **[Điều 14]`<DIEU>`** . **[3 . Trường hợp **[ngân hàng thương mại]`<TO_CHUC_DOANH_NGHIEP>`** khiếu nại văn bản của **[Ngân hàng Nhà nước]`<CO_QUAN_THAM_QUYEN>`** **[nêu tại]`<TU_KHOA_PHAP_LY>`** **[Khoản 2 Điều này]`<THAM_CHIEU_PHAP_LY>`** , trong vòng năm ngày làm việc kể từ ngày nhận được văn bản yêu cầu của **[Ngân hàng Nhà nước]`<CO_QUAN_THAM_QUYEN>`** , Chủ tịch **[Hội đồng quản trị]`<TO_CHUC_DOANH_NGHIEP>`** **[ngân hàng thương mại]`<TO_CHUC_DOANH_NGHIEP>`** có văn bản gửi **[Ngân hàng Nhà nước]`<CO_QUAN_THAM_QUYEN>`** để giải quyết theo quy định của pháp luật .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 14** → `DIEU` (span: `[0:2]`)
- `[e1]` **3 . Trường hợp ngân hàng thương mại khiếu nại văn bản của Ngân hàng Nhà nước nêu tại Khoản 2 Điều này , trong vòng năm ngày làm việc kể từ ngày nhận được văn bản yêu cầu của Ngân hàng Nhà nước , Chủ tịch Hội đồng quản trị ngân hàng thương mại có văn bản gửi Ngân hàng Nhà nước để giải quyết theo quy định của pháp luật .** → `KHOAN` (span: `[3:53]`)
- `[e2]` **ngân hàng thương mại** → `TO_CHUC_DOANH_NGHIEP` (span: `[6:8]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **ngân hàng thương mại** → `TO_CHUC_DOANH_NGHIEP` (span: `[39:41]`) *(lồng trong `e1` (`KHOAN`))*
- `[e4]` **Khoản 2 Điều này** → `THAM_CHIEU_PHAP_LY` (span: `[15:19]`) *(lồng trong `e1` (`KHOAN`))*
- `[e5]` **nêu tại** → `TU_KHOA_PHAP_LY` (span: `[13:15]`) *(lồng trong `e1` (`KHOAN`))*
- `[e6]` **Ngân hàng Nhà nước** → `CO_QUAN_THAM_QUYEN` (span: `[11:13]`) *(lồng trong `e1` (`KHOAN`))*
- `[e7]` **Ngân hàng Nhà nước** → `CO_QUAN_THAM_QUYEN` (span: `[33:35]`) *(lồng trong `e1` (`KHOAN`))*
- `[e8]` **Ngân hàng Nhà nước** → `CO_QUAN_THAM_QUYEN` (span: `[44:46]`) *(lồng trong `e1` (`KHOAN`))*
- `[e9]` **Hội đồng quản trị** → `TO_CHUC_DOANH_NGHIEP` (span: `[37:39]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 3 . Trường hợp ngân hàng thương mại khiếu nại văn bản của Ngân hàng Nhà nước nêu tại Khoản 2 Điều này , trong vòng năm ngày làm việc kể từ ngày nhận được văn bản yêu cầu của Ngân hàng Nhà nước , Chủ tịch Hội đồng quản trị ngân hàng thương mại có văn bản gửi Ngân hàng Nhà nước để giải quyết theo quy định của pháp luật . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 14 `[DIEU]`)
- (`e5` nêu tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e4` Khoản 2 Điều này `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 3 . Trường hợp ngân hàng thương mại khiếu nại văn bản của Ngân hàng Nhà nước nêu tại Khoản 2 Điều này , trong vòng năm ngày làm việc kể từ ngày nhận được văn bản yêu cầu của Ngân hàng Nhà nước , Chủ tịch Hội đồng quản trị ngân hàng thương mại có văn bản gửi Ngân hàng Nhà nước để giải quyết theo quy định của pháp luật . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e4` Khoản 2 Điều này `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #13_2008_QĐ-NHNN_32111#body_context_77 (Loại: `body_context`)
> **[Quyết định]`<LOAI_VAN_BAN>`** số **[13/2008/QĐ-NHNN]`<SO_HIEU>`** của **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Ngân hàng]`<LINH_VUC>`** . **[Điều 14]`<DIEU>`** . **[Khoản 4]`<KHOAN>`** . **[a ) Trình **[Ngân hàng Nhà nước]`<CO_QUAN_THAM_QUYEN>`** phương án giải quyết các quyền lợi và nghĩa vụ đối với **[khách hàng]`<CHU_THE_CA_NHAN>`** của **[sở giao dịch]`<CO_QUAN_THAM_QUYEN>`** , chi nhánh , **[văn phòng đại diện]`<TO_CHUC_DOANH_NGHIEP>`** , **[đơn vị sự nghiệp]`<TO_CHUC_DOANH_NGHIEP>`** ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Quyết định** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **13/2008/QĐ-NHNN** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_BAN_HANH` (span: `[4:7]`)
- `[e3]` **Ngân hàng** → `LINH_VUC` (span: `[9:10]`)
- `[e4]` **Điều 14** → `DIEU` (span: `[11:13]`)
- `[e5]` **Khoản 4** → `KHOAN` (span: `[14:16]`)
- `[e6]` **a ) Trình Ngân hàng Nhà nước phương án giải quyết các quyền lợi và nghĩa vụ đối với khách hàng của sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp ;** → `DIEM` (span: `[17:42]`)
- `[e7]` **sở giao dịch** → `CO_QUAN_THAM_QUYEN` (span: `[31:33]`) *(lồng trong `e6` (`DIEM`))*
- `[e8]` **văn phòng đại diện** → `TO_CHUC_DOANH_NGHIEP` (span: `[36:38]`) *(lồng trong `e6` (`DIEM`))*
- `[e9]` **đơn vị sự nghiệp** → `TO_CHUC_DOANH_NGHIEP` (span: `[39:41]`) *(lồng trong `e6` (`DIEM`))*
- `[e10]` **Ngân hàng Nhà nước** → `CO_QUAN_THAM_QUYEN` (span: `[20:22]`) *(lồng trong `e6` (`DIEM`))*
- `[e11]` **khách hàng** → `CHU_THE_CA_NHAN` (span: `[29:30]`) *(lồng trong `e6` (`DIEM`))*

**Quan hệ:**
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Ngân hàng Nhà nước Việt Nam `[CO_QUAN_BAN_HANH]`)
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Quyết định `[LOAI_VAN_BAN]`)
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Ngân hàng `[LINH_VUC]`)
- (`e4` Điều 14 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`)
- (`e5` Khoản 4 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 14 `[DIEU]`)
- (`e6` a ) Trình Ngân hàng Nhà nước phương án giải quyết các quyền lợi và nghĩa vụ đối với khách hàng của sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e5` Khoản 4 `[KHOAN]`)
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Ngân hàng `[LINH_VUC]`)
- (`e6` a ) Trình Ngân hàng Nhà nước phương án giải quyết các quyền lợi và nghĩa vụ đối với khách hàng của sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp ; `[DIEM]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Ngân hàng `[LINH_VUC]`)


---

### Mẫu #13_2008_QĐ-NHNN_32111#body_standalone_78 (Loại: `body_standalone`)
> **[Điều 14]`<DIEU>`** . **[Khoản 4]`<KHOAN>`** . **[a ) Trình **[Ngân hàng Nhà nước]`<CO_QUAN_THAM_QUYEN>`** phương án giải quyết các quyền lợi và nghĩa vụ đối với **[khách hàng]`<CHU_THE_CA_NHAN>`** của **[sở giao dịch]`<CO_QUAN_THAM_QUYEN>`** , chi nhánh , **[văn phòng đại diện]`<TO_CHUC_DOANH_NGHIEP>`** , **[đơn vị sự nghiệp]`<TO_CHUC_DOANH_NGHIEP>`** ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Điều 14** → `DIEU` (span: `[0:2]`)
- `[e1]` **Khoản 4** → `KHOAN` (span: `[3:5]`)
- `[e2]` **a ) Trình Ngân hàng Nhà nước phương án giải quyết các quyền lợi và nghĩa vụ đối với khách hàng của sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp ;** → `DIEM` (span: `[6:31]`)
- `[e3]` **sở giao dịch** → `CO_QUAN_THAM_QUYEN` (span: `[20:22]`) *(lồng trong `e2` (`DIEM`))*
- `[e4]` **văn phòng đại diện** → `TO_CHUC_DOANH_NGHIEP` (span: `[25:27]`) *(lồng trong `e2` (`DIEM`))*
- `[e5]` **đơn vị sự nghiệp** → `TO_CHUC_DOANH_NGHIEP` (span: `[28:30]`) *(lồng trong `e2` (`DIEM`))*
- `[e6]` **Ngân hàng Nhà nước** → `CO_QUAN_THAM_QUYEN` (span: `[9:11]`) *(lồng trong `e2` (`DIEM`))*
- `[e7]` **khách hàng** → `CHU_THE_CA_NHAN` (span: `[18:19]`) *(lồng trong `e2` (`DIEM`))*

**Quan hệ:**
- (`e1` Khoản 4 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 14 `[DIEU]`)
- (`e2` a ) Trình Ngân hàng Nhà nước phương án giải quyết các quyền lợi và nghĩa vụ đối với khách hàng của sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e1` Khoản 4 `[KHOAN]`)


---

### Mẫu #13_2008_QĐ-NHNN_32111#body_context_79 (Loại: `body_context`)
> **[Quyết định]`<LOAI_VAN_BAN>`** số **[13/2008/QĐ-NHNN]`<SO_HIEU>`** của **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Ngân hàng]`<LINH_VUC>`** . **[Điều 16]`<DIEU>`** . **[Khoản 1 . Quyết định chấm dứt hoạt động **[sở giao dịch]`<CO_QUAN_THAM_QUYEN>`** , chi nhánh , **[văn phòng đại diện]`<TO_CHUC_DOANH_NGHIEP>`** , **[đơn vị sự nghiệp]`<TO_CHUC_DOANH_NGHIEP>`** của **[ngân hàng thương mại]`<TO_CHUC_DOANH_NGHIEP>`** phải được]`<KHOAN>`** : **[a ) Gửi **[Ngân hàng Nhà nước]`<CO_QUAN_THAM_QUYEN>`** ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Quyết định** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **13/2008/QĐ-NHNN** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_BAN_HANH` (span: `[4:7]`)
- `[e3]` **Ngân hàng** → `LINH_VUC` (span: `[9:10]`)
- `[e4]` **Điều 16** → `DIEU` (span: `[11:13]`)
- `[e5]` **Khoản 1 . Quyết định chấm dứt hoạt động sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp của ngân hàng thương mại phải được** → `KHOAN` (span: `[14:35]`)
- `[e6]` **a ) Gửi Ngân hàng Nhà nước ;** → `DIEM` (span: `[36:42]`)
- `[e7]` **sở giao dịch** → `CO_QUAN_THAM_QUYEN` (span: `[20:22]`) *(lồng trong `e5` (`KHOAN`))*
- `[e8]` **ngân hàng thương mại** → `TO_CHUC_DOANH_NGHIEP` (span: `[31:33]`) *(lồng trong `e5` (`KHOAN`))*
- `[e9]` **văn phòng đại diện** → `TO_CHUC_DOANH_NGHIEP` (span: `[25:27]`) *(lồng trong `e5` (`KHOAN`))*
- `[e10]` **đơn vị sự nghiệp** → `TO_CHUC_DOANH_NGHIEP` (span: `[28:30]`) *(lồng trong `e5` (`KHOAN`))*
- `[e11]` **Ngân hàng Nhà nước** → `CO_QUAN_THAM_QUYEN` (span: `[39:41]`) *(lồng trong `e6` (`DIEM`))*

**Quan hệ:**
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Ngân hàng Nhà nước Việt Nam `[CO_QUAN_BAN_HANH]`)
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Quyết định `[LOAI_VAN_BAN]`)
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Ngân hàng `[LINH_VUC]`)
- (`e4` Điều 16 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`)
- (`e5` Khoản 1 . Quyết định chấm dứt hoạt động sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp của ngân hàng thương mại phải được `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 16 `[DIEU]`)
- (`e6` a ) Gửi Ngân hàng Nhà nước ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e5` Khoản 1 . Quyết định chấm dứt hoạt động sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp của ngân hàng thương mại phải được `[KHOAN]`)
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Ngân hàng `[LINH_VUC]`)
- (`e6` a ) Gửi Ngân hàng Nhà nước ; `[DIEM]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Ngân hàng `[LINH_VUC]`)


---

### Mẫu #13_2008_QĐ-NHNN_32111#body_standalone_80 (Loại: `body_standalone`)
> **[Điều 16]`<DIEU>`** . **[Khoản 1 . Quyết định chấm dứt hoạt động **[sở giao dịch]`<CO_QUAN_THAM_QUYEN>`** , chi nhánh , **[văn phòng đại diện]`<TO_CHUC_DOANH_NGHIEP>`** , **[đơn vị sự nghiệp]`<TO_CHUC_DOANH_NGHIEP>`** của **[ngân hàng thương mại]`<TO_CHUC_DOANH_NGHIEP>`** phải được]`<KHOAN>`** : **[a ) Gửi **[Ngân hàng Nhà nước]`<CO_QUAN_THAM_QUYEN>`** ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Điều 16** → `DIEU` (span: `[0:2]`)
- `[e1]` **Khoản 1 . Quyết định chấm dứt hoạt động sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp của ngân hàng thương mại phải được** → `KHOAN` (span: `[3:24]`)
- `[e2]` **a ) Gửi Ngân hàng Nhà nước ;** → `DIEM` (span: `[25:31]`)
- `[e3]` **sở giao dịch** → `CO_QUAN_THAM_QUYEN` (span: `[9:11]`) *(lồng trong `e1` (`KHOAN`))*
- `[e4]` **ngân hàng thương mại** → `TO_CHUC_DOANH_NGHIEP` (span: `[20:22]`) *(lồng trong `e1` (`KHOAN`))*
- `[e5]` **văn phòng đại diện** → `TO_CHUC_DOANH_NGHIEP` (span: `[14:16]`) *(lồng trong `e1` (`KHOAN`))*
- `[e6]` **đơn vị sự nghiệp** → `TO_CHUC_DOANH_NGHIEP` (span: `[17:19]`) *(lồng trong `e1` (`KHOAN`))*
- `[e7]` **Ngân hàng Nhà nước** → `CO_QUAN_THAM_QUYEN` (span: `[28:30]`) *(lồng trong `e2` (`DIEM`))*

**Quan hệ:**
- (`e1` Khoản 1 . Quyết định chấm dứt hoạt động sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp của ngân hàng thương mại phải được `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 16 `[DIEU]`)
- (`e2` a ) Gửi Ngân hàng Nhà nước ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e1` Khoản 1 . Quyết định chấm dứt hoạt động sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp của ngân hàng thương mại phải được `[KHOAN]`)


---

### Mẫu #13_2008_QĐ-NHNN_32111#body_context_81 (Loại: `body_context`)
> **[Quyết định]`<LOAI_VAN_BAN>`** số **[13/2008/QĐ-NHNN]`<SO_HIEU>`** ban hành **[ngày 29 tháng 04 năm 2008]`<NGAY_BAN_HANH>`** bởi **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_BAN_HANH>`** . **[Điều 16]`<DIEU>`** . **[Khoản 1 . Quyết định chấm dứt hoạt động **[sở giao dịch]`<CO_QUAN_THAM_QUYEN>`** , chi nhánh , **[văn phòng đại diện]`<TO_CHUC_DOANH_NGHIEP>`** , **[đơn vị sự nghiệp]`<TO_CHUC_DOANH_NGHIEP>`** của **[ngân hàng thương mại]`<TO_CHUC_DOANH_NGHIEP>`** phải được]`<KHOAN>`** : **[b ) Gửi **[Ngân hàng Nhà nước chi nhánh tỉnh , thành phố]`<CO_QUAN_THAM_QUYEN>`** nơi **[sở giao dịch]`<CO_QUAN_THAM_QUYEN>`** , chi nhánh , **[văn phòng đại diện]`<TO_CHUC_DOANH_NGHIEP>`** , **[đơn vị sự nghiệp]`<TO_CHUC_DOANH_NGHIEP>`** chấm dứt hoạt động ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Quyết định** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **13/2008/QĐ-NHNN** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_BAN_HANH` (span: `[11:14]`)
- `[e3]` **ngày 29 tháng 04 năm 2008** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 16** → `DIEU` (span: `[15:17]`)
- `[e5]` **Khoản 1 . Quyết định chấm dứt hoạt động sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp của ngân hàng thương mại phải được** → `KHOAN` (span: `[18:39]`)
- `[e6]` **b ) Gửi Ngân hàng Nhà nước chi nhánh tỉnh , thành phố nơi sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp chấm dứt hoạt động ;** → `DIEM` (span: `[40:63]`)
- `[e7]` **sở giao dịch** → `CO_QUAN_THAM_QUYEN` (span: `[24:26]`) *(lồng trong `e5` (`KHOAN`))*
- `[e8]` **sở giao dịch** → `CO_QUAN_THAM_QUYEN` (span: `[50:52]`) *(lồng trong `e6` (`DIEM`))*
- `[e9]` **ngân hàng thương mại** → `TO_CHUC_DOANH_NGHIEP` (span: `[35:37]`) *(lồng trong `e5` (`KHOAN`))*
- `[e10]` **văn phòng đại diện** → `TO_CHUC_DOANH_NGHIEP` (span: `[29:31]`) *(lồng trong `e5` (`KHOAN`))*
- `[e11]` **văn phòng đại diện** → `TO_CHUC_DOANH_NGHIEP` (span: `[55:57]`) *(lồng trong `e6` (`DIEM`))*
- `[e12]` **đơn vị sự nghiệp** → `TO_CHUC_DOANH_NGHIEP` (span: `[32:34]`) *(lồng trong `e5` (`KHOAN`))*
- `[e13]` **đơn vị sự nghiệp** → `TO_CHUC_DOANH_NGHIEP` (span: `[58:60]`) *(lồng trong `e6` (`DIEM`))*
- `[e14]` **Ngân hàng Nhà nước chi nhánh tỉnh , thành phố** → `CO_QUAN_THAM_QUYEN` (span: `[43:49]`) *(lồng trong `e6` (`DIEM`))*

**Quan hệ:**
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Ngân hàng Nhà nước Việt Nam `[CO_QUAN_BAN_HANH]`)
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Quyết định `[LOAI_VAN_BAN]`)
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 29 tháng 04 năm 2008 `[NGAY_BAN_HANH]`)
- (`e4` Điều 16 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`)
- (`e5` Khoản 1 . Quyết định chấm dứt hoạt động sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp của ngân hàng thương mại phải được `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 16 `[DIEU]`)
- (`e6` b ) Gửi Ngân hàng Nhà nước chi nhánh tỉnh , thành phố nơi sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp chấm dứt hoạt động ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e5` Khoản 1 . Quyết định chấm dứt hoạt động sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp của ngân hàng thương mại phải được `[KHOAN]`)


---

### Mẫu #13_2008_QĐ-NHNN_32111#body_standalone_82 (Loại: `body_standalone`)
> **[Điều 16]`<DIEU>`** . **[Khoản 1 . Quyết định chấm dứt hoạt động **[sở giao dịch]`<CO_QUAN_THAM_QUYEN>`** , chi nhánh , **[văn phòng đại diện]`<TO_CHUC_DOANH_NGHIEP>`** , **[đơn vị sự nghiệp]`<TO_CHUC_DOANH_NGHIEP>`** của **[ngân hàng thương mại]`<TO_CHUC_DOANH_NGHIEP>`** phải được]`<KHOAN>`** : **[b ) Gửi **[Ngân hàng Nhà nước chi nhánh tỉnh , thành phố]`<CO_QUAN_THAM_QUYEN>`** nơi **[sở giao dịch]`<CO_QUAN_THAM_QUYEN>`** , chi nhánh , **[văn phòng đại diện]`<TO_CHUC_DOANH_NGHIEP>`** , **[đơn vị sự nghiệp]`<TO_CHUC_DOANH_NGHIEP>`** chấm dứt hoạt động ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Điều 16** → `DIEU` (span: `[0:2]`)
- `[e1]` **Khoản 1 . Quyết định chấm dứt hoạt động sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp của ngân hàng thương mại phải được** → `KHOAN` (span: `[3:24]`)
- `[e2]` **b ) Gửi Ngân hàng Nhà nước chi nhánh tỉnh , thành phố nơi sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp chấm dứt hoạt động ;** → `DIEM` (span: `[25:48]`)
- `[e3]` **sở giao dịch** → `CO_QUAN_THAM_QUYEN` (span: `[9:11]`) *(lồng trong `e1` (`KHOAN`))*
- `[e4]` **sở giao dịch** → `CO_QUAN_THAM_QUYEN` (span: `[35:37]`) *(lồng trong `e2` (`DIEM`))*
- `[e5]` **ngân hàng thương mại** → `TO_CHUC_DOANH_NGHIEP` (span: `[20:22]`) *(lồng trong `e1` (`KHOAN`))*
- `[e6]` **văn phòng đại diện** → `TO_CHUC_DOANH_NGHIEP` (span: `[14:16]`) *(lồng trong `e1` (`KHOAN`))*
- `[e7]` **văn phòng đại diện** → `TO_CHUC_DOANH_NGHIEP` (span: `[40:42]`) *(lồng trong `e2` (`DIEM`))*
- `[e8]` **đơn vị sự nghiệp** → `TO_CHUC_DOANH_NGHIEP` (span: `[17:19]`) *(lồng trong `e1` (`KHOAN`))*
- `[e9]` **đơn vị sự nghiệp** → `TO_CHUC_DOANH_NGHIEP` (span: `[43:45]`) *(lồng trong `e2` (`DIEM`))*
- `[e10]` **Ngân hàng Nhà nước chi nhánh tỉnh , thành phố** → `CO_QUAN_THAM_QUYEN` (span: `[28:34]`) *(lồng trong `e2` (`DIEM`))*

**Quan hệ:**
- (`e1` Khoản 1 . Quyết định chấm dứt hoạt động sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp của ngân hàng thương mại phải được `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 16 `[DIEU]`)
- (`e2` b ) Gửi Ngân hàng Nhà nước chi nhánh tỉnh , thành phố nơi sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp chấm dứt hoạt động ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e1` Khoản 1 . Quyết định chấm dứt hoạt động sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp của ngân hàng thương mại phải được `[KHOAN]`)


---

### Mẫu #13_2008_QĐ-NHNN_32111#body_context_83 (Loại: `body_context`)
> **[Quyết định]`<LOAI_VAN_BAN>`** số **[13/2008/QĐ-NHNN]`<SO_HIEU>`** của **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Ngân hàng]`<LINH_VUC>`** . **[Điều 16]`<DIEU>`** . **[Khoản 1 . Quyết định chấm dứt hoạt động **[sở giao dịch]`<CO_QUAN_THAM_QUYEN>`** , chi nhánh , **[văn phòng đại diện]`<TO_CHUC_DOANH_NGHIEP>`** , **[đơn vị sự nghiệp]`<TO_CHUC_DOANH_NGHIEP>`** của **[ngân hàng thương mại]`<TO_CHUC_DOANH_NGHIEP>`** phải được]`<KHOAN>`** : **[c ) Niêm yết công khai tại địa điểm của **[sở giao dịch]`<CO_QUAN_THAM_QUYEN>`** , chi nhánh , **[văn phòng đại diện]`<TO_CHUC_DOANH_NGHIEP>`** , **[đơn vị sự nghiệp]`<TO_CHUC_DOANH_NGHIEP>`** chấm dứt hoạt động .]`<DIEM>`**

**Thực thể:**
- `[e0]` **Quyết định** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **13/2008/QĐ-NHNN** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_BAN_HANH` (span: `[4:7]`)
- `[e3]` **Ngân hàng** → `LINH_VUC` (span: `[9:10]`)
- `[e4]` **Điều 16** → `DIEU` (span: `[11:13]`)
- `[e5]` **Khoản 1 . Quyết định chấm dứt hoạt động sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp của ngân hàng thương mại phải được** → `KHOAN` (span: `[14:35]`)
- `[e6]` **c ) Niêm yết công khai tại địa điểm của sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp chấm dứt hoạt động .** → `DIEM` (span: `[36:56]`)
- `[e7]` **sở giao dịch** → `CO_QUAN_THAM_QUYEN` (span: `[20:22]`) *(lồng trong `e5` (`KHOAN`))*
- `[e8]` **sở giao dịch** → `CO_QUAN_THAM_QUYEN` (span: `[43:45]`) *(lồng trong `e6` (`DIEM`))*
- `[e9]` **ngân hàng thương mại** → `TO_CHUC_DOANH_NGHIEP` (span: `[31:33]`) *(lồng trong `e5` (`KHOAN`))*
- `[e10]` **văn phòng đại diện** → `TO_CHUC_DOANH_NGHIEP` (span: `[25:27]`) *(lồng trong `e5` (`KHOAN`))*
- `[e11]` **văn phòng đại diện** → `TO_CHUC_DOANH_NGHIEP` (span: `[48:50]`) *(lồng trong `e6` (`DIEM`))*
- `[e12]` **đơn vị sự nghiệp** → `TO_CHUC_DOANH_NGHIEP` (span: `[28:30]`) *(lồng trong `e5` (`KHOAN`))*
- `[e13]` **đơn vị sự nghiệp** → `TO_CHUC_DOANH_NGHIEP` (span: `[51:53]`) *(lồng trong `e6` (`DIEM`))*

**Quan hệ:**
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Ngân hàng Nhà nước Việt Nam `[CO_QUAN_BAN_HANH]`)
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Quyết định `[LOAI_VAN_BAN]`)
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Ngân hàng `[LINH_VUC]`)
- (`e4` Điều 16 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`)
- (`e5` Khoản 1 . Quyết định chấm dứt hoạt động sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp của ngân hàng thương mại phải được `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 16 `[DIEU]`)
- (`e6` c ) Niêm yết công khai tại địa điểm của sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp chấm dứt hoạt động . `[DIEM]`) ==[ **THUOC_VE** ]==> (`e5` Khoản 1 . Quyết định chấm dứt hoạt động sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp của ngân hàng thương mại phải được `[KHOAN]`)
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Ngân hàng `[LINH_VUC]`)
- (`e6` c ) Niêm yết công khai tại địa điểm của sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp chấm dứt hoạt động . `[DIEM]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Ngân hàng `[LINH_VUC]`)


---

### Mẫu #13_2008_QĐ-NHNN_32111#body_standalone_84 (Loại: `body_standalone`)
> **[Điều 16]`<DIEU>`** . **[Khoản 1 . Quyết định chấm dứt hoạt động **[sở giao dịch]`<CO_QUAN_THAM_QUYEN>`** , chi nhánh , **[văn phòng đại diện]`<TO_CHUC_DOANH_NGHIEP>`** , **[đơn vị sự nghiệp]`<TO_CHUC_DOANH_NGHIEP>`** của **[ngân hàng thương mại]`<TO_CHUC_DOANH_NGHIEP>`** phải được]`<KHOAN>`** : **[c ) Niêm yết công khai tại địa điểm của **[sở giao dịch]`<CO_QUAN_THAM_QUYEN>`** , chi nhánh , **[văn phòng đại diện]`<TO_CHUC_DOANH_NGHIEP>`** , **[đơn vị sự nghiệp]`<TO_CHUC_DOANH_NGHIEP>`** chấm dứt hoạt động .]`<DIEM>`**

**Thực thể:**
- `[e0]` **Điều 16** → `DIEU` (span: `[0:2]`)
- `[e1]` **Khoản 1 . Quyết định chấm dứt hoạt động sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp của ngân hàng thương mại phải được** → `KHOAN` (span: `[3:24]`)
- `[e2]` **c ) Niêm yết công khai tại địa điểm của sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp chấm dứt hoạt động .** → `DIEM` (span: `[25:45]`)
- `[e3]` **sở giao dịch** → `CO_QUAN_THAM_QUYEN` (span: `[9:11]`) *(lồng trong `e1` (`KHOAN`))*
- `[e4]` **sở giao dịch** → `CO_QUAN_THAM_QUYEN` (span: `[32:34]`) *(lồng trong `e2` (`DIEM`))*
- `[e5]` **ngân hàng thương mại** → `TO_CHUC_DOANH_NGHIEP` (span: `[20:22]`) *(lồng trong `e1` (`KHOAN`))*
- `[e6]` **văn phòng đại diện** → `TO_CHUC_DOANH_NGHIEP` (span: `[14:16]`) *(lồng trong `e1` (`KHOAN`))*
- `[e7]` **văn phòng đại diện** → `TO_CHUC_DOANH_NGHIEP` (span: `[37:39]`) *(lồng trong `e2` (`DIEM`))*
- `[e8]` **đơn vị sự nghiệp** → `TO_CHUC_DOANH_NGHIEP` (span: `[17:19]`) *(lồng trong `e1` (`KHOAN`))*
- `[e9]` **đơn vị sự nghiệp** → `TO_CHUC_DOANH_NGHIEP` (span: `[40:42]`) *(lồng trong `e2` (`DIEM`))*

**Quan hệ:**
- (`e1` Khoản 1 . Quyết định chấm dứt hoạt động sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp của ngân hàng thương mại phải được `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 16 `[DIEU]`)
- (`e2` c ) Niêm yết công khai tại địa điểm của sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp chấm dứt hoạt động . `[DIEM]`) ==[ **THUOC_VE** ]==> (`e1` Khoản 1 . Quyết định chấm dứt hoạt động sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp của ngân hàng thương mại phải được `[KHOAN]`)


---

### Mẫu #13_2008_QĐ-NHNN_32111#body_context_85 (Loại: `body_context`)
> **[Quyết định]`<LOAI_VAN_BAN>`** số **[13/2008/QĐ-NHNN]`<SO_HIEU>`** của **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Ngân hàng]`<LINH_VUC>`** . **[Điều 17]`<DIEU>`** . **[7 . Không bị Thanh tra Ngân hàng xử phạt hành chính tổng cộng từ ba mươi triệu đồng trở lên trong thời gian một năm tính đến thời điểm đề nghị mở chi nhánh , **[văn phòng đại diện]`<TO_CHUC_DOANH_NGHIEP>`** ở nước ngoài ;]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Quyết định** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **13/2008/QĐ-NHNN** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_BAN_HANH` (span: `[4:7]`)
- `[e3]` **Ngân hàng** → `LINH_VUC` (span: `[9:10]`)
- `[e4]` **Điều 17** → `DIEU` (span: `[11:13]`)
- `[e5]` **7 . Không bị Thanh tra Ngân hàng xử phạt hành chính tổng cộng từ ba mươi triệu đồng trở lên trong thời gian một năm tính đến thời điểm đề nghị mở chi nhánh , văn phòng đại diện ở nước ngoài ;** → `KHOAN` (span: `[14:46]`)
- `[e6]` **văn phòng đại diện** → `TO_CHUC_DOANH_NGHIEP` (span: `[41:43]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Ngân hàng Nhà nước Việt Nam `[CO_QUAN_BAN_HANH]`)
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Quyết định `[LOAI_VAN_BAN]`)
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Ngân hàng `[LINH_VUC]`)
- (`e4` Điều 17 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`)
- (`e5` 7 . Không bị Thanh tra Ngân hàng xử phạt hành chính tổng cộng từ ba mươi triệu đồng trở lên trong thời gian một năm tính đến thời điểm đề nghị mở chi nhánh , văn phòng đại diện ở nước ngoài ; `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 17 `[DIEU]`)
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Ngân hàng `[LINH_VUC]`)
- (`e5` 7 . Không bị Thanh tra Ngân hàng xử phạt hành chính tổng cộng từ ba mươi triệu đồng trở lên trong thời gian một năm tính đến thời điểm đề nghị mở chi nhánh , văn phòng đại diện ở nước ngoài ; `[KHOAN]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Ngân hàng `[LINH_VUC]`)


---

### Mẫu #13_2008_QĐ-NHNN_32111#body_standalone_86 (Loại: `body_standalone`)
> **[Điều 17]`<DIEU>`** . **[7 . Không bị Thanh tra Ngân hàng xử phạt hành chính tổng cộng từ ba mươi triệu đồng trở lên trong thời gian một năm tính đến thời điểm đề nghị mở chi nhánh , **[văn phòng đại diện]`<TO_CHUC_DOANH_NGHIEP>`** ở nước ngoài ;]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 17** → `DIEU` (span: `[0:2]`)
- `[e1]` **7 . Không bị Thanh tra Ngân hàng xử phạt hành chính tổng cộng từ ba mươi triệu đồng trở lên trong thời gian một năm tính đến thời điểm đề nghị mở chi nhánh , văn phòng đại diện ở nước ngoài ;** → `KHOAN` (span: `[3:35]`)
- `[e2]` **văn phòng đại diện** → `TO_CHUC_DOANH_NGHIEP` (span: `[30:32]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 7 . Không bị Thanh tra Ngân hàng xử phạt hành chính tổng cộng từ ba mươi triệu đồng trở lên trong thời gian một năm tính đến thời điểm đề nghị mở chi nhánh , văn phòng đại diện ở nước ngoài ; `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 17 `[DIEU]`)


---

### Mẫu #13_2008_QĐ-NHNN_32111#body_context_87 (Loại: `body_context`)
> **[Quyết định]`<LOAI_VAN_BAN>`** số **[13/2008/QĐ-NHNN]`<SO_HIEU>`** của **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Ngân hàng]`<LINH_VUC>`** . **[Điều 18]`<DIEU>`** . **[Khoản 1]`<KHOAN>`** . **[a ) Văn bản của Chủ tịch **[Hội đồng quản trị]`<TO_CHUC_DOANH_NGHIEP>`** **[ngân hàng thương mại]`<TO_CHUC_DOANH_NGHIEP>`** đề nghị **[Ngân hàng Nhà nước]`<CO_QUAN_THAM_QUYEN>`** chấp thuận mở chi nhánh , **[văn phòng đại diện]`<TO_CHUC_DOANH_NGHIEP>`** ở nước ngoài theo **[Phụ lục 09]`<THAM_CHIEU_PHAP_LY>`** kèm theo Quy định này ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Quyết định** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **13/2008/QĐ-NHNN** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_BAN_HANH` (span: `[4:7]`)
- `[e3]` **Ngân hàng** → `LINH_VUC` (span: `[9:10]`)
- `[e4]` **Điều 18** → `DIEU` (span: `[11:13]`)
- `[e5]` **Khoản 1** → `KHOAN` (span: `[14:16]`)
- `[e6]` **a ) Văn bản của Chủ tịch Hội đồng quản trị ngân hàng thương mại đề nghị Ngân hàng Nhà nước chấp thuận mở chi nhánh , văn phòng đại diện ở nước ngoài theo Phụ lục 09 kèm theo Quy định này ;** → `DIEM` (span: `[17:45]`)
- `[e7]` **ngân hàng thương mại** → `TO_CHUC_DOANH_NGHIEP` (span: `[24:26]`) *(lồng trong `e6` (`DIEM`))*
- `[e8]` **văn phòng đại diện** → `TO_CHUC_DOANH_NGHIEP` (span: `[33:35]`) *(lồng trong `e6` (`DIEM`))*
- `[e9]` **Phụ lục 09** → `THAM_CHIEU_PHAP_LY` (span: `[38:40]`) *(lồng trong `e6` (`DIEM`))*
- `[e10]` **Ngân hàng Nhà nước** → `CO_QUAN_THAM_QUYEN` (span: `[27:29]`) *(lồng trong `e6` (`DIEM`))*
- `[e11]` **Hội đồng quản trị** → `TO_CHUC_DOANH_NGHIEP` (span: `[22:24]`) *(lồng trong `e6` (`DIEM`))*

**Quan hệ:**
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Ngân hàng Nhà nước Việt Nam `[CO_QUAN_BAN_HANH]`)
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Quyết định `[LOAI_VAN_BAN]`)
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Ngân hàng `[LINH_VUC]`)
- (`e4` Điều 18 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`)
- (`e5` Khoản 1 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 18 `[DIEU]`)
- (`e6` a ) Văn bản của Chủ tịch Hội đồng quản trị ngân hàng thương mại đề nghị Ngân hàng Nhà nước chấp thuận mở chi nhánh , văn phòng đại diện ở nước ngoài theo Phụ lục 09 kèm theo Quy định này ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e5` Khoản 1 `[KHOAN]`)
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Ngân hàng `[LINH_VUC]`)
- (`e6` a ) Văn bản của Chủ tịch Hội đồng quản trị ngân hàng thương mại đề nghị Ngân hàng Nhà nước chấp thuận mở chi nhánh , văn phòng đại diện ở nước ngoài theo Phụ lục 09 kèm theo Quy định này ; `[DIEM]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Ngân hàng `[LINH_VUC]`)
- (`e6` a ) Văn bản của Chủ tịch Hội đồng quản trị ngân hàng thương mại đề nghị Ngân hàng Nhà nước chấp thuận mở chi nhánh , văn phòng đại diện ở nước ngoài theo Phụ lục 09 kèm theo Quy định này ; `[DIEM]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e9` Phụ lục 09 `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #13_2008_QĐ-NHNN_32111#body_standalone_88 (Loại: `body_standalone`)
> **[Điều 18]`<DIEU>`** . **[Khoản 1]`<KHOAN>`** . **[a ) Văn bản của Chủ tịch **[Hội đồng quản trị]`<TO_CHUC_DOANH_NGHIEP>`** **[ngân hàng thương mại]`<TO_CHUC_DOANH_NGHIEP>`** đề nghị **[Ngân hàng Nhà nước]`<CO_QUAN_THAM_QUYEN>`** chấp thuận mở chi nhánh , **[văn phòng đại diện]`<TO_CHUC_DOANH_NGHIEP>`** ở nước ngoài theo **[Phụ lục 09]`<THAM_CHIEU_PHAP_LY>`** kèm theo Quy định này ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Điều 18** → `DIEU` (span: `[0:2]`)
- `[e1]` **Khoản 1** → `KHOAN` (span: `[3:5]`)
- `[e2]` **a ) Văn bản của Chủ tịch Hội đồng quản trị ngân hàng thương mại đề nghị Ngân hàng Nhà nước chấp thuận mở chi nhánh , văn phòng đại diện ở nước ngoài theo Phụ lục 09 kèm theo Quy định này ;** → `DIEM` (span: `[6:34]`)
- `[e3]` **ngân hàng thương mại** → `TO_CHUC_DOANH_NGHIEP` (span: `[13:15]`) *(lồng trong `e2` (`DIEM`))*
- `[e4]` **văn phòng đại diện** → `TO_CHUC_DOANH_NGHIEP` (span: `[22:24]`) *(lồng trong `e2` (`DIEM`))*
- `[e5]` **Phụ lục 09** → `THAM_CHIEU_PHAP_LY` (span: `[27:29]`) *(lồng trong `e2` (`DIEM`))*
- `[e6]` **Ngân hàng Nhà nước** → `CO_QUAN_THAM_QUYEN` (span: `[16:18]`) *(lồng trong `e2` (`DIEM`))*
- `[e7]` **Hội đồng quản trị** → `TO_CHUC_DOANH_NGHIEP` (span: `[11:13]`) *(lồng trong `e2` (`DIEM`))*

**Quan hệ:**
- (`e1` Khoản 1 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 18 `[DIEU]`)
- (`e2` a ) Văn bản của Chủ tịch Hội đồng quản trị ngân hàng thương mại đề nghị Ngân hàng Nhà nước chấp thuận mở chi nhánh , văn phòng đại diện ở nước ngoài theo Phụ lục 09 kèm theo Quy định này ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e1` Khoản 1 `[KHOAN]`)
- (`e2` a ) Văn bản của Chủ tịch Hội đồng quản trị ngân hàng thương mại đề nghị Ngân hàng Nhà nước chấp thuận mở chi nhánh , văn phòng đại diện ở nước ngoài theo Phụ lục 09 kèm theo Quy định này ; `[DIEM]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e5` Phụ lục 09 `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #13_2008_QĐ-NHNN_32111#body_context_89 (Loại: `body_context`)
> **[Quyết định]`<LOAI_VAN_BAN>`** số **[13/2008/QĐ-NHNN]`<SO_HIEU>`** ban hành **[ngày 29 tháng 04 năm 2008]`<NGAY_BAN_HANH>`** bởi **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_BAN_HANH>`** . **[Điều 18]`<DIEU>`** . **[4 . Trong thời hạn mười ngày làm việc kể từ ngày nhận đủ hồ sơ **[theo quy định tại]`<TU_KHOA_PHAP_LY>`** **[Khoản 1 Điều này]`<THAM_CHIEU_PHAP_LY>`** , **[Ngân hàng Nhà nước chi nhánh tỉnh , thành phố]`<CO_QUAN_THAM_QUYEN>`** nơi **[ngân hàng thương mại]`<TO_CHUC_DOANH_NGHIEP>`** đặt trụ sở chính gửi hồ sơ và báo cáo **[Ngân hàng Nhà nước]`<CO_QUAN_THAM_QUYEN>`** việc **[ngân hàng thương mại]`<TO_CHUC_DOANH_NGHIEP>`** đáp ứng các điều kiện mở chi nhánh , **[văn phòng đại diện]`<TO_CHUC_DOANH_NGHIEP>`** ở nước ngoài và có ý kiến nêu rõ đồng ý hoặc không đồng ý ; trường hợp không đồng ý , nêu rõ lý do .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Quyết định** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **13/2008/QĐ-NHNN** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_BAN_HANH` (span: `[11:14]`)
- `[e3]` **ngày 29 tháng 04 năm 2008** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 18** → `DIEU` (span: `[15:17]`)
- `[e5]` **4 . Trong thời hạn mười ngày làm việc kể từ ngày nhận đủ hồ sơ theo quy định tại Khoản 1 Điều này , Ngân hàng Nhà nước chi nhánh tỉnh , thành phố nơi ngân hàng thương mại đặt trụ sở chính gửi hồ sơ và báo cáo Ngân hàng Nhà nước việc ngân hàng thương mại đáp ứng các điều kiện mở chi nhánh , văn phòng đại diện ở nước ngoài và có ý kiến nêu rõ đồng ý hoặc không đồng ý ; trường hợp không đồng ý , nêu rõ lý do .** → `KHOAN` (span: `[18:88]`)
- `[e6]` **ngân hàng thương mại** → `TO_CHUC_DOANH_NGHIEP` (span: `[46:48]`) *(lồng trong `e5` (`KHOAN`))*
- `[e7]` **ngân hàng thương mại** → `TO_CHUC_DOANH_NGHIEP` (span: `[58:60]`) *(lồng trong `e5` (`KHOAN`))*
- `[e8]` **văn phòng đại diện** → `TO_CHUC_DOANH_NGHIEP` (span: `[66:68]`) *(lồng trong `e5` (`KHOAN`))*
- `[e9]` **Khoản 1 Điều này** → `THAM_CHIEU_PHAP_LY` (span: `[34:38]`) *(lồng trong `e5` (`KHOAN`))*
- `[e10]` **theo quy định tại** → `TU_KHOA_PHAP_LY` (span: `[31:34]`) *(lồng trong `e5` (`KHOAN`))*
- `[e11]` **Ngân hàng Nhà nước chi nhánh tỉnh , thành phố** → `CO_QUAN_THAM_QUYEN` (span: `[39:45]`) *(lồng trong `e5` (`KHOAN`))*
- `[e12]` **Ngân hàng Nhà nước** → `CO_QUAN_THAM_QUYEN` (span: `[55:57]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Ngân hàng Nhà nước Việt Nam `[CO_QUAN_BAN_HANH]`)
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Quyết định `[LOAI_VAN_BAN]`)
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 29 tháng 04 năm 2008 `[NGAY_BAN_HANH]`)
- (`e4` Điều 18 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`)
- (`e5` 4 . Trong thời hạn mười ngày làm việc kể từ ngày nhận đủ hồ sơ theo quy định tại Khoản 1 Điều này , Ngân hàng Nhà nước chi nhánh tỉnh , thành phố nơi ngân hàng thương mại đặt trụ sở chính gửi hồ sơ và báo cáo Ngân hàng Nhà nước việc ngân hàng thương mại đáp ứng các điều kiện mở chi nhánh , văn phòng đại diện ở nước ngoài và có ý kiến nêu rõ đồng ý hoặc không đồng ý ; trường hợp không đồng ý , nêu rõ lý do . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 18 `[DIEU]`)
- (`e10` theo quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e9` Khoản 1 Điều này `[THAM_CHIEU_PHAP_LY]`)
- (`e5` 4 . Trong thời hạn mười ngày làm việc kể từ ngày nhận đủ hồ sơ theo quy định tại Khoản 1 Điều này , Ngân hàng Nhà nước chi nhánh tỉnh , thành phố nơi ngân hàng thương mại đặt trụ sở chính gửi hồ sơ và báo cáo Ngân hàng Nhà nước việc ngân hàng thương mại đáp ứng các điều kiện mở chi nhánh , văn phòng đại diện ở nước ngoài và có ý kiến nêu rõ đồng ý hoặc không đồng ý ; trường hợp không đồng ý , nêu rõ lý do . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e9` Khoản 1 Điều này `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #13_2008_QĐ-NHNN_32111#body_standalone_90 (Loại: `body_standalone`)
> **[Điều 18]`<DIEU>`** . **[4 . Trong thời hạn mười ngày làm việc kể từ ngày nhận đủ hồ sơ **[theo quy định tại]`<TU_KHOA_PHAP_LY>`** **[Khoản 1 Điều này]`<THAM_CHIEU_PHAP_LY>`** , **[Ngân hàng Nhà nước chi nhánh tỉnh , thành phố]`<CO_QUAN_THAM_QUYEN>`** nơi **[ngân hàng thương mại]`<TO_CHUC_DOANH_NGHIEP>`** đặt trụ sở chính gửi hồ sơ và báo cáo **[Ngân hàng Nhà nước]`<CO_QUAN_THAM_QUYEN>`** việc **[ngân hàng thương mại]`<TO_CHUC_DOANH_NGHIEP>`** đáp ứng các điều kiện mở chi nhánh , **[văn phòng đại diện]`<TO_CHUC_DOANH_NGHIEP>`** ở nước ngoài và có ý kiến nêu rõ đồng ý hoặc không đồng ý ; trường hợp không đồng ý , nêu rõ lý do .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 18** → `DIEU` (span: `[0:2]`)
- `[e1]` **4 . Trong thời hạn mười ngày làm việc kể từ ngày nhận đủ hồ sơ theo quy định tại Khoản 1 Điều này , Ngân hàng Nhà nước chi nhánh tỉnh , thành phố nơi ngân hàng thương mại đặt trụ sở chính gửi hồ sơ và báo cáo Ngân hàng Nhà nước việc ngân hàng thương mại đáp ứng các điều kiện mở chi nhánh , văn phòng đại diện ở nước ngoài và có ý kiến nêu rõ đồng ý hoặc không đồng ý ; trường hợp không đồng ý , nêu rõ lý do .** → `KHOAN` (span: `[3:73]`)
- `[e2]` **ngân hàng thương mại** → `TO_CHUC_DOANH_NGHIEP` (span: `[31:33]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **ngân hàng thương mại** → `TO_CHUC_DOANH_NGHIEP` (span: `[43:45]`) *(lồng trong `e1` (`KHOAN`))*
- `[e4]` **văn phòng đại diện** → `TO_CHUC_DOANH_NGHIEP` (span: `[51:53]`) *(lồng trong `e1` (`KHOAN`))*
- `[e5]` **Khoản 1 Điều này** → `THAM_CHIEU_PHAP_LY` (span: `[19:23]`) *(lồng trong `e1` (`KHOAN`))*
- `[e6]` **theo quy định tại** → `TU_KHOA_PHAP_LY` (span: `[16:19]`) *(lồng trong `e1` (`KHOAN`))*
- `[e7]` **Ngân hàng Nhà nước chi nhánh tỉnh , thành phố** → `CO_QUAN_THAM_QUYEN` (span: `[24:30]`) *(lồng trong `e1` (`KHOAN`))*
- `[e8]` **Ngân hàng Nhà nước** → `CO_QUAN_THAM_QUYEN` (span: `[40:42]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 4 . Trong thời hạn mười ngày làm việc kể từ ngày nhận đủ hồ sơ theo quy định tại Khoản 1 Điều này , Ngân hàng Nhà nước chi nhánh tỉnh , thành phố nơi ngân hàng thương mại đặt trụ sở chính gửi hồ sơ và báo cáo Ngân hàng Nhà nước việc ngân hàng thương mại đáp ứng các điều kiện mở chi nhánh , văn phòng đại diện ở nước ngoài và có ý kiến nêu rõ đồng ý hoặc không đồng ý ; trường hợp không đồng ý , nêu rõ lý do . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 18 `[DIEU]`)
- (`e6` theo quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e5` Khoản 1 Điều này `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 4 . Trong thời hạn mười ngày làm việc kể từ ngày nhận đủ hồ sơ theo quy định tại Khoản 1 Điều này , Ngân hàng Nhà nước chi nhánh tỉnh , thành phố nơi ngân hàng thương mại đặt trụ sở chính gửi hồ sơ và báo cáo Ngân hàng Nhà nước việc ngân hàng thương mại đáp ứng các điều kiện mở chi nhánh , văn phòng đại diện ở nước ngoài và có ý kiến nêu rõ đồng ý hoặc không đồng ý ; trường hợp không đồng ý , nêu rõ lý do . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e5` Khoản 1 Điều này `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #13_2008_QĐ-NHNN_32111#body_context_91 (Loại: `body_context`)
> **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_BAN_HANH>`** ban hành **[Quyết định]`<LOAI_VAN_BAN>`** số **[13/2008/QĐ-NHNN]`<SO_HIEU>`** . **[Điều 18]`<DIEU>`** . **[5 . Trong thời hạn ba mươi ngày làm việc kể từ ngày nhận được hồ sơ và báo cáo của **[Ngân hàng Nhà nước chi nhánh tỉnh , thành phố]`<CO_QUAN_THAM_QUYEN>`** nơi **[ngân hàng thương mại]`<TO_CHUC_DOANH_NGHIEP>`** đặt trụ sở chính **[quy định tại]`<TU_KHOA_PHAP_LY>`** **[Khoản 4 Điều này]`<THAM_CHIEU_PHAP_LY>`** , **[Ngân hàng Nhà nước]`<CO_QUAN_THAM_QUYEN>`** có **[văn bản chấp thuận]`<GIAY_TO_HO_SO>`** đề nghị mở chi nhánh , **[văn phòng đại diện]`<TO_CHUC_DOANH_NGHIEP>`** ở nước ngoài theo **[Phụ lục 10]`<THAM_CHIEU_PHAP_LY>`** kèm theo Quy định này ; trường hợp không chấp thuận , có văn bản nêu rõ lý do hoặc các yêu cầu ( nếu]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Quyết định** → `LOAI_VAN_BAN` (span: `[4:5]`)
- `[e1]` **13/2008/QĐ-NHNN** → `SO_HIEU` (span: `[6:7]`)
- `[e2]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_BAN_HANH` (span: `[0:3]`)
- `[e3]` **Điều 18** → `DIEU` (span: `[8:10]`)
- `[e4]` **5 . Trong thời hạn ba mươi ngày làm việc kể từ ngày nhận được hồ sơ và báo cáo của Ngân hàng Nhà nước chi nhánh tỉnh , thành phố nơi ngân hàng thương mại đặt trụ sở chính quy định tại Khoản 4 Điều này , Ngân hàng Nhà nước có văn bản chấp thuận đề nghị mở chi nhánh , văn phòng đại diện ở nước ngoài theo Phụ lục 10 kèm theo Quy định này ; trường hợp không chấp thuận , có văn bản nêu rõ lý do hoặc các yêu cầu ( nếu** → `KHOAN` (span: `[11:82]`)
- `[e5]` **ngân hàng thương mại** → `TO_CHUC_DOANH_NGHIEP` (span: `[35:37]`) *(lồng trong `e4` (`KHOAN`))*
- `[e6]` **văn phòng đại diện** → `TO_CHUC_DOANH_NGHIEP` (span: `[56:58]`) *(lồng trong `e4` (`KHOAN`))*
- `[e7]` **Khoản 4 Điều này** → `THAM_CHIEU_PHAP_LY` (span: `[42:46]`) *(lồng trong `e4` (`KHOAN`))*
- `[e8]` **Phụ lục 10** → `THAM_CHIEU_PHAP_LY` (span: `[61:63]`) *(lồng trong `e4` (`KHOAN`))*
- `[e9]` **quy định tại** → `TU_KHOA_PHAP_LY` (span: `[40:42]`) *(lồng trong `e4` (`KHOAN`))*
- `[e10]` **Ngân hàng Nhà nước chi nhánh tỉnh , thành phố** → `CO_QUAN_THAM_QUYEN` (span: `[28:34]`) *(lồng trong `e4` (`KHOAN`))*
- `[e11]` **Ngân hàng Nhà nước** → `CO_QUAN_THAM_QUYEN` (span: `[47:49]`) *(lồng trong `e4` (`KHOAN`))*
- `[e12]` **văn bản chấp thuận** → `GIAY_TO_HO_SO` (span: `[50:52]`) *(lồng trong `e4` (`KHOAN`))*

**Quan hệ:**
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Ngân hàng Nhà nước Việt Nam `[CO_QUAN_BAN_HANH]`)
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Quyết định `[LOAI_VAN_BAN]`)
- (`e3` Điều 18 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`)
- (`e4` 5 . Trong thời hạn ba mươi ngày làm việc kể từ ngày nhận được hồ sơ và báo cáo của Ngân hàng Nhà nước chi nhánh tỉnh , thành phố nơi ngân hàng thương mại đặt trụ sở chính quy định tại Khoản 4 Điều này , Ngân hàng Nhà nước có văn bản chấp thuận đề nghị mở chi nhánh , văn phòng đại diện ở nước ngoài theo Phụ lục 10 kèm theo Quy định này ; trường hợp không chấp thuận , có văn bản nêu rõ lý do hoặc các yêu cầu ( nếu `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 18 `[DIEU]`)
- (`e9` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e7` Khoản 4 Điều này `[THAM_CHIEU_PHAP_LY]`)
- (`e4` 5 . Trong thời hạn ba mươi ngày làm việc kể từ ngày nhận được hồ sơ và báo cáo của Ngân hàng Nhà nước chi nhánh tỉnh , thành phố nơi ngân hàng thương mại đặt trụ sở chính quy định tại Khoản 4 Điều này , Ngân hàng Nhà nước có văn bản chấp thuận đề nghị mở chi nhánh , văn phòng đại diện ở nước ngoài theo Phụ lục 10 kèm theo Quy định này ; trường hợp không chấp thuận , có văn bản nêu rõ lý do hoặc các yêu cầu ( nếu `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e7` Khoản 4 Điều này `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e9` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e8` Phụ lục 10 `[THAM_CHIEU_PHAP_LY]`)
- (`e4` 5 . Trong thời hạn ba mươi ngày làm việc kể từ ngày nhận được hồ sơ và báo cáo của Ngân hàng Nhà nước chi nhánh tỉnh , thành phố nơi ngân hàng thương mại đặt trụ sở chính quy định tại Khoản 4 Điều này , Ngân hàng Nhà nước có văn bản chấp thuận đề nghị mở chi nhánh , văn phòng đại diện ở nước ngoài theo Phụ lục 10 kèm theo Quy định này ; trường hợp không chấp thuận , có văn bản nêu rõ lý do hoặc các yêu cầu ( nếu `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e8` Phụ lục 10 `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #13_2008_QĐ-NHNN_32111#body_standalone_92 (Loại: `body_standalone`)
> **[Điều 18]`<DIEU>`** . **[5 . Trong thời hạn ba mươi ngày làm việc kể từ ngày nhận được hồ sơ và báo cáo của **[Ngân hàng Nhà nước chi nhánh tỉnh , thành phố]`<CO_QUAN_THAM_QUYEN>`** nơi **[ngân hàng thương mại]`<TO_CHUC_DOANH_NGHIEP>`** đặt trụ sở chính **[quy định tại]`<TU_KHOA_PHAP_LY>`** **[Khoản 4 Điều này]`<THAM_CHIEU_PHAP_LY>`** , **[Ngân hàng Nhà nước]`<CO_QUAN_THAM_QUYEN>`** có **[văn bản chấp thuận]`<GIAY_TO_HO_SO>`** đề nghị mở chi nhánh , **[văn phòng đại diện]`<TO_CHUC_DOANH_NGHIEP>`** ở nước ngoài theo **[Phụ lục 10]`<THAM_CHIEU_PHAP_LY>`** kèm theo Quy định này ; trường hợp không chấp thuận , có văn bản nêu rõ lý do hoặc các yêu cầu ( nếu]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 18** → `DIEU` (span: `[0:2]`)
- `[e1]` **5 . Trong thời hạn ba mươi ngày làm việc kể từ ngày nhận được hồ sơ và báo cáo của Ngân hàng Nhà nước chi nhánh tỉnh , thành phố nơi ngân hàng thương mại đặt trụ sở chính quy định tại Khoản 4 Điều này , Ngân hàng Nhà nước có văn bản chấp thuận đề nghị mở chi nhánh , văn phòng đại diện ở nước ngoài theo Phụ lục 10 kèm theo Quy định này ; trường hợp không chấp thuận , có văn bản nêu rõ lý do hoặc các yêu cầu ( nếu** → `KHOAN` (span: `[3:74]`)
- `[e2]` **ngân hàng thương mại** → `TO_CHUC_DOANH_NGHIEP` (span: `[27:29]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **văn phòng đại diện** → `TO_CHUC_DOANH_NGHIEP` (span: `[48:50]`) *(lồng trong `e1` (`KHOAN`))*
- `[e4]` **Khoản 4 Điều này** → `THAM_CHIEU_PHAP_LY` (span: `[34:38]`) *(lồng trong `e1` (`KHOAN`))*
- `[e5]` **Phụ lục 10** → `THAM_CHIEU_PHAP_LY` (span: `[53:55]`) *(lồng trong `e1` (`KHOAN`))*
- `[e6]` **quy định tại** → `TU_KHOA_PHAP_LY` (span: `[32:34]`) *(lồng trong `e1` (`KHOAN`))*
- `[e7]` **Ngân hàng Nhà nước chi nhánh tỉnh , thành phố** → `CO_QUAN_THAM_QUYEN` (span: `[20:26]`) *(lồng trong `e1` (`KHOAN`))*
- `[e8]` **Ngân hàng Nhà nước** → `CO_QUAN_THAM_QUYEN` (span: `[39:41]`) *(lồng trong `e1` (`KHOAN`))*
- `[e9]` **văn bản chấp thuận** → `GIAY_TO_HO_SO` (span: `[42:44]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 5 . Trong thời hạn ba mươi ngày làm việc kể từ ngày nhận được hồ sơ và báo cáo của Ngân hàng Nhà nước chi nhánh tỉnh , thành phố nơi ngân hàng thương mại đặt trụ sở chính quy định tại Khoản 4 Điều này , Ngân hàng Nhà nước có văn bản chấp thuận đề nghị mở chi nhánh , văn phòng đại diện ở nước ngoài theo Phụ lục 10 kèm theo Quy định này ; trường hợp không chấp thuận , có văn bản nêu rõ lý do hoặc các yêu cầu ( nếu `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 18 `[DIEU]`)
- (`e6` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e4` Khoản 4 Điều này `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 5 . Trong thời hạn ba mươi ngày làm việc kể từ ngày nhận được hồ sơ và báo cáo của Ngân hàng Nhà nước chi nhánh tỉnh , thành phố nơi ngân hàng thương mại đặt trụ sở chính quy định tại Khoản 4 Điều này , Ngân hàng Nhà nước có văn bản chấp thuận đề nghị mở chi nhánh , văn phòng đại diện ở nước ngoài theo Phụ lục 10 kèm theo Quy định này ; trường hợp không chấp thuận , có văn bản nêu rõ lý do hoặc các yêu cầu ( nếu `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e4` Khoản 4 Điều này `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e6` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e5` Phụ lục 10 `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 5 . Trong thời hạn ba mươi ngày làm việc kể từ ngày nhận được hồ sơ và báo cáo của Ngân hàng Nhà nước chi nhánh tỉnh , thành phố nơi ngân hàng thương mại đặt trụ sở chính quy định tại Khoản 4 Điều này , Ngân hàng Nhà nước có văn bản chấp thuận đề nghị mở chi nhánh , văn phòng đại diện ở nước ngoài theo Phụ lục 10 kèm theo Quy định này ; trường hợp không chấp thuận , có văn bản nêu rõ lý do hoặc các yêu cầu ( nếu `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e5` Phụ lục 10 `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #13_2008_QĐ-NHNN_32111#body_context_93 (Loại: `body_context`)
> **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_BAN_HANH>`** ban hành **[Quyết định]`<LOAI_VAN_BAN>`** số **[13/2008/QĐ-NHNN]`<SO_HIEU>`** . **[Điều 18]`<DIEU>`** . **[6 . Trong thời hạn mười tám tháng kể từ ngày có **[văn bản chấp thuận]`<GIAY_TO_HO_SO>`** của **[Ngân hàng Nhà nước]`<CO_QUAN_THAM_QUYEN>`** , **[ngân hàng thương mại]`<TO_CHUC_DOANH_NGHIEP>`** phải hoàn thành các thủ tục pháp lý , chuẩn bị cơ sở vật chất , nhân sự theo quy định của nước sở tại nơi mở chi nhánh , **[văn phòng đại diện]`<TO_CHUC_DOANH_NGHIEP>`** để được **[cơ quan có thẩm quyền]`<CO_QUAN_THAM_QUYEN>`** của nước sở tại **[cấp **[giấy phép mở chi nhánh]`<GIAY_TO_HO_SO>`**]`<NGHIA_VU_QUYEN>`** , **[văn phòng đại diện]`<TO_CHUC_DOANH_NGHIEP>`** .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Quyết định** → `LOAI_VAN_BAN` (span: `[4:5]`)
- `[e1]` **13/2008/QĐ-NHNN** → `SO_HIEU` (span: `[6:7]`)
- `[e2]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_BAN_HANH` (span: `[0:3]`)
- `[e3]` **Điều 18** → `DIEU` (span: `[8:10]`)
- `[e4]` **6 . Trong thời hạn mười tám tháng kể từ ngày có văn bản chấp thuận của Ngân hàng Nhà nước , ngân hàng thương mại phải hoàn thành các thủ tục pháp lý , chuẩn bị cơ sở vật chất , nhân sự theo quy định của nước sở tại nơi mở chi nhánh , văn phòng đại diện để được cơ quan có thẩm quyền của nước sở tại cấp giấy phép mở chi nhánh , văn phòng đại diện .** → `KHOAN` (span: `[11:68]`)
- `[e5]` **cấp giấy phép mở chi nhánh** → `NGHIA_VU_QUYEN` (span: `[60:64]`) *(lồng trong `e4` (`KHOAN`))*
- `[e6]` **ngân hàng thương mại** → `TO_CHUC_DOANH_NGHIEP` (span: `[28:30]`) *(lồng trong `e4` (`KHOAN`))*
- `[e7]` **văn phòng đại diện** → `TO_CHUC_DOANH_NGHIEP` (span: `[50:52]`) *(lồng trong `e4` (`KHOAN`))*
- `[e8]` **văn phòng đại diện** → `TO_CHUC_DOANH_NGHIEP` (span: `[65:67]`) *(lồng trong `e4` (`KHOAN`))*
- `[e9]` **Ngân hàng Nhà nước** → `CO_QUAN_THAM_QUYEN` (span: `[25:27]`) *(lồng trong `e4` (`KHOAN`))*
- `[e10]` **cơ quan có thẩm quyền** → `CO_QUAN_THAM_QUYEN` (span: `[54:57]`) *(lồng trong `e4` (`KHOAN`))*
- `[e11]` **văn bản chấp thuận** → `GIAY_TO_HO_SO` (span: `[22:24]`) *(lồng trong `e4` (`KHOAN`))*
- `[e12]` **giấy phép mở chi nhánh** → `GIAY_TO_HO_SO` (span: `[61:64]`) *(lồng trong `e4` (`KHOAN`), `e5` (`NGHIA_VU_QUYEN`))*

**Quan hệ:**
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Ngân hàng Nhà nước Việt Nam `[CO_QUAN_BAN_HANH]`)
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Quyết định `[LOAI_VAN_BAN]`)
- (`e3` Điều 18 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`)
- (`e4` 6 . Trong thời hạn mười tám tháng kể từ ngày có văn bản chấp thuận của Ngân hàng Nhà nước , ngân hàng thương mại phải hoàn thành các thủ tục pháp lý , chuẩn bị cơ sở vật chất , nhân sự theo quy định của nước sở tại nơi mở chi nhánh , văn phòng đại diện để được cơ quan có thẩm quyền của nước sở tại cấp giấy phép mở chi nhánh , văn phòng đại diện . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 18 `[DIEU]`)
- (`e5` cấp giấy phép mở chi nhánh `[NGHIA_VU_QUYEN]`) ==[ **TAC_DONG_DOI_TUONG** ]==> (`e12` giấy phép mở chi nhánh `[GIAY_TO_HO_SO]`) *(Quan hệ lồng nhau)*
- (`e6` ngân hàng thương mại `[TO_CHUC_DOANH_NGHIEP]`) ==[ **CO_NGHIA_VU_QUYEN** ]==> (`e5` cấp giấy phép mở chi nhánh `[NGHIA_VU_QUYEN]`)
- (`e7` văn phòng đại diện `[TO_CHUC_DOANH_NGHIEP]`) ==[ **CO_NGHIA_VU_QUYEN** ]==> (`e5` cấp giấy phép mở chi nhánh `[NGHIA_VU_QUYEN]`)
- (`e5` cấp giấy phép mở chi nhánh `[NGHIA_VU_QUYEN]`) ==[ **TAC_DONG_CHU_THE** ]==> (`e8` văn phòng đại diện `[TO_CHUC_DOANH_NGHIEP]`)
- (`e9` Ngân hàng Nhà nước `[CO_QUAN_THAM_QUYEN]`) ==[ **CO_THAM_QUYEN** ]==> (`e5` cấp giấy phép mở chi nhánh `[NGHIA_VU_QUYEN]`)
- (`e10` cơ quan có thẩm quyền `[CO_QUAN_THAM_QUYEN]`) ==[ **CO_THAM_QUYEN** ]==> (`e5` cấp giấy phép mở chi nhánh `[NGHIA_VU_QUYEN]`)
- (`e5` cấp giấy phép mở chi nhánh `[NGHIA_VU_QUYEN]`) ==[ **TAC_DONG_DOI_TUONG** ]==> (`e11` văn bản chấp thuận `[GIAY_TO_HO_SO]`)


---

### Mẫu #13_2008_QĐ-NHNN_32111#body_standalone_94 (Loại: `body_standalone`)
> **[Điều 18]`<DIEU>`** . **[6 . Trong thời hạn mười tám tháng kể từ ngày có **[văn bản chấp thuận]`<GIAY_TO_HO_SO>`** của **[Ngân hàng Nhà nước]`<CO_QUAN_THAM_QUYEN>`** , **[ngân hàng thương mại]`<TO_CHUC_DOANH_NGHIEP>`** phải hoàn thành các thủ tục pháp lý , chuẩn bị cơ sở vật chất , nhân sự theo quy định của nước sở tại nơi mở chi nhánh , **[văn phòng đại diện]`<TO_CHUC_DOANH_NGHIEP>`** để được **[cơ quan có thẩm quyền]`<CO_QUAN_THAM_QUYEN>`** của nước sở tại **[cấp **[giấy phép mở chi nhánh]`<GIAY_TO_HO_SO>`**]`<NGHIA_VU_QUYEN>`** , **[văn phòng đại diện]`<TO_CHUC_DOANH_NGHIEP>`** .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 18** → `DIEU` (span: `[0:2]`)
- `[e1]` **6 . Trong thời hạn mười tám tháng kể từ ngày có văn bản chấp thuận của Ngân hàng Nhà nước , ngân hàng thương mại phải hoàn thành các thủ tục pháp lý , chuẩn bị cơ sở vật chất , nhân sự theo quy định của nước sở tại nơi mở chi nhánh , văn phòng đại diện để được cơ quan có thẩm quyền của nước sở tại cấp giấy phép mở chi nhánh , văn phòng đại diện .** → `KHOAN` (span: `[3:60]`)
- `[e2]` **cấp giấy phép mở chi nhánh** → `NGHIA_VU_QUYEN` (span: `[52:56]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **ngân hàng thương mại** → `TO_CHUC_DOANH_NGHIEP` (span: `[20:22]`) *(lồng trong `e1` (`KHOAN`))*
- `[e4]` **văn phòng đại diện** → `TO_CHUC_DOANH_NGHIEP` (span: `[42:44]`) *(lồng trong `e1` (`KHOAN`))*
- `[e5]` **văn phòng đại diện** → `TO_CHUC_DOANH_NGHIEP` (span: `[57:59]`) *(lồng trong `e1` (`KHOAN`))*
- `[e6]` **Ngân hàng Nhà nước** → `CO_QUAN_THAM_QUYEN` (span: `[17:19]`) *(lồng trong `e1` (`KHOAN`))*
- `[e7]` **cơ quan có thẩm quyền** → `CO_QUAN_THAM_QUYEN` (span: `[46:49]`) *(lồng trong `e1` (`KHOAN`))*
- `[e8]` **văn bản chấp thuận** → `GIAY_TO_HO_SO` (span: `[14:16]`) *(lồng trong `e1` (`KHOAN`))*
- `[e9]` **giấy phép mở chi nhánh** → `GIAY_TO_HO_SO` (span: `[53:56]`) *(lồng trong `e1` (`KHOAN`), `e2` (`NGHIA_VU_QUYEN`))*

**Quan hệ:**
- (`e1` 6 . Trong thời hạn mười tám tháng kể từ ngày có văn bản chấp thuận của Ngân hàng Nhà nước , ngân hàng thương mại phải hoàn thành các thủ tục pháp lý , chuẩn bị cơ sở vật chất , nhân sự theo quy định của nước sở tại nơi mở chi nhánh , văn phòng đại diện để được cơ quan có thẩm quyền của nước sở tại cấp giấy phép mở chi nhánh , văn phòng đại diện . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 18 `[DIEU]`)
- (`e2` cấp giấy phép mở chi nhánh `[NGHIA_VU_QUYEN]`) ==[ **TAC_DONG_DOI_TUONG** ]==> (`e9` giấy phép mở chi nhánh `[GIAY_TO_HO_SO]`) *(Quan hệ lồng nhau)*
- (`e3` ngân hàng thương mại `[TO_CHUC_DOANH_NGHIEP]`) ==[ **CO_NGHIA_VU_QUYEN** ]==> (`e2` cấp giấy phép mở chi nhánh `[NGHIA_VU_QUYEN]`)
- (`e4` văn phòng đại diện `[TO_CHUC_DOANH_NGHIEP]`) ==[ **CO_NGHIA_VU_QUYEN** ]==> (`e2` cấp giấy phép mở chi nhánh `[NGHIA_VU_QUYEN]`)
- (`e2` cấp giấy phép mở chi nhánh `[NGHIA_VU_QUYEN]`) ==[ **TAC_DONG_CHU_THE** ]==> (`e5` văn phòng đại diện `[TO_CHUC_DOANH_NGHIEP]`)
- (`e6` Ngân hàng Nhà nước `[CO_QUAN_THAM_QUYEN]`) ==[ **CO_THAM_QUYEN** ]==> (`e2` cấp giấy phép mở chi nhánh `[NGHIA_VU_QUYEN]`)
- (`e7` cơ quan có thẩm quyền `[CO_QUAN_THAM_QUYEN]`) ==[ **CO_THAM_QUYEN** ]==> (`e2` cấp giấy phép mở chi nhánh `[NGHIA_VU_QUYEN]`)
- (`e2` cấp giấy phép mở chi nhánh `[NGHIA_VU_QUYEN]`) ==[ **TAC_DONG_DOI_TUONG** ]==> (`e8` văn bản chấp thuận `[GIAY_TO_HO_SO]`)


---

### Mẫu #13_2008_QĐ-NHNN_32111#body_context_95 (Loại: `body_context`)
> **[Quyết định]`<LOAI_VAN_BAN>`** số **[13/2008/QĐ-NHNN]`<SO_HIEU>`** của **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Ngân hàng]`<LINH_VUC>`** . **[Điều 18]`<DIEU>`** . **[7 . Kết thúc thời hạn **[quy định tại]`<TU_KHOA_PHAP_LY>`** **[Khoản 6 Điều này]`<THAM_CHIEU_PHAP_LY>`** , **[ngân hàng thương mại]`<TO_CHUC_DOANH_NGHIEP>`** chưa được **[cơ quan có thẩm quyền]`<CO_QUAN_THAM_QUYEN>`** của nước sở tại **[cấp **[giấy phép mở chi nhánh]`<GIAY_TO_HO_SO>`**]`<NGHIA_VU_QUYEN>`** , **[văn phòng đại diện]`<TO_CHUC_DOANH_NGHIEP>`** , **[văn bản chấp thuận]`<GIAY_TO_HO_SO>`** của **[Ngân hàng Nhà nước]`<CO_QUAN_THAM_QUYEN>`** không còn giá trị .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Quyết định** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **13/2008/QĐ-NHNN** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_BAN_HANH` (span: `[4:7]`)
- `[e3]` **Ngân hàng** → `LINH_VUC` (span: `[9:10]`)
- `[e4]` **Điều 18** → `DIEU` (span: `[11:13]`)
- `[e5]` **7 . Kết thúc thời hạn quy định tại Khoản 6 Điều này , ngân hàng thương mại chưa được cơ quan có thẩm quyền của nước sở tại cấp giấy phép mở chi nhánh , văn phòng đại diện , văn bản chấp thuận của Ngân hàng Nhà nước không còn giá trị .** → `KHOAN` (span: `[14:52]`)
- `[e6]` **cấp giấy phép mở chi nhánh** → `NGHIA_VU_QUYEN` (span: `[35:39]`) *(lồng trong `e5` (`KHOAN`))*
- `[e7]` **ngân hàng thương mại** → `TO_CHUC_DOANH_NGHIEP` (span: `[25:27]`) *(lồng trong `e5` (`KHOAN`))*
- `[e8]` **văn phòng đại diện** → `TO_CHUC_DOANH_NGHIEP` (span: `[40:42]`) *(lồng trong `e5` (`KHOAN`))*
- `[e9]` **Khoản 6 Điều này** → `THAM_CHIEU_PHAP_LY` (span: `[20:24]`) *(lồng trong `e5` (`KHOAN`))*
- `[e10]` **quy định tại** → `TU_KHOA_PHAP_LY` (span: `[18:20]`) *(lồng trong `e5` (`KHOAN`))*
- `[e11]` **cơ quan có thẩm quyền** → `CO_QUAN_THAM_QUYEN` (span: `[29:32]`) *(lồng trong `e5` (`KHOAN`))*
- `[e12]` **Ngân hàng Nhà nước** → `CO_QUAN_THAM_QUYEN` (span: `[46:48]`) *(lồng trong `e5` (`KHOAN`))*
- `[e13]` **văn bản chấp thuận** → `GIAY_TO_HO_SO` (span: `[43:45]`) *(lồng trong `e5` (`KHOAN`))*
- `[e14]` **giấy phép mở chi nhánh** → `GIAY_TO_HO_SO` (span: `[36:39]`) *(lồng trong `e5` (`KHOAN`), `e6` (`NGHIA_VU_QUYEN`))*

**Quan hệ:**
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Ngân hàng Nhà nước Việt Nam `[CO_QUAN_BAN_HANH]`)
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Quyết định `[LOAI_VAN_BAN]`)
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Ngân hàng `[LINH_VUC]`)
- (`e4` Điều 18 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`)
- (`e5` 7 . Kết thúc thời hạn quy định tại Khoản 6 Điều này , ngân hàng thương mại chưa được cơ quan có thẩm quyền của nước sở tại cấp giấy phép mở chi nhánh , văn phòng đại diện , văn bản chấp thuận của Ngân hàng Nhà nước không còn giá trị . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 18 `[DIEU]`)
- (`e6` cấp giấy phép mở chi nhánh `[NGHIA_VU_QUYEN]`) ==[ **TAC_DONG_DOI_TUONG** ]==> (`e14` giấy phép mở chi nhánh `[GIAY_TO_HO_SO]`) *(Quan hệ lồng nhau)*
- (`e7` ngân hàng thương mại `[TO_CHUC_DOANH_NGHIEP]`) ==[ **CO_NGHIA_VU_QUYEN** ]==> (`e6` cấp giấy phép mở chi nhánh `[NGHIA_VU_QUYEN]`)
- (`e6` cấp giấy phép mở chi nhánh `[NGHIA_VU_QUYEN]`) ==[ **TAC_DONG_CHU_THE** ]==> (`e8` văn phòng đại diện `[TO_CHUC_DOANH_NGHIEP]`)
- (`e11` cơ quan có thẩm quyền `[CO_QUAN_THAM_QUYEN]`) ==[ **CO_THAM_QUYEN** ]==> (`e6` cấp giấy phép mở chi nhánh `[NGHIA_VU_QUYEN]`)
- (`e6` cấp giấy phép mở chi nhánh `[NGHIA_VU_QUYEN]`) ==[ **TAC_DONG_CHU_THE** ]==> (`e12` Ngân hàng Nhà nước `[CO_QUAN_THAM_QUYEN]`)
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Ngân hàng `[LINH_VUC]`)
- (`e6` cấp giấy phép mở chi nhánh `[NGHIA_VU_QUYEN]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Ngân hàng `[LINH_VUC]`)
- (`e10` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e9` Khoản 6 Điều này `[THAM_CHIEU_PHAP_LY]`)
- (`e6` cấp giấy phép mở chi nhánh `[NGHIA_VU_QUYEN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e9` Khoản 6 Điều này `[THAM_CHIEU_PHAP_LY]`)
- (`e6` cấp giấy phép mở chi nhánh `[NGHIA_VU_QUYEN]`) ==[ **TAC_DONG_DOI_TUONG** ]==> (`e13` văn bản chấp thuận `[GIAY_TO_HO_SO]`)


---

### Mẫu #13_2008_QĐ-NHNN_32111#body_standalone_96 (Loại: `body_standalone`)
> **[Điều 18]`<DIEU>`** . **[7 . Kết thúc thời hạn **[quy định tại]`<TU_KHOA_PHAP_LY>`** **[Khoản 6 Điều này]`<THAM_CHIEU_PHAP_LY>`** , **[ngân hàng thương mại]`<TO_CHUC_DOANH_NGHIEP>`** chưa được **[cơ quan có thẩm quyền]`<CO_QUAN_THAM_QUYEN>`** của nước sở tại **[cấp **[giấy phép mở chi nhánh]`<GIAY_TO_HO_SO>`**]`<NGHIA_VU_QUYEN>`** , **[văn phòng đại diện]`<TO_CHUC_DOANH_NGHIEP>`** , **[văn bản chấp thuận]`<GIAY_TO_HO_SO>`** của **[Ngân hàng Nhà nước]`<CO_QUAN_THAM_QUYEN>`** không còn giá trị .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 18** → `DIEU` (span: `[0:2]`)
- `[e1]` **7 . Kết thúc thời hạn quy định tại Khoản 6 Điều này , ngân hàng thương mại chưa được cơ quan có thẩm quyền của nước sở tại cấp giấy phép mở chi nhánh , văn phòng đại diện , văn bản chấp thuận của Ngân hàng Nhà nước không còn giá trị .** → `KHOAN` (span: `[3:41]`)
- `[e2]` **cấp giấy phép mở chi nhánh** → `NGHIA_VU_QUYEN` (span: `[24:28]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **ngân hàng thương mại** → `TO_CHUC_DOANH_NGHIEP` (span: `[14:16]`) *(lồng trong `e1` (`KHOAN`))*
- `[e4]` **văn phòng đại diện** → `TO_CHUC_DOANH_NGHIEP` (span: `[29:31]`) *(lồng trong `e1` (`KHOAN`))*
- `[e5]` **Khoản 6 Điều này** → `THAM_CHIEU_PHAP_LY` (span: `[9:13]`) *(lồng trong `e1` (`KHOAN`))*
- `[e6]` **quy định tại** → `TU_KHOA_PHAP_LY` (span: `[7:9]`) *(lồng trong `e1` (`KHOAN`))*
- `[e7]` **cơ quan có thẩm quyền** → `CO_QUAN_THAM_QUYEN` (span: `[18:21]`) *(lồng trong `e1` (`KHOAN`))*
- `[e8]` **Ngân hàng Nhà nước** → `CO_QUAN_THAM_QUYEN` (span: `[35:37]`) *(lồng trong `e1` (`KHOAN`))*
- `[e9]` **văn bản chấp thuận** → `GIAY_TO_HO_SO` (span: `[32:34]`) *(lồng trong `e1` (`KHOAN`))*
- `[e10]` **giấy phép mở chi nhánh** → `GIAY_TO_HO_SO` (span: `[25:28]`) *(lồng trong `e1` (`KHOAN`), `e2` (`NGHIA_VU_QUYEN`))*

**Quan hệ:**
- (`e1` 7 . Kết thúc thời hạn quy định tại Khoản 6 Điều này , ngân hàng thương mại chưa được cơ quan có thẩm quyền của nước sở tại cấp giấy phép mở chi nhánh , văn phòng đại diện , văn bản chấp thuận của Ngân hàng Nhà nước không còn giá trị . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 18 `[DIEU]`)
- (`e2` cấp giấy phép mở chi nhánh `[NGHIA_VU_QUYEN]`) ==[ **TAC_DONG_DOI_TUONG** ]==> (`e10` giấy phép mở chi nhánh `[GIAY_TO_HO_SO]`) *(Quan hệ lồng nhau)*
- (`e3` ngân hàng thương mại `[TO_CHUC_DOANH_NGHIEP]`) ==[ **CO_NGHIA_VU_QUYEN** ]==> (`e2` cấp giấy phép mở chi nhánh `[NGHIA_VU_QUYEN]`)
- (`e2` cấp giấy phép mở chi nhánh `[NGHIA_VU_QUYEN]`) ==[ **TAC_DONG_CHU_THE** ]==> (`e4` văn phòng đại diện `[TO_CHUC_DOANH_NGHIEP]`)
- (`e7` cơ quan có thẩm quyền `[CO_QUAN_THAM_QUYEN]`) ==[ **CO_THAM_QUYEN** ]==> (`e2` cấp giấy phép mở chi nhánh `[NGHIA_VU_QUYEN]`)
- (`e2` cấp giấy phép mở chi nhánh `[NGHIA_VU_QUYEN]`) ==[ **TAC_DONG_CHU_THE** ]==> (`e8` Ngân hàng Nhà nước `[CO_QUAN_THAM_QUYEN]`)
- (`e6` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e5` Khoản 6 Điều này `[THAM_CHIEU_PHAP_LY]`)
- (`e2` cấp giấy phép mở chi nhánh `[NGHIA_VU_QUYEN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e5` Khoản 6 Điều này `[THAM_CHIEU_PHAP_LY]`)
- (`e2` cấp giấy phép mở chi nhánh `[NGHIA_VU_QUYEN]`) ==[ **TAC_DONG_DOI_TUONG** ]==> (`e9` văn bản chấp thuận `[GIAY_TO_HO_SO]`)


---

### Mẫu #13_2008_QĐ-NHNN_32111#body_context_97 (Loại: `body_context`)
> **[Quyết định]`<LOAI_VAN_BAN>`** số **[13/2008/QĐ-NHNN]`<SO_HIEU>`** ban hành **[ngày 29 tháng 04 năm 2008]`<NGAY_BAN_HANH>`** bởi **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_BAN_HANH>`** . **[Chương II]`<CHUONG>`** . **[Điều 19 . Chấm dứt hoạt động chi nhánh , **[văn phòng đại diện]`<TO_CHUC_DOANH_NGHIEP>`** ở nước ngoài]`<DIEU>`**

**Thực thể:**
- `[e0]` **Quyết định** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **13/2008/QĐ-NHNN** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_BAN_HANH` (span: `[11:14]`)
- `[e3]` **ngày 29 tháng 04 năm 2008** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Chương II** → `CHUONG` (span: `[15:17]`)
- `[e5]` **Điều 19 . Chấm dứt hoạt động chi nhánh , văn phòng đại diện ở nước ngoài** → `DIEU` (span: `[18:29]`)
- `[e6]` **văn phòng đại diện** → `TO_CHUC_DOANH_NGHIEP` (span: `[25:27]`) *(lồng trong `e5` (`DIEU`))*

**Quan hệ:**
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Ngân hàng Nhà nước Việt Nam `[CO_QUAN_BAN_HANH]`)
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Quyết định `[LOAI_VAN_BAN]`)
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 29 tháng 04 năm 2008 `[NGAY_BAN_HANH]`)
- (`e4` Chương II `[CHUONG]`) ==[ **THUOC_VE** ]==> (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`)
- (`e5` Điều 19 . Chấm dứt hoạt động chi nhánh , văn phòng đại diện ở nước ngoài `[DIEU]`) ==[ **THUOC_VE** ]==> (`e4` Chương II `[CHUONG]`)


---

### Mẫu #13_2008_QĐ-NHNN_32111#body_context_98 (Loại: `body_context`)
> **[Quyết định]`<LOAI_VAN_BAN>`** số **[13/2008/QĐ-NHNN]`<SO_HIEU>`** của **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Ngân hàng]`<LINH_VUC>`** . **[Điều 20]`<DIEU>`** . **[2 . **[Ngân hàng thương mại]`<TO_CHUC_DOANH_NGHIEP>`** không phải điều chỉnh đối với số chi nhánh hiện đang hoạt động vượt quá số lượng chi nhánh **[quy định tại]`<TU_KHOA_PHAP_LY>`** **[Khoản 2 Điều 6]`<THAM_CHIEU_PHAP_LY>`** Quy định này .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Quyết định** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **13/2008/QĐ-NHNN** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_BAN_HANH` (span: `[4:7]`)
- `[e3]` **Ngân hàng** → `LINH_VUC` (span: `[9:10]`)
- `[e4]` **Điều 20** → `DIEU` (span: `[11:13]`)
- `[e5]` **2 . Ngân hàng thương mại không phải điều chỉnh đối với số chi nhánh hiện đang hoạt động vượt quá số lượng chi nhánh quy định tại Khoản 2 Điều 6 Quy định này .** → `KHOAN` (span: `[14:40]`)
- `[e6]` **Ngân hàng thương mại** → `TO_CHUC_DOANH_NGHIEP` (span: `[16:18]`) *(lồng trong `e5` (`KHOAN`))*
- `[e7]` **Khoản 2 Điều 6** → `THAM_CHIEU_PHAP_LY` (span: `[33:37]`) *(lồng trong `e5` (`KHOAN`))*
- `[e8]` **quy định tại** → `TU_KHOA_PHAP_LY` (span: `[31:33]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Ngân hàng Nhà nước Việt Nam `[CO_QUAN_BAN_HANH]`)
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Quyết định `[LOAI_VAN_BAN]`)
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Ngân hàng `[LINH_VUC]`)
- (`e4` Điều 20 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`)
- (`e5` 2 . Ngân hàng thương mại không phải điều chỉnh đối với số chi nhánh hiện đang hoạt động vượt quá số lượng chi nhánh quy định tại Khoản 2 Điều 6 Quy định này . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 20 `[DIEU]`)
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Ngân hàng `[LINH_VUC]`)
- (`e5` 2 . Ngân hàng thương mại không phải điều chỉnh đối với số chi nhánh hiện đang hoạt động vượt quá số lượng chi nhánh quy định tại Khoản 2 Điều 6 Quy định này . `[KHOAN]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Ngân hàng `[LINH_VUC]`)
- (`e8` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e7` Khoản 2 Điều 6 `[THAM_CHIEU_PHAP_LY]`)
- (`e5` 2 . Ngân hàng thương mại không phải điều chỉnh đối với số chi nhánh hiện đang hoạt động vượt quá số lượng chi nhánh quy định tại Khoản 2 Điều 6 Quy định này . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e7` Khoản 2 Điều 6 `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #13_2008_QĐ-NHNN_32111#body_standalone_99 (Loại: `body_standalone`)
> **[Điều 20]`<DIEU>`** . **[2 . **[Ngân hàng thương mại]`<TO_CHUC_DOANH_NGHIEP>`** không phải điều chỉnh đối với số chi nhánh hiện đang hoạt động vượt quá số lượng chi nhánh **[quy định tại]`<TU_KHOA_PHAP_LY>`** **[Khoản 2 Điều 6]`<THAM_CHIEU_PHAP_LY>`** Quy định này .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 20** → `DIEU` (span: `[0:2]`)
- `[e1]` **2 . Ngân hàng thương mại không phải điều chỉnh đối với số chi nhánh hiện đang hoạt động vượt quá số lượng chi nhánh quy định tại Khoản 2 Điều 6 Quy định này .** → `KHOAN` (span: `[3:29]`)
- `[e2]` **Ngân hàng thương mại** → `TO_CHUC_DOANH_NGHIEP` (span: `[5:7]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **Khoản 2 Điều 6** → `THAM_CHIEU_PHAP_LY` (span: `[22:26]`) *(lồng trong `e1` (`KHOAN`))*
- `[e4]` **quy định tại** → `TU_KHOA_PHAP_LY` (span: `[20:22]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 2 . Ngân hàng thương mại không phải điều chỉnh đối với số chi nhánh hiện đang hoạt động vượt quá số lượng chi nhánh quy định tại Khoản 2 Điều 6 Quy định này . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 20 `[DIEU]`)
- (`e4` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Khoản 2 Điều 6 `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 2 . Ngân hàng thương mại không phải điều chỉnh đối với số chi nhánh hiện đang hoạt động vượt quá số lượng chi nhánh quy định tại Khoản 2 Điều 6 Quy định này . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Khoản 2 Điều 6 `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #13_2008_QĐ-NHNN_32111#body_context_100 (Loại: `body_context`)
> **[Quyết định]`<LOAI_VAN_BAN>`** số **[13/2008/QĐ-NHNN]`<SO_HIEU>`** ban hành **[ngày 29 tháng 04 năm 2008]`<NGAY_BAN_HANH>`** bởi **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_BAN_HANH>`** . **[Điều 21]`<DIEU>`** . **[1 . **[Sở giao dịch]`<CO_QUAN_THAM_QUYEN>`** , chi nhánh , **[văn phòng đại diện]`<TO_CHUC_DOANH_NGHIEP>`** , **[đơn vị sự nghiệp]`<TO_CHUC_DOANH_NGHIEP>`** của **[ngân hàng thương mại]`<TO_CHUC_DOANH_NGHIEP>`** phải **[thực hiện chế độ báo cáo]`<NGHIA_VU_QUYEN>`** thống kê theo quy định của **[Ngân hàng Nhà nước]`<CO_QUAN_THAM_QUYEN>`** .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Quyết định** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **13/2008/QĐ-NHNN** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_BAN_HANH` (span: `[11:14]`)
- `[e3]` **ngày 29 tháng 04 năm 2008** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 21** → `DIEU` (span: `[15:17]`)
- `[e5]` **1 . Sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp của ngân hàng thương mại phải thực hiện chế độ báo cáo thống kê theo quy định của Ngân hàng Nhà nước .** → `KHOAN` (span: `[18:44]`)
- `[e6]` **thực hiện chế độ báo cáo** → `NGHIA_VU_QUYEN` (span: `[34:37]`) *(lồng trong `e5` (`KHOAN`))*
- `[e7]` **Sở giao dịch** → `CO_QUAN_THAM_QUYEN` (span: `[20:22]`) *(lồng trong `e5` (`KHOAN`))*
- `[e8]` **ngân hàng thương mại** → `TO_CHUC_DOANH_NGHIEP` (span: `[31:33]`) *(lồng trong `e5` (`KHOAN`))*
- `[e9]` **văn phòng đại diện** → `TO_CHUC_DOANH_NGHIEP` (span: `[25:27]`) *(lồng trong `e5` (`KHOAN`))*
- `[e10]` **đơn vị sự nghiệp** → `TO_CHUC_DOANH_NGHIEP` (span: `[28:30]`) *(lồng trong `e5` (`KHOAN`))*
- `[e11]` **Ngân hàng Nhà nước** → `CO_QUAN_THAM_QUYEN` (span: `[41:43]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Ngân hàng Nhà nước Việt Nam `[CO_QUAN_BAN_HANH]`)
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Quyết định `[LOAI_VAN_BAN]`)
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 29 tháng 04 năm 2008 `[NGAY_BAN_HANH]`)
- (`e4` Điều 21 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`)
- (`e5` 1 . Sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp của ngân hàng thương mại phải thực hiện chế độ báo cáo thống kê theo quy định của Ngân hàng Nhà nước . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 21 `[DIEU]`)
- (`e7` Sở giao dịch `[CO_QUAN_THAM_QUYEN]`) ==[ **CO_THAM_QUYEN** ]==> (`e6` thực hiện chế độ báo cáo `[NGHIA_VU_QUYEN]`)
- (`e8` ngân hàng thương mại `[TO_CHUC_DOANH_NGHIEP]`) ==[ **CO_NGHIA_VU_QUYEN** ]==> (`e6` thực hiện chế độ báo cáo `[NGHIA_VU_QUYEN]`)
- (`e9` văn phòng đại diện `[TO_CHUC_DOANH_NGHIEP]`) ==[ **CO_NGHIA_VU_QUYEN** ]==> (`e6` thực hiện chế độ báo cáo `[NGHIA_VU_QUYEN]`)
- (`e10` đơn vị sự nghiệp `[TO_CHUC_DOANH_NGHIEP]`) ==[ **CO_NGHIA_VU_QUYEN** ]==> (`e6` thực hiện chế độ báo cáo `[NGHIA_VU_QUYEN]`)
- (`e6` thực hiện chế độ báo cáo `[NGHIA_VU_QUYEN]`) ==[ **TAC_DONG_CHU_THE** ]==> (`e11` Ngân hàng Nhà nước `[CO_QUAN_THAM_QUYEN]`)


---

### Mẫu #13_2008_QĐ-NHNN_32111#body_standalone_101 (Loại: `body_standalone`)
> **[Điều 21]`<DIEU>`** . **[1 . **[Sở giao dịch]`<CO_QUAN_THAM_QUYEN>`** , chi nhánh , **[văn phòng đại diện]`<TO_CHUC_DOANH_NGHIEP>`** , **[đơn vị sự nghiệp]`<TO_CHUC_DOANH_NGHIEP>`** của **[ngân hàng thương mại]`<TO_CHUC_DOANH_NGHIEP>`** phải **[thực hiện chế độ báo cáo]`<NGHIA_VU_QUYEN>`** thống kê theo quy định của **[Ngân hàng Nhà nước]`<CO_QUAN_THAM_QUYEN>`** .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 21** → `DIEU` (span: `[0:2]`)
- `[e1]` **1 . Sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp của ngân hàng thương mại phải thực hiện chế độ báo cáo thống kê theo quy định của Ngân hàng Nhà nước .** → `KHOAN` (span: `[3:29]`)
- `[e2]` **thực hiện chế độ báo cáo** → `NGHIA_VU_QUYEN` (span: `[19:22]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **Sở giao dịch** → `CO_QUAN_THAM_QUYEN` (span: `[5:7]`) *(lồng trong `e1` (`KHOAN`))*
- `[e4]` **ngân hàng thương mại** → `TO_CHUC_DOANH_NGHIEP` (span: `[16:18]`) *(lồng trong `e1` (`KHOAN`))*
- `[e5]` **văn phòng đại diện** → `TO_CHUC_DOANH_NGHIEP` (span: `[10:12]`) *(lồng trong `e1` (`KHOAN`))*
- `[e6]` **đơn vị sự nghiệp** → `TO_CHUC_DOANH_NGHIEP` (span: `[13:15]`) *(lồng trong `e1` (`KHOAN`))*
- `[e7]` **Ngân hàng Nhà nước** → `CO_QUAN_THAM_QUYEN` (span: `[26:28]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 1 . Sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp của ngân hàng thương mại phải thực hiện chế độ báo cáo thống kê theo quy định của Ngân hàng Nhà nước . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 21 `[DIEU]`)
- (`e3` Sở giao dịch `[CO_QUAN_THAM_QUYEN]`) ==[ **CO_THAM_QUYEN** ]==> (`e2` thực hiện chế độ báo cáo `[NGHIA_VU_QUYEN]`)
- (`e4` ngân hàng thương mại `[TO_CHUC_DOANH_NGHIEP]`) ==[ **CO_NGHIA_VU_QUYEN** ]==> (`e2` thực hiện chế độ báo cáo `[NGHIA_VU_QUYEN]`)
- (`e5` văn phòng đại diện `[TO_CHUC_DOANH_NGHIEP]`) ==[ **CO_NGHIA_VU_QUYEN** ]==> (`e2` thực hiện chế độ báo cáo `[NGHIA_VU_QUYEN]`)
- (`e6` đơn vị sự nghiệp `[TO_CHUC_DOANH_NGHIEP]`) ==[ **CO_NGHIA_VU_QUYEN** ]==> (`e2` thực hiện chế độ báo cáo `[NGHIA_VU_QUYEN]`)
- (`e2` thực hiện chế độ báo cáo `[NGHIA_VU_QUYEN]`) ==[ **TAC_DONG_CHU_THE** ]==> (`e7` Ngân hàng Nhà nước `[CO_QUAN_THAM_QUYEN]`)


---

### Mẫu #13_2008_QĐ-NHNN_32111#body_context_102 (Loại: `body_context`)
> **[Quyết định]`<LOAI_VAN_BAN>`** số **[13/2008/QĐ-NHNN]`<SO_HIEU>`** của **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Ngân hàng]`<LINH_VUC>`** . **[Điều 21]`<DIEU>`** . **[2 . **[Sở giao dịch]`<CO_QUAN_THAM_QUYEN>`** , chi nhánh , **[văn phòng đại diện]`<TO_CHUC_DOANH_NGHIEP>`** , **[đơn vị sự nghiệp]`<TO_CHUC_DOANH_NGHIEP>`** của **[ngân hàng thương mại]`<TO_CHUC_DOANH_NGHIEP>`** có trách nhiệm báo cáo đột xuất theo yêu cầu của **[Ngân hàng Nhà nước]`<CO_QUAN_THAM_QUYEN>`** , **[Ngân hàng Nhà nước chi nhánh tỉnh , thành phố]`<CO_QUAN_THAM_QUYEN>`** nơi đặt **[sở giao dịch]`<CO_QUAN_THAM_QUYEN>`** , chi nhánh , **[văn phòng đại diện]`<TO_CHUC_DOANH_NGHIEP>`** , **[đơn vị sự nghiệp]`<TO_CHUC_DOANH_NGHIEP>`** .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Quyết định** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **13/2008/QĐ-NHNN** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_BAN_HANH` (span: `[4:7]`)
- `[e3]` **Ngân hàng** → `LINH_VUC` (span: `[9:10]`)
- `[e4]` **Điều 21** → `DIEU` (span: `[11:13]`)
- `[e5]` **2 . Sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp của ngân hàng thương mại có trách nhiệm báo cáo đột xuất theo yêu cầu của Ngân hàng Nhà nước , Ngân hàng Nhà nước chi nhánh tỉnh , thành phố nơi đặt sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp .** → `KHOAN` (span: `[14:58]`)
- `[e6]` **Sở giao dịch** → `CO_QUAN_THAM_QUYEN` (span: `[16:18]`) *(lồng trong `e5` (`KHOAN`))*
- `[e7]` **sở giao dịch** → `CO_QUAN_THAM_QUYEN` (span: `[47:49]`) *(lồng trong `e5` (`KHOAN`))*
- `[e8]` **ngân hàng thương mại** → `TO_CHUC_DOANH_NGHIEP` (span: `[27:29]`) *(lồng trong `e5` (`KHOAN`))*
- `[e9]` **văn phòng đại diện** → `TO_CHUC_DOANH_NGHIEP` (span: `[21:23]`) *(lồng trong `e5` (`KHOAN`))*
- `[e10]` **văn phòng đại diện** → `TO_CHUC_DOANH_NGHIEP` (span: `[52:54]`) *(lồng trong `e5` (`KHOAN`))*
- `[e11]` **đơn vị sự nghiệp** → `TO_CHUC_DOANH_NGHIEP` (span: `[24:26]`) *(lồng trong `e5` (`KHOAN`))*
- `[e12]` **đơn vị sự nghiệp** → `TO_CHUC_DOANH_NGHIEP` (span: `[55:57]`) *(lồng trong `e5` (`KHOAN`))*
- `[e13]` **Ngân hàng Nhà nước** → `CO_QUAN_THAM_QUYEN` (span: `[36:38]`) *(lồng trong `e5` (`KHOAN`))*
- `[e14]` **Ngân hàng Nhà nước chi nhánh tỉnh , thành phố** → `CO_QUAN_THAM_QUYEN` (span: `[39:45]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Ngân hàng Nhà nước Việt Nam `[CO_QUAN_BAN_HANH]`)
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Quyết định `[LOAI_VAN_BAN]`)
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Ngân hàng `[LINH_VUC]`)
- (`e4` Điều 21 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`)
- (`e5` 2 . Sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp của ngân hàng thương mại có trách nhiệm báo cáo đột xuất theo yêu cầu của Ngân hàng Nhà nước , Ngân hàng Nhà nước chi nhánh tỉnh , thành phố nơi đặt sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 21 `[DIEU]`)
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Ngân hàng `[LINH_VUC]`)
- (`e5` 2 . Sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp của ngân hàng thương mại có trách nhiệm báo cáo đột xuất theo yêu cầu của Ngân hàng Nhà nước , Ngân hàng Nhà nước chi nhánh tỉnh , thành phố nơi đặt sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp . `[KHOAN]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Ngân hàng `[LINH_VUC]`)


---

### Mẫu #13_2008_QĐ-NHNN_32111#body_standalone_103 (Loại: `body_standalone`)
> **[Điều 21]`<DIEU>`** . **[2 . **[Sở giao dịch]`<CO_QUAN_THAM_QUYEN>`** , chi nhánh , **[văn phòng đại diện]`<TO_CHUC_DOANH_NGHIEP>`** , **[đơn vị sự nghiệp]`<TO_CHUC_DOANH_NGHIEP>`** của **[ngân hàng thương mại]`<TO_CHUC_DOANH_NGHIEP>`** có trách nhiệm báo cáo đột xuất theo yêu cầu của **[Ngân hàng Nhà nước]`<CO_QUAN_THAM_QUYEN>`** , **[Ngân hàng Nhà nước chi nhánh tỉnh , thành phố]`<CO_QUAN_THAM_QUYEN>`** nơi đặt **[sở giao dịch]`<CO_QUAN_THAM_QUYEN>`** , chi nhánh , **[văn phòng đại diện]`<TO_CHUC_DOANH_NGHIEP>`** , **[đơn vị sự nghiệp]`<TO_CHUC_DOANH_NGHIEP>`** .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 21** → `DIEU` (span: `[0:2]`)
- `[e1]` **2 . Sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp của ngân hàng thương mại có trách nhiệm báo cáo đột xuất theo yêu cầu của Ngân hàng Nhà nước , Ngân hàng Nhà nước chi nhánh tỉnh , thành phố nơi đặt sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp .** → `KHOAN` (span: `[3:47]`)
- `[e2]` **Sở giao dịch** → `CO_QUAN_THAM_QUYEN` (span: `[5:7]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **sở giao dịch** → `CO_QUAN_THAM_QUYEN` (span: `[36:38]`) *(lồng trong `e1` (`KHOAN`))*
- `[e4]` **ngân hàng thương mại** → `TO_CHUC_DOANH_NGHIEP` (span: `[16:18]`) *(lồng trong `e1` (`KHOAN`))*
- `[e5]` **văn phòng đại diện** → `TO_CHUC_DOANH_NGHIEP` (span: `[10:12]`) *(lồng trong `e1` (`KHOAN`))*
- `[e6]` **văn phòng đại diện** → `TO_CHUC_DOANH_NGHIEP` (span: `[41:43]`) *(lồng trong `e1` (`KHOAN`))*
- `[e7]` **đơn vị sự nghiệp** → `TO_CHUC_DOANH_NGHIEP` (span: `[13:15]`) *(lồng trong `e1` (`KHOAN`))*
- `[e8]` **đơn vị sự nghiệp** → `TO_CHUC_DOANH_NGHIEP` (span: `[44:46]`) *(lồng trong `e1` (`KHOAN`))*
- `[e9]` **Ngân hàng Nhà nước** → `CO_QUAN_THAM_QUYEN` (span: `[25:27]`) *(lồng trong `e1` (`KHOAN`))*
- `[e10]` **Ngân hàng Nhà nước chi nhánh tỉnh , thành phố** → `CO_QUAN_THAM_QUYEN` (span: `[28:34]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 2 . Sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp của ngân hàng thương mại có trách nhiệm báo cáo đột xuất theo yêu cầu của Ngân hàng Nhà nước , Ngân hàng Nhà nước chi nhánh tỉnh , thành phố nơi đặt sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 21 `[DIEU]`)


---

### Mẫu #13_2008_QĐ-NHNN_32111#body_context_104 (Loại: `body_context`)
> **[Quyết định]`<LOAI_VAN_BAN>`** số **[13/2008/QĐ-NHNN]`<SO_HIEU>`** của **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Ngân hàng]`<LINH_VUC>`** . **[Điều 23]`<DIEU>`** . **[1 . Sau khi nhận được hồ sơ và báo cáo của **[Ngân hàng Nhà nước chi nhánh tỉnh , thành phố]`<CO_QUAN_THAM_QUYEN>`** nơi **[ngân hàng thương mại]`<TO_CHUC_DOANH_NGHIEP>`** đặt trụ sở chính về việc mở **[sở giao dịch]`<CO_QUAN_THAM_QUYEN>`** , chi nhánh , **[văn phòng đại diện]`<TO_CHUC_DOANH_NGHIEP>`** , **[đơn vị sự nghiệp]`<TO_CHUC_DOANH_NGHIEP>`** của **[ngân hàng thương mại]`<TO_CHUC_DOANH_NGHIEP>`** **[quy định tại]`<TU_KHOA_PHAP_LY>`** **[Điều 8 và Điều 18]`<THAM_CHIEU_PHAP_LY>`** Quy định này , Vụ Các ngân hàng và **[tổ chức tín dụng phi ngân hàng]`<TO_CHUC_DOANH_NGHIEP>`** gửi văn bản lấy ý kiến của **[Thanh tra Ngân hàng Nhà nước]`<CO_QUAN_THAM_QUYEN>`** , Vụ Chính sách tiền tệ ; tổng]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Quyết định** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **13/2008/QĐ-NHNN** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_BAN_HANH` (span: `[4:7]`)
- `[e3]` **Ngân hàng** → `LINH_VUC` (span: `[9:10]`)
- `[e4]` **Điều 23** → `DIEU` (span: `[11:13]`)
- `[e5]` **1 . Sau khi nhận được hồ sơ và báo cáo của Ngân hàng Nhà nước chi nhánh tỉnh , thành phố nơi ngân hàng thương mại đặt trụ sở chính về việc mở sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp của ngân hàng thương mại quy định tại Điều 8 và Điều 18 Quy định này , Vụ Các ngân hàng và tổ chức tín dụng phi ngân hàng gửi văn bản lấy ý kiến của Thanh tra Ngân hàng Nhà nước , Vụ Chính sách tiền tệ ; tổng** → `KHOAN` (span: `[14:84]`)
- `[e6]` **sở giao dịch** → `CO_QUAN_THAM_QUYEN` (span: `[39:41]`) *(lồng trong `e5` (`KHOAN`))*
- `[e7]` **ngân hàng thương mại** → `TO_CHUC_DOANH_NGHIEP` (span: `[31:33]`) *(lồng trong `e5` (`KHOAN`))*
- `[e8]` **ngân hàng thương mại** → `TO_CHUC_DOANH_NGHIEP` (span: `[50:52]`) *(lồng trong `e5` (`KHOAN`))*
- `[e9]` **văn phòng đại diện** → `TO_CHUC_DOANH_NGHIEP` (span: `[44:46]`) *(lồng trong `e5` (`KHOAN`))*
- `[e10]` **đơn vị sự nghiệp** → `TO_CHUC_DOANH_NGHIEP` (span: `[47:49]`) *(lồng trong `e5` (`KHOAN`))*
- `[e11]` **Điều 8 và Điều 18** → `THAM_CHIEU_PHAP_LY` (span: `[54:59]`) *(lồng trong `e5` (`KHOAN`))*
- `[e12]` **quy định tại** → `TU_KHOA_PHAP_LY` (span: `[52:54]`) *(lồng trong `e5` (`KHOAN`))*
- `[e13]` **Ngân hàng Nhà nước chi nhánh tỉnh , thành phố** → `CO_QUAN_THAM_QUYEN` (span: `[24:30]`) *(lồng trong `e5` (`KHOAN`))*
- `[e14]` **Thanh tra Ngân hàng Nhà nước** → `CO_QUAN_THAM_QUYEN` (span: `[75:78]`) *(lồng trong `e5` (`KHOAN`))*
- `[e15]` **tổ chức tín dụng phi ngân hàng** → `TO_CHUC_DOANH_NGHIEP` (span: `[66:70]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Ngân hàng Nhà nước Việt Nam `[CO_QUAN_BAN_HANH]`)
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Quyết định `[LOAI_VAN_BAN]`)
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Ngân hàng `[LINH_VUC]`)
- (`e4` Điều 23 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`)
- (`e5` 1 . Sau khi nhận được hồ sơ và báo cáo của Ngân hàng Nhà nước chi nhánh tỉnh , thành phố nơi ngân hàng thương mại đặt trụ sở chính về việc mở sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp của ngân hàng thương mại quy định tại Điều 8 và Điều 18 Quy định này , Vụ Các ngân hàng và tổ chức tín dụng phi ngân hàng gửi văn bản lấy ý kiến của Thanh tra Ngân hàng Nhà nước , Vụ Chính sách tiền tệ ; tổng `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 23 `[DIEU]`)
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Ngân hàng `[LINH_VUC]`)
- (`e5` 1 . Sau khi nhận được hồ sơ và báo cáo của Ngân hàng Nhà nước chi nhánh tỉnh , thành phố nơi ngân hàng thương mại đặt trụ sở chính về việc mở sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp của ngân hàng thương mại quy định tại Điều 8 và Điều 18 Quy định này , Vụ Các ngân hàng và tổ chức tín dụng phi ngân hàng gửi văn bản lấy ý kiến của Thanh tra Ngân hàng Nhà nước , Vụ Chính sách tiền tệ ; tổng `[KHOAN]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Ngân hàng `[LINH_VUC]`)
- (`e12` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e11` Điều 8 và Điều 18 `[THAM_CHIEU_PHAP_LY]`)
- (`e5` 1 . Sau khi nhận được hồ sơ và báo cáo của Ngân hàng Nhà nước chi nhánh tỉnh , thành phố nơi ngân hàng thương mại đặt trụ sở chính về việc mở sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp của ngân hàng thương mại quy định tại Điều 8 và Điều 18 Quy định này , Vụ Các ngân hàng và tổ chức tín dụng phi ngân hàng gửi văn bản lấy ý kiến của Thanh tra Ngân hàng Nhà nước , Vụ Chính sách tiền tệ ; tổng `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e11` Điều 8 và Điều 18 `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #13_2008_QĐ-NHNN_32111#body_standalone_105 (Loại: `body_standalone`)
> **[Điều 23]`<DIEU>`** . **[1 . Sau khi nhận được hồ sơ và báo cáo của **[Ngân hàng Nhà nước chi nhánh tỉnh , thành phố]`<CO_QUAN_THAM_QUYEN>`** nơi **[ngân hàng thương mại]`<TO_CHUC_DOANH_NGHIEP>`** đặt trụ sở chính về việc mở **[sở giao dịch]`<CO_QUAN_THAM_QUYEN>`** , chi nhánh , **[văn phòng đại diện]`<TO_CHUC_DOANH_NGHIEP>`** , **[đơn vị sự nghiệp]`<TO_CHUC_DOANH_NGHIEP>`** của **[ngân hàng thương mại]`<TO_CHUC_DOANH_NGHIEP>`** **[quy định tại]`<TU_KHOA_PHAP_LY>`** **[Điều 8 và Điều 18]`<THAM_CHIEU_PHAP_LY>`** Quy định này , Vụ Các ngân hàng và **[tổ chức tín dụng phi ngân hàng]`<TO_CHUC_DOANH_NGHIEP>`** gửi văn bản lấy ý kiến của **[Thanh tra Ngân hàng Nhà nước]`<CO_QUAN_THAM_QUYEN>`** , Vụ Chính sách tiền tệ ; tổng]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 23** → `DIEU` (span: `[0:2]`)
- `[e1]` **1 . Sau khi nhận được hồ sơ và báo cáo của Ngân hàng Nhà nước chi nhánh tỉnh , thành phố nơi ngân hàng thương mại đặt trụ sở chính về việc mở sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp của ngân hàng thương mại quy định tại Điều 8 và Điều 18 Quy định này , Vụ Các ngân hàng và tổ chức tín dụng phi ngân hàng gửi văn bản lấy ý kiến của Thanh tra Ngân hàng Nhà nước , Vụ Chính sách tiền tệ ; tổng** → `KHOAN` (span: `[3:73]`)
- `[e2]` **sở giao dịch** → `CO_QUAN_THAM_QUYEN` (span: `[28:30]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **ngân hàng thương mại** → `TO_CHUC_DOANH_NGHIEP` (span: `[20:22]`) *(lồng trong `e1` (`KHOAN`))*
- `[e4]` **ngân hàng thương mại** → `TO_CHUC_DOANH_NGHIEP` (span: `[39:41]`) *(lồng trong `e1` (`KHOAN`))*
- `[e5]` **văn phòng đại diện** → `TO_CHUC_DOANH_NGHIEP` (span: `[33:35]`) *(lồng trong `e1` (`KHOAN`))*
- `[e6]` **đơn vị sự nghiệp** → `TO_CHUC_DOANH_NGHIEP` (span: `[36:38]`) *(lồng trong `e1` (`KHOAN`))*
- `[e7]` **Điều 8 và Điều 18** → `THAM_CHIEU_PHAP_LY` (span: `[43:48]`) *(lồng trong `e1` (`KHOAN`))*
- `[e8]` **quy định tại** → `TU_KHOA_PHAP_LY` (span: `[41:43]`) *(lồng trong `e1` (`KHOAN`))*
- `[e9]` **Ngân hàng Nhà nước chi nhánh tỉnh , thành phố** → `CO_QUAN_THAM_QUYEN` (span: `[13:19]`) *(lồng trong `e1` (`KHOAN`))*
- `[e10]` **Thanh tra Ngân hàng Nhà nước** → `CO_QUAN_THAM_QUYEN` (span: `[64:67]`) *(lồng trong `e1` (`KHOAN`))*
- `[e11]` **tổ chức tín dụng phi ngân hàng** → `TO_CHUC_DOANH_NGHIEP` (span: `[55:59]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 1 . Sau khi nhận được hồ sơ và báo cáo của Ngân hàng Nhà nước chi nhánh tỉnh , thành phố nơi ngân hàng thương mại đặt trụ sở chính về việc mở sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp của ngân hàng thương mại quy định tại Điều 8 và Điều 18 Quy định này , Vụ Các ngân hàng và tổ chức tín dụng phi ngân hàng gửi văn bản lấy ý kiến của Thanh tra Ngân hàng Nhà nước , Vụ Chính sách tiền tệ ; tổng `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 23 `[DIEU]`)
- (`e8` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e7` Điều 8 và Điều 18 `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 1 . Sau khi nhận được hồ sơ và báo cáo của Ngân hàng Nhà nước chi nhánh tỉnh , thành phố nơi ngân hàng thương mại đặt trụ sở chính về việc mở sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp của ngân hàng thương mại quy định tại Điều 8 và Điều 18 Quy định này , Vụ Các ngân hàng và tổ chức tín dụng phi ngân hàng gửi văn bản lấy ý kiến của Thanh tra Ngân hàng Nhà nước , Vụ Chính sách tiền tệ ; tổng `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e7` Điều 8 và Điều 18 `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #13_2008_QĐ-NHNN_32111#body_context_106 (Loại: `body_context`)
> **[Quyết định]`<LOAI_VAN_BAN>`** số **[13/2008/QĐ-NHNN]`<SO_HIEU>`** ban hành **[ngày 29 tháng 04 năm 2008]`<NGAY_BAN_HANH>`** bởi **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_BAN_HANH>`** . **[Điều 23]`<DIEU>`** . **[2 . Sau khi nhận đủ **[hồ sơ đề nghị]`<GIAY_TO_HO_SO>`** chấm dứt hoạt động **[sở giao dịch]`<CO_QUAN_THAM_QUYEN>`** , chi nhánh , **[văn phòng đại diện]`<TO_CHUC_DOANH_NGHIEP>`** , **[đơn vị sự nghiệp]`<TO_CHUC_DOANH_NGHIEP>`** của **[ngân hàng thương mại]`<TO_CHUC_DOANH_NGHIEP>`** **[quy định tại]`<TU_KHOA_PHAP_LY>`** **[Khoản 1 Điều 13]`<THAM_CHIEU_PHAP_LY>`** hoặc căn cứ các trường hợp **[quy định tại]`<TU_KHOA_PHAP_LY>`** **[Khoản 1 Điều 14]`<THAM_CHIEU_PHAP_LY>`** Quy định này , Vụ Các ngân hàng và **[tổ chức tín dụng phi ngân hàng]`<TO_CHUC_DOANH_NGHIEP>`** gửi văn bản lấy ý kiến của **[Thanh tra Ngân hàng Nhà nước]`<CO_QUAN_THAM_QUYEN>`** , **[Ngân hàng Nhà nước chi nhánh tỉnh , thành phố]`<CO_QUAN_THAM_QUYEN>`** nơi ngân hàng thương]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Quyết định** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **13/2008/QĐ-NHNN** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_BAN_HANH` (span: `[11:14]`)
- `[e3]` **ngày 29 tháng 04 năm 2008** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 23** → `DIEU` (span: `[15:17]`)
- `[e5]` **2 . Sau khi nhận đủ hồ sơ đề nghị chấm dứt hoạt động sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp của ngân hàng thương mại quy định tại Khoản 1 Điều 13 hoặc căn cứ các trường hợp quy định tại Khoản 1 Điều 14 Quy định này , Vụ Các ngân hàng và tổ chức tín dụng phi ngân hàng gửi văn bản lấy ý kiến của Thanh tra Ngân hàng Nhà nước , Ngân hàng Nhà nước chi nhánh tỉnh , thành phố nơi ngân hàng thương** → `KHOAN` (span: `[18:86]`)
- `[e6]` **sở giao dịch** → `CO_QUAN_THAM_QUYEN` (span: `[28:30]`) *(lồng trong `e5` (`KHOAN`))*
- `[e7]` **ngân hàng thương mại** → `TO_CHUC_DOANH_NGHIEP` (span: `[39:41]`) *(lồng trong `e5` (`KHOAN`))*
- `[e8]` **văn phòng đại diện** → `TO_CHUC_DOANH_NGHIEP` (span: `[33:35]`) *(lồng trong `e5` (`KHOAN`))*
- `[e9]` **đơn vị sự nghiệp** → `TO_CHUC_DOANH_NGHIEP` (span: `[36:38]`) *(lồng trong `e5` (`KHOAN`))*
- `[e10]` **Khoản 1 Điều 13** → `THAM_CHIEU_PHAP_LY` (span: `[43:47]`) *(lồng trong `e5` (`KHOAN`))*
- `[e11]` **Khoản 1 Điều 14** → `THAM_CHIEU_PHAP_LY` (span: `[53:57]`) *(lồng trong `e5` (`KHOAN`))*
- `[e12]` **quy định tại** → `TU_KHOA_PHAP_LY` (span: `[41:43]`) *(lồng trong `e5` (`KHOAN`))*
- `[e13]` **quy định tại** → `TU_KHOA_PHAP_LY` (span: `[51:53]`) *(lồng trong `e5` (`KHOAN`))*
- `[e14]` **Thanh tra Ngân hàng Nhà nước** → `CO_QUAN_THAM_QUYEN` (span: `[73:76]`) *(lồng trong `e5` (`KHOAN`))*
- `[e15]` **Ngân hàng Nhà nước chi nhánh tỉnh , thành phố** → `CO_QUAN_THAM_QUYEN` (span: `[77:83]`) *(lồng trong `e5` (`KHOAN`))*
- `[e16]` **hồ sơ đề nghị** → `GIAY_TO_HO_SO` (span: `[24:26]`) *(lồng trong `e5` (`KHOAN`))*
- `[e17]` **tổ chức tín dụng phi ngân hàng** → `TO_CHUC_DOANH_NGHIEP` (span: `[64:68]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Ngân hàng Nhà nước Việt Nam `[CO_QUAN_BAN_HANH]`)
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Quyết định `[LOAI_VAN_BAN]`)
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 29 tháng 04 năm 2008 `[NGAY_BAN_HANH]`)
- (`e4` Điều 23 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`)
- (`e5` 2 . Sau khi nhận đủ hồ sơ đề nghị chấm dứt hoạt động sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp của ngân hàng thương mại quy định tại Khoản 1 Điều 13 hoặc căn cứ các trường hợp quy định tại Khoản 1 Điều 14 Quy định này , Vụ Các ngân hàng và tổ chức tín dụng phi ngân hàng gửi văn bản lấy ý kiến của Thanh tra Ngân hàng Nhà nước , Ngân hàng Nhà nước chi nhánh tỉnh , thành phố nơi ngân hàng thương `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 23 `[DIEU]`)
- (`e12` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e10` Khoản 1 Điều 13 `[THAM_CHIEU_PHAP_LY]`)
- (`e5` 2 . Sau khi nhận đủ hồ sơ đề nghị chấm dứt hoạt động sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp của ngân hàng thương mại quy định tại Khoản 1 Điều 13 hoặc căn cứ các trường hợp quy định tại Khoản 1 Điều 14 Quy định này , Vụ Các ngân hàng và tổ chức tín dụng phi ngân hàng gửi văn bản lấy ý kiến của Thanh tra Ngân hàng Nhà nước , Ngân hàng Nhà nước chi nhánh tỉnh , thành phố nơi ngân hàng thương `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e10` Khoản 1 Điều 13 `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e13` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e11` Khoản 1 Điều 14 `[THAM_CHIEU_PHAP_LY]`)
- (`e5` 2 . Sau khi nhận đủ hồ sơ đề nghị chấm dứt hoạt động sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp của ngân hàng thương mại quy định tại Khoản 1 Điều 13 hoặc căn cứ các trường hợp quy định tại Khoản 1 Điều 14 Quy định này , Vụ Các ngân hàng và tổ chức tín dụng phi ngân hàng gửi văn bản lấy ý kiến của Thanh tra Ngân hàng Nhà nước , Ngân hàng Nhà nước chi nhánh tỉnh , thành phố nơi ngân hàng thương `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e11` Khoản 1 Điều 14 `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #13_2008_QĐ-NHNN_32111#body_standalone_107 (Loại: `body_standalone`)
> **[Điều 23]`<DIEU>`** . **[2 . Sau khi nhận đủ **[hồ sơ đề nghị]`<GIAY_TO_HO_SO>`** chấm dứt hoạt động **[sở giao dịch]`<CO_QUAN_THAM_QUYEN>`** , chi nhánh , **[văn phòng đại diện]`<TO_CHUC_DOANH_NGHIEP>`** , **[đơn vị sự nghiệp]`<TO_CHUC_DOANH_NGHIEP>`** của **[ngân hàng thương mại]`<TO_CHUC_DOANH_NGHIEP>`** **[quy định tại]`<TU_KHOA_PHAP_LY>`** **[Khoản 1 Điều 13]`<THAM_CHIEU_PHAP_LY>`** hoặc căn cứ các trường hợp **[quy định tại]`<TU_KHOA_PHAP_LY>`** **[Khoản 1 Điều 14]`<THAM_CHIEU_PHAP_LY>`** Quy định này , Vụ Các ngân hàng và **[tổ chức tín dụng phi ngân hàng]`<TO_CHUC_DOANH_NGHIEP>`** gửi văn bản lấy ý kiến của **[Thanh tra Ngân hàng Nhà nước]`<CO_QUAN_THAM_QUYEN>`** , **[Ngân hàng Nhà nước chi nhánh tỉnh , thành phố]`<CO_QUAN_THAM_QUYEN>`** nơi ngân hàng thương]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 23** → `DIEU` (span: `[0:2]`)
- `[e1]` **2 . Sau khi nhận đủ hồ sơ đề nghị chấm dứt hoạt động sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp của ngân hàng thương mại quy định tại Khoản 1 Điều 13 hoặc căn cứ các trường hợp quy định tại Khoản 1 Điều 14 Quy định này , Vụ Các ngân hàng và tổ chức tín dụng phi ngân hàng gửi văn bản lấy ý kiến của Thanh tra Ngân hàng Nhà nước , Ngân hàng Nhà nước chi nhánh tỉnh , thành phố nơi ngân hàng thương** → `KHOAN` (span: `[3:71]`)
- `[e2]` **sở giao dịch** → `CO_QUAN_THAM_QUYEN` (span: `[13:15]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **ngân hàng thương mại** → `TO_CHUC_DOANH_NGHIEP` (span: `[24:26]`) *(lồng trong `e1` (`KHOAN`))*
- `[e4]` **văn phòng đại diện** → `TO_CHUC_DOANH_NGHIEP` (span: `[18:20]`) *(lồng trong `e1` (`KHOAN`))*
- `[e5]` **đơn vị sự nghiệp** → `TO_CHUC_DOANH_NGHIEP` (span: `[21:23]`) *(lồng trong `e1` (`KHOAN`))*
- `[e6]` **Khoản 1 Điều 13** → `THAM_CHIEU_PHAP_LY` (span: `[28:32]`) *(lồng trong `e1` (`KHOAN`))*
- `[e7]` **Khoản 1 Điều 14** → `THAM_CHIEU_PHAP_LY` (span: `[38:42]`) *(lồng trong `e1` (`KHOAN`))*
- `[e8]` **quy định tại** → `TU_KHOA_PHAP_LY` (span: `[26:28]`) *(lồng trong `e1` (`KHOAN`))*
- `[e9]` **quy định tại** → `TU_KHOA_PHAP_LY` (span: `[36:38]`) *(lồng trong `e1` (`KHOAN`))*
- `[e10]` **Thanh tra Ngân hàng Nhà nước** → `CO_QUAN_THAM_QUYEN` (span: `[58:61]`) *(lồng trong `e1` (`KHOAN`))*
- `[e11]` **Ngân hàng Nhà nước chi nhánh tỉnh , thành phố** → `CO_QUAN_THAM_QUYEN` (span: `[62:68]`) *(lồng trong `e1` (`KHOAN`))*
- `[e12]` **hồ sơ đề nghị** → `GIAY_TO_HO_SO` (span: `[9:11]`) *(lồng trong `e1` (`KHOAN`))*
- `[e13]` **tổ chức tín dụng phi ngân hàng** → `TO_CHUC_DOANH_NGHIEP` (span: `[49:53]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 2 . Sau khi nhận đủ hồ sơ đề nghị chấm dứt hoạt động sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp của ngân hàng thương mại quy định tại Khoản 1 Điều 13 hoặc căn cứ các trường hợp quy định tại Khoản 1 Điều 14 Quy định này , Vụ Các ngân hàng và tổ chức tín dụng phi ngân hàng gửi văn bản lấy ý kiến của Thanh tra Ngân hàng Nhà nước , Ngân hàng Nhà nước chi nhánh tỉnh , thành phố nơi ngân hàng thương `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 23 `[DIEU]`)
- (`e8` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e6` Khoản 1 Điều 13 `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 2 . Sau khi nhận đủ hồ sơ đề nghị chấm dứt hoạt động sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp của ngân hàng thương mại quy định tại Khoản 1 Điều 13 hoặc căn cứ các trường hợp quy định tại Khoản 1 Điều 14 Quy định này , Vụ Các ngân hàng và tổ chức tín dụng phi ngân hàng gửi văn bản lấy ý kiến của Thanh tra Ngân hàng Nhà nước , Ngân hàng Nhà nước chi nhánh tỉnh , thành phố nơi ngân hàng thương `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e6` Khoản 1 Điều 13 `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e9` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e7` Khoản 1 Điều 14 `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 2 . Sau khi nhận đủ hồ sơ đề nghị chấm dứt hoạt động sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp của ngân hàng thương mại quy định tại Khoản 1 Điều 13 hoặc căn cứ các trường hợp quy định tại Khoản 1 Điều 14 Quy định này , Vụ Các ngân hàng và tổ chức tín dụng phi ngân hàng gửi văn bản lấy ý kiến của Thanh tra Ngân hàng Nhà nước , Ngân hàng Nhà nước chi nhánh tỉnh , thành phố nơi ngân hàng thương `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e7` Khoản 1 Điều 14 `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #13_2008_QĐ-NHNN_32111#body_context_108 (Loại: `body_context`)
> **[Quyết định]`<LOAI_VAN_BAN>`** số **[13/2008/QĐ-NHNN]`<SO_HIEU>`** ban hành **[ngày 29 tháng 04 năm 2008]`<NGAY_BAN_HANH>`** bởi **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_BAN_HANH>`** . **[Chương III]`<CHUONG>`** . **[Điều 25 . Trách nhiệm của Vụ Chính sách tiền tệ]`<DIEU>`**

**Thực thể:**
- `[e0]` **Quyết định** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **13/2008/QĐ-NHNN** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_BAN_HANH` (span: `[11:14]`)
- `[e3]` **ngày 29 tháng 04 năm 2008** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Chương III** → `CHUONG` (span: `[15:17]`)
- `[e5]` **Điều 25 . Trách nhiệm của Vụ Chính sách tiền tệ** → `DIEU` (span: `[18:26]`)

**Quan hệ:**
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Ngân hàng Nhà nước Việt Nam `[CO_QUAN_BAN_HANH]`)
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Quyết định `[LOAI_VAN_BAN]`)
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 29 tháng 04 năm 2008 `[NGAY_BAN_HANH]`)
- (`e4` Chương III `[CHUONG]`) ==[ **THUOC_VE** ]==> (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`)
- (`e5` Điều 25 . Trách nhiệm của Vụ Chính sách tiền tệ `[DIEU]`) ==[ **THUOC_VE** ]==> (`e4` Chương III `[CHUONG]`)


---

### Mẫu #13_2008_QĐ-NHNN_32111#body_context_109 (Loại: `body_context`)
> **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_BAN_HANH>`** ban hành **[Quyết định]`<LOAI_VAN_BAN>`** số **[13/2008/QĐ-NHNN]`<SO_HIEU>`** . **[Điều 26]`<DIEU>`** . **[1 . Sau khi nhận đủ hồ sơ **[quy định tại]`<TU_KHOA_PHAP_LY>`** **[Khoản 1 Điều 8]`<THAM_CHIEU_PHAP_LY>`** hoặc **[Khoản 1 Điều 18]`<THAM_CHIEU_PHAP_LY>`** Quy định này , **[Ngân hàng Nhà nước chi nhánh tỉnh , thành phố]`<CO_QUAN_THAM_QUYEN>`** nơi **[ngân hàng thương mại]`<TO_CHUC_DOANH_NGHIEP>`** đặt trụ sở chính có trách nhiệm đánh giá việc **[ngân hàng thương mại]`<TO_CHUC_DOANH_NGHIEP>`** đáp ứng các điều kiện mở **[sở giao dịch]`<CO_QUAN_THAM_QUYEN>`** , chi nhánh , **[văn phòng đại diện]`<TO_CHUC_DOANH_NGHIEP>`** , **[đơn vị sự nghiệp]`<TO_CHUC_DOANH_NGHIEP>`** và có ý kiến đồng ý hoặc không đồng ý ; trường hợp không đồng ý , nêu rõ lý do .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Quyết định** → `LOAI_VAN_BAN` (span: `[4:5]`)
- `[e1]` **13/2008/QĐ-NHNN** → `SO_HIEU` (span: `[6:7]`)
- `[e2]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_BAN_HANH` (span: `[0:3]`)
- `[e3]` **Điều 26** → `DIEU` (span: `[8:10]`)
- `[e4]` **1 . Sau khi nhận đủ hồ sơ quy định tại Khoản 1 Điều 8 hoặc Khoản 1 Điều 18 Quy định này , Ngân hàng Nhà nước chi nhánh tỉnh , thành phố nơi ngân hàng thương mại đặt trụ sở chính có trách nhiệm đánh giá việc ngân hàng thương mại đáp ứng các điều kiện mở sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp và có ý kiến đồng ý hoặc không đồng ý ; trường hợp không đồng ý , nêu rõ lý do .** → `KHOAN` (span: `[11:80]`)
- `[e5]` **sở giao dịch** → `CO_QUAN_THAM_QUYEN` (span: `[54:56]`) *(lồng trong `e4` (`KHOAN`))*
- `[e6]` **ngân hàng thương mại** → `TO_CHUC_DOANH_NGHIEP` (span: `[39:41]`) *(lồng trong `e4` (`KHOAN`))*
- `[e7]` **ngân hàng thương mại** → `TO_CHUC_DOANH_NGHIEP` (span: `[48:50]`) *(lồng trong `e4` (`KHOAN`))*
- `[e8]` **văn phòng đại diện** → `TO_CHUC_DOANH_NGHIEP` (span: `[59:61]`) *(lồng trong `e4` (`KHOAN`))*
- `[e9]` **đơn vị sự nghiệp** → `TO_CHUC_DOANH_NGHIEP` (span: `[62:64]`) *(lồng trong `e4` (`KHOAN`))*
- `[e10]` **Khoản 1 Điều 8** → `THAM_CHIEU_PHAP_LY` (span: `[20:24]`) *(lồng trong `e4` (`KHOAN`))*
- `[e11]` **Khoản 1 Điều 18** → `THAM_CHIEU_PHAP_LY` (span: `[25:29]`) *(lồng trong `e4` (`KHOAN`))*
- `[e12]` **quy định tại** → `TU_KHOA_PHAP_LY` (span: `[18:20]`) *(lồng trong `e4` (`KHOAN`))*
- `[e13]` **Ngân hàng Nhà nước chi nhánh tỉnh , thành phố** → `CO_QUAN_THAM_QUYEN` (span: `[32:38]`) *(lồng trong `e4` (`KHOAN`))*

**Quan hệ:**
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Ngân hàng Nhà nước Việt Nam `[CO_QUAN_BAN_HANH]`)
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Quyết định `[LOAI_VAN_BAN]`)
- (`e3` Điều 26 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`)
- (`e4` 1 . Sau khi nhận đủ hồ sơ quy định tại Khoản 1 Điều 8 hoặc Khoản 1 Điều 18 Quy định này , Ngân hàng Nhà nước chi nhánh tỉnh , thành phố nơi ngân hàng thương mại đặt trụ sở chính có trách nhiệm đánh giá việc ngân hàng thương mại đáp ứng các điều kiện mở sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp và có ý kiến đồng ý hoặc không đồng ý ; trường hợp không đồng ý , nêu rõ lý do . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 26 `[DIEU]`)
- (`e12` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e10` Khoản 1 Điều 8 `[THAM_CHIEU_PHAP_LY]`)
- (`e4` 1 . Sau khi nhận đủ hồ sơ quy định tại Khoản 1 Điều 8 hoặc Khoản 1 Điều 18 Quy định này , Ngân hàng Nhà nước chi nhánh tỉnh , thành phố nơi ngân hàng thương mại đặt trụ sở chính có trách nhiệm đánh giá việc ngân hàng thương mại đáp ứng các điều kiện mở sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp và có ý kiến đồng ý hoặc không đồng ý ; trường hợp không đồng ý , nêu rõ lý do . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e10` Khoản 1 Điều 8 `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e12` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e11` Khoản 1 Điều 18 `[THAM_CHIEU_PHAP_LY]`)
- (`e4` 1 . Sau khi nhận đủ hồ sơ quy định tại Khoản 1 Điều 8 hoặc Khoản 1 Điều 18 Quy định này , Ngân hàng Nhà nước chi nhánh tỉnh , thành phố nơi ngân hàng thương mại đặt trụ sở chính có trách nhiệm đánh giá việc ngân hàng thương mại đáp ứng các điều kiện mở sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp và có ý kiến đồng ý hoặc không đồng ý ; trường hợp không đồng ý , nêu rõ lý do . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e11` Khoản 1 Điều 18 `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #13_2008_QĐ-NHNN_32111#body_standalone_110 (Loại: `body_standalone`)
> **[Điều 26]`<DIEU>`** . **[1 . Sau khi nhận đủ hồ sơ **[quy định tại]`<TU_KHOA_PHAP_LY>`** **[Khoản 1 Điều 8]`<THAM_CHIEU_PHAP_LY>`** hoặc **[Khoản 1 Điều 18]`<THAM_CHIEU_PHAP_LY>`** Quy định này , **[Ngân hàng Nhà nước chi nhánh tỉnh , thành phố]`<CO_QUAN_THAM_QUYEN>`** nơi **[ngân hàng thương mại]`<TO_CHUC_DOANH_NGHIEP>`** đặt trụ sở chính có trách nhiệm đánh giá việc **[ngân hàng thương mại]`<TO_CHUC_DOANH_NGHIEP>`** đáp ứng các điều kiện mở **[sở giao dịch]`<CO_QUAN_THAM_QUYEN>`** , chi nhánh , **[văn phòng đại diện]`<TO_CHUC_DOANH_NGHIEP>`** , **[đơn vị sự nghiệp]`<TO_CHUC_DOANH_NGHIEP>`** và có ý kiến đồng ý hoặc không đồng ý ; trường hợp không đồng ý , nêu rõ lý do .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 26** → `DIEU` (span: `[0:2]`)
- `[e1]` **1 . Sau khi nhận đủ hồ sơ quy định tại Khoản 1 Điều 8 hoặc Khoản 1 Điều 18 Quy định này , Ngân hàng Nhà nước chi nhánh tỉnh , thành phố nơi ngân hàng thương mại đặt trụ sở chính có trách nhiệm đánh giá việc ngân hàng thương mại đáp ứng các điều kiện mở sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp và có ý kiến đồng ý hoặc không đồng ý ; trường hợp không đồng ý , nêu rõ lý do .** → `KHOAN` (span: `[3:72]`)
- `[e2]` **sở giao dịch** → `CO_QUAN_THAM_QUYEN` (span: `[46:48]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **ngân hàng thương mại** → `TO_CHUC_DOANH_NGHIEP` (span: `[31:33]`) *(lồng trong `e1` (`KHOAN`))*
- `[e4]` **ngân hàng thương mại** → `TO_CHUC_DOANH_NGHIEP` (span: `[40:42]`) *(lồng trong `e1` (`KHOAN`))*
- `[e5]` **văn phòng đại diện** → `TO_CHUC_DOANH_NGHIEP` (span: `[51:53]`) *(lồng trong `e1` (`KHOAN`))*
- `[e6]` **đơn vị sự nghiệp** → `TO_CHUC_DOANH_NGHIEP` (span: `[54:56]`) *(lồng trong `e1` (`KHOAN`))*
- `[e7]` **Khoản 1 Điều 8** → `THAM_CHIEU_PHAP_LY` (span: `[12:16]`) *(lồng trong `e1` (`KHOAN`))*
- `[e8]` **Khoản 1 Điều 18** → `THAM_CHIEU_PHAP_LY` (span: `[17:21]`) *(lồng trong `e1` (`KHOAN`))*
- `[e9]` **quy định tại** → `TU_KHOA_PHAP_LY` (span: `[10:12]`) *(lồng trong `e1` (`KHOAN`))*
- `[e10]` **Ngân hàng Nhà nước chi nhánh tỉnh , thành phố** → `CO_QUAN_THAM_QUYEN` (span: `[24:30]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 1 . Sau khi nhận đủ hồ sơ quy định tại Khoản 1 Điều 8 hoặc Khoản 1 Điều 18 Quy định này , Ngân hàng Nhà nước chi nhánh tỉnh , thành phố nơi ngân hàng thương mại đặt trụ sở chính có trách nhiệm đánh giá việc ngân hàng thương mại đáp ứng các điều kiện mở sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp và có ý kiến đồng ý hoặc không đồng ý ; trường hợp không đồng ý , nêu rõ lý do . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 26 `[DIEU]`)
- (`e9` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e7` Khoản 1 Điều 8 `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 1 . Sau khi nhận đủ hồ sơ quy định tại Khoản 1 Điều 8 hoặc Khoản 1 Điều 18 Quy định này , Ngân hàng Nhà nước chi nhánh tỉnh , thành phố nơi ngân hàng thương mại đặt trụ sở chính có trách nhiệm đánh giá việc ngân hàng thương mại đáp ứng các điều kiện mở sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp và có ý kiến đồng ý hoặc không đồng ý ; trường hợp không đồng ý , nêu rõ lý do . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e7` Khoản 1 Điều 8 `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e9` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e8` Khoản 1 Điều 18 `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 1 . Sau khi nhận đủ hồ sơ quy định tại Khoản 1 Điều 8 hoặc Khoản 1 Điều 18 Quy định này , Ngân hàng Nhà nước chi nhánh tỉnh , thành phố nơi ngân hàng thương mại đặt trụ sở chính có trách nhiệm đánh giá việc ngân hàng thương mại đáp ứng các điều kiện mở sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp và có ý kiến đồng ý hoặc không đồng ý ; trường hợp không đồng ý , nêu rõ lý do . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e8` Khoản 1 Điều 18 `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #13_2008_QĐ-NHNN_32111#body_context_111 (Loại: `body_context`)
> **[Quyết định]`<LOAI_VAN_BAN>`** số **[13/2008/QĐ-NHNN]`<SO_HIEU>`** ban hành **[ngày 29 tháng 04 năm 2008]`<NGAY_BAN_HANH>`** bởi **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_BAN_HANH>`** . **[Điều 26]`<DIEU>`** . **[2 . **[Giám đốc]`<CHU_THE_CA_NHAN>`** **[Ngân hàng Nhà nước chi nhánh tỉnh , thành phố]`<CO_QUAN_THAM_QUYEN>`** chịu trách nhiệm trước **[Thống đốc Ngân hàng Nhà nước]`<CO_QUAN_THAM_QUYEN>`** về ý kiến **[nêu tại]`<TU_KHOA_PHAP_LY>`** **[Khoản 1 Điều này]`<THAM_CHIEU_PHAP_LY>`** .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Quyết định** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **13/2008/QĐ-NHNN** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_BAN_HANH` (span: `[11:14]`)
- `[e3]` **ngày 29 tháng 04 năm 2008** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 26** → `DIEU` (span: `[15:17]`)
- `[e5]` **2 . Giám đốc Ngân hàng Nhà nước chi nhánh tỉnh , thành phố chịu trách nhiệm trước Thống đốc Ngân hàng Nhà nước về ý kiến nêu tại Khoản 1 Điều này .** → `KHOAN` (span: `[18:42]`)
- `[e6]` **Khoản 1 Điều này** → `THAM_CHIEU_PHAP_LY` (span: `[37:41]`) *(lồng trong `e5` (`KHOAN`))*
- `[e7]` **nêu tại** → `TU_KHOA_PHAP_LY` (span: `[35:37]`) *(lồng trong `e5` (`KHOAN`))*
- `[e8]` **Ngân hàng Nhà nước chi nhánh tỉnh , thành phố** → `CO_QUAN_THAM_QUYEN` (span: `[21:27]`) *(lồng trong `e5` (`KHOAN`))*
- `[e9]` **Thống đốc Ngân hàng Nhà nước** → `CO_QUAN_THAM_QUYEN` (span: `[30:33]`) *(lồng trong `e5` (`KHOAN`))*
- `[e10]` **Giám đốc** → `CHU_THE_CA_NHAN` (span: `[20:21]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Ngân hàng Nhà nước Việt Nam `[CO_QUAN_BAN_HANH]`)
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Quyết định `[LOAI_VAN_BAN]`)
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 29 tháng 04 năm 2008 `[NGAY_BAN_HANH]`)
- (`e4` Điều 26 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`)
- (`e5` 2 . Giám đốc Ngân hàng Nhà nước chi nhánh tỉnh , thành phố chịu trách nhiệm trước Thống đốc Ngân hàng Nhà nước về ý kiến nêu tại Khoản 1 Điều này . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 26 `[DIEU]`)
- (`e7` nêu tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e6` Khoản 1 Điều này `[THAM_CHIEU_PHAP_LY]`)
- (`e5` 2 . Giám đốc Ngân hàng Nhà nước chi nhánh tỉnh , thành phố chịu trách nhiệm trước Thống đốc Ngân hàng Nhà nước về ý kiến nêu tại Khoản 1 Điều này . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e6` Khoản 1 Điều này `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #13_2008_QĐ-NHNN_32111#body_standalone_112 (Loại: `body_standalone`)
> **[Điều 26]`<DIEU>`** . **[2 . **[Giám đốc]`<CHU_THE_CA_NHAN>`** **[Ngân hàng Nhà nước chi nhánh tỉnh , thành phố]`<CO_QUAN_THAM_QUYEN>`** chịu trách nhiệm trước **[Thống đốc Ngân hàng Nhà nước]`<CO_QUAN_THAM_QUYEN>`** về ý kiến **[nêu tại]`<TU_KHOA_PHAP_LY>`** **[Khoản 1 Điều này]`<THAM_CHIEU_PHAP_LY>`** .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 26** → `DIEU` (span: `[0:2]`)
- `[e1]` **2 . Giám đốc Ngân hàng Nhà nước chi nhánh tỉnh , thành phố chịu trách nhiệm trước Thống đốc Ngân hàng Nhà nước về ý kiến nêu tại Khoản 1 Điều này .** → `KHOAN` (span: `[3:27]`)
- `[e2]` **Khoản 1 Điều này** → `THAM_CHIEU_PHAP_LY` (span: `[22:26]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **nêu tại** → `TU_KHOA_PHAP_LY` (span: `[20:22]`) *(lồng trong `e1` (`KHOAN`))*
- `[e4]` **Ngân hàng Nhà nước chi nhánh tỉnh , thành phố** → `CO_QUAN_THAM_QUYEN` (span: `[6:12]`) *(lồng trong `e1` (`KHOAN`))*
- `[e5]` **Thống đốc Ngân hàng Nhà nước** → `CO_QUAN_THAM_QUYEN` (span: `[15:18]`) *(lồng trong `e1` (`KHOAN`))*
- `[e6]` **Giám đốc** → `CHU_THE_CA_NHAN` (span: `[5:6]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 2 . Giám đốc Ngân hàng Nhà nước chi nhánh tỉnh , thành phố chịu trách nhiệm trước Thống đốc Ngân hàng Nhà nước về ý kiến nêu tại Khoản 1 Điều này . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 26 `[DIEU]`)
- (`e3` nêu tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e2` Khoản 1 Điều này `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 2 . Giám đốc Ngân hàng Nhà nước chi nhánh tỉnh , thành phố chịu trách nhiệm trước Thống đốc Ngân hàng Nhà nước về ý kiến nêu tại Khoản 1 Điều này . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e2` Khoản 1 Điều này `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #13_2008_QĐ-NHNN_32111#body_context_113 (Loại: `body_context`)
> **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_BAN_HANH>`** ban hành **[Quyết định]`<LOAI_VAN_BAN>`** số **[13/2008/QĐ-NHNN]`<SO_HIEU>`** . **[Điều 27]`<DIEU>`** . **[Khoản 1]`<KHOAN>`** . **[a ) Trong thời hạn mười ngày làm việc kể từ ngày nhận được **[văn bản đề nghị]`<GIAY_TO_HO_SO>`** mở **[sở giao dịch]`<CO_QUAN_THAM_QUYEN>`** , chi nhánh , **[văn phòng đại diện]`<TO_CHUC_DOANH_NGHIEP>`** , **[đơn vị sự nghiệp]`<TO_CHUC_DOANH_NGHIEP>`** của **[ngân hàng thương mại]`<TO_CHUC_DOANH_NGHIEP>`** , **[Ngân hàng Nhà nước chi nhánh tỉnh , thành phố]`<CO_QUAN_THAM_QUYEN>`** có **[văn bản trả lời]`<GIAY_TO_HO_SO>`** **[ngân hàng thương mại]`<TO_CHUC_DOANH_NGHIEP>`** , trong đó nêu rõ ý kiến đồng ý hoặc không đồng ý ; trường hợp không đồng ý , nêu rõ lý do .]`<DIEM>`**

**Thực thể:**
- `[e0]` **Quyết định** → `LOAI_VAN_BAN` (span: `[4:5]`)
- `[e1]` **13/2008/QĐ-NHNN** → `SO_HIEU` (span: `[6:7]`)
- `[e2]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_BAN_HANH` (span: `[0:3]`)
- `[e3]` **Điều 27** → `DIEU` (span: `[8:10]`)
- `[e4]` **Khoản 1** → `KHOAN` (span: `[11:13]`)
- `[e5]` **a ) Trong thời hạn mười ngày làm việc kể từ ngày nhận được văn bản đề nghị mở sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp của ngân hàng thương mại , Ngân hàng Nhà nước chi nhánh tỉnh , thành phố có văn bản trả lời ngân hàng thương mại , trong đó nêu rõ ý kiến đồng ý hoặc không đồng ý ; trường hợp không đồng ý , nêu rõ lý do .** → `DIEM` (span: `[14:73]`)
- `[e6]` **sở giao dịch** → `CO_QUAN_THAM_QUYEN` (span: `[29:31]`) *(lồng trong `e5` (`DIEM`))*
- `[e7]` **ngân hàng thương mại** → `TO_CHUC_DOANH_NGHIEP` (span: `[40:42]`) *(lồng trong `e5` (`DIEM`))*
- `[e8]` **ngân hàng thương mại** → `TO_CHUC_DOANH_NGHIEP` (span: `[52:54]`) *(lồng trong `e5` (`DIEM`))*
- `[e9]` **văn phòng đại diện** → `TO_CHUC_DOANH_NGHIEP` (span: `[34:36]`) *(lồng trong `e5` (`DIEM`))*
- `[e10]` **đơn vị sự nghiệp** → `TO_CHUC_DOANH_NGHIEP` (span: `[37:39]`) *(lồng trong `e5` (`DIEM`))*
- `[e11]` **Ngân hàng Nhà nước chi nhánh tỉnh , thành phố** → `CO_QUAN_THAM_QUYEN` (span: `[43:49]`) *(lồng trong `e5` (`DIEM`))*
- `[e12]` **văn bản đề nghị** → `GIAY_TO_HO_SO` (span: `[26:28]`) *(lồng trong `e5` (`DIEM`))*
- `[e13]` **văn bản trả lời** → `GIAY_TO_HO_SO` (span: `[50:52]`) *(lồng trong `e5` (`DIEM`))*

**Quan hệ:**
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Ngân hàng Nhà nước Việt Nam `[CO_QUAN_BAN_HANH]`)
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Quyết định `[LOAI_VAN_BAN]`)
- (`e3` Điều 27 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`)
- (`e4` Khoản 1 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 27 `[DIEU]`)
- (`e5` a ) Trong thời hạn mười ngày làm việc kể từ ngày nhận được văn bản đề nghị mở sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp của ngân hàng thương mại , Ngân hàng Nhà nước chi nhánh tỉnh , thành phố có văn bản trả lời ngân hàng thương mại , trong đó nêu rõ ý kiến đồng ý hoặc không đồng ý ; trường hợp không đồng ý , nêu rõ lý do . `[DIEM]`) ==[ **THUOC_VE** ]==> (`e4` Khoản 1 `[KHOAN]`)


---

### Mẫu #13_2008_QĐ-NHNN_32111#body_standalone_114 (Loại: `body_standalone`)
> **[Điều 27]`<DIEU>`** . **[Khoản 1]`<KHOAN>`** . **[a ) Trong thời hạn mười ngày làm việc kể từ ngày nhận được **[văn bản đề nghị]`<GIAY_TO_HO_SO>`** mở **[sở giao dịch]`<CO_QUAN_THAM_QUYEN>`** , chi nhánh , **[văn phòng đại diện]`<TO_CHUC_DOANH_NGHIEP>`** , **[đơn vị sự nghiệp]`<TO_CHUC_DOANH_NGHIEP>`** của **[ngân hàng thương mại]`<TO_CHUC_DOANH_NGHIEP>`** , **[Ngân hàng Nhà nước chi nhánh tỉnh , thành phố]`<CO_QUAN_THAM_QUYEN>`** có **[văn bản trả lời]`<GIAY_TO_HO_SO>`** **[ngân hàng thương mại]`<TO_CHUC_DOANH_NGHIEP>`** , trong đó nêu rõ ý kiến đồng ý hoặc không đồng ý ; trường hợp không đồng ý , nêu rõ lý do .]`<DIEM>`**

**Thực thể:**
- `[e0]` **Điều 27** → `DIEU` (span: `[0:2]`)
- `[e1]` **Khoản 1** → `KHOAN` (span: `[3:5]`)
- `[e2]` **a ) Trong thời hạn mười ngày làm việc kể từ ngày nhận được văn bản đề nghị mở sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp của ngân hàng thương mại , Ngân hàng Nhà nước chi nhánh tỉnh , thành phố có văn bản trả lời ngân hàng thương mại , trong đó nêu rõ ý kiến đồng ý hoặc không đồng ý ; trường hợp không đồng ý , nêu rõ lý do .** → `DIEM` (span: `[6:65]`)
- `[e3]` **sở giao dịch** → `CO_QUAN_THAM_QUYEN` (span: `[21:23]`) *(lồng trong `e2` (`DIEM`))*
- `[e4]` **ngân hàng thương mại** → `TO_CHUC_DOANH_NGHIEP` (span: `[32:34]`) *(lồng trong `e2` (`DIEM`))*
- `[e5]` **ngân hàng thương mại** → `TO_CHUC_DOANH_NGHIEP` (span: `[44:46]`) *(lồng trong `e2` (`DIEM`))*
- `[e6]` **văn phòng đại diện** → `TO_CHUC_DOANH_NGHIEP` (span: `[26:28]`) *(lồng trong `e2` (`DIEM`))*
- `[e7]` **đơn vị sự nghiệp** → `TO_CHUC_DOANH_NGHIEP` (span: `[29:31]`) *(lồng trong `e2` (`DIEM`))*
- `[e8]` **Ngân hàng Nhà nước chi nhánh tỉnh , thành phố** → `CO_QUAN_THAM_QUYEN` (span: `[35:41]`) *(lồng trong `e2` (`DIEM`))*
- `[e9]` **văn bản đề nghị** → `GIAY_TO_HO_SO` (span: `[18:20]`) *(lồng trong `e2` (`DIEM`))*
- `[e10]` **văn bản trả lời** → `GIAY_TO_HO_SO` (span: `[42:44]`) *(lồng trong `e2` (`DIEM`))*

**Quan hệ:**
- (`e1` Khoản 1 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 27 `[DIEU]`)
- (`e2` a ) Trong thời hạn mười ngày làm việc kể từ ngày nhận được văn bản đề nghị mở sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp của ngân hàng thương mại , Ngân hàng Nhà nước chi nhánh tỉnh , thành phố có văn bản trả lời ngân hàng thương mại , trong đó nêu rõ ý kiến đồng ý hoặc không đồng ý ; trường hợp không đồng ý , nêu rõ lý do . `[DIEM]`) ==[ **THUOC_VE** ]==> (`e1` Khoản 1 `[KHOAN]`)


---

### Mẫu #13_2008_QĐ-NHNN_32111#body_context_115 (Loại: `body_context`)
> **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_BAN_HANH>`** ban hành **[Quyết định]`<LOAI_VAN_BAN>`** số **[13/2008/QĐ-NHNN]`<SO_HIEU>`** . **[Điều 27]`<DIEU>`** . **[Khoản 1]`<KHOAN>`** . **[b ) Trong thời hạn mười ngày làm việc kể từ ngày nhận được văn bản của Vụ Các ngân hàng và **[tổ chức tín dụng phi ngân hàng]`<TO_CHUC_DOANH_NGHIEP>`** về việc chấm dứt hoạt động **[sở giao dịch]`<CO_QUAN_THAM_QUYEN>`** , chi nhánh , **[văn phòng đại diện]`<TO_CHUC_DOANH_NGHIEP>`** , **[đơn vị sự nghiệp]`<TO_CHUC_DOANH_NGHIEP>`** của **[ngân hàng thương mại]`<TO_CHUC_DOANH_NGHIEP>`** , **[Ngân hàng Nhà nước chi nhánh tỉnh , thành phố]`<CO_QUAN_THAM_QUYEN>`** có văn bản gửi **[Ngân hàng Nhà nước]`<CO_QUAN_THAM_QUYEN>`** , trong đó nêu rõ ý kiến đồng ý hoặc không đồng ý ; trường hợp không đồng ý , nêu rõ lý]`<DIEM>`**

**Thực thể:**
- `[e0]` **Quyết định** → `LOAI_VAN_BAN` (span: `[4:5]`)
- `[e1]` **13/2008/QĐ-NHNN** → `SO_HIEU` (span: `[6:7]`)
- `[e2]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_BAN_HANH` (span: `[0:3]`)
- `[e3]` **Điều 27** → `DIEU` (span: `[8:10]`)
- `[e4]` **Khoản 1** → `KHOAN` (span: `[11:13]`)
- `[e5]` **b ) Trong thời hạn mười ngày làm việc kể từ ngày nhận được văn bản của Vụ Các ngân hàng và tổ chức tín dụng phi ngân hàng về việc chấm dứt hoạt động sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp của ngân hàng thương mại , Ngân hàng Nhà nước chi nhánh tỉnh , thành phố có văn bản gửi Ngân hàng Nhà nước , trong đó nêu rõ ý kiến đồng ý hoặc không đồng ý ; trường hợp không đồng ý , nêu rõ lý** → `DIEM` (span: `[14:83]`)
- `[e6]` **sở giao dịch** → `CO_QUAN_THAM_QUYEN` (span: `[40:42]`) *(lồng trong `e5` (`DIEM`))*
- `[e7]` **ngân hàng thương mại** → `TO_CHUC_DOANH_NGHIEP` (span: `[51:53]`) *(lồng trong `e5` (`DIEM`))*
- `[e8]` **văn phòng đại diện** → `TO_CHUC_DOANH_NGHIEP` (span: `[45:47]`) *(lồng trong `e5` (`DIEM`))*
- `[e9]` **đơn vị sự nghiệp** → `TO_CHUC_DOANH_NGHIEP` (span: `[48:50]`) *(lồng trong `e5` (`DIEM`))*
- `[e10]` **Ngân hàng Nhà nước chi nhánh tỉnh , thành phố** → `CO_QUAN_THAM_QUYEN` (span: `[54:60]`) *(lồng trong `e5` (`DIEM`))*
- `[e11]` **Ngân hàng Nhà nước** → `CO_QUAN_THAM_QUYEN` (span: `[63:65]`) *(lồng trong `e5` (`DIEM`))*
- `[e12]` **tổ chức tín dụng phi ngân hàng** → `TO_CHUC_DOANH_NGHIEP` (span: `[32:36]`) *(lồng trong `e5` (`DIEM`))*

**Quan hệ:**
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Ngân hàng Nhà nước Việt Nam `[CO_QUAN_BAN_HANH]`)
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Quyết định `[LOAI_VAN_BAN]`)
- (`e3` Điều 27 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`)
- (`e4` Khoản 1 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 27 `[DIEU]`)
- (`e5` b ) Trong thời hạn mười ngày làm việc kể từ ngày nhận được văn bản của Vụ Các ngân hàng và tổ chức tín dụng phi ngân hàng về việc chấm dứt hoạt động sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp của ngân hàng thương mại , Ngân hàng Nhà nước chi nhánh tỉnh , thành phố có văn bản gửi Ngân hàng Nhà nước , trong đó nêu rõ ý kiến đồng ý hoặc không đồng ý ; trường hợp không đồng ý , nêu rõ lý `[DIEM]`) ==[ **THUOC_VE** ]==> (`e4` Khoản 1 `[KHOAN]`)


---

### Mẫu #13_2008_QĐ-NHNN_32111#body_standalone_116 (Loại: `body_standalone`)
> **[Điều 27]`<DIEU>`** . **[Khoản 1]`<KHOAN>`** . **[b ) Trong thời hạn mười ngày làm việc kể từ ngày nhận được văn bản của Vụ Các ngân hàng và **[tổ chức tín dụng phi ngân hàng]`<TO_CHUC_DOANH_NGHIEP>`** về việc chấm dứt hoạt động **[sở giao dịch]`<CO_QUAN_THAM_QUYEN>`** , chi nhánh , **[văn phòng đại diện]`<TO_CHUC_DOANH_NGHIEP>`** , **[đơn vị sự nghiệp]`<TO_CHUC_DOANH_NGHIEP>`** của **[ngân hàng thương mại]`<TO_CHUC_DOANH_NGHIEP>`** , **[Ngân hàng Nhà nước chi nhánh tỉnh , thành phố]`<CO_QUAN_THAM_QUYEN>`** có văn bản gửi **[Ngân hàng Nhà nước]`<CO_QUAN_THAM_QUYEN>`** , trong đó nêu rõ ý kiến đồng ý hoặc không đồng ý ; trường hợp không đồng ý , nêu rõ lý]`<DIEM>`**

**Thực thể:**
- `[e0]` **Điều 27** → `DIEU` (span: `[0:2]`)
- `[e1]` **Khoản 1** → `KHOAN` (span: `[3:5]`)
- `[e2]` **b ) Trong thời hạn mười ngày làm việc kể từ ngày nhận được văn bản của Vụ Các ngân hàng và tổ chức tín dụng phi ngân hàng về việc chấm dứt hoạt động sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp của ngân hàng thương mại , Ngân hàng Nhà nước chi nhánh tỉnh , thành phố có văn bản gửi Ngân hàng Nhà nước , trong đó nêu rõ ý kiến đồng ý hoặc không đồng ý ; trường hợp không đồng ý , nêu rõ lý** → `DIEM` (span: `[6:75]`)
- `[e3]` **sở giao dịch** → `CO_QUAN_THAM_QUYEN` (span: `[32:34]`) *(lồng trong `e2` (`DIEM`))*
- `[e4]` **ngân hàng thương mại** → `TO_CHUC_DOANH_NGHIEP` (span: `[43:45]`) *(lồng trong `e2` (`DIEM`))*
- `[e5]` **văn phòng đại diện** → `TO_CHUC_DOANH_NGHIEP` (span: `[37:39]`) *(lồng trong `e2` (`DIEM`))*
- `[e6]` **đơn vị sự nghiệp** → `TO_CHUC_DOANH_NGHIEP` (span: `[40:42]`) *(lồng trong `e2` (`DIEM`))*
- `[e7]` **Ngân hàng Nhà nước chi nhánh tỉnh , thành phố** → `CO_QUAN_THAM_QUYEN` (span: `[46:52]`) *(lồng trong `e2` (`DIEM`))*
- `[e8]` **Ngân hàng Nhà nước** → `CO_QUAN_THAM_QUYEN` (span: `[55:57]`) *(lồng trong `e2` (`DIEM`))*
- `[e9]` **tổ chức tín dụng phi ngân hàng** → `TO_CHUC_DOANH_NGHIEP` (span: `[24:28]`) *(lồng trong `e2` (`DIEM`))*

**Quan hệ:**
- (`e1` Khoản 1 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 27 `[DIEU]`)
- (`e2` b ) Trong thời hạn mười ngày làm việc kể từ ngày nhận được văn bản của Vụ Các ngân hàng và tổ chức tín dụng phi ngân hàng về việc chấm dứt hoạt động sở giao dịch , chi nhánh , văn phòng đại diện , đơn vị sự nghiệp của ngân hàng thương mại , Ngân hàng Nhà nước chi nhánh tỉnh , thành phố có văn bản gửi Ngân hàng Nhà nước , trong đó nêu rõ ý kiến đồng ý hoặc không đồng ý ; trường hợp không đồng ý , nêu rõ lý `[DIEM]`) ==[ **THUOC_VE** ]==> (`e1` Khoản 1 `[KHOAN]`)


---

### Mẫu #13_2008_QĐ-NHNN_32111#body_context_117 (Loại: `body_context`)
> **[Quyết định]`<LOAI_VAN_BAN>`** số **[13/2008/QĐ-NHNN]`<SO_HIEU>`** ban hành **[ngày 29 tháng 04 năm 2008]`<NGAY_BAN_HANH>`** bởi **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_BAN_HANH>`** . **[Điều 27]`<DIEU>`** . **[2 . **[Giám đốc]`<CHU_THE_CA_NHAN>`** **[Ngân hàng Nhà nước chi nhánh tỉnh , thành phố]`<CO_QUAN_THAM_QUYEN>`** chịu trách nhiệm trước **[Thống đốc Ngân hàng Nhà nước]`<CO_QUAN_THAM_QUYEN>`** về các ý kiến , quyết định **[nêu tại]`<TU_KHOA_PHAP_LY>`** **[Khoản 1 Điều này]`<THAM_CHIEU_PHAP_LY>`** .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Quyết định** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **13/2008/QĐ-NHNN** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_BAN_HANH` (span: `[11:14]`)
- `[e3]` **ngày 29 tháng 04 năm 2008** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 27** → `DIEU` (span: `[15:17]`)
- `[e5]` **2 . Giám đốc Ngân hàng Nhà nước chi nhánh tỉnh , thành phố chịu trách nhiệm trước Thống đốc Ngân hàng Nhà nước về các ý kiến , quyết định nêu tại Khoản 1 Điều này .** → `KHOAN` (span: `[18:45]`)
- `[e6]` **Khoản 1 Điều này** → `THAM_CHIEU_PHAP_LY` (span: `[40:44]`) *(lồng trong `e5` (`KHOAN`))*
- `[e7]` **nêu tại** → `TU_KHOA_PHAP_LY` (span: `[38:40]`) *(lồng trong `e5` (`KHOAN`))*
- `[e8]` **Ngân hàng Nhà nước chi nhánh tỉnh , thành phố** → `CO_QUAN_THAM_QUYEN` (span: `[21:27]`) *(lồng trong `e5` (`KHOAN`))*
- `[e9]` **Thống đốc Ngân hàng Nhà nước** → `CO_QUAN_THAM_QUYEN` (span: `[30:33]`) *(lồng trong `e5` (`KHOAN`))*
- `[e10]` **Giám đốc** → `CHU_THE_CA_NHAN` (span: `[20:21]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Ngân hàng Nhà nước Việt Nam `[CO_QUAN_BAN_HANH]`)
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Quyết định `[LOAI_VAN_BAN]`)
- (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 29 tháng 04 năm 2008 `[NGAY_BAN_HANH]`)
- (`e4` Điều 27 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 13/2008/QĐ-NHNN `[SO_HIEU]`)
- (`e5` 2 . Giám đốc Ngân hàng Nhà nước chi nhánh tỉnh , thành phố chịu trách nhiệm trước Thống đốc Ngân hàng Nhà nước về các ý kiến , quyết định nêu tại Khoản 1 Điều này . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 27 `[DIEU]`)
- (`e7` nêu tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e6` Khoản 1 Điều này `[THAM_CHIEU_PHAP_LY]`)
- (`e5` 2 . Giám đốc Ngân hàng Nhà nước chi nhánh tỉnh , thành phố chịu trách nhiệm trước Thống đốc Ngân hàng Nhà nước về các ý kiến , quyết định nêu tại Khoản 1 Điều này . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e6` Khoản 1 Điều này `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #13_2008_QĐ-NHNN_32111#body_standalone_118 (Loại: `body_standalone`)
> **[Điều 27]`<DIEU>`** . **[2 . **[Giám đốc]`<CHU_THE_CA_NHAN>`** **[Ngân hàng Nhà nước chi nhánh tỉnh , thành phố]`<CO_QUAN_THAM_QUYEN>`** chịu trách nhiệm trước **[Thống đốc Ngân hàng Nhà nước]`<CO_QUAN_THAM_QUYEN>`** về các ý kiến , quyết định **[nêu tại]`<TU_KHOA_PHAP_LY>`** **[Khoản 1 Điều này]`<THAM_CHIEU_PHAP_LY>`** .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 27** → `DIEU` (span: `[0:2]`)
- `[e1]` **2 . Giám đốc Ngân hàng Nhà nước chi nhánh tỉnh , thành phố chịu trách nhiệm trước Thống đốc Ngân hàng Nhà nước về các ý kiến , quyết định nêu tại Khoản 1 Điều này .** → `KHOAN` (span: `[3:30]`)
- `[e2]` **Khoản 1 Điều này** → `THAM_CHIEU_PHAP_LY` (span: `[25:29]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **nêu tại** → `TU_KHOA_PHAP_LY` (span: `[23:25]`) *(lồng trong `e1` (`KHOAN`))*
- `[e4]` **Ngân hàng Nhà nước chi nhánh tỉnh , thành phố** → `CO_QUAN_THAM_QUYEN` (span: `[6:12]`) *(lồng trong `e1` (`KHOAN`))*
- `[e5]` **Thống đốc Ngân hàng Nhà nước** → `CO_QUAN_THAM_QUYEN` (span: `[15:18]`) *(lồng trong `e1` (`KHOAN`))*
- `[e6]` **Giám đốc** → `CHU_THE_CA_NHAN` (span: `[5:6]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 2 . Giám đốc Ngân hàng Nhà nước chi nhánh tỉnh , thành phố chịu trách nhiệm trước Thống đốc Ngân hàng Nhà nước về các ý kiến , quyết định nêu tại Khoản 1 Điều này . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 27 `[DIEU]`)
- (`e3` nêu tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e2` Khoản 1 Điều này `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 2 . Giám đốc Ngân hàng Nhà nước chi nhánh tỉnh , thành phố chịu trách nhiệm trước Thống đốc Ngân hàng Nhà nước về các ý kiến , quyết định nêu tại Khoản 1 Điều này . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e2` Khoản 1 Điều này `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #13_2008_QĐ-NHNN_32111#hard_negative_119 (Loại: `hard_negative`)
> CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM


---

### Mẫu #13_2008_QĐ-NHNN_32111#hard_negative_120 (Loại: `hard_negative`)
> Mục 2 . MỞ , CHẤM DỨT HOẠT ĐỘNG CHI NHÁNH , VĂN PHÒNG ĐẠI DIỆN Ở NƯỚC NGOÀI


---

### Mẫu #13_2008_QĐ-NHNN_32111#hard_negative_121 (Loại: `hard_negative`)
> Mục 1 . TRÁCH NHIỆM CỦA NGÂN HÀNG THƯƠNG MẠI


---

### Mẫu #13_2008_QĐ-NHNN_32111#hard_negative_122 (Loại: `hard_negative`)
> Mục 2 . TRÁCH NHIỆM CỦA CÁC ĐƠN VỊ THUỘC NGÂN HÀNG NHÀ NƯỚC


---
