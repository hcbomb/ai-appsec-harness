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
- OWASP Top 10 for Agentic Applications
  - https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/
- OWASP Multi-Agentic System Threat Modeling Guide
  - https://genai.owasp.org/resource/multi-agentic-system-threat-modeling-guide-v1-0/
- MAESTRO Threat Modeling Playbook and CSA MAESTRO framework
  - https://agentic-threat-modeling.github.io/MAESTRO/
  - https://cloudsecurityalliance.org/blog/2025/02/06/agentic-ai-threat-modeling-framework-maestro
- AI Defense Matrix by Lenny Zeltser and Sounil Yu
  - https://aidefensematrix.com/
- OWASP Threat Modeling Project
  - https://owasp.org/www-project-threat-modeling/
- OWASP Application Security Verification Standard (ASVS)
  - https://owasp.org/www-project-application-security-verification-standard/
- Model Context Protocol Authorization and Security Guidance
  - https://modelcontextprotocol.io/specification/2025-06-18/basic/authorization
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

The AI threat modeling workflow in this repo is now MAESTRO-first for agentic, RAG, MCP, tool-using, and multi-layer AI architectures. STRIDE and the four-question frame remain credited here because the harness still uses them as secondary translation, completeness-check, and lightweight fallback practices:

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

## Ongoing Monitoring Sources

- tl;dr sec Newsletter
  - https://tldrsec.com/t/Newsletter
- Unsupervised Learning by Daniel Miessler
  - https://newsletter.danielmiessler.com/
- OWASP GenAI Security Project News and Resources
  - https://genai.owasp.org/news/
  - https://genai.owasp.org/resources/
- AVID: AI Vulnerability Database
  - https://avidml.org/

Secondary strategic sweep sources include:

- Microsoft Security Blog: AI and agents
  - https://www.microsoft.com/en-us/security/blog/topic/ai-and-machine-learning/
- Google Threat Intelligence Group / Mandiant AI threat coverage
  - https://cloud.google.com/blog/topics/threat-intelligence
- Anthropic Frontier Red Team
  - https://www.anthropic.com/research/team/frontier-red-team
- Frontier Model Forum AI-Cyber and AI Security workstreams
  - https://www.frontiermodelforum.org/workstreams/ai-cyber-workstream/
  - https://www.frontiermodelforum.org/workstreams/ai-security-workstream/
- Trail of Bits AI/ML security
  - https://blog.trailofbits.com/categories/machine-learning/
  - https://blog.trailofbits.com/categories/prompt-injection/
- Lakera Blog
  - https://www.lakera.ai/blog
- HiddenLayer Innovation Hub / AI Threat Landscape
  - https://www.hiddenlayer.com/innovation-hub
- NCSC secure AI system development and frontier AI cyber guidance
  - https://www.ncsc.gov.uk/collection/guidelines-secure-ai-system-development

## Practitioner Operating Patterns

The baseline review workflow also reflects generalized AppSec operating practices for request intake, architecture evidence, MAESTRO-first threat modeling, optional STRIDE translation, control-gap tracking, exception support, and remediation follow-up.

Private wiki pages, ticketing content, organization-specific material, and non-public process details are intentionally not copied, linked, or redistributed in this public repository. Where practitioner workflows were useful, they were converted into generic patterns.

## Attribution Model

This repository links to upstream sources rather than copying full standards or external content. Future importers should preserve source URL, upstream version, retrieval date, license metadata where available, and local transformation notes.
