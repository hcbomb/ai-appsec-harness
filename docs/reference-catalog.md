# Reference Catalog

This catalog separates discovery feeds from operating standards. Awesome lists help AppSec and engineering discover patterns and tooling. Standards and frameworks become the evidence and attestation backbone.

## Primary Standards And Frameworks

| Source | Use In This Repo | URL |
| --- | --- | --- |
| OWASP AISVS | Primary verification standard for AI-enabled systems. Use as the authoritative source for control IDs, levels, and testable requirements. | https://github.com/OWASP/AISVS |
| OWASP AISVS Docs | Human-readable reference for engineers, architects, security engineers, and auditors. | https://owasp.org/www-project-artificial-intelligence-security-verification-standard-aisvs-docs/ |
| OWASP GenAI Security Project | Risk taxonomy and practitioner guidance for LLM and GenAI applications. | https://genai.owasp.org/ |
| OWASP Top 10 for LLM Applications | AppSec-friendly risk language for threat modeling and security review narratives. | https://genai.owasp.org/llm-top-10/ |
| CSA AI Controls Matrix | Governance and control mapping for secure, responsible AI systems, especially cloud-based AI. | https://cloudsecurityalliance.org/artifacts/ai-controls-matrix-v1-1 |
| CSA AI Safety Initiative | Working-group home for CSA AI safety, agentic AI, and governance work. | https://cloudsecurityalliance.org/ai-safety-initiative |
| CSA STAR for AI | Assurance and trust program context for CSA AI attestations. | https://cloudsecurityalliance.org/star/ai |
| NIST AI RMF | Risk management vocabulary for governance, mapping, measurement, and management. | https://www.nist.gov/itl/ai-risk-management-framework |
| NIST AI 600-1 GenAI Profile | GenAI-specific companion profile for AI RMF risk management. | https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence |
| MITRE ATLAS | Adversary tactics and techniques for AI threat modeling and red-team scenario design. | https://atlas.mitre.org/ |
| Shostack Four Question Frame | Practical threat modeling frame: what are we working on, what can go wrong, what are we going to do about it, and did we do a good job. | https://github.com/adamshostack/4QuestionFrame |
| Shostack Threat Modeling Guide | Practitioner guidance from Adam Shostack on structured, repeatable threat modeling. | https://shostack.org/resources/threat-modeling.html |
| Threat Modeling Manifesto | Values, principles, patterns, and anti-patterns for productive threat modeling programs. | https://www.threatmodelingmanifesto.org/ |
| OWASP Threat Modeling Project | Current OWASP entry point for threat modeling techniques, community references, tools, and examples. | https://owasp.org/www-project-threat-modeling/ |

## Awesome AI Discovery Feeds

| Source | Best Use | URL |
| --- | --- | --- |
| Awesome Artificial Intelligence | Broad AI engineering resources, especially RAG, agents, evals, guardrails, and deployment. | https://github.com/owainlewis/awesome-artificial-intelligence |
| Awesome LLM | LLM research, tooling, datasets, alignment, systems, compression, and related lists. | https://github.com/hannibal046/awesome-llm |
| Awesome Generative AI | Generative AI projects and services. | https://github.com/steven2358/awesome-generative-ai |
| Awesome LLM Apps | Runnable templates for LLM applications, RAG, agents, and MCP-style integrations. | https://github.com/Shubhamsaboo/awesome-llm-apps |
| Awesome AI Security | AI security frameworks, standards, learning resources, and open source tools. | https://github.com/ottosulin/awesome-ai-security |
| Awesome AI Security by Tal Eliyahu | Security resources, research, and tools for securing AI systems. | https://github.com/TalEliyahu/Awesome-AI-Security |
| GitHub awesome-ai topic | Broad discovery of AI awesome lists and related repositories. | https://github.com/topics/awesome-ai |
| GitHub ai-security topic | Discovery of AI security repositories and tooling. | https://github.com/topics/ai-security |

## Secondary Discovery Backlog

These are useful candidates for later categorization, especially when the harness grows tool recommendation and benchmark modules.

| Source | Potential Use | URL |
| --- | --- | --- |
| Awesome Generative AI Guide | Research updates, courses, notebooks, and interview resources. | https://github.com/aishwaryanr/awesome-generative-ai-guide |
| Awesome LLM Powered Agent | Agent papers, repositories, and implementation references. | https://github.com/hyp1231/awesome-llm-powered-agent |
| Awesome Open Source AI | Open source AI projects, models, tools, and infrastructure. | https://github.com/alvinreal/awesome-opensource-ai |
| Awesome AI Apps | Practical examples and recipes for LLM-powered applications. | https://github.com/Arindam200/awesome-ai-apps |

## Ongoing Monitoring Feeds

These sources are useful for ongoing review. They should not automatically become controls or requirements. Promote an item only when it materially improves threat modeling, harness design, AI-client hardening, AISVS/CSA mapping, testing, detection, or engineering actionability.

### Primary Weekly Sources

| Source | Best Use | URL |
| --- | --- | --- |
| tl;dr sec Newsletter | Weekly security research and tooling roundup; useful for AI + security items, autonomous vulnerability research, agentic security tooling, MCP/security implications, and AppSec-relevant research. | https://tldrsec.com/t/Newsletter |
| Unsupervised Learning by Daniel Miessler | Broad signal across AI, cybersecurity, technology, national security, and culture; useful for AI security trend spotting and emerging tool discovery. | https://newsletter.danielmiessler.com/ |
| OWASP GenAI Security Project News / Resources | Standards-community updates, new OWASP GenAI resources, agentic security guidance, MCP guidance, red-team guidance, and other material that may affect harness mappings or templates. | News: https://genai.owasp.org/news/<br>Resources: https://genai.owasp.org/resources/ |
| AVID: AI Vulnerability Database | Evidence-backed AI vulnerability and failure records that can improve abuse cases, test/evidence ideas, and threat-model examples. | https://avidml.org/ |

### Monthly / Secondary Strategic Sweep Sources

Use these as monthly or signal-driven strategic sweep sources, not weekly sources, unless they repeatedly produce actionable signal for this harness.

| Source | Best Use | URL |
| --- | --- | --- |
| Microsoft Security Blog: AI and agents | AI security, agent hardening, AI threat research, and security engineering practices; useful for strategy and test ideas when backed by primary technical detail. | https://www.microsoft.com/en-us/security/blog/topic/ai-and-machine-learning/ |
| Google Threat Intelligence Group / Mandiant AI threat coverage | Adversary use of AI, AI-enabled threat intelligence, detection, and incident-response implications. | https://cloud.google.com/blog/topics/threat-intelligence |
| Anthropic Frontier Red Team | Empirical AI cyber capability, red-team, and autonomous-system research that may inform threat scenarios, benchmarks, and safety/evidence tests. | https://www.anthropic.com/research/team/frontier-red-team |
| Frontier Model Forum AI-Cyber / AI Security workstreams | Frontier model cyber risk practices, capability thresholds, shared evaluations, and security practices for model development and deployment. | AI-Cyber: https://www.frontiermodelforum.org/workstreams/ai-cyber-workstream/<br>AI Security: https://www.frontiermodelforum.org/workstreams/ai-security-workstream/ |
| Trail of Bits AI/ML security | Practical AI-assisted AppSec, ML security, prompt injection, MCP, agent, and audit research; useful for concrete test/evidence and hardening ideas. | Machine learning: https://blog.trailofbits.com/categories/machine-learning/<br>Prompt injection: https://blog.trailofbits.com/categories/prompt-injection/ |
| Lakera Blog | AI application and agent security research, guardrail patterns, and prompt-injection trends; treat vendor content as secondary signal until validated by technical sources. | https://www.lakera.ai/blog |
| HiddenLayer Innovation Hub / AI Threat Landscape | AI threat landscape, attack taxonomy, model supply-chain, and runtime security signal; validate vendor claims before durable promotion. | https://www.hiddenlayer.com/innovation-hub |
| NCSC secure AI system development and frontier AI cyber guidance | Public guidance for secure AI lifecycle, secure-by-design expectations, AI cyber risk, and governance operating-model checks. | https://www.ncsc.gov.uk/collection/guidelines-secure-ai-system-development |

## Curation Rules

- Prefer primary sources for standards, frameworks, and requirements.
- Treat awesome lists as discovery feeds, not authorities.
- Treat newsletters as monitoring feeds: summarize and triage first, then promote only durable or actionable items.
- Preserve upstream URLs and retrieval dates in machine-readable records.
- Do not claim AISVS, CSA, NIST, or OWASP conformance until exact upstream controls and evidence are mapped.
- Track tool recommendations separately from hardening requirements.
- Do not publish internal wiki content into public artifacts. Synthesize reusable operating patterns without copying private source text or links.
