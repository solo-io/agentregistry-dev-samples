# everything-server — small demo MCP server

A tiny MCP server exposing a handful of general-purpose tools. Useful as an
end-to-end smoke test for agentregistry's MCP integration — add it to any
agent and you've got something non-trivial to call.

| Tool | Description |
|------|-------------|
| `echo` | Return the input string. |
| `now` | Return the current UTC time in ISO-8601. |
| `add` | Add two numbers. |
| `reverse` | Reverse a string. |

Built with [FastMCP](https://github.com/jlowin/fastmcp) over stdio.

## Use it

**Fork this parent repo, then copy this template:**

```bash
cp -R TEMPLATES/everything-server ./my-everything-server
cd ./my-everything-server
# edit mcp.yaml → set the image you'll push to
arctl mcp build . --push
arctl mcp publish . --version 0.1.0
```

**Wire it into an agent:**

```bash
arctl agent add-mcp "<your-registry-user>/everything-server" 0.1.0 my-agent
```
