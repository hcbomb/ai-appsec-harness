# Acknowledgements

This project is a synthesis of public AI security, AppSec, threat modeling, and governance resources, plus practitioner experience turning those resources into review workflows.

It is not affiliated with, endorsed by, or certified by any standards body, project, company, or maintainer named below.

## Standards, Frameworks, And Public Guidance

- OWASP Artificial Intelligence Security Verification Standard (AISVS)
  - https://github.com/OWASP/AISVS
  - https://owasp.org/www-project-artificial-intelligence-security-verification-standard-aisvs-docs/
  - Credit to the OWASP AISVS project leadership, including Jim Manico, and the broader contributor community.
- OWASP GenAI Security Project and OWASP Top 10 for LLM and GenAI Applications
  - https://genai.owasp.org/
  - https://genai.owasp.org/llm-top-10/
- OWASP Threat Modeling Project
  - https://owasp.org/www-project-threat-modeling/
- Cloud Security Alliance AI Controls Matrix, AI Safety Initiative, and STAR for AI
  - https://cloudsecurityalliance.org/artifacts/ai-controls-matrix-v1-1
  - https://cloudsecurityalliance.org/ai-safety-initiative
  - https://cloudsecurityalliance.org/star/ai
- NIST AI Risk Management Framework and NIST AI 600-1 Generative AI Profile
  - https://www.nist.gov/itl/ai-risk-management-framework
  - https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence
- MITRE ATLAS
  - https://atlas.mitre.org/

## Threat Modeling Practice

- Adam Shostack's Four Question Frame for threat modeling
  - https://github.com/adamshostack/4QuestionFrame
- Shostack + Associates threat modeling resources
  - https://shostack.org/resources/threat-modeling.html
- Threat Modeling Manifesto
  - https://www.threatmodelingmanifesto.org/

The STRIDE workflow in this repo uses the four-question frame as the organizing practice for deeper reviews:

1. What are we working on?
2. What can go wrong?
3. What are we going to do about it?
4. Did we do a good job?

## Community Discovery Feeds

The reference catalog was seeded from community-maintained "awesome" lists and GitHub topic indexes, including:

- Awesome Artificial Intelligence
  - https://github.com/owainlewis/awesome-artificial-intelligence
- Awesome LLM
  - https://github.com/hannibal046/awesome-llm
- Awesome Generative AI
  - https://github.com/steven2358/awesome-generative-ai
- Awesome LLM Apps
  - https://github.com/Shubhamsaboo/awesome-llm-apps
- Awesome AI Security
  - https://github.com/ottosulin/awesome-ai-security
- Awesome AI Security by Tal Eliyahu
  - https://github.com/TalEliyahu/Awesome-AI-Security
- GitHub awesome-ai topic
  - https://github.com/topics/awesome-ai
- GitHub ai-security topic
  - https://github.com/topics/ai-security

## Internal Operating Guidance

The baseline review workflow also reflects generalized internal AppSec operating practices for request intake, architecture evidence, STRIDE review, control-gap tracking, exception support, and remediation follow-up.

Private internal wiki pages, ticketing content, and non-public process details are intentionally not copied, linked, or redistributed in this public repository. Where internal practices were useful, they were converted into generic practitioner patterns.

## Attribution Model

This repository links to upstream sources rather than copying full standards or external content. Future importers should preserve source URL, upstream version, retrieval date, license metadata where available, and local transformation notes.
