# AGENTS.md — AEO/GEO Researcher

> First file any AI reads when working on this project. Contains architecture, commands, rules, and pointers to the full agent workflow infrastructure.

## Project Overview

AEO/GEO Researcher is a folder-based AI research system for the AEO, GEO, SOM, RAG, and Agentic Marketing space — the practice of getting content found, retrieved, and cited by AI answer systems and AI agents.

Two packages, one system:
- **Claude Projects** → use `claude-projects/`. Paste `INSTRUCTIONS.md` into Project Instructions; upload everything else to the Knowledge Base.
- **Claude Code** → use this folder. Open with `claude` from the project root.

The Orchestrator runs a 3-question intake, routes to the right specialist, and every session ends with a research brief.

## Architecture

Six-specialist system. The Orchestrator owns intake and routing. Five domain specialists own research. All specialists share a reference library. The Research Brief Export system (generate_report.py + renderer.html) converts session output into a client-deliverable audit report. The MkDocs site (references/docs/) is the public-facing product documentation.

`claude-projects/` is a self-contained package optimized for the Claude Projects environment — Orchestrator in `INSTRUCTIONS.md` (Project Instructions layer), specialists and references in the Knowledge Base. Content is identical to the main package; the difference is delivery architecture. Changes to specialist `rules.md` or `examples.md` files must be reflected in both packages.

### Specialist Map

| # | Folder | Responsibility | Receives routing from |
|---|---|---|---|
| 0 | `Specialists/0-orchestrator/` | 3-question intake, routing decision, packet construction | User (always first) |
| 1 | `Specialists/1-signal-technical/` | RAG mechanics, llms.txt, schema, crawl signals | Orchestrator |
| 2 | `Specialists/2-competitive-intelligence/` | Who's winning AI citations and what signals they have | Orchestrator |
| 3 | `Specialists/3-platform-intelligence/` | Per-platform behavior: ChatGPT, Perplexity, Claude, Gemini | Orchestrator |
| 4 | `Specialists/4-content-gap/` | Missing content that AI agents can't answer | Orchestrator |
| 5 | `Specialists/5-agentic-discovery/` | MCP, agent pipelines, agentic marketing | Orchestrator |

### Reference Library

`references/specialist-info/` — shared knowledge base all specialists draw from. Read `references/specialist-info/INDEX.md` first to find the right doc for your task.

| File | Contents | Primary users |
|---|---|---|
| `references/specialist-info/INDEX.md` | Full reference library index — one-line description and specialist mapping for every doc | All — read first |
| `references/manifest.yaml` | Shared packet schema for context handoff between specialists | Orchestrator |
| `references/specialist-info/glossary.md` | AEO/GEO/SOM/RAG/MCP terms | All |
| `references/specialist-info/source-credibility.md` | T1–T5 credibility tiers, verification status flags, tool-fidelity rule | All |
| `references/specialist-info/aeo-geo-signals.md` | RAG pipeline, chunking, llms.txt, schema types, crawl signals, content length benchmarks, monitoring tools, SoM measurement | 1-signal-technical, 4-content-gap |
| `references/specialist-info/aeo-audit-checklist.md` | 5-category structured audit: crawlability → schema → content → authority → monitoring | 1-signal-technical, 4-content-gap |
| `references/specialist-info/geo-content-framework.md` | GEO content framework (Answer Capsule, Factual Density, Extractable Blocks, FAQ Architecture), citation readiness scorecard, GEO-Bench research (T1) | 4-content-gap, 2-competitive-intelligence, 3-platform-intelligence |
| `references/specialist-info/platform-behaviors.md` | Per-platform citation mechanics with quantified thresholds; Google AI Mode; off-site authority building | 3-platform-intelligence, 2-competitive-intelligence |
| `references/specialist-info/rag-taxonomy.md` | 16 RAG types, decision framework, hybrid search, evaluation metrics, frameworks/tools ecosystem | 5-agentic-discovery, 1-signal-technical |
| `references/specialist-info/agentic-patterns.md` | MCP servers, agent pipelines, agentic vs single-query retrieval, agent-native content design | 5-agentic-discovery |
| `references/specialist-info/diagnostic-patterns.md` | Reframe library — Part A framing forks (Orchestrator) + Part B per-specialist investigation pivot chains | Orchestrator + all specialists |
| `references/report-template.html` | Claude Projects HTML export template | Orchestrator (final output) |

### Research Procedures

`references/procedures/` — three-step session workflow. Use for comprehensive sessions or when findings need adversarial review before acting.

| File | Purpose |
|---|---|
| `references/procedures/01-scan.md` | Rapid surface sweep across all signal dimensions — identifies the highest-priority angle before deep investigation |
| `references/procedures/02-investigate.md` | Deep specialist work on a specific angle — the core research step |
| `references/procedures/03-source-audit.md` | Adversarial review of findings — challenges citation traceability, confirmation status accuracy, T4/T5 reliance, and platform behavior staleness |

Procedures are optional — a simple scoped session goes straight to the relevant specialist. Run the full pipeline for comprehensive sessions or when findings will be acted on directly.

### Research Brief Export

| File | Purpose |
|---|---|
| `references/scripts/generate_report.py` | Agent-callable script — reads brief.yaml, injects into renderer.html, opens browser |
| `references/scripts/renderer.html` | Pre-built HTML template — data injected by script, no fetch calls |
| `references/scripts/brief.yaml` | AI-generated session data — created fresh each session |
| `references/scripts/report.html` | Generated output — recreated by script each session |

### Documentation Site

`references/docs/` — MkDocs Material site, deployed to GitHub Pages via `mkdocs gh-deploy`.

## Commands

| Task | Command |
|---|---|
| Serve docs locally | `mkdocs serve` |
| Build docs site | `mkdocs build` |
| Deploy to GitHub Pages | `mkdocs gh-deploy` |
| Generate research brief | `python references/scripts/generate_report.py` |
| Install MkDocs + theme | `pip install mkdocs-material` |

## Always / Never Rules

- Always run `mkdocs build` before `mkdocs gh-deploy` to catch broken links BECAUSE the deploy pushes directly to `gh-pages` with no rollback prompt.
- Always write `references/scripts/brief.yaml` before running `references/scripts/generate_report.py` BECAUSE the script exits with an error if brief.yaml is missing — it does not create a placeholder.
- Always preserve the `references/manifest.yaml` packet schema when modifying specialist identity files BECAUSE all specialists read from this shared schema — a schema change requires updating every specialist that references the changed field.
- Never modify `references/manifest.yaml` without updating `AGENTS.md` and the relevant specialist `identity.md` files BECAUSE the packet schema is the contract between orchestrator and specialists.
- Never add new files to `references/docs/` that are not part of the MkDocs site BECAUSE MkDocs includes everything under `references/docs/` in the build. Internal planning files go in `_dev/`.

## Workflow

This project uses a three-phase AI workflow: Design → Plan → Implement.
Full details: `_dev/agents/README.md`

## Boundaries

**Do not modify without explicit instruction:**
- `references/manifest.yaml` — packet schema contract
- `references/specialist-info/source-credibility.md` — T1–T5 tiers and tool-fidelity rule; all specialists depend on this
- Any specialist `identity.md` — defines specialist scope and routing behavior
- `references/scripts/renderer.html` — visual design for report output

**Safe to modify for scoped tasks:**
- Any specialist `examples.md` — add or update example sessions
- Any specialist `rules.md` — update research rules
- Any file in `references/docs/` — documentation content
- `mkdocs.yml` — site configuration

## Agent Orientation

| Need | Location |
|---|---|
| This file | `AGENTS.md` (you are here) |
| Agent infrastructure overview | `_dev/agents/README.md` |
| Task-type reading lists | `_dev/agents/context-packs.md` |
| Boundary change checklists | `_dev/agents/boundary-checklists.md` |
| Task handoff template | `_dev/agents/task-brief-template.md` |
| Workflow rubric | `_dev/agents/workflow-rubric.md` |
| Change-type gate matrix | `_dev/agents/change-type-matrix.md` |
| Instruction ownership map | `_dev/agents/instruction-map.md` |
| Known pitfalls | `_dev/gotchas/INDEX.md` |
| Architecture decisions | `_dev/adr/INDEX.md` |
| Completed examples | `_dev/agents/done-examples/` |
