# Write an email campaign

Channel: Email · Level: Prepare · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Write an email campaign" (id: email-write-a-campaign, Email).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Writes subject lines, body copy and the product block for one send.
It writes in your voice, uses your real products and offers, and suggests a send time from your past results.
A person pastes it into Klaviyo.

What to read: Your brand voice, products, past winners
What to give me: Three subject lines, ready-to-paste copy in your voice, and the best time to send

Synthesis tools to use:
- `klaviyo_metric metric=subject_feature_lift`
- `klaviyo_metric metric=send_timing`
- `klaviyo_metric metric=campaign_scorecard`
- `brand_facts`
- `find_product`

Steps:
1. Ask what the send is for: product, offer and audience.
2. Call `klaviyo_metric` with `metric=campaign_scorecard` to find the brand's best past campaigns to learn from. This read has no date setting, so say the dates the result covers.
3. Call `klaviyo_metric` with `metric=subject_feature_lift` to see which subject styles lift opens for this list. It uses the list's whole send history.
4. Call `brand_facts` with `query` set to the product, and `find_product` to get its real name and pack sizes.
5. Call `klaviyo_metric` with `metric=send_timing` to pick the send day and hour. It uses the brand's own send history, with no date setting.

Checks before answering:
- Every claim in the copy must come from the brand's own facts.
- If Klaviyo history is empty, say the send time is a default, not learned from this list.
- Use the real product name and price. Never guess either.

Output:
- Three subject lines and a preview line for each.
- Body copy under 150 words, with the product block and one button.
- One suggested send time and why.

Never:
- Nothing goes live in any account. A person pastes and sends it in Klaviyo.
- Never write a health or results claim the brand does not already make.
- Never invent a discount the person did not give.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: email-write-a-campaign". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
