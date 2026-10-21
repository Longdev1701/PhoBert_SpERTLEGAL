"""
Tach tu tieng Viet dung chung cho xay dung du lieu VA suy luan (bat buoc dung cung 1 ham).
- Giu nguyen ma so hieu van ban (vd: 44/2007/NĐ-CP, 15/CP) thanh 1 token duy nhat
  thay vi de PyVi cat thanh '44 / 2007 / NĐ - CP'.
"""
import re
from pyvi import ViTokenizer

# Chuoi bat dau bang chu so va co chua '/' -> ma so hieu (vd 05/2006/TT-BCA, 101/2023/QH15, 15/CP)
_CODE_RE = re.compile(r"(?<!\w)\d+[\w\.\-]*/[\w/\.\-]*\w")


def vi_tokenize(text):
    tokens, cur = [], 0
    for m in _CODE_RE.finditer(text):
        seg = text[cur:m.start()].strip()
        if seg:
            tokens += ViTokenizer.tokenize(seg).split()
        tokens.append(m.group(0))
        cur = m.end()
    seg = text[cur:].strip()
    if seg:
        tokens += ViTokenizer.tokenize(seg).split()
    return tokens
