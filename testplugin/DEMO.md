# Demo: plugin-bundled executable running in a hosted agent

**Story (one line):** this plugin carries a real executable; the hosted
agent runs it in-session — same bundle, both harnesses. The legacy
env-var config transport stripped executable permissions, so this demo is
only possible on the image/S3 bundle transports.

## Prompt (send to BOTH the Claude Code and the OpenClaw deployment)

> Use agentregistry-resource-authoring to draft a Prompt named demo with
> description "Demo prompt" and content "Answer briefly." Return exactly
> one YAML document, then run the bundled validate-resource executable on
> your draft and include its full output.

## What to point at in the reply

1. `# drafted by agentregistry-resource-author` — the skill loaded from the plugin.
2. `agentregistry-resource-validator v0.1.0 (bundled executable)` — a binary
   that traveled inside the plugin bundle just executed inside the agent.
3. `PASS:` lines and `RESULT: VALID` — real output, not prose.
4. Run the identical prompt on the other harness deployment — same plugin,
   same result.

## Second beat (optional): show the validator is real

> Use agentregistry-resource-authoring to draft a Prompt named demo with
> description "Demo prompt" and content set to the empty string "". Return
> exactly one YAML document, then run the bundled validate-resource
> executable on your draft and include its full output.

The empty string is a supplied (not missing) value, so the skill drafts and
validates instead of asking for content.

Expected: `FAIL: spec.content is non-empty (Prompt)` and `RESULT: INVALID`.

## Troubleshooting

If the agent reports the validator is missing right after a (re)deploy, the
endpoint is likely still serving the previous runtime version — wait a
minute and re-send the prompt.
