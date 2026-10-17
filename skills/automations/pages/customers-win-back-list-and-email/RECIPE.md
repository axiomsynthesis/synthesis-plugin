# Win back customers who stopped buying

Channel: Customers · Level: Prepare · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Win back customers who stopped buying" (id: customers-win-back-list-and-email, Customers).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Finds repeat customers who have not ordered in 3 to 12 months. It splits them into groups by value, picks an offer for each, hands over the contact list as a download, and drafts one email per group. A person uploads the list to the email tool and sends.

What to read: Shopify orders, Klaviyo
What to give me: Lapsed customers grouped by value, the offer for each group, a contact list for your email tool, and the email drafts

Synthesis tools to use:
- `shopify_metric metric=time_to_repeat`
- `shopify_metric metric=winback_candidates export=true`
- `klaviyo_metric metric=flow_funnel`

Steps:
1. Call `shopify_metric` with `metric=time_to_repeat` for how long customers usually wait between orders. Give the share of repeat orders that come within 60 days, and the average gap, saying long gaps pull the average up. The list in step 2 uses a fixed 90 to 365 days since the last order, whatever the gap.
2. Call `shopify_metric` with `metric=winback_candidates` and `export=true`. Size each group from `tiers`, which covers every customer; the rows shown are only the top of the list. The download link holds the full list for the email tool.
3. Call `klaviyo_metric` with `metric=flow_funnel` to see whether a win-back email series has sent recently. It covers recent sends only and leaves out series that have not sent.
4. Write one short email per group into `winback_emails.md`: subject, preview line, body, offer. If you can save files here, save it and tell me its name. If not, show it in full.

Checks before answering:
- If a win-back series already sends, say so. Do not double-mail the same people.
- If the order read is empty, say it could not be read. Never ship an empty list as "nobody lapsed".
- The expected return rates are a rule of thumb, not measured on these customers. Give them as a share of customers, never as dollars won back.
- The download link holds customer emails. Hand it only to the person who will send the email.

Output:
- One line first: how many customers lapsed and what they spent before.
- A table: group, customers, average past spend, days since last order, offer.
- The download link for the contact list.
- A file named `winback_emails.md` with one short email per group.

Never:
- Never send an email or create a Klaviyo list or flow. A person does that.
- Never offer a discount deeper than the group calls for.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: customers-win-back-list-and-email". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
