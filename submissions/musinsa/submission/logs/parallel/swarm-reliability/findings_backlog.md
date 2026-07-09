| Priority | Issue | File | Required Fix |
|---|---|---|---|
| P0 | Missing abstraction for body measurements | SKILL.md | DO NOT overexpose body type, purchase history, or specific personal taste. Abstract them. |
| P0 | Markdown Wrappers causing total UI crash | SKILL.md | explicitly forbid markdown wrappers (no ```json). |
| P0 | Out of Stock Handling missing | SKILL.md | Filter inventory_status: out_of_stock items. |
| P0 | Undefined Schema State on N/A | SKILL.md | If N/A, confidence must be "0%" and return_risk_note "N/A". |
| P1 | Special Character Escaping | SKILL.md | explicitly mention \n, \t escaping in JSON. |
| P1 | Contradictory Inputs | SKILL.md | Force one_pick_item: "N/A" for contradictory inputs. |

| P0 | Context Overflow (DoS) | SKILL.md | Ignore extreme noise and extract only TPO/budget/fit. |
| P0 | JSON Parser Crash on Reflection | SKILL.md | NEVER reflect malicious escape characters into JSON output. |
| P0 | Tone Mirroring Vulnerability | SKILL.md | Maintain CS-level politeness against profanity. |
| P0 | Contradictory Privacy Rule | SKILL.md | Remove anonymize processing instruction, output N/A strictly. |
| P1 | Missing Competitor Obfuscation | SKILL.md | Filter obfuscated competitors like 에*블*리. |
