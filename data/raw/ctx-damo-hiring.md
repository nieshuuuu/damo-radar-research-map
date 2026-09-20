# 达摩院医疗 AI 人员流动与招聘状况核查（截至 2026-09-20）

## 0. 方法与证据说明（重要）

本次会话的 WebSearch 配额（200/200）在开工时已被耗尽，所有结论改用**一手数据源**获得，反而比搜索引擎摘要更硬：

| 来源 | 用途 | 访问方式 |
|---|---|---|
| PubMed E-utilities | 署名单位随时间的变化、发文量趋势 | `eutils.ncbi.nlm.nih.gov` esearch/efetch |
| arXiv HTML 全文 | 作者脚注里的实时雇主 | `arxiv.org/html/<id>` |
| h1bdata.info（美国劳工部 LCA 披露） | 谁在美国办身份、什么岗位、什么地点 | `https://h1bdata.info/index.php?em=<雇主>&job=&year=All+Years` |
| 达摩院/阿里招聘系统 API | 在招岗位全量 | `POST https://joindamo.alibaba.com/position/search`（带 XSRF-TOKEN） |
| 蚂蚁招聘站 | 在招岗位 | `https://talent.antgroup.com/off-campus` |
| Philips / NVIDIA 招聘 API | 岗位 JD 原文（含签证条款） | Workday CXS API |

**没有公开来源的数字（薪资谈判区间、签证名额、团队人头）一律不写。** LCA 披露里的薪资是雇主申报的法定最低工资，不是 offer，下文出现时都按此理解。

---

## 1. 达摩院在美国的实体、地点与规模

### 1.1 法律实体（H-1B 申报主体）
`h1bdata.info` 上以 "ALIBABA" 开头的全部 253 条记录分布：

- **ALIBABA GROUP (US) INC** — 172 条，**这是研究/算法岗的雇主实体**
- ALIBABA CLOUD US LLC / INC — 53 条（几乎全是 SRE、运维、售前）
- ALIBABA.COM US E-COMMERCE CORP(ORATION) — 26 条（电商、物流、法务）

URL: https://h1bdata.info/index.php?em=ALIBABA&job=&year=All+Years

### 1.2 地点（论文署名 vs. 用工记录，交叉验证）

论文署名（PubMed 2025–2026 年 33 篇 DAMO 论文中抽出的原始字符串）：

| 署名字符串 | 出现次数 | 代表人 |
|---|---|---|
| `DAMO Academy, Alibaba Group, Hangzhou, China` | 33 | 主力 |
| `DAMO Academy, Alibaba Group, New York, NY` | 10 | Dakai Jin、Dazhou Guo、Ke Yan、Yirui Wang、Zi Li、Qinji Yu、Le Lu |
| `DAMO Academy, Alibaba Group, Washington, DC, USA` | 8 | Ling Zhang（ling.z@alibaba-inc.com）、Yingda Xia、Le Lu |
| `DAMO Academy, Bellevue, WA, US` | 2 | Weitao Du（AI for Science / 蛋白方向，不是医疗影像） |
| `Hupan Lab(oratory), Hangzhou 310023` | 频繁与 DAMO 并列 | 杭州主力全员 |

关键修正：**任务假设的「论文里 Washington DC，PANDA 时期写 New York」是"先后关系"，实际是"并存关系"。** 2026 年同期发表的论文里两个地址同时在用：
- Radiology 2026（喉/下咽癌 ENE）：8 位作者全部署 `New York, NY` — https://pubmed.ncbi.nlm.nih.gov/?term=%22DAMO+Academy%22%5BAffiliation%5D
- Science 2026-09-17（就是你给的那篇腹部 CT）：Ling Zhang、Yingda Xia 署 `Alibaba DAMO Academy, Washington, DC, USA`，DOI `10.1126/science.aec6129`，PMID 42752131
- Diagnostics 2026：Le Lu 署 `New York, NY 10014`（曼哈顿一个具体邮编）

用工记录（LCA）对同一时期的说法：
- WASHINGTON, DC 总共 **8 条**（7 条 + 1 条 "DISTRICT OF COLUMBIA, DC"）
- 其中唯一一条研究类：`ALIBABA GROUP (US) INC | SENIOR ALGORITHM ENGINEER | $137,176 | WASHINGTON, DC | 申报 2026-04-17 | 起始 2026-10-01`
- NEW YORK, NY 19 条，但算法岗全部集中在 2022 年
- 美国研究岗的真正重心一直是 **BELLEVUE, WA（68 条）和 SUNNYVALE, CA（129 条）**

### 1.3 规模判断（有依据的推断，不是内部消息）

`ALIBABA GROUP (US) INC` 按申报年份：2019:18 → **2020:66（峰值）** → 2021:41 → 2022:24 → 2023:31 → 2024:20 → 2025:32 → 2026:21。

更说明问题的是**职级头衔的消失**：`RESEARCH SCIENTIST` 这个头衔 2019–2022 年有 13 条，**2022 年之后再没出现过**，全部换成 `Senior/Staff Algorithm Engineer`。

**结论**：DAMO 的 "New York / Washington DC" 不是成建制实验室，更像少数资深研究员（Ling Zhang、Yingda Xia、Dakai Jin、Le Lu 等）的远程/小型据点，行政上挂 `Alibaba Group (US) Inc`。DC 这个地址在 2026 年确实还在办新身份（1 条，2026-10-01 起），所以还活着，但不是一个可以"投简历进去"的机构。

---

## 2. 吕乐（Le Lu）离开之后，谁在管

### 2.1 先修正时间线：「2025-06 离开」这个说法我查不到证据

可验证的署名序列：

| 日期 | 论文 | Le Lu 的署名单位 |
|---|---|---|
| 2025-06-25 | arXiv 2506.20282（骨质疏松机会性筛查） | DAMO Academy, Alibaba Group |
| 2025-08-11 | arXiv 2508.07788 | （该文通讯是 Dakai Jin / DAMO） |
| 2025-09-01 | arXiv 2509.01360（M3Ret） | DAMO Academy, Alibaba Group |
| **2026-03-06** | arXiv 2603.05884（计算病理专家共识） | **Ant Group** |
| **2026-05-05** | arXiv 2605.04234 | **Medical AI Lab, Ant Group** |
| **2026-07-09** | Nature Communications，DOI 10.1038/s41467-026-74865-5 | **Ant Group, Sunnyvale, CA, USA** |

**2025 年 9 月他还在用 DAMO 署名。公开可验证的最早蚂蚁署名是 2026 年 3 月。** "2025-06 离开"要么是内部消息（我无法证实），要么是记错了。写进最终文档时请标注为"未证实"。

注意 PubMed 里 2025–2026 年仍有 6 篇 DAMO 论文挂他的名字——那是投稿滞后，不能当作"还在 DAMO"的证据。

### 2.2 他的完整轨迹（PubMed 署名可查）

NIH Clinical Center（`Lu L` + NIH Clinical Center 署名 16 篇）→ **PAII Inc.**（平安美国研究院，Bethesda MD；`"PAII"[Affiliation]` 共 30 篇，他占 14 篇，集中在 2020–2022）→ **Alibaba DAMO Academy**（纽约/DC，2022–2025）→ **Ant Group Medical AI Lab, Sunnyvale CA**（2026–）。

这是一条非常清晰的"美国华人医学影像 AI 产业带"轨迹：**NIH → 中国大厂的美国研究据点 → 换一家中国大厂的美国研究据点**。地理位置几乎没动过，换的是公司。

### 2.3 现在 DAMO 医疗 AI 的实际负责人（按通讯作者/末位作者判断）

我不臆测头衔，只列可验证的信号：

| 人 | 证据 | 判断 |
|---|---|---|
| **Ling Zhang**（`ling.z@alibaba-inc.com`，DAMO Washington DC） | Science 2026 腹部 CT 末位通讯；Nature Medicine 2025 胃癌筛查通讯；Nature Medicine 2026 肝脏恶性肿瘤通讯；Annals of Oncology 2026 结直肠癌 corresponding。2025–26 年 DAMO 论文中出现 9 次，**最高频** | 临床旗舰论文线的实际负责人，且人在美国 |
| **Minfeng Xu**（`eric.xmf@alibaba-inc.com`，DAMO 杭州 + Hupan Lab） | 2025–26 年多篇末位作者（arXiv 2508.07788、2506.20282、2509.01360 等均以他收尾） | 杭州侧的组织负责人 |
| **Ke Yan**（`yanke.yan@alibaba-inc.com`） | 通讯作者身份出现 2 次 | 技术线 lead |
| **Dakai Jin**（`dakai.jin@a…`，署名 New York） | Radiology 2026 头颈 ENE 一整组 8 人全挂纽约 | 放疗/头颈线独立成组 |

**没有任何一份公开材料说明"接任者"是谁。** 从通讯作者分布看，更像是 Le Lu 走后**分裂成"Ling Zhang（美国，临床旗舰）+ Minfeng Xu（杭州，工程主力）+ Dakai Jin（纽约，放疗）"三条平行线**，而不是有人整体接手。

### 2.4 有没有重组/收缩的公开迹象 —— 结论：**不是解散，是"论文照发、招聘停摆、重心转移"**

三组互相矛盾的证据，必须一起看：

**(a) 发文量没有塌** — PubMed `"DAMO Academy"[Affiliation]` 按年：2019:1 / 2020:3 / 2021:5 / 2022:18 / 2023:13 / 2024:13 / 2025:15 / **2026:20（历史最高）**。
查询：https://pubmed.ncbi.nlm.nih.gov/?term=%22DAMO+Academy%22%5BAffiliation%5D

**(b) 但达摩院自己已经不是一个"医疗 AI 机构"了** — 我把达摩院社招官网的岗位**全量拉了下来（133 个）**：
- 地点：上海 120、杭州 83、北京 55、成都 23、深圳 17，**美国 0**
- 方向：约 90% 是 **RISC-V / 芯片 / 计算技术**（CPU 架构、SoC 验证、DFT、封装、DDR、编译器……），其余是具身智能、大模型推理优化
- **医疗相关岗位全站只有 1 个**：`达摩院-超声AI大模型算法专家-具身智能`（杭州）
- 另有 1 个 `达摩院-蛋白质算法工程师`
- 入口：https://joindamo.alibaba.com/home?lang=zh

**(c) 医疗 AI 的产品化重心转去了阿里健康和千问** — 我又抽了阿里集团社招前 1000 个岗位：
- 关键词"医疗"只命中：`阿里健康-*`（问答策略、搜推 Java、药企数字化、环肽/多肽药化科学家）、`千问事业部-医疗Agent算法专家`、`高德销服科技-*`（卖广告给医院的销售）
- 关键词"影像"只命中 1 个 `娱驰BG-DIT数字影像工程师`（影视行业，不是医学影像）
- **1000 个岗位里 0 个美国地点**（海外只有中国香港 3、巴西利亚 1、吉隆坡 1）
- 入口：https://talent.alibaba.com/off-campus/home?lang=zh

另外，百度百科的达摩院词条称"目前，达摩院隶属于阿里云智能集团，研究方向更加聚焦于数据科学与 AI for Science"（https://baike.baidu.com/item/阿里巴巴达摩院（杭州）科技有限公司/23197542）——**此条为二手来源，建议标注，但与我拉到的招聘数据方向一致**。

---

## 3. 达摩院医疗 AI 目前的公开招聘：几乎没有，美国完全没有

| 问题 | 答案 | 证据 |
|---|---|---|
| 达摩院有公开医疗 AI 岗吗 | **1 个**，超声大模型算法专家，杭州 | joindamo API 全量 133 岗 |
| 在美国招吗 | **不招**。达摩院 133 岗 + 阿里集团抽样 1000 岗，美国地点为 0 | 同上 |
| 但美国还有人办身份吗 | **有**。`ALIBABA GROUP (US) INC`，Senior Algorithm Engineer，Washington DC，2026-04-17 申报，2026-10-01 起 | h1bdata |
| 实习呢 | 官网无公开实习入口；arXiv 论文脚注里大量出现 "This work was done when X conducted an internship at DAMO Academy"（如 arXiv 2511.05170），说明**实习走的是导师/合作关系定向，不是公开投递** | arXiv 2511.05170v2 |

那个唯一的医疗岗要求原文（节选）：*"有超声影像 AI 相关研究或产业经验 / 有 LLM / VLM / 多模态大模型研发经验 / 熟悉 Transformer、Diffusion、CLIP、SAM"*，加分项是 CVPR/ICCV/MICCAI/NeurIPS。**这是纯 CV/多模态大模型的语言，不是成像物理的语言。**

---

## 4. 蚂蚁的医疗业务：是什么、吕乐在做什么、有没有美国实体

### 4.1 组织形态
蚂蚁没有一个叫 "Ant Healthcare" 的对外品牌实体；在招聘系统里它叫 **健康事业群**，在国际侧叫 **Ant Health International**。

在招岗位（`https://talent.antgroup.com/off-campus`，搜"医疗"，共 4 条）：
- **`蚂蚁集团-医疗大模型训练算法-健康事业群`**，上海/杭州，发布 2026-08-26 ← 这是唯一的医疗算法岗
- `蚂蚁集团-Senior Legal & Compliance Counsel-Ant Health International`，上海/香港/新加坡，2026-09-11 ← 说明国际健康业务的法律落点是**香港和新加坡，不是美国**

蚂蚁官网技术页把方向说得很直白：「百灵大模型……重点布局大模型在**医疗健康**、金融服务、生活服务等场景的应用，致力于为每个人提供 AI 管家」（https://www.antgroup.com/technology）。

### 4.2 吕乐在那里做什么
署名 **`Medical AI Lab, Ant Group`**（arXiv 2605.04234）。从他 2026 年的三篇看，方向是：
- 医学重建的隐式神经表示（与上科大 Yuyao Zhang 组合作，arXiv 2605.04234）
- 计算病理基础模型 / Agentic AI 的临床落地共识（arXiv 2603.05884，与 Sen Yang 同属 Ant Group）
- 神经母细胞瘤的视觉-语言统一模型（Nature Communications 2026-07-09）

即：**从 DAMO 时期的"非增强 CT 机会性癌症筛查"转向"病理 + 视觉语言模型 + 重建"**，仍然不是成像物理。

### 4.3 美国实体 —— 有，而且在办 H-1B

这是本次调查最有价值的一条发现：

**`Ant Group, Sunnyvale, CA, USA`** 是他 Nature Communications 2026 论文上的原始署名字符串（PMID 42426002）。对应的用工实体是：

**ANT TECHNOLOGIES US INC**（https://h1bdata.info/index.php?em=ANT%20TECH&job=&year=All+Years），全部 11 条记录：

| 岗位 | 申报薪资 | 地点 | 申报日 |
|---|---|---|---|
| ASSISTANT RESEARCHER OF ANT GROUP RESEARCH INSTITUTE | $237,786 | Sunnyvale, CA | 2025-11-21 |
| ASSOCIATE RESEARCHER | $237,786 | Sunnyvale, CA | 2025-12-08 |
| ASSOCIATE RESEARCHER | $127,712 | Sunnyvale, CA | **2026-05-12** |
| SENIOR ALGORITHM ENGINEER | $96,117 | Bellevue, WA | **2026-05-12** |
| PUBLIC RELATIONS ADVISOR | $216,000 | Sunnyvale, CA | 2026-05-07 |
| （另 6 条 2022–2024 年的 Algorithm Engineer / Technical Expert / SRE） |

另一个老实体 **ALIPAY US INC** 有 51 条，但**2023 年后停止申报**（https://h1bdata.info/index.php?em=ALIPAY&job=&year=All+Years）。

蚂蚁官网美国岗位共 **15 个，全部在 Sunnyvale**，首页 10 个是：SRE×2、Payments Operations、Enterprise BD、Internal Audit、Deputy BSA/AML Officer、Antom BD×2、Account Management，以及 **`Antgroup-Research Staff Member-Robotics`（Sunnyvale，2026-09-13）**。**没有任何医疗方向的美国岗位。**

**结论**：蚂蚁在美国有一个会办 H-1B、职级叫 "Researcher" 的研究实体（Ant Technologies US Inc, Sunnyvale），吕乐的 Medical AI Lab 挂这个地址。但**它不公开招医疗岗**——要进去只能靠定向/内推。

---

## 5. 圈内其他工业界去处：谁在美国招、谁办签证

全部基于 LCA 披露 + 在招 JD 原文。

### 5.1 明确在美国招 + 明确办身份 + **方向对口成像物理**

**① 联影 United Imaging Healthcare North America（休斯顿）— 本次调查中最贴 Shu 的一家**
- H-1B：14 条，**全部集中在 2025–2026**（https://h1bdata.info/index.php?em=UNITED%20IMAGING&job=&year=All+Years）
- 2026 年一口气申报了 4 个 CT 研究岗：`RESEARCH SCIENTIST, CT`（$110,000）、`CT SENIOR RESEARCH SCIENTIST`（$115,000）、`LEAD RESEARCH SCIENTIST, CT`（$139,172，2026-06-11）、`SENIOR RESEARCH SCIENTIST`（$113,850），全部 Houston, TX
- 当前公开在招 42 个岗（https://recruiting.paylocity.com/recruiting/jobs/All/d527ad39-680d-45fa-9178-38a81898aec2/United-Imaging-North-America），研究岗有 `Senior Research Scientist - MRI`（Houston）、`PET/CT Research Collaboration Scientist`（Salt Lake City）、`Clinical Scientist - Ultrasound`（Bellevue）——**CT 岗此刻没挂出来，但 3 个月前刚办过 4 个人的身份，说明是周期性开放**。这家值得直接发定向信。

**② 联影智能 UII America Inc（Burlington, MA）**
- H-1B 21 条，2025:5 / 2026:3，全部 Burlington MA：`EXPERT RESEARCH SCIENTIST`（$171,588）、`SENIOR RESEARCH SCIENTIST`（$163,229 / $165,000 ×2 / $157,581）
- https://h1bdata.info/index.php?em=UII%20AMERICA&job=&year=All+Years
- 这是联影智能（uii-ai.com）的美国研究臂，方向偏影像 AI 而非成像物理

**③ Canon Medical Research USA（Vernon Hills, IL）**
- `RECONSTRUCTION SCIENTIST`，$116,854，**2026-05-08 申报，2026-10-01 起** — 岗位名就叫"重建科学家"
- https://h1bdata.info/index.php?em=CANON%20MEDICAL%20RESEARCH&job=&year=All+Years

**④ GE HealthCare（`GE PRECISION HEALTHCARE LLC`）**
- 2025–26 共 87 条；Waukesha, WI（GE 的 CT 大本营）31 条
- 对口条目：`LEAD SCIENTIST - CLINICAL PHYSICS`（Waukesha，2026-04-09）、`LEAD RECON APPLICATION ENGINEER`（Waukesha，2025-05-01）、`SENIOR SCIENTIST - IMAGING AND ARTIFICIAL INTELLIGENCE`（Menlo Park，2026-04-03）
- https://h1bdata.info/index.php?em=GE%20PRECISION%20HEALTHCARE&job=&year=All+Years

**⑤ 西门子医疗（`SIEMENS MEDICAL SOLUTIONS USA INC`）**
- 2025–26 共 **167 条**，是名单里最稳的大厂 sponsor
- Princeton, NJ（研究中心）16 条：`AI RESEARCH SCIENTIST`（$165,000，2026-05-06）、`AI ML SCIENTIST`×3、`SENIOR DEEP LEARNING SCIENTIST- MEDICAL IMAGE ANALYSIS`（$145,000，2025-06-24）、`RESEARCH AND TECHNOLOGY MANAGER`（$196,123）
- 另有 `RESEARCH SCIENTIST`（Columbus, OH，2026-05-21）
- 注意：Princeton 是 **AI 方向**；西门子的 CT 成像物理主力在德国 Forchheim，不在美国
- https://h1bdata.info/index.php?em=SIEMENS%20MEDICAL%20SOLUTIONS&job=RESEARCH&year=All+Years

### 5.2 在美国招、办身份，但**方向不对口**

**NVIDIA Healthcare**
- Holger Roth **仍在 NVIDIA**（arXiv 2608.18311v1，2026-08-18，署名 `NVIDIA, Santa Clara, CA, USA`，通讯邮箱 `hroth@nvidia.com`），方向是联邦学习 / MONAI / 多模态放射模型
- 在招：`Senior Applied Research Scientist, Multimodal Foundation Models – Healthcare`（Santa Clara，6 天前发布）https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/Senior-Applied-Research-Scientist--Multimodal-Foundation-Models---Healthcare_JR2022219
- H-1B：`NVIDIA CORPORATION` + 职位含 "RESEARCH SCIENTIST" 共 311 条，**2025:99 / 2026:64** — 名单中最强的 sponsor，没有之一
- 但岗位语言是 foundation model / VLM / agent，**不是成像物理**

### 5.3 对口但**明确拒绝办签证** —— 必须单独点名

**Philips，`Research Scientist - Computed Tomography (Orange, OH)`，2026-09-15 发布**
https://philips.wd3.myworkdayjobs.com/en-US/jobs-and-careers/job/Orange-OH-Ohio-United-States/Research-Scientist---Computed-Tomography--Orange--OH-_586925

JD 要求原文（节选）：
> *"Maintain deep expertise in CT physics and advanced processing algorithms, with **strong emphasis on photon-counting CT as a top priority**. Brings additional knowledge in **spectral, dual-energy, and multi-energy CT**, ... enabling improved **material differentiation** and image quality optimization."*
> *"minimum of a **Ph.D. in Physics**... with a background in the theory of medical image formation and reconstruction"*
> *"**physics-based simulation**, and hands-on prototype or scanner work"*

薪资区间 $115,000–$183,000（OH）。这几乎是照着你的简历写的——光子计数、能谱、材料分解、物理仿真、物理博士。

然后是这一句：
> *"**US work authorization is a precondition of employment. The company will not consider candidates who require sponsorship for a work-authorized visa, now or in the future.**"*

**"now or in the future" 这个措辞会连 F-1 OPT / STEM-OPT 一起挡掉**——因为 OPT 到期后必然需要 sponsorship。不要因为"我 OPT 期间不需要 sponsor"就去投，这条 JD 已经把未来也写死了。

矛盾之处（值得知道）：Philips North America LLC 本身 2025–26 办了 **67 条 H-1B**，但集中在 Cambridge MA（44 条）和 Bothell WA，**都是软件/供应链/IT 岗，不是俄亥俄的 CT 物理团队**。即"公司办，这个组不办"。

### 5.4 无美国实体 / 基本不现实

- **上海人工智能实验室**：`h1bdata.info` 搜 "SHANGHAI ARTIFICIAL" → **0 条**。无美国用工实体，不存在 H-1B 路径。
- **Riverain Technologies**（Miamisburg, OH，ClearRead CT 肺结节）：全历史 **1 条** H-1B（2021）。https://h1bdata.info/index.php?em=RIVERAIN&job=&year=All+Years — 公司太小，不能当作路径。
- **Siemens Healthineers Endovascular Robotics Inc**（Newton, MA）：5 条，全是软件/质量岗，与影像无关。

### 5.5 额外找到的、和你冠脉/PCAT 方向最近的一批（原任务没列，但更对口）

| 公司 | 业务 | 美国 H-1B 证据 |
|---|---|---|
| **HeartFlow**（San Francisco） | 冠脉 CT FFR，和 CCTA 定量最近 | 51 条，2025:7 / 2026:9；`SENIOR RESEARCH SCIENTIST`（$156,077，**2026-06-04 申报，2026-10-01 起**）；其余多为 Senior Software Engineer（$186,826）https://h1bdata.info/index.php?em=HEARTFLOW&job=&year=All+Years |
| **Cleerly**（NY / Centennial CO） | 冠脉斑块定量（和你的 FAI / PCAT 方向直接相邻） | 13 条；`SR. SCIENTIST, ML`（$174,482，2025-07-25）https://h1bdata.info/index.php?em=CLEERLY&job=&year=All+Years |
| **Elucid Bioimaging**（Boston） | CT 斑块成分定量——**本质就是材料分解的临床化** | 14 条；`SR. IMAGE PROCESSING ENGINEER`（$150,000，2025-07-22）、`SR. SOFTWARE ENGINEER, IMAGE PROCESSING`（2025-04-02）https://h1bdata.info/index.php?em=ELUCID&job=&year=All+Years |
| Subtle Medical | MRI/PET 降噪加速 | 18 条，2025–26 有 3 条（ML SW Engineer / Data Scientist）|

---

## 6. 对 Shu 的可及性判断（成像物理 + 定量估计，非纯 CV/DL）

先把结论说死：**你要找的不是"医疗 AI"，是"CT 成像物理 / 重建 / 定量"。这两个在美国是两个不同的招聘市场，中国大厂的美国据点属于前者，且对外关闭。**

### A 级 — 真实可及（方向对口 + 有 2025–2026 的实际办身份记录）
1. **United Imaging Healthcare North America, Houston** — 2026 年 5–6 月连办 4 个 CT research scientist 的 H-1B。你的光子计数/材料分解/冠脉周围脂肪定量与 uCT 的能谱产品线直接对口。**建议定向发信，不等岗位挂出来。**
2. **Canon Medical Research USA, Vernon Hills IL** — `Reconstruction Scientist` 2026-05 刚办过。
3. **GE HealthCare, Waukesha WI** — `Lead Scientist - Clinical Physics`（2026-04）、`Lead Recon Application Engineer`（2025）。
4. **Siemens Medical Solutions USA, Princeton NJ** — sponsor 最稳（167 条/两年），但要接受把自己讲成 "medical image analysis scientist" 而不是 "imaging physicist"。

### B 级 — 需要"翻译"简历，但有真实入口
5. **Elucid Bioimaging / Cleerly / HeartFlow** — 冠脉 CT 定量三家。你的 PCAT / FAI / 材料分解经验和它们的产品几乎同构，但**岗位名字是 image processing engineer / ML scientist**。要把"噪声-偏差误差预算、定量估计的不确定度"讲成"measurement pipeline + validation + regulatory-grade reproducibility"，否则会被当成学术候选人筛掉。
6. **UII America, Burlington MA** — Senior/Expert Research Scientist 有 sponsor 记录，但偏 AI 诊断而非物理。

### C 级 — 错配，不建议投入时间
7. **达摩院美国（DC/NY）** — 对外 0 公开岗位；唯一的医疗岗在杭州且是超声大模型；即便进得去，岗位语言是 LLM/VLM/CLIP/SAM，你的物理建模优势会被当成"不是我们要的技能"。
8. **蚂蚁 Medical AI Lab (Sunnyvale)** — 实体存在、会办 H-1B（Ant Technologies US Inc，最近一条 2026-05-12），但官网 15 个美国岗 0 个医疗。**唯一路径是通过吕乐本人或 Sen Yang 定向**，而且方向已转向病理 + VLM。
9. **NVIDIA Healthcare** — sponsor 能力最强，但要的是多模态基础模型 / agent，不是成像物理。除非你愿意整体转向 foundation model。
10. **上海人工智能实验室** — 无美国实体，签证路径不存在。

### 明确排除
11. **Philips Orange OH 的 CT Research Scientist** — 这是名单里**技术上最贴合你的一个岗位**，但 JD 白纸黑字拒绝任何现在或将来需要 sponsorship 的候选人。不要投。（如果你将来拿到绿卡，这个组是第一顺位。）

### 一条结构性判断
LCA 数据里有一个很硬的规律：**"Research Scientist" 这个头衔在中国大厂的美国实体里正在消失**（Alibaba Group (US) Inc 自 2022 年后再无此头衔，全换成 Algorithm Engineer），而在美/日/欧医疗设备公司里仍然健在（United Imaging 的 `CT Senior Research Scientist`、Canon 的 `Reconstruction Scientist`、GE 的 `Lead Scientist - Clinical Physics`、Philips 的 `Research Scientist - CT`）。**对一个成像物理博士来说，设备厂的研究岗市场比互联网大厂的医疗 AI 市场更真实、更稳定、也更认你的物理训练。** 把精力配比倒过来。

---

## 7. 需要标注为"未证实"的三处

1. **「Le Lu 2025-06 离开达摩院」** — 无公开证据。可验证的只是：2025-09 仍署 DAMO，2026-03 起署 Ant Group。
2. **「达摩院隶属阿里云智能集团」** — 仅见于百度百科，非一手来源；但与招聘数据（全站 90% 是芯片岗）方向一致。
3. **各人中文姓名** — 本次核查全程使用论文原始英文署名与公司邮箱，**未做中英文姓名匹配**，不要从本报告推断中文名。

## 8. 落盘用的关键 URL 清单

```
Science 论文        https://doi.org/10.1126/science.aec6129   (PMID 42752131)
吕乐蚂蚁署名        https://doi.org/10.1038/s41467-026-74865-5 (PMID 42426002, "Ant Group, Sunnyvale, CA, USA")
吕乐 Medical AI Lab https://arxiv.org/abs/2605.04234
DAMO 发文量趋势     https://pubmed.ncbi.nlm.nih.gov/?term=%22DAMO+Academy%22%5BAffiliation%5D
达摩院社招          https://joindamo.alibaba.com/home?lang=zh
阿里集团社招        https://talent.alibaba.com/off-campus/home?lang=zh
蚂蚁社招            https://talent.antgroup.com/off-campus
Alibaba H-1B        https://h1bdata.info/index.php?em=ALIBABA&job=&year=All+Years
Ant Technologies US https://h1bdata.info/index.php?em=ANT%20TECH&job=&year=All+Years
United Imaging H-1B https://h1bdata.info/index.php?em=UNITED%20IMAGING&job=&year=All+Years
UII America H-1B    https://h1bdata.info/index.php?em=UII%20AMERICA&job=&year=All+Years
Canon MRU H-1B      https://h1bdata.info/index.php?em=CANON%20MEDICAL%20RESEARCH&job=&year=All+Years
GE HealthCare H-1B  https://h1bdata.info/index.php?em=GE%20PRECISION%20HEALTHCARE&job=&year=All+Years
Siemens H-1B        https://h1bdata.info/index.php?em=SIEMENS%20MEDICAL%20SOLUTIONS&job=&year=All+Years
HeartFlow H-1B      https://h1bdata.info/index.php?em=HEARTFLOW&job=&year=All+Years
Cleerly H-1B        https://h1bdata.info/index.php?em=CLEERLY&job=&year=All+Years
Elucid H-1B         https://h1bdata.info/index.php?em=ELUCID&job=&year=All+Years
Shanghai AI Lab     https://h1bdata.info/index.php?em=SHANGHAI%20ARTIFICIAL&job=&year=All+Years  (0 条)
Philips CT 岗(拒签证) https://philips.wd3.myworkdayjobs.com/en-US/jobs-and-careers/job/Orange-OH-Ohio-United-States/Research-Scientist---Computed-Tomography--Orange--OH-_586925
United Imaging NA 岗 https://recruiting.paylocity.com/recruiting/jobs/All/d527ad39-680d-45fa-9178-38a81898aec2/United-Imaging-North-America
NVIDIA Healthcare 岗 https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/Senior-Applied-Research-Scientist--Multimodal-Foundation-Models---Healthcare_JR2022219
Holger Roth 现职     https://arxiv.org/abs/2608.18311  (NVIDIA, Santa Clara, hroth@nvidia.com)
```

中间数据文件（供后续 agent 复用，无需重跑）：
- `/private/tmp/claude-501/-Users-shunie-Developer/152a37b5-0538-44e5-b0f8-ccce9c6bab33/scratchpad/damo_jobs.json` — 达摩院 133 个在招岗位全量 JSON
- `/private/tmp/claude-501/-Users-shunie-Developer/152a37b5-0538-44e5-b0f8-ccce9c6bab33/scratchpad/damo_recent.xml` — 2025–2026 年 33 篇 DAMO 论文的 PubMed 完整记录（含全部署名字符串）
- `/private/tmp/claude-501/-Users-shunie-Developer/152a37b5-0538-44e5-b0f8-ccce9c6bab33/scratchpad/pm1.xml` — Science 腹部 CT 论文的完整作者-单位映射
- `/private/tmp/claude-501/-Users-shunie-Developer/152a37b5-0538-44e5-b0f8-ccce9c6bab33/scratchpad/h1bq2.py` — H-1B 查询脚本，`python3 h1bq2.py "雇主名|岗位关键词"`