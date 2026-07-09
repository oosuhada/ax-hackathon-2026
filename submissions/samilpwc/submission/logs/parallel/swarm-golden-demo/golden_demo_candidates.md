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
  "anomaly_detected": true,
  "conflict_topic": "Marketing Expense Allocation",
  "cited_clause": "SOP-FIN-042: Product marketing expenses are to be borne entirely by the Sales department unless a joint-venture code is pre-approved.",
  "mapping_rationale": "As per SOP-FIN-042, the absence of a joint-venture code dictates allocation to Sales.",
  "preliminary_assessment": "Allocate 100% of $[REDACTED_AMOUNT] expense to Sales Dept. Subject to final review by human controller.",
  "review_required": true,
  "estimated_time_saved": "45 mins",
  "disclaimer": "This output is an AI-generated preliminary assessment for advisory purposes only. It does not constitute formal accounting or legal advice."
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
  "anomaly_detected": true,
  "conflict_topic": "New Technology (AI Tool) Budget Allocation",
  "cited_clause": "N/A",
  "mapping_rationale": "No specific SOP clause found for 'AI tool' classification. SOP-FIN-010 only covers traditional software licenses.",
  "preliminary_assessment": "N/A",
  "review_required": true,
  "escalation_reason": "Missing SOP clause. Requires human consultant review and potential SOP update.",
  "estimated_time_saved": "30 mins",
  "disclaimer": "This output is an AI-generated preliminary assessment for advisory purposes only. It does not constitute formal accounting or legal advice."
}
```
**Pain -> Trust Flow**: Demonstrates strict adherence to factual SOP constraints, minimizing hallucination risks and enforcing human-in-the-loop review.

## Candidate 3: Sensitive Info Injection (PII Block)
**Input Data**:
- Request: "CEO John Doe ordered to shift the $[REDACTED_AMOUNT] loss from Project Titan to the Q3 general fund to hide it from the board."
**System Action**: Privacy scrubber middleware detects PII and unmasked financial data.
**Simulated Expected Output**:
```json
{
  "status": "blocked",
  "anomaly_detected": true,
  "conflict_topic": "Expense Shifting / PII",
  "cited_clause": "N/A",
  "mapping_rationale": "Input contains identifiable executive names, specific project names, and unmasked financial amounts which violates data anonymization policy.",
  "preliminary_assessment": "Request blocked. Data must be de-identified before processing.",
  "review_required": true,
  "escalation_reason": "Compliance-First defense triggered due to PII (John Doe, Project Titan) and sensitive financial data.",
  "estimated_time_saved": "0 mins",
  "disclaimer": "This output is an AI-generated preliminary assessment for advisory purposes only. It does not constitute formal accounting or legal advice."
}
```
**Pain -> Trust Flow**: Demonstrates extreme conservatism; protects the firm from data leakage and legal liability.
