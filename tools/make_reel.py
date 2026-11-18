"""Build a 1080x1920 Reel from scene HTML files.
Usage: python3 tools/make_reel.py posts/<folder>
The folder needs reel.json: {"fade": 0.35, "scenes": [{"file": "scene-1.html", "dur": 2.8, "zoom": true}, ...]}
Outputs posts/<folder>/reel.mp4 (H.264, 30 fps, silent AAC track) and cover.jpg (first scene).
Keep text inside the Reels safe area: top 200px to 1550px from the top, 72px side margins.
Needs ffmpeg and playwright (see tools/render.py)."""
import os, sys, json, asyncio, subprocess
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import importlib.util
spec = importlib.util.spec_from_file_location('r', os.path.join(os.path.dirname(os.path.abspath(__file__)), 'render.py'))
src = open(spec.origin).read().split('async def main')[0]   # reuse font faces + build()
ns = {'__file__': spec.origin}; exec(src, ns); build = ns['build']

async def shoot(folder, files):
    from playwright.async_api import async_playwright
    async with async_playwright() as p:
        kw = {'args': ['--allow-file-access-from-files']}
        if os.environ.get('CHROME'): kw['executable_path'] = os.environ['CHROME']
        b = await p.chromium.launch(**kw); pg = await b.new_page(viewport={'width': 1080, 'height': 1920})
        outs = []
        for f in files:
            path = os.path.join(folder, f); tmp = path + '.tmp.html'; open(tmp, 'w').write(build(path))
            await pg.goto('file://' + os.path.abspath(tmp)); await pg.evaluate('document.fonts.ready'); await pg.wait_for_timeout(400)
            out = path[:-5] + '.png'; await pg.screenshot(path=out); os.remove(tmp); outs.append(out)
        await b.close(); return outs

def main(folder):
    cfg = json.load(open(os.path.join(folder, 'reel.json'))); fade = cfg.get('fade', 0.35); sc = cfg['scenes']
    pngs = asyncio.run(shoot(folder, [s['file'] for s in sc]))
    cmd = ['ffmpeg', '-y', '-loglevel', 'error']
    for s, p in zip(sc, pngs): cmd += ['-loop', '1', '-framerate', '30', '-t', str(s['dur']), '-i', p]
    cmd += ['-f', 'lavfi', '-i', 'anullsrc=channel_layout=stereo:sample_rate=44100']
    f = []
    for i, s in enumerate(sc):
        if s.get('zoom'):
            n = int(s['dur'] * 30)
            f.append(f"[{i}:v]scale=2160:3840,zoompan=z='min(1+0.06*on/{n},1.06)':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=1:s=1080x1920:fps=30,setsar=1,format=yuv420p[v{i}]")
        else:
            f.append(f"[{i}:v]scale=1080:1920,fps=30,setsar=1,format=yuv420p[v{i}]")
    cum = sc[0]['dur']; last = 'v0'
    for i in range(1, len(sc)):
        off = round(cum - fade, 3); f.append(f"[{last}][v{i}]xfade=transition=fade:duration={fade}:offset={off}[x{i}]"); last = f'x{i}'; cum = off + sc[i]['dur']
    out = os.path.join(folder, 'reel.mp4')
    cmd += ['-filter_complex', ';'.join(f), '-map', f'[{last}]', '-map', f'{len(sc)}:a', '-shortest',
            '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '20', '-pix_fmt', 'yuv420p', '-r', '30',
            '-c:a', 'aac', '-b:a', '128k', '-movflags', '+faststart', '-t', str(round(cum, 2)), out]
    subprocess.run(cmd, check=True)
    from PIL import Image
    Image.open(pngs[0]).convert('RGB').save(os.path.join(folder, 'cover.jpg'), quality=90)
    for p in pngs: os.remove(p)
    print(out, round(cum, 2), 's')

main(sys.argv[1])
