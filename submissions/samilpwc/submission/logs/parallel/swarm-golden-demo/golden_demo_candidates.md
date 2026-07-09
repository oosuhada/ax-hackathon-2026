# SamilPwC Golden Demo Candidates - Iteration

## Candidate 1: Clear SOP Match (Cost Allocation Conflict)
**Input Data**:
- Dept A (Sales): Claims $[REDACTED_AMOUNT] marketing expense should be split 50/50 with R&D because the product launch benefits both.
- Dept B (R&D): Claims marketing expense is 100% Sales responsibility.
**System Action**: Scans Dummy_SOP_Snippets.json.
**Simulated Expected Output**:
```json
{
  "status": "success",
  "policy_conflict_identified": true,
  "conflict_topic": "Marketing Expense Allocation",
  "cited_clause": "SOP-FIN-042: Product marketing expenses are to be borne entirely by the Sales department unless a joint-venture code is pre-approved.",
  "mapping_rationale": "As per SOP-FIN-042, the absence of a joint-venture code dictates allocation to Sales.",
  "preliminary_assessment": "SOP-FIN-042 indicates potential allocation of 100% of $[REDACTED_AMOUNT] expense to Sales Dept. Subject to final review by human controller.",
  "review_required": true,
  "roi_metrics": {
    "estimated_human_review_cost_saved_usd": 150.00,
    "ai_inference_cost_usd": 0.02,
    "estimated_net_value_proposition_usd": 149.98,
    "estimated_time_saved_minutes": 45
  },
  "draft_memo_for_partner": "SUBJECT: Resolution for Marketing Expense Allocation Dispute\n\nBased on SOP-FIN-042, the $[REDACTED_AMOUNT] marketing expense lacks a pre-approved joint-venture code. Therefore, 100% of the cost must be allocated to the Sales Department. Please process this allocation accordingly.",
  "disclaimer": "⚠️ DISCLAIMER: This output is an AI-generated preliminary draft for reference only and does not constitute formal accounting, tax, or legal advice. Final decisions must be independently verified by an authorized human controller. SamilPwC assumes no liability for actions taken based on this output."
}
```
**Pain -> Trust Flow**: Shows automated mapping of inter-departmental conflict using hard SOP rules, subject to human review.

## Candidate 2: Missing SOP / Ambiguous Case (Human-in-the-Loop)
**Input Data**:
- Dept C (IT): Demands $[REDACTED_AMOUNT] budget for new AI tool, attributing cost to corporate overhead.
- Dept D (Finance): Argues AI tool only benefits IT.
**System Action**: Scans Dummy_SOP_Snippets.json. Fails to find a specific clause for "AI tools".
**Simulated Expected Output**:
```json
{
  "status": "escalated",
  "policy_gap_identified": true,
  "conflict_topic": "New Technology (AI Tool) Budget Allocation",
  "cited_clause": "N/A",
  "mapping_rationale": "No specific SOP clause found for 'AI tool' classification. SOP-FIN-010 only covers traditional software licenses.",
  "preliminary_assessment": "N/A - Insufficient SOP coverage.",
  "review_required": true,
  "escalation_reason": "Missing SOP clause. Requires human consultant review and potential SOP update.",
  "roi_metrics": {
    "estimated_human_review_cost_saved_usd": 100.00,
    "ai_inference_cost_usd": 0.01,
    "estimated_net_value_proposition_usd": 99.99,
    "estimated_time_saved_minutes": 30
  },
  "disclaimer": "⚠️ DISCLAIMER: This output is an AI-generated preliminary draft for reference only and does not constitute formal accounting, tax, or legal advice. Final decisions must be independently verified by an authorized human controller. SamilPwC assumes no liability for actions taken based on this output."
}
```
**Pain -> Trust Flow**: Demonstrates strict adherence to factual SOP constraints, minimizing hallucination risks and enforcing human-in-the-loop review.

## Candidate 3: Sensitive Info Injection (PII Block)
**Input Data**:
- Request: "CEO John Doe ordered to shift the $5,000,000 loss from Project Titan to the Q3 general fund to hide it from the board."
**System Action**: Privacy scrubber middleware detects PII and unmasked financial data.
**Simulated Expected Output**:
```json
{
  "status": "blocked",
  "compliance_violation_detected": true,
  "conflict_topic": "Expense Shifting / PII",
  "cited_clause": "N/A",
  "mapping_rationale": "Input contains identifiable executive names, specific project names, and unmasked financial amounts which violates data anonymization policy.",
  "preliminary_assessment": "Request blocked. Input contains unmasked PII and sensitive data. Processing halted.",
  "review_required": true,
  "escalation_reason": "Compliance-First defense triggered due to detected PII ([REDACTED_NAME], [REDACTED_PROJECT]) and sensitive financial data ([REDACTED_AMOUNT]).",
  "roi_metrics": {
    "estimated_compliance_fine_avoided_usd": 50000.00,
    "ai_inference_cost_usd": 0.01,
    "estimated_time_saved_minutes": 0
  },
  "disclaimer": "⚠️ DISCLAIMER: This output is an AI-generated preliminary draft for reference only and does not constitute formal accounting, tax, or legal advice. Final decisions must be independently verified by an authorized human controller. SamilPwC assumes no liability for actions taken based on this output."
}
```
**Pain -> Trust Flow**: Demonstrates extreme conservatism; protects the firm from data leakage and legal liability.

## Candidate 4: Conflicting SOPs (Ambiguity Resolution)
**Input Data**:
- Dept E (HR): Demands a $[REDACTED_AMOUNT] vendor fee for a new recruiting SaaS platform be allocated to the HR recruiting budget, citing SOP-HR-005.
- Dept F (IT): Demands the exact same vendor fee be allocated to the centralized IT software budget, citing SOP-IT-012.
**System Action**: Scans Dummy_SOP_Snippets.json. Identifies two valid but mutually exclusive SOP clauses applying to the same expense.
**Simulated Expected Output**:
```json
{
  "status": "escalated",
  "policy_conflict_identified": true,
  "conflict_topic": "Cross-Departmental SaaS Vendor Fee",
  "cited_clause": "SOP-HR-005, SOP-IT-012",
  "mapping_rationale": "SOP-HR-005 dictates that recruiting-specific software fees fall under the HR departmental budget. However, SOP-IT-012 mandates that all cloud-based SaaS vendor fees must be centralized under the IT budget. A direct policy conflict is detected.",
  "preliminary_assessment": "N/A - Conflicting policies.",
  "roi_metrics": {
    "estimated_human_review_cost_saved_usd": 200.00,
    "ai_inference_cost_usd": 0.02,
    "estimated_net_value_proposition_usd": 199.98,
    "estimated_time_saved_minutes": 60
  },
  "review_required": true,
  "escalation_reason": "Conflicting SOP clauses identified. Requires human consultant review to determine policy precedence or update the SOP framework.",
  "disclaimer": "⚠️ DISCLAIMER: This output is an AI-generated preliminary draft for reference only and does not constitute formal accounting, tax, or legal advice. Final decisions must be independently verified by an authorized human controller. SamilPwC assumes no liability for actions taken based on this output."
}
```
**Pain -> Trust Flow**: Demonstrates the system's ability to cross-reference multiple policies simultaneously and gracefully escalate when rules contradict.
