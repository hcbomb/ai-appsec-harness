# Threat Modeling With MAESTRO

This repo uses MAESTRO as the primary AI threat modeling workflow for AI clients, LLM applications, RAG systems, MCP/tool-using workflows, and autonomous or semi-autonomous agents.

STRIDE remains useful, but it is secondary: use it as a consumer-friendly translation layer, a completeness check, or a fallback when the audience expects traditional AppSec categories.

## Why MAESTRO First

Traditional threat modeling usually starts with components, trust boundaries, and data flows, then applies a category system such as STRIDE. That still helps, but AI systems add architecture-specific risks that are easy to miss when the model starts too generically:

- model/provider trust and configuration drift;
- prompt, memory, context, and retrieval boundaries;
- non-deterministic planning and output;
- tools, plugins, MCP servers, and external actions;
- agent identity, delegation, and approval chains;
- observability, evaluation, and runtime policy feedback loops;
- ecosystem and supply-chain dependencies.

MAESTRO gives the harness an AI-native decomposition first. STRIDE can then make the resulting findings easier for broad AppSec, engineering, and leadership audiences to consume.

## Review Tiers

### Tier 1: Minimum Viable MAESTRO

Use this tier for fast design reviews, project intake, exception support, and early AI feature reviews.

Minimum steps:

1. Capture business context, system purpose, owners, lifecycle stage, data sensitivity, and requested output.
2. Map the architecture across MAESTRO layers.
3. Identify trust boundaries and asset flows across prompt, retrieval, model, tool, identity, deployment, and monitoring paths.
4. Identify the highest-risk threats and abuse cases per relevant layer.
5. Produce mitigations, evidence requests, backlog items, and residual-risk notes.
6. Translate the highest-priority findings into STRIDE only when it helps the audience understand them.

### Tier 2: Full MAESTRO Review

Use this tier when the system is agentic, production-facing, externally integrated, sensitive, regulated, customer-visible, or capable of privileged/external action.

Full steps:

1. Business context analysis.
2. Architecture and component analysis.
3. Threat actor analysis.
4. Trust boundary analysis.
5. Asset and data-flow analysis.
6. MAESTRO layer threat identification.
7. Mitigation planning.
8. Code/configuration/evidence validation.
9. Residual risk analysis.
10. Output generation and documentation.

## MAESTRO Layer Map

Use this layer map as the harness default. If an upstream MAESTRO source updates naming, keep this local map stable until the repo intentionally revises it.

| Layer | Focus | Harness Lens |
| --- | --- | --- |
| L1 Foundation Models | Base models, consumed model APIs, fine-tuned models, model cards, model registry assumptions. | Provider trust, model selection, retention/training-use settings, model behavior assumptions, jailbreak resistance, model supply chain. |
| L2 Data Operations | Training data, fine-tuning data, prompts, RAG content, vector stores, memory, logs, evaluation datasets. | Data classification, poisoning, leakage, freshness, provenance, retention, cross-tenant retrieval, canary secrets. |
| L3 Agent Frameworks | Agent runtime, orchestration, planners, skills, tool definitions, system prompts, MCP clients, memory managers. | Instruction hierarchy, prompt boundaries, tool schemas, approval gates, plan validation, agent framework dependencies. |
| L4 Deployment And Infrastructure | Hosting, containers, CI/CD, secrets, network paths, cloud services, inference endpoints, model-loading pipeline. | Workload hardening, environment boundaries, secret handling, deployment drift, artifact integrity, rollback and kill switches. |
| L5 Evaluation And Observability | Evals, red-team tests, monitoring, traces, audit logs, policy decisions, drift and anomaly detection. | Prompt/tool abuse telemetry, blocked actions, regression tests, incident triggers, evidence quality, replayability. |
| L6 Security And Compliance | Governance, risk acceptance, policy, privacy, regulatory obligations, control mapping, attestations. | AISVS, OWASP GenAI, CSA, NIST AI RMF, EU AI Act overlays, exceptions, residual risk, reviewer decisions. |
| L7 Agent Ecosystem | Multi-agent coordination, third-party agents, plugins, external services, human handoffs, ecosystem protocols. | Delegation, agent identity, inter-agent trust, MCP/tool ecosystems, external side effects, confused-deputy paths. |

## MAESTRO Threat Questions

Ask these questions for each relevant layer:

- What trusted and untrusted inputs can influence this layer?
- What decisions, actions, or outputs can this layer change?
- What identities, permissions, secrets, or delegated authority exist here?
- What can be poisoned, tampered with, spoofed, leaked, replayed, or denied?
- What telemetry proves the control worked or failed?
- What would make this layer unsafe if the model behaves unexpectedly?
- What happens if a lower layer is compromised and a higher layer trusts it?
- What happens if a higher layer delegates unsafe authority to a lower layer?

## STRIDE Translation

After identifying MAESTRO threats, translate significant findings into STRIDE only as needed:

| STRIDE Category | Use As A Translation For |
| --- | --- |
| Spoofing | Agent identity confusion, model/provider impersonation, forged tool responses, tenant or user confusion. |
| Tampering | Prompt/context mutation, retrieval poisoning, tool argument tampering, model/config drift, artifact modification. |
| Repudiation | Missing proof of prompt, retrieval, approval, tool call, model response, or generated change. |
| Information Disclosure | Leakage through prompts, embeddings, model output, logs, providers, memory, retrieval, or generated artifacts. |
| Denial of Service | Token, quota, cost, tool-loop, retrieval, provider, or support exhaustion. |
| Elevation of Privilege | Agent/tool overreach, delegated authority expansion, service-account abuse, approval bypass, MCP confused-deputy paths. |

## Minimum Outputs

A MAESTRO-first threat model should include:

- scope, owners, assumptions, lifecycle stage, and requested output;
- MAESTRO layer inventory;
- AI Defense Matrix asset-class coverage notes when leadership or roadmap planning is needed;
- trust boundaries and asset/data flows;
- threat actors and abuse cases;
- MAESTRO layer threats with impact, likelihood, controls, gaps, and mitigations;
- STRIDE translation for the top findings, if useful;
- evidence requests and test ideas;
- backlog items, owners, and priority;
- residual risk and accepted-risk path;
- revalidation triggers.

## Definition Of Done

A threat model is ready for AppSec review when:

- MAESTRO layers relevant to the system were considered;
- missing layers or not-applicable layers have rationale;
- significant cross-layer threats are captured;
- external actions, privileged tools, memory, retrieval, identity, and monitoring were reviewed where applicable;
- the highest-priority threats map to mitigations, tests, backlog items, or accepted-risk decisions;
- STRIDE was used only where it improves communication or catches a gap;
- the output can be understood by engineering, AppSec, governance, and incident response.

