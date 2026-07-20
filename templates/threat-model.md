# AI Threat Model

## Scope

- System:
- Review date:
- Reviewers:
- Lifecycle stage:
- Review tier: Minimum viable MAESTRO / Full MAESTRO / STRIDE fallback
- Requested output: Quick feedback / full assessment / exception support / architecture review / leadership summary

## MAESTRO Review Summary

| Area | Answer |
| --- | --- |
| Business context and risk appetite |  |
| Architecture scope |  |
| Threat actors |  |
| Trust boundaries |  |
| Asset and data flows |  |
| Highest-risk MAESTRO layers |  |
| Residual risk summary |  |
| STRIDE translation needed? | Yes / No |
| AI Defense Matrix overlay needed? | Yes / No |

## Request Context

- Requestor:
- Owning team:
- Business owner:
- Technical owner / SME:
- Related ticket / epic:
- Business objective:
- Delivery or review date:

## Current And Target State

- Current state:
- Target state:
- Transitional / interim state:

## Assets

| Asset | Owner | Sensitivity | Why It Matters |
| --- | --- | --- | --- |
|  |  |  |  |

## MAESTRO Layer Inventory

| Layer | In Scope? | Components / Evidence | Key Trust Boundaries | Primary Concerns |
| --- | --- | --- | --- | --- |
| L1 Foundation Models | Yes / No / N/A |  |  |  |
| L2 Data Operations | Yes / No / N/A |  |  |  |
| L3 Agent Frameworks | Yes / No / N/A |  |  |  |
| L4 Deployment And Infrastructure | Yes / No / N/A |  |  |  |
| L5 Evaluation And Observability | Yes / No / N/A |  |  |  |
| L6 Security And Compliance | Yes / No / N/A |  |  |  |
| L7 Agent Ecosystem | Yes / No / N/A |  |  |  |

## Trust Boundaries

| Boundary | Trusted Side | Untrusted Side | Controls |
| --- | --- | --- | --- |
|  |  |  |  |

## Architecture Views

| View | Link / Attachment | Notes |
| --- | --- | --- |
| System context |  |  |
| Trust zones / environments |  |  |
| IAM / access flow |  |  |
| Data flow |  |  |
| Agent / tool invocation flow |  |  |
| Retrieval ingestion / query flow |  |  |
| Infrastructure / deployment |  |  |
| Operational workflow |  |  |

## Data Flows

| Flow | Source | Sink | Data Class | Controls |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |

## AI Inventory

| Item | Provider / Owner | Scope | Approval Required | Notes |
| --- | --- | --- | --- | --- |
| Model provider |  |  |  |  |
| Agent framework |  |  |  |  |
| Tool / plugin / MCP server |  |  |  |  |
| Retrieval source |  |  |  |  |
| Prompt template |  |  |  |  |

## Abuse Cases

| Abuse Case | Actor | Impact | Existing Controls | Gaps |
| --- | --- | --- | --- | --- |
| Prompt injection |  |  |  |  |
| Sensitive data leakage |  |  |  |  |
| Unauthorized tool use |  |  |  |  |
| Retrieval poisoning |  |  |  |  |
| Unsafe generated output |  |  |  |  |
| Provider or plugin compromise |  |  |  |  |

## MAESTRO Threat Analysis

| Layer | Threat / Abuse Case | Scenario | Impact | Likelihood | Existing Controls | Gaps | Mitigation / Decision | Residual Risk |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| L1 Foundation Models |  |  |  | Low / Medium / High |  |  |  | Low / Medium / High |
| L2 Data Operations |  |  |  | Low / Medium / High |  |  |  | Low / Medium / High |
| L3 Agent Frameworks |  |  |  | Low / Medium / High |  |  |  | Low / Medium / High |
| L4 Deployment And Infrastructure |  |  |  | Low / Medium / High |  |  |  | Low / Medium / High |
| L5 Evaluation And Observability |  |  |  | Low / Medium / High |  |  |  | Low / Medium / High |
| L6 Security And Compliance |  |  |  | Low / Medium / High |  |  |  | Low / Medium / High |
| L7 Agent Ecosystem |  |  |  | Low / Medium / High |  |  |  | Low / Medium / High |

## Cross-Layer Scenarios

| Scenario | Layers Involved | Attack Path | Controls | Gaps | Decision |
| --- | --- | --- | --- | --- | --- |
| Prompt injection to tool misuse | L2 / L3 / L7 |  |  |  |  |
| RAG poisoning to unsafe output | L2 / L3 / L5 |  |  |  |  |
| Agent identity delegation failure | L3 / L6 / L7 |  |  |  |  |
| Provider or model supply-chain drift | L1 / L4 / L6 |  |  |  |  |

## STRIDE Translation

| Category | Threat | Scenario | Impact | Existing Controls | Gaps | Mitigation / Decision | Residual Risk |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Spoofing |  |  |  |  |  |  | Low / Medium / High |
| Tampering |  |  |  |  |  |  | Low / Medium / High |
| Repudiation |  |  |  |  |  |  | Low / Medium / High |
| Information Disclosure |  |  |  |  |  |  | Low / Medium / High |
| Denial of Service |  |  |  |  |  |  | Low / Medium / High |
| Elevation of Privilege |  |  |  |  |  |  | Low / Medium / High |

## AI Defense Matrix Overlay

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

## Control Gaps And Compensating Controls

| Control Area | Expected Control | Current Gap | Compensating Control | Owner |
| --- | --- | --- | --- | --- |
| Identity and access |  |  |  |  |
| Agent tool authorization |  |  |  |  |
| Prompt and context boundary |  |  |  |  |
| Retrieval authorization |  |  |  |  |
| Sensitive data handling |  |  |  |  |
| Logging and monitoring |  |  |  |  |

## Release Risks

| Risk | Severity | Owner | Decision | Due Date |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |

## Revalidation Triggers

- Design change:
- New model, provider, tool, or retrieval source:
- New data classification:
- New environment rollout:
- Exception renewal:
- Incident or control failure:
