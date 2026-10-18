# Where Google ads pay, region by region

Channel: Google · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Where Google ads pay, region by region" (id: grw-google-geo-efficiency, Google).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Shows where your Google spend lands and what each region returns. It sets that beside where website revenue already comes from, so you stop paying for regions that do not buy.

What to read: Google Ads spend and return by region, and website revenue by state
What to give me: Regions to bid up and regions to cut, next to where your website sales already come from

Synthesis tools to use:
- `google_ads_metric metric=geo days=30 limit=50`
- `shopify_metric metric=state_revenue`

Steps:
1. Pull `google_ads_metric metric=geo days=30 limit=50`.
2. Pull `shopify_metric metric=state_revenue`.
3. Flag regions with at least $200 spend and return under half the account.
4. Flag strong revenue states with little Google spend.

Checks before answering:
- Google Ads data for this view holds at most 90 days. Only campaign spend totals are kept longer. A short history is the age of the connection, not a business fact. Never compare year over year here.
- Google Ads cost is click cost from the API, not the invoice. Say so beside any total.
- Rows under $200 spend are listed, not judged.

Output:
- Answer first. Table with columns region, spend, return, share of website revenue, move.

Never:
- Nothing changes in any live account. A person on your team makes every change.
- Never fill a missing, gated or empty number with an estimate. Say what is missing and why.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: grw-google-geo-efficiency". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
