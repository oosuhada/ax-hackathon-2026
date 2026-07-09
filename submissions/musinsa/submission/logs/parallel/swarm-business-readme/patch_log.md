## Iteration 1 & 2 Patch Log

- File: `README.md`
  - Change: Simplified ROI section, fixed math units, added Inference Cost section, updated 60s pitch. Added `[ASSUMPTION]` label, improved "원천 차단하는" to "최소화하는".
  - Reason: To improve readability, mathematical accuracy, credibility, and proactively answer judge objections.
- File: `src/skills/one-pick-decision-agent/SKILL.md`
  - Change: Updated Rule 1 (tie-breaker logic for overstocked items and multi-item concealment bypass block) and Rule 4 (prompt injection error schema `why_this: "Security/Bias Policy Violation"`).
  - Reason: To align SKILL.md implementation with README.md claims and defend against bundling bypasses.
- File: `src/skills/one-pick-decision-agent/SKILL.md`
  - Change: Updated Rule 3 (Data Privacy) to explicitly reject input containing exact body measurements or purchase IDs.
  - Reason: To prevent the LLM from processing highly sensitive PII.
- File: `src/skills/one-pick-decision-agent/SKILL.md`
  - Change: Updated Rule 5 to block obfuscated competitor names (e.g. Z-i-g-z-a-g).
  - Reason: To prevent competitor injection bypass.
