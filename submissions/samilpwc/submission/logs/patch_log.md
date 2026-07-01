# Patch Log
| Round | File | Summary |
|---|---|---|
| 1 | SKILL.md | PII 출력 마스킹 규칙 추가, 블랙리스트 대신 컨텍스트 격리 원칙 추가, 정상 재무 데이터 예외 처리 |
| 1 | README.md | ROI 5축 확장 (운영 통합 비용 포함) 및 MM 단가 수식 오류 정정 |
| 1 | logs/roi_audit.md | ROI 5축 확장 내역 반영 |
| 2 | SKILL.md | 음수 예외 조건 추가, 인코딩 문자열(Base64) 감지/차단 명시, Fallback JSON 스키마 유지 강제 |
| 2 | README.md | Justification 축에 정성적 ROI 효과(회의 시간 단축) 추가 반영 |
| 3 | SKILL.md | Division by Zero 검토 로직 추가, URL/Markdown 금지 조항, Dry Tone 제약 추가 |
| 3 | README.md | Follow-on Project 항목에 시스템 자원 오배분 식별 효과 명시 |
| 4 | SKILL.md | Cross-lingual 인젝션 차단 조항, JSON Schema 내 mapping_rationale 필드 추가 |
| 4 | README.md | 6축 ROI 확립 (Time-to-Audit 추가) |
| 5 | SKILL.md | K-익명성 10인 룰(사용자 반영), 동형문자 차단, 청킹 리스크 추가 |
| 6 | SKILL.md | Rule Leakage 방어 조항(사용자 반영), Token Exhaustion 엣지 케이스 추가 |
| 6 | README.md | 8축 ROI 확립 (Client Onboarding Time 단축 추가) |
| 7 | SKILL.md | 부동소수점 아노말리 차단 추가, JSON Key Injection 방어 추가 |
| 7 | README.md | 9축 ROI 반영(사용자 수동), PoC 검증 로드맵 추가 |
| 8 | SKILL.md | 빈 입력(Empty/Null) 무한루프 방어, 가짜 SOP 포이즈닝 방어 |
| 8 | README.md | CRI(SOP 교착해결률) 지표, FP Escalation Rate(정상 재승인비율) KPI |
| 9 | SKILL.md | Deep Nesting(Stack Overflow) 차단, Nested Role 탈취 차단, Session State 로드맵 |
| 9 | README.md | 10축 ROI 반영(평판 리스크 회피) |
| 11 | SKILL.md | 인코딩 우회(Encoding Confusion), 롤 사칭(Role Spoofing) 공격 원천 방어 |
| 11 | README.md | 12축 ROI(임원 커뮤니케이션 속도), FP 대시보드 트래커 UI 기획안 |
| 12 | SKILL.md | Array Expansion(DoW) 및 Indirect Injection 원천 차단 |
| 12 | README.md | 13축 ROI(API Cost Spike 보호), Guardrail Latency 모니터링 |
| 14 | SKILL.md | Prompt Extraction(Model Stealing) 방어, Logical Contradiction 이관 |
| 14 | README.md | 15축 ROI(IP 보호), Progressive UI 및 Ensemble Architecture 추가 |
| 15-20 | SKILL.md | Token Smuggling, Logic Bomb, Data Exfiltration, Probing 방어 |
| 15-20 | README.md | 16~20번째 방위산업급 보안 ROI 및 Threat Intel 지표 완성 |
| 15 | SKILL.md | Phonetic/Homophone Prompt Injection (음성 인식 우회) 방어 추가 |
| 15 | README.md | ROI 19축 (음성 위조 방어 / Insurance Cost 절감) 반영 |
| 16 | SKILL.md | Zero-Width 문자 및 가짜 외부지식 주입 차단 |
| 16 | README.md | ROI 21축(Fake News 방어), Anomaly Score 모니터링 추가 |
| 18 | SKILL.md | Token Smuggling(Base64/Hex) 방어 |
| 19 | SKILL.md | Data Exfiltration(Markdown) 아웃바운드 링크 차단 |
| 20 | SKILL.md | Automated Scanner Probing 방어 |
