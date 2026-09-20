#!/usr/bin/env python3
"""把 archify 交付的 HTML 导成干净 PNG（隐掉 viewer 外壳，只留标题+图+卡片），供 README 内嵌。

用法: python3 figures/export-png.py radar-structure deeplesion-lineage
产物: figures/<name>.light.png / <name>.dark.png
"""
import subprocess, sys, tempfile, pathlib, re
from PIL import Image, ImageChops

CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
HERE = pathlib.Path(__file__).resolve().parent

INJECT = """
<style id="png-export">
  .toolbar, #guided-views, .no-print, .diagram-guide, .node-finder,
  #share-chapter-cue, #focus-chip { display: none !important; }
  body { margin: 0 !important; padding: 18px !important; }
  .container { max-width: none !important; }
</style>
<script>
  function forceTheme(){ document.documentElement.setAttribute('data-theme', '__THEME__'); }
  forceTheme(); addEventListener('load', forceTheme); setTimeout(forceTheme, 400);
</script>
"""

def trim(path):
    im = Image.open(path).convert("RGB")
    bg = Image.new("RGB", im.size, im.getpixel((2, 2)))
    bbox = ImageChops.difference(im, bg).getbbox()
    if bbox:
        pad = 12
        l, t, r, b = bbox
        box = (max(0, l - pad), max(0, t - pad), min(im.width, r + pad), min(im.height, b + pad))
        im.crop(box).save(path)
    return Image.open(path).size

# 每张图的导出窗口宽度：窗口比图宽会在面板右侧留白
WINDOW = {"radar-structure": (1560, 1250), "deeplesion-lineage": (1240, 1150)}

def export(name, theme, w=None, h=None):
    w, h = WINDOW.get(name, (1560, 1250)) if w is None else (w, h)
    src = HERE / f"{name}.html"
    html = src.read_text(encoding="utf-8")
    html = html.replace("</body>", INJECT.replace("__THEME__", theme) + "</body>")
    with tempfile.TemporaryDirectory() as td:
        tmp = pathlib.Path(td) / f"{name}.{theme}.html"
        tmp.write_text(html, encoding="utf-8")
        out = HERE / f"{name}.{theme}.png"
        subprocess.run([
            CHROME, "--headless", "--disable-gpu", "--hide-scrollbars",
            f"--window-size={w},{h}", "--virtual-time-budget=4000",
            "--default-background-color=00000000" if False else "--force-device-scale-factor=2",
            f"--screenshot={out}", tmp.as_uri(),
        ], check=True, capture_output=True)
        return out, trim(out)

if __name__ == "__main__":
    for name in sys.argv[1:]:
        for theme in ("light", "dark"):
            out, size = export(name, theme)
            print(f"{out.name:38s} {size[0]}x{size[1]}  {out.stat().st_size//1024} KB")
