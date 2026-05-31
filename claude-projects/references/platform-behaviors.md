# Platform Intelligence Reference

Per-platform behavior for AI answer systems. Specialists never generalize across platforms — what works on Perplexity may fail on ChatGPT. Each platform is a separate research question.

---

## ChatGPT (OpenAI)

**Retrieval mechanism:** Bing-powered web search. Content must be indexed in Bing to appear in ChatGPT search results. Bing indexation is a prerequisite, not an assumption.

**Crawlers:**
- OAI-SearchBot: real-time search crawler
- GPTBot: training data crawler (blocking this does NOT affect ChatGPT search)

**Paid placement:** As of 2026, ChatGPT integrates sponsored results in some response contexts. Organic citation and paid placement are distinct — a competitor appearing in ChatGPT answers may be there through paid placement despite weak organic signals.

**Content behavior:** ChatGPT search synthesizes across multiple Bing-indexed pages. It does not consistently prefer any single source — it weights recency, authority (domain trust), and content specificity. FAQPage schema has limited observed lift in ChatGPT responses compared to Google AI Overviews.

**Citability threshold:** Only 15% of retrieved pages end up cited — retrieval and citation are separate gates. A site can be indexed and retrieved but still not cited if content doesn't pass the citability check (source: T3 — Averi.ai practitioner analysis).

**Quantified thresholds (T3 — Averi.ai, treat as directional):**
- 350K+ referring domains → 5x higher citation likelihood vs. ~200 domains
- FCP under 0.4 seconds → 3x citation likelihood vs. FCP over 1.13 seconds
- Preferred section length: 120–180 words with definite language and high entity density
- Reddit citations in ChatGPT responses surged 87% in mid-2025

**Shopping integration:** ChatGPT Shopping surfaces products from merchant feeds. Separate from organic search. Product schema alone is insufficient — merchant feed integration is required.

**What works:** Bing indexation + high domain authority + answer-first content structure + recency for time-sensitive queries.

**What doesn't:** llms.txt (not yet utilized for ranking). Schema markup has limited observed impact compared to Perplexity.

---

## Perplexity

**Retrieval mechanism:** Proprietary crawler (PerplexityBot) with aggressive crawl frequency. Builds its own index — not dependent on Google or Bing.

**Crawlers:** PerplexityBot. Blocks PerplexityBot = removed from Perplexity citation pool.

**Citation behavior:** Perplexity is the most citation-heavy platform — it surfaces 3–8 sources per response with inline attribution. Numbered footnote citations mean the URL appears explicitly; anchor text matters.

**Freshness weighting:** ~50% of citations come from content under 3 months old. New domains can earn citations within days on timely topics. Perplexity's fast index refresh is its most distinctive behavior — treat freshness as structural, not cosmetic (T3 — Averi.ai).

**llms.txt:** Perplexity has the highest confirmed adoption of llms.txt among major platforms. Including a well-structured llms.txt has observed impact on how Perplexity understands and cites a site.

**What works:** llms.txt + answer-first structure + high factual density + fresh content + PerplexityBot access in robots.txt. Timely topics benefit most from Perplexity's fast refresh.

**What doesn't:** Schema markup has limited observed impact — Perplexity reads content directly rather than relying on structured data signals as heavily as Google.

---

## Google (AI Overviews / Gemini)

**Retrieval mechanism:** Google's search index (Googlebot) + Gemini. AI Overviews pull from Google's existing index — ranking in core search is prerequisite to AI Overview inclusion.

**Crawlers:** Googlebot (core index), Google-Extended (AI Overviews and Gemini training). Blocking Google-Extended while allowing Googlebot removes content from AI features while maintaining search presence.

**Schema impact:** Highest schema impact of any platform. FAQPage, HowTo, and Speakable schema have confirmed lift in AI Overview citation. Complete Tier 1 schema (Organization + Article + FAQPage) correlates with ~40% more AI Overview appearances (T3). JSON-LD in `<head>` is strongly preferred.

**Citation source distribution (T3 — Averi.ai):** 59.6% of AI Overview citations come from URLs outside the top 20 organic results — AI Overviews do not replicate organic rankings. Blog content is the #1 cited page type. Triggers on 39.4% of informational queries.

**Reddit advantage:** 21–40% of AI Overview citations come from Reddit. Consumer-facing brands with authentic Reddit presence have a structural citation advantage.

**Business impact:** Cited brands earn 35% higher organic CTR and 91% higher paid CTR than non-cited brands (T3 — Averi.ai). Reach: 1.5B monthly users; 50% of searches show AI Overviews.

**Paid placement:** Google AI Overviews integrate shopping ads. Organic AI Overview presence and paid Shopping ads are separate systems with some overlap in appearance.

**What works:** Core search ranking + FAQPage/HowTo schema + entity authority (sameAs to Wikipedia/Wikidata) + Reddit presence + high factual density.

**What doesn't:** llms.txt has no confirmed impact on Google systems. Google-Extended blocking removes AI features without affecting core search.

---

## Google AI Mode

**Behavior:** Distinct from AI Overviews. High URL and domain volatility between identical queries.

**Key characteristics (T3 — Averi.ai):**
- Top citation predictor: domain traffic (SHAP value 0.63 — the single strongest predictor)
- 60%+ domain disappearance between identical query runs
- 80% URL disappearance between identical query runs
- 93% of sessions end without an external click

**Implication:** AI Mode citation is less predictable than AI Overviews. Domain-level authority (traffic, not just backlinks) is the lever. Don't optimize for specific URL placement — optimize the domain.

---

## Claude (Anthropic)

**Retrieval mechanism:** Training data by default. No real-time web access unless the user has enabled web search tools or the Claude instance is connected to an MCP server with web access.

**Training data cutoff:** Knowledge cutoff means Claude cannot cite content published after its training data was assembled — unless given tools.

**Credibility bar:** Claude applies a higher credibility threshold before citation compared to other platforms. Key signals: balanced multi-viewpoint coverage, nuanced treatment of complex topics, institutional authority signals, and evidence of original research or direct expertise (T3 — Averi.ai).

**MCP opportunity:** Claude is the primary platform where MCP servers create direct brand access points. A brand with an MCP server can be queried directly by Claude when Claude has tools enabled — bypassing retrieval competition entirely.

**llms.txt:** Anthropic's Claude.ai checks llms.txt. Relevant for Claude instances where web access is enabled.

**What works:** MCP server integration for direct agent access + institutional authority signals + balanced, nuanced content + inclusion in training data (long-term) + llms.txt for web-enabled Claude.

**What doesn't:** Schema markup has no observed impact on Claude's training-data-based responses. Promotional tone correlates negatively with citation (-26.19%, GEO-Bench study — T1).

---

## Microsoft Copilot

**Retrieval mechanism:** Bing-powered, similar to ChatGPT. Content must be indexed in Bing.

**Crawlers:** Bingbot. Same Bing indexation dependency as ChatGPT.

**Enterprise context:** Copilot is deeply integrated into Microsoft 365 (Word, Excel, Teams, Outlook). Enterprise Copilot instances may query internal SharePoint/OneDrive data rather than the web — different research question for B2B brands with enterprise customers.

**What works:** Bing indexation + domain authority + answer-first content structure.

---

## Off-Site Authority Building

Off-site presence directly influences AI citation rates, independently from on-site optimization. Each platform type creates citation opportunities through different mechanisms.

Source basis: T3 — Averi.ai guide. All figures directional; treat as working hypotheses, not verified constants.

### Reddit
- Most-cited domain overall in AI systems (~5,588 citations tracked in one analysis)
- 4–6 weeks of authentic community participation required before mentioning product; aggressive promotion in early weeks triggers downvotes, which harms citation probability
- Millions of brand mentions → 4x citation chances
- Critical for Google AI Overviews (21–40% of citations) and ChatGPT (87% citation surge in mid-2025)
- Research approach: check if brand, competitors, or category keywords appear in subreddit discussions; authentic mentions outweigh created content

### YouTube
- #2 most-cited domain in AI systems
- 10-minute video generates 1,500–2,000 words of citable transcript content
- Transcripts are indexed and retrieved by AI systems — video without transcript has low citation value
- Optimization: publish transcripts as companion articles; structure video content with clear section headings that translate to transcript readability

### LinkedIn
- Most-cited platform for professional and B2B queries
- Founder and key-person content generates 8x more engagement than company page content
- Optimal posting frequency: 2x per week
- Research approach: check if client's key people have active LinkedIn presence; founder-attributed content has higher citation probability in professional query contexts

### Review Platforms (G2, Capterra, Trustpilot)
- Verified review profiles → 3x higher ChatGPT citation chances
- Minimum viable presence: 5–10 reviews
- Review platforms function as independent entity verification — AI systems check multiple independent sources for brand claims

### Entity Directories (Crunchbase, Wikipedia, Wikidata, AngelList, industry databases)
- Entity recognition requires independent corroboration across sources
- Wikipedia and Wikidata are highest-authority sameAs targets — each connection strengthens entity graph
- Crunchbase is standard for tech/startup entity recognition
- Industry-specific directories matter for domain-specific citation contexts

---

## Platform-Specific Research Questions

When researching a client's platform presence, investigate separately for each platform:

1. Is the client indexed by this platform's crawler?
2. Does the client appear when their target queries are run on this platform?
3. If not: is it a technical gap (crawler block, indexation issue) or a content/authority gap?
4. If a competitor appears here: is it organic or paid?
5. What platform-specific signals does this client have or lack?
