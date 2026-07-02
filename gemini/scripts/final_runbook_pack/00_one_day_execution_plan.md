# 00. 마감 전 1일 실행 계획

## 전체 전략

3개 기업을 모두 선택했다면 기업별로 제출물이 따로 필요합니다. 각 기업에 대해 최소 제출 가능 형태는 다음입니다.

```text
submission_<company>.zip
├── src/
│   ├── .codex-plugin/plugin.json
│   ├── skills/<skill-name>/SKILL.md
│   ├── sample_inputs/
│   ├── sample_outputs/
│   └── scripts/validate_submission_structure.py
├── README.md
└── logs/
    └── <company>_raw_log.md
```

## 시간 배분

### 기업 1개당 최소 2.5~3.5시간

1. 새 AI 세션 시작 및 로그 수집 시작: 10분
2. 문제정의/근거 수집: 30~40분
3. plugin 구조 및 `plugin.json`: 20분
4. `SKILL.md` 작성: 40분
5. 샘플 입력/출력 작성: 30분
6. README 5문항 답변: 30분
7. 구조 검증 및 압축: 20분
8. 로그 저장: 10분

## 우선순위

1. 카카오페이증권 먼저 완성
2. 삼일PwC 완성
3. 무신사 완성

## 제출 전 반드시 확인

- 각 기업별 zip은 하나의 기업만 다루는가?
- zip 루트에 `src`, `README.md`, `logs`가 바로 있는가?
- `src/.codex-plugin/plugin.json`이 존재하는가?
- `src/skills/<name>/SKILL.md`가 존재하는가?
- README 5문항이 실제 플러그인 기능과 일치하는가?
- 로그가 실제 작업 대화 원본인가?
- 공개자료 URL이 README 또는 `evidence_sources.md`에 들어갔는가?
