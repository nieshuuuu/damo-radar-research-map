# 叶香华 Xianghua Ye — 浙大一院放疗科副主任，达摩院医疗 AI 在浙江一侧合作最久的临床医生

<img src="../photos/22-xianghua-ye.jpg" width="160" align="right" alt="叶香华">

> RADAR 第 22 / 40 位作者 · 浙江大学医学院附属第一医院放疗科（论文单位 12）· 临床端专家节点

## 一句话画像

胸部肿瘤精准放疗的主任医师，医院官网把「肿瘤放化疗人工智能辅诊」直接写进研究方向——这在放疗科临床医生里极少见。从 2021 年起连续 6 年、14 篇论文，**跟着吕乐（Le Lu）团队从平安 PAII 一路走到阿里巴巴达摩院**，算法团队换了东家，临床合作者没换。RADAR 40 位作者里，==单位串含「放疗科 / 放射治疗」的只有这一人==。

## 在 RADAR 里的位置

- 第 **22/40** 位，单位 12（浙大一院放疗科）。既不在达摩院 / 湖畔实验室 / 浙大计算机的算法块，也不在浙一放射科（[肖文波](38-wenbo-xiao.md)等）的影像诊断块，更不在肝胆胰外科（[章琦](01-qi-zhang.md)、[梁廷波](40-tingbo-liang.md)）的主导块——是一个被单独拎出来的**临床专家节点**。
- 最可能的角色（**推断**）：临床数据策展 + 专家级阅片标注 + 多中心临床验证。依据是位次、单位归属与既往 5 年的固定分工（头颈 OAR 多中心专家勾画、食管 GTV 多机构验证、结外侵犯专家判读）。RADAR 需要大量专家级腹部 CT 判读作参照标准，正好是这个工位。
- 不太可能参与模型设计、训练与代码（**推断**）。在全部 14 篇影像 AI 论文里，方法学的通讯 / 末位作者始终是达摩院一侧（Dakai Jin、吕乐、Ke Yan 等）；即便在 Nature Communications 2022 挂共同第一作者，通讯端仍在算法方。
- ⚠️ 角色判断**未经原文 Author Contributions 印证**（Science 正文付费墙），整段建立在位次 + 单位 + 既往合作史的三角推断之上。
- **不在 PANDA 作者名单里**（36 人逐一核对无此人）。合理解释（推断）：PANDA 走的是胰腺 + 腹部外科 / 放射科轴，与胸部肿瘤放疗不搭。但与达摩院体系的合作**比 PANDA 那一拨更长、更深**，只是器官轴不同。参见 [达摩院谱系](../sources/damo-lineage.md)、[浙大一院](../sources/zju-hospital.md)。

## 背景与履历

| 时间 | 单位 · 职位 | 备注 |
|---|---|---|
| 年份不详 | 博士学位 | 医院官网记最高学历与学位均为博士。授予单位、年份，以及本科 / 硕士院校专业，均未查到 |
| ≤2013 | 南方医科大学南方医院 放疗科（广州） | Tiam1 与肝癌转移的分子机制课题；*Int J Cancer* 2013 共同第一作者（原文注记 "J.H. and X.Y. contributed equally"）。在该处是学生还是在职医师，未证实 |
| 2011 已在 | 浙江大学医学院附属第一医院 放疗科 | *Eur J Radiol* 2011 低剂量腹部 CT 去噪论文的出版社元数据中，单位已写作「浙大一院放射治疗科」。迁移的确切年份未定，两处署名一度并存 |
| 2014–2018 | 浙大一院 放疗科 | 产出集中在抗肿瘤药物不良反应的 meta 分析（aflibercept、everolimus / temsirolimus、硼替佐米、BRAF 抑制剂、eribulin、阿帕替尼）。与后来的影像 AI 线无关 |
| 2020 | 同上 | 第一篇深度学习论文：*Eur Radiol* COVID-19 厚层 CT 定量（第 8/13）。同年参与两项 GBD 疾病负担研究 |
| 2021 | 同上 · 与 **PAII Inc.**（Bethesda，吕乐团队）合作 | *Clin Cancer Res* 口咽癌 FDG-PET 生存预测（第 4/17）；*Front Oncol* 食管癌 GTV 自动勾画（第 1/25） |
| 2022 起 | 同上 · 合作方整体变为**阿里巴巴达摩院** | *Nat Commun* 2022 头颈部 28 个危及器官勾画，**共同第一作者**。此后连续出现在 IEEE TMI、*Med Image Anal*、*Radiology*、*Nat Commun*、*Science* |
| 现任 | 浙大一院放疗科 **主任医师** · **放疗科副主任** | 2026 年首次以通讯作者身份出现（IJROBP 放射性肺炎血浆蛋白组学，与科主任严森祥并列通讯），开始带自己的转化研究线。庆春院区周三上午、之江院区周一上午门诊 |

所在科室为国家级临床重点专科（肿瘤学），5 台直线加速器、3 台大孔径模拟定位 CT，医护 84 人（医生 26、医学物理师 12、技术员 23、护士 23）。

## 研究方向

- **胸部肿瘤精准放疗与综合治疗**：乳腺癌、肺癌、食管癌、胸腺瘤；技术覆盖 SBRT、TOMO 螺旋断层、射波刀。
- **医学影像 AI 的临床端**——官网原文「肿瘤放化疗人工智能辅诊」。承担的是**数据、专家标注、多中心临床验证**这一端，不是算法端。
- 自动勾画（OAR / GTV）：头颈部 28 个危及器官、食管癌 GTV、气道树分割（IEEE TMI 2024，第 10/11）。
- 预后与检测：口咽癌 PET 生存、胰腺癌术后生存、食管癌术前生存（IEEE TMI 2026，第 16/18）、喉与下咽癌结外侵犯、3D 淋巴结自回归跟踪（IEEE TMI 2026，第 15/16）。
- 方法学基础设施上的临床端：通用解剖嵌入 UAE、域迁移主动学习 DistAL（IEEE TMI 2025，第 5/8）。
- 放疗生物学与并发症：食管鳞癌放疗抵抗的铁死亡机制（CoQ / FSP1，*Drug Resist Updat* 2024，第 7/18）、放射性肺炎的纵向血浆蛋白组学。
- ==一个罕见的历史细节==：2011 年以第 4 作者参与过**低剂量腹部 CT 去噪**（大尺度邻域加权强度平均），第一作者是陈阳（Yang Chen，现东南大学，中国 CT / 低剂量重建方向的主力），通讯为陈武凡、罗立民。也就是说，对「图像是怎么造出来的」有过一手接触——这在放疗科临床医生里极罕见，也解释了为什么能十几年如一日当成像 AI 团队的临床锚点。

## 代表作

| 论文 | 期刊 · 年份 | 作者位次 |
|---|---|---|
| An expert-level generalist AI for abdominal CT diagnosis（RADAR） | *Science* 2026（PMID 42752131） | 22 / 40 |
| Comprehensive and clinically accurate head and neck cancer organs-at-risk delineation on a multi-institutional study | *Nature Communications* 2022（PMID 36253346） | **1 / 26，共同第一作者** |
| Multi-Institutional Validation of Two-Streamed Deep Learning Method for Automated Delineation of Esophageal Gross Tumor Volume | *Frontiers in Oncology* 2021 卷（2022-01 上线，PMID 35141147） | **1 / 25，第一作者** |
| Towards automated organs at risk and target volumes contouring: Defining precision radiation therapy in the modern era | *J National Cancer Center* 2022（PMID 39036546） | 4 / 5（全文仅 5 人：Dakai Jin、Dazhou Guo、Jia Ge、叶香华、吕乐） |
| UAE: Universal Anatomical Embedding on multi-modality medical images | *Medical Image Analysis* 2025（PMID 40209554） | 6 / 9 |
| Pretreatment CT Identification of Extranodal Extension in Laryngeal and Hypopharyngeal Cancers Using Deep Learning | *Radiology* 2026（PMID 41528225） | 14 / 19 |
| Longitudinal Plasma Proteomics Reveals an Immuno-thrombotic Signature That Predicts Radiation Pneumonitis in Lung Cancer | *Int J Radiat Oncol Biol Phys* 2026（PMID 42176864） | 23 / 24，**并列通讯** |
| Improving low-dose abdominal CT images by Weighted Intensity Averaging over Large-scale Neighborhoods | *European Journal of Radiology* 2011（PMID 20709478） | 4 / 9 |

另有 *Nat Commun* 2026 脂肪性肝病多模态 AI（第 5/22，PMID 41672973）、*Ann Surg* 2023 胰腺癌术后生存（第 9/23，末位作者 [张灵](39-ling-zhang.md)）、*BMC Pulm Med* 2022 免疫检查点抑制剂诱发放射回忆性肺炎个案（第 1/4）。

## 师承与关系

- **南方医院一段（推断）**：2013 年 Tiam1 / 肝癌转移论文以南方医院放疗科署名、共同第一作者，末位作者为 Longhua Chen（陈龙华）。但同文第 3 位 Jian Guan、第 9 位 Yanqing Ding 在中国医学院署名惯例里同样是典型导师位，**博士导师究竟是谁未排他，无中文来源直接证实**。
- **陈阳 / 陈武凡 / 罗立民 的图像重建线（不构成师承）**：2011 年低剂量腹部 CT 去噪论文里的临床侧配合。这是与「成像物理 / 重建」这一世界唯一一次直接接触，时间极早。有意思的是 RADAR 单位 26 是东南大学附属中大医院放射科（[居胜红](36-shenghong-ju.md)），与陈阳同校——是否有残存联系，未查证。
- ⭐ **吕乐团队（PAII → 达摩院），最重要的一段**：2021 年两文中吕乐、Dakai Jin、Dazhou Guo、Jiawen Yao、[张灵](39-ling-zhang.md) 的单位全部标 "PAII Inc., Bethesda"；2022 年起同一批人整体变为 "DAMO Academy, Alibaba Group, New York"。叶香华**两个阶段都在**，并在跨越点（2022 *Nat Commun*）升为共同第一作者。不是达摩院的人，而是==被算法团队一路带过东家更迭的临床端合作者==。
- **台湾长庚支线**：早期两篇勾画论文的另一端是林口长庚（Tsung-Ying Ho、Chien-Yu Lin、Bing-Shen Huang 等），吕乐团队 PAII 时期的固定临床伙伴，叶香华是「两岸双中心」的浙江一侧。2022 年后这条支线淡出，被达摩院—浙大一院的杭州本地闭环取代。
- **科室内部**：严森祥（浙大一院放疗科主任）是最高频的资深共同作者（*Nat Commun* 2022、*Front Oncol* 2021、IJROBP 2026 等）。2026 年首次与严森祥并列通讯，是从「科主任的人」转向「自己带线」的标志。
- **与本文其他作者**：UAE（*Med Image Anal* 2025）的末位作者是西北工业大学[夏勇](13-yong-xia.md)（RADAR 第 13 位）。与 [夏英达](20-yingda-xia.md)、[张建鹏](02-jianpeng-zhang.md) 等达摩院算法前排属不同分工层。

## 学术指标

| 指标 | 数值（2026-09-20 抓取） | 说明 |
|---|---|---|
| 总被引（自建口径） | **≥ 1007** | 对 35 篇经 PubMed 单位串人工确认属「浙大一院放疗科 / 南方医院放疗科 Xianghua Ye」的论文逐篇取 OpenAlex 引用数；为保守剔除了 3 篇归属存疑者，故为**下界** |
| h-index（自建口径） | **≥ 14** | 同上口径，下界 |
| 前五高被引 | 292 / 163 / 116 / 60 / 53 | 分别为 *J Hematol Oncol* 2020 肺癌 GBD、*J Hematol Oncol* 2020 中国食管癌 GBD、*Eur Radiol* 2020 COVID-19、*Clin Cancer Res* 2021、*Oncotarget* 2017 |
| *Nat Commun* 2022（共同一作） | 45 | |
| Google Scholar | 未获取 | 是否存在本人认领的主页，未知 |
| ORCID | **0000-0002-4075-4777** | 作品列表仅一条，正是 RADAR 本文；无任职、教育信息。可作机读锚点，不能用于核履历 |

⚠️ **两点警告**：

1. ==被引最高的两篇是 GBD 流行病学论文，与真正的学术身份（自动勾画 + 影像 AI 临床验证）无关==。用总被引评价会严重失真；*Nat Commun* 2022 那篇共同一作的 45 次引用才是代表性影响力。
2. OpenAlex 聚合作者档案 **A5027212917（works 181 / cited 2133 / h 24）不可用**——该 ID 把南昌大学第二附属医院、丽水学院、长治医学院、山西振东制药、浙大二院、Stanford 等至少 8 个不相干机构的同名者合并在了一起。

## 同名消歧（重要）

- **浙江大学医学院附属第二医院神经内科 / 康复科另有一位持续活跃的 Xianghua Ye**，研究脑出血、血肿吸收、Gas6/Axl、细胞外囊泡（PMID 35955686、36425320、36802818、37949481、39846256 等），2022–2025 年产出与本人在时间上完全重叠。==同城、同校系统、同拼音，是最容易被缝合的对象==；其中文名未知，**不可假定也叫叶香华**。
- 另有南昌大学第二附属医院、丽水学院、长治医学院等多个 Xianghua Ye。
- PMID 38410560（*J Thorac Dis* 2024，碘-125 粒子植入）单位写「浙大一院放射科」而非放疗科，归属不确定。

## 对 Shu 意味着什么

**直接价值低，样本价值高。** 这是一位放疗科临床医生（MD），不带物理 / 工程博后，也不是达摩院编制内的人，无法作为达摩院招聘的引荐路径；方向（材料分解、水脂分解、光子计数 CT、冠脉周围脂肪）与临床线零交集。

但这是**「临床锚点」这条职业路径的教科书案例**：2014 年还在发药物毒性 meta 分析的普通主治，靠长期稳定地向一个算法团队供给专家标注与多中心验证数据，2022 年拿到 *Nature Communications* 共同第一作者，2026 年进 *Science*，同期在院内升到主任医师兼副主任。卖的不是算法，是==别人拿不到的东西==：标注、患者队列、临床可信度。Shu 在 Molloi 组手里握着的是同构资产（PCCT 原始数据、体模、材料分解真值、PCAT 测量流程）——这条路径说明，把一份别人做不了的「验证能力」稳定供给一个持续存在的算法团队，六年能换来什么。

次要的一点：2011 年那篇低剂量腹部 CT 去噪把这个人与陈阳（东南大学）、陈武凡、罗立民这条中国 CT 重建谱系连了起来。若哪天需要中国侧的重建方向对接，这是一条有共同语言的线——但注意只是「曾在场」，本人早已转向临床。

**一件不要做的事**：不要把这里当成浙大一院的门路去敲。这扇门是放疗科胸部肿瘤，敲错门概率极高；对口的是放射科（单位 8，[肖文波](38-wenbo-xiao.md) 等）。

## 未解决

- 本科、硕士院校 / 专业 / 年份：未查到。博士授予单位与年份：未查到。
- 博士导师：三名候选（Longhua Chen、Jian Guan、Yanqing Ding）均未排除，无中文来源直接证实。
- 入职浙大一院的确切年份、晋升主任医师年份、出任放疗科副主任年份：均未查到。
- 是否为硕导 / 博导：科室页写「硕士生导师 2 名，博士生导师 1 名」但未指名，不能推断。
- 国家自然科学基金项目、学会任职：未查到。
- 中文期刊论文与学位论文（知网 / 万方 / 维普）：本次未能取得，中文搜索引擎全部被拦截。「未查到」只意味着本次工具未能取得。
- PMID 40577849（*J Neurosurg Spine* 2025，脊柱转移瘤 SBRT）第 4/19 位署名 Xianghua Ye，单位仅标 Stanford 放疗科，**无任何并列的杭州单位、ORCID 或邮箱**，与本人无交叉链接——按==同名记录、身份未证实==处理，不作为经历写入。
- RADAR 中的具体贡献：需读 *Science* 正文 Author Contributions 方能坐实。
- PMID 19717279（*Comput Med Imaging Graph* 2009，PET 透射断层重建）PubMed 只写 "Ye X"、无全名无单位，归属为**推断**，不作为南方医院时期的起点证据。

## 来源

- https://www.zy91.com/department/doctor/74/9 — 浙大一院官网 叶香华 个人页（中文名、学历学位、职称、院内职务、研究方向的一手来源）
- https://www.zy91.com/department/doctor_list?dept_id=37&cid=74 — 浙大一院放疗科医生名册（10 人为高级职称子集，全科医生 26 人）
- https://www.zy91.com/department/dept/73/37 — 浙大一院放疗科科室简介
- https://pubmed.ncbi.nlm.nih.gov/42752131/ — *Science* 2026 RADAR，第 22/40
- https://pubmed.ncbi.nlm.nih.gov/36253346/ — *Nat Commun* 2022 头颈 OAR 勾画，共同第一作者
- https://pubmed.ncbi.nlm.nih.gov/35141147/ — *Front Oncol* 2021 食管癌 GTV 勾画，第一作者
- https://pubmed.ncbi.nlm.nih.gov/39036546/ — *J Natl Cancer Cent* 2022 自动勾画综述，5 人作者中第 4
- https://pubmed.ncbi.nlm.nih.gov/33947697/ — *Clin Cancer Res* 2021 口咽癌 PET 生存预测（PAII 期）
- https://pubmed.ncbi.nlm.nih.gov/40209554/ — *Med Image Anal* 2025 UAE，第 6/9
- https://pubmed.ncbi.nlm.nih.gov/41528225/ — *Radiology* 2026 结外侵犯，第 14/19
- https://pubmed.ncbi.nlm.nih.gov/38923479/ — IEEE TMI 2024 气道树分割，第 10/11
- https://pubmed.ncbi.nlm.nih.gov/42176864/ — IJROBP 2026 放射性肺炎蛋白组学，并列通讯
- https://pubmed.ncbi.nlm.nih.gov/35123465/ — *BMC Pulm Med* 2022 个案报道，第 1/4
- https://pubmed.ncbi.nlm.nih.gov/22573407/ — *Int J Cancer* 2013 Tiam1 / 肝癌转移，南方医院放疗科，共同第一作者
- https://pubmed.ncbi.nlm.nih.gov/20709478/ — *Eur J Radiol* 2011 低剂量腹部 CT 去噪（迁移节点证据）
- https://pubmed.ncbi.nlm.nih.gov/37985692/ — PANDA, *Nat Med* 2023（36 人名单逐一核对，无此人）
- https://api.openalex.org/works/pmid:20709478 — OpenAlex 记录，保留 2011 年浙大一院放疗科原始单位串
- https://api.openalex.org/authors/A5027212917 — OpenAlex 聚合档案（多人合并，数据不可用，仅留痕）
- https://pub.orcid.org/v3.0/0000-0002-4075-4777/record — ORCID，唯一作品即 RADAR
- 照片：https://www.zy91.com/department/doctor/74/9
