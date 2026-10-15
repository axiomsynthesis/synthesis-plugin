# Your pages fighting each other on Google

Channel: Website · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Your pages fighting each other on Google" (id: grw-seo-cannibalisation, Website).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Finds searches where two or more of your pages compete, so Google keeps swapping them and neither ranks well. It names the page that should own each search and what to do with the others.

What to read: Google Search Console queries and how many of your pages each one hits
What to give me: Searches split across several of your pages, and which page should own each

Synthesis tools to use:
- `search_console_organic view=queries days=90 limit=200 min_impressions=100`

Steps:
1. Pull `search_console_organic view=queries days=90 limit=200 min_impressions=100`.
2. Keep terms where more than one page earns impressions.
3. For each, pick the owner page: the one with the best position and click rate.
4. Suggest for the others: merge, redirect, or change their focus, with internal links pointing to the owner.

Checks before answering:
- Two pages on one brand-name search is normal. Exclude pure brand-name terms.
- If fewer than 100 terms come back, say the site is small for this read.

Output:
- Answer first. Table with columns search, impressions, pages competing, owner page, action for the others.

Never:
- Nothing changes in any live account. A person on your team makes every change.
- Never fill a missing, gated or empty number with an estimate. Say what is missing and why.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: grw-seo-cannibalisation". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
