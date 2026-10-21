# Dữ liệu gán nhãn văn bản: 11_2015_TT-BKHĐT_92514
- **Thể loại**: `thong_tu`
- **Phân vùng dữ liệu**: `DEV`
- **Tổng số mẫu**: 58 mẫu
- **Tổng số thực thể**: 368
- **Tổng số quan hệ**: 261

---

### Mẫu #11_2015_TT-BKHĐT_92514#header_0 (Loại: `header`)
> **[BỘ KẾ HOẠCH VÀ ĐẦU TƯ]`<CO_QUAN_BAN_HANH>`** . CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM . Độc lập – Tự do – Hạnh phúc . Số : **[11/2015/TT-BKHĐT]`<SO_HIEU>`** . **[Ngày 27 tháng 10 năm 2015]`<NGAY_BAN_HANH>`** . **[THÔNG TƯ]`<LOAI_VAN_BAN>`**

**Thực thể:**
- `[e0]` **11/2015/TT-BKHĐT** → `SO_HIEU` (span: `[20:21]`)
- `[e1]` **Ngày 27 tháng 10 năm 2015** → `NGAY_BAN_HANH` (span: `[22:28]`)
- `[e2]` **BỘ KẾ HOẠCH VÀ ĐẦU TƯ** → `CO_QUAN_BAN_HANH` (span: `[0:4]`)
- `[e3]` **THÔNG TƯ** → `LOAI_VAN_BAN` (span: `[29:30]`)

**Quan hệ:**
- (`e0` 11/2015/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` BỘ KẾ HOẠCH VÀ ĐẦU TƯ `[CO_QUAN_BAN_HANH]`)
- (`e0` 11/2015/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e1` Ngày 27 tháng 10 năm 2015 `[NGAY_BAN_HANH]`)
- (`e0` 11/2015/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e3` THÔNG TƯ `[LOAI_VAN_BAN]`)


---

### Mẫu #11_2015_TT-BKHĐT_92514#signature_1 (Loại: `signature`)
> **[BỘ TRƯỞNG]`<CHUC_DANH_NGUOI_KY>`** . ( Đã ký ) . **[Bùi Quang Vinh]`<NGUOI_KY>`**

**Thực thể:**
- `[e0]` **Bùi Quang Vinh** → `NGUOI_KY` (span: `[7:9]`)
- `[e1]` **BỘ TRƯỞNG** → `CHUC_DANH_NGUOI_KY` (span: `[0:1]`)

**Quan hệ:**
- (`e0` Bùi Quang Vinh `[NGUOI_KY]`) ==[ **GIU_CHUC_VU** ]==> (`e1` BỘ TRƯỞNG `[CHUC_DANH_NGUOI_KY]`)


---

### Mẫu #11_2015_TT-BKHĐT_92514#meta_2 (Loại: `meta`)
> **[BỘ KẾ HOẠCH VÀ ĐẦU TƯ]`<CO_QUAN_BAN_HANH>`** . CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM . Độc lập – Tự do – Hạnh phúc . Số : **[11/2015/TT-BKHĐT]`<SO_HIEU>`** . Ngày 27 tháng 10 năm 2015 . **[THÔNG TƯ]`<LOAI_VAN_BAN>`** . **[BỘ TRƯỞNG]`<CHUC_DANH_NGUOI_KY>`** . ( Đã ký ) . **[Bùi Quang Vinh]`<NGUOI_KY>`**

**Thực thể:**
- `[e0]` **11/2015/TT-BKHĐT** → `SO_HIEU` (span: `[20:21]`)
- `[e1]` **BỘ KẾ HOẠCH VÀ ĐẦU TƯ** → `CO_QUAN_BAN_HANH` (span: `[0:4]`)
- `[e2]` **THÔNG TƯ** → `LOAI_VAN_BAN` (span: `[29:30]`)
- `[e3]` **Bùi Quang Vinh** → `NGUOI_KY` (span: `[38:40]`)
- `[e4]` **BỘ TRƯỞNG** → `CHUC_DANH_NGUOI_KY` (span: `[31:32]`)

**Quan hệ:**
- (`e0` 11/2015/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e1` BỘ KẾ HOẠCH VÀ ĐẦU TƯ `[CO_QUAN_BAN_HANH]`)
- (`e0` 11/2015/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e2` THÔNG TƯ `[LOAI_VAN_BAN]`)
- (`e0` 11/2015/TT-BKHĐT `[SO_HIEU]`) ==[ **KY_BOI** ]==> (`e3` Bùi Quang Vinh `[NGUOI_KY]`)
- (`e3` Bùi Quang Vinh `[NGUOI_KY]`) ==[ **GIU_CHUC_VU** ]==> (`e4` BỘ TRƯỞNG `[CHUC_DANH_NGUOI_KY]`)


---

### Mẫu #11_2015_TT-BKHĐT_92514#preamble_context_3 (Loại: `preamble_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[11/2015/TT-BKHĐT]`<SO_HIEU>`** của **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** . Quy định chi tiết lập **[hồ sơ yêu cầu]`<GIAY_TO_HO_SO>`** đối với chỉ định thầu , chào hàng cạnh tranh

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **11/2015/TT-BKHĐT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[4:8]`)
- `[e3]` **hồ sơ yêu cầu** → `GIAY_TO_HO_SO` (span: `[12:14]`)

**Quan hệ:**
- (`e1` 11/2015/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 11/2015/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)


---

### Mẫu #11_2015_TT-BKHĐT_92514#preamble_standalone_4 (Loại: `preamble_standalone`)
> Quy định chi tiết lập **[hồ sơ yêu cầu]`<GIAY_TO_HO_SO>`** đối với chỉ định thầu , chào hàng cạnh tranh

**Thực thể:**
- `[e0]` **hồ sơ yêu cầu** → `GIAY_TO_HO_SO` (span: `[3:5]`)


---

### Mẫu #11_2015_TT-BKHĐT_92514#preamble_context_5 (Loại: `preamble_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[11/2015/TT-BKHĐT]`<SO_HIEU>`** của **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** . **[Căn cứ]`<TU_KHOA_PHAP_LY>`** **[Luật đấu thầu số 43/2013/QH13]`<THAM_CHIEU_PHAP_LY>`** **[ngày 26 tháng 11 năm 2013]`<NGAY_THAM_CHIEU>`** ;

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **11/2015/TT-BKHĐT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[4:8]`)
- `[e3]` **Luật đấu thầu số 43/2013/QH13** → `THAM_CHIEU_PHAP_LY` (span: `[10:14]`)
- `[e4]` **Căn cứ** → `TU_KHOA_PHAP_LY` (span: `[9:10]`)
- `[e5]` **ngày 26 tháng 11 năm 2013** → `NGAY_THAM_CHIEU` (span: `[14:20]`)

**Quan hệ:**
- (`e1` 11/2015/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 11/2015/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e4` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Luật đấu thầu số 43/2013/QH13 `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 11/2015/TT-BKHĐT `[SO_HIEU]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Luật đấu thầu số 43/2013/QH13 `[THAM_CHIEU_PHAP_LY]`)
- (`e3` Luật đấu thầu số 43/2013/QH13 `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e5` ngày 26 tháng 11 năm 2013 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #11_2015_TT-BKHĐT_92514#preamble_standalone_6 (Loại: `preamble_standalone`)
> **[Căn cứ]`<TU_KHOA_PHAP_LY>`** **[Luật đấu thầu số 43/2013/QH13]`<THAM_CHIEU_PHAP_LY>`** **[ngày 26 tháng 11 năm 2013]`<NGAY_THAM_CHIEU>`** ;

**Thực thể:**
- `[e0]` **Luật đấu thầu số 43/2013/QH13** → `THAM_CHIEU_PHAP_LY` (span: `[1:5]`)
- `[e1]` **Căn cứ** → `TU_KHOA_PHAP_LY` (span: `[0:1]`)
- `[e2]` **ngày 26 tháng 11 năm 2013** → `NGAY_THAM_CHIEU` (span: `[5:11]`)

**Quan hệ:**
- (`e1` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e0` Luật đấu thầu số 43/2013/QH13 `[THAM_CHIEU_PHAP_LY]`)
- (`e0` Luật đấu thầu số 43/2013/QH13 `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e2` ngày 26 tháng 11 năm 2013 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #11_2015_TT-BKHĐT_92514#preamble_context_7 (Loại: `preamble_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[11/2015/TT-BKHĐT]`<SO_HIEU>`** của **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** . **[Căn cứ]`<TU_KHOA_PHAP_LY>`** **[Nghị định số 63/2014/NĐ-CP]`<THAM_CHIEU_PHAP_LY>`** **[ngày 26 tháng 6 năm 2014]`<NGAY_THAM_CHIEU>`** của **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** quy định chi tiết thi hành một số điều của Luật đấu thầu về lựa chọn nhà thầu ;

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **11/2015/TT-BKHĐT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[4:8]`)
- `[e3]` **Nghị định số 63/2014/NĐ-CP** → `THAM_CHIEU_PHAP_LY` (span: `[10:13]`)
- `[e4]` **Căn cứ** → `TU_KHOA_PHAP_LY` (span: `[9:10]`)
- `[e5]` **ngày 26 tháng 6 năm 2014** → `NGAY_THAM_CHIEU` (span: `[13:19]`)
- `[e6]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[20:21]`)

**Quan hệ:**
- (`e1` 11/2015/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 11/2015/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e4` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Nghị định số 63/2014/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 11/2015/TT-BKHĐT `[SO_HIEU]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Nghị định số 63/2014/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e3` Nghị định số 63/2014/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e5` ngày 26 tháng 6 năm 2014 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #11_2015_TT-BKHĐT_92514#preamble_standalone_8 (Loại: `preamble_standalone`)
> **[Căn cứ]`<TU_KHOA_PHAP_LY>`** **[Nghị định số 63/2014/NĐ-CP]`<THAM_CHIEU_PHAP_LY>`** **[ngày 26 tháng 6 năm 2014]`<NGAY_THAM_CHIEU>`** của **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** quy định chi tiết thi hành một số điều của Luật đấu thầu về lựa chọn nhà thầu ;

**Thực thể:**
- `[e0]` **Nghị định số 63/2014/NĐ-CP** → `THAM_CHIEU_PHAP_LY` (span: `[1:4]`)
- `[e1]` **Căn cứ** → `TU_KHOA_PHAP_LY` (span: `[0:1]`)
- `[e2]` **ngày 26 tháng 6 năm 2014** → `NGAY_THAM_CHIEU` (span: `[4:10]`)
- `[e3]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[11:12]`)

**Quan hệ:**
- (`e1` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e0` Nghị định số 63/2014/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e3` Chính phủ `[CO_QUAN_THAM_QUYEN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e0` Nghị định số 63/2014/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e0` Nghị định số 63/2014/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e2` ngày 26 tháng 6 năm 2014 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #11_2015_TT-BKHĐT_92514#preamble_context_9 (Loại: `preamble_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[11/2015/TT-BKHĐT]`<SO_HIEU>`** của **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** . **[Căn cứ]`<TU_KHOA_PHAP_LY>`** **[Nghị định số 116/2008/NĐ-CP]`<THAM_CHIEU_PHAP_LY>`** **[ngày 14 tháng 11 năm 2008]`<NGAY_THAM_CHIEU>`** của **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** quy định chức năng , nhiệm vụ , quyền hạn và cơ cấu tổ chức của **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_THAM_QUYEN>`** ;

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **11/2015/TT-BKHĐT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[4:8]`)
- `[e3]` **Nghị định số 116/2008/NĐ-CP** → `THAM_CHIEU_PHAP_LY` (span: `[10:13]`)
- `[e4]` **Căn cứ** → `TU_KHOA_PHAP_LY` (span: `[9:10]`)
- `[e5]` **ngày 14 tháng 11 năm 2008** → `NGAY_THAM_CHIEU` (span: `[13:19]`)
- `[e6]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[20:21]`)
- `[e7]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_THAM_QUYEN` (span: `[31:35]`)

**Quan hệ:**
- (`e1` 11/2015/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 11/2015/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e4` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Nghị định số 116/2008/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 11/2015/TT-BKHĐT `[SO_HIEU]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Nghị định số 116/2008/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e3` Nghị định số 116/2008/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e5` ngày 14 tháng 11 năm 2008 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #11_2015_TT-BKHĐT_92514#preamble_standalone_10 (Loại: `preamble_standalone`)
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

### Mẫu #11_2015_TT-BKHĐT_92514#preamble_context_11 (Loại: `preamble_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[11/2015/TT-BKHĐT]`<SO_HIEU>`** của **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** . **[Bộ trưởng Bộ Kế hoạch và Đầu tư]`<CO_QUAN_THAM_QUYEN>`** ban hành Thông tư quy định chi tiết việc lập **[hồ sơ yêu cầu]`<GIAY_TO_HO_SO>`** đối với chỉ định thầu , chào hàng cạnh tranh .

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **11/2015/TT-BKHĐT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[4:8]`)
- `[e3]` **Bộ trưởng Bộ Kế hoạch và Đầu tư** → `CO_QUAN_THAM_QUYEN` (span: `[9:14]`)
- `[e4]` **hồ sơ yêu cầu** → `GIAY_TO_HO_SO` (span: `[20:22]`)

**Quan hệ:**
- (`e1` 11/2015/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 11/2015/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)


---

### Mẫu #11_2015_TT-BKHĐT_92514#preamble_standalone_12 (Loại: `preamble_standalone`)
> **[Bộ trưởng Bộ Kế hoạch và Đầu tư]`<CO_QUAN_THAM_QUYEN>`** ban hành Thông tư quy định chi tiết việc lập **[hồ sơ yêu cầu]`<GIAY_TO_HO_SO>`** đối với chỉ định thầu , chào hàng cạnh tranh .

**Thực thể:**
- `[e0]` **Bộ trưởng Bộ Kế hoạch và Đầu tư** → `CO_QUAN_THAM_QUYEN` (span: `[0:5]`)
- `[e1]` **hồ sơ yêu cầu** → `GIAY_TO_HO_SO` (span: `[11:13]`)


---

### Mẫu #11_2015_TT-BKHĐT_92514#body_context_13 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[11/2015/TT-BKHĐT]`<SO_HIEU>`** ban hành **[ngày 27 tháng 10 năm 2015]`<NGAY_BAN_HANH>`** bởi **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** . **[Điều 1 . Phạm vi điều chỉnh . Thông tư này quy định chi tiết về lập **[hồ sơ yêu cầu]`<GIAY_TO_HO_SO>`** đối với gói thầu thuộc phạm vi điều chỉnh **[quy định tại]`<TU_KHOA_PHAP_LY>`** **[Điều 1]`<THAM_CHIEU_PHAP_LY>`** **[Luật đấu thầu số 43/2013/QH13]`<THAM_CHIEU_PHAP_LY>`** như sau :]`<DIEU>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **11/2015/TT-BKHĐT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[11:15]`)
- `[e3]` **ngày 27 tháng 10 năm 2015** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 1 . Phạm vi điều chỉnh . Thông tư này quy định chi tiết về lập hồ sơ yêu cầu đối với gói thầu thuộc phạm vi điều chỉnh quy định tại Điều 1 Luật đấu thầu số 43/2013/QH13 như sau :** → `DIEU` (span: `[16:46]`)
- `[e5]` **Điều 1** → `THAM_CHIEU_PHAP_LY` (span: `[37:39]`) *(lồng trong `e4` (`DIEU`))*
- `[e6]` **Luật đấu thầu số 43/2013/QH13** → `THAM_CHIEU_PHAP_LY` (span: `[39:43]`) *(lồng trong `e4` (`DIEU`))*
- `[e7]` **quy định tại** → `TU_KHOA_PHAP_LY` (span: `[35:37]`) *(lồng trong `e4` (`DIEU`))*
- `[e8]` **hồ sơ yêu cầu** → `GIAY_TO_HO_SO` (span: `[28:30]`) *(lồng trong `e4` (`DIEU`))*

**Quan hệ:**
- (`e1` 11/2015/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 11/2015/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 11/2015/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 27 tháng 10 năm 2015 `[NGAY_BAN_HANH]`)
- (`e4` Điều 1 . Phạm vi điều chỉnh . Thông tư này quy định chi tiết về lập hồ sơ yêu cầu đối với gói thầu thuộc phạm vi điều chỉnh quy định tại Điều 1 Luật đấu thầu số 43/2013/QH13 như sau : `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 11/2015/TT-BKHĐT `[SO_HIEU]`)
- (`e7` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e5` Điều 1 `[THAM_CHIEU_PHAP_LY]`)
- (`e4` Điều 1 . Phạm vi điều chỉnh . Thông tư này quy định chi tiết về lập hồ sơ yêu cầu đối với gói thầu thuộc phạm vi điều chỉnh quy định tại Điều 1 Luật đấu thầu số 43/2013/QH13 như sau : `[DIEU]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e5` Điều 1 `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e7` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e6` Luật đấu thầu số 43/2013/QH13 `[THAM_CHIEU_PHAP_LY]`)
- (`e4` Điều 1 . Phạm vi điều chỉnh . Thông tư này quy định chi tiết về lập hồ sơ yêu cầu đối với gói thầu thuộc phạm vi điều chỉnh quy định tại Điều 1 Luật đấu thầu số 43/2013/QH13 như sau : `[DIEU]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e6` Luật đấu thầu số 43/2013/QH13 `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #11_2015_TT-BKHĐT_92514#body_standalone_14 (Loại: `body_standalone`)
> **[Điều 1 . Phạm vi điều chỉnh . Thông tư này quy định chi tiết về lập **[hồ sơ yêu cầu]`<GIAY_TO_HO_SO>`** đối với gói thầu thuộc phạm vi điều chỉnh **[quy định tại]`<TU_KHOA_PHAP_LY>`** **[Điều 1]`<THAM_CHIEU_PHAP_LY>`** **[Luật đấu thầu số 43/2013/QH13]`<THAM_CHIEU_PHAP_LY>`** như sau :]`<DIEU>`**

**Thực thể:**
- `[e0]` **Điều 1 . Phạm vi điều chỉnh . Thông tư này quy định chi tiết về lập hồ sơ yêu cầu đối với gói thầu thuộc phạm vi điều chỉnh quy định tại Điều 1 Luật đấu thầu số 43/2013/QH13 như sau :** → `DIEU` (span: `[0:30]`)
- `[e1]` **Điều 1** → `THAM_CHIEU_PHAP_LY` (span: `[21:23]`) *(lồng trong `e0` (`DIEU`))*
- `[e2]` **Luật đấu thầu số 43/2013/QH13** → `THAM_CHIEU_PHAP_LY` (span: `[23:27]`) *(lồng trong `e0` (`DIEU`))*
- `[e3]` **quy định tại** → `TU_KHOA_PHAP_LY` (span: `[19:21]`) *(lồng trong `e0` (`DIEU`))*
- `[e4]` **hồ sơ yêu cầu** → `GIAY_TO_HO_SO` (span: `[12:14]`) *(lồng trong `e0` (`DIEU`))*

**Quan hệ:**
- (`e3` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e1` Điều 1 `[THAM_CHIEU_PHAP_LY]`)
- (`e0` Điều 1 . Phạm vi điều chỉnh . Thông tư này quy định chi tiết về lập hồ sơ yêu cầu đối với gói thầu thuộc phạm vi điều chỉnh quy định tại Điều 1 Luật đấu thầu số 43/2013/QH13 như sau : `[DIEU]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e1` Điều 1 `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e3` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e2` Luật đấu thầu số 43/2013/QH13 `[THAM_CHIEU_PHAP_LY]`)
- (`e0` Điều 1 . Phạm vi điều chỉnh . Thông tư này quy định chi tiết về lập hồ sơ yêu cầu đối với gói thầu thuộc phạm vi điều chỉnh quy định tại Điều 1 Luật đấu thầu số 43/2013/QH13 như sau : `[DIEU]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e2` Luật đấu thầu số 43/2013/QH13 `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #11_2015_TT-BKHĐT_92514#body_context_15 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[11/2015/TT-BKHĐT]`<SO_HIEU>`** ban hành **[ngày 27 tháng 10 năm 2015]`<NGAY_BAN_HANH>`** bởi **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** . **[Điều 1]`<DIEU>`** . **[1 . Mẫu **[hồ sơ yêu cầu]`<GIAY_TO_HO_SO>`** áp dụng cho gói thầu xây lắp thực hiện chỉ định thầu trong nước theo quy trình thông thường ( **[Mẫu số 01]`<THAM_CHIEU_PHAP_LY>`** - **[Hồ sơ yêu cầu]`<GIAY_TO_HO_SO>`** chỉ định thầu xây lắp ) ;]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **11/2015/TT-BKHĐT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[11:15]`)
- `[e3]` **ngày 27 tháng 10 năm 2015** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 1** → `DIEU` (span: `[16:18]`)
- `[e5]` **1 . Mẫu hồ sơ yêu cầu áp dụng cho gói thầu xây lắp thực hiện chỉ định thầu trong nước theo quy trình thông thường ( Mẫu số 01 - Hồ sơ yêu cầu chỉ định thầu xây lắp ) ;** → `KHOAN` (span: `[19:47]`)
- `[e6]` **Mẫu số 01** → `THAM_CHIEU_PHAP_LY` (span: `[37:39]`) *(lồng trong `e5` (`KHOAN`))*
- `[e7]` **hồ sơ yêu cầu** → `GIAY_TO_HO_SO` (span: `[22:24]`) *(lồng trong `e5` (`KHOAN`))*
- `[e8]` **Hồ sơ yêu cầu** → `GIAY_TO_HO_SO` (span: `[40:42]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 11/2015/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 11/2015/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 11/2015/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 27 tháng 10 năm 2015 `[NGAY_BAN_HANH]`)
- (`e4` Điều 1 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 11/2015/TT-BKHĐT `[SO_HIEU]`)
- (`e5` 1 . Mẫu hồ sơ yêu cầu áp dụng cho gói thầu xây lắp thực hiện chỉ định thầu trong nước theo quy trình thông thường ( Mẫu số 01 - Hồ sơ yêu cầu chỉ định thầu xây lắp ) ; `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 1 `[DIEU]`)
- (`e5` 1 . Mẫu hồ sơ yêu cầu áp dụng cho gói thầu xây lắp thực hiện chỉ định thầu trong nước theo quy trình thông thường ( Mẫu số 01 - Hồ sơ yêu cầu chỉ định thầu xây lắp ) ; `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e6` Mẫu số 01 `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #11_2015_TT-BKHĐT_92514#body_standalone_16 (Loại: `body_standalone`)
> **[Điều 1]`<DIEU>`** . **[1 . Mẫu **[hồ sơ yêu cầu]`<GIAY_TO_HO_SO>`** áp dụng cho gói thầu xây lắp thực hiện chỉ định thầu trong nước theo quy trình thông thường ( **[Mẫu số 01]`<THAM_CHIEU_PHAP_LY>`** - **[Hồ sơ yêu cầu]`<GIAY_TO_HO_SO>`** chỉ định thầu xây lắp ) ;]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 1** → `DIEU` (span: `[0:2]`)
- `[e1]` **1 . Mẫu hồ sơ yêu cầu áp dụng cho gói thầu xây lắp thực hiện chỉ định thầu trong nước theo quy trình thông thường ( Mẫu số 01 - Hồ sơ yêu cầu chỉ định thầu xây lắp ) ;** → `KHOAN` (span: `[3:31]`)
- `[e2]` **Mẫu số 01** → `THAM_CHIEU_PHAP_LY` (span: `[21:23]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **hồ sơ yêu cầu** → `GIAY_TO_HO_SO` (span: `[6:8]`) *(lồng trong `e1` (`KHOAN`))*
- `[e4]` **Hồ sơ yêu cầu** → `GIAY_TO_HO_SO` (span: `[24:26]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 1 . Mẫu hồ sơ yêu cầu áp dụng cho gói thầu xây lắp thực hiện chỉ định thầu trong nước theo quy trình thông thường ( Mẫu số 01 - Hồ sơ yêu cầu chỉ định thầu xây lắp ) ; `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 1 `[DIEU]`)
- (`e1` 1 . Mẫu hồ sơ yêu cầu áp dụng cho gói thầu xây lắp thực hiện chỉ định thầu trong nước theo quy trình thông thường ( Mẫu số 01 - Hồ sơ yêu cầu chỉ định thầu xây lắp ) ; `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e2` Mẫu số 01 `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #11_2015_TT-BKHĐT_92514#body_context_17 (Loại: `body_context`)
> **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[11/2015/TT-BKHĐT]`<SO_HIEU>`** . **[Điều 1]`<DIEU>`** . **[2 . Mẫu **[hồ sơ yêu cầu]`<GIAY_TO_HO_SO>`** áp dụng cho gói thầu mua sắm **[hàng hóa]`<TAI_SAN_VAT_CHAT>`** thực hiện chỉ định thầu trong nước theo quy trình thông thường ( **[Mẫu số 02]`<THAM_CHIEU_PHAP_LY>`** - **[Hồ sơ yêu cầu]`<GIAY_TO_HO_SO>`** chỉ định thầu mua sắm **[hàng hóa]`<TAI_SAN_VAT_CHAT>`** ) ;]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[5:6]`)
- `[e1]` **11/2015/TT-BKHĐT** → `SO_HIEU` (span: `[7:8]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[0:4]`)
- `[e3]` **Điều 1** → `DIEU` (span: `[9:11]`)
- `[e4]` **2 . Mẫu hồ sơ yêu cầu áp dụng cho gói thầu mua sắm hàng hóa thực hiện chỉ định thầu trong nước theo quy trình thông thường ( Mẫu số 02 - Hồ sơ yêu cầu chỉ định thầu mua sắm hàng hóa ) ;** → `KHOAN` (span: `[12:42]`)
- `[e5]` **Mẫu số 02** → `THAM_CHIEU_PHAP_LY` (span: `[31:33]`) *(lồng trong `e4` (`KHOAN`))*
- `[e6]` **hồ sơ yêu cầu** → `GIAY_TO_HO_SO` (span: `[15:17]`) *(lồng trong `e4` (`KHOAN`))*
- `[e7]` **Hồ sơ yêu cầu** → `GIAY_TO_HO_SO` (span: `[34:36]`) *(lồng trong `e4` (`KHOAN`))*
- `[e8]` **hàng hóa** → `TAI_SAN_VAT_CHAT` (span: `[21:22]`) *(lồng trong `e4` (`KHOAN`))*
- `[e9]` **hàng hóa** → `TAI_SAN_VAT_CHAT` (span: `[39:40]`) *(lồng trong `e4` (`KHOAN`))*

**Quan hệ:**
- (`e1` 11/2015/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 11/2015/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 1 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 11/2015/TT-BKHĐT `[SO_HIEU]`)
- (`e4` 2 . Mẫu hồ sơ yêu cầu áp dụng cho gói thầu mua sắm hàng hóa thực hiện chỉ định thầu trong nước theo quy trình thông thường ( Mẫu số 02 - Hồ sơ yêu cầu chỉ định thầu mua sắm hàng hóa ) ; `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 1 `[DIEU]`)
- (`e4` 2 . Mẫu hồ sơ yêu cầu áp dụng cho gói thầu mua sắm hàng hóa thực hiện chỉ định thầu trong nước theo quy trình thông thường ( Mẫu số 02 - Hồ sơ yêu cầu chỉ định thầu mua sắm hàng hóa ) ; `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e5` Mẫu số 02 `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #11_2015_TT-BKHĐT_92514#body_standalone_18 (Loại: `body_standalone`)
> **[Điều 1]`<DIEU>`** . **[2 . Mẫu **[hồ sơ yêu cầu]`<GIAY_TO_HO_SO>`** áp dụng cho gói thầu mua sắm **[hàng hóa]`<TAI_SAN_VAT_CHAT>`** thực hiện chỉ định thầu trong nước theo quy trình thông thường ( **[Mẫu số 02]`<THAM_CHIEU_PHAP_LY>`** - **[Hồ sơ yêu cầu]`<GIAY_TO_HO_SO>`** chỉ định thầu mua sắm **[hàng hóa]`<TAI_SAN_VAT_CHAT>`** ) ;]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 1** → `DIEU` (span: `[0:2]`)
- `[e1]` **2 . Mẫu hồ sơ yêu cầu áp dụng cho gói thầu mua sắm hàng hóa thực hiện chỉ định thầu trong nước theo quy trình thông thường ( Mẫu số 02 - Hồ sơ yêu cầu chỉ định thầu mua sắm hàng hóa ) ;** → `KHOAN` (span: `[3:33]`)
- `[e2]` **Mẫu số 02** → `THAM_CHIEU_PHAP_LY` (span: `[22:24]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **hồ sơ yêu cầu** → `GIAY_TO_HO_SO` (span: `[6:8]`) *(lồng trong `e1` (`KHOAN`))*
- `[e4]` **Hồ sơ yêu cầu** → `GIAY_TO_HO_SO` (span: `[25:27]`) *(lồng trong `e1` (`KHOAN`))*
- `[e5]` **hàng hóa** → `TAI_SAN_VAT_CHAT` (span: `[12:13]`) *(lồng trong `e1` (`KHOAN`))*
- `[e6]` **hàng hóa** → `TAI_SAN_VAT_CHAT` (span: `[30:31]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 2 . Mẫu hồ sơ yêu cầu áp dụng cho gói thầu mua sắm hàng hóa thực hiện chỉ định thầu trong nước theo quy trình thông thường ( Mẫu số 02 - Hồ sơ yêu cầu chỉ định thầu mua sắm hàng hóa ) ; `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 1 `[DIEU]`)
- (`e1` 2 . Mẫu hồ sơ yêu cầu áp dụng cho gói thầu mua sắm hàng hóa thực hiện chỉ định thầu trong nước theo quy trình thông thường ( Mẫu số 02 - Hồ sơ yêu cầu chỉ định thầu mua sắm hàng hóa ) ; `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e2` Mẫu số 02 `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #11_2015_TT-BKHĐT_92514#body_context_19 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[11/2015/TT-BKHĐT]`<SO_HIEU>`** ban hành **[ngày 27 tháng 10 năm 2015]`<NGAY_BAN_HANH>`** bởi **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** . **[Điều 1]`<DIEU>`** . **[3 . Mẫu **[hồ sơ yêu cầu]`<GIAY_TO_HO_SO>`** áp dụng cho gói thầu xây lắp thực hiện chào hàng cạnh tranh trong nước theo quy trình thông thường ( **[Mẫu số 03]`<THAM_CHIEU_PHAP_LY>`** - **[Hồ sơ yêu cầu]`<GIAY_TO_HO_SO>`** chào hàng cạnh tranh xây lắp ) ;]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **11/2015/TT-BKHĐT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[11:15]`)
- `[e3]` **ngày 27 tháng 10 năm 2015** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 1** → `DIEU` (span: `[16:18]`)
- `[e5]` **3 . Mẫu hồ sơ yêu cầu áp dụng cho gói thầu xây lắp thực hiện chào hàng cạnh tranh trong nước theo quy trình thông thường ( Mẫu số 03 - Hồ sơ yêu cầu chào hàng cạnh tranh xây lắp ) ;** → `KHOAN` (span: `[19:47]`)
- `[e6]` **Mẫu số 03** → `THAM_CHIEU_PHAP_LY` (span: `[37:39]`) *(lồng trong `e5` (`KHOAN`))*
- `[e7]` **hồ sơ yêu cầu** → `GIAY_TO_HO_SO` (span: `[22:24]`) *(lồng trong `e5` (`KHOAN`))*
- `[e8]` **Hồ sơ yêu cầu** → `GIAY_TO_HO_SO` (span: `[40:42]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 11/2015/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 11/2015/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 11/2015/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 27 tháng 10 năm 2015 `[NGAY_BAN_HANH]`)
- (`e4` Điều 1 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 11/2015/TT-BKHĐT `[SO_HIEU]`)
- (`e5` 3 . Mẫu hồ sơ yêu cầu áp dụng cho gói thầu xây lắp thực hiện chào hàng cạnh tranh trong nước theo quy trình thông thường ( Mẫu số 03 - Hồ sơ yêu cầu chào hàng cạnh tranh xây lắp ) ; `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 1 `[DIEU]`)
- (`e5` 3 . Mẫu hồ sơ yêu cầu áp dụng cho gói thầu xây lắp thực hiện chào hàng cạnh tranh trong nước theo quy trình thông thường ( Mẫu số 03 - Hồ sơ yêu cầu chào hàng cạnh tranh xây lắp ) ; `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e6` Mẫu số 03 `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #11_2015_TT-BKHĐT_92514#body_standalone_20 (Loại: `body_standalone`)
> **[Điều 1]`<DIEU>`** . **[3 . Mẫu **[hồ sơ yêu cầu]`<GIAY_TO_HO_SO>`** áp dụng cho gói thầu xây lắp thực hiện chào hàng cạnh tranh trong nước theo quy trình thông thường ( **[Mẫu số 03]`<THAM_CHIEU_PHAP_LY>`** - **[Hồ sơ yêu cầu]`<GIAY_TO_HO_SO>`** chào hàng cạnh tranh xây lắp ) ;]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 1** → `DIEU` (span: `[0:2]`)
- `[e1]` **3 . Mẫu hồ sơ yêu cầu áp dụng cho gói thầu xây lắp thực hiện chào hàng cạnh tranh trong nước theo quy trình thông thường ( Mẫu số 03 - Hồ sơ yêu cầu chào hàng cạnh tranh xây lắp ) ;** → `KHOAN` (span: `[3:31]`)
- `[e2]` **Mẫu số 03** → `THAM_CHIEU_PHAP_LY` (span: `[21:23]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **hồ sơ yêu cầu** → `GIAY_TO_HO_SO` (span: `[6:8]`) *(lồng trong `e1` (`KHOAN`))*
- `[e4]` **Hồ sơ yêu cầu** → `GIAY_TO_HO_SO` (span: `[24:26]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 3 . Mẫu hồ sơ yêu cầu áp dụng cho gói thầu xây lắp thực hiện chào hàng cạnh tranh trong nước theo quy trình thông thường ( Mẫu số 03 - Hồ sơ yêu cầu chào hàng cạnh tranh xây lắp ) ; `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 1 `[DIEU]`)
- (`e1` 3 . Mẫu hồ sơ yêu cầu áp dụng cho gói thầu xây lắp thực hiện chào hàng cạnh tranh trong nước theo quy trình thông thường ( Mẫu số 03 - Hồ sơ yêu cầu chào hàng cạnh tranh xây lắp ) ; `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e2` Mẫu số 03 `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #11_2015_TT-BKHĐT_92514#body_context_21 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[11/2015/TT-BKHĐT]`<SO_HIEU>`** ban hành **[ngày 27 tháng 10 năm 2015]`<NGAY_BAN_HANH>`** bởi **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** . **[Điều 1]`<DIEU>`** . **[4 . Mẫu **[hồ sơ yêu cầu]`<GIAY_TO_HO_SO>`** áp dụng cho gói thầu mua sắm **[hàng hóa]`<TAI_SAN_VAT_CHAT>`** thực hiện chào hàng cạnh tranh trong nước theo quy trình thông thường ( **[Mẫu số 04]`<THAM_CHIEU_PHAP_LY>`** - **[Hồ sơ yêu cầu]`<GIAY_TO_HO_SO>`** chào hàng cạnh tranh mua sắm **[hàng hóa]`<TAI_SAN_VAT_CHAT>`** ) ;]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **11/2015/TT-BKHĐT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[11:15]`)
- `[e3]` **ngày 27 tháng 10 năm 2015** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 1** → `DIEU` (span: `[16:18]`)
- `[e5]` **4 . Mẫu hồ sơ yêu cầu áp dụng cho gói thầu mua sắm hàng hóa thực hiện chào hàng cạnh tranh trong nước theo quy trình thông thường ( Mẫu số 04 - Hồ sơ yêu cầu chào hàng cạnh tranh mua sắm hàng hóa ) ;** → `KHOAN` (span: `[19:49]`)
- `[e6]` **Mẫu số 04** → `THAM_CHIEU_PHAP_LY` (span: `[38:40]`) *(lồng trong `e5` (`KHOAN`))*
- `[e7]` **hồ sơ yêu cầu** → `GIAY_TO_HO_SO` (span: `[22:24]`) *(lồng trong `e5` (`KHOAN`))*
- `[e8]` **Hồ sơ yêu cầu** → `GIAY_TO_HO_SO` (span: `[41:43]`) *(lồng trong `e5` (`KHOAN`))*
- `[e9]` **hàng hóa** → `TAI_SAN_VAT_CHAT` (span: `[28:29]`) *(lồng trong `e5` (`KHOAN`))*
- `[e10]` **hàng hóa** → `TAI_SAN_VAT_CHAT` (span: `[46:47]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 11/2015/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 11/2015/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 11/2015/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 27 tháng 10 năm 2015 `[NGAY_BAN_HANH]`)
- (`e4` Điều 1 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 11/2015/TT-BKHĐT `[SO_HIEU]`)
- (`e5` 4 . Mẫu hồ sơ yêu cầu áp dụng cho gói thầu mua sắm hàng hóa thực hiện chào hàng cạnh tranh trong nước theo quy trình thông thường ( Mẫu số 04 - Hồ sơ yêu cầu chào hàng cạnh tranh mua sắm hàng hóa ) ; `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 1 `[DIEU]`)
- (`e5` 4 . Mẫu hồ sơ yêu cầu áp dụng cho gói thầu mua sắm hàng hóa thực hiện chào hàng cạnh tranh trong nước theo quy trình thông thường ( Mẫu số 04 - Hồ sơ yêu cầu chào hàng cạnh tranh mua sắm hàng hóa ) ; `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e6` Mẫu số 04 `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #11_2015_TT-BKHĐT_92514#body_standalone_22 (Loại: `body_standalone`)
> **[Điều 1]`<DIEU>`** . **[4 . Mẫu **[hồ sơ yêu cầu]`<GIAY_TO_HO_SO>`** áp dụng cho gói thầu mua sắm **[hàng hóa]`<TAI_SAN_VAT_CHAT>`** thực hiện chào hàng cạnh tranh trong nước theo quy trình thông thường ( **[Mẫu số 04]`<THAM_CHIEU_PHAP_LY>`** - **[Hồ sơ yêu cầu]`<GIAY_TO_HO_SO>`** chào hàng cạnh tranh mua sắm **[hàng hóa]`<TAI_SAN_VAT_CHAT>`** ) ;]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 1** → `DIEU` (span: `[0:2]`)
- `[e1]` **4 . Mẫu hồ sơ yêu cầu áp dụng cho gói thầu mua sắm hàng hóa thực hiện chào hàng cạnh tranh trong nước theo quy trình thông thường ( Mẫu số 04 - Hồ sơ yêu cầu chào hàng cạnh tranh mua sắm hàng hóa ) ;** → `KHOAN` (span: `[3:33]`)
- `[e2]` **Mẫu số 04** → `THAM_CHIEU_PHAP_LY` (span: `[22:24]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **hồ sơ yêu cầu** → `GIAY_TO_HO_SO` (span: `[6:8]`) *(lồng trong `e1` (`KHOAN`))*
- `[e4]` **Hồ sơ yêu cầu** → `GIAY_TO_HO_SO` (span: `[25:27]`) *(lồng trong `e1` (`KHOAN`))*
- `[e5]` **hàng hóa** → `TAI_SAN_VAT_CHAT` (span: `[12:13]`) *(lồng trong `e1` (`KHOAN`))*
- `[e6]` **hàng hóa** → `TAI_SAN_VAT_CHAT` (span: `[30:31]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 4 . Mẫu hồ sơ yêu cầu áp dụng cho gói thầu mua sắm hàng hóa thực hiện chào hàng cạnh tranh trong nước theo quy trình thông thường ( Mẫu số 04 - Hồ sơ yêu cầu chào hàng cạnh tranh mua sắm hàng hóa ) ; `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 1 `[DIEU]`)
- (`e1` 4 . Mẫu hồ sơ yêu cầu áp dụng cho gói thầu mua sắm hàng hóa thực hiện chào hàng cạnh tranh trong nước theo quy trình thông thường ( Mẫu số 04 - Hồ sơ yêu cầu chào hàng cạnh tranh mua sắm hàng hóa ) ; `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e2` Mẫu số 04 `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #11_2015_TT-BKHĐT_92514#body_context_23 (Loại: `body_context`)
> **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[11/2015/TT-BKHĐT]`<SO_HIEU>`** . **[Điều 1]`<DIEU>`** . **[5 . Mẫu bản yêu cầu báo giá áp dụng cho gói thầu xây lắp , mua sắm **[hàng hóa]`<TAI_SAN_VAT_CHAT>`** thực hiện chào hàng cạnh tranh trong nước theo quy trình rút gọn ( **[Mẫu số 05]`<THAM_CHIEU_PHAP_LY>`** - Bản yêu cầu báo giá ) ;]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[5:6]`)
- `[e1]` **11/2015/TT-BKHĐT** → `SO_HIEU` (span: `[7:8]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[0:4]`)
- `[e3]` **Điều 1** → `DIEU` (span: `[9:11]`)
- `[e4]` **5 . Mẫu bản yêu cầu báo giá áp dụng cho gói thầu xây lắp , mua sắm hàng hóa thực hiện chào hàng cạnh tranh trong nước theo quy trình rút gọn ( Mẫu số 05 - Bản yêu cầu báo giá ) ;** → `KHOAN` (span: `[12:42]`)
- `[e5]` **Mẫu số 05** → `THAM_CHIEU_PHAP_LY` (span: `[34:36]`) *(lồng trong `e4` (`KHOAN`))*
- `[e6]` **hàng hóa** → `TAI_SAN_VAT_CHAT` (span: `[24:25]`) *(lồng trong `e4` (`KHOAN`))*

**Quan hệ:**
- (`e1` 11/2015/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 11/2015/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 1 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 11/2015/TT-BKHĐT `[SO_HIEU]`)
- (`e4` 5 . Mẫu bản yêu cầu báo giá áp dụng cho gói thầu xây lắp , mua sắm hàng hóa thực hiện chào hàng cạnh tranh trong nước theo quy trình rút gọn ( Mẫu số 05 - Bản yêu cầu báo giá ) ; `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 1 `[DIEU]`)
- (`e4` 5 . Mẫu bản yêu cầu báo giá áp dụng cho gói thầu xây lắp , mua sắm hàng hóa thực hiện chào hàng cạnh tranh trong nước theo quy trình rút gọn ( Mẫu số 05 - Bản yêu cầu báo giá ) ; `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e5` Mẫu số 05 `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #11_2015_TT-BKHĐT_92514#body_standalone_24 (Loại: `body_standalone`)
> **[Điều 1]`<DIEU>`** . **[5 . Mẫu bản yêu cầu báo giá áp dụng cho gói thầu xây lắp , mua sắm **[hàng hóa]`<TAI_SAN_VAT_CHAT>`** thực hiện chào hàng cạnh tranh trong nước theo quy trình rút gọn ( **[Mẫu số 05]`<THAM_CHIEU_PHAP_LY>`** - Bản yêu cầu báo giá ) ;]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 1** → `DIEU` (span: `[0:2]`)
- `[e1]` **5 . Mẫu bản yêu cầu báo giá áp dụng cho gói thầu xây lắp , mua sắm hàng hóa thực hiện chào hàng cạnh tranh trong nước theo quy trình rút gọn ( Mẫu số 05 - Bản yêu cầu báo giá ) ;** → `KHOAN` (span: `[3:33]`)
- `[e2]` **Mẫu số 05** → `THAM_CHIEU_PHAP_LY` (span: `[25:27]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **hàng hóa** → `TAI_SAN_VAT_CHAT` (span: `[15:16]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 5 . Mẫu bản yêu cầu báo giá áp dụng cho gói thầu xây lắp , mua sắm hàng hóa thực hiện chào hàng cạnh tranh trong nước theo quy trình rút gọn ( Mẫu số 05 - Bản yêu cầu báo giá ) ; `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 1 `[DIEU]`)
- (`e1` 5 . Mẫu bản yêu cầu báo giá áp dụng cho gói thầu xây lắp , mua sắm hàng hóa thực hiện chào hàng cạnh tranh trong nước theo quy trình rút gọn ( Mẫu số 05 - Bản yêu cầu báo giá ) ; `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e2` Mẫu số 05 `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #11_2015_TT-BKHĐT_92514#body_context_25 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[11/2015/TT-BKHĐT]`<SO_HIEU>`** ban hành **[ngày 27 tháng 10 năm 2015]`<NGAY_BAN_HANH>`** bởi **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** . **[Điều 1]`<DIEU>`** . **[6 . Mẫu dự thảo hợp đồng áp dụng cho gói thầu xây lắp , mua sắm **[hàng hóa]`<TAI_SAN_VAT_CHAT>`** thuộc hạn mức chỉ định thầu ( **[Mẫu số 06]`<THAM_CHIEU_PHAP_LY>`** - Dự thảo hợp đồng cho chỉ định thầu rút gọn ) .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **11/2015/TT-BKHĐT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[11:15]`)
- `[e3]` **ngày 27 tháng 10 năm 2015** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 1** → `DIEU` (span: `[16:18]`)
- `[e5]` **6 . Mẫu dự thảo hợp đồng áp dụng cho gói thầu xây lắp , mua sắm hàng hóa thuộc hạn mức chỉ định thầu ( Mẫu số 06 - Dự thảo hợp đồng cho chỉ định thầu rút gọn ) .** → `KHOAN` (span: `[19:47]`)
- `[e6]` **Mẫu số 06** → `THAM_CHIEU_PHAP_LY` (span: `[36:38]`) *(lồng trong `e5` (`KHOAN`))*
- `[e7]` **hàng hóa** → `TAI_SAN_VAT_CHAT` (span: `[30:31]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 11/2015/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 11/2015/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 11/2015/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 27 tháng 10 năm 2015 `[NGAY_BAN_HANH]`)
- (`e4` Điều 1 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 11/2015/TT-BKHĐT `[SO_HIEU]`)
- (`e5` 6 . Mẫu dự thảo hợp đồng áp dụng cho gói thầu xây lắp , mua sắm hàng hóa thuộc hạn mức chỉ định thầu ( Mẫu số 06 - Dự thảo hợp đồng cho chỉ định thầu rút gọn ) . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 1 `[DIEU]`)
- (`e5` 6 . Mẫu dự thảo hợp đồng áp dụng cho gói thầu xây lắp , mua sắm hàng hóa thuộc hạn mức chỉ định thầu ( Mẫu số 06 - Dự thảo hợp đồng cho chỉ định thầu rút gọn ) . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e6` Mẫu số 06 `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #11_2015_TT-BKHĐT_92514#body_standalone_26 (Loại: `body_standalone`)
> **[Điều 1]`<DIEU>`** . **[6 . Mẫu dự thảo hợp đồng áp dụng cho gói thầu xây lắp , mua sắm **[hàng hóa]`<TAI_SAN_VAT_CHAT>`** thuộc hạn mức chỉ định thầu ( **[Mẫu số 06]`<THAM_CHIEU_PHAP_LY>`** - Dự thảo hợp đồng cho chỉ định thầu rút gọn ) .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 1** → `DIEU` (span: `[0:2]`)
- `[e1]` **6 . Mẫu dự thảo hợp đồng áp dụng cho gói thầu xây lắp , mua sắm hàng hóa thuộc hạn mức chỉ định thầu ( Mẫu số 06 - Dự thảo hợp đồng cho chỉ định thầu rút gọn ) .** → `KHOAN` (span: `[3:31]`)
- `[e2]` **Mẫu số 06** → `THAM_CHIEU_PHAP_LY` (span: `[20:22]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **hàng hóa** → `TAI_SAN_VAT_CHAT` (span: `[14:15]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 6 . Mẫu dự thảo hợp đồng áp dụng cho gói thầu xây lắp , mua sắm hàng hóa thuộc hạn mức chỉ định thầu ( Mẫu số 06 - Dự thảo hợp đồng cho chỉ định thầu rút gọn ) . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 1 `[DIEU]`)
- (`e1` 6 . Mẫu dự thảo hợp đồng áp dụng cho gói thầu xây lắp , mua sắm hàng hóa thuộc hạn mức chỉ định thầu ( Mẫu số 06 - Dự thảo hợp đồng cho chỉ định thầu rút gọn ) . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e2` Mẫu số 06 `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #11_2015_TT-BKHĐT_92514#body_context_27 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[11/2015/TT-BKHĐT]`<SO_HIEU>`** của **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Đấu thầu]`<LINH_VUC>`** . **[Điều 2 . Đối tượng áp dụng . Thông tư này áp dụng đối với tổ chức , cá nhân tham gia hoặc có liên quan đến hoạt động lựa chọn nhà thầu gói thầu **[quy định tại]`<TU_KHOA_PHAP_LY>`** **[Điều 1 của Thông tư này]`<THAM_CHIEU_PHAP_LY>`** .]`<DIEU>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **11/2015/TT-BKHĐT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[4:8]`)
- `[e3]` **Đấu thầu** → `LINH_VUC` (span: `[10:11]`)
- `[e4]` **Điều 2 . Đối tượng áp dụng . Thông tư này áp dụng đối với tổ chức , cá nhân tham gia hoặc có liên quan đến hoạt động lựa chọn nhà thầu gói thầu quy định tại Điều 1 của Thông tư này .** → `DIEU` (span: `[12:42]`)
- `[e5]` **Điều 1 của Thông tư này** → `THAM_CHIEU_PHAP_LY` (span: `[36:41]`) *(lồng trong `e4` (`DIEU`))*
- `[e6]` **quy định tại** → `TU_KHOA_PHAP_LY` (span: `[34:36]`) *(lồng trong `e4` (`DIEU`))*

**Quan hệ:**
- (`e1` 11/2015/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 11/2015/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 11/2015/TT-BKHĐT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Đấu thầu `[LINH_VUC]`)
- (`e4` Điều 2 . Đối tượng áp dụng . Thông tư này áp dụng đối với tổ chức , cá nhân tham gia hoặc có liên quan đến hoạt động lựa chọn nhà thầu gói thầu quy định tại Điều 1 của Thông tư này . `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 11/2015/TT-BKHĐT `[SO_HIEU]`)
- (`e1` 11/2015/TT-BKHĐT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Đấu thầu `[LINH_VUC]`)
- (`e4` Điều 2 . Đối tượng áp dụng . Thông tư này áp dụng đối với tổ chức , cá nhân tham gia hoặc có liên quan đến hoạt động lựa chọn nhà thầu gói thầu quy định tại Điều 1 của Thông tư này . `[DIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Đấu thầu `[LINH_VUC]`)
- (`e6` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e5` Điều 1 của Thông tư này `[THAM_CHIEU_PHAP_LY]`)
- (`e4` Điều 2 . Đối tượng áp dụng . Thông tư này áp dụng đối với tổ chức , cá nhân tham gia hoặc có liên quan đến hoạt động lựa chọn nhà thầu gói thầu quy định tại Điều 1 của Thông tư này . `[DIEU]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e5` Điều 1 của Thông tư này `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #11_2015_TT-BKHĐT_92514#body_standalone_28 (Loại: `body_standalone`)
> **[Điều 2 . Đối tượng áp dụng . Thông tư này áp dụng đối với tổ chức , cá nhân tham gia hoặc có liên quan đến hoạt động lựa chọn nhà thầu gói thầu **[quy định tại]`<TU_KHOA_PHAP_LY>`** **[Điều 1 của Thông tư này]`<THAM_CHIEU_PHAP_LY>`** .]`<DIEU>`**

**Thực thể:**
- `[e0]` **Điều 2 . Đối tượng áp dụng . Thông tư này áp dụng đối với tổ chức , cá nhân tham gia hoặc có liên quan đến hoạt động lựa chọn nhà thầu gói thầu quy định tại Điều 1 của Thông tư này .** → `DIEU` (span: `[0:30]`)
- `[e1]` **Điều 1 của Thông tư này** → `THAM_CHIEU_PHAP_LY` (span: `[24:29]`) *(lồng trong `e0` (`DIEU`))*
- `[e2]` **quy định tại** → `TU_KHOA_PHAP_LY` (span: `[22:24]`) *(lồng trong `e0` (`DIEU`))*

**Quan hệ:**
- (`e2` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e1` Điều 1 của Thông tư này `[THAM_CHIEU_PHAP_LY]`)
- (`e0` Điều 2 . Đối tượng áp dụng . Thông tư này áp dụng đối với tổ chức , cá nhân tham gia hoặc có liên quan đến hoạt động lựa chọn nhà thầu gói thầu quy định tại Điều 1 của Thông tư này . `[DIEU]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e1` Điều 1 của Thông tư này `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #11_2015_TT-BKHĐT_92514#body_context_29 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[11/2015/TT-BKHĐT]`<SO_HIEU>`** ban hành **[ngày 27 tháng 10 năm 2015]`<NGAY_BAN_HANH>`** bởi **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** . **[Điều 3 . Áp dụng hình thức chỉ định thầu , chào hàng cạnh tranh và các Mẫu **[hồ sơ yêu cầu]`<GIAY_TO_HO_SO>`** , bản yêu cầu báo giá , dự thảo hợp đồng]`<DIEU>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **11/2015/TT-BKHĐT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[11:15]`)
- `[e3]` **ngày 27 tháng 10 năm 2015** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 3 . Áp dụng hình thức chỉ định thầu , chào hàng cạnh tranh và các Mẫu hồ sơ yêu cầu , bản yêu cầu báo giá , dự thảo hợp đồng** → `DIEU` (span: `[16:38]`)
- `[e5]` **hồ sơ yêu cầu** → `GIAY_TO_HO_SO` (span: `[29:31]`) *(lồng trong `e4` (`DIEU`))*

**Quan hệ:**
- (`e1` 11/2015/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 11/2015/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 11/2015/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 27 tháng 10 năm 2015 `[NGAY_BAN_HANH]`)
- (`e4` Điều 3 . Áp dụng hình thức chỉ định thầu , chào hàng cạnh tranh và các Mẫu hồ sơ yêu cầu , bản yêu cầu báo giá , dự thảo hợp đồng `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 11/2015/TT-BKHĐT `[SO_HIEU]`)


---

### Mẫu #11_2015_TT-BKHĐT_92514#body_context_30 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[11/2015/TT-BKHĐT]`<SO_HIEU>`** ban hành **[ngày 27 tháng 10 năm 2015]`<NGAY_BAN_HANH>`** bởi **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** . **[Điều 3]`<DIEU>`** . **[1 . Hình thức chỉ định thầu theo quy trình thông thường được áp dụng đối với gói thầu thuộc trường hợp chỉ định thầu **[quy định tại]`<TU_KHOA_PHAP_LY>`** **[các điểm b , c , d , đ và g]`<THAM_CHIEU_PHAP_LY>`** ói thầu cần thực hiện để bảo đảm bí mật nhà nước **[quy định tại]`<TU_KHOA_PHAP_LY>`** **[điểm a khoản 1 Điều 22]`<THAM_CHIEU_PHAP_LY>`** **[Luật đấu thầu số 43/2013/QH13]`<THAM_CHIEU_PHAP_LY>`** , đồng thời đáp ứng các điều kiện **[quy định tại]`<TU_KHOA_PHAP_LY>`** **[khoản 2 Điều 22]`<THAM_CHIEU_PHAP_LY>`** **[Luật đấu thầu số 43/2013/QH13]`<THAM_CHIEU_PHAP_LY>`** . Hình thức chỉ định thầu theo quy trình rút gọn được]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **11/2015/TT-BKHĐT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[11:15]`)
- `[e3]` **ngày 27 tháng 10 năm 2015** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 3** → `DIEU` (span: `[16:18]`)
- `[e5]` **1 . Hình thức chỉ định thầu theo quy trình thông thường được áp dụng đối với gói thầu thuộc trường hợp chỉ định thầu quy định tại các điểm b , c , d , đ và g ói thầu cần thực hiện để bảo đảm bí mật nhà nước quy định tại điểm a khoản 1 Điều 22 Luật đấu thầu số 43/2013/QH13 , đồng thời đáp ứng các điều kiện quy định tại khoản 2 Điều 22 Luật đấu thầu số 43/2013/QH13 . Hình thức chỉ định thầu theo quy trình rút gọn được** → `KHOAN` (span: `[19:91]`)
- `[e6]` **các điểm b , c , d , đ và g** → `THAM_CHIEU_PHAP_LY` (span: `[37:48]`) *(lồng trong `e5` (`KHOAN`))*
- `[e7]` **điểm a khoản 1 Điều 22** → `THAM_CHIEU_PHAP_LY` (span: `[58:64]`) *(lồng trong `e5` (`KHOAN`))*
- `[e8]` **Luật đấu thầu số 43/2013/QH13** → `THAM_CHIEU_PHAP_LY` (span: `[64:68]`) *(lồng trong `e5` (`KHOAN`))*
- `[e9]` **khoản 2 Điều 22** → `THAM_CHIEU_PHAP_LY` (span: `[75:79]`) *(lồng trong `e5` (`KHOAN`))*
- `[e10]` **Luật đấu thầu số 43/2013/QH13** → `THAM_CHIEU_PHAP_LY` (span: `[79:83]`) *(lồng trong `e5` (`KHOAN`))*
- `[e11]` **quy định tại** → `TU_KHOA_PHAP_LY` (span: `[35:37]`) *(lồng trong `e5` (`KHOAN`))*
- `[e12]` **quy định tại** → `TU_KHOA_PHAP_LY` (span: `[56:58]`) *(lồng trong `e5` (`KHOAN`))*
- `[e13]` **quy định tại** → `TU_KHOA_PHAP_LY` (span: `[73:75]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 11/2015/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 11/2015/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 11/2015/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 27 tháng 10 năm 2015 `[NGAY_BAN_HANH]`)
- (`e4` Điều 3 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 11/2015/TT-BKHĐT `[SO_HIEU]`)
- (`e5` 1 . Hình thức chỉ định thầu theo quy trình thông thường được áp dụng đối với gói thầu thuộc trường hợp chỉ định thầu quy định tại các điểm b , c , d , đ và g ói thầu cần thực hiện để bảo đảm bí mật nhà nước quy định tại điểm a khoản 1 Điều 22 Luật đấu thầu số 43/2013/QH13 , đồng thời đáp ứng các điều kiện quy định tại khoản 2 Điều 22 Luật đấu thầu số 43/2013/QH13 . Hình thức chỉ định thầu theo quy trình rút gọn được `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 3 `[DIEU]`)
- (`e11` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e6` các điểm b , c , d , đ và g `[THAM_CHIEU_PHAP_LY]`)
- (`e5` 1 . Hình thức chỉ định thầu theo quy trình thông thường được áp dụng đối với gói thầu thuộc trường hợp chỉ định thầu quy định tại các điểm b , c , d , đ và g ói thầu cần thực hiện để bảo đảm bí mật nhà nước quy định tại điểm a khoản 1 Điều 22 Luật đấu thầu số 43/2013/QH13 , đồng thời đáp ứng các điều kiện quy định tại khoản 2 Điều 22 Luật đấu thầu số 43/2013/QH13 . Hình thức chỉ định thầu theo quy trình rút gọn được `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e6` các điểm b , c , d , đ và g `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e12` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e7` điểm a khoản 1 Điều 22 `[THAM_CHIEU_PHAP_LY]`)
- (`e5` 1 . Hình thức chỉ định thầu theo quy trình thông thường được áp dụng đối với gói thầu thuộc trường hợp chỉ định thầu quy định tại các điểm b , c , d , đ và g ói thầu cần thực hiện để bảo đảm bí mật nhà nước quy định tại điểm a khoản 1 Điều 22 Luật đấu thầu số 43/2013/QH13 , đồng thời đáp ứng các điều kiện quy định tại khoản 2 Điều 22 Luật đấu thầu số 43/2013/QH13 . Hình thức chỉ định thầu theo quy trình rút gọn được `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e7` điểm a khoản 1 Điều 22 `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e12` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e8` Luật đấu thầu số 43/2013/QH13 `[THAM_CHIEU_PHAP_LY]`)
- (`e5` 1 . Hình thức chỉ định thầu theo quy trình thông thường được áp dụng đối với gói thầu thuộc trường hợp chỉ định thầu quy định tại các điểm b , c , d , đ và g ói thầu cần thực hiện để bảo đảm bí mật nhà nước quy định tại điểm a khoản 1 Điều 22 Luật đấu thầu số 43/2013/QH13 , đồng thời đáp ứng các điều kiện quy định tại khoản 2 Điều 22 Luật đấu thầu số 43/2013/QH13 . Hình thức chỉ định thầu theo quy trình rút gọn được `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e8` Luật đấu thầu số 43/2013/QH13 `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e13` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e9` khoản 2 Điều 22 `[THAM_CHIEU_PHAP_LY]`)
- (`e5` 1 . Hình thức chỉ định thầu theo quy trình thông thường được áp dụng đối với gói thầu thuộc trường hợp chỉ định thầu quy định tại các điểm b , c , d , đ và g ói thầu cần thực hiện để bảo đảm bí mật nhà nước quy định tại điểm a khoản 1 Điều 22 Luật đấu thầu số 43/2013/QH13 , đồng thời đáp ứng các điều kiện quy định tại khoản 2 Điều 22 Luật đấu thầu số 43/2013/QH13 . Hình thức chỉ định thầu theo quy trình rút gọn được `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e9` khoản 2 Điều 22 `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e13` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e10` Luật đấu thầu số 43/2013/QH13 `[THAM_CHIEU_PHAP_LY]`)
- (`e5` 1 . Hình thức chỉ định thầu theo quy trình thông thường được áp dụng đối với gói thầu thuộc trường hợp chỉ định thầu quy định tại các điểm b , c , d , đ và g ói thầu cần thực hiện để bảo đảm bí mật nhà nước quy định tại điểm a khoản 1 Điều 22 Luật đấu thầu số 43/2013/QH13 , đồng thời đáp ứng các điều kiện quy định tại khoản 2 Điều 22 Luật đấu thầu số 43/2013/QH13 . Hình thức chỉ định thầu theo quy trình rút gọn được `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e10` Luật đấu thầu số 43/2013/QH13 `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #11_2015_TT-BKHĐT_92514#body_standalone_31 (Loại: `body_standalone`)
> **[Điều 3]`<DIEU>`** . **[1 . Hình thức chỉ định thầu theo quy trình thông thường được áp dụng đối với gói thầu thuộc trường hợp chỉ định thầu **[quy định tại]`<TU_KHOA_PHAP_LY>`** **[các điểm b , c , d , đ và g]`<THAM_CHIEU_PHAP_LY>`** ói thầu cần thực hiện để bảo đảm bí mật nhà nước **[quy định tại]`<TU_KHOA_PHAP_LY>`** **[điểm a khoản 1 Điều 22]`<THAM_CHIEU_PHAP_LY>`** **[Luật đấu thầu số 43/2013/QH13]`<THAM_CHIEU_PHAP_LY>`** , đồng thời đáp ứng các điều kiện **[quy định tại]`<TU_KHOA_PHAP_LY>`** **[khoản 2 Điều 22]`<THAM_CHIEU_PHAP_LY>`** **[Luật đấu thầu số 43/2013/QH13]`<THAM_CHIEU_PHAP_LY>`** . Hình thức chỉ định thầu theo quy trình rút gọn được]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 3** → `DIEU` (span: `[0:2]`)
- `[e1]` **1 . Hình thức chỉ định thầu theo quy trình thông thường được áp dụng đối với gói thầu thuộc trường hợp chỉ định thầu quy định tại các điểm b , c , d , đ và g ói thầu cần thực hiện để bảo đảm bí mật nhà nước quy định tại điểm a khoản 1 Điều 22 Luật đấu thầu số 43/2013/QH13 , đồng thời đáp ứng các điều kiện quy định tại khoản 2 Điều 22 Luật đấu thầu số 43/2013/QH13 . Hình thức chỉ định thầu theo quy trình rút gọn được** → `KHOAN` (span: `[3:75]`)
- `[e2]` **các điểm b , c , d , đ và g** → `THAM_CHIEU_PHAP_LY` (span: `[21:32]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **điểm a khoản 1 Điều 22** → `THAM_CHIEU_PHAP_LY` (span: `[42:48]`) *(lồng trong `e1` (`KHOAN`))*
- `[e4]` **Luật đấu thầu số 43/2013/QH13** → `THAM_CHIEU_PHAP_LY` (span: `[48:52]`) *(lồng trong `e1` (`KHOAN`))*
- `[e5]` **khoản 2 Điều 22** → `THAM_CHIEU_PHAP_LY` (span: `[59:63]`) *(lồng trong `e1` (`KHOAN`))*
- `[e6]` **Luật đấu thầu số 43/2013/QH13** → `THAM_CHIEU_PHAP_LY` (span: `[63:67]`) *(lồng trong `e1` (`KHOAN`))*
- `[e7]` **quy định tại** → `TU_KHOA_PHAP_LY` (span: `[19:21]`) *(lồng trong `e1` (`KHOAN`))*
- `[e8]` **quy định tại** → `TU_KHOA_PHAP_LY` (span: `[40:42]`) *(lồng trong `e1` (`KHOAN`))*
- `[e9]` **quy định tại** → `TU_KHOA_PHAP_LY` (span: `[57:59]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 1 . Hình thức chỉ định thầu theo quy trình thông thường được áp dụng đối với gói thầu thuộc trường hợp chỉ định thầu quy định tại các điểm b , c , d , đ và g ói thầu cần thực hiện để bảo đảm bí mật nhà nước quy định tại điểm a khoản 1 Điều 22 Luật đấu thầu số 43/2013/QH13 , đồng thời đáp ứng các điều kiện quy định tại khoản 2 Điều 22 Luật đấu thầu số 43/2013/QH13 . Hình thức chỉ định thầu theo quy trình rút gọn được `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 3 `[DIEU]`)
- (`e7` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e2` các điểm b , c , d , đ và g `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 1 . Hình thức chỉ định thầu theo quy trình thông thường được áp dụng đối với gói thầu thuộc trường hợp chỉ định thầu quy định tại các điểm b , c , d , đ và g ói thầu cần thực hiện để bảo đảm bí mật nhà nước quy định tại điểm a khoản 1 Điều 22 Luật đấu thầu số 43/2013/QH13 , đồng thời đáp ứng các điều kiện quy định tại khoản 2 Điều 22 Luật đấu thầu số 43/2013/QH13 . Hình thức chỉ định thầu theo quy trình rút gọn được `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e2` các điểm b , c , d , đ và g `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e8` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` điểm a khoản 1 Điều 22 `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 1 . Hình thức chỉ định thầu theo quy trình thông thường được áp dụng đối với gói thầu thuộc trường hợp chỉ định thầu quy định tại các điểm b , c , d , đ và g ói thầu cần thực hiện để bảo đảm bí mật nhà nước quy định tại điểm a khoản 1 Điều 22 Luật đấu thầu số 43/2013/QH13 , đồng thời đáp ứng các điều kiện quy định tại khoản 2 Điều 22 Luật đấu thầu số 43/2013/QH13 . Hình thức chỉ định thầu theo quy trình rút gọn được `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` điểm a khoản 1 Điều 22 `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e8` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e4` Luật đấu thầu số 43/2013/QH13 `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 1 . Hình thức chỉ định thầu theo quy trình thông thường được áp dụng đối với gói thầu thuộc trường hợp chỉ định thầu quy định tại các điểm b , c , d , đ và g ói thầu cần thực hiện để bảo đảm bí mật nhà nước quy định tại điểm a khoản 1 Điều 22 Luật đấu thầu số 43/2013/QH13 , đồng thời đáp ứng các điều kiện quy định tại khoản 2 Điều 22 Luật đấu thầu số 43/2013/QH13 . Hình thức chỉ định thầu theo quy trình rút gọn được `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e4` Luật đấu thầu số 43/2013/QH13 `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e9` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e5` khoản 2 Điều 22 `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 1 . Hình thức chỉ định thầu theo quy trình thông thường được áp dụng đối với gói thầu thuộc trường hợp chỉ định thầu quy định tại các điểm b , c , d , đ và g ói thầu cần thực hiện để bảo đảm bí mật nhà nước quy định tại điểm a khoản 1 Điều 22 Luật đấu thầu số 43/2013/QH13 , đồng thời đáp ứng các điều kiện quy định tại khoản 2 Điều 22 Luật đấu thầu số 43/2013/QH13 . Hình thức chỉ định thầu theo quy trình rút gọn được `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e5` khoản 2 Điều 22 `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e9` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e6` Luật đấu thầu số 43/2013/QH13 `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 1 . Hình thức chỉ định thầu theo quy trình thông thường được áp dụng đối với gói thầu thuộc trường hợp chỉ định thầu quy định tại các điểm b , c , d , đ và g ói thầu cần thực hiện để bảo đảm bí mật nhà nước quy định tại điểm a khoản 1 Điều 22 Luật đấu thầu số 43/2013/QH13 , đồng thời đáp ứng các điều kiện quy định tại khoản 2 Điều 22 Luật đấu thầu số 43/2013/QH13 . Hình thức chỉ định thầu theo quy trình rút gọn được `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e6` Luật đấu thầu số 43/2013/QH13 `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #11_2015_TT-BKHĐT_92514#body_context_32 (Loại: `body_context`)
> **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[11/2015/TT-BKHĐT]`<SO_HIEU>`** . **[Điều 3]`<DIEU>`** . **[2 . Hình thức chào hàng cạnh tranh theo quy trình thông thường được áp dụng đối với gói thầu **[quy định tại]`<TU_KHOA_PHAP_LY>`** **[Điều 23]`<THAM_CHIEU_PHAP_LY>`** **[Luật đấu thầu số 43/2013/QH13]`<THAM_CHIEU_PHAP_LY>`** và **[khoản 1 Điều 57 Nghị định số 63/2014/NĐ-CP]`<THAM_CHIEU_PHAP_LY>`** . Hình thức chào hàng cạnh tranh theo quy trình rút gọn được áp dụng đối với gói thầu **[quy định tại]`<TU_KHOA_PHAP_LY>`** **[Điều 23]`<THAM_CHIEU_PHAP_LY>`** **[Luật đấu thầu số 43/2013/QH13]`<THAM_CHIEU_PHAP_LY>`** và **[khoản 2 Điều 57 Nghị định số 63/2014/NĐ-CP]`<THAM_CHIEU_PHAP_LY>`** .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[5:6]`)
- `[e1]` **11/2015/TT-BKHĐT** → `SO_HIEU` (span: `[7:8]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[0:4]`)
- `[e3]` **Điều 3** → `DIEU` (span: `[9:11]`)
- `[e4]` **2 . Hình thức chào hàng cạnh tranh theo quy trình thông thường được áp dụng đối với gói thầu quy định tại Điều 23 Luật đấu thầu số 43/2013/QH13 và khoản 1 Điều 57 Nghị định số 63/2014/NĐ-CP . Hình thức chào hàng cạnh tranh theo quy trình rút gọn được áp dụng đối với gói thầu quy định tại Điều 23 Luật đấu thầu số 43/2013/QH13 và khoản 2 Điều 57 Nghị định số 63/2014/NĐ-CP .** → `KHOAN` (span: `[12:68]`)
- `[e5]` **Điều 23** → `THAM_CHIEU_PHAP_LY` (span: `[26:28]`) *(lồng trong `e4` (`KHOAN`))*
- `[e6]` **Luật đấu thầu số 43/2013/QH13** → `THAM_CHIEU_PHAP_LY` (span: `[28:32]`) *(lồng trong `e4` (`KHOAN`))*
- `[e7]` **khoản 1 Điều 57 Nghị định số 63/2014/NĐ-CP** → `THAM_CHIEU_PHAP_LY` (span: `[33:40]`) *(lồng trong `e4` (`KHOAN`))*
- `[e8]` **Điều 23** → `THAM_CHIEU_PHAP_LY` (span: `[53:55]`) *(lồng trong `e4` (`KHOAN`))*
- `[e9]` **Luật đấu thầu số 43/2013/QH13** → `THAM_CHIEU_PHAP_LY` (span: `[55:59]`) *(lồng trong `e4` (`KHOAN`))*
- `[e10]` **khoản 2 Điều 57 Nghị định số 63/2014/NĐ-CP** → `THAM_CHIEU_PHAP_LY` (span: `[60:67]`) *(lồng trong `e4` (`KHOAN`))*
- `[e11]` **quy định tại** → `TU_KHOA_PHAP_LY` (span: `[24:26]`) *(lồng trong `e4` (`KHOAN`))*
- `[e12]` **quy định tại** → `TU_KHOA_PHAP_LY` (span: `[51:53]`) *(lồng trong `e4` (`KHOAN`))*

**Quan hệ:**
- (`e1` 11/2015/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 11/2015/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 3 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 11/2015/TT-BKHĐT `[SO_HIEU]`)
- (`e4` 2 . Hình thức chào hàng cạnh tranh theo quy trình thông thường được áp dụng đối với gói thầu quy định tại Điều 23 Luật đấu thầu số 43/2013/QH13 và khoản 1 Điều 57 Nghị định số 63/2014/NĐ-CP . Hình thức chào hàng cạnh tranh theo quy trình rút gọn được áp dụng đối với gói thầu quy định tại Điều 23 Luật đấu thầu số 43/2013/QH13 và khoản 2 Điều 57 Nghị định số 63/2014/NĐ-CP . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 3 `[DIEU]`)
- (`e11` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e5` Điều 23 `[THAM_CHIEU_PHAP_LY]`)
- (`e4` 2 . Hình thức chào hàng cạnh tranh theo quy trình thông thường được áp dụng đối với gói thầu quy định tại Điều 23 Luật đấu thầu số 43/2013/QH13 và khoản 1 Điều 57 Nghị định số 63/2014/NĐ-CP . Hình thức chào hàng cạnh tranh theo quy trình rút gọn được áp dụng đối với gói thầu quy định tại Điều 23 Luật đấu thầu số 43/2013/QH13 và khoản 2 Điều 57 Nghị định số 63/2014/NĐ-CP . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e5` Điều 23 `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e11` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e6` Luật đấu thầu số 43/2013/QH13 `[THAM_CHIEU_PHAP_LY]`)
- (`e4` 2 . Hình thức chào hàng cạnh tranh theo quy trình thông thường được áp dụng đối với gói thầu quy định tại Điều 23 Luật đấu thầu số 43/2013/QH13 và khoản 1 Điều 57 Nghị định số 63/2014/NĐ-CP . Hình thức chào hàng cạnh tranh theo quy trình rút gọn được áp dụng đối với gói thầu quy định tại Điều 23 Luật đấu thầu số 43/2013/QH13 và khoản 2 Điều 57 Nghị định số 63/2014/NĐ-CP . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e6` Luật đấu thầu số 43/2013/QH13 `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e11` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e7` khoản 1 Điều 57 Nghị định số 63/2014/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e4` 2 . Hình thức chào hàng cạnh tranh theo quy trình thông thường được áp dụng đối với gói thầu quy định tại Điều 23 Luật đấu thầu số 43/2013/QH13 và khoản 1 Điều 57 Nghị định số 63/2014/NĐ-CP . Hình thức chào hàng cạnh tranh theo quy trình rút gọn được áp dụng đối với gói thầu quy định tại Điều 23 Luật đấu thầu số 43/2013/QH13 và khoản 2 Điều 57 Nghị định số 63/2014/NĐ-CP . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e7` khoản 1 Điều 57 Nghị định số 63/2014/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e12` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e8` Điều 23 `[THAM_CHIEU_PHAP_LY]`)
- (`e4` 2 . Hình thức chào hàng cạnh tranh theo quy trình thông thường được áp dụng đối với gói thầu quy định tại Điều 23 Luật đấu thầu số 43/2013/QH13 và khoản 1 Điều 57 Nghị định số 63/2014/NĐ-CP . Hình thức chào hàng cạnh tranh theo quy trình rút gọn được áp dụng đối với gói thầu quy định tại Điều 23 Luật đấu thầu số 43/2013/QH13 và khoản 2 Điều 57 Nghị định số 63/2014/NĐ-CP . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e8` Điều 23 `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e12` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e9` Luật đấu thầu số 43/2013/QH13 `[THAM_CHIEU_PHAP_LY]`)
- (`e4` 2 . Hình thức chào hàng cạnh tranh theo quy trình thông thường được áp dụng đối với gói thầu quy định tại Điều 23 Luật đấu thầu số 43/2013/QH13 và khoản 1 Điều 57 Nghị định số 63/2014/NĐ-CP . Hình thức chào hàng cạnh tranh theo quy trình rút gọn được áp dụng đối với gói thầu quy định tại Điều 23 Luật đấu thầu số 43/2013/QH13 và khoản 2 Điều 57 Nghị định số 63/2014/NĐ-CP . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e9` Luật đấu thầu số 43/2013/QH13 `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e12` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e10` khoản 2 Điều 57 Nghị định số 63/2014/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e4` 2 . Hình thức chào hàng cạnh tranh theo quy trình thông thường được áp dụng đối với gói thầu quy định tại Điều 23 Luật đấu thầu số 43/2013/QH13 và khoản 1 Điều 57 Nghị định số 63/2014/NĐ-CP . Hình thức chào hàng cạnh tranh theo quy trình rút gọn được áp dụng đối với gói thầu quy định tại Điều 23 Luật đấu thầu số 43/2013/QH13 và khoản 2 Điều 57 Nghị định số 63/2014/NĐ-CP . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e10` khoản 2 Điều 57 Nghị định số 63/2014/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #11_2015_TT-BKHĐT_92514#body_standalone_33 (Loại: `body_standalone`)
> **[Điều 3]`<DIEU>`** . **[2 . Hình thức chào hàng cạnh tranh theo quy trình thông thường được áp dụng đối với gói thầu **[quy định tại]`<TU_KHOA_PHAP_LY>`** **[Điều 23]`<THAM_CHIEU_PHAP_LY>`** **[Luật đấu thầu số 43/2013/QH13]`<THAM_CHIEU_PHAP_LY>`** và **[khoản 1 Điều 57 Nghị định số 63/2014/NĐ-CP]`<THAM_CHIEU_PHAP_LY>`** . Hình thức chào hàng cạnh tranh theo quy trình rút gọn được áp dụng đối với gói thầu **[quy định tại]`<TU_KHOA_PHAP_LY>`** **[Điều 23]`<THAM_CHIEU_PHAP_LY>`** **[Luật đấu thầu số 43/2013/QH13]`<THAM_CHIEU_PHAP_LY>`** và **[khoản 2 Điều 57 Nghị định số 63/2014/NĐ-CP]`<THAM_CHIEU_PHAP_LY>`** .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 3** → `DIEU` (span: `[0:2]`)
- `[e1]` **2 . Hình thức chào hàng cạnh tranh theo quy trình thông thường được áp dụng đối với gói thầu quy định tại Điều 23 Luật đấu thầu số 43/2013/QH13 và khoản 1 Điều 57 Nghị định số 63/2014/NĐ-CP . Hình thức chào hàng cạnh tranh theo quy trình rút gọn được áp dụng đối với gói thầu quy định tại Điều 23 Luật đấu thầu số 43/2013/QH13 và khoản 2 Điều 57 Nghị định số 63/2014/NĐ-CP .** → `KHOAN` (span: `[3:59]`)
- `[e2]` **Điều 23** → `THAM_CHIEU_PHAP_LY` (span: `[17:19]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **Luật đấu thầu số 43/2013/QH13** → `THAM_CHIEU_PHAP_LY` (span: `[19:23]`) *(lồng trong `e1` (`KHOAN`))*
- `[e4]` **khoản 1 Điều 57 Nghị định số 63/2014/NĐ-CP** → `THAM_CHIEU_PHAP_LY` (span: `[24:31]`) *(lồng trong `e1` (`KHOAN`))*
- `[e5]` **Điều 23** → `THAM_CHIEU_PHAP_LY` (span: `[44:46]`) *(lồng trong `e1` (`KHOAN`))*
- `[e6]` **Luật đấu thầu số 43/2013/QH13** → `THAM_CHIEU_PHAP_LY` (span: `[46:50]`) *(lồng trong `e1` (`KHOAN`))*
- `[e7]` **khoản 2 Điều 57 Nghị định số 63/2014/NĐ-CP** → `THAM_CHIEU_PHAP_LY` (span: `[51:58]`) *(lồng trong `e1` (`KHOAN`))*
- `[e8]` **quy định tại** → `TU_KHOA_PHAP_LY` (span: `[15:17]`) *(lồng trong `e1` (`KHOAN`))*
- `[e9]` **quy định tại** → `TU_KHOA_PHAP_LY` (span: `[42:44]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 2 . Hình thức chào hàng cạnh tranh theo quy trình thông thường được áp dụng đối với gói thầu quy định tại Điều 23 Luật đấu thầu số 43/2013/QH13 và khoản 1 Điều 57 Nghị định số 63/2014/NĐ-CP . Hình thức chào hàng cạnh tranh theo quy trình rút gọn được áp dụng đối với gói thầu quy định tại Điều 23 Luật đấu thầu số 43/2013/QH13 và khoản 2 Điều 57 Nghị định số 63/2014/NĐ-CP . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 3 `[DIEU]`)
- (`e8` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e2` Điều 23 `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 2 . Hình thức chào hàng cạnh tranh theo quy trình thông thường được áp dụng đối với gói thầu quy định tại Điều 23 Luật đấu thầu số 43/2013/QH13 và khoản 1 Điều 57 Nghị định số 63/2014/NĐ-CP . Hình thức chào hàng cạnh tranh theo quy trình rút gọn được áp dụng đối với gói thầu quy định tại Điều 23 Luật đấu thầu số 43/2013/QH13 và khoản 2 Điều 57 Nghị định số 63/2014/NĐ-CP . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e2` Điều 23 `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e8` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Luật đấu thầu số 43/2013/QH13 `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 2 . Hình thức chào hàng cạnh tranh theo quy trình thông thường được áp dụng đối với gói thầu quy định tại Điều 23 Luật đấu thầu số 43/2013/QH13 và khoản 1 Điều 57 Nghị định số 63/2014/NĐ-CP . Hình thức chào hàng cạnh tranh theo quy trình rút gọn được áp dụng đối với gói thầu quy định tại Điều 23 Luật đấu thầu số 43/2013/QH13 và khoản 2 Điều 57 Nghị định số 63/2014/NĐ-CP . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Luật đấu thầu số 43/2013/QH13 `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e8` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e4` khoản 1 Điều 57 Nghị định số 63/2014/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 2 . Hình thức chào hàng cạnh tranh theo quy trình thông thường được áp dụng đối với gói thầu quy định tại Điều 23 Luật đấu thầu số 43/2013/QH13 và khoản 1 Điều 57 Nghị định số 63/2014/NĐ-CP . Hình thức chào hàng cạnh tranh theo quy trình rút gọn được áp dụng đối với gói thầu quy định tại Điều 23 Luật đấu thầu số 43/2013/QH13 và khoản 2 Điều 57 Nghị định số 63/2014/NĐ-CP . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e4` khoản 1 Điều 57 Nghị định số 63/2014/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e9` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e5` Điều 23 `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 2 . Hình thức chào hàng cạnh tranh theo quy trình thông thường được áp dụng đối với gói thầu quy định tại Điều 23 Luật đấu thầu số 43/2013/QH13 và khoản 1 Điều 57 Nghị định số 63/2014/NĐ-CP . Hình thức chào hàng cạnh tranh theo quy trình rút gọn được áp dụng đối với gói thầu quy định tại Điều 23 Luật đấu thầu số 43/2013/QH13 và khoản 2 Điều 57 Nghị định số 63/2014/NĐ-CP . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e5` Điều 23 `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e9` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e6` Luật đấu thầu số 43/2013/QH13 `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 2 . Hình thức chào hàng cạnh tranh theo quy trình thông thường được áp dụng đối với gói thầu quy định tại Điều 23 Luật đấu thầu số 43/2013/QH13 và khoản 1 Điều 57 Nghị định số 63/2014/NĐ-CP . Hình thức chào hàng cạnh tranh theo quy trình rút gọn được áp dụng đối với gói thầu quy định tại Điều 23 Luật đấu thầu số 43/2013/QH13 và khoản 2 Điều 57 Nghị định số 63/2014/NĐ-CP . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e6` Luật đấu thầu số 43/2013/QH13 `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e9` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e7` khoản 2 Điều 57 Nghị định số 63/2014/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 2 . Hình thức chào hàng cạnh tranh theo quy trình thông thường được áp dụng đối với gói thầu quy định tại Điều 23 Luật đấu thầu số 43/2013/QH13 và khoản 1 Điều 57 Nghị định số 63/2014/NĐ-CP . Hình thức chào hàng cạnh tranh theo quy trình rút gọn được áp dụng đối với gói thầu quy định tại Điều 23 Luật đấu thầu số 43/2013/QH13 và khoản 2 Điều 57 Nghị định số 63/2014/NĐ-CP . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e7` khoản 2 Điều 57 Nghị định số 63/2014/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #11_2015_TT-BKHĐT_92514#body_context_34 (Loại: `body_context`)
> **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[11/2015/TT-BKHĐT]`<SO_HIEU>`** . **[Điều 3]`<DIEU>`** . **[3 . Khi lập , thẩm định , phê duyệt **[hồ sơ yêu cầu]`<GIAY_TO_HO_SO>`** áp dụng cho gói thầu xây lắp , mua sắm **[hàng hóa]`<TAI_SAN_VAT_CHAT>`** thực hiện chỉ định thầu theo quy trình thông thường , tổ chức , cá nhân phải áp dụng tương ứng **[Mẫu số 01]`<THAM_CHIEU_PHAP_LY>`** hoặc **[Mẫu số 02 ban hành kèm theo Thông tư này]`<THAM_CHIEU_PHAP_LY>`** và căn cứ vào quy mô , tính chất của từng gói thầu cụ thể để đưa ra các yêu cầu phù hợp trên cơ sở bảo đảm nguyên tắc công khai , minh bạch và hiệu quả kinh]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[5:6]`)
- `[e1]` **11/2015/TT-BKHĐT** → `SO_HIEU` (span: `[7:8]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[0:4]`)
- `[e3]` **Điều 3** → `DIEU` (span: `[9:11]`)
- `[e4]` **3 . Khi lập , thẩm định , phê duyệt hồ sơ yêu cầu áp dụng cho gói thầu xây lắp , mua sắm hàng hóa thực hiện chỉ định thầu theo quy trình thông thường , tổ chức , cá nhân phải áp dụng tương ứng Mẫu số 01 hoặc Mẫu số 02 ban hành kèm theo Thông tư này và căn cứ vào quy mô , tính chất của từng gói thầu cụ thể để đưa ra các yêu cầu phù hợp trên cơ sở bảo đảm nguyên tắc công khai , minh bạch và hiệu quả kinh** → `KHOAN` (span: `[12:78]`)
- `[e5]` **Mẫu số 01** → `THAM_CHIEU_PHAP_LY` (span: `[42:44]`) *(lồng trong `e4` (`KHOAN`))*
- `[e6]` **Mẫu số 02 ban hành kèm theo Thông tư này** → `THAM_CHIEU_PHAP_LY` (span: `[45:52]`) *(lồng trong `e4` (`KHOAN`))*
- `[e7]` **hồ sơ yêu cầu** → `GIAY_TO_HO_SO` (span: `[20:22]`) *(lồng trong `e4` (`KHOAN`))*
- `[e8]` **hàng hóa** → `TAI_SAN_VAT_CHAT` (span: `[28:29]`) *(lồng trong `e4` (`KHOAN`))*

**Quan hệ:**
- (`e1` 11/2015/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 11/2015/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 3 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 11/2015/TT-BKHĐT `[SO_HIEU]`)
- (`e4` 3 . Khi lập , thẩm định , phê duyệt hồ sơ yêu cầu áp dụng cho gói thầu xây lắp , mua sắm hàng hóa thực hiện chỉ định thầu theo quy trình thông thường , tổ chức , cá nhân phải áp dụng tương ứng Mẫu số 01 hoặc Mẫu số 02 ban hành kèm theo Thông tư này và căn cứ vào quy mô , tính chất của từng gói thầu cụ thể để đưa ra các yêu cầu phù hợp trên cơ sở bảo đảm nguyên tắc công khai , minh bạch và hiệu quả kinh `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 3 `[DIEU]`)
- (`e4` 3 . Khi lập , thẩm định , phê duyệt hồ sơ yêu cầu áp dụng cho gói thầu xây lắp , mua sắm hàng hóa thực hiện chỉ định thầu theo quy trình thông thường , tổ chức , cá nhân phải áp dụng tương ứng Mẫu số 01 hoặc Mẫu số 02 ban hành kèm theo Thông tư này và căn cứ vào quy mô , tính chất của từng gói thầu cụ thể để đưa ra các yêu cầu phù hợp trên cơ sở bảo đảm nguyên tắc công khai , minh bạch và hiệu quả kinh `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e5` Mẫu số 01 `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e4` 3 . Khi lập , thẩm định , phê duyệt hồ sơ yêu cầu áp dụng cho gói thầu xây lắp , mua sắm hàng hóa thực hiện chỉ định thầu theo quy trình thông thường , tổ chức , cá nhân phải áp dụng tương ứng Mẫu số 01 hoặc Mẫu số 02 ban hành kèm theo Thông tư này và căn cứ vào quy mô , tính chất của từng gói thầu cụ thể để đưa ra các yêu cầu phù hợp trên cơ sở bảo đảm nguyên tắc công khai , minh bạch và hiệu quả kinh `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e6` Mẫu số 02 ban hành kèm theo Thông tư này `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #11_2015_TT-BKHĐT_92514#body_standalone_35 (Loại: `body_standalone`)
> **[Điều 3]`<DIEU>`** . **[3 . Khi lập , thẩm định , phê duyệt **[hồ sơ yêu cầu]`<GIAY_TO_HO_SO>`** áp dụng cho gói thầu xây lắp , mua sắm **[hàng hóa]`<TAI_SAN_VAT_CHAT>`** thực hiện chỉ định thầu theo quy trình thông thường , tổ chức , cá nhân phải áp dụng tương ứng **[Mẫu số 01]`<THAM_CHIEU_PHAP_LY>`** hoặc **[Mẫu số 02 ban hành kèm theo Thông tư này]`<THAM_CHIEU_PHAP_LY>`** và căn cứ vào quy mô , tính chất của từng gói thầu cụ thể để đưa ra các yêu cầu phù hợp trên cơ sở bảo đảm nguyên tắc công khai , minh bạch và hiệu quả kinh]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 3** → `DIEU` (span: `[0:2]`)
- `[e1]` **3 . Khi lập , thẩm định , phê duyệt hồ sơ yêu cầu áp dụng cho gói thầu xây lắp , mua sắm hàng hóa thực hiện chỉ định thầu theo quy trình thông thường , tổ chức , cá nhân phải áp dụng tương ứng Mẫu số 01 hoặc Mẫu số 02 ban hành kèm theo Thông tư này và căn cứ vào quy mô , tính chất của từng gói thầu cụ thể để đưa ra các yêu cầu phù hợp trên cơ sở bảo đảm nguyên tắc công khai , minh bạch và hiệu quả kinh** → `KHOAN` (span: `[3:69]`)
- `[e2]` **Mẫu số 01** → `THAM_CHIEU_PHAP_LY` (span: `[33:35]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **Mẫu số 02 ban hành kèm theo Thông tư này** → `THAM_CHIEU_PHAP_LY` (span: `[36:43]`) *(lồng trong `e1` (`KHOAN`))*
- `[e4]` **hồ sơ yêu cầu** → `GIAY_TO_HO_SO` (span: `[11:13]`) *(lồng trong `e1` (`KHOAN`))*
- `[e5]` **hàng hóa** → `TAI_SAN_VAT_CHAT` (span: `[19:20]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 3 . Khi lập , thẩm định , phê duyệt hồ sơ yêu cầu áp dụng cho gói thầu xây lắp , mua sắm hàng hóa thực hiện chỉ định thầu theo quy trình thông thường , tổ chức , cá nhân phải áp dụng tương ứng Mẫu số 01 hoặc Mẫu số 02 ban hành kèm theo Thông tư này và căn cứ vào quy mô , tính chất của từng gói thầu cụ thể để đưa ra các yêu cầu phù hợp trên cơ sở bảo đảm nguyên tắc công khai , minh bạch và hiệu quả kinh `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 3 `[DIEU]`)
- (`e1` 3 . Khi lập , thẩm định , phê duyệt hồ sơ yêu cầu áp dụng cho gói thầu xây lắp , mua sắm hàng hóa thực hiện chỉ định thầu theo quy trình thông thường , tổ chức , cá nhân phải áp dụng tương ứng Mẫu số 01 hoặc Mẫu số 02 ban hành kèm theo Thông tư này và căn cứ vào quy mô , tính chất của từng gói thầu cụ thể để đưa ra các yêu cầu phù hợp trên cơ sở bảo đảm nguyên tắc công khai , minh bạch và hiệu quả kinh `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e2` Mẫu số 01 `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e1` 3 . Khi lập , thẩm định , phê duyệt hồ sơ yêu cầu áp dụng cho gói thầu xây lắp , mua sắm hàng hóa thực hiện chỉ định thầu theo quy trình thông thường , tổ chức , cá nhân phải áp dụng tương ứng Mẫu số 01 hoặc Mẫu số 02 ban hành kèm theo Thông tư này và căn cứ vào quy mô , tính chất của từng gói thầu cụ thể để đưa ra các yêu cầu phù hợp trên cơ sở bảo đảm nguyên tắc công khai , minh bạch và hiệu quả kinh `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Mẫu số 02 ban hành kèm theo Thông tư này `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #11_2015_TT-BKHĐT_92514#body_context_36 (Loại: `body_context`)
> **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[11/2015/TT-BKHĐT]`<SO_HIEU>`** . **[Điều 3]`<DIEU>`** . **[4 . Trường hợp có chỉnh sửa các quy định nêu trong Mẫu **[hồ sơ yêu cầu]`<GIAY_TO_HO_SO>`** , bản yêu cầu báo giá , dự thảo hợp đồng thì tổ chức , cá nhân thực hiện việc lập , thẩm định , phê duyệt **[hồ sơ yêu cầu]`<GIAY_TO_HO_SO>`** , bản yêu cầu báo giá , dự thảo hợp đồng phải bảo đảm việc chỉnh sửa đó là phù hợp , khoa học , chặt chẽ và không trái với quy định của pháp luật về đấu thầu . Trong tờ trình đề nghị phê duyệt **[hồ sơ yêu cầu]`<GIAY_TO_HO_SO>`** , bản yêu cầu báo]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[5:6]`)
- `[e1]` **11/2015/TT-BKHĐT** → `SO_HIEU` (span: `[7:8]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[0:4]`)
- `[e3]` **Điều 3** → `DIEU` (span: `[9:11]`)
- `[e4]` **4 . Trường hợp có chỉnh sửa các quy định nêu trong Mẫu hồ sơ yêu cầu , bản yêu cầu báo giá , dự thảo hợp đồng thì tổ chức , cá nhân thực hiện việc lập , thẩm định , phê duyệt hồ sơ yêu cầu , bản yêu cầu báo giá , dự thảo hợp đồng phải bảo đảm việc chỉnh sửa đó là phù hợp , khoa học , chặt chẽ và không trái với quy định của pháp luật về đấu thầu . Trong tờ trình đề nghị phê duyệt hồ sơ yêu cầu , bản yêu cầu báo** → `KHOAN` (span: `[12:82]`)
- `[e5]` **hồ sơ yêu cầu** → `GIAY_TO_HO_SO` (span: `[22:24]`) *(lồng trong `e4` (`KHOAN`))*
- `[e6]` **hồ sơ yêu cầu** → `GIAY_TO_HO_SO` (span: `[42:44]`) *(lồng trong `e4` (`KHOAN`))*
- `[e7]` **hồ sơ yêu cầu** → `GIAY_TO_HO_SO` (span: `[76:78]`) *(lồng trong `e4` (`KHOAN`))*

**Quan hệ:**
- (`e1` 11/2015/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 11/2015/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 3 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 11/2015/TT-BKHĐT `[SO_HIEU]`)
- (`e4` 4 . Trường hợp có chỉnh sửa các quy định nêu trong Mẫu hồ sơ yêu cầu , bản yêu cầu báo giá , dự thảo hợp đồng thì tổ chức , cá nhân thực hiện việc lập , thẩm định , phê duyệt hồ sơ yêu cầu , bản yêu cầu báo giá , dự thảo hợp đồng phải bảo đảm việc chỉnh sửa đó là phù hợp , khoa học , chặt chẽ và không trái với quy định của pháp luật về đấu thầu . Trong tờ trình đề nghị phê duyệt hồ sơ yêu cầu , bản yêu cầu báo `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 3 `[DIEU]`)


---

### Mẫu #11_2015_TT-BKHĐT_92514#body_standalone_37 (Loại: `body_standalone`)
> **[Điều 3]`<DIEU>`** . **[4 . Trường hợp có chỉnh sửa các quy định nêu trong Mẫu **[hồ sơ yêu cầu]`<GIAY_TO_HO_SO>`** , bản yêu cầu báo giá , dự thảo hợp đồng thì tổ chức , cá nhân thực hiện việc lập , thẩm định , phê duyệt **[hồ sơ yêu cầu]`<GIAY_TO_HO_SO>`** , bản yêu cầu báo giá , dự thảo hợp đồng phải bảo đảm việc chỉnh sửa đó là phù hợp , khoa học , chặt chẽ và không trái với quy định của pháp luật về đấu thầu . Trong tờ trình đề nghị phê duyệt **[hồ sơ yêu cầu]`<GIAY_TO_HO_SO>`** , bản yêu cầu báo]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 3** → `DIEU` (span: `[0:2]`)
- `[e1]` **4 . Trường hợp có chỉnh sửa các quy định nêu trong Mẫu hồ sơ yêu cầu , bản yêu cầu báo giá , dự thảo hợp đồng thì tổ chức , cá nhân thực hiện việc lập , thẩm định , phê duyệt hồ sơ yêu cầu , bản yêu cầu báo giá , dự thảo hợp đồng phải bảo đảm việc chỉnh sửa đó là phù hợp , khoa học , chặt chẽ và không trái với quy định của pháp luật về đấu thầu . Trong tờ trình đề nghị phê duyệt hồ sơ yêu cầu , bản yêu cầu báo** → `KHOAN` (span: `[3:73]`)
- `[e2]` **hồ sơ yêu cầu** → `GIAY_TO_HO_SO` (span: `[13:15]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **hồ sơ yêu cầu** → `GIAY_TO_HO_SO` (span: `[33:35]`) *(lồng trong `e1` (`KHOAN`))*
- `[e4]` **hồ sơ yêu cầu** → `GIAY_TO_HO_SO` (span: `[67:69]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 4 . Trường hợp có chỉnh sửa các quy định nêu trong Mẫu hồ sơ yêu cầu , bản yêu cầu báo giá , dự thảo hợp đồng thì tổ chức , cá nhân thực hiện việc lập , thẩm định , phê duyệt hồ sơ yêu cầu , bản yêu cầu báo giá , dự thảo hợp đồng phải bảo đảm việc chỉnh sửa đó là phù hợp , khoa học , chặt chẽ và không trái với quy định của pháp luật về đấu thầu . Trong tờ trình đề nghị phê duyệt hồ sơ yêu cầu , bản yêu cầu báo `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 3 `[DIEU]`)


---

### Mẫu #11_2015_TT-BKHĐT_92514#body_context_38 (Loại: `body_context`)
> **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[11/2015/TT-BKHĐT]`<SO_HIEU>`** . **[Điều 3]`<DIEU>`** . **[5 . Đối với gói thầu dịch vụ phi tư vấn khi áp dụng hình thức chỉ định thầu , chào hàng cạnh tranh , việc lập **[hồ sơ yêu cầu]`<GIAY_TO_HO_SO>`** , bản yêu cầu báo giá , dự thảo hợp đồng thực hiện trên cơ sở vận dụng các Mẫu tương ứng ban hành kèm theo Thông tư này .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[5:6]`)
- `[e1]` **11/2015/TT-BKHĐT** → `SO_HIEU` (span: `[7:8]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[0:4]`)
- `[e3]` **Điều 3** → `DIEU` (span: `[9:11]`)
- `[e4]` **5 . Đối với gói thầu dịch vụ phi tư vấn khi áp dụng hình thức chỉ định thầu , chào hàng cạnh tranh , việc lập hồ sơ yêu cầu , bản yêu cầu báo giá , dự thảo hợp đồng thực hiện trên cơ sở vận dụng các Mẫu tương ứng ban hành kèm theo Thông tư này .** → `KHOAN` (span: `[12:52]`)
- `[e5]` **hồ sơ yêu cầu** → `GIAY_TO_HO_SO` (span: `[30:32]`) *(lồng trong `e4` (`KHOAN`))*

**Quan hệ:**
- (`e1` 11/2015/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 11/2015/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 3 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 11/2015/TT-BKHĐT `[SO_HIEU]`)
- (`e4` 5 . Đối với gói thầu dịch vụ phi tư vấn khi áp dụng hình thức chỉ định thầu , chào hàng cạnh tranh , việc lập hồ sơ yêu cầu , bản yêu cầu báo giá , dự thảo hợp đồng thực hiện trên cơ sở vận dụng các Mẫu tương ứng ban hành kèm theo Thông tư này . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 3 `[DIEU]`)


---

### Mẫu #11_2015_TT-BKHĐT_92514#body_standalone_39 (Loại: `body_standalone`)
> **[Điều 3]`<DIEU>`** . **[5 . Đối với gói thầu dịch vụ phi tư vấn khi áp dụng hình thức chỉ định thầu , chào hàng cạnh tranh , việc lập **[hồ sơ yêu cầu]`<GIAY_TO_HO_SO>`** , bản yêu cầu báo giá , dự thảo hợp đồng thực hiện trên cơ sở vận dụng các Mẫu tương ứng ban hành kèm theo Thông tư này .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 3** → `DIEU` (span: `[0:2]`)
- `[e1]` **5 . Đối với gói thầu dịch vụ phi tư vấn khi áp dụng hình thức chỉ định thầu , chào hàng cạnh tranh , việc lập hồ sơ yêu cầu , bản yêu cầu báo giá , dự thảo hợp đồng thực hiện trên cơ sở vận dụng các Mẫu tương ứng ban hành kèm theo Thông tư này .** → `KHOAN` (span: `[3:43]`)
- `[e2]` **hồ sơ yêu cầu** → `GIAY_TO_HO_SO` (span: `[21:23]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 5 . Đối với gói thầu dịch vụ phi tư vấn khi áp dụng hình thức chỉ định thầu , chào hàng cạnh tranh , việc lập hồ sơ yêu cầu , bản yêu cầu báo giá , dự thảo hợp đồng thực hiện trên cơ sở vận dụng các Mẫu tương ứng ban hành kèm theo Thông tư này . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 3 `[DIEU]`)


---

### Mẫu #11_2015_TT-BKHĐT_92514#body_context_40 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[11/2015/TT-BKHĐT]`<SO_HIEU>`** ban hành **[ngày 27 tháng 10 năm 2015]`<NGAY_BAN_HANH>`** bởi **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** . **[Điều 3]`<DIEU>`** . **[6 . Đối với gói thầu thuộc phạm vi điều chỉnh **[quy định tại]`<TU_KHOA_PHAP_LY>`** **[Điều 1 của Thông tư này]`<THAM_CHIEU_PHAP_LY>`** khi thực hiện chỉ định thầu hoặc chào hàng cạnh tranh quốc tế , căn cứ quy mô , tính chất của gói thầu , **[chủ đầu tư]`<CHU_THE_CA_NHAN>`** , bên mời thầu chỉnh sửa quy định về ngôn ngữ , đồng tiền , thời gian trong đấu thầu và các nội dung liên quan khác cho phù hợp với quy định của **[Luật đấu thầu số 43/2013/QH13]`<THAM_CHIEU_PHAP_LY>`** và **[Nghị định số 63/2014/NĐ-CP]`<THAM_CHIEU_PHAP_LY>`** .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **11/2015/TT-BKHĐT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[11:15]`)
- `[e3]` **ngày 27 tháng 10 năm 2015** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 3** → `DIEU` (span: `[16:18]`)
- `[e5]` **6 . Đối với gói thầu thuộc phạm vi điều chỉnh quy định tại Điều 1 của Thông tư này khi thực hiện chỉ định thầu hoặc chào hàng cạnh tranh quốc tế , căn cứ quy mô , tính chất của gói thầu , chủ đầu tư , bên mời thầu chỉnh sửa quy định về ngôn ngữ , đồng tiền , thời gian trong đấu thầu và các nội dung liên quan khác cho phù hợp với quy định của Luật đấu thầu số 43/2013/QH13 và Nghị định số 63/2014/NĐ-CP .** → `KHOAN` (span: `[19:83]`)
- `[e6]` **Điều 1 của Thông tư này** → `THAM_CHIEU_PHAP_LY` (span: `[28:33]`) *(lồng trong `e5` (`KHOAN`))*
- `[e7]` **Luật đấu thầu số 43/2013/QH13** → `THAM_CHIEU_PHAP_LY` (span: `[74:78]`) *(lồng trong `e5` (`KHOAN`))*
- `[e8]` **Nghị định số 63/2014/NĐ-CP** → `THAM_CHIEU_PHAP_LY` (span: `[79:82]`) *(lồng trong `e5` (`KHOAN`))*
- `[e9]` **quy định tại** → `TU_KHOA_PHAP_LY` (span: `[26:28]`) *(lồng trong `e5` (`KHOAN`))*
- `[e10]` **chủ đầu tư** → `CHU_THE_CA_NHAN` (span: `[49:51]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 11/2015/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 11/2015/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 11/2015/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 27 tháng 10 năm 2015 `[NGAY_BAN_HANH]`)
- (`e4` Điều 3 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 11/2015/TT-BKHĐT `[SO_HIEU]`)
- (`e5` 6 . Đối với gói thầu thuộc phạm vi điều chỉnh quy định tại Điều 1 của Thông tư này khi thực hiện chỉ định thầu hoặc chào hàng cạnh tranh quốc tế , căn cứ quy mô , tính chất của gói thầu , chủ đầu tư , bên mời thầu chỉnh sửa quy định về ngôn ngữ , đồng tiền , thời gian trong đấu thầu và các nội dung liên quan khác cho phù hợp với quy định của Luật đấu thầu số 43/2013/QH13 và Nghị định số 63/2014/NĐ-CP . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 3 `[DIEU]`)
- (`e9` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e6` Điều 1 của Thông tư này `[THAM_CHIEU_PHAP_LY]`)
- (`e5` 6 . Đối với gói thầu thuộc phạm vi điều chỉnh quy định tại Điều 1 của Thông tư này khi thực hiện chỉ định thầu hoặc chào hàng cạnh tranh quốc tế , căn cứ quy mô , tính chất của gói thầu , chủ đầu tư , bên mời thầu chỉnh sửa quy định về ngôn ngữ , đồng tiền , thời gian trong đấu thầu và các nội dung liên quan khác cho phù hợp với quy định của Luật đấu thầu số 43/2013/QH13 và Nghị định số 63/2014/NĐ-CP . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e6` Điều 1 của Thông tư này `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e9` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e7` Luật đấu thầu số 43/2013/QH13 `[THAM_CHIEU_PHAP_LY]`)
- (`e5` 6 . Đối với gói thầu thuộc phạm vi điều chỉnh quy định tại Điều 1 của Thông tư này khi thực hiện chỉ định thầu hoặc chào hàng cạnh tranh quốc tế , căn cứ quy mô , tính chất của gói thầu , chủ đầu tư , bên mời thầu chỉnh sửa quy định về ngôn ngữ , đồng tiền , thời gian trong đấu thầu và các nội dung liên quan khác cho phù hợp với quy định của Luật đấu thầu số 43/2013/QH13 và Nghị định số 63/2014/NĐ-CP . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e7` Luật đấu thầu số 43/2013/QH13 `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e9` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e8` Nghị định số 63/2014/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e5` 6 . Đối với gói thầu thuộc phạm vi điều chỉnh quy định tại Điều 1 của Thông tư này khi thực hiện chỉ định thầu hoặc chào hàng cạnh tranh quốc tế , căn cứ quy mô , tính chất của gói thầu , chủ đầu tư , bên mời thầu chỉnh sửa quy định về ngôn ngữ , đồng tiền , thời gian trong đấu thầu và các nội dung liên quan khác cho phù hợp với quy định của Luật đấu thầu số 43/2013/QH13 và Nghị định số 63/2014/NĐ-CP . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e8` Nghị định số 63/2014/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #11_2015_TT-BKHĐT_92514#body_standalone_41 (Loại: `body_standalone`)
> **[Điều 3]`<DIEU>`** . **[6 . Đối với gói thầu thuộc phạm vi điều chỉnh **[quy định tại]`<TU_KHOA_PHAP_LY>`** **[Điều 1 của Thông tư này]`<THAM_CHIEU_PHAP_LY>`** khi thực hiện chỉ định thầu hoặc chào hàng cạnh tranh quốc tế , căn cứ quy mô , tính chất của gói thầu , **[chủ đầu tư]`<CHU_THE_CA_NHAN>`** , bên mời thầu chỉnh sửa quy định về ngôn ngữ , đồng tiền , thời gian trong đấu thầu và các nội dung liên quan khác cho phù hợp với quy định của **[Luật đấu thầu số 43/2013/QH13]`<THAM_CHIEU_PHAP_LY>`** và **[Nghị định số 63/2014/NĐ-CP]`<THAM_CHIEU_PHAP_LY>`** .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 3** → `DIEU` (span: `[0:2]`)
- `[e1]` **6 . Đối với gói thầu thuộc phạm vi điều chỉnh quy định tại Điều 1 của Thông tư này khi thực hiện chỉ định thầu hoặc chào hàng cạnh tranh quốc tế , căn cứ quy mô , tính chất của gói thầu , chủ đầu tư , bên mời thầu chỉnh sửa quy định về ngôn ngữ , đồng tiền , thời gian trong đấu thầu và các nội dung liên quan khác cho phù hợp với quy định của Luật đấu thầu số 43/2013/QH13 và Nghị định số 63/2014/NĐ-CP .** → `KHOAN` (span: `[3:67]`)
- `[e2]` **Điều 1 của Thông tư này** → `THAM_CHIEU_PHAP_LY` (span: `[12:17]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **Luật đấu thầu số 43/2013/QH13** → `THAM_CHIEU_PHAP_LY` (span: `[58:62]`) *(lồng trong `e1` (`KHOAN`))*
- `[e4]` **Nghị định số 63/2014/NĐ-CP** → `THAM_CHIEU_PHAP_LY` (span: `[63:66]`) *(lồng trong `e1` (`KHOAN`))*
- `[e5]` **quy định tại** → `TU_KHOA_PHAP_LY` (span: `[10:12]`) *(lồng trong `e1` (`KHOAN`))*
- `[e6]` **chủ đầu tư** → `CHU_THE_CA_NHAN` (span: `[33:35]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 6 . Đối với gói thầu thuộc phạm vi điều chỉnh quy định tại Điều 1 của Thông tư này khi thực hiện chỉ định thầu hoặc chào hàng cạnh tranh quốc tế , căn cứ quy mô , tính chất của gói thầu , chủ đầu tư , bên mời thầu chỉnh sửa quy định về ngôn ngữ , đồng tiền , thời gian trong đấu thầu và các nội dung liên quan khác cho phù hợp với quy định của Luật đấu thầu số 43/2013/QH13 và Nghị định số 63/2014/NĐ-CP . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 3 `[DIEU]`)
- (`e5` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e2` Điều 1 của Thông tư này `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 6 . Đối với gói thầu thuộc phạm vi điều chỉnh quy định tại Điều 1 của Thông tư này khi thực hiện chỉ định thầu hoặc chào hàng cạnh tranh quốc tế , căn cứ quy mô , tính chất của gói thầu , chủ đầu tư , bên mời thầu chỉnh sửa quy định về ngôn ngữ , đồng tiền , thời gian trong đấu thầu và các nội dung liên quan khác cho phù hợp với quy định của Luật đấu thầu số 43/2013/QH13 và Nghị định số 63/2014/NĐ-CP . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e2` Điều 1 của Thông tư này `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e5` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Luật đấu thầu số 43/2013/QH13 `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 6 . Đối với gói thầu thuộc phạm vi điều chỉnh quy định tại Điều 1 của Thông tư này khi thực hiện chỉ định thầu hoặc chào hàng cạnh tranh quốc tế , căn cứ quy mô , tính chất của gói thầu , chủ đầu tư , bên mời thầu chỉnh sửa quy định về ngôn ngữ , đồng tiền , thời gian trong đấu thầu và các nội dung liên quan khác cho phù hợp với quy định của Luật đấu thầu số 43/2013/QH13 và Nghị định số 63/2014/NĐ-CP . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Luật đấu thầu số 43/2013/QH13 `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e5` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e4` Nghị định số 63/2014/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 6 . Đối với gói thầu thuộc phạm vi điều chỉnh quy định tại Điều 1 của Thông tư này khi thực hiện chỉ định thầu hoặc chào hàng cạnh tranh quốc tế , căn cứ quy mô , tính chất của gói thầu , chủ đầu tư , bên mời thầu chỉnh sửa quy định về ngôn ngữ , đồng tiền , thời gian trong đấu thầu và các nội dung liên quan khác cho phù hợp với quy định của Luật đấu thầu số 43/2013/QH13 và Nghị định số 63/2014/NĐ-CP . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e4` Nghị định số 63/2014/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #11_2015_TT-BKHĐT_92514#body_context_42 (Loại: `body_context`)
> **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[11/2015/TT-BKHĐT]`<SO_HIEU>`** . **[Điều 3]`<DIEU>`** . **[7 . Đối với các gói thầu thuộc dự án có sử dụng vốn hỗ trợ phát triển chính thức , vốn vay ưu đãi phát sinh từ điều ước quốc tế , thỏa thuận quốc tế giữa Việt Nam với nhà tài trợ , trường hợp được nhà tài trợ chấp thuận thì áp dụng các mẫu **[hồ sơ yêu cầu]`<GIAY_TO_HO_SO>`** , bản yêu cầu báo giá , dự thảo hợp đồng ban hành kèm theo Thông tư này .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[5:6]`)
- `[e1]` **11/2015/TT-BKHĐT** → `SO_HIEU` (span: `[7:8]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[0:4]`)
- `[e3]` **Điều 3** → `DIEU` (span: `[9:11]`)
- `[e4]` **7 . Đối với các gói thầu thuộc dự án có sử dụng vốn hỗ trợ phát triển chính thức , vốn vay ưu đãi phát sinh từ điều ước quốc tế , thỏa thuận quốc tế giữa Việt Nam với nhà tài trợ , trường hợp được nhà tài trợ chấp thuận thì áp dụng các mẫu hồ sơ yêu cầu , bản yêu cầu báo giá , dự thảo hợp đồng ban hành kèm theo Thông tư này .** → `KHOAN` (span: `[12:66]`)
- `[e5]` **hồ sơ yêu cầu** → `GIAY_TO_HO_SO` (span: `[51:53]`) *(lồng trong `e4` (`KHOAN`))*

**Quan hệ:**
- (`e1` 11/2015/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 11/2015/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 3 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 11/2015/TT-BKHĐT `[SO_HIEU]`)
- (`e4` 7 . Đối với các gói thầu thuộc dự án có sử dụng vốn hỗ trợ phát triển chính thức , vốn vay ưu đãi phát sinh từ điều ước quốc tế , thỏa thuận quốc tế giữa Việt Nam với nhà tài trợ , trường hợp được nhà tài trợ chấp thuận thì áp dụng các mẫu hồ sơ yêu cầu , bản yêu cầu báo giá , dự thảo hợp đồng ban hành kèm theo Thông tư này . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 3 `[DIEU]`)


---

### Mẫu #11_2015_TT-BKHĐT_92514#body_standalone_43 (Loại: `body_standalone`)
> **[Điều 3]`<DIEU>`** . **[7 . Đối với các gói thầu thuộc dự án có sử dụng vốn hỗ trợ phát triển chính thức , vốn vay ưu đãi phát sinh từ điều ước quốc tế , thỏa thuận quốc tế giữa Việt Nam với nhà tài trợ , trường hợp được nhà tài trợ chấp thuận thì áp dụng các mẫu **[hồ sơ yêu cầu]`<GIAY_TO_HO_SO>`** , bản yêu cầu báo giá , dự thảo hợp đồng ban hành kèm theo Thông tư này .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 3** → `DIEU` (span: `[0:2]`)
- `[e1]` **7 . Đối với các gói thầu thuộc dự án có sử dụng vốn hỗ trợ phát triển chính thức , vốn vay ưu đãi phát sinh từ điều ước quốc tế , thỏa thuận quốc tế giữa Việt Nam với nhà tài trợ , trường hợp được nhà tài trợ chấp thuận thì áp dụng các mẫu hồ sơ yêu cầu , bản yêu cầu báo giá , dự thảo hợp đồng ban hành kèm theo Thông tư này .** → `KHOAN` (span: `[3:57]`)
- `[e2]` **hồ sơ yêu cầu** → `GIAY_TO_HO_SO` (span: `[42:44]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 7 . Đối với các gói thầu thuộc dự án có sử dụng vốn hỗ trợ phát triển chính thức , vốn vay ưu đãi phát sinh từ điều ước quốc tế , thỏa thuận quốc tế giữa Việt Nam với nhà tài trợ , trường hợp được nhà tài trợ chấp thuận thì áp dụng các mẫu hồ sơ yêu cầu , bản yêu cầu báo giá , dự thảo hợp đồng ban hành kèm theo Thông tư này . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 3 `[DIEU]`)


---

### Mẫu #11_2015_TT-BKHĐT_92514#body_context_44 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[11/2015/TT-BKHĐT]`<SO_HIEU>`** của **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Đấu thầu]`<LINH_VUC>`** . **[Điều 4 . Yêu cầu về nhãn hiệu , xuất xứ **[hàng hóa]`<TAI_SAN_VAT_CHAT>`**]`<DIEU>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **11/2015/TT-BKHĐT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[4:8]`)
- `[e3]` **Đấu thầu** → `LINH_VUC` (span: `[10:11]`)
- `[e4]` **Điều 4 . Yêu cầu về nhãn hiệu , xuất xứ hàng hóa** → `DIEU` (span: `[12:21]`)
- `[e5]` **hàng hóa** → `TAI_SAN_VAT_CHAT` (span: `[20:21]`) *(lồng trong `e4` (`DIEU`))*

**Quan hệ:**
- (`e1` 11/2015/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 11/2015/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 11/2015/TT-BKHĐT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Đấu thầu `[LINH_VUC]`)
- (`e4` Điều 4 . Yêu cầu về nhãn hiệu , xuất xứ hàng hóa `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 11/2015/TT-BKHĐT `[SO_HIEU]`)
- (`e1` 11/2015/TT-BKHĐT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Đấu thầu `[LINH_VUC]`)
- (`e4` Điều 4 . Yêu cầu về nhãn hiệu , xuất xứ hàng hóa `[DIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Đấu thầu `[LINH_VUC]`)


---

### Mẫu #11_2015_TT-BKHĐT_92514#body_context_45 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[11/2015/TT-BKHĐT]`<SO_HIEU>`** của **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Đấu thầu]`<LINH_VUC>`** . **[Điều 4]`<DIEU>`** . **[1 . Đối với gói thầu áp dụng hình thức chỉ định thầu , có thể nêu nhãn hiệu , xuất xứ cụ thể của **[hàng hóa]`<TAI_SAN_VAT_CHAT>`** trong **[hồ sơ yêu cầu]`<GIAY_TO_HO_SO>`** .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **11/2015/TT-BKHĐT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[4:8]`)
- `[e3]` **Đấu thầu** → `LINH_VUC` (span: `[10:11]`)
- `[e4]` **Điều 4** → `DIEU` (span: `[12:14]`)
- `[e5]` **1 . Đối với gói thầu áp dụng hình thức chỉ định thầu , có thể nêu nhãn hiệu , xuất xứ cụ thể của hàng hóa trong hồ sơ yêu cầu .** → `KHOAN` (span: `[15:36]`)
- `[e6]` **hồ sơ yêu cầu** → `GIAY_TO_HO_SO` (span: `[33:35]`) *(lồng trong `e5` (`KHOAN`))*
- `[e7]` **hàng hóa** → `TAI_SAN_VAT_CHAT` (span: `[31:32]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 11/2015/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 11/2015/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 11/2015/TT-BKHĐT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Đấu thầu `[LINH_VUC]`)
- (`e4` Điều 4 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 11/2015/TT-BKHĐT `[SO_HIEU]`)
- (`e5` 1 . Đối với gói thầu áp dụng hình thức chỉ định thầu , có thể nêu nhãn hiệu , xuất xứ cụ thể của hàng hóa trong hồ sơ yêu cầu . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 4 `[DIEU]`)
- (`e1` 11/2015/TT-BKHĐT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Đấu thầu `[LINH_VUC]`)
- (`e5` 1 . Đối với gói thầu áp dụng hình thức chỉ định thầu , có thể nêu nhãn hiệu , xuất xứ cụ thể của hàng hóa trong hồ sơ yêu cầu . `[KHOAN]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Đấu thầu `[LINH_VUC]`)


---

### Mẫu #11_2015_TT-BKHĐT_92514#body_standalone_46 (Loại: `body_standalone`)
> **[Điều 4]`<DIEU>`** . **[1 . Đối với gói thầu áp dụng hình thức chỉ định thầu , có thể nêu nhãn hiệu , xuất xứ cụ thể của **[hàng hóa]`<TAI_SAN_VAT_CHAT>`** trong **[hồ sơ yêu cầu]`<GIAY_TO_HO_SO>`** .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 4** → `DIEU` (span: `[0:2]`)
- `[e1]` **1 . Đối với gói thầu áp dụng hình thức chỉ định thầu , có thể nêu nhãn hiệu , xuất xứ cụ thể của hàng hóa trong hồ sơ yêu cầu .** → `KHOAN` (span: `[3:24]`)
- `[e2]` **hồ sơ yêu cầu** → `GIAY_TO_HO_SO` (span: `[21:23]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **hàng hóa** → `TAI_SAN_VAT_CHAT` (span: `[19:20]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 1 . Đối với gói thầu áp dụng hình thức chỉ định thầu , có thể nêu nhãn hiệu , xuất xứ cụ thể của hàng hóa trong hồ sơ yêu cầu . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 4 `[DIEU]`)


---

### Mẫu #11_2015_TT-BKHĐT_92514#body_context_47 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[11/2015/TT-BKHĐT]`<SO_HIEU>`** ban hành **[ngày 27 tháng 10 năm 2015]`<NGAY_BAN_HANH>`** bởi **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** . **[Điều 4]`<DIEU>`** . **[2 . Đối với gói thầu áp dụng hình thức chào hàng cạnh tranh , khi đưa ra yêu cầu đối với **[hàng hóa]`<TAI_SAN_VAT_CHAT>`** cần quy định đặc tính kỹ thuật , tiêu chuẩn sản xuất , tiêu chuẩn chế tạo , công nghệ mang tính chất trung tính , không đưa ra các đặc tính kỹ thuật , tiêu chuẩn mang tính cá biệt hóa mà không phải là đặc tính cơ bản của sản phẩm để chỉ một hoặc một số ít nhà thầu đáp ứng yêu cầu làm hạn chế sự tham gia của các nhà]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **11/2015/TT-BKHĐT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[11:15]`)
- `[e3]` **ngày 27 tháng 10 năm 2015** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 4** → `DIEU` (span: `[16:18]`)
- `[e5]` **2 . Đối với gói thầu áp dụng hình thức chào hàng cạnh tranh , khi đưa ra yêu cầu đối với hàng hóa cần quy định đặc tính kỹ thuật , tiêu chuẩn sản xuất , tiêu chuẩn chế tạo , công nghệ mang tính chất trung tính , không đưa ra các đặc tính kỹ thuật , tiêu chuẩn mang tính cá biệt hóa mà không phải là đặc tính cơ bản của sản phẩm để chỉ một hoặc một số ít nhà thầu đáp ứng yêu cầu làm hạn chế sự tham gia của các nhà** → `KHOAN` (span: `[19:84]`)
- `[e6]` **hàng hóa** → `TAI_SAN_VAT_CHAT` (span: `[33:34]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 11/2015/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 11/2015/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 11/2015/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 27 tháng 10 năm 2015 `[NGAY_BAN_HANH]`)
- (`e4` Điều 4 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 11/2015/TT-BKHĐT `[SO_HIEU]`)
- (`e5` 2 . Đối với gói thầu áp dụng hình thức chào hàng cạnh tranh , khi đưa ra yêu cầu đối với hàng hóa cần quy định đặc tính kỹ thuật , tiêu chuẩn sản xuất , tiêu chuẩn chế tạo , công nghệ mang tính chất trung tính , không đưa ra các đặc tính kỹ thuật , tiêu chuẩn mang tính cá biệt hóa mà không phải là đặc tính cơ bản của sản phẩm để chỉ một hoặc một số ít nhà thầu đáp ứng yêu cầu làm hạn chế sự tham gia của các nhà `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 4 `[DIEU]`)


---

### Mẫu #11_2015_TT-BKHĐT_92514#body_standalone_48 (Loại: `body_standalone`)
> **[Điều 4]`<DIEU>`** . **[2 . Đối với gói thầu áp dụng hình thức chào hàng cạnh tranh , khi đưa ra yêu cầu đối với **[hàng hóa]`<TAI_SAN_VAT_CHAT>`** cần quy định đặc tính kỹ thuật , tiêu chuẩn sản xuất , tiêu chuẩn chế tạo , công nghệ mang tính chất trung tính , không đưa ra các đặc tính kỹ thuật , tiêu chuẩn mang tính cá biệt hóa mà không phải là đặc tính cơ bản của sản phẩm để chỉ một hoặc một số ít nhà thầu đáp ứng yêu cầu làm hạn chế sự tham gia của các nhà]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 4** → `DIEU` (span: `[0:2]`)
- `[e1]` **2 . Đối với gói thầu áp dụng hình thức chào hàng cạnh tranh , khi đưa ra yêu cầu đối với hàng hóa cần quy định đặc tính kỹ thuật , tiêu chuẩn sản xuất , tiêu chuẩn chế tạo , công nghệ mang tính chất trung tính , không đưa ra các đặc tính kỹ thuật , tiêu chuẩn mang tính cá biệt hóa mà không phải là đặc tính cơ bản của sản phẩm để chỉ một hoặc một số ít nhà thầu đáp ứng yêu cầu làm hạn chế sự tham gia của các nhà** → `KHOAN` (span: `[3:68]`)
- `[e2]` **hàng hóa** → `TAI_SAN_VAT_CHAT` (span: `[17:18]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 2 . Đối với gói thầu áp dụng hình thức chào hàng cạnh tranh , khi đưa ra yêu cầu đối với hàng hóa cần quy định đặc tính kỹ thuật , tiêu chuẩn sản xuất , tiêu chuẩn chế tạo , công nghệ mang tính chất trung tính , không đưa ra các đặc tính kỹ thuật , tiêu chuẩn mang tính cá biệt hóa mà không phải là đặc tính cơ bản của sản phẩm để chỉ một hoặc một số ít nhà thầu đáp ứng yêu cầu làm hạn chế sự tham gia của các nhà `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 4 `[DIEU]`)


---

### Mẫu #11_2015_TT-BKHĐT_92514#body_context_49 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[11/2015/TT-BKHĐT]`<SO_HIEU>`** của **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Đấu thầu]`<LINH_VUC>`** . **[Điều 5 . Tổ chức thực hiện]`<DIEU>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **11/2015/TT-BKHĐT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[4:8]`)
- `[e3]` **Đấu thầu** → `LINH_VUC` (span: `[10:11]`)
- `[e4]` **Điều 5 . Tổ chức thực hiện** → `DIEU` (span: `[12:17]`)

**Quan hệ:**
- (`e1` 11/2015/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 11/2015/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 11/2015/TT-BKHĐT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Đấu thầu `[LINH_VUC]`)
- (`e4` Điều 5 . Tổ chức thực hiện `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 11/2015/TT-BKHĐT `[SO_HIEU]`)
- (`e1` 11/2015/TT-BKHĐT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Đấu thầu `[LINH_VUC]`)
- (`e4` Điều 5 . Tổ chức thực hiện `[DIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Đấu thầu `[LINH_VUC]`)


---

### Mẫu #11_2015_TT-BKHĐT_92514#body_context_50 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[11/2015/TT-BKHĐT]`<SO_HIEU>`** của **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Đấu thầu]`<LINH_VUC>`** . **[Điều 5]`<DIEU>`** . **[1 . Thông tư này có hiệu lực thi hành kể từ ngày 22 tháng 12 năm 2015 . Thông tư này thay thế **[Thông tư số 04/2010/TT-BKH]`<THAM_CHIEU_PHAP_LY>`** **[ngày 01/02/2010]`<NGAY_THAM_CHIEU>`** của **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_THAM_QUYEN>`** quy định chi tiết lập **[hồ sơ yêu cầu]`<GIAY_TO_HO_SO>`** chỉ định thầu xây lắp , **[Thông tư số 11/2010/TT-BKH]`<THAM_CHIEU_PHAP_LY>`** **[ngày 27/5/2010]`<NGAY_THAM_CHIEU>`** của **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_THAM_QUYEN>`** quy định chi tiết về chào hàng cạnh tranh .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **11/2015/TT-BKHĐT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[4:8]`)
- `[e3]` **Đấu thầu** → `LINH_VUC` (span: `[10:11]`)
- `[e4]` **Điều 5** → `DIEU` (span: `[12:14]`)
- `[e5]` **1 . Thông tư này có hiệu lực thi hành kể từ ngày 22 tháng 12 năm 2015 . Thông tư này thay thế Thông tư số 04/2010/TT-BKH ngày 01/02/2010 của Bộ Kế hoạch và Đầu tư quy định chi tiết lập hồ sơ yêu cầu chỉ định thầu xây lắp , Thông tư số 11/2010/TT-BKH ngày 27/5/2010 của Bộ Kế hoạch và Đầu tư quy định chi tiết về chào hàng cạnh tranh .** → `KHOAN` (span: `[15:69]`)
- `[e6]` **Thông tư số 04/2010/TT-BKH** → `THAM_CHIEU_PHAP_LY` (span: `[34:37]`) *(lồng trong `e5` (`KHOAN`))*
- `[e7]` **Thông tư số 11/2010/TT-BKH** → `THAM_CHIEU_PHAP_LY` (span: `[53:56]`) *(lồng trong `e5` (`KHOAN`))*
- `[e8]` **ngày 01/02/2010** → `NGAY_THAM_CHIEU` (span: `[37:39]`) *(lồng trong `e5` (`KHOAN`))*
- `[e9]` **ngày 27/5/2010** → `NGAY_THAM_CHIEU` (span: `[56:58]`) *(lồng trong `e5` (`KHOAN`))*
- `[e10]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_THAM_QUYEN` (span: `[40:44]`) *(lồng trong `e5` (`KHOAN`))*
- `[e11]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_THAM_QUYEN` (span: `[59:63]`) *(lồng trong `e5` (`KHOAN`))*
- `[e12]` **hồ sơ yêu cầu** → `GIAY_TO_HO_SO` (span: `[47:49]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 11/2015/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 11/2015/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 11/2015/TT-BKHĐT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Đấu thầu `[LINH_VUC]`)
- (`e4` Điều 5 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 11/2015/TT-BKHĐT `[SO_HIEU]`)
- (`e5` 1 . Thông tư này có hiệu lực thi hành kể từ ngày 22 tháng 12 năm 2015 . Thông tư này thay thế Thông tư số 04/2010/TT-BKH ngày 01/02/2010 của Bộ Kế hoạch và Đầu tư quy định chi tiết lập hồ sơ yêu cầu chỉ định thầu xây lắp , Thông tư số 11/2010/TT-BKH ngày 27/5/2010 của Bộ Kế hoạch và Đầu tư quy định chi tiết về chào hàng cạnh tranh . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 5 `[DIEU]`)
- (`e1` 11/2015/TT-BKHĐT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Đấu thầu `[LINH_VUC]`)
- (`e5` 1 . Thông tư này có hiệu lực thi hành kể từ ngày 22 tháng 12 năm 2015 . Thông tư này thay thế Thông tư số 04/2010/TT-BKH ngày 01/02/2010 của Bộ Kế hoạch và Đầu tư quy định chi tiết lập hồ sơ yêu cầu chỉ định thầu xây lắp , Thông tư số 11/2010/TT-BKH ngày 27/5/2010 của Bộ Kế hoạch và Đầu tư quy định chi tiết về chào hàng cạnh tranh . `[KHOAN]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Đấu thầu `[LINH_VUC]`)
- (`e5` 1 . Thông tư này có hiệu lực thi hành kể từ ngày 22 tháng 12 năm 2015 . Thông tư này thay thế Thông tư số 04/2010/TT-BKH ngày 01/02/2010 của Bộ Kế hoạch và Đầu tư quy định chi tiết lập hồ sơ yêu cầu chỉ định thầu xây lắp , Thông tư số 11/2010/TT-BKH ngày 27/5/2010 của Bộ Kế hoạch và Đầu tư quy định chi tiết về chào hàng cạnh tranh . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e6` Thông tư số 04/2010/TT-BKH `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e5` 1 . Thông tư này có hiệu lực thi hành kể từ ngày 22 tháng 12 năm 2015 . Thông tư này thay thế Thông tư số 04/2010/TT-BKH ngày 01/02/2010 của Bộ Kế hoạch và Đầu tư quy định chi tiết lập hồ sơ yêu cầu chỉ định thầu xây lắp , Thông tư số 11/2010/TT-BKH ngày 27/5/2010 của Bộ Kế hoạch và Đầu tư quy định chi tiết về chào hàng cạnh tranh . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e7` Thông tư số 11/2010/TT-BKH `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e6` Thông tư số 04/2010/TT-BKH `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e8` ngày 01/02/2010 `[NGAY_THAM_CHIEU]`)
- (`e7` Thông tư số 11/2010/TT-BKH `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e9` ngày 27/5/2010 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #11_2015_TT-BKHĐT_92514#body_standalone_51 (Loại: `body_standalone`)
> **[Điều 5]`<DIEU>`** . **[1 . Thông tư này có hiệu lực thi hành kể từ ngày 22 tháng 12 năm 2015 . Thông tư này thay thế **[Thông tư số 04/2010/TT-BKH]`<THAM_CHIEU_PHAP_LY>`** **[ngày 01/02/2010]`<NGAY_THAM_CHIEU>`** của **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_THAM_QUYEN>`** quy định chi tiết lập **[hồ sơ yêu cầu]`<GIAY_TO_HO_SO>`** chỉ định thầu xây lắp , **[Thông tư số 11/2010/TT-BKH]`<THAM_CHIEU_PHAP_LY>`** **[ngày 27/5/2010]`<NGAY_THAM_CHIEU>`** của **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_THAM_QUYEN>`** quy định chi tiết về chào hàng cạnh tranh .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 5** → `DIEU` (span: `[0:2]`)
- `[e1]` **1 . Thông tư này có hiệu lực thi hành kể từ ngày 22 tháng 12 năm 2015 . Thông tư này thay thế Thông tư số 04/2010/TT-BKH ngày 01/02/2010 của Bộ Kế hoạch và Đầu tư quy định chi tiết lập hồ sơ yêu cầu chỉ định thầu xây lắp , Thông tư số 11/2010/TT-BKH ngày 27/5/2010 của Bộ Kế hoạch và Đầu tư quy định chi tiết về chào hàng cạnh tranh .** → `KHOAN` (span: `[3:57]`)
- `[e2]` **Thông tư số 04/2010/TT-BKH** → `THAM_CHIEU_PHAP_LY` (span: `[22:25]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **Thông tư số 11/2010/TT-BKH** → `THAM_CHIEU_PHAP_LY` (span: `[41:44]`) *(lồng trong `e1` (`KHOAN`))*
- `[e4]` **ngày 01/02/2010** → `NGAY_THAM_CHIEU` (span: `[25:27]`) *(lồng trong `e1` (`KHOAN`))*
- `[e5]` **ngày 27/5/2010** → `NGAY_THAM_CHIEU` (span: `[44:46]`) *(lồng trong `e1` (`KHOAN`))*
- `[e6]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_THAM_QUYEN` (span: `[28:32]`) *(lồng trong `e1` (`KHOAN`))*
- `[e7]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_THAM_QUYEN` (span: `[47:51]`) *(lồng trong `e1` (`KHOAN`))*
- `[e8]` **hồ sơ yêu cầu** → `GIAY_TO_HO_SO` (span: `[35:37]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 1 . Thông tư này có hiệu lực thi hành kể từ ngày 22 tháng 12 năm 2015 . Thông tư này thay thế Thông tư số 04/2010/TT-BKH ngày 01/02/2010 của Bộ Kế hoạch và Đầu tư quy định chi tiết lập hồ sơ yêu cầu chỉ định thầu xây lắp , Thông tư số 11/2010/TT-BKH ngày 27/5/2010 của Bộ Kế hoạch và Đầu tư quy định chi tiết về chào hàng cạnh tranh . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 5 `[DIEU]`)
- (`e1` 1 . Thông tư này có hiệu lực thi hành kể từ ngày 22 tháng 12 năm 2015 . Thông tư này thay thế Thông tư số 04/2010/TT-BKH ngày 01/02/2010 của Bộ Kế hoạch và Đầu tư quy định chi tiết lập hồ sơ yêu cầu chỉ định thầu xây lắp , Thông tư số 11/2010/TT-BKH ngày 27/5/2010 của Bộ Kế hoạch và Đầu tư quy định chi tiết về chào hàng cạnh tranh . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e2` Thông tư số 04/2010/TT-BKH `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e1` 1 . Thông tư này có hiệu lực thi hành kể từ ngày 22 tháng 12 năm 2015 . Thông tư này thay thế Thông tư số 04/2010/TT-BKH ngày 01/02/2010 của Bộ Kế hoạch và Đầu tư quy định chi tiết lập hồ sơ yêu cầu chỉ định thầu xây lắp , Thông tư số 11/2010/TT-BKH ngày 27/5/2010 của Bộ Kế hoạch và Đầu tư quy định chi tiết về chào hàng cạnh tranh . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Thông tư số 11/2010/TT-BKH `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e2` Thông tư số 04/2010/TT-BKH `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e4` ngày 01/02/2010 `[NGAY_THAM_CHIEU]`)
- (`e3` Thông tư số 11/2010/TT-BKH `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e5` ngày 27/5/2010 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #11_2015_TT-BKHĐT_92514#body_context_52 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[11/2015/TT-BKHĐT]`<SO_HIEU>`** ban hành **[ngày 27 tháng 10 năm 2015]`<NGAY_BAN_HANH>`** bởi **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** . **[Điều 5]`<DIEU>`** . **[2 . Các Bộ , cơ quan ngang Bộ , cơ quan thuộc **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** , cơ quan khác ở Trung ương , **[Ủy ban nhân dân các cấp]`<CO_QUAN_THAM_QUYEN>`** và tổ chức , cá nhân có liên quan chịu trách nhiệm thi hành Thông tư này . Trong quá trình thực hiện , nếu có vướng mắc , đề nghị các Bộ , cơ quan ngang Bộ , cơ quan thuộc **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** , cơ quan khác ở Trung ương , **[Ủy ban nhân dân các cấp]`<CO_QUAN_THAM_QUYEN>`** và tổ chức , cá nhân có liên quan gửi ý kiến về **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_THAM_QUYEN>`**]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **11/2015/TT-BKHĐT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[11:15]`)
- `[e3]` **ngày 27 tháng 10 năm 2015** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 5** → `DIEU` (span: `[16:18]`)
- `[e5]` **2 . Các Bộ , cơ quan ngang Bộ , cơ quan thuộc Chính phủ , cơ quan khác ở Trung ương , Ủy ban nhân dân các cấp và tổ chức , cá nhân có liên quan chịu trách nhiệm thi hành Thông tư này . Trong quá trình thực hiện , nếu có vướng mắc , đề nghị các Bộ , cơ quan ngang Bộ , cơ quan thuộc Chính phủ , cơ quan khác ở Trung ương , Ủy ban nhân dân các cấp và tổ chức , cá nhân có liên quan gửi ý kiến về Bộ Kế hoạch và Đầu tư** → `KHOAN` (span: `[19:95]`)
- `[e6]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[30:31]`) *(lồng trong `e5` (`KHOAN`))*
- `[e7]` **Ủy ban nhân dân các cấp** → `CO_QUAN_THAM_QUYEN` (span: `[37:41]`) *(lồng trong `e5` (`KHOAN`))*
- `[e8]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[71:72]`) *(lồng trong `e5` (`KHOAN`))*
- `[e9]` **Ủy ban nhân dân các cấp** → `CO_QUAN_THAM_QUYEN` (span: `[78:82]`) *(lồng trong `e5` (`KHOAN`))*
- `[e10]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_THAM_QUYEN` (span: `[91:95]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 11/2015/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 11/2015/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 11/2015/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 27 tháng 10 năm 2015 `[NGAY_BAN_HANH]`)
- (`e4` Điều 5 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 11/2015/TT-BKHĐT `[SO_HIEU]`)
- (`e5` 2 . Các Bộ , cơ quan ngang Bộ , cơ quan thuộc Chính phủ , cơ quan khác ở Trung ương , Ủy ban nhân dân các cấp và tổ chức , cá nhân có liên quan chịu trách nhiệm thi hành Thông tư này . Trong quá trình thực hiện , nếu có vướng mắc , đề nghị các Bộ , cơ quan ngang Bộ , cơ quan thuộc Chính phủ , cơ quan khác ở Trung ương , Ủy ban nhân dân các cấp và tổ chức , cá nhân có liên quan gửi ý kiến về Bộ Kế hoạch và Đầu tư `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 5 `[DIEU]`)


---

### Mẫu #11_2015_TT-BKHĐT_92514#body_standalone_53 (Loại: `body_standalone`)
> **[Điều 5]`<DIEU>`** . **[2 . Các Bộ , cơ quan ngang Bộ , cơ quan thuộc **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** , cơ quan khác ở Trung ương , **[Ủy ban nhân dân các cấp]`<CO_QUAN_THAM_QUYEN>`** và tổ chức , cá nhân có liên quan chịu trách nhiệm thi hành Thông tư này . Trong quá trình thực hiện , nếu có vướng mắc , đề nghị các Bộ , cơ quan ngang Bộ , cơ quan thuộc **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** , cơ quan khác ở Trung ương , **[Ủy ban nhân dân các cấp]`<CO_QUAN_THAM_QUYEN>`** và tổ chức , cá nhân có liên quan gửi ý kiến về **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_THAM_QUYEN>`**]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 5** → `DIEU` (span: `[0:2]`)
- `[e1]` **2 . Các Bộ , cơ quan ngang Bộ , cơ quan thuộc Chính phủ , cơ quan khác ở Trung ương , Ủy ban nhân dân các cấp và tổ chức , cá nhân có liên quan chịu trách nhiệm thi hành Thông tư này . Trong quá trình thực hiện , nếu có vướng mắc , đề nghị các Bộ , cơ quan ngang Bộ , cơ quan thuộc Chính phủ , cơ quan khác ở Trung ương , Ủy ban nhân dân các cấp và tổ chức , cá nhân có liên quan gửi ý kiến về Bộ Kế hoạch và Đầu tư** → `KHOAN` (span: `[3:79]`)
- `[e2]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[14:15]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **Ủy ban nhân dân các cấp** → `CO_QUAN_THAM_QUYEN` (span: `[21:25]`) *(lồng trong `e1` (`KHOAN`))*
- `[e4]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[55:56]`) *(lồng trong `e1` (`KHOAN`))*
- `[e5]` **Ủy ban nhân dân các cấp** → `CO_QUAN_THAM_QUYEN` (span: `[62:66]`) *(lồng trong `e1` (`KHOAN`))*
- `[e6]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_THAM_QUYEN` (span: `[75:79]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 2 . Các Bộ , cơ quan ngang Bộ , cơ quan thuộc Chính phủ , cơ quan khác ở Trung ương , Ủy ban nhân dân các cấp và tổ chức , cá nhân có liên quan chịu trách nhiệm thi hành Thông tư này . Trong quá trình thực hiện , nếu có vướng mắc , đề nghị các Bộ , cơ quan ngang Bộ , cơ quan thuộc Chính phủ , cơ quan khác ở Trung ương , Ủy ban nhân dân các cấp và tổ chức , cá nhân có liên quan gửi ý kiến về Bộ Kế hoạch và Đầu tư `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 5 `[DIEU]`)


---

### Mẫu #11_2015_TT-BKHĐT_92514#body_context_54 (Loại: `body_context`)
> **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[11/2015/TT-BKHĐT]`<SO_HIEU>`** . **[Điều 1 . Phạm vi điều chỉnh]`<DIEU>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[5:6]`)
- `[e1]` **11/2015/TT-BKHĐT** → `SO_HIEU` (span: `[7:8]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[0:4]`)
- `[e3]` **Điều 1 . Phạm vi điều chỉnh** → `DIEU` (span: `[9:14]`)

**Quan hệ:**
- (`e1` 11/2015/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 11/2015/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 1 . Phạm vi điều chỉnh `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 11/2015/TT-BKHĐT `[SO_HIEU]`)


---

### Mẫu #11_2015_TT-BKHĐT_92514#body_context_55 (Loại: `body_context`)
> **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[11/2015/TT-BKHĐT]`<SO_HIEU>`** . **[Điều 2 . Đối tượng áp dụng]`<DIEU>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[5:6]`)
- `[e1]` **11/2015/TT-BKHĐT** → `SO_HIEU` (span: `[7:8]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[0:4]`)
- `[e3]` **Điều 2 . Đối tượng áp dụng** → `DIEU` (span: `[9:14]`)

**Quan hệ:**
- (`e1` 11/2015/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 11/2015/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 2 . Đối tượng áp dụng `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 11/2015/TT-BKHĐT `[SO_HIEU]`)


---

### Mẫu #11_2015_TT-BKHĐT_92514#body_context_56 (Loại: `body_context`)
> **[Bộ Kế hoạch và Đầu tư]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[11/2015/TT-BKHĐT]`<SO_HIEU>`** . **[Điều 5 . Tổ chức thực hiện]`<DIEU>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[5:6]`)
- `[e1]` **11/2015/TT-BKHĐT** → `SO_HIEU` (span: `[7:8]`)
- `[e2]` **Bộ Kế hoạch và Đầu tư** → `CO_QUAN_BAN_HANH` (span: `[0:4]`)
- `[e3]` **Điều 5 . Tổ chức thực hiện** → `DIEU` (span: `[9:14]`)

**Quan hệ:**
- (`e1` 11/2015/TT-BKHĐT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Kế hoạch và Đầu tư `[CO_QUAN_BAN_HANH]`)
- (`e1` 11/2015/TT-BKHĐT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 5 . Tổ chức thực hiện `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 11/2015/TT-BKHĐT `[SO_HIEU]`)


---

### Mẫu #11_2015_TT-BKHĐT_92514#hard_negative_57 (Loại: `hard_negative`)
> CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM


---
