# Security Advisory Response Workflow

This workflow captures a common AppSec pattern: a team asks for a security review, but the most useful first response is not a meeting. It is a concise advisory that tells the requestor what to document, what risks to think through, and when Security should engage.

The goal is to turn a lightweight project ask into practical guidance that is both strategic and tactical:

- strategic: frame the review around use case, data handling, trust boundaries, and control assumptions;
- tactical: tell the requestor exactly what to document before review and what open risks will trigger a meeting or launch decision.

## When To Use This

Use this response pattern when a request involves:

- a new platform, product, service, or open-source component;
- telemetry, reporting, analytics, quality, or support workflows;
- AI clients, agents, RAG, chat, or model integrations;
- customer, patient, member, regulated, confidential, or joinable metadata;
- external integrations, internet exposure, admin/support access, bulk export, automation, bots, subscriptions, or dashboards;
- a request for Security sign-off before the design is fully documented.

## Core Advisory Position

The first security question is not "is this safe?"

The first security question is:

> What exactly is being built or changed, what data is involved, where does it flow, where is it stored, who can access it, what controls are assumed, and what data classification applies at each step?

The product or engineering team designing and deploying the system is best positioned to document that first. Security can then review actual risks, gaps, and decisions instead of using the first meeting as discovery.

## Requestor Guidance Structure

When responding to a requestor, ask them to publish a self-service threat model or review packet covering the sections below.

### 1. Use Case And Scope

Ask for:

- business or product use case;
- users, personas, tenants, customers, partners, or support/admin roles;
- lifecycle stage: dev-only, pilot, staging, production, customer-facing, or internal-only;
- whether real regulated data, customer data, confidential data, or synthetic data will be used;
- whether PHI/ePHI, PII, clinical, claims, prior-authorization, financial, or other regulated data may be in scope;
- whether this is a temporary design, pilot, or target-state architecture.

### 2. Data Inventory

Ask for:

- all data elements collected, processed, stored, displayed, logged, exported, or derived;
- domain resource types such as FHIR resources, claims, prior-authorization records, clinical documents, attachments, tasks, communications, audit events, and binary files where applicable;
- identifiers, session IDs, correlation IDs, user IDs, customer/member/patient IDs, tenant IDs, plan IDs, claim IDs, or other joinable metadata;
- prompts, responses, feedback, attachments, documents, binaries, tasks, communications, audit events, telemetry fields, and derived analytics;
- regulated, confidential, sensitive, or inferred data;
- data classification for each category.

### 3. Data Flow

Ask for:

- producer/source systems;
- API, ingestion, webhook, subscription, file, batch, or bulk export paths;
- validation, redaction, rejection, transformation, and enrichment points;
- app/server, workflow, bot, agent, or automation components;
- databases, caches, object/blob storage, key management, queues, and search/indexing systems;
- logs, telemetry, monitoring, analytics, dashboards, and support workflows;
- external integrations and outbound destinations.

### 4. Trust Boundaries

Ask for:

- customer/user boundary;
- internet, partner, or external integration boundary;
- API gateway, WAF, ingress, or edge boundary;
- service-to-service boundary;
- application/workload boundary;
- database, cache, storage, and key-management boundary;
- tenant/customer/provider boundary;
- support, admin, break-glass, or operations boundary;
- reporting, dashboard, analytics, or export boundary.

### 5. Security Controls

Ask for control assumptions around:

- authentication and SSO;
- authorization and access policy model;
- tenant isolation and row/object-level enforcement;
- network exposure and ingress restrictions;
- secret management and key management;
- encryption in transit and at rest;
- audit logging and tamper resistance;
- backup, restore, retention, deletion, and legal hold;
- redaction, rejection, field allowlists, and payload validation;
- dashboard, reporting, and export restrictions;
- bot, subscription, workflow, or agent execution controls;
- vulnerability, container, dependency, and infrastructure scanning;
- access reviews and privileged support/admin controls.

### 6. Known Assumptions And Open Risks

Ask the team to call out:

- dev shortcuts such as public ingress, no WAF, weak network segmentation, local secrets, permissive roles, or synthetic-only assumptions;
- whether sensitive or regulated data is prohibited in non-production;
- whether key management, private networking, SSO, tenant isolation, or logging is mandatory before launch;
- whether multi-tenancy is in scope;
- whether raw prompts, chat content, telemetry payloads, or attachments are stored;
- whether tenant routing, authorization scope, or user identity is accepted from payloads;
- whether bulk export, dashboards, GraphQL, bots, subscriptions, external integrations, or analytics workflows are enabled;
- known open issues, deferred controls, and compensating controls.

## Meeting Gate

Recommend a meeting only after the requestor publishes the threat model or review packet, and only when one or more of these remain:

- unresolved risks;
- unclear data flows;
- sensitive-data handling concerns;
- unclear tenant or authorization boundaries;
- missing control assumptions;
- exception or risk acceptance needs;
- launch-blocking decisions.

## Output To The Requestor

A useful response should include:

- thanks and acknowledgement of the request;
- recommendation to complete the self-service threat model or review packet first;
- why this helps: Security can review risks and decisions rather than perform discovery;
- scoped checklist of what the threat model should cover;
- clear next steps;
- conditions for a follow-up meeting.

Use `templates/security-advisory-response.md` as a reusable response draft, and `examples/security-advisory-request.example.json` as a minimal example of the kind of early request this workflow is meant to enrich.

## Specialized Intake Profiles

### Healthcare Or Regulated Data Platform

Emphasize:

- regulated data scope and privacy-policy alignment;
- PHI/ePHI, PII, FHIR or domain resource types, and sensitive metadata;
- patient, member, customer, provider, tenant, and support/admin identifiers;
- API, storage, export, bot/subscription, and integration paths;
- tenant isolation, access policies, audit logs, retention, backup/restore, and bulk export restrictions;
- non-production data prohibitions and synthetic-data assumptions.

### Telemetry, Reporting, Or Quality Flow

Emphasize:

- exact telemetry fields and joinable metadata;
- whether prompts, responses, chat history, feedback, or free-text comments are captured;
- redaction, rejection, allowlist, and validation points;
- logs, reporting databases, dashboards, export paths, and support/analytics workflows;
- cross-tenant exposure, dashboard permissions, retention, and auditability;
- whether raw content or regulated data can enter telemetry.

## Definition Of Done

The advisory response is complete when the requestor knows:

- what artifact to publish before review;
- what data, architecture, trust boundary, control, and risk questions to answer;
- what Security will review after the artifact exists;
- when a meeting is warranted;
- what immediate launch blockers or data-handling concerns may exist.
