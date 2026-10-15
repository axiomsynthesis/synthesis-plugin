---
description: "Are your ads buying sales you'd get anyway?: Products where ads mostly pay for sales that would have happened anyway, with a test to prove it"
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
High ad-credited sales can mean ads are working. It can also mean ads are paying for buyers who were already looking for you.
This finds the products where the second is likely and sets up a small test to find out.

What to read: Ad-credited sales against total sales for each product, branded and non-branded ad spend, and organic sales over time
What to give me: Products where ads mostly pay for sales that would have happened anyway, with a test to prove it

Synthesis tools to use:
- `amazon_metric metric=ppc_organic_vs_paid days=60 limit=30`
- `amazon_metric metric=ppc_branded_split days=60`
- `amazon_metric metric=velocity_momentum weeks=16 limit=30`
- `measurable_test`

Steps:
1. Call `amazon_metric metric=ppc_organic_vs_paid days=60 limit=30`. Note each product's paid share of units and its total ad cost share.
2. Call `amazon_metric metric=ppc_branded_split days=60`. Heavy branded spend on a high-paid-share product is the warning sign.
3. Call `amazon_metric metric=velocity_momentum weeks=16 limit=30` to look for past weeks when ads dropped and total units held.
4. Shortlist up to 3 products. For each, design one test with `measurable_test`: the cut, the window, and the units level that would prove ads were needed.

Checks before answering:
- Organic units are total minus ad-credited. That is a floor, not a measurement. Say so.
- A product with paid share over 100% means double counting across sizes. Read it at parent level instead.
- Promo weeks are flagged in the momentum data. Never use one as the "before" in a comparison.
- Never call ads wasted on this read alone. It points to a test, not a verdict.

Output:
- One line: how many products look over-advertised and the monthly spend at stake.
- A table: product, paid share of units, branded share of spend, total ad cost share, evidence from past pauses.
- One test per shortlisted product: change, length, success and failure thresholds.

Never:
- Never pause or cut ads in the account.
- Never present the organic figure as measured.
- Never run more than one test on the same product at once.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: mkt-amazon-ads-incrementality-by-product". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.

---

Anything the person typed after the shortcut is extra instruction for this run: $ARGUMENTS
