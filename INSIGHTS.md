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
| 01-intro | 18101627624208574 | 2026-11-18 | 15 | 0 | 0 | 0 | 1 | 0 | 0.13 | no (all others score 0, rule not meaningful yet) |
| 07-reel-stop-guessing | 18111007739241804 | 2026-11-19 | 13 | 0 | 0 | 0 | 0 | 0 | 0.00 | no |
| 03-how-an-audit-works | 17928707355199440 | 2026-11-21 | 1 | 0 | 0 | 0 | 0 | 0 | 0.00 | no |
| 02-comments-waitlist | 18143348698615567 | 2026-11-22 | 4 | 0 | 0 | 0 | 0 | 0 | 0.00 | no |

## Learnings (max 10 bullets, newest first, keep only what still holds)
- All 4 posts are now judged, but no standouts: every post except the intro scores 0, so the 1.5×-median rule can't separate anything yet (median is 0). Only call a standout once the median of the others is above 0.
- Account is brand new: reach 1–15 per post, no likes or comments yet. Intro carousel (27 views, 3 profile visits, 1 share) and first Reel (22 views) reached the most; the two later carousels reached only 1–4. Too small to read as a format signal yet.

## Lean the next 1–2 new posts toward
- Nothing yet: keep rotating content types per BRAND.md.

## Topic ideas from comments and DMs
- (empty)
