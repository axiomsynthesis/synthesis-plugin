# What first orders make the best customers?

Channel: Customers · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "What first orders make the best customers?" (id: grw-ltv-drivers, Customers).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Looks past the first product to other traits of a customer's first order: whether they used a discount, how much they spent, single or multipack. It ranks which traits go with customers worth more a year later.

What to read: First-order traits such as discount used, basket size, pack size and month
What to give me: The first-order traits that predict higher customer value, ranked by money

Synthesis tools to use:
- `ltv_driver_dimensions channel=amazon`
- `ltv_driver_dimensions channel=shopify`
- `ltv_drivers channel=amazon dimension=<dimension> window_days=365 min_n=200`
- `ltv_drivers channel=shopify dimension=<dimension> window_days=90 min_n=200`

Steps:
1. Run `ltv_driver_dimensions` for amazon and for shopify to see which traits each channel has. Discount at first order exists on Amazon only.
2. For each available trait other than first product, run `ltv_drivers` at window_days=90 and 365.
3. Keep segments with sample_ok true. Rank by lift times revenue share.
4. A lift at 90 days that vanishes at 365 is a pull-forward, not a driver. Drop it.

Checks before answering:
- Never blend Amazon and website in one read. Run each channel on its own.
- Every lift is an association, not proof. The tool files the top falsifier as a prediction; say so.
- A refused dimension is a data gap, never proof nobody used a discount.
- Multipack is guessed from titles. Say so.

Output:
- Answer first. Table: trait, segment, customers, value at 365 days, lift, revenue share.

Never:
- Nothing changes in any live account. A person on your team makes every change.
- Never fill a missing, gated or empty number with an estimate. Say what is missing and why.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: grw-ltv-drivers". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
