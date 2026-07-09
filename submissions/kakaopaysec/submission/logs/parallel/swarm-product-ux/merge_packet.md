## Merge Packet - Iteration 1

### Branch
`parallel/product-ux/kakaopaysec`

### Target Directory
`submissions/kakaopaysec/submission/`

### Change Summary
- **Category**: UX Improvement & Compliance Update
- **Status**: Ready to Merge
- **Key Changes**:
  1. `README.md`: 투자 권유/안전 자산 배분 관련 워딩을 '투자성향 진단 및 리스크 체크리스트 전환'으로 교체.
  2. `src/skills/fomo-defense-agent/SKILL.md`: `show_safe_routing_button`을 `show_suitability_routing_button`으로 변경 및 로직 내 '안전 자산 추천' 제거.
  3. `src/.codex-plugin/plugin.json`: description 내 '안심 투자' 워딩 제거.

### Verification (Subagents)
- `evaluator-pitch-judge`: Approved
- `compliance-lawyer`: Approved
- `qa-tester`: Approved
- `data-privacy-scrubber`: Approved
- `cost-estimator`: Approved

### Next Steps
- 1분 후 2차 라운드(Iteration 2) 시작 예정.
- 모의 시나리오 JSON 통계 텍스트가 UX 원칙에 맞는지 추가 검증.
