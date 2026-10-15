# Is your email list growing or rotting?

Channel: Email · Level: Advise · Status: Ready after we build it

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Is your email list growing or rotting?" (id: grw-email-list-health, Email).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Tracks how many people join the list each month, from which form or source, and how many go quiet or unsubscribe. A list growing in size but shrinking in readers costs money and hurts inbox placement.

What to read: Klaviyo profiles added, suppressed and engaged by month, by signup source
What to give me: Whether your list is growing in people who actually read, and which signup sources bring them

Synthesis tools to use:
- `klaviyo_metric metric=campaign_scorecard limit=40`

Steps:
1. When a reader exists: pull profile growth by month and signup source, suppressions and the 90-day engaged count.
2. Today, `klaviyo_metric metric=campaign_scorecard limit=40` gives list size per send as a rough trend only.

Checks before answering:
- List size per send changes with segment choice. Never present it as list growth.

Output:
- Table by month: joined, unsubscribed, suppressed, engaged in 90 days, top source.

Never:
- Nothing changes in any live account. A person on your team makes every change.
- Never fill a missing, gated or empty number with an estimate. Say what is missing and why.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: grw-email-list-health". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.

Not fully ready yet (ready after we build it): Profile and list-membership data is not synced from Klaviyo. A connector extension and a reading tool are needed. Do the parts you can and say plainly what is missing.
