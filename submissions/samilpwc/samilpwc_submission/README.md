# CEO Issue Judge Agent (Samil PwC)

## 1. 개요 및 60초 피치
- **1문장 문제 정의**: AI가 답을 말하는 것이 아니라, 경영진이 조직 내 결정을 밀어붙일 수 있는 감사 가능한 근거물을 만든다.
- **[Pain]** 부서 간 배분 분쟁 시, McKinsey 조사에 따르면 72%의 고위 경영진이 **나쁜 전략적 결정이 좋은 결정만큼이나 빈번**하다고 응답했습니다. `[ASSUMPTION based on commonly cited McKinsey survey — 원문 URL 접근 불가로 직접 인용 대신 일반적으로 알려진 통계 수치로 표기]`
- **[Moment]** 단순 '텍스트 요약 AI'는 내부 사내 정치를 뚫고 총대를 메어주지 않습니다.
- **[Relief]** 본 에이전트는 합성 재무 데이터를 주입하면 수 초 내에 데이터 이상 징후를 자동으로 플래그합니다. (실제 응답 속도는 LLM 추론 시간에 따라 변동) **사내 규정(SOP)을 인용한 객관적 권고 리포트**를 출력합니다.
- **[Trust]** 모순이나 SOP 부재 시 AI는 자의적 추측(Hallucination)을 최소화하도록 설계되었으며, 선례가 없는 엣지 케이스는 즉각 인간 컨설턴트의 검토(Human-in-the-Loop)로 이관하여 높은 수준의 감사 추적성과 객관성을 유지하도록 설계되었습니다.

> ℹ️ *엔터프라이즈 환경 도입을 위한 시스템 아키텍처 및 Simulated RAG 데모 환경의 기술적 스펙은 하단의 '5. Known Limitations & Roadmap' 섹션에서 확인할 수 있습니다.*

## 2. 20-Round Stress Test (방어 매트릭스)
본 에이전트는 제출 전 멀티에이전트를 활용한 20라운드 무한 검증 루프를 거치며 60여 개의 악성/엣지 케이스를 모두 방어해 냈습니다. (`logs/` 디렉토리 참조)
- **PII 우회 및 인젝션 차단**: Base64 인코딩, 협박성 프롬프트, 시스템 프롬프트 노출 등 전면 방어 완료.
- **Hallucination-Resistant**: SOP 조항이 없거나 상충되는 데이터(예: 매출/비용 동시 500% 급증) 입력 시 `review_required=true` 락인 전환 설계 적용.

## 3. 핵심 5문항 답변
### Q1. 무엇을, 누가, 어떤 상황에서 쓰나요?
- **누가**: C-레벨 경영진 및 의사결정권자.
- **상황**: 원가 할당, 매출 분쟁 등 이해관계가 얽힌 교착 상태.
- **무엇을**: 내부 사내 정치와 책임 회피 병목을 돌파하기 위한 '객관적 SOP 기반 판독 리포트 생성기'.

### Q2. 왜 이 문제를 선택했나요?
- **[FACT]** 데이터 요약기가 아닌, **결정의 정당성을 뒷받침할 외부 권위(SOP 규정)와 책임 분산 장치**가 B2B 엔터프라이즈 컨설팅 AI의 진정한 핵심 가치이기 때문입니다.

### Q3. 플러그인은 어떻게 작동하나요?
1. 비식별화된 `[SYNTHETIC]` 영업/재무 데이터 입력.
2. 부서 간 자원 편중 등 이상 패턴 탐지.
3. `Dummy_SOP_Snippets`을 매핑하는 Simulated RAG 실행.
4. AI의 추측을 배제하고 SOP 근거를 인용한 리포트 JSON 출력.

### Q4. AI를 어떻게 활용했나요?
- 통계 단순 계산을 넘어, 숫자 뒤 '행간'을 추론하고 이를 규정(SOP)과 연결하는 **Explainability** 엔진.
- 확실한 SOP 근거 부재 시 **Human Review 강제 이관** 구조 채택.

### Q5. 어떻게 검증했나요?
- `logs/iteration_report.md`에 기록된 20라운드의 집요한 공격(프롬프트 인젝션, 책임 전가 유도, PII 주입, 스키마 파괴 등 60종의 테스트 매트릭스)을 모두 패스(PASS)했습니다.

## 4. 컨설팅 ROI (Business Impact)
주니어 컨설턴트의 데이터 대조 공수(건당 80h → 8h) 단축을 가정한 `[ASSUMPTION]` 기반 핵심 5축 모델입니다.

| ROI 축 | 상세 내용 | 비고 |
|--------|-----------|------|
| **1. 데이터 대조 공수 절감** | 리서치 공수 90% 절감 (건당 80h → 8h, 시간당 단가 10만 원 기준 건당 720만 원 절약) | **[ASSUMPTION]** |
| **2. 리스크 조기 탐지** | 전분기 대비 30% 이상 이상 수치 자동 플래그 — 이상 징후를 수 초 내에 탐지하여 인간 분석가 부담 경감 | **[DESIGN_GOAL]** |
| **3. 감사 추적성 확보** | `mapping_rationale`을 통한 명시적 SOP 매핑 근거 자동 기록으로 감사 대응 속도 대폭 향상 | **[FACT]** |
| **4. API 비용 효율성** | 단일 세션 기준 LLM 토큰 소비량 최적화. 실측 시 건당 비용 추적 가능 | **[ASSUMPTION]** |
| **5. 의사결정 일관성** | 동일 이슈 → 동일 SOP 적용으로 인간 컨설턴트의 피로도·주관 편향 없이 균일한 판단 품질 유지 | **[DESIGN_GOAL]** |

## 7. 운영(Operational) KPIs
- **정상 재승인 비율 (False Positive Escalation Rate)**: 과도한 Compliance-First 가드레일로 인해 무해한 데이터가 인간 검토(Human-in-the-Loop)로 이관되어 병목을 일으키지 않도록, 이관 건수 중 "수정 없이 단순 통과"된 건의 비율을 모니터링하여 방어 민감도를 지속 튜닝합니다.
  - *Dashboard UI/UX 제안*: Dual-Axis 차트를 통해 일일 검토 이관량(Bar)과 정상 재승인 비율(Line)을 시각화하고, 특정 임계치(Threshold) 초과 시 원인이 되는 룰을 식별하는 **Escalation Efficiency & Sensitivity Tracker** 위젯 구현을 권고합니다.
- **Anomaly Score Threshold Monitoring**: 여러 미세한 방어 룰(Zero-width 문자, 오타 등)이 개별 임계치를 넘지 않더라도, 누적된 기형적 패턴이 특정 점수(Anomaly Score)를 초과하면 자동으로 Human-in-the-loop 검토를 강제하는 구조를 도입합니다.
- **Threat Intelligence Map**: 악의적인 데이터 주입(Injection, DoW 등) 시도를 실시간으로 추적하여, 경영진이 시스템이 방어해낸 엣지 케이스 공격들을 시각적으로 체감할 수 있는 **Threat Defense Map** 위젯을 추가합니다.
- **Strict JSON Schema Validator Middleware**: 애플리케이션 레벨(Rust/Go)에서 LLM에 도달하기 전에 초고속으로 Cyclic JSON 및 스키마 변조를 1차 차단하는 미들웨어 아키텍처를 도입하여 AI 서버 부하를 최소화합니다.
- **Human-AI Collaboration Protocol**: AI의 판정을 인간 전문가가 기각(Override)할 경우, 해당 사유를 반드시 시스템에 표준화된 폼으로 기록하게 하여 향후 AI 모델 미세조정(Fine-tuning) 데이터로 역환류시키는 협업 프로토콜을 수립 중입니다.
- **Guardrail Latency Monitoring**: 극단적 엣지 케이스를 스캔하는 겹겹의 방어 로직으로 인해 처리 시간이 증가(UX 저하)하지 않도록, 파이프라인의 P95 응답 시간(Response Time)을 지속 추적하는 지표를 도입합니다.

## 5. Known Limitations
- **Compliance-First**: 민감 정보 감지 시 마스킹 처리가 아닌 전면 분석 중단을 채택하는 극단적 보수성을 띕니다.
- **[WARN] 시스템 프롬프트 우회 우려**: 20라운드 방어에도 불구, 일부 초거대 LLM의 최신 탈옥 기법에 취약할 여지가 있습니다.
- **[WARN] Simulated RAG**: 온프레미스 Vector DB 인프라는 데모에 미포함되었습니다.
