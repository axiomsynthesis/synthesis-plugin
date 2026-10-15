# What is Performance Max really buying?

Channel: Google · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "What is Performance Max really buying?" (id: grw-google-pmax-xray, Google).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Performance Max hides where money goes. This pulls its spend by product and checks how much of its search traffic is people already typing your brand, which you would mostly get for free.

What to read: Performance Max spend and results by product, and Google search terms
What to give me: How much of Performance Max goes to your own brand name and to each product

Synthesis tools to use:
- `google_ads_metric metric=pmax days=30 limit=30`
- `google_ads_metric metric=products days=30 limit=50`
- `google_ads_metric metric=search_terms days=30 limit=100`

Steps:
1. Pull `google_ads_metric metric=pmax days=30 limit=30`.
2. Pull `google_ads_metric metric=products days=30 limit=50` and rank products by spend and return.
3. Pull `google_ads_metric metric=search_terms days=30 limit=100` and mark terms containing your brand name.
4. Estimate the brand share of Performance Max where the data allows, and list products taking spend with no conversions.

Checks before answering:
- Google Ads campaign and keyword data holds at most 90 days. A short history is the age of the connection, not a business fact. Never compare year over year here.
- Google Ads cost is click cost from the API, not the invoice. Say so beside any total.
- If Performance Max search term data is not present, say the brand share cannot be measured, rather than reporting zero.
- Products with under $20 spend are listed, not judged.

Output:
- Answer first. Table of products: product, spend, conversions, return, verdict.
- One line on brand-name share and one move.

Never:
- Nothing changes in any live account. A person on your team makes every change.
- Never fill a missing, gated or empty number with an estimate. Say what is missing and why.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: grw-google-pmax-xray". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
