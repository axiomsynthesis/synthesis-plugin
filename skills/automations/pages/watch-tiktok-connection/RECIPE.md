# Check TikTok is still connected and sending data

Channel: TikTok Ads · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Check TikTok is still connected and sending data" (id: watch-tiktok-connection, TikTok Ads).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
TikTok makes you re-approve ad access every 30 days. Refreshing does not extend it. If nobody reconnects, ad data quietly stops. This proves the connection still works by reading real report rows, not by checking that a token is saved. It warns a week before the cutoff and catches ad accounts that were left unticked. Run it weekly, or daily in the last week.

What to read: TikTok's 30-day ad authorization, which ad accounts sync, yesterday's spend rows and the shop data dates
What to give me: Days left before TikTok data stops, any ad account that dropped out, and the exact reconnect step

Synthesis tools to use:
- `cost_rules for=watch-tiktok-connection`
- `tiktok_metric metric=coverage`
- `tiktok_metric metric=spend_trend months=2`
- `tiktok_metric metric=shop_sales_trend months=1`
- `data_freshness`
- `ad_health_check only=tiktok_ads`

Steps:
1. Call `tiktok_metric` with `metric=coverage`. Read every ad account TikTok lists, which ones actually sync, and over what dates. Each account's `last_day` is its newest spend day. This is the real test that the connection works.
2. Call `tiktok_metric` with `metric=spend_trend` and `months=2`. Read `feed.expires_on` for the cutoff date and `feed.expires_in_days` for days left. Read the closed month and this month so far for spend at risk.
3. Call `tiktok_metric` with `metric=shop_sales_trend` and `months=1` if the brand has a TikTok Shop. The shop uses a separate connection with its own dates.
4. Call `data_freshness` for the last sync date of TikTok ads and TikTok Shop.
5. Call `ad_health_check` with `only=["tiktok_ads"]` for the server's own pass or fail on the TikTok connection.
6. Warn when 7 or fewer days are left. Warn when an ad account TikTok lists is not syncing. Warn when the newest spend day is more than 2 days old while the account still had spend the month before.
7. An unticked account with no spend history may belong to an agency or another business. Ask before telling them to tick it. Ticking it could pull someone else's spend into your numbers.
8. Give the reconnect step: Data, then Connections, then Reconnect TikTok Ads. On TikTok's screen, tick every ad account that is yours before you approve. On one live brand, 3 of 7 were left unticked at a reconnect and their data stopped without notice.
9. After a reconnect, run steps 1 and 2 again the next day. Pass only when every ad account shows yesterday as its newest day.

Checks before answering:
- Safe test: this only reads. Nothing in TikTok changes. To test it, run it on a brand whose cutoff is near and confirm it names the right date.
- Spend: say this month's spend so far and the spend a day. That is the spend that goes unmeasured after the cutoff.
- A token that exists is not a passing check. Only a recent spend row proves the connection works.
- If coverage shows no TikTok connection, say TikTok ads are not connected. Never say spend is zero.
- A sync that ran but read no ad accounts is an error, never "all fine".
- An account with no spend for weeks may simply be paused. Say so instead of calling it broken.

Output:
- One line first: days left, the date data stops and the warning date a week before it. Or "connected, data current to <date>".
- Each ad account: synced yes or no, newest spend day, spend this month so far.
- The reconnect step when it is needed, with "tick every ad account that is yours".

Never:
- Never reconnect, approve or change the connection for the person. Reconnecting is their click.
- Never call the connection healthy from a saved token alone.
- Never fill a missing day with an estimate.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Before step 1, call cost_rules. If it returns questions, ask them in one message as written (dollars, choices, what skip does) and save each answer with set_cost_rule. On a scheduled run, use the defaults and list the questions at the end. End the answer with its used_line.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: watch-tiktok-connection". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
