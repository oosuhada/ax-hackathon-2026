# Build Plugins
Create, test, and distribute plugins for ChatGPT

This page is for plugin authors. If you want to browse, install, and use plugins, see Plugins. 
Build a plugin when you want to share a workflow across teams, bundle connectors or MCP config, package lifecycle hooks, or publish a stable package.

## Create a plugin with @plugin-creator
For the fastest setup, use the built-in `@plugin-creator` skill.
It scaffolds the required `.codex-plugin/plugin.json` manifest and can also generate a local marketplace entry for testing.

Prompt example:
> `$plugin-creator create a Codex plugin for my ChatGPT app.`
> `Use plugin_asdk_app_6a4c... and name it Acme Support.`
> `Include a personal marketplace entry so I can test it locally.`

After creation:
1. Review `.app.json`.
2. Review `.codex-plugin/plugin.json`.
3. Add any bundled skills under `skills/`.

## Build your own curated plugin list (Marketplace)
A marketplace is a JSON catalog of plugins. 
Use `$REPO_ROOT/.agents/plugins/marketplace.json` for a repo-scoped list or `~/.agents/plugins/marketplace.json` for a personal list.

### Add a marketplace from the CLI
```bash
codex plugin marketplace add owner/repo
codex plugin marketplace add https://github.com/example/plugins.git --sparse .agents/plugins
codex plugin marketplace add ./local-marketplace-root
```

To inspect or remove configured marketplaces:
```bash
codex plugin marketplace list
codex plugin marketplace upgrade
codex plugin marketplace remove marketplace-name
```

## Create a plugin manually
Start with a minimal plugin that packages one skill.
```bash
mkdir -p my-first-plugin/.codex-plugin
```

**my-first-plugin/.codex-plugin/plugin.json**
```json
{
  "name": "my-first-plugin",
  "version": "1.0.0",
  "description": "Reusable greeting workflow",
  "skills": "./skills/"
}
```

Add a skill under `skills/<skill-name>/SKILL.md`.

## Plugin structure
Every plugin has a manifest at `.codex-plugin/plugin.json`. It can also include a `skills/` directory, a `hooks/` directory, `.app.json`, `.mcp.json`, and `assets/`.

**Directory Layout:**
```text
my-plugin/
  .codex-plugin/
    plugin.json      (Required)
  skills/            (Optional)
  hooks/             (Optional)
  .app.json          (Optional)
  .mcp.json          (Optional)
  assets/            (Optional)
```

## Manifest fields
- `name`, `version`, `description` identify the plugin.
- `author`, `homepage`, `repository` provide discovery metadata.
- `skills`, `mcpServers`, `apps`, and `hooks` point to bundled components relative to the plugin root (starting with `./`).

## Bundled MCP servers and lifecycle hooks
After installation, users can enable or disable a bundled MCP server and tune tool approval policy from their Codex config without editing the plugin.

Plugin hooks use the same event schema as regular hooks. Installing or enabling a plugin doesn’t automatically trust its hooks. Plugin-bundled hooks are non-managed hooks, so Codex skips them until the user reviews and trusts the current hook definition.
