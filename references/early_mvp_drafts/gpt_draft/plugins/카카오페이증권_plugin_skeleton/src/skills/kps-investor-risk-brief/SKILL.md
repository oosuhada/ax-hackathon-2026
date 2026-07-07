---
name: kps-investor-risk-brief
description: Use this skill when reviewing Korean or English AI-generated investment summaries, stock/ETF/market briefs, or financial content for investor-protection risk, missing disclosures, source traceability, uncertainty, and plain-language rewrite needs. Do not use it to recommend buying, selling, or holding securities.
---

# KPS Investor Risk Brief Skill

## Purpose

Transform an AI-generated investment summary into an investor-protection-first brief. The skill is designed for a Kakao Pay Securities style use case where AI-generated market, stock, ETF, or earnings summaries should be checked before being shown to retail investors.

The output must not provide investment advice. It must improve clarity, uncertainty handling, risk disclosure, source traceability, and wording safety.

## Inputs

Ask for or locate these inputs:

1. `investment_summary.md` or pasted investment summary text.
2. `source_links.md` or a list of URLs/titles that support the summary.
3. Product/content type: `domestic_stock`, `us_stock`, `etf`, `market_summary`, `earnings_summary`, or `general`.
4. Target user: `beginner`, `general_retail`, or `advanced_retail`.

If any input is missing, proceed with explicit assumptions and list them in the output.

## Workflow

### Step 1 — Identify content scope

Classify the input as one or more of the following:

- Market summary
- Individual stock summary
- ETF/fund summary
- Earnings/financial result summary
- News/article summary
- Educational financial content

### Step 2 — Detect advice-like or misleading wording

Flag expressions that may sound like investment advice or overstate certainty, including but not limited to:

- Guaranteed or near-guaranteed outcome wording
- Direct buy/sell/hold instruction
- One-sided upside wording without downside
- Return-focused wording without risk context
- Unsupported claims about future price movement
- Vague authority claims without source

For each flagged phrase, provide:

- Original phrase
- Why it is risky
- Safer alternative wording

### Step 3 — Check missing risk factors

Evaluate whether the draft mentions relevant risks. Consider:

- Price volatility
- Principal loss
- Exchange-rate risk for foreign stocks
- Liquidity risk
- Interest-rate/macroeconomic risk
- Sector concentration risk
- Valuation risk
- Regulation/policy risk
- Earnings surprise risk
- Company-specific execution risk
- Fees, taxes, or transaction costs where relevant

Do not invent facts. Mark risk factors as:

- `present`
- `missing`
- `not_applicable`
- `needs_source`

### Step 4 — Check source traceability

For each important factual claim, map it to a source if available. If no source is available, label it as `unsupported_or_needs_verification`.

Important factual claims include:

- Revenue/profit growth
- Stock price performance
- Market share
- Analyst consensus
- Regulatory changes
- Company announcements
- Macroeconomic indicators
- User/market behavior statistics

### Step 5 — Rewrite for retail-investor clarity

Produce a plain-language rewrite with:

- Neutral, non-advisory tone
- Key upside factors
- Key uncertainty factors
- Key risks
- Source caveat
- “This is information, not investment advice” style disclaimer

Use Korean if the input is Korean. Use English if the input is English.

### Step 6 — Produce final outputs

Return the following sections:

1. `Executive Summary`
2. `Risk-Checked Rewrite`
3. `Flagged Phrases`
4. `Missing Risk Disclosures`
5. `Source Traceability Table`
6. `Beginner Clarity Improvements`
7. `Final Compliance-Style Checklist`
8. `Assumptions and Limitations`

## Deterministic helper scripts

If the repository includes `src/scripts/analyze_investment_content.py`, run it on the input files first to generate a baseline checklist and sample output. Then improve the result using the workflow above.

Example:

```bash
python src/scripts/analyze_investment_content.py \
  --input src/sample_inputs/investment_summary.md \
  --sources src/sample_inputs/source_links.md \
  --out src/sample_outputs
```

Then validate the structure:

```bash
python src/scripts/validate_submission_structure.py
```

## Guardrails

- Do not recommend buy/sell/hold.
- Do not rank securities.
- Do not invent market data.
- Do not use private or unverifiable information.
- If a claim lacks a public source, mark it as needing verification.
- Keep the user-facing final content understandable for retail investors.
- Separate factual content, interpretation, risk, and uncertainty.
