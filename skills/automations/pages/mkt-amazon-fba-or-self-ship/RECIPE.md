# Should Amazon ship this, or should you?

Channel: Amazon · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Should Amazon ship this, or should you?" (id: mkt-amazon-fba-or-self-ship, Amazon).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Amazon's fulfilment gives the Prime badge but its fees hit bulky, slow products hard. This checks each product with a simple rule and names the few worth a quote.

What to read: Monthly units, price and Amazon fulfilment fees per product, and how orders split between Amazon and self-fulfilled today
What to give me: Products that may cost less to ship yourself or through a third-party warehouse, and the ones that must stay with Amazon

Synthesis tools to use:
- `amazon_metric metric=fulfillment_mix`
- `amazon_metric metric=pnl_by_asin limit=40`
- `decide_fulfillment`

Steps:
1. Call `amazon_metric metric=fulfillment_mix month=<last closed month>` for the current split.
2. Call `amazon_metric metric=pnl_by_asin limit=40` for units, price and fulfilment fee per unit.
3. For each product, call `decide_fulfillment` with monthly units, average price and whether it is oversized.
4. For products the rule says to move, size the saving against a quote the person enters. Never assume a quote.

Checks before answering:
- Multi-channel fulfilment orders are other channels using Amazon's warehouse. Keep them out of Amazon sales.
- Losing Prime can cut conversion. Say this cost is not in the rule.
- Use a closed month.

Output:
- One line: products to keep and products worth a quote.
- A table: product, monthly units, price, fulfilment fee per unit, rule result.

Never:
- Never change fulfilment settings.
- Never invent a third-party warehouse price.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: mkt-amazon-fba-or-self-ship". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
