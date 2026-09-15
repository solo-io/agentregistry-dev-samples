---
name: agentregistry-resource-authoring
description: Draft one AgentRegistry Prompt YAML document and validate it with the bundled validator. No side effects.
---

# AgentRegistry Resource Authoring

When asked to author a resource, produce exactly one YAML document, run the
bundled validator on it, and return both. Never run `arctl`, call an API,
apply the document, invent values, or claim that it is Ready.

1. Draft the YAML. The first line must be:
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

   Ask for missing name, description, or content.

2. Save the draft to a temporary file, then validate it with the
   `validate-resource` executable that ships in this skill's directory.
   Run it directly as `./validate-resource <file>` from this skill's
   directory (or by its absolute path). Do NOT run it via `node ...` and
   do NOT chmod it — it arrives executable; executing it directly is part
   of what this plugin demonstrates. If direct execution fails, report the
   exact error instead of working around it.

3. Reply with the YAML document followed by the validator's complete
   output (banner, PASS/FAIL lines, RESULT line). End with:
   `# Review, validate locally, then run: arctl apply --dry-run -f <file>`
