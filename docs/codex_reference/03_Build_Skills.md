# Build Skills
Give Codex new capabilities and expertise

Use agent skills to extend Codex with task-specific capabilities. A skill packages instructions, resources, and optional scripts so Codex can follow a workflow reliably. Skills build on the open agent skills standard.

Skills are the authoring format for reusable workflows. Plugins distribute reusable skills and connectors.

## How Codex uses skills
Codex can activate skills in two ways:
1. **Explicit invocation**: Include the skill directly in your prompt. In CLI/IDE, run `/skills` or type `$` to mention a skill.
2. **Implicit invocation**: Codex can choose a skill when your task matches the skill description.

Because implicit matching depends on description, write concise descriptions with clear scope and boundaries.

## Create a skill
A skill is a directory with a `SKILL.md` file plus optional scripts and references. 

**Directory Layout:**
```text
my-skill/
  SKILL.md       (Required: instructions + metadata)
  scripts/       (Optional: executable code)
  references/    (Optional: documentation)
  assets/        (Optional: templates, resources)
  agents/
    openai.yaml  (Optional: appearance and dependencies)
```

Use the built-in creator:
```bash
$skill-creator
```

Or manually create `SKILL.md`:
```yaml
---
name: skill-name
description: Explain exactly when this skill should and should not trigger.
---

Skill instructions for Codex to follow.
```

## Where to save skills
Codex reads skills from repository, user, admin, and system locations:
- **REPO**: `$CWD/.agents/skills` (Microservice / Module)
- **REPO ROOT**: `$REPO_ROOT/.agents/skills` (Available to any subfolder)
- **USER**: `$HOME/.agents/skills` (Personal curated skills)
- **ADMIN**: `/etc/codex/skills` (Machine-wide)

## Distribute skills with plugins
Direct skill folders are best for local authoring and repo-scoped workflows. If you want to distribute a reusable skill, package them as a plugin. Plugins can include one or more skills.

## Optional metadata (openai.yaml)
Add `agents/openai.yaml` to configure UI metadata, invocation policy, and declare tool dependencies.
```yaml
interface:
  display_name: "Optional user-facing name"
  short_description: "Optional user-facing description"

policy:
  allow_implicit_invocation: false

dependencies:
  tools:
    - type: "mcp"
      value: "openaiDeveloperDocs"
```

## Best practices
- Keep each skill focused on one job.
- Prefer instructions over scripts unless you need deterministic behavior or external tooling.
- Write imperative steps with explicit inputs and outputs.
- Test prompts against the skill description to confirm the right trigger behavior.
