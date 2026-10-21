# Dữ liệu gán nhãn văn bản: 01_2009_TT-BNV_12219
- **Thể loại**: `thong_tu`
- **Phân vùng dữ liệu**: `TEST`
- **Tổng số mẫu**: 108 mẫu
- **Tổng số thực thể**: 899
- **Tổng số quan hệ**: 519

---

### Mẫu #01_2009_TT-BNV_12219#preamble_context_0 (Loại: `preamble_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[01/2009/TT-BNV]`<SO_HIEU>`** của **[Bộ Nội vụ]`<CO_QUAN_BAN_HANH>`** . **[Căn cứ]`<TU_KHOA_PHAP_LY>`** **[Nghị quyết số 26/2008/QH12]`<THAM_CHIEU_PHAP_LY>`** **[ngày 15 tháng 11 năm 2008]`<NGAY_THAM_CHIEU>`** của **[Quốc hội]`<CO_QUAN_THAM_QUYEN>`** khóa XII về thực hiện thí điểm không tổ chức **[Hội đồng nhân dân huyện , quận , phường]`<CO_QUAN_THAM_QUYEN>`** ;

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **01/2009/TT-BNV** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Nội vụ** → `CO_QUAN_BAN_HANH` (span: `[4:6]`)
- `[e3]` **Nghị quyết số 26/2008/QH12** → `THAM_CHIEU_PHAP_LY` (span: `[8:11]`)
- `[e4]` **Căn cứ** → `TU_KHOA_PHAP_LY` (span: `[7:8]`)
- `[e5]` **ngày 15 tháng 11 năm 2008** → `NGAY_THAM_CHIEU` (span: `[11:17]`)
- `[e6]` **Quốc hội** → `CO_QUAN_THAM_QUYEN` (span: `[18:19]`)
- `[e7]` **Hội đồng nhân dân huyện , quận , phường** → `CO_QUAN_THAM_QUYEN` (span: `[26:33]`)

**Quan hệ:**
- (`e1` 01/2009/TT-BNV `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Nội vụ `[CO_QUAN_BAN_HANH]`)
- (`e1` 01/2009/TT-BNV `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e4` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Nghị quyết số 26/2008/QH12 `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 01/2009/TT-BNV `[SO_HIEU]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Nghị quyết số 26/2008/QH12 `[THAM_CHIEU_PHAP_LY]`)
- (`e3` Nghị quyết số 26/2008/QH12 `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e5` ngày 15 tháng 11 năm 2008 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #01_2009_TT-BNV_12219#preamble_standalone_1 (Loại: `preamble_standalone`)
> **[Căn cứ]`<TU_KHOA_PHAP_LY>`** **[Nghị quyết số 26/2008/QH12]`<THAM_CHIEU_PHAP_LY>`** **[ngày 15 tháng 11 năm 2008]`<NGAY_THAM_CHIEU>`** của **[Quốc hội]`<CO_QUAN_THAM_QUYEN>`** khóa XII về thực hiện thí điểm không tổ chức **[Hội đồng nhân dân huyện , quận , phường]`<CO_QUAN_THAM_QUYEN>`** ;

**Thực thể:**
- `[e0]` **Nghị quyết số 26/2008/QH12** → `THAM_CHIEU_PHAP_LY` (span: `[1:4]`)
- `[e1]` **Căn cứ** → `TU_KHOA_PHAP_LY` (span: `[0:1]`)
- `[e2]` **ngày 15 tháng 11 năm 2008** → `NGAY_THAM_CHIEU` (span: `[4:10]`)
- `[e3]` **Quốc hội** → `CO_QUAN_THAM_QUYEN` (span: `[11:12]`)
- `[e4]` **Hội đồng nhân dân huyện , quận , phường** → `CO_QUAN_THAM_QUYEN` (span: `[19:26]`)

**Quan hệ:**
- (`e1` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e0` Nghị quyết số 26/2008/QH12 `[THAM_CHIEU_PHAP_LY]`)
- (`e3` Quốc hội `[CO_QUAN_THAM_QUYEN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e0` Nghị quyết số 26/2008/QH12 `[THAM_CHIEU_PHAP_LY]`)
- (`e0` Nghị quyết số 26/2008/QH12 `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e2` ngày 15 tháng 11 năm 2008 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #01_2009_TT-BNV_12219#preamble_context_2 (Loại: `preamble_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[01/2009/TT-BNV]`<SO_HIEU>`** của **[Bộ Nội vụ]`<CO_QUAN_BAN_HANH>`** . **[Căn cứ]`<TU_KHOA_PHAP_LY>`** **[Nghị quyết số 724/2009/UBTVQH12]`<THAM_CHIEU_PHAP_LY>`** **[ngày 16 tháng 01 năm 2009]`<NGAY_THAM_CHIEU>`** của **[Ủy ban thường vụ Quốc hội]`<CO_QUAN_THAM_QUYEN>`** về danh sách huyện , quận , phường của các tỉnh , thành phố trực thuộc trung ương thực hiện thí điểm không tổ chức **[Hội đồng nhân dân huyện , quận , phường]`<CO_QUAN_THAM_QUYEN>`** ;

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **01/2009/TT-BNV** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Nội vụ** → `CO_QUAN_BAN_HANH` (span: `[4:6]`)
- `[e3]` **Nghị quyết số 724/2009/UBTVQH12** → `THAM_CHIEU_PHAP_LY` (span: `[8:11]`)
- `[e4]` **Căn cứ** → `TU_KHOA_PHAP_LY` (span: `[7:8]`)
- `[e5]` **ngày 16 tháng 01 năm 2009** → `NGAY_THAM_CHIEU` (span: `[11:17]`)
- `[e6]` **Ủy ban thường vụ Quốc hội** → `CO_QUAN_THAM_QUYEN` (span: `[18:21]`)
- `[e7]` **Hội đồng nhân dân huyện , quận , phường** → `CO_QUAN_THAM_QUYEN` (span: `[39:46]`)

**Quan hệ:**
- (`e1` 01/2009/TT-BNV `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Nội vụ `[CO_QUAN_BAN_HANH]`)
- (`e1` 01/2009/TT-BNV `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e4` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Nghị quyết số 724/2009/UBTVQH12 `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 01/2009/TT-BNV `[SO_HIEU]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Nghị quyết số 724/2009/UBTVQH12 `[THAM_CHIEU_PHAP_LY]`)
- (`e3` Nghị quyết số 724/2009/UBTVQH12 `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e5` ngày 16 tháng 01 năm 2009 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #01_2009_TT-BNV_12219#preamble_standalone_3 (Loại: `preamble_standalone`)
> **[Căn cứ]`<TU_KHOA_PHAP_LY>`** **[Nghị quyết số 724/2009/UBTVQH12]`<THAM_CHIEU_PHAP_LY>`** **[ngày 16 tháng 01 năm 2009]`<NGAY_THAM_CHIEU>`** của **[Ủy ban thường vụ Quốc hội]`<CO_QUAN_THAM_QUYEN>`** về danh sách huyện , quận , phường của các tỉnh , thành phố trực thuộc trung ương thực hiện thí điểm không tổ chức **[Hội đồng nhân dân huyện , quận , phường]`<CO_QUAN_THAM_QUYEN>`** ;

**Thực thể:**
- `[e0]` **Nghị quyết số 724/2009/UBTVQH12** → `THAM_CHIEU_PHAP_LY` (span: `[1:4]`)
- `[e1]` **Căn cứ** → `TU_KHOA_PHAP_LY` (span: `[0:1]`)
- `[e2]` **ngày 16 tháng 01 năm 2009** → `NGAY_THAM_CHIEU` (span: `[4:10]`)
- `[e3]` **Ủy ban thường vụ Quốc hội** → `CO_QUAN_THAM_QUYEN` (span: `[11:14]`)
- `[e4]` **Hội đồng nhân dân huyện , quận , phường** → `CO_QUAN_THAM_QUYEN` (span: `[32:39]`)

**Quan hệ:**
- (`e1` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e0` Nghị quyết số 724/2009/UBTVQH12 `[THAM_CHIEU_PHAP_LY]`)
- (`e3` Ủy ban thường vụ Quốc hội `[CO_QUAN_THAM_QUYEN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e0` Nghị quyết số 724/2009/UBTVQH12 `[THAM_CHIEU_PHAP_LY]`)
- (`e0` Nghị quyết số 724/2009/UBTVQH12 `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e2` ngày 16 tháng 01 năm 2009 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #01_2009_TT-BNV_12219#preamble_context_4 (Loại: `preamble_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[01/2009/TT-BNV]`<SO_HIEU>`** của **[Bộ Nội vụ]`<CO_QUAN_BAN_HANH>`** . **[Căn cứ]`<TU_KHOA_PHAP_LY>`** **[Nghị quyết số 725/2009/UBTVQH12]`<THAM_CHIEU_PHAP_LY>`** **[ngày 16 tháng 01 năm 2009]`<NGAY_THAM_CHIEU>`** của **[Ủy ban thường vụ Quốc hội]`<CO_QUAN_THAM_QUYEN>`** về điều chỉnh nhiệm vụ , quyền hạn của **[Hội đồng nhân dân]`<CO_QUAN_THAM_QUYEN>`** , **[Ủy ban nhân dân tỉnh , thành phố trực thuộc trung ương]`<CO_QUAN_THAM_QUYEN>`** và quy định nhiệm vụ , quyền hạn , tổ chức bộ máy của **[Ủy ban nhân dân huyện , quận , phường]`<CO_QUAN_THAM_QUYEN>`** nơi không tổ chức **[Hội đồng nhân dân huyện , quận , phường]`<CO_QUAN_THAM_QUYEN>`** ;

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **01/2009/TT-BNV** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Nội vụ** → `CO_QUAN_BAN_HANH` (span: `[4:6]`)
- `[e3]` **Nghị quyết số 725/2009/UBTVQH12** → `THAM_CHIEU_PHAP_LY` (span: `[8:11]`)
- `[e4]` **Căn cứ** → `TU_KHOA_PHAP_LY` (span: `[7:8]`)
- `[e5]` **ngày 16 tháng 01 năm 2009** → `NGAY_THAM_CHIEU` (span: `[11:17]`)
- `[e6]` **Ủy ban thường vụ Quốc hội** → `CO_QUAN_THAM_QUYEN` (span: `[18:21]`)
- `[e7]` **Hội đồng nhân dân** → `CO_QUAN_THAM_QUYEN` (span: `[27:29]`)
- `[e8]` **Ủy ban nhân dân tỉnh , thành phố trực thuộc trung ương** → `CO_QUAN_THAM_QUYEN` (span: `[30:37]`)
- `[e9]` **Ủy ban nhân dân huyện , quận , phường** → `CO_QUAN_THAM_QUYEN` (span: `[46:53]`)
- `[e10]` **Hội đồng nhân dân huyện , quận , phường** → `CO_QUAN_THAM_QUYEN` (span: `[56:63]`)

**Quan hệ:**
- (`e1` 01/2009/TT-BNV `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Nội vụ `[CO_QUAN_BAN_HANH]`)
- (`e1` 01/2009/TT-BNV `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e4` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Nghị quyết số 725/2009/UBTVQH12 `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 01/2009/TT-BNV `[SO_HIEU]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Nghị quyết số 725/2009/UBTVQH12 `[THAM_CHIEU_PHAP_LY]`)
- (`e3` Nghị quyết số 725/2009/UBTVQH12 `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e5` ngày 16 tháng 01 năm 2009 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #01_2009_TT-BNV_12219#preamble_standalone_5 (Loại: `preamble_standalone`)
> **[Căn cứ]`<TU_KHOA_PHAP_LY>`** **[Nghị quyết số 725/2009/UBTVQH12]`<THAM_CHIEU_PHAP_LY>`** **[ngày 16 tháng 01 năm 2009]`<NGAY_THAM_CHIEU>`** của **[Ủy ban thường vụ Quốc hội]`<CO_QUAN_THAM_QUYEN>`** về điều chỉnh nhiệm vụ , quyền hạn của **[Hội đồng nhân dân]`<CO_QUAN_THAM_QUYEN>`** , **[Ủy ban nhân dân tỉnh , thành phố trực thuộc trung ương]`<CO_QUAN_THAM_QUYEN>`** và quy định nhiệm vụ , quyền hạn , tổ chức bộ máy của **[Ủy ban nhân dân huyện , quận , phường]`<CO_QUAN_THAM_QUYEN>`** nơi không tổ chức **[Hội đồng nhân dân huyện , quận , phường]`<CO_QUAN_THAM_QUYEN>`** ;

**Thực thể:**
- `[e0]` **Nghị quyết số 725/2009/UBTVQH12** → `THAM_CHIEU_PHAP_LY` (span: `[1:4]`)
- `[e1]` **Căn cứ** → `TU_KHOA_PHAP_LY` (span: `[0:1]`)
- `[e2]` **ngày 16 tháng 01 năm 2009** → `NGAY_THAM_CHIEU` (span: `[4:10]`)
- `[e3]` **Ủy ban thường vụ Quốc hội** → `CO_QUAN_THAM_QUYEN` (span: `[11:14]`)
- `[e4]` **Hội đồng nhân dân** → `CO_QUAN_THAM_QUYEN` (span: `[20:22]`)
- `[e5]` **Ủy ban nhân dân tỉnh , thành phố trực thuộc trung ương** → `CO_QUAN_THAM_QUYEN` (span: `[23:30]`)
- `[e6]` **Ủy ban nhân dân huyện , quận , phường** → `CO_QUAN_THAM_QUYEN` (span: `[39:46]`)
- `[e7]` **Hội đồng nhân dân huyện , quận , phường** → `CO_QUAN_THAM_QUYEN` (span: `[49:56]`)

**Quan hệ:**
- (`e1` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e0` Nghị quyết số 725/2009/UBTVQH12 `[THAM_CHIEU_PHAP_LY]`)
- (`e3` Ủy ban thường vụ Quốc hội `[CO_QUAN_THAM_QUYEN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e0` Nghị quyết số 725/2009/UBTVQH12 `[THAM_CHIEU_PHAP_LY]`)
- (`e0` Nghị quyết số 725/2009/UBTVQH12 `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e2` ngày 16 tháng 01 năm 2009 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #01_2009_TT-BNV_12219#preamble_context_6 (Loại: `preamble_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[01/2009/TT-BNV]`<SO_HIEU>`** của **[Bộ Nội vụ]`<CO_QUAN_BAN_HANH>`** . **[Căn cứ]`<TU_KHOA_PHAP_LY>`** **[Nghị định số 107/2004/NĐ-CP]`<THAM_CHIEU_PHAP_LY>`** **[ngày 01 tháng 04 năm 2004]`<NGAY_THAM_CHIEU>`** của **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** quy định số lượng Phó Chủ tịch và cơ cấu thành viên **[Ủy ban nhân dân các cấp]`<CO_QUAN_THAM_QUYEN>`** ; **[Nghị định số 27/2009/NĐ-CP]`<THAM_CHIEU_PHAP_LY>`** **[ngày 19 tháng 3 năm 2009]`<NGAY_THAM_CHIEU>`** của **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** **[sửa đổi , bổ sung]`<TU_KHOA_PHAP_LY>`** **[Nghị định số 107/2004/NĐ-CP]`<THAM_CHIEU_PHAP_LY>`** **[ngày 01 tháng 4 năm 2004]`<NGAY_THAM_CHIEU>`** của **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** quy định số lượng Phó Chủ tịch và cơ cấu thành viên **[Ủy ban nhân dân các cấp]`<CO_QUAN_THAM_QUYEN>`** ;

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **01/2009/TT-BNV** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Nội vụ** → `CO_QUAN_BAN_HANH` (span: `[4:6]`)
- `[e3]` **Nghị định số 107/2004/NĐ-CP** → `THAM_CHIEU_PHAP_LY` (span: `[8:11]`)
- `[e4]` **Nghị định số 27/2009/NĐ-CP** → `THAM_CHIEU_PHAP_LY` (span: `[29:32]`)
- `[e5]` **Nghị định số 107/2004/NĐ-CP** → `THAM_CHIEU_PHAP_LY` (span: `[43:46]`)
- `[e6]` **Căn cứ** → `TU_KHOA_PHAP_LY` (span: `[7:8]`)
- `[e7]` **sửa đổi , bổ sung** → `TU_KHOA_PHAP_LY` (span: `[40:43]`)
- `[e8]` **ngày 01 tháng 04 năm 2004** → `NGAY_THAM_CHIEU` (span: `[11:17]`)
- `[e9]` **ngày 19 tháng 3 năm 2009** → `NGAY_THAM_CHIEU` (span: `[32:38]`)
- `[e10]` **ngày 01 tháng 4 năm 2004** → `NGAY_THAM_CHIEU` (span: `[46:52]`)
- `[e11]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[18:19]`)
- `[e12]` **Ủy ban nhân dân các cấp** → `CO_QUAN_THAM_QUYEN` (span: `[24:28]`)
- `[e13]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[39:40]`)
- `[e14]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[53:54]`)
- `[e15]` **Ủy ban nhân dân các cấp** → `CO_QUAN_THAM_QUYEN` (span: `[59:63]`)

**Quan hệ:**
- (`e1` 01/2009/TT-BNV `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Nội vụ `[CO_QUAN_BAN_HANH]`)
- (`e1` 01/2009/TT-BNV `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e6` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Nghị định số 107/2004/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 01/2009/TT-BNV `[SO_HIEU]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Nghị định số 107/2004/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e6` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e4` Nghị định số 27/2009/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 01/2009/TT-BNV `[SO_HIEU]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e4` Nghị định số 27/2009/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e7` sửa đổi , bổ sung `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e5` Nghị định số 107/2004/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 01/2009/TT-BNV `[SO_HIEU]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e5` Nghị định số 107/2004/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e3` Nghị định số 107/2004/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e8` ngày 01 tháng 04 năm 2004 `[NGAY_THAM_CHIEU]`)
- (`e4` Nghị định số 27/2009/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e9` ngày 19 tháng 3 năm 2009 `[NGAY_THAM_CHIEU]`)
- (`e5` Nghị định số 107/2004/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e10` ngày 01 tháng 4 năm 2004 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #01_2009_TT-BNV_12219#preamble_standalone_7 (Loại: `preamble_standalone`)
> **[Căn cứ]`<TU_KHOA_PHAP_LY>`** **[Nghị định số 107/2004/NĐ-CP]`<THAM_CHIEU_PHAP_LY>`** **[ngày 01 tháng 04 năm 2004]`<NGAY_THAM_CHIEU>`** của **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** quy định số lượng Phó Chủ tịch và cơ cấu thành viên **[Ủy ban nhân dân các cấp]`<CO_QUAN_THAM_QUYEN>`** ; **[Nghị định số 27/2009/NĐ-CP]`<THAM_CHIEU_PHAP_LY>`** **[ngày 19 tháng 3 năm 2009]`<NGAY_THAM_CHIEU>`** của **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** **[sửa đổi , bổ sung]`<TU_KHOA_PHAP_LY>`** **[Nghị định số 107/2004/NĐ-CP]`<THAM_CHIEU_PHAP_LY>`** **[ngày 01 tháng 4 năm 2004]`<NGAY_THAM_CHIEU>`** của **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** quy định số lượng Phó Chủ tịch và cơ cấu thành viên **[Ủy ban nhân dân các cấp]`<CO_QUAN_THAM_QUYEN>`** ;

**Thực thể:**
- `[e0]` **Nghị định số 107/2004/NĐ-CP** → `THAM_CHIEU_PHAP_LY` (span: `[1:4]`)
- `[e1]` **Nghị định số 27/2009/NĐ-CP** → `THAM_CHIEU_PHAP_LY` (span: `[22:25]`)
- `[e2]` **Nghị định số 107/2004/NĐ-CP** → `THAM_CHIEU_PHAP_LY` (span: `[36:39]`)
- `[e3]` **Căn cứ** → `TU_KHOA_PHAP_LY` (span: `[0:1]`)
- `[e4]` **sửa đổi , bổ sung** → `TU_KHOA_PHAP_LY` (span: `[33:36]`)
- `[e5]` **ngày 01 tháng 04 năm 2004** → `NGAY_THAM_CHIEU` (span: `[4:10]`)
- `[e6]` **ngày 19 tháng 3 năm 2009** → `NGAY_THAM_CHIEU` (span: `[25:31]`)
- `[e7]` **ngày 01 tháng 4 năm 2004** → `NGAY_THAM_CHIEU` (span: `[39:45]`)
- `[e8]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[11:12]`)
- `[e9]` **Ủy ban nhân dân các cấp** → `CO_QUAN_THAM_QUYEN` (span: `[17:21]`)
- `[e10]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[32:33]`)
- `[e11]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[46:47]`)
- `[e12]` **Ủy ban nhân dân các cấp** → `CO_QUAN_THAM_QUYEN` (span: `[52:56]`)

**Quan hệ:**
- (`e3` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e0` Nghị định số 107/2004/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e8` Chính phủ `[CO_QUAN_THAM_QUYEN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e0` Nghị định số 107/2004/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e3` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e1` Nghị định số 27/2009/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e9` Ủy ban nhân dân các cấp `[CO_QUAN_THAM_QUYEN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e1` Nghị định số 27/2009/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e4` sửa đổi , bổ sung `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e2` Nghị định số 107/2004/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e10` Chính phủ `[CO_QUAN_THAM_QUYEN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e2` Nghị định số 107/2004/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e0` Nghị định số 107/2004/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e5` ngày 01 tháng 04 năm 2004 `[NGAY_THAM_CHIEU]`)
- (`e1` Nghị định số 27/2009/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e6` ngày 19 tháng 3 năm 2009 `[NGAY_THAM_CHIEU]`)
- (`e2` Nghị định số 107/2004/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e7` ngày 01 tháng 4 năm 2004 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #01_2009_TT-BNV_12219#preamble_context_8 (Loại: `preamble_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[01/2009/TT-BNV]`<SO_HIEU>`** của **[Bộ Nội vụ]`<CO_QUAN_BAN_HANH>`** . **[Căn cứ]`<TU_KHOA_PHAP_LY>`** **[Nghị định số 48/2008/NĐ-CP]`<THAM_CHIEU_PHAP_LY>`** **[ngày 17 tháng 4 năm 2008]`<NGAY_THAM_CHIEU>`** của **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** quy định chức năng , nhiệm vụ , quyền hạn và cơ cấu tổ chức của **[Bộ Nội vụ]`<CO_QUAN_THAM_QUYEN>`** ;

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **01/2009/TT-BNV** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Nội vụ** → `CO_QUAN_BAN_HANH` (span: `[4:6]`)
- `[e3]` **Nghị định số 48/2008/NĐ-CP** → `THAM_CHIEU_PHAP_LY` (span: `[8:11]`)
- `[e4]` **Căn cứ** → `TU_KHOA_PHAP_LY` (span: `[7:8]`)
- `[e5]` **ngày 17 tháng 4 năm 2008** → `NGAY_THAM_CHIEU` (span: `[11:17]`)
- `[e6]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[18:19]`)
- `[e7]` **Bộ Nội vụ** → `CO_QUAN_THAM_QUYEN` (span: `[29:31]`)

**Quan hệ:**
- (`e1` 01/2009/TT-BNV `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Nội vụ `[CO_QUAN_BAN_HANH]`)
- (`e1` 01/2009/TT-BNV `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e4` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Nghị định số 48/2008/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 01/2009/TT-BNV `[SO_HIEU]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Nghị định số 48/2008/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e3` Nghị định số 48/2008/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e5` ngày 17 tháng 4 năm 2008 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #01_2009_TT-BNV_12219#preamble_standalone_9 (Loại: `preamble_standalone`)
> **[Căn cứ]`<TU_KHOA_PHAP_LY>`** **[Nghị định số 48/2008/NĐ-CP]`<THAM_CHIEU_PHAP_LY>`** **[ngày 17 tháng 4 năm 2008]`<NGAY_THAM_CHIEU>`** của **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** quy định chức năng , nhiệm vụ , quyền hạn và cơ cấu tổ chức của **[Bộ Nội vụ]`<CO_QUAN_THAM_QUYEN>`** ;

**Thực thể:**
- `[e0]` **Nghị định số 48/2008/NĐ-CP** → `THAM_CHIEU_PHAP_LY` (span: `[1:4]`)
- `[e1]` **Căn cứ** → `TU_KHOA_PHAP_LY` (span: `[0:1]`)
- `[e2]` **ngày 17 tháng 4 năm 2008** → `NGAY_THAM_CHIEU` (span: `[4:10]`)
- `[e3]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[11:12]`)
- `[e4]` **Bộ Nội vụ** → `CO_QUAN_THAM_QUYEN` (span: `[22:24]`)

**Quan hệ:**
- (`e1` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e0` Nghị định số 48/2008/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e3` Chính phủ `[CO_QUAN_THAM_QUYEN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e0` Nghị định số 48/2008/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e0` Nghị định số 48/2008/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e2` ngày 17 tháng 4 năm 2008 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #01_2009_TT-BNV_12219#preamble_context_10 (Loại: `preamble_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[01/2009/TT-BNV]`<SO_HIEU>`** của **[Bộ Nội vụ]`<CO_QUAN_BAN_HANH>`** . **[Căn cứ]`<TU_KHOA_PHAP_LY>`** **[Quyết định số 241/QĐ-TTg]`<THAM_CHIEU_PHAP_LY>`** **[ngày 23 tháng 02 năm 2009]`<NGAY_THAM_CHIEU>`** của **[Thủ tướng Chính phủ]`<CO_QUAN_THAM_QUYEN>`** phê duyệt Kế hoạch thực hiện **[Nghị quyết số 26/2008/QH12]`<THAM_CHIEU_PHAP_LY>`** **[ngày 15 tháng 11 năm 2008]`<NGAY_THAM_CHIEU>`** của **[Quốc hội]`<CO_QUAN_THAM_QUYEN>`** khóa XII về thực hiện thí điểm không tổ chức **[Hội đồng nhân dân huyện , quận , phường]`<CO_QUAN_THAM_QUYEN>`** .

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **01/2009/TT-BNV** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Nội vụ** → `CO_QUAN_BAN_HANH` (span: `[4:6]`)
- `[e3]` **Quyết định số 241/QĐ-TTg** → `THAM_CHIEU_PHAP_LY` (span: `[8:11]`)
- `[e4]` **Nghị quyết số 26/2008/QH12** → `THAM_CHIEU_PHAP_LY` (span: `[23:26]`)
- `[e5]` **Căn cứ** → `TU_KHOA_PHAP_LY` (span: `[7:8]`)
- `[e6]` **ngày 23 tháng 02 năm 2009** → `NGAY_THAM_CHIEU` (span: `[11:17]`)
- `[e7]` **ngày 15 tháng 11 năm 2008** → `NGAY_THAM_CHIEU` (span: `[26:32]`)
- `[e8]` **Thủ tướng Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[18:20]`)
- `[e9]` **Quốc hội** → `CO_QUAN_THAM_QUYEN` (span: `[33:34]`)
- `[e10]` **Hội đồng nhân dân huyện , quận , phường** → `CO_QUAN_THAM_QUYEN` (span: `[41:48]`)

**Quan hệ:**
- (`e1` 01/2009/TT-BNV `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Nội vụ `[CO_QUAN_BAN_HANH]`)
- (`e1` 01/2009/TT-BNV `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e5` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Quyết định số 241/QĐ-TTg `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 01/2009/TT-BNV `[SO_HIEU]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Quyết định số 241/QĐ-TTg `[THAM_CHIEU_PHAP_LY]`)
- (`e5` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e4` Nghị quyết số 26/2008/QH12 `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 01/2009/TT-BNV `[SO_HIEU]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e4` Nghị quyết số 26/2008/QH12 `[THAM_CHIEU_PHAP_LY]`)
- (`e3` Quyết định số 241/QĐ-TTg `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e6` ngày 23 tháng 02 năm 2009 `[NGAY_THAM_CHIEU]`)
- (`e4` Nghị quyết số 26/2008/QH12 `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e7` ngày 15 tháng 11 năm 2008 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #01_2009_TT-BNV_12219#preamble_standalone_11 (Loại: `preamble_standalone`)
> **[Căn cứ]`<TU_KHOA_PHAP_LY>`** **[Quyết định số 241/QĐ-TTg]`<THAM_CHIEU_PHAP_LY>`** **[ngày 23 tháng 02 năm 2009]`<NGAY_THAM_CHIEU>`** của **[Thủ tướng Chính phủ]`<CO_QUAN_THAM_QUYEN>`** phê duyệt Kế hoạch thực hiện **[Nghị quyết số 26/2008/QH12]`<THAM_CHIEU_PHAP_LY>`** **[ngày 15 tháng 11 năm 2008]`<NGAY_THAM_CHIEU>`** của **[Quốc hội]`<CO_QUAN_THAM_QUYEN>`** khóa XII về thực hiện thí điểm không tổ chức **[Hội đồng nhân dân huyện , quận , phường]`<CO_QUAN_THAM_QUYEN>`** .

**Thực thể:**
- `[e0]` **Quyết định số 241/QĐ-TTg** → `THAM_CHIEU_PHAP_LY` (span: `[1:4]`)
- `[e1]` **Nghị quyết số 26/2008/QH12** → `THAM_CHIEU_PHAP_LY` (span: `[16:19]`)
- `[e2]` **Căn cứ** → `TU_KHOA_PHAP_LY` (span: `[0:1]`)
- `[e3]` **ngày 23 tháng 02 năm 2009** → `NGAY_THAM_CHIEU` (span: `[4:10]`)
- `[e4]` **ngày 15 tháng 11 năm 2008** → `NGAY_THAM_CHIEU` (span: `[19:25]`)
- `[e5]` **Thủ tướng Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[11:13]`)
- `[e6]` **Quốc hội** → `CO_QUAN_THAM_QUYEN` (span: `[26:27]`)
- `[e7]` **Hội đồng nhân dân huyện , quận , phường** → `CO_QUAN_THAM_QUYEN` (span: `[34:41]`)

**Quan hệ:**
- (`e2` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e0` Quyết định số 241/QĐ-TTg `[THAM_CHIEU_PHAP_LY]`)
- (`e5` Thủ tướng Chính phủ `[CO_QUAN_THAM_QUYEN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e0` Quyết định số 241/QĐ-TTg `[THAM_CHIEU_PHAP_LY]`)
- (`e2` Căn cứ `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e1` Nghị quyết số 26/2008/QH12 `[THAM_CHIEU_PHAP_LY]`)
- (`e5` Thủ tướng Chính phủ `[CO_QUAN_THAM_QUYEN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e1` Nghị quyết số 26/2008/QH12 `[THAM_CHIEU_PHAP_LY]`)
- (`e0` Quyết định số 241/QĐ-TTg `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e3` ngày 23 tháng 02 năm 2009 `[NGAY_THAM_CHIEU]`)
- (`e1` Nghị quyết số 26/2008/QH12 `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e4` ngày 15 tháng 11 năm 2008 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #01_2009_TT-BNV_12219#preamble_context_12 (Loại: `preamble_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[01/2009/TT-BNV]`<SO_HIEU>`** của **[Bộ Nội vụ]`<CO_QUAN_BAN_HANH>`** . Sau khi thống nhất với **[Ban Tổ chức Trung ương Đảng]`<CO_QUAN_THAM_QUYEN>`** , **[Bộ Nội vụ]`<CO_QUAN_THAM_QUYEN>`** hướng dẫn trình tự , thủ tục **[bổ nhiệm , miễn nhiệm , cách chức Chủ tịch , Phó Chủ tịch]`<NGHIA_VU_QUYEN>`** , Ủy viên **[Ủy ban nhân dân huyện , quận , phường]`<CO_QUAN_THAM_QUYEN>`** **[nơi thực hiện thí điểm]`<DIA_DIEM>`** không tổ chức **[Hội đồng nhân dân]`<CO_QUAN_THAM_QUYEN>`** ( sau đây gọi chung là **[nơi thực hiện thí điểm]`<DIA_DIEM>`** ) như sau :

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **01/2009/TT-BNV** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Nội vụ** → `CO_QUAN_BAN_HANH` (span: `[4:6]`)
- `[e3]` **bổ nhiệm , miễn nhiệm , cách chức Chủ tịch , Phó Chủ tịch** → `NGHIA_VU_QUYEN` (span: `[22:30]`)
- `[e4]` **Ban Tổ chức Trung ương Đảng** → `CO_QUAN_THAM_QUYEN` (span: `[11:15]`)
- `[e5]` **Bộ Nội vụ** → `CO_QUAN_THAM_QUYEN` (span: `[16:18]`)
- `[e6]` **Ủy ban nhân dân huyện , quận , phường** → `CO_QUAN_THAM_QUYEN` (span: `[32:39]`)
- `[e7]` **Hội đồng nhân dân** → `CO_QUAN_THAM_QUYEN` (span: `[44:46]`)
- `[e8]` **nơi thực hiện thí điểm** → `DIA_DIEM` (span: `[39:42]`)
- `[e9]` **nơi thực hiện thí điểm** → `DIA_DIEM` (span: `[52:55]`)

**Quan hệ:**
- (`e1` 01/2009/TT-BNV `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Nội vụ `[CO_QUAN_BAN_HANH]`)
- (`e1` 01/2009/TT-BNV `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e4` Ban Tổ chức Trung ương Đảng `[CO_QUAN_THAM_QUYEN]`) ==[ **CO_THAM_QUYEN** ]==> (`e3` bổ nhiệm , miễn nhiệm , cách chức Chủ tịch , Phó Chủ tịch `[NGHIA_VU_QUYEN]`)
- (`e5` Bộ Nội vụ `[CO_QUAN_THAM_QUYEN]`) ==[ **CO_THAM_QUYEN** ]==> (`e3` bổ nhiệm , miễn nhiệm , cách chức Chủ tịch , Phó Chủ tịch `[NGHIA_VU_QUYEN]`)
- (`e3` bổ nhiệm , miễn nhiệm , cách chức Chủ tịch , Phó Chủ tịch `[NGHIA_VU_QUYEN]`) ==[ **TAC_DONG_CHU_THE** ]==> (`e6` Ủy ban nhân dân huyện , quận , phường `[CO_QUAN_THAM_QUYEN]`)
- (`e3` bổ nhiệm , miễn nhiệm , cách chức Chủ tịch , Phó Chủ tịch `[NGHIA_VU_QUYEN]`) ==[ **TAC_DONG_CHU_THE** ]==> (`e7` Hội đồng nhân dân `[CO_QUAN_THAM_QUYEN]`)
- (`e3` bổ nhiệm , miễn nhiệm , cách chức Chủ tịch , Phó Chủ tịch `[NGHIA_VU_QUYEN]`) ==[ **DIEN_RA_TAI** ]==> (`e8` nơi thực hiện thí điểm `[DIA_DIEM]`)
- (`e3` bổ nhiệm , miễn nhiệm , cách chức Chủ tịch , Phó Chủ tịch `[NGHIA_VU_QUYEN]`) ==[ **DIEN_RA_TAI** ]==> (`e9` nơi thực hiện thí điểm `[DIA_DIEM]`)


---

### Mẫu #01_2009_TT-BNV_12219#preamble_standalone_13 (Loại: `preamble_standalone`)
> Sau khi thống nhất với **[Ban Tổ chức Trung ương Đảng]`<CO_QUAN_THAM_QUYEN>`** , **[Bộ Nội vụ]`<CO_QUAN_THAM_QUYEN>`** hướng dẫn trình tự , thủ tục **[bổ nhiệm , miễn nhiệm , cách chức Chủ tịch , Phó Chủ tịch]`<NGHIA_VU_QUYEN>`** , Ủy viên **[Ủy ban nhân dân huyện , quận , phường]`<CO_QUAN_THAM_QUYEN>`** **[nơi thực hiện thí điểm]`<DIA_DIEM>`** không tổ chức **[Hội đồng nhân dân]`<CO_QUAN_THAM_QUYEN>`** ( sau đây gọi chung là **[nơi thực hiện thí điểm]`<DIA_DIEM>`** ) như sau :

**Thực thể:**
- `[e0]` **bổ nhiệm , miễn nhiệm , cách chức Chủ tịch , Phó Chủ tịch** → `NGHIA_VU_QUYEN` (span: `[15:23]`)
- `[e1]` **Ban Tổ chức Trung ương Đảng** → `CO_QUAN_THAM_QUYEN` (span: `[4:8]`)
- `[e2]` **Bộ Nội vụ** → `CO_QUAN_THAM_QUYEN` (span: `[9:11]`)
- `[e3]` **Ủy ban nhân dân huyện , quận , phường** → `CO_QUAN_THAM_QUYEN` (span: `[25:32]`)
- `[e4]` **Hội đồng nhân dân** → `CO_QUAN_THAM_QUYEN` (span: `[37:39]`)
- `[e5]` **nơi thực hiện thí điểm** → `DIA_DIEM` (span: `[32:35]`)
- `[e6]` **nơi thực hiện thí điểm** → `DIA_DIEM` (span: `[45:48]`)

**Quan hệ:**
- (`e1` Ban Tổ chức Trung ương Đảng `[CO_QUAN_THAM_QUYEN]`) ==[ **CO_THAM_QUYEN** ]==> (`e0` bổ nhiệm , miễn nhiệm , cách chức Chủ tịch , Phó Chủ tịch `[NGHIA_VU_QUYEN]`)
- (`e2` Bộ Nội vụ `[CO_QUAN_THAM_QUYEN]`) ==[ **CO_THAM_QUYEN** ]==> (`e0` bổ nhiệm , miễn nhiệm , cách chức Chủ tịch , Phó Chủ tịch `[NGHIA_VU_QUYEN]`)
- (`e0` bổ nhiệm , miễn nhiệm , cách chức Chủ tịch , Phó Chủ tịch `[NGHIA_VU_QUYEN]`) ==[ **TAC_DONG_CHU_THE** ]==> (`e3` Ủy ban nhân dân huyện , quận , phường `[CO_QUAN_THAM_QUYEN]`)
- (`e0` bổ nhiệm , miễn nhiệm , cách chức Chủ tịch , Phó Chủ tịch `[NGHIA_VU_QUYEN]`) ==[ **TAC_DONG_CHU_THE** ]==> (`e4` Hội đồng nhân dân `[CO_QUAN_THAM_QUYEN]`)
- (`e0` bổ nhiệm , miễn nhiệm , cách chức Chủ tịch , Phó Chủ tịch `[NGHIA_VU_QUYEN]`) ==[ **DIEN_RA_TAI** ]==> (`e5` nơi thực hiện thí điểm `[DIA_DIEM]`)
- (`e0` bổ nhiệm , miễn nhiệm , cách chức Chủ tịch , Phó Chủ tịch `[NGHIA_VU_QUYEN]`) ==[ **DIEN_RA_TAI** ]==> (`e6` nơi thực hiện thí điểm `[DIA_DIEM]`)


---

### Mẫu #01_2009_TT-BNV_12219#body_context_14 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[01/2009/TT-BNV]`<SO_HIEU>`** ban hành **[ngày 19 tháng 03 năm 2009]`<NGAY_BAN_HANH>`** bởi **[Bộ Nội vụ]`<CO_QUAN_BAN_HANH>`** . **[Điều 1 . Quy định chung]`<DIEU>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **01/2009/TT-BNV** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Nội vụ** → `CO_QUAN_BAN_HANH` (span: `[11:13]`)
- `[e3]` **ngày 19 tháng 03 năm 2009** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 1 . Quy định chung** → `DIEU` (span: `[14:19]`)

**Quan hệ:**
- (`e1` 01/2009/TT-BNV `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Nội vụ `[CO_QUAN_BAN_HANH]`)
- (`e1` 01/2009/TT-BNV `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 01/2009/TT-BNV `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 19 tháng 03 năm 2009 `[NGAY_BAN_HANH]`)
- (`e4` Điều 1 . Quy định chung `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 01/2009/TT-BNV `[SO_HIEU]`)


---

### Mẫu #01_2009_TT-BNV_12219#body_context_15 (Loại: `body_context`)
> **[Bộ Nội vụ]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[01/2009/TT-BNV]`<SO_HIEU>`** . **[Điều 1]`<DIEU>`** . **[1 . Đảm bảo nguyên tắc Đảng thống nhất lãnh đạo công tác **[bổ nhiệm , miễn nhiệm , cách chức Chủ tịch , Phó Chủ tịch]`<NGHIA_VU_QUYEN>`** , Ủy viên **[Ủy ban nhân dân huyện , quận , phường]`<CO_QUAN_THAM_QUYEN>`** **[nơi thực hiện thí điểm]`<DIA_DIEM>`** .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[3:4]`)
- `[e1]` **01/2009/TT-BNV** → `SO_HIEU` (span: `[5:6]`)
- `[e2]` **Bộ Nội vụ** → `CO_QUAN_BAN_HANH` (span: `[0:2]`)
- `[e3]` **Điều 1** → `DIEU` (span: `[7:9]`)
- `[e4]` **1 . Đảm bảo nguyên tắc Đảng thống nhất lãnh đạo công tác bổ nhiệm , miễn nhiệm , cách chức Chủ tịch , Phó Chủ tịch , Ủy viên Ủy ban nhân dân huyện , quận , phường nơi thực hiện thí điểm .** → `KHOAN` (span: `[10:39]`)
- `[e5]` **bổ nhiệm , miễn nhiệm , cách chức Chủ tịch , Phó Chủ tịch** → `NGHIA_VU_QUYEN` (span: `[18:26]`) *(lồng trong `e4` (`KHOAN`))*
- `[e6]` **Ủy ban nhân dân huyện , quận , phường** → `CO_QUAN_THAM_QUYEN` (span: `[28:35]`) *(lồng trong `e4` (`KHOAN`))*
- `[e7]` **nơi thực hiện thí điểm** → `DIA_DIEM` (span: `[35:38]`) *(lồng trong `e4` (`KHOAN`))*

**Quan hệ:**
- (`e1` 01/2009/TT-BNV `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Nội vụ `[CO_QUAN_BAN_HANH]`)
- (`e1` 01/2009/TT-BNV `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 1 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 01/2009/TT-BNV `[SO_HIEU]`)
- (`e4` 1 . Đảm bảo nguyên tắc Đảng thống nhất lãnh đạo công tác bổ nhiệm , miễn nhiệm , cách chức Chủ tịch , Phó Chủ tịch , Ủy viên Ủy ban nhân dân huyện , quận , phường nơi thực hiện thí điểm . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 1 `[DIEU]`)
- (`e5` bổ nhiệm , miễn nhiệm , cách chức Chủ tịch , Phó Chủ tịch `[NGHIA_VU_QUYEN]`) ==[ **TAC_DONG_CHU_THE** ]==> (`e6` Ủy ban nhân dân huyện , quận , phường `[CO_QUAN_THAM_QUYEN]`)
- (`e5` bổ nhiệm , miễn nhiệm , cách chức Chủ tịch , Phó Chủ tịch `[NGHIA_VU_QUYEN]`) ==[ **DIEN_RA_TAI** ]==> (`e7` nơi thực hiện thí điểm `[DIA_DIEM]`)


---

### Mẫu #01_2009_TT-BNV_12219#body_standalone_16 (Loại: `body_standalone`)
> **[Điều 1]`<DIEU>`** . **[1 . Đảm bảo nguyên tắc Đảng thống nhất lãnh đạo công tác **[bổ nhiệm , miễn nhiệm , cách chức Chủ tịch , Phó Chủ tịch]`<NGHIA_VU_QUYEN>`** , Ủy viên **[Ủy ban nhân dân huyện , quận , phường]`<CO_QUAN_THAM_QUYEN>`** **[nơi thực hiện thí điểm]`<DIA_DIEM>`** .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 1** → `DIEU` (span: `[0:2]`)
- `[e1]` **1 . Đảm bảo nguyên tắc Đảng thống nhất lãnh đạo công tác bổ nhiệm , miễn nhiệm , cách chức Chủ tịch , Phó Chủ tịch , Ủy viên Ủy ban nhân dân huyện , quận , phường nơi thực hiện thí điểm .** → `KHOAN` (span: `[3:32]`)
- `[e2]` **bổ nhiệm , miễn nhiệm , cách chức Chủ tịch , Phó Chủ tịch** → `NGHIA_VU_QUYEN` (span: `[11:19]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **Ủy ban nhân dân huyện , quận , phường** → `CO_QUAN_THAM_QUYEN` (span: `[21:28]`) *(lồng trong `e1` (`KHOAN`))*
- `[e4]` **nơi thực hiện thí điểm** → `DIA_DIEM` (span: `[28:31]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 1 . Đảm bảo nguyên tắc Đảng thống nhất lãnh đạo công tác bổ nhiệm , miễn nhiệm , cách chức Chủ tịch , Phó Chủ tịch , Ủy viên Ủy ban nhân dân huyện , quận , phường nơi thực hiện thí điểm . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 1 `[DIEU]`)
- (`e2` bổ nhiệm , miễn nhiệm , cách chức Chủ tịch , Phó Chủ tịch `[NGHIA_VU_QUYEN]`) ==[ **TAC_DONG_CHU_THE** ]==> (`e3` Ủy ban nhân dân huyện , quận , phường `[CO_QUAN_THAM_QUYEN]`)
- (`e2` bổ nhiệm , miễn nhiệm , cách chức Chủ tịch , Phó Chủ tịch `[NGHIA_VU_QUYEN]`) ==[ **DIEN_RA_TAI** ]==> (`e4` nơi thực hiện thí điểm `[DIA_DIEM]`)


---

### Mẫu #01_2009_TT-BNV_12219#body_context_17 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[01/2009/TT-BNV]`<SO_HIEU>`** của **[Bộ Nội vụ]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Nội vụ]`<LINH_VUC>`** . **[Điều 1]`<DIEU>`** . **[2 . **[Người được bổ nhiệm]`<CHU_THE_CA_NHAN>`** phải đạt tiêu chuẩn chung của **[cán bộ , công chức]`<CHU_THE_CA_NHAN>`** và tiêu chuẩn cụ thể của từng chức danh bổ nhiệm theo quy định của Đảng và Nhà nước .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **01/2009/TT-BNV** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Nội vụ** → `CO_QUAN_BAN_HANH` (span: `[4:6]`)
- `[e3]` **Nội vụ** → `LINH_VUC` (span: `[8:9]`)
- `[e4]` **Điều 1** → `DIEU` (span: `[10:12]`)
- `[e5]` **2 . Người được bổ nhiệm phải đạt tiêu chuẩn chung của cán bộ , công chức và tiêu chuẩn cụ thể của từng chức danh bổ nhiệm theo quy định của Đảng và Nhà nước .** → `KHOAN` (span: `[13:40]`)
- `[e6]` **Người được bổ nhiệm** → `CHU_THE_CA_NHAN` (span: `[15:18]`) *(lồng trong `e5` (`KHOAN`))*
- `[e7]` **cán bộ , công chức** → `CHU_THE_CA_NHAN` (span: `[23:26]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 01/2009/TT-BNV `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Nội vụ `[CO_QUAN_BAN_HANH]`)
- (`e1` 01/2009/TT-BNV `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 01/2009/TT-BNV `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Nội vụ `[LINH_VUC]`)
- (`e4` Điều 1 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 01/2009/TT-BNV `[SO_HIEU]`)
- (`e5` 2 . Người được bổ nhiệm phải đạt tiêu chuẩn chung của cán bộ , công chức và tiêu chuẩn cụ thể của từng chức danh bổ nhiệm theo quy định của Đảng và Nhà nước . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 1 `[DIEU]`)
- (`e1` 01/2009/TT-BNV `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Nội vụ `[LINH_VUC]`)
- (`e5` 2 . Người được bổ nhiệm phải đạt tiêu chuẩn chung của cán bộ , công chức và tiêu chuẩn cụ thể của từng chức danh bổ nhiệm theo quy định của Đảng và Nhà nước . `[KHOAN]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Nội vụ `[LINH_VUC]`)


---

### Mẫu #01_2009_TT-BNV_12219#body_standalone_18 (Loại: `body_standalone`)
> **[Điều 1]`<DIEU>`** . **[2 . **[Người được bổ nhiệm]`<CHU_THE_CA_NHAN>`** phải đạt tiêu chuẩn chung của **[cán bộ , công chức]`<CHU_THE_CA_NHAN>`** và tiêu chuẩn cụ thể của từng chức danh bổ nhiệm theo quy định của Đảng và Nhà nước .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 1** → `DIEU` (span: `[0:2]`)
- `[e1]` **2 . Người được bổ nhiệm phải đạt tiêu chuẩn chung của cán bộ , công chức và tiêu chuẩn cụ thể của từng chức danh bổ nhiệm theo quy định của Đảng và Nhà nước .** → `KHOAN` (span: `[3:30]`)
- `[e2]` **Người được bổ nhiệm** → `CHU_THE_CA_NHAN` (span: `[5:8]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **cán bộ , công chức** → `CHU_THE_CA_NHAN` (span: `[13:16]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 2 . Người được bổ nhiệm phải đạt tiêu chuẩn chung của cán bộ , công chức và tiêu chuẩn cụ thể của từng chức danh bổ nhiệm theo quy định của Đảng và Nhà nước . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 1 `[DIEU]`)


---

### Mẫu #01_2009_TT-BNV_12219#body_context_19 (Loại: `body_context`)
> **[Bộ Nội vụ]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[01/2009/TT-BNV]`<SO_HIEU>`** . **[Điều 1]`<DIEU>`** . **[3 . **[Chủ tịch Ủy ban nhân dân tỉnh , thành phố trực thuộc trung ương]`<CO_QUAN_THAM_QUYEN>`** **[bổ nhiệm , miễn nhiệm , cách chức Chủ tịch , Phó Chủ tịch]`<NGHIA_VU_QUYEN>`** , Ủy viên **[Ủy ban nhân dân huyện , quận]`<CO_QUAN_THAM_QUYEN>`** ; **[Chủ tịch Ủy ban nhân dân quận , thị xã , thành phố thuộc tỉnh]`<CO_QUAN_THAM_QUYEN>`** **[bổ nhiệm , miễn nhiệm , cách chức Chủ tịch , Phó Chủ tịch]`<NGHIA_VU_QUYEN>`** , Ủy viên **[Ủy ban nhân dân phường]`<CO_QUAN_THAM_QUYEN>`** .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[3:4]`)
- `[e1]` **01/2009/TT-BNV** → `SO_HIEU` (span: `[5:6]`)
- `[e2]` **Bộ Nội vụ** → `CO_QUAN_BAN_HANH` (span: `[0:2]`)
- `[e3]` **Điều 1** → `DIEU` (span: `[7:9]`)
- `[e4]` **3 . Chủ tịch Ủy ban nhân dân tỉnh , thành phố trực thuộc trung ương bổ nhiệm , miễn nhiệm , cách chức Chủ tịch , Phó Chủ tịch , Ủy viên Ủy ban nhân dân huyện , quận ; Chủ tịch Ủy ban nhân dân quận , thị xã , thành phố thuộc tỉnh bổ nhiệm , miễn nhiệm , cách chức Chủ tịch , Phó Chủ tịch , Ủy viên Ủy ban nhân dân phường .** → `KHOAN` (span: `[10:60]`)
- `[e5]` **bổ nhiệm , miễn nhiệm , cách chức Chủ tịch , Phó Chủ tịch** → `NGHIA_VU_QUYEN` (span: `[20:28]`) *(lồng trong `e4` (`KHOAN`))*
- `[e6]` **bổ nhiệm , miễn nhiệm , cách chức Chủ tịch , Phó Chủ tịch** → `NGHIA_VU_QUYEN` (span: `[46:54]`) *(lồng trong `e4` (`KHOAN`))*
- `[e7]` **Chủ tịch Ủy ban nhân dân tỉnh , thành phố trực thuộc trung ương** → `CO_QUAN_THAM_QUYEN` (span: `[12:20]`) *(lồng trong `e4` (`KHOAN`))*
- `[e8]` **Ủy ban nhân dân huyện , quận** → `CO_QUAN_THAM_QUYEN` (span: `[30:35]`) *(lồng trong `e4` (`KHOAN`))*
- `[e9]` **Chủ tịch Ủy ban nhân dân quận , thị xã , thành phố thuộc tỉnh** → `CO_QUAN_THAM_QUYEN` (span: `[36:46]`) *(lồng trong `e4` (`KHOAN`))*
- `[e10]` **Ủy ban nhân dân phường** → `CO_QUAN_THAM_QUYEN` (span: `[56:59]`) *(lồng trong `e4` (`KHOAN`))*

**Quan hệ:**
- (`e1` 01/2009/TT-BNV `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Nội vụ `[CO_QUAN_BAN_HANH]`)
- (`e1` 01/2009/TT-BNV `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 1 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 01/2009/TT-BNV `[SO_HIEU]`)
- (`e4` 3 . Chủ tịch Ủy ban nhân dân tỉnh , thành phố trực thuộc trung ương bổ nhiệm , miễn nhiệm , cách chức Chủ tịch , Phó Chủ tịch , Ủy viên Ủy ban nhân dân huyện , quận ; Chủ tịch Ủy ban nhân dân quận , thị xã , thành phố thuộc tỉnh bổ nhiệm , miễn nhiệm , cách chức Chủ tịch , Phó Chủ tịch , Ủy viên Ủy ban nhân dân phường . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 1 `[DIEU]`)
- (`e7` Chủ tịch Ủy ban nhân dân tỉnh , thành phố trực thuộc trung ương `[CO_QUAN_THAM_QUYEN]`) ==[ **CO_THAM_QUYEN** ]==> (`e5` bổ nhiệm , miễn nhiệm , cách chức Chủ tịch , Phó Chủ tịch `[NGHIA_VU_QUYEN]`)
- (`e7` Chủ tịch Ủy ban nhân dân tỉnh , thành phố trực thuộc trung ương `[CO_QUAN_THAM_QUYEN]`) ==[ **CO_THAM_QUYEN** ]==> (`e6` bổ nhiệm , miễn nhiệm , cách chức Chủ tịch , Phó Chủ tịch `[NGHIA_VU_QUYEN]`)
- (`e5` bổ nhiệm , miễn nhiệm , cách chức Chủ tịch , Phó Chủ tịch `[NGHIA_VU_QUYEN]`) ==[ **TAC_DONG_CHU_THE** ]==> (`e8` Ủy ban nhân dân huyện , quận `[CO_QUAN_THAM_QUYEN]`)
- (`e8` Ủy ban nhân dân huyện , quận `[CO_QUAN_THAM_QUYEN]`) ==[ **CO_THAM_QUYEN** ]==> (`e6` bổ nhiệm , miễn nhiệm , cách chức Chủ tịch , Phó Chủ tịch `[NGHIA_VU_QUYEN]`)
- (`e5` bổ nhiệm , miễn nhiệm , cách chức Chủ tịch , Phó Chủ tịch `[NGHIA_VU_QUYEN]`) ==[ **TAC_DONG_CHU_THE** ]==> (`e9` Chủ tịch Ủy ban nhân dân quận , thị xã , thành phố thuộc tỉnh `[CO_QUAN_THAM_QUYEN]`)
- (`e9` Chủ tịch Ủy ban nhân dân quận , thị xã , thành phố thuộc tỉnh `[CO_QUAN_THAM_QUYEN]`) ==[ **CO_THAM_QUYEN** ]==> (`e6` bổ nhiệm , miễn nhiệm , cách chức Chủ tịch , Phó Chủ tịch `[NGHIA_VU_QUYEN]`)
- (`e5` bổ nhiệm , miễn nhiệm , cách chức Chủ tịch , Phó Chủ tịch `[NGHIA_VU_QUYEN]`) ==[ **TAC_DONG_CHU_THE** ]==> (`e10` Ủy ban nhân dân phường `[CO_QUAN_THAM_QUYEN]`)
- (`e6` bổ nhiệm , miễn nhiệm , cách chức Chủ tịch , Phó Chủ tịch `[NGHIA_VU_QUYEN]`) ==[ **TAC_DONG_CHU_THE** ]==> (`e10` Ủy ban nhân dân phường `[CO_QUAN_THAM_QUYEN]`)


---

### Mẫu #01_2009_TT-BNV_12219#body_standalone_20 (Loại: `body_standalone`)
> **[Điều 1]`<DIEU>`** . **[3 . **[Chủ tịch Ủy ban nhân dân tỉnh , thành phố trực thuộc trung ương]`<CO_QUAN_THAM_QUYEN>`** **[bổ nhiệm , miễn nhiệm , cách chức Chủ tịch , Phó Chủ tịch]`<NGHIA_VU_QUYEN>`** , Ủy viên **[Ủy ban nhân dân huyện , quận]`<CO_QUAN_THAM_QUYEN>`** ; **[Chủ tịch Ủy ban nhân dân quận , thị xã , thành phố thuộc tỉnh]`<CO_QUAN_THAM_QUYEN>`** **[bổ nhiệm , miễn nhiệm , cách chức Chủ tịch , Phó Chủ tịch]`<NGHIA_VU_QUYEN>`** , Ủy viên **[Ủy ban nhân dân phường]`<CO_QUAN_THAM_QUYEN>`** .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 1** → `DIEU` (span: `[0:2]`)
- `[e1]` **3 . Chủ tịch Ủy ban nhân dân tỉnh , thành phố trực thuộc trung ương bổ nhiệm , miễn nhiệm , cách chức Chủ tịch , Phó Chủ tịch , Ủy viên Ủy ban nhân dân huyện , quận ; Chủ tịch Ủy ban nhân dân quận , thị xã , thành phố thuộc tỉnh bổ nhiệm , miễn nhiệm , cách chức Chủ tịch , Phó Chủ tịch , Ủy viên Ủy ban nhân dân phường .** → `KHOAN` (span: `[3:53]`)
- `[e2]` **bổ nhiệm , miễn nhiệm , cách chức Chủ tịch , Phó Chủ tịch** → `NGHIA_VU_QUYEN` (span: `[13:21]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **bổ nhiệm , miễn nhiệm , cách chức Chủ tịch , Phó Chủ tịch** → `NGHIA_VU_QUYEN` (span: `[39:47]`) *(lồng trong `e1` (`KHOAN`))*
- `[e4]` **Chủ tịch Ủy ban nhân dân tỉnh , thành phố trực thuộc trung ương** → `CO_QUAN_THAM_QUYEN` (span: `[5:13]`) *(lồng trong `e1` (`KHOAN`))*
- `[e5]` **Ủy ban nhân dân huyện , quận** → `CO_QUAN_THAM_QUYEN` (span: `[23:28]`) *(lồng trong `e1` (`KHOAN`))*
- `[e6]` **Chủ tịch Ủy ban nhân dân quận , thị xã , thành phố thuộc tỉnh** → `CO_QUAN_THAM_QUYEN` (span: `[29:39]`) *(lồng trong `e1` (`KHOAN`))*
- `[e7]` **Ủy ban nhân dân phường** → `CO_QUAN_THAM_QUYEN` (span: `[49:52]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 3 . Chủ tịch Ủy ban nhân dân tỉnh , thành phố trực thuộc trung ương bổ nhiệm , miễn nhiệm , cách chức Chủ tịch , Phó Chủ tịch , Ủy viên Ủy ban nhân dân huyện , quận ; Chủ tịch Ủy ban nhân dân quận , thị xã , thành phố thuộc tỉnh bổ nhiệm , miễn nhiệm , cách chức Chủ tịch , Phó Chủ tịch , Ủy viên Ủy ban nhân dân phường . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 1 `[DIEU]`)
- (`e4` Chủ tịch Ủy ban nhân dân tỉnh , thành phố trực thuộc trung ương `[CO_QUAN_THAM_QUYEN]`) ==[ **CO_THAM_QUYEN** ]==> (`e2` bổ nhiệm , miễn nhiệm , cách chức Chủ tịch , Phó Chủ tịch `[NGHIA_VU_QUYEN]`)
- (`e4` Chủ tịch Ủy ban nhân dân tỉnh , thành phố trực thuộc trung ương `[CO_QUAN_THAM_QUYEN]`) ==[ **CO_THAM_QUYEN** ]==> (`e3` bổ nhiệm , miễn nhiệm , cách chức Chủ tịch , Phó Chủ tịch `[NGHIA_VU_QUYEN]`)
- (`e2` bổ nhiệm , miễn nhiệm , cách chức Chủ tịch , Phó Chủ tịch `[NGHIA_VU_QUYEN]`) ==[ **TAC_DONG_CHU_THE** ]==> (`e5` Ủy ban nhân dân huyện , quận `[CO_QUAN_THAM_QUYEN]`)
- (`e5` Ủy ban nhân dân huyện , quận `[CO_QUAN_THAM_QUYEN]`) ==[ **CO_THAM_QUYEN** ]==> (`e3` bổ nhiệm , miễn nhiệm , cách chức Chủ tịch , Phó Chủ tịch `[NGHIA_VU_QUYEN]`)
- (`e2` bổ nhiệm , miễn nhiệm , cách chức Chủ tịch , Phó Chủ tịch `[NGHIA_VU_QUYEN]`) ==[ **TAC_DONG_CHU_THE** ]==> (`e6` Chủ tịch Ủy ban nhân dân quận , thị xã , thành phố thuộc tỉnh `[CO_QUAN_THAM_QUYEN]`)
- (`e6` Chủ tịch Ủy ban nhân dân quận , thị xã , thành phố thuộc tỉnh `[CO_QUAN_THAM_QUYEN]`) ==[ **CO_THAM_QUYEN** ]==> (`e3` bổ nhiệm , miễn nhiệm , cách chức Chủ tịch , Phó Chủ tịch `[NGHIA_VU_QUYEN]`)
- (`e2` bổ nhiệm , miễn nhiệm , cách chức Chủ tịch , Phó Chủ tịch `[NGHIA_VU_QUYEN]`) ==[ **TAC_DONG_CHU_THE** ]==> (`e7` Ủy ban nhân dân phường `[CO_QUAN_THAM_QUYEN]`)
- (`e3` bổ nhiệm , miễn nhiệm , cách chức Chủ tịch , Phó Chủ tịch `[NGHIA_VU_QUYEN]`) ==[ **TAC_DONG_CHU_THE** ]==> (`e7` Ủy ban nhân dân phường `[CO_QUAN_THAM_QUYEN]`)


---

### Mẫu #01_2009_TT-BNV_12219#body_context_21 (Loại: `body_context`)
> **[Bộ Nội vụ]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[01/2009/TT-BNV]`<SO_HIEU>`** . **[Điều 1]`<DIEU>`** . **[4 . Việc bổ nhiệm Chủ tịch , Phó Chủ tịch , Ủy viên **[Ủy ban nhân dân huyện , quận , phường]`<CO_QUAN_THAM_QUYEN>`** **[nơi thực hiện thí điểm]`<DIA_DIEM>`** , về thời hạn bổ nhiệm được áp dụng theo quy định hiện hành . Trong trường hợp **[Quốc hội]`<CO_QUAN_THAM_QUYEN>`** quyết định chấm dứt việc thực hiện thí điểm , thì **[quyết định bổ nhiệm]`<GIAY_TO_HO_SO>`** Chủ tịch , Phó Chủ tịch , Ủy viên **[Ủy ban nhân dân huyện , quận , phường]`<CO_QUAN_THAM_QUYEN>`** **[nơi thực hiện thí điểm]`<DIA_DIEM>`** cũng chấm dứt hiệu lực .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[3:4]`)
- `[e1]` **01/2009/TT-BNV** → `SO_HIEU` (span: `[5:6]`)
- `[e2]` **Bộ Nội vụ** → `CO_QUAN_BAN_HANH` (span: `[0:2]`)
- `[e3]` **Điều 1** → `DIEU` (span: `[7:9]`)
- `[e4]` **4 . Việc bổ nhiệm Chủ tịch , Phó Chủ tịch , Ủy viên Ủy ban nhân dân huyện , quận , phường nơi thực hiện thí điểm , về thời hạn bổ nhiệm được áp dụng theo quy định hiện hành . Trong trường hợp Quốc hội quyết định chấm dứt việc thực hiện thí điểm , thì quyết định bổ nhiệm Chủ tịch , Phó Chủ tịch , Ủy viên Ủy ban nhân dân huyện , quận , phường nơi thực hiện thí điểm cũng chấm dứt hiệu lực .** → `KHOAN` (span: `[10:70]`)
- `[e5]` **Ủy ban nhân dân huyện , quận , phường** → `CO_QUAN_THAM_QUYEN` (span: `[19:26]`) *(lồng trong `e4` (`KHOAN`))*
- `[e6]` **Quốc hội** → `CO_QUAN_THAM_QUYEN` (span: `[41:42]`) *(lồng trong `e4` (`KHOAN`))*
- `[e7]` **Ủy ban nhân dân huyện , quận , phường** → `CO_QUAN_THAM_QUYEN` (span: `[56:63]`) *(lồng trong `e4` (`KHOAN`))*
- `[e8]` **quyết định bổ nhiệm** → `GIAY_TO_HO_SO` (span: `[49:51]`) *(lồng trong `e4` (`KHOAN`))*
- `[e9]` **nơi thực hiện thí điểm** → `DIA_DIEM` (span: `[26:29]`) *(lồng trong `e4` (`KHOAN`))*
- `[e10]` **nơi thực hiện thí điểm** → `DIA_DIEM` (span: `[63:66]`) *(lồng trong `e4` (`KHOAN`))*

**Quan hệ:**
- (`e1` 01/2009/TT-BNV `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Nội vụ `[CO_QUAN_BAN_HANH]`)
- (`e1` 01/2009/TT-BNV `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 1 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 01/2009/TT-BNV `[SO_HIEU]`)
- (`e4` 4 . Việc bổ nhiệm Chủ tịch , Phó Chủ tịch , Ủy viên Ủy ban nhân dân huyện , quận , phường nơi thực hiện thí điểm , về thời hạn bổ nhiệm được áp dụng theo quy định hiện hành . Trong trường hợp Quốc hội quyết định chấm dứt việc thực hiện thí điểm , thì quyết định bổ nhiệm Chủ tịch , Phó Chủ tịch , Ủy viên Ủy ban nhân dân huyện , quận , phường nơi thực hiện thí điểm cũng chấm dứt hiệu lực . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 1 `[DIEU]`)


---

### Mẫu #01_2009_TT-BNV_12219#body_standalone_22 (Loại: `body_standalone`)
> **[Điều 1]`<DIEU>`** . **[4 . Việc bổ nhiệm Chủ tịch , Phó Chủ tịch , Ủy viên **[Ủy ban nhân dân huyện , quận , phường]`<CO_QUAN_THAM_QUYEN>`** **[nơi thực hiện thí điểm]`<DIA_DIEM>`** , về thời hạn bổ nhiệm được áp dụng theo quy định hiện hành . Trong trường hợp **[Quốc hội]`<CO_QUAN_THAM_QUYEN>`** quyết định chấm dứt việc thực hiện thí điểm , thì **[quyết định bổ nhiệm]`<GIAY_TO_HO_SO>`** Chủ tịch , Phó Chủ tịch , Ủy viên **[Ủy ban nhân dân huyện , quận , phường]`<CO_QUAN_THAM_QUYEN>`** **[nơi thực hiện thí điểm]`<DIA_DIEM>`** cũng chấm dứt hiệu lực .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 1** → `DIEU` (span: `[0:2]`)
- `[e1]` **4 . Việc bổ nhiệm Chủ tịch , Phó Chủ tịch , Ủy viên Ủy ban nhân dân huyện , quận , phường nơi thực hiện thí điểm , về thời hạn bổ nhiệm được áp dụng theo quy định hiện hành . Trong trường hợp Quốc hội quyết định chấm dứt việc thực hiện thí điểm , thì quyết định bổ nhiệm Chủ tịch , Phó Chủ tịch , Ủy viên Ủy ban nhân dân huyện , quận , phường nơi thực hiện thí điểm cũng chấm dứt hiệu lực .** → `KHOAN` (span: `[3:63]`)
- `[e2]` **Ủy ban nhân dân huyện , quận , phường** → `CO_QUAN_THAM_QUYEN` (span: `[12:19]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **Quốc hội** → `CO_QUAN_THAM_QUYEN` (span: `[34:35]`) *(lồng trong `e1` (`KHOAN`))*
- `[e4]` **Ủy ban nhân dân huyện , quận , phường** → `CO_QUAN_THAM_QUYEN` (span: `[49:56]`) *(lồng trong `e1` (`KHOAN`))*
- `[e5]` **quyết định bổ nhiệm** → `GIAY_TO_HO_SO` (span: `[42:44]`) *(lồng trong `e1` (`KHOAN`))*
- `[e6]` **nơi thực hiện thí điểm** → `DIA_DIEM` (span: `[19:22]`) *(lồng trong `e1` (`KHOAN`))*
- `[e7]` **nơi thực hiện thí điểm** → `DIA_DIEM` (span: `[56:59]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 4 . Việc bổ nhiệm Chủ tịch , Phó Chủ tịch , Ủy viên Ủy ban nhân dân huyện , quận , phường nơi thực hiện thí điểm , về thời hạn bổ nhiệm được áp dụng theo quy định hiện hành . Trong trường hợp Quốc hội quyết định chấm dứt việc thực hiện thí điểm , thì quyết định bổ nhiệm Chủ tịch , Phó Chủ tịch , Ủy viên Ủy ban nhân dân huyện , quận , phường nơi thực hiện thí điểm cũng chấm dứt hiệu lực . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 1 `[DIEU]`)


---

### Mẫu #01_2009_TT-BNV_12219#body_context_23 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[01/2009/TT-BNV]`<SO_HIEU>`** ban hành **[ngày 19 tháng 03 năm 2009]`<NGAY_BAN_HANH>`** bởi **[Bộ Nội vụ]`<CO_QUAN_BAN_HANH>`** . **[Điều 1]`<DIEU>`** . **[5 . Trường hợp Bí thư cấp ủy nơi thí điểm Bí thư đồng thời là **[Chủ tịch Ủy ban nhân dân huyện , quận , phường]`<CO_QUAN_THAM_QUYEN>`** cũng thực hiện trình tự , thủ tục bổ nhiệm Chủ tịch Ủy ban nhân dân theo hướng dẫn tại Thông tư này .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **01/2009/TT-BNV** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Nội vụ** → `CO_QUAN_BAN_HANH` (span: `[11:13]`)
- `[e3]` **ngày 19 tháng 03 năm 2009** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 1** → `DIEU` (span: `[14:16]`)
- `[e5]` **5 . Trường hợp Bí thư cấp ủy nơi thí điểm Bí thư đồng thời là Chủ tịch Ủy ban nhân dân huyện , quận , phường cũng thực hiện trình tự , thủ tục bổ nhiệm Chủ tịch Ủy ban nhân dân theo hướng dẫn tại Thông tư này .** → `KHOAN` (span: `[17:51]`)
- `[e6]` **Chủ tịch Ủy ban nhân dân huyện , quận , phường** → `CO_QUAN_THAM_QUYEN` (span: `[28:36]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 01/2009/TT-BNV `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Nội vụ `[CO_QUAN_BAN_HANH]`)
- (`e1` 01/2009/TT-BNV `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 01/2009/TT-BNV `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 19 tháng 03 năm 2009 `[NGAY_BAN_HANH]`)
- (`e4` Điều 1 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 01/2009/TT-BNV `[SO_HIEU]`)
- (`e5` 5 . Trường hợp Bí thư cấp ủy nơi thí điểm Bí thư đồng thời là Chủ tịch Ủy ban nhân dân huyện , quận , phường cũng thực hiện trình tự , thủ tục bổ nhiệm Chủ tịch Ủy ban nhân dân theo hướng dẫn tại Thông tư này . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 1 `[DIEU]`)


---

### Mẫu #01_2009_TT-BNV_12219#body_standalone_24 (Loại: `body_standalone`)
> **[Điều 1]`<DIEU>`** . **[5 . Trường hợp Bí thư cấp ủy nơi thí điểm Bí thư đồng thời là **[Chủ tịch Ủy ban nhân dân huyện , quận , phường]`<CO_QUAN_THAM_QUYEN>`** cũng thực hiện trình tự , thủ tục bổ nhiệm Chủ tịch Ủy ban nhân dân theo hướng dẫn tại Thông tư này .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 1** → `DIEU` (span: `[0:2]`)
- `[e1]` **5 . Trường hợp Bí thư cấp ủy nơi thí điểm Bí thư đồng thời là Chủ tịch Ủy ban nhân dân huyện , quận , phường cũng thực hiện trình tự , thủ tục bổ nhiệm Chủ tịch Ủy ban nhân dân theo hướng dẫn tại Thông tư này .** → `KHOAN` (span: `[3:37]`)
- `[e2]` **Chủ tịch Ủy ban nhân dân huyện , quận , phường** → `CO_QUAN_THAM_QUYEN` (span: `[14:22]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 5 . Trường hợp Bí thư cấp ủy nơi thí điểm Bí thư đồng thời là Chủ tịch Ủy ban nhân dân huyện , quận , phường cũng thực hiện trình tự , thủ tục bổ nhiệm Chủ tịch Ủy ban nhân dân theo hướng dẫn tại Thông tư này . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 1 `[DIEU]`)


---

### Mẫu #01_2009_TT-BNV_12219#body_context_25 (Loại: `body_context`)
> **[Bộ Nội vụ]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[01/2009/TT-BNV]`<SO_HIEU>`** . **[Điều 2 . Trình tự , thủ tục bổ nhiệm]`<DIEU>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[3:4]`)
- `[e1]` **01/2009/TT-BNV** → `SO_HIEU` (span: `[5:6]`)
- `[e2]` **Bộ Nội vụ** → `CO_QUAN_BAN_HANH` (span: `[0:2]`)
- `[e3]` **Điều 2 . Trình tự , thủ tục bổ nhiệm** → `DIEU` (span: `[7:14]`)

**Quan hệ:**
- (`e1` 01/2009/TT-BNV `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Nội vụ `[CO_QUAN_BAN_HANH]`)
- (`e1` 01/2009/TT-BNV `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 2 . Trình tự , thủ tục bổ nhiệm `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 01/2009/TT-BNV `[SO_HIEU]`)


---

### Mẫu #01_2009_TT-BNV_12219#body_context_26 (Loại: `body_context`)
> **[Bộ Nội vụ]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[01/2009/TT-BNV]`<SO_HIEU>`** . **[Điều 2]`<DIEU>`** . **[1 . Bổ nhiệm **[Chủ tịch Ủy ban nhân dân huyện , quận , phường]`<CO_QUAN_THAM_QUYEN>`**]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[3:4]`)
- `[e1]` **01/2009/TT-BNV** → `SO_HIEU` (span: `[5:6]`)
- `[e2]` **Bộ Nội vụ** → `CO_QUAN_BAN_HANH` (span: `[0:2]`)
- `[e3]` **Điều 2** → `DIEU` (span: `[7:9]`)
- `[e4]` **1 . Bổ nhiệm Chủ tịch Ủy ban nhân dân huyện , quận , phường** → `KHOAN` (span: `[10:21]`)
- `[e5]` **Chủ tịch Ủy ban nhân dân huyện , quận , phường** → `CO_QUAN_THAM_QUYEN` (span: `[13:21]`) *(lồng trong `e4` (`KHOAN`))*

**Quan hệ:**
- (`e1` 01/2009/TT-BNV `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Nội vụ `[CO_QUAN_BAN_HANH]`)
- (`e1` 01/2009/TT-BNV `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 2 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 01/2009/TT-BNV `[SO_HIEU]`)
- (`e4` 1 . Bổ nhiệm Chủ tịch Ủy ban nhân dân huyện , quận , phường `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 2 `[DIEU]`)


---

### Mẫu #01_2009_TT-BNV_12219#body_context_27 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[01/2009/TT-BNV]`<SO_HIEU>`** ban hành **[ngày 19 tháng 03 năm 2009]`<NGAY_BAN_HANH>`** bởi **[Bộ Nội vụ]`<CO_QUAN_BAN_HANH>`** . **[Điều 2]`<DIEU>`** . **[Khoản 1]`<KHOAN>`** . **[a ) Căn cứ **[thông báo bằng văn bản]`<GIAY_TO_HO_SO>`** về chủ trương của **[cấp có thẩm quyền quản lý cán bộ]`<CO_QUAN_THAM_QUYEN>`** , **[Ủy ban nhân dân huyện , quận , phường]`<CO_QUAN_THAM_QUYEN>`** đương nhiệm **[giới thiệu nhân sự **[Chủ tịch Ủy ban nhân dân cùng cấp]`<CO_QUAN_THAM_QUYEN>`**]`<NGHIA_VU_QUYEN>`** ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **01/2009/TT-BNV** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Nội vụ** → `CO_QUAN_BAN_HANH` (span: `[11:13]`)
- `[e3]` **ngày 19 tháng 03 năm 2009** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 2** → `DIEU` (span: `[14:16]`)
- `[e5]` **Khoản 1** → `KHOAN` (span: `[17:19]`)
- `[e6]` **a ) Căn cứ thông báo bằng văn bản về chủ trương của cấp có thẩm quyền quản lý cán bộ , Ủy ban nhân dân huyện , quận , phường đương nhiệm giới thiệu nhân sự Chủ tịch Ủy ban nhân dân cùng cấp ;** → `DIEM` (span: `[20:51]`)
- `[e7]` **giới thiệu nhân sự Chủ tịch Ủy ban nhân dân cùng cấp** → `NGHIA_VU_QUYEN` (span: `[43:50]`) *(lồng trong `e6` (`DIEM`))*
- `[e8]` **cấp có thẩm quyền quản lý cán bộ** → `CO_QUAN_THAM_QUYEN` (span: `[29:34]`) *(lồng trong `e6` (`DIEM`))*
- `[e9]` **Ủy ban nhân dân huyện , quận , phường** → `CO_QUAN_THAM_QUYEN` (span: `[35:42]`) *(lồng trong `e6` (`DIEM`))*
- `[e10]` **Chủ tịch Ủy ban nhân dân cùng cấp** → `CO_QUAN_THAM_QUYEN` (span: `[45:50]`) *(lồng trong `e6` (`DIEM`), `e7` (`NGHIA_VU_QUYEN`))*
- `[e11]` **thông báo bằng văn bản** → `GIAY_TO_HO_SO` (span: `[23:26]`) *(lồng trong `e6` (`DIEM`))*

**Quan hệ:**
- (`e1` 01/2009/TT-BNV `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Nội vụ `[CO_QUAN_BAN_HANH]`)
- (`e1` 01/2009/TT-BNV `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 01/2009/TT-BNV `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 19 tháng 03 năm 2009 `[NGAY_BAN_HANH]`)
- (`e4` Điều 2 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 01/2009/TT-BNV `[SO_HIEU]`)
- (`e5` Khoản 1 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 2 `[DIEU]`)
- (`e6` a ) Căn cứ thông báo bằng văn bản về chủ trương của cấp có thẩm quyền quản lý cán bộ , Ủy ban nhân dân huyện , quận , phường đương nhiệm giới thiệu nhân sự Chủ tịch Ủy ban nhân dân cùng cấp ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e5` Khoản 1 `[KHOAN]`)
- (`e7` giới thiệu nhân sự Chủ tịch Ủy ban nhân dân cùng cấp `[NGHIA_VU_QUYEN]`) ==[ **TAC_DONG_CHU_THE** ]==> (`e10` Chủ tịch Ủy ban nhân dân cùng cấp `[CO_QUAN_THAM_QUYEN]`) *(Quan hệ lồng nhau)*
- (`e8` cấp có thẩm quyền quản lý cán bộ `[CO_QUAN_THAM_QUYEN]`) ==[ **CO_THAM_QUYEN** ]==> (`e7` giới thiệu nhân sự Chủ tịch Ủy ban nhân dân cùng cấp `[NGHIA_VU_QUYEN]`)
- (`e9` Ủy ban nhân dân huyện , quận , phường `[CO_QUAN_THAM_QUYEN]`) ==[ **CO_THAM_QUYEN** ]==> (`e7` giới thiệu nhân sự Chủ tịch Ủy ban nhân dân cùng cấp `[NGHIA_VU_QUYEN]`)
- (`e7` giới thiệu nhân sự Chủ tịch Ủy ban nhân dân cùng cấp `[NGHIA_VU_QUYEN]`) ==[ **TAC_DONG_DOI_TUONG** ]==> (`e11` thông báo bằng văn bản `[GIAY_TO_HO_SO]`)


---

### Mẫu #01_2009_TT-BNV_12219#body_standalone_28 (Loại: `body_standalone`)
> **[Điều 2]`<DIEU>`** . **[Khoản 1]`<KHOAN>`** . **[a ) Căn cứ **[thông báo bằng văn bản]`<GIAY_TO_HO_SO>`** về chủ trương của **[cấp có thẩm quyền quản lý cán bộ]`<CO_QUAN_THAM_QUYEN>`** , **[Ủy ban nhân dân huyện , quận , phường]`<CO_QUAN_THAM_QUYEN>`** đương nhiệm **[giới thiệu nhân sự **[Chủ tịch Ủy ban nhân dân cùng cấp]`<CO_QUAN_THAM_QUYEN>`**]`<NGHIA_VU_QUYEN>`** ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Điều 2** → `DIEU` (span: `[0:2]`)
- `[e1]` **Khoản 1** → `KHOAN` (span: `[3:5]`)
- `[e2]` **a ) Căn cứ thông báo bằng văn bản về chủ trương của cấp có thẩm quyền quản lý cán bộ , Ủy ban nhân dân huyện , quận , phường đương nhiệm giới thiệu nhân sự Chủ tịch Ủy ban nhân dân cùng cấp ;** → `DIEM` (span: `[6:37]`)
- `[e3]` **giới thiệu nhân sự Chủ tịch Ủy ban nhân dân cùng cấp** → `NGHIA_VU_QUYEN` (span: `[29:36]`) *(lồng trong `e2` (`DIEM`))*
- `[e4]` **cấp có thẩm quyền quản lý cán bộ** → `CO_QUAN_THAM_QUYEN` (span: `[15:20]`) *(lồng trong `e2` (`DIEM`))*
- `[e5]` **Ủy ban nhân dân huyện , quận , phường** → `CO_QUAN_THAM_QUYEN` (span: `[21:28]`) *(lồng trong `e2` (`DIEM`))*
- `[e6]` **Chủ tịch Ủy ban nhân dân cùng cấp** → `CO_QUAN_THAM_QUYEN` (span: `[31:36]`) *(lồng trong `e2` (`DIEM`), `e3` (`NGHIA_VU_QUYEN`))*
- `[e7]` **thông báo bằng văn bản** → `GIAY_TO_HO_SO` (span: `[9:12]`) *(lồng trong `e2` (`DIEM`))*

**Quan hệ:**
- (`e1` Khoản 1 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 2 `[DIEU]`)
- (`e2` a ) Căn cứ thông báo bằng văn bản về chủ trương của cấp có thẩm quyền quản lý cán bộ , Ủy ban nhân dân huyện , quận , phường đương nhiệm giới thiệu nhân sự Chủ tịch Ủy ban nhân dân cùng cấp ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e1` Khoản 1 `[KHOAN]`)
- (`e3` giới thiệu nhân sự Chủ tịch Ủy ban nhân dân cùng cấp `[NGHIA_VU_QUYEN]`) ==[ **TAC_DONG_CHU_THE** ]==> (`e6` Chủ tịch Ủy ban nhân dân cùng cấp `[CO_QUAN_THAM_QUYEN]`) *(Quan hệ lồng nhau)*
- (`e4` cấp có thẩm quyền quản lý cán bộ `[CO_QUAN_THAM_QUYEN]`) ==[ **CO_THAM_QUYEN** ]==> (`e3` giới thiệu nhân sự Chủ tịch Ủy ban nhân dân cùng cấp `[NGHIA_VU_QUYEN]`)
- (`e5` Ủy ban nhân dân huyện , quận , phường `[CO_QUAN_THAM_QUYEN]`) ==[ **CO_THAM_QUYEN** ]==> (`e3` giới thiệu nhân sự Chủ tịch Ủy ban nhân dân cùng cấp `[NGHIA_VU_QUYEN]`)
- (`e3` giới thiệu nhân sự Chủ tịch Ủy ban nhân dân cùng cấp `[NGHIA_VU_QUYEN]`) ==[ **TAC_DONG_DOI_TUONG** ]==> (`e7` thông báo bằng văn bản `[GIAY_TO_HO_SO]`)


---

### Mẫu #01_2009_TT-BNV_12219#body_context_29 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[01/2009/TT-BNV]`<SO_HIEU>`** ban hành **[ngày 19 tháng 03 năm 2009]`<NGAY_BAN_HANH>`** bởi **[Bộ Nội vụ]`<CO_QUAN_BAN_HANH>`** . **[Điều 2]`<DIEU>`** . **[Khoản 1]`<KHOAN>`** . **[b ) Các cơ quan chức năng làm công tác tổ chức **[cán bộ]`<CHU_THE_CA_NHAN>`** tham mưu giúp **[cấp có thẩm quyền quản lý cán bộ]`<CO_QUAN_THAM_QUYEN>`** tiến hành quy trình nhân sự theo quy định hiện hành ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **01/2009/TT-BNV** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Nội vụ** → `CO_QUAN_BAN_HANH` (span: `[11:13]`)
- `[e3]` **ngày 19 tháng 03 năm 2009** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 2** → `DIEU` (span: `[14:16]`)
- `[e5]` **Khoản 1** → `KHOAN` (span: `[17:19]`)
- `[e6]` **b ) Các cơ quan chức năng làm công tác tổ chức cán bộ tham mưu giúp cấp có thẩm quyền quản lý cán bộ tiến hành quy trình nhân sự theo quy định hiện hành ;** → `DIEM` (span: `[20:42]`)
- `[e7]` **cấp có thẩm quyền quản lý cán bộ** → `CO_QUAN_THAM_QUYEN` (span: `[30:35]`) *(lồng trong `e6` (`DIEM`))*
- `[e8]` **cán bộ** → `CHU_THE_CA_NHAN` (span: `[27:28]`) *(lồng trong `e6` (`DIEM`))*

**Quan hệ:**
- (`e1` 01/2009/TT-BNV `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Nội vụ `[CO_QUAN_BAN_HANH]`)
- (`e1` 01/2009/TT-BNV `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 01/2009/TT-BNV `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 19 tháng 03 năm 2009 `[NGAY_BAN_HANH]`)
- (`e4` Điều 2 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 01/2009/TT-BNV `[SO_HIEU]`)
- (`e5` Khoản 1 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 2 `[DIEU]`)
- (`e6` b ) Các cơ quan chức năng làm công tác tổ chức cán bộ tham mưu giúp cấp có thẩm quyền quản lý cán bộ tiến hành quy trình nhân sự theo quy định hiện hành ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e5` Khoản 1 `[KHOAN]`)


---

### Mẫu #01_2009_TT-BNV_12219#body_standalone_30 (Loại: `body_standalone`)
> **[Điều 2]`<DIEU>`** . **[Khoản 1]`<KHOAN>`** . **[b ) Các cơ quan chức năng làm công tác tổ chức **[cán bộ]`<CHU_THE_CA_NHAN>`** tham mưu giúp **[cấp có thẩm quyền quản lý cán bộ]`<CO_QUAN_THAM_QUYEN>`** tiến hành quy trình nhân sự theo quy định hiện hành ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Điều 2** → `DIEU` (span: `[0:2]`)
- `[e1]` **Khoản 1** → `KHOAN` (span: `[3:5]`)
- `[e2]` **b ) Các cơ quan chức năng làm công tác tổ chức cán bộ tham mưu giúp cấp có thẩm quyền quản lý cán bộ tiến hành quy trình nhân sự theo quy định hiện hành ;** → `DIEM` (span: `[6:28]`)
- `[e3]` **cấp có thẩm quyền quản lý cán bộ** → `CO_QUAN_THAM_QUYEN` (span: `[16:21]`) *(lồng trong `e2` (`DIEM`))*
- `[e4]` **cán bộ** → `CHU_THE_CA_NHAN` (span: `[13:14]`) *(lồng trong `e2` (`DIEM`))*

**Quan hệ:**
- (`e1` Khoản 1 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 2 `[DIEU]`)
- (`e2` b ) Các cơ quan chức năng làm công tác tổ chức cán bộ tham mưu giúp cấp có thẩm quyền quản lý cán bộ tiến hành quy trình nhân sự theo quy định hiện hành ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e1` Khoản 1 `[KHOAN]`)


---

### Mẫu #01_2009_TT-BNV_12219#body_context_31 (Loại: `body_context`)
> **[Bộ Nội vụ]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[01/2009/TT-BNV]`<SO_HIEU>`** . **[Điều 2]`<DIEU>`** . **[Khoản 1]`<KHOAN>`** . **[c ) **[Cấp có thẩm quyền quản lý cán bộ]`<CO_QUAN_THAM_QUYEN>`** xem xét , kết luận và có ý kiến đồng ý bằng văn bản ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[3:4]`)
- `[e1]` **01/2009/TT-BNV** → `SO_HIEU` (span: `[5:6]`)
- `[e2]` **Bộ Nội vụ** → `CO_QUAN_BAN_HANH` (span: `[0:2]`)
- `[e3]` **Điều 2** → `DIEU` (span: `[7:9]`)
- `[e4]` **Khoản 1** → `KHOAN` (span: `[10:12]`)
- `[e5]` **c ) Cấp có thẩm quyền quản lý cán bộ xem xét , kết luận và có ý kiến đồng ý bằng văn bản ;** → `DIEM` (span: `[13:30]`)
- `[e6]` **Cấp có thẩm quyền quản lý cán bộ** → `CO_QUAN_THAM_QUYEN` (span: `[15:20]`) *(lồng trong `e5` (`DIEM`))*

**Quan hệ:**
- (`e1` 01/2009/TT-BNV `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Nội vụ `[CO_QUAN_BAN_HANH]`)
- (`e1` 01/2009/TT-BNV `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 2 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 01/2009/TT-BNV `[SO_HIEU]`)
- (`e4` Khoản 1 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 2 `[DIEU]`)
- (`e5` c ) Cấp có thẩm quyền quản lý cán bộ xem xét , kết luận và có ý kiến đồng ý bằng văn bản ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e4` Khoản 1 `[KHOAN]`)


---

### Mẫu #01_2009_TT-BNV_12219#body_context_32 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[01/2009/TT-BNV]`<SO_HIEU>`** của **[Bộ Nội vụ]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Nội vụ]`<LINH_VUC>`** . **[Điều 2]`<DIEU>`** . **[Khoản 1]`<KHOAN>`** . **[d ) Căn cứ **[thông báo bằng văn bản]`<GIAY_TO_HO_SO>`** của **[cấp có thẩm quyền quản lý cán bộ]`<CO_QUAN_THAM_QUYEN>`** , **[Sở Nội vụ]`<CO_QUAN_THAM_QUYEN>`** hoàn chỉnh **[hồ sơ trình]`<GIAY_TO_HO_SO>`** **[Chủ tịch Ủy ban nhân dân tỉnh , thành phố trực thuộc trung ương]`<CO_QUAN_THAM_QUYEN>`** bổ nhiệm **[Chủ tịch Ủy ban nhân dân huyện , quận]`<CO_QUAN_THAM_QUYEN>`** ; **[Phòng Nội vụ]`<CO_QUAN_THAM_QUYEN>`** hoàn chỉnh **[hồ sơ trình]`<GIAY_TO_HO_SO>`** **[Chủ tịch Ủy ban nhân dân quận , thị xã , thành phố thuộc tỉnh]`<CO_QUAN_THAM_QUYEN>`** bổ nhiệm **[Chủ tịch Ủy ban nhân dân phường]`<CO_QUAN_THAM_QUYEN>`** .]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **01/2009/TT-BNV** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Nội vụ** → `CO_QUAN_BAN_HANH` (span: `[4:6]`)
- `[e3]` **Nội vụ** → `LINH_VUC` (span: `[8:9]`)
- `[e4]` **Điều 2** → `DIEU` (span: `[10:12]`)
- `[e5]` **Khoản 1** → `KHOAN` (span: `[13:15]`)
- `[e6]` **d ) Căn cứ thông báo bằng văn bản của cấp có thẩm quyền quản lý cán bộ , Sở Nội vụ hoàn chỉnh hồ sơ trình Chủ tịch Ủy ban nhân dân tỉnh , thành phố trực thuộc trung ương bổ nhiệm Chủ tịch Ủy ban nhân dân huyện , quận ; Phòng Nội vụ hoàn chỉnh hồ sơ trình Chủ tịch Ủy ban nhân dân quận , thị xã , thành phố thuộc tỉnh bổ nhiệm Chủ tịch Ủy ban nhân dân phường .** → `DIEM` (span: `[16:69]`)
- `[e7]` **cấp có thẩm quyền quản lý cán bộ** → `CO_QUAN_THAM_QUYEN` (span: `[23:28]`) *(lồng trong `e6` (`DIEM`))*
- `[e8]` **Sở Nội vụ** → `CO_QUAN_THAM_QUYEN` (span: `[29:31]`) *(lồng trong `e6` (`DIEM`))*
- `[e9]` **Chủ tịch Ủy ban nhân dân tỉnh , thành phố trực thuộc trung ương** → `CO_QUAN_THAM_QUYEN` (span: `[33:41]`) *(lồng trong `e6` (`DIEM`))*
- `[e10]` **Chủ tịch Ủy ban nhân dân huyện , quận** → `CO_QUAN_THAM_QUYEN` (span: `[42:48]`) *(lồng trong `e6` (`DIEM`))*
- `[e11]` **Phòng Nội vụ** → `CO_QUAN_THAM_QUYEN` (span: `[49:51]`) *(lồng trong `e6` (`DIEM`))*
- `[e12]` **Chủ tịch Ủy ban nhân dân quận , thị xã , thành phố thuộc tỉnh** → `CO_QUAN_THAM_QUYEN` (span: `[53:63]`) *(lồng trong `e6` (`DIEM`))*
- `[e13]` **Chủ tịch Ủy ban nhân dân phường** → `CO_QUAN_THAM_QUYEN` (span: `[64:68]`) *(lồng trong `e6` (`DIEM`))*
- `[e14]` **thông báo bằng văn bản** → `GIAY_TO_HO_SO` (span: `[19:22]`) *(lồng trong `e6` (`DIEM`))*
- `[e15]` **hồ sơ trình** → `GIAY_TO_HO_SO` (span: `[32:33]`) *(lồng trong `e6` (`DIEM`))*
- `[e16]` **hồ sơ trình** → `GIAY_TO_HO_SO` (span: `[52:53]`) *(lồng trong `e6` (`DIEM`))*

**Quan hệ:**
- (`e1` 01/2009/TT-BNV `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Nội vụ `[CO_QUAN_BAN_HANH]`)
- (`e1` 01/2009/TT-BNV `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 01/2009/TT-BNV `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Nội vụ `[LINH_VUC]`)
- (`e4` Điều 2 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 01/2009/TT-BNV `[SO_HIEU]`)
- (`e5` Khoản 1 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 2 `[DIEU]`)
- (`e6` d ) Căn cứ thông báo bằng văn bản của cấp có thẩm quyền quản lý cán bộ , Sở Nội vụ hoàn chỉnh hồ sơ trình Chủ tịch Ủy ban nhân dân tỉnh , thành phố trực thuộc trung ương bổ nhiệm Chủ tịch Ủy ban nhân dân huyện , quận ; Phòng Nội vụ hoàn chỉnh hồ sơ trình Chủ tịch Ủy ban nhân dân quận , thị xã , thành phố thuộc tỉnh bổ nhiệm Chủ tịch Ủy ban nhân dân phường . `[DIEM]`) ==[ **THUOC_VE** ]==> (`e5` Khoản 1 `[KHOAN]`)
- (`e1` 01/2009/TT-BNV `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Nội vụ `[LINH_VUC]`)
- (`e6` d ) Căn cứ thông báo bằng văn bản của cấp có thẩm quyền quản lý cán bộ , Sở Nội vụ hoàn chỉnh hồ sơ trình Chủ tịch Ủy ban nhân dân tỉnh , thành phố trực thuộc trung ương bổ nhiệm Chủ tịch Ủy ban nhân dân huyện , quận ; Phòng Nội vụ hoàn chỉnh hồ sơ trình Chủ tịch Ủy ban nhân dân quận , thị xã , thành phố thuộc tỉnh bổ nhiệm Chủ tịch Ủy ban nhân dân phường . `[DIEM]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Nội vụ `[LINH_VUC]`)


---

### Mẫu #01_2009_TT-BNV_12219#body_standalone_33 (Loại: `body_standalone`)
> **[Điều 2]`<DIEU>`** . **[Khoản 1]`<KHOAN>`** . **[d ) Căn cứ **[thông báo bằng văn bản]`<GIAY_TO_HO_SO>`** của **[cấp có thẩm quyền quản lý cán bộ]`<CO_QUAN_THAM_QUYEN>`** , **[Sở Nội vụ]`<CO_QUAN_THAM_QUYEN>`** hoàn chỉnh **[hồ sơ trình]`<GIAY_TO_HO_SO>`** **[Chủ tịch Ủy ban nhân dân tỉnh , thành phố trực thuộc trung ương]`<CO_QUAN_THAM_QUYEN>`** bổ nhiệm **[Chủ tịch Ủy ban nhân dân huyện , quận]`<CO_QUAN_THAM_QUYEN>`** ; **[Phòng Nội vụ]`<CO_QUAN_THAM_QUYEN>`** hoàn chỉnh **[hồ sơ trình]`<GIAY_TO_HO_SO>`** **[Chủ tịch Ủy ban nhân dân quận , thị xã , thành phố thuộc tỉnh]`<CO_QUAN_THAM_QUYEN>`** bổ nhiệm **[Chủ tịch Ủy ban nhân dân phường]`<CO_QUAN_THAM_QUYEN>`** .]`<DIEM>`**

**Thực thể:**
- `[e0]` **Điều 2** → `DIEU` (span: `[0:2]`)
- `[e1]` **Khoản 1** → `KHOAN` (span: `[3:5]`)
- `[e2]` **d ) Căn cứ thông báo bằng văn bản của cấp có thẩm quyền quản lý cán bộ , Sở Nội vụ hoàn chỉnh hồ sơ trình Chủ tịch Ủy ban nhân dân tỉnh , thành phố trực thuộc trung ương bổ nhiệm Chủ tịch Ủy ban nhân dân huyện , quận ; Phòng Nội vụ hoàn chỉnh hồ sơ trình Chủ tịch Ủy ban nhân dân quận , thị xã , thành phố thuộc tỉnh bổ nhiệm Chủ tịch Ủy ban nhân dân phường .** → `DIEM` (span: `[6:59]`)
- `[e3]` **cấp có thẩm quyền quản lý cán bộ** → `CO_QUAN_THAM_QUYEN` (span: `[13:18]`) *(lồng trong `e2` (`DIEM`))*
- `[e4]` **Sở Nội vụ** → `CO_QUAN_THAM_QUYEN` (span: `[19:21]`) *(lồng trong `e2` (`DIEM`))*
- `[e5]` **Chủ tịch Ủy ban nhân dân tỉnh , thành phố trực thuộc trung ương** → `CO_QUAN_THAM_QUYEN` (span: `[23:31]`) *(lồng trong `e2` (`DIEM`))*
- `[e6]` **Chủ tịch Ủy ban nhân dân huyện , quận** → `CO_QUAN_THAM_QUYEN` (span: `[32:38]`) *(lồng trong `e2` (`DIEM`))*
- `[e7]` **Phòng Nội vụ** → `CO_QUAN_THAM_QUYEN` (span: `[39:41]`) *(lồng trong `e2` (`DIEM`))*
- `[e8]` **Chủ tịch Ủy ban nhân dân quận , thị xã , thành phố thuộc tỉnh** → `CO_QUAN_THAM_QUYEN` (span: `[43:53]`) *(lồng trong `e2` (`DIEM`))*
- `[e9]` **Chủ tịch Ủy ban nhân dân phường** → `CO_QUAN_THAM_QUYEN` (span: `[54:58]`) *(lồng trong `e2` (`DIEM`))*
- `[e10]` **thông báo bằng văn bản** → `GIAY_TO_HO_SO` (span: `[9:12]`) *(lồng trong `e2` (`DIEM`))*
- `[e11]` **hồ sơ trình** → `GIAY_TO_HO_SO` (span: `[22:23]`) *(lồng trong `e2` (`DIEM`))*
- `[e12]` **hồ sơ trình** → `GIAY_TO_HO_SO` (span: `[42:43]`) *(lồng trong `e2` (`DIEM`))*

**Quan hệ:**
- (`e1` Khoản 1 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 2 `[DIEU]`)
- (`e2` d ) Căn cứ thông báo bằng văn bản của cấp có thẩm quyền quản lý cán bộ , Sở Nội vụ hoàn chỉnh hồ sơ trình Chủ tịch Ủy ban nhân dân tỉnh , thành phố trực thuộc trung ương bổ nhiệm Chủ tịch Ủy ban nhân dân huyện , quận ; Phòng Nội vụ hoàn chỉnh hồ sơ trình Chủ tịch Ủy ban nhân dân quận , thị xã , thành phố thuộc tỉnh bổ nhiệm Chủ tịch Ủy ban nhân dân phường . `[DIEM]`) ==[ **THUOC_VE** ]==> (`e1` Khoản 1 `[KHOAN]`)


---

### Mẫu #01_2009_TT-BNV_12219#body_context_34 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[01/2009/TT-BNV]`<SO_HIEU>`** ban hành **[ngày 19 tháng 03 năm 2009]`<NGAY_BAN_HANH>`** bởi **[Bộ Nội vụ]`<CO_QUAN_BAN_HANH>`** . **[Điều 2]`<DIEU>`** . **[2 . Bổ nhiệm Phó **[Chủ tịch Ủy ban nhân dân huyện , quận , phường]`<CO_QUAN_THAM_QUYEN>`**]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **01/2009/TT-BNV** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Nội vụ** → `CO_QUAN_BAN_HANH` (span: `[11:13]`)
- `[e3]` **ngày 19 tháng 03 năm 2009** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 2** → `DIEU` (span: `[14:16]`)
- `[e5]` **2 . Bổ nhiệm Phó Chủ tịch Ủy ban nhân dân huyện , quận , phường** → `KHOAN` (span: `[17:29]`)
- `[e6]` **Chủ tịch Ủy ban nhân dân huyện , quận , phường** → `CO_QUAN_THAM_QUYEN` (span: `[21:29]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 01/2009/TT-BNV `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Nội vụ `[CO_QUAN_BAN_HANH]`)
- (`e1` 01/2009/TT-BNV `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 01/2009/TT-BNV `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 19 tháng 03 năm 2009 `[NGAY_BAN_HANH]`)
- (`e4` Điều 2 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 01/2009/TT-BNV `[SO_HIEU]`)
- (`e5` 2 . Bổ nhiệm Phó Chủ tịch Ủy ban nhân dân huyện , quận , phường `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 2 `[DIEU]`)


---

### Mẫu #01_2009_TT-BNV_12219#body_context_35 (Loại: `body_context`)
> **[Bộ Nội vụ]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[01/2009/TT-BNV]`<SO_HIEU>`** . **[Điều 2]`<DIEU>`** . **[Khoản 2]`<KHOAN>`** . **[a ) Căn cứ **[Nghị định số 107/2004/NĐ-CP]`<THAM_CHIEU_PHAP_LY>`** **[ngày 01 tháng 4 năm 2004]`<NGAY_THAM_CHIEU>`** của **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** quy định số lượng Phó Chủ tịch và cơ cấu thành viên **[Ủy ban nhân dân các cấp]`<CO_QUAN_THAM_QUYEN>`** ; **[Nghị định số 27/2009/NĐ-CP]`<THAM_CHIEU_PHAP_LY>`** **[ngày 19 tháng 3 năm 2009]`<NGAY_THAM_CHIEU>`** của **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** **[sửa đổi , bổ sung]`<TU_KHOA_PHAP_LY>`** **[Nghị định số 107/2004/NĐ-CP]`<THAM_CHIEU_PHAP_LY>`** **[ngày 01 tháng 4 năm 2004]`<NGAY_THAM_CHIEU>`** của **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** quy định số lượng Phó Chủ tịch và cơ cấu thành viên **[Ủy ban nhân dân các cấp]`<CO_QUAN_THAM_QUYEN>`** và **[thông báo bằng văn bản]`<GIAY_TO_HO_SO>`** về]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[3:4]`)
- `[e1]` **01/2009/TT-BNV** → `SO_HIEU` (span: `[5:6]`)
- `[e2]` **Bộ Nội vụ** → `CO_QUAN_BAN_HANH` (span: `[0:2]`)
- `[e3]` **Điều 2** → `DIEU` (span: `[7:9]`)
- `[e4]` **Khoản 2** → `KHOAN` (span: `[10:12]`)
- `[e5]` **a ) Căn cứ Nghị định số 107/2004/NĐ-CP ngày 01 tháng 4 năm 2004 của Chính phủ quy định số lượng Phó Chủ tịch và cơ cấu thành viên Ủy ban nhân dân các cấp ; Nghị định số 27/2009/NĐ-CP ngày 19 tháng 3 năm 2009 của Chính phủ sửa đổi , bổ sung Nghị định số 107/2004/NĐ-CP ngày 01 tháng 4 năm 2004 của Chính phủ quy định số lượng Phó Chủ tịch và cơ cấu thành viên Ủy ban nhân dân các cấp và thông báo bằng văn bản về** → `DIEM` (span: `[13:76]`)
- `[e6]` **Nghị định số 107/2004/NĐ-CP** → `THAM_CHIEU_PHAP_LY` (span: `[16:19]`) *(lồng trong `e5` (`DIEM`))*
- `[e7]` **Nghị định số 27/2009/NĐ-CP** → `THAM_CHIEU_PHAP_LY` (span: `[37:40]`) *(lồng trong `e5` (`DIEM`))*
- `[e8]` **Nghị định số 107/2004/NĐ-CP** → `THAM_CHIEU_PHAP_LY` (span: `[51:54]`) *(lồng trong `e5` (`DIEM`))*
- `[e9]` **sửa đổi , bổ sung** → `TU_KHOA_PHAP_LY` (span: `[48:51]`) *(lồng trong `e5` (`DIEM`))*
- `[e10]` **ngày 01 tháng 4 năm 2004** → `NGAY_THAM_CHIEU` (span: `[19:25]`) *(lồng trong `e5` (`DIEM`))*
- `[e11]` **ngày 19 tháng 3 năm 2009** → `NGAY_THAM_CHIEU` (span: `[40:46]`) *(lồng trong `e5` (`DIEM`))*
- `[e12]` **ngày 01 tháng 4 năm 2004** → `NGAY_THAM_CHIEU` (span: `[54:60]`) *(lồng trong `e5` (`DIEM`))*
- `[e13]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[26:27]`) *(lồng trong `e5` (`DIEM`))*
- `[e14]` **Ủy ban nhân dân các cấp** → `CO_QUAN_THAM_QUYEN` (span: `[32:36]`) *(lồng trong `e5` (`DIEM`))*
- `[e15]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[47:48]`) *(lồng trong `e5` (`DIEM`))*
- `[e16]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[61:62]`) *(lồng trong `e5` (`DIEM`))*
- `[e17]` **Ủy ban nhân dân các cấp** → `CO_QUAN_THAM_QUYEN` (span: `[67:71]`) *(lồng trong `e5` (`DIEM`))*
- `[e18]` **thông báo bằng văn bản** → `GIAY_TO_HO_SO` (span: `[72:75]`) *(lồng trong `e5` (`DIEM`))*

**Quan hệ:**
- (`e1` 01/2009/TT-BNV `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Nội vụ `[CO_QUAN_BAN_HANH]`)
- (`e1` 01/2009/TT-BNV `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 2 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 01/2009/TT-BNV `[SO_HIEU]`)
- (`e4` Khoản 2 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 2 `[DIEU]`)
- (`e5` a ) Căn cứ Nghị định số 107/2004/NĐ-CP ngày 01 tháng 4 năm 2004 của Chính phủ quy định số lượng Phó Chủ tịch và cơ cấu thành viên Ủy ban nhân dân các cấp ; Nghị định số 27/2009/NĐ-CP ngày 19 tháng 3 năm 2009 của Chính phủ sửa đổi , bổ sung Nghị định số 107/2004/NĐ-CP ngày 01 tháng 4 năm 2004 của Chính phủ quy định số lượng Phó Chủ tịch và cơ cấu thành viên Ủy ban nhân dân các cấp và thông báo bằng văn bản về `[DIEM]`) ==[ **THUOC_VE** ]==> (`e4` Khoản 2 `[KHOAN]`)
- (`e5` a ) Căn cứ Nghị định số 107/2004/NĐ-CP ngày 01 tháng 4 năm 2004 của Chính phủ quy định số lượng Phó Chủ tịch và cơ cấu thành viên Ủy ban nhân dân các cấp ; Nghị định số 27/2009/NĐ-CP ngày 19 tháng 3 năm 2009 của Chính phủ sửa đổi , bổ sung Nghị định số 107/2004/NĐ-CP ngày 01 tháng 4 năm 2004 của Chính phủ quy định số lượng Phó Chủ tịch và cơ cấu thành viên Ủy ban nhân dân các cấp và thông báo bằng văn bản về `[DIEM]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e6` Nghị định số 107/2004/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e5` a ) Căn cứ Nghị định số 107/2004/NĐ-CP ngày 01 tháng 4 năm 2004 của Chính phủ quy định số lượng Phó Chủ tịch và cơ cấu thành viên Ủy ban nhân dân các cấp ; Nghị định số 27/2009/NĐ-CP ngày 19 tháng 3 năm 2009 của Chính phủ sửa đổi , bổ sung Nghị định số 107/2004/NĐ-CP ngày 01 tháng 4 năm 2004 của Chính phủ quy định số lượng Phó Chủ tịch và cơ cấu thành viên Ủy ban nhân dân các cấp và thông báo bằng văn bản về `[DIEM]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e7` Nghị định số 27/2009/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e9` sửa đổi , bổ sung `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e8` Nghị định số 107/2004/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e5` a ) Căn cứ Nghị định số 107/2004/NĐ-CP ngày 01 tháng 4 năm 2004 của Chính phủ quy định số lượng Phó Chủ tịch và cơ cấu thành viên Ủy ban nhân dân các cấp ; Nghị định số 27/2009/NĐ-CP ngày 19 tháng 3 năm 2009 của Chính phủ sửa đổi , bổ sung Nghị định số 107/2004/NĐ-CP ngày 01 tháng 4 năm 2004 của Chính phủ quy định số lượng Phó Chủ tịch và cơ cấu thành viên Ủy ban nhân dân các cấp và thông báo bằng văn bản về `[DIEM]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e8` Nghị định số 107/2004/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e6` Nghị định số 107/2004/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e10` ngày 01 tháng 4 năm 2004 `[NGAY_THAM_CHIEU]`)
- (`e7` Nghị định số 27/2009/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e11` ngày 19 tháng 3 năm 2009 `[NGAY_THAM_CHIEU]`)
- (`e8` Nghị định số 107/2004/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e12` ngày 01 tháng 4 năm 2004 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #01_2009_TT-BNV_12219#body_standalone_36 (Loại: `body_standalone`)
> **[Điều 2]`<DIEU>`** . **[Khoản 2]`<KHOAN>`** . **[a ) Căn cứ **[Nghị định số 107/2004/NĐ-CP]`<THAM_CHIEU_PHAP_LY>`** **[ngày 01 tháng 4 năm 2004]`<NGAY_THAM_CHIEU>`** của **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** quy định số lượng Phó Chủ tịch và cơ cấu thành viên **[Ủy ban nhân dân các cấp]`<CO_QUAN_THAM_QUYEN>`** ; **[Nghị định số 27/2009/NĐ-CP]`<THAM_CHIEU_PHAP_LY>`** **[ngày 19 tháng 3 năm 2009]`<NGAY_THAM_CHIEU>`** của **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** **[sửa đổi , bổ sung]`<TU_KHOA_PHAP_LY>`** **[Nghị định số 107/2004/NĐ-CP]`<THAM_CHIEU_PHAP_LY>`** **[ngày 01 tháng 4 năm 2004]`<NGAY_THAM_CHIEU>`** của **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** quy định số lượng Phó Chủ tịch và cơ cấu thành viên **[Ủy ban nhân dân các cấp]`<CO_QUAN_THAM_QUYEN>`** và **[thông báo bằng văn bản]`<GIAY_TO_HO_SO>`** về]`<DIEM>`**

**Thực thể:**
- `[e0]` **Điều 2** → `DIEU` (span: `[0:2]`)
- `[e1]` **Khoản 2** → `KHOAN` (span: `[3:5]`)
- `[e2]` **a ) Căn cứ Nghị định số 107/2004/NĐ-CP ngày 01 tháng 4 năm 2004 của Chính phủ quy định số lượng Phó Chủ tịch và cơ cấu thành viên Ủy ban nhân dân các cấp ; Nghị định số 27/2009/NĐ-CP ngày 19 tháng 3 năm 2009 của Chính phủ sửa đổi , bổ sung Nghị định số 107/2004/NĐ-CP ngày 01 tháng 4 năm 2004 của Chính phủ quy định số lượng Phó Chủ tịch và cơ cấu thành viên Ủy ban nhân dân các cấp và thông báo bằng văn bản về** → `DIEM` (span: `[6:69]`)
- `[e3]` **Nghị định số 107/2004/NĐ-CP** → `THAM_CHIEU_PHAP_LY` (span: `[9:12]`) *(lồng trong `e2` (`DIEM`))*
- `[e4]` **Nghị định số 27/2009/NĐ-CP** → `THAM_CHIEU_PHAP_LY` (span: `[30:33]`) *(lồng trong `e2` (`DIEM`))*
- `[e5]` **Nghị định số 107/2004/NĐ-CP** → `THAM_CHIEU_PHAP_LY` (span: `[44:47]`) *(lồng trong `e2` (`DIEM`))*
- `[e6]` **sửa đổi , bổ sung** → `TU_KHOA_PHAP_LY` (span: `[41:44]`) *(lồng trong `e2` (`DIEM`))*
- `[e7]` **ngày 01 tháng 4 năm 2004** → `NGAY_THAM_CHIEU` (span: `[12:18]`) *(lồng trong `e2` (`DIEM`))*
- `[e8]` **ngày 19 tháng 3 năm 2009** → `NGAY_THAM_CHIEU` (span: `[33:39]`) *(lồng trong `e2` (`DIEM`))*
- `[e9]` **ngày 01 tháng 4 năm 2004** → `NGAY_THAM_CHIEU` (span: `[47:53]`) *(lồng trong `e2` (`DIEM`))*
- `[e10]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[19:20]`) *(lồng trong `e2` (`DIEM`))*
- `[e11]` **Ủy ban nhân dân các cấp** → `CO_QUAN_THAM_QUYEN` (span: `[25:29]`) *(lồng trong `e2` (`DIEM`))*
- `[e12]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[40:41]`) *(lồng trong `e2` (`DIEM`))*
- `[e13]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[54:55]`) *(lồng trong `e2` (`DIEM`))*
- `[e14]` **Ủy ban nhân dân các cấp** → `CO_QUAN_THAM_QUYEN` (span: `[60:64]`) *(lồng trong `e2` (`DIEM`))*
- `[e15]` **thông báo bằng văn bản** → `GIAY_TO_HO_SO` (span: `[65:68]`) *(lồng trong `e2` (`DIEM`))*

**Quan hệ:**
- (`e1` Khoản 2 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 2 `[DIEU]`)
- (`e2` a ) Căn cứ Nghị định số 107/2004/NĐ-CP ngày 01 tháng 4 năm 2004 của Chính phủ quy định số lượng Phó Chủ tịch và cơ cấu thành viên Ủy ban nhân dân các cấp ; Nghị định số 27/2009/NĐ-CP ngày 19 tháng 3 năm 2009 của Chính phủ sửa đổi , bổ sung Nghị định số 107/2004/NĐ-CP ngày 01 tháng 4 năm 2004 của Chính phủ quy định số lượng Phó Chủ tịch và cơ cấu thành viên Ủy ban nhân dân các cấp và thông báo bằng văn bản về `[DIEM]`) ==[ **THUOC_VE** ]==> (`e1` Khoản 2 `[KHOAN]`)
- (`e2` a ) Căn cứ Nghị định số 107/2004/NĐ-CP ngày 01 tháng 4 năm 2004 của Chính phủ quy định số lượng Phó Chủ tịch và cơ cấu thành viên Ủy ban nhân dân các cấp ; Nghị định số 27/2009/NĐ-CP ngày 19 tháng 3 năm 2009 của Chính phủ sửa đổi , bổ sung Nghị định số 107/2004/NĐ-CP ngày 01 tháng 4 năm 2004 của Chính phủ quy định số lượng Phó Chủ tịch và cơ cấu thành viên Ủy ban nhân dân các cấp và thông báo bằng văn bản về `[DIEM]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Nghị định số 107/2004/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e2` a ) Căn cứ Nghị định số 107/2004/NĐ-CP ngày 01 tháng 4 năm 2004 của Chính phủ quy định số lượng Phó Chủ tịch và cơ cấu thành viên Ủy ban nhân dân các cấp ; Nghị định số 27/2009/NĐ-CP ngày 19 tháng 3 năm 2009 của Chính phủ sửa đổi , bổ sung Nghị định số 107/2004/NĐ-CP ngày 01 tháng 4 năm 2004 của Chính phủ quy định số lượng Phó Chủ tịch và cơ cấu thành viên Ủy ban nhân dân các cấp và thông báo bằng văn bản về `[DIEM]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e4` Nghị định số 27/2009/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e6` sửa đổi , bổ sung `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e5` Nghị định số 107/2004/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e2` a ) Căn cứ Nghị định số 107/2004/NĐ-CP ngày 01 tháng 4 năm 2004 của Chính phủ quy định số lượng Phó Chủ tịch và cơ cấu thành viên Ủy ban nhân dân các cấp ; Nghị định số 27/2009/NĐ-CP ngày 19 tháng 3 năm 2009 của Chính phủ sửa đổi , bổ sung Nghị định số 107/2004/NĐ-CP ngày 01 tháng 4 năm 2004 của Chính phủ quy định số lượng Phó Chủ tịch và cơ cấu thành viên Ủy ban nhân dân các cấp và thông báo bằng văn bản về `[DIEM]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e5` Nghị định số 107/2004/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e3` Nghị định số 107/2004/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e7` ngày 01 tháng 4 năm 2004 `[NGAY_THAM_CHIEU]`)
- (`e4` Nghị định số 27/2009/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e8` ngày 19 tháng 3 năm 2009 `[NGAY_THAM_CHIEU]`)
- (`e5` Nghị định số 107/2004/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e9` ngày 01 tháng 4 năm 2004 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #01_2009_TT-BNV_12219#body_context_37 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[01/2009/TT-BNV]`<SO_HIEU>`** ban hành **[ngày 19 tháng 03 năm 2009]`<NGAY_BAN_HANH>`** bởi **[Bộ Nội vụ]`<CO_QUAN_BAN_HANH>`** . **[Điều 2]`<DIEU>`** . **[Khoản 2]`<KHOAN>`** . **[b ) Các cơ quan chức năng làm công tác tổ chức **[cán bộ]`<CHU_THE_CA_NHAN>`** tham mưu giúp **[cấp có thẩm quyền quản lý cán bộ]`<CO_QUAN_THAM_QUYEN>`** tiến hành quy trình nhân sự theo quy định hiện hành ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **01/2009/TT-BNV** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Nội vụ** → `CO_QUAN_BAN_HANH` (span: `[11:13]`)
- `[e3]` **ngày 19 tháng 03 năm 2009** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 2** → `DIEU` (span: `[14:16]`)
- `[e5]` **Khoản 2** → `KHOAN` (span: `[17:19]`)
- `[e6]` **b ) Các cơ quan chức năng làm công tác tổ chức cán bộ tham mưu giúp cấp có thẩm quyền quản lý cán bộ tiến hành quy trình nhân sự theo quy định hiện hành ;** → `DIEM` (span: `[20:42]`)
- `[e7]` **cấp có thẩm quyền quản lý cán bộ** → `CO_QUAN_THAM_QUYEN` (span: `[30:35]`) *(lồng trong `e6` (`DIEM`))*
- `[e8]` **cán bộ** → `CHU_THE_CA_NHAN` (span: `[27:28]`) *(lồng trong `e6` (`DIEM`))*

**Quan hệ:**
- (`e1` 01/2009/TT-BNV `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Nội vụ `[CO_QUAN_BAN_HANH]`)
- (`e1` 01/2009/TT-BNV `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 01/2009/TT-BNV `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 19 tháng 03 năm 2009 `[NGAY_BAN_HANH]`)
- (`e4` Điều 2 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 01/2009/TT-BNV `[SO_HIEU]`)
- (`e5` Khoản 2 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 2 `[DIEU]`)
- (`e6` b ) Các cơ quan chức năng làm công tác tổ chức cán bộ tham mưu giúp cấp có thẩm quyền quản lý cán bộ tiến hành quy trình nhân sự theo quy định hiện hành ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e5` Khoản 2 `[KHOAN]`)


---

### Mẫu #01_2009_TT-BNV_12219#body_standalone_38 (Loại: `body_standalone`)
> **[Điều 2]`<DIEU>`** . **[Khoản 2]`<KHOAN>`** . **[b ) Các cơ quan chức năng làm công tác tổ chức **[cán bộ]`<CHU_THE_CA_NHAN>`** tham mưu giúp **[cấp có thẩm quyền quản lý cán bộ]`<CO_QUAN_THAM_QUYEN>`** tiến hành quy trình nhân sự theo quy định hiện hành ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Điều 2** → `DIEU` (span: `[0:2]`)
- `[e1]` **Khoản 2** → `KHOAN` (span: `[3:5]`)
- `[e2]` **b ) Các cơ quan chức năng làm công tác tổ chức cán bộ tham mưu giúp cấp có thẩm quyền quản lý cán bộ tiến hành quy trình nhân sự theo quy định hiện hành ;** → `DIEM` (span: `[6:28]`)
- `[e3]` **cấp có thẩm quyền quản lý cán bộ** → `CO_QUAN_THAM_QUYEN` (span: `[16:21]`) *(lồng trong `e2` (`DIEM`))*
- `[e4]` **cán bộ** → `CHU_THE_CA_NHAN` (span: `[13:14]`) *(lồng trong `e2` (`DIEM`))*

**Quan hệ:**
- (`e1` Khoản 2 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 2 `[DIEU]`)
- (`e2` b ) Các cơ quan chức năng làm công tác tổ chức cán bộ tham mưu giúp cấp có thẩm quyền quản lý cán bộ tiến hành quy trình nhân sự theo quy định hiện hành ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e1` Khoản 2 `[KHOAN]`)


---

### Mẫu #01_2009_TT-BNV_12219#body_context_39 (Loại: `body_context`)
> **[Bộ Nội vụ]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[01/2009/TT-BNV]`<SO_HIEU>`** . **[Điều 2]`<DIEU>`** . **[Khoản 2]`<KHOAN>`** . **[c ) **[Cấp có thẩm quyền quản lý cán bộ]`<CO_QUAN_THAM_QUYEN>`** xem xét , kết luận và có ý kiến đồng ý bằng văn bản ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[3:4]`)
- `[e1]` **01/2009/TT-BNV** → `SO_HIEU` (span: `[5:6]`)
- `[e2]` **Bộ Nội vụ** → `CO_QUAN_BAN_HANH` (span: `[0:2]`)
- `[e3]` **Điều 2** → `DIEU` (span: `[7:9]`)
- `[e4]` **Khoản 2** → `KHOAN` (span: `[10:12]`)
- `[e5]` **c ) Cấp có thẩm quyền quản lý cán bộ xem xét , kết luận và có ý kiến đồng ý bằng văn bản ;** → `DIEM` (span: `[13:30]`)
- `[e6]` **Cấp có thẩm quyền quản lý cán bộ** → `CO_QUAN_THAM_QUYEN` (span: `[15:20]`) *(lồng trong `e5` (`DIEM`))*

**Quan hệ:**
- (`e1` 01/2009/TT-BNV `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Nội vụ `[CO_QUAN_BAN_HANH]`)
- (`e1` 01/2009/TT-BNV `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 2 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 01/2009/TT-BNV `[SO_HIEU]`)
- (`e4` Khoản 2 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 2 `[DIEU]`)
- (`e5` c ) Cấp có thẩm quyền quản lý cán bộ xem xét , kết luận và có ý kiến đồng ý bằng văn bản ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e4` Khoản 2 `[KHOAN]`)


---

### Mẫu #01_2009_TT-BNV_12219#body_standalone_40 (Loại: `body_standalone`)
> **[Điều 2]`<DIEU>`** . **[Khoản 2]`<KHOAN>`** . **[c ) **[Cấp có thẩm quyền quản lý cán bộ]`<CO_QUAN_THAM_QUYEN>`** xem xét , kết luận và có ý kiến đồng ý bằng văn bản ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Điều 2** → `DIEU` (span: `[0:2]`)
- `[e1]` **Khoản 2** → `KHOAN` (span: `[3:5]`)
- `[e2]` **c ) Cấp có thẩm quyền quản lý cán bộ xem xét , kết luận và có ý kiến đồng ý bằng văn bản ;** → `DIEM` (span: `[6:23]`)
- `[e3]` **Cấp có thẩm quyền quản lý cán bộ** → `CO_QUAN_THAM_QUYEN` (span: `[8:13]`) *(lồng trong `e2` (`DIEM`))*

**Quan hệ:**
- (`e1` Khoản 2 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 2 `[DIEU]`)
- (`e2` c ) Cấp có thẩm quyền quản lý cán bộ xem xét , kết luận và có ý kiến đồng ý bằng văn bản ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e1` Khoản 2 `[KHOAN]`)


---

### Mẫu #01_2009_TT-BNV_12219#body_context_41 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[01/2009/TT-BNV]`<SO_HIEU>`** ban hành **[ngày 19 tháng 03 năm 2009]`<NGAY_BAN_HANH>`** bởi **[Bộ Nội vụ]`<CO_QUAN_BAN_HANH>`** . **[Điều 2]`<DIEU>`** . **[Khoản 2]`<KHOAN>`** . **[d ) Căn cứ **[thông báo bằng văn bản]`<GIAY_TO_HO_SO>`** của **[cấp có thẩm quyền quản lý cán bộ]`<CO_QUAN_THAM_QUYEN>`** , **[Sở Nội vụ]`<CO_QUAN_THAM_QUYEN>`** hoàn chỉnh **[hồ sơ trình]`<GIAY_TO_HO_SO>`** **[Chủ tịch Ủy ban nhân dân tỉnh , thành phố trực thuộc trung ương]`<CO_QUAN_THAM_QUYEN>`** bổ nhiệm Phó **[Chủ tịch Ủy ban nhân dân huyện , quận]`<CO_QUAN_THAM_QUYEN>`** ; **[Phòng Nội vụ]`<CO_QUAN_THAM_QUYEN>`** hoàn chỉnh **[hồ sơ trình]`<GIAY_TO_HO_SO>`** **[Chủ tịch Ủy ban nhân dân quận , thị xã , thành phố thuộc tỉnh]`<CO_QUAN_THAM_QUYEN>`** bổ nhiệm Phó **[Chủ tịch Ủy ban nhân dân phường]`<CO_QUAN_THAM_QUYEN>`** .]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **01/2009/TT-BNV** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Nội vụ** → `CO_QUAN_BAN_HANH` (span: `[11:13]`)
- `[e3]` **ngày 19 tháng 03 năm 2009** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 2** → `DIEU` (span: `[14:16]`)
- `[e5]` **Khoản 2** → `KHOAN` (span: `[17:19]`)
- `[e6]` **d ) Căn cứ thông báo bằng văn bản của cấp có thẩm quyền quản lý cán bộ , Sở Nội vụ hoàn chỉnh hồ sơ trình Chủ tịch Ủy ban nhân dân tỉnh , thành phố trực thuộc trung ương bổ nhiệm Phó Chủ tịch Ủy ban nhân dân huyện , quận ; Phòng Nội vụ hoàn chỉnh hồ sơ trình Chủ tịch Ủy ban nhân dân quận , thị xã , thành phố thuộc tỉnh bổ nhiệm Phó Chủ tịch Ủy ban nhân dân phường .** → `DIEM` (span: `[20:75]`)
- `[e7]` **cấp có thẩm quyền quản lý cán bộ** → `CO_QUAN_THAM_QUYEN` (span: `[27:32]`) *(lồng trong `e6` (`DIEM`))*
- `[e8]` **Sở Nội vụ** → `CO_QUAN_THAM_QUYEN` (span: `[33:35]`) *(lồng trong `e6` (`DIEM`))*
- `[e9]` **Chủ tịch Ủy ban nhân dân tỉnh , thành phố trực thuộc trung ương** → `CO_QUAN_THAM_QUYEN` (span: `[37:45]`) *(lồng trong `e6` (`DIEM`))*
- `[e10]` **Chủ tịch Ủy ban nhân dân huyện , quận** → `CO_QUAN_THAM_QUYEN` (span: `[47:53]`) *(lồng trong `e6` (`DIEM`))*
- `[e11]` **Phòng Nội vụ** → `CO_QUAN_THAM_QUYEN` (span: `[54:56]`) *(lồng trong `e6` (`DIEM`))*
- `[e12]` **Chủ tịch Ủy ban nhân dân quận , thị xã , thành phố thuộc tỉnh** → `CO_QUAN_THAM_QUYEN` (span: `[58:68]`) *(lồng trong `e6` (`DIEM`))*
- `[e13]` **Chủ tịch Ủy ban nhân dân phường** → `CO_QUAN_THAM_QUYEN` (span: `[70:74]`) *(lồng trong `e6` (`DIEM`))*
- `[e14]` **thông báo bằng văn bản** → `GIAY_TO_HO_SO` (span: `[23:26]`) *(lồng trong `e6` (`DIEM`))*
- `[e15]` **hồ sơ trình** → `GIAY_TO_HO_SO` (span: `[36:37]`) *(lồng trong `e6` (`DIEM`))*
- `[e16]` **hồ sơ trình** → `GIAY_TO_HO_SO` (span: `[57:58]`) *(lồng trong `e6` (`DIEM`))*

**Quan hệ:**
- (`e1` 01/2009/TT-BNV `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Nội vụ `[CO_QUAN_BAN_HANH]`)
- (`e1` 01/2009/TT-BNV `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 01/2009/TT-BNV `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 19 tháng 03 năm 2009 `[NGAY_BAN_HANH]`)
- (`e4` Điều 2 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 01/2009/TT-BNV `[SO_HIEU]`)
- (`e5` Khoản 2 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 2 `[DIEU]`)
- (`e6` d ) Căn cứ thông báo bằng văn bản của cấp có thẩm quyền quản lý cán bộ , Sở Nội vụ hoàn chỉnh hồ sơ trình Chủ tịch Ủy ban nhân dân tỉnh , thành phố trực thuộc trung ương bổ nhiệm Phó Chủ tịch Ủy ban nhân dân huyện , quận ; Phòng Nội vụ hoàn chỉnh hồ sơ trình Chủ tịch Ủy ban nhân dân quận , thị xã , thành phố thuộc tỉnh bổ nhiệm Phó Chủ tịch Ủy ban nhân dân phường . `[DIEM]`) ==[ **THUOC_VE** ]==> (`e5` Khoản 2 `[KHOAN]`)


---

### Mẫu #01_2009_TT-BNV_12219#body_standalone_42 (Loại: `body_standalone`)
> **[Điều 2]`<DIEU>`** . **[Khoản 2]`<KHOAN>`** . **[d ) Căn cứ **[thông báo bằng văn bản]`<GIAY_TO_HO_SO>`** của **[cấp có thẩm quyền quản lý cán bộ]`<CO_QUAN_THAM_QUYEN>`** , **[Sở Nội vụ]`<CO_QUAN_THAM_QUYEN>`** hoàn chỉnh **[hồ sơ trình]`<GIAY_TO_HO_SO>`** **[Chủ tịch Ủy ban nhân dân tỉnh , thành phố trực thuộc trung ương]`<CO_QUAN_THAM_QUYEN>`** bổ nhiệm Phó **[Chủ tịch Ủy ban nhân dân huyện , quận]`<CO_QUAN_THAM_QUYEN>`** ; **[Phòng Nội vụ]`<CO_QUAN_THAM_QUYEN>`** hoàn chỉnh **[hồ sơ trình]`<GIAY_TO_HO_SO>`** **[Chủ tịch Ủy ban nhân dân quận , thị xã , thành phố thuộc tỉnh]`<CO_QUAN_THAM_QUYEN>`** bổ nhiệm Phó **[Chủ tịch Ủy ban nhân dân phường]`<CO_QUAN_THAM_QUYEN>`** .]`<DIEM>`**

**Thực thể:**
- `[e0]` **Điều 2** → `DIEU` (span: `[0:2]`)
- `[e1]` **Khoản 2** → `KHOAN` (span: `[3:5]`)
- `[e2]` **d ) Căn cứ thông báo bằng văn bản của cấp có thẩm quyền quản lý cán bộ , Sở Nội vụ hoàn chỉnh hồ sơ trình Chủ tịch Ủy ban nhân dân tỉnh , thành phố trực thuộc trung ương bổ nhiệm Phó Chủ tịch Ủy ban nhân dân huyện , quận ; Phòng Nội vụ hoàn chỉnh hồ sơ trình Chủ tịch Ủy ban nhân dân quận , thị xã , thành phố thuộc tỉnh bổ nhiệm Phó Chủ tịch Ủy ban nhân dân phường .** → `DIEM` (span: `[6:61]`)
- `[e3]` **cấp có thẩm quyền quản lý cán bộ** → `CO_QUAN_THAM_QUYEN` (span: `[13:18]`) *(lồng trong `e2` (`DIEM`))*
- `[e4]` **Sở Nội vụ** → `CO_QUAN_THAM_QUYEN` (span: `[19:21]`) *(lồng trong `e2` (`DIEM`))*
- `[e5]` **Chủ tịch Ủy ban nhân dân tỉnh , thành phố trực thuộc trung ương** → `CO_QUAN_THAM_QUYEN` (span: `[23:31]`) *(lồng trong `e2` (`DIEM`))*
- `[e6]` **Chủ tịch Ủy ban nhân dân huyện , quận** → `CO_QUAN_THAM_QUYEN` (span: `[33:39]`) *(lồng trong `e2` (`DIEM`))*
- `[e7]` **Phòng Nội vụ** → `CO_QUAN_THAM_QUYEN` (span: `[40:42]`) *(lồng trong `e2` (`DIEM`))*
- `[e8]` **Chủ tịch Ủy ban nhân dân quận , thị xã , thành phố thuộc tỉnh** → `CO_QUAN_THAM_QUYEN` (span: `[44:54]`) *(lồng trong `e2` (`DIEM`))*
- `[e9]` **Chủ tịch Ủy ban nhân dân phường** → `CO_QUAN_THAM_QUYEN` (span: `[56:60]`) *(lồng trong `e2` (`DIEM`))*
- `[e10]` **thông báo bằng văn bản** → `GIAY_TO_HO_SO` (span: `[9:12]`) *(lồng trong `e2` (`DIEM`))*
- `[e11]` **hồ sơ trình** → `GIAY_TO_HO_SO` (span: `[22:23]`) *(lồng trong `e2` (`DIEM`))*
- `[e12]` **hồ sơ trình** → `GIAY_TO_HO_SO` (span: `[43:44]`) *(lồng trong `e2` (`DIEM`))*

**Quan hệ:**
- (`e1` Khoản 2 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 2 `[DIEU]`)
- (`e2` d ) Căn cứ thông báo bằng văn bản của cấp có thẩm quyền quản lý cán bộ , Sở Nội vụ hoàn chỉnh hồ sơ trình Chủ tịch Ủy ban nhân dân tỉnh , thành phố trực thuộc trung ương bổ nhiệm Phó Chủ tịch Ủy ban nhân dân huyện , quận ; Phòng Nội vụ hoàn chỉnh hồ sơ trình Chủ tịch Ủy ban nhân dân quận , thị xã , thành phố thuộc tỉnh bổ nhiệm Phó Chủ tịch Ủy ban nhân dân phường . `[DIEM]`) ==[ **THUOC_VE** ]==> (`e1` Khoản 2 `[KHOAN]`)


---

### Mẫu #01_2009_TT-BNV_12219#body_context_43 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[01/2009/TT-BNV]`<SO_HIEU>`** của **[Bộ Nội vụ]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Nội vụ]`<LINH_VUC>`** . **[Điều 2]`<DIEU>`** . **[Khoản 3]`<KHOAN>`** . **[a ) Căn cứ **[Nghị định số 107/2004/NĐ-CP]`<THAM_CHIEU_PHAP_LY>`** **[ngày 01 tháng 4 năm 2004]`<NGAY_THAM_CHIEU>`** của **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** quy định số lượng Phó Chủ tịch và cơ cấu thành viên **[Ủy ban nhân dân các cấp]`<CO_QUAN_THAM_QUYEN>`** ; **[Nghị định số 27/2009/NĐ-CP]`<THAM_CHIEU_PHAP_LY>`** **[ngày 19 tháng 3 năm 2009]`<NGAY_THAM_CHIEU>`** của **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** **[sửa đổi , bổ sung]`<TU_KHOA_PHAP_LY>`** **[Nghị định số 107/2004/NĐ-CP]`<THAM_CHIEU_PHAP_LY>`** **[ngày 01 tháng 4 năm 2004]`<NGAY_THAM_CHIEU>`** của **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** quy định số lượng Phó Chủ tịch và cơ cấu thành viên **[Ủy ban nhân dân các cấp]`<CO_QUAN_THAM_QUYEN>`** , Chủ tịch Ủy ban nhân dân huyện ,]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **01/2009/TT-BNV** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Nội vụ** → `CO_QUAN_BAN_HANH` (span: `[4:6]`)
- `[e3]` **Nội vụ** → `LINH_VUC` (span: `[8:9]`)
- `[e4]` **Điều 2** → `DIEU` (span: `[10:12]`)
- `[e5]` **Khoản 3** → `KHOAN` (span: `[13:15]`)
- `[e6]` **a ) Căn cứ Nghị định số 107/2004/NĐ-CP ngày 01 tháng 4 năm 2004 của Chính phủ quy định số lượng Phó Chủ tịch và cơ cấu thành viên Ủy ban nhân dân các cấp ; Nghị định số 27/2009/NĐ-CP ngày 19 tháng 3 năm 2009 của Chính phủ sửa đổi , bổ sung Nghị định số 107/2004/NĐ-CP ngày 01 tháng 4 năm 2004 của Chính phủ quy định số lượng Phó Chủ tịch và cơ cấu thành viên Ủy ban nhân dân các cấp , Chủ tịch Ủy ban nhân dân huyện ,** → `DIEM` (span: `[16:80]`)
- `[e7]` **Nghị định số 107/2004/NĐ-CP** → `THAM_CHIEU_PHAP_LY` (span: `[19:22]`) *(lồng trong `e6` (`DIEM`))*
- `[e8]` **Nghị định số 27/2009/NĐ-CP** → `THAM_CHIEU_PHAP_LY` (span: `[40:43]`) *(lồng trong `e6` (`DIEM`))*
- `[e9]` **Nghị định số 107/2004/NĐ-CP** → `THAM_CHIEU_PHAP_LY` (span: `[54:57]`) *(lồng trong `e6` (`DIEM`))*
- `[e10]` **sửa đổi , bổ sung** → `TU_KHOA_PHAP_LY` (span: `[51:54]`) *(lồng trong `e6` (`DIEM`))*
- `[e11]` **ngày 01 tháng 4 năm 2004** → `NGAY_THAM_CHIEU` (span: `[22:28]`) *(lồng trong `e6` (`DIEM`))*
- `[e12]` **ngày 19 tháng 3 năm 2009** → `NGAY_THAM_CHIEU` (span: `[43:49]`) *(lồng trong `e6` (`DIEM`))*
- `[e13]` **ngày 01 tháng 4 năm 2004** → `NGAY_THAM_CHIEU` (span: `[57:63]`) *(lồng trong `e6` (`DIEM`))*
- `[e14]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[29:30]`) *(lồng trong `e6` (`DIEM`))*
- `[e15]` **Ủy ban nhân dân các cấp** → `CO_QUAN_THAM_QUYEN` (span: `[35:39]`) *(lồng trong `e6` (`DIEM`))*
- `[e16]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[50:51]`) *(lồng trong `e6` (`DIEM`))*
- `[e17]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[64:65]`) *(lồng trong `e6` (`DIEM`))*
- `[e18]` **Ủy ban nhân dân các cấp** → `CO_QUAN_THAM_QUYEN` (span: `[70:74]`) *(lồng trong `e6` (`DIEM`))*

**Quan hệ:**
- (`e1` 01/2009/TT-BNV `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Nội vụ `[CO_QUAN_BAN_HANH]`)
- (`e1` 01/2009/TT-BNV `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 01/2009/TT-BNV `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Nội vụ `[LINH_VUC]`)
- (`e4` Điều 2 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 01/2009/TT-BNV `[SO_HIEU]`)
- (`e5` Khoản 3 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 2 `[DIEU]`)
- (`e6` a ) Căn cứ Nghị định số 107/2004/NĐ-CP ngày 01 tháng 4 năm 2004 của Chính phủ quy định số lượng Phó Chủ tịch và cơ cấu thành viên Ủy ban nhân dân các cấp ; Nghị định số 27/2009/NĐ-CP ngày 19 tháng 3 năm 2009 của Chính phủ sửa đổi , bổ sung Nghị định số 107/2004/NĐ-CP ngày 01 tháng 4 năm 2004 của Chính phủ quy định số lượng Phó Chủ tịch và cơ cấu thành viên Ủy ban nhân dân các cấp , Chủ tịch Ủy ban nhân dân huyện , `[DIEM]`) ==[ **THUOC_VE** ]==> (`e5` Khoản 3 `[KHOAN]`)
- (`e1` 01/2009/TT-BNV `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Nội vụ `[LINH_VUC]`)
- (`e6` a ) Căn cứ Nghị định số 107/2004/NĐ-CP ngày 01 tháng 4 năm 2004 của Chính phủ quy định số lượng Phó Chủ tịch và cơ cấu thành viên Ủy ban nhân dân các cấp ; Nghị định số 27/2009/NĐ-CP ngày 19 tháng 3 năm 2009 của Chính phủ sửa đổi , bổ sung Nghị định số 107/2004/NĐ-CP ngày 01 tháng 4 năm 2004 của Chính phủ quy định số lượng Phó Chủ tịch và cơ cấu thành viên Ủy ban nhân dân các cấp , Chủ tịch Ủy ban nhân dân huyện , `[DIEM]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Nội vụ `[LINH_VUC]`)
- (`e6` a ) Căn cứ Nghị định số 107/2004/NĐ-CP ngày 01 tháng 4 năm 2004 của Chính phủ quy định số lượng Phó Chủ tịch và cơ cấu thành viên Ủy ban nhân dân các cấp ; Nghị định số 27/2009/NĐ-CP ngày 19 tháng 3 năm 2009 của Chính phủ sửa đổi , bổ sung Nghị định số 107/2004/NĐ-CP ngày 01 tháng 4 năm 2004 của Chính phủ quy định số lượng Phó Chủ tịch và cơ cấu thành viên Ủy ban nhân dân các cấp , Chủ tịch Ủy ban nhân dân huyện , `[DIEM]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e7` Nghị định số 107/2004/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e6` a ) Căn cứ Nghị định số 107/2004/NĐ-CP ngày 01 tháng 4 năm 2004 của Chính phủ quy định số lượng Phó Chủ tịch và cơ cấu thành viên Ủy ban nhân dân các cấp ; Nghị định số 27/2009/NĐ-CP ngày 19 tháng 3 năm 2009 của Chính phủ sửa đổi , bổ sung Nghị định số 107/2004/NĐ-CP ngày 01 tháng 4 năm 2004 của Chính phủ quy định số lượng Phó Chủ tịch và cơ cấu thành viên Ủy ban nhân dân các cấp , Chủ tịch Ủy ban nhân dân huyện , `[DIEM]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e8` Nghị định số 27/2009/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e10` sửa đổi , bổ sung `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e9` Nghị định số 107/2004/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e6` a ) Căn cứ Nghị định số 107/2004/NĐ-CP ngày 01 tháng 4 năm 2004 của Chính phủ quy định số lượng Phó Chủ tịch và cơ cấu thành viên Ủy ban nhân dân các cấp ; Nghị định số 27/2009/NĐ-CP ngày 19 tháng 3 năm 2009 của Chính phủ sửa đổi , bổ sung Nghị định số 107/2004/NĐ-CP ngày 01 tháng 4 năm 2004 của Chính phủ quy định số lượng Phó Chủ tịch và cơ cấu thành viên Ủy ban nhân dân các cấp , Chủ tịch Ủy ban nhân dân huyện , `[DIEM]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e9` Nghị định số 107/2004/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e7` Nghị định số 107/2004/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e11` ngày 01 tháng 4 năm 2004 `[NGAY_THAM_CHIEU]`)
- (`e8` Nghị định số 27/2009/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e12` ngày 19 tháng 3 năm 2009 `[NGAY_THAM_CHIEU]`)
- (`e9` Nghị định số 107/2004/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e13` ngày 01 tháng 4 năm 2004 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #01_2009_TT-BNV_12219#body_standalone_44 (Loại: `body_standalone`)
> **[Điều 2]`<DIEU>`** . **[Khoản 3]`<KHOAN>`** . **[a ) Căn cứ **[Nghị định số 107/2004/NĐ-CP]`<THAM_CHIEU_PHAP_LY>`** **[ngày 01 tháng 4 năm 2004]`<NGAY_THAM_CHIEU>`** của **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** quy định số lượng Phó Chủ tịch và cơ cấu thành viên **[Ủy ban nhân dân các cấp]`<CO_QUAN_THAM_QUYEN>`** ; **[Nghị định số 27/2009/NĐ-CP]`<THAM_CHIEU_PHAP_LY>`** **[ngày 19 tháng 3 năm 2009]`<NGAY_THAM_CHIEU>`** của **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** **[sửa đổi , bổ sung]`<TU_KHOA_PHAP_LY>`** **[Nghị định số 107/2004/NĐ-CP]`<THAM_CHIEU_PHAP_LY>`** **[ngày 01 tháng 4 năm 2004]`<NGAY_THAM_CHIEU>`** của **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** quy định số lượng Phó Chủ tịch và cơ cấu thành viên **[Ủy ban nhân dân các cấp]`<CO_QUAN_THAM_QUYEN>`** , Chủ tịch Ủy ban nhân dân huyện ,]`<DIEM>`**

**Thực thể:**
- `[e0]` **Điều 2** → `DIEU` (span: `[0:2]`)
- `[e1]` **Khoản 3** → `KHOAN` (span: `[3:5]`)
- `[e2]` **a ) Căn cứ Nghị định số 107/2004/NĐ-CP ngày 01 tháng 4 năm 2004 của Chính phủ quy định số lượng Phó Chủ tịch và cơ cấu thành viên Ủy ban nhân dân các cấp ; Nghị định số 27/2009/NĐ-CP ngày 19 tháng 3 năm 2009 của Chính phủ sửa đổi , bổ sung Nghị định số 107/2004/NĐ-CP ngày 01 tháng 4 năm 2004 của Chính phủ quy định số lượng Phó Chủ tịch và cơ cấu thành viên Ủy ban nhân dân các cấp , Chủ tịch Ủy ban nhân dân huyện ,** → `DIEM` (span: `[6:70]`)
- `[e3]` **Nghị định số 107/2004/NĐ-CP** → `THAM_CHIEU_PHAP_LY` (span: `[9:12]`) *(lồng trong `e2` (`DIEM`))*
- `[e4]` **Nghị định số 27/2009/NĐ-CP** → `THAM_CHIEU_PHAP_LY` (span: `[30:33]`) *(lồng trong `e2` (`DIEM`))*
- `[e5]` **Nghị định số 107/2004/NĐ-CP** → `THAM_CHIEU_PHAP_LY` (span: `[44:47]`) *(lồng trong `e2` (`DIEM`))*
- `[e6]` **sửa đổi , bổ sung** → `TU_KHOA_PHAP_LY` (span: `[41:44]`) *(lồng trong `e2` (`DIEM`))*
- `[e7]` **ngày 01 tháng 4 năm 2004** → `NGAY_THAM_CHIEU` (span: `[12:18]`) *(lồng trong `e2` (`DIEM`))*
- `[e8]` **ngày 19 tháng 3 năm 2009** → `NGAY_THAM_CHIEU` (span: `[33:39]`) *(lồng trong `e2` (`DIEM`))*
- `[e9]` **ngày 01 tháng 4 năm 2004** → `NGAY_THAM_CHIEU` (span: `[47:53]`) *(lồng trong `e2` (`DIEM`))*
- `[e10]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[19:20]`) *(lồng trong `e2` (`DIEM`))*
- `[e11]` **Ủy ban nhân dân các cấp** → `CO_QUAN_THAM_QUYEN` (span: `[25:29]`) *(lồng trong `e2` (`DIEM`))*
- `[e12]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[40:41]`) *(lồng trong `e2` (`DIEM`))*
- `[e13]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[54:55]`) *(lồng trong `e2` (`DIEM`))*
- `[e14]` **Ủy ban nhân dân các cấp** → `CO_QUAN_THAM_QUYEN` (span: `[60:64]`) *(lồng trong `e2` (`DIEM`))*

**Quan hệ:**
- (`e1` Khoản 3 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 2 `[DIEU]`)
- (`e2` a ) Căn cứ Nghị định số 107/2004/NĐ-CP ngày 01 tháng 4 năm 2004 của Chính phủ quy định số lượng Phó Chủ tịch và cơ cấu thành viên Ủy ban nhân dân các cấp ; Nghị định số 27/2009/NĐ-CP ngày 19 tháng 3 năm 2009 của Chính phủ sửa đổi , bổ sung Nghị định số 107/2004/NĐ-CP ngày 01 tháng 4 năm 2004 của Chính phủ quy định số lượng Phó Chủ tịch và cơ cấu thành viên Ủy ban nhân dân các cấp , Chủ tịch Ủy ban nhân dân huyện , `[DIEM]`) ==[ **THUOC_VE** ]==> (`e1` Khoản 3 `[KHOAN]`)
- (`e2` a ) Căn cứ Nghị định số 107/2004/NĐ-CP ngày 01 tháng 4 năm 2004 của Chính phủ quy định số lượng Phó Chủ tịch và cơ cấu thành viên Ủy ban nhân dân các cấp ; Nghị định số 27/2009/NĐ-CP ngày 19 tháng 3 năm 2009 của Chính phủ sửa đổi , bổ sung Nghị định số 107/2004/NĐ-CP ngày 01 tháng 4 năm 2004 của Chính phủ quy định số lượng Phó Chủ tịch và cơ cấu thành viên Ủy ban nhân dân các cấp , Chủ tịch Ủy ban nhân dân huyện , `[DIEM]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Nghị định số 107/2004/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e2` a ) Căn cứ Nghị định số 107/2004/NĐ-CP ngày 01 tháng 4 năm 2004 của Chính phủ quy định số lượng Phó Chủ tịch và cơ cấu thành viên Ủy ban nhân dân các cấp ; Nghị định số 27/2009/NĐ-CP ngày 19 tháng 3 năm 2009 của Chính phủ sửa đổi , bổ sung Nghị định số 107/2004/NĐ-CP ngày 01 tháng 4 năm 2004 của Chính phủ quy định số lượng Phó Chủ tịch và cơ cấu thành viên Ủy ban nhân dân các cấp , Chủ tịch Ủy ban nhân dân huyện , `[DIEM]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e4` Nghị định số 27/2009/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e6` sửa đổi , bổ sung `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e5` Nghị định số 107/2004/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e2` a ) Căn cứ Nghị định số 107/2004/NĐ-CP ngày 01 tháng 4 năm 2004 của Chính phủ quy định số lượng Phó Chủ tịch và cơ cấu thành viên Ủy ban nhân dân các cấp ; Nghị định số 27/2009/NĐ-CP ngày 19 tháng 3 năm 2009 của Chính phủ sửa đổi , bổ sung Nghị định số 107/2004/NĐ-CP ngày 01 tháng 4 năm 2004 của Chính phủ quy định số lượng Phó Chủ tịch và cơ cấu thành viên Ủy ban nhân dân các cấp , Chủ tịch Ủy ban nhân dân huyện , `[DIEM]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e5` Nghị định số 107/2004/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e3` Nghị định số 107/2004/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e7` ngày 01 tháng 4 năm 2004 `[NGAY_THAM_CHIEU]`)
- (`e4` Nghị định số 27/2009/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e8` ngày 19 tháng 3 năm 2009 `[NGAY_THAM_CHIEU]`)
- (`e5` Nghị định số 107/2004/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e9` ngày 01 tháng 4 năm 2004 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #01_2009_TT-BNV_12219#body_context_45 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[01/2009/TT-BNV]`<SO_HIEU>`** của **[Bộ Nội vụ]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Nội vụ]`<LINH_VUC>`** . **[Điều 2]`<DIEU>`** . **[Khoản 3]`<KHOAN>`** . **[b ) **[Cấp có thẩm quyền quản lý cán bộ]`<CO_QUAN_THAM_QUYEN>`** xem xét , kết luận và có ý kiến đồng ý bằng văn bản ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **01/2009/TT-BNV** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Nội vụ** → `CO_QUAN_BAN_HANH` (span: `[4:6]`)
- `[e3]` **Nội vụ** → `LINH_VUC` (span: `[8:9]`)
- `[e4]` **Điều 2** → `DIEU` (span: `[10:12]`)
- `[e5]` **Khoản 3** → `KHOAN` (span: `[13:15]`)
- `[e6]` **b ) Cấp có thẩm quyền quản lý cán bộ xem xét , kết luận và có ý kiến đồng ý bằng văn bản ;** → `DIEM` (span: `[16:33]`)
- `[e7]` **Cấp có thẩm quyền quản lý cán bộ** → `CO_QUAN_THAM_QUYEN` (span: `[18:23]`) *(lồng trong `e6` (`DIEM`))*

**Quan hệ:**
- (`e1` 01/2009/TT-BNV `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Nội vụ `[CO_QUAN_BAN_HANH]`)
- (`e1` 01/2009/TT-BNV `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 01/2009/TT-BNV `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Nội vụ `[LINH_VUC]`)
- (`e4` Điều 2 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 01/2009/TT-BNV `[SO_HIEU]`)
- (`e5` Khoản 3 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 2 `[DIEU]`)
- (`e6` b ) Cấp có thẩm quyền quản lý cán bộ xem xét , kết luận và có ý kiến đồng ý bằng văn bản ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e5` Khoản 3 `[KHOAN]`)
- (`e1` 01/2009/TT-BNV `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Nội vụ `[LINH_VUC]`)
- (`e6` b ) Cấp có thẩm quyền quản lý cán bộ xem xét , kết luận và có ý kiến đồng ý bằng văn bản ; `[DIEM]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Nội vụ `[LINH_VUC]`)


---

### Mẫu #01_2009_TT-BNV_12219#body_context_46 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[01/2009/TT-BNV]`<SO_HIEU>`** ban hành **[ngày 19 tháng 03 năm 2009]`<NGAY_BAN_HANH>`** bởi **[Bộ Nội vụ]`<CO_QUAN_BAN_HANH>`** . **[Điều 2]`<DIEU>`** . **[Khoản 3]`<KHOAN>`** . **[c ) Căn cứ **[thông báo bằng văn bản]`<GIAY_TO_HO_SO>`** của **[cơ quan có thẩm quyền]`<CO_QUAN_THAM_QUYEN>`** quản lý **[cán bộ]`<CHU_THE_CA_NHAN>`** , **[Sở Nội vụ]`<CO_QUAN_THAM_QUYEN>`** hoàn chỉnh **[hồ sơ trình]`<GIAY_TO_HO_SO>`** **[Chủ tịch Ủy ban nhân dân tỉnh , thành phố trực thuộc trung ương]`<CO_QUAN_THAM_QUYEN>`** bổ nhiệm Ủy viên **[Ủy ban nhân dân huyện , quận]`<CO_QUAN_THAM_QUYEN>`** ; **[Phòng Nội vụ]`<CO_QUAN_THAM_QUYEN>`** hoàn chỉnh **[hồ sơ trình]`<GIAY_TO_HO_SO>`** **[Chủ tịch Ủy ban nhân dân quận , thị xã , thành phố thuộc tỉnh]`<CO_QUAN_THAM_QUYEN>`** bổ nhiệm Ủy viên **[Ủy ban nhân dân phường]`<CO_QUAN_THAM_QUYEN>`** .]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **01/2009/TT-BNV** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Nội vụ** → `CO_QUAN_BAN_HANH` (span: `[11:13]`)
- `[e3]` **ngày 19 tháng 03 năm 2009** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 2** → `DIEU` (span: `[14:16]`)
- `[e5]` **Khoản 3** → `KHOAN` (span: `[17:19]`)
- `[e6]` **c ) Căn cứ thông báo bằng văn bản của cơ quan có thẩm quyền quản lý cán bộ , Sở Nội vụ hoàn chỉnh hồ sơ trình Chủ tịch Ủy ban nhân dân tỉnh , thành phố trực thuộc trung ương bổ nhiệm Ủy viên Ủy ban nhân dân huyện , quận ; Phòng Nội vụ hoàn chỉnh hồ sơ trình Chủ tịch Ủy ban nhân dân quận , thị xã , thành phố thuộc tỉnh bổ nhiệm Ủy viên Ủy ban nhân dân phường .** → `DIEM` (span: `[20:73]`)
- `[e7]` **cơ quan có thẩm quyền** → `CO_QUAN_THAM_QUYEN` (span: `[27:30]`) *(lồng trong `e6` (`DIEM`))*
- `[e8]` **Sở Nội vụ** → `CO_QUAN_THAM_QUYEN` (span: `[33:35]`) *(lồng trong `e6` (`DIEM`))*
- `[e9]` **Chủ tịch Ủy ban nhân dân tỉnh , thành phố trực thuộc trung ương** → `CO_QUAN_THAM_QUYEN` (span: `[37:45]`) *(lồng trong `e6` (`DIEM`))*
- `[e10]` **Ủy ban nhân dân huyện , quận** → `CO_QUAN_THAM_QUYEN` (span: `[47:52]`) *(lồng trong `e6` (`DIEM`))*
- `[e11]` **Phòng Nội vụ** → `CO_QUAN_THAM_QUYEN` (span: `[53:55]`) *(lồng trong `e6` (`DIEM`))*
- `[e12]` **Chủ tịch Ủy ban nhân dân quận , thị xã , thành phố thuộc tỉnh** → `CO_QUAN_THAM_QUYEN` (span: `[57:67]`) *(lồng trong `e6` (`DIEM`))*
- `[e13]` **Ủy ban nhân dân phường** → `CO_QUAN_THAM_QUYEN` (span: `[69:72]`) *(lồng trong `e6` (`DIEM`))*
- `[e14]` **thông báo bằng văn bản** → `GIAY_TO_HO_SO` (span: `[23:26]`) *(lồng trong `e6` (`DIEM`))*
- `[e15]` **hồ sơ trình** → `GIAY_TO_HO_SO` (span: `[36:37]`) *(lồng trong `e6` (`DIEM`))*
- `[e16]` **hồ sơ trình** → `GIAY_TO_HO_SO` (span: `[56:57]`) *(lồng trong `e6` (`DIEM`))*
- `[e17]` **cán bộ** → `CHU_THE_CA_NHAN` (span: `[31:32]`) *(lồng trong `e6` (`DIEM`))*

**Quan hệ:**
- (`e1` 01/2009/TT-BNV `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Nội vụ `[CO_QUAN_BAN_HANH]`)
- (`e1` 01/2009/TT-BNV `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 01/2009/TT-BNV `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 19 tháng 03 năm 2009 `[NGAY_BAN_HANH]`)
- (`e4` Điều 2 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 01/2009/TT-BNV `[SO_HIEU]`)
- (`e5` Khoản 3 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 2 `[DIEU]`)
- (`e6` c ) Căn cứ thông báo bằng văn bản của cơ quan có thẩm quyền quản lý cán bộ , Sở Nội vụ hoàn chỉnh hồ sơ trình Chủ tịch Ủy ban nhân dân tỉnh , thành phố trực thuộc trung ương bổ nhiệm Ủy viên Ủy ban nhân dân huyện , quận ; Phòng Nội vụ hoàn chỉnh hồ sơ trình Chủ tịch Ủy ban nhân dân quận , thị xã , thành phố thuộc tỉnh bổ nhiệm Ủy viên Ủy ban nhân dân phường . `[DIEM]`) ==[ **THUOC_VE** ]==> (`e5` Khoản 3 `[KHOAN]`)


---

### Mẫu #01_2009_TT-BNV_12219#body_standalone_47 (Loại: `body_standalone`)
> **[Điều 2]`<DIEU>`** . **[Khoản 3]`<KHOAN>`** . **[c ) Căn cứ **[thông báo bằng văn bản]`<GIAY_TO_HO_SO>`** của **[cơ quan có thẩm quyền]`<CO_QUAN_THAM_QUYEN>`** quản lý **[cán bộ]`<CHU_THE_CA_NHAN>`** , **[Sở Nội vụ]`<CO_QUAN_THAM_QUYEN>`** hoàn chỉnh **[hồ sơ trình]`<GIAY_TO_HO_SO>`** **[Chủ tịch Ủy ban nhân dân tỉnh , thành phố trực thuộc trung ương]`<CO_QUAN_THAM_QUYEN>`** bổ nhiệm Ủy viên **[Ủy ban nhân dân huyện , quận]`<CO_QUAN_THAM_QUYEN>`** ; **[Phòng Nội vụ]`<CO_QUAN_THAM_QUYEN>`** hoàn chỉnh **[hồ sơ trình]`<GIAY_TO_HO_SO>`** **[Chủ tịch Ủy ban nhân dân quận , thị xã , thành phố thuộc tỉnh]`<CO_QUAN_THAM_QUYEN>`** bổ nhiệm Ủy viên **[Ủy ban nhân dân phường]`<CO_QUAN_THAM_QUYEN>`** .]`<DIEM>`**

**Thực thể:**
- `[e0]` **Điều 2** → `DIEU` (span: `[0:2]`)
- `[e1]` **Khoản 3** → `KHOAN` (span: `[3:5]`)
- `[e2]` **c ) Căn cứ thông báo bằng văn bản của cơ quan có thẩm quyền quản lý cán bộ , Sở Nội vụ hoàn chỉnh hồ sơ trình Chủ tịch Ủy ban nhân dân tỉnh , thành phố trực thuộc trung ương bổ nhiệm Ủy viên Ủy ban nhân dân huyện , quận ; Phòng Nội vụ hoàn chỉnh hồ sơ trình Chủ tịch Ủy ban nhân dân quận , thị xã , thành phố thuộc tỉnh bổ nhiệm Ủy viên Ủy ban nhân dân phường .** → `DIEM` (span: `[6:59]`)
- `[e3]` **cơ quan có thẩm quyền** → `CO_QUAN_THAM_QUYEN` (span: `[13:16]`) *(lồng trong `e2` (`DIEM`))*
- `[e4]` **Sở Nội vụ** → `CO_QUAN_THAM_QUYEN` (span: `[19:21]`) *(lồng trong `e2` (`DIEM`))*
- `[e5]` **Chủ tịch Ủy ban nhân dân tỉnh , thành phố trực thuộc trung ương** → `CO_QUAN_THAM_QUYEN` (span: `[23:31]`) *(lồng trong `e2` (`DIEM`))*
- `[e6]` **Ủy ban nhân dân huyện , quận** → `CO_QUAN_THAM_QUYEN` (span: `[33:38]`) *(lồng trong `e2` (`DIEM`))*
- `[e7]` **Phòng Nội vụ** → `CO_QUAN_THAM_QUYEN` (span: `[39:41]`) *(lồng trong `e2` (`DIEM`))*
- `[e8]` **Chủ tịch Ủy ban nhân dân quận , thị xã , thành phố thuộc tỉnh** → `CO_QUAN_THAM_QUYEN` (span: `[43:53]`) *(lồng trong `e2` (`DIEM`))*
- `[e9]` **Ủy ban nhân dân phường** → `CO_QUAN_THAM_QUYEN` (span: `[55:58]`) *(lồng trong `e2` (`DIEM`))*
- `[e10]` **thông báo bằng văn bản** → `GIAY_TO_HO_SO` (span: `[9:12]`) *(lồng trong `e2` (`DIEM`))*
- `[e11]` **hồ sơ trình** → `GIAY_TO_HO_SO` (span: `[22:23]`) *(lồng trong `e2` (`DIEM`))*
- `[e12]` **hồ sơ trình** → `GIAY_TO_HO_SO` (span: `[42:43]`) *(lồng trong `e2` (`DIEM`))*
- `[e13]` **cán bộ** → `CHU_THE_CA_NHAN` (span: `[17:18]`) *(lồng trong `e2` (`DIEM`))*

**Quan hệ:**
- (`e1` Khoản 3 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 2 `[DIEU]`)
- (`e2` c ) Căn cứ thông báo bằng văn bản của cơ quan có thẩm quyền quản lý cán bộ , Sở Nội vụ hoàn chỉnh hồ sơ trình Chủ tịch Ủy ban nhân dân tỉnh , thành phố trực thuộc trung ương bổ nhiệm Ủy viên Ủy ban nhân dân huyện , quận ; Phòng Nội vụ hoàn chỉnh hồ sơ trình Chủ tịch Ủy ban nhân dân quận , thị xã , thành phố thuộc tỉnh bổ nhiệm Ủy viên Ủy ban nhân dân phường . `[DIEM]`) ==[ **THUOC_VE** ]==> (`e1` Khoản 3 `[KHOAN]`)


---

### Mẫu #01_2009_TT-BNV_12219#body_context_48 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[01/2009/TT-BNV]`<SO_HIEU>`** của **[Bộ Nội vụ]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Nội vụ]`<LINH_VUC>`** . **[Điều 2]`<DIEU>`** . **[4 . **[Hồ sơ trình đề nghị bổ nhiệm Hồ sơ trình đề nghị bổ nhiệm Chủ]`<GIAY_TO_HO_SO>`** tịch , Phó Chủ tịch và Ủy viên **[Ủy ban nhân dân huyện , quận , phường]`<CO_QUAN_THAM_QUYEN>`** gửi Chủ tịch Ủy ban nhân dân cấp trên trực tiếp , đồng thời gửi **[Sở Nội vụ]`<CO_QUAN_THAM_QUYEN>`** ( đối với huyện , quận ) , **[Phòng Nội vụ]`<CO_QUAN_THAM_QUYEN>`** ( đối với phường ) . Hồ sơ bao gồm :]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **01/2009/TT-BNV** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Nội vụ** → `CO_QUAN_BAN_HANH` (span: `[4:6]`)
- `[e3]` **Nội vụ** → `LINH_VUC` (span: `[8:9]`)
- `[e4]` **Điều 2** → `DIEU` (span: `[10:12]`)
- `[e5]` **4 . Hồ sơ trình đề nghị bổ nhiệm Hồ sơ trình đề nghị bổ nhiệm Chủ tịch , Phó Chủ tịch và Ủy viên Ủy ban nhân dân huyện , quận , phường gửi Chủ tịch Ủy ban nhân dân cấp trên trực tiếp , đồng thời gửi Sở Nội vụ ( đối với huyện , quận ) , Phòng Nội vụ ( đối với phường ) . Hồ sơ bao gồm :** → `KHOAN` (span: `[13:65]`)
- `[e6]` **Ủy ban nhân dân huyện , quận , phường** → `CO_QUAN_THAM_QUYEN` (span: `[29:36]`) *(lồng trong `e5` (`KHOAN`))*
- `[e7]` **Sở Nội vụ** → `CO_QUAN_THAM_QUYEN` (span: `[46:48]`) *(lồng trong `e5` (`KHOAN`))*
- `[e8]` **Phòng Nội vụ** → `CO_QUAN_THAM_QUYEN` (span: `[55:57]`) *(lồng trong `e5` (`KHOAN`))*
- `[e9]` **Hồ sơ trình đề nghị bổ nhiệm Hồ sơ trình đề nghị bổ nhiệm Chủ** → `GIAY_TO_HO_SO` (span: `[15:24]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 01/2009/TT-BNV `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Nội vụ `[CO_QUAN_BAN_HANH]`)
- (`e1` 01/2009/TT-BNV `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 01/2009/TT-BNV `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Nội vụ `[LINH_VUC]`)
- (`e4` Điều 2 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 01/2009/TT-BNV `[SO_HIEU]`)
- (`e5` 4 . Hồ sơ trình đề nghị bổ nhiệm Hồ sơ trình đề nghị bổ nhiệm Chủ tịch , Phó Chủ tịch và Ủy viên Ủy ban nhân dân huyện , quận , phường gửi Chủ tịch Ủy ban nhân dân cấp trên trực tiếp , đồng thời gửi Sở Nội vụ ( đối với huyện , quận ) , Phòng Nội vụ ( đối với phường ) . Hồ sơ bao gồm : `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 2 `[DIEU]`)
- (`e1` 01/2009/TT-BNV `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Nội vụ `[LINH_VUC]`)
- (`e5` 4 . Hồ sơ trình đề nghị bổ nhiệm Hồ sơ trình đề nghị bổ nhiệm Chủ tịch , Phó Chủ tịch và Ủy viên Ủy ban nhân dân huyện , quận , phường gửi Chủ tịch Ủy ban nhân dân cấp trên trực tiếp , đồng thời gửi Sở Nội vụ ( đối với huyện , quận ) , Phòng Nội vụ ( đối với phường ) . Hồ sơ bao gồm : `[KHOAN]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Nội vụ `[LINH_VUC]`)


---

### Mẫu #01_2009_TT-BNV_12219#body_standalone_49 (Loại: `body_standalone`)
> **[Điều 2]`<DIEU>`** . **[4 . **[Hồ sơ trình đề nghị bổ nhiệm Hồ sơ trình đề nghị bổ nhiệm Chủ]`<GIAY_TO_HO_SO>`** tịch , Phó Chủ tịch và Ủy viên **[Ủy ban nhân dân huyện , quận , phường]`<CO_QUAN_THAM_QUYEN>`** gửi Chủ tịch Ủy ban nhân dân cấp trên trực tiếp , đồng thời gửi **[Sở Nội vụ]`<CO_QUAN_THAM_QUYEN>`** ( đối với huyện , quận ) , **[Phòng Nội vụ]`<CO_QUAN_THAM_QUYEN>`** ( đối với phường ) . Hồ sơ bao gồm :]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 2** → `DIEU` (span: `[0:2]`)
- `[e1]` **4 . Hồ sơ trình đề nghị bổ nhiệm Hồ sơ trình đề nghị bổ nhiệm Chủ tịch , Phó Chủ tịch và Ủy viên Ủy ban nhân dân huyện , quận , phường gửi Chủ tịch Ủy ban nhân dân cấp trên trực tiếp , đồng thời gửi Sở Nội vụ ( đối với huyện , quận ) , Phòng Nội vụ ( đối với phường ) . Hồ sơ bao gồm :** → `KHOAN` (span: `[3:55]`)
- `[e2]` **Ủy ban nhân dân huyện , quận , phường** → `CO_QUAN_THAM_QUYEN` (span: `[19:26]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **Sở Nội vụ** → `CO_QUAN_THAM_QUYEN` (span: `[36:38]`) *(lồng trong `e1` (`KHOAN`))*
- `[e4]` **Phòng Nội vụ** → `CO_QUAN_THAM_QUYEN` (span: `[45:47]`) *(lồng trong `e1` (`KHOAN`))*
- `[e5]` **Hồ sơ trình đề nghị bổ nhiệm Hồ sơ trình đề nghị bổ nhiệm Chủ** → `GIAY_TO_HO_SO` (span: `[5:14]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 4 . Hồ sơ trình đề nghị bổ nhiệm Hồ sơ trình đề nghị bổ nhiệm Chủ tịch , Phó Chủ tịch và Ủy viên Ủy ban nhân dân huyện , quận , phường gửi Chủ tịch Ủy ban nhân dân cấp trên trực tiếp , đồng thời gửi Sở Nội vụ ( đối với huyện , quận ) , Phòng Nội vụ ( đối với phường ) . Hồ sơ bao gồm : `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 2 `[DIEU]`)


---

### Mẫu #01_2009_TT-BNV_12219#body_context_50 (Loại: `body_context`)
> **[Bộ Nội vụ]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[01/2009/TT-BNV]`<SO_HIEU>`** . **[Điều 2]`<DIEU>`** . **[Khoản 4]`<KHOAN>`** . **[a ) Tờ trình của Ủy ban nhân dân cấp có **[cán bộ]`<CHU_THE_CA_NHAN>`** được bổ nhiệm ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[3:4]`)
- `[e1]` **01/2009/TT-BNV** → `SO_HIEU` (span: `[5:6]`)
- `[e2]` **Bộ Nội vụ** → `CO_QUAN_BAN_HANH` (span: `[0:2]`)
- `[e3]` **Điều 2** → `DIEU` (span: `[7:9]`)
- `[e4]` **Khoản 4** → `KHOAN` (span: `[10:12]`)
- `[e5]` **a ) Tờ trình của Ủy ban nhân dân cấp có cán bộ được bổ nhiệm ;** → `DIEM` (span: `[13:25]`)
- `[e6]` **cán bộ** → `CHU_THE_CA_NHAN` (span: `[21:22]`) *(lồng trong `e5` (`DIEM`))*

**Quan hệ:**
- (`e1` 01/2009/TT-BNV `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Nội vụ `[CO_QUAN_BAN_HANH]`)
- (`e1` 01/2009/TT-BNV `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 2 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 01/2009/TT-BNV `[SO_HIEU]`)
- (`e4` Khoản 4 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 2 `[DIEU]`)
- (`e5` a ) Tờ trình của Ủy ban nhân dân cấp có cán bộ được bổ nhiệm ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e4` Khoản 4 `[KHOAN]`)


---

### Mẫu #01_2009_TT-BNV_12219#body_context_51 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[01/2009/TT-BNV]`<SO_HIEU>`** ban hành **[ngày 19 tháng 03 năm 2009]`<NGAY_BAN_HANH>`** bởi **[Bộ Nội vụ]`<CO_QUAN_BAN_HANH>`** . **[Điều 2]`<DIEU>`** . **[Khoản 4]`<KHOAN>`** . **[b ) **[Văn bản thông báo]`<GIAY_TO_HO_SO>`** ý kiến đồng ý của **[cấp có thẩm quyền quản lý cán bộ]`<CO_QUAN_THAM_QUYEN>`** ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **01/2009/TT-BNV** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Nội vụ** → `CO_QUAN_BAN_HANH` (span: `[11:13]`)
- `[e3]` **ngày 19 tháng 03 năm 2009** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 2** → `DIEU` (span: `[14:16]`)
- `[e5]` **Khoản 4** → `KHOAN` (span: `[17:19]`)
- `[e6]` **b ) Văn bản thông báo ý kiến đồng ý của cấp có thẩm quyền quản lý cán bộ ;** → `DIEM` (span: `[20:33]`)
- `[e7]` **cấp có thẩm quyền quản lý cán bộ** → `CO_QUAN_THAM_QUYEN` (span: `[27:32]`) *(lồng trong `e6` (`DIEM`))*
- `[e8]` **Văn bản thông báo** → `GIAY_TO_HO_SO` (span: `[22:24]`) *(lồng trong `e6` (`DIEM`))*

**Quan hệ:**
- (`e1` 01/2009/TT-BNV `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Nội vụ `[CO_QUAN_BAN_HANH]`)
- (`e1` 01/2009/TT-BNV `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 01/2009/TT-BNV `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 19 tháng 03 năm 2009 `[NGAY_BAN_HANH]`)
- (`e4` Điều 2 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 01/2009/TT-BNV `[SO_HIEU]`)
- (`e5` Khoản 4 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 2 `[DIEU]`)
- (`e6` b ) Văn bản thông báo ý kiến đồng ý của cấp có thẩm quyền quản lý cán bộ ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e5` Khoản 4 `[KHOAN]`)


---

### Mẫu #01_2009_TT-BNV_12219#body_standalone_52 (Loại: `body_standalone`)
> **[Điều 2]`<DIEU>`** . **[Khoản 4]`<KHOAN>`** . **[b ) **[Văn bản thông báo]`<GIAY_TO_HO_SO>`** ý kiến đồng ý của **[cấp có thẩm quyền quản lý cán bộ]`<CO_QUAN_THAM_QUYEN>`** ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Điều 2** → `DIEU` (span: `[0:2]`)
- `[e1]` **Khoản 4** → `KHOAN` (span: `[3:5]`)
- `[e2]` **b ) Văn bản thông báo ý kiến đồng ý của cấp có thẩm quyền quản lý cán bộ ;** → `DIEM` (span: `[6:19]`)
- `[e3]` **cấp có thẩm quyền quản lý cán bộ** → `CO_QUAN_THAM_QUYEN` (span: `[13:18]`) *(lồng trong `e2` (`DIEM`))*
- `[e4]` **Văn bản thông báo** → `GIAY_TO_HO_SO` (span: `[8:10]`) *(lồng trong `e2` (`DIEM`))*

**Quan hệ:**
- (`e1` Khoản 4 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 2 `[DIEU]`)
- (`e2` b ) Văn bản thông báo ý kiến đồng ý của cấp có thẩm quyền quản lý cán bộ ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e1` Khoản 4 `[KHOAN]`)


---

### Mẫu #01_2009_TT-BNV_12219#body_context_53 (Loại: `body_context`)
> **[Bộ Nội vụ]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[01/2009/TT-BNV]`<SO_HIEU>`** . **[Điều 2]`<DIEU>`** . **[Khoản 4]`<KHOAN>`** . **[c ) Lý lịch **[cán bộ]`<CHU_THE_CA_NHAN>`** ( **[Mẫu 2C]`<THAM_CHIEU_PHAP_LY>`** – TCTW ) ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[3:4]`)
- `[e1]` **01/2009/TT-BNV** → `SO_HIEU` (span: `[5:6]`)
- `[e2]` **Bộ Nội vụ** → `CO_QUAN_BAN_HANH` (span: `[0:2]`)
- `[e3]` **Điều 2** → `DIEU` (span: `[7:9]`)
- `[e4]` **Khoản 4** → `KHOAN` (span: `[10:12]`)
- `[e5]` **c ) Lý lịch cán bộ ( Mẫu 2C – TCTW ) ;** → `DIEM` (span: `[13:24]`)
- `[e6]` **Mẫu 2C** → `THAM_CHIEU_PHAP_LY` (span: `[18:20]`) *(lồng trong `e5` (`DIEM`))*
- `[e7]` **cán bộ** → `CHU_THE_CA_NHAN` (span: `[16:17]`) *(lồng trong `e5` (`DIEM`))*

**Quan hệ:**
- (`e1` 01/2009/TT-BNV `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Nội vụ `[CO_QUAN_BAN_HANH]`)
- (`e1` 01/2009/TT-BNV `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 2 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 01/2009/TT-BNV `[SO_HIEU]`)
- (`e4` Khoản 4 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 2 `[DIEU]`)
- (`e5` c ) Lý lịch cán bộ ( Mẫu 2C – TCTW ) ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e4` Khoản 4 `[KHOAN]`)
- (`e5` c ) Lý lịch cán bộ ( Mẫu 2C – TCTW ) ; `[DIEM]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e6` Mẫu 2C `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #01_2009_TT-BNV_12219#body_standalone_54 (Loại: `body_standalone`)
> **[Điều 2]`<DIEU>`** . **[Khoản 4]`<KHOAN>`** . **[c ) Lý lịch **[cán bộ]`<CHU_THE_CA_NHAN>`** ( **[Mẫu 2C]`<THAM_CHIEU_PHAP_LY>`** – TCTW ) ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Điều 2** → `DIEU` (span: `[0:2]`)
- `[e1]` **Khoản 4** → `KHOAN` (span: `[3:5]`)
- `[e2]` **c ) Lý lịch cán bộ ( Mẫu 2C – TCTW ) ;** → `DIEM` (span: `[6:17]`)
- `[e3]` **Mẫu 2C** → `THAM_CHIEU_PHAP_LY` (span: `[11:13]`) *(lồng trong `e2` (`DIEM`))*
- `[e4]` **cán bộ** → `CHU_THE_CA_NHAN` (span: `[9:10]`) *(lồng trong `e2` (`DIEM`))*

**Quan hệ:**
- (`e1` Khoản 4 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 2 `[DIEU]`)
- (`e2` c ) Lý lịch cán bộ ( Mẫu 2C – TCTW ) ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e1` Khoản 4 `[KHOAN]`)
- (`e2` c ) Lý lịch cán bộ ( Mẫu 2C – TCTW ) ; `[DIEM]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Mẫu 2C `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #01_2009_TT-BNV_12219#body_context_55 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[01/2009/TT-BNV]`<SO_HIEU>`** của **[Bộ Nội vụ]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Nội vụ]`<LINH_VUC>`** . **[Điều 2]`<DIEU>`** . **[Khoản 4]`<KHOAN>`** . **[d ) **[Bản kê khai tài sản]`<GIAY_TO_HO_SO>`** theo quy định của **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** .]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **01/2009/TT-BNV** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Nội vụ** → `CO_QUAN_BAN_HANH` (span: `[4:6]`)
- `[e3]` **Nội vụ** → `LINH_VUC` (span: `[8:9]`)
- `[e4]` **Điều 2** → `DIEU` (span: `[10:12]`)
- `[e5]` **Khoản 4** → `KHOAN` (span: `[13:15]`)
- `[e6]` **d ) Bản kê khai tài sản theo quy định của Chính phủ .** → `DIEM` (span: `[16:26]`)
- `[e7]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[24:25]`) *(lồng trong `e6` (`DIEM`))*
- `[e8]` **Bản kê khai tài sản** → `GIAY_TO_HO_SO` (span: `[18:21]`) *(lồng trong `e6` (`DIEM`))*

**Quan hệ:**
- (`e1` 01/2009/TT-BNV `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Nội vụ `[CO_QUAN_BAN_HANH]`)
- (`e1` 01/2009/TT-BNV `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 01/2009/TT-BNV `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Nội vụ `[LINH_VUC]`)
- (`e4` Điều 2 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 01/2009/TT-BNV `[SO_HIEU]`)
- (`e5` Khoản 4 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 2 `[DIEU]`)
- (`e6` d ) Bản kê khai tài sản theo quy định của Chính phủ . `[DIEM]`) ==[ **THUOC_VE** ]==> (`e5` Khoản 4 `[KHOAN]`)
- (`e1` 01/2009/TT-BNV `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Nội vụ `[LINH_VUC]`)
- (`e6` d ) Bản kê khai tài sản theo quy định của Chính phủ . `[DIEM]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Nội vụ `[LINH_VUC]`)


---

### Mẫu #01_2009_TT-BNV_12219#body_standalone_56 (Loại: `body_standalone`)
> **[Điều 2]`<DIEU>`** . **[Khoản 4]`<KHOAN>`** . **[d ) **[Bản kê khai tài sản]`<GIAY_TO_HO_SO>`** theo quy định của **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** .]`<DIEM>`**

**Thực thể:**
- `[e0]` **Điều 2** → `DIEU` (span: `[0:2]`)
- `[e1]` **Khoản 4** → `KHOAN` (span: `[3:5]`)
- `[e2]` **d ) Bản kê khai tài sản theo quy định của Chính phủ .** → `DIEM` (span: `[6:16]`)
- `[e3]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[14:15]`) *(lồng trong `e2` (`DIEM`))*
- `[e4]` **Bản kê khai tài sản** → `GIAY_TO_HO_SO` (span: `[8:11]`) *(lồng trong `e2` (`DIEM`))*

**Quan hệ:**
- (`e1` Khoản 4 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 2 `[DIEU]`)
- (`e2` d ) Bản kê khai tài sản theo quy định của Chính phủ . `[DIEM]`) ==[ **THUOC_VE** ]==> (`e1` Khoản 4 `[KHOAN]`)


---

### Mẫu #01_2009_TT-BNV_12219#body_context_57 (Loại: `body_context`)
> **[Bộ Nội vụ]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[01/2009/TT-BNV]`<SO_HIEU>`** . **[Điều 3 . Trình tự , thủ tục miễn nhiệm]`<DIEU>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[3:4]`)
- `[e1]` **01/2009/TT-BNV** → `SO_HIEU` (span: `[5:6]`)
- `[e2]` **Bộ Nội vụ** → `CO_QUAN_BAN_HANH` (span: `[0:2]`)
- `[e3]` **Điều 3 . Trình tự , thủ tục miễn nhiệm** → `DIEU` (span: `[7:14]`)

**Quan hệ:**
- (`e1` 01/2009/TT-BNV `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Nội vụ `[CO_QUAN_BAN_HANH]`)
- (`e1` 01/2009/TT-BNV `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 3 . Trình tự , thủ tục miễn nhiệm `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 01/2009/TT-BNV `[SO_HIEU]`)


---

### Mẫu #01_2009_TT-BNV_12219#body_context_58 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[01/2009/TT-BNV]`<SO_HIEU>`** của **[Bộ Nội vụ]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Nội vụ]`<LINH_VUC>`** . **[Điều 3]`<DIEU>`** . **[1 . Các trường hợp miễn nhiệm Miễn nhiệm Chủ tịch , Phó Chủ tịch và Ủy viên **[Ủy ban nhân dân huyện , quận , phường]`<CO_QUAN_THAM_QUYEN>`** **[nơi thực hiện thí điểm]`<DIA_DIEM>`** trong các trường hợp sau đây :]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **01/2009/TT-BNV** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Nội vụ** → `CO_QUAN_BAN_HANH` (span: `[4:6]`)
- `[e3]` **Nội vụ** → `LINH_VUC` (span: `[8:9]`)
- `[e4]` **Điều 3** → `DIEU` (span: `[10:12]`)
- `[e5]` **1 . Các trường hợp miễn nhiệm Miễn nhiệm Chủ tịch , Phó Chủ tịch và Ủy viên Ủy ban nhân dân huyện , quận , phường nơi thực hiện thí điểm trong các trường hợp sau đây :** → `KHOAN` (span: `[13:40]`)
- `[e6]` **Ủy ban nhân dân huyện , quận , phường** → `CO_QUAN_THAM_QUYEN` (span: `[24:31]`) *(lồng trong `e5` (`KHOAN`))*
- `[e7]` **nơi thực hiện thí điểm** → `DIA_DIEM` (span: `[31:34]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 01/2009/TT-BNV `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Nội vụ `[CO_QUAN_BAN_HANH]`)
- (`e1` 01/2009/TT-BNV `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 01/2009/TT-BNV `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Nội vụ `[LINH_VUC]`)
- (`e4` Điều 3 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 01/2009/TT-BNV `[SO_HIEU]`)
- (`e5` 1 . Các trường hợp miễn nhiệm Miễn nhiệm Chủ tịch , Phó Chủ tịch và Ủy viên Ủy ban nhân dân huyện , quận , phường nơi thực hiện thí điểm trong các trường hợp sau đây : `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 3 `[DIEU]`)
- (`e1` 01/2009/TT-BNV `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Nội vụ `[LINH_VUC]`)
- (`e5` 1 . Các trường hợp miễn nhiệm Miễn nhiệm Chủ tịch , Phó Chủ tịch và Ủy viên Ủy ban nhân dân huyện , quận , phường nơi thực hiện thí điểm trong các trường hợp sau đây : `[KHOAN]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Nội vụ `[LINH_VUC]`)


---

### Mẫu #01_2009_TT-BNV_12219#body_standalone_59 (Loại: `body_standalone`)
> **[Điều 3]`<DIEU>`** . **[1 . Các trường hợp miễn nhiệm Miễn nhiệm Chủ tịch , Phó Chủ tịch và Ủy viên **[Ủy ban nhân dân huyện , quận , phường]`<CO_QUAN_THAM_QUYEN>`** **[nơi thực hiện thí điểm]`<DIA_DIEM>`** trong các trường hợp sau đây :]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 3** → `DIEU` (span: `[0:2]`)
- `[e1]` **1 . Các trường hợp miễn nhiệm Miễn nhiệm Chủ tịch , Phó Chủ tịch và Ủy viên Ủy ban nhân dân huyện , quận , phường nơi thực hiện thí điểm trong các trường hợp sau đây :** → `KHOAN` (span: `[3:30]`)
- `[e2]` **Ủy ban nhân dân huyện , quận , phường** → `CO_QUAN_THAM_QUYEN` (span: `[14:21]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **nơi thực hiện thí điểm** → `DIA_DIEM` (span: `[21:24]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 1 . Các trường hợp miễn nhiệm Miễn nhiệm Chủ tịch , Phó Chủ tịch và Ủy viên Ủy ban nhân dân huyện , quận , phường nơi thực hiện thí điểm trong các trường hợp sau đây : `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 3 `[DIEU]`)


---

### Mẫu #01_2009_TT-BNV_12219#body_context_60 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[01/2009/TT-BNV]`<SO_HIEU>`** ban hành **[ngày 19 tháng 03 năm 2009]`<NGAY_BAN_HANH>`** bởi **[Bộ Nội vụ]`<CO_QUAN_BAN_HANH>`** . **[Điều 3]`<DIEU>`** . **[Khoản 1 . Miễn nhiệm Chủ tịch , Phó Chủ tịch và Ủy viên **[Ủy ban nhân dân huyện , quận , phường]`<CO_QUAN_THAM_QUYEN>`** **[nơi thực hiện thí điểm]`<DIA_DIEM>`** trong các trường hợp sau đây]`<KHOAN>`** : **[a ) Không đủ sức khỏe ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **01/2009/TT-BNV** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Nội vụ** → `CO_QUAN_BAN_HANH` (span: `[11:13]`)
- `[e3]` **ngày 19 tháng 03 năm 2009** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 3** → `DIEU` (span: `[14:16]`)
- `[e5]` **Khoản 1 . Miễn nhiệm Chủ tịch , Phó Chủ tịch và Ủy viên Ủy ban nhân dân huyện , quận , phường nơi thực hiện thí điểm trong các trường hợp sau đây** → `KHOAN` (span: `[17:41]`)
- `[e6]` **a ) Không đủ sức khỏe ;** → `DIEM` (span: `[42:48]`)
- `[e7]` **Ủy ban nhân dân huyện , quận , phường** → `CO_QUAN_THAM_QUYEN` (span: `[26:33]`) *(lồng trong `e5` (`KHOAN`))*
- `[e8]` **nơi thực hiện thí điểm** → `DIA_DIEM` (span: `[33:36]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 01/2009/TT-BNV `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Nội vụ `[CO_QUAN_BAN_HANH]`)
- (`e1` 01/2009/TT-BNV `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 01/2009/TT-BNV `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 19 tháng 03 năm 2009 `[NGAY_BAN_HANH]`)
- (`e4` Điều 3 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 01/2009/TT-BNV `[SO_HIEU]`)
- (`e5` Khoản 1 . Miễn nhiệm Chủ tịch , Phó Chủ tịch và Ủy viên Ủy ban nhân dân huyện , quận , phường nơi thực hiện thí điểm trong các trường hợp sau đây `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 3 `[DIEU]`)
- (`e6` a ) Không đủ sức khỏe ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e5` Khoản 1 . Miễn nhiệm Chủ tịch , Phó Chủ tịch và Ủy viên Ủy ban nhân dân huyện , quận , phường nơi thực hiện thí điểm trong các trường hợp sau đây `[KHOAN]`)


---

### Mẫu #01_2009_TT-BNV_12219#body_standalone_61 (Loại: `body_standalone`)
> **[Điều 3]`<DIEU>`** . **[Khoản 1 . Miễn nhiệm Chủ tịch , Phó Chủ tịch và Ủy viên **[Ủy ban nhân dân huyện , quận , phường]`<CO_QUAN_THAM_QUYEN>`** **[nơi thực hiện thí điểm]`<DIA_DIEM>`** trong các trường hợp sau đây]`<KHOAN>`** : **[a ) Không đủ sức khỏe ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Điều 3** → `DIEU` (span: `[0:2]`)
- `[e1]` **Khoản 1 . Miễn nhiệm Chủ tịch , Phó Chủ tịch và Ủy viên Ủy ban nhân dân huyện , quận , phường nơi thực hiện thí điểm trong các trường hợp sau đây** → `KHOAN` (span: `[3:27]`)
- `[e2]` **a ) Không đủ sức khỏe ;** → `DIEM` (span: `[28:34]`)
- `[e3]` **Ủy ban nhân dân huyện , quận , phường** → `CO_QUAN_THAM_QUYEN` (span: `[12:19]`) *(lồng trong `e1` (`KHOAN`))*
- `[e4]` **nơi thực hiện thí điểm** → `DIA_DIEM` (span: `[19:22]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` Khoản 1 . Miễn nhiệm Chủ tịch , Phó Chủ tịch và Ủy viên Ủy ban nhân dân huyện , quận , phường nơi thực hiện thí điểm trong các trường hợp sau đây `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 3 `[DIEU]`)
- (`e2` a ) Không đủ sức khỏe ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e1` Khoản 1 . Miễn nhiệm Chủ tịch , Phó Chủ tịch và Ủy viên Ủy ban nhân dân huyện , quận , phường nơi thực hiện thí điểm trong các trường hợp sau đây `[KHOAN]`)


---

### Mẫu #01_2009_TT-BNV_12219#body_context_62 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[01/2009/TT-BNV]`<SO_HIEU>`** ban hành **[ngày 19 tháng 03 năm 2009]`<NGAY_BAN_HANH>`** bởi **[Bộ Nội vụ]`<CO_QUAN_BAN_HANH>`** . **[Điều 3]`<DIEU>`** . **[Khoản 1 . Miễn nhiệm Chủ tịch , Phó Chủ tịch và Ủy viên **[Ủy ban nhân dân huyện , quận , phường]`<CO_QUAN_THAM_QUYEN>`** **[nơi thực hiện thí điểm]`<DIA_DIEM>`** trong các trường hợp sau đây]`<KHOAN>`** : **[b ) Không đủ năng lực và uy tín để hoàn thành nhiệm vụ được giao ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **01/2009/TT-BNV** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Nội vụ** → `CO_QUAN_BAN_HANH` (span: `[11:13]`)
- `[e3]` **ngày 19 tháng 03 năm 2009** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 3** → `DIEU` (span: `[14:16]`)
- `[e5]` **Khoản 1 . Miễn nhiệm Chủ tịch , Phó Chủ tịch và Ủy viên Ủy ban nhân dân huyện , quận , phường nơi thực hiện thí điểm trong các trường hợp sau đây** → `KHOAN` (span: `[17:41]`)
- `[e6]` **b ) Không đủ năng lực và uy tín để hoàn thành nhiệm vụ được giao ;** → `DIEM` (span: `[42:55]`)
- `[e7]` **Ủy ban nhân dân huyện , quận , phường** → `CO_QUAN_THAM_QUYEN` (span: `[26:33]`) *(lồng trong `e5` (`KHOAN`))*
- `[e8]` **nơi thực hiện thí điểm** → `DIA_DIEM` (span: `[33:36]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 01/2009/TT-BNV `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Nội vụ `[CO_QUAN_BAN_HANH]`)
- (`e1` 01/2009/TT-BNV `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 01/2009/TT-BNV `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 19 tháng 03 năm 2009 `[NGAY_BAN_HANH]`)
- (`e4` Điều 3 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 01/2009/TT-BNV `[SO_HIEU]`)
- (`e5` Khoản 1 . Miễn nhiệm Chủ tịch , Phó Chủ tịch và Ủy viên Ủy ban nhân dân huyện , quận , phường nơi thực hiện thí điểm trong các trường hợp sau đây `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 3 `[DIEU]`)
- (`e6` b ) Không đủ năng lực và uy tín để hoàn thành nhiệm vụ được giao ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e5` Khoản 1 . Miễn nhiệm Chủ tịch , Phó Chủ tịch và Ủy viên Ủy ban nhân dân huyện , quận , phường nơi thực hiện thí điểm trong các trường hợp sau đây `[KHOAN]`)


---

### Mẫu #01_2009_TT-BNV_12219#body_standalone_63 (Loại: `body_standalone`)
> **[Điều 3]`<DIEU>`** . **[Khoản 1 . Miễn nhiệm Chủ tịch , Phó Chủ tịch và Ủy viên **[Ủy ban nhân dân huyện , quận , phường]`<CO_QUAN_THAM_QUYEN>`** **[nơi thực hiện thí điểm]`<DIA_DIEM>`** trong các trường hợp sau đây]`<KHOAN>`** : **[b ) Không đủ năng lực và uy tín để hoàn thành nhiệm vụ được giao ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Điều 3** → `DIEU` (span: `[0:2]`)
- `[e1]` **Khoản 1 . Miễn nhiệm Chủ tịch , Phó Chủ tịch và Ủy viên Ủy ban nhân dân huyện , quận , phường nơi thực hiện thí điểm trong các trường hợp sau đây** → `KHOAN` (span: `[3:27]`)
- `[e2]` **b ) Không đủ năng lực và uy tín để hoàn thành nhiệm vụ được giao ;** → `DIEM` (span: `[28:41]`)
- `[e3]` **Ủy ban nhân dân huyện , quận , phường** → `CO_QUAN_THAM_QUYEN` (span: `[12:19]`) *(lồng trong `e1` (`KHOAN`))*
- `[e4]` **nơi thực hiện thí điểm** → `DIA_DIEM` (span: `[19:22]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` Khoản 1 . Miễn nhiệm Chủ tịch , Phó Chủ tịch và Ủy viên Ủy ban nhân dân huyện , quận , phường nơi thực hiện thí điểm trong các trường hợp sau đây `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 3 `[DIEU]`)
- (`e2` b ) Không đủ năng lực và uy tín để hoàn thành nhiệm vụ được giao ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e1` Khoản 1 . Miễn nhiệm Chủ tịch , Phó Chủ tịch và Ủy viên Ủy ban nhân dân huyện , quận , phường nơi thực hiện thí điểm trong các trường hợp sau đây `[KHOAN]`)


---

### Mẫu #01_2009_TT-BNV_12219#body_context_64 (Loại: `body_context`)
> **[Bộ Nội vụ]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[01/2009/TT-BNV]`<SO_HIEU>`** . **[Điều 3]`<DIEU>`** . **[Khoản 1 . Miễn nhiệm Chủ tịch , Phó Chủ tịch và Ủy viên **[Ủy ban nhân dân huyện , quận , phường]`<CO_QUAN_THAM_QUYEN>`** **[nơi thực hiện thí điểm]`<DIA_DIEM>`** trong các trường hợp sau đây]`<KHOAN>`** : **[c ) Theo yêu cầu nhiệm vụ của cơ quan quản lý **[cán bộ]`<CHU_THE_CA_NHAN>`** có thẩm quyền ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[3:4]`)
- `[e1]` **01/2009/TT-BNV** → `SO_HIEU` (span: `[5:6]`)
- `[e2]` **Bộ Nội vụ** → `CO_QUAN_BAN_HANH` (span: `[0:2]`)
- `[e3]` **Điều 3** → `DIEU` (span: `[7:9]`)
- `[e4]` **Khoản 1 . Miễn nhiệm Chủ tịch , Phó Chủ tịch và Ủy viên Ủy ban nhân dân huyện , quận , phường nơi thực hiện thí điểm trong các trường hợp sau đây** → `KHOAN` (span: `[10:34]`)
- `[e5]` **c ) Theo yêu cầu nhiệm vụ của cơ quan quản lý cán bộ có thẩm quyền ;** → `DIEM` (span: `[35:47]`)
- `[e6]` **Ủy ban nhân dân huyện , quận , phường** → `CO_QUAN_THAM_QUYEN` (span: `[19:26]`) *(lồng trong `e4` (`KHOAN`))*
- `[e7]` **cán bộ** → `CHU_THE_CA_NHAN` (span: `[43:44]`) *(lồng trong `e5` (`DIEM`))*
- `[e8]` **nơi thực hiện thí điểm** → `DIA_DIEM` (span: `[26:29]`) *(lồng trong `e4` (`KHOAN`))*

**Quan hệ:**
- (`e1` 01/2009/TT-BNV `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Nội vụ `[CO_QUAN_BAN_HANH]`)
- (`e1` 01/2009/TT-BNV `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 3 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 01/2009/TT-BNV `[SO_HIEU]`)
- (`e4` Khoản 1 . Miễn nhiệm Chủ tịch , Phó Chủ tịch và Ủy viên Ủy ban nhân dân huyện , quận , phường nơi thực hiện thí điểm trong các trường hợp sau đây `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 3 `[DIEU]`)
- (`e5` c ) Theo yêu cầu nhiệm vụ của cơ quan quản lý cán bộ có thẩm quyền ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e4` Khoản 1 . Miễn nhiệm Chủ tịch , Phó Chủ tịch và Ủy viên Ủy ban nhân dân huyện , quận , phường nơi thực hiện thí điểm trong các trường hợp sau đây `[KHOAN]`)


---

### Mẫu #01_2009_TT-BNV_12219#body_standalone_65 (Loại: `body_standalone`)
> **[Điều 3]`<DIEU>`** . **[Khoản 1 . Miễn nhiệm Chủ tịch , Phó Chủ tịch và Ủy viên **[Ủy ban nhân dân huyện , quận , phường]`<CO_QUAN_THAM_QUYEN>`** **[nơi thực hiện thí điểm]`<DIA_DIEM>`** trong các trường hợp sau đây]`<KHOAN>`** : **[c ) Theo yêu cầu nhiệm vụ của cơ quan quản lý **[cán bộ]`<CHU_THE_CA_NHAN>`** có thẩm quyền ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Điều 3** → `DIEU` (span: `[0:2]`)
- `[e1]` **Khoản 1 . Miễn nhiệm Chủ tịch , Phó Chủ tịch và Ủy viên Ủy ban nhân dân huyện , quận , phường nơi thực hiện thí điểm trong các trường hợp sau đây** → `KHOAN` (span: `[3:27]`)
- `[e2]` **c ) Theo yêu cầu nhiệm vụ của cơ quan quản lý cán bộ có thẩm quyền ;** → `DIEM` (span: `[28:40]`)
- `[e3]` **Ủy ban nhân dân huyện , quận , phường** → `CO_QUAN_THAM_QUYEN` (span: `[12:19]`) *(lồng trong `e1` (`KHOAN`))*
- `[e4]` **cán bộ** → `CHU_THE_CA_NHAN` (span: `[36:37]`) *(lồng trong `e2` (`DIEM`))*
- `[e5]` **nơi thực hiện thí điểm** → `DIA_DIEM` (span: `[19:22]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` Khoản 1 . Miễn nhiệm Chủ tịch , Phó Chủ tịch và Ủy viên Ủy ban nhân dân huyện , quận , phường nơi thực hiện thí điểm trong các trường hợp sau đây `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 3 `[DIEU]`)
- (`e2` c ) Theo yêu cầu nhiệm vụ của cơ quan quản lý cán bộ có thẩm quyền ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e1` Khoản 1 . Miễn nhiệm Chủ tịch , Phó Chủ tịch và Ủy viên Ủy ban nhân dân huyện , quận , phường nơi thực hiện thí điểm trong các trường hợp sau đây `[KHOAN]`)


---

### Mẫu #01_2009_TT-BNV_12219#body_context_66 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[01/2009/TT-BNV]`<SO_HIEU>`** ban hành **[ngày 19 tháng 03 năm 2009]`<NGAY_BAN_HANH>`** bởi **[Bộ Nội vụ]`<CO_QUAN_BAN_HANH>`** . **[Điều 3]`<DIEU>`** . **[Khoản 1 . Miễn nhiệm Chủ tịch , Phó Chủ tịch và Ủy viên **[Ủy ban nhân dân huyện , quận , phường]`<CO_QUAN_THAM_QUYEN>`** **[nơi thực hiện thí điểm]`<DIA_DIEM>`** trong các trường hợp sau đây]`<KHOAN>`** : **[d ) Vì lý do cá nhân khác .]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **01/2009/TT-BNV** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Nội vụ** → `CO_QUAN_BAN_HANH` (span: `[11:13]`)
- `[e3]` **ngày 19 tháng 03 năm 2009** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 3** → `DIEU` (span: `[14:16]`)
- `[e5]` **Khoản 1 . Miễn nhiệm Chủ tịch , Phó Chủ tịch và Ủy viên Ủy ban nhân dân huyện , quận , phường nơi thực hiện thí điểm trong các trường hợp sau đây** → `KHOAN` (span: `[17:41]`)
- `[e6]` **d ) Vì lý do cá nhân khác .** → `DIEM` (span: `[42:49]`)
- `[e7]` **Ủy ban nhân dân huyện , quận , phường** → `CO_QUAN_THAM_QUYEN` (span: `[26:33]`) *(lồng trong `e5` (`KHOAN`))*
- `[e8]` **nơi thực hiện thí điểm** → `DIA_DIEM` (span: `[33:36]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 01/2009/TT-BNV `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Nội vụ `[CO_QUAN_BAN_HANH]`)
- (`e1` 01/2009/TT-BNV `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 01/2009/TT-BNV `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 19 tháng 03 năm 2009 `[NGAY_BAN_HANH]`)
- (`e4` Điều 3 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 01/2009/TT-BNV `[SO_HIEU]`)
- (`e5` Khoản 1 . Miễn nhiệm Chủ tịch , Phó Chủ tịch và Ủy viên Ủy ban nhân dân huyện , quận , phường nơi thực hiện thí điểm trong các trường hợp sau đây `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 3 `[DIEU]`)
- (`e6` d ) Vì lý do cá nhân khác . `[DIEM]`) ==[ **THUOC_VE** ]==> (`e5` Khoản 1 . Miễn nhiệm Chủ tịch , Phó Chủ tịch và Ủy viên Ủy ban nhân dân huyện , quận , phường nơi thực hiện thí điểm trong các trường hợp sau đây `[KHOAN]`)


---

### Mẫu #01_2009_TT-BNV_12219#body_standalone_67 (Loại: `body_standalone`)
> **[Điều 3]`<DIEU>`** . **[Khoản 1 . Miễn nhiệm Chủ tịch , Phó Chủ tịch và Ủy viên **[Ủy ban nhân dân huyện , quận , phường]`<CO_QUAN_THAM_QUYEN>`** **[nơi thực hiện thí điểm]`<DIA_DIEM>`** trong các trường hợp sau đây]`<KHOAN>`** : **[d ) Vì lý do cá nhân khác .]`<DIEM>`**

**Thực thể:**
- `[e0]` **Điều 3** → `DIEU` (span: `[0:2]`)
- `[e1]` **Khoản 1 . Miễn nhiệm Chủ tịch , Phó Chủ tịch và Ủy viên Ủy ban nhân dân huyện , quận , phường nơi thực hiện thí điểm trong các trường hợp sau đây** → `KHOAN` (span: `[3:27]`)
- `[e2]` **d ) Vì lý do cá nhân khác .** → `DIEM` (span: `[28:35]`)
- `[e3]` **Ủy ban nhân dân huyện , quận , phường** → `CO_QUAN_THAM_QUYEN` (span: `[12:19]`) *(lồng trong `e1` (`KHOAN`))*
- `[e4]` **nơi thực hiện thí điểm** → `DIA_DIEM` (span: `[19:22]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` Khoản 1 . Miễn nhiệm Chủ tịch , Phó Chủ tịch và Ủy viên Ủy ban nhân dân huyện , quận , phường nơi thực hiện thí điểm trong các trường hợp sau đây `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 3 `[DIEU]`)
- (`e2` d ) Vì lý do cá nhân khác . `[DIEM]`) ==[ **THUOC_VE** ]==> (`e1` Khoản 1 . Miễn nhiệm Chủ tịch , Phó Chủ tịch và Ủy viên Ủy ban nhân dân huyện , quận , phường nơi thực hiện thí điểm trong các trường hợp sau đây `[KHOAN]`)


---

### Mẫu #01_2009_TT-BNV_12219#body_context_68 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[01/2009/TT-BNV]`<SO_HIEU>`** ban hành **[ngày 19 tháng 03 năm 2009]`<NGAY_BAN_HANH>`** bởi **[Bộ Nội vụ]`<CO_QUAN_BAN_HANH>`** . **[Điều 3]`<DIEU>`** . **[Khoản 2]`<KHOAN>`** . **[a ) Căn cứ **[thông báo bằng văn bản]`<GIAY_TO_HO_SO>`** về chủ trương của **[cấp có thẩm quyền quản lý cán bộ]`<CO_QUAN_THAM_QUYEN>`** , **[Ủy ban nhân dân huyện , quận , phường]`<CO_QUAN_THAM_QUYEN>`** đề xuất việc miễn nhiệm **[Chủ tịch Ủy ban nhân dân cùng cấp]`<CO_QUAN_THAM_QUYEN>`** ; **[Chủ tịch Ủy ban nhân dân huyện , quận , phường]`<CO_QUAN_THAM_QUYEN>`** đề xuất việc miễn nhiệm Phó Chủ tịch và Ủy viên **[Ủy ban nhân dân cùng cấp]`<CO_QUAN_THAM_QUYEN>`** .]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **01/2009/TT-BNV** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Nội vụ** → `CO_QUAN_BAN_HANH` (span: `[11:13]`)
- `[e3]` **ngày 19 tháng 03 năm 2009** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 3** → `DIEU` (span: `[14:16]`)
- `[e5]` **Khoản 2** → `KHOAN` (span: `[17:19]`)
- `[e6]` **a ) Căn cứ thông báo bằng văn bản về chủ trương của cấp có thẩm quyền quản lý cán bộ , Ủy ban nhân dân huyện , quận , phường đề xuất việc miễn nhiệm Chủ tịch Ủy ban nhân dân cùng cấp ; Chủ tịch Ủy ban nhân dân huyện , quận , phường đề xuất việc miễn nhiệm Phó Chủ tịch và Ủy viên Ủy ban nhân dân cùng cấp .** → `DIEM` (span: `[20:70]`)
- `[e7]` **cấp có thẩm quyền quản lý cán bộ** → `CO_QUAN_THAM_QUYEN` (span: `[29:34]`) *(lồng trong `e6` (`DIEM`))*
- `[e8]` **Ủy ban nhân dân huyện , quận , phường** → `CO_QUAN_THAM_QUYEN` (span: `[35:42]`) *(lồng trong `e6` (`DIEM`))*
- `[e9]` **Chủ tịch Ủy ban nhân dân cùng cấp** → `CO_QUAN_THAM_QUYEN` (span: `[45:50]`) *(lồng trong `e6` (`DIEM`))*
- `[e10]` **Chủ tịch Ủy ban nhân dân huyện , quận , phường** → `CO_QUAN_THAM_QUYEN` (span: `[51:59]`) *(lồng trong `e6` (`DIEM`))*
- `[e11]` **Ủy ban nhân dân cùng cấp** → `CO_QUAN_THAM_QUYEN` (span: `[65:69]`) *(lồng trong `e6` (`DIEM`))*
- `[e12]` **thông báo bằng văn bản** → `GIAY_TO_HO_SO` (span: `[23:26]`) *(lồng trong `e6` (`DIEM`))*

**Quan hệ:**
- (`e1` 01/2009/TT-BNV `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Nội vụ `[CO_QUAN_BAN_HANH]`)
- (`e1` 01/2009/TT-BNV `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 01/2009/TT-BNV `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 19 tháng 03 năm 2009 `[NGAY_BAN_HANH]`)
- (`e4` Điều 3 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 01/2009/TT-BNV `[SO_HIEU]`)
- (`e5` Khoản 2 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 3 `[DIEU]`)
- (`e6` a ) Căn cứ thông báo bằng văn bản về chủ trương của cấp có thẩm quyền quản lý cán bộ , Ủy ban nhân dân huyện , quận , phường đề xuất việc miễn nhiệm Chủ tịch Ủy ban nhân dân cùng cấp ; Chủ tịch Ủy ban nhân dân huyện , quận , phường đề xuất việc miễn nhiệm Phó Chủ tịch và Ủy viên Ủy ban nhân dân cùng cấp . `[DIEM]`) ==[ **THUOC_VE** ]==> (`e5` Khoản 2 `[KHOAN]`)


---

### Mẫu #01_2009_TT-BNV_12219#body_standalone_69 (Loại: `body_standalone`)
> **[Điều 3]`<DIEU>`** . **[Khoản 2]`<KHOAN>`** . **[a ) Căn cứ **[thông báo bằng văn bản]`<GIAY_TO_HO_SO>`** về chủ trương của **[cấp có thẩm quyền quản lý cán bộ]`<CO_QUAN_THAM_QUYEN>`** , **[Ủy ban nhân dân huyện , quận , phường]`<CO_QUAN_THAM_QUYEN>`** đề xuất việc miễn nhiệm **[Chủ tịch Ủy ban nhân dân cùng cấp]`<CO_QUAN_THAM_QUYEN>`** ; **[Chủ tịch Ủy ban nhân dân huyện , quận , phường]`<CO_QUAN_THAM_QUYEN>`** đề xuất việc miễn nhiệm Phó Chủ tịch và Ủy viên **[Ủy ban nhân dân cùng cấp]`<CO_QUAN_THAM_QUYEN>`** .]`<DIEM>`**

**Thực thể:**
- `[e0]` **Điều 3** → `DIEU` (span: `[0:2]`)
- `[e1]` **Khoản 2** → `KHOAN` (span: `[3:5]`)
- `[e2]` **a ) Căn cứ thông báo bằng văn bản về chủ trương của cấp có thẩm quyền quản lý cán bộ , Ủy ban nhân dân huyện , quận , phường đề xuất việc miễn nhiệm Chủ tịch Ủy ban nhân dân cùng cấp ; Chủ tịch Ủy ban nhân dân huyện , quận , phường đề xuất việc miễn nhiệm Phó Chủ tịch và Ủy viên Ủy ban nhân dân cùng cấp .** → `DIEM` (span: `[6:56]`)
- `[e3]` **cấp có thẩm quyền quản lý cán bộ** → `CO_QUAN_THAM_QUYEN` (span: `[15:20]`) *(lồng trong `e2` (`DIEM`))*
- `[e4]` **Ủy ban nhân dân huyện , quận , phường** → `CO_QUAN_THAM_QUYEN` (span: `[21:28]`) *(lồng trong `e2` (`DIEM`))*
- `[e5]` **Chủ tịch Ủy ban nhân dân cùng cấp** → `CO_QUAN_THAM_QUYEN` (span: `[31:36]`) *(lồng trong `e2` (`DIEM`))*
- `[e6]` **Chủ tịch Ủy ban nhân dân huyện , quận , phường** → `CO_QUAN_THAM_QUYEN` (span: `[37:45]`) *(lồng trong `e2` (`DIEM`))*
- `[e7]` **Ủy ban nhân dân cùng cấp** → `CO_QUAN_THAM_QUYEN` (span: `[51:55]`) *(lồng trong `e2` (`DIEM`))*
- `[e8]` **thông báo bằng văn bản** → `GIAY_TO_HO_SO` (span: `[9:12]`) *(lồng trong `e2` (`DIEM`))*

**Quan hệ:**
- (`e1` Khoản 2 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 3 `[DIEU]`)
- (`e2` a ) Căn cứ thông báo bằng văn bản về chủ trương của cấp có thẩm quyền quản lý cán bộ , Ủy ban nhân dân huyện , quận , phường đề xuất việc miễn nhiệm Chủ tịch Ủy ban nhân dân cùng cấp ; Chủ tịch Ủy ban nhân dân huyện , quận , phường đề xuất việc miễn nhiệm Phó Chủ tịch và Ủy viên Ủy ban nhân dân cùng cấp . `[DIEM]`) ==[ **THUOC_VE** ]==> (`e1` Khoản 2 `[KHOAN]`)


---

### Mẫu #01_2009_TT-BNV_12219#body_context_70 (Loại: `body_context`)
> **[Bộ Nội vụ]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[01/2009/TT-BNV]`<SO_HIEU>`** . **[Điều 3]`<DIEU>`** . **[Khoản 2]`<KHOAN>`** . **[b ) **[Sở Nội vụ]`<CO_QUAN_THAM_QUYEN>`** ( đối với miễn nhiệm Chủ tịch , Phó Chủ tịch và Ủy viên **[Ủy ban nhân dân huyện , quận]`<CO_QUAN_THAM_QUYEN>`** ) , **[Phòng Nội vụ]`<CO_QUAN_THAM_QUYEN>`** ( đối với miễn nhiệm Chủ tịch , Phó Chủ tịch và Ủy viên **[Ủy ban nhân dân phường]`<CO_QUAN_THAM_QUYEN>`** ) phối hợp với các cơ quan chức năng làm công tác tổ chức **[cán bộ]`<CHU_THE_CA_NHAN>`** , tiến hành : - Tiếp xúc với **[cán bộ]`<CHU_THE_CA_NHAN>`** miễn nhiệm ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[3:4]`)
- `[e1]` **01/2009/TT-BNV** → `SO_HIEU` (span: `[5:6]`)
- `[e2]` **Bộ Nội vụ** → `CO_QUAN_BAN_HANH` (span: `[0:2]`)
- `[e3]` **Điều 3** → `DIEU` (span: `[7:9]`)
- `[e4]` **Khoản 2** → `KHOAN` (span: `[10:12]`)
- `[e5]` **b ) Sở Nội vụ ( đối với miễn nhiệm Chủ tịch , Phó Chủ tịch và Ủy viên Ủy ban nhân dân huyện , quận ) , Phòng Nội vụ ( đối với miễn nhiệm Chủ tịch , Phó Chủ tịch và Ủy viên Ủy ban nhân dân phường ) phối hợp với các cơ quan chức năng làm công tác tổ chức cán bộ , tiến hành : - Tiếp xúc với cán bộ miễn nhiệm ;** → `DIEM` (span: `[13:63]`)
- `[e6]` **Sở Nội vụ** → `CO_QUAN_THAM_QUYEN` (span: `[15:17]`) *(lồng trong `e5` (`DIEM`))*
- `[e7]` **Ủy ban nhân dân huyện , quận** → `CO_QUAN_THAM_QUYEN` (span: `[25:30]`) *(lồng trong `e5` (`DIEM`))*
- `[e8]` **Phòng Nội vụ** → `CO_QUAN_THAM_QUYEN` (span: `[32:34]`) *(lồng trong `e5` (`DIEM`))*
- `[e9]` **Ủy ban nhân dân phường** → `CO_QUAN_THAM_QUYEN` (span: `[42:45]`) *(lồng trong `e5` (`DIEM`))*
- `[e10]` **cán bộ** → `CHU_THE_CA_NHAN` (span: `[53:54]`) *(lồng trong `e5` (`DIEM`))*
- `[e11]` **cán bộ** → `CHU_THE_CA_NHAN` (span: `[60:61]`) *(lồng trong `e5` (`DIEM`))*

**Quan hệ:**
- (`e1` 01/2009/TT-BNV `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Nội vụ `[CO_QUAN_BAN_HANH]`)
- (`e1` 01/2009/TT-BNV `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 3 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 01/2009/TT-BNV `[SO_HIEU]`)
- (`e4` Khoản 2 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 3 `[DIEU]`)
- (`e5` b ) Sở Nội vụ ( đối với miễn nhiệm Chủ tịch , Phó Chủ tịch và Ủy viên Ủy ban nhân dân huyện , quận ) , Phòng Nội vụ ( đối với miễn nhiệm Chủ tịch , Phó Chủ tịch và Ủy viên Ủy ban nhân dân phường ) phối hợp với các cơ quan chức năng làm công tác tổ chức cán bộ , tiến hành : - Tiếp xúc với cán bộ miễn nhiệm ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e4` Khoản 2 `[KHOAN]`)


---

### Mẫu #01_2009_TT-BNV_12219#body_standalone_71 (Loại: `body_standalone`)
> **[Điều 3]`<DIEU>`** . **[Khoản 2]`<KHOAN>`** . **[b ) **[Sở Nội vụ]`<CO_QUAN_THAM_QUYEN>`** ( đối với miễn nhiệm Chủ tịch , Phó Chủ tịch và Ủy viên **[Ủy ban nhân dân huyện , quận]`<CO_QUAN_THAM_QUYEN>`** ) , **[Phòng Nội vụ]`<CO_QUAN_THAM_QUYEN>`** ( đối với miễn nhiệm Chủ tịch , Phó Chủ tịch và Ủy viên **[Ủy ban nhân dân phường]`<CO_QUAN_THAM_QUYEN>`** ) phối hợp với các cơ quan chức năng làm công tác tổ chức **[cán bộ]`<CHU_THE_CA_NHAN>`** , tiến hành : - Tiếp xúc với **[cán bộ]`<CHU_THE_CA_NHAN>`** miễn nhiệm ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Điều 3** → `DIEU` (span: `[0:2]`)
- `[e1]` **Khoản 2** → `KHOAN` (span: `[3:5]`)
- `[e2]` **b ) Sở Nội vụ ( đối với miễn nhiệm Chủ tịch , Phó Chủ tịch và Ủy viên Ủy ban nhân dân huyện , quận ) , Phòng Nội vụ ( đối với miễn nhiệm Chủ tịch , Phó Chủ tịch và Ủy viên Ủy ban nhân dân phường ) phối hợp với các cơ quan chức năng làm công tác tổ chức cán bộ , tiến hành : - Tiếp xúc với cán bộ miễn nhiệm ;** → `DIEM` (span: `[6:56]`)
- `[e3]` **Sở Nội vụ** → `CO_QUAN_THAM_QUYEN` (span: `[8:10]`) *(lồng trong `e2` (`DIEM`))*
- `[e4]` **Ủy ban nhân dân huyện , quận** → `CO_QUAN_THAM_QUYEN` (span: `[18:23]`) *(lồng trong `e2` (`DIEM`))*
- `[e5]` **Phòng Nội vụ** → `CO_QUAN_THAM_QUYEN` (span: `[25:27]`) *(lồng trong `e2` (`DIEM`))*
- `[e6]` **Ủy ban nhân dân phường** → `CO_QUAN_THAM_QUYEN` (span: `[35:38]`) *(lồng trong `e2` (`DIEM`))*
- `[e7]` **cán bộ** → `CHU_THE_CA_NHAN` (span: `[46:47]`) *(lồng trong `e2` (`DIEM`))*
- `[e8]` **cán bộ** → `CHU_THE_CA_NHAN` (span: `[53:54]`) *(lồng trong `e2` (`DIEM`))*

**Quan hệ:**
- (`e1` Khoản 2 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 3 `[DIEU]`)
- (`e2` b ) Sở Nội vụ ( đối với miễn nhiệm Chủ tịch , Phó Chủ tịch và Ủy viên Ủy ban nhân dân huyện , quận ) , Phòng Nội vụ ( đối với miễn nhiệm Chủ tịch , Phó Chủ tịch và Ủy viên Ủy ban nhân dân phường ) phối hợp với các cơ quan chức năng làm công tác tổ chức cán bộ , tiến hành : - Tiếp xúc với cán bộ miễn nhiệm ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e1` Khoản 2 `[KHOAN]`)


---

### Mẫu #01_2009_TT-BNV_12219#body_context_72 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[01/2009/TT-BNV]`<SO_HIEU>`** của **[Bộ Nội vụ]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Nội vụ]`<LINH_VUC>`** . **[Điều 3]`<DIEU>`** . **[Khoản 2]`<KHOAN>`** . **[b ) **[Sở Nội vụ]`<CO_QUAN_THAM_QUYEN>`** ( đối với miễn nhiệm Chủ tịch , Phó Chủ tịch và Ủy viên **[Ủy ban nhân dân huyện , quận]`<CO_QUAN_THAM_QUYEN>`** ) , **[Phòng Nội vụ]`<CO_QUAN_THAM_QUYEN>`** ( đối với miễn nhiệm Chủ tịch , Phó Chủ tịch và Ủy viên **[Ủy ban nhân dân phường]`<CO_QUAN_THAM_QUYEN>`** ) phối hợp với các cơ quan chức năng làm công tác tổ chức **[cán bộ]`<CHU_THE_CA_NHAN>`** , tiến hành : - Tổng hợp ý kiến các cơ quan có liên quan ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **01/2009/TT-BNV** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Nội vụ** → `CO_QUAN_BAN_HANH` (span: `[4:6]`)
- `[e3]` **Nội vụ** → `LINH_VUC` (span: `[8:9]`)
- `[e4]` **Điều 3** → `DIEU` (span: `[10:12]`)
- `[e5]` **Khoản 2** → `KHOAN` (span: `[13:15]`)
- `[e6]` **b ) Sở Nội vụ ( đối với miễn nhiệm Chủ tịch , Phó Chủ tịch và Ủy viên Ủy ban nhân dân huyện , quận ) , Phòng Nội vụ ( đối với miễn nhiệm Chủ tịch , Phó Chủ tịch và Ủy viên Ủy ban nhân dân phường ) phối hợp với các cơ quan chức năng làm công tác tổ chức cán bộ , tiến hành : - Tổng hợp ý kiến các cơ quan có liên quan ;** → `DIEM` (span: `[16:67]`)
- `[e7]` **Sở Nội vụ** → `CO_QUAN_THAM_QUYEN` (span: `[18:20]`) *(lồng trong `e6` (`DIEM`))*
- `[e8]` **Ủy ban nhân dân huyện , quận** → `CO_QUAN_THAM_QUYEN` (span: `[28:33]`) *(lồng trong `e6` (`DIEM`))*
- `[e9]` **Phòng Nội vụ** → `CO_QUAN_THAM_QUYEN` (span: `[35:37]`) *(lồng trong `e6` (`DIEM`))*
- `[e10]` **Ủy ban nhân dân phường** → `CO_QUAN_THAM_QUYEN` (span: `[45:48]`) *(lồng trong `e6` (`DIEM`))*
- `[e11]` **cán bộ** → `CHU_THE_CA_NHAN` (span: `[56:57]`) *(lồng trong `e6` (`DIEM`))*

**Quan hệ:**
- (`e1` 01/2009/TT-BNV `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Nội vụ `[CO_QUAN_BAN_HANH]`)
- (`e1` 01/2009/TT-BNV `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 01/2009/TT-BNV `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Nội vụ `[LINH_VUC]`)
- (`e4` Điều 3 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 01/2009/TT-BNV `[SO_HIEU]`)
- (`e5` Khoản 2 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 3 `[DIEU]`)
- (`e6` b ) Sở Nội vụ ( đối với miễn nhiệm Chủ tịch , Phó Chủ tịch và Ủy viên Ủy ban nhân dân huyện , quận ) , Phòng Nội vụ ( đối với miễn nhiệm Chủ tịch , Phó Chủ tịch và Ủy viên Ủy ban nhân dân phường ) phối hợp với các cơ quan chức năng làm công tác tổ chức cán bộ , tiến hành : - Tổng hợp ý kiến các cơ quan có liên quan ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e5` Khoản 2 `[KHOAN]`)
- (`e1` 01/2009/TT-BNV `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Nội vụ `[LINH_VUC]`)
- (`e6` b ) Sở Nội vụ ( đối với miễn nhiệm Chủ tịch , Phó Chủ tịch và Ủy viên Ủy ban nhân dân huyện , quận ) , Phòng Nội vụ ( đối với miễn nhiệm Chủ tịch , Phó Chủ tịch và Ủy viên Ủy ban nhân dân phường ) phối hợp với các cơ quan chức năng làm công tác tổ chức cán bộ , tiến hành : - Tổng hợp ý kiến các cơ quan có liên quan ; `[DIEM]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Nội vụ `[LINH_VUC]`)


---

### Mẫu #01_2009_TT-BNV_12219#body_standalone_73 (Loại: `body_standalone`)
> **[Điều 3]`<DIEU>`** . **[Khoản 2]`<KHOAN>`** . **[b ) **[Sở Nội vụ]`<CO_QUAN_THAM_QUYEN>`** ( đối với miễn nhiệm Chủ tịch , Phó Chủ tịch và Ủy viên **[Ủy ban nhân dân huyện , quận]`<CO_QUAN_THAM_QUYEN>`** ) , **[Phòng Nội vụ]`<CO_QUAN_THAM_QUYEN>`** ( đối với miễn nhiệm Chủ tịch , Phó Chủ tịch và Ủy viên **[Ủy ban nhân dân phường]`<CO_QUAN_THAM_QUYEN>`** ) phối hợp với các cơ quan chức năng làm công tác tổ chức **[cán bộ]`<CHU_THE_CA_NHAN>`** , tiến hành : - Tổng hợp ý kiến các cơ quan có liên quan ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Điều 3** → `DIEU` (span: `[0:2]`)
- `[e1]` **Khoản 2** → `KHOAN` (span: `[3:5]`)
- `[e2]` **b ) Sở Nội vụ ( đối với miễn nhiệm Chủ tịch , Phó Chủ tịch và Ủy viên Ủy ban nhân dân huyện , quận ) , Phòng Nội vụ ( đối với miễn nhiệm Chủ tịch , Phó Chủ tịch và Ủy viên Ủy ban nhân dân phường ) phối hợp với các cơ quan chức năng làm công tác tổ chức cán bộ , tiến hành : - Tổng hợp ý kiến các cơ quan có liên quan ;** → `DIEM` (span: `[6:57]`)
- `[e3]` **Sở Nội vụ** → `CO_QUAN_THAM_QUYEN` (span: `[8:10]`) *(lồng trong `e2` (`DIEM`))*
- `[e4]` **Ủy ban nhân dân huyện , quận** → `CO_QUAN_THAM_QUYEN` (span: `[18:23]`) *(lồng trong `e2` (`DIEM`))*
- `[e5]` **Phòng Nội vụ** → `CO_QUAN_THAM_QUYEN` (span: `[25:27]`) *(lồng trong `e2` (`DIEM`))*
- `[e6]` **Ủy ban nhân dân phường** → `CO_QUAN_THAM_QUYEN` (span: `[35:38]`) *(lồng trong `e2` (`DIEM`))*
- `[e7]` **cán bộ** → `CHU_THE_CA_NHAN` (span: `[46:47]`) *(lồng trong `e2` (`DIEM`))*

**Quan hệ:**
- (`e1` Khoản 2 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 3 `[DIEU]`)
- (`e2` b ) Sở Nội vụ ( đối với miễn nhiệm Chủ tịch , Phó Chủ tịch và Ủy viên Ủy ban nhân dân huyện , quận ) , Phòng Nội vụ ( đối với miễn nhiệm Chủ tịch , Phó Chủ tịch và Ủy viên Ủy ban nhân dân phường ) phối hợp với các cơ quan chức năng làm công tác tổ chức cán bộ , tiến hành : - Tổng hợp ý kiến các cơ quan có liên quan ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e1` Khoản 2 `[KHOAN]`)


---

### Mẫu #01_2009_TT-BNV_12219#body_context_74 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[01/2009/TT-BNV]`<SO_HIEU>`** của **[Bộ Nội vụ]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Nội vụ]`<LINH_VUC>`** . **[Điều 3]`<DIEU>`** . **[Khoản 2]`<KHOAN>`** . **[b ) **[Sở Nội vụ]`<CO_QUAN_THAM_QUYEN>`** ( đối với miễn nhiệm Chủ tịch , Phó Chủ tịch và Ủy viên **[Ủy ban nhân dân huyện , quận]`<CO_QUAN_THAM_QUYEN>`** ) , **[Phòng Nội vụ]`<CO_QUAN_THAM_QUYEN>`** ( đối với miễn nhiệm Chủ tịch , Phó Chủ tịch và Ủy viên **[Ủy ban nhân dân phường]`<CO_QUAN_THAM_QUYEN>`** ) phối hợp với các cơ quan chức năng làm công tác tổ chức **[cán bộ]`<CHU_THE_CA_NHAN>`** , tiến hành : - Hoàn chỉnh **[hồ sơ trình]`<GIAY_TO_HO_SO>`** **[cấp có thẩm quyền quản lý cán bộ]`<CO_QUAN_THAM_QUYEN>`** .]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **01/2009/TT-BNV** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Nội vụ** → `CO_QUAN_BAN_HANH` (span: `[4:6]`)
- `[e3]` **Nội vụ** → `LINH_VUC` (span: `[8:9]`)
- `[e4]` **Điều 3** → `DIEU` (span: `[10:12]`)
- `[e5]` **Khoản 2** → `KHOAN` (span: `[13:15]`)
- `[e6]` **b ) Sở Nội vụ ( đối với miễn nhiệm Chủ tịch , Phó Chủ tịch và Ủy viên Ủy ban nhân dân huyện , quận ) , Phòng Nội vụ ( đối với miễn nhiệm Chủ tịch , Phó Chủ tịch và Ủy viên Ủy ban nhân dân phường ) phối hợp với các cơ quan chức năng làm công tác tổ chức cán bộ , tiến hành : - Hoàn chỉnh hồ sơ trình cấp có thẩm quyền quản lý cán bộ .** → `DIEM` (span: `[16:69]`)
- `[e7]` **Sở Nội vụ** → `CO_QUAN_THAM_QUYEN` (span: `[18:20]`) *(lồng trong `e6` (`DIEM`))*
- `[e8]` **Ủy ban nhân dân huyện , quận** → `CO_QUAN_THAM_QUYEN` (span: `[28:33]`) *(lồng trong `e6` (`DIEM`))*
- `[e9]` **Phòng Nội vụ** → `CO_QUAN_THAM_QUYEN` (span: `[35:37]`) *(lồng trong `e6` (`DIEM`))*
- `[e10]` **Ủy ban nhân dân phường** → `CO_QUAN_THAM_QUYEN` (span: `[45:48]`) *(lồng trong `e6` (`DIEM`))*
- `[e11]` **cấp có thẩm quyền quản lý cán bộ** → `CO_QUAN_THAM_QUYEN` (span: `[63:68]`) *(lồng trong `e6` (`DIEM`))*
- `[e12]` **hồ sơ trình** → `GIAY_TO_HO_SO` (span: `[62:63]`) *(lồng trong `e6` (`DIEM`))*
- `[e13]` **cán bộ** → `CHU_THE_CA_NHAN` (span: `[56:57]`) *(lồng trong `e6` (`DIEM`))*

**Quan hệ:**
- (`e1` 01/2009/TT-BNV `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Nội vụ `[CO_QUAN_BAN_HANH]`)
- (`e1` 01/2009/TT-BNV `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 01/2009/TT-BNV `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Nội vụ `[LINH_VUC]`)
- (`e4` Điều 3 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 01/2009/TT-BNV `[SO_HIEU]`)
- (`e5` Khoản 2 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 3 `[DIEU]`)
- (`e6` b ) Sở Nội vụ ( đối với miễn nhiệm Chủ tịch , Phó Chủ tịch và Ủy viên Ủy ban nhân dân huyện , quận ) , Phòng Nội vụ ( đối với miễn nhiệm Chủ tịch , Phó Chủ tịch và Ủy viên Ủy ban nhân dân phường ) phối hợp với các cơ quan chức năng làm công tác tổ chức cán bộ , tiến hành : - Hoàn chỉnh hồ sơ trình cấp có thẩm quyền quản lý cán bộ . `[DIEM]`) ==[ **THUOC_VE** ]==> (`e5` Khoản 2 `[KHOAN]`)
- (`e1` 01/2009/TT-BNV `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Nội vụ `[LINH_VUC]`)
- (`e6` b ) Sở Nội vụ ( đối với miễn nhiệm Chủ tịch , Phó Chủ tịch và Ủy viên Ủy ban nhân dân huyện , quận ) , Phòng Nội vụ ( đối với miễn nhiệm Chủ tịch , Phó Chủ tịch và Ủy viên Ủy ban nhân dân phường ) phối hợp với các cơ quan chức năng làm công tác tổ chức cán bộ , tiến hành : - Hoàn chỉnh hồ sơ trình cấp có thẩm quyền quản lý cán bộ . `[DIEM]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Nội vụ `[LINH_VUC]`)


---

### Mẫu #01_2009_TT-BNV_12219#body_standalone_75 (Loại: `body_standalone`)
> **[Điều 3]`<DIEU>`** . **[Khoản 2]`<KHOAN>`** . **[b ) **[Sở Nội vụ]`<CO_QUAN_THAM_QUYEN>`** ( đối với miễn nhiệm Chủ tịch , Phó Chủ tịch và Ủy viên **[Ủy ban nhân dân huyện , quận]`<CO_QUAN_THAM_QUYEN>`** ) , **[Phòng Nội vụ]`<CO_QUAN_THAM_QUYEN>`** ( đối với miễn nhiệm Chủ tịch , Phó Chủ tịch và Ủy viên **[Ủy ban nhân dân phường]`<CO_QUAN_THAM_QUYEN>`** ) phối hợp với các cơ quan chức năng làm công tác tổ chức **[cán bộ]`<CHU_THE_CA_NHAN>`** , tiến hành : - Hoàn chỉnh **[hồ sơ trình]`<GIAY_TO_HO_SO>`** **[cấp có thẩm quyền quản lý cán bộ]`<CO_QUAN_THAM_QUYEN>`** .]`<DIEM>`**

**Thực thể:**
- `[e0]` **Điều 3** → `DIEU` (span: `[0:2]`)
- `[e1]` **Khoản 2** → `KHOAN` (span: `[3:5]`)
- `[e2]` **b ) Sở Nội vụ ( đối với miễn nhiệm Chủ tịch , Phó Chủ tịch và Ủy viên Ủy ban nhân dân huyện , quận ) , Phòng Nội vụ ( đối với miễn nhiệm Chủ tịch , Phó Chủ tịch và Ủy viên Ủy ban nhân dân phường ) phối hợp với các cơ quan chức năng làm công tác tổ chức cán bộ , tiến hành : - Hoàn chỉnh hồ sơ trình cấp có thẩm quyền quản lý cán bộ .** → `DIEM` (span: `[6:59]`)
- `[e3]` **Sở Nội vụ** → `CO_QUAN_THAM_QUYEN` (span: `[8:10]`) *(lồng trong `e2` (`DIEM`))*
- `[e4]` **Ủy ban nhân dân huyện , quận** → `CO_QUAN_THAM_QUYEN` (span: `[18:23]`) *(lồng trong `e2` (`DIEM`))*
- `[e5]` **Phòng Nội vụ** → `CO_QUAN_THAM_QUYEN` (span: `[25:27]`) *(lồng trong `e2` (`DIEM`))*
- `[e6]` **Ủy ban nhân dân phường** → `CO_QUAN_THAM_QUYEN` (span: `[35:38]`) *(lồng trong `e2` (`DIEM`))*
- `[e7]` **cấp có thẩm quyền quản lý cán bộ** → `CO_QUAN_THAM_QUYEN` (span: `[53:58]`) *(lồng trong `e2` (`DIEM`))*
- `[e8]` **hồ sơ trình** → `GIAY_TO_HO_SO` (span: `[52:53]`) *(lồng trong `e2` (`DIEM`))*
- `[e9]` **cán bộ** → `CHU_THE_CA_NHAN` (span: `[46:47]`) *(lồng trong `e2` (`DIEM`))*

**Quan hệ:**
- (`e1` Khoản 2 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 3 `[DIEU]`)
- (`e2` b ) Sở Nội vụ ( đối với miễn nhiệm Chủ tịch , Phó Chủ tịch và Ủy viên Ủy ban nhân dân huyện , quận ) , Phòng Nội vụ ( đối với miễn nhiệm Chủ tịch , Phó Chủ tịch và Ủy viên Ủy ban nhân dân phường ) phối hợp với các cơ quan chức năng làm công tác tổ chức cán bộ , tiến hành : - Hoàn chỉnh hồ sơ trình cấp có thẩm quyền quản lý cán bộ . `[DIEM]`) ==[ **THUOC_VE** ]==> (`e1` Khoản 2 `[KHOAN]`)


---

### Mẫu #01_2009_TT-BNV_12219#body_context_76 (Loại: `body_context`)
> **[Bộ Nội vụ]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[01/2009/TT-BNV]`<SO_HIEU>`** . **[Điều 3]`<DIEU>`** . **[Khoản 2]`<KHOAN>`** . **[c ) **[Cấp có thẩm quyền quản lý cán bộ]`<CO_QUAN_THAM_QUYEN>`** xem xét , kết luận và có ý kiến đồng ý bằng văn bản .]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[3:4]`)
- `[e1]` **01/2009/TT-BNV** → `SO_HIEU` (span: `[5:6]`)
- `[e2]` **Bộ Nội vụ** → `CO_QUAN_BAN_HANH` (span: `[0:2]`)
- `[e3]` **Điều 3** → `DIEU` (span: `[7:9]`)
- `[e4]` **Khoản 2** → `KHOAN` (span: `[10:12]`)
- `[e5]` **c ) Cấp có thẩm quyền quản lý cán bộ xem xét , kết luận và có ý kiến đồng ý bằng văn bản .** → `DIEM` (span: `[13:30]`)
- `[e6]` **Cấp có thẩm quyền quản lý cán bộ** → `CO_QUAN_THAM_QUYEN` (span: `[15:20]`) *(lồng trong `e5` (`DIEM`))*

**Quan hệ:**
- (`e1` 01/2009/TT-BNV `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Nội vụ `[CO_QUAN_BAN_HANH]`)
- (`e1` 01/2009/TT-BNV `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 3 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 01/2009/TT-BNV `[SO_HIEU]`)
- (`e4` Khoản 2 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 3 `[DIEU]`)
- (`e5` c ) Cấp có thẩm quyền quản lý cán bộ xem xét , kết luận và có ý kiến đồng ý bằng văn bản . `[DIEM]`) ==[ **THUOC_VE** ]==> (`e4` Khoản 2 `[KHOAN]`)


---

### Mẫu #01_2009_TT-BNV_12219#body_standalone_77 (Loại: `body_standalone`)
> **[Điều 3]`<DIEU>`** . **[Khoản 2]`<KHOAN>`** . **[c ) **[Cấp có thẩm quyền quản lý cán bộ]`<CO_QUAN_THAM_QUYEN>`** xem xét , kết luận và có ý kiến đồng ý bằng văn bản .]`<DIEM>`**

**Thực thể:**
- `[e0]` **Điều 3** → `DIEU` (span: `[0:2]`)
- `[e1]` **Khoản 2** → `KHOAN` (span: `[3:5]`)
- `[e2]` **c ) Cấp có thẩm quyền quản lý cán bộ xem xét , kết luận và có ý kiến đồng ý bằng văn bản .** → `DIEM` (span: `[6:23]`)
- `[e3]` **Cấp có thẩm quyền quản lý cán bộ** → `CO_QUAN_THAM_QUYEN` (span: `[8:13]`) *(lồng trong `e2` (`DIEM`))*

**Quan hệ:**
- (`e1` Khoản 2 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 3 `[DIEU]`)
- (`e2` c ) Cấp có thẩm quyền quản lý cán bộ xem xét , kết luận và có ý kiến đồng ý bằng văn bản . `[DIEM]`) ==[ **THUOC_VE** ]==> (`e1` Khoản 2 `[KHOAN]`)


---

### Mẫu #01_2009_TT-BNV_12219#body_context_78 (Loại: `body_context`)
> **[Bộ Nội vụ]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[01/2009/TT-BNV]`<SO_HIEU>`** . **[Điều 3]`<DIEU>`** . **[Khoản 2]`<KHOAN>`** . **[d ) Căn cứ **[thông báo bằng văn bản]`<GIAY_TO_HO_SO>`** của **[cấp có thẩm quyền quản lý cán bộ]`<CO_QUAN_THAM_QUYEN>`** , **[Sở Nội vụ]`<CO_QUAN_THAM_QUYEN>`** hoàn chỉnh **[hồ sơ trình]`<GIAY_TO_HO_SO>`** **[Chủ tịch Ủy ban nhân dân tỉnh , thành phố trực thuộc trung ương]`<CO_QUAN_THAM_QUYEN>`** miễn nhiệm Chủ tịch , Phó Chủ tịch và Ủy viên **[Ủy ban nhân dân huyện , quận]`<CO_QUAN_THAM_QUYEN>`** ; **[Phòng Nội vụ]`<CO_QUAN_THAM_QUYEN>`** hoàn chỉnh **[hồ sơ trình]`<GIAY_TO_HO_SO>`** **[Chủ tịch Ủy ban nhân dân quận , thị xã , thành phố thuộc tỉnh]`<CO_QUAN_THAM_QUYEN>`** miễn nhiệm Chủ tịch , Phó Chủ tịch và Ủy viên Ủy ban nhân dân]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[3:4]`)
- `[e1]` **01/2009/TT-BNV** → `SO_HIEU` (span: `[5:6]`)
- `[e2]` **Bộ Nội vụ** → `CO_QUAN_BAN_HANH` (span: `[0:2]`)
- `[e3]` **Điều 3** → `DIEU` (span: `[7:9]`)
- `[e4]` **Khoản 2** → `KHOAN` (span: `[10:12]`)
- `[e5]` **d ) Căn cứ thông báo bằng văn bản của cấp có thẩm quyền quản lý cán bộ , Sở Nội vụ hoàn chỉnh hồ sơ trình Chủ tịch Ủy ban nhân dân tỉnh , thành phố trực thuộc trung ương miễn nhiệm Chủ tịch , Phó Chủ tịch và Ủy viên Ủy ban nhân dân huyện , quận ; Phòng Nội vụ hoàn chỉnh hồ sơ trình Chủ tịch Ủy ban nhân dân quận , thị xã , thành phố thuộc tỉnh miễn nhiệm Chủ tịch , Phó Chủ tịch và Ủy viên Ủy ban nhân dân** → `DIEM` (span: `[13:72]`)
- `[e6]` **cấp có thẩm quyền quản lý cán bộ** → `CO_QUAN_THAM_QUYEN` (span: `[20:25]`) *(lồng trong `e5` (`DIEM`))*
- `[e7]` **Sở Nội vụ** → `CO_QUAN_THAM_QUYEN` (span: `[26:28]`) *(lồng trong `e5` (`DIEM`))*
- `[e8]` **Chủ tịch Ủy ban nhân dân tỉnh , thành phố trực thuộc trung ương** → `CO_QUAN_THAM_QUYEN` (span: `[30:38]`) *(lồng trong `e5` (`DIEM`))*
- `[e9]` **Ủy ban nhân dân huyện , quận** → `CO_QUAN_THAM_QUYEN` (span: `[44:49]`) *(lồng trong `e5` (`DIEM`))*
- `[e10]` **Phòng Nội vụ** → `CO_QUAN_THAM_QUYEN` (span: `[50:52]`) *(lồng trong `e5` (`DIEM`))*
- `[e11]` **Chủ tịch Ủy ban nhân dân quận , thị xã , thành phố thuộc tỉnh** → `CO_QUAN_THAM_QUYEN` (span: `[54:64]`) *(lồng trong `e5` (`DIEM`))*
- `[e12]` **thông báo bằng văn bản** → `GIAY_TO_HO_SO` (span: `[16:19]`) *(lồng trong `e5` (`DIEM`))*
- `[e13]` **hồ sơ trình** → `GIAY_TO_HO_SO` (span: `[29:30]`) *(lồng trong `e5` (`DIEM`))*
- `[e14]` **hồ sơ trình** → `GIAY_TO_HO_SO` (span: `[53:54]`) *(lồng trong `e5` (`DIEM`))*

**Quan hệ:**
- (`e1` 01/2009/TT-BNV `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Nội vụ `[CO_QUAN_BAN_HANH]`)
- (`e1` 01/2009/TT-BNV `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 3 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 01/2009/TT-BNV `[SO_HIEU]`)
- (`e4` Khoản 2 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 3 `[DIEU]`)
- (`e5` d ) Căn cứ thông báo bằng văn bản của cấp có thẩm quyền quản lý cán bộ , Sở Nội vụ hoàn chỉnh hồ sơ trình Chủ tịch Ủy ban nhân dân tỉnh , thành phố trực thuộc trung ương miễn nhiệm Chủ tịch , Phó Chủ tịch và Ủy viên Ủy ban nhân dân huyện , quận ; Phòng Nội vụ hoàn chỉnh hồ sơ trình Chủ tịch Ủy ban nhân dân quận , thị xã , thành phố thuộc tỉnh miễn nhiệm Chủ tịch , Phó Chủ tịch và Ủy viên Ủy ban nhân dân `[DIEM]`) ==[ **THUOC_VE** ]==> (`e4` Khoản 2 `[KHOAN]`)


---

### Mẫu #01_2009_TT-BNV_12219#body_standalone_79 (Loại: `body_standalone`)
> **[Điều 3]`<DIEU>`** . **[Khoản 2]`<KHOAN>`** . **[d ) Căn cứ **[thông báo bằng văn bản]`<GIAY_TO_HO_SO>`** của **[cấp có thẩm quyền quản lý cán bộ]`<CO_QUAN_THAM_QUYEN>`** , **[Sở Nội vụ]`<CO_QUAN_THAM_QUYEN>`** hoàn chỉnh **[hồ sơ trình]`<GIAY_TO_HO_SO>`** **[Chủ tịch Ủy ban nhân dân tỉnh , thành phố trực thuộc trung ương]`<CO_QUAN_THAM_QUYEN>`** miễn nhiệm Chủ tịch , Phó Chủ tịch và Ủy viên **[Ủy ban nhân dân huyện , quận]`<CO_QUAN_THAM_QUYEN>`** ; **[Phòng Nội vụ]`<CO_QUAN_THAM_QUYEN>`** hoàn chỉnh **[hồ sơ trình]`<GIAY_TO_HO_SO>`** **[Chủ tịch Ủy ban nhân dân quận , thị xã , thành phố thuộc tỉnh]`<CO_QUAN_THAM_QUYEN>`** miễn nhiệm Chủ tịch , Phó Chủ tịch và Ủy viên Ủy ban nhân dân]`<DIEM>`**

**Thực thể:**
- `[e0]` **Điều 3** → `DIEU` (span: `[0:2]`)
- `[e1]` **Khoản 2** → `KHOAN` (span: `[3:5]`)
- `[e2]` **d ) Căn cứ thông báo bằng văn bản của cấp có thẩm quyền quản lý cán bộ , Sở Nội vụ hoàn chỉnh hồ sơ trình Chủ tịch Ủy ban nhân dân tỉnh , thành phố trực thuộc trung ương miễn nhiệm Chủ tịch , Phó Chủ tịch và Ủy viên Ủy ban nhân dân huyện , quận ; Phòng Nội vụ hoàn chỉnh hồ sơ trình Chủ tịch Ủy ban nhân dân quận , thị xã , thành phố thuộc tỉnh miễn nhiệm Chủ tịch , Phó Chủ tịch và Ủy viên Ủy ban nhân dân** → `DIEM` (span: `[6:65]`)
- `[e3]` **cấp có thẩm quyền quản lý cán bộ** → `CO_QUAN_THAM_QUYEN` (span: `[13:18]`) *(lồng trong `e2` (`DIEM`))*
- `[e4]` **Sở Nội vụ** → `CO_QUAN_THAM_QUYEN` (span: `[19:21]`) *(lồng trong `e2` (`DIEM`))*
- `[e5]` **Chủ tịch Ủy ban nhân dân tỉnh , thành phố trực thuộc trung ương** → `CO_QUAN_THAM_QUYEN` (span: `[23:31]`) *(lồng trong `e2` (`DIEM`))*
- `[e6]` **Ủy ban nhân dân huyện , quận** → `CO_QUAN_THAM_QUYEN` (span: `[37:42]`) *(lồng trong `e2` (`DIEM`))*
- `[e7]` **Phòng Nội vụ** → `CO_QUAN_THAM_QUYEN` (span: `[43:45]`) *(lồng trong `e2` (`DIEM`))*
- `[e8]` **Chủ tịch Ủy ban nhân dân quận , thị xã , thành phố thuộc tỉnh** → `CO_QUAN_THAM_QUYEN` (span: `[47:57]`) *(lồng trong `e2` (`DIEM`))*
- `[e9]` **thông báo bằng văn bản** → `GIAY_TO_HO_SO` (span: `[9:12]`) *(lồng trong `e2` (`DIEM`))*
- `[e10]` **hồ sơ trình** → `GIAY_TO_HO_SO` (span: `[22:23]`) *(lồng trong `e2` (`DIEM`))*
- `[e11]` **hồ sơ trình** → `GIAY_TO_HO_SO` (span: `[46:47]`) *(lồng trong `e2` (`DIEM`))*

**Quan hệ:**
- (`e1` Khoản 2 `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 3 `[DIEU]`)
- (`e2` d ) Căn cứ thông báo bằng văn bản của cấp có thẩm quyền quản lý cán bộ , Sở Nội vụ hoàn chỉnh hồ sơ trình Chủ tịch Ủy ban nhân dân tỉnh , thành phố trực thuộc trung ương miễn nhiệm Chủ tịch , Phó Chủ tịch và Ủy viên Ủy ban nhân dân huyện , quận ; Phòng Nội vụ hoàn chỉnh hồ sơ trình Chủ tịch Ủy ban nhân dân quận , thị xã , thành phố thuộc tỉnh miễn nhiệm Chủ tịch , Phó Chủ tịch và Ủy viên Ủy ban nhân dân `[DIEM]`) ==[ **THUOC_VE** ]==> (`e1` Khoản 2 `[KHOAN]`)


---

### Mẫu #01_2009_TT-BNV_12219#body_context_80 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[01/2009/TT-BNV]`<SO_HIEU>`** của **[Bộ Nội vụ]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Nội vụ]`<LINH_VUC>`** . **[Điều 3]`<DIEU>`** . **[3 . **[Hồ sơ miễn nhiệm]`<GIAY_TO_HO_SO>`** **[Hồ sơ trình miễn nhiệm cán bộ]`<GIAY_TO_HO_SO>`** , bao gồm :]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **01/2009/TT-BNV** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Nội vụ** → `CO_QUAN_BAN_HANH` (span: `[4:6]`)
- `[e3]` **Nội vụ** → `LINH_VUC` (span: `[8:9]`)
- `[e4]` **Điều 3** → `DIEU` (span: `[10:12]`)
- `[e5]` **3 . Hồ sơ miễn nhiệm Hồ sơ trình miễn nhiệm cán bộ , bao gồm :** → `KHOAN` (span: `[13:24]`)
- `[e6]` **Hồ sơ miễn nhiệm** → `GIAY_TO_HO_SO` (span: `[15:17]`) *(lồng trong `e5` (`KHOAN`))*
- `[e7]` **Hồ sơ trình miễn nhiệm cán bộ** → `GIAY_TO_HO_SO` (span: `[17:21]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 01/2009/TT-BNV `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Nội vụ `[CO_QUAN_BAN_HANH]`)
- (`e1` 01/2009/TT-BNV `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 01/2009/TT-BNV `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Nội vụ `[LINH_VUC]`)
- (`e4` Điều 3 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 01/2009/TT-BNV `[SO_HIEU]`)
- (`e5` 3 . Hồ sơ miễn nhiệm Hồ sơ trình miễn nhiệm cán bộ , bao gồm : `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 3 `[DIEU]`)
- (`e1` 01/2009/TT-BNV `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Nội vụ `[LINH_VUC]`)
- (`e5` 3 . Hồ sơ miễn nhiệm Hồ sơ trình miễn nhiệm cán bộ , bao gồm : `[KHOAN]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Nội vụ `[LINH_VUC]`)


---

### Mẫu #01_2009_TT-BNV_12219#body_standalone_81 (Loại: `body_standalone`)
> **[Điều 3]`<DIEU>`** . **[3 . **[Hồ sơ miễn nhiệm]`<GIAY_TO_HO_SO>`** **[Hồ sơ trình miễn nhiệm cán bộ]`<GIAY_TO_HO_SO>`** , bao gồm :]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 3** → `DIEU` (span: `[0:2]`)
- `[e1]` **3 . Hồ sơ miễn nhiệm Hồ sơ trình miễn nhiệm cán bộ , bao gồm :** → `KHOAN` (span: `[3:14]`)
- `[e2]` **Hồ sơ miễn nhiệm** → `GIAY_TO_HO_SO` (span: `[5:7]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **Hồ sơ trình miễn nhiệm cán bộ** → `GIAY_TO_HO_SO` (span: `[7:11]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 3 . Hồ sơ miễn nhiệm Hồ sơ trình miễn nhiệm cán bộ , bao gồm : `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 3 `[DIEU]`)


---

### Mẫu #01_2009_TT-BNV_12219#body_context_82 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[01/2009/TT-BNV]`<SO_HIEU>`** của **[Bộ Nội vụ]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Nội vụ]`<LINH_VUC>`** . **[Điều 3]`<DIEU>`** . **[Khoản 3 . **[Hồ sơ trình miễn nhiệm cán bộ]`<GIAY_TO_HO_SO>`** , bao gồm]`<KHOAN>`** : **[a ) Tờ trình của Ủy ban nhân dân cấp có **[cán bộ]`<CHU_THE_CA_NHAN>`** miễn nhiệm ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **01/2009/TT-BNV** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Nội vụ** → `CO_QUAN_BAN_HANH` (span: `[4:6]`)
- `[e3]` **Nội vụ** → `LINH_VUC` (span: `[8:9]`)
- `[e4]` **Điều 3** → `DIEU` (span: `[10:12]`)
- `[e5]` **Khoản 3 . Hồ sơ trình miễn nhiệm cán bộ , bao gồm** → `KHOAN` (span: `[13:22]`)
- `[e6]` **a ) Tờ trình của Ủy ban nhân dân cấp có cán bộ miễn nhiệm ;** → `DIEM` (span: `[23:34]`)
- `[e7]` **cán bộ** → `CHU_THE_CA_NHAN` (span: `[31:32]`) *(lồng trong `e6` (`DIEM`))*
- `[e8]` **Hồ sơ trình miễn nhiệm cán bộ** → `GIAY_TO_HO_SO` (span: `[16:20]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 01/2009/TT-BNV `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Nội vụ `[CO_QUAN_BAN_HANH]`)
- (`e1` 01/2009/TT-BNV `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 01/2009/TT-BNV `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Nội vụ `[LINH_VUC]`)
- (`e4` Điều 3 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 01/2009/TT-BNV `[SO_HIEU]`)
- (`e5` Khoản 3 . Hồ sơ trình miễn nhiệm cán bộ , bao gồm `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 3 `[DIEU]`)
- (`e6` a ) Tờ trình của Ủy ban nhân dân cấp có cán bộ miễn nhiệm ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e5` Khoản 3 . Hồ sơ trình miễn nhiệm cán bộ , bao gồm `[KHOAN]`)
- (`e1` 01/2009/TT-BNV `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Nội vụ `[LINH_VUC]`)
- (`e6` a ) Tờ trình của Ủy ban nhân dân cấp có cán bộ miễn nhiệm ; `[DIEM]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Nội vụ `[LINH_VUC]`)


---

### Mẫu #01_2009_TT-BNV_12219#body_standalone_83 (Loại: `body_standalone`)
> **[Điều 3]`<DIEU>`** . **[Khoản 3 . **[Hồ sơ trình miễn nhiệm cán bộ]`<GIAY_TO_HO_SO>`** , bao gồm]`<KHOAN>`** : **[a ) Tờ trình của Ủy ban nhân dân cấp có **[cán bộ]`<CHU_THE_CA_NHAN>`** miễn nhiệm ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Điều 3** → `DIEU` (span: `[0:2]`)
- `[e1]` **Khoản 3 . Hồ sơ trình miễn nhiệm cán bộ , bao gồm** → `KHOAN` (span: `[3:12]`)
- `[e2]` **a ) Tờ trình của Ủy ban nhân dân cấp có cán bộ miễn nhiệm ;** → `DIEM` (span: `[13:24]`)
- `[e3]` **cán bộ** → `CHU_THE_CA_NHAN` (span: `[21:22]`) *(lồng trong `e2` (`DIEM`))*
- `[e4]` **Hồ sơ trình miễn nhiệm cán bộ** → `GIAY_TO_HO_SO` (span: `[6:10]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` Khoản 3 . Hồ sơ trình miễn nhiệm cán bộ , bao gồm `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 3 `[DIEU]`)
- (`e2` a ) Tờ trình của Ủy ban nhân dân cấp có cán bộ miễn nhiệm ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e1` Khoản 3 . Hồ sơ trình miễn nhiệm cán bộ , bao gồm `[KHOAN]`)


---

### Mẫu #01_2009_TT-BNV_12219#body_context_84 (Loại: `body_context`)
> **[Bộ Nội vụ]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[01/2009/TT-BNV]`<SO_HIEU>`** . **[Điều 3]`<DIEU>`** . **[Khoản 3 . **[Hồ sơ trình miễn nhiệm cán bộ]`<GIAY_TO_HO_SO>`** , bao gồm]`<KHOAN>`** : **[b ) Đơn xin miễn nhiệm của **[cán bộ]`<CHU_THE_CA_NHAN>`** trong trường hợp miễn nhiệm vì lý do cá nhân ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[3:4]`)
- `[e1]` **01/2009/TT-BNV** → `SO_HIEU` (span: `[5:6]`)
- `[e2]` **Bộ Nội vụ** → `CO_QUAN_BAN_HANH` (span: `[0:2]`)
- `[e3]` **Điều 3** → `DIEU` (span: `[7:9]`)
- `[e4]` **Khoản 3 . Hồ sơ trình miễn nhiệm cán bộ , bao gồm** → `KHOAN` (span: `[10:19]`)
- `[e5]` **b ) Đơn xin miễn nhiệm của cán bộ trong trường hợp miễn nhiệm vì lý do cá nhân ;** → `DIEM` (span: `[20:34]`)
- `[e6]` **cán bộ** → `CHU_THE_CA_NHAN` (span: `[26:27]`) *(lồng trong `e5` (`DIEM`))*
- `[e7]` **Hồ sơ trình miễn nhiệm cán bộ** → `GIAY_TO_HO_SO` (span: `[13:17]`) *(lồng trong `e4` (`KHOAN`))*

**Quan hệ:**
- (`e1` 01/2009/TT-BNV `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Nội vụ `[CO_QUAN_BAN_HANH]`)
- (`e1` 01/2009/TT-BNV `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 3 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 01/2009/TT-BNV `[SO_HIEU]`)
- (`e4` Khoản 3 . Hồ sơ trình miễn nhiệm cán bộ , bao gồm `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 3 `[DIEU]`)
- (`e5` b ) Đơn xin miễn nhiệm của cán bộ trong trường hợp miễn nhiệm vì lý do cá nhân ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e4` Khoản 3 . Hồ sơ trình miễn nhiệm cán bộ , bao gồm `[KHOAN]`)


---

### Mẫu #01_2009_TT-BNV_12219#body_standalone_85 (Loại: `body_standalone`)
> **[Điều 3]`<DIEU>`** . **[Khoản 3 . **[Hồ sơ trình miễn nhiệm cán bộ]`<GIAY_TO_HO_SO>`** , bao gồm]`<KHOAN>`** : **[b ) Đơn xin miễn nhiệm của **[cán bộ]`<CHU_THE_CA_NHAN>`** trong trường hợp miễn nhiệm vì lý do cá nhân ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Điều 3** → `DIEU` (span: `[0:2]`)
- `[e1]` **Khoản 3 . Hồ sơ trình miễn nhiệm cán bộ , bao gồm** → `KHOAN` (span: `[3:12]`)
- `[e2]` **b ) Đơn xin miễn nhiệm của cán bộ trong trường hợp miễn nhiệm vì lý do cá nhân ;** → `DIEM` (span: `[13:27]`)
- `[e3]` **cán bộ** → `CHU_THE_CA_NHAN` (span: `[19:20]`) *(lồng trong `e2` (`DIEM`))*
- `[e4]` **Hồ sơ trình miễn nhiệm cán bộ** → `GIAY_TO_HO_SO` (span: `[6:10]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` Khoản 3 . Hồ sơ trình miễn nhiệm cán bộ , bao gồm `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 3 `[DIEU]`)
- (`e2` b ) Đơn xin miễn nhiệm của cán bộ trong trường hợp miễn nhiệm vì lý do cá nhân ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e1` Khoản 3 . Hồ sơ trình miễn nhiệm cán bộ , bao gồm `[KHOAN]`)


---

### Mẫu #01_2009_TT-BNV_12219#body_context_86 (Loại: `body_context`)
> **[Bộ Nội vụ]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[01/2009/TT-BNV]`<SO_HIEU>`** . **[Điều 3]`<DIEU>`** . **[Khoản 3 . **[Hồ sơ trình miễn nhiệm cán bộ]`<GIAY_TO_HO_SO>`** , bao gồm]`<KHOAN>`** : **[c ) **[Thông báo kết luận bằng văn bản]`<GIAY_TO_HO_SO>`** của **[cấp có thẩm quyền]`<CO_QUAN_THAM_QUYEN>`** .]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[3:4]`)
- `[e1]` **01/2009/TT-BNV** → `SO_HIEU` (span: `[5:6]`)
- `[e2]` **Bộ Nội vụ** → `CO_QUAN_BAN_HANH` (span: `[0:2]`)
- `[e3]` **Điều 3** → `DIEU` (span: `[7:9]`)
- `[e4]` **Khoản 3 . Hồ sơ trình miễn nhiệm cán bộ , bao gồm** → `KHOAN` (span: `[10:19]`)
- `[e5]` **c ) Thông báo kết luận bằng văn bản của cấp có thẩm quyền .** → `DIEM` (span: `[20:31]`)
- `[e6]` **cấp có thẩm quyền** → `CO_QUAN_THAM_QUYEN` (span: `[27:30]`) *(lồng trong `e5` (`DIEM`))*
- `[e7]` **Thông báo kết luận bằng văn bản** → `GIAY_TO_HO_SO` (span: `[22:26]`) *(lồng trong `e5` (`DIEM`))*
- `[e8]` **Hồ sơ trình miễn nhiệm cán bộ** → `GIAY_TO_HO_SO` (span: `[13:17]`) *(lồng trong `e4` (`KHOAN`))*

**Quan hệ:**
- (`e1` 01/2009/TT-BNV `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Nội vụ `[CO_QUAN_BAN_HANH]`)
- (`e1` 01/2009/TT-BNV `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 3 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 01/2009/TT-BNV `[SO_HIEU]`)
- (`e4` Khoản 3 . Hồ sơ trình miễn nhiệm cán bộ , bao gồm `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 3 `[DIEU]`)
- (`e5` c ) Thông báo kết luận bằng văn bản của cấp có thẩm quyền . `[DIEM]`) ==[ **THUOC_VE** ]==> (`e4` Khoản 3 . Hồ sơ trình miễn nhiệm cán bộ , bao gồm `[KHOAN]`)


---

### Mẫu #01_2009_TT-BNV_12219#body_standalone_87 (Loại: `body_standalone`)
> **[Điều 3]`<DIEU>`** . **[Khoản 3 . **[Hồ sơ trình miễn nhiệm cán bộ]`<GIAY_TO_HO_SO>`** , bao gồm]`<KHOAN>`** : **[c ) **[Thông báo kết luận bằng văn bản]`<GIAY_TO_HO_SO>`** của **[cấp có thẩm quyền]`<CO_QUAN_THAM_QUYEN>`** .]`<DIEM>`**

**Thực thể:**
- `[e0]` **Điều 3** → `DIEU` (span: `[0:2]`)
- `[e1]` **Khoản 3 . Hồ sơ trình miễn nhiệm cán bộ , bao gồm** → `KHOAN` (span: `[3:12]`)
- `[e2]` **c ) Thông báo kết luận bằng văn bản của cấp có thẩm quyền .** → `DIEM` (span: `[13:24]`)
- `[e3]` **cấp có thẩm quyền** → `CO_QUAN_THAM_QUYEN` (span: `[20:23]`) *(lồng trong `e2` (`DIEM`))*
- `[e4]` **Thông báo kết luận bằng văn bản** → `GIAY_TO_HO_SO` (span: `[15:19]`) *(lồng trong `e2` (`DIEM`))*
- `[e5]` **Hồ sơ trình miễn nhiệm cán bộ** → `GIAY_TO_HO_SO` (span: `[6:10]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` Khoản 3 . Hồ sơ trình miễn nhiệm cán bộ , bao gồm `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 3 `[DIEU]`)
- (`e2` c ) Thông báo kết luận bằng văn bản của cấp có thẩm quyền . `[DIEM]`) ==[ **THUOC_VE** ]==> (`e1` Khoản 3 . Hồ sơ trình miễn nhiệm cán bộ , bao gồm `[KHOAN]`)


---

### Mẫu #01_2009_TT-BNV_12219#body_context_88 (Loại: `body_context`)
> **[Bộ Nội vụ]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[01/2009/TT-BNV]`<SO_HIEU>`** . **[Điều 4 . Trình tự , thủ tục cách chức]`<DIEU>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[3:4]`)
- `[e1]` **01/2009/TT-BNV** → `SO_HIEU` (span: `[5:6]`)
- `[e2]` **Bộ Nội vụ** → `CO_QUAN_BAN_HANH` (span: `[0:2]`)
- `[e3]` **Điều 4 . Trình tự , thủ tục cách chức** → `DIEU` (span: `[7:14]`)

**Quan hệ:**
- (`e1` 01/2009/TT-BNV `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Nội vụ `[CO_QUAN_BAN_HANH]`)
- (`e1` 01/2009/TT-BNV `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 4 . Trình tự , thủ tục cách chức `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 01/2009/TT-BNV `[SO_HIEU]`)


---

### Mẫu #01_2009_TT-BNV_12219#body_context_89 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[01/2009/TT-BNV]`<SO_HIEU>`** ban hành **[ngày 19 tháng 03 năm 2009]`<NGAY_BAN_HANH>`** bởi **[Bộ Nội vụ]`<CO_QUAN_BAN_HANH>`** . **[Điều 4]`<DIEU>`** . **[1 . Chủ tịch , Phó Chủ tịch và Ủy viên **[Ủy ban nhân dân huyện , quận , phường]`<CO_QUAN_THAM_QUYEN>`** **[nơi thực hiện thí điểm]`<DIA_DIEM>`** có hành vi vi phạm kỷ luật , vi phạm pháp luật nghiêm trọng không thể đảm nhiệm chức vụ được giao thì phải áp dụng hình thức kỷ luật cách chức .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **01/2009/TT-BNV** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Nội vụ** → `CO_QUAN_BAN_HANH` (span: `[11:13]`)
- `[e3]` **ngày 19 tháng 03 năm 2009** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 4** → `DIEU` (span: `[14:16]`)
- `[e5]` **1 . Chủ tịch , Phó Chủ tịch và Ủy viên Ủy ban nhân dân huyện , quận , phường nơi thực hiện thí điểm có hành vi vi phạm kỷ luật , vi phạm pháp luật nghiêm trọng không thể đảm nhiệm chức vụ được giao thì phải áp dụng hình thức kỷ luật cách chức .** → `KHOAN` (span: `[17:53]`)
- `[e6]` **Ủy ban nhân dân huyện , quận , phường** → `CO_QUAN_THAM_QUYEN` (span: `[24:31]`) *(lồng trong `e5` (`KHOAN`))*
- `[e7]` **nơi thực hiện thí điểm** → `DIA_DIEM` (span: `[31:34]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 01/2009/TT-BNV `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Nội vụ `[CO_QUAN_BAN_HANH]`)
- (`e1` 01/2009/TT-BNV `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 01/2009/TT-BNV `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 19 tháng 03 năm 2009 `[NGAY_BAN_HANH]`)
- (`e4` Điều 4 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 01/2009/TT-BNV `[SO_HIEU]`)
- (`e5` 1 . Chủ tịch , Phó Chủ tịch và Ủy viên Ủy ban nhân dân huyện , quận , phường nơi thực hiện thí điểm có hành vi vi phạm kỷ luật , vi phạm pháp luật nghiêm trọng không thể đảm nhiệm chức vụ được giao thì phải áp dụng hình thức kỷ luật cách chức . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 4 `[DIEU]`)


---

### Mẫu #01_2009_TT-BNV_12219#body_standalone_90 (Loại: `body_standalone`)
> **[Điều 4]`<DIEU>`** . **[1 . Chủ tịch , Phó Chủ tịch và Ủy viên **[Ủy ban nhân dân huyện , quận , phường]`<CO_QUAN_THAM_QUYEN>`** **[nơi thực hiện thí điểm]`<DIA_DIEM>`** có hành vi vi phạm kỷ luật , vi phạm pháp luật nghiêm trọng không thể đảm nhiệm chức vụ được giao thì phải áp dụng hình thức kỷ luật cách chức .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 4** → `DIEU` (span: `[0:2]`)
- `[e1]` **1 . Chủ tịch , Phó Chủ tịch và Ủy viên Ủy ban nhân dân huyện , quận , phường nơi thực hiện thí điểm có hành vi vi phạm kỷ luật , vi phạm pháp luật nghiêm trọng không thể đảm nhiệm chức vụ được giao thì phải áp dụng hình thức kỷ luật cách chức .** → `KHOAN` (span: `[3:39]`)
- `[e2]` **Ủy ban nhân dân huyện , quận , phường** → `CO_QUAN_THAM_QUYEN` (span: `[10:17]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **nơi thực hiện thí điểm** → `DIA_DIEM` (span: `[17:20]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 1 . Chủ tịch , Phó Chủ tịch và Ủy viên Ủy ban nhân dân huyện , quận , phường nơi thực hiện thí điểm có hành vi vi phạm kỷ luật , vi phạm pháp luật nghiêm trọng không thể đảm nhiệm chức vụ được giao thì phải áp dụng hình thức kỷ luật cách chức . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 4 `[DIEU]`)


---

### Mẫu #01_2009_TT-BNV_12219#body_context_91 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[01/2009/TT-BNV]`<SO_HIEU>`** ban hành **[ngày 19 tháng 03 năm 2009]`<NGAY_BAN_HANH>`** bởi **[Bộ Nội vụ]`<CO_QUAN_BAN_HANH>`** . **[Điều 4]`<DIEU>`** . **[2 . Quy trình , thủ tục cách chức Chủ tịch , Phó Chủ tịch và Ủy viên **[Ủy ban nhân dân huyện , quận , phường]`<CO_QUAN_THAM_QUYEN>`** **[nơi thực hiện thí điểm]`<DIA_DIEM>`** thực hiện **[theo quy định tại]`<TU_KHOA_PHAP_LY>`** **[Nghị định số 35/2005/NĐ-CP]`<THAM_CHIEU_PHAP_LY>`** **[ngày 17 tháng 3 năm 2005]`<NGAY_THAM_CHIEU>`** của **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** về việc xử lý kỷ luật **[cán bộ , công chức]`<CHU_THE_CA_NHAN>`** .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **01/2009/TT-BNV** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Nội vụ** → `CO_QUAN_BAN_HANH` (span: `[11:13]`)
- `[e3]` **ngày 19 tháng 03 năm 2009** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 4** → `DIEU` (span: `[14:16]`)
- `[e5]` **2 . Quy trình , thủ tục cách chức Chủ tịch , Phó Chủ tịch và Ủy viên Ủy ban nhân dân huyện , quận , phường nơi thực hiện thí điểm thực hiện theo quy định tại Nghị định số 35/2005/NĐ-CP ngày 17 tháng 3 năm 2005 của Chính phủ về việc xử lý kỷ luật cán bộ , công chức .** → `KHOAN` (span: `[17:61]`)
- `[e6]` **Nghị định số 35/2005/NĐ-CP** → `THAM_CHIEU_PHAP_LY` (span: `[42:45]`) *(lồng trong `e5` (`KHOAN`))*
- `[e7]` **theo quy định tại** → `TU_KHOA_PHAP_LY` (span: `[39:42]`) *(lồng trong `e5` (`KHOAN`))*
- `[e8]` **ngày 17 tháng 3 năm 2005** → `NGAY_THAM_CHIEU` (span: `[45:51]`) *(lồng trong `e5` (`KHOAN`))*
- `[e9]` **Ủy ban nhân dân huyện , quận , phường** → `CO_QUAN_THAM_QUYEN` (span: `[28:35]`) *(lồng trong `e5` (`KHOAN`))*
- `[e10]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[52:53]`) *(lồng trong `e5` (`KHOAN`))*
- `[e11]` **cán bộ , công chức** → `CHU_THE_CA_NHAN` (span: `[57:60]`) *(lồng trong `e5` (`KHOAN`))*
- `[e12]` **nơi thực hiện thí điểm** → `DIA_DIEM` (span: `[35:38]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 01/2009/TT-BNV `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Nội vụ `[CO_QUAN_BAN_HANH]`)
- (`e1` 01/2009/TT-BNV `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 01/2009/TT-BNV `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 19 tháng 03 năm 2009 `[NGAY_BAN_HANH]`)
- (`e4` Điều 4 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 01/2009/TT-BNV `[SO_HIEU]`)
- (`e5` 2 . Quy trình , thủ tục cách chức Chủ tịch , Phó Chủ tịch và Ủy viên Ủy ban nhân dân huyện , quận , phường nơi thực hiện thí điểm thực hiện theo quy định tại Nghị định số 35/2005/NĐ-CP ngày 17 tháng 3 năm 2005 của Chính phủ về việc xử lý kỷ luật cán bộ , công chức . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 4 `[DIEU]`)
- (`e7` theo quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e6` Nghị định số 35/2005/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e5` 2 . Quy trình , thủ tục cách chức Chủ tịch , Phó Chủ tịch và Ủy viên Ủy ban nhân dân huyện , quận , phường nơi thực hiện thí điểm thực hiện theo quy định tại Nghị định số 35/2005/NĐ-CP ngày 17 tháng 3 năm 2005 của Chính phủ về việc xử lý kỷ luật cán bộ , công chức . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e6` Nghị định số 35/2005/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e6` Nghị định số 35/2005/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e8` ngày 17 tháng 3 năm 2005 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #01_2009_TT-BNV_12219#body_standalone_92 (Loại: `body_standalone`)
> **[Điều 4]`<DIEU>`** . **[2 . Quy trình , thủ tục cách chức Chủ tịch , Phó Chủ tịch và Ủy viên **[Ủy ban nhân dân huyện , quận , phường]`<CO_QUAN_THAM_QUYEN>`** **[nơi thực hiện thí điểm]`<DIA_DIEM>`** thực hiện **[theo quy định tại]`<TU_KHOA_PHAP_LY>`** **[Nghị định số 35/2005/NĐ-CP]`<THAM_CHIEU_PHAP_LY>`** **[ngày 17 tháng 3 năm 2005]`<NGAY_THAM_CHIEU>`** của **[Chính phủ]`<CO_QUAN_THAM_QUYEN>`** về việc xử lý kỷ luật **[cán bộ , công chức]`<CHU_THE_CA_NHAN>`** .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 4** → `DIEU` (span: `[0:2]`)
- `[e1]` **2 . Quy trình , thủ tục cách chức Chủ tịch , Phó Chủ tịch và Ủy viên Ủy ban nhân dân huyện , quận , phường nơi thực hiện thí điểm thực hiện theo quy định tại Nghị định số 35/2005/NĐ-CP ngày 17 tháng 3 năm 2005 của Chính phủ về việc xử lý kỷ luật cán bộ , công chức .** → `KHOAN` (span: `[3:47]`)
- `[e2]` **Nghị định số 35/2005/NĐ-CP** → `THAM_CHIEU_PHAP_LY` (span: `[28:31]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **theo quy định tại** → `TU_KHOA_PHAP_LY` (span: `[25:28]`) *(lồng trong `e1` (`KHOAN`))*
- `[e4]` **ngày 17 tháng 3 năm 2005** → `NGAY_THAM_CHIEU` (span: `[31:37]`) *(lồng trong `e1` (`KHOAN`))*
- `[e5]` **Ủy ban nhân dân huyện , quận , phường** → `CO_QUAN_THAM_QUYEN` (span: `[14:21]`) *(lồng trong `e1` (`KHOAN`))*
- `[e6]` **Chính phủ** → `CO_QUAN_THAM_QUYEN` (span: `[38:39]`) *(lồng trong `e1` (`KHOAN`))*
- `[e7]` **cán bộ , công chức** → `CHU_THE_CA_NHAN` (span: `[43:46]`) *(lồng trong `e1` (`KHOAN`))*
- `[e8]` **nơi thực hiện thí điểm** → `DIA_DIEM` (span: `[21:24]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 2 . Quy trình , thủ tục cách chức Chủ tịch , Phó Chủ tịch và Ủy viên Ủy ban nhân dân huyện , quận , phường nơi thực hiện thí điểm thực hiện theo quy định tại Nghị định số 35/2005/NĐ-CP ngày 17 tháng 3 năm 2005 của Chính phủ về việc xử lý kỷ luật cán bộ , công chức . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 4 `[DIEU]`)
- (`e3` theo quy định tại `[TU_KHOA_PHAP_LY]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e2` Nghị định số 35/2005/NĐ-CP `[THAM_CHIEU_PHAP_LY]`)
- (`e1` 2 . Quy trình , thủ tục cách chức Chủ tịch , Phó Chủ tịch và Ủy viên Ủy ban nhân dân huyện , quận , phường nơi thực hiện thí điểm thực hiện theo quy định tại Nghị định số 35/2005/NĐ-CP ngày 17 tháng 3 năm 2005 của Chính phủ về việc xử lý kỷ luật cán bộ , công chức . `[KHOAN]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e2` Nghị định số 35/2005/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*
- (`e2` Nghị định số 35/2005/NĐ-CP `[THAM_CHIEU_PHAP_LY]`) ==[ **NGAY_BAN_HANH_THAM_CHIEU** ]==> (`e4` ngày 17 tháng 3 năm 2005 `[NGAY_THAM_CHIEU]`)


---

### Mẫu #01_2009_TT-BNV_12219#body_context_93 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[01/2009/TT-BNV]`<SO_HIEU>`** của **[Bộ Nội vụ]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Nội vụ]`<LINH_VUC>`** . **[Điều 5 . Hiệu lực thi hành]`<DIEU>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **01/2009/TT-BNV** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Nội vụ** → `CO_QUAN_BAN_HANH` (span: `[4:6]`)
- `[e3]` **Nội vụ** → `LINH_VUC` (span: `[8:9]`)
- `[e4]` **Điều 5 . Hiệu lực thi hành** → `DIEU` (span: `[10:15]`)

**Quan hệ:**
- (`e1` 01/2009/TT-BNV `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Nội vụ `[CO_QUAN_BAN_HANH]`)
- (`e1` 01/2009/TT-BNV `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 01/2009/TT-BNV `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Nội vụ `[LINH_VUC]`)
- (`e4` Điều 5 . Hiệu lực thi hành `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 01/2009/TT-BNV `[SO_HIEU]`)
- (`e1` 01/2009/TT-BNV `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Nội vụ `[LINH_VUC]`)
- (`e4` Điều 5 . Hiệu lực thi hành `[DIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Nội vụ `[LINH_VUC]`)


---

### Mẫu #01_2009_TT-BNV_12219#body_context_94 (Loại: `body_context`)
> **[Bộ Nội vụ]`<CO_QUAN_BAN_HANH>`** ban hành **[Thông tư]`<LOAI_VAN_BAN>`** số **[01/2009/TT-BNV]`<SO_HIEU>`** . **[Điều 5]`<DIEU>`** . **[1 . Thông tư này có hiệu lực thi hành kể từ ngày 01 tháng 4 năm 2009 .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[3:4]`)
- `[e1]` **01/2009/TT-BNV** → `SO_HIEU` (span: `[5:6]`)
- `[e2]` **Bộ Nội vụ** → `CO_QUAN_BAN_HANH` (span: `[0:2]`)
- `[e3]` **Điều 5** → `DIEU` (span: `[7:9]`)
- `[e4]` **1 . Thông tư này có hiệu lực thi hành kể từ ngày 01 tháng 4 năm 2009 .** → `KHOAN` (span: `[10:26]`)

**Quan hệ:**
- (`e1` 01/2009/TT-BNV `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Nội vụ `[CO_QUAN_BAN_HANH]`)
- (`e1` 01/2009/TT-BNV `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e3` Điều 5 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 01/2009/TT-BNV `[SO_HIEU]`)
- (`e4` 1 . Thông tư này có hiệu lực thi hành kể từ ngày 01 tháng 4 năm 2009 . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e3` Điều 5 `[DIEU]`)


---

### Mẫu #01_2009_TT-BNV_12219#body_context_95 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[01/2009/TT-BNV]`<SO_HIEU>`** của **[Bộ Nội vụ]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Nội vụ]`<LINH_VUC>`** . **[Điều 5]`<DIEU>`** . **[2 . **[Chủ tịch Ủy ban nhân dân tỉnh , thành phố trực thuộc trung ương]`<CO_QUAN_THAM_QUYEN>`** **[nơi thực hiện thí điểm]`<DIA_DIEM>`** chịu trách nhiệm tổ chức thực hiện Thông tư này .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **01/2009/TT-BNV** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Nội vụ** → `CO_QUAN_BAN_HANH` (span: `[4:6]`)
- `[e3]` **Nội vụ** → `LINH_VUC` (span: `[8:9]`)
- `[e4]` **Điều 5** → `DIEU` (span: `[10:12]`)
- `[e5]` **2 . Chủ tịch Ủy ban nhân dân tỉnh , thành phố trực thuộc trung ương nơi thực hiện thí điểm chịu trách nhiệm tổ chức thực hiện Thông tư này .** → `KHOAN` (span: `[13:33]`)
- `[e6]` **Chủ tịch Ủy ban nhân dân tỉnh , thành phố trực thuộc trung ương** → `CO_QUAN_THAM_QUYEN` (span: `[15:23]`) *(lồng trong `e5` (`KHOAN`))*
- `[e7]` **nơi thực hiện thí điểm** → `DIA_DIEM` (span: `[23:26]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 01/2009/TT-BNV `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Nội vụ `[CO_QUAN_BAN_HANH]`)
- (`e1` 01/2009/TT-BNV `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 01/2009/TT-BNV `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Nội vụ `[LINH_VUC]`)
- (`e4` Điều 5 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 01/2009/TT-BNV `[SO_HIEU]`)
- (`e5` 2 . Chủ tịch Ủy ban nhân dân tỉnh , thành phố trực thuộc trung ương nơi thực hiện thí điểm chịu trách nhiệm tổ chức thực hiện Thông tư này . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 5 `[DIEU]`)
- (`e1` 01/2009/TT-BNV `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Nội vụ `[LINH_VUC]`)
- (`e5` 2 . Chủ tịch Ủy ban nhân dân tỉnh , thành phố trực thuộc trung ương nơi thực hiện thí điểm chịu trách nhiệm tổ chức thực hiện Thông tư này . `[KHOAN]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Nội vụ `[LINH_VUC]`)


---

### Mẫu #01_2009_TT-BNV_12219#body_standalone_96 (Loại: `body_standalone`)
> **[Điều 5]`<DIEU>`** . **[2 . **[Chủ tịch Ủy ban nhân dân tỉnh , thành phố trực thuộc trung ương]`<CO_QUAN_THAM_QUYEN>`** **[nơi thực hiện thí điểm]`<DIA_DIEM>`** chịu trách nhiệm tổ chức thực hiện Thông tư này .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 5** → `DIEU` (span: `[0:2]`)
- `[e1]` **2 . Chủ tịch Ủy ban nhân dân tỉnh , thành phố trực thuộc trung ương nơi thực hiện thí điểm chịu trách nhiệm tổ chức thực hiện Thông tư này .** → `KHOAN` (span: `[3:23]`)
- `[e2]` **Chủ tịch Ủy ban nhân dân tỉnh , thành phố trực thuộc trung ương** → `CO_QUAN_THAM_QUYEN` (span: `[5:13]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **nơi thực hiện thí điểm** → `DIA_DIEM` (span: `[13:16]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 2 . Chủ tịch Ủy ban nhân dân tỉnh , thành phố trực thuộc trung ương nơi thực hiện thí điểm chịu trách nhiệm tổ chức thực hiện Thông tư này . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 5 `[DIEU]`)


---

### Mẫu #01_2009_TT-BNV_12219#body_context_97 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[01/2009/TT-BNV]`<SO_HIEU>`** ban hành **[ngày 19 tháng 03 năm 2009]`<NGAY_BAN_HANH>`** bởi **[Bộ Nội vụ]`<CO_QUAN_BAN_HANH>`** . **[Điều 5]`<DIEU>`** . **[3 . Trong quá trình tổ chức thực hiện , nếu có vấn đề phát sinh hoặc khó khăn , vướng mắc , **[Ủy ban nhân dân tỉnh , thành phố trực thuộc trung ương]`<CO_QUAN_THAM_QUYEN>`** **[nơi thực hiện thí điểm]`<DIA_DIEM>`** báo cáo về **[Bộ Nội vụ]`<CO_QUAN_THAM_QUYEN>`** để nghiên cứu , giải quyết .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **01/2009/TT-BNV** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Nội vụ** → `CO_QUAN_BAN_HANH` (span: `[11:13]`)
- `[e3]` **ngày 19 tháng 03 năm 2009** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 5** → `DIEU` (span: `[14:16]`)
- `[e5]` **3 . Trong quá trình tổ chức thực hiện , nếu có vấn đề phát sinh hoặc khó khăn , vướng mắc , Ủy ban nhân dân tỉnh , thành phố trực thuộc trung ương nơi thực hiện thí điểm báo cáo về Bộ Nội vụ để nghiên cứu , giải quyết .** → `KHOAN` (span: `[17:52]`)
- `[e6]` **Ủy ban nhân dân tỉnh , thành phố trực thuộc trung ương** → `CO_QUAN_THAM_QUYEN` (span: `[33:40]`) *(lồng trong `e5` (`KHOAN`))*
- `[e7]` **Bộ Nội vụ** → `CO_QUAN_THAM_QUYEN` (span: `[45:47]`) *(lồng trong `e5` (`KHOAN`))*
- `[e8]` **nơi thực hiện thí điểm** → `DIA_DIEM` (span: `[40:43]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 01/2009/TT-BNV `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Nội vụ `[CO_QUAN_BAN_HANH]`)
- (`e1` 01/2009/TT-BNV `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 01/2009/TT-BNV `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 19 tháng 03 năm 2009 `[NGAY_BAN_HANH]`)
- (`e4` Điều 5 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 01/2009/TT-BNV `[SO_HIEU]`)
- (`e5` 3 . Trong quá trình tổ chức thực hiện , nếu có vấn đề phát sinh hoặc khó khăn , vướng mắc , Ủy ban nhân dân tỉnh , thành phố trực thuộc trung ương nơi thực hiện thí điểm báo cáo về Bộ Nội vụ để nghiên cứu , giải quyết . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 5 `[DIEU]`)


---

### Mẫu #01_2009_TT-BNV_12219#body_standalone_98 (Loại: `body_standalone`)
> **[Điều 5]`<DIEU>`** . **[3 . Trong quá trình tổ chức thực hiện , nếu có vấn đề phát sinh hoặc khó khăn , vướng mắc , **[Ủy ban nhân dân tỉnh , thành phố trực thuộc trung ương]`<CO_QUAN_THAM_QUYEN>`** **[nơi thực hiện thí điểm]`<DIA_DIEM>`** báo cáo về **[Bộ Nội vụ]`<CO_QUAN_THAM_QUYEN>`** để nghiên cứu , giải quyết .]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 5** → `DIEU` (span: `[0:2]`)
- `[e1]` **3 . Trong quá trình tổ chức thực hiện , nếu có vấn đề phát sinh hoặc khó khăn , vướng mắc , Ủy ban nhân dân tỉnh , thành phố trực thuộc trung ương nơi thực hiện thí điểm báo cáo về Bộ Nội vụ để nghiên cứu , giải quyết .** → `KHOAN` (span: `[3:38]`)
- `[e2]` **Ủy ban nhân dân tỉnh , thành phố trực thuộc trung ương** → `CO_QUAN_THAM_QUYEN` (span: `[19:26]`) *(lồng trong `e1` (`KHOAN`))*
- `[e3]` **Bộ Nội vụ** → `CO_QUAN_THAM_QUYEN` (span: `[31:33]`) *(lồng trong `e1` (`KHOAN`))*
- `[e4]` **nơi thực hiện thí điểm** → `DIA_DIEM` (span: `[26:29]`) *(lồng trong `e1` (`KHOAN`))*

**Quan hệ:**
- (`e1` 3 . Trong quá trình tổ chức thực hiện , nếu có vấn đề phát sinh hoặc khó khăn , vướng mắc , Ủy ban nhân dân tỉnh , thành phố trực thuộc trung ương nơi thực hiện thí điểm báo cáo về Bộ Nội vụ để nghiên cứu , giải quyết . `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 5 `[DIEU]`)


---

### Mẫu #01_2009_TT-BNV_12219#body_context_99 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[01/2009/TT-BNV]`<SO_HIEU>`** ban hành **[ngày 19 tháng 03 năm 2009]`<NGAY_BAN_HANH>`** bởi **[Bộ Nội vụ]`<CO_QUAN_BAN_HANH>`** . **[Điều 2 . Trình tự , thủ tục bổ nhiệm]`<DIEU>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **01/2009/TT-BNV** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Nội vụ** → `CO_QUAN_BAN_HANH` (span: `[11:13]`)
- `[e3]` **ngày 19 tháng 03 năm 2009** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 2 . Trình tự , thủ tục bổ nhiệm** → `DIEU` (span: `[14:21]`)

**Quan hệ:**
- (`e1` 01/2009/TT-BNV `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Nội vụ `[CO_QUAN_BAN_HANH]`)
- (`e1` 01/2009/TT-BNV `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 01/2009/TT-BNV `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 19 tháng 03 năm 2009 `[NGAY_BAN_HANH]`)
- (`e4` Điều 2 . Trình tự , thủ tục bổ nhiệm `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 01/2009/TT-BNV `[SO_HIEU]`)


---

### Mẫu #01_2009_TT-BNV_12219#body_context_100 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[01/2009/TT-BNV]`<SO_HIEU>`** của **[Bộ Nội vụ]`<CO_QUAN_BAN_HANH>`** trong lĩnh vực **[Nội vụ]`<LINH_VUC>`** . **[Điều 2]`<DIEU>`** . **[4 . **[Hồ sơ trình đề nghị bổ nhiệm]`<GIAY_TO_HO_SO>`**]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **01/2009/TT-BNV** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Nội vụ** → `CO_QUAN_BAN_HANH` (span: `[4:6]`)
- `[e3]` **Nội vụ** → `LINH_VUC` (span: `[8:9]`)
- `[e4]` **Điều 2** → `DIEU` (span: `[10:12]`)
- `[e5]` **4 . Hồ sơ trình đề nghị bổ nhiệm** → `KHOAN` (span: `[13:19]`)
- `[e6]` **Hồ sơ trình đề nghị bổ nhiệm** → `GIAY_TO_HO_SO` (span: `[15:19]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 01/2009/TT-BNV `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Nội vụ `[CO_QUAN_BAN_HANH]`)
- (`e1` 01/2009/TT-BNV `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 01/2009/TT-BNV `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Nội vụ `[LINH_VUC]`)
- (`e4` Điều 2 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 01/2009/TT-BNV `[SO_HIEU]`)
- (`e5` 4 . Hồ sơ trình đề nghị bổ nhiệm `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 2 `[DIEU]`)
- (`e1` 01/2009/TT-BNV `[SO_HIEU]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Nội vụ `[LINH_VUC]`)
- (`e5` 4 . Hồ sơ trình đề nghị bổ nhiệm `[KHOAN]`) ==[ **THUOC_LINH_VUC** ]==> (`e3` Nội vụ `[LINH_VUC]`)


---

### Mẫu #01_2009_TT-BNV_12219#body_context_101 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[01/2009/TT-BNV]`<SO_HIEU>`** ban hành **[ngày 19 tháng 03 năm 2009]`<NGAY_BAN_HANH>`** bởi **[Bộ Nội vụ]`<CO_QUAN_BAN_HANH>`** . **[Điều 2]`<DIEU>`** . **[Khoản 4 . **[Hồ sơ trình đề nghị bổ nhiệm]`<GIAY_TO_HO_SO>`**]`<KHOAN>`** : **[c ) Lý lịch **[cán bộ]`<CHU_THE_CA_NHAN>`** ( **[Mẫu 2C]`<THAM_CHIEU_PHAP_LY>`** – TCTW ) ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **01/2009/TT-BNV** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Nội vụ** → `CO_QUAN_BAN_HANH` (span: `[11:13]`)
- `[e3]` **ngày 19 tháng 03 năm 2009** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 2** → `DIEU` (span: `[14:16]`)
- `[e5]` **Khoản 4 . Hồ sơ trình đề nghị bổ nhiệm** → `KHOAN` (span: `[17:24]`)
- `[e6]` **c ) Lý lịch cán bộ ( Mẫu 2C – TCTW ) ;** → `DIEM` (span: `[25:36]`)
- `[e7]` **Mẫu 2C** → `THAM_CHIEU_PHAP_LY` (span: `[30:32]`) *(lồng trong `e6` (`DIEM`))*
- `[e8]` **Hồ sơ trình đề nghị bổ nhiệm** → `GIAY_TO_HO_SO` (span: `[20:24]`) *(lồng trong `e5` (`KHOAN`))*
- `[e9]` **cán bộ** → `CHU_THE_CA_NHAN` (span: `[28:29]`) *(lồng trong `e6` (`DIEM`))*

**Quan hệ:**
- (`e1` 01/2009/TT-BNV `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Nội vụ `[CO_QUAN_BAN_HANH]`)
- (`e1` 01/2009/TT-BNV `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 01/2009/TT-BNV `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 19 tháng 03 năm 2009 `[NGAY_BAN_HANH]`)
- (`e4` Điều 2 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 01/2009/TT-BNV `[SO_HIEU]`)
- (`e5` Khoản 4 . Hồ sơ trình đề nghị bổ nhiệm `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 2 `[DIEU]`)
- (`e6` c ) Lý lịch cán bộ ( Mẫu 2C – TCTW ) ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e5` Khoản 4 . Hồ sơ trình đề nghị bổ nhiệm `[KHOAN]`)
- (`e6` c ) Lý lịch cán bộ ( Mẫu 2C – TCTW ) ; `[DIEM]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e7` Mẫu 2C `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #01_2009_TT-BNV_12219#body_standalone_102 (Loại: `body_standalone`)
> **[Điều 2]`<DIEU>`** . **[Khoản 4 . **[Hồ sơ trình đề nghị bổ nhiệm]`<GIAY_TO_HO_SO>`**]`<KHOAN>`** : **[c ) Lý lịch **[cán bộ]`<CHU_THE_CA_NHAN>`** ( **[Mẫu 2C]`<THAM_CHIEU_PHAP_LY>`** – TCTW ) ;]`<DIEM>`**

**Thực thể:**
- `[e0]` **Điều 2** → `DIEU` (span: `[0:2]`)
- `[e1]` **Khoản 4 . Hồ sơ trình đề nghị bổ nhiệm** → `KHOAN` (span: `[3:10]`)
- `[e2]` **c ) Lý lịch cán bộ ( Mẫu 2C – TCTW ) ;** → `DIEM` (span: `[11:22]`)
- `[e3]` **Mẫu 2C** → `THAM_CHIEU_PHAP_LY` (span: `[16:18]`) *(lồng trong `e2` (`DIEM`))*
- `[e4]` **Hồ sơ trình đề nghị bổ nhiệm** → `GIAY_TO_HO_SO` (span: `[6:10]`) *(lồng trong `e1` (`KHOAN`))*
- `[e5]` **cán bộ** → `CHU_THE_CA_NHAN` (span: `[14:15]`) *(lồng trong `e2` (`DIEM`))*

**Quan hệ:**
- (`e1` Khoản 4 . Hồ sơ trình đề nghị bổ nhiệm `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 2 `[DIEU]`)
- (`e2` c ) Lý lịch cán bộ ( Mẫu 2C – TCTW ) ; `[DIEM]`) ==[ **THUOC_VE** ]==> (`e1` Khoản 4 . Hồ sơ trình đề nghị bổ nhiệm `[KHOAN]`)
- (`e2` c ) Lý lịch cán bộ ( Mẫu 2C – TCTW ) ; `[DIEM]`) ==[ **VIEN_DAN_THAM_CHIEU** ]==> (`e3` Mẫu 2C `[THAM_CHIEU_PHAP_LY]`) *(Quan hệ lồng nhau)*


---

### Mẫu #01_2009_TT-BNV_12219#body_context_103 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[01/2009/TT-BNV]`<SO_HIEU>`** ban hành **[ngày 19 tháng 03 năm 2009]`<NGAY_BAN_HANH>`** bởi **[Bộ Nội vụ]`<CO_QUAN_BAN_HANH>`** . **[Điều 3]`<DIEU>`** . **[1 . Các trường hợp miễn nhiệm]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **01/2009/TT-BNV** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Nội vụ** → `CO_QUAN_BAN_HANH` (span: `[11:13]`)
- `[e3]` **ngày 19 tháng 03 năm 2009** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 3** → `DIEU` (span: `[14:16]`)
- `[e5]` **1 . Các trường hợp miễn nhiệm** → `KHOAN` (span: `[17:22]`)

**Quan hệ:**
- (`e1` 01/2009/TT-BNV `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Nội vụ `[CO_QUAN_BAN_HANH]`)
- (`e1` 01/2009/TT-BNV `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 01/2009/TT-BNV `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 19 tháng 03 năm 2009 `[NGAY_BAN_HANH]`)
- (`e4` Điều 3 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 01/2009/TT-BNV `[SO_HIEU]`)
- (`e5` 1 . Các trường hợp miễn nhiệm `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 3 `[DIEU]`)


---

### Mẫu #01_2009_TT-BNV_12219#body_context_104 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[01/2009/TT-BNV]`<SO_HIEU>`** ban hành **[ngày 19 tháng 03 năm 2009]`<NGAY_BAN_HANH>`** bởi **[Bộ Nội vụ]`<CO_QUAN_BAN_HANH>`** . **[Điều 3]`<DIEU>`** . **[Khoản 1 . Các trường hợp miễn nhiệm]`<KHOAN>`** : **[d ) Vì lý do cá nhân khác .]`<DIEM>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **01/2009/TT-BNV** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Nội vụ** → `CO_QUAN_BAN_HANH` (span: `[11:13]`)
- `[e3]` **ngày 19 tháng 03 năm 2009** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 3** → `DIEU` (span: `[14:16]`)
- `[e5]` **Khoản 1 . Các trường hợp miễn nhiệm** → `KHOAN` (span: `[17:23]`)
- `[e6]` **d ) Vì lý do cá nhân khác .** → `DIEM` (span: `[24:31]`)

**Quan hệ:**
- (`e1` 01/2009/TT-BNV `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Nội vụ `[CO_QUAN_BAN_HANH]`)
- (`e1` 01/2009/TT-BNV `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 01/2009/TT-BNV `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 19 tháng 03 năm 2009 `[NGAY_BAN_HANH]`)
- (`e4` Điều 3 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 01/2009/TT-BNV `[SO_HIEU]`)
- (`e5` Khoản 1 . Các trường hợp miễn nhiệm `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 3 `[DIEU]`)
- (`e6` d ) Vì lý do cá nhân khác . `[DIEM]`) ==[ **THUOC_VE** ]==> (`e5` Khoản 1 . Các trường hợp miễn nhiệm `[KHOAN]`)


---

### Mẫu #01_2009_TT-BNV_12219#body_context_105 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[01/2009/TT-BNV]`<SO_HIEU>`** ban hành **[ngày 19 tháng 03 năm 2009]`<NGAY_BAN_HANH>`** bởi **[Bộ Nội vụ]`<CO_QUAN_BAN_HANH>`** . **[Điều 3]`<DIEU>`** . **[2 . Trình tự , thủ tục miễn nhiệm]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **01/2009/TT-BNV** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Nội vụ** → `CO_QUAN_BAN_HANH` (span: `[11:13]`)
- `[e3]` **ngày 19 tháng 03 năm 2009** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 3** → `DIEU` (span: `[14:16]`)
- `[e5]` **2 . Trình tự , thủ tục miễn nhiệm** → `KHOAN` (span: `[17:23]`)

**Quan hệ:**
- (`e1` 01/2009/TT-BNV `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Nội vụ `[CO_QUAN_BAN_HANH]`)
- (`e1` 01/2009/TT-BNV `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 01/2009/TT-BNV `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 19 tháng 03 năm 2009 `[NGAY_BAN_HANH]`)
- (`e4` Điều 3 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 01/2009/TT-BNV `[SO_HIEU]`)
- (`e5` 2 . Trình tự , thủ tục miễn nhiệm `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 3 `[DIEU]`)


---

### Mẫu #01_2009_TT-BNV_12219#body_standalone_106 (Loại: `body_standalone`)
> **[Điều 3]`<DIEU>`** . **[2 . Trình tự , thủ tục miễn nhiệm]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Điều 3** → `DIEU` (span: `[0:2]`)
- `[e1]` **2 . Trình tự , thủ tục miễn nhiệm** → `KHOAN` (span: `[3:9]`)

**Quan hệ:**
- (`e1` 2 . Trình tự , thủ tục miễn nhiệm `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e0` Điều 3 `[DIEU]`)


---

### Mẫu #01_2009_TT-BNV_12219#body_context_107 (Loại: `body_context`)
> **[Thông tư]`<LOAI_VAN_BAN>`** số **[01/2009/TT-BNV]`<SO_HIEU>`** ban hành **[ngày 19 tháng 03 năm 2009]`<NGAY_BAN_HANH>`** bởi **[Bộ Nội vụ]`<CO_QUAN_BAN_HANH>`** . **[Điều 3]`<DIEU>`** . **[3 . **[Hồ sơ miễn nhiệm]`<GIAY_TO_HO_SO>`**]`<KHOAN>`**

**Thực thể:**
- `[e0]` **Thông tư** → `LOAI_VAN_BAN` (span: `[0:1]`)
- `[e1]` **01/2009/TT-BNV** → `SO_HIEU` (span: `[2:3]`)
- `[e2]` **Bộ Nội vụ** → `CO_QUAN_BAN_HANH` (span: `[11:13]`)
- `[e3]` **ngày 19 tháng 03 năm 2009** → `NGAY_BAN_HANH` (span: `[4:10]`)
- `[e4]` **Điều 3** → `DIEU` (span: `[14:16]`)
- `[e5]` **3 . Hồ sơ miễn nhiệm** → `KHOAN` (span: `[17:21]`)
- `[e6]` **Hồ sơ miễn nhiệm** → `GIAY_TO_HO_SO` (span: `[19:21]`) *(lồng trong `e5` (`KHOAN`))*

**Quan hệ:**
- (`e1` 01/2009/TT-BNV `[SO_HIEU]`) ==[ **BAN_HANH_BOI** ]==> (`e2` Bộ Nội vụ `[CO_QUAN_BAN_HANH]`)
- (`e1` 01/2009/TT-BNV `[SO_HIEU]`) ==[ **LA_LOAI_VAN_BAN** ]==> (`e0` Thông tư `[LOAI_VAN_BAN]`)
- (`e1` 01/2009/TT-BNV `[SO_HIEU]`) ==[ **BAN_HANH_NGAY** ]==> (`e3` ngày 19 tháng 03 năm 2009 `[NGAY_BAN_HANH]`)
- (`e4` Điều 3 `[DIEU]`) ==[ **THUOC_VE** ]==> (`e1` 01/2009/TT-BNV `[SO_HIEU]`)
- (`e5` 3 . Hồ sơ miễn nhiệm `[KHOAN]`) ==[ **THUOC_VE** ]==> (`e4` Điều 3 `[DIEU]`)


---
