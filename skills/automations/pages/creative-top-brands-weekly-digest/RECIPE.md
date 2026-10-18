# Weekly top brands in my category

Channel: Creative · Level: On a schedule · Status: Ready now
Schedule: Every Monday

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Weekly top brands in my category" (id: creative-top-brands-weekly-digest, Creative).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Shows what well-known brands in your category keep running.
Ads that run 30 days or more are very likely paying, so those come first, with the hook and why it may work.
Ends with one idea to borrow for your own ads.

What to read: The shared library of well-known brands' live ads and monthly playbooks
What to give me: A weekly digest of what top brands in your category run longest, and one idea to borrow

Synthesis tools to use:
- `competitor_ads source=inspiration`
- `competitor_ads source=inspiration view=playbooks`

Steps:
1. Ask the category if you do not know it. Call `competitor_ads` with `source=inspiration` and `view=brands` to list categories.
2. Call `competitor_ads` with `source=inspiration`, the `category` and `min_days=30` for the long runners.
3. Call `competitor_ads` with `source=inspiration`, `view=playbooks` and the same `category` for each brand's monthly playbook.
4. Group the long runners by hook and format. Name the pattern that repeats.
5. Write one idea to borrow, as an angle on your own best hook.

Checks before answering:
- Read `status` first. "Not yet pulled" is a setup gap, never "these brands run nothing".
- This library is the same for every customer and is not your rivals.

Output:
- One headline line: how many long runners from how many brands.
- Up to 8 ads: brand, hook, format, days running, ad link.
- One idea to borrow.

Never:
- Never copy another brand's words or claims. Borrow the shape, not the line.
- Never state spend or results for a library ad.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: creative-top-brands-weekly-digest". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
- This is meant to repeat (Every Monday). Run it once now. If you can set up a repeating task here, do it. If not, tell me how to run this again each time it is due.
