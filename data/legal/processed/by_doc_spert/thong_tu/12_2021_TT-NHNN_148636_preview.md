# Dữ liệu gán nhãn văn bản: 12_2021_TT-NHNN_148636
- **Thể loại**: `thong_tu`
- **Phân vùng dữ liệu**: `TRAIN`
- **Tổng số mẫu**: 87 mẫu
- **Tổng số thực thể**: 589
- **Tổng số quan hệ**: 352

---

### Mẫu #12_2021_TT-NHNN_148636#header_0 (Loại: `header`)
> NGÂN HÀNG NHÀ NƯỚC . VIỆT NAM . Số : **[12 / 2021/TT-NHNN]`<SO_HIEU>`** . CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM . Độc lập - Tự do - Hạnh phúc . Hà Nội , **[ngày 30 tháng 7 năm 2021]`<NGAY_BAN_HANH>`** . **[THÔNG TƯ]`<LOAI_VAN_BAN>`**

**Thực thể:**
- `[e0]` **12 / 2021/TT-NHNN** → `SO_HIEU` (span: `[8:11]`)
- `[e1]` **ngày 30 tháng 7 năm 2021** → `NGAY_BAN_HANH` (span: `[27:33]`)
- `[e2]` **THÔNG TƯ** → `LOAI_VAN_BAN` (span: `[34:35]`)

**Quan hệ:**
- (`e0` 12 / 2021/TT-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e1` ngày 30 tháng 7 năm 2021 `[NGAY_BAN_HANH]`)
- (`e0` 12 / 2021/TT-NHNN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e2` THÔNG TƯ `[LOAI_VAN_BAN]`)


---

### Mẫu #12_2021_TT-NHNN_148636#signature_1 (Loại: `signature`)
> **[THỐNG ĐỐC]`<CHUC_DANH_NGUOI_KY>`** . ( Đã ký ) . **[Nguyễn Thị Hồng]`<NGUOI_KY>`**

**Thực thể:**
- `[e0]` **Nguyễn Thị Hồng** → `NGUOI_KY` (span: `[7:8]`)
- `[e1]` **THỐNG ĐỐC** → `CHUC_DANH_NGUOI_KY` (span: `[0:1]`)

**Quan hệ:**
- (`e0` Nguyễn Thị Hồng `[NGUOI_KY]`) ==[ **GIU_CHUC_VU** ]==> (`e1` THỐNG ĐỐC `[CHUC_DANH_NGUOI_KY]`)


---

### Mẫu #12_2021_TT-NHNN_148636#meta_2 (Loại: `meta`)
> NGÂN HÀNG NHÀ NƯỚC . VIỆT NAM . Số : **[12 / 2021/TT-NHNN]`<SO_HIEU>`** . CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM . Độc lập - Tự do - Hạnh phúc . Hà Nội , ngày 30 tháng 7 năm 2021 . **[THỐNG ĐỐC]`<CHUC_DANH_NGUOI_KY>`** . ( Đã ký ) . **[Nguyễn Thị Hồng]`<NGUOI_KY>`**

**Thực thể:**
- `[e0]` **12 / 2021/TT-NHNN** → `SO_HIEU` (span: `[8:11]`)
- `[e1]` **Nguyễn Thị Hồng** → `NGUOI_KY` (span: `[41:42]`)
- `[e2]` **THỐNG ĐỐC** → `CHUC_DANH_NGUOI_KY` (span: `[34:35]`)

**Quan hệ:**
- (`e0` 12 / 2021/TT-NHNN `[SO_HIEU]`) ==[ **KY_BOI** ]==> (`e1` Nguyễn Thị Hồng `[NGUOI_KY]`)
- (`e1` Nguyễn Thị Hồng `[NGUOI_KY]`) ==[ **GIU_CHUC_VU** ]==> (`e2` THỐNG ĐỐC `[CHUC_DANH_NGUOI_KY]`)


---

### Mẫu #12_2021_TT-NHNN_148636#preamble_context_3 (Loại: `preamble_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[12/2021/TT-NHNN]`<SO_HIEU>`** của **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_BAN_HANH>`** . Quy định về việc **[tổ chức tín dụng , chi nhánh ngân hàng nước ngoài]`<TO_CHUC_DOANH_NGHIEP>`** mua ,

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **12/2021/TT-NHNN** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_BAN_HANH` (span: `[4:7]`)
- `[e3]` **tổ chức tín dụng , chi nhánh ngân hàng nước ngoài** → `TO_CHUC_DOANH_NGHIEP` (span: `[11:17]`)

**Quan hệ:**
- (`e1` 12/2021/TT-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Ngân hàng Nhà nước Việt Nam `[CO_QUAN_BAN_HANH]`)
- (`e1` 12/2021/TT-NHNN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)


---

### Mẫu #12_2021_TT-NHNN_148636#preamble_standalone_4 (Loại: `preamble_standalone`)
> Quy định về việc **[tổ chức tín dụng , chi nhánh ngân hàng nước ngoài]`<TO_CHUC_DOANH_NGHIEP>`** mua ,

**Thực thể:**
- `[e0]` **tổ chức tín dụng , chi nhánh ngân hàng nước ngoài** → `TO_CHUC_DOANH_NGHIEP` (span: `[3:9]`)


---

### Mẫu #12_2021_TT-NHNN_148636#preamble_context_5 (Loại: `preamble_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[12/2021/TT-NHNN]`<SO_HIEU>`** của **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_BAN_HANH>`** . bán kỳ phiếu , tín phiếu , **[chứng chỉ tiền gửi]`<GIAY_TO_HO_SO>`** , **[trái phiếu]`<TAI_SAN_VAT_CHAT>`** do **[tổ chức tín dụng]`<TO_CHUC_DOANH_NGHIEP>`** ,

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **12/2021/TT-NHNN** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_BAN_HANH` (span: `[4:7]`)
- `[e3]` **chứng chỉ tiền gửi** → `GIAY_TO_HO_SO` (span: `[13:16]`)
- `[e4]` **tổ chức tín dụng** → `TO_CHUC_DOANH_NGHIEP` (span: `[19:21]`)
- `[e5]` **trái phiếu** → `TAI_SAN_VAT_CHAT` (span: `[17:18]`)

**Quan hệ:**
- (`e1` 12/2021/TT-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Ngân hàng Nhà nước Việt Nam `[CO_QUAN_BAN_HANH]`)
- (`e1` 12/2021/TT-NHNN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)


---

### Mẫu #12_2021_TT-NHNN_148636#preamble_standalone_6 (Loại: `preamble_standalone`)
> bán kỳ phiếu , tín phiếu , **[chứng chỉ tiền gửi]`<GIAY_TO_HO_SO>`** , **[trái phiếu]`<TAI_SAN_VAT_CHAT>`** do **[tổ chức tín dụng]`<TO_CHUC_DOANH_NGHIEP>`** ,

**Thực thể:**
- `[e0]` **chứng chỉ tiền gửi** → `GIAY_TO_HO_SO` (span: `[5:8]`)
- `[e1]` **tổ chức tín dụng** → `TO_CHUC_DOANH_NGHIEP` (span: `[11:13]`)
- `[e2]` **trái phiếu** → `TAI_SAN_VAT_CHAT` (span: `[9:10]`)


---

### Mẫu #12_2021_TT-NHNN_148636#preamble_context_7 (Loại: `preamble_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[12/2021/TT-NHNN]`<SO_HIEU>`** của **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_BAN_HANH>`** . **[chi nhánh ngân hàng nước ngoài khác phát hành trong nước]`<TO_CHUC_DOANH_NGHIEP>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **12/2021/TT-NHNN** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_BAN_HANH` (span: `[4:7]`)
- `[e3]` **chi nhánh ngân hàng nước ngoài khác phát hành trong nước** → `TO_CHUC_DOANH_NGHIEP` (span: `[8:15]`)

**Quan hệ:**
- (`e1` 12/2021/TT-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Ngân hàng Nhà nước Việt Nam `[CO_QUAN_BAN_HANH]`)
- (`e1` 12/2021/TT-NHNN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)


---

### Mẫu #12_2021_TT-NHNN_148636#preamble_standalone_8 (Loại: `preamble_standalone`)
> **[chi nhánh ngân hàng nước ngoài khác phát hành trong nước]`<TO_CHUC_DOANH_NGHIEP>`**

**Thực thể:**
- `[e0]` **chi nhánh ngân hàng nước ngoài khác phát hành trong nước** → `TO_CHUC_DOANH_NGHIEP` (span: `[0:7]`)


---

### Mẫu #12_2021_TT-NHNN_148636#preamble_context_9 (Loại: `preamble_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[12/2021/TT-NHNN]`<SO_HIEU>`** của **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_BAN_HANH>`** . **[Căn cứ]`<TU_KHOA_PHAP_LY>`** **[Luật Ngân hàng Nhà nước Việt Nam]`<THAM_CHIEU_PHAP_LY>`** **[ngày 16 tháng 6 năm 2010]`<NGAY_THAM_CHIEU>`** ;

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **12/2021/TT-NHNN** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_BAN_HANH` (span: `[4:7]`)
- `[e3]` **Luật Ngân hàng Nhà nước Việt Nam** → `THAM_CHIEU_PHAP_LY` (span: `[9:13]`)
- `[e4]` **Căn cứ** → `TU_KHOA_PHAP_LY` (span: `[8:9]`)
- `[e5]` **ngày 16 tháng 6 năm 2010** → `NGAY_THAM_CHIEU` (span: `[13:19]`)

**Quan hệ:**
- (`e1` 12/2021/TT-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Ngân hàng Nhà nước Việt Nam `[CO_QUAN_BAN_HANH]`)
- (`e1` 12/2021/TT-NHNN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e4` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Luật Ngân hàng Nhà nước Việt Nam `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 12/2021/TT-NHNN `[SO_HIEU]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Luật Ngân hàng Nhà nước Việt Nam `[THAM_CHIEU_PHAP_LY]`)
- (`e3` Luật Ngân hàng Nhà nước Việt Nam `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e5` ngày 16 tháng 6 năm 2010 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #12_2021_TT-NHNN_148636#preamble_standalone_10 (Loại: `preamble_standalone`)
> **[Căn cứ]`<TU_KHOA_PHAP_LY>`** **[Luật Ngân hàng Nhà nước Việt Nam]`<THAM_CHIEU_PHAP_LY>`** **[ngày 16 tháng 6 năm 2010]`<NGAY_THAM_CHIEU>`** ;

**Thực thể:**
- `[e0]` **Luật Ngân hàng Nhà nước Việt Nam** → `THAM_CHIEU_PHAP_LY` (span: `[1:5]`)
- `[e1]` **Căn cứ** → `TU_KHOA_PHAP_LY` (span: `[0:1]`)
- `[e2]` **ngày 16 tháng 6 năm 2010** → `NGAY_THAM_CHIEU` (span: `[5:11]`)

**Quan hệ:**
- (`e1` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e0` Luật Ngân hàng Nhà nước Việt Nam `[THAM_CHIEU_PHAP_LY]`)
- (`e0` Luật Ngân hàng Nhà nước Việt Nam `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e2` ngày 16 tháng 6 năm 2010 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #12_2021_TT-NHNN_148636#preamble_context_11 (Loại: `preamble_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[12/2021/TT-NHNN]`<SO_HIEU>`** của **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_BAN_HANH>`** . **[Căn cứ]`<TU_KHOA_PHAP_LY>`** **[Luật Các tổ chức tín dụng]`<THAM_CHIEU_PHAP_LY>`** **[ngày 16 tháng 6 năm 2010]`<NGAY_THAM_CHIEU>`** và **[Luật sửa đổi , bổ sung một số điều của Luật Các tổ chức tín dụng]`<THAM_CHIEU_PHAP_LY>`** **[ngày 20 tháng 11 năm 2017]`<NGAY_THAM_CHIEU>`** ;

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **12/2021/TT-NHNN** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_BAN_HANH` (span: `[4:7]`)
- `[e3]` **Luật Các tổ chức tín dụng** → `THAM_CHIEU_PHAP_LY` (span: `[9:13]`)
- `[e4]` **Luật sửa đổi , bổ sung một số điều của Luật Các tổ chức tín dụng** → `THAM_CHIEU_PHAP_LY` (span: `[20:31]`)
- `[e5]` **Căn cứ** → `TU_KHOA_PHAP_LY` (span: `[8:9]`)
- `[e6]` **ngày 16 tháng 6 năm 2010** → `NGAY_THAM_CHIEU` (span: `[13:19]`)
- `[e7]` **ngày 20 tháng 11 năm 2017** → `NGAY_THAM_CHIEU` (span: `[31:37]`)

**Quan hệ:**
- (`e1` 12/2021/TT-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Ngân hàng Nhà nước Việt Nam `[CO_QUAN_BAN_HANH]`)
- (`e1` 12/2021/TT-NHNN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e5` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Luật Các tổ chức tín dụng `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 12/2021/TT-NHNN `[SO_HIEU]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Luật Các tổ chức tín dụng `[THAM_CHIEU_PHAP_LY]`)
- (`e5` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e4` Luật sửa đổi , bổ sung một số điều của Luật Các tổ chức tín dụng `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 12/2021/TT-NHNN `[SO_HIEU]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e4` Luật sửa đổi , bổ sung một số điều của Luật Các tổ chức tín dụng `[THAM_CHIEU_PHAP_LY]`)
- (`e3` Luật Các tổ chức tín dụng `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e6` ngày 16 tháng 6 năm 2010 `[NGAY_THAM_CHIEU]`)
- (`e4` Luật sửa đổi , bổ sung một số điều của Luật Các tổ chức tín dụng `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e7` ngày 20 tháng 11 năm 2017 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #12_2021_TT-NHNN_148636#preamble_standalone_12 (Loại: `preamble_standalone`)
> **[Căn cứ]`<TU_KHOA_PHAP_LY>`** **[Luật Các tổ chức tín dụng]`<THAM_CHIEU_PHAP_LY>`** **[ngày 16 tháng 6 năm 2010]`<NGAY_THAM_CHIEU>`** và **[Luật sửa đổi , bổ sung một số điều của Luật Các tổ chức tín dụng]`<THAM_CHIEU_PHAP_LY>`** **[ngày 20 tháng 11 năm 2017]`<NGAY_THAM_CHIEU>`** ;

**Thực thể:**
- `[e0]` **Luật Các tổ chức tín dụng** → `THAM_CHIEU_PHAP_LY` (span: `[1:5]`)
- `[e1]` **Luật sửa đổi , bổ sung một số điều của Luật Các tổ chức tín dụng** → `THAM_CHIEU_PHAP_LY` (span: `[12:23]`)
- `[e2]` **Căn cứ** → `TU_KHOA_PHAP_LY` (span: `[0:1]`)
- `[e3]` **ngày 16 tháng 6 năm 2010** → `NGAY_THAM_CHIEU` (span: `[5:11]`)
- `[e4]` **ngày 20 tháng 11 năm 2017** → `NGAY_THAM_CHIEU` (span: `[23:29]`)

**Quan hệ:**
- (`e2` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e0` Luật Các tổ chức tín dụng `[THAM_CHIEU_PHAP_LY]`)
- (`e2` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e1` Luật sửa đổi , bổ sung một số điều của Luật Các tổ chức tín dụng `[THAM_CHIEU_PHAP_LY]`)
- (`e0` Luật Các tổ chức tín dụng `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e3` ngày 16 tháng 6 năm 2010 `[NGAY_THAM_CHIEU]`)
- (`e1` Luật sửa đổi , bổ sung một số điều của Luật Các tổ chức tín dụng `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e4` ngày 20 tháng 11 năm 2017 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #12_2021_TT-NHNN_148636#preamble_context_13 (Loại: `preamble_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[12/2021/TT-NHNN]`<SO_HIEU>`** của **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_BAN_HANH>`** . **[Căn cứ]`<TU_KHOA_PHAP_LY>`** **[Luật Chứng khoán]`<THAM_CHIEU_PHAP_LY>`** **[ngày 26 tháng 11 năm 2019]`<NGAY_THAM_CHIEU>`** ;

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **12/2021/TT-NHNN** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_BAN_HANH` (span: `[4:7]`)
- `[e3]` **Luật Chứng khoán** → `THAM_CHIEU_PHAP_LY` (span: `[9:10]`)
- `[e4]` **Căn cứ** → `TU_KHOA_PHAP_LY` (span: `[8:9]`)
- `[e5]` **ngày 26 tháng 11 năm 2019** → `NGAY_THAM_CHIEU` (span: `[10:16]`)

**Quan hệ:**
- (`e1` 12/2021/TT-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Ngân hàng Nhà nước Việt Nam `[CO_QUAN_BAN_HANH]`)
- (`e1` 12/2021/TT-NHNN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e4` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Luật Chứng khoán `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 12/2021/TT-NHNN `[SO_HIEU]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Luật Chứng khoán `[THAM_CHIEU_PHAP_LY]`)
- (`e3` Luật Chứng khoán `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e5` ngày 26 tháng 11 năm 2019 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #12_2021_TT-NHNN_148636#preamble_standalone_14 (Loại: `preamble_standalone`)
> **[Căn cứ]`<TU_KHOA_PHAP_LY>`** **[Luật Chứng khoán]`<THAM_CHIEU_PHAP_LY>`** **[ngày 26 tháng 11 năm 2019]`<NGAY_THAM_CHIEU>`** ;

**Thực thể:**
- `[e0]` **Luật Chứng khoán** → `THAM_CHIEU_PHAP_LY` (span: `[1:2]`)
- `[e1]` **Căn cứ** → `TU_KHOA_PHAP_LY` (span: `[0:1]`)
- `[e2]` **ngày 26 tháng 11 năm 2019** → `NGAY_THAM_CHIEU` (span: `[2:8]`)

**Quan hệ:**
- (`e1` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e0` Luật Chứng khoán `[THAM_CHIEU_PHAP_LY]`)
- (`e0` Luật Chứng khoán `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e2` ngày 26 tháng 11 năm 2019 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #12_2021_TT-NHNN_148636#preamble_context_15 (Loại: `preamble_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[12/2021/TT-NHNN]`<SO_HIEU>`** của **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_BAN_HANH>`** . **[Căn cứ]`<TU_KHOA_PHAP_LY>`** **[Nghị định số 16/2017/NĐ-CP]`<THAM_CHIEU_PHAP_LY>`** **[ngày 17 tháng 02 năm 2017]`<NGAY_THAM_CHIEU>`** quy định chức năng , nhiệm vụ , quyền hạn và cơ cấu tổ chức của **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_THAM_QUYEN>`** ;

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **12/2021/TT-NHNN** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_BAN_HANH` (span: `[4:7]`)
- `[e3]` **Nghị định số 16/2017/NĐ-CP** → `THAM_CHIEU_PHAP_LY` (span: `[9:12]`)
- `[e4]` **Căn cứ** → `TU_KHOA_PHAP_LY` (span: `[8:9]`)
- `[e5]` **ngày 17 tháng 02 năm 2017** → `NGAY_THAM_CHIEU` (span: `[12:18]`)
- `[e6]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_THAM_QUYEN` (span: `[28:31]`)

**Quan hệ:**
- (`e1` 12/2021/TT-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Ngân hàng Nhà nước Việt Nam `[CO_QUAN_BAN_HANH]`)
- (`e1` 12/2021/TT-NHNN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e4` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Nghị định số 16/2017/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 12/2021/TT-NHNN `[SO_HIEU]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Nghị định số 16/2017/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e3` Nghị định số 16/2017/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e5` ngày 17 tháng 02 năm 2017 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #12_2021_TT-NHNN_148636#preamble_standalone_16 (Loại: `preamble_standalone`)
> **[Căn cứ]`<TU_KHOA_PHAP_LY>`** **[Nghị định số 16/2017/NĐ-CP]`<THAM_CHIEU_PHAP_LY>`** **[ngày 17 tháng 02 năm 2017]`<NGAY_THAM_CHIEU>`** quy định chức năng , nhiệm vụ , quyền hạn và cơ cấu tổ chức của **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_THAM_QUYEN>`** ;

**Thực thể:**
- `[e0]` **Nghị định số 16/2017/NĐ-CP** → `THAM_CHIEU_PHAP_LY` (span: `[1:4]`)
- `[e1]` **Căn cứ** → `TU_KHOA_PHAP_LY` (span: `[0:1]`)
- `[e2]` **ngày 17 tháng 02 năm 2017** → `NGAY_THAM_CHIEU` (span: `[4:10]`)
- `[e3]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_THAM_QUYEN` (span: `[20:23]`)

**Quan hệ:**
- (`e1` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e0` Nghị định số 16/2017/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e3` Ngân hàng Nhà nước Việt Nam `[CO_QUAN_THAM_QUYEN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e0` Nghị định số 16/2017/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e0` Nghị định số 16/2017/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e2` ngày 17 tháng 02 năm 2017 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #12_2021_TT-NHNN_148636#body_context_17 (Loại: `body_context`)
> **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[12/2021/TT-NHNN]`<SO_HIEU>`** . **[Điều 1 . Phạm vi điều chỉnh]`<DIEU>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[4:5]`)
- `[e1]` **12/2021/TT-NHNN** → `SO_HIEU` (span: `[6:7]`)
- `[e2]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_BAN_HANH` (span: `[0:3]`)
- `[e3]` **Điều 1 . Phạm vi điều chỉnh** → `DIEU` (span: `[8:13]`)

**Quan hệ:**
- (`e1` 12/2021/TT-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Ngân hàng Nhà nước Việt Nam `[CO_QUAN_BAN_HANH]`)
- (`e1` 12/2021/TT-NHNN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 1 . Phạm vi điều chỉnh `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 12/2021/TT-NHNN `[SO_HIEU]`)


---

### Mẫu #12_2021_TT-NHNN_148636#body_context_18 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[12/2021/TT-NHNN]`<SO_HIEU>`** của **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Chính sách tiền tệ]`<LINH_VUC>`** . **[Điều 1]`<DIEU>`** . **[1 . Thông tư này quy định về việc **[tổ chức tín dụng , chi nhánh ngân hàng nước ngoài]`<TO_CHUC_DOANH_NGHIEP>`** mua , bán kỳ phiếu , tín phiếu , **[chứng chỉ tiền gửi]`<GIAY_TO_HO_SO>`** , **[trái phiếu]`<TAI_SAN_VAT_CHAT>`** do **[tổ chức tín dụng]`<TO_CHUC_DOANH_NGHIEP>`** , **[chi nhánh ngân hàng nước ngoài khác phát hành trong nước]`<TO_CHUC_DOANH_NGHIEP>`** ( sau đây gọi là **[giấy tờ có giá]`<TO_CHUC_DOANH_NGHIEP>`** ) chưa đến hạn thanh toán mà bên mua nhận chuyển giao quyền sở hữu và không kèm theo cam kết bán , mua lại **[giấy tờ có giá]`<TO_CHUC_DOANH_NGHIEP>`** hoặc bảo lưu quyền truy đòi ( sau đây gọi là mua ,]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **12/2021/TT-NHNN** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_BAN_HANH` (span: `[4:7]`)
- `[e3]` **Chính sách tiền tệ** → `LINH_VUC` (span: `[9:11]`)
- `[e4]` **Điều 1** → `DIEU` (span: `[12:14]`)
- `[e5]` **1 . Thông tư này quy định về việc tổ chức tín dụng , chi nhánh ngân hàng nước ngoài mua , bán kỳ phiếu , tín phiếu , chứng chỉ tiền gửi , trái phiếu do tổ chức tín dụng , chi nhánh ngân hàng nước ngoài khác phát hành trong nước ( sau đây gọi là giấy tờ có giá ) chưa đến hạn thanh toán mà bên mua nhận chuyển giao quyền sở hữu và không kèm theo cam kết bán , mua lại giấy tờ có giá hoặc bảo lưu quyền truy đòi ( sau đây gọi là mua ,** → `KHOAN` (span: `[15:93]`)
- `[e6]` **chi nhánh ngân hàng nước ngoài khác phát hành trong nước** → `TO_CHUC_DOANH_NGHIEP` (span: `[44:51]`) *(lồng trong `e5` (`KHOAN`))*
- `[e7]` **tổ chức tín dụng , chi nhánh ngân hàng nước ngoài** → `TO_CHUC_DOANH_NGHIEP` (span: `[22:28]`) *(lồng trong `e5` (`KHOAN`))*
- `[e8]` **giấy tờ có giá** → `TO_CHUC_DOANH_NGHIEP` (span: `[56:58]`) *(lồng trong `e5` (`KHOAN`))*
- `[e9]` **giấy tờ có giá** → `TO_CHUC_DOANH_NGHIEP` (span: `[79:81]`) *(lồng trong `e5` (`KHOAN`))*
- `[e10]` **chứng chỉ tiền gửi** → `GIAY_TO_HO_SO` (span: `[35:38]`) *(lồng trong `e5` (`KHOAN`))*
- `[e11]` **tổ chức tín dụng** → `TO_CHUC_DOANH_NGHIEP` (span: `[41:43]`) *(lồng trong `e5` (`KHOAN`))*
- `[e12]` **trái phiếu** → `TAI_SAN_VAT_CHAT` (span: `[39:40]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 12/2021/TT-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Ngân hàng Nhà nước Việt Nam `[CO_QUAN_BAN_HANH]`)
- (`e1` 12/2021/TT-NHNN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 12/2021/TT-NHNN `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Chính sách tiền tệ `[LINH_VUC]`)
- (`e4` Điều 1 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 12/2021/TT-NHNN `[SO_HIEU]`)
- (`e5` 1 . Thông tư này quy định về việc tổ chức tín dụng , chi nhánh ngân hàng nước ngoài mua , bán kỳ phiếu , tín phiếu , chứng chỉ tiền gửi , trái phiếu do tổ chức tín dụng , chi nhánh ngân hàng nước ngoài khác phát hành trong nước ( sau đây gọi là giấy tờ có giá ) chưa đến hạn thanh toán mà bên mua nhận chuyển giao quyền sở hữu và không kèm theo cam kết bán , mua lại giấy tờ có giá hoặc bảo lưu quyền truy đòi ( sau đây gọi là mua , `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 1 `[DIEU]`)
- (`e1` 12/2021/TT-NHNN `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Chính sách tiền tệ `[LINH_VUC]`)
- (`e5` 1 . Thông tư này quy định về việc tổ chức tín dụng , chi nhánh ngân hàng nước ngoài mua , bán kỳ phiếu , tín phiếu , chứng chỉ tiền gửi , trái phiếu do tổ chức tín dụng , chi nhánh ngân hàng nước ngoài khác phát hành trong nước ( sau đây gọi là giấy tờ có giá ) chưa đến hạn thanh toán mà bên mua nhận chuyển giao quyền sở hữu và không kèm theo cam kết bán , mua lại giấy tờ có giá hoặc bảo lưu quyền truy đòi ( sau đây gọi là mua , `[KHOAN]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Chính sách tiền tệ `[LINH_VUC]`)


---

### Mẫu #12_2021_TT-NHNN_148636#body_standalone_19 (Loại: `body_standalone`)
> **[Điều 1]`<DIEU>`** . **[1 . Thông tư này quy định về việc **[tổ chức tín dụng , chi nhánh ngân hàng nước ngoài]`<TO_CHUC_DOANH_NGHIEP>`** mua , bán kỳ phiếu , tín phiếu , **[chứng chỉ tiền gửi]`<GIAY_TO_HO_SO>`** , **[trái phiếu]`<TAI_SAN_VAT_CHAT>`** do **[tổ chức tín dụng]`<TO_CHUC_DOANH_NGHIEP>`** , **[chi nhánh ngân hàng nước ngoài khác phát hành trong nước]`<TO_CHUC_DOANH_NGHIEP>`** ( sau đây gọi là **[giấy tờ có giá]`<TO_CHUC_DOANH_NGHIEP>`** ) chưa đến hạn thanh toán mà bên mua nhận chuyển giao quyền sở hữu và không kèm theo cam kết bán , mua lại **[giấy tờ có giá]`<TO_CHUC_DOANH_NGHIEP>`** hoặc bảo lưu quyền truy đòi ( sau đây gọi là mua ,]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 1** → `DIEU` (span: `[0:2]`)
- `[e1]` **1 . Thông tư này quy định về việc tổ chức tín dụng , chi nhánh ngân hàng nước ngoài mua , bán kỳ phiếu , tín phiếu , chứng chỉ tiền gửi , trái phiếu do tổ chức tín dụng , chi nhánh ngân hàng nước ngoài khác phát hành trong nước ( sau đây gọi là giấy tờ có giá ) chưa đến hạn thanh toán mà bên mua nhận chuyển giao quyền sở hữu và không kèm theo cam kết bán , mua lại giấy tờ có giá hoặc bảo lưu quyền truy đòi ( sau đây gọi là mua ,** → `KHOAN` (span: `[3:81]`)
- `[e2]` **chi nhánh ngân hàng nước ngoài khác phát hành trong nước** → `TO_CHUC_DOANH_NGHIEP` (span: `[32:39]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **tổ chức tín dụng , chi nhánh ngân hàng nước ngoài** → `TO_CHUC_DOANH_NGHIEP` (span: `[10:16]`) *(lồng trong `e1` (`KHOAN`))*
- `[e4]` **giấy tờ có giá** → `TO_CHUC_DOANH_NGHIEP` (span: `[44:46]`) *(lồng trong `e1` (`KHOAN`))*
- `[e5]` **giấy tờ có giá** → `TO_CHUC_DOANH_NGHIEP` (span: `[67:69]`) *(lồng trong `e1` (`KHOAN`))*
- `[e6]` **chứng chỉ tiền gửi** → `GIAY_TO_HO_SO` (span: `[23:26]`) *(lồng trong `e1` (`KHOAN`))*
- `[e7]` **tổ chức tín dụng** → `TO_CHUC_DOANH_NGHIEP` (span: `[29:31]`) *(lồng trong `e1` (`KHOAN`))*
- `[e8]` **trái phiếu** → `TAI_SAN_VAT_CHAT` (span: `[27:28]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 1 . Thông tư này quy định về việc tổ chức tín dụng , chi nhánh ngân hàng nước ngoài mua , bán kỳ phiếu , tín phiếu , chứng chỉ tiền gửi , trái phiếu do tổ chức tín dụng , chi nhánh ngân hàng nước ngoài khác phát hành trong nước ( sau đây gọi là giấy tờ có giá ) chưa đến hạn thanh toán mà bên mua nhận chuyển giao quyền sở hữu và không kèm theo cam kết bán , mua lại giấy tờ có giá hoặc bảo lưu quyền truy đòi ( sau đây gọi là mua , `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 1 `[DIEU]`)


---

### Mẫu #12_2021_TT-NHNN_148636#body_context_20 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[12/2021/TT-NHNN]`<SO_HIEU>`** của **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Chính sách tiền tệ]`<LINH_VUC>`** . **[Điều 1]`<DIEU>`** . **[2 . Thông tư này không điều chỉnh đối với các hoạt động sau :]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **12/2021/TT-NHNN** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_BAN_HANH` (span: `[4:7]`)
- `[e3]` **Chính sách tiền tệ** → `LINH_VUC` (span: `[9:11]`)
- `[e4]` **Điều 1** → `DIEU` (span: `[12:14]`)
- `[e5]` **2 . Thông tư này không điều chỉnh đối với các hoạt động sau :** → `KHOAN` (span: `[15:26]`)

**Quan hệ:**
- (`e1` 12/2021/TT-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Ngân hàng Nhà nước Việt Nam `[CO_QUAN_BAN_HANH]`)
- (`e1` 12/2021/TT-NHNN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 12/2021/TT-NHNN `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Chính sách tiền tệ `[LINH_VUC]`)
- (`e4` Điều 1 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 12/2021/TT-NHNN `[SO_HIEU]`)
- (`e5` 2 . Thông tư này không điều chỉnh đối với các hoạt động sau : `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 1 `[DIEU]`)
- (`e1` 12/2021/TT-NHNN `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Chính sách tiền tệ `[LINH_VUC]`)
- (`e5` 2 . Thông tư này không điều chỉnh đối với các hoạt động sau : `[KHOAN]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Chính sách tiền tệ `[LINH_VUC]`)


---

### Mẫu #12_2021_TT-NHNN_148636#body_context_21 (Loại: `body_context`)
> **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[12/2021/TT-NHNN]`<SO_HIEU>`** . **[Điều 1]`<DIEU>`** . **[Khoản 2]`<KHOAN>`** . **[a ) Mua , bán **[giấy tờ có giá]`<TO_CHUC_DOANH_NGHIEP>`** của **[tổ chức tín dụng , chi nhánh ngân hàng nước ngoài]`<TO_CHUC_DOANH_NGHIEP>`** trên thị trường quốc tế ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[4:5]`)
- `[e1]` **12/2021/TT-NHNN** → `SO_HIEU` (span: `[6:7]`)
- `[e2]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_BAN_HANH` (span: `[0:3]`)
- `[e3]` **Điều 1** → `DIEU` (span: `[8:10]`)
- `[e4]` **Khoản 2** → `KHOAN` (span: `[11:13]`)
- `[e5]` **a ) Mua , bán giấy tờ có giá của tổ chức tín dụng , chi nhánh ngân hàng nước ngoài trên thị trường quốc tế ;** → `DIEM` (span: `[14:32]`)
- `[e6]` **tổ chức tín dụng , chi nhánh ngân hàng nước ngoài** → `TO_CHUC_DOANH_NGHIEP` (span: `[22:28]`) *(lồng trong `e5` (`DIEM`))*
- `[e7]` **giấy tờ có giá** → `TO_CHUC_DOANH_NGHIEP` (span: `[19:21]`) *(lồng trong `e5` (`DIEM`))*

**Quan hệ:**
- (`e1` 12/2021/TT-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Ngân hàng Nhà nước Việt Nam `[CO_QUAN_BAN_HANH]`)
- (`e1` 12/2021/TT-NHNN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 1 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 12/2021/TT-NHNN `[SO_HIEU]`)
- (`e4` Khoản 2 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 1 `[DIEU]`)
- (`e5` a ) Mua , bán giấy tờ có giá của tổ chức tín dụng , chi nhánh ngân hàng nước ngoài trên thị trường quốc tế ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e4` Khoản 2 `[KHOAN]`)


---

### Mẫu #12_2021_TT-NHNN_148636#body_standalone_22 (Loại: `body_standalone`)
> **[Điều 1]`<DIEU>`** . **[Khoản 2]`<KHOAN>`** . **[a ) Mua , bán **[giấy tờ có giá]`<TO_CHUC_DOANH_NGHIEP>`** của **[tổ chức tín dụng , chi nhánh ngân hàng nước ngoài]`<TO_CHUC_DOANH_NGHIEP>`** trên thị trường quốc tế ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Điều 1** → `DIEU` (span: `[0:2]`)
- `[e1]` **Khoản 2** → `KHOAN` (span: `[3:5]`)
- `[e2]` **a ) Mua , bán giấy tờ có giá của tổ chức tín dụng , chi nhánh ngân hàng nước ngoài trên thị trường quốc tế ;** → `DIEM` (span: `[6:24]`)
- `[e3]` **tổ chức tín dụng , chi nhánh ngân hàng nước ngoài** → `TO_CHUC_DOANH_NGHIEP` (span: `[14:20]`) *(lồng trong `e2` (`DIEM`))*
- `[e4]` **giấy tờ có giá** → `TO_CHUC_DOANH_NGHIEP` (span: `[11:13]`) *(lồng trong `e2` (`DIEM`))*

**Quan hệ:**
- (`e1` Khoản 2 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 1 `[DIEU]`)
- (`e2` a ) Mua , bán giấy tờ có giá của tổ chức tín dụng , chi nhánh ngân hàng nước ngoài trên thị trường quốc tế ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e1` Khoản 2 `[KHOAN]`)


---

### Mẫu #12_2021_TT-NHNN_148636#body_context_23 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[12/2021/TT-NHNN]`<SO_HIEU>`** của **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Chính sách tiền tệ]`<LINH_VUC>`** . **[Điều 1]`<DIEU>`** . **[Khoản 2]`<KHOAN>`** . **[b ) Mua , bán **[trái phiếu]`<TAI_SAN_VAT_CHAT>`** do **[tổ chức tín dụng phát hành]`<TO_CHUC_DOANH_NGHIEP>`** được **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** bảo lãnh ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **12/2021/TT-NHNN** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_BAN_HANH` (span: `[4:7]`)
- `[e3]` **Chính sách tiền tệ** → `LINH_VUC` (span: `[9:11]`)
- `[e4]` **Điều 1** → `DIEU` (span: `[12:14]`)
- `[e5]` **Khoản 2** → `KHOAN` (span: `[15:17]`)
- `[e6]` **b ) Mua , bán trái phiếu do tổ chức tín dụng phát hành được Chính phủ bảo lãnh ;** → `DIEM` (span: `[18:32]`)
- `[e7]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[29:30]`) *(lồng trong `e6` (`DIEM`))*
- `[e8]` **trái phiếu** → `TAI_SAN_VAT_CHAT` (span: `[23:24]`) *(lồng trong `e6` (`DIEM`))*
- `[e9]` **tổ chức tín dụng phát hành** → `TO_CHUC_DOANH_NGHIEP` (span: `[25:28]`) *(lồng trong `e6` (`DIEM`))*

**Quan hệ:**
- (`e1` 12/2021/TT-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Ngân hàng Nhà nước Việt Nam `[CO_QUAN_BAN_HANH]`)
- (`e1` 12/2021/TT-NHNN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 12/2021/TT-NHNN `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Chính sách tiền tệ `[LINH_VUC]`)
- (`e4` Điều 1 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 12/2021/TT-NHNN `[SO_HIEU]`)
- (`e5` Khoản 2 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 1 `[DIEU]`)
- (`e6` b ) Mua , bán trái phiếu do tổ chức tín dụng phát hành được Chính phủ bảo lãnh ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e5` Khoản 2 `[KHOAN]`)
- (`e1` 12/2021/TT-NHNN `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Chính sách tiền tệ `[LINH_VUC]`)
- (`e6` b ) Mua , bán trái phiếu do tổ chức tín dụng phát hành được Chính phủ bảo lãnh ; `[DIEM]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Chính sách tiền tệ `[LINH_VUC]`)


---

### Mẫu #12_2021_TT-NHNN_148636#body_standalone_24 (Loại: `body_standalone`)
> **[Điều 1]`<DIEU>`** . **[Khoản 2]`<KHOAN>`** . **[b ) Mua , bán **[trái phiếu]`<TAI_SAN_VAT_CHAT>`** do **[tổ chức tín dụng phát hành]`<TO_CHUC_DOANH_NGHIEP>`** được **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** bảo lãnh ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Điều 1** → `DIEU` (span: `[0:2]`)
- `[e1]` **Khoản 2** → `KHOAN` (span: `[3:5]`)
- `[e2]` **b ) Mua , bán trái phiếu do tổ chức tín dụng phát hành được Chính phủ bảo lãnh ;** → `DIEM` (span: `[6:20]`)
- `[e3]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[17:18]`) *(lồng trong `e2` (`DIEM`))*
- `[e4]` **trái phiếu** → `TAI_SAN_VAT_CHAT` (span: `[11:12]`) *(lồng trong `e2` (`DIEM`))*
- `[e5]` **tổ chức tín dụng phát hành** → `TO_CHUC_DOANH_NGHIEP` (span: `[13:16]`) *(lồng trong `e2` (`DIEM`))*

**Quan hệ:**
- (`e1` Khoản 2 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 1 `[DIEU]`)
- (`e2` b ) Mua , bán trái phiếu do tổ chức tín dụng phát hành được Chính phủ bảo lãnh ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e1` Khoản 2 `[KHOAN]`)


---

### Mẫu #12_2021_TT-NHNN_148636#body_context_25 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[12/2021/TT-NHNN]`<SO_HIEU>`** ban hành **[ngày 30 tháng 07 năm 2021]`<NGAY_BAN_HANH>`** bởi **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_BAN_HANH>`** . **[Điều 1]`<DIEU>`** . **[Khoản 2]`<KHOAN>`** . **[c ) Phát hành **[giấy tờ có giá]`<TO_CHUC_DOANH_NGHIEP>`** trong nước của **[tổ chức tín dụng , chi nhánh ngân hàng nước ngoài]`<TO_CHUC_DOANH_NGHIEP>`** ; mua lại và hoán đổi **[trái phiếu]`<TAI_SAN_VAT_CHAT>`** do chính **[tổ chức tín dụng phát hành]`<TO_CHUC_DOANH_NGHIEP>`** ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **12/2021/TT-NHNN** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_BAN_HANH` (span: `[11:14]`)
- `[e3]` **ngày 30 tháng 07 năm 2021** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 1** → `DIEU` (span: `[15:17]`)
- `[e5]` **Khoản 2** → `KHOAN` (span: `[18:20]`)
- `[e6]` **c ) Phát hành giấy tờ có giá trong nước của tổ chức tín dụng , chi nhánh ngân hàng nước ngoài ; mua lại và hoán đổi trái phiếu do chính tổ chức tín dụng phát hành ;** → `DIEM` (span: `[21:47]`)
- `[e7]` **tổ chức tín dụng , chi nhánh ngân hàng nước ngoài** → `TO_CHUC_DOANH_NGHIEP` (span: `[29:35]`) *(lồng trong `e6` (`DIEM`))*
- `[e8]` **giấy tờ có giá** → `TO_CHUC_DOANH_NGHIEP` (span: `[24:26]`) *(lồng trong `e6` (`DIEM`))*
- `[e9]` **trái phiếu** → `TAI_SAN_VAT_CHAT` (span: `[40:41]`) *(lồng trong `e6` (`DIEM`))*
- `[e10]` **tổ chức tín dụng phát hành** → `TO_CHUC_DOANH_NGHIEP` (span: `[43:46]`) *(lồng trong `e6` (`DIEM`))*

**Quan hệ:**
- (`e1` 12/2021/TT-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Ngân hàng Nhà nước Việt Nam `[CO_QUAN_BAN_HANH]`)
- (`e1` 12/2021/TT-NHNN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 12/2021/TT-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 30 tháng 07 năm 2021 `[NGAY_BAN_HANH]`)
- (`e4` Điều 1 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 12/2021/TT-NHNN `[SO_HIEU]`)
- (`e5` Khoản 2 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 1 `[DIEU]`)
- (`e6` c ) Phát hành giấy tờ có giá trong nước của tổ chức tín dụng , chi nhánh ngân hàng nước ngoài ; mua lại và hoán đổi trái phiếu do chính tổ chức tín dụng phát hành ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e5` Khoản 2 `[KHOAN]`)


---

### Mẫu #12_2021_TT-NHNN_148636#body_standalone_26 (Loại: `body_standalone`)
> **[Điều 1]`<DIEU>`** . **[Khoản 2]`<KHOAN>`** . **[c ) Phát hành **[giấy tờ có giá]`<TO_CHUC_DOANH_NGHIEP>`** trong nước của **[tổ chức tín dụng , chi nhánh ngân hàng nước ngoài]`<TO_CHUC_DOANH_NGHIEP>`** ; mua lại và hoán đổi **[trái phiếu]`<TAI_SAN_VAT_CHAT>`** do chính **[tổ chức tín dụng phát hành]`<TO_CHUC_DOANH_NGHIEP>`** ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Điều 1** → `DIEU` (span: `[0:2]`)
- `[e1]` **Khoản 2** → `KHOAN` (span: `[3:5]`)
- `[e2]` **c ) Phát hành giấy tờ có giá trong nước của tổ chức tín dụng , chi nhánh ngân hàng nước ngoài ; mua lại và hoán đổi trái phiếu do chính tổ chức tín dụng phát hành ;** → `DIEM` (span: `[6:32]`)
- `[e3]` **tổ chức tín dụng , chi nhánh ngân hàng nước ngoài** → `TO_CHUC_DOANH_NGHIEP` (span: `[14:20]`) *(lồng trong `e2` (`DIEM`))*
- `[e4]` **giấy tờ có giá** → `TO_CHUC_DOANH_NGHIEP` (span: `[9:11]`) *(lồng trong `e2` (`DIEM`))*
- `[e5]` **trái phiếu** → `TAI_SAN_VAT_CHAT` (span: `[25:26]`) *(lồng trong `e2` (`DIEM`))*
- `[e6]` **tổ chức tín dụng phát hành** → `TO_CHUC_DOANH_NGHIEP` (span: `[28:31]`) *(lồng trong `e2` (`DIEM`))*

**Quan hệ:**
- (`e1` Khoản 2 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 1 `[DIEU]`)
- (`e2` c ) Phát hành giấy tờ có giá trong nước của tổ chức tín dụng , chi nhánh ngân hàng nước ngoài ; mua lại và hoán đổi trái phiếu do chính tổ chức tín dụng phát hành ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e1` Khoản 2 `[KHOAN]`)


---

### Mẫu #12_2021_TT-NHNN_148636#body_context_27 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[12/2021/TT-NHNN]`<SO_HIEU>`** của **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Chính sách tiền tệ]`<LINH_VUC>`** . **[Điều 1]`<DIEU>`** . **[Khoản 2]`<KHOAN>`** . **[d ) Mua , bán có kỳ hạn **[giấy tờ có giá]`<TO_CHUC_DOANH_NGHIEP>`** giữa các **[tổ chức tín dụng , chi nhánh ngân hàng nước ngoài]`<TO_CHUC_DOANH_NGHIEP>`** ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **12/2021/TT-NHNN** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_BAN_HANH` (span: `[4:7]`)
- `[e3]` **Chính sách tiền tệ** → `LINH_VUC` (span: `[9:11]`)
- `[e4]` **Điều 1** → `DIEU` (span: `[12:14]`)
- `[e5]` **Khoản 2** → `KHOAN` (span: `[15:17]`)
- `[e6]` **d ) Mua , bán có kỳ hạn giấy tờ có giá giữa các tổ chức tín dụng , chi nhánh ngân hàng nước ngoài ;** → `DIEM` (span: `[18:36]`)
- `[e7]` **tổ chức tín dụng , chi nhánh ngân hàng nước ngoài** → `TO_CHUC_DOANH_NGHIEP` (span: `[29:35]`) *(lồng trong `e6` (`DIEM`))*
- `[e8]` **giấy tờ có giá** → `TO_CHUC_DOANH_NGHIEP` (span: `[25:27]`) *(lồng trong `e6` (`DIEM`))*

**Quan hệ:**
- (`e1` 12/2021/TT-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Ngân hàng Nhà nước Việt Nam `[CO_QUAN_BAN_HANH]`)
- (`e1` 12/2021/TT-NHNN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 12/2021/TT-NHNN `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Chính sách tiền tệ `[LINH_VUC]`)
- (`e4` Điều 1 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 12/2021/TT-NHNN `[SO_HIEU]`)
- (`e5` Khoản 2 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 1 `[DIEU]`)
- (`e6` d ) Mua , bán có kỳ hạn giấy tờ có giá giữa các tổ chức tín dụng , chi nhánh ngân hàng nước ngoài ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e5` Khoản 2 `[KHOAN]`)
- (`e1` 12/2021/TT-NHNN `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Chính sách tiền tệ `[LINH_VUC]`)
- (`e6` d ) Mua , bán có kỳ hạn giấy tờ có giá giữa các tổ chức tín dụng , chi nhánh ngân hàng nước ngoài ; `[DIEM]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Chính sách tiền tệ `[LINH_VUC]`)


---

### Mẫu #12_2021_TT-NHNN_148636#body_standalone_28 (Loại: `body_standalone`)
> **[Điều 1]`<DIEU>`** . **[Khoản 2]`<KHOAN>`** . **[d ) Mua , bán có kỳ hạn **[giấy tờ có giá]`<TO_CHUC_DOANH_NGHIEP>`** giữa các **[tổ chức tín dụng , chi nhánh ngân hàng nước ngoài]`<TO_CHUC_DOANH_NGHIEP>`** ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Điều 1** → `DIEU` (span: `[0:2]`)
- `[e1]` **Khoản 2** → `KHOAN` (span: `[3:5]`)
- `[e2]` **d ) Mua , bán có kỳ hạn giấy tờ có giá giữa các tổ chức tín dụng , chi nhánh ngân hàng nước ngoài ;** → `DIEM` (span: `[6:24]`)
- `[e3]` **tổ chức tín dụng , chi nhánh ngân hàng nước ngoài** → `TO_CHUC_DOANH_NGHIEP` (span: `[17:23]`) *(lồng trong `e2` (`DIEM`))*
- `[e4]` **giấy tờ có giá** → `TO_CHUC_DOANH_NGHIEP` (span: `[13:15]`) *(lồng trong `e2` (`DIEM`))*

**Quan hệ:**
- (`e1` Khoản 2 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 1 `[DIEU]`)
- (`e2` d ) Mua , bán có kỳ hạn giấy tờ có giá giữa các tổ chức tín dụng , chi nhánh ngân hàng nước ngoài ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e1` Khoản 2 `[KHOAN]`)


---

### Mẫu #12_2021_TT-NHNN_148636#body_context_29 (Loại: `body_context`)
> **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[12/2021/TT-NHNN]`<SO_HIEU>`** . **[Điều 1]`<DIEU>`** . **[Khoản 2]`<KHOAN>`** . **[đ ) Chuyển quyền sở hữu **[giấy tờ có giá]`<TO_CHUC_DOANH_NGHIEP>`** do xử lý **[tài sản bảo đảm]`<TAI_SAN_VAT_CHAT>`** . Việc chuyển quyền sở hữu trong trường hợp này thực hiện theo pháp luật về giao dịch bảo đảm .]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[4:5]`)
- `[e1]` **12/2021/TT-NHNN** → `SO_HIEU` (span: `[6:7]`)
- `[e2]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_BAN_HANH` (span: `[0:3]`)
- `[e3]` **Điều 1** → `DIEU` (span: `[8:10]`)
- `[e4]` **Khoản 2** → `KHOAN` (span: `[11:13]`)
- `[e5]` **đ ) Chuyển quyền sở hữu giấy tờ có giá do xử lý tài sản bảo đảm . Việc chuyển quyền sở hữu trong trường hợp này thực hiện theo pháp luật về giao dịch bảo đảm .** → `DIEM` (span: `[14:40]`)
- `[e6]` **giấy tờ có giá** → `TO_CHUC_DOANH_NGHIEP` (span: `[19:21]`) *(lồng trong `e5` (`DIEM`))*
- `[e7]` **tài sản bảo đảm** → `TAI_SAN_VAT_CHAT` (span: `[23:25]`) *(lồng trong `e5` (`DIEM`))*

**Quan hệ:**
- (`e1` 12/2021/TT-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Ngân hàng Nhà nước Việt Nam `[CO_QUAN_BAN_HANH]`)
- (`e1` 12/2021/TT-NHNN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 1 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 12/2021/TT-NHNN `[SO_HIEU]`)
- (`e4` Khoản 2 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 1 `[DIEU]`)
- (`e5` đ ) Chuyển quyền sở hữu giấy tờ có giá do xử lý tài sản bảo đảm . Việc chuyển quyền sở hữu trong trường hợp này thực hiện theo pháp luật về giao dịch bảo đảm . `[DIEM]`) ==[ **THUOC_VE** ]==> (`e4` Khoản 2 `[KHOAN]`)


---

### Mẫu #12_2021_TT-NHNN_148636#body_standalone_30 (Loại: `body_standalone`)
> **[Điều 1]`<DIEU>`** . **[Khoản 2]`<KHOAN>`** . **[đ ) Chuyển quyền sở hữu **[giấy tờ có giá]`<TO_CHUC_DOANH_NGHIEP>`** do xử lý **[tài sản bảo đảm]`<TAI_SAN_VAT_CHAT>`** . Việc chuyển quyền sở hữu trong trường hợp này thực hiện theo pháp luật về giao dịch bảo đảm .]`<DIEM>`**

**Thực thể:**
- `[e0]` **Điều 1** → `DIEU` (span: `[0:2]`)
- `[e1]` **Khoản 2** → `KHOAN` (span: `[3:5]`)
- `[e2]` **đ ) Chuyển quyền sở hữu giấy tờ có giá do xử lý tài sản bảo đảm . Việc chuyển quyền sở hữu trong trường hợp này thực hiện theo pháp luật về giao dịch bảo đảm .** → `DIEM` (span: `[6:32]`)
- `[e3]` **giấy tờ có giá** → `TO_CHUC_DOANH_NGHIEP` (span: `[11:13]`) *(lồng trong `e2` (`DIEM`))*
- `[e4]` **tài sản bảo đảm** → `TAI_SAN_VAT_CHAT` (span: `[15:17]`) *(lồng trong `e2` (`DIEM`))*

**Quan hệ:**
- (`e1` Khoản 2 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 1 `[DIEU]`)
- (`e2` đ ) Chuyển quyền sở hữu giấy tờ có giá do xử lý tài sản bảo đảm . Việc chuyển quyền sở hữu trong trường hợp này thực hiện theo pháp luật về giao dịch bảo đảm . `[DIEM]`) ==[ **THUOC_VE** ]==> (`e1` Khoản 2 `[KHOAN]`)


---

### Mẫu #12_2021_TT-NHNN_148636#body_context_31 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[12/2021/TT-NHNN]`<SO_HIEU>`** ban hành **[ngày 30 tháng 07 năm 2021]`<NGAY_BAN_HANH>`** bởi **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_BAN_HANH>`** . **[Điều 2 . Đối tượng áp dụng . Bên bán , Bên mua **[giấy tờ có giá]`<TO_CHUC_DOANH_NGHIEP>`** bao gồm các đối tượng sau :]`<DIEU>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **12/2021/TT-NHNN** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_BAN_HANH` (span: `[11:14]`)
- `[e3]` **ngày 30 tháng 07 năm 2021** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 2 . Đối tượng áp dụng . Bên bán , Bên mua giấy tờ có giá bao gồm các đối tượng sau :** → `DIEU` (span: `[15:33]`)
- `[e5]` **giấy tờ có giá** → `TO_CHUC_DOANH_NGHIEP` (span: `[26:28]`) *(lồng trong `e4` (`DIEU`))*

**Quan hệ:**
- (`e1` 12/2021/TT-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Ngân hàng Nhà nước Việt Nam `[CO_QUAN_BAN_HANH]`)
- (`e1` 12/2021/TT-NHNN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 12/2021/TT-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 30 tháng 07 năm 2021 `[NGAY_BAN_HANH]`)
- (`e4` Điều 2 . Đối tượng áp dụng . Bên bán , Bên mua giấy tờ có giá bao gồm các đối tượng sau : `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 12/2021/TT-NHNN `[SO_HIEU]`)


---

### Mẫu #12_2021_TT-NHNN_148636#body_context_32 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[12/2021/TT-NHNN]`<SO_HIEU>`** ban hành **[ngày 30 tháng 07 năm 2021]`<NGAY_BAN_HANH>`** bởi **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_BAN_HANH>`** . **[Điều 2]`<DIEU>`** . **[1 . **[Tổ chức tín dụng , chi nhánh ngân hàng nước ngoài]`<TO_CHUC_DOANH_NGHIEP>`** được thành lập và hoạt động theo quy định của Luật Các **[tổ chức tín dụng]`<TO_CHUC_DOANH_NGHIEP>`** bao gồm : **[ngân hàng thương mại]`<TO_CHUC_DOANH_NGHIEP>`** , **[ngân hàng hợp tác xã]`<TO_CHUC_DOANH_NGHIEP>`** , **[chi nhánh ngân hàng nước ngoài]`<TO_CHUC_DOANH_NGHIEP>`** , **[công ty tài chính]`<TO_CHUC_DOANH_NGHIEP>`** ( sau đây gọi là **[tổ chức tín dụng , chi nhánh ngân hàng nước ngoài]`<TO_CHUC_DOANH_NGHIEP>`** ) .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **12/2021/TT-NHNN** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_BAN_HANH` (span: `[11:14]`)
- `[e3]` **ngày 30 tháng 07 năm 2021** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 2** → `DIEU` (span: `[15:17]`)
- `[e5]` **1 . Tổ chức tín dụng , chi nhánh ngân hàng nước ngoài được thành lập và hoạt động theo quy định của Luật Các tổ chức tín dụng bao gồm : ngân hàng thương mại , ngân hàng hợp tác xã , chi nhánh ngân hàng nước ngoài , công ty tài chính ( sau đây gọi là tổ chức tín dụng , chi nhánh ngân hàng nước ngoài ) .** → `KHOAN` (span: `[18:64]`)
- `[e6]` **Tổ chức tín dụng , chi nhánh ngân hàng nước ngoài** → `TO_CHUC_DOANH_NGHIEP` (span: `[20:26]`) *(lồng trong `e5` (`KHOAN`))*
- `[e7]` **tổ chức tín dụng , chi nhánh ngân hàng nước ngoài** → `TO_CHUC_DOANH_NGHIEP` (span: `[56:62]`) *(lồng trong `e5` (`KHOAN`))*
- `[e8]` **công ty tài chính** → `TO_CHUC_DOANH_NGHIEP` (span: `[49:51]`) *(lồng trong `e5` (`KHOAN`))*
- `[e9]` **tổ chức tín dụng** → `TO_CHUC_DOANH_NGHIEP` (span: `[35:37]`) *(lồng trong `e5` (`KHOAN`))*
- `[e10]` **ngân hàng thương mại** → `TO_CHUC_DOANH_NGHIEP` (span: `[39:41]`) *(lồng trong `e5` (`KHOAN`))*
- `[e11]` **ngân hàng hợp tác xã** → `TO_CHUC_DOANH_NGHIEP` (span: `[42:44]`) *(lồng trong `e5` (`KHOAN`))*
- `[e12]` **chi nhánh ngân hàng nước ngoài** → `TO_CHUC_DOANH_NGHIEP` (span: `[45:48]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 12/2021/TT-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Ngân hàng Nhà nước Việt Nam `[CO_QUAN_BAN_HANH]`)
- (`e1` 12/2021/TT-NHNN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 12/2021/TT-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 30 tháng 07 năm 2021 `[NGAY_BAN_HANH]`)
- (`e4` Điều 2 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 12/2021/TT-NHNN `[SO_HIEU]`)
- (`e5` 1 . Tổ chức tín dụng , chi nhánh ngân hàng nước ngoài được thành lập và hoạt động theo quy định của Luật Các tổ chức tín dụng bao gồm : ngân hàng thương mại , ngân hàng hợp tác xã , chi nhánh ngân hàng nước ngoài , công ty tài chính ( sau đây gọi là tổ chức tín dụng , chi nhánh ngân hàng nước ngoài ) . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 2 `[DIEU]`)


---

### Mẫu #12_2021_TT-NHNN_148636#body_standalone_33 (Loại: `body_standalone`)
> **[Điều 2]`<DIEU>`** . **[1 . **[Tổ chức tín dụng , chi nhánh ngân hàng nước ngoài]`<TO_CHUC_DOANH_NGHIEP>`** được thành lập và hoạt động theo quy định của Luật Các **[tổ chức tín dụng]`<TO_CHUC_DOANH_NGHIEP>`** bao gồm : **[ngân hàng thương mại]`<TO_CHUC_DOANH_NGHIEP>`** , **[ngân hàng hợp tác xã]`<TO_CHUC_DOANH_NGHIEP>`** , **[chi nhánh ngân hàng nước ngoài]`<TO_CHUC_DOANH_NGHIEP>`** , **[công ty tài chính]`<TO_CHUC_DOANH_NGHIEP>`** ( sau đây gọi là **[tổ chức tín dụng , chi nhánh ngân hàng nước ngoài]`<TO_CHUC_DOANH_NGHIEP>`** ) .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 2** → `DIEU` (span: `[0:2]`)
- `[e1]` **1 . Tổ chức tín dụng , chi nhánh ngân hàng nước ngoài được thành lập và hoạt động theo quy định của Luật Các tổ chức tín dụng bao gồm : ngân hàng thương mại , ngân hàng hợp tác xã , chi nhánh ngân hàng nước ngoài , công ty tài chính ( sau đây gọi là tổ chức tín dụng , chi nhánh ngân hàng nước ngoài ) .** → `KHOAN` (span: `[3:49]`)
- `[e2]` **Tổ chức tín dụng , chi nhánh ngân hàng nước ngoài** → `TO_CHUC_DOANH_NGHIEP` (span: `[5:11]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **tổ chức tín dụng , chi nhánh ngân hàng nước ngoài** → `TO_CHUC_DOANH_NGHIEP` (span: `[41:47]`) *(lồng trong `e1` (`KHOAN`))*
- `[e4]` **công ty tài chính** → `TO_CHUC_DOANH_NGHIEP` (span: `[34:36]`) *(lồng trong `e1` (`KHOAN`))*
- `[e5]` **tổ chức tín dụng** → `TO_CHUC_DOANH_NGHIEP` (span: `[20:22]`) *(lồng trong `e1` (`KHOAN`))*
- `[e6]` **ngân hàng thương mại** → `TO_CHUC_DOANH_NGHIEP` (span: `[24:26]`) *(lồng trong `e1` (`KHOAN`))*
- `[e7]` **ngân hàng hợp tác xã** → `TO_CHUC_DOANH_NGHIEP` (span: `[27:29]`) *(lồng trong `e1` (`KHOAN`))*
- `[e8]` **chi nhánh ngân hàng nước ngoài** → `TO_CHUC_DOANH_NGHIEP` (span: `[30:33]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 1 . Tổ chức tín dụng , chi nhánh ngân hàng nước ngoài được thành lập và hoạt động theo quy định của Luật Các tổ chức tín dụng bao gồm : ngân hàng thương mại , ngân hàng hợp tác xã , chi nhánh ngân hàng nước ngoài , công ty tài chính ( sau đây gọi là tổ chức tín dụng , chi nhánh ngân hàng nước ngoài ) . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 2 `[DIEU]`)


---

### Mẫu #12_2021_TT-NHNN_148636#body_context_34 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[12/2021/TT-NHNN]`<SO_HIEU>`** của **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Chính sách tiền tệ]`<LINH_VUC>`** . **[Điều 2]`<DIEU>`** . **[2 . Tổ chức , cá nhân Việt Nam và tổ chức , cá nhân nước ngoài thực hiện mua , bán **[giấy tờ có giá]`<TO_CHUC_DOANH_NGHIEP>`** với **[tổ chức tín dụng , chi nhánh ngân hàng nước ngoài]`<TO_CHUC_DOANH_NGHIEP>`** .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **12/2021/TT-NHNN** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_BAN_HANH` (span: `[4:7]`)
- `[e3]` **Chính sách tiền tệ** → `LINH_VUC` (span: `[9:11]`)
- `[e4]` **Điều 2** → `DIEU` (span: `[12:14]`)
- `[e5]` **2 . Tổ chức , cá nhân Việt Nam và tổ chức , cá nhân nước ngoài thực hiện mua , bán giấy tờ có giá với tổ chức tín dụng , chi nhánh ngân hàng nước ngoài .** → `KHOAN` (span: `[15:40]`)
- `[e6]` **tổ chức tín dụng , chi nhánh ngân hàng nước ngoài** → `TO_CHUC_DOANH_NGHIEP` (span: `[33:39]`) *(lồng trong `e5` (`KHOAN`))*
- `[e7]` **giấy tờ có giá** → `TO_CHUC_DOANH_NGHIEP` (span: `[30:32]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 12/2021/TT-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Ngân hàng Nhà nước Việt Nam `[CO_QUAN_BAN_HANH]`)
- (`e1` 12/2021/TT-NHNN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 12/2021/TT-NHNN `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Chính sách tiền tệ `[LINH_VUC]`)
- (`e4` Điều 2 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 12/2021/TT-NHNN `[SO_HIEU]`)
- (`e5` 2 . Tổ chức , cá nhân Việt Nam và tổ chức , cá nhân nước ngoài thực hiện mua , bán giấy tờ có giá với tổ chức tín dụng , chi nhánh ngân hàng nước ngoài . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 2 `[DIEU]`)
- (`e1` 12/2021/TT-NHNN `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Chính sách tiền tệ `[LINH_VUC]`)
- (`e5` 2 . Tổ chức , cá nhân Việt Nam và tổ chức , cá nhân nước ngoài thực hiện mua , bán giấy tờ có giá với tổ chức tín dụng , chi nhánh ngân hàng nước ngoài . `[KHOAN]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Chính sách tiền tệ `[LINH_VUC]`)


---

### Mẫu #12_2021_TT-NHNN_148636#body_standalone_35 (Loại: `body_standalone`)
> **[Điều 2]`<DIEU>`** . **[2 . Tổ chức , cá nhân Việt Nam và tổ chức , cá nhân nước ngoài thực hiện mua , bán **[giấy tờ có giá]`<TO_CHUC_DOANH_NGHIEP>`** với **[tổ chức tín dụng , chi nhánh ngân hàng nước ngoài]`<TO_CHUC_DOANH_NGHIEP>`** .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 2** → `DIEU` (span: `[0:2]`)
- `[e1]` **2 . Tổ chức , cá nhân Việt Nam và tổ chức , cá nhân nước ngoài thực hiện mua , bán giấy tờ có giá với tổ chức tín dụng , chi nhánh ngân hàng nước ngoài .** → `KHOAN` (span: `[3:28]`)
- `[e2]` **tổ chức tín dụng , chi nhánh ngân hàng nước ngoài** → `TO_CHUC_DOANH_NGHIEP` (span: `[21:27]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **giấy tờ có giá** → `TO_CHUC_DOANH_NGHIEP` (span: `[18:20]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 2 . Tổ chức , cá nhân Việt Nam và tổ chức , cá nhân nước ngoài thực hiện mua , bán giấy tờ có giá với tổ chức tín dụng , chi nhánh ngân hàng nước ngoài . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 2 `[DIEU]`)


---

### Mẫu #12_2021_TT-NHNN_148636#body_context_36 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[12/2021/TT-NHNN]`<SO_HIEU>`** ban hành **[ngày 30 tháng 07 năm 2021]`<NGAY_BAN_HANH>`** bởi **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_BAN_HANH>`** . **[Điều 3 . Nguyên tắc mua , bán **[giấy tờ có giá]`<TO_CHUC_DOANH_NGHIEP>`**]`<DIEU>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **12/2021/TT-NHNN** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_BAN_HANH` (span: `[11:14]`)
- `[e3]` **ngày 30 tháng 07 năm 2021** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 3 . Nguyên tắc mua , bán giấy tờ có giá** → `DIEU` (span: `[15:24]`)
- `[e5]` **giấy tờ có giá** → `TO_CHUC_DOANH_NGHIEP` (span: `[22:24]`) *(lồng trong `e4` (`DIEU`))*

**Quan hệ:**
- (`e1` 12/2021/TT-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Ngân hàng Nhà nước Việt Nam `[CO_QUAN_BAN_HANH]`)
- (`e1` 12/2021/TT-NHNN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 12/2021/TT-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 30 tháng 07 năm 2021 `[NGAY_BAN_HANH]`)
- (`e4` Điều 3 . Nguyên tắc mua , bán giấy tờ có giá `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 12/2021/TT-NHNN `[SO_HIEU]`)


---

### Mẫu #12_2021_TT-NHNN_148636#body_context_37 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[12/2021/TT-NHNN]`<SO_HIEU>`** ban hành **[ngày 30 tháng 07 năm 2021]`<NGAY_BAN_HANH>`** bởi **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_BAN_HANH>`** . **[Điều 3]`<DIEU>`** . **[1 . **[Tổ chức tín dụng , chi nhánh ngân hàng nước ngoài]`<TO_CHUC_DOANH_NGHIEP>`** được mua , bán **[giấy tờ có giá]`<TO_CHUC_DOANH_NGHIEP>`** phù hợp với nội dung mua , bán **[trái phiếu doanh nghiệp]`<TAI_SAN_VAT_CHAT>`** và / hoặc **[giấy tờ có giá]`<TO_CHUC_DOANH_NGHIEP>`** khác ghi trong Giấy phép do **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_THAM_QUYEN>`** cấp .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **12/2021/TT-NHNN** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_BAN_HANH` (span: `[11:14]`)
- `[e3]` **ngày 30 tháng 07 năm 2021** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 3** → `DIEU` (span: `[15:17]`)
- `[e5]` **1 . Tổ chức tín dụng , chi nhánh ngân hàng nước ngoài được mua , bán giấy tờ có giá phù hợp với nội dung mua , bán trái phiếu doanh nghiệp và / hoặc giấy tờ có giá khác ghi trong Giấy phép do Ngân hàng Nhà nước Việt Nam cấp .** → `KHOAN` (span: `[18:55]`)
- `[e6]` **Tổ chức tín dụng , chi nhánh ngân hàng nước ngoài** → `TO_CHUC_DOANH_NGHIEP` (span: `[20:26]`) *(lồng trong `e5` (`KHOAN`))*
- `[e7]` **giấy tờ có giá** → `TO_CHUC_DOANH_NGHIEP` (span: `[30:32]`) *(lồng trong `e5` (`KHOAN`))*
- `[e8]` **giấy tờ có giá** → `TO_CHUC_DOANH_NGHIEP` (span: `[43:45]`) *(lồng trong `e5` (`KHOAN`))*
- `[e9]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_THAM_QUYEN` (span: `[50:53]`) *(lồng trong `e5` (`KHOAN`))*
- `[e10]` **trái phiếu doanh nghiệp** → `TAI_SAN_VAT_CHAT` (span: `[38:40]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 12/2021/TT-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Ngân hàng Nhà nước Việt Nam `[CO_QUAN_BAN_HANH]`)
- (`e1` 12/2021/TT-NHNN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 12/2021/TT-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 30 tháng 07 năm 2021 `[NGAY_BAN_HANH]`)
- (`e4` Điều 3 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 12/2021/TT-NHNN `[SO_HIEU]`)
- (`e5` 1 . Tổ chức tín dụng , chi nhánh ngân hàng nước ngoài được mua , bán giấy tờ có giá phù hợp với nội dung mua , bán trái phiếu doanh nghiệp và / hoặc giấy tờ có giá khác ghi trong Giấy phép do Ngân hàng Nhà nước Việt Nam cấp . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 3 `[DIEU]`)


---

### Mẫu #12_2021_TT-NHNN_148636#body_standalone_38 (Loại: `body_standalone`)
> **[Điều 3]`<DIEU>`** . **[1 . **[Tổ chức tín dụng , chi nhánh ngân hàng nước ngoài]`<TO_CHUC_DOANH_NGHIEP>`** được mua , bán **[giấy tờ có giá]`<TO_CHUC_DOANH_NGHIEP>`** phù hợp với nội dung mua , bán **[trái phiếu doanh nghiệp]`<TAI_SAN_VAT_CHAT>`** và / hoặc **[giấy tờ có giá]`<TO_CHUC_DOANH_NGHIEP>`** khác ghi trong Giấy phép do **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_THAM_QUYEN>`** cấp .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 3** → `DIEU` (span: `[0:2]`)
- `[e1]` **1 . Tổ chức tín dụng , chi nhánh ngân hàng nước ngoài được mua , bán giấy tờ có giá phù hợp với nội dung mua , bán trái phiếu doanh nghiệp và / hoặc giấy tờ có giá khác ghi trong Giấy phép do Ngân hàng Nhà nước Việt Nam cấp .** → `KHOAN` (span: `[3:40]`)
- `[e2]` **Tổ chức tín dụng , chi nhánh ngân hàng nước ngoài** → `TO_CHUC_DOANH_NGHIEP` (span: `[5:11]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **giấy tờ có giá** → `TO_CHUC_DOANH_NGHIEP` (span: `[15:17]`) *(lồng trong `e1` (`KHOAN`))*
- `[e4]` **giấy tờ có giá** → `TO_CHUC_DOANH_NGHIEP` (span: `[28:30]`) *(lồng trong `e1` (`KHOAN`))*
- `[e5]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_THAM_QUYEN` (span: `[35:38]`) *(lồng trong `e1` (`KHOAN`))*
- `[e6]` **trái phiếu doanh nghiệp** → `TAI_SAN_VAT_CHAT` (span: `[23:25]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 1 . Tổ chức tín dụng , chi nhánh ngân hàng nước ngoài được mua , bán giấy tờ có giá phù hợp với nội dung mua , bán trái phiếu doanh nghiệp và / hoặc giấy tờ có giá khác ghi trong Giấy phép do Ngân hàng Nhà nước Việt Nam cấp . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 3 `[DIEU]`)


---

### Mẫu #12_2021_TT-NHNN_148636#body_context_39 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[12/2021/TT-NHNN]`<SO_HIEU>`** của **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Chính sách tiền tệ]`<LINH_VUC>`** . **[Điều 3]`<DIEU>`** . **[2 . Bên mua , Bên bán chịu trách nhiệm trước pháp luật về việc mua , bán **[giấy tờ có giá]`<TO_CHUC_DOANH_NGHIEP>`** phù hợp với **[quy định tại]`<TU_KHOA_PHAP_LY>`** **[Thông tư này]`<THAM_CHIEU_PHAP_LY>`** và quy định của pháp luật có liên quan .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **12/2021/TT-NHNN** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_BAN_HANH` (span: `[4:7]`)
- `[e3]` **Chính sách tiền tệ** → `LINH_VUC` (span: `[9:11]`)
- `[e4]` **Điều 3** → `DIEU` (span: `[12:14]`)
- `[e5]` **2 . Bên mua , Bên bán chịu trách nhiệm trước pháp luật về việc mua , bán giấy tờ có giá phù hợp với quy định tại Thông tư này và quy định của pháp luật có liên quan .** → `KHOAN` (span: `[15:45]`)
- `[e6]` **giấy tờ có giá** → `TO_CHUC_DOANH_NGHIEP` (span: `[30:32]`) *(lồng trong `e5` (`KHOAN`))*
- `[e7]` **Thông tư này** → `THAM_CHIEU_PHAP_LY` (span: `[36:38]`) *(lồng trong `e5` (`KHOAN`))*
- `[e8]` **quy định tại** → `TU_KHOA_PHAP_LY` (span: `[34:36]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 12/2021/TT-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Ngân hàng Nhà nước Việt Nam `[CO_QUAN_BAN_HANH]`)
- (`e1` 12/2021/TT-NHNN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 12/2021/TT-NHNN `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Chính sách tiền tệ `[LINH_VUC]`)
- (`e4` Điều 3 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 12/2021/TT-NHNN `[SO_HIEU]`)
- (`e5` 2 . Bên mua , Bên bán chịu trách nhiệm trước pháp luật về việc mua , bán giấy tờ có giá phù hợp với quy định tại Thông tư này và quy định của pháp luật có liên quan . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 3 `[DIEU]`)
- (`e1` 12/2021/TT-NHNN `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Chính sách tiền tệ `[LINH_VUC]`)
- (`e5` 2 . Bên mua , Bên bán chịu trách nhiệm trước pháp luật về việc mua , bán giấy tờ có giá phù hợp với quy định tại Thông tư này và quy định của pháp luật có liên quan . `[KHOAN]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Chính sách tiền tệ `[LINH_VUC]`)
- (`e8` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e7` Thông tư này `[THAM_CHIEU_PHAP_LY]`)
- (`e5` 2 . Bên mua , Bên bán chịu trách nhiệm trước pháp luật về việc mua , bán giấy tờ có giá phù hợp với quy định tại Thông tư này và quy định của pháp luật có liên quan . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e7` Thông tư này `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #12_2021_TT-NHNN_148636#body_standalone_40 (Loại: `body_standalone`)
> **[Điều 3]`<DIEU>`** . **[2 . Bên mua , Bên bán chịu trách nhiệm trước pháp luật về việc mua , bán **[giấy tờ có giá]`<TO_CHUC_DOANH_NGHIEP>`** phù hợp với **[quy định tại]`<TU_KHOA_PHAP_LY>`** **[Thông tư này]`<THAM_CHIEU_PHAP_LY>`** và quy định của pháp luật có liên quan .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 3** → `DIEU` (span: `[0:2]`)
- `[e1]` **2 . Bên mua , Bên bán chịu trách nhiệm trước pháp luật về việc mua , bán giấy tờ có giá phù hợp với quy định tại Thông tư này và quy định của pháp luật có liên quan .** → `KHOAN` (span: `[3:33]`)
- `[e2]` **giấy tờ có giá** → `TO_CHUC_DOANH_NGHIEP` (span: `[18:20]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **Thông tư này** → `THAM_CHIEU_PHAP_LY` (span: `[24:26]`) *(lồng trong `e1` (`KHOAN`))*
- `[e4]` **quy định tại** → `TU_KHOA_PHAP_LY` (span: `[22:24]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 2 . Bên mua , Bên bán chịu trách nhiệm trước pháp luật về việc mua , bán giấy tờ có giá phù hợp với quy định tại Thông tư này và quy định của pháp luật có liên quan . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 3 `[DIEU]`)
- (`e4` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Thông tư này `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 2 . Bên mua , Bên bán chịu trách nhiệm trước pháp luật về việc mua , bán giấy tờ có giá phù hợp với quy định tại Thông tư này và quy định của pháp luật có liên quan . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Thông tư này `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #12_2021_TT-NHNN_148636#body_context_41 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[12/2021/TT-NHNN]`<SO_HIEU>`** ban hành **[ngày 30 tháng 07 năm 2021]`<NGAY_BAN_HANH>`** bởi **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_BAN_HANH>`** . **[Điều 3]`<DIEU>`** . **[3 . Đồng tiền thực hiện trong giao dịch mua , bán **[giấy tờ có giá]`<TO_CHUC_DOANH_NGHIEP>`** là đồng Việt Nam .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **12/2021/TT-NHNN** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_BAN_HANH` (span: `[11:14]`)
- `[e3]` **ngày 30 tháng 07 năm 2021** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 3** → `DIEU` (span: `[15:17]`)
- `[e5]` **3 . Đồng tiền thực hiện trong giao dịch mua , bán giấy tờ có giá là đồng Việt Nam .** → `KHOAN` (span: `[18:33]`)
- `[e6]` **giấy tờ có giá** → `TO_CHUC_DOANH_NGHIEP` (span: `[27:29]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 12/2021/TT-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Ngân hàng Nhà nước Việt Nam `[CO_QUAN_BAN_HANH]`)
- (`e1` 12/2021/TT-NHNN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 12/2021/TT-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 30 tháng 07 năm 2021 `[NGAY_BAN_HANH]`)
- (`e4` Điều 3 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 12/2021/TT-NHNN `[SO_HIEU]`)
- (`e5` 3 . Đồng tiền thực hiện trong giao dịch mua , bán giấy tờ có giá là đồng Việt Nam . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 3 `[DIEU]`)


---

### Mẫu #12_2021_TT-NHNN_148636#body_context_42 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[12/2021/TT-NHNN]`<SO_HIEU>`** ban hành **[ngày 30 tháng 07 năm 2021]`<NGAY_BAN_HANH>`** bởi **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_BAN_HANH>`** . **[Điều 3]`<DIEU>`** . **[4 . **[Giấy tờ có giá]`<TO_CHUC_DOANH_NGHIEP>`** được mua , bán thuộc quyền sở hữu hợp pháp của Bên bán và chưa đến hạn thanh toán hết gốc và lãi ; Bên bán có cam kết **[giấy tờ có giá]`<TO_CHUC_DOANH_NGHIEP>`** không có tranh chấp , được phép giao dịch theo quy định của pháp luật , không trong tình trạng đang được chiết khấu , tái chiết khấu .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **12/2021/TT-NHNN** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_BAN_HANH` (span: `[11:14]`)
- `[e3]` **ngày 30 tháng 07 năm 2021** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 3** → `DIEU` (span: `[15:17]`)
- `[e5]` **4 . Giấy tờ có giá được mua , bán thuộc quyền sở hữu hợp pháp của Bên bán và chưa đến hạn thanh toán hết gốc và lãi ; Bên bán có cam kết giấy tờ có giá không có tranh chấp , được phép giao dịch theo quy định của pháp luật , không trong tình trạng đang được chiết khấu , tái chiết khấu .** → `KHOAN` (span: `[18:71]`)
- `[e6]` **Giấy tờ có giá** → `TO_CHUC_DOANH_NGHIEP` (span: `[20:22]`) *(lồng trong `e5` (`KHOAN`))*
- `[e7]` **giấy tờ có giá** → `TO_CHUC_DOANH_NGHIEP` (span: `[47:49]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 12/2021/TT-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Ngân hàng Nhà nước Việt Nam `[CO_QUAN_BAN_HANH]`)
- (`e1` 12/2021/TT-NHNN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 12/2021/TT-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 30 tháng 07 năm 2021 `[NGAY_BAN_HANH]`)
- (`e4` Điều 3 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 12/2021/TT-NHNN `[SO_HIEU]`)
- (`e5` 4 . Giấy tờ có giá được mua , bán thuộc quyền sở hữu hợp pháp của Bên bán và chưa đến hạn thanh toán hết gốc và lãi ; Bên bán có cam kết giấy tờ có giá không có tranh chấp , được phép giao dịch theo quy định của pháp luật , không trong tình trạng đang được chiết khấu , tái chiết khấu . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 3 `[DIEU]`)


---

### Mẫu #12_2021_TT-NHNN_148636#body_standalone_43 (Loại: `body_standalone`)
> **[Điều 3]`<DIEU>`** . **[4 . **[Giấy tờ có giá]`<TO_CHUC_DOANH_NGHIEP>`** được mua , bán thuộc quyền sở hữu hợp pháp của Bên bán và chưa đến hạn thanh toán hết gốc và lãi ; Bên bán có cam kết **[giấy tờ có giá]`<TO_CHUC_DOANH_NGHIEP>`** không có tranh chấp , được phép giao dịch theo quy định của pháp luật , không trong tình trạng đang được chiết khấu , tái chiết khấu .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 3** → `DIEU` (span: `[0:2]`)
- `[e1]` **4 . Giấy tờ có giá được mua , bán thuộc quyền sở hữu hợp pháp của Bên bán và chưa đến hạn thanh toán hết gốc và lãi ; Bên bán có cam kết giấy tờ có giá không có tranh chấp , được phép giao dịch theo quy định của pháp luật , không trong tình trạng đang được chiết khấu , tái chiết khấu .** → `KHOAN` (span: `[3:56]`)
- `[e2]` **Giấy tờ có giá** → `TO_CHUC_DOANH_NGHIEP` (span: `[5:7]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **giấy tờ có giá** → `TO_CHUC_DOANH_NGHIEP` (span: `[32:34]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 4 . Giấy tờ có giá được mua , bán thuộc quyền sở hữu hợp pháp của Bên bán và chưa đến hạn thanh toán hết gốc và lãi ; Bên bán có cam kết giấy tờ có giá không có tranh chấp , được phép giao dịch theo quy định của pháp luật , không trong tình trạng đang được chiết khấu , tái chiết khấu . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 3 `[DIEU]`)


---

### Mẫu #12_2021_TT-NHNN_148636#body_context_44 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[12/2021/TT-NHNN]`<SO_HIEU>`** của **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Chính sách tiền tệ]`<LINH_VUC>`** . **[Điều 3]`<DIEU>`** . **[5 . **[Tổ chức tín dụng , chi nhánh ngân hàng nước ngoài]`<TO_CHUC_DOANH_NGHIEP>`** mua , bán **[trái phiếu]`<TAI_SAN_VAT_CHAT>`** phù hợp với **[quy định tại]`<TU_KHOA_PHAP_LY>`** Luật Các **[tổ chức tín dụng]`<TO_CHUC_DOANH_NGHIEP>`** , Luật **[Chứng khoán]`<TAI_SAN_VAT_CHAT>`** , Nghị định của **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** quy định về phát hành **[trái phiếu doanh nghiệp]`<TAI_SAN_VAT_CHAT>`** , các văn bản khác hướng dẫn Luật **[Chứng khoán]`<TAI_SAN_VAT_CHAT>`** , quy định của pháp luật có liên quan và **[quy định tại]`<TU_KHOA_PHAP_LY>`** **[Thông tư này]`<THAM_CHIEU_PHAP_LY>`** .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **12/2021/TT-NHNN** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_BAN_HANH` (span: `[4:7]`)
- `[e3]` **Chính sách tiền tệ** → `LINH_VUC` (span: `[9:11]`)
- `[e4]` **Điều 3** → `DIEU` (span: `[12:14]`)
- `[e5]` **5 . Tổ chức tín dụng , chi nhánh ngân hàng nước ngoài mua , bán trái phiếu phù hợp với quy định tại Luật Các tổ chức tín dụng , Luật Chứng khoán , Nghị định của Chính phủ quy định về phát hành trái phiếu doanh nghiệp , các văn bản khác hướng dẫn Luật Chứng khoán , quy định của pháp luật có liên quan và quy định tại Thông tư này .** → `KHOAN` (span: `[15:66]`)
- `[e6]` **Tổ chức tín dụng , chi nhánh ngân hàng nước ngoài** → `TO_CHUC_DOANH_NGHIEP` (span: `[17:23]`) *(lồng trong `e5` (`KHOAN`))*
- `[e7]` **Thông tư này** → `THAM_CHIEU_PHAP_LY` (span: `[63:65]`) *(lồng trong `e5` (`KHOAN`))*
- `[e8]` **quy định tại** → `TU_KHOA_PHAP_LY` (span: `[29:31]`) *(lồng trong `e5` (`KHOAN`))*
- `[e9]` **quy định tại** → `TU_KHOA_PHAP_LY` (span: `[61:63]`) *(lồng trong `e5` (`KHOAN`))*
- `[e10]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[41:42]`) *(lồng trong `e5` (`KHOAN`))*
- `[e11]` **tổ chức tín dụng** → `TO_CHUC_DOANH_NGHIEP` (span: `[33:35]`) *(lồng trong `e5` (`KHOAN`))*
- `[e12]` **trái phiếu** → `TAI_SAN_VAT_CHAT` (span: `[26:27]`) *(lồng trong `e5` (`KHOAN`))*
- `[e13]` **Chứng khoán** → `TAI_SAN_VAT_CHAT` (span: `[37:38]`) *(lồng trong `e5` (`KHOAN`))*
- `[e14]` **trái phiếu doanh nghiệp** → `TAI_SAN_VAT_CHAT` (span: `[45:47]`) *(lồng trong `e5` (`KHOAN`))*
- `[e15]` **Chứng khoán** → `TAI_SAN_VAT_CHAT` (span: `[53:54]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 12/2021/TT-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Ngân hàng Nhà nước Việt Nam `[CO_QUAN_BAN_HANH]`)
- (`e1` 12/2021/TT-NHNN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 12/2021/TT-NHNN `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Chính sách tiền tệ `[LINH_VUC]`)
- (`e4` Điều 3 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 12/2021/TT-NHNN `[SO_HIEU]`)
- (`e5` 5 . Tổ chức tín dụng , chi nhánh ngân hàng nước ngoài mua , bán trái phiếu phù hợp với quy định tại Luật Các tổ chức tín dụng , Luật Chứng khoán , Nghị định của Chính phủ quy định về phát hành trái phiếu doanh nghiệp , các văn bản khác hướng dẫn Luật Chứng khoán , quy định của pháp luật có liên quan và quy định tại Thông tư này . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 3 `[DIEU]`)
- (`e1` 12/2021/TT-NHNN `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Chính sách tiền tệ `[LINH_VUC]`)
- (`e5` 5 . Tổ chức tín dụng , chi nhánh ngân hàng nước ngoài mua , bán trái phiếu phù hợp với quy định tại Luật Các tổ chức tín dụng , Luật Chứng khoán , Nghị định của Chính phủ quy định về phát hành trái phiếu doanh nghiệp , các văn bản khác hướng dẫn Luật Chứng khoán , quy định của pháp luật có liên quan và quy định tại Thông tư này . `[KHOAN]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Chính sách tiền tệ `[LINH_VUC]`)
- (`e9` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e7` Thông tư này `[THAM_CHIEU_PHAP_LY]`)
- (`e5` 5 . Tổ chức tín dụng , chi nhánh ngân hàng nước ngoài mua , bán trái phiếu phù hợp với quy định tại Luật Các tổ chức tín dụng , Luật Chứng khoán , Nghị định của Chính phủ quy định về phát hành trái phiếu doanh nghiệp , các văn bản khác hướng dẫn Luật Chứng khoán , quy định của pháp luật có liên quan và quy định tại Thông tư này . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e7` Thông tư này `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #12_2021_TT-NHNN_148636#body_standalone_45 (Loại: `body_standalone`)
> **[Điều 3]`<DIEU>`** . **[5 . **[Tổ chức tín dụng , chi nhánh ngân hàng nước ngoài]`<TO_CHUC_DOANH_NGHIEP>`** mua , bán **[trái phiếu]`<TAI_SAN_VAT_CHAT>`** phù hợp với **[quy định tại]`<TU_KHOA_PHAP_LY>`** Luật Các **[tổ chức tín dụng]`<TO_CHUC_DOANH_NGHIEP>`** , Luật **[Chứng khoán]`<TAI_SAN_VAT_CHAT>`** , Nghị định của **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** quy định về phát hành **[trái phiếu doanh nghiệp]`<TAI_SAN_VAT_CHAT>`** , các văn bản khác hướng dẫn Luật **[Chứng khoán]`<TAI_SAN_VAT_CHAT>`** , quy định của pháp luật có liên quan và **[quy định tại]`<TU_KHOA_PHAP_LY>`** **[Thông tư này]`<THAM_CHIEU_PHAP_LY>`** .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 3** → `DIEU` (span: `[0:2]`)
- `[e1]` **5 . Tổ chức tín dụng , chi nhánh ngân hàng nước ngoài mua , bán trái phiếu phù hợp với quy định tại Luật Các tổ chức tín dụng , Luật Chứng khoán , Nghị định của Chính phủ quy định về phát hành trái phiếu doanh nghiệp , các văn bản khác hướng dẫn Luật Chứng khoán , quy định của pháp luật có liên quan và quy định tại Thông tư này .** → `KHOAN` (span: `[3:54]`)
- `[e2]` **Tổ chức tín dụng , chi nhánh ngân hàng nước ngoài** → `TO_CHUC_DOANH_NGHIEP` (span: `[5:11]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **Thông tư này** → `THAM_CHIEU_PHAP_LY` (span: `[51:53]`) *(lồng trong `e1` (`KHOAN`))*
- `[e4]` **quy định tại** → `TU_KHOA_PHAP_LY` (span: `[17:19]`) *(lồng trong `e1` (`KHOAN`))*
- `[e5]` **quy định tại** → `TU_KHOA_PHAP_LY` (span: `[49:51]`) *(lồng trong `e1` (`KHOAN`))*
- `[e6]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[29:30]`) *(lồng trong `e1` (`KHOAN`))*
- `[e7]` **tổ chức tín dụng** → `TO_CHUC_DOANH_NGHIEP` (span: `[21:23]`) *(lồng trong `e1` (`KHOAN`))*
- `[e8]` **trái phiếu** → `TAI_SAN_VAT_CHAT` (span: `[14:15]`) *(lồng trong `e1` (`KHOAN`))*
- `[e9]` **Chứng khoán** → `TAI_SAN_VAT_CHAT` (span: `[25:26]`) *(lồng trong `e1` (`KHOAN`))*
- `[e10]` **trái phiếu doanh nghiệp** → `TAI_SAN_VAT_CHAT` (span: `[33:35]`) *(lồng trong `e1` (`KHOAN`))*
- `[e11]` **Chứng khoán** → `TAI_SAN_VAT_CHAT` (span: `[41:42]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 5 . Tổ chức tín dụng , chi nhánh ngân hàng nước ngoài mua , bán trái phiếu phù hợp với quy định tại Luật Các tổ chức tín dụng , Luật Chứng khoán , Nghị định của Chính phủ quy định về phát hành trái phiếu doanh nghiệp , các văn bản khác hướng dẫn Luật Chứng khoán , quy định của pháp luật có liên quan và quy định tại Thông tư này . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 3 `[DIEU]`)
- (`e5` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Thông tư này `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 5 . Tổ chức tín dụng , chi nhánh ngân hàng nước ngoài mua , bán trái phiếu phù hợp với quy định tại Luật Các tổ chức tín dụng , Luật Chứng khoán , Nghị định của Chính phủ quy định về phát hành trái phiếu doanh nghiệp , các văn bản khác hướng dẫn Luật Chứng khoán , quy định của pháp luật có liên quan và quy định tại Thông tư này . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Thông tư này `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #12_2021_TT-NHNN_148636#body_context_46 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[12/2021/TT-NHNN]`<SO_HIEU>`** ban hành **[ngày 30 tháng 07 năm 2021]`<NGAY_BAN_HANH>`** bởi **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_BAN_HANH>`** . **[Điều 3]`<DIEU>`** . **[6 . **[Tổ chức tín dụng , chi nhánh ngân hàng nước ngoài]`<TO_CHUC_DOANH_NGHIEP>`** chỉ được mua kỳ phiếu , tín phiếu , **[chứng chỉ tiền gửi]`<GIAY_TO_HO_SO>`** có thời hạn còn lại **[dưới 12 tháng]`<THOI_HAN>`** . Thời hạn còn lại là khoảng thời gian được xác định từ ngày thanh toán tiền mua **[giấy tờ có giá]`<TO_CHUC_DOANH_NGHIEP>`** **[quy định tại]`<TU_KHOA_PHAP_LY>`** **[khoản 3 Điều 4 Thông tư này]`<THAM_CHIEU_PHAP_LY>`** đến ngày đến hạn thanh toán hết gốc , lãi của **[giấy tờ có giá]`<TO_CHUC_DOANH_NGHIEP>`** đó .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **12/2021/TT-NHNN** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_BAN_HANH` (span: `[11:14]`)
- `[e3]` **ngày 30 tháng 07 năm 2021** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 3** → `DIEU` (span: `[15:17]`)
- `[e5]` **6 . Tổ chức tín dụng , chi nhánh ngân hàng nước ngoài chỉ được mua kỳ phiếu , tín phiếu , chứng chỉ tiền gửi có thời hạn còn lại dưới 12 tháng . Thời hạn còn lại là khoảng thời gian được xác định từ ngày thanh toán tiền mua giấy tờ có giá quy định tại khoản 3 Điều 4 Thông tư này đến ngày đến hạn thanh toán hết gốc , lãi của giấy tờ có giá đó .** → `KHOAN` (span: `[18:81]`)
- `[e6]` **Tổ chức tín dụng , chi nhánh ngân hàng nước ngoài** → `TO_CHUC_DOANH_NGHIEP` (span: `[20:26]`) *(lồng trong `e5` (`KHOAN`))*
- `[e7]` **giấy tờ có giá** → `TO_CHUC_DOANH_NGHIEP` (span: `[57:59]`) *(lồng trong `e5` (`KHOAN`))*
- `[e8]` **giấy tờ có giá** → `TO_CHUC_DOANH_NGHIEP` (span: `[77:79]`) *(lồng trong `e5` (`KHOAN`))*
- `[e9]` **khoản 3 Điều 4 Thông tư này** → `THAM_CHIEU_PHAP_LY` (span: `[61:67]`) *(lồng trong `e5` (`KHOAN`))*
- `[e10]` **quy định tại** → `TU_KHOA_PHAP_LY` (span: `[59:61]`) *(lồng trong `e5` (`KHOAN`))*
- `[e11]` **dưới 12 tháng** → `THOI_HAN` (span: `[40:43]`) *(lồng trong `e5` (`KHOAN`))*
- `[e12]` **chứng chỉ tiền gửi** → `GIAY_TO_HO_SO` (span: `[33:36]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 12/2021/TT-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Ngân hàng Nhà nước Việt Nam `[CO_QUAN_BAN_HANH]`)
- (`e1` 12/2021/TT-NHNN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 12/2021/TT-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 30 tháng 07 năm 2021 `[NGAY_BAN_HANH]`)
- (`e4` Điều 3 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 12/2021/TT-NHNN `[SO_HIEU]`)
- (`e5` 6 . Tổ chức tín dụng , chi nhánh ngân hàng nước ngoài chỉ được mua kỳ phiếu , tín phiếu , chứng chỉ tiền gửi có thời hạn còn lại dưới 12 tháng . Thời hạn còn lại là khoảng thời gian được xác định từ ngày thanh toán tiền mua giấy tờ có giá quy định tại khoản 3 Điều 4 Thông tư này đến ngày đến hạn thanh toán hết gốc , lãi của giấy tờ có giá đó . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 3 `[DIEU]`)
- (`e10` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e9` khoản 3 Điều 4 Thông tư này `[THAM_CHIEU_PHAP_LY]`)
- (`e5` 6 . Tổ chức tín dụng , chi nhánh ngân hàng nước ngoài chỉ được mua kỳ phiếu , tín phiếu , chứng chỉ tiền gửi có thời hạn còn lại dưới 12 tháng . Thời hạn còn lại là khoảng thời gian được xác định từ ngày thanh toán tiền mua giấy tờ có giá quy định tại khoản 3 Điều 4 Thông tư này đến ngày đến hạn thanh toán hết gốc , lãi của giấy tờ có giá đó . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e9` khoản 3 Điều 4 Thông tư này `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #12_2021_TT-NHNN_148636#body_standalone_47 (Loại: `body_standalone`)
> **[Điều 3]`<DIEU>`** . **[6 . **[Tổ chức tín dụng , chi nhánh ngân hàng nước ngoài]`<TO_CHUC_DOANH_NGHIEP>`** chỉ được mua kỳ phiếu , tín phiếu , **[chứng chỉ tiền gửi]`<GIAY_TO_HO_SO>`** có thời hạn còn lại **[dưới 12 tháng]`<THOI_HAN>`** . Thời hạn còn lại là khoảng thời gian được xác định từ ngày thanh toán tiền mua **[giấy tờ có giá]`<TO_CHUC_DOANH_NGHIEP>`** **[quy định tại]`<TU_KHOA_PHAP_LY>`** **[khoản 3 Điều 4 Thông tư này]`<THAM_CHIEU_PHAP_LY>`** đến ngày đến hạn thanh toán hết gốc , lãi của **[giấy tờ có giá]`<TO_CHUC_DOANH_NGHIEP>`** đó .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 3** → `DIEU` (span: `[0:2]`)
- `[e1]` **6 . Tổ chức tín dụng , chi nhánh ngân hàng nước ngoài chỉ được mua kỳ phiếu , tín phiếu , chứng chỉ tiền gửi có thời hạn còn lại dưới 12 tháng . Thời hạn còn lại là khoảng thời gian được xác định từ ngày thanh toán tiền mua giấy tờ có giá quy định tại khoản 3 Điều 4 Thông tư này đến ngày đến hạn thanh toán hết gốc , lãi của giấy tờ có giá đó .** → `KHOAN` (span: `[3:66]`)
- `[e2]` **Tổ chức tín dụng , chi nhánh ngân hàng nước ngoài** → `TO_CHUC_DOANH_NGHIEP` (span: `[5:11]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **giấy tờ có giá** → `TO_CHUC_DOANH_NGHIEP` (span: `[42:44]`) *(lồng trong `e1` (`KHOAN`))*
- `[e4]` **giấy tờ có giá** → `TO_CHUC_DOANH_NGHIEP` (span: `[62:64]`) *(lồng trong `e1` (`KHOAN`))*
- `[e5]` **khoản 3 Điều 4 Thông tư này** → `THAM_CHIEU_PHAP_LY` (span: `[46:52]`) *(lồng trong `e1` (`KHOAN`))*
- `[e6]` **quy định tại** → `TU_KHOA_PHAP_LY` (span: `[44:46]`) *(lồng trong `e1` (`KHOAN`))*
- `[e7]` **dưới 12 tháng** → `THOI_HAN` (span: `[25:28]`) *(lồng trong `e1` (`KHOAN`))*
- `[e8]` **chứng chỉ tiền gửi** → `GIAY_TO_HO_SO` (span: `[18:21]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 6 . Tổ chức tín dụng , chi nhánh ngân hàng nước ngoài chỉ được mua kỳ phiếu , tín phiếu , chứng chỉ tiền gửi có thời hạn còn lại dưới 12 tháng . Thời hạn còn lại là khoảng thời gian được xác định từ ngày thanh toán tiền mua giấy tờ có giá quy định tại khoản 3 Điều 4 Thông tư này đến ngày đến hạn thanh toán hết gốc , lãi của giấy tờ có giá đó . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 3 `[DIEU]`)
- (`e6` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e5` khoản 3 Điều 4 Thông tư này `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 6 . Tổ chức tín dụng , chi nhánh ngân hàng nước ngoài chỉ được mua kỳ phiếu , tín phiếu , chứng chỉ tiền gửi có thời hạn còn lại dưới 12 tháng . Thời hạn còn lại là khoảng thời gian được xác định từ ngày thanh toán tiền mua giấy tờ có giá quy định tại khoản 3 Điều 4 Thông tư này đến ngày đến hạn thanh toán hết gốc , lãi của giấy tờ có giá đó . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e5` khoản 3 Điều 4 Thông tư này `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #12_2021_TT-NHNN_148636#body_context_48 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[12/2021/TT-NHNN]`<SO_HIEU>`** của **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Chính sách tiền tệ]`<LINH_VUC>`** . **[Điều 3]`<DIEU>`** . **[7 . **[Chi nhánh ngân hàng nước ngoài]`<TO_CHUC_DOANH_NGHIEP>`** không được mua **[trái phiếu chuyển đổi]`<TAI_SAN_VAT_CHAT>`** .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **12/2021/TT-NHNN** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_BAN_HANH` (span: `[4:7]`)
- `[e3]` **Chính sách tiền tệ** → `LINH_VUC` (span: `[9:11]`)
- `[e4]` **Điều 3** → `DIEU` (span: `[12:14]`)
- `[e5]` **7 . Chi nhánh ngân hàng nước ngoài không được mua trái phiếu chuyển đổi .** → `KHOAN` (span: `[15:26]`)
- `[e6]` **Chi nhánh ngân hàng nước ngoài** → `TO_CHUC_DOANH_NGHIEP` (span: `[17:20]`) *(lồng trong `e5` (`KHOAN`))*
- `[e7]` **trái phiếu chuyển đổi** → `TAI_SAN_VAT_CHAT` (span: `[23:25]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 12/2021/TT-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Ngân hàng Nhà nước Việt Nam `[CO_QUAN_BAN_HANH]`)
- (`e1` 12/2021/TT-NHNN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 12/2021/TT-NHNN `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Chính sách tiền tệ `[LINH_VUC]`)
- (`e4` Điều 3 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 12/2021/TT-NHNN `[SO_HIEU]`)
- (`e5` 7 . Chi nhánh ngân hàng nước ngoài không được mua trái phiếu chuyển đổi . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 3 `[DIEU]`)
- (`e1` 12/2021/TT-NHNN `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Chính sách tiền tệ `[LINH_VUC]`)
- (`e5` 7 . Chi nhánh ngân hàng nước ngoài không được mua trái phiếu chuyển đổi . `[KHOAN]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Chính sách tiền tệ `[LINH_VUC]`)


---

### Mẫu #12_2021_TT-NHNN_148636#body_standalone_49 (Loại: `body_standalone`)
> **[Điều 3]`<DIEU>`** . **[7 . **[Chi nhánh ngân hàng nước ngoài]`<TO_CHUC_DOANH_NGHIEP>`** không được mua **[trái phiếu chuyển đổi]`<TAI_SAN_VAT_CHAT>`** .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 3** → `DIEU` (span: `[0:2]`)
- `[e1]` **7 . Chi nhánh ngân hàng nước ngoài không được mua trái phiếu chuyển đổi .** → `KHOAN` (span: `[3:14]`)
- `[e2]` **Chi nhánh ngân hàng nước ngoài** → `TO_CHUC_DOANH_NGHIEP` (span: `[5:8]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **trái phiếu chuyển đổi** → `TAI_SAN_VAT_CHAT` (span: `[11:13]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 7 . Chi nhánh ngân hàng nước ngoài không được mua trái phiếu chuyển đổi . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 3 `[DIEU]`)


---

### Mẫu #12_2021_TT-NHNN_148636#body_context_50 (Loại: `body_context`)
> **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[12/2021/TT-NHNN]`<SO_HIEU>`** . **[Điều 3]`<DIEU>`** . **[8 . Đối với **[giấy tờ có giá]`<TO_CHUC_DOANH_NGHIEP>`** của **[công ty tài chính]`<TO_CHUC_DOANH_NGHIEP>`** hoặc **[công ty cho thuê tài chính]`<TO_CHUC_DOANH_NGHIEP>`** phát hành , **[tổ chức tín dụng , chi nhánh ngân hàng nước ngoài]`<TO_CHUC_DOANH_NGHIEP>`** chỉ được mua , bán với tổ chức ( bao gồm cả **[tổ chức tín dụng , chi nhánh ngân hàng nước ngoài]`<TO_CHUC_DOANH_NGHIEP>`** ) .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[4:5]`)
- `[e1]` **12/2021/TT-NHNN** → `SO_HIEU` (span: `[6:7]`)
- `[e2]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_BAN_HANH` (span: `[0:3]`)
- `[e3]` **Điều 3** → `DIEU` (span: `[8:10]`)
- `[e4]` **8 . Đối với giấy tờ có giá của công ty tài chính hoặc công ty cho thuê tài chính phát hành , tổ chức tín dụng , chi nhánh ngân hàng nước ngoài chỉ được mua , bán với tổ chức ( bao gồm cả tổ chức tín dụng , chi nhánh ngân hàng nước ngoài ) .** → `KHOAN` (span: `[11:50]`)
- `[e5]` **tổ chức tín dụng , chi nhánh ngân hàng nước ngoài** → `TO_CHUC_DOANH_NGHIEP` (span: `[26:32]`) *(lồng trong `e4` (`KHOAN`))*
- `[e6]` **tổ chức tín dụng , chi nhánh ngân hàng nước ngoài** → `TO_CHUC_DOANH_NGHIEP` (span: `[42:48]`) *(lồng trong `e4` (`KHOAN`))*
- `[e7]` **công ty tài chính** → `TO_CHUC_DOANH_NGHIEP` (span: `[17:19]`) *(lồng trong `e4` (`KHOAN`))*
- `[e8]` **giấy tờ có giá** → `TO_CHUC_DOANH_NGHIEP` (span: `[14:16]`) *(lồng trong `e4` (`KHOAN`))*
- `[e9]` **công ty cho thuê tài chính** → `TO_CHUC_DOANH_NGHIEP` (span: `[20:24]`) *(lồng trong `e4` (`KHOAN`))*

**Quan hệ:**
- (`e1` 12/2021/TT-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Ngân hàng Nhà nước Việt Nam `[CO_QUAN_BAN_HANH]`)
- (`e1` 12/2021/TT-NHNN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 3 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 12/2021/TT-NHNN `[SO_HIEU]`)
- (`e4` 8 . Đối với giấy tờ có giá của công ty tài chính hoặc công ty cho thuê tài chính phát hành , tổ chức tín dụng , chi nhánh ngân hàng nước ngoài chỉ được mua , bán với tổ chức ( bao gồm cả tổ chức tín dụng , chi nhánh ngân hàng nước ngoài ) . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 3 `[DIEU]`)


---

### Mẫu #12_2021_TT-NHNN_148636#body_standalone_51 (Loại: `body_standalone`)
> **[Điều 3]`<DIEU>`** . **[8 . Đối với **[giấy tờ có giá]`<TO_CHUC_DOANH_NGHIEP>`** của **[công ty tài chính]`<TO_CHUC_DOANH_NGHIEP>`** hoặc **[công ty cho thuê tài chính]`<TO_CHUC_DOANH_NGHIEP>`** phát hành , **[tổ chức tín dụng , chi nhánh ngân hàng nước ngoài]`<TO_CHUC_DOANH_NGHIEP>`** chỉ được mua , bán với tổ chức ( bao gồm cả **[tổ chức tín dụng , chi nhánh ngân hàng nước ngoài]`<TO_CHUC_DOANH_NGHIEP>`** ) .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 3** → `DIEU` (span: `[0:2]`)
- `[e1]` **8 . Đối với giấy tờ có giá của công ty tài chính hoặc công ty cho thuê tài chính phát hành , tổ chức tín dụng , chi nhánh ngân hàng nước ngoài chỉ được mua , bán với tổ chức ( bao gồm cả tổ chức tín dụng , chi nhánh ngân hàng nước ngoài ) .** → `KHOAN` (span: `[3:42]`)
- `[e2]` **tổ chức tín dụng , chi nhánh ngân hàng nước ngoài** → `TO_CHUC_DOANH_NGHIEP` (span: `[18:24]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **tổ chức tín dụng , chi nhánh ngân hàng nước ngoài** → `TO_CHUC_DOANH_NGHIEP` (span: `[34:40]`) *(lồng trong `e1` (`KHOAN`))*
- `[e4]` **công ty tài chính** → `TO_CHUC_DOANH_NGHIEP` (span: `[9:11]`) *(lồng trong `e1` (`KHOAN`))*
- `[e5]` **giấy tờ có giá** → `TO_CHUC_DOANH_NGHIEP` (span: `[6:8]`) *(lồng trong `e1` (`KHOAN`))*
- `[e6]` **công ty cho thuê tài chính** → `TO_CHUC_DOANH_NGHIEP` (span: `[12:16]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 8 . Đối với giấy tờ có giá của công ty tài chính hoặc công ty cho thuê tài chính phát hành , tổ chức tín dụng , chi nhánh ngân hàng nước ngoài chỉ được mua , bán với tổ chức ( bao gồm cả tổ chức tín dụng , chi nhánh ngân hàng nước ngoài ) . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 3 `[DIEU]`)


---

### Mẫu #12_2021_TT-NHNN_148636#body_context_52 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[12/2021/TT-NHNN]`<SO_HIEU>`** ban hành **[ngày 30 tháng 07 năm 2021]`<NGAY_BAN_HANH>`** bởi **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_BAN_HANH>`** . **[Điều 4 . Thông tin giao dịch . Mọi giao dịch mua , bán **[giấy tờ có giá]`<TO_CHUC_DOANH_NGHIEP>`** phải được thể hiện bằng hình thức giao dịch phù hợp với quy định của pháp luật có liên quan . Thỏa thuận về mua , bán **[giấy tờ có giá]`<TO_CHUC_DOANH_NGHIEP>`** phải bao gồm tối thiểu các nội dung sau :]`<DIEU>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **12/2021/TT-NHNN** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_BAN_HANH` (span: `[11:14]`)
- `[e3]` **ngày 30 tháng 07 năm 2021** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 4 . Thông tin giao dịch . Mọi giao dịch mua , bán giấy tờ có giá phải được thể hiện bằng hình thức giao dịch phù hợp với quy định của pháp luật có liên quan . Thỏa thuận về mua , bán giấy tờ có giá phải bao gồm tối thiểu các nội dung sau :** → `DIEU` (span: `[15:56]`)
- `[e5]` **giấy tờ có giá** → `TO_CHUC_DOANH_NGHIEP` (span: `[26:28]`) *(lồng trong `e4` (`DIEU`))*
- `[e6]` **giấy tờ có giá** → `TO_CHUC_DOANH_NGHIEP` (span: `[47:49]`) *(lồng trong `e4` (`DIEU`))*

**Quan hệ:**
- (`e1` 12/2021/TT-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Ngân hàng Nhà nước Việt Nam `[CO_QUAN_BAN_HANH]`)
- (`e1` 12/2021/TT-NHNN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 12/2021/TT-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 30 tháng 07 năm 2021 `[NGAY_BAN_HANH]`)
- (`e4` Điều 4 . Thông tin giao dịch . Mọi giao dịch mua , bán giấy tờ có giá phải được thể hiện bằng hình thức giao dịch phù hợp với quy định của pháp luật có liên quan . Thỏa thuận về mua , bán giấy tờ có giá phải bao gồm tối thiểu các nội dung sau : `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 12/2021/TT-NHNN `[SO_HIEU]`)


---

### Mẫu #12_2021_TT-NHNN_148636#body_context_53 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[12/2021/TT-NHNN]`<SO_HIEU>`** của **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Chính sách tiền tệ]`<LINH_VUC>`** . **[Điều 4]`<DIEU>`** . **[1 . Thông tin về Bên bán , Bên mua .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **12/2021/TT-NHNN** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_BAN_HANH` (span: `[4:7]`)
- `[e3]` **Chính sách tiền tệ** → `LINH_VUC` (span: `[9:11]`)
- `[e4]` **Điều 4** → `DIEU` (span: `[12:14]`)
- `[e5]` **1 . Thông tin về Bên bán , Bên mua .** → `KHOAN` (span: `[15:25]`)

**Quan hệ:**
- (`e1` 12/2021/TT-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Ngân hàng Nhà nước Việt Nam `[CO_QUAN_BAN_HANH]`)
- (`e1` 12/2021/TT-NHNN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 12/2021/TT-NHNN `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Chính sách tiền tệ `[LINH_VUC]`)
- (`e4` Điều 4 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 12/2021/TT-NHNN `[SO_HIEU]`)
- (`e5` 1 . Thông tin về Bên bán , Bên mua . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 4 `[DIEU]`)
- (`e1` 12/2021/TT-NHNN `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Chính sách tiền tệ `[LINH_VUC]`)
- (`e5` 1 . Thông tin về Bên bán , Bên mua . `[KHOAN]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Chính sách tiền tệ `[LINH_VUC]`)


---

### Mẫu #12_2021_TT-NHNN_148636#body_context_54 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[12/2021/TT-NHNN]`<SO_HIEU>`** của **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Chính sách tiền tệ]`<LINH_VUC>`** . **[Điều 4]`<DIEU>`** . **[2 . Tên gọi **[giấy tờ có giá]`<TO_CHUC_DOANH_NGHIEP>`** ; **[tổ chức tín dụng , chi nhánh ngân hàng nước ngoài]`<TO_CHUC_DOANH_NGHIEP>`** phát hành ; thời hạn **[giấy tờ có giá]`<TO_CHUC_DOANH_NGHIEP>`** ; ngày đến hạn thanh toán hết gốc , lãi của **[giấy tờ có giá]`<TO_CHUC_DOANH_NGHIEP>`** ; giá trị theo mệnh giá **[giấy tờ có giá]`<TO_CHUC_DOANH_NGHIEP>`** .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **12/2021/TT-NHNN** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_BAN_HANH` (span: `[4:7]`)
- `[e3]` **Chính sách tiền tệ** → `LINH_VUC` (span: `[9:11]`)
- `[e4]` **Điều 4** → `DIEU` (span: `[12:14]`)
- `[e5]` **2 . Tên gọi giấy tờ có giá ; tổ chức tín dụng , chi nhánh ngân hàng nước ngoài phát hành ; thời hạn giấy tờ có giá ; ngày đến hạn thanh toán hết gốc , lãi của giấy tờ có giá ; giá trị theo mệnh giá giấy tờ có giá .** → `KHOAN` (span: `[15:52]`)
- `[e6]` **tổ chức tín dụng , chi nhánh ngân hàng nước ngoài** → `TO_CHUC_DOANH_NGHIEP` (span: `[22:28]`) *(lồng trong `e5` (`KHOAN`))*
- `[e7]` **giấy tờ có giá** → `TO_CHUC_DOANH_NGHIEP` (span: `[19:21]`) *(lồng trong `e5` (`KHOAN`))*
- `[e8]` **giấy tờ có giá** → `TO_CHUC_DOANH_NGHIEP` (span: `[31:33]`) *(lồng trong `e5` (`KHOAN`))*
- `[e9]` **giấy tờ có giá** → `TO_CHUC_DOANH_NGHIEP` (span: `[43:45]`) *(lồng trong `e5` (`KHOAN`))*
- `[e10]` **giấy tờ có giá** → `TO_CHUC_DOANH_NGHIEP` (span: `[49:51]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 12/2021/TT-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Ngân hàng Nhà nước Việt Nam `[CO_QUAN_BAN_HANH]`)
- (`e1` 12/2021/TT-NHNN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 12/2021/TT-NHNN `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Chính sách tiền tệ `[LINH_VUC]`)
- (`e4` Điều 4 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 12/2021/TT-NHNN `[SO_HIEU]`)
- (`e5` 2 . Tên gọi giấy tờ có giá ; tổ chức tín dụng , chi nhánh ngân hàng nước ngoài phát hành ; thời hạn giấy tờ có giá ; ngày đến hạn thanh toán hết gốc , lãi của giấy tờ có giá ; giá trị theo mệnh giá giấy tờ có giá . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 4 `[DIEU]`)
- (`e1` 12/2021/TT-NHNN `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Chính sách tiền tệ `[LINH_VUC]`)
- (`e5` 2 . Tên gọi giấy tờ có giá ; tổ chức tín dụng , chi nhánh ngân hàng nước ngoài phát hành ; thời hạn giấy tờ có giá ; ngày đến hạn thanh toán hết gốc , lãi của giấy tờ có giá ; giá trị theo mệnh giá giấy tờ có giá . `[KHOAN]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Chính sách tiền tệ `[LINH_VUC]`)


---

### Mẫu #12_2021_TT-NHNN_148636#body_standalone_55 (Loại: `body_standalone`)
> **[Điều 4]`<DIEU>`** . **[2 . Tên gọi **[giấy tờ có giá]`<TO_CHUC_DOANH_NGHIEP>`** ; **[tổ chức tín dụng , chi nhánh ngân hàng nước ngoài]`<TO_CHUC_DOANH_NGHIEP>`** phát hành ; thời hạn **[giấy tờ có giá]`<TO_CHUC_DOANH_NGHIEP>`** ; ngày đến hạn thanh toán hết gốc , lãi của **[giấy tờ có giá]`<TO_CHUC_DOANH_NGHIEP>`** ; giá trị theo mệnh giá **[giấy tờ có giá]`<TO_CHUC_DOANH_NGHIEP>`** .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 4** → `DIEU` (span: `[0:2]`)
- `[e1]` **2 . Tên gọi giấy tờ có giá ; tổ chức tín dụng , chi nhánh ngân hàng nước ngoài phát hành ; thời hạn giấy tờ có giá ; ngày đến hạn thanh toán hết gốc , lãi của giấy tờ có giá ; giá trị theo mệnh giá giấy tờ có giá .** → `KHOAN` (span: `[3:40]`)
- `[e2]` **tổ chức tín dụng , chi nhánh ngân hàng nước ngoài** → `TO_CHUC_DOANH_NGHIEP` (span: `[10:16]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **giấy tờ có giá** → `TO_CHUC_DOANH_NGHIEP` (span: `[7:9]`) *(lồng trong `e1` (`KHOAN`))*
- `[e4]` **giấy tờ có giá** → `TO_CHUC_DOANH_NGHIEP` (span: `[19:21]`) *(lồng trong `e1` (`KHOAN`))*
- `[e5]` **giấy tờ có giá** → `TO_CHUC_DOANH_NGHIEP` (span: `[31:33]`) *(lồng trong `e1` (`KHOAN`))*
- `[e6]` **giấy tờ có giá** → `TO_CHUC_DOANH_NGHIEP` (span: `[37:39]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 2 . Tên gọi giấy tờ có giá ; tổ chức tín dụng , chi nhánh ngân hàng nước ngoài phát hành ; thời hạn giấy tờ có giá ; ngày đến hạn thanh toán hết gốc , lãi của giấy tờ có giá ; giá trị theo mệnh giá giấy tờ có giá . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 4 `[DIEU]`)


---

### Mẫu #12_2021_TT-NHNN_148636#body_context_56 (Loại: `body_context`)
> **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[12/2021/TT-NHNN]`<SO_HIEU>`** . **[Điều 4]`<DIEU>`** . **[3 . Ngày thanh toán tiền mua **[giấy tờ có giá]`<TO_CHUC_DOANH_NGHIEP>`** .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[4:5]`)
- `[e1]` **12/2021/TT-NHNN** → `SO_HIEU` (span: `[6:7]`)
- `[e2]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_BAN_HANH` (span: `[0:3]`)
- `[e3]` **Điều 4** → `DIEU` (span: `[8:10]`)
- `[e4]` **3 . Ngày thanh toán tiền mua giấy tờ có giá .** → `KHOAN` (span: `[11:20]`)
- `[e5]` **giấy tờ có giá** → `TO_CHUC_DOANH_NGHIEP` (span: `[17:19]`) *(lồng trong `e4` (`KHOAN`))*

**Quan hệ:**
- (`e1` 12/2021/TT-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Ngân hàng Nhà nước Việt Nam `[CO_QUAN_BAN_HANH]`)
- (`e1` 12/2021/TT-NHNN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 4 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 12/2021/TT-NHNN `[SO_HIEU]`)
- (`e4` 3 . Ngày thanh toán tiền mua giấy tờ có giá . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 4 `[DIEU]`)


---

### Mẫu #12_2021_TT-NHNN_148636#body_context_57 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[12/2021/TT-NHNN]`<SO_HIEU>`** của **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Chính sách tiền tệ]`<LINH_VUC>`** . **[Điều 4]`<DIEU>`** . **[4 . Số tiền thanh toán tiền mua **[giấy tờ có giá]`<TO_CHUC_DOANH_NGHIEP>`** .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **12/2021/TT-NHNN** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_BAN_HANH` (span: `[4:7]`)
- `[e3]` **Chính sách tiền tệ** → `LINH_VUC` (span: `[9:11]`)
- `[e4]` **Điều 4** → `DIEU` (span: `[12:14]`)
- `[e5]` **4 . Số tiền thanh toán tiền mua giấy tờ có giá .** → `KHOAN` (span: `[15:25]`)
- `[e6]` **giấy tờ có giá** → `TO_CHUC_DOANH_NGHIEP` (span: `[22:24]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 12/2021/TT-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Ngân hàng Nhà nước Việt Nam `[CO_QUAN_BAN_HANH]`)
- (`e1` 12/2021/TT-NHNN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 12/2021/TT-NHNN `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Chính sách tiền tệ `[LINH_VUC]`)
- (`e4` Điều 4 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 12/2021/TT-NHNN `[SO_HIEU]`)
- (`e5` 4 . Số tiền thanh toán tiền mua giấy tờ có giá . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 4 `[DIEU]`)
- (`e1` 12/2021/TT-NHNN `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Chính sách tiền tệ `[LINH_VUC]`)
- (`e5` 4 . Số tiền thanh toán tiền mua giấy tờ có giá . `[KHOAN]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Chính sách tiền tệ `[LINH_VUC]`)


---

### Mẫu #12_2021_TT-NHNN_148636#body_context_58 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[12/2021/TT-NHNN]`<SO_HIEU>`** ban hành **[ngày 30 tháng 07 năm 2021]`<NGAY_BAN_HANH>`** bởi **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_BAN_HANH>`** . **[Điều 4]`<DIEU>`** . **[5 . Quyền và nghĩa vụ của Bên bán , Bên mua .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **12/2021/TT-NHNN** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_BAN_HANH` (span: `[11:14]`)
- `[e3]` **ngày 30 tháng 07 năm 2021** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 4** → `DIEU` (span: `[15:17]`)
- `[e5]` **5 . Quyền và nghĩa vụ của Bên bán , Bên mua .** → `KHOAN` (span: `[18:30]`)

**Quan hệ:**
- (`e1` 12/2021/TT-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Ngân hàng Nhà nước Việt Nam `[CO_QUAN_BAN_HANH]`)
- (`e1` 12/2021/TT-NHNN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 12/2021/TT-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 30 tháng 07 năm 2021 `[NGAY_BAN_HANH]`)
- (`e4` Điều 4 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 12/2021/TT-NHNN `[SO_HIEU]`)
- (`e5` 5 . Quyền và nghĩa vụ của Bên bán , Bên mua . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 4 `[DIEU]`)


---

### Mẫu #12_2021_TT-NHNN_148636#body_standalone_59 (Loại: `body_standalone`)
> **[Điều 4]`<DIEU>`** . **[5 . Quyền và nghĩa vụ của Bên bán , Bên mua .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 4** → `DIEU` (span: `[0:2]`)
- `[e1]` **5 . Quyền và nghĩa vụ của Bên bán , Bên mua .** → `KHOAN` (span: `[3:15]`)

**Quan hệ:**
- (`e1` 5 . Quyền và nghĩa vụ của Bên bán , Bên mua . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 4 `[DIEU]`)


---

### Mẫu #12_2021_TT-NHNN_148636#body_context_60 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[12/2021/TT-NHNN]`<SO_HIEU>`** ban hành **[ngày 30 tháng 07 năm 2021]`<NGAY_BAN_HANH>`** bởi **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_BAN_HANH>`** . **[Điều 5 . Quy định nội bộ]`<DIEU>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **12/2021/TT-NHNN** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_BAN_HANH` (span: `[11:14]`)
- `[e3]` **ngày 30 tháng 07 năm 2021** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 5 . Quy định nội bộ** → `DIEU` (span: `[15:20]`)

**Quan hệ:**
- (`e1` 12/2021/TT-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Ngân hàng Nhà nước Việt Nam `[CO_QUAN_BAN_HANH]`)
- (`e1` 12/2021/TT-NHNN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 12/2021/TT-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 30 tháng 07 năm 2021 `[NGAY_BAN_HANH]`)
- (`e4` Điều 5 . Quy định nội bộ `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 12/2021/TT-NHNN `[SO_HIEU]`)


---

### Mẫu #12_2021_TT-NHNN_148636#body_context_61 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[12/2021/TT-NHNN]`<SO_HIEU>`** của **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Chính sách tiền tệ]`<LINH_VUC>`** . **[Điều 5]`<DIEU>`** . **[1 . Căn cứ **[quy định tại]`<TU_KHOA_PHAP_LY>`** Luật Các **[tổ chức tín dụng]`<TO_CHUC_DOANH_NGHIEP>`** , Thông tư này và quy định của pháp luật có liên quan , **[tổ chức tín dụng , chi nhánh ngân hàng nước ngoài]`<TO_CHUC_DOANH_NGHIEP>`** ban hành Quy định nội bộ về mua , bán **[giấy tờ có giá]`<TO_CHUC_DOANH_NGHIEP>`** phù hợp với mô hình quản lý , đặc điểm , điều kiện kinh doanh , đảm bảo an toàn hoạt động cho **[tổ chức tín dụng , chi nhánh ngân hàng nước ngoài]`<TO_CHUC_DOANH_NGHIEP>`** .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **12/2021/TT-NHNN** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_BAN_HANH` (span: `[4:7]`)
- `[e3]` **Chính sách tiền tệ** → `LINH_VUC` (span: `[9:11]`)
- `[e4]` **Điều 5** → `DIEU` (span: `[12:14]`)
- `[e5]` **1 . Căn cứ quy định tại Luật Các tổ chức tín dụng , Thông tư này và quy định của pháp luật có liên quan , tổ chức tín dụng , chi nhánh ngân hàng nước ngoài ban hành Quy định nội bộ về mua , bán giấy tờ có giá phù hợp với mô hình quản lý , đặc điểm , điều kiện kinh doanh , đảm bảo an toàn hoạt động cho tổ chức tín dụng , chi nhánh ngân hàng nước ngoài .** → `KHOAN` (span: `[15:69]`)
- `[e6]` **tổ chức tín dụng , chi nhánh ngân hàng nước ngoài** → `TO_CHUC_DOANH_NGHIEP` (span: `[34:40]`) *(lồng trong `e5` (`KHOAN`))*
- `[e7]` **tổ chức tín dụng , chi nhánh ngân hàng nước ngoài** → `TO_CHUC_DOANH_NGHIEP` (span: `[62:68]`) *(lồng trong `e5` (`KHOAN`))*
- `[e8]` **giấy tờ có giá** → `TO_CHUC_DOANH_NGHIEP` (span: `[47:49]`) *(lồng trong `e5` (`KHOAN`))*
- `[e9]` **quy định tại** → `TU_KHOA_PHAP_LY` (span: `[18:20]`) *(lồng trong `e5` (`KHOAN`))*
- `[e10]` **tổ chức tín dụng** → `TO_CHUC_DOANH_NGHIEP` (span: `[22:24]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 12/2021/TT-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Ngân hàng Nhà nước Việt Nam `[CO_QUAN_BAN_HANH]`)
- (`e1` 12/2021/TT-NHNN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 12/2021/TT-NHNN `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Chính sách tiền tệ `[LINH_VUC]`)
- (`e4` Điều 5 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 12/2021/TT-NHNN `[SO_HIEU]`)
- (`e5` 1 . Căn cứ quy định tại Luật Các tổ chức tín dụng , Thông tư này và quy định của pháp luật có liên quan , tổ chức tín dụng , chi nhánh ngân hàng nước ngoài ban hành Quy định nội bộ về mua , bán giấy tờ có giá phù hợp với mô hình quản lý , đặc điểm , điều kiện kinh doanh , đảm bảo an toàn hoạt động cho tổ chức tín dụng , chi nhánh ngân hàng nước ngoài . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 5 `[DIEU]`)
- (`e1` 12/2021/TT-NHNN `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Chính sách tiền tệ `[LINH_VUC]`)
- (`e5` 1 . Căn cứ quy định tại Luật Các tổ chức tín dụng , Thông tư này và quy định của pháp luật có liên quan , tổ chức tín dụng , chi nhánh ngân hàng nước ngoài ban hành Quy định nội bộ về mua , bán giấy tờ có giá phù hợp với mô hình quản lý , đặc điểm , điều kiện kinh doanh , đảm bảo an toàn hoạt động cho tổ chức tín dụng , chi nhánh ngân hàng nước ngoài . `[KHOAN]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Chính sách tiền tệ `[LINH_VUC]`)


---

### Mẫu #12_2021_TT-NHNN_148636#body_standalone_62 (Loại: `body_standalone`)
> **[Điều 5]`<DIEU>`** . **[1 . Căn cứ **[quy định tại]`<TU_KHOA_PHAP_LY>`** Luật Các **[tổ chức tín dụng]`<TO_CHUC_DOANH_NGHIEP>`** , Thông tư này và quy định của pháp luật có liên quan , **[tổ chức tín dụng , chi nhánh ngân hàng nước ngoài]`<TO_CHUC_DOANH_NGHIEP>`** ban hành Quy định nội bộ về mua , bán **[giấy tờ có giá]`<TO_CHUC_DOANH_NGHIEP>`** phù hợp với mô hình quản lý , đặc điểm , điều kiện kinh doanh , đảm bảo an toàn hoạt động cho **[tổ chức tín dụng , chi nhánh ngân hàng nước ngoài]`<TO_CHUC_DOANH_NGHIEP>`** .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 5** → `DIEU` (span: `[0:2]`)
- `[e1]` **1 . Căn cứ quy định tại Luật Các tổ chức tín dụng , Thông tư này và quy định của pháp luật có liên quan , tổ chức tín dụng , chi nhánh ngân hàng nước ngoài ban hành Quy định nội bộ về mua , bán giấy tờ có giá phù hợp với mô hình quản lý , đặc điểm , điều kiện kinh doanh , đảm bảo an toàn hoạt động cho tổ chức tín dụng , chi nhánh ngân hàng nước ngoài .** → `KHOAN` (span: `[3:57]`)
- `[e2]` **tổ chức tín dụng , chi nhánh ngân hàng nước ngoài** → `TO_CHUC_DOANH_NGHIEP` (span: `[22:28]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **tổ chức tín dụng , chi nhánh ngân hàng nước ngoài** → `TO_CHUC_DOANH_NGHIEP` (span: `[50:56]`) *(lồng trong `e1` (`KHOAN`))*
- `[e4]` **giấy tờ có giá** → `TO_CHUC_DOANH_NGHIEP` (span: `[35:37]`) *(lồng trong `e1` (`KHOAN`))*
- `[e5]` **quy định tại** → `TU_KHOA_PHAP_LY` (span: `[6:8]`) *(lồng trong `e1` (`KHOAN`))*
- `[e6]` **tổ chức tín dụng** → `TO_CHUC_DOANH_NGHIEP` (span: `[10:12]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 1 . Căn cứ quy định tại Luật Các tổ chức tín dụng , Thông tư này và quy định của pháp luật có liên quan , tổ chức tín dụng , chi nhánh ngân hàng nước ngoài ban hành Quy định nội bộ về mua , bán giấy tờ có giá phù hợp với mô hình quản lý , đặc điểm , điều kiện kinh doanh , đảm bảo an toàn hoạt động cho tổ chức tín dụng , chi nhánh ngân hàng nước ngoài . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 5 `[DIEU]`)


---

### Mẫu #12_2021_TT-NHNN_148636#body_context_63 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[12/2021/TT-NHNN]`<SO_HIEU>`** của **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Chính sách tiền tệ]`<LINH_VUC>`** . **[Điều 5]`<DIEU>`** . **[2 . Quy định nội bộ phải quy định rõ trách nhiệm và nghĩa vụ của từng bộ phận , cá nhân có liên quan đến việc thực hiện giao dịch mua , bán **[giấy tờ có giá]`<TO_CHUC_DOANH_NGHIEP>`** .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **12/2021/TT-NHNN** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_BAN_HANH` (span: `[4:7]`)
- `[e3]` **Chính sách tiền tệ** → `LINH_VUC` (span: `[9:11]`)
- `[e4]` **Điều 5** → `DIEU` (span: `[12:14]`)
- `[e5]` **2 . Quy định nội bộ phải quy định rõ trách nhiệm và nghĩa vụ của từng bộ phận , cá nhân có liên quan đến việc thực hiện giao dịch mua , bán giấy tờ có giá .** → `KHOAN` (span: `[15:42]`)
- `[e6]` **giấy tờ có giá** → `TO_CHUC_DOANH_NGHIEP` (span: `[39:41]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 12/2021/TT-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Ngân hàng Nhà nước Việt Nam `[CO_QUAN_BAN_HANH]`)
- (`e1` 12/2021/TT-NHNN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 12/2021/TT-NHNN `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Chính sách tiền tệ `[LINH_VUC]`)
- (`e4` Điều 5 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 12/2021/TT-NHNN `[SO_HIEU]`)
- (`e5` 2 . Quy định nội bộ phải quy định rõ trách nhiệm và nghĩa vụ của từng bộ phận , cá nhân có liên quan đến việc thực hiện giao dịch mua , bán giấy tờ có giá . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 5 `[DIEU]`)
- (`e1` 12/2021/TT-NHNN `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Chính sách tiền tệ `[LINH_VUC]`)
- (`e5` 2 . Quy định nội bộ phải quy định rõ trách nhiệm và nghĩa vụ của từng bộ phận , cá nhân có liên quan đến việc thực hiện giao dịch mua , bán giấy tờ có giá . `[KHOAN]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Chính sách tiền tệ `[LINH_VUC]`)


---

### Mẫu #12_2021_TT-NHNN_148636#body_context_64 (Loại: `body_context`)
> **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[12/2021/TT-NHNN]`<SO_HIEU>`** . **[Điều 5]`<DIEU>`** . **[3 . Quy định nội bộ tối thiểu phải có quy trình nghiệp vụ và quy định quản lý rủi ro đối với hoạt động mua , bán **[giấy tờ có giá]`<TO_CHUC_DOANH_NGHIEP>`** .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[4:5]`)
- `[e1]` **12/2021/TT-NHNN** → `SO_HIEU` (span: `[6:7]`)
- `[e2]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_BAN_HANH` (span: `[0:3]`)
- `[e3]` **Điều 5** → `DIEU` (span: `[8:10]`)
- `[e4]` **3 . Quy định nội bộ tối thiểu phải có quy trình nghiệp vụ và quy định quản lý rủi ro đối với hoạt động mua , bán giấy tờ có giá .** → `KHOAN` (span: `[11:32]`)
- `[e5]` **giấy tờ có giá** → `TO_CHUC_DOANH_NGHIEP` (span: `[29:31]`) *(lồng trong `e4` (`KHOAN`))*

**Quan hệ:**
- (`e1` 12/2021/TT-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Ngân hàng Nhà nước Việt Nam `[CO_QUAN_BAN_HANH]`)
- (`e1` 12/2021/TT-NHNN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 5 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 12/2021/TT-NHNN `[SO_HIEU]`)
- (`e4` 3 . Quy định nội bộ tối thiểu phải có quy trình nghiệp vụ và quy định quản lý rủi ro đối với hoạt động mua , bán giấy tờ có giá . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 5 `[DIEU]`)


---

### Mẫu #12_2021_TT-NHNN_148636#body_context_65 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[12/2021/TT-NHNN]`<SO_HIEU>`** của **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Chính sách tiền tệ]`<LINH_VUC>`** . **[Điều 6 . Điều khoản thi hành]`<DIEU>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **12/2021/TT-NHNN** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_BAN_HANH` (span: `[4:7]`)
- `[e3]` **Chính sách tiền tệ** → `LINH_VUC` (span: `[9:11]`)
- `[e4]` **Điều 6 . Điều khoản thi hành** → `DIEU` (span: `[12:17]`)

**Quan hệ:**
- (`e1` 12/2021/TT-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Ngân hàng Nhà nước Việt Nam `[CO_QUAN_BAN_HANH]`)
- (`e1` 12/2021/TT-NHNN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 12/2021/TT-NHNN `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Chính sách tiền tệ `[LINH_VUC]`)
- (`e4` Điều 6 . Điều khoản thi hành `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 12/2021/TT-NHNN `[SO_HIEU]`)
- (`e1` 12/2021/TT-NHNN `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Chính sách tiền tệ `[LINH_VUC]`)
- (`e4` Điều 6 . Điều khoản thi hành `[DIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Chính sách tiền tệ `[LINH_VUC]`)


---

### Mẫu #12_2021_TT-NHNN_148636#body_context_66 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[12/2021/TT-NHNN]`<SO_HIEU>`** ban hành **[ngày 30 tháng 07 năm 2021]`<NGAY_BAN_HANH>`** bởi **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_BAN_HANH>`** . **[Điều 6]`<DIEU>`** . **[1 . Thông tư này có hiệu lực thi hành kể từ ngày 27 tháng 10 năm 2021 .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **12/2021/TT-NHNN** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_BAN_HANH` (span: `[11:14]`)
- `[e3]` **ngày 30 tháng 07 năm 2021** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 6** → `DIEU` (span: `[15:17]`)
- `[e5]` **1 . Thông tư này có hiệu lực thi hành kể từ ngày 27 tháng 10 năm 2021 .** → `KHOAN` (span: `[18:34]`)

**Quan hệ:**
- (`e1` 12/2021/TT-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Ngân hàng Nhà nước Việt Nam `[CO_QUAN_BAN_HANH]`)
- (`e1` 12/2021/TT-NHNN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 12/2021/TT-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 30 tháng 07 năm 2021 `[NGAY_BAN_HANH]`)
- (`e4` Điều 6 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 12/2021/TT-NHNN `[SO_HIEU]`)
- (`e5` 1 . Thông tư này có hiệu lực thi hành kể từ ngày 27 tháng 10 năm 2021 . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 6 `[DIEU]`)


---

### Mẫu #12_2021_TT-NHNN_148636#body_context_67 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[12/2021/TT-NHNN]`<SO_HIEU>`** của **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Chính sách tiền tệ]`<LINH_VUC>`** . **[Điều 6]`<DIEU>`** . **[2 . Thông tư này **[sửa đổi , bổ sung một số điều của]`<TU_KHOA_PHAP_LY>`** Thông tư 01/2021/TT-NHNN ngày 31 tháng 3 năm 2021 của **[Thống đốc Ngân hàng nhà nước Việt Nam]`<CO_QUAN_THAM_QUYEN>`** quy định về phát hành kỳ phiếu , tín phiếu , **[chứng chỉ tiền gửi]`<GIAY_TO_HO_SO>`** , **[trái phiếu]`<TAI_SAN_VAT_CHAT>`** trong nước của **[tổ chức tín dụng , chi nhánh ngân hàng nước ngoài]`<TO_CHUC_DOANH_NGHIEP>`** như sau :]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **12/2021/TT-NHNN** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_BAN_HANH` (span: `[4:7]`)
- `[e3]` **Chính sách tiền tệ** → `LINH_VUC` (span: `[9:11]`)
- `[e4]` **Điều 6** → `DIEU` (span: `[12:14]`)
- `[e5]` **2 . Thông tư này sửa đổi , bổ sung một số điều của Thông tư 01/2021/TT-NHNN ngày 31 tháng 3 năm 2021 của Thống đốc Ngân hàng nhà nước Việt Nam quy định về phát hành kỳ phiếu , tín phiếu , chứng chỉ tiền gửi , trái phiếu trong nước của tổ chức tín dụng , chi nhánh ngân hàng nước ngoài như sau :** → `KHOAN` (span: `[15:62]`)
- `[e6]` **tổ chức tín dụng , chi nhánh ngân hàng nước ngoài** → `TO_CHUC_DOANH_NGHIEP` (span: `[53:59]`) *(lồng trong `e5` (`KHOAN`))*
- `[e7]` **sửa đổi , bổ sung một số điều của** → `TU_KHOA_PHAP_LY` (span: `[19:25]`) *(lồng trong `e5` (`KHOAN`))*
- `[e8]` **Thống đốc Ngân hàng nhà nước Việt Nam** → `CO_QUAN_THAM_QUYEN` (span: `[34:38]`) *(lồng trong `e5` (`KHOAN`))*
- `[e9]` **chứng chỉ tiền gửi** → `GIAY_TO_HO_SO` (span: `[45:48]`) *(lồng trong `e5` (`KHOAN`))*
- `[e10]` **trái phiếu** → `TAI_SAN_VAT_CHAT` (span: `[49:50]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 12/2021/TT-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Ngân hàng Nhà nước Việt Nam `[CO_QUAN_BAN_HANH]`)
- (`e1` 12/2021/TT-NHNN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 12/2021/TT-NHNN `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Chính sách tiền tệ `[LINH_VUC]`)
- (`e4` Điều 6 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 12/2021/TT-NHNN `[SO_HIEU]`)
- (`e5` 2 . Thông tư này sửa đổi , bổ sung một số điều của Thông tư 01/2021/TT-NHNN ngày 31 tháng 3 năm 2021 của Thống đốc Ngân hàng nhà nước Việt Nam quy định về phát hành kỳ phiếu , tín phiếu , chứng chỉ tiền gửi , trái phiếu trong nước của tổ chức tín dụng , chi nhánh ngân hàng nước ngoài như sau : `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 6 `[DIEU]`)
- (`e1` 12/2021/TT-NHNN `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Chính sách tiền tệ `[LINH_VUC]`)
- (`e5` 2 . Thông tư này sửa đổi , bổ sung một số điều của Thông tư 01/2021/TT-NHNN ngày 31 tháng 3 năm 2021 của Thống đốc Ngân hàng nhà nước Việt Nam quy định về phát hành kỳ phiếu , tín phiếu , chứng chỉ tiền gửi , trái phiếu trong nước của tổ chức tín dụng , chi nhánh ngân hàng nước ngoài như sau : `[KHOAN]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Chính sách tiền tệ `[LINH_VUC]`)


---

### Mẫu #12_2021_TT-NHNN_148636#body_standalone_68 (Loại: `body_standalone`)
> **[Điều 6]`<DIEU>`** . **[2 . Thông tư này **[sửa đổi , bổ sung một số điều của]`<TU_KHOA_PHAP_LY>`** Thông tư 01/2021/TT-NHNN ngày 31 tháng 3 năm 2021 của **[Thống đốc Ngân hàng nhà nước Việt Nam]`<CO_QUAN_THAM_QUYEN>`** quy định về phát hành kỳ phiếu , tín phiếu , **[chứng chỉ tiền gửi]`<GIAY_TO_HO_SO>`** , **[trái phiếu]`<TAI_SAN_VAT_CHAT>`** trong nước của **[tổ chức tín dụng , chi nhánh ngân hàng nước ngoài]`<TO_CHUC_DOANH_NGHIEP>`** như sau :]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 6** → `DIEU` (span: `[0:2]`)
- `[e1]` **2 . Thông tư này sửa đổi , bổ sung một số điều của Thông tư 01/2021/TT-NHNN ngày 31 tháng 3 năm 2021 của Thống đốc Ngân hàng nhà nước Việt Nam quy định về phát hành kỳ phiếu , tín phiếu , chứng chỉ tiền gửi , trái phiếu trong nước của tổ chức tín dụng , chi nhánh ngân hàng nước ngoài như sau :** → `KHOAN` (span: `[3:50]`)
- `[e2]` **tổ chức tín dụng , chi nhánh ngân hàng nước ngoài** → `TO_CHUC_DOANH_NGHIEP` (span: `[41:47]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **sửa đổi , bổ sung một số điều của** → `TU_KHOA_PHAP_LY` (span: `[7:13]`) *(lồng trong `e1` (`KHOAN`))*
- `[e4]` **Thống đốc Ngân hàng nhà nước Việt Nam** → `CO_QUAN_THAM_QUYEN` (span: `[22:26]`) *(lồng trong `e1` (`KHOAN`))*
- `[e5]` **chứng chỉ tiền gửi** → `GIAY_TO_HO_SO` (span: `[33:36]`) *(lồng trong `e1` (`KHOAN`))*
- `[e6]` **trái phiếu** → `TAI_SAN_VAT_CHAT` (span: `[37:38]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 2 . Thông tư này sửa đổi , bổ sung một số điều của Thông tư 01/2021/TT-NHNN ngày 31 tháng 3 năm 2021 của Thống đốc Ngân hàng nhà nước Việt Nam quy định về phát hành kỳ phiếu , tín phiếu , chứng chỉ tiền gửi , trái phiếu trong nước của tổ chức tín dụng , chi nhánh ngân hàng nước ngoài như sau : `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 6 `[DIEU]`)


---

### Mẫu #12_2021_TT-NHNN_148636#body_context_69 (Loại: `body_context`)
> **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[12/2021/TT-NHNN]`<SO_HIEU>`** . **[Điều 6]`<DIEU>`** . **[Khoản 2]`<KHOAN>`** . **[a ) **[Sửa đổi , bổ sung]`<TU_KHOA_PHAP_LY>`** **[khoản 1 Điều 4]`<THAM_CHIEU_PHAP_LY>`** như sau : “ 1 . Đối tượng mua **[giấy tờ có giá]`<TO_CHUC_DOANH_NGHIEP>`** là các tổ chức ( bao gồm cả **[tổ chức tín dụng , chi nhánh ngân hàng nước ngoài]`<TO_CHUC_DOANH_NGHIEP>`** ) , cá nhân Việt Nam và tổ chức , cá nhân nước ngoài , trừ trường hợp **[quy định tại]`<TU_KHOA_PHAP_LY>`** **[khoản 2 , khoản 3 , khoản 4 Điều này]`<THAM_CHIEU_PHAP_LY>`** . ”]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[4:5]`)
- `[e1]` **12/2021/TT-NHNN** → `SO_HIEU` (span: `[6:7]`)
- `[e2]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_BAN_HANH` (span: `[0:3]`)
- `[e3]` **Điều 6** → `DIEU` (span: `[8:10]`)
- `[e4]` **Khoản 2** → `KHOAN` (span: `[11:13]`)
- `[e5]` **a ) Sửa đổi , bổ sung khoản 1 Điều 4 như sau : “ 1 . Đối tượng mua giấy tờ có giá là các tổ chức ( bao gồm cả tổ chức tín dụng , chi nhánh ngân hàng nước ngoài ) , cá nhân Việt Nam và tổ chức , cá nhân nước ngoài , trừ trường hợp quy định tại khoản 2 , khoản 3 , khoản 4 Điều này . ”** → `DIEM` (span: `[14:71]`)
- `[e6]` **tổ chức tín dụng , chi nhánh ngân hàng nước ngoài** → `TO_CHUC_DOANH_NGHIEP` (span: `[39:45]`) *(lồng trong `e5` (`DIEM`))*
- `[e7]` **giấy tờ có giá** → `TO_CHUC_DOANH_NGHIEP` (span: `[31:33]`) *(lồng trong `e5` (`DIEM`))*
- `[e8]` **khoản 1 Điều 4** → `THAM_CHIEU_PHAP_LY` (span: `[19:23]`) *(lồng trong `e5` (`DIEM`))*
- `[e9]` **khoản 2 , khoản 3 , khoản 4 Điều này** → `THAM_CHIEU_PHAP_LY` (span: `[59:69]`) *(lồng trong `e5` (`DIEM`))*
- `[e10]` **Sửa đổi , bổ sung** → `TU_KHOA_PHAP_LY` (span: `[16:19]`) *(lồng trong `e5` (`DIEM`))*
- `[e11]` **quy định tại** → `TU_KHOA_PHAP_LY` (span: `[57:59]`) *(lồng trong `e5` (`DIEM`))*

**Quan hệ:**
- (`e1` 12/2021/TT-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Ngân hàng Nhà nước Việt Nam `[CO_QUAN_BAN_HANH]`)
- (`e1` 12/2021/TT-NHNN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 6 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 12/2021/TT-NHNN `[SO_HIEU]`)
- (`e4` Khoản 2 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 6 `[DIEU]`)
- (`e5` a ) Sửa đổi , bổ sung khoản 1 Điều 4 như sau : “ 1 . Đối tượng mua giấy tờ có giá là các tổ chức ( bao gồm cả tổ chức tín dụng , chi nhánh ngân hàng nước ngoài ) , cá nhân Việt Nam và tổ chức , cá nhân nước ngoài , trừ trường hợp quy định tại khoản 2 , khoản 3 , khoản 4 Điều này . ” `[DIEM]`) ==[ **THUOC_VE** ]==> (`e4` Khoản 2 `[KHOAN]`)
- (`e10` Sửa đổi , bổ sung `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e8` khoản 1 Điều 4 `[THAM_CHIEU_PHAP_LY]`)
- (`e5` a ) Sửa đổi , bổ sung khoản 1 Điều 4 như sau : “ 1 . Đối tượng mua giấy tờ có giá là các tổ chức ( bao gồm cả tổ chức tín dụng , chi nhánh ngân hàng nước ngoài ) , cá nhân Việt Nam và tổ chức , cá nhân nước ngoài , trừ trường hợp quy định tại khoản 2 , khoản 3 , khoản 4 Điều này . ” `[DIEM]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e8` khoản 1 Điều 4 `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e11` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e9` khoản 2 , khoản 3 , khoản 4 Điều này `[THAM_CHIEU_PHAP_LY]`)
- (`e5` a ) Sửa đổi , bổ sung khoản 1 Điều 4 như sau : “ 1 . Đối tượng mua giấy tờ có giá là các tổ chức ( bao gồm cả tổ chức tín dụng , chi nhánh ngân hàng nước ngoài ) , cá nhân Việt Nam và tổ chức , cá nhân nước ngoài , trừ trường hợp quy định tại khoản 2 , khoản 3 , khoản 4 Điều này . ” `[DIEM]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e9` khoản 2 , khoản 3 , khoản 4 Điều này `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #12_2021_TT-NHNN_148636#body_standalone_70 (Loại: `body_standalone`)
> **[Điều 6]`<DIEU>`** . **[Khoản 2]`<KHOAN>`** . **[a ) **[Sửa đổi , bổ sung]`<TU_KHOA_PHAP_LY>`** **[khoản 1 Điều 4]`<THAM_CHIEU_PHAP_LY>`** như sau : “ 1 . Đối tượng mua **[giấy tờ có giá]`<TO_CHUC_DOANH_NGHIEP>`** là các tổ chức ( bao gồm cả **[tổ chức tín dụng , chi nhánh ngân hàng nước ngoài]`<TO_CHUC_DOANH_NGHIEP>`** ) , cá nhân Việt Nam và tổ chức , cá nhân nước ngoài , trừ trường hợp **[quy định tại]`<TU_KHOA_PHAP_LY>`** **[khoản 2 , khoản 3 , khoản 4 Điều này]`<THAM_CHIEU_PHAP_LY>`** . ”]`<DIEM>`**

**Thực thể:**
- `[e0]` **Điều 6** → `DIEU` (span: `[0:2]`)
- `[e1]` **Khoản 2** → `KHOAN` (span: `[3:5]`)
- `[e2]` **a ) Sửa đổi , bổ sung khoản 1 Điều 4 như sau : “ 1 . Đối tượng mua giấy tờ có giá là các tổ chức ( bao gồm cả tổ chức tín dụng , chi nhánh ngân hàng nước ngoài ) , cá nhân Việt Nam và tổ chức , cá nhân nước ngoài , trừ trường hợp quy định tại khoản 2 , khoản 3 , khoản 4 Điều này . ”** → `DIEM` (span: `[6:63]`)
- `[e3]` **tổ chức tín dụng , chi nhánh ngân hàng nước ngoài** → `TO_CHUC_DOANH_NGHIEP` (span: `[31:37]`) *(lồng trong `e2` (`DIEM`))*
- `[e4]` **giấy tờ có giá** → `TO_CHUC_DOANH_NGHIEP` (span: `[23:25]`) *(lồng trong `e2` (`DIEM`))*
- `[e5]` **khoản 1 Điều 4** → `THAM_CHIEU_PHAP_LY` (span: `[11:15]`) *(lồng trong `e2` (`DIEM`))*
- `[e6]` **khoản 2 , khoản 3 , khoản 4 Điều này** → `THAM_CHIEU_PHAP_LY` (span: `[51:61]`) *(lồng trong `e2` (`DIEM`))*
- `[e7]` **Sửa đổi , bổ sung** → `TU_KHOA_PHAP_LY` (span: `[8:11]`) *(lồng trong `e2` (`DIEM`))*
- `[e8]` **quy định tại** → `TU_KHOA_PHAP_LY` (span: `[49:51]`) *(lồng trong `e2` (`DIEM`))*

**Quan hệ:**
- (`e1` Khoản 2 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 6 `[DIEU]`)
- (`e2` a ) Sửa đổi , bổ sung khoản 1 Điều 4 như sau : “ 1 . Đối tượng mua giấy tờ có giá là các tổ chức ( bao gồm cả tổ chức tín dụng , chi nhánh ngân hàng nước ngoài ) , cá nhân Việt Nam và tổ chức , cá nhân nước ngoài , trừ trường hợp quy định tại khoản 2 , khoản 3 , khoản 4 Điều này . ” `[DIEM]`) ==[ **THUOC_VE** ]==> (`e1` Khoản 2 `[KHOAN]`)
- (`e7` Sửa đổi , bổ sung `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e5` khoản 1 Điều 4 `[THAM_CHIEU_PHAP_LY]`)
- (`e2` a ) Sửa đổi , bổ sung khoản 1 Điều 4 như sau : “ 1 . Đối tượng mua giấy tờ có giá là các tổ chức ( bao gồm cả tổ chức tín dụng , chi nhánh ngân hàng nước ngoài ) , cá nhân Việt Nam và tổ chức , cá nhân nước ngoài , trừ trường hợp quy định tại khoản 2 , khoản 3 , khoản 4 Điều này . ” `[DIEM]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e5` khoản 1 Điều 4 `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e8` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e6` khoản 2 , khoản 3 , khoản 4 Điều này `[THAM_CHIEU_PHAP_LY]`)
- (`e2` a ) Sửa đổi , bổ sung khoản 1 Điều 4 như sau : “ 1 . Đối tượng mua giấy tờ có giá là các tổ chức ( bao gồm cả tổ chức tín dụng , chi nhánh ngân hàng nước ngoài ) , cá nhân Việt Nam và tổ chức , cá nhân nước ngoài , trừ trường hợp quy định tại khoản 2 , khoản 3 , khoản 4 Điều này . ” `[DIEM]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e6` khoản 2 , khoản 3 , khoản 4 Điều này `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #12_2021_TT-NHNN_148636#body_context_71 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[12/2021/TT-NHNN]`<SO_HIEU>`** của **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Chính sách tiền tệ]`<LINH_VUC>`** . **[Điều 6]`<DIEU>`** . **[Khoản 2]`<KHOAN>`** . **[b ) **[Bổ sung]`<TU_KHOA_PHAP_LY>`** **[khoản 4 vào Điều 4]`<THAM_CHIEU_PHAP_LY>`** như sau : “ 4 . Đối với **[giấy tờ có giá]`<TO_CHUC_DOANH_NGHIEP>`** là kỳ phiếu , tín phiếu , **[chứng chỉ tiền gửi]`<GIAY_TO_HO_SO>`** , **[tổ chức tín dụng , chi nhánh ngân hàng nước ngoài]`<TO_CHUC_DOANH_NGHIEP>`** chỉ được mua **[giấy tờ có giá]`<TO_CHUC_DOANH_NGHIEP>`** có thời hạn **[dưới 12 tháng]`<THOI_HAN>`** . ”]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **12/2021/TT-NHNN** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_BAN_HANH` (span: `[4:7]`)
- `[e3]` **Chính sách tiền tệ** → `LINH_VUC` (span: `[9:11]`)
- `[e4]` **Điều 6** → `DIEU` (span: `[12:14]`)
- `[e5]` **Khoản 2** → `KHOAN` (span: `[15:17]`)
- `[e6]` **b ) Bổ sung khoản 4 vào Điều 4 như sau : “ 4 . Đối với giấy tờ có giá là kỳ phiếu , tín phiếu , chứng chỉ tiền gửi , tổ chức tín dụng , chi nhánh ngân hàng nước ngoài chỉ được mua giấy tờ có giá có thời hạn dưới 12 tháng . ”** → `DIEM` (span: `[18:62]`)
- `[e7]` **tổ chức tín dụng , chi nhánh ngân hàng nước ngoài** → `TO_CHUC_DOANH_NGHIEP` (span: `[44:50]`) *(lồng trong `e6` (`DIEM`))*
- `[e8]` **giấy tờ có giá** → `TO_CHUC_DOANH_NGHIEP` (span: `[33:35]`) *(lồng trong `e6` (`DIEM`))*
- `[e9]` **giấy tờ có giá** → `TO_CHUC_DOANH_NGHIEP` (span: `[53:55]`) *(lồng trong `e6` (`DIEM`))*
- `[e10]` **khoản 4 vào Điều 4** → `THAM_CHIEU_PHAP_LY` (span: `[21:26]`) *(lồng trong `e6` (`DIEM`))*
- `[e11]` **Bổ sung** → `TU_KHOA_PHAP_LY` (span: `[20:21]`) *(lồng trong `e6` (`DIEM`))*
- `[e12]` **dưới 12 tháng** → `THOI_HAN` (span: `[57:60]`) *(lồng trong `e6` (`DIEM`))*
- `[e13]` **chứng chỉ tiền gửi** → `GIAY_TO_HO_SO` (span: `[40:43]`) *(lồng trong `e6` (`DIEM`))*

**Quan hệ:**
- (`e1` 12/2021/TT-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Ngân hàng Nhà nước Việt Nam `[CO_QUAN_BAN_HANH]`)
- (`e1` 12/2021/TT-NHNN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 12/2021/TT-NHNN `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Chính sách tiền tệ `[LINH_VUC]`)
- (`e4` Điều 6 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 12/2021/TT-NHNN `[SO_HIEU]`)
- (`e5` Khoản 2 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 6 `[DIEU]`)
- (`e6` b ) Bổ sung khoản 4 vào Điều 4 như sau : “ 4 . Đối với giấy tờ có giá là kỳ phiếu , tín phiếu , chứng chỉ tiền gửi , tổ chức tín dụng , chi nhánh ngân hàng nước ngoài chỉ được mua giấy tờ có giá có thời hạn dưới 12 tháng . ” `[DIEM]`) ==[ **THUOC_VE** ]==> (`e5` Khoản 2 `[KHOAN]`)
- (`e1` 12/2021/TT-NHNN `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Chính sách tiền tệ `[LINH_VUC]`)
- (`e6` b ) Bổ sung khoản 4 vào Điều 4 như sau : “ 4 . Đối với giấy tờ có giá là kỳ phiếu , tín phiếu , chứng chỉ tiền gửi , tổ chức tín dụng , chi nhánh ngân hàng nước ngoài chỉ được mua giấy tờ có giá có thời hạn dưới 12 tháng . ” `[DIEM]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Chính sách tiền tệ `[LINH_VUC]`)
- (`e11` Bổ sung `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e10` khoản 4 vào Điều 4 `[THAM_CHIEU_PHAP_LY]`)
- (`e6` b ) Bổ sung khoản 4 vào Điều 4 như sau : “ 4 . Đối với giấy tờ có giá là kỳ phiếu , tín phiếu , chứng chỉ tiền gửi , tổ chức tín dụng , chi nhánh ngân hàng nước ngoài chỉ được mua giấy tờ có giá có thời hạn dưới 12 tháng . ” `[DIEM]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e10` khoản 4 vào Điều 4 `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #12_2021_TT-NHNN_148636#body_standalone_72 (Loại: `body_standalone`)
> **[Điều 6]`<DIEU>`** . **[Khoản 2]`<KHOAN>`** . **[b ) **[Bổ sung]`<TU_KHOA_PHAP_LY>`** **[khoản 4 vào Điều 4]`<THAM_CHIEU_PHAP_LY>`** như sau : “ 4 . Đối với **[giấy tờ có giá]`<TO_CHUC_DOANH_NGHIEP>`** là kỳ phiếu , tín phiếu , **[chứng chỉ tiền gửi]`<GIAY_TO_HO_SO>`** , **[tổ chức tín dụng , chi nhánh ngân hàng nước ngoài]`<TO_CHUC_DOANH_NGHIEP>`** chỉ được mua **[giấy tờ có giá]`<TO_CHUC_DOANH_NGHIEP>`** có thời hạn **[dưới 12 tháng]`<THOI_HAN>`** . ”]`<DIEM>`**

**Thực thể:**
- `[e0]` **Điều 6** → `DIEU` (span: `[0:2]`)
- `[e1]` **Khoản 2** → `KHOAN` (span: `[3:5]`)
- `[e2]` **b ) Bổ sung khoản 4 vào Điều 4 như sau : “ 4 . Đối với giấy tờ có giá là kỳ phiếu , tín phiếu , chứng chỉ tiền gửi , tổ chức tín dụng , chi nhánh ngân hàng nước ngoài chỉ được mua giấy tờ có giá có thời hạn dưới 12 tháng . ”** → `DIEM` (span: `[6:50]`)
- `[e3]` **tổ chức tín dụng , chi nhánh ngân hàng nước ngoài** → `TO_CHUC_DOANH_NGHIEP` (span: `[32:38]`) *(lồng trong `e2` (`DIEM`))*
- `[e4]` **giấy tờ có giá** → `TO_CHUC_DOANH_NGHIEP` (span: `[21:23]`) *(lồng trong `e2` (`DIEM`))*
- `[e5]` **giấy tờ có giá** → `TO_CHUC_DOANH_NGHIEP` (span: `[41:43]`) *(lồng trong `e2` (`DIEM`))*
- `[e6]` **khoản 4 vào Điều 4** → `THAM_CHIEU_PHAP_LY` (span: `[9:14]`) *(lồng trong `e2` (`DIEM`))*
- `[e7]` **Bổ sung** → `TU_KHOA_PHAP_LY` (span: `[8:9]`) *(lồng trong `e2` (`DIEM`))*
- `[e8]` **dưới 12 tháng** → `THOI_HAN` (span: `[45:48]`) *(lồng trong `e2` (`DIEM`))*
- `[e9]` **chứng chỉ tiền gửi** → `GIAY_TO_HO_SO` (span: `[28:31]`) *(lồng trong `e2` (`DIEM`))*

**Quan hệ:**
- (`e1` Khoản 2 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 6 `[DIEU]`)
- (`e2` b ) Bổ sung khoản 4 vào Điều 4 như sau : “ 4 . Đối với giấy tờ có giá là kỳ phiếu , tín phiếu , chứng chỉ tiền gửi , tổ chức tín dụng , chi nhánh ngân hàng nước ngoài chỉ được mua giấy tờ có giá có thời hạn dưới 12 tháng . ” `[DIEM]`) ==[ **THUOC_VE** ]==> (`e1` Khoản 2 `[KHOAN]`)
- (`e7` Bổ sung `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e6` khoản 4 vào Điều 4 `[THAM_CHIEU_PHAP_LY]`)
- (`e2` b ) Bổ sung khoản 4 vào Điều 4 như sau : “ 4 . Đối với giấy tờ có giá là kỳ phiếu , tín phiếu , chứng chỉ tiền gửi , tổ chức tín dụng , chi nhánh ngân hàng nước ngoài chỉ được mua giấy tờ có giá có thời hạn dưới 12 tháng . ” `[DIEM]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e6` khoản 4 vào Điều 4 `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #12_2021_TT-NHNN_148636#body_context_73 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[12/2021/TT-NHNN]`<SO_HIEU>`** ban hành **[ngày 30 tháng 07 năm 2021]`<NGAY_BAN_HANH>`** bởi **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_BAN_HANH>`** . **[Điều 7 . Tổ chức thực hiện . Chánh Văn phòng , Vụ trưởng Vụ Chính sách tiền tệ và Thủ trưởng các đơn vị thuộc **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_THAM_QUYEN>`** ; **[tổ chức tín dụng , chi nhánh ngân hàng nước ngoài]`<TO_CHUC_DOANH_NGHIEP>`** chịu trách nhiệm tổ chức thực hiện Thông tư này . / .]`<DIEU>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **12/2021/TT-NHNN** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_BAN_HANH` (span: `[11:14]`)
- `[e3]` **ngày 30 tháng 07 năm 2021** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 7 . Tổ chức thực hiện . Chánh Văn phòng , Vụ trưởng Vụ Chính sách tiền tệ và Thủ trưởng các đơn vị thuộc Ngân hàng Nhà nước Việt Nam ; tổ chức tín dụng , chi nhánh ngân hàng nước ngoài chịu trách nhiệm tổ chức thực hiện Thông tư này . / .** → `DIEU` (span: `[15:52]`)
- `[e5]` **tổ chức tín dụng , chi nhánh ngân hàng nước ngoài** → `TO_CHUC_DOANH_NGHIEP` (span: `[37:43]`) *(lồng trong `e4` (`DIEU`))*
- `[e6]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_THAM_QUYEN` (span: `[33:36]`) *(lồng trong `e4` (`DIEU`))*

**Quan hệ:**
- (`e1` 12/2021/TT-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Ngân hàng Nhà nước Việt Nam `[CO_QUAN_BAN_HANH]`)
- (`e1` 12/2021/TT-NHNN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 12/2021/TT-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 30 tháng 07 năm 2021 `[NGAY_BAN_HANH]`)
- (`e4` Điều 7 . Tổ chức thực hiện . Chánh Văn phòng , Vụ trưởng Vụ Chính sách tiền tệ và Thủ trưởng các đơn vị thuộc Ngân hàng Nhà nước Việt Nam ; tổ chức tín dụng , chi nhánh ngân hàng nước ngoài chịu trách nhiệm tổ chức thực hiện Thông tư này . / . `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 12/2021/TT-NHNN `[SO_HIEU]`)


---

### Mẫu #12_2021_TT-NHNN_148636#body_context_74 (Loại: `body_context`)
> **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[12/2021/TT-NHNN]`<SO_HIEU>`** . **[Điều 1 . Phạm vi điều chỉnh]`<DIEU>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[4:5]`)
- `[e1]` **12/2021/TT-NHNN** → `SO_HIEU` (span: `[6:7]`)
- `[e2]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_BAN_HANH` (span: `[0:3]`)
- `[e3]` **Điều 1 . Phạm vi điều chỉnh** → `DIEU` (span: `[8:13]`)

**Quan hệ:**
- (`e1` 12/2021/TT-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Ngân hàng Nhà nước Việt Nam `[CO_QUAN_BAN_HANH]`)
- (`e1` 12/2021/TT-NHNN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 1 . Phạm vi điều chỉnh `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 12/2021/TT-NHNN `[SO_HIEU]`)


---

### Mẫu #12_2021_TT-NHNN_148636#body_context_75 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[12/2021/TT-NHNN]`<SO_HIEU>`** của **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Chính sách tiền tệ]`<LINH_VUC>`** . **[Điều 2 . Đối tượng áp dụng]`<DIEU>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **12/2021/TT-NHNN** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_BAN_HANH` (span: `[4:7]`)
- `[e3]` **Chính sách tiền tệ** → `LINH_VUC` (span: `[9:11]`)
- `[e4]` **Điều 2 . Đối tượng áp dụng** → `DIEU` (span: `[12:17]`)

**Quan hệ:**
- (`e1` 12/2021/TT-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Ngân hàng Nhà nước Việt Nam `[CO_QUAN_BAN_HANH]`)
- (`e1` 12/2021/TT-NHNN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 12/2021/TT-NHNN `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Chính sách tiền tệ `[LINH_VUC]`)
- (`e4` Điều 2 . Đối tượng áp dụng `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 12/2021/TT-NHNN `[SO_HIEU]`)
- (`e1` 12/2021/TT-NHNN `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Chính sách tiền tệ `[LINH_VUC]`)
- (`e4` Điều 2 . Đối tượng áp dụng `[DIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Chính sách tiền tệ `[LINH_VUC]`)


---

### Mẫu #12_2021_TT-NHNN_148636#body_context_76 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[12/2021/TT-NHNN]`<SO_HIEU>`** ban hành **[ngày 30 tháng 07 năm 2021]`<NGAY_BAN_HANH>`** bởi **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_BAN_HANH>`** . **[Điều 4 . Thông tin giao dịch]`<DIEU>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **12/2021/TT-NHNN** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_BAN_HANH` (span: `[11:14]`)
- `[e3]` **ngày 30 tháng 07 năm 2021** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 4 . Thông tin giao dịch** → `DIEU` (span: `[15:20]`)

**Quan hệ:**
- (`e1` 12/2021/TT-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Ngân hàng Nhà nước Việt Nam `[CO_QUAN_BAN_HANH]`)
- (`e1` 12/2021/TT-NHNN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 12/2021/TT-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 30 tháng 07 năm 2021 `[NGAY_BAN_HANH]`)
- (`e4` Điều 4 . Thông tin giao dịch `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 12/2021/TT-NHNN `[SO_HIEU]`)


---

### Mẫu #12_2021_TT-NHNN_148636#body_context_77 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[12/2021/TT-NHNN]`<SO_HIEU>`** của **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Chính sách tiền tệ]`<LINH_VUC>`** . **[Điều 4]`<DIEU>`** . **[1 . Thông tin về Bên bán , Bên mua .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **12/2021/TT-NHNN** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_BAN_HANH` (span: `[4:7]`)
- `[e3]` **Chính sách tiền tệ** → `LINH_VUC` (span: `[9:11]`)
- `[e4]` **Điều 4** → `DIEU` (span: `[12:14]`)
- `[e5]` **1 . Thông tin về Bên bán , Bên mua .** → `KHOAN` (span: `[15:25]`)

**Quan hệ:**
- (`e1` 12/2021/TT-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Ngân hàng Nhà nước Việt Nam `[CO_QUAN_BAN_HANH]`)
- (`e1` 12/2021/TT-NHNN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 12/2021/TT-NHNN `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Chính sách tiền tệ `[LINH_VUC]`)
- (`e4` Điều 4 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 12/2021/TT-NHNN `[SO_HIEU]`)
- (`e5` 1 . Thông tin về Bên bán , Bên mua . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 4 `[DIEU]`)
- (`e1` 12/2021/TT-NHNN `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Chính sách tiền tệ `[LINH_VUC]`)
- (`e5` 1 . Thông tin về Bên bán , Bên mua . `[KHOAN]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Chính sách tiền tệ `[LINH_VUC]`)


---

### Mẫu #12_2021_TT-NHNN_148636#body_context_78 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[12/2021/TT-NHNN]`<SO_HIEU>`** ban hành **[ngày 30 tháng 07 năm 2021]`<NGAY_BAN_HANH>`** bởi **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_BAN_HANH>`** . **[Điều 5 . Quy định nội bộ]`<DIEU>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **12/2021/TT-NHNN** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_BAN_HANH` (span: `[11:14]`)
- `[e3]` **ngày 30 tháng 07 năm 2021** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 5 . Quy định nội bộ** → `DIEU` (span: `[15:20]`)

**Quan hệ:**
- (`e1` 12/2021/TT-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Ngân hàng Nhà nước Việt Nam `[CO_QUAN_BAN_HANH]`)
- (`e1` 12/2021/TT-NHNN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 12/2021/TT-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 30 tháng 07 năm 2021 `[NGAY_BAN_HANH]`)
- (`e4` Điều 5 . Quy định nội bộ `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 12/2021/TT-NHNN `[SO_HIEU]`)


---

### Mẫu #12_2021_TT-NHNN_148636#body_context_79 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[12/2021/TT-NHNN]`<SO_HIEU>`** ban hành **[ngày 30 tháng 07 năm 2021]`<NGAY_BAN_HANH>`** bởi **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_BAN_HANH>`** . **[Điều 6 . Điều khoản thi hành]`<DIEU>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **12/2021/TT-NHNN** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_BAN_HANH` (span: `[11:14]`)
- `[e3]` **ngày 30 tháng 07 năm 2021** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 6 . Điều khoản thi hành** → `DIEU` (span: `[15:20]`)

**Quan hệ:**
- (`e1` 12/2021/TT-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Ngân hàng Nhà nước Việt Nam `[CO_QUAN_BAN_HANH]`)
- (`e1` 12/2021/TT-NHNN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 12/2021/TT-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 30 tháng 07 năm 2021 `[NGAY_BAN_HANH]`)
- (`e4` Điều 6 . Điều khoản thi hành `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 12/2021/TT-NHNN `[SO_HIEU]`)


---

### Mẫu #12_2021_TT-NHNN_148636#body_context_80 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[12/2021/TT-NHNN]`<SO_HIEU>`** ban hành **[ngày 30 tháng 07 năm 2021]`<NGAY_BAN_HANH>`** bởi **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_BAN_HANH>`** . **[Điều 6]`<DIEU>`** . **[1 . Đối tượng mua **[giấy tờ có giá]`<TO_CHUC_DOANH_NGHIEP>`** là các tổ chức ( bao gồm cả **[tổ chức tín dụng , chi nhánh ngân hàng nước ngoài]`<TO_CHUC_DOANH_NGHIEP>`** ) , cá nhân Việt Nam và tổ chức , cá nhân nước ngoài , trừ trường hợp **[quy định tại]`<TU_KHOA_PHAP_LY>`** **[khoản 2 , khoản 3 , khoản 4 Điều này]`<THAM_CHIEU_PHAP_LY>`** . ”]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **12/2021/TT-NHNN** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_BAN_HANH` (span: `[11:14]`)
- `[e3]` **ngày 30 tháng 07 năm 2021** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 6** → `DIEU` (span: `[15:17]`)
- `[e5]` **1 . Đối tượng mua giấy tờ có giá là các tổ chức ( bao gồm cả tổ chức tín dụng , chi nhánh ngân hàng nước ngoài ) , cá nhân Việt Nam và tổ chức , cá nhân nước ngoài , trừ trường hợp quy định tại khoản 2 , khoản 3 , khoản 4 Điều này . ”** → `KHOAN` (span: `[18:62]`)
- `[e6]` **tổ chức tín dụng , chi nhánh ngân hàng nước ngoài** → `TO_CHUC_DOANH_NGHIEP` (span: `[30:36]`) *(lồng trong `e5` (`KHOAN`))*
- `[e7]` **giấy tờ có giá** → `TO_CHUC_DOANH_NGHIEP` (span: `[22:24]`) *(lồng trong `e5` (`KHOAN`))*
- `[e8]` **khoản 2 , khoản 3 , khoản 4 Điều này** → `THAM_CHIEU_PHAP_LY` (span: `[50:60]`) *(lồng trong `e5` (`KHOAN`))*
- `[e9]` **quy định tại** → `TU_KHOA_PHAP_LY` (span: `[48:50]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 12/2021/TT-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Ngân hàng Nhà nước Việt Nam `[CO_QUAN_BAN_HANH]`)
- (`e1` 12/2021/TT-NHNN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 12/2021/TT-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 30 tháng 07 năm 2021 `[NGAY_BAN_HANH]`)
- (`e4` Điều 6 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 12/2021/TT-NHNN `[SO_HIEU]`)
- (`e5` 1 . Đối tượng mua giấy tờ có giá là các tổ chức ( bao gồm cả tổ chức tín dụng , chi nhánh ngân hàng nước ngoài ) , cá nhân Việt Nam và tổ chức , cá nhân nước ngoài , trừ trường hợp quy định tại khoản 2 , khoản 3 , khoản 4 Điều này . ” `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 6 `[DIEU]`)
- (`e9` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e8` khoản 2 , khoản 3 , khoản 4 Điều này `[THAM_CHIEU_PHAP_LY]`)
- (`e5` 1 . Đối tượng mua giấy tờ có giá là các tổ chức ( bao gồm cả tổ chức tín dụng , chi nhánh ngân hàng nước ngoài ) , cá nhân Việt Nam và tổ chức , cá nhân nước ngoài , trừ trường hợp quy định tại khoản 2 , khoản 3 , khoản 4 Điều này . ” `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e8` khoản 2 , khoản 3 , khoản 4 Điều này `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #12_2021_TT-NHNN_148636#body_standalone_81 (Loại: `body_standalone`)
> **[Điều 6]`<DIEU>`** . **[1 . Đối tượng mua **[giấy tờ có giá]`<TO_CHUC_DOANH_NGHIEP>`** là các tổ chức ( bao gồm cả **[tổ chức tín dụng , chi nhánh ngân hàng nước ngoài]`<TO_CHUC_DOANH_NGHIEP>`** ) , cá nhân Việt Nam và tổ chức , cá nhân nước ngoài , trừ trường hợp **[quy định tại]`<TU_KHOA_PHAP_LY>`** **[khoản 2 , khoản 3 , khoản 4 Điều này]`<THAM_CHIEU_PHAP_LY>`** . ”]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 6** → `DIEU` (span: `[0:2]`)
- `[e1]` **1 . Đối tượng mua giấy tờ có giá là các tổ chức ( bao gồm cả tổ chức tín dụng , chi nhánh ngân hàng nước ngoài ) , cá nhân Việt Nam và tổ chức , cá nhân nước ngoài , trừ trường hợp quy định tại khoản 2 , khoản 3 , khoản 4 Điều này . ”** → `KHOAN` (span: `[3:47]`)
- `[e2]` **tổ chức tín dụng , chi nhánh ngân hàng nước ngoài** → `TO_CHUC_DOANH_NGHIEP` (span: `[15:21]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **giấy tờ có giá** → `TO_CHUC_DOANH_NGHIEP` (span: `[7:9]`) *(lồng trong `e1` (`KHOAN`))*
- `[e4]` **khoản 2 , khoản 3 , khoản 4 Điều này** → `THAM_CHIEU_PHAP_LY` (span: `[35:45]`) *(lồng trong `e1` (`KHOAN`))*
- `[e5]` **quy định tại** → `TU_KHOA_PHAP_LY` (span: `[33:35]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 1 . Đối tượng mua giấy tờ có giá là các tổ chức ( bao gồm cả tổ chức tín dụng , chi nhánh ngân hàng nước ngoài ) , cá nhân Việt Nam và tổ chức , cá nhân nước ngoài , trừ trường hợp quy định tại khoản 2 , khoản 3 , khoản 4 Điều này . ” `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 6 `[DIEU]`)
- (`e5` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e4` khoản 2 , khoản 3 , khoản 4 Điều này `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 1 . Đối tượng mua giấy tờ có giá là các tổ chức ( bao gồm cả tổ chức tín dụng , chi nhánh ngân hàng nước ngoài ) , cá nhân Việt Nam và tổ chức , cá nhân nước ngoài , trừ trường hợp quy định tại khoản 2 , khoản 3 , khoản 4 Điều này . ” `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e4` khoản 2 , khoản 3 , khoản 4 Điều này `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #12_2021_TT-NHNN_148636#body_context_82 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[12/2021/TT-NHNN]`<SO_HIEU>`** của **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Chính sách tiền tệ]`<LINH_VUC>`** . **[Điều 6]`<DIEU>`** . **[4 . Đối với **[giấy tờ có giá]`<TO_CHUC_DOANH_NGHIEP>`** là kỳ phiếu , tín phiếu , **[chứng chỉ tiền gửi]`<GIAY_TO_HO_SO>`** , **[tổ chức tín dụng , chi nhánh ngân hàng nước ngoài]`<TO_CHUC_DOANH_NGHIEP>`** chỉ được mua **[giấy tờ có giá]`<TO_CHUC_DOANH_NGHIEP>`** có thời hạn **[dưới 12 tháng]`<THOI_HAN>`** . ”]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **12/2021/TT-NHNN** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_BAN_HANH` (span: `[4:7]`)
- `[e3]` **Chính sách tiền tệ** → `LINH_VUC` (span: `[9:11]`)
- `[e4]` **Điều 6** → `DIEU` (span: `[12:14]`)
- `[e5]` **4 . Đối với giấy tờ có giá là kỳ phiếu , tín phiếu , chứng chỉ tiền gửi , tổ chức tín dụng , chi nhánh ngân hàng nước ngoài chỉ được mua giấy tờ có giá có thời hạn dưới 12 tháng . ”** → `KHOAN` (span: `[15:47]`)
- `[e6]` **tổ chức tín dụng , chi nhánh ngân hàng nước ngoài** → `TO_CHUC_DOANH_NGHIEP` (span: `[29:35]`) *(lồng trong `e5` (`KHOAN`))*
- `[e7]` **giấy tờ có giá** → `TO_CHUC_DOANH_NGHIEP` (span: `[18:20]`) *(lồng trong `e5` (`KHOAN`))*
- `[e8]` **giấy tờ có giá** → `TO_CHUC_DOANH_NGHIEP` (span: `[38:40]`) *(lồng trong `e5` (`KHOAN`))*
- `[e9]` **dưới 12 tháng** → `THOI_HAN` (span: `[42:45]`) *(lồng trong `e5` (`KHOAN`))*
- `[e10]` **chứng chỉ tiền gửi** → `GIAY_TO_HO_SO` (span: `[25:28]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 12/2021/TT-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Ngân hàng Nhà nước Việt Nam `[CO_QUAN_BAN_HANH]`)
- (`e1` 12/2021/TT-NHNN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 12/2021/TT-NHNN `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Chính sách tiền tệ `[LINH_VUC]`)
- (`e4` Điều 6 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 12/2021/TT-NHNN `[SO_HIEU]`)
- (`e5` 4 . Đối với giấy tờ có giá là kỳ phiếu , tín phiếu , chứng chỉ tiền gửi , tổ chức tín dụng , chi nhánh ngân hàng nước ngoài chỉ được mua giấy tờ có giá có thời hạn dưới 12 tháng . ” `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 6 `[DIEU]`)
- (`e1` 12/2021/TT-NHNN `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Chính sách tiền tệ `[LINH_VUC]`)
- (`e5` 4 . Đối với giấy tờ có giá là kỳ phiếu , tín phiếu , chứng chỉ tiền gửi , tổ chức tín dụng , chi nhánh ngân hàng nước ngoài chỉ được mua giấy tờ có giá có thời hạn dưới 12 tháng . ” `[KHOAN]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Chính sách tiền tệ `[LINH_VUC]`)


---

### Mẫu #12_2021_TT-NHNN_148636#body_standalone_83 (Loại: `body_standalone`)
> **[Điều 6]`<DIEU>`** . **[4 . Đối với **[giấy tờ có giá]`<TO_CHUC_DOANH_NGHIEP>`** là kỳ phiếu , tín phiếu , **[chứng chỉ tiền gửi]`<GIAY_TO_HO_SO>`** , **[tổ chức tín dụng , chi nhánh ngân hàng nước ngoài]`<TO_CHUC_DOANH_NGHIEP>`** chỉ được mua **[giấy tờ có giá]`<TO_CHUC_DOANH_NGHIEP>`** có thời hạn **[dưới 12 tháng]`<THOI_HAN>`** . ”]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 6** → `DIEU` (span: `[0:2]`)
- `[e1]` **4 . Đối với giấy tờ có giá là kỳ phiếu , tín phiếu , chứng chỉ tiền gửi , tổ chức tín dụng , chi nhánh ngân hàng nước ngoài chỉ được mua giấy tờ có giá có thời hạn dưới 12 tháng . ”** → `KHOAN` (span: `[3:35]`)
- `[e2]` **tổ chức tín dụng , chi nhánh ngân hàng nước ngoài** → `TO_CHUC_DOANH_NGHIEP` (span: `[17:23]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **giấy tờ có giá** → `TO_CHUC_DOANH_NGHIEP` (span: `[6:8]`) *(lồng trong `e1` (`KHOAN`))*
- `[e4]` **giấy tờ có giá** → `TO_CHUC_DOANH_NGHIEP` (span: `[26:28]`) *(lồng trong `e1` (`KHOAN`))*
- `[e5]` **dưới 12 tháng** → `THOI_HAN` (span: `[30:33]`) *(lồng trong `e1` (`KHOAN`))*
- `[e6]` **chứng chỉ tiền gửi** → `GIAY_TO_HO_SO` (span: `[13:16]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 4 . Đối với giấy tờ có giá là kỳ phiếu , tín phiếu , chứng chỉ tiền gửi , tổ chức tín dụng , chi nhánh ngân hàng nước ngoài chỉ được mua giấy tờ có giá có thời hạn dưới 12 tháng . ” `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 6 `[DIEU]`)


---

### Mẫu #12_2021_TT-NHNN_148636#body_context_84 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[12/2021/TT-NHNN]`<SO_HIEU>`** ban hành **[ngày 30 tháng 07 năm 2021]`<NGAY_BAN_HANH>`** bởi **[Ngân hàng Nhà nước Việt Nam]`<CO_QUAN_BAN_HANH>`** . **[Điều 7 . Tổ chức thực hiện]`<DIEU>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **12/2021/TT-NHNN** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Ngân hàng Nhà nước Việt Nam** → `CO_QUAN_BAN_HANH` (span: `[11:14]`)
- `[e3]` **ngày 30 tháng 07 năm 2021** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 7 . Tổ chức thực hiện** → `DIEU` (span: `[15:20]`)

**Quan hệ:**
- (`e1` 12/2021/TT-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Ngân hàng Nhà nước Việt Nam `[CO_QUAN_BAN_HANH]`)
- (`e1` 12/2021/TT-NHNN `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 12/2021/TT-NHNN `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 30 tháng 07 năm 2021 `[NGAY_BAN_HANH]`)
- (`e4` Điều 7 . Tổ chức thực hiện `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 12/2021/TT-NHNN `[SO_HIEU]`)


---

### Mẫu #12_2021_TT-NHNN_148636#hard_negative_85 (Loại: `hard_negative`)
> CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM


---

### Mẫu #12_2021_TT-NHNN_148636#hard_negative_86 (Loại: `hard_negative`)
> Độc lập - Tự do - Hạnh phúc


---
