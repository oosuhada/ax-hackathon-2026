# Findings Backlog

본 파일은 최종 제출 전 evidence gap 점검 결과를 기록합니다. 2026-07-10 기준 빈 로그 파일 상태를 확인했고, 제출물 검증 명령 및 기존 QA 산출물을 근거로 남은 이슈를 정리했습니다.

| ID | Finding | Severity | Status | Evidence / Rationale |
|---|---|---:|---|---|
| KPS-FIN-001 | README에는 "10가지 시나리오"라고 되어 있으나 `qa_report.md`에는 11개 테스트 케이스가 기재되어 있었습니다. | Medium | Fixed | README와 QA report 제목을 11 cases로 일치시켰습니다. |
| KPS-FIN-002 | README의 "Zero Data Retention" 및 "원천 보장" 표현은 실제 운영 계약/정책 근거 없이는 절대 보장처럼 읽힐 수 있었습니다. | High | Fixed | 상용화 시 데이터 최소화 정책 및 PII 차단 설계로 완화했고, 본 제출물에는 합성 데이터만 포함된다고 명시했습니다. |
| KPS-FIN-003 | README의 문제 선택 근거가 제출물 내부 리서치/인터뷰 문서와 충분히 연결되지 않았습니다. | Low | Fixed | 기업 연구와 인터뷰 요약 기반 근거 문장을 README에 짧게 추가했습니다. |
| KPS-FIN-004 | `findings_backlog.md`, `patch_log.md`, `test_matrix.md`가 0바이트라 최종 제출 증거로 기능하지 못했습니다. | Medium | Fixed | 본 backlog, patch log, test matrix에 실제 점검/검증 요약을 기록했습니다. |

## Open Risks

- 실제 고객 데이터, 상담량, 투자 실행 전 이탈률은 내부 데이터가 없어 `[UNKNOWN]` 또는 `[ASSUMPTION]`으로 유지해야 합니다.
- 본 제출물은 해커톤 데모 산출물이며, 실제 금융 서비스 적용 전 법무/준법감시/개인정보 영향평가가 필요합니다.
