# Operationalizing OWASP AISVS

OWASP AISVS should become the verification backbone for AI AppSec reviews. The practical goal is not to paste the standard into a spreadsheet. The goal is to make each applicable requirement testable, evidence-backed, and useful to engineering teams building AI clients and agents.

## Implementation Pattern

1. Import upstream AISVS metadata.
   - Preserve authoritative requirement IDs, titles, levels, and text.
   - Record upstream version, source URL, and retrieval date.
2. Normalize into harness controls.
   - Add local applicability rules for AI clients, agents, RAG systems, model pipelines, and cloud-hosted services.
   - Attach expected evidence, test ideas, and engineering hardening actions.
3. Map to adjacent frameworks.
   - OWASP GenAI risks for AppSec threat language.
   - CSA AI Controls Matrix for governance and assurance language.
   - NIST AI RMF and MITRE ATLAS where they improve risk framing or scenario design.
4. Generate evidence requests.
   - Convert each applicable control into concrete artifacts engineering can provide.
5. Evaluate and report.
   - Produce a gap report, not a pass/fail claim, until a human reviewer validates evidence.

## AI Client And Agent Hardening Domains

- System boundaries and data flows.
- Model/provider trust and contractual assumptions.
- Prompt, instruction, and context separation.
- Tool inventory, scopes, and authorization.
- Delegated authority and human approval.
- Secrets and credential handling.
- Retrieval source governance and data leakage prevention.
- Output handling and unsafe action prevention.
- Logging, auditability, and replayability.
- Evaluation, regression tests, and adversarial test suites.
- Monitoring, incident response, rollback, and kill switches.
- Third-party model, plugin, extension, and agent supply chain.

## Control Record Shape

Each operationalized control should include:

- stable local control ID;
- upstream AISVS ID and version;
- title and summary;
- applicability rules;
- mapped frameworks;
- required evidence;
- suggested tests;
- hardening actions;
- review owner;
- accepted-risk path;
- last reviewed date.

## Attestation Rules

- Never claim conformance without a named scope and upstream standard version.
- Separate "evidence present" from "evidence validated."
- Record exceptions and compensating controls.
- Make residual risk explicit.
- Keep generated reports reproducible from versioned inputs.

## Near-Term Backlog

- Add an AISVS importer once the upstream control format is stable.
- Add authoritative AISVS mappings for harness self-protection controls `AIH-010`, `AIH-011`, and `AIH-012`.
- Add CSA AICM mapping import support.
- Add OWASP GenAI Top 10 risk tags to each seed control.
- Add review-pack generation for design, build, and run gates.
- Add regression tests for prompt boundaries, tool authorization, and retrieval source controls.
