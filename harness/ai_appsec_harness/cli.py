from __future__ import annotations

import argparse
import json
from pathlib import Path

from ai_appsec_harness.evaluator import evaluate, render_markdown, write_report


def load_json(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Generate an AI AppSec attestation gap report from an intake and control catalog."
    )
    parser.add_argument("--intake", required=True, type=Path, help="Path to AI system intake JSON.")
    parser.add_argument("--catalog", required=True, type=Path, help="Path to control catalog JSON.")
    parser.add_argument("--out", required=True, type=Path, help="Path to write the Markdown report.")
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    intake = load_json(args.intake)
    catalog = load_json(args.catalog)
    results = evaluate(intake, catalog)
    markdown = render_markdown(intake, results)
    write_report(markdown, args.out)
    print(f"Wrote {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
