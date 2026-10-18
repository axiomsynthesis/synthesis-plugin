# Prep for the board's toughest questions

Channel: Leadership · Level: Prepare · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Prep for the board's toughest questions" (id: ops-board-questions-prep, Leadership).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Prepares the founder for a board or investor meeting by finding the numbers that will draw questions: big moves, misses against what was said last time, and decisions whose results are now in. Each question gets a short, numbered answer so the meeting is spent on decisions, not on reconstructing the quarter.

What to read: The latest closed month and quarter, the biggest moves in revenue, margin, cash and customers, and your own explanations
What to give me: The ten hardest questions a board or investor will ask this period, each with a short answer backed by a number

Synthesis tools to use:
- `cost_rules for=ops-board-questions-prep`
- `netsuite_metric metric=pnl_trend months=13`
- `explain_metric_move metric=revenue month=YYYY-MM`
- `metric_timeseries metric_keys=[revenue,new_customers,returning_pct] start_month=YYYY-MM end_month=YYYY-MM`
- `amazon_metric metric=pnl_waterfall month=YYYY-MM`
- `recall_decisions`
- `export_docx`

Steps:
1. Call `netsuite_metric metric=pnl_trend months=13` for revenue, margin and EBITDA on closed months, and the same quarter last year where both are closed.
2. Call `explain_metric_move metric=revenue month=YYYY-MM` for the latest month's causes.
3. Call `metric_timeseries metric_keys=["revenue","new_customers","returning_pct"]` for customer trends.
4. Call `amazon_metric metric=pnl_waterfall month=YYYY-MM` for Amazon profit lines.
5. Call `recall_decisions` for decisions shared last time and their outcomes.
6. Rank the moves by size and surprise. Write ten questions with answers of two to three sentences, each with its number and basis (closed or estimate).
7. Write it with `export_docx`.

Checks before answering:
- Quote profit only from closed months, or label it an estimate in the answer.
- If a question has no good answer, say so in the document. Do not invent one.
- Compare with what was told to the board last time if the person shares it.

Output:
- Word document: ten questions, each with answer, number, basis and source.
- Two lines in chat: the hardest question and the one decision to bring to the meeting.

Never:
- Never send the document to anyone.
- Never soften a miss.
- Never quote an estimate as closed.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Before step 1, call cost_rules. If it returns questions, ask them in one message as written (dollars, choices, what skip does) and save each answer with set_cost_rule. On a scheduled run, use the defaults and list the questions at the end. End the answer with its used_line.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: ops-board-questions-prep". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
