# Platform Intelligence

**Research domain:** How specific AI platforms (ChatGPT, Perplexity, Claude, Gemini, Copilot) behave for a given content type, query type, or industry.

## When the Orchestrator Routes Here

- Platform-specific behavior matters to the client's strategy
- The client wants to optimize for one platform over others
- The client is seeing different citation behavior across platforms and doesn't know why

## What This Specialist Researches

| Platform | Key behavioral differences |
|---|---|
| ChatGPT | Bing-powered retrieval; OAI-SearchBot crawl required; only cites 15% of retrieved pages; llms.txt not yet a confirmed factor |
| Perplexity | Proprietary crawler; llms.txt highest adoption of any platform; ~50% of citations from content under 3 months old; cites sources inline with numbered footnotes |
| Google AI Overviews | Search-index-based; highest schema impact of any platform; 59.6% of citations from outside top-20 organic results; Reddit is 21–40% of cited sources |
| Google AI Mode | Distinct from AI Overviews; top citation predictor is domain traffic (SHAP 0.63); 60%+ domain disappearance and 80%+ URL disappearance between identical queries |
| Claude (claude.ai) | Training data by default; higher credibility bar; MCP servers create direct access points bypassing retrieval; llms.txt checked when web access is enabled |
| Copilot | Bing-powered; integrated into Microsoft 365 enterprise context |

Full behavioral detail, quantified thresholds, and off-site authority signals: `references/platform-behaviors.md`.

## Research Approach

Tests the client's specific query types on each platform directly. Documents which sources appear, what format they're in, and what signals the cited sources share. Flags platform-specific constraints (e.g., Bing dependency for ChatGPT).
