#!/usr/bin/env python3
from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parents[2]
REQUIRED = [
    ROOT / "src" / ".codex-plugin" / "plugin.json",
    ROOT / "README.md",
    ROOT / "logs",
]

errors = []
for path in REQUIRED:
    if not path.exists():
        errors.append(f"Missing required path: {path.relative_to(ROOT)}")

plugin_path = ROOT / "src" / ".codex-plugin" / "plugin.json"
if plugin_path.exists():
    try:
        plugin = json.loads(plugin_path.read_text(encoding="utf-8"))
        for key in ["name", "version", "description"]:
            if not plugin.get(key):
                errors.append(f"plugin.json missing key: {key}")
    except Exception as exc:
        errors.append(f"plugin.json is not valid JSON: {exc}")

skills_dir = ROOT / "src" / "skills"
if not skills_dir.exists() or not any(skills_dir.glob("*/SKILL.md")):
    errors.append("At least one skill with SKILL.md is required under src/skills/<skill-name>/SKILL.md")

logs_dir = ROOT / "logs"
if logs_dir.exists():
    log_files = [p for p in logs_dir.rglob("*") if p.is_file() and p.suffix.lower() in {".md", ".txt", ".json", ".jsonl"}]
    if not log_files:
        errors.append("logs/ exists but contains no md/txt/json/jsonl log files")

if errors:
    print("Validation failed:")
    for e in errors:
        print(f"- {e}")
    sys.exit(1)

print("Validation passed. Submission structure looks ready for packaging.")
