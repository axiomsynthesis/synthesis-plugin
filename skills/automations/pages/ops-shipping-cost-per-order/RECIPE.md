# What each website order costs to ship

Channel: Inventory · Level: Advise · Status: Ready after we build it

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "What each website order costs to ship" (id: ops-shipping-cost-per-order, Inventory).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Shows the real shipping cost per website order and splits it by carrier, service level and order size. Shipping is often the second-largest cost on a website order and the one nobody watches.

What to read: Per-shipment carrier cost from your shipping software and website orders
What to give me: Shipping cost per order by carrier, service and order size, and where you overpay

Synthesis tools to use:
- `shopify_metric metric=aov_distribution`
- `netsuite_metric metric=opex_category months=3 limit=20`

Steps:
1. Once connected, read per-shipment cost, carrier, service, weight and destination for the last 90 days.
2. Join to orders and call `shopify_metric metric=aov_distribution` for order value bands.
3. Compute cost per order and cost as a share of order value by band, carrier and service.
4. Find orders shipped faster than promised delivery needed.
5. Until then, call `netsuite_metric metric=opex_category months=3 limit=20` for total booked shipping cost and divide by website orders, labelled as a rough average.

Checks before answering:
- The shipping tables refresh over a trailing window. Older rows drop out; widen the window rather than calling history missing.
- An empty pull still replaces the table. Check the sync result before believing a drop to zero.
- The carrier invoice and the books are the truth for money; shipping software is an operational read.
- Booked shipping may include inbound freight. Say so when using it.

Output:
- Table: Order value band | Orders | Cost per order | Cost as % of value | Main carrier and service.
- Two lines: the biggest saving in dollars a month, and the change behind it.

Never:
- Never change carrier rules or shipping settings.
- Never present booked shipping divided by orders as measured per-order cost.
- Never handle the shipping software key. The brand connects it.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: ops-shipping-cost-per-order". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.

Not fully ready yet (ready after we build it): ShipStation and ShipHero connectors exist but no brand has connected one and there is no reader tool. Needs a connected account and a shipping-cost tool returning cost by shipment, carrier, service and order. Do the parts you can and say plainly what is missing.
