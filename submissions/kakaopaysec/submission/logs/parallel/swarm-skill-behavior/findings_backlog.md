# Findings Backlog

1. **SKILL execution failure possibility 1**: `dummy_peer_data.json`이 누락되거나 구조가 바뀔 경우 LLM이 합성 데이터를 환각할 가능성 존재. (조치 필요)
2. **SKILL execution failure possibility 2**: 사용자 입력에서 `risk_tolerance` 필드가 비정상적인 값(예: "모름")으로 들어왔을 때의 매핑 실패 가능성.
3. **SKILL execution failure possibility 3**: 마크다운 응답 안에 JSON 블록이 감싸지지 않고 텍스트가 혼용되어 프론트엔드 파서가 고장날 위험.
4. **SKILL execution failure possibility 4**: show_safe_routing_button이 true로 설정되어 있으나 프론트엔드 라우터에 해당 경로가 누락된 경우의 무응답 리스크.
5. **SKILL execution failure possibility 5**: 사용자 입력이 JSON 파싱을 깨는 특수문자(예: 겹따옴표 등)를 포함할 경우.
6. **SKILL execution failure possibility 6**: API Timeout으로 인해 LLM이 JSON의 disclaimer 필드까지 생성하지 못하고 중단될 경우, 법적 면책 없이 응답이 노출되는 문제.
