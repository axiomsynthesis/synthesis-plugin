---
description: "Which Meta ads lose or make money: Ad sets and ads losing money, ads ready for more budget, and what to watch, each with its cost per sale against the most you can pay for a sale"
argument-hint: "[anything to add for this run]"
disable-model-invocation: true
---

# Which Meta ads lose or make money

Channel: Meta · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Which Meta ads lose or make money" (id: meta-ad-returns, Meta).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Reads Meta directly, so it is current to the hour, and puts every live ad set and ad that buys website sales against the brand's own money lines.
Each gets a verdict: losing, winning, fine, watch, too early, or no keep line. Fine means under the keep line, but not far enough under it to add budget. It is the same read as the four-hourly ROI alerts and the Ad returns page.
Ad sets that send people to Amazon are left out and counted, because Meta cannot see their sales.

What to read: Live Meta ad sets and ads that buy website sales, with spend and sales over the last 3 and 7 closed days, against the brand's own money lines
What to give me: Ad sets and ads losing money, ads ready for more budget, and what to watch, each with its cost per sale against the most you can pay for a sale

Synthesis tools to use:
- `cost_rules for=meta-ad-returns`
- `meta_metric metric=ad_returns`
- `meta_metric metric=creative_action_breakdown days=7`

Steps:
1. Call `meta_metric` with `metric=ad_returns` and `limit=50`.
2. If it returns status error, stop: say the Meta read failed and to try again later. Never report it as no sales.
3. For each winner, the move is to raise its own ad set budget by about 20%. Do not copy it into a big ad set, because a copy there competes with every ad and can get almost no spend. If its ad set is losing as a whole, move the ad into a small ad set of its own instead.
4. For each losing ad, call `meta_metric` with `metric=creative_action_breakdown`, `ad_id` set to that ad and `days=7`. Divide purchase value by purchases for its order value.

Checks before answering:
- Use the verdicts as the server decided them. "Too early" is not losing.
- If the brand has no money lines, show spend, sales and cost per sale only, and say the lines need to be set. Never borrow another brand's lines.
- Say how many ad sets were left out as Amazon-bound.
- The windows are closed days ending yesterday. Today is not in it.
- The verdicts judge cost per sale only. They ignore order size and margin. An ad at a high cost per sale with a big order can still make money, and a "fine" ad with a small order can lose. Say this when an order value is far from the others.
- A verdict on a handful of sales is shaky. On 4 sales the true cost per sale could be less than half or more than double. Say how many sales each losing call rests on.
- Ad sets switched off during the window are not in the totals, even if they spent. Say the totals cover live ad sets only.
- The order value comes from the synced table, which runs a day behind the live read. Say so. Ad sets get no order value here. Say that plainly.
- If the result says status ok, it is a full answer, even if it also carries a gated or no-data stamp.

Output:
- One line first: spend, sales and cost per sale over 7 days, against the keep line.
- Losing: each ad set or ad, its spend, sales, the line it crossed and its order value, with one move.
- Ready for more budget: each ad with its cost per sale, sales and the budget move from step 3.
- Watch: one line.
- Under 15 lines in total.

Never:
- Never change budgets or switch ads off. A person does that.
- Never call an Amazon-bound ad set losing on Meta's own sales.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Before step 1, call cost_rules. If it returns questions, ask them in one message as written (dollars, choices, what skip does) and save each answer with set_cost_rule. On a scheduled run, use the defaults and list the questions at the end. End the answer with its used_line.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: meta-ad-returns". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.

---

Anything the person typed after the shortcut is extra instruction for this run: $ARGUMENTS
