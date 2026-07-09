# AX Hackathon 2026

AX 해커톤 2026 Codex 플러그인 제출물을 준비하기 위한 작업 레포지토리입니다.

이 레포는 3개 기업별 Codex 플러그인 제출물을 기획, 구현, 검증, 병합, 패키징하기 위한 멀티에이전트 작업 공간입니다.

- 무신사
- 카카오페이증권
- 삼일PwC

## 레포 목적

목표는 참여 기업 또는 기업 고객이 겪는 실제 문제를 해결하는 실용적인 Codex 플러그인을 만드는 것입니다.

각 플러그인은 다음 근거를 바탕으로 설계합니다.

- 공개 자료 기반 기업 리서치
- 인터뷰 인사이트
- 합성 데모 데이터
- 반복 QA 및 레드팀 검증
- 원본 AI 협업 로그

이 루트 README는 프로젝트 운영용 문서입니다. 해커톤 제출물에 포함되는 기업별 README는 아래 위치에 따로 있습니다.

- `submissions/musinsa/submission/README.md`
- `submissions/kakaopaysec/submission/README.md`
- `submissions/samilpwc/submission/README.md`

## 제출 대상 구조

각 기업별 최종 제출물은 해커톤 규정에 맞춰 다음 구조를 가져야 합니다.

```text
submission.zip
├── README.md
├── logs/
└── src/
    ├── .codex-plugin/
    │   └── plugin.json
    └── skills/
        └── <skill-name>/
            └── SKILL.md
```

`submission.zip`은 사전 검증과 사람 확인이 끝난 뒤 최종 제출 직전에만 생성합니다.

## 작업 방식

이 프로젝트는 4대 PC에서 여러 Antigravity/Codex 채팅방을 병렬로 실행하는 방식으로 운영합니다.

핵심 런북:

- `docs/antigravity_16_chat_parallel_runbook_v2.md`

운영 모델:

- 16개 worker 에이전트가 기업별 플러그인 품질을 병렬 개선합니다.
- 3개 integration 에이전트가 기업별 worker PR을 검토하고 병합합니다.
- global coordinator가 작업 범위, 실행 주기, 품질 편향을 감시합니다.
- 각 worker는 담당 기업과 담당 역할만 작업합니다.
- 3개 기업 사이에 전역 우선순위는 없습니다.

실행 주기:

- 기본은 Adaptive Cadence입니다.
- 한 라운드가 끝나면 1분 뒤 다음 follow-up/timer를 예약합니다.
- 1분 follow-up이 불가능하면 5분 timer를 사용합니다.
- 빨리 끝난 라운드는 가짜 다음 라운드를 만들지 않고, 현재 라운드 안에서 근거 확인, 재검증, readback을 강화합니다.

## Git 브랜치 전략

권장 브랜치 구조:

```text
main
integration/musinsa
integration/kakaopaysec
integration/samilpwc
parallel/<swarm>/<company>
```

예시:

```text
parallel/reliability/musinsa
parallel/product-ux/kakaopaysec
parallel/golden-demo/samilpwc
```

운영 규칙:

- worker 에이전트는 자기 `parallel/*` 브랜치에만 커밋합니다.
- worker 에이전트는 `main`에 직접 병합하지 않습니다.
- integration 에이전트는 worker 브랜치를 기업별 `integration/<company>` 브랜치로 병합합니다.
- 최종 `main` 병합과 최종 ZIP 생성은 사람 확인 이후에만 진행합니다.

## GitHub Issue 및 PR 운영

Issue는 너무 많이 만들지 않고, 기업별 tracking issue 3개를 권장합니다.

- `[TRACKING] Musinsa Submission`
- `[TRACKING] KakaoPay Securities Submission`
- `[TRACKING] Samil PwC Submission`

PR 구조:

- worker 브랜치별 Draft PR 1개
- 기업별 integration PR 1개
- 최종 제출 전 release/pre-submission PR 1개

권장 라벨:

```text
company:musinsa
company:kakaopaysec
company:samilpwc
swarm:reliability
swarm:product-ux
swarm:business-readme
swarm:skill-behavior
swarm:golden-demo
agent:needs-review
agent:changes-requested
agent:ci-failed
agent:ready-to-merge
blocked:auth
blocked:merge-conflict
```

## 보안 및 토큰 관리

GitHub token, 환경 변수, 개인 인증 정보는 절대 커밋하지 않습니다.

로컬 GitHub 자동화는 `.env.local`을 사용합니다. 이 파일은 `.gitignore`에 포함되어 있으며 Git에 올라가면 안 됩니다.

설정 가이드:

- `docs/github_token_setup.md`

템플릿:

- `.env.example`

토큰 값을 아래 위치에 절대 남기지 않습니다.

- 채팅 메시지
- AI 작업 로그
- README
- 커밋 메시지
- PR 본문
- GitHub Actions 로그

## 최종 검증 체크리스트

각 기업별 제출물은 최종 패키징 전에 아래 항목을 통과해야 합니다.

- `README.md`가 존재하고 해커톤 필수 5문항에 답합니다.
- `src/.codex-plugin/plugin.json`이 유효한 JSON입니다.
- `src/skills/*/SKILL.md`가 존재합니다.
- `logs/`에 원본 AI 대화 로그가 보존되어 있습니다.
- 원본 transcript 로그를 삭제, 축약, 편집하지 않았습니다.
- `demo_transcript.md`가 있다면 simulated expected output임을 명시합니다.
- 직접 출처가 없는 ROI 수치에는 `[ASSUMPTION]` 또는 `[UNKNOWN]` 라벨이 붙어 있습니다.
- 최종 ZIP 안에 `.env`, `.env.local`, token, `.DS_Store`, 로컬 전용 파일이 포함되지 않습니다.

기업별 추가 체크:

- 무신사: 1-Pick 결정 UX를 유지하고, 추천지가 여러 개로 번지는 문제를 방지합니다.
- 카카오페이증권: 투자 권유, 수익 보장, 매수/매도 유도처럼 보이는 표현을 금지합니다.
- 삼일PwC: 근거 없는 결론을 금지하고, SOP 근거가 부족하면 human review로 전환합니다.

## 주요 문서

- `hackathon_instructions.md`
- `docs/final_submission_execution_roadmap.md`
- `docs/antigravity_16_chat_parallel_runbook_v2.md`
- `docs/github_token_setup.md`
- `interviews/insights.md`
- `research/`
- `submissions/`

## Architecture & Topics / 아키텍처 및 주제

**Architecture / 아키텍처**<br>
[`multi-agent-systems`](https://github.com/topics/multi-agent-systems) · [`agent-orchestration`](https://github.com/topics/agent-orchestration) · [`plugin-architecture`](https://github.com/topics/plugin-architecture) · [`tool-calling`](https://github.com/topics/tool-calling) · [`sandboxed-execution`](https://github.com/topics/sandboxed-execution) · [`human-in-the-loop`](https://github.com/topics/human-in-the-loop) · [`evaluation-driven-development`](https://github.com/topics/evaluation-driven-development) · [`red-team-testing`](https://github.com/topics/red-team-testing)

**Core technologies / 핵심 기술**<br>
[`model-context-protocol`](https://github.com/topics/model-context-protocol)

**Project context / 프로젝트 맥락**<br>
[`agentic-ai`](https://github.com/topics/agentic-ai) · [`ai-agents`](https://github.com/topics/ai-agents) · [`ai-assisted-development`](https://github.com/topics/ai-assisted-development) · [`automation`](https://github.com/topics/automation) · [`codex`](https://github.com/topics/codex) · [`developer-tools`](https://github.com/topics/developer-tools) · [`evaluation`](https://github.com/topics/evaluation) · [`hackathon`](https://github.com/topics/hackathon) · [`llm`](https://github.com/topics/llm) · [`multi-agent`](https://github.com/topics/multi-agent) · [`plugin-development`](https://github.com/topics/plugin-development) · [`prompt-engineering`](https://github.com/topics/prompt-engineering) · [`red-teaming`](https://github.com/topics/red-teaming) · [`security`](https://github.com/topics/security)

**Implementation stack / 구현 스택**<br>
[`mcp`](https://github.com/topics/mcp) · [`python`](https://github.com/topics/python)
