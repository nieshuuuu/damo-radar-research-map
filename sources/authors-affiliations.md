# 作者与单位 —— 结构分析

> 全部从 **PubMed eutils** 原始 XML 抽取，不是人工转录。
> `curl "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=42752131&retmode=xml"`
> 原始 XML 存档在 [`../data/pubmed-42752131.xml`](../data/pubmed-42752131.xml)，结构化结果在 [`../data/authors-raw.json`](../data/authors-raw.json)、[`../data/radar-authors.tsv`](../data/radar-authors.tsv)。
> 抽取日期：2026-09-20。

---

## 作者位次的头尾

```
 1  章琦 Qi Zhang          浙大一院肝胆胰外科            ← 第一作者（共 6 位共同一作，前六位）
 ...
36  居胜红 Shenghong Ju     东南大学中大医院放射科
37  Jianfeng Zhang          达摩院 · 湖畔实验室
38  肖文波 Wenbo Xiao       浙大一院放射科
39  张灵 Ling Zhang         达摩院 · Washington DC        ← AI 侧资深作者
40  梁廷波 Tingbo Liang     浙大一院肝胆胰外科            ← 末位通讯
```

共 **40 位作者**（PubMed 与 Crossref 一致）。PubMed XML 的 `EqualContrib="Y"` 标在前六位。

---

## 七个板块

```
B 浙大一院                      13 人   ← 临床/数据主干
A 达摩院 + 湖畔实验室            11 人   ← AI 主干
G 基层医院（县/区/兵团）          9 人   ← 外部验证网络
D 海外学术 Adelaide / MBZUAI      3 人   ← 视觉-语言方法供给
C 浙大计算机学院                  2 人
E 宁波市第二医院                  1 人
F 东南大学中大医院                1 人
                              ─────
                               40 人
```

统计口径：一个人挂多个单位时按"最上游"归一个板块（DAMO/湖畔 > 浙大一院 > 浙大计算机 > 海外 > 其他）。复现命令见本页末尾。

---

## 名单

40 位作者的中文名、身份与把握等级见 **[../README.md#40-位作者中文名总表](../README.md#40-位作者中文名总表)**（由 `data/names-final.json` + `data/authors-meta.json` 生成，这里不重复）。论文原文的单位串见 [`../data/radar-authors.tsv`](../data/radar-authors.tsv)。

---

## 光看单位就能读出来的三件事

### ① 第一作者是外科医生，末位通讯是医院院长

- **#1 章琦 Qi Zhang** 挂的是浙大一院**肝胆胰外科**，不是任何计算机单位；同时是该院党委副书记。
- **#40 梁廷波 Tingbo Liang** 同科室，是该院**院长、党委副书记**，第十四届全国人大代表（2018-12 至 2025-07 任党委书记）→ [zju-hospital.md](zju-hospital.md)。

==AI 侧的资深作者 Ling Zhang 排在 #39，是倒数第二位。== 这个排法在中文医学期刊语境里读法很清楚：临床方拥有这项工作。

### ② PANDA → RADAR 的连续性

两篇论文的作者名做交集，**只有四个人重合**，而且单位在两篇里一致：

| 姓名 | PANDA (Nat Med 2023) 单位 | RADAR (Science 2026) 单位 |
|---|---|---|
| **Qi Zhang** | 浙大一院肝胆胰外科 | 同 |
| **Tingbo Liang** | 浙大一院肝胆胰外科 | 同 |
| **Ling Zhang** | DAMO Academy, **New York** | DAMO Academy, **Washington DC** |
| **Yingda Xia** | DAMO Academy, **New York** | DAMO Academy, **Washington DC** |

✓ 同一个外科科室 + 同一个达摩院美国团队，隔三年。
💡 达摩院美国现在是 **New York 与 Washington DC 两个点并存**：DC 是张灵 + 夏英达的平扫 CT 早筛线，NY 是 Dakai Jin 等人的头颈放疗线 → [damo-lineage.md](damo-lineage.md)。

> [!insight] 424,911 例的数据访问不是第一次取款
> 是 PANDA（2023-11, Nature Medicine, PMID 37985692）打开的那个账户的第二次。
> 这条直接回答"是不是国家支持就能拿到好数据"——顺序是**先交付，再拿数据**。

### ③ 宁波市第二医院放射科：其实是一条西工大线

三个人挂这家医院：

```
#4  Zilin Lu        达摩院 + 宁波二院放射科
#11 Shaoteng Zhang  达摩院 + 宁波二院放射科
#13 夏勇 Yong Xia   宁波二院放射科（论文给的唯一单位）
```

==#13 就是西北工业大学计算机学院的夏勇教授；#4 和 #11 是他在读的博士生，在达摩院实习。== 论文的 26 个单位里"西北工业大学"一次都没出现，这个单位编号是这条线的落点，不是一群放射科医生。证据链见 [academic-pipeline.md](academic-pipeline.md)。

---

## 跨机构桥梁（挂 2 个以上单位的 13 人）

这些人是结构上的连接点：

| 人 | 连接的是 |
|---|---|
| #1 Qi Zhang · #40 Tingbo Liang | 临床科室 ↔ 两个重点实验室 |
| #2 Jianpeng Zhang · #3 Weiwei Cao · #18 Yanjie Zhou | 达摩院 ↔ 湖畔实验室 ↔ 浙大计算机学院（三重）|
| #4 Zilin Lu · #11 Shaoteng Zhang | 达摩院 ↔ 宁波二院放射科 |
| #23 马涛 Tao Ma | 浙大一院 ↔ 新疆兵团第一师医院 —— 中组部第十一批援疆领队，任该院党委副书记兼院长 |
| #33 张微 Wei Zhang | 浙大一院 ↔ 杭州余杭区第一人民医院（浙大一院良渚分院）|
| #5 Wanxing Chang · #17 Zhilin Zheng · #19 Tony C W Mok · #37 Jianfeng Zhang | 达摩院 ↔ 湖畔实验室 |

> [!strategy] 三重挂名（达摩院+湖畔+浙大计算机）是最值得追的
> 它说明湖畔实验室不是一个挂名单位，而是达摩院和浙大之间的正式通道。→ [hupan-lab.md](hupan-lab.md)

---

## 复现

```bash
curl -sL "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=42752131&retmode=xml" > data/pubmed-42752131.xml
curl -sL "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=37985692&retmode=xml" > data/pubmed-37985692-panda.xml
```

作者抽取与板块统计脚本见 [`../data/`](../data/) 目录；两篇的交集用精确姓名匹配（对 `Qi Zhang` 这种高频名，另外核对了单位串一致）。

---

## See Also

- [radar-technical-teardown.md](radar-technical-teardown.md) —— 源码级技术拆解
- [../README.md](../README.md) —— 总图
