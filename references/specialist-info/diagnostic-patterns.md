# Diagnostic Patterns — The Reframe Library

This is the system's accumulated pattern knowledge: the questions a domain expert asks that a newcomer doesn't know to ask. It exists so the researcher can **sharpen a client's question before investigating it** — not silently reinterpret it, but surface the better question out loud and let the client confirm.

A question is **"better"** only if the client could not have asked it without domain knowledge they don't have. "What are you trying to solve?" fails that test — anyone asks it. "Do you mean *cited in an answer* or *recommended as a vendor* — those are different retrieval pipelines with different fixes?" passes it.

Two consumers use this file:
- **The Orchestrator** matches the client's stated angle against **Part A — Framing Forks** and offers the matching fork as its single reframe question before routing.
- **Each specialist** uses its slice of **Part B — Investigation Forks** as the first pivot of its investigation, so the audit branches on what it finds instead of running a fixed list.

**The one rule:** never invent a reframe. If the client's framing does not match a pattern here, route the stated angle directly — a forced or generic reframe is worse than none. The patterns cover the common cases; a genuinely novel angle is investigated as stated.

---

## Part A — Framing Forks (Orchestrator)

Each fork: the naive framing a client arrives with, the sharper question it hides, the distinct problems it conflates, and where each branch routes.

### F1 — "Why aren't we in ChatGPT / AI answers?"
**Fork:** Cited *in the answer text*, recommended *as a vendor/option*, or not appearing *at all*?
- **Cited-in-answer** failing → retrieval/legibility problem → **1-signal-technical**
- **Recommended-as-vendor** failing → authority + competitive standing → **2-competitive-intelligence**
- **Not-appearing-at-all** → access/indexation gate → **1-signal-technical** first
**Why it matters:** these run through different pipelines; "be cited" and "be recommended" are not the same fix, and most clients conflate them.

### F2 — "We're invisible in AI search"
**Fork:** Is this **access** (bots blocked or the site isn't indexed), **authority** (you're reached and read but not trusted enough to cite), or **presence** (the platform doesn't trigger AI features for this query type at all)?
- **Access** → **1-signal-technical**
- **Authority** → **2-competitive-intelligence**
- **Presence** → **3-platform-intelligence**
**Why it matters:** "invisible" has three causes with opposite fixes — unblocking a crawler does nothing if the real gap is authority.

### F3 — "What content should we create for AI?"
**Fork:** Is this a **content gap** (the answer doesn't exist) or a **retrieval gap** (the answer exists but AI can't retrieve it)? Have technical signals been diagnosed?
- Technical status unknown/broken → **1-signal-technical** first; content built on an illegible site compounds nothing
- Technical confirmed clean → **4-content-gap**
**Why it matters:** creating content is the most expensive move; doing it before diagnosing retrieval is second-step-first.

### F4 — "Competitor X is winning in AI"
**Fork:** Have you **verified** X is actually cited, or **assumed** it? On which platform, for which queries?
- Verify the premise first (live query) → then **2-competitive-intelligence**
- If X is *not* actually cited where assumed, the real question changes — re-run intake on the actual gap
**Why it matters:** competitive strategy built on an unverified premise wastes the whole session; premise-check is the cheapest high-value move.

### F5 — "We added schema but nothing changed"
**Fork:** Is the schema **present**, **valid**, **retrievable** (can the AI's crawler actually read it — JSON-LD in `<script>` is invisible to markdown fetchers), and **relevant** to the query being asked?
- All four are distinct failure points → **1-signal-technical**
**Why it matters:** "added schema" can fail at four different stages; "nothing changed" doesn't tell you which.

### F6 — "AI Overviews are killing our traffic"
**Fork:** Are you measuring **traffic** or **citation**? Being cited but getting fewer clicks is a *correct* outcome of AI answers; being uncited *and* losing clicks is a different problem.
- Cited-but-fewer-clicks → reframe success metric → **3-platform-intelligence** (how the platform surfaces you)
- Uncited-and-losing-clicks → **1-signal-technical** / **2-competitive-intelligence**
**Why it matters:** the client's metric may be wrong; the better question is what *should* be measured in an AI-answer world.

### F7 — "How do we optimize for AI / get AI to use us?"
**Fork:** Do you want to be **discovered** (found and cited when agents research your space) or **acted on** (agents transact on your behalf — book, order, look up — via MCP/agent endpoints)?
- **Discovery** → **1-signal-technical** / **4-content-gap**
- **Action** → **5-agentic-discovery** (but discovery foundations gate action — confirm Track A before investing in Track B)
**Why it matters:** "optimize for AI" spans two different games with different infrastructure.

### F8 — "How do AI agents find local businesses like ours?"
**Fork:** Which is the live concern — being **discovered** by AI agents (agentic), or how a **specific platform's local pipeline** (Google AI Overviews + Maps vs Perplexity) surfaces you?
- Routes to **5-agentic-discovery + 3-platform-intelligence** (local AI behavior is platform-specific)
**Why it matters:** local AI discovery is split across an agentic layer and platform-specific local packs; treating it as one question misses half.

---

## Part B — Investigation Forks (Specialists)

Each specialist opens its investigation at a **pivot fact** whose value determines the next question. Investigate the pivot first; do not run downstream steps until the pivot is established.

### 1 — Signal & Technical: Access → Indexation → Legibility
1. **Pivot: Access.** Can the target pipeline's bot reach the site (robots.txt + crawler directives for the right bot — OAI-SearchBot vs GPTBot vs PerplexityBot vs Google-Extended)?
   - **Blocked** → this is the root cause. Surface it immediately; downstream legibility work is moot until it's fixed. Ask whether to stop and fix or keep mapping.
   - **Allowed** → go to pivot 2.
2. **Pivot: Indexation.** Is the site in the index that feeds the target platform (Bing for ChatGPT; Google for AI Overviews)?
   - **Not indexed** → indexation is the gate; schema/chunking are premature (note them, don't lead with them).
   - **Indexed** → go to pivot 3.
3. **Pivot: Legibility.** *Now* schema (present/valid/retrievable/relevant — see F5), chunking, and factual density are the live questions. Investigate these only once access and indexation are confirmed.

### 2 — Competitive Intelligence: Premise → Organic/Paid → Signal delta
1. **Pivot: Premise.** Is each named competitor *actually* cited where the client assumes (live query), or assumed? Verify before analyzing.
   - **Not cited** → the premise is wrong; surface it and re-scope — don't analyze signals for a competitor who isn't winning.
   - **Cited** → go to pivot 2.
2. **Pivot: Organic or paid?** A weak-signal competitor appearing prominently may be buying placement; matching their organic signals won't replicate paid visibility.
3. **Signal delta.** For genuinely-cited organic competitors: what do they have (schema, llms.txt, content structure, entity authority, referring-domain count) that the client lacks?

### 3 — Platform Intelligence: Surface → Platform → Mechanics
1. **Pivot: Surface.** Is the failure about being **cited in the answer**, **recommended as an option**, or **not appearing**? (Mirror of F1, at platform depth.)
2. **Pivot: Platform.** Which platform's pipeline is in scope? Never generalize — ChatGPT (Bing-fed), Perplexity (own crawl + llms.txt), Google AI Overviews (Google index + local pack), Claude (tools/MCP) behave differently.
3. **Mechanics.** Investigate that platform's citation mechanics for this query type, with a date stamp (platform behavior is the most time-sensitive signal).

### 4 — Content Gap: Retrieval-gate → Coverage/Extractability → Format
1. **Pivot: Retrieval gate.** Has 1-signal-technical confirmed the site is technically legible? If not, the "content gap" may be a retrieval gap — flag and recommend signal diagnosis first (or proceed with every recommendation marked contingent).
2. **Pivot: Coverage or extractability?** Is the answer **absent** (no content covers the query) or **present but unextractable** (content exists but is dense prose, no schema, wrong format)? These have different fixes — write vs restructure.
3. **Format match.** Map each gap to the format AI is actually using to answer it (observed live, not assumed).

### 5 — Agentic Discovery: Discovery/Action → Discovery-gates-action
1. **Pivot: Discovery or Action?** (Mirror of F7.) Track A — can agents *find* the client? Track B — can agents *act* for the client's customers (MCP)?
2. **Gate: discovery before action.** Don't assess MCP/action investment until Track A (discovery) gaps are understood — an agent that can act but can't be found delivers nothing. If the client wants Action, confirm Discovery status first or flag the dependency.
