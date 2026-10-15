# Write saved replies for top questions

Channel: Support · Level: Prepare · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Write saved replies for top questions" (id: grw-support-macro-drafts, Support).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Finds the questions customers ask most and drafts a saved reply for each, using your own policies and product facts. Agents answer faster and give the same answer every time.

What to read: Gorgias contact reasons and topics, and your own product facts
What to give me: Draft saved replies for the top ten contact reasons, in your voice

Synthesis tools to use:
- `gorgias_metric metric=contact_reasons months=3`
- `gorgias_metric metric=topic_trends months=3`
- `search_knowledge query=<topic>`

Steps:
1. Pull `gorgias_metric metric=contact_reasons months=3`.
2. Pull `gorgias_metric metric=topic_trends months=3` for the wording customers use.
3. For each top reason, run `search_knowledge` for the policy or product fact.
4. Draft a reply under 120 words with the fact, the next step and a link placeholder.

Checks before answering:
- If Gorgias is not connected, say the helpdesk is not connected. Never say zero tickets.
- Read tag categories, never raw tag counts. Raw tags mix real reasons with spam and auto-replies.
- Never invent a policy. If the knowledge search finds none, mark the draft needs a policy.

Output:
- A document via `export_docx` named support-replies-<date>.docx: reason, share of tickets, draft reply, source of each fact.

Never:
- Nothing changes in any live account. A person on your team makes every change.
- A person loads replies into the helpdesk.
- Never fill a missing, gated or empty number with an estimate. Say what is missing and why.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: grw-support-macro-drafts". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
