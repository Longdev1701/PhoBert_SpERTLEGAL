import os
import glob
import json
import random
from typing import List, Optional, Dict
import torch
from torch.utils.data import Dataset
from transformers import AutoTokenizer

# Dinh nghia cac bo nhan

from data.legal.schema import ENTITY_TYPES, RELATION_TYPES


def create_mappings(types_list: List[str]):
    type2id = {t: i + 1 for i, t in enumerate(types_list)}
    type2id["None"] = 0
    id2type = {v: k for k, v in type2id.items()}
    return type2id, id2type


ENTITY2ID, ID2ENTITY = create_mappings(ENTITY_TYPES)
REL2ID, ID2REL = create_mappings(RELATION_TYPES)


def load_spert_samples(source_path: str, split: Optional[str] = None) -> List[Dict]:
    """
    Nạp mẫu dữ liệu SpERT trực tiếp từ:
      1. Thư mục chứa từng văn bản riêng biệt (`data/legal/processed/by_doc_spert/<cat>/<doc>.json`) lọc theo `split` ('train'/'dev'/'test'), HOẶC
      2. Một file JSON của 1 văn bản đơn lẻ (`<doc>.json`), HOẶC
      3. Một file JSON tổng hợp (`train.json` / `dev.json` / `test.json`).
    """
    if os.path.isdir(source_path):
        samples = []
        pattern = os.path.join(source_path, "*", "*.json")
        for jf in sorted(glob.glob(pattern)):
            with open(jf, "r", encoding="utf-8") as f:
                doc_obj = json.load(f)
            if isinstance(doc_obj, dict) and "samples" in doc_obj:
                if split is None or doc_obj.get("split", "").lower() == split.lower():
                    samples.extend(doc_obj["samples"])
        return samples
    else:
        with open(source_path, "r", encoding="utf-8") as f:
            obj = json.load(f)
        if isinstance(obj, dict) and "samples" in obj:
            return obj["samples"]
        return obj


def generate_candidate_spans(words: List[str], max_span_length: int = 110) -> List[tuple]:
    """
    Sinh danh sách candidate spans (w_start, w_end) tối ưu cho văn bản pháp luật:
      - Với độ dài 1..17 từ: sinh đầy đủ mọi (i, i + length) cho toàn bộ thực thể Hub & Vệ tinh.
      - Với độ dài 18..max_span_length: chỉ sinh các span khung cấu trúc (DIEU, KHOAN, DIEM)
        kết thúc ở cuối câu (w_end == num_words) hoặc bắt đầu bằng từ khóa 'Điều'/'Khoản',
        giúp bao phủ 100% thực thể chuẩn trong Train/Dev/Test mà không sinh O(N^2) nhiễu.
    """
    num_words = len(words)
    spans = []
    seen = set()
    dense_limit = min(num_words + 1, 18, max_span_length + 1)
    for length in range(1, dense_limit):
        for i in range(num_words - length + 1):
            sp = (i, i + length)
            seen.add(sp)
            spans.append(sp)
    for length in range(18, min(num_words + 1, max_span_length + 1)):
        sp = (num_words - length, num_words)
        if sp not in seen:
            seen.add(sp)
            spans.append(sp)
    for i, w in enumerate(words):
        if w in ("Khoản", "Điều", "Chương"):
            for j in range(i + 18, min(num_words + 1, i + max_span_length + 1)):
                sp = (i, j)
                if sp not in seen:
                    seen.add(sp)
                    spans.append(sp)
    return spans


class SpERTDataset(Dataset):
    """
    Dataset loader cho kiến trúc Joint Entity and Relation Extraction (PhoBERT-SpERT).
    Hỗ trợ nạp trực tiếp từ thư mục từng văn bản (by_doc_spert) hoặc file JSON.
    """
    def __init__(
        self,
        json_file: str,
        tokenizer: AutoTokenizer,
        max_span_length: int = 110,
        neg_entity_count: int = 40,
        neg_relation_count: int = 40,
        is_eval: bool = False,
        entity_types: Optional[List[str]] = None,
        relation_types: Optional[List[str]] = None,
        split: Optional[str] = None,
    ):
        self.tokenizer = tokenizer
        self.max_span_length = max_span_length
        self.neg_entity_count = neg_entity_count
        self.neg_relation_count = neg_relation_count
        self.is_eval = is_eval

        self.data = load_spert_samples(json_file, split=split)
        self.entity_types = list(entity_types) if entity_types else list(ENTITY_TYPES)
        self.relation_types = list(relation_types) if relation_types else list(RELATION_TYPES)

        self.entity2id, self.id2entity = create_mappings(self.entity_types)
        self.rel2id, self.id2rel = create_mappings(self.relation_types)

    def __len__(self):
        return len(self.data)

    def _align_words_to_subwords(self, words: List[str]):
        """
        Anh xa vi tri tu (word index) sang vi tri token subwords cua PhoBERT.
        PhoBERT bat dau bang <s> (token id 0).
        """
        bos_id = self.tokenizer.bos_token_id if self.tokenizer.bos_token_id is not None else 0
        eos_id = self.tokenizer.eos_token_id if self.tokenizer.eos_token_id is not None else 2
        unk_id = self.tokenizer.unk_token_id if self.tokenizer.unk_token_id is not None else 3

        subword_ids = [bos_id]
        word_to_subword_spans = []

        for word in words:
            tokens = self.tokenizer.encode(word, add_special_tokens=False)
            if not tokens:
                tokens = [unk_id]
            start_idx = len(subword_ids)
            subword_ids.extend(tokens)
            end_idx = len(subword_ids)
            word_to_subword_spans.append((start_idx, end_idx))

        subword_ids.append(eos_id)
        return subword_ids, word_to_subword_spans

    def __getitem__(self, idx: int):
        item = self.data[idx]
        words = item["tokens"]

        # 1. Align subwords
        subword_ids, word_to_subword = self._align_words_to_subwords(words)

        # 1B. Span-Inner Subword Dropout (chỉ áp dụng khi Train: is_eval=False)
        # Ngẫu nhiên che (<mask>) 1 từ bổ ngữ nằm giữa của thực thể chuyên ngành dài (>= 3 từ),
        # giữ nguyên từ khóa mở đầu (w_start) và từ biên cuối (w_end - 1) để mô hình học quy luật ngữ pháp biên
        if not self.is_eval and self.tokenizer.mask_token_id is not None:
            mask_id = self.tokenizer.mask_token_id
            for ent in item.get("entities", []):
                if ent.get("type") in ("GIAY_TO_HO_SO", "TO_CHUC_DOANH_NGHIEP", "CO_QUAN_THAM_QUYEN", "CHU_THE_CA_NHAN"):
                    st_w, ed_w = ent["start"], ent["end"]
                    if ed_w - st_w >= 3 and random.random() < 0.20:
                        mid_w = random.randint(st_w + 1, ed_w - 2)
                        sw_s, sw_e = word_to_subword[mid_w]
                        for sw_i in range(sw_s, sw_e):
                            subword_ids[sw_i] = mask_id

        # 2. Tap hop gold entities
        # key: (word_start, word_end), value: entity_type_id
        gold_entities = {}
        for ent in item.get("entities", []):
            etype_id = self.entity2id.get(ent["type"], 0)
            gold_entities[(ent["start"], ent["end"])] = etype_id

        # 3. Tao tat ca cac span ung vien (Candidate Spans)
        all_candidate_spans = generate_candidate_spans(words, self.max_span_length)

        # Tach thanh positive spans va negative spans
        pos_spans = []
        pos_labels = []
        neg_spans = []

        for span in all_candidate_spans:
            if span in gold_entities:
                pos_spans.append(span)
                pos_labels.append(gold_entities[span])
            else:
                neg_spans.append(span)

        # Negative sampling cho entity spans trong luc train
        if not self.is_eval and len(neg_spans) > self.neg_entity_count:
            sampled_neg_spans = random.sample(neg_spans, self.neg_entity_count)
        else:
            sampled_neg_spans = neg_spans

        all_spans = pos_spans + sampled_neg_spans
        all_labels = pos_labels + [0] * len(sampled_neg_spans)

        # 4. Tao cac cap quan he (Relation Pairs) voi Multi-Hot vector cho BCEWithLogitsLoss
        num_rel_types = len(self.relation_types)
        gold_relations = {}
        raw_entities = item.get("entities", [])
        for rel in item.get("relations", []):
            head_idx = rel.get("head")
            tail_idx = rel.get("tail")
            if head_idx is not None and tail_idx is not None and head_idx < len(raw_entities) and tail_idx < len(raw_entities):
                head_ent = raw_entities[head_idx]
                tail_ent = raw_entities[tail_idx]
                s1 = (head_ent["start"], head_ent["end"])
                s2 = (tail_ent["start"], tail_ent["end"])
                rtype_id = self.rel2id.get(rel.get("type"), 0)
                if rtype_id > 0:
                    if (s1, s2) not in gold_relations:
                        gold_relations[(s1, s2)] = [0.0] * num_rel_types
                    gold_relations[(s1, s2)][rtype_id - 1] = 1.0

        span2idx = {s: i for i, s in enumerate(all_spans)}

        pos_rel_pairs = []
        pos_rel_labels = []
        neg_rel_pairs = []

        # Cac cap quan he duong
        for (s1, s2), multi_hot in gold_relations.items():
            if s1 in span2idx and s2 in span2idx:
                pos_rel_pairs.append((span2idx[s1], span2idx[s2]))
                pos_rel_labels.append(multi_hot)

        # Cac cap am giua cac positive spans
        for i, s1 in enumerate(pos_spans):
            for j, s2 in enumerate(pos_spans):
                if i != j and (s1, s2) not in gold_relations:
                    neg_rel_pairs.append((span2idx[s1], span2idx[s2]))

        # Neu so luong cap am chua du, lay them ngau nhien giua pos_spans va sampled_neg_spans
        if len(neg_rel_pairs) < self.neg_relation_count and pos_spans and sampled_neg_spans:
            extra_candidates = []
            for s1 in pos_spans:
                for s2 in sampled_neg_spans:
                    extra_candidates.append((span2idx[s1], span2idx[s2]))
                    extra_candidates.append((span2idx[s2], span2idx[s1]))
            random.shuffle(extra_candidates)
            needed = self.neg_relation_count - len(neg_rel_pairs)
            neg_rel_pairs.extend(extra_candidates[:needed])

        # Neu van chua du va khong co pos_spans, lay giua cac sampled_neg_spans
        if len(neg_rel_pairs) < self.neg_relation_count and len(sampled_neg_spans) >= 2:
            extra_neg_only = []
            for i in range(min(15, len(sampled_neg_spans))):
                for j in range(min(15, len(sampled_neg_spans))):
                    if i != j:
                        extra_neg_only.append((span2idx[sampled_neg_spans[i]], span2idx[sampled_neg_spans[j]]))
            random.shuffle(extra_neg_only)
            needed = self.neg_relation_count - len(neg_rel_pairs)
            neg_rel_pairs.extend(extra_neg_only[:needed])

        if not self.is_eval and len(neg_rel_pairs) > self.neg_relation_count:
            sampled_neg_rels = random.sample(neg_rel_pairs, self.neg_relation_count)
        else:
            sampled_neg_rels = neg_rel_pairs

        zero_vec = [0.0] * num_rel_types
        all_rel_pairs = pos_rel_pairs + sampled_neg_rels
        all_rel_labels = pos_rel_labels + [zero_vec for _ in sampled_neg_rels]

        # Chuyen doi vi tri word sang subword index cho spans
        subword_spans = []
        span_lengths = []
        for w_start, w_end in all_spans:
            sw_start = word_to_subword[w_start][0]
            sw_end = word_to_subword[w_end - 1][1]
            subword_spans.append((sw_start, sw_end))
            span_lengths.append(w_end - w_start)

        return {
            "input_ids": torch.tensor(subword_ids, dtype=torch.long),
            "spans": torch.tensor(subword_spans, dtype=torch.long),
            "span_lengths": torch.tensor(span_lengths, dtype=torch.long),
            "span_labels": torch.tensor(all_labels, dtype=torch.long),
            "rel_pairs": torch.tensor(all_rel_pairs, dtype=torch.long) if all_rel_pairs else torch.empty((0, 2), dtype=torch.long),
            "rel_labels": torch.tensor(all_rel_labels, dtype=torch.float) if all_rel_labels else torch.empty((0, num_rel_types), dtype=torch.float),
            "raw_item": item,
            "all_spans_words": all_spans,
        }


def spert_collate_fn(batch):
    """
    Collate function de gom batch va padding token.
    """
    pad_id = 1  # PhoBERT pad_token_id (<pad>)

    # 1. Padding input_ids
    input_ids_list = [item["input_ids"] for item in batch]
    max_len = max(len(ids) for ids in input_ids_list)

    batch_size = len(batch)
    padded_input_ids = torch.full((batch_size, max_len), pad_id, dtype=torch.long)
    attention_mask = torch.zeros((batch_size, max_len), dtype=torch.long)

    for i, ids in enumerate(input_ids_list):
        padded_input_ids[i, :len(ids)] = ids
        attention_mask[i, :len(ids)] = 1

    # 2. Spans padding
    max_spans = max(item["spans"].shape[0] for item in batch)
    padded_spans = torch.zeros((batch_size, max_spans, 2), dtype=torch.long)
    padded_span_lengths = torch.zeros((batch_size, max_spans), dtype=torch.long)
    padded_span_labels = torch.full((batch_size, max_spans), -100, dtype=torch.long)

    for i, item in enumerate(batch):
        n_spans = item["spans"].shape[0]
        padded_spans[i, :n_spans] = item["spans"]
        padded_span_lengths[i, :n_spans] = item["span_lengths"]
        padded_span_labels[i, :n_spans] = item["span_labels"]

    # 3. Relation pairs padding (multi-hot float tensor cho BCEWithLogitsLoss)
    num_rel_types = batch[0]["rel_labels"].shape[-1] if batch[0]["rel_labels"].dim() == 2 else 0
    max_rels = max(item["rel_pairs"].shape[0] for item in batch) if any(item["rel_pairs"].numel() > 0 for item in batch) else 0
    if max_rels > 0:
        padded_rel_pairs = torch.zeros((batch_size, max_rels, 2), dtype=torch.long)
        padded_rel_labels = torch.full((batch_size, max_rels, num_rel_types), -100.0, dtype=torch.float)

        for i, item in enumerate(batch):
            n_rels = item["rel_pairs"].shape[0]
            if n_rels > 0:
                padded_rel_pairs[i, :n_rels] = item["rel_pairs"]
                padded_rel_labels[i, :n_rels] = item["rel_labels"]
    else:
        padded_rel_pairs = torch.empty((batch_size, 0, 2), dtype=torch.long)
        padded_rel_labels = torch.empty((batch_size, 0, num_rel_types), dtype=torch.float)

    return {
        "input_ids": padded_input_ids,
        "attention_mask": attention_mask,
        "spans": padded_spans,
        "span_lengths": padded_span_lengths,
        "span_labels": padded_span_labels,
        "rel_pairs": padded_rel_pairs,
        "rel_labels": padded_rel_labels,
        "raw_items": [item["raw_item"] for item in batch],
        "all_spans_words": [item["all_spans_words"] for item in batch],
    }
