"""
Tap lenh Huan luyen Mo hinh Joint Entity and Relation Extraction (PhoBERT-SpERT)
tren Tap du lieu Quy pham Phap luat Viet Nam (Legal NLP Dataset).

Toi uu hoa:
  - GPU: NVIDIA GeForce RTX 2050 Laptop GPU (4GB VRAM)
  - Mixed Precision FP16 (torch.amp.autocast)
  - Gradient Accumulation (effective batch size = 8)
  - NMS (Non-Maximum Suppression) trong danh gia dev/test
  - Strict Evaluation (ACL/EMNLP metric: precision, recall, f1)
  - Tu dong luu checkpoint tot nhat dua tren Validation F1 score
"""
import os
import sys
import time
import json
import math
import random
import ctypes
import argparse
import torch
import torch.nn as nn
from torch.utils.data import DataLoader
from transformers import AutoTokenizer, get_linear_schedule_with_warmup

def prevent_system_sleep():
    """Ngăn Windows tự động đi vào trạng thái Sleep/Suspend khi đang huấn luyện."""
    try:
        if sys.platform == "win32":
            ES_CONTINUOUS = 0x80000000
            ES_SYSTEM_REQUIRED = 0x00000001
            ctypes.windll.kernel32.SetThreadExecutionState(ES_CONTINUOUS | ES_SYSTEM_REQUIRED)
            print("[*] Đã kích hoạt chế độ chống Windows Sleep trong suốt quá trình huấn luyện.")
    except Exception:
        pass

def restore_system_sleep():
    """Khôi phục chế độ quản lý nguồn bình thường của Windows sau khi hoàn tất."""
    try:
        if sys.platform == "win32":
            ES_CONTINUOUS = 0x80000000
            ctypes.windll.kernel32.SetThreadExecutionState(ES_CONTINUOUS)
    except Exception:
        pass


from models.spert_phobert import PhoBERTSpeRT
from data.dataset import SpERTDataset, spert_collate_fn, load_spert_samples, generate_candidate_spans
from utils.evaluation import compute_metrics


def save_checkpoint(path, epoch, model, optimizer, scheduler, scaler, best_dev_f1, joint_f1, dev_metrics, entity_types, relation_types):
    """Lưu an toàn checkpoint với atomic write (ghi file tạm rồi đổi tên) chống hỏng file khi tắt máy đột ngột."""
    os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
    tmp_path = path + ".tmp"
    state = {
        "epoch": epoch,
        "model_state_dict": model.state_dict(),
        "optimizer_state_dict": optimizer.state_dict(),
        "scheduler_state_dict": scheduler.state_dict() if scheduler else None,
        "scaler_state_dict": scaler.state_dict() if scaler else None,
        "best_dev_f1": best_dev_f1,
        "joint_f1": joint_f1,
        "dev_metrics": dev_metrics,
        "entity_types": entity_types,
        "relation_types": relation_types,
        "torch_rng_state": torch.get_rng_state().cpu(),
        "cuda_rng_state": torch.cuda.get_rng_state().cpu() if torch.cuda.is_available() else None,
        "random_state": random.getstate(),
    }
    torch.save(state, tmp_path)
    if os.path.exists(path):
        os.replace(tmp_path, path)
    else:
        os.rename(tmp_path, path)


STRUCT_CONTAINER_SET = {"CHUONG", "DIEU", "KHOAN", "DIEM"}
OUTER_HUB_SET = {"HANH_VI_VI_PHAM", "NGHIA_VU_QUYEN", "HINH_PHAT_CHE_TAI", "BIEN_PHAP_KHAC_PHUC"}


def _nest_level(ent_type: str) -> int:
    if ent_type == "CHUONG":
        return 3
    if ent_type in {"DIEU", "KHOAN", "DIEM"}:
        return 2
    if ent_type in OUTER_HUB_SET:
        return 1
    return 0


def non_max_suppression(entities):
    """
    3-Level Nested-Aware NMS:
      - Cấp 2 (Khung cấu trúc): DIEU, KHOAN, DIEM (bao trọn toàn bộ nội dung điều/khoản/điểm).
      - Cấp 1 (Thực thể trung tâm - Outer Hubs): HANH_VI_VI_PHAM, NGHIA_VU_QUYEN, HINH_PHAT_CHE_TAI, BIEN_PHAP_KHAC_PHUC.
      - Cấp 0 (Thực thể vệ tinh - Inner Satellites): CHU_THE_CA_NHAN, TO_CHUC_DOANH_NGHIEP, MUC_TIEN, THAM_CHIEU_PHAP_LY...
      - Cho phép thực thể cấp thấp hơn nằm lồng hoàn toàn bên trong thực thể cấp cao hơn.
    """
    sorted_ents = sorted(entities, key=lambda x: x["confidence"], reverse=True)
    selected = []
    for ent in sorted_ents:
        s1, e1 = ent["span"]
        t1 = ent.get("type", "")
        lvl1 = _nest_level(t1)
        conflict = False
        for kept in selected:
            s2, e2 = kept["span"]
            t2 = kept.get("type", "")
            lvl2 = _nest_level(t2)
            if (s1, e1) == (s2, e2):
                conflict = True
                break
            if max(s1, s2) < min(e1, e2):
                is_valid_nest = (
                    (lvl1 > lvl2 and s2 >= s1 and e2 <= e1)
                    or (lvl2 > lvl1 and s1 >= s2 and e1 <= e2)
                )
                if not is_valid_nest:
                    conflict = True
                    break
        if not conflict:
            selected.append(ent)
    return sorted(selected, key=lambda x: (x["span"][0], -x["span"][1]))


def evaluate_model(model, source_path, tokenizer, device, max_span_length=110, ent_thresh=0.35, rel_thresh=0.50, split=None):
    """
    Danh gia chat che (Strict Evaluation) mo hinh tren tap du lieu (Dev hoac Test).
    """
    model.eval()
    gold_samples = load_spert_samples(source_path, split=split)

    # Nhan thuc the va quan he
    entity_types = model.entity_types if hasattr(model, "entity_types") else []
    relation_types = model.relation_types if hasattr(model, "relation_types") else []
    id2entity = {i + 1: t for i, t in enumerate(entity_types)}
    id2rel = {i + 1: t for i, t in enumerate(relation_types)}

    pred_samples = []

    with torch.no_grad():
        for sample in gold_samples:
            words = sample["tokens"]
            num_words = len(words)
            if num_words == 0:
                pred_samples.append({"entities": [], "relations": []})
                continue

            # Anh xa word sang subword
            subword_ids = [tokenizer.bos_token_id]
            word_to_subword = []
            for word in words:
                tokens = tokenizer.encode(word, add_special_tokens=False)
                if not tokens:
                    tokens = [tokenizer.unk_token_id]
                start_idx = len(subword_ids)
                subword_ids.extend(tokens)
                end_idx = len(subword_ids)
                word_to_subword.append((start_idx, end_idx))
            subword_ids.append(tokenizer.eos_token_id)

            input_ids = torch.tensor([subword_ids], dtype=torch.long, device=device)
            attention_mask = torch.ones_like(input_ids, device=device)

            # Tao candidate spans toi uu (1..17 day du + 18..max_span_length cho DIEU/KHOAN/DIEM)
            candidate_word_spans = generate_candidate_spans(words, max_span_length)
            subword_spans = []
            span_lengths = []
            for w_start, w_end in candidate_word_spans:
                sw_start = word_to_subword[w_start][0]
                sw_end = word_to_subword[w_end - 1][1]
                subword_spans.append((sw_start, sw_end))
                span_lengths.append(w_end - w_start)

            if not subword_spans:
                pred_samples.append({"entities": [], "relations": []})
                continue

            spans_tensor = torch.tensor([subword_spans], dtype=torch.long, device=device)
            lengths_tensor = torch.tensor([span_lengths], dtype=torch.long, device=device)

            with torch.amp.autocast('cuda' if torch.cuda.is_available() else 'cpu'):
                outputs = model(
                    input_ids=input_ids,
                    attention_mask=attention_mask,
                    spans=spans_tensor,
                    span_lengths=lengths_tensor
                )
                ent_logits = outputs["entity_logits"][0]
                ent_probs = torch.softmax(ent_logits, dim=-1)

            # Loc thuc the (vector hoa tren GPU, tranh goi .item() trong vong lap)
            non_none_probs = ent_probs[:, 1:]
            max_probs, best_cls_offsets = torch.max(non_none_probs, dim=-1)
            keep_mask = max_probs >= ent_thresh
            keep_indices = torch.nonzero(keep_mask, as_tuple=False).squeeze(-1).detach().cpu().tolist()
            if isinstance(keep_indices, int):
                keep_indices = [keep_indices]
            max_probs_cpu = max_probs.detach().cpu().tolist()
            best_cls_cpu = best_cls_offsets.detach().cpu().tolist()

            raw_entities = []
            for idx in keep_indices:
                w_start, w_end = candidate_word_spans[idx]
                best_cls = best_cls_cpu[idx] + 1
                conf = max_probs_cpu[idx]
                ent_type = id2entity.get(best_cls, "UNKNOWN")
                raw_entities.append({
                    "span_idx": idx,
                    "type": ent_type,
                    "start": w_start,
                    "end": w_end,
                    "span": (w_start, w_end),
                    "confidence": conf
                })

            detected_entities = non_max_suppression(raw_entities)
            if len(detected_entities) > 40:
                detected_entities = sorted(detected_entities, key=lambda x: x["confidence"], reverse=True)[:40]
                detected_entities = sorted(detected_entities, key=lambda x: (x["span"][0], -x["span"][1]))

            # Du doan quan he voi Sigmoid doc lap tren tung lop (Nang cap 3 - BCEWithLogitsLoss)
            detected_relations = []
            if len(detected_entities) >= 2:
                rel_pairs = []
                pair_idx_map = []
                for i, e1 in enumerate(detected_entities):
                    for j, e2 in enumerate(detected_entities):
                        if i != j:
                            rel_pairs.append((e1["span_idx"], e2["span_idx"]))
                            pair_idx_map.append((i, j))

                if rel_pairs:
                    rel_pairs_tensor = torch.tensor([rel_pairs], dtype=torch.long, device=device)
                    with torch.amp.autocast('cuda' if torch.cuda.is_available() else 'cpu'):
                        rel_outputs = model(
                            input_ids=input_ids,
                            attention_mask=attention_mask,
                            spans=spans_tensor,
                            span_lengths=lengths_tensor,
                            rel_pairs=rel_pairs_tensor
                        )
                        rel_logits = rel_outputs["relation_logits"][0]  # (Num_Pairs, |R|)
                        rel_probs = torch.sigmoid(rel_logits)           # (Num_Pairs, |R|)

                    pos_coords = torch.nonzero(rel_probs >= rel_thresh, as_tuple=False).detach().cpu().tolist()
                    rel_probs_cpu = rel_probs.detach().cpu().tolist()
                    for p_idx, r_offset in pos_coords:
                        head_idx, tail_idx = pair_idx_map[p_idx]
                        conf = rel_probs_cpu[p_idx][r_offset]
                        best_r_cls = r_offset + 1
                        rel_type = id2rel.get(best_r_cls, "UNKNOWN")
                        detected_relations.append({
                            "type": rel_type,
                            "head": head_idx,
                            "tail": tail_idx,
                            "confidence": conf
                        })

            pred_samples.append({
                "entities": [{"type": e["type"], "start": e["start"], "end": e["end"]} for e in detected_entities],
                "relations": detected_relations
            })

    metrics = compute_metrics(gold_samples, pred_samples)
    return metrics


def train_spert():
    parser = argparse.ArgumentParser(description="Huấn luyện mô hình PhoBERT-SpERT có lưu Checkpoint và tự động Resume khi tắt máy.")
    parser.add_argument("--epochs", type=int, default=5, help="Tổng số epoch huấn luyện (mặc định: 5)")
    parser.add_argument("--batch_size", "--batch-size", dest="batch_size", type=int, default=2, help="Kích thước batch (mặc định: 2)")
    parser.add_argument("--grad_accum", "--grad-accum", dest="grad_accum", type=int, default=4, help="Gradient accumulation steps (mặc định: 4)")
    parser.add_argument("--max_span_size", "--max-span-size", dest="max_span_size", type=int, default=110, help="Độ dài span tối đa (mặc định: 110)")
    parser.add_argument("--lr_phobert", type=float, default=2e-5, help="Learning rate PhoBERT backbone (mặc định: 2e-5)")
    parser.add_argument("--lr_heads", type=float, default=5e-4, help="Learning rate SpERT classifier heads (mặc định: 5e-4)")
    parser.add_argument("--checkpoint_dir", type=str, default="checkpoints", help="Thư mục lưu checkpoints (mặc định: checkpoints)")
    parser.add_argument("--no_resume", action="store_true", help="Không tự động resume từ last_checkpoint.pt, bắt đầu train lại từ Epoch 1")
    args = parser.parse_args()

    # 1. Thiết lập thiết bị và siêu tham số
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    gpu_name = torch.cuda.get_device_name(0) if torch.cuda.is_available() else 'CPU'
    print("=" * 70)
    print(f"[*] THIẾT BỊ HUẤN LUYỆN: {device} ({gpu_name})")
    print(f"[*] CẤU HÌNH: Epochs={args.epochs}, BatchSize={args.batch_size}, GradAccum={args.grad_accum} (Effective BS = {args.batch_size * args.grad_accum}), MaxSpan={args.max_span_size}")
    print(f"[*] CHECKPOINT DIR: {args.checkpoint_dir} (Tự động resume: {'BẬT' if not args.no_resume else 'TẮT'})")
    print("=" * 70)

    epochs = args.epochs
    batch_size = args.batch_size
    gradient_accumulation_steps = args.grad_accum
    lr_phobert = args.lr_phobert
    lr_heads = args.lr_heads
    max_span_length = args.max_span_size
    rel_loss_weight = 1.0

    # 2. Tokenizer & Dataset
    model_name = "vinai/phobert-base-v2"
    print(f"[*] Đang nạp Tokenizer từ: {model_name}...")
    tokenizer = AutoTokenizer.from_pretrained(model_name)

    train_json_path = "data/legal/processed/train.json"
    by_doc_dir = "data/legal/processed/by_doc_spert"
    data_source = train_json_path if os.path.exists(train_json_path) else by_doc_dir

    print(f"[*] Nạp tập dữ liệu Huấn luyện từ: {data_source} (split=TRAIN)")
    train_dataset = SpERTDataset(
        json_file=data_source,
        tokenizer=tokenizer,
        max_span_length=max_span_length,
        neg_entity_count=40,
        neg_relation_count=40,
        split="train" if data_source == by_doc_dir else None,
    )
    dataloader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True, collate_fn=spert_collate_fn)

    entity_types = train_dataset.entity_types
    relation_types = train_dataset.relation_types
    print(f"[*] Schema Thực thể ({len(entity_types)}): {entity_types}")
    print(f"[*] Schema Quan hệ ({len(relation_types)}): {relation_types}")
    print(f"[*] Số lượng mẫu huấn luyện: {len(train_dataset)} mẫu ({len(dataloader)} batches/epoch)")

    # 3. Khởi tạo mô hình PhoBERT-SpERT
    print("[*] Khởi tạo mô hình PhoBERTSpeRT...")
    model = PhoBERTSpeRT(
        model_name=model_name,
        num_entity_types=len(entity_types),
        num_relation_types=len(relation_types),
        max_span_length=max_span_length,
        size_embedding_dim=25,
        dropout_rate=0.1
    ).to(device)

    model.entity_types = entity_types
    model.relation_types = relation_types

    # 4. Thiết lập Optimizer & Scheduler
    phobert_params = [p for n, p in model.named_parameters() if "phobert" in n and p.requires_grad]
    head_params = [p for n, p in model.named_parameters() if "phobert" not in n and p.requires_grad]

    optimizer = torch.optim.AdamW([
        {"params": phobert_params, "lr": lr_phobert, "weight_decay": 0.01},
        {"params": head_params, "lr": lr_heads, "weight_decay": 0.001}
    ])

    total_steps = (len(dataloader) // gradient_accumulation_steps + 1) * epochs
    scheduler = get_linear_schedule_with_warmup(
        optimizer,
        num_warmup_steps=int(total_steps * 0.1),
        num_training_steps=total_steps
    )

    # 5. Hàm mất mát: CrossEntropyLoss cho Entity, BCEWithLogitsLoss cho Relation (Nâng cấp 3)
    ent_weights = torch.tensor([0.2] + [1.0] * len(entity_types), device=device)
    rel_pos_weight = torch.full((len(relation_types),), 3.0, device=device)
    entity_criterion = nn.CrossEntropyLoss(weight=ent_weights, ignore_index=-100)
    relation_criterion = nn.BCEWithLogitsLoss(pos_weight=rel_pos_weight, reduction="none")

    scaler = torch.amp.GradScaler('cuda') if torch.cuda.is_available() else None

    # Checkpoint paths
    os.makedirs(args.checkpoint_dir, exist_ok=True)
    best_checkpoint_path = os.path.join(args.checkpoint_dir, "best_spert_phobert.pt")
    last_checkpoint_path = os.path.join(args.checkpoint_dir, "last_checkpoint.pt")

    start_epoch = 1
    best_dev_f1 = -1.0

    # 6. Kiểm tra và khôi phục từ Checkpoint (Resume) nếu có
    if (not args.no_resume) and os.path.exists(last_checkpoint_path):
        print("\n" + "=" * 70)
        print(f"[*] PHÁT HIỆN CHECKPOINT TRƯỚC ĐÓ: {last_checkpoint_path}")
        try:
            chk = torch.load(last_checkpoint_path, map_location=device)
            chk_ents = chk.get("entity_types", [])
            chk_rels = chk.get("relation_types", [])
            if chk_ents != entity_types or chk_rels != relation_types:
                print(f"[!] Hệ nhãn trong checkpoint ({len(chk_ents)} thực thể, {len(chk_rels)} quan hệ) khác với hiện tại ({len(entity_types)} thực thể, {len(relation_types)} quan hệ).")
                print("[*] Sẽ bắt đầu huấn luyện mới từ Epoch 1 với Warm-start trọng số tương thích.")
                start_epoch = 1
                best_dev_f1 = -1.0
            else:
                saved_epoch = chk["epoch"]
                start_epoch = saved_epoch + 1
                best_dev_f1 = chk.get("best_dev_f1", chk.get("joint_f1", -1.0))
                model.load_state_dict(chk["model_state_dict"])
                optimizer.load_state_dict(chk["optimizer_state_dict"])
                if "scheduler_state_dict" in chk and chk["scheduler_state_dict"] is not None:
                    scheduler.load_state_dict(chk["scheduler_state_dict"])
                if scaler and "scaler_state_dict" in chk and chk["scaler_state_dict"] is not None:
                    scaler.load_state_dict(chk["scaler_state_dict"])
                try:
                    if "torch_rng_state" in chk and chk["torch_rng_state"] is not None:
                        torch.set_rng_state(chk["torch_rng_state"].cpu())
                    if torch.cuda.is_available() and "cuda_rng_state" in chk and chk["cuda_rng_state"] is not None:
                        torch.cuda.set_rng_state(chk["cuda_rng_state"].cpu())
                    if "random_state" in chk and chk["random_state"] is not None:
                        random.setstate(chk["random_state"])
                except Exception as rng_e:
                    print(f"  [i] Bỏ qua khôi phục RNG seed ({rng_e}).")

                print(f"[+] KHÔI PHỤC TRẠNG THÁI THÀNH CÔNG: Đã hoàn tất {saved_epoch}/{epochs} epochs.")
                print(f"[+] SẼ TIẾP TỤC HUẤN LUYỆN TỪ: Epoch {start_epoch}/{epochs} (Best Dev F1 trước đó: {best_dev_f1:.2f}%)")
                print("=" * 70 + "\n")
        except Exception as e:
            print(f"[!] Không thể khôi phục checkpoint ({e}). Bắt đầu lại từ Epoch 1.")
            start_epoch = 1
            best_dev_f1 = -1.0

    # Nếu bắt đầu từ Epoch 1 và có sẵn best_spert_phobert.pt trước đó -> Warm-start trọng số tương thích
    if start_epoch == 1 and os.path.exists(best_checkpoint_path):
        try:
            prev_chk = torch.load(best_checkpoint_path, map_location=device)
            prev_sd = prev_chk.get("model_state_dict", {})
            prev_ents = prev_chk.get("entity_types", [])
            curr_sd = model.state_dict()
            transferred = 0
            for k, v in prev_sd.items():
                if k not in curr_sd:
                    continue
                if curr_sd[k].shape == v.shape:
                    curr_sd[k] = v
                    transferred += 1
                elif k == "size_embeddings.weight" and curr_sd[k].shape[1] == v.shape[1]:
                    old_rows = min(curr_sd[k].shape[0], v.shape[0])
                    curr_sd[k][:old_rows] = v[:old_rows]
                    if curr_sd[k].shape[0] > old_rows:
                        curr_sd[k][old_rows:] = v[old_rows - 1].unsqueeze(0).expand(curr_sd[k].shape[0] - old_rows, -1).clone()
                    transferred += 1
                elif k in ("entity_classifier.3.weight", "entity_classifier.3.bias") and prev_ents:
                    # Chuyển đổi trọng số tầng phân loại theo tên nhãn thực thể (Name-based mapping)
                    # Lớp 0 là None
                    curr_sd[k][0] = v[0]
                    for old_i, name in enumerate(prev_ents):
                        if name in entity_types:
                            new_i = entity_types.index(name)
                            curr_sd[k][new_i + 1] = v[old_i + 1]
                    # Khởi tạo thực thể cấu trúc mới CHUONG từ DIEU (cùng nhóm Heading cấu trúc)
                    if "CHUONG" in entity_types and "DIEU" in prev_ents:
                        chuong_i = entity_types.index("CHUONG")
                        dieu_i = prev_ents.index("DIEU")
                        curr_sd[k][chuong_i + 1] = v[dieu_i + 1].clone()
                    transferred += 1

            model.load_state_dict(curr_sd)
            print(f"[+] Warm-start thành công {transferred} tensors từ {best_checkpoint_path} (Kèm Name-based transfer cho 27 nhãn thực thể).")
        except Exception as ws_e:
            print(f"[i] Bỏ qua warm-start ({ws_e}).")

    if start_epoch > epochs:
        print(f"[*] Quá trình huấn luyện đã hoàn tất trọn vẹn cả {epochs} epochs trước đó!")
        print(f"[*] Best Dev Joint F1: {best_dev_f1:.2f}%")
        print("[*] Chuyển ngay sang bước đánh giá tập Test (Academic Benchmark)...")
    else:
        print("\n" + "=" * 70)
        print(f"BẮT ĐẦU HUẤN LUYỆN: TỪ EPOCH {start_epoch} ĐẾN {epochs} (FP16 MIXED PRECISION)")
        print("=" * 70)

        start_time = time.time()
        try:
            for epoch in range(start_epoch, epochs + 1):
                epoch_start = time.time()
                model.train()
                total_epoch_loss = 0.0
                total_ent_loss = 0.0
                total_rel_loss = 0.0
                optimizer.zero_grad()

                for step, batch in enumerate(dataloader):
                    input_ids = batch["input_ids"].to(device)
                    attention_mask = batch["attention_mask"].to(device)
                    spans = batch["spans"].to(device)
                    span_lengths = batch["span_lengths"].to(device)
                    span_labels = batch["span_labels"].to(device)
                    rel_pairs = batch["rel_pairs"].to(device)
                    rel_labels = batch["rel_labels"].to(device)

                    with torch.amp.autocast('cuda' if torch.cuda.is_available() else 'cpu'):
                        outputs = model(
                            input_ids=input_ids,
                            attention_mask=attention_mask,
                            spans=spans,
                            span_lengths=span_lengths,
                            rel_pairs=rel_pairs
                        )

                        # Loss Entity (CrossEntropyLoss với lớp 0 là NONE)
                        ent_logits = outputs["entity_logits"]
                        loss_entity = entity_criterion(
                            ent_logits.view(-1, len(entity_types) + 1),
                            span_labels.view(-1)
                        )

                        # Loss Relation (BCEWithLogitsLoss trên |R| lớp, loại bỏ các cặp padding = -100)
                        rel_logits = outputs["relation_logits"]
                        loss_relation = torch.tensor(0.0, device=device)
                        if rel_logits is not None and rel_labels.numel() > 0:
                            valid_rel_mask = (rel_labels >= 0.0)
                            if valid_rel_mask.any():
                                clean_rel_targets = rel_labels.clamp(min=0.0)
                                raw_bce = relation_criterion(rel_logits, clean_rel_targets)
                                loss_relation = (raw_bce * valid_rel_mask).sum() / valid_rel_mask.sum().clamp(min=1.0)

                        loss = loss_entity + (rel_loss_weight * loss_relation)
                        loss_to_backward = loss / gradient_accumulation_steps

                    try:
                        if scaler:
                            scaler.scale(loss_to_backward).backward()
                        else:
                            loss_to_backward.backward()
                    except RuntimeError as cuda_err:
                        print(f"    [!] Cảnh báo bộ nhớ GPU tại step {step + 1} ({cuda_err}), giải phóng cache và tiếp tục...", flush=True)
                        optimizer.zero_grad(set_to_none=True)
                        if torch.cuda.is_available():
                            torch.cuda.empty_cache()
                        continue

                    total_epoch_loss += loss.item()
                    total_ent_loss += loss_entity.item()
                    total_rel_loss += loss_relation.item()

                    if (step + 1) % gradient_accumulation_steps == 0 or (step + 1) == len(dataloader):
                        if scaler:
                            scaler.step(optimizer)
                            scaler.update()
                        else:
                            optimizer.step()
                        optimizer.zero_grad(set_to_none=True)
                        scheduler.step()

                    if (step + 1) % 400 == 0 and torch.cuda.is_available():
                        torch.cuda.empty_cache()

                    if (step + 1) % 200 == 0 or (step + 1) == len(dataloader):
                        print(f"    - Step {step + 1:4d}/{len(dataloader)} | Loss: {loss.item():.4f} (Ent: {loss_entity.item():.4f}, Rel: {loss_relation.item():.4f})", flush=True)

                avg_loss = total_epoch_loss / len(dataloader)
                avg_ent = total_ent_loss / len(dataloader)
                avg_rel = total_rel_loss / len(dataloader)
                epoch_dur = time.time() - epoch_start

                # Đánh giá trên tập Dev
                print(f"\n[Epoch {epoch:02d}/{epochs:02d}] ({epoch_dur:.1f}s) | Train Loss: {avg_loss:.4f} (Ent: {avg_ent:.4f}, Rel: {avg_rel:.4f})")
                print("  --> Đang đánh giá trên tập Dev (split=DEV)...")
                if torch.cuda.is_available():
                    torch.cuda.empty_cache()
                dev_json_path = "data/legal/processed/dev.json"
                dev_src = dev_json_path if os.path.exists(dev_json_path) else by_doc_dir
                dev_metrics = evaluate_model(
                    model, dev_src, tokenizer, device,
                    max_span_length=max_span_length,
                    split="dev" if dev_src == by_doc_dir else None,
                )
                ent_m = dev_metrics["entity"]
                rel_m = dev_metrics["relation"]
                joint_f1 = (ent_m["f1"] + rel_m["f1"]) / 2.0

                print(f"  [Dev Entity]   P: {ent_m['precision']:5.2f}% | R: {ent_m['recall']:5.2f}% | F1: {ent_m['f1']:5.2f}% (Đúng: {ent_m['correct']}/{ent_m['gold']})")
                print(f"  [Dev Relation] P: {rel_m['precision']:5.2f}% | R: {rel_m['recall']:5.2f}% | F1: {rel_m['f1']:5.2f}% (Đúng: {rel_m['correct']}/{rel_m['gold']})")
                print(f"  [Dev Joint F1] {joint_f1:5.2f}%")

                # Lưu Best Checkpoint nếu Joint F1 cao hơn kỷ lục cũ
                if joint_f1 > best_dev_f1:
                    best_dev_f1 = joint_f1
                    save_checkpoint(
                        best_checkpoint_path, epoch, model, optimizer, scheduler, scaler,
                        best_dev_f1, joint_f1, dev_metrics, entity_types, relation_types
                    )
                    print(f"  [🏆 Best Checkpoint] Đã cập nhật kỷ lục mới: {best_checkpoint_path} (Joint F1: {joint_f1:.2f}%)")

                # LUÔN LUÔN LƯU last_checkpoint.pt SAU MỖI EPOCH ĐỂ TỰ ĐỘNG TIẾP TỤC NẾU TẮT MÁY
                save_checkpoint(
                    last_checkpoint_path, epoch, model, optimizer, scheduler, scaler,
                    best_dev_f1, joint_f1, dev_metrics, entity_types, relation_types
                )
                print(f"  [💾 Checkpoint] Đã ghi lại trạng thái: {last_checkpoint_path} (An toàn khi tắt máy)")

            total_time = time.time() - start_time
            print("\n" + "=" * 70)
            print(f"[HOÀN THÀNH HUẤN LUYỆN] Tổng thời gian: {total_time:.1f} giây ({total_time / 60:.1f} phút)")
            print(f"[*] Checkpoint tốt nhất: {best_checkpoint_path} (Best Dev Joint F1: {best_dev_f1:.2f}%)")
            print("=" * 70)

        except KeyboardInterrupt:
            print("\n" + "!" * 70)
            print("[!] TIẾN TRÌNH HUẤN LUYỆN TẠM DỪNG HOẶC TẮT MÁY (KEYBOARD INTERRUPT)")
            print("!" * 70)
            save_checkpoint(
                last_checkpoint_path, epoch, model, optimizer, scheduler, scaler,
                best_dev_f1, joint_f1 if 'joint_f1' in locals() else 0.0,
                dev_metrics if 'dev_metrics' in locals() else {},
                entity_types, relation_types
            )
            print(f"[*] ĐÃ LƯU AN TOÀN TRẠNG THÁI HIỆN TẠI VÀO: {last_checkpoint_path}")
            print("[*] Lần sau bạn chỉ cần bật máy và chạy lại lệnh 'python train.py' để tiếp tục từ đây!")
            return

    # 7. Đánh giá cuối cùng trên tập Test (Academic Benchmarking)
    eval_model_path = best_checkpoint_path if os.path.exists(best_checkpoint_path) else last_checkpoint_path
    test_json_path = "data/legal/processed/test.json"
    test_src = test_json_path if os.path.exists(test_json_path) else by_doc_dir
    if os.path.exists(test_src) and os.path.exists(eval_model_path):
        print("\n" + "=" * 70)
        print(f"ĐÁNH GIÁ CUỐI CÙNG TRÊN TẬP TEST (SPLIT=TEST): {eval_model_path}")
        print("=" * 70)
        chk = torch.load(eval_model_path, map_location=device)
        model.load_state_dict(chk["model_state_dict"])
        model.entity_types = chk.get("entity_types", entity_types)
        model.relation_types = chk.get("relation_types", relation_types)
        test_metrics = evaluate_model(
            model, test_src, tokenizer, device,
            max_span_length=max_span_length,
            split="test" if test_src == by_doc_dir else None,
        )
        t_ent = test_metrics["entity"]
        t_rel = test_metrics["relation"]
        t_joint = (t_ent["f1"] + t_rel["f1"]) / 2.0
        print(f"  [Test Entity]   Precision: {t_ent['precision']:5.2f}% | Recall: {t_ent['recall']:5.2f}% | F1: {t_ent['f1']:5.2f}%")
        print(f"  [Test Relation] Precision: {t_rel['precision']:5.2f}% | Recall: {t_rel['recall']:5.2f}% | F1: {t_rel['f1']:5.2f}%")
        print(f"  [Test Joint F1] {t_joint:5.2f}%")
        print("=" * 70)

        # Ghi kết quả ra file json
        with open(os.path.join(args.checkpoint_dir, "evaluation_results.json"), "w", encoding="utf-8") as f:
            json.dump({
                "best_epoch": chk.get("epoch"),
                "dev_metrics": chk.get("dev_metrics"),
                "test_metrics": test_metrics,
            }, f, ensure_ascii=False, indent=2)
        print(f"[*] Đã lưu báo cáo kết quả nghiên cứu: {os.path.join(args.checkpoint_dir, 'evaluation_results.json')}")


if __name__ == "__main__":
    prevent_system_sleep()
    try:
        train_spert()
    finally:
        restore_system_sleep()

