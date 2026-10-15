# Did the test work?

Channel: Data · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Did the test work?" (id: ops-test-readout, Data).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Reads out a test in plain odds. Instead of "significant or not", it says how likely the new version is to be better and by how much, so the founder can decide whether to switch, keep testing or stop.

What to read: Results of a test you ran (a price, a page, an offer, an email), as successes and tries for each version
What to give me: The chance the new version is really better, how big the difference likely is, and whether to keep running it

Synthesis tools to use:
- `run_bayesian alpha=1 beta=1 successes=<wins> trials=<tries>`
- `query_series metric=orders grain=week asin=<asin>`
- `query_series metric=sessions grain=week asin=<asin>`
- `log_outcome`

Steps:
1. Ask what was tested, the dates, and the counts for each version (orders and sessions, clicks and sends, and so on). For Amazon listings, pull `query_series metric=orders grain=week asin=<asin>` and `query_series metric=sessions grain=week asin=<asin>` for each version's weeks. Wins are orders and tries are sessions. Never use the conversion rate series here. It is units over sessions, so one shopper buying three counts as three wins.
2. Run `run_bayesian alpha=1 beta=1 successes=<wins> trials=<tries>` for each version.
3. Compare the two results: the chance B beats A, and the likely size of the difference.
4. Translate the difference into dollars a month at current traffic.
5. If a decision was logged, record the outcome with `log_outcome`.

Checks before answering:
- A before-and-after on Amazon is not a split test; season, price and ads change too. Say so and widen the caution.
- Under 300 trials per version is usually too few. Say so.
- Stopping the moment one version looks ahead inflates the result. Ask whether the end date was set in advance.

Output:
- Four lines: the chance B is better, the likely difference, the dollar effect, and the recommendation (switch, run longer, or stop).

Never:
- Never switch the live version.
- Never call a before-and-after a controlled test.
- Never round a 70% chance up to "it works".

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: ops-test-readout". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
