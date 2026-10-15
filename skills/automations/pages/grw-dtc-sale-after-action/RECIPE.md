# Did the website sale make money?

Channel: Growth · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Did the website sale make money?" (id: grw-dtc-sale-after-action, Growth).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
A sitewide sale always looks good in the week it runs. This compares the sale with the weeks before and the weeks after, to find what it truly added once the dip and the discount are counted.

What to read: Daily website sales, orders and new customers around a sale
What to give me: What the sale really added after the dip that follows it

Synthesis tools to use:
- `shopify_metric metric=daily_revenue start_date=<YYYY-MM-DD> end_date=<YYYY-MM-DD>`
- `shopify_metric metric=new_vs_returning_orders months=12`
- `klaviyo_metric metric=campaign_scorecard limit=20`

Steps:
1. Ask for the sale dates and discount.
2. Pull `shopify_metric metric=daily_revenue` from 28 days before to 28 days after.
3. Baseline = average of the 4 weeks before, same weekdays.
4. Lift = sale days over baseline, minus any shortfall in the 4 weeks after.
5. Pull `shopify_metric metric=new_vs_returning_orders months=12`, enough months back to reach the sale month, and `klaviyo_metric metric=campaign_scorecard limit=20` to see who bought and which sends drove it.
6. Net the discount dollars the person gave in step 1. No tool here returns them. If they are not known, say the net is before discount.

Checks before answering:
- If the after-window is under 14 days old, say the dip is not measured yet.
- Days are UTC. Say so if the sale ran on local time.
- Another event in the window spoils the baseline. Ask.

Output:
- Answer first: net added sales after the dip and discount. Table: baseline, sale, after, net, new customers.

Never:
- Nothing changes in any live account. A person on your team makes every change.
- Never fill a missing, gated or empty number with an estimate. Say what is missing and why.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: grw-dtc-sale-after-action". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
