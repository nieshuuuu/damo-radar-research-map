#!/usr/bin/env python3
"""members/others.md 由本目录的 6 个片段 + data/names-final.json + data/authors-meta.json 生成。
改内容请改片段（members/_parts/*.md）或两个 JSON，再跑: python3 members/_parts/build.py"""
import json, pathlib, re
HERE = pathlib.Path(__file__).resolve().parent; ROOT = HERE.parent.parent
names = json.load(open(ROOT/'data/names-final.json', encoding='utf-8'))
meta  = json.load(open(ROOT/'data/authors-meta.json', encoding='utf-8'))
core  = {str(r['pos']) for r in json.load(open(ROOT/'data/raw/people/_roster.json', encoding='utf-8'))}
GROUPS = [
 ('一、达摩院研究员与在读学生', ['damo-junior-a', 'damo-junior-b'],
  '8 人。算法侧的执行层：达摩院的正式研究员，加上从西工大、Adelaide、浙大-西湖过来实习的博士生。'),
 ('二、浙大一院的临床团队', ['zju-hpb-surgery', 'zju-radiology-er'],
  '8 人。肝胆胰外科、放射科、急诊科。其中两位同时是外派医院的一把手 —— 外部验证中心是靠这条行政线接进来的。'),
 ('三、外部验证医院', ['grassroots-a', 'grassroots-b'],
  '9 人，来自 8 家医院。除嘉兴一院外，全部在浙大一院的托管 / 分院 / 对口支援体系内。'),
]
which = {}
for title, keys, _ in GROUPS:
    for k in keys:
        for pos in re.findall(r'^### #(\d+) ', (HERE/f'{k}.md').read_text(encoding='utf-8'), flags=re.M):
            which[pos] = title.split('、')[1]
out = ['# 其余 25 位作者', '',
 '> RADAR（*Science* 2026）40 位作者里，15 位核心作者各有单独一页（见 [../README.md](../README.md#15-位核心作者)），其余 25 位合在这里。',
 '> 条目比核心作者页短；在读学生和县医院医生的公开资料很少，缺的信息在条目末尾用「查不到」标出，不凑。',
 '> 照片只在所在医院 / 学校的官方个人页上直接有头像时才取，所以大多数人没有。', '',
 '## 速查', '', '| # | 姓名 | 分组 | 身份 |', '|---:|---|---|---|']
for pos in sorted((p for p in names if p not in core), key=int):
    n = names[pos]; cn = n['cn'] if n['cn'] and n['cn'] != '—' else ''
    out.append(f"| {pos} | {(cn + ' ') if cn else ''}{n['en']} | {which.get(pos, '')} | {meta[pos]['role']} |")
for title, keys, blurb in GROUPS:
    out += ['', '---', '', f'## {title}', '', blurb, '']
    for k in keys:
        out += [(HERE/f'{k}.md').read_text(encoding='utf-8').strip(), '']
out += ['---', '', '## See Also', '',
 '- [../README.md](../README.md) —— 总图与 40 位作者中文名总表',
 '- [../sources/grassroots-network.md](../sources/grassroots-network.md) —— 外部验证医院与浙大一院的托管关系',
 '- [../sources/academic-pipeline.md](../sources/academic-pipeline.md) —— 西工大 → Adelaide → MBZUAI 学术供给线',
 '- [../sources/damo-lineage.md](../sources/damo-lineage.md) —— NIH → 平安 PAII → 达摩院', '']
(ROOT/'members/others.md').write_text('\n'.join(out), encoding='utf-8')
missing = [p for p in names if p not in core and p not in which]
print(f"others.md: {sum(1 for p in names if p not in core)} 人；未在片段里找到的位次: {missing or '无'}")
