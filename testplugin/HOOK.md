---
name: agentregistry-resource-author
description: "Loads the AgentRegistry resource authoring skill."
metadata:
  { "openclaw": { "emoji": "🧩", "events": [] } }
---

# AgentRegistry Resource Authoring

When the user asks to author an AgentRegistry resource, use the
`agentregistry-resource-authoring` skill from this plugin. Return exactly one
YAML resource document and do not run `arctl` or call external services.
