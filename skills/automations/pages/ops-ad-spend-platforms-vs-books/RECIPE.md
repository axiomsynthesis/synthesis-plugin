# Ad spend: platforms vs your books

Channel: Money · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Ad spend: platforms vs your books" (id: ops-ad-spend-platforms-vs-books, Money).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Ties the ad spend the platforms report to the marketing cost in the books. Agency fees, creator payments, timing of bills and missed accounts all open a gap, and a gap that nobody explains is how money leaks or gets double counted in a margin model.

What to read: Ad spend reported by each ad platform and marketing cost booked in the accounting ledger
What to give me: Month by month, what the ad platforms say you spent against your books, and the gap explained

Synthesis tools to use:
- `meta_metric metric=spend month=YYYY-MM`
- `amazon_metric metric=ad_spend days=180`
- `google_ads_metric metric=efficiency_trend weeks=26`
- `tiktok_metric metric=spend_trend months=6`
- `netsuite_metric metric=opex_category months=6 limit=20`

Steps:
1. Pull platform spend by month: `meta_metric metric=spend month=YYYY-MM` for each of the six months, `amazon_metric metric=ad_spend days=180`, `google_ads_metric metric=efficiency_trend weeks=26`, and `tiktok_metric metric=spend_trend months=6` for each connected platform.
2. Call `netsuite_metric metric=opex_category months=6 limit=20` and request single months (`months=1`) for the month you are reconciling, to get marketing cost by category.
3. For each closed month, sum platform spend and compare with booked marketing.
4. Explain the gap with what can be named: agency fees, creator payments, billing timing (a platform bills after the month it ran), and channels not connected.
5. Report what remains as unexplained.

Checks before answering:
- Platform spend is by day of delivery; bills land later. A one-month timing shift explains a lot. Check the neighbouring month before calling anything missing.
- Booked marketing often includes non-ad items. Never assume it is all media.
- A platform with no data for a month is not zero spend. Say "not connected" or "missing".
- If the brand has no ledger connected, say so and stop.

Output:
- Table: Month | Platform spend by platform | Total platforms | Booked marketing | Gap | Explained | Unexplained.
- One line naming the biggest unexplained amount and the question to ask finance.

Never:
- Never add platform spend and booked marketing together.
- Never conclude fraud or overbilling from a gap. Ask for the bills.
- Never change anything in an ad account or the ledger.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: ops-ad-spend-platforms-vs-books". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
