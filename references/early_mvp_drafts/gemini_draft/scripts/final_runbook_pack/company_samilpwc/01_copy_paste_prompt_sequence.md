# 삼일PwC — 붙여넣기용 AI 작업 프롬프트 시퀀스

아래 프롬프트를 새 AI 세션에 순서대로 붙여넣으세요.  
이 문서 자체는 제출 로그가 아니며, 실제 AI와 주고받은 대화 전체를 제출 로그로 저장해야 합니다.

---

## 프로젝트 콘셉트

- 기업: 삼일PwC
- 플러그인 이름: `samil-ax-usecase-prioritizer`
- 스킬 이름: `samil-ax-usecase-prioritizer`
- 문제정의: 기업은 생성형 AI 도입 필요성은 인식하지만 어떤 업무부터 AX를 적용해야 하는지, ROI·데이터 준비도·리스크·조직 수용성을 어떻게 비교해야 하는지 판단하기 어렵다.
- 가치제안: 업무 목록과 pain point를 입력하면 Codex가 AX use case 후보를 도출하고 우선순위 매트릭스, Quick Win, PoC 계획, 리스크/거버넌스 체크리스트를 생성하는 컨설팅 보조 플러그인.

---

## PROMPT 01 — 역할 부여 및 과제 제약 확인

```text
나는 AX 해커톤 예선 과제로 삼일PwC 대상 Codex 플러그인을 만들고 있다.

과제 제약은 다음과 같다.
1. 선택 기업, 기업의 산업, 또는 기업의 고객이 겪는 실제 문제를 공개 자료로 입증해야 한다.
2. 그 문제를 해결하는 Codex 플러그인을 제출해야 한다.
3. 제출 구조는 submission.zip 안에 src/.codex-plugin/plugin.json, src/skills/<이름>/SKILL.md, README.md, logs/가 있어야 한다.
4. AI와 주고받은 로그 전체를 편집 없이 제출해야 한다.
5. 출처 없는 숫자, 비공개 정보, 사적인 경험은 근거로 인정되지 않는다.

이번 기업은 삼일PwC이고, 내가 만들고 싶은 플러그인은 `samil-ax-usecase-prioritizer`이다.
핵심 문제정의는 다음과 같다.

기업은 생성형 AI 도입 필요성은 인식하지만 어떤 업무부터 AX를 적용해야 하는지, ROI·데이터 준비도·리스크·조직 수용성을 어떻게 비교해야 하는지 판단하기 어렵다.

너는 지금부터 내 AX 해커톤 작업 파트너다.
먼저 이 문제정의가 과제 요구사항에 맞는지 비판적으로 검토하고, 더 강한 문제정의 문장 3개를 제안해줘.
```

---

## PROMPT 02 — 공개자료 근거 수집 계획

```text
좋아. 이제 이 문제를 공개 자료로 입증하기 위한 evidence plan을 만들어줘.

다음 조건을 지켜줘.
- 실제로 확인 가능한 공개자료 유형만 제안해줘.
- 출처를 조작하지 말고, 내가 직접 확인해야 하는 URL은 TODO로 표시해줘.
- 공식 보도자료, 공식 블로그, 공식 서비스 페이지, 금융/산업 기사, 규제기관 또는 공공자료를 우선해줘.
- 근거는 '문제 존재', '기업/산업 적합성', '플러그인 필요성'으로 나눠줘.

현재 내가 확보하거나 확인할 공개자료 후보는 다음과 같다.


- 삼일PwC AX Node 공식 페이지
  - https://www.pwc.com/kr/ko/services/ax-node.html
- 삼일PwC Digital & AI Transformation 공식 페이지
  - https://www.pwc.com/kr/ko/services/ax-node/digital-ai.html
- 삼일PwC Expertise Meets AI PDF
  - https://www.pwc.com/kr/ko/insights/service/samilpwc_expertise-meets-ai.pdf
- 삼일PwC Physical AI / AX Node 자료
  - https://www.pwc.com/kr/ko/insights/service/samilpwc_physical-ai.pdf


출력 형식:
1. 근거 테이블
2. README에 들어갈 evidence paragraph 초안
3. 확인해야 할 URL 체크리스트
```

---

## PROMPT 03 — 최종 문제정의 확정

```text
이제 문제정의를 최종 확정하자.

다음 형식으로 작성해줘.
1. 한 문장 문제정의
2. 누가 겪는 문제인가
3. 언제/어떤 상황에서 발생하는가
4. 기존 방식의 한계
5. Codex 플러그인이 해결하는 방식
6. 이 문제가 삼일PwC와 직접 연결되는 이유

조건:
- 너무 거창한 플랫폼 개발처럼 쓰지 말고, Codex 플러그인으로 반복 수행 가능한 업무 단위로 좁혀줘.
- 해커톤 심사자가 30초 안에 이해할 수 있게 작성해줘.
```

---

## PROMPT 04 — 입력/출력/워크플로우 설계

```text
`samil-ax-usecase-prioritizer`의 입력, 처리 단계, 출력물을 설계해줘.

플러그인은 Codex skill 중심으로 구현할 것이다.
복잡한 서버나 DB 없이도 작동해야 한다.

구체적으로 아래를 작성해줘.
1. 사용자가 제공하는 입력 파일 또는 텍스트
2. Codex가 수행하는 단계별 workflow
3. 각 단계에서 확인해야 할 기준
4. 최종 출력물 목록
5. 실패/예외 상황 처리 방식
6. 검증 가능한 sample input과 sample output 구성

추가 요구:
삼일PwC의 AX Node가 강조하는 진단→과제 식별→우선순위화→PoC 실행 흐름과 맞춰줘. 단, 삼일PwC 내부 방법론을 아는 척하지 말고 공개자료에 기반한 일반화된 프레임워크로 표현해줘.
```

---

## PROMPT 05 — `plugin.json` 작성

```text
이제 Codex 플러그인용 `src/.codex-plugin/plugin.json` 초안을 작성해줘.

조건:
- JSON만 출력해줘.
- name은 `samil-ax-usecase-prioritizer`로 해줘.
- version은 `1.0.0`.
- description은 120자 이내 한국어로 작성.
- skill entry에는 `samil-ax-usecase-prioritizer`을 포함.
```

---

## PROMPT 06 — `SKILL.md` 작성

```text
이제 `src/skills/samil-ax-usecase-prioritizer/SKILL.md` 파일 내용을 작성해줘.

조건:
- 한국어로 작성.
- Codex가 언제 이 스킬을 사용해야 하는지 명확히 설명.
- 반드시 다음 섹션 포함:
  1. Purpose
  2. When to use this skill
  3. Required inputs
  4. Workflow
  5. Output format
  6. Validation checklist
  7. Guardrails
  8. Example
- 과장된 성능 약속 금지.
- 공개자료로 확인되지 않은 사실을 단정하지 말라고 지시.
- 투자/금융/법률/회계 등 고위험 도메인일 경우 의사결정 대체가 아니라 보조 도구라고 명시.
```

---

## PROMPT 07 — 샘플 입력/출력 작성

```text
이 플러그인을 검증할 수 있는 샘플 입력과 샘플 출력을 만들어줘.

샘플 입력 상황:
중견 제조/유통 기업이 12개 업무 프로세스와 pain point 목록을 제공했고, AX 적용 우선순위와 4주 PoC 계획이 필요한 상황.

출력물은 아래를 포함해야 한다.
- AX use case 후보 목록
- 우선순위 매트릭스
- Quick Win / Strategic Bet / Risky Bet 분류
- 4주 PoC 계획
- 리스크/거버넌스 체크리스트
- 임원 보고용 1페이지 요약

주의:
- 샘플은 제출자가 만든 테스트 데이터임을 명시.
- 실제 기업 내부데이터처럼 꾸미지 말 것.
- 공개자료가 필요한 부분은 TODO_SOURCE로 표시.
```

---

## PROMPT 08 — README 5문항 작성

```text
해커톤 제출 페이지의 5문항에 맞춰 README 초안을 작성해줘.

질문:
1. 무엇을, 누가, 어떤 상황에서 쓰나요?
2. 왜 이 문제를 선택했나요?
3. 플러그인은 어떻게 작동하나요?
4. AI를 어떻게 활용했나요?
5. 어떻게 검증했나요?

조건:
- 답변은 과제 제출용 문체로 작성.
- 너무 길지 않게 각 문항 300~600자 정도.
- 공개자료 근거가 필요한 문장에는 [근거: evidence_sources.md] 식으로 표시.
- 실제 로그와 어긋나지 않도록 AI 활용 방식은 우리가 실제로 한 작업만 언급.
```

---

## PROMPT 09 — 정합성 검사

```text
지금까지 만든 문제정의, plugin.json, SKILL.md, sample input/output, README 5문항이 서로 모순되는지 검사해줘.

검사 항목:
1. 기업이 하나만 다뤄지는가?
2. 문제정의와 플러그인 기능이 일치하는가?
3. README의 AI 활용 설명이 실제 대화 흐름과 일치하는가?
4. 공개자료로 입증 가능한 주장만 남아 있는가?
5. 과제 요구 구조를 만족하는가?
6. 심사자가 볼 때 '실제로 동작하는 Codex 플러그인'처럼 보이는가?
7. 너무 가벼운 프롬프트 모음처럼 보이지 않는가?

출력:
- 통과 항목
- 수정 필요 항목
- 최종 수정안
```

---

## PROMPT 10 — 최종 압축 전 체크리스트

```text
최종 제출 전 체크리스트를 만들어줘.

내 폴더 구조는 다음과 같아.

submission.zip
├── src/
│   ├── .codex-plugin/plugin.json
│   ├── skills/samil-ax-usecase-prioritizer/SKILL.md
│   ├── sample_inputs/
│   ├── sample_outputs/
│   └── scripts/
├── README.md
└── logs/

이 구조에서 누락되면 안 되는 파일과 제출 직전 확인해야 할 사항을 표로 정리해줘.
```
