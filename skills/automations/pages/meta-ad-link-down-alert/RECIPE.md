# Tell me when an ad link stops working

Channel: Meta · Level: On a schedule · Status: Ready now
Schedule: every morning, from our server

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Tell me when an ad link stops working" (id: meta-ad-link-down-alert, Meta).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Every morning, opens each of your Meta to Amazon links the way a shopper would and checks it still leads to the right Amazon product with your Amazon tag. Emails you only when one is broken, or when a link could not be checked.

What to read: Every Meta to Amazon link you made in Synthesis, opened each morning the way a shopper would
What to give me: An email the morning a link stops working: which link, what is wrong with it, and how to fix it

Synthesis tools to use:
- `cost_rules for=meta-ad-link-down-alert`
- `meta_metric metric=ad_destinations days=14 active_only=true`

Steps:
1. Call `meta_metric metric=ad_destinations days=14 active_only=true` for the address every spending Meta ad sends people to.
2. Match each address to the links on the Meta to Amazon page. A spending ad whose address is not one of those links is not measured on Amazon.

Checks before answering:
- A link that could not be reached is "could not check", never "working".
- A link that reaches the product without the Amazon tag is broken: it sells and nobody is credited.
- Name each link by its name and the ad or ads that use it.

Output:
- One line first: how many links are broken, out of how many.
- Each broken link, what is wrong with it, and the ads that use it.
- The fix: make the link again on the Meta to Amazon page, step 4, and put the new address in those ads.

Never:
- Never change, pause or launch an ad.
- Never remove a link. A person does that on the page.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Before step 1, call cost_rules. If it returns questions, ask them in one message as written (dollars, choices, what skip does) and save each answer with set_cost_rule. On a scheduled run, use the defaults and list the questions at the end. End the answer with its used_line.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: meta-ad-link-down-alert". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
- This one runs on the Synthesis server (every morning, from our server). Do not set up a repeat yourself; read the latest copy instead.
