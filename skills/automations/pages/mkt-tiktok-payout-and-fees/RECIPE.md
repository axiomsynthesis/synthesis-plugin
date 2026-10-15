# What TikTok keeps from each sale

Channel: TikTok Shop · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "What TikTok keeps from each sale" (id: mkt-tiktok-payout-and-fees, TikTok Shop).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Shows what TikTok keeps before it pays you: fees, shipping and adjustments, month by month.

What to read: TikTok Shop statements by month, paid and unpaid, with fees, shipping cost and adjustments by type
What to give me: TikTok's fee, shipping and payout rates by month, what's still unpaid, and any fee that jumped

Synthesis tools to use:
- `tiktok_metric metric=shop_payouts months=6`

Steps:
1. Call `tiktok_metric metric=shop_payouts months=6`.
2. Read fee, shipping and payout rates against settlement revenue for each month.
3. Read the fee breakdown by type. Flag any type that moved more than 2 points.
4. Report the unpaid amount separately.

Checks before answering:
- Rates are against settlement revenue, which includes shipping paid by buyers and platform subsidies. Never divide fees by order sales.
- A settlement month is not the same set of orders as a sales month.
- Reserve holds are excluded. They are your money held, not a fee.
- If the tool flags that statement totals do not tie to their lines, say so first.

Output:
- Three lines: paid out, unpaid, payout rate.
- A table: month, settlement revenue, fee rate, shipping rate, payout rate.

Never:
- Never call order sales the payout.
- Never count reserve holds as costs.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: mkt-tiktok-payout-and-fees". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
