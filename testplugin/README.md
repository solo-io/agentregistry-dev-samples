# AgentRegistry Resource Author

Portable Claude Code and OpenClaw sample for drafting AgentRegistry resources.
Its shared behavior lives in `skills/agentregistry-resource-authoring/SKILL.md`.

OpenClaw 2026.7.1 requires Node.js 22.22.3+ or 24.15.0+.

## Local behavior checks

Claude Code:

```bash
claude --plugin-dir ./testplugin \
  -p 'Use agentregistry-resource-authoring to draft a Prompt named demo in namespace default with description "Demo prompt" and content "Answer briefly."'
```

OpenClaw:

```bash
openclaw plugins install ./testplugin --pin
openclaw agent --local --agent main \
  --message 'Use agentregistry-resource-authoring to draft the same Prompt resource.'
```

The plugin includes `HOOK.md` because OpenClaw requires that file for local
plugin installation. The hook delegates resource authoring to the shared
skill used by Claude Code.

Successful output is one applyable YAML document containing
`# drafted by agentregistry-resource-author` and the requested resource kind.
