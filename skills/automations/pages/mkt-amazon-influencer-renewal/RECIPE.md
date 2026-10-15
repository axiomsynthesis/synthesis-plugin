# Which outside partners to renew or drop

Channel: Amazon · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Which outside partners to renew or drop" (id: mkt-amazon-influencer-renewal, Amazon).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Ranks each outside source you send to Amazon by the sales it produced. This is the grain at which a partner is renewed or dropped.

What to read: Clicks, detail page views, carts and Amazon sales for each tracked outside link, by partner and placement
What to give me: A renew, renegotiate or drop call for each influencer, affiliate or placement sending shoppers to Amazon, ranked by sales

Synthesis tools to use:
- `amazon_metric metric=attribution_sources days=90 limit=50`
- `amazon_metric metric=attribution_publishers days=90`
- `amazon_metric metric=attribution_trueup weeks=4`

Steps:
1. Call `amazon_metric metric=attribution_sources days=90 limit=50`.
2. Call `amazon_metric metric=attribution_publishers days=90` for totals by platform.
3. Call `amazon_metric metric=attribution_trueup weeks=4`. Recent weeks are still collecting sales. Say how much they typically grow.
4. Ask the person what they pay each partner. The data has no cost side. Then compute sales per dollar paid.

Checks before answering:
- Outside-link sales keep landing for 14 days. Never judge a partner on the last two weeks.
- Without the fee paid, never call a partner profitable or unprofitable. Rank by sales only.
- Clicks with zero detail page views usually mean a broken link. Flag them.

Output:
- One line: the top partners and the ones to drop.
- A table: partner, placement, clicks, detail page views, orders, sales, conversion, fee paid if given, sales per $1.

Never:
- Never contact partners.
- Never invent what a partner is paid.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: mkt-amazon-influencer-renewal". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
