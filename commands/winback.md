---
description: "Win back customers who stopped buying: Lapsed website customers by value, a held-back test group, an affordable offer, a contact list and email drafts"
argument-hint: "[anything to add for this run]"
disable-model-invocation: true
---

# Win back customers who stopped buying

Channel: Customers · Level: Prepare · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Win back customers who stopped buying" (id: customers-win-back-list-and-email, Customers).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Finds repeat website customers who have not ordered in 3 to 12 months. It splits them into groups by value, holds some back as a test group, caps each offer at what the group can afford, and drafts one email per group. A person uploads the list to the email tool and sends.

What to read: Shopify orders, website profit, Klaviyo
What to give me: Lapsed website customers by value, a held-back test group, an affordable offer, a contact list and email drafts

Synthesis tools to use:
- `cost_rules for=customers-win-back-list-and-email`
- `shopify_metric metric=time_to_repeat`
- `shopify_metric metric=winback_candidates`
- `shopify_metric metric=profit`
- `klaviyo_metric metric=flow_funnel`
- `brand_facts`

Steps:
1. Call `shopify_metric` with `metric=time_to_repeat` for how long customers usually wait between orders. Give the share of repeat orders within 60 days and the typical gap. Twice the typical gap is the point a customer is likely lapsed. The list in step 2 uses a fixed 90 to 365 days. Say if twice the gap is well under 90 days, because lapsed customers are then missing from the list.
2. Call `shopify_metric` with `metric=winback_candidates`. Size each group from `tiers`, which covers every customer. The rows shown are only the top of the list.
3. Call `shopify_metric` with `metric=profit` for the last closed month. Profit divided by orders is what one order keeps. The deepest affordable discount is that amount times the share who would not come back without the offer. Show it at 25% and 50%, since that share is not measured yet.
4. Call `klaviyo_metric` with `metric=flow_funnel` to see whether a win-back email series has sent recently. It covers recent sends only.
5. Only if the person who will send asks for the contact file, call again with `export=true`. Tell them to move every row whose `customer_ref` ends in 0, 1 or 2 to a held-back sheet before uploading. That is about one in five, picked at random. Those people get no email.
6. Write one short email per group into `winback_emails.md`: subject, preview line, body, offer. If you can save files here, save it and tell me its name. If not, show it in full.

Checks before answering:
- If a win-back series already sends, say so. Do not double-mail the same people.
- If the order read is empty, say it could not be read. Never ship an empty list as "nobody lapsed".
- The tool's expected return rates are fixed numbers, not measured on these customers. Never show them. The held-back group is how the real rate gets measured.
- Past spend is lifetime spend, not yearly. Say so. The list cannot show the last 12 months yet.
- The list cannot yet tell subscribers from one-time buyers, or drop people now buying on Amazon. Say so. A lapsed subscriber needs a skip or longer-plan offer, not a discount.
- Never offer more than the affordable discount from step 3. If profit is missing or gated, say the offer cannot be sized.
- The download link holds customer emails. Hand it only to the person who will send the email.

Rounds (relook before you answer):
1. **Lapse window.** Re-read step 1. Fails when: twice the typical gap is under 60 days or over 365. Fix: say the fixed 90 to 365 day list misses or over-includes people, and roughly how many.
2. **Held back.** Fails when: the held-back share is under 15%, or it was picked by value instead of the `customer_ref` rule. Fix: redo the split by the rule.
3. **Offer cap.** Re-check every offer against step 3 at a 25% share won back. Fails when: any offer costs more per order than that cap. Fix: swap it for a free extra or a size up, which most brands afford better than a percent off.
4. **Double mail.** Re-read `klaviyo_metric` with `metric=flow_funnel`. Fails when: a win-back series sent in the last 30 days. Fix: hold this send or drop those people.
5. **Claim check.** Call `brand_facts` for every claim in the emails. Fails when: an email states a health result no fact backs. Fix: cut it.
6. **Read date.** Fails when: the answer has no read date and no gap target. Fix: set the read at 30 days, and judge only the gap between emailed and held back.

Output:
- One line first: how many customers lapsed, the offer cap per order, and the read date 30 days after sending.
- A table: group, customers, average lifetime spend, days since last order, offer, affordable discount.
- The held-back rule, and the download link if asked for.
- A file named `winback_emails.md` with one short email per group.
- At the read date, compare the return rate of the emailed and held-back groups. Only the gap counts as won back.

Never:
- Never send an email or create a Klaviyo list or flow. A person does that.
- Never offer a discount deeper than the group can afford.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Before step 1, call cost_rules. If it returns questions, ask them in one message as written (dollars, choices, what skip does) and save each answer with set_cost_rule. On a scheduled run, use the defaults and list the questions at the end. End the answer with its used_line.
- This job is worked in rounds; the first pass is never the answer. First call recall_decisions and look for an earlier run of this job: if one exists, start from where it ended, not from zero. After the Steps, run every round in Rounds in order. Each round re-reads the data it needs, says what it found wrong and fixes the draft. Log one line per round: what changed and why, or 'no change' if its check passed. Never invent a change. Stop mid-way only for a choice only I can make. Show the final draft, then the round log, then 2 or 3 next rounds I could ask for. Treat my feedback as a new round: re-run every check it touches, and never quietly undo an earlier fix. At the end, save where this run stopped with log_decision so the next run picks it up.
- Read every number that drives the call in layers and over several windows, never one. Layers, where they apply: volume (orders, sales), then profit after every cost, then return on the money spent against break-even, then what a customer is worth later on profit. Windows by how fast the number moves: fast ones (clicks, buy rate, cost per sale) over the last 7 closed days and the 7 before; sales, spend and return over 28 days, never under 4 weeks; slow ones (repeat, lifetime value, share) over 90 days to 12 months, comparing only customers of the same age. Set each against the same weeks last year, not last week. Closed days only; a young cohort is unfinished, not low. Before calling a change, rule out a deal, a stock-out or a part month. Show one small grid: each key number by window, with return on spend. When windows disagree, say so plainly: a fall in a slow number outranks a wobble in a fast one, a trend needs 4 steady weeks, and mixed signals mean no clear signal yet, not a verdict.
- Before trusting a number, compare it the way an expert would. Against itself: its own usual level and the same weeks last year. Against its peers: the other products, ads, pages or channels doing the same job, ranked side by side. Against the line that matters: break-even and any goal the brand set. An outside benchmark only shows room to grow, never a grade. Against a control: a holdout, the page being beaten, or a past natural test such as a pause or a stock-out. Break every move into its parts (price times units times mix, or rate times count) and name the part that moved. Look at the spread, not just the average: the top and bottom few, and how much rides on one item. Size each finding in dollars a month. Name the number that would flip the call.
- Go deeper with the tools built for it, picking the ones this job needs and saying which you ran and which you skipped. Start from the map: brand_brain with action=what_matters, then action=links_here on the thing at hand to find what it is tied to, and action=explain_link to check a link was tested and is not chance. Incrementality: attribution_lenses to set what the platform claims beside what was likely extra, plus any past pause, stock-out or spend jump as a natural test; never treat a platform's own credit as extra sales. Models: media_response_model or diminishing_returns for what the next dollar returns; run_monte_carlo for a range of outcomes, never one point; run_bayesian when the sample is small; explain_metric_move for why a number moved; backtest_rule to check the call would have held in the brand's own past. List what is working and what is breaking, both sides. Check find_contradictions against earlier conclusions. Close every recommendation with measurable_test: the number, the date and the line that says it worked.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: customers-win-back-list-and-email". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.

---

Anything the person typed after the shortcut is extra instruction for this run: $ARGUMENTS
