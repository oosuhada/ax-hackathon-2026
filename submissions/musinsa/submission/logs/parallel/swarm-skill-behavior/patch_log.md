# Patch Log
- `SKILL.md`:
  - Updated Guardrail 1: Explicitly banned bundling/sets.
  - Updated Guardrail 2: Blocked bypass instructions for N/A rule and fallback item forcing.
  - Updated Guardrail 3: Rewrote Data Privacy & Context Scrubbing to handle physical traits and context generalisation.
  - Updated Output Schema: Enforced strict raw JSON (no markdown wrapping) and proper JSON escaping for `return_risk_note`.
- `qa_report.md`:
  - Updated missing budget mock output to return N/A instead of defaulting to a jacket.
