---
description: "Check Google Ads data is landing: Which Google Ads reports are current, which are empty or stale and why, and whether purchases may be counted twice"
argument-hint: "[anything to add for this run]"
disable-model-invocation: true
---

# Check Google Ads data is landing

Channel: Google · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Check Google Ads data is landing" (id: watch-google-ads-data, Google).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Google Ads data comes in several reports. One can stop while the others look fine. This checks each report has recent rows, and proves an empty one is really empty. It also checks for a second Google tag on the site that may count each purchase twice.

What to read: Google Ads campaigns, search terms, keywords and change history, with rows in the last 7 days for each
What to give me: Which Google Ads reports are current, which are empty or stale and why, and whether purchases may be counted twice

Synthesis tools to use:
- `cost_rules for=watch-google-ads-data`
- `google_ads_metric metric=changes days=30`
- `google_ads_metric metric=campaign_performance days=7`
- `google_ads_metric metric=search_terms days=7`
- `google_ads_metric metric=keyword_performance days=7`
- `data_freshness`
- `ad_health_check only=[google_ads]`

Steps:
1. Call `google_ads_metric` with `metric=changes` and `days=30`. Google keeps change history for about 30 days only. Note the newest change date. If it is gated as not collected, say we do not collect change history yet. That gap is ours, not Google's, so never ask the brand to reconnect. Move on.
2. Call `google_ads_metric` with `metric=campaign_performance` and `days=7`. This is the control. If campaigns have spend rows, the connection works. Note each campaign's destination.
3. Call `google_ads_metric` with `metric=search_terms` and `days=7`, then `metric=keyword_performance` with `days=7`. Neither gives a newest date per row. Confirm each has rows in the 7 days, and compare its cost with the campaign cost from step 2.
4. Call `data_freshness` for the last sync of each Google report. If it skips the Google reports check for time, say so. Only the campaign table's sync time is then known.
5. Call `ad_health_check` with `only=["google_ads"]` for the server's own read of the Google account.
6. Judge each report against the control. Campaign spend with no search terms means the search term report is stuck, not that there was no waste. No campaign spend either means the account was quiet or the connection is down. Say which.
7. Search terms cover only about 80% of search spend. Google hides low-volume terms. That gap is normal.
8. If campaigns send shoppers to Amazon, zero Google conversions are normal. Judge them by the Amazon sales per $1 from step 2, never as broken tracking.
9. Tag check needs a real browser tool. A page-text fetch cannot see tags. Open the website, decline non-essential cookies, then list the Google tags that load. A cookie banner can hold tags, so the count may be low. A Google Ads purchase tag plus the Google and YouTube store app can count one purchase twice. Report it as possible, never as proven. If every campaign sends shoppers to Amazon, a site purchase tag these ads never fire is not a double count. Say so.
10. Ask once whether Google ad spend should count toward Amazon sales or website sales. Use the saved answer if there is one.

Checks before answering:
- Safe test: this only reads. To test it, run it on a second brand built differently from the first, and confirm each report shows rows.
- Spend: give Google spend for the last 7 days from step 2, so the person sees how much runs unmeasured if a report is stuck.
- Zero rows is never a pass. Prove it against the control in step 2.
- A small account with thin data is not broken. Say the spend before calling a report empty.
- Shopping product data exists only if the brand linked Merchant Center. If it is empty, ask whether it is linked.
- Google deletes detail after about 90 days. If a report has been stuck that long, the missing days are gone.

Output:
- One line first: all current, or which report stopped and since when.
- Each report: rows in 7 days, cost against the control, current or stuck.
- The tag check result, or "not checked, no browser here".

Never:
- Never change anything in Google Ads or on the site.
- Never call an empty report a clean result.
- Never state double-counted purchases as fact without the tag check.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Before step 1, call cost_rules. If it returns questions, ask them in one message as written (dollars, choices, what skip does) and save each answer with set_cost_rule. On a scheduled run, use the defaults and list the questions at the end. End the answer with its used_line.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: watch-google-ads-data". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.

---

Anything the person typed after the shortcut is extra instruction for this run: $ARGUMENTS
