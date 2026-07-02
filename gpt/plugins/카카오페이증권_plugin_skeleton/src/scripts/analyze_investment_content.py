#!/usr/bin/env python3
"""
Baseline deterministic helper for the kps-investor-risk-brief Codex plugin.

This script does not replace Codex/LLM reasoning. It provides a simple,
repeatable baseline so the submission has an executable component.

Usage:
  python src/scripts/analyze_investment_content.py \
    --input src/sample_inputs/investment_summary.md \
    --sources src/sample_inputs/source_links.md \
    --out src/sample_outputs
"""

from __future__ import annotations

import argparse
import json
import re
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import List, Dict


ADVICE_OR_CERTAINTY_PATTERNS = {
    "direct_investment_action": [
        r"매수",
        r"매도",
        r"보유",
        r"buy\b",
        r"sell\b",
        r"hold\b",
    ],
    "certainty_or_guarantee": [
        r"반드시",
        r"무조건",
        r"확실",
        r"보장",
        r"guarantee",
        r"certain",
        r"without risk",
    ],
    "one_sided_upside": [
        r"상승 가능성",
        r"상승할 것",
        r"고성장",
        r"장기 성장",
        r"기대됩니다",
        r"upside",
        r"growth potential",
    ],
}

RISK_FACTORS = {
    "price_volatility": ["변동성", "주가 변동", "가격 변동", "volatility", "price fluctuation"],
    "principal_loss": ["원금 손실", "손실 가능성", "principal loss", "loss of principal"],
    "exchange_rate": ["환율", "달러", "외환", "exchange rate", "FX"],
    "fees_taxes_costs": ["수수료", "세금", "거래비용", "fee", "tax", "cost"],
    "liquidity": ["유동성", "liquidity"],
    "valuation": ["밸류에이션", "고평가", "valuation"],
    "macro_rate": ["금리", "경기", "인플레이션", "interest rate", "macro", "inflation"],
    "regulatory": ["규제", "정책", "regulation", "policy"],
}


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8") if path.exists() else ""


def find_patterns(text: str, pattern_map: Dict[str, List[str]]) -> Dict[str, List[str]]:
    findings: Dict[str, List[str]] = {}
    for label, patterns in pattern_map.items():
        hits: List[str] = []
        for pattern in patterns:
            if re.search(pattern, text, flags=re.IGNORECASE):
                hits.append(pattern)
        findings[label] = hits
    return findings


def split_sentences(text: str) -> List[str]:
    normalized = re.sub(r"\s+", " ", text.strip())
    if not normalized:
        return []
    parts = re.split(r"(?<=[.!?。！？다요])\s+", normalized)
    return [p.strip() for p in parts if p.strip()]


@dataclass
class FlaggedPhrase:
    phrase: str
    risk_type: str
    reason: str
    safer_wording: str


def extract_flagged_phrases(text: str) -> List[FlaggedPhrase]:
    sentences = split_sentences(text)
    flagged: List[FlaggedPhrase] = []
    for sentence in sentences:
        for label, patterns in ADVICE_OR_CERTAINTY_PATTERNS.items():
            for pattern in patterns:
                if re.search(pattern, sentence, flags=re.IGNORECASE):
                    if label == "direct_investment_action":
                        reason = "투자 조언 또는 매매 지시처럼 오해될 수 있습니다."
                        safer = "정보 제공 목적의 중립적 표현으로 바꾸고, 투자 판단은 투자자 본인 책임임을 분리해 고지하세요."
                    elif label == "certainty_or_guarantee":
                        reason = "투자 결과가 확정적이라는 인상을 줄 수 있습니다."
                        safer = "가능성, 조건, 불확실성을 함께 제시하세요."
                    else:
                        reason = "상방 요인만 강조하고 하방 리스크가 약하게 보일 수 있습니다."
                        safer = "성장 요인과 변동성/밸류에이션/거시 리스크를 함께 제시하세요."
                    flagged.append(FlaggedPhrase(sentence, label, reason, safer))
                    break
    # Deduplicate by sentence + type
    seen = set()
    deduped = []
    for item in flagged:
        key = (item.phrase, item.risk_type)
        if key not in seen:
            deduped.append(item)
            seen.add(key)
    return deduped


def assess_risk_factors(text: str) -> Dict[str, str]:
    lower = text.lower()
    results: Dict[str, str] = {}
    for risk, keywords in RISK_FACTORS.items():
        results[risk] = "present" if any(k.lower() in lower for k in keywords) else "missing"
    return results


def parse_sources(source_text: str) -> List[str]:
    lines = [line.strip("-• \t") for line in source_text.splitlines()]
    return [line for line in lines if line and not line.startswith("#")]


def build_markdown_report(summary_text: str, sources_text: str) -> str:
    flagged = extract_flagged_phrases(summary_text)
    risk_factors = assess_risk_factors(summary_text)
    sources = parse_sources(sources_text)

    unsupported_note = "needs_verification" if not sources else "source_review_required"

    lines: List[str] = []
    lines.append("# KPS Investor Risk Brief — Sample Output")
    lines.append("")
    lines.append("## 1. Executive Summary")
    lines.append("")
    lines.append("- Content type: sample investment / market summary")
    lines.append("- Target user: retail investor, beginner-to-general level")
    lines.append(f"- Flagged advice/certainty phrases: {len(flagged)}")
    lines.append(f"- Available source entries: {len(sources)}")
    lines.append("- Recommended action: rewrite into neutral information-first wording and add missing risk disclosures before publication.")
    lines.append("")

    lines.append("## 2. Risk-Checked Rewrite")
    lines.append("")
    lines.append("> 아래 문안은 예시용 자동 생성 초안입니다. 최종 제출 전 실제 공개자료와 금융소비자보호 기준에 맞춰 검토하세요.")
    lines.append("")
    lines.append("이 콘텐츠는 특정 종목이나 금융상품의 매수·매도·보유를 권유하기 위한 것이 아니라, 공개 정보를 바탕으로 주요 요인과 유의점을 정리한 참고용 정보입니다. 성장 기대 요인이 있더라도 실제 투자 성과는 시장 변동성, 금리, 환율, 밸류에이션, 기업 실적, 규제 변화 등에 따라 달라질 수 있습니다. 투자자는 원금 손실 가능성을 포함한 위험을 충분히 확인한 뒤 본인의 판단과 책임으로 의사결정을 해야 합니다.")
    lines.append("")

    lines.append("## 3. Flagged Phrases")
    lines.append("")
    lines.append("| Original phrase | Risk type | Why it matters | Safer wording |")
    lines.append("|---|---|---|---|")
    if flagged:
        for item in flagged:
            phrase = item.phrase.replace("|", "\\|")
            lines.append(f"| {phrase} | {item.risk_type} | {item.reason} | {item.safer_wording} |")
    else:
        lines.append("| No obvious phrase flagged by baseline script | - | Manual review still required | Check source traceability and missing risks |")
    lines.append("")

    lines.append("## 4. Missing Risk Disclosures")
    lines.append("")
    lines.append("| Risk factor | Status | Suggested disclosure |")
    lines.append("|---|---|---|")
    suggested = {
        "price_volatility": "시장 상황에 따라 가격이 크게 변동할 수 있습니다.",
        "principal_loss": "투자 원금 손실 가능성이 있습니다.",
        "exchange_rate": "해외 자산은 환율 변동에 따라 원화 기준 수익률이 달라질 수 있습니다.",
        "fees_taxes_costs": "거래 수수료, 세금, 환전 비용 등이 실제 수익률에 영향을 줄 수 있습니다.",
        "liquidity": "시장 상황에 따라 원하는 시점에 거래가 어려울 수 있습니다.",
        "valuation": "성장 기대가 이미 가격에 반영되었을 가능성이 있습니다.",
        "macro_rate": "금리, 경기, 인플레이션 등 거시 환경 변화의 영향을 받을 수 있습니다.",
        "regulatory": "규제와 정책 변화가 기업가치와 시장심리에 영향을 줄 수 있습니다.",
    }
    for risk, status in risk_factors.items():
        lines.append(f"| {risk} | {status} | {suggested.get(risk, '관련 위험을 명확히 고지하세요.')} |")
    lines.append("")

    lines.append("## 5. Source Traceability Table")
    lines.append("")
    lines.append("| Claim | Source | Status | Note |")
    lines.append("|---|---|---|---|")
    sentences = split_sentences(summary_text)[:8]
    if sentences:
        for idx, sentence in enumerate(sentences, 1):
            source = sources[min(idx - 1, len(sources) - 1)] if sources else "not provided"
            lines.append(f"| {sentence.replace('|', '\\|')} | {source.replace('|', '\\|')} | {unsupported_note} | Verify before final submission |")
    else:
        lines.append("| No input claims detected | not provided | needs_verification | Add input content |")
    lines.append("")

    lines.append("## 6. Beginner Clarity Improvements")
    lines.append("")
    lines.append("- Separate what happened, why it may matter, and what could go wrong.")
    lines.append("- Avoid one-directional phrases such as ‘상승 가능성이 높다’ unless uncertainty and downside risks are stated together.")
    lines.append("- Define technical terms such as valuation, volatility, liquidity, and exchange-rate risk in plain language.")
    lines.append("")

    lines.append("## 7. Final Compliance-Style Checklist")
    lines.append("")
    checklist = [
        "Does not include direct buy/sell/hold recommendation.",
        "Separates upside factors from risks.",
        "Mentions principal-loss possibility where relevant.",
        "Mentions exchange-rate risk for foreign assets where relevant.",
        "Avoids guaranteed-return wording.",
        "Identifies unsupported claims.",
        "Uses beginner-friendly language.",
        "Includes information-not-advice framing.",
    ]
    for item in checklist:
        lines.append(f"- [ ] {item}")
    lines.append("")

    lines.append("## 8. Assumptions and Limitations")
    lines.append("")
    lines.append("- This baseline script uses keyword heuristics and cannot replace legal, compliance, or professional financial review.")
    lines.append("- The Codex skill should perform an additional contextual review using public, verifiable sources.")
    lines.append("- Final submission must cite exact public sources and must not rely on private or unverifiable information.")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="Path to investment summary markdown/text file")
    parser.add_argument("--sources", required=False, help="Path to source links markdown/text file")
    parser.add_argument("--out", required=True, help="Output directory")
    args = parser.parse_args()

    input_path = Path(args.input)
    source_path = Path(args.sources) if args.sources else None
    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)

    summary_text = read_text(input_path)
    sources_text = read_text(source_path) if source_path else ""

    flagged = [asdict(item) for item in extract_flagged_phrases(summary_text)]
    risk_factors = assess_risk_factors(summary_text)
    sources = parse_sources(sources_text)

    checklist = {
        "input_file": str(input_path),
        "source_file": str(source_path) if source_path else None,
        "flagged_phrases": flagged,
        "risk_factor_status": risk_factors,
        "source_count": len(sources),
        "needs_manual_review": True,
    }

    (out_dir / "compliance_checklist.json").write_text(
        json.dumps(checklist, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    (out_dir / "risk_checked_summary.md").write_text(
        build_markdown_report(summary_text, sources_text), encoding="utf-8"
    )
    (out_dir / "source_traceability_table.md").write_text(
        "# Source Traceability Table\n\n" +
        "| Source entry | Status | Note |\n|---|---|---|\n" +
        "\n".join(f"| {s.replace('|', '\\|')} | needs_verification | Replace with exact public source metadata |" for s in sources),
        encoding="utf-8",
    )

    print(f"Wrote outputs to {out_dir}")


if __name__ == "__main__":
    main()
