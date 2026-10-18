# Should you launch in a new marketplace?

Channel: Growth · Level: Advise · Status: Ready after we build it

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Should you launch in a new marketplace?" (id: growth-new-marketplace-readiness, Growth).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Says whether a new marketplace or country is worth entering, and what the first steps are. It compares your own sales with the shelf and search interest in the new market.

What to read: Your sales, category data
What to give me: A go, no-go or not yet on a new marketplace or country, and the first steps

Synthesis tools to use:
- `cost_rules for=growth-new-marketplace-readiness`
- `channel_revenue_mix`
- `amazon_metric metric=pnl_by_asin`
- `scrape_amazon_search`
- `google_trends`

Steps:
1. Call `channel_revenue_mix` and `amazon_metric` with `metric=pnl_by_asin` for the last closed month, to pick the products with the margin to travel.
2. For your top 3 searches, call `scrape_amazon_search` with that `keyword`, `k=20` and the new market's `domain` to read rivals, prices and ratings there.
3. Call `google_trends` with the same searches and `geo` set to the new country, against your home country, for relative interest.
4. Write a go or no-go with the first three steps, and say what is still unknown.

Checks before answering:
- Google Trends is relative interest, not volume. Never turn it into sales.
- A live shelf read is one day. Say so.
- Without category size, the answer is a direction, not a forecast. Say that plainly.

Output:
- One line first: go, no-go or not yet, and the main reason.
- A table: market, rivals on page one, average price, average rating, relative interest.
- Three first steps, and what data would change the answer.

Never:
- Never open an account or list a product in a new market. A person does that.
- Never invent a market size.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Before step 1, call cost_rules. If it returns questions, ask them in one message as written (dollars, choices, what skip does) and save each answer with set_cost_rule. On a scheduled run, use the defaults and list the questions at the end. End the answer with its used_line.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: growth-new-marketplace-readiness". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.

Not fully ready yet (ready after we build it): We do not hold outside market data such as category size and search volume by country yet. A live shelf read and relative search interest work today, but they cannot size demand on their own. Do the parts you can and say plainly what is missing.
