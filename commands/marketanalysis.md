---
description: "Market analysis deck for a new Amazon product: A landscape deck in the house look: market size, seasons, leaders, price lanes, last year's launches, three first-season paths and a launch calendar"
argument-hint: "[anything to add for this run]"
disable-model-invocation: true
---

# Market analysis deck for a new Amazon product

Channel: Agency · Level: Prepare · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Market analysis deck for a new Amazon product" (id: agency-prospect-market-deck, Agency).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Turns two category exports into a deck on one Amazon market, for a new product going into it: a brand sizing up its own next launch, or an agency pitching a brand that is not on Amazon yet. One finding per slide, every headline worked out from the files. An agency's deck is signed Prepared by that agency.

What to read: Two category files from your Amazon data provider, the product and its launch month
What to give me: A landscape deck in the house look: market size, seasons, leaders, price lanes, last year's launches, three first-season paths and a launch calendar

Synthesis tools to use:
- `list_files`
- `get_upload_link`
- `finalize_upload`
- `market_report`

Steps:
1. Ask for the two files: the monthly brand revenue export (a Date column, then one column per brand) and the product list export (one row per listing). The easy way to upload them is the Upload documents button on the Connections page in the Synthesis app.
2. Call `list_files` and find both files by name. If they are not there, call `get_upload_link` for each, have the person upload it, then call `finalize_upload` with its file_id.
3. Ask for what the files cannot know: the brand's name, the product, its planned Amazon price, its size in ounces, the launch month, and who the deck is for. Ask which sub-category it competes in (for example face sunscreen) and whether to track a brand group (for example Korean brands).
4. Ask one question about copycats: is any rival's product name being used by other sellers? If yes, get the product name and the brand that owns it.
5. Live reads are optional and cost shared search credits: 1 per Amazon search plus 1 for Google Trends. Say the count and ask before turning them on. If agreed, get up to 8 searches, most important first.
6. Call `market_report` with the two file_ids and the answers. Set live only if the person agreed in step 5.

Checks before answering:
- Name every slide in `left_out` and say why it has nothing to show.
- Say which months `product_file_months` used for the product file. If they are wrong, rerun with product_period.
- Say how many search credits were spent and name any search that came back empty.
- The deck is drawn from estimates by an outside data provider, not Amazon's own figures. Say so once.

Output:
- One line first: the market size and the typical first season for a brand launching at that point in the calendar.
- The download link to the deck.
- The slides left out, the product file's months and the credits spent.

Never:
- Never turn on live reads without a yes to the stated credit count.
- Never add a copycat claim the person did not name.
- Never send the deck to anyone outside. A person does that.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: agency-prospect-market-deck". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
- If you could not finish, open your answer with "Stuck:" and what I need to do. If your answers are not saved for you automatically, save this one with the Synthesis tool `capture_turn`: my request as `question`, your answer as `answer`, and `context` starting with "automation: agency-prospect-market-deck".

---

Anything the person typed after the shortcut is extra instruction for this run: $ARGUMENTS
