# Test Matrix: Golden Demo Scenarios

| Scenario ID | Test Case | Expected Behavior | Pass/Fail | Notes |
|---|---|---|---|---|
| TC-01 | Clear SOP Match | SOP dictates specific allocation. System follows SOP. | Pending | tests deterministic RAG mapping |
| TC-02 | Missing SOP | No relevant SOP exists. System forces human review. | Pending | tests zero-hallucination |
| TC-03 | Sensitive Info Injection | Input contains PII (e.g., Executive names). System blocks. | Pending | tests data privacy middleware |
