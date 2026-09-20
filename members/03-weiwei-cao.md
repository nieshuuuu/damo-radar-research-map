# 曹维维 Weiwei Cao — RADAR 视觉侧表征的技术底座

> RADAR 第 3 / 40 位作者 · 阿里巴巴达摩院 + 湖畔实验室 + 浙江大学计算机科学与技术学院 · **共同第一作者**（6 人之一）

## 一句话画像

2024 年从中科院苏州医工所博士毕业进达摩院，两年内拿下 CVPR 一作、ICCV 一作、*Science* 共同一作。研究主线只有一条：**3D CT 的视觉-语言预训练**——不靠人工标注，把诊断报告本身当监督信号。==媒体反复宣传的 RADAR「器官级细粒度对齐」，正是下面 CVPR 2024、fVLM、ICCV 2025 三篇的工程化集成。==

## 在 RADAR 里的位置

- **第 3 / 40 位作者，共同第一作者**。RADAR 的共同一作共 6 人，位次 1–6：[章琦](01-qi-zhang.md)、[张建鹏](02-jianpeng-zhang.md)、曹维维、Zilin Lu、常琬星、Haonan Ding —— 后三位与曹维维同级，不在其下。
- 论文标的单位串是 **达摩院 + [湖畔实验室](../sources/hupan-lab.md) + 浙大计算机学院**，与 [张建鹏](02-jianpeng-zhang.md) 一字不差。说明是全职算法核心，不是外部合作者，也不是临床方。
- **承担角色（推断）**：CT 视觉编码器的预训练，以及「器官级细粒度对齐 / 异常语义增强」这一块的核心实现，即 RADAR 表征学习的技术底座。推断依据是位次、与张建鹏完全相同的单位串，以及技术血缘——RADAR 的关键创新正是曹维维一作的 CVPR 2024（跨模态蒸馏做 CT 表征）、参与的 fVLM（器官级对齐）、一作的 ICCV 2025（解剖正常性建模放大异常信号）三篇的直接延续。技术拆解见 [radar-technical-teardown](../sources/radar-technical-teardown.md)。
- **不在 PANDA 作者列表**。PANDA（*Nat Med* 2023）发表时曹维维还在苏州做 2D 分割，2024 年才入职；RADAR 与 PANDA 的人员桥梁是 [张灵](39-ling-zhang.md)、[夏英达](20-yingda-xia.md)、吕乐三人，不含在内。
- **已被纳入平扫 CT 筛癌主力班底**：2026 年 *Annals of Oncology* 结直肠癌多中心研究中署名第 6、与前五位并列标星，同批作者含 JP Zhang、YD Xia、K Cao —— 这是 PANDA 那条产品线的结直肠版。

## 背景与履历

| 时间 | 单位 · 职位 | 备注 |
|---|---|---|
| 约 2019—2024 | 中国科学技术大学 博士研究生（培养单位：中国科学院苏州生物医学工程技术研究所 医学影像研究室） | 导师郑健（**推断**）。苏州医工所研究生归口中国科大、共建生物医学工程学院（苏州），这解释了论文上 USTC 与 SIBET 两单位并列。起止年份仅见于学术聚合页，无官方来源 |
| 2020-12 | 中科院苏州医工所 | 专利「基于边界及邻域引导的医学图像分割方法及系统」第 2 发明人，第 1 发明人郑健 —— 2020 年底前已在所内工作的机构级证据 |
| 2021 | 同上 | 首篇一作《Edge and neighborhood guidance network》（BSPC），进入分割方向 |
| 2022 | 同上 | 一作 ICL-Net（IEEE JBHI），个人一作被引最高 |
| 2024-04 之前 | **阿里巴巴达摩院** | CVPR 2024 一作论文首页，达摩院已排在本人单位串第 1 位；阿里巴巴（中国）名下最早一件发明专利优先权日 2024-04-03 |
| 2024 | 博士毕业，正式入职达摩院 / 湖畔实验室 | 同年发表 NeighborNet（JBHI）等收尾于苏州的工作 |
| 2024-04 之后、2025-08 之前 | 浙江大学计算机科学与技术学院 | 身份性质（博士后 / 兼聘 / 联合聘任）**未查实**。2025-08 的 ICCV 论文作者块已变为 浙大计算机 + 达摩院 + 湖畔，USTC 与苏州医工所同时消失 |
| 2025 起 | 阿里巴巴达摩院（杭州）科技有限公司 | 专利申请人主体由「阿里巴巴（中国）」转为达摩院独立法人，与单位串演变同步 |
| 2026-09-18 | *Science* 393(6817):eaec6129，RADAR 第 3 作者、共同一作 | |

本科、硕士院校与专业完全未查到。

## 研究方向

- **主线：3D CT 的医学视觉-语言预训练（VLP）与器官级细粒度图文对齐。** 目标是免人工标注、用放射报告当监督，下游是零样本多病种诊断与报告生成。
- **技术演进三步**：①CT 图文对太少 → 用语言引导检索把 3D CT 配到语义最近的 2D X 光，从成熟 X 光专家模型蒸馏到 3D CT 编码器（CVPR 2024）；②把 CT 拆成解剖单元做器官级对齐（fVLM）；③针对「医学图像信噪比低、报告信噪比高」的语义密度落差，一路用大语言模型抽解剖异常标签做疾病级对比学习，另一路用轻量 VQ-VAE 在潜空间建模正常解剖分布、靠重建误差放大异常（ICCV 2025）。
- **副线：多模态融合与临床任务落地**——PET-CT 胰腺肿瘤分割、报告生成评测基准、强化学习式报告生成、并列多癌平扫 CT 筛查。
- **早期（2021–2024，苏州阶段）：2D 医学图像分割与配准**——皮肤镜病变、乳腺超声 / DBT、像素邻域关系建模、CT-CBCT 可变形配准。
- 同期还被拉去做过 X 射线 BGA 焊球缺陷、表面缺陷检测这类**工业检测题**，是典型工科所「课题跟着经费走」的培养模式。

## 代表作

被引数为 **2026-09-20** 抓取。

| 论文 | 期刊 · 年份 | 作者位次 |
|---|---|---|
| An expert-level generalist AI for abdominal CT diagnosis（RADAR） | *Science* 393(6817):eaec6129 · 2026 | **第 3 / 40，共同一作** |
| Boosting Vision Semantic Density with Anatomy Normality Modeling for Medical Vision-language Pre-training | ICCV 2025 · pp.23041–23050 | **第 1**（通讯 张建鹏）· 被引 17 |
| Bootstrapping Chest CT Image Understanding by Distilling Knowledge from X-ray Expert Models | CVPR 2024 · pp.11238–11247 | **第 1**（双通讯 张建鹏 + 郑健）· 被引 46 |
| Large-scale and Fine-grained Vision-language Pre-training for Enhanced CT Image Understanding（fVLM） | ICLR 2025 Spotlight | 第 3 · 被引 79（参与论文中最高） |
| ICL-Net: Global and Local Inter-Pixel Correlations Learning Network for Skin Lesion Segmentation | IEEE JBHI 27(1):145–156 · 2022 | **第 1** · 被引 94（个人一作最高） |
| MFCNet: A multi-modal fusion and calibration network for 3D pancreas tumor segmentation on PET-CT images | Computers in Biology and Medicine 155:106657 · 2023 | 第 3 · 被引 51（苏州时期唯一一篇胰腺题） |
| Edge and neighborhood guidance network for 2D medical image segmentation | BSPC 69:102856 · 2021 | **第 1**（最早一作）· 被引 27 |
| Colorectal cancer detection using non-contrast CT and deep learning: a multicenter and international cohort study | *Annals of Oncology* · 2026 | 第 6（并列标星） |

其余：NeighborNet（IEEE JBHI 28(8), 2024，第 1 作者）、CDFRegNet（CMPB 2022）、NCRNet（CBM 2022，被引 31）、FMRNet（*Medical Physics* 49(1), 2022，第 4 作者，被引 59）、CT-FineBench（ACL 2026，第 3）、RadSight（arXiv 2026，第 2）、Disease-Centric VLP（arXiv 2026，第 2）。

## 师承与关系

**第一段谱系（2019–2024，苏州）。** 中科院苏州医工所医学影像研究室，**郑健**（Jian Zheng）门下（**推断**：三条间接证据——CVPR 2024 论文里郑健同单位且带通讯星号；郑健的机构个人页把曹维维的三篇一作 ICL-Net、NeighborNet、Bootstrapping Chest CT 列入自己的代表论著；2020 年那件苏州医工所专利上郑健第 1、曹维维第 2 发明人。没有任何来源出现「导师—学生」的字面表述）。郑健是苏州医工所研究员、博导，方向为基于人工智能的医学影像技术。同组常见合作者有杨晓冬、袁刚、曹玉柱、刘兆邦、Yakang Dai、Dehui Xiang，临床合作方是常州方向的 Xinye Ni。苏州的线至今没断：2025 年《图学学报》「基于类内区域动态解耦的半监督肺气管分割」仍署第 2 作者，通讯仍是郑健。

**第二段谱系（2024 起，杭州）。** 进入达摩院医疗影像 AI 线（见 [damo-lineage](../sources/damo-lineage.md)）。这条线顶层是吕乐与 [张灵](39-ling-zhang.md)，都出自 NIH / PAII 一脉；**直接带教的是 [张建鹏](02-jianpeng-zhang.md)** —— 曹维维两篇一作（CVPR 2024、ICCV 2025）的通讯作者都是张建鹏，两人在 RADAR 的单位串一字不差。

**迁移方式（推断）**：不是跟着郑健走的，而是经由 CVPR 2024 那篇合作论文完成交接 —— 该文是唯一一篇同时挂 达摩院 + USTC + 苏州医工所、并由张建鹏与郑健双通讯的作品，形式上就是交接协议；此后 USTC / 苏州医工所从其单位串里彻底消失。路径类型见 [academic-pipeline](../sources/academic-pipeline.md)。

**与本文其他作者的直接共同署名**：
- CVPR 2024 一作论文合作者含 [夏英达](20-yingda-xia.md)、[Tony C W Mok](19-tony-c-w-mok.md)、[叶香华](22-xianghua-ye.md)、吕乐。
- ICCV 2025 一作论文合作者含 [李玺](16-xi-li.md)、[叶香华](22-xianghua-ye.md)、吕乐、[张灵](39-ling-zhang.md)。
- fVLM（曹维维为第 3 作者）作者串横跨算法与临床两侧：Zhongyi Shui、[张建鹏](02-jianpeng-zhang.md)、曹维维、Sinuo Wang、Ruizhe Guo、吕乐、Lin Yang、[叶香华](22-xianghua-ye.md)、[梁廷波](40-tingbo-liang.md)、[章琦](01-qi-zhang.md)、[张灵](39-ling-zhang.md)。

**固定搭档圈**（按共同署名频次）：张建鹏、常琬星、Ruifeng Yuan、Bowen Shi、Zhongyi Shui、Sinuo Wang、Zilin Lu、张灵、吕乐、夏英达、Tony C W Mok、叶香华。

## 学术指标

- **Google Scholar**（profile `user=foe2YScAAAAJ`，验证邮箱域 alibaba-inc.com，自述单位 "Alibaba DAMO Academy, Zhejiang University"，标签 Medical Image Analysis / Vision and Language），**2026-09-20 抓取**：总引用 **513**、h-index **12**、i10-index **13**。全时段与「2021 年至今」两列数值完全相同 —— 说明 2021 年前无被引论文，与 2019 年入学、2021 年首篇一作相容。
- **ORCID**：0000-0002-8991-9915。记录建于 2022-02，除姓名外基本为空，无教育与任职条目，仅关联 8 篇作品。
- ==同名污染极重，中英文皆然。== 本页所有条目由三项硬锚点绑定：上述 ORCID、上述 Google Scholar profile 编号、论文首页单位串（达摩院 + USTC + 苏州医工所 → 浙大计算机 + 达摩院 + 湖畔）。**AMiner 上方向与单位均正确的那条 profile 已混入一位做密码学的同名作者，其 h-index 等指标不可引用。**
- 中文媒体报道 RADAR 时从未点名，因此拿不到「高级算法专家」这类官方头衔表述。

## 对 Shu 意味着什么

**是技术对接对象，不是去向。** 同辈（2024 年博士毕业）、无招 PhD 或博后的权限、人在杭州，对 visa / sponsorship 这条线价值为零。唯一真实的接口：RADAR 与 fVLM 的「器官级细粒度对齐」本质是把 CT 拆成解剖单元再与报告对齐，==而 Shu 手里的水 / 脂 / 蛋白分数图、PCAT 脂肪衰减、光子计数的多能量通道，恰好是比单通道 HU 更富信息的器官级定量输入==——达摩院这条线缺物理上更干净的输入，Shu 缺下游临床评价场景，这是真互补，不是硬凑；要接触这条线，写信对象是张建鹏或张灵，不是本人。**反向的警示更值钱**：RADAR 走的是大数据 + 弱监督 + 端到端，对「物理建模 + 小样本 + 可解释定量」是结构性竞争，代码已开源（400 stars，2026-09-20），跑一遍它在腹部脂肪 / 胰腺这类任务上的实际表现，比读论文更能判断自己的定量方法在**临床终点**层面还剩多少不可替代性。最后，这条履历本身是模板：==先和工业实验室合作发一篇，再谈位置。==

## 未解决

- **本科、硕士院校与专业**：完全未查到。
- **职称 / 职级**：无任何官方表述。
- **浙江大学计算机学院身份的性质**（博士后？兼聘？浙大-达摩院联合聘任？）：未查实。已确认的只有时间窗（2024-04 尚为 USTC + 苏州医工所，2025-08 已为浙大计算机 + 达摩院 + 湖畔）。同单位串的张建鹏、Yanjie Zhou 疑为同一种制度安排。
- **博士在读起止年份 2019–2024**：仅见于自动生成的学术聚合页 alphaXiv，无官方来源；与 2020-12 已署名苏州医工所专利、2021 年首篇一作相容，但不构成证据。
- **郑健为其博士导师**：推断，三条间接证据，无字面表述来源。
- **RADAR 中的具体分工**：推断。*Science* 正文的 Author Contributions 段落未能获取（需订阅）。
- 中文媒体从未点名，公开痕迹极少：无个人主页、无机构个人页、无公开讲者页。

## 来源

- https://pubmed.ncbi.nlm.nih.gov/42752131/ — RADAR, *Science* 393(6817):eaec6129, 2026；完整作者单位串与 ORCID
- https://scholar.google.com/citations?user=foe2YScAAAAJ — Google Scholar（验证邮箱域 alibaba-inc.com）；513 引用 / h-index 12 / i10 13，2026-09-20 抓取
- https://orcid.org/0000-0002-8991-9915 — ORCID（记录基本为空）
- https://openaccess.thecvf.com/content/CVPR2024/papers/Cao_Bootstrapping_Chest_CT_Image_Understanding_by_Distilling_Knowledge_from_X-ray_CVPR_2024_paper.pdf — CVPR 2024 一作论文，首页三单位串与双通讯
- https://arxiv.org/abs/2508.03742 — ICCV 2025 一作论文；作者块显示单位已变为浙大计算机 + 达摩院 + 湖畔
- https://arxiv.org/abs/2501.14548 — fVLM（ICLR 2025 Spotlight），第 3 作者
- https://sibet.cas.cn/sourcedb/zw/yjdw/yjy/201306/t20130621_3879596.html — 苏州医工所 郑健 个人页，代表论著含其三篇一作
- https://sibet.cas.cn/yjsjy2020/zsxx_169599/202309/t20230919_6883339.html — 苏州医工所研究生归口中国科大、共建生物医学工程学院（苏州）
- http://www.txxb.com.cn/CN/abstract/abstract2450.shtml — 《图学学报》46(4):763–774, 2025，「基于类内区域动态解耦的半监督肺气管分割」，第 2 作者，通讯郑健
- https://patents.google.com/patent/CN112489062A/zh — CN112489062A「基于边界及邻域引导的医学图像分割方法及系统」，申请人中科院苏州医工所，发明人郑健、曹维维等
- https://github.com/alibaba-damo-academy/damo-radar — RADAR 开源库，2026-07-03 创建，400 stars（2026-09-20）
- https://github.com/alibaba-damo-academy/fvlm — fVLM 开源库
- https://pubmed.ncbi.nlm.nih.gov/37985692/ — PANDA, *Nat Med* 2023；36 位作者中无其人
- https://www.alphaxiv.org/@weiwei-cao — 唯一给出「2019–2024 USTC 博士、2024– 阿里在职」的来源（弱来源，未二次验证）
- 照片：未找到可确认身份的公开照片
