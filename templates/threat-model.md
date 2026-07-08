# AI Threat Model

## Scope

- System:
- Review date:
- Reviewers:
- Lifecycle stage:
- Review tier: Baseline assisted STRIDE / Advanced STRIDE
- Requested output: Quick feedback / full assessment / exception support / architecture review / leadership summary

## Four-Question Frame

| Question | Answer |
| --- | --- |
| What are we working on? |  |
| What can go wrong? |  |
| What are we going to do about it? |  |
| Did we do a good job? |  |

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

## STRIDE Analysis

| Category | Threat | Scenario | Impact | Existing Controls | Gaps | Mitigation / Decision | Residual Risk |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Spoofing |  |  |  |  |  |  | Low / Medium / High |
| Tampering |  |  |  |  |  |  | Low / Medium / High |
| Repudiation |  |  |  |  |  |  | Low / Medium / High |
| Information Disclosure |  |  |  |  |  |  | Low / Medium / High |
| Denial of Service |  |  |  |  |  |  | Low / Medium / High |
| Elevation of Privilege |  |  |  |  |  |  | Low / Medium / High |

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
