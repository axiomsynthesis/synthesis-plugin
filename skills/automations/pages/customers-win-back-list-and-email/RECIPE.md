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
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: customers-win-back-list-and-email". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
