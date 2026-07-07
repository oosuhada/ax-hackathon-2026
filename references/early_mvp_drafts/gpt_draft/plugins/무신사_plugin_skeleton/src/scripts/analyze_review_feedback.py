#!/usr/bin/env python3
import argparse, csv, json, re
from pathlib import Path

THEMES = {
    "size_fit": ["핏", "작", "크", "사이즈", "허리", "소매", "길"],
    "color_photo": ["색", "사진", "노란", "어둡", "밝"],
    "material_quality": ["재질", "얇", "보풀", "품질", "부드", "두껍"],
    "shipping_packaging": ["배송", "포장"],
    "styling_marketing": ["코디", "출근룩", "다른 색", "사고 싶"],
    "price_value": ["가격", "가성비", "비싸", "가격 대비"],
}

def classify(text):
    hits = []
    for theme, keywords in THEMES.items():
        if any(k in text for k in keywords):
            hits.append(theme)
    return hits or ["uncategorized"]

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--reviews", required=True)
    p.add_argument("--context", required=False)
    p.add_argument("--out", required=True)
    args = p.parse_args()

    out = Path(args.out); out.mkdir(parents=True, exist_ok=True)
    rows = list(csv.DictReader(Path(args.reviews).read_text(encoding="utf-8-sig").splitlines()))
    counts = {k: 0 for k in THEMES}
    counts["uncategorized"] = 0
    evidence = {k: [] for k in counts}

    for row in rows:
        text = row.get("review_text", "")
        for t in classify(text):
            counts[t] += 1
            if len(evidence[t]) < 3:
                evidence[t].append(text)

    actions = []
    for theme, count in sorted(counts.items(), key=lambda x: x[1], reverse=True):
        if count == 0: continue
        if theme == "size_fit":
            action = "Add clearer fit notes, option-level sizing guidance, and reviewer size examples."
            action_type = "Detail Page Fix"
        elif theme == "color_photo":
            action = "Add natural-light photos and color disclaimer by option."
            action_type = "Detail Page Fix"
        elif theme == "material_quality":
            action = "Clarify material thickness/care and investigate quality issues such as pilling."
            action_type = "Product Improvement"
        elif theme == "shipping_packaging":
            action = "Preserve shipping/packaging strength as review-highlight copy."
            action_type = "Marketing Opportunity"
        elif theme == "styling_marketing":
            action = "Add styling photos and cross-sell copy based on positive use cases."
            action_type = "Marketing Opportunity"
        elif theme == "price_value":
            action = "Reframe value proposition or address quality concerns."
            action_type = "Product/Marketing"
        else:
            action = "Review manually and gather more data."
            action_type = "Needs More Data"
        actions.append({"theme": theme, "count": count, "evidence": evidence[theme], "recommended_action": action, "action_type": action_type})

    (out / "action_matrix.json").write_text(json.dumps(actions, ensure_ascii=False, indent=2), encoding="utf-8")

    md = ["# Sample Review-to-Action Report\n"]
    md.append("## Executive Summary\n")
    md.append(f"Analyzed {len(rows)} sample reviews. Highest-frequency themes are listed below. This is a sample output; final submission should use public evidence and task-specific inputs.\n")
    md.append("## Review-to-Action Matrix\n")
    md.append("| Theme | Count | Action Type | Recommended Action | Evidence |\n|---|---:|---|---|---|\n")
    for a in actions:
        ev = " / ".join(a["evidence"]).replace("|", " ")
        md.append(f"| {a['theme']} | {a['count']} | {a['action_type']} | {a['recommended_action']} | {ev} |\n")
    md.append("\n## Validation Notes\n\n- Recommendations are generated only from sample input text.\n- No sales or conversion metrics are fabricated.\n- Human review is required before using recommendations in production.\n")
    (out / "review_action_report.md").write_text("".join(md), encoding="utf-8")

    faq = """# Sample FAQ and Macro Drafts\n\n## FAQ candidates\n\n1. Q: 사이즈가 작게 나온 편인가요?\n   A: 일부 리뷰에서 허리와 소매 길이에 대한 의견이 있어, 상세 사이즈와 착용 예시를 확인한 뒤 구매해 주세요.\n\n2. Q: 실제 색상은 상세페이지와 동일한가요?\n   A: 조명과 화면 설정에 따라 차이가 있을 수 있으며, 옵션별 자연광 사진을 추가로 확인하는 것을 권장합니다.\n\n## Seller macro candidates\n\n- 색상 차이 문의: 고객님, 화면 설정과 촬영 조명에 따라 색상이 다르게 보일 수 있습니다. 옵션별 실제 착용컷과 자연광 사진을 참고해 주세요.\n"""
    (out / "faq_macro_drafts.md").write_text(faq, encoding="utf-8")
    print(f"Wrote outputs to {out}")

if __name__ == "__main__":
    main()
