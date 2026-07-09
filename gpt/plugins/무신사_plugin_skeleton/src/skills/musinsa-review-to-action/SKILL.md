---
name: musinsa-review-to-action
description: Use this skill when turning fashion commerce product reviews, customer Q&A, return reasons, or seller feedback into prioritized seller/MD actions. The skill is designed for a Musinsa-style marketplace or brand operations workflow. It should not fabricate sales metrics or private platform data.
---

# Musinsa Review-to-Action Skill

## Purpose

Transform customer review text into practical seller-facing actions. The goal is not to summarize reviews for consumers, but to help sellers, MDs, product planners, CS operators, and detail-page editors convert customer feedback into concrete improvements.

This skill is designed for a Musinsa-style marketplace context where brands need to understand why customers hesitate, complain, return items, or misunderstand product information.

## Inputs

Ask for or locate these inputs:

1. `product_reviews.csv` or pasted review text.
2. `product_context.md` with product category, target customer, price range, key product claims, size guide, and detail-page information if available.
3. Optional `return_reasons.csv`, `qna.csv`, or sales context.
4. The desired output language: Korean by default.

If data is missing, proceed with explicit assumptions and mark missing fields in the output.

## Workflow

### Step 1 — Inspect input data

Identify available columns such as:

- review text
- rating
- product option
- size purchased
- customer body/fit information if available
- date
- helpful count
- return reason
- seller response

Do not infer private platform metrics that are not present.

### Step 2 — Classify review themes

Classify feedback into actionable categories:

- Size / fit
- Material / fabric feel
- Color mismatch
- Photo-detail mismatch
- Quality / durability
- Price-value perception
- Shipping / packaging
- Customer service
- Styling / coordination
- Reorder / loyalty signal
- Detail-page information gap

For each category, capture representative evidence snippets.

### Step 3 — Separate consumer summary from seller action

Produce two layers:

1. `Consumer-facing insight`: what customers are saying.
2. `Seller-facing action`: what the seller or MD should change.

Do not stop at sentiment summary. Every major insight should map to a proposed action.

### Step 4 — Prioritize actions

Score each action from 1 to 5 on:

- Frequency of evidence
- Customer pain intensity
- Conversion impact hypothesis
- Return/refund impact hypothesis
- Ease of implementation
- Confidence based on available evidence

Then classify into:

- `Quick Fix`: high impact, easy implementation
- `Product Improvement`: product/production change needed
- `Detail Page Fix`: copy, size guide, image, or information change
- `CS Automation`: FAQ or response macro candidate
- `Marketing Opportunity`: copy, bundle, or campaign angle
- `Needs More Data`: not enough evidence

### Step 5 — Generate practical outputs

Return the following sections:

1. `Executive Summary`
2. `Top Review Themes`
3. `Review-to-Action Matrix`
4. `Detail Page Fixes`
5. `CS FAQ and Response Macros`
6. `Product Improvement Ideas`
7. `Marketing Copy Opportunities`
8. `Risks, Assumptions, and Missing Data`
9. `Validation Checklist`

## Deterministic helper scripts

If the repository includes `src/scripts/analyze_review_feedback.py`, run it on sample input first to generate baseline counts and template outputs. Then use this skill to improve the analysis.

Example:

```bash
python src/scripts/analyze_review_feedback.py \
  --reviews src/sample_inputs/product_reviews.csv \
  --context src/sample_inputs/product_context.md \
  --out src/sample_outputs
```

Then validate the submission structure:

```bash
python src/scripts/validate_submission_structure.py
```

## Guardrails

- Do not claim access to Musinsa internal data.
- Do not fabricate sales, conversion, or return rates.
- Use public sources only for problem evidence.
- Use sample data only for demonstration.
- Clearly distinguish evidence from hypothesis.
- Do not make discriminatory or sensitive inferences about customers.
- Keep recommendations practical for sellers and MDs.
