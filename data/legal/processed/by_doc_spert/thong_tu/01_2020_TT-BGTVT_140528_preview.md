# Dữ liệu gán nhãn văn bản: 01_2020_TT-BGTVT_140528
- **Thể loại**: `thong_tu`
- **Phân vùng dữ liệu**: `TRAIN`
- **Tổng số mẫu**: 106 mẫu
- **Tổng số thực thể**: 667
- **Tổng số quan hệ**: 435

---

### Mẫu #01_2020_TT-BGTVT_140528#header_0 (Loại: `header`)
> **[BỘ GIAO THÔNG VẬN TẢI]`<CO_QUAN_BAN_HANH>`** . CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM . Độc lập – Tự do – Hạnh phúc . Số : **[01/2020/TT-BGTVT]`<SO_HIEU>`** . Hà Nội , **[ngày 20 tháng 01 năm 2020]`<NGAY_BAN_HANH>`** . **[THÔNG TƯ]`<LOAI_VAN_BAN>`** Quy định về báo cáo và điều tra tai nạn hàng hải

**Thực thể:**
- `[e0]` **01/2020/TT-BGTVT** → `SO_HIEU` (span: `[19:20]`)
- `[e1]` **ngày 20 tháng 01 năm 2020** → `NGAY_BAN_HANH` (span: `[23:29]`)
- `[e2]` **BỘ GIAO THÔNG VẬN TẢI** → `CO_QUAN_BAN_HANH` (span: `[0:3]`)
- `[e3]` **THÔNG TƯ** → `LOAI_VAN_BAN` (span: `[30:31]`)

**Quan hệ:**
- (`e0` 01/2020/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` BỘ GIAO THÔNG VẬN TẢI `[CO_QUAN_BAN_HANH]`)
- (`e0` 01/2020/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e1` ngày 20 tháng 01 năm 2020 `[NGAY_BAN_HANH]`)
- (`e0` 01/2020/TT-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e3` THÔNG TƯ `[LOAI_VAN_BAN]`)


---

### Mẫu #01_2020_TT-BGTVT_140528#signature_1 (Loại: `signature`)
> KT. BỘ TRƯỞNG **[THỨ TRƯỞNG]`<CHUC_DANH_NGUOI_KY>`** . **[Nguyễn Văn Công]`<NGUOI_KY>`**

**Thực thể:**
- `[e0]` **Nguyễn Văn Công** → `NGUOI_KY` (span: `[4:6]`)
- `[e1]` **THỨ TRƯỞNG** → `CHUC_DANH_NGUOI_KY` (span: `[2:3]`)

**Quan hệ:**
- (`e0` Nguyễn Văn Công `[NGUOI_KY]`) ==[ **GIU_CHUC_VU** ]==> (`e1` THỨ TRƯỞNG `[CHUC_DANH_NGUOI_KY]`)


---

### Mẫu #01_2020_TT-BGTVT_140528#meta_2 (Loại: `meta`)
> **[BỘ GIAO THÔNG VẬN TẢI]`<CO_QUAN_BAN_HANH>`** . CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM . Độc lập – Tự do – Hạnh phúc . Số : **[01/2020/TT-BGTVT]`<SO_HIEU>`** . Hà Nội , ngày 20 tháng 01 năm 2020 . **[THÔNG TƯ]`<LOAI_VAN_BAN>`** Quy định về báo cáo và điều tra tai nạn hàng hải . KT. BỘ TRƯỞNG **[THỨ TRƯỞNG]`<CHUC_DANH_NGUOI_KY>`** . **[Nguyễn Văn Công]`<NGUOI_KY>`**

**Thực thể:**
- `[e0]` **01/2020/TT-BGTVT** → `SO_HIEU` (span: `[19:20]`)
- `[e1]` **BỘ GIAO THÔNG VẬN TẢI** → `CO_QUAN_BAN_HANH` (span: `[0:3]`)
- `[e2]` **THÔNG TƯ** → `LOAI_VAN_BAN` (span: `[30:31]`)
- `[e3]` **Nguyễn Văn Công** → `NGUOI_KY` (span: `[43:45]`)
- `[e4]` **THỨ TRƯỞNG** → `CHUC_DANH_NGUOI_KY` (span: `[41:42]`)

**Quan hệ:**
- (`e0` 01/2020/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e1` BỘ GIAO THÔNG VẬN TẢI `[CO_QUAN_BAN_HANH]`)
- (`e0` 01/2020/TT-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e2` THÔNG TƯ `[LOAI_VAN_BAN]`)
- (`e0` 01/2020/TT-BGTVT `[SO_HIEU]`) ==[ **KY_BOI** ]==> (`e3` Nguyễn Văn Công `[NGUOI_KY]`)
- (`e3` Nguyễn Văn Công `[NGUOI_KY]`) ==[ **GIU_CHUC_VU** ]==> (`e4` THỨ TRƯỞNG `[CHUC_DANH_NGUOI_KY]`)


---

### Mẫu #01_2020_TT-BGTVT_140528#preamble_context_3 (Loại: `preamble_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[01/2020/TT-BGTVT]`<SO_HIEU>`** của **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** . **[Căn cứ]`<TU_KHOA_PHAP_LY>`** **[Bộ luật Hàng hải Việt Nam số 95/2015/QH13]`<THAM_CHIEU_PHAP_LY>`** **[ngày 25 tháng 11 năm 2015]`<NGAY_THAM_CHIEU>`** ;

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **01/2020/TT-BGTVT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[4:7]`)
- `[e3]` **Bộ luật Hàng hải Việt Nam số 95/2015/QH13** → `THAM_CHIEU_PHAP_LY` (span: `[9:13]`)
- `[e4]` **Căn cứ** → `TU_KHOA_PHAP_LY` (span: `[8:9]`)
- `[e5]` **ngày 25 tháng 11 năm 2015** → `NGAY_THAM_CHIEU` (span: `[13:19]`)

**Quan hệ:**
- (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e4` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Bộ luật Hàng hải Việt Nam số 95/2015/QH13 `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Bộ luật Hàng hải Việt Nam số 95/2015/QH13 `[THAM_CHIEU_PHAP_LY]`)
- (`e3` Bộ luật Hàng hải Việt Nam số 95/2015/QH13 `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e5` ngày 25 tháng 11 năm 2015 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #01_2020_TT-BGTVT_140528#preamble_standalone_4 (Loại: `preamble_standalone`)
> **[Căn cứ]`<TU_KHOA_PHAP_LY>`** **[Bộ luật Hàng hải Việt Nam số 95/2015/QH13]`<THAM_CHIEU_PHAP_LY>`** **[ngày 25 tháng 11 năm 2015]`<NGAY_THAM_CHIEU>`** ;

**Thực thể:**
- `[e0]` **Bộ luật Hàng hải Việt Nam số 95/2015/QH13** → `THAM_CHIEU_PHAP_LY` (span: `[1:5]`)
- `[e1]` **Căn cứ** → `TU_KHOA_PHAP_LY` (span: `[0:1]`)
- `[e2]` **ngày 25 tháng 11 năm 2015** → `NGAY_THAM_CHIEU` (span: `[5:11]`)

**Quan hệ:**
- (`e1` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e0` Bộ luật Hàng hải Việt Nam số 95/2015/QH13 `[THAM_CHIEU_PHAP_LY]`)
- (`e0` Bộ luật Hàng hải Việt Nam số 95/2015/QH13 `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e2` ngày 25 tháng 11 năm 2015 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #01_2020_TT-BGTVT_140528#preamble_context_5 (Loại: `preamble_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[01/2020/TT-BGTVT]`<SO_HIEU>`** của **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** . **[Căn cứ]`<TU_KHOA_PHAP_LY>`** Bộ luật về các tiêu chuẩn và khuyến nghị quốc tế đối với hoạt động điều tra tai nạn hoặc sự cố hàng hải của Tổ chức Hàng hải quốc tế ( IMO ) ;

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **01/2020/TT-BGTVT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[4:7]`)
- `[e3]` **Căn cứ** → `TU_KHOA_PHAP_LY` (span: `[8:9]`)

**Quan hệ:**
- (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)


---

### Mẫu #01_2020_TT-BGTVT_140528#preamble_standalone_6 (Loại: `preamble_standalone`)
> **[Căn cứ]`<TU_KHOA_PHAP_LY>`** Bộ luật về các tiêu chuẩn và khuyến nghị quốc tế đối với hoạt động điều tra tai nạn hoặc sự cố hàng hải của Tổ chức Hàng hải quốc tế ( IMO ) ;

**Thực thể:**
- `[e0]` **Căn cứ** → `TU_KHOA_PHAP_LY` (span: `[0:1]`)


---

### Mẫu #01_2020_TT-BGTVT_140528#preamble_context_7 (Loại: `preamble_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[01/2020/TT-BGTVT]`<SO_HIEU>`** của **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** . **[Căn cứ]`<TU_KHOA_PHAP_LY>`** **[Nghị định số 12/2017/NĐ-CP]`<THAM_CHIEU_PHAP_LY>`** **[ngày 10 tháng 02 năm 2017]`<NGAY_THAM_CHIEU>`** của **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** quy định chức năng , nhiệm vụ , quyền hạn và cơ cấu tổ chức của **[Bộ Giao thông vận tải]`<CO_QUAN_THAM_QUYEN>`** ;

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **01/2020/TT-BGTVT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[4:7]`)
- `[e3]` **Nghị định số 12/2017/NĐ-CP** → `THAM_CHIEU_PHAP_LY` (span: `[9:12]`)
- `[e4]` **Căn cứ** → `TU_KHOA_PHAP_LY` (span: `[8:9]`)
- `[e5]` **ngày 10 tháng 02 năm 2017** → `NGAY_THAM_CHIEU` (span: `[12:18]`)
- `[e6]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[19:20]`)
- `[e7]` **Bộ Giao thông vận tải** → `CO_QUAN_THAM_QUYEN` (span: `[30:33]`)

**Quan hệ:**
- (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e4` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Nghị định số 12/2017/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Nghị định số 12/2017/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e3` Nghị định số 12/2017/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e5` ngày 10 tháng 02 năm 2017 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #01_2020_TT-BGTVT_140528#preamble_standalone_8 (Loại: `preamble_standalone`)
> **[Căn cứ]`<TU_KHOA_PHAP_LY>`** **[Nghị định số 12/2017/NĐ-CP]`<THAM_CHIEU_PHAP_LY>`** **[ngày 10 tháng 02 năm 2017]`<NGAY_THAM_CHIEU>`** của **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** quy định chức năng , nhiệm vụ , quyền hạn và cơ cấu tổ chức của **[Bộ Giao thông vận tải]`<CO_QUAN_THAM_QUYEN>`** ;

**Thực thể:**
- `[e0]` **Nghị định số 12/2017/NĐ-CP** → `THAM_CHIEU_PHAP_LY` (span: `[1:4]`)
- `[e1]` **Căn cứ** → `TU_KHOA_PHAP_LY` (span: `[0:1]`)
- `[e2]` **ngày 10 tháng 02 năm 2017** → `NGAY_THAM_CHIEU` (span: `[4:10]`)
- `[e3]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[11:12]`)
- `[e4]` **Bộ Giao thông vận tải** → `CO_QUAN_THAM_QUYEN` (span: `[22:25]`)

**Quan hệ:**
- (`e1` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e0` Nghị định số 12/2017/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e3` Chính phủ `[CO_QUAN_THAM_QUYEN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e0` Nghị định số 12/2017/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e0` Nghị định số 12/2017/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e2` ngày 10 tháng 02 năm 2017 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #01_2020_TT-BGTVT_140528#preamble_context_9 (Loại: `preamble_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[01/2020/TT-BGTVT]`<SO_HIEU>`** của **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** . **[Bộ trưởng Bộ Giao thông vận tải]`<CO_QUAN_THAM_QUYEN>`** ban hành Thông tư quy định về báo cáo và điều tra tai nạn hàng hải .

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **01/2020/TT-BGTVT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[4:7]`)
- `[e3]` **Bộ trưởng Bộ Giao thông vận tải** → `CO_QUAN_THAM_QUYEN` (span: `[8:12]`)

**Quan hệ:**
- (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)


---

### Mẫu #01_2020_TT-BGTVT_140528#preamble_standalone_10 (Loại: `preamble_standalone`)
> **[Bộ trưởng Bộ Giao thông vận tải]`<CO_QUAN_THAM_QUYEN>`** ban hành Thông tư quy định về báo cáo và điều tra tai nạn hàng hải .

**Thực thể:**
- `[e0]` **Bộ trưởng Bộ Giao thông vận tải** → `CO_QUAN_THAM_QUYEN` (span: `[0:4]`)


---

### Mẫu #01_2020_TT-BGTVT_140528#body_context_11 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[01/2020/TT-BGTVT]`<SO_HIEU>`** của **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Hàng hải]`<LINH_VUC>`** . **[Chương I. QUY ĐỊNH CHUNG]`<CHUONG>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **01/2020/TT-BGTVT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[4:7]`)
- `[e3]` **Hàng hải** → `LINH_VUC` (span: `[9:10]`)
- `[e4]` **Chương I. QUY ĐỊNH CHUNG** → `CHUONG` (span: `[11:15]`)

**Quan hệ:**
- (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Hàng hải `[LINH_VUC]`)
- (`e4` Chương I. QUY ĐỊNH CHUNG `[CHUONG]`) ==[ **THUOC_VE** ]==> (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`)
- (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Hàng hải `[LINH_VUC]`)


---

### Mẫu #01_2020_TT-BGTVT_140528#body_context_12 (Loại: `body_context`)
> **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[01/2020/TT-BGTVT]`<SO_HIEU>`** . **[Điều 2]`<DIEU>`** . **[2 . Các quy định của Thông tư này cũng được áp dụng để điều tra tai nạn xảy ra đối với tàu công vụ , thủy phi cơ trong các vùng nước cảng biển Việt Nam ; **[phương tiện thủy nội địa]`<TAI_SAN_VAT_CHAT>`** mang cấp VR - SB , kho chứa nổi , giàn di động trong các vùng nước cảng biển Việt Nam và trên vùng biển Việt Nam .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[4:5]`)
- `[e1]` **01/2020/TT-BGTVT** → `SO_HIEU` (span: `[6:7]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[0:3]`)
- `[e3]` **Điều 2** → `DIEU` (span: `[8:10]`)
- `[e4]` **2 . Các quy định của Thông tư này cũng được áp dụng để điều tra tai nạn xảy ra đối với tàu công vụ , thủy phi cơ trong các vùng nước cảng biển Việt Nam ; phương tiện thủy nội địa mang cấp VR - SB , kho chứa nổi , giàn di động trong các vùng nước cảng biển Việt Nam và trên vùng biển Việt Nam .** → `KHOAN` (span: `[11:65]`)
- `[e5]` **phương tiện thủy nội địa** → `TAI_SAN_VAT_CHAT` (span: `[39:41]`) *(lồng trong `e4` (`KHOAN`))*

**Quan hệ:**
- (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 2 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`)
- (`e4` 2 . Các quy định của Thông tư này cũng được áp dụng để điều tra tai nạn xảy ra đối với tàu công vụ , thủy phi cơ trong các vùng nước cảng biển Việt Nam ; phương tiện thủy nội địa mang cấp VR - SB , kho chứa nổi , giàn di động trong các vùng nước cảng biển Việt Nam và trên vùng biển Việt Nam . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 2 `[DIEU]`)


---

### Mẫu #01_2020_TT-BGTVT_140528#body_context_13 (Loại: `body_context`)
> **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[01/2020/TT-BGTVT]`<SO_HIEU>`** . **[Điều 3]`<DIEU>`** . **[1 . Tai nạn hàng hải là sự kiện liên quan trực tiếp đến hoạt động của **[tàu biển]`<TAI_SAN_VAT_CHAT>`** gây ra một trong những hậu quả sau : làm chết người , mất tích , bị thương nặng ; làm cho **[tàu biển]`<TAI_SAN_VAT_CHAT>`** đâm va ; hư hỏng nghiêm trọng đến cấu trúc tàu ; làm cho tàu mất tích , chìm đắm , mắc cạn , mất khả năng điều động ; làm hư hỏng kết cấu hạ tầng hàng hải hoặc gây ô nhiễm môi trường nghiêm trọng . Tai nạn hàng hải không bao gồm những hành vi cố ý gây]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[4:5]`)
- `[e1]` **01/2020/TT-BGTVT** → `SO_HIEU` (span: `[6:7]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[0:3]`)
- `[e3]` **Điều 3** → `DIEU` (span: `[8:10]`)
- `[e4]` **1 . Tai nạn hàng hải là sự kiện liên quan trực tiếp đến hoạt động của tàu biển gây ra một trong những hậu quả sau : làm chết người , mất tích , bị thương nặng ; làm cho tàu biển đâm va ; hư hỏng nghiêm trọng đến cấu trúc tàu ; làm cho tàu mất tích , chìm đắm , mắc cạn , mất khả năng điều động ; làm hư hỏng kết cấu hạ tầng hàng hải hoặc gây ô nhiễm môi trường nghiêm trọng . Tai nạn hàng hải không bao gồm những hành vi cố ý gây** → `KHOAN` (span: `[11:83]`)
- `[e5]` **tàu biển** → `TAI_SAN_VAT_CHAT` (span: `[22:23]`) *(lồng trong `e4` (`KHOAN`))*
- `[e6]` **tàu biển** → `TAI_SAN_VAT_CHAT` (span: `[42:43]`) *(lồng trong `e4` (`KHOAN`))*

**Quan hệ:**
- (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 3 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`)
- (`e4` 1 . Tai nạn hàng hải là sự kiện liên quan trực tiếp đến hoạt động của tàu biển gây ra một trong những hậu quả sau : làm chết người , mất tích , bị thương nặng ; làm cho tàu biển đâm va ; hư hỏng nghiêm trọng đến cấu trúc tàu ; làm cho tàu mất tích , chìm đắm , mắc cạn , mất khả năng điều động ; làm hư hỏng kết cấu hạ tầng hàng hải hoặc gây ô nhiễm môi trường nghiêm trọng . Tai nạn hàng hải không bao gồm những hành vi cố ý gây `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 3 `[DIEU]`)


---

### Mẫu #01_2020_TT-BGTVT_140528#body_standalone_14 (Loại: `body_standalone`)
> **[Điều 3]`<DIEU>`** . **[1 . Tai nạn hàng hải là sự kiện liên quan trực tiếp đến hoạt động của **[tàu biển]`<TAI_SAN_VAT_CHAT>`** gây ra một trong những hậu quả sau : làm chết người , mất tích , bị thương nặng ; làm cho **[tàu biển]`<TAI_SAN_VAT_CHAT>`** đâm va ; hư hỏng nghiêm trọng đến cấu trúc tàu ; làm cho tàu mất tích , chìm đắm , mắc cạn , mất khả năng điều động ; làm hư hỏng kết cấu hạ tầng hàng hải hoặc gây ô nhiễm môi trường nghiêm trọng . Tai nạn hàng hải không bao gồm những hành vi cố ý gây]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 3** → `DIEU` (span: `[0:2]`)
- `[e1]` **1 . Tai nạn hàng hải là sự kiện liên quan trực tiếp đến hoạt động của tàu biển gây ra một trong những hậu quả sau : làm chết người , mất tích , bị thương nặng ; làm cho tàu biển đâm va ; hư hỏng nghiêm trọng đến cấu trúc tàu ; làm cho tàu mất tích , chìm đắm , mắc cạn , mất khả năng điều động ; làm hư hỏng kết cấu hạ tầng hàng hải hoặc gây ô nhiễm môi trường nghiêm trọng . Tai nạn hàng hải không bao gồm những hành vi cố ý gây** → `KHOAN` (span: `[3:75]`)
- `[e2]` **tàu biển** → `TAI_SAN_VAT_CHAT` (span: `[14:15]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **tàu biển** → `TAI_SAN_VAT_CHAT` (span: `[34:35]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 1 . Tai nạn hàng hải là sự kiện liên quan trực tiếp đến hoạt động của tàu biển gây ra một trong những hậu quả sau : làm chết người , mất tích , bị thương nặng ; làm cho tàu biển đâm va ; hư hỏng nghiêm trọng đến cấu trúc tàu ; làm cho tàu mất tích , chìm đắm , mắc cạn , mất khả năng điều động ; làm hư hỏng kết cấu hạ tầng hàng hải hoặc gây ô nhiễm môi trường nghiêm trọng . Tai nạn hàng hải không bao gồm những hành vi cố ý gây `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 3 `[DIEU]`)


---

### Mẫu #01_2020_TT-BGTVT_140528#body_context_15 (Loại: `body_context`)
> **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[01/2020/TT-BGTVT]`<SO_HIEU>`** . **[Điều 3]`<DIEU>`** . **[2 . Sự cố hàng hải là sự việc xảy ra liên quan trực tiếp đến hoạt động của **[tàu biển]`<TAI_SAN_VAT_CHAT>`** mà không phải là tai nạn hàng hải được **[quy định tại]`<TU_KHOA_PHAP_LY>`** **[khoản 1 Điều này]`<THAM_CHIEU_PHAP_LY>`** gây nguy hiểm hoặc nếu không được khắc phục sẽ gây nguy hiểm cho an toàn của tàu con người hoặc môi trường .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[4:5]`)
- `[e1]` **01/2020/TT-BGTVT** → `SO_HIEU` (span: `[6:7]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[0:3]`)
- `[e3]` **Điều 3** → `DIEU` (span: `[8:10]`)
- `[e4]` **2 . Sự cố hàng hải là sự việc xảy ra liên quan trực tiếp đến hoạt động của tàu biển mà không phải là tai nạn hàng hải được quy định tại khoản 1 Điều này gây nguy hiểm hoặc nếu không được khắc phục sẽ gây nguy hiểm cho an toàn của tàu con người hoặc môi trường .** → `KHOAN` (span: `[11:56]`)
- `[e5]` **khoản 1 Điều này** → `THAM_CHIEU_PHAP_LY` (span: `[34:38]`) *(lồng trong `e4` (`KHOAN`))*
- `[e6]` **quy định tại** → `TU_KHOA_PHAP_LY` (span: `[32:34]`) *(lồng trong `e4` (`KHOAN`))*
- `[e7]` **tàu biển** → `TAI_SAN_VAT_CHAT` (span: `[24:25]`) *(lồng trong `e4` (`KHOAN`))*

**Quan hệ:**
- (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 3 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`)
- (`e4` 2 . Sự cố hàng hải là sự việc xảy ra liên quan trực tiếp đến hoạt động của tàu biển mà không phải là tai nạn hàng hải được quy định tại khoản 1 Điều này gây nguy hiểm hoặc nếu không được khắc phục sẽ gây nguy hiểm cho an toàn của tàu con người hoặc môi trường . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 3 `[DIEU]`)
- (`e6` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e5` khoản 1 Điều này `[THAM_CHIEU_PHAP_LY]`)
- (`e4` 2 . Sự cố hàng hải là sự việc xảy ra liên quan trực tiếp đến hoạt động của tàu biển mà không phải là tai nạn hàng hải được quy định tại khoản 1 Điều này gây nguy hiểm hoặc nếu không được khắc phục sẽ gây nguy hiểm cho an toàn của tàu con người hoặc môi trường . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e5` khoản 1 Điều này `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #01_2020_TT-BGTVT_140528#body_standalone_16 (Loại: `body_standalone`)
> **[Điều 3]`<DIEU>`** . **[2 . Sự cố hàng hải là sự việc xảy ra liên quan trực tiếp đến hoạt động của **[tàu biển]`<TAI_SAN_VAT_CHAT>`** mà không phải là tai nạn hàng hải được **[quy định tại]`<TU_KHOA_PHAP_LY>`** **[khoản 1 Điều này]`<THAM_CHIEU_PHAP_LY>`** gây nguy hiểm hoặc nếu không được khắc phục sẽ gây nguy hiểm cho an toàn của tàu con người hoặc môi trường .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 3** → `DIEU` (span: `[0:2]`)
- `[e1]` **2 . Sự cố hàng hải là sự việc xảy ra liên quan trực tiếp đến hoạt động của tàu biển mà không phải là tai nạn hàng hải được quy định tại khoản 1 Điều này gây nguy hiểm hoặc nếu không được khắc phục sẽ gây nguy hiểm cho an toàn của tàu con người hoặc môi trường .** → `KHOAN` (span: `[3:48]`)
- `[e2]` **khoản 1 Điều này** → `THAM_CHIEU_PHAP_LY` (span: `[26:30]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **quy định tại** → `TU_KHOA_PHAP_LY` (span: `[24:26]`) *(lồng trong `e1` (`KHOAN`))*
- `[e4]` **tàu biển** → `TAI_SAN_VAT_CHAT` (span: `[16:17]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 2 . Sự cố hàng hải là sự việc xảy ra liên quan trực tiếp đến hoạt động của tàu biển mà không phải là tai nạn hàng hải được quy định tại khoản 1 Điều này gây nguy hiểm hoặc nếu không được khắc phục sẽ gây nguy hiểm cho an toàn của tàu con người hoặc môi trường . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 3 `[DIEU]`)
- (`e3` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e2` khoản 1 Điều này `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 2 . Sự cố hàng hải là sự việc xảy ra liên quan trực tiếp đến hoạt động của tàu biển mà không phải là tai nạn hàng hải được quy định tại khoản 1 Điều này gây nguy hiểm hoặc nếu không được khắc phục sẽ gây nguy hiểm cho an toàn của tàu con người hoặc môi trường . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e2` khoản 1 Điều này `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #01_2020_TT-BGTVT_140528#body_context_17 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[01/2020/TT-BGTVT]`<SO_HIEU>`** của **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Hàng hải]`<LINH_VUC>`** . **[Điều 4]`<DIEU>`** . **[Khoản 1]`<KHOAN>`** . **[c ) Làm tràn ra môi trường từ 100 tấn dầu trở lên hoặc từ 50 tấn hoá chất độc hại trở lên ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **01/2020/TT-BGTVT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[4:7]`)
- `[e3]` **Hàng hải** → `LINH_VUC` (span: `[9:10]`)
- `[e4]` **Điều 4** → `DIEU` (span: `[11:13]`)
- `[e5]` **Khoản 1** → `KHOAN` (span: `[14:16]`)
- `[e6]` **c ) Làm tràn ra môi trường từ 100 tấn dầu trở lên hoặc từ 50 tấn hoá chất độc hại trở lên ;** → `DIEM` (span: `[17:37]`)

**Quan hệ:**
- (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Hàng hải `[LINH_VUC]`)
- (`e4` Điều 4 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`)
- (`e5` Khoản 1 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 4 `[DIEU]`)
- (`e6` c ) Làm tràn ra môi trường từ 100 tấn dầu trở lên hoặc từ 50 tấn hoá chất độc hại trở lên ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e5` Khoản 1 `[KHOAN]`)
- (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Hàng hải `[LINH_VUC]`)
- (`e6` c ) Làm tràn ra môi trường từ 100 tấn dầu trở lên hoặc từ 50 tấn hoá chất độc hại trở lên ; `[DIEM]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Hàng hải `[LINH_VUC]`)


---

### Mẫu #01_2020_TT-BGTVT_140528#body_context_18 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[01/2020/TT-BGTVT]`<SO_HIEU>`** của **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Hàng hải]`<LINH_VUC>`** . **[Điều 4]`<DIEU>`** . **[2 . Tai nạn hàng hải nghiêm trọng là tai nạn hàng hải không thuộc các trường hợp **[quy định tại]`<TU_KHOA_PHAP_LY>`** **[khoản 1 Điều này]`<THAM_CHIEU_PHAP_LY>`** và gây ra một trong các thiệt hại dưới đây :]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **01/2020/TT-BGTVT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[4:7]`)
- `[e3]` **Hàng hải** → `LINH_VUC` (span: `[9:10]`)
- `[e4]` **Điều 4** → `DIEU` (span: `[11:13]`)
- `[e5]` **2 . Tai nạn hàng hải nghiêm trọng là tai nạn hàng hải không thuộc các trường hợp quy định tại khoản 1 Điều này và gây ra một trong các thiệt hại dưới đây :** → `KHOAN` (span: `[14:42]`)
- `[e6]` **khoản 1 Điều này** → `THAM_CHIEU_PHAP_LY` (span: `[28:32]`) *(lồng trong `e5` (`KHOAN`))*
- `[e7]` **quy định tại** → `TU_KHOA_PHAP_LY` (span: `[26:28]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Hàng hải `[LINH_VUC]`)
- (`e4` Điều 4 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`)
- (`e5` 2 . Tai nạn hàng hải nghiêm trọng là tai nạn hàng hải không thuộc các trường hợp quy định tại khoản 1 Điều này và gây ra một trong các thiệt hại dưới đây : `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 4 `[DIEU]`)
- (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Hàng hải `[LINH_VUC]`)
- (`e5` 2 . Tai nạn hàng hải nghiêm trọng là tai nạn hàng hải không thuộc các trường hợp quy định tại khoản 1 Điều này và gây ra một trong các thiệt hại dưới đây : `[KHOAN]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Hàng hải `[LINH_VUC]`)
- (`e7` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e6` khoản 1 Điều này `[THAM_CHIEU_PHAP_LY]`)
- (`e5` 2 . Tai nạn hàng hải nghiêm trọng là tai nạn hàng hải không thuộc các trường hợp quy định tại khoản 1 Điều này và gây ra một trong các thiệt hại dưới đây : `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e6` khoản 1 Điều này `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #01_2020_TT-BGTVT_140528#body_standalone_19 (Loại: `body_standalone`)
> **[Điều 4]`<DIEU>`** . **[2 . Tai nạn hàng hải nghiêm trọng là tai nạn hàng hải không thuộc các trường hợp **[quy định tại]`<TU_KHOA_PHAP_LY>`** **[khoản 1 Điều này]`<THAM_CHIEU_PHAP_LY>`** và gây ra một trong các thiệt hại dưới đây :]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 4** → `DIEU` (span: `[0:2]`)
- `[e1]` **2 . Tai nạn hàng hải nghiêm trọng là tai nạn hàng hải không thuộc các trường hợp quy định tại khoản 1 Điều này và gây ra một trong các thiệt hại dưới đây :** → `KHOAN` (span: `[3:31]`)
- `[e2]` **khoản 1 Điều này** → `THAM_CHIEU_PHAP_LY` (span: `[17:21]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **quy định tại** → `TU_KHOA_PHAP_LY` (span: `[15:17]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 2 . Tai nạn hàng hải nghiêm trọng là tai nạn hàng hải không thuộc các trường hợp quy định tại khoản 1 Điều này và gây ra một trong các thiệt hại dưới đây : `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 4 `[DIEU]`)
- (`e3` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e2` khoản 1 Điều này `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 2 . Tai nạn hàng hải nghiêm trọng là tai nạn hàng hải không thuộc các trường hợp quy định tại khoản 1 Điều này và gây ra một trong các thiệt hại dưới đây : `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e2` khoản 1 Điều này `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #01_2020_TT-BGTVT_140528#body_context_20 (Loại: `body_context`)
> **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[01/2020/TT-BGTVT]`<SO_HIEU>`** . **[Điều 4]`<DIEU>`** . **[3 . Tai nạn hàng hải ít nghiêm trọng là sự cố hàng hải hoặc tai nạn hàng hải xảy ra ngoài các trường hợp **[quy định tại]`<TU_KHOA_PHAP_LY>`** **[khoản 1 và khoản 2 Điều này]`<THAM_CHIEU_PHAP_LY>`** .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[4:5]`)
- `[e1]` **01/2020/TT-BGTVT** → `SO_HIEU` (span: `[6:7]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[0:3]`)
- `[e3]` **Điều 4** → `DIEU` (span: `[8:10]`)
- `[e4]` **3 . Tai nạn hàng hải ít nghiêm trọng là sự cố hàng hải hoặc tai nạn hàng hải xảy ra ngoài các trường hợp quy định tại khoản 1 và khoản 2 Điều này .** → `KHOAN` (span: `[11:38]`)
- `[e5]` **khoản 1 và khoản 2 Điều này** → `THAM_CHIEU_PHAP_LY` (span: `[30:37]`) *(lồng trong `e4` (`KHOAN`))*
- `[e6]` **quy định tại** → `TU_KHOA_PHAP_LY` (span: `[28:30]`) *(lồng trong `e4` (`KHOAN`))*

**Quan hệ:**
- (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 4 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`)
- (`e4` 3 . Tai nạn hàng hải ít nghiêm trọng là sự cố hàng hải hoặc tai nạn hàng hải xảy ra ngoài các trường hợp quy định tại khoản 1 và khoản 2 Điều này . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 4 `[DIEU]`)
- (`e6` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e5` khoản 1 và khoản 2 Điều này `[THAM_CHIEU_PHAP_LY]`)
- (`e4` 3 . Tai nạn hàng hải ít nghiêm trọng là sự cố hàng hải hoặc tai nạn hàng hải xảy ra ngoài các trường hợp quy định tại khoản 1 và khoản 2 Điều này . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e5` khoản 1 và khoản 2 Điều này `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #01_2020_TT-BGTVT_140528#body_standalone_21 (Loại: `body_standalone`)
> **[Điều 4]`<DIEU>`** . **[3 . Tai nạn hàng hải ít nghiêm trọng là sự cố hàng hải hoặc tai nạn hàng hải xảy ra ngoài các trường hợp **[quy định tại]`<TU_KHOA_PHAP_LY>`** **[khoản 1 và khoản 2 Điều này]`<THAM_CHIEU_PHAP_LY>`** .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 4** → `DIEU` (span: `[0:2]`)
- `[e1]` **3 . Tai nạn hàng hải ít nghiêm trọng là sự cố hàng hải hoặc tai nạn hàng hải xảy ra ngoài các trường hợp quy định tại khoản 1 và khoản 2 Điều này .** → `KHOAN` (span: `[3:30]`)
- `[e2]` **khoản 1 và khoản 2 Điều này** → `THAM_CHIEU_PHAP_LY` (span: `[22:29]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **quy định tại** → `TU_KHOA_PHAP_LY` (span: `[20:22]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 3 . Tai nạn hàng hải ít nghiêm trọng là sự cố hàng hải hoặc tai nạn hàng hải xảy ra ngoài các trường hợp quy định tại khoản 1 và khoản 2 Điều này . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 4 `[DIEU]`)
- (`e3` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e2` khoản 1 và khoản 2 Điều này `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 3 . Tai nạn hàng hải ít nghiêm trọng là sự cố hàng hải hoặc tai nạn hàng hải xảy ra ngoài các trường hợp quy định tại khoản 1 và khoản 2 Điều này . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e2` khoản 1 và khoản 2 Điều này `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #01_2020_TT-BGTVT_140528#body_context_22 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[01/2020/TT-BGTVT]`<SO_HIEU>`** ban hành **[ngày 20 tháng 01 năm 2020]`<NGAY_BAN_HANH>`** bởi **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** . **[Điều 5]`<DIEU>`** . **[1 . Thuyền trưởng , chủ tàu , người quản lý tàu , người khai thác tàu và các tổ chức , cá nhân liên quan tới tai nạn hàng hải có trách nhiệm báo cáo tai nạn hàng hải cho **[Cảng vụ hàng hải]`<CO_QUAN_THAM_QUYEN>`** hoặc Cục Hàng hải Việt Nam hoặc **[Bộ Giao thông vận tải]`<CO_QUAN_THAM_QUYEN>`** nhanh chóng , chính xác **[theo quy định tại]`<TU_KHOA_PHAP_LY>`** **[Thông tư này]`<THAM_CHIEU_PHAP_LY>`** .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **01/2020/TT-BGTVT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[11:14]`)
- `[e3]` **ngày 20 tháng 01 năm 2020** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 5** → `DIEU` (span: `[15:17]`)
- `[e5]` **1 . Thuyền trưởng , chủ tàu , người quản lý tàu , người khai thác tàu và các tổ chức , cá nhân liên quan tới tai nạn hàng hải có trách nhiệm báo cáo tai nạn hàng hải cho Cảng vụ hàng hải hoặc Cục Hàng hải Việt Nam hoặc Bộ Giao thông vận tải nhanh chóng , chính xác theo quy định tại Thông tư này .** → `KHOAN` (span: `[18:66]`)
- `[e6]` **Thông tư này** → `THAM_CHIEU_PHAP_LY` (span: `[63:65]`) *(lồng trong `e5` (`KHOAN`))*
- `[e7]` **theo quy định tại** → `TU_KHOA_PHAP_LY` (span: `[60:63]`) *(lồng trong `e5` (`KHOAN`))*
- `[e8]` **Cảng vụ hàng hải** → `CO_QUAN_THAM_QUYEN` (span: `[47:49]`) *(lồng trong `e5` (`KHOAN`))*
- `[e9]` **Bộ Giao thông vận tải** → `CO_QUAN_THAM_QUYEN` (span: `[54:57]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 20 tháng 01 năm 2020 `[NGAY_BAN_HANH]`)
- (`e4` Điều 5 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`)
- (`e5` 1 . Thuyền trưởng , chủ tàu , người quản lý tàu , người khai thác tàu và các tổ chức , cá nhân liên quan tới tai nạn hàng hải có trách nhiệm báo cáo tai nạn hàng hải cho Cảng vụ hàng hải hoặc Cục Hàng hải Việt Nam hoặc Bộ Giao thông vận tải nhanh chóng , chính xác theo quy định tại Thông tư này . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 5 `[DIEU]`)
- (`e7` theo quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e6` Thông tư này `[THAM_CHIEU_PHAP_LY]`)
- (`e5` 1 . Thuyền trưởng , chủ tàu , người quản lý tàu , người khai thác tàu và các tổ chức , cá nhân liên quan tới tai nạn hàng hải có trách nhiệm báo cáo tai nạn hàng hải cho Cảng vụ hàng hải hoặc Cục Hàng hải Việt Nam hoặc Bộ Giao thông vận tải nhanh chóng , chính xác theo quy định tại Thông tư này . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e6` Thông tư này `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #01_2020_TT-BGTVT_140528#body_standalone_23 (Loại: `body_standalone`)
> **[Điều 5]`<DIEU>`** . **[1 . Thuyền trưởng , chủ tàu , người quản lý tàu , người khai thác tàu và các tổ chức , cá nhân liên quan tới tai nạn hàng hải có trách nhiệm báo cáo tai nạn hàng hải cho **[Cảng vụ hàng hải]`<CO_QUAN_THAM_QUYEN>`** hoặc Cục Hàng hải Việt Nam hoặc **[Bộ Giao thông vận tải]`<CO_QUAN_THAM_QUYEN>`** nhanh chóng , chính xác **[theo quy định tại]`<TU_KHOA_PHAP_LY>`** **[Thông tư này]`<THAM_CHIEU_PHAP_LY>`** .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 5** → `DIEU` (span: `[0:2]`)
- `[e1]` **1 . Thuyền trưởng , chủ tàu , người quản lý tàu , người khai thác tàu và các tổ chức , cá nhân liên quan tới tai nạn hàng hải có trách nhiệm báo cáo tai nạn hàng hải cho Cảng vụ hàng hải hoặc Cục Hàng hải Việt Nam hoặc Bộ Giao thông vận tải nhanh chóng , chính xác theo quy định tại Thông tư này .** → `KHOAN` (span: `[3:51]`)
- `[e2]` **Thông tư này** → `THAM_CHIEU_PHAP_LY` (span: `[48:50]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **theo quy định tại** → `TU_KHOA_PHAP_LY` (span: `[45:48]`) *(lồng trong `e1` (`KHOAN`))*
- `[e4]` **Cảng vụ hàng hải** → `CO_QUAN_THAM_QUYEN` (span: `[32:34]`) *(lồng trong `e1` (`KHOAN`))*
- `[e5]` **Bộ Giao thông vận tải** → `CO_QUAN_THAM_QUYEN` (span: `[39:42]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 1 . Thuyền trưởng , chủ tàu , người quản lý tàu , người khai thác tàu và các tổ chức , cá nhân liên quan tới tai nạn hàng hải có trách nhiệm báo cáo tai nạn hàng hải cho Cảng vụ hàng hải hoặc Cục Hàng hải Việt Nam hoặc Bộ Giao thông vận tải nhanh chóng , chính xác theo quy định tại Thông tư này . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 5 `[DIEU]`)
- (`e3` theo quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e2` Thông tư này `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 1 . Thuyền trưởng , chủ tàu , người quản lý tàu , người khai thác tàu và các tổ chức , cá nhân liên quan tới tai nạn hàng hải có trách nhiệm báo cáo tai nạn hàng hải cho Cảng vụ hàng hải hoặc Cục Hàng hải Việt Nam hoặc Bộ Giao thông vận tải nhanh chóng , chính xác theo quy định tại Thông tư này . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e2` Thông tư này `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #01_2020_TT-BGTVT_140528#body_context_24 (Loại: `body_context`)
> **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[01/2020/TT-BGTVT]`<SO_HIEU>`** . **[Điều 5]`<DIEU>`** . **[3 . Thuyền trưởng , thuyền viên của **[tàu biển]`<TAI_SAN_VAT_CHAT>`** liên quan tới tai nạn hàng hải có trách nhiệm tổ chức bảo vệ hiện trường tai nạn và thiết bị ghi dữ liệu hành trình tại thời điểm xảy ra tai nạn hàng hải và cung cấp các chứng cứ liên quan đến tai nạn hàng hải cho **[cơ quan điều tra]`<CO_QUAN_THAM_QUYEN>`** .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[4:5]`)
- `[e1]` **01/2020/TT-BGTVT** → `SO_HIEU` (span: `[6:7]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[0:3]`)
- `[e3]` **Điều 5** → `DIEU` (span: `[8:10]`)
- `[e4]` **3 . Thuyền trưởng , thuyền viên của tàu biển liên quan tới tai nạn hàng hải có trách nhiệm tổ chức bảo vệ hiện trường tai nạn và thiết bị ghi dữ liệu hành trình tại thời điểm xảy ra tai nạn hàng hải và cung cấp các chứng cứ liên quan đến tai nạn hàng hải cho cơ quan điều tra .** → `KHOAN` (span: `[11:51]`)
- `[e5]` **cơ quan điều tra** → `CO_QUAN_THAM_QUYEN` (span: `[48:50]`) *(lồng trong `e4` (`KHOAN`))*
- `[e6]` **tàu biển** → `TAI_SAN_VAT_CHAT` (span: `[17:18]`) *(lồng trong `e4` (`KHOAN`))*

**Quan hệ:**
- (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 5 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`)
- (`e4` 3 . Thuyền trưởng , thuyền viên của tàu biển liên quan tới tai nạn hàng hải có trách nhiệm tổ chức bảo vệ hiện trường tai nạn và thiết bị ghi dữ liệu hành trình tại thời điểm xảy ra tai nạn hàng hải và cung cấp các chứng cứ liên quan đến tai nạn hàng hải cho cơ quan điều tra . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 5 `[DIEU]`)


---

### Mẫu #01_2020_TT-BGTVT_140528#body_standalone_25 (Loại: `body_standalone`)
> **[Điều 5]`<DIEU>`** . **[3 . Thuyền trưởng , thuyền viên của **[tàu biển]`<TAI_SAN_VAT_CHAT>`** liên quan tới tai nạn hàng hải có trách nhiệm tổ chức bảo vệ hiện trường tai nạn và thiết bị ghi dữ liệu hành trình tại thời điểm xảy ra tai nạn hàng hải và cung cấp các chứng cứ liên quan đến tai nạn hàng hải cho **[cơ quan điều tra]`<CO_QUAN_THAM_QUYEN>`** .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 5** → `DIEU` (span: `[0:2]`)
- `[e1]` **3 . Thuyền trưởng , thuyền viên của tàu biển liên quan tới tai nạn hàng hải có trách nhiệm tổ chức bảo vệ hiện trường tai nạn và thiết bị ghi dữ liệu hành trình tại thời điểm xảy ra tai nạn hàng hải và cung cấp các chứng cứ liên quan đến tai nạn hàng hải cho cơ quan điều tra .** → `KHOAN` (span: `[3:43]`)
- `[e2]` **cơ quan điều tra** → `CO_QUAN_THAM_QUYEN` (span: `[40:42]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **tàu biển** → `TAI_SAN_VAT_CHAT` (span: `[9:10]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 3 . Thuyền trưởng , thuyền viên của tàu biển liên quan tới tai nạn hàng hải có trách nhiệm tổ chức bảo vệ hiện trường tai nạn và thiết bị ghi dữ liệu hành trình tại thời điểm xảy ra tai nạn hàng hải và cung cấp các chứng cứ liên quan đến tai nạn hàng hải cho cơ quan điều tra . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 5 `[DIEU]`)


---

### Mẫu #01_2020_TT-BGTVT_140528#body_context_26 (Loại: `body_context`)
> **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[01/2020/TT-BGTVT]`<SO_HIEU>`** . **[Điều 5]`<DIEU>`** . **[4 . Thuyền trưởng , thuyền viên của **[tàu biển]`<TAI_SAN_VAT_CHAT>`** và các tổ chức , cá nhân liên quan tới tai nạn hàng hải có trách nhiệm cung cấp thông tin đầy đủ , trung thực và kịp thời cho **[cơ quan điều tra]`<CO_QUAN_THAM_QUYEN>`** và hoàn toàn chịu trách nhiệm trước pháp luật về những thông tin cung cấp .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[4:5]`)
- `[e1]` **01/2020/TT-BGTVT** → `SO_HIEU` (span: `[6:7]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[0:3]`)
- `[e3]` **Điều 5** → `DIEU` (span: `[8:10]`)
- `[e4]` **4 . Thuyền trưởng , thuyền viên của tàu biển và các tổ chức , cá nhân liên quan tới tai nạn hàng hải có trách nhiệm cung cấp thông tin đầy đủ , trung thực và kịp thời cho cơ quan điều tra và hoàn toàn chịu trách nhiệm trước pháp luật về những thông tin cung cấp .** → `KHOAN` (span: `[11:50]`)
- `[e5]` **cơ quan điều tra** → `CO_QUAN_THAM_QUYEN` (span: `[37:39]`) *(lồng trong `e4` (`KHOAN`))*
- `[e6]` **tàu biển** → `TAI_SAN_VAT_CHAT` (span: `[17:18]`) *(lồng trong `e4` (`KHOAN`))*

**Quan hệ:**
- (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 5 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`)
- (`e4` 4 . Thuyền trưởng , thuyền viên của tàu biển và các tổ chức , cá nhân liên quan tới tai nạn hàng hải có trách nhiệm cung cấp thông tin đầy đủ , trung thực và kịp thời cho cơ quan điều tra và hoàn toàn chịu trách nhiệm trước pháp luật về những thông tin cung cấp . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 5 `[DIEU]`)


---

### Mẫu #01_2020_TT-BGTVT_140528#body_standalone_27 (Loại: `body_standalone`)
> **[Điều 5]`<DIEU>`** . **[4 . Thuyền trưởng , thuyền viên của **[tàu biển]`<TAI_SAN_VAT_CHAT>`** và các tổ chức , cá nhân liên quan tới tai nạn hàng hải có trách nhiệm cung cấp thông tin đầy đủ , trung thực và kịp thời cho **[cơ quan điều tra]`<CO_QUAN_THAM_QUYEN>`** và hoàn toàn chịu trách nhiệm trước pháp luật về những thông tin cung cấp .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 5** → `DIEU` (span: `[0:2]`)
- `[e1]` **4 . Thuyền trưởng , thuyền viên của tàu biển và các tổ chức , cá nhân liên quan tới tai nạn hàng hải có trách nhiệm cung cấp thông tin đầy đủ , trung thực và kịp thời cho cơ quan điều tra và hoàn toàn chịu trách nhiệm trước pháp luật về những thông tin cung cấp .** → `KHOAN` (span: `[3:42]`)
- `[e2]` **cơ quan điều tra** → `CO_QUAN_THAM_QUYEN` (span: `[29:31]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **tàu biển** → `TAI_SAN_VAT_CHAT` (span: `[9:10]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 4 . Thuyền trưởng , thuyền viên của tàu biển và các tổ chức , cá nhân liên quan tới tai nạn hàng hải có trách nhiệm cung cấp thông tin đầy đủ , trung thực và kịp thời cho cơ quan điều tra và hoàn toàn chịu trách nhiệm trước pháp luật về những thông tin cung cấp . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 5 `[DIEU]`)


---

### Mẫu #01_2020_TT-BGTVT_140528#body_context_28 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[01/2020/TT-BGTVT]`<SO_HIEU>`** của **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Hàng hải]`<LINH_VUC>`** . **[Điều 5]`<DIEU>`** . **[5 . Đối với tai nạn hàng hải gây tổn thất về thân thể thuyền viên thì thuyền trưởng , chủ tàu , **[người sử dụng lao động]`<CHU_THE_CA_NHAN>`** , ngoài nghĩa vụ báo cáo theo quy định của Thông tư này , phải thực hiện việc khai báo tai nạn lao động hàng hải theo quy định pháp luật .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **01/2020/TT-BGTVT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[4:7]`)
- `[e3]` **Hàng hải** → `LINH_VUC` (span: `[9:10]`)
- `[e4]` **Điều 5** → `DIEU` (span: `[11:13]`)
- `[e5]` **5 . Đối với tai nạn hàng hải gây tổn thất về thân thể thuyền viên thì thuyền trưởng , chủ tàu , người sử dụng lao động , ngoài nghĩa vụ báo cáo theo quy định của Thông tư này , phải thực hiện việc khai báo tai nạn lao động hàng hải theo quy định pháp luật .** → `KHOAN` (span: `[14:54]`)
- `[e6]` **người sử dụng lao động** → `CHU_THE_CA_NHAN` (span: `[30:33]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Hàng hải `[LINH_VUC]`)
- (`e4` Điều 5 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`)
- (`e5` 5 . Đối với tai nạn hàng hải gây tổn thất về thân thể thuyền viên thì thuyền trưởng , chủ tàu , người sử dụng lao động , ngoài nghĩa vụ báo cáo theo quy định của Thông tư này , phải thực hiện việc khai báo tai nạn lao động hàng hải theo quy định pháp luật . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 5 `[DIEU]`)
- (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Hàng hải `[LINH_VUC]`)
- (`e5` 5 . Đối với tai nạn hàng hải gây tổn thất về thân thể thuyền viên thì thuyền trưởng , chủ tàu , người sử dụng lao động , ngoài nghĩa vụ báo cáo theo quy định của Thông tư này , phải thực hiện việc khai báo tai nạn lao động hàng hải theo quy định pháp luật . `[KHOAN]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Hàng hải `[LINH_VUC]`)


---

### Mẫu #01_2020_TT-BGTVT_140528#body_context_29 (Loại: `body_context`)
> **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[01/2020/TT-BGTVT]`<SO_HIEU>`** . **[Điều 6]`<DIEU>`** . **[1 . Báo cáo tai nạn hàng hải bao gồm Báo cáo khẩn , Báo cáo chi tiết , Báo cáo định kỳ **[theo quy định tại]`<TU_KHOA_PHAP_LY>`** các **[Phụ lục 1]`<THAM_CHIEU_PHAP_LY>`** , 2 và 3 ban hành kèm theo Thông tư này .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[4:5]`)
- `[e1]` **01/2020/TT-BGTVT** → `SO_HIEU` (span: `[6:7]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[0:3]`)
- `[e3]` **Điều 6** → `DIEU` (span: `[8:10]`)
- `[e4]` **1 . Báo cáo tai nạn hàng hải bao gồm Báo cáo khẩn , Báo cáo chi tiết , Báo cáo định kỳ theo quy định tại các Phụ lục 1 , 2 và 3 ban hành kèm theo Thông tư này .** → `KHOAN` (span: `[11:41]`)
- `[e5]` **Phụ lục 1** → `THAM_CHIEU_PHAP_LY` (span: `[29:31]`) *(lồng trong `e4` (`KHOAN`))*
- `[e6]` **theo quy định tại** → `TU_KHOA_PHAP_LY` (span: `[25:28]`) *(lồng trong `e4` (`KHOAN`))*

**Quan hệ:**
- (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 6 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`)
- (`e4` 1 . Báo cáo tai nạn hàng hải bao gồm Báo cáo khẩn , Báo cáo chi tiết , Báo cáo định kỳ theo quy định tại các Phụ lục 1 , 2 và 3 ban hành kèm theo Thông tư này . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 6 `[DIEU]`)
- (`e6` theo quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e5` Phụ lục 1 `[THAM_CHIEU_PHAP_LY]`)
- (`e4` 1 . Báo cáo tai nạn hàng hải bao gồm Báo cáo khẩn , Báo cáo chi tiết , Báo cáo định kỳ theo quy định tại các Phụ lục 1 , 2 và 3 ban hành kèm theo Thông tư này . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e5` Phụ lục 1 `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #01_2020_TT-BGTVT_140528#body_standalone_30 (Loại: `body_standalone`)
> **[Điều 6]`<DIEU>`** . **[1 . Báo cáo tai nạn hàng hải bao gồm Báo cáo khẩn , Báo cáo chi tiết , Báo cáo định kỳ **[theo quy định tại]`<TU_KHOA_PHAP_LY>`** các **[Phụ lục 1]`<THAM_CHIEU_PHAP_LY>`** , 2 và 3 ban hành kèm theo Thông tư này .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 6** → `DIEU` (span: `[0:2]`)
- `[e1]` **1 . Báo cáo tai nạn hàng hải bao gồm Báo cáo khẩn , Báo cáo chi tiết , Báo cáo định kỳ theo quy định tại các Phụ lục 1 , 2 và 3 ban hành kèm theo Thông tư này .** → `KHOAN` (span: `[3:33]`)
- `[e2]` **Phụ lục 1** → `THAM_CHIEU_PHAP_LY` (span: `[21:23]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **theo quy định tại** → `TU_KHOA_PHAP_LY` (span: `[17:20]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 1 . Báo cáo tai nạn hàng hải bao gồm Báo cáo khẩn , Báo cáo chi tiết , Báo cáo định kỳ theo quy định tại các Phụ lục 1 , 2 và 3 ban hành kèm theo Thông tư này . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 6 `[DIEU]`)
- (`e3` theo quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e2` Phụ lục 1 `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 1 . Báo cáo tai nạn hàng hải bao gồm Báo cáo khẩn , Báo cáo chi tiết , Báo cáo định kỳ theo quy định tại các Phụ lục 1 , 2 và 3 ban hành kèm theo Thông tư này . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e2` Phụ lục 1 `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #01_2020_TT-BGTVT_140528#body_context_31 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[01/2020/TT-BGTVT]`<SO_HIEU>`** ban hành **[ngày 20 tháng 01 năm 2020]`<NGAY_BAN_HANH>`** bởi **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** . **[Điều 7]`<DIEU>`** . **[Khoản 1]`<KHOAN>`** . **[a ) Trong trường hợp tai nạn hàng hải xảy ra trong vùng nước cảng biển và vùng biển Việt Nam , thuyền trưởng hoặc người có trách nhiệm cao nhất trên **[tàu biển]`<TAI_SAN_VAT_CHAT>`** phải gửi ngay Báo cáo khẩn cho **[Cảng vụ hàng hải]`<CO_QUAN_THAM_QUYEN>`** nơi gần nhất . Trường hợp những người này không thực hiện được Báo cáo khẩn thì chủ tàu hoặc đại lý **[tàu biển]`<TAI_SAN_VAT_CHAT>`** liên quan đến tai nạn có trách nhiệm báo cáo .]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **01/2020/TT-BGTVT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[11:14]`)
- `[e3]` **ngày 20 tháng 01 năm 2020** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 7** → `DIEU` (span: `[15:17]`)
- `[e5]` **Khoản 1** → `KHOAN` (span: `[18:20]`)
- `[e6]` **a ) Trong trường hợp tai nạn hàng hải xảy ra trong vùng nước cảng biển và vùng biển Việt Nam , thuyền trưởng hoặc người có trách nhiệm cao nhất trên tàu biển phải gửi ngay Báo cáo khẩn cho Cảng vụ hàng hải nơi gần nhất . Trường hợp những người này không thực hiện được Báo cáo khẩn thì chủ tàu hoặc đại lý tàu biển liên quan đến tai nạn có trách nhiệm báo cáo .** → `DIEM` (span: `[21:81]`)
- `[e7]` **Cảng vụ hàng hải** → `CO_QUAN_THAM_QUYEN` (span: `[53:55]`) *(lồng trong `e6` (`DIEM`))*
- `[e8]` **tàu biển** → `TAI_SAN_VAT_CHAT` (span: `[46:47]`) *(lồng trong `e6` (`DIEM`))*
- `[e9]` **tàu biển** → `TAI_SAN_VAT_CHAT` (span: `[73:74]`) *(lồng trong `e6` (`DIEM`))*

**Quan hệ:**
- (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 20 tháng 01 năm 2020 `[NGAY_BAN_HANH]`)
- (`e4` Điều 7 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`)
- (`e5` Khoản 1 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 7 `[DIEU]`)
- (`e6` a ) Trong trường hợp tai nạn hàng hải xảy ra trong vùng nước cảng biển và vùng biển Việt Nam , thuyền trưởng hoặc người có trách nhiệm cao nhất trên tàu biển phải gửi ngay Báo cáo khẩn cho Cảng vụ hàng hải nơi gần nhất . Trường hợp những người này không thực hiện được Báo cáo khẩn thì chủ tàu hoặc đại lý tàu biển liên quan đến tai nạn có trách nhiệm báo cáo . `[DIEM]`) ==[ **THUOC_VE** ]==> (`e5` Khoản 1 `[KHOAN]`)


---

### Mẫu #01_2020_TT-BGTVT_140528#body_standalone_32 (Loại: `body_standalone`)
> **[Điều 7]`<DIEU>`** . **[Khoản 1]`<KHOAN>`** . **[a ) Trong trường hợp tai nạn hàng hải xảy ra trong vùng nước cảng biển và vùng biển Việt Nam , thuyền trưởng hoặc người có trách nhiệm cao nhất trên **[tàu biển]`<TAI_SAN_VAT_CHAT>`** phải gửi ngay Báo cáo khẩn cho **[Cảng vụ hàng hải]`<CO_QUAN_THAM_QUYEN>`** nơi gần nhất . Trường hợp những người này không thực hiện được Báo cáo khẩn thì chủ tàu hoặc đại lý **[tàu biển]`<TAI_SAN_VAT_CHAT>`** liên quan đến tai nạn có trách nhiệm báo cáo .]`<DIEM>`**

**Thực thể:**
- `[e0]` **Điều 7** → `DIEU` (span: `[0:2]`)
- `[e1]` **Khoản 1** → `KHOAN` (span: `[3:5]`)
- `[e2]` **a ) Trong trường hợp tai nạn hàng hải xảy ra trong vùng nước cảng biển và vùng biển Việt Nam , thuyền trưởng hoặc người có trách nhiệm cao nhất trên tàu biển phải gửi ngay Báo cáo khẩn cho Cảng vụ hàng hải nơi gần nhất . Trường hợp những người này không thực hiện được Báo cáo khẩn thì chủ tàu hoặc đại lý tàu biển liên quan đến tai nạn có trách nhiệm báo cáo .** → `DIEM` (span: `[6:66]`)
- `[e3]` **Cảng vụ hàng hải** → `CO_QUAN_THAM_QUYEN` (span: `[38:40]`) *(lồng trong `e2` (`DIEM`))*
- `[e4]` **tàu biển** → `TAI_SAN_VAT_CHAT` (span: `[31:32]`) *(lồng trong `e2` (`DIEM`))*
- `[e5]` **tàu biển** → `TAI_SAN_VAT_CHAT` (span: `[58:59]`) *(lồng trong `e2` (`DIEM`))*

**Quan hệ:**
- (`e1` Khoản 1 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 7 `[DIEU]`)
- (`e2` a ) Trong trường hợp tai nạn hàng hải xảy ra trong vùng nước cảng biển và vùng biển Việt Nam , thuyền trưởng hoặc người có trách nhiệm cao nhất trên tàu biển phải gửi ngay Báo cáo khẩn cho Cảng vụ hàng hải nơi gần nhất . Trường hợp những người này không thực hiện được Báo cáo khẩn thì chủ tàu hoặc đại lý tàu biển liên quan đến tai nạn có trách nhiệm báo cáo . `[DIEM]`) ==[ **THUOC_VE** ]==> (`e1` Khoản 1 `[KHOAN]`)


---

### Mẫu #01_2020_TT-BGTVT_140528#body_context_33 (Loại: `body_context`)
> **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[01/2020/TT-BGTVT]`<SO_HIEU>`** . **[Điều 7]`<DIEU>`** . **[Khoản 1]`<KHOAN>`** . **[b ) **[Cảng vụ hàng hải]`<CO_QUAN_THAM_QUYEN>`** nơi gần nhất khi nhận được Báo cáo khẩn hoặc biết tin về tai nạn hàng hải xảy ra có trách nhiệm chuyển ngay Báo cáo khẩn hoặc các thông tin đó cho các cơ quan , tổ chức sau đây : **[Cảng vụ hàng hải]`<CO_QUAN_THAM_QUYEN>`** được giao quản lý khu vực tàu xảy ra tai nạn ; Cục Hàng hải Việt Nam ; Tổng **[Công ty Bảo đảm an toàn hàng hải]`<TO_CHUC_DOANH_NGHIEP>`** , nếu tai nạn gây hư hỏng , làm mất tác dụng các thiết bị trợ giúp]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[4:5]`)
- `[e1]` **01/2020/TT-BGTVT** → `SO_HIEU` (span: `[6:7]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[0:3]`)
- `[e3]` **Điều 7** → `DIEU` (span: `[8:10]`)
- `[e4]` **Khoản 1** → `KHOAN` (span: `[11:13]`)
- `[e5]` **b ) Cảng vụ hàng hải nơi gần nhất khi nhận được Báo cáo khẩn hoặc biết tin về tai nạn hàng hải xảy ra có trách nhiệm chuyển ngay Báo cáo khẩn hoặc các thông tin đó cho các cơ quan , tổ chức sau đây : Cảng vụ hàng hải được giao quản lý khu vực tàu xảy ra tai nạn ; Cục Hàng hải Việt Nam ; Tổng Công ty Bảo đảm an toàn hàng hải , nếu tai nạn gây hư hỏng , làm mất tác dụng các thiết bị trợ giúp** → `DIEM` (span: `[14:84]`)
- `[e6]` **Cảng vụ hàng hải** → `CO_QUAN_THAM_QUYEN` (span: `[16:18]`) *(lồng trong `e5` (`DIEM`))*
- `[e7]` **Cảng vụ hàng hải** → `CO_QUAN_THAM_QUYEN` (span: `[52:54]`) *(lồng trong `e5` (`DIEM`))*
- `[e8]` **Công ty Bảo đảm an toàn hàng hải** → `TO_CHUC_DOANH_NGHIEP` (span: `[68:72]`) *(lồng trong `e5` (`DIEM`))*

**Quan hệ:**
- (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 7 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`)
- (`e4` Khoản 1 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 7 `[DIEU]`)
- (`e5` b ) Cảng vụ hàng hải nơi gần nhất khi nhận được Báo cáo khẩn hoặc biết tin về tai nạn hàng hải xảy ra có trách nhiệm chuyển ngay Báo cáo khẩn hoặc các thông tin đó cho các cơ quan , tổ chức sau đây : Cảng vụ hàng hải được giao quản lý khu vực tàu xảy ra tai nạn ; Cục Hàng hải Việt Nam ; Tổng Công ty Bảo đảm an toàn hàng hải , nếu tai nạn gây hư hỏng , làm mất tác dụng các thiết bị trợ giúp `[DIEM]`) ==[ **THUOC_VE** ]==> (`e4` Khoản 1 `[KHOAN]`)


---

### Mẫu #01_2020_TT-BGTVT_140528#body_standalone_34 (Loại: `body_standalone`)
> **[Điều 7]`<DIEU>`** . **[Khoản 1]`<KHOAN>`** . **[b ) **[Cảng vụ hàng hải]`<CO_QUAN_THAM_QUYEN>`** nơi gần nhất khi nhận được Báo cáo khẩn hoặc biết tin về tai nạn hàng hải xảy ra có trách nhiệm chuyển ngay Báo cáo khẩn hoặc các thông tin đó cho các cơ quan , tổ chức sau đây : **[Cảng vụ hàng hải]`<CO_QUAN_THAM_QUYEN>`** được giao quản lý khu vực tàu xảy ra tai nạn ; Cục Hàng hải Việt Nam ; Tổng **[Công ty Bảo đảm an toàn hàng hải]`<TO_CHUC_DOANH_NGHIEP>`** , nếu tai nạn gây hư hỏng , làm mất tác dụng các thiết bị trợ giúp]`<DIEM>`**

**Thực thể:**
- `[e0]` **Điều 7** → `DIEU` (span: `[0:2]`)
- `[e1]` **Khoản 1** → `KHOAN` (span: `[3:5]`)
- `[e2]` **b ) Cảng vụ hàng hải nơi gần nhất khi nhận được Báo cáo khẩn hoặc biết tin về tai nạn hàng hải xảy ra có trách nhiệm chuyển ngay Báo cáo khẩn hoặc các thông tin đó cho các cơ quan , tổ chức sau đây : Cảng vụ hàng hải được giao quản lý khu vực tàu xảy ra tai nạn ; Cục Hàng hải Việt Nam ; Tổng Công ty Bảo đảm an toàn hàng hải , nếu tai nạn gây hư hỏng , làm mất tác dụng các thiết bị trợ giúp** → `DIEM` (span: `[6:76]`)
- `[e3]` **Cảng vụ hàng hải** → `CO_QUAN_THAM_QUYEN` (span: `[8:10]`) *(lồng trong `e2` (`DIEM`))*
- `[e4]` **Cảng vụ hàng hải** → `CO_QUAN_THAM_QUYEN` (span: `[44:46]`) *(lồng trong `e2` (`DIEM`))*
- `[e5]` **Công ty Bảo đảm an toàn hàng hải** → `TO_CHUC_DOANH_NGHIEP` (span: `[60:64]`) *(lồng trong `e2` (`DIEM`))*

**Quan hệ:**
- (`e1` Khoản 1 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 7 `[DIEU]`)
- (`e2` b ) Cảng vụ hàng hải nơi gần nhất khi nhận được Báo cáo khẩn hoặc biết tin về tai nạn hàng hải xảy ra có trách nhiệm chuyển ngay Báo cáo khẩn hoặc các thông tin đó cho các cơ quan , tổ chức sau đây : Cảng vụ hàng hải được giao quản lý khu vực tàu xảy ra tai nạn ; Cục Hàng hải Việt Nam ; Tổng Công ty Bảo đảm an toàn hàng hải , nếu tai nạn gây hư hỏng , làm mất tác dụng các thiết bị trợ giúp `[DIEM]`) ==[ **THUOC_VE** ]==> (`e1` Khoản 1 `[KHOAN]`)


---

### Mẫu #01_2020_TT-BGTVT_140528#body_context_35 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[01/2020/TT-BGTVT]`<SO_HIEU>`** ban hành **[ngày 20 tháng 01 năm 2020]`<NGAY_BAN_HANH>`** bởi **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** . **[Điều 7]`<DIEU>`** . **[2 . Trường hợp tai nạn hàng hải liên quan đến **[tàu biển]`<TAI_SAN_VAT_CHAT>`** Việt Nam khi hoạt động trong vùng biển của quốc gia khác , thuyền trưởng hoặc người có trách nhiệm cao nhất trên **[tàu biển]`<TAI_SAN_VAT_CHAT>`** hoặc chủ tàu phải báo cáo theo yêu cầu của quốc gia ven biển nơi tàu bị tai nạn và gửi ngay Báo cáo khẩn cho Cục Hàng hải Việt Nam . Nếu tai nạn thuộc loại đặc biệt nghiêm trọng , thuyền trưởng hoặc người có trách nhiệm cao nhất trên **[tàu biển]`<TAI_SAN_VAT_CHAT>`** hoặc chủ tàu phải]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **01/2020/TT-BGTVT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[11:14]`)
- `[e3]` **ngày 20 tháng 01 năm 2020** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 7** → `DIEU` (span: `[15:17]`)
- `[e5]` **2 . Trường hợp tai nạn hàng hải liên quan đến tàu biển Việt Nam khi hoạt động trong vùng biển của quốc gia khác , thuyền trưởng hoặc người có trách nhiệm cao nhất trên tàu biển hoặc chủ tàu phải báo cáo theo yêu cầu của quốc gia ven biển nơi tàu bị tai nạn và gửi ngay Báo cáo khẩn cho Cục Hàng hải Việt Nam . Nếu tai nạn thuộc loại đặc biệt nghiêm trọng , thuyền trưởng hoặc người có trách nhiệm cao nhất trên tàu biển hoặc chủ tàu phải** → `KHOAN` (span: `[18:89]`)
- `[e6]` **tàu biển** → `TAI_SAN_VAT_CHAT` (span: `[25:26]`) *(lồng trong `e5` (`KHOAN`))*
- `[e7]` **tàu biển** → `TAI_SAN_VAT_CHAT` (span: `[43:44]`) *(lồng trong `e5` (`KHOAN`))*
- `[e8]` **tàu biển** → `TAI_SAN_VAT_CHAT` (span: `[84:85]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 20 tháng 01 năm 2020 `[NGAY_BAN_HANH]`)
- (`e4` Điều 7 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`)
- (`e5` 2 . Trường hợp tai nạn hàng hải liên quan đến tàu biển Việt Nam khi hoạt động trong vùng biển của quốc gia khác , thuyền trưởng hoặc người có trách nhiệm cao nhất trên tàu biển hoặc chủ tàu phải báo cáo theo yêu cầu của quốc gia ven biển nơi tàu bị tai nạn và gửi ngay Báo cáo khẩn cho Cục Hàng hải Việt Nam . Nếu tai nạn thuộc loại đặc biệt nghiêm trọng , thuyền trưởng hoặc người có trách nhiệm cao nhất trên tàu biển hoặc chủ tàu phải `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 7 `[DIEU]`)


---

### Mẫu #01_2020_TT-BGTVT_140528#body_standalone_36 (Loại: `body_standalone`)
> **[Điều 7]`<DIEU>`** . **[2 . Trường hợp tai nạn hàng hải liên quan đến **[tàu biển]`<TAI_SAN_VAT_CHAT>`** Việt Nam khi hoạt động trong vùng biển của quốc gia khác , thuyền trưởng hoặc người có trách nhiệm cao nhất trên **[tàu biển]`<TAI_SAN_VAT_CHAT>`** hoặc chủ tàu phải báo cáo theo yêu cầu của quốc gia ven biển nơi tàu bị tai nạn và gửi ngay Báo cáo khẩn cho Cục Hàng hải Việt Nam . Nếu tai nạn thuộc loại đặc biệt nghiêm trọng , thuyền trưởng hoặc người có trách nhiệm cao nhất trên **[tàu biển]`<TAI_SAN_VAT_CHAT>`** hoặc chủ tàu phải]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 7** → `DIEU` (span: `[0:2]`)
- `[e1]` **2 . Trường hợp tai nạn hàng hải liên quan đến tàu biển Việt Nam khi hoạt động trong vùng biển của quốc gia khác , thuyền trưởng hoặc người có trách nhiệm cao nhất trên tàu biển hoặc chủ tàu phải báo cáo theo yêu cầu của quốc gia ven biển nơi tàu bị tai nạn và gửi ngay Báo cáo khẩn cho Cục Hàng hải Việt Nam . Nếu tai nạn thuộc loại đặc biệt nghiêm trọng , thuyền trưởng hoặc người có trách nhiệm cao nhất trên tàu biển hoặc chủ tàu phải** → `KHOAN` (span: `[3:74]`)
- `[e2]` **tàu biển** → `TAI_SAN_VAT_CHAT` (span: `[10:11]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **tàu biển** → `TAI_SAN_VAT_CHAT` (span: `[28:29]`) *(lồng trong `e1` (`KHOAN`))*
- `[e4]` **tàu biển** → `TAI_SAN_VAT_CHAT` (span: `[69:70]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 2 . Trường hợp tai nạn hàng hải liên quan đến tàu biển Việt Nam khi hoạt động trong vùng biển của quốc gia khác , thuyền trưởng hoặc người có trách nhiệm cao nhất trên tàu biển hoặc chủ tàu phải báo cáo theo yêu cầu của quốc gia ven biển nơi tàu bị tai nạn và gửi ngay Báo cáo khẩn cho Cục Hàng hải Việt Nam . Nếu tai nạn thuộc loại đặc biệt nghiêm trọng , thuyền trưởng hoặc người có trách nhiệm cao nhất trên tàu biển hoặc chủ tàu phải `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 7 `[DIEU]`)


---

### Mẫu #01_2020_TT-BGTVT_140528#body_context_37 (Loại: `body_context`)
> **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[01/2020/TT-BGTVT]`<SO_HIEU>`** . **[Điều 7]`<DIEU>`** . **[3 . Trường hợp tai nạn hàng hải liên quan đến **[tàu biển]`<TAI_SAN_VAT_CHAT>`** Việt Nam khi hoạt động ở vùng biển quốc tế , thuyền trưởng hoặc người có trách nhiệm cao nhất trên **[tàu biển]`<TAI_SAN_VAT_CHAT>`** hoặc chủ tàu phải gửi ngay Báo cáo khẩn cho Cục Hàng hải Việt Nam .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[4:5]`)
- `[e1]` **01/2020/TT-BGTVT** → `SO_HIEU` (span: `[6:7]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[0:3]`)
- `[e3]` **Điều 7** → `DIEU` (span: `[8:10]`)
- `[e4]` **3 . Trường hợp tai nạn hàng hải liên quan đến tàu biển Việt Nam khi hoạt động ở vùng biển quốc tế , thuyền trưởng hoặc người có trách nhiệm cao nhất trên tàu biển hoặc chủ tàu phải gửi ngay Báo cáo khẩn cho Cục Hàng hải Việt Nam .** → `KHOAN` (span: `[11:48]`)
- `[e5]` **tàu biển** → `TAI_SAN_VAT_CHAT` (span: `[18:19]`) *(lồng trong `e4` (`KHOAN`))*
- `[e6]` **tàu biển** → `TAI_SAN_VAT_CHAT` (span: `[34:35]`) *(lồng trong `e4` (`KHOAN`))*

**Quan hệ:**
- (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 7 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`)
- (`e4` 3 . Trường hợp tai nạn hàng hải liên quan đến tàu biển Việt Nam khi hoạt động ở vùng biển quốc tế , thuyền trưởng hoặc người có trách nhiệm cao nhất trên tàu biển hoặc chủ tàu phải gửi ngay Báo cáo khẩn cho Cục Hàng hải Việt Nam . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 7 `[DIEU]`)


---

### Mẫu #01_2020_TT-BGTVT_140528#body_standalone_38 (Loại: `body_standalone`)
> **[Điều 7]`<DIEU>`** . **[3 . Trường hợp tai nạn hàng hải liên quan đến **[tàu biển]`<TAI_SAN_VAT_CHAT>`** Việt Nam khi hoạt động ở vùng biển quốc tế , thuyền trưởng hoặc người có trách nhiệm cao nhất trên **[tàu biển]`<TAI_SAN_VAT_CHAT>`** hoặc chủ tàu phải gửi ngay Báo cáo khẩn cho Cục Hàng hải Việt Nam .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 7** → `DIEU` (span: `[0:2]`)
- `[e1]` **3 . Trường hợp tai nạn hàng hải liên quan đến tàu biển Việt Nam khi hoạt động ở vùng biển quốc tế , thuyền trưởng hoặc người có trách nhiệm cao nhất trên tàu biển hoặc chủ tàu phải gửi ngay Báo cáo khẩn cho Cục Hàng hải Việt Nam .** → `KHOAN` (span: `[3:40]`)
- `[e2]` **tàu biển** → `TAI_SAN_VAT_CHAT` (span: `[10:11]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **tàu biển** → `TAI_SAN_VAT_CHAT` (span: `[26:27]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 3 . Trường hợp tai nạn hàng hải liên quan đến tàu biển Việt Nam khi hoạt động ở vùng biển quốc tế , thuyền trưởng hoặc người có trách nhiệm cao nhất trên tàu biển hoặc chủ tàu phải gửi ngay Báo cáo khẩn cho Cục Hàng hải Việt Nam . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 7 `[DIEU]`)


---

### Mẫu #01_2020_TT-BGTVT_140528#body_context_39 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[01/2020/TT-BGTVT]`<SO_HIEU>`** của **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Hàng hải]`<LINH_VUC>`** . **[Điều 7]`<DIEU>`** . **[4 . Báo cáo khẩn có thể được chuyển trực tiếp hoặc gửi bằng các phương thức thông tin liên lạc phù hợp .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **01/2020/TT-BGTVT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[4:7]`)
- `[e3]` **Hàng hải** → `LINH_VUC` (span: `[9:10]`)
- `[e4]` **Điều 7** → `DIEU` (span: `[11:13]`)
- `[e5]` **4 . Báo cáo khẩn có thể được chuyển trực tiếp hoặc gửi bằng các phương thức thông tin liên lạc phù hợp .** → `KHOAN` (span: `[14:31]`)

**Quan hệ:**
- (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Hàng hải `[LINH_VUC]`)
- (`e4` Điều 7 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`)
- (`e5` 4 . Báo cáo khẩn có thể được chuyển trực tiếp hoặc gửi bằng các phương thức thông tin liên lạc phù hợp . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 7 `[DIEU]`)
- (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Hàng hải `[LINH_VUC]`)
- (`e5` 4 . Báo cáo khẩn có thể được chuyển trực tiếp hoặc gửi bằng các phương thức thông tin liên lạc phù hợp . `[KHOAN]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Hàng hải `[LINH_VUC]`)


---

### Mẫu #01_2020_TT-BGTVT_140528#body_context_40 (Loại: `body_context`)
> **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[01/2020/TT-BGTVT]`<SO_HIEU>`** . **[Điều 7]`<DIEU>`** . **[6 . Cục Hàng hải Việt Nam thông báo cho Chính quyền hàng hải của quốc gia tàu mang cờ đối với tai nạn hàng hải xảy ra trong các trường hợp **[quy định tại]`<TU_KHOA_PHAP_LY>`** **[điểm b khoản 1 Điều 2 của Thông tư này]`<THAM_CHIEU_PHAP_LY>`** .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[4:5]`)
- `[e1]` **01/2020/TT-BGTVT** → `SO_HIEU` (span: `[6:7]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[0:3]`)
- `[e3]` **Điều 7** → `DIEU` (span: `[8:10]`)
- `[e4]` **6 . Cục Hàng hải Việt Nam thông báo cho Chính quyền hàng hải của quốc gia tàu mang cờ đối với tai nạn hàng hải xảy ra trong các trường hợp quy định tại điểm b khoản 1 Điều 2 của Thông tư này .** → `KHOAN` (span: `[11:45]`)
- `[e5]` **điểm b khoản 1 Điều 2 của Thông tư này** → `THAM_CHIEU_PHAP_LY` (span: `[35:44]`) *(lồng trong `e4` (`KHOAN`))*
- `[e6]` **quy định tại** → `TU_KHOA_PHAP_LY` (span: `[33:35]`) *(lồng trong `e4` (`KHOAN`))*

**Quan hệ:**
- (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 7 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`)
- (`e4` 6 . Cục Hàng hải Việt Nam thông báo cho Chính quyền hàng hải của quốc gia tàu mang cờ đối với tai nạn hàng hải xảy ra trong các trường hợp quy định tại điểm b khoản 1 Điều 2 của Thông tư này . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 7 `[DIEU]`)
- (`e6` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e5` điểm b khoản 1 Điều 2 của Thông tư này `[THAM_CHIEU_PHAP_LY]`)
- (`e4` 6 . Cục Hàng hải Việt Nam thông báo cho Chính quyền hàng hải của quốc gia tàu mang cờ đối với tai nạn hàng hải xảy ra trong các trường hợp quy định tại điểm b khoản 1 Điều 2 của Thông tư này . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e5` điểm b khoản 1 Điều 2 của Thông tư này `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #01_2020_TT-BGTVT_140528#body_standalone_41 (Loại: `body_standalone`)
> **[Điều 7]`<DIEU>`** . **[6 . Cục Hàng hải Việt Nam thông báo cho Chính quyền hàng hải của quốc gia tàu mang cờ đối với tai nạn hàng hải xảy ra trong các trường hợp **[quy định tại]`<TU_KHOA_PHAP_LY>`** **[điểm b khoản 1 Điều 2 của Thông tư này]`<THAM_CHIEU_PHAP_LY>`** .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 7** → `DIEU` (span: `[0:2]`)
- `[e1]` **6 . Cục Hàng hải Việt Nam thông báo cho Chính quyền hàng hải của quốc gia tàu mang cờ đối với tai nạn hàng hải xảy ra trong các trường hợp quy định tại điểm b khoản 1 Điều 2 của Thông tư này .** → `KHOAN` (span: `[3:37]`)
- `[e2]` **điểm b khoản 1 Điều 2 của Thông tư này** → `THAM_CHIEU_PHAP_LY` (span: `[27:36]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **quy định tại** → `TU_KHOA_PHAP_LY` (span: `[25:27]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 6 . Cục Hàng hải Việt Nam thông báo cho Chính quyền hàng hải của quốc gia tàu mang cờ đối với tai nạn hàng hải xảy ra trong các trường hợp quy định tại điểm b khoản 1 Điều 2 của Thông tư này . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 7 `[DIEU]`)
- (`e3` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e2` điểm b khoản 1 Điều 2 của Thông tư này `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 6 . Cục Hàng hải Việt Nam thông báo cho Chính quyền hàng hải của quốc gia tàu mang cờ đối với tai nạn hàng hải xảy ra trong các trường hợp quy định tại điểm b khoản 1 Điều 2 của Thông tư này . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e2` điểm b khoản 1 Điều 2 của Thông tư này `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #01_2020_TT-BGTVT_140528#body_context_42 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[01/2020/TT-BGTVT]`<SO_HIEU>`** ban hành **[ngày 20 tháng 01 năm 2020]`<NGAY_BAN_HANH>`** bởi **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** . **[Điều 8]`<DIEU>`** . **[2 . Trường hợp tai nạn hàng hải xảy ra trong lãnh hải và vùng đặc quyền kinh tế của Việt Nam **[theo quy định tại]`<TU_KHOA_PHAP_LY>`** **[điểm b khoản 1 Điều 2 của Thông tư này]`<THAM_CHIEU_PHAP_LY>`** , sau khi xảy ra tai nạn , tàu vào neo đậu tại vùng nước cảng biển Việt Nam , Báo cáo chi tiết phải gửi **[Cảng vụ hàng hải]`<CO_QUAN_THAM_QUYEN>`** được giao quản lý tại khu vực vùng nước đó trong vòng 24 giờ , kể từ khi tàu vào neo đậu tại vị trí được chỉ định . Trường hợp sau]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **01/2020/TT-BGTVT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[11:14]`)
- `[e3]` **ngày 20 tháng 01 năm 2020** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 8** → `DIEU` (span: `[15:17]`)
- `[e5]` **2 . Trường hợp tai nạn hàng hải xảy ra trong lãnh hải và vùng đặc quyền kinh tế của Việt Nam theo quy định tại điểm b khoản 1 Điều 2 của Thông tư này , sau khi xảy ra tai nạn , tàu vào neo đậu tại vùng nước cảng biển Việt Nam , Báo cáo chi tiết phải gửi Cảng vụ hàng hải được giao quản lý tại khu vực vùng nước đó trong vòng 24 giờ , kể từ khi tàu vào neo đậu tại vị trí được chỉ định . Trường hợp sau** → `KHOAN` (span: `[18:96]`)
- `[e6]` **điểm b khoản 1 Điều 2 của Thông tư này** → `THAM_CHIEU_PHAP_LY` (span: `[36:45]`) *(lồng trong `e5` (`KHOAN`))*
- `[e7]` **theo quy định tại** → `TU_KHOA_PHAP_LY` (span: `[33:36]`) *(lồng trong `e5` (`KHOAN`))*
- `[e8]` **Cảng vụ hàng hải** → `CO_QUAN_THAM_QUYEN` (span: `[67:69]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 20 tháng 01 năm 2020 `[NGAY_BAN_HANH]`)
- (`e4` Điều 8 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`)
- (`e5` 2 . Trường hợp tai nạn hàng hải xảy ra trong lãnh hải và vùng đặc quyền kinh tế của Việt Nam theo quy định tại điểm b khoản 1 Điều 2 của Thông tư này , sau khi xảy ra tai nạn , tàu vào neo đậu tại vùng nước cảng biển Việt Nam , Báo cáo chi tiết phải gửi Cảng vụ hàng hải được giao quản lý tại khu vực vùng nước đó trong vòng 24 giờ , kể từ khi tàu vào neo đậu tại vị trí được chỉ định . Trường hợp sau `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 8 `[DIEU]`)
- (`e7` theo quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e6` điểm b khoản 1 Điều 2 của Thông tư này `[THAM_CHIEU_PHAP_LY]`)
- (`e5` 2 . Trường hợp tai nạn hàng hải xảy ra trong lãnh hải và vùng đặc quyền kinh tế của Việt Nam theo quy định tại điểm b khoản 1 Điều 2 của Thông tư này , sau khi xảy ra tai nạn , tàu vào neo đậu tại vùng nước cảng biển Việt Nam , Báo cáo chi tiết phải gửi Cảng vụ hàng hải được giao quản lý tại khu vực vùng nước đó trong vòng 24 giờ , kể từ khi tàu vào neo đậu tại vị trí được chỉ định . Trường hợp sau `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e6` điểm b khoản 1 Điều 2 của Thông tư này `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #01_2020_TT-BGTVT_140528#body_standalone_43 (Loại: `body_standalone`)
> **[Điều 8]`<DIEU>`** . **[2 . Trường hợp tai nạn hàng hải xảy ra trong lãnh hải và vùng đặc quyền kinh tế của Việt Nam **[theo quy định tại]`<TU_KHOA_PHAP_LY>`** **[điểm b khoản 1 Điều 2 của Thông tư này]`<THAM_CHIEU_PHAP_LY>`** , sau khi xảy ra tai nạn , tàu vào neo đậu tại vùng nước cảng biển Việt Nam , Báo cáo chi tiết phải gửi **[Cảng vụ hàng hải]`<CO_QUAN_THAM_QUYEN>`** được giao quản lý tại khu vực vùng nước đó trong vòng 24 giờ , kể từ khi tàu vào neo đậu tại vị trí được chỉ định . Trường hợp sau]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 8** → `DIEU` (span: `[0:2]`)
- `[e1]` **2 . Trường hợp tai nạn hàng hải xảy ra trong lãnh hải và vùng đặc quyền kinh tế của Việt Nam theo quy định tại điểm b khoản 1 Điều 2 của Thông tư này , sau khi xảy ra tai nạn , tàu vào neo đậu tại vùng nước cảng biển Việt Nam , Báo cáo chi tiết phải gửi Cảng vụ hàng hải được giao quản lý tại khu vực vùng nước đó trong vòng 24 giờ , kể từ khi tàu vào neo đậu tại vị trí được chỉ định . Trường hợp sau** → `KHOAN` (span: `[3:81]`)
- `[e2]` **điểm b khoản 1 Điều 2 của Thông tư này** → `THAM_CHIEU_PHAP_LY` (span: `[21:30]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **theo quy định tại** → `TU_KHOA_PHAP_LY` (span: `[18:21]`) *(lồng trong `e1` (`KHOAN`))*
- `[e4]` **Cảng vụ hàng hải** → `CO_QUAN_THAM_QUYEN` (span: `[52:54]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 2 . Trường hợp tai nạn hàng hải xảy ra trong lãnh hải và vùng đặc quyền kinh tế của Việt Nam theo quy định tại điểm b khoản 1 Điều 2 của Thông tư này , sau khi xảy ra tai nạn , tàu vào neo đậu tại vùng nước cảng biển Việt Nam , Báo cáo chi tiết phải gửi Cảng vụ hàng hải được giao quản lý tại khu vực vùng nước đó trong vòng 24 giờ , kể từ khi tàu vào neo đậu tại vị trí được chỉ định . Trường hợp sau `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 8 `[DIEU]`)
- (`e3` theo quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e2` điểm b khoản 1 Điều 2 của Thông tư này `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 2 . Trường hợp tai nạn hàng hải xảy ra trong lãnh hải và vùng đặc quyền kinh tế của Việt Nam theo quy định tại điểm b khoản 1 Điều 2 của Thông tư này , sau khi xảy ra tai nạn , tàu vào neo đậu tại vùng nước cảng biển Việt Nam , Báo cáo chi tiết phải gửi Cảng vụ hàng hải được giao quản lý tại khu vực vùng nước đó trong vòng 24 giờ , kể từ khi tàu vào neo đậu tại vị trí được chỉ định . Trường hợp sau `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e2` điểm b khoản 1 Điều 2 của Thông tư này `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #01_2020_TT-BGTVT_140528#body_context_44 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[01/2020/TT-BGTVT]`<SO_HIEU>`** ban hành **[ngày 20 tháng 01 năm 2020]`<NGAY_BAN_HANH>`** bởi **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** . **[Điều 8]`<DIEU>`** . **[3 . Trường hợp tai nạn hàng hải liên quan đến **[tàu biển]`<TAI_SAN_VAT_CHAT>`** Việt Nam khi hoạt động ở vùng biển quốc tế và vùng biển của quốc gia khác , sau khi xảy ra tai nạn , tàu vào neo đậu tại vùng nước cảng biển Việt Nam , Báo cáo chi tiết phải gửi **[Cảng vụ hàng hải]`<CO_QUAN_THAM_QUYEN>`** được giao quản lý tại khu vực vùng nước đó trong vòng 24 giờ , kể từ khi tàu vào neo đậu tại vị trí được chỉ định . Trường hợp sau khi xảy ra tai nạn , tàu]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **01/2020/TT-BGTVT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[11:14]`)
- `[e3]` **ngày 20 tháng 01 năm 2020** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 8** → `DIEU` (span: `[15:17]`)
- `[e5]` **3 . Trường hợp tai nạn hàng hải liên quan đến tàu biển Việt Nam khi hoạt động ở vùng biển quốc tế và vùng biển của quốc gia khác , sau khi xảy ra tai nạn , tàu vào neo đậu tại vùng nước cảng biển Việt Nam , Báo cáo chi tiết phải gửi Cảng vụ hàng hải được giao quản lý tại khu vực vùng nước đó trong vòng 24 giờ , kể từ khi tàu vào neo đậu tại vị trí được chỉ định . Trường hợp sau khi xảy ra tai nạn , tàu** → `KHOAN` (span: `[18:94]`)
- `[e6]` **Cảng vụ hàng hải** → `CO_QUAN_THAM_QUYEN` (span: `[59:61]`) *(lồng trong `e5` (`KHOAN`))*
- `[e7]` **tàu biển** → `TAI_SAN_VAT_CHAT` (span: `[25:26]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 20 tháng 01 năm 2020 `[NGAY_BAN_HANH]`)
- (`e4` Điều 8 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`)
- (`e5` 3 . Trường hợp tai nạn hàng hải liên quan đến tàu biển Việt Nam khi hoạt động ở vùng biển quốc tế và vùng biển của quốc gia khác , sau khi xảy ra tai nạn , tàu vào neo đậu tại vùng nước cảng biển Việt Nam , Báo cáo chi tiết phải gửi Cảng vụ hàng hải được giao quản lý tại khu vực vùng nước đó trong vòng 24 giờ , kể từ khi tàu vào neo đậu tại vị trí được chỉ định . Trường hợp sau khi xảy ra tai nạn , tàu `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 8 `[DIEU]`)


---

### Mẫu #01_2020_TT-BGTVT_140528#body_standalone_45 (Loại: `body_standalone`)
> **[Điều 8]`<DIEU>`** . **[3 . Trường hợp tai nạn hàng hải liên quan đến **[tàu biển]`<TAI_SAN_VAT_CHAT>`** Việt Nam khi hoạt động ở vùng biển quốc tế và vùng biển của quốc gia khác , sau khi xảy ra tai nạn , tàu vào neo đậu tại vùng nước cảng biển Việt Nam , Báo cáo chi tiết phải gửi **[Cảng vụ hàng hải]`<CO_QUAN_THAM_QUYEN>`** được giao quản lý tại khu vực vùng nước đó trong vòng 24 giờ , kể từ khi tàu vào neo đậu tại vị trí được chỉ định . Trường hợp sau khi xảy ra tai nạn , tàu]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 8** → `DIEU` (span: `[0:2]`)
- `[e1]` **3 . Trường hợp tai nạn hàng hải liên quan đến tàu biển Việt Nam khi hoạt động ở vùng biển quốc tế và vùng biển của quốc gia khác , sau khi xảy ra tai nạn , tàu vào neo đậu tại vùng nước cảng biển Việt Nam , Báo cáo chi tiết phải gửi Cảng vụ hàng hải được giao quản lý tại khu vực vùng nước đó trong vòng 24 giờ , kể từ khi tàu vào neo đậu tại vị trí được chỉ định . Trường hợp sau khi xảy ra tai nạn , tàu** → `KHOAN` (span: `[3:79]`)
- `[e2]` **Cảng vụ hàng hải** → `CO_QUAN_THAM_QUYEN` (span: `[44:46]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **tàu biển** → `TAI_SAN_VAT_CHAT` (span: `[10:11]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 3 . Trường hợp tai nạn hàng hải liên quan đến tàu biển Việt Nam khi hoạt động ở vùng biển quốc tế và vùng biển của quốc gia khác , sau khi xảy ra tai nạn , tàu vào neo đậu tại vùng nước cảng biển Việt Nam , Báo cáo chi tiết phải gửi Cảng vụ hàng hải được giao quản lý tại khu vực vùng nước đó trong vòng 24 giờ , kể từ khi tàu vào neo đậu tại vị trí được chỉ định . Trường hợp sau khi xảy ra tai nạn , tàu `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 8 `[DIEU]`)


---

### Mẫu #01_2020_TT-BGTVT_140528#body_context_46 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[01/2020/TT-BGTVT]`<SO_HIEU>`** ban hành **[ngày 20 tháng 01 năm 2020]`<NGAY_BAN_HANH>`** bởi **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** . **[Điều 9]`<DIEU>`** . **[1 . Định kỳ sáu tháng và hàng năm , **[Cảng vụ hàng hải]`<CO_QUAN_THAM_QUYEN>`** phải lập báo cáo bằng văn bản và gửi Cục Hàng hải Việt Nam về các tai nạn hàng hải xảy ra theo mẫu **[quy định tại]`<TU_KHOA_PHAP_LY>`** **[Phụ lục 3 ban hành kèm theo Thông tư này]`<THAM_CHIEU_PHAP_LY>`** .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **01/2020/TT-BGTVT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[11:14]`)
- `[e3]` **ngày 20 tháng 01 năm 2020** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 9** → `DIEU` (span: `[15:17]`)
- `[e5]` **1 . Định kỳ sáu tháng và hàng năm , Cảng vụ hàng hải phải lập báo cáo bằng văn bản và gửi Cục Hàng hải Việt Nam về các tai nạn hàng hải xảy ra theo mẫu quy định tại Phụ lục 3 ban hành kèm theo Thông tư này .** → `KHOAN` (span: `[18:57]`)
- `[e6]` **Phụ lục 3 ban hành kèm theo Thông tư này** → `THAM_CHIEU_PHAP_LY` (span: `[49:56]`) *(lồng trong `e5` (`KHOAN`))*
- `[e7]` **quy định tại** → `TU_KHOA_PHAP_LY` (span: `[47:49]`) *(lồng trong `e5` (`KHOAN`))*
- `[e8]` **Cảng vụ hàng hải** → `CO_QUAN_THAM_QUYEN` (span: `[27:29]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 20 tháng 01 năm 2020 `[NGAY_BAN_HANH]`)
- (`e4` Điều 9 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`)
- (`e5` 1 . Định kỳ sáu tháng và hàng năm , Cảng vụ hàng hải phải lập báo cáo bằng văn bản và gửi Cục Hàng hải Việt Nam về các tai nạn hàng hải xảy ra theo mẫu quy định tại Phụ lục 3 ban hành kèm theo Thông tư này . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 9 `[DIEU]`)
- (`e7` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e6` Phụ lục 3 ban hành kèm theo Thông tư này `[THAM_CHIEU_PHAP_LY]`)
- (`e5` 1 . Định kỳ sáu tháng và hàng năm , Cảng vụ hàng hải phải lập báo cáo bằng văn bản và gửi Cục Hàng hải Việt Nam về các tai nạn hàng hải xảy ra theo mẫu quy định tại Phụ lục 3 ban hành kèm theo Thông tư này . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e6` Phụ lục 3 ban hành kèm theo Thông tư này `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #01_2020_TT-BGTVT_140528#body_standalone_47 (Loại: `body_standalone`)
> **[Điều 9]`<DIEU>`** . **[1 . Định kỳ sáu tháng và hàng năm , **[Cảng vụ hàng hải]`<CO_QUAN_THAM_QUYEN>`** phải lập báo cáo bằng văn bản và gửi Cục Hàng hải Việt Nam về các tai nạn hàng hải xảy ra theo mẫu **[quy định tại]`<TU_KHOA_PHAP_LY>`** **[Phụ lục 3 ban hành kèm theo Thông tư này]`<THAM_CHIEU_PHAP_LY>`** .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 9** → `DIEU` (span: `[0:2]`)
- `[e1]` **1 . Định kỳ sáu tháng và hàng năm , Cảng vụ hàng hải phải lập báo cáo bằng văn bản và gửi Cục Hàng hải Việt Nam về các tai nạn hàng hải xảy ra theo mẫu quy định tại Phụ lục 3 ban hành kèm theo Thông tư này .** → `KHOAN` (span: `[3:42]`)
- `[e2]` **Phụ lục 3 ban hành kèm theo Thông tư này** → `THAM_CHIEU_PHAP_LY` (span: `[34:41]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **quy định tại** → `TU_KHOA_PHAP_LY` (span: `[32:34]`) *(lồng trong `e1` (`KHOAN`))*
- `[e4]` **Cảng vụ hàng hải** → `CO_QUAN_THAM_QUYEN` (span: `[12:14]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 1 . Định kỳ sáu tháng và hàng năm , Cảng vụ hàng hải phải lập báo cáo bằng văn bản và gửi Cục Hàng hải Việt Nam về các tai nạn hàng hải xảy ra theo mẫu quy định tại Phụ lục 3 ban hành kèm theo Thông tư này . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 9 `[DIEU]`)
- (`e3` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e2` Phụ lục 3 ban hành kèm theo Thông tư này `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 1 . Định kỳ sáu tháng và hàng năm , Cảng vụ hàng hải phải lập báo cáo bằng văn bản và gửi Cục Hàng hải Việt Nam về các tai nạn hàng hải xảy ra theo mẫu quy định tại Phụ lục 3 ban hành kèm theo Thông tư này . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e2` Phụ lục 3 ban hành kèm theo Thông tư này `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #01_2020_TT-BGTVT_140528#body_context_48 (Loại: `body_context`)
> **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[01/2020/TT-BGTVT]`<SO_HIEU>`** . **[Điều 9]`<DIEU>`** . **[2 . Định kỳ sáu tháng và hàng năm , Cục Hàng hải Việt Nam phải lập báo cáo bằng văn bản và gửi **[Bộ Giao thông vận tải]`<CO_QUAN_THAM_QUYEN>`** về các tai nạn hàng hải theo mẫu **[quy định tại]`<TU_KHOA_PHAP_LY>`** **[Phụ lục 3 ban hành kèm theo Thông tư này]`<THAM_CHIEU_PHAP_LY>`** .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[4:5]`)
- `[e1]` **01/2020/TT-BGTVT** → `SO_HIEU` (span: `[6:7]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[0:3]`)
- `[e3]` **Điều 9** → `DIEU` (span: `[8:10]`)
- `[e4]` **2 . Định kỳ sáu tháng và hàng năm , Cục Hàng hải Việt Nam phải lập báo cáo bằng văn bản và gửi Bộ Giao thông vận tải về các tai nạn hàng hải theo mẫu quy định tại Phụ lục 3 ban hành kèm theo Thông tư này .** → `KHOAN` (span: `[11:49]`)
- `[e5]` **Phụ lục 3 ban hành kèm theo Thông tư này** → `THAM_CHIEU_PHAP_LY` (span: `[41:48]`) *(lồng trong `e4` (`KHOAN`))*
- `[e6]` **quy định tại** → `TU_KHOA_PHAP_LY` (span: `[39:41]`) *(lồng trong `e4` (`KHOAN`))*
- `[e7]` **Bộ Giao thông vận tải** → `CO_QUAN_THAM_QUYEN` (span: `[30:33]`) *(lồng trong `e4` (`KHOAN`))*

**Quan hệ:**
- (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 9 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`)
- (`e4` 2 . Định kỳ sáu tháng và hàng năm , Cục Hàng hải Việt Nam phải lập báo cáo bằng văn bản và gửi Bộ Giao thông vận tải về các tai nạn hàng hải theo mẫu quy định tại Phụ lục 3 ban hành kèm theo Thông tư này . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 9 `[DIEU]`)
- (`e6` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e5` Phụ lục 3 ban hành kèm theo Thông tư này `[THAM_CHIEU_PHAP_LY]`)
- (`e4` 2 . Định kỳ sáu tháng và hàng năm , Cục Hàng hải Việt Nam phải lập báo cáo bằng văn bản và gửi Bộ Giao thông vận tải về các tai nạn hàng hải theo mẫu quy định tại Phụ lục 3 ban hành kèm theo Thông tư này . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e5` Phụ lục 3 ban hành kèm theo Thông tư này `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #01_2020_TT-BGTVT_140528#body_standalone_49 (Loại: `body_standalone`)
> **[Điều 9]`<DIEU>`** . **[2 . Định kỳ sáu tháng và hàng năm , Cục Hàng hải Việt Nam phải lập báo cáo bằng văn bản và gửi **[Bộ Giao thông vận tải]`<CO_QUAN_THAM_QUYEN>`** về các tai nạn hàng hải theo mẫu **[quy định tại]`<TU_KHOA_PHAP_LY>`** **[Phụ lục 3 ban hành kèm theo Thông tư này]`<THAM_CHIEU_PHAP_LY>`** .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 9** → `DIEU` (span: `[0:2]`)
- `[e1]` **2 . Định kỳ sáu tháng và hàng năm , Cục Hàng hải Việt Nam phải lập báo cáo bằng văn bản và gửi Bộ Giao thông vận tải về các tai nạn hàng hải theo mẫu quy định tại Phụ lục 3 ban hành kèm theo Thông tư này .** → `KHOAN` (span: `[3:41]`)
- `[e2]` **Phụ lục 3 ban hành kèm theo Thông tư này** → `THAM_CHIEU_PHAP_LY` (span: `[33:40]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **quy định tại** → `TU_KHOA_PHAP_LY` (span: `[31:33]`) *(lồng trong `e1` (`KHOAN`))*
- `[e4]` **Bộ Giao thông vận tải** → `CO_QUAN_THAM_QUYEN` (span: `[22:25]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 2 . Định kỳ sáu tháng và hàng năm , Cục Hàng hải Việt Nam phải lập báo cáo bằng văn bản và gửi Bộ Giao thông vận tải về các tai nạn hàng hải theo mẫu quy định tại Phụ lục 3 ban hành kèm theo Thông tư này . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 9 `[DIEU]`)
- (`e3` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e2` Phụ lục 3 ban hành kèm theo Thông tư này `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 2 . Định kỳ sáu tháng và hàng năm , Cục Hàng hải Việt Nam phải lập báo cáo bằng văn bản và gửi Bộ Giao thông vận tải về các tai nạn hàng hải theo mẫu quy định tại Phụ lục 3 ban hành kèm theo Thông tư này . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e2` Phụ lục 3 ban hành kèm theo Thông tư này `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #01_2020_TT-BGTVT_140528#body_context_50 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[01/2020/TT-BGTVT]`<SO_HIEU>`** ban hành **[ngày 20 tháng 01 năm 2020]`<NGAY_BAN_HANH>`** bởi **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** . **[Điều 9]`<DIEU>`** . **[Khoản 3]`<KHOAN>`** . **[b ) Thời hạn gửi báo cáo năm : **[Cảng vụ hàng hải]`<CO_QUAN_THAM_QUYEN>`** chậm nhất ngày 16 tháng 12 hàng năm và Cục Hàng hải Việt Nam chậm nhất là ngày 20 tháng 12 hàng năm .]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **01/2020/TT-BGTVT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[11:14]`)
- `[e3]` **ngày 20 tháng 01 năm 2020** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 9** → `DIEU` (span: `[15:17]`)
- `[e5]` **Khoản 3** → `KHOAN` (span: `[18:20]`)
- `[e6]` **b ) Thời hạn gửi báo cáo năm : Cảng vụ hàng hải chậm nhất ngày 16 tháng 12 hàng năm và Cục Hàng hải Việt Nam chậm nhất là ngày 20 tháng 12 hàng năm .** → `DIEM` (span: `[21:52]`)
- `[e7]` **Cảng vụ hàng hải** → `CO_QUAN_THAM_QUYEN` (span: `[28:30]`) *(lồng trong `e6` (`DIEM`))*

**Quan hệ:**
- (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 20 tháng 01 năm 2020 `[NGAY_BAN_HANH]`)
- (`e4` Điều 9 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`)
- (`e5` Khoản 3 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 9 `[DIEU]`)
- (`e6` b ) Thời hạn gửi báo cáo năm : Cảng vụ hàng hải chậm nhất ngày 16 tháng 12 hàng năm và Cục Hàng hải Việt Nam chậm nhất là ngày 20 tháng 12 hàng năm . `[DIEM]`) ==[ **THUOC_VE** ]==> (`e5` Khoản 3 `[KHOAN]`)


---

### Mẫu #01_2020_TT-BGTVT_140528#body_standalone_51 (Loại: `body_standalone`)
> **[Điều 9]`<DIEU>`** . **[Khoản 3]`<KHOAN>`** . **[b ) Thời hạn gửi báo cáo năm : **[Cảng vụ hàng hải]`<CO_QUAN_THAM_QUYEN>`** chậm nhất ngày 16 tháng 12 hàng năm và Cục Hàng hải Việt Nam chậm nhất là ngày 20 tháng 12 hàng năm .]`<DIEM>`**

**Thực thể:**
- `[e0]` **Điều 9** → `DIEU` (span: `[0:2]`)
- `[e1]` **Khoản 3** → `KHOAN` (span: `[3:5]`)
- `[e2]` **b ) Thời hạn gửi báo cáo năm : Cảng vụ hàng hải chậm nhất ngày 16 tháng 12 hàng năm và Cục Hàng hải Việt Nam chậm nhất là ngày 20 tháng 12 hàng năm .** → `DIEM` (span: `[6:37]`)
- `[e3]` **Cảng vụ hàng hải** → `CO_QUAN_THAM_QUYEN` (span: `[13:15]`) *(lồng trong `e2` (`DIEM`))*

**Quan hệ:**
- (`e1` Khoản 3 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 9 `[DIEU]`)
- (`e2` b ) Thời hạn gửi báo cáo năm : Cảng vụ hàng hải chậm nhất ngày 16 tháng 12 hàng năm và Cục Hàng hải Việt Nam chậm nhất là ngày 20 tháng 12 hàng năm . `[DIEM]`) ==[ **THUOC_VE** ]==> (`e1` Khoản 3 `[KHOAN]`)


---

### Mẫu #01_2020_TT-BGTVT_140528#body_context_52 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[01/2020/TT-BGTVT]`<SO_HIEU>`** của **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Hàng hải]`<LINH_VUC>`** . **[Điều 11 . Các trường hợp điều tra tai nạn hàng hải]`<DIEU>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **01/2020/TT-BGTVT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[4:7]`)
- `[e3]` **Hàng hải** → `LINH_VUC` (span: `[9:10]`)
- `[e4]` **Điều 11 . Các trường hợp điều tra tai nạn hàng hải** → `DIEU` (span: `[11:19]`)

**Quan hệ:**
- (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Hàng hải `[LINH_VUC]`)
- (`e4` Điều 11 . Các trường hợp điều tra tai nạn hàng hải `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`)
- (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Hàng hải `[LINH_VUC]`)
- (`e4` Điều 11 . Các trường hợp điều tra tai nạn hàng hải `[DIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Hàng hải `[LINH_VUC]`)


---

### Mẫu #01_2020_TT-BGTVT_140528#body_context_53 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[01/2020/TT-BGTVT]`<SO_HIEU>`** của **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Hàng hải]`<LINH_VUC>`** . **[Điều 11]`<DIEU>`** . **[2 . Các tai nạn hàng hải ít nghiêm trọng có thể được điều tra hay không điều tra do **[Giám đốc]`<CHU_THE_CA_NHAN>`** **[Cảng vụ hàng hải]`<CO_QUAN_THAM_QUYEN>`** quyết định . Trường hợp không điều tra , **[Cảng vụ hàng hải]`<CO_QUAN_THAM_QUYEN>`** phải báo cáo Cục Hàng hải Việt Nam .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **01/2020/TT-BGTVT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[4:7]`)
- `[e3]` **Hàng hải** → `LINH_VUC` (span: `[9:10]`)
- `[e4]` **Điều 11** → `DIEU` (span: `[11:13]`)
- `[e5]` **2 . Các tai nạn hàng hải ít nghiêm trọng có thể được điều tra hay không điều tra do Giám đốc Cảng vụ hàng hải quyết định . Trường hợp không điều tra , Cảng vụ hàng hải phải báo cáo Cục Hàng hải Việt Nam .** → `KHOAN` (span: `[14:45]`)
- `[e6]` **Cảng vụ hàng hải** → `CO_QUAN_THAM_QUYEN` (span: `[29:31]`) *(lồng trong `e5` (`KHOAN`))*
- `[e7]` **Cảng vụ hàng hải** → `CO_QUAN_THAM_QUYEN` (span: `[37:39]`) *(lồng trong `e5` (`KHOAN`))*
- `[e8]` **Giám đốc** → `CHU_THE_CA_NHAN` (span: `[28:29]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Hàng hải `[LINH_VUC]`)
- (`e4` Điều 11 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`)
- (`e5` 2 . Các tai nạn hàng hải ít nghiêm trọng có thể được điều tra hay không điều tra do Giám đốc Cảng vụ hàng hải quyết định . Trường hợp không điều tra , Cảng vụ hàng hải phải báo cáo Cục Hàng hải Việt Nam . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 11 `[DIEU]`)
- (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Hàng hải `[LINH_VUC]`)
- (`e5` 2 . Các tai nạn hàng hải ít nghiêm trọng có thể được điều tra hay không điều tra do Giám đốc Cảng vụ hàng hải quyết định . Trường hợp không điều tra , Cảng vụ hàng hải phải báo cáo Cục Hàng hải Việt Nam . `[KHOAN]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Hàng hải `[LINH_VUC]`)


---

### Mẫu #01_2020_TT-BGTVT_140528#body_standalone_54 (Loại: `body_standalone`)
> **[Điều 11]`<DIEU>`** . **[2 . Các tai nạn hàng hải ít nghiêm trọng có thể được điều tra hay không điều tra do **[Giám đốc]`<CHU_THE_CA_NHAN>`** **[Cảng vụ hàng hải]`<CO_QUAN_THAM_QUYEN>`** quyết định . Trường hợp không điều tra , **[Cảng vụ hàng hải]`<CO_QUAN_THAM_QUYEN>`** phải báo cáo Cục Hàng hải Việt Nam .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 11** → `DIEU` (span: `[0:2]`)
- `[e1]` **2 . Các tai nạn hàng hải ít nghiêm trọng có thể được điều tra hay không điều tra do Giám đốc Cảng vụ hàng hải quyết định . Trường hợp không điều tra , Cảng vụ hàng hải phải báo cáo Cục Hàng hải Việt Nam .** → `KHOAN` (span: `[3:34]`)
- `[e2]` **Cảng vụ hàng hải** → `CO_QUAN_THAM_QUYEN` (span: `[18:20]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **Cảng vụ hàng hải** → `CO_QUAN_THAM_QUYEN` (span: `[26:28]`) *(lồng trong `e1` (`KHOAN`))*
- `[e4]` **Giám đốc** → `CHU_THE_CA_NHAN` (span: `[17:18]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 2 . Các tai nạn hàng hải ít nghiêm trọng có thể được điều tra hay không điều tra do Giám đốc Cảng vụ hàng hải quyết định . Trường hợp không điều tra , Cảng vụ hàng hải phải báo cáo Cục Hàng hải Việt Nam . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 11 `[DIEU]`)


---

### Mẫu #01_2020_TT-BGTVT_140528#body_context_55 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[01/2020/TT-BGTVT]`<SO_HIEU>`** ban hành **[ngày 20 tháng 01 năm 2020]`<NGAY_BAN_HANH>`** bởi **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** . **[Điều 12]`<DIEU>`** . **[Khoản 1]`<KHOAN>`** . **[a ) **[Giám đốc]`<CHU_THE_CA_NHAN>`** **[Cảng vụ hàng hải]`<CO_QUAN_THAM_QUYEN>`** khu vực có trách nhiệm tổ chức điều tra tai nạn hàng hải xảy ra trong vùng nước cảng biển thuộc phạm vi quản lý và tai nạn hàng hải khác do Cục trưởng Cục Hàng hải Việt Nam giao ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **01/2020/TT-BGTVT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[11:14]`)
- `[e3]` **ngày 20 tháng 01 năm 2020** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 12** → `DIEU` (span: `[15:17]`)
- `[e5]` **Khoản 1** → `KHOAN` (span: `[18:20]`)
- `[e6]` **a ) Giám đốc Cảng vụ hàng hải khu vực có trách nhiệm tổ chức điều tra tai nạn hàng hải xảy ra trong vùng nước cảng biển thuộc phạm vi quản lý và tai nạn hàng hải khác do Cục trưởng Cục Hàng hải Việt Nam giao ;** → `DIEM` (span: `[21:54]`)
- `[e7]` **Cảng vụ hàng hải** → `CO_QUAN_THAM_QUYEN` (span: `[24:26]`) *(lồng trong `e6` (`DIEM`))*
- `[e8]` **Giám đốc** → `CHU_THE_CA_NHAN` (span: `[23:24]`) *(lồng trong `e6` (`DIEM`))*

**Quan hệ:**
- (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 20 tháng 01 năm 2020 `[NGAY_BAN_HANH]`)
- (`e4` Điều 12 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`)
- (`e5` Khoản 1 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 12 `[DIEU]`)
- (`e6` a ) Giám đốc Cảng vụ hàng hải khu vực có trách nhiệm tổ chức điều tra tai nạn hàng hải xảy ra trong vùng nước cảng biển thuộc phạm vi quản lý và tai nạn hàng hải khác do Cục trưởng Cục Hàng hải Việt Nam giao ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e5` Khoản 1 `[KHOAN]`)


---

### Mẫu #01_2020_TT-BGTVT_140528#body_standalone_56 (Loại: `body_standalone`)
> **[Điều 12]`<DIEU>`** . **[Khoản 1]`<KHOAN>`** . **[a ) **[Giám đốc]`<CHU_THE_CA_NHAN>`** **[Cảng vụ hàng hải]`<CO_QUAN_THAM_QUYEN>`** khu vực có trách nhiệm tổ chức điều tra tai nạn hàng hải xảy ra trong vùng nước cảng biển thuộc phạm vi quản lý và tai nạn hàng hải khác do Cục trưởng Cục Hàng hải Việt Nam giao ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Điều 12** → `DIEU` (span: `[0:2]`)
- `[e1]` **Khoản 1** → `KHOAN` (span: `[3:5]`)
- `[e2]` **a ) Giám đốc Cảng vụ hàng hải khu vực có trách nhiệm tổ chức điều tra tai nạn hàng hải xảy ra trong vùng nước cảng biển thuộc phạm vi quản lý và tai nạn hàng hải khác do Cục trưởng Cục Hàng hải Việt Nam giao ;** → `DIEM` (span: `[6:39]`)
- `[e3]` **Cảng vụ hàng hải** → `CO_QUAN_THAM_QUYEN` (span: `[9:11]`) *(lồng trong `e2` (`DIEM`))*
- `[e4]` **Giám đốc** → `CHU_THE_CA_NHAN` (span: `[8:9]`) *(lồng trong `e2` (`DIEM`))*

**Quan hệ:**
- (`e1` Khoản 1 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 12 `[DIEU]`)
- (`e2` a ) Giám đốc Cảng vụ hàng hải khu vực có trách nhiệm tổ chức điều tra tai nạn hàng hải xảy ra trong vùng nước cảng biển thuộc phạm vi quản lý và tai nạn hàng hải khác do Cục trưởng Cục Hàng hải Việt Nam giao ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e1` Khoản 1 `[KHOAN]`)


---

### Mẫu #01_2020_TT-BGTVT_140528#body_context_57 (Loại: `body_context`)
> **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[01/2020/TT-BGTVT]`<SO_HIEU>`** . **[Điều 12]`<DIEU>`** . **[Khoản 1]`<KHOAN>`** . **[b ) Trong trường hợp tai nạn hàng hải xảy ra tại vùng nước cảng biển , **[tàu biển]`<TAI_SAN_VAT_CHAT>`** liên quan đến tai nạn tiếp tục hành trình đến vị trí neo đậu được chỉ định tại vùng nước cảng biển khác , Cục trưởng Cục Hàng hải Việt Nam quyết định giao tổ chức điều tra tai nạn hàng hải đó cho **[Cảng vụ hàng hải]`<CO_QUAN_THAM_QUYEN>`** nơi xảy ra tai nạn hoặc nơi **[tàu biển]`<TAI_SAN_VAT_CHAT>`** neo đậu . Khi tàu đến vị trí neo đậu được chỉ định trong vùng nước cảng]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[4:5]`)
- `[e1]` **01/2020/TT-BGTVT** → `SO_HIEU` (span: `[6:7]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[0:3]`)
- `[e3]` **Điều 12** → `DIEU` (span: `[8:10]`)
- `[e4]` **Khoản 1** → `KHOAN` (span: `[11:13]`)
- `[e5]` **b ) Trong trường hợp tai nạn hàng hải xảy ra tại vùng nước cảng biển , tàu biển liên quan đến tai nạn tiếp tục hành trình đến vị trí neo đậu được chỉ định tại vùng nước cảng biển khác , Cục trưởng Cục Hàng hải Việt Nam quyết định giao tổ chức điều tra tai nạn hàng hải đó cho Cảng vụ hàng hải nơi xảy ra tai nạn hoặc nơi tàu biển neo đậu . Khi tàu đến vị trí neo đậu được chỉ định trong vùng nước cảng** → `DIEM` (span: `[14:83]`)
- `[e6]` **Cảng vụ hàng hải** → `CO_QUAN_THAM_QUYEN` (span: `[59:61]`) *(lồng trong `e5` (`DIEM`))*
- `[e7]` **tàu biển** → `TAI_SAN_VAT_CHAT` (span: `[28:29]`) *(lồng trong `e5` (`DIEM`))*
- `[e8]` **tàu biển** → `TAI_SAN_VAT_CHAT` (span: `[67:68]`) *(lồng trong `e5` (`DIEM`))*

**Quan hệ:**
- (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 12 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`)
- (`e4` Khoản 1 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 12 `[DIEU]`)
- (`e5` b ) Trong trường hợp tai nạn hàng hải xảy ra tại vùng nước cảng biển , tàu biển liên quan đến tai nạn tiếp tục hành trình đến vị trí neo đậu được chỉ định tại vùng nước cảng biển khác , Cục trưởng Cục Hàng hải Việt Nam quyết định giao tổ chức điều tra tai nạn hàng hải đó cho Cảng vụ hàng hải nơi xảy ra tai nạn hoặc nơi tàu biển neo đậu . Khi tàu đến vị trí neo đậu được chỉ định trong vùng nước cảng `[DIEM]`) ==[ **THUOC_VE** ]==> (`e4` Khoản 1 `[KHOAN]`)


---

### Mẫu #01_2020_TT-BGTVT_140528#body_standalone_58 (Loại: `body_standalone`)
> **[Điều 12]`<DIEU>`** . **[Khoản 1]`<KHOAN>`** . **[b ) Trong trường hợp tai nạn hàng hải xảy ra tại vùng nước cảng biển , **[tàu biển]`<TAI_SAN_VAT_CHAT>`** liên quan đến tai nạn tiếp tục hành trình đến vị trí neo đậu được chỉ định tại vùng nước cảng biển khác , Cục trưởng Cục Hàng hải Việt Nam quyết định giao tổ chức điều tra tai nạn hàng hải đó cho **[Cảng vụ hàng hải]`<CO_QUAN_THAM_QUYEN>`** nơi xảy ra tai nạn hoặc nơi **[tàu biển]`<TAI_SAN_VAT_CHAT>`** neo đậu . Khi tàu đến vị trí neo đậu được chỉ định trong vùng nước cảng]`<DIEM>`**

**Thực thể:**
- `[e0]` **Điều 12** → `DIEU` (span: `[0:2]`)
- `[e1]` **Khoản 1** → `KHOAN` (span: `[3:5]`)
- `[e2]` **b ) Trong trường hợp tai nạn hàng hải xảy ra tại vùng nước cảng biển , tàu biển liên quan đến tai nạn tiếp tục hành trình đến vị trí neo đậu được chỉ định tại vùng nước cảng biển khác , Cục trưởng Cục Hàng hải Việt Nam quyết định giao tổ chức điều tra tai nạn hàng hải đó cho Cảng vụ hàng hải nơi xảy ra tai nạn hoặc nơi tàu biển neo đậu . Khi tàu đến vị trí neo đậu được chỉ định trong vùng nước cảng** → `DIEM` (span: `[6:75]`)
- `[e3]` **Cảng vụ hàng hải** → `CO_QUAN_THAM_QUYEN` (span: `[51:53]`) *(lồng trong `e2` (`DIEM`))*
- `[e4]` **tàu biển** → `TAI_SAN_VAT_CHAT` (span: `[20:21]`) *(lồng trong `e2` (`DIEM`))*
- `[e5]` **tàu biển** → `TAI_SAN_VAT_CHAT` (span: `[59:60]`) *(lồng trong `e2` (`DIEM`))*

**Quan hệ:**
- (`e1` Khoản 1 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 12 `[DIEU]`)
- (`e2` b ) Trong trường hợp tai nạn hàng hải xảy ra tại vùng nước cảng biển , tàu biển liên quan đến tai nạn tiếp tục hành trình đến vị trí neo đậu được chỉ định tại vùng nước cảng biển khác , Cục trưởng Cục Hàng hải Việt Nam quyết định giao tổ chức điều tra tai nạn hàng hải đó cho Cảng vụ hàng hải nơi xảy ra tai nạn hoặc nơi tàu biển neo đậu . Khi tàu đến vị trí neo đậu được chỉ định trong vùng nước cảng `[DIEM]`) ==[ **THUOC_VE** ]==> (`e1` Khoản 1 `[KHOAN]`)


---

### Mẫu #01_2020_TT-BGTVT_140528#body_context_59 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[01/2020/TT-BGTVT]`<SO_HIEU>`** ban hành **[ngày 20 tháng 01 năm 2020]`<NGAY_BAN_HANH>`** bởi **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** . **[Điều 12]`<DIEU>`** . **[2 . Khi nhận được thông tin về tai nạn hàng hải trong vùng nước cảng biển thuộc khu vực quản lý , trong điều kiện cho phép , **[Giám đốc]`<CHU_THE_CA_NHAN>`** **[Cảng vụ hàng hải]`<CO_QUAN_THAM_QUYEN>`** phải cử người có chuyên môn nghiệp vụ đến ngay hiện trường xảy ra tai nạn hàng hải và lên tàu kiểm tra hiện trường , xem xét các vị trí làm việc và thu thập các chứng cứ cần thiết cho công tác điều tra . Khi tiến hành các công việc này , nhất thiết phải lập biên bản và có]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **01/2020/TT-BGTVT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[11:14]`)
- `[e3]` **ngày 20 tháng 01 năm 2020** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 12** → `DIEU` (span: `[15:17]`)
- `[e5]` **2 . Khi nhận được thông tin về tai nạn hàng hải trong vùng nước cảng biển thuộc khu vực quản lý , trong điều kiện cho phép , Giám đốc Cảng vụ hàng hải phải cử người có chuyên môn nghiệp vụ đến ngay hiện trường xảy ra tai nạn hàng hải và lên tàu kiểm tra hiện trường , xem xét các vị trí làm việc và thu thập các chứng cứ cần thiết cho công tác điều tra . Khi tiến hành các công việc này , nhất thiết phải lập biên bản và có** → `KHOAN` (span: `[18:88]`)
- `[e6]` **Cảng vụ hàng hải** → `CO_QUAN_THAM_QUYEN` (span: `[42:44]`) *(lồng trong `e5` (`KHOAN`))*
- `[e7]` **Giám đốc** → `CHU_THE_CA_NHAN` (span: `[41:42]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 20 tháng 01 năm 2020 `[NGAY_BAN_HANH]`)
- (`e4` Điều 12 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`)
- (`e5` 2 . Khi nhận được thông tin về tai nạn hàng hải trong vùng nước cảng biển thuộc khu vực quản lý , trong điều kiện cho phép , Giám đốc Cảng vụ hàng hải phải cử người có chuyên môn nghiệp vụ đến ngay hiện trường xảy ra tai nạn hàng hải và lên tàu kiểm tra hiện trường , xem xét các vị trí làm việc và thu thập các chứng cứ cần thiết cho công tác điều tra . Khi tiến hành các công việc này , nhất thiết phải lập biên bản và có `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 12 `[DIEU]`)


---

### Mẫu #01_2020_TT-BGTVT_140528#body_standalone_60 (Loại: `body_standalone`)
> **[Điều 12]`<DIEU>`** . **[2 . Khi nhận được thông tin về tai nạn hàng hải trong vùng nước cảng biển thuộc khu vực quản lý , trong điều kiện cho phép , **[Giám đốc]`<CHU_THE_CA_NHAN>`** **[Cảng vụ hàng hải]`<CO_QUAN_THAM_QUYEN>`** phải cử người có chuyên môn nghiệp vụ đến ngay hiện trường xảy ra tai nạn hàng hải và lên tàu kiểm tra hiện trường , xem xét các vị trí làm việc và thu thập các chứng cứ cần thiết cho công tác điều tra . Khi tiến hành các công việc này , nhất thiết phải lập biên bản và có]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 12** → `DIEU` (span: `[0:2]`)
- `[e1]` **2 . Khi nhận được thông tin về tai nạn hàng hải trong vùng nước cảng biển thuộc khu vực quản lý , trong điều kiện cho phép , Giám đốc Cảng vụ hàng hải phải cử người có chuyên môn nghiệp vụ đến ngay hiện trường xảy ra tai nạn hàng hải và lên tàu kiểm tra hiện trường , xem xét các vị trí làm việc và thu thập các chứng cứ cần thiết cho công tác điều tra . Khi tiến hành các công việc này , nhất thiết phải lập biên bản và có** → `KHOAN` (span: `[3:73]`)
- `[e2]` **Cảng vụ hàng hải** → `CO_QUAN_THAM_QUYEN` (span: `[27:29]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **Giám đốc** → `CHU_THE_CA_NHAN` (span: `[26:27]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 2 . Khi nhận được thông tin về tai nạn hàng hải trong vùng nước cảng biển thuộc khu vực quản lý , trong điều kiện cho phép , Giám đốc Cảng vụ hàng hải phải cử người có chuyên môn nghiệp vụ đến ngay hiện trường xảy ra tai nạn hàng hải và lên tàu kiểm tra hiện trường , xem xét các vị trí làm việc và thu thập các chứng cứ cần thiết cho công tác điều tra . Khi tiến hành các công việc này , nhất thiết phải lập biên bản và có `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 12 `[DIEU]`)


---

### Mẫu #01_2020_TT-BGTVT_140528#body_context_61 (Loại: `body_context`)
> **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[01/2020/TT-BGTVT]`<SO_HIEU>`** . **[Điều 12]`<DIEU>`** . **[3 . **[Giám đốc]`<CHU_THE_CA_NHAN>`** **[Cảng vụ hàng hải]`<CO_QUAN_THAM_QUYEN>`** tổ chức điều tra tai nạn hàng hải có trách nhiệm ra **[quyết định thành lập]`<GIAY_TO_HO_SO>`** Tổ điều tra tai nạn hàng hải .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[4:5]`)
- `[e1]` **01/2020/TT-BGTVT** → `SO_HIEU` (span: `[6:7]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[0:3]`)
- `[e3]` **Điều 12** → `DIEU` (span: `[8:10]`)
- `[e4]` **3 . Giám đốc Cảng vụ hàng hải tổ chức điều tra tai nạn hàng hải có trách nhiệm ra quyết định thành lập Tổ điều tra tai nạn hàng hải .** → `KHOAN` (span: `[11:30]`)
- `[e5]` **Cảng vụ hàng hải** → `CO_QUAN_THAM_QUYEN` (span: `[14:16]`) *(lồng trong `e4` (`KHOAN`))*
- `[e6]` **quyết định thành lập** → `GIAY_TO_HO_SO` (span: `[23:25]`) *(lồng trong `e4` (`KHOAN`))*
- `[e7]` **Giám đốc** → `CHU_THE_CA_NHAN` (span: `[13:14]`) *(lồng trong `e4` (`KHOAN`))*

**Quan hệ:**
- (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 12 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`)
- (`e4` 3 . Giám đốc Cảng vụ hàng hải tổ chức điều tra tai nạn hàng hải có trách nhiệm ra quyết định thành lập Tổ điều tra tai nạn hàng hải . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 12 `[DIEU]`)


---

### Mẫu #01_2020_TT-BGTVT_140528#body_standalone_62 (Loại: `body_standalone`)
> **[Điều 12]`<DIEU>`** . **[3 . **[Giám đốc]`<CHU_THE_CA_NHAN>`** **[Cảng vụ hàng hải]`<CO_QUAN_THAM_QUYEN>`** tổ chức điều tra tai nạn hàng hải có trách nhiệm ra **[quyết định thành lập]`<GIAY_TO_HO_SO>`** Tổ điều tra tai nạn hàng hải .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 12** → `DIEU` (span: `[0:2]`)
- `[e1]` **3 . Giám đốc Cảng vụ hàng hải tổ chức điều tra tai nạn hàng hải có trách nhiệm ra quyết định thành lập Tổ điều tra tai nạn hàng hải .** → `KHOAN` (span: `[3:22]`)
- `[e2]` **Cảng vụ hàng hải** → `CO_QUAN_THAM_QUYEN` (span: `[6:8]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **quyết định thành lập** → `GIAY_TO_HO_SO` (span: `[15:17]`) *(lồng trong `e1` (`KHOAN`))*
- `[e4]` **Giám đốc** → `CHU_THE_CA_NHAN` (span: `[5:6]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 3 . Giám đốc Cảng vụ hàng hải tổ chức điều tra tai nạn hàng hải có trách nhiệm ra quyết định thành lập Tổ điều tra tai nạn hàng hải . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 12 `[DIEU]`)


---

### Mẫu #01_2020_TT-BGTVT_140528#body_context_63 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[01/2020/TT-BGTVT]`<SO_HIEU>`** của **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Hàng hải]`<LINH_VUC>`** . **[Điều 12]`<DIEU>`** . **[4 . Trong quá trình điều tra tai nạn hàng hải , nếu phát hiện có dấu hiệu cấu thành tội phạm thì **[Giám đốc]`<CHU_THE_CA_NHAN>`** **[Cảng vụ hàng hải]`<CO_QUAN_THAM_QUYEN>`** thông báo cho **[cơ quan điều tra]`<CO_QUAN_THAM_QUYEN>`** có thẩm quyền và chuyển giao hồ sơ , tài liệu , chứng cứ có liên quan đến vụ tai nạn hàng hải theo yêu cầu của **[cơ quan điều tra]`<CO_QUAN_THAM_QUYEN>`** có thẩm quyền ; trước khi chuyển giao , hồ sơ , tài liệu phải được sao y hoặc phô tô để lưu lại phục vụ việc điều tra tai nạn hàng]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **01/2020/TT-BGTVT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[4:7]`)
- `[e3]` **Hàng hải** → `LINH_VUC` (span: `[9:10]`)
- `[e4]` **Điều 12** → `DIEU` (span: `[11:13]`)
- `[e5]` **4 . Trong quá trình điều tra tai nạn hàng hải , nếu phát hiện có dấu hiệu cấu thành tội phạm thì Giám đốc Cảng vụ hàng hải thông báo cho cơ quan điều tra có thẩm quyền và chuyển giao hồ sơ , tài liệu , chứng cứ có liên quan đến vụ tai nạn hàng hải theo yêu cầu của cơ quan điều tra có thẩm quyền ; trước khi chuyển giao , hồ sơ , tài liệu phải được sao y hoặc phô tô để lưu lại phục vụ việc điều tra tai nạn hàng** → `KHOAN` (span: `[14:80]`)
- `[e6]` **Cảng vụ hàng hải** → `CO_QUAN_THAM_QUYEN` (span: `[30:32]`) *(lồng trong `e5` (`KHOAN`))*
- `[e7]` **cơ quan điều tra** → `CO_QUAN_THAM_QUYEN` (span: `[34:36]`) *(lồng trong `e5` (`KHOAN`))*
- `[e8]` **cơ quan điều tra** → `CO_QUAN_THAM_QUYEN` (span: `[54:56]`) *(lồng trong `e5` (`KHOAN`))*
- `[e9]` **Giám đốc** → `CHU_THE_CA_NHAN` (span: `[29:30]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Hàng hải `[LINH_VUC]`)
- (`e4` Điều 12 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`)
- (`e5` 4 . Trong quá trình điều tra tai nạn hàng hải , nếu phát hiện có dấu hiệu cấu thành tội phạm thì Giám đốc Cảng vụ hàng hải thông báo cho cơ quan điều tra có thẩm quyền và chuyển giao hồ sơ , tài liệu , chứng cứ có liên quan đến vụ tai nạn hàng hải theo yêu cầu của cơ quan điều tra có thẩm quyền ; trước khi chuyển giao , hồ sơ , tài liệu phải được sao y hoặc phô tô để lưu lại phục vụ việc điều tra tai nạn hàng `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 12 `[DIEU]`)
- (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Hàng hải `[LINH_VUC]`)
- (`e5` 4 . Trong quá trình điều tra tai nạn hàng hải , nếu phát hiện có dấu hiệu cấu thành tội phạm thì Giám đốc Cảng vụ hàng hải thông báo cho cơ quan điều tra có thẩm quyền và chuyển giao hồ sơ , tài liệu , chứng cứ có liên quan đến vụ tai nạn hàng hải theo yêu cầu của cơ quan điều tra có thẩm quyền ; trước khi chuyển giao , hồ sơ , tài liệu phải được sao y hoặc phô tô để lưu lại phục vụ việc điều tra tai nạn hàng `[KHOAN]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Hàng hải `[LINH_VUC]`)


---

### Mẫu #01_2020_TT-BGTVT_140528#body_standalone_64 (Loại: `body_standalone`)
> **[Điều 12]`<DIEU>`** . **[4 . Trong quá trình điều tra tai nạn hàng hải , nếu phát hiện có dấu hiệu cấu thành tội phạm thì **[Giám đốc]`<CHU_THE_CA_NHAN>`** **[Cảng vụ hàng hải]`<CO_QUAN_THAM_QUYEN>`** thông báo cho **[cơ quan điều tra]`<CO_QUAN_THAM_QUYEN>`** có thẩm quyền và chuyển giao hồ sơ , tài liệu , chứng cứ có liên quan đến vụ tai nạn hàng hải theo yêu cầu của **[cơ quan điều tra]`<CO_QUAN_THAM_QUYEN>`** có thẩm quyền ; trước khi chuyển giao , hồ sơ , tài liệu phải được sao y hoặc phô tô để lưu lại phục vụ việc điều tra tai nạn hàng]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 12** → `DIEU` (span: `[0:2]`)
- `[e1]` **4 . Trong quá trình điều tra tai nạn hàng hải , nếu phát hiện có dấu hiệu cấu thành tội phạm thì Giám đốc Cảng vụ hàng hải thông báo cho cơ quan điều tra có thẩm quyền và chuyển giao hồ sơ , tài liệu , chứng cứ có liên quan đến vụ tai nạn hàng hải theo yêu cầu của cơ quan điều tra có thẩm quyền ; trước khi chuyển giao , hồ sơ , tài liệu phải được sao y hoặc phô tô để lưu lại phục vụ việc điều tra tai nạn hàng** → `KHOAN` (span: `[3:69]`)
- `[e2]` **Cảng vụ hàng hải** → `CO_QUAN_THAM_QUYEN` (span: `[19:21]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **cơ quan điều tra** → `CO_QUAN_THAM_QUYEN` (span: `[23:25]`) *(lồng trong `e1` (`KHOAN`))*
- `[e4]` **cơ quan điều tra** → `CO_QUAN_THAM_QUYEN` (span: `[43:45]`) *(lồng trong `e1` (`KHOAN`))*
- `[e5]` **Giám đốc** → `CHU_THE_CA_NHAN` (span: `[18:19]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 4 . Trong quá trình điều tra tai nạn hàng hải , nếu phát hiện có dấu hiệu cấu thành tội phạm thì Giám đốc Cảng vụ hàng hải thông báo cho cơ quan điều tra có thẩm quyền và chuyển giao hồ sơ , tài liệu , chứng cứ có liên quan đến vụ tai nạn hàng hải theo yêu cầu của cơ quan điều tra có thẩm quyền ; trước khi chuyển giao , hồ sơ , tài liệu phải được sao y hoặc phô tô để lưu lại phục vụ việc điều tra tai nạn hàng `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 12 `[DIEU]`)


---

### Mẫu #01_2020_TT-BGTVT_140528#body_context_65 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[01/2020/TT-BGTVT]`<SO_HIEU>`** của **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Hàng hải]`<LINH_VUC>`** . **[Điều 12]`<DIEU>`** . **[6 . Cục Hàng hải Việt Nam thông báo cho các chính quyền hàng hải của quốc gia tàu mang cờ về việc điều tra tai nạn hàng hải đối với các tàu nước ngoài **[quy định tại]`<TU_KHOA_PHAP_LY>`** **[khoản 1 Điều 2 của Thông tư này]`<THAM_CHIEU_PHAP_LY>`** .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **01/2020/TT-BGTVT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[4:7]`)
- `[e3]` **Hàng hải** → `LINH_VUC` (span: `[9:10]`)
- `[e4]` **Điều 12** → `DIEU` (span: `[11:13]`)
- `[e5]` **6 . Cục Hàng hải Việt Nam thông báo cho các chính quyền hàng hải của quốc gia tàu mang cờ về việc điều tra tai nạn hàng hải đối với các tàu nước ngoài quy định tại khoản 1 Điều 2 của Thông tư này .** → `KHOAN` (span: `[14:48]`)
- `[e6]` **khoản 1 Điều 2 của Thông tư này** → `THAM_CHIEU_PHAP_LY` (span: `[40:47]`) *(lồng trong `e5` (`KHOAN`))*
- `[e7]` **quy định tại** → `TU_KHOA_PHAP_LY` (span: `[38:40]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Hàng hải `[LINH_VUC]`)
- (`e4` Điều 12 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`)
- (`e5` 6 . Cục Hàng hải Việt Nam thông báo cho các chính quyền hàng hải của quốc gia tàu mang cờ về việc điều tra tai nạn hàng hải đối với các tàu nước ngoài quy định tại khoản 1 Điều 2 của Thông tư này . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 12 `[DIEU]`)
- (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Hàng hải `[LINH_VUC]`)
- (`e5` 6 . Cục Hàng hải Việt Nam thông báo cho các chính quyền hàng hải của quốc gia tàu mang cờ về việc điều tra tai nạn hàng hải đối với các tàu nước ngoài quy định tại khoản 1 Điều 2 của Thông tư này . `[KHOAN]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Hàng hải `[LINH_VUC]`)
- (`e7` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e6` khoản 1 Điều 2 của Thông tư này `[THAM_CHIEU_PHAP_LY]`)
- (`e5` 6 . Cục Hàng hải Việt Nam thông báo cho các chính quyền hàng hải của quốc gia tàu mang cờ về việc điều tra tai nạn hàng hải đối với các tàu nước ngoài quy định tại khoản 1 Điều 2 của Thông tư này . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e6` khoản 1 Điều 2 của Thông tư này `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #01_2020_TT-BGTVT_140528#body_standalone_66 (Loại: `body_standalone`)
> **[Điều 12]`<DIEU>`** . **[6 . Cục Hàng hải Việt Nam thông báo cho các chính quyền hàng hải của quốc gia tàu mang cờ về việc điều tra tai nạn hàng hải đối với các tàu nước ngoài **[quy định tại]`<TU_KHOA_PHAP_LY>`** **[khoản 1 Điều 2 của Thông tư này]`<THAM_CHIEU_PHAP_LY>`** .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 12** → `DIEU` (span: `[0:2]`)
- `[e1]` **6 . Cục Hàng hải Việt Nam thông báo cho các chính quyền hàng hải của quốc gia tàu mang cờ về việc điều tra tai nạn hàng hải đối với các tàu nước ngoài quy định tại khoản 1 Điều 2 của Thông tư này .** → `KHOAN` (span: `[3:37]`)
- `[e2]` **khoản 1 Điều 2 của Thông tư này** → `THAM_CHIEU_PHAP_LY` (span: `[29:36]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **quy định tại** → `TU_KHOA_PHAP_LY` (span: `[27:29]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 6 . Cục Hàng hải Việt Nam thông báo cho các chính quyền hàng hải của quốc gia tàu mang cờ về việc điều tra tai nạn hàng hải đối với các tàu nước ngoài quy định tại khoản 1 Điều 2 của Thông tư này . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 12 `[DIEU]`)
- (`e3` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e2` khoản 1 Điều 2 của Thông tư này `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 6 . Cục Hàng hải Việt Nam thông báo cho các chính quyền hàng hải của quốc gia tàu mang cờ về việc điều tra tai nạn hàng hải đối với các tàu nước ngoài quy định tại khoản 1 Điều 2 của Thông tư này . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e2` khoản 1 Điều 2 của Thông tư này `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #01_2020_TT-BGTVT_140528#body_context_67 (Loại: `body_context`)
> **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[01/2020/TT-BGTVT]`<SO_HIEU>`** . **[Điều 12]`<DIEU>`** . **[7 . **[Giám đốc]`<CHU_THE_CA_NHAN>`** **[Cảng vụ hàng hải]`<CO_QUAN_THAM_QUYEN>`** được tạm giữ **[tàu biển]`<TAI_SAN_VAT_CHAT>`** **[không quá 05 ngày]`<THOI_HAN>`** để thu thập chứng cứ phục vụ công tác điều tra . Việc tạm giữ quá thời hạn trên trong trường hợp tai nạn xảy ra trong vùng nước cảng biển sẽ do Cục trưởng Cục Hàng hải Việt Nam quyết định trên cơ sở đề nghị của **[Giám đốc]`<CHU_THE_CA_NHAN>`** **[Cảng vụ hàng hải]`<CO_QUAN_THAM_QUYEN>`** , thời gian gia hạn tạm giữ **[không quá 05 ngày]`<THOI_HAN>`** ; trường hợp tai nạn xảy ra ngoài vùng nước cảng biển thì thời]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[4:5]`)
- `[e1]` **01/2020/TT-BGTVT** → `SO_HIEU` (span: `[6:7]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[0:3]`)
- `[e3]` **Điều 12** → `DIEU` (span: `[8:10]`)
- `[e4]` **7 . Giám đốc Cảng vụ hàng hải được tạm giữ tàu biển không quá 05 ngày để thu thập chứng cứ phục vụ công tác điều tra . Việc tạm giữ quá thời hạn trên trong trường hợp tai nạn xảy ra trong vùng nước cảng biển sẽ do Cục trưởng Cục Hàng hải Việt Nam quyết định trên cơ sở đề nghị của Giám đốc Cảng vụ hàng hải , thời gian gia hạn tạm giữ không quá 05 ngày ; trường hợp tai nạn xảy ra ngoài vùng nước cảng biển thì thời** → `KHOAN` (span: `[11:82]`)
- `[e5]` **không quá 05 ngày** → `THOI_HAN` (span: `[20:24]`) *(lồng trong `e4` (`KHOAN`))*
- `[e6]` **không quá 05 ngày** → `THOI_HAN` (span: `[66:70]`) *(lồng trong `e4` (`KHOAN`))*
- `[e7]` **Cảng vụ hàng hải** → `CO_QUAN_THAM_QUYEN` (span: `[14:16]`) *(lồng trong `e4` (`KHOAN`))*
- `[e8]` **Cảng vụ hàng hải** → `CO_QUAN_THAM_QUYEN` (span: `[59:61]`) *(lồng trong `e4` (`KHOAN`))*
- `[e9]` **Giám đốc** → `CHU_THE_CA_NHAN` (span: `[13:14]`) *(lồng trong `e4` (`KHOAN`))*
- `[e10]` **Giám đốc** → `CHU_THE_CA_NHAN` (span: `[58:59]`) *(lồng trong `e4` (`KHOAN`))*
- `[e11]` **tàu biển** → `TAI_SAN_VAT_CHAT` (span: `[19:20]`) *(lồng trong `e4` (`KHOAN`))*

**Quan hệ:**
- (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 12 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`)
- (`e4` 7 . Giám đốc Cảng vụ hàng hải được tạm giữ tàu biển không quá 05 ngày để thu thập chứng cứ phục vụ công tác điều tra . Việc tạm giữ quá thời hạn trên trong trường hợp tai nạn xảy ra trong vùng nước cảng biển sẽ do Cục trưởng Cục Hàng hải Việt Nam quyết định trên cơ sở đề nghị của Giám đốc Cảng vụ hàng hải , thời gian gia hạn tạm giữ không quá 05 ngày ; trường hợp tai nạn xảy ra ngoài vùng nước cảng biển thì thời `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 12 `[DIEU]`)


---

### Mẫu #01_2020_TT-BGTVT_140528#body_standalone_68 (Loại: `body_standalone`)
> **[Điều 12]`<DIEU>`** . **[7 . **[Giám đốc]`<CHU_THE_CA_NHAN>`** **[Cảng vụ hàng hải]`<CO_QUAN_THAM_QUYEN>`** được tạm giữ **[tàu biển]`<TAI_SAN_VAT_CHAT>`** **[không quá 05 ngày]`<THOI_HAN>`** để thu thập chứng cứ phục vụ công tác điều tra . Việc tạm giữ quá thời hạn trên trong trường hợp tai nạn xảy ra trong vùng nước cảng biển sẽ do Cục trưởng Cục Hàng hải Việt Nam quyết định trên cơ sở đề nghị của **[Giám đốc]`<CHU_THE_CA_NHAN>`** **[Cảng vụ hàng hải]`<CO_QUAN_THAM_QUYEN>`** , thời gian gia hạn tạm giữ **[không quá 05 ngày]`<THOI_HAN>`** ; trường hợp tai nạn xảy ra ngoài vùng nước cảng biển thì thời]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 12** → `DIEU` (span: `[0:2]`)
- `[e1]` **7 . Giám đốc Cảng vụ hàng hải được tạm giữ tàu biển không quá 05 ngày để thu thập chứng cứ phục vụ công tác điều tra . Việc tạm giữ quá thời hạn trên trong trường hợp tai nạn xảy ra trong vùng nước cảng biển sẽ do Cục trưởng Cục Hàng hải Việt Nam quyết định trên cơ sở đề nghị của Giám đốc Cảng vụ hàng hải , thời gian gia hạn tạm giữ không quá 05 ngày ; trường hợp tai nạn xảy ra ngoài vùng nước cảng biển thì thời** → `KHOAN` (span: `[3:74]`)
- `[e2]` **không quá 05 ngày** → `THOI_HAN` (span: `[12:16]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **không quá 05 ngày** → `THOI_HAN` (span: `[58:62]`) *(lồng trong `e1` (`KHOAN`))*
- `[e4]` **Cảng vụ hàng hải** → `CO_QUAN_THAM_QUYEN` (span: `[6:8]`) *(lồng trong `e1` (`KHOAN`))*
- `[e5]` **Cảng vụ hàng hải** → `CO_QUAN_THAM_QUYEN` (span: `[51:53]`) *(lồng trong `e1` (`KHOAN`))*
- `[e6]` **Giám đốc** → `CHU_THE_CA_NHAN` (span: `[5:6]`) *(lồng trong `e1` (`KHOAN`))*
- `[e7]` **Giám đốc** → `CHU_THE_CA_NHAN` (span: `[50:51]`) *(lồng trong `e1` (`KHOAN`))*
- `[e8]` **tàu biển** → `TAI_SAN_VAT_CHAT` (span: `[11:12]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 7 . Giám đốc Cảng vụ hàng hải được tạm giữ tàu biển không quá 05 ngày để thu thập chứng cứ phục vụ công tác điều tra . Việc tạm giữ quá thời hạn trên trong trường hợp tai nạn xảy ra trong vùng nước cảng biển sẽ do Cục trưởng Cục Hàng hải Việt Nam quyết định trên cơ sở đề nghị của Giám đốc Cảng vụ hàng hải , thời gian gia hạn tạm giữ không quá 05 ngày ; trường hợp tai nạn xảy ra ngoài vùng nước cảng biển thì thời `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 12 `[DIEU]`)


---

### Mẫu #01_2020_TT-BGTVT_140528#body_context_69 (Loại: `body_context`)
> **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[01/2020/TT-BGTVT]`<SO_HIEU>`** . **[Điều 13 . Thỏa thuận điều tra tai nạn hàng hải . Trong trường hợp cần thiết , Cục Hàng hải Việt Nam thỏa thuận điều tra tai nạn hàng hải như sau :]`<DIEU>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[4:5]`)
- `[e1]` **01/2020/TT-BGTVT** → `SO_HIEU` (span: `[6:7]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[0:3]`)
- `[e3]` **Điều 13 . Thỏa thuận điều tra tai nạn hàng hải . Trong trường hợp cần thiết , Cục Hàng hải Việt Nam thỏa thuận điều tra tai nạn hàng hải như sau :** → `DIEU` (span: `[8:30]`)

**Quan hệ:**
- (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 13 . Thỏa thuận điều tra tai nạn hàng hải . Trong trường hợp cần thiết , Cục Hàng hải Việt Nam thỏa thuận điều tra tai nạn hàng hải như sau : `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`)


---

### Mẫu #01_2020_TT-BGTVT_140528#body_context_70 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[01/2020/TT-BGTVT]`<SO_HIEU>`** ban hành **[ngày 20 tháng 01 năm 2020]`<NGAY_BAN_HANH>`** bởi **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** . **[Điều 14]`<DIEU>`** . **[Khoản 1]`<KHOAN>`** . **[a ) Tổ điều tra tai nạn hàng hải phải có Tổ trưởng trực tiếp điều hành và tối thiểu phải có 01 Tổ phó giúp việc cho Tổ trưởng , 01 tổ viên do **[Giám đốc]`<CHU_THE_CA_NHAN>`** **[Cảng vụ hàng hải]`<CO_QUAN_THAM_QUYEN>`** quyết định theo thẩm quyền ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **01/2020/TT-BGTVT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[11:14]`)
- `[e3]` **ngày 20 tháng 01 năm 2020** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 14** → `DIEU` (span: `[15:17]`)
- `[e5]` **Khoản 1** → `KHOAN` (span: `[18:20]`)
- `[e6]` **a ) Tổ điều tra tai nạn hàng hải phải có Tổ trưởng trực tiếp điều hành và tối thiểu phải có 01 Tổ phó giúp việc cho Tổ trưởng , 01 tổ viên do Giám đốc Cảng vụ hàng hải quyết định theo thẩm quyền ;** → `DIEM` (span: `[21:52]`)
- `[e7]` **Cảng vụ hàng hải** → `CO_QUAN_THAM_QUYEN` (span: `[46:48]`) *(lồng trong `e6` (`DIEM`))*
- `[e8]` **Giám đốc** → `CHU_THE_CA_NHAN` (span: `[45:46]`) *(lồng trong `e6` (`DIEM`))*

**Quan hệ:**
- (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 20 tháng 01 năm 2020 `[NGAY_BAN_HANH]`)
- (`e4` Điều 14 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`)
- (`e5` Khoản 1 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 14 `[DIEU]`)
- (`e6` a ) Tổ điều tra tai nạn hàng hải phải có Tổ trưởng trực tiếp điều hành và tối thiểu phải có 01 Tổ phó giúp việc cho Tổ trưởng , 01 tổ viên do Giám đốc Cảng vụ hàng hải quyết định theo thẩm quyền ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e5` Khoản 1 `[KHOAN]`)


---

### Mẫu #01_2020_TT-BGTVT_140528#body_standalone_71 (Loại: `body_standalone`)
> **[Điều 14]`<DIEU>`** . **[Khoản 1]`<KHOAN>`** . **[a ) Tổ điều tra tai nạn hàng hải phải có Tổ trưởng trực tiếp điều hành và tối thiểu phải có 01 Tổ phó giúp việc cho Tổ trưởng , 01 tổ viên do **[Giám đốc]`<CHU_THE_CA_NHAN>`** **[Cảng vụ hàng hải]`<CO_QUAN_THAM_QUYEN>`** quyết định theo thẩm quyền ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Điều 14** → `DIEU` (span: `[0:2]`)
- `[e1]` **Khoản 1** → `KHOAN` (span: `[3:5]`)
- `[e2]` **a ) Tổ điều tra tai nạn hàng hải phải có Tổ trưởng trực tiếp điều hành và tối thiểu phải có 01 Tổ phó giúp việc cho Tổ trưởng , 01 tổ viên do Giám đốc Cảng vụ hàng hải quyết định theo thẩm quyền ;** → `DIEM` (span: `[6:37]`)
- `[e3]` **Cảng vụ hàng hải** → `CO_QUAN_THAM_QUYEN` (span: `[31:33]`) *(lồng trong `e2` (`DIEM`))*
- `[e4]` **Giám đốc** → `CHU_THE_CA_NHAN` (span: `[30:31]`) *(lồng trong `e2` (`DIEM`))*

**Quan hệ:**
- (`e1` Khoản 1 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 14 `[DIEU]`)
- (`e2` a ) Tổ điều tra tai nạn hàng hải phải có Tổ trưởng trực tiếp điều hành và tối thiểu phải có 01 Tổ phó giúp việc cho Tổ trưởng , 01 tổ viên do Giám đốc Cảng vụ hàng hải quyết định theo thẩm quyền ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e1` Khoản 1 `[KHOAN]`)


---

### Mẫu #01_2020_TT-BGTVT_140528#body_context_72 (Loại: `body_context`)
> **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[01/2020/TT-BGTVT]`<SO_HIEU>`** . **[Điều 14]`<DIEU>`** . **[Khoản 1]`<KHOAN>`** . **[b ) Trong trường hợp cần thiết , Cục trưởng Cục Hàng hải Việt Nam bổ sung người có chuyên môn phù hợp cùng tham gia Tổ điều tra tai nạn hàng hải . **[Giám đốc]`<CHU_THE_CA_NHAN>`** **[Cảng vụ hàng hải]`<CO_QUAN_THAM_QUYEN>`** căn cứ chỉ đạo của Cục trưởng Cục Hàng hải Việt Nam để **[quyết định thành lập]`<GIAY_TO_HO_SO>`** Tổ điều tra tai nạn hàng hải .]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[4:5]`)
- `[e1]` **01/2020/TT-BGTVT** → `SO_HIEU` (span: `[6:7]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[0:3]`)
- `[e3]` **Điều 14** → `DIEU` (span: `[8:10]`)
- `[e4]` **Khoản 1** → `KHOAN` (span: `[11:13]`)
- `[e5]` **b ) Trong trường hợp cần thiết , Cục trưởng Cục Hàng hải Việt Nam bổ sung người có chuyên môn phù hợp cùng tham gia Tổ điều tra tai nạn hàng hải . Giám đốc Cảng vụ hàng hải căn cứ chỉ đạo của Cục trưởng Cục Hàng hải Việt Nam để quyết định thành lập Tổ điều tra tai nạn hàng hải .** → `DIEM` (span: `[14:54]`)
- `[e6]` **Cảng vụ hàng hải** → `CO_QUAN_THAM_QUYEN` (span: `[37:39]`) *(lồng trong `e5` (`DIEM`))*
- `[e7]` **quyết định thành lập** → `GIAY_TO_HO_SO` (span: `[47:49]`) *(lồng trong `e5` (`DIEM`))*
- `[e8]` **Giám đốc** → `CHU_THE_CA_NHAN` (span: `[36:37]`) *(lồng trong `e5` (`DIEM`))*

**Quan hệ:**
- (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 14 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`)
- (`e4` Khoản 1 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 14 `[DIEU]`)
- (`e5` b ) Trong trường hợp cần thiết , Cục trưởng Cục Hàng hải Việt Nam bổ sung người có chuyên môn phù hợp cùng tham gia Tổ điều tra tai nạn hàng hải . Giám đốc Cảng vụ hàng hải căn cứ chỉ đạo của Cục trưởng Cục Hàng hải Việt Nam để quyết định thành lập Tổ điều tra tai nạn hàng hải . `[DIEM]`) ==[ **THUOC_VE** ]==> (`e4` Khoản 1 `[KHOAN]`)


---

### Mẫu #01_2020_TT-BGTVT_140528#body_standalone_73 (Loại: `body_standalone`)
> **[Điều 14]`<DIEU>`** . **[Khoản 1]`<KHOAN>`** . **[b ) Trong trường hợp cần thiết , Cục trưởng Cục Hàng hải Việt Nam bổ sung người có chuyên môn phù hợp cùng tham gia Tổ điều tra tai nạn hàng hải . **[Giám đốc]`<CHU_THE_CA_NHAN>`** **[Cảng vụ hàng hải]`<CO_QUAN_THAM_QUYEN>`** căn cứ chỉ đạo của Cục trưởng Cục Hàng hải Việt Nam để **[quyết định thành lập]`<GIAY_TO_HO_SO>`** Tổ điều tra tai nạn hàng hải .]`<DIEM>`**

**Thực thể:**
- `[e0]` **Điều 14** → `DIEU` (span: `[0:2]`)
- `[e1]` **Khoản 1** → `KHOAN` (span: `[3:5]`)
- `[e2]` **b ) Trong trường hợp cần thiết , Cục trưởng Cục Hàng hải Việt Nam bổ sung người có chuyên môn phù hợp cùng tham gia Tổ điều tra tai nạn hàng hải . Giám đốc Cảng vụ hàng hải căn cứ chỉ đạo của Cục trưởng Cục Hàng hải Việt Nam để quyết định thành lập Tổ điều tra tai nạn hàng hải .** → `DIEM` (span: `[6:46]`)
- `[e3]` **Cảng vụ hàng hải** → `CO_QUAN_THAM_QUYEN` (span: `[29:31]`) *(lồng trong `e2` (`DIEM`))*
- `[e4]` **quyết định thành lập** → `GIAY_TO_HO_SO` (span: `[39:41]`) *(lồng trong `e2` (`DIEM`))*
- `[e5]` **Giám đốc** → `CHU_THE_CA_NHAN` (span: `[28:29]`) *(lồng trong `e2` (`DIEM`))*

**Quan hệ:**
- (`e1` Khoản 1 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 14 `[DIEU]`)
- (`e2` b ) Trong trường hợp cần thiết , Cục trưởng Cục Hàng hải Việt Nam bổ sung người có chuyên môn phù hợp cùng tham gia Tổ điều tra tai nạn hàng hải . Giám đốc Cảng vụ hàng hải căn cứ chỉ đạo của Cục trưởng Cục Hàng hải Việt Nam để quyết định thành lập Tổ điều tra tai nạn hàng hải . `[DIEM]`) ==[ **THUOC_VE** ]==> (`e1` Khoản 1 `[KHOAN]`)


---

### Mẫu #01_2020_TT-BGTVT_140528#body_context_74 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[01/2020/TT-BGTVT]`<SO_HIEU>`** của **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Hàng hải]`<LINH_VUC>`** . **[Điều 14]`<DIEU>`** . **[2 . Thành viên Tổ điều tra tai nạn hàng hải phải đáp ứng các điều kiện sau : là thuyền trưởng , máy trưởng hoặc kỹ sư các chuyên ngành điều khiển **[tàu biển]`<TAI_SAN_VAT_CHAT>`** , vận hành máy **[tàu biển]`<TAI_SAN_VAT_CHAT>`** , khai thác máy **[tàu biển]`<TAI_SAN_VAT_CHAT>`** , đóng tàu , điện và điện tự động tàu thủy , luật hàng hải hoặc ngành nghề tương đương ; có thời gian kinh nghiệm thực tế với ngành nghề đã học **[tối thiểu 05 năm]`<THOI_HAN>`** và đã qua các khóa tập huấn , bồi dưỡng nghiệp vụ về điều tra tai nạn hàng]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **01/2020/TT-BGTVT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[4:7]`)
- `[e3]` **Hàng hải** → `LINH_VUC` (span: `[9:10]`)
- `[e4]` **Điều 14** → `DIEU` (span: `[11:13]`)
- `[e5]` **2 . Thành viên Tổ điều tra tai nạn hàng hải phải đáp ứng các điều kiện sau : là thuyền trưởng , máy trưởng hoặc kỹ sư các chuyên ngành điều khiển tàu biển , vận hành máy tàu biển , khai thác máy tàu biển , đóng tàu , điện và điện tự động tàu thủy , luật hàng hải hoặc ngành nghề tương đương ; có thời gian kinh nghiệm thực tế với ngành nghề đã học tối thiểu 05 năm và đã qua các khóa tập huấn , bồi dưỡng nghiệp vụ về điều tra tai nạn hàng** → `KHOAN` (span: `[14:87]`)
- `[e6]` **tối thiểu 05 năm** → `THOI_HAN` (span: `[71:74]`) *(lồng trong `e5` (`KHOAN`))*
- `[e7]` **tàu biển** → `TAI_SAN_VAT_CHAT` (span: `[37:38]`) *(lồng trong `e5` (`KHOAN`))*
- `[e8]` **tàu biển** → `TAI_SAN_VAT_CHAT` (span: `[41:42]`) *(lồng trong `e5` (`KHOAN`))*
- `[e9]` **tàu biển** → `TAI_SAN_VAT_CHAT` (span: `[45:46]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Hàng hải `[LINH_VUC]`)
- (`e4` Điều 14 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`)
- (`e5` 2 . Thành viên Tổ điều tra tai nạn hàng hải phải đáp ứng các điều kiện sau : là thuyền trưởng , máy trưởng hoặc kỹ sư các chuyên ngành điều khiển tàu biển , vận hành máy tàu biển , khai thác máy tàu biển , đóng tàu , điện và điện tự động tàu thủy , luật hàng hải hoặc ngành nghề tương đương ; có thời gian kinh nghiệm thực tế với ngành nghề đã học tối thiểu 05 năm và đã qua các khóa tập huấn , bồi dưỡng nghiệp vụ về điều tra tai nạn hàng `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 14 `[DIEU]`)
- (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Hàng hải `[LINH_VUC]`)
- (`e5` 2 . Thành viên Tổ điều tra tai nạn hàng hải phải đáp ứng các điều kiện sau : là thuyền trưởng , máy trưởng hoặc kỹ sư các chuyên ngành điều khiển tàu biển , vận hành máy tàu biển , khai thác máy tàu biển , đóng tàu , điện và điện tự động tàu thủy , luật hàng hải hoặc ngành nghề tương đương ; có thời gian kinh nghiệm thực tế với ngành nghề đã học tối thiểu 05 năm và đã qua các khóa tập huấn , bồi dưỡng nghiệp vụ về điều tra tai nạn hàng `[KHOAN]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Hàng hải `[LINH_VUC]`)


---

### Mẫu #01_2020_TT-BGTVT_140528#body_standalone_75 (Loại: `body_standalone`)
> **[Điều 14]`<DIEU>`** . **[2 . Thành viên Tổ điều tra tai nạn hàng hải phải đáp ứng các điều kiện sau : là thuyền trưởng , máy trưởng hoặc kỹ sư các chuyên ngành điều khiển **[tàu biển]`<TAI_SAN_VAT_CHAT>`** , vận hành máy **[tàu biển]`<TAI_SAN_VAT_CHAT>`** , khai thác máy **[tàu biển]`<TAI_SAN_VAT_CHAT>`** , đóng tàu , điện và điện tự động tàu thủy , luật hàng hải hoặc ngành nghề tương đương ; có thời gian kinh nghiệm thực tế với ngành nghề đã học **[tối thiểu 05 năm]`<THOI_HAN>`** và đã qua các khóa tập huấn , bồi dưỡng nghiệp vụ về điều tra tai nạn hàng]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 14** → `DIEU` (span: `[0:2]`)
- `[e1]` **2 . Thành viên Tổ điều tra tai nạn hàng hải phải đáp ứng các điều kiện sau : là thuyền trưởng , máy trưởng hoặc kỹ sư các chuyên ngành điều khiển tàu biển , vận hành máy tàu biển , khai thác máy tàu biển , đóng tàu , điện và điện tự động tàu thủy , luật hàng hải hoặc ngành nghề tương đương ; có thời gian kinh nghiệm thực tế với ngành nghề đã học tối thiểu 05 năm và đã qua các khóa tập huấn , bồi dưỡng nghiệp vụ về điều tra tai nạn hàng** → `KHOAN` (span: `[3:76]`)
- `[e2]` **tối thiểu 05 năm** → `THOI_HAN` (span: `[60:63]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **tàu biển** → `TAI_SAN_VAT_CHAT` (span: `[26:27]`) *(lồng trong `e1` (`KHOAN`))*
- `[e4]` **tàu biển** → `TAI_SAN_VAT_CHAT` (span: `[30:31]`) *(lồng trong `e1` (`KHOAN`))*
- `[e5]` **tàu biển** → `TAI_SAN_VAT_CHAT` (span: `[34:35]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 2 . Thành viên Tổ điều tra tai nạn hàng hải phải đáp ứng các điều kiện sau : là thuyền trưởng , máy trưởng hoặc kỹ sư các chuyên ngành điều khiển tàu biển , vận hành máy tàu biển , khai thác máy tàu biển , đóng tàu , điện và điện tự động tàu thủy , luật hàng hải hoặc ngành nghề tương đương ; có thời gian kinh nghiệm thực tế với ngành nghề đã học tối thiểu 05 năm và đã qua các khóa tập huấn , bồi dưỡng nghiệp vụ về điều tra tai nạn hàng `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 14 `[DIEU]`)


---

### Mẫu #01_2020_TT-BGTVT_140528#body_context_76 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[01/2020/TT-BGTVT]`<SO_HIEU>`** của **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Hàng hải]`<LINH_VUC>`** . **[Điều 15]`<DIEU>`** . **[1 . Lập kế hoạch điều tra , xây dựng dự toán kinh phí điều tra thực hiện điều tra tai nạn hàng hải theo quy định của Thông tư này và các quy định có liên quan khác của pháp luật . Kế hoạch điều tra phải được **[Giám đốc]`<CHU_THE_CA_NHAN>`** **[Cảng vụ hàng hải]`<CO_QUAN_THAM_QUYEN>`** phê duyệt . Báo cáo bằng văn bản về quá trình điều tra và kết quả điều tra tai nạn hàng hải cho **[Giám đốc]`<CHU_THE_CA_NHAN>`** **[Cảng vụ hàng hải]`<CO_QUAN_THAM_QUYEN>`** thành lập Tổ điều tra tai nạn hàng hải .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **01/2020/TT-BGTVT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[4:7]`)
- `[e3]` **Hàng hải** → `LINH_VUC` (span: `[9:10]`)
- `[e4]` **Điều 15** → `DIEU` (span: `[11:13]`)
- `[e5]` **1 . Lập kế hoạch điều tra , xây dựng dự toán kinh phí điều tra thực hiện điều tra tai nạn hàng hải theo quy định của Thông tư này và các quy định có liên quan khác của pháp luật . Kế hoạch điều tra phải được Giám đốc Cảng vụ hàng hải phê duyệt . Báo cáo bằng văn bản về quá trình điều tra và kết quả điều tra tai nạn hàng hải cho Giám đốc Cảng vụ hàng hải thành lập Tổ điều tra tai nạn hàng hải .** → `KHOAN` (span: `[14:72]`)
- `[e6]` **Cảng vụ hàng hải** → `CO_QUAN_THAM_QUYEN` (span: `[47:49]`) *(lồng trong `e5` (`KHOAN`))*
- `[e7]` **Cảng vụ hàng hải** → `CO_QUAN_THAM_QUYEN` (span: `[64:66]`) *(lồng trong `e5` (`KHOAN`))*
- `[e8]` **Giám đốc** → `CHU_THE_CA_NHAN` (span: `[46:47]`) *(lồng trong `e5` (`KHOAN`))*
- `[e9]` **Giám đốc** → `CHU_THE_CA_NHAN` (span: `[63:64]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Hàng hải `[LINH_VUC]`)
- (`e4` Điều 15 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`)
- (`e5` 1 . Lập kế hoạch điều tra , xây dựng dự toán kinh phí điều tra thực hiện điều tra tai nạn hàng hải theo quy định của Thông tư này và các quy định có liên quan khác của pháp luật . Kế hoạch điều tra phải được Giám đốc Cảng vụ hàng hải phê duyệt . Báo cáo bằng văn bản về quá trình điều tra và kết quả điều tra tai nạn hàng hải cho Giám đốc Cảng vụ hàng hải thành lập Tổ điều tra tai nạn hàng hải . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 15 `[DIEU]`)
- (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Hàng hải `[LINH_VUC]`)
- (`e5` 1 . Lập kế hoạch điều tra , xây dựng dự toán kinh phí điều tra thực hiện điều tra tai nạn hàng hải theo quy định của Thông tư này và các quy định có liên quan khác của pháp luật . Kế hoạch điều tra phải được Giám đốc Cảng vụ hàng hải phê duyệt . Báo cáo bằng văn bản về quá trình điều tra và kết quả điều tra tai nạn hàng hải cho Giám đốc Cảng vụ hàng hải thành lập Tổ điều tra tai nạn hàng hải . `[KHOAN]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Hàng hải `[LINH_VUC]`)


---

### Mẫu #01_2020_TT-BGTVT_140528#body_standalone_77 (Loại: `body_standalone`)
> **[Điều 15]`<DIEU>`** . **[1 . Lập kế hoạch điều tra , xây dựng dự toán kinh phí điều tra thực hiện điều tra tai nạn hàng hải theo quy định của Thông tư này và các quy định có liên quan khác của pháp luật . Kế hoạch điều tra phải được **[Giám đốc]`<CHU_THE_CA_NHAN>`** **[Cảng vụ hàng hải]`<CO_QUAN_THAM_QUYEN>`** phê duyệt . Báo cáo bằng văn bản về quá trình điều tra và kết quả điều tra tai nạn hàng hải cho **[Giám đốc]`<CHU_THE_CA_NHAN>`** **[Cảng vụ hàng hải]`<CO_QUAN_THAM_QUYEN>`** thành lập Tổ điều tra tai nạn hàng hải .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 15** → `DIEU` (span: `[0:2]`)
- `[e1]` **1 . Lập kế hoạch điều tra , xây dựng dự toán kinh phí điều tra thực hiện điều tra tai nạn hàng hải theo quy định của Thông tư này và các quy định có liên quan khác của pháp luật . Kế hoạch điều tra phải được Giám đốc Cảng vụ hàng hải phê duyệt . Báo cáo bằng văn bản về quá trình điều tra và kết quả điều tra tai nạn hàng hải cho Giám đốc Cảng vụ hàng hải thành lập Tổ điều tra tai nạn hàng hải .** → `KHOAN` (span: `[3:61]`)
- `[e2]` **Cảng vụ hàng hải** → `CO_QUAN_THAM_QUYEN` (span: `[36:38]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **Cảng vụ hàng hải** → `CO_QUAN_THAM_QUYEN` (span: `[53:55]`) *(lồng trong `e1` (`KHOAN`))*
- `[e4]` **Giám đốc** → `CHU_THE_CA_NHAN` (span: `[35:36]`) *(lồng trong `e1` (`KHOAN`))*
- `[e5]` **Giám đốc** → `CHU_THE_CA_NHAN` (span: `[52:53]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 1 . Lập kế hoạch điều tra , xây dựng dự toán kinh phí điều tra thực hiện điều tra tai nạn hàng hải theo quy định của Thông tư này và các quy định có liên quan khác của pháp luật . Kế hoạch điều tra phải được Giám đốc Cảng vụ hàng hải phê duyệt . Báo cáo bằng văn bản về quá trình điều tra và kết quả điều tra tai nạn hàng hải cho Giám đốc Cảng vụ hàng hải thành lập Tổ điều tra tai nạn hàng hải . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 15 `[DIEU]`)


---

### Mẫu #01_2020_TT-BGTVT_140528#body_context_78 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[01/2020/TT-BGTVT]`<SO_HIEU>`** của **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Hàng hải]`<LINH_VUC>`** . **[Điều 15]`<DIEU>`** . **[2 . **[Thông báo bằng văn bản]`<GIAY_TO_HO_SO>`** cho thuyền trưởng hoặc người có trách nhiệm cao nhất trên **[tàu biển]`<TAI_SAN_VAT_CHAT>`** , chủ tàu và đại lý **[tàu biển]`<TAI_SAN_VAT_CHAT>`** về việc tiến hành điều tra tai nạn hàng hải , Nội dung thông báo bao gồm những thông tin chính sau đây :]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **01/2020/TT-BGTVT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[4:7]`)
- `[e3]` **Hàng hải** → `LINH_VUC` (span: `[9:10]`)
- `[e4]` **Điều 15** → `DIEU` (span: `[11:13]`)
- `[e5]` **2 . Thông báo bằng văn bản cho thuyền trưởng hoặc người có trách nhiệm cao nhất trên tàu biển , chủ tàu và đại lý tàu biển về việc tiến hành điều tra tai nạn hàng hải , Nội dung thông báo bao gồm những thông tin chính sau đây :** → `KHOAN` (span: `[14:51]`)
- `[e6]` **Thông báo bằng văn bản** → `GIAY_TO_HO_SO` (span: `[16:19]`) *(lồng trong `e5` (`KHOAN`))*
- `[e7]` **tàu biển** → `TAI_SAN_VAT_CHAT` (span: `[28:29]`) *(lồng trong `e5` (`KHOAN`))*
- `[e8]` **tàu biển** → `TAI_SAN_VAT_CHAT` (span: `[34:35]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Hàng hải `[LINH_VUC]`)
- (`e4` Điều 15 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`)
- (`e5` 2 . Thông báo bằng văn bản cho thuyền trưởng hoặc người có trách nhiệm cao nhất trên tàu biển , chủ tàu và đại lý tàu biển về việc tiến hành điều tra tai nạn hàng hải , Nội dung thông báo bao gồm những thông tin chính sau đây : `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 15 `[DIEU]`)
- (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Hàng hải `[LINH_VUC]`)
- (`e5` 2 . Thông báo bằng văn bản cho thuyền trưởng hoặc người có trách nhiệm cao nhất trên tàu biển , chủ tàu và đại lý tàu biển về việc tiến hành điều tra tai nạn hàng hải , Nội dung thông báo bao gồm những thông tin chính sau đây : `[KHOAN]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Hàng hải `[LINH_VUC]`)


---

### Mẫu #01_2020_TT-BGTVT_140528#body_standalone_79 (Loại: `body_standalone`)
> **[Điều 15]`<DIEU>`** . **[2 . **[Thông báo bằng văn bản]`<GIAY_TO_HO_SO>`** cho thuyền trưởng hoặc người có trách nhiệm cao nhất trên **[tàu biển]`<TAI_SAN_VAT_CHAT>`** , chủ tàu và đại lý **[tàu biển]`<TAI_SAN_VAT_CHAT>`** về việc tiến hành điều tra tai nạn hàng hải , Nội dung thông báo bao gồm những thông tin chính sau đây :]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 15** → `DIEU` (span: `[0:2]`)
- `[e1]` **2 . Thông báo bằng văn bản cho thuyền trưởng hoặc người có trách nhiệm cao nhất trên tàu biển , chủ tàu và đại lý tàu biển về việc tiến hành điều tra tai nạn hàng hải , Nội dung thông báo bao gồm những thông tin chính sau đây :** → `KHOAN` (span: `[3:40]`)
- `[e2]` **Thông báo bằng văn bản** → `GIAY_TO_HO_SO` (span: `[5:8]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **tàu biển** → `TAI_SAN_VAT_CHAT` (span: `[17:18]`) *(lồng trong `e1` (`KHOAN`))*
- `[e4]` **tàu biển** → `TAI_SAN_VAT_CHAT` (span: `[23:24]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 2 . Thông báo bằng văn bản cho thuyền trưởng hoặc người có trách nhiệm cao nhất trên tàu biển , chủ tàu và đại lý tàu biển về việc tiến hành điều tra tai nạn hàng hải , Nội dung thông báo bao gồm những thông tin chính sau đây : `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 15 `[DIEU]`)


---

### Mẫu #01_2020_TT-BGTVT_140528#body_context_80 (Loại: `body_context`)
> **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[01/2020/TT-BGTVT]`<SO_HIEU>`** . **[Điều 15]`<DIEU>`** . **[Khoản 2]`<KHOAN>`** . **[a ) Tai nạn hàng hải được điều tra ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[4:5]`)
- `[e1]` **01/2020/TT-BGTVT** → `SO_HIEU` (span: `[6:7]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[0:3]`)
- `[e3]` **Điều 15** → `DIEU` (span: `[8:10]`)
- `[e4]` **Khoản 2** → `KHOAN` (span: `[11:13]`)
- `[e5]` **a ) Tai nạn hàng hải được điều tra ;** → `DIEM` (span: `[14:21]`)

**Quan hệ:**
- (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 15 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`)
- (`e4` Khoản 2 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 15 `[DIEU]`)
- (`e5` a ) Tai nạn hàng hải được điều tra ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e4` Khoản 2 `[KHOAN]`)


---

### Mẫu #01_2020_TT-BGTVT_140528#body_standalone_81 (Loại: `body_standalone`)
> **[Điều 15]`<DIEU>`** . **[Khoản 2]`<KHOAN>`** . **[a ) Tai nạn hàng hải được điều tra ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Điều 15** → `DIEU` (span: `[0:2]`)
- `[e1]` **Khoản 2** → `KHOAN` (span: `[3:5]`)
- `[e2]` **a ) Tai nạn hàng hải được điều tra ;** → `DIEM` (span: `[6:13]`)

**Quan hệ:**
- (`e1` Khoản 2 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 15 `[DIEU]`)
- (`e2` a ) Tai nạn hàng hải được điều tra ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e1` Khoản 2 `[KHOAN]`)


---

### Mẫu #01_2020_TT-BGTVT_140528#body_context_82 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[01/2020/TT-BGTVT]`<SO_HIEU>`** của **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Hàng hải]`<LINH_VUC>`** . **[Điều 15]`<DIEU>`** . **[5 . Yêu cầu những người liên quan đến tai nạn hàng hải tường trình bằng văn bản những vấn đề họ biết về điều kiện , hoàn cảnh , diễn biến của tai nạn hàng hải và đối tượng liên quan đến tai nạn hàng hải . Trong trường hợp cần thiết , phải thẩm vấn những người này thì phải thông báo cho họ biết trước về thời gian , địa điểm tiến hành thẩm vấn .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **01/2020/TT-BGTVT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[4:7]`)
- `[e3]` **Hàng hải** → `LINH_VUC` (span: `[9:10]`)
- `[e4]` **Điều 15** → `DIEU` (span: `[11:13]`)
- `[e5]` **5 . Yêu cầu những người liên quan đến tai nạn hàng hải tường trình bằng văn bản những vấn đề họ biết về điều kiện , hoàn cảnh , diễn biến của tai nạn hàng hải và đối tượng liên quan đến tai nạn hàng hải . Trong trường hợp cần thiết , phải thẩm vấn những người này thì phải thông báo cho họ biết trước về thời gian , địa điểm tiến hành thẩm vấn .** → `KHOAN` (span: `[14:69]`)

**Quan hệ:**
- (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Hàng hải `[LINH_VUC]`)
- (`e4` Điều 15 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`)
- (`e5` 5 . Yêu cầu những người liên quan đến tai nạn hàng hải tường trình bằng văn bản những vấn đề họ biết về điều kiện , hoàn cảnh , diễn biến của tai nạn hàng hải và đối tượng liên quan đến tai nạn hàng hải . Trong trường hợp cần thiết , phải thẩm vấn những người này thì phải thông báo cho họ biết trước về thời gian , địa điểm tiến hành thẩm vấn . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 15 `[DIEU]`)
- (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Hàng hải `[LINH_VUC]`)
- (`e5` 5 . Yêu cầu những người liên quan đến tai nạn hàng hải tường trình bằng văn bản những vấn đề họ biết về điều kiện , hoàn cảnh , diễn biến của tai nạn hàng hải và đối tượng liên quan đến tai nạn hàng hải . Trong trường hợp cần thiết , phải thẩm vấn những người này thì phải thông báo cho họ biết trước về thời gian , địa điểm tiến hành thẩm vấn . `[KHOAN]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Hàng hải `[LINH_VUC]`)


---

### Mẫu #01_2020_TT-BGTVT_140528#body_context_83 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[01/2020/TT-BGTVT]`<SO_HIEU>`** ban hành **[ngày 20 tháng 01 năm 2020]`<NGAY_BAN_HANH>`** bởi **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** . **[Điều 15]`<DIEU>`** . **[10 . Tổng hợp , xác minh , phân tích , đánh giá và đề xuất kết luận nguyên nhân gây ra tai nạn hàng hải . Trong trường hợp cần thiết , đề xuất **[Giám đốc]`<CHU_THE_CA_NHAN>`** **[Cảng vụ hàng hải]`<CO_QUAN_THAM_QUYEN>`** quyết định trưng cầu ý kiến của tổ chức phân cấp và giám sát kỹ thuật tàu hoặc các cơ quan chuyên môn liên quan .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **01/2020/TT-BGTVT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[11:14]`)
- `[e3]` **ngày 20 tháng 01 năm 2020** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 15** → `DIEU` (span: `[15:17]`)
- `[e5]` **10 . Tổng hợp , xác minh , phân tích , đánh giá và đề xuất kết luận nguyên nhân gây ra tai nạn hàng hải . Trong trường hợp cần thiết , đề xuất Giám đốc Cảng vụ hàng hải quyết định trưng cầu ý kiến của tổ chức phân cấp và giám sát kỹ thuật tàu hoặc các cơ quan chuyên môn liên quan .** → `KHOAN` (span: `[18:60]`)
- `[e6]` **Cảng vụ hàng hải** → `CO_QUAN_THAM_QUYEN` (span: `[42:44]`) *(lồng trong `e5` (`KHOAN`))*
- `[e7]` **Giám đốc** → `CHU_THE_CA_NHAN` (span: `[41:42]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 20 tháng 01 năm 2020 `[NGAY_BAN_HANH]`)
- (`e4` Điều 15 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`)
- (`e5` 10 . Tổng hợp , xác minh , phân tích , đánh giá và đề xuất kết luận nguyên nhân gây ra tai nạn hàng hải . Trong trường hợp cần thiết , đề xuất Giám đốc Cảng vụ hàng hải quyết định trưng cầu ý kiến của tổ chức phân cấp và giám sát kỹ thuật tàu hoặc các cơ quan chuyên môn liên quan . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 15 `[DIEU]`)


---

### Mẫu #01_2020_TT-BGTVT_140528#body_standalone_84 (Loại: `body_standalone`)
> **[Điều 15]`<DIEU>`** . **[10 . Tổng hợp , xác minh , phân tích , đánh giá và đề xuất kết luận nguyên nhân gây ra tai nạn hàng hải . Trong trường hợp cần thiết , đề xuất **[Giám đốc]`<CHU_THE_CA_NHAN>`** **[Cảng vụ hàng hải]`<CO_QUAN_THAM_QUYEN>`** quyết định trưng cầu ý kiến của tổ chức phân cấp và giám sát kỹ thuật tàu hoặc các cơ quan chuyên môn liên quan .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 15** → `DIEU` (span: `[0:2]`)
- `[e1]` **10 . Tổng hợp , xác minh , phân tích , đánh giá và đề xuất kết luận nguyên nhân gây ra tai nạn hàng hải . Trong trường hợp cần thiết , đề xuất Giám đốc Cảng vụ hàng hải quyết định trưng cầu ý kiến của tổ chức phân cấp và giám sát kỹ thuật tàu hoặc các cơ quan chuyên môn liên quan .** → `KHOAN` (span: `[3:45]`)
- `[e2]` **Cảng vụ hàng hải** → `CO_QUAN_THAM_QUYEN` (span: `[27:29]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **Giám đốc** → `CHU_THE_CA_NHAN` (span: `[26:27]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 10 . Tổng hợp , xác minh , phân tích , đánh giá và đề xuất kết luận nguyên nhân gây ra tai nạn hàng hải . Trong trường hợp cần thiết , đề xuất Giám đốc Cảng vụ hàng hải quyết định trưng cầu ý kiến của tổ chức phân cấp và giám sát kỹ thuật tàu hoặc các cơ quan chuyên môn liên quan . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 15 `[DIEU]`)


---

### Mẫu #01_2020_TT-BGTVT_140528#body_context_85 (Loại: `body_context`)
> **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[01/2020/TT-BGTVT]`<SO_HIEU>`** . **[Điều 15]`<DIEU>`** . **[13 . Tổ chức dịch sang tiếng Anh Dự thảo Báo cáo điều tra tai nạn , Báo cáo điều tra tai nạn đối với các vụ tai nạn hàng hải đặc biệt nghiêm trọng và các vụ tai nạn hàng hải liên quan đến tàu mang cờ quốc tịch nước ngoài .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[4:5]`)
- `[e1]` **01/2020/TT-BGTVT** → `SO_HIEU` (span: `[6:7]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[0:3]`)
- `[e3]` **Điều 15** → `DIEU` (span: `[8:10]`)
- `[e4]` **13 . Tổ chức dịch sang tiếng Anh Dự thảo Báo cáo điều tra tai nạn , Báo cáo điều tra tai nạn đối với các vụ tai nạn hàng hải đặc biệt nghiêm trọng và các vụ tai nạn hàng hải liên quan đến tàu mang cờ quốc tịch nước ngoài .** → `KHOAN` (span: `[11:46]`)

**Quan hệ:**
- (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 15 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`)
- (`e4` 13 . Tổ chức dịch sang tiếng Anh Dự thảo Báo cáo điều tra tai nạn , Báo cáo điều tra tai nạn đối với các vụ tai nạn hàng hải đặc biệt nghiêm trọng và các vụ tai nạn hàng hải liên quan đến tàu mang cờ quốc tịch nước ngoài . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 15 `[DIEU]`)


---

### Mẫu #01_2020_TT-BGTVT_140528#body_context_86 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[01/2020/TT-BGTVT]`<SO_HIEU>`** ban hành **[ngày 20 tháng 01 năm 2020]`<NGAY_BAN_HANH>`** bởi **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** . **[Điều 15]`<DIEU>`** . **[14 . Tổ chức điều tra lại tai nạn hàng hải **[theo quy định tại]`<TU_KHOA_PHAP_LY>`** **[Điều 20 của Thông tư này]`<THAM_CHIEU_PHAP_LY>`** .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **01/2020/TT-BGTVT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[11:14]`)
- `[e3]` **ngày 20 tháng 01 năm 2020** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 15** → `DIEU` (span: `[15:17]`)
- `[e5]` **14 . Tổ chức điều tra lại tai nạn hàng hải theo quy định tại Điều 20 của Thông tư này .** → `KHOAN` (span: `[18:34]`)
- `[e6]` **Điều 20 của Thông tư này** → `THAM_CHIEU_PHAP_LY` (span: `[28:33]`) *(lồng trong `e5` (`KHOAN`))*
- `[e7]` **theo quy định tại** → `TU_KHOA_PHAP_LY` (span: `[25:28]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 20 tháng 01 năm 2020 `[NGAY_BAN_HANH]`)
- (`e4` Điều 15 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`)
- (`e5` 14 . Tổ chức điều tra lại tai nạn hàng hải theo quy định tại Điều 20 của Thông tư này . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 15 `[DIEU]`)
- (`e7` theo quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e6` Điều 20 của Thông tư này `[THAM_CHIEU_PHAP_LY]`)
- (`e5` 14 . Tổ chức điều tra lại tai nạn hàng hải theo quy định tại Điều 20 của Thông tư này . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e6` Điều 20 của Thông tư này `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #01_2020_TT-BGTVT_140528#body_standalone_87 (Loại: `body_standalone`)
> **[Điều 15]`<DIEU>`** . **[14 . Tổ chức điều tra lại tai nạn hàng hải **[theo quy định tại]`<TU_KHOA_PHAP_LY>`** **[Điều 20 của Thông tư này]`<THAM_CHIEU_PHAP_LY>`** .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 15** → `DIEU` (span: `[0:2]`)
- `[e1]` **14 . Tổ chức điều tra lại tai nạn hàng hải theo quy định tại Điều 20 của Thông tư này .** → `KHOAN` (span: `[3:19]`)
- `[e2]` **Điều 20 của Thông tư này** → `THAM_CHIEU_PHAP_LY` (span: `[13:18]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **theo quy định tại** → `TU_KHOA_PHAP_LY` (span: `[10:13]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 14 . Tổ chức điều tra lại tai nạn hàng hải theo quy định tại Điều 20 của Thông tư này . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 15 `[DIEU]`)
- (`e3` theo quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e2` Điều 20 của Thông tư này `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 14 . Tổ chức điều tra lại tai nạn hàng hải theo quy định tại Điều 20 của Thông tư này . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e2` Điều 20 của Thông tư này `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #01_2020_TT-BGTVT_140528#body_context_88 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[01/2020/TT-BGTVT]`<SO_HIEU>`** của **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Hàng hải]`<LINH_VUC>`** . **[Điều 16]`<DIEU>`** . **[1 . Đối với tai nạn hàng hải xảy ra trong vùng nước cảng biển Việt Nam thì thời hạn điều tra **[không quá 60 ngày]`<THOI_HAN>`** kể từ ngày tai nạn hàng hải xảy ra ; đối với các tai nạn hàng hải xảy ra ngoài vùng nước cảng biển thì thời hạn điều tra **[không quá 60 ngày]`<THOI_HAN>`** kể từ ngày được giao điều tra tai nạn hàng hải .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **01/2020/TT-BGTVT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[4:7]`)
- `[e3]` **Hàng hải** → `LINH_VUC` (span: `[9:10]`)
- `[e4]` **Điều 16** → `DIEU` (span: `[11:13]`)
- `[e5]` **1 . Đối với tai nạn hàng hải xảy ra trong vùng nước cảng biển Việt Nam thì thời hạn điều tra không quá 60 ngày kể từ ngày tai nạn hàng hải xảy ra ; đối với các tai nạn hàng hải xảy ra ngoài vùng nước cảng biển thì thời hạn điều tra không quá 60 ngày kể từ ngày được giao điều tra tai nạn hàng hải .** → `KHOAN` (span: `[14:69]`)
- `[e6]` **không quá 60 ngày** → `THOI_HAN` (span: `[30:34]`) *(lồng trong `e5` (`KHOAN`))*
- `[e7]` **không quá 60 ngày** → `THOI_HAN` (span: `[56:60]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Hàng hải `[LINH_VUC]`)
- (`e4` Điều 16 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`)
- (`e5` 1 . Đối với tai nạn hàng hải xảy ra trong vùng nước cảng biển Việt Nam thì thời hạn điều tra không quá 60 ngày kể từ ngày tai nạn hàng hải xảy ra ; đối với các tai nạn hàng hải xảy ra ngoài vùng nước cảng biển thì thời hạn điều tra không quá 60 ngày kể từ ngày được giao điều tra tai nạn hàng hải . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 16 `[DIEU]`)
- (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Hàng hải `[LINH_VUC]`)
- (`e5` 1 . Đối với tai nạn hàng hải xảy ra trong vùng nước cảng biển Việt Nam thì thời hạn điều tra không quá 60 ngày kể từ ngày tai nạn hàng hải xảy ra ; đối với các tai nạn hàng hải xảy ra ngoài vùng nước cảng biển thì thời hạn điều tra không quá 60 ngày kể từ ngày được giao điều tra tai nạn hàng hải . `[KHOAN]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Hàng hải `[LINH_VUC]`)


---

### Mẫu #01_2020_TT-BGTVT_140528#body_standalone_89 (Loại: `body_standalone`)
> **[Điều 16]`<DIEU>`** . **[1 . Đối với tai nạn hàng hải xảy ra trong vùng nước cảng biển Việt Nam thì thời hạn điều tra **[không quá 60 ngày]`<THOI_HAN>`** kể từ ngày tai nạn hàng hải xảy ra ; đối với các tai nạn hàng hải xảy ra ngoài vùng nước cảng biển thì thời hạn điều tra **[không quá 60 ngày]`<THOI_HAN>`** kể từ ngày được giao điều tra tai nạn hàng hải .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 16** → `DIEU` (span: `[0:2]`)
- `[e1]` **1 . Đối với tai nạn hàng hải xảy ra trong vùng nước cảng biển Việt Nam thì thời hạn điều tra không quá 60 ngày kể từ ngày tai nạn hàng hải xảy ra ; đối với các tai nạn hàng hải xảy ra ngoài vùng nước cảng biển thì thời hạn điều tra không quá 60 ngày kể từ ngày được giao điều tra tai nạn hàng hải .** → `KHOAN` (span: `[3:58]`)
- `[e2]` **không quá 60 ngày** → `THOI_HAN` (span: `[19:23]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **không quá 60 ngày** → `THOI_HAN` (span: `[45:49]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 1 . Đối với tai nạn hàng hải xảy ra trong vùng nước cảng biển Việt Nam thì thời hạn điều tra không quá 60 ngày kể từ ngày tai nạn hàng hải xảy ra ; đối với các tai nạn hàng hải xảy ra ngoài vùng nước cảng biển thì thời hạn điều tra không quá 60 ngày kể từ ngày được giao điều tra tai nạn hàng hải . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 16 `[DIEU]`)


---

### Mẫu #01_2020_TT-BGTVT_140528#body_context_90 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[01/2020/TT-BGTVT]`<SO_HIEU>`** của **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Hàng hải]`<LINH_VUC>`** . **[Điều 16]`<DIEU>`** . **[2 . Trong trường hợp phức tạp , nếu việc điều tra tai nạn hàng hải không thể hoàn thành theo thời hạn **[quy định tại]`<TU_KHOA_PHAP_LY>`** **[khoản 1 Điều này]`<THAM_CHIEU_PHAP_LY>`** , trên cơ sở đề xuất của Tổ trưởng Tổ điều tra tai nạn hàng hải , **[Giám đốc]`<CHU_THE_CA_NHAN>`** **[Cảng vụ hàng hải]`<CO_QUAN_THAM_QUYEN>`** phải kịp thời báo cáo bằng văn bản cho Cục trưởng Cục Hàng hải Việt Nam xem xét , quyết định gia hạn thời gian điều tra tai nạn hàng hải .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **01/2020/TT-BGTVT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[4:7]`)
- `[e3]` **Hàng hải** → `LINH_VUC` (span: `[9:10]`)
- `[e4]` **Điều 16** → `DIEU` (span: `[11:13]`)
- `[e5]` **2 . Trong trường hợp phức tạp , nếu việc điều tra tai nạn hàng hải không thể hoàn thành theo thời hạn quy định tại khoản 1 Điều này , trên cơ sở đề xuất của Tổ trưởng Tổ điều tra tai nạn hàng hải , Giám đốc Cảng vụ hàng hải phải kịp thời báo cáo bằng văn bản cho Cục trưởng Cục Hàng hải Việt Nam xem xét , quyết định gia hạn thời gian điều tra tai nạn hàng hải .** → `KHOAN` (span: `[14:68]`)
- `[e6]` **khoản 1 Điều này** → `THAM_CHIEU_PHAP_LY` (span: `[31:35]`) *(lồng trong `e5` (`KHOAN`))*
- `[e7]` **quy định tại** → `TU_KHOA_PHAP_LY` (span: `[29:31]`) *(lồng trong `e5` (`KHOAN`))*
- `[e8]` **Cảng vụ hàng hải** → `CO_QUAN_THAM_QUYEN` (span: `[47:49]`) *(lồng trong `e5` (`KHOAN`))*
- `[e9]` **Giám đốc** → `CHU_THE_CA_NHAN` (span: `[46:47]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Hàng hải `[LINH_VUC]`)
- (`e4` Điều 16 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`)
- (`e5` 2 . Trong trường hợp phức tạp , nếu việc điều tra tai nạn hàng hải không thể hoàn thành theo thời hạn quy định tại khoản 1 Điều này , trên cơ sở đề xuất của Tổ trưởng Tổ điều tra tai nạn hàng hải , Giám đốc Cảng vụ hàng hải phải kịp thời báo cáo bằng văn bản cho Cục trưởng Cục Hàng hải Việt Nam xem xét , quyết định gia hạn thời gian điều tra tai nạn hàng hải . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 16 `[DIEU]`)
- (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Hàng hải `[LINH_VUC]`)
- (`e5` 2 . Trong trường hợp phức tạp , nếu việc điều tra tai nạn hàng hải không thể hoàn thành theo thời hạn quy định tại khoản 1 Điều này , trên cơ sở đề xuất của Tổ trưởng Tổ điều tra tai nạn hàng hải , Giám đốc Cảng vụ hàng hải phải kịp thời báo cáo bằng văn bản cho Cục trưởng Cục Hàng hải Việt Nam xem xét , quyết định gia hạn thời gian điều tra tai nạn hàng hải . `[KHOAN]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Hàng hải `[LINH_VUC]`)
- (`e7` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e6` khoản 1 Điều này `[THAM_CHIEU_PHAP_LY]`)
- (`e5` 2 . Trong trường hợp phức tạp , nếu việc điều tra tai nạn hàng hải không thể hoàn thành theo thời hạn quy định tại khoản 1 Điều này , trên cơ sở đề xuất của Tổ trưởng Tổ điều tra tai nạn hàng hải , Giám đốc Cảng vụ hàng hải phải kịp thời báo cáo bằng văn bản cho Cục trưởng Cục Hàng hải Việt Nam xem xét , quyết định gia hạn thời gian điều tra tai nạn hàng hải . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e6` khoản 1 Điều này `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #01_2020_TT-BGTVT_140528#body_standalone_91 (Loại: `body_standalone`)
> **[Điều 16]`<DIEU>`** . **[2 . Trong trường hợp phức tạp , nếu việc điều tra tai nạn hàng hải không thể hoàn thành theo thời hạn **[quy định tại]`<TU_KHOA_PHAP_LY>`** **[khoản 1 Điều này]`<THAM_CHIEU_PHAP_LY>`** , trên cơ sở đề xuất của Tổ trưởng Tổ điều tra tai nạn hàng hải , **[Giám đốc]`<CHU_THE_CA_NHAN>`** **[Cảng vụ hàng hải]`<CO_QUAN_THAM_QUYEN>`** phải kịp thời báo cáo bằng văn bản cho Cục trưởng Cục Hàng hải Việt Nam xem xét , quyết định gia hạn thời gian điều tra tai nạn hàng hải .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 16** → `DIEU` (span: `[0:2]`)
- `[e1]` **2 . Trong trường hợp phức tạp , nếu việc điều tra tai nạn hàng hải không thể hoàn thành theo thời hạn quy định tại khoản 1 Điều này , trên cơ sở đề xuất của Tổ trưởng Tổ điều tra tai nạn hàng hải , Giám đốc Cảng vụ hàng hải phải kịp thời báo cáo bằng văn bản cho Cục trưởng Cục Hàng hải Việt Nam xem xét , quyết định gia hạn thời gian điều tra tai nạn hàng hải .** → `KHOAN` (span: `[3:57]`)
- `[e2]` **khoản 1 Điều này** → `THAM_CHIEU_PHAP_LY` (span: `[20:24]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **quy định tại** → `TU_KHOA_PHAP_LY` (span: `[18:20]`) *(lồng trong `e1` (`KHOAN`))*
- `[e4]` **Cảng vụ hàng hải** → `CO_QUAN_THAM_QUYEN` (span: `[36:38]`) *(lồng trong `e1` (`KHOAN`))*
- `[e5]` **Giám đốc** → `CHU_THE_CA_NHAN` (span: `[35:36]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 2 . Trong trường hợp phức tạp , nếu việc điều tra tai nạn hàng hải không thể hoàn thành theo thời hạn quy định tại khoản 1 Điều này , trên cơ sở đề xuất của Tổ trưởng Tổ điều tra tai nạn hàng hải , Giám đốc Cảng vụ hàng hải phải kịp thời báo cáo bằng văn bản cho Cục trưởng Cục Hàng hải Việt Nam xem xét , quyết định gia hạn thời gian điều tra tai nạn hàng hải . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 16 `[DIEU]`)
- (`e3` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e2` khoản 1 Điều này `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 2 . Trong trường hợp phức tạp , nếu việc điều tra tai nạn hàng hải không thể hoàn thành theo thời hạn quy định tại khoản 1 Điều này , trên cơ sở đề xuất của Tổ trưởng Tổ điều tra tai nạn hàng hải , Giám đốc Cảng vụ hàng hải phải kịp thời báo cáo bằng văn bản cho Cục trưởng Cục Hàng hải Việt Nam xem xét , quyết định gia hạn thời gian điều tra tai nạn hàng hải . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e2` khoản 1 Điều này `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #01_2020_TT-BGTVT_140528#body_context_92 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[01/2020/TT-BGTVT]`<SO_HIEU>`** của **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Hàng hải]`<LINH_VUC>`** . **[Điều 17]`<DIEU>`** . **[4 . Thông báo cho các bên liên quan về việc tiến hành điều tra .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **01/2020/TT-BGTVT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[4:7]`)
- `[e3]` **Hàng hải** → `LINH_VUC` (span: `[9:10]`)
- `[e4]` **Điều 17** → `DIEU` (span: `[11:13]`)
- `[e5]` **4 . Thông báo cho các bên liên quan về việc tiến hành điều tra .** → `KHOAN` (span: `[14:26]`)

**Quan hệ:**
- (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Hàng hải `[LINH_VUC]`)
- (`e4` Điều 17 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`)
- (`e5` 4 . Thông báo cho các bên liên quan về việc tiến hành điều tra . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 17 `[DIEU]`)
- (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Hàng hải `[LINH_VUC]`)
- (`e5` 4 . Thông báo cho các bên liên quan về việc tiến hành điều tra . `[KHOAN]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Hàng hải `[LINH_VUC]`)


---

### Mẫu #01_2020_TT-BGTVT_140528#body_context_93 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[01/2020/TT-BGTVT]`<SO_HIEU>`** ban hành **[ngày 20 tháng 01 năm 2020]`<NGAY_BAN_HANH>`** bởi **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** . **[Điều 17]`<DIEU>`** . **[7 . Lập Dự thảo Báo cáo điều tra tai nạn hàng hải gửi các bên liên quan để góp ý **[theo quy định tại]`<TU_KHOA_PHAP_LY>`** **[Điều 18 Thông tư này]`<THAM_CHIEU_PHAP_LY>`** .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **01/2020/TT-BGTVT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[11:14]`)
- `[e3]` **ngày 20 tháng 01 năm 2020** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 17** → `DIEU` (span: `[15:17]`)
- `[e5]` **7 . Lập Dự thảo Báo cáo điều tra tai nạn hàng hải gửi các bên liên quan để góp ý theo quy định tại Điều 18 Thông tư này .** → `KHOAN` (span: `[18:40]`)
- `[e6]` **Điều 18 Thông tư này** → `THAM_CHIEU_PHAP_LY` (span: `[35:39]`) *(lồng trong `e5` (`KHOAN`))*
- `[e7]` **theo quy định tại** → `TU_KHOA_PHAP_LY` (span: `[32:35]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 20 tháng 01 năm 2020 `[NGAY_BAN_HANH]`)
- (`e4` Điều 17 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`)
- (`e5` 7 . Lập Dự thảo Báo cáo điều tra tai nạn hàng hải gửi các bên liên quan để góp ý theo quy định tại Điều 18 Thông tư này . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 17 `[DIEU]`)
- (`e7` theo quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e6` Điều 18 Thông tư này `[THAM_CHIEU_PHAP_LY]`)
- (`e5` 7 . Lập Dự thảo Báo cáo điều tra tai nạn hàng hải gửi các bên liên quan để góp ý theo quy định tại Điều 18 Thông tư này . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e6` Điều 18 Thông tư này `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #01_2020_TT-BGTVT_140528#body_standalone_94 (Loại: `body_standalone`)
> **[Điều 17]`<DIEU>`** . **[7 . Lập Dự thảo Báo cáo điều tra tai nạn hàng hải gửi các bên liên quan để góp ý **[theo quy định tại]`<TU_KHOA_PHAP_LY>`** **[Điều 18 Thông tư này]`<THAM_CHIEU_PHAP_LY>`** .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 17** → `DIEU` (span: `[0:2]`)
- `[e1]` **7 . Lập Dự thảo Báo cáo điều tra tai nạn hàng hải gửi các bên liên quan để góp ý theo quy định tại Điều 18 Thông tư này .** → `KHOAN` (span: `[3:25]`)
- `[e2]` **Điều 18 Thông tư này** → `THAM_CHIEU_PHAP_LY` (span: `[20:24]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **theo quy định tại** → `TU_KHOA_PHAP_LY` (span: `[17:20]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 7 . Lập Dự thảo Báo cáo điều tra tai nạn hàng hải gửi các bên liên quan để góp ý theo quy định tại Điều 18 Thông tư này . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 17 `[DIEU]`)
- (`e3` theo quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e2` Điều 18 Thông tư này `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 7 . Lập Dự thảo Báo cáo điều tra tai nạn hàng hải gửi các bên liên quan để góp ý theo quy định tại Điều 18 Thông tư này . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e2` Điều 18 Thông tư này `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #01_2020_TT-BGTVT_140528#body_context_95 (Loại: `body_context`)
> **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[01/2020/TT-BGTVT]`<SO_HIEU>`** . **[Điều 18]`<DIEU>`** . **[2 . Chính quyền hàng hải của quốc gia tàu mang cờ , chủ tàu , người quản lý tàu , người khai thác tàu có liên quan không được phổ biến , công bố hoặc cho phép tiếp cận Dự thảo Báo cáo hoặc bất cứ phần nào của Dự thảo Báo cáo khi chưa có sự đồng ý của Tổ điều tra tai nạn hàng hải , **[Giám đốc]`<CHU_THE_CA_NHAN>`** **[Cảng vụ hàng hải]`<CO_QUAN_THAM_QUYEN>`** hoặc Cục Hàng hải Việt Nam .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[4:5]`)
- `[e1]` **01/2020/TT-BGTVT** → `SO_HIEU` (span: `[6:7]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[0:3]`)
- `[e3]` **Điều 18** → `DIEU` (span: `[8:10]`)
- `[e4]` **2 . Chính quyền hàng hải của quốc gia tàu mang cờ , chủ tàu , người quản lý tàu , người khai thác tàu có liên quan không được phổ biến , công bố hoặc cho phép tiếp cận Dự thảo Báo cáo hoặc bất cứ phần nào của Dự thảo Báo cáo khi chưa có sự đồng ý của Tổ điều tra tai nạn hàng hải , Giám đốc Cảng vụ hàng hải hoặc Cục Hàng hải Việt Nam .** → `KHOAN` (span: `[11:69]`)
- `[e5]` **Cảng vụ hàng hải** → `CO_QUAN_THAM_QUYEN` (span: `[62:64]`) *(lồng trong `e4` (`KHOAN`))*
- `[e6]` **Giám đốc** → `CHU_THE_CA_NHAN` (span: `[61:62]`) *(lồng trong `e4` (`KHOAN`))*

**Quan hệ:**
- (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 18 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`)
- (`e4` 2 . Chính quyền hàng hải của quốc gia tàu mang cờ , chủ tàu , người quản lý tàu , người khai thác tàu có liên quan không được phổ biến , công bố hoặc cho phép tiếp cận Dự thảo Báo cáo hoặc bất cứ phần nào của Dự thảo Báo cáo khi chưa có sự đồng ý của Tổ điều tra tai nạn hàng hải , Giám đốc Cảng vụ hàng hải hoặc Cục Hàng hải Việt Nam . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 18 `[DIEU]`)


---

### Mẫu #01_2020_TT-BGTVT_140528#body_standalone_96 (Loại: `body_standalone`)
> **[Điều 18]`<DIEU>`** . **[2 . Chính quyền hàng hải của quốc gia tàu mang cờ , chủ tàu , người quản lý tàu , người khai thác tàu có liên quan không được phổ biến , công bố hoặc cho phép tiếp cận Dự thảo Báo cáo hoặc bất cứ phần nào của Dự thảo Báo cáo khi chưa có sự đồng ý của Tổ điều tra tai nạn hàng hải , **[Giám đốc]`<CHU_THE_CA_NHAN>`** **[Cảng vụ hàng hải]`<CO_QUAN_THAM_QUYEN>`** hoặc Cục Hàng hải Việt Nam .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 18** → `DIEU` (span: `[0:2]`)
- `[e1]` **2 . Chính quyền hàng hải của quốc gia tàu mang cờ , chủ tàu , người quản lý tàu , người khai thác tàu có liên quan không được phổ biến , công bố hoặc cho phép tiếp cận Dự thảo Báo cáo hoặc bất cứ phần nào của Dự thảo Báo cáo khi chưa có sự đồng ý của Tổ điều tra tai nạn hàng hải , Giám đốc Cảng vụ hàng hải hoặc Cục Hàng hải Việt Nam .** → `KHOAN` (span: `[3:61]`)
- `[e2]` **Cảng vụ hàng hải** → `CO_QUAN_THAM_QUYEN` (span: `[54:56]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **Giám đốc** → `CHU_THE_CA_NHAN` (span: `[53:54]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 2 . Chính quyền hàng hải của quốc gia tàu mang cờ , chủ tàu , người quản lý tàu , người khai thác tàu có liên quan không được phổ biến , công bố hoặc cho phép tiếp cận Dự thảo Báo cáo hoặc bất cứ phần nào của Dự thảo Báo cáo khi chưa có sự đồng ý của Tổ điều tra tai nạn hàng hải , Giám đốc Cảng vụ hàng hải hoặc Cục Hàng hải Việt Nam . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 18 `[DIEU]`)


---

### Mẫu #01_2020_TT-BGTVT_140528#body_context_97 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[01/2020/TT-BGTVT]`<SO_HIEU>`** ban hành **[ngày 20 tháng 01 năm 2020]`<NGAY_BAN_HANH>`** bởi **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** . **[Điều 18]`<DIEU>`** . **[3 . Chậm nhất 30 ngày hoặc trong thời gian thống nhất giữa Tổ điều tra và các bên liên quan nhưng **[không quá 30 ngày]`<THOI_HAN>`** , kể từ ngày gửi Dự thảo Báo cáo , Chính quyền hàng hải của quốc gia tàu mang cờ , chủ tàu , người quản lý tàu , người khai thác tàu có liên quan có ý kiến đóng góp về bản Dự thảo Báo cáo . Quá thời hạn trên , nếu chưa nhận được ý kiến đóng góp , Tổ điều tra tiến hành trình Báo cáo điều tra tai nạn hàng]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **01/2020/TT-BGTVT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[11:14]`)
- `[e3]` **ngày 20 tháng 01 năm 2020** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 18** → `DIEU` (span: `[15:17]`)
- `[e5]` **3 . Chậm nhất 30 ngày hoặc trong thời gian thống nhất giữa Tổ điều tra và các bên liên quan nhưng không quá 30 ngày , kể từ ngày gửi Dự thảo Báo cáo , Chính quyền hàng hải của quốc gia tàu mang cờ , chủ tàu , người quản lý tàu , người khai thác tàu có liên quan có ý kiến đóng góp về bản Dự thảo Báo cáo . Quá thời hạn trên , nếu chưa nhận được ý kiến đóng góp , Tổ điều tra tiến hành trình Báo cáo điều tra tai nạn hàng** → `KHOAN` (span: `[18:94]`)
- `[e6]` **không quá 30 ngày** → `THOI_HAN` (span: `[36:40]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 20 tháng 01 năm 2020 `[NGAY_BAN_HANH]`)
- (`e4` Điều 18 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`)
- (`e5` 3 . Chậm nhất 30 ngày hoặc trong thời gian thống nhất giữa Tổ điều tra và các bên liên quan nhưng không quá 30 ngày , kể từ ngày gửi Dự thảo Báo cáo , Chính quyền hàng hải của quốc gia tàu mang cờ , chủ tàu , người quản lý tàu , người khai thác tàu có liên quan có ý kiến đóng góp về bản Dự thảo Báo cáo . Quá thời hạn trên , nếu chưa nhận được ý kiến đóng góp , Tổ điều tra tiến hành trình Báo cáo điều tra tai nạn hàng `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 18 `[DIEU]`)


---

### Mẫu #01_2020_TT-BGTVT_140528#body_context_98 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[01/2020/TT-BGTVT]`<SO_HIEU>`** của **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Hàng hải]`<LINH_VUC>`** . **[Điều 19]`<DIEU>`** . **[Khoản 1]`<KHOAN>`** . **[đ ) Phân tích , lập luận và chứng minh các yếu tố dẫn đến nguyên nhân của tai nạn hàng hải ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **01/2020/TT-BGTVT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[4:7]`)
- `[e3]` **Hàng hải** → `LINH_VUC` (span: `[9:10]`)
- `[e4]` **Điều 19** → `DIEU` (span: `[11:13]`)
- `[e5]` **Khoản 1** → `KHOAN` (span: `[14:16]`)
- `[e6]` **đ ) Phân tích , lập luận và chứng minh các yếu tố dẫn đến nguyên nhân của tai nạn hàng hải ;** → `DIEM` (span: `[17:33]`)

**Quan hệ:**
- (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Hàng hải `[LINH_VUC]`)
- (`e4` Điều 19 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`)
- (`e5` Khoản 1 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 19 `[DIEU]`)
- (`e6` đ ) Phân tích , lập luận và chứng minh các yếu tố dẫn đến nguyên nhân của tai nạn hàng hải ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e5` Khoản 1 `[KHOAN]`)
- (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Hàng hải `[LINH_VUC]`)
- (`e6` đ ) Phân tích , lập luận và chứng minh các yếu tố dẫn đến nguyên nhân của tai nạn hàng hải ; `[DIEM]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Hàng hải `[LINH_VUC]`)


---

### Mẫu #01_2020_TT-BGTVT_140528#body_context_99 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[01/2020/TT-BGTVT]`<SO_HIEU>`** ban hành **[ngày 20 tháng 01 năm 2020]`<NGAY_BAN_HANH>`** bởi **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** . **[Chương III]`<CHUONG>`** . **[Điều 20 . Điều tra lại tai nạn hàng hải . Trong trường hợp có những bằng chứng mới được cung cấp hay thu thập được mà những bằng chứng này làm thay đổi cơ bản nguyên nhân của vụ tai nạn hàng hải , **[Giám đốc]`<CHU_THE_CA_NHAN>`** **[Cảng vụ hàng hải]`<CO_QUAN_THAM_QUYEN>`** quyết định tiến hành điều tra lại vụ tai nạn đó .]`<DIEU>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **01/2020/TT-BGTVT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[11:14]`)
- `[e3]` **ngày 20 tháng 01 năm 2020** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Chương III** → `CHUONG` (span: `[15:17]`)
- `[e5]` **Điều 20 . Điều tra lại tai nạn hàng hải . Trong trường hợp có những bằng chứng mới được cung cấp hay thu thập được mà những bằng chứng này làm thay đổi cơ bản nguyên nhân của vụ tai nạn hàng hải , Giám đốc Cảng vụ hàng hải quyết định tiến hành điều tra lại vụ tai nạn đó .** → `DIEU` (span: `[18:61]`)
- `[e6]` **Cảng vụ hàng hải** → `CO_QUAN_THAM_QUYEN` (span: `[51:53]`) *(lồng trong `e5` (`DIEU`))*
- `[e7]` **Giám đốc** → `CHU_THE_CA_NHAN` (span: `[50:51]`) *(lồng trong `e5` (`DIEU`))*

**Quan hệ:**
- (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 20 tháng 01 năm 2020 `[NGAY_BAN_HANH]`)
- (`e4` Chương III `[CHUONG]`) ==[ **THUOC_VE** ]==> (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`)
- (`e5` Điều 20 . Điều tra lại tai nạn hàng hải . Trong trường hợp có những bằng chứng mới được cung cấp hay thu thập được mà những bằng chứng này làm thay đổi cơ bản nguyên nhân của vụ tai nạn hàng hải , Giám đốc Cảng vụ hàng hải quyết định tiến hành điều tra lại vụ tai nạn đó . `[DIEU]`) ==[ **THUOC_VE** ]==> (`e4` Chương III `[CHUONG]`)


---

### Mẫu #01_2020_TT-BGTVT_140528#body_context_100 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[01/2020/TT-BGTVT]`<SO_HIEU>`** ban hành **[ngày 20 tháng 01 năm 2020]`<NGAY_BAN_HANH>`** bởi **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** . **[Chương III]`<CHUONG>`** . **[Điều 21 . Khiếu nại , tố cáo và giải quyết khiếu nại , tố cáo . Khiếu nại , tố cáo ( nếu có ) liên quan đến việc điều tra tai nạn hàng hải sẽ được giải quyết theo quy định của pháp luật về giải quyết khiếu nại , tố cáo .]`<DIEU>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **01/2020/TT-BGTVT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[11:14]`)
- `[e3]` **ngày 20 tháng 01 năm 2020** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Chương III** → `CHUONG` (span: `[15:17]`)
- `[e5]` **Điều 21 . Khiếu nại , tố cáo và giải quyết khiếu nại , tố cáo . Khiếu nại , tố cáo ( nếu có ) liên quan đến việc điều tra tai nạn hàng hải sẽ được giải quyết theo quy định của pháp luật về giải quyết khiếu nại , tố cáo .** → `DIEU` (span: `[18:56]`)

**Quan hệ:**
- (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 20 tháng 01 năm 2020 `[NGAY_BAN_HANH]`)
- (`e4` Chương III `[CHUONG]`) ==[ **THUOC_VE** ]==> (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`)
- (`e5` Điều 21 . Khiếu nại , tố cáo và giải quyết khiếu nại , tố cáo . Khiếu nại , tố cáo ( nếu có ) liên quan đến việc điều tra tai nạn hàng hải sẽ được giải quyết theo quy định của pháp luật về giải quyết khiếu nại , tố cáo . `[DIEU]`) ==[ **THUOC_VE** ]==> (`e4` Chương III `[CHUONG]`)


---

### Mẫu #01_2020_TT-BGTVT_140528#body_context_101 (Loại: `body_context`)
> **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[01/2020/TT-BGTVT]`<SO_HIEU>`** . **[Điều 23 . Hiệu lực thi hành . Thông tư này có hiệu lực kể từ ngày 15 tháng 3 năm 2020 . **[Bãi bỏ]`<TU_KHOA_PHAP_LY>`** **[Thông tư số 34/2015/TT-BGTVT]`<THAM_CHIEU_PHAP_LY>`** **[ngày 24 tháng 7 năm 2015]`<NGAY_THAM_CHIEU>`** của **[Bộ trưởng Bộ Giao thông vận tải]`<CO_QUAN_THAM_QUYEN>`** về báo cáo và điều tra tai nạn hàng hải và **[Thông tư số 39/2017/TT-BGTVT]`<THAM_CHIEU_PHAP_LY>`** **[ngày 07 tháng 11 năm 2017]`<NGAY_THAM_CHIEU>`** **[sửa đổi , bổ sung một số điều của]`<TU_KHOA_PHAP_LY>`** **[Thông tư số 34/2015/TT-BGTVT]`<THAM_CHIEU_PHAP_LY>`** **[ngày 24 tháng 7 năm 2015]`<NGAY_THAM_CHIEU>`** của **[Bộ trưởng Bộ Giao thông vận tải]`<CO_QUAN_THAM_QUYEN>`** quy định về báo cáo và điều]`<DIEU>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[4:5]`)
- `[e1]` **01/2020/TT-BGTVT** → `SO_HIEU` (span: `[6:7]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[0:3]`)
- `[e3]` **Điều 23 . Hiệu lực thi hành . Thông tư này có hiệu lực kể từ ngày 15 tháng 3 năm 2020 . Bãi bỏ Thông tư số 34/2015/TT-BGTVT ngày 24 tháng 7 năm 2015 của Bộ trưởng Bộ Giao thông vận tải về báo cáo và điều tra tai nạn hàng hải và Thông tư số 39/2017/TT-BGTVT ngày 07 tháng 11 năm 2017 sửa đổi , bổ sung một số điều của Thông tư số 34/2015/TT-BGTVT ngày 24 tháng 7 năm 2015 của Bộ trưởng Bộ Giao thông vận tải quy định về báo cáo và điều** → `DIEU` (span: `[8:83]`)
- `[e4]` **Thông tư số 34/2015/TT-BGTVT** → `THAM_CHIEU_PHAP_LY` (span: `[28:31]`) *(lồng trong `e3` (`DIEU`))*
- `[e5]` **Thông tư số 39/2017/TT-BGTVT** → `THAM_CHIEU_PHAP_LY` (span: `[49:52]`) *(lồng trong `e3` (`DIEU`))*
- `[e6]` **Thông tư số 34/2015/TT-BGTVT** → `THAM_CHIEU_PHAP_LY` (span: `[64:67]`) *(lồng trong `e3` (`DIEU`))*
- `[e7]` **Bãi bỏ** → `TU_KHOA_PHAP_LY` (span: `[27:28]`) *(lồng trong `e3` (`DIEU`))*
- `[e8]` **sửa đổi , bổ sung một số điều của** → `TU_KHOA_PHAP_LY` (span: `[58:64]`) *(lồng trong `e3` (`DIEU`))*
- `[e9]` **ngày 24 tháng 7 năm 2015** → `NGAY_THAM_CHIEU` (span: `[31:37]`) *(lồng trong `e3` (`DIEU`))*
- `[e10]` **ngày 07 tháng 11 năm 2017** → `NGAY_THAM_CHIEU` (span: `[52:58]`) *(lồng trong `e3` (`DIEU`))*
- `[e11]` **ngày 24 tháng 7 năm 2015** → `NGAY_THAM_CHIEU` (span: `[67:73]`) *(lồng trong `e3` (`DIEU`))*
- `[e12]` **Bộ trưởng Bộ Giao thông vận tải** → `CO_QUAN_THAM_QUYEN` (span: `[38:42]`) *(lồng trong `e3` (`DIEU`))*
- `[e13]` **Bộ trưởng Bộ Giao thông vận tải** → `CO_QUAN_THAM_QUYEN` (span: `[74:78]`) *(lồng trong `e3` (`DIEU`))*

**Quan hệ:**
- (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 23 . Hiệu lực thi hành . Thông tư này có hiệu lực kể từ ngày 15 tháng 3 năm 2020 . Bãi bỏ Thông tư số 34/2015/TT-BGTVT ngày 24 tháng 7 năm 2015 của Bộ trưởng Bộ Giao thông vận tải về báo cáo và điều tra tai nạn hàng hải và Thông tư số 39/2017/TT-BGTVT ngày 07 tháng 11 năm 2017 sửa đổi , bổ sung một số điều của Thông tư số 34/2015/TT-BGTVT ngày 24 tháng 7 năm 2015 của Bộ trưởng Bộ Giao thông vận tải quy định về báo cáo và điều `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`)
- (`e7` Bãi bỏ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e4` Thông tư số 34/2015/TT-BGTVT `[THAM_CHIEU_PHAP_LY]`)
- (`e3` Điều 23 . Hiệu lực thi hành . Thông tư này có hiệu lực kể từ ngày 15 tháng 3 năm 2020 . Bãi bỏ Thông tư số 34/2015/TT-BGTVT ngày 24 tháng 7 năm 2015 của Bộ trưởng Bộ Giao thông vận tải về báo cáo và điều tra tai nạn hàng hải và Thông tư số 39/2017/TT-BGTVT ngày 07 tháng 11 năm 2017 sửa đổi , bổ sung một số điều của Thông tư số 34/2015/TT-BGTVT ngày 24 tháng 7 năm 2015 của Bộ trưởng Bộ Giao thông vận tải quy định về báo cáo và điều `[DIEU]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e4` Thông tư số 34/2015/TT-BGTVT `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e7` Bãi bỏ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e5` Thông tư số 39/2017/TT-BGTVT `[THAM_CHIEU_PHAP_LY]`)
- (`e3` Điều 23 . Hiệu lực thi hành . Thông tư này có hiệu lực kể từ ngày 15 tháng 3 năm 2020 . Bãi bỏ Thông tư số 34/2015/TT-BGTVT ngày 24 tháng 7 năm 2015 của Bộ trưởng Bộ Giao thông vận tải về báo cáo và điều tra tai nạn hàng hải và Thông tư số 39/2017/TT-BGTVT ngày 07 tháng 11 năm 2017 sửa đổi , bổ sung một số điều của Thông tư số 34/2015/TT-BGTVT ngày 24 tháng 7 năm 2015 của Bộ trưởng Bộ Giao thông vận tải quy định về báo cáo và điều `[DIEU]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e5` Thông tư số 39/2017/TT-BGTVT `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e8` sửa đổi , bổ sung một số điều của `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e6` Thông tư số 34/2015/TT-BGTVT `[THAM_CHIEU_PHAP_LY]`)
- (`e3` Điều 23 . Hiệu lực thi hành . Thông tư này có hiệu lực kể từ ngày 15 tháng 3 năm 2020 . Bãi bỏ Thông tư số 34/2015/TT-BGTVT ngày 24 tháng 7 năm 2015 của Bộ trưởng Bộ Giao thông vận tải về báo cáo và điều tra tai nạn hàng hải và Thông tư số 39/2017/TT-BGTVT ngày 07 tháng 11 năm 2017 sửa đổi , bổ sung một số điều của Thông tư số 34/2015/TT-BGTVT ngày 24 tháng 7 năm 2015 của Bộ trưởng Bộ Giao thông vận tải quy định về báo cáo và điều `[DIEU]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e6` Thông tư số 34/2015/TT-BGTVT `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e4` Thông tư số 34/2015/TT-BGTVT `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e9` ngày 24 tháng 7 năm 2015 `[NGAY_THAM_CHIEU]`)
- (`e5` Thông tư số 39/2017/TT-BGTVT `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e10` ngày 07 tháng 11 năm 2017 `[NGAY_THAM_CHIEU]`)
- (`e6` Thông tư số 34/2015/TT-BGTVT `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e11` ngày 24 tháng 7 năm 2015 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #01_2020_TT-BGTVT_140528#body_standalone_102 (Loại: `body_standalone`)
> **[Điều 23 . Hiệu lực thi hành . Thông tư này có hiệu lực kể từ ngày 15 tháng 3 năm 2020 . **[Bãi bỏ]`<TU_KHOA_PHAP_LY>`** **[Thông tư số 34/2015/TT-BGTVT]`<THAM_CHIEU_PHAP_LY>`** **[ngày 24 tháng 7 năm 2015]`<NGAY_THAM_CHIEU>`** của **[Bộ trưởng Bộ Giao thông vận tải]`<CO_QUAN_THAM_QUYEN>`** về báo cáo và điều tra tai nạn hàng hải và **[Thông tư số 39/2017/TT-BGTVT]`<THAM_CHIEU_PHAP_LY>`** **[ngày 07 tháng 11 năm 2017]`<NGAY_THAM_CHIEU>`** **[sửa đổi , bổ sung một số điều của]`<TU_KHOA_PHAP_LY>`** **[Thông tư số 34/2015/TT-BGTVT]`<THAM_CHIEU_PHAP_LY>`** **[ngày 24 tháng 7 năm 2015]`<NGAY_THAM_CHIEU>`** của **[Bộ trưởng Bộ Giao thông vận tải]`<CO_QUAN_THAM_QUYEN>`** quy định về báo cáo và điều]`<DIEU>`**

**Thực thể:**
- `[e0]` **Điều 23 . Hiệu lực thi hành . Thông tư này có hiệu lực kể từ ngày 15 tháng 3 năm 2020 . Bãi bỏ Thông tư số 34/2015/TT-BGTVT ngày 24 tháng 7 năm 2015 của Bộ trưởng Bộ Giao thông vận tải về báo cáo và điều tra tai nạn hàng hải và Thông tư số 39/2017/TT-BGTVT ngày 07 tháng 11 năm 2017 sửa đổi , bổ sung một số điều của Thông tư số 34/2015/TT-BGTVT ngày 24 tháng 7 năm 2015 của Bộ trưởng Bộ Giao thông vận tải quy định về báo cáo và điều** → `DIEU` (span: `[0:75]`)
- `[e1]` **Thông tư số 34/2015/TT-BGTVT** → `THAM_CHIEU_PHAP_LY` (span: `[20:23]`) *(lồng trong `e0` (`DIEU`))*
- `[e2]` **Thông tư số 39/2017/TT-BGTVT** → `THAM_CHIEU_PHAP_LY` (span: `[41:44]`) *(lồng trong `e0` (`DIEU`))*
- `[e3]` **Thông tư số 34/2015/TT-BGTVT** → `THAM_CHIEU_PHAP_LY` (span: `[56:59]`) *(lồng trong `e0` (`DIEU`))*
- `[e4]` **Bãi bỏ** → `TU_KHOA_PHAP_LY` (span: `[19:20]`) *(lồng trong `e0` (`DIEU`))*
- `[e5]` **sửa đổi , bổ sung một số điều của** → `TU_KHOA_PHAP_LY` (span: `[50:56]`) *(lồng trong `e0` (`DIEU`))*
- `[e6]` **ngày 24 tháng 7 năm 2015** → `NGAY_THAM_CHIEU` (span: `[23:29]`) *(lồng trong `e0` (`DIEU`))*
- `[e7]` **ngày 07 tháng 11 năm 2017** → `NGAY_THAM_CHIEU` (span: `[44:50]`) *(lồng trong `e0` (`DIEU`))*
- `[e8]` **ngày 24 tháng 7 năm 2015** → `NGAY_THAM_CHIEU` (span: `[59:65]`) *(lồng trong `e0` (`DIEU`))*
- `[e9]` **Bộ trưởng Bộ Giao thông vận tải** → `CO_QUAN_THAM_QUYEN` (span: `[30:34]`) *(lồng trong `e0` (`DIEU`))*
- `[e10]` **Bộ trưởng Bộ Giao thông vận tải** → `CO_QUAN_THAM_QUYEN` (span: `[66:70]`) *(lồng trong `e0` (`DIEU`))*

**Quan hệ:**
- (`e4` Bãi bỏ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e1` Thông tư số 34/2015/TT-BGTVT `[THAM_CHIEU_PHAP_LY]`)
- (`e0` Điều 23 . Hiệu lực thi hành . Thông tư này có hiệu lực kể từ ngày 15 tháng 3 năm 2020 . Bãi bỏ Thông tư số 34/2015/TT-BGTVT ngày 24 tháng 7 năm 2015 của Bộ trưởng Bộ Giao thông vận tải về báo cáo và điều tra tai nạn hàng hải và Thông tư số 39/2017/TT-BGTVT ngày 07 tháng 11 năm 2017 sửa đổi , bổ sung một số điều của Thông tư số 34/2015/TT-BGTVT ngày 24 tháng 7 năm 2015 của Bộ trưởng Bộ Giao thông vận tải quy định về báo cáo và điều `[DIEU]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e1` Thông tư số 34/2015/TT-BGTVT `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e4` Bãi bỏ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e2` Thông tư số 39/2017/TT-BGTVT `[THAM_CHIEU_PHAP_LY]`)
- (`e0` Điều 23 . Hiệu lực thi hành . Thông tư này có hiệu lực kể từ ngày 15 tháng 3 năm 2020 . Bãi bỏ Thông tư số 34/2015/TT-BGTVT ngày 24 tháng 7 năm 2015 của Bộ trưởng Bộ Giao thông vận tải về báo cáo và điều tra tai nạn hàng hải và Thông tư số 39/2017/TT-BGTVT ngày 07 tháng 11 năm 2017 sửa đổi , bổ sung một số điều của Thông tư số 34/2015/TT-BGTVT ngày 24 tháng 7 năm 2015 của Bộ trưởng Bộ Giao thông vận tải quy định về báo cáo và điều `[DIEU]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e2` Thông tư số 39/2017/TT-BGTVT `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e5` sửa đổi , bổ sung một số điều của `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Thông tư số 34/2015/TT-BGTVT `[THAM_CHIEU_PHAP_LY]`)
- (`e0` Điều 23 . Hiệu lực thi hành . Thông tư này có hiệu lực kể từ ngày 15 tháng 3 năm 2020 . Bãi bỏ Thông tư số 34/2015/TT-BGTVT ngày 24 tháng 7 năm 2015 của Bộ trưởng Bộ Giao thông vận tải về báo cáo và điều tra tai nạn hàng hải và Thông tư số 39/2017/TT-BGTVT ngày 07 tháng 11 năm 2017 sửa đổi , bổ sung một số điều của Thông tư số 34/2015/TT-BGTVT ngày 24 tháng 7 năm 2015 của Bộ trưởng Bộ Giao thông vận tải quy định về báo cáo và điều `[DIEU]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Thông tư số 34/2015/TT-BGTVT `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e1` Thông tư số 34/2015/TT-BGTVT `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e6` ngày 24 tháng 7 năm 2015 `[NGAY_THAM_CHIEU]`)
- (`e2` Thông tư số 39/2017/TT-BGTVT `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e7` ngày 07 tháng 11 năm 2017 `[NGAY_THAM_CHIEU]`)
- (`e3` Thông tư số 34/2015/TT-BGTVT `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e8` ngày 24 tháng 7 năm 2015 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #01_2020_TT-BGTVT_140528#body_context_103 (Loại: `body_context`)
> **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[01/2020/TT-BGTVT]`<SO_HIEU>`** . **[Điều 2 . Đối tượng áp dụng]`<DIEU>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[4:5]`)
- `[e1]` **01/2020/TT-BGTVT** → `SO_HIEU` (span: `[6:7]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[0:3]`)
- `[e3]` **Điều 2 . Đối tượng áp dụng** → `DIEU` (span: `[8:13]`)

**Quan hệ:**
- (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 2 . Đối tượng áp dụng `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`)


---

### Mẫu #01_2020_TT-BGTVT_140528#body_context_104 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[01/2020/TT-BGTVT]`<SO_HIEU>`** ban hành **[ngày 20 tháng 01 năm 2020]`<NGAY_BAN_HANH>`** bởi **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** . **[Chương II]`<CHUONG>`** . **[Điều 8 . Báo cáo chi tiết]`<DIEU>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **01/2020/TT-BGTVT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[11:14]`)
- `[e3]` **ngày 20 tháng 01 năm 2020** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Chương II** → `CHUONG` (span: `[15:17]`)
- `[e5]` **Điều 8 . Báo cáo chi tiết** → `DIEU` (span: `[18:23]`)

**Quan hệ:**
- (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 20 tháng 01 năm 2020 `[NGAY_BAN_HANH]`)
- (`e4` Chương II `[CHUONG]`) ==[ **THUOC_VE** ]==> (`e1` 01/2020/TT-BGTVT `[SO_HIEU]`)
- (`e5` Điều 8 . Báo cáo chi tiết `[DIEU]`) ==[ **THUOC_VE** ]==> (`e4` Chương II `[CHUONG]`)


---

### Mẫu #01_2020_TT-BGTVT_140528#hard_negative_105 (Loại: `hard_negative`)
> CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM


---
