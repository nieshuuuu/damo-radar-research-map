#!/usr/bin/env python3
"""README 的中文名总表由 data/names-final.json 生成，不要手改 README 的表格正文。
用法: python3 data/build_name_table.py   (原地改写 README.md 的 marker 区间)"""
import json, re, pathlib
ROOT = pathlib.Path(__file__).resolve().parent.parent
names = json.load(open(ROOT/'data/names-final.json', encoding='utf-8'))
meta  = json.load(open(ROOT/'data/authors-meta.json', encoding='utf-8'))  # 单位/身份/PANDA
rows = ['| # | 英文 | 中文 | 把握 | 单位 · 身份 | PANDA |', '|---:|---|---|:---:|---|:---:|']
for pos in sorted(names, key=int):
    n, m = names[pos], meta.get(pos, {})
    cn = f"**{n['cn']}**" if n['cn'] else '—'
    mk = {'✅ 确认':'✅','🟡 可能':'🟡','❓ 未知':'❓'}.get(n['conf'], '❓')
    rows.append(f"| {pos} | {n['en']} | {cn} | {mk} | {m.get('role','')} | {'✅' if m.get('panda') else ''} |")
table = '\n'.join(rows)
p = ROOT/'README.md'; txt = p.read_text(encoding='utf-8')
new = re.sub(r'(<!-- NAME-TABLE:START -->\n).*?(\n<!-- NAME-TABLE:END -->)',
             lambda m: m.group(1)+table+m.group(2), txt, flags=re.S)
p.write_text(new, encoding='utf-8')
print(f'名表已由 names-final.json 生成，{len(names)} 行')
