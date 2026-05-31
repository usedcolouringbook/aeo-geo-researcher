# Glossary — AEO/GEO/SOM/RAG/Agentic Marketing

Plain-language definitions for the research domain. Specialists use this vocabulary consistently. When a client uses a term differently, note the discrepancy rather than silently adopting the client's usage.

---

## Core Terms

**AEO — Answer Engine Optimization**
The practice of structuring content so that AI answer systems (ChatGPT, Perplexity, Google AI Overviews, Claude) retrieve and cite it when answering user queries. Distinct from SEO: AEO optimizes for machine extraction and citation, not human click-through.

**GEO — Generative Engine Optimization**
Broader term encompassing AEO. Where AEO focuses on answer extraction, GEO covers the full set of practices that improve a brand's presence across generative AI outputs — citations, recommendations, summaries, and agent actions.

**SOM — Share of Model**
The proportion of relevant AI responses that cite, mention, or recommend a specific brand, product, or entity. Analogous to share of voice in traditional marketing. Measured by sampling AI responses to a target query set and counting brand appearances.

**RAG — Retrieval Augmented Generation**
The architecture most AI answer systems use: when a query arrives, the system retrieves relevant content from an index (via vector similarity search), then generates a response grounded in that retrieved content. Understanding RAG mechanics is prerequisite to any GEO strategy — if content isn't retrieved, it cannot be cited.

**Vector Similarity**
How RAG systems find relevant content. Content is converted into numerical embeddings; when a query arrives, its embedding is compared to stored content embeddings. Closest matches are retrieved. Implications: content that uses the same language as likely queries retrieves better than content that paraphrases.

**Chunking**
How RAG systems break content into retrievable pieces. Most systems chunk by paragraph, heading section, or token count. A 5,000-word page may produce 20+ chunks — only the relevant chunks are retrieved per query. Implication: key facts buried in long prose may never be retrieved if their chunk doesn't match the query.

**llms.txt**
A plain-text file at `yourdomain.com/llms.txt` designed for AI agent consumption. Contains structured information about the site — what it is, who it serves, key pages, and what agents are permitted to use. The agent-native equivalent of `robots.txt`. Not yet universally adopted by AI platforms but increasingly recognized.

**llms-full.txt**
Extended version of `llms.txt` — contains the full site content in a flat, agent-readable format rather than linking to pages. Allows agents to read the entire site without crawling individual URLs.

**AI Overview**
Google's AI-generated response that appears above organic search results (formerly Search Generative Experience / SGE). Powered by a combination of Google's index and Gemini. Appearing in AI Overviews is a primary GEO target for content strategies targeting Google.

**Citation**
When an AI system includes a reference to a specific source in its response — either inline attribution or a source link. Citation is the primary measurable output of AEO/GEO work.

**Entity**
A recognized, named subject in AI knowledge graphs — a business, person, product, concept, or place that AI systems have learned to identify and distinguish from similar entities. Strong entity recognition (the AI knows who you are) is prerequisite to consistent citation.

**JSON-LD**
The structured data format preferred for schema markup. Placed in a `<script type="application/ld+json">` block in the page `<head>`. AI crawlers that parse raw HTML can read it; AI tools that convert pages to markdown cannot (the script tags are stripped). This is the audit tool gap.

**Schema Markup**
Structured data vocabulary (schema.org) embedded in page HTML that explicitly labels content for machines. Types relevant to AEO: Organization, LocalBusiness, FAQPage, HowTo, Product, Review, Article, Speakable. Correct schema type selection matters — FAQPage markup on content that isn't actually FAQ format produces no signal lift.

**MCP — Model Context Protocol**
Anthropic's open standard for connecting AI models to external tools, data sources, and services. Relevant to agentic marketing: brands that expose MCP servers allow AI agents to take actions (book a table, check inventory, retrieve personalized data) rather than just retrieve information.

**Agentic Marketing**
Marketing designed for AI agents as the audience rather than (or in addition to) humans. Includes: llms.txt/llms-full.txt for agent readability, MCP servers for agent actions, structured data for agent extraction, and content framing optimized for how agents synthesize rather than how humans read.

**Organic GEO vs Paid AI Placement**
As of 2026, major AI platforms are integrating paid advertising alongside organic citations. Organic GEO = winning citations through content quality, entity authority, and technical signals. Paid AI placement = appearing in AI responses through advertising spend. These are distinct channels with different strategies. When a competitor appears in AI answers despite weak signals, paid placement is a plausible explanation.

**OAI-SearchBot vs GPTBot**
Two distinct OpenAI crawlers with different purposes. OAI-SearchBot powers ChatGPT's real-time web search (Bing-indexed content). GPTBot trains OpenAI models (future training data). Blocking GPTBot does not prevent ChatGPT search from finding your content — blocking OAI-SearchBot does.

**Perplexity Bot**
Perplexity's crawler. Aggressive crawl frequency relative to other AI crawlers. Content indexed by PerplexityBot is available for real-time citation in Perplexity responses. Blocking it removes content from Perplexity's citation pool.

**Factual Density**
The ratio of specific, verifiable facts to total content volume. High factual density = more citeable content per chunk. AI systems prefer dense, specific content for citation over prose that describes rather than states.
