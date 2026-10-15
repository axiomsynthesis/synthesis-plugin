# Items at risk of losing their shelf

Channel: Retail · Level: Advise · Status: Ready after we build it

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Items at risk of losing their shelf" (id: mkt-retail-hurdle-risk, Retail).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Retailers drop items that sell under a set rate per store per week. This shows which items are under it or sliding toward it, before the review.

What to read: Each retail item's units per store per week against the retailer's hurdle rate, its trend, and its store count
What to give me: Items below or sliding toward the sales rate the retailer requires, and weeks until the review

Synthesis tools to use:
- `gsheets_metric metric=tables`
- `gsheets_metric metric=trend`
- `search_files query=hurdle`

Steps:
1. Call `search_files query=hurdle` and `gsheets_metric metric=tables` to find the hurdle rates and weekly item sales.
2. Call `gsheets_metric metric=trend` for units per store per week, by item, for 26 weeks.
3. Compare each item's trailing 13-week rate with its hurdle. Mark under, near (within 15%), or clear.
4. For items under or near, compute the lift needed to clear by the review date.

Checks before answering:
- Velocity is units per store per week. Never use total units; store count changes hide the real rate.
- Check whether shares and rates are fractions or percents in the sheet before comparing. Convert once.
- Sheet figures are typed by people. Say so.
- Never call shelf dollars your revenue.

Output:
- One line: items under hurdle and weeks to review.
- A table: item, rate now, 13-week rate, hurdle, gap, trend, lift needed.

Never:
- Never commit promotion money. That is a business decision.
- Never send this to a buyer without a person's review.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: mkt-retail-hurdle-risk". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.

Not fully ready yet (ready after we build it): No governed tool reads store sales or hurdle rates for customers yet. Needs weekly item sales by store count and the retailer's hurdle connected. Until then it works only if both live in a connected Google Sheet or an uploaded file. Do the parts you can and say plainly what is missing.
