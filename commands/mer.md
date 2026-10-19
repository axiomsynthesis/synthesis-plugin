---
description: "Is all your marketing paying, together?: Your whole-business return on ad spend by month, and marketing as a share of sales"
argument-hint: "[anything to add for this run]"
disable-model-invocation: true
---

# Is all your marketing paying, together?

Channel: Growth · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Is all your marketing paying, together?" (id: grw-blended-mer-trend, Growth).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Ignores what each platform claims and asks one question: for every dollar of ads, how many dollars of total sales came in. It tracks that month by month with marketing as a share of sales.

What to read: Total sales and total ad spend by month across Meta, Google, TikTok and Amazon ads
What to give me: Your whole-business return on ad spend by month, and marketing as a share of sales

Synthesis tools to use:
- `cost_rules for=grw-blended-mer-trend`
- `mer month=<YYYY-MM>`
- `new_to_brand_customers month=<YYYY-MM>`

Steps:
1. For each of the last 12 closed months, run `mer`.
2. Read spend by channel from each result's `ad_channels`. Every ad leg is already there with its amount and status, so do not call Meta, TikTok, Google or Amazon spend tools separately.
3. Read sales by channel from `sales_channels`, and `error_direction` for whether the missing legs make the month read high or low.
4. For each month, call `new_to_brand_customers` and divide Amazon ad spend by it for Amazon ad spend per new Amazon customer. Never add website new customers to it: they are a different channel and a different meaning of new.
5. Show spend mix by channel beside the efficiency number.

Checks before answering:
- If `mer` is gated for a month, do not state it. Give its reason.
- Count TikTok spend from both auction and shop ads.
- Google Ads campaign spend is kept only from where its history starts. Months before that show Google as not measured, never zero, and their total spend is labelled as excluding Google.
- If a month's return is withheld, show its `upper_bound_only` as a ceiling, labelled, never as the month's number.
- Leave the current month out.
- Amazon ad spend counts Sponsored Products, Brands and Display. A month before the brand's Amazon ad history begins shows Amazon ads as not measured, never zero.
- A channel whose status says missing may simply have sold nothing that month. If a sales leg reads zero or missing for a channel that stopped selling, say it stopped, and that the month does not read low because of it.
- Spend here leaves out creator and affiliate pay and agency fees. It may also leave out display ads bought through Amazon's separate display service, which on one live brand was the size of a whole channel. Say total marketing is higher than shown, so the real return is lower.
- Amazon sales in the total are before discounts. Say the total reads high by those discounts.
- This answer gives no break-even line yet. The return that just pays for marketing is 1 divided by the business's margin before marketing. If `business_profit` has been read this session, give that line. If not, say the number cannot be judged good or bad without it.
- New-customer sales per ad dollar is not available. The new-customer tools give counts, not sales. Show ad spend per new customer instead and say so.

Output:
- Answer first: is total marketing paying? Last month's sales per ad dollar, its trend, and whether it sits above or below break-even when that line is known.
- Table by month: total sales, total ad spend, efficiency, marketing share of sales, ad spend per new customer, spend mix.
- One line: the costs left out of spend, and which way they move the return.

Never:
- Nothing changes in any live account. A person on your team makes every change.
- Never fill a missing, gated or empty number with an estimate. Say what is missing and why.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Before step 1, call cost_rules. If it returns questions, ask them in one message as written (dollars, choices, what skip does) and save each answer with set_cost_rule. On a scheduled run, use the defaults and list the questions at the end. End the answer with its used_line.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: grw-blended-mer-trend". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.

---

Anything the person typed after the shortcut is extra instruction for this run: $ARGUMENTS
