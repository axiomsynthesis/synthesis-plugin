# Are your Walmart ads paying?

Channel: Walmart · Level: Advise · Status: Ready after we build it

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Are your Walmart ads paying?" (id: mkt-walmart-sponsored-search-check, Walmart).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Measures Walmart sponsored search the way you measure Amazon ads: return per dollar, wasted keywords, and ad share of total sales.

What to read: Walmart Connect sponsored search spend, sales and return by campaign and keyword, against Walmart Marketplace orders
What to give me: Whether Walmart ads pay, the keywords wasting money, and ad sales against total Walmart sales

Synthesis tools to use:
- `walmart_metric metric=revenue months=6`
- `walmart_metric metric=top_skus months=3 limit=20`

Steps:
1. Once Walmart ad data is synced: read spend, clicks, sales and return per campaign and keyword for 30 days.
2. Call `walmart_metric metric=revenue months=6` for total Walmart sales. Ad sales are a slice of it. Never add them.
3. Call `walmart_metric metric=top_skus months=3 limit=20` to see which items carry ad-driven sales.
4. List keywords with spend and no sales, and campaigns below your break-even.

Checks before answering:
- Until ad data exists, never present a Walmart ad figure.
- Ad-credited sales use Walmart's window. Recent days will still grow.

Output:
- One line: return per dollar and waste.
- A table: campaign, spend, sales, return per $1. A list of keywords to block.

Never:
- Never change Walmart campaigns.
- Never add ad sales to total sales.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: mkt-walmart-sponsored-search-check". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.

Not fully ready yet (ready after we build it): Walmart Connect ad data is not synced. Needs a Walmart advertising connector before spend, keywords or return can be read. Do the parts you can and say plainly what is missing.
