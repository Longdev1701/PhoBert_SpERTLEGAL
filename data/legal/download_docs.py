"""
Buoc 1: Tai mau van ban tu Google Drive.

Chi lay: thuoc_tinh.json, muc_luc.json, noi_dung.docx
Chi lay nhom: nghi_dinh, thong_tu, quyet_dinh; nam ban hanh >= 2006 (doc tu ten thu muc).

Chay:  python -m data.legal.download_docs --per-category 35
Ket qua: data/legal/raw/<nhom>/<ten_van_ban>/...
"""
import os
import re
import json
import random
import argparse
import time

from data.legal.drive_client import ROOT_FOLDER_ID, list_folder, download
from data.legal.schema import SELECTED_CATEGORIES, MIN_YEAR

WANTED_FILES = ["thuoc_tinh.json", "muc_luc.json", "noi_dung.docx"]
RAW_DIR = os.path.join(os.path.dirname(__file__), "raw")


def doc_year(name):
    m = re.search(r"_((?:19|20)\d{2})_", name)
    return int(m.group(1)) if m else None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--per-category", type=int, default=35)
    ap.add_argument("--seed", type=int, default=42)
    args = ap.parse_args()
    random.seed(args.seed)

    root = list_folder(ROOT_FOLDER_ID)
    if root is None:
        raise SystemExit("Khong doc duoc thu muc goc tren Drive.")
    cats = {name: fid for fid, name, is_folder in root if is_folder}

    manifest = []
    for cat in SELECTED_CATEGORIES:
        docs = list_folder(cats[cat]) or []
        eligible = [(i, n) for i, n, f in docs if f and (doc_year(n) or 0) >= MIN_YEAR]
        random.shuffle(eligible)
        print(f"[{cat}] {len(docs)} van ban, {len(eligible)} van ban >= {MIN_YEAR}")

        got = 0
        for did, dname in eligible:
            if got >= args.per_category:
                break
            time.sleep(0.4)
            files = list_folder(did)
            if not files:
                continue
            fmap = {n: i for i, n, _ in files}
            # Bat buoc co thuoc_tinh + noi_dung; muc_luc la tuy chon (co fallback)
            if "thuoc_tinh.json" not in fmap or "noi_dung.docx" not in fmap:
                continue
            out_dir = os.path.join(RAW_DIR, cat, dname)
            ok = True
            for fn in WANTED_FILES:
                if fn in fmap:
                    ok &= download(fmap[fn], os.path.join(out_dir, fn))
            if not ok:
                print(f"   [!] Loi tai {dname}")
                continue
            got += 1
            manifest.append({"category": cat, "doc": dname, "folder_id": did,
                             "has_muc_luc": "muc_luc.json" in fmap})
            print(f"   ({got}/{args.per_category}) {dname}", flush=True)

    os.makedirs(RAW_DIR, exist_ok=True)
    with open(os.path.join(RAW_DIR, "manifest.json"), "w", encoding="utf-8") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=1)
    print(f"[OK] Da tai {len(manifest)} van ban -> {RAW_DIR}")


if __name__ == "__main__":
    main()
