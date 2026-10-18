# New idea to a brief for my editor or creator

Channel: Creative · Level: Prepare · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "New idea to a brief for my editor or creator" (id: creative-idea-to-editor-brief, Creative).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Turns one saved idea into a brief someone else can shoot from.
It sets the length, the shots second by second, the words on screen, the claims allowed and the do-nots.

What to read: One saved idea, your brand kit, your brand facts
What to give me: A one-page shoot brief an editor or creator can follow, and the idea marked briefed

Synthesis tools to use:
- `ad_idea_bank action=get`
- `brand_kit`
- `brand_facts`
- `ad_idea_bank action=set_status`

Steps:
1. Ask which idea. If none is named, call `ad_idea_bank` with `action=list` and `status=idea` and offer the newest five.
2. Call `ad_idea_bank` with `action=get` and the `idea_id` for the full idea.
3. Call `brand_kit` for colours, typefaces and logo, and `brand_facts` for the claims on file.
4. Write the brief: format and length, shot list by second, words on screen, the claims allowed, the do-nots.
5. Call `ad_idea_bank` with `action=set_status`, `status=briefed` and a short `note`.

Checks before answering:
- Only claims on file go in the brief. List any line the brand must confirm.
- Give 9:16 and 4:5 framing notes when it is a video.

Output:
- One brief, one page, ready to send.
- One line confirming the idea is now marked briefed.

Never:
- Never put a health or results claim in a brief that is not on file.
- Nothing is sent to anyone. You send the brief.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: creative-idea-to-editor-brief". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
