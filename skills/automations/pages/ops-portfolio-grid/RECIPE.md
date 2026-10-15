# Stars, cash cows and weak spots in your range

Channel: Strategy · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Stars, cash cows and weak spots in your range" (id: ops-portfolio-grid, Strategy).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Places each product range on a grid of share against growth, then adds the cash each range makes or uses. It shows which ranges fund the others and which consume cash without a clear path.

What to read: Share and growth for each product range
What to give me: Each range placed as a star, cash generator, question mark or weak spot, with the cash each makes or needs

Synthesis tools to use:
- `netsuite_metric metric=family_revenue months=12 limit=10`
- `product_family_pnl`
- `amazon_metric metric=contribution_by_asin months=6`
- `estimate_market_share signals=[...]`
- `strategy_framework framework=bcg_matrix`

Steps:
1. Call `netsuite_metric metric=family_revenue months=12 limit=10` and `product_family_pnl` for revenue and growth by range across channels.
2. Call `amazon_metric metric=contribution_by_asin months=6` and roll products to ranges for profit on Amazon.
3. For share, use category share where held, or run `estimate_market_share signals=[...]` from search and revenue signals. Otherwise use share of your own revenue and say so.
4. Run `strategy_framework framework=bcg_matrix skus=[{name, share, growth}] share_threshold=<cut> growth_threshold=<cut>` with one entry per range, passing explicit thresholds.
5. Add monthly profit or loss per range.

Checks before answering:
- Range revenue from the books includes non-product lines such as shipping income. Drop them.
- A range of one product is not a range.
- Share of your own revenue is not market share. Label it.
- Group ranges from the curated range list, never from product names.

Output:
- Table: Range | Share | Growth | Monthly profit | Place on grid.
- Two lines: which range funds the rest, and the question mark to decide on.

Never:
- Never discontinue or launch anything.
- Never infer ranges from product names.
- Never use the grid's default median thresholds without saying so.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: ops-portfolio-grid". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
