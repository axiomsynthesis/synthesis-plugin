# Check a promo's margin before you run it

Channel: Money · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Check a promo's margin before you run it" (id: ops-promo-margin-floor, Money).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Checks a planned deal or coupon before it goes live. It works out what each unit earns at the promo price and how many more units the promo must sell just to stand still, then compares that with how past promos actually did.

What to read: Price, Amazon fees, product cost and normal sales pace for the products in a planned promotion
What to give me: Profit per unit at the promo price, the extra units needed to break even, and whether it clears your floor

Synthesis tools to use:
- `amazon_metric metric=contribution_by_asin months=3`
- `first_order_contribution_margin asin=<asin> price=<promo_price>`
- `amazon_metric metric=promotion_performance months=12 limit=20`
- `amazon_metric metric=velocity_momentum`

Steps:
1. Ask for the promo: products, discount, dates, and the margin floor if one is set.
2. Call `amazon_metric metric=contribution_by_asin months=3` for normal price, fees, product cost and units.
3. Run `first_order_contribution_margin asin=<asin> price=<promo_price>` for each product. Referral fees fall with price; fulfilment fees do not.
4. Break-even lift = normal profit per unit divided by promo profit per unit.
5. Call `amazon_metric metric=promotion_performance months=12 limit=20` and `amazon_metric metric=velocity_momentum` to find the lift past promos of similar depth delivered.
6. Compare the break-even lift with past lift. If past lift is lower, say the promo likely loses money unless its new buyers repeat, and state the repeat needed.

Checks before answering:
- Use normal weeks for the base pace. Leave out past deal weeks and stockout weeks.
- Past lift from a big event (Prime Day and similar) is not comparable to an ordinary week. Match like with like.
- A product without cost cannot be checked. Say so.
- Fees at the promo price must be recomputed, not copied from the full-price month.

Output:
- Table: Product | Profit per unit normal | Profit per unit on promo | Break-even lift | Past lift at this depth | Verdict.
- Two lines: the expected profit or loss of the promo, and the discount depth that would break even.

Never:
- Never create, change or cancel a promotion.
- Never count promo sales as all incremental.
- Never use a guessed lift. If no past promo matches, say so.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: ops-promo-margin-floor". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
