# alanbentleypghagentdemo Agent

This project was scaffolded with the AgentRegistry CLI. It gives you a working
ADK Python agent wired for MCP tools and ready to publish through AgentRegistry.

## Model configuration

- Provider: **bedrock**
- Model: **us.anthropic.claude-sonnet-4-6**

Update `alanbentleypghagentdemo/agent.py` if you need to switch providers, add tools, or
change the root instructions.

## Local iteration

1. Install [uv](https://docs.astral.sh/uv/) if you haven't already.
2. From the project root run:

   ```bash
   uv sync
   uv run alanbentleypghagentdemo
   ```

3. Use `arctl agent run .` to launch the local chat experience with docker
   compose.

## Build & publish with AgentRegistry

1. Build (and optionally push) the container image:

   ```bash
   arctl build . --push
   ```

2. Publish the agent so the registry can serve it to clients:

   ```bash
   arctl apply -f agent.yaml
   ```

3. Share the resulting agent link or deploy it to your runtime of choice.

Need MCP servers? Edit `agent.yaml` manually to append MCP entries under
`spec.mcpServers`, then re-apply once you're happy with the configuration:

```bash
arctl apply -f agent.yaml
```

