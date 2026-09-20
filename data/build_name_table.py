#!/usr/bin/env python3
"""README 的中文名总表由 data/names-final.json 生成，不要手改 README 的表格正文。
用法: python3 data/build_name_table.py   (原地改写 README.md 的 marker 区间)"""
import json, re, pathlib
ROOT = pathlib.Path(__file__).resolve().parent.parent
names = json.load(open(ROOT/'data/names-final.json', encoding='utf-8'))
meta  = json.load(open(ROOT/'data/authors-meta.json', encoding='utf-8'))  # 单位/身份/PANDA
rows = ['| # | 英文 | 中文 | 把握 | 单位 · 身份 | PANDA |', '|---:|---|---|:---:|---|:---:|']
roster = {str(r['pos']): r for r in json.load(open(ROOT/'data/raw/people/_roster.json', encoding='utf-8'))}
for pos in sorted(names, key=int):
    n, m = names[pos], meta.get(pos, {})
    page = f"members/{roster[pos]['slug']}.md" if pos in roster else None
    if page: n = dict(n, en=f"[{n['en']}]({page})")
    cn = f"**{n['cn']}**" if n['cn'] and n['cn'] != '—' else '—'
    mk = {'✅ 确认':'✅','🟡 可能':'🟡','❓ 未知':'❓'}.get(n['conf'], '❓')
    rows.append(f"| {pos} | {n['en']} | {cn} | {mk} | {m.get('role','')} | {'✅' if m.get('panda') else ''} |")
table = '\n'.join(rows)
# 核心作者缩略图表
mrows = ['| 照片 | 姓名 | # | 身份 |', '|:---:|---|---:|---|']
for pos in sorted(roster, key=int):
    r = roster[pos]; cn = r['cn'] if r['cn'] and r['cn'] != '—' else ''
    thumb = ROOT/f"photos/thumbs/{r['slug']}.jpg"
    img = f'<img src="photos/thumbs/{r["slug"]}.jpg" width="80">' if thumb.exists() else '—'
    who = f"**[{cn} {r['en']}](members/{r['slug']}.md)**" if cn else f"**[{r['en']}](members/{r['slug']}.md)**"
    mrows.append(f"| {img} | {who} | {pos} | {meta.get(pos, {}).get('role', '')} |")
members_table = '\n'.join(mrows)
p = ROOT/'README.md'; txt = p.read_text(encoding='utf-8')
txt = re.sub(r'(<!-- MEMBERS:START -->\n).*?(\n<!-- MEMBERS:END -->)', lambda m: m.group(1)+members_table+m.group(2), txt, flags=re.S)
new = re.sub(r'(<!-- NAME-TABLE:START -->\n).*?(\n<!-- NAME-TABLE:END -->)',
             lambda m: m.group(1)+table+m.group(2), txt, flags=re.S)
p.write_text(new, encoding='utf-8')
print(f'名表已由 names-final.json 生成，{len(names)} 行')
