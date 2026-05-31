# Procedure 02 — Deep Investigation

**Purpose:** Focused specialist work on the angle identified in Procedure 01 (or directly from orchestrator intake). This is where research happens — not scanning, not auditing, but investigating a specific question using the right specialist.

---

## How to Enter Procedure 02

From the orchestrator packet or scan output, a primary specialist has been identified. Open that specialist's folder and pass the full packet. The specialist runs its investigation sequence and produces findings.

If the scan (Procedure 01) was run: include the scan output in the packet trail before handing to the specialist. The specialist reads it and skips any dimension already confirmed in the scan.

If the scan was skipped: the specialist starts from scratch with the intake packet.

---

## Specialist Routing (from Orchestrator)

| If the primary question is... | Go to... |
|---|---|
| Technical foundations — why content isn't retrieved | `1-signal-technical/` |
| Who's winning AI citations and what signals they have | `2-competitive-intelligence/` |
| How a specific platform behaves for this content type | `3-platform-intelligence/` |
| What content is missing that AI agents can't answer | `4-content-gap/` |
| MCP, agent pipelines, agentic marketing | `5-agentic-discovery/` |

Multi-specialist sessions: complete one specialist's investigation before opening the next. Append to the trail after each.

---

## During Investigation

Each specialist follows its own rules file. Investigation is **branching, not a checklist**: the specialist opens by establishing its pivot fact (per `references/specialist-info/diagnostic-patterns.md` → Part B), and the value of that pivot determines the next question. Signal & Technical confirms access before indexation before legibility; Competitive Intelligence confirms a competitor is actually cited before analyzing signals. The investigation ends when:
- The specialist has produced findings across its full investigation sequence, OR
- A confirmed critical gap has been found that blocks all downstream work — in that case, surface it immediately and ask the client whether to stop and fix or continue mapping

The specialist does not move to Procedure 03 automatically. Wait for the client to request a source audit, or offer it at the end of the investigation output.

---

## Ending Procedure 02

After the specialist produces findings, close with:

1. **Research ledger** — confirmed / unconfirmed / what would change the conclusion (see `references/source-credibility.md` → Research Ledger)
2. **Next research move** — one specific action
3. **Offer Procedure 03** — "Would you like a source audit on these findings before we act on them? Procedure 03 runs an adversarial review to challenge what we've produced."
