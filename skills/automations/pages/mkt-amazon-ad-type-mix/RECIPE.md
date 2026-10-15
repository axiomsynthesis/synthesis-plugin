# Which Amazon ad type earns the most?

Channel: Amazon · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Which Amazon ad type earns the most?" (id: mkt-amazon-ad-type-mix, Amazon).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Most accounts drift into spending almost everything on one ad type. This shows the split, what each type returns, and whether the mix should change.

What to read: Spend, sales, new-to-brand share and trend for Sponsored Products, Sponsored Brands and Sponsored Display
What to give me: How your ad money splits across the three ad types, which earns best, and the split to aim for

Synthesis tools to use:
- `amazon_metric metric=ppc_campaigns days=90 limit=100`
- `amazon_metric metric=ppc_ntb days=90`
- `amazon_metric metric=ppc_trend weeks=12`
- `amazon_metric metric=tacos`

Steps:
1. Call `amazon_metric metric=ppc_campaigns days=90 limit=100`. Sum spend and sales by ad type (SP, SB, SD).
2. Call `amazon_metric metric=ppc_ntb days=90` for new-to-brand share on Sponsored Brands and Display.
3. Call `amazon_metric metric=ppc_trend weeks=12` to see whether Sponsored Products efficiency is rising or falling.
4. Call `amazon_metric metric=tacos month=<last closed month>` so the mix is read against total Amazon sales, not just ad sales.
5. Suggest one move between types, in dollars a month.

Checks before answering:
- Each ad type counts a sale differently. Sponsored Brands and Display include view-through and brand-halo sales. Say this before comparing returns.
- If one ad type shows zero spend, check whether the account simply does not run it, or the sync is missing it.
- New-to-brand share does not exist for Sponsored Products. Never print a value for it.
- Use a closed month for the total-sales ratio.

Output:
- One line: the split today and the one move.
- A table: ad type, spend, share of spend, sales, return per $1, new-to-brand share where it exists, 12-week direction.

Never:
- Never move budget between ad types in the account.
- Never call one ad type "best" on return alone without the counting caveat.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: mkt-amazon-ad-type-mix". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
