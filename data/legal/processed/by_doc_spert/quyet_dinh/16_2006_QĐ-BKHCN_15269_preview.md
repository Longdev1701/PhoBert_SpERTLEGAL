# Dữ liệu gán nhãn văn bản: 16_2006_QĐ-BKHCN_15269
- **Thể loại**: `quyet_dinh`
- **Phân vùng dữ liệu**: `TRAIN`
- **Tổng số mẫu**: 13 mẫu
- **Tổng số thực thể**: 63
- **Tổng số quan hệ**: 47

---

### Mẫu #16_2006_QĐ-BKHCN_15269#header_0 (Loại: `header`)
> **[BỘ KHOA HỌC VÀ CÔNG NGHỆ]`<CO_QUAN_BAN_HANH>`** . CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM . Độc lập – Tự do – Hạnh phúc . Số : **[16/2006/QĐ-BKHCN]`<SO_HIEU>`** . Hà Nội , **[ngày 23 tháng 8 năm 2006]`<NGAY_BAN_HANH>`** . **[QUYẾT ĐỊNH]`<LOAI_VAN_BAN>`**

**Thực thể:**
- `[e0]` **16/2006/QĐ-BKHCN** → `SO_HIEU` (span: `[20:21]`)
- `[e1]` **ngày 23 tháng 8 năm 2006** → `NGAY_BAN_HANH` (span: `[24:30]`)
- `[e2]` **BỘ KHOA HỌC VÀ CÔNG NGHỆ** → `CO_QUAN_BAN_HANH` (span: `[0:4]`)
- `[e3]` **QUYẾT ĐỊNH** → `LOAI_VAN_BAN` (span: `[31:32]`)

**Quan hệ:**
- (`e0` 16/2006/QĐ-BKHCN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` BỘ KHOA HỌC VÀ CÔNG NGHỆ `[CO_QUAN_BAN_HANH]`)
- (`e0` 16/2006/QĐ-BKHCN `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e1` ngày 23 tháng 8 năm 2006 `[NGAY_BAN_HANH]`)
- (`e0` 16/2006/QĐ-BKHCN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e3` QUYẾT ĐỊNH `[LOAI_VAN_BAN]`)


---

### Mẫu #16_2006_QĐ-BKHCN_15269#signature_1 (Loại: `signature`)
> Điều 2 . Quyết định này có hiệu lực sau 15 ngày , kể từ ngày đăng Công báo . . KT. BỘ TRƯỞNG **[THỨ TRƯỞNG]`<CHUC_DANH_NGUOI_KY>`** ( Đã ký ) **[Bùi Mạnh Hải]`<NGUOI_KY>`**

**Thực thể:**
- `[e0]` **Bùi Mạnh Hải** → `NGUOI_KY` (span: `[25:26]`)
- `[e1]` **THỨ TRƯỞNG** → `CHUC_DANH_NGUOI_KY` (span: `[20:21]`)

**Quan hệ:**
- (`e0` Bùi Mạnh Hải `[NGUOI_KY]`) ==[ **GIU_CHUC_VU** ]==> (`e1` THỨ TRƯỞNG `[CHUC_DANH_NGUOI_KY]`)


---

### Mẫu #16_2006_QĐ-BKHCN_15269#meta_2 (Loại: `meta`)
> **[BỘ KHOA HỌC VÀ CÔNG NGHỆ]`<CO_QUAN_BAN_HANH>`** . CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM . Độc lập – Tự do – Hạnh phúc . Số : **[16/2006/QĐ-BKHCN]`<SO_HIEU>`** . Hà Nội , ngày 23 tháng 8 năm 2006 . **[QUYẾT ĐỊNH]`<LOAI_VAN_BAN>`** . Điều 2 . Quyết định này có hiệu lực sau 15 ngày , kể từ ngày đăng Công báo . . KT. BỘ TRƯỞNG **[THỨ TRƯỞNG]`<CHUC_DANH_NGUOI_KY>`** ( Đã ký ) **[Bùi Mạnh Hải]`<NGUOI_KY>`**

**Thực thể:**
- `[e0]` **16/2006/QĐ-BKHCN** → `SO_HIEU` (span: `[20:21]`)
- `[e1]` **BỘ KHOA HỌC VÀ CÔNG NGHỆ** → `CO_QUAN_BAN_HANH` (span: `[0:4]`)
- `[e2]` **QUYẾT ĐỊNH** → `LOAI_VAN_BAN` (span: `[31:32]`)
- `[e3]` **Bùi Mạnh Hải** → `NGUOI_KY` (span: `[58:59]`)
- `[e4]` **THỨ TRƯỞNG** → `CHUC_DANH_NGUOI_KY` (span: `[53:54]`)

**Quan hệ:**
- (`e0` 16/2006/QĐ-BKHCN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e1` BỘ KHOA HỌC VÀ CÔNG NGHỆ `[CO_QUAN_BAN_HANH]`)
- (`e0` 16/2006/QĐ-BKHCN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e2` QUYẾT ĐỊNH `[LOAI_VAN_BAN]`)
- (`e0` 16/2006/QĐ-BKHCN `[SO_HIEU]`) ==[ **KY_BOI** ]==> (`e3` Bùi Mạnh Hải `[NGUOI_KY]`)
- (`e3` Bùi Mạnh Hải `[NGUOI_KY]`) ==[ **GIU_CHUC_VU** ]==> (`e4` THỨ TRƯỞNG `[CHUC_DANH_NGUOI_KY]`)


---

### Mẫu #16_2006_QĐ-BKHCN_15269#preamble_context_3 (Loại: `preamble_context`)
> **[Quyết định]`<LOAI_VAN_BAN>`** số **[16/2006/QĐ-BKHCN]`<SO_HIEU>`** của **[Bộ Khoa học và Công nghệ]`<CO_QUAN_BAN_HANH>`** . **[BỘ TRƯỞNG BỘ KHOA HỌC VÀ CÔNG NGHỆ]`<CO_QUAN_THAM_QUYEN>`**

**Thực thể:**
- `[e0]` **Quyết định** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **16/2006/QĐ-BKHCN** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Khoa học và Công nghệ** → `CO_QUAN_BAN_HANH` (span: `[4:8]`)
- `[e3]` **BỘ TRƯỞNG BỘ KHOA HỌC VÀ CÔNG NGHỆ** → `CO_QUAN_THAM_QUYEN` (span: `[9:14]`)

**Quan hệ:**
- (`e1` 16/2006/QĐ-BKHCN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Khoa học và Công nghệ `[CO_QUAN_BAN_HANH]`)
- (`e1` 16/2006/QĐ-BKHCN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Quyết định `[LOAI_VAN_BAN]`)


---

### Mẫu #16_2006_QĐ-BKHCN_15269#preamble_standalone_4 (Loại: `preamble_standalone`)
> **[BỘ TRƯỞNG BỘ KHOA HỌC VÀ CÔNG NGHỆ]`<CO_QUAN_THAM_QUYEN>`**

**Thực thể:**
- `[e0]` **BỘ TRƯỞNG BỘ KHOA HỌC VÀ CÔNG NGHỆ** → `CO_QUAN_THAM_QUYEN` (span: `[0:5]`)


---

### Mẫu #16_2006_QĐ-BKHCN_15269#preamble_context_5 (Loại: `preamble_context`)
> **[Quyết định]`<LOAI_VAN_BAN>`** số **[16/2006/QĐ-BKHCN]`<SO_HIEU>`** của **[Bộ Khoa học và Công nghệ]`<CO_QUAN_BAN_HANH>`** . **[Căn cứ]`<TU_KHOA_PHAP_LY>`** **[Nghị định số 54/2003/NĐ-CP]`<THAM_CHIEU_PHAP_LY>`** **[ngày 19 tháng 05 năm 2003]`<NGAY_THAM_CHIEU>`** của **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** quy định chức năng , nhiệm vụ , quyền hạn và cơ cấu tổ chức của **[Bộ Khoa học và Công nghệ]`<CO_QUAN_THAM_QUYEN>`** và **[Nghị định số 28/2004/NĐ-CP]`<THAM_CHIEU_PHAP_LY>`** **[ngày 16 tháng 01 năm 2004]`<NGAY_THAM_CHIEU>`** của **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** về việc **[sửa đổi , bổ sung một số điều của]`<TU_KHOA_PHAP_LY>`** Nghị định 54/2003/NĐ-CP ;

**Thực thể:**
- `[e0]` **Quyết định** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **16/2006/QĐ-BKHCN** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Khoa học và Công nghệ** → `CO_QUAN_BAN_HANH` (span: `[4:8]`)
- `[e3]` **Nghị định số 54/2003/NĐ-CP** → `THAM_CHIEU_PHAP_LY` (span: `[10:13]`)
- `[e4]` **Nghị định số 28/2004/NĐ-CP** → `THAM_CHIEU_PHAP_LY` (span: `[36:39]`)
- `[e5]` **Căn cứ** → `TU_KHOA_PHAP_LY` (span: `[9:10]`)
- `[e6]` **sửa đổi , bổ sung một số điều của** → `TU_KHOA_PHAP_LY` (span: `[49:55]`)
- `[e7]` **ngày 19 tháng 05 năm 2003** → `NGAY_THAM_CHIEU` (span: `[13:19]`)
- `[e8]` **ngày 16 tháng 01 năm 2004** → `NGAY_THAM_CHIEU` (span: `[39:45]`)
- `[e9]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[20:21]`)
- `[e10]` **Bộ Khoa học và Công nghệ** → `CO_QUAN_THAM_QUYEN` (span: `[31:35]`)
- `[e11]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[46:47]`)

**Quan hệ:**
- (`e1` 16/2006/QĐ-BKHCN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Khoa học và Công nghệ `[CO_QUAN_BAN_HANH]`)
- (`e1` 16/2006/QĐ-BKHCN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Quyết định `[LOAI_VAN_BAN]`)
- (`e5` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Nghị định số 54/2003/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 16/2006/QĐ-BKHCN `[SO_HIEU]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Nghị định số 54/2003/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e5` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e4` Nghị định số 28/2004/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 16/2006/QĐ-BKHCN `[SO_HIEU]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e4` Nghị định số 28/2004/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e3` Nghị định số 54/2003/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e7` ngày 19 tháng 05 năm 2003 `[NGAY_THAM_CHIEU]`)
- (`e4` Nghị định số 28/2004/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e8` ngày 16 tháng 01 năm 2004 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #16_2006_QĐ-BKHCN_15269#preamble_standalone_6 (Loại: `preamble_standalone`)
> **[Căn cứ]`<TU_KHOA_PHAP_LY>`** **[Nghị định số 54/2003/NĐ-CP]`<THAM_CHIEU_PHAP_LY>`** **[ngày 19 tháng 05 năm 2003]`<NGAY_THAM_CHIEU>`** của **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** quy định chức năng , nhiệm vụ , quyền hạn và cơ cấu tổ chức của **[Bộ Khoa học và Công nghệ]`<CO_QUAN_THAM_QUYEN>`** và **[Nghị định số 28/2004/NĐ-CP]`<THAM_CHIEU_PHAP_LY>`** **[ngày 16 tháng 01 năm 2004]`<NGAY_THAM_CHIEU>`** của **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** về việc **[sửa đổi , bổ sung một số điều của]`<TU_KHOA_PHAP_LY>`** Nghị định 54/2003/NĐ-CP ;

**Thực thể:**
- `[e0]` **Nghị định số 54/2003/NĐ-CP** → `THAM_CHIEU_PHAP_LY` (span: `[1:4]`)
- `[e1]` **Nghị định số 28/2004/NĐ-CP** → `THAM_CHIEU_PHAP_LY` (span: `[27:30]`)
- `[e2]` **Căn cứ** → `TU_KHOA_PHAP_LY` (span: `[0:1]`)
- `[e3]` **sửa đổi , bổ sung một số điều của** → `TU_KHOA_PHAP_LY` (span: `[40:46]`)
- `[e4]` **ngày 19 tháng 05 năm 2003** → `NGAY_THAM_CHIEU` (span: `[4:10]`)
- `[e5]` **ngày 16 tháng 01 năm 2004** → `NGAY_THAM_CHIEU` (span: `[30:36]`)
- `[e6]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[11:12]`)
- `[e7]` **Bộ Khoa học và Công nghệ** → `CO_QUAN_THAM_QUYEN` (span: `[22:26]`)
- `[e8]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[37:38]`)

**Quan hệ:**
- (`e2` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e0` Nghị định số 54/2003/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e6` Chính phủ `[CO_QUAN_THAM_QUYEN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e0` Nghị định số 54/2003/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e2` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e1` Nghị định số 28/2004/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e7` Bộ Khoa học và Công nghệ `[CO_QUAN_THAM_QUYEN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e1` Nghị định số 28/2004/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e0` Nghị định số 54/2003/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e4` ngày 19 tháng 05 năm 2003 `[NGAY_THAM_CHIEU]`)
- (`e1` Nghị định số 28/2004/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e5` ngày 16 tháng 01 năm 2004 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #16_2006_QĐ-BKHCN_15269#preamble_context_7 (Loại: `preamble_context`)
> **[Quyết định]`<LOAI_VAN_BAN>`** số **[16/2006/QĐ-BKHCN]`<SO_HIEU>`** của **[Bộ Khoa học và Công nghệ]`<CO_QUAN_BAN_HANH>`** . **[Căn cứ]`<TU_KHOA_PHAP_LY>`** **[Quyết định số 444/QĐ-TTg]`<THAM_CHIEU_PHAP_LY>`** **[ngày 26 tháng 05 năm 2005]`<NGAY_THAM_CHIEU>`** của **[Thủ tướng Chính phủ]`<CO_QUAN_THAM_QUYEN>`** về việc phê duyệt Đề án triển khai thực hiện Hiệp định hàng rào kỹ thuật trong thương mại ;

**Thực thể:**
- `[e0]` **Quyết định** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **16/2006/QĐ-BKHCN** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Khoa học và Công nghệ** → `CO_QUAN_BAN_HANH` (span: `[4:8]`)
- `[e3]` **Quyết định số 444/QĐ-TTg** → `THAM_CHIEU_PHAP_LY` (span: `[10:13]`)
- `[e4]` **Căn cứ** → `TU_KHOA_PHAP_LY` (span: `[9:10]`)
- `[e5]` **ngày 26 tháng 05 năm 2005** → `NGAY_THAM_CHIEU` (span: `[13:19]`)
- `[e6]` **Thủ tướng Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[20:22]`)

**Quan hệ:**
- (`e1` 16/2006/QĐ-BKHCN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Khoa học và Công nghệ `[CO_QUAN_BAN_HANH]`)
- (`e1` 16/2006/QĐ-BKHCN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Quyết định `[LOAI_VAN_BAN]`)
- (`e4` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Quyết định số 444/QĐ-TTg `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 16/2006/QĐ-BKHCN `[SO_HIEU]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Quyết định số 444/QĐ-TTg `[THAM_CHIEU_PHAP_LY]`)
- (`e3` Quyết định số 444/QĐ-TTg `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e5` ngày 26 tháng 05 năm 2005 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #16_2006_QĐ-BKHCN_15269#preamble_standalone_8 (Loại: `preamble_standalone`)
> **[Căn cứ]`<TU_KHOA_PHAP_LY>`** **[Quyết định số 444/QĐ-TTg]`<THAM_CHIEU_PHAP_LY>`** **[ngày 26 tháng 05 năm 2005]`<NGAY_THAM_CHIEU>`** của **[Thủ tướng Chính phủ]`<CO_QUAN_THAM_QUYEN>`** về việc phê duyệt Đề án triển khai thực hiện Hiệp định hàng rào kỹ thuật trong thương mại ;

**Thực thể:**
- `[e0]` **Quyết định số 444/QĐ-TTg** → `THAM_CHIEU_PHAP_LY` (span: `[1:4]`)
- `[e1]` **Căn cứ** → `TU_KHOA_PHAP_LY` (span: `[0:1]`)
- `[e2]` **ngày 26 tháng 05 năm 2005** → `NGAY_THAM_CHIEU` (span: `[4:10]`)
- `[e3]` **Thủ tướng Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[11:13]`)

**Quan hệ:**
- (`e1` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e0` Quyết định số 444/QĐ-TTg `[THAM_CHIEU_PHAP_LY]`)
- (`e3` Thủ tướng Chính phủ `[CO_QUAN_THAM_QUYEN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e0` Quyết định số 444/QĐ-TTg `[THAM_CHIEU_PHAP_LY]`)
- (`e0` Quyết định số 444/QĐ-TTg `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e2` ngày 26 tháng 05 năm 2005 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #16_2006_QĐ-BKHCN_15269#body_context_9 (Loại: `body_context`)
> **[Bộ Khoa học và Công nghệ]`<CO_QUAN_BAN_HANH>`** ban hành **[Quyết định]`<LOAI_VAN_BAN>`** số **[16/2006/QĐ-BKHCN]`<SO_HIEU>`** . **[Điều 1 . Ban hành kèm theo Quyết định này " Quy định về việc tổ chức thực hiện các nhiệm vụ thuộc Đề án triển khai thực hiện Hiệp định hàng rào kỹ thuật trong thương mại giai đoạn 2006 - 2010 " .]`<DIEU>`**

**Thực thể:**
- `[e0]` **Quyết định** → `LOAI_VAN_BAN` (span: `[5:6]`)
- `[e1]` **16/2006/QĐ-BKHCN** → `SO_HIEU` (span: `[7:8]`)
- `[e2]` **Bộ Khoa học và Công nghệ** → `CO_QUAN_BAN_HANH` (span: `[0:4]`)
- `[e3]` **Điều 1 . Ban hành kèm theo Quyết định này " Quy định về việc tổ chức thực hiện các nhiệm vụ thuộc Đề án triển khai thực hiện Hiệp định hàng rào kỹ thuật trong thương mại giai đoạn 2006 - 2010 " .** → `DIEU` (span: `[9:40]`)

**Quan hệ:**
- (`e1` 16/2006/QĐ-BKHCN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Khoa học và Công nghệ `[CO_QUAN_BAN_HANH]`)
- (`e1` 16/2006/QĐ-BKHCN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Quyết định `[LOAI_VAN_BAN]`)
- (`e3` Điều 1 . Ban hành kèm theo Quyết định này " Quy định về việc tổ chức thực hiện các nhiệm vụ thuộc Đề án triển khai thực hiện Hiệp định hàng rào kỹ thuật trong thương mại giai đoạn 2006 - 2010 " . `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 16/2006/QĐ-BKHCN `[SO_HIEU]`)


---

### Mẫu #16_2006_QĐ-BKHCN_15269#body_context_10 (Loại: `body_context`)
> **[Quyết định]`<LOAI_VAN_BAN>`** số **[16/2006/QĐ-BKHCN]`<SO_HIEU>`** của **[Bộ Khoa học và Công nghệ]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Khoa học và công nghệ]`<LINH_VUC>`** . **[Điều 2 . Quyết định này có hiệu lực **[sau 15 ngày]`<THOI_HAN>`** , kể từ ngày đăng Công báo .]`<DIEU>`**

**Thực thể:**
- `[e0]` **Quyết định** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **16/2006/QĐ-BKHCN** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Khoa học và Công nghệ** → `CO_QUAN_BAN_HANH` (span: `[4:8]`)
- `[e3]` **Khoa học và công nghệ** → `LINH_VUC` (span: `[10:13]`)
- `[e4]` **Điều 2 . Quyết định này có hiệu lực sau 15 ngày , kể từ ngày đăng Công báo .** → `DIEU` (span: `[14:31]`)
- `[e5]` **sau 15 ngày** → `THOI_HAN` (span: `[21:24]`) *(lồng trong `e4` (`DIEU`))*

**Quan hệ:**
- (`e1` 16/2006/QĐ-BKHCN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Khoa học và Công nghệ `[CO_QUAN_BAN_HANH]`)
- (`e1` 16/2006/QĐ-BKHCN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Quyết định `[LOAI_VAN_BAN]`)
- (`e1` 16/2006/QĐ-BKHCN `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Khoa học và công nghệ `[LINH_VUC]`)
- (`e4` Điều 2 . Quyết định này có hiệu lực sau 15 ngày , kể từ ngày đăng Công báo . `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 16/2006/QĐ-BKHCN `[SO_HIEU]`)
- (`e1` 16/2006/QĐ-BKHCN `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Khoa học và công nghệ `[LINH_VUC]`)
- (`e4` Điều 2 . Quyết định này có hiệu lực sau 15 ngày , kể từ ngày đăng Công báo . `[DIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Khoa học và công nghệ `[LINH_VUC]`)


---

### Mẫu #16_2006_QĐ-BKHCN_15269#body_context_11 (Loại: `body_context`)
> **[Quyết định]`<LOAI_VAN_BAN>`** số **[16/2006/QĐ-BKHCN]`<SO_HIEU>`** của **[Bộ Khoa học và Công nghệ]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Khoa học và công nghệ]`<LINH_VUC>`** . **[Điều 3 . Chánh Văn phòng , Vụ trưởng Vụ Kế hoạch - Tài chính , Tổng cục trưởng Tổng cục Tiêu chuẩn Đo lường Chất lượng , Thủ trưởng các đơn vị thuộc Bộ và các cơ quan , tổ chức , cá nhân có liên quan chịu trách nhiệm thi hành Quyết định này .]`<DIEU>`**

**Thực thể:**
- `[e0]` **Quyết định** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **16/2006/QĐ-BKHCN** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Khoa học và Công nghệ** → `CO_QUAN_BAN_HANH` (span: `[4:8]`)
- `[e3]` **Khoa học và công nghệ** → `LINH_VUC` (span: `[10:13]`)
- `[e4]` **Điều 3 . Chánh Văn phòng , Vụ trưởng Vụ Kế hoạch - Tài chính , Tổng cục trưởng Tổng cục Tiêu chuẩn Đo lường Chất lượng , Thủ trưởng các đơn vị thuộc Bộ và các cơ quan , tổ chức , cá nhân có liên quan chịu trách nhiệm thi hành Quyết định này .** → `DIEU` (span: `[14:52]`)

**Quan hệ:**
- (`e1` 16/2006/QĐ-BKHCN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Khoa học và Công nghệ `[CO_QUAN_BAN_HANH]`)
- (`e1` 16/2006/QĐ-BKHCN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Quyết định `[LOAI_VAN_BAN]`)
- (`e1` 16/2006/QĐ-BKHCN `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Khoa học và công nghệ `[LINH_VUC]`)
- (`e4` Điều 3 . Chánh Văn phòng , Vụ trưởng Vụ Kế hoạch - Tài chính , Tổng cục trưởng Tổng cục Tiêu chuẩn Đo lường Chất lượng , Thủ trưởng các đơn vị thuộc Bộ và các cơ quan , tổ chức , cá nhân có liên quan chịu trách nhiệm thi hành Quyết định này . `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 16/2006/QĐ-BKHCN `[SO_HIEU]`)
- (`e1` 16/2006/QĐ-BKHCN `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Khoa học và công nghệ `[LINH_VUC]`)
- (`e4` Điều 3 . Chánh Văn phòng , Vụ trưởng Vụ Kế hoạch - Tài chính , Tổng cục trưởng Tổng cục Tiêu chuẩn Đo lường Chất lượng , Thủ trưởng các đơn vị thuộc Bộ và các cơ quan , tổ chức , cá nhân có liên quan chịu trách nhiệm thi hành Quyết định này . `[DIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Khoa học và công nghệ `[LINH_VUC]`)


---

### Mẫu #16_2006_QĐ-BKHCN_15269#hard_negative_12 (Loại: `hard_negative`)
> CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM


---
