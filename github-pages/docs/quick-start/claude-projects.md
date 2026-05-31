# Quick Start — Claude Projects

## What You Need

- A Claude account (claude.ai)
- The `claude-projects/` folder from this repo

## Setup (one time)

**1. Create a new Claude project**

Go to [claude.ai](https://claude.ai) → Projects → New project. Name it "AEO/GEO Researcher" or anything you like.

**2. Set Project Instructions**

Open project settings → Project Instructions. Paste the full contents of `claude-projects/INSTRUCTIONS.md` into this field.

This loads the Orchestrator at the highest-priority context layer — it routes every session before any specialist content is in play.

**3. Upload the Knowledge Base**

In project settings → Knowledge Base, upload everything in `claude-projects/` **except** `INSTRUCTIONS.md` and `README.md`:

- The five specialist folders (`1-signal-technical/` through `5-agentic-discovery/`)
- The `references/` folder

**4. That's it.** The project is ready.

> **Why two steps instead of one upload?** Project Instructions loads at highest priority, separately from the Knowledge Base. Putting the Orchestrator there means the routing layer is always active and weighted correctly — the specialists and reference library respond to it rather than competing with it.

---

## Running a Session

**Start a chat in your project.** Describe your situation in plain English.

Examples:
- "I run a B2B SaaS product. We're not appearing when people ask AI tools to recommend HR software."
- "I want to understand who's winning AI citations in the enterprise cybersecurity space."
- "My content team wants to know what topics AI agents can't answer in our space."

The Orchestrator will ask three questions — one at a time. Answer each one before it continues.

---

## Requesting a Research Brief

At the end of a session, say: **"Generate the research brief."**

The AI will output:
1. The brief as formatted markdown — read it directly in conversation
2. On request: "Give me the HTML export" — the AI generates the complete HTML file inline

**To save the HTML export:**
1. Copy the HTML output from the conversation
2. Save as `report.html` (or any name with `.html` extension)
3. Open in your browser
4. File → Print → Save as PDF

---

## Tips

- Sessions build on each other. Start a new chat in the same project to continue research — the knowledge base carries the specialist files forward.
- The Orchestrator routes to one specialist by default. If your question spans multiple domains, say so: "I want signal & technical and competitive intelligence."
- Uncertainty flags are a feature. "Unconfirmed" findings are the ones that become your next research session.
