# Harness Python Helpers

This is a small no-dependency Python helper package for deterministic AI AppSec Harness reports.

The primary human-in-the-loop workflow is the agent-import harness described in `../docs/agent-tool-import.md` and `../docs/preflight-workflow.md`. The coding agent performs semantic repository inspection and threat modeling using the skill. Python helpers validate and render structured inputs.

It currently supports:

- JSON preflight packages;
- preflight completeness validation;
- Markdown preflight report generation;
- JSON intake files;
- JSON control catalogs;
- applicability matching by system type, capability, and data classification;
- required evidence gap analysis;
- Markdown attestation gap report generation.

Render a preflight package:

```bash
PYTHONPATH=harness python3 -m ai_appsec_harness.cli \
  --preflight examples/preflight/mcp-agent.preflight.json \
  --out build/mcp-agent-preflight.md
```

Validate a preflight package:

```bash
PYTHONPATH=harness python3 -m ai_appsec_harness.cli \
  --preflight examples/preflight/mcp-agent.preflight.json \
  --validate-only
```

Render a structured intake gap report:

```bash
PYTHONPATH=harness python3 -m ai_appsec_harness.cli \
  --intake examples/ai-client-intake.example.json \
  --catalog data/control-catalog.seed.json \
  --out build/ai-client-attestation.md
```

The Python CLI does not inspect arbitrary repositories or perform a complete semantic threat model. Future versions may ingest upstream AISVS and CSA AICM control exports directly so local mappings can be refreshed from source metadata.
