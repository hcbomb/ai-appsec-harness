# Secondary STRIDE Threat Modeling

Use `docs/threat-modeling-maestro.md` first for AI clients, LLM applications, RAG systems, MCP/tool-using workflows, and autonomous or semi-autonomous agents.

STRIDE remains in this repo because it is familiar to many AppSec and engineering audiences. Use it as:

- a fallback when MAESTRO would be too much for the review scope;
- a translation layer for leadership, AppSec, and engineering teams that expect traditional categories;
- a completeness check after MAESTRO layer analysis;
- a lightweight intake path for non-AI or low-complexity changes.

Do not use STRIDE as the primary method for agentic AI, multi-agent, RAG, MCP, or tool-using systems unless the review is intentionally lightweight. Those systems should start with MAESTRO and optionally translate top findings into STRIDE.

## Tier 1: Lightweight STRIDE Fallback

Use this tier for normal software design reviews, project risk assessments, exception support, and low-complexity AI system reviews where MAESTRO is not needed and the team needs fast, structured security feedback.

### When To Run It

Run a lightweight STRIDE fallback when a team is:

- designing a new non-AI service, application, or data flow;
- reviewing a low-complexity AI client or feature after documenting why MAESTRO is not needed;
- introducing new integrations, APIs, tools, retrieval sources, or providers in a non-agentic or intentionally lightweight scope;
- changing identity, authorization, access, networking, or environment boundaries;
- processing sensitive data such as customer data, PHI, PII, financial data, secrets, or internal confidential data;
- adopting AI platforms, LLM providers, model pipelines, agent frameworks, or RAG systems where the review will immediately escalate to MAESTRO if the scope becomes agentic, sensitive, or production-facing;
- requesting an exception, transitional control, or compensating-control path.

### Minimum Intake

Ask for what already exists before asking the team to create new artifacts.

Required:

- request title, requestor, owning team, business owner, and technical owner;
- related implementation ticket, epic, design doc, or wiki page;
- business use case and target delivery or review date;
- current state, target state, and any interim operating model;
- known manual controls, control gaps, or transitional concerns;
- intended review output: quick feedback, STRIDE translation, exception support, architecture review, leadership summary, or PDF/exportable artifact.

Minimum architecture views:

- system context;
- trust zones or environment boundaries;
- identity and access flow;
- data flow;
- short notes on sensitive data, encryption, secrets, logging, and external dependencies.

For complex systems, add software/component, infrastructure/deployment, network ingress/egress, key management, and operational workflow views.

### STRIDE Categories

| Category | Core Question | AI-Specific Lens |
| --- | --- | --- |
| Spoofing | Can one actor, service, tenant, user, or tool impersonate another? | Can prompts, tool responses, plugins, agents, or identities be confused or forged? |
| Tampering | Can data, code, configuration, prompts, context, tools, or logs be changed without authorization? | Can retrieved content, prompts, model config, agent plans, or tool arguments be poisoned or altered? |
| Repudiation | Can an actor deny a security-relevant action? | Can we prove who prompted, approved, retrieved, generated, invoked, or executed an agent action? |
| Information Disclosure | Can sensitive information be exposed beyond intended boundaries? | Can prompts, embeddings, model outputs, logs, retrieval, or providers leak sensitive data? |
| Denial of Service | Can availability, cost, quota, or support capacity be exhausted? | Can prompt floods, expensive tool loops, retrieval spikes, model failures, or provider limits degrade service? |
| Elevation of Privilege | Can an actor gain more authority than intended? | Can an agent, tool, plugin, service account, or user escalate through delegated authority? |

### Baseline Flow

1. Confirm the request.
   - Clarify what is changing, why the business needs it, who owns it, and what output Security should provide.
2. Gather source artifacts.
   - Prefer existing PRDs, TRDs, design docs, tickets, wiki pages, diagrams, runbooks, SOPs, and standards.
3. Capture business use cases.
   - Identify users, workflows, affected systems, environments, and impact if delayed or unavailable.
4. Identify review shape.
   - Choose lightweight review, STRIDE translation, exception-supporting assessment, architecture-heavy review, or follow-on implementation tasks.
5. Review architecture.
   - Confirm enough context exists to understand system scope, trust boundaries, IAM/access flow, data flow, and environment differences.
6. Analyze STRIDE.
   - Review every STRIDE category. Capture meaningful threats, exploit scenarios, business impact, current controls, gaps, and residual risk.
7. Decide what to do.
   - For each meaningful risk, decide whether to remediate, defer with compensating controls, accept with rationale, redesign, or block release.
8. Return structured feedback.
   - Capture missing inputs, control gaps, architecture concerns, unresolved decisions, remediation items, and exception needs in the right system of record.

### Minimum Outputs

Lightweight review:

- feedback in the tracking ticket;
- missing inputs called out;
- no full artifact unless risk requires it.

Standard threat model or risk assessment:

- completed threat model or assessment artifact;
- linked implementation ticket;
- remediation items or accepted-risk notes.

Exception-supporting review:

- completed assessment artifact;
- linked exception or risk ticket;
- explicit residual risk, compensating controls, expiration, and remediation plan.

Architecture-heavy review:

- architecture feedback;
- linked diagrams;
- assessment artifact;
- optional exportable packet for review meetings.

### Fallback Definition Of Done

A lightweight STRIDE fallback is complete when:

- all STRIDE categories were considered;
- significant risks are documented in plain language;
- current controls, gaps, and compensating controls are clear;
- remediation or acceptance decisions are captured;
- owners and next steps are assigned;
- the output informs design, release, exception, or deployment decisions.

## Tier 2: STRIDE Translation After MAESTRO

Use this tier after a MAESTRO review when the output needs to be easier for a traditional AppSec audience to consume.

Translation rule: do not re-run the whole review from scratch. Start from the MAESTRO layer threats, cross-layer scenarios, and AI Defense Matrix coverage gaps, then classify only the significant findings into STRIDE categories.

### What Are We Working On?

Build enough model to reason from the same facts:

- system purpose, users, business workflows, and assets;
- system context and external dependencies;
- trust boundaries, ownership boundaries, environments, and tenants;
- data flows, identity flows, tool flows, retrieval flows, and approval flows;
- model providers, agent frameworks, plugins, MCP servers, service accounts, secrets, and logs;
- current, target, and transitional states.

Use multiple diagrams when one diagram would hide too much:

- context diagram;
- trust-zone/environment diagram;
- identity/access flow;
- data flow diagram;
- agent/tool invocation flow;
- RAG ingestion and retrieval flow;
- deployment/infrastructure view;
- operational/admin workflow.

### What Can Go Wrong?

Apply STRIDE to the MAESTRO-informed system model, not only to a text description.

Review threats by:

- external actor;
- user role;
- service identity;
- model/provider boundary;
- prompt/context boundary;
- retrieval source;
- tool or plugin;
- data store;
- CI/CD and configuration path;
- logging and audit path;
- human approval or exception path.

For AI clients and agents, include:

- prompt injection and indirect prompt injection;
- instruction hierarchy confusion;
- retrieved-content poisoning;
- sensitive data leakage through prompts, embeddings, logs, providers, and outputs;
- unauthorized tool invocation;
- tool argument tampering;
- excessive agency;
- cross-tenant or cross-role retrieval;
- unsafe generated code, commands, tickets, messages, or deployments;
- model/provider configuration drift;
- evaluation bypass or missing regression tests.

### What Are We Going To Do About It?

For each meaningful threat, capture:

- affected asset and boundary;
- impact and likelihood;
- existing controls;
- missing controls;
- recommended remediation;
- compensating controls if remediation is deferred;
- owner and due date;
- residual risk;
- release or exception decision.

Prefer mitigations that engineering can implement and test:

- narrow tool scopes and allowlists;
- policy checks before agent action;
- schemas for tool arguments and outputs;
- human approval for destructive or privileged actions;
- retrieval authorization before prompt assembly;
- prompt/content boundary labeling;
- provider retention and training-use controls;
- canary secrets and leakage tests;
- correlation IDs across prompt, retrieval, model, and tool events;
- kill switches, rollback, and provider isolation.

### Did We Do A Good Job?

Use review quality checks:

- Did we include the right people: product, engineering, security, platform, data, and operations?
- Did diagrams show trust boundaries, current/target state, and sensitive data?
- If STRIDE translation was used, did we review the relevant STRIDE categories without forcing irrelevant filler?
- Did we identify specific abuse cases, not only generic risks?
- Did we convert risks into decisions, backlog items, tests, or accepted risks?
- Did we record assumptions and unresolved questions?
- Did we define revalidation triggers?
- Can the final artifact be used by engineering, leadership, audit, and incident response?

## Escalation Triggers

Escalate from a lightweight STRIDE fallback to MAESTRO-first when:

- production scope includes unresolved manual access handling;
- privileged access is standing, unclear, broad, or not reviewable;
- broad user enablement lacks a clear business need;
- lifecycle provisioning or deprovisioning is missing but assumed;
- ownership for access review, monitoring, or recertification is unclear;
- diagrams do not show trust boundaries, environment differences, or data flows;
- the team wants approval despite unresolved control gaps;
- an AI agent can perform external, destructive, privileged, financial, regulated, or customer-visible actions;
- sensitive data reaches prompts, embeddings, providers, retrieval indexes, or logs without a clear minimization and retention model.

## System Of Record Pattern

Use the right artifact for the right job:

- tracking ticket: status, missing inputs, follow-up questions, remediation tasks, and implementation work;
- assessment artifact: formal MAESTRO results, optional STRIDE translation, residual risk, control gaps, compensating controls, and decisions;
- diagrams: architecture, trust boundaries, data flow, IAM/access flow, agent/tool flow, and operational workflow;
- exportable packet: leadership, audit, exception, or approval workflows.

## AI Threat Model Acceptance Criteria

An AI threat model is ready for AppSec review when it includes:

- system scope and owners;
- current, target, and transitional state;
- MAESTRO layer analysis or rationale for a lightweight STRIDE-only review;
- model/provider inventory;
- tools, plugins, MCP servers, APIs, and external actions;
- retrieval sources and data classifications;
- trust boundaries for prompts, context, tools, identity, data, and providers;
- MAESTRO threats and optional STRIDE translation with AI-specific abuse cases;
- control gaps and compensating controls;
- remediation plan and accepted-risk path;
- monitoring, incident response, and revalidation triggers.
