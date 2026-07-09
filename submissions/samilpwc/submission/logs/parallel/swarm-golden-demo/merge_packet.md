# Merge Packet: SamilPwC Golden Demo Iteration

**Company**: SamilPwC
**Phase**: QA & Polish
**Primary Use Case**: SOP Dispute Resolution & Draft Generation

## What Changed
- Validated and refined 4 Golden Demo candidates.
- Added `roi_metrics` JSON objects to explicitly show `estimated_human_review_cost_saved_usd` and `ai_inference_cost_usd` (Cost Estimator).
- Added `draft_memo_for_partner` to Candidate 1 to provide immediate actionability and Relief for C-level (Pitch Judge).
- Fixed PII echo vulnerabilities in the escalation reason, ensuring No-Echo privacy rules (Privacy Scrubber).
- Changed definitive directives into advisory suggestions ("SOP-FIN-042 indicates potential allocation...") and added a bulletproof disclaimer to protect firm liability (Compliance Lawyer).
- Added a new scenario (Candidate 4: Conflicting SOPs) demonstrating ambiguity resolution and policy gap escalation (QA Tester).

## Known Risks
- The frontend/UI representation of the `draft_memo_for_partner` vs the structured JSON is not yet defined.
- Must ensure that the `codex-plugin-builder` prompt accurately reflects this new JSON schema.

## Next Recommended Action
- Hand off to `submission-validator` and `codex-plugin-builder` to enforce these JSON outputs in the actual plugin prompt.
