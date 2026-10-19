---
description: "Profit per website visit: What each website visit earns before ads, and what a paid visit earns against what this brand's ads pay for one"
argument-hint: "[anything to add for this run]"
disable-model-invocation: true
---

# Profit per website visit

Channel: Website · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Profit per website visit" (id: website-profit-per-visitor, Website).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Answers one question: does a visit to the website make money? A visit here is one session, so one shopper who comes back twice counts twice. It takes the website's own orders' profit after product cost, fees and shipping, divides it by the month's visits, and does the same for paid visits. It sets paid visits against what this brand's own ads pay for one. Orders another marketplace sent into the store never visited the website, so they are left out.

What to read: Website profit after product cost, fees and shipping, the website's visits, and ad spend that sends shoppers there
What to give me: What each website visit earns before ads, and what a paid visit earns against what this brand's ads pay for one

Synthesis tools to use:
- `cost_rules for=website-profit-per-visitor`
- `shopify_metric metric=profit month=YYYY-MM`

Steps:
1. Call `shopify_metric` with `metric=profit` and `month=` set to last month, and again for the month before.
2. Read `profit_per_visitor`, `visitors`, `own_store_profit`, `visitors_note` and `profit_per_visitor_note` for each month.
3. If `profit_per_visitor` is missing, say why from `visitors_note` or `no_headline_reason`, and stop.
4. Read `paid_visitors`, `profit_per_paid_visitor`, `website_ad_spend`, `ad_cost_per_paid_visit` and `ad_cost_per_ad_click`. `website_ad_spend` is Meta, Google and TikTok spend that points at the website. If `ad_cost_per_paid_visit` is missing, give the reason in `paid_note` and use `ad_cost_per_ad_click`, saying clicks run above visits so it reads low. If both are missing, give no gap.
5. Compare `profit_per_paid_visitor` with `ppv_marks.break_even`. That mark is this brand's own ad cost for a paid visit this month. It is not a target the owner set. Never set a budget from it alone.

Checks before answering:
- Profit per visit is before ads. Say so in the same sentence as the number.
- The tool fields say visitor, but the count is sessions. Call it a visit, never a visitor or a person.
- Visits include free ones from search, email and direct. The fair test is profit per paid visit against ad cost per paid visit. Never set ad cost against all visits.
- Paid visits are the visits tagged as paid. Profit per paid visit takes a paid order to be an average order. Say so.
- Own-site orders are split from marketplace orders order by order, with the books' shipping cost per order. If they cannot be split, there is no figure. Never guess one.
- Read `data_quality_flags`. Each cost not connected makes profit per visit read high. Name them.
- If visits cover fewer days than the month, the figure reads high. Say so.
- Subscription renewals are profit with no visit behind them. If the store sells subscriptions, say they lift the figure. This answer does not measure that lift yet.
- Use closed months.

Output:
- One line first: does a paid website visit pay for what ads spend to bring it? Profit per paid visit before ads for last month against ad cost per paid visit, the gap in cents, profit per visit, and the change from the month before.
- A small table: month, visits, paid visits, website profit, profit per visit, profit per paid visit, ad cost per paid visit.
- One move: the lever that would close the gap most, with what to measure next month.

Never:
- Never count orders another marketplace sent into the store as website visits' profit.
- Never call the break-even mark the owner's target, and never use another brand's mark.
- Never change budgets or prices. A person does that.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Before step 1, call cost_rules. If it returns questions, ask them in one message as written (dollars, choices, what skip does) and save each answer with set_cost_rule. On a scheduled run, use the defaults and list the questions at the end. End the answer with its used_line.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: website-profit-per-visitor". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.

---

Anything the person typed after the shortcut is extra instruction for this run: $ARGUMENTS
