# Research Brief — Claude Projects

## Default: Markdown in Conversation

At the end of a session, say: **"Generate the research brief."**

The AI outputs the brief as formatted markdown directly in the conversation. Read findings, copy sections, or reference it for follow-up sessions — no extra steps required.

## On Demand: HTML Export

Say: **"Give me the HTML export."**

The AI populates the `report-template.html` stored in `references/` with session data and outputs the complete, self-contained HTML in conversation.

**To save and open:**
1. Copy the entire HTML block from the conversation
2. Save to a file with `.html` extension (e.g., `research-brief-2026-05-28.html`)
3. Open in your browser
4. File → Print → Save as PDF

## Why Two Modes

Full HTML generation in-session has a token cost. The markdown default keeps session budget available for continued research. HTML export is user-triggered — appropriate for sessions that have produced findings worth preserving as a client deliverable.

## What the AI Fills In

When populating the HTML template, the AI replaces every `{{VARIABLE}}` placeholder with real session data. It does not change the visual design — that's locked in the template. It only fills in your session's content.
