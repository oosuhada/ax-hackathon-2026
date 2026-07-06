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
## Candidate 7 (Mixed Queries & Steering Demo)
**Input:** "나 내일 제주도 가는데 입을 옷 추천해줘. 아, 그리고 제주도 맛집도 몇 개만 알려줄래?"

**Expected JSON Output:**
```json
{
  "one_pick_item": "무신사 스탠다드 라이트웨이트 나일론 파라슈트 팬츠 (item_007)",
  "why_this": "제주도 방풍 파라슈트 팬츠 최적. 맛집 정보는 미제공.",
  "rejected_options": [
    "와이드데님(무거움)",
    "리넨셔츠(바람취약)"
  ],
  "confidence": "95%",
  "return_risk_note": "허리 밴딩 핏 조절 가능. 사이즈 미스 리스크 최소화."
}
```

---
## Candidate 8 (Extreme Weather Constraints Demo)
**Input:** "영하 15도 한파에 야외에서 8시간 동안 현장 작업해야 하는데, 두껍지 않으면서도 얼어 죽지 않을 아우터 하나만 골라줘."

**Expected JSON Output:**
```json
{
  "one_pick_item": "내셔널지오그래픽 타루가 고어텍스 발열 패딩 (item_008)",
  "why_this": "영하 15도 야외, 얇은 고어텍스 발열 안감.",
  "rejected_options": [
    "헤비롱패딩(활동저해)",
    "경량패딩레이어링(보온부족)"
  ],
  "confidence": "99%",
  "return_risk_note": "내구성 강한 소재로 마모 불만족 리스크 낮음."
}
```

---
## Candidate 9 (Complex Body Type Combinations Demo)
**Input:** "제가 어깨는 엄청 넓고 팔도 긴 편인데, 허리랑 하체는 많이 말라서 바지가 자꾸 흘러내려요. 이번 주말 데이트 때 입을 상하의 코디 딱 하나만 추천해주세요."

**Expected JSON Output:**
```json
{
  "one_pick_item": "수아레 래글런 하프 집업 니트 & 와이드 밴딩 핀턱 슬랙스 셋업 (item_009)",
  "why_this": "어깨 커버 래글런, 마른 하체 보완 핀턱 밴딩 와이드 핏.",
  "rejected_options": [
    "드롭숄더셔츠(상체부각)",
    "슬림슬랙스(불균형심화)"
  ],
  "confidence": "96%",
  "return_risk_note": "체형 단점 보완 핏. 반품 리스크 극히 낮음."
}
```
