---
description: "Are your ads buying sales you'd get anyway?: Products where ads likely buy sales you would get anyway or cost more than they earn, with a test"
argument-hint: "[anything to add for this run]"
disable-model-invocation: true
---

# Are your ads buying sales you'd get anyway?

Channel: Amazon · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Are your ads buying sales you'd get anyway?" (id: mkt-amazon-ads-incrementality-by-product, Amazon).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
High ad-credited sales can mean ads are working. It can also mean ads are paying for buyers who were already looking for you, or bidding more than the product can afford.
This first checks which of the two fits this account. Then it shortlists products and sets up a small test to find out.

What to read: Ad-credited sales against total sales for each product, branded and non-branded ad spend, and organic sales over time
What to give me: Products where ads likely buy sales you would get anyway or cost more than they earn, with a test

Synthesis tools to use:
- `cost_rules for=mkt-amazon-ads-incrementality-by-product`
- `amazon_metric metric=ppc_branded_split start_date=YYYY-MM-DD end_date=YYYY-MM-DD`
- `amazon_metric metric=ppc_organic_vs_paid days=60 limit=30`
- `amazon_metric metric=breakeven_acos_ltv months=3 limit=30`
- `amazon_metric metric=velocity_momentum weeks=16 limit=30`
- `measurable_test`

Steps:
1. Call `amazon_metric metric=ppc_branded_split start_date=YYYY-MM-DD end_date=YYYY-MM-DD` for the 60 days ending 30 days ago, so ad-credited sales have landed. Say which dates you used. Note branded spend as a share of all ad spend.
2. Call `amazon_metric metric=ppc_organic_vs_paid days=60 limit=30`. Note each product's paid share of units, its `acos` (ad spend over ad-credited sales, as a fraction) and its spend.
3. Call `amazon_metric metric=breakeven_acos_ltv months=3 limit=30` for each product's first-order break-even ad cost share. It comes as a percent, so multiply `acos` by 100 before comparing.
4. Pick the test. If branded is 15% of spend or more, shortlist products with high paid share and heavy branded spend. If branded is under 15%, the waste is not on your own name: shortlist products whose `acos` is above break-even, largest spend first.
5. Call `amazon_metric metric=velocity_momentum weeks=16 limit=30` to look for past weeks when ads dropped and total units held.
6. Shortlist up to 3 products. For each, design one test with `measurable_test`: the cut, the window, and the total units level that would prove ads were needed.

Checks before answering:
- Organic units are total minus ad-credited. That is a floor, not a measurement. Say so.
- The branded split is account-wide. It cannot be read per product yet, so never write a branded share for one product.
- The product read cannot yet be set to a mature window. Its newest 30 days are still collecting ad-credited sales, so `acos` reads high and paid share reads low there. Say so.
- The momentum data has no ad spend beside it. A week where units held is a hint that ads dropped, not proof.
- A product with paid share over 100% means double counting across sizes. Read it at parent level instead.
- Promo weeks are flagged in the momentum data. Never use one as the "before" in a comparison.
- The test tool writes the plan in words. It cannot yet size the test from weekly swings in units, so say the thresholds are a judgment.
- Never call ads wasted on this read alone. It points to a test, not a verdict.

Output:
- One line: which problem this account has, branded buying or bids above break-even, how many products, and the monthly spend at stake.
- A table: product, paid share of units, ACoS vs break-even, spend, evidence from past weeks.
- One test per shortlisted product: change, length, success and failure thresholds.

Never:
- Never pause or cut ads in the account.
- Never present the organic figure as measured.
- Never run more than one test on the same product at once.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Before step 1, call cost_rules. If it returns questions, ask them in one message as written (dollars, choices, what skip does) and save each answer with set_cost_rule. On a scheduled run, use the defaults and list the questions at the end. End the answer with its used_line.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: mkt-amazon-ads-incrementality-by-product". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.

---

Anything the person typed after the shortcut is extra instruction for this run: $ARGUMENTS
