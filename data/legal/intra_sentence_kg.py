"""
Bộ trích xuất Thực thể Lồng nhau (Nested Entities) và Đồ thị Tri thức Nội câu (Intra-Sentence KG)
cho văn bản quy phạm pháp luật Việt Nam theo nguyên tắc Hub-Centered (Hành vi & Chế tài làm tâm).
"""
import re
from data.legal.vi_tokenize import vi_tokenize
from data.legal.schema import (
    OUTER_HUB_ENTITY_TYPES,
    INNER_SATELLITE_ENTITY_TYPES,
    RELATION_CONSTRAINTS,
)

MAX_SPAN_TOKENS = 16

# Chuỗi tham chiếu điều khoản đầy đủ từ nhỏ đến lớn: [ý (i)] + [điểm a, b] + [khoản 1, 2] + [(vào/sau) Điều X, Y] + [(của) Nghị định/Luật ...]
_DOC_TAIL_REF = (
    r"(?:\s+(?:của\s+)?(?:"
    r"(?:Bộ\s+luật|Luật|Nghị\s+định|Thông\s+tư|Quyết\s+định|Pháp\s+lệnh|Nghị\s+quyết)\s+(?:này|số\s+\d+(?:/\d{4})?/[A-ZĐa-zđ0-9-]+)"
    r"|(?:Bộ\s+luật|Luật)\s+(?:Lao\s+động|Hình\s+sự|Dân\s+sự|Chứng\s+khoán|Doanh\s+nghiệp|Đầu\s+tư|Đất\s+đai|Thương\s+mại|Xử\s+lý\s+vi\s+phạm\s+hành\s+chính|Sở\s+hữu\s+trí\s+tuệ|Bảo\s+hiểm\s+xã\s+hội|Giao\s+thông\s+đường\s+bộ|Công\s+chứng|Luật\s+sư|Các\s+tổ\s+chức\s+tín\s+dụng|Ngân\s+hàng\s+Nhà\s+nước\s+Việt\s+Nam|Tổ\s+chức\s+Chính\s+phủ|Phòng,\s*chống\s+rửa\s+tiền|Phòng,\s*chống\s+khủng\s+bố)"
    r"))?"
)

_FULL_PROVISION_REF = (
    r"(?:(?:(?:các\s+)?điểm\s+[a-zđ]\d?(?:\([ivx0-9]+\))?(?:\s*(?:,|và)\s*(?:điểm\s+)?[a-zđ]\d?(?:\([ivx0-9]+\))?)*\s+)?(?:các\s+)?khoản\s+\d+[a-z]?(?:\s*(?:,|và)\s*(?:khoản\s+)?\d+[a-z]?)*\s*,\s*)*"
    r"(?:(?:các\s+)?(?:ý|tiết)\s+\([ivx0-9]+\)(?:\s*(?:,|và)\s*(?:(?:ý|tiết)\s+)?\([ivx0-9]+\))*\s+)?"
    r"(?:(?:các\s+)?điểm\s+[a-zđ]\d?(?:\([ivx0-9]+\))?(?:\s*(?:,|và)\s*(?:điểm\s+)?[a-zđ]\d?(?:\([ivx0-9]+\))?)*\s+)?"
    r"(?:(?:các\s+)?khoản\s+\d+[a-z]?(?:\s*(?:,|và)\s*(?:khoản\s+)?\d+[a-z]?)*\s+)?"
    r"(?:(?:vào\s+sau|vào\s+trước|vào|sau|trước|của)\s+)?(?:các\s+)?(?:Điều\s+(?:\d+[a-z]?(?:\s*(?:,|và)\s*(?:Điều\s+)?\d+[a-z]?)*|này))"
    + _DOC_TAIL_REF
)

# ======================================================================
# 1. Bộ mẫu Regex cho các Thực thể Vệ tinh / Lồng bên trong (Inner/Satellite Spans)
#    Đặt THAM_CHIEU_PHAP_LY lên đầu để các tên Luật/Nghị định không bị cắt ngang.
# ======================================================================
INNER_PATTERNS = [
    (
        "THAM_CHIEU_PHAP_LY",
        re.compile(
            r"(?:"
            # 1. Văn bản kèm số hiệu (có hoặc không có tên Luật/Nghị định ở giữa, VD: Luật Doanh nghiệp số 59/2020/QH14, Luật Phòng, chống rửa tiền số 14/2022/QH15)
            r"\b((?:Bộ\s+luật|Luật|Nghị\s+định|Thông\s+tư(?:\s+liên\s+tịch)?|Quyết\s+định|Nghị\s+quyết|Pháp\s+lệnh|Chỉ\s+thị)(?:\s+(?!số\s+\d|sửa\s+đổi,\s*bổ\s+sung\s+một\s+số\s+điều\s+của\s+(?:Nghị\s+định|Thông\s+tư|Luật|Bộ\s+luật|Quyết\s+định)\s+số)(?:(?!được\s+sửa\s+đổi|số\s+\d|ngày\s+\d|\b(?:Bộ\s+luật|Luật|Nghị\s+định|Thông\s+tư|Quyết\s+định)\s+số\b)[^.;:()0-9]){1,65}?)?\s+số\s+\d+(?:/\d{4})?/[A-ZĐa-zđ0-9-]+)"
            # 2. Căn cứ + Tên Luật/Bộ luật/Pháp lệnh KHÔNG kèm số hiệu ở sau
            r"|(?<=Căn cứ )("
                r"(?:Bộ\s+luật|Luật|Pháp\s+lệnh)\s+(?!số\s+\d)"
                r"(?:sửa\s+đổi,\s*bổ\s+sung\s+một\s+số\s+điều\s+của\s+)?"
                r"(?:(?!số\s+\d)[^,.;:()]){3,85}?"
            r")(?=\s*[;,.]|$|\s+(?:ngày\s+\d|được\s+sửa\s+đổi|và\s+(?:Luật|Bộ\s+luật|Nghị\s+định)|của\s+|quy\s+định\s+))"
            r"|(?<=và )("
                r"(?:Bộ\s+luật|Luật|Pháp\s+lệnh)\s+(?!số\s+\d)"
                r"(?:sửa\s+đổi,\s*bổ\s+sung\s+một\s+số\s+điều\s+của\s+)?"
                r"(?:(?!số\s+\d)[^,.;:()]){3,85}?"
            r")(?=\s+(?:ngày\s+\d|của\s+Chính\s+phủ|của\s+Quốc\s+hội))"
            # 3. Mẫu biểu / Phụ lục / Mục / Chương (Chỉ bắt Chương/Mục khi có từ khóa viện dẫn phía trước)
            r"|\b((?:Mẫu\s+biểu|Mẫu|Phụ\s+lục)\s+(?:số\s+)?[0-9IVX]+[a-z]?(?:\s+(?:đính\s+kèm|ban\s+hành\s+kèm\s+theo)\s+(?:Nghị\s+định|Thông\s+tư|Quyết\s+định|Luật)\s+này)?)"
            r"|\b(?:tại|theo|của|trong|quy\s+định\s+tại)\s+((?:Mục\s+\d+[a-z]?\s+)?Chương\s+[IVX0-9]+)"


            # 4. Tổ hợp đầy đủ có Điều (có ý/tiết/điểm/khoản ở trước HOẶC của Nghị định/Luật ở sau)
            r"|\b("
                r"(?:(?:các\s+)?(?:ý|tiết)\s+\([ivx0-9]+\)(?:\s*(?:,|và)\s*(?:(?:ý|tiết)\s+)?\([ivx0-9]+\))*\s+)" + _FULL_PROVISION_REF
                + r"|(?:(?:các\s+)?điểm\s+[a-zđ]\d?(?:\([ivx0-9]+\))?(?:\s*(?:,|và)\s*(?:điểm\s+)?[a-zđ]\d?(?:\([ivx0-9]+\))?)*\s+)" + _FULL_PROVISION_REF
                + r"|(?:(?:các\s+)?khoản\s+\d+[a-z]?(?:\s*(?:,|và)\s*(?:khoản\s+)?\d+[a-z]?)*\s+)" + _FULL_PROVISION_REF
                + r"|(?:các\s+)?Điều\s+\d+[a-z]?(?:\s*(?:,|và)\s*(?:Điều\s+)?\d+[a-z]?)+" + _DOC_TAIL_REF
                + r"|Điều\s+(?:\d+[a-z]?|này)\s+(?:của\s+)?(?:(?:Bộ\s+luật|Luật|Nghị\s+định|Thông\s+tư|Quyết\s+định|Pháp\s+lệnh|Nghị\s+quyết)\s+(?:này|số\s+\d+(?:/\d{4})?/[A-ZĐa-zđ0-9-]+)|(?:Bộ\s+luật|Luật)\s+(?:Lao\s+động|Hình\s+sự|Dân\s+sự|Chứng\s+khoán|Doanh\s+nghiệp|Đầu\s+tư|Đất\s+đai|Thương\s+mại|Xử\s+lý\s+vi\s+phạm\s+hành\s+chính|Sở\s+hữu\s+trí\s+tuệ|Bảo\s+hiểm\s+xã\s+hội|Giao\s+thông\s+đường\s+bộ|Công\s+chứng|Luật\s+sư|Các\s+tổ\s+chức\s+tín\s+dụng))"
                + r"|Điều\s+này"
            r")"
            # 5. Sau các động từ lập pháp / giới từ đối chiếu (Sửa đổi, bổ sung, bãi bỏ, vào sau, quy định tại, nêu tại, áp dụng)
            r"|(?:Sửa\s+đổi,\s*bổ\s+sung(?:\s+một\s+số\s+(?:điều|điểm,\s*khoản)\s+của)?|Sửa\s+đổi(?:\s+tên)?|bổ\s+sung|Bãi\s+bỏ|vào\s+sau|vào\s+trước|sau|quy\s+định\s+tại|nêu\s+tại|áp\s+dụng)\s+("
                + _FULL_PROVISION_REF
                + r"|(?:các\s+)?điểm\s+[a-zđ]\d?(?:\s*(?:,|và)\s*(?:điểm\s+)?[a-zđ]\d?)*(?:\s+khoản\s+\d+[a-z]?(?:\s+Điều\s+này)?)?"
                + r"|(?:các\s+)?khoản\s+\d+[a-z]?(?:\s*(?:,|và)\s*(?:khoản\s+)?\d+[a-z]?)*(?:\s+Điều\s+này)?"
                + r"|điểm\s+[a-zđ]\d?\s+khoản\s+này|khoản\s+này|điểm\s+này"
                + r"|(?:Bộ\s+luật|Luật|Nghị\s+định|Thông\s+tư|Quyết\s+định|Pháp\s+lệnh)\s+này"
            r")"
            # 6. Điều độc lập nằm trong chuỗi liệt kê phân cách bằng dấu chấm phẩy (; Điều 25;)
            r"|(?<=; )(Điều\s+\d+[a-z]?)(?=\s*[;,])"
            r")",
            re.I,
        ),
    ),
    (
        "TU_KHOA_PHAP_LY",
        re.compile(
            r"(?:"
            r"^(Căn\s+cứ)\b"
            r"|\b(được\s+sửa\s+đổi,\s*bổ\s+sung\s+(?:một\s+số\s+điều\s+theo|bởi))\b"
            r"|\b(Thay\s+thế\s+cụm\s+từ(?:\s+và\s+bãi\s+bỏ\s+một\s+số\s+(?:điều|khoản|điểm)\s+của)?)\b"
            r"|\b(Sửa\s+đổi,\s*bổ\s+sung(?:\s+một\s+số\s+(?:điều|điểm,\s*khoản)\s+của|\s+tiêu\s+đề)?|Sửa\s+đổi(?:\s+tên)?|Bổ\s+sung|Bãi\s+bỏ(?:\s+một\s+số\s+(?:điều|khoản|điểm)\s+của)?)\b(?=\s+(?:các\s+|một\s+số\s+|tiêu\s+đề\s+)?(?:ý|tiết|điểm|khoản|Điều|Mục|Chương|Mẫu|Phụ\s+lục|Nghị\s+định|Thông\s+tư|Luật|Bộ\s+luật|Quyết\s+định))"
            r"|\b(theo\s+quy\s+định\s+tại|quy\s+định\s+tại|nêu\s+tại)\b(?=\s+(?:các\s+)?(?:ý|tiết|điểm|khoản|Điều|Mục|Chương|Phụ\s+lục|Mẫu|Nghị\s+định|Thông\s+tư|Luật|Bộ\s+luật|Quyết\s+định))"
            r")",
            re.I,
        ),
    ),
    (
        "NGAY_THAM_CHIEU",
        re.compile(
            r"\bngày\s+\d{1,2}\s+tháng\s+\d{1,2}\s+năm\s+\d{4}\b"
            r"|\bngày\s+\d{1,2}/\d{1,2}/\d{4}\b"
            r"|(?<!\d)\d{1,2}/\d{1,2}/\d{4}(?!\d)",
            re.I,
        ),
    ),
    (
        "LINH_VUC",
        re.compile(
            r"(?:"
            r"\b(lĩnh\s+vực\s+(?:"
                r"chứng\s+khoán(?:\s+và\s+thị\s+trường\s+chứng\s+khoán)?"
                r"|bảo\s+vệ\s+quyền\s+lợi\s+người\s+tiêu\s+dùng"
                r"|sở\s+hữu\s+công\s+nghiệp"
                r"|bổ\s+trợ\s+tư\s+pháp"
                r"|hành\s+chính\s+tư\s+pháp"
                r"|hôn\s+nhân\s+và\s+gia\s+đình"
                r"|thi\s+hành\s+án\s+dân\s+sự"
                r"|phá\s+sản\s+doanh\s+nghiệp,\s*hợp\s+tác\s+xã"
                r"|giao\s+thông\s+đường\s+bộ(?:\s+và\s+đường\s+sắt)?"
                r"|vận\s+tải\s+đường\s+bộ|đường\s+bộ|đường\s+sắt|đường\s+thủy\s+nội\s+địa"
                r"|hàng\s+hải|hàng\s+không(?:\s+dân\s+dụng)?|đăng\s+kiểm|an\s+toàn\s+giao\s+thông"
                r"|tiền\s+tệ\s+và\s+ngân\s+hàng|chính\s+sách\s+tiền\s+tệ|tín\s+dụng|ngân\s+hàng|Kho\s+bạc\s+Nhà\s+nước"
                r"|thuế\s+và\s+hải\s+quan|chính\s+sách\s+thuế|thuế|hải\s+quan|phí\s+và\s+lệ\s+phí|tài\s+chính"
                r"|kế\s+toán(?:,\s*kiểm\s+toán(?:\s+độc\s+lập)?)?|chuyên\s+môn\s+kế\s+toán|kiểm\s+toán|giá|xổ\s+số"
                r"|kinh\s+doanh\s+bảo\s+hiểm|bảo\s+hiểm(?:\s+nhân\s+thọ)?"
                r"|lao\s+động(?:,\s*tiền\s+lương,\s*tiền\s+công)?|quan\s+hệ\s+lao\s+động"
                r"|(?:kiểm\s+định\s+kỹ\s+thuật\s+)?an\s+toàn\s+lao\s+động(?:\s+trong\s+thi\s+công\s+xây\s+dựng)?|đảm\s+bảo\s+xã\s+hội"
                r"|(?:hoạt\s+động\s+)?đầu\s+tư\s+xây\s+dựng|phát\s+triển\s+đô\s+thị|hạ\s+tầng\s+kỹ\s+thuật|nhà\s+ở"
                r"|(?:kinh\s+doanh\s+)?bất\s+động\s+sản|vật\s+liệu\s+xây\s+dựng|quy\s+hoạch(?:\s*-\s*kiến\s+trúc)?"
                r"|quản\s+lý\s+chất\s+lượng\s+công\s+trình\s+xây\s+dựng|thí\s+nghiệm\s+chuyên\s+ngành\s+xây\s+dựng|xây\s+dựng"
                r"|tài\s+nguyên\s+và\s+môi\s+trường|bảo\s+vệ\s+môi\s+trường|phân\s+tích\s+môi\s+trường|quản\s+lý\s+tài\s+nguyên\s+đất|đất\s+đai|dầu\s+khí"
                r"|nông\s+nghiệp|lâm\s+nghiệp|thủy\s+sản"
                r"|thương\s+mại\s+điện\s+tử|thương\s+mại|công\s+nghiệp|sản\s+xuất"
                r"|công\s+nghệ\s+thông\s+tin|viễn\s+thông(?:\s+và\s+Internet)?|khoa\s+học\s+(?:và\s+)?công\s+nghệ|công\s+nghệ\s+cao|tiêu\s+chuẩn"
                r"|giáo\s+dục\s*(?:-|và)\s*đào\s+tạo|y\s+tế|văn\s+hóa|nghệ\s+thuật|xuất\s+bản,\s*in,\s*phát\s+hành|in"
                r"|nuôi\s+con\s+nuôi(?:\s+có\s+yếu\s+tố\s+nước\s+ngoài|\s+quốc\s+tế)?|giám\s+định\s+tư\s+pháp|thừa\s+phát\s+lại|hộ\s+tịch,\s*quốc\s+tịch,\s*chứng\s+thực|tư\s+pháp|dân\s+sự|hành\s+chính"
                r"|quốc\s+phòng|an\s+ninh(?:\s+quốc\s+phòng|,\s*trật\s+tự,\s*an\s+toàn\s+xã\s+hội)?|quản\s+lý\s+vùng\s+trời"
                r"|kế\s+hoạch\s+và\s+đầu\s+tư|đấu\s+thầu|đầu\s+tư|kinh\s+tế(?:\s*-\s*xã\s+hội)?|chính\s+trị"
                r"|phòng,\s*chống\s+rửa\s+tiền|phòng,\s*chống\s+khủng\s+bố"
                r"|quản\s+lý\s+nhà\s+nước\s+của\s+Bộ\s+(?:Xây\s+dựng|Tài\s+chính|Tư\s+pháp|Giao\s+thông\s+vận\s+tải|Công\s+Thương|Lao\s+động\s*-\s*Thương\s+binh\s+và\s+Xã\s+hội|Nông\s+nghiệp\s+và\s+Phát\s+triển\s+nông\s+thôn|Tài\s+nguyên\s+và\s+Môi\s+trường|Thông\s+tin\s+và\s+Truyền\s+thông|Kế\s+hoạch\s+và\s+Đầu\s+tư|Y\s+tế|Giáo\s+dục\s+và\s+Đào\s+tạo|Nội\s+vụ|Công\s+an|Quốc\s+phòng)"
            r"))\b"
            r"|(?<=về\s)(chứng\s+khoán(?:\s+phái\s+sinh)?\s+và\s+thị\s+trường\s+chứng\s+khoán(?:\s+phái\s+sinh)?)\b"
            r"|\b(ngành\s+(?:Kế\s+hoạch\s+và\s+Đầu\s+tư(?:\s+Việt\s+Nam)?|Thống\s+kê|Tư\s+pháp|Tài\s+chính|Ngân\s+hàng|Giao\s+thông\s+vận\s+tải|Xây\s+dựng|Y\s+tế|Giáo\s+dục|tài\s+nguyên\s+và\s+môi\s+trường))\b"
            r")",
            re.I,
        ),
    ),
    (
        "MUC_TIEN",
        re.compile(
            r"\b\d{1,3}(?:[.,]\d{3})+(?:\s*đồng|\s*VNĐ)\b"
            r"|\b\d+(?:[.,]\d+)?\s*(?:\([a-zđÀ-ỹ]+\)\s*)?(?:triệu|tỷ|nghìn|ngàn)\s*(?:đồng|VNĐ)?\b",
            re.I,
        ),
    ),
    (
        "THOI_HAN",
        re.compile(
            r"\b(?:trong\s+thời\s+hạn|trong\s+thời\s+gian|thời\s+hạn|trong\s+vòng)\s+\d+\s+(?:ngày|tháng|năm)(?:\s+làm\s+việc)?\b"
            r"|\btừ\s+\d+\s+(?:ngày|tháng|năm)(?:\s+làm\s+việc)?\s+đến\s+(?:dưới\s+)?\d+\s+(?:ngày|tháng|năm)(?:\s+làm\s+việc)?\b"
            r"|\btừ\s+\d+\s+(?:ngày|tháng|năm)(?:\s+làm\s+việc)?\s+trở\s+lên\b"
            r"|\b(?:sau|trước|quá|dưới|trên|đủ)\s+\d+\s+(?:ngày|tháng|năm)(?:\s+làm\s+việc)?\b"
            r"|\b(?:tối\s+thiểu|tối\s+đa)(?:\s+là)?\s+(?:\d+(?:\s*\([a-zđÀ-ỹ]+\))?|một|hai|ba|bốn|năm|sáu|bảy|tám|chín|mười)\s+(?:ngày|tháng|năm|giờ)\b"
            r"|\bkhông\s+quá\s+\d+\s+(?:giờ|ngày|tháng|năm|tuần)\b"
            r"|\b\d+\s+(?:ngày|tháng|năm)\s+(?:tù|tạm\s+giữ|tạm\s+giam|cải\s+tạo(?:\s+không\s+giam\s+giữ)?|làm\s+việc)\b",
            re.I,
        ),
    ),
    (
        "NGUONG_DINH_LUONG",
        re.compile(
            r"\btừ\s+\d+(?:[.,]\d+)?\s*%\s+đến\s+\d+(?:[.,]\d+)?\s*%"
            r"|\btừ\s+\d+(?:[.,]\d+)?\s*%\s+trở\s+lên\b"
            r"|\btừ\s+\d+\s+(?:người|lần|đơn\s+vị|tấn|kg|m2|ha|tuổi|công\s+ty)\s+đến\s+(?:dưới\s+)?\d+\s+(?:người|lần|đơn\s+vị|tấn|kg|m2|ha|tuổi|công\s+ty)\b"
            r"|\b(?:quá|trên|dưới|từ|đủ)\s+\d+\s+(?:tuổi|công\s+ty(?:\s+khác)?|người|lần)\b"
            r"|\b\d+(?:[.,]\d+)?\s*%",
            re.I,
        ),
    ),
    (
        "CO_QUAN_THAM_QUYEN",
        re.compile(
            r"\b(?:Chủ\s+tịch\s+(?:Ủy\s+ban\s+nhân\s+dân|UBND)\s+(?:các\s+tỉnh,\s+thành\s+phố\s+trực\s+thuộc\s+trung\s+ương|cấp\s+tỉnh|cấp\s+huyện|cấp\s+xã|tỉnh,\s+thành\s+phố\s+trực\s+thuộc\s+trung\s+ương|quận,\s+thị\s+xã,\s+thành\s+phố\s+thuộc\s+tỉnh|huyện,\s+quận,\s+phường|huyện,\s+quận|quận,\s+thị\s+xã|phường|xã,\s+phường,\s+thị\s+trấn|cùng\s+cấp)"
            r"|(?:Ủy\s+ban\s+nhân\s+dân|UBND|Hội\s+đồng\s+nhân\s+dân)\s+(?:các\s+cấp|cấp\s+tỉnh|cấp\s+huyện|cấp\s+xã|tỉnh,\s+thành\s+phố\s+trực\s+thuộc\s+trung\s+ương|quận,\s+thị\s+xã,\s+thành\s+phố\s+thuộc\s+tỉnh|huyện,\s+quận,\s+phường|huyện,\s+quận|phường|xã,\s+phường,\s+thị\s+trấn|cùng\s+cấp)"
            r"|Hội\s+đồng\s+nhân\s+dân"
            r"|Thủ\s+tướng\s+Chính\s+phủ|Chính\s+phủ|Quốc\s+hội|Ủy\s+ban\s+Thường\s+vụ\s+Quốc\s+hội"
            r"|Ngân\s+hàng\s+Nhà\s+nước(?:\s+Việt\s+Nam|\s+chi\s+nhánh\s+tỉnh,\s*thành\s+phố(?:\s+trực\s+thuộc\s+Trung\s+ương)?)?|Thống\s+đốc\s+Ngân\s+hàng\s+Nhà\s+nước(?:\s+Việt\s+Nam)?"
            r"|Ủy\s+ban\s+Chứng\s+khoán\s+Nhà\s+nước|Kho\s+bạc\s+Nhà\s+nước|Tổng\s+Kiểm\s+toán\s+nhà\s+nước|Kiểm\s+toán\s+nhà\s+nước"
            r"|Bộ\s+trưởng\s+Bộ\s+(?:Tư\s+pháp|Lao\s+động\s*-\s*Thương\s+binh\s+và\s+Xã\s+hội|Tài\s+chính|Công\s+an|Quốc\s+phòng|Nội\s+vụ|Giao\s+thông\s+vận\s+tải|Công\s+Thương|Thương\s+mại|Xây\s+dựng|Y\s+tế|Giáo\s+dục\s+và\s+Đào\s+tạo|Nông\s+nghiệp\s+và\s+Phát\s+triển\s+nông\s+thôn|Tài\s+nguyên\s+và\s+Môi\s+trường|Thông\s+tin\s+và\s+Truyền\s+thông|Kế\s+hoạch\s+và\s+Đầu\s+tư|Khoa\s+học\s+và\s+Công\s+nghệ|Văn\s+hóa,\s*Thể\s+thao\s+và\s+Du\s+lịch|Ngoại\s+giao)"
            r"|Bộ\s+(?:Tư\s+pháp|Lao\s+động\s*-\s*Thương\s+binh\s+và\s+Xã\s+hội|Tài\s+chính|Công\s+an|Quốc\s+phòng|Nội\s+vụ|Giao\s+thông\s+vận\s+tải|Công\s+Thương|Thương\s+mại|Xây\s+dựng|Y\s+tế|Giáo\s+dục\s+và\s+Đào\s+tạo|Nông\s+nghiệp\s+và\s+Phát\s+triển\s+nông\s+thôn|Tài\s+nguyên\s+và\s+Môi\s+trường|Thông\s+tin\s+và\s+Truyền\s+thông|Kế\s+hoạch\s+và\s+Đầu\s+tư|Khoa\s+học\s+và\s+Công\s+nghệ|Văn\s+hóa,\s*Thể\s+thao\s+và\s+Du\s+lịch|Ngoại\s+giao)"
            r"|Tòa\s+án(?:\s+nhân\s+dân(?:\s+cấp\s+tỉnh|\s+cấp\s+huyện|\s+tối\s+cao)?)?|Viện\s+kiểm\s+sát(?:\s+nhân\s+dân(?:\s+cấp\s+tỉnh|\s+cấp\s+huyện|\s+tối\s+cao)?)?"
            r"|Cơ\s+quan\s+đại\s+diện\s+(?:nước\s+Cộng\s+hòa\s+xã\s+hội\s+chủ\s+nghĩa\s+)?Việt\s+Nam\s+ở\s+nước\s+ngoài"
            r"|Cơ\s+quan\s+(?:điều\s+tra|thi\s+hành\s+án\s+(?:dân\s+sự|hình\s+sự)|thuế|hải\s+quan|bảo\s+hiểm\s+xã\s+hội|đăng\s+ký\s+kinh\s+doanh|quản\s+lý\s+nhà\s+nước)"
            r"|Cảng\s+vụ\s+(?:đường\s+thủy\s+nội\s+địa(?:\s+khu\s+vực\s+[IVX]+(?:\s+và\s+khu\s+vực\s+[IVX]+)?)?|hàng\s+hải|hàng\s+không)"
            r"|Văn\s+phòng\s+(?:Trung\s+ương\s+Đảng|Chính\s+phủ|Quốc\s+hội|Chủ\s+tịch\s+nước)"
            r"|Ban\s+(?:Tổ\s+chức\s+Trung\s+ương(?:\s+Đảng)?|Chỉ\s+đạo\s+phòng,\s*chống\s+lụt,\s*bão\s+Trung\s+ương|Cơ\s+yếu\s+Chính\s+phủ|Dân\s+tộc|Tôn\s+giáo\s+Chính\s+phủ)"
            r"|Chủ\s+tịch\s+Ủy\s+ban\s+quốc\s+gia\s+Tìm\s+kiếm\s+Cứu\s+nạn|Ủy\s+ban\s+quốc\s+gia\s+Tìm\s+kiếm\s+Cứu\s+nạn"
            r"|Chủ\s+tịch\s+Hội\s+đồng\s+Thi\s+đua,\s*Khen\s+thưởng(?:\s+Bộ)?|Hội\s+đồng\s+Thi\s+đua,\s*Khen\s+thưởng(?:\s+Bộ|\s+Nhà\s+nước)?"
            r"|Chánh\s+Thanh\s+tra(?:,\s*giám\s+sát\s+ngân\s+hàng|\s+(?:Bộ|Sở|Ngân\s+hàng\s+Nhà\s+nước))|Thanh\s+tra,\s*giám\s+sát\s+ngân\s+hàng|Thanh\s+tra\s+(?:Chính\s+phủ|Bộ|Sở|Ngân\s+hàng\s+Nhà\s+nước|Chứng\s+khoán)"
            r"|Giám\s+đốc\s+Sở\s+(?:Tư\s+pháp|Nội\s+vụ|Tài\s+chính|Thương\s+mại(?:\s*-\s*Du\s+lịch)?|Công\s+Thương|Xây\s+dựng|Y\s+tế|Giáo\s+dục\s+và\s+Đào\s+tạo|Tài\s+nguyên\s+và\s+Môi\s+trường|Lao\s+động\s*-\s*Thương\s+binh\s+và\s+Xã\s+hội|Giao\s+thông\s+vận\s+tải|Kế\s+hoạch\s+và\s+Đầu\s+tư|Nông\s+nghiệp\s+và\s+Phát\s+triển\s+nông\s+thôn)"
            r"|Sở\s+(?:Tư\s+pháp|Nội\s+vụ|Tài\s+chính|Thương\s+mại(?:\s*-\s*Du\s+lịch)?|Công\s+Thương|Xây\s+dựng|Y\s+tế|Giáo\s+dục\s+và\s+Đào\s+tạo|Tài\s+nguyên\s+và\s+Môi\s+trường|Lao\s+động\s*-\s*Thương\s+binh\s+và\s+Xã\s+hội|Giao\s+thông\s+vận\s+tải|Kế\s+hoạch\s+và\s+Đầu\s+tư|Nông\s+nghiệp\s+và\s+Phát\s+triển\s+nông\s+thôn)"
            r"|Phòng\s+(?:Nội\s+vụ|Tư\s+pháp|Tài\s+chính\s*-\s*Kế\s+hoạch|Lao\s+động\s*-\s*Thương\s+binh\s+và\s+Xã\s+hội|Giáo\s+dục\s+và\s+Đào\s+tạo|Tài\s+nguyên\s+và\s+Môi\s+trường)"
            r"|cơ\s+quan\s+(?:quản\s+lý\s+nhà\s+nước\s+|nhà\s+nước\s+|chuyên\s+môn\s+)?có\s+thẩm\s+quyền|cấp\s+có\s+thẩm\s+quyền(?:\s+quản\s+lý\s+cán\s+bộ)?)\b",
            re.I,
        ),
    ),
    (
        "GIAY_TO_HO_SO",
        re.compile(
            r"\b(?:"
            # 1. Giấy phép chuyên biệt
            r"Giấy\s+phép\s+(?:lái\s+xe|kinh\s+doanh(?:\s+dịch\s+vụ|\s+vận\s+tải|\s+lữ\s+hành|\s+bất\s+động\s+sản)?|lao\s+động|xây\s+dựng|hoạt\s+động(?:\s+(?:in|điện\s+lực|khám\s+bệnh,\s*chữa\s+bệnh|ngân\s+hàng|báo\s+chí|viễn\s+thông|bưu\s+chính|dịch\s+vụ\s+việc\s+làm|cho\s+thuê\s+lại\s+lao\s+động))?|thành\s+lập(?:\s+và\s+hoạt\s+động)?|lập\s+văn\s+phòng(?:\s+đại\s+diện|\s+con\s+nuôi\s+nước\s+ngoài)?|xuất\s+khẩu(?:,\s*nhập\s+khẩu)?(?:\s+tiền\s+chất(?:\s+công\s+nghiệp)?)?|nhập\s+khẩu(?:\s+thiết\s+bị\s+in)?|hành\s+nghề(?:\s+luật\s+sư)?|sát\s+hạch|điều\s+chỉnh|khai\s+thác|môi\s+trường|cung\s+cấp\s+dịch\s+vụ)"
            # 2. Giấy chứng nhận chuyên biệt
            r"|Giấy\s+chứng\s+nhận(?:\s+(?:"
                r"đăng\s+ký\s+(?:doanh\s+nghiệp|kinh\s+doanh|đầu\s+tư|thuế|hoạt\s+động(?:\s+văn\s+phòng\s+đại\s+diện|\s+chi\s+nhánh)?|chào\s+bán(?:\s+cổ\s+phiếu|\s+trái\s+phiếu|\s+chứng\s+khoán(?:\s+ra\s+công\s+chúng)?)?|phát\s+hành(?:\s+cổ\s+phiếu|\s+trái\s+phiếu|\s+chứng\s+khoán)?|chứng\s+khoán|lập\s+quỹ|nhãn\s+hiệu|quyền\s+tác\s+giả|quyền\s+sử\s+dụng\s+đất|hợp\s+tác\s+xã|tổ\s+hợp\s+tác|hộ\s+kinh\s+doanh)"
                r"|quyền\s+sử\s+dụng\s+đất(?:,\s*quyền\s+sở\s+hữu\s+nhà\s+ở(?:\s+và\s+tài\s+sản\s+khác\s+gắn\s+liền\s+với\s+đất)?)?|quyền\s+sở\s+hữu\s+(?:nhà\s+ở|công\s+trình\s+xây\s+dựng)"
                r"|đủ\s+điều\s+kiện\s+(?:kinh\s+doanh(?:\s+dịch\s+vụ\s+kế\s+toán|\s+kiểm\s+toán|\s+chứng\s+khoán|\s+bất\s+động\s+sản|\s+thương\s+mại|\s+dược)?|về\s+an\s+ninh,\s*trật\s+tự|hoạt\s+động|sản\s+xuất)"
                r"|an\s+toàn\s+kỹ\s+thuật(?:\s+và\s+bảo\s+vệ\s+môi\s+trường(?:\s+phương\s+tiện\s+giao\s+thông\s+cơ\s+giới\s+đường\s+bộ)?)?"
                r"|giáo\s+viên(?:\s+dạy\s+thực\s+hành\s+lái\s+xe)?|người\s+bào\s+chữa"
                r"|hoạt\s+động\s+khoa\s+học\s+và\s+công\s+nghệ|doanh\s+nghiệp\s+nông\s+nghiệp\s+ứng\s+dụng\s+công\s+nghệ\s+cao"
                r"|đầu\s+tư|căn\s+cước|sức\s+khỏe|kiểm\s+định|xuất\s+xứ(?:\s+hàng\s+hóa)?|hợp\s+chuẩn|hợp\s+quy|bồi\s+dưỡng\s+nghiệp\s+vụ(?:\s+công\s+chứng)?|tốt\s+nghiệp"
            r"))?"
            # 3. Giấy đăng ký / Giấy xác nhận / Giấy đề nghị / Giấy tờ
            r"|Giấy\s+đăng\s+ký(?:\s+(?:hoạt\s+động(?:\s+của)?(?:\s+(?:văn\s+phòng\s+công\s+chứng|tổ\s+chức\s+hành\s+nghề\s+luật\s+sư|văn\s+phòng\s+luật\s+sư|công\s+ty\s+luật(?:\s+trách\s+nhiệm\s+hữu\s+hạn(?:\s+một\s+thành\s+viên|\s+hai\s+thành\s+viên\s+trở\s+lên)?|\s+hợp\s+danh)?|doanh\s+nghiệp|chi\s+nhánh|văn\s+phòng\s+đại\s+diện))?|hành\s+nghề(?:\s+luật\s+sư|\s+kiểm\s+toán|\s+quản\s+lý,\s*thanh\s+lý\s+tài\s+sản)?|doanh\s+nghiệp|kinh\s+doanh|đầu\s+tư|thuế|phương\s+tiện(?:\s+thủy(?:\s+nội\s+địa)?)?|xe(?:\s+mô\s+tô,\s*xe\s+gắn\s+máy|\s+ô\s+tô)?|tàu\s+biển|kết\s+hôn|khai\s+sinh|nhãn\s+hiệu|tập\s+sự(?:\s+hành\s+nghề(?:\s+công\s+chứng|\s+luật\s+sư)?)?))?"
            r"|Giấy\s+xác\s+nhận(?:\s+(?:đăng\s+ký\s+hoạt\s+động(?:\s+in)?|nội\s+dung\s+quảng\s+cáo(?:\s+thực\s+phẩm)?|nơi\s+công\s+tác|không\s+thuộc\s+diện\s+cấp\s+giấy\s+phép\s+lao\s+động|khai\s+báo\s+nhập\s+khẩu(?:\s+thiết\s+bị\s+in)?|công\s+bố\s+phù\s+hợp(?:\s+quy\s+định\s+an\s+toàn\s+thực\s+phẩm)?|tình\s+trạng\s+hôn\s+nhân|đã\s+nộp\s+lại\s+Giấy\s+đăng\s+ký(?:\s+hành\s+nghề(?:\s+luật\s+sư)?|\s+hoạt\s+động(?:\s+văn\s+phòng\s+luật\s+sư|\s+văn\s+phòng\s+công\s+chứng|\s+công\s+ty\s+luật)?)?|đã\s+rút\s+tên\s+khỏi\s+danh\s+sách\s+thành\s+viên|đã\s+chấm\s+dứt\s+(?:tư\s+cách\s+thành\s+viên|hợp\s+đồng\s+làm\s+việc)))?"
            r"|Giấy\s+đề\s+nghị(?:\s+(?:cấp(?:\s+lại|\s+đổi)?\s+(?:giấy\s+phép(?:\s+lao\s+động|\s+hoạt\s+động|\s+kinh\s+doanh)?|giấy\s+chứng\s+nhận|giấy\s+đăng\s+ký(?:\s+hoạt\s+động|\s+hành\s+nghề)?|chứng\s+chỉ\s+hành\s+nghề|thẻ(?:\s+công\s+chứng\s+viên|\s+luật\s+sư)?)|đăng\s+ký(?:\s+doanh\s+nghiệp|\s+hoạt\s+động|\s+hành\s+nghề)?|thay\s+đổi\s+nội\s+dung\s+Giấy\s+phép|gia\s+hạn(?:\s+giấy\s+phép)?|khoanh\s+nợ|xóa\s+nợ|bổ\s+nhiệm|miễn\s+nhiệm|thanh\s+toán|vay\s+vốn))?"
            r"|(?:bản\s+chính\s+|bản\s+sao\s+(?:có\s+chứng\s+thực\s+)?)?giấy\s+tờ\s+(?:tùy\s+thân|chứng\s+minh(?:\s+quyền\s+sở\s+hữu|\s+nhân\s+thân|\s+là\s+đã\s+nghỉ\s+hưu)?|có\s+giá)"
            r"|Giấy\s+(?:khai\s+sinh|khám\s+sức\s+khỏe|ra\s+viện|triệu\s+tập|ủy\s+quyền|giới\s+thiệu|báo\s+tử)"
            # 4. Hồ sơ chuyên biệt (Hồ sơ đề nghị..., Hồ sơ đăng ký..., Hồ sơ trình..., Hồ sơ...)
            r"|hồ\s+sơ\s+trình(?:\s+đề\s+nghị(?:\s+(?:bổ\s+nhiệm|miễn\s+nhiệm(?:,\s*cách\s+chức)?|cách\s+chức))?)?"
            r"|hồ\s+sơ\s+đề\s+nghị(?:\s+(?:"
                r"cấp(?:\s+lại|\s+đổi)?\s+(?:giấy\s+phép(?:\s+lao\s+động|\s+hoạt\s+động(?:\s+in)?|\s+thành\s+lập|\s+kinh\s+doanh|\s+xây\s+dựng)?|giấy\s+chứng\s+nhận(?:\s+đủ\s+điều\s+kiện)?|giấy\s+đăng\s+ký(?:\s+hoạt\s+động|\s+hành\s+nghề)?|chứng\s+chỉ\s+hành\s+nghề(?:\s+luật\s+sư|\s+quản\s+tài\s+viên|\s+công\s+chứng|\s+đấu\s+giá)?|thẻ(?:\s+công\s+chứng\s+viên|\s+luật\s+sư)?)"
                r"|gia\s+hạn\s+(?:giấy\s+phép(?:\s+lao\s+động|\s+hoạt\s+động)?|giấy\s+chứng\s+nhận|giấy\s+đăng\s+ký)"
                r"|bổ\s+nhiệm(?:\s+lại)?(?:\s+công\s+chứng\s+viên|\s+giám\s+định\s+viên|\s+đấu\s+giá\s+viên)?"
                r"|miễn\s+nhiệm(?:\s+công\s+chứng\s+viên|\s+giám\s+định\s+viên|\s+đấu\s+giá\s+viên)?"
                r"|thành\s+lập(?:\s+văn\s+phòng\s+công\s+chứng|\s+doanh\s+nghiệp|\s+quỹ|\s+chi\s+nhánh)?"
                r"|mở\s+chi\s+nhánh(?:,\s*văn\s+phòng\s+đại\s+diện)?"
                r"|chuyển\s+đổi(?:\s+loại\s+hình\s+văn\s+phòng\s+công\s+chứng)?"
                r"|đăng\s+ký(?:\s+hành\s+nghề(?:\s+quản\s+lý,\s*thanh\s+lý\s+tài\s+sản)?)?"
                r"|phê\s+duyệt(?:\s+giá\s+khởi\s+điểm|\s+phương\s+án)?"
                r"|công\s+nhận|xét\s+tặng(?:\s+Kỷ\s+niệm\s+chương|\s+danh\s+hiệu)?"
                r"|áp\s+dụng\s+biện\s+pháp(?:\s+giáo\s+dục\s+tại\s+xã(?:,\s*phường,\s*thị\s+trấn)?|\s+đưa\s+vào\s+cơ\s+sở\s+cai\s+nghiện)?"
                r"|điều\s+chuyển\s+tài\s+sản|chuyển\s+giao\s+tài\s+sản|thu\s+hồi\s+tài\s+sản|thanh\s+lý\s+tài\s+sản|giao\s+tài\s+sản(?:\s+kết\s+cấu\s+hạ\s+tầng(?:\s+đường\s+bộ)?)?"
                r"|khoanh\s+nợ|xóa\s+nợ|hưởng\s+trợ\s+cấp"
            r"))?"
            r"|hồ\s+sơ\s+đăng\s+ký(?:\s+(?:"
                r"chào\s+bán(?:,\s*phát\s+hành)?(?:\s+riêng\s+lẻ|\s+cổ\s+phiếu(?:\s+riêng\s+lẻ)?|\s+trái\s+phiếu(?:\s+riêng\s+lẻ)?|\s+chứng\s+khoán(?:\s+ra\s+công\s+chúng)?)?"
                r"|phát\s+hành(?:\s+riêng\s+lẻ|\s+cổ\s+phiếu|\s+trái\s+phiếu|\s+chứng\s+khoán)?"
                r"|hoạt\s+động(?:\s+của)?(?:\s+văn\s+phòng\s+công\s+chứng|\s+văn\s+phòng\s+luật\s+sư|\s+doanh\s+nghiệp|\s+chi\s+nhánh|\s+văn\s+phòng\s+đại\s+diện|\s+cơ\s+sở\s+in)?"
                r"|doanh\s+nghiệp|kinh\s+doanh|đầu\s+tư|thuế"
                r"|hành\s+nghề(?:\s+luật\s+sư|\s+kiểm\s+toán|\s+công\s+chứng)?"
                r"|tập\s+sự(?:\s+hành\s+nghề(?:\s+luật\s+sư|\s+công\s+chứng)?)?"
                r"|dự\s+tuyển(?:\s+lao\s+động)?|danh\s+sách\s+công\s+chứng\s+viên"
                r"|chất\s+lượng\s+dịch\s+vụ(?:\s+vận\s+tải)?|đất\s+đai|biến\s+động\s+đất\s+đai|thế\s+chấp|lập\s+quỹ|giao\s+dịch|niêm\s+yết"
            r"))?"
            r"|hồ\s+sơ\s+(?:kê\s+khai(?:\s+thuế|\s+tài\s+sản)?|khai\s+thuế|hoàn\s+thuế|hải\s+quan|chào\s+bán(?:,\s*phát\s+hành)?(?:\s+trái\s+phiếu(?:\s+riêng\s+lẻ)?|\s+cổ\s+phiếu(?:\s+riêng\s+lẻ)?|\s+chứng\s+khoán|\s+riêng\s+lẻ)?|phát\s+hành(?:\s+trái\s+phiếu|\s+cổ\s+phiếu|\s+chứng\s+khoán|\s+riêng\s+lẻ)?|mời\s+thầu|dự\s+thầu|yêu\s+cầu|đề\s+xuất|bổ\s+nhiệm(?:\s+lại)?(?:\s+công\s+chứng\s+viên)?|miễn\s+nhiệm(?:\s+công\s+chứng\s+viên)?|thanh\s+toán|quyết\s+toán|thiết\s+kế(?:\s+kỹ\s+thuật|\s+bản\s+vẽ\s+thi\s+công)?|hoàn\s+công|xét\s+tặng(?:\s+Kỷ\s+niệm\s+chương)?|hành\s+nghề|công\s+chứng|kiểm\s+toán|xử\s+phạt(?:\s+vi\s+phạm\s+hành\s+chính)?|vụ\s+án|bệnh\s+án|thi\s+hành\s+án|vay\s+vốn|tín\s+dụng|thẩm\s+định|đấu\s+giá)"
            # 5. Báo cáo / Bản / Hợp đồng / Chứng chỉ / Thẻ / Quyết định / Biên bản / Tờ khai / Phương án / Đơn / Sổ / Văn bản
            r"|Báo\s+cáo\s+(?:tài\s+chính(?:\s+năm|\s+hàng\s+năm|\s+bán\s+niên|\s+quý|\s+hợp\s+nhất|\s+đã\s+được\s+kiểm\s+toán)?|kiểm\s+toán(?:\s+nội\s+bộ|\s+năm|\s+độc\s+lập)?|kết\s+quả\s+(?:đợt\s+chào\s+bán|đợt\s+phát\s+hành|chào\s+bán|phát\s+hành|kiểm\s+toán|thực\s+hiện(?:\s+giao\s+dịch)?|hoạt\s+động|kinh\s+doanh|sử\s+dụng\s+vốn)|sử\s+dụng\s+vốn|đánh\s+giá(?:\s+tác\s+động\s+môi\s+trường)?|thường\s+niên|bất\s+thường|tình\s+hình\s+(?:quản\s+trị\s+công\s+ty|tài\s+chính|hoạt\s+động|sử\s+dụng\s+lao\s+động)|tỷ\s+lệ\s+an\s+toàn\s+tài\s+chính|nghiên\s+cứu\s+khả\s+thi|kinh\s+tế\s*-\s*kỹ\s+thuật|giải\s+trình|giao\s+dịch(?:\s+có\s+giá\s+trị\s+lớn|\s+đáng\s+ngờ)?|hành\s+vi\s+nghi\s+ngờ|thành\s+tích)|ý\s+kiến\s+kiểm\s+toán"
            r"|Bản\s+(?:cáo\s+bạch(?:\s+tóm\s+tắt)?|công\s+bố\s+thông\s+tin|án(?:\s+hình\s+sự|\s+dân\s+sự|\s+hành\s+chính)?|thuyết\s+minh(?:\s+báo\s+cáo\s+tài\s+chính)?|kê\s+khai\s+tài\s+sản|cam\s+kết|kiểm\s+điểm|sao\s+(?:có\s+chứng\s+thực|văn\s+bằng,\s*chứng\s+chỉ))"
            r"|hợp\s+đồng\s+(?:lao\s+động(?:\s+không\s+xác\s+định\s+thời\s+hạn|\s+xác\s+định\s+thời\s+hạn)?|làm\s+việc|tuyển\s+dụng|kinh\s+tế|dân\s+sự|thương\s+mại|công\s+chứng|thử\s+việc|đào\s+tạo(?:\s+nghề)?|cho\s+thuê\s+lại(?:\s+lao\s+động)?|thuê(?:\s+nhà|\s+đất|\s+tài\s+sản)?|tín\s+dụng|thế\s+chấp(?:\s+tài\s+sản|\s+quyền\s+sử\s+dụng\s+đất)?|cầm\s+cố(?:\s+tài\s+sản)?|bảo\s+lãnh|bảo\s+hiểm|ủy\s+thác|đại\s+lý|dịch\s+vụ(?:\s+pháp\s+lý|\s+kiểm\s+toán)?|kiểm\s+toán|liên\s+kết|tiêu\s+thụ|mua\s+bán(?:\s+hàng\s+hóa|\s+điện|\s+nhà\s+ở|\s+tài\s+sản(?:\s+đấu\s+giá)?)?|chuyển\s+nhượng(?:\s+quyền\s+sử\s+dụng\s+đất|\s+cổ\s+phần|\s+vốn)?|giao\s+khoán|hợp\s+tác(?:\s+kinh\s+doanh)?|giao\s+dịch)|hợp\s+đồng,\s*giao\s+dịch"
            r"|chứng\s+chỉ\s+hành\s+nghề(?:\s+(?:luật\s+sư|công\s+chứng|đấu\s+giá|quản\s+tài\s+viên|kế\s+toán|kiểm\s+toán|chứng\s+khoán|khám\s+bệnh,\s*chữa\s+bệnh|y|dược|hoạt\s+động\s+xây\s+dựng|dịch\s+vụ\s+đại\s+diện\s+sở\s+hữu\s+công\s+nghiệp))?"
            r"|chứng\s+chỉ\s+(?:tiền\s+gửi|bồi\s+dưỡng(?:\s+nghiệp\s+vụ(?:\s+công\s+chứng)?)?|đào\s+tạo|kiểm\s+định|chuyên\s+môn)|văn\s+bằng,\s*chứng\s+chỉ|bằng\s+tốt\s+nghiệp(?:\s+đại\s+học|\s+trung\s+học)?"
            r"|Thẻ\s+(?:công\s+chứng\s+viên|luật\s+sư|đấu\s+giá\s+viên|giám\s+định\s+viên(?:\s+tư\s+pháp)?|thẩm\s+định\s+viên(?:\s+về\s+giá)?|kiểm\s+tra\s+viên|bảo\s+hiểm\s+y\s+tế|căn\s+cước(?:\s+công\s+dân)?|thành\s+viên|hội\s+viên|đầu\s+cuối)|(?:Giấy\s+)?Chứng\s+minh\s+nhân\s+dân|Hộ\s+chiếu(?:\s+thuyền\s+viên)?"
            r"|quyết\s+định\s+(?:xử\s+phạt(?:\s+vi\s+phạm\s+hành\s+chính)?|truy\s+nã|bổ\s+nhiệm(?:\s+lại)?(?:\s+công\s+chứng\s+viên)?|miễn\s+nhiệm(?:\s+công\s+chứng\s+viên)?|tuyển\s+dụng|thu\s+hồi(?:\s+đất|\s+Giấy\s+phép(?:\s+hoạt\s+động|\s+thành\s+lập|\s+kinh\s+doanh)?|\s+Giấy\s+chứng\s+nhận(?:\s+đăng\s+ký)?|\s+Giấy\s+đăng\s+ký(?:\s+hoạt\s+động(?:\s+của\s+Văn\s+phòng\s+công\s+chứng)?)?)?|cưỡng\s+chế(?:\s+thi\s+hành)?|đình\s+chỉ(?:\s+thi\s+hành\s+án|\s+giải\s+quyết)?|tạm\s+đình\s+chỉ|áp\s+dụng\s+biện\s+pháp|khởi\s+tố(?:\s+vụ\s+án|\s+bị\s+can)?|thi\s+hành\s+án|công\s+nhận|phê\s+duyệt|giao\s+tài\s+sản|cho\s+phép\s+thành\s+lập(?:\s+Văn\s+phòng\s+công\s+chứng)?|thành\s+lập(?:\s+Phòng\s+công\s+chứng|\s+cơ\s+sở\s+in)?|giải\s+thể|chuyển\s+đổi)"
            r"|biên\s+bản\s+(?:vi\s+phạm(?:\s+hành\s+chính)?|kiểm\s+tra|thanh\s+tra|nghiệm\s+thu|bàn\s+giao|tạm\s+giữ|thu\s+giữ|họp(?:\s+Đại\s+hội\s+đồng\s+cổ\s+đông|\s+Hội\s+đồng\s+quản\s+trị|\s+Hội\s+đồng\s+thành\s+viên)?|thỏa\s+thuận|xác\s+nhận|kiểm\s+phiếu|đối\s+chiếu)"
            r"|tờ\s+khai\s+(?:đăng\s+ký(?:\s+thay\s+đổi\s+thông\s+tin|\s+hoạt\s+động(?:\s+cơ\s+sở\s+in)?)?|hải\s+quan(?:\s+hàng\s+hóa\s+xuất\s+khẩu,\s*nhập\s+khẩu)?|thuế(?:\s+giá\s+trị\s+gia\s+tăng|\s+thu\s+nhập)?|đề\s+nghị\s+cấp(?:\s+lại)?(?:\s+hộ\s+chiếu\s+thuyền\s+viên|\s+sổ\s+thuyền\s+viên)?|tham\s+gia\s+bảo\s+hiểm)"
            r"|phương\s+án\s+(?:bồi\s+thường(?:,\s*hỗ\s+trợ(?:,\s*tái\s+định\s+cư)?)?|sản\s+xuất(?:\s+kinh\s+doanh)?|tài\s+chính|trả\s+nợ|sử\s+dụng\s+(?:vốn|lao\s+động|đất)|chào\s+bán|phát\s+hành|khắc\s+phục|xử\s+lý(?:\s+tài\s+sản)?|phá\s+dỡ|tổ\s+chức|cơ\s+cấu\s+lại)"
            r"|đơn\s+(?:đề\s+nghị(?:\s+(?:cấp(?:\s+lại|\s+đổi)?(?:\s+Giấy\s+phép|\s+Giấy\s+chứng\s+nhận|\s+Giấy\s+đăng\s+ký|\s+Thẻ\s+công\s+chứng\s+viên|\s+chứng\s+chỉ\s+hành\s+nghề)?|bổ\s+nhiệm(?:\s+lại)?(?:\s+công\s+chứng\s+viên)?|miễn\s+nhiệm(?:\s+công\s+chứng\s+viên)?|thành\s+lập(?:\s+Văn\s+phòng\s+công\s+chứng)?|gia\s+hạn))?|đăng\s+ký(?:\s+hoạt\s+động(?:\s+Văn\s+phòng\s+công\s+chứng)?|\s+hành\s+nghề|\s+tập\s+sự)?|khiếu\s+nại|tố\s+cáo|khởi\s+kiện|kháng\s+cáo|xin\s+(?:cấp|nghỉ|gia\s+nhập)|yêu\s+cầu)"
            r"|sổ\s+(?:bảo\s+hiểm\s+xã\s+hội|đăng\s+ký\s+(?:cổ\s+đông|thành\s+viên|chủ\s+sở\s+hữu)|kế\s+toán|hộ\s+khẩu|tạm\s+trú|thuyền\s+viên|nhật\s+ký|theo\s+dõi|quản\s+lý)"
            r"|văn\s+bản\s+(?:chấp\s+thuận|xác\s+nhận|đề\s+nghị|thông\s+báo(?:\s+đề\s+nghị)?|giải\s+trình|ủy\s+quyền|trả\s+lời|hướng\s+dẫn|thỏa\s+thuận)"
            r"|thông\s+báo\s+(?:kết\s+luận\s+)?bằng\s+văn\s+bản|phiếu\s+(?:lý\s+lịch\s+tư\s+pháp(?:\s+số\s+[12])?|lấy\s+ý\s+kiến|biểu\s+quyết|thu|chi)|hóa\s+đơn(?:,\s*chứng\s+từ)?|chứng\s+từ\s+(?:chi\s+tiêu|quyết\s+toán|kế\s+toán)"
            r"|Điều\s+lệ\s+(?:của\s+tổ\s+chức\s+xã\s+hội\s*(?:-|\s+)?nghề\s+nghiệp(?:\s+của\s+công\s+chứng\s+viên)?|công\s+ty|tổ\s+chức\s+tín\s+dụng|quỹ(?:\s+tín\s+dụng\s+nhân\s+dân)?|hợp\s+tác\s+xã)"
            r"|Quy\s+chế\s+(?:kiểm\s+soát\s+chất\s+lượng\s+kiểm\s+toán|thông\s+tin\s+cảnh\s+báo,\s*dự\s+báo\s+thiên\s+tai\s+trên\s+biển|xét\s+tặng\s+Kỷ\s+niệm\s+chương(?:\s+[“\"']Vì\s+sự\s+nghiệp\s+thương\s+mại[”\"'])?|nội\s+bộ(?:\s+về\s+quản\s+trị\s+công\s+ty)?|tổ\s+chức\s+và\s+hoạt\s+động|hoạt\s+động|quản\s+lý)"
            r"|Đề\s+án\s+(?:tổ\s+chức\s+thông\s+tin\s+phục\s+vụ\s+công\s+tác\s+phòng,\s*chống\s+thiên\s+tai\s+trên\s+biển|thành\s+lập(?:\s+Văn\s+phòng\s+công\s+chứng|\s+Phòng\s+công\s+chứng)?|cổ\s+phần\s+hóa|cơ\s+cấu\s+lại)"
            r"|Kế\s+hoạch\s+thực\s+hiện\s+Nghị\s+quyết(?:\s+số\s+\d+/\d{4}/[A-ZĐ0-9-]+)?"
            r"|nội\s+quy\s+(?:lao\s+động|cơ\s+quan|cơ\s+sở)|thỏa\s+ước\s+lao\s+động\s+tập\s+thể|Kỷ\s+niệm\s+chương(?:\s+[“\"']Vì\s+sự\s+nghiệp\s+thương\s+mại[”\"'])?"
            r")(?=\b|\s|[.,;:!?)]|$)",
            re.I,
        ),
    ),
    (
        "TO_CHUC_DOANH_NGHIEP",
        re.compile(
            r"\b(?:"
            # 1. Doanh nghiệp chuyên biệt
            r"(?<!trái phiếu )(?<!đăng ký )(?<!thuế thu nhập )(?<!quản trị )(?<!tài chính )doanh\s+nghiệp(?:\s+(?:"
                r"nhà\s+nước|tư\s+nhân|có\s+vốn\s+đầu\s+tư\s+nước\s+ngoài|nhỏ\s+và\s+vừa|xã\s+hội|dự\s+án"
                r"|bảo\s+hiểm|tái\s+bảo\s+hiểm|môi\s+giới\s+bảo\s+hiểm"
                r"|kinh\s+doanh\s+(?:bảo\s+hiểm|kết\s+cấu\s+hạ\s+tầng|bất\s+động\s+sản|chứng\s+khoán|dịch\s+vụ\s+(?:kế\s+toán|kiểm\s+toán|thẩm\s+định\s+giá|viễn\s+thông|lữ\s+hành|vận\s+tải|đấu\s+giá))"
                r"|kiểm\s+toán|thẩm\s+định\s+giá|quản\s+lý(?:,\s*thanh\s+lý)?\s+tài\s+sản(?:\s+đường\s+sắt)?"
                r"|cho\s+thuê\s+lại\s+lao\s+động|sử\s+dụng\s+nhiều\s+lao\s+động|nông\s+nghiệp\s+ứng\s+dụng\s+công\s+nghệ\s+cao|công\s+nghiệp\s+quốc\s+phòng"
                r"|thành\s+viên(?:\s+hạch\s+toán\s+độc\s+lập)?|khai\s+khoáng|phát\s+hành|viễn\s+thông|bưu\s+chính|vận\s+tải|chế\s+xuất|xuất\s+khẩu|nhập\s+khẩu|sản\s+xuất,\s*kinh\s+doanh|cổ\s+phần\s+hóa|phá\s+sản"
            r"))?"
            # 2. Tổng công ty & Tập đoàn
            r"|Tổng\s+công\s+ty\s+lưu\s+ký\s+và\s+bù\s+trừ\s+chứng\s+khoán\s+Việt\s+Nam(?:\s+và\s+công\s+ty\s+con)?"
            r"|Tổng\s+công\s+ty\s+(?:Nhà\s+nước|Đường\s+sắt\s+Việt\s+Nam|Đầu\s+tư\s+và\s+Kinh\s+doanh\s+vốn\s+nhà\s+nước|Hàng\s+hải\s+Việt\s+Nam|Hàng\s+không\s+Việt\s+Nam|Điện\s+lực\s+Việt\s+Nam|Bưu\s+điện\s+Việt\s+Nam)"
            r"|Tập\s+đoàn\s+(?:Công\s+nghiệp\s*-\s*Viễn\s+thông\s+Quân\s+đội|Điện\s+lực\s+Việt\s+Nam|Dầu\s+khí\s+Việt\s+Nam|Bưu\s+chính\s+Viễn\s+thông\s+Việt\s+Nam|Than\s*-\s*Khoáng\s+sản\s+Việt\s+Nam|kinh\s+tế|xuyên\s+quốc\s+gia)"
            # 3. Công ty chuyên biệt
            r"|công\s+ty\s+(?:"
                r"trách\s+nhiệm\s+hữu\s+hạn(?:\s+một\s+thành\s+viên|\s+hai\s+thành\s+viên\s+trở\s+lên)?"
                r"|TNHH(?:\s+một\s+thành\s+viên|\s+hai\s+thành\s+viên\s+trở\s+lên)?"
                r"|cổ\s+phần(?:\s+chứng\s+khoán)?|hợp\s+danh|đại\s+chúng|niêm\s+yết|chứng\s+khoán|nhà\s+nước|lớn"
                r"|quản\s+lý\s+quỹ(?:\s+đầu\s+tư\s+chứng\s+khoán)?|đầu\s+tư\s+chứng\s+khoán"
                r"|tài\s+chính|cho\s+thuê\s+tài\s+chính|bảo\s+hiểm|tái\s+bảo\s+hiểm|môi\s+giới\s+bảo\s+hiểm"
                r"|kiểm\s+toán|thẩm\s+định\s+giá|luật(?:\s+trách\s+nhiệm\s+hữu\s+hạn(?:\s+một\s+thành\s+viên|\s+hai\s+thành\s+viên\s+trở\s+lên)?|\s+hợp\s+danh)?"
                r"|đấu\s+giá\s+hợp\s+danh|quản\s+lý\s+tài\s+sản|xổ\s+số\s+kiến\s+thiết|bảo\s+đảm\s+an\s+toàn\s+hàng\s+hải"
                r"|sản\s+xuất,\s*lắp\s+ráp(?:\s+xe\s+ô\s+tô)?|mẹ|con|liên\s+kết"
            r")"
            # 4. Tổ chức chuyên biệt
            r"|tổ\s+chức\s+(?:"
                r"tín\s+dụng(?:\s+phi\s+ngân\s+hàng)?|tài\s+chính(?:\s+vi\s+mô|\s+nhà\s+nước)?|kinh\s+tế"
                r"|kinh\s+doanh\s+(?:chứng\s+khoán|bảo\s+hiểm|dịch\s+vụ\s+(?:kế\s+toán|kiểm\s+toán|đại\s+diện\s+sở\s+hữu\s+công\s+nghiệp))"
                r"|phát\s+hành|chào\s+bán(?:,\s*phát\s+hành)?|niêm\s+yết|đăng\s+ký\s+giao\s+dịch|bảo\s+lãnh\s+phát\s+hành"
                r"|tư\s+vấn(?:\s+hồ\s+sơ\s+chào\s+bán|\s+phát\s+hành)?|kiểm\s+toán(?:\s+được\s+chấp\s+thuận)?"
                r"|thẩm\s+định\s+giá|định\s+giá|xếp\s+hạng\s+tín\s+nhiệm|đấu\s+giá\s+tài\s+sản"
                r"|hành\s+nghề\s+(?:công\s+chứng|luật\s+sư|đấu\s+giá)|giám\s+định\s+tư\s+pháp|trọng\s+tài(?:\s+thương\s+mại)?"
                r"|đại\s+diện\s+(?:người\s+lao\s+động|tập\s+thể\s+lao\s+động|sở\s+hữu\s+công\s+nghiệp)|công\s+đoàn"
                r"|chính\s+trị\s*-\s*xã\s+hội|xã\s+hội(?:\s*-\s*nghề\s+nghiệp|\s+nghề\s+nghiệp)?(?:\s+của\s+công\s+chứng\s+viên)?|khoa\s+học\s+và\s+công\s+nghệ"
                r"|giáo\s+dục(?:\s+nghề\s+nghiệp)?|y\s+tế|bảo\s+hiểm|đầu\s+mối|lưu\s+ký\s+chứng\s+khoán|bù\s+trừ|con\s+nuôi\s+nước\s+ngoài"
            r")"
            # 5. Ngân hàng / Chi nhánh / Văn phòng / Quỹ / Trung tâm / Cơ sở / Đơn vị / Hợp tác xã / Hội đồng / Đoàn
            r"|(?:chi\s+nhánh\s+)?ngân\s+hàng\s+(?:thương\s+mại(?:\s+cổ\s+phần|\s+nhà\s+nước)?|chính\s+sách\s+xã\s+hội|phát\s+triển(?:\s+Việt\s+Nam)?|hợp\s+tác\s+xã(?:\s+Việt\s+Nam)?|nước\s+ngoài)"
            r"|Văn\s+phòng\s+(?:công\s+chứng|luật\s+sư|thừa\s+phát\s+lại|đăng\s+ký\s+(?:đất\s+đai|quyền\s+sử\s+dụng\s+đất)|con\s+nuôi\s+nước\s+ngoài|đại\s+diện(?:\s+của\s+(?:doanh\s+nghiệp|thương\s+nhân|tổ\s+chức)\s+nước\s+ngoài)?)|Phòng\s+công\s+chứng"
            r"|Ban\s+chủ\s+nhiệm\s+Đoàn\s+luật\s+sư|Đoàn\s+luật\s+sư(?:\s+tỉnh,\s*thành\s+phố\s+trực\s+thuộc\s+trung\s+ương)?|Liên\s+đoàn\s+luật\s+sư\s+Việt\s+Nam"
            r"|quỹ\s+(?:bảo\s+đảm\s+an\s+toàn\s+hệ\s+thống(?:\s+quỹ\s+tín\s+dụng\s+nhân\s+dân)?|bảo\s+toàn|tín\s+dụng\s+nhân\s+dân(?:\s+thành\s+viên)?|đầu\s+tư\s+(?:chứng\s+khoán|đại\s+chúng|phát\s+triển)|đại\s+chúng|thành\s+viên|bảo\s+hiểm\s+(?:xã\s+hội|y\s+tế|thất\s+nghiệp)|tài\s+chính(?:\s+nhà\s+nước\s+ngoài\s+ngân\s+sách)?|phát\s+triển\s+khoa\s+học\s+và\s+công\s+nghệ|bảo\s+vệ\s+môi\s+trường)"
            r"|Trung\s+tâm\s+(?:sát\s+hạch\s+lái\s+xe|tư\s+vấn\s+pháp\s+luật|trợ\s+giúp\s+pháp\s+lý(?:\s+nhà\s+nước)?|dịch\s+vụ\s+(?:việc\s+làm|đấu\s+giá\s+tài\s+sản|hậu\s+cần\s+nghề\s+cá)|đăng\s+kiểm|lưu\s+ký\s+chứng\s+khoán(?:\s+Việt\s+Nam)?|trọng\s+tài)"
            r"|cơ\s+sở\s+(?:sản\s+xuất(?:,\s*kinh\s+doanh|\s+kinh\s+doanh)?|kinh\s+doanh|in|khám\s+bệnh,\s*chữa\s+bệnh|y\s+tế|giáo\s+dục(?:\s+nghề\s+nghiệp|\s+đại\s+học)?|đào\s+tạo(?:\s+lái\s+xe(?:\s+ô\s+tô)?)?|dạy\s+nghề|giam\s+giữ|cai\s+nghiện(?:\s+bắt\s+buộc)?|công\s+nghiệp\s+quốc\s+phòng(?:\s+nòng\s+cốt)?|kinh\s+tế|chăn\s+nuôi)"
            r"|đơn\s+vị\s+(?:sự\s+nghiệp(?:\s+công\s+lập)?|quản\s+lý\s+tài\s+sản|được\s+kiểm\s+toán|kiểm\s+toán|kinh\s+doanh\s+vận\s+tải|đăng\s+kiểm|sản\s+xuất\s+điện|dự\s+toán|sử\s+dụng\s+ngân\s+sách|vũ\s+trang\s+nhân\s+dân)"
            r"|liên\s+hiệp\s+hợp\s+tác\s+xã|(?<!ngân hàng )(?<!Ngân hàng )hợp\s+tác\s+xã(?:\s+kinh\s+doanh\s+vận\s+tải)?|tổ\s+hợp\s+tác|hộ\s+(?:gia\s+đình|kinh\s+doanh|nghèo|cận\s+nghèo)"
            r"|Sở\s+giao\s+dịch\s+chứng\s+khoán(?:\s+Việt\s+Nam(?:\s+và\s+công\s+ty\s+con)?)?|Đại\s+hội\s+đồng\s+cổ\s+đông|Hội\s+đồng\s+quản\s+trị|Hội\s+đồng\s+thành\s+viên|Hội\s+đồng\s+thẩm\s+định\s+giá|Ban\s+kiểm\s+soát|Ủy\s+ban\s+kiểm\s+toán"
            r"|thành\s+viên\s+(?:lưu\s+ký|bù\s+trừ|giao\s+dịch|lập\s+quỹ)"
            r"|pháp\s+nhân\s+thương\s+mại(?:\s+phạm\s+tội)?|lực\s+lượng\s+vũ\s+trang\s+nhân\s+dân"
            r")\b",
            re.I,
        ),
    ),
    (
        "CHU_THE_CA_NHAN",
        re.compile(
            r"\b(?:người\s+sử\s+dụng\s+lao\s+động"
            r"|người\s+lao\s+động(?:\s+nước\s+ngoài|\s+chưa\s+thành\s+niên|\s+cao\s+tuổi|\s+khuyết\s+tật|\s+nữ)?"
            r"|người\s+điều\s+khiển\s+(?:xe(?:\s+mô\s+tô,\s*xe\s+gắn\s+máy|\s+ô\s+tô)?|phương\s+tiện(?:\s+giao\s+thông)?|tàu\s+biển)"
            r"|người\s+phạm\s+tội(?:\s+ít\s+nghiêm\s+trọng|\s+đặc\s+biệt\s+nghiêm\s+trọng)?"
            r"|người\s+bị\s+(?:kết\s+án|tạm\s+giữ,\s*tạm\s+giam|phạt\s+cải\s+tạo\s+không\s+giam\s+giữ|xử\s+phạt|buộc\s+thôi\s+việc|tước\s+quyền\s+sử\s+dụng)"
            r"|người\s+chấp\s+hành\s+án|người\s+nước\s+ngoài(?:\s+bị\s+kết\s+án|\s+làm\s+việc\s+tại\s+Việt\s+Nam)?"
            r"|người\s+dưới\s+18\s+tuổi|người\s+được\s+bổ\s+nhiệm|người\s+học\s+nghề|người\s+tập\s+nghề|người\s+tập\s+sự(?:\s+hành\s+nghề\s+công\s+chứng)?"
            r"|người\s+chỉ\s+huy|người\s+đại\s+diện(?:\s+theo\s+pháp\s+luật|\s+theo\s+ủy\s+quyền|\s+của\s+pháp\s+nhân)?|người\s+phụ\s+trách\s+quản\s+trị\s+công\s+ty|người\s+nội\s+bộ|người\s+có\s+liên\s+quan|người\s+hành\s+nghề(?:\s+chứng\s+khoán|\s+khám\s+bệnh,\s*chữa\s+bệnh)?"
            r"|chủ\s+trang\s+trại|chủ\s+đầu\s+tư|khách\s+hàng(?:\s+vay\s+vốn)?"
            r"|nhà\s+đầu\s+tư(?:\s+chứng\s+khoán\s+chuyên\s+nghiệp|\s+nước\s+ngoài|\s+cá\s+nhân)?"
            r"|Chủ\s+tịch\s+Hội\s+đồng\s+quản\s+trị|Chủ\s+tịch\s+Hội\s+đồng\s+thành\s+viên|thành\s+viên\s+Hội\s+đồng\s+quản\s+trị(?:\s+độc\s+lập|\s+không\s+điều\s+hành)?|thành\s+viên\s+Hội\s+đồng\s+thành\s+viên|Trưởng\s+Ban\s+kiểm\s+soát|Kiểm\s+soát\s+viên|Chủ\s+tịch\s+Ủy\s+ban\s+kiểm\s+toán|Tổng\s+Giám\s+đốc|Phó\s+Tổng\s+Giám\s+đốc|Giám\s+đốc|Phó\s+Giám\s+đốc|Chủ\s+tịch\s+công\s+ty|chủ\s+sở\s+hữu\s+công\s+ty|(?<!Đại hội đồng )cổ\s+đông(?:\s+lớn)?"
            r"|công\s+chứng\s+viên(?:\s+hợp\s+danh)?|(?<!Đoàn )(?<!Văn phòng )luật\s+sư|đấu\s+giá\s+viên|thừa\s+phát\s+lại|giám\s+định\s+viên(?:\s+tư\s+pháp)?|quản\s+tài\s+viên|trọng\s+tài\s+viên|kiểm\s+toán\s+viên(?:\s+nhà\s+nước)?|kế\s+toán\s+trưởng|thẩm\s+định\s+viên\s+về\s+giá"
            r"|cán\s+bộ,\s+công\s+chức,\s+viên\s+chức|cán\s+bộ,\s+công\s+chức"
            r"|cán\s+bộ(?:\s+biệt\s+phái)?|công\s+chức|viên\s+chức"
            r"|phụ\s+nữ\s+có\s+thai)\b",
            re.I,
        ),
    ),
    (
        "TAI_SAN_VAT_CHAT",
        re.compile(
            r"\b(?:tiền\s+lương|tiền\s+thưởng|trợ\s+cấp(?:\s+thôi\s+việc|\s+mất\s+việc\s+làm)?|thu\s+nhập|số\s+lợi\s+bất\s+hợp\s+pháp"
            r"|tài\s+sản(?:\s+bảo\s+đảm|\s+nhà\s+nước|\s+công|\s+của\s+người\s+khác|\s+ký\s+quỹ|\s+kết\s+cấu\s+hạ\s+tầng(?:\s+đường\s+bộ)?)?"
            r"|trái\s+phiếu(?:\s+doanh\s+nghiệp)?(?:\s+riêng\s+lẻ|\s+chuyển\s+đổi(?:\s+riêng\s+lẻ)?|\s+kèm\s+chứng\s+quyền(?:\s+riêng\s+lẻ)?)?"
            r"|cổ\s+phiếu(?:\s+riêng\s+lẻ)?|chứng\s+khoán(?:\s+phái\s+sinh|\s+cơ\s+sở)?(?!\s+(?:Nhà\s+nước|Việt\s+Nam|chuyên\s+nghiệp))"
            r"|phương\s+tiện(?:\s+giao\s+thông|\s+thủy(?:\s+nội\s+địa)?|\s+vi\s+phạm)?|tàu\s+biển"
            r"|hàng\s+hóa(?:\s+giả\s+mạo|\s+nhập\s+khẩu|\s+xuất\s+khẩu|\s+vi\s+phạm)?"
            r"|sản\s+phẩm\s+thủy\s+sản|hàng\s+thủy\s+sản(?:\s+xuất\s+khẩu)?"
            r"|tang\s+vật(?:\s+vi\s+phạm)?"
            r"|mũ\s+bảo\s+hiểm|trang\s+thiết\s+bị(?:\s+an\s+toàn)?"
            r"|quỹ\s+nhà\s+nước|(?<!Luật )ngân\s+sách\s+(?:nhà\s+nước|trung\s+ương|địa\s+phương))\b",
            re.I,
        ),
    ),
    (
        "DIA_DIEM",
        re.compile(
            r"\b(?:tại\s+(?:nơi\s+làm\s+việc|cơ\s+sở\s+giam\s+giữ|nơi\s+cư\s+trú|địa\s+phương|địa\s+bàn\s+nông\s+thôn|cửa\s+khẩu|Việt\s+Nam|thị\s+trường\s+trong\s+nước)"
            r"|trên\s+(?:phần\s+đường\s+dành\s+cho\s+người\s+đi\s+bộ|đường\s+giao\s+thông|lãnh\s+thổ\s+Việt\s+Nam|địa\s+bàn\s+(?:tỉnh|nông\s+thôn|hoạt\s+động))"
            r"|ra\s+thị\s+trường\s+quốc\s+tế"
            r"|lãnh\s+thổ\s+nước\s+Cộng\s+hòa\s+xã\s+hội\s+chủ\s+nghĩa\s+Việt\s+Nam"
            r"|khu\s+nông\s+nghiệp\s+ứng\s+dụng\s+công\s+nghệ\s+cao|khu\s+công\s+nghiệp,\s*khu\s+chế\s+xuất"
            r"|nơi\s+(?:làm\s+việc\s+ổn\s+định|làm\s+việc|cư\s+trú\s+rõ\s+ràng|cư\s+trú|thực\s+hiện\s+thí\s+điểm|đặt\s+trụ\s+sở\s+chính))\b",
            re.I,
        ),
    ),
]


# ======================================================================
# 2. Bộ mẫu Regex cho các Thực thể Tâm / Bao ngoài (Outer Hub Spans)
# ======================================================================
STOP_TAIL_RE = re.compile(
    r"\s+(?:quy\s+định\s+tại|theo\s+quy\s+định|theo\s+yêu\s+cầu|theo\s+hướng\s+dẫn|nếu\s+|thì\s+|mà\s+|nhưng\s+|để\s+|khi\s+(?!chưa\s+|không\s+)|trường\s+hợp\s+|trong\s+trường\s+hợp|đối\s+với\s+|tại\s+khoản|tại\s+điều|tại\s+điểm|so\s+với\s+thời\s+hạn).*$",
    re.I,
)

OUTER_HUB_PATTERNS = [
    (
        "HINH_PHAT_CHE_TAI",
        re.compile(
            r"\b(?:Phạt\s+tiền\s+từ\s+\d{1,3}(?:[.,]\d{3})+\s*đồng\s+đến\s+\d{1,3}(?:[.,]\d{3})+\s*đồng"
            r"|phạt\s+tiền\s+(?:đến|từ)\s+\d{1,3}(?:[.,]\d{3})+\s*đồng(?:\s+đến\s+\d{1,3}(?:[.,]\d{3})+\s*đồng)?"
            r"|phạt\s+cảnh\s+cáo(?:\s+hoặc\s+phạt\s+tiền(?:\s+từ\s+\d{1,3}(?:[.,]\d{3})+\s*đồng\s+đến\s+\d{1,3}(?:[.,]\d{3})+\s*đồng)?)?"
            r"|tước\s+quyền\s+sử\s+dụng\s+(?:Giấy\s+phép(?:\s+lái\s+xe|\s+kinh\s+doanh|\s+lao\s+động|\s+hoạt\s+động)?|Thẻ\s+(?:công\s+chứng\s+viên|luật\s+sư)|chứng\s+chỉ\s+hành\s+nghề)(?:\s+từ\s+\d+\s+tháng\s+đến\s+\d+\s+tháng)?"
            r"|tịch\s+thu\s+(?:tang\s+vật,\s*phương\s+tiện(?:\s+vi\s+phạm)?|tang\s+vật(?:\s+vi\s+phạm(?:\s+hành\s+chính)?)?(?:,\s*phương\s+tiện)?|phương\s+tiện(?:\s+vi\s+phạm)?|hàng\s+hóa(?:\s+vi\s+phạm)?|một\s+phần\s+hoặc\s+toàn\s+bộ\s+tài\s+sản)"
            r"|khấu\s+trừ\s+một\s+phần\s+(?:thu\s+nhập|tiền\s+lương)(?:\s+từ\s+\d+(?:[.,]\d+)?\s*%\s+đến\s+\d+(?:[.,]\d+)?\s*%)?"
            r"|Cải\s+tạo\s+không\s+giam\s+giữ(?:\s+được\s+áp\s+dụng)?(?:\s+từ\s+\d+\s+tháng\s+đến\s+\d+\s+năm|\s+đến\s+\d+\s+năm)?"
            r"|xử\s+lý\s+kỷ\s+luật,\s*xử\s+lý\s+vi\s+phạm\s+hành\s+chính"
            r"|(?<=bị\s)xử\s+phạt\s+vi\s+phạm\s+hành\s+chính"
            r"|phạt\s+tù\s+từ\s+\d+\s+(?:tháng|năm)\s+đến\s+\d+\s+năm"
            r"|chịu\s+trách\s+nhiệm\s+hình\s+sự|truy\s+cứu\s+trách\s+nhiệm\s+hình\s+sự|miễn\s+trách\s+nhiệm\s+hình\s+sự"
            r"|bị\s+trục\s+xuất(?:\s+theo\s+bản\s+án)?"
            r"|tù\s+chung\s+thân|xử\s+phạt\s+tử\s+hình)\b",
            re.I,
        ),
    ),
    (
        "BIEN_PHAP_KHAC_PHUC",
        re.compile(
            r"\b(?:buộc\s+(?:phải\s+)?(?:trả\s+lại|nộp\s+lại|nộp\s+vào\s+ngân\s+sách\s+nhà\s+nước|khôi\s+phục\s+lại|bồi\s+thường|tiêu\s+hủy|tháo\s+dỡ|chấm\s+dứt|giảm(?:\s+giá\s+trị)?|thu\s+hồi|cải\s+chính|hủy\s+bỏ\s+thông\s+tin|cung\s+cấp\s+thông\s+tin|giải\s+trình|quản\s+lý\s+tách\s+biệt|mở\s+tài\s+khoản|xây\s+dựng\s+hệ\s+thống|tách\s+biệt|dừng\s+hoạt\s+động|dừng\s+thực\s+hiện|báo\s+cáo|công\s+bố\s+báo\s+cáo|thông\s+qua|xin\s+lỗi|đưa\s+ra\s+khỏi\s+lãnh\s+thổ|người\s+nước\s+ngoài\s+bị\s+kết\s+án\s+phải\s+rời\s+khỏi|người\s+bị\s+kết\s+án\s+phải\s+chấp\s+hành)\s+[^,.;:()]{3,55}\b"
            r"|bồi\s+thường\s+(?:thiệt\s+hại\s+)?cho\s+(?:người\s+sử\s+dụng\s+lao\s+động|người\s+lao\s+động)(?:\s+nửa\s+tháng\s+tiền\s+lương)?"
            r"|thu\s+hồi\s+(?:Giấy\s+chứng\s+nhận(?:\s+đăng\s+ký\s+(?:doanh\s+nghiệp|kinh\s+doanh|đầu\s+tư))?|Giấy\s+phép(?:\s+kinh\s+doanh|\s+hoạt\s+động|\s+lao\s+động|\s+xây\s+dựng)?|Giấy\s+đăng\s+ký(?:\s+hành\s+nghề(?:\s+luật\s+sư)?)?|chứng\s+chỉ\s+hành\s+nghề(?:\s+luật\s+sư)?|Thẻ\s+(?:công\s+chứng\s+viên|luật\s+sư)|quyết\s+định\s+bổ\s+nhiệm)"
            r"|đình\s+chỉ\s+hoạt\s+động(?:\s+giao\s+dịch\s+chứng\s+khoán|\s+nghiệp\s+vụ\s+bảo\s+lãnh\s+phát\s+hành\s+chứng\s+khoán|\s+chào\s+mua\s+công\s+khai)?(?:\s+có\s+thời\s+hạn)?(?:\s+từ\s+\d+\s+tháng\s+đến\s+\d+\s+tháng)?)\b",
            re.I,
        ),
    ),
    (
        "HANH_VI_VI_PHAM",
        re.compile(
            r"(?:"
            # 1. Mệnh đề hành vi sau cụm "đối với [chủ thể thực hiện] hành vi ..."
            r"đối\s+với\s+(?:[^,.;:()]{1,40}?\s+thực\s+hiện\s+)?hành\s+vi\s+(?!vi\s+phạm\s+(?:sau|quy\s+định\s+tại))([^.;:]{4,115}\b)"
            # 2. Mệnh đề hành vi bắt đầu bằng Không / Chậm + động từ pháp lý
            r"|\b((?:không|chậm)\s+(?!phải\s+là\b|phải\s+nộp\b|có\s+Cục\b|giam\s+giữ\b|kỳ\s+hạn\b|chuyển\s+đổi\b|kèm\s+chứng\s+quyền\b|điều\s+hành\b|liền\s+kề\b|quá\s+\d)(?:tham\s+gia(?:\s+lớp\s+bồi\s+dưỡng)?|đội\s+mũ\s+bảo\s+hiểm|ký\s+kết|giao\s+kết|thanh\s+toán|trả(?:\s+đủ)?|nộp\s+hồ\s+sơ|chấp\s+hành|báo\s+trước|thông\s+báo|cấp\s+Giấy|niêm\s+yết|lập(?:\s+hồ\s+sơ|\s+báo\s+cáo)?|bảo\s+đảm|đảm\s+bảo|công\s+bố|sửa\s+đổi,\s*bổ\s+sung\s+hồ\s+sơ|chuyển\s+số\s+tiền|đăng\s+ký|rà\s+soát|kiểm\s+tra|bổ\s+nhiệm|tổ\s+chức\s+họp|mời\s+đại\s+diện|thực\s+hiện\s+chi\s+trả|thông\s+qua|báo\s+cáo|đưa\s+nội\s+dung|thuyết\s+minh|luôn\s+giữ)[^.;:()]{3,95}\b)"
            # 3. Mệnh đề hành vi có tính chất sai phạm (không đúng quy định / không phù hợp / sai sự thật / khi chưa được...)
            r"|\b((?:Thực\s+hiện|Thay\s+đổi|Công\s+bố|Quảng\s+cáo|Chứng\s+nhận|Chào\s+bán(?:,\s*phát\s+hành)?|Sử\s+dụng|Lập,\s*xác\s+nhận|Làm\s+giả|Tư\s+vấn,\s*hỗ\s+trợ|Cung\s+cấp|Đưa\s+ra\s+nhận\s+định(?:\s+hoặc\s+đảm\s+bảo)?|Kiêm\s+nhiệm)\s+[^.;:()]{4,115}?(?:không\s+đúng(?:\s+với)?(?:\s+thời\s+gian|\s+phương\s+án|\s+quy\s+định(?:\s+pháp\s+luật)?)?|không\s+phù\s+hợp|không\s+đầy\s+đủ|không\s+chính\s+xác|không\s+trung\s+thực|sai\s+lệch|sai\s+sự\s+thật|trái\s+quy\s+định|trái\s+phép|khi\s+chưa\s+(?:được|đáp\s+ứng(?:\s+đủ\s+điều\s+kiện)?)|trong\s+thời\s+gian\s+hạn\s+chế|không\s+được\s+chuyển\s+nhượng|có\s+tính\s+chất\s+quảng\s+cáo|trong\s+tương\s+lai|đảm\s+bảo\s+không\s+bị\s+thua\s+lỗ|của\s+một\s+công\s+ty\s+đại\s+chúng)\b)"
            # 4. Các mẫu hành vi vi phạm chuyên biệt
            r"|\b(giữ\s+bản\s+chính\s+giấy\s+tờ\s+tùy\s+thân(?:\s+của\s+người\s+lao\s+động)?"
            r"|dừng\s+xe,\s*đỗ\s+xe(?:\s+trái\s+quy\s+định)?"
            r"|ngược\s+đãi,\s*đánh\s+đập|cưỡng\s+bức\s+lao\s+động"
            r"|hành\s+nghề\s+(?:khác|khi\s+chưa\s+được\s+cấp\s+chứng\s+chỉ\s+hành\s+nghề|công\s+chứng\s+trái\s+phép)"
            r"|kiêm\s+nhiệm\s+các\s+chức\s+danh\s+tư\s+pháp"
            r"|gây\s+(?:hậu\s+quả\s+nguy\s+hại\s+cho\s+xã\s+hội|thiệt\s+hại\s+cho\s+tài\s+sản(?:\s+nhà\s+nước|\s+của\s+người\s+khác)?|thiệt\s+hại\s+trong\s+khi\s+thi\s+hành\s+mệnh\s+lệnh)"
            r"|thực\s+hiện\s+hành\s+vi\s+(?:phạm\s+tội\s+mới|nguy\s+hiểm\s+cho\s+xã\s+hội|vi\s+phạm(?:\s+pháp\s+luật|\s+hành\s+chính)?)"
            r"|vi\s+phạm\s+quy\s+định\s+(?:pháp\s+luật\s+)?về\s+[^,.;:()]{3,55}\b"
            r"|cố\s+tình\s+trốn\s+tránh(?:\s+và\s+đã\s+có\s+quyết\s+định\s+truy\s+nã)?"
            r"|sử\s+dụng\s+trái\s+phép\s+(?:tài\s+sản(?:\s+nhà\s+nước)?|hàng\s+hóa(?:\s+giả\s+mạo)?|Giấy\s+phép(?:\s+kinh\s+doanh|\s+hoạt\s+động)?|Thẻ\s+(?:công\s+chứng\s+viên|luật\s+sư)|chứng\s+chỉ\s+hành\s+nghề)"
            r"|cho\s+người\s+khác\s+mượn,\s*thuê\s+(?:Thẻ\s+(?:công\s+chứng\s+viên|luật\s+sư)|chứng\s+chỉ\s+hành\s+nghề|Giấy\s+phép(?:\s+kinh\s+doanh|\s+hoạt\s+động)?)"
            r"|tẩy\s+xóa,\s*sửa\s+chữa\s+làm\s+sai\s+lệch\s+nội\s+dung\s+(?:Giấy\s+phép|Giấy\s+đăng\s+ký|chứng\s+chỉ\s+hành\s+nghề|Thẻ\s+công\s+chứng\s+viên|hồ\s+sơ)"
            r"|kê\s+khai\s+không\s+trung\s+thực(?:\s+trong\s+hồ\s+sơ(?:\s+đề\s+nghị|\s+đăng\s+ký)?)?"
            r"|chiếm\s+đoạt\s+tài\s+sản(?:\s+nhà\s+nước|\s+của\s+người\s+khác)?"
            r"|lợi\s+dụng\s+chức\s+vụ,\s*quyền\s+hạn"
            r"|giả\s+mạo\s+(?:hồ\s+sơ(?:\s+đăng\s+ký|\s+đề\s+nghị)?|giấy\s+tờ(?:\s+tùy\s+thân)?|chứng\s+chỉ\s+hành\s+nghề|chữ\s+ký))\b"
            r")",
            re.I,
        ),
    ),
    (
        "NGHIA_VU_QUYEN",
        re.compile(
            r"(?<!không\s)(?<!Không\s)(?<!chưa\s)(?<!chậm\s)\b(?:tham\s+gia\s+lớp\s+bồi\s+dưỡng\s+nghiệp\s+vụ\s+công\s+chứng(?:\s+hàng\s+năm)?"
            r"|hướng\s+dẫn,\s*chỉ\s+đạo\s+(?:tổ\s+chức\s+thực\s+hiện(?:\s+việc\s+bồi\s+dưỡng\s+nghiệp\s+vụ\s+công\s+chứng)?|Ủy\s+ban\s+nhân\s+dân\s+các\s+cấp)"
            r"|hướng\s+dẫn\s+(?:thống\s+nhất\s+trong\s+hệ\s+thống\s+quỹ\s+tín\s+dụng\s+nhân\s+dân|thực\s+hiện\s+theo\s+quy\s+định)"
            r"|nộp\s+lại\s+(?:Giấy\s+đăng\s+ký(?:\s+hành\s+nghề(?:\s+luật\s+sư)?)?|Giấy\s+phép(?:\s+hoạt\s+động|\s+kinh\s+doanh|\s+lao\s+động)?|chứng\s+chỉ\s+hành\s+nghề|Thẻ\s+(?:công\s+chứng\s+viên|luật\s+sư))"
            r"|nộp\s+hồ\s+sơ\s+(?:kê\s+khai(?:\s+thuế)?|đăng\s+ký|đề\s+nghị(?:\s+khoanh\s+nợ)?|bổ\s+nhiệm|dự\s+thầu|thanh\s+toán|xét\s+tặng|hành\s+nghề)"
            r"|lập\s+hồ\s+sơ\s+đề\s+nghị(?:\s+khoanh\s+nợ)?"
            r"|xem\s+xét(?:\s*,?\s*quyết\s+định)?\s+(?:việc\s+khoanh\s+nợ|khoanh\s+nợ\s+không\s+tính\s+lãi|cho\s+vay\s+không\s+có\s+tài\s+sản\s+bảo\s+đảm|hỗ\s+trợ\s+từ\s+dự\s+phòng\s+ngân\s+sách\s+trung\s+ương)"
            r"|không\s+phải\s+nộp\s+phí\s+chứng\s+thực\s+hợp\s+đồng\s+thế\s+chấp\s+tài\s+sản"
            r"|cơ\s+cấu\s+lại\s+thời\s+hạn\s+trả\s+nợ,\s*khoanh\s+nợ\s+và\s+cho\s+vay\s+mới"
            r"|bố\s+trí\s+(?:nguồn\s+vốn\s+ngân\s+sách|ngân\s+sách\s+địa\s+phương)"
            r"|sử\s+dụng\s+dự\s+phòng\s+để\s+xử\s+lý\s+rủi\s+ro"
            r"|sửa\s+đổi,\s*bổ\s+sung\s+hợp\s+đồng\s+(?:lao\s+động|tín\s+dụng)"
            r"|đơn\s+phương\s+chấm\s+dứt\s+hợp\s+đồng\s+lao\s+động(?:\s+của\s+người\s+lao\s+động|\s+của\s+người\s+sử\s+dụng\s+lao\s+động)?"
            r"|giao\s+kết\s+hợp\s+đồng\s+lao\s+động|chấm\s+dứt\s+hợp\s+đồng\s+lao\s+động"
            r"|ký\s+quỹ\s+và\s+được\s+cấp\s+Giấy\s+phép\s+hoạt\s+động|được\s+cấp\s+Giấy\s+phép\s+(?:hoạt\s+động|kinh\s+doanh|lao\s+động)"
            r"|cấp\s+(?:Giấy\s+chứng\s+nhận(?:\s+đăng\s+ký\s+(?:doanh\s+nghiệp|kinh\s+doanh|đầu\s+tư)|\s+doanh\s+nghiệp\s+nông\s+nghiệp\s+ứng\s+dụng\s+công\s+nghệ\s+cao)?|Giấy\s+phép(?:\s+hoạt\s+động|\s+kinh\s+doanh|\s+lao\s+động|\s+xây\s+dựng)?|Giấy\s+đăng\s+ký(?:\s+hành\s+nghề)?|chứng\s+chỉ\s+hành\s+nghề|Thẻ\s+(?:công\s+chứng\s+viên|luật\s+sư))"
            r"|bổ\s+nhiệm,\s*miễn\s+nhiệm,\s*cách\s+chức\s+Chủ\s+tịch,\s*Phó\s+Chủ\s+tịch"
            r"|giới\s+thiệu\s+nhân\s+sự\s+Chủ\s+tịch\s+Ủy\s+ban\s+nhân\s+dân\s+cùng\s+cấp"
            r"|kiểm\s+tra,\s*chứng\s+nhận\s+chất\s+lượng,\s*an\s+toàn\s+thực\s+phẩm(?:\s+đối\s+với\s+thủy\s+sản)?"
            r"|xét\s+tặng\s+Kỷ\s+niệm\s+chương"
            r"|thực\s+hiện\s+(?:một\s+số\s+công\s+việc\s+lao\s+động\s+phục\s+vụ\s+cộng\s+đồng|nghĩa\s+vụ\s+quân\s+sự|nhiệm\s+vụ\s+quốc\s+phòng,\s*an\s+ninh|hợp\s+đồng\s+lao\s+động|chế\s+độ\s+báo\s+cáo)"
            r"|thanh\s+toán\s+đầy\s+đủ\s+tiền\s+lương(?:\s+cho\s+người\s+lao\s+động)?"
            r"|trả\s+tiền\s+lương(?:\s+cho\s+người\s+lao\s+động)?|trả\s+trợ\s+cấp\s+thôi\s+việc(?:\s+cho\s+người\s+lao\s+động)?"
            r"|thông\s+báo\s+bằng\s+văn\s+bản\s+cho\s+(?:người\s+lao\s+động|Sở\s+Tư\s+pháp|cơ\s+quan\s+có\s+thẩm\s+quyền))\b",
            re.I,
        ),
    ),
]


def _clamp_span_to_max_tokens(text: str, s: int, e: int, inner_spans: list, max_tokens: int = MAX_SPAN_TOKENS):
    """
    Đảm bảo span (s, e) có độ dài từ 1..max_tokens từ (sau khi tách từ bằng vi_tokenize)
    và bao trọn (không cắt ngang) bất kỳ inner_span nào nằm bên trong.
    """
    sub = text[s:e]
    sub_clean = STOP_TAIL_RE.sub("", sub).strip(" ,.;:()")
    if not sub_clean:
        return None
    e = s + len(sub_clean)
    # Nếu biên phải e của Outer Hub rơi vào giữa một thực thể vệ tinh (VD: 'nộp hồ sơ đề nghị' cắt ngang
    # 'hồ sơ đề nghị cấp giấy phép môi trường'), ưu tiên mở rộng e tới hết thực thể vệ tinh đó
    for is_start, is_end, _ in inner_spans:
        if is_start > s and is_start < e < is_end:
            if len(vi_tokenize(text[s:is_end])) <= max_tokens:
                e = is_end
            else:
                e = is_start
    words = vi_tokenize(text[s:e])
    if len(words) <= max_tokens:
        while e > s and text[e - 1] in " ,.;:()":
            e -= 1
        return (s, e) if len(vi_tokenize(text[s:e])) >= 2 else None

    # Cắt bớt từ bên phải để <= max_tokens
    parts = sub_clean.split()
    while len(parts) > 2:
        parts.pop()
        cand_sub = " ".join(parts)
        if len(vi_tokenize(cand_sub)) <= max_tokens:
            new_e = s + len(cand_sub)
            for is_start, is_end, _ in inner_spans:
                if is_start >= s and is_start < new_e < is_end:
                    new_e = is_start
            while new_e > s and text[new_e - 1] in " ,.;:()":
                new_e -= 1
            if new_e > s and len(vi_tokenize(text[s:new_e])) >= 2:
                return (s, new_e)
    return None


_DATE_SUFFIX_RE = re.compile(r"\s+ngày\s+\d{1,2}\s+tháng\s+\d{1,2}\s+năm\s+\d{4}$", re.I)

# ======================================================================
# 2B. Tự động rút trích Từ điển Động cấp Văn bản (Document Self-Lexicon)
#     & Mở rộng Ranh giới Cụm Danh Từ bằng Điểm Chặn Ngữ Pháp
# ======================================================================
_DOC_HEAD_CLASSIFIER = [
    (
        "GIAY_TO_HO_SO",
        re.compile(
            r"^(?:Giấy\s+(?:chứng\s+nhận|phép|đăng\s+ký|xác\s+nhận|báo|ủy\s+quyền|đề\s+nghị|tờ)"
            r"|Hồ\s+sơ|Đơn\s+(?:đề\s+nghị|đăng\s+ký|khiếu\s+nại|tố\s+cáo|xin)|Tờ\s+khai|Báo\s+cáo|Biên\s+bản"
            r"|Chứng\s+chỉ|Văn\s+bằng|Thẻ\s+|Quyết\s+định\s+(?:cấp|thu\s+hồi|bổ\s+nhiệm|miễn\s+nhiệm|xử\s+phạt|phê\s+duyệt|thành\s+lập|cho\s+phép)"
            r"|Phương\s+án|Đề\s+án|Kế\s+hoạch|Quy\s+chế|Điều\s+lệ|Nội\s+quy|Hợp\s+đồng|Sổ\s+|Phiếu\s+|Hóa\s+đơn|Chứng\s+từ|Biên\s+lai|Bản\s+(?:kê\s+khai|cáo\s+bạch|cam\s+kết|sao)|Kỷ\s+niệm\s+chương)\b",
            re.I,
        ),
    ),
    (
        "CO_QUAN_THAM_QUYEN",
        re.compile(
            r"^(?:Bộ\s+|Cơ\s+quan\s+(?:quản\s+lý|nhà\s+nước|chuyên\s+môn|đại\s+diện|công\s+an|thuế|hải\s+quan|thanh\s+tra|thi\s+hành\s+án|điều\s+tra)"
            r"|Ủy\s+ban\s+(?:nhân\s+dân|Chứng\s+khoán|Cạnh\s+tranh|Quản\s+lý\s+vốn|Thường\s+vụ\s+Quốc\s+hội)|Hội\s+đồng\s+nhân\s+dân"
            r"|Tổng\s+cục\s+|Cục\s+|Vụ\s+|Thanh\s+tra\s+|Sở\s+(?!giao\s+dịch\s+chứng\s+khoán)|Chi\s+cục\s+|Tòa\s+án|Viện\s+kiểm\s+sát|Cảng\s+vụ|Kho\s+bạc|Bảo\s+hiểm\s+xã\s+hội|Kiểm\s+toán\s+nhà\s+nước)\b",
            re.I,
        ),
    ),
    (
        "TO_CHUC_DOANH_NGHIEP",
        re.compile(
            r"^(?:Công\s+ty|Doanh\s+nghiệp|Tổng\s+công\s+ty|Tập\s+đoàn|Tổ\s+chức\s+(?:hành\s+nghề|kinh\s+doanh|tín\s+dụng|tài\s+chính|kiểm\s+toán|thẩm\s+định|đấu\s+giá|giám\s+định|trọng\s+tài|xã\s+hội|khoa\s+học|giáo\s+dục|y\s+tế|bảo\s+hiểm|phát\s+hành|chào\s+bán|niêm\s+yết|lưu\s+ký|bù\s+trừ|đại\s+diện)"
            r"|Ngân\s+hàng\s+(?!Nhà\s+nước)|Chi\s+nhánh|Văn\s+phòng\s+(?:công\s+chứng|luật\s+sư|thừa\s+phát\s+lại|đăng\s+ký|đại\s+diện)|Phòng\s+công\s+chứng"
            r"|Quỹ\s+|Trung\s+tâm\s+|Cơ\s+sở\s+|Đơn\s+vị\s+(?:sự\s+nghiệp|kinh\s+doanh|kiểm\s+toán|được\s+kiểm\s+toán|quản\s+lý)|Hợp\s+tác\s+xã|Liên\s+hiệp\s+hợp\s+tác\s+xã"
            r"|Hội\s+đồng\s+(?:quản\s+trị|thành\s+viên|thẩm\s+định)|Ban\s+(?:kiểm\s+soát|chủ\s+nhiệm)|Ủy\s+ban\s+kiểm\s+toán|Đoàn\s+luật\s+sư|Liên\s+đoàn|Hiệp\s+hội|Sở\s+giao\s+dịch\s+chứng\s+khoán)\b",
            re.I,
        ),
    ),
    (
        "CHU_THE_CA_NHAN",
        re.compile(
            r"^(?:Người\s+(?:lao\s+động|sử\s+dụng\s+lao\s+động|hành\s+nghề|đại\s+diện|điều\s+khiển|phạm\s+tội|bị\s+kết\s+án|nộp\s+thuế|tập\s+sự|chấp\s+hành)"
            r"|Nhà\s+đầu\s+tư|Công\s+chứng\s+viên|Luật\s+sư|Đấu\s+giá\s+viên|Giám\s+định\s+viên|Thừa\s+phát\s+lại|Kiểm\s+toán\s+viên|Thẩm\s+định\s+viên|Quản\s+tài\s+viên|Trọng\s+tài\s+viên|Kế\s+toán\s+trưởng)\b",
            re.I,
        ),
    ),
]

# Điểm chặn ngữ pháp biên phải (Syntactic Right-Boundary Stopwords) cho Cụm Danh Từ Pháp Lý
_SYNTACTIC_STOP_RE = re.compile(
    r"\b(?:"
    r"này|đó|ấy|nêu\s+trên|nói\s+trên|sau\s+đây|như\s+sau|khác|hợp\s+lệ|đầy\s+đủ|chính\s+xác|trung\s+thực|cụ\s+thể"
    r"|phải|được|không|chưa|đã|đang|sẽ|bị|chịu|do|bởi|là|gồm|bao\s+gồm|có"
    r"|thực\s+hiện|nộp|gửi|thu\s+hồi|đình\s+chỉ|tước|buộc|phạt|xử\s+phạt|vi\s+phạm"
    r"|phù\s+hợp|liên\s+quan|xét|quy\s+định|áp\s+dụng|ban\s+hành|bảo\s+đảm|đảm\s+bảo"
    r"|theo|tại|trong|kể\s+từ|đối\s+với|cho|với|đến|từ|trước|sau|khi|nếu|trường\s+hợp|nhưng|mà|thì|để|nhằm|hoặc|hay|và|vào|ra|qua"
    r"|của\s+(?:cơ\s+quan|người|tổ\s+chức|doanh\s+nghiệp|cá\s+nhân|khách\s+hàng|mình|địa\s+phương|nhà\s+nước|Chính\s+phủ|Bộ|Sở|Ủy\s+ban|một|các)"
    r")\b",
    re.I,
)

# Các mẫu Hạt nhân Cụm Danh Từ Mở (Open-Domain Syntactic Prefixes)
_OPEN_DOMAIN_PREFIXES = [
    (
        "GIAY_TO_HO_SO",
        re.compile(
            r"\b(?:"
            r"Giấy\s+(?:chứng\s+nhận|phép|đăng\s+ký|xác\s+nhận)\s+(?:đủ\s+điều\s+kiện\s+|đăng\s+ký\s+|hoạt\s+động\s+|kinh\s+doanh\s+|hành\s+nghề\s+|lưu\s+hành\s+|quyền\s+|an\s+toàn\s+|xuất\s+xứ\s+|kiểm\s+định\s+|lập\s+)?"
            r"|hồ\s+sơ\s+(?:đề\s+nghị|đăng\s+ký|trình|xin\s+cấp|mời\s+thầu|dự\s+thầu|quyết\s+toán|kê\s+khai|thẩm\s+định)\s+"
            r"|đơn\s+(?:đề\s+nghị|đăng\s+ký|xin\s+cấp)\s+"
            r"|tờ\s+khai\s+(?:đăng\s+ký|hải\s+quan|thuế|đề\s+nghị)\s+"
            r"|chứng\s+chỉ\s+hành\s+nghề\s+"
            r"|Báo\s+cáo\s+(?:đánh\s+giá|kết\s+quả|tình\s+hình)\s+"
            r"|Quy\s+chế\s+(?:quản\s+lý|hoạt\s+động|tổ\s+chức\s+và\s+hoạt\s+động|phối\s+hợp|kiểm\s+soát|xét\s+tặng)\s+"
            r"|Đề\s+án\s+(?:tổ\s+chức|thành\s+lập|phát\s+triển|cơ\s+cấu\s+lại)\s+"
            r")((?:khám\s+bệnh,\s*chữa\s+bệnh|sản\s+xuất,\s*kinh\s+doanh|chào\s+bán,\s*phát\s+hành|xuất\s+khẩu,\s*nhập\s+khẩu|[^,.;:!?()\n]){2,50})",
            re.I,
        ),
    ),
    (
        "TO_CHUC_DOANH_NGHIEP",
        re.compile(
            r"\b(?:"
            r"tổ\s+chức\s+(?:hành\s+nghề|kinh\s+doanh(?:\s+dịch\s+vụ)?|dịch\s+vụ|kiểm\s+định|giám\s+định|chứng\s+nhận|đánh\s+giá\s+sự\s+phù\s+hợp|đấu\s+giá|thẩm\s+định|tín\s+dụng|khoa\s+học\s+và\s+công\s+nghệ)\s+"
            r"|doanh\s+nghiệp\s+(?:kinh\s+doanh(?:\s+dịch\s+vụ)?|sản\s+xuất|cung\s+cấp\s+dịch\s+vụ|khai\s+thác|viễn\s+thông|bảo\s+hiểm|thẩm\s+định|kiểm\s+toán)\s+"
            r"|cơ\s+sở\s+(?:sản\s+xuất|kinh\s+doanh|khám\s+bệnh,\s*chữa\s+bệnh|giáo\s+dục|đào\s+tạo|dạy\s+nghề|dịch\s+vụ|chăn\s+nuôi|giết\s+mổ)\s+"
            r"|Trung\s+tâm\s+(?:dịch\s+vụ|kiểm\s+định|giám\s+định|trợ\s+giúp|tư\s+vấn|phát\s+triển\s+quỹ\s+đất|lưu\s+ký)\s+"
            r"|Văn\s+phòng\s+(?:đăng\s+ký|công\s+chứng|luật\s+sư|thừa\s+phát\s+lại)\s+"
            r")((?:khám\s+bệnh,\s*chữa\s+bệnh|sản\s+xuất,\s*kinh\s+doanh|chào\s+bán,\s*phát\s+hành|xuất\s+khẩu,\s*nhập\s+khẩu|[^,.;:!?()\n]){2,45})",
            re.I,
        ),
    ),
]


def _classify_doc_term(term: str):
    term_clean = term.strip(" “”\"'.,;:()-")
    if not term_clean or len(term_clean) < 4:
        return None
    for etype, rgx in _DOC_HEAD_CLASSIFIER:
        if rgx.search(term_clean):
            n_tok = len(vi_tokenize(term_clean))
            if 2 <= n_tok <= MAX_SPAN_TOKENS:
                return etype, term_clean
    return None


def extract_document_self_lexicon(paras: list) -> dict:
    """
    Quét nhanh toàn bộ các đoạn văn `paras` của một văn bản pháp luật (Pass 1) để tự động rút trích
    Từ điển Động (`doc_lexicon`) gồm các thực thể chuyên biệt được định nghĩa hoặc gọi tắt ngay trong văn bản đó:
      1. Các mục giải thích từ ngữ: '1. [Thuật ngữ] là ...'
      2. Các cụm định danh / gọi tắt: '[Thuật ngữ đầy đủ] (sau đây gọi tắt là [Thuật ngữ rút gọn])'
      3. Các văn bản / quy chế phụ lục ban hành kèm theo: 'Ban hành kèm theo ... [Quy chế / Đề án / Quy định ...]'
    """
    lexicon = {
        "GIAY_TO_HO_SO": set(),
        "TO_CHUC_DOANH_NGHIEP": set(),
        "CO_QUAN_THAM_QUYEN": set(),
        "CHU_THE_CA_NHAN": set(),
    }
    def_re = re.compile(r"^(?:\d+\.\s+|[a-zđ]\)\s+)?[“\"']?([A-ZÀ-ỸĐ][^”\"':;,.]{4,85}?)[”\"']?\s+là\s+", re.I)
    alias_re = re.compile(
        r"([A-ZÀ-ỸĐa-zà-ỹđ][^,.;:()]{4,85}?)\s*\((?:sau\s+đây\s+)?gọi(?:\s+tắt|\s+chung)?\s+là\s+[“\"']?([^”\"')]{3,60}?)[”\"']?\)",
        re.I,
    )
    attached_re = re.compile(
        r"Ban\s+hành\s+kèm\s+theo\s+[^,.;:]{3,45}?\s+((?:Quy\s+chế|Quy\s+định|Đề\s+án|Kế\s+hoạch|Điều\s+lệ|Hướng\s+dẫn)[^.;:()]{4,90})",
        re.I,
    )

    for p in paras:
        m_def = def_re.match(p.strip())
        if m_def:
            res = _classify_doc_term(m_def.group(1))
            if res:
                lexicon[res[0]].add(res[1])

        for m_al in alias_re.finditer(p):
            full_t, short_t = m_al.group(1).strip(), m_al.group(2).strip()
            res_full = _classify_doc_term(full_t)
            if res_full:
                lexicon[res_full[0]].add(res_full[1])
                if 2 <= len(vi_tokenize(short_t)) <= MAX_SPAN_TOKENS:
                    lexicon[res_full[0]].add(short_t.strip(" “”\"'.,;:"))
            else:
                res_short = _classify_doc_term(short_t)
                if res_short:
                    lexicon[res_short[0]].add(res_short[1])

        for m_att in attached_re.finditer(p):
            res_att = _classify_doc_term(m_att.group(1))
            if res_att:
                lexicon[res_att[0]].add(res_att[1])

    # Sắp xếp từ dài đến ngắn để ưu tiên khớp cụm đầy đủ nhất
    return {k: sorted(v, key=len, reverse=True) for k, v in lexicon.items() if v}


def extract_intra_sentence_spans(text: str, base_offset: int = 0, existing_spans: list = None, doc_lexicon: dict = None):
    """
    Trích xuất danh sách các span ngữ nghĩa nội câu (bao gồm cả Outer Hub Spans và Inner Spans lồng bên trong)
    từ chuỗi `text[base_offset:]`.
    Kết hợp 3 lớp nhận diện thực thể vệ tinh:
      - Lớp 0: Từ điển Động của chính văn bản (`doc_lexicon`) nếu được cung cấp.
      - Lớp 1: Bộ mẫu chuyên ngành chuẩn (`INNER_PATTERNS`).
      - Lớp 2: Mở rộng ranh giới Cụm Danh Từ Mở theo Điểm chặn Ngữ pháp (`_OPEN_DOMAIN_PREFIXES` + `_SYNTACTIC_STOP_RE`).
    Trả về danh sách các tuple `(char_start, char_end, entity_type)`.
    """
    existing_spans = existing_spans or []
    sub_text = text[base_offset:]

    def conflicts_with_existing(s, e):
        return any(s < ex_e and ex_s < e for ex_s, ex_e, _ in existing_spans)

    inner_spans = []

    # Lớp 0: Khớp từ Từ điển Động của văn bản (doc_lexicon) nếu có
    if doc_lexicon:
        for etype in ("GIAY_TO_HO_SO", "CO_QUAN_THAM_QUYEN", "TO_CHUC_DOANH_NGHIEP", "CHU_THE_CA_NHAN"):
            for term in doc_lexicon.get(etype, []):
                if not term:
                    continue
                pat = re.compile(r"\b" + re.escape(term) + r"(?=\b|\s|[.,;:!?)]|$)", re.I)
                for m in pat.finditer(sub_text):
                    s, e = base_offset + m.start(), base_offset + m.end()
                    if e <= s or conflicts_with_existing(s, e):
                        continue
                    if any(s < ie and is_ < e for is_, ie, _ in inner_spans):
                        continue
                    n_tok = len(vi_tokenize(text[s:e]))
                    if 1 <= n_tok <= MAX_SPAN_TOKENS:
                        inner_spans.append((s, e, etype))

    # Lớp 1: Tìm các Inner / Satellite Spans từ INNER_PATTERNS (không chồng lấp nhau)
    for etype, rgx in INNER_PATTERNS:
        for m in rgx.finditer(sub_text):
            if m.lastindex:
                g_idx = next((gi for gi in range(1, m.lastindex + 1) if m.group(gi) is not None), 0)
                s, e = base_offset + m.start(g_idx), base_offset + m.end(g_idx)
            else:
                s, e = base_offset + m.start(), base_offset + m.end()
            while e > s and text[e - 1] in " ,.;:()":
                e -= 1
            if e <= s or conflicts_with_existing(s, e):
                continue
            if any(s < ie and is_ < e for is_, ie, _ in inner_spans):
                continue
            n_tok = len(vi_tokenize(text[s:e]))
            if etype == "THAM_CHIEU_PHAP_LY" and n_tok > MAX_SPAN_TOKENS:
                # Nếu câu căn cứ tên Luật quá dài (> 16 tokens), lược bỏ hậu tố ngày tháng năm ở cuối để vừa khung span
                trimmed = _DATE_SUFFIX_RE.sub("", text[s:e]).rstrip(" ,.;:")
                if trimmed and len(vi_tokenize(trimmed)) <= MAX_SPAN_TOKENS:
                    e = s + len(trimmed)
                    n_tok = len(vi_tokenize(text[s:e]))
            if 1 <= n_tok <= MAX_SPAN_TOKENS:
                inner_spans.append((s, e, etype))

    # Lớp 2: Mở rộng ranh giới Cụm Danh Từ Mở theo Điểm chặn Ngữ pháp (Open-Domain Syntactic Right-Boundary Chunking)
    # Giúp bắt trọn vẹn các GIAY_TO_HO_SO và TO_CHUC_DOANH_NGHIEP thuộc lĩnh vực mới chưa có từ khóa đuôi trong từ điển tĩnh
    for etype, open_rgx in _OPEN_DOMAIN_PREFIXES:
        for m in open_rgx.finditer(sub_text):
            s = base_offset + m.start()
            raw_e = base_offset + m.end()
            cand_str = text[s:raw_e]
            stop_m = _SYNTACTIC_STOP_RE.search(cand_str)
            if stop_m:
                cand_str = cand_str[:stop_m.start()]
            cand_str = cand_str.rstrip(" ,.;:!?()“”\"'-")
            e = s + len(cand_str)
            if e <= s or conflicts_with_existing(s, e):
                continue
            # Cho phép bao gọn các thực thể vệ tinh ngắn hơn nằm trọn bên trong [s, e] (VD: 'giấy phép' nằm trong 'hồ sơ đề nghị cấp giấy phép môi trường')
            blocked_by_other = False
            encl_indices = []
            for idx_isp, (is_, ie, iet) in enumerate(inner_spans):
                if s < ie and is_ < e:
                    if is_ >= s and ie <= e and (ie - is_) < (e - s) and iet in ("GIAY_TO_HO_SO", "TO_CHUC_DOANH_NGHIEP", "CHU_THE_CA_NHAN", "TAI_SAN_VAT_CHAT"):
                        encl_indices.append(idx_isp)
                    else:
                        blocked_by_other = True
                        break
            if blocked_by_other:
                continue
            n_tok = len(vi_tokenize(text[s:e]))
            if 2 <= n_tok <= min(12, MAX_SPAN_TOKENS):
                for idx_rem in reversed(encl_indices):
                    inner_spans.pop(idx_rem)
                inner_spans.append((s, e, etype))

    # Lọc NGAY_THAM_CHIEU trong inner_spans: Chỉ giữ các ngày đứng ngay sau một THAM_CHIEU_PHAP_LY
    ref_char_spans = [(s, e) for s, e, et in inner_spans if et == "THAM_CHIEU_PHAP_LY"]
    inner_spans = [
        (s, e, et)
        for s, e, et in inner_spans
        if et != "NGAY_THAM_CHIEU" or any(re_ <= s and (s - re_) <= 35 for _, re_ in ref_char_spans)
    ]

    # Bước 2: Tìm các Outer Hub Spans (HANH_VI_VI_PHAM, NGHIA_VU_QUYEN, HINH_PHAT_CHE_TAI, BIEN_PHAP_KHAC_PHUC)
    # Các Outer Hub Spans ĐƯỢC PHÉP chứa (nest) các Inner Spans bên trong!
    outer_spans = []
    for etype, rgx in OUTER_HUB_PATTERNS:
        for m in rgx.finditer(sub_text):
            if m.lastindex:
                g_idx = next((gi for gi in range(1, m.lastindex + 1) if m.group(gi) is not None), 0)
                raw_s, raw_e = base_offset + m.start(g_idx), base_offset + m.end(g_idx)
            else:
                raw_s, raw_e = base_offset + m.start(), base_offset + m.end()
            if conflicts_with_existing(raw_s, raw_e):
                continue
            clamped = _clamp_span_to_max_tokens(text, raw_s, raw_e, inner_spans, MAX_SPAN_TOKENS)
            if not clamped:
                continue
            s, e = clamped
            # Không trùng hoàn toàn với một inner span
            if any(s == is_ and e == ie for is_, ie, _ in inner_spans):
                continue
            # Không giao cắt một phần với một inner span (chỉ cho phép bao trọn hoặc tách rời)
            partial_cross = False
            for is_, ie, _ in inner_spans:
                if s < ie and is_ < e:
                    if not (is_ >= s and ie <= e):
                        partial_cross = True
                        break
            if partial_cross:
                continue
            # Các outer spans không chồng lấp lên nhau
            if any(s < oe and os_ < e for os_, oe, _ in outer_spans):
                continue
            outer_spans.append((s, e, etype))

    return outer_spans + inner_spans


def build_intra_sentence_relations(tok_spans: list):
    """
    Xây dựng đồ thị quan hệ nội câu từ danh sách `tok_spans = [(tok_start, tok_end, entity_type), ...]`.
    Tuân thủ nghiêm ngặt 18 nhãn quan hệ và `RELATION_CONSTRAINTS` trong `data/legal/schema.py`.
    """
    relations = []
    seen = set()

    def add_rel(rtype, h_idx, t_idx):
        if h_idx == t_idx:
            return
        ht = (tok_spans[h_idx][2], tok_spans[t_idx][2])
        if ht not in RELATION_CONSTRAINTS.get(rtype, set()):
            return
        key = (rtype, h_idx, t_idx)
        if key not in seen:
            seen.add(key)
            relations.append({"type": rtype, "head": h_idx, "tail": t_idx})

    def is_nested_in(inner_idx, outer_idx):
        s_in, e_in, _ = tok_spans[inner_idx]
        s_out, e_out, _ = tok_spans[outer_idx]
        return s_in >= s_out and e_in <= e_out and (s_in, e_in) != (s_out, e_out)

    n = len(tok_spans)
    nested_inner_indices = set()

    # 1. Quan hệ Lồng nhau (Outer Hub Span -> Inner Nested Span)
    for i in range(n):
        _, _, t_out = tok_spans[i]
        if t_out not in OUTER_HUB_ENTITY_TYPES:
            continue
        for j in range(n):
            if i == j:
                continue
            if is_nested_in(j, i):
                _, _, t_in = tok_spans[j]
                nested_inner_indices.add(j)
                if t_in in ("MUC_TIEN", "NGUONG_DINH_LUONG"):
                    add_rel("CO_MUC_DINH_LUONG", i, j)
                elif t_in in ("GIAY_TO_HO_SO", "TAI_SAN_VAT_CHAT"):
                    add_rel("TAC_DONG_DOI_TUONG", i, j)
                elif t_in in ("CHU_THE_CA_NHAN", "TO_CHUC_DOANH_NGHIEP", "CO_QUAN_THAM_QUYEN"):
                    add_rel("TAC_DONG_CHU_THE", i, j)
                elif t_in == "THOI_HAN":
                    add_rel("TRONG_THOI_HAN", i, j)
                elif t_in == "DIA_DIEM":
                    add_rel("DIEN_RA_TAI", i, j)
                elif t_in == "THAM_CHIEU_PHAP_LY":
                    add_rel("VIEN_DAN_THAM_CHIEU", i, j)
                elif t_in == "LINH_VUC":
                    add_rel("THUOC_LINH_VUC", i, j)

    # Phân loại các span Hub và các thực thể cấu trúc (DIEU, KHOAN, DIEM, SO_HIEU, LOAI_VAN_BAN)
    hubs_by_type = {t: [] for t in OUTER_HUB_ENTITY_TYPES}
    struct_by_type = {"DIEM": [], "KHOAN": [], "DIEU": [], "SO_HIEU": [], "LOAI_VAN_BAN": []}
    kw_indices = []
    ref_indices_all = []
    fallback_ref_heads = []
    for i, (_, _, etype) in enumerate(tok_spans):
        if etype in hubs_by_type:
            hubs_by_type[etype].append(i)
        elif etype in struct_by_type:
            struct_by_type[etype].append(i)
        elif etype == "TU_KHOA_PHAP_LY":
            kw_indices.append(i)
        elif etype == "THAM_CHIEU_PHAP_LY":
            ref_indices_all.append(i)
        elif etype in ("GIAY_TO_HO_SO", "CO_QUAN_THAM_QUYEN", "TO_CHUC_DOANH_NGHIEP", "CHU_THE_CA_NHAN"):
            fallback_ref_heads.append(i)

    # 2. Quan hệ Nhân quả Pháp lý: HANH_VI_VI_PHAM -> HINH_PHAT_CHE_TAI / BIEN_PHAP_KHAC_PHUC
    for v_idx in hubs_by_type["HANH_VI_VI_PHAM"]:
        for p_idx in hubs_by_type["HINH_PHAT_CHE_TAI"] + hubs_by_type["BIEN_PHAP_KHAC_PHUC"]:
            add_rel("DAN_DEN_CHE_TAI", v_idx, p_idx)

    # 3. Quan hệ Chủ thể / Thẩm quyền -> Hub
    for i, (s_i, e_i, etype) in enumerate(tok_spans):
        if i in nested_inner_indices:
            continue

        if etype in ("CHU_THE_CA_NHAN", "TO_CHUC_DOANH_NGHIEP"):
            if hubs_by_type["HANH_VI_VI_PHAM"]:
                v_idx = min(hubs_by_type["HANH_VI_VI_PHAM"], key=lambda k: abs(tok_spans[k][0] - s_i))
                add_rel("THUC_HIEN_VI_PHAM", i, v_idx)
            elif hubs_by_type["NGHIA_VU_QUYEN"]:
                o_idx = min(hubs_by_type["NGHIA_VU_QUYEN"], key=lambda k: abs(tok_spans[k][0] - s_i))
                if s_i <= tok_spans[o_idx][0]:
                    add_rel("CO_NGHIA_VU_QUYEN", i, o_idx)
                else:
                    add_rel("TAC_DONG_CHU_THE", o_idx, i)
            elif hubs_by_type["HINH_PHAT_CHE_TAI"] or hubs_by_type["BIEN_PHAP_KHAC_PHUC"]:
                for p_idx in hubs_by_type["HINH_PHAT_CHE_TAI"] + hubs_by_type["BIEN_PHAP_KHAC_PHUC"]:
                    add_rel("CHIU_CHE_TAI", i, p_idx)

        elif etype == "CO_QUAN_THAM_QUYEN":
            target_hubs = hubs_by_type["HINH_PHAT_CHE_TAI"] + hubs_by_type["BIEN_PHAP_KHAC_PHUC"] + hubs_by_type["NGHIA_VU_QUYEN"]
            for h_idx in target_hubs:
                if s_i <= tok_spans[h_idx][0]:
                    add_rel("CO_THAM_QUYEN", i, h_idx)
                else:
                    add_rel("TAC_DONG_CHU_THE", h_idx, i)

    # 4. Quan hệ từ Hub (hoặc Điều/Khoản/Điểm/Số hiệu/Từ khóa pháp lý) tới các Thực thể Bối cảnh / Định lượng / Đối chiếu đứng bên ngoài Hub
    all_hubs = (
        hubs_by_type["HANH_VI_VI_PHAM"]
        + hubs_by_type["NGHIA_VU_QUYEN"]
        + hubs_by_type["HINH_PHAT_CHE_TAI"]
        + hubs_by_type["BIEN_PHAP_KHAC_PHUC"]
    )
    non_penalty_hubs = (
        hubs_by_type["HANH_VI_VI_PHAM"]
        + hubs_by_type["NGHIA_VU_QUYEN"]
        + hubs_by_type["BIEN_PHAP_KHAC_PHUC"]
    )
    primary_struct_idx = (
        struct_by_type["DIEM"][0]
        if struct_by_type["DIEM"]
        else (
            struct_by_type["KHOAN"][0]
            if struct_by_type["KHOAN"]
            else (
                struct_by_type["DIEU"][0]
                if struct_by_type["DIEU"]
                else (
                    struct_by_type["SO_HIEU"][0]
                    if struct_by_type["SO_HIEU"]
                    else (struct_by_type["LOAI_VAN_BAN"][0] if struct_by_type["LOAI_VAN_BAN"] else None)
                )
            )
        )
    )

    for j, (s_j, e_j, etype) in enumerate(tok_spans):
        if etype in OUTER_HUB_ENTITY_TYPES:
            continue
        if etype == "THAM_CHIEU_PHAP_LY":
            # Liên kết từ TU_KHOA_PHAP_LY đứng gần nhất phía trước (nếu có)
            preceding_kws = [k_idx for k_idx in kw_indices if tok_spans[k_idx][1] <= s_j]
            if preceding_kws:
                best_kw = max(preceding_kws, key=lambda k: tok_spans[k][1])
                add_rel("VIEN_DAN_THAM_CHIEU", best_kw, j)
            if j in nested_inner_indices:
                continue
            # Đồng thời liên kết với Hub hoặc Đơn vị cấu trúc của câu
            if all_hubs:
                nearest_hub = min(all_hubs, key=lambda k: abs(tok_spans[k][0] - s_j))
                add_rel("VIEN_DAN_THAM_CHIEU", nearest_hub, j)
            elif primary_struct_idx is not None:
                add_rel("VIEN_DAN_THAM_CHIEU", primary_struct_idx, j)
            elif fallback_ref_heads:
                nearest_fb = min(fallback_ref_heads, key=lambda k: abs(tok_spans[k][0] - s_j))
                add_rel("VIEN_DAN_THAM_CHIEU", nearest_fb, j)
        elif etype == "LINH_VUC":
            # Liên kết từ THAM_CHIEU_PHAP_LY đứng gần nhất phía trước (khi lĩnh vực mô tả văn bản tham chiếu)
            preceding_refs = [r_idx for r_idx in ref_indices_all if tok_spans[r_idx][1] <= s_j and (s_j - tok_spans[r_idx][1]) <= 25]
            if preceding_refs:
                best_ref = max(preceding_refs, key=lambda k: tok_spans[k][1])
                add_rel("THUOC_LINH_VUC", best_ref, j)
            # Đồng thời liên kết với SO_HIEU / Đơn vị cấu trúc / Hub của câu
            if struct_by_type["SO_HIEU"]:
                add_rel("THUOC_LINH_VUC", struct_by_type["SO_HIEU"][0], j)
            if j in nested_inner_indices:
                continue
            if all_hubs:
                nearest_hub = min(all_hubs, key=lambda k: abs(tok_spans[k][0] - s_j))
                add_rel("THUOC_LINH_VUC", nearest_hub, j)
            elif primary_struct_idx is not None:
                add_rel("THUOC_LINH_VUC", primary_struct_idx, j)
            elif fallback_ref_heads:
                nearest_fb = min(fallback_ref_heads, key=lambda k: abs(tok_spans[k][0] - s_j))
                add_rel("THUOC_LINH_VUC", nearest_fb, j)
        elif j not in nested_inner_indices and all_hubs:
            nearest_hub = min(all_hubs, key=lambda k: abs(tok_spans[k][0] - s_j))
            if etype in ("GIAY_TO_HO_SO", "TAI_SAN_VAT_CHAT"):
                target_h = min(non_penalty_hubs, key=lambda k: abs(tok_spans[k][0] - s_j)) if non_penalty_hubs else nearest_hub
                add_rel("TAC_DONG_DOI_TUONG", target_h, j)
            elif etype == "MUC_TIEN":
                pen_hub = hubs_by_type["HINH_PHAT_CHE_TAI"][0] if hubs_by_type["HINH_PHAT_CHE_TAI"] else nearest_hub
                add_rel("CO_MUC_DINH_LUONG", pen_hub, j)
            elif etype == "NGUONG_DINH_LUONG":
                target_h = min(non_penalty_hubs, key=lambda k: abs(tok_spans[k][0] - s_j)) if non_penalty_hubs else nearest_hub
                add_rel("CO_MUC_DINH_LUONG", target_h, j)
            elif etype == "THOI_HAN":
                target_h = min(non_penalty_hubs, key=lambda k: abs(tok_spans[k][0] - s_j)) if non_penalty_hubs else nearest_hub
                add_rel("TRONG_THOI_HAN", target_h, j)
            elif etype == "DIA_DIEM":
                target_h = min(non_penalty_hubs, key=lambda k: abs(tok_spans[k][0] - s_j)) if non_penalty_hubs else nearest_hub
                add_rel("DIEN_RA_TAI", target_h, j)

    # 5. Quan hệ Ngày ban hành của văn bản tham chiếu: THAM_CHIEU_PHAP_LY -> NGAY_THAM_CHIEU
    refs_indices = [i for i, (_, _, et) in enumerate(tok_spans) if et == "THAM_CHIEU_PHAP_LY"]
    dates_indices = [j for j, (_, _, et) in enumerate(tok_spans) if et == "NGAY_THAM_CHIEU"]
    for d_idx in dates_indices:
        s_d = tok_spans[d_idx][0]
        # Tìm THAM_CHIEU_PHAP_LY ngay trước hoặc gần nhất trước NGAY_THAM_CHIEU (trong khoảng 6 token)
        cand_refs = [r_idx for r_idx in refs_indices if tok_spans[r_idx][1] <= s_d and (s_d - tok_spans[r_idx][1]) <= 6]
        if cand_refs:
            best_ref = max(cand_refs, key=lambda k: tok_spans[k][1])
            add_rel("NGAY_BAN_HANH_THAM_CHIEU", best_ref, d_idx)

    return relations

