---
description: Draft an AgentRegistry Plugin resource for a published Git source
argument-hint: <repository-url> <40-character-commit> [subfolder]
---

Use the `agentregistry-plugin-registration` skill to draft a Plugin resource
from `$ARGUMENTS`. Ask for any missing name, namespace, or tag. Do not apply it.
Return only the applyable YAML document, with apply guidance in YAML comments
and every supplied value safely quoted as required by the skill.
