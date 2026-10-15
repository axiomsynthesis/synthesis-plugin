# Spot product problems early from support

Channel: Support · Level: On a schedule · Status: Ready now
Schedule: weekly Monday 9am

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Spot product problems early from support" (id: grw-support-defect-alert, Support).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Every week, checks whether any complaint topic is climbing, such as leaking caps, a bad batch or a broken checkout. Support sees product trouble weeks before reviews and sales do.

What to read: Gorgias ticket topics by month with a rising-topic flag, and ticket volume
What to give me: An alert when a complaint topic starts rising, before it shows in reviews or returns

Synthesis tools to use:
- `gorgias_metric metric=topic_trends months=3`
- `gorgias_metric metric=ticket_volume months=3`
- `gorgias_metric metric=contact_reasons months=3`

Steps:
1. Pull `gorgias_metric metric=topic_trends months=3` and keep topics flagged rising.
2. Pull `gorgias_metric metric=ticket_volume months=3` to judge each topic against total volume.
3. Pull `gorgias_metric metric=contact_reasons months=3` for the matching reason bucket.
4. Alert when a topic's share of tickets doubled against its 8-week average on at least 15 tickets.

Checks before answering:
- If Gorgias is not connected, say the helpdesk is not connected. Never say zero tickets.
- Topics come from subject lines only; ticket bodies are not synced. Say so.
- Read tag categories, never raw tag counts. Raw tags mix real reasons with spam and auto-replies.
- The topic table is rewritten each run and runs a few days behind. Say the newest date.

Output:
- One line when quiet. When rising: topic, tickets this week, normal, example subject lines (no customer names), likely product.

Never:
- Nothing changes in any live account. A person on your team makes every change.
- Never fill a missing, gated or empty number with an estimate. Say what is missing and why.
- Never quote a customer's name or email.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: grw-support-defect-alert". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
- This is meant to repeat (weekly Monday 9am). Run it once now. If you can set up a repeating task here, do it. If not, tell me how to run this again each time it is due.
