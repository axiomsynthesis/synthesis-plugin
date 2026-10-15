# Is your affiliate platform over-claiming?

Channel: Creators · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Is your affiliate platform over-claiming?" (id: grw-affiliate-vs-amazon-attribution, Creators).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
You pay affiliates on the platform's numbers. This checks those numbers against Amazon's own attribution for the same months, so payouts rest on sales Amazon also saw.

What to read: Affiliate platform sales against Amazon Attribution sales for the same links
What to give me: Where the affiliate platform claims more sales than Amazon recorded, and by how much

Synthesis tools to use:
- `levanta_metric metric=marketplace_reconciliation months=3`
- `levanta_metric metric=marketplace_mix months=3`
- `amazon_metric metric=attribution_sources days=90 limit=50`

Steps:
1. Pull `levanta_metric metric=marketplace_reconciliation months=3`.
2. Pull `levanta_metric metric=marketplace_mix months=3` to see sales by marketplace.
3. Pull `amazon_metric metric=attribution_sources days=90 limit=50` for the same partners by Amazon's count.
4. Compare per month and per partner where names match. Show the gap in dollars and percent.

Checks before answering:
- Creator sales are the platform's own attribution. They will not tie to your order records, and they are a slice of the shop, not all of it.
- Overlapping sources are shown side by side, never added together.
- Sales on a marketplace you do not sell on are a labelling error. Flag them.
- Small gaps under 5% are normal lag and settling.

Output:
- Answer first: the total gap. Table: month or partner, platform sales, Amazon-attributed sales, gap.

Never:
- Nothing changes in any live account. A person on your team makes every change.
- Never dispute a payout for the person.
- Never fill a missing, gated or empty number with an estimate. Say what is missing and why.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: grw-affiliate-vs-amazon-attribution". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
