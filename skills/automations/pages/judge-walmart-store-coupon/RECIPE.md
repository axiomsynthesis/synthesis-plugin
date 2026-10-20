# Is this Walmart store coupon worth running again?

Channel: Retail · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Is this Walmart store coupon worth running again?" (id: judge-walmart-store-coupon, Retail).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Judges an in-store coupon or cash-back offer at Walmart, or a Meta ad push aimed at Walmart, before you pay for more. It compares what each redemption cost with the profit on each unit, and checks whether the offer added sales or only paid people who would have bought anyway.

What to read: Walmart store weekly sales files, the coupon or cash-back invoices, product cost, Walmart's cost price, and Meta spend aimed at Walmart
What to give me: Cost per redemption against gross profit per unit, the extra units the offer really added, and a run-again, resize or stop verdict

Synthesis tools to use:
- `list_files`
- `search_files query=coupon`
- `read_file`
- `gsheets_metric metric=tables`
- `gsheets_metric metric=profile`
- `gsheets_metric metric=trend`
- `operator_inputs section=cogs`

Steps:
1. Ask: the offer, the item, the value per redemption, the cap, the dates, and Walmart's cost price per unit (what Walmart pays you). No tool holds that price.
2. Call `list_files`, then `search_files` with `query=coupon`, `query=walmart`, `query=retail campaign tracker` and the offer company's name. Call `read_file` on the offer invoices and the store weekly sales files.
3. Hard stop. The offer invoice and the store weekly sales file (units by item by week, 8 weeks before to 4 weeks after) must both be on file. If either is missing, ask for it and stop here. Do not go on to step 4. If the tracker sheet shows a push on the same items those weeks, say so before they upload. The result will not split.
4. If the brand keeps store sales in a sheet, call `gsheets_metric` with `metric=tables`. Tables come in pages, so search_files first and match the name. Call `metric=profile` on the hit for its date column, then `metric=trend`.
5. Remove duplicate rows before adding up. Store files can split one item across several rows. Count a row once per week, item and store category line.
6. Take 8 weeks before the offer as the baseline. Compare units in the offer weeks and in the 4 weeks after. Extra units are offer weeks minus baseline.
7. Call `operator_inputs` with `section=cogs` for product cost. It holds product cost only. Gross profit per unit is Walmart's cost price from step 1 minus product cost and any allowance.
8. Cost per redemption is the invoice total divided by redemptions. Compare it with gross profit per unit and with cost per extra unit.
9. If two offers or pushes ran on the same items at once, the result cannot be split. Say so. Run offers solo.
10. For a Meta push aimed at Walmart, the spend sits in the agency's tracker sheet from step 2, not in Meta's weekly spend split, which covers Amazon and website only. Compare the push weeks with store units the same way.
11. Verdict: run again, resize the cap, or stop. On one live brand, $5.25 to $7.31 per redemption was the range that paid.

Checks before answering:
- Safe test: this only reads. Nothing in Walmart or the offer app changes.
- Spend: state the offer's total cost and the cap. A cap set too high pays for redemptions you did not need.
- Totals must tie to the store sales file. If they do not, say by how much.
- If product cost or Walmart's cost price is missing, give cost per redemption only. Never call it profitable.
- Ask for the lowest price held on other channels. Say if a deeper offer would break it.
- Online marketplace sales are a different channel from store sales. Never mix them.

Output:
- One line first: run again, resize or stop, with cost per redemption against profit per unit. Or the one file still missing.
- A table: offer, weeks, redemptions, cost, cost per redemption, extra units, profit per unit.
- What to change next time: cap, value, timing.

Never:
- Never book, change or cancel an offer. The team does that with Walmart or the offer company.
- Never count a redemption as an extra sale.
- Never judge an offer that overlapped another as if it ran alone.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: judge-walmart-store-coupon". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
