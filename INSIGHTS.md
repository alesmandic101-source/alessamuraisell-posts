# What we're learning (updated daily)

## How the daily check works
Each day: pull every post's numbers through the Windsor.ai for Social Media connector (connector `instagram`, account `17841422405541422`), using get_data with the fields
`media_id, timestamp, media_type, media_reach, media_views, media_total_like_count, media_total_comments_count, media_saved, media_shares, media_follows, media_profile_visits`
and `date_preset: "last_28dT"` (the Windsor trial only reads the last 30 days; "last_2yearsT" errors. Once posts are older than 28 days, keep their last recorded numbers). Also read the comments (`comment_text, comment_timestamp, media_id`).

Score per post = (likes + 3×comments + 3×saves + 2×shares + 5×follows) ÷ max(reach, 1). Judge a post only once it's at least 48 hours old.
A post is a **standout** when its score is at least 1.5× the median score of the other judged posts, and at least 4 posts have been judged. Before that, there isn't enough data: just record the numbers.

## How learnings are used (Aleš's rule)
- Never repeat or copy a post that did well.
- After a standout, make the next 1 or 2 NEW posts *a bit similar*: same type, a related angle or the same format. Then go back to fresh content.
- Default is always new content, unless the data clearly says otherwise.
- Questions people ask in comments are the best source of new topics. Add them as ideas below.

## Numbers
| Folder | Media id | Published | Reach | Likes | Comments | Saves | Shares | Follows | Score | Standout |
|---|---|---|---|---|---|---|---|---|---|---|
| 01-intro | 18101627624208574 | 2026-11-18 | 14 | 0 | 0 | 0 | 1 | 0 | 0.14 | judged (need 4 judged to call standouts) |
| 07-reel-stop-guessing | 18111007739241804 | 2026-11-19 | 12 | 0 | 0 | 0 | 0 | 0 | 0.00 | judged (need 4 judged to call standouts) |
| 03-how-an-audit-works | 17928707355199440 | 2026-11-21 | 0 | 0 | 0 | 0 | 0 | 0 | 0.00 | too new |

## Learnings (max 10 bullets, newest first, keep only what still holds)
- None yet. The account is brand new (reach 12–14 per post, no likes or comments yet), so don't over-read anything. Intro carousel: 26 views, 3 profile visits and 1 share from 14 reached; first Reel: 19 views from 12 reached. 2 of 4 posts needed for standout calls are judged.

## Lean the next 1–2 new posts toward
- Nothing yet: keep rotating content types per BRAND.md.

## Topic ideas from comments and DMs
- (empty)
