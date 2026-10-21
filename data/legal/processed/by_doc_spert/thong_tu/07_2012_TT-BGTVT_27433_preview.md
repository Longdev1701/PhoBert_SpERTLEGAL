# Dữ liệu gán nhãn văn bản: 07_2012_TT-BGTVT_27433
- **Thể loại**: `thong_tu`
- **Phân vùng dữ liệu**: `TRAIN`
- **Tổng số mẫu**: 107 mẫu
- **Tổng số thực thể**: 694
- **Tổng số quan hệ**: 487

---

### Mẫu #07_2012_TT-BGTVT_27433#preamble_context_0 (Loại: `preamble_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[07/2012/TT-BGTVT]`<SO_HIEU>`** của **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** . **[Căn cứ]`<TU_KHOA_PHAP_LY>`** **[Bộ luật Hàng hải Việt Nam]`<THAM_CHIEU_PHAP_LY>`** **[ngày 14 tháng 6 năm 2005]`<NGAY_THAM_CHIEU>`** ;

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **07/2012/TT-BGTVT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[4:7]`)
- `[e3]` **Bộ luật Hàng hải Việt Nam** → `THAM_CHIEU_PHAP_LY` (span: `[9:12]`)
- `[e4]` **Căn cứ** → `TU_KHOA_PHAP_LY` (span: `[8:9]`)
- `[e5]` **ngày 14 tháng 6 năm 2005** → `NGAY_THAM_CHIEU` (span: `[12:18]`)

**Quan hệ:**
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e4` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Bộ luật Hàng hải Việt Nam `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Bộ luật Hàng hải Việt Nam `[THAM_CHIEU_PHAP_LY]`)
- (`e3` Bộ luật Hàng hải Việt Nam `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e5` ngày 14 tháng 6 năm 2005 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #07_2012_TT-BGTVT_27433#preamble_standalone_1 (Loại: `preamble_standalone`)
> **[Căn cứ]`<TU_KHOA_PHAP_LY>`** **[Bộ luật Hàng hải Việt Nam]`<THAM_CHIEU_PHAP_LY>`** **[ngày 14 tháng 6 năm 2005]`<NGAY_THAM_CHIEU>`** ;

**Thực thể:**
- `[e0]` **Bộ luật Hàng hải Việt Nam** → `THAM_CHIEU_PHAP_LY` (span: `[1:4]`)
- `[e1]` **Căn cứ** → `TU_KHOA_PHAP_LY` (span: `[0:1]`)
- `[e2]` **ngày 14 tháng 6 năm 2005** → `NGAY_THAM_CHIEU` (span: `[4:10]`)

**Quan hệ:**
- (`e1` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e0` Bộ luật Hàng hải Việt Nam `[THAM_CHIEU_PHAP_LY]`)
- (`e0` Bộ luật Hàng hải Việt Nam `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e2` ngày 14 tháng 6 năm 2005 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #07_2012_TT-BGTVT_27433#preamble_context_2 (Loại: `preamble_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[07/2012/TT-BGTVT]`<SO_HIEU>`** của **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** . **[Căn cứ]`<TU_KHOA_PHAP_LY>`** **[Nghị định số 51/2008/NĐ-CP]`<THAM_CHIEU_PHAP_LY>`** **[ngày 22 tháng 4 năm 2008]`<NGAY_THAM_CHIEU>`** của **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** quy định chức năng , nhiệm vụ , quyền hạn và cơ cấu tổ chức của **[Bộ Giao thông vận tải]`<CO_QUAN_THAM_QUYEN>`** ;

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **07/2012/TT-BGTVT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[4:7]`)
- `[e3]` **Nghị định số 51/2008/NĐ-CP** → `THAM_CHIEU_PHAP_LY` (span: `[9:12]`)
- `[e4]` **Căn cứ** → `TU_KHOA_PHAP_LY` (span: `[8:9]`)
- `[e5]` **ngày 22 tháng 4 năm 2008** → `NGAY_THAM_CHIEU` (span: `[12:18]`)
- `[e6]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[19:20]`)
- `[e7]` **Bộ Giao thông vận tải** → `CO_QUAN_THAM_QUYEN` (span: `[30:33]`)

**Quan hệ:**
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e4` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Nghị định số 51/2008/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Nghị định số 51/2008/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e3` Nghị định số 51/2008/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e5` ngày 22 tháng 4 năm 2008 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #07_2012_TT-BGTVT_27433#preamble_standalone_3 (Loại: `preamble_standalone`)
> **[Căn cứ]`<TU_KHOA_PHAP_LY>`** **[Nghị định số 51/2008/NĐ-CP]`<THAM_CHIEU_PHAP_LY>`** **[ngày 22 tháng 4 năm 2008]`<NGAY_THAM_CHIEU>`** của **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** quy định chức năng , nhiệm vụ , quyền hạn và cơ cấu tổ chức của **[Bộ Giao thông vận tải]`<CO_QUAN_THAM_QUYEN>`** ;

**Thực thể:**
- `[e0]` **Nghị định số 51/2008/NĐ-CP** → `THAM_CHIEU_PHAP_LY` (span: `[1:4]`)
- `[e1]` **Căn cứ** → `TU_KHOA_PHAP_LY` (span: `[0:1]`)
- `[e2]` **ngày 22 tháng 4 năm 2008** → `NGAY_THAM_CHIEU` (span: `[4:10]`)
- `[e3]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[11:12]`)
- `[e4]` **Bộ Giao thông vận tải** → `CO_QUAN_THAM_QUYEN` (span: `[22:25]`)

**Quan hệ:**
- (`e1` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e0` Nghị định số 51/2008/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e3` Chính phủ `[CO_QUAN_THAM_QUYEN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e0` Nghị định số 51/2008/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e0` Nghị định số 51/2008/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e2` ngày 22 tháng 4 năm 2008 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #07_2012_TT-BGTVT_27433#preamble_context_4 (Loại: `preamble_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[07/2012/TT-BGTVT]`<SO_HIEU>`** của **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** . **[Căn cứ]`<TU_KHOA_PHAP_LY>`** Công ước quốc tế về tiêu chuẩn huấn luyện , cấp chứng chỉ và trực ca cho thuyền viên 1978 sửa đổi 2010 mà Việt Nam là thành viên .

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **07/2012/TT-BGTVT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[4:7]`)
- `[e3]` **Căn cứ** → `TU_KHOA_PHAP_LY` (span: `[8:9]`)

**Quan hệ:**
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)


---

### Mẫu #07_2012_TT-BGTVT_27433#preamble_standalone_5 (Loại: `preamble_standalone`)
> **[Căn cứ]`<TU_KHOA_PHAP_LY>`** Công ước quốc tế về tiêu chuẩn huấn luyện , cấp chứng chỉ và trực ca cho thuyền viên 1978 sửa đổi 2010 mà Việt Nam là thành viên .

**Thực thể:**
- `[e0]` **Căn cứ** → `TU_KHOA_PHAP_LY` (span: `[0:1]`)


---

### Mẫu #07_2012_TT-BGTVT_27433#preamble_context_6 (Loại: `preamble_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[07/2012/TT-BGTVT]`<SO_HIEU>`** của **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** . **[Bộ trưởng Bộ Giao thông vận tải]`<CO_QUAN_THAM_QUYEN>`** ban hành Thông tư quy định về chức danh , nhiệm vụ theo chức danh của thuyền viên và đăng ký thuyền viên làm việc trên **[tàu biển]`<TAI_SAN_VAT_CHAT>`** Việt Nam .

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **07/2012/TT-BGTVT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[4:7]`)
- `[e3]` **Bộ trưởng Bộ Giao thông vận tải** → `CO_QUAN_THAM_QUYEN` (span: `[8:12]`)
- `[e4]` **tàu biển** → `TAI_SAN_VAT_CHAT` (span: `[28:29]`)

**Quan hệ:**
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)


---

### Mẫu #07_2012_TT-BGTVT_27433#preamble_standalone_7 (Loại: `preamble_standalone`)
> **[Bộ trưởng Bộ Giao thông vận tải]`<CO_QUAN_THAM_QUYEN>`** ban hành Thông tư quy định về chức danh , nhiệm vụ theo chức danh của thuyền viên và đăng ký thuyền viên làm việc trên **[tàu biển]`<TAI_SAN_VAT_CHAT>`** Việt Nam .

**Thực thể:**
- `[e0]` **Bộ trưởng Bộ Giao thông vận tải** → `CO_QUAN_THAM_QUYEN` (span: `[0:4]`)
- `[e1]` **tàu biển** → `TAI_SAN_VAT_CHAT` (span: `[20:21]`)


---

### Mẫu #07_2012_TT-BGTVT_27433#body_context_8 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[07/2012/TT-BGTVT]`<SO_HIEU>`** của **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Giao thông Vận tải]`<LINH_VUC>`** . **[Chương I. QUY ĐỊNH CHUNG]`<CHUONG>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **07/2012/TT-BGTVT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[4:7]`)
- `[e3]` **Giao thông Vận tải** → `LINH_VUC` (span: `[9:11]`)
- `[e4]` **Chương I. QUY ĐỊNH CHUNG** → `CHUONG` (span: `[12:16]`)

**Quan hệ:**
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Giao thông Vận tải `[LINH_VUC]`)
- (`e4` Chương I. QUY ĐỊNH CHUNG `[CHUONG]`) ==[ **THUOC_VE** ]==> (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`)
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Giao thông Vận tải `[LINH_VUC]`)


---

### Mẫu #07_2012_TT-BGTVT_27433#body_context_9 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[07/2012/TT-BGTVT]`<SO_HIEU>`** ban hành **[ngày 21 tháng 03 năm 2012]`<NGAY_BAN_HANH>`** bởi **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** . **[Chương I]`<CHUONG>`** . **[Điều 2 . Đối tượng áp dụng . Thông tư này áp dụng đối với thuyền viên làm việc trên **[tàu biển]`<TAI_SAN_VAT_CHAT>`** Việt Nam và cơ quan , tổ chức , cá nhân có liên quan . Đối với thuyền viên Việt Nam làm việc trên **[tàu biển]`<TAI_SAN_VAT_CHAT>`** nước ngoài chỉ áp dụng khi có những quy định cụ thể trong Thông tư này .]`<DIEU>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **07/2012/TT-BGTVT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[11:14]`)
- `[e3]` **ngày 21 tháng 03 năm 2012** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Chương I** → `CHUONG` (span: `[15:17]`)
- `[e5]` **Điều 2 . Đối tượng áp dụng . Thông tư này áp dụng đối với thuyền viên làm việc trên tàu biển Việt Nam và cơ quan , tổ chức , cá nhân có liên quan . Đối với thuyền viên Việt Nam làm việc trên tàu biển nước ngoài chỉ áp dụng khi có những quy định cụ thể trong Thông tư này .** → `DIEU` (span: `[18:60]`)
- `[e6]` **tàu biển** → `TAI_SAN_VAT_CHAT` (span: `[31:32]`) *(lồng trong `e5` (`DIEU`))*
- `[e7]` **tàu biển** → `TAI_SAN_VAT_CHAT` (span: `[47:48]`) *(lồng trong `e5` (`DIEU`))*

**Quan hệ:**
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 21 tháng 03 năm 2012 `[NGAY_BAN_HANH]`)
- (`e4` Chương I `[CHUONG]`) ==[ **THUOC_VE** ]==> (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`)
- (`e5` Điều 2 . Đối tượng áp dụng . Thông tư này áp dụng đối với thuyền viên làm việc trên tàu biển Việt Nam và cơ quan , tổ chức , cá nhân có liên quan . Đối với thuyền viên Việt Nam làm việc trên tàu biển nước ngoài chỉ áp dụng khi có những quy định cụ thể trong Thông tư này . `[DIEU]`) ==[ **THUOC_VE** ]==> (`e4` Chương I `[CHUONG]`)


---

### Mẫu #07_2012_TT-BGTVT_27433#body_context_10 (Loại: `body_context`)
> **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[07/2012/TT-BGTVT]`<SO_HIEU>`** . **[Điều 3]`<DIEU>`** . **[4 . Khi có Tổng Bí thư Đảng Cộng sản Việt Nam , Chủ tịch nước , Phó Chủ tịch nước , Chủ tịch **[Quốc hội]`<CO_QUAN_THAM_QUYEN>`** , Phó Chủ tịch **[Quốc hội]`<CO_QUAN_THAM_QUYEN>`** , **[Thủ tướng Chính phủ]`<CO_QUAN_THAM_QUYEN>`** , Phó **[Thủ tướng Chính phủ]`<CO_QUAN_THAM_QUYEN>`** nước Cộng hoà xã hội chủ nghĩa Việt Nam ở trên tàu , ngoài Quốc kỳ treo ở đỉnh cột phía lái còn phải treo thêm một Quốc kỳ ở đỉnh cột chính và chỉ được phép hạ xuống khi các vị khách nói trên đã rời khỏi tàu .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[4:5]`)
- `[e1]` **07/2012/TT-BGTVT** → `SO_HIEU` (span: `[6:7]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[0:3]`)
- `[e3]` **Điều 3** → `DIEU` (span: `[8:10]`)
- `[e4]` **4 . Khi có Tổng Bí thư Đảng Cộng sản Việt Nam , Chủ tịch nước , Phó Chủ tịch nước , Chủ tịch Quốc hội , Phó Chủ tịch Quốc hội , Thủ tướng Chính phủ , Phó Thủ tướng Chính phủ nước Cộng hoà xã hội chủ nghĩa Việt Nam ở trên tàu , ngoài Quốc kỳ treo ở đỉnh cột phía lái còn phải treo thêm một Quốc kỳ ở đỉnh cột chính và chỉ được phép hạ xuống khi các vị khách nói trên đã rời khỏi tàu .** → `KHOAN` (span: `[11:82]`)
- `[e5]` **Quốc hội** → `CO_QUAN_THAM_QUYEN` (span: `[27:28]`) *(lồng trong `e4` (`KHOAN`))*
- `[e6]` **Quốc hội** → `CO_QUAN_THAM_QUYEN` (span: `[30:31]`) *(lồng trong `e4` (`KHOAN`))*
- `[e7]` **Thủ tướng Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[32:34]`) *(lồng trong `e4` (`KHOAN`))*
- `[e8]` **Thủ tướng Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[36:38]`) *(lồng trong `e4` (`KHOAN`))*

**Quan hệ:**
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 3 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`)
- (`e4` 4 . Khi có Tổng Bí thư Đảng Cộng sản Việt Nam , Chủ tịch nước , Phó Chủ tịch nước , Chủ tịch Quốc hội , Phó Chủ tịch Quốc hội , Thủ tướng Chính phủ , Phó Thủ tướng Chính phủ nước Cộng hoà xã hội chủ nghĩa Việt Nam ở trên tàu , ngoài Quốc kỳ treo ở đỉnh cột phía lái còn phải treo thêm một Quốc kỳ ở đỉnh cột chính và chỉ được phép hạ xuống khi các vị khách nói trên đã rời khỏi tàu . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 3 `[DIEU]`)


---

### Mẫu #07_2012_TT-BGTVT_27433#body_standalone_11 (Loại: `body_standalone`)
> **[Điều 3]`<DIEU>`** . **[4 . Khi có Tổng Bí thư Đảng Cộng sản Việt Nam , Chủ tịch nước , Phó Chủ tịch nước , Chủ tịch **[Quốc hội]`<CO_QUAN_THAM_QUYEN>`** , Phó Chủ tịch **[Quốc hội]`<CO_QUAN_THAM_QUYEN>`** , **[Thủ tướng Chính phủ]`<CO_QUAN_THAM_QUYEN>`** , Phó **[Thủ tướng Chính phủ]`<CO_QUAN_THAM_QUYEN>`** nước Cộng hoà xã hội chủ nghĩa Việt Nam ở trên tàu , ngoài Quốc kỳ treo ở đỉnh cột phía lái còn phải treo thêm một Quốc kỳ ở đỉnh cột chính và chỉ được phép hạ xuống khi các vị khách nói trên đã rời khỏi tàu .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 3** → `DIEU` (span: `[0:2]`)
- `[e1]` **4 . Khi có Tổng Bí thư Đảng Cộng sản Việt Nam , Chủ tịch nước , Phó Chủ tịch nước , Chủ tịch Quốc hội , Phó Chủ tịch Quốc hội , Thủ tướng Chính phủ , Phó Thủ tướng Chính phủ nước Cộng hoà xã hội chủ nghĩa Việt Nam ở trên tàu , ngoài Quốc kỳ treo ở đỉnh cột phía lái còn phải treo thêm một Quốc kỳ ở đỉnh cột chính và chỉ được phép hạ xuống khi các vị khách nói trên đã rời khỏi tàu .** → `KHOAN` (span: `[3:74]`)
- `[e2]` **Quốc hội** → `CO_QUAN_THAM_QUYEN` (span: `[19:20]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **Quốc hội** → `CO_QUAN_THAM_QUYEN` (span: `[22:23]`) *(lồng trong `e1` (`KHOAN`))*
- `[e4]` **Thủ tướng Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[24:26]`) *(lồng trong `e1` (`KHOAN`))*
- `[e5]` **Thủ tướng Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[28:30]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 4 . Khi có Tổng Bí thư Đảng Cộng sản Việt Nam , Chủ tịch nước , Phó Chủ tịch nước , Chủ tịch Quốc hội , Phó Chủ tịch Quốc hội , Thủ tướng Chính phủ , Phó Thủ tướng Chính phủ nước Cộng hoà xã hội chủ nghĩa Việt Nam ở trên tàu , ngoài Quốc kỳ treo ở đỉnh cột phía lái còn phải treo thêm một Quốc kỳ ở đỉnh cột chính và chỉ được phép hạ xuống khi các vị khách nói trên đã rời khỏi tàu . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 3 `[DIEU]`)


---

### Mẫu #07_2012_TT-BGTVT_27433#body_context_12 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[07/2012/TT-BGTVT]`<SO_HIEU>`** ban hành **[ngày 21 tháng 03 năm 2012]`<NGAY_BAN_HANH>`** bởi **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** . **[Chương I]`<CHUONG>`** . **[Điều 5 . Đón khách thăm tàu . Khi có các vị khách được **[quy định tại]`<TU_KHOA_PHAP_LY>`** **[khoản 4 Điều 3 của Thông tư này]`<THAM_CHIEU_PHAP_LY>`** đến thăm tàu :]`<DIEU>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **07/2012/TT-BGTVT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[11:14]`)
- `[e3]` **ngày 21 tháng 03 năm 2012** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Chương I** → `CHUONG` (span: `[15:17]`)
- `[e5]` **Điều 5 . Đón khách thăm tàu . Khi có các vị khách được quy định tại khoản 4 Điều 3 của Thông tư này đến thăm tàu :** → `DIEU` (span: `[18:45]`)
- `[e6]` **khoản 4 Điều 3 của Thông tư này** → `THAM_CHIEU_PHAP_LY` (span: `[34:41]`) *(lồng trong `e5` (`DIEU`))*
- `[e7]` **quy định tại** → `TU_KHOA_PHAP_LY` (span: `[32:34]`) *(lồng trong `e5` (`DIEU`))*

**Quan hệ:**
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 21 tháng 03 năm 2012 `[NGAY_BAN_HANH]`)
- (`e4` Chương I `[CHUONG]`) ==[ **THUOC_VE** ]==> (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`)
- (`e5` Điều 5 . Đón khách thăm tàu . Khi có các vị khách được quy định tại khoản 4 Điều 3 của Thông tư này đến thăm tàu : `[DIEU]`) ==[ **THUOC_VE** ]==> (`e4` Chương I `[CHUONG]`)
- (`e7` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e6` khoản 4 Điều 3 của Thông tư này `[THAM_CHIEU_PHAP_LY]`)
- (`e5` Điều 5 . Đón khách thăm tàu . Khi có các vị khách được quy định tại khoản 4 Điều 3 của Thông tư này đến thăm tàu : `[DIEU]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e6` khoản 4 Điều 3 của Thông tư này `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #07_2012_TT-BGTVT_27433#body_standalone_13 (Loại: `body_standalone`)
> **[Điều 5 . Đón khách thăm tàu . Khi có các vị khách được **[quy định tại]`<TU_KHOA_PHAP_LY>`** **[khoản 4 Điều 3 của Thông tư này]`<THAM_CHIEU_PHAP_LY>`** đến thăm tàu :]`<DIEU>`**

**Thực thể:**
- `[e0]` **Điều 5 . Đón khách thăm tàu . Khi có các vị khách được quy định tại khoản 4 Điều 3 của Thông tư này đến thăm tàu :** → `DIEU` (span: `[0:27]`)
- `[e1]` **khoản 4 Điều 3 của Thông tư này** → `THAM_CHIEU_PHAP_LY` (span: `[16:23]`) *(lồng trong `e0` (`DIEU`))*
- `[e2]` **quy định tại** → `TU_KHOA_PHAP_LY` (span: `[14:16]`) *(lồng trong `e0` (`DIEU`))*

**Quan hệ:**
- (`e2` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e1` khoản 4 Điều 3 của Thông tư này `[THAM_CHIEU_PHAP_LY]`)
- (`e0` Điều 5 . Đón khách thăm tàu . Khi có các vị khách được quy định tại khoản 4 Điều 3 của Thông tư này đến thăm tàu : `[DIEU]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e1` khoản 4 Điều 3 của Thông tư này `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #07_2012_TT-BGTVT_27433#body_context_14 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[07/2012/TT-BGTVT]`<SO_HIEU>`** ban hành **[ngày 21 tháng 03 năm 2012]`<NGAY_BAN_HANH>`** bởi **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** . **[Điều 6]`<DIEU>`** . **[1 . Chức danh của thuyền viên trên **[tàu biển]`<TAI_SAN_VAT_CHAT>`** Việt Nam bao gồm : thuyền trưởng , đại phó , sỹ quan boong ( phó hai , phó ba ) , máy trưởng , máy hai , sỹ quan máy ( máy ba , máy tư ) , thuyền phó hành khách , sỹ quan thông tin vô tuyến , sỹ quan kỹ thuật điện , sỹ quan an ninh **[tàu biển]`<TAI_SAN_VAT_CHAT>`** , sỹ quan máy lạnh , thủy thủ trưởng , thủy thủ phó , thủy thủ trực ca , thợ máy chính , thợ máy trực ca , thợ kỹ thuật điện , nhân viên thông tin vô tuyến , quản trị , bác sỹ]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **07/2012/TT-BGTVT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[11:14]`)
- `[e3]` **ngày 21 tháng 03 năm 2012** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 6** → `DIEU` (span: `[15:17]`)
- `[e5]` **1 . Chức danh của thuyền viên trên tàu biển Việt Nam bao gồm : thuyền trưởng , đại phó , sỹ quan boong ( phó hai , phó ba ) , máy trưởng , máy hai , sỹ quan máy ( máy ba , máy tư ) , thuyền phó hành khách , sỹ quan thông tin vô tuyến , sỹ quan kỹ thuật điện , sỹ quan an ninh tàu biển , sỹ quan máy lạnh , thủy thủ trưởng , thủy thủ phó , thủy thủ trực ca , thợ máy chính , thợ máy trực ca , thợ kỹ thuật điện , nhân viên thông tin vô tuyến , quản trị , bác sỹ** → `KHOAN` (span: `[18:110]`)
- `[e6]` **tàu biển** → `TAI_SAN_VAT_CHAT` (span: `[24:25]`) *(lồng trong `e5` (`KHOAN`))*
- `[e7]` **tàu biển** → `TAI_SAN_VAT_CHAT` (span: `[77:78]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 21 tháng 03 năm 2012 `[NGAY_BAN_HANH]`)
- (`e4` Điều 6 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`)
- (`e5` 1 . Chức danh của thuyền viên trên tàu biển Việt Nam bao gồm : thuyền trưởng , đại phó , sỹ quan boong ( phó hai , phó ba ) , máy trưởng , máy hai , sỹ quan máy ( máy ba , máy tư ) , thuyền phó hành khách , sỹ quan thông tin vô tuyến , sỹ quan kỹ thuật điện , sỹ quan an ninh tàu biển , sỹ quan máy lạnh , thủy thủ trưởng , thủy thủ phó , thủy thủ trực ca , thợ máy chính , thợ máy trực ca , thợ kỹ thuật điện , nhân viên thông tin vô tuyến , quản trị , bác sỹ `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 6 `[DIEU]`)


---

### Mẫu #07_2012_TT-BGTVT_27433#body_standalone_15 (Loại: `body_standalone`)
> **[Điều 6]`<DIEU>`** . **[1 . Chức danh của thuyền viên trên **[tàu biển]`<TAI_SAN_VAT_CHAT>`** Việt Nam bao gồm : thuyền trưởng , đại phó , sỹ quan boong ( phó hai , phó ba ) , máy trưởng , máy hai , sỹ quan máy ( máy ba , máy tư ) , thuyền phó hành khách , sỹ quan thông tin vô tuyến , sỹ quan kỹ thuật điện , sỹ quan an ninh **[tàu biển]`<TAI_SAN_VAT_CHAT>`** , sỹ quan máy lạnh , thủy thủ trưởng , thủy thủ phó , thủy thủ trực ca , thợ máy chính , thợ máy trực ca , thợ kỹ thuật điện , nhân viên thông tin vô tuyến , quản trị , bác sỹ]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 6** → `DIEU` (span: `[0:2]`)
- `[e1]` **1 . Chức danh của thuyền viên trên tàu biển Việt Nam bao gồm : thuyền trưởng , đại phó , sỹ quan boong ( phó hai , phó ba ) , máy trưởng , máy hai , sỹ quan máy ( máy ba , máy tư ) , thuyền phó hành khách , sỹ quan thông tin vô tuyến , sỹ quan kỹ thuật điện , sỹ quan an ninh tàu biển , sỹ quan máy lạnh , thủy thủ trưởng , thủy thủ phó , thủy thủ trực ca , thợ máy chính , thợ máy trực ca , thợ kỹ thuật điện , nhân viên thông tin vô tuyến , quản trị , bác sỹ** → `KHOAN` (span: `[3:95]`)
- `[e2]` **tàu biển** → `TAI_SAN_VAT_CHAT` (span: `[9:10]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **tàu biển** → `TAI_SAN_VAT_CHAT` (span: `[62:63]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 1 . Chức danh của thuyền viên trên tàu biển Việt Nam bao gồm : thuyền trưởng , đại phó , sỹ quan boong ( phó hai , phó ba ) , máy trưởng , máy hai , sỹ quan máy ( máy ba , máy tư ) , thuyền phó hành khách , sỹ quan thông tin vô tuyến , sỹ quan kỹ thuật điện , sỹ quan an ninh tàu biển , sỹ quan máy lạnh , thủy thủ trưởng , thủy thủ phó , thủy thủ trực ca , thợ máy chính , thợ máy trực ca , thợ kỹ thuật điện , nhân viên thông tin vô tuyến , quản trị , bác sỹ `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 6 `[DIEU]`)


---

### Mẫu #07_2012_TT-BGTVT_27433#body_context_16 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[07/2012/TT-BGTVT]`<SO_HIEU>`** ban hành **[ngày 21 tháng 03 năm 2012]`<NGAY_BAN_HANH>`** bởi **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** . **[Điều 6]`<DIEU>`** . **[2 . Đối với các chức danh không được quy định cụ thể tại **[khoản 1 Điều này]`<THAM_CHIEU_PHAP_LY>`** thì chủ tàu căn cứ vào điều kiện kỹ thuật và mục đích sử dụng của tàu để bố trí các chức danh đó .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **07/2012/TT-BGTVT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[11:14]`)
- `[e3]` **ngày 21 tháng 03 năm 2012** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 6** → `DIEU` (span: `[15:17]`)
- `[e5]` **2 . Đối với các chức danh không được quy định cụ thể tại khoản 1 Điều này thì chủ tàu căn cứ vào điều kiện kỹ thuật và mục đích sử dụng của tàu để bố trí các chức danh đó .** → `KHOAN` (span: `[18:50]`)
- `[e6]` **khoản 1 Điều này** → `THAM_CHIEU_PHAP_LY` (span: `[28:32]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 21 tháng 03 năm 2012 `[NGAY_BAN_HANH]`)
- (`e4` Điều 6 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`)
- (`e5` 2 . Đối với các chức danh không được quy định cụ thể tại khoản 1 Điều này thì chủ tàu căn cứ vào điều kiện kỹ thuật và mục đích sử dụng của tàu để bố trí các chức danh đó . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 6 `[DIEU]`)
- (`e5` 2 . Đối với các chức danh không được quy định cụ thể tại khoản 1 Điều này thì chủ tàu căn cứ vào điều kiện kỹ thuật và mục đích sử dụng của tàu để bố trí các chức danh đó . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e6` khoản 1 Điều này `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #07_2012_TT-BGTVT_27433#body_context_17 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[07/2012/TT-BGTVT]`<SO_HIEU>`** ban hành **[ngày 21 tháng 03 năm 2012]`<NGAY_BAN_HANH>`** bởi **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** . **[Điều 7]`<DIEU>`** . **[Khoản 1]`<KHOAN>`** . **[b ) Khi giao , nhận tàu phải bàn giao chi tiết về phần vỏ tàu , các máy móc , **[trang thiết bị]`<TAI_SAN_VAT_CHAT>`** , **[tài sản]`<TAI_SAN_VAT_CHAT>`** , toàn bộ các hồ sơ , tài liệu , tiền mặt và phải lập bản thống kê từng hạng mục ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **07/2012/TT-BGTVT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[11:14]`)
- `[e3]` **ngày 21 tháng 03 năm 2012** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 7** → `DIEU` (span: `[15:17]`)
- `[e5]` **Khoản 1** → `KHOAN` (span: `[18:20]`)
- `[e6]` **b ) Khi giao , nhận tàu phải bàn giao chi tiết về phần vỏ tàu , các máy móc , trang thiết bị , tài sản , toàn bộ các hồ sơ , tài liệu , tiền mặt và phải lập bản thống kê từng hạng mục ;** → `DIEM` (span: `[21:59]`)
- `[e7]` **trang thiết bị** → `TAI_SAN_VAT_CHAT` (span: `[39:41]`) *(lồng trong `e6` (`DIEM`))*
- `[e8]` **tài sản** → `TAI_SAN_VAT_CHAT` (span: `[42:43]`) *(lồng trong `e6` (`DIEM`))*

**Quan hệ:**
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 21 tháng 03 năm 2012 `[NGAY_BAN_HANH]`)
- (`e4` Điều 7 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`)
- (`e5` Khoản 1 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 7 `[DIEU]`)
- (`e6` b ) Khi giao , nhận tàu phải bàn giao chi tiết về phần vỏ tàu , các máy móc , trang thiết bị , tài sản , toàn bộ các hồ sơ , tài liệu , tiền mặt và phải lập bản thống kê từng hạng mục ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e5` Khoản 1 `[KHOAN]`)


---

### Mẫu #07_2012_TT-BGTVT_27433#body_standalone_18 (Loại: `body_standalone`)
> **[Điều 7]`<DIEU>`** . **[Khoản 1]`<KHOAN>`** . **[b ) Khi giao , nhận tàu phải bàn giao chi tiết về phần vỏ tàu , các máy móc , **[trang thiết bị]`<TAI_SAN_VAT_CHAT>`** , **[tài sản]`<TAI_SAN_VAT_CHAT>`** , toàn bộ các hồ sơ , tài liệu , tiền mặt và phải lập bản thống kê từng hạng mục ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Điều 7** → `DIEU` (span: `[0:2]`)
- `[e1]` **Khoản 1** → `KHOAN` (span: `[3:5]`)
- `[e2]` **b ) Khi giao , nhận tàu phải bàn giao chi tiết về phần vỏ tàu , các máy móc , trang thiết bị , tài sản , toàn bộ các hồ sơ , tài liệu , tiền mặt và phải lập bản thống kê từng hạng mục ;** → `DIEM` (span: `[6:44]`)
- `[e3]` **trang thiết bị** → `TAI_SAN_VAT_CHAT` (span: `[24:26]`) *(lồng trong `e2` (`DIEM`))*
- `[e4]` **tài sản** → `TAI_SAN_VAT_CHAT` (span: `[27:28]`) *(lồng trong `e2` (`DIEM`))*

**Quan hệ:**
- (`e1` Khoản 1 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 7 `[DIEU]`)
- (`e2` b ) Khi giao , nhận tàu phải bàn giao chi tiết về phần vỏ tàu , các máy móc , trang thiết bị , tài sản , toàn bộ các hồ sơ , tài liệu , tiền mặt và phải lập bản thống kê từng hạng mục ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e1` Khoản 1 `[KHOAN]`)


---

### Mẫu #07_2012_TT-BGTVT_27433#body_context_19 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[07/2012/TT-BGTVT]`<SO_HIEU>`** của **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Giao thông Vận tải]`<LINH_VUC>`** . **[Điều 7]`<DIEU>`** . **[Khoản 2]`<KHOAN>`** . **[e ) Kiểm tra việc xếp dỡ **[hàng hóa]`<TAI_SAN_VAT_CHAT>`** theo sơ đồ **[hàng hóa]`<TAI_SAN_VAT_CHAT>`** bảo đảm số lượng và chất lượng của **[hàng hóa]`<TAI_SAN_VAT_CHAT>`** . Đặc biệt , chú ý xếp dỡ và vận chuyển hàng rời , hàng nguy hiểm trên tàu ; tận dụng dung tích và trọng tải của tàu nhưng phải đảm bảo tính ổn định và an toàn của tàu ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **07/2012/TT-BGTVT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[4:7]`)
- `[e3]` **Giao thông Vận tải** → `LINH_VUC` (span: `[9:11]`)
- `[e4]` **Điều 7** → `DIEU` (span: `[12:14]`)
- `[e5]` **Khoản 2** → `KHOAN` (span: `[15:17]`)
- `[e6]` **e ) Kiểm tra việc xếp dỡ hàng hóa theo sơ đồ hàng hóa bảo đảm số lượng và chất lượng của hàng hóa . Đặc biệt , chú ý xếp dỡ và vận chuyển hàng rời , hàng nguy hiểm trên tàu ; tận dụng dung tích và trọng tải của tàu nhưng phải đảm bảo tính ổn định và an toàn của tàu ;** → `DIEM` (span: `[18:64]`)
- `[e7]` **hàng hóa** → `TAI_SAN_VAT_CHAT` (span: `[23:24]`) *(lồng trong `e6` (`DIEM`))*
- `[e8]` **hàng hóa** → `TAI_SAN_VAT_CHAT` (span: `[26:27]`) *(lồng trong `e6` (`DIEM`))*
- `[e9]` **hàng hóa** → `TAI_SAN_VAT_CHAT` (span: `[32:33]`) *(lồng trong `e6` (`DIEM`))*

**Quan hệ:**
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Giao thông Vận tải `[LINH_VUC]`)
- (`e4` Điều 7 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`)
- (`e5` Khoản 2 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 7 `[DIEU]`)
- (`e6` e ) Kiểm tra việc xếp dỡ hàng hóa theo sơ đồ hàng hóa bảo đảm số lượng và chất lượng của hàng hóa . Đặc biệt , chú ý xếp dỡ và vận chuyển hàng rời , hàng nguy hiểm trên tàu ; tận dụng dung tích và trọng tải của tàu nhưng phải đảm bảo tính ổn định và an toàn của tàu ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e5` Khoản 2 `[KHOAN]`)
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Giao thông Vận tải `[LINH_VUC]`)
- (`e6` e ) Kiểm tra việc xếp dỡ hàng hóa theo sơ đồ hàng hóa bảo đảm số lượng và chất lượng của hàng hóa . Đặc biệt , chú ý xếp dỡ và vận chuyển hàng rời , hàng nguy hiểm trên tàu ; tận dụng dung tích và trọng tải của tàu nhưng phải đảm bảo tính ổn định và an toàn của tàu ; `[DIEM]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Giao thông Vận tải `[LINH_VUC]`)


---

### Mẫu #07_2012_TT-BGTVT_27433#body_standalone_20 (Loại: `body_standalone`)
> **[Điều 7]`<DIEU>`** . **[Khoản 2]`<KHOAN>`** . **[e ) Kiểm tra việc xếp dỡ **[hàng hóa]`<TAI_SAN_VAT_CHAT>`** theo sơ đồ **[hàng hóa]`<TAI_SAN_VAT_CHAT>`** bảo đảm số lượng và chất lượng của **[hàng hóa]`<TAI_SAN_VAT_CHAT>`** . Đặc biệt , chú ý xếp dỡ và vận chuyển hàng rời , hàng nguy hiểm trên tàu ; tận dụng dung tích và trọng tải của tàu nhưng phải đảm bảo tính ổn định và an toàn của tàu ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Điều 7** → `DIEU` (span: `[0:2]`)
- `[e1]` **Khoản 2** → `KHOAN` (span: `[3:5]`)
- `[e2]` **e ) Kiểm tra việc xếp dỡ hàng hóa theo sơ đồ hàng hóa bảo đảm số lượng và chất lượng của hàng hóa . Đặc biệt , chú ý xếp dỡ và vận chuyển hàng rời , hàng nguy hiểm trên tàu ; tận dụng dung tích và trọng tải của tàu nhưng phải đảm bảo tính ổn định và an toàn của tàu ;** → `DIEM` (span: `[6:52]`)
- `[e3]` **hàng hóa** → `TAI_SAN_VAT_CHAT` (span: `[11:12]`) *(lồng trong `e2` (`DIEM`))*
- `[e4]` **hàng hóa** → `TAI_SAN_VAT_CHAT` (span: `[14:15]`) *(lồng trong `e2` (`DIEM`))*
- `[e5]` **hàng hóa** → `TAI_SAN_VAT_CHAT` (span: `[20:21]`) *(lồng trong `e2` (`DIEM`))*

**Quan hệ:**
- (`e1` Khoản 2 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 7 `[DIEU]`)
- (`e2` e ) Kiểm tra việc xếp dỡ hàng hóa theo sơ đồ hàng hóa bảo đảm số lượng và chất lượng của hàng hóa . Đặc biệt , chú ý xếp dỡ và vận chuyển hàng rời , hàng nguy hiểm trên tàu ; tận dụng dung tích và trọng tải của tàu nhưng phải đảm bảo tính ổn định và an toàn của tàu ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e1` Khoản 2 `[KHOAN]`)


---

### Mẫu #07_2012_TT-BGTVT_27433#body_context_21 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[07/2012/TT-BGTVT]`<SO_HIEU>`** ban hành **[ngày 21 tháng 03 năm 2012]`<NGAY_BAN_HANH>`** bởi **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** . **[Điều 7]`<DIEU>`** . **[Khoản 3]`<KHOAN>`** . **[d ) Khẩn trương có mặt ở buồng lái khi sỹ quan trực ca boong đề nghị và có mặt thường xuyên ở buồng lái khi tàu hành trình trong luồng hẹp , eo biển , kênh đào , gần bờ , khi ra vào cảng , trong các khu vực nguy hiểm , khi thời tiết xấu , tầm nhìn xa bị hạn chế hoặc qua những khu vực có mật độ **[phương tiện thủy]`<TAI_SAN_VAT_CHAT>`** cao . Trong các trường hợp nói trên , thuyền trưởng phải áp dụng các biện pháp thích hợp , chuẩn bị neo ở]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **07/2012/TT-BGTVT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[11:14]`)
- `[e3]` **ngày 21 tháng 03 năm 2012** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 7** → `DIEU` (span: `[15:17]`)
- `[e5]` **Khoản 3** → `KHOAN` (span: `[18:20]`)
- `[e6]` **d ) Khẩn trương có mặt ở buồng lái khi sỹ quan trực ca boong đề nghị và có mặt thường xuyên ở buồng lái khi tàu hành trình trong luồng hẹp , eo biển , kênh đào , gần bờ , khi ra vào cảng , trong các khu vực nguy hiểm , khi thời tiết xấu , tầm nhìn xa bị hạn chế hoặc qua những khu vực có mật độ phương tiện thủy cao . Trong các trường hợp nói trên , thuyền trưởng phải áp dụng các biện pháp thích hợp , chuẩn bị neo ở** → `DIEM` (span: `[21:97]`)
- `[e7]` **phương tiện thủy** → `TAI_SAN_VAT_CHAT` (span: `[78:79]`) *(lồng trong `e6` (`DIEM`))*

**Quan hệ:**
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 21 tháng 03 năm 2012 `[NGAY_BAN_HANH]`)
- (`e4` Điều 7 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`)
- (`e5` Khoản 3 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 7 `[DIEU]`)
- (`e6` d ) Khẩn trương có mặt ở buồng lái khi sỹ quan trực ca boong đề nghị và có mặt thường xuyên ở buồng lái khi tàu hành trình trong luồng hẹp , eo biển , kênh đào , gần bờ , khi ra vào cảng , trong các khu vực nguy hiểm , khi thời tiết xấu , tầm nhìn xa bị hạn chế hoặc qua những khu vực có mật độ phương tiện thủy cao . Trong các trường hợp nói trên , thuyền trưởng phải áp dụng các biện pháp thích hợp , chuẩn bị neo ở `[DIEM]`) ==[ **THUOC_VE** ]==> (`e5` Khoản 3 `[KHOAN]`)


---

### Mẫu #07_2012_TT-BGTVT_27433#body_standalone_22 (Loại: `body_standalone`)
> **[Điều 7]`<DIEU>`** . **[Khoản 3]`<KHOAN>`** . **[d ) Khẩn trương có mặt ở buồng lái khi sỹ quan trực ca boong đề nghị và có mặt thường xuyên ở buồng lái khi tàu hành trình trong luồng hẹp , eo biển , kênh đào , gần bờ , khi ra vào cảng , trong các khu vực nguy hiểm , khi thời tiết xấu , tầm nhìn xa bị hạn chế hoặc qua những khu vực có mật độ **[phương tiện thủy]`<TAI_SAN_VAT_CHAT>`** cao . Trong các trường hợp nói trên , thuyền trưởng phải áp dụng các biện pháp thích hợp , chuẩn bị neo ở]`<DIEM>`**

**Thực thể:**
- `[e0]` **Điều 7** → `DIEU` (span: `[0:2]`)
- `[e1]` **Khoản 3** → `KHOAN` (span: `[3:5]`)
- `[e2]` **d ) Khẩn trương có mặt ở buồng lái khi sỹ quan trực ca boong đề nghị và có mặt thường xuyên ở buồng lái khi tàu hành trình trong luồng hẹp , eo biển , kênh đào , gần bờ , khi ra vào cảng , trong các khu vực nguy hiểm , khi thời tiết xấu , tầm nhìn xa bị hạn chế hoặc qua những khu vực có mật độ phương tiện thủy cao . Trong các trường hợp nói trên , thuyền trưởng phải áp dụng các biện pháp thích hợp , chuẩn bị neo ở** → `DIEM` (span: `[6:82]`)
- `[e3]` **phương tiện thủy** → `TAI_SAN_VAT_CHAT` (span: `[63:64]`) *(lồng trong `e2` (`DIEM`))*

**Quan hệ:**
- (`e1` Khoản 3 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 7 `[DIEU]`)
- (`e2` d ) Khẩn trương có mặt ở buồng lái khi sỹ quan trực ca boong đề nghị và có mặt thường xuyên ở buồng lái khi tàu hành trình trong luồng hẹp , eo biển , kênh đào , gần bờ , khi ra vào cảng , trong các khu vực nguy hiểm , khi thời tiết xấu , tầm nhìn xa bị hạn chế hoặc qua những khu vực có mật độ phương tiện thủy cao . Trong các trường hợp nói trên , thuyền trưởng phải áp dụng các biện pháp thích hợp , chuẩn bị neo ở `[DIEM]`) ==[ **THUOC_VE** ]==> (`e1` Khoản 3 `[KHOAN]`)


---

### Mẫu #07_2012_TT-BGTVT_27433#body_context_23 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[07/2012/TT-BGTVT]`<SO_HIEU>`** của **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Giao thông Vận tải]`<LINH_VUC>`** . **[Điều 7]`<DIEU>`** . **[Khoản 10]`<KHOAN>`** . **[e ) Phải có mặt ở buồng lái khi điều động tàu thuyền ra , vào cảng hoặc cập , rời cầu cảng , khu neo đậu . Khi tàu neo đậu ở các khu vực mà các điều kiện an toàn hàng hải **[không đảm bảo , thuyền trưởng phải thường xuyên có mặt ở tàu]`<HANH_VI_VI_PHAM>`** . Nếu phải vắng mặt trên tàu thì yêu cầu đại phó ở lại tàu để thay mặt mình xử lý kịp thời những tình huống có thể xảy ra ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **07/2012/TT-BGTVT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[4:7]`)
- `[e3]` **Giao thông Vận tải** → `LINH_VUC` (span: `[9:11]`)
- `[e4]` **Điều 7** → `DIEU` (span: `[12:14]`)
- `[e5]` **Khoản 10** → `KHOAN` (span: `[15:17]`)
- `[e6]` **e ) Phải có mặt ở buồng lái khi điều động tàu thuyền ra , vào cảng hoặc cập , rời cầu cảng , khu neo đậu . Khi tàu neo đậu ở các khu vực mà các điều kiện an toàn hàng hải không đảm bảo , thuyền trưởng phải thường xuyên có mặt ở tàu . Nếu phải vắng mặt trên tàu thì yêu cầu đại phó ở lại tàu để thay mặt mình xử lý kịp thời những tình huống có thể xảy ra ;** → `DIEM` (span: `[18:86]`)
- `[e7]` **không đảm bảo , thuyền trưởng phải thường xuyên có mặt ở tàu** → `HANH_VI_VI_PHAM` (span: `[53:62]`) *(lồng trong `e6` (`DIEM`))*

**Quan hệ:**
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Giao thông Vận tải `[LINH_VUC]`)
- (`e4` Điều 7 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`)
- (`e5` Khoản 10 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 7 `[DIEU]`)
- (`e6` e ) Phải có mặt ở buồng lái khi điều động tàu thuyền ra , vào cảng hoặc cập , rời cầu cảng , khu neo đậu . Khi tàu neo đậu ở các khu vực mà các điều kiện an toàn hàng hải không đảm bảo , thuyền trưởng phải thường xuyên có mặt ở tàu . Nếu phải vắng mặt trên tàu thì yêu cầu đại phó ở lại tàu để thay mặt mình xử lý kịp thời những tình huống có thể xảy ra ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e5` Khoản 10 `[KHOAN]`)
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Giao thông Vận tải `[LINH_VUC]`)
- (`e7` không đảm bảo , thuyền trưởng phải thường xuyên có mặt ở tàu `[HANH_VI_VI_PHAM]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Giao thông Vận tải `[LINH_VUC]`)


---

### Mẫu #07_2012_TT-BGTVT_27433#body_standalone_24 (Loại: `body_standalone`)
> **[Điều 7]`<DIEU>`** . **[Khoản 10]`<KHOAN>`** . **[e ) Phải có mặt ở buồng lái khi điều động tàu thuyền ra , vào cảng hoặc cập , rời cầu cảng , khu neo đậu . Khi tàu neo đậu ở các khu vực mà các điều kiện an toàn hàng hải **[không đảm bảo , thuyền trưởng phải thường xuyên có mặt ở tàu]`<HANH_VI_VI_PHAM>`** . Nếu phải vắng mặt trên tàu thì yêu cầu đại phó ở lại tàu để thay mặt mình xử lý kịp thời những tình huống có thể xảy ra ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Điều 7** → `DIEU` (span: `[0:2]`)
- `[e1]` **Khoản 10** → `KHOAN` (span: `[3:5]`)
- `[e2]` **e ) Phải có mặt ở buồng lái khi điều động tàu thuyền ra , vào cảng hoặc cập , rời cầu cảng , khu neo đậu . Khi tàu neo đậu ở các khu vực mà các điều kiện an toàn hàng hải không đảm bảo , thuyền trưởng phải thường xuyên có mặt ở tàu . Nếu phải vắng mặt trên tàu thì yêu cầu đại phó ở lại tàu để thay mặt mình xử lý kịp thời những tình huống có thể xảy ra ;** → `DIEM` (span: `[6:74]`)
- `[e3]` **không đảm bảo , thuyền trưởng phải thường xuyên có mặt ở tàu** → `HANH_VI_VI_PHAM` (span: `[41:50]`) *(lồng trong `e2` (`DIEM`))*

**Quan hệ:**
- (`e1` Khoản 10 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 7 `[DIEU]`)
- (`e2` e ) Phải có mặt ở buồng lái khi điều động tàu thuyền ra , vào cảng hoặc cập , rời cầu cảng , khu neo đậu . Khi tàu neo đậu ở các khu vực mà các điều kiện an toàn hàng hải không đảm bảo , thuyền trưởng phải thường xuyên có mặt ở tàu . Nếu phải vắng mặt trên tàu thì yêu cầu đại phó ở lại tàu để thay mặt mình xử lý kịp thời những tình huống có thể xảy ra ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e1` Khoản 10 `[KHOAN]`)


---

### Mẫu #07_2012_TT-BGTVT_27433#body_context_25 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[07/2012/TT-BGTVT]`<SO_HIEU>`** của **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Giao thông Vận tải]`<LINH_VUC>`** . **[Điều 7]`<DIEU>`** . **[11 . Nhiệm vụ của thuyền trưởng khi tàu chở khách : Áp dụng các biện pháp cần thiết để bảo đảm an toàn tuyệt đối cho hành khách , thuyền viên , hàng hoá , hành lý và **[tài sản]`<TAI_SAN_VAT_CHAT>`** trên tàu ; tổ chức huấn luyện cứu sinh , cứu hoả , cứu thủng tàu cho thuyền viên và tổ chức hướng dẫn cho hành khách làm quen , sử dụng **[phương tiện]`<TAI_SAN_VAT_CHAT>`** cứu sinh , cứu hoả và các thiết bị an toàn khác .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **07/2012/TT-BGTVT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[4:7]`)
- `[e3]` **Giao thông Vận tải** → `LINH_VUC` (span: `[9:11]`)
- `[e4]` **Điều 7** → `DIEU` (span: `[12:14]`)
- `[e5]` **11 . Nhiệm vụ của thuyền trưởng khi tàu chở khách : Áp dụng các biện pháp cần thiết để bảo đảm an toàn tuyệt đối cho hành khách , thuyền viên , hàng hoá , hành lý và tài sản trên tàu ; tổ chức huấn luyện cứu sinh , cứu hoả , cứu thủng tàu cho thuyền viên và tổ chức hướng dẫn cho hành khách làm quen , sử dụng phương tiện cứu sinh , cứu hoả và các thiết bị an toàn khác .** → `KHOAN` (span: `[15:75]`)
- `[e6]` **tài sản** → `TAI_SAN_VAT_CHAT` (span: `[42:43]`) *(lồng trong `e5` (`KHOAN`))*
- `[e7]` **phương tiện** → `TAI_SAN_VAT_CHAT` (span: `[65:66]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Giao thông Vận tải `[LINH_VUC]`)
- (`e4` Điều 7 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`)
- (`e5` 11 . Nhiệm vụ của thuyền trưởng khi tàu chở khách : Áp dụng các biện pháp cần thiết để bảo đảm an toàn tuyệt đối cho hành khách , thuyền viên , hàng hoá , hành lý và tài sản trên tàu ; tổ chức huấn luyện cứu sinh , cứu hoả , cứu thủng tàu cho thuyền viên và tổ chức hướng dẫn cho hành khách làm quen , sử dụng phương tiện cứu sinh , cứu hoả và các thiết bị an toàn khác . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 7 `[DIEU]`)
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Giao thông Vận tải `[LINH_VUC]`)
- (`e5` 11 . Nhiệm vụ của thuyền trưởng khi tàu chở khách : Áp dụng các biện pháp cần thiết để bảo đảm an toàn tuyệt đối cho hành khách , thuyền viên , hàng hoá , hành lý và tài sản trên tàu ; tổ chức huấn luyện cứu sinh , cứu hoả , cứu thủng tàu cho thuyền viên và tổ chức hướng dẫn cho hành khách làm quen , sử dụng phương tiện cứu sinh , cứu hoả và các thiết bị an toàn khác . `[KHOAN]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Giao thông Vận tải `[LINH_VUC]`)


---

### Mẫu #07_2012_TT-BGTVT_27433#body_standalone_26 (Loại: `body_standalone`)
> **[Điều 7]`<DIEU>`** . **[11 . Nhiệm vụ của thuyền trưởng khi tàu chở khách : Áp dụng các biện pháp cần thiết để bảo đảm an toàn tuyệt đối cho hành khách , thuyền viên , hàng hoá , hành lý và **[tài sản]`<TAI_SAN_VAT_CHAT>`** trên tàu ; tổ chức huấn luyện cứu sinh , cứu hoả , cứu thủng tàu cho thuyền viên và tổ chức hướng dẫn cho hành khách làm quen , sử dụng **[phương tiện]`<TAI_SAN_VAT_CHAT>`** cứu sinh , cứu hoả và các thiết bị an toàn khác .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 7** → `DIEU` (span: `[0:2]`)
- `[e1]` **11 . Nhiệm vụ của thuyền trưởng khi tàu chở khách : Áp dụng các biện pháp cần thiết để bảo đảm an toàn tuyệt đối cho hành khách , thuyền viên , hàng hoá , hành lý và tài sản trên tàu ; tổ chức huấn luyện cứu sinh , cứu hoả , cứu thủng tàu cho thuyền viên và tổ chức hướng dẫn cho hành khách làm quen , sử dụng phương tiện cứu sinh , cứu hoả và các thiết bị an toàn khác .** → `KHOAN` (span: `[3:63]`)
- `[e2]` **tài sản** → `TAI_SAN_VAT_CHAT` (span: `[30:31]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **phương tiện** → `TAI_SAN_VAT_CHAT` (span: `[53:54]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 11 . Nhiệm vụ của thuyền trưởng khi tàu chở khách : Áp dụng các biện pháp cần thiết để bảo đảm an toàn tuyệt đối cho hành khách , thuyền viên , hàng hoá , hành lý và tài sản trên tàu ; tổ chức huấn luyện cứu sinh , cứu hoả , cứu thủng tàu cho thuyền viên và tổ chức hướng dẫn cho hành khách làm quen , sử dụng phương tiện cứu sinh , cứu hoả và các thiết bị an toàn khác . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 7 `[DIEU]`)


---

### Mẫu #07_2012_TT-BGTVT_27433#body_context_27 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[07/2012/TT-BGTVT]`<SO_HIEU>`** ban hành **[ngày 21 tháng 03 năm 2012]`<NGAY_BAN_HANH>`** bởi **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** . **[Điều 7]`<DIEU>`** . **[13 . Nhiệm vụ của thuyền trưởng khi sửa chữa tàu :]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **07/2012/TT-BGTVT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[11:14]`)
- `[e3]` **ngày 21 tháng 03 năm 2012** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 7** → `DIEU` (span: `[15:17]`)
- `[e5]` **13 . Nhiệm vụ của thuyền trưởng khi sửa chữa tàu :** → `KHOAN` (span: `[18:27]`)

**Quan hệ:**
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 21 tháng 03 năm 2012 `[NGAY_BAN_HANH]`)
- (`e4` Điều 7 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`)
- (`e5` 13 . Nhiệm vụ của thuyền trưởng khi sửa chữa tàu : `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 7 `[DIEU]`)


---

### Mẫu #07_2012_TT-BGTVT_27433#body_context_28 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[07/2012/TT-BGTVT]`<SO_HIEU>`** ban hành **[ngày 21 tháng 03 năm 2012]`<NGAY_BAN_HANH>`** bởi **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** . **[Điều 8]`<DIEU>`** . **[9 . Trường hợp thuyền trưởng vắng mặt , nếu xảy ra tình huống cấp bách **[không bảo đảm an toàn cho tàu hoặc]`<HANH_VI_VI_PHAM>`** khi có lệnh của **[Giám đốc]`<CHU_THE_CA_NHAN>`** **[cảng vụ hàng hải]`<CO_QUAN_THAM_QUYEN>`** hay chủ tàu thì đại phó có trách nhiệm yêu cầu hoa tiêu đến để điều động tàu đảm bảo an toàn ;]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **07/2012/TT-BGTVT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[11:14]`)
- `[e3]` **ngày 21 tháng 03 năm 2012** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 8** → `DIEU` (span: `[15:17]`)
- `[e5]` **9 . Trường hợp thuyền trưởng vắng mặt , nếu xảy ra tình huống cấp bách không bảo đảm an toàn cho tàu hoặc khi có lệnh của Giám đốc cảng vụ hàng hải hay chủ tàu thì đại phó có trách nhiệm yêu cầu hoa tiêu đến để điều động tàu đảm bảo an toàn ;** → `KHOAN` (span: `[18:58]`)
- `[e6]` **không bảo đảm an toàn cho tàu hoặc** → `HANH_VI_VI_PHAM` (span: `[29:35]`) *(lồng trong `e5` (`KHOAN`))*
- `[e7]` **cảng vụ hàng hải** → `CO_QUAN_THAM_QUYEN` (span: `[40:42]`) *(lồng trong `e5` (`KHOAN`))*
- `[e8]` **Giám đốc** → `CHU_THE_CA_NHAN` (span: `[39:40]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 21 tháng 03 năm 2012 `[NGAY_BAN_HANH]`)
- (`e4` Điều 8 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`)
- (`e5` 9 . Trường hợp thuyền trưởng vắng mặt , nếu xảy ra tình huống cấp bách không bảo đảm an toàn cho tàu hoặc khi có lệnh của Giám đốc cảng vụ hàng hải hay chủ tàu thì đại phó có trách nhiệm yêu cầu hoa tiêu đến để điều động tàu đảm bảo an toàn ; `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 8 `[DIEU]`)
- (`e8` Giám đốc `[CHU_THE_CA_NHAN]`) ==[ **THUC_HIEN_VI_PHAM** ]==> (`e6` không bảo đảm an toàn cho tàu hoặc `[HANH_VI_VI_PHAM]`)


---

### Mẫu #07_2012_TT-BGTVT_27433#body_standalone_29 (Loại: `body_standalone`)
> **[Điều 8]`<DIEU>`** . **[9 . Trường hợp thuyền trưởng vắng mặt , nếu xảy ra tình huống cấp bách **[không bảo đảm an toàn cho tàu hoặc]`<HANH_VI_VI_PHAM>`** khi có lệnh của **[Giám đốc]`<CHU_THE_CA_NHAN>`** **[cảng vụ hàng hải]`<CO_QUAN_THAM_QUYEN>`** hay chủ tàu thì đại phó có trách nhiệm yêu cầu hoa tiêu đến để điều động tàu đảm bảo an toàn ;]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 8** → `DIEU` (span: `[0:2]`)
- `[e1]` **9 . Trường hợp thuyền trưởng vắng mặt , nếu xảy ra tình huống cấp bách không bảo đảm an toàn cho tàu hoặc khi có lệnh của Giám đốc cảng vụ hàng hải hay chủ tàu thì đại phó có trách nhiệm yêu cầu hoa tiêu đến để điều động tàu đảm bảo an toàn ;** → `KHOAN` (span: `[3:43]`)
- `[e2]` **không bảo đảm an toàn cho tàu hoặc** → `HANH_VI_VI_PHAM` (span: `[14:20]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **cảng vụ hàng hải** → `CO_QUAN_THAM_QUYEN` (span: `[25:27]`) *(lồng trong `e1` (`KHOAN`))*
- `[e4]` **Giám đốc** → `CHU_THE_CA_NHAN` (span: `[24:25]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 9 . Trường hợp thuyền trưởng vắng mặt , nếu xảy ra tình huống cấp bách không bảo đảm an toàn cho tàu hoặc khi có lệnh của Giám đốc cảng vụ hàng hải hay chủ tàu thì đại phó có trách nhiệm yêu cầu hoa tiêu đến để điều động tàu đảm bảo an toàn ; `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 8 `[DIEU]`)
- (`e4` Giám đốc `[CHU_THE_CA_NHAN]`) ==[ **THUC_HIEN_VI_PHAM** ]==> (`e2` không bảo đảm an toàn cho tàu hoặc `[HANH_VI_VI_PHAM]`)


---

### Mẫu #07_2012_TT-BGTVT_27433#body_context_30 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[07/2012/TT-BGTVT]`<SO_HIEU>`** ban hành **[ngày 21 tháng 03 năm 2012]`<NGAY_BAN_HANH>`** bởi **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** . **[Điều 8]`<DIEU>`** . **[12 . Tổ chức giao nhận **[hàng hóa]`<TAI_SAN_VAT_CHAT>`** , bưu kiện , bưu phẩm và chuẩn bị các giấy tờ về **[hàng hóa]`<TAI_SAN_VAT_CHAT>`** trình thuyền trưởng ; hàng ngày phải báo cáo thuyền trưởng biết về tình hình làm hàng và số lượng hàng hoá xếp dỡ được ; trước khi xếp **[hàng hóa]`<TAI_SAN_VAT_CHAT>`** , có nhiệm vụ lập sơ đồ xếp dỡ hàng hoá theo yêu cầu của thuyền trưởng nhằm tận dụng dung tích và trọng tải của tàu , bảo đảm đúng quy định về xếp dỡ , vận chuyển hàng hoá trên tàu ; đặc biệt , chú]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **07/2012/TT-BGTVT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[11:14]`)
- `[e3]` **ngày 21 tháng 03 năm 2012** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 8** → `DIEU` (span: `[15:17]`)
- `[e5]` **12 . Tổ chức giao nhận hàng hóa , bưu kiện , bưu phẩm và chuẩn bị các giấy tờ về hàng hóa trình thuyền trưởng ; hàng ngày phải báo cáo thuyền trưởng biết về tình hình làm hàng và số lượng hàng hoá xếp dỡ được ; trước khi xếp hàng hóa , có nhiệm vụ lập sơ đồ xếp dỡ hàng hoá theo yêu cầu của thuyền trưởng nhằm tận dụng dung tích và trọng tải của tàu , bảo đảm đúng quy định về xếp dỡ , vận chuyển hàng hoá trên tàu ; đặc biệt , chú** → `KHOAN` (span: `[18:88]`)
- `[e6]` **hàng hóa** → `TAI_SAN_VAT_CHAT` (span: `[22:23]`) *(lồng trong `e5` (`KHOAN`))*
- `[e7]` **hàng hóa** → `TAI_SAN_VAT_CHAT` (span: `[32:33]`) *(lồng trong `e5` (`KHOAN`))*
- `[e8]` **hàng hóa** → `TAI_SAN_VAT_CHAT` (span: `[54:55]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 21 tháng 03 năm 2012 `[NGAY_BAN_HANH]`)
- (`e4` Điều 8 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`)
- (`e5` 12 . Tổ chức giao nhận hàng hóa , bưu kiện , bưu phẩm và chuẩn bị các giấy tờ về hàng hóa trình thuyền trưởng ; hàng ngày phải báo cáo thuyền trưởng biết về tình hình làm hàng và số lượng hàng hoá xếp dỡ được ; trước khi xếp hàng hóa , có nhiệm vụ lập sơ đồ xếp dỡ hàng hoá theo yêu cầu của thuyền trưởng nhằm tận dụng dung tích và trọng tải của tàu , bảo đảm đúng quy định về xếp dỡ , vận chuyển hàng hoá trên tàu ; đặc biệt , chú `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 8 `[DIEU]`)


---

### Mẫu #07_2012_TT-BGTVT_27433#body_standalone_31 (Loại: `body_standalone`)
> **[Điều 8]`<DIEU>`** . **[12 . Tổ chức giao nhận **[hàng hóa]`<TAI_SAN_VAT_CHAT>`** , bưu kiện , bưu phẩm và chuẩn bị các giấy tờ về **[hàng hóa]`<TAI_SAN_VAT_CHAT>`** trình thuyền trưởng ; hàng ngày phải báo cáo thuyền trưởng biết về tình hình làm hàng và số lượng hàng hoá xếp dỡ được ; trước khi xếp **[hàng hóa]`<TAI_SAN_VAT_CHAT>`** , có nhiệm vụ lập sơ đồ xếp dỡ hàng hoá theo yêu cầu của thuyền trưởng nhằm tận dụng dung tích và trọng tải của tàu , bảo đảm đúng quy định về xếp dỡ , vận chuyển hàng hoá trên tàu ; đặc biệt , chú]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 8** → `DIEU` (span: `[0:2]`)
- `[e1]` **12 . Tổ chức giao nhận hàng hóa , bưu kiện , bưu phẩm và chuẩn bị các giấy tờ về hàng hóa trình thuyền trưởng ; hàng ngày phải báo cáo thuyền trưởng biết về tình hình làm hàng và số lượng hàng hoá xếp dỡ được ; trước khi xếp hàng hóa , có nhiệm vụ lập sơ đồ xếp dỡ hàng hoá theo yêu cầu của thuyền trưởng nhằm tận dụng dung tích và trọng tải của tàu , bảo đảm đúng quy định về xếp dỡ , vận chuyển hàng hoá trên tàu ; đặc biệt , chú** → `KHOAN` (span: `[3:73]`)
- `[e2]` **hàng hóa** → `TAI_SAN_VAT_CHAT` (span: `[7:8]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **hàng hóa** → `TAI_SAN_VAT_CHAT` (span: `[17:18]`) *(lồng trong `e1` (`KHOAN`))*
- `[e4]` **hàng hóa** → `TAI_SAN_VAT_CHAT` (span: `[39:40]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 12 . Tổ chức giao nhận hàng hóa , bưu kiện , bưu phẩm và chuẩn bị các giấy tờ về hàng hóa trình thuyền trưởng ; hàng ngày phải báo cáo thuyền trưởng biết về tình hình làm hàng và số lượng hàng hoá xếp dỡ được ; trước khi xếp hàng hóa , có nhiệm vụ lập sơ đồ xếp dỡ hàng hoá theo yêu cầu của thuyền trưởng nhằm tận dụng dung tích và trọng tải của tàu , bảo đảm đúng quy định về xếp dỡ , vận chuyển hàng hoá trên tàu ; đặc biệt , chú `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 8 `[DIEU]`)


---

### Mẫu #07_2012_TT-BGTVT_27433#body_context_32 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[07/2012/TT-BGTVT]`<SO_HIEU>`** của **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Giao thông Vận tải]`<LINH_VUC>`** . **[Điều 9]`<DIEU>`** . **[12 . Trong thời gian điều động tàu trong cảng , luồng hẹp hoặc hành trình trên biển , máy trưởng muốn thay đổi chế độ hoạt động của máy , các thiết bị kỹ thuật khác hay điều chỉnh nhiên liệu , nước ngọt , nước dằn thì phải được sự đồng ý của thuyền trưởng ;]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **07/2012/TT-BGTVT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[4:7]`)
- `[e3]` **Giao thông Vận tải** → `LINH_VUC` (span: `[9:11]`)
- `[e4]` **Điều 9** → `DIEU` (span: `[12:14]`)
- `[e5]` **12 . Trong thời gian điều động tàu trong cảng , luồng hẹp hoặc hành trình trên biển , máy trưởng muốn thay đổi chế độ hoạt động của máy , các thiết bị kỹ thuật khác hay điều chỉnh nhiên liệu , nước ngọt , nước dằn thì phải được sự đồng ý của thuyền trưởng ;** → `KHOAN` (span: `[15:60]`)

**Quan hệ:**
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Giao thông Vận tải `[LINH_VUC]`)
- (`e4` Điều 9 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`)
- (`e5` 12 . Trong thời gian điều động tàu trong cảng , luồng hẹp hoặc hành trình trên biển , máy trưởng muốn thay đổi chế độ hoạt động của máy , các thiết bị kỹ thuật khác hay điều chỉnh nhiên liệu , nước ngọt , nước dằn thì phải được sự đồng ý của thuyền trưởng ; `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 9 `[DIEU]`)
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Giao thông Vận tải `[LINH_VUC]`)
- (`e5` 12 . Trong thời gian điều động tàu trong cảng , luồng hẹp hoặc hành trình trên biển , máy trưởng muốn thay đổi chế độ hoạt động của máy , các thiết bị kỹ thuật khác hay điều chỉnh nhiên liệu , nước ngọt , nước dằn thì phải được sự đồng ý của thuyền trưởng ; `[KHOAN]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Giao thông Vận tải `[LINH_VUC]`)


---

### Mẫu #07_2012_TT-BGTVT_27433#body_context_33 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[07/2012/TT-BGTVT]`<SO_HIEU>`** của **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Giao thông Vận tải]`<LINH_VUC>`** . **[Điều 12 . Nhiệm vụ của phó ba . Phó ba chịu sự quản lý và điều hành trực tiếp của thuyền trưởng khi tàu hành trình và của đại phó khi tàu không hành trình . Phó ba có nhiệm vụ sau đây :]`<DIEU>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **07/2012/TT-BGTVT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[4:7]`)
- `[e3]` **Giao thông Vận tải** → `LINH_VUC` (span: `[9:11]`)
- `[e4]` **Điều 12 . Nhiệm vụ của phó ba . Phó ba chịu sự quản lý và điều hành trực tiếp của thuyền trưởng khi tàu hành trình và của đại phó khi tàu không hành trình . Phó ba có nhiệm vụ sau đây :** → `DIEU` (span: `[12:47]`)

**Quan hệ:**
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Giao thông Vận tải `[LINH_VUC]`)
- (`e4` Điều 12 . Nhiệm vụ của phó ba . Phó ba chịu sự quản lý và điều hành trực tiếp của thuyền trưởng khi tàu hành trình và của đại phó khi tàu không hành trình . Phó ba có nhiệm vụ sau đây : `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`)
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Giao thông Vận tải `[LINH_VUC]`)
- (`e4` Điều 12 . Nhiệm vụ của phó ba . Phó ba chịu sự quản lý và điều hành trực tiếp của thuyền trưởng khi tàu hành trình và của đại phó khi tàu không hành trình . Phó ba có nhiệm vụ sau đây : `[DIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Giao thông Vận tải `[LINH_VUC]`)


---

### Mẫu #07_2012_TT-BGTVT_27433#body_context_34 (Loại: `body_context`)
> **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[07/2012/TT-BGTVT]`<SO_HIEU>`** . **[Điều 15]`<DIEU>`** . **[6 . Trước khi tàu nhận hành khách , phải kiểm tra việc đóng các cửa kín nước , chằng buộc và sắp xếp cố định các vật dụng thuộc bộ phận mình quản lý ;]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[4:5]`)
- `[e1]` **07/2012/TT-BGTVT** → `SO_HIEU` (span: `[6:7]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[0:3]`)
- `[e3]` **Điều 15** → `DIEU` (span: `[8:10]`)
- `[e4]` **6 . Trước khi tàu nhận hành khách , phải kiểm tra việc đóng các cửa kín nước , chằng buộc và sắp xếp cố định các vật dụng thuộc bộ phận mình quản lý ;** → `KHOAN` (span: `[11:40]`)

**Quan hệ:**
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 15 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`)
- (`e4` 6 . Trước khi tàu nhận hành khách , phải kiểm tra việc đóng các cửa kín nước , chằng buộc và sắp xếp cố định các vật dụng thuộc bộ phận mình quản lý ; `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 15 `[DIEU]`)


---

### Mẫu #07_2012_TT-BGTVT_27433#body_context_35 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[07/2012/TT-BGTVT]`<SO_HIEU>`** ban hành **[ngày 21 tháng 03 năm 2012]`<NGAY_BAN_HANH>`** bởi **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** . **[Chương II]`<CHUONG>`** . **[Điều 18 . Nhiệm vụ của sỹ quan an ninh **[tàu biển]`<TAI_SAN_VAT_CHAT>`** . Sỹ quan an ninh **[tàu biển]`<TAI_SAN_VAT_CHAT>`** là sỹ quan quản lý được chủ tàu bổ nhiệm , chịu sự quản lý và điều hành trực tiếp của thuyền trưởng . Sỹ quan an ninh **[tàu biển]`<TAI_SAN_VAT_CHAT>`** có nhiệm vụ sau đây :]`<DIEU>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **07/2012/TT-BGTVT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[11:14]`)
- `[e3]` **ngày 21 tháng 03 năm 2012** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Chương II** → `CHUONG` (span: `[15:17]`)
- `[e5]` **Điều 18 . Nhiệm vụ của sỹ quan an ninh tàu biển . Sỹ quan an ninh tàu biển là sỹ quan quản lý được chủ tàu bổ nhiệm , chịu sự quản lý và điều hành trực tiếp của thuyền trưởng . Sỹ quan an ninh tàu biển có nhiệm vụ sau đây :** → `DIEU` (span: `[18:59]`)
- `[e6]` **tàu biển** → `TAI_SAN_VAT_CHAT` (span: `[26:27]`) *(lồng trong `e5` (`DIEU`))*
- `[e7]` **tàu biển** → `TAI_SAN_VAT_CHAT` (span: `[31:32]`) *(lồng trong `e5` (`DIEU`))*
- `[e8]` **tàu biển** → `TAI_SAN_VAT_CHAT` (span: `[53:54]`) *(lồng trong `e5` (`DIEU`))*

**Quan hệ:**
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 21 tháng 03 năm 2012 `[NGAY_BAN_HANH]`)
- (`e4` Chương II `[CHUONG]`) ==[ **THUOC_VE** ]==> (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`)
- (`e5` Điều 18 . Nhiệm vụ của sỹ quan an ninh tàu biển . Sỹ quan an ninh tàu biển là sỹ quan quản lý được chủ tàu bổ nhiệm , chịu sự quản lý và điều hành trực tiếp của thuyền trưởng . Sỹ quan an ninh tàu biển có nhiệm vụ sau đây : `[DIEU]`) ==[ **THUOC_VE** ]==> (`e4` Chương II `[CHUONG]`)


---

### Mẫu #07_2012_TT-BGTVT_27433#body_context_36 (Loại: `body_context`)
> **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[07/2012/TT-BGTVT]`<SO_HIEU>`** . **[Điều 19]`<DIEU>`** . **[2 . Trực tiếp quản lý , khai thác công suất máy và bảo đảm tình trạng kỹ thuật , chế độ hoạt động của máy móc , thiết bị làm lạnh , hệ thống làm mát bằng không khí và hệ thống điều hoà nhiệt độ trên tàu theo đúng quy trình , quy phạm hiện hành ;]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[4:5]`)
- `[e1]` **07/2012/TT-BGTVT** → `SO_HIEU` (span: `[6:7]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[0:3]`)
- `[e3]` **Điều 19** → `DIEU` (span: `[8:10]`)
- `[e4]` **2 . Trực tiếp quản lý , khai thác công suất máy và bảo đảm tình trạng kỹ thuật , chế độ hoạt động của máy móc , thiết bị làm lạnh , hệ thống làm mát bằng không khí và hệ thống điều hoà nhiệt độ trên tàu theo đúng quy trình , quy phạm hiện hành ;** → `KHOAN` (span: `[11:50]`)

**Quan hệ:**
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 19 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`)
- (`e4` 2 . Trực tiếp quản lý , khai thác công suất máy và bảo đảm tình trạng kỹ thuật , chế độ hoạt động của máy móc , thiết bị làm lạnh , hệ thống làm mát bằng không khí và hệ thống điều hoà nhiệt độ trên tàu theo đúng quy trình , quy phạm hiện hành ; `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 19 `[DIEU]`)


---

### Mẫu #07_2012_TT-BGTVT_27433#body_context_37 (Loại: `body_context`)
> **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[07/2012/TT-BGTVT]`<SO_HIEU>`** . **[Điều 20]`<DIEU>`** . **[2 . Kiểm tra và theo dõi việc bảo quản vỏ tàu , các loại dây , **[trang thiết bị]`<TAI_SAN_VAT_CHAT>`** của các hệ thống neo , cần cẩu , **[phương tiện]`<TAI_SAN_VAT_CHAT>`** cứu sinh , cứu hoả , cứu thủng tàu , các kho để vật tư dụng cụ và vật tư kỹ thuật , các **[tài sản]`<TAI_SAN_VAT_CHAT>`** khác của tàu do bộ phận boong quản lý ;]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[4:5]`)
- `[e1]` **07/2012/TT-BGTVT** → `SO_HIEU` (span: `[6:7]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[0:3]`)
- `[e3]` **Điều 20** → `DIEU` (span: `[8:10]`)
- `[e4]` **2 . Kiểm tra và theo dõi việc bảo quản vỏ tàu , các loại dây , trang thiết bị của các hệ thống neo , cần cẩu , phương tiện cứu sinh , cứu hoả , cứu thủng tàu , các kho để vật tư dụng cụ và vật tư kỹ thuật , các tài sản khác của tàu do bộ phận boong quản lý ;** → `KHOAN` (span: `[11:62]`)
- `[e5]` **trang thiết bị** → `TAI_SAN_VAT_CHAT` (span: `[25:27]`) *(lồng trong `e4` (`KHOAN`))*
- `[e6]` **phương tiện** → `TAI_SAN_VAT_CHAT` (span: `[34:35]`) *(lồng trong `e4` (`KHOAN`))*
- `[e7]` **tài sản** → `TAI_SAN_VAT_CHAT` (span: `[53:54]`) *(lồng trong `e4` (`KHOAN`))*

**Quan hệ:**
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 20 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`)
- (`e4` 2 . Kiểm tra và theo dõi việc bảo quản vỏ tàu , các loại dây , trang thiết bị của các hệ thống neo , cần cẩu , phương tiện cứu sinh , cứu hoả , cứu thủng tàu , các kho để vật tư dụng cụ và vật tư kỹ thuật , các tài sản khác của tàu do bộ phận boong quản lý ; `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 20 `[DIEU]`)


---

### Mẫu #07_2012_TT-BGTVT_27433#body_standalone_38 (Loại: `body_standalone`)
> **[Điều 20]`<DIEU>`** . **[2 . Kiểm tra và theo dõi việc bảo quản vỏ tàu , các loại dây , **[trang thiết bị]`<TAI_SAN_VAT_CHAT>`** của các hệ thống neo , cần cẩu , **[phương tiện]`<TAI_SAN_VAT_CHAT>`** cứu sinh , cứu hoả , cứu thủng tàu , các kho để vật tư dụng cụ và vật tư kỹ thuật , các **[tài sản]`<TAI_SAN_VAT_CHAT>`** khác của tàu do bộ phận boong quản lý ;]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 20** → `DIEU` (span: `[0:2]`)
- `[e1]` **2 . Kiểm tra và theo dõi việc bảo quản vỏ tàu , các loại dây , trang thiết bị của các hệ thống neo , cần cẩu , phương tiện cứu sinh , cứu hoả , cứu thủng tàu , các kho để vật tư dụng cụ và vật tư kỹ thuật , các tài sản khác của tàu do bộ phận boong quản lý ;** → `KHOAN` (span: `[3:54]`)
- `[e2]` **trang thiết bị** → `TAI_SAN_VAT_CHAT` (span: `[17:19]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **phương tiện** → `TAI_SAN_VAT_CHAT` (span: `[26:27]`) *(lồng trong `e1` (`KHOAN`))*
- `[e4]` **tài sản** → `TAI_SAN_VAT_CHAT` (span: `[45:46]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 2 . Kiểm tra và theo dõi việc bảo quản vỏ tàu , các loại dây , trang thiết bị của các hệ thống neo , cần cẩu , phương tiện cứu sinh , cứu hoả , cứu thủng tàu , các kho để vật tư dụng cụ và vật tư kỹ thuật , các tài sản khác của tàu do bộ phận boong quản lý ; `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 20 `[DIEU]`)


---

### Mẫu #07_2012_TT-BGTVT_27433#body_context_39 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[07/2012/TT-BGTVT]`<SO_HIEU>`** của **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Giao thông Vận tải]`<LINH_VUC>`** . **[Điều 23]`<DIEU>`** . **[3 . Thực hiện chế độ vệ sinh công nghiệp đối với máy móc thiết bị bộ phận máy ;]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **07/2012/TT-BGTVT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[4:7]`)
- `[e3]` **Giao thông Vận tải** → `LINH_VUC` (span: `[9:11]`)
- `[e4]` **Điều 23** → `DIEU` (span: `[12:14]`)
- `[e5]` **3 . Thực hiện chế độ vệ sinh công nghiệp đối với máy móc thiết bị bộ phận máy ;** → `KHOAN` (span: `[15:27]`)

**Quan hệ:**
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Giao thông Vận tải `[LINH_VUC]`)
- (`e4` Điều 23 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`)
- (`e5` 3 . Thực hiện chế độ vệ sinh công nghiệp đối với máy móc thiết bị bộ phận máy ; `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 23 `[DIEU]`)
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Giao thông Vận tải `[LINH_VUC]`)
- (`e5` 3 . Thực hiện chế độ vệ sinh công nghiệp đối với máy móc thiết bị bộ phận máy ; `[KHOAN]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Giao thông Vận tải `[LINH_VUC]`)


---

### Mẫu #07_2012_TT-BGTVT_27433#body_standalone_40 (Loại: `body_standalone`)
> **[Điều 23]`<DIEU>`** . **[3 . Thực hiện chế độ vệ sinh công nghiệp đối với máy móc thiết bị bộ phận máy ;]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 23** → `DIEU` (span: `[0:2]`)
- `[e1]` **3 . Thực hiện chế độ vệ sinh công nghiệp đối với máy móc thiết bị bộ phận máy ;** → `KHOAN` (span: `[3:15]`)

**Quan hệ:**
- (`e1` 3 . Thực hiện chế độ vệ sinh công nghiệp đối với máy móc thiết bị bộ phận máy ; `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 23 `[DIEU]`)


---

### Mẫu #07_2012_TT-BGTVT_27433#body_context_41 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[07/2012/TT-BGTVT]`<SO_HIEU>`** ban hành **[ngày 21 tháng 03 năm 2012]`<NGAY_BAN_HANH>`** bởi **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** . **[Điều 28]`<DIEU>`** . **[8 . Trước mỗi chuyến đi phải kiểm tra **[giấy chứng nhận sức khoẻ của thuyền viên]`<GIAY_TO_HO_SO>`** , sổ tiêm chủng của thuyền viên , **[giấy chứng nhận miễn xử lý vệ sinh tàu thủy]`<GIAY_TO_HO_SO>`** , **[giấy chứng nhận tiêm phòng dịch]`<GIAY_TO_HO_SO>`** cho gia súc ( nếu có ) ;]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **07/2012/TT-BGTVT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[11:14]`)
- `[e3]` **ngày 21 tháng 03 năm 2012** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 28** → `DIEU` (span: `[15:17]`)
- `[e5]` **8 . Trước mỗi chuyến đi phải kiểm tra giấy chứng nhận sức khoẻ của thuyền viên , sổ tiêm chủng của thuyền viên , giấy chứng nhận miễn xử lý vệ sinh tàu thủy , giấy chứng nhận tiêm phòng dịch cho gia súc ( nếu có ) ;** → `KHOAN` (span: `[18:55]`)
- `[e6]` **giấy chứng nhận sức khoẻ của thuyền viên** → `GIAY_TO_HO_SO` (span: `[26:31]`) *(lồng trong `e5` (`KHOAN`))*
- `[e7]` **giấy chứng nhận miễn xử lý vệ sinh tàu thủy** → `GIAY_TO_HO_SO` (span: `[37:43]`) *(lồng trong `e5` (`KHOAN`))*
- `[e8]` **giấy chứng nhận tiêm phòng dịch** → `GIAY_TO_HO_SO` (span: `[44:48]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 21 tháng 03 năm 2012 `[NGAY_BAN_HANH]`)
- (`e4` Điều 28 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`)
- (`e5` 8 . Trước mỗi chuyến đi phải kiểm tra giấy chứng nhận sức khoẻ của thuyền viên , sổ tiêm chủng của thuyền viên , giấy chứng nhận miễn xử lý vệ sinh tàu thủy , giấy chứng nhận tiêm phòng dịch cho gia súc ( nếu có ) ; `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 28 `[DIEU]`)


---

### Mẫu #07_2012_TT-BGTVT_27433#body_standalone_42 (Loại: `body_standalone`)
> **[Điều 28]`<DIEU>`** . **[8 . Trước mỗi chuyến đi phải kiểm tra **[giấy chứng nhận sức khoẻ của thuyền viên]`<GIAY_TO_HO_SO>`** , sổ tiêm chủng của thuyền viên , **[giấy chứng nhận miễn xử lý vệ sinh tàu thủy]`<GIAY_TO_HO_SO>`** , **[giấy chứng nhận tiêm phòng dịch]`<GIAY_TO_HO_SO>`** cho gia súc ( nếu có ) ;]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 28** → `DIEU` (span: `[0:2]`)
- `[e1]` **8 . Trước mỗi chuyến đi phải kiểm tra giấy chứng nhận sức khoẻ của thuyền viên , sổ tiêm chủng của thuyền viên , giấy chứng nhận miễn xử lý vệ sinh tàu thủy , giấy chứng nhận tiêm phòng dịch cho gia súc ( nếu có ) ;** → `KHOAN` (span: `[3:40]`)
- `[e2]` **giấy chứng nhận sức khoẻ của thuyền viên** → `GIAY_TO_HO_SO` (span: `[11:16]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **giấy chứng nhận miễn xử lý vệ sinh tàu thủy** → `GIAY_TO_HO_SO` (span: `[22:28]`) *(lồng trong `e1` (`KHOAN`))*
- `[e4]` **giấy chứng nhận tiêm phòng dịch** → `GIAY_TO_HO_SO` (span: `[29:33]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 8 . Trước mỗi chuyến đi phải kiểm tra giấy chứng nhận sức khoẻ của thuyền viên , sổ tiêm chủng của thuyền viên , giấy chứng nhận miễn xử lý vệ sinh tàu thủy , giấy chứng nhận tiêm phòng dịch cho gia súc ( nếu có ) ; `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 28 `[DIEU]`)


---

### Mẫu #07_2012_TT-BGTVT_27433#body_context_43 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[07/2012/TT-BGTVT]`<SO_HIEU>`** của **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Giao thông Vận tải]`<LINH_VUC>`** . **[Điều 30]`<DIEU>`** . **[1 . Tổ chức thực hiện các công việc của nhà bếp và trực tiếp chuẩn bị bữa ăn hàng ngày cho thuyền viên và hành khách ;]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **07/2012/TT-BGTVT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[4:7]`)
- `[e3]` **Giao thông Vận tải** → `LINH_VUC` (span: `[9:11]`)
- `[e4]` **Điều 30** → `DIEU` (span: `[12:14]`)
- `[e5]` **1 . Tổ chức thực hiện các công việc của nhà bếp và trực tiếp chuẩn bị bữa ăn hàng ngày cho thuyền viên và hành khách ;** → `KHOAN` (span: `[15:34]`)

**Quan hệ:**
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Giao thông Vận tải `[LINH_VUC]`)
- (`e4` Điều 30 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`)
- (`e5` 1 . Tổ chức thực hiện các công việc của nhà bếp và trực tiếp chuẩn bị bữa ăn hàng ngày cho thuyền viên và hành khách ; `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 30 `[DIEU]`)
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Giao thông Vận tải `[LINH_VUC]`)
- (`e5` 1 . Tổ chức thực hiện các công việc của nhà bếp và trực tiếp chuẩn bị bữa ăn hàng ngày cho thuyền viên và hành khách ; `[KHOAN]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Giao thông Vận tải `[LINH_VUC]`)


---

### Mẫu #07_2012_TT-BGTVT_27433#body_context_44 (Loại: `body_context`)
> **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[07/2012/TT-BGTVT]`<SO_HIEU>`** . **[Điều 36]`<DIEU>`** . **[1 . Quản lý các **[tài sản]`<TAI_SAN_VAT_CHAT>`** , đồ dùng , các kho và phòng công cộng phục vụ hành khách ;]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[4:5]`)
- `[e1]` **07/2012/TT-BGTVT** → `SO_HIEU` (span: `[6:7]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[0:3]`)
- `[e3]` **Điều 36** → `DIEU` (span: `[8:10]`)
- `[e4]` **1 . Quản lý các tài sản , đồ dùng , các kho và phòng công cộng phục vụ hành khách ;** → `KHOAN` (span: `[11:27]`)
- `[e5]` **tài sản** → `TAI_SAN_VAT_CHAT` (span: `[15:16]`) *(lồng trong `e4` (`KHOAN`))*

**Quan hệ:**
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 36 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`)
- (`e4` 1 . Quản lý các tài sản , đồ dùng , các kho và phòng công cộng phục vụ hành khách ; `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 36 `[DIEU]`)


---

### Mẫu #07_2012_TT-BGTVT_27433#body_context_45 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[07/2012/TT-BGTVT]`<SO_HIEU>`** của **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Giao thông Vận tải]`<LINH_VUC>`** . **[Điều 42]`<DIEU>`** . **[3 . Khám xét tại chỗ và lập biên bản những vụ phạm pháp quả tang trên tàu . Lập hồ sơ những vụ vi phạm pháp luật do hành khách phát giác ;]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **07/2012/TT-BGTVT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[4:7]`)
- `[e3]` **Giao thông Vận tải** → `LINH_VUC` (span: `[9:11]`)
- `[e4]` **Điều 42** → `DIEU` (span: `[12:14]`)
- `[e5]` **3 . Khám xét tại chỗ và lập biên bản những vụ phạm pháp quả tang trên tàu . Lập hồ sơ những vụ vi phạm pháp luật do hành khách phát giác ;** → `KHOAN` (span: `[15:38]`)

**Quan hệ:**
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Giao thông Vận tải `[LINH_VUC]`)
- (`e4` Điều 42 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`)
- (`e5` 3 . Khám xét tại chỗ và lập biên bản những vụ phạm pháp quả tang trên tàu . Lập hồ sơ những vụ vi phạm pháp luật do hành khách phát giác ; `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 42 `[DIEU]`)
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Giao thông Vận tải `[LINH_VUC]`)
- (`e5` 3 . Khám xét tại chỗ và lập biên bản những vụ phạm pháp quả tang trên tàu . Lập hồ sơ những vụ vi phạm pháp luật do hành khách phát giác ; `[KHOAN]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Giao thông Vận tải `[LINH_VUC]`)


---

### Mẫu #07_2012_TT-BGTVT_27433#body_context_46 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[07/2012/TT-BGTVT]`<SO_HIEU>`** của **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Giao thông Vận tải]`<LINH_VUC>`** . **[Điều 48]`<DIEU>`** . **[Khoản 3]`<KHOAN>`** . **[a ) Nắm vững tình hình hoạt động của tàu , các điều kiện có liên quan đến khu vực hành trình để chủ động tiếp nhận ca trực ; tiến hành thủ tục nhận ca theo đúng quy định ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **07/2012/TT-BGTVT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[4:7]`)
- `[e3]` **Giao thông Vận tải** → `LINH_VUC` (span: `[9:11]`)
- `[e4]` **Điều 48** → `DIEU` (span: `[12:14]`)
- `[e5]` **Khoản 3** → `KHOAN` (span: `[15:17]`)
- `[e6]` **a ) Nắm vững tình hình hoạt động của tàu , các điều kiện có liên quan đến khu vực hành trình để chủ động tiếp nhận ca trực ; tiến hành thủ tục nhận ca theo đúng quy định ;** → `DIEM` (span: `[18:48]`)

**Quan hệ:**
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Giao thông Vận tải `[LINH_VUC]`)
- (`e4` Điều 48 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`)
- (`e5` Khoản 3 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 48 `[DIEU]`)
- (`e6` a ) Nắm vững tình hình hoạt động của tàu , các điều kiện có liên quan đến khu vực hành trình để chủ động tiếp nhận ca trực ; tiến hành thủ tục nhận ca theo đúng quy định ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e5` Khoản 3 `[KHOAN]`)
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Giao thông Vận tải `[LINH_VUC]`)
- (`e6` a ) Nắm vững tình hình hoạt động của tàu , các điều kiện có liên quan đến khu vực hành trình để chủ động tiếp nhận ca trực ; tiến hành thủ tục nhận ca theo đúng quy định ; `[DIEM]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Giao thông Vận tải `[LINH_VUC]`)


---

### Mẫu #07_2012_TT-BGTVT_27433#body_context_47 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[07/2012/TT-BGTVT]`<SO_HIEU>`** của **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Giao thông Vận tải]`<LINH_VUC>`** . **[Chương II]`<CHUONG>`** . **[Điều 50 . Nhiệm vụ của thủy thủ trực ca]`<DIEU>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **07/2012/TT-BGTVT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[4:7]`)
- `[e3]` **Giao thông Vận tải** → `LINH_VUC` (span: `[9:11]`)
- `[e4]` **Chương II** → `CHUONG` (span: `[12:14]`)
- `[e5]` **Điều 50 . Nhiệm vụ của thủy thủ trực ca** → `DIEU` (span: `[15:23]`)

**Quan hệ:**
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Giao thông Vận tải `[LINH_VUC]`)
- (`e4` Chương II `[CHUONG]`) ==[ **THUOC_VE** ]==> (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`)
- (`e5` Điều 50 . Nhiệm vụ của thủy thủ trực ca `[DIEU]`) ==[ **THUOC_VE** ]==> (`e4` Chương II `[CHUONG]`)
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Giao thông Vận tải `[LINH_VUC]`)
- (`e5` Điều 50 . Nhiệm vụ của thủy thủ trực ca `[DIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Giao thông Vận tải `[LINH_VUC]`)


---

### Mẫu #07_2012_TT-BGTVT_27433#body_context_48 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[07/2012/TT-BGTVT]`<SO_HIEU>`** của **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Giao thông Vận tải]`<LINH_VUC>`** . **[Điều 53]`<DIEU>`** . **[Khoản 2]`<KHOAN>`** . **[p ) Ghi nhật ký thông tin vô tuyến ; kiểm tra và đánh dấu vào danh mục kiểm tra .]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **07/2012/TT-BGTVT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[4:7]`)
- `[e3]` **Giao thông Vận tải** → `LINH_VUC` (span: `[9:11]`)
- `[e4]` **Điều 53** → `DIEU` (span: `[12:14]`)
- `[e5]` **Khoản 2** → `KHOAN` (span: `[15:17]`)
- `[e6]` **p ) Ghi nhật ký thông tin vô tuyến ; kiểm tra và đánh dấu vào danh mục kiểm tra .** → `DIEM` (span: `[18:32]`)

**Quan hệ:**
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Giao thông Vận tải `[LINH_VUC]`)
- (`e4` Điều 53 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`)
- (`e5` Khoản 2 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 53 `[DIEU]`)
- (`e6` p ) Ghi nhật ký thông tin vô tuyến ; kiểm tra và đánh dấu vào danh mục kiểm tra . `[DIEM]`) ==[ **THUOC_VE** ]==> (`e5` Khoản 2 `[KHOAN]`)
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Giao thông Vận tải `[LINH_VUC]`)
- (`e6` p ) Ghi nhật ký thông tin vô tuyến ; kiểm tra và đánh dấu vào danh mục kiểm tra . `[DIEM]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Giao thông Vận tải `[LINH_VUC]`)


---

### Mẫu #07_2012_TT-BGTVT_27433#body_context_49 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[07/2012/TT-BGTVT]`<SO_HIEU>`** ban hành **[ngày 21 tháng 03 năm 2012]`<NGAY_BAN_HANH>`** bởi **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** . **[Điều 60]`<DIEU>`** . **[2 . Nghiêm cấm chứa chất nổ , vũ khí , chất dễ cháy , những hàng hoá nguy hiểm , hàng cấm khác trong buồng ở , phòng làm việc và phòng công cộng .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **07/2012/TT-BGTVT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[11:14]`)
- `[e3]` **ngày 21 tháng 03 năm 2012** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 60** → `DIEU` (span: `[15:17]`)
- `[e5]` **2 . Nghiêm cấm chứa chất nổ , vũ khí , chất dễ cháy , những hàng hoá nguy hiểm , hàng cấm khác trong buồng ở , phòng làm việc và phòng công cộng .** → `KHOAN` (span: `[18:46]`)

**Quan hệ:**
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 21 tháng 03 năm 2012 `[NGAY_BAN_HANH]`)
- (`e4` Điều 60 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`)
- (`e5` 2 . Nghiêm cấm chứa chất nổ , vũ khí , chất dễ cháy , những hàng hoá nguy hiểm , hàng cấm khác trong buồng ở , phòng làm việc và phòng công cộng . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 60 `[DIEU]`)


---

### Mẫu #07_2012_TT-BGTVT_27433#body_standalone_50 (Loại: `body_standalone`)
> **[Điều 60]`<DIEU>`** . **[2 . Nghiêm cấm chứa chất nổ , vũ khí , chất dễ cháy , những hàng hoá nguy hiểm , hàng cấm khác trong buồng ở , phòng làm việc và phòng công cộng .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 60** → `DIEU` (span: `[0:2]`)
- `[e1]` **2 . Nghiêm cấm chứa chất nổ , vũ khí , chất dễ cháy , những hàng hoá nguy hiểm , hàng cấm khác trong buồng ở , phòng làm việc và phòng công cộng .** → `KHOAN` (span: `[3:31]`)

**Quan hệ:**
- (`e1` 2 . Nghiêm cấm chứa chất nổ , vũ khí , chất dễ cháy , những hàng hoá nguy hiểm , hàng cấm khác trong buồng ở , phòng làm việc và phòng công cộng . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 60 `[DIEU]`)


---

### Mẫu #07_2012_TT-BGTVT_27433#body_context_51 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[07/2012/TT-BGTVT]`<SO_HIEU>`** ban hành **[ngày 21 tháng 03 năm 2012]`<NGAY_BAN_HANH>`** bởi **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** . **[Điều 63]`<DIEU>`** . **[1 . Thuyền viên Việt Nam làm việc trên **[tàu biển]`<TAI_SAN_VAT_CHAT>`** Việt Nam , **[tàu biển]`<TAI_SAN_VAT_CHAT>`** nước ngoài và thuyền viên nước ngoài làm việc trên **[tàu biển]`<TAI_SAN_VAT_CHAT>`** Việt Nam phải đăng ký với cơ quan đăng ký thuyền viên và được cấp **[Sổ thuyền viên]`<GIAY_TO_HO_SO>`** .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **07/2012/TT-BGTVT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[11:14]`)
- `[e3]` **ngày 21 tháng 03 năm 2012** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 63** → `DIEU` (span: `[15:17]`)
- `[e5]` **1 . Thuyền viên Việt Nam làm việc trên tàu biển Việt Nam , tàu biển nước ngoài và thuyền viên nước ngoài làm việc trên tàu biển Việt Nam phải đăng ký với cơ quan đăng ký thuyền viên và được cấp Sổ thuyền viên .** → `KHOAN` (span: `[18:48]`)
- `[e6]` **Sổ thuyền viên** → `GIAY_TO_HO_SO` (span: `[45:47]`) *(lồng trong `e5` (`KHOAN`))*
- `[e7]` **tàu biển** → `TAI_SAN_VAT_CHAT` (span: `[24:25]`) *(lồng trong `e5` (`KHOAN`))*
- `[e8]` **tàu biển** → `TAI_SAN_VAT_CHAT` (span: `[27:28]`) *(lồng trong `e5` (`KHOAN`))*
- `[e9]` **tàu biển** → `TAI_SAN_VAT_CHAT` (span: `[34:35]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 21 tháng 03 năm 2012 `[NGAY_BAN_HANH]`)
- (`e4` Điều 63 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`)
- (`e5` 1 . Thuyền viên Việt Nam làm việc trên tàu biển Việt Nam , tàu biển nước ngoài và thuyền viên nước ngoài làm việc trên tàu biển Việt Nam phải đăng ký với cơ quan đăng ký thuyền viên và được cấp Sổ thuyền viên . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 63 `[DIEU]`)


---

### Mẫu #07_2012_TT-BGTVT_27433#body_standalone_52 (Loại: `body_standalone`)
> **[Điều 63]`<DIEU>`** . **[1 . Thuyền viên Việt Nam làm việc trên **[tàu biển]`<TAI_SAN_VAT_CHAT>`** Việt Nam , **[tàu biển]`<TAI_SAN_VAT_CHAT>`** nước ngoài và thuyền viên nước ngoài làm việc trên **[tàu biển]`<TAI_SAN_VAT_CHAT>`** Việt Nam phải đăng ký với cơ quan đăng ký thuyền viên và được cấp **[Sổ thuyền viên]`<GIAY_TO_HO_SO>`** .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 63** → `DIEU` (span: `[0:2]`)
- `[e1]` **1 . Thuyền viên Việt Nam làm việc trên tàu biển Việt Nam , tàu biển nước ngoài và thuyền viên nước ngoài làm việc trên tàu biển Việt Nam phải đăng ký với cơ quan đăng ký thuyền viên và được cấp Sổ thuyền viên .** → `KHOAN` (span: `[3:33]`)
- `[e2]` **Sổ thuyền viên** → `GIAY_TO_HO_SO` (span: `[30:32]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **tàu biển** → `TAI_SAN_VAT_CHAT` (span: `[9:10]`) *(lồng trong `e1` (`KHOAN`))*
- `[e4]` **tàu biển** → `TAI_SAN_VAT_CHAT` (span: `[12:13]`) *(lồng trong `e1` (`KHOAN`))*
- `[e5]` **tàu biển** → `TAI_SAN_VAT_CHAT` (span: `[19:20]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 1 . Thuyền viên Việt Nam làm việc trên tàu biển Việt Nam , tàu biển nước ngoài và thuyền viên nước ngoài làm việc trên tàu biển Việt Nam phải đăng ký với cơ quan đăng ký thuyền viên và được cấp Sổ thuyền viên . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 63 `[DIEU]`)


---

### Mẫu #07_2012_TT-BGTVT_27433#body_context_53 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[07/2012/TT-BGTVT]`<SO_HIEU>`** ban hành **[ngày 21 tháng 03 năm 2012]`<NGAY_BAN_HANH>`** bởi **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** . **[Chương III]`<CHUONG>`** . **[Điều 64 . Trách nhiệm của người được cấp **[Sổ thuyền viên]`<GIAY_TO_HO_SO>`** . Mỗi thuyền viên chỉ được cấp một **[Sổ thuyền viên]`<GIAY_TO_HO_SO>`** . Thuyền viên có trách nhiệm giữ gìn và bảo quản **[Sổ thuyền viên]`<GIAY_TO_HO_SO>`** ; không được tẩy , xóa , sửa chữa những nội dung trong **[Sổ thuyền viên]`<GIAY_TO_HO_SO>`** , không được cho người khác sử dụng hoặc sử dụng trái với các quy định của pháp luật .]`<DIEU>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **07/2012/TT-BGTVT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[11:14]`)
- `[e3]` **ngày 21 tháng 03 năm 2012** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Chương III** → `CHUONG` (span: `[15:17]`)
- `[e5]` **Điều 64 . Trách nhiệm của người được cấp Sổ thuyền viên . Mỗi thuyền viên chỉ được cấp một Sổ thuyền viên . Thuyền viên có trách nhiệm giữ gìn và bảo quản Sổ thuyền viên ; không được tẩy , xóa , sửa chữa những nội dung trong Sổ thuyền viên , không được cho người khác sử dụng hoặc sử dụng trái với các quy định của pháp luật .** → `DIEU` (span: `[18:75]`)
- `[e6]` **Sổ thuyền viên** → `GIAY_TO_HO_SO` (span: `[26:28]`) *(lồng trong `e5` (`DIEU`))*
- `[e7]` **Sổ thuyền viên** → `GIAY_TO_HO_SO` (span: `[35:37]`) *(lồng trong `e5` (`DIEU`))*
- `[e8]` **Sổ thuyền viên** → `GIAY_TO_HO_SO` (span: `[44:46]`) *(lồng trong `e5` (`DIEU`))*
- `[e9]` **Sổ thuyền viên** → `GIAY_TO_HO_SO` (span: `[57:59]`) *(lồng trong `e5` (`DIEU`))*

**Quan hệ:**
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 21 tháng 03 năm 2012 `[NGAY_BAN_HANH]`)
- (`e4` Chương III `[CHUONG]`) ==[ **THUOC_VE** ]==> (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`)
- (`e5` Điều 64 . Trách nhiệm của người được cấp Sổ thuyền viên . Mỗi thuyền viên chỉ được cấp một Sổ thuyền viên . Thuyền viên có trách nhiệm giữ gìn và bảo quản Sổ thuyền viên ; không được tẩy , xóa , sửa chữa những nội dung trong Sổ thuyền viên , không được cho người khác sử dụng hoặc sử dụng trái với các quy định của pháp luật . `[DIEU]`) ==[ **THUOC_VE** ]==> (`e4` Chương III `[CHUONG]`)


---

### Mẫu #07_2012_TT-BGTVT_27433#body_context_54 (Loại: `body_context`)
> **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[07/2012/TT-BGTVT]`<SO_HIEU>`** . **[Điều 66]`<DIEU>`** . **[1 . Tổ chức , cá nhân nộp một ( 01 ) bộ hồ sơ trực tiếp hoặc gửi qua hệ thống bưu chính đến một trong các cơ quan đăng ký **[quy định tại]`<TU_KHOA_PHAP_LY>`** **[khoản 2 Điều 63 của Thông tư này]`<THAM_CHIEU_PHAP_LY>`** . Hồ sơ bao gồm :]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[4:5]`)
- `[e1]` **07/2012/TT-BGTVT** → `SO_HIEU` (span: `[6:7]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[0:3]`)
- `[e3]` **Điều 66** → `DIEU` (span: `[8:10]`)
- `[e4]` **1 . Tổ chức , cá nhân nộp một ( 01 ) bộ hồ sơ trực tiếp hoặc gửi qua hệ thống bưu chính đến một trong các cơ quan đăng ký quy định tại khoản 2 Điều 63 của Thông tư này . Hồ sơ bao gồm :** → `KHOAN` (span: `[11:48]`)
- `[e5]` **khoản 2 Điều 63 của Thông tư này** → `THAM_CHIEU_PHAP_LY` (span: `[37:44]`) *(lồng trong `e4` (`KHOAN`))*
- `[e6]` **quy định tại** → `TU_KHOA_PHAP_LY` (span: `[35:37]`) *(lồng trong `e4` (`KHOAN`))*

**Quan hệ:**
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 66 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`)
- (`e4` 1 . Tổ chức , cá nhân nộp một ( 01 ) bộ hồ sơ trực tiếp hoặc gửi qua hệ thống bưu chính đến một trong các cơ quan đăng ký quy định tại khoản 2 Điều 63 của Thông tư này . Hồ sơ bao gồm : `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 66 `[DIEU]`)
- (`e6` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e5` khoản 2 Điều 63 của Thông tư này `[THAM_CHIEU_PHAP_LY]`)
- (`e4` 1 . Tổ chức , cá nhân nộp một ( 01 ) bộ hồ sơ trực tiếp hoặc gửi qua hệ thống bưu chính đến một trong các cơ quan đăng ký quy định tại khoản 2 Điều 63 của Thông tư này . Hồ sơ bao gồm : `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e5` khoản 2 Điều 63 của Thông tư này `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #07_2012_TT-BGTVT_27433#body_standalone_55 (Loại: `body_standalone`)
> **[Điều 66]`<DIEU>`** . **[1 . Tổ chức , cá nhân nộp một ( 01 ) bộ hồ sơ trực tiếp hoặc gửi qua hệ thống bưu chính đến một trong các cơ quan đăng ký **[quy định tại]`<TU_KHOA_PHAP_LY>`** **[khoản 2 Điều 63 của Thông tư này]`<THAM_CHIEU_PHAP_LY>`** . Hồ sơ bao gồm :]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 66** → `DIEU` (span: `[0:2]`)
- `[e1]` **1 . Tổ chức , cá nhân nộp một ( 01 ) bộ hồ sơ trực tiếp hoặc gửi qua hệ thống bưu chính đến một trong các cơ quan đăng ký quy định tại khoản 2 Điều 63 của Thông tư này . Hồ sơ bao gồm :** → `KHOAN` (span: `[3:40]`)
- `[e2]` **khoản 2 Điều 63 của Thông tư này** → `THAM_CHIEU_PHAP_LY` (span: `[29:36]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **quy định tại** → `TU_KHOA_PHAP_LY` (span: `[27:29]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 1 . Tổ chức , cá nhân nộp một ( 01 ) bộ hồ sơ trực tiếp hoặc gửi qua hệ thống bưu chính đến một trong các cơ quan đăng ký quy định tại khoản 2 Điều 63 của Thông tư này . Hồ sơ bao gồm : `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 66 `[DIEU]`)
- (`e3` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e2` khoản 2 Điều 63 của Thông tư này `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 1 . Tổ chức , cá nhân nộp một ( 01 ) bộ hồ sơ trực tiếp hoặc gửi qua hệ thống bưu chính đến một trong các cơ quan đăng ký quy định tại khoản 2 Điều 63 của Thông tư này . Hồ sơ bao gồm : `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e2` khoản 2 Điều 63 của Thông tư này `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #07_2012_TT-BGTVT_27433#body_context_56 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[07/2012/TT-BGTVT]`<SO_HIEU>`** của **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Giao thông Vận tải]`<LINH_VUC>`** . **[Điều 66]`<DIEU>`** . **[Khoản 1]`<KHOAN>`** . **[a ) **[Tờ khai đề nghị cấp Sổ thuyền viên]`<GIAY_TO_HO_SO>`** theo mẫu tại **[Phụ lục II]`<THAM_CHIEU_PHAP_LY>`** của Thông tư này ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **07/2012/TT-BGTVT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[4:7]`)
- `[e3]` **Giao thông Vận tải** → `LINH_VUC` (span: `[9:11]`)
- `[e4]` **Điều 66** → `DIEU` (span: `[12:14]`)
- `[e5]` **Khoản 1** → `KHOAN` (span: `[15:17]`)
- `[e6]` **a ) Tờ khai đề nghị cấp Sổ thuyền viên theo mẫu tại Phụ lục II của Thông tư này ;** → `DIEM` (span: `[18:35]`)
- `[e7]` **Phụ lục II** → `THAM_CHIEU_PHAP_LY` (span: `[29:31]`) *(lồng trong `e6` (`DIEM`))*
- `[e8]` **Tờ khai đề nghị cấp Sổ thuyền viên** → `GIAY_TO_HO_SO` (span: `[20:26]`) *(lồng trong `e6` (`DIEM`))*

**Quan hệ:**
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Giao thông Vận tải `[LINH_VUC]`)
- (`e4` Điều 66 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`)
- (`e5` Khoản 1 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 66 `[DIEU]`)
- (`e6` a ) Tờ khai đề nghị cấp Sổ thuyền viên theo mẫu tại Phụ lục II của Thông tư này ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e5` Khoản 1 `[KHOAN]`)
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Giao thông Vận tải `[LINH_VUC]`)
- (`e6` a ) Tờ khai đề nghị cấp Sổ thuyền viên theo mẫu tại Phụ lục II của Thông tư này ; `[DIEM]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Giao thông Vận tải `[LINH_VUC]`)
- (`e6` a ) Tờ khai đề nghị cấp Sổ thuyền viên theo mẫu tại Phụ lục II của Thông tư này ; `[DIEM]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e7` Phụ lục II `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #07_2012_TT-BGTVT_27433#body_standalone_57 (Loại: `body_standalone`)
> **[Điều 66]`<DIEU>`** . **[Khoản 1]`<KHOAN>`** . **[a ) **[Tờ khai đề nghị cấp Sổ thuyền viên]`<GIAY_TO_HO_SO>`** theo mẫu tại **[Phụ lục II]`<THAM_CHIEU_PHAP_LY>`** của Thông tư này ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Điều 66** → `DIEU` (span: `[0:2]`)
- `[e1]` **Khoản 1** → `KHOAN` (span: `[3:5]`)
- `[e2]` **a ) Tờ khai đề nghị cấp Sổ thuyền viên theo mẫu tại Phụ lục II của Thông tư này ;** → `DIEM` (span: `[6:23]`)
- `[e3]` **Phụ lục II** → `THAM_CHIEU_PHAP_LY` (span: `[17:19]`) *(lồng trong `e2` (`DIEM`))*
- `[e4]` **Tờ khai đề nghị cấp Sổ thuyền viên** → `GIAY_TO_HO_SO` (span: `[8:14]`) *(lồng trong `e2` (`DIEM`))*

**Quan hệ:**
- (`e1` Khoản 1 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 66 `[DIEU]`)
- (`e2` a ) Tờ khai đề nghị cấp Sổ thuyền viên theo mẫu tại Phụ lục II của Thông tư này ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e1` Khoản 1 `[KHOAN]`)
- (`e2` a ) Tờ khai đề nghị cấp Sổ thuyền viên theo mẫu tại Phụ lục II của Thông tư này ; `[DIEM]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Phụ lục II `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #07_2012_TT-BGTVT_27433#body_context_58 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[07/2012/TT-BGTVT]`<SO_HIEU>`** của **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Giao thông Vận tải]`<LINH_VUC>`** . **[Điều 66]`<DIEU>`** . **[3 . Trong thời hạn ba ( 03 ) ngày làm việc , kể từ ngày nhận đủ hồ sơ theo quy định , cơ quan đăng ký thuyền viên thực hiện việc vào Sổ đăng ký thuyền viên và cấp **[Sổ thuyền viên]`<GIAY_TO_HO_SO>`** theo mẫu tại **[Phụ lục I]`<THAM_CHIEU_PHAP_LY>`** của Thông tư này . Trường hợp không cấp **[Sổ thuyền viên]`<GIAY_TO_HO_SO>`** , cơ quan đăng ký thuyền viên phải trả lời bằng văn bản trong thời hạn **[quy định tại]`<TU_KHOA_PHAP_LY>`** **[khoản này]`<THAM_CHIEU_PHAP_LY>`** và nêu rõ lý do .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **07/2012/TT-BGTVT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[4:7]`)
- `[e3]` **Giao thông Vận tải** → `LINH_VUC` (span: `[9:11]`)
- `[e4]` **Điều 66** → `DIEU` (span: `[12:14]`)
- `[e5]` **3 . Trong thời hạn ba ( 03 ) ngày làm việc , kể từ ngày nhận đủ hồ sơ theo quy định , cơ quan đăng ký thuyền viên thực hiện việc vào Sổ đăng ký thuyền viên và cấp Sổ thuyền viên theo mẫu tại Phụ lục I của Thông tư này . Trường hợp không cấp Sổ thuyền viên , cơ quan đăng ký thuyền viên phải trả lời bằng văn bản trong thời hạn quy định tại khoản này và nêu rõ lý do .** → `KHOAN` (span: `[15:81]`)
- `[e6]` **Phụ lục I** → `THAM_CHIEU_PHAP_LY` (span: `[51:53]`) *(lồng trong `e5` (`KHOAN`))*
- `[e7]` **khoản này** → `THAM_CHIEU_PHAP_LY` (span: `[74:76]`) *(lồng trong `e5` (`KHOAN`))*
- `[e8]` **quy định tại** → `TU_KHOA_PHAP_LY` (span: `[72:74]`) *(lồng trong `e5` (`KHOAN`))*
- `[e9]` **Sổ thuyền viên** → `GIAY_TO_HO_SO` (span: `[46:48]`) *(lồng trong `e5` (`KHOAN`))*
- `[e10]` **Sổ thuyền viên** → `GIAY_TO_HO_SO` (span: `[60:62]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Giao thông Vận tải `[LINH_VUC]`)
- (`e4` Điều 66 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`)
- (`e5` 3 . Trong thời hạn ba ( 03 ) ngày làm việc , kể từ ngày nhận đủ hồ sơ theo quy định , cơ quan đăng ký thuyền viên thực hiện việc vào Sổ đăng ký thuyền viên và cấp Sổ thuyền viên theo mẫu tại Phụ lục I của Thông tư này . Trường hợp không cấp Sổ thuyền viên , cơ quan đăng ký thuyền viên phải trả lời bằng văn bản trong thời hạn quy định tại khoản này và nêu rõ lý do . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 66 `[DIEU]`)
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Giao thông Vận tải `[LINH_VUC]`)
- (`e5` 3 . Trong thời hạn ba ( 03 ) ngày làm việc , kể từ ngày nhận đủ hồ sơ theo quy định , cơ quan đăng ký thuyền viên thực hiện việc vào Sổ đăng ký thuyền viên và cấp Sổ thuyền viên theo mẫu tại Phụ lục I của Thông tư này . Trường hợp không cấp Sổ thuyền viên , cơ quan đăng ký thuyền viên phải trả lời bằng văn bản trong thời hạn quy định tại khoản này và nêu rõ lý do . `[KHOAN]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Giao thông Vận tải `[LINH_VUC]`)
- (`e5` 3 . Trong thời hạn ba ( 03 ) ngày làm việc , kể từ ngày nhận đủ hồ sơ theo quy định , cơ quan đăng ký thuyền viên thực hiện việc vào Sổ đăng ký thuyền viên và cấp Sổ thuyền viên theo mẫu tại Phụ lục I của Thông tư này . Trường hợp không cấp Sổ thuyền viên , cơ quan đăng ký thuyền viên phải trả lời bằng văn bản trong thời hạn quy định tại khoản này và nêu rõ lý do . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e6` Phụ lục I `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e8` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e7` khoản này `[THAM_CHIEU_PHAP_LY]`)
- (`e5` 3 . Trong thời hạn ba ( 03 ) ngày làm việc , kể từ ngày nhận đủ hồ sơ theo quy định , cơ quan đăng ký thuyền viên thực hiện việc vào Sổ đăng ký thuyền viên và cấp Sổ thuyền viên theo mẫu tại Phụ lục I của Thông tư này . Trường hợp không cấp Sổ thuyền viên , cơ quan đăng ký thuyền viên phải trả lời bằng văn bản trong thời hạn quy định tại khoản này và nêu rõ lý do . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e7` khoản này `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #07_2012_TT-BGTVT_27433#body_standalone_59 (Loại: `body_standalone`)
> **[Điều 66]`<DIEU>`** . **[3 . Trong thời hạn ba ( 03 ) ngày làm việc , kể từ ngày nhận đủ hồ sơ theo quy định , cơ quan đăng ký thuyền viên thực hiện việc vào Sổ đăng ký thuyền viên và cấp **[Sổ thuyền viên]`<GIAY_TO_HO_SO>`** theo mẫu tại **[Phụ lục I]`<THAM_CHIEU_PHAP_LY>`** của Thông tư này . Trường hợp không cấp **[Sổ thuyền viên]`<GIAY_TO_HO_SO>`** , cơ quan đăng ký thuyền viên phải trả lời bằng văn bản trong thời hạn **[quy định tại]`<TU_KHOA_PHAP_LY>`** **[khoản này]`<THAM_CHIEU_PHAP_LY>`** và nêu rõ lý do .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 66** → `DIEU` (span: `[0:2]`)
- `[e1]` **3 . Trong thời hạn ba ( 03 ) ngày làm việc , kể từ ngày nhận đủ hồ sơ theo quy định , cơ quan đăng ký thuyền viên thực hiện việc vào Sổ đăng ký thuyền viên và cấp Sổ thuyền viên theo mẫu tại Phụ lục I của Thông tư này . Trường hợp không cấp Sổ thuyền viên , cơ quan đăng ký thuyền viên phải trả lời bằng văn bản trong thời hạn quy định tại khoản này và nêu rõ lý do .** → `KHOAN` (span: `[3:69]`)
- `[e2]` **Phụ lục I** → `THAM_CHIEU_PHAP_LY` (span: `[39:41]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **khoản này** → `THAM_CHIEU_PHAP_LY` (span: `[62:64]`) *(lồng trong `e1` (`KHOAN`))*
- `[e4]` **quy định tại** → `TU_KHOA_PHAP_LY` (span: `[60:62]`) *(lồng trong `e1` (`KHOAN`))*
- `[e5]` **Sổ thuyền viên** → `GIAY_TO_HO_SO` (span: `[34:36]`) *(lồng trong `e1` (`KHOAN`))*
- `[e6]` **Sổ thuyền viên** → `GIAY_TO_HO_SO` (span: `[48:50]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 3 . Trong thời hạn ba ( 03 ) ngày làm việc , kể từ ngày nhận đủ hồ sơ theo quy định , cơ quan đăng ký thuyền viên thực hiện việc vào Sổ đăng ký thuyền viên và cấp Sổ thuyền viên theo mẫu tại Phụ lục I của Thông tư này . Trường hợp không cấp Sổ thuyền viên , cơ quan đăng ký thuyền viên phải trả lời bằng văn bản trong thời hạn quy định tại khoản này và nêu rõ lý do . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 66 `[DIEU]`)
- (`e1` 3 . Trong thời hạn ba ( 03 ) ngày làm việc , kể từ ngày nhận đủ hồ sơ theo quy định , cơ quan đăng ký thuyền viên thực hiện việc vào Sổ đăng ký thuyền viên và cấp Sổ thuyền viên theo mẫu tại Phụ lục I của Thông tư này . Trường hợp không cấp Sổ thuyền viên , cơ quan đăng ký thuyền viên phải trả lời bằng văn bản trong thời hạn quy định tại khoản này và nêu rõ lý do . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e2` Phụ lục I `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e4` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` khoản này `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 3 . Trong thời hạn ba ( 03 ) ngày làm việc , kể từ ngày nhận đủ hồ sơ theo quy định , cơ quan đăng ký thuyền viên thực hiện việc vào Sổ đăng ký thuyền viên và cấp Sổ thuyền viên theo mẫu tại Phụ lục I của Thông tư này . Trường hợp không cấp Sổ thuyền viên , cơ quan đăng ký thuyền viên phải trả lời bằng văn bản trong thời hạn quy định tại khoản này và nêu rõ lý do . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` khoản này `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #07_2012_TT-BGTVT_27433#body_context_60 (Loại: `body_context`)
> **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[07/2012/TT-BGTVT]`<SO_HIEU>`** . **[Điều 67]`<DIEU>`** . **[2 . Tổ chức , cá nhân nộp một ( 01 ) bộ hồ sơ cấp lại **[Sổ thuyền viên]`<GIAY_TO_HO_SO>`** trực tiếp hoặc gửi qua hệ thống bưu chính đến cơ quan cơ quan đăng ký thuyền viên đã cấp **[Sổ thuyền viên]`<GIAY_TO_HO_SO>`** lần đầu . Hồ sơ cấp lại **[Sổ thuyền viên]`<GIAY_TO_HO_SO>`** bao gồm :]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[4:5]`)
- `[e1]` **07/2012/TT-BGTVT** → `SO_HIEU` (span: `[6:7]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[0:3]`)
- `[e3]` **Điều 67** → `DIEU` (span: `[8:10]`)
- `[e4]` **2 . Tổ chức , cá nhân nộp một ( 01 ) bộ hồ sơ cấp lại Sổ thuyền viên trực tiếp hoặc gửi qua hệ thống bưu chính đến cơ quan cơ quan đăng ký thuyền viên đã cấp Sổ thuyền viên lần đầu . Hồ sơ cấp lại Sổ thuyền viên bao gồm :** → `KHOAN` (span: `[11:50]`)
- `[e5]` **Sổ thuyền viên** → `GIAY_TO_HO_SO` (span: `[24:26]`) *(lồng trong `e4` (`KHOAN`))*
- `[e6]` **Sổ thuyền viên** → `GIAY_TO_HO_SO` (span: `[39:41]`) *(lồng trong `e4` (`KHOAN`))*
- `[e7]` **Sổ thuyền viên** → `GIAY_TO_HO_SO` (span: `[46:48]`) *(lồng trong `e4` (`KHOAN`))*

**Quan hệ:**
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 67 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`)
- (`e4` 2 . Tổ chức , cá nhân nộp một ( 01 ) bộ hồ sơ cấp lại Sổ thuyền viên trực tiếp hoặc gửi qua hệ thống bưu chính đến cơ quan cơ quan đăng ký thuyền viên đã cấp Sổ thuyền viên lần đầu . Hồ sơ cấp lại Sổ thuyền viên bao gồm : `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 67 `[DIEU]`)


---

### Mẫu #07_2012_TT-BGTVT_27433#body_standalone_61 (Loại: `body_standalone`)
> **[Điều 67]`<DIEU>`** . **[2 . Tổ chức , cá nhân nộp một ( 01 ) bộ hồ sơ cấp lại **[Sổ thuyền viên]`<GIAY_TO_HO_SO>`** trực tiếp hoặc gửi qua hệ thống bưu chính đến cơ quan cơ quan đăng ký thuyền viên đã cấp **[Sổ thuyền viên]`<GIAY_TO_HO_SO>`** lần đầu . Hồ sơ cấp lại **[Sổ thuyền viên]`<GIAY_TO_HO_SO>`** bao gồm :]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 67** → `DIEU` (span: `[0:2]`)
- `[e1]` **2 . Tổ chức , cá nhân nộp một ( 01 ) bộ hồ sơ cấp lại Sổ thuyền viên trực tiếp hoặc gửi qua hệ thống bưu chính đến cơ quan cơ quan đăng ký thuyền viên đã cấp Sổ thuyền viên lần đầu . Hồ sơ cấp lại Sổ thuyền viên bao gồm :** → `KHOAN` (span: `[3:42]`)
- `[e2]` **Sổ thuyền viên** → `GIAY_TO_HO_SO` (span: `[16:18]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **Sổ thuyền viên** → `GIAY_TO_HO_SO` (span: `[31:33]`) *(lồng trong `e1` (`KHOAN`))*
- `[e4]` **Sổ thuyền viên** → `GIAY_TO_HO_SO` (span: `[38:40]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 2 . Tổ chức , cá nhân nộp một ( 01 ) bộ hồ sơ cấp lại Sổ thuyền viên trực tiếp hoặc gửi qua hệ thống bưu chính đến cơ quan cơ quan đăng ký thuyền viên đã cấp Sổ thuyền viên lần đầu . Hồ sơ cấp lại Sổ thuyền viên bao gồm : `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 67 `[DIEU]`)


---

### Mẫu #07_2012_TT-BGTVT_27433#body_context_62 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[07/2012/TT-BGTVT]`<SO_HIEU>`** ban hành **[ngày 21 tháng 03 năm 2012]`<NGAY_BAN_HANH>`** bởi **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** . **[Điều 67]`<DIEU>`** . **[Khoản 2]`<KHOAN>`** . **[a ) **[Tờ khai đề nghị cấp lại sổ thuyền viên]`<GIAY_TO_HO_SO>`** theo mẫu tại **[Phụ lục II]`<THAM_CHIEU_PHAP_LY>`** của Thông tư này ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **07/2012/TT-BGTVT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[11:14]`)
- `[e3]` **ngày 21 tháng 03 năm 2012** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 67** → `DIEU` (span: `[15:17]`)
- `[e5]` **Khoản 2** → `KHOAN` (span: `[18:20]`)
- `[e6]` **a ) Tờ khai đề nghị cấp lại sổ thuyền viên theo mẫu tại Phụ lục II của Thông tư này ;** → `DIEM` (span: `[21:39]`)
- `[e7]` **Phụ lục II** → `THAM_CHIEU_PHAP_LY` (span: `[33:35]`) *(lồng trong `e6` (`DIEM`))*
- `[e8]` **Tờ khai đề nghị cấp lại sổ thuyền viên** → `GIAY_TO_HO_SO` (span: `[23:30]`) *(lồng trong `e6` (`DIEM`))*

**Quan hệ:**
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 21 tháng 03 năm 2012 `[NGAY_BAN_HANH]`)
- (`e4` Điều 67 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`)
- (`e5` Khoản 2 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 67 `[DIEU]`)
- (`e6` a ) Tờ khai đề nghị cấp lại sổ thuyền viên theo mẫu tại Phụ lục II của Thông tư này ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e5` Khoản 2 `[KHOAN]`)
- (`e6` a ) Tờ khai đề nghị cấp lại sổ thuyền viên theo mẫu tại Phụ lục II của Thông tư này ; `[DIEM]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e7` Phụ lục II `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #07_2012_TT-BGTVT_27433#body_standalone_63 (Loại: `body_standalone`)
> **[Điều 67]`<DIEU>`** . **[Khoản 2]`<KHOAN>`** . **[a ) **[Tờ khai đề nghị cấp lại sổ thuyền viên]`<GIAY_TO_HO_SO>`** theo mẫu tại **[Phụ lục II]`<THAM_CHIEU_PHAP_LY>`** của Thông tư này ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Điều 67** → `DIEU` (span: `[0:2]`)
- `[e1]` **Khoản 2** → `KHOAN` (span: `[3:5]`)
- `[e2]` **a ) Tờ khai đề nghị cấp lại sổ thuyền viên theo mẫu tại Phụ lục II của Thông tư này ;** → `DIEM` (span: `[6:24]`)
- `[e3]` **Phụ lục II** → `THAM_CHIEU_PHAP_LY` (span: `[18:20]`) *(lồng trong `e2` (`DIEM`))*
- `[e4]` **Tờ khai đề nghị cấp lại sổ thuyền viên** → `GIAY_TO_HO_SO` (span: `[8:15]`) *(lồng trong `e2` (`DIEM`))*

**Quan hệ:**
- (`e1` Khoản 2 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 67 `[DIEU]`)
- (`e2` a ) Tờ khai đề nghị cấp lại sổ thuyền viên theo mẫu tại Phụ lục II của Thông tư này ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e1` Khoản 2 `[KHOAN]`)
- (`e2` a ) Tờ khai đề nghị cấp lại sổ thuyền viên theo mẫu tại Phụ lục II của Thông tư này ; `[DIEM]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Phụ lục II `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #07_2012_TT-BGTVT_27433#body_context_64 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[07/2012/TT-BGTVT]`<SO_HIEU>`** của **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Giao thông Vận tải]`<LINH_VUC>`** . **[Điều 67]`<DIEU>`** . **[Khoản 3]`<KHOAN>`** . **[b ) Trường hợp nhận hồ sơ nhận qua hệ thống bưu chính , nếu hồ sơ không đầy đủ theo quy định , trong thời gian chậm nhất hai ( 02 ) ngày làm việc kể từ ngày nhận được hồ sơ thì cơ quan đăng ký thuyền viên phải trả lời bằng văn bản và nêu rõ lý do .]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **07/2012/TT-BGTVT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[4:7]`)
- `[e3]` **Giao thông Vận tải** → `LINH_VUC` (span: `[9:11]`)
- `[e4]` **Điều 67** → `DIEU` (span: `[12:14]`)
- `[e5]` **Khoản 3** → `KHOAN` (span: `[15:17]`)
- `[e6]` **b ) Trường hợp nhận hồ sơ nhận qua hệ thống bưu chính , nếu hồ sơ không đầy đủ theo quy định , trong thời gian chậm nhất hai ( 02 ) ngày làm việc kể từ ngày nhận được hồ sơ thì cơ quan đăng ký thuyền viên phải trả lời bằng văn bản và nêu rõ lý do .** → `DIEM` (span: `[18:64]`)

**Quan hệ:**
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Giao thông Vận tải `[LINH_VUC]`)
- (`e4` Điều 67 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`)
- (`e5` Khoản 3 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 67 `[DIEU]`)
- (`e6` b ) Trường hợp nhận hồ sơ nhận qua hệ thống bưu chính , nếu hồ sơ không đầy đủ theo quy định , trong thời gian chậm nhất hai ( 02 ) ngày làm việc kể từ ngày nhận được hồ sơ thì cơ quan đăng ký thuyền viên phải trả lời bằng văn bản và nêu rõ lý do . `[DIEM]`) ==[ **THUOC_VE** ]==> (`e5` Khoản 3 `[KHOAN]`)
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Giao thông Vận tải `[LINH_VUC]`)
- (`e6` b ) Trường hợp nhận hồ sơ nhận qua hệ thống bưu chính , nếu hồ sơ không đầy đủ theo quy định , trong thời gian chậm nhất hai ( 02 ) ngày làm việc kể từ ngày nhận được hồ sơ thì cơ quan đăng ký thuyền viên phải trả lời bằng văn bản và nêu rõ lý do . `[DIEM]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Giao thông Vận tải `[LINH_VUC]`)


---

### Mẫu #07_2012_TT-BGTVT_27433#body_standalone_65 (Loại: `body_standalone`)
> **[Điều 67]`<DIEU>`** . **[Khoản 3]`<KHOAN>`** . **[b ) Trường hợp nhận hồ sơ nhận qua hệ thống bưu chính , nếu hồ sơ không đầy đủ theo quy định , trong thời gian chậm nhất hai ( 02 ) ngày làm việc kể từ ngày nhận được hồ sơ thì cơ quan đăng ký thuyền viên phải trả lời bằng văn bản và nêu rõ lý do .]`<DIEM>`**

**Thực thể:**
- `[e0]` **Điều 67** → `DIEU` (span: `[0:2]`)
- `[e1]` **Khoản 3** → `KHOAN` (span: `[3:5]`)
- `[e2]` **b ) Trường hợp nhận hồ sơ nhận qua hệ thống bưu chính , nếu hồ sơ không đầy đủ theo quy định , trong thời gian chậm nhất hai ( 02 ) ngày làm việc kể từ ngày nhận được hồ sơ thì cơ quan đăng ký thuyền viên phải trả lời bằng văn bản và nêu rõ lý do .** → `DIEM` (span: `[6:52]`)

**Quan hệ:**
- (`e1` Khoản 3 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 67 `[DIEU]`)
- (`e2` b ) Trường hợp nhận hồ sơ nhận qua hệ thống bưu chính , nếu hồ sơ không đầy đủ theo quy định , trong thời gian chậm nhất hai ( 02 ) ngày làm việc kể từ ngày nhận được hồ sơ thì cơ quan đăng ký thuyền viên phải trả lời bằng văn bản và nêu rõ lý do . `[DIEM]`) ==[ **THUOC_VE** ]==> (`e1` Khoản 3 `[KHOAN]`)


---

### Mẫu #07_2012_TT-BGTVT_27433#body_context_66 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[07/2012/TT-BGTVT]`<SO_HIEU>`** ban hành **[ngày 21 tháng 03 năm 2012]`<NGAY_BAN_HANH>`** bởi **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** . **[Điều 67]`<DIEU>`** . **[4 . Trong thời hạn ba ( 03 ) ngày làm việc , kể từ ngày nhận đủ hồ sơ theo quy định , cơ quan đăng ký thuyền viên thực hiện việc vào Sổ đăng ký thuyền viên và cấp **[Sổ thuyền viên]`<GIAY_TO_HO_SO>`** theo mẫu **[quy định tại]`<TU_KHOA_PHAP_LY>`** **[Phụ lục I]`<THAM_CHIEU_PHAP_LY>`** của Thông tư này . Trường hợp không lại cấp **[Sổ thuyền viên]`<GIAY_TO_HO_SO>`** , cơ quan đăng ký thuyền viên phải trả lời bằng văn bản trong thời hạn **[quy định tại]`<TU_KHOA_PHAP_LY>`** **[khoản này]`<THAM_CHIEU_PHAP_LY>`** và nêu rõ lý do .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **07/2012/TT-BGTVT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[11:14]`)
- `[e3]` **ngày 21 tháng 03 năm 2012** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 67** → `DIEU` (span: `[15:17]`)
- `[e5]` **4 . Trong thời hạn ba ( 03 ) ngày làm việc , kể từ ngày nhận đủ hồ sơ theo quy định , cơ quan đăng ký thuyền viên thực hiện việc vào Sổ đăng ký thuyền viên và cấp Sổ thuyền viên theo mẫu quy định tại Phụ lục I của Thông tư này . Trường hợp không lại cấp Sổ thuyền viên , cơ quan đăng ký thuyền viên phải trả lời bằng văn bản trong thời hạn quy định tại khoản này và nêu rõ lý do .** → `KHOAN` (span: `[18:86]`)
- `[e6]` **Phụ lục I** → `THAM_CHIEU_PHAP_LY` (span: `[55:57]`) *(lồng trong `e5` (`KHOAN`))*
- `[e7]` **khoản này** → `THAM_CHIEU_PHAP_LY` (span: `[79:81]`) *(lồng trong `e5` (`KHOAN`))*
- `[e8]` **quy định tại** → `TU_KHOA_PHAP_LY` (span: `[53:55]`) *(lồng trong `e5` (`KHOAN`))*
- `[e9]` **quy định tại** → `TU_KHOA_PHAP_LY` (span: `[77:79]`) *(lồng trong `e5` (`KHOAN`))*
- `[e10]` **Sổ thuyền viên** → `GIAY_TO_HO_SO` (span: `[49:51]`) *(lồng trong `e5` (`KHOAN`))*
- `[e11]` **Sổ thuyền viên** → `GIAY_TO_HO_SO` (span: `[65:67]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 21 tháng 03 năm 2012 `[NGAY_BAN_HANH]`)
- (`e4` Điều 67 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`)
- (`e5` 4 . Trong thời hạn ba ( 03 ) ngày làm việc , kể từ ngày nhận đủ hồ sơ theo quy định , cơ quan đăng ký thuyền viên thực hiện việc vào Sổ đăng ký thuyền viên và cấp Sổ thuyền viên theo mẫu quy định tại Phụ lục I của Thông tư này . Trường hợp không lại cấp Sổ thuyền viên , cơ quan đăng ký thuyền viên phải trả lời bằng văn bản trong thời hạn quy định tại khoản này và nêu rõ lý do . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 67 `[DIEU]`)
- (`e8` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e6` Phụ lục I `[THAM_CHIEU_PHAP_LY]`)
- (`e5` 4 . Trong thời hạn ba ( 03 ) ngày làm việc , kể từ ngày nhận đủ hồ sơ theo quy định , cơ quan đăng ký thuyền viên thực hiện việc vào Sổ đăng ký thuyền viên và cấp Sổ thuyền viên theo mẫu quy định tại Phụ lục I của Thông tư này . Trường hợp không lại cấp Sổ thuyền viên , cơ quan đăng ký thuyền viên phải trả lời bằng văn bản trong thời hạn quy định tại khoản này và nêu rõ lý do . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e6` Phụ lục I `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e9` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e7` khoản này `[THAM_CHIEU_PHAP_LY]`)
- (`e5` 4 . Trong thời hạn ba ( 03 ) ngày làm việc , kể từ ngày nhận đủ hồ sơ theo quy định , cơ quan đăng ký thuyền viên thực hiện việc vào Sổ đăng ký thuyền viên và cấp Sổ thuyền viên theo mẫu quy định tại Phụ lục I của Thông tư này . Trường hợp không lại cấp Sổ thuyền viên , cơ quan đăng ký thuyền viên phải trả lời bằng văn bản trong thời hạn quy định tại khoản này và nêu rõ lý do . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e7` khoản này `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #07_2012_TT-BGTVT_27433#body_standalone_67 (Loại: `body_standalone`)
> **[Điều 67]`<DIEU>`** . **[4 . Trong thời hạn ba ( 03 ) ngày làm việc , kể từ ngày nhận đủ hồ sơ theo quy định , cơ quan đăng ký thuyền viên thực hiện việc vào Sổ đăng ký thuyền viên và cấp **[Sổ thuyền viên]`<GIAY_TO_HO_SO>`** theo mẫu **[quy định tại]`<TU_KHOA_PHAP_LY>`** **[Phụ lục I]`<THAM_CHIEU_PHAP_LY>`** của Thông tư này . Trường hợp không lại cấp **[Sổ thuyền viên]`<GIAY_TO_HO_SO>`** , cơ quan đăng ký thuyền viên phải trả lời bằng văn bản trong thời hạn **[quy định tại]`<TU_KHOA_PHAP_LY>`** **[khoản này]`<THAM_CHIEU_PHAP_LY>`** và nêu rõ lý do .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 67** → `DIEU` (span: `[0:2]`)
- `[e1]` **4 . Trong thời hạn ba ( 03 ) ngày làm việc , kể từ ngày nhận đủ hồ sơ theo quy định , cơ quan đăng ký thuyền viên thực hiện việc vào Sổ đăng ký thuyền viên và cấp Sổ thuyền viên theo mẫu quy định tại Phụ lục I của Thông tư này . Trường hợp không lại cấp Sổ thuyền viên , cơ quan đăng ký thuyền viên phải trả lời bằng văn bản trong thời hạn quy định tại khoản này và nêu rõ lý do .** → `KHOAN` (span: `[3:71]`)
- `[e2]` **Phụ lục I** → `THAM_CHIEU_PHAP_LY` (span: `[40:42]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **khoản này** → `THAM_CHIEU_PHAP_LY` (span: `[64:66]`) *(lồng trong `e1` (`KHOAN`))*
- `[e4]` **quy định tại** → `TU_KHOA_PHAP_LY` (span: `[38:40]`) *(lồng trong `e1` (`KHOAN`))*
- `[e5]` **quy định tại** → `TU_KHOA_PHAP_LY` (span: `[62:64]`) *(lồng trong `e1` (`KHOAN`))*
- `[e6]` **Sổ thuyền viên** → `GIAY_TO_HO_SO` (span: `[34:36]`) *(lồng trong `e1` (`KHOAN`))*
- `[e7]` **Sổ thuyền viên** → `GIAY_TO_HO_SO` (span: `[50:52]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 4 . Trong thời hạn ba ( 03 ) ngày làm việc , kể từ ngày nhận đủ hồ sơ theo quy định , cơ quan đăng ký thuyền viên thực hiện việc vào Sổ đăng ký thuyền viên và cấp Sổ thuyền viên theo mẫu quy định tại Phụ lục I của Thông tư này . Trường hợp không lại cấp Sổ thuyền viên , cơ quan đăng ký thuyền viên phải trả lời bằng văn bản trong thời hạn quy định tại khoản này và nêu rõ lý do . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 67 `[DIEU]`)
- (`e4` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e2` Phụ lục I `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 4 . Trong thời hạn ba ( 03 ) ngày làm việc , kể từ ngày nhận đủ hồ sơ theo quy định , cơ quan đăng ký thuyền viên thực hiện việc vào Sổ đăng ký thuyền viên và cấp Sổ thuyền viên theo mẫu quy định tại Phụ lục I của Thông tư này . Trường hợp không lại cấp Sổ thuyền viên , cơ quan đăng ký thuyền viên phải trả lời bằng văn bản trong thời hạn quy định tại khoản này và nêu rõ lý do . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e2` Phụ lục I `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e5` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` khoản này `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 4 . Trong thời hạn ba ( 03 ) ngày làm việc , kể từ ngày nhận đủ hồ sơ theo quy định , cơ quan đăng ký thuyền viên thực hiện việc vào Sổ đăng ký thuyền viên và cấp Sổ thuyền viên theo mẫu quy định tại Phụ lục I của Thông tư này . Trường hợp không lại cấp Sổ thuyền viên , cơ quan đăng ký thuyền viên phải trả lời bằng văn bản trong thời hạn quy định tại khoản này và nêu rõ lý do . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` khoản này `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #07_2012_TT-BGTVT_27433#body_context_68 (Loại: `body_context`)
> **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[07/2012/TT-BGTVT]`<SO_HIEU>`** . **[Điều 69]`<DIEU>`** . **[1 . **[Hộ chiếu thuyền viên]`<GIAY_TO_HO_SO>`** được cấp cho thuyền viên Việt Nam làm việc trên **[tàu biển]`<TAI_SAN_VAT_CHAT>`** hoạt động trên tuyến quốc tế và có giá trị sử dụng để xuất cảnh , nhập cảnh theo **[tàu biển]`<TAI_SAN_VAT_CHAT>`** .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[4:5]`)
- `[e1]` **07/2012/TT-BGTVT** → `SO_HIEU` (span: `[6:7]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[0:3]`)
- `[e3]` **Điều 69** → `DIEU` (span: `[8:10]`)
- `[e4]` **1 . Hộ chiếu thuyền viên được cấp cho thuyền viên Việt Nam làm việc trên tàu biển hoạt động trên tuyến quốc tế và có giá trị sử dụng để xuất cảnh , nhập cảnh theo tàu biển .** → `KHOAN` (span: `[11:38]`)
- `[e5]` **Hộ chiếu thuyền viên** → `GIAY_TO_HO_SO` (span: `[13:15]`) *(lồng trong `e4` (`KHOAN`))*
- `[e6]` **tàu biển** → `TAI_SAN_VAT_CHAT` (span: `[22:23]`) *(lồng trong `e4` (`KHOAN`))*
- `[e7]` **tàu biển** → `TAI_SAN_VAT_CHAT` (span: `[36:37]`) *(lồng trong `e4` (`KHOAN`))*

**Quan hệ:**
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 69 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`)
- (`e4` 1 . Hộ chiếu thuyền viên được cấp cho thuyền viên Việt Nam làm việc trên tàu biển hoạt động trên tuyến quốc tế và có giá trị sử dụng để xuất cảnh , nhập cảnh theo tàu biển . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 69 `[DIEU]`)


---

### Mẫu #07_2012_TT-BGTVT_27433#body_standalone_69 (Loại: `body_standalone`)
> **[Điều 69]`<DIEU>`** . **[1 . **[Hộ chiếu thuyền viên]`<GIAY_TO_HO_SO>`** được cấp cho thuyền viên Việt Nam làm việc trên **[tàu biển]`<TAI_SAN_VAT_CHAT>`** hoạt động trên tuyến quốc tế và có giá trị sử dụng để xuất cảnh , nhập cảnh theo **[tàu biển]`<TAI_SAN_VAT_CHAT>`** .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 69** → `DIEU` (span: `[0:2]`)
- `[e1]` **1 . Hộ chiếu thuyền viên được cấp cho thuyền viên Việt Nam làm việc trên tàu biển hoạt động trên tuyến quốc tế và có giá trị sử dụng để xuất cảnh , nhập cảnh theo tàu biển .** → `KHOAN` (span: `[3:30]`)
- `[e2]` **Hộ chiếu thuyền viên** → `GIAY_TO_HO_SO` (span: `[5:7]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **tàu biển** → `TAI_SAN_VAT_CHAT` (span: `[14:15]`) *(lồng trong `e1` (`KHOAN`))*
- `[e4]` **tàu biển** → `TAI_SAN_VAT_CHAT` (span: `[28:29]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 1 . Hộ chiếu thuyền viên được cấp cho thuyền viên Việt Nam làm việc trên tàu biển hoạt động trên tuyến quốc tế và có giá trị sử dụng để xuất cảnh , nhập cảnh theo tàu biển . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 69 `[DIEU]`)


---

### Mẫu #07_2012_TT-BGTVT_27433#body_context_70 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[07/2012/TT-BGTVT]`<SO_HIEU>`** của **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Giao thông Vận tải]`<LINH_VUC>`** . **[Điều 69]`<DIEU>`** . **[2 . **[Hộ chiếu thuyền viên]`<GIAY_TO_HO_SO>`** do Cục Hàng hải Việt Nam cấp theo mẫu tại **[Phụ lục III]`<THAM_CHIEU_PHAP_LY>`** của Thông tư này . **[Hộ chiếu thuyền viên]`<GIAY_TO_HO_SO>`** có giá trị không quá 05 ( năm ) năm kể từ ngày cấp mới hoặc cấp lại .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **07/2012/TT-BGTVT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[4:7]`)
- `[e3]` **Giao thông Vận tải** → `LINH_VUC` (span: `[9:11]`)
- `[e4]` **Điều 69** → `DIEU` (span: `[12:14]`)
- `[e5]` **2 . Hộ chiếu thuyền viên do Cục Hàng hải Việt Nam cấp theo mẫu tại Phụ lục III của Thông tư này . Hộ chiếu thuyền viên có giá trị không quá 05 ( năm ) năm kể từ ngày cấp mới hoặc cấp lại .** → `KHOAN` (span: `[15:53]`)
- `[e6]` **Phụ lục III** → `THAM_CHIEU_PHAP_LY` (span: `[27:29]`) *(lồng trong `e5` (`KHOAN`))*
- `[e7]` **Hộ chiếu thuyền viên** → `GIAY_TO_HO_SO` (span: `[17:19]`) *(lồng trong `e5` (`KHOAN`))*
- `[e8]` **Hộ chiếu thuyền viên** → `GIAY_TO_HO_SO` (span: `[33:35]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Giao thông Vận tải `[LINH_VUC]`)
- (`e4` Điều 69 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`)
- (`e5` 2 . Hộ chiếu thuyền viên do Cục Hàng hải Việt Nam cấp theo mẫu tại Phụ lục III của Thông tư này . Hộ chiếu thuyền viên có giá trị không quá 05 ( năm ) năm kể từ ngày cấp mới hoặc cấp lại . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 69 `[DIEU]`)
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Giao thông Vận tải `[LINH_VUC]`)
- (`e5` 2 . Hộ chiếu thuyền viên do Cục Hàng hải Việt Nam cấp theo mẫu tại Phụ lục III của Thông tư này . Hộ chiếu thuyền viên có giá trị không quá 05 ( năm ) năm kể từ ngày cấp mới hoặc cấp lại . `[KHOAN]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Giao thông Vận tải `[LINH_VUC]`)
- (`e5` 2 . Hộ chiếu thuyền viên do Cục Hàng hải Việt Nam cấp theo mẫu tại Phụ lục III của Thông tư này . Hộ chiếu thuyền viên có giá trị không quá 05 ( năm ) năm kể từ ngày cấp mới hoặc cấp lại . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e6` Phụ lục III `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #07_2012_TT-BGTVT_27433#body_standalone_71 (Loại: `body_standalone`)
> **[Điều 69]`<DIEU>`** . **[2 . **[Hộ chiếu thuyền viên]`<GIAY_TO_HO_SO>`** do Cục Hàng hải Việt Nam cấp theo mẫu tại **[Phụ lục III]`<THAM_CHIEU_PHAP_LY>`** của Thông tư này . **[Hộ chiếu thuyền viên]`<GIAY_TO_HO_SO>`** có giá trị không quá 05 ( năm ) năm kể từ ngày cấp mới hoặc cấp lại .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 69** → `DIEU` (span: `[0:2]`)
- `[e1]` **2 . Hộ chiếu thuyền viên do Cục Hàng hải Việt Nam cấp theo mẫu tại Phụ lục III của Thông tư này . Hộ chiếu thuyền viên có giá trị không quá 05 ( năm ) năm kể từ ngày cấp mới hoặc cấp lại .** → `KHOAN` (span: `[3:41]`)
- `[e2]` **Phụ lục III** → `THAM_CHIEU_PHAP_LY` (span: `[15:17]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **Hộ chiếu thuyền viên** → `GIAY_TO_HO_SO` (span: `[5:7]`) *(lồng trong `e1` (`KHOAN`))*
- `[e4]` **Hộ chiếu thuyền viên** → `GIAY_TO_HO_SO` (span: `[21:23]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 2 . Hộ chiếu thuyền viên do Cục Hàng hải Việt Nam cấp theo mẫu tại Phụ lục III của Thông tư này . Hộ chiếu thuyền viên có giá trị không quá 05 ( năm ) năm kể từ ngày cấp mới hoặc cấp lại . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 69 `[DIEU]`)
- (`e1` 2 . Hộ chiếu thuyền viên do Cục Hàng hải Việt Nam cấp theo mẫu tại Phụ lục III của Thông tư này . Hộ chiếu thuyền viên có giá trị không quá 05 ( năm ) năm kể từ ngày cấp mới hoặc cấp lại . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e2` Phụ lục III `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #07_2012_TT-BGTVT_27433#body_context_72 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[07/2012/TT-BGTVT]`<SO_HIEU>`** của **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Giao thông Vận tải]`<LINH_VUC>`** . **[Điều 71]`<DIEU>`** . **[Khoản 1]`<KHOAN>`** . **[a ) **[Tờ khai đề nghị cấp Hộ chiếu thuyền viên]`<GIAY_TO_HO_SO>`** theo mẫu tại **[Phụ lục IV]`<THAM_CHIEU_PHAP_LY>`** của Thông tư này ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **07/2012/TT-BGTVT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[4:7]`)
- `[e3]` **Giao thông Vận tải** → `LINH_VUC` (span: `[9:11]`)
- `[e4]` **Điều 71** → `DIEU` (span: `[12:14]`)
- `[e5]` **Khoản 1** → `KHOAN` (span: `[15:17]`)
- `[e6]` **a ) Tờ khai đề nghị cấp Hộ chiếu thuyền viên theo mẫu tại Phụ lục IV của Thông tư này ;** → `DIEM` (span: `[18:35]`)
- `[e7]` **Phụ lục IV** → `THAM_CHIEU_PHAP_LY` (span: `[29:31]`) *(lồng trong `e6` (`DIEM`))*
- `[e8]` **Tờ khai đề nghị cấp Hộ chiếu thuyền viên** → `GIAY_TO_HO_SO` (span: `[20:26]`) *(lồng trong `e6` (`DIEM`))*

**Quan hệ:**
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Giao thông Vận tải `[LINH_VUC]`)
- (`e4` Điều 71 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`)
- (`e5` Khoản 1 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 71 `[DIEU]`)
- (`e6` a ) Tờ khai đề nghị cấp Hộ chiếu thuyền viên theo mẫu tại Phụ lục IV của Thông tư này ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e5` Khoản 1 `[KHOAN]`)
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Giao thông Vận tải `[LINH_VUC]`)
- (`e6` a ) Tờ khai đề nghị cấp Hộ chiếu thuyền viên theo mẫu tại Phụ lục IV của Thông tư này ; `[DIEM]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Giao thông Vận tải `[LINH_VUC]`)
- (`e6` a ) Tờ khai đề nghị cấp Hộ chiếu thuyền viên theo mẫu tại Phụ lục IV của Thông tư này ; `[DIEM]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e7` Phụ lục IV `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #07_2012_TT-BGTVT_27433#body_standalone_73 (Loại: `body_standalone`)
> **[Điều 71]`<DIEU>`** . **[Khoản 1]`<KHOAN>`** . **[a ) **[Tờ khai đề nghị cấp Hộ chiếu thuyền viên]`<GIAY_TO_HO_SO>`** theo mẫu tại **[Phụ lục IV]`<THAM_CHIEU_PHAP_LY>`** của Thông tư này ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Điều 71** → `DIEU` (span: `[0:2]`)
- `[e1]` **Khoản 1** → `KHOAN` (span: `[3:5]`)
- `[e2]` **a ) Tờ khai đề nghị cấp Hộ chiếu thuyền viên theo mẫu tại Phụ lục IV của Thông tư này ;** → `DIEM` (span: `[6:23]`)
- `[e3]` **Phụ lục IV** → `THAM_CHIEU_PHAP_LY` (span: `[17:19]`) *(lồng trong `e2` (`DIEM`))*
- `[e4]` **Tờ khai đề nghị cấp Hộ chiếu thuyền viên** → `GIAY_TO_HO_SO` (span: `[8:14]`) *(lồng trong `e2` (`DIEM`))*

**Quan hệ:**
- (`e1` Khoản 1 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 71 `[DIEU]`)
- (`e2` a ) Tờ khai đề nghị cấp Hộ chiếu thuyền viên theo mẫu tại Phụ lục IV của Thông tư này ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e1` Khoản 1 `[KHOAN]`)
- (`e2` a ) Tờ khai đề nghị cấp Hộ chiếu thuyền viên theo mẫu tại Phụ lục IV của Thông tư này ; `[DIEM]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Phụ lục IV `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #07_2012_TT-BGTVT_27433#body_context_74 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[07/2012/TT-BGTVT]`<SO_HIEU>`** của **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Giao thông Vận tải]`<LINH_VUC>`** . **[Điều 71]`<DIEU>`** . **[3 . Trong thời hạn ba ( 03 ) ngày làm việc , kể từ ngày nhận đủ hồ sơ theo quy định , Cục Hàng hải Việt Nam thực hiện việc cấp **[Hộ chiếu thuyền viên]`<GIAY_TO_HO_SO>`** theo mẫu tại **[Phụ lục III]`<THAM_CHIEU_PHAP_LY>`** của Thông tư này . Trường hợp không cấp **[Hộ chiếu thuyền viên]`<GIAY_TO_HO_SO>`** , Cục Hàng hải Việt Nam phải trả lời bằng văn bản trong thời hạn **[quy định tại]`<TU_KHOA_PHAP_LY>`** **[khoản này]`<THAM_CHIEU_PHAP_LY>`** và nêu rõ lý do .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **07/2012/TT-BGTVT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[4:7]`)
- `[e3]` **Giao thông Vận tải** → `LINH_VUC` (span: `[9:11]`)
- `[e4]` **Điều 71** → `DIEU` (span: `[12:14]`)
- `[e5]` **3 . Trong thời hạn ba ( 03 ) ngày làm việc , kể từ ngày nhận đủ hồ sơ theo quy định , Cục Hàng hải Việt Nam thực hiện việc cấp Hộ chiếu thuyền viên theo mẫu tại Phụ lục III của Thông tư này . Trường hợp không cấp Hộ chiếu thuyền viên , Cục Hàng hải Việt Nam phải trả lời bằng văn bản trong thời hạn quy định tại khoản này và nêu rõ lý do .** → `KHOAN` (span: `[15:76]`)
- `[e6]` **Phụ lục III** → `THAM_CHIEU_PHAP_LY` (span: `[46:48]`) *(lồng trong `e5` (`KHOAN`))*
- `[e7]` **khoản này** → `THAM_CHIEU_PHAP_LY` (span: `[69:71]`) *(lồng trong `e5` (`KHOAN`))*
- `[e8]` **quy định tại** → `TU_KHOA_PHAP_LY` (span: `[67:69]`) *(lồng trong `e5` (`KHOAN`))*
- `[e9]` **Hộ chiếu thuyền viên** → `GIAY_TO_HO_SO` (span: `[41:43]`) *(lồng trong `e5` (`KHOAN`))*
- `[e10]` **Hộ chiếu thuyền viên** → `GIAY_TO_HO_SO` (span: `[55:57]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Giao thông Vận tải `[LINH_VUC]`)
- (`e4` Điều 71 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`)
- (`e5` 3 . Trong thời hạn ba ( 03 ) ngày làm việc , kể từ ngày nhận đủ hồ sơ theo quy định , Cục Hàng hải Việt Nam thực hiện việc cấp Hộ chiếu thuyền viên theo mẫu tại Phụ lục III của Thông tư này . Trường hợp không cấp Hộ chiếu thuyền viên , Cục Hàng hải Việt Nam phải trả lời bằng văn bản trong thời hạn quy định tại khoản này và nêu rõ lý do . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 71 `[DIEU]`)
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Giao thông Vận tải `[LINH_VUC]`)
- (`e5` 3 . Trong thời hạn ba ( 03 ) ngày làm việc , kể từ ngày nhận đủ hồ sơ theo quy định , Cục Hàng hải Việt Nam thực hiện việc cấp Hộ chiếu thuyền viên theo mẫu tại Phụ lục III của Thông tư này . Trường hợp không cấp Hộ chiếu thuyền viên , Cục Hàng hải Việt Nam phải trả lời bằng văn bản trong thời hạn quy định tại khoản này và nêu rõ lý do . `[KHOAN]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Giao thông Vận tải `[LINH_VUC]`)
- (`e5` 3 . Trong thời hạn ba ( 03 ) ngày làm việc , kể từ ngày nhận đủ hồ sơ theo quy định , Cục Hàng hải Việt Nam thực hiện việc cấp Hộ chiếu thuyền viên theo mẫu tại Phụ lục III của Thông tư này . Trường hợp không cấp Hộ chiếu thuyền viên , Cục Hàng hải Việt Nam phải trả lời bằng văn bản trong thời hạn quy định tại khoản này và nêu rõ lý do . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e6` Phụ lục III `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e8` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e7` khoản này `[THAM_CHIEU_PHAP_LY]`)
- (`e5` 3 . Trong thời hạn ba ( 03 ) ngày làm việc , kể từ ngày nhận đủ hồ sơ theo quy định , Cục Hàng hải Việt Nam thực hiện việc cấp Hộ chiếu thuyền viên theo mẫu tại Phụ lục III của Thông tư này . Trường hợp không cấp Hộ chiếu thuyền viên , Cục Hàng hải Việt Nam phải trả lời bằng văn bản trong thời hạn quy định tại khoản này và nêu rõ lý do . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e7` khoản này `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #07_2012_TT-BGTVT_27433#body_standalone_75 (Loại: `body_standalone`)
> **[Điều 71]`<DIEU>`** . **[3 . Trong thời hạn ba ( 03 ) ngày làm việc , kể từ ngày nhận đủ hồ sơ theo quy định , Cục Hàng hải Việt Nam thực hiện việc cấp **[Hộ chiếu thuyền viên]`<GIAY_TO_HO_SO>`** theo mẫu tại **[Phụ lục III]`<THAM_CHIEU_PHAP_LY>`** của Thông tư này . Trường hợp không cấp **[Hộ chiếu thuyền viên]`<GIAY_TO_HO_SO>`** , Cục Hàng hải Việt Nam phải trả lời bằng văn bản trong thời hạn **[quy định tại]`<TU_KHOA_PHAP_LY>`** **[khoản này]`<THAM_CHIEU_PHAP_LY>`** và nêu rõ lý do .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 71** → `DIEU` (span: `[0:2]`)
- `[e1]` **3 . Trong thời hạn ba ( 03 ) ngày làm việc , kể từ ngày nhận đủ hồ sơ theo quy định , Cục Hàng hải Việt Nam thực hiện việc cấp Hộ chiếu thuyền viên theo mẫu tại Phụ lục III của Thông tư này . Trường hợp không cấp Hộ chiếu thuyền viên , Cục Hàng hải Việt Nam phải trả lời bằng văn bản trong thời hạn quy định tại khoản này và nêu rõ lý do .** → `KHOAN` (span: `[3:64]`)
- `[e2]` **Phụ lục III** → `THAM_CHIEU_PHAP_LY` (span: `[34:36]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **khoản này** → `THAM_CHIEU_PHAP_LY` (span: `[57:59]`) *(lồng trong `e1` (`KHOAN`))*
- `[e4]` **quy định tại** → `TU_KHOA_PHAP_LY` (span: `[55:57]`) *(lồng trong `e1` (`KHOAN`))*
- `[e5]` **Hộ chiếu thuyền viên** → `GIAY_TO_HO_SO` (span: `[29:31]`) *(lồng trong `e1` (`KHOAN`))*
- `[e6]` **Hộ chiếu thuyền viên** → `GIAY_TO_HO_SO` (span: `[43:45]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 3 . Trong thời hạn ba ( 03 ) ngày làm việc , kể từ ngày nhận đủ hồ sơ theo quy định , Cục Hàng hải Việt Nam thực hiện việc cấp Hộ chiếu thuyền viên theo mẫu tại Phụ lục III của Thông tư này . Trường hợp không cấp Hộ chiếu thuyền viên , Cục Hàng hải Việt Nam phải trả lời bằng văn bản trong thời hạn quy định tại khoản này và nêu rõ lý do . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 71 `[DIEU]`)
- (`e1` 3 . Trong thời hạn ba ( 03 ) ngày làm việc , kể từ ngày nhận đủ hồ sơ theo quy định , Cục Hàng hải Việt Nam thực hiện việc cấp Hộ chiếu thuyền viên theo mẫu tại Phụ lục III của Thông tư này . Trường hợp không cấp Hộ chiếu thuyền viên , Cục Hàng hải Việt Nam phải trả lời bằng văn bản trong thời hạn quy định tại khoản này và nêu rõ lý do . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e2` Phụ lục III `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e4` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` khoản này `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 3 . Trong thời hạn ba ( 03 ) ngày làm việc , kể từ ngày nhận đủ hồ sơ theo quy định , Cục Hàng hải Việt Nam thực hiện việc cấp Hộ chiếu thuyền viên theo mẫu tại Phụ lục III của Thông tư này . Trường hợp không cấp Hộ chiếu thuyền viên , Cục Hàng hải Việt Nam phải trả lời bằng văn bản trong thời hạn quy định tại khoản này và nêu rõ lý do . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` khoản này `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #07_2012_TT-BGTVT_27433#body_context_76 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[07/2012/TT-BGTVT]`<SO_HIEU>`** ban hành **[ngày 21 tháng 03 năm 2012]`<NGAY_BAN_HANH>`** bởi **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** . **[Điều 72]`<DIEU>`** . **[Khoản 2]`<KHOAN>`** . **[a ) **[Tờ khai đề nghị cấp lại Hộ chiếu thuyền viên]`<GIAY_TO_HO_SO>`** theo mẫu tại **[Phụ lục V]`<THAM_CHIEU_PHAP_LY>`** của Thông tư này ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **07/2012/TT-BGTVT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[11:14]`)
- `[e3]` **ngày 21 tháng 03 năm 2012** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 72** → `DIEU` (span: `[15:17]`)
- `[e5]` **Khoản 2** → `KHOAN` (span: `[18:20]`)
- `[e6]` **a ) Tờ khai đề nghị cấp lại Hộ chiếu thuyền viên theo mẫu tại Phụ lục V của Thông tư này ;** → `DIEM` (span: `[21:39]`)
- `[e7]` **Phụ lục V** → `THAM_CHIEU_PHAP_LY` (span: `[33:35]`) *(lồng trong `e6` (`DIEM`))*
- `[e8]` **Tờ khai đề nghị cấp lại Hộ chiếu thuyền viên** → `GIAY_TO_HO_SO` (span: `[23:30]`) *(lồng trong `e6` (`DIEM`))*

**Quan hệ:**
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 21 tháng 03 năm 2012 `[NGAY_BAN_HANH]`)
- (`e4` Điều 72 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`)
- (`e5` Khoản 2 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 72 `[DIEU]`)
- (`e6` a ) Tờ khai đề nghị cấp lại Hộ chiếu thuyền viên theo mẫu tại Phụ lục V của Thông tư này ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e5` Khoản 2 `[KHOAN]`)
- (`e6` a ) Tờ khai đề nghị cấp lại Hộ chiếu thuyền viên theo mẫu tại Phụ lục V của Thông tư này ; `[DIEM]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e7` Phụ lục V `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #07_2012_TT-BGTVT_27433#body_standalone_77 (Loại: `body_standalone`)
> **[Điều 72]`<DIEU>`** . **[Khoản 2]`<KHOAN>`** . **[a ) **[Tờ khai đề nghị cấp lại Hộ chiếu thuyền viên]`<GIAY_TO_HO_SO>`** theo mẫu tại **[Phụ lục V]`<THAM_CHIEU_PHAP_LY>`** của Thông tư này ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Điều 72** → `DIEU` (span: `[0:2]`)
- `[e1]` **Khoản 2** → `KHOAN` (span: `[3:5]`)
- `[e2]` **a ) Tờ khai đề nghị cấp lại Hộ chiếu thuyền viên theo mẫu tại Phụ lục V của Thông tư này ;** → `DIEM` (span: `[6:24]`)
- `[e3]` **Phụ lục V** → `THAM_CHIEU_PHAP_LY` (span: `[18:20]`) *(lồng trong `e2` (`DIEM`))*
- `[e4]` **Tờ khai đề nghị cấp lại Hộ chiếu thuyền viên** → `GIAY_TO_HO_SO` (span: `[8:15]`) *(lồng trong `e2` (`DIEM`))*

**Quan hệ:**
- (`e1` Khoản 2 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 72 `[DIEU]`)
- (`e2` a ) Tờ khai đề nghị cấp lại Hộ chiếu thuyền viên theo mẫu tại Phụ lục V của Thông tư này ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e1` Khoản 2 `[KHOAN]`)
- (`e2` a ) Tờ khai đề nghị cấp lại Hộ chiếu thuyền viên theo mẫu tại Phụ lục V của Thông tư này ; `[DIEM]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Phụ lục V `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #07_2012_TT-BGTVT_27433#body_context_78 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[07/2012/TT-BGTVT]`<SO_HIEU>`** của **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Giao thông Vận tải]`<LINH_VUC>`** . **[Điều 72]`<DIEU>`** . **[4 . Trong thời hạn ba ( 03 ) ngày làm việc , kể từ ngày nhận đủ hồ sơ theo quy định , Cục Hàng hải Việt Nam thực hiện việc cấp **[Hộ chiếu thuyền viên]`<GIAY_TO_HO_SO>`** theo mẫu **[quy định tại]`<TU_KHOA_PHAP_LY>`** **[Phụ lục III]`<THAM_CHIEU_PHAP_LY>`** của Thông tư này . Trường hợp không cấp lại **[Hộ chiếu thuyền viên]`<GIAY_TO_HO_SO>`** , Cục Hàng hải Việt Nam phải trả lời bằng văn bản trong thời hạn **[quy định tại]`<TU_KHOA_PHAP_LY>`** **[khoản này]`<THAM_CHIEU_PHAP_LY>`** và nêu rõ lý do .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **07/2012/TT-BGTVT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[4:7]`)
- `[e3]` **Giao thông Vận tải** → `LINH_VUC` (span: `[9:11]`)
- `[e4]` **Điều 72** → `DIEU` (span: `[12:14]`)
- `[e5]` **4 . Trong thời hạn ba ( 03 ) ngày làm việc , kể từ ngày nhận đủ hồ sơ theo quy định , Cục Hàng hải Việt Nam thực hiện việc cấp Hộ chiếu thuyền viên theo mẫu quy định tại Phụ lục III của Thông tư này . Trường hợp không cấp lại Hộ chiếu thuyền viên , Cục Hàng hải Việt Nam phải trả lời bằng văn bản trong thời hạn quy định tại khoản này và nêu rõ lý do .** → `KHOAN` (span: `[15:78]`)
- `[e6]` **Phụ lục III** → `THAM_CHIEU_PHAP_LY` (span: `[47:49]`) *(lồng trong `e5` (`KHOAN`))*
- `[e7]` **khoản này** → `THAM_CHIEU_PHAP_LY` (span: `[71:73]`) *(lồng trong `e5` (`KHOAN`))*
- `[e8]` **quy định tại** → `TU_KHOA_PHAP_LY` (span: `[45:47]`) *(lồng trong `e5` (`KHOAN`))*
- `[e9]` **quy định tại** → `TU_KHOA_PHAP_LY` (span: `[69:71]`) *(lồng trong `e5` (`KHOAN`))*
- `[e10]` **Hộ chiếu thuyền viên** → `GIAY_TO_HO_SO` (span: `[41:43]`) *(lồng trong `e5` (`KHOAN`))*
- `[e11]` **Hộ chiếu thuyền viên** → `GIAY_TO_HO_SO` (span: `[57:59]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Giao thông Vận tải `[LINH_VUC]`)
- (`e4` Điều 72 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`)
- (`e5` 4 . Trong thời hạn ba ( 03 ) ngày làm việc , kể từ ngày nhận đủ hồ sơ theo quy định , Cục Hàng hải Việt Nam thực hiện việc cấp Hộ chiếu thuyền viên theo mẫu quy định tại Phụ lục III của Thông tư này . Trường hợp không cấp lại Hộ chiếu thuyền viên , Cục Hàng hải Việt Nam phải trả lời bằng văn bản trong thời hạn quy định tại khoản này và nêu rõ lý do . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 72 `[DIEU]`)
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Giao thông Vận tải `[LINH_VUC]`)
- (`e5` 4 . Trong thời hạn ba ( 03 ) ngày làm việc , kể từ ngày nhận đủ hồ sơ theo quy định , Cục Hàng hải Việt Nam thực hiện việc cấp Hộ chiếu thuyền viên theo mẫu quy định tại Phụ lục III của Thông tư này . Trường hợp không cấp lại Hộ chiếu thuyền viên , Cục Hàng hải Việt Nam phải trả lời bằng văn bản trong thời hạn quy định tại khoản này và nêu rõ lý do . `[KHOAN]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Giao thông Vận tải `[LINH_VUC]`)
- (`e8` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e6` Phụ lục III `[THAM_CHIEU_PHAP_LY]`)
- (`e5` 4 . Trong thời hạn ba ( 03 ) ngày làm việc , kể từ ngày nhận đủ hồ sơ theo quy định , Cục Hàng hải Việt Nam thực hiện việc cấp Hộ chiếu thuyền viên theo mẫu quy định tại Phụ lục III của Thông tư này . Trường hợp không cấp lại Hộ chiếu thuyền viên , Cục Hàng hải Việt Nam phải trả lời bằng văn bản trong thời hạn quy định tại khoản này và nêu rõ lý do . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e6` Phụ lục III `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e9` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e7` khoản này `[THAM_CHIEU_PHAP_LY]`)
- (`e5` 4 . Trong thời hạn ba ( 03 ) ngày làm việc , kể từ ngày nhận đủ hồ sơ theo quy định , Cục Hàng hải Việt Nam thực hiện việc cấp Hộ chiếu thuyền viên theo mẫu quy định tại Phụ lục III của Thông tư này . Trường hợp không cấp lại Hộ chiếu thuyền viên , Cục Hàng hải Việt Nam phải trả lời bằng văn bản trong thời hạn quy định tại khoản này và nêu rõ lý do . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e7` khoản này `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #07_2012_TT-BGTVT_27433#body_standalone_79 (Loại: `body_standalone`)
> **[Điều 72]`<DIEU>`** . **[4 . Trong thời hạn ba ( 03 ) ngày làm việc , kể từ ngày nhận đủ hồ sơ theo quy định , Cục Hàng hải Việt Nam thực hiện việc cấp **[Hộ chiếu thuyền viên]`<GIAY_TO_HO_SO>`** theo mẫu **[quy định tại]`<TU_KHOA_PHAP_LY>`** **[Phụ lục III]`<THAM_CHIEU_PHAP_LY>`** của Thông tư này . Trường hợp không cấp lại **[Hộ chiếu thuyền viên]`<GIAY_TO_HO_SO>`** , Cục Hàng hải Việt Nam phải trả lời bằng văn bản trong thời hạn **[quy định tại]`<TU_KHOA_PHAP_LY>`** **[khoản này]`<THAM_CHIEU_PHAP_LY>`** và nêu rõ lý do .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 72** → `DIEU` (span: `[0:2]`)
- `[e1]` **4 . Trong thời hạn ba ( 03 ) ngày làm việc , kể từ ngày nhận đủ hồ sơ theo quy định , Cục Hàng hải Việt Nam thực hiện việc cấp Hộ chiếu thuyền viên theo mẫu quy định tại Phụ lục III của Thông tư này . Trường hợp không cấp lại Hộ chiếu thuyền viên , Cục Hàng hải Việt Nam phải trả lời bằng văn bản trong thời hạn quy định tại khoản này và nêu rõ lý do .** → `KHOAN` (span: `[3:66]`)
- `[e2]` **Phụ lục III** → `THAM_CHIEU_PHAP_LY` (span: `[35:37]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **khoản này** → `THAM_CHIEU_PHAP_LY` (span: `[59:61]`) *(lồng trong `e1` (`KHOAN`))*
- `[e4]` **quy định tại** → `TU_KHOA_PHAP_LY` (span: `[33:35]`) *(lồng trong `e1` (`KHOAN`))*
- `[e5]` **quy định tại** → `TU_KHOA_PHAP_LY` (span: `[57:59]`) *(lồng trong `e1` (`KHOAN`))*
- `[e6]` **Hộ chiếu thuyền viên** → `GIAY_TO_HO_SO` (span: `[29:31]`) *(lồng trong `e1` (`KHOAN`))*
- `[e7]` **Hộ chiếu thuyền viên** → `GIAY_TO_HO_SO` (span: `[45:47]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 4 . Trong thời hạn ba ( 03 ) ngày làm việc , kể từ ngày nhận đủ hồ sơ theo quy định , Cục Hàng hải Việt Nam thực hiện việc cấp Hộ chiếu thuyền viên theo mẫu quy định tại Phụ lục III của Thông tư này . Trường hợp không cấp lại Hộ chiếu thuyền viên , Cục Hàng hải Việt Nam phải trả lời bằng văn bản trong thời hạn quy định tại khoản này và nêu rõ lý do . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 72 `[DIEU]`)
- (`e4` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e2` Phụ lục III `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 4 . Trong thời hạn ba ( 03 ) ngày làm việc , kể từ ngày nhận đủ hồ sơ theo quy định , Cục Hàng hải Việt Nam thực hiện việc cấp Hộ chiếu thuyền viên theo mẫu quy định tại Phụ lục III của Thông tư này . Trường hợp không cấp lại Hộ chiếu thuyền viên , Cục Hàng hải Việt Nam phải trả lời bằng văn bản trong thời hạn quy định tại khoản này và nêu rõ lý do . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e2` Phụ lục III `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e5` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` khoản này `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 4 . Trong thời hạn ba ( 03 ) ngày làm việc , kể từ ngày nhận đủ hồ sơ theo quy định , Cục Hàng hải Việt Nam thực hiện việc cấp Hộ chiếu thuyền viên theo mẫu quy định tại Phụ lục III của Thông tư này . Trường hợp không cấp lại Hộ chiếu thuyền viên , Cục Hàng hải Việt Nam phải trả lời bằng văn bản trong thời hạn quy định tại khoản này và nêu rõ lý do . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` khoản này `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #07_2012_TT-BGTVT_27433#body_context_80 (Loại: `body_context`)
> **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[07/2012/TT-BGTVT]`<SO_HIEU>`** . **[Điều 74]`<DIEU>`** . **[1 . Thông tư này có hiệu lực thi hành kể từ ngày 20 tháng 5 năm 2012 và thay thế **[Quyết định số 29/2008/QĐ-BGTVT]`<THAM_CHIEU_PHAP_LY>`** **[ngày 16 tháng 12 năm 2008]`<NGAY_THAM_CHIEU>`** của **[Bộ trưởng Bộ Giao thông vận tải]`<CO_QUAN_THAM_QUYEN>`** về chức danh , nhiệm vụ theo chức danh của thuyền viên và đăng ký thuyền viên làm việc trên **[tàu biển]`<TAI_SAN_VAT_CHAT>`** Việt Nam .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[4:5]`)
- `[e1]` **07/2012/TT-BGTVT** → `SO_HIEU` (span: `[6:7]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[0:3]`)
- `[e3]` **Điều 74** → `DIEU` (span: `[8:10]`)
- `[e4]` **1 . Thông tư này có hiệu lực thi hành kể từ ngày 20 tháng 5 năm 2012 và thay thế Quyết định số 29/2008/QĐ-BGTVT ngày 16 tháng 12 năm 2008 của Bộ trưởng Bộ Giao thông vận tải về chức danh , nhiệm vụ theo chức danh của thuyền viên và đăng ký thuyền viên làm việc trên tàu biển Việt Nam .** → `KHOAN` (span: `[11:58]`)
- `[e5]` **Quyết định số 29/2008/QĐ-BGTVT** → `THAM_CHIEU_PHAP_LY` (span: `[28:31]`) *(lồng trong `e4` (`KHOAN`))*
- `[e6]` **ngày 16 tháng 12 năm 2008** → `NGAY_THAM_CHIEU` (span: `[31:37]`) *(lồng trong `e4` (`KHOAN`))*
- `[e7]` **Bộ trưởng Bộ Giao thông vận tải** → `CO_QUAN_THAM_QUYEN` (span: `[38:42]`) *(lồng trong `e4` (`KHOAN`))*
- `[e8]` **tàu biển** → `TAI_SAN_VAT_CHAT` (span: `[55:56]`) *(lồng trong `e4` (`KHOAN`))*

**Quan hệ:**
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 74 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`)
- (`e4` 1 . Thông tư này có hiệu lực thi hành kể từ ngày 20 tháng 5 năm 2012 và thay thế Quyết định số 29/2008/QĐ-BGTVT ngày 16 tháng 12 năm 2008 của Bộ trưởng Bộ Giao thông vận tải về chức danh , nhiệm vụ theo chức danh của thuyền viên và đăng ký thuyền viên làm việc trên tàu biển Việt Nam . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 74 `[DIEU]`)
- (`e4` 1 . Thông tư này có hiệu lực thi hành kể từ ngày 20 tháng 5 năm 2012 và thay thế Quyết định số 29/2008/QĐ-BGTVT ngày 16 tháng 12 năm 2008 của Bộ trưởng Bộ Giao thông vận tải về chức danh , nhiệm vụ theo chức danh của thuyền viên và đăng ký thuyền viên làm việc trên tàu biển Việt Nam . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e5` Quyết định số 29/2008/QĐ-BGTVT `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e5` Quyết định số 29/2008/QĐ-BGTVT `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e6` ngày 16 tháng 12 năm 2008 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #07_2012_TT-BGTVT_27433#body_standalone_81 (Loại: `body_standalone`)
> **[Điều 74]`<DIEU>`** . **[1 . Thông tư này có hiệu lực thi hành kể từ ngày 20 tháng 5 năm 2012 và thay thế **[Quyết định số 29/2008/QĐ-BGTVT]`<THAM_CHIEU_PHAP_LY>`** **[ngày 16 tháng 12 năm 2008]`<NGAY_THAM_CHIEU>`** của **[Bộ trưởng Bộ Giao thông vận tải]`<CO_QUAN_THAM_QUYEN>`** về chức danh , nhiệm vụ theo chức danh của thuyền viên và đăng ký thuyền viên làm việc trên **[tàu biển]`<TAI_SAN_VAT_CHAT>`** Việt Nam .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 74** → `DIEU` (span: `[0:2]`)
- `[e1]` **1 . Thông tư này có hiệu lực thi hành kể từ ngày 20 tháng 5 năm 2012 và thay thế Quyết định số 29/2008/QĐ-BGTVT ngày 16 tháng 12 năm 2008 của Bộ trưởng Bộ Giao thông vận tải về chức danh , nhiệm vụ theo chức danh của thuyền viên và đăng ký thuyền viên làm việc trên tàu biển Việt Nam .** → `KHOAN` (span: `[3:50]`)
- `[e2]` **Quyết định số 29/2008/QĐ-BGTVT** → `THAM_CHIEU_PHAP_LY` (span: `[20:23]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **ngày 16 tháng 12 năm 2008** → `NGAY_THAM_CHIEU` (span: `[23:29]`) *(lồng trong `e1` (`KHOAN`))*
- `[e4]` **Bộ trưởng Bộ Giao thông vận tải** → `CO_QUAN_THAM_QUYEN` (span: `[30:34]`) *(lồng trong `e1` (`KHOAN`))*
- `[e5]` **tàu biển** → `TAI_SAN_VAT_CHAT` (span: `[47:48]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 1 . Thông tư này có hiệu lực thi hành kể từ ngày 20 tháng 5 năm 2012 và thay thế Quyết định số 29/2008/QĐ-BGTVT ngày 16 tháng 12 năm 2008 của Bộ trưởng Bộ Giao thông vận tải về chức danh , nhiệm vụ theo chức danh của thuyền viên và đăng ký thuyền viên làm việc trên tàu biển Việt Nam . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 74 `[DIEU]`)
- (`e1` 1 . Thông tư này có hiệu lực thi hành kể từ ngày 20 tháng 5 năm 2012 và thay thế Quyết định số 29/2008/QĐ-BGTVT ngày 16 tháng 12 năm 2008 của Bộ trưởng Bộ Giao thông vận tải về chức danh , nhiệm vụ theo chức danh của thuyền viên và đăng ký thuyền viên làm việc trên tàu biển Việt Nam . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e2` Quyết định số 29/2008/QĐ-BGTVT `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e2` Quyết định số 29/2008/QĐ-BGTVT `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e3` ngày 16 tháng 12 năm 2008 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #07_2012_TT-BGTVT_27433#body_context_82 (Loại: `body_context`)
> **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[07/2012/TT-BGTVT]`<SO_HIEU>`** . **[Điều 74]`<DIEU>`** . **[Khoản 2]`<KHOAN>`** . **[a ) **[Phụ lục I]`<THAM_CHIEU_PHAP_LY>`** : mẫu **[Sổ thuyền viên]`<GIAY_TO_HO_SO>`** ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[4:5]`)
- `[e1]` **07/2012/TT-BGTVT** → `SO_HIEU` (span: `[6:7]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[0:3]`)
- `[e3]` **Điều 74** → `DIEU` (span: `[8:10]`)
- `[e4]` **Khoản 2** → `KHOAN` (span: `[11:13]`)
- `[e5]` **a ) Phụ lục I : mẫu Sổ thuyền viên ;** → `DIEM` (span: `[14:23]`)
- `[e6]` **Phụ lục I** → `THAM_CHIEU_PHAP_LY` (span: `[16:18]`) *(lồng trong `e5` (`DIEM`))*
- `[e7]` **Sổ thuyền viên** → `GIAY_TO_HO_SO` (span: `[20:22]`) *(lồng trong `e5` (`DIEM`))*

**Quan hệ:**
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 74 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`)
- (`e4` Khoản 2 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 74 `[DIEU]`)
- (`e5` a ) Phụ lục I : mẫu Sổ thuyền viên ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e4` Khoản 2 `[KHOAN]`)
- (`e5` a ) Phụ lục I : mẫu Sổ thuyền viên ; `[DIEM]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e6` Phụ lục I `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #07_2012_TT-BGTVT_27433#body_standalone_83 (Loại: `body_standalone`)
> **[Điều 74]`<DIEU>`** . **[Khoản 2]`<KHOAN>`** . **[a ) **[Phụ lục I]`<THAM_CHIEU_PHAP_LY>`** : mẫu **[Sổ thuyền viên]`<GIAY_TO_HO_SO>`** ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Điều 74** → `DIEU` (span: `[0:2]`)
- `[e1]` **Khoản 2** → `KHOAN` (span: `[3:5]`)
- `[e2]` **a ) Phụ lục I : mẫu Sổ thuyền viên ;** → `DIEM` (span: `[6:15]`)
- `[e3]` **Phụ lục I** → `THAM_CHIEU_PHAP_LY` (span: `[8:10]`) *(lồng trong `e2` (`DIEM`))*
- `[e4]` **Sổ thuyền viên** → `GIAY_TO_HO_SO` (span: `[12:14]`) *(lồng trong `e2` (`DIEM`))*

**Quan hệ:**
- (`e1` Khoản 2 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 74 `[DIEU]`)
- (`e2` a ) Phụ lục I : mẫu Sổ thuyền viên ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e1` Khoản 2 `[KHOAN]`)
- (`e2` a ) Phụ lục I : mẫu Sổ thuyền viên ; `[DIEM]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Phụ lục I `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #07_2012_TT-BGTVT_27433#body_context_84 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[07/2012/TT-BGTVT]`<SO_HIEU>`** của **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Giao thông Vận tải]`<LINH_VUC>`** . **[Điều 74]`<DIEU>`** . **[Khoản 2]`<KHOAN>`** . **[b ) **[Phụ lục II]`<THAM_CHIEU_PHAP_LY>`** : mẫu **[Tờ khai đề nghị cấp Sổ thuyền viên]`<GIAY_TO_HO_SO>`** ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **07/2012/TT-BGTVT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[4:7]`)
- `[e3]` **Giao thông Vận tải** → `LINH_VUC` (span: `[9:11]`)
- `[e4]` **Điều 74** → `DIEU` (span: `[12:14]`)
- `[e5]` **Khoản 2** → `KHOAN` (span: `[15:17]`)
- `[e6]` **b ) Phụ lục II : mẫu Tờ khai đề nghị cấp Sổ thuyền viên ;** → `DIEM` (span: `[18:31]`)
- `[e7]` **Phụ lục II** → `THAM_CHIEU_PHAP_LY` (span: `[20:22]`) *(lồng trong `e6` (`DIEM`))*
- `[e8]` **Tờ khai đề nghị cấp Sổ thuyền viên** → `GIAY_TO_HO_SO` (span: `[24:30]`) *(lồng trong `e6` (`DIEM`))*

**Quan hệ:**
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Giao thông Vận tải `[LINH_VUC]`)
- (`e4` Điều 74 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`)
- (`e5` Khoản 2 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 74 `[DIEU]`)
- (`e6` b ) Phụ lục II : mẫu Tờ khai đề nghị cấp Sổ thuyền viên ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e5` Khoản 2 `[KHOAN]`)
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Giao thông Vận tải `[LINH_VUC]`)
- (`e6` b ) Phụ lục II : mẫu Tờ khai đề nghị cấp Sổ thuyền viên ; `[DIEM]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Giao thông Vận tải `[LINH_VUC]`)
- (`e6` b ) Phụ lục II : mẫu Tờ khai đề nghị cấp Sổ thuyền viên ; `[DIEM]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e7` Phụ lục II `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #07_2012_TT-BGTVT_27433#body_standalone_85 (Loại: `body_standalone`)
> **[Điều 74]`<DIEU>`** . **[Khoản 2]`<KHOAN>`** . **[b ) **[Phụ lục II]`<THAM_CHIEU_PHAP_LY>`** : mẫu **[Tờ khai đề nghị cấp Sổ thuyền viên]`<GIAY_TO_HO_SO>`** ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Điều 74** → `DIEU` (span: `[0:2]`)
- `[e1]` **Khoản 2** → `KHOAN` (span: `[3:5]`)
- `[e2]` **b ) Phụ lục II : mẫu Tờ khai đề nghị cấp Sổ thuyền viên ;** → `DIEM` (span: `[6:19]`)
- `[e3]` **Phụ lục II** → `THAM_CHIEU_PHAP_LY` (span: `[8:10]`) *(lồng trong `e2` (`DIEM`))*
- `[e4]` **Tờ khai đề nghị cấp Sổ thuyền viên** → `GIAY_TO_HO_SO` (span: `[12:18]`) *(lồng trong `e2` (`DIEM`))*

**Quan hệ:**
- (`e1` Khoản 2 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 74 `[DIEU]`)
- (`e2` b ) Phụ lục II : mẫu Tờ khai đề nghị cấp Sổ thuyền viên ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e1` Khoản 2 `[KHOAN]`)
- (`e2` b ) Phụ lục II : mẫu Tờ khai đề nghị cấp Sổ thuyền viên ; `[DIEM]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Phụ lục II `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #07_2012_TT-BGTVT_27433#body_context_86 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[07/2012/TT-BGTVT]`<SO_HIEU>`** của **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Giao thông Vận tải]`<LINH_VUC>`** . **[Điều 74]`<DIEU>`** . **[Khoản 2]`<KHOAN>`** . **[c ) **[Phụ lục III]`<THAM_CHIEU_PHAP_LY>`** : mẫu **[Hộ chiếu thuyền viên]`<GIAY_TO_HO_SO>`** ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **07/2012/TT-BGTVT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[4:7]`)
- `[e3]` **Giao thông Vận tải** → `LINH_VUC` (span: `[9:11]`)
- `[e4]` **Điều 74** → `DIEU` (span: `[12:14]`)
- `[e5]` **Khoản 2** → `KHOAN` (span: `[15:17]`)
- `[e6]` **c ) Phụ lục III : mẫu Hộ chiếu thuyền viên ;** → `DIEM` (span: `[18:27]`)
- `[e7]` **Phụ lục III** → `THAM_CHIEU_PHAP_LY` (span: `[20:22]`) *(lồng trong `e6` (`DIEM`))*
- `[e8]` **Hộ chiếu thuyền viên** → `GIAY_TO_HO_SO` (span: `[24:26]`) *(lồng trong `e6` (`DIEM`))*

**Quan hệ:**
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Giao thông Vận tải `[LINH_VUC]`)
- (`e4` Điều 74 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`)
- (`e5` Khoản 2 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 74 `[DIEU]`)
- (`e6` c ) Phụ lục III : mẫu Hộ chiếu thuyền viên ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e5` Khoản 2 `[KHOAN]`)
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Giao thông Vận tải `[LINH_VUC]`)
- (`e6` c ) Phụ lục III : mẫu Hộ chiếu thuyền viên ; `[DIEM]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Giao thông Vận tải `[LINH_VUC]`)
- (`e6` c ) Phụ lục III : mẫu Hộ chiếu thuyền viên ; `[DIEM]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e7` Phụ lục III `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #07_2012_TT-BGTVT_27433#body_standalone_87 (Loại: `body_standalone`)
> **[Điều 74]`<DIEU>`** . **[Khoản 2]`<KHOAN>`** . **[c ) **[Phụ lục III]`<THAM_CHIEU_PHAP_LY>`** : mẫu **[Hộ chiếu thuyền viên]`<GIAY_TO_HO_SO>`** ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Điều 74** → `DIEU` (span: `[0:2]`)
- `[e1]` **Khoản 2** → `KHOAN` (span: `[3:5]`)
- `[e2]` **c ) Phụ lục III : mẫu Hộ chiếu thuyền viên ;** → `DIEM` (span: `[6:15]`)
- `[e3]` **Phụ lục III** → `THAM_CHIEU_PHAP_LY` (span: `[8:10]`) *(lồng trong `e2` (`DIEM`))*
- `[e4]` **Hộ chiếu thuyền viên** → `GIAY_TO_HO_SO` (span: `[12:14]`) *(lồng trong `e2` (`DIEM`))*

**Quan hệ:**
- (`e1` Khoản 2 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 74 `[DIEU]`)
- (`e2` c ) Phụ lục III : mẫu Hộ chiếu thuyền viên ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e1` Khoản 2 `[KHOAN]`)
- (`e2` c ) Phụ lục III : mẫu Hộ chiếu thuyền viên ; `[DIEM]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Phụ lục III `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #07_2012_TT-BGTVT_27433#body_context_88 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[07/2012/TT-BGTVT]`<SO_HIEU>`** của **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Giao thông Vận tải]`<LINH_VUC>`** . **[Điều 74]`<DIEU>`** . **[Khoản 2]`<KHOAN>`** . **[d ) **[Phụ lục IV]`<THAM_CHIEU_PHAP_LY>`** : mẫu **[Tờ khai đề nghị cấp Hộ chiếu thuyền viên]`<GIAY_TO_HO_SO>`** ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **07/2012/TT-BGTVT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[4:7]`)
- `[e3]` **Giao thông Vận tải** → `LINH_VUC` (span: `[9:11]`)
- `[e4]` **Điều 74** → `DIEU` (span: `[12:14]`)
- `[e5]` **Khoản 2** → `KHOAN` (span: `[15:17]`)
- `[e6]` **d ) Phụ lục IV : mẫu Tờ khai đề nghị cấp Hộ chiếu thuyền viên ;** → `DIEM` (span: `[18:31]`)
- `[e7]` **Phụ lục IV** → `THAM_CHIEU_PHAP_LY` (span: `[20:22]`) *(lồng trong `e6` (`DIEM`))*
- `[e8]` **Tờ khai đề nghị cấp Hộ chiếu thuyền viên** → `GIAY_TO_HO_SO` (span: `[24:30]`) *(lồng trong `e6` (`DIEM`))*

**Quan hệ:**
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Giao thông Vận tải `[LINH_VUC]`)
- (`e4` Điều 74 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`)
- (`e5` Khoản 2 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 74 `[DIEU]`)
- (`e6` d ) Phụ lục IV : mẫu Tờ khai đề nghị cấp Hộ chiếu thuyền viên ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e5` Khoản 2 `[KHOAN]`)
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Giao thông Vận tải `[LINH_VUC]`)
- (`e6` d ) Phụ lục IV : mẫu Tờ khai đề nghị cấp Hộ chiếu thuyền viên ; `[DIEM]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Giao thông Vận tải `[LINH_VUC]`)
- (`e6` d ) Phụ lục IV : mẫu Tờ khai đề nghị cấp Hộ chiếu thuyền viên ; `[DIEM]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e7` Phụ lục IV `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #07_2012_TT-BGTVT_27433#body_standalone_89 (Loại: `body_standalone`)
> **[Điều 74]`<DIEU>`** . **[Khoản 2]`<KHOAN>`** . **[d ) **[Phụ lục IV]`<THAM_CHIEU_PHAP_LY>`** : mẫu **[Tờ khai đề nghị cấp Hộ chiếu thuyền viên]`<GIAY_TO_HO_SO>`** ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Điều 74** → `DIEU` (span: `[0:2]`)
- `[e1]` **Khoản 2** → `KHOAN` (span: `[3:5]`)
- `[e2]` **d ) Phụ lục IV : mẫu Tờ khai đề nghị cấp Hộ chiếu thuyền viên ;** → `DIEM` (span: `[6:19]`)
- `[e3]` **Phụ lục IV** → `THAM_CHIEU_PHAP_LY` (span: `[8:10]`) *(lồng trong `e2` (`DIEM`))*
- `[e4]` **Tờ khai đề nghị cấp Hộ chiếu thuyền viên** → `GIAY_TO_HO_SO` (span: `[12:18]`) *(lồng trong `e2` (`DIEM`))*

**Quan hệ:**
- (`e1` Khoản 2 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 74 `[DIEU]`)
- (`e2` d ) Phụ lục IV : mẫu Tờ khai đề nghị cấp Hộ chiếu thuyền viên ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e1` Khoản 2 `[KHOAN]`)
- (`e2` d ) Phụ lục IV : mẫu Tờ khai đề nghị cấp Hộ chiếu thuyền viên ; `[DIEM]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Phụ lục IV `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #07_2012_TT-BGTVT_27433#body_context_90 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[07/2012/TT-BGTVT]`<SO_HIEU>`** của **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Giao thông Vận tải]`<LINH_VUC>`** . **[Điều 74]`<DIEU>`** . **[Khoản 2]`<KHOAN>`** . **[đ ) **[Phụ lục V]`<THAM_CHIEU_PHAP_LY>`** : mẫu **[Tờ khai đề nghị cấp lại Hộ chiếu thuyền viên]`<GIAY_TO_HO_SO>`** .]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **07/2012/TT-BGTVT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[4:7]`)
- `[e3]` **Giao thông Vận tải** → `LINH_VUC` (span: `[9:11]`)
- `[e4]` **Điều 74** → `DIEU` (span: `[12:14]`)
- `[e5]` **Khoản 2** → `KHOAN` (span: `[15:17]`)
- `[e6]` **đ ) Phụ lục V : mẫu Tờ khai đề nghị cấp lại Hộ chiếu thuyền viên .** → `DIEM` (span: `[18:32]`)
- `[e7]` **Phụ lục V** → `THAM_CHIEU_PHAP_LY` (span: `[20:22]`) *(lồng trong `e6` (`DIEM`))*
- `[e8]` **Tờ khai đề nghị cấp lại Hộ chiếu thuyền viên** → `GIAY_TO_HO_SO` (span: `[24:31]`) *(lồng trong `e6` (`DIEM`))*

**Quan hệ:**
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Giao thông Vận tải `[LINH_VUC]`)
- (`e4` Điều 74 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`)
- (`e5` Khoản 2 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 74 `[DIEU]`)
- (`e6` đ ) Phụ lục V : mẫu Tờ khai đề nghị cấp lại Hộ chiếu thuyền viên . `[DIEM]`) ==[ **THUOC_VE** ]==> (`e5` Khoản 2 `[KHOAN]`)
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Giao thông Vận tải `[LINH_VUC]`)
- (`e6` đ ) Phụ lục V : mẫu Tờ khai đề nghị cấp lại Hộ chiếu thuyền viên . `[DIEM]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Giao thông Vận tải `[LINH_VUC]`)
- (`e6` đ ) Phụ lục V : mẫu Tờ khai đề nghị cấp lại Hộ chiếu thuyền viên . `[DIEM]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e7` Phụ lục V `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #07_2012_TT-BGTVT_27433#body_standalone_91 (Loại: `body_standalone`)
> **[Điều 74]`<DIEU>`** . **[Khoản 2]`<KHOAN>`** . **[đ ) **[Phụ lục V]`<THAM_CHIEU_PHAP_LY>`** : mẫu **[Tờ khai đề nghị cấp lại Hộ chiếu thuyền viên]`<GIAY_TO_HO_SO>`** .]`<DIEM>`**

**Thực thể:**
- `[e0]` **Điều 74** → `DIEU` (span: `[0:2]`)
- `[e1]` **Khoản 2** → `KHOAN` (span: `[3:5]`)
- `[e2]` **đ ) Phụ lục V : mẫu Tờ khai đề nghị cấp lại Hộ chiếu thuyền viên .** → `DIEM` (span: `[6:20]`)
- `[e3]` **Phụ lục V** → `THAM_CHIEU_PHAP_LY` (span: `[8:10]`) *(lồng trong `e2` (`DIEM`))*
- `[e4]` **Tờ khai đề nghị cấp lại Hộ chiếu thuyền viên** → `GIAY_TO_HO_SO` (span: `[12:19]`) *(lồng trong `e2` (`DIEM`))*

**Quan hệ:**
- (`e1` Khoản 2 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 74 `[DIEU]`)
- (`e2` đ ) Phụ lục V : mẫu Tờ khai đề nghị cấp lại Hộ chiếu thuyền viên . `[DIEM]`) ==[ **THUOC_VE** ]==> (`e1` Khoản 2 `[KHOAN]`)
- (`e2` đ ) Phụ lục V : mẫu Tờ khai đề nghị cấp lại Hộ chiếu thuyền viên . `[DIEM]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Phụ lục V `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #07_2012_TT-BGTVT_27433#body_context_92 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[07/2012/TT-BGTVT]`<SO_HIEU>`** của **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Giao thông Vận tải]`<LINH_VUC>`** . **[Điều 74]`<DIEU>`** . **[3 . **[Hộ chiếu thuyền viên]`<GIAY_TO_HO_SO>`** đã cấp theo **[Quyết định số 65/2005/QĐ-BGTVT]`<THAM_CHIEU_PHAP_LY>`** **[ngày 30 tháng 11 năm 2005]`<NGAY_THAM_CHIEU>`** của **[Bộ trưởng Bộ Giao thông vận tải]`<CO_QUAN_THAM_QUYEN>`** về chức danh , nhiệm vụ theo chức danh của thuyền viên và đăng ký thuyền viên làm việc trên **[tàu biển]`<TAI_SAN_VAT_CHAT>`** Việt Nam và **[Quyết định số 29/2008/QĐ-BGTVT]`<THAM_CHIEU_PHAP_LY>`** **[ngày 16 tháng 12 năm 2008]`<NGAY_THAM_CHIEU>`** của **[Bộ trưởng Bộ Giao thông vận tải]`<CO_QUAN_THAM_QUYEN>`** về chức danh , nhiệm vụ theo chức danh của thuyền viên và đăng ký thuyền viên làm việc trên **[tàu biển]`<TAI_SAN_VAT_CHAT>`** Việt Nam còn]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **07/2012/TT-BGTVT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[4:7]`)
- `[e3]` **Giao thông Vận tải** → `LINH_VUC` (span: `[9:11]`)
- `[e4]` **Điều 74** → `DIEU` (span: `[12:14]`)
- `[e5]` **3 . Hộ chiếu thuyền viên đã cấp theo Quyết định số 65/2005/QĐ-BGTVT ngày 30 tháng 11 năm 2005 của Bộ trưởng Bộ Giao thông vận tải về chức danh , nhiệm vụ theo chức danh của thuyền viên và đăng ký thuyền viên làm việc trên tàu biển Việt Nam và Quyết định số 29/2008/QĐ-BGTVT ngày 16 tháng 12 năm 2008 của Bộ trưởng Bộ Giao thông vận tải về chức danh , nhiệm vụ theo chức danh của thuyền viên và đăng ký thuyền viên làm việc trên tàu biển Việt Nam còn** → `KHOAN` (span: `[15:81]`)
- `[e6]` **Quyết định số 65/2005/QĐ-BGTVT** → `THAM_CHIEU_PHAP_LY` (span: `[22:25]`) *(lồng trong `e5` (`KHOAN`))*
- `[e7]` **Quyết định số 29/2008/QĐ-BGTVT** → `THAM_CHIEU_PHAP_LY` (span: `[52:55]`) *(lồng trong `e5` (`KHOAN`))*
- `[e8]` **ngày 30 tháng 11 năm 2005** → `NGAY_THAM_CHIEU` (span: `[25:31]`) *(lồng trong `e5` (`KHOAN`))*
- `[e9]` **ngày 16 tháng 12 năm 2008** → `NGAY_THAM_CHIEU` (span: `[55:61]`) *(lồng trong `e5` (`KHOAN`))*
- `[e10]` **Bộ trưởng Bộ Giao thông vận tải** → `CO_QUAN_THAM_QUYEN` (span: `[32:36]`) *(lồng trong `e5` (`KHOAN`))*
- `[e11]` **Bộ trưởng Bộ Giao thông vận tải** → `CO_QUAN_THAM_QUYEN` (span: `[62:66]`) *(lồng trong `e5` (`KHOAN`))*
- `[e12]` **Hộ chiếu thuyền viên** → `GIAY_TO_HO_SO` (span: `[17:19]`) *(lồng trong `e5` (`KHOAN`))*
- `[e13]` **tàu biển** → `TAI_SAN_VAT_CHAT` (span: `[49:50]`) *(lồng trong `e5` (`KHOAN`))*
- `[e14]` **tàu biển** → `TAI_SAN_VAT_CHAT` (span: `[79:80]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Giao thông Vận tải `[LINH_VUC]`)
- (`e4` Điều 74 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`)
- (`e5` 3 . Hộ chiếu thuyền viên đã cấp theo Quyết định số 65/2005/QĐ-BGTVT ngày 30 tháng 11 năm 2005 của Bộ trưởng Bộ Giao thông vận tải về chức danh , nhiệm vụ theo chức danh của thuyền viên và đăng ký thuyền viên làm việc trên tàu biển Việt Nam và Quyết định số 29/2008/QĐ-BGTVT ngày 16 tháng 12 năm 2008 của Bộ trưởng Bộ Giao thông vận tải về chức danh , nhiệm vụ theo chức danh của thuyền viên và đăng ký thuyền viên làm việc trên tàu biển Việt Nam còn `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 74 `[DIEU]`)
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Giao thông Vận tải `[LINH_VUC]`)
- (`e5` 3 . Hộ chiếu thuyền viên đã cấp theo Quyết định số 65/2005/QĐ-BGTVT ngày 30 tháng 11 năm 2005 của Bộ trưởng Bộ Giao thông vận tải về chức danh , nhiệm vụ theo chức danh của thuyền viên và đăng ký thuyền viên làm việc trên tàu biển Việt Nam và Quyết định số 29/2008/QĐ-BGTVT ngày 16 tháng 12 năm 2008 của Bộ trưởng Bộ Giao thông vận tải về chức danh , nhiệm vụ theo chức danh của thuyền viên và đăng ký thuyền viên làm việc trên tàu biển Việt Nam còn `[KHOAN]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Giao thông Vận tải `[LINH_VUC]`)
- (`e5` 3 . Hộ chiếu thuyền viên đã cấp theo Quyết định số 65/2005/QĐ-BGTVT ngày 30 tháng 11 năm 2005 của Bộ trưởng Bộ Giao thông vận tải về chức danh , nhiệm vụ theo chức danh của thuyền viên và đăng ký thuyền viên làm việc trên tàu biển Việt Nam và Quyết định số 29/2008/QĐ-BGTVT ngày 16 tháng 12 năm 2008 của Bộ trưởng Bộ Giao thông vận tải về chức danh , nhiệm vụ theo chức danh của thuyền viên và đăng ký thuyền viên làm việc trên tàu biển Việt Nam còn `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e6` Quyết định số 65/2005/QĐ-BGTVT `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e5` 3 . Hộ chiếu thuyền viên đã cấp theo Quyết định số 65/2005/QĐ-BGTVT ngày 30 tháng 11 năm 2005 của Bộ trưởng Bộ Giao thông vận tải về chức danh , nhiệm vụ theo chức danh của thuyền viên và đăng ký thuyền viên làm việc trên tàu biển Việt Nam và Quyết định số 29/2008/QĐ-BGTVT ngày 16 tháng 12 năm 2008 của Bộ trưởng Bộ Giao thông vận tải về chức danh , nhiệm vụ theo chức danh của thuyền viên và đăng ký thuyền viên làm việc trên tàu biển Việt Nam còn `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e7` Quyết định số 29/2008/QĐ-BGTVT `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e6` Quyết định số 65/2005/QĐ-BGTVT `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e8` ngày 30 tháng 11 năm 2005 `[NGAY_THAM_CHIEU]`)
- (`e7` Quyết định số 29/2008/QĐ-BGTVT `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e9` ngày 16 tháng 12 năm 2008 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #07_2012_TT-BGTVT_27433#body_standalone_93 (Loại: `body_standalone`)
> **[Điều 74]`<DIEU>`** . **[3 . **[Hộ chiếu thuyền viên]`<GIAY_TO_HO_SO>`** đã cấp theo **[Quyết định số 65/2005/QĐ-BGTVT]`<THAM_CHIEU_PHAP_LY>`** **[ngày 30 tháng 11 năm 2005]`<NGAY_THAM_CHIEU>`** của **[Bộ trưởng Bộ Giao thông vận tải]`<CO_QUAN_THAM_QUYEN>`** về chức danh , nhiệm vụ theo chức danh của thuyền viên và đăng ký thuyền viên làm việc trên **[tàu biển]`<TAI_SAN_VAT_CHAT>`** Việt Nam và **[Quyết định số 29/2008/QĐ-BGTVT]`<THAM_CHIEU_PHAP_LY>`** **[ngày 16 tháng 12 năm 2008]`<NGAY_THAM_CHIEU>`** của **[Bộ trưởng Bộ Giao thông vận tải]`<CO_QUAN_THAM_QUYEN>`** về chức danh , nhiệm vụ theo chức danh của thuyền viên và đăng ký thuyền viên làm việc trên **[tàu biển]`<TAI_SAN_VAT_CHAT>`** Việt Nam còn]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 74** → `DIEU` (span: `[0:2]`)
- `[e1]` **3 . Hộ chiếu thuyền viên đã cấp theo Quyết định số 65/2005/QĐ-BGTVT ngày 30 tháng 11 năm 2005 của Bộ trưởng Bộ Giao thông vận tải về chức danh , nhiệm vụ theo chức danh của thuyền viên và đăng ký thuyền viên làm việc trên tàu biển Việt Nam và Quyết định số 29/2008/QĐ-BGTVT ngày 16 tháng 12 năm 2008 của Bộ trưởng Bộ Giao thông vận tải về chức danh , nhiệm vụ theo chức danh của thuyền viên và đăng ký thuyền viên làm việc trên tàu biển Việt Nam còn** → `KHOAN` (span: `[3:69]`)
- `[e2]` **Quyết định số 65/2005/QĐ-BGTVT** → `THAM_CHIEU_PHAP_LY` (span: `[10:13]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **Quyết định số 29/2008/QĐ-BGTVT** → `THAM_CHIEU_PHAP_LY` (span: `[40:43]`) *(lồng trong `e1` (`KHOAN`))*
- `[e4]` **ngày 30 tháng 11 năm 2005** → `NGAY_THAM_CHIEU` (span: `[13:19]`) *(lồng trong `e1` (`KHOAN`))*
- `[e5]` **ngày 16 tháng 12 năm 2008** → `NGAY_THAM_CHIEU` (span: `[43:49]`) *(lồng trong `e1` (`KHOAN`))*
- `[e6]` **Bộ trưởng Bộ Giao thông vận tải** → `CO_QUAN_THAM_QUYEN` (span: `[20:24]`) *(lồng trong `e1` (`KHOAN`))*
- `[e7]` **Bộ trưởng Bộ Giao thông vận tải** → `CO_QUAN_THAM_QUYEN` (span: `[50:54]`) *(lồng trong `e1` (`KHOAN`))*
- `[e8]` **Hộ chiếu thuyền viên** → `GIAY_TO_HO_SO` (span: `[5:7]`) *(lồng trong `e1` (`KHOAN`))*
- `[e9]` **tàu biển** → `TAI_SAN_VAT_CHAT` (span: `[37:38]`) *(lồng trong `e1` (`KHOAN`))*
- `[e10]` **tàu biển** → `TAI_SAN_VAT_CHAT` (span: `[67:68]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 3 . Hộ chiếu thuyền viên đã cấp theo Quyết định số 65/2005/QĐ-BGTVT ngày 30 tháng 11 năm 2005 của Bộ trưởng Bộ Giao thông vận tải về chức danh , nhiệm vụ theo chức danh của thuyền viên và đăng ký thuyền viên làm việc trên tàu biển Việt Nam và Quyết định số 29/2008/QĐ-BGTVT ngày 16 tháng 12 năm 2008 của Bộ trưởng Bộ Giao thông vận tải về chức danh , nhiệm vụ theo chức danh của thuyền viên và đăng ký thuyền viên làm việc trên tàu biển Việt Nam còn `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 74 `[DIEU]`)
- (`e1` 3 . Hộ chiếu thuyền viên đã cấp theo Quyết định số 65/2005/QĐ-BGTVT ngày 30 tháng 11 năm 2005 của Bộ trưởng Bộ Giao thông vận tải về chức danh , nhiệm vụ theo chức danh của thuyền viên và đăng ký thuyền viên làm việc trên tàu biển Việt Nam và Quyết định số 29/2008/QĐ-BGTVT ngày 16 tháng 12 năm 2008 của Bộ trưởng Bộ Giao thông vận tải về chức danh , nhiệm vụ theo chức danh của thuyền viên và đăng ký thuyền viên làm việc trên tàu biển Việt Nam còn `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e2` Quyết định số 65/2005/QĐ-BGTVT `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e1` 3 . Hộ chiếu thuyền viên đã cấp theo Quyết định số 65/2005/QĐ-BGTVT ngày 30 tháng 11 năm 2005 của Bộ trưởng Bộ Giao thông vận tải về chức danh , nhiệm vụ theo chức danh của thuyền viên và đăng ký thuyền viên làm việc trên tàu biển Việt Nam và Quyết định số 29/2008/QĐ-BGTVT ngày 16 tháng 12 năm 2008 của Bộ trưởng Bộ Giao thông vận tải về chức danh , nhiệm vụ theo chức danh của thuyền viên và đăng ký thuyền viên làm việc trên tàu biển Việt Nam còn `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Quyết định số 29/2008/QĐ-BGTVT `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e2` Quyết định số 65/2005/QĐ-BGTVT `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e4` ngày 30 tháng 11 năm 2005 `[NGAY_THAM_CHIEU]`)
- (`e3` Quyết định số 29/2008/QĐ-BGTVT `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e5` ngày 16 tháng 12 năm 2008 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #07_2012_TT-BGTVT_27433#body_context_94 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[07/2012/TT-BGTVT]`<SO_HIEU>`** của **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Giao thông Vận tải]`<LINH_VUC>`** . **[Điều 74]`<DIEU>`** . **[4 . **[Sổ thuyền viên]`<GIAY_TO_HO_SO>`** đã cấp theo **[Quyết định số 65/2005/QĐ-BGTVT]`<THAM_CHIEU_PHAP_LY>`** **[ngày 30 tháng 11 năm 2005]`<NGAY_THAM_CHIEU>`** của **[Bộ trưởng Bộ Giao thông vận tải]`<CO_QUAN_THAM_QUYEN>`** về chức danh , nhiệm vụ theo chức danh của thuyền viên và đăng ký thuyền viên làm việc trên **[tàu biển]`<TAI_SAN_VAT_CHAT>`** Việt Nam và **[Quyết định số 29/2008/QĐ-BGTVT]`<THAM_CHIEU_PHAP_LY>`** **[ngày 16 tháng 12 năm 2008]`<NGAY_THAM_CHIEU>`** của **[Bộ trưởng Bộ Giao thông vận tải]`<CO_QUAN_THAM_QUYEN>`** về chức danh , nhiệm vụ theo chức danh của thuyền viên và đăng ký thuyền viên làm việc trên **[tàu biển]`<TAI_SAN_VAT_CHAT>`** Việt Nam có giá]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **07/2012/TT-BGTVT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[4:7]`)
- `[e3]` **Giao thông Vận tải** → `LINH_VUC` (span: `[9:11]`)
- `[e4]` **Điều 74** → `DIEU` (span: `[12:14]`)
- `[e5]` **4 . Sổ thuyền viên đã cấp theo Quyết định số 65/2005/QĐ-BGTVT ngày 30 tháng 11 năm 2005 của Bộ trưởng Bộ Giao thông vận tải về chức danh , nhiệm vụ theo chức danh của thuyền viên và đăng ký thuyền viên làm việc trên tàu biển Việt Nam và Quyết định số 29/2008/QĐ-BGTVT ngày 16 tháng 12 năm 2008 của Bộ trưởng Bộ Giao thông vận tải về chức danh , nhiệm vụ theo chức danh của thuyền viên và đăng ký thuyền viên làm việc trên tàu biển Việt Nam có giá** → `KHOAN` (span: `[15:82]`)
- `[e6]` **Quyết định số 65/2005/QĐ-BGTVT** → `THAM_CHIEU_PHAP_LY` (span: `[22:25]`) *(lồng trong `e5` (`KHOAN`))*
- `[e7]` **Quyết định số 29/2008/QĐ-BGTVT** → `THAM_CHIEU_PHAP_LY` (span: `[52:55]`) *(lồng trong `e5` (`KHOAN`))*
- `[e8]` **ngày 30 tháng 11 năm 2005** → `NGAY_THAM_CHIEU` (span: `[25:31]`) *(lồng trong `e5` (`KHOAN`))*
- `[e9]` **ngày 16 tháng 12 năm 2008** → `NGAY_THAM_CHIEU` (span: `[55:61]`) *(lồng trong `e5` (`KHOAN`))*
- `[e10]` **Bộ trưởng Bộ Giao thông vận tải** → `CO_QUAN_THAM_QUYEN` (span: `[32:36]`) *(lồng trong `e5` (`KHOAN`))*
- `[e11]` **Bộ trưởng Bộ Giao thông vận tải** → `CO_QUAN_THAM_QUYEN` (span: `[62:66]`) *(lồng trong `e5` (`KHOAN`))*
- `[e12]` **Sổ thuyền viên** → `GIAY_TO_HO_SO` (span: `[17:19]`) *(lồng trong `e5` (`KHOAN`))*
- `[e13]` **tàu biển** → `TAI_SAN_VAT_CHAT` (span: `[49:50]`) *(lồng trong `e5` (`KHOAN`))*
- `[e14]` **tàu biển** → `TAI_SAN_VAT_CHAT` (span: `[79:80]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Giao thông Vận tải `[LINH_VUC]`)
- (`e4` Điều 74 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`)
- (`e5` 4 . Sổ thuyền viên đã cấp theo Quyết định số 65/2005/QĐ-BGTVT ngày 30 tháng 11 năm 2005 của Bộ trưởng Bộ Giao thông vận tải về chức danh , nhiệm vụ theo chức danh của thuyền viên và đăng ký thuyền viên làm việc trên tàu biển Việt Nam và Quyết định số 29/2008/QĐ-BGTVT ngày 16 tháng 12 năm 2008 của Bộ trưởng Bộ Giao thông vận tải về chức danh , nhiệm vụ theo chức danh của thuyền viên và đăng ký thuyền viên làm việc trên tàu biển Việt Nam có giá `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 74 `[DIEU]`)
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Giao thông Vận tải `[LINH_VUC]`)
- (`e5` 4 . Sổ thuyền viên đã cấp theo Quyết định số 65/2005/QĐ-BGTVT ngày 30 tháng 11 năm 2005 của Bộ trưởng Bộ Giao thông vận tải về chức danh , nhiệm vụ theo chức danh của thuyền viên và đăng ký thuyền viên làm việc trên tàu biển Việt Nam và Quyết định số 29/2008/QĐ-BGTVT ngày 16 tháng 12 năm 2008 của Bộ trưởng Bộ Giao thông vận tải về chức danh , nhiệm vụ theo chức danh của thuyền viên và đăng ký thuyền viên làm việc trên tàu biển Việt Nam có giá `[KHOAN]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Giao thông Vận tải `[LINH_VUC]`)
- (`e5` 4 . Sổ thuyền viên đã cấp theo Quyết định số 65/2005/QĐ-BGTVT ngày 30 tháng 11 năm 2005 của Bộ trưởng Bộ Giao thông vận tải về chức danh , nhiệm vụ theo chức danh của thuyền viên và đăng ký thuyền viên làm việc trên tàu biển Việt Nam và Quyết định số 29/2008/QĐ-BGTVT ngày 16 tháng 12 năm 2008 của Bộ trưởng Bộ Giao thông vận tải về chức danh , nhiệm vụ theo chức danh của thuyền viên và đăng ký thuyền viên làm việc trên tàu biển Việt Nam có giá `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e6` Quyết định số 65/2005/QĐ-BGTVT `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e5` 4 . Sổ thuyền viên đã cấp theo Quyết định số 65/2005/QĐ-BGTVT ngày 30 tháng 11 năm 2005 của Bộ trưởng Bộ Giao thông vận tải về chức danh , nhiệm vụ theo chức danh của thuyền viên và đăng ký thuyền viên làm việc trên tàu biển Việt Nam và Quyết định số 29/2008/QĐ-BGTVT ngày 16 tháng 12 năm 2008 của Bộ trưởng Bộ Giao thông vận tải về chức danh , nhiệm vụ theo chức danh của thuyền viên và đăng ký thuyền viên làm việc trên tàu biển Việt Nam có giá `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e7` Quyết định số 29/2008/QĐ-BGTVT `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e6` Quyết định số 65/2005/QĐ-BGTVT `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e8` ngày 30 tháng 11 năm 2005 `[NGAY_THAM_CHIEU]`)
- (`e7` Quyết định số 29/2008/QĐ-BGTVT `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e9` ngày 16 tháng 12 năm 2008 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #07_2012_TT-BGTVT_27433#body_standalone_95 (Loại: `body_standalone`)
> **[Điều 74]`<DIEU>`** . **[4 . **[Sổ thuyền viên]`<GIAY_TO_HO_SO>`** đã cấp theo **[Quyết định số 65/2005/QĐ-BGTVT]`<THAM_CHIEU_PHAP_LY>`** **[ngày 30 tháng 11 năm 2005]`<NGAY_THAM_CHIEU>`** của **[Bộ trưởng Bộ Giao thông vận tải]`<CO_QUAN_THAM_QUYEN>`** về chức danh , nhiệm vụ theo chức danh của thuyền viên và đăng ký thuyền viên làm việc trên **[tàu biển]`<TAI_SAN_VAT_CHAT>`** Việt Nam và **[Quyết định số 29/2008/QĐ-BGTVT]`<THAM_CHIEU_PHAP_LY>`** **[ngày 16 tháng 12 năm 2008]`<NGAY_THAM_CHIEU>`** của **[Bộ trưởng Bộ Giao thông vận tải]`<CO_QUAN_THAM_QUYEN>`** về chức danh , nhiệm vụ theo chức danh của thuyền viên và đăng ký thuyền viên làm việc trên **[tàu biển]`<TAI_SAN_VAT_CHAT>`** Việt Nam có giá]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 74** → `DIEU` (span: `[0:2]`)
- `[e1]` **4 . Sổ thuyền viên đã cấp theo Quyết định số 65/2005/QĐ-BGTVT ngày 30 tháng 11 năm 2005 của Bộ trưởng Bộ Giao thông vận tải về chức danh , nhiệm vụ theo chức danh của thuyền viên và đăng ký thuyền viên làm việc trên tàu biển Việt Nam và Quyết định số 29/2008/QĐ-BGTVT ngày 16 tháng 12 năm 2008 của Bộ trưởng Bộ Giao thông vận tải về chức danh , nhiệm vụ theo chức danh của thuyền viên và đăng ký thuyền viên làm việc trên tàu biển Việt Nam có giá** → `KHOAN` (span: `[3:70]`)
- `[e2]` **Quyết định số 65/2005/QĐ-BGTVT** → `THAM_CHIEU_PHAP_LY` (span: `[10:13]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **Quyết định số 29/2008/QĐ-BGTVT** → `THAM_CHIEU_PHAP_LY` (span: `[40:43]`) *(lồng trong `e1` (`KHOAN`))*
- `[e4]` **ngày 30 tháng 11 năm 2005** → `NGAY_THAM_CHIEU` (span: `[13:19]`) *(lồng trong `e1` (`KHOAN`))*
- `[e5]` **ngày 16 tháng 12 năm 2008** → `NGAY_THAM_CHIEU` (span: `[43:49]`) *(lồng trong `e1` (`KHOAN`))*
- `[e6]` **Bộ trưởng Bộ Giao thông vận tải** → `CO_QUAN_THAM_QUYEN` (span: `[20:24]`) *(lồng trong `e1` (`KHOAN`))*
- `[e7]` **Bộ trưởng Bộ Giao thông vận tải** → `CO_QUAN_THAM_QUYEN` (span: `[50:54]`) *(lồng trong `e1` (`KHOAN`))*
- `[e8]` **Sổ thuyền viên** → `GIAY_TO_HO_SO` (span: `[5:7]`) *(lồng trong `e1` (`KHOAN`))*
- `[e9]` **tàu biển** → `TAI_SAN_VAT_CHAT` (span: `[37:38]`) *(lồng trong `e1` (`KHOAN`))*
- `[e10]` **tàu biển** → `TAI_SAN_VAT_CHAT` (span: `[67:68]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 4 . Sổ thuyền viên đã cấp theo Quyết định số 65/2005/QĐ-BGTVT ngày 30 tháng 11 năm 2005 của Bộ trưởng Bộ Giao thông vận tải về chức danh , nhiệm vụ theo chức danh của thuyền viên và đăng ký thuyền viên làm việc trên tàu biển Việt Nam và Quyết định số 29/2008/QĐ-BGTVT ngày 16 tháng 12 năm 2008 của Bộ trưởng Bộ Giao thông vận tải về chức danh , nhiệm vụ theo chức danh của thuyền viên và đăng ký thuyền viên làm việc trên tàu biển Việt Nam có giá `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 74 `[DIEU]`)
- (`e1` 4 . Sổ thuyền viên đã cấp theo Quyết định số 65/2005/QĐ-BGTVT ngày 30 tháng 11 năm 2005 của Bộ trưởng Bộ Giao thông vận tải về chức danh , nhiệm vụ theo chức danh của thuyền viên và đăng ký thuyền viên làm việc trên tàu biển Việt Nam và Quyết định số 29/2008/QĐ-BGTVT ngày 16 tháng 12 năm 2008 của Bộ trưởng Bộ Giao thông vận tải về chức danh , nhiệm vụ theo chức danh của thuyền viên và đăng ký thuyền viên làm việc trên tàu biển Việt Nam có giá `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e2` Quyết định số 65/2005/QĐ-BGTVT `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e1` 4 . Sổ thuyền viên đã cấp theo Quyết định số 65/2005/QĐ-BGTVT ngày 30 tháng 11 năm 2005 của Bộ trưởng Bộ Giao thông vận tải về chức danh , nhiệm vụ theo chức danh của thuyền viên và đăng ký thuyền viên làm việc trên tàu biển Việt Nam và Quyết định số 29/2008/QĐ-BGTVT ngày 16 tháng 12 năm 2008 của Bộ trưởng Bộ Giao thông vận tải về chức danh , nhiệm vụ theo chức danh của thuyền viên và đăng ký thuyền viên làm việc trên tàu biển Việt Nam có giá `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Quyết định số 29/2008/QĐ-BGTVT `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e2` Quyết định số 65/2005/QĐ-BGTVT `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e4` ngày 30 tháng 11 năm 2005 `[NGAY_THAM_CHIEU]`)
- (`e3` Quyết định số 29/2008/QĐ-BGTVT `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e5` ngày 16 tháng 12 năm 2008 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #07_2012_TT-BGTVT_27433#body_context_96 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[07/2012/TT-BGTVT]`<SO_HIEU>`** ban hành **[ngày 21 tháng 03 năm 2012]`<NGAY_BAN_HANH>`** bởi **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** . **[Điều 74]`<DIEU>`** . **[5 . Cục Hàng hải Việt Nam tổ chức in và cấp **[Sổ thuyền viên]`<GIAY_TO_HO_SO>`** , **[Hộ chiếu thuyền viên]`<GIAY_TO_HO_SO>`** **[theo quy định tại]`<TU_KHOA_PHAP_LY>`** **[Thông tư này]`<THAM_CHIEU_PHAP_LY>`** .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **07/2012/TT-BGTVT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[11:14]`)
- `[e3]` **ngày 21 tháng 03 năm 2012** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 74** → `DIEU` (span: `[15:17]`)
- `[e5]` **5 . Cục Hàng hải Việt Nam tổ chức in và cấp Sổ thuyền viên , Hộ chiếu thuyền viên theo quy định tại Thông tư này .** → `KHOAN` (span: `[18:38]`)
- `[e6]` **Thông tư này** → `THAM_CHIEU_PHAP_LY` (span: `[35:37]`) *(lồng trong `e5` (`KHOAN`))*
- `[e7]` **theo quy định tại** → `TU_KHOA_PHAP_LY` (span: `[32:35]`) *(lồng trong `e5` (`KHOAN`))*
- `[e8]` **Sổ thuyền viên** → `GIAY_TO_HO_SO` (span: `[27:29]`) *(lồng trong `e5` (`KHOAN`))*
- `[e9]` **Hộ chiếu thuyền viên** → `GIAY_TO_HO_SO` (span: `[30:32]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 21 tháng 03 năm 2012 `[NGAY_BAN_HANH]`)
- (`e4` Điều 74 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`)
- (`e5` 5 . Cục Hàng hải Việt Nam tổ chức in và cấp Sổ thuyền viên , Hộ chiếu thuyền viên theo quy định tại Thông tư này . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 74 `[DIEU]`)
- (`e7` theo quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e6` Thông tư này `[THAM_CHIEU_PHAP_LY]`)
- (`e5` 5 . Cục Hàng hải Việt Nam tổ chức in và cấp Sổ thuyền viên , Hộ chiếu thuyền viên theo quy định tại Thông tư này . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e6` Thông tư này `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #07_2012_TT-BGTVT_27433#body_standalone_97 (Loại: `body_standalone`)
> **[Điều 74]`<DIEU>`** . **[5 . Cục Hàng hải Việt Nam tổ chức in và cấp **[Sổ thuyền viên]`<GIAY_TO_HO_SO>`** , **[Hộ chiếu thuyền viên]`<GIAY_TO_HO_SO>`** **[theo quy định tại]`<TU_KHOA_PHAP_LY>`** **[Thông tư này]`<THAM_CHIEU_PHAP_LY>`** .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 74** → `DIEU` (span: `[0:2]`)
- `[e1]` **5 . Cục Hàng hải Việt Nam tổ chức in và cấp Sổ thuyền viên , Hộ chiếu thuyền viên theo quy định tại Thông tư này .** → `KHOAN` (span: `[3:23]`)
- `[e2]` **Thông tư này** → `THAM_CHIEU_PHAP_LY` (span: `[20:22]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **theo quy định tại** → `TU_KHOA_PHAP_LY` (span: `[17:20]`) *(lồng trong `e1` (`KHOAN`))*
- `[e4]` **Sổ thuyền viên** → `GIAY_TO_HO_SO` (span: `[12:14]`) *(lồng trong `e1` (`KHOAN`))*
- `[e5]` **Hộ chiếu thuyền viên** → `GIAY_TO_HO_SO` (span: `[15:17]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 5 . Cục Hàng hải Việt Nam tổ chức in và cấp Sổ thuyền viên , Hộ chiếu thuyền viên theo quy định tại Thông tư này . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 74 `[DIEU]`)
- (`e3` theo quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e2` Thông tư này `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 5 . Cục Hàng hải Việt Nam tổ chức in và cấp Sổ thuyền viên , Hộ chiếu thuyền viên theo quy định tại Thông tư này . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e2` Thông tư này `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #07_2012_TT-BGTVT_27433#body_context_98 (Loại: `body_context`)
> **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[07/2012/TT-BGTVT]`<SO_HIEU>`** . **[Điều 3]`<DIEU>`** . **[Khoản 2]`<KHOAN>`** . **[a ) Tàu vào , rời cảng ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[4:5]`)
- `[e1]` **07/2012/TT-BGTVT** → `SO_HIEU` (span: `[6:7]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[0:3]`)
- `[e3]` **Điều 3** → `DIEU` (span: `[8:10]`)
- `[e4]` **Khoản 2** → `KHOAN` (span: `[11:13]`)
- `[e5]` **a ) Tàu vào , rời cảng ;** → `DIEM` (span: `[14:22]`)

**Quan hệ:**
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 3 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`)
- (`e4` Khoản 2 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 3 `[DIEU]`)
- (`e5` a ) Tàu vào , rời cảng ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e4` Khoản 2 `[KHOAN]`)


---

### Mẫu #07_2012_TT-BGTVT_27433#body_context_99 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[07/2012/TT-BGTVT]`<SO_HIEU>`** của **[Bộ Giao thông vận tải]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Giao thông Vận tải]`<LINH_VUC>`** . **[Điều 74]`<DIEU>`** . **[Khoản 2 . Ban hành kèm theo Thông tư này 05 phụ lục]`<KHOAN>`** : **[a ) **[Phụ lục I]`<THAM_CHIEU_PHAP_LY>`** : mẫu **[Sổ thuyền viên]`<GIAY_TO_HO_SO>`** ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **07/2012/TT-BGTVT** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Giao thông vận tải** → `CO_QUAN_BAN_HANH` (span: `[4:7]`)
- `[e3]` **Giao thông Vận tải** → `LINH_VUC` (span: `[9:11]`)
- `[e4]` **Điều 74** → `DIEU` (span: `[12:14]`)
- `[e5]` **Khoản 2 . Ban hành kèm theo Thông tư này 05 phụ lục** → `KHOAN` (span: `[15:25]`)
- `[e6]` **a ) Phụ lục I : mẫu Sổ thuyền viên ;** → `DIEM` (span: `[26:35]`)
- `[e7]` **Phụ lục I** → `THAM_CHIEU_PHAP_LY` (span: `[28:30]`) *(lồng trong `e6` (`DIEM`))*
- `[e8]` **Sổ thuyền viên** → `GIAY_TO_HO_SO` (span: `[32:34]`) *(lồng trong `e6` (`DIEM`))*

**Quan hệ:**
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Giao thông vận tải `[CO_QUAN_BAN_HANH]`)
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Giao thông Vận tải `[LINH_VUC]`)
- (`e4` Điều 74 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`)
- (`e5` Khoản 2 . Ban hành kèm theo Thông tư này 05 phụ lục `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 74 `[DIEU]`)
- (`e6` a ) Phụ lục I : mẫu Sổ thuyền viên ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e5` Khoản 2 . Ban hành kèm theo Thông tư này 05 phụ lục `[KHOAN]`)
- (`e1` 07/2012/TT-BGTVT `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Giao thông Vận tải `[LINH_VUC]`)
- (`e6` a ) Phụ lục I : mẫu Sổ thuyền viên ; `[DIEM]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Giao thông Vận tải `[LINH_VUC]`)
- (`e6` a ) Phụ lục I : mẫu Sổ thuyền viên ; `[DIEM]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e7` Phụ lục I `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #07_2012_TT-BGTVT_27433#body_standalone_100 (Loại: `body_standalone`)
> **[Điều 74]`<DIEU>`** . **[Khoản 2 . Ban hành kèm theo Thông tư này 05 phụ lục]`<KHOAN>`** : **[a ) **[Phụ lục I]`<THAM_CHIEU_PHAP_LY>`** : mẫu **[Sổ thuyền viên]`<GIAY_TO_HO_SO>`** ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Điều 74** → `DIEU` (span: `[0:2]`)
- `[e1]` **Khoản 2 . Ban hành kèm theo Thông tư này 05 phụ lục** → `KHOAN` (span: `[3:13]`)
- `[e2]` **a ) Phụ lục I : mẫu Sổ thuyền viên ;** → `DIEM` (span: `[14:23]`)
- `[e3]` **Phụ lục I** → `THAM_CHIEU_PHAP_LY` (span: `[16:18]`) *(lồng trong `e2` (`DIEM`))*
- `[e4]` **Sổ thuyền viên** → `GIAY_TO_HO_SO` (span: `[20:22]`) *(lồng trong `e2` (`DIEM`))*

**Quan hệ:**
- (`e1` Khoản 2 . Ban hành kèm theo Thông tư này 05 phụ lục `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 74 `[DIEU]`)
- (`e2` a ) Phụ lục I : mẫu Sổ thuyền viên ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e1` Khoản 2 . Ban hành kèm theo Thông tư này 05 phụ lục `[KHOAN]`)
- (`e2` a ) Phụ lục I : mẫu Sổ thuyền viên ; `[DIEM]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Phụ lục I `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #07_2012_TT-BGTVT_27433#hard_negative_101 (Loại: `hard_negative`)
> Mục 1


---

### Mẫu #07_2012_TT-BGTVT_27433#hard_negative_102 (Loại: `hard_negative`)
> Mục 2


---

### Mẫu #07_2012_TT-BGTVT_27433#hard_negative_103 (Loại: `hard_negative`)
> Mục 3


---

### Mẫu #07_2012_TT-BGTVT_27433#hard_negative_104 (Loại: `hard_negative`)
> Mục 4


---

### Mẫu #07_2012_TT-BGTVT_27433#hard_negative_105 (Loại: `hard_negative`)
> Mục 1


---

### Mẫu #07_2012_TT-BGTVT_27433#hard_negative_106 (Loại: `hard_negative`)
> Mục 2


---
