---
name: ai-appsec-harness
description: Use for AI AppSec review, LLM threat modeling, AISVS-oriented evidence mapping, RAG or agent hardening, CSA AI mapping, and attestation drafting.
---

# AI AppSec Harness

Use this skill when reviewing an AI client, LLM application, RAG workflow, model integration, MCP/tool-using workflow, or autonomous/semi-autonomous agent.

## Inputs

Prefer existing artifacts before asking for new ones:

- product or engineering notes;
- architecture, trust boundary, data flow, identity flow, retrieval flow, or agent/tool flow diagrams;
- model/provider inventory;
- tool, plugin, MCP server, API, and external action inventory;
- data classification and retention notes;
- prompt, policy, test, logging, monitoring, and incident-response evidence.

If structured input is needed, use `templates/system-intake.md` or `examples/ai-client-intake.example.json`.

## Procedure

1. Establish scope, owner, lifecycle stage, target state, and requested output.
2. Classify the system: AI client, agent, RAG app, LLM app, model service, model pipeline, or evaluation harness.
3. Select threat-model depth using `docs/threat-modeling-stride.md`.
4. Identify AI-specific trust boundaries: prompt/context, retrieval, model/provider, tool/action, identity, data, logging, and human approval.
5. Apply STRIDE with AI abuse cases: prompt injection, indirect prompt injection, retrieval poisoning, sensitive data leakage, unauthorized tool invocation, excessive agency, unsafe output handling, provider/config drift, and missing regression tests.
6. Map evidence to `data/control-catalog.seed.json` and `docs/aisvs-operationalization.md`.
7. Use role prompts in `agents/prompts/` when a focused subtask is needed.
8. Draft outputs with `templates/threat-model.md`, `templates/aisvs-attestation.md`, or `templates/engineering-cohort-brief.md`.

## Output Requirements

Return:

- scope, assumptions, and missing inputs;
- threat-model tier recommendation;
- STRIDE table or summary with AI-specific abuse cases;
- applicable controls and evidence status;
- hardening actions and test/evidence ideas;
- backlog items with priority and owner placeholder;
- attestation caveats and residual risk.

## Guardrails

- Keep all repo-ready content public-safe and organization-neutral.
- Do not claim conformance or certification.
- Separate generated analysis from human decisions.
- Prefer primary sources for standards or durable references.
- Do not silently access sensitive data or perform external side effects.
- Require human approval for privileged, destructive, regulated, financial, customer-visible, or production-impacting actions.

