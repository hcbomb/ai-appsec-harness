#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
import stat
import sys
from pathlib import Path


REQUIRED_FILES = [
    "AGENTS.md",
    "CLAUDE.md",
    ".agents/skills/ai-appsec-harness/SKILL.md",
    ".claude/skills/ai-appsec-harness/SKILL.md",
    "docs/agent-tool-import.md",
    "docs/aisvs-operationalization.md",
    "docs/threat-modeling-stride.md",
    "data/control-catalog.seed.json",
]

AGENT_SURFACES = [
    "AGENTS.md",
    "CLAUDE.md",
    ".agents/skills/ai-appsec-harness/SKILL.md",
    ".claude/skills/ai-appsec-harness/SKILL.md",
]

REQUIRED_SELF_CONTROLS = {"AIH-010", "AIH-011", "AIH-012"}

RISKY_PATTERNS = [
    (re.compile(r"\bignore\s+(all\s+)?(previous|prior|above)\s+instructions\b", re.I), "instruction override language"),
    (re.compile(r"\bdisable\s+(security|safety|approval|approvals|guardrails)\b", re.I), "guardrail-disable language"),
    (re.compile(r"\b(curl|wget)\b[^\n|]*\|\s*(sh|bash|python3?)\b", re.I), "network download piped to interpreter"),
    (re.compile(r"\brm\s+-rf\s+(/|\$HOME|~|\.)", re.I), "destructive recursive delete"),
    (re.compile(r"\bchmod\s+777\b", re.I), "overly permissive chmod"),
    (re.compile(r"\bsudo\b", re.I), "privileged command"),
    (re.compile(r"\b(send|upload|exfiltrate)\b[^\n]*(secret|token|credential|key)s?\b", re.I), "secret exfiltration language"),
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Verify AI AppSec Harness import surfaces and self-protection controls."
    )
    parser.add_argument(
        "--root",
        type=Path,
        default=Path.cwd(),
        help="Harness repository root. Defaults to current directory.",
    )
    return parser.parse_args()


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def strip_frontmatter(text: str) -> str:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return text.strip()
    for index, line in enumerate(lines[1:], start=1):
        if line.strip() == "---":
            return "\n".join(lines[index + 1 :]).strip()
    return text.strip()


def check_required_files(root: Path, errors: list[str]) -> None:
    for relative in REQUIRED_FILES:
        path = root / relative
        if not path.is_file():
            errors.append(f"Missing required harness file: {relative}")


def check_agent_surfaces(root: Path, errors: list[str]) -> None:
    for relative in AGENT_SURFACES:
        path = root / relative
        if not path.is_file():
            continue

        text = read_text(path)
        for pattern, label in RISKY_PATTERNS:
            if pattern.search(text):
                errors.append(f"{relative} contains risky {label}.")

        mode = path.stat().st_mode
        if mode & (stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH):
            errors.append(f"{relative} is executable; agent guidance should be data, not runnable code.")


def check_claude_imports(root: Path, errors: list[str]) -> None:
    path = root / "CLAUDE.md"
    if not path.is_file():
        return

    allowed = {"@AGENTS.md"}
    for line_number, line in enumerate(read_text(path).splitlines(), start=1):
        stripped = line.strip()
        if stripped.startswith("@") and stripped not in allowed:
            errors.append(
                f"CLAUDE.md:{line_number} imports {stripped!r}; only @AGENTS.md is allowed by default."
            )


def check_skill_parity(root: Path, errors: list[str]) -> None:
    codex = root / ".agents/skills/ai-appsec-harness/SKILL.md"
    claude = root / ".claude/skills/ai-appsec-harness/SKILL.md"
    if not codex.is_file() or not claude.is_file():
        return

    codex_body = strip_frontmatter(read_text(codex))
    claude_body = strip_frontmatter(read_text(claude))
    if codex_body != claude_body:
        errors.append("Codex and Claude AI AppSec Harness skill bodies differ.")

    for relative in [codex, claude]:
        for line_number, line in enumerate(read_text(relative).splitlines(), start=1):
            if line.lstrip().startswith("!`"):
                errors.append(f"{relative.relative_to(root)}:{line_number} uses dynamic command injection.")


def check_catalog(root: Path, errors: list[str]) -> None:
    path = root / "data/control-catalog.seed.json"
    if not path.is_file():
        return

    try:
        catalog = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        errors.append(f"Invalid JSON in {path.relative_to(root)}: {exc}")
        return

    control_ids = {
        control.get("id")
        for control in catalog.get("controls", [])
        if isinstance(control, dict)
    }
    missing = sorted(REQUIRED_SELF_CONTROLS - control_ids)
    if missing:
        errors.append(f"Missing harness self-protection controls: {', '.join(missing)}")


def check_required_guardrails(root: Path, errors: list[str]) -> None:
    agents = root / "AGENTS.md"
    if not agents.is_file():
        return

    text = read_text(agents).lower()
    required_phrases = [
        "do not claim aisvs",
        "human approval",
        "untrusted",
        "primary standards",
    ]
    for phrase in required_phrases:
        if phrase not in text:
            errors.append(f"AGENTS.md is missing required guardrail phrase: {phrase!r}")


def main() -> int:
    args = parse_args()
    root = args.root.resolve()
    errors: list[str] = []

    check_required_files(root, errors)
    check_agent_surfaces(root, errors)
    check_claude_imports(root, errors)
    check_skill_parity(root, errors)
    check_catalog(root, errors)
    check_required_guardrails(root, errors)

    if errors:
        print("AI AppSec Harness integrity check failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("AI AppSec Harness integrity check passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
