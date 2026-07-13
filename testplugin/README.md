# AgentRegistry Resource Helper

Portable Claude Code and OpenClaw sample for drafting Git-backed AgentRegistry
`Plugin` resources. Its shared behavior lives in
`skills/agentregistry-plugin-registration/SKILL.md`.

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

Successful output is one applyable YAML document containing
`# drafted by agentregistry-resource-helper` and `kind: Plugin`.
