#!/usr/bin/env python3
"""
AEO/GEO Researcher — Research Brief Generator

Usage: python generate_report.py [--no-browser]

Reads brief.yaml, injects data into renderer.html, writes report.html,
opens in browser. Pass --no-browser to skip browser open (testing).
"""
import json
import sys
import webbrowser
from pathlib import Path

try:
    import yaml
except ImportError:
    print("Error: PyYAML not installed. Run: pip install pyyaml")
    sys.exit(1)

BASE = Path(__file__).parent
BRIEF_PATH = BASE / "brief.yaml"
RENDERER_PATH = BASE / "renderer.html"
REPORT_PATH = BASE / "report.html"
PLACEHOLDER = "// __BRIEF_DATA_PLACEHOLDER__"


def main():
    no_browser = "--no-browser" in sys.argv

    if not BRIEF_PATH.exists():
        print("Error: brief.yaml not found.")
        print("Run a research session and ask the AI to write brief.yaml first.")
        sys.exit(1)

    if not RENDERER_PATH.exists():
        print("Error: renderer.html not found. Is this the correct project directory?")
        sys.exit(1)

    with BRIEF_PATH.open() as f:
        data = yaml.safe_load(f)

    template = RENDERER_PATH.read_text(encoding="utf-8")

    if PLACEHOLDER not in template:
        print("Error: renderer.html is missing the data placeholder comment.")
        print(f"Expected: {PLACEHOLDER}")
        sys.exit(1)

    injected = template.replace(
        PLACEHOLDER,
        f"const BRIEF = {json.dumps(data, indent=2, ensure_ascii=False)};"
    )

    REPORT_PATH.write_text(injected, encoding="utf-8")
    print(f"Report generated: {REPORT_PATH}")

    if not no_browser:
        webbrowser.open(f"file://{REPORT_PATH.resolve()}")
        print("Opening in browser. Use File → Print to export PDF.")


if __name__ == "__main__":
    main()
