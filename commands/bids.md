---
description: "Build the keyword bid change sheet: A ready-to-upload sheet of bid cuts and raises by keyword, each tied to the product's real break-even"
argument-hint: "[anything to add for this run]"
disable-model-invocation: true
---

# Build the keyword bid change sheet

Channel: Amazon · Level: Prepare · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Build the keyword bid change sheet" (id: mkt-amazon-keyword-bid-sheet, Amazon).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
This turns ad data into a bid sheet a person can upload. Every keyword gets a target bid set from what its product can afford, not from a rule of thumb.
It covers both directions: cuts on keywords losing money and raises on keywords leaving sales on the table.

What to read: Every Sponsored Products keyword and product target with its current bid, spend, clicks and sales over a mature window, plus each product's break-even ad cost
What to give me: A ready-to-upload sheet of bid cuts and raises by keyword, each tied to the product's real break-even

Synthesis tools to use:
- `cost_rules for=mkt-amazon-keyword-bid-sheet`
- `amazon_metric metric=ppc_keyword_bids days=60 min_clicks=20 limit=80 shape=compact match_type=EXACT`
- `amazon_metric metric=ppc_keyword_bids days=60 min_clicks=20 limit=80 shape=compact match_type=PHRASE`
- `amazon_metric metric=ppc_keyword_bids days=60 min_clicks=20 limit=80 shape=compact match_type=BROAD`
- `amazon_metric metric=breakeven_acos_ltv months=12 limit=12`
- `amazon_metric metric=ppc_purchase_latency days=60 limit=10`
- `export_xlsx`

Steps:
1. Call `amazon_metric metric=ppc_purchase_latency days=60 limit=10` to see how long sales take to land after a click.
2. Call `amazon_metric metric=ppc_keyword_bids days=60 min_clicks=20 limit=80 shape=compact` three times, once each with `match_type=EXACT`, `match_type=PHRASE` and `match_type=BROAD`. Leave the dates unset: the tool already picks a window whose sales have landed, and passing dates overrides it. Cuts come first in each. Keep the campaign, ad group and target ids. If `paging` says more rows exist, call again with `offset` set to where the next page starts until every row is read.
3. Call `amazon_metric metric=breakeven_acos_ltv months=12 limit=12`. It takes no offset; if the result says it was split into pages, call again with `result_page` set to the next page. Use the first-order break-even for one-time products and the 3-month figure for products people rebuy. Say which you used.
4. For each keyword the target is the most it can pay per click and still make money: revenue per click x the product's break-even ad cost share (the tool returns it as `max_profitable_cpc`). Compare the target with the cost actually paid per click (`cpc`), never with the bid: the paid cost often runs well above the bid. Cut where the paid cost is over 15% above target. Raise only where the paid cost is over 25% below target AND the keyword has orders. A keyword paying more per click than its target is never raised, whatever its bid says. The tool's own `suggested_bid` only ever cuts, so work out raises yourself.
5. Build the sheet with `export_xlsx`: a "changes" tab with campaign id, ad group id, target id, keyword, match type, current bid, new bid, reason; and a "skipped" tab for thin or uncosted keywords.

Checks before answering:
- Keywords under 20 clicks go to "skipped". Too few clicks to set a bid.
- A product with no entered product cost has no real break-even. Leave its keywords out and list the product as missing a cost.
- Say how much of the window's Sponsored Products keyword spend the sheet covers, in dollars and percent. If a read says it was cut, the sheet is partial: say so in the first line, never as a footnote.
- Never set a bid below Amazon's minimum. Cap any single change at 30%, so one sheet cannot swing the account.

Output:
- One line: number of cuts, number of raises, and the monthly dollar effect at today's clicks.
- File `bid_changes_<week>.xlsx` with the two tabs above.
- One line on how we will know: recheck return per dollar on these keywords in 3 weeks.

Never:
- Never upload or change bids in the account. A person uploads the file.
- Never guess a missing product cost.
- Never judge keywords on a window that is still collecting sales.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Before step 1, call cost_rules. If it returns questions, ask them in one message as written (dollars, choices, what skip does) and save each answer with set_cost_rule. On a scheduled run, use the defaults and list the questions at the end. End the answer with its used_line.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: mkt-amazon-keyword-bid-sheet". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.

---

Anything the person typed after the shortcut is extra instruction for this run: $ARGUMENTS
