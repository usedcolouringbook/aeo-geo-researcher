# Signal & Technical Researcher — Examples

What an investigative session looks like. Not a summary. A research chain.

---

## Example Session: Local Restaurant Not Appearing in AI Answers

**Client brief:** Italian restaurant in Austin. Owner asks why they don't appear when someone asks ChatGPT "best Italian restaurant in Austin."

**Pipeline context:** Client described a broad, unknown-cause problem. Procedure 01 (Signal Scan) ran first — surface sweep flagged crawler blocks and zero Bing indexation as the highest-priority angle, routed here for deep investigation. Client requested Procedure 03 (Source Audit) after reviewing findings before sharing with their web developer.

**Opening question asked:** The owner's question is about ChatGPT specifically, so the pivot is ChatGPT's pipeline (Bing-fed, OAI-SearchBot). Confirmed with one question: "We'll diagnose the ChatGPT pipeline first — that's Bing-indexed and crawled by OAI-SearchBot. Can I work from your public site, or do you have Search Console access too?"

**Client answer:** Public site only.

---

### Investigation Chain (branching — each pivot decides the next question)

**Pivot 1 — Access (gates everything below)**

Check `austintrattoria.com/robots.txt` directly in browser.

Found:
```
User-agent: GPTBot
Disallow: /

User-agent: OAI-SearchBot
Disallow: /
```

Finding: ChatGPT's crawlers are blocked. This is the most likely root cause. The site is invisible to the pipeline that feeds ChatGPT citations.

Uncertainty flag: GPTBot handles training data. OAI-SearchBot handles live retrieval. Both are blocked here — but even if unblocked, ChatGPT citations run through Bing indexation. This is a necessary but not sufficient fix.

**Branch decision:** Access is blocked — this is a root cause. I surface it now rather than burying it under a schema audit: "Before we go further — ChatGPT's crawlers are blocked at the door. No amount of schema or content fixes anything until this clears. I'll keep mapping so you have the full picture, but this is fix #1." The client said keep mapping, so I continue to indexation.

---

**Pivot 2 — Indexation (gates legibility)**

Search `site:austintrattoria.com` on bing.com.

Found: 0 results.

Finding: The site is not indexed in Bing. ChatGPT's retrieval pipeline is Bing-powered. A site not in Bing cannot be cited by ChatGPT regardless of robots.txt status.

Source: Direct Bing search — no tool required.

Verification: Run the same `site:` check on Google to establish baseline. Google shows 12 pages indexed. Bing gap is confirmed, not a site-wide crawl issue.

**Branch decision:** Not indexed in Bing — the second gate. The two access/indexation gates already fully explain ChatGPT non-appearance. Legibility (schema, chunking, density) is now downstream work, not the cause — so I investigate it for completeness but rank it below the two gates in the output.

---

**Pivot 3 — Legibility: Agent-native endpoints**

Check `austintrattoria.com/llms.txt` directly.

Found: 404.

Finding: No llms.txt present. Perplexity has documented adoption of llms.txt for citation prioritization. This is a missing signal for Perplexity specifically.

Uncertainty flag: llms.txt is not a confirmed citation factor for ChatGPT or Google AI Overviews. Do not overstate its impact. Flag as Perplexity-relevant only.

---

**Pivot 3 — Legibility: Schema markup**

Run `validator.schema.org` against the homepage URL — never read schema from my own page fetch, which strips `<script>` JSON-LD (see source-credibility.md → Tool Fidelity).

Found: No structured data detected at validator.schema.org. `unconfirmed · T2` — pending confirmation that the validator, not a markdown-stripped read, produced this.

Finding (flagged): If confirmed, missing Restaurant schema means AI systems cannot extract structured facts (cuisine type, hours, location, price range) without parsing unstructured prose. A "no schema" result is only `confirmed` once validator.schema.org or the Google Rich Results Test is run against the live URL — a markdown-based read would report the same false negative even if full schema were present.

Source: validator.schema.org — paste the live URL, read output directly. T2.

Verification: Cross-reference against Schema.org/Restaurant to confirm which fields are high-value (name, servesCuisine, address, openingHours, priceRange, aggregateRating).

---

**Pivot 3 — Legibility: Chunking quality**

Read three pages of the site: homepage, about page, menu page.

Found: Homepage is one paragraph of marketing prose. About page is 400 words with no headers. Menu page lists items with no descriptions or prices.

Finding: Content is not structured for chunking. RAG retrieval systems break content at natural boundaries — headers, list items, short dense blocks. Dense prose produces oversized, unfocused chunks that dilute factual density and reduce retrieval probability.

---

**Pivot 3 — Legibility: Factual density**

Count specific factual claims per page.

Homepage: 1 (cuisine type). No hours, no awards, no specific dishes, no neighborhood.
About: 3 (founding year, chef name, one award from 2019).
Menu: 0 structured claims (item names only, no descriptions).

Finding: Factual density is critically low. AI retrieval favors pages with dense, specific, verifiable claims. A page that states "Award-winning pasta since 2018, open Tuesday–Sunday 5–10PM, located in South Congress, Austin" is more citable than a page that says "We bring the flavors of Rome to Austin."

---

### Output Format

**Technical Audit Summary — austintrattoria.com**

| Signal | Status | Priority |
|--------|--------|----------|
| GPTBot / OAI-SearchBot access | Blocked | Critical |
| Bing indexation | Not indexed | Critical |
| llms.txt | Missing | Medium (Perplexity) |
| Schema markup | None detected (unconfirmed — verify at validator.schema.org) | High |
| Chunking structure | Poor | High |
| Factual density | Low | High |

**Root cause:** Bing non-indexation + crawler block = zero ChatGPT citation possibility regardless of content quality.

**Recommended sequence:** Unblock OAI-SearchBot → submit sitemap to Bing Webmaster Tools → implement Restaurant schema → restructure content for chunking → add factual density.

**What I cannot determine without GSC access:** crawl errors, index coverage, Core Web Vitals impact on crawl budget.

---

## How This Researcher Verifies Claims

- Schema claims: always validated at validator.schema.org, never assumed from page inspection
- Crawler access: always read robots.txt directly, never assumed from CMS defaults
- Bing indexation: always checked via live `site:` search, never inferred from Google status
- llms.txt: always checked via direct URL, never assumed absent without checking
- Uncertainty flags are mandatory when a finding is inferred rather than directly observed
- "I cannot confirm X without Y access" is a valid research output — never fabricate access you don't have

---

## Procedure 03 — Source Audit

Client requested an adversarial review before sharing findings with their web developer. 6 findings reviewed.

---

**Finding: GPTBot / OAI-SearchBot blocked — `confirmed · critical`**
Audit: **PASS**
robots.txt read directly from the live URL. Both crawlers explicitly disallowed. T2 observation. Status and tier are accurate.

---

**Finding: Bing indexation — 0 results — `confirmed · critical`**
Audit: **PASS**
Live `site:austintrattoria.com` on bing.com. Cross-referenced against Google (12 pages indexed) to confirm the gap is Bing-specific, not a site-wide crawl failure. T2. Status accurate.

---

**Finding: Schema markup — None detected — `unconfirmed · T2`**
Audit: **PASS — correctly tagged, but action dependency must be stated more explicitly**
The finding is correctly tagged `unconfirmed` pending validator.schema.org confirmation. However: the "Confirmed Gaps" section lists schema as a gap, which implies confirmed. It belongs in "Unconfirmed Flags" until the validator is run. Revision: move schema from Confirmed Gaps to Unconfirmed Flags with the note: "If validator confirms absence, add Restaurant schema including `servesCuisine`, `address`, `openingHours`, `priceRange`, `aggregateRating`."

---

**Finding: Chunking structure — Poor — `unconfirmed`**
Audit: **FLAGGED — tier not stated; basis is researcher observation only**
The finding rests on reading three pages: homepage (one paragraph of prose), about (400 words, no headers), menu (item names only). This is a T5 observation — the researcher's read of page structure. "Poor" is a judgment against the chunking benchmarks in `references/specialist-info/aeo-geo-signals.md`, which is a reasonable basis, but the tier should be stated: `unconfirmed · T5 (researcher observation)`. What would confirm it: run the page through a chunking simulator or compare heading hierarchy against the H1→H2→H3 standard in the audit checklist.

---

**Finding: Factual density — critically low — `unconfirmed`**
Audit: **FLAGGED — "critically low" label needs its benchmark cited**
The counts (1 fact on homepage, 3 on about, 0 on menu) are T2 (direct page read). The "critically low" label implies a threshold. That threshold comes from `references/specialist-info/geo-content-framework.md`: one hyperlinked statistic per 150–200 words is target density. Homepage is approximately 80 words with 1 non-linked claim — below target. The observation is sound but should cite the benchmark: "Homepage factual density: 1 claim / ~80 words — below target density of 1 per 150–200 words (`geo-content-framework.md` · T3 · high)."

---

### Gaps Not Surfaced

**Core Web Vitals / page speed not assessed.** ChatGPT citation likelihood drops sharply above FCP 1.13 seconds (`platform-behaviors.md` · T3). A restaurant site on shared hosting may fail this threshold. Should be investigated alongside Bing indexation fix.

**Google Business Profile not checked.** For local queries ("best Italian restaurant in Austin"), Google AI Overviews pull heavily from the local pack. GBP completeness is a parallel signal to on-site technical work — not covered in this session.

---

### Audit Summary

6 findings reviewed. 2 passed clean. 2 passed with labelling revisions needed. 1 required a priority category correction (schema → unconfirmed flags). 1 required benchmark citation.

**Actionable without revision:** Unblock OAI-SearchBot, submit sitemap to Bing Webmaster Tools.
**Requires verification before acting:** Schema (run validator first). Chunking and factual density (T5 basis — confirm before using as client-facing findings without that caveat).
