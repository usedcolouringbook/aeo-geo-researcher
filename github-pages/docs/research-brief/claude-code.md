# Research Brief — Claude Code

## Automatic Export

At the end of a session, say: **"Write brief.yaml and generate the report."**

The AI:
1. Writes `brief.yaml` — the structured session data in YAML format
2. Calls `python generate_report.py`
3. The script reads `brief.yaml`, injects data into `renderer.html`, writes `report.html`, and opens it in your browser

You see the rendered report immediately. Export to PDF via browser print.

## Manual Regeneration

To regenerate the report from an existing session (without a new AI interaction):

```bash
python generate_report.py
```

Requires `brief.yaml` to exist in the project directory. The script exits with an error if it's missing.

## The brief.yaml Format

```yaml
client:
  type: "B2B SaaS, Series A"
  goal: "Improve AI citation rate for enterprise HR queries"
  date: "2026-05-28"

session:
  angle: "Technical signal audit — why content isn't appearing"
  specialists_engaged:
    - "1-signal-technical"

findings:
  - domain: "Signal & Technical"
    summary: "Two critical blockers preventing ChatGPT citation."
    items:
      - signal: "GPTBot blocked in robots.txt"
        status: confirmed
        priority: critical
        detail: "Direct observation. OAI-SearchBot also blocked."

gaps:
  - "Cannot verify Bing indexation without GSC access"

next_move: "Unblock OAI-SearchBot, recheck Bing indexation in 48 hours"
```
