# 무신사 — AX 해커톤 Codex 플러그인 로그용 프롬프트 시퀀스

> 사용법: 아래 `PROMPT 01`부터 실제 AI 세션에 하나씩 복사해 입력하세요.  
> AI의 실제 답변까지 포함된 전체 대화가 최종 `logs/musinsa-review-to-action_raw_log.md`가 됩니다.  
> 이 문서는 “프롬프트 대본”이지, 최종 제출용 원본 로그가 아닙니다.

## 프로젝트 요약

- 대상 기업: **무신사**
- 플러그인 이름: **`musinsa-review-to-action`**
- 핵심 문제: 소비자 리뷰와 Q&A가 많아도 입점 브랜드/MD가 이를 상품 개선, 상세페이지 개선, CS FAQ, 마케팅 액션으로 체계적으로 전환하기 어려운 문제
- 주 사용자: 무신사 입점 브랜드 운영자, MD, 상품기획자, 마케팅/CS 담당자
- 주요 산출물: review_insight_report.md, seller_action_plan.md, product_page_fix_list.md, cs_faq_draft.md, next_season_improvement_ideas.md, priority_matrix.md

---

## PROMPT 01 — 작업 선언 및 규칙 설정

```text
나는 AX 인재전쟁 해커톤 예선 과제로 무신사을 대상으로 한 Codex 플러그인을 만들고 있다.

중요한 규칙:
1. 제출물에는 AI와 주고받은 원본 로그 전체가 들어가야 하므로, 앞으로의 대화는 나중에 그대로 제출될 수 있다.
2. API 키, 비밀번호, 토큰, 실제 고객 데이터, 기업 내부자료 같은 비밀정보는 절대 요구하지 말고 사용하지 말아라.
3. 문제정의는 반드시 공개자료로 검증 가능한 내용만 사용해야 한다.
4. 출처 없는 숫자나 확인 불가능한 사적 경험은 근거로 쓰지 않는다.
5. 최종 목표는 보고서가 아니라 Codex에서 재사용 가능한 플러그인이다.

이번 플러그인 후보는 `musinsa-review-to-action`이고, 내가 풀고 싶은 문제는 다음과 같다:
"소비자 리뷰와 Q&A가 많아도 입점 브랜드/MD가 이를 상품 개선, 상세페이지 개선, CS FAQ, 마케팅 액션으로 체계적으로 전환하기 어려운 문제"

먼저 이 문제정의가 해커톤 과제 취지에 맞는지 검토하고, 더 날카로운 문제정의 3개를 제안해줘.
```

### 기대 결과

- 문제정의 후보 3개
- 공개자료로 입증 가능한지에 대한 판단
- 플러그인화 가능성 평가

---

## PROMPT 02 — 공개자료 조사 계획 수립

```text
좋아. 이제 이 문제를 공개자료로 입증하기 위한 evidence plan을 세워줘.

다음 조건을 지켜줘:
1. 기업 공식자료, 보도자료, 블로그, 공신력 있는 기사, 정부/기관 자료를 우선한다.
2. 검증 가능한 URL을 모아야 한다.
3. 출처별로 어떤 주장에 쓰면 좋은지 연결해줘.
4. 최종적으로 `src/skills/musinsa-review-to-action/references/evidence_sources.md`에 넣을 수 있는 구조로 정리해줘.

검색 키워드 후보는 다음과 같다:
무신사 AI 후기 요약 리뷰 데이터, 무신사 입점 브랜드 판매자 지원, 이커머스 리뷰 분석 상품 개선, 패션 커머스 반품 사이즈 리뷰 문제

표 형식으로 정리해줘:
- Source Type
- Search Query
- Expected Evidence
- Claim Supported
- Priority
```

### 기대 결과

- 출처 수집 계획
- 어떤 주장에 어떤 출처를 연결할지 정리

---

## PROMPT 03 — 최종 문제정의 확정

```text
위 evidence plan을 바탕으로, 해커톤 제출용 최종 문제정의를 작성해줘.

포맷:
1. Problem Statement: 한 문장
2. Who has this problem?
3. When does it happen?
4. Why is it important for 무신사?
5. Why is it suitable for a Codex plugin rather than a one-time report?
6. What should be explicitly excluded to avoid overclaiming?

톤은 과장하지 말고, 공개자료로 검증 가능한 주장만 사용하는 방식으로 작성해줘.
```

### 기대 결과

- README 5문항 중 “왜 이 문제를 선택했나요?”에 들어갈 핵심 문장
- 과장 방지 범위

---

## PROMPT 04 — 플러그인 사용자·입력·출력 정의

```text
이제 `musinsa-review-to-action`의 사용자 시나리오와 입출력을 구체화해줘.

다음 항목을 만들어줘:
1. Primary User
2. Secondary User
3. Job-to-be-Done
4. Input Files
5. Output Files
6. Step-by-step Workflow
7. Failure Cases
8. Success Criteria

Codex 플러그인이 실제 반복 업무에 쓰이는 느낌이 나도록 작성해줘. 단순 기획서가 아니라, 사용자가 입력 파일을 넣고 Codex가 산출물을 만드는 형태여야 해.
```

### 기대 결과

- `README.md`의 사용 시나리오
- `SKILL.md`의 workflow 초안

---

## PROMPT 05 — Codex Plugin 파일 구조 설계

```text
AX 해커톤 제출 조건은 다음과 같다.

submission.zip
├── src/
│   ├── .codex-plugin/plugin.json
│   ├── skills/<이름>/SKILL.md
│   ├── .mcp.json 선택
│   └── 실행 코드와 설정 파일
├── README.md
└── logs/

전체 플러그인 루트가 src 안에 있어야 하고, src/.codex-plugin/plugin.json은 필수다.

이 조건에 맞춰 `musinsa-review-to-action`의 파일 구조를 설계해줘.
각 파일의 역할도 설명해줘.
가능하면 너무 복잡하지 않고, 예선 제출에 맞게 실행 가능한 최소 구조로 제안해줘.
```

### 기대 결과

- 제출 zip 구조
- 각 파일의 역할

---

## PROMPT 06 — plugin.json 초안 작성

```text
`src/.codex-plugin/plugin.json` 초안을 작성해줘.

조건:
1. JSON만 출력하지 말고, 먼저 필드 설명을 간단히 해줘.
2. 그 다음 복사 가능한 JSON 코드블록을 제공해줘.
3. 플러그인 이름은 `musinsa-review-to-action`으로 해줘.
4. description은 무신사 대상 문제와 연결되게 작성해줘.
5. 실제 Codex 플러그인 구조에서 무리한 필드는 넣지 말고 최소한으로 작성해줘.
```

### 기대 결과

- plugin.json 초안

---

## PROMPT 07 — SKILL.md 본문 작성

```text
이제 `src/skills/musinsa-review-to-action/SKILL.md`에 들어갈 내용을 작성해줘.

조건:
1. Codex가 언제 이 skill을 사용해야 하는지 명확히 써줘.
2. 입력 파일을 확인하는 단계부터 시작해줘.
3. 공개자료 기반 주장과 사용자가 넣은 입력 데이터를 구분하게 해줘.
4. 출력 파일 형식을 명시해줘.
5. hallucination 방지 규칙을 넣어줘.
6. 마지막에 validation checklist를 넣어줘.

마크다운 파일로 바로 저장할 수 있게 작성해줘.
```

### 기대 결과

- 완성형 SKILL.md

---

## PROMPT 08 — 샘플 입력 데이터 설계

```text
`musinsa-review-to-action`을 검증하기 위한 샘플 입력 데이터를 만들어줘.

조건:
1. 실제 기업 내부자료나 실제 고객 데이터처럼 보이면 안 된다.
2. 합성 데이터임을 명시한다.
3. 그래도 플러그인 기능을 충분히 테스트할 수 있어야 한다.
4. 파일명과 컬럼 구조를 제안해줘.
5. CSV 또는 Markdown 형태로 바로 저장 가능한 샘플을 제공해줘.

출력은 다음 형태로 해줘:
- sample input file list
- 각 파일의 목적
- 각 파일의 내용 코드블록
```

### 기대 결과

- sample_inputs 파일 내용

---

## PROMPT 09 — 실행 스크립트/검증 스크립트 로직 설계

```text
이 플러그인에 넣을 간단한 Python 보조 스크립트를 설계해줘.

목표:
1. 입력 파일 존재 여부 확인
2. 샘플 데이터를 읽어 기본 통계 또는 체크리스트 생성
3. 출력 폴더에 Markdown 결과물 생성
4. 복잡한 AI 모델 호출 없이 로컬에서 동작 가능한 수준
5. 예선 제출용으로 "실행 가능한 구조"를 보여주는 데 집중

파일명은 `src/scripts/analyze.py`와 `src/scripts/validate_submission_structure.py`로 가정하고, 각 스크립트의 의사코드와 실제 코드 초안을 작성해줘.
```

### 기대 결과

- 간단한 Python 코드 초안

---

## PROMPT 10 — README 5문항 초안 작성

```text
AX 해커톤 질문 5문항에 답하는 README 초안을 작성해줘.

질문:
1. 무엇을, 누가, 어떤 상황에서 쓰나요?
2. 왜 이 문제를 선택했나요?
3. 플러그인은 어떻게 작동하나요?
4. AI를 어떻게 활용했나요?
5. 어떻게 검증했나요?

조건:
- 대상 기업은 무신사
- 플러그인 이름은 `musinsa-review-to-action`
- 공개자료 기반 문제정의라는 점을 강조
- AI 활용 내용은 지금까지 이 대화에서 실제로 수행한 일과 일치해야 함
- 과장된 성과, 실제로 검증하지 않은 성능 수치, 내부자료 접근 주장은 넣지 말 것
- 최종 제출 README에 바로 반영 가능한 톤으로 작성
```

### 기대 결과

- README 5문항 초안

---

## PROMPT 11 — 검증 시나리오와 예상 출력 만들기

```text
이제 `musinsa-review-to-action`의 검증 시나리오를 만들어줘.

포함할 것:
1. Test Case 1: 정상 입력
2. Test Case 2: 필수 입력 누락
3. Test Case 3: 과장되거나 근거 없는 주장 포함
4. Test Case 4: 공개자료와 사용자 입력을 혼동할 위험
5. 각 테스트의 expected behavior
6. 검증 결과를 `sample_outputs/validation_report.md`에 쓸 수 있는 형태

실제 성능을 과장하지 말고, 구조적 검증 중심으로 작성해줘.
```

### 기대 결과

- validation_report.md 초안

---

## PROMPT 12 — 최종 정합성 검사

```text
지금까지 설계한 `musinsa-review-to-action` 제출물이 해커톤 조건에 맞는지 최종 점검해줘.

체크할 것:
1. src/.codex-plugin/plugin.json 존재
2. skills/musinsa-review-to-action/SKILL.md 존재
3. 플러그인이 실제로 동작하도록 만드는 구성 요소가 하나 이상 존재
4. README 5문항 답변이 플러그인과 일치
5. 공개자료 기반 문제정의가 과장되지 않음
6. 로그와 README의 AI 활용 설명이 서로 모순되지 않음
7. logs 폴더에는 원본 로그를 넣어야 한다는 주의사항
8. 제출 전 남은 TODO 목록

마지막으로, 이 제출물의 가장 강한 점 3개와 가장 약한 점 3개를 평가해줘.
```

### 기대 결과

- 최종 제출 전 체크리스트
- 약점 보완 방향

---

# 실제 로그 저장 팁

세션이 끝나면 전체 대화를 아래 파일명으로 저장하세요.

```text
logs/musinsa-review-to-action_raw_log.md
```

이 프롬프트 시퀀스 파일은 최종 로그가 아닙니다. 실제 AI 응답을 포함한 원본 대화 전체가 로그입니다.
