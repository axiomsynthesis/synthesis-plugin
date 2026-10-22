---
description: "Whole-business profit, every channel: Every channel side by side, ad spend and fixed costs, down to one net profit, with every missing cost named"
argument-hint: "[anything to add for this run]"
disable-model-invocation: true
---

# Whole-business profit, every channel

Channel: Money · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Whole-business profit, every channel" (id: money-whole-business-profit, Money).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Puts every channel on one page for one month: Amazon, the website, TikTok Shop, Walmart, stores and wholesale. Each shows its sales and its profit after its own costs. Ad spend that cannot be pinned to one store sits in its own row. Your fixed costs come off last, down to one net profit. Every channel or cost with no data is named, so the net is never read as more complete than it is.

What to read: Every sales channel's profit as the Profit page counts it, ad spend by platform, and your entered fixed costs
What to give me: Every channel side by side, ad spend and fixed costs, down to one net profit, with every missing cost named

Synthesis tools to use:
- `cost_rules for=money-whole-business-profit`
- `business_profit month=YYYY-MM`
- `amazon_metric metric=pnl_waterfall month=YYYY-MM`
- `netsuite_metric metric=vendor_spend limit=20`

Steps:
1. Call `business_profit` with `month=` set to last month.
2. Read `data_quality_flags` before anything else. Sort them into three groups: channels left out, channels with sales but no profit yet, and costs not counted.
3. Read `columns`. List each sales channel with its sales, profit and margin, then each ad platform's spend.
4. Read `ads_by_destination` and `channels_after_ads`. For each channel give its profit after the ad spend pointing at it. Show `unallocated` (another store's shelf, no known destination) as its own row. If `channels_after_ads.withheld` is true, say the ad split did not add back and use the before-ads table only.
5. Read `books_tie`. If `checked` is true, give net sales here, the books' net revenue and the gap. If `ok` is false, say a channel or deduction is counted differently. Show the books' net income beside the net, never tied to it. If `checked` is false, say why.
6. Read `stopped_channels`. Name each one with the date of its last sale. Never call it not connected.
7. If Amazon is the largest channel and the month is still settling, call `amazon_metric` with `metric=pnl_waterfall` for the month before as well, and say which month is settled.
8. Read `fixed_costs`. None entered: ask for them. Net profit drops by every dollar. Not given: say net profit is before rent, salaries and software.
9. Stores and wholesale with sales but no product cost: ask what share of those sales it is. Show their profit with it, marked as your figure.

Checks before answering:
- If `gated` is true, there is no net to state. Give the reason.
- A channel with sales and no profit is not in the net. Say how much it sold, so the gap is visible.
- Only move ad spend to a channel through `channels_after_ads`. Never add a whole platform's spend to one channel.
- A margin above 70% on a product channel almost always means a missing cost. Say so beside it.
- Use a closed month.

Rounds (relook before you answer):
1. **Cost gap in the first line.** Re-read `total.product_cost_missing_pct_of_sales` and every flag. Fails when: any sales lack a cost or a channel is held out, and the first line does not say "product cost missing for X% of sales" and name the held-out sales. Fix: put both in the first line. Never blank the net.
2. **Every bill once.** Call `netsuite_metric metric=vendor_spend limit=20` and set each agency, influencer or marketing firm bill beside the columns and the cost rules used. Fails when: such a bill of $500 or 0.5% of sales or more is in no column and no ruling, or affiliate pay is counted both as billed and as reported. Fix: ask whether to count it, with the dollars, and show the net both ways until they answer.
3. **Same orders twice.** Fails when: orders another marketplace sent into the store are also in stores and wholesale, or `books_tie` is off by more than 2%. Fix: name the overlap in dollars and keep it on one side only.
4. **Settled, not in flight.** Fails when: `period.in_flight` is true or Amazon's month is still settling. Fix: lead with the last closed month and call the other an estimate.
5. **What moved since last time.** Set the net beside the last run, or call `business_profit` for the month before. Fails when: the net moved more than 15% and the lines you name explain under 80% of it. Fix: add the lines, and call the rest unexplained.
6. **Losing channels after ads.** Fails when: a channel's profit after the ads pointing at it is below zero and it is not the second line. Fix: say what it lost and the ad dollars behind it.

Output:
- One line first: net profit for the month, its share of sales, and how many channels or costs are missing.
- A table: channel, sales, profit before ads, profit after the ads pointing at it, margin, what is not counted.
- Two lines: the channel that makes the most per dollar of sales after its own ads, and the one missing cost that would change the net most.
- One line: the tie to the books, or why there is none.
- One move: the cost to enter or the feed to connect first.

Never:
- Never fill a missing channel or cost with an estimate of your own.
- Never call the net complete while a flag says otherwise.
- Never move budget between channels. A person does that.
- Never add a bill from the books on top of a line the page already counts, such as display ads or affiliate pay.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Before step 1, call cost_rules. If it returns questions, ask them in one message as written (dollars, choices, what skip does) and save each answer with set_cost_rule. On a scheduled run, use the defaults and list the questions at the end. End the answer with its used_line.
- Inputs only I know: fixed costs a month (rent, salaries, software); product cost for store and wholesale sales, as a share of them. If the tools lack one, ask me ONE plain question for it, all in one message: why it matters and about how many dollars it moves. Use my answer for this run. Never invent one. If I do not know, say what the answer leaves out. Then tell me to save fixed costs on the Dashboard, All channels, Fixed costs box. Nothing saves store and wholesale cost yet: say it was used for this run only. On a scheduled run, name what is missing instead.
- This job is worked in rounds; the first pass is never the answer. First call recall_decisions and look for an earlier run of this job: if one exists, start from where it ended, not from zero. After the Steps, run every round in Rounds in order. Each round re-reads the data it needs, says what it found wrong and fixes the draft. Log one line per round: what changed and why, or 'no change' if its check passed. Never invent a change. Stop mid-way only for a choice only I can make. Show the final draft, then the round log, then 2 or 3 next rounds I could ask for. Treat my feedback as a new round: re-run every check it touches, and never quietly undo an earlier fix. At the end, save where this run stopped with log_decision so the next run picks it up.
- Read every number that drives the call in layers and over several windows, never one. Layers, where they apply: volume (orders, sales), then profit after every cost, then return on the money spent against break-even, then what a customer is worth later on profit. Windows by how fast the number moves: fast ones (clicks, buy rate, cost per sale) over the last 7 closed days and the 7 before; sales, spend and return over 28 days, never under 4 weeks; slow ones (repeat, lifetime value, share) over 90 days to 12 months, comparing only customers of the same age. Set each against the same weeks last year, not last week. Closed days only; a young cohort is unfinished, not low. Before calling a change, rule out a deal, a stock-out or a part month. Show one small grid: each key number by window, with return on spend. When windows disagree, say so plainly: a fall in a slow number outranks a wobble in a fast one, a trend needs 4 steady weeks, and mixed signals mean no clear signal yet, not a verdict.
- Before trusting a number, compare it the way an expert would. Against itself: its own usual level and the same weeks last year. Against its peers: the other products, ads, pages or channels doing the same job, ranked side by side. Against the line that matters: break-even and any goal the brand set. An outside benchmark only shows room to grow, never a grade. Against a control: a holdout, the page being beaten, or a past natural test such as a pause or a stock-out. Break every move into its parts (price times units times mix, or rate times count) and name the part that moved. Look at the spread, not just the average: the top and bottom few, and how much rides on one item. Size each finding in dollars a month. Name the number that would flip the call.
- Go deeper with the tools built for it, picking the ones this job needs and saying which you ran and which you skipped. Start from the map: brand_brain with action=what_matters, then action=links_here on the thing at hand to find what it is tied to, and action=explain_link to check a link was tested and is not chance. Incrementality: attribution_lenses to set what the platform claims beside what was likely extra, plus any past pause, stock-out or spend jump as a natural test; never treat a platform's own credit as extra sales. Models: media_response_model or diminishing_returns for what the next dollar returns; run_monte_carlo for a range of outcomes, never one point; run_bayesian when the sample is small; explain_metric_move for why a number moved; backtest_rule to check the call would have held in the brand's own past. List what is working and what is breaking, both sides. Check find_contradictions against earlier conclusions. Close every recommendation with measurable_test: the number, the date and the line that says it worked.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: money-whole-business-profit". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.

---

Anything the person typed after the shortcut is extra instruction for this run: $ARGUMENTS
