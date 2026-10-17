# How much profit comes from repeat buyers?

Channel: Amazon · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "How much profit comes from repeat buyers?" (id: mkt-amazon-new-vs-repeat-profit, Amazon).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Splits Amazon profit between first orders and repeat orders. A rising repeat share means past ad spend is paying off now.

What to read: Amazon sales, cost and fees split by first-time buyers and buyers who ordered before
What to give me: How much of your Amazon profit comes from repeat buyers, how that share is moving, and what it means for ad spend

Synthesis tools to use:
- `amazon_metric metric=pnl_by_customer_type days=90`
- `amazon_metric metric=pnl_by_customer_type start_date=<YYYY-MM-DD> end_date=<YYYY-MM-DD>`
- `amazon_metric metric=tacos`

Steps:
1. Call `amazon_metric metric=pnl_by_customer_type days=90`, and again with `start_date` and `end_date` set to the same 90 days a year earlier. One call covers at most 90 days.
2. Compare order share, revenue share and profit share for new and repeat buyers, now and over the year.
3. Call `amazon_metric metric=tacos month=<last closed month>` to set the ad cost beside it.

Checks before answering:
- New-to-brand here means the buyer's first order ever with you on Amazon. Amazon's own ad reports use a 12-month rule. Never mix the two.
- Profit needs entered product costs. Name missing costs.
- A buyer's history starts when your synced order history starts. A loyal buyer from before that date looks new. If history is under two years, say new is overstated.

Output:
- Two lines: repeat share of profit now and a year ago.
- A table: buyer type, orders, revenue, profit, average order value.

Never:
- Never compare this new-buyer count with Amazon's ad new-to-brand count as if they were the same.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: mkt-amazon-new-vs-repeat-profit". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
