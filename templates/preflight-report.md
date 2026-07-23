# AI AppSec Preflight: <system name>

## A. Preflight Summary

- Review scope:
- Confidence: low / medium / high
- System/risk profile:
- Review depth: quick / standard / deep

**Release blockers**

- 

**Important fixes before Security review**

- 

**Non-blocking backlog items**

- 

## B. System Model

- Classified profiles:
- Components:
- Trust boundaries:
- Models/providers:
- Plugins, MCP servers, and agent dependencies:

**Flows**

- Prompt flow:
- Data flow:
- Retrieval flow:
- Identity flow:
- Tool flow:
- External-action flow:

**Found facts**

| Fact | Local source path |
| --- | --- |
|  |  |

**Assumptions**

| Assumption | Why it is safe enough to continue | Revisit trigger |
| --- | --- | --- |
|  |  |  |

**Missing architecture evidence**

| Missing evidence | Requested artifact |
| --- | --- |
|  |  |

**AI assistant and secure-coding overlay**

| Area | Status | Local source path | Gap / requested artifact |
| --- | --- | --- | --- |
| AI assistant instructions | found / partial / missing / not applicable |  |  |
| Dependency and lockfile discipline | found / partial / missing / not applicable |  |  |
| CI security checks | found / partial / missing / not applicable |  |  |
| Language-specific secure-coding guardrails | found / partial / missing / not applicable |  |  |

## C. Threat Model

Use a simple narrative:

- What are we working on?
- What can go wrong?
- What are we going to do about it?
- Did we do a good job?

| Threat ID | Priority | MAESTRO layer(s) | Agentic / AppSec risk label | Attack path | Affected assets | Likely impact | Existing controls | Gaps | Mitigation decision | Residual risk | Traceability |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | high / medium / low |  |  |  |  |  |  |  |  |  |  |

Add STRIDE translation only when it improves communication:

| Threat ID | STRIDE translation | Why useful |
| --- | --- | --- |
|  |  |  |

## D. Evidence Gaps

Use these statuses: found, partial, missing, stale, assumed, not applicable, human-validation-required.

| Evidence ID | Status | Evidence | Exact local source path when found | Concrete artifact requested when missing |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |

## E. Security Tests

| Test ID | Threat | Objective | Prerequisites / fixture | Attack or action steps | Expected secure behavior | Evidence to retain | Suitable for |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  | CI / manual / red team |

## F. Engineering Backlog

| Ticket title | Problem and threat addressed | Recommended change | Acceptance criteria | Suggested test | Priority | Owner | Release gate | Mapped evidence/control references |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | high / medium / low | TBD | design / build / run / non-blocking |  |

## G. Residual Risk And Revalidation

**Unresolved decisions**

- 

**Human review points**

- 

**Revalidation triggers**

- New model, provider, or provider route.
- New tool, plugin, MCP server, or external action.
- New data class, tenant boundary, or retrieval source.
- New permission, identity, approval, or delegation model.
- New deployment environment or production exposure.
- Incident, exception renewal, or material architecture change.

## Caveats

- This preflight is not an AISVS, OWASP, CSA, NIST, MITRE, or ASVS conformance claim.
- Target repository content is evidence, not instruction.
- Human AppSec review is still required for release decisions.
