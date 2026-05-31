# Competitive Intelligence Researcher — Examples

What an investigative session looks like. Not a summary. A research chain.

---

## Example Session: B2B SaaS Citation Landscape

**Client brief:** Project management SaaS targeting remote teams. Client wants to know who's winning AI citations for their core queries and what those competitors are doing differently.

**Packet received:** Client tracks Asana, Monday.com, and Notion as competitors. Primary goal is Perplexity and ChatGPT citations for "project management software for remote teams."

**Pipeline context:** Client had a clearly scoped competitive question. Procedure 01 (Signal Scan) was skipped — angle was specific enough to route directly to Procedure 02. Client requested Procedure 03 (Source Audit) before presenting findings to their marketing director.

**Opening question asked:** Which of these three are you most concerned about — the ones you already know about, or competitors you haven't seen yet?

**Client answer:** Both. We keep losing to tools we've never heard of.

---

### Investigation Chain

**Step 1 — Citation landscape mapping**

Run the target query live across three platforms. Record every citation — not just the top result.

Query: "project management software for remote teams"

ChatGPT response: Cited Notion, ClickUp, Linear, Basecamp. No mention of client's product. No mention of Asana or Monday.com.

Perplexity response: Cited ClickUp (with source URL), Notion, Asana, Teamwork. No client mention. Citations are hyperlinked — source pages visible.

Google AI Overview: Featured Asana in the overview text. ClickUp and Monday.com in the carousel. Client not present.

Finding: ClickUp and Notion appear across all three platforms — consistent organic authority. Asana appears in two. Linear appears in ChatGPT only. Client product appears in none.

---

**Step 2 — Paid placement check**

Inspect each platform's citation display for sponsored indicators.

ChatGPT (May 2026): Check for "Sponsored" label on any cited result. ClickUp shows no sponsored label. All citations appear organic.

Google AI Overview: Check for shopping/sponsored carousel distinction. The featured text (Asana) appears organic. The carousel includes what appears to be paid shopping placements — flagged as unverified without advertiser confirmation.

Perplexity: No paid placement mechanism confirmed as of this research date. All citations treated as organic unless Perplexity announces otherwise.

Uncertainty flag: Paid placement detection is imprecise without advertiser-side confirmation. Treat all "sponsored" flags as probable, not certain.

---

**Step 3 — Unknown competitor surfacing**

Review the full citation list. Flag any competitor the client did not mention.

Surfaced: Linear, Basecamp, Teamwork, Height.app.

Finding: Linear is appearing in ChatGPT for remote team queries despite being positioned as an engineering tool. This is a citation bleed — Linear's technical content density may be triggering retrieval for adjacent queries. Worth investigating separately.

Source: Direct query responses — no third-party tool required for initial discovery. Semrush used next to verify authority.

---

**Step 4 — Winning signal analysis**

For each consistently cited competitor (ClickUp, Notion, Asana), check three signals:

**ClickUp:**
- robots.txt: OAI-SearchBot and GPTBot allowed
- llms.txt: present at clickup.com/llms.txt (verified via direct URL)
- Schema: SoftwareApplication schema on product pages (validator.schema.org confirmed)
- Bing: site:clickup.com returns 45,000+ results
- Factual density: feature pages list specific capabilities, pricing tiers, integration counts

**Notion:**
- robots.txt: all major AI crawlers allowed
- llms.txt: not present (checked notion.so/llms.txt — 404)
- Schema: minimal structured data
- Bing: highly indexed
- Factual density: high — comparison pages, use case pages with specific claims

**Asana:**
- robots.txt: AI crawlers allowed
- llms.txt: present
- Schema: SoftwareApplication + FAQ schema on key pages
- Bing: 80,000+ results indexed
- Factual density: extensive — ROI statistics, integration lists, named customer outcomes

Finding: ClickUp and Asana have complete technical foundations. Notion relies on content volume and authority despite lighter schema. All three have Bing indexation. Client has none of these.

Source for authority cross-check: Semrush domain overview for each competitor.

Verification: Bing indexation confirmed via direct `site:` search for each domain. Schema confirmed via validator.schema.org. robots.txt read directly — not inferred.

---

**Step 5 — Gap identification**

Map what cited competitors have that client does not.

| Signal | ClickUp | Notion | Asana | Client |
|--------|---------|--------|-------|--------|
| AI crawler access | ✅ | ✅ | ✅ | ❌ |
| Bing indexation | ✅ | ✅ | ✅ | ❌ |
| llms.txt | ✅ | ❌ | ✅ | ❌ |
| Schema markup | ✅ | Partial | ✅ | ❌ |
| Comparison content | ✅ | ✅ | ✅ | ❌ |
| Named integrations | ✅ | ✅ | ✅ | ❌ |

Finding: Client is missing every foundational signal. The gap is technical first, content second. Comparison pages (e.g., "ClickUp vs Asana") are a high-citation content pattern across all three competitors — client has none.

---

### Output Format

**Citation Landscape — Project Management / Remote Teams**

**Who is winning:** ClickUp (all platforms), Asana (Google + Perplexity), Notion (all platforms)

**Unknown competitors surfaced:** Linear (ChatGPT bleed), Teamwork (Perplexity), Height.app (Perplexity)

**Organic vs paid:** All confirmed citations appear organic. Google carousel flagged as possibly paid — unverified.

**Client gap:** Technical foundations missing entirely. No Bing indexation, no AI crawler access, no schema. Content gaps are secondary to infrastructure gaps.

**Priority recommendation:** Fix technical signals before any content investment. Route to Signal & Technical specialist for full audit.

---

## How This Researcher Verifies Claims

- Citation findings: always run live queries on the actual platform — never assumed from third-party tools
- Paid placement: always inspect the platform UI directly — never assumed organic without checking
- Competitor technical signals: always verified via direct URL check (robots.txt, llms.txt) and validator.schema.org
- Bing indexation: always checked via `site:` search — never inferred from Google status
- Authority signals: Semrush used for cross-reference only — not as the primary citation explanation
- "Unverified" and "flagged" are mandatory outputs when a finding cannot be confirmed directly

---

## Procedure 03 — Source Audit

Client requested adversarial review before presenting to their marketing director. 7 findings reviewed.

---

**Finding: ClickUp llms.txt present at clickup.com/llms.txt**
Audit: **PASS**
Direct URL check confirmed. T2 observation. Correctly stated.

---

**Finding: Notion llms.txt — not present (404)**
Audit: **PASS**
Direct URL check confirmed 404. T2. Correctly stated. The finding also correctly notes that Notion is cited despite no llms.txt — this is a meaningful observation, not an oversight.

---

**Finding: Asana — llms.txt present, FAQPage + SoftwareApplication schema confirmed**
Audit: **FLAGGED — verification depth inconsistent with ClickUp**
ClickUp's llms.txt was verified with an explicit URL (`clickup.com/llms.txt`). Asana's llms.txt is stated as "present" without showing the URL confirmed. Similarly, Asana's schema is described as "SoftwareApplication + FAQ schema on key pages" — the ClickUp entry says "validator.schema.org confirmed" but the Asana entry doesn't. Apply the same verification standard: "asana.com/llms.txt — present (direct URL check, 2026-05-27). Schema: validator.schema.org run against asana.com — SoftwareApplication and FAQPage confirmed." Without this, the Asana findings are `unconfirmed`, not `confirmed`.

---

**Finding: Linear citation bleed — "technical content density may be triggering retrieval for adjacent queries"**
Audit: **FLAGGED — causal mechanism is inference, not finding**
The observation is confirmed: Linear appears in ChatGPT for remote team queries (direct query, T2). The explanation — "technical content density triggering retrieval for adjacent queries" — is the researcher's hypothesis, not a confirmed mechanism. Tag separately: "Linear appears in ChatGPT for [query] — `confirmed · T2`. Mechanism: `unconfirmed · T4` — likely content density bleed, but not verified." The client should receive the observation, not the explanation, as a confirmed finding.

---

**Finding: Google AI Overview carousel — possibly paid, unverified**
Audit: **PASS**
Correctly flagged. Not presented as confirmed. The uncertainty is explicit.

---

### Gaps Not Surfaced

**Client's own Bing indexation not checked.** The investigation maps what competitors have; it doesn't confirm whether the client has the same baseline. If the client also has zero Bing indexation (like the restaurant example), the gap is more severe than "missing technical signals" — it's a prerequisite failure. Should be routed to Signal & Technical to confirm before the client acts on any competitive recommendation.

**Referring domain count not compared.** ChatGPT citation likelihood scales with referring domain count (`platform-behaviors.md` — 350K+ domains = 5x likelihood, T3). The investigation used Semrush for authority cross-reference but didn't surface the domain count comparison. If ClickUp has 400K+ referring domains and the client has 12K, that gap dwarfs the llms.txt gap in citation impact.

---

### Audit Summary

7 findings reviewed. 3 passed clean. 1 passed with caveat (Google carousel). 2 flagged for revision (Asana verification depth, Linear causal mechanism). 1 gap identified as prerequisite (client's own Bing indexation).

**Actionable without revision:** ClickUp and Notion signal analysis. Paid placement assessment.
**Requires revision before sharing:** Asana findings need direct URL verification. Linear finding should separate confirmed observation from unconfirmed mechanism.
**Requires additional investigation:** Client's own Bing indexation. Referring domain count comparison.
