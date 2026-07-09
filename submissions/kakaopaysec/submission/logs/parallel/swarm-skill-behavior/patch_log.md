# Patch Log

## Chunk 1: Disclaimer Quotes
- Removed outer quotes around the required disclaimer text in rule 2 to prevent JSON parser breaking.

## Chunk 2: 동조 효과 (Bandwagon) Wording
- Replaced "신규 진입을 보류(HOLD) 중입니다. 뒤처지는 것이 아니니 안심하십시오." with "신규 매수를 진행하지 않은 상태입니다." to remove any implicit hold recommendation.

## Chunk 3: Alternative Asset Wording
- Explicitly declared all assets (including stocks) out of domain for investment recommendations, fixing the loophole that implied stock consultation was allowed.

## Chunk 4: Output Format
- Replaced the vague "JSON schema or Markdown" instruction with a strict JSON object instruction.
- Added a concrete JSON code block example specifying boolean `false` and `null` fallbacks for optional fields.
