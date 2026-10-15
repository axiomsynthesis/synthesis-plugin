---
name: making-the-call
description: >-
  Load for why something moved, what happens next, whether a number is good, strategy and scenario questions, market size and rivals, competitor prices, risks, and before recommending anything consequential.
---

# Making the call

This skill is a group of pages. Before you answer, read the ONE page below
that fits the question, then follow it. Read a second page only when the
question truly spans both. The paths are relative to this skill's folder.

**Every page is a pointer.** It says what it covers and how to fetch its
method from the server with `get_skill`. Make that call before you answer;
the page alone is not the method.

If the question is about one channel's number, open that channel's group first to get the number right, then come back here to judge it.

| Page | Open it when |
|---|---|
| `pages/benchmark-grammar/PAGE.md` | Before calling any metric good, bad, healthy, weak, strong or below target, before comparing a number to a benchmark, band, threshold, "industry average" or "what it should be", and before turning a cut-off you proposed into a… |
| `pages/reasoning-certificate/PAGE.md` | After the evidence about your brand is gathered and checked, and before writing a recommendation the answer rests on. |
| `pages/reasoning-gates/PAGE.md` | Before acting on any recommendation, "we should" claim, strategy call or rule of thumb about your brand, and before quoting a verdict from any of the challenge tools: "is this actually true for us", "what is the case against",… |
| `pages/challenge-and-premortem/PAGE.md` | Before giving a final recommendation on your brand, or when you push back on one: "are you sure?", "argue the other side", "what could go wrong", "what if we're wrong", "give me the opposite call", "that seems wrong". |
| `pages/reversibility-and-decision-doors/PAGE.md` | Before recommending a pause, kill, exit, channel stop, big inventory or supplier commitment, a price change, a large budget move, or any other consequential action for your brand: "should we pause Meta", "should we kill this… |
| `pages/decision-frameworks/PAGE.md` | Before running any strategy grid or option scorer: SWOT, BCG, Ansoff, Five Forces, Blue Ocean, a positioning map, a scenario grid, a war game, pros and cons, a priority ranking, a weighted scorecard or Kelly sizing ("score these… |
| `pages/decision-routing-and-constraint-layers/PAGE.md` | Before deciding how much effort a question deserves, before running a deep synthesis on a decision, before calling a decision reversible or one-way, before ranking findings by which layer of the business they sit in, before… |
| `pages/structural-assessment/PAGE.md` | When you ask for a full structural assessment, a brand health check, the full picture, a full diagnostic, or "where does my brand stand" / "what shape is the business in". |
| `pages/forecasting-and-trend-reads/PAGE.md` | Before saying what a number will do next or whether it has really changed: a revenue forecast or range, a "what has to go right" case, a belief update from a small test, a sustained-trend verdict, a break in a series, or a… |
| `pages/distribution-and-risk-reads/PAGE.md` | Before saying your business is concentrated, a move is real rather than noise, a metric has hit a tipping point, a plan survives a bad quarter, or a growth rate compounds ("how dependent are we on one product", "is this drop… |
| `pages/explain-a-metric-move/PAGE.md` | For any "why did this go up or down" question ("why is revenue down this month", "what drove the jump in July", "why did conversion fall", "is this growth real"), and before writing the words because, driven by, due to or thanks… |
| `pages/cross-signal-connections/PAGE.md` | When you want non-obvious patterns across channels, an "idea of the week", to know whether the way your business works has changed, or to test a relationship you believe in ("is our model still holding", "find me something we… |
| `pages/market-size-and-rivals/PAGE.md` | Before answering how big your market is, what share you hold, how crowded the category is, what a competitor's price cut or new channel means, what protects you from a copycat or an Amazon own-brand, or what the business might be… |
| `pages/competitor-shelf-and-price-checks/PAGE.md` | Before any live look at a competitor's Amazon listing, a keyword's search shelf, a Walmart.com shelf or a price across retailers ("what is the competitor charging now", "who ranks for this search", "where else is this sold and at… |
| `pages/outside-web-reads/PAGE.md` | Before reading anything from outside your own data: a web search, a competitor or news page, public mentions of a topic, a theme map over review text, or where a product ranks on the live Amazon shelf ("what are people saying… |

## When a page names another skill

Pages sometimes say "load <some-skill>". Those skills are pages in this
plugin's groups: every name is listed in `../start-here/INDEX.md`, and
`get_skill` takes the name directly, with or without the `ssi-` prefix.
