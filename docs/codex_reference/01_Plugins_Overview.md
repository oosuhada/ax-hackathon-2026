# Plugins Overview

Browse, install, and use plugins in ChatGPT and Codex clients

## Overview
Plugins bundle capabilities into reusable workflows in ChatGPT. They can include skills, an MCP-backed app, or both. Plugins are available in ChatGPT Work on the web and in Work or Codex in the ChatGPT desktop app. Codex CLI and the IDE extension can also browse and install plugins for a Codex environment.

In the ChatGPT desktop app, open Plugins from Work or Codex to browse, install, and use plugins. Installed plugins can add skills, connectors, and MCP tools to new chats.

Extend what ChatGPT can do, for example:
- Install the Codex Security plugin to scan authorized code and confirm plausible vulnerability findings.
- Install the Gmail plugin to let ChatGPT read and manage Gmail.
- Install the Google Drive plugin to work across Drive, Docs, Sheets, and Slides.
- Install the Slack plugin to summarize channels or draft replies.

A plugin can contain one or more of these parts:
- **Skills**: reusable instructions for specific kinds of work.
- **Apps**: connections to tools like GitHub, Slack, or Google Drive.
- **MCP servers**: services that give ChatGPT access to more tools or shared information.
- **Browser extensions**: browser capabilities that a plugin needs for its workflow.
- **Hooks**: commands that run at configured lifecycle points.
- **Scheduled task templates**: reusable starting points for recurring tasks.

## Use and install plugins
To browse and install curated plugins:
1. On the web, select Work and open Plugins.
2. In the ChatGPT desktop app, select Work or Codex and open Plugins.

The plugin directory organizes plugins into tabs:
- OpenAI: plugins built by OpenAI.
- Your workspace name: plugins provided by your workspace.
- Personal: personal marketplace plugins, including Created by me and Shared with me.

## Install and use a plugin in ChatGPT
Once you open the plugin directory:
1. Search or browse for a plugin, then open its details.
2. Select the plus button to install the plugin.
3. If the plugin needs a connector, connect it when prompted.

After installation, start a new task and ask ChatGPT to use the plugin.
- **Describe the task directly**: Ask for the outcome you want, such as “Summarize unread Gmail threads from today”.
- **Choose a specific plugin**: Type `@` to invoke the plugin or one of its bundled skills explicitly.

## How permissions and data sharing work
When a plugin capability runs through a Codex host, the host’s sandbox and approval policy applies.
- Bundled skills become available when you start a new chat or CLI session after installation.
- When ChatGPT sends data through a bundled connector, that service’s terms and privacy policy apply.

## Remove a plugin
To remove a plugin, reopen it from the plugin browser and select Uninstall plugin.
