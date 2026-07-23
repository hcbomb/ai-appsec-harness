# AI AppSec Harness

Engineer-first AI AppSec preflight resources for hardening AI clients, LLM applications, RAG systems, MCP/tool-using workflows, and autonomous or semi-autonomous agents.

This repository turns community AI security references into an operational AppSec workflow for:

- running pre-Security AI AppSec preflights from local repository evidence;
- threat modeling AI-enabled systems;
- mapping engineering evidence to versioned OWASP AISVS-style verification;
- preparing evidence-backed AppSec review and attestation material;
- building repeatable review harnesses for AI clients and agents.

## Audience

- AppSec practitioners who need a repeatable AI security review motion.
- Engineering cohorts building AI clients, agents, RAG applications, tool-using workflows, or model integrations.
- Security governance stakeholders who need evidence-based attestations instead of slideware.

## Quick Start

Open your project in Codex, Claude Code, or another Agent Skills-compatible coding agent and ask:

```text
Run the AI AppSec preflight on this project.
```

The agent should inspect local evidence first, label facts versus assumptions, and produce one Markdown report with:

- preflight summary;
- system model;
- threat model;
- evidence gaps;
- concrete security tests;
- ticket-ready backlog;
- residual risk and revalidation triggers.

Compact example input:

```text
Run the AI AppSec preflight on this RAG assistant before Security review.
It answers internal engineering questions from wiki pages and runbooks.
```

Abbreviated output:

```text
# AI AppSec Preflight: Engineering Knowledge Assistant

## A. Preflight Summary
- Review depth: standard
- Release blocker: retrieval authorization evidence is missing.
- Important fix: add poisoned-document and cross-team retrieval tests.

## C. Threat Model
T-RAG-001: indirect prompt injection through retrieved content.
Mitigation decision: require untrusted-content labeling and regression tests.

## E. Security Tests
TEST-RAG-001: insert hostile instructions into an indexed document and verify
retrieved text cannot override trusted instructions.

## F. Engineering Backlog
Add RAG poisoning regression coverage. Release gate: build.
```

To use this harness in a target repository:

1. Open this repo in the AI tool, or vendor it into a target repo as `.ai-appsec-harness/`.
2. If this is a vendored or updated copy, run `python3 tools/verify-harness-integrity.py`.
3. Ask: `Run the AI AppSec preflight on this project.`
4. Answer only high-value blocking questions. The agent should continue with labeled assumptions when a question is not blocking.
5. For implementation work, use `templates/ai-code-assistant-request.md` to give coding agents explicit security, dependency, approval, test, and self-review expectations.

Codex can use `AGENTS.md` and `.agents/skills/ai-appsec-harness/SKILL.md`. Claude Code can use `CLAUDE.md` and `.claude/skills/ai-appsec-harness/SKILL.md`.

See [docs/agent-tool-import.md](docs/agent-tool-import.md) for import patterns, target-repo snippets, expected inputs, and guardrails.

## What This Operationalizes

- Shostack's Four Questions as the simple engineer-facing report narrative.
- OWASP MAESTRO as the primary AI threat modeling method for agentic, RAG, MCP, and multi-layer AI architectures.
- OWASP AISVS 1.0 as the versioned verification backbone.
- OWASP Top 10 for Agentic Applications and OWASP Top 10 for LLM and GenAI Applications as risk language engineers already recognize.
- MITRE ATLAS for concrete adversary techniques and test scenarios.
- OWASP ASVS 5.0.0 for conventional web/API security when an application or API is in scope.
- Official MCP security and authorization guidance when MCP is detected.
- OpenSSF Security-Focused Guide for AI Code Assistant Instructions as an overlay for safer engineer prompts, coding-agent instruction files, generated-code review, dependency discipline, and AI-assisted secure coding.
- OpenSSF secure coding, SCM, npm, Python, and C/C++ compiler-hardening guides as language and platform overlays when the target stack matches.
- AI Defense Matrix as a leadership and roadmap view for AI asset classes across Govern, Identify, Protect, Detect, Respond, and Recover.
- CSA AI Controls Matrix, CSA AI Safety, NIST AI RMF, and NIST AI 600-1 as optional governance and assurance overlays.
- Community "awesome AI" repositories as discovery feeds for tools, patterns, examples, and research.

This repo intentionally does not fork entire upstream standards. It keeps canonical links, seed mappings, and import-ready data shapes so future harnesses can ingest authoritative upstream controls.

See [ACKNOWLEDGEMENTS.md](ACKNOWLEDGEMENTS.md) for credited standards, frameworks, threat modeling resources, and community discovery feeds.

## Python Helpers

The no-dependency Python harness is deterministic. It can validate and render structured preflight packages, or render starter control/evidence gap reports from structured intake files. It does not inspect a repository or perform the complete semantic threat model by itself.

Render an included preflight example:

```bash
PYTHONPATH=harness python3 -m ai_appsec_harness.cli \
  --preflight examples/preflight/mcp-agent.preflight.json \
  --out build/mcp-agent-preflight.md
```

Render a structured intake gap report:

```bash
PYTHONPATH=harness python3 -m ai_appsec_harness.cli \
  --intake examples/ai-client-intake.example.json \
  --catalog data/control-catalog.seed.json \
  --out build/ai-client-attestation.md
```

Generated reports are not compliance certificates. They are evidence gap analyses and hardening plans that can support a later human AppSec review or attestation.

## Repository Map

- `docs/reference-catalog.md` - curated sources and how each should feed AppSec work.
- `docs/agent-tool-import.md` - how to import this harness into Codex, Claude Code, or another AI tool.
- `docs/harness-self-hardening.md` - AISVS- and OpenSSF-informed protections for the harness itself.
- `docs/preflight-workflow.md` - engineer-first AI AppSec preflight workflow and report expectations.
- `docs/ai-code-assistant-guidance.md` - OpenSSF-informed overlay for safer AI coding-agent instructions and secure implementation requests.
- `docs/threat-modeling-maestro.md` - primary MAESTRO-first AI threat modeling workflow.
- `docs/ai-defense-matrix.md` - leadership and coverage overlay for AI defensive asset classes.
- `docs/harness-design.md` - target architecture for agents, harnesses, and review gates.
- `docs/threat-modeling-stride.md` - secondary STRIDE fallback and translation guide.
- `docs/weekly-monitoring.md` - weekly AI + security monitoring workflow and triage criteria.
- `docs/aisvs-operationalization.md` - how to turn AISVS into engineering-ready evidence checks.
- `data/reference-catalog.yml` - machine-readable reference catalog.
- `data/control-catalog.seed.json` - starter harness controls for AI clients and agents.
- `examples/preflight/` - structured preflight packages for chatbot, RAG, MCP/tool-agent, and hostile-repo scenarios.
- `examples/ai-client-intake.example.json` - sample input for the harness.
- `examples/harness-import-intake.example.json` - sample intake for reviewing the harness import path itself.
- `harness/` - no-dependency Python helpers for preflight validation/rendering and structured intake gap reports.
- `agents/` - agent roles and prompts for threat modeling, evidence collection, CSA mapping, and attestation.
- `.agents/skills/ai-appsec-harness/` - Codex repo skill for AI AppSec review workflows.
- `.claude/skills/ai-appsec-harness/` - Claude Code project skill for AI AppSec review workflows.
- `tools/verify-harness-integrity.py` - local sanity check for import-sensitive harness files.
- `SECURITY.md` - public-safe vulnerability reporting guidance.
- `templates/` - preflight, AI code assistant request, review, threat model, and attestation templates.

## Operating Principles

- Evidence before assertion.
- Model the system before debating controls.
- Human approval for agentic actions, sensitive data access, and production changes.
- Clear source-to-control mapping.
- Reproducible reports from versioned inputs.
- Engineering-readable output with AppSec-grade traceability.

## Threat Modeling Tiers

- Baseline: perform a minimum viable OWASP MAESTRO assessment with business context, AI architecture layers, agentic risk factors, trust boundaries, asset flows, key threats, mitigations, evidence requests, and residual-risk notes.
- Advanced: perform the full OWASP MAESTRO review across business context, architecture, threat actors, trust boundaries, asset flows, agentic risk factors, layer threats, cross-layer threats, mitigations, code/evidence validation, residual risk, and final documentation.
- Secondary: translate the highest-priority findings into STRIDE when that makes the result easier for broad AppSec, engineering, or leadership audiences to consume.

## Current Status

Alpha scaffold with agent-import support, engineer-first preflight workflow, AISVS-oriented operational controls, weekly monitoring guidance, and deterministic Python helpers. The seed catalog now includes versioned AISVS 1.0 traceability for active controls, but it still does not claim conformance or certification.
