# Sales leaking out as discounts and refunds

Channel: Money · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Sales leaking out as discounts and refunds" (id: ops-gross-to-net-leak, Money).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Shows the gap between what you sold at list price and what you kept after discounts and refunds. It splits the gap by channel and by type, so a creeping promo habit or a refund problem shows up as dollars, not as a vague margin dip.

What to read: Accounting ledger product sales, discounts and refunds by month and channel
What to give me: How many dollars go back out as discounts and refunds each month, by channel, and which is growing

Synthesis tools to use:
- `cost_rules for=ops-gross-to-net-leak`
- `netsuite_metric metric=gross_to_net_bridge months=12`
- `netsuite_metric metric=contra_revenue months=12`
- `netsuite_metric metric=refund_rate months=12`

Steps:
1. Call `netsuite_metric metric=gross_to_net_bridge months=12` for product sales, discounts, refunds and net revenue per month.
2. Call `netsuite_metric metric=contra_revenue months=12` for discount and refund dollars by channel.
3. Call `netsuite_metric metric=refund_rate months=12` for refund dollars and rates by channel.
4. For each channel, compute discount dollars and refund dollars per month, and the change between the average of the last three full months and the three before.
5. Rank the lines by dollar increase. Keep the top three.

Checks before answering:
- Use the bridge for discount and refund DOLLARS only. Its margin columns are raw ledger and overstated.
- Marketplace sales are booked net, so a marketplace discount or refund RATE is meaningless. If the tool returns NULL for a rate, say the rate is not measurable and use dollars.
- Drop the running month. The refund series includes it, and a part month reads low.
- Drop any partial first month of the ledger. It is far smaller than a real month.
- If the brand has no ledger connected, say so and stop.

Output:
- Table: Channel | Discounts per month (last 3 vs prior 3) | Refunds per month (last 3 vs prior 3) | Change in dollars.
- Three lines: the biggest leak in dollars a month, the likely reason to check, and the one move.

Never:
- Never present a marketplace discount or refund rate.
- Never add invoiced revenue by account to statement revenue. They are different measures.
- Never change a price, promo or policy. A person decides.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Before step 1, call cost_rules. If it returns questions, ask them in one message as written (dollars, choices, what skip does) and save each answer with set_cost_rule. On a scheduled run, use the defaults and list the questions at the end. End the answer with its used_line.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: ops-gross-to-net-leak". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
