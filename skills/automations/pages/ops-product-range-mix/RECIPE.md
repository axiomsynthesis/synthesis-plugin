# Is your product mix moving the right way?

Channel: Strategy · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Is your product mix moving the right way?" (id: ops-product-range-mix, Strategy).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Shows how the company's revenue is shifting between product ranges across every channel, and what that shift does to profit. A business can grow revenue while its mix quietly moves toward lower-margin ranges.

What to read: Revenue by product range from the books across Amazon, retail, wholesale and the website
What to give me: How each range's share of company revenue is shifting, and whether the mix is heading to higher or lower margin

Synthesis tools to use:
- `netsuite_metric metric=family_revenue months=12 limit=10`
- `product_family_pnl`
- `amazon_metric metric=contribution_by_asin months=6`

Steps:
1. Call `netsuite_metric metric=family_revenue months=12 limit=10` for revenue and share by range.
2. Call `product_family_pnl` for the latest month's range revenue and change.
3. Call `amazon_metric metric=contribution_by_asin months=6` and roll products to ranges for profit share on Amazon.
4. Compare each range's share now with a year ago.
5. Estimate the profit effect of the shift using Amazon margins per range, and say that retail margins may differ.

Checks before answering:
- Range figures from the books include non-product lines (shipping income, marketplace credits). Leave them out.
- A range year-over-year is only valid when both months are closed. A blank means not closed, not no change.
- Never size an Amazon-only move against all-channel range revenue.
- If the ledger is not connected, run on Amazon and website only and say so.

Output:
- Table: Range | Share a year ago | Share now | Change | Margin on Amazon.
- Two lines: the shift in one sentence and its profit effect.

Never:
- Never infer ranges from product names; use the curated range list.
- Never mix ledger ranges with a differently curated Amazon range list without saying so.
- Never change any product plan.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: ops-product-range-mix". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
