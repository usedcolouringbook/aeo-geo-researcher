# Quick Start — Claude Code

## What You Need

- Claude Code installed (`npm install -g @anthropic-ai/claude-code`)
- Python 3.x (for the research brief export)
- PyYAML (`pip install pyyaml`)

## Setup (one time)

```bash
cd aeo-geo-researcher
claude
```

That's it. Claude Code uses the folder as its project context.

---

## Running a Session

Start a chat. Describe your situation in plain English. The Orchestrator will ask three questions — one at a time. Answer each before it continues.

Examples:
- "I run a local restaurant. We don't appear when people ask AI tools for restaurant recommendations nearby."
- "I want to map which platforms are best for our content type — we're a B2B newsletter."

---

## Generating the Research Brief

At the end of a session, say: **"Write brief.yaml and generate the report."**

The AI will:
1. Write `brief.yaml` with the structured session data
2. Run `python generate_report.py`
3. Your research brief opens in the browser automatically

**Manual report generation:**

If you want to regenerate the report without a new session:

```bash
python generate_report.py
```

The script reads the existing `brief.yaml` and opens `report.html` in your browser.

**Export to PDF:**
Browser → File → Print → Save as PDF
