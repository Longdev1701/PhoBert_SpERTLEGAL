"""
Client toi gian de doc thu muc Google Drive cong khai (khong can API key).
- list_folder: dung trang embeddedfolderview (1 tang, khong de quy -> tranh bi chan 500).
- download: tai file qua uc?export=download, co cache tren dia.
"""
import os
import re
import html
import time
import requests

ROOT_FOLDER_ID = "1yR_MSNjIuHuzN5oL7PyOpBrHmOUWigOr"

_session = requests.Session()
_session.headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"

_ENTRY_RE = re.compile(
    r'<div class="flip-entry" id="entry-([^"]+)".*?<a href="([^"]+)".*?'
    r'<div class="flip-entry-title">(.*?)</div>',
    re.S,
)


def _get(url, retries=4, timeout=60):
    for attempt in range(retries):
        try:
            r = _session.get(url, timeout=timeout)
            if r.status_code == 200:
                return r
            if r.status_code in (429, 500, 503):
                time.sleep(2 ** attempt * 2)
                continue
            return None
        except requests.RequestException:
            time.sleep(2 ** attempt)
    return None


def list_folder(folder_id):
    """Tra ve list (id, name, is_folder) cua 1 thu muc (1 tang)."""
    r = _get(f"https://drive.google.com/embeddedfolderview?id={folder_id}")
    if r is None:
        return None
    items = []
    for m in _ENTRY_RE.finditer(r.text):
        iid, href, name = m.group(1), m.group(2), html.unescape(m.group(3))
        items.append((iid, name, "/folders/" in href))
    return items


def download(file_id, dest_path, sleep=0.3):
    """Tai file ve dest_path (bo qua neu da co). Tra ve True neu thanh cong."""
    if os.path.exists(dest_path) and os.path.getsize(dest_path) > 0:
        return True
    r = _get(f"https://drive.google.com/uc?export=download&id={file_id}")
    if r is None or not r.content:
        return False
    # Drive tra ve trang HTML canh bao virus voi file lon -> coi nhu that bai
    if r.headers.get("Content-Type", "").startswith("text/html"):
        return False
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    with open(dest_path, "wb") as f:
        f.write(r.content)
    time.sleep(sleep)
    return True
