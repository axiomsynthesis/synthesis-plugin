# Are you overpaying to own your brand name?

Channel: Amazon · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Are you overpaying to own your brand name?" (id: amazon-brand-defense-audit, Amazon).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Shows how much you pay to appear on searches for your own brand name, and whether you need to. It sets that spend next to how many clicks rivals take on your name. Then it says whether to keep, cut or test the spend.

What to read: Ads, branded search
What to give me: What you spend on searches for your own name, how many clicks rivals take on it, and whether you need to spend that much

Synthesis tools to use:
- `amazon_metric metric=ppc_branded_split`
- `amazon_metric metric=search_competitors`
- `amazon_metric metric=search_query_performance`
- `amazon_metric metric=ppc_search_terms`

Steps:
1. Call `amazon_metric` with `metric=ppc_branded_split` and `days=30` for spend, sales and return on branded and non-branded ads.
2. Call `amazon_metric` with `metric=ppc_search_terms`, `days=30` and `limit=50` to list the branded search terms you pay for.
3. Call `amazon_metric` with `metric=search_competitors`, `grain=week`, `periods=4` and your brand name as `term` for rivals taking clicks on your name.
4. Call `amazon_metric` with `metric=search_query_performance`, `grain=week` and `periods=4` for your total click share on branded searches.
5. Weigh the spend against the share rivals take. Little rival pressure means the spend may be buying sales you would get anyway.

Checks before answering:
- Never average branded and non-branded returns. They are different businesses.
- If no rival shows on your name, say so plainly. That is a real answer, not missing data, only when the search read itself worked.
- If the search data is missing, say so. Do not judge defense without it.

Output:
- One line first: monthly spend on your own name and the share of clicks rivals take.
- A table: branded term, spend, sales, your click share, top rival, rival click share.
- One move, usually a small pause test on the safest terms, and how we will know.

Never:
- Never pause or change a campaign. A person does that.
- Never call branded spend wasted without a test that shows it.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: amazon-brand-defense-audit". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
