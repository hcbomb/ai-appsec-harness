# Security Advisory Response

Hi team,

Before scheduling a security review meeting, please first complete a self-service threat model or security review packet and publish it for review.

For this request, the team designing and deploying the system should document the actual use case, architecture, data flows, trust boundaries, and control assumptions. Security can provide a much more useful review once that artifact exists. Otherwise, the first meeting is likely to become discovery rather than risk review.

## Please Cover

### 1. Use Case And Scope

- What business or product use case this supports.
- Whether this is dev-only, pilot, staging, production, customer-facing, or internal-only.
- Whether real regulated data, customer data, confidential data, joinable metadata, or synthetic data will be used.
- Whether PHI/ePHI, PII, clinical, claims, prior-authorization, financial, or other regulated data may be in scope.

### 2. Data Inventory

- Data elements collected, processed, stored, displayed, logged, exported, or derived.
- Domain resource types such as FHIR resources, claims, prior-authorization records, clinical documents, attachments, tasks, communications, audit events, and binary files where applicable.
- Identifiers, session IDs, correlation IDs, tenant IDs, user/customer/member/patient IDs, and other joinable metadata.
- Prompts, responses, feedback, attachments, documents, telemetry fields, audit events, and binary files where applicable.
- Data classification for each category.

### 3. Data Flow

- Source systems and producers.
- API, ingestion, webhook, subscription, batch, or export paths.
- Validation, redaction, rejection, and transformation points.
- Application, workflow, bot, agent, or automation components.
- Databases, caches, storage, key management, logs, telemetry, dashboards, and monitoring platforms.
- External integrations and outbound destinations.

### 4. Trust Boundaries

- Customer/user boundary.
- Internet, partner, or external integration boundary.
- API gateway, WAF, ingress, or edge boundary.
- Service-to-service boundary.
- Application/workload boundary.
- Database/cache/storage/key-management boundary.
- Tenant/customer/provider boundary.
- Support, admin, break-glass, reporting, dashboard, or export boundary.

### 5. Security Controls

- Authentication and SSO.
- Authorization and access policy model.
- Tenant isolation.
- Network exposure.
- Secret and key management.
- Encryption.
- Audit logging.
- Backup, restore, retention, and deletion.
- Redaction, rejection, field allowlists, and payload validation.
- Export restrictions.
- Bot, subscription, workflow, or agent execution controls.
- Vulnerability, container, dependency, and infrastructure scanning.
- Access reviews and privileged support/admin controls.

### 6. Known Assumptions And Open Risks

- Any dev shortcuts or temporary controls.
- Whether sensitive or regulated data is prohibited in non-production.
- Whether key management, private networking, SSO, tenant isolation, or logging is mandatory before launch.
- Whether multi-tenancy is in scope.
- Whether raw prompts, chat content, telemetry payloads, attachments, or free-text comments are stored.
- Whether tenant routing, authorization scope, or user identity is accepted from payloads.
- Whether bulk export, dashboards, external integrations, bots, subscriptions, or analytics workflows are enabled.
- Known open issues, deferred controls, compensating controls, or accepted risks.

## Recommendation

- Engineering publishes the threat model or review packet first.
- Security reviews the documented design, data flow, and control assumptions.
- We meet only if there are unresolved risks, unclear data flows, sensitive-data handling concerns, exception needs, or launch-blocking decisions.

Thanks.
