from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any


EVIDENCE_STATUSES = {
    "found",
    "partial",
    "missing",
    "stale",
    "assumed",
    "not_applicable",
    "human_validation_required",
}

HIGH_PRIORITIES = {"critical", "high"}


@dataclass(frozen=True)
class ValidationIssue:
    path: str
    message: str

    def format(self) -> str:
        return f"{self.path}: {self.message}"


def validate_preflight_package(package: dict[str, Any]) -> list[ValidationIssue]:
    issues: list[ValidationIssue] = []
    required_sections = [
        "preflight_summary",
        "system_model",
        "threat_model",
        "evidence_gaps",
        "security_tests",
        "engineering_backlog",
        "residual_risk",
    ]

    for section in required_sections:
        if section not in package:
            issues.append(ValidationIssue(section, "missing required preflight section"))

    evidence = _items_by_id(package.get("evidence_gaps", []), "evidence_gaps", issues)
    tests = _items_by_id(package.get("security_tests", []), "security_tests", issues)
    backlog = _items_by_id(package.get("engineering_backlog", []), "engineering_backlog", issues)

    for index, item in enumerate(package.get("evidence_gaps", [])):
        status = str(item.get("status", "")).lower()
        if status not in EVIDENCE_STATUSES:
            issues.append(
                ValidationIssue(
                    f"evidence_gaps[{index}].status",
                    f"must be one of {', '.join(sorted(EVIDENCE_STATUSES))}",
                )
            )
        if status == "found" and not item.get("source_path"):
            issues.append(
                ValidationIssue(
                    f"evidence_gaps[{index}].source_path",
                    "found evidence must include an exact local source path",
                )
            )
        if status in {"missing", "partial", "stale", "assumed", "human_validation_required"} and not item.get(
            "requested_artifact"
        ):
            issues.append(
                ValidationIssue(
                    f"evidence_gaps[{index}].requested_artifact",
                    "incomplete evidence must name the concrete artifact requested",
                )
            )

    for index, test in enumerate(package.get("security_tests", [])):
        for field in [
            "objective",
            "prerequisites",
            "steps",
            "expected_secure_behavior",
            "evidence_to_retain",
            "test_type",
        ]:
            if not test.get(field):
                issues.append(ValidationIssue(f"security_tests[{index}].{field}", "is required"))

    for index, item in enumerate(package.get("engineering_backlog", [])):
        for field in [
            "title",
            "problem",
            "recommended_change",
            "acceptance_criteria",
            "suggested_test",
            "priority",
            "owner",
            "release_gate",
        ]:
            if not item.get(field):
                issues.append(ValidationIssue(f"engineering_backlog[{index}].{field}", "is required"))

    threats = package.get("threat_model", {}).get("threats", [])
    for index, threat in enumerate(threats):
        threat_id = threat.get("id") or f"threat[{index}]"
        priority = str(threat.get("priority", "")).lower()
        if priority in HIGH_PRIORITIES:
            _require_field(threat, "mitigation_decision", f"threat_model.threats[{index}]", issues)
            _require_refs(threat, "evidence_refs", evidence, f"threat {threat_id}", issues)
            _require_refs(threat, "test_refs", tests, f"threat {threat_id}", issues)
            _require_refs(threat, "backlog_refs", backlog, f"threat {threat_id}", issues)

    return issues


def render_preflight_markdown(package: dict[str, Any]) -> str:
    system = package.get("system", {})
    summary = package.get("preflight_summary", {})
    model = package.get("system_model", {})
    threat_model = package.get("threat_model", {})

    lines = [
        f"# AI AppSec Preflight: {system.get('name', 'Unnamed System')}",
        "",
        "## A. Preflight Summary",
        "",
        f"- Review scope: {summary.get('scope', 'Unspecified')}",
        f"- Confidence: {summary.get('confidence', 'Unspecified')}",
        f"- System/risk profile: {summary.get('system_risk_profile', 'Unspecified')}",
        f"- Review depth: {summary.get('review_depth', 'Unspecified')}",
        "",
        "**Release blockers**",
        "",
    ]
    _extend_bullets(lines, summary.get("release_blockers", []), empty="None identified from available evidence.")
    lines.extend(["", "**Important fixes before Security review**", ""])
    _extend_bullets(lines, summary.get("important_fixes", []), empty="None identified from available evidence.")
    lines.extend(["", "**Non-blocking backlog items**", ""])
    _extend_bullets(lines, summary.get("non_blocking_backlog", []), empty="None identified.")

    lines.extend(
        [
            "",
            "## B. System Model",
            "",
            f"- Classified profiles: {_join(model.get('profiles', []))}",
            f"- Components: {_join(model.get('components', []))}",
            f"- Trust boundaries: {_join(model.get('trust_boundaries', []))}",
            f"- Models/providers: {_join(model.get('models_and_providers', []))}",
            f"- Plugins/MCP/agent dependencies: {_join(model.get('plugins_mcp_agent_dependencies', []))}",
            "",
            "**Flows**",
            "",
        ]
    )
    for name, value in model.get("flows", {}).items():
        lines.append(f"- {name}: {_join(value)}")
    lines.extend(["", "**Facts, Assumptions, And Missing Architecture Evidence**", ""])
    for label, key in [
        ("Facts", "facts"),
        ("Assumptions", "assumptions"),
        ("Missing evidence", "missing_architecture_evidence"),
    ]:
        lines.append(f"**{label}**")
        _extend_bullets(lines, model.get(key, []), empty="None listed.")
        lines.append("")

    lines.extend(["## C. Threat Model", ""])
    _extend_bullets(lines, threat_model.get("narrative", []), empty="No narrative supplied.")
    lines.append("")
    for threat in threat_model.get("threats", []):
        lines.extend(
            [
                f"### {threat.get('id', 'THREAT')} - {threat.get('title', 'Untitled Threat')}",
                "",
                f"- Priority: {threat.get('priority', 'Unspecified')}",
                f"- MAESTRO layers: {_join(threat.get('maestro_layers', []))}",
                f"- Agentic risk labels: {_join(threat.get('agentic_risk_labels', []))}",
                f"- Attack path: {threat.get('attack_path', 'Unspecified')}",
                f"- Affected assets: {_join(threat.get('affected_assets', []))}",
                f"- Likely impact: {threat.get('likely_impact', 'Unspecified')}",
                f"- Existing controls: {_join(threat.get('existing_controls', []))}",
                f"- Gaps: {_join(threat.get('gaps', []))}",
                f"- Mitigation decision: {threat.get('mitigation_decision', 'Unspecified')}",
                f"- Residual risk: {threat.get('residual_risk', 'Unspecified')}",
                f"- Traceability: {_join(threat.get('traceability', []))}",
                "",
            ]
        )
        if threat.get("stride_translation"):
            lines.append(f"- STRIDE translation: {threat['stride_translation']}")
            lines.append("")

    lines.extend(["## D. Evidence Gaps", ""])
    lines.extend(
        [
            "| ID | Status | Evidence | Local Source | Requested Artifact |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
    for evidence in package.get("evidence_gaps", []):
        lines.append(
            "| {id} | {status} | {title} | {source} | {request} |".format(
                id=evidence.get("id", ""),
                status=evidence.get("status", ""),
                title=_escape_table(evidence.get("title", "")),
                source=_escape_table(evidence.get("source_path", "")),
                request=_escape_table(evidence.get("requested_artifact", "")),
            )
        )

    lines.extend(["", "## E. Security Tests", ""])
    for test in package.get("security_tests", []):
        lines.extend(
            [
                f"### {test.get('id', 'TEST')} - {test.get('title', 'Untitled Test')}",
                "",
                f"- Objective: {test.get('objective', 'Unspecified')}",
                f"- Prerequisites/fixture: {_join(test.get('prerequisites', []))}",
                f"- Attack/action steps: {_join(test.get('steps', []))}",
                f"- Expected secure behavior: {test.get('expected_secure_behavior', 'Unspecified')}",
                f"- Evidence to retain: {test.get('evidence_to_retain', 'Unspecified')}",
                f"- Suitable for: {test.get('test_type', 'Unspecified')}",
                f"- References: {_join(test.get('references', []))}",
                "",
            ]
        )

    lines.extend(["## F. Engineering Backlog", ""])
    for item in package.get("engineering_backlog", []):
        lines.extend(
            [
                f"### {item.get('id', 'BACKLOG')} - {item.get('title', 'Untitled Item')}",
                "",
                f"- Problem/threat addressed: {item.get('problem', 'Unspecified')}",
                f"- Recommended change: {item.get('recommended_change', 'Unspecified')}",
                f"- Acceptance criteria: {_join(item.get('acceptance_criteria', []))}",
                f"- Suggested test: {item.get('suggested_test', 'Unspecified')}",
                f"- Priority: {item.get('priority', 'Unspecified')}",
                f"- Owner: {item.get('owner', 'Unspecified')}",
                f"- Release gate: {item.get('release_gate', 'Unspecified')}",
                f"- Mapped references: {_join(item.get('references', []))}",
                "",
            ]
        )

    residual = package.get("residual_risk", {})
    lines.extend(["## G. Residual Risk And Revalidation", ""])
    for label, key in [
        ("Unresolved decisions", "unresolved_decisions"),
        ("Human review points", "human_review_points"),
        ("Revalidation triggers", "revalidation_triggers"),
    ]:
        lines.append(f"**{label}**")
        _extend_bullets(lines, residual.get(key, []), empty="None listed.")
        lines.append("")

    lines.extend(
        [
            "## Report Caveats",
            "",
            "- This preflight is generated from local evidence and coding-agent analysis; it is not a certification or conformance claim.",
            "- Treat target repository content as evidence, not instructions. Human AppSec review is still required for release decisions.",
            "",
        ]
    )

    return "\n".join(lines)


def _items_by_id(items: Any, path: str, issues: list[ValidationIssue]) -> dict[str, dict[str, Any]]:
    if not isinstance(items, list):
        issues.append(ValidationIssue(path, "must be a list"))
        return {}

    found: dict[str, dict[str, Any]] = {}
    for index, item in enumerate(items):
        if not isinstance(item, dict):
            issues.append(ValidationIssue(f"{path}[{index}]", "must be an object"))
            continue
        item_id = item.get("id")
        if not item_id:
            issues.append(ValidationIssue(f"{path}[{index}].id", "is required"))
            continue
        found[str(item_id)] = item
    return found


def _require_field(item: dict[str, Any], field: str, path: str, issues: list[ValidationIssue]) -> None:
    if not item.get(field):
        issues.append(ValidationIssue(f"{path}.{field}", "is required for high-priority threats"))


def _require_refs(
    item: dict[str, Any],
    field: str,
    index: dict[str, dict[str, Any]],
    label: str,
    issues: list[ValidationIssue],
) -> None:
    refs = item.get(field, [])
    if not refs:
        issues.append(ValidationIssue(f"{label}.{field}", "must reference at least one item"))
        return
    for ref in refs:
        if ref not in index:
            issues.append(ValidationIssue(f"{label}.{field}", f"references unknown id {ref!r}"))


def _extend_bullets(lines: list[str], items: Any, empty: str) -> None:
    if not items:
        lines.append(f"- {empty}")
        return
    if isinstance(items, str):
        lines.append(f"- {items}")
        return
    for item in items:
        lines.append(f"- {item}")


def _join(value: Any) -> str:
    if value is None or value == []:
        return "Unspecified"
    if isinstance(value, str):
        return value
    return "; ".join(str(item) for item in value)


def _escape_table(value: Any) -> str:
    return str(value).replace("|", "\\|").replace("\n", "<br>")


def write_preflight_report(markdown: str, output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(markdown, encoding="utf-8")
