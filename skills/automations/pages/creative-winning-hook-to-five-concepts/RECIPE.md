# Turn a winning hook into 5 concepts

Channel: Creative · Level: Prepare · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Turn a winning hook into 5 concepts" (id: creative-winning-hook-to-five-concepts, Creative).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Takes your best-selling hook and writes five new ways to run it.
Each concept keeps what makes the hook work and changes the format, the person or the proof.
All five are saved to your ideas list so you can track them.

What to read: Your hook ranking, the demand behind your best hook, your brand facts
What to give me: Five new ad concepts on one winning hook, saved to your ideas list

Synthesis tools to use:
- `winning_hooks`
- `brand_facts`
- `find_product`
- `ad_idea_bank action=save`

Steps:
1. Call `winning_hooks` with `read_new=false`. Pick the winner with the highest return against your average, or the hook the person names.
2. Read that hook's top ads and its demand quotes from the same result.
3. Call `find_product` for the product the hook's ads sell, and `brand_facts` with `query` set to it for the claims on file.
4. Write five concepts: title, hook line, script, brief for the shoot, why, claims used.
5. Save each with `ad_idea_bank` and `action=save`, `source=chat`, and the hook in `source_detail`.

Checks before answering:
- The five must differ in format or layout, not just wording.
- Every claim must be on file. Drop any that is not and say which.
- If no hook is a winner yet, say so and use the best promising hook, marked as promising.

Output:
- One headline line: the hook, its return against your average, and its spend.
- Five concepts, each with its saved idea id.
- One line on the cheapest way to test them.

Never:
- Never copy a disease or results claim from an old ad, even a winning one.
- Never invent a customer quote. Quotes come from the demand evidence only.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: creative-winning-hook-to-five-concepts". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
