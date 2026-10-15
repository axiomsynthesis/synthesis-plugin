# Don't cut ads that sell your other products

Channel: Amazon · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Don't cut ads that sell your other products" (id: mkt-amazon-ad-halo-credit, Amazon).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
A shopper clicks an ad for one product and buys another. A strict per-product ad cost hides that.
This shows, for each advertised product, how much of what it sold was something else.

What to read: Which product each ad promoted against which product the shopper actually bought
What to give me: Ads whose real value is the other products they sell, so you don't kill one that only looks bad on its own

Synthesis tools to use:
- `amazon_metric metric=ppc_halo days=60 limit=40`
- `amazon_metric metric=ppc_spend_by_parent days=60 limit=30`

Steps:
1. Call `amazon_metric metric=ppc_halo days=60 limit=40`. Each row pairs the advertised product with the purchased product.
2. For each advertised product, split sales into same product, same family other size, and other products.
3. Call `amazon_metric metric=ppc_spend_by_parent days=60 limit=30` to show the family-level ad cost next to it.
4. Flag ads that look unprofitable alone but profitable with halo, and the reverse.

Checks before answering:
- Sponsored Brands rows have no single advertised product. They are grouped as unattributed. Leave them out of per-product reads.
- Halo sales to a different size of the same family are the same decision. Group them at family level before calling it halo.
- If halo totals exceed ad-credited sales, something is double counted. Stop and say so.

Output:
- One line: the ad most undervalued by its own number, with both returns.
- A table: advertised product, ad spend, own-product sales, other-product sales, return alone, return with halo.

Never:
- Never pause an ad on its own return without checking halo.
- Never change anything in the account.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: mkt-amazon-ad-halo-credit". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
