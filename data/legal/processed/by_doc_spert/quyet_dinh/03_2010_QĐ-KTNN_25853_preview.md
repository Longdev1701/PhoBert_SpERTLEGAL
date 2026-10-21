# Dữ liệu gán nhãn văn bản: 03_2010_QĐ-KTNN_25853
- **Thể loại**: `quyet_dinh`
- **Phân vùng dữ liệu**: `DEV`
- **Tổng số mẫu**: 17 mẫu
- **Tổng số thực thể**: 79
- **Tổng số quan hệ**: 50

---

### Mẫu #03_2010_QĐ-KTNN_25853#header_0 (Loại: `header`)
> TỔNG **[KIỂM TOÁN NHÀ NƯỚC]`<CO_QUAN_BAN_HANH>`** . CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM . Độc lập – Tự do – Hạnh phúc . Số : **[03/2010/QĐ-KTNN]`<SO_HIEU>`** . Hà Nội , **[ngày 10 tháng 02 năm 2010]`<NGAY_BAN_HANH>`** . **[QUYẾT ĐỊNH]`<LOAI_VAN_BAN>`**

**Thực thể:**
- `[e0]` **03/2010/QĐ-KTNN** → `SO_HIEU` (span: `[19:20]`)
- `[e1]` **ngày 10 tháng 02 năm 2010** → `NGAY_BAN_HANH` (span: `[23:29]`)
- `[e2]` **KIỂM TOÁN NHÀ NƯỚC** → `CO_QUAN_BAN_HANH` (span: `[1:3]`)
- `[e3]` **QUYẾT ĐỊNH** → `LOAI_VAN_BAN` (span: `[30:31]`)

**Quan hệ:**
- (`e0` 03/2010/QĐ-KTNN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` KIỂM TOÁN NHÀ NƯỚC `[CO_QUAN_BAN_HANH]`)
- (`e0` 03/2010/QĐ-KTNN `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e1` ngày 10 tháng 02 năm 2010 `[NGAY_BAN_HANH]`)
- (`e0` 03/2010/QĐ-KTNN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e3` QUYẾT ĐỊNH `[LOAI_VAN_BAN]`)


---

### Mẫu #03_2010_QĐ-KTNN_25853#signature_1 (Loại: `signature`)
> **[TỔNG KIỂM TOÁN NHÀ NƯỚC]`<CHUC_DANH_NGUOI_KY>`** . ( Đã ký ) . **[Vương Đình Huệ]`<NGUOI_KY>`**

**Thực thể:**
- `[e0]` **Vương Đình Huệ** → `NGUOI_KY` (span: `[8:9]`)
- `[e1]` **TỔNG KIỂM TOÁN NHÀ NƯỚC** → `CHUC_DANH_NGUOI_KY` (span: `[0:2]`)

**Quan hệ:**
- (`e0` Vương Đình Huệ `[NGUOI_KY]`) ==[ **GIU_CHUC_VU** ]==> (`e1` TỔNG KIỂM TOÁN NHÀ NƯỚC `[CHUC_DANH_NGUOI_KY]`)


---

### Mẫu #03_2010_QĐ-KTNN_25853#meta_2 (Loại: `meta`)
> TỔNG **[KIỂM TOÁN NHÀ NƯỚC]`<CO_QUAN_BAN_HANH>`** . CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM . Độc lập – Tự do – Hạnh phúc . Số : **[03/2010/QĐ-KTNN]`<SO_HIEU>`** . Hà Nội , ngày 10 tháng 02 năm 2010 . **[QUYẾT ĐỊNH]`<LOAI_VAN_BAN>`** . **[TỔNG KIỂM TOÁN NHÀ NƯỚC]`<CHUC_DANH_NGUOI_KY>`** . ( Đã ký ) . **[Vương Đình Huệ]`<NGUOI_KY>`**

**Thực thể:**
- `[e0]` **03/2010/QĐ-KTNN** → `SO_HIEU` (span: `[19:20]`)
- `[e1]` **KIỂM TOÁN NHÀ NƯỚC** → `CO_QUAN_BAN_HANH` (span: `[1:3]`)
- `[e2]` **QUYẾT ĐỊNH** → `LOAI_VAN_BAN` (span: `[30:31]`)
- `[e3]` **Vương Đình Huệ** → `NGUOI_KY` (span: `[40:41]`)
- `[e4]` **TỔNG KIỂM TOÁN NHÀ NƯỚC** → `CHUC_DANH_NGUOI_KY` (span: `[32:34]`)

**Quan hệ:**
- (`e0` 03/2010/QĐ-KTNN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e1` KIỂM TOÁN NHÀ NƯỚC `[CO_QUAN_BAN_HANH]`)
- (`e0` 03/2010/QĐ-KTNN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e2` QUYẾT ĐỊNH `[LOAI_VAN_BAN]`)
- (`e0` 03/2010/QĐ-KTNN `[SO_HIEU]`) ==[ **KY_BOI** ]==> (`e3` Vương Đình Huệ `[NGUOI_KY]`)
- (`e3` Vương Đình Huệ `[NGUOI_KY]`) ==[ **GIU_CHUC_VU** ]==> (`e4` TỔNG KIỂM TOÁN NHÀ NƯỚC `[CHUC_DANH_NGUOI_KY]`)


---

### Mẫu #03_2010_QĐ-KTNN_25853#preamble_context_3 (Loại: `preamble_context`)
> **[Quyết định]`<LOAI_VAN_BAN>`** số **[03/2010/QĐ-KTNN]`<SO_HIEU>`** của **[Kiểm toán nhà nước]`<CO_QUAN_BAN_HANH>`** . Ban hành Quy trình kiểm toán Các **[tổ chức tài chính]`<TO_CHUC_DOANH_NGHIEP>`** - ngân hàng

**Thực thể:**
- `[e0]` **Quyết định** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **03/2010/QĐ-KTNN** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Kiểm toán nhà nước** → `CO_QUAN_BAN_HANH` (span: `[4:6]`)
- `[e3]` **tổ chức tài chính** → `TO_CHUC_DOANH_NGHIEP` (span: `[11:13]`)

**Quan hệ:**
- (`e1` 03/2010/QĐ-KTNN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Kiểm toán nhà nước `[CO_QUAN_BAN_HANH]`)
- (`e1` 03/2010/QĐ-KTNN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Quyết định `[LOAI_VAN_BAN]`)


---

### Mẫu #03_2010_QĐ-KTNN_25853#preamble_standalone_4 (Loại: `preamble_standalone`)
> Ban hành Quy trình kiểm toán Các **[tổ chức tài chính]`<TO_CHUC_DOANH_NGHIEP>`** - ngân hàng

**Thực thể:**
- `[e0]` **tổ chức tài chính** → `TO_CHUC_DOANH_NGHIEP` (span: `[4:6]`)


---

### Mẫu #03_2010_QĐ-KTNN_25853#preamble_context_5 (Loại: `preamble_context`)
> **[Quyết định]`<LOAI_VAN_BAN>`** số **[03/2010/QĐ-KTNN]`<SO_HIEU>`** của **[Kiểm toán nhà nước]`<CO_QUAN_BAN_HANH>`** . **[Căn cứ]`<TU_KHOA_PHAP_LY>`** **[Luật Kiểm toán nhà nước]`<THAM_CHIEU_PHAP_LY>`** ;

**Thực thể:**
- `[e0]` **Quyết định** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **03/2010/QĐ-KTNN** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Kiểm toán nhà nước** → `CO_QUAN_BAN_HANH` (span: `[4:6]`)
- `[e3]` **Luật Kiểm toán nhà nước** → `THAM_CHIEU_PHAP_LY` (span: `[8:11]`)
- `[e4]` **Căn cứ** → `TU_KHOA_PHAP_LY` (span: `[7:8]`)

**Quan hệ:**
- (`e1` 03/2010/QĐ-KTNN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Kiểm toán nhà nước `[CO_QUAN_BAN_HANH]`)
- (`e1` 03/2010/QĐ-KTNN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Quyết định `[LOAI_VAN_BAN]`)
- (`e4` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Luật Kiểm toán nhà nước `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 03/2010/QĐ-KTNN `[SO_HIEU]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Luật Kiểm toán nhà nước `[THAM_CHIEU_PHAP_LY]`)


---

### Mẫu #03_2010_QĐ-KTNN_25853#preamble_standalone_6 (Loại: `preamble_standalone`)
> **[Căn cứ]`<TU_KHOA_PHAP_LY>`** **[Luật Kiểm toán nhà nước]`<THAM_CHIEU_PHAP_LY>`** ;

**Thực thể:**
- `[e0]` **Luật Kiểm toán nhà nước** → `THAM_CHIEU_PHAP_LY` (span: `[1:4]`)
- `[e1]` **Căn cứ** → `TU_KHOA_PHAP_LY` (span: `[0:1]`)

**Quan hệ:**
- (`e1` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e0` Luật Kiểm toán nhà nước `[THAM_CHIEU_PHAP_LY]`)


---

### Mẫu #03_2010_QĐ-KTNN_25853#preamble_context_7 (Loại: `preamble_context`)
> **[Quyết định]`<LOAI_VAN_BAN>`** số **[03/2010/QĐ-KTNN]`<SO_HIEU>`** của **[Kiểm toán nhà nước]`<CO_QUAN_BAN_HANH>`** . **[Căn cứ]`<TU_KHOA_PHAP_LY>`** **[Nghị quyết số 916/2005/NQ-UBTVQH11]`<THAM_CHIEU_PHAP_LY>`** **[ngày 15/9/2005]`<NGAY_THAM_CHIEU>`** của **[Ủy ban Thường vụ Quốc hội]`<CO_QUAN_THAM_QUYEN>`** về cơ cấu tổ chức của **[Kiểm toán Nhà nước]`<CO_QUAN_THAM_QUYEN>`** ;

**Thực thể:**
- `[e0]` **Quyết định** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **03/2010/QĐ-KTNN** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Kiểm toán nhà nước** → `CO_QUAN_BAN_HANH` (span: `[4:6]`)
- `[e3]` **Nghị quyết số 916/2005/NQ-UBTVQH11** → `THAM_CHIEU_PHAP_LY` (span: `[8:11]`)
- `[e4]` **Căn cứ** → `TU_KHOA_PHAP_LY` (span: `[7:8]`)
- `[e5]` **ngày 15/9/2005** → `NGAY_THAM_CHIEU` (span: `[11:13]`)
- `[e6]` **Ủy ban Thường vụ Quốc hội** → `CO_QUAN_THAM_QUYEN` (span: `[14:17]`)
- `[e7]` **Kiểm toán Nhà nước** → `CO_QUAN_THAM_QUYEN` (span: `[21:23]`)

**Quan hệ:**
- (`e1` 03/2010/QĐ-KTNN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Kiểm toán nhà nước `[CO_QUAN_BAN_HANH]`)
- (`e1` 03/2010/QĐ-KTNN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Quyết định `[LOAI_VAN_BAN]`)
- (`e4` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Nghị quyết số 916/2005/NQ-UBTVQH11 `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 03/2010/QĐ-KTNN `[SO_HIEU]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Nghị quyết số 916/2005/NQ-UBTVQH11 `[THAM_CHIEU_PHAP_LY]`)
- (`e3` Nghị quyết số 916/2005/NQ-UBTVQH11 `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e5` ngày 15/9/2005 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #03_2010_QĐ-KTNN_25853#preamble_standalone_8 (Loại: `preamble_standalone`)
> **[Căn cứ]`<TU_KHOA_PHAP_LY>`** **[Nghị quyết số 916/2005/NQ-UBTVQH11]`<THAM_CHIEU_PHAP_LY>`** **[ngày 15/9/2005]`<NGAY_THAM_CHIEU>`** của **[Ủy ban Thường vụ Quốc hội]`<CO_QUAN_THAM_QUYEN>`** về cơ cấu tổ chức của **[Kiểm toán Nhà nước]`<CO_QUAN_THAM_QUYEN>`** ;

**Thực thể:**
- `[e0]` **Nghị quyết số 916/2005/NQ-UBTVQH11** → `THAM_CHIEU_PHAP_LY` (span: `[1:4]`)
- `[e1]` **Căn cứ** → `TU_KHOA_PHAP_LY` (span: `[0:1]`)
- `[e2]` **ngày 15/9/2005** → `NGAY_THAM_CHIEU` (span: `[4:6]`)
- `[e3]` **Ủy ban Thường vụ Quốc hội** → `CO_QUAN_THAM_QUYEN` (span: `[7:10]`)
- `[e4]` **Kiểm toán Nhà nước** → `CO_QUAN_THAM_QUYEN` (span: `[14:16]`)

**Quan hệ:**
- (`e1` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e0` Nghị quyết số 916/2005/NQ-UBTVQH11 `[THAM_CHIEU_PHAP_LY]`)
- (`e3` Ủy ban Thường vụ Quốc hội `[CO_QUAN_THAM_QUYEN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e0` Nghị quyết số 916/2005/NQ-UBTVQH11 `[THAM_CHIEU_PHAP_LY]`)
- (`e0` Nghị quyết số 916/2005/NQ-UBTVQH11 `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e2` ngày 15/9/2005 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #03_2010_QĐ-KTNN_25853#preamble_context_9 (Loại: `preamble_context`)
> **[Quyết định]`<LOAI_VAN_BAN>`** số **[03/2010/QĐ-KTNN]`<SO_HIEU>`** của **[Kiểm toán nhà nước]`<CO_QUAN_BAN_HANH>`** . **[Căn cứ]`<TU_KHOA_PHAP_LY>`** **[Quyết định số 02/2008/QĐ-KTNN]`<THAM_CHIEU_PHAP_LY>`** **[ngày 15/02/2008]`<NGAY_THAM_CHIEU>`** của **[Tổng Kiểm toán Nhà nước]`<CO_QUAN_THAM_QUYEN>`** ban hành Quy chế soạn thảo , thẩm định và ban hành văn bản quy phạm pháp luật của **[Kiểm toán Nhà nước]`<CO_QUAN_THAM_QUYEN>`** ;

**Thực thể:**
- `[e0]` **Quyết định** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **03/2010/QĐ-KTNN** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Kiểm toán nhà nước** → `CO_QUAN_BAN_HANH` (span: `[4:6]`)
- `[e3]` **Quyết định số 02/2008/QĐ-KTNN** → `THAM_CHIEU_PHAP_LY` (span: `[8:11]`)
- `[e4]` **Căn cứ** → `TU_KHOA_PHAP_LY` (span: `[7:8]`)
- `[e5]` **ngày 15/02/2008** → `NGAY_THAM_CHIEU` (span: `[11:13]`)
- `[e6]` **Tổng Kiểm toán Nhà nước** → `CO_QUAN_THAM_QUYEN` (span: `[14:16]`)
- `[e7]` **Kiểm toán Nhà nước** → `CO_QUAN_THAM_QUYEN` (span: `[25:27]`)

**Quan hệ:**
- (`e1` 03/2010/QĐ-KTNN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Kiểm toán nhà nước `[CO_QUAN_BAN_HANH]`)
- (`e1` 03/2010/QĐ-KTNN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Quyết định `[LOAI_VAN_BAN]`)
- (`e4` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Quyết định số 02/2008/QĐ-KTNN `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 03/2010/QĐ-KTNN `[SO_HIEU]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Quyết định số 02/2008/QĐ-KTNN `[THAM_CHIEU_PHAP_LY]`)
- (`e3` Quyết định số 02/2008/QĐ-KTNN `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e5` ngày 15/02/2008 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #03_2010_QĐ-KTNN_25853#preamble_standalone_10 (Loại: `preamble_standalone`)
> **[Căn cứ]`<TU_KHOA_PHAP_LY>`** **[Quyết định số 02/2008/QĐ-KTNN]`<THAM_CHIEU_PHAP_LY>`** **[ngày 15/02/2008]`<NGAY_THAM_CHIEU>`** của **[Tổng Kiểm toán Nhà nước]`<CO_QUAN_THAM_QUYEN>`** ban hành Quy chế soạn thảo , thẩm định và ban hành văn bản quy phạm pháp luật của **[Kiểm toán Nhà nước]`<CO_QUAN_THAM_QUYEN>`** ;

**Thực thể:**
- `[e0]` **Quyết định số 02/2008/QĐ-KTNN** → `THAM_CHIEU_PHAP_LY` (span: `[1:4]`)
- `[e1]` **Căn cứ** → `TU_KHOA_PHAP_LY` (span: `[0:1]`)
- `[e2]` **ngày 15/02/2008** → `NGAY_THAM_CHIEU` (span: `[4:6]`)
- `[e3]` **Tổng Kiểm toán Nhà nước** → `CO_QUAN_THAM_QUYEN` (span: `[7:9]`)
- `[e4]` **Kiểm toán Nhà nước** → `CO_QUAN_THAM_QUYEN` (span: `[18:20]`)

**Quan hệ:**
- (`e1` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e0` Quyết định số 02/2008/QĐ-KTNN `[THAM_CHIEU_PHAP_LY]`)
- (`e3` Tổng Kiểm toán Nhà nước `[CO_QUAN_THAM_QUYEN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e0` Quyết định số 02/2008/QĐ-KTNN `[THAM_CHIEU_PHAP_LY]`)
- (`e0` Quyết định số 02/2008/QĐ-KTNN `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e2` ngày 15/02/2008 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #03_2010_QĐ-KTNN_25853#preamble_context_11 (Loại: `preamble_context`)
> **[Quyết định]`<LOAI_VAN_BAN>`** số **[03/2010/QĐ-KTNN]`<SO_HIEU>`** của **[Kiểm toán nhà nước]`<CO_QUAN_BAN_HANH>`** . **[Căn cứ]`<TU_KHOA_PHAP_LY>`** **[Quyết định số 04/2007/QĐ-KTNN]`<THAM_CHIEU_PHAP_LY>`** **[ngày 02/8/2007]`<NGAY_THAM_CHIEU>`** của **[Tổng Kiểm toán Nhà nước]`<CO_QUAN_THAM_QUYEN>`** ban hành Quy trình kiểm toán của **[Kiểm toán Nhà nước]`<CO_QUAN_THAM_QUYEN>`** ;

**Thực thể:**
- `[e0]` **Quyết định** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **03/2010/QĐ-KTNN** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Kiểm toán nhà nước** → `CO_QUAN_BAN_HANH` (span: `[4:6]`)
- `[e3]` **Quyết định số 04/2007/QĐ-KTNN** → `THAM_CHIEU_PHAP_LY` (span: `[8:11]`)
- `[e4]` **Căn cứ** → `TU_KHOA_PHAP_LY` (span: `[7:8]`)
- `[e5]` **ngày 02/8/2007** → `NGAY_THAM_CHIEU` (span: `[11:13]`)
- `[e6]` **Tổng Kiểm toán Nhà nước** → `CO_QUAN_THAM_QUYEN` (span: `[14:16]`)
- `[e7]` **Kiểm toán Nhà nước** → `CO_QUAN_THAM_QUYEN` (span: `[20:22]`)

**Quan hệ:**
- (`e1` 03/2010/QĐ-KTNN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Kiểm toán nhà nước `[CO_QUAN_BAN_HANH]`)
- (`e1` 03/2010/QĐ-KTNN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Quyết định `[LOAI_VAN_BAN]`)
- (`e4` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Quyết định số 04/2007/QĐ-KTNN `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 03/2010/QĐ-KTNN `[SO_HIEU]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Quyết định số 04/2007/QĐ-KTNN `[THAM_CHIEU_PHAP_LY]`)
- (`e3` Quyết định số 04/2007/QĐ-KTNN `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e5` ngày 02/8/2007 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #03_2010_QĐ-KTNN_25853#preamble_standalone_12 (Loại: `preamble_standalone`)
> **[Căn cứ]`<TU_KHOA_PHAP_LY>`** **[Quyết định số 04/2007/QĐ-KTNN]`<THAM_CHIEU_PHAP_LY>`** **[ngày 02/8/2007]`<NGAY_THAM_CHIEU>`** của **[Tổng Kiểm toán Nhà nước]`<CO_QUAN_THAM_QUYEN>`** ban hành Quy trình kiểm toán của **[Kiểm toán Nhà nước]`<CO_QUAN_THAM_QUYEN>`** ;

**Thực thể:**
- `[e0]` **Quyết định số 04/2007/QĐ-KTNN** → `THAM_CHIEU_PHAP_LY` (span: `[1:4]`)
- `[e1]` **Căn cứ** → `TU_KHOA_PHAP_LY` (span: `[0:1]`)
- `[e2]` **ngày 02/8/2007** → `NGAY_THAM_CHIEU` (span: `[4:6]`)
- `[e3]` **Tổng Kiểm toán Nhà nước** → `CO_QUAN_THAM_QUYEN` (span: `[7:9]`)
- `[e4]` **Kiểm toán Nhà nước** → `CO_QUAN_THAM_QUYEN` (span: `[13:15]`)

**Quan hệ:**
- (`e1` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e0` Quyết định số 04/2007/QĐ-KTNN `[THAM_CHIEU_PHAP_LY]`)
- (`e3` Tổng Kiểm toán Nhà nước `[CO_QUAN_THAM_QUYEN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e0` Quyết định số 04/2007/QĐ-KTNN `[THAM_CHIEU_PHAP_LY]`)
- (`e0` Quyết định số 04/2007/QĐ-KTNN `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e2` ngày 02/8/2007 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #03_2010_QĐ-KTNN_25853#body_context_13 (Loại: `body_context`)
> **[Quyết định]`<LOAI_VAN_BAN>`** số **[03/2010/QĐ-KTNN]`<SO_HIEU>`** của **[Kiểm toán nhà nước]`<CO_QUAN_BAN_HANH>`** . **[Điều 1 . Ban hành kèm theo Quyết định này Quy trình kiểm toán Các **[tổ chức tài chính]`<TO_CHUC_DOANH_NGHIEP>`** - ngân hàng .]`<DIEU>`**

**Thực thể:**
- `[e0]` **Quyết định** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **03/2010/QĐ-KTNN** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Kiểm toán nhà nước** → `CO_QUAN_BAN_HANH` (span: `[4:6]`)
- `[e3]` **Điều 1 . Ban hành kèm theo Quyết định này Quy trình kiểm toán Các tổ chức tài chính - ngân hàng .** → `DIEU` (span: `[7:23]`)
- `[e4]` **tổ chức tài chính** → `TO_CHUC_DOANH_NGHIEP` (span: `[18:20]`) *(lồng trong `e3` (`DIEU`))*

**Quan hệ:**
- (`e1` 03/2010/QĐ-KTNN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Kiểm toán nhà nước `[CO_QUAN_BAN_HANH]`)
- (`e1` 03/2010/QĐ-KTNN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Quyết định `[LOAI_VAN_BAN]`)
- (`e3` Điều 1 . Ban hành kèm theo Quyết định này Quy trình kiểm toán Các tổ chức tài chính - ngân hàng . `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 03/2010/QĐ-KTNN `[SO_HIEU]`)


---

### Mẫu #03_2010_QĐ-KTNN_25853#body_context_14 (Loại: `body_context`)
> **[Quyết định]`<LOAI_VAN_BAN>`** số **[03/2010/QĐ-KTNN]`<SO_HIEU>`** ban hành **[ngày 10 tháng 02 năm 2010]`<NGAY_BAN_HANH>`** bởi **[Kiểm toán nhà nước]`<CO_QUAN_BAN_HANH>`** . **[Điều 2 . Quyết định này có hiệu lực thi hành **[sau 45 ngày]`<THOI_HAN>`** , kể từ ngày ký .]`<DIEU>`**

**Thực thể:**
- `[e0]` **Quyết định** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **03/2010/QĐ-KTNN** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Kiểm toán nhà nước** → `CO_QUAN_BAN_HANH` (span: `[11:13]`)
- `[e3]` **ngày 10 tháng 02 năm 2010** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 2 . Quyết định này có hiệu lực thi hành sau 45 ngày , kể từ ngày ký .** → `DIEU` (span: `[14:31]`)
- `[e5]` **sau 45 ngày** → `THOI_HAN` (span: `[22:25]`) *(lồng trong `e4` (`DIEU`))*

**Quan hệ:**
- (`e1` 03/2010/QĐ-KTNN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Kiểm toán nhà nước `[CO_QUAN_BAN_HANH]`)
- (`e1` 03/2010/QĐ-KTNN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Quyết định `[LOAI_VAN_BAN]`)
- (`e1` 03/2010/QĐ-KTNN `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 10 tháng 02 năm 2010 `[NGAY_BAN_HANH]`)
- (`e4` Điều 2 . Quyết định này có hiệu lực thi hành sau 45 ngày , kể từ ngày ký . `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 03/2010/QĐ-KTNN `[SO_HIEU]`)


---

### Mẫu #03_2010_QĐ-KTNN_25853#body_context_15 (Loại: `body_context`)
> **[Quyết định]`<LOAI_VAN_BAN>`** số **[03/2010/QĐ-KTNN]`<SO_HIEU>`** ban hành **[ngày 10 tháng 02 năm 2010]`<NGAY_BAN_HANH>`** bởi **[Kiểm toán nhà nước]`<CO_QUAN_BAN_HANH>`** . **[Điều 3 . Thủ trưởng các đơn vị trực thuộc **[Kiểm toán Nhà nước]`<CO_QUAN_THAM_QUYEN>`** , các tổ chức và cá nhân có liên quan chịu trách nhiệm thi hành Quyết định này . / .]`<DIEU>`**

**Thực thể:**
- `[e0]` **Quyết định** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **03/2010/QĐ-KTNN** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Kiểm toán nhà nước** → `CO_QUAN_BAN_HANH` (span: `[11:13]`)
- `[e3]` **ngày 10 tháng 02 năm 2010** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 3 . Thủ trưởng các đơn vị trực thuộc Kiểm toán Nhà nước , các tổ chức và cá nhân có liên quan chịu trách nhiệm thi hành Quyết định này . / .** → `DIEU` (span: `[14:38]`)
- `[e5]` **Kiểm toán Nhà nước** → `CO_QUAN_THAM_QUYEN` (span: `[21:23]`) *(lồng trong `e4` (`DIEU`))*

**Quan hệ:**
- (`e1` 03/2010/QĐ-KTNN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Kiểm toán nhà nước `[CO_QUAN_BAN_HANH]`)
- (`e1` 03/2010/QĐ-KTNN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Quyết định `[LOAI_VAN_BAN]`)
- (`e1` 03/2010/QĐ-KTNN `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 10 tháng 02 năm 2010 `[NGAY_BAN_HANH]`)
- (`e4` Điều 3 . Thủ trưởng các đơn vị trực thuộc Kiểm toán Nhà nước , các tổ chức và cá nhân có liên quan chịu trách nhiệm thi hành Quyết định này . / . `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 03/2010/QĐ-KTNN `[SO_HIEU]`)


---

### Mẫu #03_2010_QĐ-KTNN_25853#hard_negative_16 (Loại: `hard_negative`)
> CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM


---
