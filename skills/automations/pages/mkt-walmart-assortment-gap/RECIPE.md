# Amazon best sellers missing on Walmart

Channel: Walmart · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Amazon best sellers missing on Walmart" (id: mkt-walmart-assortment-gap, Walmart).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Compares your Amazon best sellers with your Walmart Marketplace catalog. It sizes the gap using your own Walmart-to-Amazon ratio on products listed on both.

What to read: Your top Amazon products by sales, your Walmart Marketplace items and their sales
What to give me: Products that sell well on Amazon but aren't listed or barely sell on Walmart, ranked by the size of the prize

Synthesis tools to use:
- `cost_rules for=mkt-walmart-assortment-gap`
- `amazon_metric metric=pnl_by_asin limit=40`
- `walmart_metric metric=top_skus months=6 limit=50`
- `walmart_metric metric=catalog_health`

Steps:
1. Call `amazon_metric metric=pnl_by_asin limit=40`.
2. Call `walmart_metric metric=top_skus months=6 limit=50` and `walmart_metric metric=catalog_health`.
3. Match by your product code. Ask the person for a mapping if codes differ.
4. Ratio = Walmart sales divided by Amazon sales across products sold on both. Prize per missing product = its Amazon sales times that ratio.

Checks before answering:
- Use the ratio from your own matched products. Never use an industry ratio.
- A product listed but unpublished is not missing. It is a fix, and it belongs in the unpublished list.
- Walmart revenue here is order value, not settlement. Say so.

Output:
- One line: products missing and the likely monthly prize.
- A table: product, Amazon sales per month, on Walmart (no, unpublished, low), estimated Walmart sales.

Never:
- Never create Walmart listings.
- Never present the estimate as a forecast.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Before step 1, call cost_rules. If it returns questions, ask them in one message as written (dollars, choices, what skip does) and save each answer with set_cost_rule. On a scheduled run, use the defaults and list the questions at the end. End the answer with its used_line.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: mkt-walmart-assortment-gap". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
