def compute_metrics(gold_docs, pred_docs):
    """
    Tinh toan do do chuan theo danh gia nghiem ngat (Strict Evaluation)
    trong cac hoi nghi khoa hoc ACL/EMNLP cho bai toan Joint NER & RE.
    
    Entity: Dung ca vi tri span (start, end) va loai thuc the (type).
    Relation: Dung ca vi tri, loai cua 2 thuc the va loai quan he giua chung: (e1, rel, e2).
    """
    total_gold_entities = 0
    total_pred_entities = 0
    correct_entities = 0

    total_gold_relations = 0
    total_pred_relations = 0
    correct_relations = 0

    for gold, pred in zip(gold_docs, pred_docs):
        # 1. Gold Entities: {(start, end, type)}
        gold_ents = {(e["start"], e["end"], e["type"]) for e in gold.get("entities", [])}
        pred_ents = {(e["start"], e["end"], e["type"]) for e in pred.get("entities", [])}

        total_gold_entities += len(gold_ents)
        total_pred_entities += len(pred_ents)
        correct_entities += len(gold_ents & pred_ents)

        # 2. Relations: {( (s1_start, s1_end), rel_type, (s2_start, s2_end) )}
        raw_gold_ents = gold.get("entities", [])
        gold_rels = set()
        for r in gold.get("relations", []):
            h = raw_gold_ents[r["head"]]
            t = raw_gold_ents[r["tail"]]
            gold_rels.add(((h["start"], h["end"]), r["type"], (t["start"], t["end"])))

        raw_pred_ents = pred.get("entities", [])
        pred_rels = set()
        for r in pred.get("relations", []):
            if r["head"] < len(raw_pred_ents) and r["tail"] < len(raw_pred_ents):
                h = raw_pred_ents[r["head"]]
                t = raw_pred_ents[r["tail"]]
                pred_rels.add(((h["start"], h["end"]), r["type"], (t["start"], t["end"])))

        total_gold_relations += len(gold_rels)
        total_pred_relations += len(pred_rels)
        correct_relations += len(gold_rels & pred_rels)

    def calc_prf(correct, pred, gold):
        p = (correct / pred) if pred > 0 else 0.0
        r = (correct / gold) if gold > 0 else 0.0
        f1 = (2 * p * r / (p + r)) if (p + r) > 0 else 0.0
        return {"precision": p * 100, "recall": r * 100, "f1": f1 * 100, "correct": correct, "pred": pred, "gold": gold}

    return {
        "entity": calc_prf(correct_entities, total_pred_entities, total_gold_entities),
        "relation": calc_prf(correct_relations, total_pred_relations, total_gold_relations)
    }
