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

- Engineer-first AI AppSec preflight report.
- MAESTRO-first threat model.
- STRIDE translation where useful.
- AI Defense Matrix coverage summary when leadership or roadmap framing is needed.
- Evidence gaps with local source paths when found.
- Concrete security tests.
- Ticket-ready backlog and hardening actions.
- Residual-risk notes and revalidation triggers.
- Attestation-ready summary later, if scope and evidence justify it.

## What Good Looks Like

- The system has clear owners and boundaries.
- Tool use is least-privileged and logged.
- Sensitive data is minimized before model exposure.
- Retrieval respects authorization.
- Generated output is validated before action.
- Human approval exists where the agent can cause meaningful harm.
- Monitoring and rollback paths exist before production.
