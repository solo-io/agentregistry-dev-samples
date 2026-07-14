# AgentRegistry Resource Author

Portable Claude Code and OpenClaw sample for drafting AgentRegistry resources.
Its shared behavior lives in `skills/agentregistry-resource-authoring/SKILL.md`.

## Local behavior checks

Claude Code:

```bash
claude --plugin-dir ./testplugin \
  -p 'Use agentregistry-resource-authoring to draft a Prompt named demo in namespace default with description "Demo prompt" and content "Answer briefly."'
```

OpenClaw:

```bash
openclaw plugins install ./testplugin --pin
openclaw agent --local --message 'Use agentregistry-resource-authoring to draft the same Prompt resource.'
```

Validate a generated document locally without credentials or network access:

```bash
python3 scripts/validate-resource.py prompt.yaml
cat prompt.yaml | python3 scripts/validate-resource.py -
```

Successful output is one applyable YAML document containing
`# drafted by agentregistry-resource-author` and the requested resource kind.
