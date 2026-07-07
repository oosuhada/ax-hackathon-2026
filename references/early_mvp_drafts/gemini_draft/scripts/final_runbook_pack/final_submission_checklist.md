# 최종 제출 체크리스트

## 기업별 체크

- [ ] 기업별로 별도의 zip을 만들었다.
- [ ] 하나의 zip에 여러 기업 내용이 섞이지 않았다.
- [ ] zip 루트에 `src/`, `README.md`, `logs/`가 바로 있다.
- [ ] `src/.codex-plugin/plugin.json`이 있다.
- [ ] `src/skills/<name>/SKILL.md`가 있다.
- [ ] `README.md`에 5문항 답변이 있다.
- [ ] `logs/`에 실제 AI 대화 원본이 있다.
- [ ] 로그를 편집/삭제/발췌하지 않았다.
- [ ] `evidence_sources.md`에 공개자료 URL이 있다.
- [ ] README의 주장과 evidence가 모순되지 않는다.
- [ ] 샘플 입력/출력이 있다.
- [ ] 검증 기준이 있다.

## 제출 전 위험 점검

| 위험 | 점검 |
|---|---|
| 가짜 로그 제출 | 절대 금지. 실제 대화 원본만 제출 |
| 출처 없는 수치 | 삭제하거나 TODO_SOURCE로 표시 |
| 기업 내부정보처럼 보이는 내용 | 삭제 |
| 플러그인 기능 과장 | “보조”, “초안”, “점검”으로 표현 |
| 금융투자 조언 위험 | 카카오페이증권 플러그인은 매수/매도 추천 금지 |
| 삼일PwC 내부 방법론 사칭 | 공개자료 기반 범용 프레임워크로 표현 |
| 무신사 실시간 재고/지도 API 단정 | 상권 단위 추천, 실시간 확인 필요로 표현 |

## 압축 명령 예시

각 기업 폴더 안에서:

```bash
zip -r submission.zip src README.md logs
```

또는 macOS Finder에서 `src`, `README.md`, `logs`를 선택해 압축한 뒤 파일명을 `submission.zip`으로 변경.
