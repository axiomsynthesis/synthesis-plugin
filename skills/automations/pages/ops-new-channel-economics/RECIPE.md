# Is a new sales channel worth it?

Channel: Growth · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Is a new sales channel worth it?" (id: ops-new-channel-economics, Growth).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Before saying yes to a retailer, a new marketplace or a distributor, this works out what each unit really earns there and how much cash the launch ties up. New channels often look like growth and work like a loan to the retailer.

What to read: Your product costs and prices, the new channel's fees and terms, and expected volume
What to give me: Profit per unit in the new channel, the cash it ties up before the first payment, and the volume needed to break even

Synthesis tools to use:
- `cost_rules for=ops-new-channel-economics`
- `amazon_metric metric=contribution_by_asin months=3`
- `unit_economics_waterfall asp=<price> cogs=<cost> fulfillment=<cost>`
- `run_scenario scenario_type=inventory_bet`
- `ccc_health dio=<days> dso=<days> dpo=<days>`

Steps:
1. Ask for the channel's terms: wholesale or sell price, fees, trade spend, slotting fees, freight, payment terms, store count and expected units per store per week.
2. Call `amazon_metric metric=contribution_by_asin months=3` for your current cost and profit per unit, as the comparison.
3. Run `unit_economics_waterfall asp=<price> cogs=<cost> fulfillment=<freight>` with the channel's fees in place of Amazon's.
4. Cash: run `run_scenario scenario_type=inventory_bet` for the first fill, and `ccc_health` with the channel's payment terms.
5. Break-even volume = fixed launch costs divided by profit per unit, per store per week.

Checks before answering:
- Every channel term comes from the person or the offer. Label each.
- Trade spend and deductions are usually higher than quoted. Show the result at the quoted level and at 50% higher.
- Never compare channel profit per unit with Amazon profit per unit unless both are after the same cost lines.

Output:
- Table: Line | New channel per unit | Amazon per unit.
- Four lines: profit per unit, cash tied up, break-even volume, and the verdict.

Never:
- Never accept, sign or reply to a channel's offer.
- Never invent terms.
- Never count the channel's sales as incremental without saying some may move from existing channels.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Before step 1, call cost_rules. If it returns questions, ask them in one message as written (dollars, choices, what skip does) and save each answer with set_cost_rule. On a scheduled run, use the defaults and list the questions at the end. End the answer with its used_line.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: ops-new-channel-economics". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
