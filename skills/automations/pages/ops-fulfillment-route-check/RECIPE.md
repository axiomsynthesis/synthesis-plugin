# Amazon fulfilment or your own warehouse?

Channel: Inventory · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Amazon fulfilment or your own warehouse?" (id: ops-fulfillment-route-check, Inventory).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Flags products where Amazon's fulfilment and storage fees look heavy for their size and price, so you know which ones to get warehouse quotes for. It is a shortlist for pricing, not a decision, because it has never seen a warehouse's quote.

What to read: Monthly units, price, size and Amazon fulfilment and storage fees per product
What to give me: For each product, whether Amazon fulfilment, a third-party warehouse or a mix is worth pricing, with the fees at stake

Synthesis tools to use:
- `amazon_metric metric=storage_fee_forecast`
- `amazon_metric metric=contribution_by_asin months=3`
- `amazon_metric metric=fulfillment_mix month=YYYY-MM`
- `decide_fulfillment unit_volume_monthly=<units> avg_price=<price> oversized=<true|false>`

Steps:
1. Call `amazon_metric metric=contribution_by_asin months=3` for units, price and fulfilment fees per product.
2. Call `amazon_metric metric=storage_fee_forecast` for each product's storage a month and its cubic feet per unit.
3. Call `amazon_metric metric=fulfillment_mix month=YYYY-MM` to see what already ships from your own stock.
4. For each product, run `decide_fulfillment unit_volume_monthly=<units> avg_price=<price> oversized=<true|false>`. Ask whether it is oversized if not known.
5. Compute fulfilment plus storage as a share of price per product.
6. Shortlist products where the rule suggests a warehouse or a mix and fees exceed 25% of price.

Checks before answering:
- The rule uses three thresholds only. A product within a few hundred units of 2,000 a month, or within a dollar of $12, sits on a knife edge. Say so.
- Moving off Amazon fulfilment can cost the Prime badge and conversion. Name that cost; it is not in the fees.
- Use settled months for fees.
- Without a warehouse quote there is no saving, only a fee to beat. Say "fee to beat" until a quote arrives.

Output:
- Table: Product | Units a month | Price | Amazon fees per unit | Fees as % of price | Rule says | Fee to beat.
- One line: the products to request quotes for.

Never:
- Never move stock or change fulfilment settings.
- Never present the rule's answer as a decision.
- Never contact a warehouse.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: ops-fulfillment-route-check". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
