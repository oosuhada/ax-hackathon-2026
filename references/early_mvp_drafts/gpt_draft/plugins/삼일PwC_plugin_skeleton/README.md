# AX 해커톤 예선 제출 스켈레톤 — Samil PwC AX Use Case Prioritizer

## Plugin concept

**Plugin name:** `samil-ax-usecase-prioritizer`

기업의 업무 프로세스와 pain point를 입력하면 Codex가 AX/GenAI 적용 후보를 도출하고, impact·feasibility·data readiness·risk·change difficulty 기준으로 우선순위를 매긴 뒤, PoC 계획과 임원 보고용 요약을 생성하는 플러그인입니다.

핵심 차별점은 “AI 아이디어 목록”이 아니라 **컨설팅 산출물 형태의 AX use-case portfolio + PoC roadmap**입니다.

---

## 1. 무엇을, 누가, 어떤 상황에서 쓰나요?

이 플러그인은 AX 컨설턴트, 전략기획팀, 재무/경영관리팀, DX/AI TF, 중견기업 경영진이 사용합니다. 기업이 생성형 AI를 도입하고 싶지만 어떤 업무부터 시작해야 할지, ROI와 리스크를 어떻게 비교해야 할지, 4주 PoC를 어떻게 설계해야 할지 결정해야 하는 상황에서 사용합니다.

---

## 2. 왜 이 문제를 선택했나요?

많은 기업은 생성형 AI 도입 필요성을 인식하지만, 실제 업무 적용 단계에서는 우선순위 선정, 데이터 준비도, 보안·거버넌스, 변화관리, PoC 성공지표 설정에서 어려움을 겪습니다. 삼일PwC는 AX/Digital/AI 컨설팅 맥락에서 이런 문제를 다루는 기업이므로, Codex 플러그인으로 AX use case를 구조화하고 우선순위를 정하는 문제는 기업의 산업과 직접적으로 연결됩니다.

최종 제출 전 `src/skills/samil-ax-usecase-prioritizer/references/evidence_sources.md`에 공개자료 기반 근거를 채워야 합니다.

---

## 3. 플러그인은 어떻게 작동하나요?

1. 사용자가 업무 프로세스 목록과 회사 컨텍스트를 제공합니다.
2. helper script가 기본 impact/feasibility/data/risk 점수를 생성합니다.
3. Codex skill이 컨설팅 관점에서 use case를 보강하고 포트폴리오로 분류합니다.
4. 최종 산출물은 다음과 같습니다.
   - AX Use Case Portfolio
   - Prioritization Matrix
   - Top 3 PoC Plans
   - Data and System Requirements
   - Risk and Governance Checklist
   - Executive One-Pager

샘플 실행:

```bash
python src/scripts/prioritize_ax_usecases.py \
  --processes src/sample_inputs/business_processes.csv \
  --context src/sample_inputs/company_context.md \
  --out src/sample_outputs

python src/scripts/validate_submission_structure.py
```

---

## 4. AI를 어떻게 활용했나요?

AI는 문제정의, AX scoring framework 구성, plugin/skill 작성, PoC roadmap 템플릿 설계, 샘플 업무 프로세스 생성, 리스크·거버넌스 체크리스트 구성에 활용합니다.

주의: 실제 제출 시 이 문항은 `logs/` 폴더에 포함된 원본 AI 작업 로그와 반드시 일치해야 합니다.

---

## 5. 어떻게 검증했나요?

검증은 다음 기준으로 수행합니다.

- 제출 구조 검증: `plugin.json`, `SKILL.md`, `README.md`, `logs/` 존재 여부
- 샘플 업무 프로세스 입력에 대한 산출물 생성 여부
- use case가 실제 pain point와 연결되는지
- ROI/효과 수치를 근거 없이 조작하지 않는지
- high-risk workflow에 governance/human review가 포함되는지
- PoC 계획이 4주 내 실행 가능한 수준인지
- 공개자료 기반 문제정의와 플러그인 기능이 일치하는지

---

## Final submission reminder

- `logs/README_REPLACE_WITH_RAW_LOGS.md`는 placeholder입니다. 제출 전 원본 AI 작업 로그로 교체하세요.
- `evidence_sources.md`의 TODO를 실제 공개자료 URL과 근거로 채우세요.
- 여러 기업을 제출하는 경우, 기업별로 별도의 zip을 제출해야 합니다.
