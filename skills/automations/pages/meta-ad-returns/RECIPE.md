# Which Meta ads lose or make money

Channel: Meta · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Which Meta ads lose or make money" (id: meta-ad-returns, Meta).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Reads Meta directly, so it is current to the hour, and puts every live ad set and ad that buys website sales against the brand's own money lines.
Each gets a verdict: losing, winning, watch, too early, or no keep line. It is the same read as the four-hourly ROI alerts and the Ad returns page.
Ad sets that send people to Amazon are left out and counted, because Meta cannot see their sales.

What to read: Live Meta ad sets and ads that buy website sales, with spend and sales over the last 3 and 7 closed days, against the brand's own money lines
What to give me: Ad sets and ads losing money, ads ready for more budget, and what to watch, each with its cost per sale against the keep line

Synthesis tools to use:
- `meta_metric metric=ad_returns`

Steps:
1. Call `meta_metric` with `metric=ad_returns` and `limit=50`.
2. If it returns status error, stop: say the Meta read failed and to try again later. Never report it as no sales.
3. For any ad marked winning, name the ad set it should be copied into, and keep the original running.

Checks before answering:
- Use the verdicts as the server decided them. "Too early" is not losing.
- If the brand has no money lines, show spend, sales and cost per sale only, and say the lines need to be set. Never borrow another brand's lines.
- Say how many ad sets were left out as Amazon-bound.
- The windows are closed days ending yesterday. Today is not in it.

Output:
- One line first: spend, sales and cost per sale over 7 days, against the keep line.
- Losing: each ad set or ad, its spend, sales and the line it crossed, with one move.
- Ready for more budget: each ad with its cost per sale and sales.
- Watch: one line.
- Under 15 lines in total.

Never:
- Never change budgets or switch ads off. A person does that.
- Never call an Amazon-bound ad set losing on Meta's own sales.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: meta-ad-returns". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
