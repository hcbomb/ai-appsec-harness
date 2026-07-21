from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any


@dataclass(frozen=True)
class EvidenceResult:
    evidence_id: str
    prompt: str
    required: bool
    status: str
    path: str | None


@dataclass(frozen=True)
class ControlResult:
    control: dict[str, Any]
    evidence: list[EvidenceResult]

    @property
    def missing_required(self) -> list[EvidenceResult]:
        return [
            item
            for item in self.evidence
            if item.required and item.status not in {"available", "not_applicable", "accepted_risk"}
        ]


def evaluate(intake: dict[str, Any], catalog: dict[str, Any]) -> list[ControlResult]:
    controls = catalog.get("controls", [])
    evidence_index = {
        item.get("id"): item
        for item in intake.get("evidence", [])
        if isinstance(item, dict) and item.get("id")
    }

    results: list[ControlResult] = []
    for control in controls:
        if not applies(control, intake):
            continue

        evidence_results = []
        for expected in control.get("evidence", []):
            evidence_id = expected.get("id", "")
            provided = evidence_index.get(evidence_id, {})
            evidence_results.append(
                EvidenceResult(
                    evidence_id=evidence_id,
                    prompt=expected.get("prompt", ""),
                    required=bool(expected.get("required", False)),
                    status=provided.get("status", "missing"),
                    path=provided.get("path"),
                )
            )
        results.append(ControlResult(control=control, evidence=evidence_results))

    return results


def applies(control: dict[str, Any], intake: dict[str, Any]) -> bool:
    rules = control.get("applies_when", {})
    system_type = intake.get("system", {}).get("system_type")
    capabilities = set(intake.get("capabilities", []))
    data_classes = set(intake.get("data", {}).get("classifications", []))

    allowed_systems = set(rules.get("system_types", []))
    if allowed_systems and "all" not in allowed_systems and system_type not in allowed_systems:
        return False

    capability_any = set(rules.get("capabilities_any", []))
    if capability_any and capabilities.isdisjoint(capability_any):
        return False

    data_any = set(rules.get("data_classifications_any", []))
    if data_any and data_classes.isdisjoint(data_any):
        return False

    return True


def render_markdown(intake: dict[str, Any], results: list[ControlResult]) -> str:
    system = intake.get("system", {})
    missing_count = sum(len(result.missing_required) for result in results)
    applicable_count = len(results)
    status = "Evidence gaps found" if missing_count else "Ready for human validation"

    lines = [
        f"# AI AppSec Attestation Gap Report: {system.get('name', 'Unnamed System')}",
        "",
        f"- Owner: {system.get('owner', 'Unspecified')}",
        f"- System type: {system.get('system_type', 'Unspecified')}",
        f"- Lifecycle stage: {system.get('lifecycle_stage', 'Unspecified')}",
        f"- Status: {status}",
        f"- Applicable seed controls: {applicable_count}",
        f"- Missing required evidence items: {missing_count}",
        "",
        "## Scope",
        "",
        system.get("description", "No system description provided."),
        "",
        "## Applicable Controls",
        "",
    ]

    for result in results:
        control = result.control
        lines.extend(
            [
                f"### {control.get('id')} - {control.get('title')}",
                "",
                control.get("summary", ""),
                "",
                "**Framework alignment**",
                "",
            ]
        )
        for alignment in control.get("alignments", []):
            lines.append(
                f"- {alignment.get('framework')}: {alignment.get('note')} ({alignment.get('status')})"
            )

        if control.get("authoritative_mappings"):
            lines.extend(["", "**Versioned traceability**", ""])
            for mapping in control.get("authoritative_mappings", []):
                version = mapping.get("version", "unknown")
                ids = ", ".join(mapping.get("ids", []))
                lines.append(f"- {mapping.get('framework')} {version}: {ids}")
                if mapping.get("note"):
                    lines.append(f"  - Note: {mapping.get('note')}")

        if control.get("risk_tags"):
            lines.extend(["", "**Risk labels**", ""])
            for tag in control.get("risk_tags", []):
                lines.append(f"- {tag}")

        lines.extend(["", "**Evidence**", ""])
        for evidence in result.evidence:
            marker = "required" if evidence.required else "optional"
            path = f" - {evidence.path}" if evidence.path else ""
            lines.append(f"- `{evidence.evidence_id}` ({marker}): {evidence.status}{path}")
            if evidence.status in {"missing", "partial", "stale"}:
                lines.append(f"  - Request: {evidence.prompt}")

        lines.extend(["", "**Suggested tests**", ""])
        for test in control.get("tests", []):
            lines.append(f"- {test.get('id')}: {test.get('prompt')}")

        lines.extend(["", "**Hardening actions**", ""])
        for action in control.get("hardening_actions", []):
            lines.append(f"- {action}")

        if result.missing_required:
            lines.extend(["", "**Gap summary**", ""])
            for evidence in result.missing_required:
                lines.append(f"- Missing or incomplete required evidence: `{evidence.evidence_id}`")

        lines.append("")

    lines.extend(
        [
            "## Reviewer Notes",
            "",
            "- This report is generated from seed controls and requires human AppSec validation.",
            "- Do not claim OWASP AISVS or CSA AI conformance until scope, evidence, exceptions, and reviewer decisions are validated by humans.",
            "- Record accepted risks, compensating controls, and residual risk before release approval.",
            "",
        ]
    )

    return "\n".join(lines)


def write_report(markdown: str, output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(markdown, encoding="utf-8")
