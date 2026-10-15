# Money left in abandoned carts

Channel: Email · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Money left in abandoned carts" (id: grw-abandoned-cart-recovery, Email).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Sizes the carts and checkouts people start and do not finish, then shows how many your recovery emails bring back. It finds the cheapest step to win more of them.

What to read: GA4 add-to-cart and checkout counts, Klaviyo abandoned cart flow results
What to give me: How many carts are left, how many your flow wins back, and the size of the gap

Synthesis tools to use:
- `ga4_metric metric=funnel days=28`
- `klaviyo_metric metric=flow_funnel`
- `klaviyo_metric metric=flow_step_performance limit=60`

Steps:
1. Pull `ga4_metric metric=funnel days=28` for sessions with add to cart, checkout started and purchase.
2. Pull `klaviyo_metric metric=flow_funnel` and `klaviyo_metric metric=flow_step_performance limit=60` for the abandoned cart and abandoned checkout flows.
3. Compute abandoned checkouts per month, recovery flow orders per month and the recovery rate.
4. Check the flow's first send delay and whether there is both a cart and a checkout flow.

Checks before answering:
- Klaviyo revenue is last-touch credit on website orders. It cannot see Amazon orders. Never call it email's total effect.
- GA4 counts sessions, Klaviyo counts profiles it can identify. Say that only identified shoppers can be emailed.
- Use the same 28 days where possible and say where the windows differ.

Output:
- Answer first: recovery rate and the gap in dollars. Then the three numbers and one fix.

Never:
- Nothing changes in any live account. A person on your team makes every change.
- Never fill a missing, gated or empty number with an estimate. Say what is missing and why.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: grw-abandoned-cart-recovery". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
