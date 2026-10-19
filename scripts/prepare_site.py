"""Synchronize the standalone presentation and responsive mobile layer into public/."""
from pathlib import Path
import re
import shutil

ROOT = Path(__file__).resolve().parents[1]
source = ROOT / 'prototype/apresentacao.html'
target = ROOT / 'public/index.html'
# Keep this script usable in a checkout that only contains the published files.
html = (source if source.exists() else target).read_text()
html = re.sub(r'\n?<!-- responsive-mobile:start -->.*?<!-- responsive-mobile:end -->\n?', '', html, flags=re.S)
html = re.sub(r'</script>\s*</html>$', '</script></html>', html)
css = (ROOT / 'scripts/mobile.css').read_text()
js = (ROOT / 'scripts/mobile.js').read_text()
block = ('\n<!-- responsive-mobile:start -->\n<style>\n' + css +
         '\n</style>\n<div id="mobile-app" hidden></div>\n<script>\n' + js +
         '\n</script>\n<!-- responsive-mobile:end -->\n')
html = html.replace('</html>', block + '</html>')
target.parent.mkdir(exist_ok=True)
target.write_text(html)
if source.exists():
    source.write_text(html)
figcraft = ROOT / 'prototype/AmigoPet-Gestao.figcraft'
if figcraft.exists():
    shutil.copyfile(figcraft, ROOT / 'public/AmigoPet-Gestao.figcraft')
print('Prepared public/index.html with responsive mobile presentation.')
