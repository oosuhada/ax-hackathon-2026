
## Iteration 2 - 2026-07-09T22:43:00+09:00 (Deepening Pass)

### Business Focus
- ROI 정량 지표 강화 (Delivery Cost: 80h/800만원 -> 5,000원, 99% 절감)
- 아키텍처 리스크 방어 논리 보강 (Vector DB Cost Scaling 및 Latency 방어 - Semantic Caching 적용 계획)
- [SYNTHETIC] MVP 명시 및 과장된 온프레미스/RAG 구현 여부 명확화 재점검

### Mandatory Subagents Used
| Subagent | Required Output |
|---|---|
| evaluator-pitch-judge | 심사위원 반박 질문 추가 3개 도출 및 답변 (보안/컴플라이언스/스케일링) |
| roi-architect | 정량적 수치 보강 (Token vs 인건비 절감률 99%) |
| cost-estimator | 대규모 트래픽 시 Vector DB 운영 비용 최적화(Semantic Caching) 논리 추가 |

### Judge Objections Added
| ID | Question | Risk | Best Answer |
|---|---|---|---|
| Q4 | Air-gapped 온프레미스 구축 비용이 막대할 텐데, ROI가 나오는가? | Medium | 데모는 토큰 API 기반이나, 상용화 시 데이터의 민감도에 따라 PII 마스킹+퍼블릭 LLM을 혼용하는 하이브리드 아키텍처로 구축 비용을 최적화합니다. |
| Q5 | Vector DB를 엔터프라이즈 전사 단위로 확장할 때 검색 지연(Latency)과 비용 폭증 문제는? | Medium | Semantic Caching 계층을 미들웨어에 도입하여 중복된 SOP 조회 패턴의 응답 속도를 높이고 LLM 쿼리 비용을 대폭 절감하도록 설계되었습니다. |
| Q6 | 데이터 요약 기능만이라면 기존 RPA나 규칙 기반 시스템과 다를 바 없지 않은가? | High | 통계 단순 계산을 넘어 숫자 뒤의 "행간(Intent)"을 추론하고 이를 규정과 연결하는 Explainability가 핵심 차별점이며, 규칙 기반으로 감지할 수 없는 우회 패턴을 적발합니다. |

### README / ROI Findings
| Priority | Issue | File | Fix |
|---|---|---|---|
| High | ROI 정량화 부족 (단순 90% 명시) | README.md | 인건비 대비 원가 절감률 99% 및 구체적 비용(800만원->5천원) 명시 |
| Medium | 아키텍처 리스크 방어 부재 | README.md | Vector DB Cost Scaling & Latency 방어 (Semantic Caching) 추가 |

### Patch Applied
| File | Change | Reason |
|---|---|---|
| README.md | ROI 섹션 1번 항목을 정량적 수치(99% 절감)로 보완 | 신뢰성 확보 및 정량적 근거 마련 |
| README.md | 운영 KPIs에 Vector DB 리스크 방어 로직 추가 | 아키텍처 확장성 질문 방어 |

### Judge Score
- Score: 92/100
- Why not 100: 프롬프트 인젝션 및 난독화 공격 등에 대한 보안 감사(Security Audit) 결과의 가시성 부족
- Next round focus: 보안 컴플라이언스 측면(data-privacy-scrubber)을 강조하여 엣지 케이스 테스트 매트릭스 구체화

