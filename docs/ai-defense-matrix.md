# AI Defense Matrix Overlay

Use the AI Defense Matrix as the harness's leadership and program-coverage view.

MAESTRO decomposes the AI architecture for threat modeling. The AI Defense Matrix helps organizations explain what needs defending, who owns it, and where control coverage is thin across the NIST CSF 2.0 functions: Govern, Identify, Protect, Detect, Respond, and Recover.

## When To Use It

Use this overlay when the review needs:

- leadership communication;
- security roadmap planning;
- ownership mapping;
- control coverage comparison;
- vendor/tool evaluation;
- portfolio-level AI defense gap analysis.

It should not replace MAESTRO threat modeling or AISVS evidence checks. It is a way to make the defense surface visible.

## Asset Classes

Use these rows as the default asset classes:

| Asset Class | Harness Interpretation |
| --- | --- |
| AI-Workload Platforms | Inference servers, training platforms, vector database platforms, build/runtime platforms, and model-loading supply chain. |
| AI Orchestration Tools | Agent frameworks, plugins, skills, hooks, system prompts, harnesses, MCP clients, and orchestration configuration. |
| AI-Generated Code | AI-authored code, infrastructure as code, tests, reviews, pull requests, scripts, and applications. |
| AI Gateways And Routers | MCP gateways, MCP proxies, LLM routers, AI egress controls, model registry traffic, and outbound AI-service paths. |
| AI Models | Self-hosted models, consumed third-party models, model weights, fine-tuning checkpoints, model cards, registries, and AIBOMs. |
| Training Data | Training, fine-tuning, continued-learning, synthetic, and evaluation datasets. |
| Runtime AI Data | Prompts, inference inputs, RAG content, vector content, persistent memory, logs, and interaction history. |
| AI Agent Identities | Agent identities, non-human principals, credentials, keys, scopes, service accounts, delegation chains, and approvals. |

## NIST CSF 2.0 Columns

For each relevant asset class, ask:

| Function | Review Question |
| --- | --- |
| Govern | Who owns policy, risk appetite, roles, exceptions, and accountability for this asset class? |
| Identify | Do we have inventory, classification, dependencies, data flows, identities, and exposure mapped? |
| Protect | What preventive controls reduce misuse, compromise, leakage, unsafe action, or supply-chain risk? |
| Detect | What telemetry, detections, evals, red-team tests, and anomaly signals reveal abuse or drift? |
| Respond | What playbooks, approval paths, containment steps, and escalation routes exist? |
| Recover | How do we rollback, disable, rotate, restore, reindex, retrain, or revalidate safely? |

## Output Format

For leadership or roadmap reviews, add this table:

| Asset Class | Govern | Identify | Protect | Detect | Respond | Recover | Owner | Gap / Backlog |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| AI-Workload Platforms |  |  |  |  |  |  |  |  |
| AI Orchestration Tools |  |  |  |  |  |  |  |  |
| AI-Generated Code |  |  |  |  |  |  |  |  |
| AI Gateways And Routers |  |  |  |  |  |  |  |  |
| AI Models |  |  |  |  |  |  |  |  |
| Training Data |  |  |  |  |  |  |  |  |
| Runtime AI Data |  |  |  |  |  |  |  |  |
| AI Agent Identities |  |  |  |  |  |  |  |  |

## How It Connects To MAESTRO

- Use OWASP MAESTRO to find architecture-specific threats, agentic risk factors, and cross-layer abuse cases.
- Use the AI Defense Matrix to show where defensive ownership and coverage are missing.
- Use AISVS to turn findings into verification evidence.
- Use CSA AI Controls Matrix and NIST AI RMF for governance and assurance language.
- Use STRIDE only as a translation layer for teams that expect traditional AppSec threat categories.

## Backlog Framing

Turn weak cells into backlog entries:

- `govern`: define owner, policy, exception path, or risk appetite;
- `identify`: inventory assets, identities, data, dependencies, or exposure;
- `protect`: implement preventive controls, guardrails, approvals, hardening, or segmentation;
- `detect`: add logs, traces, alerts, evals, red-team checks, or anomaly detection;
- `respond`: write containment, escalation, incident, and rollback playbooks;
- `recover`: test restore, rotation, rollback, reindexing, disabling, or revalidation paths.
