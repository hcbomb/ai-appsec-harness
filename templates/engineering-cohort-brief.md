# Engineering Cohort Brief

## Why This Review Exists

We are reviewing AI clients, agents, and LLM applications so teams can ship useful AI features with clear security boundaries, evidence, and repeatable hardening patterns.

## What Engineering Should Bring

- Architecture and data flow.
- Model/provider configuration.
- Prompt and instruction design.
- Tool and plugin inventory.
- Retrieval source inventory.
- Tests for prompt injection, data leakage, tool authorization, and unsafe outputs.
- Monitoring and incident response plan.

## What AppSec Will Produce

- Threat model.
- Applicable controls.
- Evidence gap report.
- Hardening actions.
- Attestation-ready summary.

## What Good Looks Like

- The system has clear owners and boundaries.
- Tool use is least-privileged and logged.
- Sensitive data is minimized before model exposure.
- Retrieval respects authorization.
- Generated output is validated before action.
- Human approval exists where the agent can cause meaningful harm.
- Monitoring and rollback paths exist before production.
