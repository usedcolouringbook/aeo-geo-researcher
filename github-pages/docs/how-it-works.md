# How It Works

## The Session Pipeline

Every session follows a three-step procedure:

```
01 · Signal Scan → 02 · Deep Investigation → 03 · Source Audit
```

| Step | What happens |
|---|---|
| **01 · Signal Scan** | Rapid surface sweep across all signal dimensions — crawl access, schema, platform visibility, content structure, off-site presence. Identifies the highest-priority angle before going deep. |
| **02 · Deep Investigation** | The right specialist investigates the identified angle. Produces tagged findings with source credibility tiers. Ends with a research ledger. |
| **03 · Source Audit** | Adversarial review of the findings. Challenges citation traceability, confirmation status accuracy, T4/T5 source reliance, and platform behavior staleness. A clean audit with zero findings is a failed audit. |

Simple, scoped sessions can skip the scan and go directly to the specialist. Procedure 03 is offered at the end of any investigation that produces findings the client plans to act on.

## The Six-Specialist System

AEO/GEO Researcher is built around six specialists in a routing architecture. The Orchestrator owns intake. The five domain specialists own research. No specialist engages until the Orchestrator has built a research packet.

```
User → Orchestrator (3-question intake) → routing decision → specialist(s) → Research Brief
```

## The Intake Sequence

The Orchestrator asks three questions, one at a time, before routing:

1. "What are you trying to figure out or solve?"
2. "What do you already know about this — any research, gut sense, or prior attempts?"
3. "What sources have you already looked at, if any?"

These populate the **research packet** — the shared data structure that moves between specialists. A specialist who receives a populated packet does not re-ask what the previous specialist already answered.

## The Reframe

Between intake and routing, the Orchestrator sharpens the client's question against a library of known failure patterns (`references/diagnostic-patterns.md`). Most clients arrive with a framing that conflates two different problems — "we're invisible in AI" can mean access, authority, or presence, each with an opposite fix. The Orchestrator surfaces the sharper question in the client's own terms ("did you mean *cited in the answer* or *recommended as a vendor*?") and lets them confirm. It sharpens out loud; it never silently reinterprets, and it never invents a reframe where no pattern matches. The confirmed answer becomes the angle the specialist investigates.

## The Research Packet

Every handoff between Orchestrator and specialist uses the packet schema defined in `references/manifest.yaml`. The packet carries:

- Client profile (type, goal)
- Research brief (angle, existing knowledge, sources reviewed)
- Routing decision (primary specialist, reason)
- Trail (every specialist that has touched the packet)
- Gaps (unknowns flagged before research begins)

## Signal Strength

Every finding is tagged with its signal strength:

| Signal | Meaning |
|---|---|
| `confirmed` | Directly observed or verified against a primary source |
| `unconfirmed` | Inferred or reported — needs verification |
| `emerging` | Pattern observed but not yet established as a consistent signal |

## The Specialist Follow-Up

Each specialist opens with one investigative question that sets the pivot for its investigation, then branches on what it finds rather than running a fixed checklist. Signal & Technical establishes access before indexation before legibility; Competitive Intelligence verifies a competitor is actually cited before analyzing its signals. The pivot the opener establishes decides which question comes next — this is what makes the output investigative rather than a summary of a predetermined list.

## Session End

Every session ends with:
- A **research ledger** — confirmed findings, inferred findings, and what would change the conclusion
- A gap identified — what's still unknown
- A next research move — one concrete action

Multiple sessions build on each other. The packet carries what's been established forward.

## Citation Discipline

Every finding carries two labels — verification status (`confirmed / unconfirmed / emerging`) and source credibility tier (`T1`–`T5`). These are independent axes.

A statistic that cannot be traced to a named source at a named tier is a hypothesis, not a finding. Specialists tag unverifiable stats `unconfirmed · T5` rather than presenting them as established benchmarks. The Source Audit (Procedure 03) is specifically designed to catch and flag this.

## The Research Brief Export

At session end, request a research brief. The AI structures findings into an audit-style deliverable with sections for executive summary, signal legend, findings by domain, priority matrix, gap map, and next research move.

[Claude Projects delivery →](research-brief/claude-projects.md) | [Claude Code delivery →](research-brief/claude-code.md)
