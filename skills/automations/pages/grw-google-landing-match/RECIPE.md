# Send Google clicks to the right page

Channel: Google · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Send Google clicks to the right page" (id: grw-google-landing-match, Google).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Matches every page your Google ads send people to with how that page behaves for all visitors. A page that converts far worse than your best page is a quick fix with no extra spend.

What to read: Google Ads landing pages and the same pages' site behaviour
What to give me: Paid pages that waste clicks, and the better page to send them to

Synthesis tools to use:
- `google_ads_metric metric=landing_pages days=30 limit=30`
- `ga4_metric metric=landing_pages days=30 limit=50`

Steps:
1. Pull `google_ads_metric metric=landing_pages days=30 limit=30`.
2. Pull `ga4_metric metric=landing_pages days=30 limit=50`.
3. Match on the page path with tracking tags stripped.
4. Flag paid pages with conversion rate under half the best paid page and more than $300 spend.
5. Suggest the better page for each flagged one, from pages with the same product and higher conversion.

Checks before answering:
- Google Ads campaign and keyword data holds at most 90 days. A short history is the age of the connection, not a business fact. Never compare year over year here.
- GA4 is behaviour only. Never quote its revenue as sales; sales come from the order data.
- Report how many paid pages matched a GA4 page. If under half matched, say the join is weak and stop before advising.

Output:
- Answer first. Table with columns paid page, spend, conversion rate, better page, its conversion rate.

Never:
- Nothing changes in any live account. A person on your team makes every change.
- Never fill a missing, gated or empty number with an estimate. Say what is missing and why.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: grw-google-landing-match". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
