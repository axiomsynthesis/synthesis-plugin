---
description: "How fast does a new customer pay back?: Months to earn back the cost of a new website customer, set against how each month's customers have spent since"
argument-hint: "[anything to add for this run]"
disable-model-invocation: true
---

# How fast does a new customer pay back?

Channel: Customers · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "How fast does a new customer pay back?" (id: grw-cac-payback, Customers).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Divides the ad spend that sends shoppers to the website by the new website customers it won, for one cost per new customer over the last 90 days. It then follows earlier months' customers to see how many months their spending takes to pay that cost back after product cost.

What to read: Ad spend that sends shoppers to the website, new website customers and their cumulative value by acquisition month
What to give me: Months to earn back the cost of a new website customer, set against how each month's customers have spent since

Synthesis tools to use:
- `cost_rules for=grw-cac-payback`
- `meta_metric metric=ad_destinations days=90`
- `google_ads_metric metric=efficiency_trend weeks=13`
- `tiktok_metric metric=spend_trend months=4`
- `new_customers_dtc month=<YYYY-MM>`
- `shopify_metric metric=cohort_ltv_censor_safe`

Steps:
1. Call `meta_metric metric=ad_destinations days=90` for Meta spend split by where each ad sends people. Count only spend pointing at the website. Spend pointing at Amazon is not a website cost. Show spend with no known destination on its own line.
2. Call `google_ads_metric metric=efficiency_trend weeks=13` and add the 13 full weeks.
3. Call `tiktok_metric metric=spend_trend months=4` and count only `auction_spend` for the months in the window. Shop ad spend sells inside TikTok Shop, not on the website, so leave it out.
4. Call `new_customers_dtc` for each of the last three closed months and add them.
5. Cost per new website customer = website spend over new website customers. Give a low figure with known website spend only, and a high figure that adds the spend with no known destination.
6. Call `shopify_metric metric=cohort_ltv_censor_safe` for cumulative website value per customer by acquisition month.
7. Ask for gross margin if unknown. Payback month = first month where a cohort's value times margin passes the cost.

Checks before answering:
- If a customer tool returns gated, do not state the number. Give its refusal reason.
- The spend window is the last 90 days and the customer count is the last three closed months. Say they overlap but do not match to the day.
- Young cohorts are unfinished. Leave immature cells blank and never read them as low.
- Shopify new means first website order, not first purchase from the brand anywhere. Say so.
- Never add spend that points at Amazon or sells inside TikTok Shop to the website cost. Say how much was left out and why.
- Google and TikTok auction spend carry no destination in these reads. They are counted as website spend. Say so, because any of it that points at Amazon makes the cost read high.
- Never use Google Ads history past 90 days. It does not exist.
- Use website cohorts only. The brand-wide cohort tables are built from Amazon orders and must not be mixed in.

Output:
- Answer first: cost per new website customer as a low and high figure, and payback in months.
- Table: spend by source counted and left out, new customers, cost each.
- Table by acquisition month: value at month 1, 3, 6 and 12, payback month.

Never:
- Nothing changes in any live account. A person on your team makes every change.
- Never fill a missing, gated or empty number with an estimate. Say what is missing and why.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Before step 1, call cost_rules. If it returns questions, ask them in one message as written (dollars, choices, what skip does) and save each answer with set_cost_rule. On a scheduled run, use the defaults and list the questions at the end. End the answer with its used_line.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: grw-cac-payback". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.

---

Anything the person typed after the shortcut is extra instruction for this run: $ARGUMENTS
