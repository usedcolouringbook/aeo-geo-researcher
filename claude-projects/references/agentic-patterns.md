# Agentic Patterns Reference

How AI agents actively find, consume, and act on content. Distinct from how humans use AI — agents operate autonomously, follow instructions, use tools, and take actions. Agentic marketing means building for agents as the audience.

---

## What Makes an Agent Different

A user asking ChatGPT a question is a single retrieval event. An AI agent working on a task is a pipeline:

1. **Receives a goal** — "research breakfast restaurants near downtown with loyalty programs"
2. **Plans steps** — decompose goal into research subtasks
3. **Uses tools** — web search, URL fetch, API calls, database queries
4. **Synthesizes findings** — combines results across steps
5. **Takes action or reports** — books a reservation, drafts an email, produces a report

**Implication:** Content optimized for single-query retrieval (AEO/GEO) and content designed for agent consumption (agentic marketing) have overlapping but distinct requirements. Agents read more deeply, follow links, and can execute structured data — humans mostly scan.

---

## MCP — Model Context Protocol

**What it is:** Anthropic's open standard for connecting AI models to external tools, APIs, and data sources. An MCP server exposes capabilities that AI agents can call.

**How agents use it:** When Claude (or another MCP-compatible model) has tools enabled, it can query MCP servers directly — bypassing web retrieval. A restaurant with an MCP server could let agents check table availability, retrieve the menu, or look up a customer's order history.

**Types of MCP tools relevant to agentic marketing:**
- **Resource tools:** Let agents read structured data (menus, catalogs, FAQs, hours, pricing)
- **Action tools:** Let agents take actions (book a reservation, add to cart, subscribe to a list)
- **Search tools:** Let agents query the brand's own content/database

**Who's building MCP servers now:** SaaS products (Anthropic, Linear, GitHub, Notion have published MCP servers), e-commerce platforms, enterprise software. Consumer-facing local businesses are early-stage.

**Competitive advantage window:** MCP adoption is early. Brands that expose MCP endpoints now face minimal competition for agent-mediated discovery.

---

## Agent-Native Content Formats

### llms.txt and llms-full.txt
See `references/aeo-geo-signals.md` for technical format. Agentic context: agents that read llms.txt before engaging with a site arrive with correct context about the site's purpose, key pages, and permissions. This reduces misattribution and improves the quality of agent-generated content about the brand.

### Structured Data as Agent API
JSON-LD schema markup functions as a machine-readable API layer on top of human-readable content. Agents that parse raw HTML (not markdown-converted HTML) can extract structured data without NLP guesswork.

**What this means practically:** A LocalBusiness schema block tells an agent the restaurant's hours, address, phone, and cuisine type without requiring the agent to read and interpret prose. It's the difference between `SELECT hours FROM restaurant WHERE id = X` and "read this page and figure out when they're open."

### Answer-First Structure for Agent Chunking
Agents using RAG pipelines retrieve chunks, not full pages. Answer-first structure — stating the key fact in the first sentence of a paragraph — ensures the key fact appears in the chunk that matches the query, not buried in context that may not be retrieved.

---

## How Agents Discover Content

### Discovery Pipeline (Typical Research Agent)
1. Web search (Bing/Google depending on platform)
2. URL fetch and read (often markdown-converted — the audit tool gap applies)
3. Link follow for deep research
4. Structured data extraction if agent parses raw HTML
5. llms.txt check if agent is configured to respect it

### Discovery Pipeline (Action Agent)
1. Tool selection — which MCP servers or APIs are available?
2. Capability query — what can this tool do?
3. Action execution — call the tool with parameters
4. Result synthesis — incorporate result into task

**Implication:** Action agents never touch the web at all if an MCP server provides what they need. Web-visible content strategy is irrelevant if the agent goes direct to an MCP endpoint.

---

## Agentic Marketing Strategies

### Tier 1: Be Findable by Agents (defensive)
- llms.txt with accurate site description
- Schema markup accessible to raw HTML parsers
- Crawl permissions for AI bots
- Answer-first content structure
- High factual density

### Tier 2: Be Readable by Agents (intermediate)
- llms-full.txt for sites with content spread across many pages
- Clear heading hierarchy for clean chunking
- Tables over prose for multi-attribute content
- Consistent entity naming (same name, same format, every page)

### Tier 3: Be Actionable by Agents (advanced)
- MCP server with resource and action tools
- Structured APIs for agent consumption
- Agent-specific documentation (what can an agent do here?)
- Webhooks or callbacks for async agent workflows

---

## Emerging Signals (Treat as Unconfirmed)

The following patterns have early evidence but are not yet confirmed at scale:

- **Agent-specific sitemaps:** Some platforms are beginning to recognize `agent-sitemap.xml` files that list agent-relevant pages separately from human-relevant pages. Unconfirmed adoption.
- **Speakable schema for agents:** Originally designed for voice assistants, Speakable markup may begin to signal "this content is designed for machine consumption" to agent crawlers. Unconfirmed.
- **Agent personas in llms.txt:** Some implementations include sections describing how different agent types should interact with the site. No confirmed platform support yet.

Always flag these as `emerging` when citing in research outputs.
