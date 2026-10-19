# Keep my Meta to Amazon ads sheet up to date

Channel: Meta · Level: On a schedule · Status: Ready now
Schedule: every weekday 7am

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Keep my Meta to Amazon ads sheet up to date" (id: meta-amazon-ads-sheet, Meta).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Fills your Meta to Amazon ads sheet: tabs for last week, the month so far, all time, and raw data with one row per ad per week. Each tab is broken out by product. Every ad shows spend, Amazon sales, ROAS, orders, clicks, cost per click, conversion rate and a link to watch it. Last week's tab also lists the top ads, new possible winners and ads dropping fast.

What to read: Meta ad spend, Amazon Attribution sales, your ad link tracker or your own ad links
What to give me: Weekly, month to date, all time and raw data tabs, broken out by product, for every Meta ad that sends shoppers to Amazon, each with a link to watch the ad

Synthesis tools to use:
- `meta_metric metric=amazon_ads period=week`
- `meta_metric metric=amazon_ads period=mtd`
- `meta_metric metric=amazon_ads period=all`
- `meta_metric metric=amazon_ads period=weekly`
- `export_xlsx`

Steps:
1. First run only, before any numbers: ask for the link to the Google Sheet to fill. Check this Claude has a Google Sheets or Drive tool that can edit. If not, tell them to add a Google Sheets or Drive connector that can edit in their Claude's connector settings, sign in with the Google account that can edit that sheet, then run this again in a new chat; offer the file from step 6 for today. If it can, open the sheet once, list its tabs, and confirm the four tab names. Ask before replacing a tab with one of those names, and never touch the team's own tabs. Remember the link and answers, and skip this step later.
2. Call `meta_metric` with `metric=amazon_ads` and `period=week` for last week's rows, the by-product totals and the three picks.
3. Call `meta_metric` with `metric=amazon_ads` and `period=mtd` for the month so far.
4. Call `meta_metric` with `metric=amazon_ads` and `period=all` for all time.
5. Call `meta_metric` with `metric=amazon_ads` and `period=weekly` and `weeks=8` for the raw data, one block per week.
6. Build tabs Weekly, Month to date, All time and Raw data. Ad columns: Ad, Spend, Amazon sales, ROAS, Orders, Amazon clicks, Meta clicks, CPC Amazon, CPC Meta, CVR, First ran, Watch as a clickable link. Each of the first three tabs opens with its dates, headline totals and settling note. Weekly then has Top ads, New potential winners and Dropping fast, each with ROAS last week and Product. Then on all three: a By product table from `by_product`, one row per product plus Total, then each product under its own heading with its ads and a subtotal row. Raw data is one row per ad per week: Week start, Week end, Product, then the ad columns, with a filter on the header. Write into the sheet if this Claude can edit it, leaving every other tab alone. Otherwise use `export_xlsx` with `filename=meta-amazon-ads.xlsx`.

Checks before answering:
- If a result says unavailable, say why in one line and stop. Never fill a tab with zeros.
- If it says no_linked_ads, give its reason and action in one line and stop. If error, say it is not a zero.
- If the sheet cannot be opened or edited, say so and hand back the file. Never call the sheet updated unless the write returned no error.
- When a result says it has not settled, put its settling note above that tab. Amazon keeps crediting orders for 14 days after a click, so recent weeks will still rise.
- Ads that share one Amazon link are one row. Never split their sales between them.
- Ads with no product label go under Product not identified. Spend on ads with no Amazon link is its own line, so product totals add up to the headline.
- If linked spend is under 80%, say so first.

Output:
- One line first: last week's spend, Amazon sales, ROAS and orders, and the change from the week before.
- Then the top ads, new possible winners and ads dropping fast, with ROAS, product and watch link.
- Then where the tabs went, the sheet link or the file. On the first run, say what was set up and what is missing.

Never:
- Never change, pause or launch an ad.
- Never edit a tab other than the four this fills, and never delete a row a person added.
- Never compare a week that has not settled as if it were final.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: meta-amazon-ads-sheet". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
- This is meant to repeat (every weekday 7am). Run it once now. If you can set up a repeating task here, do it. If not, tell me how to run this again each time it is due.
