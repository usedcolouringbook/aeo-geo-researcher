# AEO/GEO Signal Reference

The technical and structural signals that determine whether AI systems retrieve, cite, and recommend content. Specialists draw from this reference — they do not restate it verbatim.

---

## How RAG Retrieval Works (And Why It Matters)

Most AI answer systems follow this pipeline:

1. **Query arrives** — user asks a question
2. **Query embedded** — the query is converted to a vector embedding
3. **Index searched** — the embedding is compared against stored content embeddings via vector similarity
4. **Chunks retrieved** — the top N most similar content chunks are returned
5. **Response generated** — the model generates an answer grounded in the retrieved chunks

**Implication for GEO:** Content that doesn't survive chunking doesn't get cited. A 3,000-word article where the key fact appears in paragraph 14 may never be retrieved if paragraph 14's chunk doesn't match the query embedding. Answer-first structure — stating the key fact immediately, before context — directly improves retrieval rate.

**Chunking boundary types:**
- Paragraph-based (most common): each paragraph is a chunk
- Heading-based: each H2/H3 section is a chunk
- Token-based: fixed token count (512–1024 tokens typical), regardless of content boundaries
- Hybrid: heading-based with token cap fallback

**Implication:** Content with clear heading hierarchy and short, fact-dense paragraphs chunks cleanly. Long, flowing prose chunks poorly — key facts may straddle chunk boundaries and never retrieve cleanly for either half.

---

## Agent-Native Endpoints

### llms.txt
**What it is:** A plain-text file at `/llms.txt` that tells AI agents about the site — what it does, who it serves, key pages, and usage permissions.

**Format:**
```
# [Site Name]
> [One-sentence description of what the site is and does]

[Optional: 2-3 sentences of context agents should carry when using this site]

## Key Pages
- [/page-1]: [What this page covers]
- [/page-2]: [What this page covers]

## Usage
[What agents may and may not do with this content]
```

**Placement:** Must be in the site root (`/llms.txt`). Subdirectory placement defeats the purpose — most agents check root only.

**Platform support (as of mid-2026):** Perplexity recognizes it. Anthropic's Claude.ai checks it. ChatGPT does not yet use it for retrieval prioritization. Google has not adopted it. Adoption is growing.

### llms-full.txt
**What it is:** Full site content in flat, agent-readable format. Agents read it in one request instead of crawling individual pages.

**When to use:** Sites where key content is spread across many pages, or where page structure makes crawling inefficient. High-value for knowledge-dense sites (documentation, research, FAQs).

**Risk:** Exposes all site content in one flat file. Content behind authentication or intended to be discovery-gated should be excluded.

---

## Schema Markup (JSON-LD)

### The Audit Tool Gap
Most AI audit tools convert pages to markdown before reading them. Markdown strips `<script>` tags. JSON-LD lives in `<script type="application/ld+json">` blocks. **A site with comprehensive schema markup will appear schema-free to a naive markdown-based audit.** Always verify schema against raw page source, not audit tool output.

### High-Value Schema Types for AEO

| Schema Type | When to use | AEO signal |
|---|---|---|
| Organization | Every brand site | Entity recognition, sameAs linkage |
| LocalBusiness | Physical location businesses | Local AI citation, hours, location |
| FAQPage | Actual FAQ content | Direct extraction into AI answers |
| HowTo | Step-by-step instructional content | Procedural query citation |
| Article | News, blog, editorial content | Freshness signal, author authority |
| Product | E-commerce, product pages | Shopping AI, product queries |
| Review / AggregateRating | Reviews, ratings | Trust signal, citation with ratings |
| Speakable | Content intended for voice/audio AI | Voice assistant citation |
| BreadcrumbList | Site navigation | Context signal for AI crawlers |

**Common mistakes:**
- Using FAQPage markup on content that isn't structured as actual Q&A
- Placing JSON-LD in the `<body>` rather than `<head>` (some crawlers miss it)
- Missing `sameAs` property on Organization schema — this is how AI systems link your entity to Wikipedia, LinkedIn, Wikidata, and other authority sources

### sameAs — Entity Authority Linker
The `sameAs` property connects your Organization schema to external authority sources. Each `sameAs` link tells AI systems: "this is the same entity as the one described at this URL."

**High-value sameAs targets:**
- Wikipedia page (highest authority signal)
- Wikidata entry
- LinkedIn company page
- Crunchbase profile
- Google Business Profile
- Industry directory listings

---

## Crawl Signals

### Crawler Taxonomy

| Crawler | Platform | Purpose | Block to remove from |
|---|---|---|---|
| OAI-SearchBot | ChatGPT | Real-time web search via Bing | ChatGPT search results |
| GPTBot | OpenAI | Model training data | Future OpenAI training (not ChatGPT search) |
| PerplexityBot | Perplexity | Real-time citation index | Perplexity responses |
| Google-Extended | Google AI | AI Overviews / Gemini training | Google AI features |
| Googlebot | Google | Core search index | Google search entirely (high risk) |
| ClaudeBot | Anthropic | Claude training data | Anthropic training data |

**Key distinction:** Blocking GPTBot only removes content from OpenAI training data — it does NOT prevent ChatGPT's web search from finding content. OAI-SearchBot is the search crawler.

### robots.txt for AI Crawlers

```
# Allow all AI search crawlers (recommended for AEO)
User-agent: OAI-SearchBot
Allow: /

User-agent: PerplexityBot
Allow: /

# Block from training data without blocking search
User-agent: GPTBot
Disallow: /

# Block from Google AI features while keeping search index
User-agent: Google-Extended
Disallow: /
```

**Bing indexation dependency:** ChatGPT's web search is Bing-powered. Content that isn't indexed in Bing is invisible to ChatGPT search, regardless of OAI-SearchBot permissions. Bing indexation is a prerequisite, not an assumption.

---

## Citability Mechanics

### Factual Density
AI systems prefer to cite content with high ratios of specific, verifiable facts to total word count. Recommendations:
- State the fact before the context (answer-first)
- Use specific numbers over vague qualifiers ("87% of" not "most")
- Tables outperform prose for multi-attribute facts — tables chunk as single units and retrieve whole

### Retrieval Rate: Tables vs Prose
Research on RAG retrieval patterns indicates tables retrieve at higher rates than equivalent prose for multi-attribute comparisons (`T4` directional — vendor/practitioner analysis, not a controlled study; treat as a working hypothesis, not a measured constant). A table comparing five competitors on six dimensions retrieves as one chunk and provides complete information. The same information in prose may span three chunks, each retrieved independently and without the comparative context.

### Content Freshness
Some AI platforms (Perplexity, ChatGPT search) weight recency. Others (Claude, when using training data) cannot access content published after training cutoff. Freshness matters most for:
- News, regulatory changes, market conditions
- Pricing, availability, business hours
- Competitive landscape

Evergreen content (frameworks, explanations, how-tos) has longer citation half-life and doesn't require freshness optimization.

### Content Length Benchmarks (T3 — Averi.ai)
- **Pillar topics:** 2,900+ words → 59% more citation likelihood vs. content under 800 words
- **Section length:** 120–180 words → 70% more citations than very short sections
- Publishing weekly or more → 67% higher AI citation rates vs. monthly publishers
- Content over 18 months old shows decreased citation rates

### The 250-Source Threshold
Analysis of AI Overview citation patterns (`T4`, as of early 2026, single vendor study) indicates brands may need presence across roughly 250 unique domains before achieving consistent citation in competitive queries. Directional, not verified across independent datasets — present it to clients as a hypothesis with its source, not a fixed threshold.

### Reddit Citation Share
In Google AI Overview citations, multiple `T4` analyses (as of early 2026) estimate Reddit content at roughly 21–40% of cited sources depending on query type. The range is wide and source-dependent — cite it as a directional signal with its date, and re-check current data before acting. This is a structural advantage for consumer-facing brands: authentic Reddit presence (reviews, mentions, community discussions) contributes to AI citation at higher rates than most brand-owned content.

---

## Monitoring & Measurement

### Manual Audit Protocol
- Define 50–100 brand-relevant queries covering branded + category terms
- Run 20 target queries × 3 platforms monthly (~45 min total)
- Track for minimum 3 months before drawing conclusions — citation patterns lag optimization changes
- Track citations (URL explicitly referenced) separately from brand mentions
- Establish SoM baseline before any optimization begins — without baseline, attribution is impossible

### Monitoring Tools
| Tool | Tier | Use case |
|---|---|---|
| Profound | Enterprise | Answer-engine optimization; $20M Series A |
| Otterly | SMB | Citation tracking |
| SE Ranking | General | Citation + visibility |
| AiCarma | Monitoring | Brand citation tracking across models |
| FalconRank.ai | Monitoring | AI ranking visibility |
| Trackerly.ai | Monitoring | AI citation tracking |
| BrandWell AI Visibility Score | Analysis | Citation monitoring |

### Share of Model (SoM) — The Core Metric
- SoM = percentage of AI responses in a query category that cite your brand
- Measure separately per platform — SoM is not transferable across platforms
- Competitor SoM trends matter as much as absolute own SoM — a rising competitor signals a content gap
- SoM is the GEO analog to share of voice in traditional marketing

### Market Context (for client brief calibration)
- GEO market: $848M (2025) → $33.7B (2034) at 50.5% CAGR (T3 — Averi.ai, citing Grand View Research)
- Brand mentions correlate 0.664 with AI citations vs. 0.218 for backlinks (Ahrefs research — T3)
- Gartner: 25% search volume drop on traditional engines by 2026 (T3 — directional)
- ChatGPT: 883M monthly users; 77% of AI-driven web visits (T3 — Averi.ai)
- 59% of searches end without clicks across all search types ("zero-click") (T3)

All market figures: T3 sources, vendor-reported or cited from aggregators. Use for client context-setting, not as verified facts. Tag all as `unconfirmed` when included in research output.
