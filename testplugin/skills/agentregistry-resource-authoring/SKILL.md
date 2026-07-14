---
name: agentregistry-resource-authoring
description: Draft one applyable AgentRegistry resource YAML document with safe references and no side effects.
---

# AgentRegistry Resource Authoring

Help the user draft exactly one AgentRegistry resource at a time. Ask which
resource they want, collect missing required values, and return only one YAML
document. Never run `arctl`, call an API, apply the document, invent a source,
image, credential, or referenced resource, or claim that a resource is Ready.

The first line must be exactly:

`# drafted by agentregistry-resource-author`

Use `apiVersion: ar.dev/v1alpha1`, a supported `kind`, and
`metadata.name`. Quote every user-provided scalar with JSON-style double quotes
inside YAML. Preserve user values; do not silently normalize names or URLs.

Supported kinds and minimum fields:

- `Agent`: ask for a name, description, source, and any referenced MCPServer names.
- `MCPServer`: ask for a name, description, transport, and source/package details.
- `Skill`: ask for a name, description, and skill content or source details.
- `Prompt`: ask for a name, description, and prompt content.
- `Plugin`: ask for a name, title/description, compatible harnesses, and Git source.
- `Runtime`: ask for a name, runtime type, and provider-specific settings.
- `Deployment`: ask for the target and runtime references described below.

Use the repository’s API examples as field guidance, but include only fields
the user supplied or explicitly selected. If a required value is unknown, ask
for it instead of producing a guessed manifest.

## Deployment rules

Deployment is a reference resource, not a place to define an Agent or
MCPServer. Require both references:

```yaml
spec:
  targetRef:
    kind: "Agent" # or "MCPServer"
    name: "example-agent"
  runtimeRef:
    kind: "Runtime"
    name: "example-runtime"
```

The target kind must be exactly `Agent` or `MCPServer`. The runtime kind must
be exactly `Runtime`. Ask for the namespace when the target or runtime is not
in the default namespace, and do not infer cross-namespace references. Ask
for harness-specific fields only when the target is a harness Agent. Never put
passwords, bearer tokens, API keys, or secret values in `env`.

End the document with a YAML comment such as:

`# Review, validate locally, then run: arctl apply --dry-run -f <file>`
