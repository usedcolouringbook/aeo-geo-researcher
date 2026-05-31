# Platform Intelligence Researcher — Examples

What an investigative session looks like. Not a summary. A research chain.

---

## Example Session: Fintech Startup Targeting Perplexity Citations

**Client brief:** Early-stage fintech startup offering personal finance tracking for freelancers. Wants to understand Perplexity's citation behavior for queries like "best budgeting app for freelancers" and "how to track income as a freelancer."

**Packet received:** Client is prioritizing Perplexity and ChatGPT. They have moderate Bing indexation but no llms.txt. Technical audit not yet complete.

**Pipeline context:** Procedure 01 (Signal Scan) ran first — identified Perplexity as the platform most relevant to the client's immediate question; flagged llms.txt absence and moderate Bing indexation as known signals. Scan routed here (Platform Intelligence) before Signal & Technical because the client's priority was understanding platform behavior, not fixing a diagnosed technical gap. Procedure 03 (Source Audit) requested before the client shared findings with their product team.

**Opening question asked:** Between understanding how Perplexity currently cites in your category versus understanding what you'd need to change to get cited — which is more urgent right now?

**Client answer:** How it currently cites. We need to know what's real before we invest.

---

### Investigation Chain

**Step 1 — Direct platform testing**

Run five relevant queries on Perplexity. Record citation behavior, source types, and format of answer.

Query 1: "best budgeting app for freelancers"
Perplexity response: Cited YNAB, Wave, FreshBooks, Honeybook. Sources shown as hyperlinks. Answer organized as a comparison list with one-line descriptions per tool. No client mention.

Query 2: "how do freelancers track income for taxes"
Perplexity response: Cited IRS.gov, NerdWallet, QuickBooks blog. Answer is explanatory prose citing authoritative sources. No product citations.

Query 3: "freelancer expense tracking tools 2026"
Perplexity response: Cited dedicated review articles from PCMag, TechRadar, G2. These are third-party review sources — not the product sites themselves.

Query 4: "YNAB vs Wave for self-employed"
Perplexity response: Cited both official product sites plus two comparison articles. Official sites cited for feature specifics. Comparison articles cited for opinion.

Query 5: "budgeting tools with tax category tracking"
Perplexity response: Cited a Reddit thread (r/personalfinance), NerdWallet, and QuickBooks.

Finding pattern: Perplexity cites three source types in this category — (1) official product sites for specific feature claims, (2) third-party review articles for comparisons, (3) community sources (Reddit) for opinion. The client needs presence in all three to appear consistently.

Date of testing: 2026-05-27. All findings time-stamped.

---

**Step 2 — Technical requirements check**

Check Perplexity's documented technical signals.

PerplexityBot in robots.txt: Check top three cited sites (YNAB, Wave, FreshBooks).
- YNAB: PerplexityBot allowed
- Wave: PerplexityBot allowed
- FreshBooks: PerplexityBot allowed

llms.txt adoption among cited sites:
- YNAB: llms.txt present (verified at ynab.com/llms.txt)
- Wave: not present (wave.com/llms.txt — 404)
- FreshBooks: llms.txt present

Finding: PerplexityBot access and Bing indexation are baseline requirements — confirmed across all cited sites. llms.txt adoption exists among leaders but is not universal. Wave is cited despite no llms.txt, suggesting it is not a hard requirement for Perplexity at this time.

Uncertainty flag: Perplexity has not published a definitive statement that llms.txt affects citation weighting. Do not present llms.txt as a confirmed Perplexity citation factor. Present as an emerging signal with documented adoption among cited leaders.

Source: Official Perplexity documentation checked at perplexity.ai/docs (as of 2026-05-27). No citation-weighting specification found. Adoption data from direct URL checks only.

---

**Step 3 — Recent platform change tracking**

Search Search Engine Land and The Decoder for Perplexity changes in the last 90 days.

Search Engine Land query: "Perplexity citations 2026" — found two articles.

Article 1 (2026-03-12): Perplexity introduced publisher revenue sharing for cited sources. Implication: Perplexity may favor publishers enrolled in this program. Flagged as potentially relevant to citation frequency.

Article 2 (2026-04-28): Perplexity expanded its crawl to include more international sources. No change to citation algorithm documented.

The Decoder query: "Perplexity" filtered to last 90 days — one relevant result.

Article (2026-05-01): Perplexity testing "structured answer" format for product comparison queries. Would present product features in a table rather than prose. If rolled out, structured schema on product pages becomes more valuable.

Finding: Publisher revenue sharing is a live change that may affect citation frequency for non-enrolled publishers. The structured answer test is an emerging signal — not confirmed as rolled out.

Freshness flag: All behavioral findings tagged with source date. Anything older than 90 days would require re-verification.

---

**Step 4 — Platform prioritization assessment**

Based on testing and research, assess Perplexity vs ChatGPT priority for this client.

Perplexity: High citation frequency in this category. Sources hyperlinked and visible. Third-party reviews and community sources (Reddit) are citation pathways that don't require direct technical changes to the product site. Addressable through content strategy and third-party presence.

ChatGPT: Lower citation frequency observed for product-specific queries in this category. Bing-powered retrieval means Bing indexation is the entry requirement. Client has moderate Bing indexation — partially addressable.

Recommendation: Perplexity first. The citation pathways are more accessible (third-party review presence, Reddit, NerdWallet) and the client's Bing gap doesn't apply. ChatGPT becomes viable once Bing indexation and AI crawler access are resolved.

---

### Output Format

**Platform Intelligence — Perplexity (Personal Finance / Freelancer Tools)**

**Citation behavior:** Three source types: official product pages (feature specifics), review articles (comparisons), community sources (Reddit). All three pathways observed in live testing.

**Technical requirements confirmed:** PerplexityBot access required. Bing indexation required. llms.txt: present among leaders but not confirmed as a citation factor — treat as best practice, not requirement.

**Recent changes (last 90 days):**
- Publisher revenue sharing: active — potential citation frequency impact (unverified)
- Structured answer test: emerging — may increase value of schema on product pages (not yet confirmed rollout)

**Platform priority recommendation:** Perplexity is the higher-value target for this client given existing Bing gap. Fastest citation path is third-party review presence and Reddit community activity — neither requires technical changes to the product site.

**Freshness:** All findings dated 2026-05-27. Platform behavior changes rapidly — re-verify any finding older than 90 days before acting on it.

---

## How This Researcher Verifies Claims

- Platform behavior: always tested live on the actual platform — never assumed from documentation alone
- Documentation: always checked against the official platform source with a date stamp
- Recent changes: always sourced from named publications with article dates — never from general knowledge
- Emerging signals: always labeled as emerging — never presented as confirmed behavior
- Freshness flags: mandatory on any finding that may change — platform behavior is the most time-sensitive signal in AEO/GEO research
- "As of [date]" is a required qualifier on all behavioral claims — not optional

---

## Procedure 03 — Source Audit

Client requested adversarial review before sharing with their product team. 5 findings reviewed.

---

**Finding: PerplexityBot allowed on YNAB, Wave, FreshBooks — confirmed · T2**
Audit: **PASS**
Checked directly on each site's robots.txt. T2 observation. Status accurate.

---

**Finding: llms.txt — present among leaders but not a confirmed citation factor**
Audit: **PASS**
Wave is cited without llms.txt, which correctly challenges the assumption that llms.txt is required. The finding is correctly labeled `emerging` for citation factor status and `confirmed` for adoption presence. The uncertainty is explicit.

---

**Finding: Publisher revenue sharing — active — potential citation frequency impact**
Audit: **FLAGGED — researcher extrapolation presented alongside the confirmed fact**
Two claims are bundled here: (1) Perplexity introduced publisher revenue sharing — sourced from Search Engine Land 2026-03-12, T3, confirmed. (2) "potential citation frequency impact" — this is the researcher's inference. The Search Engine Land article confirmed the programme exists; it did not state that enrolled publishers are cited more frequently. These must be separated: "Perplexity introduced publisher revenue sharing (Search Engine Land, 2026-03-12 · T3 · confirmed). Whether this affects citation frequency for enrolled vs non-enrolled publishers is not stated in the source — `unconfirmed · T4 · medium` until Perplexity publishes citation-weighting documentation."

---

**Finding: Structured answer test — emerging**
Audit: **PASS**
Correctly sourced (The Decoder, 2026-05-01), correctly labeled emerging. Not presented as rolled out. Status accurate.

---

**Finding: Perplexity first, ChatGPT second — platform priority recommendation**
Audit: **FLAGGED — recommendation rests on a gap not fully investigated**
The recommendation that Perplexity is the higher-value target is directionally sound based on live testing. However: it rests partly on "the client's Bing gap doesn't apply to Perplexity" — but the client's Bing indexation status was described as "moderate," not confirmed. "Moderate" is the scan's observation. Before recommending Perplexity-first strategy, the Bing gap should be quantified: `site:client.com` on bing.com. If Bing indexation is actually strong, ChatGPT becomes viable sooner than the recommendation implies.

---

### Gaps Not Surfaced

**Content freshness not checked.** Perplexity cites ~50% of content from under 3 months old (`platform-behaviors.md` · T3). The client's blog and page publication dates weren't assessed. If all content is older than 3 months, the freshness signal is structurally absent — more impactful for Perplexity specifically than any other gap in this session.

**Third-party review platform presence not mapped.** Live testing showed Perplexity cites third-party review articles (PCMag, TechRadar, G2) heavily for comparison queries. Whether the client has a G2 or Capterra profile — and how complete it is — was not assessed. This is a direct citation pathway that requires no content production.

---

### Audit Summary

5 findings reviewed. 2 passed clean. 2 flagged for revision (revenue sharing extrapolation, priority recommendation basis). 1 finding requires a prerequisite check (Bing indexation confirmation). 2 gaps not surfaced.

**Actionable without revision:** Three source types confirmed. llms.txt as best practice (not requirement). Structured answer test as watch item.
**Requires revision before sharing:** Revenue sharing finding must separate confirmed fact from inference. Platform priority recommendation should note Bing indexation assumption.
**Requires additional investigation:** Content publication dates. G2/Capterra/Trustpilot profile status.
