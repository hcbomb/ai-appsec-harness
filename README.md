# AI AppSec Harness

Practitioner-focused resources for hardening AI clients, LLM applications, RAG systems, and autonomous or semi-autonomous agents.

This repository turns community AI security references into an operational AppSec workflow for:

- threat modeling AI-enabled systems;
- mapping engineering evidence to OWASP AISVS-style verification;
- preparing OWASP and CSA AI attestations;
- building repeatable review harnesses for AI clients and agents.

## Audience

- AppSec practitioners who need a repeatable AI security review motion.
- Engineering cohorts building AI clients, agents, RAG applications, tool-using workflows, or model integrations.
- Security governance stakeholders who need evidence-based attestations instead of slideware.

## What This Operationalizes

- OWASP Artificial Intelligence Security Verification Standard (AISVS) as the primary verification backbone.
- MAESTRO as the primary AI threat modeling method for agentic, RAG, MCP, and multi-layer AI architectures.
- OWASP GenAI Security Project and OWASP Top 10 for LLM and GenAI applications as risk language engineers already recognize.
- AI Defense Matrix as a leadership and roadmap view for AI asset classes across Govern, Identify, Protect, Detect, Respond, and Recover.
- CSA AI Controls Matrix and CSA AI Safety work as the governance and control mapping layer.
- NIST AI RMF and NIST AI 600-1 as risk management lifecycle and GenAI risk framing.
- Community "awesome AI" repositories as discovery feeds for tools, patterns, examples, and research.

This repo intentionally does not fork entire upstream standards. It keeps canonical links, seed mappings, and import-ready data shapes so future harnesses can ingest authoritative upstream controls.

See [ACKNOWLEDGEMENTS.md](ACKNOWLEDGEMENTS.md) for credited standards, frameworks, threat modeling resources, and community discovery feeds.

## Quick Start

Use the repo as an AI AppSec harness inside Codex, Claude Code, or another AI coding/security agent:

1. Open this repo in the AI tool, or vendor it into a target repo as `.ai-appsec-harness/`.
2. If this is a vendored or updated copy, run `python3 tools/verify-harness-integrity.py`.
3. Ask the tool to use the AI AppSec Harness for an AI client, LLM app, RAG, MCP, model-provider, or agent review.
4. Provide existing architecture notes, system intake, data flows, model/provider inventory, tool inventory, prompts, tests, logs, or monitoring evidence.
5. Ask for scope, assumptions, MAESTRO layer threats, optional STRIDE translation, AI Defense Matrix coverage gaps, applicable controls, evidence gaps, hardening actions, test ideas, backlog items, and attestation caveats.

Codex can use `AGENTS.md` and `.agents/skills/ai-appsec-harness/SKILL.md`. Claude Code can use `CLAUDE.md` and `.claude/skills/ai-appsec-harness/SKILL.md`.

See [docs/agent-tool-import.md](docs/agent-tool-import.md) for import patterns, target-repo snippets, expected inputs, and guardrails.

## Python Proof Of Concept

The no-dependency Python harness remains available for structured JSON intake files:

```bash
PYTHONPATH=harness python3 -m ai_appsec_harness.cli \
  --intake examples/ai-client-intake.example.json \
  --catalog data/control-catalog.seed.json \
  --out build/ai-client-attestation.md
```

The generated report is not a compliance certificate. It is an evidence gap analysis and hardening plan that can support a later attestation.

## Repository Map

- `docs/reference-catalog.md` - curated sources and how each should feed AppSec work.
- `docs/agent-tool-import.md` - how to import this harness into Codex, Claude Code, or another AI tool.
- `docs/harness-self-hardening.md` - AISVS-inspired protections for the harness itself.
- `docs/threat-modeling-maestro.md` - primary MAESTRO-first AI threat modeling workflow.
- `docs/ai-defense-matrix.md` - leadership and coverage overlay for AI defensive asset classes.
- `docs/harness-design.md` - target architecture for agents, harnesses, and review gates.
- `docs/threat-modeling-stride.md` - secondary STRIDE fallback and translation guide.
- `docs/weekly-monitoring.md` - weekly AI + security monitoring workflow and triage criteria.
- `docs/aisvs-operationalization.md` - how to turn AISVS into engineering-ready evidence checks.
- `data/reference-catalog.yml` - machine-readable reference catalog.
- `data/control-catalog.seed.json` - starter harness controls for AI clients and agents.
- `examples/ai-client-intake.example.json` - sample input for the harness.
- `examples/harness-import-intake.example.json` - sample intake for reviewing the harness import path itself.
- `harness/` - no-dependency Python proof of concept.
- `agents/` - agent roles and prompts for threat modeling, evidence collection, CSA mapping, and attestation.
- `.agents/skills/ai-appsec-harness/` - Codex repo skill for AI AppSec review workflows.
- `.claude/skills/ai-appsec-harness/` - Claude Code project skill for AI AppSec review workflows.
- `tools/verify-harness-integrity.py` - local sanity check for import-sensitive harness files.
- `SECURITY.md` - public-safe vulnerability reporting guidance.
- `templates/` - review, threat model, and attestation templates.

## Operating Principles

- Evidence before assertion.
- Model the system before debating controls.
- Human approval for agentic actions, sensitive data access, and production changes.
- Clear source-to-control mapping.
- Reproducible reports from versioned inputs.
- Engineering-readable output with AppSec-grade traceability.

## Threat Modeling Tiers

- Baseline: perform a minimum viable MAESTRO assessment with business context, AI architecture layers, trust boundaries, asset flows, key threats, mitigations, evidence requests, and residual-risk notes.
- Advanced: perform the full MAESTRO review across business context, architecture, threat actors, trust boundaries, asset flows, layer threats, mitigations, code/evidence validation, residual risk, and final documentation.
- Secondary: translate the highest-priority findings into STRIDE when that makes the result easier for broad AppSec, engineering, or leadership audiences to consume.

## Current Status

Alpha scaffold with agent-import support, AISVS-oriented operational controls, weekly monitoring guidance, and a small Python proof of concept. Future work should replace candidate AISVS alignments with authoritative upstream AISVS requirement IDs, versions, and import metadata once the importer is implemented.
