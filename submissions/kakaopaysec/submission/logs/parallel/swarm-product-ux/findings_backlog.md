# Findings Backlog
- **BL-01 (Privacy)**: 현재 로그 시스템(`logs/transcript.jsonl`) 내 사용자 프롬프트 평문 저장 이슈. (로깅 계층 필터링 추가 필요)
- **BL-02 (Architecture)**: 실제 API 환경에서 사용하기 위한 Pre-LLM Data Scrubber(정규표현식, NER 등) 도입 필요.
- **BL-03 (Performance)**: 빈 입력 시 불필요한 LLM 호출 낭비 (API Gateway 단의 필터링 아키텍처 적용 필요).
