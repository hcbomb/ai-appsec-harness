# Harness Design

The harness should make AI AppSec reviews repeatable without flattening the nuance out of them.

## North Star

Given an AI system intake, the harness produces:

- an AI threat model;
- an applicable control set;
- an AISVS-oriented evidence checklist;
- CSA AI control mapping notes;
- OWASP GenAI risk mapping;
- hardening actions for engineering;
- an attestation-ready report with gaps and residual risk.

## Review Flow

1. Intake
   - Capture system purpose, owners, lifecycle stage, architecture, model providers, tools, retrieval sources, data classes, identities, environments, and release gate needs.
2. Classify
   - Identify whether the system is an AI client, agent, RAG app, model-hosting service, model-training pipeline, evaluation harness, or internal productivity tool.
3. Threat Model
   - Use the baseline assisted STRIDE flow for normal reviews and the advanced Shostack-style flow for high-impact or agentic systems.
   - Model trust boundaries, prompt boundaries, data flows, tool calls, delegated authority, identity transitions, external actions, current/target state, compensating controls, and abuse cases.
4. Map Controls
   - Select applicable controls from AISVS, OWASP GenAI, CSA AICM, and local AppSec requirements.
5. Collect Evidence
   - Request engineering artifacts, test results, architecture diagrams, policy decisions, logs, and runtime configuration.
6. Evaluate
   - Determine whether evidence is present, reviewable, stale, incomplete, or contradicted by implementation.
7. Harden
   - Produce engineering actions that reduce risk and can be regression-tested.
8. Attest
   - Generate an attestation package that states scope, evidence, gaps, exceptions, compensating controls, and residual risk.

## Agent Import Surface

The harness should be usable by AI coding and security tools before every workflow is automated in Python.

Supported repo-level import surfaces:

- `AGENTS.md` for Codex and other agents that read repository instructions;
- `CLAUDE.md` for Claude Code;
- `.agents/skills/ai-appsec-harness/SKILL.md` for Codex skill discovery;
- `.claude/skills/ai-appsec-harness/SKILL.md` for Claude Code skill discovery;
- `docs/agent-tool-import.md` for target-repo integration patterns.
- `docs/harness-self-hardening.md` and `tools/verify-harness-integrity.py` for AISVS-inspired self-protection checks.

Agent-imported reviews should produce human-readable artifacts first: intake gaps, STRIDE abuse cases, evidence requests, backlog items, hardening actions, and attestation caveats. The Python harness can then provide deterministic report generation when structured JSON inputs are available.

## Threat Modeling Depth

Baseline reviews must answer:

- what is changing;
- why the business needs it;
- who owns it;
- what systems, environments, identities, and data are involved;
- what STRIDE threats matter;
- what controls, gaps, compensating controls, and decisions exist.

Advanced reviews must also answer Adam Shostack's four-question frame:

- what are we working on;
- what can go wrong;
- what are we going to do about it;
- did we do a good job.

For AI clients and agents, advanced reviews must include prompt/context boundaries, model/provider boundaries, retrieval poisoning, tool authorization, delegated authority, output validation, logging/auditability, rollback, and monitoring.

## Agent Roles

- Intake Agent: normalizes engineering input into a review-ready schema.
- Threat Model Agent: turns architecture and use cases into abuse cases and control priorities.
- Evidence Agent: maps artifacts to control requirements and identifies gaps.
- CSA Mapper Agent: maps technical evidence to CSA AI governance and assurance language.
- Attestation Agent: drafts a scoped, evidence-backed report for AppSec and engineering review.

Agents should recommend actions, not silently perform sensitive changes. Any agent with tool access must have explicit authorization boundaries, audit logging, and human approval for external side effects.

## Evidence States

- `available` - evidence exists and is attached or linked.
- `partial` - evidence exists but does not fully answer the control.
- `missing` - evidence is not available.
- `stale` - evidence exists but is likely outdated.
- `not_applicable` - control does not apply to this system and the rationale is recorded.
- `accepted_risk` - gap is explicitly accepted by the accountable owner.

## Release Gate Pattern

Use three gates:

- Design gate: architecture, data flows, threat model, and risk tier are reviewed.
- Build gate: controls, tests, prompts, tool permissions, and logging are implemented.
- Run gate: monitoring, abuse detection, incident response, and periodic reevaluation are in place.

The current Python harness implements a small slice of this model: intake, control selection, evidence gap analysis, and Markdown report generation. The agent-import surface implements the broader human-led review workflow by making the prompts, templates, controls, and guardrails available directly to AI tools.
