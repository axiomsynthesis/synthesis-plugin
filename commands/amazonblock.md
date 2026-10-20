---
description: "Block Amazon searches that cost money and never sell: Each wasted search blocked where it wastes, in your Amazon Ads console or a bulk file, then read back"
argument-hint: "[anything to add for this run]"
disable-model-invocation: true
---

# Block Amazon searches that cost money and never sell

Channel: Amazon · Level: Does it for you · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Block Amazon searches that cost money and never sell" (id: do-amazon-block-wasted-searches, Amazon).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Finds Amazon ad searches that took money and sold nothing. It blocks each in your Amazon Ads console where it wastes, or in a bulk file for you to upload. This can only lower spend.

What to read: Amazon Ads search terms by ad group, blocks in place, break-even ad cost
What to give me: Each wasted search blocked where it wastes, in your Amazon Ads console or a bulk file, then read back

Synthesis tools to use:
- `cost_rules for=do-amazon-block-wasted-searches`
- `amazon_metric metric=ppc_search_terms start_date=YYYY-MM-DD end_date=YYYY-MM-DD min_clicks=10 limit=50`
- `breakeven_roas months=1`
- `export_xlsx filename=negatives_bulk.xlsx`
- `amazon_metric metric=ppc_account_changes days=3`

Steps:
1. Ask the window. Default 90 days ending 14 days ago and 10 clicks. Ask browser or bulk file. Default browser, up to 10 rows.
2. Call `amazon_metric` with `metric=ppc_search_terms`, `start_date`, `end_date`, `min_clicks=10` and `limit=50`. The most it takes is 200. Read every page with `result_page` until `next_page` is empty. Use `totals` for the headline. Rows skip searches already blocked there.
3. Call `breakeven_roas` with each main product's `asin` and `months=1`. Match each campaign to the product it sells. Keep searches that spent over one break-even sale and sold nothing.
4. Drop every row with `is_branded` true or any spelling of your name. Block a short wasting fragment, never your own name.
5. Before a phrase block, check the word in the n-gram list and the harvest list from step 2. If it sells anywhere, block exact only.
6. Show one list, one row per ad group in the row's `ad_groups`: search, campaign, ad group, level, match type, spend, clicks, undo. Wait for yes.
7. Bulk file: call `export_xlsx` with `filename=negatives_bulk.xlsx` in Amazon's bulk template. Stop. You upload it.
8. Browser: open Amazon Ads, Campaign manager. Read the account and country at the top, say them, get a yes.
9. Open the campaign by its full name first, then the ad group inside it. Many ad groups share names like Ad Group 1. If two campaigns share a name, stop and ask.
10. Open the negative keywords list there, or on the campaign for a campaign row. A product-target ad group takes negative products, not keywords: stop there. If a campaign is run by an outside bid tool, ask before adding. If the screen looks different, stop and describe it.
11. Read the list on screen. The report cannot see phrase or Sponsored Brands blocks. If it is already there, mark it skipped. Else type it exactly, pick the row's match type, read it twice, save.
12. Reload and read it back.
13. Next day, run step 2 again. Blocked searches must be gone from those ad groups. Call `amazon_metric` with `metric=ppc_account_changes` and `days=3` to see each one logged.

Checks before answering:
- Safe test: on a test run, make the bulk file only. For a live test, block one search in a paused ad group and read it back.
- Spend: never touch a bid, budget or placement setting here. Decline every console suggestion and suggested bid.
- If the report could not check existing blocks, stop.
- Sales land up to 30 days after a click. Leave out the last 14 days. Never compare a fresh week with an older one.
- One search can waste in 6 ad groups. Ten browser rows may cover only 2 or 3 searches. Say how many are left.
- No API path for Amazon blocks is live. Use the browser or the bulk file.

Output:
- One line first: searches blocked and what they took.
- A table: search, campaign, ad group, level, match type, spend, done or skipped.

Never:
- Never block your own brand, a product name, or a search that sold.
- Never swap exact and phrase. Phrase blocks every search with those words.
- A block cannot be edited. Its undo, archive, is permanent.
- Never upload the bulk file yourself.

Rules:
- This one makes the change for me, in my own browser where I am already signed in (Claude in Chrome or another browser tool). Before changing anything, show me the exact change in one list: every object by name, every budget, price, link and date. Wait for my clear yes. Then change only what I approved. Never delete, never buy, never raise spend or a price beyond what I approved, and decline every platform suggestion that would. If a platform's safety check stops a step, quote my approval once and stop if it still refuses. When it is done, read every changed object back and tell me what is live, what is off and anything that differs from the plan. If no browser tool is available here, give me the exact click-by-click steps instead.
- Before step 1, call cost_rules. If it returns questions, ask them in one message as written (dollars, choices, what skip does) and save each answer with set_cost_rule. On a scheduled run, use the defaults and list the questions at the end. End the answer with its used_line.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: do-amazon-block-wasted-searches". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.

---

Anything the person typed after the shortcut is extra instruction for this run: $ARGUMENTS
