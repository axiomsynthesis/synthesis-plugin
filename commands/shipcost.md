---
description: "Is real shipping cost per box above what your profit numbers assume?: Real postage, packing and handling per box by pack and zone against the cost your profit numbers use, the dollars a month it moves, the corrected cost per box, and cheaper ways to ship sized in dollars"
argument-hint: "[anything to add for this run]"
disable-model-invocation: true
---

# Is real shipping cost per box above what your profit numbers assume?

Channel: Inventory · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Is real shipping cost per box above what your profit numbers assume?" (id: ops-shipping-cost-check, Inventory).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Checks the shipping cost your profit numbers use against what shipping really costs. It splits real cost into postage, packing and handling for each box by pack size, box type and zone, and sets each against the cost you gave. It sizes the gap in dollars a month, gives the corrected cost per box, and sizes cheaper ways to ship. Every profit-per-order, break-even and page call rides on this number.

What to read: Your warehouse's shipment file or invoices, the shipping cost your profit numbers use, any per-box cost you gave us, and where your website orders ship to
What to give me: Real postage, packing and handling per box by pack and zone against the cost your profit numbers use, the dollars a month it moves, the corrected cost per box, and cheaper ways to ship sized in dollars

Synthesis tools to use:
- `cost_rules for=ops-shipping-cost-check`
- `brand_facts query=shipping`
- `list_files`
- `search_file_content query=shipping`
- `shopify_metric metric=profit month=YYYY-MM`
- `shopify_metric metric=daily_revenue days=28`
- `shopify_metric metric=state_revenue`
- `first_order_contribution_margin`

Steps:
1. Call `cost_rules` first, as the rules say.
2. The cost your profit uses: call `shopify_metric` with `metric=profit` and `month=` set to last month, and read `shipping_rate` (per order, accounts, window). If it is the books average, say so: it is booked shipping divided by orders, not a box cost. Then `brand_facts` with `query=shipping` for any per-pack cost the owner gave. If none, ask for postage, packing and handling per box for each pack. Never guess one.
3. The real cost: call `list_files` and `search_file_content` with `query=shipping` for a shipment file or invoice. If `search_file_content` times out, say the search could not finish and rely on `list_files`; never report "no file" from a timeout. If none, ask for the warehouse's last 30 to 60 days of shipments with zone, or its invoice. Read postage, packing, handling and surcharges per box.
4. Group boxes by pack size, box type and zone. Give each group's box count and average cost per part.
5. Books: the same `shopify_metric metric=profit` month gives the website shipping booked in the account named in `shipping_rate.accounts`. Books shipping for all channels mixes store freight and inbound: never compare it per box.
6. Boxes a month: call `shopify_metric` with `metric=daily_revenue` and `days=28`. Add orders another marketplace sent into the store to ship. Check the month's marketplace-sent boxes against the last 28 days' `offsite_orders`; if the run-rates differ by over 25%, size dollars a month on the newer one and say why. Say if the window holds a big sale (Prime, Black Friday).
7. Call `shopify_metric` with `metric=state_revenue` for where website orders go, so the zone mix holds beyond the file. Never use Amazon's customer map for boxes your warehouse ships.
8. Gap times boxes, by pack, is the dollars a month. Call `first_order_contribution_margin` with `price`, `cogs` and `misc` set to the real cost, to show what each pack keeps.
9. Size cheaper options with the file's own numbers: a smaller box or lower weight band, a slower service, shipping from a second warehouse closer to most buyers, a free-shipping minimum, or shipping charged to the shopper.
10. The fix: the corrected cost per box for each pack. If `cost_rules` asks how to count website shipping, propose an answer. Save it with `set_cost_rule` only after the owner's yes.

Checks before answering:
- Like for like: postage against postage, handling against handling. A sheet line may hold packing that the invoice bills apart.
- Books may hold inbound freight, returns labels and marketplace-sent boxes. Say so before comparing.
- A file from a holiday peak carries surcharges. Say which weeks it covers.

Rounds (relook before you answer):
1. **Part by part.** Re-split each pack into postage, packing and handling. Fails when: one part is in one source and not the other. Fix: compare part by part.
2. **Zone mix.** Re-weight by the file's zone share, checked against step 7. Fails when: over half the boxes go to zones the sheet did not price. On one live brand 85% went far. Fix: price by the real mix.
3. **Books tie.** File total against the website shipping account for the same month (step 5). Fails when: they differ by over 5%. Fix: find the missing lines. No file: not run, since the cost your profit uses is the books' own number and cannot fail.
4. **Every box.** Fails when: boxes a month count website orders only while the file holds more. Fix: use the file's count.
5. **Second window.** Re-read another single month of the file, never a 12-month average. Fails when: a pack's gap moves over $1. Fix: name the rate change or surcharge, and use the later month.
6. **Full fix.** Fails when: the answer stops at the gap without corrected costs per pack, dollars a month and one cheaper option in dollars. Fix: add them.

Output:
- One line first: real cost per box against the sheet, the gap, and dollars a month.
- Table: pack | box type | zone share | sheet cost | real cost | gap | boxes a month | dollars a month.
- The corrected cost per pack, ready to save.
- Cheaper options, each with dollars a month and what it risks.
- With no file, rounds that need it say "not checked: no shipment file", never passed, and the answer gives what $1 a box moves a month.

Never:
- Never save a cost or answer a cost question without the owner's yes.
- Never change carrier, box or shipping settings.
- Never present booked shipping divided by orders as measured cost per box.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Before step 1, call cost_rules. If it returns questions, ask them in one message as written (dollars, choices, what skip does) and save each answer with set_cost_rule. On a scheduled run, use the defaults and list the questions at the end. End the answer with its used_line.
- This job is worked in rounds; the first pass is never the answer. First call recall_decisions and look for an earlier run of this job: if one exists, start from where it ended, not from zero. After the Steps, run every round in Rounds in order. Each round re-reads the data it needs, says what it found wrong and fixes the draft. Log one line per round: what changed and why, or 'no change' if its check passed. Never invent a change. Stop mid-way only for a choice only I can make. Show the final draft, then the round log, then 2 or 3 next rounds I could ask for. Treat my feedback as a new round: re-run every check it touches, and never quietly undo an earlier fix. At the end, save where this run stopped with log_decision so the next run picks it up.
- Read every number that drives the call in layers and over several windows, never one. Layers, where they apply: volume (orders, sales), then profit after every cost, then return on the money spent against break-even, then what a customer is worth later on profit. Windows by how fast the number moves: fast ones (clicks, buy rate, cost per sale) over the last 7 closed days and the 7 before; sales, spend and return over 28 days, never under 4 weeks; slow ones (repeat, lifetime value, share) over 90 days to 12 months, comparing only customers of the same age. Set each against the same weeks last year, not last week. Closed days only; a young cohort is unfinished, not low. Before calling a change, rule out a deal, a stock-out or a part month. Show one small grid: each key number by window, with return on spend. When windows disagree, say so plainly: a fall in a slow number outranks a wobble in a fast one, a trend needs 4 steady weeks, and mixed signals mean no clear signal yet, not a verdict.
- Before trusting a number, compare it the way an expert would. Against itself: its own usual level and the same weeks last year. Against its peers: the other products, ads, pages or channels doing the same job, ranked side by side. Against the line that matters: break-even and any goal the brand set. An outside benchmark only shows room to grow, never a grade. Against a control: a holdout, the page being beaten, or a past natural test such as a pause or a stock-out. Break every move into its parts (price times units times mix, or rate times count) and name the part that moved. Look at the spread, not just the average: the top and bottom few, and how much rides on one item. Size each finding in dollars a month. Name the number that would flip the call.
- Go deeper with the tools built for it, picking the ones this job needs and saying which you ran and which you skipped. Start from the map: brand_brain with action=what_matters, then action=links_here on the thing at hand to find what it is tied to, and action=explain_link to check a link was tested and is not chance. Incrementality: attribution_lenses to set what the platform claims beside what was likely extra, plus any past pause, stock-out or spend jump as a natural test; never treat a platform's own credit as extra sales. Models: media_response_model or diminishing_returns for what the next dollar returns; run_monte_carlo for a range of outcomes, never one point; run_bayesian when the sample is small; explain_metric_move for why a number moved; backtest_rule to check the call would have held in the brand's own past. List what is working and what is breaking, both sides. Check find_contradictions against earlier conclusions. Close every recommendation with measurable_test: the number, the date and the line that says it worked.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: ops-shipping-cost-check". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.

---

Anything the person typed after the shortcut is extra instruction for this run: $ARGUMENTS
