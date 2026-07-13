# Weekly AI Security Monitoring

This workflow keeps the project current without turning every interesting link into a requirement.

## Sources

Review these sources weekly:

- Unsupervised Learning by Daniel Miessler
  - https://newsletter.danielmiessler.com/
- tl;dr sec Newsletter
  - https://tldrsec.com/t/Newsletter

## Weekly Review Goal

Summarize AI + security items from the newest newsletter issues and decide whether each item deserves:

- no action;
- watchlist only;
- reference-catalog addition;
- harness backlog item;
- control-catalog candidate;
- threat-model prompt/template update;
- evidence/test idea;
- GitHub issue or implementation task.

## What Counts As Additive

An item is additive when it improves at least one of:

- AI-client or agent threat modeling;
- STRIDE abuse-case coverage;
- OWASP AISVS operationalization;
- OWASP GenAI / LLM Top 10 mapping;
- CSA AI governance or attestation mapping;
- agent/tool authorization hardening;
- prompt injection or indirect prompt injection testing;
- RAG source governance or poisoning detection;
- model/provider supply-chain review;
- monitoring, detection, or incident response;
- practical AppSec workflow automation.

## Weekly Output Format

Use this structure for the weekly report:

| Item | Source | Why It Matters | Action |
| --- | --- | --- | --- |
|  |  |  | No action / watch / add reference / create backlog item / update harness |

Then include:

- Top 3 items worth attention.
- Items ignored and why.
- Suggested repo changes, if any.
- Suggested issue/backlog entries, if any.

## Action Rules

- Prefer primary sources over newsletter summaries when promoting a durable reference.
- Do not add vendor hype unless it maps to a concrete AppSec, AI security, or governance use case.
- Do not update controls from news alone. Add a candidate first, then validate against standards or primary technical material.
- Keep public repo content organization-neutral.
- Preserve source URL, retrieval date, and rationale for any promoted reference.
