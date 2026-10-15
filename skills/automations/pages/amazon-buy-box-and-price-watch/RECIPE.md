# Know the moment you lose the Buy Box

Channel: Amazon · Level: On a schedule · Status: Ready now
Schedule: every day 8am

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Know the moment you lose the Buy Box" (id: amazon-buy-box-and-price-watch, Amazon).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Checks each morning who holds the buy box on each of your products, and at what price. When another seller has it, or Amazon shows no buy box while your offer is live, it names the seller, their price, how long it has lasted and the sales at risk.

What to read: Amazon offers, prices
What to give me: Products another seller is winning, who holds it at what price, and the sales at risk each day

Synthesis tools to use:
- `amazon_metric metric=buybox_watch`
- `find_product`

Steps:
1. Call `amazon_metric` with `metric=buybox_watch` and `limit=50` to get today's holder, prices, days off and sales at risk for every product.
2. Read `headline` first. It counts the products off the buy box and the dollars at risk.
3. For each product in `off_buybox`, note the seller id, the buy box price, your price, the gap and the days off.
4. Use `find_product` to name each product the way the brand does.
5. List the `no_live_offer` products apart. You have no live offer on them, so they are a stock or listing question, not a lost buy box.

Checks before answering:
- If the result is gated or says it could not check, say the buy box could not be checked and why. Never report "you own every buy box" from a failed or stale check.
- Name any product that could not be checked. It is not held and not lost.
- Sales at risk is an estimate and the most it could be. Say so.
- Name sellers by the seller id the tool returns. Never guess a seller name.
- One check is one moment. When two sellers ask the same price, Amazon can share the buy box through the day.

Output:
- One line first: how many products are off the buy box and the sales at risk in dollars.
- A table: product, who holds it, buy box price, your price, gap, days off, sales at risk.
- One move: which product to check first and what to look at.

Never:
- Never change a price or file a report in Seller Central. A person does that.
- Never name a seller or price the tools did not return.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: amazon-buy-box-and-price-watch". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
- This is meant to repeat (every day 8am). Run it once now. If you can set up a repeating task here, do it. If not, tell me how to run this again each time it is due.
