---
description: "Where your email flows lose people: The flow steps that lose readers or earn nothing, and the step to rewrite"
argument-hint: "[anything to add for this run]"
disable-model-invocation: true
---

# Where your email flows lose people

Channel: Email · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Where your email flows lose people" (id: grw-email-flow-step-leak, Email).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Reads each automated flow step by step: welcome, abandoned cart, browse, post-purchase and win-back. It finds the step where clicks or orders fall off a cliff and the steps that earn nothing.

What to read: Klaviyo flow step results from first email to last
What to give me: The flow steps that lose readers or earn nothing, and the step to rewrite

Synthesis tools to use:
- `klaviyo_metric metric=flow_funnel`
- `klaviyo_metric metric=flow_step_performance limit=60`
- `shopify_metric metric=time_to_repeat`

Steps:
1. Pull `klaviyo_metric metric=flow_funnel`.
2. Pull `klaviyo_metric metric=flow_step_performance limit=60`.
3. Put each flow's steps in their real order. Use the email names or templates first, and the number of people reached only when they say nothing.
4. For each flow, compute click rate and placed-order rate per step from summed counts. Give each rate a 95% range, using the Wilson method for a share. Flag a step only when its range sits fully below the step before. Otherwise say there are too few sends to tell, and about how many more sends would settle it.
5. Flag steps with fewer than 1 order per 1,000 delivered only when the range backs it.
6. Name one rewrite or removal per flagged step. List common flows that are missing, such as win-back, browse abandon or running low, with when each last sent.
7. For after-purchase flows, call `shopify_metric` with `metric=time_to_repeat`. A running-low email should land about two weeks before the typical reorder, and each email should offer one size up from what was bought.

Checks before answering:
- Open rates are inflated by Apple's privacy auto-opens. Judge on clicks and placed orders, never on opens alone.
- Klaviyo revenue is last-touch credit on website orders. It cannot see Amazon orders. Never call it email's total effect.
- Flow numbers cover recent sends, up to the last 12 months, not a fixed window. Say so.
- Say when the step order is a guess made from how many people each email reached.
- Later steps reach fewer people because some already bought or left. Compare a step only with the step before it, among people sent both.
- Say how many orders each verdict rests on, and call anything under 10 orders a hint, not a result.

Rounds (relook before you answer):
1. **Real step order.** Re-check each flow's order from email names and templates. Fails when: a flagged step's place came only from how many people it reached. Fix: mark the verdict a guess or drop it.
2. **The range backs the flag.** Re-work each flagged step's 95% range. Fails when: it overlaps the step before, or the step rests on under 10 orders. Fix: downgrade to "too few sends" with the sends needed.
3. **Timing against reorders.** Compare running-low and reorder emails with `time_to_repeat`. Fails when: the running-low email lands after the typical reorder day, or more than 4 weeks before it. Fix: name the new delay.
4. **Missing flows are really missing.** Fails when: a flow called missing shows sends in the last 60 days under another name. Fix: take it off the missing list.
5. **Claims in the step to rewrite.** Read the flagged emails' text. Fails when: one carries a disease or medical claim. Fix: put that first among the rewrites, since it cannot be pulled back once sent.

Output:
- Answer first: the one step that is truly leaking, or that no step has enough sends to call, and the biggest missing flow.
- Table with columns flow, step, delivered, orders, order rate with its range, problem, move.
- One move: switch on a 10% held-back group in each flow, who get no email, and read extra website orders after 30 days. Name the read date. Say that a discount in the first welcome email may pay buyers who would have ordered anyway.

Never:
- Nothing changes in any live account. A person on your team makes every change.
- Never fill a missing, gated or empty number with an estimate. Say what is missing and why.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- This job is worked in rounds; the first pass is never the answer. First call recall_decisions and look for an earlier run of this job: if one exists, start from where it ended, not from zero. After the Steps, run every round in Rounds in order. Each round re-reads the data it needs, says what it found wrong and fixes the draft. Log one line per round: what changed and why, or 'no change' if its check passed. Never invent a change. Stop mid-way only for a choice only I can make. Show the final draft, then the round log, then 2 or 3 next rounds I could ask for. Treat my feedback as a new round: re-run every check it touches, and never quietly undo an earlier fix. At the end, save where this run stopped with log_decision so the next run picks it up.
- Read every number that drives the call in layers and over several windows, never one. Layers, where they apply: volume (orders, sales), then profit after every cost, then return on the money spent against break-even, then what a customer is worth later on profit. Windows by how fast the number moves: fast ones (clicks, buy rate, cost per sale) over the last 7 closed days and the 7 before; sales, spend and return over 28 days, never under 4 weeks; slow ones (repeat, lifetime value, share) over 90 days to 12 months, comparing only customers of the same age. Set each against the same weeks last year, not last week. Closed days only; a young cohort is unfinished, not low. Before calling a change, rule out a deal, a stock-out or a part month. Show one small grid: each key number by window, with return on spend. When windows disagree, say so plainly: a fall in a slow number outranks a wobble in a fast one, a trend needs 4 steady weeks, and mixed signals mean no clear signal yet, not a verdict.
- Before trusting a number, compare it the way an expert would. Against itself: its own usual level and the same weeks last year. Against its peers: the other products, ads, pages or channels doing the same job, ranked side by side. Against the line that matters: break-even and any goal the brand set. An outside benchmark only shows room to grow, never a grade. Against a control: a holdout, the page being beaten, or a past natural test such as a pause or a stock-out. Break every move into its parts (price times units times mix, or rate times count) and name the part that moved. Look at the spread, not just the average: the top and bottom few, and how much rides on one item. Size each finding in dollars a month. Name the number that would flip the call.
- Go deeper with the tools built for it, picking the ones this job needs and saying which you ran and which you skipped. Start from the map: brand_brain with action=what_matters, then action=links_here on the thing at hand to find what it is tied to, and action=explain_link to check a link was tested and is not chance. Incrementality: attribution_lenses to set what the platform claims beside what was likely extra, plus any past pause, stock-out or spend jump as a natural test; never treat a platform's own credit as extra sales. Models: media_response_model or diminishing_returns for what the next dollar returns; run_monte_carlo for a range of outcomes, never one point; run_bayesian when the sample is small; explain_metric_move for why a number moved; backtest_rule to check the call would have held in the brand's own past. List what is working and what is breaking, both sides. Check find_contradictions against earlier conclusions. Close every recommendation with measurable_test: the number, the date and the line that says it worked.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: grw-email-flow-step-leak". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.

---

Anything the person typed after the shortcut is extra instruction for this run: $ARGUMENTS
