| File | Change | Reason |
|---|---|---|
| `src/validators/audit_evidence_validator.py` | `detect_evidence_conflict` 및 `validate_sop_basis` 함수 추가 | 증거 상충 및 SOP 근거 누락 시 `proposed_status` 채택 차단 |
| `src/security/pii_scanner.py` | `has_unmasked_money` 및 `has_unmasked_contract` 검증 로직 추가 | 마스킹 누락 방지 및 2차 필터링 |
| `src/validators/compliance_validator.py` | `LIABILITY_KEYWORDS` 정규식 추가 | 책임 한계 초과 표현 검출 시 차단 |
| `src/skills/ceo-issue-judge-agent/SKILL.md` | Malformed Formatting 방어 지시어 추가 | 포맷 파괴 목적의 입력 방어 가이드 |
| `src/validators/audit_evidence_validator.py` | `verify_sop_existence` 함수 추가 | 가상의 SOP(환각) 참조 방지 |
| `src/validators/payload_depth_checker.py` | `check_json_depth_and_tags` 모듈 추가 | UI 렌더링 크래시/무한루프 방어 |
| `src/security/prompt_guard.py` | 롤플레잉 우회 탐지 정규식/분류기 추가 | 시스템 프롬프트 유출 원천 차단 |
