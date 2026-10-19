# Check for Amazon fee jumps

Channel: Money · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Check for Amazon fee jumps" (id: amazon-fee-overcharge-check, Money).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Finds Amazon fees that changed for no business reason, like a product re-measured into a bigger size tier or a referral rate that crept up. It sizes each change in dollars a month and says which ones are worth a case with Amazon. It finds changes only. A fee that was wrong from the start, or a storage, placement or returns fee, is not checked yet.

What to read: Amazon settlement fees by product
What to give me: Every product whose fee per unit or referral rate changed, and what it costs

Synthesis tools to use:
- `cost_rules for=amazon-fee-overcharge-check`
- `amazon_metric metric=fee_anomaly`
- `amazon_metric metric=fee_rate_trend`
- `amazon_metric metric=fee_breakdown month=YYYY-MM`
- `find_product`

Steps:
1. Call `amazon_metric` with `metric=fee_anomaly` and `months=6` to get per-unit fulfilment fee step changes and referral rate drift by product.
2. Call `amazon_metric` with `metric=fee_rate_trend` and `months=12` to see whether fees as a share of sales are creeping across the whole catalog.
3. Call `amazon_metric` with `metric=fee_breakdown` and `month=YYYY-MM` set to the latest closed month to put the changes next to total referral and fulfilment fees. If it marks that month still posting while the fee change tool counts it closed, say the two disagree and use the month before for totals only.
4. For each product with a step change, use `find_product` to name it the way the brand does, and multiply the change per unit by last month's units for the monthly cost.
5. Rank by monthly cost and mark the ones that look like a size tier or weight change.

Checks before answering:
- Use settled months only. A month still settling can look like a fee jump that is not there.
- A step change needs at least two weeks at the new fee before it counts. One odd order is not a change.
- If the fee tools return nothing or an error, say the fee data could not be read. Never report "no overcharges" from an empty result.
- Check the change against a price change. A referral fee rises with price, and that is not an overcharge.
- "Per unit" is really per order line. A month with many multi-unit orders can look like a jump. Say so beside any jump.
- If fees as a share of sales rose with no product jump, say it is mix or price, a pricing and pack-size question, not a case to open.

Output:
- One line answer first: open a case or not, and how much a month the fee changes cost.
- One line on fees as a share of sales over 12 months, and what drove it.
- A table: product, old fee per unit, new fee per unit, date it changed, units a month, cost a month, likely cause.
- One move: which product to open a case for first, and what to ask Amazon to re-measure.

Never:
- Never open a case or change anything in Seller Central. A person does that.
- Never guess a fee or a unit count that the tools did not return.
- Never call a fee change an overcharge without saying how sure you are and why.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Before step 1, call cost_rules. If it returns questions, ask them in one message as written (dollars, choices, what skip does) and save each answer with set_cost_rule. On a scheduled run, use the defaults and list the questions at the end. End the answer with its used_line.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: amazon-fee-overcharge-check". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
