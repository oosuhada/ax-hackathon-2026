# Findings Backlog

## Resolved
- **UI Parser Vulnerabilities**: Output format allowed markdown, missing strict schema, and missing keys for optional fields. Resolved by adding a strict JSON schema block and forbidding markdown blocks.
- **Nested Quotes in Disclaimer**: The disclaimer in constraints had nested quotes which could break JSON string values. Resolved by removing outer quotes.
- **Compliance: Alternative Assets**: Wording implied that while alternative assets are out of domain, stocks might be within domain for consultation. Resolved by explicitly stating all assets are out of domain for investment recommendations.
- **Compliance: "HOLD" Recommendation**: "보류(HOLD) 중입니다" implied a hold recommendation. Resolved by using objective metrics only without judgment.

## Unresolved Risks
- **LLM Hallucination Risk**: As noted by security-auditor, while prompt-level defenses are strong, LLM hallucination cannot be 100% ruled out without an external Guardrail model.
