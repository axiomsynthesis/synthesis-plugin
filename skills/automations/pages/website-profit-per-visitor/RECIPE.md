# Profit per website visitor

Channel: Website · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Profit per website visitor" (id: website-profit-per-visitor, Website).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Answers one question: does a visit to the website make money? It takes the website's own orders' profit after product cost, fees and shipping, divides it by the month's visits, and sets that against what ads pay for a visit. Orders another marketplace sent into the store never visited the website, so they are left out.

What to read: Website profit after product cost, fees and shipping, the website's visits, and ad spend that sends shoppers there
What to give me: What each website visit earns before ads, against what a visit costs in ads, month by month

Synthesis tools to use:
- `cost_rules for=website-profit-per-visitor`
- `shopify_metric metric=profit month=YYYY-MM`
- `meta_metric metric=ad_destinations days=30`

Steps:
1. Call `shopify_metric` with `metric=profit` and `month=` set to last month, and again for the month before.
2. Read `profit_per_visitor`, `visitors`, `own_store_profit`, `visitors_note` and `profit_per_visitor_note` for each month.
3. If `profit_per_visitor` is missing, say why from `visitors_note` or `no_headline_reason`, and stop.
4. Call `meta_metric` with `metric=ad_destinations` and `days=30` for the Meta spend that sends shoppers to the website. Divide it by the month's visits for the ad cost of a visit. Say it is Meta only.
5. Compare profit per visitor with `ppv_marks_estimated`. Say these marks are estimates, not targets the owner set.

Checks before answering:
- Profit per visitor is before ads. Say so in the same sentence as the number.
- Read `data_quality_flags`. Each cost not connected makes profit per visitor read high. Name them.
- If visits cover fewer days than the month, the figure reads high. Say so.
- Subscription renewals are profit with no visit behind them. If the store sells subscriptions, say they lift the figure.
- Use closed months.

Output:
- One line first: profit per visit before ads for last month, and the change from the month before.
- A small table: month, visits, website profit, profit per visit, ad cost per visit.
- One line: the gap between profit per visit and ad cost per visit, in cents.
- One move: the lever that would close the gap most, with what to measure next month.

Never:
- Never count orders another marketplace sent into the store as website visits' profit.
- Never call an estimated mark the owner's target.
- Never change budgets or prices. A person does that.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Before step 1, call cost_rules. If it returns questions, ask them in one message as written (dollars, choices, what skip does) and save each answer with set_cost_rule. On a scheduled run, use the defaults and list the questions at the end. End the answer with its used_line.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: website-profit-per-visitor". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
