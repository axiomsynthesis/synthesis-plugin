# Clean up messy variation families

Channel: Amazon · Level: Advise · Status: Ready after we build it

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Clean up messy variation families" (id: mkt-amazon-variation-family-check, Amazon).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
A family page shares one rating and one set of reviews across all its sizes and flavors. A weak child can drag down the whole page.
This looks inside each family for children that sell almost nothing, hurt the shared rating, or break the price ladder.

What to read: How sales, reviews and ad spend split across the sizes and flavors inside each product family
What to give me: Dead or duplicate variations to drop or merge, and children that drag the family's rating or price ladder

Synthesis tools to use:
- `find_product`
- `amazon_metric metric=pnl_by_asin limit=60`
- `amazon_metric metric=ppc_spend_by_parent days=60 limit=30`
- `amazon_metric metric=velocity_momentum weeks=12 limit=60`

Steps:
1. Call `find_product query=<family name>` to list every size in the family. This works only where the brand has set up its product families.
2. Call `amazon_metric metric=pnl_by_asin limit=60` and `amazon_metric metric=velocity_momentum weeks=12 limit=60`. Split sales and trend per child.
3. Call `amazon_metric metric=ppc_spend_by_parent days=60 limit=30` to read ad cost for the whole family at once.
4. Flag children with under 2% of family sales for 6 months, and any child whose price per unit is above a bigger size's.

Checks before answering:
- Without a family list from the brand, never group products by name. Names repeat across different products. Say families are not set up.
- A new child under 90 days old is not dead. Leave it out.
- Read ads at family level. A click on one child is often credited to another.

Output:
- One line per family: keep as is, or the change.
- A table: family, child, share of family sales, 12-week trend, price per unit, flag.

Never:
- Never merge, split or delete variations in Seller Central.
- Never guess a family from product names.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: mkt-amazon-variation-family-check". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.

Not fully ready yet (ready after we build it): Amazon publishes no parent-child link in any table we sync, so families come only from a brand's own product family list. A tool that reads the live variation relationship from Amazon's catalog is not built. Do the parts you can and say plainly what is missing.
