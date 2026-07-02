# AX 해커톤 예선 제출 스켈레톤 — Musinsa Review-to-Action Plugin

## Plugin concept

**Plugin name:** `musinsa-review-to-action`

무신사 스타일의 패션 커머스/마켓플레이스 환경에서 상품 리뷰, Q&A, 반품 사유 같은 고객 피드백을 판매자·MD·상품기획자·CS 담당자가 실행할 수 있는 액션으로 바꾸는 Codex 플러그인입니다.

핵심 차별점은 “소비자용 리뷰 요약”이 아니라 **판매자/MD용 액션 변환**입니다.

---

## 1. 무엇을, 누가, 어떤 상황에서 쓰나요?

이 플러그인은 패션 커머스 입점 브랜드, MD, 상품기획자, CS 운영자, 상세페이지 담당자가 사용합니다. 사용자는 상품 리뷰 CSV, Q&A, 반품 사유, 상품 설명을 입력하고, Codex는 반복 불만, 사이즈/핏 이슈, 색상·소재·상세페이지 정보 부족, CS 자동화 후보, 마케팅 카피 기회 등을 분석해 실행 가능한 개선안을 생성합니다.

---

## 2. 왜 이 문제를 선택했나요?

패션 커머스에서 리뷰는 구매 전환과 신뢰에 중요한 역할을 합니다. 하지만 리뷰를 단순히 요약하는 것만으로는 판매자가 실제로 무엇을 바꿔야 하는지 알기 어렵습니다. 특히 사이즈, 핏, 색상, 소재, 배송, 상세페이지 정보 부족 같은 피드백은 제품 개선, 상세페이지 수정, FAQ, CS 매크로, 마케팅 카피로 전환되어야 실질적 가치가 생깁니다.

최종 제출 전 `src/skills/musinsa-review-to-action/references/evidence_sources.md`에 공개자료 기반 근거를 채워야 합니다.

---

## 3. 플러그인은 어떻게 작동하나요?

1. 사용자가 상품 리뷰/상품 컨텍스트를 제공합니다.
2. helper script가 리뷰 테마별 기본 분류와 카운트를 생성합니다.
3. Codex skill이 결과를 검토하여 seller-facing action으로 변환합니다.
4. 최종 산출물은 다음과 같습니다.
   - Review-to-Action Matrix
   - Detail Page Fixes
   - CS FAQ and Response Macros
   - Product Improvement Ideas
   - Marketing Copy Opportunities
   - Validation Checklist

샘플 실행:

```bash
python src/scripts/analyze_review_feedback.py \
  --reviews src/sample_inputs/product_reviews.csv \
  --context src/sample_inputs/product_context.md \
  --out src/sample_outputs

python src/scripts/validate_submission_structure.py
```

---

## 4. AI를 어떻게 활용했나요?

AI는 문제 구조화, 공개자료 조사 방향 설정, Codex plugin/skill 설계, 리뷰 테마 분류 프레임워크 작성, 샘플 데이터 생성, 산출물 템플릿 작성, 검증 체크리스트 구성에 활용합니다.

주의: 실제 제출 시 이 문항은 `logs/` 폴더에 포함된 원본 AI 작업 로그와 반드시 일치해야 합니다.

---

## 5. 어떻게 검증했나요?

검증은 다음 기준으로 수행합니다.

- 제출 구조 검증: `plugin.json`, `SKILL.md`, `README.md`, `logs/` 존재 여부
- 샘플 리뷰 입력에 대한 출력 생성 여부
- 각 추천 액션이 실제 리뷰 evidence와 연결되는지
- 판매자/MD가 실행할 수 있는 수준의 액션인지
- 허위 sales/conversion/return metric을 생성하지 않았는지
- 공개자료 기반 문제정의와 플러그인 기능이 일치하는지

---

## Final submission reminder

- `logs/README_REPLACE_WITH_RAW_LOGS.md`는 placeholder입니다. 제출 전 원본 AI 작업 로그로 교체하세요.
- `evidence_sources.md`의 TODO를 실제 공개자료 URL과 근거로 채우세요.
- 여러 기업을 제출하는 경우, 기업별로 별도의 zip을 제출해야 합니다.
