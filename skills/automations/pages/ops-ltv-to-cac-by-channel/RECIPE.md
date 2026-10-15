# Customer value vs cost to win, by channel

Channel: Money · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Customer value vs cost to win, by channel" (id: ops-ltv-to-cac-by-channel, Money).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Compares what a customer is worth with what it costs to win one, for each channel that brings customers in. It is the check a board or investor asks for first, built from mature cohorts only so young customers do not drag the value down.

What to read: Mature-cohort customer value, Amazon new-to-brand cost, Meta cost per purchase and website new customers
What to give me: For each channel, what a customer is worth against what it costs to win one

Synthesis tools to use:
- `brand_ltv`
- `shopify_metric metric=cohort_ltv_censor_safe`
- `amazon_metric metric=ppc_ntb`
- `meta_metric metric=cpa month=YYYY-MM`
- `google_ads_metric metric=campaign_performance days=90 limit=20`

Steps:
1. Call `brand_ltv` for value per customer across mature cohorts on Amazon.
2. Call `shopify_metric metric=cohort_ltv_censor_safe` for website customer value by cohort.
3. Convert value to profit with each channel's margin before ads.
4. Cost to win: `amazon_metric metric=ppc_ntb` for Amazon ads, `meta_metric metric=cpa month=YYYY-MM` for each of the last three months for Meta, `google_ads_metric metric=campaign_performance days=90 limit=20` for Google.
5. Ratio = profit value divided by cost to win. Show the 12-month window and say so.

Checks before answering:
- Only mature cohorts count. A cohort younger than the value window is not finished.
- Platform cost per purchase counts platform-credited buyers. It is not incremental. Say so.
- Revenue value is not profit value. Convert, and say which margin was used.
- A channel with no cost data cannot have a ratio. Show it as not measurable.

Output:
- Table: Channel | Profit per customer (12 months) | Cost to win | Ratio | Customers in the cohorts used.
- Two lines: the strongest channel and the weakest, in dollars.

Never:
- Never use repeat rate as value.
- Never present a revenue-based ratio as a profit ratio.
- Never change budgets.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: ops-ltv-to-cac-by-channel". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
