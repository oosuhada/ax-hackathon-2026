# Test Matrix: samilpwc
| Test Case | Schema Match | PII Masking | SOP Strictness | Result |
|-----------|--------------|-------------|----------------|--------|
| Case 1-4 | OK | N/A | OK | PASSED |
| Case 5-7 | OK | OK | OK | PASSED (Fixed) |
| Case 8-10| OK | N/A | OK | PASSED (Fixed) |
| Case 5-8 (Iter 2)| OK | OK (Standardized) | OK (Compliance/Security Risk Explicit) | PASSED |

| Case 16-20 | OK (Type Strict) | OK (Bucketized) | OK (No Ontology Hack) | PASSED (Deepening Pass Complete) |

