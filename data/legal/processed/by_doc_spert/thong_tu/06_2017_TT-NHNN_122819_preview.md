# Dữ liệu gán nhãn văn bản: 06_2017_TT-NHNN_122819
- **Thể loại**: `thong_tu`
- **Phân vùng dữ liệu**: `DEV`
- **Tổng số mẫu**: 111 mẫu
- **Tổng số thực thể**: 997
- **Tổng số quan hệ**: 622

---

### Mẫu #06_2017_TT-NHNN_122819#preamble_context_0 (Loại: `preamble_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[06/2017/TT-NHNN]`<SO_HIEU>`** của **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_BAN_HANH>`** . **[Sửa đổi , bổ sung một số điều của]`<TU_KHOA_PHAP_LY>`** **[Thông tư số 03/2014/TT-NHNN]`<THAM_CHIEU_PHAP_LY>`** **[ngày 23/01/2014]`<NGAY_THAM_CHIEU>`** của **[Thống đốc Ngân hàng Nhà nước]`<CO_QUAN_THAM_QUYEN>`** quy định về **[Quỹ bảo đảm an toàn hệ thống quỹ tín dụng nhân dân]`<TO_CHUC_DOANH_NGHIEP>`** và **[Thông tư số 04/2015/TT-NHNN]`<THAM_CHIEU_PHAP_LY>`** **[ngày 31/3/2015]`<NGAY_THAM_CHIEU>`** của **[Thống đốc Ngân hàng Nhà nước]`<CO_QUAN_THAM_QUYEN>`** quy định về **[quỹ tín dụng nhân dân]`<TO_CHUC_DOANH_NGHIEP>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **06/2017/TT-NHNN** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_BAN_HANH` (span: `[4:7]`)
- `[e3]` **Thông tư số 03/2014/TT-NHNN** → `THAM_CHIEU_PHAP_LY` (span: `[14:17]`)
- `[e4]` **Thông tư số 04/2015/TT-NHNN** → `THAM_CHIEU_PHAP_LY` (span: `[33:36]`)
- `[e5]` **Sửa đổi , bổ sung một số điều của** → `TU_KHOA_PHAP_LY` (span: `[8:14]`)
- `[e6]` **ngày 23/01/2014** → `NGAY_THAM_CHIEU` (span: `[17:19]`)
- `[e7]` **ngày 31/3/2015** → `NGAY_THAM_CHIEU` (span: `[36:38]`)
- `[e8]` **Thống đốc Ngân hàng Nhà nước** → `CO_QUAN_THAM_QUYEN` (span: `[20:23]`)
- `[e9]` **Thống đốc Ngân hàng Nhà nước** → `CO_QUAN_THAM_QUYEN` (span: `[39:42]`)
- `[e10]` **Quỹ bảo đảm an toàn hệ thống quỹ tín dụng nhân dân** → `TO_CHUC_DOANH_NGHIEP` (span: `[25:32]`)
- `[e11]` **quỹ tín dụng nhân dân** → `TO_CHUC_DOANH_NGHIEP` (span: `[44:47]`)

**Quan hệ:**
- (`e1` 06/2017/TT-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Ngân hàng Nhà nước Việt Nam `[CO_QUAN_BAN_HANH]`)
- (`e1` 06/2017/TT-NHNN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e5` Sửa đổi , bổ sung một số điều của `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Thông tư số 03/2014/TT-NHNN `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 06/2017/TT-NHNN `[SO_HIEU]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Thông tư số 03/2014/TT-NHNN `[THAM_CHIEU_PHAP_LY]`)
- (`e5` Sửa đổi , bổ sung một số điều của `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e4` Thông tư số 04/2015/TT-NHNN `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 06/2017/TT-NHNN `[SO_HIEU]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e4` Thông tư số 04/2015/TT-NHNN `[THAM_CHIEU_PHAP_LY]`)
- (`e3` Thông tư số 03/2014/TT-NHNN `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e6` ngày 23/01/2014 `[NGAY_THAM_CHIEU]`)
- (`e4` Thông tư số 04/2015/TT-NHNN `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e7` ngày 31/3/2015 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #06_2017_TT-NHNN_122819#preamble_standalone_1 (Loại: `preamble_standalone`)
> **[Sửa đổi , bổ sung một số điều của]`<TU_KHOA_PHAP_LY>`** **[Thông tư số 03/2014/TT-NHNN]`<THAM_CHIEU_PHAP_LY>`** **[ngày 23/01/2014]`<NGAY_THAM_CHIEU>`** của **[Thống đốc Ngân hàng Nhà nước]`<CO_QUAN_THAM_QUYEN>`** quy định về **[Quỹ bảo đảm an toàn hệ thống quỹ tín dụng nhân dân]`<TO_CHUC_DOANH_NGHIEP>`** và **[Thông tư số 04/2015/TT-NHNN]`<THAM_CHIEU_PHAP_LY>`** **[ngày 31/3/2015]`<NGAY_THAM_CHIEU>`** của **[Thống đốc Ngân hàng Nhà nước]`<CO_QUAN_THAM_QUYEN>`** quy định về **[quỹ tín dụng nhân dân]`<TO_CHUC_DOANH_NGHIEP>`**

**Thực thể:**
- `[e0]` **Thông tư số 03/2014/TT-NHNN** → `THAM_CHIEU_PHAP_LY` (span: `[6:9]`)
- `[e1]` **Thông tư số 04/2015/TT-NHNN** → `THAM_CHIEU_PHAP_LY` (span: `[25:28]`)
- `[e2]` **Sửa đổi , bổ sung một số điều của** → `TU_KHOA_PHAP_LY` (span: `[0:6]`)
- `[e3]` **ngày 23/01/2014** → `NGAY_THAM_CHIEU` (span: `[9:11]`)
- `[e4]` **ngày 31/3/2015** → `NGAY_THAM_CHIEU` (span: `[28:30]`)
- `[e5]` **Thống đốc Ngân hàng Nhà nước** → `CO_QUAN_THAM_QUYEN` (span: `[12:15]`)
- `[e6]` **Thống đốc Ngân hàng Nhà nước** → `CO_QUAN_THAM_QUYEN` (span: `[31:34]`)
- `[e7]` **Quỹ bảo đảm an toàn hệ thống quỹ tín dụng nhân dân** → `TO_CHUC_DOANH_NGHIEP` (span: `[17:24]`)
- `[e8]` **quỹ tín dụng nhân dân** → `TO_CHUC_DOANH_NGHIEP` (span: `[36:39]`)

**Quan hệ:**
- (`e2` Sửa đổi , bổ sung một số điều của `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e0` Thông tư số 03/2014/TT-NHNN `[THAM_CHIEU_PHAP_LY]`)
- (`e5` Thống đốc Ngân hàng Nhà nước `[CO_QUAN_THAM_QUYEN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e0` Thông tư số 03/2014/TT-NHNN `[THAM_CHIEU_PHAP_LY]`)
- (`e2` Sửa đổi , bổ sung một số điều của `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e1` Thông tư số 04/2015/TT-NHNN `[THAM_CHIEU_PHAP_LY]`)
- (`e6` Thống đốc Ngân hàng Nhà nước `[CO_QUAN_THAM_QUYEN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e1` Thông tư số 04/2015/TT-NHNN `[THAM_CHIEU_PHAP_LY]`)
- (`e0` Thông tư số 03/2014/TT-NHNN `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e3` ngày 23/01/2014 `[NGAY_THAM_CHIEU]`)
- (`e1` Thông tư số 04/2015/TT-NHNN `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e4` ngày 31/3/2015 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #06_2017_TT-NHNN_122819#preamble_context_2 (Loại: `preamble_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[06/2017/TT-NHNN]`<SO_HIEU>`** của **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_BAN_HANH>`** . **[Căn cứ]`<TU_KHOA_PHAP_LY>`** **[Luật Ngân hàng Nhà nước Việt Nam]`<THAM_CHIEU_PHAP_LY>`** **[ngày 16 tháng 6 năm 2010]`<NGAY_THAM_CHIEU>`** ;

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **06/2017/TT-NHNN** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_BAN_HANH` (span: `[4:7]`)
- `[e3]` **Luật Ngân hàng Nhà nước Việt Nam** → `THAM_CHIEU_PHAP_LY` (span: `[9:13]`)
- `[e4]` **Căn cứ** → `TU_KHOA_PHAP_LY` (span: `[8:9]`)
- `[e5]` **ngày 16 tháng 6 năm 2010** → `NGAY_THAM_CHIEU` (span: `[13:19]`)

**Quan hệ:**
- (`e1` 06/2017/TT-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Ngân hàng Nhà nước Việt Nam `[CO_QUAN_BAN_HANH]`)
- (`e1` 06/2017/TT-NHNN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e4` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Luật Ngân hàng Nhà nước Việt Nam `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 06/2017/TT-NHNN `[SO_HIEU]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Luật Ngân hàng Nhà nước Việt Nam `[THAM_CHIEU_PHAP_LY]`)
- (`e3` Luật Ngân hàng Nhà nước Việt Nam `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e5` ngày 16 tháng 6 năm 2010 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #06_2017_TT-NHNN_122819#preamble_standalone_3 (Loại: `preamble_standalone`)
> **[Căn cứ]`<TU_KHOA_PHAP_LY>`** **[Luật Ngân hàng Nhà nước Việt Nam]`<THAM_CHIEU_PHAP_LY>`** **[ngày 16 tháng 6 năm 2010]`<NGAY_THAM_CHIEU>`** ;

**Thực thể:**
- `[e0]` **Luật Ngân hàng Nhà nước Việt Nam** → `THAM_CHIEU_PHAP_LY` (span: `[1:5]`)
- `[e1]` **Căn cứ** → `TU_KHOA_PHAP_LY` (span: `[0:1]`)
- `[e2]` **ngày 16 tháng 6 năm 2010** → `NGAY_THAM_CHIEU` (span: `[5:11]`)

**Quan hệ:**
- (`e1` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e0` Luật Ngân hàng Nhà nước Việt Nam `[THAM_CHIEU_PHAP_LY]`)
- (`e0` Luật Ngân hàng Nhà nước Việt Nam `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e2` ngày 16 tháng 6 năm 2010 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #06_2017_TT-NHNN_122819#preamble_context_4 (Loại: `preamble_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[06/2017/TT-NHNN]`<SO_HIEU>`** của **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_BAN_HANH>`** . **[Căn cứ]`<TU_KHOA_PHAP_LY>`** **[Luật Các tổ chức tín dụng]`<THAM_CHIEU_PHAP_LY>`** **[ngày 16 tháng 6 năm 2010]`<NGAY_THAM_CHIEU>`** ;

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **06/2017/TT-NHNN** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_BAN_HANH` (span: `[4:7]`)
- `[e3]` **Luật Các tổ chức tín dụng** → `THAM_CHIEU_PHAP_LY` (span: `[9:13]`)
- `[e4]` **Căn cứ** → `TU_KHOA_PHAP_LY` (span: `[8:9]`)
- `[e5]` **ngày 16 tháng 6 năm 2010** → `NGAY_THAM_CHIEU` (span: `[13:19]`)

**Quan hệ:**
- (`e1` 06/2017/TT-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Ngân hàng Nhà nước Việt Nam `[CO_QUAN_BAN_HANH]`)
- (`e1` 06/2017/TT-NHNN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e4` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Luật Các tổ chức tín dụng `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 06/2017/TT-NHNN `[SO_HIEU]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Luật Các tổ chức tín dụng `[THAM_CHIEU_PHAP_LY]`)
- (`e3` Luật Các tổ chức tín dụng `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e5` ngày 16 tháng 6 năm 2010 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #06_2017_TT-NHNN_122819#preamble_standalone_5 (Loại: `preamble_standalone`)
> **[Căn cứ]`<TU_KHOA_PHAP_LY>`** **[Luật Các tổ chức tín dụng]`<THAM_CHIEU_PHAP_LY>`** **[ngày 16 tháng 6 năm 2010]`<NGAY_THAM_CHIEU>`** ;

**Thực thể:**
- `[e0]` **Luật Các tổ chức tín dụng** → `THAM_CHIEU_PHAP_LY` (span: `[1:5]`)
- `[e1]` **Căn cứ** → `TU_KHOA_PHAP_LY` (span: `[0:1]`)
- `[e2]` **ngày 16 tháng 6 năm 2010** → `NGAY_THAM_CHIEU` (span: `[5:11]`)

**Quan hệ:**
- (`e1` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e0` Luật Các tổ chức tín dụng `[THAM_CHIEU_PHAP_LY]`)
- (`e0` Luật Các tổ chức tín dụng `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e2` ngày 16 tháng 6 năm 2010 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #06_2017_TT-NHNN_122819#preamble_context_6 (Loại: `preamble_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[06/2017/TT-NHNN]`<SO_HIEU>`** của **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_BAN_HANH>`** . **[Căn cứ]`<TU_KHOA_PHAP_LY>`** **[Nghị định số 16/2017/NĐ-CP]`<THAM_CHIEU_PHAP_LY>`** **[ngày 17 tháng 02 năm 2017]`<NGAY_THAM_CHIEU>`** của **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** quy định chức năng , nhiệm vụ , quyền hạn và cơ cấu tổ chức của **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_THAM_QUYEN>`** ;

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **06/2017/TT-NHNN** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_BAN_HANH` (span: `[4:7]`)
- `[e3]` **Nghị định số 16/2017/NĐ-CP** → `THAM_CHIEU_PHAP_LY` (span: `[9:12]`)
- `[e4]` **Căn cứ** → `TU_KHOA_PHAP_LY` (span: `[8:9]`)
- `[e5]` **ngày 17 tháng 02 năm 2017** → `NGAY_THAM_CHIEU` (span: `[12:18]`)
- `[e6]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[19:20]`)
- `[e7]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_THAM_QUYEN` (span: `[30:33]`)

**Quan hệ:**
- (`e1` 06/2017/TT-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Ngân hàng Nhà nước Việt Nam `[CO_QUAN_BAN_HANH]`)
- (`e1` 06/2017/TT-NHNN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e4` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Nghị định số 16/2017/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 06/2017/TT-NHNN `[SO_HIEU]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Nghị định số 16/2017/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e3` Nghị định số 16/2017/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e5` ngày 17 tháng 02 năm 2017 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #06_2017_TT-NHNN_122819#preamble_standalone_7 (Loại: `preamble_standalone`)
> **[Căn cứ]`<TU_KHOA_PHAP_LY>`** **[Nghị định số 16/2017/NĐ-CP]`<THAM_CHIEU_PHAP_LY>`** **[ngày 17 tháng 02 năm 2017]`<NGAY_THAM_CHIEU>`** của **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** quy định chức năng , nhiệm vụ , quyền hạn và cơ cấu tổ chức của **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_THAM_QUYEN>`** ;

**Thực thể:**
- `[e0]` **Nghị định số 16/2017/NĐ-CP** → `THAM_CHIEU_PHAP_LY` (span: `[1:4]`)
- `[e1]` **Căn cứ** → `TU_KHOA_PHAP_LY` (span: `[0:1]`)
- `[e2]` **ngày 17 tháng 02 năm 2017** → `NGAY_THAM_CHIEU` (span: `[4:10]`)
- `[e3]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[11:12]`)
- `[e4]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_THAM_QUYEN` (span: `[22:25]`)

**Quan hệ:**
- (`e1` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e0` Nghị định số 16/2017/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e3` Chính phủ `[CO_QUAN_THAM_QUYEN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e0` Nghị định số 16/2017/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e0` Nghị định số 16/2017/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e2` ngày 17 tháng 02 năm 2017 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #06_2017_TT-NHNN_122819#preamble_context_8 (Loại: `preamble_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[06/2017/TT-NHNN]`<SO_HIEU>`** của **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_BAN_HANH>`** . Theo đề nghị của **[Chánh Thanh tra , giám sát ngân hàng]`<CO_QUAN_THAM_QUYEN>`** ;

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **06/2017/TT-NHNN** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_BAN_HANH` (span: `[4:7]`)
- `[e3]` **Chánh Thanh tra , giám sát ngân hàng** → `CO_QUAN_THAM_QUYEN` (span: `[11:16]`)

**Quan hệ:**
- (`e1` 06/2017/TT-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Ngân hàng Nhà nước Việt Nam `[CO_QUAN_BAN_HANH]`)
- (`e1` 06/2017/TT-NHNN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)


---

### Mẫu #06_2017_TT-NHNN_122819#preamble_standalone_9 (Loại: `preamble_standalone`)
> Theo đề nghị của **[Chánh Thanh tra , giám sát ngân hàng]`<CO_QUAN_THAM_QUYEN>`** ;

**Thực thể:**
- `[e0]` **Chánh Thanh tra , giám sát ngân hàng** → `CO_QUAN_THAM_QUYEN` (span: `[3:8]`)


---

### Mẫu #06_2017_TT-NHNN_122819#preamble_context_10 (Loại: `preamble_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[06/2017/TT-NHNN]`<SO_HIEU>`** của **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_BAN_HANH>`** . **[Thống đốc Ngân hàng Nhà nước]`<CO_QUAN_THAM_QUYEN>`** ban hành Thông tư **[sửa đổi , bổ sung một số điều của]`<TU_KHOA_PHAP_LY>`** **[Thông tư số 03/2014/TT-NHNN]`<THAM_CHIEU_PHAP_LY>`** **[ngày 23 tháng 01 năm 2014]`<NGAY_THAM_CHIEU>`** của **[Thống đốc Ngân hàng Nhà nước]`<CO_QUAN_THAM_QUYEN>`** quy định về **[Quỹ bảo đảm an toàn hệ thống quỹ tín dụng nhân dân]`<TO_CHUC_DOANH_NGHIEP>`** và **[Thông tư số 04/2015/TT-NHNN]`<THAM_CHIEU_PHAP_LY>`** **[ngày 31 tháng 3 năm 2015]`<NGAY_THAM_CHIEU>`** của **[Thống đốc Ngân hàng Nhà nước]`<CO_QUAN_THAM_QUYEN>`** quy định về **[quỹ tín dụng nhân dân]`<TO_CHUC_DOANH_NGHIEP>`** .

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **06/2017/TT-NHNN** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_BAN_HANH` (span: `[4:7]`)
- `[e3]` **Thông tư số 03/2014/TT-NHNN** → `THAM_CHIEU_PHAP_LY` (span: `[19:22]`)
- `[e4]` **Thông tư số 04/2015/TT-NHNN** → `THAM_CHIEU_PHAP_LY` (span: `[42:45]`)
- `[e5]` **sửa đổi , bổ sung một số điều của** → `TU_KHOA_PHAP_LY` (span: `[13:19]`)
- `[e6]` **ngày 23 tháng 01 năm 2014** → `NGAY_THAM_CHIEU` (span: `[22:28]`)
- `[e7]` **ngày 31 tháng 3 năm 2015** → `NGAY_THAM_CHIEU` (span: `[45:51]`)
- `[e8]` **Thống đốc Ngân hàng Nhà nước** → `CO_QUAN_THAM_QUYEN` (span: `[8:11]`)
- `[e9]` **Thống đốc Ngân hàng Nhà nước** → `CO_QUAN_THAM_QUYEN` (span: `[29:32]`)
- `[e10]` **Thống đốc Ngân hàng Nhà nước** → `CO_QUAN_THAM_QUYEN` (span: `[52:55]`)
- `[e11]` **Quỹ bảo đảm an toàn hệ thống quỹ tín dụng nhân dân** → `TO_CHUC_DOANH_NGHIEP` (span: `[34:41]`)
- `[e12]` **quỹ tín dụng nhân dân** → `TO_CHUC_DOANH_NGHIEP` (span: `[57:60]`)

**Quan hệ:**
- (`e1` 06/2017/TT-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Ngân hàng Nhà nước Việt Nam `[CO_QUAN_BAN_HANH]`)
- (`e1` 06/2017/TT-NHNN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e5` sửa đổi , bổ sung một số điều của `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Thông tư số 03/2014/TT-NHNN `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 06/2017/TT-NHNN `[SO_HIEU]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Thông tư số 03/2014/TT-NHNN `[THAM_CHIEU_PHAP_LY]`)
- (`e5` sửa đổi , bổ sung một số điều của `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e4` Thông tư số 04/2015/TT-NHNN `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 06/2017/TT-NHNN `[SO_HIEU]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e4` Thông tư số 04/2015/TT-NHNN `[THAM_CHIEU_PHAP_LY]`)
- (`e3` Thông tư số 03/2014/TT-NHNN `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e6` ngày 23 tháng 01 năm 2014 `[NGAY_THAM_CHIEU]`)
- (`e4` Thông tư số 04/2015/TT-NHNN `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e7` ngày 31 tháng 3 năm 2015 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #06_2017_TT-NHNN_122819#preamble_standalone_11 (Loại: `preamble_standalone`)
> **[Thống đốc Ngân hàng Nhà nước]`<CO_QUAN_THAM_QUYEN>`** ban hành Thông tư **[sửa đổi , bổ sung một số điều của]`<TU_KHOA_PHAP_LY>`** **[Thông tư số 03/2014/TT-NHNN]`<THAM_CHIEU_PHAP_LY>`** **[ngày 23 tháng 01 năm 2014]`<NGAY_THAM_CHIEU>`** của **[Thống đốc Ngân hàng Nhà nước]`<CO_QUAN_THAM_QUYEN>`** quy định về **[Quỹ bảo đảm an toàn hệ thống quỹ tín dụng nhân dân]`<TO_CHUC_DOANH_NGHIEP>`** và **[Thông tư số 04/2015/TT-NHNN]`<THAM_CHIEU_PHAP_LY>`** **[ngày 31 tháng 3 năm 2015]`<NGAY_THAM_CHIEU>`** của **[Thống đốc Ngân hàng Nhà nước]`<CO_QUAN_THAM_QUYEN>`** quy định về **[quỹ tín dụng nhân dân]`<TO_CHUC_DOANH_NGHIEP>`** .

**Thực thể:**
- `[e0]` **Thông tư số 03/2014/TT-NHNN** → `THAM_CHIEU_PHAP_LY` (span: `[11:14]`)
- `[e1]` **Thông tư số 04/2015/TT-NHNN** → `THAM_CHIEU_PHAP_LY` (span: `[34:37]`)
- `[e2]` **sửa đổi , bổ sung một số điều của** → `TU_KHOA_PHAP_LY` (span: `[5:11]`)
- `[e3]` **ngày 23 tháng 01 năm 2014** → `NGAY_THAM_CHIEU` (span: `[14:20]`)
- `[e4]` **ngày 31 tháng 3 năm 2015** → `NGAY_THAM_CHIEU` (span: `[37:43]`)
- `[e5]` **Thống đốc Ngân hàng Nhà nước** → `CO_QUAN_THAM_QUYEN` (span: `[0:3]`)
- `[e6]` **Thống đốc Ngân hàng Nhà nước** → `CO_QUAN_THAM_QUYEN` (span: `[21:24]`)
- `[e7]` **Thống đốc Ngân hàng Nhà nước** → `CO_QUAN_THAM_QUYEN` (span: `[44:47]`)
- `[e8]` **Quỹ bảo đảm an toàn hệ thống quỹ tín dụng nhân dân** → `TO_CHUC_DOANH_NGHIEP` (span: `[26:33]`)
- `[e9]` **quỹ tín dụng nhân dân** → `TO_CHUC_DOANH_NGHIEP` (span: `[49:52]`)

**Quan hệ:**
- (`e2` sửa đổi , bổ sung một số điều của `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e0` Thông tư số 03/2014/TT-NHNN `[THAM_CHIEU_PHAP_LY]`)
- (`e6` Thống đốc Ngân hàng Nhà nước `[CO_QUAN_THAM_QUYEN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e0` Thông tư số 03/2014/TT-NHNN `[THAM_CHIEU_PHAP_LY]`)
- (`e2` sửa đổi , bổ sung một số điều của `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e1` Thông tư số 04/2015/TT-NHNN `[THAM_CHIEU_PHAP_LY]`)
- (`e8` Quỹ bảo đảm an toàn hệ thống quỹ tín dụng nhân dân `[TO_CHUC_DOANH_NGHIEP]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e1` Thông tư số 04/2015/TT-NHNN `[THAM_CHIEU_PHAP_LY]`)
- (`e0` Thông tư số 03/2014/TT-NHNN `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e3` ngày 23 tháng 01 năm 2014 `[NGAY_THAM_CHIEU]`)
- (`e1` Thông tư số 04/2015/TT-NHNN `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e4` ngày 31 tháng 3 năm 2015 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #06_2017_TT-NHNN_122819#body_context_12 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[06/2017/TT-NHNN]`<SO_HIEU>`** của **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Thanh tra , giám sát ngân hàng]`<LINH_VUC>`** . **[Điều 1 . **[Sửa đổi]`<TU_KHOA_PHAP_LY>`** **[Điều 4 Thông tư số 03/2014/TT-NHNN]`<THAM_CHIEU_PHAP_LY>`** **[ngày 23/01/2014]`<NGAY_THAM_CHIEU>`** của **[Thống đốc Ngân hàng Nhà nước]`<CO_QUAN_THAM_QUYEN>`** quy định về **[Quỹ bảo đảm an toàn hệ thống quỹ tín dụng nhân dân]`<TO_CHUC_DOANH_NGHIEP>`** . **[Sửa đổi]`<TU_KHOA_PHAP_LY>`** **[khoản 2 Điều 4]`<THAM_CHIEU_PHAP_LY>`** như sau :]`<DIEU>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **06/2017/TT-NHNN** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_BAN_HANH` (span: `[4:7]`)
- `[e3]` **Thanh tra , giám sát ngân hàng** → `LINH_VUC` (span: `[9:13]`)
- `[e4]` **Điều 1 . Sửa đổi Điều 4 Thông tư số 03/2014/TT-NHNN ngày 23/01/2014 của Thống đốc Ngân hàng Nhà nước quy định về Quỹ bảo đảm an toàn hệ thống quỹ tín dụng nhân dân . Sửa đổi khoản 2 Điều 4 như sau :** → `DIEU` (span: `[14:47]`)
- `[e5]` **Điều 4 Thông tư số 03/2014/TT-NHNN** → `THAM_CHIEU_PHAP_LY` (span: `[18:23]`) *(lồng trong `e4` (`DIEU`))*
- `[e6]` **khoản 2 Điều 4** → `THAM_CHIEU_PHAP_LY` (span: `[40:44]`) *(lồng trong `e4` (`DIEU`))*
- `[e7]` **Sửa đổi** → `TU_KHOA_PHAP_LY` (span: `[17:18]`) *(lồng trong `e4` (`DIEU`))*
- `[e8]` **Sửa đổi** → `TU_KHOA_PHAP_LY` (span: `[39:40]`) *(lồng trong `e4` (`DIEU`))*
- `[e9]` **ngày 23/01/2014** → `NGAY_THAM_CHIEU` (span: `[23:25]`) *(lồng trong `e4` (`DIEU`))*
- `[e10]` **Thống đốc Ngân hàng Nhà nước** → `CO_QUAN_THAM_QUYEN` (span: `[26:29]`) *(lồng trong `e4` (`DIEU`))*
- `[e11]` **Quỹ bảo đảm an toàn hệ thống quỹ tín dụng nhân dân** → `TO_CHUC_DOANH_NGHIEP` (span: `[31:38]`) *(lồng trong `e4` (`DIEU`))*

**Quan hệ:**
- (`e1` 06/2017/TT-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Ngân hàng Nhà nước Việt Nam `[CO_QUAN_BAN_HANH]`)
- (`e1` 06/2017/TT-NHNN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 06/2017/TT-NHNN `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Thanh tra , giám sát ngân hàng `[LINH_VUC]`)
- (`e4` Điều 1 . Sửa đổi Điều 4 Thông tư số 03/2014/TT-NHNN ngày 23/01/2014 của Thống đốc Ngân hàng Nhà nước quy định về Quỹ bảo đảm an toàn hệ thống quỹ tín dụng nhân dân . Sửa đổi khoản 2 Điều 4 như sau : `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 06/2017/TT-NHNN `[SO_HIEU]`)
- (`e1` 06/2017/TT-NHNN `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Thanh tra , giám sát ngân hàng `[LINH_VUC]`)
- (`e4` Điều 1 . Sửa đổi Điều 4 Thông tư số 03/2014/TT-NHNN ngày 23/01/2014 của Thống đốc Ngân hàng Nhà nước quy định về Quỹ bảo đảm an toàn hệ thống quỹ tín dụng nhân dân . Sửa đổi khoản 2 Điều 4 như sau : `[DIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Thanh tra , giám sát ngân hàng `[LINH_VUC]`)
- (`e7` Sửa đổi `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e5` Điều 4 Thông tư số 03/2014/TT-NHNN `[THAM_CHIEU_PHAP_LY]`)
- (`e4` Điều 1 . Sửa đổi Điều 4 Thông tư số 03/2014/TT-NHNN ngày 23/01/2014 của Thống đốc Ngân hàng Nhà nước quy định về Quỹ bảo đảm an toàn hệ thống quỹ tín dụng nhân dân . Sửa đổi khoản 2 Điều 4 như sau : `[DIEU]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e5` Điều 4 Thông tư số 03/2014/TT-NHNN `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e8` Sửa đổi `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e6` khoản 2 Điều 4 `[THAM_CHIEU_PHAP_LY]`)
- (`e4` Điều 1 . Sửa đổi Điều 4 Thông tư số 03/2014/TT-NHNN ngày 23/01/2014 của Thống đốc Ngân hàng Nhà nước quy định về Quỹ bảo đảm an toàn hệ thống quỹ tín dụng nhân dân . Sửa đổi khoản 2 Điều 4 như sau : `[DIEU]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e6` khoản 2 Điều 4 `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e5` Điều 4 Thông tư số 03/2014/TT-NHNN `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e9` ngày 23/01/2014 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #06_2017_TT-NHNN_122819#body_standalone_13 (Loại: `body_standalone`)
> **[Điều 1 . **[Sửa đổi]`<TU_KHOA_PHAP_LY>`** **[Điều 4 Thông tư số 03/2014/TT-NHNN]`<THAM_CHIEU_PHAP_LY>`** **[ngày 23/01/2014]`<NGAY_THAM_CHIEU>`** của **[Thống đốc Ngân hàng Nhà nước]`<CO_QUAN_THAM_QUYEN>`** quy định về **[Quỹ bảo đảm an toàn hệ thống quỹ tín dụng nhân dân]`<TO_CHUC_DOANH_NGHIEP>`** . **[Sửa đổi]`<TU_KHOA_PHAP_LY>`** **[khoản 2 Điều 4]`<THAM_CHIEU_PHAP_LY>`** như sau :]`<DIEU>`**

**Thực thể:**
- `[e0]` **Điều 1 . Sửa đổi Điều 4 Thông tư số 03/2014/TT-NHNN ngày 23/01/2014 của Thống đốc Ngân hàng Nhà nước quy định về Quỹ bảo đảm an toàn hệ thống quỹ tín dụng nhân dân . Sửa đổi khoản 2 Điều 4 như sau :** → `DIEU` (span: `[0:33]`)
- `[e1]` **Điều 4 Thông tư số 03/2014/TT-NHNN** → `THAM_CHIEU_PHAP_LY` (span: `[4:9]`) *(lồng trong `e0` (`DIEU`))*
- `[e2]` **khoản 2 Điều 4** → `THAM_CHIEU_PHAP_LY` (span: `[26:30]`) *(lồng trong `e0` (`DIEU`))*
- `[e3]` **Sửa đổi** → `TU_KHOA_PHAP_LY` (span: `[3:4]`) *(lồng trong `e0` (`DIEU`))*
- `[e4]` **Sửa đổi** → `TU_KHOA_PHAP_LY` (span: `[25:26]`) *(lồng trong `e0` (`DIEU`))*
- `[e5]` **ngày 23/01/2014** → `NGAY_THAM_CHIEU` (span: `[9:11]`) *(lồng trong `e0` (`DIEU`))*
- `[e6]` **Thống đốc Ngân hàng Nhà nước** → `CO_QUAN_THAM_QUYEN` (span: `[12:15]`) *(lồng trong `e0` (`DIEU`))*
- `[e7]` **Quỹ bảo đảm an toàn hệ thống quỹ tín dụng nhân dân** → `TO_CHUC_DOANH_NGHIEP` (span: `[17:24]`) *(lồng trong `e0` (`DIEU`))*

**Quan hệ:**
- (`e3` Sửa đổi `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e1` Điều 4 Thông tư số 03/2014/TT-NHNN `[THAM_CHIEU_PHAP_LY]`)
- (`e0` Điều 1 . Sửa đổi Điều 4 Thông tư số 03/2014/TT-NHNN ngày 23/01/2014 của Thống đốc Ngân hàng Nhà nước quy định về Quỹ bảo đảm an toàn hệ thống quỹ tín dụng nhân dân . Sửa đổi khoản 2 Điều 4 như sau : `[DIEU]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e1` Điều 4 Thông tư số 03/2014/TT-NHNN `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e4` Sửa đổi `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e2` khoản 2 Điều 4 `[THAM_CHIEU_PHAP_LY]`)
- (`e0` Điều 1 . Sửa đổi Điều 4 Thông tư số 03/2014/TT-NHNN ngày 23/01/2014 của Thống đốc Ngân hàng Nhà nước quy định về Quỹ bảo đảm an toàn hệ thống quỹ tín dụng nhân dân . Sửa đổi khoản 2 Điều 4 như sau : `[DIEU]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e2` khoản 2 Điều 4 `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e1` Điều 4 Thông tư số 03/2014/TT-NHNN `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e5` ngày 23/01/2014 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #06_2017_TT-NHNN_122819#body_context_14 (Loại: `body_context`)
> **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[06/2017/TT-NHNN]`<SO_HIEU>`** . **[Điều 1 . **[Sửa đổi]`<TU_KHOA_PHAP_LY>`** **[Điều 4 Thông tư số 03/2014/TT-NHNN]`<THAM_CHIEU_PHAP_LY>`** **[ngày 23/01/2014]`<NGAY_THAM_CHIEU>`** của **[Thống đốc Ngân hàng Nhà nước]`<CO_QUAN_THAM_QUYEN>`** quy định về **[Quỹ bảo đảm an toàn hệ thống quỹ tín dụng nhân dân]`<TO_CHUC_DOANH_NGHIEP>`** . “ 2 . Việc trích nộp **[Quỹ bảo toàn]`<TO_CHUC_DOANH_NGHIEP>`** **[theo quy định tại]`<TU_KHOA_PHAP_LY>`** **[khoản 1 Điều này]`<THAM_CHIEU_PHAP_LY>`** được thực hiện như sau :]`<DIEU>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[4:5]`)
- `[e1]` **06/2017/TT-NHNN** → `SO_HIEU` (span: `[6:7]`)
- `[e2]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_BAN_HANH` (span: `[0:3]`)
- `[e3]` **Điều 1 . Sửa đổi Điều 4 Thông tư số 03/2014/TT-NHNN ngày 23/01/2014 của Thống đốc Ngân hàng Nhà nước quy định về Quỹ bảo đảm an toàn hệ thống quỹ tín dụng nhân dân . “ 2 . Việc trích nộp Quỹ bảo toàn theo quy định tại khoản 1 Điều này được thực hiện như sau :** → `DIEU` (span: `[8:53]`)
- `[e4]` **Điều 4 Thông tư số 03/2014/TT-NHNN** → `THAM_CHIEU_PHAP_LY` (span: `[12:17]`) *(lồng trong `e3` (`DIEU`))*
- `[e5]` **khoản 1 Điều này** → `THAM_CHIEU_PHAP_LY` (span: `[44:48]`) *(lồng trong `e3` (`DIEU`))*
- `[e6]` **Sửa đổi** → `TU_KHOA_PHAP_LY` (span: `[11:12]`) *(lồng trong `e3` (`DIEU`))*
- `[e7]` **theo quy định tại** → `TU_KHOA_PHAP_LY` (span: `[41:44]`) *(lồng trong `e3` (`DIEU`))*
- `[e8]` **ngày 23/01/2014** → `NGAY_THAM_CHIEU` (span: `[17:19]`) *(lồng trong `e3` (`DIEU`))*
- `[e9]` **Thống đốc Ngân hàng Nhà nước** → `CO_QUAN_THAM_QUYEN` (span: `[20:23]`) *(lồng trong `e3` (`DIEU`))*
- `[e10]` **Quỹ bảo đảm an toàn hệ thống quỹ tín dụng nhân dân** → `TO_CHUC_DOANH_NGHIEP` (span: `[25:32]`) *(lồng trong `e3` (`DIEU`))*
- `[e11]` **Quỹ bảo toàn** → `TO_CHUC_DOANH_NGHIEP` (span: `[39:41]`) *(lồng trong `e3` (`DIEU`))*

**Quan hệ:**
- (`e1` 06/2017/TT-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Ngân hàng Nhà nước Việt Nam `[CO_QUAN_BAN_HANH]`)
- (`e1` 06/2017/TT-NHNN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 1 . Sửa đổi Điều 4 Thông tư số 03/2014/TT-NHNN ngày 23/01/2014 của Thống đốc Ngân hàng Nhà nước quy định về Quỹ bảo đảm an toàn hệ thống quỹ tín dụng nhân dân . “ 2 . Việc trích nộp Quỹ bảo toàn theo quy định tại khoản 1 Điều này được thực hiện như sau : `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 06/2017/TT-NHNN `[SO_HIEU]`)
- (`e6` Sửa đổi `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e4` Điều 4 Thông tư số 03/2014/TT-NHNN `[THAM_CHIEU_PHAP_LY]`)
- (`e3` Điều 1 . Sửa đổi Điều 4 Thông tư số 03/2014/TT-NHNN ngày 23/01/2014 của Thống đốc Ngân hàng Nhà nước quy định về Quỹ bảo đảm an toàn hệ thống quỹ tín dụng nhân dân . “ 2 . Việc trích nộp Quỹ bảo toàn theo quy định tại khoản 1 Điều này được thực hiện như sau : `[DIEU]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e4` Điều 4 Thông tư số 03/2014/TT-NHNN `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e7` theo quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e5` khoản 1 Điều này `[THAM_CHIEU_PHAP_LY]`)
- (`e3` Điều 1 . Sửa đổi Điều 4 Thông tư số 03/2014/TT-NHNN ngày 23/01/2014 của Thống đốc Ngân hàng Nhà nước quy định về Quỹ bảo đảm an toàn hệ thống quỹ tín dụng nhân dân . “ 2 . Việc trích nộp Quỹ bảo toàn theo quy định tại khoản 1 Điều này được thực hiện như sau : `[DIEU]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e5` khoản 1 Điều này `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e4` Điều 4 Thông tư số 03/2014/TT-NHNN `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e8` ngày 23/01/2014 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #06_2017_TT-NHNN_122819#body_standalone_15 (Loại: `body_standalone`)
> **[Điều 1 . **[Sửa đổi]`<TU_KHOA_PHAP_LY>`** **[Điều 4 Thông tư số 03/2014/TT-NHNN]`<THAM_CHIEU_PHAP_LY>`** **[ngày 23/01/2014]`<NGAY_THAM_CHIEU>`** của **[Thống đốc Ngân hàng Nhà nước]`<CO_QUAN_THAM_QUYEN>`** quy định về **[Quỹ bảo đảm an toàn hệ thống quỹ tín dụng nhân dân]`<TO_CHUC_DOANH_NGHIEP>`** . “ 2 . Việc trích nộp **[Quỹ bảo toàn]`<TO_CHUC_DOANH_NGHIEP>`** **[theo quy định tại]`<TU_KHOA_PHAP_LY>`** **[khoản 1 Điều này]`<THAM_CHIEU_PHAP_LY>`** được thực hiện như sau :]`<DIEU>`**

**Thực thể:**
- `[e0]` **Điều 1 . Sửa đổi Điều 4 Thông tư số 03/2014/TT-NHNN ngày 23/01/2014 của Thống đốc Ngân hàng Nhà nước quy định về Quỹ bảo đảm an toàn hệ thống quỹ tín dụng nhân dân . “ 2 . Việc trích nộp Quỹ bảo toàn theo quy định tại khoản 1 Điều này được thực hiện như sau :** → `DIEU` (span: `[0:45]`)
- `[e1]` **Điều 4 Thông tư số 03/2014/TT-NHNN** → `THAM_CHIEU_PHAP_LY` (span: `[4:9]`) *(lồng trong `e0` (`DIEU`))*
- `[e2]` **khoản 1 Điều này** → `THAM_CHIEU_PHAP_LY` (span: `[36:40]`) *(lồng trong `e0` (`DIEU`))*
- `[e3]` **Sửa đổi** → `TU_KHOA_PHAP_LY` (span: `[3:4]`) *(lồng trong `e0` (`DIEU`))*
- `[e4]` **theo quy định tại** → `TU_KHOA_PHAP_LY` (span: `[33:36]`) *(lồng trong `e0` (`DIEU`))*
- `[e5]` **ngày 23/01/2014** → `NGAY_THAM_CHIEU` (span: `[9:11]`) *(lồng trong `e0` (`DIEU`))*
- `[e6]` **Thống đốc Ngân hàng Nhà nước** → `CO_QUAN_THAM_QUYEN` (span: `[12:15]`) *(lồng trong `e0` (`DIEU`))*
- `[e7]` **Quỹ bảo đảm an toàn hệ thống quỹ tín dụng nhân dân** → `TO_CHUC_DOANH_NGHIEP` (span: `[17:24]`) *(lồng trong `e0` (`DIEU`))*
- `[e8]` **Quỹ bảo toàn** → `TO_CHUC_DOANH_NGHIEP` (span: `[31:33]`) *(lồng trong `e0` (`DIEU`))*

**Quan hệ:**
- (`e3` Sửa đổi `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e1` Điều 4 Thông tư số 03/2014/TT-NHNN `[THAM_CHIEU_PHAP_LY]`)
- (`e0` Điều 1 . Sửa đổi Điều 4 Thông tư số 03/2014/TT-NHNN ngày 23/01/2014 của Thống đốc Ngân hàng Nhà nước quy định về Quỹ bảo đảm an toàn hệ thống quỹ tín dụng nhân dân . “ 2 . Việc trích nộp Quỹ bảo toàn theo quy định tại khoản 1 Điều này được thực hiện như sau : `[DIEU]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e1` Điều 4 Thông tư số 03/2014/TT-NHNN `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e4` theo quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e2` khoản 1 Điều này `[THAM_CHIEU_PHAP_LY]`)
- (`e0` Điều 1 . Sửa đổi Điều 4 Thông tư số 03/2014/TT-NHNN ngày 23/01/2014 của Thống đốc Ngân hàng Nhà nước quy định về Quỹ bảo đảm an toàn hệ thống quỹ tín dụng nhân dân . “ 2 . Việc trích nộp Quỹ bảo toàn theo quy định tại khoản 1 Điều này được thực hiện như sau : `[DIEU]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e2` khoản 1 Điều này `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e1` Điều 4 Thông tư số 03/2014/TT-NHNN `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e5` ngày 23/01/2014 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #06_2017_TT-NHNN_122819#body_context_16 (Loại: `body_context`)
> **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[06/2017/TT-NHNN]`<SO_HIEU>`** . **[Điều 1]`<DIEU>`** . **[a ) Mức phí trích nộp hằng năm bằng **[0,08 %]`<NGUONG_DINH_LUONG>`** dư nợ cho vay bình quân năm liền kề trước kết thúc vào ngày 31/12 của **[ngân hàng hợp tác xã]`<TO_CHUC_DOANH_NGHIEP>`** , **[quỹ tín dụng nhân dân]`<TO_CHUC_DOANH_NGHIEP>`** . Dư nợ cho vay bình quân năm được tính bằng tổng dư nợ cho vay ( nhóm 1 và nhóm 2 theo quy định về phân loại nợ của **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_THAM_QUYEN>`** ) tại thời điểm cuối mỗi tháng trong năm chia cho số tháng phải tính thực tế . Riêng đối với ngân hàng hợp tác]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[4:5]`)
- `[e1]` **06/2017/TT-NHNN** → `SO_HIEU` (span: `[6:7]`)
- `[e2]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_BAN_HANH` (span: `[0:3]`)
- `[e3]` **Điều 1** → `DIEU` (span: `[8:10]`)
- `[e4]` **a ) Mức phí trích nộp hằng năm bằng 0,08 % dư nợ cho vay bình quân năm liền kề trước kết thúc vào ngày 31/12 của ngân hàng hợp tác xã , quỹ tín dụng nhân dân . Dư nợ cho vay bình quân năm được tính bằng tổng dư nợ cho vay ( nhóm 1 và nhóm 2 theo quy định về phân loại nợ của Ngân hàng Nhà nước Việt Nam ) tại thời điểm cuối mỗi tháng trong năm chia cho số tháng phải tính thực tế . Riêng đối với ngân hàng hợp tác** → `DIEM` (span: `[11:88]`)
- `[e5]` **0,08 %** → `NGUONG_DINH_LUONG` (span: `[20:22]`) *(lồng trong `e4` (`DIEM`))*
- `[e6]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_THAM_QUYEN` (span: `[65:68]`) *(lồng trong `e4` (`DIEM`))*
- `[e7]` **ngân hàng hợp tác xã** → `TO_CHUC_DOANH_NGHIEP` (span: `[35:37]`) *(lồng trong `e4` (`DIEM`))*
- `[e8]` **quỹ tín dụng nhân dân** → `TO_CHUC_DOANH_NGHIEP` (span: `[38:41]`) *(lồng trong `e4` (`DIEM`))*

**Quan hệ:**
- (`e1` 06/2017/TT-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Ngân hàng Nhà nước Việt Nam `[CO_QUAN_BAN_HANH]`)
- (`e1` 06/2017/TT-NHNN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 1 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 06/2017/TT-NHNN `[SO_HIEU]`)


---

### Mẫu #06_2017_TT-NHNN_122819#body_context_17 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[06/2017/TT-NHNN]`<SO_HIEU>`** của **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Thanh tra , giám sát ngân hàng]`<LINH_VUC>`** . **[Điều 1]`<DIEU>`** . **[b ) Việc trích nộp **[Quỹ bảo toàn]`<TO_CHUC_DOANH_NGHIEP>`** của năm tài chính chỉ được thực hiện khi tổng nguồn vốn hoạt động của **[Quỹ bảo toàn]`<TO_CHUC_DOANH_NGHIEP>`** trước khi trích nộp thấp hơn **[1,5 %]`<NGUONG_DINH_LUONG>`** tổng **[tài sản]`<TAI_SAN_VAT_CHAT>`** có của hệ thống **[quỹ tín dụng nhân dân]`<TO_CHUC_DOANH_NGHIEP>`** . Trường hợp , sau khi trích nộp **[Quỹ bảo toàn]`<TO_CHUC_DOANH_NGHIEP>`** của năm tài chính dẫn đến tổng nguồn vốn hoạt động của **[Quỹ bảo toàn]`<TO_CHUC_DOANH_NGHIEP>`** cao hơn hoặc bằng **[1,5 %]`<NGUONG_DINH_LUONG>`** tổng **[tài sản]`<TAI_SAN_VAT_CHAT>`** có của hệ thống **[quỹ tín dụng nhân dân]`<TO_CHUC_DOANH_NGHIEP>`** thì **[Ngân hàng Hợp tác xã]`<TO_CHUC_DOANH_NGHIEP>`** , Quỹ]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **06/2017/TT-NHNN** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_BAN_HANH` (span: `[4:7]`)
- `[e3]` **Thanh tra , giám sát ngân hàng** → `LINH_VUC` (span: `[9:13]`)
- `[e4]` **Điều 1** → `DIEU` (span: `[14:16]`)
- `[e5]` **b ) Việc trích nộp Quỹ bảo toàn của năm tài chính chỉ được thực hiện khi tổng nguồn vốn hoạt động của Quỹ bảo toàn trước khi trích nộp thấp hơn 1,5 % tổng tài sản có của hệ thống quỹ tín dụng nhân dân . Trường hợp , sau khi trích nộp Quỹ bảo toàn của năm tài chính dẫn đến tổng nguồn vốn hoạt động của Quỹ bảo toàn cao hơn hoặc bằng 1,5 % tổng tài sản có của hệ thống quỹ tín dụng nhân dân thì Ngân hàng Hợp tác xã , Quỹ** → `DIEM` (span: `[17:92]`)
- `[e6]` **1,5 %** → `NGUONG_DINH_LUONG` (span: `[43:45]`) *(lồng trong `e5` (`DIEM`))*
- `[e7]` **1,5 %** → `NGUONG_DINH_LUONG` (span: `[77:79]`) *(lồng trong `e5` (`DIEM`))*
- `[e8]` **Quỹ bảo toàn** → `TO_CHUC_DOANH_NGHIEP` (span: `[22:24]`) *(lồng trong `e5` (`DIEM`))*
- `[e9]` **Quỹ bảo toàn** → `TO_CHUC_DOANH_NGHIEP` (span: `[35:37]`) *(lồng trong `e5` (`DIEM`))*
- `[e10]` **quỹ tín dụng nhân dân** → `TO_CHUC_DOANH_NGHIEP` (span: `[50:53]`) *(lồng trong `e5` (`DIEM`))*
- `[e11]` **Quỹ bảo toàn** → `TO_CHUC_DOANH_NGHIEP` (span: `[60:62]`) *(lồng trong `e5` (`DIEM`))*
- `[e12]` **Quỹ bảo toàn** → `TO_CHUC_DOANH_NGHIEP` (span: `[71:73]`) *(lồng trong `e5` (`DIEM`))*
- `[e13]` **quỹ tín dụng nhân dân** → `TO_CHUC_DOANH_NGHIEP` (span: `[84:87]`) *(lồng trong `e5` (`DIEM`))*
- `[e14]` **Ngân hàng Hợp tác xã** → `TO_CHUC_DOANH_NGHIEP` (span: `[88:90]`) *(lồng trong `e5` (`DIEM`))*
- `[e15]` **tài sản** → `TAI_SAN_VAT_CHAT` (span: `[46:47]`) *(lồng trong `e5` (`DIEM`))*
- `[e16]` **tài sản** → `TAI_SAN_VAT_CHAT` (span: `[80:81]`) *(lồng trong `e5` (`DIEM`))*

**Quan hệ:**
- (`e1` 06/2017/TT-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Ngân hàng Nhà nước Việt Nam `[CO_QUAN_BAN_HANH]`)
- (`e1` 06/2017/TT-NHNN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 06/2017/TT-NHNN `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Thanh tra , giám sát ngân hàng `[LINH_VUC]`)
- (`e4` Điều 1 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 06/2017/TT-NHNN `[SO_HIEU]`)
- (`e1` 06/2017/TT-NHNN `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Thanh tra , giám sát ngân hàng `[LINH_VUC]`)
- (`e5` b ) Việc trích nộp Quỹ bảo toàn của năm tài chính chỉ được thực hiện khi tổng nguồn vốn hoạt động của Quỹ bảo toàn trước khi trích nộp thấp hơn 1,5 % tổng tài sản có của hệ thống quỹ tín dụng nhân dân . Trường hợp , sau khi trích nộp Quỹ bảo toàn của năm tài chính dẫn đến tổng nguồn vốn hoạt động của Quỹ bảo toàn cao hơn hoặc bằng 1,5 % tổng tài sản có của hệ thống quỹ tín dụng nhân dân thì Ngân hàng Hợp tác xã , Quỹ `[DIEM]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Thanh tra , giám sát ngân hàng `[LINH_VUC]`)


---

### Mẫu #06_2017_TT-NHNN_122819#body_context_18 (Loại: `body_context`)
> **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[06/2017/TT-NHNN]`<SO_HIEU>`** . **[Điều 1]`<DIEU>`** . **[c ) Số tiền trích nộp **[Quỹ bảo toàn]`<TO_CHUC_DOANH_NGHIEP>`** được hạch toán vào chi phí hoạt động của **[ngân hàng hợp tác xã]`<TO_CHUC_DOANH_NGHIEP>`** , **[quỹ tín dụng nhân dân]`<TO_CHUC_DOANH_NGHIEP>`** ” .]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[4:5]`)
- `[e1]` **06/2017/TT-NHNN** → `SO_HIEU` (span: `[6:7]`)
- `[e2]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_BAN_HANH` (span: `[0:3]`)
- `[e3]` **Điều 1** → `DIEU` (span: `[8:10]`)
- `[e4]` **c ) Số tiền trích nộp Quỹ bảo toàn được hạch toán vào chi phí hoạt động của ngân hàng hợp tác xã , quỹ tín dụng nhân dân ” .** → `DIEM` (span: `[11:33]`)
- `[e5]` **Quỹ bảo toàn** → `TO_CHUC_DOANH_NGHIEP` (span: `[17:19]`) *(lồng trong `e4` (`DIEM`))*
- `[e6]` **ngân hàng hợp tác xã** → `TO_CHUC_DOANH_NGHIEP` (span: `[25:27]`) *(lồng trong `e4` (`DIEM`))*
- `[e7]` **quỹ tín dụng nhân dân** → `TO_CHUC_DOANH_NGHIEP` (span: `[28:31]`) *(lồng trong `e4` (`DIEM`))*

**Quan hệ:**
- (`e1` 06/2017/TT-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Ngân hàng Nhà nước Việt Nam `[CO_QUAN_BAN_HANH]`)
- (`e1` 06/2017/TT-NHNN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 1 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 06/2017/TT-NHNN `[SO_HIEU]`)


---

### Mẫu #06_2017_TT-NHNN_122819#body_context_19 (Loại: `body_context`)
> **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[06/2017/TT-NHNN]`<SO_HIEU>`** . **[Điều 2 . **[Sửa đổi , bổ sung một số điều của]`<TU_KHOA_PHAP_LY>`** **[Thông tư số 04/2015/TT-NHNN]`<THAM_CHIEU_PHAP_LY>`** **[ngày 31/3/2015]`<NGAY_THAM_CHIEU>`** của **[Thống đốc Ngân hàng Nhà nước]`<CO_QUAN_THAM_QUYEN>`** quy định về **[quỹ tín dụng nhân dân]`<TO_CHUC_DOANH_NGHIEP>`**]`<DIEU>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[4:5]`)
- `[e1]` **06/2017/TT-NHNN** → `SO_HIEU` (span: `[6:7]`)
- `[e2]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_BAN_HANH` (span: `[0:3]`)
- `[e3]` **Điều 2 . Sửa đổi , bổ sung một số điều của Thông tư số 04/2015/TT-NHNN ngày 31/3/2015 của Thống đốc Ngân hàng Nhà nước quy định về quỹ tín dụng nhân dân** → `DIEU` (span: `[8:31]`)
- `[e4]` **Thông tư số 04/2015/TT-NHNN** → `THAM_CHIEU_PHAP_LY` (span: `[17:20]`) *(lồng trong `e3` (`DIEU`))*
- `[e5]` **Sửa đổi , bổ sung một số điều của** → `TU_KHOA_PHAP_LY` (span: `[11:17]`) *(lồng trong `e3` (`DIEU`))*
- `[e6]` **ngày 31/3/2015** → `NGAY_THAM_CHIEU` (span: `[20:22]`) *(lồng trong `e3` (`DIEU`))*
- `[e7]` **Thống đốc Ngân hàng Nhà nước** → `CO_QUAN_THAM_QUYEN` (span: `[23:26]`) *(lồng trong `e3` (`DIEU`))*
- `[e8]` **quỹ tín dụng nhân dân** → `TO_CHUC_DOANH_NGHIEP` (span: `[28:31]`) *(lồng trong `e3` (`DIEU`))*

**Quan hệ:**
- (`e1` 06/2017/TT-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Ngân hàng Nhà nước Việt Nam `[CO_QUAN_BAN_HANH]`)
- (`e1` 06/2017/TT-NHNN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 2 . Sửa đổi , bổ sung một số điều của Thông tư số 04/2015/TT-NHNN ngày 31/3/2015 của Thống đốc Ngân hàng Nhà nước quy định về quỹ tín dụng nhân dân `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 06/2017/TT-NHNN `[SO_HIEU]`)
- (`e5` Sửa đổi , bổ sung một số điều của `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e4` Thông tư số 04/2015/TT-NHNN `[THAM_CHIEU_PHAP_LY]`)
- (`e3` Điều 2 . Sửa đổi , bổ sung một số điều của Thông tư số 04/2015/TT-NHNN ngày 31/3/2015 của Thống đốc Ngân hàng Nhà nước quy định về quỹ tín dụng nhân dân `[DIEU]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e4` Thông tư số 04/2015/TT-NHNN `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e4` Thông tư số 04/2015/TT-NHNN `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e6` ngày 31/3/2015 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #06_2017_TT-NHNN_122819#body_standalone_20 (Loại: `body_standalone`)
> **[Điều 2 . **[Sửa đổi , bổ sung một số điều của]`<TU_KHOA_PHAP_LY>`** **[Thông tư số 04/2015/TT-NHNN]`<THAM_CHIEU_PHAP_LY>`** **[ngày 31/3/2015]`<NGAY_THAM_CHIEU>`** của **[Thống đốc Ngân hàng Nhà nước]`<CO_QUAN_THAM_QUYEN>`** quy định về **[quỹ tín dụng nhân dân]`<TO_CHUC_DOANH_NGHIEP>`**]`<DIEU>`**

**Thực thể:**
- `[e0]` **Điều 2 . Sửa đổi , bổ sung một số điều của Thông tư số 04/2015/TT-NHNN ngày 31/3/2015 của Thống đốc Ngân hàng Nhà nước quy định về quỹ tín dụng nhân dân** → `DIEU` (span: `[0:23]`)
- `[e1]` **Thông tư số 04/2015/TT-NHNN** → `THAM_CHIEU_PHAP_LY` (span: `[9:12]`) *(lồng trong `e0` (`DIEU`))*
- `[e2]` **Sửa đổi , bổ sung một số điều của** → `TU_KHOA_PHAP_LY` (span: `[3:9]`) *(lồng trong `e0` (`DIEU`))*
- `[e3]` **ngày 31/3/2015** → `NGAY_THAM_CHIEU` (span: `[12:14]`) *(lồng trong `e0` (`DIEU`))*
- `[e4]` **Thống đốc Ngân hàng Nhà nước** → `CO_QUAN_THAM_QUYEN` (span: `[15:18]`) *(lồng trong `e0` (`DIEU`))*
- `[e5]` **quỹ tín dụng nhân dân** → `TO_CHUC_DOANH_NGHIEP` (span: `[20:23]`) *(lồng trong `e0` (`DIEU`))*

**Quan hệ:**
- (`e2` Sửa đổi , bổ sung một số điều của `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e1` Thông tư số 04/2015/TT-NHNN `[THAM_CHIEU_PHAP_LY]`)
- (`e0` Điều 2 . Sửa đổi , bổ sung một số điều của Thông tư số 04/2015/TT-NHNN ngày 31/3/2015 của Thống đốc Ngân hàng Nhà nước quy định về quỹ tín dụng nhân dân `[DIEU]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e1` Thông tư số 04/2015/TT-NHNN `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e1` Thông tư số 04/2015/TT-NHNN `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e3` ngày 31/3/2015 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #06_2017_TT-NHNN_122819#body_context_21 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[06/2017/TT-NHNN]`<SO_HIEU>`** của **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Thanh tra , giám sát ngân hàng]`<LINH_VUC>`** . **[Điều 2]`<DIEU>`** . **[1 . **[Sửa đổi]`<TU_KHOA_PHAP_LY>`** **[khoản 7 Điều 11]`<THAM_CHIEU_PHAP_LY>`** như sau : “ 7 . Bản sao **[giấy chứng minh nhân dân]`<GIAY_TO_HO_SO>`** hoặc **[hộ chiếu]`<GIAY_TO_HO_SO>`** hoặc **[thẻ căn cước công dân]`<GIAY_TO_HO_SO>`** ( đối với thành viên là cá nhân , **[người đại diện của pháp nhân]`<CHU_THE_CA_NHAN>`** , **[hộ gia đình]`<TO_CHUC_DOANH_NGHIEP>`** ) còn hiệu lực . Đối với thành viên là **[cán bộ , công chức , viên chức]`<CHU_THE_CA_NHAN>`** phải có thêm **[giấy xác nhận nơi công tác]`<GIAY_TO_HO_SO>`** , bản sao quyết định tuyển dụn g hoặc **[hợp đồng tuyển dụng]`<GIAY_TO_HO_SO>`** của cơ quan , đơn vị tuyển dụng ” .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **06/2017/TT-NHNN** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_BAN_HANH` (span: `[4:7]`)
- `[e3]` **Thanh tra , giám sát ngân hàng** → `LINH_VUC` (span: `[9:13]`)
- `[e4]` **Điều 2** → `DIEU` (span: `[14:16]`)
- `[e5]` **1 . Sửa đổi khoản 7 Điều 11 như sau : “ 7 . Bản sao giấy chứng minh nhân dân hoặc hộ chiếu hoặc thẻ căn cước công dân ( đối với thành viên là cá nhân , người đại diện của pháp nhân , hộ gia đình ) còn hiệu lực . Đối với thành viên là cán bộ , công chức , viên chức phải có thêm giấy xác nhận nơi công tác , bản sao quyết định tuyển dụn g hoặc hợp đồng tuyển dụng của cơ quan , đơn vị tuyển dụng ” .** → `KHOAN` (span: `[17:88]`)
- `[e6]` **khoản 7 Điều 11** → `THAM_CHIEU_PHAP_LY` (span: `[20:24]`) *(lồng trong `e5` (`KHOAN`))*
- `[e7]` **Sửa đổi** → `TU_KHOA_PHAP_LY` (span: `[19:20]`) *(lồng trong `e5` (`KHOAN`))*
- `[e8]` **giấy chứng minh nhân dân** → `GIAY_TO_HO_SO` (span: `[31:34]`) *(lồng trong `e5` (`KHOAN`))*
- `[e9]` **hộ chiếu** → `GIAY_TO_HO_SO` (span: `[35:36]`) *(lồng trong `e5` (`KHOAN`))*
- `[e10]` **thẻ căn cước công dân** → `GIAY_TO_HO_SO` (span: `[37:40]`) *(lồng trong `e5` (`KHOAN`))*
- `[e11]` **giấy xác nhận nơi công tác** → `GIAY_TO_HO_SO` (span: `[68:72]`) *(lồng trong `e5` (`KHOAN`))*
- `[e12]` **hợp đồng tuyển dụng** → `GIAY_TO_HO_SO` (span: `[79:81]`) *(lồng trong `e5` (`KHOAN`))*
- `[e13]` **hộ gia đình** → `TO_CHUC_DOANH_NGHIEP` (span: `[51:53]`) *(lồng trong `e5` (`KHOAN`))*
- `[e14]` **người đại diện của pháp nhân** → `CHU_THE_CA_NHAN` (span: `[46:50]`) *(lồng trong `e5` (`KHOAN`))*
- `[e15]` **cán bộ , công chức , viên chức** → `CHU_THE_CA_NHAN` (span: `[60:65]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 06/2017/TT-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Ngân hàng Nhà nước Việt Nam `[CO_QUAN_BAN_HANH]`)
- (`e1` 06/2017/TT-NHNN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 06/2017/TT-NHNN `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Thanh tra , giám sát ngân hàng `[LINH_VUC]`)
- (`e4` Điều 2 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 06/2017/TT-NHNN `[SO_HIEU]`)
- (`e5` 1 . Sửa đổi khoản 7 Điều 11 như sau : “ 7 . Bản sao giấy chứng minh nhân dân hoặc hộ chiếu hoặc thẻ căn cước công dân ( đối với thành viên là cá nhân , người đại diện của pháp nhân , hộ gia đình ) còn hiệu lực . Đối với thành viên là cán bộ , công chức , viên chức phải có thêm giấy xác nhận nơi công tác , bản sao quyết định tuyển dụn g hoặc hợp đồng tuyển dụng của cơ quan , đơn vị tuyển dụng ” . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 2 `[DIEU]`)
- (`e1` 06/2017/TT-NHNN `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Thanh tra , giám sát ngân hàng `[LINH_VUC]`)
- (`e5` 1 . Sửa đổi khoản 7 Điều 11 như sau : “ 7 . Bản sao giấy chứng minh nhân dân hoặc hộ chiếu hoặc thẻ căn cước công dân ( đối với thành viên là cá nhân , người đại diện của pháp nhân , hộ gia đình ) còn hiệu lực . Đối với thành viên là cán bộ , công chức , viên chức phải có thêm giấy xác nhận nơi công tác , bản sao quyết định tuyển dụn g hoặc hợp đồng tuyển dụng của cơ quan , đơn vị tuyển dụng ” . `[KHOAN]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Thanh tra , giám sát ngân hàng `[LINH_VUC]`)
- (`e7` Sửa đổi `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e6` khoản 7 Điều 11 `[THAM_CHIEU_PHAP_LY]`)
- (`e5` 1 . Sửa đổi khoản 7 Điều 11 như sau : “ 7 . Bản sao giấy chứng minh nhân dân hoặc hộ chiếu hoặc thẻ căn cước công dân ( đối với thành viên là cá nhân , người đại diện của pháp nhân , hộ gia đình ) còn hiệu lực . Đối với thành viên là cán bộ , công chức , viên chức phải có thêm giấy xác nhận nơi công tác , bản sao quyết định tuyển dụn g hoặc hợp đồng tuyển dụng của cơ quan , đơn vị tuyển dụng ” . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e6` khoản 7 Điều 11 `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #06_2017_TT-NHNN_122819#body_standalone_22 (Loại: `body_standalone`)
> **[Điều 2]`<DIEU>`** . **[1 . **[Sửa đổi]`<TU_KHOA_PHAP_LY>`** **[khoản 7 Điều 11]`<THAM_CHIEU_PHAP_LY>`** như sau : “ 7 . Bản sao **[giấy chứng minh nhân dân]`<GIAY_TO_HO_SO>`** hoặc **[hộ chiếu]`<GIAY_TO_HO_SO>`** hoặc **[thẻ căn cước công dân]`<GIAY_TO_HO_SO>`** ( đối với thành viên là cá nhân , **[người đại diện của pháp nhân]`<CHU_THE_CA_NHAN>`** , **[hộ gia đình]`<TO_CHUC_DOANH_NGHIEP>`** ) còn hiệu lực . Đối với thành viên là **[cán bộ , công chức , viên chức]`<CHU_THE_CA_NHAN>`** phải có thêm **[giấy xác nhận nơi công tác]`<GIAY_TO_HO_SO>`** , bản sao quyết định tuyển dụn g hoặc **[hợp đồng tuyển dụng]`<GIAY_TO_HO_SO>`** của cơ quan , đơn vị tuyển dụng ” .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 2** → `DIEU` (span: `[0:2]`)
- `[e1]` **1 . Sửa đổi khoản 7 Điều 11 như sau : “ 7 . Bản sao giấy chứng minh nhân dân hoặc hộ chiếu hoặc thẻ căn cước công dân ( đối với thành viên là cá nhân , người đại diện của pháp nhân , hộ gia đình ) còn hiệu lực . Đối với thành viên là cán bộ , công chức , viên chức phải có thêm giấy xác nhận nơi công tác , bản sao quyết định tuyển dụn g hoặc hợp đồng tuyển dụng của cơ quan , đơn vị tuyển dụng ” .** → `KHOAN` (span: `[3:74]`)
- `[e2]` **khoản 7 Điều 11** → `THAM_CHIEU_PHAP_LY` (span: `[6:10]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **Sửa đổi** → `TU_KHOA_PHAP_LY` (span: `[5:6]`) *(lồng trong `e1` (`KHOAN`))*
- `[e4]` **giấy chứng minh nhân dân** → `GIAY_TO_HO_SO` (span: `[17:20]`) *(lồng trong `e1` (`KHOAN`))*
- `[e5]` **hộ chiếu** → `GIAY_TO_HO_SO` (span: `[21:22]`) *(lồng trong `e1` (`KHOAN`))*
- `[e6]` **thẻ căn cước công dân** → `GIAY_TO_HO_SO` (span: `[23:26]`) *(lồng trong `e1` (`KHOAN`))*
- `[e7]` **giấy xác nhận nơi công tác** → `GIAY_TO_HO_SO` (span: `[54:58]`) *(lồng trong `e1` (`KHOAN`))*
- `[e8]` **hợp đồng tuyển dụng** → `GIAY_TO_HO_SO` (span: `[65:67]`) *(lồng trong `e1` (`KHOAN`))*
- `[e9]` **hộ gia đình** → `TO_CHUC_DOANH_NGHIEP` (span: `[37:39]`) *(lồng trong `e1` (`KHOAN`))*
- `[e10]` **người đại diện của pháp nhân** → `CHU_THE_CA_NHAN` (span: `[32:36]`) *(lồng trong `e1` (`KHOAN`))*
- `[e11]` **cán bộ , công chức , viên chức** → `CHU_THE_CA_NHAN` (span: `[46:51]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 1 . Sửa đổi khoản 7 Điều 11 như sau : “ 7 . Bản sao giấy chứng minh nhân dân hoặc hộ chiếu hoặc thẻ căn cước công dân ( đối với thành viên là cá nhân , người đại diện của pháp nhân , hộ gia đình ) còn hiệu lực . Đối với thành viên là cán bộ , công chức , viên chức phải có thêm giấy xác nhận nơi công tác , bản sao quyết định tuyển dụn g hoặc hợp đồng tuyển dụng của cơ quan , đơn vị tuyển dụng ” . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 2 `[DIEU]`)
- (`e3` Sửa đổi `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e2` khoản 7 Điều 11 `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 1 . Sửa đổi khoản 7 Điều 11 như sau : “ 7 . Bản sao giấy chứng minh nhân dân hoặc hộ chiếu hoặc thẻ căn cước công dân ( đối với thành viên là cá nhân , người đại diện của pháp nhân , hộ gia đình ) còn hiệu lực . Đối với thành viên là cán bộ , công chức , viên chức phải có thêm giấy xác nhận nơi công tác , bản sao quyết định tuyển dụn g hoặc hợp đồng tuyển dụng của cơ quan , đơn vị tuyển dụng ” . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e2` khoản 7 Điều 11 `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #06_2017_TT-NHNN_122819#body_context_23 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[06/2017/TT-NHNN]`<SO_HIEU>`** của **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Thanh tra , giám sát ngân hàng]`<LINH_VUC>`** . **[Điều 2]`<DIEU>`** . **[2 . **[Sửa đổi]`<TU_KHOA_PHAP_LY>`** **[điểm đ khoản 4 Điều 15]`<THAM_CHIEU_PHAP_LY>`** như sau : ‟ đ ) Có các quy định nội bộ **[theo quy định tại]`<TU_KHOA_PHAP_LY>`** **[khoản 2 Điều 93 Luật Các tổ chức tín dụng]`<THAM_CHIEU_PHAP_LY>`** và các quy định về tổ chức và hoạt động của **[Hội đồng quản trị]`<TO_CHUC_DOANH_NGHIEP>`** , **[Ban kiểm soát]`<TO_CHUC_DOANH_NGHIEP>`** **[quỹ tín dụng nhân dân]`<TO_CHUC_DOANH_NGHIEP>`** ” .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **06/2017/TT-NHNN** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_BAN_HANH` (span: `[4:7]`)
- `[e3]` **Thanh tra , giám sát ngân hàng** → `LINH_VUC` (span: `[9:13]`)
- `[e4]` **Điều 2** → `DIEU` (span: `[14:16]`)
- `[e5]` **2 . Sửa đổi điểm đ khoản 4 Điều 15 như sau : ‟ đ ) Có các quy định nội bộ theo quy định tại khoản 2 Điều 93 Luật Các tổ chức tín dụng và các quy định về tổ chức và hoạt động của Hội đồng quản trị , Ban kiểm soát quỹ tín dụng nhân dân ” .** → `KHOAN` (span: `[17:65]`)
- `[e6]` **điểm đ khoản 4 Điều 15** → `THAM_CHIEU_PHAP_LY` (span: `[20:26]`) *(lồng trong `e5` (`KHOAN`))*
- `[e7]` **khoản 2 Điều 93 Luật Các tổ chức tín dụng** → `THAM_CHIEU_PHAP_LY` (span: `[39:47]`) *(lồng trong `e5` (`KHOAN`))*
- `[e8]` **Sửa đổi** → `TU_KHOA_PHAP_LY` (span: `[19:20]`) *(lồng trong `e5` (`KHOAN`))*
- `[e9]` **theo quy định tại** → `TU_KHOA_PHAP_LY` (span: `[36:39]`) *(lồng trong `e5` (`KHOAN`))*
- `[e10]` **Hội đồng quản trị** → `TO_CHUC_DOANH_NGHIEP` (span: `[55:57]`) *(lồng trong `e5` (`KHOAN`))*
- `[e11]` **Ban kiểm soát** → `TO_CHUC_DOANH_NGHIEP` (span: `[58:60]`) *(lồng trong `e5` (`KHOAN`))*
- `[e12]` **quỹ tín dụng nhân dân** → `TO_CHUC_DOANH_NGHIEP` (span: `[60:63]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 06/2017/TT-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Ngân hàng Nhà nước Việt Nam `[CO_QUAN_BAN_HANH]`)
- (`e1` 06/2017/TT-NHNN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 06/2017/TT-NHNN `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Thanh tra , giám sát ngân hàng `[LINH_VUC]`)
- (`e4` Điều 2 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 06/2017/TT-NHNN `[SO_HIEU]`)
- (`e5` 2 . Sửa đổi điểm đ khoản 4 Điều 15 như sau : ‟ đ ) Có các quy định nội bộ theo quy định tại khoản 2 Điều 93 Luật Các tổ chức tín dụng và các quy định về tổ chức và hoạt động của Hội đồng quản trị , Ban kiểm soát quỹ tín dụng nhân dân ” . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 2 `[DIEU]`)
- (`e1` 06/2017/TT-NHNN `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Thanh tra , giám sát ngân hàng `[LINH_VUC]`)
- (`e5` 2 . Sửa đổi điểm đ khoản 4 Điều 15 như sau : ‟ đ ) Có các quy định nội bộ theo quy định tại khoản 2 Điều 93 Luật Các tổ chức tín dụng và các quy định về tổ chức và hoạt động của Hội đồng quản trị , Ban kiểm soát quỹ tín dụng nhân dân ” . `[KHOAN]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Thanh tra , giám sát ngân hàng `[LINH_VUC]`)
- (`e8` Sửa đổi `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e6` điểm đ khoản 4 Điều 15 `[THAM_CHIEU_PHAP_LY]`)
- (`e5` 2 . Sửa đổi điểm đ khoản 4 Điều 15 như sau : ‟ đ ) Có các quy định nội bộ theo quy định tại khoản 2 Điều 93 Luật Các tổ chức tín dụng và các quy định về tổ chức và hoạt động của Hội đồng quản trị , Ban kiểm soát quỹ tín dụng nhân dân ” . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e6` điểm đ khoản 4 Điều 15 `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e9` theo quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e7` khoản 2 Điều 93 Luật Các tổ chức tín dụng `[THAM_CHIEU_PHAP_LY]`)
- (`e5` 2 . Sửa đổi điểm đ khoản 4 Điều 15 như sau : ‟ đ ) Có các quy định nội bộ theo quy định tại khoản 2 Điều 93 Luật Các tổ chức tín dụng và các quy định về tổ chức và hoạt động của Hội đồng quản trị , Ban kiểm soát quỹ tín dụng nhân dân ” . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e7` khoản 2 Điều 93 Luật Các tổ chức tín dụng `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #06_2017_TT-NHNN_122819#body_standalone_24 (Loại: `body_standalone`)
> **[Điều 2]`<DIEU>`** . **[2 . **[Sửa đổi]`<TU_KHOA_PHAP_LY>`** **[điểm đ khoản 4 Điều 15]`<THAM_CHIEU_PHAP_LY>`** như sau : ‟ đ ) Có các quy định nội bộ **[theo quy định tại]`<TU_KHOA_PHAP_LY>`** **[khoản 2 Điều 93 Luật Các tổ chức tín dụng]`<THAM_CHIEU_PHAP_LY>`** và các quy định về tổ chức và hoạt động của **[Hội đồng quản trị]`<TO_CHUC_DOANH_NGHIEP>`** , **[Ban kiểm soát]`<TO_CHUC_DOANH_NGHIEP>`** **[quỹ tín dụng nhân dân]`<TO_CHUC_DOANH_NGHIEP>`** ” .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 2** → `DIEU` (span: `[0:2]`)
- `[e1]` **2 . Sửa đổi điểm đ khoản 4 Điều 15 như sau : ‟ đ ) Có các quy định nội bộ theo quy định tại khoản 2 Điều 93 Luật Các tổ chức tín dụng và các quy định về tổ chức và hoạt động của Hội đồng quản trị , Ban kiểm soát quỹ tín dụng nhân dân ” .** → `KHOAN` (span: `[3:51]`)
- `[e2]` **điểm đ khoản 4 Điều 15** → `THAM_CHIEU_PHAP_LY` (span: `[6:12]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **khoản 2 Điều 93 Luật Các tổ chức tín dụng** → `THAM_CHIEU_PHAP_LY` (span: `[25:33]`) *(lồng trong `e1` (`KHOAN`))*
- `[e4]` **Sửa đổi** → `TU_KHOA_PHAP_LY` (span: `[5:6]`) *(lồng trong `e1` (`KHOAN`))*
- `[e5]` **theo quy định tại** → `TU_KHOA_PHAP_LY` (span: `[22:25]`) *(lồng trong `e1` (`KHOAN`))*
- `[e6]` **Hội đồng quản trị** → `TO_CHUC_DOANH_NGHIEP` (span: `[41:43]`) *(lồng trong `e1` (`KHOAN`))*
- `[e7]` **Ban kiểm soát** → `TO_CHUC_DOANH_NGHIEP` (span: `[44:46]`) *(lồng trong `e1` (`KHOAN`))*
- `[e8]` **quỹ tín dụng nhân dân** → `TO_CHUC_DOANH_NGHIEP` (span: `[46:49]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 2 . Sửa đổi điểm đ khoản 4 Điều 15 như sau : ‟ đ ) Có các quy định nội bộ theo quy định tại khoản 2 Điều 93 Luật Các tổ chức tín dụng và các quy định về tổ chức và hoạt động của Hội đồng quản trị , Ban kiểm soát quỹ tín dụng nhân dân ” . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 2 `[DIEU]`)
- (`e4` Sửa đổi `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e2` điểm đ khoản 4 Điều 15 `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 2 . Sửa đổi điểm đ khoản 4 Điều 15 như sau : ‟ đ ) Có các quy định nội bộ theo quy định tại khoản 2 Điều 93 Luật Các tổ chức tín dụng và các quy định về tổ chức và hoạt động của Hội đồng quản trị , Ban kiểm soát quỹ tín dụng nhân dân ” . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e2` điểm đ khoản 4 Điều 15 `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e5` theo quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` khoản 2 Điều 93 Luật Các tổ chức tín dụng `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 2 . Sửa đổi điểm đ khoản 4 Điều 15 như sau : ‟ đ ) Có các quy định nội bộ theo quy định tại khoản 2 Điều 93 Luật Các tổ chức tín dụng và các quy định về tổ chức và hoạt động của Hội đồng quản trị , Ban kiểm soát quỹ tín dụng nhân dân ” . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` khoản 2 Điều 93 Luật Các tổ chức tín dụng `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #06_2017_TT-NHNN_122819#body_context_25 (Loại: `body_context`)
> **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[06/2017/TT-NHNN]`<SO_HIEU>`** . **[Điều 2]`<DIEU>`** . **[3 . **[Sửa đổi]`<TU_KHOA_PHAP_LY>`** **[khoản 1 , khoản 2 Điều 31]`<THAM_CHIEU_PHAP_LY>`** như sau : “ 1 . Đối với cá nhân :]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[4:5]`)
- `[e1]` **06/2017/TT-NHNN** → `SO_HIEU` (span: `[6:7]`)
- `[e2]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_BAN_HANH` (span: `[0:3]`)
- `[e3]` **Điều 2** → `DIEU` (span: `[8:10]`)
- `[e4]` **3 . Sửa đổi khoản 1 , khoản 2 Điều 31 như sau : “ 1 . Đối với cá nhân :** → `KHOAN` (span: `[11:30]`)
- `[e5]` **khoản 1 , khoản 2 Điều 31** → `THAM_CHIEU_PHAP_LY` (span: `[14:21]`) *(lồng trong `e4` (`KHOAN`))*
- `[e6]` **Sửa đổi** → `TU_KHOA_PHAP_LY` (span: `[13:14]`) *(lồng trong `e4` (`KHOAN`))*

**Quan hệ:**
- (`e1` 06/2017/TT-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Ngân hàng Nhà nước Việt Nam `[CO_QUAN_BAN_HANH]`)
- (`e1` 06/2017/TT-NHNN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 2 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 06/2017/TT-NHNN `[SO_HIEU]`)
- (`e4` 3 . Sửa đổi khoản 1 , khoản 2 Điều 31 như sau : “ 1 . Đối với cá nhân : `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 2 `[DIEU]`)
- (`e6` Sửa đổi `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e5` khoản 1 , khoản 2 Điều 31 `[THAM_CHIEU_PHAP_LY]`)
- (`e4` 3 . Sửa đổi khoản 1 , khoản 2 Điều 31 như sau : “ 1 . Đối với cá nhân : `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e5` khoản 1 , khoản 2 Điều 31 `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #06_2017_TT-NHNN_122819#body_standalone_26 (Loại: `body_standalone`)
> **[Điều 2]`<DIEU>`** . **[3 . **[Sửa đổi]`<TU_KHOA_PHAP_LY>`** **[khoản 1 , khoản 2 Điều 31]`<THAM_CHIEU_PHAP_LY>`** như sau : “ 1 . Đối với cá nhân :]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 2** → `DIEU` (span: `[0:2]`)
- `[e1]` **3 . Sửa đổi khoản 1 , khoản 2 Điều 31 như sau : “ 1 . Đối với cá nhân :** → `KHOAN` (span: `[3:22]`)
- `[e2]` **khoản 1 , khoản 2 Điều 31** → `THAM_CHIEU_PHAP_LY` (span: `[6:13]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **Sửa đổi** → `TU_KHOA_PHAP_LY` (span: `[5:6]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 3 . Sửa đổi khoản 1 , khoản 2 Điều 31 như sau : “ 1 . Đối với cá nhân : `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 2 `[DIEU]`)
- (`e3` Sửa đổi `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e2` khoản 1 , khoản 2 Điều 31 `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 3 . Sửa đổi khoản 1 , khoản 2 Điều 31 như sau : “ 1 . Đối với cá nhân : `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e2` khoản 1 , khoản 2 Điều 31 `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #06_2017_TT-NHNN_122819#body_context_27 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[06/2017/TT-NHNN]`<SO_HIEU>`** của **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Thanh tra , giám sát ngân hàng]`<LINH_VUC>`** . **[Điều 2]`<DIEU>`** . **[Khoản 3 . “ 1 . Đối với cá nhân]`<KHOAN>`** : **[b ) **[Cán bộ , công chức , viên chức]`<CHU_THE_CA_NHAN>`** đang làm việc tại các tổ chức , cơ quan có trụ sở chính đóng **[trên địa bàn hoạt động]`<DIA_DIEM>`** của **[quỹ tín dụng nhân dân]`<TO_CHUC_DOANH_NGHIEP>`** . Thành viên của **[quỹ tín dụng nhân dân]`<TO_CHUC_DOANH_NGHIEP>`** là **[cán bộ , công chức , viên chức]`<CHU_THE_CA_NHAN>`** không được giữ các chức danh Chủ tịch và thành viên **[Hội đồng quản trị]`<TO_CHUC_DOANH_NGHIEP>`** ; Trưởng ban và thành viên **[Ban kiểm soát]`<TO_CHUC_DOANH_NGHIEP>`** ; **[Giám đốc]`<CHU_THE_CA_NHAN>`** , **[Phó giám đốc]`<CHU_THE_CA_NHAN>`** ; **[Kế toán trưởng]`<CHU_THE_CA_NHAN>`** và các chức danh chuyên]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **06/2017/TT-NHNN** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_BAN_HANH` (span: `[4:7]`)
- `[e3]` **Thanh tra , giám sát ngân hàng** → `LINH_VUC` (span: `[9:13]`)
- `[e4]` **Điều 2** → `DIEU` (span: `[14:16]`)
- `[e5]` **Khoản 3 . “ 1 . Đối với cá nhân** → `KHOAN` (span: `[17:25]`)
- `[e6]` **b ) Cán bộ , công chức , viên chức đang làm việc tại các tổ chức , cơ quan có trụ sở chính đóng trên địa bàn hoạt động của quỹ tín dụng nhân dân . Thành viên của quỹ tín dụng nhân dân là cán bộ , công chức , viên chức không được giữ các chức danh Chủ tịch và thành viên Hội đồng quản trị ; Trưởng ban và thành viên Ban kiểm soát ; Giám đốc , Phó giám đốc ; Kế toán trưởng và các chức danh chuyên** → `DIEM` (span: `[26:90]`)
- `[e7]` **quỹ tín dụng nhân dân** → `TO_CHUC_DOANH_NGHIEP` (span: `[48:51]`) *(lồng trong `e6` (`DIEM`))*
- `[e8]` **quỹ tín dụng nhân dân** → `TO_CHUC_DOANH_NGHIEP` (span: `[54:57]`) *(lồng trong `e6` (`DIEM`))*
- `[e9]` **Hội đồng quản trị** → `TO_CHUC_DOANH_NGHIEP` (span: `[71:73]`) *(lồng trong `e6` (`DIEM`))*
- `[e10]` **Ban kiểm soát** → `TO_CHUC_DOANH_NGHIEP` (span: `[78:80]`) *(lồng trong `e6` (`DIEM`))*
- `[e11]` **Cán bộ , công chức , viên chức** → `CHU_THE_CA_NHAN` (span: `[28:33]`) *(lồng trong `e6` (`DIEM`))*
- `[e12]` **cán bộ , công chức , viên chức** → `CHU_THE_CA_NHAN` (span: `[58:63]`) *(lồng trong `e6` (`DIEM`))*
- `[e13]` **Giám đốc** → `CHU_THE_CA_NHAN` (span: `[81:82]`) *(lồng trong `e6` (`DIEM`))*
- `[e14]` **Phó giám đốc** → `CHU_THE_CA_NHAN` (span: `[83:84]`) *(lồng trong `e6` (`DIEM`))*
- `[e15]` **Kế toán trưởng** → `CHU_THE_CA_NHAN` (span: `[85:86]`) *(lồng trong `e6` (`DIEM`))*
- `[e16]` **trên địa bàn hoạt động** → `DIA_DIEM` (span: `[44:47]`) *(lồng trong `e6` (`DIEM`))*

**Quan hệ:**
- (`e1` 06/2017/TT-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Ngân hàng Nhà nước Việt Nam `[CO_QUAN_BAN_HANH]`)
- (`e1` 06/2017/TT-NHNN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 06/2017/TT-NHNN `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Thanh tra , giám sát ngân hàng `[LINH_VUC]`)
- (`e4` Điều 2 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 06/2017/TT-NHNN `[SO_HIEU]`)
- (`e5` Khoản 3 . “ 1 . Đối với cá nhân `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 2 `[DIEU]`)
- (`e6` b ) Cán bộ , công chức , viên chức đang làm việc tại các tổ chức , cơ quan có trụ sở chính đóng trên địa bàn hoạt động của quỹ tín dụng nhân dân . Thành viên của quỹ tín dụng nhân dân là cán bộ , công chức , viên chức không được giữ các chức danh Chủ tịch và thành viên Hội đồng quản trị ; Trưởng ban và thành viên Ban kiểm soát ; Giám đốc , Phó giám đốc ; Kế toán trưởng và các chức danh chuyên `[DIEM]`) ==[ **THUOC_VE** ]==> (`e5` Khoản 3 . “ 1 . Đối với cá nhân `[KHOAN]`)
- (`e1` 06/2017/TT-NHNN `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Thanh tra , giám sát ngân hàng `[LINH_VUC]`)
- (`e6` b ) Cán bộ , công chức , viên chức đang làm việc tại các tổ chức , cơ quan có trụ sở chính đóng trên địa bàn hoạt động của quỹ tín dụng nhân dân . Thành viên của quỹ tín dụng nhân dân là cán bộ , công chức , viên chức không được giữ các chức danh Chủ tịch và thành viên Hội đồng quản trị ; Trưởng ban và thành viên Ban kiểm soát ; Giám đốc , Phó giám đốc ; Kế toán trưởng và các chức danh chuyên `[DIEM]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Thanh tra , giám sát ngân hàng `[LINH_VUC]`)


---

### Mẫu #06_2017_TT-NHNN_122819#body_standalone_28 (Loại: `body_standalone`)
> **[Điều 2]`<DIEU>`** . **[Khoản 3 . “ 1 . Đối với cá nhân]`<KHOAN>`** : **[b ) **[Cán bộ , công chức , viên chức]`<CHU_THE_CA_NHAN>`** đang làm việc tại các tổ chức , cơ quan có trụ sở chính đóng **[trên địa bàn hoạt động]`<DIA_DIEM>`** của **[quỹ tín dụng nhân dân]`<TO_CHUC_DOANH_NGHIEP>`** . Thành viên của **[quỹ tín dụng nhân dân]`<TO_CHUC_DOANH_NGHIEP>`** là **[cán bộ , công chức , viên chức]`<CHU_THE_CA_NHAN>`** không được giữ các chức danh Chủ tịch và thành viên **[Hội đồng quản trị]`<TO_CHUC_DOANH_NGHIEP>`** ; Trưởng ban và thành viên **[Ban kiểm soát]`<TO_CHUC_DOANH_NGHIEP>`** ; **[Giám đốc]`<CHU_THE_CA_NHAN>`** , **[Phó giám đốc]`<CHU_THE_CA_NHAN>`** ; **[Kế toán trưởng]`<CHU_THE_CA_NHAN>`** và các chức danh chuyên]`<DIEM>`**

**Thực thể:**
- `[e0]` **Điều 2** → `DIEU` (span: `[0:2]`)
- `[e1]` **Khoản 3 . “ 1 . Đối với cá nhân** → `KHOAN` (span: `[3:11]`)
- `[e2]` **b ) Cán bộ , công chức , viên chức đang làm việc tại các tổ chức , cơ quan có trụ sở chính đóng trên địa bàn hoạt động của quỹ tín dụng nhân dân . Thành viên của quỹ tín dụng nhân dân là cán bộ , công chức , viên chức không được giữ các chức danh Chủ tịch và thành viên Hội đồng quản trị ; Trưởng ban và thành viên Ban kiểm soát ; Giám đốc , Phó giám đốc ; Kế toán trưởng và các chức danh chuyên** → `DIEM` (span: `[12:76]`)
- `[e3]` **quỹ tín dụng nhân dân** → `TO_CHUC_DOANH_NGHIEP` (span: `[34:37]`) *(lồng trong `e2` (`DIEM`))*
- `[e4]` **quỹ tín dụng nhân dân** → `TO_CHUC_DOANH_NGHIEP` (span: `[40:43]`) *(lồng trong `e2` (`DIEM`))*
- `[e5]` **Hội đồng quản trị** → `TO_CHUC_DOANH_NGHIEP` (span: `[57:59]`) *(lồng trong `e2` (`DIEM`))*
- `[e6]` **Ban kiểm soát** → `TO_CHUC_DOANH_NGHIEP` (span: `[64:66]`) *(lồng trong `e2` (`DIEM`))*
- `[e7]` **Cán bộ , công chức , viên chức** → `CHU_THE_CA_NHAN` (span: `[14:19]`) *(lồng trong `e2` (`DIEM`))*
- `[e8]` **cán bộ , công chức , viên chức** → `CHU_THE_CA_NHAN` (span: `[44:49]`) *(lồng trong `e2` (`DIEM`))*
- `[e9]` **Giám đốc** → `CHU_THE_CA_NHAN` (span: `[67:68]`) *(lồng trong `e2` (`DIEM`))*
- `[e10]` **Phó giám đốc** → `CHU_THE_CA_NHAN` (span: `[69:70]`) *(lồng trong `e2` (`DIEM`))*
- `[e11]` **Kế toán trưởng** → `CHU_THE_CA_NHAN` (span: `[71:72]`) *(lồng trong `e2` (`DIEM`))*
- `[e12]` **trên địa bàn hoạt động** → `DIA_DIEM` (span: `[30:33]`) *(lồng trong `e2` (`DIEM`))*

**Quan hệ:**
- (`e1` Khoản 3 . “ 1 . Đối với cá nhân `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 2 `[DIEU]`)
- (`e2` b ) Cán bộ , công chức , viên chức đang làm việc tại các tổ chức , cơ quan có trụ sở chính đóng trên địa bàn hoạt động của quỹ tín dụng nhân dân . Thành viên của quỹ tín dụng nhân dân là cán bộ , công chức , viên chức không được giữ các chức danh Chủ tịch và thành viên Hội đồng quản trị ; Trưởng ban và thành viên Ban kiểm soát ; Giám đốc , Phó giám đốc ; Kế toán trưởng và các chức danh chuyên `[DIEM]`) ==[ **THUOC_VE** ]==> (`e1` Khoản 3 . “ 1 . Đối với cá nhân `[KHOAN]`)


---

### Mẫu #06_2017_TT-NHNN_122819#body_context_29 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[06/2017/TT-NHNN]`<SO_HIEU>`** ban hành **[ngày 05 tháng 07 năm 2017]`<NGAY_BAN_HANH>`** bởi **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_BAN_HANH>`** . **[Điều 2]`<DIEU>`** . **[Khoản 3 . “ 1 . Đối với cá nhân]`<KHOAN>`** : **[c ) Không thuộc các đối tượng sau đây : ( i ) Đang bị **[truy cứu trách nhiệm hình sự]`<HINH_PHAT_CHE_TAI>`** , đang phải chấp hành **[bản án]`<GIAY_TO_HO_SO>`** , quyết định về hình sự của **[tòa án]`<CO_QUAN_THAM_QUYEN>`** ; người đã bị kết án từ tội phạm nghiêm trọng trở lên mà chưa được xóa án tích ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **06/2017/TT-NHNN** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_BAN_HANH` (span: `[11:14]`)
- `[e3]` **ngày 05 tháng 07 năm 2017** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 2** → `DIEU` (span: `[15:17]`)
- `[e5]` **Khoản 3 . “ 1 . Đối với cá nhân** → `KHOAN` (span: `[18:26]`)
- `[e6]` **c ) Không thuộc các đối tượng sau đây : ( i ) Đang bị truy cứu trách nhiệm hình sự , đang phải chấp hành bản án , quyết định về hình sự của tòa án ; người đã bị kết án từ tội phạm nghiêm trọng trở lên mà chưa được xóa án tích ;** → `DIEM` (span: `[27:71]`)
- `[e7]` **truy cứu trách nhiệm hình sự** → `HINH_PHAT_CHE_TAI` (span: `[41:44]`) *(lồng trong `e6` (`DIEM`))*
- `[e8]` **tòa án** → `CO_QUAN_THAM_QUYEN` (span: `[54:55]`) *(lồng trong `e6` (`DIEM`))*
- `[e9]` **bản án** → `GIAY_TO_HO_SO` (span: `[48:49]`) *(lồng trong `e6` (`DIEM`))*

**Quan hệ:**
- (`e1` 06/2017/TT-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Ngân hàng Nhà nước Việt Nam `[CO_QUAN_BAN_HANH]`)
- (`e1` 06/2017/TT-NHNN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 06/2017/TT-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 05 tháng 07 năm 2017 `[NGAY_BAN_HANH]`)
- (`e4` Điều 2 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 06/2017/TT-NHNN `[SO_HIEU]`)
- (`e5` Khoản 3 . “ 1 . Đối với cá nhân `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 2 `[DIEU]`)
- (`e6` c ) Không thuộc các đối tượng sau đây : ( i ) Đang bị truy cứu trách nhiệm hình sự , đang phải chấp hành bản án , quyết định về hình sự của tòa án ; người đã bị kết án từ tội phạm nghiêm trọng trở lên mà chưa được xóa án tích ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e5` Khoản 3 . “ 1 . Đối với cá nhân `[KHOAN]`)
- (`e7` truy cứu trách nhiệm hình sự `[HINH_PHAT_CHE_TAI]`) ==[ **TAC_DONG_DOI_TUONG** ]==> (`e9` bản án `[GIAY_TO_HO_SO]`)


---

### Mẫu #06_2017_TT-NHNN_122819#body_standalone_30 (Loại: `body_standalone`)
> **[Điều 2]`<DIEU>`** . **[Khoản 3 . “ 1 . Đối với cá nhân]`<KHOAN>`** : **[c ) Không thuộc các đối tượng sau đây : ( i ) Đang bị **[truy cứu trách nhiệm hình sự]`<HINH_PHAT_CHE_TAI>`** , đang phải chấp hành **[bản án]`<GIAY_TO_HO_SO>`** , quyết định về hình sự của **[tòa án]`<CO_QUAN_THAM_QUYEN>`** ; người đã bị kết án từ tội phạm nghiêm trọng trở lên mà chưa được xóa án tích ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Điều 2** → `DIEU` (span: `[0:2]`)
- `[e1]` **Khoản 3 . “ 1 . Đối với cá nhân** → `KHOAN` (span: `[3:11]`)
- `[e2]` **c ) Không thuộc các đối tượng sau đây : ( i ) Đang bị truy cứu trách nhiệm hình sự , đang phải chấp hành bản án , quyết định về hình sự của tòa án ; người đã bị kết án từ tội phạm nghiêm trọng trở lên mà chưa được xóa án tích ;** → `DIEM` (span: `[12:56]`)
- `[e3]` **truy cứu trách nhiệm hình sự** → `HINH_PHAT_CHE_TAI` (span: `[26:29]`) *(lồng trong `e2` (`DIEM`))*
- `[e4]` **tòa án** → `CO_QUAN_THAM_QUYEN` (span: `[39:40]`) *(lồng trong `e2` (`DIEM`))*
- `[e5]` **bản án** → `GIAY_TO_HO_SO` (span: `[33:34]`) *(lồng trong `e2` (`DIEM`))*

**Quan hệ:**
- (`e1` Khoản 3 . “ 1 . Đối với cá nhân `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 2 `[DIEU]`)
- (`e2` c ) Không thuộc các đối tượng sau đây : ( i ) Đang bị truy cứu trách nhiệm hình sự , đang phải chấp hành bản án , quyết định về hình sự của tòa án ; người đã bị kết án từ tội phạm nghiêm trọng trở lên mà chưa được xóa án tích ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e1` Khoản 3 . “ 1 . Đối với cá nhân `[KHOAN]`)
- (`e3` truy cứu trách nhiệm hình sự `[HINH_PHAT_CHE_TAI]`) ==[ **TAC_DONG_DOI_TUONG** ]==> (`e5` bản án `[GIAY_TO_HO_SO]`)


---

### Mẫu #06_2017_TT-NHNN_122819#body_context_31 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[06/2017/TT-NHNN]`<SO_HIEU>`** của **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Thanh tra , giám sát ngân hàng]`<LINH_VUC>`** . **[Điều 2]`<DIEU>`** . **[Khoản 3]`<KHOAN>`** . **[( ii ) **[Cán bộ , công chức , viên chức]`<CHU_THE_CA_NHAN>`** làm việc ở những ngành , nghề có liên quan đến bí mật nhà nước theo quy định của pháp luật ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **06/2017/TT-NHNN** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_BAN_HANH` (span: `[4:7]`)
- `[e3]` **Thanh tra , giám sát ngân hàng** → `LINH_VUC` (span: `[9:13]`)
- `[e4]` **Điều 2** → `DIEU` (span: `[14:16]`)
- `[e5]` **Khoản 3** → `KHOAN` (span: `[17:19]`)
- `[e6]` **( ii ) Cán bộ , công chức , viên chức làm việc ở những ngành , nghề có liên quan đến bí mật nhà nước theo quy định của pháp luật ;** → `DIEM` (span: `[20:44]`)
- `[e7]` **Cán bộ , công chức , viên chức** → `CHU_THE_CA_NHAN` (span: `[23:28]`) *(lồng trong `e6` (`DIEM`))*

**Quan hệ:**
- (`e1` 06/2017/TT-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Ngân hàng Nhà nước Việt Nam `[CO_QUAN_BAN_HANH]`)
- (`e1` 06/2017/TT-NHNN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 06/2017/TT-NHNN `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Thanh tra , giám sát ngân hàng `[LINH_VUC]`)
- (`e4` Điều 2 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 06/2017/TT-NHNN `[SO_HIEU]`)
- (`e5` Khoản 3 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 2 `[DIEU]`)
- (`e6` ( ii ) Cán bộ , công chức , viên chức làm việc ở những ngành , nghề có liên quan đến bí mật nhà nước theo quy định của pháp luật ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e5` Khoản 3 `[KHOAN]`)
- (`e1` 06/2017/TT-NHNN `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Thanh tra , giám sát ngân hàng `[LINH_VUC]`)
- (`e6` ( ii ) Cán bộ , công chức , viên chức làm việc ở những ngành , nghề có liên quan đến bí mật nhà nước theo quy định của pháp luật ; `[DIEM]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Thanh tra , giám sát ngân hàng `[LINH_VUC]`)


---

### Mẫu #06_2017_TT-NHNN_122819#body_context_32 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[06/2017/TT-NHNN]`<SO_HIEU>`** ban hành **[ngày 05 tháng 07 năm 2017]`<NGAY_BAN_HANH>`** bởi **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_BAN_HANH>`** . **[Điều 2]`<DIEU>`** . **[Khoản 3 . “ 1 . Đối với cá nhân]`<KHOAN>`** : **[d ) Các điều kiện khác theo quy định của **[Điều lệ quỹ tín dụng nhân dân]`<GIAY_TO_HO_SO>`** .]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **06/2017/TT-NHNN** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_BAN_HANH` (span: `[11:14]`)
- `[e3]` **ngày 05 tháng 07 năm 2017** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 2** → `DIEU` (span: `[15:17]`)
- `[e5]` **Khoản 3 . “ 1 . Đối với cá nhân** → `KHOAN` (span: `[18:26]`)
- `[e6]` **d ) Các điều kiện khác theo quy định của Điều lệ quỹ tín dụng nhân dân .** → `DIEM` (span: `[27:40]`)
- `[e7]` **Điều lệ quỹ tín dụng nhân dân** → `GIAY_TO_HO_SO` (span: `[35:39]`) *(lồng trong `e6` (`DIEM`))*

**Quan hệ:**
- (`e1` 06/2017/TT-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Ngân hàng Nhà nước Việt Nam `[CO_QUAN_BAN_HANH]`)
- (`e1` 06/2017/TT-NHNN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 06/2017/TT-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 05 tháng 07 năm 2017 `[NGAY_BAN_HANH]`)
- (`e4` Điều 2 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 06/2017/TT-NHNN `[SO_HIEU]`)
- (`e5` Khoản 3 . “ 1 . Đối với cá nhân `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 2 `[DIEU]`)
- (`e6` d ) Các điều kiện khác theo quy định của Điều lệ quỹ tín dụng nhân dân . `[DIEM]`) ==[ **THUOC_VE** ]==> (`e5` Khoản 3 . “ 1 . Đối với cá nhân `[KHOAN]`)


---

### Mẫu #06_2017_TT-NHNN_122819#body_context_33 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[06/2017/TT-NHNN]`<SO_HIEU>`** của **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Thanh tra , giám sát ngân hàng]`<LINH_VUC>`** . **[Điều 2]`<DIEU>`** . **[Khoản 2]`<KHOAN>`** . **[a ) Là **[hộ gia đình]`<TO_CHUC_DOANH_NGHIEP>`** có các thành viên đăng ký thường trú **[trên địa bàn hoạt động]`<DIA_DIEM>`** của **[quỹ tín dụng nhân dân]`<TO_CHUC_DOANH_NGHIEP>`** ; các thành viên trong hộ có chung **[tài sản]`<TAI_SAN_VAT_CHAT>`** để phục vụ sản xuất , kinh doanh dịch vụ của **[hộ gia đình]`<TO_CHUC_DOANH_NGHIEP>`** ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **06/2017/TT-NHNN** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_BAN_HANH` (span: `[4:7]`)
- `[e3]` **Thanh tra , giám sát ngân hàng** → `LINH_VUC` (span: `[9:13]`)
- `[e4]` **Điều 2** → `DIEU` (span: `[14:16]`)
- `[e5]` **Khoản 2** → `KHOAN` (span: `[17:19]`)
- `[e6]` **a ) Là hộ gia đình có các thành viên đăng ký thường trú trên địa bàn hoạt động của quỹ tín dụng nhân dân ; các thành viên trong hộ có chung tài sản để phục vụ sản xuất , kinh doanh dịch vụ của hộ gia đình ;** → `DIEM` (span: `[20:55]`)
- `[e7]` **hộ gia đình** → `TO_CHUC_DOANH_NGHIEP` (span: `[23:25]`) *(lồng trong `e6` (`DIEM`))*
- `[e8]` **quỹ tín dụng nhân dân** → `TO_CHUC_DOANH_NGHIEP` (span: `[34:37]`) *(lồng trong `e6` (`DIEM`))*
- `[e9]` **hộ gia đình** → `TO_CHUC_DOANH_NGHIEP` (span: `[52:54]`) *(lồng trong `e6` (`DIEM`))*
- `[e10]` **tài sản** → `TAI_SAN_VAT_CHAT` (span: `[44:45]`) *(lồng trong `e6` (`DIEM`))*
- `[e11]` **trên địa bàn hoạt động** → `DIA_DIEM` (span: `[30:33]`) *(lồng trong `e6` (`DIEM`))*

**Quan hệ:**
- (`e1` 06/2017/TT-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Ngân hàng Nhà nước Việt Nam `[CO_QUAN_BAN_HANH]`)
- (`e1` 06/2017/TT-NHNN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 06/2017/TT-NHNN `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Thanh tra , giám sát ngân hàng `[LINH_VUC]`)
- (`e4` Điều 2 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 06/2017/TT-NHNN `[SO_HIEU]`)
- (`e5` Khoản 2 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 2 `[DIEU]`)
- (`e6` a ) Là hộ gia đình có các thành viên đăng ký thường trú trên địa bàn hoạt động của quỹ tín dụng nhân dân ; các thành viên trong hộ có chung tài sản để phục vụ sản xuất , kinh doanh dịch vụ của hộ gia đình ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e5` Khoản 2 `[KHOAN]`)
- (`e1` 06/2017/TT-NHNN `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Thanh tra , giám sát ngân hàng `[LINH_VUC]`)
- (`e6` a ) Là hộ gia đình có các thành viên đăng ký thường trú trên địa bàn hoạt động của quỹ tín dụng nhân dân ; các thành viên trong hộ có chung tài sản để phục vụ sản xuất , kinh doanh dịch vụ của hộ gia đình ; `[DIEM]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Thanh tra , giám sát ngân hàng `[LINH_VUC]`)


---

### Mẫu #06_2017_TT-NHNN_122819#body_standalone_34 (Loại: `body_standalone`)
> **[Điều 2]`<DIEU>`** . **[Khoản 2]`<KHOAN>`** . **[a ) Là **[hộ gia đình]`<TO_CHUC_DOANH_NGHIEP>`** có các thành viên đăng ký thường trú **[trên địa bàn hoạt động]`<DIA_DIEM>`** của **[quỹ tín dụng nhân dân]`<TO_CHUC_DOANH_NGHIEP>`** ; các thành viên trong hộ có chung **[tài sản]`<TAI_SAN_VAT_CHAT>`** để phục vụ sản xuất , kinh doanh dịch vụ của **[hộ gia đình]`<TO_CHUC_DOANH_NGHIEP>`** ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Điều 2** → `DIEU` (span: `[0:2]`)
- `[e1]` **Khoản 2** → `KHOAN` (span: `[3:5]`)
- `[e2]` **a ) Là hộ gia đình có các thành viên đăng ký thường trú trên địa bàn hoạt động của quỹ tín dụng nhân dân ; các thành viên trong hộ có chung tài sản để phục vụ sản xuất , kinh doanh dịch vụ của hộ gia đình ;** → `DIEM` (span: `[6:41]`)
- `[e3]` **hộ gia đình** → `TO_CHUC_DOANH_NGHIEP` (span: `[9:11]`) *(lồng trong `e2` (`DIEM`))*
- `[e4]` **quỹ tín dụng nhân dân** → `TO_CHUC_DOANH_NGHIEP` (span: `[20:23]`) *(lồng trong `e2` (`DIEM`))*
- `[e5]` **hộ gia đình** → `TO_CHUC_DOANH_NGHIEP` (span: `[38:40]`) *(lồng trong `e2` (`DIEM`))*
- `[e6]` **tài sản** → `TAI_SAN_VAT_CHAT` (span: `[30:31]`) *(lồng trong `e2` (`DIEM`))*
- `[e7]` **trên địa bàn hoạt động** → `DIA_DIEM` (span: `[16:19]`) *(lồng trong `e2` (`DIEM`))*

**Quan hệ:**
- (`e1` Khoản 2 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 2 `[DIEU]`)
- (`e2` a ) Là hộ gia đình có các thành viên đăng ký thường trú trên địa bàn hoạt động của quỹ tín dụng nhân dân ; các thành viên trong hộ có chung tài sản để phục vụ sản xuất , kinh doanh dịch vụ của hộ gia đình ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e1` Khoản 2 `[KHOAN]`)


---

### Mẫu #06_2017_TT-NHNN_122819#body_context_35 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[06/2017/TT-NHNN]`<SO_HIEU>`** ban hành **[ngày 05 tháng 07 năm 2017]`<NGAY_BAN_HANH>`** bởi **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_BAN_HANH>`** . **[Điều 2]`<DIEU>`** . **[Khoản 2]`<KHOAN>`** . **[b ) **[Người đại diện]`<CHU_THE_CA_NHAN>`** của **[hộ gia đình]`<TO_CHUC_DOANH_NGHIEP>`** phải được các thành viên của **[hộ gia đình]`<TO_CHUC_DOANH_NGHIEP>`** ủy quyền đại diện bằng văn bản theo quy định của pháp luật và phải đảm bảo các điều kiện **[theo quy định tại]`<TU_KHOA_PHAP_LY>`** **[khoản 1 Điều này]`<THAM_CHIEU_PHAP_LY>`** ” .]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **06/2017/TT-NHNN** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_BAN_HANH` (span: `[11:14]`)
- `[e3]` **ngày 05 tháng 07 năm 2017** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 2** → `DIEU` (span: `[15:17]`)
- `[e5]` **Khoản 2** → `KHOAN` (span: `[18:20]`)
- `[e6]` **b ) Người đại diện của hộ gia đình phải được các thành viên của hộ gia đình ủy quyền đại diện bằng văn bản theo quy định của pháp luật và phải đảm bảo các điều kiện theo quy định tại khoản 1 Điều này ” .** → `DIEM` (span: `[21:58]`)
- `[e7]` **khoản 1 Điều này** → `THAM_CHIEU_PHAP_LY` (span: `[52:56]`) *(lồng trong `e6` (`DIEM`))*
- `[e8]` **theo quy định tại** → `TU_KHOA_PHAP_LY` (span: `[49:52]`) *(lồng trong `e6` (`DIEM`))*
- `[e9]` **hộ gia đình** → `TO_CHUC_DOANH_NGHIEP` (span: `[26:28]`) *(lồng trong `e6` (`DIEM`))*
- `[e10]` **hộ gia đình** → `TO_CHUC_DOANH_NGHIEP` (span: `[33:35]`) *(lồng trong `e6` (`DIEM`))*
- `[e11]` **Người đại diện** → `CHU_THE_CA_NHAN` (span: `[23:25]`) *(lồng trong `e6` (`DIEM`))*

**Quan hệ:**
- (`e1` 06/2017/TT-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Ngân hàng Nhà nước Việt Nam `[CO_QUAN_BAN_HANH]`)
- (`e1` 06/2017/TT-NHNN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 06/2017/TT-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 05 tháng 07 năm 2017 `[NGAY_BAN_HANH]`)
- (`e4` Điều 2 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 06/2017/TT-NHNN `[SO_HIEU]`)
- (`e5` Khoản 2 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 2 `[DIEU]`)
- (`e6` b ) Người đại diện của hộ gia đình phải được các thành viên của hộ gia đình ủy quyền đại diện bằng văn bản theo quy định của pháp luật và phải đảm bảo các điều kiện theo quy định tại khoản 1 Điều này ” . `[DIEM]`) ==[ **THUOC_VE** ]==> (`e5` Khoản 2 `[KHOAN]`)
- (`e8` theo quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e7` khoản 1 Điều này `[THAM_CHIEU_PHAP_LY]`)
- (`e6` b ) Người đại diện của hộ gia đình phải được các thành viên của hộ gia đình ủy quyền đại diện bằng văn bản theo quy định của pháp luật và phải đảm bảo các điều kiện theo quy định tại khoản 1 Điều này ” . `[DIEM]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e7` khoản 1 Điều này `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #06_2017_TT-NHNN_122819#body_standalone_36 (Loại: `body_standalone`)
> **[Điều 2]`<DIEU>`** . **[Khoản 2]`<KHOAN>`** . **[b ) **[Người đại diện]`<CHU_THE_CA_NHAN>`** của **[hộ gia đình]`<TO_CHUC_DOANH_NGHIEP>`** phải được các thành viên của **[hộ gia đình]`<TO_CHUC_DOANH_NGHIEP>`** ủy quyền đại diện bằng văn bản theo quy định của pháp luật và phải đảm bảo các điều kiện **[theo quy định tại]`<TU_KHOA_PHAP_LY>`** **[khoản 1 Điều này]`<THAM_CHIEU_PHAP_LY>`** ” .]`<DIEM>`**

**Thực thể:**
- `[e0]` **Điều 2** → `DIEU` (span: `[0:2]`)
- `[e1]` **Khoản 2** → `KHOAN` (span: `[3:5]`)
- `[e2]` **b ) Người đại diện của hộ gia đình phải được các thành viên của hộ gia đình ủy quyền đại diện bằng văn bản theo quy định của pháp luật và phải đảm bảo các điều kiện theo quy định tại khoản 1 Điều này ” .** → `DIEM` (span: `[6:43]`)
- `[e3]` **khoản 1 Điều này** → `THAM_CHIEU_PHAP_LY` (span: `[37:41]`) *(lồng trong `e2` (`DIEM`))*
- `[e4]` **theo quy định tại** → `TU_KHOA_PHAP_LY` (span: `[34:37]`) *(lồng trong `e2` (`DIEM`))*
- `[e5]` **hộ gia đình** → `TO_CHUC_DOANH_NGHIEP` (span: `[11:13]`) *(lồng trong `e2` (`DIEM`))*
- `[e6]` **hộ gia đình** → `TO_CHUC_DOANH_NGHIEP` (span: `[18:20]`) *(lồng trong `e2` (`DIEM`))*
- `[e7]` **Người đại diện** → `CHU_THE_CA_NHAN` (span: `[8:10]`) *(lồng trong `e2` (`DIEM`))*

**Quan hệ:**
- (`e1` Khoản 2 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 2 `[DIEU]`)
- (`e2` b ) Người đại diện của hộ gia đình phải được các thành viên của hộ gia đình ủy quyền đại diện bằng văn bản theo quy định của pháp luật và phải đảm bảo các điều kiện theo quy định tại khoản 1 Điều này ” . `[DIEM]`) ==[ **THUOC_VE** ]==> (`e1` Khoản 2 `[KHOAN]`)
- (`e4` theo quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` khoản 1 Điều này `[THAM_CHIEU_PHAP_LY]`)
- (`e2` b ) Người đại diện của hộ gia đình phải được các thành viên của hộ gia đình ủy quyền đại diện bằng văn bản theo quy định của pháp luật và phải đảm bảo các điều kiện theo quy định tại khoản 1 Điều này ” . `[DIEM]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` khoản 1 Điều này `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #06_2017_TT-NHNN_122819#body_context_37 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[06/2017/TT-NHNN]`<SO_HIEU>`** của **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Thanh tra , giám sát ngân hàng]`<LINH_VUC>`** . **[Điều 2]`<DIEU>`** . **[4 . **[Sửa đổi]`<TU_KHOA_PHAP_LY>`** **[khoản 4 , khoản 5 Điều 37]`<THAM_CHIEU_PHAP_LY>`** như sau : “ 4 . **[Quỹ tín dụng nhân dân]`<TO_CHUC_DOANH_NGHIEP>`** cho vay đối với **[khách hàng]`<CHU_THE_CA_NHAN>`** là pháp nhân , cá nhân không phải là thành viên , có tiền gửi tại **[quỹ tín dụng nhân dân]`<TO_CHUC_DOANH_NGHIEP>`** trên cơ sở bảo đảm bằng sổ tiền gửi do chính **[quỹ tín dụng nhân dân]`<TO_CHUC_DOANH_NGHIEP>`** phát hành . Tổng số tiền cho vay không được vượt quá số dư của sổ tiền gửi tại thời điểm quyết định cho vay và thời hạn cho vay không được vượt quá]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **06/2017/TT-NHNN** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_BAN_HANH` (span: `[4:7]`)
- `[e3]` **Thanh tra , giám sát ngân hàng** → `LINH_VUC` (span: `[9:13]`)
- `[e4]` **Điều 2** → `DIEU` (span: `[14:16]`)
- `[e5]` **4 . Sửa đổi khoản 4 , khoản 5 Điều 37 như sau : “ 4 . Quỹ tín dụng nhân dân cho vay đối với khách hàng là pháp nhân , cá nhân không phải là thành viên , có tiền gửi tại quỹ tín dụng nhân dân trên cơ sở bảo đảm bằng sổ tiền gửi do chính quỹ tín dụng nhân dân phát hành . Tổng số tiền cho vay không được vượt quá số dư của sổ tiền gửi tại thời điểm quyết định cho vay và thời hạn cho vay không được vượt quá** → `KHOAN` (span: `[17:96]`)
- `[e6]` **khoản 4 , khoản 5 Điều 37** → `THAM_CHIEU_PHAP_LY` (span: `[20:27]`) *(lồng trong `e5` (`KHOAN`))*
- `[e7]` **Sửa đổi** → `TU_KHOA_PHAP_LY` (span: `[19:20]`) *(lồng trong `e5` (`KHOAN`))*
- `[e8]` **Quỹ tín dụng nhân dân** → `TO_CHUC_DOANH_NGHIEP` (span: `[33:36]`) *(lồng trong `e5` (`KHOAN`))*
- `[e9]` **quỹ tín dụng nhân dân** → `TO_CHUC_DOANH_NGHIEP` (span: `[53:56]`) *(lồng trong `e5` (`KHOAN`))*
- `[e10]` **quỹ tín dụng nhân dân** → `TO_CHUC_DOANH_NGHIEP` (span: `[65:68]`) *(lồng trong `e5` (`KHOAN`))*
- `[e11]` **khách hàng** → `CHU_THE_CA_NHAN` (span: `[39:40]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 06/2017/TT-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Ngân hàng Nhà nước Việt Nam `[CO_QUAN_BAN_HANH]`)
- (`e1` 06/2017/TT-NHNN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 06/2017/TT-NHNN `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Thanh tra , giám sát ngân hàng `[LINH_VUC]`)
- (`e4` Điều 2 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 06/2017/TT-NHNN `[SO_HIEU]`)
- (`e5` 4 . Sửa đổi khoản 4 , khoản 5 Điều 37 như sau : “ 4 . Quỹ tín dụng nhân dân cho vay đối với khách hàng là pháp nhân , cá nhân không phải là thành viên , có tiền gửi tại quỹ tín dụng nhân dân trên cơ sở bảo đảm bằng sổ tiền gửi do chính quỹ tín dụng nhân dân phát hành . Tổng số tiền cho vay không được vượt quá số dư của sổ tiền gửi tại thời điểm quyết định cho vay và thời hạn cho vay không được vượt quá `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 2 `[DIEU]`)
- (`e1` 06/2017/TT-NHNN `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Thanh tra , giám sát ngân hàng `[LINH_VUC]`)
- (`e5` 4 . Sửa đổi khoản 4 , khoản 5 Điều 37 như sau : “ 4 . Quỹ tín dụng nhân dân cho vay đối với khách hàng là pháp nhân , cá nhân không phải là thành viên , có tiền gửi tại quỹ tín dụng nhân dân trên cơ sở bảo đảm bằng sổ tiền gửi do chính quỹ tín dụng nhân dân phát hành . Tổng số tiền cho vay không được vượt quá số dư của sổ tiền gửi tại thời điểm quyết định cho vay và thời hạn cho vay không được vượt quá `[KHOAN]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Thanh tra , giám sát ngân hàng `[LINH_VUC]`)
- (`e7` Sửa đổi `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e6` khoản 4 , khoản 5 Điều 37 `[THAM_CHIEU_PHAP_LY]`)
- (`e5` 4 . Sửa đổi khoản 4 , khoản 5 Điều 37 như sau : “ 4 . Quỹ tín dụng nhân dân cho vay đối với khách hàng là pháp nhân , cá nhân không phải là thành viên , có tiền gửi tại quỹ tín dụng nhân dân trên cơ sở bảo đảm bằng sổ tiền gửi do chính quỹ tín dụng nhân dân phát hành . Tổng số tiền cho vay không được vượt quá số dư của sổ tiền gửi tại thời điểm quyết định cho vay và thời hạn cho vay không được vượt quá `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e6` khoản 4 , khoản 5 Điều 37 `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #06_2017_TT-NHNN_122819#body_standalone_38 (Loại: `body_standalone`)
> **[Điều 2]`<DIEU>`** . **[4 . **[Sửa đổi]`<TU_KHOA_PHAP_LY>`** **[khoản 4 , khoản 5 Điều 37]`<THAM_CHIEU_PHAP_LY>`** như sau : “ 4 . **[Quỹ tín dụng nhân dân]`<TO_CHUC_DOANH_NGHIEP>`** cho vay đối với **[khách hàng]`<CHU_THE_CA_NHAN>`** là pháp nhân , cá nhân không phải là thành viên , có tiền gửi tại **[quỹ tín dụng nhân dân]`<TO_CHUC_DOANH_NGHIEP>`** trên cơ sở bảo đảm bằng sổ tiền gửi do chính **[quỹ tín dụng nhân dân]`<TO_CHUC_DOANH_NGHIEP>`** phát hành . Tổng số tiền cho vay không được vượt quá số dư của sổ tiền gửi tại thời điểm quyết định cho vay và thời hạn cho vay không được vượt quá]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 2** → `DIEU` (span: `[0:2]`)
- `[e1]` **4 . Sửa đổi khoản 4 , khoản 5 Điều 37 như sau : “ 4 . Quỹ tín dụng nhân dân cho vay đối với khách hàng là pháp nhân , cá nhân không phải là thành viên , có tiền gửi tại quỹ tín dụng nhân dân trên cơ sở bảo đảm bằng sổ tiền gửi do chính quỹ tín dụng nhân dân phát hành . Tổng số tiền cho vay không được vượt quá số dư của sổ tiền gửi tại thời điểm quyết định cho vay và thời hạn cho vay không được vượt quá** → `KHOAN` (span: `[3:82]`)
- `[e2]` **khoản 4 , khoản 5 Điều 37** → `THAM_CHIEU_PHAP_LY` (span: `[6:13]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **Sửa đổi** → `TU_KHOA_PHAP_LY` (span: `[5:6]`) *(lồng trong `e1` (`KHOAN`))*
- `[e4]` **Quỹ tín dụng nhân dân** → `TO_CHUC_DOANH_NGHIEP` (span: `[19:22]`) *(lồng trong `e1` (`KHOAN`))*
- `[e5]` **quỹ tín dụng nhân dân** → `TO_CHUC_DOANH_NGHIEP` (span: `[39:42]`) *(lồng trong `e1` (`KHOAN`))*
- `[e6]` **quỹ tín dụng nhân dân** → `TO_CHUC_DOANH_NGHIEP` (span: `[51:54]`) *(lồng trong `e1` (`KHOAN`))*
- `[e7]` **khách hàng** → `CHU_THE_CA_NHAN` (span: `[25:26]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 4 . Sửa đổi khoản 4 , khoản 5 Điều 37 như sau : “ 4 . Quỹ tín dụng nhân dân cho vay đối với khách hàng là pháp nhân , cá nhân không phải là thành viên , có tiền gửi tại quỹ tín dụng nhân dân trên cơ sở bảo đảm bằng sổ tiền gửi do chính quỹ tín dụng nhân dân phát hành . Tổng số tiền cho vay không được vượt quá số dư của sổ tiền gửi tại thời điểm quyết định cho vay và thời hạn cho vay không được vượt quá `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 2 `[DIEU]`)
- (`e3` Sửa đổi `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e2` khoản 4 , khoản 5 Điều 37 `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 4 . Sửa đổi khoản 4 , khoản 5 Điều 37 như sau : “ 4 . Quỹ tín dụng nhân dân cho vay đối với khách hàng là pháp nhân , cá nhân không phải là thành viên , có tiền gửi tại quỹ tín dụng nhân dân trên cơ sở bảo đảm bằng sổ tiền gửi do chính quỹ tín dụng nhân dân phát hành . Tổng số tiền cho vay không được vượt quá số dư của sổ tiền gửi tại thời điểm quyết định cho vay và thời hạn cho vay không được vượt quá `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e2` khoản 4 , khoản 5 Điều 37 `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #06_2017_TT-NHNN_122819#body_context_39 (Loại: `body_context`)
> **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[06/2017/TT-NHNN]`<SO_HIEU>`** . **[Điều 2]`<DIEU>`** . **[5 . **[Quỹ tín dụng nhân dân]`<TO_CHUC_DOANH_NGHIEP>`** cho vay thành viên của **[hộ nghèo]`<TO_CHUC_DOANH_NGHIEP>`** có đăng ký thường trú **[trên địa bàn hoạt động]`<DIA_DIEM>`** của **[quỹ tín dụng nhân dân]`<TO_CHUC_DOANH_NGHIEP>`** trong trường hợp **[hộ nghèo]`<TO_CHUC_DOANH_NGHIEP>`** không phải là thành viên của **[quỹ tín dụng nhân dân]`<TO_CHUC_DOANH_NGHIEP>`** . Trường hợp nhiều thành viên của **[hộ nghèo]`<TO_CHUC_DOANH_NGHIEP>`** cùng vay vốn thì các thành viên của **[hộ nghèo]`<TO_CHUC_DOANH_NGHIEP>`** cùng ký hoặc ủy quyền cho một thành viên của **[hộ nghèo]`<TO_CHUC_DOANH_NGHIEP>`** đại diện ký thỏa thuận cho vay với **[quỹ tín dụng nhân dân]`<TO_CHUC_DOANH_NGHIEP>`** . **[Hộ nghèo]`<TO_CHUC_DOANH_NGHIEP>`** phải được]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[4:5]`)
- `[e1]` **06/2017/TT-NHNN** → `SO_HIEU` (span: `[6:7]`)
- `[e2]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_BAN_HANH` (span: `[0:3]`)
- `[e3]` **Điều 2** → `DIEU` (span: `[8:10]`)
- `[e4]` **5 . Quỹ tín dụng nhân dân cho vay thành viên của hộ nghèo có đăng ký thường trú trên địa bàn hoạt động của quỹ tín dụng nhân dân trong trường hợp hộ nghèo không phải là thành viên của quỹ tín dụng nhân dân . Trường hợp nhiều thành viên của hộ nghèo cùng vay vốn thì các thành viên của hộ nghèo cùng ký hoặc ủy quyền cho một thành viên của hộ nghèo đại diện ký thỏa thuận cho vay với quỹ tín dụng nhân dân . Hộ nghèo phải được** → `KHOAN` (span: `[11:85]`)
- `[e5]` **Quỹ tín dụng nhân dân** → `TO_CHUC_DOANH_NGHIEP` (span: `[13:16]`) *(lồng trong `e4` (`KHOAN`))*
- `[e6]` **hộ nghèo** → `TO_CHUC_DOANH_NGHIEP` (span: `[20:22]`) *(lồng trong `e4` (`KHOAN`))*
- `[e7]` **quỹ tín dụng nhân dân** → `TO_CHUC_DOANH_NGHIEP` (span: `[29:32]`) *(lồng trong `e4` (`KHOAN`))*
- `[e8]` **hộ nghèo** → `TO_CHUC_DOANH_NGHIEP` (span: `[34:36]`) *(lồng trong `e4` (`KHOAN`))*
- `[e9]` **quỹ tín dụng nhân dân** → `TO_CHUC_DOANH_NGHIEP` (span: `[41:44]`) *(lồng trong `e4` (`KHOAN`))*
- `[e10]` **hộ nghèo** → `TO_CHUC_DOANH_NGHIEP` (span: `[49:51]`) *(lồng trong `e4` (`KHOAN`))*
- `[e11]` **hộ nghèo** → `TO_CHUC_DOANH_NGHIEP` (span: `[58:60]`) *(lồng trong `e4` (`KHOAN`))*
- `[e12]` **hộ nghèo** → `TO_CHUC_DOANH_NGHIEP` (span: `[69:71]`) *(lồng trong `e4` (`KHOAN`))*
- `[e13]` **quỹ tín dụng nhân dân** → `TO_CHUC_DOANH_NGHIEP` (span: `[77:80]`) *(lồng trong `e4` (`KHOAN`))*
- `[e14]` **Hộ nghèo** → `TO_CHUC_DOANH_NGHIEP` (span: `[81:83]`) *(lồng trong `e4` (`KHOAN`))*
- `[e15]` **trên địa bàn hoạt động** → `DIA_DIEM` (span: `[25:28]`) *(lồng trong `e4` (`KHOAN`))*

**Quan hệ:**
- (`e1` 06/2017/TT-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Ngân hàng Nhà nước Việt Nam `[CO_QUAN_BAN_HANH]`)
- (`e1` 06/2017/TT-NHNN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 2 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 06/2017/TT-NHNN `[SO_HIEU]`)
- (`e4` 5 . Quỹ tín dụng nhân dân cho vay thành viên của hộ nghèo có đăng ký thường trú trên địa bàn hoạt động của quỹ tín dụng nhân dân trong trường hợp hộ nghèo không phải là thành viên của quỹ tín dụng nhân dân . Trường hợp nhiều thành viên của hộ nghèo cùng vay vốn thì các thành viên của hộ nghèo cùng ký hoặc ủy quyền cho một thành viên của hộ nghèo đại diện ký thỏa thuận cho vay với quỹ tín dụng nhân dân . Hộ nghèo phải được `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 2 `[DIEU]`)


---

### Mẫu #06_2017_TT-NHNN_122819#body_standalone_40 (Loại: `body_standalone`)
> **[Điều 2]`<DIEU>`** . **[5 . **[Quỹ tín dụng nhân dân]`<TO_CHUC_DOANH_NGHIEP>`** cho vay thành viên của **[hộ nghèo]`<TO_CHUC_DOANH_NGHIEP>`** có đăng ký thường trú **[trên địa bàn hoạt động]`<DIA_DIEM>`** của **[quỹ tín dụng nhân dân]`<TO_CHUC_DOANH_NGHIEP>`** trong trường hợp **[hộ nghèo]`<TO_CHUC_DOANH_NGHIEP>`** không phải là thành viên của **[quỹ tín dụng nhân dân]`<TO_CHUC_DOANH_NGHIEP>`** . Trường hợp nhiều thành viên của **[hộ nghèo]`<TO_CHUC_DOANH_NGHIEP>`** cùng vay vốn thì các thành viên của **[hộ nghèo]`<TO_CHUC_DOANH_NGHIEP>`** cùng ký hoặc ủy quyền cho một thành viên của **[hộ nghèo]`<TO_CHUC_DOANH_NGHIEP>`** đại diện ký thỏa thuận cho vay với **[quỹ tín dụng nhân dân]`<TO_CHUC_DOANH_NGHIEP>`** . **[Hộ nghèo]`<TO_CHUC_DOANH_NGHIEP>`** phải được]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 2** → `DIEU` (span: `[0:2]`)
- `[e1]` **5 . Quỹ tín dụng nhân dân cho vay thành viên của hộ nghèo có đăng ký thường trú trên địa bàn hoạt động của quỹ tín dụng nhân dân trong trường hợp hộ nghèo không phải là thành viên của quỹ tín dụng nhân dân . Trường hợp nhiều thành viên của hộ nghèo cùng vay vốn thì các thành viên của hộ nghèo cùng ký hoặc ủy quyền cho một thành viên của hộ nghèo đại diện ký thỏa thuận cho vay với quỹ tín dụng nhân dân . Hộ nghèo phải được** → `KHOAN` (span: `[3:77]`)
- `[e2]` **Quỹ tín dụng nhân dân** → `TO_CHUC_DOANH_NGHIEP` (span: `[5:8]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **hộ nghèo** → `TO_CHUC_DOANH_NGHIEP` (span: `[12:14]`) *(lồng trong `e1` (`KHOAN`))*
- `[e4]` **quỹ tín dụng nhân dân** → `TO_CHUC_DOANH_NGHIEP` (span: `[21:24]`) *(lồng trong `e1` (`KHOAN`))*
- `[e5]` **hộ nghèo** → `TO_CHUC_DOANH_NGHIEP` (span: `[26:28]`) *(lồng trong `e1` (`KHOAN`))*
- `[e6]` **quỹ tín dụng nhân dân** → `TO_CHUC_DOANH_NGHIEP` (span: `[33:36]`) *(lồng trong `e1` (`KHOAN`))*
- `[e7]` **hộ nghèo** → `TO_CHUC_DOANH_NGHIEP` (span: `[41:43]`) *(lồng trong `e1` (`KHOAN`))*
- `[e8]` **hộ nghèo** → `TO_CHUC_DOANH_NGHIEP` (span: `[50:52]`) *(lồng trong `e1` (`KHOAN`))*
- `[e9]` **hộ nghèo** → `TO_CHUC_DOANH_NGHIEP` (span: `[61:63]`) *(lồng trong `e1` (`KHOAN`))*
- `[e10]` **quỹ tín dụng nhân dân** → `TO_CHUC_DOANH_NGHIEP` (span: `[69:72]`) *(lồng trong `e1` (`KHOAN`))*
- `[e11]` **Hộ nghèo** → `TO_CHUC_DOANH_NGHIEP` (span: `[73:75]`) *(lồng trong `e1` (`KHOAN`))*
- `[e12]` **trên địa bàn hoạt động** → `DIA_DIEM` (span: `[17:20]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 5 . Quỹ tín dụng nhân dân cho vay thành viên của hộ nghèo có đăng ký thường trú trên địa bàn hoạt động của quỹ tín dụng nhân dân trong trường hợp hộ nghèo không phải là thành viên của quỹ tín dụng nhân dân . Trường hợp nhiều thành viên của hộ nghèo cùng vay vốn thì các thành viên của hộ nghèo cùng ký hoặc ủy quyền cho một thành viên của hộ nghèo đại diện ký thỏa thuận cho vay với quỹ tín dụng nhân dân . Hộ nghèo phải được `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 2 `[DIEU]`)


---

### Mẫu #06_2017_TT-NHNN_122819#body_context_41 (Loại: `body_context`)
> **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[06/2017/TT-NHNN]`<SO_HIEU>`** . **[Điều 2]`<DIEU>`** . **[5 . **[Sửa đổi]`<TU_KHOA_PHAP_LY>`** **[khoản 3 Điều 40]`<THAM_CHIEU_PHAP_LY>`** như sau : “ 3 . Được **[Ngân hàng Hợp tác xã]`<TO_CHUC_DOANH_NGHIEP>`** hỗ trợ trong việc thực hiện kiểm toán nội bộ khi có yêu cầu ” .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[4:5]`)
- `[e1]` **06/2017/TT-NHNN** → `SO_HIEU` (span: `[6:7]`)
- `[e2]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_BAN_HANH` (span: `[0:3]`)
- `[e3]` **Điều 2** → `DIEU` (span: `[8:10]`)
- `[e4]` **5 . Sửa đổi khoản 3 Điều 40 như sau : “ 3 . Được Ngân hàng Hợp tác xã hỗ trợ trong việc thực hiện kiểm toán nội bộ khi có yêu cầu ” .** → `KHOAN` (span: `[11:38]`)
- `[e5]` **khoản 3 Điều 40** → `THAM_CHIEU_PHAP_LY` (span: `[14:18]`) *(lồng trong `e4` (`KHOAN`))*
- `[e6]` **Sửa đổi** → `TU_KHOA_PHAP_LY` (span: `[13:14]`) *(lồng trong `e4` (`KHOAN`))*
- `[e7]` **Ngân hàng Hợp tác xã** → `TO_CHUC_DOANH_NGHIEP` (span: `[25:27]`) *(lồng trong `e4` (`KHOAN`))*

**Quan hệ:**
- (`e1` 06/2017/TT-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Ngân hàng Nhà nước Việt Nam `[CO_QUAN_BAN_HANH]`)
- (`e1` 06/2017/TT-NHNN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 2 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 06/2017/TT-NHNN `[SO_HIEU]`)
- (`e4` 5 . Sửa đổi khoản 3 Điều 40 như sau : “ 3 . Được Ngân hàng Hợp tác xã hỗ trợ trong việc thực hiện kiểm toán nội bộ khi có yêu cầu ” . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 2 `[DIEU]`)
- (`e6` Sửa đổi `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e5` khoản 3 Điều 40 `[THAM_CHIEU_PHAP_LY]`)
- (`e4` 5 . Sửa đổi khoản 3 Điều 40 như sau : “ 3 . Được Ngân hàng Hợp tác xã hỗ trợ trong việc thực hiện kiểm toán nội bộ khi có yêu cầu ” . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e5` khoản 3 Điều 40 `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #06_2017_TT-NHNN_122819#body_standalone_42 (Loại: `body_standalone`)
> **[Điều 2]`<DIEU>`** . **[5 . **[Sửa đổi]`<TU_KHOA_PHAP_LY>`** **[khoản 3 Điều 40]`<THAM_CHIEU_PHAP_LY>`** như sau : “ 3 . Được **[Ngân hàng Hợp tác xã]`<TO_CHUC_DOANH_NGHIEP>`** hỗ trợ trong việc thực hiện kiểm toán nội bộ khi có yêu cầu ” .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 2** → `DIEU` (span: `[0:2]`)
- `[e1]` **5 . Sửa đổi khoản 3 Điều 40 như sau : “ 3 . Được Ngân hàng Hợp tác xã hỗ trợ trong việc thực hiện kiểm toán nội bộ khi có yêu cầu ” .** → `KHOAN` (span: `[3:30]`)
- `[e2]` **khoản 3 Điều 40** → `THAM_CHIEU_PHAP_LY` (span: `[6:10]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **Sửa đổi** → `TU_KHOA_PHAP_LY` (span: `[5:6]`) *(lồng trong `e1` (`KHOAN`))*
- `[e4]` **Ngân hàng Hợp tác xã** → `TO_CHUC_DOANH_NGHIEP` (span: `[17:19]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 5 . Sửa đổi khoản 3 Điều 40 như sau : “ 3 . Được Ngân hàng Hợp tác xã hỗ trợ trong việc thực hiện kiểm toán nội bộ khi có yêu cầu ” . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 2 `[DIEU]`)
- (`e3` Sửa đổi `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e2` khoản 3 Điều 40 `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 5 . Sửa đổi khoản 3 Điều 40 như sau : “ 3 . Được Ngân hàng Hợp tác xã hỗ trợ trong việc thực hiện kiểm toán nội bộ khi có yêu cầu ” . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e2` khoản 3 Điều 40 `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #06_2017_TT-NHNN_122819#body_context_43 (Loại: `body_context`)
> **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[06/2017/TT-NHNN]`<SO_HIEU>`** . **[Điều 2]`<DIEU>`** . **[6 . **[Sửa đổi]`<TU_KHOA_PHAP_LY>`** **[khoản 3]`<THAM_CHIEU_PHAP_LY>`** và **[bổ sung]`<TU_KHOA_PHAP_LY>`** **[khoản 4 Điều 45]`<THAM_CHIEU_PHAP_LY>`** như sau : “ 3 . Việc chuyển tiếp đối với **[quỹ tín dụng nhân dân]`<TO_CHUC_DOANH_NGHIEP>`** **[không đảm bảo các quy định về địa bàn hoạt động]`<HANH_VI_VI_PHAM>`** ; tỷ lệ vốn góp tối đa của một thành viên ; thành viên đăng ký thường trú ngoài địa bàn ; tổng mức nhận tiền gửi từ thành viên thực hiện **[theo quy định tại]`<TU_KHOA_PHAP_LY>`** **[các Điều 47 , 47a , 48 , 49 và 50 Thông tư này]`<THAM_CHIEU_PHAP_LY>`** .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[4:5]`)
- `[e1]` **06/2017/TT-NHNN** → `SO_HIEU` (span: `[6:7]`)
- `[e2]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_BAN_HANH` (span: `[0:3]`)
- `[e3]` **Điều 2** → `DIEU` (span: `[8:10]`)
- `[e4]` **6 . Sửa đổi khoản 3 và bổ sung khoản 4 Điều 45 như sau : “ 3 . Việc chuyển tiếp đối với quỹ tín dụng nhân dân không đảm bảo các quy định về địa bàn hoạt động ; tỷ lệ vốn góp tối đa của một thành viên ; thành viên đăng ký thường trú ngoài địa bàn ; tổng mức nhận tiền gửi từ thành viên thực hiện theo quy định tại các Điều 47 , 47a , 48 , 49 và 50 Thông tư này .** → `KHOAN` (span: `[11:81]`)
- `[e5]` **không đảm bảo các quy định về địa bàn hoạt động** → `HANH_VI_VI_PHAM` (span: `[34:41]`) *(lồng trong `e4` (`KHOAN`))*
- `[e6]` **khoản 3** → `THAM_CHIEU_PHAP_LY` (span: `[14:16]`) *(lồng trong `e4` (`KHOAN`))*
- `[e7]` **khoản 4 Điều 45** → `THAM_CHIEU_PHAP_LY` (span: `[18:22]`) *(lồng trong `e4` (`KHOAN`))*
- `[e8]` **các Điều 47 , 47a , 48 , 49 và 50 Thông tư này** → `THAM_CHIEU_PHAP_LY` (span: `[67:80]`) *(lồng trong `e4` (`KHOAN`))*
- `[e9]` **Sửa đổi** → `TU_KHOA_PHAP_LY` (span: `[13:14]`) *(lồng trong `e4` (`KHOAN`))*
- `[e10]` **bổ sung** → `TU_KHOA_PHAP_LY` (span: `[17:18]`) *(lồng trong `e4` (`KHOAN`))*
- `[e11]` **theo quy định tại** → `TU_KHOA_PHAP_LY` (span: `[64:67]`) *(lồng trong `e4` (`KHOAN`))*
- `[e12]` **quỹ tín dụng nhân dân** → `TO_CHUC_DOANH_NGHIEP` (span: `[31:34]`) *(lồng trong `e4` (`KHOAN`))*

**Quan hệ:**
- (`e1` 06/2017/TT-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Ngân hàng Nhà nước Việt Nam `[CO_QUAN_BAN_HANH]`)
- (`e1` 06/2017/TT-NHNN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 2 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 06/2017/TT-NHNN `[SO_HIEU]`)
- (`e4` 6 . Sửa đổi khoản 3 và bổ sung khoản 4 Điều 45 như sau : “ 3 . Việc chuyển tiếp đối với quỹ tín dụng nhân dân không đảm bảo các quy định về địa bàn hoạt động ; tỷ lệ vốn góp tối đa của một thành viên ; thành viên đăng ký thường trú ngoài địa bàn ; tổng mức nhận tiền gửi từ thành viên thực hiện theo quy định tại các Điều 47 , 47a , 48 , 49 và 50 Thông tư này . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 2 `[DIEU]`)
- (`e12` quỹ tín dụng nhân dân `[TO_CHUC_DOANH_NGHIEP]`) ==[ **THUC_HIEN_VI_PHAM** ]==> (`e5` không đảm bảo các quy định về địa bàn hoạt động `[HANH_VI_VI_PHAM]`)
- (`e9` Sửa đổi `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e6` khoản 3 `[THAM_CHIEU_PHAP_LY]`)
- (`e5` không đảm bảo các quy định về địa bàn hoạt động `[HANH_VI_VI_PHAM]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e6` khoản 3 `[THAM_CHIEU_PHAP_LY]`)
- (`e10` bổ sung `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e7` khoản 4 Điều 45 `[THAM_CHIEU_PHAP_LY]`)
- (`e5` không đảm bảo các quy định về địa bàn hoạt động `[HANH_VI_VI_PHAM]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e7` khoản 4 Điều 45 `[THAM_CHIEU_PHAP_LY]`)
- (`e11` theo quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e8` các Điều 47 , 47a , 48 , 49 và 50 Thông tư này `[THAM_CHIEU_PHAP_LY]`)
- (`e5` không đảm bảo các quy định về địa bàn hoạt động `[HANH_VI_VI_PHAM]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e8` các Điều 47 , 47a , 48 , 49 và 50 Thông tư này `[THAM_CHIEU_PHAP_LY]`)


---

### Mẫu #06_2017_TT-NHNN_122819#body_standalone_44 (Loại: `body_standalone`)
> **[Điều 2]`<DIEU>`** . **[6 . **[Sửa đổi]`<TU_KHOA_PHAP_LY>`** **[khoản 3]`<THAM_CHIEU_PHAP_LY>`** và **[bổ sung]`<TU_KHOA_PHAP_LY>`** **[khoản 4 Điều 45]`<THAM_CHIEU_PHAP_LY>`** như sau : “ 3 . Việc chuyển tiếp đối với **[quỹ tín dụng nhân dân]`<TO_CHUC_DOANH_NGHIEP>`** **[không đảm bảo các quy định về địa bàn hoạt động]`<HANH_VI_VI_PHAM>`** ; tỷ lệ vốn góp tối đa của một thành viên ; thành viên đăng ký thường trú ngoài địa bàn ; tổng mức nhận tiền gửi từ thành viên thực hiện **[theo quy định tại]`<TU_KHOA_PHAP_LY>`** **[các Điều 47 , 47a , 48 , 49 và 50 Thông tư này]`<THAM_CHIEU_PHAP_LY>`** .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 2** → `DIEU` (span: `[0:2]`)
- `[e1]` **6 . Sửa đổi khoản 3 và bổ sung khoản 4 Điều 45 như sau : “ 3 . Việc chuyển tiếp đối với quỹ tín dụng nhân dân không đảm bảo các quy định về địa bàn hoạt động ; tỷ lệ vốn góp tối đa của một thành viên ; thành viên đăng ký thường trú ngoài địa bàn ; tổng mức nhận tiền gửi từ thành viên thực hiện theo quy định tại các Điều 47 , 47a , 48 , 49 và 50 Thông tư này .** → `KHOAN` (span: `[3:73]`)
- `[e2]` **không đảm bảo các quy định về địa bàn hoạt động** → `HANH_VI_VI_PHAM` (span: `[26:33]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **khoản 3** → `THAM_CHIEU_PHAP_LY` (span: `[6:8]`) *(lồng trong `e1` (`KHOAN`))*
- `[e4]` **khoản 4 Điều 45** → `THAM_CHIEU_PHAP_LY` (span: `[10:14]`) *(lồng trong `e1` (`KHOAN`))*
- `[e5]` **các Điều 47 , 47a , 48 , 49 và 50 Thông tư này** → `THAM_CHIEU_PHAP_LY` (span: `[59:72]`) *(lồng trong `e1` (`KHOAN`))*
- `[e6]` **Sửa đổi** → `TU_KHOA_PHAP_LY` (span: `[5:6]`) *(lồng trong `e1` (`KHOAN`))*
- `[e7]` **bổ sung** → `TU_KHOA_PHAP_LY` (span: `[9:10]`) *(lồng trong `e1` (`KHOAN`))*
- `[e8]` **theo quy định tại** → `TU_KHOA_PHAP_LY` (span: `[56:59]`) *(lồng trong `e1` (`KHOAN`))*
- `[e9]` **quỹ tín dụng nhân dân** → `TO_CHUC_DOANH_NGHIEP` (span: `[23:26]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 6 . Sửa đổi khoản 3 và bổ sung khoản 4 Điều 45 như sau : “ 3 . Việc chuyển tiếp đối với quỹ tín dụng nhân dân không đảm bảo các quy định về địa bàn hoạt động ; tỷ lệ vốn góp tối đa của một thành viên ; thành viên đăng ký thường trú ngoài địa bàn ; tổng mức nhận tiền gửi từ thành viên thực hiện theo quy định tại các Điều 47 , 47a , 48 , 49 và 50 Thông tư này . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 2 `[DIEU]`)
- (`e9` quỹ tín dụng nhân dân `[TO_CHUC_DOANH_NGHIEP]`) ==[ **THUC_HIEN_VI_PHAM** ]==> (`e2` không đảm bảo các quy định về địa bàn hoạt động `[HANH_VI_VI_PHAM]`)
- (`e6` Sửa đổi `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` khoản 3 `[THAM_CHIEU_PHAP_LY]`)
- (`e2` không đảm bảo các quy định về địa bàn hoạt động `[HANH_VI_VI_PHAM]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` khoản 3 `[THAM_CHIEU_PHAP_LY]`)
- (`e7` bổ sung `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e4` khoản 4 Điều 45 `[THAM_CHIEU_PHAP_LY]`)
- (`e2` không đảm bảo các quy định về địa bàn hoạt động `[HANH_VI_VI_PHAM]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e4` khoản 4 Điều 45 `[THAM_CHIEU_PHAP_LY]`)
- (`e8` theo quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e5` các Điều 47 , 47a , 48 , 49 và 50 Thông tư này `[THAM_CHIEU_PHAP_LY]`)
- (`e2` không đảm bảo các quy định về địa bàn hoạt động `[HANH_VI_VI_PHAM]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e5` các Điều 47 , 47a , 48 , 49 và 50 Thông tư này `[THAM_CHIEU_PHAP_LY]`)


---

### Mẫu #06_2017_TT-NHNN_122819#body_context_45 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[06/2017/TT-NHNN]`<SO_HIEU>`** của **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Thanh tra , giám sát ngân hàng]`<LINH_VUC>`** . **[Điều 2]`<DIEU>`** . **[4 . **[Quỹ tín dụng nhân dân]`<TO_CHUC_DOANH_NGHIEP>`** chuyển vốn góp thường xuyên của thành viên **[theo quy định tại]`<TU_KHOA_PHAP_LY>`** **[khoản 3]`<THAM_CHIEU_PHAP_LY>`** **[Thông tư số 08/2005/TT-NHNN]`<THAM_CHIEU_PHAP_LY>`** **[ngày 30/12/2005]`<NGAY_THAM_CHIEU>`** và khoản 3 **[Thông tư số 06/2007/TT-NHNN]`<THAM_CHIEU_PHAP_LY>`** **[ngày 06/11/2007]`<NGAY_THAM_CHIEU>`** của **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_THAM_QUYEN>`** hướng dẫn thực hiện một số điều của **[Nghị định số 48/2001/NĐ-CP]`<THAM_CHIEU_PHAP_LY>`** **[ngày 13/8/2001]`<NGAY_THAM_CHIEU>`** và **[Nghị định số 69/2005/NĐ-CP]`<THAM_CHIEU_PHAP_LY>`** **[ngày 26/5/2005]`<NGAY_THAM_CHIEU>`** của **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** quy định về tổ chức và hoạt động của **[quỹ tín dụng nhân dân]`<TO_CHUC_DOANH_NGHIEP>`** thành vốn góp thường niên của thành viên theo quy định tại]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **06/2017/TT-NHNN** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_BAN_HANH` (span: `[4:7]`)
- `[e3]` **Thanh tra , giám sát ngân hàng** → `LINH_VUC` (span: `[9:13]`)
- `[e4]` **Điều 2** → `DIEU` (span: `[14:16]`)
- `[e5]` **4 . Quỹ tín dụng nhân dân chuyển vốn góp thường xuyên của thành viên theo quy định tại khoản 3 Thông tư số 08/2005/TT-NHNN ngày 30/12/2005 và khoản 3 Thông tư số 06/2007/TT-NHNN ngày 06/11/2007 của Ngân hàng Nhà nước Việt Nam hướng dẫn thực hiện một số điều của Nghị định số 48/2001/NĐ-CP ngày 13/8/2001 và Nghị định số 69/2005/NĐ-CP ngày 26/5/2005 của Chính phủ quy định về tổ chức và hoạt động của quỹ tín dụng nhân dân thành vốn góp thường niên của thành viên theo quy định tại** → `KHOAN` (span: `[17:86]`)
- `[e6]` **khoản 3** → `THAM_CHIEU_PHAP_LY` (span: `[31:33]`) *(lồng trong `e5` (`KHOAN`))*
- `[e7]` **Thông tư số 08/2005/TT-NHNN** → `THAM_CHIEU_PHAP_LY` (span: `[33:36]`) *(lồng trong `e5` (`KHOAN`))*
- `[e8]` **Thông tư số 06/2007/TT-NHNN** → `THAM_CHIEU_PHAP_LY` (span: `[41:44]`) *(lồng trong `e5` (`KHOAN`))*
- `[e9]` **Nghị định số 48/2001/NĐ-CP** → `THAM_CHIEU_PHAP_LY` (span: `[55:58]`) *(lồng trong `e5` (`KHOAN`))*
- `[e10]` **Nghị định số 69/2005/NĐ-CP** → `THAM_CHIEU_PHAP_LY` (span: `[61:64]`) *(lồng trong `e5` (`KHOAN`))*
- `[e11]` **theo quy định tại** → `TU_KHOA_PHAP_LY` (span: `[28:31]`) *(lồng trong `e5` (`KHOAN`))*
- `[e12]` **ngày 30/12/2005** → `NGAY_THAM_CHIEU` (span: `[36:38]`) *(lồng trong `e5` (`KHOAN`))*
- `[e13]` **ngày 06/11/2007** → `NGAY_THAM_CHIEU` (span: `[44:46]`) *(lồng trong `e5` (`KHOAN`))*
- `[e14]` **ngày 13/8/2001** → `NGAY_THAM_CHIEU` (span: `[58:60]`) *(lồng trong `e5` (`KHOAN`))*
- `[e15]` **ngày 26/5/2005** → `NGAY_THAM_CHIEU` (span: `[64:66]`) *(lồng trong `e5` (`KHOAN`))*
- `[e16]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_THAM_QUYEN` (span: `[47:50]`) *(lồng trong `e5` (`KHOAN`))*
- `[e17]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[67:68]`) *(lồng trong `e5` (`KHOAN`))*
- `[e18]` **Quỹ tín dụng nhân dân** → `TO_CHUC_DOANH_NGHIEP` (span: `[19:22]`) *(lồng trong `e5` (`KHOAN`))*
- `[e19]` **quỹ tín dụng nhân dân** → `TO_CHUC_DOANH_NGHIEP` (span: `[74:77]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 06/2017/TT-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Ngân hàng Nhà nước Việt Nam `[CO_QUAN_BAN_HANH]`)
- (`e1` 06/2017/TT-NHNN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 06/2017/TT-NHNN `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Thanh tra , giám sát ngân hàng `[LINH_VUC]`)
- (`e4` Điều 2 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 06/2017/TT-NHNN `[SO_HIEU]`)
- (`e5` 4 . Quỹ tín dụng nhân dân chuyển vốn góp thường xuyên của thành viên theo quy định tại khoản 3 Thông tư số 08/2005/TT-NHNN ngày 30/12/2005 và khoản 3 Thông tư số 06/2007/TT-NHNN ngày 06/11/2007 của Ngân hàng Nhà nước Việt Nam hướng dẫn thực hiện một số điều của Nghị định số 48/2001/NĐ-CP ngày 13/8/2001 và Nghị định số 69/2005/NĐ-CP ngày 26/5/2005 của Chính phủ quy định về tổ chức và hoạt động của quỹ tín dụng nhân dân thành vốn góp thường niên của thành viên theo quy định tại `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 2 `[DIEU]`)
- (`e1` 06/2017/TT-NHNN `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Thanh tra , giám sát ngân hàng `[LINH_VUC]`)
- (`e5` 4 . Quỹ tín dụng nhân dân chuyển vốn góp thường xuyên của thành viên theo quy định tại khoản 3 Thông tư số 08/2005/TT-NHNN ngày 30/12/2005 và khoản 3 Thông tư số 06/2007/TT-NHNN ngày 06/11/2007 của Ngân hàng Nhà nước Việt Nam hướng dẫn thực hiện một số điều của Nghị định số 48/2001/NĐ-CP ngày 13/8/2001 và Nghị định số 69/2005/NĐ-CP ngày 26/5/2005 của Chính phủ quy định về tổ chức và hoạt động của quỹ tín dụng nhân dân thành vốn góp thường niên của thành viên theo quy định tại `[KHOAN]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Thanh tra , giám sát ngân hàng `[LINH_VUC]`)
- (`e11` theo quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e6` khoản 3 `[THAM_CHIEU_PHAP_LY]`)
- (`e5` 4 . Quỹ tín dụng nhân dân chuyển vốn góp thường xuyên của thành viên theo quy định tại khoản 3 Thông tư số 08/2005/TT-NHNN ngày 30/12/2005 và khoản 3 Thông tư số 06/2007/TT-NHNN ngày 06/11/2007 của Ngân hàng Nhà nước Việt Nam hướng dẫn thực hiện một số điều của Nghị định số 48/2001/NĐ-CP ngày 13/8/2001 và Nghị định số 69/2005/NĐ-CP ngày 26/5/2005 của Chính phủ quy định về tổ chức và hoạt động của quỹ tín dụng nhân dân thành vốn góp thường niên của thành viên theo quy định tại `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e6` khoản 3 `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e11` theo quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e7` Thông tư số 08/2005/TT-NHNN `[THAM_CHIEU_PHAP_LY]`)
- (`e5` 4 . Quỹ tín dụng nhân dân chuyển vốn góp thường xuyên của thành viên theo quy định tại khoản 3 Thông tư số 08/2005/TT-NHNN ngày 30/12/2005 và khoản 3 Thông tư số 06/2007/TT-NHNN ngày 06/11/2007 của Ngân hàng Nhà nước Việt Nam hướng dẫn thực hiện một số điều của Nghị định số 48/2001/NĐ-CP ngày 13/8/2001 và Nghị định số 69/2005/NĐ-CP ngày 26/5/2005 của Chính phủ quy định về tổ chức và hoạt động của quỹ tín dụng nhân dân thành vốn góp thường niên của thành viên theo quy định tại `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e7` Thông tư số 08/2005/TT-NHNN `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e11` theo quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e8` Thông tư số 06/2007/TT-NHNN `[THAM_CHIEU_PHAP_LY]`)
- (`e5` 4 . Quỹ tín dụng nhân dân chuyển vốn góp thường xuyên của thành viên theo quy định tại khoản 3 Thông tư số 08/2005/TT-NHNN ngày 30/12/2005 và khoản 3 Thông tư số 06/2007/TT-NHNN ngày 06/11/2007 của Ngân hàng Nhà nước Việt Nam hướng dẫn thực hiện một số điều của Nghị định số 48/2001/NĐ-CP ngày 13/8/2001 và Nghị định số 69/2005/NĐ-CP ngày 26/5/2005 của Chính phủ quy định về tổ chức và hoạt động của quỹ tín dụng nhân dân thành vốn góp thường niên của thành viên theo quy định tại `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e8` Thông tư số 06/2007/TT-NHNN `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e11` theo quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e9` Nghị định số 48/2001/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e5` 4 . Quỹ tín dụng nhân dân chuyển vốn góp thường xuyên của thành viên theo quy định tại khoản 3 Thông tư số 08/2005/TT-NHNN ngày 30/12/2005 và khoản 3 Thông tư số 06/2007/TT-NHNN ngày 06/11/2007 của Ngân hàng Nhà nước Việt Nam hướng dẫn thực hiện một số điều của Nghị định số 48/2001/NĐ-CP ngày 13/8/2001 và Nghị định số 69/2005/NĐ-CP ngày 26/5/2005 của Chính phủ quy định về tổ chức và hoạt động của quỹ tín dụng nhân dân thành vốn góp thường niên của thành viên theo quy định tại `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e9` Nghị định số 48/2001/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e11` theo quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e10` Nghị định số 69/2005/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e5` 4 . Quỹ tín dụng nhân dân chuyển vốn góp thường xuyên của thành viên theo quy định tại khoản 3 Thông tư số 08/2005/TT-NHNN ngày 30/12/2005 và khoản 3 Thông tư số 06/2007/TT-NHNN ngày 06/11/2007 của Ngân hàng Nhà nước Việt Nam hướng dẫn thực hiện một số điều của Nghị định số 48/2001/NĐ-CP ngày 13/8/2001 và Nghị định số 69/2005/NĐ-CP ngày 26/5/2005 của Chính phủ quy định về tổ chức và hoạt động của quỹ tín dụng nhân dân thành vốn góp thường niên của thành viên theo quy định tại `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e10` Nghị định số 69/2005/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e7` Thông tư số 08/2005/TT-NHNN `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e12` ngày 30/12/2005 `[NGAY_THAM_CHIEU]`)
- (`e8` Thông tư số 06/2007/TT-NHNN `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e13` ngày 06/11/2007 `[NGAY_THAM_CHIEU]`)
- (`e9` Nghị định số 48/2001/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e14` ngày 13/8/2001 `[NGAY_THAM_CHIEU]`)
- (`e10` Nghị định số 69/2005/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e15` ngày 26/5/2005 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #06_2017_TT-NHNN_122819#body_standalone_46 (Loại: `body_standalone`)
> **[Điều 2]`<DIEU>`** . **[4 . **[Quỹ tín dụng nhân dân]`<TO_CHUC_DOANH_NGHIEP>`** chuyển vốn góp thường xuyên của thành viên **[theo quy định tại]`<TU_KHOA_PHAP_LY>`** **[khoản 3]`<THAM_CHIEU_PHAP_LY>`** **[Thông tư số 08/2005/TT-NHNN]`<THAM_CHIEU_PHAP_LY>`** **[ngày 30/12/2005]`<NGAY_THAM_CHIEU>`** và khoản 3 **[Thông tư số 06/2007/TT-NHNN]`<THAM_CHIEU_PHAP_LY>`** **[ngày 06/11/2007]`<NGAY_THAM_CHIEU>`** của **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_THAM_QUYEN>`** hướng dẫn thực hiện một số điều của **[Nghị định số 48/2001/NĐ-CP]`<THAM_CHIEU_PHAP_LY>`** **[ngày 13/8/2001]`<NGAY_THAM_CHIEU>`** và **[Nghị định số 69/2005/NĐ-CP]`<THAM_CHIEU_PHAP_LY>`** **[ngày 26/5/2005]`<NGAY_THAM_CHIEU>`** của **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** quy định về tổ chức và hoạt động của **[quỹ tín dụng nhân dân]`<TO_CHUC_DOANH_NGHIEP>`** thành vốn góp thường niên của thành viên theo quy định tại]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 2** → `DIEU` (span: `[0:2]`)
- `[e1]` **4 . Quỹ tín dụng nhân dân chuyển vốn góp thường xuyên của thành viên theo quy định tại khoản 3 Thông tư số 08/2005/TT-NHNN ngày 30/12/2005 và khoản 3 Thông tư số 06/2007/TT-NHNN ngày 06/11/2007 của Ngân hàng Nhà nước Việt Nam hướng dẫn thực hiện một số điều của Nghị định số 48/2001/NĐ-CP ngày 13/8/2001 và Nghị định số 69/2005/NĐ-CP ngày 26/5/2005 của Chính phủ quy định về tổ chức và hoạt động của quỹ tín dụng nhân dân thành vốn góp thường niên của thành viên theo quy định tại** → `KHOAN` (span: `[3:72]`)
- `[e2]` **khoản 3** → `THAM_CHIEU_PHAP_LY` (span: `[17:19]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **Thông tư số 08/2005/TT-NHNN** → `THAM_CHIEU_PHAP_LY` (span: `[19:22]`) *(lồng trong `e1` (`KHOAN`))*
- `[e4]` **Thông tư số 06/2007/TT-NHNN** → `THAM_CHIEU_PHAP_LY` (span: `[27:30]`) *(lồng trong `e1` (`KHOAN`))*
- `[e5]` **Nghị định số 48/2001/NĐ-CP** → `THAM_CHIEU_PHAP_LY` (span: `[41:44]`) *(lồng trong `e1` (`KHOAN`))*
- `[e6]` **Nghị định số 69/2005/NĐ-CP** → `THAM_CHIEU_PHAP_LY` (span: `[47:50]`) *(lồng trong `e1` (`KHOAN`))*
- `[e7]` **theo quy định tại** → `TU_KHOA_PHAP_LY` (span: `[14:17]`) *(lồng trong `e1` (`KHOAN`))*
- `[e8]` **ngày 30/12/2005** → `NGAY_THAM_CHIEU` (span: `[22:24]`) *(lồng trong `e1` (`KHOAN`))*
- `[e9]` **ngày 06/11/2007** → `NGAY_THAM_CHIEU` (span: `[30:32]`) *(lồng trong `e1` (`KHOAN`))*
- `[e10]` **ngày 13/8/2001** → `NGAY_THAM_CHIEU` (span: `[44:46]`) *(lồng trong `e1` (`KHOAN`))*
- `[e11]` **ngày 26/5/2005** → `NGAY_THAM_CHIEU` (span: `[50:52]`) *(lồng trong `e1` (`KHOAN`))*
- `[e12]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_THAM_QUYEN` (span: `[33:36]`) *(lồng trong `e1` (`KHOAN`))*
- `[e13]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[53:54]`) *(lồng trong `e1` (`KHOAN`))*
- `[e14]` **Quỹ tín dụng nhân dân** → `TO_CHUC_DOANH_NGHIEP` (span: `[5:8]`) *(lồng trong `e1` (`KHOAN`))*
- `[e15]` **quỹ tín dụng nhân dân** → `TO_CHUC_DOANH_NGHIEP` (span: `[60:63]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 4 . Quỹ tín dụng nhân dân chuyển vốn góp thường xuyên của thành viên theo quy định tại khoản 3 Thông tư số 08/2005/TT-NHNN ngày 30/12/2005 và khoản 3 Thông tư số 06/2007/TT-NHNN ngày 06/11/2007 của Ngân hàng Nhà nước Việt Nam hướng dẫn thực hiện một số điều của Nghị định số 48/2001/NĐ-CP ngày 13/8/2001 và Nghị định số 69/2005/NĐ-CP ngày 26/5/2005 của Chính phủ quy định về tổ chức và hoạt động của quỹ tín dụng nhân dân thành vốn góp thường niên của thành viên theo quy định tại `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 2 `[DIEU]`)
- (`e7` theo quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e2` khoản 3 `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 4 . Quỹ tín dụng nhân dân chuyển vốn góp thường xuyên của thành viên theo quy định tại khoản 3 Thông tư số 08/2005/TT-NHNN ngày 30/12/2005 và khoản 3 Thông tư số 06/2007/TT-NHNN ngày 06/11/2007 của Ngân hàng Nhà nước Việt Nam hướng dẫn thực hiện một số điều của Nghị định số 48/2001/NĐ-CP ngày 13/8/2001 và Nghị định số 69/2005/NĐ-CP ngày 26/5/2005 của Chính phủ quy định về tổ chức và hoạt động của quỹ tín dụng nhân dân thành vốn góp thường niên của thành viên theo quy định tại `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e2` khoản 3 `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e7` theo quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Thông tư số 08/2005/TT-NHNN `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 4 . Quỹ tín dụng nhân dân chuyển vốn góp thường xuyên của thành viên theo quy định tại khoản 3 Thông tư số 08/2005/TT-NHNN ngày 30/12/2005 và khoản 3 Thông tư số 06/2007/TT-NHNN ngày 06/11/2007 của Ngân hàng Nhà nước Việt Nam hướng dẫn thực hiện một số điều của Nghị định số 48/2001/NĐ-CP ngày 13/8/2001 và Nghị định số 69/2005/NĐ-CP ngày 26/5/2005 của Chính phủ quy định về tổ chức và hoạt động của quỹ tín dụng nhân dân thành vốn góp thường niên của thành viên theo quy định tại `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Thông tư số 08/2005/TT-NHNN `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e7` theo quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e4` Thông tư số 06/2007/TT-NHNN `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 4 . Quỹ tín dụng nhân dân chuyển vốn góp thường xuyên của thành viên theo quy định tại khoản 3 Thông tư số 08/2005/TT-NHNN ngày 30/12/2005 và khoản 3 Thông tư số 06/2007/TT-NHNN ngày 06/11/2007 của Ngân hàng Nhà nước Việt Nam hướng dẫn thực hiện một số điều của Nghị định số 48/2001/NĐ-CP ngày 13/8/2001 và Nghị định số 69/2005/NĐ-CP ngày 26/5/2005 của Chính phủ quy định về tổ chức và hoạt động của quỹ tín dụng nhân dân thành vốn góp thường niên của thành viên theo quy định tại `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e4` Thông tư số 06/2007/TT-NHNN `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e7` theo quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e5` Nghị định số 48/2001/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 4 . Quỹ tín dụng nhân dân chuyển vốn góp thường xuyên của thành viên theo quy định tại khoản 3 Thông tư số 08/2005/TT-NHNN ngày 30/12/2005 và khoản 3 Thông tư số 06/2007/TT-NHNN ngày 06/11/2007 của Ngân hàng Nhà nước Việt Nam hướng dẫn thực hiện một số điều của Nghị định số 48/2001/NĐ-CP ngày 13/8/2001 và Nghị định số 69/2005/NĐ-CP ngày 26/5/2005 của Chính phủ quy định về tổ chức và hoạt động của quỹ tín dụng nhân dân thành vốn góp thường niên của thành viên theo quy định tại `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e5` Nghị định số 48/2001/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e7` theo quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e6` Nghị định số 69/2005/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 4 . Quỹ tín dụng nhân dân chuyển vốn góp thường xuyên của thành viên theo quy định tại khoản 3 Thông tư số 08/2005/TT-NHNN ngày 30/12/2005 và khoản 3 Thông tư số 06/2007/TT-NHNN ngày 06/11/2007 của Ngân hàng Nhà nước Việt Nam hướng dẫn thực hiện một số điều của Nghị định số 48/2001/NĐ-CP ngày 13/8/2001 và Nghị định số 69/2005/NĐ-CP ngày 26/5/2005 của Chính phủ quy định về tổ chức và hoạt động của quỹ tín dụng nhân dân thành vốn góp thường niên của thành viên theo quy định tại `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e6` Nghị định số 69/2005/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e3` Thông tư số 08/2005/TT-NHNN `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e8` ngày 30/12/2005 `[NGAY_THAM_CHIEU]`)
- (`e4` Thông tư số 06/2007/TT-NHNN `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e9` ngày 06/11/2007 `[NGAY_THAM_CHIEU]`)
- (`e5` Nghị định số 48/2001/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e10` ngày 13/8/2001 `[NGAY_THAM_CHIEU]`)
- (`e6` Nghị định số 69/2005/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e11` ngày 26/5/2005 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #06_2017_TT-NHNN_122819#body_context_47 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[06/2017/TT-NHNN]`<SO_HIEU>`** ban hành **[ngày 05 tháng 07 năm 2017]`<NGAY_BAN_HANH>`** bởi **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_BAN_HANH>`** . **[Điều 2]`<DIEU>`** . **[7 . **[Sửa đổi]`<TU_KHOA_PHAP_LY>`** **[khoản 1 Điều 46]`<THAM_CHIEU_PHAP_LY>`** như sau : “ 1 . Tại thời điểm Thông tư này có hiệu lực thi hành , **[quỹ tín dụng nhân dân]`<TO_CHUC_DOANH_NGHIEP>`** chưa đảm bảo các quy định về địa bàn hoạt động , tỷ lệ góp vốn của một thành viên , thành viên đăng ký thường trú ngoài địa bàn , tổng mức nhận tiền gửi từ thành viên tại Thông tư này phải xây dựng các **[phương án xử lý]`<GIAY_TO_HO_SO>`** và chủ động tổ chức thực hiện các biện pháp xử lý để tuân thủ đúng quy định ” .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **06/2017/TT-NHNN** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_BAN_HANH` (span: `[11:14]`)
- `[e3]` **ngày 05 tháng 07 năm 2017** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 2** → `DIEU` (span: `[15:17]`)
- `[e5]` **7 . Sửa đổi khoản 1 Điều 46 như sau : “ 1 . Tại thời điểm Thông tư này có hiệu lực thi hành , quỹ tín dụng nhân dân chưa đảm bảo các quy định về địa bàn hoạt động , tỷ lệ góp vốn của một thành viên , thành viên đăng ký thường trú ngoài địa bàn , tổng mức nhận tiền gửi từ thành viên tại Thông tư này phải xây dựng các phương án xử lý và chủ động tổ chức thực hiện các biện pháp xử lý để tuân thủ đúng quy định ” .** → `KHOAN` (span: `[18:91]`)
- `[e6]` **khoản 1 Điều 46** → `THAM_CHIEU_PHAP_LY` (span: `[21:25]`) *(lồng trong `e5` (`KHOAN`))*
- `[e7]` **Sửa đổi** → `TU_KHOA_PHAP_LY` (span: `[20:21]`) *(lồng trong `e5` (`KHOAN`))*
- `[e8]` **phương án xử lý** → `GIAY_TO_HO_SO` (span: `[76:78]`) *(lồng trong `e5` (`KHOAN`))*
- `[e9]` **quỹ tín dụng nhân dân** → `TO_CHUC_DOANH_NGHIEP` (span: `[39:42]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 06/2017/TT-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Ngân hàng Nhà nước Việt Nam `[CO_QUAN_BAN_HANH]`)
- (`e1` 06/2017/TT-NHNN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 06/2017/TT-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 05 tháng 07 năm 2017 `[NGAY_BAN_HANH]`)
- (`e4` Điều 2 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 06/2017/TT-NHNN `[SO_HIEU]`)
- (`e5` 7 . Sửa đổi khoản 1 Điều 46 như sau : “ 1 . Tại thời điểm Thông tư này có hiệu lực thi hành , quỹ tín dụng nhân dân chưa đảm bảo các quy định về địa bàn hoạt động , tỷ lệ góp vốn của một thành viên , thành viên đăng ký thường trú ngoài địa bàn , tổng mức nhận tiền gửi từ thành viên tại Thông tư này phải xây dựng các phương án xử lý và chủ động tổ chức thực hiện các biện pháp xử lý để tuân thủ đúng quy định ” . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 2 `[DIEU]`)
- (`e7` Sửa đổi `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e6` khoản 1 Điều 46 `[THAM_CHIEU_PHAP_LY]`)
- (`e5` 7 . Sửa đổi khoản 1 Điều 46 như sau : “ 1 . Tại thời điểm Thông tư này có hiệu lực thi hành , quỹ tín dụng nhân dân chưa đảm bảo các quy định về địa bàn hoạt động , tỷ lệ góp vốn của một thành viên , thành viên đăng ký thường trú ngoài địa bàn , tổng mức nhận tiền gửi từ thành viên tại Thông tư này phải xây dựng các phương án xử lý và chủ động tổ chức thực hiện các biện pháp xử lý để tuân thủ đúng quy định ” . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e6` khoản 1 Điều 46 `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #06_2017_TT-NHNN_122819#body_standalone_48 (Loại: `body_standalone`)
> **[Điều 2]`<DIEU>`** . **[7 . **[Sửa đổi]`<TU_KHOA_PHAP_LY>`** **[khoản 1 Điều 46]`<THAM_CHIEU_PHAP_LY>`** như sau : “ 1 . Tại thời điểm Thông tư này có hiệu lực thi hành , **[quỹ tín dụng nhân dân]`<TO_CHUC_DOANH_NGHIEP>`** chưa đảm bảo các quy định về địa bàn hoạt động , tỷ lệ góp vốn của một thành viên , thành viên đăng ký thường trú ngoài địa bàn , tổng mức nhận tiền gửi từ thành viên tại Thông tư này phải xây dựng các **[phương án xử lý]`<GIAY_TO_HO_SO>`** và chủ động tổ chức thực hiện các biện pháp xử lý để tuân thủ đúng quy định ” .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 2** → `DIEU` (span: `[0:2]`)
- `[e1]` **7 . Sửa đổi khoản 1 Điều 46 như sau : “ 1 . Tại thời điểm Thông tư này có hiệu lực thi hành , quỹ tín dụng nhân dân chưa đảm bảo các quy định về địa bàn hoạt động , tỷ lệ góp vốn của một thành viên , thành viên đăng ký thường trú ngoài địa bàn , tổng mức nhận tiền gửi từ thành viên tại Thông tư này phải xây dựng các phương án xử lý và chủ động tổ chức thực hiện các biện pháp xử lý để tuân thủ đúng quy định ” .** → `KHOAN` (span: `[3:76]`)
- `[e2]` **khoản 1 Điều 46** → `THAM_CHIEU_PHAP_LY` (span: `[6:10]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **Sửa đổi** → `TU_KHOA_PHAP_LY` (span: `[5:6]`) *(lồng trong `e1` (`KHOAN`))*
- `[e4]` **phương án xử lý** → `GIAY_TO_HO_SO` (span: `[61:63]`) *(lồng trong `e1` (`KHOAN`))*
- `[e5]` **quỹ tín dụng nhân dân** → `TO_CHUC_DOANH_NGHIEP` (span: `[24:27]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 7 . Sửa đổi khoản 1 Điều 46 như sau : “ 1 . Tại thời điểm Thông tư này có hiệu lực thi hành , quỹ tín dụng nhân dân chưa đảm bảo các quy định về địa bàn hoạt động , tỷ lệ góp vốn của một thành viên , thành viên đăng ký thường trú ngoài địa bàn , tổng mức nhận tiền gửi từ thành viên tại Thông tư này phải xây dựng các phương án xử lý và chủ động tổ chức thực hiện các biện pháp xử lý để tuân thủ đúng quy định ” . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 2 `[DIEU]`)
- (`e3` Sửa đổi `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e2` khoản 1 Điều 46 `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 7 . Sửa đổi khoản 1 Điều 46 như sau : “ 1 . Tại thời điểm Thông tư này có hiệu lực thi hành , quỹ tín dụng nhân dân chưa đảm bảo các quy định về địa bàn hoạt động , tỷ lệ góp vốn của một thành viên , thành viên đăng ký thường trú ngoài địa bàn , tổng mức nhận tiền gửi từ thành viên tại Thông tư này phải xây dựng các phương án xử lý và chủ động tổ chức thực hiện các biện pháp xử lý để tuân thủ đúng quy định ” . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e2` khoản 1 Điều 46 `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #06_2017_TT-NHNN_122819#body_context_49 (Loại: `body_context`)
> **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[06/2017/TT-NHNN]`<SO_HIEU>`** . **[Điều 2]`<DIEU>`** . **[8 . **[Bổ sung]`<TU_KHOA_PHAP_LY>`** **[Điều 47a]`<THAM_CHIEU_PHAP_LY>`** vào sau **[Điều 47]`<THAM_CHIEU_PHAP_LY>`** như sau : “ Điều 47 a . Quy định đối với thay đổi địa bàn hoạt động do chia , tách địa giới hành chính kể từ ngày 01 tháng 6 năm 2015]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[4:5]`)
- `[e1]` **06/2017/TT-NHNN** → `SO_HIEU` (span: `[6:7]`)
- `[e2]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_BAN_HANH` (span: `[0:3]`)
- `[e3]` **Điều 2** → `DIEU` (span: `[8:10]`)
- `[e4]` **8 . Bổ sung Điều 47a vào sau Điều 47 như sau : “ Điều 47 a . Quy định đối với thay đổi địa bàn hoạt động do chia , tách địa giới hành chính kể từ ngày 01 tháng 6 năm 2015** → `KHOAN` (span: `[11:47]`)
- `[e5]` **Điều 47a** → `THAM_CHIEU_PHAP_LY` (span: `[14:16]`) *(lồng trong `e4` (`KHOAN`))*
- `[e6]` **Điều 47** → `THAM_CHIEU_PHAP_LY` (span: `[18:20]`) *(lồng trong `e4` (`KHOAN`))*
- `[e7]` **Bổ sung** → `TU_KHOA_PHAP_LY` (span: `[13:14]`) *(lồng trong `e4` (`KHOAN`))*

**Quan hệ:**
- (`e1` 06/2017/TT-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Ngân hàng Nhà nước Việt Nam `[CO_QUAN_BAN_HANH]`)
- (`e1` 06/2017/TT-NHNN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 2 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 06/2017/TT-NHNN `[SO_HIEU]`)
- (`e4` 8 . Bổ sung Điều 47a vào sau Điều 47 như sau : “ Điều 47 a . Quy định đối với thay đổi địa bàn hoạt động do chia , tách địa giới hành chính kể từ ngày 01 tháng 6 năm 2015 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 2 `[DIEU]`)
- (`e7` Bổ sung `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e5` Điều 47a `[THAM_CHIEU_PHAP_LY]`)
- (`e4` 8 . Bổ sung Điều 47a vào sau Điều 47 như sau : “ Điều 47 a . Quy định đối với thay đổi địa bàn hoạt động do chia , tách địa giới hành chính kể từ ngày 01 tháng 6 năm 2015 `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e5` Điều 47a `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e7` Bổ sung `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e6` Điều 47 `[THAM_CHIEU_PHAP_LY]`)
- (`e4` 8 . Bổ sung Điều 47a vào sau Điều 47 như sau : “ Điều 47 a . Quy định đối với thay đổi địa bàn hoạt động do chia , tách địa giới hành chính kể từ ngày 01 tháng 6 năm 2015 `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e6` Điều 47 `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #06_2017_TT-NHNN_122819#body_standalone_50 (Loại: `body_standalone`)
> **[Điều 2]`<DIEU>`** . **[8 . **[Bổ sung]`<TU_KHOA_PHAP_LY>`** **[Điều 47a]`<THAM_CHIEU_PHAP_LY>`** vào sau **[Điều 47]`<THAM_CHIEU_PHAP_LY>`** như sau : “ Điều 47 a . Quy định đối với thay đổi địa bàn hoạt động do chia , tách địa giới hành chính kể từ ngày 01 tháng 6 năm 2015]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 2** → `DIEU` (span: `[0:2]`)
- `[e1]` **8 . Bổ sung Điều 47a vào sau Điều 47 như sau : “ Điều 47 a . Quy định đối với thay đổi địa bàn hoạt động do chia , tách địa giới hành chính kể từ ngày 01 tháng 6 năm 2015** → `KHOAN` (span: `[3:39]`)
- `[e2]` **Điều 47a** → `THAM_CHIEU_PHAP_LY` (span: `[6:8]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **Điều 47** → `THAM_CHIEU_PHAP_LY` (span: `[10:12]`) *(lồng trong `e1` (`KHOAN`))*
- `[e4]` **Bổ sung** → `TU_KHOA_PHAP_LY` (span: `[5:6]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 8 . Bổ sung Điều 47a vào sau Điều 47 như sau : “ Điều 47 a . Quy định đối với thay đổi địa bàn hoạt động do chia , tách địa giới hành chính kể từ ngày 01 tháng 6 năm 2015 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 2 `[DIEU]`)
- (`e4` Bổ sung `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e2` Điều 47a `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 8 . Bổ sung Điều 47a vào sau Điều 47 như sau : “ Điều 47 a . Quy định đối với thay đổi địa bàn hoạt động do chia , tách địa giới hành chính kể từ ngày 01 tháng 6 năm 2015 `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e2` Điều 47a `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e4` Bổ sung `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Điều 47 `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 8 . Bổ sung Điều 47a vào sau Điều 47 như sau : “ Điều 47 a . Quy định đối với thay đổi địa bàn hoạt động do chia , tách địa giới hành chính kể từ ngày 01 tháng 6 năm 2015 `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Điều 47 `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #06_2017_TT-NHNN_122819#body_context_51 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[06/2017/TT-NHNN]`<SO_HIEU>`** ban hành **[ngày 05 tháng 07 năm 2017]`<NGAY_BAN_HANH>`** bởi **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_BAN_HANH>`** . **[Điều 2]`<DIEU>`** . **[1 . Đối với các xã không liền kề với xã **[nơi đặt trụ sở chính]`<DIA_DIEM>`** :]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **06/2017/TT-NHNN** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_BAN_HANH` (span: `[11:14]`)
- `[e3]` **ngày 05 tháng 07 năm 2017** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 2** → `DIEU` (span: `[15:17]`)
- `[e5]` **1 . Đối với các xã không liền kề với xã nơi đặt trụ sở chính :** → `KHOAN` (span: `[18:33]`)
- `[e6]` **nơi đặt trụ sở chính** → `DIA_DIEM` (span: `[28:32]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 06/2017/TT-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Ngân hàng Nhà nước Việt Nam `[CO_QUAN_BAN_HANH]`)
- (`e1` 06/2017/TT-NHNN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 06/2017/TT-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 05 tháng 07 năm 2017 `[NGAY_BAN_HANH]`)
- (`e4` Điều 2 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 06/2017/TT-NHNN `[SO_HIEU]`)
- (`e5` 1 . Đối với các xã không liền kề với xã nơi đặt trụ sở chính : `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 2 `[DIEU]`)


---

### Mẫu #06_2017_TT-NHNN_122819#body_context_52 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[06/2017/TT-NHNN]`<SO_HIEU>`** ban hành **[ngày 05 tháng 07 năm 2017]`<NGAY_BAN_HANH>`** bởi **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_BAN_HANH>`** . **[Điều 2]`<DIEU>`** . **[Khoản 1]`<KHOAN>`** . **[a ) Chấm dứt hoạt động tại các xã không liền kề với xã **[nơi đặt trụ sở chính]`<DIA_DIEM>`** **[theo quy định tại]`<TU_KHOA_PHAP_LY>`** **[điểm b]`<THAM_CHIEU_PHAP_LY>`** khoản này ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **06/2017/TT-NHNN** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_BAN_HANH` (span: `[11:14]`)
- `[e3]` **ngày 05 tháng 07 năm 2017** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 2** → `DIEU` (span: `[15:17]`)
- `[e5]` **Khoản 1** → `KHOAN` (span: `[18:20]`)
- `[e6]` **a ) Chấm dứt hoạt động tại các xã không liền kề với xã nơi đặt trụ sở chính theo quy định tại điểm b khoản này ;** → `DIEM` (span: `[21:45]`)
- `[e7]` **điểm b** → `THAM_CHIEU_PHAP_LY` (span: `[40:42]`) *(lồng trong `e6` (`DIEM`))*
- `[e8]` **theo quy định tại** → `TU_KHOA_PHAP_LY` (span: `[37:40]`) *(lồng trong `e6` (`DIEM`))*
- `[e9]` **nơi đặt trụ sở chính** → `DIA_DIEM` (span: `[33:37]`) *(lồng trong `e6` (`DIEM`))*

**Quan hệ:**
- (`e1` 06/2017/TT-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Ngân hàng Nhà nước Việt Nam `[CO_QUAN_BAN_HANH]`)
- (`e1` 06/2017/TT-NHNN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 06/2017/TT-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 05 tháng 07 năm 2017 `[NGAY_BAN_HANH]`)
- (`e4` Điều 2 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 06/2017/TT-NHNN `[SO_HIEU]`)
- (`e5` Khoản 1 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 2 `[DIEU]`)
- (`e6` a ) Chấm dứt hoạt động tại các xã không liền kề với xã nơi đặt trụ sở chính theo quy định tại điểm b khoản này ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e5` Khoản 1 `[KHOAN]`)
- (`e8` theo quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e7` điểm b `[THAM_CHIEU_PHAP_LY]`)
- (`e6` a ) Chấm dứt hoạt động tại các xã không liền kề với xã nơi đặt trụ sở chính theo quy định tại điểm b khoản này ; `[DIEM]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e7` điểm b `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #06_2017_TT-NHNN_122819#body_standalone_53 (Loại: `body_standalone`)
> **[Điều 2]`<DIEU>`** . **[Khoản 1]`<KHOAN>`** . **[a ) Chấm dứt hoạt động tại các xã không liền kề với xã **[nơi đặt trụ sở chính]`<DIA_DIEM>`** **[theo quy định tại]`<TU_KHOA_PHAP_LY>`** **[điểm b]`<THAM_CHIEU_PHAP_LY>`** khoản này ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Điều 2** → `DIEU` (span: `[0:2]`)
- `[e1]` **Khoản 1** → `KHOAN` (span: `[3:5]`)
- `[e2]` **a ) Chấm dứt hoạt động tại các xã không liền kề với xã nơi đặt trụ sở chính theo quy định tại điểm b khoản này ;** → `DIEM` (span: `[6:30]`)
- `[e3]` **điểm b** → `THAM_CHIEU_PHAP_LY` (span: `[25:27]`) *(lồng trong `e2` (`DIEM`))*
- `[e4]` **theo quy định tại** → `TU_KHOA_PHAP_LY` (span: `[22:25]`) *(lồng trong `e2` (`DIEM`))*
- `[e5]` **nơi đặt trụ sở chính** → `DIA_DIEM` (span: `[18:22]`) *(lồng trong `e2` (`DIEM`))*

**Quan hệ:**
- (`e1` Khoản 1 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 2 `[DIEU]`)
- (`e2` a ) Chấm dứt hoạt động tại các xã không liền kề với xã nơi đặt trụ sở chính theo quy định tại điểm b khoản này ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e1` Khoản 1 `[KHOAN]`)
- (`e4` theo quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` điểm b `[THAM_CHIEU_PHAP_LY]`)
- (`e2` a ) Chấm dứt hoạt động tại các xã không liền kề với xã nơi đặt trụ sở chính theo quy định tại điểm b khoản này ; `[DIEM]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` điểm b `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #06_2017_TT-NHNN_122819#body_context_54 (Loại: `body_context`)
> **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[06/2017/TT-NHNN]`<SO_HIEU>`** . **[Điều 2]`<DIEU>`** . **[Khoản 1]`<KHOAN>`** . **[b ) **[Trong thời hạn 30 ngày]`<THOI_HAN>`** kể từ ngày Văn bản điều chỉnh địa giới hành chính của **[Cơ quan Nhà nước có thẩm quyền]`<CO_QUAN_THAM_QUYEN>`** có hiệu lực thi hành hoặc 30 ngày kể từ ngày 01/9/2017 ( đối với trường hợp Văn bản điều chỉnh địa giới hành chính có hiệu lực thi hành trước ngày 01/9/2017 , **[quỹ tín dụng nhân dân]`<TO_CHUC_DOANH_NGHIEP>`** phải xây dựng phương án chấm dứt hoạt động tại các xã không liền kề với xã **[nơi đặt trụ sở chính]`<DIA_DIEM>`** , gửi **[Ngân hàng Nhà nước]`<CO_QUAN_THAM_QUYEN>`**]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[4:5]`)
- `[e1]` **06/2017/TT-NHNN** → `SO_HIEU` (span: `[6:7]`)
- `[e2]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_BAN_HANH` (span: `[0:3]`)
- `[e3]` **Điều 2** → `DIEU` (span: `[8:10]`)
- `[e4]` **Khoản 1** → `KHOAN` (span: `[11:13]`)
- `[e5]` **b ) Trong thời hạn 30 ngày kể từ ngày Văn bản điều chỉnh địa giới hành chính của Cơ quan Nhà nước có thẩm quyền có hiệu lực thi hành hoặc 30 ngày kể từ ngày 01/9/2017 ( đối với trường hợp Văn bản điều chỉnh địa giới hành chính có hiệu lực thi hành trước ngày 01/9/2017 , quỹ tín dụng nhân dân phải xây dựng phương án chấm dứt hoạt động tại các xã không liền kề với xã nơi đặt trụ sở chính , gửi Ngân hàng Nhà nước** → `DIEM` (span: `[14:80]`)
- `[e6]` **Trong thời hạn 30 ngày** → `THOI_HAN` (span: `[16:20]`) *(lồng trong `e5` (`DIEM`))*
- `[e7]` **Cơ quan Nhà nước có thẩm quyền** → `CO_QUAN_THAM_QUYEN` (span: `[28:32]`) *(lồng trong `e5` (`DIEM`))*
- `[e8]` **Ngân hàng Nhà nước** → `CO_QUAN_THAM_QUYEN` (span: `[78:80]`) *(lồng trong `e5` (`DIEM`))*
- `[e9]` **quỹ tín dụng nhân dân** → `TO_CHUC_DOANH_NGHIEP` (span: `[56:59]`) *(lồng trong `e5` (`DIEM`))*
- `[e10]` **nơi đặt trụ sở chính** → `DIA_DIEM` (span: `[72:76]`) *(lồng trong `e5` (`DIEM`))*

**Quan hệ:**
- (`e1` 06/2017/TT-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Ngân hàng Nhà nước Việt Nam `[CO_QUAN_BAN_HANH]`)
- (`e1` 06/2017/TT-NHNN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 2 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 06/2017/TT-NHNN `[SO_HIEU]`)
- (`e4` Khoản 1 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 2 `[DIEU]`)
- (`e5` b ) Trong thời hạn 30 ngày kể từ ngày Văn bản điều chỉnh địa giới hành chính của Cơ quan Nhà nước có thẩm quyền có hiệu lực thi hành hoặc 30 ngày kể từ ngày 01/9/2017 ( đối với trường hợp Văn bản điều chỉnh địa giới hành chính có hiệu lực thi hành trước ngày 01/9/2017 , quỹ tín dụng nhân dân phải xây dựng phương án chấm dứt hoạt động tại các xã không liền kề với xã nơi đặt trụ sở chính , gửi Ngân hàng Nhà nước `[DIEM]`) ==[ **THUOC_VE** ]==> (`e4` Khoản 1 `[KHOAN]`)


---

### Mẫu #06_2017_TT-NHNN_122819#body_standalone_55 (Loại: `body_standalone`)
> **[Điều 2]`<DIEU>`** . **[Khoản 1]`<KHOAN>`** . **[b ) **[Trong thời hạn 30 ngày]`<THOI_HAN>`** kể từ ngày Văn bản điều chỉnh địa giới hành chính của **[Cơ quan Nhà nước có thẩm quyền]`<CO_QUAN_THAM_QUYEN>`** có hiệu lực thi hành hoặc 30 ngày kể từ ngày 01/9/2017 ( đối với trường hợp Văn bản điều chỉnh địa giới hành chính có hiệu lực thi hành trước ngày 01/9/2017 , **[quỹ tín dụng nhân dân]`<TO_CHUC_DOANH_NGHIEP>`** phải xây dựng phương án chấm dứt hoạt động tại các xã không liền kề với xã **[nơi đặt trụ sở chính]`<DIA_DIEM>`** , gửi **[Ngân hàng Nhà nước]`<CO_QUAN_THAM_QUYEN>`**]`<DIEM>`**

**Thực thể:**
- `[e0]` **Điều 2** → `DIEU` (span: `[0:2]`)
- `[e1]` **Khoản 1** → `KHOAN` (span: `[3:5]`)
- `[e2]` **b ) Trong thời hạn 30 ngày kể từ ngày Văn bản điều chỉnh địa giới hành chính của Cơ quan Nhà nước có thẩm quyền có hiệu lực thi hành hoặc 30 ngày kể từ ngày 01/9/2017 ( đối với trường hợp Văn bản điều chỉnh địa giới hành chính có hiệu lực thi hành trước ngày 01/9/2017 , quỹ tín dụng nhân dân phải xây dựng phương án chấm dứt hoạt động tại các xã không liền kề với xã nơi đặt trụ sở chính , gửi Ngân hàng Nhà nước** → `DIEM` (span: `[6:72]`)
- `[e3]` **Trong thời hạn 30 ngày** → `THOI_HAN` (span: `[8:12]`) *(lồng trong `e2` (`DIEM`))*
- `[e4]` **Cơ quan Nhà nước có thẩm quyền** → `CO_QUAN_THAM_QUYEN` (span: `[20:24]`) *(lồng trong `e2` (`DIEM`))*
- `[e5]` **Ngân hàng Nhà nước** → `CO_QUAN_THAM_QUYEN` (span: `[70:72]`) *(lồng trong `e2` (`DIEM`))*
- `[e6]` **quỹ tín dụng nhân dân** → `TO_CHUC_DOANH_NGHIEP` (span: `[48:51]`) *(lồng trong `e2` (`DIEM`))*
- `[e7]` **nơi đặt trụ sở chính** → `DIA_DIEM` (span: `[64:68]`) *(lồng trong `e2` (`DIEM`))*

**Quan hệ:**
- (`e1` Khoản 1 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 2 `[DIEU]`)
- (`e2` b ) Trong thời hạn 30 ngày kể từ ngày Văn bản điều chỉnh địa giới hành chính của Cơ quan Nhà nước có thẩm quyền có hiệu lực thi hành hoặc 30 ngày kể từ ngày 01/9/2017 ( đối với trường hợp Văn bản điều chỉnh địa giới hành chính có hiệu lực thi hành trước ngày 01/9/2017 , quỹ tín dụng nhân dân phải xây dựng phương án chấm dứt hoạt động tại các xã không liền kề với xã nơi đặt trụ sở chính , gửi Ngân hàng Nhà nước `[DIEM]`) ==[ **THUOC_VE** ]==> (`e1` Khoản 1 `[KHOAN]`)


---

### Mẫu #06_2017_TT-NHNN_122819#body_context_56 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[06/2017/TT-NHNN]`<SO_HIEU>`** ban hành **[ngày 05 tháng 07 năm 2017]`<NGAY_BAN_HANH>`** bởi **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_BAN_HANH>`** . **[Điều 2]`<DIEU>`** . **[Khoản 1]`<KHOAN>`** . **[( ii ) Thực trạng hoạt động tại địa bàn xã không liền kề ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **06/2017/TT-NHNN** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_BAN_HANH` (span: `[11:14]`)
- `[e3]` **ngày 05 tháng 07 năm 2017** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 2** → `DIEU` (span: `[15:17]`)
- `[e5]` **Khoản 1** → `KHOAN` (span: `[18:20]`)
- `[e6]` **( ii ) Thực trạng hoạt động tại địa bàn xã không liền kề ;** → `DIEM` (span: `[21:33]`)

**Quan hệ:**
- (`e1` 06/2017/TT-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Ngân hàng Nhà nước Việt Nam `[CO_QUAN_BAN_HANH]`)
- (`e1` 06/2017/TT-NHNN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 06/2017/TT-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 05 tháng 07 năm 2017 `[NGAY_BAN_HANH]`)
- (`e4` Điều 2 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 06/2017/TT-NHNN `[SO_HIEU]`)
- (`e5` Khoản 1 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 2 `[DIEU]`)
- (`e6` ( ii ) Thực trạng hoạt động tại địa bàn xã không liền kề ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e5` Khoản 1 `[KHOAN]`)


---

### Mẫu #06_2017_TT-NHNN_122819#body_context_57 (Loại: `body_context`)
> **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[06/2017/TT-NHNN]`<SO_HIEU>`** . **[Điều 2]`<DIEU>`** . **[2 . Đối với các xã liền kề với xã **[nơi đặt trụ sở chính]`<DIA_DIEM>`** :]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[4:5]`)
- `[e1]` **06/2017/TT-NHNN** → `SO_HIEU` (span: `[6:7]`)
- `[e2]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_BAN_HANH` (span: `[0:3]`)
- `[e3]` **Điều 2** → `DIEU` (span: `[8:10]`)
- `[e4]` **2 . Đối với các xã liền kề với xã nơi đặt trụ sở chính :** → `KHOAN` (span: `[11:25]`)
- `[e5]` **nơi đặt trụ sở chính** → `DIA_DIEM` (span: `[20:24]`) *(lồng trong `e4` (`KHOAN`))*

**Quan hệ:**
- (`e1` 06/2017/TT-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Ngân hàng Nhà nước Việt Nam `[CO_QUAN_BAN_HANH]`)
- (`e1` 06/2017/TT-NHNN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 2 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 06/2017/TT-NHNN `[SO_HIEU]`)
- (`e4` 2 . Đối với các xã liền kề với xã nơi đặt trụ sở chính : `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 2 `[DIEU]`)


---

### Mẫu #06_2017_TT-NHNN_122819#body_context_58 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[06/2017/TT-NHNN]`<SO_HIEU>`** của **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Thanh tra , giám sát ngân hàng]`<LINH_VUC>`** . **[Điều 2]`<DIEU>`** . **[Khoản 2]`<KHOAN>`** . **[a ) **[Quỹ tín dụng nhân dân]`<TO_CHUC_DOANH_NGHIEP>`** được hoạt động tại các xã liền kề với xã **[nơi đặt trụ sở chính]`<DIA_DIEM>`** , trừ trường hợp **[quy định tại]`<TU_KHOA_PHAP_LY>`** **[điểm b]`<THAM_CHIEU_PHAP_LY>`** khoản này ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **06/2017/TT-NHNN** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_BAN_HANH` (span: `[4:7]`)
- `[e3]` **Thanh tra , giám sát ngân hàng** → `LINH_VUC` (span: `[9:13]`)
- `[e4]` **Điều 2** → `DIEU` (span: `[14:16]`)
- `[e5]` **Khoản 2** → `KHOAN` (span: `[17:19]`)
- `[e6]` **a ) Quỹ tín dụng nhân dân được hoạt động tại các xã liền kề với xã nơi đặt trụ sở chính , trừ trường hợp quy định tại điểm b khoản này ;** → `DIEM` (span: `[20:48]`)
- `[e7]` **điểm b** → `THAM_CHIEU_PHAP_LY` (span: `[43:45]`) *(lồng trong `e6` (`DIEM`))*
- `[e8]` **quy định tại** → `TU_KHOA_PHAP_LY` (span: `[41:43]`) *(lồng trong `e6` (`DIEM`))*
- `[e9]` **Quỹ tín dụng nhân dân** → `TO_CHUC_DOANH_NGHIEP` (span: `[22:25]`) *(lồng trong `e6` (`DIEM`))*
- `[e10]` **nơi đặt trụ sở chính** → `DIA_DIEM` (span: `[34:38]`) *(lồng trong `e6` (`DIEM`))*

**Quan hệ:**
- (`e1` 06/2017/TT-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Ngân hàng Nhà nước Việt Nam `[CO_QUAN_BAN_HANH]`)
- (`e1` 06/2017/TT-NHNN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 06/2017/TT-NHNN `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Thanh tra , giám sát ngân hàng `[LINH_VUC]`)
- (`e4` Điều 2 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 06/2017/TT-NHNN `[SO_HIEU]`)
- (`e5` Khoản 2 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 2 `[DIEU]`)
- (`e6` a ) Quỹ tín dụng nhân dân được hoạt động tại các xã liền kề với xã nơi đặt trụ sở chính , trừ trường hợp quy định tại điểm b khoản này ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e5` Khoản 2 `[KHOAN]`)
- (`e1` 06/2017/TT-NHNN `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Thanh tra , giám sát ngân hàng `[LINH_VUC]`)
- (`e6` a ) Quỹ tín dụng nhân dân được hoạt động tại các xã liền kề với xã nơi đặt trụ sở chính , trừ trường hợp quy định tại điểm b khoản này ; `[DIEM]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Thanh tra , giám sát ngân hàng `[LINH_VUC]`)
- (`e8` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e7` điểm b `[THAM_CHIEU_PHAP_LY]`)
- (`e6` a ) Quỹ tín dụng nhân dân được hoạt động tại các xã liền kề với xã nơi đặt trụ sở chính , trừ trường hợp quy định tại điểm b khoản này ; `[DIEM]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e7` điểm b `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #06_2017_TT-NHNN_122819#body_standalone_59 (Loại: `body_standalone`)
> **[Điều 2]`<DIEU>`** . **[Khoản 2]`<KHOAN>`** . **[a ) **[Quỹ tín dụng nhân dân]`<TO_CHUC_DOANH_NGHIEP>`** được hoạt động tại các xã liền kề với xã **[nơi đặt trụ sở chính]`<DIA_DIEM>`** , trừ trường hợp **[quy định tại]`<TU_KHOA_PHAP_LY>`** **[điểm b]`<THAM_CHIEU_PHAP_LY>`** khoản này ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Điều 2** → `DIEU` (span: `[0:2]`)
- `[e1]` **Khoản 2** → `KHOAN` (span: `[3:5]`)
- `[e2]` **a ) Quỹ tín dụng nhân dân được hoạt động tại các xã liền kề với xã nơi đặt trụ sở chính , trừ trường hợp quy định tại điểm b khoản này ;** → `DIEM` (span: `[6:34]`)
- `[e3]` **điểm b** → `THAM_CHIEU_PHAP_LY` (span: `[29:31]`) *(lồng trong `e2` (`DIEM`))*
- `[e4]` **quy định tại** → `TU_KHOA_PHAP_LY` (span: `[27:29]`) *(lồng trong `e2` (`DIEM`))*
- `[e5]` **Quỹ tín dụng nhân dân** → `TO_CHUC_DOANH_NGHIEP` (span: `[8:11]`) *(lồng trong `e2` (`DIEM`))*
- `[e6]` **nơi đặt trụ sở chính** → `DIA_DIEM` (span: `[20:24]`) *(lồng trong `e2` (`DIEM`))*

**Quan hệ:**
- (`e1` Khoản 2 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 2 `[DIEU]`)
- (`e2` a ) Quỹ tín dụng nhân dân được hoạt động tại các xã liền kề với xã nơi đặt trụ sở chính , trừ trường hợp quy định tại điểm b khoản này ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e1` Khoản 2 `[KHOAN]`)
- (`e4` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` điểm b `[THAM_CHIEU_PHAP_LY]`)
- (`e2` a ) Quỹ tín dụng nhân dân được hoạt động tại các xã liền kề với xã nơi đặt trụ sở chính , trừ trường hợp quy định tại điểm b khoản này ; `[DIEM]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` điểm b `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #06_2017_TT-NHNN_122819#body_context_60 (Loại: `body_context`)
> **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[06/2017/TT-NHNN]`<SO_HIEU>`** . **[Điều 2]`<DIEU>`** . **[Khoản 2]`<KHOAN>`** . **[b ) Trường hợp tại thời điểm Văn bản điều chỉnh địa giới hành chính của **[Cơ quan Nhà nước có thẩm quyền]`<CO_QUAN_THAM_QUYEN>`** có hiệu lực thi hành hoặc kể từ ngày 01/9/2017 ( đối với trường hợp Văn bản điều chỉnh địa giới hành chính có hiệu lực thi hành trước ngày 01/9/2017 ) , **[quỹ tín dụng nhân dân]`<TO_CHUC_DOANH_NGHIEP>`** đang thực hiện phương án **[theo quy định tại]`<TU_KHOA_PHAP_LY>`** **[khoản 2 , khoản 3 Điều 47 Thông tư này]`<THAM_CHIEU_PHAP_LY>`** thì thực hiện theo **[phương án xử lý]`<GIAY_TO_HO_SO>`** đã báo cáo ” .]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[4:5]`)
- `[e1]` **06/2017/TT-NHNN** → `SO_HIEU` (span: `[6:7]`)
- `[e2]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_BAN_HANH` (span: `[0:3]`)
- `[e3]` **Điều 2** → `DIEU` (span: `[8:10]`)
- `[e4]` **Khoản 2** → `KHOAN` (span: `[11:13]`)
- `[e5]` **b ) Trường hợp tại thời điểm Văn bản điều chỉnh địa giới hành chính của Cơ quan Nhà nước có thẩm quyền có hiệu lực thi hành hoặc kể từ ngày 01/9/2017 ( đối với trường hợp Văn bản điều chỉnh địa giới hành chính có hiệu lực thi hành trước ngày 01/9/2017 ) , quỹ tín dụng nhân dân đang thực hiện phương án theo quy định tại khoản 2 , khoản 3 Điều 47 Thông tư này thì thực hiện theo phương án xử lý đã báo cáo ” .** → `DIEM` (span: `[14:78]`)
- `[e6]` **khoản 2 , khoản 3 Điều 47 Thông tư này** → `THAM_CHIEU_PHAP_LY` (span: `[60:69]`) *(lồng trong `e5` (`DIEM`))*
- `[e7]` **theo quy định tại** → `TU_KHOA_PHAP_LY` (span: `[57:60]`) *(lồng trong `e5` (`DIEM`))*
- `[e8]` **Cơ quan Nhà nước có thẩm quyền** → `CO_QUAN_THAM_QUYEN` (span: `[24:28]`) *(lồng trong `e5` (`DIEM`))*
- `[e9]` **phương án xử lý** → `GIAY_TO_HO_SO` (span: `[72:74]`) *(lồng trong `e5` (`DIEM`))*
- `[e10]` **quỹ tín dụng nhân dân** → `TO_CHUC_DOANH_NGHIEP` (span: `[51:54]`) *(lồng trong `e5` (`DIEM`))*

**Quan hệ:**
- (`e1` 06/2017/TT-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Ngân hàng Nhà nước Việt Nam `[CO_QUAN_BAN_HANH]`)
- (`e1` 06/2017/TT-NHNN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 2 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 06/2017/TT-NHNN `[SO_HIEU]`)
- (`e4` Khoản 2 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 2 `[DIEU]`)
- (`e5` b ) Trường hợp tại thời điểm Văn bản điều chỉnh địa giới hành chính của Cơ quan Nhà nước có thẩm quyền có hiệu lực thi hành hoặc kể từ ngày 01/9/2017 ( đối với trường hợp Văn bản điều chỉnh địa giới hành chính có hiệu lực thi hành trước ngày 01/9/2017 ) , quỹ tín dụng nhân dân đang thực hiện phương án theo quy định tại khoản 2 , khoản 3 Điều 47 Thông tư này thì thực hiện theo phương án xử lý đã báo cáo ” . `[DIEM]`) ==[ **THUOC_VE** ]==> (`e4` Khoản 2 `[KHOAN]`)
- (`e7` theo quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e6` khoản 2 , khoản 3 Điều 47 Thông tư này `[THAM_CHIEU_PHAP_LY]`)
- (`e5` b ) Trường hợp tại thời điểm Văn bản điều chỉnh địa giới hành chính của Cơ quan Nhà nước có thẩm quyền có hiệu lực thi hành hoặc kể từ ngày 01/9/2017 ( đối với trường hợp Văn bản điều chỉnh địa giới hành chính có hiệu lực thi hành trước ngày 01/9/2017 ) , quỹ tín dụng nhân dân đang thực hiện phương án theo quy định tại khoản 2 , khoản 3 Điều 47 Thông tư này thì thực hiện theo phương án xử lý đã báo cáo ” . `[DIEM]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e6` khoản 2 , khoản 3 Điều 47 Thông tư này `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #06_2017_TT-NHNN_122819#body_standalone_61 (Loại: `body_standalone`)
> **[Điều 2]`<DIEU>`** . **[Khoản 2]`<KHOAN>`** . **[b ) Trường hợp tại thời điểm Văn bản điều chỉnh địa giới hành chính của **[Cơ quan Nhà nước có thẩm quyền]`<CO_QUAN_THAM_QUYEN>`** có hiệu lực thi hành hoặc kể từ ngày 01/9/2017 ( đối với trường hợp Văn bản điều chỉnh địa giới hành chính có hiệu lực thi hành trước ngày 01/9/2017 ) , **[quỹ tín dụng nhân dân]`<TO_CHUC_DOANH_NGHIEP>`** đang thực hiện phương án **[theo quy định tại]`<TU_KHOA_PHAP_LY>`** **[khoản 2 , khoản 3 Điều 47 Thông tư này]`<THAM_CHIEU_PHAP_LY>`** thì thực hiện theo **[phương án xử lý]`<GIAY_TO_HO_SO>`** đã báo cáo ” .]`<DIEM>`**

**Thực thể:**
- `[e0]` **Điều 2** → `DIEU` (span: `[0:2]`)
- `[e1]` **Khoản 2** → `KHOAN` (span: `[3:5]`)
- `[e2]` **b ) Trường hợp tại thời điểm Văn bản điều chỉnh địa giới hành chính của Cơ quan Nhà nước có thẩm quyền có hiệu lực thi hành hoặc kể từ ngày 01/9/2017 ( đối với trường hợp Văn bản điều chỉnh địa giới hành chính có hiệu lực thi hành trước ngày 01/9/2017 ) , quỹ tín dụng nhân dân đang thực hiện phương án theo quy định tại khoản 2 , khoản 3 Điều 47 Thông tư này thì thực hiện theo phương án xử lý đã báo cáo ” .** → `DIEM` (span: `[6:70]`)
- `[e3]` **khoản 2 , khoản 3 Điều 47 Thông tư này** → `THAM_CHIEU_PHAP_LY` (span: `[52:61]`) *(lồng trong `e2` (`DIEM`))*
- `[e4]` **theo quy định tại** → `TU_KHOA_PHAP_LY` (span: `[49:52]`) *(lồng trong `e2` (`DIEM`))*
- `[e5]` **Cơ quan Nhà nước có thẩm quyền** → `CO_QUAN_THAM_QUYEN` (span: `[16:20]`) *(lồng trong `e2` (`DIEM`))*
- `[e6]` **phương án xử lý** → `GIAY_TO_HO_SO` (span: `[64:66]`) *(lồng trong `e2` (`DIEM`))*
- `[e7]` **quỹ tín dụng nhân dân** → `TO_CHUC_DOANH_NGHIEP` (span: `[43:46]`) *(lồng trong `e2` (`DIEM`))*

**Quan hệ:**
- (`e1` Khoản 2 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 2 `[DIEU]`)
- (`e2` b ) Trường hợp tại thời điểm Văn bản điều chỉnh địa giới hành chính của Cơ quan Nhà nước có thẩm quyền có hiệu lực thi hành hoặc kể từ ngày 01/9/2017 ( đối với trường hợp Văn bản điều chỉnh địa giới hành chính có hiệu lực thi hành trước ngày 01/9/2017 ) , quỹ tín dụng nhân dân đang thực hiện phương án theo quy định tại khoản 2 , khoản 3 Điều 47 Thông tư này thì thực hiện theo phương án xử lý đã báo cáo ” . `[DIEM]`) ==[ **THUOC_VE** ]==> (`e1` Khoản 2 `[KHOAN]`)
- (`e4` theo quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` khoản 2 , khoản 3 Điều 47 Thông tư này `[THAM_CHIEU_PHAP_LY]`)
- (`e2` b ) Trường hợp tại thời điểm Văn bản điều chỉnh địa giới hành chính của Cơ quan Nhà nước có thẩm quyền có hiệu lực thi hành hoặc kể từ ngày 01/9/2017 ( đối với trường hợp Văn bản điều chỉnh địa giới hành chính có hiệu lực thi hành trước ngày 01/9/2017 ) , quỹ tín dụng nhân dân đang thực hiện phương án theo quy định tại khoản 2 , khoản 3 Điều 47 Thông tư này thì thực hiện theo phương án xử lý đã báo cáo ” . `[DIEM]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` khoản 2 , khoản 3 Điều 47 Thông tư này `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #06_2017_TT-NHNN_122819#body_context_62 (Loại: `body_context`)
> **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[06/2017/TT-NHNN]`<SO_HIEU>`** . **[Điều 2]`<DIEU>`** . **[1 . Cơ quan **[Thanh tra , giám sát ngân hàng]`<CO_QUAN_THAM_QUYEN>`** :]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[4:5]`)
- `[e1]` **06/2017/TT-NHNN** → `SO_HIEU` (span: `[6:7]`)
- `[e2]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_BAN_HANH` (span: `[0:3]`)
- `[e3]` **Điều 2** → `DIEU` (span: `[8:10]`)
- `[e4]` **1 . Cơ quan Thanh tra , giám sát ngân hàng :** → `KHOAN` (span: `[11:19]`)
- `[e5]` **Thanh tra , giám sát ngân hàng** → `CO_QUAN_THAM_QUYEN` (span: `[14:18]`) *(lồng trong `e4` (`KHOAN`))*

**Quan hệ:**
- (`e1` 06/2017/TT-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Ngân hàng Nhà nước Việt Nam `[CO_QUAN_BAN_HANH]`)
- (`e1` 06/2017/TT-NHNN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 2 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 06/2017/TT-NHNN `[SO_HIEU]`)
- (`e4` 1 . Cơ quan Thanh tra , giám sát ngân hàng : `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 2 `[DIEU]`)


---

### Mẫu #06_2017_TT-NHNN_122819#body_standalone_63 (Loại: `body_standalone`)
> **[Điều 2]`<DIEU>`** . **[1 . Cơ quan **[Thanh tra , giám sát ngân hàng]`<CO_QUAN_THAM_QUYEN>`** :]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 2** → `DIEU` (span: `[0:2]`)
- `[e1]` **1 . Cơ quan Thanh tra , giám sát ngân hàng :** → `KHOAN` (span: `[3:11]`)
- `[e2]` **Thanh tra , giám sát ngân hàng** → `CO_QUAN_THAM_QUYEN` (span: `[6:10]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 1 . Cơ quan Thanh tra , giám sát ngân hàng : `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 2 `[DIEU]`)


---

### Mẫu #06_2017_TT-NHNN_122819#body_context_64 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[06/2017/TT-NHNN]`<SO_HIEU>`** của **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Thanh tra , giám sát ngân hàng]`<LINH_VUC>`** . **[Điều 2]`<DIEU>`** . **[Khoản 1]`<KHOAN>`** . **[a ) Đầu mối tiếp nhận báo cáo của **[Ngân hàng Nhà nước]`<CO_QUAN_THAM_QUYEN>`** chi nhánh **[theo quy định tại]`<TU_KHOA_PHAP_LY>`** **[điểm b , điểm d khoản 2 Điều này]`<THAM_CHIEU_PHAP_LY>`** và theo quy định của pháp luật ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **06/2017/TT-NHNN** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_BAN_HANH` (span: `[4:7]`)
- `[e3]` **Thanh tra , giám sát ngân hàng** → `LINH_VUC` (span: `[9:13]`)
- `[e4]` **Điều 2** → `DIEU` (span: `[14:16]`)
- `[e5]` **Khoản 1** → `KHOAN` (span: `[17:19]`)
- `[e6]` **a ) Đầu mối tiếp nhận báo cáo của Ngân hàng Nhà nước chi nhánh theo quy định tại điểm b , điểm d khoản 2 Điều này và theo quy định của pháp luật ;** → `DIEM` (span: `[20:47]`)
- `[e7]` **điểm b , điểm d khoản 2 Điều này** → `THAM_CHIEU_PHAP_LY` (span: `[32:41]`) *(lồng trong `e6` (`DIEM`))*
- `[e8]` **theo quy định tại** → `TU_KHOA_PHAP_LY` (span: `[29:32]`) *(lồng trong `e6` (`DIEM`))*
- `[e9]` **Ngân hàng Nhà nước** → `CO_QUAN_THAM_QUYEN` (span: `[26:28]`) *(lồng trong `e6` (`DIEM`))*

**Quan hệ:**
- (`e1` 06/2017/TT-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Ngân hàng Nhà nước Việt Nam `[CO_QUAN_BAN_HANH]`)
- (`e1` 06/2017/TT-NHNN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 06/2017/TT-NHNN `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Thanh tra , giám sát ngân hàng `[LINH_VUC]`)
- (`e4` Điều 2 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 06/2017/TT-NHNN `[SO_HIEU]`)
- (`e5` Khoản 1 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 2 `[DIEU]`)
- (`e6` a ) Đầu mối tiếp nhận báo cáo của Ngân hàng Nhà nước chi nhánh theo quy định tại điểm b , điểm d khoản 2 Điều này và theo quy định của pháp luật ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e5` Khoản 1 `[KHOAN]`)
- (`e1` 06/2017/TT-NHNN `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Thanh tra , giám sát ngân hàng `[LINH_VUC]`)
- (`e6` a ) Đầu mối tiếp nhận báo cáo của Ngân hàng Nhà nước chi nhánh theo quy định tại điểm b , điểm d khoản 2 Điều này và theo quy định của pháp luật ; `[DIEM]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Thanh tra , giám sát ngân hàng `[LINH_VUC]`)
- (`e8` theo quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e7` điểm b , điểm d khoản 2 Điều này `[THAM_CHIEU_PHAP_LY]`)
- (`e6` a ) Đầu mối tiếp nhận báo cáo của Ngân hàng Nhà nước chi nhánh theo quy định tại điểm b , điểm d khoản 2 Điều này và theo quy định của pháp luật ; `[DIEM]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e7` điểm b , điểm d khoản 2 Điều này `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #06_2017_TT-NHNN_122819#body_standalone_65 (Loại: `body_standalone`)
> **[Điều 2]`<DIEU>`** . **[Khoản 1]`<KHOAN>`** . **[a ) Đầu mối tiếp nhận báo cáo của **[Ngân hàng Nhà nước]`<CO_QUAN_THAM_QUYEN>`** chi nhánh **[theo quy định tại]`<TU_KHOA_PHAP_LY>`** **[điểm b , điểm d khoản 2 Điều này]`<THAM_CHIEU_PHAP_LY>`** và theo quy định của pháp luật ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Điều 2** → `DIEU` (span: `[0:2]`)
- `[e1]` **Khoản 1** → `KHOAN` (span: `[3:5]`)
- `[e2]` **a ) Đầu mối tiếp nhận báo cáo của Ngân hàng Nhà nước chi nhánh theo quy định tại điểm b , điểm d khoản 2 Điều này và theo quy định của pháp luật ;** → `DIEM` (span: `[6:33]`)
- `[e3]` **điểm b , điểm d khoản 2 Điều này** → `THAM_CHIEU_PHAP_LY` (span: `[18:27]`) *(lồng trong `e2` (`DIEM`))*
- `[e4]` **theo quy định tại** → `TU_KHOA_PHAP_LY` (span: `[15:18]`) *(lồng trong `e2` (`DIEM`))*
- `[e5]` **Ngân hàng Nhà nước** → `CO_QUAN_THAM_QUYEN` (span: `[12:14]`) *(lồng trong `e2` (`DIEM`))*

**Quan hệ:**
- (`e1` Khoản 1 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 2 `[DIEU]`)
- (`e2` a ) Đầu mối tiếp nhận báo cáo của Ngân hàng Nhà nước chi nhánh theo quy định tại điểm b , điểm d khoản 2 Điều này và theo quy định của pháp luật ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e1` Khoản 1 `[KHOAN]`)
- (`e4` theo quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` điểm b , điểm d khoản 2 Điều này `[THAM_CHIEU_PHAP_LY]`)
- (`e2` a ) Đầu mối tiếp nhận báo cáo của Ngân hàng Nhà nước chi nhánh theo quy định tại điểm b , điểm d khoản 2 Điều này và theo quy định của pháp luật ; `[DIEM]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` điểm b , điểm d khoản 2 Điều này `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #06_2017_TT-NHNN_122819#body_context_66 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[06/2017/TT-NHNN]`<SO_HIEU>`** ban hành **[ngày 05 tháng 07 năm 2017]`<NGAY_BAN_HANH>`** bởi **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_BAN_HANH>`** . **[Điều 2]`<DIEU>`** . **[Khoản 1]`<KHOAN>`** . **[b ) Thanh tra , giám sát , xử lý đối với các hành vi vi phạm của **[quỹ tín dụng nhân dân]`<TO_CHUC_DOANH_NGHIEP>`** trên địa bàn địa bàn tỉnh , thành phố nơi có Cục **[thanh tra , giám sát ngân hàng]`<CO_QUAN_THAM_QUYEN>`** trong việc thực hiện các **[quy định tại]`<TU_KHOA_PHAP_LY>`** **[Thông tư này]`<THAM_CHIEU_PHAP_LY>`** và các quy định của pháp luật có liên quan ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **06/2017/TT-NHNN** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_BAN_HANH` (span: `[11:14]`)
- `[e3]` **ngày 05 tháng 07 năm 2017** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 2** → `DIEU` (span: `[15:17]`)
- `[e5]` **Khoản 1** → `KHOAN` (span: `[18:20]`)
- `[e6]` **b ) Thanh tra , giám sát , xử lý đối với các hành vi vi phạm của quỹ tín dụng nhân dân trên địa bàn địa bàn tỉnh , thành phố nơi có Cục thanh tra , giám sát ngân hàng trong việc thực hiện các quy định tại Thông tư này và các quy định của pháp luật có liên quan ;** → `DIEM` (span: `[21:65]`)
- `[e7]` **Thông tư này** → `THAM_CHIEU_PHAP_LY` (span: `[55:57]`) *(lồng trong `e6` (`DIEM`))*
- `[e8]` **quy định tại** → `TU_KHOA_PHAP_LY` (span: `[53:55]`) *(lồng trong `e6` (`DIEM`))*
- `[e9]` **thanh tra , giám sát ngân hàng** → `CO_QUAN_THAM_QUYEN` (span: `[45:49]`) *(lồng trong `e6` (`DIEM`))*
- `[e10]` **quỹ tín dụng nhân dân** → `TO_CHUC_DOANH_NGHIEP` (span: `[33:36]`) *(lồng trong `e6` (`DIEM`))*

**Quan hệ:**
- (`e1` 06/2017/TT-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Ngân hàng Nhà nước Việt Nam `[CO_QUAN_BAN_HANH]`)
- (`e1` 06/2017/TT-NHNN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 06/2017/TT-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 05 tháng 07 năm 2017 `[NGAY_BAN_HANH]`)
- (`e4` Điều 2 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 06/2017/TT-NHNN `[SO_HIEU]`)
- (`e5` Khoản 1 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 2 `[DIEU]`)
- (`e6` b ) Thanh tra , giám sát , xử lý đối với các hành vi vi phạm của quỹ tín dụng nhân dân trên địa bàn địa bàn tỉnh , thành phố nơi có Cục thanh tra , giám sát ngân hàng trong việc thực hiện các quy định tại Thông tư này và các quy định của pháp luật có liên quan ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e5` Khoản 1 `[KHOAN]`)
- (`e8` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e7` Thông tư này `[THAM_CHIEU_PHAP_LY]`)
- (`e6` b ) Thanh tra , giám sát , xử lý đối với các hành vi vi phạm của quỹ tín dụng nhân dân trên địa bàn địa bàn tỉnh , thành phố nơi có Cục thanh tra , giám sát ngân hàng trong việc thực hiện các quy định tại Thông tư này và các quy định của pháp luật có liên quan ; `[DIEM]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e7` Thông tư này `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #06_2017_TT-NHNN_122819#body_standalone_67 (Loại: `body_standalone`)
> **[Điều 2]`<DIEU>`** . **[Khoản 1]`<KHOAN>`** . **[b ) Thanh tra , giám sát , xử lý đối với các hành vi vi phạm của **[quỹ tín dụng nhân dân]`<TO_CHUC_DOANH_NGHIEP>`** trên địa bàn địa bàn tỉnh , thành phố nơi có Cục **[thanh tra , giám sát ngân hàng]`<CO_QUAN_THAM_QUYEN>`** trong việc thực hiện các **[quy định tại]`<TU_KHOA_PHAP_LY>`** **[Thông tư này]`<THAM_CHIEU_PHAP_LY>`** và các quy định của pháp luật có liên quan ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Điều 2** → `DIEU` (span: `[0:2]`)
- `[e1]` **Khoản 1** → `KHOAN` (span: `[3:5]`)
- `[e2]` **b ) Thanh tra , giám sát , xử lý đối với các hành vi vi phạm của quỹ tín dụng nhân dân trên địa bàn địa bàn tỉnh , thành phố nơi có Cục thanh tra , giám sát ngân hàng trong việc thực hiện các quy định tại Thông tư này và các quy định của pháp luật có liên quan ;** → `DIEM` (span: `[6:50]`)
- `[e3]` **Thông tư này** → `THAM_CHIEU_PHAP_LY` (span: `[40:42]`) *(lồng trong `e2` (`DIEM`))*
- `[e4]` **quy định tại** → `TU_KHOA_PHAP_LY` (span: `[38:40]`) *(lồng trong `e2` (`DIEM`))*
- `[e5]` **thanh tra , giám sát ngân hàng** → `CO_QUAN_THAM_QUYEN` (span: `[30:34]`) *(lồng trong `e2` (`DIEM`))*
- `[e6]` **quỹ tín dụng nhân dân** → `TO_CHUC_DOANH_NGHIEP` (span: `[18:21]`) *(lồng trong `e2` (`DIEM`))*

**Quan hệ:**
- (`e1` Khoản 1 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 2 `[DIEU]`)
- (`e2` b ) Thanh tra , giám sát , xử lý đối với các hành vi vi phạm của quỹ tín dụng nhân dân trên địa bàn địa bàn tỉnh , thành phố nơi có Cục thanh tra , giám sát ngân hàng trong việc thực hiện các quy định tại Thông tư này và các quy định của pháp luật có liên quan ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e1` Khoản 1 `[KHOAN]`)
- (`e4` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Thông tư này `[THAM_CHIEU_PHAP_LY]`)
- (`e2` b ) Thanh tra , giám sát , xử lý đối với các hành vi vi phạm của quỹ tín dụng nhân dân trên địa bàn địa bàn tỉnh , thành phố nơi có Cục thanh tra , giám sát ngân hàng trong việc thực hiện các quy định tại Thông tư này và các quy định của pháp luật có liên quan ; `[DIEM]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Thông tư này `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #06_2017_TT-NHNN_122819#body_context_68 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[06/2017/TT-NHNN]`<SO_HIEU>`** của **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Thanh tra , giám sát ngân hàng]`<LINH_VUC>`** . **[Điều 2]`<DIEU>`** . **[Khoản 1]`<KHOAN>`** . **[c ) Chỉ đạo , hướng dẫn , giám sát , kiểm tra **[quỹ tín dụng nhân dân]`<TO_CHUC_DOANH_NGHIEP>`** đặt trụ sở chính nơi có Cục **[thanh tra , giám sát ngân hàng]`<CO_QUAN_THAM_QUYEN>`** trong việc thực hiện quy định về chuyển tiếp và xử lý sau chuyển tiếp tại **[các Điều 46 , 47 , 47a và Điều 51 Thông tư này]`<THAM_CHIEU_PHAP_LY>`** ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **06/2017/TT-NHNN** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_BAN_HANH` (span: `[4:7]`)
- `[e3]` **Thanh tra , giám sát ngân hàng** → `LINH_VUC` (span: `[9:13]`)
- `[e4]` **Điều 2** → `DIEU` (span: `[14:16]`)
- `[e5]` **Khoản 1** → `KHOAN` (span: `[17:19]`)
- `[e6]` **c ) Chỉ đạo , hướng dẫn , giám sát , kiểm tra quỹ tín dụng nhân dân đặt trụ sở chính nơi có Cục thanh tra , giám sát ngân hàng trong việc thực hiện quy định về chuyển tiếp và xử lý sau chuyển tiếp tại các Điều 46 , 47 , 47a và Điều 51 Thông tư này ;** → `DIEM` (span: `[20:66]`)
- `[e7]` **các Điều 46 , 47 , 47a và Điều 51 Thông tư này** → `THAM_CHIEU_PHAP_LY` (span: `[53:65]`) *(lồng trong `e6` (`DIEM`))*
- `[e8]` **thanh tra , giám sát ngân hàng** → `CO_QUAN_THAM_QUYEN` (span: `[38:42]`) *(lồng trong `e6` (`DIEM`))*
- `[e9]` **quỹ tín dụng nhân dân** → `TO_CHUC_DOANH_NGHIEP` (span: `[29:32]`) *(lồng trong `e6` (`DIEM`))*

**Quan hệ:**
- (`e1` 06/2017/TT-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Ngân hàng Nhà nước Việt Nam `[CO_QUAN_BAN_HANH]`)
- (`e1` 06/2017/TT-NHNN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 06/2017/TT-NHNN `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Thanh tra , giám sát ngân hàng `[LINH_VUC]`)
- (`e4` Điều 2 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 06/2017/TT-NHNN `[SO_HIEU]`)
- (`e5` Khoản 1 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 2 `[DIEU]`)
- (`e6` c ) Chỉ đạo , hướng dẫn , giám sát , kiểm tra quỹ tín dụng nhân dân đặt trụ sở chính nơi có Cục thanh tra , giám sát ngân hàng trong việc thực hiện quy định về chuyển tiếp và xử lý sau chuyển tiếp tại các Điều 46 , 47 , 47a và Điều 51 Thông tư này ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e5` Khoản 1 `[KHOAN]`)
- (`e1` 06/2017/TT-NHNN `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Thanh tra , giám sát ngân hàng `[LINH_VUC]`)
- (`e6` c ) Chỉ đạo , hướng dẫn , giám sát , kiểm tra quỹ tín dụng nhân dân đặt trụ sở chính nơi có Cục thanh tra , giám sát ngân hàng trong việc thực hiện quy định về chuyển tiếp và xử lý sau chuyển tiếp tại các Điều 46 , 47 , 47a và Điều 51 Thông tư này ; `[DIEM]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Thanh tra , giám sát ngân hàng `[LINH_VUC]`)
- (`e6` c ) Chỉ đạo , hướng dẫn , giám sát , kiểm tra quỹ tín dụng nhân dân đặt trụ sở chính nơi có Cục thanh tra , giám sát ngân hàng trong việc thực hiện quy định về chuyển tiếp và xử lý sau chuyển tiếp tại các Điều 46 , 47 , 47a và Điều 51 Thông tư này ; `[DIEM]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e7` các Điều 46 , 47 , 47a và Điều 51 Thông tư này `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #06_2017_TT-NHNN_122819#body_standalone_69 (Loại: `body_standalone`)
> **[Điều 2]`<DIEU>`** . **[Khoản 1]`<KHOAN>`** . **[c ) Chỉ đạo , hướng dẫn , giám sát , kiểm tra **[quỹ tín dụng nhân dân]`<TO_CHUC_DOANH_NGHIEP>`** đặt trụ sở chính nơi có Cục **[thanh tra , giám sát ngân hàng]`<CO_QUAN_THAM_QUYEN>`** trong việc thực hiện quy định về chuyển tiếp và xử lý sau chuyển tiếp tại **[các Điều 46 , 47 , 47a và Điều 51 Thông tư này]`<THAM_CHIEU_PHAP_LY>`** ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Điều 2** → `DIEU` (span: `[0:2]`)
- `[e1]` **Khoản 1** → `KHOAN` (span: `[3:5]`)
- `[e2]` **c ) Chỉ đạo , hướng dẫn , giám sát , kiểm tra quỹ tín dụng nhân dân đặt trụ sở chính nơi có Cục thanh tra , giám sát ngân hàng trong việc thực hiện quy định về chuyển tiếp và xử lý sau chuyển tiếp tại các Điều 46 , 47 , 47a và Điều 51 Thông tư này ;** → `DIEM` (span: `[6:52]`)
- `[e3]` **các Điều 46 , 47 , 47a và Điều 51 Thông tư này** → `THAM_CHIEU_PHAP_LY` (span: `[39:51]`) *(lồng trong `e2` (`DIEM`))*
- `[e4]` **thanh tra , giám sát ngân hàng** → `CO_QUAN_THAM_QUYEN` (span: `[24:28]`) *(lồng trong `e2` (`DIEM`))*
- `[e5]` **quỹ tín dụng nhân dân** → `TO_CHUC_DOANH_NGHIEP` (span: `[15:18]`) *(lồng trong `e2` (`DIEM`))*

**Quan hệ:**
- (`e1` Khoản 1 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 2 `[DIEU]`)
- (`e2` c ) Chỉ đạo , hướng dẫn , giám sát , kiểm tra quỹ tín dụng nhân dân đặt trụ sở chính nơi có Cục thanh tra , giám sát ngân hàng trong việc thực hiện quy định về chuyển tiếp và xử lý sau chuyển tiếp tại các Điều 46 , 47 , 47a và Điều 51 Thông tư này ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e1` Khoản 1 `[KHOAN]`)
- (`e2` c ) Chỉ đạo , hướng dẫn , giám sát , kiểm tra quỹ tín dụng nhân dân đặt trụ sở chính nơi có Cục thanh tra , giám sát ngân hàng trong việc thực hiện quy định về chuyển tiếp và xử lý sau chuyển tiếp tại các Điều 46 , 47 , 47a và Điều 51 Thông tư này ; `[DIEM]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` các Điều 46 , 47 , 47a và Điều 51 Thông tư này `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #06_2017_TT-NHNN_122819#body_context_70 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[06/2017/TT-NHNN]`<SO_HIEU>`** ban hành **[ngày 05 tháng 07 năm 2017]`<NGAY_BAN_HANH>`** bởi **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_BAN_HANH>`** . **[Điều 2]`<DIEU>`** . **[2 . **[Ngân hàng Nhà nước chi nhánh tỉnh , thành phố trực thuộc Trung ương]`<CO_QUAN_THAM_QUYEN>`** :]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **06/2017/TT-NHNN** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_BAN_HANH` (span: `[11:14]`)
- `[e3]` **ngày 05 tháng 07 năm 2017** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 2** → `DIEU` (span: `[15:17]`)
- `[e5]` **2 . Ngân hàng Nhà nước chi nhánh tỉnh , thành phố trực thuộc Trung ương :** → `KHOAN` (span: `[18:29]`)
- `[e6]` **Ngân hàng Nhà nước chi nhánh tỉnh , thành phố trực thuộc Trung ương** → `CO_QUAN_THAM_QUYEN` (span: `[20:28]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 06/2017/TT-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Ngân hàng Nhà nước Việt Nam `[CO_QUAN_BAN_HANH]`)
- (`e1` 06/2017/TT-NHNN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 06/2017/TT-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 05 tháng 07 năm 2017 `[NGAY_BAN_HANH]`)
- (`e4` Điều 2 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 06/2017/TT-NHNN `[SO_HIEU]`)
- (`e5` 2 . Ngân hàng Nhà nước chi nhánh tỉnh , thành phố trực thuộc Trung ương : `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 2 `[DIEU]`)


---

### Mẫu #06_2017_TT-NHNN_122819#body_context_71 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[06/2017/TT-NHNN]`<SO_HIEU>`** của **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Thanh tra , giám sát ngân hàng]`<LINH_VUC>`** . **[Điều 2]`<DIEU>`** . **[Khoản 2]`<KHOAN>`** . **[a ) Quản lý , thanh tra , giám sát , xử lý đối với các hành vi vi phạm của **[quỹ tín dụng nhân dân]`<TO_CHUC_DOANH_NGHIEP>`** **[trên địa bàn tỉnh]`<DIA_DIEM>`** , thành phố nơi không có Cục **[thanh tra , giám sát ngân hàng]`<CO_QUAN_THAM_QUYEN>`** trong việc thực hiện các **[quy định tại]`<TU_KHOA_PHAP_LY>`** **[Thông tư này]`<THAM_CHIEU_PHAP_LY>`** và các quy định của pháp luật có liên quan ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **06/2017/TT-NHNN** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_BAN_HANH` (span: `[4:7]`)
- `[e3]` **Thanh tra , giám sát ngân hàng** → `LINH_VUC` (span: `[9:13]`)
- `[e4]` **Điều 2** → `DIEU` (span: `[14:16]`)
- `[e5]` **Khoản 2** → `KHOAN` (span: `[17:19]`)
- `[e6]` **a ) Quản lý , thanh tra , giám sát , xử lý đối với các hành vi vi phạm của quỹ tín dụng nhân dân trên địa bàn tỉnh , thành phố nơi không có Cục thanh tra , giám sát ngân hàng trong việc thực hiện các quy định tại Thông tư này và các quy định của pháp luật có liên quan ;** → `DIEM` (span: `[20:66]`)
- `[e7]` **Thông tư này** → `THAM_CHIEU_PHAP_LY` (span: `[56:58]`) *(lồng trong `e6` (`DIEM`))*
- `[e8]` **quy định tại** → `TU_KHOA_PHAP_LY` (span: `[54:56]`) *(lồng trong `e6` (`DIEM`))*
- `[e9]` **thanh tra , giám sát ngân hàng** → `CO_QUAN_THAM_QUYEN` (span: `[46:50]`) *(lồng trong `e6` (`DIEM`))*
- `[e10]` **quỹ tín dụng nhân dân** → `TO_CHUC_DOANH_NGHIEP` (span: `[34:37]`) *(lồng trong `e6` (`DIEM`))*
- `[e11]` **trên địa bàn tỉnh** → `DIA_DIEM` (span: `[37:40]`) *(lồng trong `e6` (`DIEM`))*

**Quan hệ:**
- (`e1` 06/2017/TT-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Ngân hàng Nhà nước Việt Nam `[CO_QUAN_BAN_HANH]`)
- (`e1` 06/2017/TT-NHNN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 06/2017/TT-NHNN `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Thanh tra , giám sát ngân hàng `[LINH_VUC]`)
- (`e4` Điều 2 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 06/2017/TT-NHNN `[SO_HIEU]`)
- (`e5` Khoản 2 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 2 `[DIEU]`)
- (`e6` a ) Quản lý , thanh tra , giám sát , xử lý đối với các hành vi vi phạm của quỹ tín dụng nhân dân trên địa bàn tỉnh , thành phố nơi không có Cục thanh tra , giám sát ngân hàng trong việc thực hiện các quy định tại Thông tư này và các quy định của pháp luật có liên quan ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e5` Khoản 2 `[KHOAN]`)
- (`e1` 06/2017/TT-NHNN `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Thanh tra , giám sát ngân hàng `[LINH_VUC]`)
- (`e6` a ) Quản lý , thanh tra , giám sát , xử lý đối với các hành vi vi phạm của quỹ tín dụng nhân dân trên địa bàn tỉnh , thành phố nơi không có Cục thanh tra , giám sát ngân hàng trong việc thực hiện các quy định tại Thông tư này và các quy định của pháp luật có liên quan ; `[DIEM]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Thanh tra , giám sát ngân hàng `[LINH_VUC]`)
- (`e8` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e7` Thông tư này `[THAM_CHIEU_PHAP_LY]`)
- (`e6` a ) Quản lý , thanh tra , giám sát , xử lý đối với các hành vi vi phạm của quỹ tín dụng nhân dân trên địa bàn tỉnh , thành phố nơi không có Cục thanh tra , giám sát ngân hàng trong việc thực hiện các quy định tại Thông tư này và các quy định của pháp luật có liên quan ; `[DIEM]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e7` Thông tư này `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #06_2017_TT-NHNN_122819#body_standalone_72 (Loại: `body_standalone`)
> **[Điều 2]`<DIEU>`** . **[Khoản 2]`<KHOAN>`** . **[a ) Quản lý , thanh tra , giám sát , xử lý đối với các hành vi vi phạm của **[quỹ tín dụng nhân dân]`<TO_CHUC_DOANH_NGHIEP>`** **[trên địa bàn tỉnh]`<DIA_DIEM>`** , thành phố nơi không có Cục **[thanh tra , giám sát ngân hàng]`<CO_QUAN_THAM_QUYEN>`** trong việc thực hiện các **[quy định tại]`<TU_KHOA_PHAP_LY>`** **[Thông tư này]`<THAM_CHIEU_PHAP_LY>`** và các quy định của pháp luật có liên quan ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Điều 2** → `DIEU` (span: `[0:2]`)
- `[e1]` **Khoản 2** → `KHOAN` (span: `[3:5]`)
- `[e2]` **a ) Quản lý , thanh tra , giám sát , xử lý đối với các hành vi vi phạm của quỹ tín dụng nhân dân trên địa bàn tỉnh , thành phố nơi không có Cục thanh tra , giám sát ngân hàng trong việc thực hiện các quy định tại Thông tư này và các quy định của pháp luật có liên quan ;** → `DIEM` (span: `[6:52]`)
- `[e3]` **Thông tư này** → `THAM_CHIEU_PHAP_LY` (span: `[42:44]`) *(lồng trong `e2` (`DIEM`))*
- `[e4]` **quy định tại** → `TU_KHOA_PHAP_LY` (span: `[40:42]`) *(lồng trong `e2` (`DIEM`))*
- `[e5]` **thanh tra , giám sát ngân hàng** → `CO_QUAN_THAM_QUYEN` (span: `[32:36]`) *(lồng trong `e2` (`DIEM`))*
- `[e6]` **quỹ tín dụng nhân dân** → `TO_CHUC_DOANH_NGHIEP` (span: `[20:23]`) *(lồng trong `e2` (`DIEM`))*
- `[e7]` **trên địa bàn tỉnh** → `DIA_DIEM` (span: `[23:26]`) *(lồng trong `e2` (`DIEM`))*

**Quan hệ:**
- (`e1` Khoản 2 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 2 `[DIEU]`)
- (`e2` a ) Quản lý , thanh tra , giám sát , xử lý đối với các hành vi vi phạm của quỹ tín dụng nhân dân trên địa bàn tỉnh , thành phố nơi không có Cục thanh tra , giám sát ngân hàng trong việc thực hiện các quy định tại Thông tư này và các quy định của pháp luật có liên quan ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e1` Khoản 2 `[KHOAN]`)
- (`e4` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Thông tư này `[THAM_CHIEU_PHAP_LY]`)
- (`e2` a ) Quản lý , thanh tra , giám sát , xử lý đối với các hành vi vi phạm của quỹ tín dụng nhân dân trên địa bàn tỉnh , thành phố nơi không có Cục thanh tra , giám sát ngân hàng trong việc thực hiện các quy định tại Thông tư này và các quy định của pháp luật có liên quan ; `[DIEM]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Thông tư này `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #06_2017_TT-NHNN_122819#body_context_73 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[06/2017/TT-NHNN]`<SO_HIEU>`** của **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Thanh tra , giám sát ngân hàng]`<LINH_VUC>`** . **[Điều 2]`<DIEU>`** . **[Khoản 2]`<KHOAN>`** . **[b ) Thẩm định , **[cấp Giấy phép]`<NGHIA_VU_QUYEN>`** , chấp thuận danh sách những người được dự kiến bầu , bổ nhiệm làm Chủ tịch và các thành viên khác của **[Hội đồng quản trị]`<TO_CHUC_DOANH_NGHIEP>`** , Trưởng Ban và các thành viên khác của **[Ban kiểm soát]`<TO_CHUC_DOANH_NGHIEP>`** , **[Giám đốc]`<CHU_THE_CA_NHAN>`** **[quỹ tín dụng nhân dân]`<TO_CHUC_DOANH_NGHIEP>`** ; xác nhận việc đăng ký **[Điều lệ quỹ tín dụng nhân dân]`<GIAY_TO_HO_SO>`** **[theo quy định tại]`<TU_KHOA_PHAP_LY>`** **[Thông tư này]`<THAM_CHIEU_PHAP_LY>`** ; Trong thời hạn **[tối đa 15 ngày]`<THOI_HAN>`** kể từ ngày **[cấp Giấy phép]`<NGHIA_VU_QUYEN>`** báo cáo **[Thống đốc Ngân hàng Nhà nước]`<CO_QUAN_THAM_QUYEN>`**]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **06/2017/TT-NHNN** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_BAN_HANH` (span: `[4:7]`)
- `[e3]` **Thanh tra , giám sát ngân hàng** → `LINH_VUC` (span: `[9:13]`)
- `[e4]` **Điều 2** → `DIEU` (span: `[14:16]`)
- `[e5]` **Khoản 2** → `KHOAN` (span: `[17:19]`)
- `[e6]` **b ) Thẩm định , cấp Giấy phép , chấp thuận danh sách những người được dự kiến bầu , bổ nhiệm làm Chủ tịch và các thành viên khác của Hội đồng quản trị , Trưởng Ban và các thành viên khác của Ban kiểm soát , Giám đốc quỹ tín dụng nhân dân ; xác nhận việc đăng ký Điều lệ quỹ tín dụng nhân dân theo quy định tại Thông tư này ; Trong thời hạn tối đa 15 ngày kể từ ngày cấp Giấy phép báo cáo Thống đốc Ngân hàng Nhà nước** → `DIEM` (span: `[20:88]`)
- `[e7]` **cấp Giấy phép** → `NGHIA_VU_QUYEN` (span: `[24:26]`) *(lồng trong `e6` (`DIEM`))*
- `[e8]` **cấp Giấy phép** → `NGHIA_VU_QUYEN` (span: `[82:84]`) *(lồng trong `e6` (`DIEM`))*
- `[e9]` **Thông tư này** → `THAM_CHIEU_PHAP_LY` (span: `[71:73]`) *(lồng trong `e6` (`DIEM`))*
- `[e10]` **theo quy định tại** → `TU_KHOA_PHAP_LY` (span: `[68:71]`) *(lồng trong `e6` (`DIEM`))*
- `[e11]` **tối đa 15 ngày** → `THOI_HAN` (span: `[76:79]`) *(lồng trong `e6` (`DIEM`))*
- `[e12]` **Thống đốc Ngân hàng Nhà nước** → `CO_QUAN_THAM_QUYEN` (span: `[85:88]`) *(lồng trong `e6` (`DIEM`))*
- `[e13]` **Điều lệ quỹ tín dụng nhân dân** → `GIAY_TO_HO_SO` (span: `[64:68]`) *(lồng trong `e6` (`DIEM`))*
- `[e14]` **Hội đồng quản trị** → `TO_CHUC_DOANH_NGHIEP` (span: `[43:45]`) *(lồng trong `e6` (`DIEM`))*
- `[e15]` **Ban kiểm soát** → `TO_CHUC_DOANH_NGHIEP` (span: `[53:55]`) *(lồng trong `e6` (`DIEM`))*
- `[e16]` **quỹ tín dụng nhân dân** → `TO_CHUC_DOANH_NGHIEP` (span: `[57:60]`) *(lồng trong `e6` (`DIEM`))*
- `[e17]` **Giám đốc** → `CHU_THE_CA_NHAN` (span: `[56:57]`) *(lồng trong `e6` (`DIEM`))*

**Quan hệ:**
- (`e1` 06/2017/TT-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Ngân hàng Nhà nước Việt Nam `[CO_QUAN_BAN_HANH]`)
- (`e1` 06/2017/TT-NHNN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 06/2017/TT-NHNN `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Thanh tra , giám sát ngân hàng `[LINH_VUC]`)
- (`e4` Điều 2 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 06/2017/TT-NHNN `[SO_HIEU]`)
- (`e5` Khoản 2 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 2 `[DIEU]`)
- (`e6` b ) Thẩm định , cấp Giấy phép , chấp thuận danh sách những người được dự kiến bầu , bổ nhiệm làm Chủ tịch và các thành viên khác của Hội đồng quản trị , Trưởng Ban và các thành viên khác của Ban kiểm soát , Giám đốc quỹ tín dụng nhân dân ; xác nhận việc đăng ký Điều lệ quỹ tín dụng nhân dân theo quy định tại Thông tư này ; Trong thời hạn tối đa 15 ngày kể từ ngày cấp Giấy phép báo cáo Thống đốc Ngân hàng Nhà nước `[DIEM]`) ==[ **THUOC_VE** ]==> (`e5` Khoản 2 `[KHOAN]`)
- (`e7` cấp Giấy phép `[NGHIA_VU_QUYEN]`) ==[ **TAC_DONG_CHU_THE** ]==> (`e12` Thống đốc Ngân hàng Nhà nước `[CO_QUAN_THAM_QUYEN]`)
- (`e8` cấp Giấy phép `[NGHIA_VU_QUYEN]`) ==[ **TAC_DONG_CHU_THE** ]==> (`e12` Thống đốc Ngân hàng Nhà nước `[CO_QUAN_THAM_QUYEN]`)
- (`e7` cấp Giấy phép `[NGHIA_VU_QUYEN]`) ==[ **TAC_DONG_CHU_THE** ]==> (`e14` Hội đồng quản trị `[TO_CHUC_DOANH_NGHIEP]`)
- (`e7` cấp Giấy phép `[NGHIA_VU_QUYEN]`) ==[ **TAC_DONG_CHU_THE** ]==> (`e15` Ban kiểm soát `[TO_CHUC_DOANH_NGHIEP]`)
- (`e16` quỹ tín dụng nhân dân `[TO_CHUC_DOANH_NGHIEP]`) ==[ **CO_NGHIA_VU_QUYEN** ]==> (`e8` cấp Giấy phép `[NGHIA_VU_QUYEN]`)
- (`e17` Giám đốc `[CHU_THE_CA_NHAN]`) ==[ **CO_NGHIA_VU_QUYEN** ]==> (`e8` cấp Giấy phép `[NGHIA_VU_QUYEN]`)
- (`e1` 06/2017/TT-NHNN `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Thanh tra , giám sát ngân hàng `[LINH_VUC]`)
- (`e7` cấp Giấy phép `[NGHIA_VU_QUYEN]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Thanh tra , giám sát ngân hàng `[LINH_VUC]`)
- (`e10` theo quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e9` Thông tư này `[THAM_CHIEU_PHAP_LY]`)
- (`e8` cấp Giấy phép `[NGHIA_VU_QUYEN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e9` Thông tư này `[THAM_CHIEU_PHAP_LY]`)
- (`e8` cấp Giấy phép `[NGHIA_VU_QUYEN]`) ==[ **TRONG_THOI_HAN** ]==> (`e11` tối đa 15 ngày `[THOI_HAN]`)
- (`e8` cấp Giấy phép `[NGHIA_VU_QUYEN]`) ==[ **TAC_DONG_DOI_TUONG** ]==> (`e13` Điều lệ quỹ tín dụng nhân dân `[GIAY_TO_HO_SO]`)


---

### Mẫu #06_2017_TT-NHNN_122819#body_standalone_74 (Loại: `body_standalone`)
> **[Điều 2]`<DIEU>`** . **[Khoản 2]`<KHOAN>`** . **[b ) Thẩm định , **[cấp Giấy phép]`<NGHIA_VU_QUYEN>`** , chấp thuận danh sách những người được dự kiến bầu , bổ nhiệm làm Chủ tịch và các thành viên khác của **[Hội đồng quản trị]`<TO_CHUC_DOANH_NGHIEP>`** , Trưởng Ban và các thành viên khác của **[Ban kiểm soát]`<TO_CHUC_DOANH_NGHIEP>`** , **[Giám đốc]`<CHU_THE_CA_NHAN>`** **[quỹ tín dụng nhân dân]`<TO_CHUC_DOANH_NGHIEP>`** ; xác nhận việc đăng ký **[Điều lệ quỹ tín dụng nhân dân]`<GIAY_TO_HO_SO>`** **[theo quy định tại]`<TU_KHOA_PHAP_LY>`** **[Thông tư này]`<THAM_CHIEU_PHAP_LY>`** ; Trong thời hạn **[tối đa 15 ngày]`<THOI_HAN>`** kể từ ngày **[cấp Giấy phép]`<NGHIA_VU_QUYEN>`** báo cáo **[Thống đốc Ngân hàng Nhà nước]`<CO_QUAN_THAM_QUYEN>`**]`<DIEM>`**

**Thực thể:**
- `[e0]` **Điều 2** → `DIEU` (span: `[0:2]`)
- `[e1]` **Khoản 2** → `KHOAN` (span: `[3:5]`)
- `[e2]` **b ) Thẩm định , cấp Giấy phép , chấp thuận danh sách những người được dự kiến bầu , bổ nhiệm làm Chủ tịch và các thành viên khác của Hội đồng quản trị , Trưởng Ban và các thành viên khác của Ban kiểm soát , Giám đốc quỹ tín dụng nhân dân ; xác nhận việc đăng ký Điều lệ quỹ tín dụng nhân dân theo quy định tại Thông tư này ; Trong thời hạn tối đa 15 ngày kể từ ngày cấp Giấy phép báo cáo Thống đốc Ngân hàng Nhà nước** → `DIEM` (span: `[6:74]`)
- `[e3]` **cấp Giấy phép** → `NGHIA_VU_QUYEN` (span: `[10:12]`) *(lồng trong `e2` (`DIEM`))*
- `[e4]` **cấp Giấy phép** → `NGHIA_VU_QUYEN` (span: `[68:70]`) *(lồng trong `e2` (`DIEM`))*
- `[e5]` **Thông tư này** → `THAM_CHIEU_PHAP_LY` (span: `[57:59]`) *(lồng trong `e2` (`DIEM`))*
- `[e6]` **theo quy định tại** → `TU_KHOA_PHAP_LY` (span: `[54:57]`) *(lồng trong `e2` (`DIEM`))*
- `[e7]` **tối đa 15 ngày** → `THOI_HAN` (span: `[62:65]`) *(lồng trong `e2` (`DIEM`))*
- `[e8]` **Thống đốc Ngân hàng Nhà nước** → `CO_QUAN_THAM_QUYEN` (span: `[71:74]`) *(lồng trong `e2` (`DIEM`))*
- `[e9]` **Điều lệ quỹ tín dụng nhân dân** → `GIAY_TO_HO_SO` (span: `[50:54]`) *(lồng trong `e2` (`DIEM`))*
- `[e10]` **Hội đồng quản trị** → `TO_CHUC_DOANH_NGHIEP` (span: `[29:31]`) *(lồng trong `e2` (`DIEM`))*
- `[e11]` **Ban kiểm soát** → `TO_CHUC_DOANH_NGHIEP` (span: `[39:41]`) *(lồng trong `e2` (`DIEM`))*
- `[e12]` **quỹ tín dụng nhân dân** → `TO_CHUC_DOANH_NGHIEP` (span: `[43:46]`) *(lồng trong `e2` (`DIEM`))*
- `[e13]` **Giám đốc** → `CHU_THE_CA_NHAN` (span: `[42:43]`) *(lồng trong `e2` (`DIEM`))*

**Quan hệ:**
- (`e1` Khoản 2 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 2 `[DIEU]`)
- (`e2` b ) Thẩm định , cấp Giấy phép , chấp thuận danh sách những người được dự kiến bầu , bổ nhiệm làm Chủ tịch và các thành viên khác của Hội đồng quản trị , Trưởng Ban và các thành viên khác của Ban kiểm soát , Giám đốc quỹ tín dụng nhân dân ; xác nhận việc đăng ký Điều lệ quỹ tín dụng nhân dân theo quy định tại Thông tư này ; Trong thời hạn tối đa 15 ngày kể từ ngày cấp Giấy phép báo cáo Thống đốc Ngân hàng Nhà nước `[DIEM]`) ==[ **THUOC_VE** ]==> (`e1` Khoản 2 `[KHOAN]`)
- (`e3` cấp Giấy phép `[NGHIA_VU_QUYEN]`) ==[ **TAC_DONG_CHU_THE** ]==> (`e8` Thống đốc Ngân hàng Nhà nước `[CO_QUAN_THAM_QUYEN]`)
- (`e4` cấp Giấy phép `[NGHIA_VU_QUYEN]`) ==[ **TAC_DONG_CHU_THE** ]==> (`e8` Thống đốc Ngân hàng Nhà nước `[CO_QUAN_THAM_QUYEN]`)
- (`e3` cấp Giấy phép `[NGHIA_VU_QUYEN]`) ==[ **TAC_DONG_CHU_THE** ]==> (`e10` Hội đồng quản trị `[TO_CHUC_DOANH_NGHIEP]`)
- (`e3` cấp Giấy phép `[NGHIA_VU_QUYEN]`) ==[ **TAC_DONG_CHU_THE** ]==> (`e11` Ban kiểm soát `[TO_CHUC_DOANH_NGHIEP]`)
- (`e12` quỹ tín dụng nhân dân `[TO_CHUC_DOANH_NGHIEP]`) ==[ **CO_NGHIA_VU_QUYEN** ]==> (`e4` cấp Giấy phép `[NGHIA_VU_QUYEN]`)
- (`e13` Giám đốc `[CHU_THE_CA_NHAN]`) ==[ **CO_NGHIA_VU_QUYEN** ]==> (`e4` cấp Giấy phép `[NGHIA_VU_QUYEN]`)
- (`e6` theo quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e5` Thông tư này `[THAM_CHIEU_PHAP_LY]`)
- (`e4` cấp Giấy phép `[NGHIA_VU_QUYEN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e5` Thông tư này `[THAM_CHIEU_PHAP_LY]`)
- (`e4` cấp Giấy phép `[NGHIA_VU_QUYEN]`) ==[ **TRONG_THOI_HAN** ]==> (`e7` tối đa 15 ngày `[THOI_HAN]`)
- (`e4` cấp Giấy phép `[NGHIA_VU_QUYEN]`) ==[ **TAC_DONG_DOI_TUONG** ]==> (`e9` Điều lệ quỹ tín dụng nhân dân `[GIAY_TO_HO_SO]`)


---

### Mẫu #06_2017_TT-NHNN_122819#body_context_75 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[06/2017/TT-NHNN]`<SO_HIEU>`** ban hành **[ngày 05 tháng 07 năm 2017]`<NGAY_BAN_HANH>`** bởi **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_BAN_HANH>`** . **[Điều 2]`<DIEU>`** . **[Khoản 2]`<KHOAN>`** . **[c ) Có văn bản lấy ý kiến : ( i ) Ủy ban nhân dân xã về việc thành lập **[quỹ tín dụng nhân dân]`<TO_CHUC_DOANH_NGHIEP>`** trên địa bàn , danh sách nhân sự dự kiến bầu , bổ nhiệm làm Chủ tịch và các thành viên khác của **[Hội đồng quản trị]`<TO_CHUC_DOANH_NGHIEP>`** , Trưởng ban và các thành viên khác của **[Ban kiểm soát]`<TO_CHUC_DOANH_NGHIEP>`** , **[Giám đốc]`<CHU_THE_CA_NHAN>`** **[quỹ tín dụng nhân dân]`<TO_CHUC_DOANH_NGHIEP>`** ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **06/2017/TT-NHNN** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_BAN_HANH` (span: `[11:14]`)
- `[e3]` **ngày 05 tháng 07 năm 2017** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 2** → `DIEU` (span: `[15:17]`)
- `[e5]` **Khoản 2** → `KHOAN` (span: `[18:20]`)
- `[e6]` **c ) Có văn bản lấy ý kiến : ( i ) Ủy ban nhân dân xã về việc thành lập quỹ tín dụng nhân dân trên địa bàn , danh sách nhân sự dự kiến bầu , bổ nhiệm làm Chủ tịch và các thành viên khác của Hội đồng quản trị , Trưởng ban và các thành viên khác của Ban kiểm soát , Giám đốc quỹ tín dụng nhân dân ;** → `DIEM` (span: `[21:74]`)
- `[e7]` **quỹ tín dụng nhân dân** → `TO_CHUC_DOANH_NGHIEP` (span: `[37:40]`) *(lồng trong `e6` (`DIEM`))*
- `[e8]` **Hội đồng quản trị** → `TO_CHUC_DOANH_NGHIEP` (span: `[56:58]`) *(lồng trong `e6` (`DIEM`))*
- `[e9]` **Ban kiểm soát** → `TO_CHUC_DOANH_NGHIEP` (span: `[66:68]`) *(lồng trong `e6` (`DIEM`))*
- `[e10]` **quỹ tín dụng nhân dân** → `TO_CHUC_DOANH_NGHIEP` (span: `[70:73]`) *(lồng trong `e6` (`DIEM`))*
- `[e11]` **Giám đốc** → `CHU_THE_CA_NHAN` (span: `[69:70]`) *(lồng trong `e6` (`DIEM`))*

**Quan hệ:**
- (`e1` 06/2017/TT-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Ngân hàng Nhà nước Việt Nam `[CO_QUAN_BAN_HANH]`)
- (`e1` 06/2017/TT-NHNN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 06/2017/TT-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 05 tháng 07 năm 2017 `[NGAY_BAN_HANH]`)
- (`e4` Điều 2 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 06/2017/TT-NHNN `[SO_HIEU]`)
- (`e5` Khoản 2 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 2 `[DIEU]`)
- (`e6` c ) Có văn bản lấy ý kiến : ( i ) Ủy ban nhân dân xã về việc thành lập quỹ tín dụng nhân dân trên địa bàn , danh sách nhân sự dự kiến bầu , bổ nhiệm làm Chủ tịch và các thành viên khác của Hội đồng quản trị , Trưởng ban và các thành viên khác của Ban kiểm soát , Giám đốc quỹ tín dụng nhân dân ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e5` Khoản 2 `[KHOAN]`)


---

### Mẫu #06_2017_TT-NHNN_122819#body_standalone_76 (Loại: `body_standalone`)
> **[Điều 2]`<DIEU>`** . **[Khoản 2]`<KHOAN>`** . **[c ) Có văn bản lấy ý kiến : ( i ) Ủy ban nhân dân xã về việc thành lập **[quỹ tín dụng nhân dân]`<TO_CHUC_DOANH_NGHIEP>`** trên địa bàn , danh sách nhân sự dự kiến bầu , bổ nhiệm làm Chủ tịch và các thành viên khác của **[Hội đồng quản trị]`<TO_CHUC_DOANH_NGHIEP>`** , Trưởng ban và các thành viên khác của **[Ban kiểm soát]`<TO_CHUC_DOANH_NGHIEP>`** , **[Giám đốc]`<CHU_THE_CA_NHAN>`** **[quỹ tín dụng nhân dân]`<TO_CHUC_DOANH_NGHIEP>`** ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Điều 2** → `DIEU` (span: `[0:2]`)
- `[e1]` **Khoản 2** → `KHOAN` (span: `[3:5]`)
- `[e2]` **c ) Có văn bản lấy ý kiến : ( i ) Ủy ban nhân dân xã về việc thành lập quỹ tín dụng nhân dân trên địa bàn , danh sách nhân sự dự kiến bầu , bổ nhiệm làm Chủ tịch và các thành viên khác của Hội đồng quản trị , Trưởng ban và các thành viên khác của Ban kiểm soát , Giám đốc quỹ tín dụng nhân dân ;** → `DIEM` (span: `[6:59]`)
- `[e3]` **quỹ tín dụng nhân dân** → `TO_CHUC_DOANH_NGHIEP` (span: `[22:25]`) *(lồng trong `e2` (`DIEM`))*
- `[e4]` **Hội đồng quản trị** → `TO_CHUC_DOANH_NGHIEP` (span: `[41:43]`) *(lồng trong `e2` (`DIEM`))*
- `[e5]` **Ban kiểm soát** → `TO_CHUC_DOANH_NGHIEP` (span: `[51:53]`) *(lồng trong `e2` (`DIEM`))*
- `[e6]` **quỹ tín dụng nhân dân** → `TO_CHUC_DOANH_NGHIEP` (span: `[55:58]`) *(lồng trong `e2` (`DIEM`))*
- `[e7]` **Giám đốc** → `CHU_THE_CA_NHAN` (span: `[54:55]`) *(lồng trong `e2` (`DIEM`))*

**Quan hệ:**
- (`e1` Khoản 2 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 2 `[DIEU]`)
- (`e2` c ) Có văn bản lấy ý kiến : ( i ) Ủy ban nhân dân xã về việc thành lập quỹ tín dụng nhân dân trên địa bàn , danh sách nhân sự dự kiến bầu , bổ nhiệm làm Chủ tịch và các thành viên khác của Hội đồng quản trị , Trưởng ban và các thành viên khác của Ban kiểm soát , Giám đốc quỹ tín dụng nhân dân ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e1` Khoản 2 `[KHOAN]`)


---

### Mẫu #06_2017_TT-NHNN_122819#body_context_77 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[06/2017/TT-NHNN]`<SO_HIEU>`** ban hành **[ngày 05 tháng 07 năm 2017]`<NGAY_BAN_HANH>`** bởi **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_BAN_HANH>`** . **[Điều 2]`<DIEU>`** . **[Khoản 2]`<KHOAN>`** . **[( iii ) Cục **[Thanh tra , giám sát ngân hàng]`<CO_QUAN_THAM_QUYEN>`** **[quy định tại]`<TU_KHOA_PHAP_LY>`** **[điểm c ( iii ) khoản 1 Điều 12 Thông tư này]`<THAM_CHIEU_PHAP_LY>`** ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **06/2017/TT-NHNN** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_BAN_HANH` (span: `[11:14]`)
- `[e3]` **ngày 05 tháng 07 năm 2017** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 2** → `DIEU` (span: `[15:17]`)
- `[e5]` **Khoản 2** → `KHOAN` (span: `[18:20]`)
- `[e6]` **( iii ) Cục Thanh tra , giám sát ngân hàng quy định tại điểm c ( iii ) khoản 1 Điều 12 Thông tư này ;** → `DIEM` (span: `[21:43]`)
- `[e7]` **điểm c ( iii ) khoản 1 Điều 12 Thông tư này** → `THAM_CHIEU_PHAP_LY` (span: `[31:42]`) *(lồng trong `e6` (`DIEM`))*
- `[e8]` **quy định tại** → `TU_KHOA_PHAP_LY` (span: `[29:31]`) *(lồng trong `e6` (`DIEM`))*
- `[e9]` **Thanh tra , giám sát ngân hàng** → `CO_QUAN_THAM_QUYEN` (span: `[25:29]`) *(lồng trong `e6` (`DIEM`))*

**Quan hệ:**
- (`e1` 06/2017/TT-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Ngân hàng Nhà nước Việt Nam `[CO_QUAN_BAN_HANH]`)
- (`e1` 06/2017/TT-NHNN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 06/2017/TT-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 05 tháng 07 năm 2017 `[NGAY_BAN_HANH]`)
- (`e4` Điều 2 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 06/2017/TT-NHNN `[SO_HIEU]`)
- (`e5` Khoản 2 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 2 `[DIEU]`)
- (`e6` ( iii ) Cục Thanh tra , giám sát ngân hàng quy định tại điểm c ( iii ) khoản 1 Điều 12 Thông tư này ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e5` Khoản 2 `[KHOAN]`)
- (`e8` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e7` điểm c ( iii ) khoản 1 Điều 12 Thông tư này `[THAM_CHIEU_PHAP_LY]`)
- (`e6` ( iii ) Cục Thanh tra , giám sát ngân hàng quy định tại điểm c ( iii ) khoản 1 Điều 12 Thông tư này ; `[DIEM]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e7` điểm c ( iii ) khoản 1 Điều 12 Thông tư này `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #06_2017_TT-NHNN_122819#body_standalone_78 (Loại: `body_standalone`)
> **[Điều 2]`<DIEU>`** . **[Khoản 2]`<KHOAN>`** . **[( iii ) Cục **[Thanh tra , giám sát ngân hàng]`<CO_QUAN_THAM_QUYEN>`** **[quy định tại]`<TU_KHOA_PHAP_LY>`** **[điểm c ( iii ) khoản 1 Điều 12 Thông tư này]`<THAM_CHIEU_PHAP_LY>`** ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Điều 2** → `DIEU` (span: `[0:2]`)
- `[e1]` **Khoản 2** → `KHOAN` (span: `[3:5]`)
- `[e2]` **( iii ) Cục Thanh tra , giám sát ngân hàng quy định tại điểm c ( iii ) khoản 1 Điều 12 Thông tư này ;** → `DIEM` (span: `[6:28]`)
- `[e3]` **điểm c ( iii ) khoản 1 Điều 12 Thông tư này** → `THAM_CHIEU_PHAP_LY` (span: `[16:27]`) *(lồng trong `e2` (`DIEM`))*
- `[e4]` **quy định tại** → `TU_KHOA_PHAP_LY` (span: `[14:16]`) *(lồng trong `e2` (`DIEM`))*
- `[e5]` **Thanh tra , giám sát ngân hàng** → `CO_QUAN_THAM_QUYEN` (span: `[10:14]`) *(lồng trong `e2` (`DIEM`))*

**Quan hệ:**
- (`e1` Khoản 2 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 2 `[DIEU]`)
- (`e2` ( iii ) Cục Thanh tra , giám sát ngân hàng quy định tại điểm c ( iii ) khoản 1 Điều 12 Thông tư này ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e1` Khoản 2 `[KHOAN]`)
- (`e4` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` điểm c ( iii ) khoản 1 Điều 12 Thông tư này `[THAM_CHIEU_PHAP_LY]`)
- (`e2` ( iii ) Cục Thanh tra , giám sát ngân hàng quy định tại điểm c ( iii ) khoản 1 Điều 12 Thông tư này ; `[DIEM]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` điểm c ( iii ) khoản 1 Điều 12 Thông tư này `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #06_2017_TT-NHNN_122819#body_context_79 (Loại: `body_context`)
> **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[06/2017/TT-NHNN]`<SO_HIEU>`** . **[Điều 2]`<DIEU>`** . **[Khoản 2]`<KHOAN>`** . **[d ) Chỉ đạo , hướng dẫn , giám sát , kiểm tra **[quỹ tín dụng nhân dân]`<TO_CHUC_DOANH_NGHIEP>`** trong việc thực hiện quy định về chuyển tiếp và xử lý sau chuyển tiếp tại **[các Điều 46 , 47 , 47a và Điều 51 Thông tư này]`<THAM_CHIEU_PHAP_LY>`** . Định kỳ hàng quý , **[trong thời gian 15 ngày]`<THOI_HAN>`** đầu tiên của tháng đầu tiên của quý , có văn bản báo cáo **[Ngân hàng Nhà nước]`<CO_QUAN_THAM_QUYEN>`** ( Cơ quan **[Thanh tra , giám sát ngân hàng]`<CO_QUAN_THAM_QUYEN>`** ) về tình hình thực hiện quy định chuyển tiếp của quỹ tín dụng nhân]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[4:5]`)
- `[e1]` **06/2017/TT-NHNN** → `SO_HIEU` (span: `[6:7]`)
- `[e2]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_BAN_HANH` (span: `[0:3]`)
- `[e3]` **Điều 2** → `DIEU` (span: `[8:10]`)
- `[e4]` **Khoản 2** → `KHOAN` (span: `[11:13]`)
- `[e5]` **d ) Chỉ đạo , hướng dẫn , giám sát , kiểm tra quỹ tín dụng nhân dân trong việc thực hiện quy định về chuyển tiếp và xử lý sau chuyển tiếp tại các Điều 46 , 47 , 47a và Điều 51 Thông tư này . Định kỳ hàng quý , trong thời gian 15 ngày đầu tiên của tháng đầu tiên của quý , có văn bản báo cáo Ngân hàng Nhà nước ( Cơ quan Thanh tra , giám sát ngân hàng ) về tình hình thực hiện quy định chuyển tiếp của quỹ tín dụng nhân** → `DIEM` (span: `[14:86]`)
- `[e6]` **các Điều 46 , 47 , 47a và Điều 51 Thông tư này** → `THAM_CHIEU_PHAP_LY` (span: `[37:49]`) *(lồng trong `e5` (`DIEM`))*
- `[e7]` **trong thời gian 15 ngày** → `THOI_HAN` (span: `[54:58]`) *(lồng trong `e5` (`DIEM`))*
- `[e8]` **Ngân hàng Nhà nước** → `CO_QUAN_THAM_QUYEN` (span: `[68:70]`) *(lồng trong `e5` (`DIEM`))*
- `[e9]` **Thanh tra , giám sát ngân hàng** → `CO_QUAN_THAM_QUYEN` (span: `[72:76]`) *(lồng trong `e5` (`DIEM`))*
- `[e10]` **quỹ tín dụng nhân dân** → `TO_CHUC_DOANH_NGHIEP` (span: `[23:26]`) *(lồng trong `e5` (`DIEM`))*

**Quan hệ:**
- (`e1` 06/2017/TT-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Ngân hàng Nhà nước Việt Nam `[CO_QUAN_BAN_HANH]`)
- (`e1` 06/2017/TT-NHNN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 2 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 06/2017/TT-NHNN `[SO_HIEU]`)
- (`e4` Khoản 2 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 2 `[DIEU]`)
- (`e5` d ) Chỉ đạo , hướng dẫn , giám sát , kiểm tra quỹ tín dụng nhân dân trong việc thực hiện quy định về chuyển tiếp và xử lý sau chuyển tiếp tại các Điều 46 , 47 , 47a và Điều 51 Thông tư này . Định kỳ hàng quý , trong thời gian 15 ngày đầu tiên của tháng đầu tiên của quý , có văn bản báo cáo Ngân hàng Nhà nước ( Cơ quan Thanh tra , giám sát ngân hàng ) về tình hình thực hiện quy định chuyển tiếp của quỹ tín dụng nhân `[DIEM]`) ==[ **THUOC_VE** ]==> (`e4` Khoản 2 `[KHOAN]`)
- (`e5` d ) Chỉ đạo , hướng dẫn , giám sát , kiểm tra quỹ tín dụng nhân dân trong việc thực hiện quy định về chuyển tiếp và xử lý sau chuyển tiếp tại các Điều 46 , 47 , 47a và Điều 51 Thông tư này . Định kỳ hàng quý , trong thời gian 15 ngày đầu tiên của tháng đầu tiên của quý , có văn bản báo cáo Ngân hàng Nhà nước ( Cơ quan Thanh tra , giám sát ngân hàng ) về tình hình thực hiện quy định chuyển tiếp của quỹ tín dụng nhân `[DIEM]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e6` các Điều 46 , 47 , 47a và Điều 51 Thông tư này `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #06_2017_TT-NHNN_122819#body_standalone_80 (Loại: `body_standalone`)
> **[Điều 2]`<DIEU>`** . **[Khoản 2]`<KHOAN>`** . **[d ) Chỉ đạo , hướng dẫn , giám sát , kiểm tra **[quỹ tín dụng nhân dân]`<TO_CHUC_DOANH_NGHIEP>`** trong việc thực hiện quy định về chuyển tiếp và xử lý sau chuyển tiếp tại **[các Điều 46 , 47 , 47a và Điều 51 Thông tư này]`<THAM_CHIEU_PHAP_LY>`** . Định kỳ hàng quý , **[trong thời gian 15 ngày]`<THOI_HAN>`** đầu tiên của tháng đầu tiên của quý , có văn bản báo cáo **[Ngân hàng Nhà nước]`<CO_QUAN_THAM_QUYEN>`** ( Cơ quan **[Thanh tra , giám sát ngân hàng]`<CO_QUAN_THAM_QUYEN>`** ) về tình hình thực hiện quy định chuyển tiếp của quỹ tín dụng nhân]`<DIEM>`**

**Thực thể:**
- `[e0]` **Điều 2** → `DIEU` (span: `[0:2]`)
- `[e1]` **Khoản 2** → `KHOAN` (span: `[3:5]`)
- `[e2]` **d ) Chỉ đạo , hướng dẫn , giám sát , kiểm tra quỹ tín dụng nhân dân trong việc thực hiện quy định về chuyển tiếp và xử lý sau chuyển tiếp tại các Điều 46 , 47 , 47a và Điều 51 Thông tư này . Định kỳ hàng quý , trong thời gian 15 ngày đầu tiên của tháng đầu tiên của quý , có văn bản báo cáo Ngân hàng Nhà nước ( Cơ quan Thanh tra , giám sát ngân hàng ) về tình hình thực hiện quy định chuyển tiếp của quỹ tín dụng nhân** → `DIEM` (span: `[6:78]`)
- `[e3]` **các Điều 46 , 47 , 47a và Điều 51 Thông tư này** → `THAM_CHIEU_PHAP_LY` (span: `[29:41]`) *(lồng trong `e2` (`DIEM`))*
- `[e4]` **trong thời gian 15 ngày** → `THOI_HAN` (span: `[46:50]`) *(lồng trong `e2` (`DIEM`))*
- `[e5]` **Ngân hàng Nhà nước** → `CO_QUAN_THAM_QUYEN` (span: `[60:62]`) *(lồng trong `e2` (`DIEM`))*
- `[e6]` **Thanh tra , giám sát ngân hàng** → `CO_QUAN_THAM_QUYEN` (span: `[64:68]`) *(lồng trong `e2` (`DIEM`))*
- `[e7]` **quỹ tín dụng nhân dân** → `TO_CHUC_DOANH_NGHIEP` (span: `[15:18]`) *(lồng trong `e2` (`DIEM`))*

**Quan hệ:**
- (`e1` Khoản 2 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 2 `[DIEU]`)
- (`e2` d ) Chỉ đạo , hướng dẫn , giám sát , kiểm tra quỹ tín dụng nhân dân trong việc thực hiện quy định về chuyển tiếp và xử lý sau chuyển tiếp tại các Điều 46 , 47 , 47a và Điều 51 Thông tư này . Định kỳ hàng quý , trong thời gian 15 ngày đầu tiên của tháng đầu tiên của quý , có văn bản báo cáo Ngân hàng Nhà nước ( Cơ quan Thanh tra , giám sát ngân hàng ) về tình hình thực hiện quy định chuyển tiếp của quỹ tín dụng nhân `[DIEM]`) ==[ **THUOC_VE** ]==> (`e1` Khoản 2 `[KHOAN]`)
- (`e2` d ) Chỉ đạo , hướng dẫn , giám sát , kiểm tra quỹ tín dụng nhân dân trong việc thực hiện quy định về chuyển tiếp và xử lý sau chuyển tiếp tại các Điều 46 , 47 , 47a và Điều 51 Thông tư này . Định kỳ hàng quý , trong thời gian 15 ngày đầu tiên của tháng đầu tiên của quý , có văn bản báo cáo Ngân hàng Nhà nước ( Cơ quan Thanh tra , giám sát ngân hàng ) về tình hình thực hiện quy định chuyển tiếp của quỹ tín dụng nhân `[DIEM]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` các Điều 46 , 47 , 47a và Điều 51 Thông tư này `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #06_2017_TT-NHNN_122819#body_context_81 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[06/2017/TT-NHNN]`<SO_HIEU>`** của **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Thanh tra , giám sát ngân hàng]`<LINH_VUC>`** . **[Điều 2]`<DIEU>`** . **[3 . **[Ngân hàng Hợp tác xã Việt Nam]`<TO_CHUC_DOANH_NGHIEP>`** :]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **06/2017/TT-NHNN** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_BAN_HANH` (span: `[4:7]`)
- `[e3]` **Thanh tra , giám sát ngân hàng** → `LINH_VUC` (span: `[9:13]`)
- `[e4]` **Điều 2** → `DIEU` (span: `[14:16]`)
- `[e5]` **3 . Ngân hàng Hợp tác xã Việt Nam :** → `KHOAN` (span: `[17:23]`)
- `[e6]` **Ngân hàng Hợp tác xã Việt Nam** → `TO_CHUC_DOANH_NGHIEP` (span: `[19:22]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 06/2017/TT-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Ngân hàng Nhà nước Việt Nam `[CO_QUAN_BAN_HANH]`)
- (`e1` 06/2017/TT-NHNN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 06/2017/TT-NHNN `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Thanh tra , giám sát ngân hàng `[LINH_VUC]`)
- (`e4` Điều 2 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 06/2017/TT-NHNN `[SO_HIEU]`)
- (`e5` 3 . Ngân hàng Hợp tác xã Việt Nam : `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 2 `[DIEU]`)
- (`e1` 06/2017/TT-NHNN `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Thanh tra , giám sát ngân hàng `[LINH_VUC]`)
- (`e5` 3 . Ngân hàng Hợp tác xã Việt Nam : `[KHOAN]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Thanh tra , giám sát ngân hàng `[LINH_VUC]`)


---

### Mẫu #06_2017_TT-NHNN_122819#body_standalone_82 (Loại: `body_standalone`)
> **[Điều 2]`<DIEU>`** . **[3 . **[Ngân hàng Hợp tác xã Việt Nam]`<TO_CHUC_DOANH_NGHIEP>`** :]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 2** → `DIEU` (span: `[0:2]`)
- `[e1]` **3 . Ngân hàng Hợp tác xã Việt Nam :** → `KHOAN` (span: `[3:9]`)
- `[e2]` **Ngân hàng Hợp tác xã Việt Nam** → `TO_CHUC_DOANH_NGHIEP` (span: `[5:8]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 3 . Ngân hàng Hợp tác xã Việt Nam : `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 2 `[DIEU]`)


---

### Mẫu #06_2017_TT-NHNN_122819#body_context_83 (Loại: `body_context`)
> **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[06/2017/TT-NHNN]`<SO_HIEU>`** . **[Điều 2]`<DIEU>`** . **[Khoản 3]`<KHOAN>`** . **[a ) **[Hướng dẫn thống nhất trong hệ thống **[quỹ tín dụng nhân dân]`<TO_CHUC_DOANH_NGHIEP>`**]`<NGHIA_VU_QUYEN>`** việc thiết kế , in ấn **[Thẻ thành viên]`<GIAY_TO_HO_SO>`** **[theo quy định tại]`<TU_KHOA_PHAP_LY>`** **[khoản 5 Điều 28 Thông tư này]`<THAM_CHIEU_PHAP_LY>`** ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[4:5]`)
- `[e1]` **06/2017/TT-NHNN** → `SO_HIEU` (span: `[6:7]`)
- `[e2]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_BAN_HANH` (span: `[0:3]`)
- `[e3]` **Điều 2** → `DIEU` (span: `[8:10]`)
- `[e4]` **Khoản 3** → `KHOAN` (span: `[11:13]`)
- `[e5]` **a ) Hướng dẫn thống nhất trong hệ thống quỹ tín dụng nhân dân việc thiết kế , in ấn Thẻ thành viên theo quy định tại khoản 5 Điều 28 Thông tư này ;** → `DIEM` (span: `[14:39]`)
- `[e6]` **Hướng dẫn thống nhất trong hệ thống quỹ tín dụng nhân dân** → `NGHIA_VU_QUYEN` (span: `[16:23]`) *(lồng trong `e5` (`DIEM`))*
- `[e7]` **khoản 5 Điều 28 Thông tư này** → `THAM_CHIEU_PHAP_LY` (span: `[32:38]`) *(lồng trong `e5` (`DIEM`))*
- `[e8]` **theo quy định tại** → `TU_KHOA_PHAP_LY` (span: `[29:32]`) *(lồng trong `e5` (`DIEM`))*
- `[e9]` **Thẻ thành viên** → `GIAY_TO_HO_SO` (span: `[27:29]`) *(lồng trong `e5` (`DIEM`))*
- `[e10]` **quỹ tín dụng nhân dân** → `TO_CHUC_DOANH_NGHIEP` (span: `[20:23]`) *(lồng trong `e5` (`DIEM`), `e6` (`NGHIA_VU_QUYEN`))*

**Quan hệ:**
- (`e1` 06/2017/TT-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Ngân hàng Nhà nước Việt Nam `[CO_QUAN_BAN_HANH]`)
- (`e1` 06/2017/TT-NHNN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 2 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 06/2017/TT-NHNN `[SO_HIEU]`)
- (`e4` Khoản 3 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 2 `[DIEU]`)
- (`e5` a ) Hướng dẫn thống nhất trong hệ thống quỹ tín dụng nhân dân việc thiết kế , in ấn Thẻ thành viên theo quy định tại khoản 5 Điều 28 Thông tư này ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e4` Khoản 3 `[KHOAN]`)
- (`e6` Hướng dẫn thống nhất trong hệ thống quỹ tín dụng nhân dân `[NGHIA_VU_QUYEN]`) ==[ **TAC_DONG_CHU_THE** ]==> (`e10` quỹ tín dụng nhân dân `[TO_CHUC_DOANH_NGHIEP]`) *(Quan hệ lồng nhau)*
- (`e8` theo quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e7` khoản 5 Điều 28 Thông tư này `[THAM_CHIEU_PHAP_LY]`)
- (`e6` Hướng dẫn thống nhất trong hệ thống quỹ tín dụng nhân dân `[NGHIA_VU_QUYEN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e7` khoản 5 Điều 28 Thông tư này `[THAM_CHIEU_PHAP_LY]`)
- (`e6` Hướng dẫn thống nhất trong hệ thống quỹ tín dụng nhân dân `[NGHIA_VU_QUYEN]`) ==[ **TAC_DONG_DOI_TUONG** ]==> (`e9` Thẻ thành viên `[GIAY_TO_HO_SO]`)


---

### Mẫu #06_2017_TT-NHNN_122819#body_standalone_84 (Loại: `body_standalone`)
> **[Điều 2]`<DIEU>`** . **[Khoản 3]`<KHOAN>`** . **[a ) **[Hướng dẫn thống nhất trong hệ thống **[quỹ tín dụng nhân dân]`<TO_CHUC_DOANH_NGHIEP>`**]`<NGHIA_VU_QUYEN>`** việc thiết kế , in ấn **[Thẻ thành viên]`<GIAY_TO_HO_SO>`** **[theo quy định tại]`<TU_KHOA_PHAP_LY>`** **[khoản 5 Điều 28 Thông tư này]`<THAM_CHIEU_PHAP_LY>`** ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Điều 2** → `DIEU` (span: `[0:2]`)
- `[e1]` **Khoản 3** → `KHOAN` (span: `[3:5]`)
- `[e2]` **a ) Hướng dẫn thống nhất trong hệ thống quỹ tín dụng nhân dân việc thiết kế , in ấn Thẻ thành viên theo quy định tại khoản 5 Điều 28 Thông tư này ;** → `DIEM` (span: `[6:31]`)
- `[e3]` **Hướng dẫn thống nhất trong hệ thống quỹ tín dụng nhân dân** → `NGHIA_VU_QUYEN` (span: `[8:15]`) *(lồng trong `e2` (`DIEM`))*
- `[e4]` **khoản 5 Điều 28 Thông tư này** → `THAM_CHIEU_PHAP_LY` (span: `[24:30]`) *(lồng trong `e2` (`DIEM`))*
- `[e5]` **theo quy định tại** → `TU_KHOA_PHAP_LY` (span: `[21:24]`) *(lồng trong `e2` (`DIEM`))*
- `[e6]` **Thẻ thành viên** → `GIAY_TO_HO_SO` (span: `[19:21]`) *(lồng trong `e2` (`DIEM`))*
- `[e7]` **quỹ tín dụng nhân dân** → `TO_CHUC_DOANH_NGHIEP` (span: `[12:15]`) *(lồng trong `e2` (`DIEM`), `e3` (`NGHIA_VU_QUYEN`))*

**Quan hệ:**
- (`e1` Khoản 3 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 2 `[DIEU]`)
- (`e2` a ) Hướng dẫn thống nhất trong hệ thống quỹ tín dụng nhân dân việc thiết kế , in ấn Thẻ thành viên theo quy định tại khoản 5 Điều 28 Thông tư này ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e1` Khoản 3 `[KHOAN]`)
- (`e3` Hướng dẫn thống nhất trong hệ thống quỹ tín dụng nhân dân `[NGHIA_VU_QUYEN]`) ==[ **TAC_DONG_CHU_THE** ]==> (`e7` quỹ tín dụng nhân dân `[TO_CHUC_DOANH_NGHIEP]`) *(Quan hệ lồng nhau)*
- (`e5` theo quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e4` khoản 5 Điều 28 Thông tư này `[THAM_CHIEU_PHAP_LY]`)
- (`e3` Hướng dẫn thống nhất trong hệ thống quỹ tín dụng nhân dân `[NGHIA_VU_QUYEN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e4` khoản 5 Điều 28 Thông tư này `[THAM_CHIEU_PHAP_LY]`)
- (`e3` Hướng dẫn thống nhất trong hệ thống quỹ tín dụng nhân dân `[NGHIA_VU_QUYEN]`) ==[ **TAC_DONG_DOI_TUONG** ]==> (`e6` Thẻ thành viên `[GIAY_TO_HO_SO]`)


---

### Mẫu #06_2017_TT-NHNN_122819#body_context_85 (Loại: `body_context`)
> **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[06/2017/TT-NHNN]`<SO_HIEU>`** . **[Điều 2]`<DIEU>`** . **[Khoản 3]`<KHOAN>`** . **[b ) Có ý kiến tham gia bằng văn bản đối với danh sách nhân sự dự kiến bầu , bổ nhiệm làm Chủ tịch và các thành viên khác của **[Hội đồng quản trị]`<TO_CHUC_DOANH_NGHIEP>`** , Trưởng ban và các thành viên khác của **[Ban kiểm soát]`<TO_CHUC_DOANH_NGHIEP>`** , **[Giám đốc]`<CHU_THE_CA_NHAN>`** **[quỹ tín dụng nhân dân]`<TO_CHUC_DOANH_NGHIEP>`** khi **[Ngân hàng Nhà nước]`<CO_QUAN_THAM_QUYEN>`** chi nhánh hoặc **[quỹ tín dụng nhân dân]`<TO_CHUC_DOANH_NGHIEP>`** yêu cầu .]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[4:5]`)
- `[e1]` **06/2017/TT-NHNN** → `SO_HIEU` (span: `[6:7]`)
- `[e2]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_BAN_HANH` (span: `[0:3]`)
- `[e3]` **Điều 2** → `DIEU` (span: `[8:10]`)
- `[e4]` **Khoản 3** → `KHOAN` (span: `[11:13]`)
- `[e5]` **b ) Có ý kiến tham gia bằng văn bản đối với danh sách nhân sự dự kiến bầu , bổ nhiệm làm Chủ tịch và các thành viên khác của Hội đồng quản trị , Trưởng ban và các thành viên khác của Ban kiểm soát , Giám đốc quỹ tín dụng nhân dân khi Ngân hàng Nhà nước chi nhánh hoặc quỹ tín dụng nhân dân yêu cầu .** → `DIEM` (span: `[14:62]`)
- `[e6]` **Ngân hàng Nhà nước** → `CO_QUAN_THAM_QUYEN` (span: `[53:55]`) *(lồng trong `e5` (`DIEM`))*
- `[e7]` **Hội đồng quản trị** → `TO_CHUC_DOANH_NGHIEP` (span: `[35:37]`) *(lồng trong `e5` (`DIEM`))*
- `[e8]` **Ban kiểm soát** → `TO_CHUC_DOANH_NGHIEP` (span: `[45:47]`) *(lồng trong `e5` (`DIEM`))*
- `[e9]` **quỹ tín dụng nhân dân** → `TO_CHUC_DOANH_NGHIEP` (span: `[49:52]`) *(lồng trong `e5` (`DIEM`))*
- `[e10]` **quỹ tín dụng nhân dân** → `TO_CHUC_DOANH_NGHIEP` (span: `[57:60]`) *(lồng trong `e5` (`DIEM`))*
- `[e11]` **Giám đốc** → `CHU_THE_CA_NHAN` (span: `[48:49]`) *(lồng trong `e5` (`DIEM`))*

**Quan hệ:**
- (`e1` 06/2017/TT-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Ngân hàng Nhà nước Việt Nam `[CO_QUAN_BAN_HANH]`)
- (`e1` 06/2017/TT-NHNN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 2 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 06/2017/TT-NHNN `[SO_HIEU]`)
- (`e4` Khoản 3 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 2 `[DIEU]`)
- (`e5` b ) Có ý kiến tham gia bằng văn bản đối với danh sách nhân sự dự kiến bầu , bổ nhiệm làm Chủ tịch và các thành viên khác của Hội đồng quản trị , Trưởng ban và các thành viên khác của Ban kiểm soát , Giám đốc quỹ tín dụng nhân dân khi Ngân hàng Nhà nước chi nhánh hoặc quỹ tín dụng nhân dân yêu cầu . `[DIEM]`) ==[ **THUOC_VE** ]==> (`e4` Khoản 3 `[KHOAN]`)


---

### Mẫu #06_2017_TT-NHNN_122819#body_standalone_86 (Loại: `body_standalone`)
> **[Điều 2]`<DIEU>`** . **[Khoản 3]`<KHOAN>`** . **[b ) Có ý kiến tham gia bằng văn bản đối với danh sách nhân sự dự kiến bầu , bổ nhiệm làm Chủ tịch và các thành viên khác của **[Hội đồng quản trị]`<TO_CHUC_DOANH_NGHIEP>`** , Trưởng ban và các thành viên khác của **[Ban kiểm soát]`<TO_CHUC_DOANH_NGHIEP>`** , **[Giám đốc]`<CHU_THE_CA_NHAN>`** **[quỹ tín dụng nhân dân]`<TO_CHUC_DOANH_NGHIEP>`** khi **[Ngân hàng Nhà nước]`<CO_QUAN_THAM_QUYEN>`** chi nhánh hoặc **[quỹ tín dụng nhân dân]`<TO_CHUC_DOANH_NGHIEP>`** yêu cầu .]`<DIEM>`**

**Thực thể:**
- `[e0]` **Điều 2** → `DIEU` (span: `[0:2]`)
- `[e1]` **Khoản 3** → `KHOAN` (span: `[3:5]`)
- `[e2]` **b ) Có ý kiến tham gia bằng văn bản đối với danh sách nhân sự dự kiến bầu , bổ nhiệm làm Chủ tịch và các thành viên khác của Hội đồng quản trị , Trưởng ban và các thành viên khác của Ban kiểm soát , Giám đốc quỹ tín dụng nhân dân khi Ngân hàng Nhà nước chi nhánh hoặc quỹ tín dụng nhân dân yêu cầu .** → `DIEM` (span: `[6:54]`)
- `[e3]` **Ngân hàng Nhà nước** → `CO_QUAN_THAM_QUYEN` (span: `[45:47]`) *(lồng trong `e2` (`DIEM`))*
- `[e4]` **Hội đồng quản trị** → `TO_CHUC_DOANH_NGHIEP` (span: `[27:29]`) *(lồng trong `e2` (`DIEM`))*
- `[e5]` **Ban kiểm soát** → `TO_CHUC_DOANH_NGHIEP` (span: `[37:39]`) *(lồng trong `e2` (`DIEM`))*
- `[e6]` **quỹ tín dụng nhân dân** → `TO_CHUC_DOANH_NGHIEP` (span: `[41:44]`) *(lồng trong `e2` (`DIEM`))*
- `[e7]` **quỹ tín dụng nhân dân** → `TO_CHUC_DOANH_NGHIEP` (span: `[49:52]`) *(lồng trong `e2` (`DIEM`))*
- `[e8]` **Giám đốc** → `CHU_THE_CA_NHAN` (span: `[40:41]`) *(lồng trong `e2` (`DIEM`))*

**Quan hệ:**
- (`e1` Khoản 3 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 2 `[DIEU]`)
- (`e2` b ) Có ý kiến tham gia bằng văn bản đối với danh sách nhân sự dự kiến bầu , bổ nhiệm làm Chủ tịch và các thành viên khác của Hội đồng quản trị , Trưởng ban và các thành viên khác của Ban kiểm soát , Giám đốc quỹ tín dụng nhân dân khi Ngân hàng Nhà nước chi nhánh hoặc quỹ tín dụng nhân dân yêu cầu . `[DIEM]`) ==[ **THUOC_VE** ]==> (`e1` Khoản 3 `[KHOAN]`)


---

### Mẫu #06_2017_TT-NHNN_122819#body_context_87 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[06/2017/TT-NHNN]`<SO_HIEU>`** của **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Thanh tra , giám sát ngân hàng]`<LINH_VUC>`** . **[Điều 3 . **[Bãi bỏ]`<TU_KHOA_PHAP_LY>`** **[khoản 16 , khoản 22 Điều 11]`<THAM_CHIEU_PHAP_LY>`** và **[khoản 3 Điều 16 Thông tư số 04/2015/TT-NHNN]`<THAM_CHIEU_PHAP_LY>`** **[ngày 31/3/2015]`<NGAY_THAM_CHIEU>`** của **[Thống đốc Ngân hàng Nhà nước]`<CO_QUAN_THAM_QUYEN>`** quy định về **[quỹ tín dụng nhân dân]`<TO_CHUC_DOANH_NGHIEP>`** .]`<DIEU>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **06/2017/TT-NHNN** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_BAN_HANH` (span: `[4:7]`)
- `[e3]` **Thanh tra , giám sát ngân hàng** → `LINH_VUC` (span: `[9:13]`)
- `[e4]` **Điều 3 . Bãi bỏ khoản 16 , khoản 22 Điều 11 và khoản 3 Điều 16 Thông tư số 04/2015/TT-NHNN ngày 31/3/2015 của Thống đốc Ngân hàng Nhà nước quy định về quỹ tín dụng nhân dân .** → `DIEU` (span: `[14:45]`)
- `[e5]` **khoản 16 , khoản 22 Điều 11** → `THAM_CHIEU_PHAP_LY` (span: `[18:25]`) *(lồng trong `e4` (`DIEU`))*
- `[e6]` **khoản 3 Điều 16 Thông tư số 04/2015/TT-NHNN** → `THAM_CHIEU_PHAP_LY` (span: `[26:33]`) *(lồng trong `e4` (`DIEU`))*
- `[e7]` **Bãi bỏ** → `TU_KHOA_PHAP_LY` (span: `[17:18]`) *(lồng trong `e4` (`DIEU`))*
- `[e8]` **ngày 31/3/2015** → `NGAY_THAM_CHIEU` (span: `[33:35]`) *(lồng trong `e4` (`DIEU`))*
- `[e9]` **Thống đốc Ngân hàng Nhà nước** → `CO_QUAN_THAM_QUYEN` (span: `[36:39]`) *(lồng trong `e4` (`DIEU`))*
- `[e10]` **quỹ tín dụng nhân dân** → `TO_CHUC_DOANH_NGHIEP` (span: `[41:44]`) *(lồng trong `e4` (`DIEU`))*

**Quan hệ:**
- (`e1` 06/2017/TT-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Ngân hàng Nhà nước Việt Nam `[CO_QUAN_BAN_HANH]`)
- (`e1` 06/2017/TT-NHNN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 06/2017/TT-NHNN `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Thanh tra , giám sát ngân hàng `[LINH_VUC]`)
- (`e4` Điều 3 . Bãi bỏ khoản 16 , khoản 22 Điều 11 và khoản 3 Điều 16 Thông tư số 04/2015/TT-NHNN ngày 31/3/2015 của Thống đốc Ngân hàng Nhà nước quy định về quỹ tín dụng nhân dân . `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 06/2017/TT-NHNN `[SO_HIEU]`)
- (`e1` 06/2017/TT-NHNN `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Thanh tra , giám sát ngân hàng `[LINH_VUC]`)
- (`e4` Điều 3 . Bãi bỏ khoản 16 , khoản 22 Điều 11 và khoản 3 Điều 16 Thông tư số 04/2015/TT-NHNN ngày 31/3/2015 của Thống đốc Ngân hàng Nhà nước quy định về quỹ tín dụng nhân dân . `[DIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Thanh tra , giám sát ngân hàng `[LINH_VUC]`)
- (`e7` Bãi bỏ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e5` khoản 16 , khoản 22 Điều 11 `[THAM_CHIEU_PHAP_LY]`)
- (`e4` Điều 3 . Bãi bỏ khoản 16 , khoản 22 Điều 11 và khoản 3 Điều 16 Thông tư số 04/2015/TT-NHNN ngày 31/3/2015 của Thống đốc Ngân hàng Nhà nước quy định về quỹ tín dụng nhân dân . `[DIEU]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e5` khoản 16 , khoản 22 Điều 11 `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e7` Bãi bỏ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e6` khoản 3 Điều 16 Thông tư số 04/2015/TT-NHNN `[THAM_CHIEU_PHAP_LY]`)
- (`e4` Điều 3 . Bãi bỏ khoản 16 , khoản 22 Điều 11 và khoản 3 Điều 16 Thông tư số 04/2015/TT-NHNN ngày 31/3/2015 của Thống đốc Ngân hàng Nhà nước quy định về quỹ tín dụng nhân dân . `[DIEU]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e6` khoản 3 Điều 16 Thông tư số 04/2015/TT-NHNN `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e6` khoản 3 Điều 16 Thông tư số 04/2015/TT-NHNN `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e8` ngày 31/3/2015 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #06_2017_TT-NHNN_122819#body_standalone_88 (Loại: `body_standalone`)
> **[Điều 3 . **[Bãi bỏ]`<TU_KHOA_PHAP_LY>`** **[khoản 16 , khoản 22 Điều 11]`<THAM_CHIEU_PHAP_LY>`** và **[khoản 3 Điều 16 Thông tư số 04/2015/TT-NHNN]`<THAM_CHIEU_PHAP_LY>`** **[ngày 31/3/2015]`<NGAY_THAM_CHIEU>`** của **[Thống đốc Ngân hàng Nhà nước]`<CO_QUAN_THAM_QUYEN>`** quy định về **[quỹ tín dụng nhân dân]`<TO_CHUC_DOANH_NGHIEP>`** .]`<DIEU>`**

**Thực thể:**
- `[e0]` **Điều 3 . Bãi bỏ khoản 16 , khoản 22 Điều 11 và khoản 3 Điều 16 Thông tư số 04/2015/TT-NHNN ngày 31/3/2015 của Thống đốc Ngân hàng Nhà nước quy định về quỹ tín dụng nhân dân .** → `DIEU` (span: `[0:31]`)
- `[e1]` **khoản 16 , khoản 22 Điều 11** → `THAM_CHIEU_PHAP_LY` (span: `[4:11]`) *(lồng trong `e0` (`DIEU`))*
- `[e2]` **khoản 3 Điều 16 Thông tư số 04/2015/TT-NHNN** → `THAM_CHIEU_PHAP_LY` (span: `[12:19]`) *(lồng trong `e0` (`DIEU`))*
- `[e3]` **Bãi bỏ** → `TU_KHOA_PHAP_LY` (span: `[3:4]`) *(lồng trong `e0` (`DIEU`))*
- `[e4]` **ngày 31/3/2015** → `NGAY_THAM_CHIEU` (span: `[19:21]`) *(lồng trong `e0` (`DIEU`))*
- `[e5]` **Thống đốc Ngân hàng Nhà nước** → `CO_QUAN_THAM_QUYEN` (span: `[22:25]`) *(lồng trong `e0` (`DIEU`))*
- `[e6]` **quỹ tín dụng nhân dân** → `TO_CHUC_DOANH_NGHIEP` (span: `[27:30]`) *(lồng trong `e0` (`DIEU`))*

**Quan hệ:**
- (`e3` Bãi bỏ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e1` khoản 16 , khoản 22 Điều 11 `[THAM_CHIEU_PHAP_LY]`)
- (`e0` Điều 3 . Bãi bỏ khoản 16 , khoản 22 Điều 11 và khoản 3 Điều 16 Thông tư số 04/2015/TT-NHNN ngày 31/3/2015 của Thống đốc Ngân hàng Nhà nước quy định về quỹ tín dụng nhân dân . `[DIEU]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e1` khoản 16 , khoản 22 Điều 11 `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e3` Bãi bỏ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e2` khoản 3 Điều 16 Thông tư số 04/2015/TT-NHNN `[THAM_CHIEU_PHAP_LY]`)
- (`e0` Điều 3 . Bãi bỏ khoản 16 , khoản 22 Điều 11 và khoản 3 Điều 16 Thông tư số 04/2015/TT-NHNN ngày 31/3/2015 của Thống đốc Ngân hàng Nhà nước quy định về quỹ tín dụng nhân dân . `[DIEU]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e2` khoản 3 Điều 16 Thông tư số 04/2015/TT-NHNN `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e2` khoản 3 Điều 16 Thông tư số 04/2015/TT-NHNN `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e4` ngày 31/3/2015 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #06_2017_TT-NHNN_122819#body_context_89 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[06/2017/TT-NHNN]`<SO_HIEU>`** của **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Thanh tra , giám sát ngân hàng]`<LINH_VUC>`** . **[Điều 4]`<DIEU>`** . **[1 . Thông tư này có hiệu lực thi hành kể từ ngày 01 tháng 09 năm 2017 .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **06/2017/TT-NHNN** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_BAN_HANH` (span: `[4:7]`)
- `[e3]` **Thanh tra , giám sát ngân hàng** → `LINH_VUC` (span: `[9:13]`)
- `[e4]` **Điều 4** → `DIEU` (span: `[14:16]`)
- `[e5]` **1 . Thông tư này có hiệu lực thi hành kể từ ngày 01 tháng 09 năm 2017 .** → `KHOAN` (span: `[17:33]`)

**Quan hệ:**
- (`e1` 06/2017/TT-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Ngân hàng Nhà nước Việt Nam `[CO_QUAN_BAN_HANH]`)
- (`e1` 06/2017/TT-NHNN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 06/2017/TT-NHNN `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Thanh tra , giám sát ngân hàng `[LINH_VUC]`)
- (`e4` Điều 4 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 06/2017/TT-NHNN `[SO_HIEU]`)
- (`e5` 1 . Thông tư này có hiệu lực thi hành kể từ ngày 01 tháng 09 năm 2017 . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 4 `[DIEU]`)
- (`e1` 06/2017/TT-NHNN `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Thanh tra , giám sát ngân hàng `[LINH_VUC]`)
- (`e5` 1 . Thông tư này có hiệu lực thi hành kể từ ngày 01 tháng 09 năm 2017 . `[KHOAN]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Thanh tra , giám sát ngân hàng `[LINH_VUC]`)


---

### Mẫu #06_2017_TT-NHNN_122819#body_standalone_90 (Loại: `body_standalone`)
> **[Điều 4]`<DIEU>`** . **[1 . Thông tư này có hiệu lực thi hành kể từ ngày 01 tháng 09 năm 2017 .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 4** → `DIEU` (span: `[0:2]`)
- `[e1]` **1 . Thông tư này có hiệu lực thi hành kể từ ngày 01 tháng 09 năm 2017 .** → `KHOAN` (span: `[3:19]`)

**Quan hệ:**
- (`e1` 1 . Thông tư này có hiệu lực thi hành kể từ ngày 01 tháng 09 năm 2017 . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 4 `[DIEU]`)


---

### Mẫu #06_2017_TT-NHNN_122819#body_context_91 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[06/2017/TT-NHNN]`<SO_HIEU>`** ban hành **[ngày 05 tháng 07 năm 2017]`<NGAY_BAN_HANH>`** bởi **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_BAN_HANH>`** . **[Điều 4]`<DIEU>`** . **[2 . Chánh Văn phòng , **[Chánh Thanh tra , giám sát ngân hàng]`<CO_QUAN_THAM_QUYEN>`** , Thủ trưởng các đơn vị thuộc **[Ngân hàng Nhà nước]`<CO_QUAN_THAM_QUYEN>`** , **[Giám đốc]`<CHU_THE_CA_NHAN>`** **[Ngân hàng Nhà nước chi nhánh tỉnh , thành phố trực thuộc Trung ương]`<CO_QUAN_THAM_QUYEN>`** , Chủ tịch **[Hội đồng quản trị]`<TO_CHUC_DOANH_NGHIEP>`** , **[Tổng giám đốc]`<CHU_THE_CA_NHAN>`** **[Ngân hàng Hợp tác xã]`<TO_CHUC_DOANH_NGHIEP>`** , Chủ tịch **[Hội đồng quản trị]`<TO_CHUC_DOANH_NGHIEP>`** , **[Giám đốc]`<CHU_THE_CA_NHAN>`** **[quỹ tín dụng nhân dân]`<TO_CHUC_DOANH_NGHIEP>`** chịu trách nhiệm tổ chức thực hiện Thông tư này . / .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **06/2017/TT-NHNN** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_BAN_HANH` (span: `[11:14]`)
- `[e3]` **ngày 05 tháng 07 năm 2017** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 4** → `DIEU` (span: `[15:17]`)
- `[e5]` **2 . Chánh Văn phòng , Chánh Thanh tra , giám sát ngân hàng , Thủ trưởng các đơn vị thuộc Ngân hàng Nhà nước , Giám đốc Ngân hàng Nhà nước chi nhánh tỉnh , thành phố trực thuộc Trung ương , Chủ tịch Hội đồng quản trị , Tổng giám đốc Ngân hàng Hợp tác xã , Chủ tịch Hội đồng quản trị , Giám đốc quỹ tín dụng nhân dân chịu trách nhiệm tổ chức thực hiện Thông tư này . / .** → `KHOAN` (span: `[18:71]`)
- `[e6]` **Chánh Thanh tra , giám sát ngân hàng** → `CO_QUAN_THAM_QUYEN` (span: `[23:28]`) *(lồng trong `e5` (`KHOAN`))*
- `[e7]` **Ngân hàng Nhà nước** → `CO_QUAN_THAM_QUYEN` (span: `[33:35]`) *(lồng trong `e5` (`KHOAN`))*
- `[e8]` **Ngân hàng Nhà nước chi nhánh tỉnh , thành phố trực thuộc Trung ương** → `CO_QUAN_THAM_QUYEN` (span: `[37:45]`) *(lồng trong `e5` (`KHOAN`))*
- `[e9]` **Hội đồng quản trị** → `TO_CHUC_DOANH_NGHIEP` (span: `[47:49]`) *(lồng trong `e5` (`KHOAN`))*
- `[e10]` **Ngân hàng Hợp tác xã** → `TO_CHUC_DOANH_NGHIEP` (span: `[51:53]`) *(lồng trong `e5` (`KHOAN`))*
- `[e11]` **Hội đồng quản trị** → `TO_CHUC_DOANH_NGHIEP` (span: `[55:57]`) *(lồng trong `e5` (`KHOAN`))*
- `[e12]` **quỹ tín dụng nhân dân** → `TO_CHUC_DOANH_NGHIEP` (span: `[59:62]`) *(lồng trong `e5` (`KHOAN`))*
- `[e13]` **Giám đốc** → `CHU_THE_CA_NHAN` (span: `[36:37]`) *(lồng trong `e5` (`KHOAN`))*
- `[e14]` **Tổng giám đốc** → `CHU_THE_CA_NHAN` (span: `[50:51]`) *(lồng trong `e5` (`KHOAN`))*
- `[e15]` **Giám đốc** → `CHU_THE_CA_NHAN` (span: `[58:59]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 06/2017/TT-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Ngân hàng Nhà nước Việt Nam `[CO_QUAN_BAN_HANH]`)
- (`e1` 06/2017/TT-NHNN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 06/2017/TT-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 05 tháng 07 năm 2017 `[NGAY_BAN_HANH]`)
- (`e4` Điều 4 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 06/2017/TT-NHNN `[SO_HIEU]`)
- (`e5` 2 . Chánh Văn phòng , Chánh Thanh tra , giám sát ngân hàng , Thủ trưởng các đơn vị thuộc Ngân hàng Nhà nước , Giám đốc Ngân hàng Nhà nước chi nhánh tỉnh , thành phố trực thuộc Trung ương , Chủ tịch Hội đồng quản trị , Tổng giám đốc Ngân hàng Hợp tác xã , Chủ tịch Hội đồng quản trị , Giám đốc quỹ tín dụng nhân dân chịu trách nhiệm tổ chức thực hiện Thông tư này . / . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 4 `[DIEU]`)


---

### Mẫu #06_2017_TT-NHNN_122819#body_standalone_92 (Loại: `body_standalone`)
> **[Điều 4]`<DIEU>`** . **[2 . Chánh Văn phòng , **[Chánh Thanh tra , giám sát ngân hàng]`<CO_QUAN_THAM_QUYEN>`** , Thủ trưởng các đơn vị thuộc **[Ngân hàng Nhà nước]`<CO_QUAN_THAM_QUYEN>`** , **[Giám đốc]`<CHU_THE_CA_NHAN>`** **[Ngân hàng Nhà nước chi nhánh tỉnh , thành phố trực thuộc Trung ương]`<CO_QUAN_THAM_QUYEN>`** , Chủ tịch **[Hội đồng quản trị]`<TO_CHUC_DOANH_NGHIEP>`** , **[Tổng giám đốc]`<CHU_THE_CA_NHAN>`** **[Ngân hàng Hợp tác xã]`<TO_CHUC_DOANH_NGHIEP>`** , Chủ tịch **[Hội đồng quản trị]`<TO_CHUC_DOANH_NGHIEP>`** , **[Giám đốc]`<CHU_THE_CA_NHAN>`** **[quỹ tín dụng nhân dân]`<TO_CHUC_DOANH_NGHIEP>`** chịu trách nhiệm tổ chức thực hiện Thông tư này . / .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 4** → `DIEU` (span: `[0:2]`)
- `[e1]` **2 . Chánh Văn phòng , Chánh Thanh tra , giám sát ngân hàng , Thủ trưởng các đơn vị thuộc Ngân hàng Nhà nước , Giám đốc Ngân hàng Nhà nước chi nhánh tỉnh , thành phố trực thuộc Trung ương , Chủ tịch Hội đồng quản trị , Tổng giám đốc Ngân hàng Hợp tác xã , Chủ tịch Hội đồng quản trị , Giám đốc quỹ tín dụng nhân dân chịu trách nhiệm tổ chức thực hiện Thông tư này . / .** → `KHOAN` (span: `[3:56]`)
- `[e2]` **Chánh Thanh tra , giám sát ngân hàng** → `CO_QUAN_THAM_QUYEN` (span: `[8:13]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **Ngân hàng Nhà nước** → `CO_QUAN_THAM_QUYEN` (span: `[18:20]`) *(lồng trong `e1` (`KHOAN`))*
- `[e4]` **Ngân hàng Nhà nước chi nhánh tỉnh , thành phố trực thuộc Trung ương** → `CO_QUAN_THAM_QUYEN` (span: `[22:30]`) *(lồng trong `e1` (`KHOAN`))*
- `[e5]` **Hội đồng quản trị** → `TO_CHUC_DOANH_NGHIEP` (span: `[32:34]`) *(lồng trong `e1` (`KHOAN`))*
- `[e6]` **Ngân hàng Hợp tác xã** → `TO_CHUC_DOANH_NGHIEP` (span: `[36:38]`) *(lồng trong `e1` (`KHOAN`))*
- `[e7]` **Hội đồng quản trị** → `TO_CHUC_DOANH_NGHIEP` (span: `[40:42]`) *(lồng trong `e1` (`KHOAN`))*
- `[e8]` **quỹ tín dụng nhân dân** → `TO_CHUC_DOANH_NGHIEP` (span: `[44:47]`) *(lồng trong `e1` (`KHOAN`))*
- `[e9]` **Giám đốc** → `CHU_THE_CA_NHAN` (span: `[21:22]`) *(lồng trong `e1` (`KHOAN`))*
- `[e10]` **Tổng giám đốc** → `CHU_THE_CA_NHAN` (span: `[35:36]`) *(lồng trong `e1` (`KHOAN`))*
- `[e11]` **Giám đốc** → `CHU_THE_CA_NHAN` (span: `[43:44]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 2 . Chánh Văn phòng , Chánh Thanh tra , giám sát ngân hàng , Thủ trưởng các đơn vị thuộc Ngân hàng Nhà nước , Giám đốc Ngân hàng Nhà nước chi nhánh tỉnh , thành phố trực thuộc Trung ương , Chủ tịch Hội đồng quản trị , Tổng giám đốc Ngân hàng Hợp tác xã , Chủ tịch Hội đồng quản trị , Giám đốc quỹ tín dụng nhân dân chịu trách nhiệm tổ chức thực hiện Thông tư này . / . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 4 `[DIEU]`)


---

### Mẫu #06_2017_TT-NHNN_122819#body_context_93 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[06/2017/TT-NHNN]`<SO_HIEU>`** của **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Thanh tra , giám sát ngân hàng]`<LINH_VUC>`** . **[Điều 1]`<DIEU>`** . **[2 . Việc trích nộp **[Quỹ bảo toàn]`<TO_CHUC_DOANH_NGHIEP>`** **[theo quy định tại]`<TU_KHOA_PHAP_LY>`** **[khoản 1 Điều này]`<THAM_CHIEU_PHAP_LY>`** được thực hiện như sau :]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **06/2017/TT-NHNN** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_BAN_HANH` (span: `[4:7]`)
- `[e3]` **Thanh tra , giám sát ngân hàng** → `LINH_VUC` (span: `[9:13]`)
- `[e4]` **Điều 1** → `DIEU` (span: `[14:16]`)
- `[e5]` **2 . Việc trích nộp Quỹ bảo toàn theo quy định tại khoản 1 Điều này được thực hiện như sau :** → `KHOAN` (span: `[17:36]`)
- `[e6]` **khoản 1 Điều này** → `THAM_CHIEU_PHAP_LY` (span: `[27:31]`) *(lồng trong `e5` (`KHOAN`))*
- `[e7]` **theo quy định tại** → `TU_KHOA_PHAP_LY` (span: `[24:27]`) *(lồng trong `e5` (`KHOAN`))*
- `[e8]` **Quỹ bảo toàn** → `TO_CHUC_DOANH_NGHIEP` (span: `[22:24]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 06/2017/TT-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Ngân hàng Nhà nước Việt Nam `[CO_QUAN_BAN_HANH]`)
- (`e1` 06/2017/TT-NHNN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 06/2017/TT-NHNN `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Thanh tra , giám sát ngân hàng `[LINH_VUC]`)
- (`e4` Điều 1 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 06/2017/TT-NHNN `[SO_HIEU]`)
- (`e5` 2 . Việc trích nộp Quỹ bảo toàn theo quy định tại khoản 1 Điều này được thực hiện như sau : `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 1 `[DIEU]`)
- (`e1` 06/2017/TT-NHNN `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Thanh tra , giám sát ngân hàng `[LINH_VUC]`)
- (`e5` 2 . Việc trích nộp Quỹ bảo toàn theo quy định tại khoản 1 Điều này được thực hiện như sau : `[KHOAN]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Thanh tra , giám sát ngân hàng `[LINH_VUC]`)
- (`e7` theo quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e6` khoản 1 Điều này `[THAM_CHIEU_PHAP_LY]`)
- (`e5` 2 . Việc trích nộp Quỹ bảo toàn theo quy định tại khoản 1 Điều này được thực hiện như sau : `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e6` khoản 1 Điều này `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #06_2017_TT-NHNN_122819#body_standalone_94 (Loại: `body_standalone`)
> **[Điều 1]`<DIEU>`** . **[2 . Việc trích nộp **[Quỹ bảo toàn]`<TO_CHUC_DOANH_NGHIEP>`** **[theo quy định tại]`<TU_KHOA_PHAP_LY>`** **[khoản 1 Điều này]`<THAM_CHIEU_PHAP_LY>`** được thực hiện như sau :]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 1** → `DIEU` (span: `[0:2]`)
- `[e1]` **2 . Việc trích nộp Quỹ bảo toàn theo quy định tại khoản 1 Điều này được thực hiện như sau :** → `KHOAN` (span: `[3:22]`)
- `[e2]` **khoản 1 Điều này** → `THAM_CHIEU_PHAP_LY` (span: `[13:17]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **theo quy định tại** → `TU_KHOA_PHAP_LY` (span: `[10:13]`) *(lồng trong `e1` (`KHOAN`))*
- `[e4]` **Quỹ bảo toàn** → `TO_CHUC_DOANH_NGHIEP` (span: `[8:10]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 2 . Việc trích nộp Quỹ bảo toàn theo quy định tại khoản 1 Điều này được thực hiện như sau : `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 1 `[DIEU]`)
- (`e3` theo quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e2` khoản 1 Điều này `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 2 . Việc trích nộp Quỹ bảo toàn theo quy định tại khoản 1 Điều này được thực hiện như sau : `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e2` khoản 1 Điều này `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #06_2017_TT-NHNN_122819#body_context_95 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[06/2017/TT-NHNN]`<SO_HIEU>`** của **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Thanh tra , giám sát ngân hàng]`<LINH_VUC>`** . **[Điều 2]`<DIEU>`** . **[7 . Bản sao **[giấy chứng minh nhân dân]`<GIAY_TO_HO_SO>`** hoặc **[hộ chiếu]`<GIAY_TO_HO_SO>`** hoặc **[thẻ căn cước công dân]`<GIAY_TO_HO_SO>`** ( đối với thành viên là cá nhân , **[người đại diện của pháp nhân]`<CHU_THE_CA_NHAN>`** , **[hộ gia đình]`<TO_CHUC_DOANH_NGHIEP>`** ) còn hiệu lực . Đối với thành viên là **[cán bộ , công chức , viên chức]`<CHU_THE_CA_NHAN>`** phải có thêm **[giấy xác nhận nơi công tác]`<GIAY_TO_HO_SO>`** , bản sao **[quyết định tuyển dụng]`<GIAY_TO_HO_SO>`** hoặc **[hợp đồng tuyển dụng]`<GIAY_TO_HO_SO>`** của cơ quan , đơn vị tuyển dụng ” .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **06/2017/TT-NHNN** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_BAN_HANH` (span: `[4:7]`)
- `[e3]` **Thanh tra , giám sát ngân hàng** → `LINH_VUC` (span: `[9:13]`)
- `[e4]` **Điều 2** → `DIEU` (span: `[14:16]`)
- `[e5]` **7 . Bản sao giấy chứng minh nhân dân hoặc hộ chiếu hoặc thẻ căn cước công dân ( đối với thành viên là cá nhân , người đại diện của pháp nhân , hộ gia đình ) còn hiệu lực . Đối với thành viên là cán bộ , công chức , viên chức phải có thêm giấy xác nhận nơi công tác , bản sao quyết định tuyển dụng hoặc hợp đồng tuyển dụng của cơ quan , đơn vị tuyển dụng ” .** → `KHOAN` (span: `[17:75]`)
- `[e6]` **giấy chứng minh nhân dân** → `GIAY_TO_HO_SO` (span: `[20:23]`) *(lồng trong `e5` (`KHOAN`))*
- `[e7]` **hộ chiếu** → `GIAY_TO_HO_SO` (span: `[24:25]`) *(lồng trong `e5` (`KHOAN`))*
- `[e8]` **thẻ căn cước công dân** → `GIAY_TO_HO_SO` (span: `[26:29]`) *(lồng trong `e5` (`KHOAN`))*
- `[e9]` **giấy xác nhận nơi công tác** → `GIAY_TO_HO_SO` (span: `[57:61]`) *(lồng trong `e5` (`KHOAN`))*
- `[e10]` **quyết định tuyển dụng** → `GIAY_TO_HO_SO` (span: `[63:65]`) *(lồng trong `e5` (`KHOAN`))*
- `[e11]` **hợp đồng tuyển dụng** → `GIAY_TO_HO_SO` (span: `[66:68]`) *(lồng trong `e5` (`KHOAN`))*
- `[e12]` **hộ gia đình** → `TO_CHUC_DOANH_NGHIEP` (span: `[40:42]`) *(lồng trong `e5` (`KHOAN`))*
- `[e13]` **người đại diện của pháp nhân** → `CHU_THE_CA_NHAN` (span: `[35:39]`) *(lồng trong `e5` (`KHOAN`))*
- `[e14]` **cán bộ , công chức , viên chức** → `CHU_THE_CA_NHAN` (span: `[49:54]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 06/2017/TT-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Ngân hàng Nhà nước Việt Nam `[CO_QUAN_BAN_HANH]`)
- (`e1` 06/2017/TT-NHNN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 06/2017/TT-NHNN `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Thanh tra , giám sát ngân hàng `[LINH_VUC]`)
- (`e4` Điều 2 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 06/2017/TT-NHNN `[SO_HIEU]`)
- (`e5` 7 . Bản sao giấy chứng minh nhân dân hoặc hộ chiếu hoặc thẻ căn cước công dân ( đối với thành viên là cá nhân , người đại diện của pháp nhân , hộ gia đình ) còn hiệu lực . Đối với thành viên là cán bộ , công chức , viên chức phải có thêm giấy xác nhận nơi công tác , bản sao quyết định tuyển dụng hoặc hợp đồng tuyển dụng của cơ quan , đơn vị tuyển dụng ” . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 2 `[DIEU]`)
- (`e1` 06/2017/TT-NHNN `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Thanh tra , giám sát ngân hàng `[LINH_VUC]`)
- (`e5` 7 . Bản sao giấy chứng minh nhân dân hoặc hộ chiếu hoặc thẻ căn cước công dân ( đối với thành viên là cá nhân , người đại diện của pháp nhân , hộ gia đình ) còn hiệu lực . Đối với thành viên là cán bộ , công chức , viên chức phải có thêm giấy xác nhận nơi công tác , bản sao quyết định tuyển dụng hoặc hợp đồng tuyển dụng của cơ quan , đơn vị tuyển dụng ” . `[KHOAN]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Thanh tra , giám sát ngân hàng `[LINH_VUC]`)


---

### Mẫu #06_2017_TT-NHNN_122819#body_standalone_96 (Loại: `body_standalone`)
> **[Điều 2]`<DIEU>`** . **[7 . Bản sao **[giấy chứng minh nhân dân]`<GIAY_TO_HO_SO>`** hoặc **[hộ chiếu]`<GIAY_TO_HO_SO>`** hoặc **[thẻ căn cước công dân]`<GIAY_TO_HO_SO>`** ( đối với thành viên là cá nhân , **[người đại diện của pháp nhân]`<CHU_THE_CA_NHAN>`** , **[hộ gia đình]`<TO_CHUC_DOANH_NGHIEP>`** ) còn hiệu lực . Đối với thành viên là **[cán bộ , công chức , viên chức]`<CHU_THE_CA_NHAN>`** phải có thêm **[giấy xác nhận nơi công tác]`<GIAY_TO_HO_SO>`** , bản sao **[quyết định tuyển dụng]`<GIAY_TO_HO_SO>`** hoặc **[hợp đồng tuyển dụng]`<GIAY_TO_HO_SO>`** của cơ quan , đơn vị tuyển dụng ” .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 2** → `DIEU` (span: `[0:2]`)
- `[e1]` **7 . Bản sao giấy chứng minh nhân dân hoặc hộ chiếu hoặc thẻ căn cước công dân ( đối với thành viên là cá nhân , người đại diện của pháp nhân , hộ gia đình ) còn hiệu lực . Đối với thành viên là cán bộ , công chức , viên chức phải có thêm giấy xác nhận nơi công tác , bản sao quyết định tuyển dụng hoặc hợp đồng tuyển dụng của cơ quan , đơn vị tuyển dụng ” .** → `KHOAN` (span: `[3:61]`)
- `[e2]` **giấy chứng minh nhân dân** → `GIAY_TO_HO_SO` (span: `[6:9]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **hộ chiếu** → `GIAY_TO_HO_SO` (span: `[10:11]`) *(lồng trong `e1` (`KHOAN`))*
- `[e4]` **thẻ căn cước công dân** → `GIAY_TO_HO_SO` (span: `[12:15]`) *(lồng trong `e1` (`KHOAN`))*
- `[e5]` **giấy xác nhận nơi công tác** → `GIAY_TO_HO_SO` (span: `[43:47]`) *(lồng trong `e1` (`KHOAN`))*
- `[e6]` **quyết định tuyển dụng** → `GIAY_TO_HO_SO` (span: `[49:51]`) *(lồng trong `e1` (`KHOAN`))*
- `[e7]` **hợp đồng tuyển dụng** → `GIAY_TO_HO_SO` (span: `[52:54]`) *(lồng trong `e1` (`KHOAN`))*
- `[e8]` **hộ gia đình** → `TO_CHUC_DOANH_NGHIEP` (span: `[26:28]`) *(lồng trong `e1` (`KHOAN`))*
- `[e9]` **người đại diện của pháp nhân** → `CHU_THE_CA_NHAN` (span: `[21:25]`) *(lồng trong `e1` (`KHOAN`))*
- `[e10]` **cán bộ , công chức , viên chức** → `CHU_THE_CA_NHAN` (span: `[35:40]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 7 . Bản sao giấy chứng minh nhân dân hoặc hộ chiếu hoặc thẻ căn cước công dân ( đối với thành viên là cá nhân , người đại diện của pháp nhân , hộ gia đình ) còn hiệu lực . Đối với thành viên là cán bộ , công chức , viên chức phải có thêm giấy xác nhận nơi công tác , bản sao quyết định tuyển dụng hoặc hợp đồng tuyển dụng của cơ quan , đơn vị tuyển dụng ” . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 2 `[DIEU]`)


---

### Mẫu #06_2017_TT-NHNN_122819#body_context_97 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[06/2017/TT-NHNN]`<SO_HIEU>`** của **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Thanh tra , giám sát ngân hàng]`<LINH_VUC>`** . **[Điều 2]`<DIEU>`** . **[Khoản 1 . Đối với cá nhân]`<KHOAN>`** : **[( i ) Đang bị **[truy cứu trách nhiệm hình sự]`<HINH_PHAT_CHE_TAI>`** , đang phải chấp hành **[bản án]`<GIAY_TO_HO_SO>`** , quyết định về hình sự của **[tòa án]`<CO_QUAN_THAM_QUYEN>`** ; người đã bị kết án từ tội phạm nghiêm trọng trở lên mà chưa được xóa án tích ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **06/2017/TT-NHNN** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_BAN_HANH` (span: `[4:7]`)
- `[e3]` **Thanh tra , giám sát ngân hàng** → `LINH_VUC` (span: `[9:13]`)
- `[e4]` **Điều 2** → `DIEU` (span: `[14:16]`)
- `[e5]` **Khoản 1 . Đối với cá nhân** → `KHOAN` (span: `[17:22]`)
- `[e6]` **( i ) Đang bị truy cứu trách nhiệm hình sự , đang phải chấp hành bản án , quyết định về hình sự của tòa án ; người đã bị kết án từ tội phạm nghiêm trọng trở lên mà chưa được xóa án tích ;** → `DIEM` (span: `[23:58]`)
- `[e7]` **truy cứu trách nhiệm hình sự** → `HINH_PHAT_CHE_TAI` (span: `[28:31]`) *(lồng trong `e6` (`DIEM`))*
- `[e8]` **tòa án** → `CO_QUAN_THAM_QUYEN` (span: `[41:42]`) *(lồng trong `e6` (`DIEM`))*
- `[e9]` **bản án** → `GIAY_TO_HO_SO` (span: `[35:36]`) *(lồng trong `e6` (`DIEM`))*

**Quan hệ:**
- (`e1` 06/2017/TT-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Ngân hàng Nhà nước Việt Nam `[CO_QUAN_BAN_HANH]`)
- (`e1` 06/2017/TT-NHNN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 06/2017/TT-NHNN `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Thanh tra , giám sát ngân hàng `[LINH_VUC]`)
- (`e4` Điều 2 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 06/2017/TT-NHNN `[SO_HIEU]`)
- (`e5` Khoản 1 . Đối với cá nhân `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 2 `[DIEU]`)
- (`e6` ( i ) Đang bị truy cứu trách nhiệm hình sự , đang phải chấp hành bản án , quyết định về hình sự của tòa án ; người đã bị kết án từ tội phạm nghiêm trọng trở lên mà chưa được xóa án tích ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e5` Khoản 1 . Đối với cá nhân `[KHOAN]`)
- (`e1` 06/2017/TT-NHNN `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Thanh tra , giám sát ngân hàng `[LINH_VUC]`)
- (`e7` truy cứu trách nhiệm hình sự `[HINH_PHAT_CHE_TAI]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Thanh tra , giám sát ngân hàng `[LINH_VUC]`)
- (`e7` truy cứu trách nhiệm hình sự `[HINH_PHAT_CHE_TAI]`) ==[ **TAC_DONG_DOI_TUONG** ]==> (`e9` bản án `[GIAY_TO_HO_SO]`)


---

### Mẫu #06_2017_TT-NHNN_122819#body_standalone_98 (Loại: `body_standalone`)
> **[Điều 2]`<DIEU>`** . **[Khoản 1 . Đối với cá nhân]`<KHOAN>`** : **[( i ) Đang bị **[truy cứu trách nhiệm hình sự]`<HINH_PHAT_CHE_TAI>`** , đang phải chấp hành **[bản án]`<GIAY_TO_HO_SO>`** , quyết định về hình sự của **[tòa án]`<CO_QUAN_THAM_QUYEN>`** ; người đã bị kết án từ tội phạm nghiêm trọng trở lên mà chưa được xóa án tích ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Điều 2** → `DIEU` (span: `[0:2]`)
- `[e1]` **Khoản 1 . Đối với cá nhân** → `KHOAN` (span: `[3:8]`)
- `[e2]` **( i ) Đang bị truy cứu trách nhiệm hình sự , đang phải chấp hành bản án , quyết định về hình sự của tòa án ; người đã bị kết án từ tội phạm nghiêm trọng trở lên mà chưa được xóa án tích ;** → `DIEM` (span: `[9:44]`)
- `[e3]` **truy cứu trách nhiệm hình sự** → `HINH_PHAT_CHE_TAI` (span: `[14:17]`) *(lồng trong `e2` (`DIEM`))*
- `[e4]` **tòa án** → `CO_QUAN_THAM_QUYEN` (span: `[27:28]`) *(lồng trong `e2` (`DIEM`))*
- `[e5]` **bản án** → `GIAY_TO_HO_SO` (span: `[21:22]`) *(lồng trong `e2` (`DIEM`))*

**Quan hệ:**
- (`e1` Khoản 1 . Đối với cá nhân `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 2 `[DIEU]`)
- (`e2` ( i ) Đang bị truy cứu trách nhiệm hình sự , đang phải chấp hành bản án , quyết định về hình sự của tòa án ; người đã bị kết án từ tội phạm nghiêm trọng trở lên mà chưa được xóa án tích ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e1` Khoản 1 . Đối với cá nhân `[KHOAN]`)
- (`e3` truy cứu trách nhiệm hình sự `[HINH_PHAT_CHE_TAI]`) ==[ **TAC_DONG_DOI_TUONG** ]==> (`e5` bản án `[GIAY_TO_HO_SO]`)


---

### Mẫu #06_2017_TT-NHNN_122819#body_context_99 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[06/2017/TT-NHNN]`<SO_HIEU>`** ban hành **[ngày 05 tháng 07 năm 2017]`<NGAY_BAN_HANH>`** bởi **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_BAN_HANH>`** . **[Điều 2]`<DIEU>`** . **[2 . Đối với **[hộ gia đình]`<TO_CHUC_DOANH_NGHIEP>`** :]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **06/2017/TT-NHNN** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_BAN_HANH` (span: `[11:14]`)
- `[e3]` **ngày 05 tháng 07 năm 2017** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 2** → `DIEU` (span: `[15:17]`)
- `[e5]` **2 . Đối với hộ gia đình :** → `KHOAN` (span: `[18:24]`)
- `[e6]` **hộ gia đình** → `TO_CHUC_DOANH_NGHIEP` (span: `[21:23]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 06/2017/TT-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Ngân hàng Nhà nước Việt Nam `[CO_QUAN_BAN_HANH]`)
- (`e1` 06/2017/TT-NHNN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 06/2017/TT-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 05 tháng 07 năm 2017 `[NGAY_BAN_HANH]`)
- (`e4` Điều 2 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 06/2017/TT-NHNN `[SO_HIEU]`)
- (`e5` 2 . Đối với hộ gia đình : `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 2 `[DIEU]`)


---

### Mẫu #06_2017_TT-NHNN_122819#body_context_100 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[06/2017/TT-NHNN]`<SO_HIEU>`** của **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Thanh tra , giám sát ngân hàng]`<LINH_VUC>`** . **[Điều 2]`<DIEU>`** . **[4 . **[Quỹ tín dụng nhân dân]`<TO_CHUC_DOANH_NGHIEP>`** cho vay đối với **[khách hàng]`<CHU_THE_CA_NHAN>`** là pháp nhân , cá nhân không phải là thành viên , có tiền gửi tại **[quỹ tín dụng nhân dân]`<TO_CHUC_DOANH_NGHIEP>`** trên cơ sở bảo đảm bằng sổ tiền gửi do chính **[quỹ tín dụng nhân dân]`<TO_CHUC_DOANH_NGHIEP>`** phát hành . Tổng số tiền cho vay không được vượt quá số dư của sổ tiền gửi tại thời điểm quyết định cho vay và thời hạn cho vay không được vượt quá thời hạn còn lại của sổ tiền gửi .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **06/2017/TT-NHNN** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_BAN_HANH` (span: `[4:7]`)
- `[e3]` **Thanh tra , giám sát ngân hàng** → `LINH_VUC` (span: `[9:13]`)
- `[e4]` **Điều 2** → `DIEU` (span: `[14:16]`)
- `[e5]` **4 . Quỹ tín dụng nhân dân cho vay đối với khách hàng là pháp nhân , cá nhân không phải là thành viên , có tiền gửi tại quỹ tín dụng nhân dân trên cơ sở bảo đảm bằng sổ tiền gửi do chính quỹ tín dụng nhân dân phát hành . Tổng số tiền cho vay không được vượt quá số dư của sổ tiền gửi tại thời điểm quyết định cho vay và thời hạn cho vay không được vượt quá thời hạn còn lại của sổ tiền gửi .** → `KHOAN` (span: `[17:90]`)
- `[e6]` **Quỹ tín dụng nhân dân** → `TO_CHUC_DOANH_NGHIEP` (span: `[19:22]`) *(lồng trong `e5` (`KHOAN`))*
- `[e7]` **quỹ tín dụng nhân dân** → `TO_CHUC_DOANH_NGHIEP` (span: `[39:42]`) *(lồng trong `e5` (`KHOAN`))*
- `[e8]` **quỹ tín dụng nhân dân** → `TO_CHUC_DOANH_NGHIEP` (span: `[51:54]`) *(lồng trong `e5` (`KHOAN`))*
- `[e9]` **khách hàng** → `CHU_THE_CA_NHAN` (span: `[25:26]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 06/2017/TT-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Ngân hàng Nhà nước Việt Nam `[CO_QUAN_BAN_HANH]`)
- (`e1` 06/2017/TT-NHNN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 06/2017/TT-NHNN `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Thanh tra , giám sát ngân hàng `[LINH_VUC]`)
- (`e4` Điều 2 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 06/2017/TT-NHNN `[SO_HIEU]`)
- (`e5` 4 . Quỹ tín dụng nhân dân cho vay đối với khách hàng là pháp nhân , cá nhân không phải là thành viên , có tiền gửi tại quỹ tín dụng nhân dân trên cơ sở bảo đảm bằng sổ tiền gửi do chính quỹ tín dụng nhân dân phát hành . Tổng số tiền cho vay không được vượt quá số dư của sổ tiền gửi tại thời điểm quyết định cho vay và thời hạn cho vay không được vượt quá thời hạn còn lại của sổ tiền gửi . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 2 `[DIEU]`)
- (`e1` 06/2017/TT-NHNN `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Thanh tra , giám sát ngân hàng `[LINH_VUC]`)
- (`e5` 4 . Quỹ tín dụng nhân dân cho vay đối với khách hàng là pháp nhân , cá nhân không phải là thành viên , có tiền gửi tại quỹ tín dụng nhân dân trên cơ sở bảo đảm bằng sổ tiền gửi do chính quỹ tín dụng nhân dân phát hành . Tổng số tiền cho vay không được vượt quá số dư của sổ tiền gửi tại thời điểm quyết định cho vay và thời hạn cho vay không được vượt quá thời hạn còn lại của sổ tiền gửi . `[KHOAN]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Thanh tra , giám sát ngân hàng `[LINH_VUC]`)


---

### Mẫu #06_2017_TT-NHNN_122819#body_standalone_101 (Loại: `body_standalone`)
> **[Điều 2]`<DIEU>`** . **[4 . **[Quỹ tín dụng nhân dân]`<TO_CHUC_DOANH_NGHIEP>`** cho vay đối với **[khách hàng]`<CHU_THE_CA_NHAN>`** là pháp nhân , cá nhân không phải là thành viên , có tiền gửi tại **[quỹ tín dụng nhân dân]`<TO_CHUC_DOANH_NGHIEP>`** trên cơ sở bảo đảm bằng sổ tiền gửi do chính **[quỹ tín dụng nhân dân]`<TO_CHUC_DOANH_NGHIEP>`** phát hành . Tổng số tiền cho vay không được vượt quá số dư của sổ tiền gửi tại thời điểm quyết định cho vay và thời hạn cho vay không được vượt quá thời hạn còn lại của sổ tiền gửi .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 2** → `DIEU` (span: `[0:2]`)
- `[e1]` **4 . Quỹ tín dụng nhân dân cho vay đối với khách hàng là pháp nhân , cá nhân không phải là thành viên , có tiền gửi tại quỹ tín dụng nhân dân trên cơ sở bảo đảm bằng sổ tiền gửi do chính quỹ tín dụng nhân dân phát hành . Tổng số tiền cho vay không được vượt quá số dư của sổ tiền gửi tại thời điểm quyết định cho vay và thời hạn cho vay không được vượt quá thời hạn còn lại của sổ tiền gửi .** → `KHOAN` (span: `[3:76]`)
- `[e2]` **Quỹ tín dụng nhân dân** → `TO_CHUC_DOANH_NGHIEP` (span: `[5:8]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **quỹ tín dụng nhân dân** → `TO_CHUC_DOANH_NGHIEP` (span: `[25:28]`) *(lồng trong `e1` (`KHOAN`))*
- `[e4]` **quỹ tín dụng nhân dân** → `TO_CHUC_DOANH_NGHIEP` (span: `[37:40]`) *(lồng trong `e1` (`KHOAN`))*
- `[e5]` **khách hàng** → `CHU_THE_CA_NHAN` (span: `[11:12]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 4 . Quỹ tín dụng nhân dân cho vay đối với khách hàng là pháp nhân , cá nhân không phải là thành viên , có tiền gửi tại quỹ tín dụng nhân dân trên cơ sở bảo đảm bằng sổ tiền gửi do chính quỹ tín dụng nhân dân phát hành . Tổng số tiền cho vay không được vượt quá số dư của sổ tiền gửi tại thời điểm quyết định cho vay và thời hạn cho vay không được vượt quá thời hạn còn lại của sổ tiền gửi . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 2 `[DIEU]`)


---

### Mẫu #06_2017_TT-NHNN_122819#body_context_102 (Loại: `body_context`)
> **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[06/2017/TT-NHNN]`<SO_HIEU>`** . **[Điều 2]`<DIEU>`** . **[3 . Việc chuyển tiếp đối với **[quỹ tín dụng nhân dân]`<TO_CHUC_DOANH_NGHIEP>`** **[không đảm bảo các quy định về địa bàn hoạt động]`<HANH_VI_VI_PHAM>`** ; tỷ lệ vốn góp tối đa của một thành viên ; thành viên đăng ký thường trú ngoài địa bàn ; tổng mức nhận tiền gửi từ thành viên thực hiện **[theo quy định tại]`<TU_KHOA_PHAP_LY>`** **[các Điều 47 , 47a , 48 , 49 và 50 Thông tư này]`<THAM_CHIEU_PHAP_LY>`** .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[4:5]`)
- `[e1]` **06/2017/TT-NHNN** → `SO_HIEU` (span: `[6:7]`)
- `[e2]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_BAN_HANH` (span: `[0:3]`)
- `[e3]` **Điều 2** → `DIEU` (span: `[8:10]`)
- `[e4]` **3 . Việc chuyển tiếp đối với quỹ tín dụng nhân dân không đảm bảo các quy định về địa bàn hoạt động ; tỷ lệ vốn góp tối đa của một thành viên ; thành viên đăng ký thường trú ngoài địa bàn ; tổng mức nhận tiền gửi từ thành viên thực hiện theo quy định tại các Điều 47 , 47a , 48 , 49 và 50 Thông tư này .** → `KHOAN` (span: `[11:66]`)
- `[e5]` **không đảm bảo các quy định về địa bàn hoạt động** → `HANH_VI_VI_PHAM` (span: `[19:26]`) *(lồng trong `e4` (`KHOAN`))*
- `[e6]` **các Điều 47 , 47a , 48 , 49 và 50 Thông tư này** → `THAM_CHIEU_PHAP_LY` (span: `[52:65]`) *(lồng trong `e4` (`KHOAN`))*
- `[e7]` **theo quy định tại** → `TU_KHOA_PHAP_LY` (span: `[49:52]`) *(lồng trong `e4` (`KHOAN`))*
- `[e8]` **quỹ tín dụng nhân dân** → `TO_CHUC_DOANH_NGHIEP` (span: `[16:19]`) *(lồng trong `e4` (`KHOAN`))*

**Quan hệ:**
- (`e1` 06/2017/TT-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Ngân hàng Nhà nước Việt Nam `[CO_QUAN_BAN_HANH]`)
- (`e1` 06/2017/TT-NHNN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 2 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 06/2017/TT-NHNN `[SO_HIEU]`)
- (`e4` 3 . Việc chuyển tiếp đối với quỹ tín dụng nhân dân không đảm bảo các quy định về địa bàn hoạt động ; tỷ lệ vốn góp tối đa của một thành viên ; thành viên đăng ký thường trú ngoài địa bàn ; tổng mức nhận tiền gửi từ thành viên thực hiện theo quy định tại các Điều 47 , 47a , 48 , 49 và 50 Thông tư này . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 2 `[DIEU]`)
- (`e8` quỹ tín dụng nhân dân `[TO_CHUC_DOANH_NGHIEP]`) ==[ **THUC_HIEN_VI_PHAM** ]==> (`e5` không đảm bảo các quy định về địa bàn hoạt động `[HANH_VI_VI_PHAM]`)
- (`e7` theo quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e6` các Điều 47 , 47a , 48 , 49 và 50 Thông tư này `[THAM_CHIEU_PHAP_LY]`)
- (`e5` không đảm bảo các quy định về địa bàn hoạt động `[HANH_VI_VI_PHAM]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e6` các Điều 47 , 47a , 48 , 49 và 50 Thông tư này `[THAM_CHIEU_PHAP_LY]`)


---

### Mẫu #06_2017_TT-NHNN_122819#body_standalone_103 (Loại: `body_standalone`)
> **[Điều 2]`<DIEU>`** . **[3 . Việc chuyển tiếp đối với **[quỹ tín dụng nhân dân]`<TO_CHUC_DOANH_NGHIEP>`** **[không đảm bảo các quy định về địa bàn hoạt động]`<HANH_VI_VI_PHAM>`** ; tỷ lệ vốn góp tối đa của một thành viên ; thành viên đăng ký thường trú ngoài địa bàn ; tổng mức nhận tiền gửi từ thành viên thực hiện **[theo quy định tại]`<TU_KHOA_PHAP_LY>`** **[các Điều 47 , 47a , 48 , 49 và 50 Thông tư này]`<THAM_CHIEU_PHAP_LY>`** .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 2** → `DIEU` (span: `[0:2]`)
- `[e1]` **3 . Việc chuyển tiếp đối với quỹ tín dụng nhân dân không đảm bảo các quy định về địa bàn hoạt động ; tỷ lệ vốn góp tối đa của một thành viên ; thành viên đăng ký thường trú ngoài địa bàn ; tổng mức nhận tiền gửi từ thành viên thực hiện theo quy định tại các Điều 47 , 47a , 48 , 49 và 50 Thông tư này .** → `KHOAN` (span: `[3:58]`)
- `[e2]` **không đảm bảo các quy định về địa bàn hoạt động** → `HANH_VI_VI_PHAM` (span: `[11:18]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **các Điều 47 , 47a , 48 , 49 và 50 Thông tư này** → `THAM_CHIEU_PHAP_LY` (span: `[44:57]`) *(lồng trong `e1` (`KHOAN`))*
- `[e4]` **theo quy định tại** → `TU_KHOA_PHAP_LY` (span: `[41:44]`) *(lồng trong `e1` (`KHOAN`))*
- `[e5]` **quỹ tín dụng nhân dân** → `TO_CHUC_DOANH_NGHIEP` (span: `[8:11]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 3 . Việc chuyển tiếp đối với quỹ tín dụng nhân dân không đảm bảo các quy định về địa bàn hoạt động ; tỷ lệ vốn góp tối đa của một thành viên ; thành viên đăng ký thường trú ngoài địa bàn ; tổng mức nhận tiền gửi từ thành viên thực hiện theo quy định tại các Điều 47 , 47a , 48 , 49 và 50 Thông tư này . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 2 `[DIEU]`)
- (`e5` quỹ tín dụng nhân dân `[TO_CHUC_DOANH_NGHIEP]`) ==[ **THUC_HIEN_VI_PHAM** ]==> (`e2` không đảm bảo các quy định về địa bàn hoạt động `[HANH_VI_VI_PHAM]`)
- (`e4` theo quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` các Điều 47 , 47a , 48 , 49 và 50 Thông tư này `[THAM_CHIEU_PHAP_LY]`)
- (`e2` không đảm bảo các quy định về địa bàn hoạt động `[HANH_VI_VI_PHAM]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` các Điều 47 , 47a , 48 , 49 và 50 Thông tư này `[THAM_CHIEU_PHAP_LY]`)


---

### Mẫu #06_2017_TT-NHNN_122819#body_context_104 (Loại: `body_context`)
> **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[06/2017/TT-NHNN]`<SO_HIEU>`** . **[Điều 2]`<DIEU>`** . **[1 . Tại thời điểm Thông tư này có hiệu lực thi hành , **[quỹ tín dụng nhân dân]`<TO_CHUC_DOANH_NGHIEP>`** chưa đảm bảo các quy định về địa bàn hoạt động , tỷ lệ góp vốn của một thành viên , thành viên đăng ký thường trú ngoài địa bàn , tổng mức nhận tiền gửi từ thành viên tại Thông tư này phải xây dựng các **[phương án xử lý]`<GIAY_TO_HO_SO>`** và chủ động tổ chức thực hiện các biện pháp xử lý để tuân thủ đúng quy định ” .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[4:5]`)
- `[e1]` **06/2017/TT-NHNN** → `SO_HIEU` (span: `[6:7]`)
- `[e2]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_BAN_HANH` (span: `[0:3]`)
- `[e3]` **Điều 2** → `DIEU` (span: `[8:10]`)
- `[e4]` **1 . Tại thời điểm Thông tư này có hiệu lực thi hành , quỹ tín dụng nhân dân chưa đảm bảo các quy định về địa bàn hoạt động , tỷ lệ góp vốn của một thành viên , thành viên đăng ký thường trú ngoài địa bàn , tổng mức nhận tiền gửi từ thành viên tại Thông tư này phải xây dựng các phương án xử lý và chủ động tổ chức thực hiện các biện pháp xử lý để tuân thủ đúng quy định ” .** → `KHOAN` (span: `[11:73]`)
- `[e5]` **phương án xử lý** → `GIAY_TO_HO_SO` (span: `[58:60]`) *(lồng trong `e4` (`KHOAN`))*
- `[e6]` **quỹ tín dụng nhân dân** → `TO_CHUC_DOANH_NGHIEP` (span: `[21:24]`) *(lồng trong `e4` (`KHOAN`))*

**Quan hệ:**
- (`e1` 06/2017/TT-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Ngân hàng Nhà nước Việt Nam `[CO_QUAN_BAN_HANH]`)
- (`e1` 06/2017/TT-NHNN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 2 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 06/2017/TT-NHNN `[SO_HIEU]`)
- (`e4` 1 . Tại thời điểm Thông tư này có hiệu lực thi hành , quỹ tín dụng nhân dân chưa đảm bảo các quy định về địa bàn hoạt động , tỷ lệ góp vốn của một thành viên , thành viên đăng ký thường trú ngoài địa bàn , tổng mức nhận tiền gửi từ thành viên tại Thông tư này phải xây dựng các phương án xử lý và chủ động tổ chức thực hiện các biện pháp xử lý để tuân thủ đúng quy định ” . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 2 `[DIEU]`)


---

### Mẫu #06_2017_TT-NHNN_122819#body_standalone_105 (Loại: `body_standalone`)
> **[Điều 2]`<DIEU>`** . **[1 . Tại thời điểm Thông tư này có hiệu lực thi hành , **[quỹ tín dụng nhân dân]`<TO_CHUC_DOANH_NGHIEP>`** chưa đảm bảo các quy định về địa bàn hoạt động , tỷ lệ góp vốn của một thành viên , thành viên đăng ký thường trú ngoài địa bàn , tổng mức nhận tiền gửi từ thành viên tại Thông tư này phải xây dựng các **[phương án xử lý]`<GIAY_TO_HO_SO>`** và chủ động tổ chức thực hiện các biện pháp xử lý để tuân thủ đúng quy định ” .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 2** → `DIEU` (span: `[0:2]`)
- `[e1]` **1 . Tại thời điểm Thông tư này có hiệu lực thi hành , quỹ tín dụng nhân dân chưa đảm bảo các quy định về địa bàn hoạt động , tỷ lệ góp vốn của một thành viên , thành viên đăng ký thường trú ngoài địa bàn , tổng mức nhận tiền gửi từ thành viên tại Thông tư này phải xây dựng các phương án xử lý và chủ động tổ chức thực hiện các biện pháp xử lý để tuân thủ đúng quy định ” .** → `KHOAN` (span: `[3:65]`)
- `[e2]` **phương án xử lý** → `GIAY_TO_HO_SO` (span: `[50:52]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **quỹ tín dụng nhân dân** → `TO_CHUC_DOANH_NGHIEP` (span: `[13:16]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 1 . Tại thời điểm Thông tư này có hiệu lực thi hành , quỹ tín dụng nhân dân chưa đảm bảo các quy định về địa bàn hoạt động , tỷ lệ góp vốn của một thành viên , thành viên đăng ký thường trú ngoài địa bàn , tổng mức nhận tiền gửi từ thành viên tại Thông tư này phải xây dựng các phương án xử lý và chủ động tổ chức thực hiện các biện pháp xử lý để tuân thủ đúng quy định ” . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 2 `[DIEU]`)


---

### Mẫu #06_2017_TT-NHNN_122819#body_context_106 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[06/2017/TT-NHNN]`<SO_HIEU>`** ban hành **[ngày 05 tháng 07 năm 2017]`<NGAY_BAN_HANH>`** bởi **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_BAN_HANH>`** . **[Điều 2]`<DIEU>`** . **[9 . **[Sửa đổi]`<TU_KHOA_PHAP_LY>`** **[Điều 52]`<THAM_CHIEU_PHAP_LY>`** như sau :]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **06/2017/TT-NHNN** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_BAN_HANH` (span: `[11:14]`)
- `[e3]` **ngày 05 tháng 07 năm 2017** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 2** → `DIEU` (span: `[15:17]`)
- `[e5]` **9 . Sửa đổi Điều 52 như sau :** → `KHOAN` (span: `[18:26]`)
- `[e6]` **Điều 52** → `THAM_CHIEU_PHAP_LY` (span: `[21:23]`) *(lồng trong `e5` (`KHOAN`))*
- `[e7]` **Sửa đổi** → `TU_KHOA_PHAP_LY` (span: `[20:21]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 06/2017/TT-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Ngân hàng Nhà nước Việt Nam `[CO_QUAN_BAN_HANH]`)
- (`e1` 06/2017/TT-NHNN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 06/2017/TT-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 05 tháng 07 năm 2017 `[NGAY_BAN_HANH]`)
- (`e4` Điều 2 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 06/2017/TT-NHNN `[SO_HIEU]`)
- (`e5` 9 . Sửa đổi Điều 52 như sau : `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 2 `[DIEU]`)
- (`e7` Sửa đổi `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e6` Điều 52 `[THAM_CHIEU_PHAP_LY]`)
- (`e5` 9 . Sửa đổi Điều 52 như sau : `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e6` Điều 52 `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #06_2017_TT-NHNN_122819#body_standalone_107 (Loại: `body_standalone`)
> **[Điều 2]`<DIEU>`** . **[9 . **[Sửa đổi]`<TU_KHOA_PHAP_LY>`** **[Điều 52]`<THAM_CHIEU_PHAP_LY>`** như sau :]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 2** → `DIEU` (span: `[0:2]`)
- `[e1]` **9 . Sửa đổi Điều 52 như sau :** → `KHOAN` (span: `[3:11]`)
- `[e2]` **Điều 52** → `THAM_CHIEU_PHAP_LY` (span: `[6:8]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **Sửa đổi** → `TU_KHOA_PHAP_LY` (span: `[5:6]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 9 . Sửa đổi Điều 52 như sau : `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 2 `[DIEU]`)
- (`e3` Sửa đổi `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e2` Điều 52 `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 9 . Sửa đổi Điều 52 như sau : `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e2` Điều 52 `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #06_2017_TT-NHNN_122819#body_context_108 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[06/2017/TT-NHNN]`<SO_HIEU>`** ban hành **[ngày 05 tháng 07 năm 2017]`<NGAY_BAN_HANH>`** bởi **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_BAN_HANH>`** . **[Điều 2]`<DIEU>`** . **[Khoản 2 . **[Ngân hàng Nhà nước chi nhánh tỉnh , thành phố trực thuộc Trung ương]`<CO_QUAN_THAM_QUYEN>`**]`<KHOAN>`** : **[( i ) Ủy ban nhân dân xã về việc thành lập **[quỹ tín dụng nhân dân]`<TO_CHUC_DOANH_NGHIEP>`** trên địa bàn , danh sách nhân sự dự kiến bầu , bổ nhiệm làm Chủ tịch và các thành viên khác của **[Hội đồng quản trị]`<TO_CHUC_DOANH_NGHIEP>`** , Trưởng ban và các thành viên khác của **[Ban kiểm soát]`<TO_CHUC_DOANH_NGHIEP>`** , **[Giám đốc]`<CHU_THE_CA_NHAN>`** **[quỹ tín dụng nhân dân]`<TO_CHUC_DOANH_NGHIEP>`** ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **06/2017/TT-NHNN** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_BAN_HANH` (span: `[11:14]`)
- `[e3]` **ngày 05 tháng 07 năm 2017** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 2** → `DIEU` (span: `[15:17]`)
- `[e5]` **Khoản 2 . Ngân hàng Nhà nước chi nhánh tỉnh , thành phố trực thuộc Trung ương** → `KHOAN` (span: `[18:29]`)
- `[e6]` **( i ) Ủy ban nhân dân xã về việc thành lập quỹ tín dụng nhân dân trên địa bàn , danh sách nhân sự dự kiến bầu , bổ nhiệm làm Chủ tịch và các thành viên khác của Hội đồng quản trị , Trưởng ban và các thành viên khác của Ban kiểm soát , Giám đốc quỹ tín dụng nhân dân ;** → `DIEM` (span: `[30:76]`)
- `[e7]` **Ngân hàng Nhà nước chi nhánh tỉnh , thành phố trực thuộc Trung ương** → `CO_QUAN_THAM_QUYEN` (span: `[21:29]`) *(lồng trong `e5` (`KHOAN`))*
- `[e8]` **quỹ tín dụng nhân dân** → `TO_CHUC_DOANH_NGHIEP` (span: `[39:42]`) *(lồng trong `e6` (`DIEM`))*
- `[e9]` **Hội đồng quản trị** → `TO_CHUC_DOANH_NGHIEP` (span: `[58:60]`) *(lồng trong `e6` (`DIEM`))*
- `[e10]` **Ban kiểm soát** → `TO_CHUC_DOANH_NGHIEP` (span: `[68:70]`) *(lồng trong `e6` (`DIEM`))*
- `[e11]` **quỹ tín dụng nhân dân** → `TO_CHUC_DOANH_NGHIEP` (span: `[72:75]`) *(lồng trong `e6` (`DIEM`))*
- `[e12]` **Giám đốc** → `CHU_THE_CA_NHAN` (span: `[71:72]`) *(lồng trong `e6` (`DIEM`))*

**Quan hệ:**
- (`e1` 06/2017/TT-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Ngân hàng Nhà nước Việt Nam `[CO_QUAN_BAN_HANH]`)
- (`e1` 06/2017/TT-NHNN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 06/2017/TT-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 05 tháng 07 năm 2017 `[NGAY_BAN_HANH]`)
- (`e4` Điều 2 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 06/2017/TT-NHNN `[SO_HIEU]`)
- (`e5` Khoản 2 . Ngân hàng Nhà nước chi nhánh tỉnh , thành phố trực thuộc Trung ương `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 2 `[DIEU]`)
- (`e6` ( i ) Ủy ban nhân dân xã về việc thành lập quỹ tín dụng nhân dân trên địa bàn , danh sách nhân sự dự kiến bầu , bổ nhiệm làm Chủ tịch và các thành viên khác của Hội đồng quản trị , Trưởng ban và các thành viên khác của Ban kiểm soát , Giám đốc quỹ tín dụng nhân dân ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e5` Khoản 2 . Ngân hàng Nhà nước chi nhánh tỉnh , thành phố trực thuộc Trung ương `[KHOAN]`)


---

### Mẫu #06_2017_TT-NHNN_122819#body_standalone_109 (Loại: `body_standalone`)
> **[Điều 2]`<DIEU>`** . **[Khoản 2 . **[Ngân hàng Nhà nước chi nhánh tỉnh , thành phố trực thuộc Trung ương]`<CO_QUAN_THAM_QUYEN>`**]`<KHOAN>`** : **[( i ) Ủy ban nhân dân xã về việc thành lập **[quỹ tín dụng nhân dân]`<TO_CHUC_DOANH_NGHIEP>`** trên địa bàn , danh sách nhân sự dự kiến bầu , bổ nhiệm làm Chủ tịch và các thành viên khác của **[Hội đồng quản trị]`<TO_CHUC_DOANH_NGHIEP>`** , Trưởng ban và các thành viên khác của **[Ban kiểm soát]`<TO_CHUC_DOANH_NGHIEP>`** , **[Giám đốc]`<CHU_THE_CA_NHAN>`** **[quỹ tín dụng nhân dân]`<TO_CHUC_DOANH_NGHIEP>`** ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Điều 2** → `DIEU` (span: `[0:2]`)
- `[e1]` **Khoản 2 . Ngân hàng Nhà nước chi nhánh tỉnh , thành phố trực thuộc Trung ương** → `KHOAN` (span: `[3:14]`)
- `[e2]` **( i ) Ủy ban nhân dân xã về việc thành lập quỹ tín dụng nhân dân trên địa bàn , danh sách nhân sự dự kiến bầu , bổ nhiệm làm Chủ tịch và các thành viên khác của Hội đồng quản trị , Trưởng ban và các thành viên khác của Ban kiểm soát , Giám đốc quỹ tín dụng nhân dân ;** → `DIEM` (span: `[15:61]`)
- `[e3]` **Ngân hàng Nhà nước chi nhánh tỉnh , thành phố trực thuộc Trung ương** → `CO_QUAN_THAM_QUYEN` (span: `[6:14]`) *(lồng trong `e1` (`KHOAN`))*
- `[e4]` **quỹ tín dụng nhân dân** → `TO_CHUC_DOANH_NGHIEP` (span: `[24:27]`) *(lồng trong `e2` (`DIEM`))*
- `[e5]` **Hội đồng quản trị** → `TO_CHUC_DOANH_NGHIEP` (span: `[43:45]`) *(lồng trong `e2` (`DIEM`))*
- `[e6]` **Ban kiểm soát** → `TO_CHUC_DOANH_NGHIEP` (span: `[53:55]`) *(lồng trong `e2` (`DIEM`))*
- `[e7]` **quỹ tín dụng nhân dân** → `TO_CHUC_DOANH_NGHIEP` (span: `[57:60]`) *(lồng trong `e2` (`DIEM`))*
- `[e8]` **Giám đốc** → `CHU_THE_CA_NHAN` (span: `[56:57]`) *(lồng trong `e2` (`DIEM`))*

**Quan hệ:**
- (`e1` Khoản 2 . Ngân hàng Nhà nước chi nhánh tỉnh , thành phố trực thuộc Trung ương `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 2 `[DIEU]`)
- (`e2` ( i ) Ủy ban nhân dân xã về việc thành lập quỹ tín dụng nhân dân trên địa bàn , danh sách nhân sự dự kiến bầu , bổ nhiệm làm Chủ tịch và các thành viên khác của Hội đồng quản trị , Trưởng ban và các thành viên khác của Ban kiểm soát , Giám đốc quỹ tín dụng nhân dân ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e1` Khoản 2 . Ngân hàng Nhà nước chi nhánh tỉnh , thành phố trực thuộc Trung ương `[KHOAN]`)


---

### Mẫu #06_2017_TT-NHNN_122819#body_context_110 (Loại: `body_context`)
> **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[06/2017/TT-NHNN]`<SO_HIEU>`** . **[Điều 2]`<DIEU>`** . **[3 . **[Ngân hàng Hợp tác xã Việt Nam]`<TO_CHUC_DOANH_NGHIEP>`** :]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[4:5]`)
- `[e1]` **06/2017/TT-NHNN** → `SO_HIEU` (span: `[6:7]`)
- `[e2]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_BAN_HANH` (span: `[0:3]`)
- `[e3]` **Điều 2** → `DIEU` (span: `[8:10]`)
- `[e4]` **3 . Ngân hàng Hợp tác xã Việt Nam :** → `KHOAN` (span: `[11:17]`)
- `[e5]` **Ngân hàng Hợp tác xã Việt Nam** → `TO_CHUC_DOANH_NGHIEP` (span: `[13:16]`) *(lồng trong `e4` (`KHOAN`))*

**Quan hệ:**
- (`e1` 06/2017/TT-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Ngân hàng Nhà nước Việt Nam `[CO_QUAN_BAN_HANH]`)
- (`e1` 06/2017/TT-NHNN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 2 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 06/2017/TT-NHNN `[SO_HIEU]`)
- (`e4` 3 . Ngân hàng Hợp tác xã Việt Nam : `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 2 `[DIEU]`)


---
