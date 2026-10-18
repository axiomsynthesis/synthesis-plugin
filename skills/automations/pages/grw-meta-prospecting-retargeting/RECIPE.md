# Is Meta finding new customers?

Channel: Meta · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Is Meta finding new customers?" (id: grw-meta-prospecting-retargeting, Meta).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Splits Meta spend into prospecting and retargeting from campaign names and settings. It sets that against how many new website customers you actually got each month, to see whether retargeting is taking credit for buyers who were coming back anyway.

What to read: Meta spend by campaign type, and new vs returning website customers
What to give me: Whether Meta is finding new customers or re-buying the ones you already have

Synthesis tools to use:
- `cost_rules for=grw-meta-prospecting-retargeting`
- `meta_metric metric=campaign_performance limit=40`
- `shopify_metric metric=new_vs_returning months=6`
- `new_customers_dtc month=<YYYY-MM>`

Steps:
1. Pull `meta_metric metric=campaign_performance limit=40` and label each campaign prospecting or retargeting. List any you cannot label.
2. Sum spend and Meta-reported purchases per type for each of the last 6 months.
3. Pull `shopify_metric metric=new_vs_returning months=6` and `new_customers_dtc` per month.
4. Compare: retargeting share of spend vs returning customers' share of orders. Flag months where retargeting spend rose and new customers did not.

Checks before answering:
- If `new_customers_dtc` comes back gated, do not state it. Give its reason.
- Shopify new means first website order, not first purchase from the brand. Say so.
- Unlabelled campaigns are shown as unlabelled, never guessed.
- Meta's purchase numbers come from its own tag. It cannot see Amazon or retail checkouts, so say that beside any ROAS.

Output:
- Answer first. Table by month: prospecting spend, retargeting spend, new website customers, returning share of orders.
- One move.

Never:
- Nothing changes in any live account. A person on your team makes every change.
- Never fill a missing, gated or empty number with an estimate. Say what is missing and why.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Before step 1, call cost_rules. If it returns questions, ask them in one message as written (dollars, choices, what skip does) and save each answer with set_cost_rule. On a scheduled run, use the defaults and list the questions at the end. End the answer with its used_line.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: grw-meta-prospecting-retargeting". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
