# Harness Proof Of Concept

This is a small no-dependency Python harness that turns an AI system intake into an evidence gap report.

It currently supports:

- JSON intake files;
- JSON control catalogs;
- applicability matching by system type, capability, and data classification;
- required evidence gap analysis;
- Markdown report generation.

Run it from the repository root:

```bash
PYTHONPATH=harness python -m ai_appsec_harness.cli \
  --intake examples/ai-client-intake.example.json \
  --catalog data/control-catalog.seed.json \
  --out build/ai-client-attestation.md
```

Future versions should ingest upstream AISVS and CSA AICM control exports directly.
