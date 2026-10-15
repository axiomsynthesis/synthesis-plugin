# Sort and size your growth ideas

Channel: Strategy · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Sort and size your growth ideas" (id: ops-growth-options, Strategy).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Takes the founder's growth ideas and sorts them by distance from today's business (same products to same buyers, new products, new buyers, or both new). Then it sizes each in dollars with a chance of success and ranks them. Ideas far from today are not wrong, just riskier, and the ranking says by how much.

What to read: Your list of growth ideas, plus the revenue base and margin each would build on
What to give me: Each idea sorted by how far it is from what you do today, sized in dollars and ranked

Synthesis tools to use:
- `strategy_framework framework=ansoff_matrix`
- `strategy_framework framework=rank_decision_options`
- `net_revenue month=YYYY-MM`
- `amazon_metric metric=search_term_gaps`
- `amazon_metric metric=geo_penetration`

Steps:
1. Ask for the list of ideas, each with a rough cost.
2. Run `strategy_framework framework=ansoff_matrix moves=[{name, market, product}]` with each idea's market and product as existing or new.
3. Size each against the base it can move: `net_revenue` for Amazon ideas, `amazon_metric metric=search_term_gaps` for search demand you miss, `amazon_metric metric=geo_penetration` for regions underserved.
4. Ask for, or agree, a chance of success for each. Label it as judged.
5. Run `strategy_framework framework=rank_decision_options options=[{name, cost, payoff, p_good}]` with cost, payoff and chance (0 to 1) per idea.

Checks before answering:
- Size Amazon-only ideas against Amazon revenue, never company revenue.
- Chances are judgement. Show them so the person can change them.
- An idea with no measurable base is ranked "not sized".

Output:
- Table: Idea | Type | Cost | Payoff a year | Chance | Expected value | Rank.
- Two lines: the top idea and what would make the second overtake it.

Never:
- Never present a judged chance as measured.
- Never start any initiative.
- Never size against a base the idea cannot touch.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: ops-growth-options". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
