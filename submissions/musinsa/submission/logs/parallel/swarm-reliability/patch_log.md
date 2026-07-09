| File | Change | Reason |
|---|---|---|
| SKILL.md | Data Privacy Rule updated | PII block to include phone numbers, mandate abstraction of body/history in why_this |
| SKILL.md | UI Parser protection added | Added strict rule against markdown wrappers and enforced \n \t escaping |
| SKILL.md | Red team logic added | Forced N/A for out_of_stock and contradictory inputs |
| SKILL.md | Schema output fixed | Added explicit 0% confidence and N/A risk note for N/A cases |
| Dummy_Product_Data.json | Added out_of_stock dummy item | To verify Red Teaming rules for stock handling |

| SKILL.md | Context Length Guardrail | Added explicit instruction to discard extreme noise |
| SKILL.md | Tone & Manners | Enforced CS-level politeness against abuse |
| SKILL.md | JSON Injection Defense | Banned reflection of raw inputs into why_this |
| SKILL.md | Competitor Defense | Added obfuscated names (에*블*리) to blocklist |
| SKILL.md | Data Privacy Rule | Removed contradictory anonymize rule, forced N/A for PII |
