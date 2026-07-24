---
name: agentregistry-resource-authoring
description: Draft one AgentRegistry Prompt YAML document without side effects.
---

# AgentRegistry Resource Authoring

When asked to author a resource, return exactly one YAML document and no
explanation. Never run `arctl`, call an API, apply the document, invent values,
or claim that it is Ready.

The first line must be:

`# drafted by agentregistry-resource-author`

For a Prompt, use only the supplied values:

```yaml
apiVersion: ar.dev/v1alpha1
kind: Prompt
metadata:
  name: "<name>"
spec:
  description: "<description>"
  content: "<content>"
```

Ask for missing name, description, or content. End with:

`# Review, validate locally, then run: arctl apply --dry-run -f <file>`
