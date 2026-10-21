# Dữ liệu gán nhãn văn bản: 08_2007_QĐ-BGTVT_14289
- **Thể loại**: `quyet_dinh`
- **Phân vùng dữ liệu**: `DEV`
- **Tổng số mẫu**: 39 mẫu
- **Tổng số thực thể**: 199
- **Tổng số quan hệ**: 152

---

### Mẫu #08_2007_QĐ-BGTVT_14289#header_0 (Loại: `header`)
> **[BỘ GIAO THÔNG VẬN TẢI]`<CO_QUAN_BAN_HANH>`** . CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM . Độc lập – Tự do – Hạnh phúc . Số : **[08/2007/QĐ-BGTVT]`<SO_HIEU>`** . **[Ngày 23 tháng 2 năm 2007]`<NGAY_BAN_HANH>`** . **[QUYẾT ĐỊNH]`<LOAI_VAN_BAN>`**

**Thực thể:**
- `[e0]` **08/2007/QĐ-BGTVT** → `SO_HIEU` (span: `[19:20]`)
- `[e1]` **Ngày 23 tháng 2 năm 2007** → `NGAY_BAN_HANH` (span: `[21:27]`)
- `[e2]` **BỘ GIAO THÔNG VẬN TẢI** → `CO_QUAN_BAN_HANH` (span: `[0:3]`)
- `[e3]` **QUYẾT ĐỊNH** → `LOAI_VAN_BAN` (span: `[28:29]`)

**Quan hệ:**
- (`e0` 08/2007/QĐ-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` BỘ GIAO THÔNG VẬN TẢI `[CO_QUAN_BAN_HANH]`)
- (`e0` 08/2007/QĐ-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e1` Ngày 23 tháng 2 năm 2007 `[NGAY_BAN_HANH]`)
- (`e0` 08/2007/QĐ-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e3` QUYẾT ĐỊNH `[LOAI_VAN_BAN]`)


---

### Mẫu #08_2007_QĐ-BGTVT_14289#signature_1 (Loại: `signature`)
> **[BỘ TRƯỞNG]`<CHUC_DANH_NGUOI_KY>`** . ( Đã ký ) . **[Hồ Nghĩa Dũng]`<NGUOI_KY>`**

**Thực thể:**
- `[e0]` **Hồ Nghĩa Dũng** → `NGUOI_KY` (span: `[7:8]`)
- `[e1]` **BỘ TRƯỞNG** → `CHUC_DANH_NGUOI_KY` (span: `[0:1]`)

**Quan hệ:**
- (`e0` Hồ Nghĩa Dũng `[NGUOI_KY]`) ==[ **GIU_CHUC_VU** ]==> (`e1` BỘ TRƯỞNG `[CHUC_DANH_NGUOI_KY]`)


---

### Mẫu #08_2007_QĐ-BGTVT_14289#meta_2 (Loại: `meta`)
> **[BỘ GIAO THÔNG VẬN TẢI]`<CO_QUAN_BAN_HANH>`** . CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM . Độc lập – Tự do – Hạnh phúc . Số : **[08/2007/QĐ-BGTVT]`<SO_HIEU>`** . Ngày 23 tháng 2 năm 2007 . **[QUYẾT ĐỊNH]`<LOAI_VAN_BAN>`** . **[BỘ TRƯỞNG]`<CHUC_DANH_NGUOI_KY>`** . ( Đã ký ) . **[Hồ Nghĩa Dũng]`<NGUOI_KY>`**

**Thực thể:**
- `[e0]` **08/2007/QĐ-BGTVT** → `SO_HIEU` (span: `[19:20]`)
- `[e1]` **BỘ GIAO THÔNG VẬN TẢI** → `CO_QUAN_BAN_HANH` (span: `[0:3]`)
- `[e2]` **QUYẾT ĐỊNH** → `LOAI_VAN_BAN` (span: `[28:29]`)
- `[e3]` **Hồ Nghĩa Dũng** → `NGUOI_KY` (span: `[37:38]`)
- `[e4]` **BỘ TRƯỞNG** → `CHUC_DANH_NGUOI_KY` (span: `[30:31]`)

**Quan hệ:**
- (`e0` 08/2007/QĐ-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e1` BỘ GIAO THÔNG VẬN TẢI `[CO_QUAN_BAN_HANH]`)
- (`e0` 08/2007/QĐ-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e2` QUYẾT ĐỊNH `[LOAI_VAN_BAN]`)
- (`e0` 08/2007/QĐ-BGTVT `[SO_HIEU]`) ==[ **KY_BOI** ]==> (`e3` Hồ Nghĩa Dũng `[NGUOI_KY]`)
- (`e3` Hồ Nghĩa Dũng `[NGUOI_KY]`) ==[ **GIU_CHUC_VU** ]==> (`e4` BỘ TRƯỞNG `[CHUC_DANH_NGUOI_KY]`)


---

### Mẫu #08_2007_QĐ-BGTVT_14289#preamble_context_3 (Loại: `preamble_context`)
> **[Quyết định]`<LOAI_VAN_BAN>`** số **[08/2007/QĐ-BGTVT]`<SO_HIEU>`** của **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** . và khu vực quản lý của **[Cảng vụ hàng hải]`<CO_QUAN_THAM_QUYEN>`** Quảng Trị

**Thực thể:**
- `[e0]` **Quyết định** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **08/2007/QĐ-BGTVT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[4:7]`)
- `[e3]` **Cảng vụ hàng hải** → `CO_QUAN_THAM_QUYEN` (span: `[12:14]`)

**Quan hệ:**
- (`e1` 08/2007/QĐ-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 08/2007/QĐ-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Quyết định `[LOAI_VAN_BAN]`)


---

### Mẫu #08_2007_QĐ-BGTVT_14289#preamble_standalone_4 (Loại: `preamble_standalone`)
> và khu vực quản lý của **[Cảng vụ hàng hải]`<CO_QUAN_THAM_QUYEN>`** Quảng Trị

**Thực thể:**
- `[e0]` **Cảng vụ hàng hải** → `CO_QUAN_THAM_QUYEN` (span: `[4:6]`)


---

### Mẫu #08_2007_QĐ-BGTVT_14289#preamble_context_5 (Loại: `preamble_context`)
> **[Quyết định]`<LOAI_VAN_BAN>`** số **[08/2007/QĐ-BGTVT]`<SO_HIEU>`** của **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** . **[Căn cứ]`<TU_KHOA_PHAP_LY>`** **[Bộ luật Hàng hải Việt Nam]`<THAM_CHIEU_PHAP_LY>`** **[ngày 14 tháng 6 năm 2005]`<NGAY_THAM_CHIEU>`** ;

**Thực thể:**
- `[e0]` **Quyết định** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **08/2007/QĐ-BGTVT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[4:7]`)
- `[e3]` **Bộ luật Hàng hải Việt Nam** → `THAM_CHIEU_PHAP_LY` (span: `[9:12]`)
- `[e4]` **Căn cứ** → `TU_KHOA_PHAP_LY` (span: `[8:9]`)
- `[e5]` **ngày 14 tháng 6 năm 2005** → `NGAY_THAM_CHIEU` (span: `[12:18]`)

**Quan hệ:**
- (`e1` 08/2007/QĐ-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 08/2007/QĐ-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Quyết định `[LOAI_VAN_BAN]`)
- (`e4` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Bộ luật Hàng hải Việt Nam `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 08/2007/QĐ-BGTVT `[SO_HIEU]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Bộ luật Hàng hải Việt Nam `[THAM_CHIEU_PHAP_LY]`)
- (`e3` Bộ luật Hàng hải Việt Nam `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e5` ngày 14 tháng 6 năm 2005 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #08_2007_QĐ-BGTVT_14289#preamble_standalone_6 (Loại: `preamble_standalone`)
> **[Căn cứ]`<TU_KHOA_PHAP_LY>`** **[Bộ luật Hàng hải Việt Nam]`<THAM_CHIEU_PHAP_LY>`** **[ngày 14 tháng 6 năm 2005]`<NGAY_THAM_CHIEU>`** ;

**Thực thể:**
- `[e0]` **Bộ luật Hàng hải Việt Nam** → `THAM_CHIEU_PHAP_LY` (span: `[1:4]`)
- `[e1]` **Căn cứ** → `TU_KHOA_PHAP_LY` (span: `[0:1]`)
- `[e2]` **ngày 14 tháng 6 năm 2005** → `NGAY_THAM_CHIEU` (span: `[4:10]`)

**Quan hệ:**
- (`e1` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e0` Bộ luật Hàng hải Việt Nam `[THAM_CHIEU_PHAP_LY]`)
- (`e0` Bộ luật Hàng hải Việt Nam `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e2` ngày 14 tháng 6 năm 2005 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #08_2007_QĐ-BGTVT_14289#preamble_context_7 (Loại: `preamble_context`)
> **[Quyết định]`<LOAI_VAN_BAN>`** số **[08/2007/QĐ-BGTVT]`<SO_HIEU>`** của **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** . **[Căn cứ]`<TU_KHOA_PHAP_LY>`** Nghị định số 34 / 2003 / NĐ - CP ngày 04 tháng 4 năm 2003 của **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** quy định chức năng , nhiệm vụ , quyền hạn và cơ cấu tổ chức của **[Bộ Giao thông vận tải]`<CO_QUAN_THAM_QUYEN>`** ;

**Thực thể:**
- `[e0]` **Quyết định** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **08/2007/QĐ-BGTVT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[4:7]`)
- `[e3]` **Căn cứ** → `TU_KHOA_PHAP_LY` (span: `[8:9]`)
- `[e4]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[25:26]`)
- `[e5]` **Bộ Giao thông vận tải** → `CO_QUAN_THAM_QUYEN` (span: `[36:39]`)

**Quan hệ:**
- (`e1` 08/2007/QĐ-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 08/2007/QĐ-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Quyết định `[LOAI_VAN_BAN]`)


---

### Mẫu #08_2007_QĐ-BGTVT_14289#preamble_standalone_8 (Loại: `preamble_standalone`)
> **[Căn cứ]`<TU_KHOA_PHAP_LY>`** Nghị định số 34 / 2003 / NĐ - CP ngày 04 tháng 4 năm 2003 của **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** quy định chức năng , nhiệm vụ , quyền hạn và cơ cấu tổ chức của **[Bộ Giao thông vận tải]`<CO_QUAN_THAM_QUYEN>`** ;

**Thực thể:**
- `[e0]` **Căn cứ** → `TU_KHOA_PHAP_LY` (span: `[0:1]`)
- `[e1]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[17:18]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_THAM_QUYEN` (span: `[28:31]`)


---

### Mẫu #08_2007_QĐ-BGTVT_14289#preamble_context_9 (Loại: `preamble_context`)
> **[Quyết định]`<LOAI_VAN_BAN>`** số **[08/2007/QĐ-BGTVT]`<SO_HIEU>`** của **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** . **[Căn cứ]`<TU_KHOA_PHAP_LY>`** Nghị định số 71 / 2006 / NĐ - CP ngày 25 tháng 7 năm 2006 của **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** về quản lý cảng biển và luồng hàng hải ;

**Thực thể:**
- `[e0]` **Quyết định** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **08/2007/QĐ-BGTVT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[4:7]`)
- `[e3]` **Căn cứ** → `TU_KHOA_PHAP_LY` (span: `[8:9]`)
- `[e4]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[25:26]`)

**Quan hệ:**
- (`e1` 08/2007/QĐ-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 08/2007/QĐ-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Quyết định `[LOAI_VAN_BAN]`)


---

### Mẫu #08_2007_QĐ-BGTVT_14289#preamble_standalone_10 (Loại: `preamble_standalone`)
> **[Căn cứ]`<TU_KHOA_PHAP_LY>`** Nghị định số 71 / 2006 / NĐ - CP ngày 25 tháng 7 năm 2006 của **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** về quản lý cảng biển và luồng hàng hải ;

**Thực thể:**
- `[e0]` **Căn cứ** → `TU_KHOA_PHAP_LY` (span: `[0:1]`)
- `[e1]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[17:18]`)


---

### Mẫu #08_2007_QĐ-BGTVT_14289#preamble_context_11 (Loại: `preamble_context`)
> **[Quyết định]`<LOAI_VAN_BAN>`** số **[08/2007/QĐ-BGTVT]`<SO_HIEU>`** của **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** . **[Căn cứ]`<TU_KHOA_PHAP_LY>`** ý kiến của Ủy ban nhân dân tỉnh Quảng Trị tại công văn số 2415 / UBND - CN ngày 11 tháng 10 năm 2006 ;

**Thực thể:**
- `[e0]` **Quyết định** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **08/2007/QĐ-BGTVT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[4:7]`)
- `[e3]` **Căn cứ** → `TU_KHOA_PHAP_LY` (span: `[8:9]`)

**Quan hệ:**
- (`e1` 08/2007/QĐ-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 08/2007/QĐ-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Quyết định `[LOAI_VAN_BAN]`)


---

### Mẫu #08_2007_QĐ-BGTVT_14289#preamble_standalone_12 (Loại: `preamble_standalone`)
> **[Căn cứ]`<TU_KHOA_PHAP_LY>`** ý kiến của Ủy ban nhân dân tỉnh Quảng Trị tại công văn số 2415 / UBND - CN ngày 11 tháng 10 năm 2006 ;

**Thực thể:**
- `[e0]` **Căn cứ** → `TU_KHOA_PHAP_LY` (span: `[0:1]`)


---

### Mẫu #08_2007_QĐ-BGTVT_14289#body_context_13 (Loại: `body_context`)
> **[Quyết định]`<LOAI_VAN_BAN>`** số **[08/2007/QĐ-BGTVT]`<SO_HIEU>`** ban hành **[ngày 23 tháng 02 năm 2007]`<NGAY_BAN_HANH>`** bởi **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** . **[Điều 1]`<DIEU>`** . **[1 . Nay công bố vùng nước cảng biển thuộc địa phận tỉnh Quảng Trị , bao gồm :]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Quyết định** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **08/2007/QĐ-BGTVT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[11:14]`)
- `[e3]` **ngày 23 tháng 02 năm 2007** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 1** → `DIEU` (span: `[15:17]`)
- `[e5]` **1 . Nay công bố vùng nước cảng biển thuộc địa phận tỉnh Quảng Trị , bao gồm :** → `KHOAN` (span: `[18:33]`)

**Quan hệ:**
- (`e1` 08/2007/QĐ-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 08/2007/QĐ-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Quyết định `[LOAI_VAN_BAN]`)
- (`e1` 08/2007/QĐ-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 23 tháng 02 năm 2007 `[NGAY_BAN_HANH]`)
- (`e4` Điều 1 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 08/2007/QĐ-BGTVT `[SO_HIEU]`)
- (`e5` 1 . Nay công bố vùng nước cảng biển thuộc địa phận tỉnh Quảng Trị , bao gồm : `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 1 `[DIEU]`)


---

### Mẫu #08_2007_QĐ-BGTVT_14289#body_context_14 (Loại: `body_context`)
> **[Quyết định]`<LOAI_VAN_BAN>`** số **[08/2007/QĐ-BGTVT]`<SO_HIEU>`** ban hành **[ngày 23 tháng 02 năm 2007]`<NGAY_BAN_HANH>`** bởi **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** . **[Điều 1]`<DIEU>`** . **[Khoản 1]`<KHOAN>`** . **[a ) Vùng nước trước cầu cảng của cảng biển Cửa Việt .]`<DIEM>`**

**Thực thể:**
- `[e0]` **Quyết định** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **08/2007/QĐ-BGTVT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[11:14]`)
- `[e3]` **ngày 23 tháng 02 năm 2007** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 1** → `DIEU` (span: `[15:17]`)
- `[e5]` **Khoản 1** → `KHOAN` (span: `[18:20]`)
- `[e6]` **a ) Vùng nước trước cầu cảng của cảng biển Cửa Việt .** → `DIEM` (span: `[21:33]`)

**Quan hệ:**
- (`e1` 08/2007/QĐ-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 08/2007/QĐ-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Quyết định `[LOAI_VAN_BAN]`)
- (`e1` 08/2007/QĐ-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 23 tháng 02 năm 2007 `[NGAY_BAN_HANH]`)
- (`e4` Điều 1 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 08/2007/QĐ-BGTVT `[SO_HIEU]`)
- (`e5` Khoản 1 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 1 `[DIEU]`)
- (`e6` a ) Vùng nước trước cầu cảng của cảng biển Cửa Việt . `[DIEM]`) ==[ **THUOC_VE** ]==> (`e5` Khoản 1 `[KHOAN]`)


---

### Mẫu #08_2007_QĐ-BGTVT_14289#body_standalone_15 (Loại: `body_standalone`)
> **[Điều 1]`<DIEU>`** . **[Khoản 1]`<KHOAN>`** . **[a ) Vùng nước trước cầu cảng của cảng biển Cửa Việt .]`<DIEM>`**

**Thực thể:**
- `[e0]` **Điều 1** → `DIEU` (span: `[0:2]`)
- `[e1]` **Khoản 1** → `KHOAN` (span: `[3:5]`)
- `[e2]` **a ) Vùng nước trước cầu cảng của cảng biển Cửa Việt .** → `DIEM` (span: `[6:18]`)

**Quan hệ:**
- (`e1` Khoản 1 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 1 `[DIEU]`)
- (`e2` a ) Vùng nước trước cầu cảng của cảng biển Cửa Việt . `[DIEM]`) ==[ **THUOC_VE** ]==> (`e1` Khoản 1 `[KHOAN]`)


---

### Mẫu #08_2007_QĐ-BGTVT_14289#body_context_16 (Loại: `body_context`)
> **[Quyết định]`<LOAI_VAN_BAN>`** số **[08/2007/QĐ-BGTVT]`<SO_HIEU>`** ban hành **[ngày 23 tháng 02 năm 2007]`<NGAY_BAN_HANH>`** bởi **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** . **[Điều 1]`<DIEU>`** . **[Khoản 1]`<KHOAN>`** . **[b ) Vùng nước của luồng cảng biển , luồng nhánh cảng biển , vùng đón trả hoa tiêu , vùng kiểm dịch , khu neo đậu , khu chuyển tải , khu tránh bão thuộc cảng biển **[quy định tại]`<TU_KHOA_PHAP_LY>`** **[điểm a]`<THAM_CHIEU_PHAP_LY>`** khoản này .]`<DIEM>`**

**Thực thể:**
- `[e0]` **Quyết định** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **08/2007/QĐ-BGTVT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[11:14]`)
- `[e3]` **ngày 23 tháng 02 năm 2007** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 1** → `DIEU` (span: `[15:17]`)
- `[e5]` **Khoản 1** → `KHOAN` (span: `[18:20]`)
- `[e6]` **b ) Vùng nước của luồng cảng biển , luồng nhánh cảng biển , vùng đón trả hoa tiêu , vùng kiểm dịch , khu neo đậu , khu chuyển tải , khu tránh bão thuộc cảng biển quy định tại điểm a khoản này .** → `DIEM` (span: `[21:63]`)
- `[e7]` **điểm a** → `THAM_CHIEU_PHAP_LY` (span: `[58:60]`) *(lồng trong `e6` (`DIEM`))*
- `[e8]` **quy định tại** → `TU_KHOA_PHAP_LY` (span: `[56:58]`) *(lồng trong `e6` (`DIEM`))*

**Quan hệ:**
- (`e1` 08/2007/QĐ-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 08/2007/QĐ-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Quyết định `[LOAI_VAN_BAN]`)
- (`e1` 08/2007/QĐ-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 23 tháng 02 năm 2007 `[NGAY_BAN_HANH]`)
- (`e4` Điều 1 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 08/2007/QĐ-BGTVT `[SO_HIEU]`)
- (`e5` Khoản 1 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 1 `[DIEU]`)
- (`e6` b ) Vùng nước của luồng cảng biển , luồng nhánh cảng biển , vùng đón trả hoa tiêu , vùng kiểm dịch , khu neo đậu , khu chuyển tải , khu tránh bão thuộc cảng biển quy định tại điểm a khoản này . `[DIEM]`) ==[ **THUOC_VE** ]==> (`e5` Khoản 1 `[KHOAN]`)
- (`e8` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e7` điểm a `[THAM_CHIEU_PHAP_LY]`)
- (`e6` b ) Vùng nước của luồng cảng biển , luồng nhánh cảng biển , vùng đón trả hoa tiêu , vùng kiểm dịch , khu neo đậu , khu chuyển tải , khu tránh bão thuộc cảng biển quy định tại điểm a khoản này . `[DIEM]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e7` điểm a `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #08_2007_QĐ-BGTVT_14289#body_standalone_17 (Loại: `body_standalone`)
> **[Điều 1]`<DIEU>`** . **[Khoản 1]`<KHOAN>`** . **[b ) Vùng nước của luồng cảng biển , luồng nhánh cảng biển , vùng đón trả hoa tiêu , vùng kiểm dịch , khu neo đậu , khu chuyển tải , khu tránh bão thuộc cảng biển **[quy định tại]`<TU_KHOA_PHAP_LY>`** **[điểm a]`<THAM_CHIEU_PHAP_LY>`** khoản này .]`<DIEM>`**

**Thực thể:**
- `[e0]` **Điều 1** → `DIEU` (span: `[0:2]`)
- `[e1]` **Khoản 1** → `KHOAN` (span: `[3:5]`)
- `[e2]` **b ) Vùng nước của luồng cảng biển , luồng nhánh cảng biển , vùng đón trả hoa tiêu , vùng kiểm dịch , khu neo đậu , khu chuyển tải , khu tránh bão thuộc cảng biển quy định tại điểm a khoản này .** → `DIEM` (span: `[6:48]`)
- `[e3]` **điểm a** → `THAM_CHIEU_PHAP_LY` (span: `[43:45]`) *(lồng trong `e2` (`DIEM`))*
- `[e4]` **quy định tại** → `TU_KHOA_PHAP_LY` (span: `[41:43]`) *(lồng trong `e2` (`DIEM`))*

**Quan hệ:**
- (`e1` Khoản 1 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 1 `[DIEU]`)
- (`e2` b ) Vùng nước của luồng cảng biển , luồng nhánh cảng biển , vùng đón trả hoa tiêu , vùng kiểm dịch , khu neo đậu , khu chuyển tải , khu tránh bão thuộc cảng biển quy định tại điểm a khoản này . `[DIEM]`) ==[ **THUOC_VE** ]==> (`e1` Khoản 1 `[KHOAN]`)
- (`e4` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` điểm a `[THAM_CHIEU_PHAP_LY]`)
- (`e2` b ) Vùng nước của luồng cảng biển , luồng nhánh cảng biển , vùng đón trả hoa tiêu , vùng kiểm dịch , khu neo đậu , khu chuyển tải , khu tránh bão thuộc cảng biển quy định tại điểm a khoản này . `[DIEM]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` điểm a `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #08_2007_QĐ-BGTVT_14289#body_context_18 (Loại: `body_context`)
> **[Quyết định]`<LOAI_VAN_BAN>`** số **[08/2007/QĐ-BGTVT]`<SO_HIEU>`** của **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Hàng hải]`<LINH_VUC>`** . **[Điều 1]`<DIEU>`** . **[2 . Vùng nước trước cầu cảng , bến cảng , khu neo đậu , khu chuyển tải , khu tránh bão khác được công bố theo quy định của pháp luật .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Quyết định** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **08/2007/QĐ-BGTVT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[4:7]`)
- `[e3]` **Hàng hải** → `LINH_VUC` (span: `[9:10]`)
- `[e4]` **Điều 1** → `DIEU` (span: `[11:13]`)
- `[e5]` **2 . Vùng nước trước cầu cảng , bến cảng , khu neo đậu , khu chuyển tải , khu tránh bão khác được công bố theo quy định của pháp luật .** → `KHOAN` (span: `[14:42]`)

**Quan hệ:**
- (`e1` 08/2007/QĐ-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 08/2007/QĐ-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Quyết định `[LOAI_VAN_BAN]`)
- (`e1` 08/2007/QĐ-BGTVT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Hàng hải `[LINH_VUC]`)
- (`e4` Điều 1 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 08/2007/QĐ-BGTVT `[SO_HIEU]`)
- (`e5` 2 . Vùng nước trước cầu cảng , bến cảng , khu neo đậu , khu chuyển tải , khu tránh bão khác được công bố theo quy định của pháp luật . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 1 `[DIEU]`)
- (`e1` 08/2007/QĐ-BGTVT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Hàng hải `[LINH_VUC]`)
- (`e5` 2 . Vùng nước trước cầu cảng , bến cảng , khu neo đậu , khu chuyển tải , khu tránh bão khác được công bố theo quy định của pháp luật . `[KHOAN]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Hàng hải `[LINH_VUC]`)


---

### Mẫu #08_2007_QĐ-BGTVT_14289#body_context_19 (Loại: `body_context`)
> **[Quyết định]`<LOAI_VAN_BAN>`** số **[08/2007/QĐ-BGTVT]`<SO_HIEU>`** ban hành **[ngày 23 tháng 02 năm 2007]`<NGAY_BAN_HANH>`** bởi **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** . **[Điều 2 . Phạm vi vùng nước cảng biển thuộc địa phận tỉnh Quảng Trị tính theo mực nước thủy triều lớn nhất , được quy định cụ thể như sau :]`<DIEU>`**

**Thực thể:**
- `[e0]` **Quyết định** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **08/2007/QĐ-BGTVT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[11:14]`)
- `[e3]` **ngày 23 tháng 02 năm 2007** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 2 . Phạm vi vùng nước cảng biển thuộc địa phận tỉnh Quảng Trị tính theo mực nước thủy triều lớn nhất , được quy định cụ thể như sau :** → `DIEU` (span: `[15:41]`)

**Quan hệ:**
- (`e1` 08/2007/QĐ-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 08/2007/QĐ-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Quyết định `[LOAI_VAN_BAN]`)
- (`e1` 08/2007/QĐ-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 23 tháng 02 năm 2007 `[NGAY_BAN_HANH]`)
- (`e4` Điều 2 . Phạm vi vùng nước cảng biển thuộc địa phận tỉnh Quảng Trị tính theo mực nước thủy triều lớn nhất , được quy định cụ thể như sau : `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 08/2007/QĐ-BGTVT `[SO_HIEU]`)


---

### Mẫu #08_2007_QĐ-BGTVT_14289#body_context_20 (Loại: `body_context`)
> **[Quyết định]`<LOAI_VAN_BAN>`** số **[08/2007/QĐ-BGTVT]`<SO_HIEU>`** ban hành **[ngày 23 tháng 02 năm 2007]`<NGAY_BAN_HANH>`** bởi **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** . **[Điều 2]`<DIEU>`** . **[1 . Ranh giới về phía biển : được giới hạn bởi các đoạn thẳng nối các điểm CV1 , CV2 , CV3 , CV4 , CV5 có tọa độ sau đây : CV1 : 16 0 54 ’ 30 ” N , 107 0 11 ’ 06 ” E ;]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Quyết định** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **08/2007/QĐ-BGTVT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[11:14]`)
- `[e3]` **ngày 23 tháng 02 năm 2007** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 2** → `DIEU` (span: `[15:17]`)
- `[e5]` **1 . Ranh giới về phía biển : được giới hạn bởi các đoạn thẳng nối các điểm CV1 , CV2 , CV3 , CV4 , CV5 có tọa độ sau đây : CV1 : 16 0 54 ’ 30 ” N , 107 0 11 ’ 06 ” E ;** → `KHOAN` (span: `[18:65]`)

**Quan hệ:**
- (`e1` 08/2007/QĐ-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 08/2007/QĐ-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Quyết định `[LOAI_VAN_BAN]`)
- (`e1` 08/2007/QĐ-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 23 tháng 02 năm 2007 `[NGAY_BAN_HANH]`)
- (`e4` Điều 2 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 08/2007/QĐ-BGTVT `[SO_HIEU]`)
- (`e5` 1 . Ranh giới về phía biển : được giới hạn bởi các đoạn thẳng nối các điểm CV1 , CV2 , CV3 , CV4 , CV5 có tọa độ sau đây : CV1 : 16 0 54 ’ 30 ” N , 107 0 11 ’ 06 ” E ; `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 2 `[DIEU]`)


---

### Mẫu #08_2007_QĐ-BGTVT_14289#body_context_21 (Loại: `body_context`)
> **[Quyết định]`<LOAI_VAN_BAN>`** số **[08/2007/QĐ-BGTVT]`<SO_HIEU>`** ban hành **[ngày 23 tháng 02 năm 2007]`<NGAY_BAN_HANH>`** bởi **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** . **[Điều 2]`<DIEU>`** . **[1 . Ranh giới về phía biển : được giới hạn bởi các đoạn thẳng nối các điểm CV1 , CV2 , CV3 , CV4 , CV5 có tọa độ sau đây : CV2 : 16 0 55 ’ 30 ” N , 107 0 11 ’ 06 ” E ,]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Quyết định** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **08/2007/QĐ-BGTVT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[11:14]`)
- `[e3]` **ngày 23 tháng 02 năm 2007** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 2** → `DIEU` (span: `[15:17]`)
- `[e5]` **1 . Ranh giới về phía biển : được giới hạn bởi các đoạn thẳng nối các điểm CV1 , CV2 , CV3 , CV4 , CV5 có tọa độ sau đây : CV2 : 16 0 55 ’ 30 ” N , 107 0 11 ’ 06 ” E ,** → `KHOAN` (span: `[18:65]`)

**Quan hệ:**
- (`e1` 08/2007/QĐ-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 08/2007/QĐ-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Quyết định `[LOAI_VAN_BAN]`)
- (`e1` 08/2007/QĐ-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 23 tháng 02 năm 2007 `[NGAY_BAN_HANH]`)
- (`e4` Điều 2 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 08/2007/QĐ-BGTVT `[SO_HIEU]`)
- (`e5` 1 . Ranh giới về phía biển : được giới hạn bởi các đoạn thẳng nối các điểm CV1 , CV2 , CV3 , CV4 , CV5 có tọa độ sau đây : CV2 : 16 0 55 ’ 30 ” N , 107 0 11 ’ 06 ” E , `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 2 `[DIEU]`)


---

### Mẫu #08_2007_QĐ-BGTVT_14289#body_context_22 (Loại: `body_context`)
> **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** ban hành **[Quyết định]`<LOAI_VAN_BAN>`** số **[08/2007/QĐ-BGTVT]`<SO_HIEU>`** . **[Điều 2]`<DIEU>`** . **[1 . Ranh giới về phía biển : được giới hạn bởi các đoạn thẳng nối các điểm CV1 , CV2 , CV3 , CV4 , CV5 có tọa độ sau đây : CV3 : 16 0 55 ’ 30 ” N , 107 0 13 ’ 30 ” E ;]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Quyết định** → `LOAI_VAN_BAN` (span: `[4:5]`)
- `[e1]` **08/2007/QĐ-BGTVT** → `SO_HIEU` (span: `[6:7]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[0:3]`)
- `[e3]` **Điều 2** → `DIEU` (span: `[8:10]`)
- `[e4]` **1 . Ranh giới về phía biển : được giới hạn bởi các đoạn thẳng nối các điểm CV1 , CV2 , CV3 , CV4 , CV5 có tọa độ sau đây : CV3 : 16 0 55 ’ 30 ” N , 107 0 13 ’ 30 ” E ;** → `KHOAN` (span: `[11:58]`)

**Quan hệ:**
- (`e1` 08/2007/QĐ-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 08/2007/QĐ-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Quyết định `[LOAI_VAN_BAN]`)
- (`e3` Điều 2 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 08/2007/QĐ-BGTVT `[SO_HIEU]`)
- (`e4` 1 . Ranh giới về phía biển : được giới hạn bởi các đoạn thẳng nối các điểm CV1 , CV2 , CV3 , CV4 , CV5 có tọa độ sau đây : CV3 : 16 0 55 ’ 30 ” N , 107 0 13 ’ 30 ” E ; `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 2 `[DIEU]`)


---

### Mẫu #08_2007_QĐ-BGTVT_14289#body_context_23 (Loại: `body_context`)
> **[Quyết định]`<LOAI_VAN_BAN>`** số **[08/2007/QĐ-BGTVT]`<SO_HIEU>`** của **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Hàng hải]`<LINH_VUC>`** . **[Điều 2]`<DIEU>`** . **[1 . Ranh giới về phía biển : được giới hạn bởi các đoạn thẳng nối các điểm CV1 , CV2 , CV3 , CV4 , CV5 có tọa độ sau đây : CV4 : 16 0 53 ’ 54 ” N , 107 0 13 ’ 30 ” E ;]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Quyết định** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **08/2007/QĐ-BGTVT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[4:7]`)
- `[e3]` **Hàng hải** → `LINH_VUC` (span: `[9:10]`)
- `[e4]` **Điều 2** → `DIEU` (span: `[11:13]`)
- `[e5]` **1 . Ranh giới về phía biển : được giới hạn bởi các đoạn thẳng nối các điểm CV1 , CV2 , CV3 , CV4 , CV5 có tọa độ sau đây : CV4 : 16 0 53 ’ 54 ” N , 107 0 13 ’ 30 ” E ;** → `KHOAN` (span: `[14:61]`)

**Quan hệ:**
- (`e1` 08/2007/QĐ-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 08/2007/QĐ-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Quyết định `[LOAI_VAN_BAN]`)
- (`e1` 08/2007/QĐ-BGTVT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Hàng hải `[LINH_VUC]`)
- (`e4` Điều 2 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 08/2007/QĐ-BGTVT `[SO_HIEU]`)
- (`e5` 1 . Ranh giới về phía biển : được giới hạn bởi các đoạn thẳng nối các điểm CV1 , CV2 , CV3 , CV4 , CV5 có tọa độ sau đây : CV4 : 16 0 53 ’ 54 ” N , 107 0 13 ’ 30 ” E ; `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 2 `[DIEU]`)
- (`e1` 08/2007/QĐ-BGTVT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Hàng hải `[LINH_VUC]`)
- (`e5` 1 . Ranh giới về phía biển : được giới hạn bởi các đoạn thẳng nối các điểm CV1 , CV2 , CV3 , CV4 , CV5 có tọa độ sau đây : CV4 : 16 0 53 ’ 54 ” N , 107 0 13 ’ 30 ” E ; `[KHOAN]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Hàng hải `[LINH_VUC]`)


---

### Mẫu #08_2007_QĐ-BGTVT_14289#body_context_24 (Loại: `body_context`)
> **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** ban hành **[Quyết định]`<LOAI_VAN_BAN>`** số **[08/2007/QĐ-BGTVT]`<SO_HIEU>`** . **[Điều 2]`<DIEU>`** . **[1 . Ranh giới về phía biển : được giới hạn bởi các đoạn thẳng nối các điểm CV1 , CV2 , CV3 , CV4 , CV5 có tọa độ sau đây : CV5 : 16 0 53 ’ 54 ” N , 107 0 11 ’ 54 ” E.]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Quyết định** → `LOAI_VAN_BAN` (span: `[4:5]`)
- `[e1]` **08/2007/QĐ-BGTVT** → `SO_HIEU` (span: `[6:7]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[0:3]`)
- `[e3]` **Điều 2** → `DIEU` (span: `[8:10]`)
- `[e4]` **1 . Ranh giới về phía biển : được giới hạn bởi các đoạn thẳng nối các điểm CV1 , CV2 , CV3 , CV4 , CV5 có tọa độ sau đây : CV5 : 16 0 53 ’ 54 ” N , 107 0 11 ’ 54 ” E.** → `KHOAN` (span: `[11:57]`)

**Quan hệ:**
- (`e1` 08/2007/QĐ-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 08/2007/QĐ-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Quyết định `[LOAI_VAN_BAN]`)
- (`e3` Điều 2 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 08/2007/QĐ-BGTVT `[SO_HIEU]`)
- (`e4` 1 . Ranh giới về phía biển : được giới hạn bởi các đoạn thẳng nối các điểm CV1 , CV2 , CV3 , CV4 , CV5 có tọa độ sau đây : CV5 : 16 0 53 ’ 54 ” N , 107 0 11 ’ 54 ” E. `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 2 `[DIEU]`)


---

### Mẫu #08_2007_QĐ-BGTVT_14289#body_context_25 (Loại: `body_context`)
> **[Quyết định]`<LOAI_VAN_BAN>`** số **[08/2007/QĐ-BGTVT]`<SO_HIEU>`** của **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Hàng hải]`<LINH_VUC>`** . **[Điều 2]`<DIEU>`** . **[2 . Ranh giới trên sông Thạch Hãn : là vùng nước được giới hạn từ điểm CV1 và CV5 chạy dọc theo mép hai bờ sông Thạch Hãn đến đường thẳng cắt ngang sông cách cầu Cửa Việt về phía hạ lưu 150m .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Quyết định** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **08/2007/QĐ-BGTVT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[4:7]`)
- `[e3]` **Hàng hải** → `LINH_VUC` (span: `[9:10]`)
- `[e4]` **Điều 2** → `DIEU` (span: `[11:13]`)
- `[e5]` **2 . Ranh giới trên sông Thạch Hãn : là vùng nước được giới hạn từ điểm CV1 và CV5 chạy dọc theo mép hai bờ sông Thạch Hãn đến đường thẳng cắt ngang sông cách cầu Cửa Việt về phía hạ lưu 150m .** → `KHOAN` (span: `[14:53]`)

**Quan hệ:**
- (`e1` 08/2007/QĐ-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 08/2007/QĐ-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Quyết định `[LOAI_VAN_BAN]`)
- (`e1` 08/2007/QĐ-BGTVT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Hàng hải `[LINH_VUC]`)
- (`e4` Điều 2 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 08/2007/QĐ-BGTVT `[SO_HIEU]`)
- (`e5` 2 . Ranh giới trên sông Thạch Hãn : là vùng nước được giới hạn từ điểm CV1 và CV5 chạy dọc theo mép hai bờ sông Thạch Hãn đến đường thẳng cắt ngang sông cách cầu Cửa Việt về phía hạ lưu 150m . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 2 `[DIEU]`)
- (`e1` 08/2007/QĐ-BGTVT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Hàng hải `[LINH_VUC]`)
- (`e5` 2 . Ranh giới trên sông Thạch Hãn : là vùng nước được giới hạn từ điểm CV1 và CV5 chạy dọc theo mép hai bờ sông Thạch Hãn đến đường thẳng cắt ngang sông cách cầu Cửa Việt về phía hạ lưu 150m . `[KHOAN]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Hàng hải `[LINH_VUC]`)


---

### Mẫu #08_2007_QĐ-BGTVT_14289#body_context_26 (Loại: `body_context`)
> **[Quyết định]`<LOAI_VAN_BAN>`** số **[08/2007/QĐ-BGTVT]`<SO_HIEU>`** của **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Hàng hải]`<LINH_VUC>`** . **[Điều 3 . Vùng đón trả hoa tiêu , vùng kiểm dịch , khu neo đậu , khu chuyển tải , khu tránh bão cho tàu thuyền vào cảng biển Cửa Việt thuộc địa phận tỉnh Quảng Trị , được quy định như sau :]`<DIEU>`**

**Thực thể:**
- `[e0]` **Quyết định** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **08/2007/QĐ-BGTVT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[4:7]`)
- `[e3]` **Hàng hải** → `LINH_VUC` (span: `[9:10]`)
- `[e4]` **Điều 3 . Vùng đón trả hoa tiêu , vùng kiểm dịch , khu neo đậu , khu chuyển tải , khu tránh bão cho tàu thuyền vào cảng biển Cửa Việt thuộc địa phận tỉnh Quảng Trị , được quy định như sau :** → `DIEU` (span: `[11:49]`)

**Quan hệ:**
- (`e1` 08/2007/QĐ-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 08/2007/QĐ-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Quyết định `[LOAI_VAN_BAN]`)
- (`e1` 08/2007/QĐ-BGTVT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Hàng hải `[LINH_VUC]`)
- (`e4` Điều 3 . Vùng đón trả hoa tiêu , vùng kiểm dịch , khu neo đậu , khu chuyển tải , khu tránh bão cho tàu thuyền vào cảng biển Cửa Việt thuộc địa phận tỉnh Quảng Trị , được quy định như sau : `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 08/2007/QĐ-BGTVT `[SO_HIEU]`)
- (`e1` 08/2007/QĐ-BGTVT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Hàng hải `[LINH_VUC]`)
- (`e4` Điều 3 . Vùng đón trả hoa tiêu , vùng kiểm dịch , khu neo đậu , khu chuyển tải , khu tránh bão cho tàu thuyền vào cảng biển Cửa Việt thuộc địa phận tỉnh Quảng Trị , được quy định như sau : `[DIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Hàng hải `[LINH_VUC]`)


---

### Mẫu #08_2007_QĐ-BGTVT_14289#body_context_27 (Loại: `body_context`)
> **[Quyết định]`<LOAI_VAN_BAN>`** số **[08/2007/QĐ-BGTVT]`<SO_HIEU>`** ban hành **[ngày 23 tháng 02 năm 2007]`<NGAY_BAN_HANH>`** bởi **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** . **[Điều 3]`<DIEU>`** . **[1 . Vùng đón trả hoa tiêu và vùng kiểm dịch : là vùng nước được giới hạn bởi đường tròn bán kính 0,5 hải lý , với tâm có vị trí tại tọa độ : 16 0 54 ’ 54 ” N ; 107 0 13 ’ 00 ” E.]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Quyết định** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **08/2007/QĐ-BGTVT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[11:14]`)
- `[e3]` **ngày 23 tháng 02 năm 2007** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 3** → `DIEU` (span: `[15:17]`)
- `[e5]` **1 . Vùng đón trả hoa tiêu và vùng kiểm dịch : là vùng nước được giới hạn bởi đường tròn bán kính 0,5 hải lý , với tâm có vị trí tại tọa độ : 16 0 54 ’ 54 ” N ; 107 0 13 ’ 00 ” E.** → `KHOAN` (span: `[18:61]`)

**Quan hệ:**
- (`e1` 08/2007/QĐ-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 08/2007/QĐ-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Quyết định `[LOAI_VAN_BAN]`)
- (`e1` 08/2007/QĐ-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 23 tháng 02 năm 2007 `[NGAY_BAN_HANH]`)
- (`e4` Điều 3 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 08/2007/QĐ-BGTVT `[SO_HIEU]`)
- (`e5` 1 . Vùng đón trả hoa tiêu và vùng kiểm dịch : là vùng nước được giới hạn bởi đường tròn bán kính 0,5 hải lý , với tâm có vị trí tại tọa độ : 16 0 54 ’ 54 ” N ; 107 0 13 ’ 00 ” E. `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 3 `[DIEU]`)


---

### Mẫu #08_2007_QĐ-BGTVT_14289#body_context_28 (Loại: `body_context`)
> **[Quyết định]`<LOAI_VAN_BAN>`** số **[08/2007/QĐ-BGTVT]`<SO_HIEU>`** của **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Hàng hải]`<LINH_VUC>`** . **[Điều 3]`<DIEU>`** . **[2 . Khu neo đậu : tại vùng nước đối diện vùng nước trước cầu cảng Cửa Việt .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Quyết định** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **08/2007/QĐ-BGTVT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[4:7]`)
- `[e3]` **Hàng hải** → `LINH_VUC` (span: `[9:10]`)
- `[e4]` **Điều 3** → `DIEU` (span: `[11:13]`)
- `[e5]` **2 . Khu neo đậu : tại vùng nước đối diện vùng nước trước cầu cảng Cửa Việt .** → `KHOAN` (span: `[14:30]`)

**Quan hệ:**
- (`e1` 08/2007/QĐ-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 08/2007/QĐ-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Quyết định `[LOAI_VAN_BAN]`)
- (`e1` 08/2007/QĐ-BGTVT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Hàng hải `[LINH_VUC]`)
- (`e4` Điều 3 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 08/2007/QĐ-BGTVT `[SO_HIEU]`)
- (`e5` 2 . Khu neo đậu : tại vùng nước đối diện vùng nước trước cầu cảng Cửa Việt . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 3 `[DIEU]`)
- (`e1` 08/2007/QĐ-BGTVT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Hàng hải `[LINH_VUC]`)
- (`e5` 2 . Khu neo đậu : tại vùng nước đối diện vùng nước trước cầu cảng Cửa Việt . `[KHOAN]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Hàng hải `[LINH_VUC]`)


---

### Mẫu #08_2007_QĐ-BGTVT_14289#body_context_29 (Loại: `body_context`)
> **[Quyết định]`<LOAI_VAN_BAN>`** số **[08/2007/QĐ-BGTVT]`<SO_HIEU>`** của **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Hàng hải]`<LINH_VUC>`** . **[Điều 4 . **[Cảng vụ hàng hải]`<CO_QUAN_THAM_QUYEN>`** Quảng Trị có trách nhiệm :]`<DIEU>`**

**Thực thể:**
- `[e0]` **Quyết định** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **08/2007/QĐ-BGTVT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[4:7]`)
- `[e3]` **Hàng hải** → `LINH_VUC` (span: `[9:10]`)
- `[e4]` **Điều 4 . Cảng vụ hàng hải Quảng Trị có trách nhiệm :** → `DIEU` (span: `[11:20]`)
- `[e5]` **Cảng vụ hàng hải** → `CO_QUAN_THAM_QUYEN` (span: `[14:16]`) *(lồng trong `e4` (`DIEU`))*

**Quan hệ:**
- (`e1` 08/2007/QĐ-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 08/2007/QĐ-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Quyết định `[LOAI_VAN_BAN]`)
- (`e1` 08/2007/QĐ-BGTVT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Hàng hải `[LINH_VUC]`)
- (`e4` Điều 4 . Cảng vụ hàng hải Quảng Trị có trách nhiệm : `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 08/2007/QĐ-BGTVT `[SO_HIEU]`)
- (`e1` 08/2007/QĐ-BGTVT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Hàng hải `[LINH_VUC]`)
- (`e4` Điều 4 . Cảng vụ hàng hải Quảng Trị có trách nhiệm : `[DIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Hàng hải `[LINH_VUC]`)


---

### Mẫu #08_2007_QĐ-BGTVT_14289#body_context_30 (Loại: `body_context`)
> **[Quyết định]`<LOAI_VAN_BAN>`** số **[08/2007/QĐ-BGTVT]`<SO_HIEU>`** của **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Hàng hải]`<LINH_VUC>`** . **[Điều 4]`<DIEU>`** . **[1 . Thực hiện nhiệm vụ và quyền hạn của mình theo quy định của Bộ luật Hàng hải Việt Nam và pháp luật có liên quan đối với hoạt động hàng hải tại vùng nước các cảng biển thuộc địa phận tỉnh Quảng Trị .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Quyết định** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **08/2007/QĐ-BGTVT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[4:7]`)
- `[e3]` **Hàng hải** → `LINH_VUC` (span: `[9:10]`)
- `[e4]` **Điều 4** → `DIEU` (span: `[11:13]`)
- `[e5]` **1 . Thực hiện nhiệm vụ và quyền hạn của mình theo quy định của Bộ luật Hàng hải Việt Nam và pháp luật có liên quan đối với hoạt động hàng hải tại vùng nước các cảng biển thuộc địa phận tỉnh Quảng Trị .** → `KHOAN` (span: `[14:46]`)

**Quan hệ:**
- (`e1` 08/2007/QĐ-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 08/2007/QĐ-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Quyết định `[LOAI_VAN_BAN]`)
- (`e1` 08/2007/QĐ-BGTVT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Hàng hải `[LINH_VUC]`)
- (`e4` Điều 4 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 08/2007/QĐ-BGTVT `[SO_HIEU]`)
- (`e5` 1 . Thực hiện nhiệm vụ và quyền hạn của mình theo quy định của Bộ luật Hàng hải Việt Nam và pháp luật có liên quan đối với hoạt động hàng hải tại vùng nước các cảng biển thuộc địa phận tỉnh Quảng Trị . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 4 `[DIEU]`)
- (`e1` 08/2007/QĐ-BGTVT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Hàng hải `[LINH_VUC]`)
- (`e5` 1 . Thực hiện nhiệm vụ và quyền hạn của mình theo quy định của Bộ luật Hàng hải Việt Nam và pháp luật có liên quan đối với hoạt động hàng hải tại vùng nước các cảng biển thuộc địa phận tỉnh Quảng Trị . `[KHOAN]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Hàng hải `[LINH_VUC]`)


---

### Mẫu #08_2007_QĐ-BGTVT_14289#body_context_31 (Loại: `body_context`)
> **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** ban hành **[Quyết định]`<LOAI_VAN_BAN>`** số **[08/2007/QĐ-BGTVT]`<SO_HIEU>`** . **[Điều 4]`<DIEU>`** . **[2 . Căn cứ vào tình hình thực tế về thời tiết , sóng gió , mớn nước và trọng tải của tàu thuyền , chỉ định vị trí cụ thể cho tàu thuyền đón trả hoa tiêu , kiểm dịch vµ neo đậu trong vùng nước **[quy định tại]`<TU_KHOA_PHAP_LY>`** **[Điều 3 của Quyết định này]`<THAM_CHIEU_PHAP_LY>`** ; trường hợp có bão , nếu cần thiết , **[Cảng vụ hàng hải]`<CO_QUAN_THAM_QUYEN>`** Quảng Trị điều động tàu thuyền sang khu vực phù hợp , bảo đảm an toàn hàng hải , an ninh hàng hải và phòng ngừa ô nhiễm môi trường .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Quyết định** → `LOAI_VAN_BAN` (span: `[4:5]`)
- `[e1]` **08/2007/QĐ-BGTVT** → `SO_HIEU` (span: `[6:7]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[0:3]`)
- `[e3]` **Điều 4** → `DIEU` (span: `[8:10]`)
- `[e4]` **2 . Căn cứ vào tình hình thực tế về thời tiết , sóng gió , mớn nước và trọng tải của tàu thuyền , chỉ định vị trí cụ thể cho tàu thuyền đón trả hoa tiêu , kiểm dịch vµ neo đậu trong vùng nước quy định tại Điều 3 của Quyết định này ; trường hợp có bão , nếu cần thiết , Cảng vụ hàng hải Quảng Trị điều động tàu thuyền sang khu vực phù hợp , bảo đảm an toàn hàng hải , an ninh hàng hải và phòng ngừa ô nhiễm môi trường .** → `KHOAN` (span: `[11:79]`)
- `[e5]` **Điều 3 của Quyết định này** → `THAM_CHIEU_PHAP_LY` (span: `[46:51]`) *(lồng trong `e4` (`KHOAN`))*
- `[e6]` **quy định tại** → `TU_KHOA_PHAP_LY` (span: `[44:46]`) *(lồng trong `e4` (`KHOAN`))*
- `[e7]` **Cảng vụ hàng hải** → `CO_QUAN_THAM_QUYEN` (span: `[59:61]`) *(lồng trong `e4` (`KHOAN`))*

**Quan hệ:**
- (`e1` 08/2007/QĐ-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 08/2007/QĐ-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Quyết định `[LOAI_VAN_BAN]`)
- (`e3` Điều 4 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 08/2007/QĐ-BGTVT `[SO_HIEU]`)
- (`e4` 2 . Căn cứ vào tình hình thực tế về thời tiết , sóng gió , mớn nước và trọng tải của tàu thuyền , chỉ định vị trí cụ thể cho tàu thuyền đón trả hoa tiêu , kiểm dịch vµ neo đậu trong vùng nước quy định tại Điều 3 của Quyết định này ; trường hợp có bão , nếu cần thiết , Cảng vụ hàng hải Quảng Trị điều động tàu thuyền sang khu vực phù hợp , bảo đảm an toàn hàng hải , an ninh hàng hải và phòng ngừa ô nhiễm môi trường . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 4 `[DIEU]`)
- (`e6` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e5` Điều 3 của Quyết định này `[THAM_CHIEU_PHAP_LY]`)
- (`e4` 2 . Căn cứ vào tình hình thực tế về thời tiết , sóng gió , mớn nước và trọng tải của tàu thuyền , chỉ định vị trí cụ thể cho tàu thuyền đón trả hoa tiêu , kiểm dịch vµ neo đậu trong vùng nước quy định tại Điều 3 của Quyết định này ; trường hợp có bão , nếu cần thiết , Cảng vụ hàng hải Quảng Trị điều động tàu thuyền sang khu vực phù hợp , bảo đảm an toàn hàng hải , an ninh hàng hải và phòng ngừa ô nhiễm môi trường . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e5` Điều 3 của Quyết định này `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #08_2007_QĐ-BGTVT_14289#body_standalone_32 (Loại: `body_standalone`)
> **[Điều 4]`<DIEU>`** . **[2 . Căn cứ vào tình hình thực tế về thời tiết , sóng gió , mớn nước và trọng tải của tàu thuyền , chỉ định vị trí cụ thể cho tàu thuyền đón trả hoa tiêu , kiểm dịch vµ neo đậu trong vùng nước **[quy định tại]`<TU_KHOA_PHAP_LY>`** **[Điều 3 của Quyết định này]`<THAM_CHIEU_PHAP_LY>`** ; trường hợp có bão , nếu cần thiết , **[Cảng vụ hàng hải]`<CO_QUAN_THAM_QUYEN>`** Quảng Trị điều động tàu thuyền sang khu vực phù hợp , bảo đảm an toàn hàng hải , an ninh hàng hải và phòng ngừa ô nhiễm môi trường .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 4** → `DIEU` (span: `[0:2]`)
- `[e1]` **2 . Căn cứ vào tình hình thực tế về thời tiết , sóng gió , mớn nước và trọng tải của tàu thuyền , chỉ định vị trí cụ thể cho tàu thuyền đón trả hoa tiêu , kiểm dịch vµ neo đậu trong vùng nước quy định tại Điều 3 của Quyết định này ; trường hợp có bão , nếu cần thiết , Cảng vụ hàng hải Quảng Trị điều động tàu thuyền sang khu vực phù hợp , bảo đảm an toàn hàng hải , an ninh hàng hải và phòng ngừa ô nhiễm môi trường .** → `KHOAN` (span: `[3:71]`)
- `[e2]` **Điều 3 của Quyết định này** → `THAM_CHIEU_PHAP_LY` (span: `[38:43]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **quy định tại** → `TU_KHOA_PHAP_LY` (span: `[36:38]`) *(lồng trong `e1` (`KHOAN`))*
- `[e4]` **Cảng vụ hàng hải** → `CO_QUAN_THAM_QUYEN` (span: `[51:53]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 2 . Căn cứ vào tình hình thực tế về thời tiết , sóng gió , mớn nước và trọng tải của tàu thuyền , chỉ định vị trí cụ thể cho tàu thuyền đón trả hoa tiêu , kiểm dịch vµ neo đậu trong vùng nước quy định tại Điều 3 của Quyết định này ; trường hợp có bão , nếu cần thiết , Cảng vụ hàng hải Quảng Trị điều động tàu thuyền sang khu vực phù hợp , bảo đảm an toàn hàng hải , an ninh hàng hải và phòng ngừa ô nhiễm môi trường . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 4 `[DIEU]`)
- (`e3` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e2` Điều 3 của Quyết định này `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 2 . Căn cứ vào tình hình thực tế về thời tiết , sóng gió , mớn nước và trọng tải của tàu thuyền , chỉ định vị trí cụ thể cho tàu thuyền đón trả hoa tiêu , kiểm dịch vµ neo đậu trong vùng nước quy định tại Điều 3 của Quyết định này ; trường hợp có bão , nếu cần thiết , Cảng vụ hàng hải Quảng Trị điều động tàu thuyền sang khu vực phù hợp , bảo đảm an toàn hàng hải , an ninh hàng hải và phòng ngừa ô nhiễm môi trường . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e2` Điều 3 của Quyết định này `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #08_2007_QĐ-BGTVT_14289#body_context_33 (Loại: `body_context`)
> **[Quyết định]`<LOAI_VAN_BAN>`** số **[08/2007/QĐ-BGTVT]`<SO_HIEU>`** ban hành **[ngày 23 tháng 02 năm 2007]`<NGAY_BAN_HANH>`** bởi **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** . **[Điều 5 . Ngoài phạm vi vùng nước **[quy định tại]`<TU_KHOA_PHAP_LY>`** **[Điều 2 và Điều 3 Quyết định này]`<THAM_CHIEU_PHAP_LY>`** , **[Cảng vụ hàng hải]`<CO_QUAN_THAM_QUYEN>`** Quảng Trị còn có trách nhiệm quản lý nhà nước về an toàn hàng hải , an ninh hàng hải trong vùng biển thuộc địa phận tỉnh Quảng Trị .]`<DIEU>`**

**Thực thể:**
- `[e0]` **Quyết định** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **08/2007/QĐ-BGTVT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[11:14]`)
- `[e3]` **ngày 23 tháng 02 năm 2007** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 5 . Ngoài phạm vi vùng nước quy định tại Điều 2 và Điều 3 Quyết định này , Cảng vụ hàng hải Quảng Trị còn có trách nhiệm quản lý nhà nước về an toàn hàng hải , an ninh hàng hải trong vùng biển thuộc địa phận tỉnh Quảng Trị .** → `DIEU` (span: `[15:53]`)
- `[e5]` **Điều 2 và Điều 3 Quyết định này** → `THAM_CHIEU_PHAP_LY` (span: `[24:31]`) *(lồng trong `e4` (`DIEU`))*
- `[e6]` **quy định tại** → `TU_KHOA_PHAP_LY` (span: `[22:24]`) *(lồng trong `e4` (`DIEU`))*
- `[e7]` **Cảng vụ hàng hải** → `CO_QUAN_THAM_QUYEN` (span: `[32:34]`) *(lồng trong `e4` (`DIEU`))*

**Quan hệ:**
- (`e1` 08/2007/QĐ-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 08/2007/QĐ-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Quyết định `[LOAI_VAN_BAN]`)
- (`e1` 08/2007/QĐ-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 23 tháng 02 năm 2007 `[NGAY_BAN_HANH]`)
- (`e4` Điều 5 . Ngoài phạm vi vùng nước quy định tại Điều 2 và Điều 3 Quyết định này , Cảng vụ hàng hải Quảng Trị còn có trách nhiệm quản lý nhà nước về an toàn hàng hải , an ninh hàng hải trong vùng biển thuộc địa phận tỉnh Quảng Trị . `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 08/2007/QĐ-BGTVT `[SO_HIEU]`)
- (`e6` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e5` Điều 2 và Điều 3 Quyết định này `[THAM_CHIEU_PHAP_LY]`)
- (`e4` Điều 5 . Ngoài phạm vi vùng nước quy định tại Điều 2 và Điều 3 Quyết định này , Cảng vụ hàng hải Quảng Trị còn có trách nhiệm quản lý nhà nước về an toàn hàng hải , an ninh hàng hải trong vùng biển thuộc địa phận tỉnh Quảng Trị . `[DIEU]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e5` Điều 2 và Điều 3 Quyết định này `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #08_2007_QĐ-BGTVT_14289#body_standalone_34 (Loại: `body_standalone`)
> **[Điều 5 . Ngoài phạm vi vùng nước **[quy định tại]`<TU_KHOA_PHAP_LY>`** **[Điều 2 và Điều 3 Quyết định này]`<THAM_CHIEU_PHAP_LY>`** , **[Cảng vụ hàng hải]`<CO_QUAN_THAM_QUYEN>`** Quảng Trị còn có trách nhiệm quản lý nhà nước về an toàn hàng hải , an ninh hàng hải trong vùng biển thuộc địa phận tỉnh Quảng Trị .]`<DIEU>`**

**Thực thể:**
- `[e0]` **Điều 5 . Ngoài phạm vi vùng nước quy định tại Điều 2 và Điều 3 Quyết định này , Cảng vụ hàng hải Quảng Trị còn có trách nhiệm quản lý nhà nước về an toàn hàng hải , an ninh hàng hải trong vùng biển thuộc địa phận tỉnh Quảng Trị .** → `DIEU` (span: `[0:38]`)
- `[e1]` **Điều 2 và Điều 3 Quyết định này** → `THAM_CHIEU_PHAP_LY` (span: `[9:16]`) *(lồng trong `e0` (`DIEU`))*
- `[e2]` **quy định tại** → `TU_KHOA_PHAP_LY` (span: `[7:9]`) *(lồng trong `e0` (`DIEU`))*
- `[e3]` **Cảng vụ hàng hải** → `CO_QUAN_THAM_QUYEN` (span: `[17:19]`) *(lồng trong `e0` (`DIEU`))*

**Quan hệ:**
- (`e2` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e1` Điều 2 và Điều 3 Quyết định này `[THAM_CHIEU_PHAP_LY]`)
- (`e0` Điều 5 . Ngoài phạm vi vùng nước quy định tại Điều 2 và Điều 3 Quyết định này , Cảng vụ hàng hải Quảng Trị còn có trách nhiệm quản lý nhà nước về an toàn hàng hải , an ninh hàng hải trong vùng biển thuộc địa phận tỉnh Quảng Trị . `[DIEU]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e1` Điều 2 và Điều 3 Quyết định này `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #08_2007_QĐ-BGTVT_14289#body_context_35 (Loại: `body_context`)
> **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** ban hành **[Quyết định]`<LOAI_VAN_BAN>`** số **[08/2007/QĐ-BGTVT]`<SO_HIEU>`** . **[Điều 6 . Quyết định này có hiệu lực **[sau 15 ngày]`<THOI_HAN>`** , kể từ ngày đăng Công báo và **[bãi bỏ]`<TU_KHOA_PHAP_LY>`** **[Quyết định số 4466/2002/QĐ-BGTVT]`<THAM_CHIEU_PHAP_LY>`** **[ngày 31 tháng 12 năm 2002]`<NGAY_THAM_CHIEU>`** của **[Bộ trưởng Bộ Giao thông vận tải]`<CO_QUAN_THAM_QUYEN>`** về vùng nước các cảng biển thuộc địa phận tỉnh Quảng Trị và khu vực trách nhiệm của Cảng vụ Quảng Trị .]`<DIEU>`**

**Thực thể:**
- `[e0]` **Quyết định** → `LOAI_VAN_BAN` (span: `[4:5]`)
- `[e1]` **08/2007/QĐ-BGTVT** → `SO_HIEU` (span: `[6:7]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[0:3]`)
- `[e3]` **Điều 6 . Quyết định này có hiệu lực sau 15 ngày , kể từ ngày đăng Công báo và bãi bỏ Quyết định số 4466/2002/QĐ-BGTVT ngày 31 tháng 12 năm 2002 của Bộ trưởng Bộ Giao thông vận tải về vùng nước các cảng biển thuộc địa phận tỉnh Quảng Trị và khu vực trách nhiệm của Cảng vụ Quảng Trị .** → `DIEU` (span: `[8:57]`)
- `[e4]` **Quyết định số 4466/2002/QĐ-BGTVT** → `THAM_CHIEU_PHAP_LY` (span: `[26:29]`) *(lồng trong `e3` (`DIEU`))*
- `[e5]` **bãi bỏ** → `TU_KHOA_PHAP_LY` (span: `[25:26]`) *(lồng trong `e3` (`DIEU`))*
- `[e6]` **ngày 31 tháng 12 năm 2002** → `NGAY_THAM_CHIEU` (span: `[29:35]`) *(lồng trong `e3` (`DIEU`))*
- `[e7]` **sau 15 ngày** → `THOI_HAN` (span: `[15:18]`) *(lồng trong `e3` (`DIEU`))*
- `[e8]` **Bộ trưởng Bộ Giao thông vận tải** → `CO_QUAN_THAM_QUYEN` (span: `[36:40]`) *(lồng trong `e3` (`DIEU`))*

**Quan hệ:**
- (`e1` 08/2007/QĐ-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 08/2007/QĐ-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Quyết định `[LOAI_VAN_BAN]`)
- (`e3` Điều 6 . Quyết định này có hiệu lực sau 15 ngày , kể từ ngày đăng Công báo và bãi bỏ Quyết định số 4466/2002/QĐ-BGTVT ngày 31 tháng 12 năm 2002 của Bộ trưởng Bộ Giao thông vận tải về vùng nước các cảng biển thuộc địa phận tỉnh Quảng Trị và khu vực trách nhiệm của Cảng vụ Quảng Trị . `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 08/2007/QĐ-BGTVT `[SO_HIEU]`)
- (`e5` bãi bỏ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e4` Quyết định số 4466/2002/QĐ-BGTVT `[THAM_CHIEU_PHAP_LY]`)
- (`e3` Điều 6 . Quyết định này có hiệu lực sau 15 ngày , kể từ ngày đăng Công báo và bãi bỏ Quyết định số 4466/2002/QĐ-BGTVT ngày 31 tháng 12 năm 2002 của Bộ trưởng Bộ Giao thông vận tải về vùng nước các cảng biển thuộc địa phận tỉnh Quảng Trị và khu vực trách nhiệm của Cảng vụ Quảng Trị . `[DIEU]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e4` Quyết định số 4466/2002/QĐ-BGTVT `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e4` Quyết định số 4466/2002/QĐ-BGTVT `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e6` ngày 31 tháng 12 năm 2002 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #08_2007_QĐ-BGTVT_14289#body_standalone_36 (Loại: `body_standalone`)
> **[Điều 6 . Quyết định này có hiệu lực **[sau 15 ngày]`<THOI_HAN>`** , kể từ ngày đăng Công báo và **[bãi bỏ]`<TU_KHOA_PHAP_LY>`** **[Quyết định số 4466/2002/QĐ-BGTVT]`<THAM_CHIEU_PHAP_LY>`** **[ngày 31 tháng 12 năm 2002]`<NGAY_THAM_CHIEU>`** của **[Bộ trưởng Bộ Giao thông vận tải]`<CO_QUAN_THAM_QUYEN>`** về vùng nước các cảng biển thuộc địa phận tỉnh Quảng Trị và khu vực trách nhiệm của Cảng vụ Quảng Trị .]`<DIEU>`**

**Thực thể:**
- `[e0]` **Điều 6 . Quyết định này có hiệu lực sau 15 ngày , kể từ ngày đăng Công báo và bãi bỏ Quyết định số 4466/2002/QĐ-BGTVT ngày 31 tháng 12 năm 2002 của Bộ trưởng Bộ Giao thông vận tải về vùng nước các cảng biển thuộc địa phận tỉnh Quảng Trị và khu vực trách nhiệm của Cảng vụ Quảng Trị .** → `DIEU` (span: `[0:49]`)
- `[e1]` **Quyết định số 4466/2002/QĐ-BGTVT** → `THAM_CHIEU_PHAP_LY` (span: `[18:21]`) *(lồng trong `e0` (`DIEU`))*
- `[e2]` **bãi bỏ** → `TU_KHOA_PHAP_LY` (span: `[17:18]`) *(lồng trong `e0` (`DIEU`))*
- `[e3]` **ngày 31 tháng 12 năm 2002** → `NGAY_THAM_CHIEU` (span: `[21:27]`) *(lồng trong `e0` (`DIEU`))*
- `[e4]` **sau 15 ngày** → `THOI_HAN` (span: `[7:10]`) *(lồng trong `e0` (`DIEU`))*
- `[e5]` **Bộ trưởng Bộ Giao thông vận tải** → `CO_QUAN_THAM_QUYEN` (span: `[28:32]`) *(lồng trong `e0` (`DIEU`))*

**Quan hệ:**
- (`e2` bãi bỏ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e1` Quyết định số 4466/2002/QĐ-BGTVT `[THAM_CHIEU_PHAP_LY]`)
- (`e0` Điều 6 . Quyết định này có hiệu lực sau 15 ngày , kể từ ngày đăng Công báo và bãi bỏ Quyết định số 4466/2002/QĐ-BGTVT ngày 31 tháng 12 năm 2002 của Bộ trưởng Bộ Giao thông vận tải về vùng nước các cảng biển thuộc địa phận tỉnh Quảng Trị và khu vực trách nhiệm của Cảng vụ Quảng Trị . `[DIEU]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e1` Quyết định số 4466/2002/QĐ-BGTVT `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e1` Quyết định số 4466/2002/QĐ-BGTVT `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e3` ngày 31 tháng 12 năm 2002 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #08_2007_QĐ-BGTVT_14289#body_context_37 (Loại: `body_context`)
> **[Quyết định]`<LOAI_VAN_BAN>`** số **[08/2007/QĐ-BGTVT]`<SO_HIEU>`** ban hành **[ngày 23 tháng 02 năm 2007]`<NGAY_BAN_HANH>`** bởi **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** . **[Điều 7 . Chánh Văn phòng Bộ , **[Chánh Thanh tra Bộ]`<CO_QUAN_THAM_QUYEN>`** , Vụ trưởng các Vụ thuộc Bộ , Cục trưởng Cục Hàng hải Việt Nam , Cục trưởng Cục Đường sông Việt Nam , **[Giám đốc Sở Giao thông vận tải]`<CO_QUAN_THAM_QUYEN>`** tỉnh Quảng Trị , **[Giám đốc]`<CHU_THE_CA_NHAN>`** **[Cảng vụ hàng hải]`<CO_QUAN_THAM_QUYEN>`** Quảng Trị , Thủ trưởng các cơ quan , tổ chức và cá nhân có liên quan chịu trách nhiệm thi hành Quyết định này . / .]`<DIEU>`**

**Thực thể:**
- `[e0]` **Quyết định** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **08/2007/QĐ-BGTVT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[11:14]`)
- `[e3]` **ngày 23 tháng 02 năm 2007** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 7 . Chánh Văn phòng Bộ , Chánh Thanh tra Bộ , Vụ trưởng các Vụ thuộc Bộ , Cục trưởng Cục Hàng hải Việt Nam , Cục trưởng Cục Đường sông Việt Nam , Giám đốc Sở Giao thông vận tải tỉnh Quảng Trị , Giám đốc Cảng vụ hàng hải Quảng Trị , Thủ trưởng các cơ quan , tổ chức và cá nhân có liên quan chịu trách nhiệm thi hành Quyết định này . / .** → `DIEU` (span: `[15:71]`)
- `[e5]` **Chánh Thanh tra Bộ** → `CO_QUAN_THAM_QUYEN` (span: `[22:25]`) *(lồng trong `e4` (`DIEU`))*
- `[e6]` **Giám đốc Sở Giao thông vận tải** → `CO_QUAN_THAM_QUYEN` (span: `[42:46]`) *(lồng trong `e4` (`DIEU`))*
- `[e7]` **Cảng vụ hàng hải** → `CO_QUAN_THAM_QUYEN` (span: `[50:52]`) *(lồng trong `e4` (`DIEU`))*
- `[e8]` **Giám đốc** → `CHU_THE_CA_NHAN` (span: `[49:50]`) *(lồng trong `e4` (`DIEU`))*

**Quan hệ:**
- (`e1` 08/2007/QĐ-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 08/2007/QĐ-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Quyết định `[LOAI_VAN_BAN]`)
- (`e1` 08/2007/QĐ-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 23 tháng 02 năm 2007 `[NGAY_BAN_HANH]`)
- (`e4` Điều 7 . Chánh Văn phòng Bộ , Chánh Thanh tra Bộ , Vụ trưởng các Vụ thuộc Bộ , Cục trưởng Cục Hàng hải Việt Nam , Cục trưởng Cục Đường sông Việt Nam , Giám đốc Sở Giao thông vận tải tỉnh Quảng Trị , Giám đốc Cảng vụ hàng hải Quảng Trị , Thủ trưởng các cơ quan , tổ chức và cá nhân có liên quan chịu trách nhiệm thi hành Quyết định này . / . `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 08/2007/QĐ-BGTVT `[SO_HIEU]`)


---

### Mẫu #08_2007_QĐ-BGTVT_14289#hard_negative_38 (Loại: `hard_negative`)
> CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM


---
