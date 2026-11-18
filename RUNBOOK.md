# Runbook: publish ONE Instagram post for @alessamuraisell

For scheduled runs. Aleš is not watching: never ask questions, decide and report.

1. **Get the repo.** Attach `alesmandic101-source/alessamuraisell-posts` with push access (add_repo), clone it, then `git pull`.
2. **Read** BRAND.md, QUEUE.md and LOG.md. If LOG.md already has a post dated today (Europe/Ljubljana), stop and report "already posted today".
3. **Pick the post.**
   - First item in QUEUE.md marked READY → use its images and caption as they are.
   - No READY item → write a new one following BRAND.md: choose a content type different from the last LOG.md entry, and a topic not used before (check LOG.md and posts/). Copy 3 templates from templates/ into `posts/NN-short-name/slide-1.html` … `slide-3.html` (NN = next number) and change only the text (and the photo, from assets/ only). Keep headlines short enough to fit; 2–3 lines max at the template's font size.
4. **Render** (new posts only): `pip install playwright --break-system-packages`; if `/usr/bin/google-chrome` exists run `CHROME=/usr/bin/google-chrome python3 tools/render.py posts/NN-short-name`, otherwise `python3 -m playwright install chromium` first and run without CHROME. Open every JPEG and look at it: no text cut off or overlapping, his face visible. Fix and re-render if not.
5. **Push** the post folder to `main` (commit author "Aleš Mandič" <alesmandic101-source@users.noreply.github.com>).
6. **Publish** with the Windsor.ai for Social Media connector: connector `instagram`, account `17841422405541422`.
   - Carousel: action `create_carousel_post`, `image_urls` = `https://raw.githubusercontent.com/alesmandic101-source/alessamuraisell-posts/main/posts/NN-short-name/slide-1.jpg` (…slide-2, slide-3), in order, plus `caption`.
   - Single image: action `create_image_post` with `image_url` and `caption`.
   If publishing fails, retry once after 60 s. If it still fails, do not post anything else; report the error.
7. **Record**: add a row to LOG.md (date, folder, type, media id). In QUEUE.md change that item's READY to PUBLISHED <date>. Push.
8. **Report** in 2–3 lines: what was posted, the Instagram media id, and anything Aleš needs to do (e.g. "send a pool photo").

Never: post children, use photos of other people without a consent note in QUEUE.md, invent results/clients/numbers, post more than one item per run, or change BRAND.md.
