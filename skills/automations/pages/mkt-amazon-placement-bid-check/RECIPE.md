# Is top-of-search worth the extra cost?

Channel: Amazon · Level: Prepare · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Is top-of-search worth the extra cost?" (id: mkt-amazon-placement-bid-check, Amazon).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Amazon lets you pay more to show at the top of search. This checks whether that premium pays back, placement by placement.
It ends with a short list of multiplier changes for a person to make in the ads console.

What to read: Sponsored Products results by placement, top of search against product pages and the rest of search
What to give me: Whether top-of-search earns its higher click price, and the placement changes to make by hand

Synthesis tools to use:
- `amazon_metric metric=ppc_placements days=60`
- `amazon_metric metric=ppc_purchase_latency days=60 limit=10`
- `amazon_metric metric=ppc_campaigns days=60 ad_product=SP limit=25`

Steps:
1. Call `amazon_metric metric=ppc_purchase_latency days=60 limit=10` to learn how many days sales keep landing after a click. Use that as the minimum age of the window you judge.
2. Call `amazon_metric metric=ppc_placements` with `start_date` and `end_date` covering 60 days that ended at least that many days ago.
3. For each placement, compute cost per click, conversion rate and sales per dollar of spend. Compare top of search against product pages and rest of search.
4. Call `amazon_metric metric=ppc_campaigns days=60 ad_product=SP limit=25` and pick the campaigns with the most spend. Only those are worth a multiplier change.
5. Draft the change list: campaign, current multiplier if known, suggested multiplier, and the reason in one line.

Checks before answering:
- Placement data is Sponsored Products only. Sponsored Brands and Display show as "ALL". Never mix them in.
- A placement with under 100 clicks in the window is too thin to judge. Say so instead of ranking it.
- If the window ends inside the purchase-latency period, the newest days look worse than they are. Re-run on a mature window.
- Placement spend should roughly equal Sponsored Products spend for the same window. If it is far off, stop and say the data looks incomplete.

Output:
- One line: does top of search earn its premium, yes or no, with the return per dollar for each placement.
- A table: placement, spend, clicks, cost per click, conversion rate, sales per $1.
- A change list of at most 5 campaigns: campaign, suggested multiplier, why.
- One line on how we will know: the number to recheck and the date.

Never:
- Never change bids or multipliers in the account. A person makes the change.
- Never judge a window that has not finished collecting sales.
- Never average branded and non-branded campaigns into one verdict.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: mkt-amazon-placement-bid-check". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
