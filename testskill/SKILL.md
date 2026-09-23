---
name: harness-mount-probe
description: Reports a token that exists only inside this file, proving the harness config directory survived onto the serving session's mount.
---

# Harness Mount Probe

This skill exists for one purpose: to prove that a file written into the
harness config directory during container **initialization** is still readable
during an **invocation**.

`claude.Harness.Configure` symlinks every bundled skill into
`$CLAUDE_CONFIG_DIR/skills/<name>` at init. When `CLAUDE_CONFIG_DIR` is
AgentCore's managed session storage mount, that write happens before the mount
is bound to the session the container goes on to serve. If the mount is
rebound at invoke, the symlink is gone and this file cannot be read.

The token below appears nowhere else — not in the smoke prompt, not in the
runner, not in any deployed resource. Echoing it back is only possible by
reading this file off the mount.

MOUNT_INIT_TOKEN=SKILLMOUNT-7F3A21C9

When asked for the mount probe token, reply with exactly the value above.
