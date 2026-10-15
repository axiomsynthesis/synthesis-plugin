# Real change or just noise?

Channel: Data · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Real change or just noise?" (id: ops-real-change-or-noise, Data).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Stops a team from reacting to a normal bad week, and from ignoring a real drop. It compares the recent run with the metric's usual wobble and says whether the level has shifted.

What to read: Weekly or monthly history of any metric the person is worried about
What to give me: Whether a recent move is a real shift or normal week-to-week wobble, with the evidence

Synthesis tools to use:
- `query_series metric=<metric> grain=week`
- `strategy_framework framework=detect_regime_shift`
- `strategy_framework framework=signal_noise_decomp`

Steps:
1. Ask which metric and how many recent weeks look off.
2. Call `query_series metric=<metric> grain=week` for at least 26 weeks. Use the product filter if the worry is one product.
3. Run `strategy_framework framework=detect_regime_shift values=[...] recent_n=<weeks> metric_name=<metric>` with the weekly values, oldest first.
4. Run `strategy_framework framework=signal_noise_decomp values=[...] metric_name=<metric>` on the same series for the size of normal noise.
5. If it is a shift, find the first week of the new level and list events that week (price change, stockout, listing change, deal end).

Checks before answering:
- Weeks with deals or stockouts are not normal. Mark them before judging noise.
- The latest week may still be settling. Leave it out if attribution or settlement is still moving.
- Fewer than 12 weeks of history is too few to judge. Say so.
- Do not mix order-basis and settled figures in one series.

Output:
- Three lines: verdict (shift or noise), size of the move against normal noise, and the week it started.
- A small chart if the person wants one.

Never:
- Never name a cause from timing alone. List candidates.
- Never act on a single week.
- Never change anything in an account.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: ops-real-change-or-noise". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
