---
name: ax-pr-review
description: "Use this skill when integration 에이전트가 worker PR을 리뷰하여 integration/{company} 브랜치로 merge 여부를 판단해야 할 때. Do NOT use when worker가 자기 PR을 자체 검증할 때."
metadata:
  author: ax-hackathon-team
  version: "1.0"
---

# Purpose
당신은 AX Hackathon의 integration agent입니다. Worker 채팅방에서 올라온 Draft PR을 5단계 파이프라인으로 리뷰하여 integration/{company} 브랜치로의 병합 가능 여부를 판단합니다.

# When to Use This Skill
- **Use when**: Worker의 Draft PR에 `agent:needs-review` 라벨이 붙어 있을 때
- **Use when**: Worker PR이 업데이트되어 재검토가 필요할 때
- **Do NOT use when**: Worker가 자기 PR을 스스로 검증할 때 (→ ax-pr-create의 checklist)
- **Do NOT use when**: integration/{company} → main 병합을 검토할 때 (인간 전용)

# 5-Phase Review Pipeline

## Phase 1: Scope Check (범위 검증)
PR이 선언된 COMPANY와 SWARM 파일만 변경했는지 확인한다.

| 검증 항목 | 기준 | 위반 시 |
|---|---|---|
| 파일 경로 | `submissions/{COMPANY}/` 하위만 | **BLOCKING** |
| 로그 경로 | `logs/parallel/{SWARM_ID}/` 하위만 | **BLOCKING** |
| 타 회사 파일 | 변경 0개 | **BLOCKING**: cross-company contamination |
| .agents, docs, research | 변경 0개 | **BLOCKING** |

```bash
# 범위 외 파일 탐지
gh pr diff {PR_NUMBER} --name-only | grep -v "^submissions/{COMPANY}/"
```

## Phase 2: Submission Structure (구조 검증)
제출물 디렉토리 구조가 해커톤 규격을 준수하는지 확인한다.

| 검증 항목 | 기준 | 분류 |
|---|---|---|
| plugin.json | 존재 + 유효한 JSON | **BLOCKING** |
| SKILL.md name | 부모 폴더명과 일치 | **BLOCKING** |
| SKILL.md 크기 | ≤ 5,000 토큰 | **non-blocking** (suggestion) |
| README.md | 5개 필수 질문 답변 포함 | **BLOCKING** |
| logs/ | 유효한 md/txt/json/jsonl | **non-blocking** (suggestion) |

## Phase 3: Company Policy (회사별 정책)

### musinsa
| 검증 항목 | 기준 | 분류 |
|---|---|---|
| 1-Pick 원칙 | `one_pick_item` 필드가 항상 1개 | **BLOCKING** |
| rejected_options | 최소 1개, 최대 3개 | **BLOCKING** |
| 다중 추천 | 2개 이상 추천 로직 없음 | **BLOCKING** |

### kakaopaysec
| 검증 항목 | 기준 | 분류 |
|---|---|---|
| 투자 권유 금지 | "권장", "안전한 투자", "ETF 분할 매수", "상품 안착" 표현 없음 | **BLOCKING** |
| 면책조항 | 금융투자 면책 문구 포함 | **BLOCKING** |
| FOMO 방어 | 패닉 입력 시 차분한 회복 응답 | **non-blocking** |

### samilpwc
| 검증 항목 | 기준 | 분류 |
|---|---|---|
| SOP 근거 | 근거 없이 결론 내리는 로직 없음 | **BLOCKING** |
| review_required | 불확실 시 `review_required=true` 전환 일관성 | **BLOCKING** |
| 비식별화 | 고객사/임원/금액 비식별 처리 | **BLOCKING** |

## Phase 4: Quality Gate (품질 관문)

| 검증 항목 | 기준 | 분류 |
|---|---|---|
| TODO 플레이스홀더 | 0개 | **BLOCKING** |
| 하드코딩된 시크릿 | 0개 | **BLOCKING** |
| 가짜 생성 로그 | script로 만든 fake 로그 없음 | **BLOCKING** |
| 출력 스키마 일관성 | SKILL ↔ README ↔ logs 간 일치 | **BLOCKING** |
| 토큰 노출 | GITHUB_TOKEN/GH_TOKEN 값 미포함 | **BLOCKING** |
| 데드 코드 | 사용되지 않는 가드레일/필드 | **non-blocking** |

## Phase 5: Verdict (판정)

### APPROVE
```markdown
## ✅ APPROVED

- **PR**: #{PR_NUMBER}
- **Commit**: {commit_hash}
- **Reviewer**: {INTEGRATION_CHAT_LABEL}
- **Phase Results**: 1/5 ✅ | 2/5 ✅ | 3/5 ✅ | 4/5 ✅
- **Non-blocking Suggestions**: {count}개
- **Merge Target**: integration/{COMPANY}
```

### CHANGES_REQUESTED
```markdown
## ❌ CHANGES REQUESTED

- **PR**: #{PR_NUMBER}
- **Reviewer**: {INTEGRATION_CHAT_LABEL}

### Blocking Issues
| # | Phase | File | Issue | Required Fix |
|---|---|---|---|---|
| 1 | {phase} | {file_path} | {description} | {specific fix} |

### Non-blocking Suggestions
| # | Phase | File | Suggestion |
|---|---|---|---|
```

# Conventional Comments 형식
리뷰 코멘트는 아래 형식을 사용한다:

```
blocking: {message}
→ merge 전 반드시 수정

suggestion (non-blocking): {message}
→ 다음 iteration에서 개선 권장

question: {message}
→ 의도 확인 필요
```

# Blocking vs Non-blocking 분류 기준

| 분류 | 조건 |
|---|---|
| **BLOCKING** | 계약 위반, 보안 경계 침범, 스키마 호환성 깨짐, 타 회사 오염 |
| **non-blocking** | 네이밍 개선, 로그 형식 보강, 토큰 최적화, 문구 다듬기 |

# 금지 사항 (DO NOT)
- **DO NOT** LGTM만으로 승인한다. Phase 1-4 결과를 명시한다.
- **DO NOT** Worker가 아닌 다른 integration agent의 담당 회사 PR을 리뷰한다.
- **DO NOT** 자기가 만든 PR을 자기가 승인한다.
- **DO NOT** CI가 실패한 PR을 승인한다.
- **DO NOT** BLOCKED_GIT 또는 BLOCKED_AUTH 라벨이 붙은 PR을 승인한다.
- **DO NOT** Blocking issue가 1개라도 있으면 APPROVE를 내린다.
- **DO NOT** 회사별 정책을 다른 회사 PR에 기계적으로 적용한다.

# Validation Checklist
- [ ] Phase 1: 파일 변경이 선언된 COMPANY 범위 이내
- [ ] Phase 2: plugin.json, SKILL.md, README.md 구조 준수
- [ ] Phase 3: 해당 회사 정책 위반 0건
- [ ] Phase 4: TODO/시크릿/가짜로그/스키마 불일치 0건
- [ ] Phase 5: Blocking 0건이면 APPROVE, 1건 이상이면 CHANGES_REQUESTED
