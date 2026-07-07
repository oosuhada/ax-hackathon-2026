---
name: samil-ax-usecase-prioritizer
description: Use this skill when evaluating enterprise AI transformation opportunities, prioritizing GenAI/AX use cases, designing PoC roadmaps, and producing consulting-style executive summaries. The skill is designed for a Samil PwC-style AX consulting workflow.
---

# Samil AX Use Case Prioritizer Skill

## Purpose

Convert a company’s business process list, pain points, data availability, and risk context into a prioritized AI transformation use-case portfolio. The output should help consultants or internal strategy teams identify quick wins, strategic bets, risk-heavy items, and PoC candidates.

This skill is not a generic ideation tool. It should produce a structured, evidence-based prioritization matrix and implementation plan.

## Inputs

Ask for or locate these inputs:

1. `business_processes.csv` with process name, department, current pain points, frequency, data availability, and risk sensitivity.
2. `company_context.md` with industry, company size, strategic priorities, constraints, and AX goals.
3. Optional: current systems, data maturity, compliance constraints, target timeline.
4. Desired output language: Korean by default.

If inputs are incomplete, proceed with assumptions and list them explicitly.

## Workflow

### Step 1 — Understand business context

Summarize:

- Industry
- Primary business model
- Strategic priorities
- Major operational bottlenecks
- Data and system maturity
- Regulatory or compliance sensitivity

### Step 2 — Convert processes into AX use cases

For each process, generate one or more AI/automation opportunities such as:

- Research agent
- Document analysis agent
- Reporting automation
- Customer support assistant
- Forecasting and anomaly detection
- Contract/risk review assistant
- Knowledge management assistant
- Workflow orchestration agent
- Data quality or reconciliation assistant

### Step 3 — Score use cases

Score each use case from 1 to 5 on:

- Business impact
- Cost/time reduction potential
- Revenue or decision-quality impact
- Data availability
- Implementation feasibility
- Repetition/volume
- Risk/compliance sensitivity
- Change management difficulty
- Measurability
- Strategic alignment

### Step 4 — Classify portfolio

Classify use cases into:

- `Quick Win`: feasible, measurable, low risk
- `Strategic Bet`: high impact but requires investment/change
- `Governance First`: valuable but needs risk/data controls first
- `Low Priority`: low impact or weak data availability
- `Do Not Start Yet`: high risk with unclear value

### Step 5 — Generate PoC plan

For top 3 use cases, produce:

- Problem statement
- Target user
- Required data
- Minimum viable workflow
- Success metrics
- 4-week PoC plan
- Risks and mitigations
- Human-in-the-loop design
- Governance checklist

### Step 6 — Produce executive-ready outputs

Return:

1. `Executive One-Page Summary`
2. `AX Use Case Portfolio`
3. `Prioritization Matrix`
4. `Top 3 PoC Plans`
5. `Data and System Requirements`
6. `Risk and Governance Checklist`
7. `Change Management Notes`
8. `Assumptions and Open Questions`

## Deterministic helper scripts

If the repository includes `src/scripts/prioritize_ax_usecases.py`, run it first to generate baseline scoring and markdown outputs. Then use the skill to improve the recommendations.

Example:

```bash
python src/scripts/prioritize_ax_usecases.py \
  --processes src/sample_inputs/business_processes.csv \
  --context src/sample_inputs/company_context.md \
  --out src/sample_outputs
```

Then validate the submission structure:

```bash
python src/scripts/validate_submission_structure.py
```

## Guardrails

- Do not claim access to Samil PwC client data.
- Do not invent confidential company information.
- Use public sources only for problem evidence.
- Keep all ROI estimates as hypotheses unless numeric evidence is provided.
- Distinguish business impact from technical feasibility.
- Include governance and human review for high-risk workflows.
- Make outputs usable as consulting deliverables, not just brainstorming notes.
