# 作者与单位 —— 骨架表

> 全部从 **PubMed eutils** 原始 XML 抽取，不是人工转录。
> `curl "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=42752131&retmode=xml"`
> 原始 XML 存档在 [`../data/pubmed-42752131.xml`](../data/pubmed-42752131.xml)，结构化结果在 [`../data/authors-raw.json`](../data/authors-raw.json)、[`../data/radar-authors.tsv`](../data/radar-authors.tsv)。
> 抽取日期：2026-09-20。

---

## ⚠️ 先更正一处：是 40 位作者，不是 39

PubMed 返回 40 个 `<Author>` 节点。Science 的引用格式和各处转载的名单也都是 40 个人 —— 容易数错是因为末尾连着三个姓张的（Jianfeng Zhang #37、Ling Zhang #39）夹着 Wenbo Xiao #38。

正确的尾部位次：

```
36  Shenghong Ju     东南大学中大医院放射科
37  Jianfeng Zhang   达摩院 · 湖畔实验室
38  Wenbo Xiao       浙大一院放射科
39  Ling Zhang       达摩院 · Washington DC      ← AI 侧资深作者
40  Tingbo Liang     浙大一院肝胆胰外科            ← 末位通讯
```

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

## 骨架表

> 中文名一栏由 [../README.md](../README.md) 的调查填充。**把握**列：`确认` = 中文来源直接看到英↔中对应；`可能` = 间接证据；`未知` = 没查到，**不允许按拼音猜**。

| # | 英文名 | 中文名 | 把握 | 单位（论文原文压缩） | 也在 PANDA |
|---:|---|---|:---:|---|:---:|
| 1 | **Qi Zhang** | *待填* | — | 浙大一院肝胆胰外科 · 浙江省胰腺疾病重点实验室 · 教育部胰腺疾病国际合作联合实验室 | ✅ |
| 2 | **Jianpeng Zhang** | *待填* | — | 达摩院 · 湖畔实验室 · 浙大计算机学院 | |
| 3 | **Weiwei Cao** | *待填* | — | 达摩院 · 湖畔实验室 · 浙大计算机学院 | |
| 4 | **Zilin Lu** | *待填* | — | 达摩院 · **宁波市第二医院放射科** | |
| 5 | **Wanxing Chang** | *待填* | — | 达摩院 · 湖畔实验室 | |
| 6 | **Haonan Ding** | *待填* | — | 浙大一院肝胆胰外科 | |
| 7 | **Cao Chen** | *待填* | — | 浙大一院肝胆胰外科 | |
| 8 | **Zhi Li** | *待填* | — | 浙大一院放射科 | |
| 9 | **Xing Xue** | *待填* | — | 浙大一院放射科 | |
| 10 | **Sinuo Wang** | *待填* | — | Adelaide AIML | |
| 11 | **Shaoteng Zhang** | *待填* | — | 达摩院 · **宁波市第二医院放射科** | |
| 12 | **Yutong Xie** | *待填* | — | MBZUAI 计算机视觉系（阿布扎比）| |
| 13 | **Yong Xia** | *待填* | — | **宁波市第二医院放射科（唯一单位）** ⚠️ | |
| 14 | **Qi Wu** | *待填* | — | Adelaide AIML | |
| 15 | **Zhongyi Shui** | *待填* | — | 浙大计算机学院 | |
| 16 | **Xi Li** | *待填* | — | 浙大计算机学院 | |
| 17 | **Zhilin Zheng** | *待填* | — | 达摩院 · 湖畔实验室 | |
| 18 | **Yanjie Zhou** | *待填* | — | 达摩院 · 湖畔实验室 · 浙大计算机学院 | |
| 19 | **Tony C W Mok** | *待填* | — | 达摩院 · 湖畔实验室 | |
| 20 | **Yingda Xia** | *待填* | — | 达摩院 · **Washington DC** | ✅ |
| 21 | **Hongkan Wang** | *待填* | — | 浙大一院肝胆胰外科 | |
| 22 | **Xianghua Ye** | *待填* | — | 浙大一院放疗科 | |
| 23 | **Tao Ma** | *待填* | — | 浙大一院肝胆胰外科 · 兵团第一师医院普外科（阿克苏）| |
| 24 | **Jie Peng** | *待填* | — | 兵团第一师医院放射科（阿克苏）| |
| 25 | **Xiaoguang Wang** | *待填* | — | 嘉兴学院附属医院外科 | |
| 26 | **Jian Ding** | *待填* | — | 嘉兴学院附属医院放射科 | |
| 27 | **Yuming Gao** | *待填* | — | 安徽绩溪县人民医院普外科 | |
| 28 | **Huazhen Ye** | *待填* | — | 景宁畲族自治县人民医院放射科 | |
| 29 | **Yiping Liu** | *待填* | — | 嵊州市人民医院放射科 | |
| 30 | **Dongjie Chen** | *待填* | — | 海宁市人民医院普外科 | |
| 31 | **Zhaomin Ni** | *待填* | — | 安吉县人民医院放射科 | |
| 32 | **Jianwen Ning** | *待填* | — | 浙大一院急诊科 | |
| 33 | **Wei Zhang** | *待填* | — | 浙大一院肝胆胰外科 · 杭州余杭区第一人民医院普外科 | |
| 34 | **Jian Liu** | *待填* | — | 宁波北仑区人民医院外科肿瘤 | |
| 35 | **Chaohui Yu** | *待填* | — | 浙大一院消化内科 | |
| 36 | **Shenghong Ju** | *待填* | — | 东南大学中大医院放射科 + 江苏省分子影像与功能影像重点实验室 | |
| 37 | **Jianfeng Zhang** | *待填* | — | 达摩院 · 湖畔实验室 | |
| 38 | **Wenbo Xiao** | *待填* | — | 浙大一院放射科 | |
| 39 | **Ling Zhang** | *待填* | — | 达摩院 · **Washington DC** | ✅ |
| 40 | **Tingbo Liang** | *待填* | — | 浙大一院肝胆胰外科 · 浙江省胰腺疾病重点实验室 · 教育部胰腺疾病国际合作联合实验室 | ✅ |

---

## 光看单位就能读出来的三件事

### ① 第一作者是外科医生，末位通讯是医院院长

- **#1 Qi Zhang** 挂的是浙大一院**肝胆胰外科**，不是任何计算机单位。
- **#40 Tingbo Liang** 同科室，是该院院长兼党委书记、全国人大代表（待核实全部头衔 → [zju-hospital.md](zju-hospital.md)）。

==AI 侧的资深作者 Ling Zhang 排在 #39，是倒数第二位。== 这个排法在中文医学期刊语境里读法很清楚：临床方拥有这项工作。

### ② PANDA → RADAR 的连续性，用精确名字匹配验证过

两篇论文的作者名做交集，**只有四个人重合**，而且单位在两篇里一致：

| 姓名 | PANDA (Nat Med 2023) 单位 | RADAR (Science 2026) 单位 |
|---|---|---|
| **Qi Zhang** | 浙大一院肝胆胰外科 | 同 |
| **Tingbo Liang** | 浙大一院肝胆胰外科 | 同 |
| **Ling Zhang** | DAMO Academy, **New York** | DAMO Academy, **Washington DC** |
| **Yingda Xia** | DAMO Academy, **New York** | DAMO Academy, **Washington DC** |

✓ 同一个外科科室 + 同一个达摩院美国团队，隔三年。
💡 顺带抓到一个细节：**达摩院的美国办公室从 New York 搬到了 Washington DC**（或者至少论文署名的写法变了）。

> [!insight] 424,911 例的数据访问不是第一次取款
> 是 PANDA（2023-11, Nature Medicine, PMID 37985692）打开的那个账户的第二次。
> 这条直接回答"是不是国家支持就能拿到好数据"——顺序是**先交付，再拿数据**。

### ③ ⚠️ 宁波市第二医院放射科：一个需要解释的结构

三个人挂这家医院，但方式不一样：

```
#4  Zilin Lu        达摩院 + 宁波二院放射科     ← 双聘
#11 Shaoteng Zhang  达摩院 + 宁波二院放射科     ← 双聘
#13 Yong Xia        宁波二院放射科（唯一单位）   ← 纯临床
```

==两个达摩院研究员同时挂一家地级市医院的放射科，这不是普通的合作署名。== 可能的解释（**均为推断，待核实**）：
- 宁波二院是达摩院的嵌入式合作点，研究员常驻；
- 或这两人本身是放射科医生被达摩院聘用；
- 或这是为了满足数据使用/伦理审批的署名安排。

⚠️ **#13 Yong Xia 是本次调查的头号消歧风险。** 学界另有一位著名的**西北工业大学 夏勇 (Yong Xia)** 教授做医学影像 AI，且与 Jianpeng Zhang、Yutong Xie 长期合著（DoDNet、UniMiSS 等）。但本文给他标的**唯一**单位是宁波二院放射科，一个字的西工大都没有。
→ 判定见 [academic-pipeline.md](academic-pipeline.md)。**在那份判定出来之前，不要假设这两个是同一个人。**

---

## 跨机构桥梁（挂 2 个以上单位的 13 人）

这些人是结构上的连接点：

| 人 | 连接的是 |
|---|---|
| #1 Qi Zhang · #40 Tingbo Liang | 临床科室 ↔ 两个重点实验室 |
| #2 Jianpeng Zhang · #3 Weiwei Cao · #18 Yanjie Zhou | 达摩院 ↔ 湖畔实验室 ↔ 浙大计算机学院（三重）|
| #4 Zilin Lu · #11 Shaoteng Zhang | 达摩院 ↔ 宁波二院放射科 |
| #23 Tao Ma | 浙大一院 ↔ 新疆兵团第一师医院（疑似援疆医疗队，待核实）|
| #33 Wei Zhang | 浙大一院 ↔ 杭州余杭区第一人民医院 |
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
