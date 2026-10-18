# Which numbers will still change?

Channel: Data · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Which numbers will still change?" (id: ops-which-numbers-still-moving, Data).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Lists every number in a report that has not finished arriving, so nobody makes a decision on a figure that will move next week. Ad credit keeps arriving for about two weeks, settlements lag, books close a month later, and a stalled sync freezes everything.

What to read: Ad attribution settling, Amazon settlement timing, closed books and source freshness
What to give me: Before a report goes out, the periods and numbers that will still move, and by roughly how much

Synthesis tools to use:
- `cost_rules for=ops-which-numbers-still-moving`
- `amazon_metric metric=attribution_trueup`
- `netsuite_metric metric=pnl_trend months=3`
- `data_freshness`
- `warehouse_freshness`

Steps:
1. Call `amazon_metric metric=attribution_trueup` for how much a recent week's ad sales typically still grow after it ends.
2. Call `netsuite_metric metric=pnl_trend months=3` and mark which months are closed books.
3. Call `data_freshness` for when each source last synced.
4. Call `warehouse_freshness` if the brand mirrors a data warehouse.
5. For each period and metric in the planned report, mark SETTLED, SETTLING (with expected size of change), or STALE (source behind).

Checks before answering:
- Ad attribution is unsettled for about 14 days after a period ends. Any week inside that is settling.
- An estimate month's profit can move by six figures when its books close.
- A source more than two days behind is stale. Say which report sections it feeds.
- Never mark a metric settled because its source is missing.

Output:
- Table: Metric | Period | Status | Expected change | Settles on.
- One line: what is safe to decide on today.

Never:
- Never hold or send a report on the person's behalf.
- Never call an unsettled week a miss.
- Never fill a stale source with an estimate without saying so.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Before step 1, call cost_rules. If it returns questions, ask them in one message as written (dollars, choices, what skip does) and save each answer with set_cost_rule. On a scheduled run, use the defaults and list the questions at the end. End the answer with its used_line.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: ops-which-numbers-still-moving". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
