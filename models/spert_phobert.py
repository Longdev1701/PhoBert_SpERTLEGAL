import torch
import torch.nn as nn
from transformers import AutoModel, AutoConfig


class BiaffineRelationClassifier(nn.Module):
    """
    Nâng cấp 3 & 4: Bộ phân loại quan hệ kết hợp Biaffine Attention và MLP,
    đầu ra |R| chiều (không có lớp NONE) tương thích với BCEWithLogitsLoss:
        Score(s1, s2) = h_head^T U h_tail + MLP([s1 || s2 || c]) + b
    """
    def __init__(
        self,
        span_repr_dim: int,
        context_repr_dim: int,
        hidden_dim: int,
        num_relation_types: int,
        biaffine_dim: int = 256,
        dropout_rate: float = 0.1
    ):
        super().__init__()
        self.num_relation_types = num_relation_types
        self.biaffine_dim = biaffine_dim

        # Chiếu biểu diễn span đóng vai trò Subject (Head) và Object (Tail)
        self.head_proj = nn.Sequential(
            nn.Linear(span_repr_dim, biaffine_dim),
            nn.GELU(),
            nn.Dropout(dropout_rate)
        )
        self.tail_proj = nn.Sequential(
            nn.Linear(span_repr_dim, biaffine_dim),
            nn.GELU(),
            nn.Dropout(dropout_rate)
        )

        # Tensor tương tác bậc hai Biaffine U: (|R|, biaffine_dim, biaffine_dim)
        self.U = nn.Parameter(torch.empty(num_relation_types, biaffine_dim, biaffine_dim))
        nn.init.xavier_uniform_(self.U)

        # Nhánh MLP kết hợp toàn cục [s1 || s2 || c]
        rel_input_dim = (span_repr_dim * 2) + context_repr_dim
        self.mlp = nn.Sequential(
            nn.Linear(rel_input_dim, hidden_dim),
            nn.GELU(),
            nn.Dropout(dropout_rate),
            nn.Linear(hidden_dim, num_relation_types)
        )

    def forward(
        self,
        s1_repr: torch.Tensor,
        s2_repr: torch.Tensor,
        context_repr: torch.Tensor
    ) -> torch.Tensor:
        """
        s1_repr: (B, Num_Pairs, span_repr_dim)
        s2_repr: (B, Num_Pairs, span_repr_dim)
        context_repr: (B, Num_Pairs, context_repr_dim)
        Output: (B, Num_Pairs, num_relation_types)
        """
        h_head = self.head_proj(s1_repr)  # (B, Num_Pairs, biaffine_dim)
        h_tail = self.tail_proj(s2_repr)  # (B, Num_Pairs, biaffine_dim)

        # Tương tác chéo Biaffine: h_head^T U h_tail -> (B, Num_Pairs, |R|)
        biaffine_scores = torch.einsum("bpi,rij,bpj->bpr", h_head, self.U, h_tail)

        # Nhánh tuyến tính ngữ cảnh ghép nối: W [s1 || s2 || c] + b -> (B, Num_Pairs, |R|)
        concat_repr = torch.cat([s1_repr, s2_repr, context_repr], dim=-1)
        mlp_scores = self.mlp(concat_repr)

        return biaffine_scores + mlp_scores


class PhoBERTSpeRT(nn.Module):
    """
    Kiến trúc Joint Entity and Relation Extraction theo hướng SpERT (Eberts & Ulges, ACL 2020)
    sử dụng PhoBERT-base-v2 làm backbone cho tiếng Việt, kèm 4 nâng cấp chuyên sâu cho văn bản pháp luật:

      1. Boundary-Aware Span Representation (_pool_span):
         s_{i,j} = [h_start || h_end || MaxPool(h_start...h_end) || w_width] (2329 chiều)
         Giúp phân biệt rạch ròi biên trái và biên phải của các thực thể lồng nhau.
      2. Overlap-Rescued Context & Relative Topology Embedding (_pool_context):
         - Khi 2 span lồng nhau/giao nhau/sát cạnh (khoảng cách = 0), lấy Max-Pooling hợp (union) của 2 span
           thay vì trả về vector 0.
         - Bổ sung Relative Position/Overlap Embedding (25 chiều) mã hóa trạng thái tương đối:
           NESTED_INSIDE (s1 trong s2 hoặc s2 trong s1), OVERLAPPING, ADJACENT, DISJOINT (gần/vừa/xa).
      3. Multi-Label Relation Output cho BCEWithLogitsLoss:
         - Entity Classifier giữ nguyên CrossEntropyLoss (num_entity_types + 1 lớp, lớp 0 là NONE).
         - Relation Classifier xuất trực tiếp |R| = num_relation_types chiều (bỏ lớp NONE),
           huấn luyện với BCEWithLogitsLoss và suy luận độc lập qua Sigmoid.
      4. Biaffine Relation Classifier:
         Score(s1, s2) = s1'^T U s2' + MLP([s1 || s2 || c]) + b
    """
    NUM_REL_POS_STATES = 8  # 0: PAD, 1: S1_IN_S2, 2: S2_IN_S1, 3: OVERLAP, 4: ADJACENT, 5: DISJOINT_NEAR, 6: DISJOINT_MID, 7: DISJOINT_FAR

    def __init__(
        self,
        model_name: str = "vinai/phobert-base-v2",
        num_entity_types: int = 4,          # Số lượng nhãn thực thể (không tính nhãn None)
        num_relation_types: int = 4,        # Số lượng nhãn quan hệ (không tính nhãn None)
        max_span_length: int = 16,          # Độ dài tối đa của một span thực thể (số từ)
        size_embedding_dim: int = 25,       # Chiều của vector nhúng độ dài span
        rel_pos_embedding_dim: int = 25,    # Chiều của vector nhúng vị trí tương đối giữa 2 span
        biaffine_dim: int = 256,            # Chiều ẩn của tầng tương tác chéo Biaffine
        freeze_phobert: bool = False,
        dropout_rate: float = 0.1
    ):
        super(PhoBERTSpeRT, self).__init__()

        self.max_span_length = max_span_length
        self.num_entity_types = num_entity_types
        self.num_relation_types = num_relation_types
        self.size_embedding_dim = size_embedding_dim
        self.rel_pos_embedding_dim = rel_pos_embedding_dim

        # 1. PhoBERT Backbone
        self.phobert_config = AutoConfig.from_pretrained(model_name)
        self.phobert = AutoModel.from_pretrained(model_name, config=self.phobert_config)
        if freeze_phobert:
            for param in self.phobert.parameters():
                param.requires_grad = False

        hidden_dim = self.phobert_config.hidden_size  # 768 với PhoBERT-base

        # 2. Span Width Embedding + Boundary Representation (Nâng cấp 1)
        # s_{i,j} = [h_start (768) || h_end (768) || MaxPool (768) || w_width (25)] = 2329 chiều
        self.size_embeddings = nn.Embedding(max_span_length + 1, size_embedding_dim)
        self.span_repr_dim = (hidden_dim * 3) + size_embedding_dim

        # 3. Entity Classification Head (dự đoán num_entity_types + 1 lớp, lớp 0 là 'None')
        self.dropout = nn.Dropout(dropout_rate)
        self.entity_classifier = nn.Sequential(
            nn.Linear(self.span_repr_dim, hidden_dim),
            nn.GELU(),
            nn.Dropout(dropout_rate),
            nn.Linear(hidden_dim, num_entity_types + 1)
        )

        # 4. Relative Distance / Overlap Embedding cho Context (Nâng cấp 2)
        self.rel_pos_embeddings = nn.Embedding(self.NUM_REL_POS_STATES, rel_pos_embedding_dim)
        self.context_repr_dim = hidden_dim + rel_pos_embedding_dim

        # 5. Biaffine Relation Classification Head với đầu ra |R| chiều cho BCEWithLogitsLoss (Nâng cấp 3 & 4)
        self.rel_repr_dim = (self.span_repr_dim * 2) + self.context_repr_dim
        self.relation_classifier = BiaffineRelationClassifier(
            span_repr_dim=self.span_repr_dim,
            context_repr_dim=self.context_repr_dim,
            hidden_dim=hidden_dim,
            num_relation_types=num_relation_types,
            biaffine_dim=biaffine_dim,
            dropout_rate=dropout_rate
        )

    def _pool_span(self, sequence_output: torch.Tensor, spans: torch.Tensor) -> torch.Tensor:
        """
        Nâng cấp 1: Biểu diễn Span kết hợp Boundary Tokens và Max-Pooling:
            [h_start || h_end || MaxPool(h_start ... h_end)]
        sequence_output: (B, Seq_Len, Hidden_Dim)
        spans: (B, Num_Spans, 2) chứa [start_token, end_token) (nửa mở, chưa bao gồm end_token)
        Output: (B, Num_Spans, Hidden_Dim * 3)
        """
        batch_size, seq_len, hidden_dim = sequence_output.shape
        _, num_spans, _ = spans.shape

        span_starts = spans[:, :, 0]  # (B, Num_Spans)
        span_ends = spans[:, :, 1]    # (B, Num_Spans)
        is_valid = (span_ends > span_starts).unsqueeze(-1)  # (B, Num_Spans, 1)

        # 1. Trích xuất vector biên trái h_start và biên phải h_end (end_token - 1)
        start_indices = span_starts.clamp(min=0, max=seq_len - 1)
        end_indices = (span_ends - 1).clamp(min=0, max=seq_len - 1)

        h_start = torch.gather(
            sequence_output, 1,
            start_indices.unsqueeze(-1).expand(-1, -1, hidden_dim)
        )  # (B, Num_Spans, Hidden_Dim)
        h_end = torch.gather(
            sequence_output, 1,
            end_indices.unsqueeze(-1).expand(-1, -1, hidden_dim)
        )  # (B, Num_Spans, Hidden_Dim)

        # 2. Thực hiện Max-Pooling các token bên trong khoảng [start, end) theo khối (chunk=512) chống tràn VRAM
        token_indices = torch.arange(seq_len, device=sequence_output.device).view(1, 1, seq_len)
        neg_inf = torch.tensor(-1e4, dtype=sequence_output.dtype, device=sequence_output.device)
        chunk_size = 512
        pooled_chunks = []
        for c_start in range(0, num_spans, chunk_size):
            c_end = min(c_start + chunk_size, num_spans)
            c_starts = span_starts[:, c_start:c_end].unsqueeze(-1)
            c_ends = span_ends[:, c_start:c_end].unsqueeze(-1)
            mask = (token_indices >= c_starts) & (token_indices < c_ends)
            mask_expanded = mask.unsqueeze(-1)
            seq_expanded = sequence_output.unsqueeze(1).expand(-1, c_end - c_start, -1, -1)
            seq_masked = torch.where(mask_expanded, seq_expanded, neg_inf)
            c_pooled, _ = torch.max(seq_masked, dim=2)
            pooled_chunks.append(c_pooled)
        pooled_spans = torch.cat(pooled_chunks, dim=1) if pooled_chunks else torch.zeros_like(h_start)

        # 3. Ghép [h_start || h_end || MaxPool] và đưa các span padding về 0
        boundary_and_pooled = torch.cat([h_start, h_end, pooled_spans], dim=-1)  # (B, Num_Spans, Hidden_Dim * 3)
        boundary_and_pooled = torch.where(is_valid, boundary_and_pooled, torch.zeros_like(boundary_and_pooled))
        return boundary_and_pooled

    def _pool_context(
        self,
        sequence_output: torch.Tensor,
        spans: torch.Tensor,
        rel_pairs: torch.Tensor
    ) -> torch.Tensor:
        """
        Nâng cấp 2:
          - Khi 2 span tách rời (first_ends < second_starts): lấy Max-Pooling các token nằm giữa 2 span.
          - Khi 2 span lồng nhau, giao nhau hoặc đứng sát nhau (first_ends >= second_starts):
            thay vì trả về vector 0, lấy Max-Pooling của hợp (union) hai span [min_start, max_end).
          - Nối thêm Relative Distance / Overlap Embedding (25d) mã hóa trạng thái vị trí tương đối.
        Output: (B, Num_Pairs, Hidden_Dim + rel_pos_embedding_dim)
        """
        batch_size, seq_len, hidden_dim = sequence_output.shape
        _, num_pairs, _ = rel_pairs.shape

        s1_indices = rel_pairs[:, :, 0]  # (B, Num_Pairs)
        s2_indices = rel_pairs[:, :, 1]  # (B, Num_Pairs)

        s1_spans = torch.gather(spans, 1, s1_indices.unsqueeze(-1).expand(-1, -1, 2))  # (B, Num_Pairs, 2)
        s2_spans = torch.gather(spans, 1, s2_indices.unsqueeze(-1).expand(-1, -1, 2))  # (B, Num_Pairs, 2)

        start1, end1 = s1_spans[:, :, 0], s1_spans[:, :, 1]
        start2, end2 = s2_spans[:, :, 0], s2_spans[:, :, 1]

        valid_pair = (end1 > start1) & (end2 > start2)  # (B, Num_Pairs)

        first_ends = torch.min(end1, end2)
        second_starts = torch.max(start1, start2)
        union_starts = torch.min(start1, start2)
        union_ends = torch.max(end1, end2)

        token_indices = torch.arange(seq_len, device=sequence_output.device).view(1, 1, seq_len)
        neg_inf = torch.tensor(-1e4, dtype=sequence_output.dtype, device=sequence_output.device)
        chunk_size = 512
        ctx_chunks = []
        for c_start in range(0, num_pairs, chunk_size):
            c_end = min(c_start + chunk_size, num_pairs)
            c_fe = first_ends[:, c_start:c_end].unsqueeze(-1)
            c_ss = second_starts[:, c_start:c_end].unsqueeze(-1)
            c_us = union_starts[:, c_start:c_end].unsqueeze(-1)
            c_ue = union_ends[:, c_start:c_end].unsqueeze(-1)
            between_mask = (token_indices >= c_fe) & (token_indices < c_ss)
            union_mask = (token_indices >= c_us) & (token_indices < c_ue)
            has_between = (c_ss > c_fe)
            effective_mask = torch.where(has_between, between_mask, union_mask)
            mask_expanded = effective_mask.unsqueeze(-1)
            seq_expanded = sequence_output.unsqueeze(1).expand(-1, c_end - c_start, -1, -1)
            seq_masked = torch.where(mask_expanded, seq_expanded, neg_inf)
            c_ctx, _ = torch.max(seq_masked, dim=2)
            ctx_chunks.append(c_ctx)
        pooled_context = torch.cat(ctx_chunks, dim=1) if ctx_chunks else torch.zeros((batch_size, 0, hidden_dim), dtype=sequence_output.dtype, device=sequence_output.device)
        pooled_context = torch.where(valid_pair.unsqueeze(-1), pooled_context, torch.zeros_like(pooled_context))

        # Mã hóa trạng thái vị trí tương đối (Relative Topology State):
        # 0: PAD
        # 1: NESTED_S1_IN_S2 (s1 nằm trong s2)
        # 2: NESTED_S2_IN_S1 (s2 nằm trong s1)
        # 3: OVERLAPPING (giao nhau một phần)
        # 4: ADJACENT (đứng sát cạnh nhau, khoảng cách = 0)
        # 5: DISJOINT_NEAR (khoảng cách 1..3 subwords)
        # 6: DISJOINT_MID (khoảng cách 4..10 subwords)
        # 7: DISJOINT_FAR (khoảng cách > 10 subwords)
        s1_in_s2 = (start1 >= start2) & (end1 <= end2)
        s2_in_s1 = (start2 >= start1) & (end2 <= end1)
        is_overlapping = (first_ends > second_starts) & ~(s1_in_s2 | s2_in_s1)
        is_adjacent = (first_ends == second_starts)
        dist = second_starts - first_ends

        rel_pos_state = torch.zeros_like(start1)
        rel_pos_state = torch.where(dist > 10, torch.full_like(rel_pos_state, 7), rel_pos_state)
        rel_pos_state = torch.where((dist >= 4) & (dist <= 10), torch.full_like(rel_pos_state, 6), rel_pos_state)
        rel_pos_state = torch.where((dist >= 1) & (dist <= 3), torch.full_like(rel_pos_state, 5), rel_pos_state)
        rel_pos_state = torch.where(is_adjacent, torch.full_like(rel_pos_state, 4), rel_pos_state)
        rel_pos_state = torch.where(is_overlapping, torch.full_like(rel_pos_state, 3), rel_pos_state)
        rel_pos_state = torch.where(s2_in_s1, torch.full_like(rel_pos_state, 2), rel_pos_state)
        rel_pos_state = torch.where(s1_in_s2, torch.full_like(rel_pos_state, 1), rel_pos_state)
        rel_pos_state = torch.where(valid_pair, rel_pos_state, torch.zeros_like(rel_pos_state))

        rel_pos_emb = self.rel_pos_embeddings(rel_pos_state)  # (B, Num_Pairs, rel_pos_embedding_dim)
        rel_pos_emb = torch.where(valid_pair.unsqueeze(-1), rel_pos_emb, torch.zeros_like(rel_pos_emb))

        return torch.cat([pooled_context, rel_pos_emb], dim=-1)

    def forward(
        self,
        input_ids: torch.Tensor,
        attention_mask: torch.Tensor,
        spans: torch.Tensor,            # (B, Num_Spans, 2): [start, end)
        span_lengths: torch.Tensor,     # (B, Num_Spans): Độ dài của mỗi span
        rel_pairs: torch.Tensor = None  # (B, Num_Pairs, 2): Chỉ số (idx_s1, idx_s2)
    ):
        """
        Lan truyền xuôi của mô hình PhoBERT-SpERT nâng cấp.
        """
        # 1. PhoBERT Backbone
        phobert_outputs = self.phobert(input_ids=input_ids, attention_mask=attention_mask)
        sequence_output = phobert_outputs.last_hidden_state  # (B, Seq_Len, 768)

        # 2. Xây dựng Boundary-Aware Span Representation:
        # s_{i,j} = [h_start || h_end || MaxPool(s) || Size_Embedding] (2329 chiều)
        span_pooled = self._pool_span(sequence_output, spans)  # (B, Num_Spans, 768 * 3)

        clamped_lengths = torch.clamp(span_lengths, min=0, max=self.max_span_length)
        size_emb = self.size_embeddings(clamped_lengths)  # (B, Num_Spans, 25)

        span_repr = torch.cat([span_pooled, size_emb], dim=-1)  # (B, Num_Spans, 2329)
        span_repr = self.dropout(span_repr)

        # 3. Entity Classification Logits (CrossEntropy: num_entity_types + 1 lớp)
        entity_logits = self.entity_classifier(span_repr)  # (B, Num_Spans, num_entity_types + 1)

        # 4. Relation Classification Logits (Biaffine + MLP, BCEWithLogits: num_relation_types lớp)
        relation_logits = None
        if rel_pairs is not None and rel_pairs.shape[1] > 0:
            s1_idx = rel_pairs[:, :, 0].unsqueeze(-1).expand(-1, -1, self.span_repr_dim)
            s2_idx = rel_pairs[:, :, 1].unsqueeze(-1).expand(-1, -1, self.span_repr_dim)

            s1_repr = torch.gather(span_repr, 1, s1_idx)  # (B, Num_Pairs, 2329)
            s2_repr = torch.gather(span_repr, 1, s2_idx)  # (B, Num_Pairs, 2329)

            context_repr = self._pool_context(sequence_output, spans, rel_pairs)  # (B, Num_Pairs, 793)
            context_repr = self.dropout(context_repr)

            relation_logits = self.relation_classifier(s1_repr, s2_repr, context_repr)  # (B, Num_Pairs, num_relation_types)

        return {
            "entity_logits": entity_logits,
            "relation_logits": relation_logits,
            "span_repr": span_repr
        }

