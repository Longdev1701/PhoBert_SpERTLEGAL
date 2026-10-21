# Dữ liệu gán nhãn văn bản: 02_2021_TT-BVHTTDL_177987
- **Thể loại**: `thong_tu`
- **Phân vùng dữ liệu**: `TRAIN`
- **Tổng số mẫu**: 23 mẫu
- **Tổng số thực thể**: 136
- **Tổng số quan hệ**: 88

---

### Mẫu #02_2021_TT-BVHTTDL_177987#header_0 (Loại: `header`)
> BỘ VĂN HÓA , THỂ THAO . VÀ DU LỊCH . CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM . Độc lập – Tự do – Hạnh phúc . Số : **[02/2021/TT-BVHTTDL]`<SO_HIEU>`** . Hà Nội , **[ngày 13 tháng 5 năm 2021]`<NGAY_BAN_HANH>`** . **[THÔNG TƯ]`<LOAI_VAN_BAN>`**

**Thực thể:**
- `[e0]` **02/2021/TT-BVHTTDL** → `SO_HIEU` (span: `[23:24]`)
- `[e1]` **ngày 13 tháng 5 năm 2021** → `NGAY_BAN_HANH` (span: `[27:33]`)
- `[e2]` **THÔNG TƯ** → `LOAI_VAN_BAN` (span: `[34:35]`)

**Quan hệ:**
- (`e0` 02/2021/TT-BVHTTDL `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e1` ngày 13 tháng 5 năm 2021 `[NGAY_BAN_HANH]`)
- (`e0` 02/2021/TT-BVHTTDL `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e2` THÔNG TƯ `[LOAI_VAN_BAN]`)


---

### Mẫu #02_2021_TT-BVHTTDL_177987#preamble_context_1 (Loại: `preamble_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[02/2021/TT-BVHTTDL]`<SO_HIEU>`** của **[Bộ Văn hóa , Thể thao và Du lịch]`<CO_QUAN_BAN_HANH>`** . Bãi bỏ một số văn bản quy phạm pháp luật do **[Bộ trưởng Bộ Văn hóa , Thể thao và Du lịch]`<CO_QUAN_THAM_QUYEN>`** ban hành

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **02/2021/TT-BVHTTDL** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Văn hóa , Thể thao và Du lịch** → `CO_QUAN_BAN_HANH` (span: `[4:10]`)
- `[e3]` **Bộ trưởng Bộ Văn hóa , Thể thao và Du lịch** → `CO_QUAN_THAM_QUYEN` (span: `[16:23]`)

**Quan hệ:**
- (`e1` 02/2021/TT-BVHTTDL `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Văn hóa , Thể thao và Du lịch `[CO_QUAN_BAN_HANH]`)
- (`e1` 02/2021/TT-BVHTTDL `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)


---

### Mẫu #02_2021_TT-BVHTTDL_177987#preamble_standalone_2 (Loại: `preamble_standalone`)
> Bãi bỏ một số văn bản quy phạm pháp luật do **[Bộ trưởng Bộ Văn hóa , Thể thao và Du lịch]`<CO_QUAN_THAM_QUYEN>`** ban hành

**Thực thể:**
- `[e0]` **Bộ trưởng Bộ Văn hóa , Thể thao và Du lịch** → `CO_QUAN_THAM_QUYEN` (span: `[5:12]`)


---

### Mẫu #02_2021_TT-BVHTTDL_177987#preamble_context_3 (Loại: `preamble_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[02/2021/TT-BVHTTDL]`<SO_HIEU>`** của **[Bộ Văn hóa , Thể thao và Du lịch]`<CO_QUAN_BAN_HANH>`** . **[Căn cứ]`<TU_KHOA_PHAP_LY>`** **[Luật Ban hành văn bản quy phạm pháp luật]`<THAM_CHIEU_PHAP_LY>`** **[ngày 22 tháng 6 năm 2015]`<NGAY_THAM_CHIEU>`** ; Luật **[sửa đổi , bổ sung một số điều của]`<TU_KHOA_PHAP_LY>`** Luật Ban hành văn bản quy phạm pháp luật năm 2020 ;

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **02/2021/TT-BVHTTDL** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Văn hóa , Thể thao và Du lịch** → `CO_QUAN_BAN_HANH` (span: `[4:10]`)
- `[e3]` **Luật Ban hành văn bản quy phạm pháp luật** → `THAM_CHIEU_PHAP_LY` (span: `[12:15]`)
- `[e4]` **Căn cứ** → `TU_KHOA_PHAP_LY` (span: `[11:12]`)
- `[e5]` **sửa đổi , bổ sung một số điều của** → `TU_KHOA_PHAP_LY` (span: `[23:29]`)
- `[e6]` **ngày 22 tháng 6 năm 2015** → `NGAY_THAM_CHIEU` (span: `[15:21]`)

**Quan hệ:**
- (`e1` 02/2021/TT-BVHTTDL `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Văn hóa , Thể thao và Du lịch `[CO_QUAN_BAN_HANH]`)
- (`e1` 02/2021/TT-BVHTTDL `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e4` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Luật Ban hành văn bản quy phạm pháp luật `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 02/2021/TT-BVHTTDL `[SO_HIEU]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Luật Ban hành văn bản quy phạm pháp luật `[THAM_CHIEU_PHAP_LY]`)
- (`e3` Luật Ban hành văn bản quy phạm pháp luật `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e6` ngày 22 tháng 6 năm 2015 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #02_2021_TT-BVHTTDL_177987#preamble_standalone_4 (Loại: `preamble_standalone`)
> **[Căn cứ]`<TU_KHOA_PHAP_LY>`** **[Luật Ban hành văn bản quy phạm pháp luật]`<THAM_CHIEU_PHAP_LY>`** **[ngày 22 tháng 6 năm 2015]`<NGAY_THAM_CHIEU>`** ; Luật **[sửa đổi , bổ sung một số điều của]`<TU_KHOA_PHAP_LY>`** Luật Ban hành văn bản quy phạm pháp luật năm 2020 ;

**Thực thể:**
- `[e0]` **Luật Ban hành văn bản quy phạm pháp luật** → `THAM_CHIEU_PHAP_LY` (span: `[1:4]`)
- `[e1]` **Căn cứ** → `TU_KHOA_PHAP_LY` (span: `[0:1]`)
- `[e2]` **sửa đổi , bổ sung một số điều của** → `TU_KHOA_PHAP_LY` (span: `[12:18]`)
- `[e3]` **ngày 22 tháng 6 năm 2015** → `NGAY_THAM_CHIEU` (span: `[4:10]`)

**Quan hệ:**
- (`e1` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e0` Luật Ban hành văn bản quy phạm pháp luật `[THAM_CHIEU_PHAP_LY]`)
- (`e0` Luật Ban hành văn bản quy phạm pháp luật `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e3` ngày 22 tháng 6 năm 2015 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #02_2021_TT-BVHTTDL_177987#preamble_context_5 (Loại: `preamble_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[02/2021/TT-BVHTTDL]`<SO_HIEU>`** của **[Bộ Văn hóa , Thể thao và Du lịch]`<CO_QUAN_BAN_HANH>`** . **[Căn cứ]`<TU_KHOA_PHAP_LY>`** **[Nghị định số 34/2016/NĐ-CP]`<THAM_CHIEU_PHAP_LY>`** **[ngày 14 tháng 5 năm 2016]`<NGAY_THAM_CHIEU>`** của **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** quy định chi tiết một số điều và biện pháp thi hành Luật Ban hành văn bản quy phạm pháp luật ; **[Nghị định số 154/2020/NĐ-CP]`<THAM_CHIEU_PHAP_LY>`** **[ngày 31 tháng 12 năm 2020]`<NGAY_THAM_CHIEU>`** của **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** **[sửa đổi , bổ sung một số điều của]`<TU_KHOA_PHAP_LY>`** **[Nghị định số 34/2016/NĐ-CP]`<THAM_CHIEU_PHAP_LY>`** **[ngày 14 tháng 5 năm 2016]`<NGAY_THAM_CHIEU>`** của **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** quy định chi tiết một số điều và biện pháp thi hành Luật Ban hành văn bản quy phạm pháp

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **02/2021/TT-BVHTTDL** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Văn hóa , Thể thao và Du lịch** → `CO_QUAN_BAN_HANH` (span: `[4:10]`)
- `[e3]` **Nghị định số 34/2016/NĐ-CP** → `THAM_CHIEU_PHAP_LY` (span: `[12:15]`)
- `[e4]` **Nghị định số 154/2020/NĐ-CP** → `THAM_CHIEU_PHAP_LY` (span: `[34:37]`)
- `[e5]` **Nghị định số 34/2016/NĐ-CP** → `THAM_CHIEU_PHAP_LY` (span: `[51:54]`)
- `[e6]` **Căn cứ** → `TU_KHOA_PHAP_LY` (span: `[11:12]`)
- `[e7]` **sửa đổi , bổ sung một số điều của** → `TU_KHOA_PHAP_LY` (span: `[45:51]`)
- `[e8]` **ngày 14 tháng 5 năm 2016** → `NGAY_THAM_CHIEU` (span: `[15:21]`)
- `[e9]` **ngày 31 tháng 12 năm 2020** → `NGAY_THAM_CHIEU` (span: `[37:43]`)
- `[e10]` **ngày 14 tháng 5 năm 2016** → `NGAY_THAM_CHIEU` (span: `[54:60]`)
- `[e11]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[22:23]`)
- `[e12]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[44:45]`)
- `[e13]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[61:62]`)

**Quan hệ:**
- (`e1` 02/2021/TT-BVHTTDL `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Văn hóa , Thể thao và Du lịch `[CO_QUAN_BAN_HANH]`)
- (`e1` 02/2021/TT-BVHTTDL `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e6` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Nghị định số 34/2016/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 02/2021/TT-BVHTTDL `[SO_HIEU]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Nghị định số 34/2016/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e6` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e4` Nghị định số 154/2020/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 02/2021/TT-BVHTTDL `[SO_HIEU]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e4` Nghị định số 154/2020/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e7` sửa đổi , bổ sung một số điều của `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e5` Nghị định số 34/2016/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 02/2021/TT-BVHTTDL `[SO_HIEU]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e5` Nghị định số 34/2016/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e3` Nghị định số 34/2016/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e8` ngày 14 tháng 5 năm 2016 `[NGAY_THAM_CHIEU]`)
- (`e4` Nghị định số 154/2020/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e9` ngày 31 tháng 12 năm 2020 `[NGAY_THAM_CHIEU]`)
- (`e5` Nghị định số 34/2016/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e10` ngày 14 tháng 5 năm 2016 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #02_2021_TT-BVHTTDL_177987#preamble_standalone_6 (Loại: `preamble_standalone`)
> **[Căn cứ]`<TU_KHOA_PHAP_LY>`** **[Nghị định số 34/2016/NĐ-CP]`<THAM_CHIEU_PHAP_LY>`** **[ngày 14 tháng 5 năm 2016]`<NGAY_THAM_CHIEU>`** của **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** quy định chi tiết một số điều và biện pháp thi hành Luật Ban hành văn bản quy phạm pháp luật ; **[Nghị định số 154/2020/NĐ-CP]`<THAM_CHIEU_PHAP_LY>`** **[ngày 31 tháng 12 năm 2020]`<NGAY_THAM_CHIEU>`** của **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** **[sửa đổi , bổ sung một số điều của]`<TU_KHOA_PHAP_LY>`** **[Nghị định số 34/2016/NĐ-CP]`<THAM_CHIEU_PHAP_LY>`** **[ngày 14 tháng 5 năm 2016]`<NGAY_THAM_CHIEU>`** của **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** quy định chi tiết một số điều và biện pháp thi hành Luật Ban hành văn bản quy phạm pháp

**Thực thể:**
- `[e0]` **Nghị định số 34/2016/NĐ-CP** → `THAM_CHIEU_PHAP_LY` (span: `[1:4]`)
- `[e1]` **Nghị định số 154/2020/NĐ-CP** → `THAM_CHIEU_PHAP_LY` (span: `[23:26]`)
- `[e2]` **Nghị định số 34/2016/NĐ-CP** → `THAM_CHIEU_PHAP_LY` (span: `[40:43]`)
- `[e3]` **Căn cứ** → `TU_KHOA_PHAP_LY` (span: `[0:1]`)
- `[e4]` **sửa đổi , bổ sung một số điều của** → `TU_KHOA_PHAP_LY` (span: `[34:40]`)
- `[e5]` **ngày 14 tháng 5 năm 2016** → `NGAY_THAM_CHIEU` (span: `[4:10]`)
- `[e6]` **ngày 31 tháng 12 năm 2020** → `NGAY_THAM_CHIEU` (span: `[26:32]`)
- `[e7]` **ngày 14 tháng 5 năm 2016** → `NGAY_THAM_CHIEU` (span: `[43:49]`)
- `[e8]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[11:12]`)
- `[e9]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[33:34]`)
- `[e10]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[50:51]`)

**Quan hệ:**
- (`e3` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e0` Nghị định số 34/2016/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e8` Chính phủ `[CO_QUAN_THAM_QUYEN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e0` Nghị định số 34/2016/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e3` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e1` Nghị định số 154/2020/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e9` Chính phủ `[CO_QUAN_THAM_QUYEN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e1` Nghị định số 154/2020/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e4` sửa đổi , bổ sung một số điều của `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e2` Nghị định số 34/2016/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e9` Chính phủ `[CO_QUAN_THAM_QUYEN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e2` Nghị định số 34/2016/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e0` Nghị định số 34/2016/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e5` ngày 14 tháng 5 năm 2016 `[NGAY_THAM_CHIEU]`)
- (`e1` Nghị định số 154/2020/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e6` ngày 31 tháng 12 năm 2020 `[NGAY_THAM_CHIEU]`)
- (`e2` Nghị định số 34/2016/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e7` ngày 14 tháng 5 năm 2016 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #02_2021_TT-BVHTTDL_177987#preamble_context_7 (Loại: `preamble_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[02/2021/TT-BVHTTDL]`<SO_HIEU>`** của **[Bộ Văn hóa , Thể thao và Du lịch]`<CO_QUAN_BAN_HANH>`** . **[Căn cứ]`<TU_KHOA_PHAP_LY>`** **[Nghị định số 79/2017/NĐ-CP]`<THAM_CHIEU_PHAP_LY>`** **[ngày 17 tháng 7 năm 2017]`<NGAY_THAM_CHIEU>`** của **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** quy định chức năng , nhiệm vụ , quyền hạn và cơ cấu tổ chức của **[Bộ Văn hóa , Thể thao và Du lịch]`<CO_QUAN_THAM_QUYEN>`** ;

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **02/2021/TT-BVHTTDL** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Văn hóa , Thể thao và Du lịch** → `CO_QUAN_BAN_HANH` (span: `[4:10]`)
- `[e3]` **Nghị định số 79/2017/NĐ-CP** → `THAM_CHIEU_PHAP_LY` (span: `[12:15]`)
- `[e4]` **Căn cứ** → `TU_KHOA_PHAP_LY` (span: `[11:12]`)
- `[e5]` **ngày 17 tháng 7 năm 2017** → `NGAY_THAM_CHIEU` (span: `[15:21]`)
- `[e6]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[22:23]`)
- `[e7]` **Bộ Văn hóa , Thể thao và Du lịch** → `CO_QUAN_THAM_QUYEN` (span: `[33:39]`)

**Quan hệ:**
- (`e1` 02/2021/TT-BVHTTDL `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Văn hóa , Thể thao và Du lịch `[CO_QUAN_BAN_HANH]`)
- (`e1` 02/2021/TT-BVHTTDL `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e4` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Nghị định số 79/2017/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 02/2021/TT-BVHTTDL `[SO_HIEU]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Nghị định số 79/2017/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e3` Nghị định số 79/2017/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e5` ngày 17 tháng 7 năm 2017 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #02_2021_TT-BVHTTDL_177987#preamble_standalone_8 (Loại: `preamble_standalone`)
> **[Căn cứ]`<TU_KHOA_PHAP_LY>`** **[Nghị định số 79/2017/NĐ-CP]`<THAM_CHIEU_PHAP_LY>`** **[ngày 17 tháng 7 năm 2017]`<NGAY_THAM_CHIEU>`** của **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** quy định chức năng , nhiệm vụ , quyền hạn và cơ cấu tổ chức của **[Bộ Văn hóa , Thể thao và Du lịch]`<CO_QUAN_THAM_QUYEN>`** ;

**Thực thể:**
- `[e0]` **Nghị định số 79/2017/NĐ-CP** → `THAM_CHIEU_PHAP_LY` (span: `[1:4]`)
- `[e1]` **Căn cứ** → `TU_KHOA_PHAP_LY` (span: `[0:1]`)
- `[e2]` **ngày 17 tháng 7 năm 2017** → `NGAY_THAM_CHIEU` (span: `[4:10]`)
- `[e3]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[11:12]`)
- `[e4]` **Bộ Văn hóa , Thể thao và Du lịch** → `CO_QUAN_THAM_QUYEN` (span: `[22:28]`)

**Quan hệ:**
- (`e1` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e0` Nghị định số 79/2017/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e3` Chính phủ `[CO_QUAN_THAM_QUYEN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e0` Nghị định số 79/2017/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e0` Nghị định số 79/2017/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e2` ngày 17 tháng 7 năm 2017 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #02_2021_TT-BVHTTDL_177987#preamble_context_9 (Loại: `preamble_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[02/2021/TT-BVHTTDL]`<SO_HIEU>`** của **[Bộ Văn hóa , Thể thao và Du lịch]`<CO_QUAN_BAN_HANH>`** . **[Bộ trưởng Bộ Văn hóa , Thể thao và Du lịch]`<CO_QUAN_THAM_QUYEN>`** ban hành Thông tư bãi bỏ một số văn bản quy phạm pháp luật do **[Bộ trưởng Bộ Văn hóa , Thể thao và Du lịch]`<CO_QUAN_THAM_QUYEN>`** ban hành .

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **02/2021/TT-BVHTTDL** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Văn hóa , Thể thao và Du lịch** → `CO_QUAN_BAN_HANH` (span: `[4:10]`)
- `[e3]` **Bộ trưởng Bộ Văn hóa , Thể thao và Du lịch** → `CO_QUAN_THAM_QUYEN` (span: `[11:18]`)
- `[e4]` **Bộ trưởng Bộ Văn hóa , Thể thao và Du lịch** → `CO_QUAN_THAM_QUYEN` (span: `[25:32]`)

**Quan hệ:**
- (`e1` 02/2021/TT-BVHTTDL `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Văn hóa , Thể thao và Du lịch `[CO_QUAN_BAN_HANH]`)
- (`e1` 02/2021/TT-BVHTTDL `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)


---

### Mẫu #02_2021_TT-BVHTTDL_177987#preamble_standalone_10 (Loại: `preamble_standalone`)
> **[Bộ trưởng Bộ Văn hóa , Thể thao và Du lịch]`<CO_QUAN_THAM_QUYEN>`** ban hành Thông tư bãi bỏ một số văn bản quy phạm pháp luật do **[Bộ trưởng Bộ Văn hóa , Thể thao và Du lịch]`<CO_QUAN_THAM_QUYEN>`** ban hành .

**Thực thể:**
- `[e0]` **Bộ trưởng Bộ Văn hóa , Thể thao và Du lịch** → `CO_QUAN_THAM_QUYEN` (span: `[0:7]`)
- `[e1]` **Bộ trưởng Bộ Văn hóa , Thể thao và Du lịch** → `CO_QUAN_THAM_QUYEN` (span: `[14:21]`)


---

### Mẫu #02_2021_TT-BVHTTDL_177987#body_context_11 (Loại: `body_context`)
> **[Bộ Văn hóa , Thể thao và Du lịch]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[02/2021/TT-BVHTTDL]`<SO_HIEU>`** . **[Điều 1 . Bãi bỏ một số văn bản quy phạm pháp luật do **[Bộ trưởng Bộ Văn hóa , Thể thao và Du lịch]`<CO_QUAN_THAM_QUYEN>`** ban hành . Bãi bỏ toàn bộ các văn bản quy phạm pháp luật sau đây :]`<DIEU>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[7:8]`)
- `[e1]` **02/2021/TT-BVHTTDL** → `SO_HIEU` (span: `[9:10]`)
- `[e2]` **Bộ Văn hóa , Thể thao và Du lịch** → `CO_QUAN_BAN_HANH` (span: `[0:6]`)
- `[e3]` **Điều 1 . Bãi bỏ một số văn bản quy phạm pháp luật do Bộ trưởng Bộ Văn hóa , Thể thao và Du lịch ban hành . Bãi bỏ toàn bộ các văn bản quy phạm pháp luật sau đây :** → `DIEU` (span: `[11:36]`)
- `[e4]` **Bộ trưởng Bộ Văn hóa , Thể thao và Du lịch** → `CO_QUAN_THAM_QUYEN` (span: `[19:26]`) *(lồng trong `e3` (`DIEU`))*

**Quan hệ:**
- (`e1` 02/2021/TT-BVHTTDL `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Văn hóa , Thể thao và Du lịch `[CO_QUAN_BAN_HANH]`)
- (`e1` 02/2021/TT-BVHTTDL `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 1 . Bãi bỏ một số văn bản quy phạm pháp luật do Bộ trưởng Bộ Văn hóa , Thể thao và Du lịch ban hành . Bãi bỏ toàn bộ các văn bản quy phạm pháp luật sau đây : `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 02/2021/TT-BVHTTDL `[SO_HIEU]`)


---

### Mẫu #02_2021_TT-BVHTTDL_177987#body_context_12 (Loại: `body_context`)
> **[Bộ Văn hóa , Thể thao và Du lịch]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[02/2021/TT-BVHTTDL]`<SO_HIEU>`** . **[Điều 1]`<DIEU>`** . **[1 . **[Thông tư số 09/2014/TT-BVHTTDL]`<THAM_CHIEU_PHAP_LY>`** **[ngày 29 tháng 9 năm 2014]`<NGAY_THAM_CHIEU>`** của **[Bộ trưởng Bộ Văn hóa , Thể thao và Du lịch]`<CO_QUAN_THAM_QUYEN>`** quy định công tác bảo vệ bí mật nhà nước trong ngành văn hóa , thể thao và du lịch .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[7:8]`)
- `[e1]` **02/2021/TT-BVHTTDL** → `SO_HIEU` (span: `[9:10]`)
- `[e2]` **Bộ Văn hóa , Thể thao và Du lịch** → `CO_QUAN_BAN_HANH` (span: `[0:6]`)
- `[e3]` **Điều 1** → `DIEU` (span: `[11:13]`)
- `[e4]` **1 . Thông tư số 09/2014/TT-BVHTTDL ngày 29 tháng 9 năm 2014 của Bộ trưởng Bộ Văn hóa , Thể thao và Du lịch quy định công tác bảo vệ bí mật nhà nước trong ngành văn hóa , thể thao và du lịch .** → `KHOAN` (span: `[14:46]`)
- `[e5]` **Thông tư số 09/2014/TT-BVHTTDL** → `THAM_CHIEU_PHAP_LY` (span: `[16:19]`) *(lồng trong `e4` (`KHOAN`))*
- `[e6]` **ngày 29 tháng 9 năm 2014** → `NGAY_THAM_CHIEU` (span: `[19:25]`) *(lồng trong `e4` (`KHOAN`))*
- `[e7]` **Bộ trưởng Bộ Văn hóa , Thể thao và Du lịch** → `CO_QUAN_THAM_QUYEN` (span: `[26:33]`) *(lồng trong `e4` (`KHOAN`))*

**Quan hệ:**
- (`e1` 02/2021/TT-BVHTTDL `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Văn hóa , Thể thao và Du lịch `[CO_QUAN_BAN_HANH]`)
- (`e1` 02/2021/TT-BVHTTDL `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 1 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 02/2021/TT-BVHTTDL `[SO_HIEU]`)
- (`e4` 1 . Thông tư số 09/2014/TT-BVHTTDL ngày 29 tháng 9 năm 2014 của Bộ trưởng Bộ Văn hóa , Thể thao và Du lịch quy định công tác bảo vệ bí mật nhà nước trong ngành văn hóa , thể thao và du lịch . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 1 `[DIEU]`)
- (`e4` 1 . Thông tư số 09/2014/TT-BVHTTDL ngày 29 tháng 9 năm 2014 của Bộ trưởng Bộ Văn hóa , Thể thao và Du lịch quy định công tác bảo vệ bí mật nhà nước trong ngành văn hóa , thể thao và du lịch . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e5` Thông tư số 09/2014/TT-BVHTTDL `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e5` Thông tư số 09/2014/TT-BVHTTDL `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e6` ngày 29 tháng 9 năm 2014 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #02_2021_TT-BVHTTDL_177987#body_standalone_13 (Loại: `body_standalone`)
> **[Điều 1]`<DIEU>`** . **[1 . **[Thông tư số 09/2014/TT-BVHTTDL]`<THAM_CHIEU_PHAP_LY>`** **[ngày 29 tháng 9 năm 2014]`<NGAY_THAM_CHIEU>`** của **[Bộ trưởng Bộ Văn hóa , Thể thao và Du lịch]`<CO_QUAN_THAM_QUYEN>`** quy định công tác bảo vệ bí mật nhà nước trong ngành văn hóa , thể thao và du lịch .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 1** → `DIEU` (span: `[0:2]`)
- `[e1]` **1 . Thông tư số 09/2014/TT-BVHTTDL ngày 29 tháng 9 năm 2014 của Bộ trưởng Bộ Văn hóa , Thể thao và Du lịch quy định công tác bảo vệ bí mật nhà nước trong ngành văn hóa , thể thao và du lịch .** → `KHOAN` (span: `[3:35]`)
- `[e2]` **Thông tư số 09/2014/TT-BVHTTDL** → `THAM_CHIEU_PHAP_LY` (span: `[5:8]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **ngày 29 tháng 9 năm 2014** → `NGAY_THAM_CHIEU` (span: `[8:14]`) *(lồng trong `e1` (`KHOAN`))*
- `[e4]` **Bộ trưởng Bộ Văn hóa , Thể thao và Du lịch** → `CO_QUAN_THAM_QUYEN` (span: `[15:22]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 1 . Thông tư số 09/2014/TT-BVHTTDL ngày 29 tháng 9 năm 2014 của Bộ trưởng Bộ Văn hóa , Thể thao và Du lịch quy định công tác bảo vệ bí mật nhà nước trong ngành văn hóa , thể thao và du lịch . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 1 `[DIEU]`)
- (`e1` 1 . Thông tư số 09/2014/TT-BVHTTDL ngày 29 tháng 9 năm 2014 của Bộ trưởng Bộ Văn hóa , Thể thao và Du lịch quy định công tác bảo vệ bí mật nhà nước trong ngành văn hóa , thể thao và du lịch . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e2` Thông tư số 09/2014/TT-BVHTTDL `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e2` Thông tư số 09/2014/TT-BVHTTDL `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e3` ngày 29 tháng 9 năm 2014 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #02_2021_TT-BVHTTDL_177987#body_context_14 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[02/2021/TT-BVHTTDL]`<SO_HIEU>`** của **[Bộ Văn hóa , Thể thao và Du lịch]`<CO_QUAN_BAN_HANH>`** . **[Điều 1]`<DIEU>`** . **[2 . **[Thông tư số 16/2016/TT-BVHTTDL]`<THAM_CHIEU_PHAP_LY>`** **[ngày 27 tháng 12 năm 2016]`<NGAY_THAM_CHIEU>`** của **[Bộ trưởng Bộ Văn hóa , Thể thao và Du lịch]`<CO_QUAN_THAM_QUYEN>`** hướng dẫn thực hiện **[Quyết định số 650/QĐ-TTg]`<THAM_CHIEU_PHAP_LY>`** **[ngày 25 tháng 4 năm 2016]`<NGAY_THAM_CHIEU>`** của]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **02/2021/TT-BVHTTDL** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Văn hóa , Thể thao và Du lịch** → `CO_QUAN_BAN_HANH` (span: `[4:10]`)
- `[e3]` **Điều 1** → `DIEU` (span: `[11:13]`)
- `[e4]` **2 . Thông tư số 16/2016/TT-BVHTTDL ngày 27 tháng 12 năm 2016 của Bộ trưởng Bộ Văn hóa , Thể thao và Du lịch hướng dẫn thực hiện Quyết định số 650/QĐ-TTg ngày 25 tháng 4 năm 2016 của** → `KHOAN` (span: `[14:45]`)
- `[e5]` **Thông tư số 16/2016/TT-BVHTTDL** → `THAM_CHIEU_PHAP_LY` (span: `[16:19]`) *(lồng trong `e4` (`KHOAN`))*
- `[e6]` **Quyết định số 650/QĐ-TTg** → `THAM_CHIEU_PHAP_LY` (span: `[35:38]`) *(lồng trong `e4` (`KHOAN`))*
- `[e7]` **ngày 27 tháng 12 năm 2016** → `NGAY_THAM_CHIEU` (span: `[19:25]`) *(lồng trong `e4` (`KHOAN`))*
- `[e8]` **ngày 25 tháng 4 năm 2016** → `NGAY_THAM_CHIEU` (span: `[38:44]`) *(lồng trong `e4` (`KHOAN`))*
- `[e9]` **Bộ trưởng Bộ Văn hóa , Thể thao và Du lịch** → `CO_QUAN_THAM_QUYEN` (span: `[26:33]`) *(lồng trong `e4` (`KHOAN`))*

**Quan hệ:**
- (`e1` 02/2021/TT-BVHTTDL `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Văn hóa , Thể thao và Du lịch `[CO_QUAN_BAN_HANH]`)
- (`e1` 02/2021/TT-BVHTTDL `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 1 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 02/2021/TT-BVHTTDL `[SO_HIEU]`)
- (`e4` 2 . Thông tư số 16/2016/TT-BVHTTDL ngày 27 tháng 12 năm 2016 của Bộ trưởng Bộ Văn hóa , Thể thao và Du lịch hướng dẫn thực hiện Quyết định số 650/QĐ-TTg ngày 25 tháng 4 năm 2016 của `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 1 `[DIEU]`)
- (`e4` 2 . Thông tư số 16/2016/TT-BVHTTDL ngày 27 tháng 12 năm 2016 của Bộ trưởng Bộ Văn hóa , Thể thao và Du lịch hướng dẫn thực hiện Quyết định số 650/QĐ-TTg ngày 25 tháng 4 năm 2016 của `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e5` Thông tư số 16/2016/TT-BVHTTDL `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e4` 2 . Thông tư số 16/2016/TT-BVHTTDL ngày 27 tháng 12 năm 2016 của Bộ trưởng Bộ Văn hóa , Thể thao và Du lịch hướng dẫn thực hiện Quyết định số 650/QĐ-TTg ngày 25 tháng 4 năm 2016 của `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e6` Quyết định số 650/QĐ-TTg `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e5` Thông tư số 16/2016/TT-BVHTTDL `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e7` ngày 27 tháng 12 năm 2016 `[NGAY_THAM_CHIEU]`)
- (`e6` Quyết định số 650/QĐ-TTg `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e8` ngày 25 tháng 4 năm 2016 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #02_2021_TT-BVHTTDL_177987#body_standalone_15 (Loại: `body_standalone`)
> **[Điều 1]`<DIEU>`** . **[2 . **[Thông tư số 16/2016/TT-BVHTTDL]`<THAM_CHIEU_PHAP_LY>`** **[ngày 27 tháng 12 năm 2016]`<NGAY_THAM_CHIEU>`** của **[Bộ trưởng Bộ Văn hóa , Thể thao và Du lịch]`<CO_QUAN_THAM_QUYEN>`** hướng dẫn thực hiện **[Quyết định số 650/QĐ-TTg]`<THAM_CHIEU_PHAP_LY>`** **[ngày 25 tháng 4 năm 2016]`<NGAY_THAM_CHIEU>`** của]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 1** → `DIEU` (span: `[0:2]`)
- `[e1]` **2 . Thông tư số 16/2016/TT-BVHTTDL ngày 27 tháng 12 năm 2016 của Bộ trưởng Bộ Văn hóa , Thể thao và Du lịch hướng dẫn thực hiện Quyết định số 650/QĐ-TTg ngày 25 tháng 4 năm 2016 của** → `KHOAN` (span: `[3:34]`)
- `[e2]` **Thông tư số 16/2016/TT-BVHTTDL** → `THAM_CHIEU_PHAP_LY` (span: `[5:8]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **Quyết định số 650/QĐ-TTg** → `THAM_CHIEU_PHAP_LY` (span: `[24:27]`) *(lồng trong `e1` (`KHOAN`))*
- `[e4]` **ngày 27 tháng 12 năm 2016** → `NGAY_THAM_CHIEU` (span: `[8:14]`) *(lồng trong `e1` (`KHOAN`))*
- `[e5]` **ngày 25 tháng 4 năm 2016** → `NGAY_THAM_CHIEU` (span: `[27:33]`) *(lồng trong `e1` (`KHOAN`))*
- `[e6]` **Bộ trưởng Bộ Văn hóa , Thể thao và Du lịch** → `CO_QUAN_THAM_QUYEN` (span: `[15:22]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 2 . Thông tư số 16/2016/TT-BVHTTDL ngày 27 tháng 12 năm 2016 của Bộ trưởng Bộ Văn hóa , Thể thao và Du lịch hướng dẫn thực hiện Quyết định số 650/QĐ-TTg ngày 25 tháng 4 năm 2016 của `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 1 `[DIEU]`)
- (`e1` 2 . Thông tư số 16/2016/TT-BVHTTDL ngày 27 tháng 12 năm 2016 của Bộ trưởng Bộ Văn hóa , Thể thao và Du lịch hướng dẫn thực hiện Quyết định số 650/QĐ-TTg ngày 25 tháng 4 năm 2016 của `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e2` Thông tư số 16/2016/TT-BVHTTDL `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e1` 2 . Thông tư số 16/2016/TT-BVHTTDL ngày 27 tháng 12 năm 2016 của Bộ trưởng Bộ Văn hóa , Thể thao và Du lịch hướng dẫn thực hiện Quyết định số 650/QĐ-TTg ngày 25 tháng 4 năm 2016 của `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Quyết định số 650/QĐ-TTg `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e2` Thông tư số 16/2016/TT-BVHTTDL `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e4` ngày 27 tháng 12 năm 2016 `[NGAY_THAM_CHIEU]`)
- (`e3` Quyết định số 650/QĐ-TTg `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e5` ngày 25 tháng 4 năm 2016 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #02_2021_TT-BVHTTDL_177987#body_context_16 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[02/2021/TT-BVHTTDL]`<SO_HIEU>`** của **[Bộ Văn hóa , Thể thao và Du lịch]`<CO_QUAN_BAN_HANH>`** . **[Điều 1]`<DIEU>`** . **[3 . **[Thông tư số 09/2019/TT-BVHTTDL]`<THAM_CHIEU_PHAP_LY>`** **[ngày 09 tháng 9 năm 2019]`<NGAY_THAM_CHIEU>`** của **[Bộ trưởng Bộ Văn hóa , Thể thao và Du lịch]`<CO_QUAN_THAM_QUYEN>`** quy định tiêu chuẩn chức danh **[Giám đốc]`<CHU_THE_CA_NHAN>`** , **[Phó Giám đốc]`<CHU_THE_CA_NHAN>`** Sở Văn hóa , Thể thao và Du lịch ; Sở Văn hóa và Thể thao ; Sở Du lịch thuộc **[Ủy ban nhân dân tỉnh , thành phố trực thuộc Trung ương]`<CO_QUAN_THAM_QUYEN>`** .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **02/2021/TT-BVHTTDL** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Văn hóa , Thể thao và Du lịch** → `CO_QUAN_BAN_HANH` (span: `[4:10]`)
- `[e3]` **Điều 1** → `DIEU` (span: `[11:13]`)
- `[e4]` **3 . Thông tư số 09/2019/TT-BVHTTDL ngày 09 tháng 9 năm 2019 của Bộ trưởng Bộ Văn hóa , Thể thao và Du lịch quy định tiêu chuẩn chức danh Giám đốc , Phó Giám đốc Sở Văn hóa , Thể thao và Du lịch ; Sở Văn hóa và Thể thao ; Sở Du lịch thuộc Ủy ban nhân dân tỉnh , thành phố trực thuộc Trung ương .** → `KHOAN` (span: `[14:62]`)
- `[e5]` **Thông tư số 09/2019/TT-BVHTTDL** → `THAM_CHIEU_PHAP_LY` (span: `[16:19]`) *(lồng trong `e4` (`KHOAN`))*
- `[e6]` **ngày 09 tháng 9 năm 2019** → `NGAY_THAM_CHIEU` (span: `[19:25]`) *(lồng trong `e4` (`KHOAN`))*
- `[e7]` **Bộ trưởng Bộ Văn hóa , Thể thao và Du lịch** → `CO_QUAN_THAM_QUYEN` (span: `[26:33]`) *(lồng trong `e4` (`KHOAN`))*
- `[e8]` **Ủy ban nhân dân tỉnh , thành phố trực thuộc Trung ương** → `CO_QUAN_THAM_QUYEN` (span: `[54:61]`) *(lồng trong `e4` (`KHOAN`))*
- `[e9]` **Giám đốc** → `CHU_THE_CA_NHAN` (span: `[36:37]`) *(lồng trong `e4` (`KHOAN`))*
- `[e10]` **Phó Giám đốc** → `CHU_THE_CA_NHAN` (span: `[38:39]`) *(lồng trong `e4` (`KHOAN`))*

**Quan hệ:**
- (`e1` 02/2021/TT-BVHTTDL `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Văn hóa , Thể thao và Du lịch `[CO_QUAN_BAN_HANH]`)
- (`e1` 02/2021/TT-BVHTTDL `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 1 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 02/2021/TT-BVHTTDL `[SO_HIEU]`)
- (`e4` 3 . Thông tư số 09/2019/TT-BVHTTDL ngày 09 tháng 9 năm 2019 của Bộ trưởng Bộ Văn hóa , Thể thao và Du lịch quy định tiêu chuẩn chức danh Giám đốc , Phó Giám đốc Sở Văn hóa , Thể thao và Du lịch ; Sở Văn hóa và Thể thao ; Sở Du lịch thuộc Ủy ban nhân dân tỉnh , thành phố trực thuộc Trung ương . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 1 `[DIEU]`)
- (`e4` 3 . Thông tư số 09/2019/TT-BVHTTDL ngày 09 tháng 9 năm 2019 của Bộ trưởng Bộ Văn hóa , Thể thao và Du lịch quy định tiêu chuẩn chức danh Giám đốc , Phó Giám đốc Sở Văn hóa , Thể thao và Du lịch ; Sở Văn hóa và Thể thao ; Sở Du lịch thuộc Ủy ban nhân dân tỉnh , thành phố trực thuộc Trung ương . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e5` Thông tư số 09/2019/TT-BVHTTDL `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e5` Thông tư số 09/2019/TT-BVHTTDL `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e6` ngày 09 tháng 9 năm 2019 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #02_2021_TT-BVHTTDL_177987#body_standalone_17 (Loại: `body_standalone`)
> **[Điều 1]`<DIEU>`** . **[3 . **[Thông tư số 09/2019/TT-BVHTTDL]`<THAM_CHIEU_PHAP_LY>`** **[ngày 09 tháng 9 năm 2019]`<NGAY_THAM_CHIEU>`** của **[Bộ trưởng Bộ Văn hóa , Thể thao và Du lịch]`<CO_QUAN_THAM_QUYEN>`** quy định tiêu chuẩn chức danh **[Giám đốc]`<CHU_THE_CA_NHAN>`** , **[Phó Giám đốc]`<CHU_THE_CA_NHAN>`** Sở Văn hóa , Thể thao và Du lịch ; Sở Văn hóa và Thể thao ; Sở Du lịch thuộc **[Ủy ban nhân dân tỉnh , thành phố trực thuộc Trung ương]`<CO_QUAN_THAM_QUYEN>`** .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 1** → `DIEU` (span: `[0:2]`)
- `[e1]` **3 . Thông tư số 09/2019/TT-BVHTTDL ngày 09 tháng 9 năm 2019 của Bộ trưởng Bộ Văn hóa , Thể thao và Du lịch quy định tiêu chuẩn chức danh Giám đốc , Phó Giám đốc Sở Văn hóa , Thể thao và Du lịch ; Sở Văn hóa và Thể thao ; Sở Du lịch thuộc Ủy ban nhân dân tỉnh , thành phố trực thuộc Trung ương .** → `KHOAN` (span: `[3:51]`)
- `[e2]` **Thông tư số 09/2019/TT-BVHTTDL** → `THAM_CHIEU_PHAP_LY` (span: `[5:8]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **ngày 09 tháng 9 năm 2019** → `NGAY_THAM_CHIEU` (span: `[8:14]`) *(lồng trong `e1` (`KHOAN`))*
- `[e4]` **Bộ trưởng Bộ Văn hóa , Thể thao và Du lịch** → `CO_QUAN_THAM_QUYEN` (span: `[15:22]`) *(lồng trong `e1` (`KHOAN`))*
- `[e5]` **Ủy ban nhân dân tỉnh , thành phố trực thuộc Trung ương** → `CO_QUAN_THAM_QUYEN` (span: `[43:50]`) *(lồng trong `e1` (`KHOAN`))*
- `[e6]` **Giám đốc** → `CHU_THE_CA_NHAN` (span: `[25:26]`) *(lồng trong `e1` (`KHOAN`))*
- `[e7]` **Phó Giám đốc** → `CHU_THE_CA_NHAN` (span: `[27:28]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 3 . Thông tư số 09/2019/TT-BVHTTDL ngày 09 tháng 9 năm 2019 của Bộ trưởng Bộ Văn hóa , Thể thao và Du lịch quy định tiêu chuẩn chức danh Giám đốc , Phó Giám đốc Sở Văn hóa , Thể thao và Du lịch ; Sở Văn hóa và Thể thao ; Sở Du lịch thuộc Ủy ban nhân dân tỉnh , thành phố trực thuộc Trung ương . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 1 `[DIEU]`)
- (`e1` 3 . Thông tư số 09/2019/TT-BVHTTDL ngày 09 tháng 9 năm 2019 của Bộ trưởng Bộ Văn hóa , Thể thao và Du lịch quy định tiêu chuẩn chức danh Giám đốc , Phó Giám đốc Sở Văn hóa , Thể thao và Du lịch ; Sở Văn hóa và Thể thao ; Sở Du lịch thuộc Ủy ban nhân dân tỉnh , thành phố trực thuộc Trung ương . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e2` Thông tư số 09/2019/TT-BVHTTDL `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e2` Thông tư số 09/2019/TT-BVHTTDL `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e3` ngày 09 tháng 9 năm 2019 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #02_2021_TT-BVHTTDL_177987#body_context_18 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[02/2021/TT-BVHTTDL]`<SO_HIEU>`** của **[Bộ Văn hóa , Thể thao và Du lịch]`<CO_QUAN_BAN_HANH>`** . **[Điều 2 . Hiệu lực thi hành . Thông tư này có hiệu lực thi hành kể từ ngày 01 tháng 7 năm 2021 .]`<DIEU>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **02/2021/TT-BVHTTDL** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Văn hóa , Thể thao và Du lịch** → `CO_QUAN_BAN_HANH` (span: `[4:10]`)
- `[e3]` **Điều 2 . Hiệu lực thi hành . Thông tư này có hiệu lực thi hành kể từ ngày 01 tháng 7 năm 2021 .** → `DIEU` (span: `[11:31]`)

**Quan hệ:**
- (`e1` 02/2021/TT-BVHTTDL `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Văn hóa , Thể thao và Du lịch `[CO_QUAN_BAN_HANH]`)
- (`e1` 02/2021/TT-BVHTTDL `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 2 . Hiệu lực thi hành . Thông tư này có hiệu lực thi hành kể từ ngày 01 tháng 7 năm 2021 . `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 02/2021/TT-BVHTTDL `[SO_HIEU]`)


---

### Mẫu #02_2021_TT-BVHTTDL_177987#body_context_19 (Loại: `body_context`)
> **[Bộ Văn hóa , Thể thao và Du lịch]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[02/2021/TT-BVHTTDL]`<SO_HIEU>`** . **[Điều 3 . Trách nhiệm thi hành . Vụ trưởng Vụ Pháp chế , Thủ trưởng các cơ quan , đơn vị thuộc Bộ , **[Giám đốc]`<CHU_THE_CA_NHAN>`** Sở Văn hóa , Thể thao và Du lịch , Sở Văn hóa và Thể thao , Sở Du lịch các tỉnh , thành phố trực thuộc Trung ương , thủ trưởng các cơ quan , đơn vị và cá nhân có liên quan chịu trách nhiệm thi hành Thông tư này . / .]`<DIEU>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[7:8]`)
- `[e1]` **02/2021/TT-BVHTTDL** → `SO_HIEU` (span: `[9:10]`)
- `[e2]` **Bộ Văn hóa , Thể thao và Du lịch** → `CO_QUAN_BAN_HANH` (span: `[0:6]`)
- `[e3]` **Điều 3 . Trách nhiệm thi hành . Vụ trưởng Vụ Pháp chế , Thủ trưởng các cơ quan , đơn vị thuộc Bộ , Giám đốc Sở Văn hóa , Thể thao và Du lịch , Sở Văn hóa và Thể thao , Sở Du lịch các tỉnh , thành phố trực thuộc Trung ương , thủ trưởng các cơ quan , đơn vị và cá nhân có liên quan chịu trách nhiệm thi hành Thông tư này . / .** → `DIEU` (span: `[11:68]`)
- `[e4]` **Giám đốc** → `CHU_THE_CA_NHAN` (span: `[29:30]`) *(lồng trong `e3` (`DIEU`))*

**Quan hệ:**
- (`e1` 02/2021/TT-BVHTTDL `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Văn hóa , Thể thao và Du lịch `[CO_QUAN_BAN_HANH]`)
- (`e1` 02/2021/TT-BVHTTDL `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 3 . Trách nhiệm thi hành . Vụ trưởng Vụ Pháp chế , Thủ trưởng các cơ quan , đơn vị thuộc Bộ , Giám đốc Sở Văn hóa , Thể thao và Du lịch , Sở Văn hóa và Thể thao , Sở Du lịch các tỉnh , thành phố trực thuộc Trung ương , thủ trưởng các cơ quan , đơn vị và cá nhân có liên quan chịu trách nhiệm thi hành Thông tư này . / . `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 02/2021/TT-BVHTTDL `[SO_HIEU]`)


---

### Mẫu #02_2021_TT-BVHTTDL_177987#body_context_20 (Loại: `body_context`)
> **[Bộ Văn hóa , Thể thao và Du lịch]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[02/2021/TT-BVHTTDL]`<SO_HIEU>`** . **[Điều 2 . Hiệu lực thi hành]`<DIEU>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[7:8]`)
- `[e1]` **02/2021/TT-BVHTTDL** → `SO_HIEU` (span: `[9:10]`)
- `[e2]` **Bộ Văn hóa , Thể thao và Du lịch** → `CO_QUAN_BAN_HANH` (span: `[0:6]`)
- `[e3]` **Điều 2 . Hiệu lực thi hành** → `DIEU` (span: `[11:16]`)

**Quan hệ:**
- (`e1` 02/2021/TT-BVHTTDL `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Văn hóa , Thể thao và Du lịch `[CO_QUAN_BAN_HANH]`)
- (`e1` 02/2021/TT-BVHTTDL `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 2 . Hiệu lực thi hành `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 02/2021/TT-BVHTTDL `[SO_HIEU]`)


---

### Mẫu #02_2021_TT-BVHTTDL_177987#body_context_21 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[02/2021/TT-BVHTTDL]`<SO_HIEU>`** ban hành **[ngày 13 tháng 05 năm 2021]`<NGAY_BAN_HANH>`** bởi **[Bộ Văn hóa , Thể thao và Du lịch]`<CO_QUAN_BAN_HANH>`** . **[Điều 3 . Trách nhiệm thi hành]`<DIEU>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **02/2021/TT-BVHTTDL** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Văn hóa , Thể thao và Du lịch** → `CO_QUAN_BAN_HANH` (span: `[11:17]`)
- `[e3]` **ngày 13 tháng 05 năm 2021** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 3 . Trách nhiệm thi hành** → `DIEU` (span: `[18:23]`)

**Quan hệ:**
- (`e1` 02/2021/TT-BVHTTDL `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Văn hóa , Thể thao và Du lịch `[CO_QUAN_BAN_HANH]`)
- (`e1` 02/2021/TT-BVHTTDL `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 02/2021/TT-BVHTTDL `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 13 tháng 05 năm 2021 `[NGAY_BAN_HANH]`)
- (`e4` Điều 3 . Trách nhiệm thi hành `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 02/2021/TT-BVHTTDL `[SO_HIEU]`)


---

### Mẫu #02_2021_TT-BVHTTDL_177987#hard_negative_22 (Loại: `hard_negative`)
> CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM


---
