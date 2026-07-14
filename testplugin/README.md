# AgentRegistry Resource Author

Portable Claude Code/OpenClaw sample. OpenClaw 2026.7.1 requires Node.js
22.22.3+ or 24.15.0+.

Claude Code:

```bash
claude --plugin-dir ./testplugin \
  -p 'Use agentregistry-resource-authoring to draft a Prompt named demo in namespace default with description "Demo prompt" and content "Answer briefly."'
```

OpenClaw:

```bash
openclaw plugins install ./testplugin --pin
openclaw agent --local --agent main \
  --message 'Use agentregistry-resource-authoring to draft a Prompt named demo in namespace default with description "Demo prompt" and content "Answer briefly."'
```

Expected output is one applyable YAML document containing the marker
`# drafted by agentregistry-resource-author`.
