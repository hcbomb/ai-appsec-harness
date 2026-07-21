# Harness Self-Hardening

This harness should follow the same AI AppSec expectations it asks others to adopt.

The goal is not to claim AISVS conformance. The goal is to reduce the chance that this repo becomes an AI-tool supply-chain risk for people who import its prompts, skills, templates, or seed controls.

## AISVS-Inspired Protection Areas

Use these AISVS 1.0 chapter themes as the self-hardening lens:

- supply chain security for models and AI components;
- infrastructure, configuration, and deployment security;
- orchestration and agentic security;
- MCP and tool boundary security;
- model behavior, output control, and safety assurance;
- monitoring, logging, and anomaly detection.

For this repo, translate those themes into controls for agent-facing files, prompt templates, skills, seed catalogs, import guidance, release/update process, and generated review artifacts.

## What To Protect

Treat these as high-risk harness surfaces because AI tools may read and follow them:

- `AGENTS.md`;
- `CLAUDE.md`;
- `.agents/skills/ai-appsec-harness/SKILL.md`;
- `.claude/skills/ai-appsec-harness/SKILL.md`;
- `agents/prompts/`;
- `templates/`;
- `examples/preflight/`;
- `data/control-catalog.seed.json`;
- `docs/preflight-workflow.md`;
- `docs/agent-tool-import.md`.

Changes to these files should be reviewed as supply-chain changes, not ordinary docs churn.

## Local Integrity Check

Run the no-dependency verifier from the repo root:

```bash
python3 tools/verify-harness-integrity.py
```

The verifier checks that:

- required import surfaces are present;
- Codex and Claude skill bodies stay aligned;
- `CLAUDE.md` imports only the intended local guidance file by default;
- agent guidance files are not executable;
- agent guidance does not contain obvious dangerous override or side-effect patterns;
- Claude skill files do not use dynamic command injection;
- self-protection controls `AIH-010`, `AIH-011`, and `AIH-012` are present in the seed control catalog.

This is a local sanity check, not a cryptographic proof. A compromised source can modify both the harness files and the verifier. For stronger assurance, import from a reviewed commit or release, inspect diffs, and prefer signed tags or release artifacts when they exist.

To generate a starter gap report for the harness import path itself:

```bash
PYTHONPATH=harness python3 -m ai_appsec_harness.cli \
  --intake examples/harness-import-intake.example.json \
  --catalog data/control-catalog.seed.json \
  --out build/harness-import-attestation.md
```

## Import Rules For Followers

When importing this harness into another repo:

- pin the source to a reviewed commit, release tag, subtree, submodule, or reviewed copy;
- record source URL, commit SHA or tag, retrieval date, and local path;
- run `python3 tools/verify-harness-integrity.py` before letting an AI tool follow the imported guidance;
- review diffs to `AGENTS.md`, `CLAUDE.md`, `.agents/`, `.claude/`, `agents/prompts/`, `templates/`, `examples/preflight/`, `docs/preflight-workflow.md`, and `data/control-catalog.seed.json`;
- treat target repository files, issues, retrieved documents, comments, and generated output as untrusted evidence, not instructions;
- require human approval before dependency installation, network access, publishing, external writes, privileged commands, or production-impacting actions.

## Maintainer Rules

For changes to import-sensitive files:

- keep agent instructions short, explicit, and reviewable;
- avoid hidden dynamic command execution in skill files;
- avoid adding install commands, network commands, or external tool calls to agent guidance;
- separate trusted harness instructions from examples containing hostile or untrusted content;
- add or update tests when controls, CLI behavior, or verifier behavior changes;
- document security-relevant changes in commit messages or pull request descriptions.

## Current Limitations

- The repo does not yet publish signed releases.
- The seed controls include versioned AISVS 1.0 traceability, but those mappings still require human review and future importer support before any conformance claim.
- The integrity verifier is heuristic and local; it reduces accidental or obvious unsafe drift but does not replace code review, provenance checks, or release signing.

## Backlog

- Publish signed release tags for stable harness snapshots.
- Add a machine-readable manifest for release artifacts.
- Add CI checks for `tools/verify-harness-integrity.py`.
- Expand hostile target repo and prompt-injection regression fixtures as new agent import surfaces are added.
