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

    def test_outer_and_hole_boundaries(self):
        self.assertEqual([r["status"] for r in evaluate(example())],
                         ["inside", "outside", "boundary", "boundary", "outside"])

    def test_orientation_and_large_coordinates(self):
        data = example()
        offset = 10**20
        data["rings"] = [[[x+offset,y] for x,y in reversed(ring)] for ring in data["rings"]]
        data["points"] = [[x+offset,y] for x,y in data["points"]]
        self.assertEqual([r["status"] for r in evaluate(data)],
                         [r["status"] for r in evaluate(example())])

    def test_reject_degenerate_ring(self):
        with self.assertRaises(ValueError):
            evaluate({"rings": [[[0,0],[1,1]]], "points": []})
