# Where to play and how to win

Channel: Strategy · Level: Prepare · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Where to play and how to win" (id: ops-playing-to-win-choices, Strategy).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Walks through five linked strategy choices and checks each against the data. The value is in the links: an ambition that does not match where the business actually makes money gets flagged before it becomes a plan.

What to read: Revenue and profit by channel and product range, customer value by entry product, search share and price position
What to give me: Five linked strategy choices, each tested against your numbers

Synthesis tools to use:
- `cost_rules for=ops-playing-to-win-choices`
- `strategy_framework framework=playing_to_win`
- `netsuite_metric metric=family_revenue months=12 limit=10`
- `amazon_metric metric=contribution_by_asin months=6`
- `shopify_metric metric=product_ltv`
- `amazon_metric metric=search_query_performance`
- `export_docx`

Steps:
1. Ask the founder for their current answer to each of the five choices, in a line each.
2. Pull evidence for where to play: `netsuite_metric metric=family_revenue months=12 limit=10` for ranges across channels, `amazon_metric metric=contribution_by_asin months=6` for profit by product.
3. Pull evidence for how to win: `shopify_metric metric=product_ltv` for value by entry product, `amazon_metric metric=search_query_performance` for share of search.
4. Run `strategy_framework framework=playing_to_win` with the five choices.
5. For each choice mark SUPPORTED, CONTRADICTED or UNTESTED by the data, with the number.
6. Write it with `export_docx` as a two-page memo.

Checks before answering:
- Family revenue from the books covers all channels. Never size an Amazon-only choice against it.
- Capabilities and systems are mostly judgement. Label them.
- A choice contradicted by data is reported plainly, not softened.

Output:
- Word memo: the five choices, each with verdict, evidence and the one link that breaks.
- Two lines in chat: the strongest choice and the weakest link.

Never:
- Never write the strategy for the founder. Test theirs.
- Never copy any book's text. Describe the method in plain words.
- Never present judgement as measured.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Before step 1, call cost_rules. If it returns questions, ask them in one message as written (dollars, choices, what skip does) and save each answer with set_cost_rule. On a scheduled run, use the defaults and list the questions at the end. End the answer with its used_line.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: ops-playing-to-win-choices". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
