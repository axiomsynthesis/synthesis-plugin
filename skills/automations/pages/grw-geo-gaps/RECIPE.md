# States that buy but get no ads

Channel: Customers · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "States that buy but get no ads" (id: grw-geo-gaps, Customers).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Compares where your website sales come from with where your ads spend. It finds states buying well with little ad support and states taking spend without sales.

What to read: Website revenue by state and ad spend by region
What to give me: States where demand is ahead of ad spend, and states you pay for without sales

Synthesis tools to use:
- `shopify_metric metric=state_revenue`
- `meta_metric metric=breakdown dimension=region limit=60`
- `google_ads_metric metric=geo days=90 limit=60`

Steps:
1. Pull `shopify_metric metric=state_revenue`.
2. Pull `meta_metric metric=breakdown dimension=region limit=60` and `google_ads_metric metric=geo days=90 limit=60`.
3. Compute each state's share of revenue and share of combined spend.
4. Flag gaps over 3 points either way.

Checks before answering:
- Revenue per person matters. Mention state population only from a reliable source, if used.
- Small states under $1,000 revenue are listed, not judged.

Output:
- Answer first. Table: state, revenue share, spend share, gap, move.

Never:
- Nothing changes in any live account. A person on your team makes every change.
- Never fill a missing, gated or empty number with an estimate. Say what is missing and why.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: grw-geo-gaps". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
