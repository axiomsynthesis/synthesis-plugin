---
name: checking-the-numbers
description: >-
  Load for rules that apply to any figure in any channel: reading warnings on a tool result, empty or missing data, whether recent data has settled, comparing like with like, metric definitions, naming products, raw data, and checking a draft before it goes out. A question about one channel's number goes to that channel's group first.
---

# Checking the numbers

This skill is a group of pages. Before you answer, read the ONE page below
that fits the question, then follow it. Read a second page only when the
question truly spans both. The paths are relative to this skill's folder.

**Every page is a pointer.** It says what it covers and how to fetch its
method from the server with `get_skill`. Make that call before you answer;
the page alone is not the method.

If the number belongs to one channel (Amazon, ads, social, the online store, retail, finance), open that channel's group first; its pages carry the channel's own traps. Use these pages for the rules that sit across every channel.

| Page | Open it when |
|---|---|
| `pages/read-the-governed-metric-result/PAGE.md` | The moment a Synthesis tool result lands and before any number from it is stated. |
| `pages/provenance-and-truth-layer/PAGE.md` | Before stating, charting or comparing any number, or before saying how sure you are of a claim. |
| `pages/question-the-source/PAGE.md` | When a tool comes back empty, blank, refused or "not available", when a number looks too low or a chart falls off a cliff, when a deep analysis lost some of its analysts, or before you write "we have no X" or "there is no data on… |
| `pages/data-integrity-scan/PAGE.md` | After pulling data and again on the draft, before any conclusion, and whenever two metrics disagree ("orders are down but customers are up", "why does this not match my dashboard?", "is this drop real?"). |
| `pages/compare-like-with-like/PAGE.md` | Before ranking products or cohorts, saying "X beats Y", quoting a ratio, share, month-to-date, projection or year-over-year change, or deciding that two numbers conflict ("is product A doing better than product B", "which cohort… |
| `pages/data-maturity-and-settling-windows/PAGE.md` | Before any week-over-week, month-over-month, year-over-year, "latest week", "this month so far" or recent-period comparison, or before quoting a fresh figure from any source ("why did sales drop this week", "what happened… |
| `pages/deal-events-in-trends-and-projections/PAGE.md` | When a month, week or year-over-year window contains or sits beside a deal event such as Prime Day, Prime Big Deal Days, the Amazon Spring Sale, Black Friday and Cyber Monday, or your own sale ("what will this month land at",… |
| `pages/metric-definitions-and-citation/PAGE.md` | Before quoting any named KPI (revenue, repeat rate, LTV, new or returning customers, cross-sell, AOV, days of cover, CAM, MER, TACoS), when you ask "what does this metric mean", "how is this calculated", "what counts as a new… |
| `pages/operator-number-disagrees/PAGE.md` | When someone on your team, your spreadsheet, your agency or an ad platform quotes a figure that differs from the one Synthesis returns: "we did 10 orders a day", "that was our best day ever", "the dashboard says something else",… |
| `pages/operator-sheets-reading-and-grounding/PAGE.md` | For any answer that reads one of your connected Google Sheets: a target, a budget, a plan, a tracker, a KPI workbook, a creator offer sheet ("what is our target this month", "what did we plan to spend", "what does the tracker say… |
| `pages/product-identity-resolution/PAGE.md` | Whenever you ask about a product, a pack size, a bundle, a range or family, or an item code, or want products grouped ("how is the 9-pack doing", "compare the single and the 2-pack", "what does this range earn", "what is B0... |
| `pages/product-display-names/PAGE.md` | Whenever a table, chart label, legend or sentence is about to name one of your products, or when a draft shows a bare item code, a name cut off with "…", a note such as "(top seller)" inside a name, or two rows with the same… |
| `pages/audit-your-draft/PAGE.md` | Before sending any answer, memo, deck text or report narrative that states your brand's figures, and whenever someone asks "are these numbers right?", "did you check this?" or "can I send this to my team?". |
| `pages/revise-without-corrupting-numbers/PAGE.md` | Before any rewrite, repair, fix-up, plain-English, shortening or polish pass over text that already contains your brand's figures: "fix these lines", "make this readable", "tighten this answer", "cut this in half", "correct that… |
| `pages/warehouse-discovery-and-guarded-sql/PAGE.md` | When no metric tool answers the question, when you want a figure pulled "straight from the data", when checking whether data is fresh or complete ("is this up to date?", "why is this empty?", "did this stop syncing?"), when a… |
| `pages/long-tail-connectors-reading/PAGE.md` | When a question touches Fairing, Triple Whale, Instacart, Loop Returns, ShipHero, ShipStation, Stay Ai, Yotpo, Crisp, Mailchimp, Customer.io, ActiveCampaign or Campaign Monitor, or what they measure: "what does our… |

## When a page names another skill

Pages sometimes say "load <some-skill>". Those skills are pages in this
plugin's groups: every name is listed in `../start-here/INDEX.md`, and
`get_skill` takes the name directly, with or without the `ssi-` prefix.
