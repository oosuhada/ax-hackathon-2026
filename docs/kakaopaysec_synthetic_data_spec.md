# 카카오페이증권 합성 데이터 명세서 (Synthetic Data Spec)

## 1. 개요
본 문서는 카카오페이증권 FOMO 방어 에이전트에서 동조 효과(Bandwagon Effect)를 일으키기 위해 사용하는 또래 투자자 행동 데이터(`Dummy_Peer_Data.json`)의 스펙을 정의합니다.
이 데이터는 실제 고객 데이터가 아닌 100% 가상의 **[SYNTHETIC]** 데이터입니다.

## 2. 제약 조건 (Guardrails)
- **실제 데이터 사용 금지**: 실제 투자자의 이름, 실제 계좌번호, 특정 개인을 특정할 수 있는 실제 포트폴리오 데이터는 절대 포함하지 않습니다.
- **[SYNTHETIC] 명시**: JSON 파일 및 응답에서 데이터가 가상의 시뮬레이션 기반임을 명시하여 컴플라이언스(Compliance) 방어를 수행합니다.

## 3. 구조 및 필드 정의
데이터는 사용자의 프로필(`age_band`, `asset_band`, `risk_tolerance`)에 매핑할 수 있도록 그룹화되어 있습니다.

- `group_profile`: 타겟 사용자 그룹 정의 (예: 20대, 자산 1천미만, 안정추구)
- `market_sentiment_reaction`: 현재 시장 변동성에 대한 해당 그룹의 주요 반응 (예: HOLD, BUY_FRACTIONAL)
- `peer_hold_ratio_percent`: 관망하거나 소액 분할 매수 중인 비중 (FOMO 진정 목적)
- `preferred_safe_action`: 권장되는 안전한 대안 (예: monthly_fractional_saving)
- `roi_metric_link`: 데이터가 기여하는 비즈니스 임팩트 (ROI)
  - `deflection_score`: 단순 상담/문의를 스스로 해결하게 만드는 방어율 기여도
  - `conversion_to_safe_action`: 적립식 투자 등 안전한 행동으로 전환될 확률
  - `compliance_defense_flag`: 투자 권유가 아닌 통계적 정보 제공으로 면책 성립 여부

## 4. 데이터 활용 로직
AI는 사용자 질문이 입력되면 이 JSON 데이터를 조회하여, "현재 당신과 비슷한 20대 안정형 투자자의 82%는 일시적으로 투자를 보류하고 있습니다."와 같은 안심 멘트(`peer_benchmark`)를 생성합니다.
