from __future__ import annotations

import json
import unittest
from pathlib import Path

from ai_appsec_harness.evaluator import evaluate, render_markdown


ROOT = Path(__file__).resolve().parents[1]


class EvaluatorTests(unittest.TestCase):
    def setUp(self) -> None:
        self.catalog = json.loads((ROOT / "data/control-catalog.seed.json").read_text(encoding="utf-8"))

    def test_rag_control_selection(self) -> None:
        intake = {
            "system": {"name": "RAG", "system_type": "rag", "lifecycle_stage": "design"},
            "capabilities": ["chat", "rag", "document_analysis"],
            "data": {"classifications": ["internal", "confidential"]},
            "evidence": [],
        }

        results = evaluate(intake, self.catalog)
        control_ids = {result.control["id"] for result in results}

        self.assertIn("AIH-001", control_ids)
        self.assertIn("AIH-002", control_ids)
        self.assertIn("AIH-004", control_ids)
        self.assertIn("AIH-005", control_ids)
        self.assertIn("AIH-009", control_ids)
        self.assertNotIn("AIH-010", control_ids)

    def test_mcp_agent_control_selection(self) -> None:
        intake = {
            "system": {"name": "MCP Agent", "system_type": "agent", "lifecycle_stage": "design"},
            "capabilities": ["tool_use", "mcp", "external_actions"],
            "data": {"classifications": ["internal"]},
            "evidence": [],
        }

        results = evaluate(intake, self.catalog)
        control_ids = {result.control["id"] for result in results}

        self.assertIn("AIH-003", control_ids)
        self.assertIn("AIH-006", control_ids)
        self.assertNotIn("AIH-012", control_ids)

    def test_harness_tooling_control_selection(self) -> None:
        intake = {
            "system": {"name": "Harness Import", "system_type": "agent_tooling", "lifecycle_stage": "design"},
            "capabilities": ["tool_use", "mcp", "code_generation"],
            "data": {"classifications": ["public"]},
            "evidence": [],
        }

        results = evaluate(intake, self.catalog)
        control_ids = {result.control["id"] for result in results}

        self.assertIn("AIH-010", control_ids)
        self.assertIn("AIH-011", control_ids)
        self.assertIn("AIH-012", control_ids)

    def test_attestation_renderer_keeps_cli_caveat(self) -> None:
        intake = {
            "system": {
                "name": "Tiny Chat",
                "owner": "Engineering",
                "system_type": "llm_app",
                "lifecycle_stage": "design",
                "description": "Minimal test system.",
            },
            "capabilities": ["chat"],
            "data": {"classifications": ["internal"]},
            "evidence": [],
        }

        markdown = render_markdown(intake, evaluate(intake, self.catalog))

        self.assertIn("# AI AppSec Attestation Gap Report: Tiny Chat", markdown)
        self.assertIn("requires human AppSec validation", markdown)
        self.assertIn("Do not claim OWASP AISVS or CSA AI conformance", markdown)


if __name__ == "__main__":
    unittest.main()
