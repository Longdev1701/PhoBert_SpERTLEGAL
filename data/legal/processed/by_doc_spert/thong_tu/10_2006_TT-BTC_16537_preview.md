# Dữ liệu gán nhãn văn bản: 10_2006_TT-BTC_16537
- **Thể loại**: `thong_tu`
- **Phân vùng dữ liệu**: `TRAIN`
- **Tổng số mẫu**: 14 mẫu
- **Tổng số thực thể**: 51
- **Tổng số quan hệ**: 23

---

### Mẫu #10_2006_TT-BTC_16537#preamble_context_0 (Loại: `preamble_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[10/2006/TT-BTC]`<SO_HIEU>`** của **[Bộ Tài chính]`<CO_QUAN_BAN_HANH>`** . **[Căn cứ]`<TU_KHOA_PHAP_LY>`** các Luật Thuế và Pháp lệnh Thuế , Pháp lệnh Phí , lệ phí ;

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **10/2006/TT-BTC** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Tài chính** → `CO_QUAN_BAN_HANH` (span: `[4:6]`)
- `[e3]` **Căn cứ** → `TU_KHOA_PHAP_LY` (span: `[7:8]`)

**Quan hệ:**
- (`e1` 10/2006/TT-BTC `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Tài chính `[CO_QUAN_BAN_HANH]`)
- (`e1` 10/2006/TT-BTC `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)


---

### Mẫu #10_2006_TT-BTC_16537#preamble_standalone_1 (Loại: `preamble_standalone`)
> **[Căn cứ]`<TU_KHOA_PHAP_LY>`** các Luật Thuế và Pháp lệnh Thuế , Pháp lệnh Phí , lệ phí ;

**Thực thể:**
- `[e0]` **Căn cứ** → `TU_KHOA_PHAP_LY` (span: `[0:1]`)


---

### Mẫu #10_2006_TT-BTC_16537#preamble_context_2 (Loại: `preamble_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[10/2006/TT-BTC]`<SO_HIEU>`** của **[Bộ Tài chính]`<CO_QUAN_BAN_HANH>`** . **[Căn cứ]`<TU_KHOA_PHAP_LY>`** **[Luật Hải quan]`<THAM_CHIEU_PHAP_LY>`** ;

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **10/2006/TT-BTC** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Tài chính** → `CO_QUAN_BAN_HANH` (span: `[4:6]`)
- `[e3]` **Luật Hải quan** → `THAM_CHIEU_PHAP_LY` (span: `[8:10]`)
- `[e4]` **Căn cứ** → `TU_KHOA_PHAP_LY` (span: `[7:8]`)

**Quan hệ:**
- (`e1` 10/2006/TT-BTC `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Tài chính `[CO_QUAN_BAN_HANH]`)
- (`e1` 10/2006/TT-BTC `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e4` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Luật Hải quan `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 10/2006/TT-BTC `[SO_HIEU]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Luật Hải quan `[THAM_CHIEU_PHAP_LY]`)


---

### Mẫu #10_2006_TT-BTC_16537#preamble_standalone_3 (Loại: `preamble_standalone`)
> **[Căn cứ]`<TU_KHOA_PHAP_LY>`** **[Luật Hải quan]`<THAM_CHIEU_PHAP_LY>`** ;

**Thực thể:**
- `[e0]` **Luật Hải quan** → `THAM_CHIEU_PHAP_LY` (span: `[1:3]`)
- `[e1]` **Căn cứ** → `TU_KHOA_PHAP_LY` (span: `[0:1]`)

**Quan hệ:**
- (`e1` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e0` Luật Hải quan `[THAM_CHIEU_PHAP_LY]`)


---

### Mẫu #10_2006_TT-BTC_16537#preamble_context_4 (Loại: `preamble_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[10/2006/TT-BTC]`<SO_HIEU>`** của **[Bộ Tài chính]`<CO_QUAN_BAN_HANH>`** . **[Căn cứ]`<TU_KHOA_PHAP_LY>`** **[Quyết định số 75/1998/QĐ-TTg]`<THAM_CHIEU_PHAP_LY>`** **[ngày 4/4/1998]`<NGAY_THAM_CHIEU>`** của **[Thủ tướng Chính phủ]`<CO_QUAN_THAM_QUYEN>`** quy định về mã số đối tượng nộp thuế ;

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **10/2006/TT-BTC** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Tài chính** → `CO_QUAN_BAN_HANH` (span: `[4:6]`)
- `[e3]` **Quyết định số 75/1998/QĐ-TTg** → `THAM_CHIEU_PHAP_LY` (span: `[8:11]`)
- `[e4]` **Căn cứ** → `TU_KHOA_PHAP_LY` (span: `[7:8]`)
- `[e5]` **ngày 4/4/1998** → `NGAY_THAM_CHIEU` (span: `[11:13]`)
- `[e6]` **Thủ tướng Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[14:16]`)

**Quan hệ:**
- (`e1` 10/2006/TT-BTC `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Tài chính `[CO_QUAN_BAN_HANH]`)
- (`e1` 10/2006/TT-BTC `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e4` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Quyết định số 75/1998/QĐ-TTg `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 10/2006/TT-BTC `[SO_HIEU]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Quyết định số 75/1998/QĐ-TTg `[THAM_CHIEU_PHAP_LY]`)
- (`e3` Quyết định số 75/1998/QĐ-TTg `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e5` ngày 4/4/1998 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #10_2006_TT-BTC_16537#preamble_standalone_5 (Loại: `preamble_standalone`)
> **[Căn cứ]`<TU_KHOA_PHAP_LY>`** **[Quyết định số 75/1998/QĐ-TTg]`<THAM_CHIEU_PHAP_LY>`** **[ngày 4/4/1998]`<NGAY_THAM_CHIEU>`** của **[Thủ tướng Chính phủ]`<CO_QUAN_THAM_QUYEN>`** quy định về mã số đối tượng nộp thuế ;

**Thực thể:**
- `[e0]` **Quyết định số 75/1998/QĐ-TTg** → `THAM_CHIEU_PHAP_LY` (span: `[1:4]`)
- `[e1]` **Căn cứ** → `TU_KHOA_PHAP_LY` (span: `[0:1]`)
- `[e2]` **ngày 4/4/1998** → `NGAY_THAM_CHIEU` (span: `[4:6]`)
- `[e3]` **Thủ tướng Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[7:9]`)

**Quan hệ:**
- (`e1` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e0` Quyết định số 75/1998/QĐ-TTg `[THAM_CHIEU_PHAP_LY]`)
- (`e3` Thủ tướng Chính phủ `[CO_QUAN_THAM_QUYEN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e0` Quyết định số 75/1998/QĐ-TTg `[THAM_CHIEU_PHAP_LY]`)
- (`e0` Quyết định số 75/1998/QĐ-TTg `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e2` ngày 4/4/1998 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #10_2006_TT-BTC_16537#preamble_context_6 (Loại: `preamble_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[10/2006/TT-BTC]`<SO_HIEU>`** của **[Bộ Tài chính]`<CO_QUAN_BAN_HANH>`** . **[Bộ Tài chính]`<CO_QUAN_THAM_QUYEN>`** hướng dẫn thực hiện việc đăng ký cấp mã số của tổ chức , cá nhân nộp thuế ( gọi tắt là mã số thuế ) và sử dụng mã số thuế như sau :

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **10/2006/TT-BTC** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Tài chính** → `CO_QUAN_BAN_HANH` (span: `[4:6]`)
- `[e3]` **Bộ Tài chính** → `CO_QUAN_THAM_QUYEN` (span: `[7:9]`)

**Quan hệ:**
- (`e1` 10/2006/TT-BTC `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Tài chính `[CO_QUAN_BAN_HANH]`)
- (`e1` 10/2006/TT-BTC `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)


---

### Mẫu #10_2006_TT-BTC_16537#preamble_standalone_7 (Loại: `preamble_standalone`)
> **[Bộ Tài chính]`<CO_QUAN_THAM_QUYEN>`** hướng dẫn thực hiện việc đăng ký cấp mã số của tổ chức , cá nhân nộp thuế ( gọi tắt là mã số thuế ) và sử dụng mã số thuế như sau :

**Thực thể:**
- `[e0]` **Bộ Tài chính** → `CO_QUAN_THAM_QUYEN` (span: `[0:2]`)


---

### Mẫu #10_2006_TT-BTC_16537#preamble_context_8 (Loại: `preamble_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[10/2006/TT-BTC]`<SO_HIEU>`** của **[Bộ Tài chính]`<CO_QUAN_BAN_HANH>`** . 2 . Đối tượng được cấp mã số thuế : tất cả các tổ chức , cá nhân nộp thuế với **[cơ quan Thuế]`<CO_QUAN_THAM_QUYEN>`** , **[cơ quan Hải quan]`<CO_QUAN_THAM_QUYEN>`** theo quy định của pháp luật về thuế ( trừ các đối tượng chỉ nộp thuế nhà đất , thuế sử dụng đất nông nghiệp , thu tiền sử dụng đất , thuế chuyển quyền sử dụng đất , cá nhân nộp lệ phí trước bạ ) .

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **10/2006/TT-BTC** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Tài chính** → `CO_QUAN_BAN_HANH` (span: `[4:6]`)
- `[e3]` **cơ quan Thuế** → `CO_QUAN_THAM_QUYEN` (span: `[23:25]`)
- `[e4]` **cơ quan Hải quan** → `CO_QUAN_THAM_QUYEN` (span: `[26:28]`)

**Quan hệ:**
- (`e1` 10/2006/TT-BTC `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Tài chính `[CO_QUAN_BAN_HANH]`)
- (`e1` 10/2006/TT-BTC `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)


---

### Mẫu #10_2006_TT-BTC_16537#preamble_standalone_9 (Loại: `preamble_standalone`)
> 2 . Đối tượng được cấp mã số thuế : tất cả các tổ chức , cá nhân nộp thuế với **[cơ quan Thuế]`<CO_QUAN_THAM_QUYEN>`** , **[cơ quan Hải quan]`<CO_QUAN_THAM_QUYEN>`** theo quy định của pháp luật về thuế ( trừ các đối tượng chỉ nộp thuế nhà đất , thuế sử dụng đất nông nghiệp , thu tiền sử dụng đất , thuế chuyển quyền sử dụng đất , cá nhân nộp lệ phí trước bạ ) .

**Thực thể:**
- `[e0]` **cơ quan Thuế** → `CO_QUAN_THAM_QUYEN` (span: `[16:18]`)
- `[e1]` **cơ quan Hải quan** → `CO_QUAN_THAM_QUYEN` (span: `[19:21]`)


---

### Mẫu #10_2006_TT-BTC_16537#preamble_context_10 (Loại: `preamble_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[10/2006/TT-BTC]`<SO_HIEU>`** của **[Bộ Tài chính]`<CO_QUAN_BAN_HANH>`** . Mã số thuế gắn với sự tồn tại của tổ chức , cá nhân nộp thuế . Mã số thuế đã được cấp sẽ không được sử dụng lại để cấp cho tổ chức , cá nhân nộp thuế khác . Tổ chức , cá nhân nộp thuế chấm dứt tồn tại thì mã số thuế sẽ không còn giá trị sử dụng . Các **[doanh nghiệp]`<TO_CHUC_DOANH_NGHIEP>`** , **[tổ chức kinh doanh chấm dứt tồn]`<TO_CHUC_DOANH_NGHIEP>`** tại thì mã số thuế bị đóng và không được sử dụng lại . Mã số thuế đã cấp cho một cá nhân

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **10/2006/TT-BTC** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Tài chính** → `CO_QUAN_BAN_HANH` (span: `[4:6]`)
- `[e3]` **doanh nghiệp** → `TO_CHUC_DOANH_NGHIEP` (span: `[56:57]`)
- `[e4]` **tổ chức kinh doanh chấm dứt tồn** → `TO_CHUC_DOANH_NGHIEP` (span: `[58:62]`)

**Quan hệ:**
- (`e1` 10/2006/TT-BTC `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Tài chính `[CO_QUAN_BAN_HANH]`)
- (`e1` 10/2006/TT-BTC `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)


---

### Mẫu #10_2006_TT-BTC_16537#preamble_standalone_11 (Loại: `preamble_standalone`)
> Mã số thuế gắn với sự tồn tại của tổ chức , cá nhân nộp thuế . Mã số thuế đã được cấp sẽ không được sử dụng lại để cấp cho tổ chức , cá nhân nộp thuế khác . Tổ chức , cá nhân nộp thuế chấm dứt tồn tại thì mã số thuế sẽ không còn giá trị sử dụng . Các **[doanh nghiệp]`<TO_CHUC_DOANH_NGHIEP>`** , **[tổ chức kinh doanh chấm dứt tồn]`<TO_CHUC_DOANH_NGHIEP>`** tại thì mã số thuế bị đóng và không được sử dụng lại . Mã số thuế đã cấp cho một cá nhân

**Thực thể:**
- `[e0]` **doanh nghiệp** → `TO_CHUC_DOANH_NGHIEP` (span: `[49:50]`)
- `[e1]` **tổ chức kinh doanh chấm dứt tồn** → `TO_CHUC_DOANH_NGHIEP` (span: `[51:55]`)


---

### Mẫu #10_2006_TT-BTC_16537#preamble_context_12 (Loại: `preamble_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[10/2006/TT-BTC]`<SO_HIEU>`** của **[Bộ Tài chính]`<CO_QUAN_BAN_HANH>`** . Các chi nhánh , **[văn phòng đại diện]`<TO_CHUC_DOANH_NGHIEP>`** của các **[doanh nghiệp]`<TO_CHUC_DOANH_NGHIEP>`** có hoạt động kinh doanh và đăng ký nộp thuế trực tiếp với **[cơ quan Thuế]`<CO_QUAN_THAM_QUYEN>`** ( trừ các Chi nhánh của Công ty nước ngoài mà trụ sở chính của Công ty đặt tại nước ngoài ) ;

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **10/2006/TT-BTC** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Tài chính** → `CO_QUAN_BAN_HANH` (span: `[4:6]`)
- `[e3]` **cơ quan Thuế** → `CO_QUAN_THAM_QUYEN` (span: `[23:25]`)
- `[e4]` **văn phòng đại diện** → `TO_CHUC_DOANH_NGHIEP` (span: `[10:12]`)
- `[e5]` **doanh nghiệp** → `TO_CHUC_DOANH_NGHIEP` (span: `[14:15]`)

**Quan hệ:**
- (`e1` 10/2006/TT-BTC `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Tài chính `[CO_QUAN_BAN_HANH]`)
- (`e1` 10/2006/TT-BTC `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)


---

### Mẫu #10_2006_TT-BTC_16537#preamble_standalone_13 (Loại: `preamble_standalone`)
> Các chi nhánh , **[văn phòng đại diện]`<TO_CHUC_DOANH_NGHIEP>`** của các **[doanh nghiệp]`<TO_CHUC_DOANH_NGHIEP>`** có hoạt động kinh doanh và đăng ký nộp thuế trực tiếp với **[cơ quan Thuế]`<CO_QUAN_THAM_QUYEN>`** ( trừ các Chi nhánh của Công ty nước ngoài mà trụ sở chính của Công ty đặt tại nước ngoài ) ;

**Thực thể:**
- `[e0]` **cơ quan Thuế** → `CO_QUAN_THAM_QUYEN` (span: `[16:18]`)
- `[e1]` **văn phòng đại diện** → `TO_CHUC_DOANH_NGHIEP` (span: `[3:5]`)
- `[e2]` **doanh nghiệp** → `TO_CHUC_DOANH_NGHIEP` (span: `[7:8]`)


---
