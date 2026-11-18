"""Render slide HTML files to 1080x1350 JPEGs.
Usage: python3 tools/render.py posts/<folder>   (renders every slide-*.html in it to slide-*.jpg)
Needs: pip install playwright --break-system-packages && python3 -m playwright install chromium  (or set CHROME=/usr/bin/google-chrome)
In slide HTML, reference photos as ASSET/<file>.jpg (files in assets/)."""
import os, sys, glob, asyncio
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
F=os.path.join(ROOT,'fonts')
faces=''
for fam,key,styles in [('Fraunces','fraunces',('normal','italic')),('Inter','inter',('normal',))]:
    for w in (400,600):
        for st in styles:
            for sub,rng in (('latin','U+0000-00FF,U+2000-206F,U+20AC'),('latin-ext','U+0100-024F')):
                faces+=f"@font-face{{font-family:{fam};font-weight:{w};font-style:{st};src:url(file://{F}/{key}-{sub}-{w}-{st}.woff2);unicode-range:{rng}}}\n"
def build(path):
    h=open(path).read().replace('ASSET/','file://'+os.path.join(ROOT,'assets')+'/')
    return h.replace('<head>',f'<head><style>{faces} body{{margin:0}}</style>',1)
async def main(folder):
    from playwright.async_api import async_playwright
    async with async_playwright() as p:
        kw={'args':['--allow-file-access-from-files']}
        if os.environ.get('CHROME'): kw['executable_path']=os.environ['CHROME']
        b=await p.chromium.launch(**kw); pg=await b.new_page(viewport={'width':1080,'height':1350})
        for src in sorted(glob.glob(os.path.join(folder,'slide-*.html'))):
            tmp=src+'.tmp.html'; open(tmp,'w').write(build(src))
            await pg.goto('file://'+os.path.abspath(tmp)); await pg.evaluate('document.fonts.ready'); await pg.wait_for_timeout(400)
            out=src[:-5]+'.jpg'; await pg.screenshot(path=out,type='jpeg',quality=92); os.remove(tmp); print(out)
        await b.close()
asyncio.run(main(sys.argv[1]))
