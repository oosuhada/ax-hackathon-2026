# Patch Log
- 초기 생성
- [QA Fix] `test_matrix.md`: Null 입력 처리 케이스 추가
- [QA Fix] `test_matrix.md`: 패닉/손실 시나리오에서 불완전판매 소지가 있는 "위로" 멘트 완전 제거
- [QA Fix] `test_matrix.md`: 정상 FOMO 시나리오에서 수익률 순 정렬 금지, 중립적 데이터 제공 명시
- [QA Fix] 면책조항 출력 시 LLM 의존을 벗어나 UI 단 하드코딩 적용 정책으로 변경
- [Cost-Estimator Fix] 면책조항 122자 -> 58자로 축소 (본 정보는 AI 시뮬레이션 결과로...)
- [QA Fix] `fomo-defense-agent` SKILL.md에 벤치마크 데이터 환각 방지 Fallback 조건 업데이트 필요(이후 빌드 단계에서 반영)
- [Deepening Pass] Merged Evaluator's Peer Benchmark mechanism into golden_demo_candidates.md while strictly maintaining QA-Tester's no-empathy and neutral sorting rules, alongside Cost-Estimator's concise disclaimer. Workspace conflict successfully resolved via cherry-pick.
