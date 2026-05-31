# References — Index

Shared knowledge library. All specialists draw from this. Read the docs relevant to your investigation — do not restate them verbatim, apply their content to the client's specific context.

**Session workflow:** Three-step pipeline — Signal Scan (surface sweep) → Deep Investigation (specialist deep dive) → Source Audit (adversarial review before acting). The Orchestrator in Project Instructions governs when to use each step.

| File | What it contains | Primary users |
|---|---|---|
| `aeo-geo-signals.md` | RAG pipeline mechanics, chunking types, llms.txt/llms-full.txt spec, schema markup types, crawl signal taxonomy, citability mechanics, content length benchmarks, monitoring tools, SoM measurement, market benchmarks | 1-signal-technical, 4-content-gap |
| `aeo-audit-checklist.md` | 5-category structured audit protocol: crawlability, schema, content structure, off-site authority, monitoring — with triage order | 1-signal-technical, 4-content-gap |
| `geo-content-framework.md` | GEO content framework (Answer Capsule, Factual Density, Extractable Blocks, FAQ Architecture), content length benchmarks, citation readiness scorecard, platform-specific content thresholds, budget allocation, ROI benchmarks, GEO-Bench academic research (T1) | 4-content-gap, 2-competitive-intelligence, 3-platform-intelligence |
| `platform-behaviors.md` | Per-platform citation mechanics: ChatGPT, Perplexity, Google AI Overviews, Google AI Mode, Claude, Microsoft Copilot — quantified thresholds, what works, what doesn't. Off-site authority building (Reddit, YouTube, LinkedIn, reviews, directories) | 3-platform-intelligence, 2-competitive-intelligence |
| `rag-taxonomy.md` | 16 RAG types with decision framework, chunking and retrieval mechanics, hybrid search, HyDE, contextual retrieval, RAG evaluation metrics, frameworks/engines/tools ecosystem | 5-agentic-discovery, 1-signal-technical |
| `agentic-patterns.md` | MCP architecture, agent pipeline mechanics, agentic vs single-query retrieval, agent-native content design | 5-agentic-discovery |
| `source-credibility.md` | T1–T5 credibility tiers, weighting rules, verification status flags, citation fabrication rule, research ledger format, tool-fidelity rule (JSON-LD strip gap) | All specialists |
| `diagnostic-patterns.md` | Reframe library — Part A framing forks (Orchestrator sharpens the client's question) and Part B per-specialist investigation pivot chains | Orchestrator (Part A); all specialists (Part B) |
| `glossary.md` | Domain terminology definitions | All specialists |
| `manifest.yaml` | Packet schema — field definitions for all inter-specialist handoff packets | Orchestrator |
| `report-template.html` | Claude Projects HTML export template — AI populates `{{VARIABLE}}` fields with session data on user request | AI during Claude Projects sessions |
