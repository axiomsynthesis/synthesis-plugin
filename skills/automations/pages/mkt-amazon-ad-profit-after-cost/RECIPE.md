# Find ads that lose money after product cost

Channel: Amazon · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Find ads that lose money after product cost" (id: mkt-amazon-ad-profit-after-cost, Amazon).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Ad dashboards stop at sales. This goes to profit, and it asks what the ads themselves earn.
Ad profit is the sales the ads are credited with, times the product's profit rate before ads, minus the ad spend.
A product can make money after its ad bill and still have ads that lose money, because its organic sales pay for them. This names those ads.

What to read: Each advertised product's settled sales, Amazon fees, product cost, its ad-credited sales and its own ad spend for the last three closed months
What to give me: Product families whose ads lose money on the sales they are credited with, and the dollars

Synthesis tools to use:
- `cost_rules for=mkt-amazon-ad-profit-after-cost`
- `amazon_metric metric=ppc_profit_by_asin month=YYYY-MM limit=40`
- `amazon_metric metric=ad_spend_monthly month=YYYY-MM`
- `operator_inputs section=cogs`

Steps:
1. Call `amazon_metric metric=ppc_profit_by_asin month=YYYY-MM limit=40` three times, once for each of the last three months whose `settlement_status.fully_settled` is true. If the newest month is still settling, show it only as the estimate range the tool returns.
2. For each product row, work out ad profit: `ad_sales` x (`contribution_before_ads` / `sales`) minus `ad_spend_reported`. Add the rows up by `family`. Compare the three months by family to see whether the loss is new or steady.
3. Call `amazon_metric metric=ad_spend_monthly month=YYYY-MM` for the latest settled month. Use its Sponsored Products and Display spend in `by_ad_product` for the spend check below.
4. Call `operator_inputs section=cogs` and list any advertised product that has no cost entered.
5. Sort families by ad dollars lost. Also work out margin after ads: `profit_after_ads` over `sales`, by family. For each losing family, give one move: cut ad spend, raise price, or stop advertising it.

Checks before answering:
- Use a fully settled month: the latest month whose `settlement_status.fully_settled` is true. If the newest month is still settling, show it only as the estimate range the tool returns. A month that has ended but is still settling has all its ad spend and only part of its sales, so it shows false losses.
- A product that is profitable after ads can still have ads that lose money. Never call the ads fine because the product row is positive.
- Credited sales are the most the ads can claim. Some of those buyers would have bought anyway. So a loss on credited sales is a real loss, and a small ad profit may be smaller still.
- Sum `ad_spend_reported` across rows and compare it with the Sponsored Products and Display spend from `ad_spend_monthly` for the month. Say how much is unmatched. The Profit page's advertising line also holds Sponsored Brands and outside traffic sent to Amazon, so never tie to it.
- Zero is not the only line. Flag any family under 10% margin after ads as "ads eat the margin", even when it is above zero.
- A product with incomplete cost is flagged by the tool. Never call it a loser or a winner.
- One bad month is not a pattern. Use the 3-month view before recommending a stop.
- This answer cannot yet show the return on the last dollar spent, or a tested lift. Say so if someone asks whether a smaller budget would earn more.

Output:
- One line: the dollars the ads lost last month on the sales they are credited with, and the number of families.
- A table by family: ad spend, credited sales, ad profit on credited sales, product profit after ads, margin after ads, 3-month direction, move.
- A list of advertised products with no cost entered.

Never:
- Never estimate a missing product cost.
- Never change ads or prices in any account.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Before step 1, call cost_rules. If it returns questions, ask them in one message as written (dollars, choices, what skip does) and save each answer with set_cost_rule. On a scheduled run, use the defaults and list the questions at the end. End the answer with its used_line.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: mkt-amazon-ad-profit-after-cost". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
