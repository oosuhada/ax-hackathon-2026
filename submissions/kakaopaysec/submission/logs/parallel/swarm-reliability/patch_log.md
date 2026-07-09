# Patch Log

## Iteration 1
- **File**: `submissions/kakaopaysec/submission/src/skills/fomo-defense-agent/SKILL.md`
- **Changes**:
  1. Removed `123-4567` and `000-11-2222` dummy strings. Replaced with `<ACCOUNT_NUM>` and `<RESIDENT_ID>`.
  2. Updated JSON schema constraint (Line 54) to enforce strict JSON without markdown blocks, removing ambiguity.
  3. Added `is_rejected` and `reject_reason` fail-fast outputs for edge case handling.
  4. Updated compliance disclaimer to strictly adhere to Article 57 of the Capital Markets Act.

## Iteration 2
- **File**: `submissions/kakaopaysec/submission/src/skills/fomo-defense-agent/SKILL.md`
- **Changes**:
  1. Removed explicit asset recommendations ("ETF", "로보어드바이저") from step 5 to maintain zero investment advice.
  2. Modified peer benchmark logic from precise ratios ("88%") to generalized psychological reassurance to prevent reverse-FOMO.
  3. Enforced masking rules for `asset_band` and `risk_tolerance` to prevent secondary PII exposure in system logs.
  4. Restored Iteration 1 fixes that were overwritten by rogue commits.
