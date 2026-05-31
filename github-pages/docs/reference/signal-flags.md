# Signal Flags

Every finding produced by a specialist is tagged with two attributes: **signal strength** and **priority level**.

## Signal Strength

Reflects how well-established a finding is.

| Flag | Color | Meaning | When to use |
|---|---|---|---|
| `confirmed` | Green | Directly observed or verified against a primary source | robots.txt read directly, schema validated at validator.schema.org, Bing `site:` check run live |
| `unconfirmed` | Amber | Inferred or reported — needs verification | Competitor behavior inferred from citations, platform behavior reported not tested |
| `emerging` | Red | Pattern observed in limited cases — not yet a consistent signal | New platform behavior seen in one or two instances, not yet documented across sessions |

## Source Credibility

Independent of signal strength, every finding also carries a **credibility tier** — how trustworthy the underlying source is. Strength is "how sure are we it's true"; credibility is "how good is the source." A finding can be `confirmed` from a weak source or `unconfirmed` from a strong one, so both are stated: `[finding] — [strength] · [tier] · [priority]`.

| Tier | Source type |
|---|---|
| `T1` | Official platform documentation / first-party announcements |
| `T2` | Direct, reproducible observation (live query, robots.txt, schema validator, Bing `site:`) |
| `T3` | Reputable empirical study with stated sample and date |
| `T4` | Vendor / practitioner analysis — directional |
| `T5` | Anecdote / community signal |

**Weighting rule:** when sources conflict, the higher tier governs; a T4/T5 claim is never reported as fact without a T1–T3 corroborator.

**Tool fidelity:** the researcher's own page fetch (HTML→markdown) strips `<script>` JSON-LD, so a "no schema" result from its own read is non-evidence — `unconfirmed` until verified at validator.schema.org or the Google Rich Results Test. Full detail in `references/source-credibility.md`.

## Priority Level

Reflects urgency and impact on the client's AI visibility.

| Level | Color | Meaning |
|---|---|---|
| `critical` | Purple | Blocks citation capability entirely — fix before anything else |
| `high` | Red | Significant impact on retrieval — high effort justified |
| `medium` | Amber | Notable gap — address after critical and high |
| `low` | Gray | Worth noting, low urgency — useful for backlog |

## How They Work Together

A finding tagged `confirmed · critical` is a verified blocker — act on it immediately.

A finding tagged `unconfirmed · high` is worth investigating further before acting — the impact is real if confirmed, but you need verification first.

A finding tagged `emerging · medium` is a trend to watch — not urgent enough to redirect resources, but worth tracking across future sessions.

## Investigator Confidence

Separate from signal strength and source credibility, findings also carry an **investigator confidence level** — how certain the investigator is about the implication or recommendation that follows from the evidence.

| Level | Meaning |
|---|---|
| `High` | Implication is unambiguous; inline tags are sufficient |
| `Moderate` | A plausible alternative interpretation exists; consequence statement required |
| `Low` | Evidence supports multiple interpretations; directional only; primary investigation needed before acting |

When confidence is Moderate or Low, the finding appends a consequence statement:
`[finding] — [strength] · [tier] · [priority] — Confidence: [level] — [what changes if the alternative is correct]`

High-confidence findings do not require the suffix. Full format and examples in `references/source-credibility.md` → Investigator Confidence.

## Session Close Rule

A session that produces findings must close with two mandatory elements before the conversation ends:

1. **Research Ledger** — confirmed findings, unconfirmed inferences, and what would change the conclusion (format in `references/source-credibility.md` → Research Ledger)
2. **Next Research Move** — one specific action, naming the exact query, tool, or check, and what it will resolve

Neither is optional. A session that ends without surfacing its uncertainty and naming the next move has not completed its investigation — it has paused it without a handoff.

## In the Research Brief

The Priority Matrix sorts all findings by priority level (critical → low) regardless of domain. This gives you a single ranked action list across the entire research session.
