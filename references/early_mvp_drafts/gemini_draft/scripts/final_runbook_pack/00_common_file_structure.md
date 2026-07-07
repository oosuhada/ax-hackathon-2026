# 00. 공통 제출 파일 구조 템플릿

각 기업별 제출 zip 내부는 아래 구조를 추천합니다.

```text
submission.zip
├── src/
│   ├── .codex-plugin/
│   │   └── plugin.json
│   ├── skills/
│   │   └── <skill-name>/
│   │       ├── SKILL.md
│   │       └── references/
│   │           └── evidence_sources.md
│   ├── sample_inputs/
│   │   └── sample_input.md
│   ├── sample_outputs/
│   │   └── sample_output.md
│   └── scripts/
│       └── validate_submission_structure.py
├── README.md
└── logs/
    └── <company>_raw_log.md
```

## `plugin.json` 권장 필드

```json
{
  "name": "plugin-name",
  "version": "1.0.0",
  "description": "짧은 설명",
  "author": "Woosoo Jang",
  "skills": [
    {
      "name": "skill-folder-name",
      "description": "Codex가 언제 이 스킬을 사용해야 하는지"
    }
  ]
}
```

## 검증 스크립트 예시

```python
from pathlib import Path

required = [
    "src/.codex-plugin/plugin.json",
    "README.md",
    "logs",
]

missing = [p for p in required if not Path(p).exists()]
if missing:
    print("MISSING:", missing)
    raise SystemExit(1)

skill_files = list(Path("src/skills").glob("*/SKILL.md"))
if not skill_files:
    print("MISSING: src/skills/<name>/SKILL.md")
    raise SystemExit(1)

print("OK: submission structure looks valid.")
```
