# Patch Log (Iteration 2)

## Chunk 1: Anti-Indirect Profiling
- Expanded "개인정보 취급 불가" to include "간접 프로파일링 차단" to prevent metadata combination tracking.

## Chunk 2: Bandwagon Backfire Fallback
- Added fallback instructions to ignore "Buy" sentiment in benchmarks and route to "market volatility" reassurance instead.

## Chunk 3: Safe Asset / Comparative Choice Trap
- explicitly prohibited labeling ETFs or leveraged products as "safe assets" and banned comparative risk assessment between two assets.

## Chunk 4 & 5: Strict Output Schema
- Refined JSON output format rules to strictly ban hallucinated extra fields.
- Added type constraints (String, Boolean) to each field.
- Removed `system_fallback_message` from the schema and YAML block as it represents an architectural contradiction for the LLM to output API timeout errors.
