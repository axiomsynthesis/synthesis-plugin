# How fast does a new customer pay back?

Channel: Customers · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "How fast does a new customer pay back?" (id: grw-cac-payback, Customers).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Divides ad spend that sends shoppers to the website by the new website customers it won, over the same three closed months. It then follows earlier customers to see how many months their profit, after product cost, shipping and card fees, takes to pay that cost back.

What to read: Ad spend that sends shoppers to the website, new website customers and their cumulative value by acquisition month
What to give me: Months to earn back a new website customer's cost from profit after product cost, shipping and fees

Synthesis tools to use:
- `cost_rules for=grw-cac-payback`
- `meta_metric metric=weekly_trend weeks=13`
- `meta_metric metric=ad_destinations days=90`
- `google_ads_metric metric=efficiency_trend weeks=13`
- `tiktok_metric metric=spend_trend months=4`
- `new_customers_dtc month=<YYYY-MM>`
- `shopify_metric metric=cohort_ltv_censor_safe`
- `shopify_metric metric=profit month=YYYY-MM`
- `first_order_contribution_margin`

Steps:
1. Use the last three closed calendar months for every spend and customer count.
2. Call `meta_metric metric=weekly_trend weeks=13`. Add the spend of weeks that start inside the three months, minus each week's `amazon_bound_spend`. Then call `meta_metric metric=ad_destinations days=90` only to split the rest into website, Walmart and no known destination. Top ads only.
3. Call `google_ads_metric metric=efficiency_trend weeks=13`. Same weeks, minus each week's `amazon_bound_spend`.
4. Call `tiktok_metric metric=spend_trend months=4`. Keep `auction_spend` for the three months as a destination unknown line. Leave shop ad spend out. It sells inside TikTok Shop.
5. Call `new_customers_dtc` for each of the three months and add them.
6. Cost per new customer = website spend over new customers. Low figure: known website spend only. High figure: add no known destination and TikTok auction spend.
7. Call `shopify_metric metric=profit` for the latest month. From `column`: product cost share of sales, card fee share of sales, shipping per order (shipping line over `orders`) and average order value (sales over `orders`).
8. Call `shopify_metric metric=cohort_ltv_censor_safe` for cumulative sales per customer by acquisition month. Orders per customer = that over average order value, an estimate.
9. Profit per customer = cumulative sales times (1 minus product cost share minus card fee share), minus orders per customer times shipping per order. Payback month = first month it passes the cost. Never use a gross margin alone.
10. Call `first_order_contribution_margin` with `price=` the average order value, `cogs=`, `misc=` the shipping per order and `cac=` the cost per new customer.

Checks before answering:
- If a customer tool returns gated, do not state the number. Give its refusal reason.
- Weeks do not match months to the day. Say so.
- Young cohorts are unfinished. Leave immature cells blank, never read them as low.
- New means first website order. A long-time Amazon buyer counts as new, so cost per new customer reads low. Say so.
- Never add Amazon-bound or TikTok Shop spend to the website cost. Say how much was left out.
- Use website cohorts only. Brand-wide cohort tables are built from Amazon orders.
- Costs the profit column marks not connected make payback read fast. Name them.
- Email and retention spend on repeat orders is not taken off yet, so payback reads a little fast.

Output:
- Answer first: does a new website customer pay back, and in how many months? Cost per new customer as low and high. If no cohort pays back within 12 months, say so plainly.
- Table: spend by source counted and left out, new customers, cost each.
- Table by acquisition month: profit per customer at month 1, 3, 6 and 12, payback month.
- One line: whether the first order alone covers its cost.

Never:
- Nothing changes in any live account. A person on your team makes every change.
- Never fill a missing, gated or empty number with an estimate. Say what is missing and why.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Before step 1, call cost_rules. If it returns questions, ask them in one message as written (dollars, choices, what skip does) and save each answer with set_cost_rule. On a scheduled run, use the defaults and list the questions at the end. End the answer with its used_line.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: grw-cac-payback". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
