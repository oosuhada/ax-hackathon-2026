# GitHub Token Setup For 4-PC Antigravity Run

각 PC에서 한 번만 실행한다.

```bash
cd "/path/to/AX Hackerton"
cp .env.example .env.local
chmod 600 .env.local
open -e .env.local
```

`.env.local`에 GitHub token을 붙여넣은 뒤 저장한다. 토큰 값은 절대 채팅창, 로그, README, 커밋 메시지에 쓰지 않는다.

검증:

```bash
cd "/path/to/AX Hackerton"
set -a
source .env.local
set +a

test -n "$GITHUB_TOKEN" && echo "GITHUB_TOKEN is set"
test -n "$GH_TOKEN" && echo "GH_TOKEN is set"
gh auth status || printf '%s' "$GH_TOKEN" | gh auth login --with-token
gh auth setup-git
```

주의:
- `echo "$GITHUB_TOKEN"` 실행 금지
- `.env.local` 커밋 금지
- 제출용 `logs/` 안에 토큰 값 기록 금지
- 에이전트가 인증 실패를 만나면 토큰 값을 출력하지 말고 `BLOCKED_AUTH`만 기록

