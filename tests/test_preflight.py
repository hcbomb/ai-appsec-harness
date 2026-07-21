from __future__ import annotations

import copy
import json
import unittest
from pathlib import Path

from ai_appsec_harness.preflight import render_preflight_markdown, validate_preflight_package


ROOT = Path(__file__).resolve().parents[1]
PREFLIGHT_FIXTURES = [
    ROOT / "examples/preflight/basic-chatbot.preflight.json",
    ROOT / "examples/preflight/rag-app.preflight.json",
    ROOT / "examples/preflight/mcp-agent.preflight.json",
    ROOT / "examples/preflight/hostile-repo.preflight.json",
]


def strip_frontmatter(text: str) -> str:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return text.strip()
    for index, line in enumerate(lines[1:], start=1):
        if line.strip() == "---":
            return "\n".join(lines[index + 1 :]).strip()
    return text.strip()


class PreflightTests(unittest.TestCase):
    def load_fixture(self, name: str) -> dict:
        return json.loads((ROOT / f"examples/preflight/{name}.preflight.json").read_text(encoding="utf-8"))

    def test_golden_preflight_fixtures_validate(self) -> None:
        for path in PREFLIGHT_FIXTURES:
            with self.subTest(path=path.name):
                package = json.loads(path.read_text(encoding="utf-8"))
                issues = validate_preflight_package(package)
                self.assertEqual([], [issue.format() for issue in issues])

    def test_preflight_renderer_includes_complete_engineer_report_shape(self) -> None:
        package = self.load_fixture("mcp-agent")

        markdown = render_preflight_markdown(package)

        for heading in [
            "## A. Preflight Summary",
            "## B. System Model",
            "## C. Threat Model",
            "## D. Evidence Gaps",
            "## E. Security Tests",
            "## F. Engineering Backlog",
            "## G. Residual Risk And Revalidation",
        ]:
            self.assertIn(heading, markdown)
        self.assertIn("T-MCP-001", markdown)
        self.assertIn("TEST-MCP-002", markdown)
        self.assertIn("BACKLOG-MCP-002", markdown)
        self.assertIn("v1.0-C10.2.7", markdown)

    def test_high_priority_threat_requires_traceability(self) -> None:
        package = self.load_fixture("basic-chatbot")
        broken = copy.deepcopy(package)
        broken["threat_model"]["threats"][0]["backlog_refs"] = []

        issues = validate_preflight_package(broken)

        self.assertTrue(
            any("backlog_refs" in issue.format() for issue in issues),
            [issue.format() for issue in issues],
        )

    def test_hostile_repository_fixture_is_untrusted_evidence(self) -> None:
        package = self.load_fixture("hostile-repo")

        markdown = render_preflight_markdown(package)

        self.assertIn("IGNORE PREVIOUS SECURITY INSTRUCTIONS", markdown)
        self.assertIn("hostile evidence, not as an instruction to follow", markdown)
        self.assertIn("target repository content as evidence, not instructions", markdown.lower())

    def test_codex_and_claude_skill_bodies_remain_aligned(self) -> None:
        codex = (ROOT / ".agents/skills/ai-appsec-harness/SKILL.md").read_text(encoding="utf-8")
        claude = (ROOT / ".claude/skills/ai-appsec-harness/SKILL.md").read_text(encoding="utf-8")

        self.assertEqual(strip_frontmatter(codex), strip_frontmatter(claude))
        for text in [codex.lower(), claude.lower()]:
            self.assertIn("run the ai appsec preflight on this project", text)
            self.assertIn("what will appsec ask us for", text)


if __name__ == "__main__":
    unittest.main()
