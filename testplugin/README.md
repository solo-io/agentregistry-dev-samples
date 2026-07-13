# AgentRegistry Resource Helper

This directory contains a portable plugin fixture for drafting Git-backed
AgentRegistry `Plugin` resources.

## Layout

- `.claude-plugin/plugin.json` — plugin metadata
- `skills/agentregistry-plugin-registration/SKILL.md` — registration workflow
- `commands/register-plugin.md` — optional interactive command

## Local behavior checks

Claude Code:

```bash
claude --plugin-dir ./testplugin \
  -p 'Use agentregistry-plugin-registration to draft a Plugin named demo at tag v1 in namespace default for https://github.com/acme/plugins commit 0123456789abcdef0123456789abcdef01234567 subfolder plugins/demo.'
```

OpenClaw:

```bash
openclaw plugins install ./testplugin --pin
openclaw agent --local --message 'Use agentregistry-plugin-registration to draft the same Plugin resource.'
```

Successful output contains:

```text
# drafted by agentregistry-resource-helper
kind: Plugin
```
