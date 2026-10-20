# Block wasted Google searches for me

Channel: Google · Level: Does it for you · Status: Ready after we build it

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Block wasted Google searches for me" (id: do-google-block-wasted-searches, Google).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Finds the Google searches you pay for that never sell, and blocks them as negatives on the campaign that paid for them, after your yes.

What to read: Google Ads search terms with spend, clicks and sales, keywords, and where each campaign sends shoppers
What to give me: Google searches that cost money and sold nothing, added as campaign negatives after your yes, then read back

Synthesis tools to use:
- `google_ads_metric metric=campaign_performance days=30`
- `google_ads_metric metric=search_terms days=90 limit=200`
- `google_ads_metric metric=keyword_performance days=90`
- `export_xlsx`

Steps:
1. Ask: the window (default 90 days), the minimum clicks (default 10), and your own brand name and product names, which are never blocked.
2. Call `google_ads_metric` with `metric=campaign_performance` and `days=30`. Note each campaign's destination. If a campaign sends shoppers to Amazon, Google cannot see its sales, so drop the zero-sales screen for it. Judge it by its Amazon sales per $1. For it, only block searches that do not fit the product or name a rival.
3. Call `google_ads_metric` with `metric=search_terms`, `days=90` and `limit=200`, the most it takes. Read every result_page. For campaigns that send shoppers to the website, keep terms with clicks at or over the minimum, spend over $25 and zero sales in the window. Skip places where already_excluded is true. If campaigns have spend but this is empty, stop. The search term report is stuck.
4. Call `google_ads_metric` with `metric=keyword_performance` and `days=90` to see which keyword pulled each term in. Never block a term that is an active keyword in another campaign of the same account.
5. Drop any term that contains your brand or product names or a rival you bid on on purpose. A rival-name search is a candidate only when you do not bid on that rival on purpose. If a shorter version is blocked as exact match, the longer search still spends.
6. Build the change list: campaign, term, match type (default phrase, ask), spend, clicks, and the undo. Save it with `export_xlsx` as `google-negatives.xlsx`. Show it and wait for yes.
7. In Google Ads, check the account picker at the top shows the right account.
8. Go to Campaigns, then Audiences, keywords and content, then Search keywords, then the Negative search keywords tab. Click the blue plus.
9. Choose "Add negative keywords to a campaign", never "Add to list". Pick the one campaign named in the term's place. Paste its terms one per line. Phrase match is "term" in quotes, exact is [term]. Click Save.
10. Repeat step 9 for each campaign. Do one campaign at a time. Never use a shared negative list, because it touches every campaign linked to it.
11. Skip every Recommendations card, optimization score prompt and "raise budget" offer.
12. Reload the Negative search keywords tab. Read back every term, campaign and match type against the list.
13. Change history is not collected, so it cannot confirm the change. The next day, call `google_ads_metric` with `metric=search_terms` and `days=7`. Confirm the blocked searches show no new cost.

Checks before answering:
- Safe test when asked: add one low-spend term to one campaign, read it back, then show how to remove it. Nothing else changes.
- Spend: blocking cuts spend and never raises it. Say the dollars a month the list saves.
- For campaigns that send shoppers to Amazon, put their Amazon sales per $1 beside any saving.
- If every campaign sends shoppers to Amazon, the list may be empty or rival names only. Say so.
- Search terms show about 80% of search spend. Google hides low-volume terms. Say so beside the total.
- Performance Max shows no search terms here. Say how much spend that hides.
- If the search term read is empty, say so. Never say there is no waste.

Output:
- One line first: terms blocked and dollars a month saved.
- A table: campaign, term, match type, spend, clicks, sales, added yes or no.
- The file google-negatives.xlsx, and what to check in a week.

Never:
- Never block your own brand or product names, or the searches your keywords target.
- Never edit a shared negative list, a budget, a bid or a keyword.
- Never accept a Google recommendation.

Rules:
- This one makes the change for me, in my own browser where I am already signed in (Claude in Chrome or another browser tool). Before changing anything, show me the exact change in one list: every object by name, every budget, price, link and date. Wait for my clear yes. Then change only what I approved. Never delete, never buy, never raise spend or a price beyond what I approved, and decline every platform suggestion that would. If a platform's safety check stops a step, quote my approval once and stop if it still refuses. When it is done, read every changed object back and tell me what is live, what is off and anything that differs from the plan. If no browser tool is available here, give me the exact click-by-click steps instead.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: do-google-block-wasted-searches". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.

Not fully ready yet (ready after we build it): Claude has never run these Google Ads screens on a live account, and our Google write access is off. Until one supervised run proves them, change only with the person watching. Not usable for campaigns that send shoppers to Amazon until Amazon credit by search term exists. Amazon credits Google by ad group only. Do the parts you can and say plainly what is missing.
