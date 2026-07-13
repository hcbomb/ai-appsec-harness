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
- watchlist;
- add reference;
- create backlog item;
- update harness;
- update prompt/template;
- update test/evidence idea.

Identify the newest issues or posts since the previous run. If there is no previous run state, start with the newest visible issue from each source and record the issue URL, publication date, and retrieval date in the report.

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

Use this structure for the weekly report summary:

| Item | Source | Plain-Language Summary | Why It Matters / No Action Rationale | Action |
| --- | --- | --- | --- | --- |
|  |  |  |  | No action / watchlist / add reference / create backlog item / update harness / update prompt/template / update test/evidence idea |

Then include:

- Top 5 items worth attention.
- Items ignored and why.
- Recommended repo updates, if any.
- Suggested issue/backlog entries, if any.
- Any immediate AppSec action to take.

## Action Rules

- Prefer primary sources over newsletter summaries when promoting a durable reference.
- Do not add vendor hype unless it maps to a concrete AppSec, AI security, or governance use case.
- Do not update controls from news alone. Add a candidate first, then validate against standards or primary technical material.
- Keep public repo content organization-neutral.
- Preserve source URL, retrieval date, and rationale for any promoted reference.
- When a change is additive, keep it small and explain the rationale in the branch, commit, or proposed patch.
