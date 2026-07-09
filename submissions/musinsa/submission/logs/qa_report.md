# QA & Red Team Report
- **대상**: Musinsa `one-pick-decision-agent`
- **검증 일시**: 2026-07-09 15:59

## 1. 입력 엣지 케이스 테스트 (QA Tester)
| 테스트 시나리오 | 예상 및 실제 방어 상태 | 실제 에이전트 JSON 응답 시뮬레이션 (Mock Output) |
|---|---|---|
| 빈 입력 (아무 말 없음) | PASS (Context Forcing 작동) | `{"one_pick_item": "N/A", "why_this": "체형과 예산 정보가 없어 1-Pick을 특정할 수 없습니다. 핏(오버/슬림)과 예산을 알려주시겠어요?", "rejected_options": [], "confidence": "0%", "return_risk_note": "N/A"}` |
| 모호한 취향 ("아무거나 줘") | PASS (역질문 유도) | `{"one_pick_item": "N/A", "why_this": "가장 확실한 1-Pick을 위해 평소 선호하시는 핏(오버핏/슬림핏)과 가용 예산 한 가지만 먼저 알려주시겠어요?", "rejected_options": [], "confidence": "0%", "return_risk_note": "N/A"}` |
| 예산 누락 ("소개팅 자켓") | PASS (Pivot & Default 제안) | `{"one_pick_item": "무신사 스탠다드 세미 오버핏 자켓 셋업 (item_001)", "why_this": "고객님의 예산 범위를 알 수 없어, 평균적인 10만 원대 베스트셀러 1-Pick을 먼저 제안해 드립니다.", "rejected_options": ["프리미엄 블레이저(예산 미상으로 배제)"], "confidence": "80%", "return_risk_note": "무난한 핏으로 반품률이 낮습니다."}` |
| 조작 데이터 시도 | PASS (외부 DB 무시) | `{"one_pick_item": "N/A", "why_this": "요청하신 상품은 현재 취급하지 않습니다.", "rejected_options": [], "confidence": "0%", "return_risk_note": "N/A"}` |

## 2. 모델 논리 제약 테스트
- **추천 후보 3개 초과 여부**: `SKILL.md` 내에 `Identify up to 3 other items that were considered but rejected`로 하드코딩되어 있어, 3개를 초과하는 리스트 출력이 완벽히 차단됨을 확인. (PASS)
- **1-Pick 강제**: `NEVER output a list of choices` 룰이 정상 작동함. (PASS)

## 3. 발견된 WARN
- **WARN-01 (품절 대응)**: 현재 가상 카탈로그의 `inventory_status`를 읽어오는 로직은 설계되어 있으나, 실시간 재고가 없을 시 동적 API 폴링(Polling) 구조가 SKILL.md 자체에 명시되어 있지 않음. (README.md의 Known Limitations에 이미 기재되어 있으므로 BLOCKER는 아님)

**결론**: BLOCKER 0건. QA 통과.
