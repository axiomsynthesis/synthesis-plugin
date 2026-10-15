# Where customers wait longest for support

Channel: Support · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Where customers wait longest for support" (id: grw-support-speed, Support).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Shows how long tickets take to close by channel such as email, chat and social, and by agent. It finds where customers wait longest and whether the fix is people, hours or a saved reply.

What to read: Gorgias time to close by channel, agent and month
What to give me: Wait times by channel and agent, and the staffing or saved-reply fix

Synthesis tools to use:
- `gorgias_metric metric=resolution_sla months=6`
- `gorgias_metric metric=agent_performance months=3 limit=20`
- `gorgias_metric metric=channel_mix months=6`

Steps:
1. Pull `gorgias_metric metric=resolution_sla months=6`.
2. Pull `gorgias_metric metric=agent_performance months=3 limit=20`.
3. Pull `gorgias_metric metric=channel_mix months=6`.
4. Report median and 90th percentile minutes to close by channel and month.

Checks before answering:
- If Gorgias is not connected, say the helpdesk is not connected. Never say zero tickets.
- Customer satisfaction scores do not exist in this feed. Never estimate them from speed.
- Time to close is closed minus created. First response time is unreliable here. Say time to close, in minutes.

Output:
- Answer first. Table: channel, tickets, median minutes to close, 90th percentile. A short agent table.

Never:
- Nothing changes in any live account. A person on your team makes every change.
- Never fill a missing, gated or empty number with an estimate. Say what is missing and why.
- Never rank people as good or bad. Show workload beside speed.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: grw-support-speed". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
