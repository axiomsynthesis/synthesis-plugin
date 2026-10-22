---
description: "Is all your marketing paying, together?: Your whole-business return on ad spend by month, and marketing as a share of sales"
argument-hint: "[anything to add for this run]"
disable-model-invocation: true
---

# Is all your marketing paying, together?

Channel: Growth · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Is all your marketing paying, together?" (id: grw-blended-mer-trend, Growth).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Ignores what each platform claims and asks one question: for every dollar of ads, how many dollars of total sales came in. It tracks that month by month with marketing as a share of sales.

What to read: Total sales and total ad spend by month across Meta, Google, TikTok and Amazon ads
What to give me: Your whole-business return on ad spend by month, and marketing as a share of sales

Synthesis tools to use:
- `cost_rules for=grw-blended-mer-trend`
- `mer month=<YYYY-MM>`
- `new_to_brand_customers month=<YYYY-MM>`
- `business_profit month=YYYY-MM`

Steps:
1. For each of the last 12 closed months, run `mer`.
2. Read spend by channel from each result's `ad_channels`. Every ad leg is already there with its amount and status, so do not call Meta, TikTok, Google or Amazon spend tools separately.
3. Read sales by channel from `sales_channels`, and `error_direction` for whether the missing legs make the month read high or low.
4. For each month, call `new_to_brand_customers` and divide Amazon ad spend by it for Amazon ad spend per new Amazon customer. Never add website new customers to it: they are a different channel and a different meaning of new.
5. Show spend mix by channel beside the efficiency number.

Checks before answering:
- If `mer` is gated for a month, do not state it. Give its reason.
- Count TikTok spend from both auction and shop ads.
- Google Ads campaign spend is kept only from where its history starts. Months before that show Google as not measured, never zero, and their total spend is labelled as excluding Google.
- If a month's return is withheld, show its `upper_bound_only` as a ceiling, labelled, never as the month's number.
- Leave the current month out.
- Amazon ad spend counts Sponsored Products, Brands and Display. A month before the brand's Amazon ad history begins shows Amazon ads as not measured, never zero.
- A channel whose status says missing may simply have sold nothing that month. If a sales leg reads zero or missing for a channel that stopped selling, say it stopped, and that the month does not read low because of it.
- Spend here leaves out creator and affiliate pay and agency fees. It may also leave out display ads bought through Amazon's separate display service, which on one live brand was the size of a whole channel. Say total marketing is higher than shown, so the real return is lower.
- Amazon sales in the total are before discounts. Say the total reads high by those discounts.
- This answer gives no break-even line yet. The return that just pays for marketing is 1 divided by the business's margin before marketing. Round 2 reads it from `business_profit`. If that is gated or missing, say the number cannot be judged good or bad without it.
- New-customer sales per ad dollar is not available. The new-customer tools give counts, not sales. Show ad spend per new customer instead and say so.

Rounds (relook before you answer):
1. **Spend left out.** Ask for creator, affiliate and agency pay by month if not given. Fails when: it is over 10% of ad spend. Fix: add it and show the return both ways.
2. **Break-even.** Call `business_profit` with `month=` last month. Break-even is 1 over the margin before marketing. Fails when: last month's sales per ad dollar sit under it. Fix: lead with that.
3. **Same months last year.** Fails when: the month-to-month trend and the same months a year back point opposite ways. Fix: say the season drives it, and lead with the year-on-year read.
4. **Mix shift.** Fails when: one channel's share of spend moved over 10 points across the window. Fix: say the change may be mix, not efficiency.
5. **Settled.** Fails when: a counted month carries a partial-data or settling flag. Fix: drop it or label it as not settled.

Output:
- Answer first: is total marketing paying? Last month's sales per ad dollar, its trend, and whether it sits above or below break-even when that line is known.
- Table by month: total sales, total ad spend, efficiency, marketing share of sales, ad spend per new customer, spend mix.
- One line: the costs left out of spend, and which way they move the return.

Never:
- Nothing changes in any live account. A person on your team makes every change.
- Never fill a missing, gated or empty number with an estimate. Say what is missing and why.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Before step 1, call cost_rules. If it returns questions, ask them in one message as written (dollars, choices, what skip does) and save each answer with set_cost_rule. On a scheduled run, use the defaults and list the questions at the end. End the answer with its used_line.
- This job is worked in rounds; the first pass is never the answer. First call recall_decisions and look for an earlier run of this job: if one exists, start from where it ended, not from zero. After the Steps, run every round in Rounds in order. Each round re-reads the data it needs, says what it found wrong and fixes the draft. Log one line per round: what changed and why, or 'no change' if its check passed. Never invent a change. Stop mid-way only for a choice only I can make. Show the final draft, then the round log, then 2 or 3 next rounds I could ask for. Treat my feedback as a new round: re-run every check it touches, and never quietly undo an earlier fix. At the end, save where this run stopped with log_decision so the next run picks it up.
- Read every number that drives the call in layers and over several windows, never one. Layers, where they apply: volume (orders, sales), then profit after every cost, then return on the money spent against break-even, then what a customer is worth later on profit. Windows by how fast the number moves: fast ones (clicks, buy rate, cost per sale) over the last 7 closed days and the 7 before; sales, spend and return over 28 days, never under 4 weeks; slow ones (repeat, lifetime value, share) over 90 days to 12 months, comparing only customers of the same age. Set each against the same weeks last year, not last week. Closed days only; a young cohort is unfinished, not low. Before calling a change, rule out a deal, a stock-out or a part month. Show one small grid: each key number by window, with return on spend. When windows disagree, say so plainly: a fall in a slow number outranks a wobble in a fast one, a trend needs 4 steady weeks, and mixed signals mean no clear signal yet, not a verdict.
- Before trusting a number, compare it the way an expert would. Against itself: its own usual level and the same weeks last year. Against its peers: the other products, ads, pages or channels doing the same job, ranked side by side. Against the line that matters: break-even and any goal the brand set. An outside benchmark only shows room to grow, never a grade. Against a control: a holdout, the page being beaten, or a past natural test such as a pause or a stock-out. Break every move into its parts (price times units times mix, or rate times count) and name the part that moved. Look at the spread, not just the average: the top and bottom few, and how much rides on one item. Size each finding in dollars a month. Name the number that would flip the call.
- Go deeper with the tools built for it, picking the ones this job needs and saying which you ran and which you skipped. Start from the map: brand_brain with action=what_matters, then action=links_here on the thing at hand to find what it is tied to, and action=explain_link to check a link was tested and is not chance. Incrementality: attribution_lenses to set what the platform claims beside what was likely extra, plus any past pause, stock-out or spend jump as a natural test; never treat a platform's own credit as extra sales. Models: media_response_model or diminishing_returns for what the next dollar returns; run_monte_carlo for a range of outcomes, never one point; run_bayesian when the sample is small; explain_metric_move for why a number moved; backtest_rule to check the call would have held in the brand's own past. List what is working and what is breaking, both sides. Check find_contradictions against earlier conclusions. Close every recommendation with measurable_test: the number, the date and the line that says it worked.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: grw-blended-mer-trend". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.

---

Anything the person typed after the shortcut is extra instruction for this run: $ARGUMENTS
