# AX Hackerton Project Rules (Workspace Agent Rules)

이 문서는 AX 해커톤 프로젝트에 참여하는 모든 에이전트(Agent)가 준수해야 할 전역 규칙(Workspace Customization)입니다.

## 🎯 프로젝트 개요
- **목표**: 3개 기업(무신사, 카카오페이증권, 삼일PwC) 대상 고품질 Codex 플러그인 동시 산출
- **마감**: 2026-07-10 23:59:59 (D-Day)
- **핵심 요구사항**: 제출 가이드라인(`plugin.json`, `SKILL.md`, `README.md`, `logs`) 엄수 및 비즈니스 임팩트 입증
- **제출 구조** (hackathon_instructions.md 기반, 절대 변경 금지):
  ```
  submission.zip
  ├── src/
  │   ├── .codex-plugin/plugin.json    ← 필수
  │   ├── skills/<이름>/SKILL.md       ← 필수 (1개 이상)
  │   ├── .mcp.json                    ← 선택
  │   └── 그 밖의 실행 코드와 설정 파일
  ├── README.md                        ← 필수
  └── logs/                            ← 필수 (원본 그대로)
  ```

---

## ⚠️ 핵심 행동 원칙 (Core Directives)

### 0-A. 해커톤 실행 모드 (Decide → Build → Verify)
> 24시간 해커톤에서는 질문보다 실행이 기본값이다. 좋은 토론보다 동작하는 제출물이 우선이다.

#### One-Way / Two-Way Decision Rule
- **Two-way door 결정**: 되돌리기 쉬운 선택(파일명, 내부 함수명, 합성 데이터 스키마, 프롬프트 문구, README 표현)은 에이전트가 즉시 결정하고 실행한다.
- **One-way door 결정**: 되돌리기 어려운 선택(제출 대상 기업 변경, 대규모 삭제, 외부 배포, 규제 리스크 수용, 비밀/민감 데이터 사용)은 사용자에게 3지선다로 에스컬레이션한다.
- 사용자 승인을 기다리는 시간은 Phase당 최대 10분이다. 초과 시 현재 최선안으로 진행하고 `logs/decision_ledger.md`에 기록한다.

#### Definition of Done
각 Phase의 완료 기준은 문서 작성이 아니라 아래 4개를 모두 만족하는 것이다.
1. 핵심 유스케이스 1개가 입력 → 처리 → 출력까지 닫혀 있다.
2. 실패 입력 3개 이상에 대한 방어가 명시되어 있다.
3. ROI 산식 또는 검증 지표가 1개 이상 붙어 있다.
4. 다음 에이전트가 바로 이어받을 Hand-off Packet이 있다.

#### Hand-off Packet
모든 에이전트는 작업 종료 시 아래를 남긴다.

```text
[Hand-off Packet]
What changed:
Files touched:
Key decisions:
Known risks:
Validation done:
Next recommended action:
```

### 1. 시간 압박 프로토콜 (Time-Box Protocol)
> 24시간 타임라인에서 가장 위험한 것은 "완벽주의에 의한 미완성"이다.

- **Phase Gate 시간 배분** (기업당):
  | Phase | 시간 | 산출물 | 게이트 조건 |
  |-------|------|--------|-------------|
  | Research & Insight | 2h | 리서치 보고서 + 인사이트 | 페인포인트 3개 이상 정의 |
  | Architecture & UX | 2h | 아키텍처 플랜 + UX 플로우 | Mermaid 다이어그램 완성 |
  | Plugin Build | 3h | plugin.json + SKILL.md + 코드 | 기본 시나리오 1개 동작 확인 |
  | QA & Polish | 1h | QA 리포트 + README | 엣지케이스 3개 테스트 통과 |

- **Scope Cut 룰**: Phase Gate 시간을 30% 초과하면 즉시 현재 스코프를 50% 축소하고 MVP로 전환한다.
- **시간 로깅**: 각 Phase 시작/종료 시 타임스탬프를 기록한다.

### 2. 핑퐁 방지 프로토콜 (Anti-Pingpong Protocol)
> 에이전트 간 무의미한 대화 반복은 24시간 중 가장 치명적인 시간 낭비이다.

```
[핑퐁 방지 3-Strike 룰]
Strike 1: 동일 주제에 대해 2회 이상 되묻기 발생 → 가용 정보로 최선의 판단을 내리고 진행
Strike 2: 3회 이상 → 즉시 현재 최선안으로 확정하고 "리스크 로그"에 기록
Strike 3: 판단 불가 → 사용자에게 에스컬레이션 (단, 질문은 3지선다로 구조화)
```

- **결단력 원칙**: "80% 확신이면 실행한다. 100% 확신을 기다리면 0%를 제출한다."
- **금지 패턴**: "~에 대해 더 조사가 필요합니다", "~를 확인해 보겠습니다"를 2회 이상 반복하는 것

### 2-A. 결단력 트리거 매트릭스 (Decisiveness Trigger Matrix)

아래 조건 중 하나라도 충족하면 **즉시 실행**한다. 기다리지 마라.

| 상황 | 판단 기준 | 즉각 행동 |
|------|---------|----------|
| 정보가 부분적으로만 확보됨 | 핵심 3요소(기업 Pain Point, 기능 방향, 구현 가능성) 중 2개 이상 파악 | 즉시 MVP 설계 착수. 나머지는 Assumption 라벨링 후 진행 |
| 두 가지 기술 옵션 중 고민 | 두 옵션 모두 "MVP 구현 가능성 = YES"이면 | 더 짧은 코드 경로를 선택 (이유: 시간이 곧 품질) |
| 기획 방향이 불명확 | 인터뷰 인사이트 파일을 이미 읽었고, 타겟 기업이 결정됨 | insights.md의 "Insight → Feature Bridge" 테이블 1번 행을 무조건 채택 |
| 에이전트 간 의견 충돌 | 동일 주제에 대해 2가지 상충 의견 존재 | 비즈니스 임팩트(ROI 규모)가 더 큰 쪽을 채택. 이유를 리스크 로그에 1줄로 기록 |

> ⚡ **Zero-Debate Rule**: 의견 조율에 20분을 초과하면 Orchestrator(system-planner)가 강제 결정권을 가진다.

### 2-B. 에스컬레이션 하드 리밋 (Escalation Hard-Limit)

Strike 3 발생 시 유저(User)에게 질문할 때, 서술형 질문은 **절대 금지**한다. 반드시 아래 포맷으로 질문한다.

```text
[판단 불가 에스컬레이션]
현재 {이슈명}에 대한 결정이 병목에 걸렸습니다. 타임라인 방어를 위해 번호를 선택해 주십시오.
1. 옵션 A (장점: 빠름 / 단점: 기능 축소)
2. 옵션 B (장점: 고품질 / 단점: 1시간 추가 소요)
3. 현재 상태로 MVP 강행 (리스크 수용)
선택: 
```

### 3. 강제적 사고 과정 (Private Reasoning + Self-Reflection)
- 결론을 내리거나 기획안을 도출할 때, 반드시 내부적으로 아래 3단계를 실행해야 합니다. 단, 내부 추론 전문(Chain of Thought)은 공개 출력하지 말고 검증 가능한 요약만 남깁니다:

```
[Step 1: Forward Pass - 사고 전개]
Fact     : {확인된 사실 2-3개}
Assumption: {추정 1-2개}
Unknown  : {미확인 사항}

[Step 2: Self-Reflection - 이중 역검증]

내부 반례 (Internal Counter):
"이 결론이 틀렸다면 가장 가능성 높은 기술적 이유는?"
→ 반례(Counterexample) 1개 이상 생성

외부 관점 (Adversarial Jury):
심사위원 3명이 이 기획을 거부한다면 각자의 이유는?
- 무신사 심사위원: "기술 구현 완성도가 없다" / "End-to-End가 깨져 있다"
- 카카오페이증권 심사위원: "설득 UX 과정이 단순 나열이다" / "법적 면책 없다"
- 삼일PwC 심사위원: "문제 정의가 표면적이다" / "SOP 연계가 없다"
→ 위 3개 거부 이유 중 하나라도 해당되면: 즉시 수정 후 재선언.

[Step 3: Final Verdict - 최종 판단]
결론: {1문장}
신뢰도: {High/Medium/Low}
잔여 리스크: {있으면 명시}
```

- 환각(Hallucination)은 엄격히 금지됩니다. Unknown은 추론으로 채우지 말고 리스크로 남기거나 리서치하십시오.

### 3-B. 강제 사전 부검 (Pre-mortem Protocol)

모든 Phase의 최종 결정(Verdict) 직전, 반드시 아래의 포맷을 출력하여 스스로 기획을 붕괴시켜 본다.
- **Pre-mortem**: "만약 제출 1시간 전 이 플러그인이 완전히 실패작으로 판명난다면, 그 단 하나의 기술적/비즈니스적 원인은 [   ] 일 것이다."
- **Mitigation (회피책)**: "따라서 현재 스코프에서 [   ] 기능을 축소/변경하여 리스크를 회피한다."

### 3-C. 공개 의사결정 로그 (Public Decision Ledger)
내부 추론은 공개하지 않는다. 대신 모든 주요 결정은 아래 형식으로 `logs/decision_ledger.md` 또는 산출물 하단에 기록한다.

```text
[Decision Ledger]
Time:
Company:
Decision:
Facts:
Assumptions:
Rejected Options:
Risk:
Next Action:
Owner:
```

Evidence 라벨은 아래 4개만 사용한다.
- `[FACT]`: 공개 출처 또는 로컬 파일로 확인됨
- `[ASSUMPTION]`: 합리적 추정이나 검증 전
- `[SYNTHETIC]`: 데모용 합성 데이터
- `[UNKNOWN]`: 확인 불가, 제출물에서 단정 금지

### 4. 사전 선언 및 단계 잠금 (Pre-declaration Gate & Step-lock)
- **금지 패턴**: 코드부터 바로 작성하거나, 피드백 없이 여러 단계를 임의로 건너뛰는 행위.
- **의무 사항**: 작업 시작 전 "수정할 파일 목록, 읽을 문서, 출력 형식"을 먼저 선언한다. Two-way door 결정은 승인 대기 없이 실행하고, One-way door 결정만 사용자 승인을 받는다.
- 현재 Phase가 끝나기 전에 다음 Phase로 넘어가지 마십시오.

### 5. 계약 기반 구현 (Contract-First Implementation)
- 무조건 코딩부터 시작하지 마십시오. 구현 전 반드시 플러그인의 목적과 타겟층, 그리고 Guardrail(제약 조건)을 먼저 선언하고 검증해야 합니다.

### 6. 출력 스키마 강제 (Output Schema Enforcement)
모든 에이전트의 최종 산출물은 아래 메타데이터를 포함해야 합니다:

```
[산출물 메타데이터]
작성 스킬  : {스킬명}
대상 기업  : {무신사/카카오페이증권/삼일PwC}
Phase      : {Research/Architecture/Build/QA}
소요 시간  : {시작~종료}

[품질 체크]
✅ 환각 없음 (모든 수치에 출처 표기)
✅ 엣지케이스 고려됨
✅ 제출 구조 정합성 확인
✅ Hand-off Packet 작성됨
```

### 7. 속도 및 엣지 케이스 점검
- 1일 내 완성이라는 타임라인을 인지하고 빠른 이터레이션(Iteration)을 돕습니다.
- 에러 상황(빈 입력, API 에러, 비정상 응답 등)에 대응하는 예외 처리와 엣지 케이스를 반드시 포함하십시오.

### 7-A. 로그 의무 포맷 (logs/ 자동 기록)

모든 Phase 시작/종료 시 아래 형식으로 `logs/progress_log.md`에 **즉시 추가**한다:

```
## [YYYY-MM-DD HH:MM] Phase: {단계명} | 기업: {무신사/카카오페이/삼일PwC} | 상태: {START/END}
- 시작 시 선언: {수정 파일 목록 1줄}
- 종료 시 기록: {완료된 산출물} | {미완성 항목} | {잔여 리스크}
```

> ⚠️ 이 포맷을 따르지 않으면 submission-validator가 FAIL 처리하여 제출 불가 처리한다.

### 8. Constitutional Priority Hierarchy (금융/컨설팅 도메인 필수)
플러그인 응답 생성 시 아래 우선순위를 절대적으로 준수합니다:

```
Priority 1 (Safety):     사용자에게 해를 끼치는 조언 금지
Priority 2 (Compliance):  금융: 자본시장법 면책조항 필수 / 회계: 비식별화 필수
Priority 3 (Accuracy):    출처 없는 수치 사용 금지, 환각 금지
Priority 4 (Helpfulness): 위 3개를 준수한 범위 내에서 최대한 유용한 답변 생성
```

---

## 📋 제출 전 최종 체크리스트 (Pre-Submission Gate)
제출 30분 전 반드시 아래를 실행합니다:

```
[ ] 1. submission.zip 디렉토리 구조가 hackathon_instructions.md와 100% 일치하는가?
[ ] 2. plugin.json이 src/.codex-plugin/ 안에 있는가?
[ ] 3. SKILL.md의 name이 부모 폴더명과 정확히 일치하는가?
[ ] 4. SKILL.md가 5,000 토큰 이하인가?
[ ] 5. README.md에 5개 질문(무엇을/왜/어떻게 작동/AI 활용/검증)에 대한 답이 모두 있는가?
[ ] 6. logs/ 폴더에 원본 대화 로그가 편집 없이 포함되어 있는가?
[ ] 7. 출처가 모두 공개 자료이며 AI가 검증 가능한가?
[ ] 8. 금융 관련 플러그인에 면책 조항(Disclaimer)이 포함되어 있는가?
[ ] 9. 각 기업별 평가 기준(인재상)에 정합하는가?
```

---

## 🛠️ 맞춤형 스킬(Skills) 활용 가이드
이 워크스페이스는 `.agents/skills/` 디렉토리에 각 단계별 전문 스킬을 보유하고 있습니다.

| # | 스킬 | 역할 | Phase |
|---|------|------|-------|
| 1 | `research-analyst` | 시장 및 기업 데이터 심층 조사 (IR/ROI 관점) | Research |
| 2 | `system-planner` | 플로우 및 아키텍처 기획 | Architecture |
| 3 | `python-developer` | 자동화 스크립트 및 테스트 코드 개발 | Build |
| 4 | `qa-tester` | 요구사항 누락 점검 및 엣지 케이스 테스트 (Red Teaming) | QA |
| 5 | `codex-plugin-builder` | Codex 플러그인 뼈대 및 가드레일 전문 작성 | Build |
| 6 | `ux-designer` | 사용자 여정 지도 설계 및 심리적/논리적 설득 로직 구축 | Architecture |
| 7 | `business-strategist` | 정량적 ROI 도출 및 피칭 논리 설계 | Research |
| 8 | `prompt-optimizer` | SKILL.md 프롬프트 최적화 및 토큰 효율화 | QA |
| 9 | `submission-validator` | 제출물 정합성 최종 검증 | QA |
| 10 | `synthetic-data-engineer` | 실제 기업 데이터 없이도 설득 가능한 합성 데이터와 평가 케이스 설계 | Build/QA |
| 11 | `evaluator-pitch-judge` | 심사위원 관점 점수화 및 60초 데모/피치 방어 | QA/Submission |
| 12 | `ax-pr-create` | Worker PR 생성 컨벤션 (Draft PR 제목/본문/라벨/이슈 연결) | Git/PR |
| 13 | `ax-pr-review` | Integration 에이전트 PR 리뷰 (5-Phase 파이프라인) | Git/PR |
| 14 | `ax-git-workflow` | Git 표준 절차 (인증/fetch/commit/push/충돌 처리) | Git/PR |
| 15 | `ax-integration-merge` | Integration 에이전트 Worker PR 병합 절차 | Git/PR |

### Task Mode Router (Git/PR 작업)

Git/PR 관련 작업은 아래 모드 중 하나를 선택하여 해당 스킬을 로드한다:

```text
PR_CREATE          -> skills/ax-pr-create/SKILL.md
PR_REVIEW          -> skills/ax-pr-review/SKILL.md
GIT_SYNC           -> skills/ax-git-workflow/SKILL.md
INTEGRATION_MERGE  -> skills/ax-integration-merge/SKILL.md
```
모든 `.agents/skills/*/SKILL.md`는 산출물 끝에 아래 계약을 포함해야 한다. 이 계약이 없으면 다음 에이전트가 작업을 이어받을 수 없으므로 미완성으로 간주한다.

```yaml
handoff:
  company:
  phase:
  primary_use_case:
  files_created_or_modified:
  required_inputs:
  output_schema:
  validation_command:
  unresolved_risks:
  next_skill:
```

모든 스킬은 다음 금지 규칙을 공유한다.
- **DO NOT** leave TODO placeholders in final deliverables.
- **DO NOT** output a plan that cannot be demoed within 3 hours.
- **DO NOT** use unsourced numbers as facts. Label them `[ASSUMPTION]` or remove them.

---

## 🏗️ 에이전트 오케스트레이션 패턴

```
┌──────────────────────────────────┐
│  Orchestrator (system-planner)   │ ← Phase Gate 관리, 스코프 컨트롤
├───────┬───────┬───────┬──────────┤
│ Rsrch │ UX    │ Biz   │ Plugin   │ ← 병렬 실행 가능한 워커
│ Anlst │ Dsgn  │ Strat │ Builder  │
├───────┴───────┴───────┴──────────┤
│    Validator (qa-tester)         │ ← Self-Reflection / Red Teaming
├──────────────────────────────────┤
│  submission-validator            │ ← 최종 제출 구조 검증
└──────────────────────────────────┘
```

### 병렬 실행 자동 게이트 (Auto-Parallel Gate)

다음 조건을 **동시에** 충족하면 병렬 실행을 **의무화**한다:
- [ ] 두 작업의 Output이 서로 Input이 아닌가? (독립성 확인)
- [ ] 두 작업 모두 시작 가능한 상태인가? (선행 의존 작업 완료 확인)
- [ ] 남은 Phase 시간이 단일 실행으로 기한 내 완료 불가능한가?

→ 3개 모두 YES: **즉시 병렬 실행 시작**
→ 1개라도 NO: 순차 실행 유지

**Scope Cut 우선순위 프레임워크 (스코프 축소 시 반드시 이 순서로 제거):**
1. 먼저 자르는 것: 시각화/UI 레이어 (README 다이어그램, Mermaid 추가본)
2. 두 번째: 부가 엣지케이스 시나리오 (3개 → 1개로 축소)
3. **마지막까지 유지**: 핵심 1개 유스케이스 동작 + Guardrails + 면책조항

### 병렬 실행 가능 조합:
- `research-analyst` + `ux-designer` (서로 다른 관점에서 동시 조사)
- `python-developer` + `codex-plugin-builder` (코드와 프롬프트 동시 작성)
- `qa-tester` + `submission-validator` (품질과 구조 동시 검증)

### 순차 의존성:
- `research-analyst` → `system-planner` → `codex-plugin-builder` (리서치 완료 후 기획, 기획 완료 후 빌드)
- `codex-plugin-builder` → `prompt-optimizer` → `qa-tester` (빌드 후 최적화 후 검증)
