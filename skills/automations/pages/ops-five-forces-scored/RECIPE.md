# What's squeezing your margins?

Channel: Strategy · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "What's squeezing your margins?" (id: ops-five-forces-scored, Strategy).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Scores the five pressures on profit in your category (rivals, new entrants, substitutes, supplier power, buyer power) from evidence rather than opinion. It ends with the one pressure costing the most and the move that eases it.

What to read: Category concentration, rival shelf and price moves, supplier spend dependence, channel dependence and own-label risk
What to give me: A score for each of the five industry pressures with the evidence, and the one that squeezes margin most

Synthesis tools to use:
- `strategy_framework framework=five_forces`
- `strategy_framework framework=hhi`
- `amazon_metric metric=search_competitors`
- `amazon_metric metric=shelf_position`
- `netsuite_metric metric=vendor_spend limit=20`
- `private_label_threat`

Steps:
1. Rivalry and entrants: call `amazon_metric metric=search_competitors` for rivals taking clicks on your searches and `amazon_metric metric=shelf_position` for their prices, ranks and new names. Run `strategy_framework framework=hhi shares=[...]` on the shares for concentration.
2. Supplier power: call `netsuite_metric metric=vendor_spend limit=20` for spend share per supplier.
3. Buyer power: use your channel dependence from invoiced revenue by account and Amazon fee rate trend.
4. Substitutes: ask the founder; check search demand for substitute terms if named.
5. Own-label risk: run `private_label_threat` with measured or stated inputs.
6. Score each force 0 to 10 with one line of evidence, then run `strategy_framework framework=five_forces supplier_power=<0-10> buyer_power=<0-10> new_entrants=<0-10> substitutes=<0-10> rivalry=<0-10>`.

Checks before answering:
- Every score cites evidence. A force with none is marked "judged".
- Shelf and search share data is a snapshot. Give its date.
- Shares in percent and in fractions must not be mixed in one calculation.

Output:
- Table: Force | Score | Evidence | Source.
- Two lines: the force squeezing margin most, and the move that eases it.

Never:
- Never present a judged score as measured.
- Never copy any book's text.
- Never act on the move.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: ops-five-forces-scored". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
