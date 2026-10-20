# Make a tracked Amazon link for each ad

Channel: Amazon · Level: Prepare · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Make a tracked Amazon link for each ad" (id: do-amazon-ad-link, Amazon).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Makes one tracked Amazon link for each ad that sends people to Amazon. Each link sits on your own link address and carries its own Amazon Attribution tag. Amazon then credits each sale to the one ad that sent it. Putting a link into a live ad is the job of the ad launch shortcut.

What to read: Your Meta ads that send people to Amazon, the links they use today, your own link address
What to give me: One tracked Amazon link per ad, on your own link address, so Amazon can credit each sale to the ad that sent it

Synthesis tools to use:
- `cost_rules for=do-amazon-ad-link`
- `meta_metric metric=ad_destinations days=14 active_only=true`
- `create_ad_links kind=meta`

Steps:
1. Ask the product page or its product code. Ask which ads the links are for.
2. Call `meta_metric` with `metric=ad_destinations`, `days=14` and `active_only=true`. Read every page with `result_page`. If a page holds no rows but rows are still missing, say the list is incomplete. Ask which ads to cover, or try `days=7`. Keep only ads whose `effective_status` is ACTIVE.
3. List ads that go to Amazon with no link of their own. An empty link with basis rule or inference has no link Synthesis can see. List it as needs a link, never as shared. Links shared by two or more ads go on a second list.
4. An ad with no name cannot get a link. Say to name it in Ads Manager first.
5. Build one row per ad: creator handle or short ad name, month, year, version and product. Read the product from the old link's last word, like twopacknha or 9pack. If there is no link, ask the product.
6. Call `create_ad_links` with `kind=meta` and the rows, WITHOUT `create`. This is a preview and writes nothing. Show every link name and product code. Wait for yes.
7. Call `create_ad_links` again with the same rows and `create=true`.
8. Read back: call `create_ad_links` once more with the same rows and no `create`. Each row must return the same link, never a new one. Confirm each link name and its product.
9. Hand over each link next to its ad name. The link goes in the ad's website address. Leave the ad's URL parameters box empty, so the tag is not doubled.

Checks before answering:
- Safe test: when the person asks for a test run, make one link named claudetest that points at your main product page. Never use it in an ad.
- Spend: making a link spends nothing and changes no ad. Never edit, publish or turn on an ad here.
- One link per ad. Never give two ads the same link, or their sales cannot be told apart.
- One ad lives in one campaign. A copy of an ad in a second campaign gets its own link.
- Meta cannot see Amazon purchases. Judge these ads on the Amazon credit for each link, never on Meta's own results.
- If the answer says the Meta to Amazon add-on or your own link address is missing, say so and stop.
- If an ad account's last day is weeks old, say its ads are missing from this list.
- A new link in a live ad resets Meta's learning on it. Say so. The swap needs its own yes, at a quiet hour.

Output:
- One line first: how many links made, and how many old shared links were found.
- A table: ad name, product, link name, the link.

Never:
- Never reuse a link that another ad already uses.
- Never invent a product code the tool did not return.
- Never change a live ad. Use the ad launch shortcut, with its own yes.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Before step 1, call cost_rules. If it returns questions, ask them in one message as written (dollars, choices, what skip does) and save each answer with set_cost_rule. On a scheduled run, use the defaults and list the questions at the end. End the answer with its used_line.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: do-amazon-ad-link". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
