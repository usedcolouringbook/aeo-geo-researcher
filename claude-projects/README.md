# AEO/GEO Researcher — Claude Projects

A six-specialist AI research system for AEO, GEO, SOM, RAG, and Agentic Marketing — packaged for Claude Projects.

For the full build with scripts, report export, and CLI support: see the parent `aeo-geo-researcher/` folder (Claude Code).

---

## Setup (one time, ~2 minutes)

### 1. Create a new Claude project

Go to [claude.ai](https://claude.ai) → Projects → New project. Name it "AEO/GEO Researcher" or anything you like.

### 2. Set Project Instructions

Open project settings → Project Instructions. Paste the full contents of `INSTRUCTIONS.md` into this field.

This loads the Orchestrator at the highest priority layer — it routes every session before any specialist engages.

### 3. Upload the Knowledge Base

In project settings → Knowledge Base, upload everything in this folder **except** `INSTRUCTIONS.md` and this `README.md`:

- `1-signal-technical/` — RAG mechanics, schema, crawl signals, llms.txt
- `2-competitive-intelligence/` — who's winning AI citations and why
- `3-platform-intelligence/` — ChatGPT, Perplexity, Claude, Gemini behavior
- `4-content-gap/` — what AI agents can't answer in your space
- `5-agentic-discovery/` — MCP, agent pipelines, agentic marketing
- `references/` — shared knowledge library all specialists draw from

### 4. That's it.

---

## Running a Session

Start a chat in your project. Describe your situation in plain English.

Examples:
- "I run a B2B SaaS product. We're not appearing when people ask AI tools to recommend HR software."
- "I want to understand who's winning AI citations in the enterprise cybersecurity space."
- "My content team wants to know what topics AI agents can't answer in our space."

The Orchestrator asks three questions — one at a time. Answer each before it continues. After intake, it constructs a research packet and routes to the right specialist.

---

## Requesting a Research Brief

At the end of a session, say: **"Generate the research brief."**

The AI outputs a structured deliverable:

**Executive Summary → Signal Legend → Findings by Domain → Priority Matrix → Gap Map → Next Research Move**

To export as a formatted document:
1. Say: "Give me the HTML export"
2. Copy the HTML output from the conversation
3. Save as `report.html`, open in browser, File → Print → Save as PDF

---

## Specialists

| # | Specialist | Research domain |
|---|---|---|
| 0 | Orchestrator | Intake + routing (Project Instructions) |
| 1 | Signal & Technical | RAG mechanics, llms.txt, schema, crawl signals |
| 2 | Competitive Intelligence | Who's winning AI citations and why |
| 3 | Platform Intelligence | ChatGPT, Perplexity, Claude, Gemini behavior |
| 4 | Content Gap | What content AI agents can't answer |
| 5 | Agentic Discovery | MCP, agent pipelines, agentic marketing |

---

## How It Works

The Orchestrator lives in Project Instructions — the always-loaded, priority-weighted context layer. The specialists and reference library live in the Knowledge Base. This split means every session starts with the routing layer fully active before any specialist content is in play.

Every finding is tagged on two axes — verification (`confirmed / unconfirmed / emerging`) and source credibility (`T1`–`T5`) — so a finding's certainty and the trustworthiness of its source are always visible. When confidence in a finding's implication is Moderate or Low, a consequence statement is appended: what changes if the alternative interpretation is correct.

Sessions run a three-step pipeline: a **Signal Scan** identifies the highest-priority angle, a **Deep Investigation** by the right specialist produces findings, and a **Source Audit** runs an adversarial challenge on those findings before the client acts. Every session closes with a Research Ledger (confirmed vs. inferred) and a mandatory Next Research Move.

**It researches. It does not summarize.**

---

## Tips

- Sessions build on each other. Start a new chat in the same project to continue research — Project Instructions and the Knowledge Base carry forward automatically.
- The Orchestrator routes to one specialist by default. If your question spans multiple domains, say so: "I want signal & technical and competitive intelligence."
- Uncertainty flags are a feature. `unconfirmed` findings are the ones that become your next research session.
- If quality degrades mid-session, start a new chat. Long conversations accumulate context noise — a fresh chat with the same project settings resets the window cleanly.
