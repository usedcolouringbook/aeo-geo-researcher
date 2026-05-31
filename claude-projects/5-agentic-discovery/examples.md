# Agentic Discovery Researcher — Examples

What an investigative session looks like. Not a summary. A research chain.

---

## Example Session: E-Commerce Retailer — Can Agents Find and Act?

**Client brief:** Mid-size outdoor gear retailer. 8,000 SKUs, Shopify-based, ships US-wide. Wants to understand if AI shopping agents can find their products and whether there's a real opportunity in MCP or agent-native tooling.

**Packet received:** Technical foundations are solid — AI crawlers allowed, Bing indexed, basic schema in place. Client wants to explore the agentic layer specifically.

**Pipeline context:** Procedure 01 (Signal Scan) ran first — confirmed technical foundations solid and flagged llms.txt absence and AI shopping query invisibility as the highest-priority agentic signals. Scan routed here (Agentic Discovery) for Track A + Track B investigation. Client requested Procedure 03 (Source Audit) specifically for the MCP findings before making an investment decision.

**Opening question asked:** Are we focused on making sure agents can find the store, or on what agents could actually do for customers once they're there — or both?

**Client answer:** Both, but start with whether they can even find us. Then tell us what's actually possible right now vs what's still theoretical.

---

### Investigation Chain — Track A: Discovery

**Step 1 — llms.txt assessment**

Check `outdoorgearco.com/llms.txt` directly in browser.

Found: 404. No llms.txt present.

Finding: The retailer has not published an agent-native endpoint. AI research agents that use llms.txt as a discovery signal cannot find a structured summary of what this site offers. Product catalog, brand story, and return policy are not machine-readable in agent format.

Check what a well-structured llms.txt looks like for a comparable retailer:

REI.com/llms.txt — found. Contains: brand description, product category index, customer service endpoints, return policy summary, store locator API reference.

Finding: REI has invested in agent-native discoverability. The outdoor gear category has at least one competitor with a live llms.txt. This is no longer a theoretical gap.

Uncertainty flag: llms.txt is confirmed as used by Perplexity for citation prioritization. Its effect on shopping agents specifically (as opposed to research agents) is not yet confirmed in published documentation. Do not overstate the direct shopping conversion impact.

---

**Step 2 — AI crawler access verification**

Read `outdoorgearco.com/robots.txt` directly.

Found:
```
User-agent: GPTBot
Allow: /

User-agent: OAI-SearchBot
Allow: /

User-agent: PerplexityBot
Allow: /
```

Finding: All major AI crawlers have access. Track A foundational requirement met.

---

**Step 3 — Live agent discovery test**

Run shopping-intent queries in ChatGPT and Perplexity. Test whether the retailer appears.

Query: "best hiking boots under $200"

ChatGPT: Cited REI, Backcountry, Amazon. No client mention.

Perplexity: Cited REI buying guide, OutdoorGearLab review, Reddit r/hiking thread. No client mention.

Query: "outdoor gear retailer with free returns"

ChatGPT: Cited REI and Backcountry. No client mention.

Query: "where to buy Merrell trail runners online"

ChatGPT: Cited Merrell official, REI, Amazon, Zappos. No client mention despite the retailer carrying Merrell.

Finding: The retailer is invisible in AI shopping queries despite having AI crawler access and Bing indexation. The gap is not technical access — it's content authority and structured product data. REI appears consistently because it has brand-specific pages, structured product listings, expert buying guides, and domain authority. The client has SKUs, not content.

---

### Investigation Chain — Track B: Action

**Step 4 — What actions do customers want from agents?**

Define the customer actions that a shopping agent could fulfill for this retailer.

Based on the product category (outdoor gear):
- Find products matching specific criteria (weight, waterproofing, size, price)
- Compare two products on spec (e.g., tent A vs tent B)
- Check stock availability for a specific SKU and size
- Get a curated recommendation for a use case ("camping trip in Patagonia in October")
- Process a return or check order status

These are the actions worth assessing for MCP viability.

---

**Step 5 — MCP opportunity assessment**

Assess each action against four criteria: customer demand, data availability, tech stack compatibility, competitive timing.

**Product search by criteria:**
- Customer demand: High — spec-based filtering is a primary shopping behavior
- Data available: Yes — Shopify has product catalog API with metadata
- Tech stack: Shopify has a confirmed MCP server in development (modelcontextprotocol.io registry — searched 2026-05-27, found Shopify listed as partner)
- Competitive timing: REI does not appear to have a public MCP server yet. Early-mover window is open.
- Verdict: High-value Track B opportunity. Confirmed path via Shopify MCP.

**Stock availability check:**
- Customer demand: High — especially for seasonal items and popular sizes
- Data available: Yes — Shopify inventory API is real-time
- Tech stack: Covered by Shopify MCP server
- Verdict: Bundled with product search — low incremental cost.

**Curated recommendation by use case:**
- Customer demand: High — "help me pack for X trip" is a common shopping intent
- Data available: Requires product tagging by use case, climate, season — not currently in the catalog
- Tech stack: Possible but requires data enrichment before MCP exposure
- Verdict: Medium-term opportunity. Requires catalog work before MCP implementation is meaningful.

**Order status / returns:**
- Customer demand: High
- Data available: Yes — Shopify order API
- Tech stack: Covered by Shopify MCP
- Verdict: Viable but lower strategic value than product discovery for citation purposes.

Uncertainty flag: The Shopify MCP server is listed as in development as of 2026-05-27. Its release date and capability scope are not confirmed. Do not recommend the client build on an unreleased tool without flagging this dependency.

---

**Step 6 — Confirmed vs emerging signal audit**

Before delivering findings, sort every signal into confirmed or emerging.

**Confirmed:**
- AI crawlers can access the site (tested directly)
- Bing indexation is in place (verified via site: search)
- llms.txt is missing (tested directly)
- REI has llms.txt (tested directly)
- Shopify is listed in the MCP registry (checked modelcontextprotocol.io 2026-05-27)
- The retailer is invisible in current AI shopping queries (tested live)

**Emerging (documented but not confirmed at scale):**
- Shopify MCP server availability and capability (listed but not released)
- llms.txt impact on shopping agent behavior specifically (confirmed for research agents, not shopping agents)
- Agent-specific sitemaps as a citation signal (mentioned in emerging documentation, no platform confirmation)

---

### Output Format

**Agentic Discovery Assessment — Outdoor Gear Retailer**

**Track A: Can agents find the store?**

| Signal | Status |
|--------|--------|
| AI crawler access | ✅ Confirmed |
| Bing indexation | ✅ Confirmed |
| llms.txt | ❌ Missing |
| AI citation presence | ❌ Not appearing |

Root cause of citation absence: content authority gap, not technical access. REI dominates because of buying guides, expert content, and structured product data — not because of superior crawler access.

**Track B: What can agents do?**

| Action | Feasibility | Status |
|--------|-------------|--------|
| Product search by spec | High | Shopify MCP (emerging — not yet released) |
| Stock availability | High | Bundled with above |
| Use-case recommendation | Medium | Requires catalog enrichment first |
| Order / returns | High | Shopify MCP (emerging) |

**Recommended sequence:**
1. Publish llms.txt — low effort, confirmed signal for Perplexity, best practice for emerging agents
2. Build product buying guides — closes the content authority gap, addresses Track A
3. Monitor Shopify MCP release — act when confirmed available, not before
4. Plan catalog enrichment for use-case tagging — sets up Track B recommendation capability

**What I cannot confirm:** Shopify MCP release date and scope. Any action plan dependent on this tool carries a dependency risk that must be flagged to the client.

---

## How This Researcher Verifies Claims

- llms.txt presence: always checked via direct URL — never assumed
- Crawler access: always read from robots.txt directly — never inferred from CMS defaults
- MCP registry: always checked at the current registry source with a date stamp — never cited from memory
- Live agent testing: always run on the actual platform — never assumed from third-party reports
- Confirmed vs emerging: a mandatory split — every finding is classified before delivery
- Never recommend MCP without first confirming Track A (discovery) gaps are addressed
- "Listed but not released" and "documented but not confirmed" are required qualifiers — never collapse them into "available" or "confirmed"

---

## Procedure 03 — Source Audit

Client requested adversarial review specifically for MCP findings before making an investment decision. 6 findings reviewed.

---

**Finding: llms.txt — 404, missing — confirmed · T2**
Audit: **PASS**
Direct URL check. T2. Correctly stated.

---

**Finding: REI has llms.txt with specific content — confirmed · T2**
Audit: **PASS**
Direct URL check confirmed. Content described (brand description, product category index, return policy summary, store locator API reference). T2. Correctly stated. This is the strongest comparative finding in the session — a same-category competitor with a live, structured llms.txt.

---

**Finding: "REI dominates because of buying guides, expert content, and structured product data"**
Audit: **FLAGGED — causal mechanism is inference bundled with a confirmed observation**
Two things are true: (1) REI appears consistently in AI shopping queries — `confirmed · T2`. (2) REI has buying guides, expert content, and structured product pages — observable. But the claim that REI dominates *because of* these things is a causal inference. The investigation showed REI appears and has this content; it did not test whether the content is what drives citation. The mechanism is `unconfirmed · T4` — plausible but not proven. Revision: "REI appears in all three test queries — `confirmed · T2`. REI's content profile includes buying guides, expert reviews, and structured product listings. Whether these are the primary citation drivers is `unconfirmed · T4` — consistent with citation patterns in `geo-content-framework.md` but not directly tested."

---

**Finding: "Early-mover window is open — REI does not appear to have a public MCP server"**
Audit: **FLAGGED — absence is stated as weaker than it is**
"Does not appear to have" is vague. What was checked? The investigation checked modelcontextprotocol.io registry as of 2026-05-27. REI was not found listed. That's T2 — directly checked. The finding should say: "REI not found in MCP registry at modelcontextprotocol.io as of 2026-05-27 — `confirmed · T2`. Cannot rule out a private or enterprise MCP implementation not listed in the public registry. The early-mover claim is based on public registry absence only."

---

**Finding: Shopify MCP — listed in registry, in development, not yet released — emerging**
Audit: **PASS**
Registry checked with date stamp. "Listed but not released" qualifier applied. "Emerging" status correctly applied. This is the highest-stakes finding for the client's investment decision and it's handled correctly.

---

**Finding: Product search by spec — High-value Track B opportunity via Shopify MCP**
Audit: **FLAGGED — recommendation depends on an unreleased tool**
The opportunity assessment is sound. But "High-value opportunity" implies near-term actionability. The Shopify MCP is not released. The correct framing: "High-value opportunity contingent on Shopify MCP release. Until released, the client should monitor the registry and prepare the data layer (catalog metadata, product tagging) so they can activate quickly when the tool is available. Do not begin integration work against an unreleased API."

---

### Gaps Not Surfaced

**Catalog data quality not assessed.** Track B recommendation for "use-case recommendation" requires catalog enrichment (product tagging by use case, climate, season). The current state of the catalog metadata wasn't investigated. If the catalog has minimal metadata now, the enrichment effort is substantial — this changes the sequencing recommendation.

**Other major outdoor gear retailers not checked for MCP presence.** REI was checked; Backcountry and Moosejaw were not. If Backcountry already has MCP exposure, the early-mover framing changes significantly.

---

### Audit Summary

6 findings reviewed. 2 passed clean. 2 flagged for causal inference (REI mechanism, early-mover basis). 1 flagged for actionability framing (Shopify MCP recommendation). 1 passed with stronger verification language needed.

**Actionable without revision:** llms.txt gap. REI comparison (observation, not mechanism). Shopify MCP monitoring.
**Requires revision before sharing:** REI dominance mechanism (inference not finding). Early-mover claim (registry absence, not confirmed absence). Shopify MCP recommendation framing (contingent, not actionable today).
**Requires additional investigation:** Catalog metadata state. Backcountry and Moosejaw MCP presence.
