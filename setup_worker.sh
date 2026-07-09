#!/bin/bash
# ──────────────────────────────────────────────
# AX 해커톤 2026 — PC 초기 세팅 스크립트
# 사용법: git clone 후 ./setup_worker.sh 실행
# ──────────────────────────────────────────────

set -euo pipefail

echo "🔧 AX 해커톤 워커 PC 세팅 시작..."

# 1. Git 사용자 정보 고정
git config user.name "oosuhada"
git config user.email "woosu91@gmail.com"
echo "✅ Git user: oosuhada <woosu91@gmail.com>"

# 2. .env.local 생성 (없는 경우만)
if [ ! -f .env.local ]; then
  cp .env.example .env.local
  chmod 600 .env.local
  echo "📝 .env.local 생성 완료. 토큰을 입력해주세요."
  echo ""
  echo "   다음 명령어로 편집:"
  echo "   nano .env.local"
  echo ""
else
  echo "✅ .env.local 이미 존재"
fi

# 3. GitHub CLI 인증 테스트
echo ""
echo "🔐 GitHub 인증 테스트 중..."
if [ -f .env.local ]; then
  set -a; source .env.local; set +a
  
  if [ -z "${GITHUB_TOKEN:-}" ] || [ "$GITHUB_TOKEN" = "paste_your_github_token_here" ]; then
    echo "⚠️  .env.local에 실제 GitHub 토큰을 입력해주세요."
    echo "   nano .env.local 로 편집 후 다시 실행하세요."
    exit 1
  fi
  
  # gh CLI 인증
  printf '%s' "$GH_TOKEN" | gh auth login --with-token 2>/dev/null && \
    echo "✅ GitHub CLI 인증 성공" || \
    echo "⚠️  gh CLI 인증 실패. gh가 설치되어 있는지 확인하세요."
  
  # git push/pull 인증 위임
  gh auth setup-git 2>/dev/null && \
    echo "✅ Git 인증을 GitHub CLI에 위임 완료" || true
fi

# 4. 레포 접근 확인
echo ""
echo "📡 레포 접근 테스트..."
gh repo view oosuhada/ax-hackathon-2026 --json name,visibility 2>/dev/null && \
  echo "✅ 레포 접근 정상" || \
  echo "⚠️  레포 접근 실패. 토큰 권한을 확인하세요."

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "🎉 세팅 완료!"
echo ""
echo "다음 단계:"
echo "1. .env.local에 토큰이 입력되어 있는지 확인"
echo "2. docs/antigravity_16_chat_parallel_runbook_v2.md 파일을 열기"
echo "3. 이 PC에 해당하는 프롬프트를 복사"
echo "4. AI 채팅창에 붙여넣기 & Enter"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
