# Cash for the next 13 weeks

Channel: Money · Level: Prepare · Status: Ready after we build it

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Cash for the next 13 weeks" (id: ops-13-week-cash-forecast, Money).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Builds the weekly cash view a finance lead uses to avoid surprises: what comes in, what goes out, and the lowest point over the next quarter. It is different from runway, which is months of cash at an average burn. This one finds the specific week that gets tight.

What to read: Cash on hand, expected marketplace payouts, card payouts, purchase order payments and operating costs
What to give me: Week-by-week cash in, cash out and ending balance, with the tightest week named

Synthesis tools to use:
- `cost_rules for=ops-13-week-cash-forecast`
- `operator_inputs section=cash`
- `operator_inputs section=purchase_orders`
- `amazon_metric metric=daily_settled_revenue days=90`
- `recharge_metric metric=upcoming_charges weeks=13`
- `netsuite_metric metric=opex_category months=3 limit=20`
- `export_xlsx filename=13-week-cash.xlsx`

Steps:
1. Call `operator_inputs section=cash` for the opening cash balance and the entered 30-day cash flow.
2. Call `operator_inputs section=purchase_orders` for open orders, amounts and dates. Ask for deposit and balance terms; they are not stored.
3. Call `amazon_metric metric=daily_settled_revenue days=90` to set the expected payout size per two-week cycle.
4. If a subscription app is connected, call `recharge_metric metric=upcoming_charges weeks=13` for expected subscription billing.
5. Call `netsuite_metric metric=opex_category months=3 limit=20` and divide by three for the monthly operating cost run rate. Spread payroll and rent on their real dates when the person gives them.
6. Lay out 13 weeks: opening cash, each inflow, each outflow, closing cash. Write it with `export_xlsx filename=13-week-cash.xlsx`.

Checks before answering:
- Opening cash must come from an entry dated within the last 7 days. Older than that, ask for today's balance.
- Every payment term not entered is an assumption. Mark each assumed row in the sheet and in the chat summary.
- Amazon holds a reserve and pays in cycles. Never treat daily sales as daily cash.
- A missing source is a blank row named "not connected", never a zero.

Output:
- Spreadsheet with tabs: Weekly view, Assumptions, Sources.
- In chat: the lowest week and its balance, the item driving it, and one move that fixes it.

Never:
- Never move money, draw on a line or change a payment date.
- Never present the forecast as measured. It is a plan built on stated assumptions.
- Never use the accounting ledger's cash movement as a cash balance.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Before step 1, call cost_rules. If it returns questions, ask them in one message as written (dollars, choices, what skip does) and save each answer with set_cost_rule. On a scheduled run, use the defaults and list the questions at the end. End the answer with its used_line.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: ops-13-week-cash-forecast". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.

Not fully ready yet (ready after we build it): Synthesis holds entered cash, purchase orders, Amazon settlements and subscription charges, but not supplier payment terms, a payables schedule, the Amazon payout calendar with reserves, or card processor payouts (the Stripe and PayPal data lands but has no reader tool). Needs a payout-schedule tool, a card-payout reader, and a place to enter payment terms. Do the parts you can and say plainly what is missing.
