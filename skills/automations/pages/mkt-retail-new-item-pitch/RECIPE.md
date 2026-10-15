# Pitch a new item to a retail buyer

Channel: Retail · Level: Prepare · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Pitch a new item to a retail buyer" (id: mkt-retail-new-item-pitch, Retail).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Buyers want proof before they give shelf space. This builds a short pitch from your own online sales, reviews and search demand.

What to read: Your Amazon proof for the item, sales rate, growth, rating, repeat buying and search demand in its category
What to give me: A short pitch deck for one new item, backed by your online sales, search demand and reviews

Synthesis tools to use:
- `amazon_metric metric=velocity_momentum weeks=26`
- `amazon_metric metric=search_query_trend grain=month periods=12`
- `amazon_metric metric=review_velocity days=90 limit=10`
- `repeat_rate`
- `export_pptx`

Steps:
1. Ask for the item, the retailer and what you will ask for (stores, price, launch date, promotion support).
2. Call `amazon_metric metric=velocity_momentum asin=<product id> weeks=26` for weekly units and growth, event weeks tagged.
3. Call `amazon_metric metric=search_query_trend grain=month periods=12` for category demand.
4. Call `amazon_metric metric=review_velocity days=90 limit=10` for rating and review count.
5. Call `repeat_rate asin=<product id>` for the share of first-time buyers of the item who ordered again.
6. Build six slides with `export_pptx` (title plus one dict per slide with bullets or a small table): the item, proof it sells, who buys and rebuys, category demand, the ask, how you will support it in store.

Checks before answering:
- Online sales do not predict store sales one to one. Say the deck shows proof of demand, not a store forecast.
- Leave event weeks out of the growth figure.
- Search shares are percentages already. Never rescale.
- Use the retailer's language for velocity: units per store per week only if you have store data. Otherwise say online units per week.

Output:
- One line: the strongest proof point.
- A six-slide deck file, numbers from tool calls only.

Never:
- Never send the deck to a buyer. A person sends it.
- Never promise store velocity from online sales.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: mkt-retail-new-item-pitch". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
