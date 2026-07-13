# Security Policy

## Reporting A Vulnerability

Please report security issues in the AI AppSec Harness through GitHub Security Advisories for this repository when available.

If advisories are not available, open a minimal public issue that says a security report is pending, but do not include exploit details, secrets, private target-repo information, or instructions that could compromise users.

Security-relevant reports include:

- malicious or unsafe instructions in agent-facing files;
- prompt-injection or instruction-boundary weaknesses in harness guidance;
- unsafe default permissions, commands, or import patterns;
- supply-chain concerns in skills, prompts, templates, or seed catalogs;
- vulnerabilities in the Python proof of concept;
- sensitive data exposure in examples, docs, generated reports, or tests.

## Supported Versions

This repository is an alpha scaffold. Until stable releases exist, only the current `main` branch and reviewed feature branches are supported.

## Public-Safe Reporting

This project is public and employer-agnostic. Do not include:

- customer data;
- secrets, tokens, credentials, or private keys;
- internal ticket or wiki links;
- non-public architecture diagrams;
- exploit steps against a real organization.

Use sanitized examples and describe impact in generic AppSec language.

