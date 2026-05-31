# AEO Audit Checklist Reference

A structured audit protocol across five categories. Specialists use this as a diagnostic framework — not a deliverable. The research brief defines what to investigate; this checklist identifies what to look for.

Source basis: aeo-platform.com checklist (T3), Averi.ai guide (T3), HubSpot best practices (T3). Where sources agree, treat as directional consensus. Where sources conflict, note the discrepancy and apply source-credibility tiers.

---

## Category 1: Crawlability & AI Access

| Check | What to verify |
|---|---|
| robots.txt — AI crawlers | GPTBot, OAI-SearchBot, Google-Extended, Anthropic-AI, PerplexityBot, ClaudeBot all listed; allow/disallow decision documented |
| llms.txt | Exists at site root; follows spec format; key pages listed |
| HTTP status | Priority pages return 200 — AI crawlers rarely follow 301/302 redirects |
| Page speed | FCP under 0.4s (ChatGPT citation threshold); LCP under 2.5s; FID under 100ms; CLS under 0.1 |
| JavaScript dependency | Critical content present in initial HTML response — AI crawlers may not execute JS |
| Sitemap | All priority pages included; submitted to Google Search Console and Bing Webmaster Tools |
| Bing indexation | Verified for ChatGPT/Copilot access (Bing-dependent platforms invisible to non-indexed content) |

**Critical note:** Blocking GPTBot does NOT affect ChatGPT search. GPTBot is for training data only. OAI-SearchBot is the ChatGPT search crawler. Diagnose these separately.

---

## Category 2: Structured Data & Schema

| Check | What to verify |
|---|---|
| Organization schema | Present on homepage; includes `@id`, `name`, `url`, `logo`, `description`, `sameAs` array |
| sameAs targets | LinkedIn, Wikipedia/Wikidata (if applicable), Crunchbase, Twitter/X, industry directories |
| Article schema | On all blog/editorial content; includes `headline`, `author` (Person with `name` + `url`), `datePublished`, `dateModified`, `publisher` |
| FAQPage schema | On all FAQ-structured content; `mainEntity` array with `Question` objects and `acceptedAnswer` |
| HowTo schema | On step-by-step instructional content |
| Schema validation | All markup passes Google Rich Results Test — not just Schema.org validator |
| JSON-LD placement | In `<head>`, not `<body>` |
| Audit tool limitation | Markdown-based audit tools strip `<script>` tags and will report "no schema" as false negative. Verify via raw page source or Rich Results Test. |

**Impact:** Complete Tier 1 schema (Organization + Article + FAQPage) correlates with ~40% more Google AI Overview appearances (T3 — Averi.ai).

---

## Category 3: Content Structure & Citability

| Check | What to verify |
|---|---|
| Answer Capsule | 40–60 word direct answer at start of each major section |
| Front-loading | Key facts in first 30% of content (44.2% of LLM citations drawn from this zone) |
| Section length | 120–180 words per section (optimal for AI citation) |
| Extractable blocks | Each block meaningful standalone, without surrounding context |
| Heading hierarchy | H1 → H2 → H3 consistent; no skipped levels |
| FAQ presence | 5–7 self-contained Q&A pairs; each answer independently citable |
| Factual density | One hyperlinked stat per 150–200 words; all stats link to T1–T3 sources |
| Content length | Pillar topics: 2,900+ words; general threshold for AI citation research |
| Tables vs prose | Multi-attribute comparisons in tables (chunk as single unit; retrieve whole) |
| Visual content | Images, charts, or video present (40% more citations; detailed alt text required) |
| Freshness | dateModified updated after significant changes; stats under 18 months old |
| Author credentials | Detailed author bio with credentials, role, and external links |
| Entity specificity | Full names before abbreviations; acronyms spelled out; consistent terminology |
| Tone check | Informational, not promotional; balanced viewpoints; no keyword stuffing |

---

## Category 4: Authority & Off-Site Signals

| Check | What to verify |
|---|---|
| Reddit presence | Brand mentioned authentically; avoid overt promotion in first 4–6 weeks of account activity |
| YouTube presence | Transcripts available (10-min video = 1,500–2,000 words of citable content) |
| LinkedIn presence | Company page active; founder/key person content present |
| Review platforms | G2, Capterra, or Trustpilot profile exists; minimum 5–10 reviews |
| Crunchbase/AngelList | Profile exists and accurate — entity recognition signal |
| Industry directories | Listed in relevant industry databases |
| Wikipedia | Page exists for entity-level authority (if applicable) |
| Domain authority | Referring domain count checked; 350K+ domains = 5x ChatGPT citation likelihood (T3) |
| NAP consistency | Name, Address, Phone consistent across all platforms |
| About page | Comprehensive; company history, team, mission, contact |

**Off-site priority by platform:**
- Google AI Overviews: Reddit presence is structural (21–40% of citations)
- ChatGPT: Referring domain count is a top predictor
- Perplexity: Fresh content and direct crawlability; off-site less critical than technical access
- Claude: Institutional authority; balanced third-party coverage

---

## Category 5: Monitoring & Measurement

| Check | What to verify |
|---|---|
| Query set defined | 50–100 brand-relevant queries identified; covers branded + category queries |
| SoM baseline established | Share of Model baseline measured per platform before optimizations |
| Citation vs mention tracking | Citations (URL referenced) tracked separately from brand mentions |
| AI referral traffic | GA4 custom channel for AI-platform referral traffic configured |
| Competitor SoM | Relative competitor citation trends tracked, not just absolute numbers |
| Audit cadence | Monthly manual audit (20 queries × 3 platforms, ~45 min); automated tools supplementary |
| Tool stack | Monitoring tool selected from: Profound (enterprise), Otterly, SE Ranking, AiCarma, FalconRank.ai |

**Audit frequency:** Quarterly full audit, or after major content updates or algorithm changes. Monthly for active optimization campaigns.

---

## Audit Triage Order

When a client has limited time/budget, run in this sequence — each layer depends on the one before it:

1. **Crawlability first** — If AI crawlers can't reach the content, nothing else matters
2. **Schema second** — Verification mechanisms that AI systems use before trusting content
3. **Content structure third** — Citability depends on crawlability + schema being confirmed
4. **Authority fourth** — Off-site signals amplify on-site signals; don't optimize off-site before on-site is solid
5. **Monitoring last** — Measurement is only meaningful once the optimization foundation exists
