---
name: ax-integration-merge
description: "Use this skill when integration 에이전트가 승인된 worker PR을 integration/{company} 브랜치로 squash merge해야 할 때. Do NOT use when main 브랜치로의 최종 병합이 필요할 때 (인간 전용)."
metadata:
  author: ax-hackathon-team
  version: "1.0"
---

# Purpose
당신은 AX Hackathon의 integration agent입니다. 리뷰를 통과한 worker PR을 integration/{company} 브랜치로 안전하게 병합하고, 충돌 시 문서화하며, main 병합은 인간에게 넘깁니다.

# When to Use This Skill
- **Use when**: Worker PR이 ax-pr-review Phase 5에서 APPROVE를 받은 후 병합할 때
- **Use when**: Integration 브랜치에 여러 worker PR을 순차 병합할 때
- **Do NOT use when**: Worker PR 리뷰가 아직 완료되지 않았을 때 (→ ax-pr-review)
- **Do NOT use when**: main 브랜치로 최종 병합할 때 (인간 전용 게이트)
- **Do NOT use when**: Worker가 자기 PR을 직접 merge할 때 (금지)

# Integration Agent 배치표

| 채팅방 | 담당 회사 | 병합 대상 브랜치 |
|---|---|---|
| INTEGRATION-01-musinsa-pr-review | musinsa | `integration/musinsa` |
| INTEGRATION-02-kakaopaysec-pr-review | kakaopaysec | `integration/kakaopaysec` |
| INTEGRATION-03-samilpwc-pr-review | samilpwc | `integration/samilpwc` |

# Workflow

## Step 1: 병합 자격 검증 (Pre-merge Gate)
PR 병합 전 아래 조건을 **모두** 확인한다. 하나라도 실패하면 병합하지 않는다.

| # | 조건 | 확인 방법 | 실패 시 |
|---|---|---|---|
| 1 | APPROVE 존재 | PR에 APPROVE 코멘트가 있음 | 병합 금지 |
| 2 | 리뷰어 ≠ 작성자 | APPROVE를 낸 CHAT_LABEL ≠ PR 작성 CHAT_LABEL | 병합 금지 |
| 3 | CI 통과 | `gh pr checks {PR_NUMBER}` 모두 pass | 병합 금지 |
| 4 | BLOCKED 라벨 없음 | `BLOCKED_GIT`, `BLOCKED_AUTH` 라벨 없음 | 병합 금지 |
| 5 | Scope 준수 | 변경 파일이 해당 COMPANY 범위 이내 | 병합 금지 |

```bash
# 자격 검증 명령
gh pr view {PR_NUMBER} --json reviews,labels,statusCheckRollup
gh pr diff {PR_NUMBER} --name-only
```

## Step 2: Integration 브랜치 동기화
```bash
# 환경 변수 로드
set -a; source .env.local; set +a

# 최신 상태 가져오기
git fetch origin --prune

# integration 브랜치 checkout 및 동기화
git checkout integration/{COMPANY}
git pull --rebase origin integration/{COMPANY}
```

## Step 3: Squash Merge 실행
```bash
# GitHub CLI로 squash merge
gh pr merge {PR_NUMBER} \
  --squash \
  --subject "[AX][{COMPANY}] Merge {WORKER_CHAT_LABEL} iteration {n}" \
  --body "Squash merge of #{PR_NUMBER} into integration/{COMPANY}

## Merged Content
- Worker: {WORKER_CHAT_LABEL}
- Branch: {WORKER_BRANCH}
- Iterations: {iteration range}
- Files: {file count} changed

## Review
- Reviewer: {INTEGRATION_CHAT_LABEL}
- Verdict: APPROVED at {commit_hash}"
```

## Step 4: 충돌 발생 시 처리
squash merge 중 충돌이 발생하면:

1. **merge를 중단하고 상태를 확인한다:**
   ```bash
   git merge --abort  # 또는 gh pr merge 실패 확인
   ```

2. **merge_packet.md에 기록한다:**
   ```markdown
   ## BLOCKED_GIT (Integration Merge)
   - Timestamp: {ISO 8601}
   - PR: #{PR_NUMBER}
   - Worker Branch: {WORKER_BRANCH}
   - Integration Branch: integration/{COMPANY}
   - Conflicting Files:
     - {file1}
     - {file2}
   - Resolution Plan: {수동 해결 방법 또는 worker에게 rebase 요청}
   ```

3. **수동 해결이 가능한 경우:**
   - 충돌 파일을 열어 양쪽 변경 의도를 확인한다.
   - Worker의 최신 변경을 우선하되, integration 브랜치의 기존 병합 결과를 깨지 않도록 한다.
   - 해결 후 커밋 메시지에 충돌 해결 사유를 포함한다.

4. **수동 해결이 어려운 경우:**
   - Worker에게 integration/{COMPANY} 기준으로 rebase를 요청한다.
   - PR에 코멘트로 충돌 파일 목록과 rebase 방법을 안내한다.

## Step 5: 병합 후 검증
```bash
# 1. integration 브랜치에 merge commit 확인
git log --oneline -5

# 2. PR 상태 업데이트 (자동)
# gh pr merge가 성공하면 PR은 자동으로 Merged 상태가 됨

# 3. merge commit SHA 기록
MERGE_SHA=$(git rev-parse HEAD)
echo "Merge commit: $MERGE_SHA"
```

## Step 6: PR 업데이트
병합 완료 후 PR에 결과를 코멘트로 남긴다:
```markdown
## ✅ Merged to integration/{COMPANY}

- **Merge Commit**: {MERGE_SHA}
- **Method**: Squash merge
- **Integration Branch**: integration/{COMPANY}
- **Timestamp**: {ISO 8601}
- **Next**: Human review for main merge
```

# 병합 순서 원칙
동일 COMPANY에 대해 여러 worker PR이 대기 중일 때:

1. APPROVE 시각이 빠른 순서로 병합한다.
2. 충돌이 발생하면 나중 PR의 worker에게 rebase를 요청한다.
3. P0/P1 수정이 포함된 PR을 우선 병합할 수 있다 (사유 기록).

# 금지 사항 (DO NOT)
- **DO NOT** main 브랜치에 merge한다. main 병합은 인간 전용이다.
- **DO NOT** CI가 통과하지 않은 PR을 merge한다.
- **DO NOT** 자기가 작성한 PR을 자기가 merge한다.
- **DO NOT** APPROVE 없이 PR을 merge한다.
- **DO NOT** BLOCKED_GIT 또는 BLOCKED_AUTH 라벨이 붙은 PR을 merge한다.
- **DO NOT** integration 브랜치에 force push한다.
- **DO NOT** 담당 회사가 아닌 PR을 merge한다.
- **DO NOT** 충돌을 worker와 상의 없이 임의로 해결한다 (단순 충돌 제외).
- **DO NOT** submission.zip을 생성하거나 커밋한다.

# main 병합 게이트 (Human-Only)
```
┌─────────────────────────────────────────────────┐
│  integration/{company} → main 병합은 인간만 수행  │
│                                                   │
│  조건:                                            │
│  1. 모든 worker PR이 integration에 병합 완료       │
│  2. integration 브랜치에서 최종 검증 완료           │
│  3. 인간이 submission.zip 생성 및 제출             │
└─────────────────────────────────────────────────┘
```

# Validation Checklist
- [ ] Pre-merge Gate 5개 조건 모두 통과
- [ ] integration/{COMPANY} 브랜치가 최신 상태
- [ ] Squash merge 성공 (충돌 없음 또는 해결 완료)
- [ ] Merge commit SHA 기록됨
- [ ] PR에 merge 결과 코멘트 작성됨
- [ ] main 브랜치에 직접 merge하지 않음
- [ ] 담당 회사 PR만 처리함
