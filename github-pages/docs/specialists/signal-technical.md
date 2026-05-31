# Signal & Technical

**Research domain:** RAG mechanics, llms.txt, schema markup, crawl signals, and the technical foundations that determine whether content gets retrieved by AI systems.

## When the Orchestrator Routes Here

- Technical foundations are unknown or suspected broken
- Content isn't appearing in AI answers and the reason is unclear
- Before content strategy work — a site with blocked crawlers or zero schema is not ready for content gap analysis

## What This Specialist Researches

| Area | What it covers |
|---|---|
| Crawl permissions | robots.txt — which AI crawlers are allowed |
| Bing indexation | ChatGPT's retrieval pipeline is Bing-powered |
| llms.txt | Perplexity citation prioritization signal |
| Schema markup | Structured data that makes facts machine-readable |
| Chunking quality | How well content breaks into retrievable segments |
| Factual density | Specific, verifiable claims per page |

## How It Verifies Claims

- Schema claims: validated at `validator.schema.org`, never assumed from page inspection
- Crawler access: `robots.txt` read directly, never assumed from CMS defaults
- Bing indexation: live `site:` search, never inferred from Google status
- llms.txt: checked via direct URL, never assumed absent without checking

Uncertainty flags are mandatory when a finding is inferred rather than directly observed.

## Session Output Format

Findings are presented as a table with columns: Signal · Status · Priority. Followed by a root cause statement, recommended sequence, and explicit statement of what cannot be determined without additional access.

See `1-signal-technical/examples.md` for a complete session example.
