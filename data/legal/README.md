# Pipeline dữ liệu văn bản pháp luật (Joint NER + RE)

Nguồn: Google Drive (crawl từ vbpl.vn). **Chỉ dùng `thuoc_tinh.json` và `muc_luc.json`** làm nguồn nhãn. `noi_dung.docx` chỉ dùng để lấy phần đầu văn bản và khối chữ ký. Không dùng `luoc_do.json`.

## Chạy
```powershell
# 1. Tải mẫu: nghị định / thông tư / quyết định, năm >= 2006
python -m data.legal.download_docs --per-category 35
# 2. Sinh nhãn + chia train/dev/test theo văn bản
python -m data.legal.build_dataset
```

| File | Vai trò |
|---|---|
| `schema.py` | Danh sách nhãn thực thể/quan hệ + cặp kiểu hợp lệ cho từng quan hệ |
| `drive_client.py` | Đọc thư mục Drive từng tầng một, có cache và retry khi bị chặn |
| `download_docs.py` | Bước 1: tải dữ liệu → `raw/<nhóm>/<văn bản>/` |
| `build_dataset.py` | Bước 2: sinh mẫu → `processed/{train,dev,test}.json`, `stats.json` |
| `vi_tokenize.py` | Hàm tách từ **dùng chung cho cả lúc sinh dữ liệu và lúc suy luận** (giữ nguyên mã số hiệu thành 1 token) |
| `law_lexicon.txt` | Từ điển tên luật, tự khai thác từ các dòng "Căn cứ Luật X ngày/số …" |

## Bộ nhãn
**Mẫu `meta`**: ghép phần đầu văn bản (số hiệu, ngày, cơ quan, tên loại) với khối chữ ký. Nhãn được căn chỉnh theo `thuoc_tinh.json`.
- Thực thể: `SO_HIEU`, `LOAI_VB`, `CO_QUAN`, `NGAY`, `NGUOI`, `CHUC_DANH`
- Quan hệ: `SO_HIEU→CO_QUAN (BAN_HANH_BOI)`, `SO_HIEU→NGAY (NGAY_BAN_HANH)`, `SO_HIEU→NGUOI (KY_BOI)`, `SO_HIEU→LOAI_VB (LA_LOAI)`, `NGUOI→CHUC_DANH (GIU_CHUC_VU)`

**Mẫu `body`**: mỗi node Điều/Khoản/Điểm trong `muc_luc.json` là một mẫu. Node dài hơn 120 âm tiết thì được tách nhỏ.
- Thực thể: `DIEU`, `KHOAN`, `DIEM`, `VAN_BAN` ("Nghị định này", "Nghị định số 15/2006/NĐ-CP", "Luật Nhà ở")
- Quan hệ: `THUOC` theo chiều điểm → khoản → Điều → văn bản. Cách viết liệt kê ("khoản 1, 2 và 3 Điều 5", "từ khoản 1 đến khoản 15 Điều này") cũng được xử lý.
- `muc_luc.json` còn được dùng để **kiểm chứng tham chiếu nội bộ**, tức Điều/khoản được nhắc đến có thật sự tồn tại trong văn bản không. Kết quả nằm trong `stats.json`.

## Làm sạch dữ liệu
- Chuẩn hóa Unicode NFC, chuyển `Ð` (U+00D0) thành `Đ` (U+0110), bỏ các dòng trang trí `-----`, `____`.
- Chuyển `<w:br/>`/`<w:tab/>` trong docx thành khoảng trắng. Nếu không, chữ bị dính kiểu "PHÓ THỦ TƯỚNGTrần Hồng Hà".
- Sửa âm tiết bị tách do lỗi crawl: "C ông chứng" → "Công chứng", "V ă n" → "Văn".
- Chức danh trong metadata hay dài hơn chữ ký ("Phó Thủ tướng Chính phủ" so với "PHÓ THỦ TƯỚNG"), nên khi khớp sẽ thử các tiền tố ngắn dần.
- Mẫu meta không có quan hệ nào (do mất dòng "Số:" khi crawl) sẽ bị bỏ.
- Mẫu dài hơn 250 subword PhoBERT sẽ bị bỏ.
- Chia train/dev/test **theo văn bản**, có phân tầng theo nhóm, để tránh rò rỉ dữ liệu giữa các tập.

## Hạn chế đã biết (cần ghi trong báo cáo)
1. Đây là nhãn tự sinh (distant supervision), nên **tập test cần được rà soát hoặc gán lại bằng tay**.
2. Khoảng 30% văn bản mất phần đầu hoặc khối chữ ký do lỗi crawl, nên tỉ lệ có `NGUOI` và `CHUC_DANH` thấp hơn các thực thể khác.
3. Trong **văn bản sửa đổi**, tham chiếu không ghi rõ văn bản ("khoản 1 Điều 47") thực chất trỏ tới văn bản *bị sửa đổi*. Thống kê được tách riêng với tiền tố `amend_`.
4. Tên luật chỉ được nhận diện nếu có trong `law_lexicon.txt`. Các luật không xuất hiện trong dòng "Căn cứ" của kho dữ liệu sẽ bị bỏ sót.
5. Liệt kê kiểu "điểm a, b khoản 1": chỉ "điểm a" được gán nhãn, còn "b" (chỉ có chữ cái đứng một mình) thì bị bỏ qua.
