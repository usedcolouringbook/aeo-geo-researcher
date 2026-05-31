# Procedure 01 — Signal Scan

**Purpose:** Rapid surface sweep before deep investigation. Map what's present and absent across all signal dimensions without going deep on any one of them. Identify the highest-priority angle, then hand off to the right specialist in Procedure 02.

Use the scan when: the client's AI visibility landscape is unknown, the question is broad ("why aren't we showing up?"), or this is the first session with a client and no prior trail exists.

Skip the scan when: the client has a specific, well-scoped question and the orchestrator has already identified the right specialist. Go directly to Procedure 02.

---

## What the Scan Covers

Run through all six dimensions quickly. Spend no more than 2–3 observations per dimension. The goal is to flag, not to investigate.

### 1. Crawl Access
- Are AI crawlers allowed in robots.txt? (OAI-SearchBot, PerplexityBot, ClaudeBot, Google-Extended)
- Is the site indexed in Bing? (ChatGPT dependency)
- Does `/llms.txt` exist at root?

### 2. Schema Presence
- Is any structured data present? (check raw source, not markdown fetch — see tool-fidelity rule)
- Is FAQPage or Organization schema present?

### 3. Platform Visibility
- Run 2–3 of the client's most direct target queries on ChatGPT and Perplexity
- Does the client appear? Do competitors appear?

### 4. Content Structure
- Is there answer-first structure in the top pages?
- Are key facts at the top or buried in prose?

### 5. Off-Site Presence
- Is the brand mentioned in Reddit discussions for the relevant topic?
- Does a LinkedIn or review platform presence exist?

### 6. Competitive Landscape
- Who is appearing for the client's target queries?
- Any obvious competitors the client didn't mention?

---

## Scan Output Format

Keep the scan output tight — this is a triage document, not a research brief.

```
## Signal Scan — [Client Name / Type]

**Crawl access:** [OPEN / BLOCKED / PARTIAL — one sentence]
**Schema:** [PRESENT / ABSENT / UNVERIFIED — one sentence]
**Platform visibility:** [VISIBLE / NOT VISIBLE / PARTIAL — one sentence per platform checked]
**Content structure:** [ANSWER-FIRST / BURIED / UNKNOWN — one sentence]
**Off-site presence:** [PRESENT / ABSENT / WEAK — one sentence]
**Competitive landscape:** [who's appearing — list]

**Highest-priority angle:** [one sentence — the dimension most likely to explain the gap]
**Recommended next step:** Proceed to Procedure 02 → [specialist name]
```

Every observation in the scan is `unconfirmed` unless directly verified. The scan is a hypothesis map — Procedure 02 confirms or clears each hypothesis.

---

## Scan Limitations

State these explicitly in the scan output if they apply:
- "Schema assessment is unconfirmed — requires raw source or Rich Results Test to confirm"
- "Platform visibility based on [N] test queries only — may not represent the full query landscape"
- "Off-site presence based on surface check — full competitive off-site analysis requires Procedure 02 → 2-competitive-intelligence"
