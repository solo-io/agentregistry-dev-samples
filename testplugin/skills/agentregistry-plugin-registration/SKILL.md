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
Serialize every dynamic YAML scalar with JSON quoting, which is valid YAML:

```bash
jq -Rn --arg value "${VALUE}" '$value'
```

This applies to metadata `name`, `namespace`, and `tag`, plus repository `url`,
`commit`, and a non-empty `subfolder`. Never place a raw user value into YAML.
Do not invent source coordinates. Do not run `arctl`, contact AgentRegistry, or
claim that the source is Ready.

The response must contain only the single applyable YAML document. Keep the
first-line marker and put apply guidance in YAML comments at the end, for
example `# Review, save, then run: arctl apply -f <file>`. Emit no prose before
or after the document.
