# Findings Backlog (Iteration 2)

## Resolved
- **Indirect Profiling**: Added explicit rule to prevent combination of metadata (age, asset, job) from inferring individual behavior.
- **Bandwagon Backfire**: Added fallback response to prevent inciting FOMO if benchmark data shows majority "Buy".
- **Implicit Endorsement Traps**: Explicitly banned designating any ETF as "safe" and comparing the relative risk of two specific stocks.
- **Strict Schema Enforcement**: Removed `system_fallback_message` to prevent architectural contradiction and enforced strict JSON schema types with a ban on hallucinated fields.

## Unresolved Risks
- **LLM Hallucination Risk**: As noted by security-auditor, while prompt-level defenses are strong, LLM hallucination cannot be 100% ruled out without an external Guardrail model.
- **Data Poisoning in Dummy_Peer_Data.json**: If the external API provides manipulated dummy data, the bandwagon logic might still behave unpredictably despite fallbacks.
