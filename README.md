# DAMO RADAR（*Science* 2026）—— 40 位作者关系图谱

> 调研日期：**2026-09-20**。方法：**59 个并行 AI research agent**（21 个人物调查 + 21 个对抗式交叉核查 + 9 个机构/血统专题 + 7 个 MedSAM 关系取证 + 2 个正反立场对抗），交叉核对 PubMed E-utilities、Crossref、OpenAlex、ORCID、Europe PMC、GitHub/HuggingFace API、浙大与浙大一院官网、各县市医院官网、国家卫健委与浙江省卫健委政策原文、中新网/浙报集团、Wayback、CNIPA 专利著录。
> **所有结论附证据；不确定处在各档案的"可信度注意"里明确标出。中文名查不到的一律留空 —— 不按拼音猜。**
> 论文：*An expert-level generalist AI for abdominal CT diagnosis*, **Science 393(6817):eaec6129**, 2026. DOI [10.1126/science.aec6129](https://doi.org/10.1126/science.aec6129) · PMID 42752131 · 代码 [alibaba-damo-academy/damo-radar](https://github.com/alibaba-damo-academy/damo-radar)

## 目录

- [一页概览](#一页概览)
- [40 位作者中文名总表](#40-位作者中文名总表)
- [结构：四条腿](#结构四条腿)
- [三条血统线](#三条血统线)
- [为什么是这八家县医院](#为什么是这八家县医院)
- [与 MedSAM 的关系](#与-medsam-的关系)
- [技术底细](#技术底细)
- [对抗核查推翻了什么](#对抗核查推翻了什么)
- [与你研究的交集](#与你研究的交集)
- [求职通道](#求职通道)
- [数据缺口](#数据缺口)
- [文件说明](#文件说明)

---

## 一页概览

| | |
|---|---|
| **是什么** | 腹部增强 CT 的全自动诊断视觉-语言模型。输入整卷，输出 **18 个器官 / 146 个征象**的概率。无提示。 |
| **末位通讯** | **梁廷波**（Tingbo Liang）—— 浙大一院**院长、党委副书记**，第十四届全国人大代表，长江学者，杰青 |
| **第一作者** | **章琦**（Qi Zhang）—— 浙大一院肝胆胰外科，**外科医生，不是做 AI 的**；同时是浙大一院党委副书记 |
| **AI 侧资深作者** | **张灵**（Ling Zhang）—— 达摩院 Washington DC，第 39 位（倒数第二） |
| **共同第一作者** | **6 位**（PubMed XML 的 `EqualContrib="Y"` 标在前六位）：章琦、张建鹏、曹维维、Zilin Lu、常琬星、Haonan Ding |
| **作者构成** | 浙大一院 13 · 达摩院+湖畔 11 · 基层医院 9 · 海外学术 3 · 浙大计算机 2 · 宁波二院 1 · 东南大学 1 = **40** |
| **规模** | 训练 424,911 次检查 / 1500 万 anatomy-wise 图文对，**零人工标注**（报告经 Qwen 解析）|
| **核心数字** | 146 征象平均 AUC 0.913（对照 VLM 0.776）· 8 外部中心 0.895 · 病理确诊四种癌 0.891–0.984 · 急腹症（训练时排除）0.904 · 26 位医生 reader study 敏感度 +约 10% |
| **许可** | 代码 Apache-2.0；**权重 CC BY-NC-SA 4.0（禁商用）** |
| **前序** | **PANDA**（*Nature Medicine* 2023, PMID 37985692）—— 两篇共享 4 人，单位一致 |
| **中文名结果** | **28 确认 · 1 可能 · 11 未查到**（未查到的以达摩院初级研究员和在读博士生为主）|

> [!insight] 一句话读懂作者排序
> ==第一作者是外科医生，末位通讯是医院院长，AI 侧资深作者排在倒数第二。==
> 这个排法在中文医学期刊语境里读法很清楚：**临床方拥有这项工作**。

---

## 40 位作者中文名总表

把握分三档：**✅ 确认** = 中文权威来源直接看到英↔中对应，或单位+职务+方向三重锁定；**🟡 可能** = 间接证据；**❓ 未知** = 没查到，**留空不猜**。

<!-- NAME-TABLE:START -->
| # | 英文 | 中文 | 把握 | 单位 · 身份 | PANDA |
|---:|---|---|:---:|---|:---:|
| 1 | Qi Zhang | **章琦** | ✅ | 浙大一院肝胆胰外科 教授/主任医师/博导；**院党委副书记**。共一 | ✅ |
| 2 | Jianpeng Zhang | **张建鹏** | ✅ | 达摩院 Staff Algorithm Engineer；**西工大夏勇门下**。共一，技术侧主力 |  |
| 3 | Weiwei Cao | **曹维维** | ✅ | 达摩院医疗 AI（湖畔）。共一。⚠️ 名字由核查经 CNIPA 专利著录追回 |  |
| 4 | Zilin Lu | **—** | ❓ | **西工大计算机学院在读博士**，达摩院实习。共一。ORCID 教育栏写 NWPU |  |
| 5 | Wanxing Chang | **常琬星** | ✅ | 达摩院算法工程师。共一 |  |
| 6 | Haonan Ding | **—** | ❓ | 浙大一院肝胆胰外科**硕士生**（ORCID employments）。共一 |  |
| 7 | Cao Chen | **—** | ❓ | 浙大一院肝胆胰外科，推断为章琦组研究生/在培医师 |  |
| 8 | Zhi Li | **李志** | ✅ | 浙大一院放射科 主治医师 |  |
| 9 | Xing Xue | **薛星** | ✅ | 浙大一院放射科（ORCID 自述 2018-08 起受雇） |  |
| 10 | Sinuo Wang | **—** | ❓ | Adelaide AIML 博士生 + 达摩院实习（推断） |  |
| 11 | Shaoteng Zhang | **—** | ❓ | **西工大计算机学院在读博士**，达摩院实习 |  |
| 12 | Yutong Xie | **谢雨彤** | ✅ | MBZUAI 计算机视觉系 **助理教授**；西工大 2016 级直博，**导师夏勇** |  |
| 13 | Yong Xia | **夏勇** | ✅ | ⚠️ **西北工业大学计算机学院长聘教授、博导、副院长** —— 论文只标了「宁波市第二医院放射科」 |  |
| 14 | Qi Wu | **吴琦** | ✅ | Adelaide AIML 副教授，V3A Lab 主任 |  |
| 15 | Zhongyi Shui | **—** | ❓ | 浙大-西湖大学联合培养博士生（推断） |  |
| 16 | Xi Li | **李玺** | ✅ | 浙大计算机学院 教授、**求是特聘教授** |  |
| 17 | Zhilin Zheng | **—** | ❓ | 达摩院算法研究员（2022 起持续正式署名，非实习） |  |
| 18 | Yanjie Zhou | **—** | ❓ | 达摩院算法研究员；论文另写作 Yan-Jie Zhou |  |
| 19 | Tony C W Mok | **—** | ❓ | 香港人，署名 **Tony Chi Wing MOK**；达摩院算法工程师；HKUST 博士（导师 **Pedro Sander + Albert C.S. Chung** 两人） |  |
| 20 | Yingda Xia | **夏英达** | ✅ | 达摩院 **Washington DC**；JHU Alan Yuille 门下 | ✅ |
| 21 | Hongkan Wang | **—** | ❓ | 浙大一院肝胆胰外科，深度参与早期临床试验（GCP） |  |
| 22 | Xianghua Ye | **叶香华** | ✅ | 浙大一院放疗科 **副主任**、主任医师 |  |
| 23 | Tao Ma | **马涛** | ✅ | 浙大一院肝胆胰外科主任医师；**兵团第一师医院党委副书记兼院长**、中组部第十一批援疆领队 |  |
| 24 | Jie Peng | **彭杰** | ✅ | 兵团第一师医院 医学影像中心主任、副主任医师 |  |
| 25 | Xiaoguang Wang | **王晓光** | ✅ | 嘉兴一院 **党委委员、副院长**、主任医师 |  |
| 26 | Jian Ding | **丁健** | ✅ | 嘉兴一院放射科 **副主任**、副主任医师 |  |
| 27 | Yuming Gao | **高玉明** | ✅ | 绩溪县人民医院 **院长**、主任医师 |  |
| 28 | Huazhen Ye | **叶华震** | ✅ | 景宁县人民医院放射科 **副主任（主持工作）** |  |
| 29 | Yiping Liu | **刘义平** | ✅ | 嵊州市人民医院放射科 **主任**、主任医师 |  |
| 30 | Dongjie Chen | **陈东杰** | 🟡 | 海宁市人民医院普外科三（肝胆胰脾疝）。职称未查到 |  |
| 31 | Zhaomin Ni | **倪兆敏** | ✅ | 安吉县人民医院放射科 主任医师 |  |
| 32 | Jianwen Ning | **宁建文** | ✅ | 浙大一院急诊科；**浙大一院安吉分院党委副书记、院长** |  |
| 33 | Wei Zhang | **张微** | ✅ | 浙大一院肝胆胰外科主任医师、肝移植中心副主任；兼良渚分院 |  |
| 34 | Jian Liu | **刘剑** | ✅ | 北仑区人民医院（浙大一院北仑分院）**院长**、主任医师 |  |
| 35 | Chaohui Yu | **虞朝辉** | ✅ | 浙大一院 **副院长**、消化内科主任 |  |
| 36 | Shenghong Ju | **居胜红** | ✅ | 东南大学中大医院 **副院长**、医学影像部主任、东南大学首席教授 |  |
| 37 | Jianfeng Zhang | **—** | ❓ | 达摩院医学影像研究员（CT-SAM3D 作者）。⚠️ **不是达摩院院长张建锋** |  |
| 38 | Wenbo Xiao | **肖文波** | ✅ | 浙大一院放射科 **副主任（主持工作）**、主任医师 |  |
| 39 | Ling Zhang | **张灵** | ✅ | 达摩院 Washington DC 资深算法专家。AI 侧通讯 | ✅ |
| 40 | Tingbo Liang | **梁廷波** | ✅ | 浙大一院 **院长、党委副书记**；全国人大代表。末位通讯 | ✅ |
<!-- NAME-TABLE:END -->

> [!strategy] 读这张表的正确方式：看职务，不看职称
> ==基层医院那 9 位里，有 4 位是院长或副院长（马涛、王晓光、高玉明、刘剑、宁建文），其余是科室主任或主持工作的副主任。==
> 这不是"找了几个基层医生帮忙标数据"，这是**院级签署的机构合作**。

---

## 结构：四条腿

> 🖼 **交互图（archify，含三个导览视图 + 明暗主题 + 导出）→ [figures/radar-structure.html](figures/radar-structure.html)**
> 图源 [figures/radar-structure.architecture.json](figures/radar-structure.architecture.json)，改图改 JSON 后重跑 `archify deliver`。

一句话读法：==数据从浙大一院 PACS 出发，经 Qwen 把 42 万份报告解析成器官级标签，在达摩院训练出 RADAR，最后回到浙大一院自己的分院体系做"外部"验证。==

| 腿 | 人数 | 谁 |
|---|---:|---|
| 临床 / 数据 | 13 | 浙大一院：肝胆胰外科（章琦·共一 / 梁廷波·末位通讯）、放射科（肖文波）、消化内科（虞朝辉·副院长）、急诊科、放疗科 |
| AI | 11 | 达摩院杭州 + **湖畔实验室** + 浙大计算机学院（三重挂靠）；张灵、夏英达在 Washington DC |
| 外部验证 | 9 | 10 家医院，**其中 8 家在浙大一院的托管 / 分院 / 对口支援体系内** |
| 学术方法供给 | 5 | 西工大夏勇 → Adelaide 吴琦 → MBZUAI 谢雨彤；浙大计算机李玺 |

---

## 三条血统线

### ① 西北工业大学 · 夏勇门下 —— 这篇论文的技术班底

⚠️ **本次调查最大的一处消歧**：论文给 **Yong Xia** 标的**唯一**单位是"Department of Radiology, Ningbo No. 2 Hospital"，一个字的西工大都没有。

**判定：就是西北工业大学计算机学院的夏勇教授**，长聘教授、博导、计算机学院副院长。证据链：

| 证据 | 内容 |
|---|---|
| 合著网络 | OpenAlex 查 Jianpeng Zhang 的合著，**头号合著者就是 Yong Xia，22 篇共著，机构标 NWPU ×21**；Yutong Xie 第 3 位，NWPU ×18 |
| 师承 | **谢雨彤是西工大 2016 级直博，导师夏勇**，博士论文《有限标注的医学影像分割及分类》 |
| 同单位号的旁证 | **Zilin Lu 的 ORCID（0000-0003-2437-283X）educations 明写 Northwestern Polytechnical University** —— 他和夏勇共享同一个单位编号 #7 |
| 宁波通道已证实 | 夏勇论文里出现过 `Ningbo Institute of Northwestern Polytechnical University`（西北工业大学宁波研究院），见其 2023 DoDNet 期刊版与 2025 PICK |

==所以 #4 Zilin Lu、#11 Shaoteng Zhang、#13 夏勇 三个挂"宁波二院放射科"的人，其实是一条西工大线。== 这个单位号是这条线的落点，不是一群放射科医生。

⚠️ 正方对抗 agent 另外指出：**RADAR 在 OpenAlex 与 PubMed 两处的 author-affiliation 映射本身就存在错位**（夏勇被记成宁波二院放射科、谢雨彤在两处分别被记成 MBZUAI 与 Adelaide）。引用本文 affiliation 字段做任何推断都要带这个保留。

### ② NIH → 平安 PAII → 达摩院 —— AI 侧的整建制迁徙

```
NIH Clinical Center 放射与影像科学系（Ronald M. Summers 实验室）
  吕乐(Le Lu) · Ke Yan · Xiaosong Wang · Holger Roth · 唐有宝(Youbao Tang) · 张灵
  产出：ChestX-ray8/14 (2017, 112,120 张) · DeepLesion (2018, 32k CT)
        ↓  2018–2019
PAII Inc. = 平安科技美国研究院（2016 创立，Palo Alto + Bethesda 双点）
  ★ Bethesda 点距 NIH 临床中心 3.5 公里 —— 公司有硅谷点却专为这支队伍在马里兰单开一个
  吕乐任 Executive Director (2018-06 → 2021-07)
        ↓  2021，整队迁移（已补全到 12 人）
阿里巴巴达摩院
  吕乐 → 领全球医疗 AI (2021-08 → 2025-06) → 蚂蚁 Ant Group Sunnyvale
  张灵 → 达摩院 Washington DC，PANDA 与 RADAR 的 AI 侧通讯
  Ke Yan → 达摩院（DeepLesion 一作）
  Jiawen Yao → 达摩院
```

**几条被推翻或新补的：**

- ✗ **吕乐的"NVIDIA 一段"很可能不存在。** 主页原文只有无日期残句 "...and from NVIDIA AI-Infra division"。三条反证：Siemens(→2013-01)→NIH(五年多)→PAII(2018-06)→达摩院(2021-07) 时间线**没有空隙**；PubMed 查不到任何他署 NVIDIA 的论文；这句话 2022 年写下至今一字未改（Wayback 比对）。判断是"我的团队来自 NIH 和 NVIDIA"的压缩表述。
- ✗ **达摩院医疗 AI 不是 2021 年才有的。** 2020 年就有 "HealthTech Division, DAMO Academy"，方向是生信/基因组。==2021 是**嫁接**，不是建院。==
- 💡 **Bethesda 三角**：NIH 临床中心、平安 PAII、NVIDIA 医学影像组三家都在 Bethesda，2015–2021 从同一人才池抓人。**这不是三次孤立跳槽，是几平方公里内的一个人才市场。**
- 💡 **吕乐是一个人走的。** 扫了蚂蚁 2025–26 全部 1221 篇论文的署名查 15 位旧部，**零命中**。核心班底留在达摩院，三篇 2026 旗舰的通讯作者都是张灵。
- 💡 **达摩院美国现在是两个点并存**：**DC** = 张灵 + 夏英达的平扫 CT 早筛线（*Nature Medicine* / *Science*）；**NY** = Dakai Jin 等 8 人的头颈放疗线（*Radiology*）。
- 💡 中文名确证：**Le Lu = 吕乐**、**Youbao Tang = 唐有宝**（现 Google 高级软件工程师）。

→ 详见 [sources/damo-lineage.md](sources/damo-lineage.md)

### ③ PANDA → RADAR —— 同一个账户的第二次取款

两篇论文的作者名做精确交集，**只有四人重合，且单位在两篇里一致**：

| | PANDA (*Nat Med* 2023) | RADAR (*Science* 2026) |
|---|---|---|
| **章琦** Qi Zhang | 浙大一院肝胆胰外科（33/36）| 同（1/40，共一）|
| **梁廷波** Tingbo Liang | 浙大一院肝胆胰外科 | 同（40/40，末位通讯）|
| **张灵** Ling Zhang | DAMO Academy, **New York** | DAMO Academy, **Washington DC** |
| **夏英达** Yingda Xia | DAMO Academy, **New York** | DAMO Academy, **Washington DC** |

> [!insight] 这条直接回答"是不是国家支持就能拿到好数据"
> ==424,911 例的数据访问不是第一次取款，是 PANDA 在 2023 年打开的那个账户的第二次。==
> 顺序是**先交付，再拿数据** —— 不是反过来。

---

## 为什么是这八家县医院

外部验证中心全是县级/区级/兵团医院，没有一家协和/华西/中山这一层。**这不是凑数，是沿着一条已经存在的管道取样。**

| 论文单位号 | 医院 | 层级 | 与浙大一院的正式关系 | 起始 |
|---|---|---|---|---|
| 13/14 | 兵团第一师医院（阿克苏）| 兵团师级·三甲 | **对口支援 + 跨省医联体**（浙大 6 家附属医院）| 2016-08 |
| 17 | 安徽绩溪县人民医院 | 县级·二甲 | **浙大一院绩溪分院**，紧密型重点托管，**省外唯一分院** | 2021-09 |
| 18 | 景宁畲族自治县人民医院 | 县级·二级 | **浙大一院民族分院** | 2013 |
| 19 | 嵊州市人民医院 | 县级市·三乙 | **浙大一院嵊州分院**（全面托管）| — |
| 20 | 海宁市人民医院 | 县级市·三乙 | **浙大一院海宁院区**（全面托管）| 2019 |
| 21 | 安吉县人民医院 | 县级·二甲 | **浙大一院安吉分院**（第九家分院）| 2019-01 |
| 23 | 余杭区第一人民医院 | 区级·三级 | **浙大一院良渚分院**（全面运营管理）| 2022-10 |
| 24 | 北仑区人民医院 | 区级·三乙 | **浙大一院首家托管合作医院** | 2008 |
| 15/16 | 嘉兴一院 | 市级·三甲 | ✗ 无托管关系 | — |
| 7 | 宁波二院 | 市级·三甲 | ✗ 无托管关系（是西工大那条线的落点）| — |

**8/10 在体系内。** 这个网络是三层政策叠出来的：

1. **"双下沉、两提升"**（浙江省，2010s 中期起）→ 北仑 2008、景宁 2013、安吉 2019、海宁 2019
2. **医疗卫生"山海"提升工程**（浙江省卫健委，2021-08-30）→ 13 家省市三甲帮扶山区 26 县
3. **长三角一体化跨省帮扶** → 绩溪（安徽），浙大一院省外唯一分院

> [!insight] 被低估的一条线索
> "山海"工程的官方文件把 **"县域影像共享中心"** 和 **"基层检查、上级诊断、区域互认"** 写成了省级硬任务。
> ==也就是说，在 RADAR 做外部验证之前，这些县医院的 CT 数据在**制度上已经是"要往上送给三甲读"的数据流**。==
> 论文的外部验证，某种意义上是沿着这条**已经存在的影像上行管道**取样。

**兵团第一师医院那家不是"外部中心"，是浙大一院的援疆任职点。** #23 **马涛**同挂浙大一院肝胆胰外科 + 兵团第一师医院普外科，不是学术挂名 —— 他是**中组部第十一批援疆领队、一师医院党委副书记兼院长**（2024-11 赴疆）。#32 **宁建文**同理：浙大一院急诊科 + **浙大一院安吉分院院长**。#34 **刘剑**是北仑分院院长。

**产业侧的时间线很说明问题：**

```
2024-01-23  张建锋（达摩院院长、湖畔实验室主任）建议浙江统筹建设高质量医学影像数据集
2024-02-22  阿里"医疗 AI 多癌早筛公益项目"在丽水启动
            首批部署：丽水市中心医院 + 【景宁县人民医院】 ← RADAR 外部中心 #18
2024-11-06  国家卫健委《卫生健康行业人工智能应用场景参考指引》
            4 大领域 84 个场景，【第一条就是"医学影像智能辅助诊断"】
2026-09     RADAR 发表
```

→ 详见 [sources/grassroots-network.md](sources/grassroots-network.md)（原始材料在 [data/raw/ctx-grassroots.md](data/raw/ctx-grassroots.md)）

---

## 与 MedSAM 的关系

**一句话：两个模型之间没有关系；两个团队之间有关系，而且比第一轮调查说的紧得多。**

最活的一条 —— ==**Jun Ma 在 RADAR 发布第二天给它做了 demo**==：

```
2026-09-18            jizhang02 在 damo-radar 开 issue #1 "Online tool?"
2026-09-19 03:17:41Z  JunMa11 创建 HF Space  junma/RADAR-demo
2026-09-19 03:49:16Z  JunMa11 回帖贴出链接   ← 建完 32 分钟
```

人事链（首跳是真实共同署名）：

```
Bo Wang / Jun Ma ─[FLARE22 报告, Lancet Digital Health 2024, Crossref 37 人表：
                    #1 Jun Ma · #33 Heng Guo · #37 Bo Wang]─
Heng Guo（达摩院）─[Med-Query, IEEE JBHI 2024, 五位作者全挂 DAMO Academy Hangzhou]─
Jianfeng Zhang = RADAR 第 37 位作者 ─ RADAR
```

→ 完整内容（含两种路线的结构对比、能不能合流的技术判断、Bo Wang 2025 去 Xaira 的重大人事变动）见 **[sources/radar-vs-medsam.md](sources/radar-vs-medsam.md)**

---

## 技术底细

全部物理是三行代码 —— `[-300, 400]` HU 窗 + **逐体数据** min-max 归一化。后果：**10 个肺征象被 −300 地板钳平，钙化/骨在 400 天花板饱和**。

数学层面没有新东西：ALBEF/BLIP 式图文对比（`alpha: 0.4` 是 momentum distillation 权重，`queue_size: 0`），24 张 GPU × 30 epoch。
**真正的创新在监督信号怎么造出来**，不在模型。

→ 完整拆解（含我修正自己的三处错误：视觉编码器不是 3D ResNet、文本编码器有两个、TotalSegmentator 是离线教师不是运行时组件）见 **[sources/radar-technical-teardown.md](sources/radar-technical-teardown.md)** 与 **[sources/dependency-stack.md](sources/dependency-stack.md)**

💡 **MERLIN 不是外部测试集，是 RADAR 全部公开可复现性的载体。** `docs/TRAINING.md` 明写 RADAR+ 是 "trained from scratch on Merlin-CT-Train set"。MERLIN = *Nature* 652:1318–1328(2026)，斯坦福，通讯 **Akshay S. Chaudhari**。==RAD-CT 那 42 万例永远放不出来，所以他们用一个公开的同任务美国数据集把整条流水线演示了一遍。==

---

## 对抗核查推翻了什么

**每一份人物档案都被第二个 agent 以"证伪"为目标重查过。** 这一节记录纠错，因为纠错本身就是结论的一部分。

| 被推翻的说法 | 判决 |
|---|---|
| **Jianfeng Zhang = 张建锋（达摩院院长、湖畔实验室主任）** | 🔴 **严重误判，已推翻。** 证据指向他是达摩院医学影像研究员（CT-SAM3D 作者，arXiv 2403.15063）。原推理"PubMed 单位串恰为 DAMO + Hupan 两条，与院长+主任两个职务一一对应"无效 —— 本文另有 4 人也是同样的两条单位串 |
| 梁廷波是"院长兼党委书记" | ✗ 已过时。**2025-07-28 领导班子调整：顾国煜任党委书记，梁廷波转任院长、党委副书记**。他任党委书记的时段是 2018-12 至 2025-07 |
| 曹维维"中文名完全查不到" | ✗ 可查实，核查经 CNIPA 公开专利著录追回。原调查检索的是错误写法"曹伟伟" |
| 居胜红"与浙大/达摩院无先前合作，是被外部请来的独立方" | ✗ 推翻。*Radiology* 2023 微血管侵犯那篇两边已有合作 |
| RADAR 是 39 位作者 | ✗ **40 位。** PubMed efetch 与 Crossref 都返回 40 |
| 共同一作是前 5 位 | ✗ **前 6 位。** PubMed XML 的 `EqualContrib="Y"` 标到第 6 位 Haonan Ding |
| 章琦在 PANDA 是 34/36 | ✗ **33/36** |
| 视觉编码器是 3D ResNet | ✗ 是 `PlainConvUNetLightD`。`resnet` 在推理链 grep 零命中，`resnet_vl.py` 是**死代码** |
| 文本编码器是 bert-base-uncased | ✗ **有两个**：旗舰 RAD-CT 档用 `bert-base-chinese`，MERLIN 档才是 uncased |
| Tony Mok 的博导是 Albert Chung 一人 | ✗ HKUST 学位记录 Supervisor 字段是**两人，Pedro Sander 列在第一位** |
| "RADAR 基层站点普遍是普外科1人+放射科1人成对" | ✗ 9 个站点里只有 2 个成对 |
| 吕乐有 NVIDIA 任职经历 | ⚠️ 很可能不存在，见[血统②](#-nih--平安-paii--达摩院--ai-侧的整建制迁徙) |
| Wang Lab 与达摩院"零篇共同署名" | ✗ 推翻，见 [radar-vs-medsam.md](sources/radar-vs-medsam.md) |

> [!strategy] 这张表本身就是这份报告最该信的部分
> ==如果没有第二轮对抗核查，"Jianfeng Zhang = 达摩院院长张建锋"会被写进正文。==
> 一次成的调查不可信；被证伪过一轮还站着的才可信。

---

## 与你研究的交集

**① 可以偷的：anatomy-token 技巧，零成本。**
RADAR 最值钱的工程 trick 不是 VLM，是"用现成的自动分割器把整卷 CT 切成解剖单元，所有下游量都在解剖单元上算"。这个 trick 不含任何学习参数。你几百例的材料分解数据可以照做，把 water/lipid/protein 分数、噪声、误差预算按解剖结构汇总而非按手画 ROI。==统计功效从"几百个 ROI"放大到"几百 × N 个解剖单元"，同时消除读者间变异。==

**② 绝不能偷的：它对分割质量的态度。**
RADAR 把 mask 池化到 40×32×32 mm 还照样工作，因为它只要"这堆 token 属于肝"。你做材料分解，==**边界就是 partial volume effect，边界就是信号本身**==。

**③ 你处在 RADAR 的反面，而这是优势。**
RADAR 全部设计在回答"我有海量数据但没有标签"；你的处境是"我有少量数据但**有真值**"（phantom 已知浓度、已知材料、已知 keV）。==已知真值在小数据上的信息密度，远高于 42 万份报告里的弱标签。==
✗ 任何让你放弃 phantom 真值去追"大数据自监督"的建议都是在往下走。

**④ 真正该抄的是验证形式，不是模型。**
独立金标准子集（病理／体模真值）+ 多读者 reader study + 外部中心 —— 这三件事在几百例规模上照样立得住。
和 Slomka EAT pipeline 上得出的是同一条：**copy the evaluation form, not the model.**

**⑤ 一条顺带的人脉信息。** MERLIN 的通讯作者是 **Akshay S. Chaudhari**（斯坦福）—— 就是你之前 PI scouting 里评过的那位。RADAR 能有公开可复现路径，靠的是他那个组的开放数据。

---

---

## 求职通道

达摩院美国那条**不用考虑**：`Alibaba Group (US) Inc` 的 `RESEARCH SCIENTIST` 头衔在 **2022 年之后彻底消失**（2019:5 → 2020:7 → 2021:2 → 2022:1 → 0），Washington DC 在 2026 年的研究岗 LCA 申报**只有一条**。它是几个资深研究员的据点，不是能投简历的机构。

真正对口且在办身份的是**设备厂**：

```
🟢 United Imaging（Houston）  2026 年 5–6 月五周内连办 7 个 research scientist，三个岗名带 "CT"
🟢 Canon（Vernon Hills IL）   Reconstruction Scientist，2026-05-08
🟢 GE HealthCare（Waukesha）  Lead Scientist - Clinical Physics，2026-04
🟡 Elucid / HeartFlow / Cleerly   冠脉 CT 定量三家，和 PCAT/FAI 同构，但岗位名是 engineer
⛔ Philips（Orange OH）       技术上最贴合，JD 白纸黑字拒绝任何"now or in the future"需要 sponsorship 的人
```

→ 完整分级、薪资申报数据、逐条复核状态见 **[sources/damo-hiring.md](sources/damo-hiring.md)**

## 数据缺口

不要当成已知：

- **11 位作者的中文名查不到**（Zilin Lu、Haonan Ding、Cao Chen、Sinuo Wang、Shaoteng Zhang、Zhongyi Shui、Zhilin Zheng、Yanjie Zhou、Tony C W Mok、Hongkan Wang、Jianfeng Zhang）。以达摩院初级研究员和在读博士生为主，中文互联网没有公开痕迹。**按规则留空，没有按拼音猜。**
- **Science 正文与补充材料在付费墙后**（403）。技术细节全部来自代码与仓库文档；数字来自 PubMed 摘要 + EurekAlert 新闻稿 + Zenodo 存档的交叉印证。
- **RADAR 的 PubMed 记录没有 GrantList** —— 基金号要读 Science 正文 Funding 段才有。
- **湖畔实验室的省财政拨款比例**、是否有独立法人登记 —— 无公开资料。
- **夏勇与宁波二院放射科的具体关系**未找到直接记载（西工大主页被拦，412/空白）。判定依据是合著网络 + 同单位号旁证 + 已证实的宁波通道。
- 除病理确诊子集外，**测试标签是否也由 LLM 从报告解析** —— 推断，未获一手确认。
- 多位基层医院医生的**职称**只见于媒体报道，未见官方人事文件。

---

## 文件说明

```
README.md                          本文件 —— 总图
sources/                           【裁决后的结论页，正文以此为准】
  authors-affiliations.md          40 位作者单位骨架表（PubMed 原始抽取）
  radar-technical-teardown.md      源码级技术拆解（含我自己的三处更正）
  dependency-stack.md              技术栈依赖图 × 人事血统交叉
  damo-lineage.md                  NIH → 平安 PAII → 达摩院 的整建制迁徙
  academic-pipeline.md             西工大 → Adelaide → MBZUAI 学术供给线；夏勇消歧
  zju-hospital.md                  浙大一院 × 梁廷波：424,911 例怎么拿到的
  hupan-lab.md                     湖畔实验室是什么（制度性接口）
  grassroots-network.md            八家县医院：为什么是这几家
  damo-hiring.md                   达摩院美国实体现状 + 这个圈子的求职通道（★ 求职直接相关）
  radar-vs-medsam.md               与 MedSAM 的关系（含双向对抗立场记录）
data/
  names-final.json                 ★ 中文名的【唯一真源】，含把握等级
  authors-meta.json                ★ 单位/身份/PANDA 标记的【唯一真源】
  build_name_table.py              README 名表由上面两个 JSON 生成，不要手改表格
  pubmed-42752131.xml              RADAR 的 PubMed 原始记录
  pubmed-37985692-panda.xml        PANDA 的 PubMed 原始记录
  authors-raw.json / radar-authors.tsv    两篇的结构化作者表 + 重合标记
  wf-authors.json                  人物调查 workflow 全量返回（50 agent）
  wf-medsam-relation.json          MedSAM 关系 workflow 全量返回（9 agent）
  raw/                             【各 agent 的原始返回，未经编辑，仅作出处存档】
    people-raw.json                  40 人的调查 + 对抗核查原文
    ctx-*.md                         8 个机构/血统专题
    contact-*.md                     5 个 MedSAM 取证专题
    evidence/                        damo-lineage 的 API 原始 JSON
```

**还没提升成 `sources/` 页、但内容很值的原始专题：**

- [`data/raw/ctx-radar-audit.md`](data/raw/ctx-radar-audit.md) —— RADAR 各项数字的独立技术审计（哪些在摘要里、哪些只在新闻稿里、哪些查不到）

> [!strategy] SSoT 约定
> - **中文名与单位身份的唯一真源是 `data/names-final.json` + `data/authors-meta.json`。** README 的总表是**生成的**（`python3 data/build_name_table.py`），改名字请改 JSON 再重跑，不要手改 README 的表格正文。
> - **`sources/` 是裁决后的结论，`data/raw/` 是未编辑的出处存档。** 两者冲突时以 `sources/` 为准 —— 但 raw 留着，让你能自己复核我裁得对不对。
