from __future__ import annotations

import argparse
import json
from pathlib import Path

from ai_appsec_harness.evaluator import evaluate, render_markdown, write_report
from ai_appsec_harness.preflight import (
    render_preflight_markdown,
    validate_preflight_package,
    write_preflight_report,
)


def load_json(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Render AI AppSec deterministic reports from structured inputs."
    )
    parser.add_argument("--intake", type=Path, help="Path to AI system intake JSON.")
    parser.add_argument("--catalog", type=Path, help="Path to control catalog JSON.")
    parser.add_argument("--preflight", type=Path, help="Path to AI AppSec preflight package JSON.")
    parser.add_argument("--out", type=Path, help="Path to write the Markdown report.")
    parser.add_argument(
        "--validate-only",
        action="store_true",
        help="Validate a preflight package without writing Markdown.",
    )
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    if args.preflight:
        package = load_json(args.preflight)
        issues = validate_preflight_package(package)
        if issues:
            print("AI AppSec preflight package validation failed:")
            for issue in issues:
                print(f"- {issue.format()}")
            return 1
        if args.validate_only:
            print(f"Preflight package valid: {args.preflight}")
            return 0
        if not args.out:
            parser.error("--out is required unless --validate-only is used")
        markdown = render_preflight_markdown(package)
        write_preflight_report(markdown, args.out)
        print(f"Wrote {args.out}")
        return 0

    if not args.intake or not args.catalog or not args.out:
        parser.error("--intake, --catalog, and --out are required unless --preflight is used")

    intake = load_json(args.intake)
    catalog = load_json(args.catalog)
    results = evaluate(intake, catalog)
    markdown = render_markdown(intake, results)
    write_report(markdown, args.out)
    print(f"Wrote {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
