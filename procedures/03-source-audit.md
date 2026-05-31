# Procedure 03 — Source Audit

**Purpose:** Adversarial review of the findings produced in Procedure 02. The auditor's job is to challenge what the researcher produced — not to validate it.

A clean audit with zero findings is a failed audit. If everything checks out, the auditor didn't look hard enough.

---

## Auditor Posture

The source auditor is not the same voice as the specialist. Switch posture:

- The specialist produces findings optimistically — it is trying to answer the client's question
- The auditor reviews findings skeptically — it is trying to break them

The auditor is not hostile to the client. It is hostile to weak claims in the research output. The goal is to hand the client findings they can actually act on — not findings that collapse when someone asks "where did that stat come from?"

---

## What the Auditor Checks

Work through every finding in the Procedure 02 output in order.

### 1. Citation Traceability
For every statistic, benchmark, or specific claim:
- Can it be traced to a named source?
- Does the named source actually exist and say what the finding claims?
- What tier is that source? Does the finding's confidence level match the tier?

Flag: `[finding] cites [source] — source is [accessible/not accessible/not named]. Tier: [T1–T5]. Finding confidence [matches/overstates] source tier.`

### 2. Confirmation Status Accuracy
For every `confirmed` finding:
- Was it actually directly observed (T2: live query, direct URL check, schema validator)?
- Or was it inferred from observable signals and labelled `confirmed` by mistake?

Flag: `[finding] is tagged confirmed but rests on [inferred / T4 source / unverifiable claim]. Should be unconfirmed.`

### 3. T4/T5 Reliance
Scan the entire output for T4/T5 sources being treated as authoritative:
- Vendor statistics presented as benchmarks without a T1–T3 corroborator
- "Industry consensus" claims without a primary source
- Directional data presented as verified data

Flag: `[finding] relies on T4/T5 source without T1–T3 corroborator. Must be tagged unconfirmed or dropped.`

### 4. Platform Behavior Staleness
For any finding about platform behavior (how ChatGPT retrieves, what Perplexity cites, etc.):
- Does the finding include a date or "as of" qualifier?
- Platform behavior changes frequently — an undated platform behavior claim is not a confirmed finding

Flag: `[finding] about [platform] behavior has no date qualifier. Platform behavior in this area changes; finding should carry an "as of [date]" tag or be tagged emerging.`

### 5. Gaps the Specialist Didn't Surface
What questions did the investigation fail to ask?
- Which confirmed gaps don't have a clear path to resolution?
- Which `unconfirmed` flags were never resolved?
- Is there a dimension the specialist didn't investigate that could change the priority order?

Flag: `[dimension] was not investigated. If [X] turns out to be true, the priority recommendation changes.`

---

## Audit Output Format

```
## Source Audit — [Session / Specialist]

### Findings Challenged

**[Finding 1 from Procedure 02]**
Audit: [PASS / FLAGGED]
[If flagged: what's wrong and what would fix it]

**[Finding 2]**
Audit: [PASS / FLAGGED]
...

### Unchallenged Findings
[List findings that passed audit — these are the ones the client can act on with confidence]

### Gaps Not Surfaced
[Dimensions the investigation missed, with why they matter]

### Revised Priority
[If the audit changed the priority order, state the revised order here]

### Audit Summary
[N] findings reviewed. [N] passed. [N] flagged. [N] gaps surfaced.
The [X] findings that passed are actionable. The [N] flagged findings require [specific verification] before acting.
```

---

## What the Auditor Never Does

- Validates findings just because the client seems satisfied with them
- Accepts "this is what the industry says" as a source
- Ignores a statistic because it came from a reference document rather than the specialist's live output — reference documents can contain T4 claims that need the same scrutiny
- Produces a clean audit to avoid tension — that is a failure of the procedure
