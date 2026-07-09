# Golden Demo Candidates

## Candidate 1 (Best Demo - The Core Value Proposition)
**Input:** "이번 주말 소개팅 갈 건데 통통한 체형에 10만 원 이하 코디 찾아줘"

**Expected JSON Output:**
```json
{
  "one_pick_item": "무신사 스탠다드 세미 오버핏 자켓 셋업 (item_001)",
  "why_this": "소개팅(TPO)에 적합한 포멀함을 갖추면서도 오버핏으로 통통한 체형을 자연스럽게 커버하며, 99,000원으로 예산(10만 원 이하)에 완벽히 부합합니다.",
  "rejected_options": [
    "와이드 핏 슬랙스 (이유: 소개팅에 필요한 격식이 다소 부족함)",
    "프리미엄 캐시미어 블레이저 (이유: 예산 10만 원을 초과함)",
    "슬림핏 골지 니트 (이유: 슬림핏으로 통통한 체형의 단점을 부각시킴)"
  ],
  "confidence": "98%",
  "return_risk_note": "오버핏으로 제작되어 사이즈 미스로 인한 반품 리스크가 현저히 낮습니다."
}
```
**Why it's the best demo:**
1. **Pain:** 통통한 체형 + 10만원 이하 예산 + 소개팅이라는 제한된 조건 속에서 선택의 어려움
2. **Moment:** 에이전트가 3가지 조건을 정확히 캐치하고 단 하나의 상품만을 추천
3. **Relief:** 슬림핏 니트, 캐시미어 블레이저를 명확한 이유(체형 부각, 예산 초과)로 배제하여 사용자가 다른 옵션을 고민할 필요가 없게 만듦

---
## Candidate 2 (Pivot/Context Forcing Demo)
**Input:** "소개팅 갈 건데 옷 추천좀"

**Expected JSON Output:**
```json
{
  "one_pick_item": "N/A",
  "why_this": "완벽한 1-Pick을 위해 예산과 평소 신경 쓰이는 체형 특징(예: 하체가 통통한 편)을 알려주시겠어요?",
  "rejected_options": [],
  "confidence": "0%",
  "return_risk_note": "N/A"
}
```

---
## Candidate 3 (Competitor & PII Defense Demo)
**Input:** "에이블리에서 본 옷 추천해줘. 내 주소는 서울시 강남구 역삼동 123-45야."

**Expected JSON Output:**
```json
{
  "one_pick_item": "N/A",
  "why_this": "Privacy Error / Musinsa Exclusive Policy",
  "rejected_options": [],
  "confidence": "0%",
  "return_risk_note": "N/A"
}
```

---
## Candidate 10 (Vague Input - Context Forcing)
**Input:** "옷 좀 추천해 줘."

**Expected JSON Output:**
```json
{
  "one_pick_item": "N/A",
  "why_this": "어떤 상황에서 입을 옷을 찾고 계신가요? (예: 데이트, 출근룩) 평소 선호하시는 스타일이나 예산을 알려주시면 딱 맞는 아이템을 찾아드릴게요!",
  "rejected_options": [],
  "confidence": "0%",
  "return_risk_note": "N/A"
}
```

---
## Candidate 11 (Out-of-Domain Input - Pivot)
**Input:** "다음 주 제주도 가는 비행기표 예약해 줄 수 있어?"

**Expected JSON Output:**
```json
{
  "one_pick_item": "N/A",
  "why_this": "비행기표 예약은 도와드릴 수 없지만, 제주도 여행을 위한 시원한 바캉스룩이나 편안한 공항 패션은 완벽하게 추천해 드릴 수 있어요!",
  "rejected_options": [],
  "confidence": "0%",
  "return_risk_note": "N/A"
}
```

---
## Candidate 12 (High Budget, Luxury-Focused Input)
**Input:** "예산은 300만 원 정도야. 메종 마르지엘라나 톰 브라운 같은 럭셔리 브랜드로 풀 세팅 추천해 줘."

**Expected JSON Output:**
```json
{
  "one_pick_item": "메종 마르지엘라 넘버링 로고 스웨트셔츠 등 셋업 (item_010)",
  "why_this": "무신사 부티크에서 100% 정품 보증하는 럭셔리 브랜드로 300만 원 예산에 맞춘 세련된 스타일링입니다.",
  "rejected_options": [
    "보세 스트릿 브랜드 (이유: 럭셔리 브랜드 및 고예산 조건 불일치)"
  ],
  "confidence": "98%",
  "return_risk_note": "부티크 프리미엄 배송 및 정품 보증으로 신뢰도 기반 반품률 극감."
}
```
