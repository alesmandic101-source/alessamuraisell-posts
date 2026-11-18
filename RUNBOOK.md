# Runbook: publish ONE Instagram post for @alessamuraisell

For scheduled runs. Aleš is not watching: never ask questions, decide and report.

1. **Get the repo.** Attach `alesmandic101-source/alessamuraisell-posts` with push access (add_repo), clone it, then `git pull`.
2. **Read** BRAND.md, QUEUE.md and LOG.md. If LOG.md already has a post dated today (Europe/Ljubljana), stop and report "already posted today".
3. **Pick the post.**
   - First item in QUEUE.md marked READY → use its images and caption as they are.
   - No READY item → read INSIGHTS.md first ("Lean the next 1–2 new posts toward", and the topic ideas from comments), then write a new one following BRAND.md. Never copy or repeat an earlier post; default to fresh content. Choose a content type different from the last LOG.md entry, and a topic not used before (check LOG.md and posts/). Copy 3 templates from templates/ into `posts/NN-short-name/slide-1.html` … `slide-3.html` (NN = next number) and change only the text (and the photo, from assets/ only). Keep headlines short enough to fit; 2–3 lines max at the template's font size.
4. **Render** (new posts only): `pip install playwright --break-system-packages`; if `/usr/bin/google-chrome` exists run `CHROME=/usr/bin/google-chrome python3 tools/render.py posts/NN-short-name`, otherwise `python3 -m playwright install chromium` first and run without CHROME. Open every JPEG and look at it: no text cut off or overlapping, his face visible. Fix and re-render if not.
   **Quality check before going further (new posts):** every slide has the red "A" seal, @alessamuraisell, slide count on carousels, his face somewhere in the post, no spelling mistakes, no text cut off or touching another element, no invented numbers or client results, caption 60–150 words in his voice (BRAND.md). If anything fails, fix it; if it can't be fixed, publish the next READY item instead, or nothing.
5. **Push** the post folder to `main` (commit author "Aleš Mandič" <alesmandic101-source@users.noreply.github.com>). Run `git pull --rebase` first. Then wait 60 seconds so GitHub serves the new images.
6. **Publish** with the Windsor.ai for Social Media connector: connector `instagram`, account `17841422405541422`.
   - Carousel: action `create_carousel_post`, `image_urls` = `https://raw.githubusercontent.com/alesmandic101-source/alessamuraisell-posts/main/posts/NN-short-name/slide-1.jpg` (…slide-2, slide-3), in order, plus `caption`.
   - Single image: action `create_image_post` with `image_url` and `caption`.
   If publishing fails, retry once after 60 s. If it still fails, do not post anything else; report the error.
7. **Record**: add a row to LOG.md (date, folder, type, media id). In QUEUE.md change that item's READY to PUBLISHED <date>. Push.
8. **Keep a buffer:** if fewer than 2 READY items are left in QUEUE.md, create ONE new post (steps 3–5, do NOT publish it), add it to QUEUE.md as READY with its caption, and push. This way every post is prepared and checked days before it goes out.
9. **Report** in 2–3 lines: what was posted, the Instagram media id, and anything Aleš needs to do (e.g. "send a pool photo"). If something failed, start the report with "NOT POSTED:" and the reason.

Never: post children, use photos of other people without a consent note in QUEUE.md, invent results/clients/numbers, post more than one item per run, or change BRAND.md.
