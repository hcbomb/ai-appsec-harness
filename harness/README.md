# Harness Proof Of Concept

This is a small no-dependency Python harness that turns an AI system intake into an evidence gap report.

The primary human-in-the-loop workflow is now the agent-import harness described in `../docs/agent-tool-import.md`. Use the Python CLI when you already have structured JSON intake and want a deterministic starter gap report.

It currently supports:

- JSON intake files;
- JSON control catalogs;
- applicability matching by system type, capability, and data classification;
- required evidence gap analysis;
- Markdown report generation.

Run it from the repository root:

```bash
PYTHONPATH=harness python3 -m ai_appsec_harness.cli \
  --intake examples/ai-client-intake.example.json \
  --catalog data/control-catalog.seed.json \
  --out build/ai-client-attestation.md
```

Future versions should ingest upstream AISVS and CSA AICM control exports directly so candidate alignments can become versioned, authoritative mappings.
