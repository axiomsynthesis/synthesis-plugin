# Fix your Google Shopping product mix

Channel: Google · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Fix your Google Shopping product mix" (id: grw-google-shopping-products, Google).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Compares what Google's shopping ads push with what your site actually sells. It finds products eating spend with no conversions and best sellers that barely get shown.

What to read: Google Ads results by product and website product sales
What to give me: Products Google spends on without sales, and best sellers it ignores

Synthesis tools to use:
- `google_ads_metric metric=products days=30 limit=100`
- `shopify_metric metric=top_products limit=50`

Steps:
1. Pull `google_ads_metric metric=products days=30 limit=100`.
2. Pull `shopify_metric metric=top_products limit=50`.
3. Match on product id or handle, not name.
4. List spend-without-sales products (over $50, zero conversions) and ignored best sellers (top 10 site sellers under 2% of shopping spend).

Checks before answering:
- Google Ads campaign and keyword data holds at most 90 days. A short history is the age of the connection, not a business fact. Never compare year over year here.
- Report the match count. Unmatched products are listed separately, never dropped.

Output:
- Answer first. Two short tables: spend without sales, and ignored best sellers.

Never:
- Nothing changes in any live account. A person on your team makes every change.
- Never fill a missing, gated or empty number with an estimate. Say what is missing and why.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: grw-google-shopping-products". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
