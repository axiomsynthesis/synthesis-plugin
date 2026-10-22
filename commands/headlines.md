---
description: "Rank selling angles by ad results, write headlines, and test them on the page: Your selling angles ranked by what they sold per ad dollar, headlines written from the winners inside your approved claims, and a headline split test sized to your traffic"
argument-hint: "[anything to add for this run]"
disable-model-invocation: true
---

# Rank selling angles by ad results, write headlines, and test them on the page

Channel: Website · Level: Prepare · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Rank selling angles by ad results, write headlines, and test them on the page" (id: website-headline-angles-test, Website).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Finds which angles sold in your own ads, writes headlines from the winners, and hands over a headline-only test ready to run.
House rules, as defaults: lead with the shopper's problem. The expert or the science is the reason to believe, not the promise. Test only the headline and the line under it.

What to read: Every angle your Meta ads have run and what each sold, ad comments, review praise and complaints, what shoppers search for, approved claims, the page's visitors and profit per visitor
What to give me: Your selling angles ranked by what they sold per ad dollar, headlines written from the winners inside your approved claims, and a headline split test sized to your traffic

Synthesis tools to use:
- `cost_rules for=website-headline-angles-test`
- `recall_decisions`
- `brand_brain action=moves`
- `winning_hooks read_new=false`
- `meta_metric metric=ad_comment_themes days=90`
- `amazon_metric metric=review_voice limit=12`
- `amazon_metric metric=search_query_performance grain=month scope=nonbranded`
- `brand_facts`
- `shopify_metric metric=profit`
- `ga4_metric metric=landing_pages days=28`
- `web_fetch`
- `measurable_test direction=higher_is_better`
- `get_skill`

Steps:
1. Call `recall_decisions` for past headline tests and winners, and `brand_brain` with `action=moves` and `since` 30 days ago for tests now on this page. Ask the page and any angle the owner wants tried.
2. Angles. Call `winning_hooks` with `read_new=false`. Read the leaderboard by theme, website and marketplace apart, each against its own average. Never add them. A winner needs $1,500 across 2 ads or more; one ad is "proven on one creative". Less is promising. An angle not listed in `other_themes_more` is unread, not a loser. Website return is Meta's own credit: say so, and set the spend it read against website ad spend from `shopify_metric` with `metric=profit` to show what it missed.
3. Where it breaks. For each top angle read `breaks_at`. "page" means the ad's promise is not on the page: that angle's headline is the fix.
4. Demand. Read `demand`. Call `meta_metric` with `metric=ad_comment_themes` and `days=90` for doubts. Call `amazon_metric` with `metric=review_voice`, `sentiment=positive` and `limit=12`, then `sentiment=negative`. Searches come as queries, not angles: call `amazon_metric` with `metric=search_query_trend` and `keyword` set to each angle's own word.
5. Rank angles: return vs average, then spend, then demand. Mark each proven, promising or untested.
6. Write 2 to 3 headlines per top angle, plus one untested angle the owner asked for. Each: headline and the line under it. Problem first, then the discovery, in buyers' own words.
7. Claims. Check every word against `brand_facts`, and call it with `query=claim` for any fact marking a claim open or disputed. A line in live ads is not proof it is approved. No disease claim. Mark each approved or needs approval.
8. Page. Call `web_fetch` on the page. Mock each headline on the phone first screen in the browser. Flag one that pushes the buy button below it.
9. Traffic. Call `ga4_metric` with `metric=landing_pages` and `days=28`. If not connected, use the split-test app's or Shopify's count and say which. Profit per visitor from the profit read.
10. Test plan. Every page visitor, not one ad set: on one live brand a $300 a day slice gave each headline about 300 visitors a week. Visitors a headline = 16 x p x (1 - p) / d squared. Weeks = (headlines + 1) x that / weekly visitors. Over 8 weeks: best 3 plus today's. If the app caps versions, split into tests that never share a visitor, each with today's. Drop one over 30% behind at 1,000 visitors. If the window crosses a big sale (Prime days, Black Friday), end before it or leave those weeks out, and say which. Give the read date and a winner's cost per order: today's / (1 + lift).
11. Call `measurable_test` with the claim, profit per visitor, the read date and `direction=higher_is_better`. Hand the plan to `get_skill` with `name=/splittest`.

Checks before answering:
- Marketplace returns lag: credit lands for 14 days, so recent ads read low.
- Theme labels are a model's reading. Name the top ad behind each top angle.
- One test per first screen. If a page or offer test is running or planned on it, say which goes first and why.

Rounds (relook before you answer):
1. **Angles on a second window.** Call `winning_hooks` with `days=30`. Fails when: the top angle falls below 1.0x average in the last 30. If its spend is the same in both windows, nothing was tested: call `meta_metric` with `metric=ad_daily_trend` on its top ad and compare first-half to second-half return. Fix: say it is fading, lead with the angle that held.
2. **Website, not marketplace.** Fails when: an angle is proven only on marketplace ads while its website return is under 1.0x. Fix: mark it promising.
3. **Claim sweep.** Fails when: one word has no matching fact, or a fact marks it open. Fix: reword or mark needs approval.
4. **Problem first.** Fails when: over half the headlines open with the ingredient, founder or science. Fix: rewrite.
5. **Enough visitors.** Re-run step 10. Fails when: over 8 weeks, under 1,000 visitors a headline, or a big sale inside. Fix: fewer headlines, or end before the sale.
6. **Argue the loser.** Fails when: an angle left out has a higher return than one kept on over $1,500. Fix: put it back.
7. **Ready to run.** Fails when: final copy, shortcut, split, days, metric, winner line or dollars a month is missing. Fix: add it.

Output:
- First line: the winning angle, its return vs average and spend, the headline count and read date.
- Angle table: angle, return vs average, spend, ads, orders, demand, proven or not.
- Headlines ready to paste, each with the line under it, angle and claim status.
- The next action: shortcut, split, days, profit per visitor, winner line, dollars a month at stake. What was not checked.

Never:
- Never put a headline live or start a test here. The split-test shortcut does that after a yes.
- Never rank an angle on comments or reviews alone. Sales per ad dollar first.
- Never use another brand's results as this brand's.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Before step 1, call cost_rules. If it returns questions, ask them in one message as written (dollars, choices, what skip does) and save each answer with set_cost_rule. On a scheduled run, use the defaults and list the questions at the end. End the answer with its used_line.
- This job is worked in rounds; the first pass is never the answer. First call recall_decisions and look for an earlier run of this job: if one exists, start from where it ended, not from zero. After the Steps, run every round in Rounds in order. Each round re-reads the data it needs, says what it found wrong and fixes the draft. Log one line per round: what changed and why, or 'no change' if its check passed. Never invent a change. Stop mid-way only for a choice only I can make. Show the final draft, then the round log, then 2 or 3 next rounds I could ask for. Treat my feedback as a new round: re-run every check it touches, and never quietly undo an earlier fix. At the end, save where this run stopped with log_decision so the next run picks it up.
- Read every number that drives the call in layers and over several windows, never one. Layers, where they apply: volume (orders, sales), then profit after every cost, then return on the money spent against break-even, then what a customer is worth later on profit. Windows by how fast the number moves: fast ones (clicks, buy rate, cost per sale) over the last 7 closed days and the 7 before; sales, spend and return over 28 days, never under 4 weeks; slow ones (repeat, lifetime value, share) over 90 days to 12 months, comparing only customers of the same age. Set each against the same weeks last year, not last week. Closed days only; a young cohort is unfinished, not low. Before calling a change, rule out a deal, a stock-out or a part month. Show one small grid: each key number by window, with return on spend. When windows disagree, say so plainly: a fall in a slow number outranks a wobble in a fast one, a trend needs 4 steady weeks, and mixed signals mean no clear signal yet, not a verdict.
- Before trusting a number, compare it the way an expert would. Against itself: its own usual level and the same weeks last year. Against its peers: the other products, ads, pages or channels doing the same job, ranked side by side. Against the line that matters: break-even and any goal the brand set. An outside benchmark only shows room to grow, never a grade. Against a control: a holdout, the page being beaten, or a past natural test such as a pause or a stock-out. Break every move into its parts (price times units times mix, or rate times count) and name the part that moved. Look at the spread, not just the average: the top and bottom few, and how much rides on one item. Size each finding in dollars a month. Name the number that would flip the call.
- Go deeper with the tools built for it, picking the ones this job needs and saying which you ran and which you skipped. Start from the map: brand_brain with action=what_matters, then action=links_here on the thing at hand to find what it is tied to, and action=explain_link to check a link was tested and is not chance. Incrementality: attribution_lenses to set what the platform claims beside what was likely extra, plus any past pause, stock-out or spend jump as a natural test; never treat a platform's own credit as extra sales. Models: media_response_model or diminishing_returns for what the next dollar returns; run_monte_carlo for a range of outcomes, never one point; run_bayesian when the sample is small; explain_metric_move for why a number moved; backtest_rule to check the call would have held in the brand's own past. List what is working and what is breaking, both sides. Check find_contradictions against earlier conclusions. Close every recommendation with measurable_test: the number, the date and the line that says it worked.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: website-headline-angles-test". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.

---

Anything the person typed after the shortcut is extra instruction for this run: $ARGUMENTS
