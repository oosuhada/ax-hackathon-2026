# Compliance & Security Gate Report

## 1. 카카오페이증권 (KakaoPaySec) - fomo-defense-agent
- **Data Privacy (Scrubber)**: Edge case 3 successfully defines a defense against account number input. 
  - *Risk*: Relies on the LLM to catch PII. A pre-LLM regex filter for account numbers (e.g., `\d{3}-\d{4}-\d{4}`) is recommended to ensure zero data leakage to the model.
- **Compliance**: Disclaimer and "Capital Markets Act" (자본시장법) defense are correctly implemented.
- **Cost/UI Risk**: Synthetic data (Dummy_Peer_Data) usage keeps token costs predictable.

## 2. 무신사 (Musinsa) - one-pick-decision-agent
- **Data Privacy (Scrubber)**: Edge case 3 addresses PII (e.g., address) by ignoring it. 
  - *Risk*: Similar to KakaoPay, relying on LLM to ignore PII still sends PII to the model provider. Consider a local NER (Named Entity Recognition) scrubber before LLM invocation.
- **UI/Parser**: Hard block on ambiguous input prevents empty outputs and broken UI states.
- **Cost**: Token cost is minimal; single-item retrieval bounds output length.

## 3. 삼일PwC (SamilPwC) - ceo-issue-judge-agent
- **Data Privacy (Scrubber)**: Mentions a "비식별화 모듈" (De-identification module) in the architecture. This is a robust approach if implemented locally before LLM inference.
- **Compliance**: "review_required: true" fallback ensures human-in-the-loop when SOPs are missing, preventing hallucinated consulting advice.
- **Cost (Estimator)**: *High Risk*. RAG inputs (`sop_snippets`) can easily exceed token limits or bloat inference costs if not properly chunked and retrieved. Strict `max_tokens` limits and a semantic re-ranker are required to manage costs.

## Final Verdict
**Status**: APPROVED with minor mitigation required.
**Required Actions**:
1. (SamilPwC) Document the maximum token limit for `sop_snippets` to mitigate cost risk.
2. (KakaoPaySec/Musinsa) Clarify if PII scrubbing is pre-LLM or post-LLM.
