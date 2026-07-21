# Agent Workbench

The agent roles here are designed to support a human-led AI AppSec preflight and later AppSec review. They should gather, normalize, map, and draft. They should not silently approve risk, modify production systems, or perform sensitive external actions.

For AI tools that support repository guidance or skills, start with the import surfaces at the repo root:

- `AGENTS.md` for Codex and other tools that read AGENTS guidance;
- `CLAUDE.md` for Claude Code;
- `.agents/skills/ai-appsec-harness/SKILL.md` for Codex;
- `.claude/skills/ai-appsec-harness/SKILL.md` for Claude Code.

The role prompts in this directory are supporting prompts. Use them when a preflight needs a focused intake, threat-modeling, evidence-mapping, CSA-mapping, or attestation-drafting pass.

Before trusting a copied or updated harness, run `python3 tools/verify-harness-integrity.py` and review `docs/harness-self-hardening.md`.

## Roles

- Intake Agent: convert local evidence and engineering notes into structured intake.
- Threat Model Agent: identify abuse cases, trust boundaries, and review priorities.
- AISVS Evidence Agent: map evidence to AISVS-oriented controls and identify gaps.
- CSA Mapper Agent: translate technical evidence into CSA AI governance language.
- Attestation Agent: draft a scoped attestation package for human review after preflight evidence is available.

## Required Guardrails

- No autonomous production change.
- No hidden tool invocation.
- No unapproved access to customer, regulated, or secret data.
- Preserve source links and evidence paths.
- Mark uncertainty explicitly.
- Require named human reviewers for attestation decisions.
