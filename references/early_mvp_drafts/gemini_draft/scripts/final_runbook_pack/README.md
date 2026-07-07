# AX 해커톤 예선 작업용 프롬프트 런북 & 제출 정합성 팩

이 파일팩은 `무신사`, `카카오페이증권`, `삼일PwC` 3개 기업별 Codex 플러그인을 실제로 만들기 위한 **작업 런북**입니다.

중요:
- 이 팩은 **제출 로그가 아닙니다.**
- 해커톤 규정상 제출 로그는 실제로 AI와 주고받은 대화 원본이어야 합니다.
- 따라서 기업별 `01_copy_paste_prompt_sequence.md`를 새 AI 세션에 순서대로 붙여넣고, 그 실제 대화 전체를 `logs/` 폴더에 저장하세요.
- 이 팩에 들어 있는 `not_for_submission/SIMULATED_LOG_EXAMPLE.md`는 흐름 이해용 예시이며 제출하면 안 됩니다.

## 추천 운영 방식

시간이 부족하면 3개를 모두 완성하려고 하기보다 아래 우선순위로 진행하세요.

1. **카카오페이증권**: AI 투자정보의 설명가능성·리스크 고지·초보 투자자 보호 문제. 우수의 AI 신뢰성/MOT 서사와 가장 잘 맞음.
2. **삼일PwC**: 기업 AX use case 우선순위화. 기술전략·컨설팅·MOT 서사에 강함.
3. **무신사**: K-패션 오프라인 매장/관광객/리뷰 데이터를 활용한 쇼핑 경험 개선. 포트폴리오 시각화가 쉬움.

## 폴더 구성

```text
ax_hackathon_final_runbook_pack/
├── README.md
├── 00_log_policy_and_ethics.md
├── 00_one_day_execution_plan.md
├── 00_common_file_structure.md
├── combined_copy_paste_prompts.md
├── final_submission_checklist.md
├── company_musinsa/
├── company_kakaopaysec/
├── company_samilpwc/
└── not_for_submission/
```
