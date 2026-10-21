# Dữ liệu gán nhãn văn bản: 10_2006_QĐ-BGTVT_16426
- **Thể loại**: `quyet_dinh`
- **Phân vùng dữ liệu**: `TRAIN`
- **Tổng số mẫu**: 16 mẫu
- **Tổng số thực thể**: 72
- **Tổng số quan hệ**: 51

---

### Mẫu #10_2006_QĐ-BGTVT_16426#header_0 (Loại: `header`)
> **[BỘ GIAO THÔNG VẬN TẢI]`<CO_QUAN_BAN_HANH>`** . CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM . Độc lập – Tự do – Hạnh phúc . Số : **[10/2006/QĐ-BGTVT]`<SO_HIEU>`** . **[Ngày 20 tháng 2 năm 2006]`<NGAY_BAN_HANH>`** . **[QUYẾT ĐỊNH]`<LOAI_VAN_BAN>`**

**Thực thể:**
- `[e0]` **10/2006/QĐ-BGTVT** → `SO_HIEU` (span: `[19:20]`)
- `[e1]` **Ngày 20 tháng 2 năm 2006** → `NGAY_BAN_HANH` (span: `[21:27]`)
- `[e2]` **BỘ GIAO THÔNG VẬN TẢI** → `CO_QUAN_BAN_HANH` (span: `[0:3]`)
- `[e3]` **QUYẾT ĐỊNH** → `LOAI_VAN_BAN` (span: `[28:29]`)

**Quan hệ:**
- (`e0` 10/2006/QĐ-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` BỘ GIAO THÔNG VẬN TẢI `[CO_QUAN_BAN_HANH]`)
- (`e0` 10/2006/QĐ-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e1` Ngày 20 tháng 2 năm 2006 `[NGAY_BAN_HANH]`)
- (`e0` 10/2006/QĐ-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e3` QUYẾT ĐỊNH `[LOAI_VAN_BAN]`)


---

### Mẫu #10_2006_QĐ-BGTVT_16426#meta_1 (Loại: `meta`)
> **[BỘ GIAO THÔNG VẬN TẢI]`<CO_QUAN_BAN_HANH>`** . CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM . Độc lập – Tự do – Hạnh phúc . Số : **[10/2006/QĐ-BGTVT]`<SO_HIEU>`** . Ngày 20 tháng 2 năm 2006 . **[QUYẾT ĐỊNH]`<LOAI_VAN_BAN>`** . Số đăng ký : 22 TCN 332 - 06 . Điều 2 . Quyết định này có hiệu lực thi hành sau 15 ngày , kể từ ngày đăng Công báo .

**Thực thể:**
- `[e0]` **10/2006/QĐ-BGTVT** → `SO_HIEU` (span: `[19:20]`)
- `[e1]` **BỘ GIAO THÔNG VẬN TẢI** → `CO_QUAN_BAN_HANH` (span: `[0:3]`)
- `[e2]` **QUYẾT ĐỊNH** → `LOAI_VAN_BAN` (span: `[28:29]`)

**Quan hệ:**
- (`e0` 10/2006/QĐ-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e1` BỘ GIAO THÔNG VẬN TẢI `[CO_QUAN_BAN_HANH]`)
- (`e0` 10/2006/QĐ-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e2` QUYẾT ĐỊNH `[LOAI_VAN_BAN]`)


---

### Mẫu #10_2006_QĐ-BGTVT_16426#preamble_context_2 (Loại: `preamble_context`)
> **[Quyết định]`<LOAI_VAN_BAN>`** số **[10/2006/QĐ-BGTVT]`<SO_HIEU>`** của **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** . **[BỘ TRƯỞNG BỘ GIAO THÔNG VẬN TẢI]`<CO_QUAN_THAM_QUYEN>`**

**Thực thể:**
- `[e0]` **Quyết định** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **10/2006/QĐ-BGTVT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[4:7]`)
- `[e3]` **BỘ TRƯỞNG BỘ GIAO THÔNG VẬN TẢI** → `CO_QUAN_THAM_QUYEN` (span: `[8:12]`)

**Quan hệ:**
- (`e1` 10/2006/QĐ-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 10/2006/QĐ-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Quyết định `[LOAI_VAN_BAN]`)


---

### Mẫu #10_2006_QĐ-BGTVT_16426#preamble_standalone_3 (Loại: `preamble_standalone`)
> **[BỘ TRƯỞNG BỘ GIAO THÔNG VẬN TẢI]`<CO_QUAN_THAM_QUYEN>`**

**Thực thể:**
- `[e0]` **BỘ TRƯỞNG BỘ GIAO THÔNG VẬN TẢI** → `CO_QUAN_THAM_QUYEN` (span: `[0:4]`)


---

### Mẫu #10_2006_QĐ-BGTVT_16426#preamble_context_4 (Loại: `preamble_context`)
> **[Quyết định]`<LOAI_VAN_BAN>`** số **[10/2006/QĐ-BGTVT]`<SO_HIEU>`** của **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** . **[Căn cứ]`<TU_KHOA_PHAP_LY>`** **[Luật Ban hành văn bản quy phạm pháp luật]`<THAM_CHIEU_PHAP_LY>`** **[ngày 12 tháng 11 năm 1996]`<NGAY_THAM_CHIEU>`** và **[Luật sửa đổi , bổ sung một số điều của Luật Ban hành văn bản quy phạm pháp luật]`<THAM_CHIEU_PHAP_LY>`** **[ngày 16 tháng 12 năm 2002]`<NGAY_THAM_CHIEU>`** ;

**Thực thể:**
- `[e0]` **Quyết định** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **10/2006/QĐ-BGTVT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[4:7]`)
- `[e3]` **Luật Ban hành văn bản quy phạm pháp luật** → `THAM_CHIEU_PHAP_LY` (span: `[9:12]`)
- `[e4]` **Luật sửa đổi , bổ sung một số điều của Luật Ban hành văn bản quy phạm pháp luật** → `THAM_CHIEU_PHAP_LY` (span: `[19:29]`)
- `[e5]` **Căn cứ** → `TU_KHOA_PHAP_LY` (span: `[8:9]`)
- `[e6]` **ngày 12 tháng 11 năm 1996** → `NGAY_THAM_CHIEU` (span: `[12:18]`)
- `[e7]` **ngày 16 tháng 12 năm 2002** → `NGAY_THAM_CHIEU` (span: `[29:35]`)

**Quan hệ:**
- (`e1` 10/2006/QĐ-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 10/2006/QĐ-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Quyết định `[LOAI_VAN_BAN]`)
- (`e5` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Luật Ban hành văn bản quy phạm pháp luật `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 10/2006/QĐ-BGTVT `[SO_HIEU]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Luật Ban hành văn bản quy phạm pháp luật `[THAM_CHIEU_PHAP_LY]`)
- (`e5` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e4` Luật sửa đổi , bổ sung một số điều của Luật Ban hành văn bản quy phạm pháp luật `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 10/2006/QĐ-BGTVT `[SO_HIEU]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e4` Luật sửa đổi , bổ sung một số điều của Luật Ban hành văn bản quy phạm pháp luật `[THAM_CHIEU_PHAP_LY]`)
- (`e3` Luật Ban hành văn bản quy phạm pháp luật `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e6` ngày 12 tháng 11 năm 1996 `[NGAY_THAM_CHIEU]`)
- (`e4` Luật sửa đổi , bổ sung một số điều của Luật Ban hành văn bản quy phạm pháp luật `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e7` ngày 16 tháng 12 năm 2002 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #10_2006_QĐ-BGTVT_16426#preamble_standalone_5 (Loại: `preamble_standalone`)
> **[Căn cứ]`<TU_KHOA_PHAP_LY>`** **[Luật Ban hành văn bản quy phạm pháp luật]`<THAM_CHIEU_PHAP_LY>`** **[ngày 12 tháng 11 năm 1996]`<NGAY_THAM_CHIEU>`** và **[Luật sửa đổi , bổ sung một số điều của Luật Ban hành văn bản quy phạm pháp luật]`<THAM_CHIEU_PHAP_LY>`** **[ngày 16 tháng 12 năm 2002]`<NGAY_THAM_CHIEU>`** ;

**Thực thể:**
- `[e0]` **Luật Ban hành văn bản quy phạm pháp luật** → `THAM_CHIEU_PHAP_LY` (span: `[1:4]`)
- `[e1]` **Luật sửa đổi , bổ sung một số điều của Luật Ban hành văn bản quy phạm pháp luật** → `THAM_CHIEU_PHAP_LY` (span: `[11:21]`)
- `[e2]` **Căn cứ** → `TU_KHOA_PHAP_LY` (span: `[0:1]`)
- `[e3]` **ngày 12 tháng 11 năm 1996** → `NGAY_THAM_CHIEU` (span: `[4:10]`)
- `[e4]` **ngày 16 tháng 12 năm 2002** → `NGAY_THAM_CHIEU` (span: `[21:27]`)

**Quan hệ:**
- (`e2` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e0` Luật Ban hành văn bản quy phạm pháp luật `[THAM_CHIEU_PHAP_LY]`)
- (`e2` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e1` Luật sửa đổi , bổ sung một số điều của Luật Ban hành văn bản quy phạm pháp luật `[THAM_CHIEU_PHAP_LY]`)
- (`e0` Luật Ban hành văn bản quy phạm pháp luật `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e3` ngày 12 tháng 11 năm 1996 `[NGAY_THAM_CHIEU]`)
- (`e1` Luật sửa đổi , bổ sung một số điều của Luật Ban hành văn bản quy phạm pháp luật `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e4` ngày 16 tháng 12 năm 2002 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #10_2006_QĐ-BGTVT_16426#preamble_context_6 (Loại: `preamble_context`)
> **[Quyết định]`<LOAI_VAN_BAN>`** số **[10/2006/QĐ-BGTVT]`<SO_HIEU>`** của **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** . **[Căn cứ]`<TU_KHOA_PHAP_LY>`** **[Luật Giao thông đường bộ]`<THAM_CHIEU_PHAP_LY>`** **[ngày 29 tháng 6 năm 2001]`<NGAY_THAM_CHIEU>`** ;

**Thực thể:**
- `[e0]` **Quyết định** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **10/2006/QĐ-BGTVT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[4:7]`)
- `[e3]` **Luật Giao thông đường bộ** → `THAM_CHIEU_PHAP_LY` (span: `[9:12]`)
- `[e4]` **Căn cứ** → `TU_KHOA_PHAP_LY` (span: `[8:9]`)
- `[e5]` **ngày 29 tháng 6 năm 2001** → `NGAY_THAM_CHIEU` (span: `[12:18]`)

**Quan hệ:**
- (`e1` 10/2006/QĐ-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 10/2006/QĐ-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Quyết định `[LOAI_VAN_BAN]`)
- (`e4` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Luật Giao thông đường bộ `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 10/2006/QĐ-BGTVT `[SO_HIEU]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Luật Giao thông đường bộ `[THAM_CHIEU_PHAP_LY]`)
- (`e3` Luật Giao thông đường bộ `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e5` ngày 29 tháng 6 năm 2001 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #10_2006_QĐ-BGTVT_16426#preamble_standalone_7 (Loại: `preamble_standalone`)
> **[Căn cứ]`<TU_KHOA_PHAP_LY>`** **[Luật Giao thông đường bộ]`<THAM_CHIEU_PHAP_LY>`** **[ngày 29 tháng 6 năm 2001]`<NGAY_THAM_CHIEU>`** ;

**Thực thể:**
- `[e0]` **Luật Giao thông đường bộ** → `THAM_CHIEU_PHAP_LY` (span: `[1:4]`)
- `[e1]` **Căn cứ** → `TU_KHOA_PHAP_LY` (span: `[0:1]`)
- `[e2]` **ngày 29 tháng 6 năm 2001** → `NGAY_THAM_CHIEU` (span: `[4:10]`)

**Quan hệ:**
- (`e1` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e0` Luật Giao thông đường bộ `[THAM_CHIEU_PHAP_LY]`)
- (`e0` Luật Giao thông đường bộ `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e2` ngày 29 tháng 6 năm 2001 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #10_2006_QĐ-BGTVT_16426#preamble_context_8 (Loại: `preamble_context`)
> **[Quyết định]`<LOAI_VAN_BAN>`** số **[10/2006/QĐ-BGTVT]`<SO_HIEU>`** của **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** . **[Căn cứ]`<TU_KHOA_PHAP_LY>`** **[Pháp lệnh Chất lượng hàng hóa]`<THAM_CHIEU_PHAP_LY>`** **[ngày 24 tháng 12 năm 1999]`<NGAY_THAM_CHIEU>`** ;

**Thực thể:**
- `[e0]` **Quyết định** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **10/2006/QĐ-BGTVT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[4:7]`)
- `[e3]` **Pháp lệnh Chất lượng hàng hóa** → `THAM_CHIEU_PHAP_LY` (span: `[9:12]`)
- `[e4]` **Căn cứ** → `TU_KHOA_PHAP_LY` (span: `[8:9]`)
- `[e5]` **ngày 24 tháng 12 năm 1999** → `NGAY_THAM_CHIEU` (span: `[12:18]`)

**Quan hệ:**
- (`e1` 10/2006/QĐ-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 10/2006/QĐ-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Quyết định `[LOAI_VAN_BAN]`)
- (`e4` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Pháp lệnh Chất lượng hàng hóa `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 10/2006/QĐ-BGTVT `[SO_HIEU]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Pháp lệnh Chất lượng hàng hóa `[THAM_CHIEU_PHAP_LY]`)
- (`e3` Pháp lệnh Chất lượng hàng hóa `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e5` ngày 24 tháng 12 năm 1999 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #10_2006_QĐ-BGTVT_16426#preamble_standalone_9 (Loại: `preamble_standalone`)
> **[Căn cứ]`<TU_KHOA_PHAP_LY>`** **[Pháp lệnh Chất lượng hàng hóa]`<THAM_CHIEU_PHAP_LY>`** **[ngày 24 tháng 12 năm 1999]`<NGAY_THAM_CHIEU>`** ;

**Thực thể:**
- `[e0]` **Pháp lệnh Chất lượng hàng hóa** → `THAM_CHIEU_PHAP_LY` (span: `[1:4]`)
- `[e1]` **Căn cứ** → `TU_KHOA_PHAP_LY` (span: `[0:1]`)
- `[e2]` **ngày 24 tháng 12 năm 1999** → `NGAY_THAM_CHIEU` (span: `[4:10]`)

**Quan hệ:**
- (`e1` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e0` Pháp lệnh Chất lượng hàng hóa `[THAM_CHIEU_PHAP_LY]`)
- (`e0` Pháp lệnh Chất lượng hàng hóa `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e2` ngày 24 tháng 12 năm 1999 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #10_2006_QĐ-BGTVT_16426#preamble_context_10 (Loại: `preamble_context`)
> **[Quyết định]`<LOAI_VAN_BAN>`** số **[10/2006/QĐ-BGTVT]`<SO_HIEU>`** của **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** . **[Căn cứ]`<TU_KHOA_PHAP_LY>`** **[Nghị định số 34/2003/NĐ-CP]`<THAM_CHIEU_PHAP_LY>`** **[ngày 04 tháng 4 năm 2003]`<NGAY_THAM_CHIEU>`** của **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** quy định chức năng , nhiệm vụ , quyền hạn và cơ cấu tổ chức **[Bộ Giao thông vận tải]`<CO_QUAN_THAM_QUYEN>`** ;

**Thực thể:**
- `[e0]` **Quyết định** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **10/2006/QĐ-BGTVT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[4:7]`)
- `[e3]` **Nghị định số 34/2003/NĐ-CP** → `THAM_CHIEU_PHAP_LY` (span: `[9:12]`)
- `[e4]` **Căn cứ** → `TU_KHOA_PHAP_LY` (span: `[8:9]`)
- `[e5]` **ngày 04 tháng 4 năm 2003** → `NGAY_THAM_CHIEU` (span: `[12:18]`)
- `[e6]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[19:20]`)
- `[e7]` **Bộ Giao thông vận tải** → `CO_QUAN_THAM_QUYEN` (span: `[29:32]`)

**Quan hệ:**
- (`e1` 10/2006/QĐ-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 10/2006/QĐ-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Quyết định `[LOAI_VAN_BAN]`)
- (`e4` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Nghị định số 34/2003/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 10/2006/QĐ-BGTVT `[SO_HIEU]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Nghị định số 34/2003/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e3` Nghị định số 34/2003/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e5` ngày 04 tháng 4 năm 2003 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #10_2006_QĐ-BGTVT_16426#preamble_standalone_11 (Loại: `preamble_standalone`)
> **[Căn cứ]`<TU_KHOA_PHAP_LY>`** **[Nghị định số 34/2003/NĐ-CP]`<THAM_CHIEU_PHAP_LY>`** **[ngày 04 tháng 4 năm 2003]`<NGAY_THAM_CHIEU>`** của **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** quy định chức năng , nhiệm vụ , quyền hạn và cơ cấu tổ chức **[Bộ Giao thông vận tải]`<CO_QUAN_THAM_QUYEN>`** ;

**Thực thể:**
- `[e0]` **Nghị định số 34/2003/NĐ-CP** → `THAM_CHIEU_PHAP_LY` (span: `[1:4]`)
- `[e1]` **Căn cứ** → `TU_KHOA_PHAP_LY` (span: `[0:1]`)
- `[e2]` **ngày 04 tháng 4 năm 2003** → `NGAY_THAM_CHIEU` (span: `[4:10]`)
- `[e3]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[11:12]`)
- `[e4]` **Bộ Giao thông vận tải** → `CO_QUAN_THAM_QUYEN` (span: `[21:24]`)

**Quan hệ:**
- (`e1` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e0` Nghị định số 34/2003/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e3` Chính phủ `[CO_QUAN_THAM_QUYEN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e0` Nghị định số 34/2003/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e0` Nghị định số 34/2003/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e2` ngày 04 tháng 4 năm 2003 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #10_2006_QĐ-BGTVT_16426#body_context_12 (Loại: `body_context`)
> **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** ban hành **[Quyết định]`<LOAI_VAN_BAN>`** số **[10/2006/QĐ-BGTVT]`<SO_HIEU>`** . **[Điều 1 . Ban hành kèm theo Quyết định này Tiêu chuẩn Ngành " Quy trình thí nghiệm xác định chỉ số CBR của đất , đá dăm trong phòng thí nghiệm " . Số đăng ký : 22 TCN 332 - 06]`<DIEU>`**

**Thực thể:**
- `[e0]` **Quyết định** → `LOAI_VAN_BAN` (span: `[4:5]`)
- `[e1]` **10/2006/QĐ-BGTVT** → `SO_HIEU` (span: `[6:7]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[0:3]`)
- `[e3]` **Điều 1 . Ban hành kèm theo Quyết định này Tiêu chuẩn Ngành " Quy trình thí nghiệm xác định chỉ số CBR của đất , đá dăm trong phòng thí nghiệm " . Số đăng ký : 22 TCN 332 - 06** → `DIEU` (span: `[8:41]`)

**Quan hệ:**
- (`e1` 10/2006/QĐ-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 10/2006/QĐ-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Quyết định `[LOAI_VAN_BAN]`)
- (`e3` Điều 1 . Ban hành kèm theo Quyết định này Tiêu chuẩn Ngành " Quy trình thí nghiệm xác định chỉ số CBR của đất , đá dăm trong phòng thí nghiệm " . Số đăng ký : 22 TCN 332 - 06 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 10/2006/QĐ-BGTVT `[SO_HIEU]`)


---

### Mẫu #10_2006_QĐ-BGTVT_16426#body_context_13 (Loại: `body_context`)
> **[Quyết định]`<LOAI_VAN_BAN>`** số **[10/2006/QĐ-BGTVT]`<SO_HIEU>`** ban hành **[ngày 20 tháng 02 năm 2006]`<NGAY_BAN_HANH>`** bởi **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** . **[Điều 2 . Quyết định này có hiệu lực thi hành **[sau 15 ngày]`<THOI_HAN>`** , kể từ ngày đăng Công báo .]`<DIEU>`**

**Thực thể:**
- `[e0]` **Quyết định** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **10/2006/QĐ-BGTVT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[11:14]`)
- `[e3]` **ngày 20 tháng 02 năm 2006** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 2 . Quyết định này có hiệu lực thi hành sau 15 ngày , kể từ ngày đăng Công báo .** → `DIEU` (span: `[15:33]`)
- `[e5]` **sau 15 ngày** → `THOI_HAN` (span: `[23:26]`) *(lồng trong `e4` (`DIEU`))*

**Quan hệ:**
- (`e1` 10/2006/QĐ-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 10/2006/QĐ-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Quyết định `[LOAI_VAN_BAN]`)
- (`e1` 10/2006/QĐ-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 20 tháng 02 năm 2006 `[NGAY_BAN_HANH]`)
- (`e4` Điều 2 . Quyết định này có hiệu lực thi hành sau 15 ngày , kể từ ngày đăng Công báo . `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 10/2006/QĐ-BGTVT `[SO_HIEU]`)


---

### Mẫu #10_2006_QĐ-BGTVT_16426#body_context_14 (Loại: `body_context`)
> **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** ban hành **[Quyết định]`<LOAI_VAN_BAN>`** số **[10/2006/QĐ-BGTVT]`<SO_HIEU>`** . **[Điều 3 . Chánh Văn phòng Bộ , **[Chánh Thanh tra Bộ]`<CO_QUAN_THAM_QUYEN>`** , Vụ trưởng Vụ Khoa học - Công nghệ , Viện trưởng Viện Khoa học và công nghệ giao thông vận tải , **[Giám đốc Sở Giao thông vận tải]`<CO_QUAN_THAM_QUYEN>`** , Sở Giao thông công chính và Thủ trưởng các đơn vị có liên quan chịu trách nhiệm thi hành Quyết định này . / .]`<DIEU>`**

**Thực thể:**
- `[e0]` **Quyết định** → `LOAI_VAN_BAN` (span: `[4:5]`)
- `[e1]` **10/2006/QĐ-BGTVT** → `SO_HIEU` (span: `[6:7]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[0:3]`)
- `[e3]` **Điều 3 . Chánh Văn phòng Bộ , Chánh Thanh tra Bộ , Vụ trưởng Vụ Khoa học - Công nghệ , Viện trưởng Viện Khoa học và công nghệ giao thông vận tải , Giám đốc Sở Giao thông vận tải , Sở Giao thông công chính và Thủ trưởng các đơn vị có liên quan chịu trách nhiệm thi hành Quyết định này . / .** → `DIEU` (span: `[8:55]`)
- `[e4]` **Chánh Thanh tra Bộ** → `CO_QUAN_THAM_QUYEN` (span: `[15:18]`) *(lồng trong `e3` (`DIEU`))*
- `[e5]` **Giám đốc Sở Giao thông vận tải** → `CO_QUAN_THAM_QUYEN` (span: `[33:37]`) *(lồng trong `e3` (`DIEU`))*

**Quan hệ:**
- (`e1` 10/2006/QĐ-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 10/2006/QĐ-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Quyết định `[LOAI_VAN_BAN]`)
- (`e3` Điều 3 . Chánh Văn phòng Bộ , Chánh Thanh tra Bộ , Vụ trưởng Vụ Khoa học - Công nghệ , Viện trưởng Viện Khoa học và công nghệ giao thông vận tải , Giám đốc Sở Giao thông vận tải , Sở Giao thông công chính và Thủ trưởng các đơn vị có liên quan chịu trách nhiệm thi hành Quyết định này . / . `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 10/2006/QĐ-BGTVT `[SO_HIEU]`)


---

### Mẫu #10_2006_QĐ-BGTVT_16426#hard_negative_15 (Loại: `hard_negative`)
> CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM


---
