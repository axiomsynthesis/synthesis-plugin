# Stop paying Google for searches that don't sell

Channel: Google · Level: Prepare · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Stop paying Google for searches that don't sell" (id: google-ads-cleanup, Google).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Finds the Google searches you pay for that never turn into sales, and puts them in a negative keyword file a person can upload. It also flags paid terms you already rank for at the top of Google, as a test list.

What to read: Google Ads
What to give me: A ready-to-upload list of searches to block, and the money it saves a month

Synthesis tools to use:
- `google_ads_metric metric=search_terms`
- `google_ads_metric metric=campaign_performance`
- `google_ads_metric metric=keyword_performance`
- `search_console_organic view=paid_overlap`
- `export_xlsx`

Steps:
1. Call `google_ads_metric` with `metric=campaign_performance` and `days=30` to see how much spend runs through keyword campaigns and how much through Performance Max.
2. Call `google_ads_metric` with `metric=search_terms`, `days=90` and `limit=500` for every search term with spend, clicks and sales.
3. Call `google_ads_metric` with `metric=keyword_performance` and `days=90` to see which keyword pulled each wasted term in.
4. Call `search_console_organic` with `view="paid_overlap"` and `days=90` for paid terms that already rank in the organic top 3.
5. Mark as negatives the terms with spend over $50 and no sales in 90 days. Save with `export_xlsx`, `filename="google-ads-negatives.xlsx"`, with campaign, term and match type columns ready for upload.

Checks before answering:
- Say what share of spend has no search terms at all, because Performance Max does not show them.
- 90 days with no sale is the bar. A term with 3 clicks is too thin to block.
- If the search term read is empty or fails, say so. Never say there is no waste.
- Paid terms you rank for are a test list, not a cut list.

Output:
- One line first: dollars a month the negatives save.
- A table: term, campaign, spend, clicks, sales, reason.
- File: google-ads-negatives.xlsx. A person uploads it in Google Ads.

Never:
- Nothing goes live. A person reviews and uploads the file.
- Never block a term that has sold in the window.
- Never call the paid overlap list a cut list.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: google-ads-cleanup". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
