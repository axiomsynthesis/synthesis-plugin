# Stop paying for Google clicks you get free

Channel: Google · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Stop paying for Google clicks you get free" (id: grw-google-paid-organic-overlap, Google).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Lists the searches you pay for on Google Ads where your own page already ranks near the top organically. Some of that spend buys clicks you would mostly get anyway. It sizes the spend and proposes a careful test.

What to read: Google Ads terms beside your organic rank for the same terms
What to give me: Searches where you pay while already ranking near the top for free

Synthesis tools to use:
- `search_console_organic view=paid_overlap days=28 limit=50`
- `google_ads_metric metric=search_terms days=30 limit=200`

Steps:
1. Pull `search_console_organic view=paid_overlap days=28 limit=50`.
2. Pull `google_ads_metric metric=search_terms days=30 limit=200` for cost and conversions per term.
3. Keep terms where organic position is 3 or better and paid spend is over $100.
4. Propose a 2-week pause test on the non-brand ones, with the total organic plus paid clicks as the measure.

Checks before answering:
- Google Ads campaign and keyword data holds at most 90 days. A short history is the age of the connection, not a business fact. Never compare year over year here.
- Google Ads cost is click cost from the API, not the invoice. Say so beside any total.
- Brand-name terms often need paid cover when rivals bid on them. Say so before suggesting a pause.

Output:
- Answer first: spend on overlapping terms. Table with columns term, organic position, paid spend, paid conversions, suggestion.

Never:
- Nothing changes in any live account. A person on your team makes every change.
- Never fill a missing, gated or empty number with an estimate. Say what is missing and why.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: grw-google-paid-organic-overlap". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
