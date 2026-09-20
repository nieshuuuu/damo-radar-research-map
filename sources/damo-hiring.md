# 达摩院医疗 AI 的人员流动与求职通道

> 裁决后的结论页。**完整取证与全部 URL 在 [../data/raw/ctx-damo-hiring.md](../data/raw/ctx-damo-hiring.md)**（agent 原始返回，未编辑）。
> ⚠️ **本页关键条目我逐条亲手复核过**，复核方式标在每条后面。未能复核的明确标出。
> 核对日期：2026-09-20。

---

## 一句话

==**你要找的不是"医疗 AI"，是"CT 成像物理 / 重建 / 定量"。这在美国是两个不同的招聘市场。**==
中国大厂的美国据点属于前者，且对外关闭；**设备厂（联影/佳能/GE/西门子）属于后者，正在招，而且在办身份。**

---

## ① 达摩院美国：还活着，但不是一个能投简历的机构

**硬证据是美国劳工部的 LCA 披露**（`h1bdata.info`，我自己拉的全表，253 条）：

```
实体分布
  172  ALIBABA GROUP (US) INC          ← 研究/算法岗的雇主实体
   49  ALIBABA CLOUD US LLC            ← SRE / 运维 / 售前
   26  ALIBABACOM US E-COMMERCE CORP   ← 电商 / 物流 / 法务
    4  ALIBABA CLOUD US INC
    2  ALIBABA GROUP US INC
```

### ⚠️ 最说明问题的一条：`RESEARCH SCIENTIST` 这个头衔消失了

```
2019: 5    2020: 7    2021: 2    2022: 1    2023 之后: 0
```

==2022 年之后，阿里美国实体再没有申报过一个叫 "Research Scientist" 的岗位。== 全部换成 `Senior / Staff Algorithm Engineer`。

### Washington DC 在 2026 年 = 一个人

论文署名里 `DAMO Academy, Alibaba Group, Washington, DC` 出现 8 次（张灵、夏英达等）。但 LCA 里 DC 的研究/算法岗**只有一条**：

| 岗位 | 申报薪资 | 地点 | 申报日 | 起始 |
|---|---:|---|---|---|
| SENIOR ALGORITHM ENGINEER | $137,176 | WASHINGTON, DC | 2026-04-17 | 2026-10-01 |

New York 侧的算法岗全部集中在 **2022 年**（3 条）。

> [!insight] 判读
> DAMO 的 "New York / Washington DC" **不是成建制实验室**，更像少数资深研究员（张灵、夏英达、Dakai Jin）的小型据点，行政上挂 `Alibaba Group (US) Inc`。
> ==DC 这个点 2026 年确实还在办新身份，所以还活着 —— 但它不是一个可以"投简历进去"的机构。==

⚠️ **agent 报告称"达摩院社招全站 133 岗，美国 0，医疗岗只有 1 个（超声大模型，杭州）"。我复核时 `joindamo.alibaba.com/position/search` 返回 `datas: null, totalCount: 0`，未能独立确认这个计数。** 但上面的 LCA 数据独立指向同一结论，而且 LCA 是政府披露，比招聘页更硬。

---

## ② 吕乐（Le Lu）去向：时间点要更正

⚠️ **我之前说的"2025-06 离开达摩院去蚂蚁"没有公开证据。** 可验证的署名序列是：

| 日期 | 论文 | 署名单位 |
|---|---|---|
| 2025-06-25 | arXiv 2506.20282 | DAMO Academy, Alibaba Group |
| 2025-09-01 | arXiv 2509.01360（M3Ret）| DAMO Academy, Alibaba Group |
| **2026-03-06** | arXiv 2603.05884 | **Ant Group** |
| **2026-05-05** | arXiv 2605.04234 | **Medical AI Lab, Ant Group** |
| **2026-07-09** | *Nat Commun*, PMID 42426002 | **Ant Group, Sunnyvale, CA, USA** |

==2025 年 9 月他还在用 DAMO 署名；公开可验证的最早蚂蚁署名是 2026 年 3 月。== "2025-06" 要么是内部消息，要么是记错了 —— **标为未证实**。

（PubMed 里 2025–2026 仍有 6 篇 DAMO 论文挂他的名，那是投稿滞后，不能当"还在 DAMO"的证据。）

**他的完整轨迹**：NIH Clinical Center → PAII Inc.（平安美国研究院，Bethesda MD）→ Alibaba DAMO（纽约/DC）→ **Ant Group Medical AI Lab, Sunnyvale CA**。
==地理位置几乎没动过，换的是公司。== 这是一条"美国华人医学影像 AI 产业带"的标准轨迹。

**谁在管现在的达摩院医疗 AI** —— 没有任何公开材料说明"接任者"。按通讯作者分布看，更像**分裂成三条平行线**：

```
Ling Zhang（张灵，Washington DC）  临床旗舰论文线 —— 2025-26 出现 9 次，最高频
Minfeng Xu（杭州 + 湖畔）          工程主力
Dakai Jin（New York）              放疗/头颈线，Radiology 2026 一整组 8 人全挂纽约
```

**蚂蚁在美国有实体，会办 H-1B**（`ANT TECHNOLOGIES US INC`，Sunnyvale，我核过 11 条），但**官网 15 个美国岗 0 个医疗**。唯一路径是定向内推，且吕乐的方向已转向病理 + 视觉语言模型 + 重建 —— **仍然不是成像物理**。

---

## ③ 可及性分级

### 🟢 A 级 —— 真实可及：方向对口 + 有 2025–2026 实际办身份记录

**① United Imaging Healthcare North America（Houston, TX）—— 本次最贴你的一家**

我拉的全表，2026 年 5–6 月**五周内连办 7 个 research scientist**：

| 岗位 | 申报薪资 | 申报日 |
|---|---:|---|
| **RESEARCH SCIENTIST, CT** | $110,000 | 2026-05-06 |
| **CT SENIOR RESEARCH SCIENTIST** | $115,000 | 2026-05-06 |
| RESEARCH SCIENTIST | $113,850 | 2026-05-06 |
| SENIOR RESEARCH SCIENTIST | $105,000 | 2026-05-06 |
| SENIOR RESEARCH SCIENTIST-MRI | $130,000 | 2026-05-13 |
| SENIOR RESEARCH SCIENTIST-MRI | $130,000 | 2026-05-14 |
| **LEAD RESEARCH SCIENTIST, CT** | $139,172 | 2026-06-11 |

==三个岗位名里直接带 "CT"。这是一次成批扩张，不是零星补人。==
💡 **CT 岗此刻官网没挂出来，但三个月前刚办过一批身份 —— 说明是周期性开放。建议定向发信，不要等岗位挂出来。**

**② Canon Medical Research USA（Vernon Hills, IL）**
`RECONSTRUCTION SCIENTIST`，$116,854，**2026-05-08 申报** —— 岗位名就叫"重建科学家"。该实体历史上还办过 `Senior Reconstruction Scientist`、`Senior Imaging Scientist`。

**③ GE HealthCare（Waukesha, WI —— GE 的 CT 大本营）**
`LEAD SCIENTIST - CLINICAL PHYSICS`（2026-04-09）、`LEAD RECON APPLICATION ENGINEER`（2025-05-01）。2025–26 共 87 条，Waukesha 占 31 条。

**④ Siemens Medical Solutions USA（Princeton, NJ）**
2025–26 共 **167 条**，名单里最稳的 sponsor。但 Princeton 是 **AI 方向**（`AI Research Scientist` $165,000、`Senior Deep Learning Scientist - Medical Image Analysis` $145,000）；==西门子的 CT 成像物理主力在德国 Forchheim，不在美国==。要接受把自己讲成 "medical image analysis scientist"。

### 🟡 B 级 —— 需要"翻译"简历，但有真实入口

**冠脉 CT 定量三家 —— 和你的 PCAT / FAI / 材料分解几乎同构：**

| 公司 | 业务 | H-1B 证据 |
|---|---|---|
| **Elucid Bioimaging**（Boston）| CT 斑块成分定量 —— ==本质就是材料分解的临床化== | 14 条；`SR. IMAGE PROCESSING ENGINEER` $150,000（2025-07）|
| **HeartFlow**（San Francisco）| 冠脉 CT FFR | 51 条，2026 年 9 条；`SENIOR RESEARCH SCIENTIST` $156,077（2026-06-04 申报，2026-10-01 起）|
| **Cleerly**（NY / Centennial CO）| 冠脉斑块定量 | 13 条；`SR. SCIENTIST, ML` $174,482（2025-07）|

⚠️ 但**岗位名字是 image processing engineer / ML scientist**。要把"噪声-偏差误差预算、定量估计的不确定度"讲成 **"measurement pipeline + validation + regulatory-grade reproducibility"**，否则会被当成学术候选人筛掉。

**UII America（Burlington, MA）** —— 联影智能的美国研究臂，21 条 H-1B，`Expert Research Scientist` $171,588 / `Senior Research Scientist` $157–165k。偏影像 AI 诊断而非物理。

### 🔴 C 级 —— 错配，不建议投入时间

| | 为什么 |
|---|---|
| **达摩院美国（DC/NY）** | 对外 0 公开岗位；唯一的医疗岗在杭州且是超声大模型；岗位语言是 LLM/VLM/CLIP/SAM，==你的物理建模优势会被当成"不是我们要的技能"== |
| **蚂蚁 Medical AI Lab（Sunnyvale）** | 实体存在、会办身份，但 15 个美国岗 0 个医疗；唯一路径是通过吕乐本人定向，且方向已转病理 + VLM |
| **NVIDIA Healthcare** | sponsor 能力最强（Research Scientist 头衔 2025:99 / 2026:64），但要的是多模态基础模型 / agent。Holger Roth 仍在（`hroth@nvidia.com`），方向是联邦学习 / MONAI |
| **上海人工智能实验室** | `h1bdata` 搜 "SHANGHAI ARTIFICIAL" → **0 条**。无美国用工实体，签证路径不存在 |
| **Riverain Technologies** | 全历史 1 条 H-1B（2021）。公司太小，不能当路径 |

---

## ④ ⛔ 单独点名：Philips 那个岗，技术上最贴你，但明确不办签证

**`Research Scientist - Computed Tomography (Orange, OH)`**，2026-09-15 发布，我亲自拉 Workday API 取的原文。

JD 里的技术要求（逐字）：

> "Maintain deep expertise in CT physics and advanced processing algorithms, with **strong emphasis on photon-counting CT as a top priority**. Brings additional knowledge in **spectral, dual-energy, and multi-energy CT**, as well as cone beam CT, enabling improved **material differentiation** and image quality optimization."
>
> "You have a minimum of a **Ph.D. in Physics**, Mathematics, Biomedical, Electrical, or Nuclear Engineering, with a background in the theory of medical image formation and reconstruction."

薪资 **$115,000 – $183,000**。==光子计数、能谱、材料分解、物理博士 —— 这几乎是照着你的简历写的。==

然后是这一句，同样逐字：

> "**US work authorization is a precondition of employment. The company will not consider candidates who require sponsorship for a work-authorized visa, now or in the future.**"

> [!strategy] "now or in the future" 这五个字是关键
> ==它会连 F-1 OPT / STEM-OPT 一起挡掉==，因为 OPT 到期后必然需要 sponsorship。
> **不要因为"我 OPT 期间不需要 sponsor"就去投** —— 这条 JD 已经把未来写死了。

⚠️ 矛盾之处（值得知道）：Philips North America LLC 本身 2025–26 办了 **67 条 H-1B**，但集中在 Cambridge MA（44 条）和 Bothell WA，**全是软件/供应链/IT 岗，不是俄亥俄的 CT 物理团队**。即 ==**公司办，这个组不办**==。

💡 如果将来拿到绿卡，这个组是第一顺位。

---

## ⑤ 一条结构性判断

LCA 数据里有一个很硬的规律：

```
"Research Scientist" 这个头衔

  在中国大厂的美国实体里 → 正在消失
      Alibaba Group (US) Inc:  2019:5 → 2020:7 → 2021:2 → 2022:1 → 之后 0
      全部换成 Algorithm Engineer

  在美/日/欧医疗设备公司里 → 健在
      United Imaging:  CT Senior Research Scientist / Lead Research Scientist, CT
      Canon:           Reconstruction Scientist
      GE HealthCare:   Lead Scientist - Clinical Physics
      Philips:         Research Scientist - CT
```

> [!insight] 结论
> ==对一个成像物理博士来说，**设备厂的研究岗市场比互联网大厂的医疗 AI 市场更真实、更稳定、也更认你的物理训练**。把精力配比倒过来。==
> 这与 [[project_job_market_two_tracks_2026_09]] 里"titles decide visa sponsorship"是同一条规律的两个侧面：**头衔不只决定签证，也决定你的物理训练算不算数。**

---

## 复核状态

| 条目 | 我的复核方式 | 结果 |
|---|---|---|
| United Imaging 2026 年 7 个 research scientist | 自拉 h1bdata 全表 | ✅ 确认，且比 agent 报的多（agent 说 4 个）|
| Canon `Reconstruction Scientist` 2026-05-08 | 自拉 h1bdata 全表 | ✅ 确认 |
| Ant Technologies US Inc, Sunnyvale | 自拉 h1bdata 全表 | ✅ 确认 11 条 |
| Alibaba 实体分布 + Research Scientist 头衔消失 | 自拉 h1bdata 全表 253 条 | ✅ 确认 |
| Washington DC 只有 1 条研究岗（2026-04-17）| 同上 | ✅ 确认 |
| Philips JD 拒绝 sponsorship 的原文 | 自拉 Workday CXS API | ✅ 逐字确认 |
| 达摩院社招 133 岗 / 美国 0 / 医疗 1 | joindamo API | ❌ **接口返回空，未能独立确认** |
| 吕乐 2025-06 离职 | PubMed / arXiv 署名序列 | ⚠️ **未证实，改为"2025-09 仍署 DAMO，2026-03 起署蚂蚁"** |

---

## 未解决

- 薪资谈判区间 —— **LCA 里的数字是雇主申报的法定最低工资，不是 offer**
- 达摩院/蚂蚁内部团队人头 —— 无公开来源
- United Imaging 下一轮 CT 岗的开放时间 —— 只能从"2025-05 / 2026-05 两次成批申报"推测是年中，**这是推断**

---

## See Also

- [damo-lineage.md](damo-lineage.md) —— NIH → PAII → 达摩院的整建制迁徙（同一批人的上半场）
- [../data/raw/ctx-damo-hiring.md](../data/raw/ctx-damo-hiring.md) —— 完整取证与全部 URL
- [../README.md](../README.md)
