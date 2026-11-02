import json
import subprocess
import sys
import unittest
from pathlib import Path

from engine import evaluate


def example():
    return json.loads(Path(__file__).with_name("example.json").read_text(encoding="utf-8"))


class AcceptanceTests(unittest.TestCase):
    def test_example_cli(self):
        proc = subprocess.run([sys.executable, "cli.py", "example.json"], capture_output=True, text=True)
        self.assertEqual(proc.returncode, 0, proc.stderr)
        self.assertEqual(json.loads(proc.stdout), evaluate(example()))

    def test_audit_distinguishes_failure_causes(self):
        result = evaluate(example())
        self.assertTrue(result["review_required"])
        self.assertEqual([r["status"] for r in result["citations"]],
                         ["verified", "quote_missing", "unknown_source", "ambiguous"])

    def test_explicit_unicode_offset_and_revision(self):
        data = example()
        data["citations"] = [{"source": "guide", "quote": "Save", "start": 2}]
        self.assertFalse(evaluate(data)["review_required"])
        data["citations"][0]["sha256"] = "0" * 64
        self.assertEqual(evaluate(data)["citations"][0]["status"], "stale_revision")
