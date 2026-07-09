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
  "return_risk_note": "오버핏으로 제작되어 사이즈 미스로 인한 반품 리스크가 평균 30% 감소합니다. [ROI: 반품 건당 3천원 절감]"
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
## Candidate 4 (Gift Target & Specific Body Type - Normal Case)
**Input:** "남자친구 선물로 줄 건데, 어깨가 넓은 편이고 예산은 15만원이야. 데일리로 입기 좋은 아우터 추천해줘."

**Expected JSON Output:**
```json
{
  "one_pick_item": "오버핏 비건 레더 자켓 (item_006)",
  "why_this": "어깨 커버 오버핏, 데일리 TPO, 15만원 이하 예산 부합.",
  "rejected_options": [
    "슬림라이더(불편함)",
    "무스탕(예산초과)",
    "패턴블루종(호불호)"
  ],
  "confidence": "95%",
  "return_risk_note": "오버핏으로 사이즈 미스 리스크 감소. [ROI: 반품 건당 3천원 절감]"
}
```

---
## Candidate 5 (Unrealistic Budget - Edge Case)
**Input:** "겨울 소개팅용 패딩을 5천원 이하로 추천해줘. 마른 체형이야."

**Expected JSON Output:**
```json
{
  "one_pick_item": "N/A",
  "why_this": "예산 5천원 이하 패딩 추천 불가. 예산 상향 필요.",
  "rejected_options": [],
  "confidence": "0%",
  "return_risk_note": "N/A"
}
```

---
## Candidate 6 (Partial Constraints Provided - Ambiguous Case)
**Input:** "이번 주말 결혼식 하객으로 갈 건데, 예산은 15만원이야. 어울리는 원피스 찾아줘."

**Expected JSON Output:**
```json
{
  "one_pick_item": "N/A",
  "why_this": "하객룩, 예산 15만원 확인. 완벽 추천을 위해 체형 특징 정보 추가 요청.",
  "rejected_options": [],
  "confidence": "0%",
  "return_risk_note": "N/A"
}
```
