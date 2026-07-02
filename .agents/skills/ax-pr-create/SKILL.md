---
name: ax-pr-create
description: "Use this skill when worker 에이전트가 자기 브랜치의 Draft PR을 생성하거나 기존 Draft PR을 업데이트해야 할 때. Do NOT use when integration 브랜치나 main으로의 merge PR을 만들 때."
metadata:
  author: ax-hackathon-team
  version: "1.0"
---

# Purpose
당신은 AX Hackathon 병렬 작업 환경의 PR 생성 전문가입니다. 16개 worker 채팅방이 동시에 만드는 Draft PR의 제목·본문·커밋·라벨이 일관되도록 표준을 강제합니다.

# When to Use This Skill
- **Use when**: 라운드 종료 후 변경사항을 Draft PR로 만들거나 기존 PR을 업데이트할 때
- **Use when**: 첫 push 후 Draft PR을 최초 생성할 때
- **Do NOT use when**: integration/{company} 브랜치로 merge하는 PR을 만들 때 (→ ax-integration-merge)
- **Do NOT use when**: git fetch/branch/commit 등 단순 git 작업만 할 때 (→ ax-git-workflow)

# Workflow

## Step 1: 사전 조건 확인
1. `BRANCH`, `COMPANY`, `SWARM_ID`, `CHAT_LABEL` 환경 변수가 설정되어 있는지 확인한다.
2. `BRANCH`가 `parallel/{swarm}/{company}` 형식인지 검증한다.
3. GitHub CLI 인증 상태를 확인한다: `gh auth status`
4. 인증 안 되어 있으면 `printf '%s' "$GH_TOKEN" | gh auth login --with-token`

## Step 2: 커밋 생성
1. `git status --short`로 변경 파일을 확인한다.
2. **TARGET_PATH와 LOG_NAMESPACE 하위 파일만** stage한다:
   ```bash
   git add {TARGET_PATH}/ {LOG_NAMESPACE}/
   ```
3. 커밋 메시지 형식을 준수한다:
   ```
   {CHAT_LABEL}: iteration {n} product improvement
   ```
   예: `M1MINI-01-reliability-musinsa: iteration 5 product improvement`

## Step 3: Push
1. 원격에 브랜치가 **처음**이면: `git push -u origin {BRANCH}`
2. 이미 존재하면: `git push origin {BRANCH}`
3. push 실패 시 → Step 6 (충돌 처리)으로 이동

## Step 4: Draft PR 생성
기존 Draft PR이 없으면 새로 생성한다:
```bash
gh pr create \
  --draft \
  --title "[AX][{COMPANY}][{SWARM_ID}] {CHAT_LABEL}" \
  --body "$(cat <<'EOF'
## Iteration {n} Summary

### Files Changed
- {file1}
- {file2}

### Validation Results
| Check | Result |
|---|---|
| Scope Lock | ✅ {COMPANY} only |
| Schema Consistency | ✅ / ❌ |
| Guardrails Intact | ✅ / ❌ |

### Remaining Risks
- {risk1}

### Merge Notes
- Integration agent: squash merge into integration/{COMPANY}

Relates to #{issue_number}
EOF
)" \
  --label "agent:needs-review"
```

## Step 5: 기존 Draft PR 업데이트
Draft PR이 이미 있으면 본문만 업데이트한다:
```bash
PR_NUMBER=$(gh pr list --head "{BRANCH}" --json number -q '.[0].number')
gh pr edit "$PR_NUMBER" --body "{updated body}"
```

## Step 6: 충돌 처리
push/rebase 충돌 발생 시:
1. **절대 force push하지 않는다.**
2. `merge_packet.md`에 아래를 기록한다:
   ```markdown
   ## BLOCKED_GIT
   - Timestamp: {ISO 8601}
   - Branch: {BRANCH}
   - Error: {git error message}
   - Action Required: Integration agent 또는 coordinator 확인 필요
   ```
3. PR에 `BLOCKED_GIT` 라벨이 있으면 추가한다.

# PR 제목 형식
```
[AX][{COMPANY}][{SWARM_ID}] {CHAT_LABEL}
```

예시:
- `[AX][musinsa][swarm-reliability] M1MINI-01-reliability-musinsa`
- `[AX][kakaopaysec][swarm-product-ux] M3AIR-02-product-ux-kakaopaysec`
- `[AX][samilpwc][swarm-golden-demo] M1MAX-06-golden-demo-samilpwc`

# PR 본문 필수 섹션
| 섹션 | 내용 |
|---|---|
| Iteration Summary | 최신 iteration 번호와 이번 라운드 목표 |
| Files Changed | 변경된 파일 전체 목록 (경로 포함) |
| Validation Results | scope lock, schema, guardrails 검증 결과 표 |
| Remaining Risks | 알려진 이슈, 미완료 항목 |
| Merge Notes | integration agent를 위한 병합 참고사항 |
| Issue Link | `Relates to #{issue_number}` |

# Labels
| 라벨 | 적용 주체 |
|---|---|
| `company:{company}` | CI 자동 |
| `swarm:{swarm}` | CI 자동 |
| `agent:needs-review` | Worker가 수동 추가 |

# 금지 사항 (DO NOT)
- **DO NOT** main 브랜치에 직접 push한다.
- **DO NOT** integration/* 브랜치에 직접 push한다.
- **DO NOT** TARGET_PATH와 LOG_NAMESPACE 범위 밖 파일을 stage한다.
- **DO NOT** force push (`git push --force`, `git push -f`)를 사용한다.
- **DO NOT** 다른 회사의 파일을 변경하는 커밋을 포함한다.
- **DO NOT** 토큰 값을 커밋 메시지나 PR 본문에 포함한다.
- **DO NOT** Draft가 아닌 일반 PR을 생성한다 (worker는 항상 Draft).

# Validation Checklist
- [ ] 브랜치 이름이 `parallel/{swarm}/{company}` 형식
- [ ] 커밋 메시지가 `{CHAT_LABEL}: iteration {n} product improvement` 형식
- [ ] PR 제목이 `[AX][{COMPANY}][{SWARM_ID}] {CHAT_LABEL}` 형식
- [ ] PR 본문에 6개 필수 섹션 모두 포함
- [ ] stage된 파일이 TARGET_PATH + LOG_NAMESPACE 범위 이내
- [ ] `Relates to #{issue_number}` 링크 포함
- [ ] `agent:needs-review` 라벨 추가
- [ ] Draft PR로 생성됨
