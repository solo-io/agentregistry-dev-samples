# agentdemo — dice-rolling ADK-Python agent

A minimal Google ADK agent that rolls dice and checks primes. Useful as a
starting point for any ADK-Python agent you want to build and publish to
agentregistry.

**Fork the parent repo first, then copy this template out.** Do not edit it
in place.

```bash
cp -R TEMPLATES/agentdemo ./my-agent
cd ./my-agent
# edit agent.yaml → set the image name you'll push to
arctl agent build .
arctl agent run .
```

## What's inside

- `agent/agent.py` — the ADK `root_agent` with two built-in tools (`roll_die`,
  `check_prime`). Add MCP tools later via `arctl agent add-mcp`.
- `agent/bedrock_model.py` — a small ADK `BaseLlm` adapter that calls
  Claude on Amazon Bedrock via the official Anthropic SDK. ~160 lines,
  easy to read, easy to swap.
- `agent.yaml` — the registry manifest.
- `Dockerfile` — builds on `ghcr.io/kagent-dev/kagent/kagent-adk`.
- `pyproject.toml` — pins `google-adk` and `anthropic[bedrock]`.

## Model provider

Defaults to **Anthropic Claude on AWS Bedrock**. The same code works in two
environments with no per-environment branching:

- **Locally**: the `anthropic.AnthropicBedrock` client reads your default
  boto3 credential chain — usually an active SSO session (`aws sso login
  --profile <profile>`).
- **On AgentCore**: the workload identity attached to the runtime handles
  Bedrock auth automatically. No API keys, no env vars.

Before your first run, enable model access for the default model in the
[AWS Bedrock console](https://console.aws.amazon.com/bedrock/home#/modelaccess)
(one-time, per account + region).

To use a different Claude, set `AGENT_MODEL` to any Bedrock model ID:

```bash
AGENT_MODEL=anthropic.claude-3-5-haiku-20241022-v1:0 arctl agent run .
```

To target a different provider altogether (OpenAI, Gemini, etc.), replace
the `BedrockClaude` instance in `agent/agent.py` with whichever ADK model
class you prefer — the rest of the agent stays the same.

## Expected env

- `AGENT_MODEL` — optional; overrides the default Bedrock model ID.
- `AWS_REGION` — optional; defaults to `us-east-1` if unset.
- `OTEL_EXPORTER_OTLP_TRACES_ENDPOINT` — optional; unset ⇒ no tracing.
