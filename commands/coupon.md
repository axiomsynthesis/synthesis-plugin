---
description: "Is this Walmart store coupon worth running again?: Cost per redemption against gross profit per unit, the extra units the offer really added, and a run-again, resize or stop verdict"
argument-hint: "[anything to add for this run]"
disable-model-invocation: true
---

# Is this Walmart store coupon worth running again?

Channel: Retail · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Is this Walmart store coupon worth running again?" (id: judge-walmart-store-coupon, Retail).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Judges an in-store coupon or cash-back offer at Walmart, or a Meta ad push aimed at Walmart, before you pay for more. It compares what each redemption cost with the profit on each unit, and checks whether the offer added sales or only paid people who would have bought anyway.

What to read: Walmart store weekly sales files, the coupon or cash-back invoices, product cost, Walmart's cost price, and Meta spend aimed at Walmart
What to give me: Cost per redemption against gross profit per unit, the extra units the offer really added, and a run-again, resize or stop verdict

Synthesis tools to use:
- `list_files`
- `search_files query=coupon`
- `read_file`
- `gsheets_metric metric=tables`
- `gsheets_metric metric=profile`
- `gsheets_metric metric=trend`
- `operator_inputs section=cogs`

Steps:
1. Ask: the offer, the item, the value per redemption, the cap, the dates, and Walmart's cost price per unit (what Walmart pays you). No tool holds that price.
2. Call `list_files`, then `search_files` with `query=coupon`, `query=walmart`, `query=retail campaign tracker` and the offer company's name. Call `read_file` on the offer invoices and the store weekly sales files.
3. Hard stop. The offer invoice and the store weekly sales file (units by item by week, 8 weeks before to 4 weeks after) must both be on file. If either is missing, ask for it and stop here. Do not go on to step 4. If the tracker sheet shows a push on the same items those weeks, say so before they upload. The result will not split.
4. If the brand keeps store sales in a sheet, call `gsheets_metric` with `metric=tables`. Tables come in pages, so search_files first and match the name. Call `metric=profile` on the hit for its date column, then `metric=trend`.
5. Remove duplicate rows before adding up. Store files can split one item across several rows. Count a row once per week, item and store category line.
6. Take 8 weeks before the offer as the baseline. Compare units in the offer weeks and in the 4 weeks after. Extra units are offer weeks minus baseline.
7. Call `operator_inputs` with `section=cogs` for product cost. It holds product cost only. Gross profit per unit is Walmart's cost price from step 1 minus product cost and any allowance.
8. Cost per redemption is the invoice total divided by redemptions. Split it into the reward the shopper got and the offer company's own fee per redemption: the fee can decide it. Then the share of redemptions that must be extra sales to break even is cost per redemption over gross profit per unit. Compare that share with what step 6 measured.
9. If two offers or pushes ran on the same items at once, the result cannot be split. Say so. Run offers solo.
10. For a Meta push aimed at Walmart, the spend sits in the agency's tracker sheet from step 2, not in Meta's weekly spend split, which covers Amazon and website only. Compare the push weeks with store units the same way.
11. Verdict: run again, resize the cap, or stop. On one live brand, $5.25 to $7.31 per redemption was the range that paid.

Checks before answering:
- Safe test: this only reads. Nothing in Walmart or the offer app changes.
- Spend: state the offer's total cost and the cap. A cap set too high pays for redemptions you did not need.
- Totals must tie to the store sales file. If they do not, say by how much.
- If product cost or Walmart's cost price is missing, give cost per redemption only. Never call it profitable.
- Ask for the lowest price held on other channels. Say if a deeper offer would break it.
- Online marketplace sales are a different channel from store sales. Never mix them.

Rounds (relook before you answer):
1. **Fully loaded cost.** Fails when: gross profit per unit used product cost alone. Fix: ask for boxes, freight in and warehousing per unit, add them, and redo step 8. Leaving them out understated one live brand's coupon bite by about 10 points.
2. **Break-even share.** Fails when: the share of redemptions that must be extra sales, from step 8, is above the extra units over redemptions measured in step 6. Fix: the verdict is resize or stop, never run again.
3. **Whole item, not one unit.** Work out redeemed units as a share of all units sold in the offer weeks. Fails when: the per-unit verdict and this whole-item view point different ways. Fix: lead with the whole-item dollars. On one live brand the per-unit view said the coupon took 88% of profit, the whole-item view said under 10%.
4. **National offer.** Fails when: invoice redemptions are over a third more than the extra Walmart units, and the item also sells at other stores. The offer is likely national. Fix: count only Walmart's share and say the split is an estimate.
5. **Clean weeks and ties.** Fails when: the tracker shows another push on the same items, or totals miss the store file by over 1%. Fix: say the result cannot be split, or by how much it misses.

Output:
- One line first: run again, resize or stop, with cost per redemption against profit per unit. Or the one file still missing.
- A table: offer, weeks, redemptions, cost, cost per redemption, extra units, profit per unit.
- What to change next time: cap, value, timing.

Never:
- Never book, change or cancel an offer. The team does that with Walmart or the offer company.
- Never count a redemption as an extra sale.
- Never judge an offer that overlapped another as if it ran alone.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- This job is worked in rounds; the first pass is never the answer. First call recall_decisions and look for an earlier run of this job: if one exists, start from where it ended, not from zero. After the Steps, run every round in Rounds in order. Each round re-reads the data it needs, says what it found wrong and fixes the draft. Log one line per round: what changed and why, or 'no change' if its check passed. Never invent a change. Stop mid-way only for a choice only I can make. Show the final draft, then the round log, then 2 or 3 next rounds I could ask for. Treat my feedback as a new round: re-run every check it touches, and never quietly undo an earlier fix. At the end, save where this run stopped with log_decision so the next run picks it up.
- Read every number that drives the call in layers and over several windows, never one. Layers, where they apply: volume (orders, sales), then profit after every cost, then return on the money spent against break-even, then what a customer is worth later on profit. Windows by how fast the number moves: fast ones (clicks, buy rate, cost per sale) over the last 7 closed days and the 7 before; sales, spend and return over 28 days, never under 4 weeks; slow ones (repeat, lifetime value, share) over 90 days to 12 months, comparing only customers of the same age. Set each against the same weeks last year, not last week. Closed days only; a young cohort is unfinished, not low. Before calling a change, rule out a deal, a stock-out or a part month. Show one small grid: each key number by window, with return on spend. When windows disagree, say so plainly: a fall in a slow number outranks a wobble in a fast one, a trend needs 4 steady weeks, and mixed signals mean no clear signal yet, not a verdict.
- Before trusting a number, compare it the way an expert would. Against itself: its own usual level and the same weeks last year. Against its peers: the other products, ads, pages or channels doing the same job, ranked side by side. Against the line that matters: break-even and any goal the brand set. An outside benchmark only shows room to grow, never a grade. Against a control: a holdout, the page being beaten, or a past natural test such as a pause or a stock-out. Break every move into its parts (price times units times mix, or rate times count) and name the part that moved. Look at the spread, not just the average: the top and bottom few, and how much rides on one item. Size each finding in dollars a month. Name the number that would flip the call.
- Go deeper with the tools built for it, picking the ones this job needs and saying which you ran and which you skipped. Start from the map: brand_brain with action=what_matters, then action=links_here on the thing at hand to find what it is tied to, and action=explain_link to check a link was tested and is not chance. Incrementality: attribution_lenses to set what the platform claims beside what was likely extra, plus any past pause, stock-out or spend jump as a natural test; never treat a platform's own credit as extra sales. Models: media_response_model or diminishing_returns for what the next dollar returns; run_monte_carlo for a range of outcomes, never one point; run_bayesian when the sample is small; explain_metric_move for why a number moved; backtest_rule to check the call would have held in the brand's own past. List what is working and what is breaking, both sides. Check find_contradictions against earlier conclusions. Close every recommendation with measurable_test: the number, the date and the line that says it worked.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: judge-walmart-store-coupon". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.

---

Anything the person typed after the shortcut is extra instruction for this run: $ARGUMENTS
