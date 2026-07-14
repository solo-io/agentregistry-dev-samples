#!/usr/bin/env python3
"""Offline checks for the small AgentRegistry YAML resource subset."""

import argparse
import json
import re
import sys
from pathlib import Path


SUPPORTED = {"Agent", "MCPServer", "Skill", "Prompt", "Plugin", "Runtime", "Deployment"}
SECRET_WORDS = ("password", "token", "secret", "api_key", "apikey", "private_key")
KEY_RE = re.compile(r"^(?P<indent> *)(?P<key>[A-Za-z][A-Za-z0-9_.-]*):(?:\s*(?P<value>.*))?$")


def fail(message):
    print(f"invalid AgentRegistry resource: {message}", file=sys.stderr)
    return 1


def scalar(value):
    value = value.strip()
    if not value or value in {"|", ">", "|-", ">-", "|+", ">+"}:
        return ""
    if value.startswith(("\"", "'")) and value[-1:] == value[0]:
        return value[1:-1]
    if value.startswith("[") or value.startswith("{"):
        try:
            return json.loads(value)
        except json.JSONDecodeError:
            return value
    return value.split(" #", 1)[0].strip()


def read_document(path):
    if path == "-":
        return sys.stdin.read()
    return Path(path).read_text(encoding="utf-8")


def validate(text):
    lines = text.splitlines()
    if not lines:
        return "document is empty"
    documents = [line for line in lines if line.strip() in {"---", "..."}]
    if documents:
        return "exactly one YAML document is required"

    paths = {}
    stack = []
    for raw in lines:
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        match = KEY_RE.match(raw)
        if not match:
            continue
        indent = len(match.group("indent"))
        while stack and stack[-1][0] >= indent:
            stack.pop()
        key = match.group("key")
        path = ".".join([item[1] for item in stack] + [key])
        value = scalar(match.group("value") or "")
        paths[path] = value
        if not match.group("value") or match.group("value").strip() in {"|", ">", "|-", ">-", "|+", ">+"}:
            stack.append((indent, key))

    api_version = paths.get("apiVersion")
    kind = paths.get("kind")
    name = paths.get("metadata.name")
    if api_version != "ar.dev/v1alpha1":
        return "apiVersion must be ar.dev/v1alpha1"
    if kind not in SUPPORTED:
        return f"kind must be one of {', '.join(sorted(SUPPORTED))}"
    if not name:
        return "metadata.name is required"

    for path, value in paths.items():
        key = path.rsplit(".", 1)[-1].lower()
        if any(word in key for word in SECRET_WORDS):
            return f"secret-like field is not allowed: {path}"
        if isinstance(value, str) and any(word in value.lower() for word in ("bearer ", "-----begin private key-----")):
            return f"credential-like value is not allowed: {path}"

    if kind == "Deployment":
        target_kind = paths.get("spec.targetRef.kind")
        target_name = paths.get("spec.targetRef.name")
        runtime_kind = paths.get("spec.runtimeRef.kind")
        runtime_name = paths.get("spec.runtimeRef.name")
        if target_kind not in {"Agent", "MCPServer"}:
            return "Deployment spec.targetRef.kind must be Agent or MCPServer"
        if not target_name:
            return "Deployment spec.targetRef.name is required"
        if runtime_kind != "Runtime":
            return "Deployment spec.runtimeRef.kind must be Runtime"
        if not runtime_name:
            return "Deployment spec.runtimeRef.name is required"
    return None


def main():
    parser = argparse.ArgumentParser(description="Validate one AgentRegistry resource offline")
    parser.add_argument("file", nargs="?", default="-", help="YAML file, or - for stdin")
    args = parser.parse_args()
    try:
        error = validate(read_document(args.file))
    except OSError as exc:
        return fail(str(exc))
    if error:
        return fail(error)
    print("valid AgentRegistry resource")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
