---
name: ax-git-workflow
description: "Use this skill when 에이전트가 git fetch, branch, commit, push, gh auth 등 Git/GitHub 작업을 수행해야 할 때. Do NOT use when PR 생성/리뷰/merge 등 고수준 워크플로우만 필요할 때."
metadata:
  author: ax-hackathon-team
  version: "1.0"
---

# Purpose
당신은 AX Hackathon 병렬 작업 환경의 Git 운영 전문가입니다. 4대 PC × 16개 채팅방이 동시에 작업할 때 충돌·인증 실패·범위 위반을 방지하는 Git 표준 절차를 강제합니다.

# When to Use This Skill
- **Use when**: git fetch, checkout, commit, push 등 Git 명령을 실행할 때
- **Use when**: GitHub CLI(gh)로 인증하거나 PR/Issue 작업할 때
- **Use when**: 라운드 시작 전 브랜치 동기화가 필요할 때
- **Do NOT use when**: PR 생성/업데이트만 필요할 때 (→ ax-pr-create)
- **Do NOT use when**: PR 리뷰만 필요할 때 (→ ax-pr-review)

# Branch Naming Convention
```
parallel/{swarm}/{company}
```

| 변수 | 값 예시 |
|---|---|
| `{swarm}` | reliability, product-ux, business-readme, skill-behavior, golden-demo |
| `{company}` | musinsa, kakaopaysec, samilpwc |

예시: `parallel/reliability/musinsa`, `parallel/product-ux/kakaopaysec`

보호 브랜치 (worker 접근 금지):
- `main`
- `integration/musinsa`
- `integration/kakaopaysec`
- `integration/samilpwc`

# Workflow

## Step 1: 인증 (Auth)
모든 git/gh 명령 전에 실행한다.

```bash
# 1. 환경 변수 로드
set -a; source .env.local; set +a

# 2. 토큰 존재 확인
if [ -z "$GITHUB_TOKEN" ] && [ -z "$GH_TOKEN" ]; then
  echo "BLOCKED_AUTH: GITHUB_TOKEN/GH_TOKEN이 비어 있음"
  # merge_packet.md에 BLOCKED_AUTH 기록 후 중단
  exit 1
fi

# 3. GitHub CLI 인증 (필요 시)
printf '%s' "$GH_TOKEN" | gh auth login --with-token

# 4. git 인증 위임 (가능하면)
gh auth setup-git
```

**절대 금지:**
- `echo "$GITHUB_TOKEN"` 또는 `echo "$GH_TOKEN"` 실행
- 토큰 값을 로그, 커밋 메시지, PR 본문, README에 포함

## Step 2: 라운드 시작 전 동기화 (Fetch & Sync)
```bash
# 1. 원격 최신 상태 가져오기
git fetch origin --prune

# 2-A. 원격에 BRANCH가 있는 경우
git checkout {BRANCH}
git pull --rebase origin {BRANCH}

# 2-B. 원격에 BRANCH가 없는 경우
git checkout main
git pull origin main
git checkout -b {BRANCH}
git push -u origin {BRANCH}
```

## Step 3: 라운드 종료 후 커밋 (Stage & Commit)
```bash
# 1. 변경 파일 확인
git status --short

# 2. 범위 내 파일만 stage
git add {TARGET_PATH}/ {LOG_NAMESPACE}/

# 3. 범위 외 파일이 stage되지 않았는지 재확인
git diff --cached --name-only | grep -v "^submissions/{COMPANY}/"
# 위 결과가 있으면 → git reset HEAD {file} 로 unstage

# 4. 커밋
git commit -m "{CHAT_LABEL}: iteration {n} product improvement"
```

## Step 4: Push
```bash
# 첫 push
git push -u origin {BRANCH}

# 이후 push
git push origin {BRANCH}
```

## Step 5: 충돌 처리 (Conflict Resolution)
pull/rebase/push 중 충돌 발생 시:

1. **rebase 중단**: `git rebase --abort`
2. **merge_packet.md에 기록**:
   ```markdown
   ## BLOCKED_GIT
   - Timestamp: {ISO 8601}
   - Branch: {BRANCH}
   - Operation: {pull --rebase / push / merge}
   - Error: {전체 에러 메시지}
   - Conflicting Files: {파일 목록}
   - Action Required: Integration agent 확인 필요
   ```
3. **절대 force push하지 않는다.**
4. Integration agent 또는 global coordinator에게 보고한다.

# Staging 범위 규칙

| 허용 | 금지 |
|---|---|
| `{TARGET_PATH}/` 하위 | `.agents/` |
| `{LOG_NAMESPACE}/` 하위 | `docs/` |
| | `research/` |
| | `interviews/` |
| | 다른 회사 `submissions/` |
| | 다른 swarm `logs/parallel/` |
| | `submission.zip` |
| | 원본 `transcript.jsonl` |

# Commit Message 형식
```
{CHAT_LABEL}: iteration {n} product improvement
```

| 필드 | 규칙 |
|---|---|
| `{CHAT_LABEL}` | PC 배치표의 채팅창 라벨 (예: M1MINI-01-reliability-musinsa) |
| `{n}` | 현재 iteration 번호 (1부터 시작, 단조 증가) |

예시:
```
M1MINI-01-reliability-musinsa: iteration 3 product improvement
M3AIR-02-product-ux-kakaopaysec: iteration 12 product improvement
```

# 금지 사항 (DO NOT)
- **DO NOT** `git push --force` 또는 `git push -f`를 사용한다. 어떤 상황에서도 금지.
- **DO NOT** `main` 브랜치에 push한다.
- **DO NOT** `integration/*` 브랜치에 push한다 (integration agent 전용).
- **DO NOT** TARGET_PATH와 LOG_NAMESPACE 범위 밖 파일을 stage/commit한다.
- **DO NOT** `echo "$GITHUB_TOKEN"` 또는 `echo "$GH_TOKEN"`을 실행한다.
- **DO NOT** 토큰 값을 어떤 파일에도 기록한다.
- **DO NOT** `.env.local` 파일을 commit한다.
- **DO NOT** 충돌을 자체적으로 resolve하고 force push한다.
- **DO NOT** 다른 worker의 브랜치에 push한다.

# Error Recovery
| 상황 | 대응 |
|---|---|
| `.env.local` 없음 | `BLOCKED_AUTH` → merge_packet.md 기록, Git 작업 중단 |
| 토큰 비어 있음 | `BLOCKED_AUTH` → merge_packet.md 기록, Git 작업 중단 |
| push 거부 | `BLOCKED_GIT` → rebase --abort, merge_packet.md 기록 |
| rebase 충돌 | `BLOCKED_GIT` → rebase --abort, merge_packet.md 기록 |
| 인증 만료 | Step 1 재실행 후 재시도 |
| 원격 브랜치 삭제됨 | main에서 재생성: checkout -b, push -u |

# Validation Checklist
- [ ] `.env.local` 로드 완료 (GITHUB_TOKEN 또는 GH_TOKEN 존재)
- [ ] 토큰 값이 출력/로그/커밋에 노출되지 않음
- [ ] `git fetch origin --prune` 실행 완료
- [ ] 브랜치 이름이 `parallel/{swarm}/{company}` 형식
- [ ] stage된 파일이 TARGET_PATH + LOG_NAMESPACE 범위 이내
- [ ] 커밋 메시지가 `{CHAT_LABEL}: iteration {n} product improvement` 형식
- [ ] force push 사용하지 않음
- [ ] 충돌 발생 시 merge_packet.md에 BLOCKED_GIT 기록됨
