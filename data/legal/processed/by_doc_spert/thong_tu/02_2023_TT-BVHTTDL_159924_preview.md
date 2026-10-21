# Dữ liệu gán nhãn văn bản: 02_2023_TT-BVHTTDL_159924
- **Thể loại**: `thong_tu`
- **Phân vùng dữ liệu**: `TRAIN`
- **Tổng số mẫu**: 102 mẫu
- **Tổng số thực thể**: 723
- **Tổng số quan hệ**: 511

---

### Mẫu #02_2023_TT-BVHTTDL_159924#header_0 (Loại: `header`)
> **[BỘ VĂN HÓA , THỂ THAO VÀ DU LỊCH]`<CO_QUAN_BAN_HANH>`** . CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM Độc lập - Tự do - Hạnh phúc . Số : **[02/2023/TT-BVHTTDL]`<SO_HIEU>`** . Hà Nội , **[ngày 21 tháng 02 năm 2023]`<NGAY_BAN_HANH>`** . **[THÔNG TƯ]`<LOAI_VAN_BAN>`**

**Thực thể:**
- `[e0]` **02/2023/TT-BVHTTDL** → `SO_HIEU` (span: `[21:22]`)
- `[e1]` **ngày 21 tháng 02 năm 2023** → `NGAY_BAN_HANH` (span: `[25:31]`)
- `[e2]` **BỘ VĂN HÓA , THỂ THAO VÀ DU LỊCH** → `CO_QUAN_BAN_HANH` (span: `[0:6]`)
- `[e3]` **THÔNG TƯ** → `LOAI_VAN_BAN` (span: `[32:33]`)

**Quan hệ:**
- (`e0` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` BỘ VĂN HÓA , THỂ THAO VÀ DU LỊCH `[CO_QUAN_BAN_HANH]`)
- (`e0` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e1` ngày 21 tháng 02 năm 2023 `[NGAY_BAN_HANH]`)
- (`e0` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e3` THÔNG TƯ `[LOAI_VAN_BAN]`)


---

### Mẫu #02_2023_TT-BVHTTDL_159924#signature_1 (Loại: `signature`)
> **[BỘ TRƯỞNG]`<CHUC_DANH_NGUOI_KY>`** ( Đã ký ) **[Nguyễn Văn Hùng]`<NGUOI_KY>`**

**Thực thể:**
- `[e0]` **Nguyễn Văn Hùng** → `NGUOI_KY` (span: `[5:6]`)
- `[e1]` **BỘ TRƯỞNG** → `CHUC_DANH_NGUOI_KY` (span: `[0:1]`)

**Quan hệ:**
- (`e0` Nguyễn Văn Hùng `[NGUOI_KY]`) ==[ **GIU_CHUC_VU** ]==> (`e1` BỘ TRƯỞNG `[CHUC_DANH_NGUOI_KY]`)


---

### Mẫu #02_2023_TT-BVHTTDL_159924#meta_2 (Loại: `meta`)
> **[BỘ VĂN HÓA , THỂ THAO VÀ DU LỊCH]`<CO_QUAN_BAN_HANH>`** . CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM Độc lập - Tự do - Hạnh phúc . Số : **[02/2023/TT-BVHTTDL]`<SO_HIEU>`** . Hà Nội , ngày 21 tháng 02 năm 2023 . **[THÔNG TƯ]`<LOAI_VAN_BAN>`** . **[BỘ TRƯỞNG]`<CHUC_DANH_NGUOI_KY>`** ( Đã ký ) **[Nguyễn Văn Hùng]`<NGUOI_KY>`**

**Thực thể:**
- `[e0]` **02/2023/TT-BVHTTDL** → `SO_HIEU` (span: `[21:22]`)
- `[e1]` **BỘ VĂN HÓA , THỂ THAO VÀ DU LỊCH** → `CO_QUAN_BAN_HANH` (span: `[0:6]`)
- `[e2]` **THÔNG TƯ** → `LOAI_VAN_BAN` (span: `[32:33]`)
- `[e3]` **Nguyễn Văn Hùng** → `NGUOI_KY` (span: `[39:40]`)
- `[e4]` **BỘ TRƯỞNG** → `CHUC_DANH_NGUOI_KY` (span: `[34:35]`)

**Quan hệ:**
- (`e0` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e1` BỘ VĂN HÓA , THỂ THAO VÀ DU LỊCH `[CO_QUAN_BAN_HANH]`)
- (`e0` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e2` THÔNG TƯ `[LOAI_VAN_BAN]`)
- (`e0` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **KY_BOI** ]==> (`e3` Nguyễn Văn Hùng `[NGUOI_KY]`)
- (`e3` Nguyễn Văn Hùng `[NGUOI_KY]`) ==[ **GIU_CHUC_VU** ]==> (`e4` BỘ TRƯỞNG `[CHUC_DANH_NGUOI_KY]`)


---

### Mẫu #02_2023_TT-BVHTTDL_159924#preamble_context_3 (Loại: `preamble_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[02/2023/TT-BVHTTDL]`<SO_HIEU>`** của **[Bộ Văn hóa , Thể thao và Du lịch]`<CO_QUAN_BAN_HANH>`** . QUY ĐỊNH MÃ SỐ , TIÊU CHUẨN CHỨC DANH NGHỀ NGHIỆP VÀ XẾP LƯƠNG **[VIÊN CHỨC]`<CHU_THE_CA_NHAN>`** CHUYÊN NGÀNH TUYÊN TRUYỀN VIÊN VĂN HÓA

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **02/2023/TT-BVHTTDL** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Văn hóa , Thể thao và Du lịch** → `CO_QUAN_BAN_HANH` (span: `[4:10]`)
- `[e3]` **VIÊN CHỨC** → `CHU_THE_CA_NHAN` (span: `[20:21]`)

**Quan hệ:**
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Văn hóa , Thể thao và Du lịch `[CO_QUAN_BAN_HANH]`)
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)


---

### Mẫu #02_2023_TT-BVHTTDL_159924#preamble_standalone_4 (Loại: `preamble_standalone`)
> QUY ĐỊNH MÃ SỐ , TIÊU CHUẨN CHỨC DANH NGHỀ NGHIỆP VÀ XẾP LƯƠNG **[VIÊN CHỨC]`<CHU_THE_CA_NHAN>`** CHUYÊN NGÀNH TUYÊN TRUYỀN VIÊN VĂN HÓA

**Thực thể:**
- `[e0]` **VIÊN CHỨC** → `CHU_THE_CA_NHAN` (span: `[9:10]`)


---

### Mẫu #02_2023_TT-BVHTTDL_159924#preamble_context_5 (Loại: `preamble_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[02/2023/TT-BVHTTDL]`<SO_HIEU>`** của **[Bộ Văn hóa , Thể thao và Du lịch]`<CO_QUAN_BAN_HANH>`** . **[Căn cứ]`<TU_KHOA_PHAP_LY>`** **[Luật Viên chức]`<THAM_CHIEU_PHAP_LY>`** **[ngày 15 tháng 11 năm 2010]`<NGAY_THAM_CHIEU>`** ;

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **02/2023/TT-BVHTTDL** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Văn hóa , Thể thao và Du lịch** → `CO_QUAN_BAN_HANH` (span: `[4:10]`)
- `[e3]` **Luật Viên chức** → `THAM_CHIEU_PHAP_LY` (span: `[12:14]`)
- `[e4]` **Căn cứ** → `TU_KHOA_PHAP_LY` (span: `[11:12]`)
- `[e5]` **ngày 15 tháng 11 năm 2010** → `NGAY_THAM_CHIEU` (span: `[14:20]`)

**Quan hệ:**
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Văn hóa , Thể thao và Du lịch `[CO_QUAN_BAN_HANH]`)
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e4` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Luật Viên chức `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Luật Viên chức `[THAM_CHIEU_PHAP_LY]`)
- (`e3` Luật Viên chức `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e5` ngày 15 tháng 11 năm 2010 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #02_2023_TT-BVHTTDL_159924#preamble_standalone_6 (Loại: `preamble_standalone`)
> **[Căn cứ]`<TU_KHOA_PHAP_LY>`** **[Luật Viên chức]`<THAM_CHIEU_PHAP_LY>`** **[ngày 15 tháng 11 năm 2010]`<NGAY_THAM_CHIEU>`** ;

**Thực thể:**
- `[e0]` **Luật Viên chức** → `THAM_CHIEU_PHAP_LY` (span: `[1:3]`)
- `[e1]` **Căn cứ** → `TU_KHOA_PHAP_LY` (span: `[0:1]`)
- `[e2]` **ngày 15 tháng 11 năm 2010** → `NGAY_THAM_CHIEU` (span: `[3:9]`)

**Quan hệ:**
- (`e1` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e0` Luật Viên chức `[THAM_CHIEU_PHAP_LY]`)
- (`e0` Luật Viên chức `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e2` ngày 15 tháng 11 năm 2010 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #02_2023_TT-BVHTTDL_159924#preamble_context_7 (Loại: `preamble_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[02/2023/TT-BVHTTDL]`<SO_HIEU>`** của **[Bộ Văn hóa , Thể thao và Du lịch]`<CO_QUAN_BAN_HANH>`** . **[Căn cứ]`<TU_KHOA_PHAP_LY>`** **[Luật sửa đổi , bổ sung một số điều của Luật Cán bộ]`<THAM_CHIEU_PHAP_LY>`** , công chức và **[Luật Viên chức]`<THAM_CHIEU_PHAP_LY>`** **[ngày 25 tháng 11 năm 2019]`<NGAY_THAM_CHIEU>`** ;

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **02/2023/TT-BVHTTDL** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Văn hóa , Thể thao và Du lịch** → `CO_QUAN_BAN_HANH` (span: `[4:10]`)
- `[e3]` **Luật sửa đổi , bổ sung một số điều của Luật Cán bộ** → `THAM_CHIEU_PHAP_LY` (span: `[12:21]`)
- `[e4]` **Luật Viên chức** → `THAM_CHIEU_PHAP_LY` (span: `[24:26]`)
- `[e5]` **Căn cứ** → `TU_KHOA_PHAP_LY` (span: `[11:12]`)
- `[e6]` **ngày 25 tháng 11 năm 2019** → `NGAY_THAM_CHIEU` (span: `[26:32]`)

**Quan hệ:**
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Văn hóa , Thể thao và Du lịch `[CO_QUAN_BAN_HANH]`)
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e5` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Luật sửa đổi , bổ sung một số điều của Luật Cán bộ `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Luật sửa đổi , bổ sung một số điều của Luật Cán bộ `[THAM_CHIEU_PHAP_LY]`)
- (`e5` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e4` Luật Viên chức `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e4` Luật Viên chức `[THAM_CHIEU_PHAP_LY]`)
- (`e4` Luật Viên chức `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e6` ngày 25 tháng 11 năm 2019 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #02_2023_TT-BVHTTDL_159924#preamble_standalone_8 (Loại: `preamble_standalone`)
> **[Căn cứ]`<TU_KHOA_PHAP_LY>`** **[Luật sửa đổi , bổ sung một số điều của Luật Cán bộ]`<THAM_CHIEU_PHAP_LY>`** , công chức và **[Luật Viên chức]`<THAM_CHIEU_PHAP_LY>`** **[ngày 25 tháng 11 năm 2019]`<NGAY_THAM_CHIEU>`** ;

**Thực thể:**
- `[e0]` **Luật sửa đổi , bổ sung một số điều của Luật Cán bộ** → `THAM_CHIEU_PHAP_LY` (span: `[1:10]`)
- `[e1]` **Luật Viên chức** → `THAM_CHIEU_PHAP_LY` (span: `[13:15]`)
- `[e2]` **Căn cứ** → `TU_KHOA_PHAP_LY` (span: `[0:1]`)
- `[e3]` **ngày 25 tháng 11 năm 2019** → `NGAY_THAM_CHIEU` (span: `[15:21]`)

**Quan hệ:**
- (`e2` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e0` Luật sửa đổi , bổ sung một số điều của Luật Cán bộ `[THAM_CHIEU_PHAP_LY]`)
- (`e2` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e1` Luật Viên chức `[THAM_CHIEU_PHAP_LY]`)
- (`e1` Luật Viên chức `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e3` ngày 25 tháng 11 năm 2019 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #02_2023_TT-BVHTTDL_159924#preamble_context_9 (Loại: `preamble_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[02/2023/TT-BVHTTDL]`<SO_HIEU>`** của **[Bộ Văn hóa , Thể thao và Du lịch]`<CO_QUAN_BAN_HANH>`** . **[Căn cứ]`<TU_KHOA_PHAP_LY>`** **[Nghị định số 204/2004/NĐ-CP]`<THAM_CHIEU_PHAP_LY>`** **[ngày 14 tháng 12 năm 2004]`<NGAY_THAM_CHIEU>`** của **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** về chế độ **[tiền lương]`<TAI_SAN_VAT_CHAT>`** đối với **[cán bộ , công chức , viên chức]`<CHU_THE_CA_NHAN>`** và lực lượng vũ trang và **[Nghị định số 17/2013/NĐ-CP]`<THAM_CHIEU_PHAP_LY>`** **[ngày 19 tháng 02 năm 2013]`<NGAY_THAM_CHIEU>`** của **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** **[sửa đổi , bổ sung một số điều của]`<TU_KHOA_PHAP_LY>`** **[Nghị định số 204/2004/NĐ-CP]`<THAM_CHIEU_PHAP_LY>`** **[ngày 14 tháng 12 năm 2004]`<NGAY_THAM_CHIEU>`** của **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** về chế độ **[tiền lương]`<TAI_SAN_VAT_CHAT>`** đối với **[cán bộ , công chức , viên chức]`<CHU_THE_CA_NHAN>`** và lực lượng vũ trang ;

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **02/2023/TT-BVHTTDL** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Văn hóa , Thể thao và Du lịch** → `CO_QUAN_BAN_HANH` (span: `[4:10]`)
- `[e3]` **Nghị định số 204/2004/NĐ-CP** → `THAM_CHIEU_PHAP_LY` (span: `[12:15]`)
- `[e4]` **Nghị định số 17/2013/NĐ-CP** → `THAM_CHIEU_PHAP_LY` (span: `[36:39]`)
- `[e5]` **Nghị định số 204/2004/NĐ-CP** → `THAM_CHIEU_PHAP_LY` (span: `[53:56]`)
- `[e6]` **Căn cứ** → `TU_KHOA_PHAP_LY` (span: `[11:12]`)
- `[e7]` **sửa đổi , bổ sung một số điều của** → `TU_KHOA_PHAP_LY` (span: `[47:53]`)
- `[e8]` **ngày 14 tháng 12 năm 2004** → `NGAY_THAM_CHIEU` (span: `[15:21]`)
- `[e9]` **ngày 19 tháng 02 năm 2013** → `NGAY_THAM_CHIEU` (span: `[39:45]`)
- `[e10]` **ngày 14 tháng 12 năm 2004** → `NGAY_THAM_CHIEU` (span: `[56:62]`)
- `[e11]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[22:23]`)
- `[e12]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[46:47]`)
- `[e13]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[63:64]`)
- `[e14]` **cán bộ , công chức , viên chức** → `CHU_THE_CA_NHAN` (span: `[27:32]`)
- `[e15]` **cán bộ , công chức , viên chức** → `CHU_THE_CA_NHAN` (span: `[68:73]`)
- `[e16]` **tiền lương** → `TAI_SAN_VAT_CHAT` (span: `[25:26]`)
- `[e17]` **tiền lương** → `TAI_SAN_VAT_CHAT` (span: `[66:67]`)

**Quan hệ:**
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Văn hóa , Thể thao và Du lịch `[CO_QUAN_BAN_HANH]`)
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e6` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Nghị định số 204/2004/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Nghị định số 204/2004/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e6` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e4` Nghị định số 17/2013/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e4` Nghị định số 17/2013/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e7` sửa đổi , bổ sung một số điều của `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e5` Nghị định số 204/2004/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e5` Nghị định số 204/2004/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e3` Nghị định số 204/2004/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e8` ngày 14 tháng 12 năm 2004 `[NGAY_THAM_CHIEU]`)
- (`e4` Nghị định số 17/2013/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e9` ngày 19 tháng 02 năm 2013 `[NGAY_THAM_CHIEU]`)
- (`e5` Nghị định số 204/2004/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e10` ngày 14 tháng 12 năm 2004 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #02_2023_TT-BVHTTDL_159924#preamble_standalone_10 (Loại: `preamble_standalone`)
> **[Căn cứ]`<TU_KHOA_PHAP_LY>`** **[Nghị định số 204/2004/NĐ-CP]`<THAM_CHIEU_PHAP_LY>`** **[ngày 14 tháng 12 năm 2004]`<NGAY_THAM_CHIEU>`** của **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** về chế độ **[tiền lương]`<TAI_SAN_VAT_CHAT>`** đối với **[cán bộ , công chức , viên chức]`<CHU_THE_CA_NHAN>`** và lực lượng vũ trang và **[Nghị định số 17/2013/NĐ-CP]`<THAM_CHIEU_PHAP_LY>`** **[ngày 19 tháng 02 năm 2013]`<NGAY_THAM_CHIEU>`** của **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** **[sửa đổi , bổ sung một số điều của]`<TU_KHOA_PHAP_LY>`** **[Nghị định số 204/2004/NĐ-CP]`<THAM_CHIEU_PHAP_LY>`** **[ngày 14 tháng 12 năm 2004]`<NGAY_THAM_CHIEU>`** của **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** về chế độ **[tiền lương]`<TAI_SAN_VAT_CHAT>`** đối với **[cán bộ , công chức , viên chức]`<CHU_THE_CA_NHAN>`** và lực lượng vũ trang ;

**Thực thể:**
- `[e0]` **Nghị định số 204/2004/NĐ-CP** → `THAM_CHIEU_PHAP_LY` (span: `[1:4]`)
- `[e1]` **Nghị định số 17/2013/NĐ-CP** → `THAM_CHIEU_PHAP_LY` (span: `[25:28]`)
- `[e2]` **Nghị định số 204/2004/NĐ-CP** → `THAM_CHIEU_PHAP_LY` (span: `[42:45]`)
- `[e3]` **Căn cứ** → `TU_KHOA_PHAP_LY` (span: `[0:1]`)
- `[e4]` **sửa đổi , bổ sung một số điều của** → `TU_KHOA_PHAP_LY` (span: `[36:42]`)
- `[e5]` **ngày 14 tháng 12 năm 2004** → `NGAY_THAM_CHIEU` (span: `[4:10]`)
- `[e6]` **ngày 19 tháng 02 năm 2013** → `NGAY_THAM_CHIEU` (span: `[28:34]`)
- `[e7]` **ngày 14 tháng 12 năm 2004** → `NGAY_THAM_CHIEU` (span: `[45:51]`)
- `[e8]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[11:12]`)
- `[e9]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[35:36]`)
- `[e10]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[52:53]`)
- `[e11]` **cán bộ , công chức , viên chức** → `CHU_THE_CA_NHAN` (span: `[16:21]`)
- `[e12]` **cán bộ , công chức , viên chức** → `CHU_THE_CA_NHAN` (span: `[57:62]`)
- `[e13]` **tiền lương** → `TAI_SAN_VAT_CHAT` (span: `[14:15]`)
- `[e14]` **tiền lương** → `TAI_SAN_VAT_CHAT` (span: `[55:56]`)

**Quan hệ:**
- (`e3` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e0` Nghị định số 204/2004/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e8` Chính phủ `[CO_QUAN_THAM_QUYEN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e0` Nghị định số 204/2004/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e3` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e1` Nghị định số 17/2013/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e11` cán bộ , công chức , viên chức `[CHU_THE_CA_NHAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e1` Nghị định số 17/2013/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e4` sửa đổi , bổ sung một số điều của `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e2` Nghị định số 204/2004/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e9` Chính phủ `[CO_QUAN_THAM_QUYEN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e2` Nghị định số 204/2004/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e0` Nghị định số 204/2004/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e5` ngày 14 tháng 12 năm 2004 `[NGAY_THAM_CHIEU]`)
- (`e1` Nghị định số 17/2013/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e6` ngày 19 tháng 02 năm 2013 `[NGAY_THAM_CHIEU]`)
- (`e2` Nghị định số 204/2004/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e7` ngày 14 tháng 12 năm 2004 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #02_2023_TT-BVHTTDL_159924#preamble_context_11 (Loại: `preamble_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[02/2023/TT-BVHTTDL]`<SO_HIEU>`** của **[Bộ Văn hóa , Thể thao và Du lịch]`<CO_QUAN_BAN_HANH>`** . **[Căn cứ]`<TU_KHOA_PHAP_LY>`** **[Nghị định số 01/2023/NĐ-CP]`<THAM_CHIEU_PHAP_LY>`** **[ngày 16 tháng 01 năm 2023]`<NGAY_THAM_CHIEU>`** của **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** quy định chức năng , nhiệm vụ , quyền hạn và cơ cấu tổ chức của Bộ Văn hoá , Thể thao và Du lịch ;

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **02/2023/TT-BVHTTDL** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Văn hóa , Thể thao và Du lịch** → `CO_QUAN_BAN_HANH` (span: `[4:10]`)
- `[e3]` **Nghị định số 01/2023/NĐ-CP** → `THAM_CHIEU_PHAP_LY` (span: `[12:15]`)
- `[e4]` **Căn cứ** → `TU_KHOA_PHAP_LY` (span: `[11:12]`)
- `[e5]` **ngày 16 tháng 01 năm 2023** → `NGAY_THAM_CHIEU` (span: `[15:21]`)
- `[e6]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[22:23]`)

**Quan hệ:**
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Văn hóa , Thể thao và Du lịch `[CO_QUAN_BAN_HANH]`)
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e4` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Nghị định số 01/2023/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Nghị định số 01/2023/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e3` Nghị định số 01/2023/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e5` ngày 16 tháng 01 năm 2023 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #02_2023_TT-BVHTTDL_159924#preamble_standalone_12 (Loại: `preamble_standalone`)
> **[Căn cứ]`<TU_KHOA_PHAP_LY>`** **[Nghị định số 01/2023/NĐ-CP]`<THAM_CHIEU_PHAP_LY>`** **[ngày 16 tháng 01 năm 2023]`<NGAY_THAM_CHIEU>`** của **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** quy định chức năng , nhiệm vụ , quyền hạn và cơ cấu tổ chức của Bộ Văn hoá , Thể thao và Du lịch ;

**Thực thể:**
- `[e0]` **Nghị định số 01/2023/NĐ-CP** → `THAM_CHIEU_PHAP_LY` (span: `[1:4]`)
- `[e1]` **Căn cứ** → `TU_KHOA_PHAP_LY` (span: `[0:1]`)
- `[e2]` **ngày 16 tháng 01 năm 2023** → `NGAY_THAM_CHIEU` (span: `[4:10]`)
- `[e3]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[11:12]`)

**Quan hệ:**
- (`e1` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e0` Nghị định số 01/2023/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e3` Chính phủ `[CO_QUAN_THAM_QUYEN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e0` Nghị định số 01/2023/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e0` Nghị định số 01/2023/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e2` ngày 16 tháng 01 năm 2023 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #02_2023_TT-BVHTTDL_159924#preamble_context_13 (Loại: `preamble_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[02/2023/TT-BVHTTDL]`<SO_HIEU>`** của **[Bộ Văn hóa , Thể thao và Du lịch]`<CO_QUAN_BAN_HANH>`** . **[Căn cứ]`<TU_KHOA_PHAP_LY>`** **[Nghị định số 115/2020/NĐ-CP]`<THAM_CHIEU_PHAP_LY>`** **[ngày 25 tháng 9 năm 2020]`<NGAY_THAM_CHIEU>`** của **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** quy định về tuyển dụng , sử dụng và quản lý **[viên chức]`<CHU_THE_CA_NHAN>`** ;

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **02/2023/TT-BVHTTDL** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Văn hóa , Thể thao và Du lịch** → `CO_QUAN_BAN_HANH` (span: `[4:10]`)
- `[e3]` **Nghị định số 115/2020/NĐ-CP** → `THAM_CHIEU_PHAP_LY` (span: `[12:15]`)
- `[e4]` **Căn cứ** → `TU_KHOA_PHAP_LY` (span: `[11:12]`)
- `[e5]` **ngày 25 tháng 9 năm 2020** → `NGAY_THAM_CHIEU` (span: `[15:21]`)
- `[e6]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[22:23]`)
- `[e7]` **viên chức** → `CHU_THE_CA_NHAN` (span: `[30:31]`)

**Quan hệ:**
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Văn hóa , Thể thao và Du lịch `[CO_QUAN_BAN_HANH]`)
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e4` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Nghị định số 115/2020/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Nghị định số 115/2020/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e3` Nghị định số 115/2020/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e5` ngày 25 tháng 9 năm 2020 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #02_2023_TT-BVHTTDL_159924#preamble_standalone_14 (Loại: `preamble_standalone`)
> **[Căn cứ]`<TU_KHOA_PHAP_LY>`** **[Nghị định số 115/2020/NĐ-CP]`<THAM_CHIEU_PHAP_LY>`** **[ngày 25 tháng 9 năm 2020]`<NGAY_THAM_CHIEU>`** của **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** quy định về tuyển dụng , sử dụng và quản lý **[viên chức]`<CHU_THE_CA_NHAN>`** ;

**Thực thể:**
- `[e0]` **Nghị định số 115/2020/NĐ-CP** → `THAM_CHIEU_PHAP_LY` (span: `[1:4]`)
- `[e1]` **Căn cứ** → `TU_KHOA_PHAP_LY` (span: `[0:1]`)
- `[e2]` **ngày 25 tháng 9 năm 2020** → `NGAY_THAM_CHIEU` (span: `[4:10]`)
- `[e3]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[11:12]`)
- `[e4]` **viên chức** → `CHU_THE_CA_NHAN` (span: `[19:20]`)

**Quan hệ:**
- (`e1` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e0` Nghị định số 115/2020/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e3` Chính phủ `[CO_QUAN_THAM_QUYEN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e0` Nghị định số 115/2020/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e0` Nghị định số 115/2020/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e2` ngày 25 tháng 9 năm 2020 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #02_2023_TT-BVHTTDL_159924#preamble_context_15 (Loại: `preamble_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[02/2023/TT-BVHTTDL]`<SO_HIEU>`** của **[Bộ Văn hóa , Thể thao và Du lịch]`<CO_QUAN_BAN_HANH>`** . Theo đề nghị của Vụ trưởng Vụ Tổ chức **[cán bộ]`<CHU_THE_CA_NHAN>`** ;

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **02/2023/TT-BVHTTDL** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Văn hóa , Thể thao và Du lịch** → `CO_QUAN_BAN_HANH` (span: `[4:10]`)
- `[e3]` **cán bộ** → `CHU_THE_CA_NHAN` (span: `[17:18]`)

**Quan hệ:**
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Văn hóa , Thể thao và Du lịch `[CO_QUAN_BAN_HANH]`)
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)


---

### Mẫu #02_2023_TT-BVHTTDL_159924#preamble_standalone_16 (Loại: `preamble_standalone`)
> Theo đề nghị của Vụ trưởng Vụ Tổ chức **[cán bộ]`<CHU_THE_CA_NHAN>`** ;

**Thực thể:**
- `[e0]` **cán bộ** → `CHU_THE_CA_NHAN` (span: `[6:7]`)


---

### Mẫu #02_2023_TT-BVHTTDL_159924#body_context_17 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[02/2023/TT-BVHTTDL]`<SO_HIEU>`** ban hành **[ngày 21 tháng 02 năm 2023]`<NGAY_BAN_HANH>`** bởi **[Bộ Văn hóa , Thể thao và Du lịch]`<CO_QUAN_BAN_HANH>`** . **[Chương I. QUY ĐỊNH CHUNG]`<CHUONG>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **02/2023/TT-BVHTTDL** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Văn hóa , Thể thao và Du lịch** → `CO_QUAN_BAN_HANH` (span: `[11:17]`)
- `[e3]` **ngày 21 tháng 02 năm 2023** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Chương I. QUY ĐỊNH CHUNG** → `CHUONG` (span: `[18:22]`)

**Quan hệ:**
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Văn hóa , Thể thao và Du lịch `[CO_QUAN_BAN_HANH]`)
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 21 tháng 02 năm 2023 `[NGAY_BAN_HANH]`)
- (`e4` Chương I. QUY ĐỊNH CHUNG `[CHUONG]`) ==[ **THUOC_VE** ]==> (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`)


---

### Mẫu #02_2023_TT-BVHTTDL_159924#body_context_18 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[02/2023/TT-BVHTTDL]`<SO_HIEU>`** ban hành **[ngày 21 tháng 02 năm 2023]`<NGAY_BAN_HANH>`** bởi **[Bộ Văn hóa , Thể thao và Du lịch]`<CO_QUAN_BAN_HANH>`** . **[Điều 1]`<DIEU>`** . **[1 . Thông tư này quy định mã số , tiêu chuẩn chức danh nghề nghiệp và xếp lương **[viên chức]`<CHU_THE_CA_NHAN>`** chuyên ngành tuyên truyền viên văn hóa .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **02/2023/TT-BVHTTDL** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Văn hóa , Thể thao và Du lịch** → `CO_QUAN_BAN_HANH` (span: `[11:17]`)
- `[e3]` **ngày 21 tháng 02 năm 2023** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 1** → `DIEU` (span: `[18:20]`)
- `[e5]` **1 . Thông tư này quy định mã số , tiêu chuẩn chức danh nghề nghiệp và xếp lương viên chức chuyên ngành tuyên truyền viên văn hóa .** → `KHOAN` (span: `[21:39]`)
- `[e6]` **viên chức** → `CHU_THE_CA_NHAN` (span: `[34:35]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Văn hóa , Thể thao và Du lịch `[CO_QUAN_BAN_HANH]`)
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 21 tháng 02 năm 2023 `[NGAY_BAN_HANH]`)
- (`e4` Điều 1 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`)
- (`e5` 1 . Thông tư này quy định mã số , tiêu chuẩn chức danh nghề nghiệp và xếp lương viên chức chuyên ngành tuyên truyền viên văn hóa . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 1 `[DIEU]`)


---

### Mẫu #02_2023_TT-BVHTTDL_159924#body_context_19 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[02/2023/TT-BVHTTDL]`<SO_HIEU>`** ban hành **[ngày 21 tháng 02 năm 2023]`<NGAY_BAN_HANH>`** bởi **[Bộ Văn hóa , Thể thao và Du lịch]`<CO_QUAN_BAN_HANH>`** . **[Điều 1]`<DIEU>`** . **[2 . Thông tư này áp dụng đối với **[viên chức]`<CHU_THE_CA_NHAN>`** tuyên truyền viên văn hóa làm việc trong các **[đơn vị sự nghiệp công lập]`<TO_CHUC_DOANH_NGHIEP>`** và các tổ chức , cá nhân có liên quan .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **02/2023/TT-BVHTTDL** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Văn hóa , Thể thao và Du lịch** → `CO_QUAN_BAN_HANH` (span: `[11:17]`)
- `[e3]` **ngày 21 tháng 02 năm 2023** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 1** → `DIEU` (span: `[18:20]`)
- `[e5]` **2 . Thông tư này áp dụng đối với viên chức tuyên truyền viên văn hóa làm việc trong các đơn vị sự nghiệp công lập và các tổ chức , cá nhân có liên quan .** → `KHOAN` (span: `[21:44]`)
- `[e6]` **đơn vị sự nghiệp công lập** → `TO_CHUC_DOANH_NGHIEP` (span: `[33:36]`) *(lồng trong `e5` (`KHOAN`))*
- `[e7]` **viên chức** → `CHU_THE_CA_NHAN` (span: `[27:28]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Văn hóa , Thể thao và Du lịch `[CO_QUAN_BAN_HANH]`)
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 21 tháng 02 năm 2023 `[NGAY_BAN_HANH]`)
- (`e4` Điều 1 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`)
- (`e5` 2 . Thông tư này áp dụng đối với viên chức tuyên truyền viên văn hóa làm việc trong các đơn vị sự nghiệp công lập và các tổ chức , cá nhân có liên quan . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 1 `[DIEU]`)


---

### Mẫu #02_2023_TT-BVHTTDL_159924#body_standalone_20 (Loại: `body_standalone`)
> **[Điều 1]`<DIEU>`** . **[2 . Thông tư này áp dụng đối với **[viên chức]`<CHU_THE_CA_NHAN>`** tuyên truyền viên văn hóa làm việc trong các **[đơn vị sự nghiệp công lập]`<TO_CHUC_DOANH_NGHIEP>`** và các tổ chức , cá nhân có liên quan .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 1** → `DIEU` (span: `[0:2]`)
- `[e1]` **2 . Thông tư này áp dụng đối với viên chức tuyên truyền viên văn hóa làm việc trong các đơn vị sự nghiệp công lập và các tổ chức , cá nhân có liên quan .** → `KHOAN` (span: `[3:26]`)
- `[e2]` **đơn vị sự nghiệp công lập** → `TO_CHUC_DOANH_NGHIEP` (span: `[15:18]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **viên chức** → `CHU_THE_CA_NHAN` (span: `[9:10]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 2 . Thông tư này áp dụng đối với viên chức tuyên truyền viên văn hóa làm việc trong các đơn vị sự nghiệp công lập và các tổ chức , cá nhân có liên quan . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 1 `[DIEU]`)


---

### Mẫu #02_2023_TT-BVHTTDL_159924#body_context_21 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[02/2023/TT-BVHTTDL]`<SO_HIEU>`** ban hành **[ngày 21 tháng 02 năm 2023]`<NGAY_BAN_HANH>`** bởi **[Bộ Văn hóa , Thể thao và Du lịch]`<CO_QUAN_BAN_HANH>`** . **[Chương I]`<CHUONG>`** . **[Điều 2 . Mã số các chức danh nghề nghiệp **[viên chức]`<CHU_THE_CA_NHAN>`** chuyên ngành tuyên truyền viên văn hóa]`<DIEU>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **02/2023/TT-BVHTTDL** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Văn hóa , Thể thao và Du lịch** → `CO_QUAN_BAN_HANH` (span: `[11:17]`)
- `[e3]` **ngày 21 tháng 02 năm 2023** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Chương I** → `CHUONG` (span: `[18:20]`)
- `[e5]` **Điều 2 . Mã số các chức danh nghề nghiệp viên chức chuyên ngành tuyên truyền viên văn hóa** → `DIEU` (span: `[21:32]`)
- `[e6]` **viên chức** → `CHU_THE_CA_NHAN` (span: `[28:29]`) *(lồng trong `e5` (`DIEU`))*

**Quan hệ:**
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Văn hóa , Thể thao và Du lịch `[CO_QUAN_BAN_HANH]`)
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 21 tháng 02 năm 2023 `[NGAY_BAN_HANH]`)
- (`e4` Chương I `[CHUONG]`) ==[ **THUOC_VE** ]==> (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`)
- (`e5` Điều 2 . Mã số các chức danh nghề nghiệp viên chức chuyên ngành tuyên truyền viên văn hóa `[DIEU]`) ==[ **THUOC_VE** ]==> (`e4` Chương I `[CHUONG]`)


---

### Mẫu #02_2023_TT-BVHTTDL_159924#body_context_22 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[02/2023/TT-BVHTTDL]`<SO_HIEU>`** ban hành **[ngày 21 tháng 02 năm 2023]`<NGAY_BAN_HANH>`** bởi **[Bộ Văn hóa , Thể thao và Du lịch]`<CO_QUAN_BAN_HANH>`** . **[Điều 2]`<DIEU>`** . **[3 . Tuyên truyền viên văn hóa trung cấp Mã số : V. 10.10.36]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **02/2023/TT-BVHTTDL** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Văn hóa , Thể thao và Du lịch** → `CO_QUAN_BAN_HANH` (span: `[11:17]`)
- `[e3]` **ngày 21 tháng 02 năm 2023** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 2** → `DIEU` (span: `[18:20]`)
- `[e5]` **3 . Tuyên truyền viên văn hóa trung cấp Mã số : V. 10.10.36** → `KHOAN` (span: `[21:30]`)

**Quan hệ:**
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Văn hóa , Thể thao và Du lịch `[CO_QUAN_BAN_HANH]`)
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 21 tháng 02 năm 2023 `[NGAY_BAN_HANH]`)
- (`e4` Điều 2 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`)
- (`e5` 3 . Tuyên truyền viên văn hóa trung cấp Mã số : V. 10.10.36 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 2 `[DIEU]`)


---

### Mẫu #02_2023_TT-BVHTTDL_159924#body_context_23 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[02/2023/TT-BVHTTDL]`<SO_HIEU>`** ban hành **[ngày 21 tháng 02 năm 2023]`<NGAY_BAN_HANH>`** bởi **[Bộ Văn hóa , Thể thao và Du lịch]`<CO_QUAN_BAN_HANH>`** . **[Chương I]`<CHUONG>`** . **[Điều 3 . Tiêu chuẩn về đạo đức nghề nghiệp của **[viên chức]`<CHU_THE_CA_NHAN>`** chuyên ngành tuyên truyền viên văn hóa]`<DIEU>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **02/2023/TT-BVHTTDL** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Văn hóa , Thể thao và Du lịch** → `CO_QUAN_BAN_HANH` (span: `[11:17]`)
- `[e3]` **ngày 21 tháng 02 năm 2023** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Chương I** → `CHUONG` (span: `[18:20]`)
- `[e5]` **Điều 3 . Tiêu chuẩn về đạo đức nghề nghiệp của viên chức chuyên ngành tuyên truyền viên văn hóa** → `DIEU` (span: `[21:33]`)
- `[e6]` **viên chức** → `CHU_THE_CA_NHAN` (span: `[29:30]`) *(lồng trong `e5` (`DIEU`))*

**Quan hệ:**
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Văn hóa , Thể thao và Du lịch `[CO_QUAN_BAN_HANH]`)
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 21 tháng 02 năm 2023 `[NGAY_BAN_HANH]`)
- (`e4` Chương I `[CHUONG]`) ==[ **THUOC_VE** ]==> (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`)
- (`e5` Điều 3 . Tiêu chuẩn về đạo đức nghề nghiệp của viên chức chuyên ngành tuyên truyền viên văn hóa `[DIEU]`) ==[ **THUOC_VE** ]==> (`e4` Chương I `[CHUONG]`)


---

### Mẫu #02_2023_TT-BVHTTDL_159924#body_context_24 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[02/2023/TT-BVHTTDL]`<SO_HIEU>`** của **[Bộ Văn hóa , Thể thao và Du lịch]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Lao động - Thương binh và Xã hội]`<LINH_VUC>`** . **[Điều 3]`<DIEU>`** . **[1 . Có trách nhiệm với công việc được giao , tuân thủ các quy định của pháp luật ; thực hiện đúng và đầy đủ nghĩa vụ của **[viên chức]`<CHU_THE_CA_NHAN>`** trong hoạt động nghề nghiệp .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **02/2023/TT-BVHTTDL** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Văn hóa , Thể thao và Du lịch** → `CO_QUAN_BAN_HANH` (span: `[4:10]`)
- `[e3]` **Lao động - Thương binh và Xã hội** → `LINH_VUC` (span: `[12:17]`)
- `[e4]` **Điều 3** → `DIEU` (span: `[18:20]`)
- `[e5]` **1 . Có trách nhiệm với công việc được giao , tuân thủ các quy định của pháp luật ; thực hiện đúng và đầy đủ nghĩa vụ của viên chức trong hoạt động nghề nghiệp .** → `KHOAN` (span: `[21:47]`)
- `[e6]` **viên chức** → `CHU_THE_CA_NHAN` (span: `[42:43]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Văn hóa , Thể thao và Du lịch `[CO_QUAN_BAN_HANH]`)
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Lao động - Thương binh và Xã hội `[LINH_VUC]`)
- (`e4` Điều 3 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`)
- (`e5` 1 . Có trách nhiệm với công việc được giao , tuân thủ các quy định của pháp luật ; thực hiện đúng và đầy đủ nghĩa vụ của viên chức trong hoạt động nghề nghiệp . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 3 `[DIEU]`)
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Lao động - Thương binh và Xã hội `[LINH_VUC]`)
- (`e5` 1 . Có trách nhiệm với công việc được giao , tuân thủ các quy định của pháp luật ; thực hiện đúng và đầy đủ nghĩa vụ của viên chức trong hoạt động nghề nghiệp . `[KHOAN]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Lao động - Thương binh và Xã hội `[LINH_VUC]`)


---

### Mẫu #02_2023_TT-BVHTTDL_159924#body_standalone_25 (Loại: `body_standalone`)
> **[Điều 3]`<DIEU>`** . **[1 . Có trách nhiệm với công việc được giao , tuân thủ các quy định của pháp luật ; thực hiện đúng và đầy đủ nghĩa vụ của **[viên chức]`<CHU_THE_CA_NHAN>`** trong hoạt động nghề nghiệp .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 3** → `DIEU` (span: `[0:2]`)
- `[e1]` **1 . Có trách nhiệm với công việc được giao , tuân thủ các quy định của pháp luật ; thực hiện đúng và đầy đủ nghĩa vụ của viên chức trong hoạt động nghề nghiệp .** → `KHOAN` (span: `[3:29]`)
- `[e2]` **viên chức** → `CHU_THE_CA_NHAN` (span: `[24:25]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 1 . Có trách nhiệm với công việc được giao , tuân thủ các quy định của pháp luật ; thực hiện đúng và đầy đủ nghĩa vụ của viên chức trong hoạt động nghề nghiệp . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 3 `[DIEU]`)


---

### Mẫu #02_2023_TT-BVHTTDL_159924#body_context_26 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[02/2023/TT-BVHTTDL]`<SO_HIEU>`** ban hành **[ngày 21 tháng 02 năm 2023]`<NGAY_BAN_HANH>`** bởi **[Bộ Văn hóa , Thể thao và Du lịch]`<CO_QUAN_BAN_HANH>`** . **[Chương II. TIÊU CHUẨN CHỨC DANH NGHỀ NGHIỆP]`<CHUONG>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **02/2023/TT-BVHTTDL** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Văn hóa , Thể thao và Du lịch** → `CO_QUAN_BAN_HANH` (span: `[11:17]`)
- `[e3]` **ngày 21 tháng 02 năm 2023** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Chương II. TIÊU CHUẨN CHỨC DANH NGHỀ NGHIỆP** → `CHUONG` (span: `[18:23]`)

**Quan hệ:**
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Văn hóa , Thể thao và Du lịch `[CO_QUAN_BAN_HANH]`)
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 21 tháng 02 năm 2023 `[NGAY_BAN_HANH]`)
- (`e4` Chương II. TIÊU CHUẨN CHỨC DANH NGHỀ NGHIỆP `[CHUONG]`) ==[ **THUOC_VE** ]==> (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`)


---

### Mẫu #02_2023_TT-BVHTTDL_159924#body_context_27 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[02/2023/TT-BVHTTDL]`<SO_HIEU>`** của **[Bộ Văn hóa , Thể thao và Du lịch]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Lao động - Thương binh và Xã hội]`<LINH_VUC>`** . **[Điều 4]`<DIEU>`** . **[Khoản 1]`<KHOAN>`** . **[c ) Chủ trì tổ chức và thực hiện biên tập nội dung chương trình tuyên truyền phục vụ nhiệm vụ chính trị , kinh tế , văn hóa , xã hội ; các phong trào , các cuộc vận động lớn ; các ngày lễ , kỉ niệm lớn của địa phương và đất nước ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **02/2023/TT-BVHTTDL** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Văn hóa , Thể thao và Du lịch** → `CO_QUAN_BAN_HANH` (span: `[4:10]`)
- `[e3]` **Lao động - Thương binh và Xã hội** → `LINH_VUC` (span: `[12:17]`)
- `[e4]` **Điều 4** → `DIEU` (span: `[18:20]`)
- `[e5]` **Khoản 1** → `KHOAN` (span: `[21:23]`)
- `[e6]` **c ) Chủ trì tổ chức và thực hiện biên tập nội dung chương trình tuyên truyền phục vụ nhiệm vụ chính trị , kinh tế , văn hóa , xã hội ; các phong trào , các cuộc vận động lớn ; các ngày lễ , kỉ niệm lớn của địa phương và đất nước ;** → `DIEM` (span: `[24:63]`)

**Quan hệ:**
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Văn hóa , Thể thao và Du lịch `[CO_QUAN_BAN_HANH]`)
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Lao động - Thương binh và Xã hội `[LINH_VUC]`)
- (`e4` Điều 4 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`)
- (`e5` Khoản 1 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 4 `[DIEU]`)
- (`e6` c ) Chủ trì tổ chức và thực hiện biên tập nội dung chương trình tuyên truyền phục vụ nhiệm vụ chính trị , kinh tế , văn hóa , xã hội ; các phong trào , các cuộc vận động lớn ; các ngày lễ , kỉ niệm lớn của địa phương và đất nước ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e5` Khoản 1 `[KHOAN]`)
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Lao động - Thương binh và Xã hội `[LINH_VUC]`)
- (`e6` c ) Chủ trì tổ chức và thực hiện biên tập nội dung chương trình tuyên truyền phục vụ nhiệm vụ chính trị , kinh tế , văn hóa , xã hội ; các phong trào , các cuộc vận động lớn ; các ngày lễ , kỉ niệm lớn của địa phương và đất nước ; `[DIEM]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Lao động - Thương binh và Xã hội `[LINH_VUC]`)


---

### Mẫu #02_2023_TT-BVHTTDL_159924#body_context_28 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[02/2023/TT-BVHTTDL]`<SO_HIEU>`** ban hành **[ngày 21 tháng 02 năm 2023]`<NGAY_BAN_HANH>`** bởi **[Bộ Văn hóa , Thể thao và Du lịch]`<CO_QUAN_BAN_HANH>`** . **[Điều 4]`<DIEU>`** . **[Khoản 2]`<KHOAN>`** . **[a ) Có **[bằng tốt nghiệp đại học]`<GIAY_TO_HO_SO>`** trở lên phù hợp với chuyên ngành tuyên truyền viên văn hóa ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **02/2023/TT-BVHTTDL** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Văn hóa , Thể thao và Du lịch** → `CO_QUAN_BAN_HANH` (span: `[11:17]`)
- `[e3]` **ngày 21 tháng 02 năm 2023** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 4** → `DIEU` (span: `[18:20]`)
- `[e5]` **Khoản 2** → `KHOAN` (span: `[21:23]`)
- `[e6]` **a ) Có bằng tốt nghiệp đại học trở lên phù hợp với chuyên ngành tuyên truyền viên văn hóa ;** → `DIEM` (span: `[24:38]`)
- `[e7]` **bằng tốt nghiệp đại học** → `GIAY_TO_HO_SO` (span: `[27:30]`) *(lồng trong `e6` (`DIEM`))*

**Quan hệ:**
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Văn hóa , Thể thao và Du lịch `[CO_QUAN_BAN_HANH]`)
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 21 tháng 02 năm 2023 `[NGAY_BAN_HANH]`)
- (`e4` Điều 4 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`)
- (`e5` Khoản 2 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 4 `[DIEU]`)
- (`e6` a ) Có bằng tốt nghiệp đại học trở lên phù hợp với chuyên ngành tuyên truyền viên văn hóa ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e5` Khoản 2 `[KHOAN]`)


---

### Mẫu #02_2023_TT-BVHTTDL_159924#body_context_29 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[02/2023/TT-BVHTTDL]`<SO_HIEU>`** ban hành **[ngày 21 tháng 02 năm 2023]`<NGAY_BAN_HANH>`** bởi **[Bộ Văn hóa , Thể thao và Du lịch]`<CO_QUAN_BAN_HANH>`** . **[Điều 4]`<DIEU>`** . **[Khoản 2]`<KHOAN>`** . **[b ) Có **[chứng chỉ bồi dưỡng]`<GIAY_TO_HO_SO>`** tiêu chuẩn chức danh nghề nghiệp tuyên truyền viên văn hóa .]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **02/2023/TT-BVHTTDL** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Văn hóa , Thể thao và Du lịch** → `CO_QUAN_BAN_HANH` (span: `[11:17]`)
- `[e3]` **ngày 21 tháng 02 năm 2023** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 4** → `DIEU` (span: `[18:20]`)
- `[e5]` **Khoản 2** → `KHOAN` (span: `[21:23]`)
- `[e6]` **b ) Có chứng chỉ bồi dưỡng tiêu chuẩn chức danh nghề nghiệp tuyên truyền viên văn hóa .** → `DIEM` (span: `[24:35]`)
- `[e7]` **chứng chỉ bồi dưỡng** → `GIAY_TO_HO_SO` (span: `[27:29]`) *(lồng trong `e6` (`DIEM`))*

**Quan hệ:**
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Văn hóa , Thể thao và Du lịch `[CO_QUAN_BAN_HANH]`)
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 21 tháng 02 năm 2023 `[NGAY_BAN_HANH]`)
- (`e4` Điều 4 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`)
- (`e5` Khoản 2 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 4 `[DIEU]`)
- (`e6` b ) Có chứng chỉ bồi dưỡng tiêu chuẩn chức danh nghề nghiệp tuyên truyền viên văn hóa . `[DIEM]`) ==[ **THUOC_VE** ]==> (`e5` Khoản 2 `[KHOAN]`)


---

### Mẫu #02_2023_TT-BVHTTDL_159924#body_standalone_30 (Loại: `body_standalone`)
> **[Điều 4]`<DIEU>`** . **[Khoản 2]`<KHOAN>`** . **[b ) Có **[chứng chỉ bồi dưỡng]`<GIAY_TO_HO_SO>`** tiêu chuẩn chức danh nghề nghiệp tuyên truyền viên văn hóa .]`<DIEM>`**

**Thực thể:**
- `[e0]` **Điều 4** → `DIEU` (span: `[0:2]`)
- `[e1]` **Khoản 2** → `KHOAN` (span: `[3:5]`)
- `[e2]` **b ) Có chứng chỉ bồi dưỡng tiêu chuẩn chức danh nghề nghiệp tuyên truyền viên văn hóa .** → `DIEM` (span: `[6:17]`)
- `[e3]` **chứng chỉ bồi dưỡng** → `GIAY_TO_HO_SO` (span: `[9:11]`) *(lồng trong `e2` (`DIEM`))*

**Quan hệ:**
- (`e1` Khoản 2 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 4 `[DIEU]`)
- (`e2` b ) Có chứng chỉ bồi dưỡng tiêu chuẩn chức danh nghề nghiệp tuyên truyền viên văn hóa . `[DIEM]`) ==[ **THUOC_VE** ]==> (`e1` Khoản 2 `[KHOAN]`)


---

### Mẫu #02_2023_TT-BVHTTDL_159924#body_context_31 (Loại: `body_context`)
> **[Bộ Văn hóa , Thể thao và Du lịch]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[02/2023/TT-BVHTTDL]`<SO_HIEU>`** . **[Điều 4]`<DIEU>`** . **[3 . Tiêu chuẩn về năng lực chuyên môn , nghiệp vụ :]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[7:8]`)
- `[e1]` **02/2023/TT-BVHTTDL** → `SO_HIEU` (span: `[9:10]`)
- `[e2]` **Bộ Văn hóa , Thể thao và Du lịch** → `CO_QUAN_BAN_HANH` (span: `[0:6]`)
- `[e3]` **Điều 4** → `DIEU` (span: `[11:13]`)
- `[e4]` **3 . Tiêu chuẩn về năng lực chuyên môn , nghiệp vụ :** → `KHOAN` (span: `[14:23]`)

**Quan hệ:**
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Văn hóa , Thể thao và Du lịch `[CO_QUAN_BAN_HANH]`)
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 4 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`)
- (`e4` 3 . Tiêu chuẩn về năng lực chuyên môn , nghiệp vụ : `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 4 `[DIEU]`)


---

### Mẫu #02_2023_TT-BVHTTDL_159924#body_context_32 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[02/2023/TT-BVHTTDL]`<SO_HIEU>`** ban hành **[ngày 21 tháng 02 năm 2023]`<NGAY_BAN_HANH>`** bởi **[Bộ Văn hóa , Thể thao và Du lịch]`<CO_QUAN_BAN_HANH>`** . **[Điều 4]`<DIEU>`** . **[Khoản 3]`<KHOAN>`** . **[d ) Có chuyên môn về **[lĩnh vực văn hóa]`<LINH_VUC>`** , nghệ thuật ; am hiểu kiến thức , kỹ năng nghiệp vụ tuyên truyền ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **02/2023/TT-BVHTTDL** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Văn hóa , Thể thao và Du lịch** → `CO_QUAN_BAN_HANH` (span: `[11:17]`)
- `[e3]` **ngày 21 tháng 02 năm 2023** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 4** → `DIEU` (span: `[18:20]`)
- `[e5]` **Khoản 3** → `KHOAN` (span: `[21:23]`)
- `[e6]` **d ) Có chuyên môn về lĩnh vực văn hóa , nghệ thuật ; am hiểu kiến thức , kỹ năng nghiệp vụ tuyên truyền ;** → `DIEM` (span: `[24:41]`)
- `[e7]` **lĩnh vực văn hóa** → `LINH_VUC` (span: `[29:31]`) *(lồng trong `e6` (`DIEM`))*

**Quan hệ:**
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Văn hóa , Thể thao và Du lịch `[CO_QUAN_BAN_HANH]`)
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 21 tháng 02 năm 2023 `[NGAY_BAN_HANH]`)
- (`e4` Điều 4 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`)
- (`e5` Khoản 3 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 4 `[DIEU]`)
- (`e6` d ) Có chuyên môn về lĩnh vực văn hóa , nghệ thuật ; am hiểu kiến thức , kỹ năng nghiệp vụ tuyên truyền ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e5` Khoản 3 `[KHOAN]`)
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e7` lĩnh vực văn hóa `[LINH_VUC]`)
- (`e6` d ) Có chuyên môn về lĩnh vực văn hóa , nghệ thuật ; am hiểu kiến thức , kỹ năng nghiệp vụ tuyên truyền ; `[DIEM]`) ==[ **THUOC_LINH_VUC** ]==> (`e7` lĩnh vực văn hóa `[LINH_VUC]`) *(Quan hệ lồng nhau)*


---

### Mẫu #02_2023_TT-BVHTTDL_159924#body_context_33 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[02/2023/TT-BVHTTDL]`<SO_HIEU>`** của **[Bộ Văn hóa , Thể thao và Du lịch]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Lao động - Thương binh và Xã hội]`<LINH_VUC>`** . **[Điều 4]`<DIEU>`** . **[Khoản 3]`<KHOAN>`** . **[đ ) Có năng lực thu thập , phân tích , tổng hợp và đề xuất các giải pháp để nâng cao chất lượng công tác tuyên truyền ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **02/2023/TT-BVHTTDL** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Văn hóa , Thể thao và Du lịch** → `CO_QUAN_BAN_HANH` (span: `[4:10]`)
- `[e3]` **Lao động - Thương binh và Xã hội** → `LINH_VUC` (span: `[12:17]`)
- `[e4]` **Điều 4** → `DIEU` (span: `[18:20]`)
- `[e5]` **Khoản 3** → `KHOAN` (span: `[21:23]`)
- `[e6]` **đ ) Có năng lực thu thập , phân tích , tổng hợp và đề xuất các giải pháp để nâng cao chất lượng công tác tuyên truyền ;** → `DIEM` (span: `[24:44]`)

**Quan hệ:**
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Văn hóa , Thể thao và Du lịch `[CO_QUAN_BAN_HANH]`)
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Lao động - Thương binh và Xã hội `[LINH_VUC]`)
- (`e4` Điều 4 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`)
- (`e5` Khoản 3 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 4 `[DIEU]`)
- (`e6` đ ) Có năng lực thu thập , phân tích , tổng hợp và đề xuất các giải pháp để nâng cao chất lượng công tác tuyên truyền ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e5` Khoản 3 `[KHOAN]`)
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Lao động - Thương binh và Xã hội `[LINH_VUC]`)
- (`e6` đ ) Có năng lực thu thập , phân tích , tổng hợp và đề xuất các giải pháp để nâng cao chất lượng công tác tuyên truyền ; `[DIEM]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Lao động - Thương binh và Xã hội `[LINH_VUC]`)


---

### Mẫu #02_2023_TT-BVHTTDL_159924#body_context_34 (Loại: `body_context`)
> **[Bộ Văn hóa , Thể thao và Du lịch]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[02/2023/TT-BVHTTDL]`<SO_HIEU>`** . **[Điều 4]`<DIEU>`** . **[Khoản 3]`<KHOAN>`** . **[e ) Có kỹ năng sử dụng công nghệ thông tin cơ bản , sử dụng được ngoại ngữ hoặc sử dụng được tiếng dân tộc thiểu số đối với **[viên chức]`<CHU_THE_CA_NHAN>`** công tác ở vùng dân tộc thiểu số theo yêu cầu vị trí việc làm .]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[7:8]`)
- `[e1]` **02/2023/TT-BVHTTDL** → `SO_HIEU` (span: `[9:10]`)
- `[e2]` **Bộ Văn hóa , Thể thao và Du lịch** → `CO_QUAN_BAN_HANH` (span: `[0:6]`)
- `[e3]` **Điều 4** → `DIEU` (span: `[11:13]`)
- `[e4]` **Khoản 3** → `KHOAN` (span: `[14:16]`)
- `[e5]` **e ) Có kỹ năng sử dụng công nghệ thông tin cơ bản , sử dụng được ngoại ngữ hoặc sử dụng được tiếng dân tộc thiểu số đối với viên chức công tác ở vùng dân tộc thiểu số theo yêu cầu vị trí việc làm .** → `DIEM` (span: `[17:45]`)
- `[e6]` **viên chức** → `CHU_THE_CA_NHAN` (span: `[35:36]`) *(lồng trong `e5` (`DIEM`))*

**Quan hệ:**
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Văn hóa , Thể thao và Du lịch `[CO_QUAN_BAN_HANH]`)
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 4 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`)
- (`e4` Khoản 3 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 4 `[DIEU]`)
- (`e5` e ) Có kỹ năng sử dụng công nghệ thông tin cơ bản , sử dụng được ngoại ngữ hoặc sử dụng được tiếng dân tộc thiểu số đối với viên chức công tác ở vùng dân tộc thiểu số theo yêu cầu vị trí việc làm . `[DIEM]`) ==[ **THUOC_VE** ]==> (`e4` Khoản 3 `[KHOAN]`)


---

### Mẫu #02_2023_TT-BVHTTDL_159924#body_context_35 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[02/2023/TT-BVHTTDL]`<SO_HIEU>`** của **[Bộ Văn hóa , Thể thao và Du lịch]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Lao động - Thương binh và Xã hội]`<LINH_VUC>`** . **[Điều 4]`<DIEU>`** . **[4 . Yêu cầu đối với **[viên chức]`<CHU_THE_CA_NHAN>`** dự thi hoặc xét thăng hạng chức danh nghề nghiệp tuyên truyền viên văn hóa chính : Có thời gian công tác giữ chức danh nghề nghiệp tuyên truyền viên văn hóa hoặc tương đương từ **[đủ 09 năm]`<THOI_HAN>`** trở lên ( không kể thời gian tập sự , thử việc ) . Trường hợp có thời gian tương đương thì phải có ít nhất 01 năm ( **[đủ 12 tháng]`<THOI_HAN>`** ) đang giữ chức danh nghề nghiệp tuyên truyền viên văn hóa tính đến ngày hết thời hạn nộp hồ sơ]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **02/2023/TT-BVHTTDL** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Văn hóa , Thể thao và Du lịch** → `CO_QUAN_BAN_HANH` (span: `[4:10]`)
- `[e3]` **Lao động - Thương binh và Xã hội** → `LINH_VUC` (span: `[12:17]`)
- `[e4]` **Điều 4** → `DIEU` (span: `[18:20]`)
- `[e5]` **4 . Yêu cầu đối với viên chức dự thi hoặc xét thăng hạng chức danh nghề nghiệp tuyên truyền viên văn hóa chính : Có thời gian công tác giữ chức danh nghề nghiệp tuyên truyền viên văn hóa hoặc tương đương từ đủ 09 năm trở lên ( không kể thời gian tập sự , thử việc ) . Trường hợp có thời gian tương đương thì phải có ít nhất 01 năm ( đủ 12 tháng ) đang giữ chức danh nghề nghiệp tuyên truyền viên văn hóa tính đến ngày hết thời hạn nộp hồ sơ** → `KHOAN` (span: `[21:91]`)
- `[e6]` **đủ 09 năm** → `THOI_HAN` (span: `[48:51]`) *(lồng trong `e5` (`KHOAN`))*
- `[e7]` **đủ 12 tháng** → `THOI_HAN` (span: `[74:77]`) *(lồng trong `e5` (`KHOAN`))*
- `[e8]` **viên chức** → `CHU_THE_CA_NHAN` (span: `[25:26]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Văn hóa , Thể thao và Du lịch `[CO_QUAN_BAN_HANH]`)
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Lao động - Thương binh và Xã hội `[LINH_VUC]`)
- (`e4` Điều 4 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`)
- (`e5` 4 . Yêu cầu đối với viên chức dự thi hoặc xét thăng hạng chức danh nghề nghiệp tuyên truyền viên văn hóa chính : Có thời gian công tác giữ chức danh nghề nghiệp tuyên truyền viên văn hóa hoặc tương đương từ đủ 09 năm trở lên ( không kể thời gian tập sự , thử việc ) . Trường hợp có thời gian tương đương thì phải có ít nhất 01 năm ( đủ 12 tháng ) đang giữ chức danh nghề nghiệp tuyên truyền viên văn hóa tính đến ngày hết thời hạn nộp hồ sơ `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 4 `[DIEU]`)
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Lao động - Thương binh và Xã hội `[LINH_VUC]`)
- (`e5` 4 . Yêu cầu đối với viên chức dự thi hoặc xét thăng hạng chức danh nghề nghiệp tuyên truyền viên văn hóa chính : Có thời gian công tác giữ chức danh nghề nghiệp tuyên truyền viên văn hóa hoặc tương đương từ đủ 09 năm trở lên ( không kể thời gian tập sự , thử việc ) . Trường hợp có thời gian tương đương thì phải có ít nhất 01 năm ( đủ 12 tháng ) đang giữ chức danh nghề nghiệp tuyên truyền viên văn hóa tính đến ngày hết thời hạn nộp hồ sơ `[KHOAN]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Lao động - Thương binh và Xã hội `[LINH_VUC]`)


---

### Mẫu #02_2023_TT-BVHTTDL_159924#body_standalone_36 (Loại: `body_standalone`)
> **[Điều 4]`<DIEU>`** . **[4 . Yêu cầu đối với **[viên chức]`<CHU_THE_CA_NHAN>`** dự thi hoặc xét thăng hạng chức danh nghề nghiệp tuyên truyền viên văn hóa chính : Có thời gian công tác giữ chức danh nghề nghiệp tuyên truyền viên văn hóa hoặc tương đương từ **[đủ 09 năm]`<THOI_HAN>`** trở lên ( không kể thời gian tập sự , thử việc ) . Trường hợp có thời gian tương đương thì phải có ít nhất 01 năm ( **[đủ 12 tháng]`<THOI_HAN>`** ) đang giữ chức danh nghề nghiệp tuyên truyền viên văn hóa tính đến ngày hết thời hạn nộp hồ sơ]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 4** → `DIEU` (span: `[0:2]`)
- `[e1]` **4 . Yêu cầu đối với viên chức dự thi hoặc xét thăng hạng chức danh nghề nghiệp tuyên truyền viên văn hóa chính : Có thời gian công tác giữ chức danh nghề nghiệp tuyên truyền viên văn hóa hoặc tương đương từ đủ 09 năm trở lên ( không kể thời gian tập sự , thử việc ) . Trường hợp có thời gian tương đương thì phải có ít nhất 01 năm ( đủ 12 tháng ) đang giữ chức danh nghề nghiệp tuyên truyền viên văn hóa tính đến ngày hết thời hạn nộp hồ sơ** → `KHOAN` (span: `[3:73]`)
- `[e2]` **đủ 09 năm** → `THOI_HAN` (span: `[30:33]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **đủ 12 tháng** → `THOI_HAN` (span: `[56:59]`) *(lồng trong `e1` (`KHOAN`))*
- `[e4]` **viên chức** → `CHU_THE_CA_NHAN` (span: `[7:8]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 4 . Yêu cầu đối với viên chức dự thi hoặc xét thăng hạng chức danh nghề nghiệp tuyên truyền viên văn hóa chính : Có thời gian công tác giữ chức danh nghề nghiệp tuyên truyền viên văn hóa hoặc tương đương từ đủ 09 năm trở lên ( không kể thời gian tập sự , thử việc ) . Trường hợp có thời gian tương đương thì phải có ít nhất 01 năm ( đủ 12 tháng ) đang giữ chức danh nghề nghiệp tuyên truyền viên văn hóa tính đến ngày hết thời hạn nộp hồ sơ `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 4 `[DIEU]`)


---

### Mẫu #02_2023_TT-BVHTTDL_159924#body_context_37 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[02/2023/TT-BVHTTDL]`<SO_HIEU>`** của **[Bộ Văn hóa , Thể thao và Du lịch]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Lao động - Thương binh và Xã hội]`<LINH_VUC>`** . **[Điều 5]`<DIEU>`** . **[Khoản 1]`<KHOAN>`** . **[c ) Tham gia tổ chức , dàn dựng chương trình , tiết mục văn nghệ , tuyên truyền lưu động ; trực tiếp biểu diễn các tiết mục văn nghệ phục vụ nhiệm vụ chính trị ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **02/2023/TT-BVHTTDL** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Văn hóa , Thể thao và Du lịch** → `CO_QUAN_BAN_HANH` (span: `[4:10]`)
- `[e3]` **Lao động - Thương binh và Xã hội** → `LINH_VUC` (span: `[12:17]`)
- `[e4]` **Điều 5** → `DIEU` (span: `[18:20]`)
- `[e5]` **Khoản 1** → `KHOAN` (span: `[21:23]`)
- `[e6]` **c ) Tham gia tổ chức , dàn dựng chương trình , tiết mục văn nghệ , tuyên truyền lưu động ; trực tiếp biểu diễn các tiết mục văn nghệ phục vụ nhiệm vụ chính trị ;** → `DIEM` (span: `[24:47]`)

**Quan hệ:**
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Văn hóa , Thể thao và Du lịch `[CO_QUAN_BAN_HANH]`)
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Lao động - Thương binh và Xã hội `[LINH_VUC]`)
- (`e4` Điều 5 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`)
- (`e5` Khoản 1 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 5 `[DIEU]`)
- (`e6` c ) Tham gia tổ chức , dàn dựng chương trình , tiết mục văn nghệ , tuyên truyền lưu động ; trực tiếp biểu diễn các tiết mục văn nghệ phục vụ nhiệm vụ chính trị ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e5` Khoản 1 `[KHOAN]`)
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Lao động - Thương binh và Xã hội `[LINH_VUC]`)
- (`e6` c ) Tham gia tổ chức , dàn dựng chương trình , tiết mục văn nghệ , tuyên truyền lưu động ; trực tiếp biểu diễn các tiết mục văn nghệ phục vụ nhiệm vụ chính trị ; `[DIEM]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Lao động - Thương binh và Xã hội `[LINH_VUC]`)


---

### Mẫu #02_2023_TT-BVHTTDL_159924#body_context_38 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[02/2023/TT-BVHTTDL]`<SO_HIEU>`** của **[Bộ Văn hóa , Thể thao và Du lịch]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Lao động - Thương binh và Xã hội]`<LINH_VUC>`** . **[Điều 5]`<DIEU>`** . **[Khoản 2]`<KHOAN>`** . **[a ) Có **[bằng tốt nghiệp đại học]`<GIAY_TO_HO_SO>`** trở lên phù hợp với chuyên ngành tuyên truyền viên văn hóa ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **02/2023/TT-BVHTTDL** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Văn hóa , Thể thao và Du lịch** → `CO_QUAN_BAN_HANH` (span: `[4:10]`)
- `[e3]` **Lao động - Thương binh và Xã hội** → `LINH_VUC` (span: `[12:17]`)
- `[e4]` **Điều 5** → `DIEU` (span: `[18:20]`)
- `[e5]` **Khoản 2** → `KHOAN` (span: `[21:23]`)
- `[e6]` **a ) Có bằng tốt nghiệp đại học trở lên phù hợp với chuyên ngành tuyên truyền viên văn hóa ;** → `DIEM` (span: `[24:38]`)
- `[e7]` **bằng tốt nghiệp đại học** → `GIAY_TO_HO_SO` (span: `[27:30]`) *(lồng trong `e6` (`DIEM`))*

**Quan hệ:**
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Văn hóa , Thể thao và Du lịch `[CO_QUAN_BAN_HANH]`)
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Lao động - Thương binh và Xã hội `[LINH_VUC]`)
- (`e4` Điều 5 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`)
- (`e5` Khoản 2 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 5 `[DIEU]`)
- (`e6` a ) Có bằng tốt nghiệp đại học trở lên phù hợp với chuyên ngành tuyên truyền viên văn hóa ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e5` Khoản 2 `[KHOAN]`)
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Lao động - Thương binh và Xã hội `[LINH_VUC]`)
- (`e6` a ) Có bằng tốt nghiệp đại học trở lên phù hợp với chuyên ngành tuyên truyền viên văn hóa ; `[DIEM]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Lao động - Thương binh và Xã hội `[LINH_VUC]`)


---

### Mẫu #02_2023_TT-BVHTTDL_159924#body_context_39 (Loại: `body_context`)
> **[Bộ Văn hóa , Thể thao và Du lịch]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[02/2023/TT-BVHTTDL]`<SO_HIEU>`** . **[Điều 5]`<DIEU>`** . **[Khoản 2]`<KHOAN>`** . **[b ) Có **[chứng chỉ bồi dưỡng]`<GIAY_TO_HO_SO>`** tiêu chuẩn chức danh nghề nghiệp tuyên truyền viên văn hóa .]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[7:8]`)
- `[e1]` **02/2023/TT-BVHTTDL** → `SO_HIEU` (span: `[9:10]`)
- `[e2]` **Bộ Văn hóa , Thể thao và Du lịch** → `CO_QUAN_BAN_HANH` (span: `[0:6]`)
- `[e3]` **Điều 5** → `DIEU` (span: `[11:13]`)
- `[e4]` **Khoản 2** → `KHOAN` (span: `[14:16]`)
- `[e5]` **b ) Có chứng chỉ bồi dưỡng tiêu chuẩn chức danh nghề nghiệp tuyên truyền viên văn hóa .** → `DIEM` (span: `[17:28]`)
- `[e6]` **chứng chỉ bồi dưỡng** → `GIAY_TO_HO_SO` (span: `[20:22]`) *(lồng trong `e5` (`DIEM`))*

**Quan hệ:**
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Văn hóa , Thể thao và Du lịch `[CO_QUAN_BAN_HANH]`)
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 5 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`)
- (`e4` Khoản 2 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 5 `[DIEU]`)
- (`e5` b ) Có chứng chỉ bồi dưỡng tiêu chuẩn chức danh nghề nghiệp tuyên truyền viên văn hóa . `[DIEM]`) ==[ **THUOC_VE** ]==> (`e4` Khoản 2 `[KHOAN]`)


---

### Mẫu #02_2023_TT-BVHTTDL_159924#body_context_40 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[02/2023/TT-BVHTTDL]`<SO_HIEU>`** ban hành **[ngày 21 tháng 02 năm 2023]`<NGAY_BAN_HANH>`** bởi **[Bộ Văn hóa , Thể thao và Du lịch]`<CO_QUAN_BAN_HANH>`** . **[Điều 5]`<DIEU>`** . **[Khoản 3]`<KHOAN>`** . **[a ) Nắm vững chủ trương , đường lối của Đảng , chính sách , pháp luật của Nhà nước về hoạt động tuyên truyền ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **02/2023/TT-BVHTTDL** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Văn hóa , Thể thao và Du lịch** → `CO_QUAN_BAN_HANH` (span: `[11:17]`)
- `[e3]` **ngày 21 tháng 02 năm 2023** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 5** → `DIEU` (span: `[18:20]`)
- `[e5]` **Khoản 3** → `KHOAN` (span: `[21:23]`)
- `[e6]` **a ) Nắm vững chủ trương , đường lối của Đảng , chính sách , pháp luật của Nhà nước về hoạt động tuyên truyền ;** → `DIEM` (span: `[24:43]`)

**Quan hệ:**
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Văn hóa , Thể thao và Du lịch `[CO_QUAN_BAN_HANH]`)
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 21 tháng 02 năm 2023 `[NGAY_BAN_HANH]`)
- (`e4` Điều 5 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`)
- (`e5` Khoản 3 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 5 `[DIEU]`)
- (`e6` a ) Nắm vững chủ trương , đường lối của Đảng , chính sách , pháp luật của Nhà nước về hoạt động tuyên truyền ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e5` Khoản 3 `[KHOAN]`)


---

### Mẫu #02_2023_TT-BVHTTDL_159924#body_context_41 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[02/2023/TT-BVHTTDL]`<SO_HIEU>`** ban hành **[ngày 21 tháng 02 năm 2023]`<NGAY_BAN_HANH>`** bởi **[Bộ Văn hóa , Thể thao và Du lịch]`<CO_QUAN_BAN_HANH>`** . **[Điều 5]`<DIEU>`** . **[Khoản 3]`<KHOAN>`** . **[d ) Có kiến thức về **[lĩnh vực văn hóa]`<LINH_VUC>`** , nghệ thuật ; có một trong các kỹ năng : Thuyết minh , thuyết trình , biểu diễn nhạc cụ , biểu diễn văn nghệ , hội họa , thiết kế , thi công cổ động trực quan hoặc các kỹ năng nghiệp vụ khác phù hợp với hình thức tuyên truyền ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **02/2023/TT-BVHTTDL** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Văn hóa , Thể thao và Du lịch** → `CO_QUAN_BAN_HANH` (span: `[11:17]`)
- `[e3]` **ngày 21 tháng 02 năm 2023** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 5** → `DIEU` (span: `[18:20]`)
- `[e5]` **Khoản 3** → `KHOAN` (span: `[21:23]`)
- `[e6]` **d ) Có kiến thức về lĩnh vực văn hóa , nghệ thuật ; có một trong các kỹ năng : Thuyết minh , thuyết trình , biểu diễn nhạc cụ , biểu diễn văn nghệ , hội họa , thiết kế , thi công cổ động trực quan hoặc các kỹ năng nghiệp vụ khác phù hợp với hình thức tuyên truyền ;** → `DIEM` (span: `[24:66]`)
- `[e7]` **lĩnh vực văn hóa** → `LINH_VUC` (span: `[29:31]`) *(lồng trong `e6` (`DIEM`))*

**Quan hệ:**
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Văn hóa , Thể thao và Du lịch `[CO_QUAN_BAN_HANH]`)
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 21 tháng 02 năm 2023 `[NGAY_BAN_HANH]`)
- (`e4` Điều 5 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`)
- (`e5` Khoản 3 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 5 `[DIEU]`)
- (`e6` d ) Có kiến thức về lĩnh vực văn hóa , nghệ thuật ; có một trong các kỹ năng : Thuyết minh , thuyết trình , biểu diễn nhạc cụ , biểu diễn văn nghệ , hội họa , thiết kế , thi công cổ động trực quan hoặc các kỹ năng nghiệp vụ khác phù hợp với hình thức tuyên truyền ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e5` Khoản 3 `[KHOAN]`)
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e7` lĩnh vực văn hóa `[LINH_VUC]`)
- (`e6` d ) Có kiến thức về lĩnh vực văn hóa , nghệ thuật ; có một trong các kỹ năng : Thuyết minh , thuyết trình , biểu diễn nhạc cụ , biểu diễn văn nghệ , hội họa , thiết kế , thi công cổ động trực quan hoặc các kỹ năng nghiệp vụ khác phù hợp với hình thức tuyên truyền ; `[DIEM]`) ==[ **THUOC_LINH_VUC** ]==> (`e7` lĩnh vực văn hóa `[LINH_VUC]`) *(Quan hệ lồng nhau)*


---

### Mẫu #02_2023_TT-BVHTTDL_159924#body_context_42 (Loại: `body_context`)
> **[Bộ Văn hóa , Thể thao và Du lịch]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[02/2023/TT-BVHTTDL]`<SO_HIEU>`** . **[Điều 5]`<DIEU>`** . **[Khoản 3]`<KHOAN>`** . **[đ ) Sử dụng thành thạo các **[phương tiện]`<TAI_SAN_VAT_CHAT>`** , thiết bị kỹ thuật phục vụ yêu cầu nhiệm vụ ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[7:8]`)
- `[e1]` **02/2023/TT-BVHTTDL** → `SO_HIEU` (span: `[9:10]`)
- `[e2]` **Bộ Văn hóa , Thể thao và Du lịch** → `CO_QUAN_BAN_HANH` (span: `[0:6]`)
- `[e3]` **Điều 5** → `DIEU` (span: `[11:13]`)
- `[e4]` **Khoản 3** → `KHOAN` (span: `[14:16]`)
- `[e5]` **đ ) Sử dụng thành thạo các phương tiện , thiết bị kỹ thuật phục vụ yêu cầu nhiệm vụ ;** → `DIEM` (span: `[17:30]`)
- `[e6]` **phương tiện** → `TAI_SAN_VAT_CHAT` (span: `[22:23]`) *(lồng trong `e5` (`DIEM`))*

**Quan hệ:**
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Văn hóa , Thể thao và Du lịch `[CO_QUAN_BAN_HANH]`)
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 5 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`)
- (`e4` Khoản 3 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 5 `[DIEU]`)
- (`e5` đ ) Sử dụng thành thạo các phương tiện , thiết bị kỹ thuật phục vụ yêu cầu nhiệm vụ ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e4` Khoản 3 `[KHOAN]`)


---

### Mẫu #02_2023_TT-BVHTTDL_159924#body_context_43 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[02/2023/TT-BVHTTDL]`<SO_HIEU>`** ban hành **[ngày 21 tháng 02 năm 2023]`<NGAY_BAN_HANH>`** bởi **[Bộ Văn hóa , Thể thao và Du lịch]`<CO_QUAN_BAN_HANH>`** . **[Điều 5]`<DIEU>`** . **[Khoản 3]`<KHOAN>`** . **[e ) Có kỹ năng sử dụng công nghệ thông tin cơ bản , sử dụng được ngoại ngữ hoặc sử dụng được tiếng dân tộc thiểu số đối với **[viên chức]`<CHU_THE_CA_NHAN>`** công tác ở vùng dân tộc thiểu số theo yêu cầu vị trí việc làm .]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **02/2023/TT-BVHTTDL** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Văn hóa , Thể thao và Du lịch** → `CO_QUAN_BAN_HANH` (span: `[11:17]`)
- `[e3]` **ngày 21 tháng 02 năm 2023** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 5** → `DIEU` (span: `[18:20]`)
- `[e5]` **Khoản 3** → `KHOAN` (span: `[21:23]`)
- `[e6]` **e ) Có kỹ năng sử dụng công nghệ thông tin cơ bản , sử dụng được ngoại ngữ hoặc sử dụng được tiếng dân tộc thiểu số đối với viên chức công tác ở vùng dân tộc thiểu số theo yêu cầu vị trí việc làm .** → `DIEM` (span: `[24:52]`)
- `[e7]` **viên chức** → `CHU_THE_CA_NHAN` (span: `[42:43]`) *(lồng trong `e6` (`DIEM`))*

**Quan hệ:**
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Văn hóa , Thể thao và Du lịch `[CO_QUAN_BAN_HANH]`)
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 21 tháng 02 năm 2023 `[NGAY_BAN_HANH]`)
- (`e4` Điều 5 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`)
- (`e5` Khoản 3 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 5 `[DIEU]`)
- (`e6` e ) Có kỹ năng sử dụng công nghệ thông tin cơ bản , sử dụng được ngoại ngữ hoặc sử dụng được tiếng dân tộc thiểu số đối với viên chức công tác ở vùng dân tộc thiểu số theo yêu cầu vị trí việc làm . `[DIEM]`) ==[ **THUOC_VE** ]==> (`e5` Khoản 3 `[KHOAN]`)


---

### Mẫu #02_2023_TT-BVHTTDL_159924#body_standalone_44 (Loại: `body_standalone`)
> **[Điều 5]`<DIEU>`** . **[Khoản 3]`<KHOAN>`** . **[e ) Có kỹ năng sử dụng công nghệ thông tin cơ bản , sử dụng được ngoại ngữ hoặc sử dụng được tiếng dân tộc thiểu số đối với **[viên chức]`<CHU_THE_CA_NHAN>`** công tác ở vùng dân tộc thiểu số theo yêu cầu vị trí việc làm .]`<DIEM>`**

**Thực thể:**
- `[e0]` **Điều 5** → `DIEU` (span: `[0:2]`)
- `[e1]` **Khoản 3** → `KHOAN` (span: `[3:5]`)
- `[e2]` **e ) Có kỹ năng sử dụng công nghệ thông tin cơ bản , sử dụng được ngoại ngữ hoặc sử dụng được tiếng dân tộc thiểu số đối với viên chức công tác ở vùng dân tộc thiểu số theo yêu cầu vị trí việc làm .** → `DIEM` (span: `[6:34]`)
- `[e3]` **viên chức** → `CHU_THE_CA_NHAN` (span: `[24:25]`) *(lồng trong `e2` (`DIEM`))*

**Quan hệ:**
- (`e1` Khoản 3 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 5 `[DIEU]`)
- (`e2` e ) Có kỹ năng sử dụng công nghệ thông tin cơ bản , sử dụng được ngoại ngữ hoặc sử dụng được tiếng dân tộc thiểu số đối với viên chức công tác ở vùng dân tộc thiểu số theo yêu cầu vị trí việc làm . `[DIEM]`) ==[ **THUOC_VE** ]==> (`e1` Khoản 3 `[KHOAN]`)


---

### Mẫu #02_2023_TT-BVHTTDL_159924#body_context_45 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[02/2023/TT-BVHTTDL]`<SO_HIEU>`** của **[Bộ Văn hóa , Thể thao và Du lịch]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Lao động - Thương binh và Xã hội]`<LINH_VUC>`** . **[Điều 5]`<DIEU>`** . **[4 . Yêu cầu đối với **[viên chức]`<CHU_THE_CA_NHAN>`** dự thi hoặc xét thăng hạng chức danh nghề nghiệp tuyên truyền viên văn hóa : Có thời gian công tác giữ chức danh nghề nghiệp tuyên truyền viên văn hoá trung cấp hoặc tương đương từ **[đủ 03 năm]`<THOI_HAN>`** trở lên ( không kể thời gian tập sự , thử việc ) . Trường hợp có thời gian tương đương thì phải có ít nhất 01 năm ( **[đủ 12 tháng]`<THOI_HAN>`** ) đang giữ chức danh tuyên truyền viên văn hoá trung cấp tính đến ngày hết hạn nộp hồ sơ]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **02/2023/TT-BVHTTDL** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Văn hóa , Thể thao và Du lịch** → `CO_QUAN_BAN_HANH` (span: `[4:10]`)
- `[e3]` **Lao động - Thương binh và Xã hội** → `LINH_VUC` (span: `[12:17]`)
- `[e4]` **Điều 5** → `DIEU` (span: `[18:20]`)
- `[e5]` **4 . Yêu cầu đối với viên chức dự thi hoặc xét thăng hạng chức danh nghề nghiệp tuyên truyền viên văn hóa : Có thời gian công tác giữ chức danh nghề nghiệp tuyên truyền viên văn hoá trung cấp hoặc tương đương từ đủ 03 năm trở lên ( không kể thời gian tập sự , thử việc ) . Trường hợp có thời gian tương đương thì phải có ít nhất 01 năm ( đủ 12 tháng ) đang giữ chức danh tuyên truyền viên văn hoá trung cấp tính đến ngày hết hạn nộp hồ sơ** → `KHOAN` (span: `[21:90]`)
- `[e6]` **đủ 03 năm** → `THOI_HAN` (span: `[48:51]`) *(lồng trong `e5` (`KHOAN`))*
- `[e7]` **đủ 12 tháng** → `THOI_HAN` (span: `[74:77]`) *(lồng trong `e5` (`KHOAN`))*
- `[e8]` **viên chức** → `CHU_THE_CA_NHAN` (span: `[25:26]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Văn hóa , Thể thao và Du lịch `[CO_QUAN_BAN_HANH]`)
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Lao động - Thương binh và Xã hội `[LINH_VUC]`)
- (`e4` Điều 5 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`)
- (`e5` 4 . Yêu cầu đối với viên chức dự thi hoặc xét thăng hạng chức danh nghề nghiệp tuyên truyền viên văn hóa : Có thời gian công tác giữ chức danh nghề nghiệp tuyên truyền viên văn hoá trung cấp hoặc tương đương từ đủ 03 năm trở lên ( không kể thời gian tập sự , thử việc ) . Trường hợp có thời gian tương đương thì phải có ít nhất 01 năm ( đủ 12 tháng ) đang giữ chức danh tuyên truyền viên văn hoá trung cấp tính đến ngày hết hạn nộp hồ sơ `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 5 `[DIEU]`)
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Lao động - Thương binh và Xã hội `[LINH_VUC]`)
- (`e5` 4 . Yêu cầu đối với viên chức dự thi hoặc xét thăng hạng chức danh nghề nghiệp tuyên truyền viên văn hóa : Có thời gian công tác giữ chức danh nghề nghiệp tuyên truyền viên văn hoá trung cấp hoặc tương đương từ đủ 03 năm trở lên ( không kể thời gian tập sự , thử việc ) . Trường hợp có thời gian tương đương thì phải có ít nhất 01 năm ( đủ 12 tháng ) đang giữ chức danh tuyên truyền viên văn hoá trung cấp tính đến ngày hết hạn nộp hồ sơ `[KHOAN]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Lao động - Thương binh và Xã hội `[LINH_VUC]`)


---

### Mẫu #02_2023_TT-BVHTTDL_159924#body_standalone_46 (Loại: `body_standalone`)
> **[Điều 5]`<DIEU>`** . **[4 . Yêu cầu đối với **[viên chức]`<CHU_THE_CA_NHAN>`** dự thi hoặc xét thăng hạng chức danh nghề nghiệp tuyên truyền viên văn hóa : Có thời gian công tác giữ chức danh nghề nghiệp tuyên truyền viên văn hoá trung cấp hoặc tương đương từ **[đủ 03 năm]`<THOI_HAN>`** trở lên ( không kể thời gian tập sự , thử việc ) . Trường hợp có thời gian tương đương thì phải có ít nhất 01 năm ( **[đủ 12 tháng]`<THOI_HAN>`** ) đang giữ chức danh tuyên truyền viên văn hoá trung cấp tính đến ngày hết hạn nộp hồ sơ]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 5** → `DIEU` (span: `[0:2]`)
- `[e1]` **4 . Yêu cầu đối với viên chức dự thi hoặc xét thăng hạng chức danh nghề nghiệp tuyên truyền viên văn hóa : Có thời gian công tác giữ chức danh nghề nghiệp tuyên truyền viên văn hoá trung cấp hoặc tương đương từ đủ 03 năm trở lên ( không kể thời gian tập sự , thử việc ) . Trường hợp có thời gian tương đương thì phải có ít nhất 01 năm ( đủ 12 tháng ) đang giữ chức danh tuyên truyền viên văn hoá trung cấp tính đến ngày hết hạn nộp hồ sơ** → `KHOAN` (span: `[3:72]`)
- `[e2]` **đủ 03 năm** → `THOI_HAN` (span: `[30:33]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **đủ 12 tháng** → `THOI_HAN` (span: `[56:59]`) *(lồng trong `e1` (`KHOAN`))*
- `[e4]` **viên chức** → `CHU_THE_CA_NHAN` (span: `[7:8]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 4 . Yêu cầu đối với viên chức dự thi hoặc xét thăng hạng chức danh nghề nghiệp tuyên truyền viên văn hóa : Có thời gian công tác giữ chức danh nghề nghiệp tuyên truyền viên văn hoá trung cấp hoặc tương đương từ đủ 03 năm trở lên ( không kể thời gian tập sự , thử việc ) . Trường hợp có thời gian tương đương thì phải có ít nhất 01 năm ( đủ 12 tháng ) đang giữ chức danh tuyên truyền viên văn hoá trung cấp tính đến ngày hết hạn nộp hồ sơ `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 5 `[DIEU]`)


---

### Mẫu #02_2023_TT-BVHTTDL_159924#body_context_47 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[02/2023/TT-BVHTTDL]`<SO_HIEU>`** ban hành **[ngày 21 tháng 02 năm 2023]`<NGAY_BAN_HANH>`** bởi **[Bộ Văn hóa , Thể thao và Du lịch]`<CO_QUAN_BAN_HANH>`** . **[Điều 6]`<DIEU>`** . **[1 . Nhiệm vụ :]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **02/2023/TT-BVHTTDL** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Văn hóa , Thể thao và Du lịch** → `CO_QUAN_BAN_HANH` (span: `[11:17]`)
- `[e3]` **ngày 21 tháng 02 năm 2023** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 6** → `DIEU` (span: `[18:20]`)
- `[e5]` **1 . Nhiệm vụ :** → `KHOAN` (span: `[21:25]`)

**Quan hệ:**
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Văn hóa , Thể thao và Du lịch `[CO_QUAN_BAN_HANH]`)
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 21 tháng 02 năm 2023 `[NGAY_BAN_HANH]`)
- (`e4` Điều 6 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`)
- (`e5` 1 . Nhiệm vụ : `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 6 `[DIEU]`)


---

### Mẫu #02_2023_TT-BVHTTDL_159924#body_context_48 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[02/2023/TT-BVHTTDL]`<SO_HIEU>`** ban hành **[ngày 21 tháng 02 năm 2023]`<NGAY_BAN_HANH>`** bởi **[Bộ Văn hóa , Thể thao và Du lịch]`<CO_QUAN_BAN_HANH>`** . **[Điều 6]`<DIEU>`** . **[Khoản 2]`<KHOAN>`** . **[b ) Có **[chứng chỉ bồi dưỡng]`<GIAY_TO_HO_SO>`** tiêu chuẩn chức danh nghề nghiệp tuyên truyền viên văn hóa .]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **02/2023/TT-BVHTTDL** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Văn hóa , Thể thao và Du lịch** → `CO_QUAN_BAN_HANH` (span: `[11:17]`)
- `[e3]` **ngày 21 tháng 02 năm 2023** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 6** → `DIEU` (span: `[18:20]`)
- `[e5]` **Khoản 2** → `KHOAN` (span: `[21:23]`)
- `[e6]` **b ) Có chứng chỉ bồi dưỡng tiêu chuẩn chức danh nghề nghiệp tuyên truyền viên văn hóa .** → `DIEM` (span: `[24:35]`)
- `[e7]` **chứng chỉ bồi dưỡng** → `GIAY_TO_HO_SO` (span: `[27:29]`) *(lồng trong `e6` (`DIEM`))*

**Quan hệ:**
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Văn hóa , Thể thao và Du lịch `[CO_QUAN_BAN_HANH]`)
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 21 tháng 02 năm 2023 `[NGAY_BAN_HANH]`)
- (`e4` Điều 6 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`)
- (`e5` Khoản 2 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 6 `[DIEU]`)
- (`e6` b ) Có chứng chỉ bồi dưỡng tiêu chuẩn chức danh nghề nghiệp tuyên truyền viên văn hóa . `[DIEM]`) ==[ **THUOC_VE** ]==> (`e5` Khoản 2 `[KHOAN]`)


---

### Mẫu #02_2023_TT-BVHTTDL_159924#body_standalone_49 (Loại: `body_standalone`)
> **[Điều 6]`<DIEU>`** . **[Khoản 2]`<KHOAN>`** . **[b ) Có **[chứng chỉ bồi dưỡng]`<GIAY_TO_HO_SO>`** tiêu chuẩn chức danh nghề nghiệp tuyên truyền viên văn hóa .]`<DIEM>`**

**Thực thể:**
- `[e0]` **Điều 6** → `DIEU` (span: `[0:2]`)
- `[e1]` **Khoản 2** → `KHOAN` (span: `[3:5]`)
- `[e2]` **b ) Có chứng chỉ bồi dưỡng tiêu chuẩn chức danh nghề nghiệp tuyên truyền viên văn hóa .** → `DIEM` (span: `[6:17]`)
- `[e3]` **chứng chỉ bồi dưỡng** → `GIAY_TO_HO_SO` (span: `[9:11]`) *(lồng trong `e2` (`DIEM`))*

**Quan hệ:**
- (`e1` Khoản 2 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 6 `[DIEU]`)
- (`e2` b ) Có chứng chỉ bồi dưỡng tiêu chuẩn chức danh nghề nghiệp tuyên truyền viên văn hóa . `[DIEM]`) ==[ **THUOC_VE** ]==> (`e1` Khoản 2 `[KHOAN]`)


---

### Mẫu #02_2023_TT-BVHTTDL_159924#body_context_50 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[02/2023/TT-BVHTTDL]`<SO_HIEU>`** của **[Bộ Văn hóa , Thể thao và Du lịch]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Lao động - Thương binh và Xã hội]`<LINH_VUC>`** . **[Điều 6]`<DIEU>`** . **[Khoản 3]`<KHOAN>`** . **[c ) Sử dụng được các **[phương tiện]`<TAI_SAN_VAT_CHAT>`** , thiết bị kỹ thuật phục vụ yêu cầu nhiệm vụ ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **02/2023/TT-BVHTTDL** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Văn hóa , Thể thao và Du lịch** → `CO_QUAN_BAN_HANH` (span: `[4:10]`)
- `[e3]` **Lao động - Thương binh và Xã hội** → `LINH_VUC` (span: `[12:17]`)
- `[e4]` **Điều 6** → `DIEU` (span: `[18:20]`)
- `[e5]` **Khoản 3** → `KHOAN` (span: `[21:23]`)
- `[e6]` **c ) Sử dụng được các phương tiện , thiết bị kỹ thuật phục vụ yêu cầu nhiệm vụ ;** → `DIEM` (span: `[24:37]`)
- `[e7]` **phương tiện** → `TAI_SAN_VAT_CHAT` (span: `[29:30]`) *(lồng trong `e6` (`DIEM`))*

**Quan hệ:**
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Văn hóa , Thể thao và Du lịch `[CO_QUAN_BAN_HANH]`)
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Lao động - Thương binh và Xã hội `[LINH_VUC]`)
- (`e4` Điều 6 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`)
- (`e5` Khoản 3 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 6 `[DIEU]`)
- (`e6` c ) Sử dụng được các phương tiện , thiết bị kỹ thuật phục vụ yêu cầu nhiệm vụ ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e5` Khoản 3 `[KHOAN]`)
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Lao động - Thương binh và Xã hội `[LINH_VUC]`)
- (`e6` c ) Sử dụng được các phương tiện , thiết bị kỹ thuật phục vụ yêu cầu nhiệm vụ ; `[DIEM]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Lao động - Thương binh và Xã hội `[LINH_VUC]`)


---

### Mẫu #02_2023_TT-BVHTTDL_159924#body_context_51 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[02/2023/TT-BVHTTDL]`<SO_HIEU>`** của **[Bộ Văn hóa , Thể thao và Du lịch]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Lao động - Thương binh và Xã hội]`<LINH_VUC>`** . **[Điều 7]`<DIEU>`** . **[1 . Việc bổ nhiệm và xếp lương vào chức danh nghề nghiệp **[viên chức]`<CHU_THE_CA_NHAN>`** chuyên ngành tuyên truyền viên văn hóa **[quy định tại]`<TU_KHOA_PHAP_LY>`** **[Thông tư này]`<THAM_CHIEU_PHAP_LY>`** phải căn cứ vào vị trí việc làm , chức trách , nhiệm vụ và chuyên môn , nghiệp vụ đang đảm nhận của **[viên chức]`<CHU_THE_CA_NHAN>`** .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **02/2023/TT-BVHTTDL** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Văn hóa , Thể thao và Du lịch** → `CO_QUAN_BAN_HANH` (span: `[4:10]`)
- `[e3]` **Lao động - Thương binh và Xã hội** → `LINH_VUC` (span: `[12:17]`)
- `[e4]` **Điều 7** → `DIEU` (span: `[18:20]`)
- `[e5]` **1 . Việc bổ nhiệm và xếp lương vào chức danh nghề nghiệp viên chức chuyên ngành tuyên truyền viên văn hóa quy định tại Thông tư này phải căn cứ vào vị trí việc làm , chức trách , nhiệm vụ và chuyên môn , nghiệp vụ đang đảm nhận của viên chức .** → `KHOAN` (span: `[21:57]`)
- `[e6]` **Thông tư này** → `THAM_CHIEU_PHAP_LY` (span: `[37:39]`) *(lồng trong `e5` (`KHOAN`))*
- `[e7]` **quy định tại** → `TU_KHOA_PHAP_LY` (span: `[35:37]`) *(lồng trong `e5` (`KHOAN`))*
- `[e8]` **viên chức** → `CHU_THE_CA_NHAN` (span: `[31:32]`) *(lồng trong `e5` (`KHOAN`))*
- `[e9]` **viên chức** → `CHU_THE_CA_NHAN` (span: `[55:56]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Văn hóa , Thể thao và Du lịch `[CO_QUAN_BAN_HANH]`)
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Lao động - Thương binh và Xã hội `[LINH_VUC]`)
- (`e4` Điều 7 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`)
- (`e5` 1 . Việc bổ nhiệm và xếp lương vào chức danh nghề nghiệp viên chức chuyên ngành tuyên truyền viên văn hóa quy định tại Thông tư này phải căn cứ vào vị trí việc làm , chức trách , nhiệm vụ và chuyên môn , nghiệp vụ đang đảm nhận của viên chức . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 7 `[DIEU]`)
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Lao động - Thương binh và Xã hội `[LINH_VUC]`)
- (`e5` 1 . Việc bổ nhiệm và xếp lương vào chức danh nghề nghiệp viên chức chuyên ngành tuyên truyền viên văn hóa quy định tại Thông tư này phải căn cứ vào vị trí việc làm , chức trách , nhiệm vụ và chuyên môn , nghiệp vụ đang đảm nhận của viên chức . `[KHOAN]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Lao động - Thương binh và Xã hội `[LINH_VUC]`)
- (`e7` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e6` Thông tư này `[THAM_CHIEU_PHAP_LY]`)
- (`e5` 1 . Việc bổ nhiệm và xếp lương vào chức danh nghề nghiệp viên chức chuyên ngành tuyên truyền viên văn hóa quy định tại Thông tư này phải căn cứ vào vị trí việc làm , chức trách , nhiệm vụ và chuyên môn , nghiệp vụ đang đảm nhận của viên chức . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e6` Thông tư này `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #02_2023_TT-BVHTTDL_159924#body_standalone_52 (Loại: `body_standalone`)
> **[Điều 7]`<DIEU>`** . **[1 . Việc bổ nhiệm và xếp lương vào chức danh nghề nghiệp **[viên chức]`<CHU_THE_CA_NHAN>`** chuyên ngành tuyên truyền viên văn hóa **[quy định tại]`<TU_KHOA_PHAP_LY>`** **[Thông tư này]`<THAM_CHIEU_PHAP_LY>`** phải căn cứ vào vị trí việc làm , chức trách , nhiệm vụ và chuyên môn , nghiệp vụ đang đảm nhận của **[viên chức]`<CHU_THE_CA_NHAN>`** .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 7** → `DIEU` (span: `[0:2]`)
- `[e1]` **1 . Việc bổ nhiệm và xếp lương vào chức danh nghề nghiệp viên chức chuyên ngành tuyên truyền viên văn hóa quy định tại Thông tư này phải căn cứ vào vị trí việc làm , chức trách , nhiệm vụ và chuyên môn , nghiệp vụ đang đảm nhận của viên chức .** → `KHOAN` (span: `[3:39]`)
- `[e2]` **Thông tư này** → `THAM_CHIEU_PHAP_LY` (span: `[19:21]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **quy định tại** → `TU_KHOA_PHAP_LY` (span: `[17:19]`) *(lồng trong `e1` (`KHOAN`))*
- `[e4]` **viên chức** → `CHU_THE_CA_NHAN` (span: `[13:14]`) *(lồng trong `e1` (`KHOAN`))*
- `[e5]` **viên chức** → `CHU_THE_CA_NHAN` (span: `[37:38]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 1 . Việc bổ nhiệm và xếp lương vào chức danh nghề nghiệp viên chức chuyên ngành tuyên truyền viên văn hóa quy định tại Thông tư này phải căn cứ vào vị trí việc làm , chức trách , nhiệm vụ và chuyên môn , nghiệp vụ đang đảm nhận của viên chức . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 7 `[DIEU]`)
- (`e3` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e2` Thông tư này `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 1 . Việc bổ nhiệm và xếp lương vào chức danh nghề nghiệp viên chức chuyên ngành tuyên truyền viên văn hóa quy định tại Thông tư này phải căn cứ vào vị trí việc làm , chức trách , nhiệm vụ và chuyên môn , nghiệp vụ đang đảm nhận của viên chức . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e2` Thông tư này `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #02_2023_TT-BVHTTDL_159924#body_context_53 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[02/2023/TT-BVHTTDL]`<SO_HIEU>`** của **[Bộ Văn hóa , Thể thao và Du lịch]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Lao động - Thương binh và Xã hội]`<LINH_VUC>`** . **[Điều 7]`<DIEU>`** . **[2 . Khi bổ nhiệm và xếp lương vào các chức danh nghề nghiệp **[viên chức]`<CHU_THE_CA_NHAN>`** chuyên ngành tuyên truyền viên văn hóa tương ứng không được kết hợp nâng bậc lương hoặc thăng hạng chức danh nghề nghiệp **[viên chức]`<CHU_THE_CA_NHAN>`** .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **02/2023/TT-BVHTTDL** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Văn hóa , Thể thao và Du lịch** → `CO_QUAN_BAN_HANH` (span: `[4:10]`)
- `[e3]` **Lao động - Thương binh và Xã hội** → `LINH_VUC` (span: `[12:17]`)
- `[e4]` **Điều 7** → `DIEU` (span: `[18:20]`)
- `[e5]` **2 . Khi bổ nhiệm và xếp lương vào các chức danh nghề nghiệp viên chức chuyên ngành tuyên truyền viên văn hóa tương ứng không được kết hợp nâng bậc lương hoặc thăng hạng chức danh nghề nghiệp viên chức .** → `KHOAN` (span: `[21:49]`)
- `[e6]` **viên chức** → `CHU_THE_CA_NHAN` (span: `[32:33]`) *(lồng trong `e5` (`KHOAN`))*
- `[e7]` **viên chức** → `CHU_THE_CA_NHAN` (span: `[47:48]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Văn hóa , Thể thao và Du lịch `[CO_QUAN_BAN_HANH]`)
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Lao động - Thương binh và Xã hội `[LINH_VUC]`)
- (`e4` Điều 7 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`)
- (`e5` 2 . Khi bổ nhiệm và xếp lương vào các chức danh nghề nghiệp viên chức chuyên ngành tuyên truyền viên văn hóa tương ứng không được kết hợp nâng bậc lương hoặc thăng hạng chức danh nghề nghiệp viên chức . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 7 `[DIEU]`)
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Lao động - Thương binh và Xã hội `[LINH_VUC]`)
- (`e5` 2 . Khi bổ nhiệm và xếp lương vào các chức danh nghề nghiệp viên chức chuyên ngành tuyên truyền viên văn hóa tương ứng không được kết hợp nâng bậc lương hoặc thăng hạng chức danh nghề nghiệp viên chức . `[KHOAN]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Lao động - Thương binh và Xã hội `[LINH_VUC]`)


---

### Mẫu #02_2023_TT-BVHTTDL_159924#body_standalone_54 (Loại: `body_standalone`)
> **[Điều 7]`<DIEU>`** . **[2 . Khi bổ nhiệm và xếp lương vào các chức danh nghề nghiệp **[viên chức]`<CHU_THE_CA_NHAN>`** chuyên ngành tuyên truyền viên văn hóa tương ứng không được kết hợp nâng bậc lương hoặc thăng hạng chức danh nghề nghiệp **[viên chức]`<CHU_THE_CA_NHAN>`** .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 7** → `DIEU` (span: `[0:2]`)
- `[e1]` **2 . Khi bổ nhiệm và xếp lương vào các chức danh nghề nghiệp viên chức chuyên ngành tuyên truyền viên văn hóa tương ứng không được kết hợp nâng bậc lương hoặc thăng hạng chức danh nghề nghiệp viên chức .** → `KHOAN` (span: `[3:31]`)
- `[e2]` **viên chức** → `CHU_THE_CA_NHAN` (span: `[14:15]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **viên chức** → `CHU_THE_CA_NHAN` (span: `[29:30]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 2 . Khi bổ nhiệm và xếp lương vào các chức danh nghề nghiệp viên chức chuyên ngành tuyên truyền viên văn hóa tương ứng không được kết hợp nâng bậc lương hoặc thăng hạng chức danh nghề nghiệp viên chức . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 7 `[DIEU]`)


---

### Mẫu #02_2023_TT-BVHTTDL_159924#body_context_55 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[02/2023/TT-BVHTTDL]`<SO_HIEU>`** ban hành **[ngày 21 tháng 02 năm 2023]`<NGAY_BAN_HANH>`** bởi **[Bộ Văn hóa , Thể thao và Du lịch]`<CO_QUAN_BAN_HANH>`** . **[Chương III]`<CHUONG>`** . **[Điều 8 . Cách xếp lương]`<DIEU>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **02/2023/TT-BVHTTDL** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Văn hóa , Thể thao và Du lịch** → `CO_QUAN_BAN_HANH` (span: `[11:17]`)
- `[e3]` **ngày 21 tháng 02 năm 2023** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Chương III** → `CHUONG` (span: `[18:20]`)
- `[e5]` **Điều 8 . Cách xếp lương** → `DIEU` (span: `[21:27]`)

**Quan hệ:**
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Văn hóa , Thể thao và Du lịch `[CO_QUAN_BAN_HANH]`)
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 21 tháng 02 năm 2023 `[NGAY_BAN_HANH]`)
- (`e4` Chương III `[CHUONG]`) ==[ **THUOC_VE** ]==> (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`)
- (`e5` Điều 8 . Cách xếp lương `[DIEU]`) ==[ **THUOC_VE** ]==> (`e4` Chương III `[CHUONG]`)


---

### Mẫu #02_2023_TT-BVHTTDL_159924#body_context_56 (Loại: `body_context`)
> **[Bộ Văn hóa , Thể thao và Du lịch]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[02/2023/TT-BVHTTDL]`<SO_HIEU>`** . **[Điều 8]`<DIEU>`** . **[1 . Các chức danh nghề nghiệp **[viên chức]`<CHU_THE_CA_NHAN>`** chuyên ngành tuyên truyền viên văn hóa **[quy định tại]`<TU_KHOA_PHAP_LY>`** **[Thông tư này]`<THAM_CHIEU_PHAP_LY>`** được áp dụng Bảng 3 ( Bảng lương chuyên môn , nghiệp vụ đối với **[cán bộ]`<CHU_THE_CA_NHAN>`** , **[viên chức]`<CHU_THE_CA_NHAN>`** trong các **[đơn vị sự nghiệp]`<TO_CHUC_DOANH_NGHIEP>`** của Nhà nước ) ban hành kèm theo **[Nghị định số 204/2004/NĐ-CP]`<THAM_CHIEU_PHAP_LY>`** **[ngày 14 tháng 12 năm 2004]`<NGAY_THAM_CHIEU>`** của **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** về chế độ **[tiền lương]`<TAI_SAN_VAT_CHAT>`** đối với **[cán bộ , công chức , viên chức]`<CHU_THE_CA_NHAN>`** và lực lượng vũ trang ( sau đây viết tắt là **[Nghị định số 204/2004/NĐ-CP]`<THAM_CHIEU_PHAP_LY>`** ) , cụ]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[7:8]`)
- `[e1]` **02/2023/TT-BVHTTDL** → `SO_HIEU` (span: `[9:10]`)
- `[e2]` **Bộ Văn hóa , Thể thao và Du lịch** → `CO_QUAN_BAN_HANH` (span: `[0:6]`)
- `[e3]` **Điều 8** → `DIEU` (span: `[11:13]`)
- `[e4]` **1 . Các chức danh nghề nghiệp viên chức chuyên ngành tuyên truyền viên văn hóa quy định tại Thông tư này được áp dụng Bảng 3 ( Bảng lương chuyên môn , nghiệp vụ đối với cán bộ , viên chức trong các đơn vị sự nghiệp của Nhà nước ) ban hành kèm theo Nghị định số 204/2004/NĐ-CP ngày 14 tháng 12 năm 2004 của Chính phủ về chế độ tiền lương đối với cán bộ , công chức , viên chức và lực lượng vũ trang ( sau đây viết tắt là Nghị định số 204/2004/NĐ-CP ) , cụ** → `KHOAN` (span: `[14:86]`)
- `[e5]` **Thông tư này** → `THAM_CHIEU_PHAP_LY` (span: `[25:27]`) *(lồng trong `e4` (`KHOAN`))*
- `[e6]` **Nghị định số 204/2004/NĐ-CP** → `THAM_CHIEU_PHAP_LY` (span: `[51:54]`) *(lồng trong `e4` (`KHOAN`))*
- `[e7]` **Nghị định số 204/2004/NĐ-CP** → `THAM_CHIEU_PHAP_LY` (span: `[80:83]`) *(lồng trong `e4` (`KHOAN`))*
- `[e8]` **quy định tại** → `TU_KHOA_PHAP_LY` (span: `[23:25]`) *(lồng trong `e4` (`KHOAN`))*
- `[e9]` **ngày 14 tháng 12 năm 2004** → `NGAY_THAM_CHIEU` (span: `[54:60]`) *(lồng trong `e4` (`KHOAN`))*
- `[e10]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[61:62]`) *(lồng trong `e4` (`KHOAN`))*
- `[e11]` **đơn vị sự nghiệp** → `TO_CHUC_DOANH_NGHIEP` (span: `[43:45]`) *(lồng trong `e4` (`KHOAN`))*
- `[e12]` **viên chức** → `CHU_THE_CA_NHAN` (span: `[19:20]`) *(lồng trong `e4` (`KHOAN`))*
- `[e13]` **cán bộ** → `CHU_THE_CA_NHAN` (span: `[38:39]`) *(lồng trong `e4` (`KHOAN`))*
- `[e14]` **viên chức** → `CHU_THE_CA_NHAN` (span: `[40:41]`) *(lồng trong `e4` (`KHOAN`))*
- `[e15]` **cán bộ , công chức , viên chức** → `CHU_THE_CA_NHAN` (span: `[66:71]`) *(lồng trong `e4` (`KHOAN`))*
- `[e16]` **tiền lương** → `TAI_SAN_VAT_CHAT` (span: `[64:65]`) *(lồng trong `e4` (`KHOAN`))*

**Quan hệ:**
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Văn hóa , Thể thao và Du lịch `[CO_QUAN_BAN_HANH]`)
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 8 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`)
- (`e4` 1 . Các chức danh nghề nghiệp viên chức chuyên ngành tuyên truyền viên văn hóa quy định tại Thông tư này được áp dụng Bảng 3 ( Bảng lương chuyên môn , nghiệp vụ đối với cán bộ , viên chức trong các đơn vị sự nghiệp của Nhà nước ) ban hành kèm theo Nghị định số 204/2004/NĐ-CP ngày 14 tháng 12 năm 2004 của Chính phủ về chế độ tiền lương đối với cán bộ , công chức , viên chức và lực lượng vũ trang ( sau đây viết tắt là Nghị định số 204/2004/NĐ-CP ) , cụ `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 8 `[DIEU]`)
- (`e8` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e5` Thông tư này `[THAM_CHIEU_PHAP_LY]`)
- (`e4` 1 . Các chức danh nghề nghiệp viên chức chuyên ngành tuyên truyền viên văn hóa quy định tại Thông tư này được áp dụng Bảng 3 ( Bảng lương chuyên môn , nghiệp vụ đối với cán bộ , viên chức trong các đơn vị sự nghiệp của Nhà nước ) ban hành kèm theo Nghị định số 204/2004/NĐ-CP ngày 14 tháng 12 năm 2004 của Chính phủ về chế độ tiền lương đối với cán bộ , công chức , viên chức và lực lượng vũ trang ( sau đây viết tắt là Nghị định số 204/2004/NĐ-CP ) , cụ `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e5` Thông tư này `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e8` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e6` Nghị định số 204/2004/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e4` 1 . Các chức danh nghề nghiệp viên chức chuyên ngành tuyên truyền viên văn hóa quy định tại Thông tư này được áp dụng Bảng 3 ( Bảng lương chuyên môn , nghiệp vụ đối với cán bộ , viên chức trong các đơn vị sự nghiệp của Nhà nước ) ban hành kèm theo Nghị định số 204/2004/NĐ-CP ngày 14 tháng 12 năm 2004 của Chính phủ về chế độ tiền lương đối với cán bộ , công chức , viên chức và lực lượng vũ trang ( sau đây viết tắt là Nghị định số 204/2004/NĐ-CP ) , cụ `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e6` Nghị định số 204/2004/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e8` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e7` Nghị định số 204/2004/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e4` 1 . Các chức danh nghề nghiệp viên chức chuyên ngành tuyên truyền viên văn hóa quy định tại Thông tư này được áp dụng Bảng 3 ( Bảng lương chuyên môn , nghiệp vụ đối với cán bộ , viên chức trong các đơn vị sự nghiệp của Nhà nước ) ban hành kèm theo Nghị định số 204/2004/NĐ-CP ngày 14 tháng 12 năm 2004 của Chính phủ về chế độ tiền lương đối với cán bộ , công chức , viên chức và lực lượng vũ trang ( sau đây viết tắt là Nghị định số 204/2004/NĐ-CP ) , cụ `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e7` Nghị định số 204/2004/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e6` Nghị định số 204/2004/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e9` ngày 14 tháng 12 năm 2004 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #02_2023_TT-BVHTTDL_159924#body_standalone_57 (Loại: `body_standalone`)
> **[Điều 8]`<DIEU>`** . **[1 . Các chức danh nghề nghiệp **[viên chức]`<CHU_THE_CA_NHAN>`** chuyên ngành tuyên truyền viên văn hóa **[quy định tại]`<TU_KHOA_PHAP_LY>`** **[Thông tư này]`<THAM_CHIEU_PHAP_LY>`** được áp dụng Bảng 3 ( Bảng lương chuyên môn , nghiệp vụ đối với **[cán bộ]`<CHU_THE_CA_NHAN>`** , **[viên chức]`<CHU_THE_CA_NHAN>`** trong các **[đơn vị sự nghiệp]`<TO_CHUC_DOANH_NGHIEP>`** của Nhà nước ) ban hành kèm theo **[Nghị định số 204/2004/NĐ-CP]`<THAM_CHIEU_PHAP_LY>`** **[ngày 14 tháng 12 năm 2004]`<NGAY_THAM_CHIEU>`** của **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** về chế độ **[tiền lương]`<TAI_SAN_VAT_CHAT>`** đối với **[cán bộ , công chức , viên chức]`<CHU_THE_CA_NHAN>`** và lực lượng vũ trang ( sau đây viết tắt là **[Nghị định số 204/2004/NĐ-CP]`<THAM_CHIEU_PHAP_LY>`** ) , cụ]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 8** → `DIEU` (span: `[0:2]`)
- `[e1]` **1 . Các chức danh nghề nghiệp viên chức chuyên ngành tuyên truyền viên văn hóa quy định tại Thông tư này được áp dụng Bảng 3 ( Bảng lương chuyên môn , nghiệp vụ đối với cán bộ , viên chức trong các đơn vị sự nghiệp của Nhà nước ) ban hành kèm theo Nghị định số 204/2004/NĐ-CP ngày 14 tháng 12 năm 2004 của Chính phủ về chế độ tiền lương đối với cán bộ , công chức , viên chức và lực lượng vũ trang ( sau đây viết tắt là Nghị định số 204/2004/NĐ-CP ) , cụ** → `KHOAN` (span: `[3:75]`)
- `[e2]` **Thông tư này** → `THAM_CHIEU_PHAP_LY` (span: `[14:16]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **Nghị định số 204/2004/NĐ-CP** → `THAM_CHIEU_PHAP_LY` (span: `[40:43]`) *(lồng trong `e1` (`KHOAN`))*
- `[e4]` **Nghị định số 204/2004/NĐ-CP** → `THAM_CHIEU_PHAP_LY` (span: `[69:72]`) *(lồng trong `e1` (`KHOAN`))*
- `[e5]` **quy định tại** → `TU_KHOA_PHAP_LY` (span: `[12:14]`) *(lồng trong `e1` (`KHOAN`))*
- `[e6]` **ngày 14 tháng 12 năm 2004** → `NGAY_THAM_CHIEU` (span: `[43:49]`) *(lồng trong `e1` (`KHOAN`))*
- `[e7]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[50:51]`) *(lồng trong `e1` (`KHOAN`))*
- `[e8]` **đơn vị sự nghiệp** → `TO_CHUC_DOANH_NGHIEP` (span: `[32:34]`) *(lồng trong `e1` (`KHOAN`))*
- `[e9]` **viên chức** → `CHU_THE_CA_NHAN` (span: `[8:9]`) *(lồng trong `e1` (`KHOAN`))*
- `[e10]` **cán bộ** → `CHU_THE_CA_NHAN` (span: `[27:28]`) *(lồng trong `e1` (`KHOAN`))*
- `[e11]` **viên chức** → `CHU_THE_CA_NHAN` (span: `[29:30]`) *(lồng trong `e1` (`KHOAN`))*
- `[e12]` **cán bộ , công chức , viên chức** → `CHU_THE_CA_NHAN` (span: `[55:60]`) *(lồng trong `e1` (`KHOAN`))*
- `[e13]` **tiền lương** → `TAI_SAN_VAT_CHAT` (span: `[53:54]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 1 . Các chức danh nghề nghiệp viên chức chuyên ngành tuyên truyền viên văn hóa quy định tại Thông tư này được áp dụng Bảng 3 ( Bảng lương chuyên môn , nghiệp vụ đối với cán bộ , viên chức trong các đơn vị sự nghiệp của Nhà nước ) ban hành kèm theo Nghị định số 204/2004/NĐ-CP ngày 14 tháng 12 năm 2004 của Chính phủ về chế độ tiền lương đối với cán bộ , công chức , viên chức và lực lượng vũ trang ( sau đây viết tắt là Nghị định số 204/2004/NĐ-CP ) , cụ `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 8 `[DIEU]`)
- (`e5` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e2` Thông tư này `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 1 . Các chức danh nghề nghiệp viên chức chuyên ngành tuyên truyền viên văn hóa quy định tại Thông tư này được áp dụng Bảng 3 ( Bảng lương chuyên môn , nghiệp vụ đối với cán bộ , viên chức trong các đơn vị sự nghiệp của Nhà nước ) ban hành kèm theo Nghị định số 204/2004/NĐ-CP ngày 14 tháng 12 năm 2004 của Chính phủ về chế độ tiền lương đối với cán bộ , công chức , viên chức và lực lượng vũ trang ( sau đây viết tắt là Nghị định số 204/2004/NĐ-CP ) , cụ `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e2` Thông tư này `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e5` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Nghị định số 204/2004/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 1 . Các chức danh nghề nghiệp viên chức chuyên ngành tuyên truyền viên văn hóa quy định tại Thông tư này được áp dụng Bảng 3 ( Bảng lương chuyên môn , nghiệp vụ đối với cán bộ , viên chức trong các đơn vị sự nghiệp của Nhà nước ) ban hành kèm theo Nghị định số 204/2004/NĐ-CP ngày 14 tháng 12 năm 2004 của Chính phủ về chế độ tiền lương đối với cán bộ , công chức , viên chức và lực lượng vũ trang ( sau đây viết tắt là Nghị định số 204/2004/NĐ-CP ) , cụ `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Nghị định số 204/2004/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e5` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e4` Nghị định số 204/2004/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 1 . Các chức danh nghề nghiệp viên chức chuyên ngành tuyên truyền viên văn hóa quy định tại Thông tư này được áp dụng Bảng 3 ( Bảng lương chuyên môn , nghiệp vụ đối với cán bộ , viên chức trong các đơn vị sự nghiệp của Nhà nước ) ban hành kèm theo Nghị định số 204/2004/NĐ-CP ngày 14 tháng 12 năm 2004 của Chính phủ về chế độ tiền lương đối với cán bộ , công chức , viên chức và lực lượng vũ trang ( sau đây viết tắt là Nghị định số 204/2004/NĐ-CP ) , cụ `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e4` Nghị định số 204/2004/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e3` Nghị định số 204/2004/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e6` ngày 14 tháng 12 năm 2004 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #02_2023_TT-BVHTTDL_159924#body_context_58 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[02/2023/TT-BVHTTDL]`<SO_HIEU>`** của **[Bộ Văn hóa , Thể thao và Du lịch]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Lao động - Thương binh và Xã hội]`<LINH_VUC>`** . **[Điều 8]`<DIEU>`** . **[2 . Sau khi hết thời gian tập sự theo quy định và được **[cấp có thẩm quyền]`<CO_QUAN_THAM_QUYEN>`** quản lý **[viên chức]`<CHU_THE_CA_NHAN>`** **[quyết định bổ nhiệm]`<GIAY_TO_HO_SO>`** chức danh nghề nghiệp **[viên chức]`<CHU_THE_CA_NHAN>`** tuyên truyền viên văn hóa thì thực hiện xếp bậc lương theo chức danh nghề nghiệp được bổ nhiệm như sau :]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **02/2023/TT-BVHTTDL** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Văn hóa , Thể thao và Du lịch** → `CO_QUAN_BAN_HANH` (span: `[4:10]`)
- `[e3]` **Lao động - Thương binh và Xã hội** → `LINH_VUC` (span: `[12:17]`)
- `[e4]` **Điều 8** → `DIEU` (span: `[18:20]`)
- `[e5]` **2 . Sau khi hết thời gian tập sự theo quy định và được cấp có thẩm quyền quản lý viên chức quyết định bổ nhiệm chức danh nghề nghiệp viên chức tuyên truyền viên văn hóa thì thực hiện xếp bậc lương theo chức danh nghề nghiệp được bổ nhiệm như sau :** → `KHOAN` (span: `[21:57]`)
- `[e6]` **cấp có thẩm quyền** → `CO_QUAN_THAM_QUYEN` (span: `[32:35]`) *(lồng trong `e5` (`KHOAN`))*
- `[e7]` **quyết định bổ nhiệm** → `GIAY_TO_HO_SO` (span: `[37:39]`) *(lồng trong `e5` (`KHOAN`))*
- `[e8]` **viên chức** → `CHU_THE_CA_NHAN` (span: `[36:37]`) *(lồng trong `e5` (`KHOAN`))*
- `[e9]` **viên chức** → `CHU_THE_CA_NHAN` (span: `[41:42]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Văn hóa , Thể thao và Du lịch `[CO_QUAN_BAN_HANH]`)
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Lao động - Thương binh và Xã hội `[LINH_VUC]`)
- (`e4` Điều 8 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`)
- (`e5` 2 . Sau khi hết thời gian tập sự theo quy định và được cấp có thẩm quyền quản lý viên chức quyết định bổ nhiệm chức danh nghề nghiệp viên chức tuyên truyền viên văn hóa thì thực hiện xếp bậc lương theo chức danh nghề nghiệp được bổ nhiệm như sau : `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 8 `[DIEU]`)
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Lao động - Thương binh và Xã hội `[LINH_VUC]`)
- (`e5` 2 . Sau khi hết thời gian tập sự theo quy định và được cấp có thẩm quyền quản lý viên chức quyết định bổ nhiệm chức danh nghề nghiệp viên chức tuyên truyền viên văn hóa thì thực hiện xếp bậc lương theo chức danh nghề nghiệp được bổ nhiệm như sau : `[KHOAN]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Lao động - Thương binh và Xã hội `[LINH_VUC]`)


---

### Mẫu #02_2023_TT-BVHTTDL_159924#body_standalone_59 (Loại: `body_standalone`)
> **[Điều 8]`<DIEU>`** . **[2 . Sau khi hết thời gian tập sự theo quy định và được **[cấp có thẩm quyền]`<CO_QUAN_THAM_QUYEN>`** quản lý **[viên chức]`<CHU_THE_CA_NHAN>`** **[quyết định bổ nhiệm]`<GIAY_TO_HO_SO>`** chức danh nghề nghiệp **[viên chức]`<CHU_THE_CA_NHAN>`** tuyên truyền viên văn hóa thì thực hiện xếp bậc lương theo chức danh nghề nghiệp được bổ nhiệm như sau :]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 8** → `DIEU` (span: `[0:2]`)
- `[e1]` **2 . Sau khi hết thời gian tập sự theo quy định và được cấp có thẩm quyền quản lý viên chức quyết định bổ nhiệm chức danh nghề nghiệp viên chức tuyên truyền viên văn hóa thì thực hiện xếp bậc lương theo chức danh nghề nghiệp được bổ nhiệm như sau :** → `KHOAN` (span: `[3:39]`)
- `[e2]` **cấp có thẩm quyền** → `CO_QUAN_THAM_QUYEN` (span: `[14:17]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **quyết định bổ nhiệm** → `GIAY_TO_HO_SO` (span: `[19:21]`) *(lồng trong `e1` (`KHOAN`))*
- `[e4]` **viên chức** → `CHU_THE_CA_NHAN` (span: `[18:19]`) *(lồng trong `e1` (`KHOAN`))*
- `[e5]` **viên chức** → `CHU_THE_CA_NHAN` (span: `[23:24]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 2 . Sau khi hết thời gian tập sự theo quy định và được cấp có thẩm quyền quản lý viên chức quyết định bổ nhiệm chức danh nghề nghiệp viên chức tuyên truyền viên văn hóa thì thực hiện xếp bậc lương theo chức danh nghề nghiệp được bổ nhiệm như sau : `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 8 `[DIEU]`)


---

### Mẫu #02_2023_TT-BVHTTDL_159924#body_context_60 (Loại: `body_context`)
> **[Bộ Văn hóa , Thể thao và Du lịch]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[02/2023/TT-BVHTTDL]`<SO_HIEU>`** . **[Điều 8]`<DIEU>`** . **[Khoản 2]`<KHOAN>`** . **[a ) Trường hợp bổ nhiệm chức danh nghề nghiệp tuyên truyền viên văn hóa trung cấp : **[Viên chức]`<CHU_THE_CA_NHAN>`** có trình độ đào tạo trung cấp khi tuyển dụng , phù hợp với vị trí việc làm tuyển dụng được xếp bậc 1 , hệ số lương 1,86 , ngạch **[viên chức]`<CHU_THE_CA_NHAN>`** loại B ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[7:8]`)
- `[e1]` **02/2023/TT-BVHTTDL** → `SO_HIEU` (span: `[9:10]`)
- `[e2]` **Bộ Văn hóa , Thể thao và Du lịch** → `CO_QUAN_BAN_HANH` (span: `[0:6]`)
- `[e3]` **Điều 8** → `DIEU` (span: `[11:13]`)
- `[e4]` **Khoản 2** → `KHOAN` (span: `[14:16]`)
- `[e5]` **a ) Trường hợp bổ nhiệm chức danh nghề nghiệp tuyên truyền viên văn hóa trung cấp : Viên chức có trình độ đào tạo trung cấp khi tuyển dụng , phù hợp với vị trí việc làm tuyển dụng được xếp bậc 1 , hệ số lương 1,86 , ngạch viên chức loại B ;** → `DIEM` (span: `[17:54]`)
- `[e6]` **Viên chức** → `CHU_THE_CA_NHAN` (span: `[27:28]`) *(lồng trong `e5` (`DIEM`))*
- `[e7]` **viên chức** → `CHU_THE_CA_NHAN` (span: `[50:51]`) *(lồng trong `e5` (`DIEM`))*

**Quan hệ:**
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Văn hóa , Thể thao và Du lịch `[CO_QUAN_BAN_HANH]`)
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 8 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`)
- (`e4` Khoản 2 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 8 `[DIEU]`)
- (`e5` a ) Trường hợp bổ nhiệm chức danh nghề nghiệp tuyên truyền viên văn hóa trung cấp : Viên chức có trình độ đào tạo trung cấp khi tuyển dụng , phù hợp với vị trí việc làm tuyển dụng được xếp bậc 1 , hệ số lương 1,86 , ngạch viên chức loại B ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e4` Khoản 2 `[KHOAN]`)


---

### Mẫu #02_2023_TT-BVHTTDL_159924#body_standalone_61 (Loại: `body_standalone`)
> **[Điều 8]`<DIEU>`** . **[Khoản 2]`<KHOAN>`** . **[a ) Trường hợp bổ nhiệm chức danh nghề nghiệp tuyên truyền viên văn hóa trung cấp : **[Viên chức]`<CHU_THE_CA_NHAN>`** có trình độ đào tạo trung cấp khi tuyển dụng , phù hợp với vị trí việc làm tuyển dụng được xếp bậc 1 , hệ số lương 1,86 , ngạch **[viên chức]`<CHU_THE_CA_NHAN>`** loại B ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Điều 8** → `DIEU` (span: `[0:2]`)
- `[e1]` **Khoản 2** → `KHOAN` (span: `[3:5]`)
- `[e2]` **a ) Trường hợp bổ nhiệm chức danh nghề nghiệp tuyên truyền viên văn hóa trung cấp : Viên chức có trình độ đào tạo trung cấp khi tuyển dụng , phù hợp với vị trí việc làm tuyển dụng được xếp bậc 1 , hệ số lương 1,86 , ngạch viên chức loại B ;** → `DIEM` (span: `[6:43]`)
- `[e3]` **Viên chức** → `CHU_THE_CA_NHAN` (span: `[16:17]`) *(lồng trong `e2` (`DIEM`))*
- `[e4]` **viên chức** → `CHU_THE_CA_NHAN` (span: `[39:40]`) *(lồng trong `e2` (`DIEM`))*

**Quan hệ:**
- (`e1` Khoản 2 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 8 `[DIEU]`)
- (`e2` a ) Trường hợp bổ nhiệm chức danh nghề nghiệp tuyên truyền viên văn hóa trung cấp : Viên chức có trình độ đào tạo trung cấp khi tuyển dụng , phù hợp với vị trí việc làm tuyển dụng được xếp bậc 1 , hệ số lương 1,86 , ngạch viên chức loại B ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e1` Khoản 2 `[KHOAN]`)


---

### Mẫu #02_2023_TT-BVHTTDL_159924#body_context_62 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[02/2023/TT-BVHTTDL]`<SO_HIEU>`** của **[Bộ Văn hóa , Thể thao và Du lịch]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Lao động - Thương binh và Xã hội]`<LINH_VUC>`** . **[Điều 8]`<DIEU>`** . **[Khoản 2]`<KHOAN>`** . **[a ) Trường hợp bổ nhiệm chức danh nghề nghiệp tuyên truyền viên văn hóa trung cấp : **[Viên chức]`<CHU_THE_CA_NHAN>`** có trình độ đào tạo cao đẳng trở lên khi tuyển dụng , phù hợp với vị trí việc làm tuyển dụng được xếp bậc 2 , hệ số lương 2,06 , ngạch **[viên chức]`<CHU_THE_CA_NHAN>`** loại B.]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **02/2023/TT-BVHTTDL** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Văn hóa , Thể thao và Du lịch** → `CO_QUAN_BAN_HANH` (span: `[4:10]`)
- `[e3]` **Lao động - Thương binh và Xã hội** → `LINH_VUC` (span: `[12:17]`)
- `[e4]` **Điều 8** → `DIEU` (span: `[18:20]`)
- `[e5]` **Khoản 2** → `KHOAN` (span: `[21:23]`)
- `[e6]` **a ) Trường hợp bổ nhiệm chức danh nghề nghiệp tuyên truyền viên văn hóa trung cấp : Viên chức có trình độ đào tạo cao đẳng trở lên khi tuyển dụng , phù hợp với vị trí việc làm tuyển dụng được xếp bậc 2 , hệ số lương 2,06 , ngạch viên chức loại B.** → `DIEM` (span: `[24:62]`)
- `[e7]` **Viên chức** → `CHU_THE_CA_NHAN` (span: `[34:35]`) *(lồng trong `e6` (`DIEM`))*
- `[e8]` **viên chức** → `CHU_THE_CA_NHAN` (span: `[59:60]`) *(lồng trong `e6` (`DIEM`))*

**Quan hệ:**
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Văn hóa , Thể thao và Du lịch `[CO_QUAN_BAN_HANH]`)
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Lao động - Thương binh và Xã hội `[LINH_VUC]`)
- (`e4` Điều 8 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`)
- (`e5` Khoản 2 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 8 `[DIEU]`)
- (`e6` a ) Trường hợp bổ nhiệm chức danh nghề nghiệp tuyên truyền viên văn hóa trung cấp : Viên chức có trình độ đào tạo cao đẳng trở lên khi tuyển dụng , phù hợp với vị trí việc làm tuyển dụng được xếp bậc 2 , hệ số lương 2,06 , ngạch viên chức loại B. `[DIEM]`) ==[ **THUOC_VE** ]==> (`e5` Khoản 2 `[KHOAN]`)
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Lao động - Thương binh và Xã hội `[LINH_VUC]`)
- (`e6` a ) Trường hợp bổ nhiệm chức danh nghề nghiệp tuyên truyền viên văn hóa trung cấp : Viên chức có trình độ đào tạo cao đẳng trở lên khi tuyển dụng , phù hợp với vị trí việc làm tuyển dụng được xếp bậc 2 , hệ số lương 2,06 , ngạch viên chức loại B. `[DIEM]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Lao động - Thương binh và Xã hội `[LINH_VUC]`)


---

### Mẫu #02_2023_TT-BVHTTDL_159924#body_standalone_63 (Loại: `body_standalone`)
> **[Điều 8]`<DIEU>`** . **[Khoản 2]`<KHOAN>`** . **[a ) Trường hợp bổ nhiệm chức danh nghề nghiệp tuyên truyền viên văn hóa trung cấp : **[Viên chức]`<CHU_THE_CA_NHAN>`** có trình độ đào tạo cao đẳng trở lên khi tuyển dụng , phù hợp với vị trí việc làm tuyển dụng được xếp bậc 2 , hệ số lương 2,06 , ngạch **[viên chức]`<CHU_THE_CA_NHAN>`** loại B.]`<DIEM>`**

**Thực thể:**
- `[e0]` **Điều 8** → `DIEU` (span: `[0:2]`)
- `[e1]` **Khoản 2** → `KHOAN` (span: `[3:5]`)
- `[e2]` **a ) Trường hợp bổ nhiệm chức danh nghề nghiệp tuyên truyền viên văn hóa trung cấp : Viên chức có trình độ đào tạo cao đẳng trở lên khi tuyển dụng , phù hợp với vị trí việc làm tuyển dụng được xếp bậc 2 , hệ số lương 2,06 , ngạch viên chức loại B.** → `DIEM` (span: `[6:44]`)
- `[e3]` **Viên chức** → `CHU_THE_CA_NHAN` (span: `[16:17]`) *(lồng trong `e2` (`DIEM`))*
- `[e4]` **viên chức** → `CHU_THE_CA_NHAN` (span: `[41:42]`) *(lồng trong `e2` (`DIEM`))*

**Quan hệ:**
- (`e1` Khoản 2 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 8 `[DIEU]`)
- (`e2` a ) Trường hợp bổ nhiệm chức danh nghề nghiệp tuyên truyền viên văn hóa trung cấp : Viên chức có trình độ đào tạo cao đẳng trở lên khi tuyển dụng , phù hợp với vị trí việc làm tuyển dụng được xếp bậc 2 , hệ số lương 2,06 , ngạch viên chức loại B. `[DIEM]`) ==[ **THUOC_VE** ]==> (`e1` Khoản 2 `[KHOAN]`)


---

### Mẫu #02_2023_TT-BVHTTDL_159924#body_context_64 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[02/2023/TT-BVHTTDL]`<SO_HIEU>`** của **[Bộ Văn hóa , Thể thao và Du lịch]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Lao động - Thương binh và Xã hội]`<LINH_VUC>`** . **[Điều 8]`<DIEU>`** . **[Khoản 2]`<KHOAN>`** . **[b ) Trường hợp bổ nhiệm chức danh nghề nghiệp tuyên truyền viên văn hóa : **[Viên chức]`<CHU_THE_CA_NHAN>`** có trình độ đào tạo đại học khi tuyển dụng , phù hợp với vị trí việc làm tuyển dụng được xếp bậc 1 , hệ số lương 2,34 , ngạch **[viên chức]`<CHU_THE_CA_NHAN>`** loại A1 ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **02/2023/TT-BVHTTDL** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Văn hóa , Thể thao và Du lịch** → `CO_QUAN_BAN_HANH` (span: `[4:10]`)
- `[e3]` **Lao động - Thương binh và Xã hội** → `LINH_VUC` (span: `[12:17]`)
- `[e4]` **Điều 8** → `DIEU` (span: `[18:20]`)
- `[e5]` **Khoản 2** → `KHOAN` (span: `[21:23]`)
- `[e6]` **b ) Trường hợp bổ nhiệm chức danh nghề nghiệp tuyên truyền viên văn hóa : Viên chức có trình độ đào tạo đại học khi tuyển dụng , phù hợp với vị trí việc làm tuyển dụng được xếp bậc 1 , hệ số lương 2,34 , ngạch viên chức loại A1 ;** → `DIEM` (span: `[24:60]`)
- `[e7]` **Viên chức** → `CHU_THE_CA_NHAN` (span: `[33:34]`) *(lồng trong `e6` (`DIEM`))*
- `[e8]` **viên chức** → `CHU_THE_CA_NHAN` (span: `[56:57]`) *(lồng trong `e6` (`DIEM`))*

**Quan hệ:**
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Văn hóa , Thể thao và Du lịch `[CO_QUAN_BAN_HANH]`)
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Lao động - Thương binh và Xã hội `[LINH_VUC]`)
- (`e4` Điều 8 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`)
- (`e5` Khoản 2 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 8 `[DIEU]`)
- (`e6` b ) Trường hợp bổ nhiệm chức danh nghề nghiệp tuyên truyền viên văn hóa : Viên chức có trình độ đào tạo đại học khi tuyển dụng , phù hợp với vị trí việc làm tuyển dụng được xếp bậc 1 , hệ số lương 2,34 , ngạch viên chức loại A1 ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e5` Khoản 2 `[KHOAN]`)
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Lao động - Thương binh và Xã hội `[LINH_VUC]`)
- (`e6` b ) Trường hợp bổ nhiệm chức danh nghề nghiệp tuyên truyền viên văn hóa : Viên chức có trình độ đào tạo đại học khi tuyển dụng , phù hợp với vị trí việc làm tuyển dụng được xếp bậc 1 , hệ số lương 2,34 , ngạch viên chức loại A1 ; `[DIEM]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Lao động - Thương binh và Xã hội `[LINH_VUC]`)


---

### Mẫu #02_2023_TT-BVHTTDL_159924#body_standalone_65 (Loại: `body_standalone`)
> **[Điều 8]`<DIEU>`** . **[Khoản 2]`<KHOAN>`** . **[b ) Trường hợp bổ nhiệm chức danh nghề nghiệp tuyên truyền viên văn hóa : **[Viên chức]`<CHU_THE_CA_NHAN>`** có trình độ đào tạo đại học khi tuyển dụng , phù hợp với vị trí việc làm tuyển dụng được xếp bậc 1 , hệ số lương 2,34 , ngạch **[viên chức]`<CHU_THE_CA_NHAN>`** loại A1 ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Điều 8** → `DIEU` (span: `[0:2]`)
- `[e1]` **Khoản 2** → `KHOAN` (span: `[3:5]`)
- `[e2]` **b ) Trường hợp bổ nhiệm chức danh nghề nghiệp tuyên truyền viên văn hóa : Viên chức có trình độ đào tạo đại học khi tuyển dụng , phù hợp với vị trí việc làm tuyển dụng được xếp bậc 1 , hệ số lương 2,34 , ngạch viên chức loại A1 ;** → `DIEM` (span: `[6:42]`)
- `[e3]` **Viên chức** → `CHU_THE_CA_NHAN` (span: `[15:16]`) *(lồng trong `e2` (`DIEM`))*
- `[e4]` **viên chức** → `CHU_THE_CA_NHAN` (span: `[38:39]`) *(lồng trong `e2` (`DIEM`))*

**Quan hệ:**
- (`e1` Khoản 2 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 8 `[DIEU]`)
- (`e2` b ) Trường hợp bổ nhiệm chức danh nghề nghiệp tuyên truyền viên văn hóa : Viên chức có trình độ đào tạo đại học khi tuyển dụng , phù hợp với vị trí việc làm tuyển dụng được xếp bậc 1 , hệ số lương 2,34 , ngạch viên chức loại A1 ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e1` Khoản 2 `[KHOAN]`)


---

### Mẫu #02_2023_TT-BVHTTDL_159924#body_context_66 (Loại: `body_context`)
> **[Bộ Văn hóa , Thể thao và Du lịch]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[02/2023/TT-BVHTTDL]`<SO_HIEU>`** . **[Điều 8]`<DIEU>`** . **[Khoản 2]`<KHOAN>`** . **[b ) Trường hợp bổ nhiệm chức danh nghề nghiệp tuyên truyền viên văn hóa : **[Viên chức]`<CHU_THE_CA_NHAN>`** có trình độ đào tạo thạc sỹ khi tuyển dụng , phù hợp với vị trí việc làm tuyển dụng được xếp bậc 2 , hệ số lương 2,67 , ngạch **[viên chức]`<CHU_THE_CA_NHAN>`** loại A1 ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[7:8]`)
- `[e1]` **02/2023/TT-BVHTTDL** → `SO_HIEU` (span: `[9:10]`)
- `[e2]` **Bộ Văn hóa , Thể thao và Du lịch** → `CO_QUAN_BAN_HANH` (span: `[0:6]`)
- `[e3]` **Điều 8** → `DIEU` (span: `[11:13]`)
- `[e4]` **Khoản 2** → `KHOAN` (span: `[14:16]`)
- `[e5]` **b ) Trường hợp bổ nhiệm chức danh nghề nghiệp tuyên truyền viên văn hóa : Viên chức có trình độ đào tạo thạc sỹ khi tuyển dụng , phù hợp với vị trí việc làm tuyển dụng được xếp bậc 2 , hệ số lương 2,67 , ngạch viên chức loại A1 ;** → `DIEM` (span: `[17:54]`)
- `[e6]` **Viên chức** → `CHU_THE_CA_NHAN` (span: `[26:27]`) *(lồng trong `e5` (`DIEM`))*
- `[e7]` **viên chức** → `CHU_THE_CA_NHAN` (span: `[50:51]`) *(lồng trong `e5` (`DIEM`))*

**Quan hệ:**
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Văn hóa , Thể thao và Du lịch `[CO_QUAN_BAN_HANH]`)
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 8 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`)
- (`e4` Khoản 2 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 8 `[DIEU]`)
- (`e5` b ) Trường hợp bổ nhiệm chức danh nghề nghiệp tuyên truyền viên văn hóa : Viên chức có trình độ đào tạo thạc sỹ khi tuyển dụng , phù hợp với vị trí việc làm tuyển dụng được xếp bậc 2 , hệ số lương 2,67 , ngạch viên chức loại A1 ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e4` Khoản 2 `[KHOAN]`)


---

### Mẫu #02_2023_TT-BVHTTDL_159924#body_standalone_67 (Loại: `body_standalone`)
> **[Điều 8]`<DIEU>`** . **[Khoản 2]`<KHOAN>`** . **[b ) Trường hợp bổ nhiệm chức danh nghề nghiệp tuyên truyền viên văn hóa : **[Viên chức]`<CHU_THE_CA_NHAN>`** có trình độ đào tạo thạc sỹ khi tuyển dụng , phù hợp với vị trí việc làm tuyển dụng được xếp bậc 2 , hệ số lương 2,67 , ngạch **[viên chức]`<CHU_THE_CA_NHAN>`** loại A1 ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Điều 8** → `DIEU` (span: `[0:2]`)
- `[e1]` **Khoản 2** → `KHOAN` (span: `[3:5]`)
- `[e2]` **b ) Trường hợp bổ nhiệm chức danh nghề nghiệp tuyên truyền viên văn hóa : Viên chức có trình độ đào tạo thạc sỹ khi tuyển dụng , phù hợp với vị trí việc làm tuyển dụng được xếp bậc 2 , hệ số lương 2,67 , ngạch viên chức loại A1 ;** → `DIEM` (span: `[6:43]`)
- `[e3]` **Viên chức** → `CHU_THE_CA_NHAN` (span: `[15:16]`) *(lồng trong `e2` (`DIEM`))*
- `[e4]` **viên chức** → `CHU_THE_CA_NHAN` (span: `[39:40]`) *(lồng trong `e2` (`DIEM`))*

**Quan hệ:**
- (`e1` Khoản 2 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 8 `[DIEU]`)
- (`e2` b ) Trường hợp bổ nhiệm chức danh nghề nghiệp tuyên truyền viên văn hóa : Viên chức có trình độ đào tạo thạc sỹ khi tuyển dụng , phù hợp với vị trí việc làm tuyển dụng được xếp bậc 2 , hệ số lương 2,67 , ngạch viên chức loại A1 ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e1` Khoản 2 `[KHOAN]`)


---

### Mẫu #02_2023_TT-BVHTTDL_159924#body_context_68 (Loại: `body_context`)
> **[Bộ Văn hóa , Thể thao và Du lịch]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[02/2023/TT-BVHTTDL]`<SO_HIEU>`** . **[Điều 8]`<DIEU>`** . **[Khoản 2]`<KHOAN>`** . **[b ) Trường hợp bổ nhiệm chức danh nghề nghiệp tuyên truyền viên văn hóa : **[Viên chức]`<CHU_THE_CA_NHAN>`** có trình độ đào tạo tiến sỹ khi tuyển dụng , phù hợp với vị trí việc làm tuyển dụng được xếp bậc 3 , hệ số lương 3,00 , ngạch **[viên chức]`<CHU_THE_CA_NHAN>`** loại A1 .]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[7:8]`)
- `[e1]` **02/2023/TT-BVHTTDL** → `SO_HIEU` (span: `[9:10]`)
- `[e2]` **Bộ Văn hóa , Thể thao và Du lịch** → `CO_QUAN_BAN_HANH` (span: `[0:6]`)
- `[e3]` **Điều 8** → `DIEU` (span: `[11:13]`)
- `[e4]` **Khoản 2** → `KHOAN` (span: `[14:16]`)
- `[e5]` **b ) Trường hợp bổ nhiệm chức danh nghề nghiệp tuyên truyền viên văn hóa : Viên chức có trình độ đào tạo tiến sỹ khi tuyển dụng , phù hợp với vị trí việc làm tuyển dụng được xếp bậc 3 , hệ số lương 3,00 , ngạch viên chức loại A1 .** → `DIEM` (span: `[17:53]`)
- `[e6]` **Viên chức** → `CHU_THE_CA_NHAN` (span: `[26:27]`) *(lồng trong `e5` (`DIEM`))*
- `[e7]` **viên chức** → `CHU_THE_CA_NHAN` (span: `[49:50]`) *(lồng trong `e5` (`DIEM`))*

**Quan hệ:**
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Văn hóa , Thể thao và Du lịch `[CO_QUAN_BAN_HANH]`)
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 8 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`)
- (`e4` Khoản 2 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 8 `[DIEU]`)
- (`e5` b ) Trường hợp bổ nhiệm chức danh nghề nghiệp tuyên truyền viên văn hóa : Viên chức có trình độ đào tạo tiến sỹ khi tuyển dụng , phù hợp với vị trí việc làm tuyển dụng được xếp bậc 3 , hệ số lương 3,00 , ngạch viên chức loại A1 . `[DIEM]`) ==[ **THUOC_VE** ]==> (`e4` Khoản 2 `[KHOAN]`)


---

### Mẫu #02_2023_TT-BVHTTDL_159924#body_standalone_69 (Loại: `body_standalone`)
> **[Điều 8]`<DIEU>`** . **[Khoản 2]`<KHOAN>`** . **[b ) Trường hợp bổ nhiệm chức danh nghề nghiệp tuyên truyền viên văn hóa : **[Viên chức]`<CHU_THE_CA_NHAN>`** có trình độ đào tạo tiến sỹ khi tuyển dụng , phù hợp với vị trí việc làm tuyển dụng được xếp bậc 3 , hệ số lương 3,00 , ngạch **[viên chức]`<CHU_THE_CA_NHAN>`** loại A1 .]`<DIEM>`**

**Thực thể:**
- `[e0]` **Điều 8** → `DIEU` (span: `[0:2]`)
- `[e1]` **Khoản 2** → `KHOAN` (span: `[3:5]`)
- `[e2]` **b ) Trường hợp bổ nhiệm chức danh nghề nghiệp tuyên truyền viên văn hóa : Viên chức có trình độ đào tạo tiến sỹ khi tuyển dụng , phù hợp với vị trí việc làm tuyển dụng được xếp bậc 3 , hệ số lương 3,00 , ngạch viên chức loại A1 .** → `DIEM` (span: `[6:42]`)
- `[e3]` **Viên chức** → `CHU_THE_CA_NHAN` (span: `[15:16]`) *(lồng trong `e2` (`DIEM`))*
- `[e4]` **viên chức** → `CHU_THE_CA_NHAN` (span: `[38:39]`) *(lồng trong `e2` (`DIEM`))*

**Quan hệ:**
- (`e1` Khoản 2 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 8 `[DIEU]`)
- (`e2` b ) Trường hợp bổ nhiệm chức danh nghề nghiệp tuyên truyền viên văn hóa : Viên chức có trình độ đào tạo tiến sỹ khi tuyển dụng , phù hợp với vị trí việc làm tuyển dụng được xếp bậc 3 , hệ số lương 3,00 , ngạch viên chức loại A1 . `[DIEM]`) ==[ **THUOC_VE** ]==> (`e1` Khoản 2 `[KHOAN]`)


---

### Mẫu #02_2023_TT-BVHTTDL_159924#body_context_70 (Loại: `body_context`)
> **[Bộ Văn hóa , Thể thao và Du lịch]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[02/2023/TT-BVHTTDL]`<SO_HIEU>`** . **[Điều 8]`<DIEU>`** . **[3 . Việc chuyển xếp lương đối với **[viên chức]`<CHU_THE_CA_NHAN>`** từ chức danh nghề nghiệp hiện giữ sang chức danh nghề nghiệp tuyên truyền viên văn hóa **[quy định tại]`<TU_KHOA_PHAP_LY>`** **[Thông tư này]`<THAM_CHIEU_PHAP_LY>`** thực hiện theo hướng dẫn tại Mục II **[Thông tư số 02/2007/TT -]`<THAM_CHIEU_PHAP_LY>`** BNV **[ngày 25 tháng 5 năm 2007]`<NGAY_THAM_CHIEU>`** của **[Bộ trưởng Bộ Nội vụ]`<CO_QUAN_THAM_QUYEN>`** hướng dẫn xếp lương khi nâng ngạch , chuyển ngạch , chuyển loại **[công chức]`<CHU_THE_CA_NHAN>`** , **[viên chức]`<CHU_THE_CA_NHAN>`** ( sau đây viết tắt là **[Thông tư số 02/2007/TT-BNV]`<THAM_CHIEU_PHAP_LY>`** ) .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[7:8]`)
- `[e1]` **02/2023/TT-BVHTTDL** → `SO_HIEU` (span: `[9:10]`)
- `[e2]` **Bộ Văn hóa , Thể thao và Du lịch** → `CO_QUAN_BAN_HANH` (span: `[0:6]`)
- `[e3]` **Điều 8** → `DIEU` (span: `[11:13]`)
- `[e4]` **3 . Việc chuyển xếp lương đối với viên chức từ chức danh nghề nghiệp hiện giữ sang chức danh nghề nghiệp tuyên truyền viên văn hóa quy định tại Thông tư này thực hiện theo hướng dẫn tại Mục II Thông tư số 02/2007/TT - BNV ngày 25 tháng 5 năm 2007 của Bộ trưởng Bộ Nội vụ hướng dẫn xếp lương khi nâng ngạch , chuyển ngạch , chuyển loại công chức , viên chức ( sau đây viết tắt là Thông tư số 02/2007/TT-BNV ) .** → `KHOAN` (span: `[14:80]`)
- `[e5]` **Thông tư này** → `THAM_CHIEU_PHAP_LY` (span: `[33:35]`) *(lồng trong `e4` (`KHOAN`))*
- `[e6]` **Thông tư số 02/2007/TT -** → `THAM_CHIEU_PHAP_LY` (span: `[40:44]`) *(lồng trong `e4` (`KHOAN`))*
- `[e7]` **Thông tư số 02/2007/TT-BNV** → `THAM_CHIEU_PHAP_LY` (span: `[75:78]`) *(lồng trong `e4` (`KHOAN`))*
- `[e8]` **quy định tại** → `TU_KHOA_PHAP_LY` (span: `[31:33]`) *(lồng trong `e4` (`KHOAN`))*
- `[e9]` **ngày 25 tháng 5 năm 2007** → `NGAY_THAM_CHIEU` (span: `[45:51]`) *(lồng trong `e4` (`KHOAN`))*
- `[e10]` **Bộ trưởng Bộ Nội vụ** → `CO_QUAN_THAM_QUYEN` (span: `[52:55]`) *(lồng trong `e4` (`KHOAN`))*
- `[e11]` **viên chức** → `CHU_THE_CA_NHAN` (span: `[21:22]`) *(lồng trong `e4` (`KHOAN`))*
- `[e12]` **công chức** → `CHU_THE_CA_NHAN` (span: `[66:67]`) *(lồng trong `e4` (`KHOAN`))*
- `[e13]` **viên chức** → `CHU_THE_CA_NHAN` (span: `[68:69]`) *(lồng trong `e4` (`KHOAN`))*

**Quan hệ:**
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Văn hóa , Thể thao và Du lịch `[CO_QUAN_BAN_HANH]`)
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 8 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`)
- (`e4` 3 . Việc chuyển xếp lương đối với viên chức từ chức danh nghề nghiệp hiện giữ sang chức danh nghề nghiệp tuyên truyền viên văn hóa quy định tại Thông tư này thực hiện theo hướng dẫn tại Mục II Thông tư số 02/2007/TT - BNV ngày 25 tháng 5 năm 2007 của Bộ trưởng Bộ Nội vụ hướng dẫn xếp lương khi nâng ngạch , chuyển ngạch , chuyển loại công chức , viên chức ( sau đây viết tắt là Thông tư số 02/2007/TT-BNV ) . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 8 `[DIEU]`)
- (`e8` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e5` Thông tư này `[THAM_CHIEU_PHAP_LY]`)
- (`e4` 3 . Việc chuyển xếp lương đối với viên chức từ chức danh nghề nghiệp hiện giữ sang chức danh nghề nghiệp tuyên truyền viên văn hóa quy định tại Thông tư này thực hiện theo hướng dẫn tại Mục II Thông tư số 02/2007/TT - BNV ngày 25 tháng 5 năm 2007 của Bộ trưởng Bộ Nội vụ hướng dẫn xếp lương khi nâng ngạch , chuyển ngạch , chuyển loại công chức , viên chức ( sau đây viết tắt là Thông tư số 02/2007/TT-BNV ) . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e5` Thông tư này `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e8` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e6` Thông tư số 02/2007/TT - `[THAM_CHIEU_PHAP_LY]`)
- (`e4` 3 . Việc chuyển xếp lương đối với viên chức từ chức danh nghề nghiệp hiện giữ sang chức danh nghề nghiệp tuyên truyền viên văn hóa quy định tại Thông tư này thực hiện theo hướng dẫn tại Mục II Thông tư số 02/2007/TT - BNV ngày 25 tháng 5 năm 2007 của Bộ trưởng Bộ Nội vụ hướng dẫn xếp lương khi nâng ngạch , chuyển ngạch , chuyển loại công chức , viên chức ( sau đây viết tắt là Thông tư số 02/2007/TT-BNV ) . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e6` Thông tư số 02/2007/TT - `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e8` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e7` Thông tư số 02/2007/TT-BNV `[THAM_CHIEU_PHAP_LY]`)
- (`e4` 3 . Việc chuyển xếp lương đối với viên chức từ chức danh nghề nghiệp hiện giữ sang chức danh nghề nghiệp tuyên truyền viên văn hóa quy định tại Thông tư này thực hiện theo hướng dẫn tại Mục II Thông tư số 02/2007/TT - BNV ngày 25 tháng 5 năm 2007 của Bộ trưởng Bộ Nội vụ hướng dẫn xếp lương khi nâng ngạch , chuyển ngạch , chuyển loại công chức , viên chức ( sau đây viết tắt là Thông tư số 02/2007/TT-BNV ) . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e7` Thông tư số 02/2007/TT-BNV `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e6` Thông tư số 02/2007/TT - `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e9` ngày 25 tháng 5 năm 2007 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #02_2023_TT-BVHTTDL_159924#body_standalone_71 (Loại: `body_standalone`)
> **[Điều 8]`<DIEU>`** . **[3 . Việc chuyển xếp lương đối với **[viên chức]`<CHU_THE_CA_NHAN>`** từ chức danh nghề nghiệp hiện giữ sang chức danh nghề nghiệp tuyên truyền viên văn hóa **[quy định tại]`<TU_KHOA_PHAP_LY>`** **[Thông tư này]`<THAM_CHIEU_PHAP_LY>`** thực hiện theo hướng dẫn tại Mục II **[Thông tư số 02/2007/TT -]`<THAM_CHIEU_PHAP_LY>`** BNV **[ngày 25 tháng 5 năm 2007]`<NGAY_THAM_CHIEU>`** của **[Bộ trưởng Bộ Nội vụ]`<CO_QUAN_THAM_QUYEN>`** hướng dẫn xếp lương khi nâng ngạch , chuyển ngạch , chuyển loại **[công chức]`<CHU_THE_CA_NHAN>`** , **[viên chức]`<CHU_THE_CA_NHAN>`** ( sau đây viết tắt là **[Thông tư số 02/2007/TT-BNV]`<THAM_CHIEU_PHAP_LY>`** ) .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 8** → `DIEU` (span: `[0:2]`)
- `[e1]` **3 . Việc chuyển xếp lương đối với viên chức từ chức danh nghề nghiệp hiện giữ sang chức danh nghề nghiệp tuyên truyền viên văn hóa quy định tại Thông tư này thực hiện theo hướng dẫn tại Mục II Thông tư số 02/2007/TT - BNV ngày 25 tháng 5 năm 2007 của Bộ trưởng Bộ Nội vụ hướng dẫn xếp lương khi nâng ngạch , chuyển ngạch , chuyển loại công chức , viên chức ( sau đây viết tắt là Thông tư số 02/2007/TT-BNV ) .** → `KHOAN` (span: `[3:69]`)
- `[e2]` **Thông tư này** → `THAM_CHIEU_PHAP_LY` (span: `[22:24]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **Thông tư số 02/2007/TT -** → `THAM_CHIEU_PHAP_LY` (span: `[29:33]`) *(lồng trong `e1` (`KHOAN`))*
- `[e4]` **Thông tư số 02/2007/TT-BNV** → `THAM_CHIEU_PHAP_LY` (span: `[64:67]`) *(lồng trong `e1` (`KHOAN`))*
- `[e5]` **quy định tại** → `TU_KHOA_PHAP_LY` (span: `[20:22]`) *(lồng trong `e1` (`KHOAN`))*
- `[e6]` **ngày 25 tháng 5 năm 2007** → `NGAY_THAM_CHIEU` (span: `[34:40]`) *(lồng trong `e1` (`KHOAN`))*
- `[e7]` **Bộ trưởng Bộ Nội vụ** → `CO_QUAN_THAM_QUYEN` (span: `[41:44]`) *(lồng trong `e1` (`KHOAN`))*
- `[e8]` **viên chức** → `CHU_THE_CA_NHAN` (span: `[10:11]`) *(lồng trong `e1` (`KHOAN`))*
- `[e9]` **công chức** → `CHU_THE_CA_NHAN` (span: `[55:56]`) *(lồng trong `e1` (`KHOAN`))*
- `[e10]` **viên chức** → `CHU_THE_CA_NHAN` (span: `[57:58]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 3 . Việc chuyển xếp lương đối với viên chức từ chức danh nghề nghiệp hiện giữ sang chức danh nghề nghiệp tuyên truyền viên văn hóa quy định tại Thông tư này thực hiện theo hướng dẫn tại Mục II Thông tư số 02/2007/TT - BNV ngày 25 tháng 5 năm 2007 của Bộ trưởng Bộ Nội vụ hướng dẫn xếp lương khi nâng ngạch , chuyển ngạch , chuyển loại công chức , viên chức ( sau đây viết tắt là Thông tư số 02/2007/TT-BNV ) . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 8 `[DIEU]`)
- (`e5` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e2` Thông tư này `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 3 . Việc chuyển xếp lương đối với viên chức từ chức danh nghề nghiệp hiện giữ sang chức danh nghề nghiệp tuyên truyền viên văn hóa quy định tại Thông tư này thực hiện theo hướng dẫn tại Mục II Thông tư số 02/2007/TT - BNV ngày 25 tháng 5 năm 2007 của Bộ trưởng Bộ Nội vụ hướng dẫn xếp lương khi nâng ngạch , chuyển ngạch , chuyển loại công chức , viên chức ( sau đây viết tắt là Thông tư số 02/2007/TT-BNV ) . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e2` Thông tư này `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e5` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Thông tư số 02/2007/TT - `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 3 . Việc chuyển xếp lương đối với viên chức từ chức danh nghề nghiệp hiện giữ sang chức danh nghề nghiệp tuyên truyền viên văn hóa quy định tại Thông tư này thực hiện theo hướng dẫn tại Mục II Thông tư số 02/2007/TT - BNV ngày 25 tháng 5 năm 2007 của Bộ trưởng Bộ Nội vụ hướng dẫn xếp lương khi nâng ngạch , chuyển ngạch , chuyển loại công chức , viên chức ( sau đây viết tắt là Thông tư số 02/2007/TT-BNV ) . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Thông tư số 02/2007/TT - `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e5` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e4` Thông tư số 02/2007/TT-BNV `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 3 . Việc chuyển xếp lương đối với viên chức từ chức danh nghề nghiệp hiện giữ sang chức danh nghề nghiệp tuyên truyền viên văn hóa quy định tại Thông tư này thực hiện theo hướng dẫn tại Mục II Thông tư số 02/2007/TT - BNV ngày 25 tháng 5 năm 2007 của Bộ trưởng Bộ Nội vụ hướng dẫn xếp lương khi nâng ngạch , chuyển ngạch , chuyển loại công chức , viên chức ( sau đây viết tắt là Thông tư số 02/2007/TT-BNV ) . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e4` Thông tư số 02/2007/TT-BNV `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e3` Thông tư số 02/2007/TT - `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e6` ngày 25 tháng 5 năm 2007 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #02_2023_TT-BVHTTDL_159924#body_context_72 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[02/2023/TT-BVHTTDL]`<SO_HIEU>`** ban hành **[ngày 21 tháng 02 năm 2023]`<NGAY_BAN_HANH>`** bởi **[Bộ Văn hóa , Thể thao và Du lịch]`<CO_QUAN_BAN_HANH>`** . **[Chương IV]`<CHUONG>`** . **[Điều 9 . Quy định chuyển tiếp]`<DIEU>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **02/2023/TT-BVHTTDL** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Văn hóa , Thể thao và Du lịch** → `CO_QUAN_BAN_HANH` (span: `[11:17]`)
- `[e3]` **ngày 21 tháng 02 năm 2023** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Chương IV** → `CHUONG` (span: `[18:20]`)
- `[e5]` **Điều 9 . Quy định chuyển tiếp** → `DIEU` (span: `[21:26]`)

**Quan hệ:**
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Văn hóa , Thể thao và Du lịch `[CO_QUAN_BAN_HANH]`)
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 21 tháng 02 năm 2023 `[NGAY_BAN_HANH]`)
- (`e4` Chương IV `[CHUONG]`) ==[ **THUOC_VE** ]==> (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`)
- (`e5` Điều 9 . Quy định chuyển tiếp `[DIEU]`) ==[ **THUOC_VE** ]==> (`e4` Chương IV `[CHUONG]`)


---

### Mẫu #02_2023_TT-BVHTTDL_159924#body_context_73 (Loại: `body_context`)
> **[Bộ Văn hóa , Thể thao và Du lịch]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[02/2023/TT-BVHTTDL]`<SO_HIEU>`** . **[Điều 9]`<DIEU>`** . **[1 . **[Viên chức]`<CHU_THE_CA_NHAN>`** đã được bổ nhiệm vào các ngạch **[viên chức]`<CHU_THE_CA_NHAN>`** tuyên truyền viên **[theo quy định tại]`<TU_KHOA_PHAP_LY>`** **[Quyết định số 428/TCCP-VC]`<THAM_CHIEU_PHAP_LY>`** **[ngày 02 tháng 6 năm 1993]`<NGAY_THAM_CHIEU>`** của Bộ trưởng - Trưởng ban Ban Tổ chức - **[Cán bộ]`<CHU_THE_CA_NHAN>`** **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** ( nay là **[Bộ trưởng Bộ Nội vụ]`<CO_QUAN_THAM_QUYEN>`** ) ban hành tiêu chuẩn nghiệp vụ ngạch **[công chức]`<CHU_THE_CA_NHAN>`** ngành Văn hóa - Thông tin ( sau đây viết tắt là **[Quyết định số 428/TCCP-VC]`<THAM_CHIEU_PHAP_LY>`** ) , **[Quyết định số 78/2004/QĐ-BNV]`<THAM_CHIEU_PHAP_LY>`** **[ngày 03 tháng 11 năm 2004]`<NGAY_THAM_CHIEU>`** của **[Bộ trưởng Bộ Nội vụ]`<CO_QUAN_THAM_QUYEN>`** ban hành]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[7:8]`)
- `[e1]` **02/2023/TT-BVHTTDL** → `SO_HIEU` (span: `[9:10]`)
- `[e2]` **Bộ Văn hóa , Thể thao và Du lịch** → `CO_QUAN_BAN_HANH` (span: `[0:6]`)
- `[e3]` **Điều 9** → `DIEU` (span: `[11:13]`)
- `[e4]` **1 . Viên chức đã được bổ nhiệm vào các ngạch viên chức tuyên truyền viên theo quy định tại Quyết định số 428/TCCP-VC ngày 02 tháng 6 năm 1993 của Bộ trưởng - Trưởng ban Ban Tổ chức - Cán bộ Chính phủ ( nay là Bộ trưởng Bộ Nội vụ ) ban hành tiêu chuẩn nghiệp vụ ngạch công chức ngành Văn hóa - Thông tin ( sau đây viết tắt là Quyết định số 428/TCCP-VC ) , Quyết định số 78/2004/QĐ-BNV ngày 03 tháng 11 năm 2004 của Bộ trưởng Bộ Nội vụ ban hành** → `KHOAN` (span: `[14:88]`)
- `[e5]` **Quyết định số 428/TCCP-VC** → `THAM_CHIEU_PHAP_LY` (span: `[28:31]`) *(lồng trong `e4` (`KHOAN`))*
- `[e6]` **Quyết định số 428/TCCP-VC** → `THAM_CHIEU_PHAP_LY` (span: `[69:72]`) *(lồng trong `e4` (`KHOAN`))*
- `[e7]` **Quyết định số 78/2004/QĐ-BNV** → `THAM_CHIEU_PHAP_LY` (span: `[74:77]`) *(lồng trong `e4` (`KHOAN`))*
- `[e8]` **theo quy định tại** → `TU_KHOA_PHAP_LY` (span: `[25:28]`) *(lồng trong `e4` (`KHOAN`))*
- `[e9]` **ngày 02 tháng 6 năm 1993** → `NGAY_THAM_CHIEU` (span: `[31:37]`) *(lồng trong `e4` (`KHOAN`))*
- `[e10]` **ngày 03 tháng 11 năm 2004** → `NGAY_THAM_CHIEU` (span: `[77:83]`) *(lồng trong `e4` (`KHOAN`))*
- `[e11]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[46:47]`) *(lồng trong `e4` (`KHOAN`))*
- `[e12]` **Bộ trưởng Bộ Nội vụ** → `CO_QUAN_THAM_QUYEN` (span: `[50:53]`) *(lồng trong `e4` (`KHOAN`))*
- `[e13]` **Bộ trưởng Bộ Nội vụ** → `CO_QUAN_THAM_QUYEN` (span: `[84:87]`) *(lồng trong `e4` (`KHOAN`))*
- `[e14]` **Viên chức** → `CHU_THE_CA_NHAN` (span: `[16:17]`) *(lồng trong `e4` (`KHOAN`))*
- `[e15]` **viên chức** → `CHU_THE_CA_NHAN` (span: `[23:24]`) *(lồng trong `e4` (`KHOAN`))*
- `[e16]` **Cán bộ** → `CHU_THE_CA_NHAN` (span: `[45:46]`) *(lồng trong `e4` (`KHOAN`))*
- `[e17]` **công chức** → `CHU_THE_CA_NHAN` (span: `[58:59]`) *(lồng trong `e4` (`KHOAN`))*

**Quan hệ:**
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Văn hóa , Thể thao và Du lịch `[CO_QUAN_BAN_HANH]`)
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 9 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`)
- (`e4` 1 . Viên chức đã được bổ nhiệm vào các ngạch viên chức tuyên truyền viên theo quy định tại Quyết định số 428/TCCP-VC ngày 02 tháng 6 năm 1993 của Bộ trưởng - Trưởng ban Ban Tổ chức - Cán bộ Chính phủ ( nay là Bộ trưởng Bộ Nội vụ ) ban hành tiêu chuẩn nghiệp vụ ngạch công chức ngành Văn hóa - Thông tin ( sau đây viết tắt là Quyết định số 428/TCCP-VC ) , Quyết định số 78/2004/QĐ-BNV ngày 03 tháng 11 năm 2004 của Bộ trưởng Bộ Nội vụ ban hành `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 9 `[DIEU]`)
- (`e8` theo quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e5` Quyết định số 428/TCCP-VC `[THAM_CHIEU_PHAP_LY]`)
- (`e4` 1 . Viên chức đã được bổ nhiệm vào các ngạch viên chức tuyên truyền viên theo quy định tại Quyết định số 428/TCCP-VC ngày 02 tháng 6 năm 1993 của Bộ trưởng - Trưởng ban Ban Tổ chức - Cán bộ Chính phủ ( nay là Bộ trưởng Bộ Nội vụ ) ban hành tiêu chuẩn nghiệp vụ ngạch công chức ngành Văn hóa - Thông tin ( sau đây viết tắt là Quyết định số 428/TCCP-VC ) , Quyết định số 78/2004/QĐ-BNV ngày 03 tháng 11 năm 2004 của Bộ trưởng Bộ Nội vụ ban hành `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e5` Quyết định số 428/TCCP-VC `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e8` theo quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e6` Quyết định số 428/TCCP-VC `[THAM_CHIEU_PHAP_LY]`)
- (`e4` 1 . Viên chức đã được bổ nhiệm vào các ngạch viên chức tuyên truyền viên theo quy định tại Quyết định số 428/TCCP-VC ngày 02 tháng 6 năm 1993 của Bộ trưởng - Trưởng ban Ban Tổ chức - Cán bộ Chính phủ ( nay là Bộ trưởng Bộ Nội vụ ) ban hành tiêu chuẩn nghiệp vụ ngạch công chức ngành Văn hóa - Thông tin ( sau đây viết tắt là Quyết định số 428/TCCP-VC ) , Quyết định số 78/2004/QĐ-BNV ngày 03 tháng 11 năm 2004 của Bộ trưởng Bộ Nội vụ ban hành `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e6` Quyết định số 428/TCCP-VC `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e8` theo quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e7` Quyết định số 78/2004/QĐ-BNV `[THAM_CHIEU_PHAP_LY]`)
- (`e4` 1 . Viên chức đã được bổ nhiệm vào các ngạch viên chức tuyên truyền viên theo quy định tại Quyết định số 428/TCCP-VC ngày 02 tháng 6 năm 1993 của Bộ trưởng - Trưởng ban Ban Tổ chức - Cán bộ Chính phủ ( nay là Bộ trưởng Bộ Nội vụ ) ban hành tiêu chuẩn nghiệp vụ ngạch công chức ngành Văn hóa - Thông tin ( sau đây viết tắt là Quyết định số 428/TCCP-VC ) , Quyết định số 78/2004/QĐ-BNV ngày 03 tháng 11 năm 2004 của Bộ trưởng Bộ Nội vụ ban hành `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e7` Quyết định số 78/2004/QĐ-BNV `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e5` Quyết định số 428/TCCP-VC `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e9` ngày 02 tháng 6 năm 1993 `[NGAY_THAM_CHIEU]`)
- (`e7` Quyết định số 78/2004/QĐ-BNV `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e10` ngày 03 tháng 11 năm 2004 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #02_2023_TT-BVHTTDL_159924#body_standalone_74 (Loại: `body_standalone`)
> **[Điều 9]`<DIEU>`** . **[1 . **[Viên chức]`<CHU_THE_CA_NHAN>`** đã được bổ nhiệm vào các ngạch **[viên chức]`<CHU_THE_CA_NHAN>`** tuyên truyền viên **[theo quy định tại]`<TU_KHOA_PHAP_LY>`** **[Quyết định số 428/TCCP-VC]`<THAM_CHIEU_PHAP_LY>`** **[ngày 02 tháng 6 năm 1993]`<NGAY_THAM_CHIEU>`** của Bộ trưởng - Trưởng ban Ban Tổ chức - **[Cán bộ]`<CHU_THE_CA_NHAN>`** **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** ( nay là **[Bộ trưởng Bộ Nội vụ]`<CO_QUAN_THAM_QUYEN>`** ) ban hành tiêu chuẩn nghiệp vụ ngạch **[công chức]`<CHU_THE_CA_NHAN>`** ngành Văn hóa - Thông tin ( sau đây viết tắt là **[Quyết định số 428/TCCP-VC]`<THAM_CHIEU_PHAP_LY>`** ) , **[Quyết định số 78/2004/QĐ-BNV]`<THAM_CHIEU_PHAP_LY>`** **[ngày 03 tháng 11 năm 2004]`<NGAY_THAM_CHIEU>`** của **[Bộ trưởng Bộ Nội vụ]`<CO_QUAN_THAM_QUYEN>`** ban hành]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 9** → `DIEU` (span: `[0:2]`)
- `[e1]` **1 . Viên chức đã được bổ nhiệm vào các ngạch viên chức tuyên truyền viên theo quy định tại Quyết định số 428/TCCP-VC ngày 02 tháng 6 năm 1993 của Bộ trưởng - Trưởng ban Ban Tổ chức - Cán bộ Chính phủ ( nay là Bộ trưởng Bộ Nội vụ ) ban hành tiêu chuẩn nghiệp vụ ngạch công chức ngành Văn hóa - Thông tin ( sau đây viết tắt là Quyết định số 428/TCCP-VC ) , Quyết định số 78/2004/QĐ-BNV ngày 03 tháng 11 năm 2004 của Bộ trưởng Bộ Nội vụ ban hành** → `KHOAN` (span: `[3:77]`)
- `[e2]` **Quyết định số 428/TCCP-VC** → `THAM_CHIEU_PHAP_LY` (span: `[17:20]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **Quyết định số 428/TCCP-VC** → `THAM_CHIEU_PHAP_LY` (span: `[58:61]`) *(lồng trong `e1` (`KHOAN`))*
- `[e4]` **Quyết định số 78/2004/QĐ-BNV** → `THAM_CHIEU_PHAP_LY` (span: `[63:66]`) *(lồng trong `e1` (`KHOAN`))*
- `[e5]` **theo quy định tại** → `TU_KHOA_PHAP_LY` (span: `[14:17]`) *(lồng trong `e1` (`KHOAN`))*
- `[e6]` **ngày 02 tháng 6 năm 1993** → `NGAY_THAM_CHIEU` (span: `[20:26]`) *(lồng trong `e1` (`KHOAN`))*
- `[e7]` **ngày 03 tháng 11 năm 2004** → `NGAY_THAM_CHIEU` (span: `[66:72]`) *(lồng trong `e1` (`KHOAN`))*
- `[e8]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[35:36]`) *(lồng trong `e1` (`KHOAN`))*
- `[e9]` **Bộ trưởng Bộ Nội vụ** → `CO_QUAN_THAM_QUYEN` (span: `[39:42]`) *(lồng trong `e1` (`KHOAN`))*
- `[e10]` **Bộ trưởng Bộ Nội vụ** → `CO_QUAN_THAM_QUYEN` (span: `[73:76]`) *(lồng trong `e1` (`KHOAN`))*
- `[e11]` **Viên chức** → `CHU_THE_CA_NHAN` (span: `[5:6]`) *(lồng trong `e1` (`KHOAN`))*
- `[e12]` **viên chức** → `CHU_THE_CA_NHAN` (span: `[12:13]`) *(lồng trong `e1` (`KHOAN`))*
- `[e13]` **Cán bộ** → `CHU_THE_CA_NHAN` (span: `[34:35]`) *(lồng trong `e1` (`KHOAN`))*
- `[e14]` **công chức** → `CHU_THE_CA_NHAN` (span: `[47:48]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 1 . Viên chức đã được bổ nhiệm vào các ngạch viên chức tuyên truyền viên theo quy định tại Quyết định số 428/TCCP-VC ngày 02 tháng 6 năm 1993 của Bộ trưởng - Trưởng ban Ban Tổ chức - Cán bộ Chính phủ ( nay là Bộ trưởng Bộ Nội vụ ) ban hành tiêu chuẩn nghiệp vụ ngạch công chức ngành Văn hóa - Thông tin ( sau đây viết tắt là Quyết định số 428/TCCP-VC ) , Quyết định số 78/2004/QĐ-BNV ngày 03 tháng 11 năm 2004 của Bộ trưởng Bộ Nội vụ ban hành `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 9 `[DIEU]`)
- (`e5` theo quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e2` Quyết định số 428/TCCP-VC `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 1 . Viên chức đã được bổ nhiệm vào các ngạch viên chức tuyên truyền viên theo quy định tại Quyết định số 428/TCCP-VC ngày 02 tháng 6 năm 1993 của Bộ trưởng - Trưởng ban Ban Tổ chức - Cán bộ Chính phủ ( nay là Bộ trưởng Bộ Nội vụ ) ban hành tiêu chuẩn nghiệp vụ ngạch công chức ngành Văn hóa - Thông tin ( sau đây viết tắt là Quyết định số 428/TCCP-VC ) , Quyết định số 78/2004/QĐ-BNV ngày 03 tháng 11 năm 2004 của Bộ trưởng Bộ Nội vụ ban hành `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e2` Quyết định số 428/TCCP-VC `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e5` theo quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Quyết định số 428/TCCP-VC `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 1 . Viên chức đã được bổ nhiệm vào các ngạch viên chức tuyên truyền viên theo quy định tại Quyết định số 428/TCCP-VC ngày 02 tháng 6 năm 1993 của Bộ trưởng - Trưởng ban Ban Tổ chức - Cán bộ Chính phủ ( nay là Bộ trưởng Bộ Nội vụ ) ban hành tiêu chuẩn nghiệp vụ ngạch công chức ngành Văn hóa - Thông tin ( sau đây viết tắt là Quyết định số 428/TCCP-VC ) , Quyết định số 78/2004/QĐ-BNV ngày 03 tháng 11 năm 2004 của Bộ trưởng Bộ Nội vụ ban hành `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Quyết định số 428/TCCP-VC `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e5` theo quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e4` Quyết định số 78/2004/QĐ-BNV `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 1 . Viên chức đã được bổ nhiệm vào các ngạch viên chức tuyên truyền viên theo quy định tại Quyết định số 428/TCCP-VC ngày 02 tháng 6 năm 1993 của Bộ trưởng - Trưởng ban Ban Tổ chức - Cán bộ Chính phủ ( nay là Bộ trưởng Bộ Nội vụ ) ban hành tiêu chuẩn nghiệp vụ ngạch công chức ngành Văn hóa - Thông tin ( sau đây viết tắt là Quyết định số 428/TCCP-VC ) , Quyết định số 78/2004/QĐ-BNV ngày 03 tháng 11 năm 2004 của Bộ trưởng Bộ Nội vụ ban hành `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e4` Quyết định số 78/2004/QĐ-BNV `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e2` Quyết định số 428/TCCP-VC `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e6` ngày 02 tháng 6 năm 1993 `[NGAY_THAM_CHIEU]`)
- (`e4` Quyết định số 78/2004/QĐ-BNV `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e7` ngày 03 tháng 11 năm 2004 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #02_2023_TT-BVHTTDL_159924#body_context_75 (Loại: `body_context`)
> **[Bộ Văn hóa , Thể thao và Du lịch]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[02/2023/TT-BVHTTDL]`<SO_HIEU>`** . **[Điều 9]`<DIEU>`** . **[2 . Việc chuyển xếp lương vào chức danh nghề nghiệp **[viên chức]`<CHU_THE_CA_NHAN>`** **[quy định tại]`<TU_KHOA_PHAP_LY>`** **[khoản 1 Điều này]`<THAM_CHIEU_PHAP_LY>`** đối với **[viên chức]`<CHU_THE_CA_NHAN>`** đã được xếp lương vào các ngạch **[viên chức]`<CHU_THE_CA_NHAN>`** tuyên truyền viên **[theo quy định tại]`<TU_KHOA_PHAP_LY>`** **[Quyết định số 428/TCCP-VC]`<THAM_CHIEU_PHAP_LY>`** , **[Quyết định số 78/2004/QĐ-BNV]`<THAM_CHIEU_PHAP_LY>`** và **[Nghị định số 204/2004/NĐ-CP]`<THAM_CHIEU_PHAP_LY>`** được thực hiện theo hướng dẫn tại **[Thông tư số 02/2007/TT-BNV]`<THAM_CHIEU_PHAP_LY>`** như sau :]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[7:8]`)
- `[e1]` **02/2023/TT-BVHTTDL** → `SO_HIEU` (span: `[9:10]`)
- `[e2]` **Bộ Văn hóa , Thể thao và Du lịch** → `CO_QUAN_BAN_HANH` (span: `[0:6]`)
- `[e3]` **Điều 9** → `DIEU` (span: `[11:13]`)
- `[e4]` **2 . Việc chuyển xếp lương vào chức danh nghề nghiệp viên chức quy định tại khoản 1 Điều này đối với viên chức đã được xếp lương vào các ngạch viên chức tuyên truyền viên theo quy định tại Quyết định số 428/TCCP-VC , Quyết định số 78/2004/QĐ-BNV và Nghị định số 204/2004/NĐ-CP được thực hiện theo hướng dẫn tại Thông tư số 02/2007/TT-BNV như sau :** → `KHOAN` (span: `[14:66]`)
- `[e5]` **khoản 1 Điều này** → `THAM_CHIEU_PHAP_LY` (span: `[26:30]`) *(lồng trong `e4` (`KHOAN`))*
- `[e6]` **Quyết định số 428/TCCP-VC** → `THAM_CHIEU_PHAP_LY` (span: `[44:47]`) *(lồng trong `e4` (`KHOAN`))*
- `[e7]` **Quyết định số 78/2004/QĐ-BNV** → `THAM_CHIEU_PHAP_LY` (span: `[48:51]`) *(lồng trong `e4` (`KHOAN`))*
- `[e8]` **Nghị định số 204/2004/NĐ-CP** → `THAM_CHIEU_PHAP_LY` (span: `[52:55]`) *(lồng trong `e4` (`KHOAN`))*
- `[e9]` **Thông tư số 02/2007/TT-BNV** → `THAM_CHIEU_PHAP_LY` (span: `[60:63]`) *(lồng trong `e4` (`KHOAN`))*
- `[e10]` **quy định tại** → `TU_KHOA_PHAP_LY` (span: `[24:26]`) *(lồng trong `e4` (`KHOAN`))*
- `[e11]` **theo quy định tại** → `TU_KHOA_PHAP_LY` (span: `[41:44]`) *(lồng trong `e4` (`KHOAN`))*
- `[e12]` **viên chức** → `CHU_THE_CA_NHAN` (span: `[23:24]`) *(lồng trong `e4` (`KHOAN`))*
- `[e13]` **viên chức** → `CHU_THE_CA_NHAN` (span: `[31:32]`) *(lồng trong `e4` (`KHOAN`))*
- `[e14]` **viên chức** → `CHU_THE_CA_NHAN` (span: `[39:40]`) *(lồng trong `e4` (`KHOAN`))*

**Quan hệ:**
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Văn hóa , Thể thao và Du lịch `[CO_QUAN_BAN_HANH]`)
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 9 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`)
- (`e4` 2 . Việc chuyển xếp lương vào chức danh nghề nghiệp viên chức quy định tại khoản 1 Điều này đối với viên chức đã được xếp lương vào các ngạch viên chức tuyên truyền viên theo quy định tại Quyết định số 428/TCCP-VC , Quyết định số 78/2004/QĐ-BNV và Nghị định số 204/2004/NĐ-CP được thực hiện theo hướng dẫn tại Thông tư số 02/2007/TT-BNV như sau : `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 9 `[DIEU]`)
- (`e10` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e5` khoản 1 Điều này `[THAM_CHIEU_PHAP_LY]`)
- (`e4` 2 . Việc chuyển xếp lương vào chức danh nghề nghiệp viên chức quy định tại khoản 1 Điều này đối với viên chức đã được xếp lương vào các ngạch viên chức tuyên truyền viên theo quy định tại Quyết định số 428/TCCP-VC , Quyết định số 78/2004/QĐ-BNV và Nghị định số 204/2004/NĐ-CP được thực hiện theo hướng dẫn tại Thông tư số 02/2007/TT-BNV như sau : `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e5` khoản 1 Điều này `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e11` theo quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e6` Quyết định số 428/TCCP-VC `[THAM_CHIEU_PHAP_LY]`)
- (`e4` 2 . Việc chuyển xếp lương vào chức danh nghề nghiệp viên chức quy định tại khoản 1 Điều này đối với viên chức đã được xếp lương vào các ngạch viên chức tuyên truyền viên theo quy định tại Quyết định số 428/TCCP-VC , Quyết định số 78/2004/QĐ-BNV và Nghị định số 204/2004/NĐ-CP được thực hiện theo hướng dẫn tại Thông tư số 02/2007/TT-BNV như sau : `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e6` Quyết định số 428/TCCP-VC `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e11` theo quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e7` Quyết định số 78/2004/QĐ-BNV `[THAM_CHIEU_PHAP_LY]`)
- (`e4` 2 . Việc chuyển xếp lương vào chức danh nghề nghiệp viên chức quy định tại khoản 1 Điều này đối với viên chức đã được xếp lương vào các ngạch viên chức tuyên truyền viên theo quy định tại Quyết định số 428/TCCP-VC , Quyết định số 78/2004/QĐ-BNV và Nghị định số 204/2004/NĐ-CP được thực hiện theo hướng dẫn tại Thông tư số 02/2007/TT-BNV như sau : `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e7` Quyết định số 78/2004/QĐ-BNV `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e11` theo quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e8` Nghị định số 204/2004/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e4` 2 . Việc chuyển xếp lương vào chức danh nghề nghiệp viên chức quy định tại khoản 1 Điều này đối với viên chức đã được xếp lương vào các ngạch viên chức tuyên truyền viên theo quy định tại Quyết định số 428/TCCP-VC , Quyết định số 78/2004/QĐ-BNV và Nghị định số 204/2004/NĐ-CP được thực hiện theo hướng dẫn tại Thông tư số 02/2007/TT-BNV như sau : `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e8` Nghị định số 204/2004/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e11` theo quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e9` Thông tư số 02/2007/TT-BNV `[THAM_CHIEU_PHAP_LY]`)
- (`e4` 2 . Việc chuyển xếp lương vào chức danh nghề nghiệp viên chức quy định tại khoản 1 Điều này đối với viên chức đã được xếp lương vào các ngạch viên chức tuyên truyền viên theo quy định tại Quyết định số 428/TCCP-VC , Quyết định số 78/2004/QĐ-BNV và Nghị định số 204/2004/NĐ-CP được thực hiện theo hướng dẫn tại Thông tư số 02/2007/TT-BNV như sau : `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e9` Thông tư số 02/2007/TT-BNV `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #02_2023_TT-BVHTTDL_159924#body_standalone_76 (Loại: `body_standalone`)
> **[Điều 9]`<DIEU>`** . **[2 . Việc chuyển xếp lương vào chức danh nghề nghiệp **[viên chức]`<CHU_THE_CA_NHAN>`** **[quy định tại]`<TU_KHOA_PHAP_LY>`** **[khoản 1 Điều này]`<THAM_CHIEU_PHAP_LY>`** đối với **[viên chức]`<CHU_THE_CA_NHAN>`** đã được xếp lương vào các ngạch **[viên chức]`<CHU_THE_CA_NHAN>`** tuyên truyền viên **[theo quy định tại]`<TU_KHOA_PHAP_LY>`** **[Quyết định số 428/TCCP-VC]`<THAM_CHIEU_PHAP_LY>`** , **[Quyết định số 78/2004/QĐ-BNV]`<THAM_CHIEU_PHAP_LY>`** và **[Nghị định số 204/2004/NĐ-CP]`<THAM_CHIEU_PHAP_LY>`** được thực hiện theo hướng dẫn tại **[Thông tư số 02/2007/TT-BNV]`<THAM_CHIEU_PHAP_LY>`** như sau :]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 9** → `DIEU` (span: `[0:2]`)
- `[e1]` **2 . Việc chuyển xếp lương vào chức danh nghề nghiệp viên chức quy định tại khoản 1 Điều này đối với viên chức đã được xếp lương vào các ngạch viên chức tuyên truyền viên theo quy định tại Quyết định số 428/TCCP-VC , Quyết định số 78/2004/QĐ-BNV và Nghị định số 204/2004/NĐ-CP được thực hiện theo hướng dẫn tại Thông tư số 02/2007/TT-BNV như sau :** → `KHOAN` (span: `[3:55]`)
- `[e2]` **khoản 1 Điều này** → `THAM_CHIEU_PHAP_LY` (span: `[15:19]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **Quyết định số 428/TCCP-VC** → `THAM_CHIEU_PHAP_LY` (span: `[33:36]`) *(lồng trong `e1` (`KHOAN`))*
- `[e4]` **Quyết định số 78/2004/QĐ-BNV** → `THAM_CHIEU_PHAP_LY` (span: `[37:40]`) *(lồng trong `e1` (`KHOAN`))*
- `[e5]` **Nghị định số 204/2004/NĐ-CP** → `THAM_CHIEU_PHAP_LY` (span: `[41:44]`) *(lồng trong `e1` (`KHOAN`))*
- `[e6]` **Thông tư số 02/2007/TT-BNV** → `THAM_CHIEU_PHAP_LY` (span: `[49:52]`) *(lồng trong `e1` (`KHOAN`))*
- `[e7]` **quy định tại** → `TU_KHOA_PHAP_LY` (span: `[13:15]`) *(lồng trong `e1` (`KHOAN`))*
- `[e8]` **theo quy định tại** → `TU_KHOA_PHAP_LY` (span: `[30:33]`) *(lồng trong `e1` (`KHOAN`))*
- `[e9]` **viên chức** → `CHU_THE_CA_NHAN` (span: `[12:13]`) *(lồng trong `e1` (`KHOAN`))*
- `[e10]` **viên chức** → `CHU_THE_CA_NHAN` (span: `[20:21]`) *(lồng trong `e1` (`KHOAN`))*
- `[e11]` **viên chức** → `CHU_THE_CA_NHAN` (span: `[28:29]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 2 . Việc chuyển xếp lương vào chức danh nghề nghiệp viên chức quy định tại khoản 1 Điều này đối với viên chức đã được xếp lương vào các ngạch viên chức tuyên truyền viên theo quy định tại Quyết định số 428/TCCP-VC , Quyết định số 78/2004/QĐ-BNV và Nghị định số 204/2004/NĐ-CP được thực hiện theo hướng dẫn tại Thông tư số 02/2007/TT-BNV như sau : `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 9 `[DIEU]`)
- (`e7` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e2` khoản 1 Điều này `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 2 . Việc chuyển xếp lương vào chức danh nghề nghiệp viên chức quy định tại khoản 1 Điều này đối với viên chức đã được xếp lương vào các ngạch viên chức tuyên truyền viên theo quy định tại Quyết định số 428/TCCP-VC , Quyết định số 78/2004/QĐ-BNV và Nghị định số 204/2004/NĐ-CP được thực hiện theo hướng dẫn tại Thông tư số 02/2007/TT-BNV như sau : `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e2` khoản 1 Điều này `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e8` theo quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Quyết định số 428/TCCP-VC `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 2 . Việc chuyển xếp lương vào chức danh nghề nghiệp viên chức quy định tại khoản 1 Điều này đối với viên chức đã được xếp lương vào các ngạch viên chức tuyên truyền viên theo quy định tại Quyết định số 428/TCCP-VC , Quyết định số 78/2004/QĐ-BNV và Nghị định số 204/2004/NĐ-CP được thực hiện theo hướng dẫn tại Thông tư số 02/2007/TT-BNV như sau : `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Quyết định số 428/TCCP-VC `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e8` theo quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e4` Quyết định số 78/2004/QĐ-BNV `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 2 . Việc chuyển xếp lương vào chức danh nghề nghiệp viên chức quy định tại khoản 1 Điều này đối với viên chức đã được xếp lương vào các ngạch viên chức tuyên truyền viên theo quy định tại Quyết định số 428/TCCP-VC , Quyết định số 78/2004/QĐ-BNV và Nghị định số 204/2004/NĐ-CP được thực hiện theo hướng dẫn tại Thông tư số 02/2007/TT-BNV như sau : `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e4` Quyết định số 78/2004/QĐ-BNV `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e8` theo quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e5` Nghị định số 204/2004/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 2 . Việc chuyển xếp lương vào chức danh nghề nghiệp viên chức quy định tại khoản 1 Điều này đối với viên chức đã được xếp lương vào các ngạch viên chức tuyên truyền viên theo quy định tại Quyết định số 428/TCCP-VC , Quyết định số 78/2004/QĐ-BNV và Nghị định số 204/2004/NĐ-CP được thực hiện theo hướng dẫn tại Thông tư số 02/2007/TT-BNV như sau : `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e5` Nghị định số 204/2004/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e8` theo quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e6` Thông tư số 02/2007/TT-BNV `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 2 . Việc chuyển xếp lương vào chức danh nghề nghiệp viên chức quy định tại khoản 1 Điều này đối với viên chức đã được xếp lương vào các ngạch viên chức tuyên truyền viên theo quy định tại Quyết định số 428/TCCP-VC , Quyết định số 78/2004/QĐ-BNV và Nghị định số 204/2004/NĐ-CP được thực hiện theo hướng dẫn tại Thông tư số 02/2007/TT-BNV như sau : `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e6` Thông tư số 02/2007/TT-BNV `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #02_2023_TT-BVHTTDL_159924#body_context_77 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[02/2023/TT-BVHTTDL]`<SO_HIEU>`** của **[Bộ Văn hóa , Thể thao và Du lịch]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Lao động - Thương binh và Xã hội]`<LINH_VUC>`** . **[Điều 9]`<DIEU>`** . **[Khoản 2]`<KHOAN>`** . **[b ) Trường hợp **[viên chức]`<CHU_THE_CA_NHAN>`** có trình độ cao đẳng khi tuyển dụng đã được xếp lương **[viên chức]`<CHU_THE_CA_NHAN>`** loại A0 **[theo quy định tại]`<TU_KHOA_PHAP_LY>`** **[Nghị định số 204/2004/NĐ]`<THAM_CHIEU_PHAP_LY>`** - CP nay được bổ nhiệm vào chức danh nghề nghiệp tuyên truyền viên văn hóa trung cấp thì việc xếp bậc lương căn cứ vào thời gian công tác có đóng bảo hiểm xã hội bắt buộc theo thang lương , bảng lương do Nhà nước quy định ( trừ thời gian tập sự ) như sau : Tính từ bậc 2 bảng lương]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **02/2023/TT-BVHTTDL** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Văn hóa , Thể thao và Du lịch** → `CO_QUAN_BAN_HANH` (span: `[4:10]`)
- `[e3]` **Lao động - Thương binh và Xã hội** → `LINH_VUC` (span: `[12:17]`)
- `[e4]` **Điều 9** → `DIEU` (span: `[18:20]`)
- `[e5]` **Khoản 2** → `KHOAN` (span: `[21:23]`)
- `[e6]` **b ) Trường hợp viên chức có trình độ cao đẳng khi tuyển dụng đã được xếp lương viên chức loại A0 theo quy định tại Nghị định số 204/2004/NĐ - CP nay được bổ nhiệm vào chức danh nghề nghiệp tuyên truyền viên văn hóa trung cấp thì việc xếp bậc lương căn cứ vào thời gian công tác có đóng bảo hiểm xã hội bắt buộc theo thang lương , bảng lương do Nhà nước quy định ( trừ thời gian tập sự ) như sau : Tính từ bậc 2 bảng lương** → `DIEM` (span: `[24:93]`)
- `[e7]` **Nghị định số 204/2004/NĐ** → `THAM_CHIEU_PHAP_LY` (span: `[43:46]`) *(lồng trong `e6` (`DIEM`))*
- `[e8]` **theo quy định tại** → `TU_KHOA_PHAP_LY` (span: `[40:43]`) *(lồng trong `e6` (`DIEM`))*
- `[e9]` **viên chức** → `CHU_THE_CA_NHAN` (span: `[27:28]`) *(lồng trong `e6` (`DIEM`))*
- `[e10]` **viên chức** → `CHU_THE_CA_NHAN` (span: `[37:38]`) *(lồng trong `e6` (`DIEM`))*

**Quan hệ:**
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Văn hóa , Thể thao và Du lịch `[CO_QUAN_BAN_HANH]`)
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Lao động - Thương binh và Xã hội `[LINH_VUC]`)
- (`e4` Điều 9 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`)
- (`e5` Khoản 2 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 9 `[DIEU]`)
- (`e6` b ) Trường hợp viên chức có trình độ cao đẳng khi tuyển dụng đã được xếp lương viên chức loại A0 theo quy định tại Nghị định số 204/2004/NĐ - CP nay được bổ nhiệm vào chức danh nghề nghiệp tuyên truyền viên văn hóa trung cấp thì việc xếp bậc lương căn cứ vào thời gian công tác có đóng bảo hiểm xã hội bắt buộc theo thang lương , bảng lương do Nhà nước quy định ( trừ thời gian tập sự ) như sau : Tính từ bậc 2 bảng lương `[DIEM]`) ==[ **THUOC_VE** ]==> (`e5` Khoản 2 `[KHOAN]`)
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Lao động - Thương binh và Xã hội `[LINH_VUC]`)
- (`e6` b ) Trường hợp viên chức có trình độ cao đẳng khi tuyển dụng đã được xếp lương viên chức loại A0 theo quy định tại Nghị định số 204/2004/NĐ - CP nay được bổ nhiệm vào chức danh nghề nghiệp tuyên truyền viên văn hóa trung cấp thì việc xếp bậc lương căn cứ vào thời gian công tác có đóng bảo hiểm xã hội bắt buộc theo thang lương , bảng lương do Nhà nước quy định ( trừ thời gian tập sự ) như sau : Tính từ bậc 2 bảng lương `[DIEM]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Lao động - Thương binh và Xã hội `[LINH_VUC]`)
- (`e8` theo quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e7` Nghị định số 204/2004/NĐ `[THAM_CHIEU_PHAP_LY]`)
- (`e6` b ) Trường hợp viên chức có trình độ cao đẳng khi tuyển dụng đã được xếp lương viên chức loại A0 theo quy định tại Nghị định số 204/2004/NĐ - CP nay được bổ nhiệm vào chức danh nghề nghiệp tuyên truyền viên văn hóa trung cấp thì việc xếp bậc lương căn cứ vào thời gian công tác có đóng bảo hiểm xã hội bắt buộc theo thang lương , bảng lương do Nhà nước quy định ( trừ thời gian tập sự ) như sau : Tính từ bậc 2 bảng lương `[DIEM]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e7` Nghị định số 204/2004/NĐ `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #02_2023_TT-BVHTTDL_159924#body_standalone_78 (Loại: `body_standalone`)
> **[Điều 9]`<DIEU>`** . **[Khoản 2]`<KHOAN>`** . **[b ) Trường hợp **[viên chức]`<CHU_THE_CA_NHAN>`** có trình độ cao đẳng khi tuyển dụng đã được xếp lương **[viên chức]`<CHU_THE_CA_NHAN>`** loại A0 **[theo quy định tại]`<TU_KHOA_PHAP_LY>`** **[Nghị định số 204/2004/NĐ]`<THAM_CHIEU_PHAP_LY>`** - CP nay được bổ nhiệm vào chức danh nghề nghiệp tuyên truyền viên văn hóa trung cấp thì việc xếp bậc lương căn cứ vào thời gian công tác có đóng bảo hiểm xã hội bắt buộc theo thang lương , bảng lương do Nhà nước quy định ( trừ thời gian tập sự ) như sau : Tính từ bậc 2 bảng lương]`<DIEM>`**

**Thực thể:**
- `[e0]` **Điều 9** → `DIEU` (span: `[0:2]`)
- `[e1]` **Khoản 2** → `KHOAN` (span: `[3:5]`)
- `[e2]` **b ) Trường hợp viên chức có trình độ cao đẳng khi tuyển dụng đã được xếp lương viên chức loại A0 theo quy định tại Nghị định số 204/2004/NĐ - CP nay được bổ nhiệm vào chức danh nghề nghiệp tuyên truyền viên văn hóa trung cấp thì việc xếp bậc lương căn cứ vào thời gian công tác có đóng bảo hiểm xã hội bắt buộc theo thang lương , bảng lương do Nhà nước quy định ( trừ thời gian tập sự ) như sau : Tính từ bậc 2 bảng lương** → `DIEM` (span: `[6:75]`)
- `[e3]` **Nghị định số 204/2004/NĐ** → `THAM_CHIEU_PHAP_LY` (span: `[25:28]`) *(lồng trong `e2` (`DIEM`))*
- `[e4]` **theo quy định tại** → `TU_KHOA_PHAP_LY` (span: `[22:25]`) *(lồng trong `e2` (`DIEM`))*
- `[e5]` **viên chức** → `CHU_THE_CA_NHAN` (span: `[9:10]`) *(lồng trong `e2` (`DIEM`))*
- `[e6]` **viên chức** → `CHU_THE_CA_NHAN` (span: `[19:20]`) *(lồng trong `e2` (`DIEM`))*

**Quan hệ:**
- (`e1` Khoản 2 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 9 `[DIEU]`)
- (`e2` b ) Trường hợp viên chức có trình độ cao đẳng khi tuyển dụng đã được xếp lương viên chức loại A0 theo quy định tại Nghị định số 204/2004/NĐ - CP nay được bổ nhiệm vào chức danh nghề nghiệp tuyên truyền viên văn hóa trung cấp thì việc xếp bậc lương căn cứ vào thời gian công tác có đóng bảo hiểm xã hội bắt buộc theo thang lương , bảng lương do Nhà nước quy định ( trừ thời gian tập sự ) như sau : Tính từ bậc 2 bảng lương `[DIEM]`) ==[ **THUOC_VE** ]==> (`e1` Khoản 2 `[KHOAN]`)
- (`e4` theo quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Nghị định số 204/2004/NĐ `[THAM_CHIEU_PHAP_LY]`)
- (`e2` b ) Trường hợp viên chức có trình độ cao đẳng khi tuyển dụng đã được xếp lương viên chức loại A0 theo quy định tại Nghị định số 204/2004/NĐ - CP nay được bổ nhiệm vào chức danh nghề nghiệp tuyên truyền viên văn hóa trung cấp thì việc xếp bậc lương căn cứ vào thời gian công tác có đóng bảo hiểm xã hội bắt buộc theo thang lương , bảng lương do Nhà nước quy định ( trừ thời gian tập sự ) như sau : Tính từ bậc 2 bảng lương `[DIEM]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Nghị định số 204/2004/NĐ `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #02_2023_TT-BVHTTDL_159924#body_context_79 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[02/2023/TT-BVHTTDL]`<SO_HIEU>`** ban hành **[ngày 21 tháng 02 năm 2023]`<NGAY_BAN_HANH>`** bởi **[Bộ Văn hóa , Thể thao và Du lịch]`<CO_QUAN_BAN_HANH>`** . **[Điều 9]`<DIEU>`** . **[Khoản 2]`<KHOAN>`** . **[b ) Trường hợp **[viên chức]`<CHU_THE_CA_NHAN>`** có trình độ cao đẳng khi tuyển dụng đã được xếp lương **[viên chức]`<CHU_THE_CA_NHAN>`** loại A0 **[theo quy định tại]`<TU_KHOA_PHAP_LY>`** **[Nghị định số 204/2004/NĐ]`<THAM_CHIEU_PHAP_LY>`** - CP nay được bổ nhiệm vào chức danh nghề nghiệp tuyên truyền viên văn hóa trung cấp thì việc xếp bậc lương căn cứ vào thời gian công tác có đóng bảo hiểm xã hội bắt buộc theo thang lương , bảng lương do Nhà nước quy định ( trừ thời gian tập sự ) như sau : Sau khi chuyển xếp lương vào]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **02/2023/TT-BVHTTDL** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Văn hóa , Thể thao và Du lịch** → `CO_QUAN_BAN_HANH` (span: `[11:17]`)
- `[e3]` **ngày 21 tháng 02 năm 2023** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 9** → `DIEU` (span: `[18:20]`)
- `[e5]` **Khoản 2** → `KHOAN` (span: `[21:23]`)
- `[e6]` **b ) Trường hợp viên chức có trình độ cao đẳng khi tuyển dụng đã được xếp lương viên chức loại A0 theo quy định tại Nghị định số 204/2004/NĐ - CP nay được bổ nhiệm vào chức danh nghề nghiệp tuyên truyền viên văn hóa trung cấp thì việc xếp bậc lương căn cứ vào thời gian công tác có đóng bảo hiểm xã hội bắt buộc theo thang lương , bảng lương do Nhà nước quy định ( trừ thời gian tập sự ) như sau : Sau khi chuyển xếp lương vào** → `DIEM` (span: `[24:94]`)
- `[e7]` **Nghị định số 204/2004/NĐ** → `THAM_CHIEU_PHAP_LY` (span: `[43:46]`) *(lồng trong `e6` (`DIEM`))*
- `[e8]` **theo quy định tại** → `TU_KHOA_PHAP_LY` (span: `[40:43]`) *(lồng trong `e6` (`DIEM`))*
- `[e9]` **viên chức** → `CHU_THE_CA_NHAN` (span: `[27:28]`) *(lồng trong `e6` (`DIEM`))*
- `[e10]` **viên chức** → `CHU_THE_CA_NHAN` (span: `[37:38]`) *(lồng trong `e6` (`DIEM`))*

**Quan hệ:**
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Văn hóa , Thể thao và Du lịch `[CO_QUAN_BAN_HANH]`)
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 21 tháng 02 năm 2023 `[NGAY_BAN_HANH]`)
- (`e4` Điều 9 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`)
- (`e5` Khoản 2 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 9 `[DIEU]`)
- (`e6` b ) Trường hợp viên chức có trình độ cao đẳng khi tuyển dụng đã được xếp lương viên chức loại A0 theo quy định tại Nghị định số 204/2004/NĐ - CP nay được bổ nhiệm vào chức danh nghề nghiệp tuyên truyền viên văn hóa trung cấp thì việc xếp bậc lương căn cứ vào thời gian công tác có đóng bảo hiểm xã hội bắt buộc theo thang lương , bảng lương do Nhà nước quy định ( trừ thời gian tập sự ) như sau : Sau khi chuyển xếp lương vào `[DIEM]`) ==[ **THUOC_VE** ]==> (`e5` Khoản 2 `[KHOAN]`)
- (`e8` theo quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e7` Nghị định số 204/2004/NĐ `[THAM_CHIEU_PHAP_LY]`)
- (`e6` b ) Trường hợp viên chức có trình độ cao đẳng khi tuyển dụng đã được xếp lương viên chức loại A0 theo quy định tại Nghị định số 204/2004/NĐ - CP nay được bổ nhiệm vào chức danh nghề nghiệp tuyên truyền viên văn hóa trung cấp thì việc xếp bậc lương căn cứ vào thời gian công tác có đóng bảo hiểm xã hội bắt buộc theo thang lương , bảng lương do Nhà nước quy định ( trừ thời gian tập sự ) như sau : Sau khi chuyển xếp lương vào `[DIEM]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e7` Nghị định số 204/2004/NĐ `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #02_2023_TT-BVHTTDL_159924#body_standalone_80 (Loại: `body_standalone`)
> **[Điều 9]`<DIEU>`** . **[Khoản 2]`<KHOAN>`** . **[b ) Trường hợp **[viên chức]`<CHU_THE_CA_NHAN>`** có trình độ cao đẳng khi tuyển dụng đã được xếp lương **[viên chức]`<CHU_THE_CA_NHAN>`** loại A0 **[theo quy định tại]`<TU_KHOA_PHAP_LY>`** **[Nghị định số 204/2004/NĐ]`<THAM_CHIEU_PHAP_LY>`** - CP nay được bổ nhiệm vào chức danh nghề nghiệp tuyên truyền viên văn hóa trung cấp thì việc xếp bậc lương căn cứ vào thời gian công tác có đóng bảo hiểm xã hội bắt buộc theo thang lương , bảng lương do Nhà nước quy định ( trừ thời gian tập sự ) như sau : Sau khi chuyển xếp lương vào]`<DIEM>`**

**Thực thể:**
- `[e0]` **Điều 9** → `DIEU` (span: `[0:2]`)
- `[e1]` **Khoản 2** → `KHOAN` (span: `[3:5]`)
- `[e2]` **b ) Trường hợp viên chức có trình độ cao đẳng khi tuyển dụng đã được xếp lương viên chức loại A0 theo quy định tại Nghị định số 204/2004/NĐ - CP nay được bổ nhiệm vào chức danh nghề nghiệp tuyên truyền viên văn hóa trung cấp thì việc xếp bậc lương căn cứ vào thời gian công tác có đóng bảo hiểm xã hội bắt buộc theo thang lương , bảng lương do Nhà nước quy định ( trừ thời gian tập sự ) như sau : Sau khi chuyển xếp lương vào** → `DIEM` (span: `[6:76]`)
- `[e3]` **Nghị định số 204/2004/NĐ** → `THAM_CHIEU_PHAP_LY` (span: `[25:28]`) *(lồng trong `e2` (`DIEM`))*
- `[e4]` **theo quy định tại** → `TU_KHOA_PHAP_LY` (span: `[22:25]`) *(lồng trong `e2` (`DIEM`))*
- `[e5]` **viên chức** → `CHU_THE_CA_NHAN` (span: `[9:10]`) *(lồng trong `e2` (`DIEM`))*
- `[e6]` **viên chức** → `CHU_THE_CA_NHAN` (span: `[19:20]`) *(lồng trong `e2` (`DIEM`))*

**Quan hệ:**
- (`e1` Khoản 2 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 9 `[DIEU]`)
- (`e2` b ) Trường hợp viên chức có trình độ cao đẳng khi tuyển dụng đã được xếp lương viên chức loại A0 theo quy định tại Nghị định số 204/2004/NĐ - CP nay được bổ nhiệm vào chức danh nghề nghiệp tuyên truyền viên văn hóa trung cấp thì việc xếp bậc lương căn cứ vào thời gian công tác có đóng bảo hiểm xã hội bắt buộc theo thang lương , bảng lương do Nhà nước quy định ( trừ thời gian tập sự ) như sau : Sau khi chuyển xếp lương vào `[DIEM]`) ==[ **THUOC_VE** ]==> (`e1` Khoản 2 `[KHOAN]`)
- (`e4` theo quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Nghị định số 204/2004/NĐ `[THAM_CHIEU_PHAP_LY]`)
- (`e2` b ) Trường hợp viên chức có trình độ cao đẳng khi tuyển dụng đã được xếp lương viên chức loại A0 theo quy định tại Nghị định số 204/2004/NĐ - CP nay được bổ nhiệm vào chức danh nghề nghiệp tuyên truyền viên văn hóa trung cấp thì việc xếp bậc lương căn cứ vào thời gian công tác có đóng bảo hiểm xã hội bắt buộc theo thang lương , bảng lương do Nhà nước quy định ( trừ thời gian tập sự ) như sau : Sau khi chuyển xếp lương vào `[DIEM]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Nghị định số 204/2004/NĐ `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #02_2023_TT-BVHTTDL_159924#body_context_81 (Loại: `body_context`)
> **[Bộ Văn hóa , Thể thao và Du lịch]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[02/2023/TT-BVHTTDL]`<SO_HIEU>`** . **[Điều 9]`<DIEU>`** . **[3 . **[Viên chức]`<CHU_THE_CA_NHAN>`** đã được bổ nhiệm vào các ngạch tuyên truyền viên theo quy định của pháp luật từ trước ngày Thông tư này có hiệu lực thi hành thì được xác định là đáp ứng quy định về tiêu chuẩn chức danh nghề nghiệp **[viên chức]`<CHU_THE_CA_NHAN>`** chuyên ngành tuyên truyền viên văn hóa **[quy định tại]`<TU_KHOA_PHAP_LY>`** **[Thông tư này]`<THAM_CHIEU_PHAP_LY>`** tương ứng với chức danh nghề nghiệp đã được bổ nhiệm .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[7:8]`)
- `[e1]` **02/2023/TT-BVHTTDL** → `SO_HIEU` (span: `[9:10]`)
- `[e2]` **Bộ Văn hóa , Thể thao và Du lịch** → `CO_QUAN_BAN_HANH` (span: `[0:6]`)
- `[e3]` **Điều 9** → `DIEU` (span: `[11:13]`)
- `[e4]` **3 . Viên chức đã được bổ nhiệm vào các ngạch tuyên truyền viên theo quy định của pháp luật từ trước ngày Thông tư này có hiệu lực thi hành thì được xác định là đáp ứng quy định về tiêu chuẩn chức danh nghề nghiệp viên chức chuyên ngành tuyên truyền viên văn hóa quy định tại Thông tư này tương ứng với chức danh nghề nghiệp đã được bổ nhiệm .** → `KHOAN` (span: `[14:62]`)
- `[e5]` **Thông tư này** → `THAM_CHIEU_PHAP_LY` (span: `[52:54]`) *(lồng trong `e4` (`KHOAN`))*
- `[e6]` **quy định tại** → `TU_KHOA_PHAP_LY` (span: `[50:52]`) *(lồng trong `e4` (`KHOAN`))*
- `[e7]` **Viên chức** → `CHU_THE_CA_NHAN` (span: `[16:17]`) *(lồng trong `e4` (`KHOAN`))*
- `[e8]` **viên chức** → `CHU_THE_CA_NHAN` (span: `[46:47]`) *(lồng trong `e4` (`KHOAN`))*

**Quan hệ:**
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Văn hóa , Thể thao và Du lịch `[CO_QUAN_BAN_HANH]`)
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 9 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`)
- (`e4` 3 . Viên chức đã được bổ nhiệm vào các ngạch tuyên truyền viên theo quy định của pháp luật từ trước ngày Thông tư này có hiệu lực thi hành thì được xác định là đáp ứng quy định về tiêu chuẩn chức danh nghề nghiệp viên chức chuyên ngành tuyên truyền viên văn hóa quy định tại Thông tư này tương ứng với chức danh nghề nghiệp đã được bổ nhiệm . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 9 `[DIEU]`)
- (`e6` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e5` Thông tư này `[THAM_CHIEU_PHAP_LY]`)
- (`e4` 3 . Viên chức đã được bổ nhiệm vào các ngạch tuyên truyền viên theo quy định của pháp luật từ trước ngày Thông tư này có hiệu lực thi hành thì được xác định là đáp ứng quy định về tiêu chuẩn chức danh nghề nghiệp viên chức chuyên ngành tuyên truyền viên văn hóa quy định tại Thông tư này tương ứng với chức danh nghề nghiệp đã được bổ nhiệm . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e5` Thông tư này `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #02_2023_TT-BVHTTDL_159924#body_standalone_82 (Loại: `body_standalone`)
> **[Điều 9]`<DIEU>`** . **[3 . **[Viên chức]`<CHU_THE_CA_NHAN>`** đã được bổ nhiệm vào các ngạch tuyên truyền viên theo quy định của pháp luật từ trước ngày Thông tư này có hiệu lực thi hành thì được xác định là đáp ứng quy định về tiêu chuẩn chức danh nghề nghiệp **[viên chức]`<CHU_THE_CA_NHAN>`** chuyên ngành tuyên truyền viên văn hóa **[quy định tại]`<TU_KHOA_PHAP_LY>`** **[Thông tư này]`<THAM_CHIEU_PHAP_LY>`** tương ứng với chức danh nghề nghiệp đã được bổ nhiệm .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 9** → `DIEU` (span: `[0:2]`)
- `[e1]` **3 . Viên chức đã được bổ nhiệm vào các ngạch tuyên truyền viên theo quy định của pháp luật từ trước ngày Thông tư này có hiệu lực thi hành thì được xác định là đáp ứng quy định về tiêu chuẩn chức danh nghề nghiệp viên chức chuyên ngành tuyên truyền viên văn hóa quy định tại Thông tư này tương ứng với chức danh nghề nghiệp đã được bổ nhiệm .** → `KHOAN` (span: `[3:51]`)
- `[e2]` **Thông tư này** → `THAM_CHIEU_PHAP_LY` (span: `[41:43]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **quy định tại** → `TU_KHOA_PHAP_LY` (span: `[39:41]`) *(lồng trong `e1` (`KHOAN`))*
- `[e4]` **Viên chức** → `CHU_THE_CA_NHAN` (span: `[5:6]`) *(lồng trong `e1` (`KHOAN`))*
- `[e5]` **viên chức** → `CHU_THE_CA_NHAN` (span: `[35:36]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 3 . Viên chức đã được bổ nhiệm vào các ngạch tuyên truyền viên theo quy định của pháp luật từ trước ngày Thông tư này có hiệu lực thi hành thì được xác định là đáp ứng quy định về tiêu chuẩn chức danh nghề nghiệp viên chức chuyên ngành tuyên truyền viên văn hóa quy định tại Thông tư này tương ứng với chức danh nghề nghiệp đã được bổ nhiệm . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 9 `[DIEU]`)
- (`e3` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e2` Thông tư này `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 3 . Viên chức đã được bổ nhiệm vào các ngạch tuyên truyền viên theo quy định của pháp luật từ trước ngày Thông tư này có hiệu lực thi hành thì được xác định là đáp ứng quy định về tiêu chuẩn chức danh nghề nghiệp viên chức chuyên ngành tuyên truyền viên văn hóa quy định tại Thông tư này tương ứng với chức danh nghề nghiệp đã được bổ nhiệm . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e2` Thông tư này `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #02_2023_TT-BVHTTDL_159924#body_context_83 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[02/2023/TT-BVHTTDL]`<SO_HIEU>`** ban hành **[ngày 21 tháng 02 năm 2023]`<NGAY_BAN_HANH>`** bởi **[Bộ Văn hóa , Thể thao và Du lịch]`<CO_QUAN_BAN_HANH>`** . **[Chương IV]`<CHUONG>`** . **[Điều 10 . Tổ chức thực hiện]`<DIEU>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **02/2023/TT-BVHTTDL** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Văn hóa , Thể thao và Du lịch** → `CO_QUAN_BAN_HANH` (span: `[11:17]`)
- `[e3]` **ngày 21 tháng 02 năm 2023** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Chương IV** → `CHUONG` (span: `[18:20]`)
- `[e5]` **Điều 10 . Tổ chức thực hiện** → `DIEU` (span: `[21:26]`)

**Quan hệ:**
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Văn hóa , Thể thao và Du lịch `[CO_QUAN_BAN_HANH]`)
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 21 tháng 02 năm 2023 `[NGAY_BAN_HANH]`)
- (`e4` Chương IV `[CHUONG]`) ==[ **THUOC_VE** ]==> (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`)
- (`e5` Điều 10 . Tổ chức thực hiện `[DIEU]`) ==[ **THUOC_VE** ]==> (`e4` Chương IV `[CHUONG]`)


---

### Mẫu #02_2023_TT-BVHTTDL_159924#body_context_84 (Loại: `body_context`)
> **[Bộ Văn hóa , Thể thao và Du lịch]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[02/2023/TT-BVHTTDL]`<SO_HIEU>`** . **[Điều 10]`<DIEU>`** . **[1 . Thông tư này là căn cứ để thực hiện việc tuyển dụng , sử dụng và quản lý **[viên chức]`<CHU_THE_CA_NHAN>`** chuyên ngành tuyên truyền viên văn hóa làm việc trong các **[đơn vị sự nghiệp công lập]`<TO_CHUC_DOANH_NGHIEP>`** .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[7:8]`)
- `[e1]` **02/2023/TT-BVHTTDL** → `SO_HIEU` (span: `[9:10]`)
- `[e2]` **Bộ Văn hóa , Thể thao và Du lịch** → `CO_QUAN_BAN_HANH` (span: `[0:6]`)
- `[e3]` **Điều 10** → `DIEU` (span: `[11:13]`)
- `[e4]` **1 . Thông tư này là căn cứ để thực hiện việc tuyển dụng , sử dụng và quản lý viên chức chuyên ngành tuyên truyền viên văn hóa làm việc trong các đơn vị sự nghiệp công lập .** → `KHOAN` (span: `[14:39]`)
- `[e5]` **đơn vị sự nghiệp công lập** → `TO_CHUC_DOANH_NGHIEP` (span: `[35:38]`) *(lồng trong `e4` (`KHOAN`))*
- `[e6]` **viên chức** → `CHU_THE_CA_NHAN` (span: `[28:29]`) *(lồng trong `e4` (`KHOAN`))*

**Quan hệ:**
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Văn hóa , Thể thao và Du lịch `[CO_QUAN_BAN_HANH]`)
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 10 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`)
- (`e4` 1 . Thông tư này là căn cứ để thực hiện việc tuyển dụng , sử dụng và quản lý viên chức chuyên ngành tuyên truyền viên văn hóa làm việc trong các đơn vị sự nghiệp công lập . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 10 `[DIEU]`)


---

### Mẫu #02_2023_TT-BVHTTDL_159924#body_standalone_85 (Loại: `body_standalone`)
> **[Điều 10]`<DIEU>`** . **[1 . Thông tư này là căn cứ để thực hiện việc tuyển dụng , sử dụng và quản lý **[viên chức]`<CHU_THE_CA_NHAN>`** chuyên ngành tuyên truyền viên văn hóa làm việc trong các **[đơn vị sự nghiệp công lập]`<TO_CHUC_DOANH_NGHIEP>`** .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 10** → `DIEU` (span: `[0:2]`)
- `[e1]` **1 . Thông tư này là căn cứ để thực hiện việc tuyển dụng , sử dụng và quản lý viên chức chuyên ngành tuyên truyền viên văn hóa làm việc trong các đơn vị sự nghiệp công lập .** → `KHOAN` (span: `[3:28]`)
- `[e2]` **đơn vị sự nghiệp công lập** → `TO_CHUC_DOANH_NGHIEP` (span: `[24:27]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **viên chức** → `CHU_THE_CA_NHAN` (span: `[17:18]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 1 . Thông tư này là căn cứ để thực hiện việc tuyển dụng , sử dụng và quản lý viên chức chuyên ngành tuyên truyền viên văn hóa làm việc trong các đơn vị sự nghiệp công lập . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 10 `[DIEU]`)


---

### Mẫu #02_2023_TT-BVHTTDL_159924#body_context_86 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[02/2023/TT-BVHTTDL]`<SO_HIEU>`** của **[Bộ Văn hóa , Thể thao và Du lịch]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Lao động - Thương binh và Xã hội]`<LINH_VUC>`** . **[Điều 10]`<DIEU>`** . **[2 . Người đứng đầu các **[đơn vị sự nghiệp công lập]`<TO_CHUC_DOANH_NGHIEP>`** trực tiếp quản lý và sử dụng **[viên chức]`<CHU_THE_CA_NHAN>`** có trách nhiệm :]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **02/2023/TT-BVHTTDL** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Văn hóa , Thể thao và Du lịch** → `CO_QUAN_BAN_HANH` (span: `[4:10]`)
- `[e3]` **Lao động - Thương binh và Xã hội** → `LINH_VUC` (span: `[12:17]`)
- `[e4]` **Điều 10** → `DIEU` (span: `[18:20]`)
- `[e5]` **2 . Người đứng đầu các đơn vị sự nghiệp công lập trực tiếp quản lý và sử dụng viên chức có trách nhiệm :** → `KHOAN` (span: `[21:37]`)
- `[e6]` **đơn vị sự nghiệp công lập** → `TO_CHUC_DOANH_NGHIEP` (span: `[27:30]`) *(lồng trong `e5` (`KHOAN`))*
- `[e7]` **viên chức** → `CHU_THE_CA_NHAN` (span: `[33:34]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Văn hóa , Thể thao và Du lịch `[CO_QUAN_BAN_HANH]`)
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Lao động - Thương binh và Xã hội `[LINH_VUC]`)
- (`e4` Điều 10 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`)
- (`e5` 2 . Người đứng đầu các đơn vị sự nghiệp công lập trực tiếp quản lý và sử dụng viên chức có trách nhiệm : `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 10 `[DIEU]`)
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Lao động - Thương binh và Xã hội `[LINH_VUC]`)
- (`e5` 2 . Người đứng đầu các đơn vị sự nghiệp công lập trực tiếp quản lý và sử dụng viên chức có trách nhiệm : `[KHOAN]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Lao động - Thương binh và Xã hội `[LINH_VUC]`)


---

### Mẫu #02_2023_TT-BVHTTDL_159924#body_standalone_87 (Loại: `body_standalone`)
> **[Điều 10]`<DIEU>`** . **[2 . Người đứng đầu các **[đơn vị sự nghiệp công lập]`<TO_CHUC_DOANH_NGHIEP>`** trực tiếp quản lý và sử dụng **[viên chức]`<CHU_THE_CA_NHAN>`** có trách nhiệm :]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 10** → `DIEU` (span: `[0:2]`)
- `[e1]` **2 . Người đứng đầu các đơn vị sự nghiệp công lập trực tiếp quản lý và sử dụng viên chức có trách nhiệm :** → `KHOAN` (span: `[3:19]`)
- `[e2]` **đơn vị sự nghiệp công lập** → `TO_CHUC_DOANH_NGHIEP` (span: `[9:12]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **viên chức** → `CHU_THE_CA_NHAN` (span: `[15:16]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 2 . Người đứng đầu các đơn vị sự nghiệp công lập trực tiếp quản lý và sử dụng viên chức có trách nhiệm : `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 10 `[DIEU]`)


---

### Mẫu #02_2023_TT-BVHTTDL_159924#body_context_88 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[02/2023/TT-BVHTTDL]`<SO_HIEU>`** của **[Bộ Văn hóa , Thể thao và Du lịch]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Lao động - Thương binh và Xã hội]`<LINH_VUC>`** . **[Điều 10]`<DIEU>`** . **[Khoản 2]`<KHOAN>`** . **[a ) Rà soát vị trí việc làm của đơn vị , lập phương án bổ nhiệm chức danh nghề nghiệp **[viên chức]`<CHU_THE_CA_NHAN>`** chuyên ngành tuyên truyền viên văn hóa thuộc thẩm quyền quản lý , trình **[cấp có thẩm quyền]`<CO_QUAN_THAM_QUYEN>`** xem xét , quyết định hoặc quyết định theo thẩm quyền phân cấp ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **02/2023/TT-BVHTTDL** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Văn hóa , Thể thao và Du lịch** → `CO_QUAN_BAN_HANH` (span: `[4:10]`)
- `[e3]` **Lao động - Thương binh và Xã hội** → `LINH_VUC` (span: `[12:17]`)
- `[e4]` **Điều 10** → `DIEU` (span: `[18:20]`)
- `[e5]` **Khoản 2** → `KHOAN` (span: `[21:23]`)
- `[e6]` **a ) Rà soát vị trí việc làm của đơn vị , lập phương án bổ nhiệm chức danh nghề nghiệp viên chức chuyên ngành tuyên truyền viên văn hóa thuộc thẩm quyền quản lý , trình cấp có thẩm quyền xem xét , quyết định hoặc quyết định theo thẩm quyền phân cấp ;** → `DIEM` (span: `[24:58]`)
- `[e7]` **cấp có thẩm quyền** → `CO_QUAN_THAM_QUYEN` (span: `[46:49]`) *(lồng trong `e6` (`DIEM`))*
- `[e8]` **viên chức** → `CHU_THE_CA_NHAN` (span: `[37:38]`) *(lồng trong `e6` (`DIEM`))*

**Quan hệ:**
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Văn hóa , Thể thao và Du lịch `[CO_QUAN_BAN_HANH]`)
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Lao động - Thương binh và Xã hội `[LINH_VUC]`)
- (`e4` Điều 10 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`)
- (`e5` Khoản 2 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 10 `[DIEU]`)
- (`e6` a ) Rà soát vị trí việc làm của đơn vị , lập phương án bổ nhiệm chức danh nghề nghiệp viên chức chuyên ngành tuyên truyền viên văn hóa thuộc thẩm quyền quản lý , trình cấp có thẩm quyền xem xét , quyết định hoặc quyết định theo thẩm quyền phân cấp ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e5` Khoản 2 `[KHOAN]`)
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Lao động - Thương binh và Xã hội `[LINH_VUC]`)
- (`e6` a ) Rà soát vị trí việc làm của đơn vị , lập phương án bổ nhiệm chức danh nghề nghiệp viên chức chuyên ngành tuyên truyền viên văn hóa thuộc thẩm quyền quản lý , trình cấp có thẩm quyền xem xét , quyết định hoặc quyết định theo thẩm quyền phân cấp ; `[DIEM]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Lao động - Thương binh và Xã hội `[LINH_VUC]`)


---

### Mẫu #02_2023_TT-BVHTTDL_159924#body_standalone_89 (Loại: `body_standalone`)
> **[Điều 10]`<DIEU>`** . **[Khoản 2]`<KHOAN>`** . **[a ) Rà soát vị trí việc làm của đơn vị , lập phương án bổ nhiệm chức danh nghề nghiệp **[viên chức]`<CHU_THE_CA_NHAN>`** chuyên ngành tuyên truyền viên văn hóa thuộc thẩm quyền quản lý , trình **[cấp có thẩm quyền]`<CO_QUAN_THAM_QUYEN>`** xem xét , quyết định hoặc quyết định theo thẩm quyền phân cấp ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Điều 10** → `DIEU` (span: `[0:2]`)
- `[e1]` **Khoản 2** → `KHOAN` (span: `[3:5]`)
- `[e2]` **a ) Rà soát vị trí việc làm của đơn vị , lập phương án bổ nhiệm chức danh nghề nghiệp viên chức chuyên ngành tuyên truyền viên văn hóa thuộc thẩm quyền quản lý , trình cấp có thẩm quyền xem xét , quyết định hoặc quyết định theo thẩm quyền phân cấp ;** → `DIEM` (span: `[6:40]`)
- `[e3]` **cấp có thẩm quyền** → `CO_QUAN_THAM_QUYEN` (span: `[28:31]`) *(lồng trong `e2` (`DIEM`))*
- `[e4]` **viên chức** → `CHU_THE_CA_NHAN` (span: `[19:20]`) *(lồng trong `e2` (`DIEM`))*

**Quan hệ:**
- (`e1` Khoản 2 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 10 `[DIEU]`)
- (`e2` a ) Rà soát vị trí việc làm của đơn vị , lập phương án bổ nhiệm chức danh nghề nghiệp viên chức chuyên ngành tuyên truyền viên văn hóa thuộc thẩm quyền quản lý , trình cấp có thẩm quyền xem xét , quyết định hoặc quyết định theo thẩm quyền phân cấp ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e1` Khoản 2 `[KHOAN]`)


---

### Mẫu #02_2023_TT-BVHTTDL_159924#body_context_90 (Loại: `body_context`)
> **[Bộ Văn hóa , Thể thao và Du lịch]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[02/2023/TT-BVHTTDL]`<SO_HIEU>`** . **[Điều 10]`<DIEU>`** . **[Khoản 2]`<KHOAN>`** . **[b ) **[Quyết định bổ nhiệm]`<GIAY_TO_HO_SO>`** chức danh nghề nghiệp chuyên ngành tuyên truyền viên văn hóa trong các **[đơn vị sự nghiệp công lập]`<TO_CHUC_DOANH_NGHIEP>`** theo thẩm quyền hoặc theo phân cấp , ủy quyền sau khi phương án bổ nhiệm chức danh nghề nghiệp được **[cấp có thẩm quyền]`<CO_QUAN_THAM_QUYEN>`** phê duyệt .]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[7:8]`)
- `[e1]` **02/2023/TT-BVHTTDL** → `SO_HIEU` (span: `[9:10]`)
- `[e2]` **Bộ Văn hóa , Thể thao và Du lịch** → `CO_QUAN_BAN_HANH` (span: `[0:6]`)
- `[e3]` **Điều 10** → `DIEU` (span: `[11:13]`)
- `[e4]` **Khoản 2** → `KHOAN` (span: `[14:16]`)
- `[e5]` **b ) Quyết định bổ nhiệm chức danh nghề nghiệp chuyên ngành tuyên truyền viên văn hóa trong các đơn vị sự nghiệp công lập theo thẩm quyền hoặc theo phân cấp , ủy quyền sau khi phương án bổ nhiệm chức danh nghề nghiệp được cấp có thẩm quyền phê duyệt .** → `DIEM` (span: `[17:51]`)
- `[e6]` **cấp có thẩm quyền** → `CO_QUAN_THAM_QUYEN` (span: `[46:49]`) *(lồng trong `e5` (`DIEM`))*
- `[e7]` **Quyết định bổ nhiệm** → `GIAY_TO_HO_SO` (span: `[19:21]`) *(lồng trong `e5` (`DIEM`))*
- `[e8]` **đơn vị sự nghiệp công lập** → `TO_CHUC_DOANH_NGHIEP` (span: `[28:31]`) *(lồng trong `e5` (`DIEM`))*

**Quan hệ:**
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Văn hóa , Thể thao và Du lịch `[CO_QUAN_BAN_HANH]`)
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 10 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`)
- (`e4` Khoản 2 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 10 `[DIEU]`)
- (`e5` b ) Quyết định bổ nhiệm chức danh nghề nghiệp chuyên ngành tuyên truyền viên văn hóa trong các đơn vị sự nghiệp công lập theo thẩm quyền hoặc theo phân cấp , ủy quyền sau khi phương án bổ nhiệm chức danh nghề nghiệp được cấp có thẩm quyền phê duyệt . `[DIEM]`) ==[ **THUOC_VE** ]==> (`e4` Khoản 2 `[KHOAN]`)


---

### Mẫu #02_2023_TT-BVHTTDL_159924#body_standalone_91 (Loại: `body_standalone`)
> **[Điều 10]`<DIEU>`** . **[Khoản 2]`<KHOAN>`** . **[b ) **[Quyết định bổ nhiệm]`<GIAY_TO_HO_SO>`** chức danh nghề nghiệp chuyên ngành tuyên truyền viên văn hóa trong các **[đơn vị sự nghiệp công lập]`<TO_CHUC_DOANH_NGHIEP>`** theo thẩm quyền hoặc theo phân cấp , ủy quyền sau khi phương án bổ nhiệm chức danh nghề nghiệp được **[cấp có thẩm quyền]`<CO_QUAN_THAM_QUYEN>`** phê duyệt .]`<DIEM>`**

**Thực thể:**
- `[e0]` **Điều 10** → `DIEU` (span: `[0:2]`)
- `[e1]` **Khoản 2** → `KHOAN` (span: `[3:5]`)
- `[e2]` **b ) Quyết định bổ nhiệm chức danh nghề nghiệp chuyên ngành tuyên truyền viên văn hóa trong các đơn vị sự nghiệp công lập theo thẩm quyền hoặc theo phân cấp , ủy quyền sau khi phương án bổ nhiệm chức danh nghề nghiệp được cấp có thẩm quyền phê duyệt .** → `DIEM` (span: `[6:40]`)
- `[e3]` **cấp có thẩm quyền** → `CO_QUAN_THAM_QUYEN` (span: `[35:38]`) *(lồng trong `e2` (`DIEM`))*
- `[e4]` **Quyết định bổ nhiệm** → `GIAY_TO_HO_SO` (span: `[8:10]`) *(lồng trong `e2` (`DIEM`))*
- `[e5]` **đơn vị sự nghiệp công lập** → `TO_CHUC_DOANH_NGHIEP` (span: `[17:20]`) *(lồng trong `e2` (`DIEM`))*

**Quan hệ:**
- (`e1` Khoản 2 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 10 `[DIEU]`)
- (`e2` b ) Quyết định bổ nhiệm chức danh nghề nghiệp chuyên ngành tuyên truyền viên văn hóa trong các đơn vị sự nghiệp công lập theo thẩm quyền hoặc theo phân cấp , ủy quyền sau khi phương án bổ nhiệm chức danh nghề nghiệp được cấp có thẩm quyền phê duyệt . `[DIEM]`) ==[ **THUOC_VE** ]==> (`e1` Khoản 2 `[KHOAN]`)


---

### Mẫu #02_2023_TT-BVHTTDL_159924#body_context_92 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[02/2023/TT-BVHTTDL]`<SO_HIEU>`** ban hành **[ngày 21 tháng 02 năm 2023]`<NGAY_BAN_HANH>`** bởi **[Bộ Văn hóa , Thể thao và Du lịch]`<CO_QUAN_BAN_HANH>`** . **[Điều 10]`<DIEU>`** . **[3 . Các Bộ , cơ quan ngang Bộ , cơ quan thuộc **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** , **[Ủy ban nhân dân tỉnh , thành phố trực thuộc trung ương]`<CO_QUAN_THAM_QUYEN>`** có trách nhiệm :]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **02/2023/TT-BVHTTDL** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Văn hóa , Thể thao và Du lịch** → `CO_QUAN_BAN_HANH` (span: `[11:17]`)
- `[e3]` **ngày 21 tháng 02 năm 2023** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 10** → `DIEU` (span: `[18:20]`)
- `[e5]` **3 . Các Bộ , cơ quan ngang Bộ , cơ quan thuộc Chính phủ , Ủy ban nhân dân tỉnh , thành phố trực thuộc trung ương có trách nhiệm :** → `KHOAN` (span: `[21:44]`)
- `[e6]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[32:33]`) *(lồng trong `e5` (`KHOAN`))*
- `[e7]` **Ủy ban nhân dân tỉnh , thành phố trực thuộc trung ương** → `CO_QUAN_THAM_QUYEN` (span: `[34:41]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Văn hóa , Thể thao và Du lịch `[CO_QUAN_BAN_HANH]`)
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 21 tháng 02 năm 2023 `[NGAY_BAN_HANH]`)
- (`e4` Điều 10 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`)
- (`e5` 3 . Các Bộ , cơ quan ngang Bộ , cơ quan thuộc Chính phủ , Ủy ban nhân dân tỉnh , thành phố trực thuộc trung ương có trách nhiệm : `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 10 `[DIEU]`)


---

### Mẫu #02_2023_TT-BVHTTDL_159924#body_standalone_93 (Loại: `body_standalone`)
> **[Điều 10]`<DIEU>`** . **[3 . Các Bộ , cơ quan ngang Bộ , cơ quan thuộc **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** , **[Ủy ban nhân dân tỉnh , thành phố trực thuộc trung ương]`<CO_QUAN_THAM_QUYEN>`** có trách nhiệm :]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 10** → `DIEU` (span: `[0:2]`)
- `[e1]` **3 . Các Bộ , cơ quan ngang Bộ , cơ quan thuộc Chính phủ , Ủy ban nhân dân tỉnh , thành phố trực thuộc trung ương có trách nhiệm :** → `KHOAN` (span: `[3:26]`)
- `[e2]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[14:15]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **Ủy ban nhân dân tỉnh , thành phố trực thuộc trung ương** → `CO_QUAN_THAM_QUYEN` (span: `[16:23]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 3 . Các Bộ , cơ quan ngang Bộ , cơ quan thuộc Chính phủ , Ủy ban nhân dân tỉnh , thành phố trực thuộc trung ương có trách nhiệm : `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 10 `[DIEU]`)


---

### Mẫu #02_2023_TT-BVHTTDL_159924#body_context_94 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[02/2023/TT-BVHTTDL]`<SO_HIEU>`** của **[Bộ Văn hóa , Thể thao và Du lịch]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Lao động - Thương binh và Xã hội]`<LINH_VUC>`** . **[Điều 10]`<DIEU>`** . **[4 . Các tổ chức , **[đơn vị sự nghiệp]`<TO_CHUC_DOANH_NGHIEP>`** ngoài công lập có thể áp dụng **[quy định tại]`<TU_KHOA_PHAP_LY>`** **[Thông tư này]`<THAM_CHIEU_PHAP_LY>`** để tuyển dụng , sử dụng và quản lý đội ngũ người làm việc về chuyên ngành tuyên truyền viên văn hóa .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **02/2023/TT-BVHTTDL** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Văn hóa , Thể thao và Du lịch** → `CO_QUAN_BAN_HANH` (span: `[4:10]`)
- `[e3]` **Lao động - Thương binh và Xã hội** → `LINH_VUC` (span: `[12:17]`)
- `[e4]` **Điều 10** → `DIEU` (span: `[18:20]`)
- `[e5]` **4 . Các tổ chức , đơn vị sự nghiệp ngoài công lập có thể áp dụng quy định tại Thông tư này để tuyển dụng , sử dụng và quản lý đội ngũ người làm việc về chuyên ngành tuyên truyền viên văn hóa .** → `KHOAN` (span: `[21:50]`)
- `[e6]` **Thông tư này** → `THAM_CHIEU_PHAP_LY` (span: `[34:36]`) *(lồng trong `e5` (`KHOAN`))*
- `[e7]` **quy định tại** → `TU_KHOA_PHAP_LY` (span: `[32:34]`) *(lồng trong `e5` (`KHOAN`))*
- `[e8]` **đơn vị sự nghiệp** → `TO_CHUC_DOANH_NGHIEP` (span: `[26:28]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Văn hóa , Thể thao và Du lịch `[CO_QUAN_BAN_HANH]`)
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Lao động - Thương binh và Xã hội `[LINH_VUC]`)
- (`e4` Điều 10 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`)
- (`e5` 4 . Các tổ chức , đơn vị sự nghiệp ngoài công lập có thể áp dụng quy định tại Thông tư này để tuyển dụng , sử dụng và quản lý đội ngũ người làm việc về chuyên ngành tuyên truyền viên văn hóa . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 10 `[DIEU]`)
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Lao động - Thương binh và Xã hội `[LINH_VUC]`)
- (`e5` 4 . Các tổ chức , đơn vị sự nghiệp ngoài công lập có thể áp dụng quy định tại Thông tư này để tuyển dụng , sử dụng và quản lý đội ngũ người làm việc về chuyên ngành tuyên truyền viên văn hóa . `[KHOAN]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Lao động - Thương binh và Xã hội `[LINH_VUC]`)
- (`e7` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e6` Thông tư này `[THAM_CHIEU_PHAP_LY]`)
- (`e5` 4 . Các tổ chức , đơn vị sự nghiệp ngoài công lập có thể áp dụng quy định tại Thông tư này để tuyển dụng , sử dụng và quản lý đội ngũ người làm việc về chuyên ngành tuyên truyền viên văn hóa . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e6` Thông tư này `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #02_2023_TT-BVHTTDL_159924#body_standalone_95 (Loại: `body_standalone`)
> **[Điều 10]`<DIEU>`** . **[4 . Các tổ chức , **[đơn vị sự nghiệp]`<TO_CHUC_DOANH_NGHIEP>`** ngoài công lập có thể áp dụng **[quy định tại]`<TU_KHOA_PHAP_LY>`** **[Thông tư này]`<THAM_CHIEU_PHAP_LY>`** để tuyển dụng , sử dụng và quản lý đội ngũ người làm việc về chuyên ngành tuyên truyền viên văn hóa .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 10** → `DIEU` (span: `[0:2]`)
- `[e1]` **4 . Các tổ chức , đơn vị sự nghiệp ngoài công lập có thể áp dụng quy định tại Thông tư này để tuyển dụng , sử dụng và quản lý đội ngũ người làm việc về chuyên ngành tuyên truyền viên văn hóa .** → `KHOAN` (span: `[3:32]`)
- `[e2]` **Thông tư này** → `THAM_CHIEU_PHAP_LY` (span: `[16:18]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **quy định tại** → `TU_KHOA_PHAP_LY` (span: `[14:16]`) *(lồng trong `e1` (`KHOAN`))*
- `[e4]` **đơn vị sự nghiệp** → `TO_CHUC_DOANH_NGHIEP` (span: `[8:10]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 4 . Các tổ chức , đơn vị sự nghiệp ngoài công lập có thể áp dụng quy định tại Thông tư này để tuyển dụng , sử dụng và quản lý đội ngũ người làm việc về chuyên ngành tuyên truyền viên văn hóa . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 10 `[DIEU]`)
- (`e3` quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e2` Thông tư này `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 4 . Các tổ chức , đơn vị sự nghiệp ngoài công lập có thể áp dụng quy định tại Thông tư này để tuyển dụng , sử dụng và quản lý đội ngũ người làm việc về chuyên ngành tuyên truyền viên văn hóa . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e2` Thông tư này `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #02_2023_TT-BVHTTDL_159924#body_context_96 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[02/2023/TT-BVHTTDL]`<SO_HIEU>`** ban hành **[ngày 21 tháng 02 năm 2023]`<NGAY_BAN_HANH>`** bởi **[Bộ Văn hóa , Thể thao và Du lịch]`<CO_QUAN_BAN_HANH>`** . **[Điều 11]`<DIEU>`** . **[1 . Thông tư này có hiệu lực thi hành kể từ ngày 10 tháng 4 năm 2023 .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **02/2023/TT-BVHTTDL** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Văn hóa , Thể thao và Du lịch** → `CO_QUAN_BAN_HANH` (span: `[11:17]`)
- `[e3]` **ngày 21 tháng 02 năm 2023** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 11** → `DIEU` (span: `[18:20]`)
- `[e5]` **1 . Thông tư này có hiệu lực thi hành kể từ ngày 10 tháng 4 năm 2023 .** → `KHOAN` (span: `[21:37]`)

**Quan hệ:**
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Văn hóa , Thể thao và Du lịch `[CO_QUAN_BAN_HANH]`)
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 21 tháng 02 năm 2023 `[NGAY_BAN_HANH]`)
- (`e4` Điều 11 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`)
- (`e5` 1 . Thông tư này có hiệu lực thi hành kể từ ngày 10 tháng 4 năm 2023 . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 11 `[DIEU]`)


---

### Mẫu #02_2023_TT-BVHTTDL_159924#body_context_97 (Loại: `body_context`)
> **[Bộ Văn hóa , Thể thao và Du lịch]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[02/2023/TT-BVHTTDL]`<SO_HIEU>`** . **[Điều 12]`<DIEU>`** . **[1 . Bộ trưởng , Thủ trưởng cơ quan ngang Bộ , Thủ trưởng cơ quan thuộc **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** , **[Chủ tịch Ủy ban nhân dân tỉnh , thành phố trực thuộc trung ương]`<CO_QUAN_THAM_QUYEN>`** và cơ quan , đơn vị , cá nhân có liên quan chịu trách nhiệm thi hành Thông tư này .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[7:8]`)
- `[e1]` **02/2023/TT-BVHTTDL** → `SO_HIEU` (span: `[9:10]`)
- `[e2]` **Bộ Văn hóa , Thể thao và Du lịch** → `CO_QUAN_BAN_HANH` (span: `[0:6]`)
- `[e3]` **Điều 12** → `DIEU` (span: `[11:13]`)
- `[e4]` **1 . Bộ trưởng , Thủ trưởng cơ quan ngang Bộ , Thủ trưởng cơ quan thuộc Chính phủ , Chủ tịch Ủy ban nhân dân tỉnh , thành phố trực thuộc trung ương và cơ quan , đơn vị , cá nhân có liên quan chịu trách nhiệm thi hành Thông tư này .** → `KHOAN` (span: `[14:50]`)
- `[e5]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[26:27]`) *(lồng trong `e4` (`KHOAN`))*
- `[e6]` **Chủ tịch Ủy ban nhân dân tỉnh , thành phố trực thuộc trung ương** → `CO_QUAN_THAM_QUYEN` (span: `[28:36]`) *(lồng trong `e4` (`KHOAN`))*

**Quan hệ:**
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Văn hóa , Thể thao và Du lịch `[CO_QUAN_BAN_HANH]`)
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 12 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`)
- (`e4` 1 . Bộ trưởng , Thủ trưởng cơ quan ngang Bộ , Thủ trưởng cơ quan thuộc Chính phủ , Chủ tịch Ủy ban nhân dân tỉnh , thành phố trực thuộc trung ương và cơ quan , đơn vị , cá nhân có liên quan chịu trách nhiệm thi hành Thông tư này . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 12 `[DIEU]`)


---

### Mẫu #02_2023_TT-BVHTTDL_159924#body_standalone_98 (Loại: `body_standalone`)
> **[Điều 12]`<DIEU>`** . **[1 . Bộ trưởng , Thủ trưởng cơ quan ngang Bộ , Thủ trưởng cơ quan thuộc **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** , **[Chủ tịch Ủy ban nhân dân tỉnh , thành phố trực thuộc trung ương]`<CO_QUAN_THAM_QUYEN>`** và cơ quan , đơn vị , cá nhân có liên quan chịu trách nhiệm thi hành Thông tư này .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 12** → `DIEU` (span: `[0:2]`)
- `[e1]` **1 . Bộ trưởng , Thủ trưởng cơ quan ngang Bộ , Thủ trưởng cơ quan thuộc Chính phủ , Chủ tịch Ủy ban nhân dân tỉnh , thành phố trực thuộc trung ương và cơ quan , đơn vị , cá nhân có liên quan chịu trách nhiệm thi hành Thông tư này .** → `KHOAN` (span: `[3:39]`)
- `[e2]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[15:16]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **Chủ tịch Ủy ban nhân dân tỉnh , thành phố trực thuộc trung ương** → `CO_QUAN_THAM_QUYEN` (span: `[17:25]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 1 . Bộ trưởng , Thủ trưởng cơ quan ngang Bộ , Thủ trưởng cơ quan thuộc Chính phủ , Chủ tịch Ủy ban nhân dân tỉnh , thành phố trực thuộc trung ương và cơ quan , đơn vị , cá nhân có liên quan chịu trách nhiệm thi hành Thông tư này . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 12 `[DIEU]`)


---

### Mẫu #02_2023_TT-BVHTTDL_159924#body_context_99 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[02/2023/TT-BVHTTDL]`<SO_HIEU>`** của **[Bộ Văn hóa , Thể thao và Du lịch]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Lao động - Thương binh và Xã hội]`<LINH_VUC>`** . **[Điều 4]`<DIEU>`** . **[1 . Nhiệm vụ :]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **02/2023/TT-BVHTTDL** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Văn hóa , Thể thao và Du lịch** → `CO_QUAN_BAN_HANH` (span: `[4:10]`)
- `[e3]` **Lao động - Thương binh và Xã hội** → `LINH_VUC` (span: `[12:17]`)
- `[e4]` **Điều 4** → `DIEU` (span: `[18:20]`)
- `[e5]` **1 . Nhiệm vụ :** → `KHOAN` (span: `[21:25]`)

**Quan hệ:**
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Văn hóa , Thể thao và Du lịch `[CO_QUAN_BAN_HANH]`)
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Lao động - Thương binh và Xã hội `[LINH_VUC]`)
- (`e4` Điều 4 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`)
- (`e5` 1 . Nhiệm vụ : `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 4 `[DIEU]`)
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Lao động - Thương binh và Xã hội `[LINH_VUC]`)
- (`e5` 1 . Nhiệm vụ : `[KHOAN]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Lao động - Thương binh và Xã hội `[LINH_VUC]`)


---

### Mẫu #02_2023_TT-BVHTTDL_159924#body_context_100 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[02/2023/TT-BVHTTDL]`<SO_HIEU>`** ban hành **[ngày 21 tháng 02 năm 2023]`<NGAY_BAN_HANH>`** bởi **[Bộ Văn hóa , Thể thao và Du lịch]`<CO_QUAN_BAN_HANH>`** . **[Chương IV. ĐIỀU KHOẢN THI HÀNH]`<CHUONG>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **02/2023/TT-BVHTTDL** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Văn hóa , Thể thao và Du lịch** → `CO_QUAN_BAN_HANH` (span: `[11:17]`)
- `[e3]` **ngày 21 tháng 02 năm 2023** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Chương IV. ĐIỀU KHOẢN THI HÀNH** → `CHUONG` (span: `[18:22]`)

**Quan hệ:**
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Văn hóa , Thể thao và Du lịch `[CO_QUAN_BAN_HANH]`)
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 21 tháng 02 năm 2023 `[NGAY_BAN_HANH]`)
- (`e4` Chương IV. ĐIỀU KHOẢN THI HÀNH `[CHUONG]`) ==[ **THUOC_VE** ]==> (`e1` 02/2023/TT-BVHTTDL `[SO_HIEU]`)


---

### Mẫu #02_2023_TT-BVHTTDL_159924#hard_negative_101 (Loại: `hard_negative`)
> CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM Độc lập - Tự do - Hạnh phúc


---
