# Is all your marketing paying, together?

Channel: Growth · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Is all your marketing paying, together?" (id: grw-blended-mer-trend, Growth).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Ignores what each platform claims and asks one question: for every dollar of ads, how many dollars of total sales came in. It tracks that month by month with marketing as a share of sales.

What to read: Total sales and total ad spend by month across Meta, Google, TikTok and Amazon ads
What to give me: Your whole-business return on ad spend by month, and marketing as a share of sales

Synthesis tools to use:
- `cost_rules for=grw-blended-mer-trend`
- `mer month=<YYYY-MM>`
- `meta_metric metric=spend month=<YYYY-MM>`
- `tiktok_metric metric=spend_trend months=12`
- `google_ads_metric metric=efficiency_trend weeks=13`
- `amazon_metric metric=ad_spend_monthly months=12`

Steps:
1. For each of the last 12 closed months, run `mer`.
2. Pull spend by channel: `meta_metric metric=spend`, `tiktok_metric metric=spend_trend months=12` (auction plus shop ads), `amazon_metric metric=ad_spend_monthly months=12` for Amazon ad spend by month across all three ad types, and Google from `google_ads_metric metric=efficiency_trend weeks=13` summed into months.
3. Show spend mix by channel beside the efficiency number.

Checks before answering:
- If `mer` is gated for a month, do not state it. Give its reason.
- Count TikTok spend from both auction and shop ads.
- Google Ads holds about 90 days. Months before that show Google as not measured, never zero, and their total spend is labelled as excluding Google.
- Leave the current month out.
- Amazon ad spend counts Sponsored Products, Brands and Display. A month before the brand's Amazon ad history begins shows Amazon ads as not measured, never zero.

Output:
- Answer first. Table by month: total sales, total ad spend, efficiency, marketing share of sales, spend mix.

Never:
- Nothing changes in any live account. A person on your team makes every change.
- Never fill a missing, gated or empty number with an estimate. Say what is missing and why.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Before step 1, call cost_rules. If it returns questions, ask them in one message as written (dollars, choices, what skip does) and save each answer with set_cost_rule. On a scheduled run, use the defaults and list the questions at the end. End the answer with its used_line.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: grw-blended-mer-trend". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
