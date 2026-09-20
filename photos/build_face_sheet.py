#!/usr/bin/env python3
"""认人速查表：由 photos/*.jpg + data/raw/people/_roster.json + data/authors-meta.json 生成。
用法: python3 photos/build_face_sheet.py  → photos/face-sheet.jpg 与 photos/thumbs/*.jpg"""
import json, pathlib
from PIL import Image, ImageDraw, ImageFont, ImageOps
ROOT = pathlib.Path(__file__).resolve().parent.parent
roster = json.load(open(ROOT/'data/raw/people/_roster.json', encoding='utf-8'))
TAG = {1:'一作 · 肝胆胰外科 · 院党委副书记', 2:'共一 · 达摩院 · 技术主力', 3:'共一 · 达摩院', 12:'MBZUAI 助理教授',
       13:'西工大教授 · 计算机学院副院长', 14:'Adelaide 副教授 · V3ALab', 16:'浙大计算机 · 求是特聘教授',
       19:'达摩院 · 配准', 20:'达摩院 Washington DC', 22:'浙大一院放疗科副主任', 35:'浙大一院副院长 · 消化内科',
       36:'东南大学中大医院副院长', 38:'浙大一院放射科（主持工作）', 39:'AI 侧资深作者 · 达摩院 DC', 40:'末位通讯 · 浙大一院院长'}
def font(size, bold=False):
    for p in ['/System/Library/Fonts/PingFang.ttc', '/System/Library/Fonts/STHeiti Medium.ttc', '/System/Library/Fonts/Hiragino Sans GB.ttc']:
        if pathlib.Path(p).exists():
            return ImageFont.truetype(p, size, index=1 if bold and 'PingFang' in p else 0)
    return ImageFont.load_default()
W, H, PAD, COLS = 230, 300, 22, 5
CELL_W, CELL_H = W + PAD, H + 96
rows = (len(roster) + COLS - 1) // COLS
sheet = Image.new('RGB', (COLS*CELL_W + PAD, rows*CELL_H + PAD + 56), 'white')
d = ImageDraw.Draw(sheet)
d.text((PAD, 14), 'DAMO RADAR（Science 2026）· 15 位核心作者', fill='#111', font=font(26, True))
(ROOT/'photos/thumbs').mkdir(exist_ok=True)
for i, r in enumerate(roster):
    x = PAD + (i % COLS)*CELL_W; y = 56 + (i // COLS)*CELL_H
    p = ROOT/f"photos/{r['slug']}.jpg"
    if p.exists():
        im = ImageOps.fit(Image.open(p).convert('RGB'), (W, H), method=Image.LANCZOS, centering=(0.5, 0.35))
        ImageOps.fit(Image.open(p).convert('RGB'), (180, 235), method=Image.LANCZOS, centering=(0.5, 0.35)).save(ROOT/f"photos/thumbs/{r['slug']}.jpg", quality=88)
    else:
        im = Image.new('RGB', (W, H), '#eef0f3'); dd = ImageDraw.Draw(im)
        dd.text((W//2, H//2), '无公开照片', fill='#8a9099', font=font(20), anchor='mm')
    sheet.paste(im, (x, y)); d.rectangle([x, y, x+W-1, y+H-1], outline='#d0d4da')
    cn = r['cn'] if r['cn'] and r['cn'] != '—' else ''
    d.text((x, y+H+8), f"#{r['pos']}  {cn or r['en']}", fill='#111', font=font(21 if cn else 18, True))
    d.text((x, y+H+36), r['en'] if cn else 'Tony Chi Wing MOK', fill='#444', font=font(15))
    d.text((x, y+H+58), TAG.get(r['pos'], ''), fill='#777', font=font(13))
sheet.save(ROOT/'photos/face-sheet.jpg', quality=90)
print('face-sheet', sheet.size, '| thumbs', len(list((ROOT/'photos/thumbs').glob('*.jpg'))))
