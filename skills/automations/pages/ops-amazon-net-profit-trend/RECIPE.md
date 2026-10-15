# Amazon profit, line by line, month by month

Channel: Money · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Amazon profit, line by line, month by month" (id: ops-amazon-net-profit-trend, Money).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Lays out Amazon profit for the last six settled months as one waterfall per month: sales, referral fee, fulfilment fee, product cost, advertising, net. It shows which line is eating the margin over time, which no single-month view can show.

What to read: Amazon settlement sales, fees, product cost and ad spend by month
What to give me: Six months of Amazon account profit line by line down to net, and which line moved

Synthesis tools to use:
- `amazon_metric metric=pnl_waterfall month=YYYY-MM`
- `operator_inputs section=cogs`

Steps:
1. Call `amazon_metric metric=pnl_waterfall month=YYYY-MM` once for each of the last six months.
2. For each month keep each line's dollars and share of sales.
3. Call `operator_inputs section=cogs` to confirm every product sold has an entered cost. List products with sales and no cost.
4. Compare the newest settled month to the average of the three before. Name the line whose share of sales moved the most.
5. Each waterfall carries `settlement_status`. Mark a month part-settled when it says the month is not fully settled. Amazon pays roughly every two weeks with a few days of lag.

Checks before answering:
- Refunds are already netted into sales on this waterfall. Do not subtract them again.
- If any product with sales has no cost, profit is overstated. Say how much revenue is uncosted, and never treat a missing cost as zero.
- A part-settled month reads low on sales and odd on fee rate. Label it and leave it out of the trend comparison.
- If ad spend is zero for a month with known campaigns, the ad feed may be missing. Say so rather than reporting a profit jump.

Output:
- Table: Month | Sales | Referral fee | Fulfilment fee | Product cost | Ads | Net | Net as % of sales.
- Two lines: the trend in net margin, and the line responsible.

Never:
- Never mix the full-company ledger into this view. This is Amazon only.
- Never fill a missing product cost with a guess.
- Never change bids, prices or listings.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: ops-amazon-net-profit-trend". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
