# Content Gap Researcher — Examples

What an investigative session looks like. Not a summary. A research chain.

---

## Example Session: Healthcare Clinic Content Gaps

**Client brief:** Primary care clinic in Denver. Wants to appear in AI answers for health-related queries their patients ask before and after appointments. Technical audit is complete — signal specialist confirmed AI crawlers are allowed, Bing indexation is solid, basic schema is in place.

**Packet received:** Technical foundations confirmed clear. Content goal is appearing in ChatGPT and Google AI Overviews for patient education queries.

**Pipeline context:** Procedure 01 (Signal Scan) was skipped — Signal & Technical had already run in a prior session and its findings are in the trail. Procedure 02 entered here directly with clean technical foundations confirmed. Procedure 03 (Source Audit) was offered at session close; client accepted before handing the gap map to their content team.

**Opening question asked:** Are we trying to capture a specific set of queries you know patients ask, or map a whole topic cluster, or own a category like "primary care in Denver"?

**Client answer:** Specific queries. Patients ask us the same questions every day before appointments. We want AI to answer those questions and mention us.

---

### Investigation Chain

**Step 1 — Target query identification**

Build the query list from the client's described patient questions, then expand via research tools.

Client-stated questions:
- "What to expect at your first physical exam"
- "How to prepare for a blood draw"
- "What does a cholesterol test show"
- "When should I get a physical exam"

AlsoAsked.com — run each query, collect related question clusters:

"What to expect at your first physical exam" returns:
- "What happens during a routine physical exam"
- "How long does a physical exam take"
- "What do doctors check at a physical"
- "What should I not do before a physical"
- "Is a physical exam the same as a check-up"

Google People Also Ask — run same queries, collect additional angles:
- "What is the difference between a physical and a wellness visit"
- "Do I need to fast before a physical exam"
- "What blood tests are done at a physical"

Finding: The client's known queries are a subset of a larger cluster. Three high-frequency adjacent queries (fasting, blood tests at a physical, wellness vs physical distinction) are not on the client's radar and are likely higher-traffic than the original list.

---

**Step 2 — Live query testing**

Run each query in ChatGPT, Perplexity, and Google. Record who appears and what format the answer takes.

Query: "What to expect at your first physical exam"

ChatGPT: Answers in prose with numbered steps. No clinic cited — answer drawn from Mayo Clinic and Healthline content. Format: explanatory walkthrough.

Perplexity: Citations from WebMD, Cleveland Clinic, Verywell Health. Answer is a bulleted list of exam components. Format: structured list.

Google AI Overview: Featured snippet from Mayo Clinic. Below: People Also Ask carousel. No local clinic cited anywhere.

Finding: This query is dominated by national health authority sites (Mayo Clinic, Cleveland Clinic, WebMD, Verywell Health). A local clinic cannot displace these sites for the generic query. However —

Query: "What to expect at your first physical exam in Denver"

ChatGPT: No local clinic cited. Generic answer.

Perplexity: No local clinics cited. Same national sources.

Google AI Overview: Local pack appears below. One local clinic cited in AI Overview text — a competitor.

Finding: Adding a local modifier creates a citation opportunity. The national sites do not optimize for local queries. A Denver-specific page for this question has a realistic path to AI citation.

---

**Step 3 — Format matching**

Map each target query to the format that AI systems are using to answer it.

| Query | AI answer format | Required content format | Schema type |
|-------|-----------------|------------------------|-------------|
| What to expect at a physical exam | Numbered walkthrough | Step-by-step process | HowTo |
| How to prepare for a blood draw | Bulleted list | Short, specific bullets | HowTo |
| What does a cholesterol test show | Definition + explanation | Short definition, then context | FAQPage |
| When should I get a physical | Age-based table | Structured table by age group | FAQPage |
| Wellness visit vs physical exam | Comparison | Side-by-side distinction | FAQPage |

Finding: HowTo schema is the correct format for process queries. FAQPage schema for question/definition queries. Neither format is currently on the client's site.

---

**Step 4 — Existing content mapping**

Audit the client's site for existing content that covers any of these queries.

Found:
- One blog post: "Your annual physical — what to expect" (2019, 800 words, no schema, dense prose)
- One services page: "Primary Care" (no patient education content)
- No pages addressing cholesterol, blood draws, wellness visits, or preparation instructions

Finding: One piece of relevant content exists but is structured incorrectly for AI retrieval (dense prose, no schema, outdated). The rest of the query cluster has zero coverage.

---

**Step 5 — Gap map and priority sequencing**

Sequence gaps by: (1) citation feasibility, (2) patient volume, (3) schema readiness.

| Gap | Citation feasibility | Priority |
|-----|---------------------|----------|
| "What to expect at physical exam in Denver" | High — local modifier opens space | 1 |
| "How to prepare for a blood draw" | High — no strong local or national competitors | 2 |
| "What does a cholesterol test show" | Medium — WebMD dominates but structured answer possible | 3 |
| "Wellness visit vs physical exam" | High — underserved query, comparison format | 4 |
| "When should I get a physical" | Medium — age table format, high competition | 5 |

Technical dependency: all pages require HowTo or FAQPage schema. Route to Signal & Technical specialist to confirm implementation path before content is produced.

---

### Output Format

**Content Gap Map — Denver Primary Care Clinic**

**Target query cluster:** Patient education — pre/post appointment questions

**Queries with clear citation path:**
1. "What to expect at a physical exam in Denver" — local modifier, HowTo format, no current local competition
2. "How to prepare for a blood draw" — underserved, specific, HowTo format
3. "Wellness visit vs physical exam" — underserved comparison query, FAQPage format

**Existing content to update:** 2019 physical exam blog post — restructure to HowTo schema, add local modifier, increase factual density

**What to build new:** Four pages targeting gaps 2–5, each with appropriate schema

**Technical dependency:** HowTo and FAQPage schema implementation required — confirm with Signal & Technical before production begins

**What I cannot determine:** Search volume for these queries (requires Semrush/Ahrefs access not provided). Citation feasibility assessment is based on live AI testing, not traffic data.

---

## How This Researcher Verifies Claims

- Query gaps: always tested live in the actual AI platform — never assumed from keyword tools alone
- Format requirements: determined by observing what format AI systems are actually using, not by guessing
- Existing content audit: always read the actual pages, not inferred from site navigation
- Local modifier opportunity: confirmed by running both generic and local versions of the query live
- Technical prerequisites: always flagged before content recommendations — content strategy without technical diagnosis is second-step-first
- "I cannot determine X without Y access" is a valid and required output when data is missing

---

## Procedure 03 — Source Audit

Client accepted audit offer before handing the gap map to their content team. 5 findings reviewed.

---

**Finding: Local modifier creates a citation opportunity — competitor appears in Google AI Overview for Denver query**
Audit: **PASS — with freshness caveat required**
Both generic and local versions of the query were run live and results recorded. The observation is T2. However: competitor AI Overview appearances are volatile — `platform-behaviors.md` notes 60%+ URL disappearance between identical Google AI Mode runs. The finding should carry a date and a note that single-test observations require re-verification before acting: "Competitor [name] appeared in Google AI Overview for 'physical exam Denver' — `confirmed · T2 · 2026-05-27`. Re-verify before building content against this gap; AI Overview citations are volatile."

---

**Finding: Adjacent queries from AlsoAsked are "likely higher-traffic than the original list"**
Audit: **FLAGGED — traffic claim has no source**
AlsoAsked returns related questions — it does not provide traffic data. "Likely higher-traffic" is an inference with no cited basis. What the tool actually confirms: these are related questions users ask. That's the finding. The traffic implication requires Semrush or Ahrefs, which the client didn't provide. Revision: "Adjacent queries identified via AlsoAsked (T4 tool): [list]. Relative traffic volume unknown — requires keyword tool access to prioritize by search volume."

---

**Finding: Citation feasibility ratings — High/Medium/High for gaps 1, 3, 4**
Audit: **FLAGGED — basis for ratings not stated**
"High feasibility" for gap 1 rests on: local modifier tested live, no local clinic found in Google AI Overview for that specific query (T2). That's a sound basis. But the rating for gap 3 ("What does a cholesterol test show — Medium, WebMD dominates") rests on the researcher's judgment that WebMD is hard to displace — this is `unconfirmed · T4`. Gap 4 ("Wellness visit vs physical — High, underserved") rests on live query testing that returned no strong result — T2. Each feasibility rating should state its basis inline rather than appearing as a judgment call.

---

**Finding: 2019 blog post — 800 words, no schema, dense prose**
Audit: **PASS**
Direct page read. Word count, schema absence, and structure are T2 observations. Year (2019) confirms content freshness issue against the 18-month citation decay threshold in `geo-content-framework.md`. Finding is accurate and well-sourced.

---

**Finding: HowTo and FAQPage schema required — route to Signal & Technical before production**
Audit: **PASS**
Technical dependency correctly flagged. Content team cannot implement schema without engineering confirmation of the CMS path. The prerequisite routing is appropriate and prevents wasted content production.

---

### Gaps Not Surfaced

**Competitor schema not checked.** The competitor that appeared in Google AI Overview for the Denver local query — does it have LocalBusiness + FAQPage schema? If yes, schema is a prerequisite for local AI Overview, not just a best practice. This changes the urgency tier for the schema implementation recommendation.

**Existing blog post's FAQ opportunity missed.** The 2019 blog post is flagged for restructuring to HowTo schema. But the content also covers multiple sub-questions (fasting, timing, what doctors check) that could be structured as a FAQPage alongside the HowTo. A dual-schema approach on the updated page doubles the citation surface area without requiring a second page.

---

### Audit Summary

5 findings reviewed. 2 passed clean. 1 passed with freshness caveat. 2 flagged for revision (traffic inference, feasibility rating basis).

**Actionable without revision:** Local modifier opportunity. Existing blog post update. Technical dependency routing.
**Requires revision before sharing:** AlsoAsked finding must remove traffic inference. Feasibility ratings need basis statements.
**Requires additional investigation:** Competitor schema status. Dual-schema opportunity on updated blog post.
