#!/usr/bin/env python3
"""Validate the minimum structure expected by the AX preliminary submission."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

REQUIRED = [
    ROOT / "src" / ".codex-plugin" / "plugin.json",
    ROOT / "src" / "skills" / "kps-investor-risk-brief" / "SKILL.md",
    ROOT / "README.md",
    ROOT / "logs",
]


def main() -> None:
    errors = []
    for path in REQUIRED:
        if not path.exists():
            errors.append(f"Missing required path: {path.relative_to(ROOT)}")

    plugin_path = ROOT / "src" / ".codex-plugin" / "plugin.json"
    if plugin_path.exists():
        try:
            manifest = json.loads(plugin_path.read_text(encoding="utf-8"))
            for key in ["name", "version", "description", "skills"]:
                if key not in manifest:
                    errors.append(f"plugin.json missing key: {key}")
        except json.JSONDecodeError as exc:
            errors.append(f"plugin.json is invalid JSON: {exc}")

    skill_path = ROOT / "src" / "skills" / "kps-investor-risk-brief" / "SKILL.md"
    if skill_path.exists():
        text = skill_path.read_text(encoding="utf-8")
        if "name:" not in text or "description:" not in text:
            errors.append("SKILL.md must include name and description metadata")

    if errors:
        print("Validation failed:")
        for err in errors:
            print(f"- {err}")
        raise SystemExit(1)

    print("Validation passed. Minimum skeleton is present.")
    print("Reminder: replace logs/ placeholder files with raw, unedited AI conversation logs before final submission.")


if __name__ == "__main__":
    main()
