# Dispute retailer deductions you don't owe

Channel: Retail · Level: Prepare · Status: Ready after we build it

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Dispute retailer deductions you don't owe" (id: mkt-retail-deductions-check, Retail).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Retailers take deductions from what they pay you: promotions, fines, damages, allowances. Some are wrong. This matches each to what you agreed and lists the ones to dispute.

What to read: Deductions the retailer took from payments, by type, against the promotions and allowances you agreed
What to give me: Deductions that don't match an agreed promo or allowance, with the dollars and paperwork to dispute each

Synthesis tools to use:
- `netsuite_metric metric=contra_revenue months=6`
- `search_files query=deduction`
- `read_file`
- `export_xlsx`

Steps:
1. Call `netsuite_metric metric=contra_revenue months=6` for deductions as booked, if the brand uses NetSuite.
2. Call `search_files query=deduction` and `read_file` for any uploaded deduction report or promotion agreement.
3. Match each deduction to an agreement by promotion, date and amount.
4. Build `disputes_<quarter>.xlsx` with `export_xlsx`: deduction id, date, type, amount, matched agreement or none, reason to dispute.

Checks before answering:
- Until deduction detail is connected, never present a dispute total. Say what is missing.
- Retailers set deadlines for disputes. Tell the person to check them.
- Deductions booked in accounting may lag the retailer's payment date.

Output:
- One line: total deductions, matched, to dispute.
- The spreadsheet above.

Never:
- Never file disputes. A person files them.
- Never call a deduction wrong without the agreement to show it.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: mkt-retail-deductions-check". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.

Not fully ready yet (ready after we build it): No retailer deduction or chargeback feed is connected. Needs the retailer's deduction detail, or the brand's accounting system with deductions coded by type, before each deduction can be matched to an agreement. Do the parts you can and say plainly what is missing.
