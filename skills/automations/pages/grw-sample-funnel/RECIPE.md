# Do free samples turn into sales?

Channel: Creators · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Do free samples turn into sales?" (id: grw-sample-funnel, Creators).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Free samples cost product and shipping. This follows each sample to a post and to sales, so you can see your real cost per posting creator and stop sending to groups that never post.

What to read: Samples sent to creators, posts made and sales after
What to give me: How many samples became posts and sales, and the cost per creator who posted

Synthesis tools to use:
- `cruva_metric metric=sample_funnel days=90`
- `cruva_metric metric=outreach_health days=90`
- `cruva_metric metric=content_performance days=90 limit=25`

Steps:
1. Pull `cruva_metric metric=sample_funnel days=90`.
2. Pull `cruva_metric metric=outreach_health days=90`.
3. Pull `cruva_metric metric=content_performance days=90 limit=25`.
4. Ask for product cost and shipping per sample, then compute cost per posting creator and per dollar of creator sales.

Checks before answering:
- Creator sales are the platform's own attribution. They will not tie to your order records, and they are a slice of the shop, not all of it.
- Samples sent in the last 21 days have not had time to post. Show them apart.
- If the platform is not connected, say so. Never report zero samples.

Output:
- Answer first: post rate and cost per posting creator. Funnel table: sent, posted, earned, cost.

Never:
- Nothing changes in any live account. A person on your team makes every change.
- Never fill a missing, gated or empty number with an estimate. Say what is missing and why.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: grw-sample-funnel". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
