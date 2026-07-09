# Test Matrix

## Document & Compliance Checks

| Check | Command / Evidence | Expected Result | Status |
|---|---|---|---|
| Plugin manifest JSON syntax | `python3 -m json.tool submissions/kakaopaysec/submission/src/.codex-plugin/plugin.json >/dev/null` | Valid JSON | PASS |
| Synthetic peer data JSON syntax | `python3 -m json.tool submissions/kakaopaysec/submission/src/data/Dummy_Peer_Data.json >/dev/null` | Valid JSON | PASS |
| JSONL parse check | Parse every non-empty line under `submissions/kakaopaysec/submission/logs/**/*.jsonl` with `json.loads` | No JSON decode errors (`transcript.jsonl`, `attack_corpus.jsonl`) | PASS |
| README / QA case count consistency | README validation section and `logs/qa_report.md` | Both state 11 scenarios/cases | PASS |
| Privacy wording review | README AI usage section | No unsupported "Zero Data Retention" absolute guarantee | PASS |
| Investment-advice wording review | README, QA report, demo transcript | Specific buy/sell advice and guaranteed-return language are rejected or framed as non-advice | PASS |
| Source grounding | README, `research/카카오페이증권_company_research.md`, `interviews/카카오페이증권_interview_summary.md` | README cites local research/interview rationale briefly | PASS |

## Red-Team Coverage from `qa_report.md`

| Area | Cases Covered | Status |
|---|---:|---|
| Normal FOMO reassurance | 1 | PASS |
| Specific buy instruction / guaranteed return refusal | 2 | PASS |
| Disclaimer bypass / prompt extraction | 2 | PASS |
| Privacy and account data handling | 1 | PASS |
| Minor, panic, leverage, debt/FOMO, reverse-psychology edge cases | 5 | PASS |

Final validation commands passed on 2026-07-10 in `final/kakaopaysec`.
