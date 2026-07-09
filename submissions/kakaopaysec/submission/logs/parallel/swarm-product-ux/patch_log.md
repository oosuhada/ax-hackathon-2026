## Patch Log - Iteration 1

### File: README.md
- **Change**: `Value: AUM Retention & Safe Conversion` -> `Value: AUM Retention & Suitability Check`
- **Change**: `안전 자산 투자로 라우팅` -> `투자성향 진단 및 리스크 체크리스트 확인으로 라우팅`
- **Change**: `안전 자산 전환(Safe Conversion)` -> `적합성 확인(Suitability Check)`
- **Change**: `로보어드바이저 및 우량 ETF 등` -> 문구 삭제 및 `단순 상품 가입 유도 대신 투자성향 진단 및 공식 설명 확인, 상담 연결 절차로` 로 교체
- **Reason**: 투자 권유성 워딩의 완전한 배제를 위해.

### File: src/skills/fomo-defense-agent/SKILL.md
- **Change**: `금융 상품이나 안전 자산 라우팅 방식을 차별하지 마십시오.` -> `투자성향 진단이나 공식 설명 확인 등의 라우팅 방식을 차별하지 마십시오.`
- **Change**: `개별 종목 대신 '투자성향 진단' 절차를 거쳐 증권사의 우량 ETF나 로보어드바이저 등 안전 자산(Safe Conversion)으로의 분산 투자를 검토하도록 안내하십시오.` -> `개별 종목 제안 대신 '투자성향 진단' 절차를 거쳐 공식 설명 확인 및 상담 연결을 검토하도록 안내하십시오.`
- **Change**: `show_safe_routing_button` -> `show_suitability_routing_button`
- **Reason**: 구체적인 상품명 및 투자 유도성 지시를 적합성 확인 중심의 워딩으로 100% 교체.

### File: src/.codex-plugin/plugin.json
- **Change**: `"description": "...안심 투자를 유도하는..."` -> `"description": "...안심/적합성 절차로 유도하는..."`
- **Reason**: 메타데이터 레벨에서도 투자 권유 뉘앙스 제거.
