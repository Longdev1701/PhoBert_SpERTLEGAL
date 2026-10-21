"""
Script kiểm thử tự động toàn bộ 9 văn bản thực tế bằng mô hình PhoBERT-SpERT tối ưu nhất.
Mô hình chỉ nạp 1 lần duy nhất vào bộ nhớ GPU để tối đa hóa tốc độ suy luận.
Kết quả từng văn bản được lưu thành .md và .html tương tác trong thư mục outputs/.
"""
import os
import sys
import time
import json
import torch

from test_drive_document import LegalExtractor, process_single_document

DOCUMENTS = [
    ("01_2006_QĐ-BTM_16773", "Quyết định Bộ Thương mại"),
    ("07_2025_QĐ-KTNN_175504", "Quyết định Kiểm toán Nhà nước"),
    ("133_2009_QĐ-TTg_23839", "Quyết định Thủ tướng Chính phủ"),
    ("101_2008_TT-BTC_23888", "Thông tư Bộ Tài chính"),
    ("01_2009_TT-BNV_12219", "Thông tư Bộ Nội vụ"),
    ("06_2017_TT-NHNN_122819", "Thông tư Ngân hàng Nhà nước"),
    ("107_2011_NĐ-CP_27184", "Nghị định Xử phạt Lĩnh vực Năng lượng Nguyên tử"),
    ("04_2013_NĐ-CP_28054", "Nghị định Quản lý Phát triển Đô thị"),
    ("306_2025_NĐ-CP_186388", "Nghị định Xử phạt Vi phạm Hành chính Chứng khoán"),
]

def main():
    print("=" * 80)
    print("CHƯƠNG TRÌNH KIỂM THỬ TOÀN BỘ VĂN BẢN THỰC TẾ (BATCH REAL-DOCUMENT INFERENCE)")
    print(f"Tổng số văn bản cần xử lý: {len(DOCUMENTS)}")
    print(f"Mô hình sử dụng: checkpoints/best_spert_phobert.pt")
    print(f"Thiết bị: {'cuda' if torch.cuda.is_available() else 'cpu'}")
    print("=" * 80)

    # 1. Nạp extractor 1 lần duy nhất
    t_load_start = time.time()
    extractor = LegalExtractor(checkpoint_path="checkpoints/best_spert_phobert.pt")
    print(f"[+] Đã nạp mô hình vào GPU thành công trong {time.time() - t_load_start:.2f} giây!\n")

    summary_results = []
    total_start_time = time.time()

    for idx, (doc_name, doc_desc) in enumerate(DOCUMENTS, 1):
        print("\n" + "#" * 80)
        print(f"[{idx}/{len(DOCUMENTS)}] BẮT ĐẦU PHÂN TÍCH: {doc_name} ({doc_desc})")
        print("#" * 80)

        t_doc_start = time.time()
        try:
            res = process_single_document(
                doc_name=doc_name,
                extractor=extractor,
            )
            res["description"] = doc_desc
            summary_results.append(res)
            print(f"[SUCCESS] {doc_name} | {res['num_paras']} đoạn | {res['num_entities']} thực thể | {res['num_relations']} quan hệ | {res['inference_time']:.1f}s")
        except Exception as e:
            print(f"[ERROR] Thất bại khi xử lý {doc_name}: {e}")
            import traceback
            traceback.print_exc()

    total_time = time.time() - total_start_time

    # Lưu file thống kê tổng hợp JSON
    summary_path = os.path.join("outputs", "summary_real_documents_test.json")
    with open(summary_path, "w", encoding="utf-8") as f:
        json.dump({
            "total_documents": len(summary_results),
            "total_time_seconds": round(total_time, 2),
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
            "results": summary_results
        }, f, ensure_ascii=False, indent=2)

    # In bảng tổng kết ra màn hình
    print("\n" + "=" * 90)
    print("BẢNG TỔNG HỢP KẾT QUẢ KIỂM THỬ THỰC TẾ TRÊN 9 VĂN BẢN")
    print("=" * 90)
    print(f"{'STT':<4} | {'Tên Văn Bản':<30} | {'Số Đoạn':<8} | {'Thực Thể':<10} | {'Quan Hệ':<10} | {'Thời Gian':<10}")
    print("-" * 90)
    total_paras = sum(r["num_paras"] for r in summary_results)
    total_ents = sum(r["num_entities"] for r in summary_results)
    total_rels = sum(r["num_relations"] for r in summary_results)

    for i, r in enumerate(summary_results, 1):
        print(f"{i:<4} | {r['doc_name']:<30} | {r['num_paras']:<8} | {r['num_entities']:<10} | {r['num_relations']:<10} | {r['inference_time']:<8.1f}s")
    print("-" * 90)
    print(f"{'TỔNG':<4} | {f'{len(summary_results)} văn bản':<30} | {total_paras:<8} | {total_ents:<10} | {total_rels:<10} | {total_time:<8.1f}s")
    print("=" * 90)
    print(f"[*] Đã lưu bảng thống kê tổng hợp tại: {summary_path}")

if __name__ == "__main__":
    main()
