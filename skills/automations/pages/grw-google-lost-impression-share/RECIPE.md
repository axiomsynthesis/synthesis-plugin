# Google searches you're missing out on

Channel: Google · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Google searches you're missing out on" (id: grw-google-lost-impression-share, Google).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Shows, per campaign, how often your ads did not show because the budget ran out versus because your bid or quality was too low. Budget-limited campaigns with good returns are the cheapest growth you have.

What to read: Google Ads impression share lost to budget and to rank, by campaign
What to give me: Where a bigger budget would buy more sales, and where it would only buy worse spots

Synthesis tools to use:
- `google_ads_metric metric=impression_share days=30 limit=25`
- `google_ads_metric metric=campaign_performance days=30 limit=25`

Steps:
1. Pull `google_ads_metric metric=impression_share days=30 limit=25`.
2. Pull `google_ads_metric metric=campaign_performance days=30 limit=25` for spend, conversions and conversion value.
3. Flag campaigns losing more than 20% to budget with a return above the account average. These get a budget raise.
4. Flag campaigns losing more than 30% to rank. These need better ads or landing pages, not more money.
5. For each budget-limited winner, size a raise as a share of current budget, capped at 30% per step.

Checks before answering:
- Google Ads data for this view holds at most 90 days. Only campaign spend totals are kept longer. A short history is the age of the connection, not a business fact. Never compare year over year here.
- Google Ads cost is click cost from the API, not the invoice. Say so beside any total.
- Impression share is missing for some campaign types such as Performance Max. List those as not measured, never as zero.
- Use the same 30 days for both pulls.

Output:
- Answer first. Table with columns campaign, spend, return, lost to budget, lost to rank, verdict, move.
- Under 12 rows.

Never:
- Nothing changes in any live account. A person on your team makes every change.
- Never fill a missing, gated or empty number with an estimate. Say what is missing and why.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: grw-google-lost-impression-share". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
