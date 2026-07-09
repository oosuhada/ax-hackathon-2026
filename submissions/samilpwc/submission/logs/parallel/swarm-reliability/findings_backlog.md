| Priority | Issue | File | Required Fix |
|---|---|---|---|
| P0 | 상충 데이터 및 SOP 근거 미비 시에도 AI가 결론을 도출함 | `src/validators/audit_evidence_validator.py` | 상충 데이터 검출 및 SOP 근거 검증 로직 추가 |
| P0 | 비식별화(NER) 실패 시 원문 그대로 출력됨 | `src/security/pii_scanner.py` | 잔여 민감정보(금액, 계약명) 존재 여부 이중 확인 추가 |
| P1 | 미래 성과 보장 및 무한 책임 인수 표현 필터링 부재 | `src/validators/compliance_validator.py` | 과장/단정 표현 Regex 추가 |
| P1 | 프롬프트 유출 및 지침 무시 공격 방어 미흡 | `src/security/prompt_guard.py` | 프롬프트 사전 필터링 패치 |
| P1 | Malformed JSON/Markdown 입력 시 파서 크래시 발생 가능 | `src/skills/ceo-issue-judge-agent/SKILL.md` 등 | LLM 전처리단에서 Token 길이, 제어문자 필터링 및 JSON 파싱 검증 추가 |
| P0 | 환각에 의해 가상의 SOP 식별자를 참조해도 승인됨 | `src/validators/audit_evidence_validator.py` | SOP 식별자 DB 크로스체크 및 매핑 실패 시 리뷰 이관 로직 |
| P1 | UI 렌더링 무한루프(닫히지 않은 태그, 과도한 Depth) 취약성 | `src/validators/payload_depth_checker.py` | JSON 깊이 제한 및 DOM 태그 페어 검증 추가 |
| P1 | 롤플레잉 우회(Developer Debug Mode) 시 시스템 지침 유출 위험 | `src/security/prompt_guard.py` | 페르소나 우회 공격 인텐트 분류기 추가 |
