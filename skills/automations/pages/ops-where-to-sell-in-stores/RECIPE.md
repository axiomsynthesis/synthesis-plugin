# Where to start selling in stores

Channel: Growth · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Where to start selling in stores" (id: ops-where-to-sell-in-stores, Growth).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Uses where online buyers already are to pick where a store launch is most likely to work. A retailer buyer cares about proof of demand in their region, and online sales by state are the cheapest proof a brand has.

What to read: Amazon and website buyers by state, revenue per head of population, and repeat rates by region
What to give me: The regions where online demand is strongest, as the shortlist to pitch retailers

Synthesis tools to use:
- `amazon_metric metric=geo_penetration`
- `shopify_metric metric=state_revenue`
- `geo_performance`

Steps:
1. Call `amazon_metric metric=geo_penetration` for Amazon revenue and customers by state.
2. Call `shopify_metric metric=state_revenue` for website revenue by state.
3. Call `geo_performance` for combined region reads.
4. Compute buyers per 100,000 people per state against the national rate. Use population figures the person accepts, with source.
5. Rank states and group them into retailer regions.

Checks before answering:
- Big states lead on totals by size alone. Rank on buyers per head.
- Small states with few buyers swing a lot. Require at least 200 buyers before ranking.
- Amazon state data reflects ship-to address, not where people shop in stores. Say so.

Output:
- Table: State or region | Buyers | Buyers per 100,000 | Index vs national | Repeat rate.
- Two lines: the region to lead with and the evidence to show a buyer.

Never:
- Never share customer-level location data. Totals by state only.
- Never contact a retailer.
- Never present online demand as guaranteed store sales.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: ops-where-to-sell-in-stores". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
