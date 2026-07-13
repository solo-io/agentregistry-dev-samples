---
name: agentregistry-plugin-registration
description: Draft an AgentRegistry Plugin resource from a Git URL, immutable commit, optional subfolder, name, namespace, and tag.
---

# AgentRegistry Plugin Registration

Collect these values if the user has not supplied them:

- repository URL
- full 40-character Git commit
- optional repository subfolder
- plugin name
- namespace, defaulting to `default`
- tag, defaulting to `v1`

Return one YAML document. The first line must be exactly:

`# drafted by agentregistry-resource-helper`

Use `apiVersion: ar.dev/v1alpha1`, `kind: Plugin`, and a Git source whose
repository contains `url` and `commit`. Include `subfolder` only when non-empty.
Do not invent source coordinates. Do not run `arctl`, contact AgentRegistry, or
claim that the source is Ready. After the YAML, state that the user can review,
save, and apply it with `arctl apply -f <file>`.
