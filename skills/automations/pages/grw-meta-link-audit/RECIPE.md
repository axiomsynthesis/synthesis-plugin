# Catch broken ad links and tracking

Channel: Meta · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Catch broken ad links and tracking" (id: grw-meta-link-audit, Meta).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Lists every spending ad with the exact link it sends people to. It catches broken or mismatched links, missing tracking tags and ads still pushing a product you stopped selling.

What to read: Destination links, call to action and objective for every spending Meta ad
What to give me: Ads pointing at the wrong page, missing tracking tags, or sending people to sold-out products

Synthesis tools to use:
- `cost_rules for=grw-meta-link-audit`
- `meta_metric metric=ad_destinations days=14 active_only=true`
- `shopify_metric metric=top_products limit=50`

Steps:
1. Pull `meta_metric metric=ad_destinations days=14 active_only=true`.
2. For each ad, check: the link has tracking tags, the link domain is yours or your Amazon page, and the call to action fits the objective.
3. Pull `shopify_metric metric=top_products limit=50` and flag ads pointing at products with no website sales in the last month.
4. Group problems by type and add up the spend at risk.

Checks before answering:
- Count how many ads had a readable link. If many are blank, say links were not fetched rather than calling them broken.
- A product with no sales may be out of stock or new. Say which you cannot tell.

Output:
- Answer first: spend at risk. Table with columns ad id, spend in 14 days, link, problem.

Never:
- Nothing changes in any live account. A person on your team makes every change.
- Never fill a missing, gated or empty number with an estimate. Say what is missing and why.
- Never open or test a link that could place an order.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Before step 1, call cost_rules. If it returns questions, ask them in one message as written (dollars, choices, what skip does) and save each answer with set_cost_rule. On a scheduled run, use the defaults and list the questions at the end. End the answer with its used_line.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: grw-meta-link-audit". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
