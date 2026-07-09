#!/usr/bin/env python3
import argparse, csv, json
from pathlib import Path

USECASE_MAP = {
    "report": "Management reporting agent",
    "contract": "Contract risk review assistant",
    "competitor": "Market research agent",
    "policy": "Internal policy Q&A assistant",
    "proposal": "Proposal drafting copilot",
    "invoice": "Invoice reconciliation assistant",
}

def norm_score(value):
    v = (value or "").lower()
    if v == "high": return 5
    if v == "medium": return 3
    if v == "low": return 1
    return 2

def infer_usecase(row):
    text = f"{row.get('process_name','')} {row.get('current_pain_point','')}".lower()
    for key, uc in USECASE_MAP.items():
        if key in text:
            return uc
    return "Workflow automation copilot"

def priority_class(impact, feasibility, risk):
    if impact >= 4 and feasibility >= 4 and risk <= 3:
        return "Quick Win"
    if impact >= 4 and feasibility >= 3 and risk >= 4:
        return "Governance First"
    if impact >= 4 and feasibility <= 2:
        return "Strategic Bet"
    if impact <= 2:
        return "Low Priority"
    return "PoC Candidate"

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--processes", required=True)
    p.add_argument("--context", required=False)
    p.add_argument("--out", required=True)
    args = p.parse_args()

    out = Path(args.out); out.mkdir(parents=True, exist_ok=True)
    rows = list(csv.DictReader(Path(args.processes).read_text(encoding="utf-8-sig").splitlines()))
    portfolio = []
    for row in rows:
        freq = row.get("frequency", "")
        data = norm_score(row.get("data_availability"))
        risk = norm_score(row.get("risk_sensitivity"))
        repetition = 5 if freq in {"daily", "weekly"} else 3 if freq == "monthly" else 2
        impact = 4 if any(word in row.get("current_pain_point", "").lower() for word in ["manual", "delay", "error", "repeated", "too long"]) else 3
        feasibility = round((data + repetition) / 2)
        usecase = infer_usecase(row)
        cls = priority_class(impact, feasibility, risk)
        portfolio.append({
            "process_id": row.get("process_id"),
            "department": row.get("department"),
            "process_name": row.get("process_name"),
            "pain_point": row.get("current_pain_point"),
            "proposed_usecase": usecase,
            "impact": impact,
            "feasibility": feasibility,
            "data_readiness": data,
            "risk": risk,
            "priority_class": cls,
        })

    portfolio = sorted(portfolio, key=lambda x: (x["priority_class"] != "Quick Win", -x["impact"], -x["feasibility"], x["risk"]))
    (out / "ax_prioritization_matrix.json").write_text(json.dumps(portfolio, ensure_ascii=False, indent=2), encoding="utf-8")

    md = ["# Sample AX Use Case Prioritization Matrix\n\n"]
    md.append("| Process | Proposed Use Case | Impact | Feasibility | Data | Risk | Class |\n|---|---|---:|---:|---:|---:|---|\n")
    for x in portfolio:
        md.append(f"| {x['process_name']} | {x['proposed_usecase']} | {x['impact']} | {x['feasibility']} | {x['data_readiness']} | {x['risk']} | {x['priority_class']} |\n")
    md.append("\n## Notes\n\n- Scores are generated from sample inputs and should be reviewed by a human consultant.\n- ROI numbers are not fabricated; financial estimates require client data.\n- High-risk workflows require governance before production deployment.\n")
    (out / "ax_prioritization_matrix.md").write_text("".join(md), encoding="utf-8")

    top3 = portfolio[:3]
    poc = ["# Sample 4-Week PoC Plan\n\n"]
    for i, x in enumerate(top3, 1):
        poc.append(f"## PoC {i}: {x['proposed_usecase']}\n\n")
        poc.append(f"- Process: {x['process_name']}\n")
        poc.append(f"- Target department: {x['department']}\n")
        poc.append(f"- Pain point: {x['pain_point']}\n")
        poc.append("- Week 1: define workflow, collect sample documents/data, define success metrics\n")
        poc.append("- Week 2: build prompt/skill prototype and human review workflow\n")
        poc.append("- Week 3: test on sample cases and record failure modes\n")
        poc.append("- Week 4: refine, document governance checklist, prepare executive demo\n")
        poc.append("- Human-in-the-loop: required before external/client-facing use\n\n")
    (out / "poc_plan.md").write_text("".join(poc), encoding="utf-8")

    one = """# Executive One-Pager\n\n## Recommendation\n\nStart with AX use cases that combine high repetition, available data, measurable workflow improvement, and manageable risk.\n\n## Initial portfolio\n\nSee `ax_prioritization_matrix.md` for scored use cases.\n\n## First decision\n\nSelect one Quick Win or PoC Candidate, define success metrics, and run a 4-week human-in-the-loop pilot.\n\n## Governance note\n\nHigh-risk legal, finance, or privacy-sensitive workflows should not move to production without access control, audit logging, and human approval.\n"""
    (out / "executive_onepager.md").write_text(one, encoding="utf-8")
    print(f"Wrote outputs to {out}")

if __name__ == "__main__":
    main()
