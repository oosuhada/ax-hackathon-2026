## 검증 결과
### V1 자기 검증
- [x] V1-1: 읽은 파일 목록 (`SKILL.md`, `demo_transcript.md`, `Dummy_Business_Data.json`, `Dummy_SOP_Snippets.json`, `README.md`)
- [x] V1-2: 스키마 정합성 검증 (SKILL.md의 JSON Schema와 demo_transcript.md의 실제 출력물 대조)
- [x] V1-3: 인젝션/보안 관련 출력 여부 확인 (PII 마스킹 및 review_required 처리 정상 작동 확인)
- [x] V1-4: 엣지 케이스 시뮬레이션 (C-Level이 모바일 기기나 좁은 대시보드 화면에서 해당 JSON을 바로 읽는 경우의 인지 부하 시뮬레이션)
- [x] V1-5: scope 확인 (SamilPwC 플러그인의 End-to-End trace UX 포맷에 집중함)

### V2 다각도 검증  
- [x] V2-1: blast-radius (UX 개선안이 기존 백엔드의 JSON Output Schema 파괴를 유발하지 않는지 확인)
- [x] V2-3: contract 확인 (`SKILL.md` 명세와 `demo_transcript.md` 출력 대조 중 `mapping_rationale` 누락 발견)
- [x] V2-6: 명확성 (경영진 대상 리포트로서의 건조한 톤앤매너와 시각적 가독성 동시 만족 여부 검토)
발견 이슈: 3건 / 제안 완료: 3건 / 잔여: 0건

---

## 변경 요약 및 분석 리포트 (SamilPwC Plugin UX QA)
**목표**: "raw financial input -> SOP rule -> final Dashboard output"으로 이어지는 End-to-End Trace 과정에서의 3가지 UX 마찰(Friction) 발견 및 UI 파괴 없는 가독성 개선안 도출.

### Friction 1. 증거 추적의 단절 (Disconnected Evidence Tracing)
- **Fact**: 현재 `evidence` 필드는 "Unit_B R&D 비용이 총 비용의 80%를 초과(150k+600k)"처럼 단순 텍스트로 요약되어 출력됩니다.
- **UX 마찰**: 의사결정권자(C-Level)가 이 수치를 직접 감사(Audit)하고자 할 때, 입력된 방대한 `Dummy_Business_Data.json`에서 해당 숫자가 정확히 어디에 위치해 있는지 수동으로 찾아야 하는 인지적 마찰이 발생합니다.
- **해결안 (UI Readable Trace)**: 백엔드의 JSON 스키마를 변경하지 않고, 텍스트 내에 JSONPath 또는 명시적 노드 참조를 대괄호로 삽입합니다 (예: `[cost_allocations.Unit_B.rnd_cost: 600,000]`). 프론트엔드 대시보드에서는 정규식을 통해 이 괄호를 **"Clickable Data Badge"**로 렌더링하고, 클릭 시 화면 분할(Split View)된 원본 데이터 뷰어에서 해당 라인을 하이라이팅 처리하면 레이턴시 지연 없이 완벽한 추적성을 제공할 수 있습니다.

### Friction 2. `mapping_rationale`의 누락에 따른 논리적 단절 (Broken Explainability Trace)
- **Fact**: `SKILL.md`의 Output Schema에는 수치와 SOP 사이의 인과관계를 설명하는 `mapping_rationale` 필드가 필수(Required)로 명시되어 있으나, `demo_transcript.md`의 실제 출력 결과들에는 이 필드가 누락되어 있습니다.
- **UX 마찰**: '데이터 증거'에서 '권고안'으로 점프하는 느낌을 주어 AI의 논리적 사고 과정(Explainability)에 대한 신뢰를 떨어뜨립니다. 
- **해결안 (Progressive Disclosure UI)**: `mapping_rationale` 출력을 강제 복구하되, 대시보드 UI에서는 텍스트 폭탄이 되지 않도록 **"Progressive Disclosure(점진적 노출) Stepper"** 방식을 사용합니다. 
  - 1단계: `Evidence` (발견된 사실)
  - 2단계: `SOP Reference` (적용 규정)
  - 3단계: `↳ Rationale` (접기/펴기 아코디언 토글로 숨김 처리하여 원할 때만 논리 전개 확인)
  - 4단계: `Recommended Action` (최종 권고)

### Friction 3. 평면적 텍스트로 인한 SOP 컨텍스트 상실 (Flat-Text SOP Reference)
- **Fact**: 출력된 `sop_reference`는 `"[SOP-FIN-042] R&D 비용 배분이 50%를 초과할 경우..."`와 같은 긴 평문입니다. 원본 `Dummy_SOP_Snippets.json`에 존재하는 `category` (예: "Cost Allocation") 정보가 최종 출력에서 증발합니다.
- **UX 마찰**: 규정의 맥락(Category)을 한눈에 파악하기 어렵고, 긴 줄글이 대시보드의 시각적 여백을 훼손합니다.
- **해결안 (Hover & Fetch Tooltip)**: 
  - 텍스트 렌더링 시 대시보드에서 `[SOP-FIN-042]` 아이디 부분만 인식하여 시각적인 **"Tag/Pill"** 형태로 압축 렌더링합니다.
  - 사용자가 마우스를 올릴 때(Hover), 비동기(Asynchronous) 방식이 아닌 로컬에 캐싱된 SOP 데이터를 즉시 불러와 툴팁으로 `Category`와 전체 원문을 띄워줍니다. 이는 초기 렌더링 레이턴시(Latency)를 최적화하면서도 맥락 정보를 보존하는 방식입니다.

### 📋 Record (기록)
- **계약 대조**: `SKILL.md`의 Output Schema를 준수하며 UI 레이어의 렌더링 전략만 수정하도록 제안함. (`mapping_rationale` 누락 버그 리포트 포함)
- **잔여 리스크**: 프론트엔드 대시보드가 마크다운이나 뱃지 형태의 정규식 파싱을 지원해야 하므로, UI 컴포넌트(React/Vue 등) 단의 추가 구현 공수가 필요함.
