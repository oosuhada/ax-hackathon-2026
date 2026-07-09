# 무신사 합성 데이터 스펙 (Synthetic Data Specification)

## 1. 개요
- **목적**: 무신사 1-Pick 플러그인(`one-pick-decision-agent`)이 기업 내부의 실제 상품 데이터베이스에 접근하지 않고도 작동할 수 있도록 데모용 가상 카탈로그 스키마를 정의합니다.
- **라벨링**: 이 문서와 연관된 JSON 데이터는 모두 `[SYNTHETIC]` 데이터입니다.

## 2. 파일 위치
- `submissions/musinsa/submission/src/data/Dummy_Product_Data.json`

## 3. 스키마와 ROI 지표의 연결 구조

합성 데이터의 각 필드는 단순한 쇼핑몰 필드가 아닌, 플러그인이 기업에 가져다줄 **비즈니스 임팩트(ROI)**를 증명하기 위해 전략적으로 설계되었습니다.

| 필드명 | 설명 | ROI 연결 논리 (Business Impact) |
|---|---|---|
| `item_id` | 가상 상품 ID | - |
| `name` | 상품명 | - |
| `price` | 가격 | **결정 시간 단축**: 유저 예산 내 필터링을 통해 이탈 방지 및 CVR 상승 |
| `fit_cover_type` | 해당 상품이 커버할 수 있는 체형 단점 (예: `chubby`, `short`) | **반품률 감소 (Return Rate Drop)**: 정밀한 단점 커버 매칭으로 '핏 불만족'으로 인한 반품률(약 2%p) 최소화 |
| `tpo_tags` | 상황별 태그 (`blind_date`, `wedding`, `casual`) | **구매 전환율 (CVR)**: 맥락에 완벽히 부합하는 1-Pick을 제시하여 망설임 없이 결제 유도 |
| `inventory_status` | 재고 상태 (`overstocked`, `normal`) | **장기 재고 완화 (Inventory Clearance)**: 동일 조건 시 `overstocked` 상품을 1-Pick으로 가중치 부여하여 악성 재고 소진율 극대화 |

## 4. 활용 방안
이 데이터 스펙은 `one-pick-decision-agent`의 프롬프트 내에 Few-shot 예시로 제공되거나, 플러그인이 실제 파일(`Dummy_Product_Data.json`)을 읽어들여 1-Pick 필터링 알고리즘을 시연하는 데 사용됩니다.

---
```yaml
handoff:
  company: 무신사
  phase: Architecture & Synthetic Data
  primary_use_case: Synthetic Data Specification
  files_created_or_modified: docs/musinsa_synthetic_data_spec.md
  required_inputs: N/A
  output_schema: N/A
  validation_command: N/A
  unresolved_risks: None
  next_skill: synthetic-data-engineer (data creation)
```
