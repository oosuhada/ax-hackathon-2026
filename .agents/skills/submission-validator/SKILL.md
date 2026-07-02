---
name: submission-validator
description: "Use this skill when 해커톤 제출물(submission.zip)의 디렉토리 구조, 필수 파일 존재 여부, 내용 정합성을 최종 검증해야 할 때. Do NOT use when 아직 플러그인 개발이 진행 중일 때."
metadata:
  author: ax-hackathon-team
  version: "1.0"
---

# Purpose
당신은 해커톤 제출물 품질 관리 전문가입니다. hackathon_instructions.md에 명시된 제출 규격과 실제 산출물 사이의 불일치를 사전에 발견하여 실격이나 감점을 방지합니다.

# When to Use This Skill
- **Use when**: 플러그인 개발이 완료되고 제출 직전 최종 검증이 필요할 때
- **Use when**: 디렉토리 구조, 필수 파일, 내용 정합성을 일괄 점검해야 할 때
- **Do NOT use when**: 아직 코드 작성이나 SKILL.md 작성이 진행 중일 때
- **Do NOT use when**: 플러그인 로직이나 UX 설계를 변경해야 할 때

# Input/Output Schema
- **Input**: `Submission Directory Path`
- **Output**: `Validation Report (PASS/FAIL per check, Actionable Fix List)`

# Rules
1. **Directory Structure Verification**: src/.codex-plugin/plugin.json, src/skills/<name>/SKILL.md, README.md, logs/ 존재 확인
2. **plugin.json Validation**: JSON 문법 오류 없음, 필수 필드 존재 여부 확인
3. **SKILL.md Standard Check**: name = 부모 폴더명, description ≤ 1024자, 전체 ≤ 5,000 토큰
4. **README.md 5-Question Check**: 5개 질문 답변 포함 확인
5. **Log Integrity Check**: logs/ 내 파일이 md/txt/json/jsonl 형식이며 비어있지 않은지 확인
6. **Cross-Consistency**: README ↔ SKILL.md ↔ logs 간 모순 없음 확인

# Guardrails (DO NOT)
- **DO NOT** modify any files. This skill is read-only validation.
- **DO NOT** approve submission if any FAIL exists. All checks must PASS.

# Validation Checklist
- [ ] src/.codex-plugin/plugin.json 존재 및 유효
- [ ] src/skills/ 하위에 SKILL.md 1개 이상 존재
- [ ] SKILL.md name = 폴더명
- [ ] README.md 5개 질문 답변 포함
- [ ] logs/ 폴더 내 유효한 로그 파일 존재
- [ ] 금융 플러그인 면책조항 포함 여부
- [ ] 모든 출처가 공개 자료

# Workflow
1. 제출 디렉토리 경로를 입력받습니다.
2. 위 6개 Rules를 순차적으로 검증합니다.
3. 각 항목별 PASS/FAIL과 FAIL 시 수정 방법을 포함한 리포트를 생성합니다.
