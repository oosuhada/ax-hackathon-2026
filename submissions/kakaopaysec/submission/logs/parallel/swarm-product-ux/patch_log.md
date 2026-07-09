# Patch Log
- `[2026-07-09]` README.md: 피치 구조 변경(Pain->Moment->Relief) 및 우량 ETF/안전 자산 표현 전면 제거.
- `[2026-07-09]` README.md: Pre-LLM Data Scrubber 도입 로드맵 추가.
- `[2026-07-09]` src/skills/fomo-defense-agent/SKILL.md: 면책 조항 축소(약 50자)하여 UX 및 토큰 소모 최적화.
- `[2026-07-09]` src/skills/fomo-defense-agent/SKILL.md: `next_safe_action`을 투자성향 진단 및 전문 상담 연결 검토로 수정.
- `[2026-07-09]` src/skills/fomo-defense-agent/SKILL.md: 사전 마스킹된 `[ACCOUNT_MASKED]` 처리 방식 적용하여 개인정보 보호 강화.
- `[2026-07-09]` README.md (Iteration 2): Fail-Fast 아키텍처 및 Zero-Token Payload Blocking (BL-03) 추가하여 비용 최적화.
- `[2026-07-09]` README.md (Iteration 2): Data Privacy Scrubber를 원본 로그 기록 전 의무적으로 통과시킴을 명시하여 심사위원 프라이버시 의구심(UX-06) 해소.
- `[2026-07-09]` src/skills/fomo-defense-agent/SKILL.md (Iteration 2): 로깅 계층(BL-01)의 평문 저장 금지를 위해 Data Privacy Scrubber 역할을 지시어에 신설.
- `[2026-07-09]` src/skills/fomo-defense-agent/SKILL.md (Iteration 2): "안전 자산" 관련 간접 권유 요소를 완전히 제거하고 `show_suitability_routing_button`으로 파라미터명 교체.
