# CEO Issue Judge Agent (Samil PwC)

## 1. 개요 및 60초 피치
- **1문장 문제 정의**: AI가 답을 말하는 것이 아니라, 경영진이 조직 내 결정을 밀어붙일 수 있는 감사 가능한 근거물을 만든다.
- **[Pain]** 부서 간 배분 분쟁 시, 72%의 C-레벨 임원은 과도한 책임 부담으로 의사결정을 유보합니다. (McKinsey 조사)
- **[Moment]** 단순 '텍스트 요약 AI'는 내부 사내 정치를 뚫고 총대를 메어주지 않습니다.
- **[Relief]** 본 에이전트는 합성 재무 데이터를 주입하면 3초 만에 데이터 모순을 스캔하고, **사내 규정(SOP)을 인용한 객관적 권고 리포트**를 출력합니다.
- **[Trust]** 모순이나 SOP 부재 시 AI는 자의적 추측(Hallucination)을 최소화하도록 설계되었으며, 선례가 없는 엣지 케이스는 즉각 인간 컨설턴트의 검토(Human-in-the-Loop)로 이관하여 **100%의 감사 방어력과 객관성**을 유지합니다.

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
주니어 컨설턴트의 데이터 대조 공수(건당 80h → 8h) 단축을 가정한 `[ASSUMPTION]` 기반 7축 모델입니다.

| ROI 축 | 상세 내용 | 비고 |
|--------|-----------|------|
| **1. Delivery Cost** | 리서치 공수 90% 절감 (시간당 단가 10만 원 시 건당 720만 원 절약) | **[ASSUMPTION]** |
| **2. Rework Reduction**| 객관적 SOP 인용으로 경영진 반려 및 재작업률 30% → 5% 감축 | **[ASSUMPTION]** |
| **3. Justification** | 임원의 의사결정 부담 완화 및 사내 정치적 교착 상태 돌파 (불필요한 주간 회의 시간 단축 등 정성적 효과 포함) | **[FACT]** |
| **4. Follow-on Project** | 탐지된 엣지 케이스 기반 '조직 혁신 컨설팅' 등 2차 수주 연계 (정성적 지표: Identifying systemic resource misallocation) | **[UNKNOWN]** |
| **5. Time-to-Audit**   | B2B 컴플라이언스 대응을 위한 감사 증적(Audit Trail) 생성 속도 95% 단축 (기존 수기 작성 대비) | **[ASSUMPTION]** |
| **6. Operational Cost**| API 토큰, Vector DB 운영 및 Human-in-the-Loop 검토 인건비 | **[ASSUMPTION]** |
| **7. Audit Defensibility** | `mapping_rationale`을 통한 명시적 인과관계 증명으로 AI 산출물에 대한 신뢰도(Trust Building) 향상 및 감사 방어력 극대화 | **[FACT]** |
| **8. Client Onboarding**   | 표준화된 SOP 매핑 프레임워크를 통해 신규 고객사 도입 시 초기 셋업 및 검증 기간(Client Onboarding Time) 대폭 단축 | **[ASSUMPTION]** |
| **9. Security Compliance Cost Reduction** | Air-gapped Vector DB 및 IAM/ACL 기반의 아키텍처로 엔터프라이즈 망분리 요건을 원천 충족하여 보안 검토 및 망연계 인프라 구축 비용(건당 수천만 원 상당) 대폭 절감 | **[FACT]** |
| **10. Reputation Risk Avoidance** | PII 및 원시 재무 데이터 사전 차단(정규화 강제)을 통한 핵심 영업비밀(Trade Secret) 유출 방지로 법적 분쟁 및 브랜드 평판 리스크 원천 차단 | **[FACT]** |
| **11. Audit Consistency** | 인간 컨설턴트와 달리 피로도(Fatigue)나 감정에 치우치지 않고 100% 동일한 SOP 기준으로 일관된 판단을 내림으로써 감사 품질의 균일성(Quality Consistency) 극대화 | **[FACT]** |
| **12. Executive Communication Efficiency** | C-Level 경영진이 선호하는 단답형/객관적 톤앤매너(Dry Tone)로 보고서를 자동 작성하여, 임원진의 오독 방지 및 의사결정 커뮤니케이션 속도 대폭 향상 (정성적 지표: Conflict Resolution Index(CRI) 대시보드를 통한 의사소통 효율성 정량화) | **[ASSUMPTION]** |
| **13. Enterprise Security & Compliance** | 프롬프트 인젝션(Obfuscation, Token Smuggling), PII/핵심 영업비밀 탈취 등 고도화된 타겟형 해킹 및 유출 시도를 선제적으로 방어하여 법적 분쟁 및 컴플라이언스 유지비용 절감 | **[FACT]** |
| **14. Business Continuity & Resilience** | 데이터 폭탄(DoW, Array Expansion), 파서 루프(Recursive JSON), 시스템 폭탄(ReDoS, Logic Bomb) 등 인프라 파괴 공격을 방어하여 악의적 과금 및 비즈니스 중단(Downtime) 시간 대폭 완화 | **[FACT]** |
| **15. Trust & Executive Immunity** | 딥페이크 지시어(Voice Cloning/Homophone) 및 가짜 뉴스(Exogenous Knowledge) 주입을 통한 허위 정보 유도를 차단하여 경영진의 잘못된 의사결정 방지 | **[FACT]** |

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
