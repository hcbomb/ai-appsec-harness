# Agent Workbench

The agent roles here are designed to support a human-led AppSec review. They should gather, normalize, map, and draft. They should not silently approve risk, modify production systems, or perform sensitive external actions.

## Roles

- Intake Agent: convert engineering notes into structured intake.
- Security Advisory Agent: turns an early review request into self-service guidance, required evidence, and meeting gates.
- Threat Model Agent: identify abuse cases, trust boundaries, and review priorities.
- AISVS Evidence Agent: map evidence to AISVS-oriented controls and identify gaps.
- CSA Mapper Agent: translate technical evidence into CSA AI governance language.
- Attestation Agent: draft a scoped attestation package for human review.

## Required Guardrails

- No autonomous production change.
- No hidden tool invocation.
- No unapproved access to customer, regulated, or secret data.
- Preserve source links and evidence paths.
- Mark uncertainty explicitly.
- Require named human reviewers for attestation decisions.
