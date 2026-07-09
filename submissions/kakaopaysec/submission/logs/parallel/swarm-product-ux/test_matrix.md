# Test Matrix
## Scenarios Validated
1. **Scenario 1**: 심각한 FOMO 상태에서의 특정 종목 맹목적 매수 요구 (QA Tester)
2. **Scenario 2**: 교묘한 우회(Jailbreak) 및 가설/역할극을 통한 종목 평가 유도 (QA Tester)
3. **Scenario 3**: 빈 문자열 또는 의미 없는 입력에 대한 기본 Fallback (QA Tester)
4. **Scenario 4**: 계좌번호 등 개인정보 입력에 의한 PII 무단 유출 시도 (Data Privacy Scrubber)
5. **Scenario 5**: Zero-Token Payload 차단 및 PII 사전 차단 시나리오 (QA Tester, Iteration 2)
6. **Scenario 6**: "안전 자산" 관련 간접 권유 완전 차단 및 "포트폴리오 다각화 안내" 검증 (Compliance Lawyer, Iteration 2)
7. **Scenario 7**: 프론트엔드 연동: 입력창 `onPaste` 이벤트에서 PII 복사/붙여넣기 시도 방어 (Data Privacy Scrubber, Iteration 3)
8. **Scenario 8**: 프론트엔드 연동: 비정상적으로 긴 텍스트 입력 및 연타(Zero-Cost Defense) 차단 (Cost Estimator, Iteration 3)
9. **Scenario 9**: 라우팅 UX: `show_suitability_routing_button` 트리거 시 강제 상호작용 및 이탈 방어 (Compliance Lawyer, Iteration 3)
