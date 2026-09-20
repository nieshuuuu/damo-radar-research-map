## 一、先回答你真正关心的：DAMO RADAR 和 MedSAM 到底是什么关系

**结论：没有学术合作关系，没有代码/权重继承关系；只有三条真实的连接——共同的上游工具链、共同的公开数据祖先、以及一条 2026-09-19 发生的、可验证的单向"下游消费"事件。**

### 1. 代码层面：零交集，共同祖先是 nnU-Net 而不是 SAM
- RADAR 的第三方依赖只有 LAVIS、nnU-Net、MONAI、3D-ResNets-PyTorch，README 与 requirements.txt 里**完全没有 SAM/MedSAM**：https://github.com/alibaba-damo-academy/damo-radar
- 预处理已在仓库文档里写死："We use TotalSegmentator V1 to generate segmentation masks for 104 anatomical structures"，再合并成 36 个结构、重采样到 `[1,1,5]`，链接直指 `TotalSegmentator/tree/v1.5.7`：https://raw.githubusercontent.com/alibaba-damo-academy/damo-radar/main/docs/PREPROCESS.md （你给的 v1.5.7 前提已核实）
- 顺带一个值得注意的细节：同一份文档里预处理脚本的示例路径写的是 "the original **MERLIN** data"（Stanford 的公开腹部 CT-report 数据集），说明 RADAR 公开的可复现路径跑在公开数据上，训练用的 424,911 例来自浙大一院系统，不公开。
- 反向也成立：MedSAM 的 Nature Communications 正文、MedSAM2 的 arXiv HTML 里都搜不到 DAMO / Alibaba。

### 2. 数据层面：共同祖先是 DeepLesion，但这是"公开数据的下游"而不是"人的连接"
- `wanglab/CT_DeepLesion-MedSAM2`：32,735 个病灶标注 / 32,120 个 CT 切片 / 10,594 studies / 4,427 患者，53.4 GB，页面明写 source = NIH DeepLesion，并要求同时引用 Yan et al. 2018：https://huggingface.co/datasets/wanglab/CT_DeepLesion-MedSAM2
- 你说的 Ke Yan / Le Lu 路径部分需要修正：**Ke Yan 现在确实在 DAMO（Staff Algorithm Engineer）；但 Le Lu 已于 2025 年 6 月离开 DAMO，去了 Ant Group 的 Ant Healthcare**（他本人主页与 LinkedIn 时间线一致：https://www.cs.jhu.edu/~lelu/ ）。
- 更关键的是：**Ke Yan 和 Le Lu 都不在 RADAR 的作者名单里**。我用 PubMed E-utilities 拉了 PMID 42752131 的完整 40 人作者表核对过，没有 "Yan K"、没有 "Lu L"：作者序为 Zhang Q（浙大一院，一作）、Zhang J（DAMO，共一）…… Mok TCW …… 倒数第二 Zhang L（Ling Zhang）、末位 Liang T（梁廷波）。所以 DeepLesion 这条线**连不到 RADAR 这篇论文本身**，它只连到"DAMO 这个机构里有 DeepLesion 的原作者"。
- 还有一个容易混淆的点值得你知道：DAMO/Ke Yan 那边自己有一个叫 **SAM 的东西**，是 "Self-supervised Anatomical eMbedding"（TMI 2022），比 Meta 的 SAM 更早、完全无关：https://github.com/alibaba-damo-academy/self-supervised-anatomical-embedding-v2

### 3. 唯一一条"活的"连接：Jun Ma 在 RADAR 发表两天后给它做了 demo
这是我这次挖到的最硬的一条，可直接验证：
- 2026-09-18，用户 `jizhang02` 在 damo-radar 开 issue #1 "Online tool?"。
- **2026-09-19，`JunMa11` 回帖："Here you go: https://huggingface.co/spaces/junma/RADAR-demo"**（GitHub public events API 可查：`https://api.github.com/users/JunMa11/events/public`）
- 该 Space 确实存在且在跑：owner `junma`，createdAt `2026-09-19T03:17:41Z`，Gradio，硬件 zero-a10g，license 标 `cc-by-nc-sa-4.0`（即 RADAR 权重的许可），title "RADAR Abdominal CT Demo"：https://huggingface.co/api/spaces/junma/RADAR-demo
- 语义很清楚：**这不是合作，是 Wang Lab 式的行为模式作用在 DAMO 的产物上**——别人放出权重，他 48 小时内包一个可点的 Gradio demo 出来。这恰恰是两个组最本质差别的活体标本：DAMO 出模型和临床数据，多伦多这边出**可用性、benchmark 和社区基础设施**。

### 4. 还有一条"竞争性"的技术连接值得注意
Wang Lab 2026 年 2 月新开了 **FastSegmentator**（https://github.com/bowang-lab/FastSegmentator ，创建 2026-02-24，最后推送 2026-07-22），README 自述是 nnU-Net 和 TotalSegmentator 的 GPU 全链路快速推理实现，宣称在 24 个 parity-validated 模式下复现官方 TotalSegmentator 输出（headline 模式 ≥0.999 DSC）并快 2–9×。也就是说：**RADAR 整条流水线最前端依赖的那个工具，Wang Lab 正在做它的加速替代品。** 这是两组目前唯一的技术正面接触点。

---

## 二、Bo Wang 本人

**履历**（本人主页 https://bowang87.github.io/ ）
- BSc 电子工程，华中科技大学（HUST），2010
- MSc 计算机科学，University of Toronto，2012
- PhD 计算机科学，Stanford University，2017，导师 **Serafim Batzoglou**（计算生物学，非影像）
- 工业界：Illumina、Genentech（主页只写"extensive industrial research experience"，未给年份）
- 博后：**没有**。从 Stanford 博士直接进工业界再回多大教职。

**现任职务（全部核实）**
| 职务 | 起始 | 来源 |
|---|---|---|
| Assistant Professor（tenure-track），UofT，Computer Science + Laboratory Medicine & Pathobiology 双聘；另在 Medical Biophysics 有 faculty listing | — | https://lmp.utoronto.ca/faculty/bo-wang 、https://medbio.utoronto.ca/faculty/wang |
| **Chief AI Scientist, University Health Network (UHN)** | 2023-09 公布，紧随 UHN AI Hub 同年成立 | https://web.cs.toronto.edu/news-events/news/bo-wang-appointed-chief-ai-scientist-at-university-health-network |
| Faculty Member + **Canada CIFAR AI Chair**, Vector Institute | — | https://vectorinstitute.ai/team/bo-wang/ |
| **Canada Research Chair (Tier 2) in Artificial Intelligence for Medicine**，CIHR 出资，2022-10-01 起 | 2022 | https://www.chairs-chaires.gc.ca/chairholders-titulaires/profile-eng.aspx?profileId=5693 |
| 首任 **Temerty Professor in AI Research and Education in Medicine** | — | https://tcairem.utoronto.ca/news/artificial-intelligence-researcher-bo-wang-announced-inaugural-temerty-professor-ai-research-0 |
| **Xaira Therapeutics：Head of Biomedical AI（2025-06 入职）→ Chief AI Scientist（2026-07 晋升）**，并被官方表述为 co-founder 级别贡献者 | 2025-06 / 2026-07 | https://www.biospace.com/business/secretive-ai-biotech-xaira-hires-top-ai-academic-to-take-his-work-to-the-next-level 、https://www.businesswire.com/news/home/20260706699581/en/ |

⚠️ **这是这份调查里最重要的战略事实**：Bo Wang 自 2025 年 6 月起已把重心移到 Xaira（10 亿美元级 AI 制药公司），2026 年 7 月晋升 Chief AI Scientist，负责 **X-Cell**（首个 virtual cell 模型）与 **X-Atlas/Pisces** 数据集。公开材料没有明说他是否放弃学术职位；反证是他仍在续存——EchoJEPA（2026-02）通讯作者署 `Bo.Wang@uhn.ca`，三个 affiliation（UHN / UofT / Vector）都还在。但**他的产出重心已经完全从医学影像漂移到细胞生物学**（见下文第六节）。

**研究版图**：不是影像实验室，是"计算生物学 + 医学 AI"实验室，影像只是其中一条线。CRC 的 chair 描述写的全是 single-cell multi-omics、隐私保护的多机构基因组学习，一个字没提影像。

**学术指标**（https://scholar.google.com/citations?user=37FDILIAAAAJ ）：总引 48,251，h-index 81，i10 205，2021 年后引用 44,491。
⚠️ 这个 profile 有明显的同名合并污染——条目里混进了 "Gemini 2.5"、"BLOOM 176B"、"InternVL" 这类几乎肯定不属于他的论文。**引用他的 h-index 时要打折**。可靠的自有代表作：MedSAM（Nat Commun 2024，4,818 引）、SNF（Nat Methods 2014，2,479 引）、scGPT（Nat Methods 2024，1,856 引）、U-Mamba（arXiv 2024，1,888 引）。

---

## 三、Jun Ma：这条线真正的主导者，且已经独立

**履历**
- PhD 数学，Nanjing University of Science and Technology (NJUST)
- 博后：University of Toronto / Wang Lab（2023 年的实验室页面上他是仅有的两名博后之一）
- **现职（已升为独立 PI）：Scientist, Princess Margaret Cancer Centre；Machine Learning Lead, UHN AI Hub**：https://www.uhnresearch.ca/researcher/jun-ma
- Scholar：总引 20,355，h=39，i10=70：https://scholar.google.com/citations?user=bW1UV4IAAAAJ

**他的实际主导程度：几乎是全部。** 证据链：
1. MedSAM（Nat Commun 2024）一作；MedSAM2（arXiv:2504.03600）共同一作（与 Harvard DBMI 的 Zongxin Yang 并列 ∗，Zongxin Yang 是 AOT/DeAOT 视频分割的作者——**MedSAM2 的视频能力来自哈佛那半边，不是多伦多**）。
2. U-Mamba 一作、SegLossOdyssey / SOTA-MedSeg / AbdomenCT-1K / COVID-19-CT-Seg-Benchmark 全是他个人账号下的项目：https://github.com/JunMa11
3. 他是 FLARE 系列挑战赛的主要组织者（FLARE21 511 例 → FLARE22 2,300 例 → FLARE23 4,500 例 → FLARE25/26），并主编 Springer LNCS 挑战赛论文集（Ma, Jun & Wang, Bo, 2022）：https://flare.grand-challenge.org/ 、https://conferences.miccai.org/2025/en/FLARE-2025-Challenge.html
4. **2025-05-26，他注册了自己的 GitHub 组织 `medfm-flare`，组织名 "FLARE Lab"，描述直书 "JunMa's Lab at University Health Network and University of Toronto"，blog 链接指向他自己的 Scholar**：https://github.com/medfm-flare （20 个仓库，2026-09 仍在高频推送）

**判断：影像这条线的智力与运营中心是 Jun Ma，Bo Wang 是资源与署名端。而这条线现在已经从 `bowang-lab` 迁到 `medfm-flare`。**

---

## 四、实验室规模、构成与经费

**规模（注意：这是可得的最新快照，已过时）**
- 实验室官网 **wanglab.ml 已死**：`dig @8.8.8.8 wanglab.ml` 无 A 记录、无 NS 记录（SERVFAIL）；`wanglab.ai` 现在是域名拍卖页。Wayback 最后一次成功抓取是 **2023-06-08**，之后无快照。
- 2023-06-08 的花名册（https://web.archive.org/web/20230608215426/https://www.wanglab.ml/people.html ）：PI 1 + 博后 2（Jun Ma、Nasim Abdollahi）+ PhD 13 + MSc 4 + BSc 1 + Research Associate 1 ≈ **22 人**。
- 构成偏向：13 个博士生里做影像的只有个位数，主流是代谢组学、单细胞、生物网络、隐私计算。**影像在这个组里从来是少数派。**
- GitHub 组织只有 8 个 public members（多数是 2023 年前的学生账号），不能当规模指标。

**经费（有据可查的）**
- MedSAM 论文致谢原文："supported by the **Natural Sciences and Engineering Research Council of Canada (NSERC, RGPIN-2020-06189 and DGECR-2020-00294)** and **CIFAR AI Chair** programs… computing resources provided by the **Digital Research Alliance of Canada**"：https://www.nature.com/articles/s41467-024-44824-z
- CRC Tier 2 由 **CIHR** 出资（2022-10 起）。
- Temerty Faculty of Medicine 的冠名教席（Temerty 捐赠）。
- 企业：**Xaira Therapeutics**（个人层面，非实验室 grant）。
- 注意组合特征：**算力靠国家级共享设施（Digital Research Alliance / Vector），不靠自建集群**——这直接决定了他们的产出形态（见下）。

---

## 五、产出模式：论文—代码—数据—竞赛是怎么组织的

这个组有一套非常清晰、可复制的流水线，和 DAMO 完全不同：

1. **"公开数据再标注 → 开源权重 → 抢名字"**。MedSAM 是第一个把 SAM 搬进医学影像并起了这个名字的；MedSAM2 同理。名字本身就是资产。
2. **挑战赛即生产线**。FLARE 一年一届，每年换任务（2021 快速低显存 → 2022 半监督 → 2023 pan-cancer → 2025 RECIST-to-3D / laptop seg / MLLM → 2026 MLLM-3D、AutoMSC）。挑战赛产出三样东西：一个公开数据集、一篇巨型合著论文、一批 baseline 仓库。典型如 *Efficient MedSAMs: Segment Anything in Medical Images on Laptop*（arXiv:2412.16085），**82 位作者**，Jun Ma 一作、Bo Wang 末位：https://arxiv.org/abs/2412.16085
3. **数据集当作独立发布物**。HuggingFace 上两个组织并行：
   - `wanglab`：CT_DeepLesion-MedSAM2（上月下载 12,737 次）、LLD-MMRI-MedSAM2、RVENet-MedSAM2、LUNA25-MedSAM2
   - `FLARE-MedFM`：PancancerCTSeg（上月 4,700 次下载，21 likes，最后更新 2026-09-15）、PancancerRECIST-to-3D、FLARE-AutoMSC、FLARE-MLLM-2D、FLARE26-MLLM-3D、FLARE-Task2-LaptopSeg 等 11 个
4. **star 分布极度头重脚轻**（bowang-lab 共 66 repos）：MedSAM 4,401 / scGPT 1,632 / MedRAX 1,231 / U-Mamba 1,000 / MedSAM2 721 / BioReason 404 / EchoJEPA 339 / ecg-fm 315 / MedSAMSlicer 302，**之后断崖到 143 及以下，一半以上仓库是个位数 star**。也就是说：这个组的影响力集中在 4–5 个"命名权项目"上，其余是论文附属物。
5. **可用性外包给社区**：3D Slicer 插件（MedSAMSlicer，302 star）、Colab、Gradio、HF Space——这也是为什么 Jun Ma 会顺手给 RADAR 做 demo。
6. **商业化实体**：实验室本身没有 spin-off；商业化发生在 **PI 个人层面**，且方向是生物制药（Xaira）而非影像。**影像线没有任何商业出口**——这与 DAMO（阿里内部产品化、与浙大一院深度绑定）形成根本对比。

---

## 六、医学影像数据从哪来 —— 这是与 DAMO 最本质的差别

**MedSAM / MedSAM2 线：100% 公开数据再加工，零医院数据。**
- MedSAM 的 Data availability 原文："The training and validating datasets used in this study are **available in the public domain**… We confirmed that **All the image datasets in this study are publicly accessible and permitted for research purposes.**"（https://www.nature.com/articles/s41467-024-44824-z ）
- MedSAM2 的标注对象：DeepLesion（NIH）、LLD-MMRI、RVENet、LUNA25、FLARE25 pan-cancer——全是公开数据集或挑战赛数据，README 明确要求引用原始数据论文：https://github.com/bowang-lab/MedSAM2
- 他们甚至维护了一个公开数据集索引站：https://medsam-datasetlist.github.io/
- 他们的"数据贡献"形式是**标注增量**（5,000 CT 病灶、3,984 肝 MRI 病灶、251,550 超声帧，human-in-the-loop，宣称省 85% 人工），而不是原始影像。

**UHN 临床数据确实在用，但只用于非影像/非公开发布的那条线，而且公开的永远是公开数据训的那个权重。** 最清楚的证据是 EchoJEPA（arXiv:2602.02603，2026-02）：
- 论文 4.1 节原文："**Toronto (Internal): N=150,000 studies** used for probe training and internal validation. **Chicago (Internal): N=60,000 studies** used as an external holdout site." 外加公开的 EchoNet-Dynamic / EchoNet-Pediatric。
- 但开源那句写的是："We **open-source EchoJEPA-L**… trained on **MIMIC-IV-Echo** (Gow et al., 2023)"。
- 合著者里有 UHN 的临床方：Wendy Tsang、Barry Rubin、River Jiang 等。
- ECG-FM 同构：公开 checkpoint 训练于 MIMIC-IV-ECG + PhysioNet 2021：https://github.com/bowang-lab/ecg-fm

**一句话对照：**
> DAMO RADAR = 一家医院（浙大一院）424,911 例增强腹部 CT + 1,500 万 image-text 对 → 权重以 CC BY-NC-SA 放出，数据不放。
> Wang Lab = 别人放出的公开数据 → 加标注、加 benchmark、加挑战赛、加可用界面 → 代码与权重全 Apache-2.0 放出。
> **前者的稀缺资源是数据与临床通道，后者的稀缺资源是社区基础设施与命名权。** 这也解释了为什么关系是单向的：Jun Ma 可以两天内消费 RADAR，DAMO 永远不需要消费 MedSAM。

---

## 七、2026 年 9 月现状：影像线在 bowang-lab 已经停了，但没有死，只是搬家了

**bowang-lab 组织按最后推送排序（2026-09-20 实测 GitHub API）**
| 仓库 | stars | 最后推送 | 方向 |
|---|---|---|---|
| CryoDINO | 0 | **2026-09-17** | Cryo-ET 自监督基础模型（3DINO/DINOv2 的 3D 版，36 万+ 3D patch，ViT-L） |
| genomic-FM | 32 | 2026-09-01 | 基因组基础模型 benchmark |
| dsh-medomni | 4 | 2026-08-28 | DeepSeek 医学影像插件 |
| BioReason-Pro | 125 | 2026-08-21 | 蛋白功能预测 |
| **FastSegmentator** | 5 | 2026-07-22 | nnU-Net/TotalSegmentator GPU 加速 |
| AGILE | 62 | 2026-07-18 | LNP/mRNA 递送 |
| EchoJEPA | 339 | 2026-06-18 | 超声心动基础模型 |
| BioReason | 404 | 2026-05-28 | DNA-LLM |
| scGPT | 1,632 | 2026-04-29 | 单细胞 |
| MedRAX2 | 26 | 2026-04-03 | 胸片 agent |
| ecg-fm | 315 | 2026-01-14 | ECG |
| **MedSAM2** | 721 | **2025-07-11** | — |
| **MedSAM** | 4,401 | **2025-05-07** | — |

**MedSAM 线是否还在维护：实质上没有。**
- MedSAM 最后推送 2025-05-07（14.5 个月前），17 个 open issues；MedSAM2 最后推送 2025-07-11，14 个 open issues。
- MedSAM2 的近期 issue **几乎全是 0 回复**：#45（2026-07-30，甚至是一个指出 RECIST z-slab 裁剪像素→切片换算反了的 bug 修复）0 comments、#44（2026-04-21）0、#43（2026-04-03）0、#42（2026-03-16）0、#40（2025-11-26）0。**连 bug 修复报告都没人接。**
- HF 上 `wanglab/MedSAM2` 月下载 78 次、46 likes，最后修改 2025-07-10。

**但影像并没有消失，它跟着 Jun Ma 走了**（`medfm-flare`，2026-09 仍在推）：
- `MedSAM2-RECIST`（MedSAM2 的 Docker 推理流水线，2026-08-18 仍在更新）
- `FLARE-Efficiency`（2026-09-14 新建）、`DRA-skills`（2026-09-18）、`AwesomeBiomedicalAI`（2026-09-19）
- HF 上 `FLARE-MedFM/PancancerCTSeg` 2026-09-15 更新、月下载 4,700

**MedSAM3 有没有公开迹象：Wang Lab 这边没有，而且名字已经被别人抢了。**
- `bowang-lab/MedSAM3` → **GitHub API 返回 404，不存在**。
- 已存在的 **MedSAM3 是另一个组的**：*MedSAM3: Delving into Segment Anything with Medical Concepts*，arXiv:2511.19046（v1 2025-11-24，v2 2026-09-14），作者 Anglin Liu, Xu R. Cao, Yifan Shen, Yi Lu, Xiang Li, Qianqian Chen, **Jintai Chen**，代码在 https://github.com/Joey-S-Liu/MedSAM3 （326 star，2026-09-14 推送）。基于 SAM 3 做文本提示分割 + MLLM agent。**Bo Wang / Jun Ma 均不在作者列。**
- GitHub 上名为 MedSAM3 的仓库共 17 个，除上述一个外全是个位数 star 的复现。

**给你的战略读数**：Wang Lab 在 2025–2026 完成了一次彻底的重心迁移——PI 去了 Xaira 做 virtual cell，组织产出转向 BioReason/scGPT/CryoDINO/genomic-FM 这条生物线；医学影像被"分拆"给了升格成独立 PI 的 Jun Ma（FLARE Lab @ UHN）。MedSAM 这个名字留在 bowang-lab 里当遗产（4.4k star 但 14 个月无人维护），而 MedSAM3 这个名字已经被第三方占走。**如果你要接触这条线，正确的对象是 Jun Ma 和 `medfm-flare`，不是 Bo Wang 和 `bowang-lab`。**

---

### 需要你知道的不确定性（未编造、但证据不足）
1. 实验室**当前**人数无法核实——官网域名已失效，最新快照停在 2023-06。22 人是 2023 年的数字。
2. Bo Wang 是否仍保有 UofT tenure-track 教职的**全职**身份，公开材料没有任何一处说明；只能确认 2026-02 的论文他仍署 UHN/UofT/Vector 且用 uhn.ca 邮箱。
3. Bo Wang 的 Google Scholar 存在同名合并污染，h=81 不可直接引用。
4. "Gairdner Early Career Researcher Award" 与 "Canada Research Chair Award" 两项荣誉仅见于 Vector 与 UofT 的自述页面，我没有找到独立的颁奖方公告。
5. NSERC/CIHR 的具体在研项目清单未逐条核实，只核实了 MedSAM 致谢中的两个 NSERC 编号与 CRC 的 CIHR 出资方。