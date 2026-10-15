# What refunds cost, channel by channel

Channel: Money · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "What refunds cost, channel by channel" (id: ops-refund-cost-by-channel, Money).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Puts refund dollars from every channel side by side so a rising cost in one place is not hidden by a flat total. Rising refunds are an early sign of a product, packaging or fulfilment problem.

What to read: Refunds by channel from the ledger, Amazon return rate, and TikTok Shop returns
What to give me: What refunds cost each month in each channel, and whether any is rising

Synthesis tools to use:
- `netsuite_metric metric=refund_rate months=12`
- `netsuite_metric metric=returns_credits months=12`
- `return_rate month=YYYY-MM`
- `tiktok_metric metric=shop_returns months=6`

Steps:
1. Call `netsuite_metric metric=refund_rate months=12` for refund dollars by channel.
2. Call `netsuite_metric metric=returns_credits months=12` for retail and wholesale credit memos by issue month.
3. For Amazon, call `return_rate month=YYYY-MM` for each of the last three full months.
4. If TikTok Shop is connected, call `tiktok_metric metric=shop_returns months=6` for refunds paid.
5. For each channel compare the last full month to the average of the three before. Flag any channel up more than 30% and more than $2,000.

Checks before answering:
- Drop the running month. Part months read low.
- Credit memos are dated by issue, not by original order. Say so when one lands in a month with low sales.
- A marketplace refund rate from the ledger is NULL by design. Use dollars there.
- If a channel is not connected, show it as "not connected", never as zero refunds.

Output:
- Table: Channel | Refund dollars last month | 3-month average before | Change | Flag.
- One line naming the channel to look at, and the next read to run (for Amazon, the return reasons by product).

Never:
- Never add credit memos and channel refunds that describe the same return.
- Never blame a product without the return reasons behind it.
- Never change a returns policy or contact a customer.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: ops-refund-cost-by-channel". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
