# How long your cash is stuck

Channel: Money · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "How long your cash is stuck" (id: ops-cash-conversion-cycle, Money).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Measures the gap between cash going out to suppliers and cash coming back from customers. It shows which of the three parts drives it: stock building up, slow payouts, or paying suppliers too early. Each extra day is cash sitting on a shelf.

What to read: Stock value, product cost, channel payout timing and supplier payment terms
What to give me: Days from paying the factory to getting paid, and which part of that moved

Synthesis tools to use:
- `netsuite_metric metric=inventory_position limit=50`
- `netsuite_metric metric=pnl_trend months=6`
- `operator_inputs section=purchase_orders`
- `ccc_health dio=<days> dso=<days> dpo=<days> archetype=<category_type>`

Steps:
1. Call `netsuite_metric metric=inventory_position limit=50` for stock value on hand.
2. Call `netsuite_metric metric=pnl_trend months=6` for monthly product cost on closed months. Days of inventory = stock value divided by average daily product cost.
3. Days to get paid: compute per channel. Amazon pays in roughly two-week cycles plus a few days. Card-paid website orders settle in days. Retail accounts pay on their terms. Weight by each channel's share of revenue, and show each channel's figure.
4. Days to pay suppliers: ask for the terms. They are not stored. Purchase orders give dates, not terms.
5. Call `ccc_health dio=<days> dso=<days> dpo=<days> archetype=<category_type>`. Pass the archetype only when the person confirms it, and say which band was used.
6. If a prior reading exists, say which of the three inputs moved.

Checks before answering:
- Days of inventory needs product cost from closed months. An estimate month's cost can be off by six figures.
- The tool accepts any number, including negative days. Sanity check each input before passing it.
- Without the archetype the tool uses its tighter band. The same cycle can read amber or red depending on that one argument. State it.
- If supplier terms are not given, report the cycle as "not measurable" and show the two parts that are.

Output:
- Four lines: the cycle in days, each of the three parts with its source, and the cash freed by the most realistic change.
- Quote the tool's band thresholds beside its colour.

Never:
- Never quote the ledger's working-capital movement as a balance.
- Never assume supplier terms.
- Never change terms or contact a supplier.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: ops-cash-conversion-cycle". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
