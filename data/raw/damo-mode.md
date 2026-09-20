# 达摩院医疗 AI 与 Wang Lab 的结构对比（含 RADAR ↔ MedSAM 关系核查）

## 0. 先回答"DAMO RADAR 和 MedSAM 之间到底是什么关系"

**结论：没有直接的技术继承或人员关系。两者在三个层面上有间接接触，其中两条我能给出证据，一条不成立。**

| 连接 | 是否成立 | 证据 |
|---|---|---|
| RADAR 用了 MedSAM/MedSAM2 | **不成立** | RADAR 仓库 README 的 Acknowledgements 只列 LAVIS / nnU-Net / MONAI / 3D-ResNets-PyTorch；分割预处理用 TotalSegmentator（HuggingFace 的 `RADAR-auxiliary-data` 卡片明确写"automatic segmentation via TotalSegmentator，把 104 个标签合并成 36 个"）。https://github.com/alibaba-damo-academy/damo-radar ; https://huggingface.co/datasets/radar-generalist/RADAR-auxiliary-data |
| 达摩院有一个**直接对标 MedSAM 的产品**：CT-SAM3D | **成立** | CT-SAM3D（AAAI 2025 / arXiv 2403.15063，作者 Heng Guo, …, Ke Yan, Le Lu, Dakai Jin, Minfeng Xu）在论文正文中把 MedSAM 当作基线逐条比较：FLARE22 上 5 次点击时 MedSAM 平均 DSC 72.2% / NSD 68.2%，CT-SAM3D 88.4% / 95.8%，并指出 MedSAM "starts to degrade when N>3"。https://arxiv.org/html/2403.15063v2 ; https://github.com/alibaba-damo-academy/ct-sam3d ; https://ojs.aaai.org/index.php/AAAI/article/view/32335 |
| 两边在 **FLARE 挑战赛**上有共同署名 | **成立（但弱）** | FLARE 是 Jun Ma + Bo Wang 组织的（FLARE22 总结论文一作 Jun Ma、末作 Bo Wang，University Health Network / U Toronto / Vector Institute，Lancet Digit Health 2024, PMID 39455194, doi:10.1016/S2589-7500(24)00154-7）。"DAMO Academy" 出现在该论文的机构列表里（通过第 28 位的协作组作者，不是具名作者）；而 FLARE 2022 获奖名单上有 **DAMO MIA**（阿里达摩院），提交物是 `Med_Query`。https://flare22.grand-challenge.org/awards/ ; https://github.com/alibaba-damo-academy/Med_Query |
| 数据血缘：DeepLesion → MedSAM2 的 CT 病灶数据集 | 你给的前提我核实了一半 | Ke Yan 在 NIH 由 Le Lu 和 Ronald Summers 指导做 DeepLesion，2019–2021 在 PAII，现为达摩院 Staff Algorithm Engineer；Le Lu 2018-06 至 2021-07 领导 PAII Bethesda Research Lab，**2021 年 8 月起**负责达摩院全球医疗 AI 研发。https://yanke23.com/ ; https://lelu007.github.io/ |

**所以最准确的说法是：MedSAM/MedSAM2 的对手不是 RADAR，而是 CT-SAM3D。** RADAR 和 MedSAM2 根本不在一个任务层：RADAR 是"报告级诊断"（读报告学到 146 个征象的概率），MedSAM2 是"提示式分割"（给点/框，出 mask）。RADAR 把分割当作**上游预处理**（TotalSegmentator v1.5.7），而它的上游本来就可以是 CT-SAM3D 那一类模型——达摩院自己造了这一层，但在 RADAR 里没用自己的，用了公开的 TotalSegmentator。

值得注意的一点：**Le Lu 不在 RADAR 的作者名单上**（40 位作者，末两位是 Ling Zhang @ DAMO Washington DC 和梁廷波 @ 浙大一院）。CT-SAM3D 那条线（Le Lu / Ke Yan / Dakai Jin，美东）和 RADAR 那条线（杭州 + 浙大）在达摩院内部是两支不同的队伍。

---

## 1. 完整论文/产品年表（影像方向，2021→2026）

我用 Europe PMC 对 `AFF:"DAMO Academy"` 做了全量检索（80 条命中），下面是影像相关的主线。

| 年 | 期刊/会议 | 工作 | 数据规模 | 临床伙伴 |
|---|---|---|---|---|
| 2021-08 | — | Le Lu 出任达摩院全球医疗 AI 负责人 | — | https://lelu007.github.io/ |
| 2022 | **Nature Communications** | 头颈部肿瘤 OAR 自动勾画，多机构 | 多中心 | PMID 36253346 |
| 2022 | MICCAI FLARE22 | **DAMO MIA 获奖**（Med_Query） | 2300 CT | https://flare22.grand-challenge.org/awards/ |
| 2023-11 | **Nature Medicine** | **PANDA**（胰腺癌，平扫 CT） | 训练 3,208 例单中心；10 中心 6,239 例验证；真实世界 20,530 连续病例 | 上海长海/胰腺疾病研究所、浙大一院、盛京医院、复旦肿瘤、新华、天津肿瘤、中山肿瘤、广东省人民、林口长庚、布拉格总医院 — PMID 37985692 |
| 2023 | Annals of Surgery | 胰腺癌术后总生存预测 | — | PMID 35781511 |
| 2024 | **Lancet Digital Health** | FLARE22 挑战赛总结（达摩院在协作组内） | 2300 CT / 50+ 研究组 | PMID 39455194 |
| 2024 | arXiv → **AAAI 2025** | **CT-SAM3D**（3D 可提示分割） | 1,204 CT / 107 解剖结构（TotalSeg++） | arXiv 2403.15063 |
| 2025-06 | **Nature Medicine** | **GRAPE**（胃癌，平扫 CT） | 开发 2 中心 3,470 GC + 3,250 非 GC；外部 16 中心 18,160 例；真实世界 78,593 连续扫描 | 浙江省肿瘤医院（主导）+ 宁波、温州、丽水、湖州、安徽、辽宁、福建等 20 余家 — PMID 40555751, NCT06614179 |
| 2025-08 | **Nature Medicine** | **iAorta**（急性主动脉综合征，平扫 CT） | 回顾 20,750；真实世界 **137,525**；前瞻 13,846 | 上海长海、浙大一院、山东省立、南京鼓楼、淳安县二院 — PMID 40835970 |
| 2026-04 | **Annals of Oncology** | **COCA**（结直肠癌，平扫 CT） | 开发 1,321 CRC + 1,357 对照；6 中心 2,053 验证；真实世界 27,433 | 广东省人民、广东省中医院、四川省肿瘤、Charles University（布拉格）×3 — PMID 42025761 |
| 2026 | **Nature Medicine** | **LiON**（肝脏恶性病变，增强 CT）+ 单臂试验 | 训练 6,443；验证 22,251；单臂试验 10,333 | 浙大一院、盛京、上海长海、湖北省肿瘤、成都六院、CUHK、法国 Nice — PMID 42618635，通讯 Ke Yan + Ling Zhang |
| 2026 | Radiology | DeepENE：喉/下咽癌结外侵犯 | — | PMID 41528225 |
| 2026 | Nature Communications | 多模态脂肪肝机会性筛查/分期 | — | PMID 41672973 |
| **2026-09** | **Science** | **RADAR** | **400,000+ 增强腹部 CT，1,500 万解剖级图文对**；内部 ~39,000 例，8 家外部医院 | 浙大一院（主导）+ 嘉兴、宁波二院、安吉、嵊州、海宁、景宁、绩溪、余杭、北仑、新疆兵团一师医院 — PMID 42752131, doi:10.1126/science.aec6129 |

产品侧另有已对外宣传但我**未找到对应同行评议论文**的 EAGLE（食管癌）；动脉网口径称食管癌验证近 10 万例、肝癌 7.5 万例。https://www.vbdata.cn/1519067973

**年表读出来的模式**：2021–2023 是"单癌种 + 顶刊 + 闭源"；2024–2025 每年一到两篇 Nature Medicine，癌种横向铺开（胰→胃→主动脉→结直肠→肝）；2026 年 RADAR 是路线的**转向点**——从"每个病一个监督模型"跳到"读报告自监督的通用 VLM"，并且第一次开源。

---

## 2. 数据来源模式

**核心机制：医院是共同作者，不是数据供应商。**

- 每篇论文的通讯作者里必有一位临床方。PANDA 是上海长海 + 浙大一院（梁廷波）；GRAPE 是浙江省肿瘤医院（程向东、徐志远）；RADAR 是浙大一院（梁廷波）。达摩院方永远是 Ling Zhang（Washington DC）或 Ke Yan。
- **伦理路径统一**：回顾性收集，各院 IRB 批准 + 知情同意豁免，数据去标识后再训练。PANDA 原文列了 10 家 IRB 的全名。PMID 37985692（Ethics approval 节）
- **没有公开的合作协议文本**。能查到的"共建"是两类：
  - **署名层面的共建**：`Hupan Laboratory, Hangzhou` 与 `DAMO Academy, Alibaba Group` 在 PANDA / GRAPE / RADAR 上并列署名；杭州本地媒体直接写"湖畔实验室（达摩院）"。https://ori.hangzhou.com.cn/ornews/content/2026-09/19/content_9311231.htm
  - **公益项目层面**：2024-02 阿里"医疗AI多癌早筛公益项目"在浙江丽水落地，部署在丽水市中心医院和景宁县人民医院。https://www.qbitai.com/2024/03/124490.html ; https://www.nbd.com.cn/articles/2024-02-23/3254118.html
- **临床试验注册**：GRAPE 注册了 NCT06614179；另有 NCT06638866（胰腺癌机会性筛查）、NCT07066983/NCT07067983（GRAPE 临床评估）。这说明他们在把"回顾性论文"推成"前瞻性注册研究"，这是 Wang Lab 完全没有的一条轨道。
- **地理特征**：RADAR 的外部医院是安吉、嵊州、海宁、景宁、绩溪、北仑、新疆兵团一师——**县级医院为主**。这不是找不到大医院，而是刻意的：产品定位是"基层也能用的机会性筛查"。

---

## 3. 开源模式：Apache-2.0 代码 + CC BY-NC-SA 权重**不是惯例，是 2026 年才出现的新做法**

这一点你的前提需要修正。真实情况是：

**（a）临床旗舰模型，一直是彻底闭源，而且写明是专利原因。**

- PANDA（Nat Med 2023）Code availability 原文："The code used for the implementation of PANDA has dependencies on internal tooling and infrastructure, is under patent protection (application numbers: **CN 202210575258.9, US 18046405**), and thus is not able to be publicly released." Data availability："The remaining datasets used in this study are currently not permitted for public release by the respective institutional review boards."（只给了一个在线 demo：http://panda.medofmind.com/）PMID 37985692
- GRAPE（Nat Med 2025）几乎逐字相同的措辞，专利号 **CN116188392**；数据"not publicly available due to restrictions imposed by the respective IRBs"，且申请访问仅限 "noncommercial academic purposes only"。PMID 40555751

**（b）RADAR 是第一个破例：代码 Apache-2.0，权重 CC BY-NC-SA 4.0。**
仓库 LICENSE 是 Apache-2.0，HuggingFace 上 `radar-generalist/RADAR`（模型）和 `radar-generalist/RADAR-auxiliary-data`（数据）都是 CC BY-NC-SA 4.0，代码另存 Zenodo（https://zenodo.org/records/21271172）。https://github.com/alibaba-damo-academy/damo-radar ; https://huggingface.co/radar-generalist

**（c）研究型模型早就开源，而且更宽松。** CT-SAM3D 是 Apache-2.0，**权重也是 Apache-2.0**（托管在 ModelScope），比 RADAR 宽松。https://github.com/alibaba-damo-academy/ct-sam3d

**（d）有没有发布过公开数据集？有，但从不是自己医院的病人数据。** 三类：

1. **对公开数据的再标注**：`TotalSegPlusPlus`（TotalSegmentator 增强版，107 个解剖结构，加了骨骼肌/内脏脂肪/皮下脂肪，标注体素从 37% 提到 ~83%），ModelScope `xiuan123/TotalSegPlusPlus`。
2. **对公开数据的派生掩膜**：`RADAR-auxiliary-data` = 给 Stanford 的 **Merlin** 腹部 CT 训练集跑 TotalSegmentator 得到的 36 结构掩膜（NIfTI，1×1×5 mm），用户得自己去下 Merlin 原图。
3. **合成/文本数据**：`lingshu-medical-mllm/ReasonMed`（370K 多智能体生成的医学推理数据，Apache-2.0）、`lingshu_training_data_medical_domain`（MIT）。https://huggingface.co/datasets/lingshu-medical-mllm/ReasonMed

**一句话总结开源策略**：能被专利和 IRB 圈住的（临床模型 + 真实病人 CT）绝不放；不能被圈住的（方法论模型、在公开数据上的再标注、合成文本）大方放，而且放得比 MedSAM2 还多样。RADAR 的 CC BY-NC-SA 正是这条线的边界——**代码给你，权重不许商用**，因为商用归达医智影。

---

## 4. 商业化路径

- **FDA**：2025-04-17，DAMO PANDA 获 FDA "Breakthrough Device Designation"，报道称是中国科技企业医疗 AI 首次。https://www.targetedonc.com/view/ai-tool-earns-fda-breakthrough-device-designation-in-pancreatic-cancer ; https://tech.cnr.cn/techph/20250417/t20250417_527138301.shtml
- **NMPA**：尚**未**取得三类证。2026 年 2 月，"胰腺病变CT图像辅助分诊软件"（申请人：**阿里巴巴达摩院（北京）科技有限公司**）公示进入创新医疗器械特别审查程序（创新通道，2026 年第 4 号）。https://www.vbdata.cn/1519067973 ; https://news.yaozh.com/archive/47409.html
- **产品载体**：达医智影（damomed.com），官网口径"对接 30+ 家国内外医疗影像信息化厂商，为 1500+ 医疗机构提供技术支持"。https://damomed.com/en/about
- **筛查体量（口径互相冲突，按时间列）**：
  - 2023-11 雷峰网：阿里云开放 API，医院/体检场景**调用超 50 万次**。https://m.leiphone.com/category/healthai/47g0E0X1dLSmTkJP.html
  - 2024-06 Alizila（阿里官方媒体）：在中国**超过 600 万人次**筛查。https://www.alizila.com/damo-academy-ai-for-good-cancer-who-healthcare-2024/
  - 2025-03 报道：宁波大学附属人民医院完成 **4 万余人**筛查，查出 2 例常规未发现的早期胰腺癌（其中一例病灶仅 1.5 cm）。https://news.qq.com/rain/a/20250417A0827P00
  - 2026 动脉网：累计**5000 万人次**，覆盖 **10 个国家和地区**。https://www.vbdata.cn/1519067973
  - ⚠️ 600 万（2024）→ 5000 万（2026）这个跳跃我无法独立证实，后者是行业媒体转述，请按"厂商口径"对待。
- **渠道合作**：体检（美年大健康）、设备厂商（GE 医疗"一扫多查"集成）、保险/医药探索中。https://www.vbdata.cn/1519067973
- **国际**：2024 年 5 月与 **WHO Collaborating Center on Digital Health** 签署合作（西太平洋区首例），在新加坡、沙特等试点；另与巴基斯坦政府合作。https://www.bworldonline.com/health/2024/06/06/600289/who-damo-academy-partnership-to-further-medical-ai/ ; https://www.vbdata.cn/1519067973

---

## 5. 团队规模与构成

**具体人数我查不到公开披露——不编。** 能确证的结构性事实：

- **负责人**：吕乐（Le Lu），JHU 计算机博士 2007，2021 IEEE Fellow，2018-06–2021-07 领导 PAII Bethesda Research Lab，**2021-08 起**负责达摩院全球医疗 AI 研发。https://lelu007.github.io/ ; https://m.leiphone.com/category/healthai/47g0E0X1dLSmTkJP.html
- **美国侧**：论文署名出现过三个地点——`DAMO Academy, Alibaba Group, New York, NY, USA`（PANDA 2023、iAorta 2025）、`Washington, DC, USA`（GRAPE 2025、COCA 2026、LiON 2026、RADAR 2026）。Ling Zhang 的通讯地址从 New York 迁到 Washington DC，说明美东团队有过一次搬迁/重组。
- **中国侧**：`DAMO Academy, Alibaba Group, Hangzhou` + `Hupan Laboratory, Hangzhou`。RADAR 的多位达摩院作者同时挂 **College of Computer Science and Technology, Zhejiang University**（张建鹏、曹伟伟、周彦杰等），这就是你问的**双聘结构的实证**——不是行政文件，而是署名上的三重挂靠（DAMO + 湖畔 + 浙大计算机学院）。PMID 42752131
- **关键人**：Ling Zhang（浙大 2013 博士 → Iowa 博后 → NIH → NVIDIA → PAII → DAMO USA，多癌早筛技术负责人）https://fabiozhang0722.github.io/ ；Dakai Jin（Iowa 2016 博士 → NIH → PAII → 2021 DAMO，tech lead，MICCAI 2025/2026 Area Chair）https://dakjin.github.io/ ；Ke Yan（DeepLesion 一作，LiON 通讯）https://yanke23.com/ ；Minfeng Xu（徐敏丰，CT-SAM3D 与 iAorta 通讯 eric.xmf@alibaba-inc.com）。
- **人才管线**：DAMO 有独立的博士后单元，目标三年招募/培养 100+ 博士后（非医疗专属）。https://www.scmp.com/tech/big-tech/article/3245763/
- ⚠️ 百度百科英文版称达摩院医疗 AI 起于 2016 年、由时任 iDST 副总裁华先胜带队；达医智影官网写"Medical AI Team ... since 2017"。两者都不是一手来源，仅供参考。https://baike.baidu.com/en/item/Damo%20Academy/653561 ; https://damomed.com/en/about

---

## 6. 与竞赛生态的关系

**达摩院是"参赛并拿奖"型，不是"办赛发数据"型。**

- **FLARE 2022**：DAMO MIA 在获奖名单上（提交 Med_Query + Docker + Springer 论文）。https://flare22.grand-challenge.org/awards/
- **Learn2Reg 2023**：ThoraxCBCT 赛道第一名（Dakai Jin 主页自述）。https://dakjin.github.io/
- **基准数据集的合著者**：VerSe 椎体分割基准（Med Image Anal 2021, PMID 34340104）、ATM'22 气道树建模基准（Med Image Anal 2023, PMID 37716199）——他们参与别人的 benchmark，但主办方是别人。
- **不办赛的反证**：SegRap 2023 的组织者是 UESTC + 上海 AI Lab + 四川省肿瘤医院，**没有达摩院**。https://segrap2023.grand-challenge.org/organizers/ FLARE 系列的主办方是 Jun Ma / Bo Wang。https://github.com/JunMa11/FLARE
- **社区职务走的是"评审/AC"路线**：Dakai Jin 是 MICCAI 2025/2026 Area Chair、AAAI SPC；Ling Zhang 是 TMI/MedIA 审稿人。

我**没有找到**任何由达摩院主办的 MICCAI 或 grand-challenge 挑战赛。

---

## 结构对比：达摩院 vs Wang Lab

| 维度 | Alibaba DAMO Academy Medical AI | Wang Lab (Bo Wang, UofT/Vector/UHN) |
|---|---|---|
| **产出的终点** | 顶刊临床验证论文 + 注册器械（FDA breakthrough、NMPA 创新通道） | 开源模型 + 社区基准 + 挑战赛（MedSAM/MedSAM2 代码与权重均 Apache-2.0） |
| **数据获取** | 医院作为共同作者，IRB 豁免知情同意，回顾性队列 3k–78k 例，数据**永不公开** | 聚合已有公开数据集（DeepLesion 等）重新标注后**公开发布** |
| **开源边界** | 专利先行，临床模型闭源；方法论模型与派生标注开源；RADAR 首次"代码 Apache + 权重 NC" | 代码与权重同为 Apache-2.0，商用无限制 |
| **数据集贡献** | 只发布对公开数据的**再标注/派生掩膜**（TotalSeg++、RADAR-auxiliary-data）和合成文本（ReasonMed） | 发布可直接使用的**整编数据集**（CT_DeepLesion-MedSAM2 等）并主办 FLARE |
| **竞赛角色** | 参赛者（FLARE22 获奖、Learn2Reg 2023 第一） | 主办者（FLARE 2021–2025，总结发 Lancet Digit Health） |
| **地理与建制** | 杭州（+ 湖畔实验室 + 浙大计算机学院三重挂靠）+ 美东（NY→DC）；靠县级医院铺量 | 多伦多单点，学术建制 |
| **收入模型** | 达医智影产品化，1500+ 机构，体检/设备厂商/保险渠道 | 学术资助，模型免费 |
| **最近一次战略转向** | 2026 RADAR：从单病监督 → 读报告自监督通用 VLM，并首次开源 | 2025 MedSAM2 后仓库最后 push 2025-07-11 |

**最值得注意的一条**：达摩院和 Wang Lab 生产的其实是**互补品而不是替代品**——Wang Lab 生产"任何人都能拿去用的通用分割底座"，达摩院生产"在特定医院队列上被临床验证过、并走监管流程的诊断系统"。RADAR 用 TotalSegmentator 而不是自家 CT-SAM3D，恰恰说明在他们的价值链里，分割是可替换的商品层，值钱的是报告监督信号和 40 万例增强 CT——而那 40 万例，谁都拿不到。

---

### 未能证实 / 需要注意的缺口

1. 达摩院医疗 AI 团队的**人数**没有任何公开披露；中美两地人员配比只能从署名反推。
2. "5000 万筛查人次""10 个国家和地区"仅见于行业媒体转述（动脉网），无一手来源；与 2024 年阿里官方口径的 600 万差两个量级。
3. EAGLE（食管癌）有产品宣传但我未找到对应的同行评议论文。
4. 我未能验证 MedSAM2 论文是否反向引用 CT-SAM3D（arXiv HTML 版不可用）；只证实了 CT-SAM3D → MedSAM 这一个方向。
5. 湖畔实验室的法律实体性质（"浙江省数据科学与应用实验室"这一说法）只见于二手英文报道，我不采信为事实，只采信论文署名 `Hupan Laboratory, Hangzhou, China`。