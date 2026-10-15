# Win back customers who stopped buying

Channel: Customers · Level: Prepare · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Win back customers who stopped buying" (id: customers-win-back-list-and-email, Customers).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Finds customers who stopped buying, past the point they would normally reorder. It splits them into groups by value, picks an offer for each, and drafts the email. A person uploads the list to Klaviyo and sends.

What to read: Shopify orders, Klaviyo
What to give me: Lapsed customers grouped by value, the offer for each group, and the email draft

Synthesis tools to use:
- `shopify_metric metric=winback_candidates`
- `shopify_metric metric=time_to_repeat`
- `winback_tiers`
- `klaviyo_metric metric=flow_funnel`
- `export_xlsx`

Steps:
1. Call `shopify_metric` with `metric=time_to_repeat` for how long customers usually wait between orders. This read has no date setting, so say the dates the result covers.
2. Call `shopify_metric` with `metric=winback_candidates` for lapsed repeat customers. Size each group from `tiers`, which covers every customer; the rows are only the top of the list. Customers come back as `customer_ref`, never an email.
3. For each group, call `winback_tiers` with `days_since_last` and `lifecycle_value` for the tier, offer and expected recovery.
4. Call `klaviyo_metric` with `metric=flow_funnel` to see whether a win-back flow already runs and how it does. Flow numbers are Klaviyo's running totals, with no date setting.
5. Call `export_xlsx` with `filename=winback_list.xlsx`, one sheet per tier, and write the email drafts into `winback_emails.md`. If you can save files here, save it and tell me its name. If not, show it in full.

Checks before answering:
- If a win-back flow already runs, say so. Do not double-mail the same people.
- If the order read is empty, say it could not be read. Never ship an empty list as "nobody lapsed".
- Expected recovery is an estimate. Say so in dollars with a range.

Output:
- One line first: how many customers lapsed and the dollars a win-back could recover.
- A file named `winback_list.xlsx` with customer ID, last order date, orders, value and tier. Personal details stay in Shopify.
- A file named `winback_emails.md` with one short email per tier: subject, preview line, body, offer.

Never:
- Never send an email or create a Klaviyo list or flow. A person does that.
- Never offer a discount deeper than the tier calls for.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: customers-win-back-list-and-email". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
