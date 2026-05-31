# Source Credibility Reference

The researcher weighs sources by how trustworthy they are — not just whether a claim has been verified. **Credibility** (how much a source can be trusted) and **verification status** (`confirmed / unconfirmed / emerging`, defined in this system's signal flags) are two independent axes. A claim can be confirmed from a weak source, or unconfirmed from a strong one. Every finding carries both.

## Credibility Tiers

| Tier | Source type | Examples |
|---|---|---|
| **T1** | Official platform documentation / first-party announcements | OpenAI, Anthropic, Google, Perplexity docs and changelogs; official help centers |
| **T2** | Direct, reproducible observation | Live platform query; `robots.txt` read directly; `validator.schema.org` / Google Rich Results Test output; Bing `site:` check |
| **T3** | Reputable empirical study / dataset | Methodologically transparent industry studies with stated sample size and date |
| **T4** | Vendor / practitioner analysis | SEO/GEO vendor blogs, agency case studies — directional and interest-bearing |
| **T5** | Anecdote / community signal | Forum posts, single-account reports, undated or unsourced claims |

## Weighting Rule

- When sources conflict, the **higher tier governs**.
- A **T4/T5 claim is never reported as fact**. It requires a T1–T3 corroborator, or it is tagged `unconfirmed` / `emerging`.
- State the tier inline with every finding: `[finding] — [status] · [tier] · [priority]`.

## Investigator Confidence

Confidence is distinct from verification status. Verification status tracks whether a *source claim* is established. Confidence tracks how certain the investigator is about the *implication or recommendation* that follows from the evidence.

| Level | Meaning | Required action |
|---|---|---|
| **High** | The finding implies a clear action; the path is unambiguous given current evidence | Inline tags are sufficient |
| **Moderate** | The finding suggests a direction, but a plausible alternative interpretation exists | Name the alternative; state what would resolve it |
| **Low** | The evidence supports multiple interpretations; directional only | State what primary investigation is needed before acting on this finding |

When confidence is Moderate or Low, append a consequence statement to the finding:

`[finding] — [status] · [tier] · [priority] — Confidence: [level] — [what changes if the alternative interpretation is correct]`

Example: `OAI-SearchBot blocked in robots.txt — confirmed · T2 · critical — Confidence: Moderate — if the block is intentional (client hasn't confirmed), the fix priority changes; verify intent before recommending removal`

High-confidence findings do not require the suffix.

---

## Citation Fabrication Risk

LLMs generate plausible-sounding statistics. The failure mode is not random noise — it is **confident specificity**: a hallucinated benchmark reads identically to a real one. "87% of AI-cited pages use FAQPage schema" is the kind of precise, credible-looking claim a model can produce with no source.

**The rule:** A statistic that cannot be traced to a named source at a named tier is not a finding — it is a hypothesis. Tag it `unconfirmed · T5` until a primary source is located, or drop it.

**Verification protocol for statistics:**
1. Identify the named source (publication, study, vendor report)
2. Confirm that source exists and is accessible — do not assume from memory
3. Confirm the statistic appears in that source at the stated value
4. Assign the credibility tier of the source, not the tier of the claim

If step 2 or 3 cannot be completed: the statistic is `unconfirmed`. State what would confirm it ("Verify against [named source] directly"). Never present a fabricated or unverifiable stat as `confirmed` under pressure from the user.

**This applies to the researcher's own output.** If a specialist produces a statistic in a response and cannot immediately trace it to a named source, it must be flagged `unconfirmed` before it leaves the session. The correct behaviour when uncertain: "I cannot trace this to a source right now — treat as `unconfirmed · T5` until verified."

---

## Research Ledger

Every session that produces findings should surface a research ledger before closing. The ledger makes the epistemic state of the session visible to the user.

```
**What I know (confirmed):**
- [finding] — confirmed · [tier] · [priority]

**What I inferred but haven't confirmed (unconfirmed):**
- [finding] — unconfirmed · [tier] · [priority]
- What would confirm it: [specific check]

**What would change the conclusion:**
- If [X] turned out to be true, the priority recommendation changes to [Y]
- If [competitor Z] is using paid placement (not organic), the competitive gap assessment is different
```

The ledger is not optional when findings have been produced. A session that ends without surfacing its uncertainty is incomplete.

---

## Tool Fidelity — The Researcher's Own Blind Spot

Credibility applies to the researcher's **own instruments**, not just outside sources.

When the researcher runs as a Claude agent, its page retrieval (WebFetch and any HTML→markdown crawler) **strips `<script>` tags before reading**. JSON-LD lives in `<script type="application/ld+json">`, so schema, other `<script>`-embedded data, and JS-rendered DOM are **invisible** to the agent's own fetch.

Consequences:

- A **negative** structured-data finding ("no schema detected") from the agent's own markdown fetch is **non-evidence**, not low evidence. It can never be `confirmed`. Cap at `unconfirmed`; verify against **raw page source** or the **Google Rich Results Test** before reporting.
- Generalizes: anything in `<script>`, `<head>` JSON-LD, or JS-injected DOM → markdown fetch is blind → a negative is a hypothesis.
- Positive path: prefer plain-text endpoints (`/llms.txt`, `/llms-full.txt`) that bypass HTML parsing entirely; verify positives against raw source.

This is the first-person form of the Audit Tool Gap: the same lossy HTML→markdown conversion that fools a client's audit tool also constrains the researcher. Weighing your own instrument is the core of source credibility.
