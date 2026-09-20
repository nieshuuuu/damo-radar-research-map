## 结论（一句话）

**Wang Lab（Bo Wang / Jun Ma, Toronto）与 DAMO/NIH-Summers 阵营（Le Lu、Ling Zhang、Ke Yan、Yingda Xia、Jiawen Yao、Ronald M. Summers、Holger Roth、Xiaosong Wang、Adam Harrison）之间：没有任何一篇直接共同署名的论文。唯一穿透两边的人是 Alan Yuille（Johns Hopkins），他同时直接合著过两边——但他本人不属于达摩院也不属于 NIH，所以这是"二度连接"，不是直接共同作者。**

分项裁决：
| 问题 | 裁决 |
|---|---|
| 1. 直接共同作者（除 Yuille 外的 9 人） | **没有**（零篇） |
| 1'. 与 Alan Yuille | **有，且很强**（Bo Wang 6 篇，Jun Ma 2 篇） |
| 2. 共同白皮书 / 综述 / 共识 / 挑战赛 | **有但很弱**：同一本编著书的不同章节；同一篇挑战赛报告里一方是 organizer、另一方是 participant——从无同篇共同署名 |
| 3. MICCAI/MIDL 程序委员会、编委会 | **未发现交集**（Le Lu 与 Summers 在 MICCAI 任职，Bo Wang/Jun Ma 未出现；部分编委会名单无法访问，故为"未发现证据"而非"证明不存在"） |

---

## 1. 直接共同作者：逐人排查

**方法**：用 OpenAlex 把这 10 个人的**全部作品**（Le Lu 542 篇、Ling Zhang 413、Summers 790、Yuille 1103、Xiaosong Wang 256、Jiawen Yao 143、Adam Harrison 118、Holger Roth 276、Ke Yan 75、Yingda Xia 77）逐篇拉下来，对作者字符串做宽松匹配（`^B\w*\s+Wang$` / `^J\w*\s+Ma$`）。这种做法绕开了 OpenAlex 对 "Bo Wang" 的作者消歧失败问题（见第 5 节）。反向再用 Bo Wang 和 Jun Ma 各自 ORCID 认领的作品清单核对一遍。

结果：

| 对象 | 与 Bo Wang / Jun Ma 共同署名 |
|---|---|
| Le Lu (A5045227579) | 0（只有一条书籍 front-matter 伪记录，见第 3 节） |
| Ling Zhang (A5038765418) | 0 |
| Ke Yan (A5101967245) | 0 |
| Yingda Xia (A5075005282) | 0 |
| Jiawen Yao (A5075245264) | 0 |
| Ronald M. Summers (A5016047550) | 0 |
| Holger R. Roth (A5043710204) | 0 |
| Xiaosong Wang (A5100724911) | 0 |
| Adam P. Harrison (A5058215578) | 0（同上，只有 front-matter） |
| **Alan Yuille (A5086706224)** | **8 篇（见下）** |

反向确认：Bo Wang 的 ORCID 作品（103 条，89 条有 DOI）和 Jun Ma 的 ORCID 作品（67 条，42 条有 DOI）逐篇扫 co-author 的 raw affiliation，**没有出现任何 Alibaba / DAMO / NIH Clinical Center 的署名单位**。

API 入口（可复现）：
- `https://api.openalex.org/works?filter=authorships.author.id:A5045227579&per-page=200`（换 ID 即可）
- `https://pub.orcid.org/v3.0/0000-0002-9620-3413/works`（Bo Wang）
- `https://pub.orcid.org/v3.0/0000-0002-9739-0855/works`（Jun Ma）

---

## 2. 唯一的真桥：Alan Yuille

**Bo Wang ↔ Alan Yuille（6 篇，2017–2020，纯 computer vision）**，且这 6 篇全部在 Bo Wang 本人的 ORCID `0000-0002-9620-3413` 里被亲自认领——这是身份归属的决定性证据：

- Gradually Updated Neural Networks for Large-Scale Image Recognition — https://doi.org/10.48550/arXiv.1711.09280（Bo Wang 署 Stanford University）
- Single-Shot Object Detection with Enriched Semantics, CVPR 2018 — https://doi.org/10.1109/CVPR.2018.00609
- Deep Regression Forests for Age Estimation, CVPR 2018 — https://doi.org/10.1109/CVPR.2018.00245（署 Hikvision Research）
- Deep Co-Training for Semi-Supervised Image Recognition, ECCV 2018 — https://doi.org/10.1007/978-3-030-01267-0_9（署 Hikvision Research Institute, Hangzhou）
- Deep Differentiable Random Forests for Age Estimation, IEEE TPAMI 2019 — https://doi.org/10.1109/TPAMI.2019.2937294（**Bo Wang 署 "Vector Institute, Peter Munk Cardiac Center of University Health Network, Toronto"** — 直接锁死是多伦多这位）
- Robust Face Detection via Learning Small Faces on Hard Images, WACV 2020 — https://doi.org/10.1109/WACV45572.2020.9093445

署名轨迹 Stanford → Hikvision → Vector/UHN 与 Bo Wang 的履历完全吻合（Stanford CS PhD 2012–2017，见 https://bowang87.github.io/ ；UHN/Vector/UofT 自 2018-11 起，见 ORCID employments）。

**Jun Ma ↔ Alan Yuille（2 篇）**：

- MedShapeNet – a large-scale dataset of 3D medical shapes for computer vision, *Biomed Eng / Biomed Tech* 2024 — https://doi.org/10.1515/bmt-2024-0396 。157 位作者。Jun Ma 的 raw affiliation 是 "Department of Laboratory Medicine and Pathobiology, University of Toronto / Peter Munk Cardiac Centre, UHN / Vector Institute"，Yuille 是 "Department of Computer Science, Johns Hopkins University"。同篇还有 Zongwei Zhou、Chongyu Qu、Tiezheng Zhang、Wenxuan Li（均 JHU）。**这是一篇 dataset white paper，也就是你问的"共同白皮书"在 Yuille 这条线上是成立的。**
- PANORAMA 挑战赛报告，*Lancet Oncology* 2025 — https://doi.org/10.1016/S1470-2045(25)00567-4 。144 位作者。Yuille 署 JHU；参赛队一栏出现 "Ching-Yuan Yu, **Jun Ma**, Tianhao Fu, **Bo Wang**"。

**而 Yuille 与达摩院那边是硬合著**：Large-scale pancreatic cancer detection via non-contrast CT and deep learning, *Nature Medicine* 2023 — https://doi.org/10.1038/s41591-023-02640-w ，作者含 Yingda Xia、Jiawen Yao、Alan Yuille、Le Lu、Ling Zhang。该文也正是 DAMO RADAR 的参考文献之一。

所以最短路径是：**Bo Wang / Jun Ma —— Alan Yuille —— Le Lu / Ling Zhang / Yingda Xia / Jiawen Yao**，长度 2。

---

## 3. 两个必须排除的假阳性（否则会得出错误结论）

**(a) Jun Ma × Le Lu, CVIU 2013 —— 不是同一个 Jun Ma。**
Semantic Scholar 的 author id 2143854906（"Jun Ma"）里挂着 "Hierarchical segmentation and identification of thoracic vertebra using learning-based edge detection and coarse-to-fine deformable model", *Computer Vision and Image Understanding* 2013, https://doi.org/10.1016/j.cviu.2012.11.016 ，作者 Jun Ma + Le Lu。查原始 affiliation：**两人都署 "Siemens Corporate Research, 755 College Road East, Princeton, NJ"**。Wang Lab 的 Jun Ma 的 ORCID 记录显示他 2021-11 才进 University of Toronto（`https://pub.orcid.org/v3.0/0000-0002-9739-0855/educations`），2013 年不可能在 Siemens Princeton。**同名不同人。** OpenAlex 把这篇的 Jun Ma 分到了另一个 ID（A5100643093, 显示为 "Ma Jun"），是对的。

**(b) "List of contributors", https://doi.org/10.1016/b978-0-12-821259-2.00035-1 —— 是书籍 front matter，不是论文。**
这条记录在 OpenAlex 里把 Bo Wang、Le Lu、Adam P. Harrison 并列为"共同作者"，纯属元数据假象。查原书（Crossref, ISBN 9780128212592，*Artificial Intelligence in Medicine*, Elsevier/Academic Press 2021，共 35 条记录）可以看到他们写的是**不同章节**：
- 第 14 章 "Artificial intelligence in radiology" — https://doi.org/10.1016/b978-0-12-821259-2.00014-4 — Dakai Jin, **Adam P. Harrison, Ling Zhang, Ke Yan**, Yirui Wang, Jinzheng Cai, Shun Miao, **Le Lu**（PAII/达摩院系）
- 第 7 章 "Analytics methods and tools for integration of biomedical data in medicine" — https://doi.org/10.1016/b978-0-12-821259-2.00007-7 — Lin Zhang, Mehran Karimzadeh, Mattea Welch, Chris McIntosh, **Bo Wang**（合著者 Chris McIntosh = UHN，Mehran Karimzadeh = Wang Lab，可确认就是多伦多的 Bo Wang）

**裁决：同书不同章，是"共处一本编著"，不是共同作者。这是两阵营唯一一次出现在同一个出版物容器里（Yuille 线之外）。属于"有但很弱"。**

---

## 4. 白皮书 / 综述 / 共识文件 / 挑战赛

逐篇核对大型多作者文件的完整作者表（OpenAlex + Crossref）：

| 文件 | Wang Lab 侧 | DAMO/NIH 侧 | 同篇共存？ |
|---|---|---|---|
| Metrics reloaded, *Nat Methods* 2024, https://doi.org/10.1038/s41592-023-02151-z (73 作者) | — | **Ronald M. Summers** | 否 |
| Understanding metric-related pitfalls, *Nat Methods* 2024, https://doi.org/10.1038/s41592-023-02150-0 (70 作者) | — | **Ronald M. Summers** | 否 |
| Why is the Winner the Best?, CVPR 2023, https://doi.org/10.1109/CVPR52729.2023.01911 (125 作者) | — | — | 否 |
| Biomedical image analysis competitions: state of current participation practice, https://doi.org/10.48550/arXiv.2212.08568 (356 作者) | **Jun Ma** | — | 否 |
| The Medical Segmentation Decathlon, *Nat Commun* 2022, https://doi.org/10.1038/s41467-022-30695-9 (58 作者) | — | **Summers, Yingda Xia** | 否 |
| The Liver Tumor Segmentation Benchmark (LiTS), *MedIA* 2022, https://doi.org/10.1016/j.media.2022.102680 (109 作者) | **Jun Ma** | —（只有 NVIDIA 的 Daguang Xu） | 否 |
| Touchstone Benchmark, https://doi.org/10.48550/arXiv.2411.03670 (53 作者) | — | **Holger R. Roth, Alan Yuille** | 否 |
| AbdomenAtlas, *MedIA* 2024, https://doi.org/10.1016/j.media.2024.103285 | — | **Alan Yuille** | 否 |
| FLARE22, https://doi.org/10.48550/arXiv.2308.05862 (29 作者) | **Jun Ma（一作/组织者）, Bo Wang（末位）** | — | 否 |
| FLARE23, https://doi.org/10.48550/arXiv.2408.12534 (10 作者) | **Jun Ma, Bo Wang** | — | 否 |
| **MedShapeNet**, https://doi.org/10.1515/bmt-2024-0396 (157 作者) | **Jun Ma** | **Alan Yuille**（+ JHU 的 Zongwei Zhou 等） | **是**（仅 Yuille 线） |
| **PANORAMA**, https://doi.org/10.1016/S1470-2045(25)00567-4 (144 作者) | **Jun Ma, Bo Wang, Tianhao Fu**（参赛队） | **Alan Yuille**（作者） | **是**（仅 Yuille 线） |

一个清晰的模式：**FLARE 系列由 Wang Lab 组织，DAMO 不参与；MSD / Metrics Reloaded / Touchstone 这条 Maier-Hein–Summers–Roth 共识链里没有 Wang Lab。两条 challenge/consensus 生态基本不相交。**

---

## 5. 委员会 / 编委会层面

可验证到的：
- **Le Lu**：自述 "I currently lead the global Medical AI R&D efforts for DAMO Academy, Alibaba Group"；**Associate Editor, IEEE TPAMI** 及 IEEE Signal Processing Letters；**Elected Board Member, MICCAI Society, 2021**；**Industry Co-chair, MICCAI 2022**；Area Chair: CVPR 2021/2022, MICCAI 2021, AAAI 2021/2022, ICIP 2021。来源：https://lelu007.github.io/
- **MICCAI 2023 Organizing Committee**（https://conferences.miccai.org/2023/en/ORGANIZING-COMMITTEE.html）：Industrial Sponsorships = **Le Lu**, Mohammad Yaqub, Yanwu Xu；Publications Chairs = **Ron Summers**, Kevin Zhou。**Bo Wang、Jun Ma、Ling Zhang、Ke Yan、Yuille、Roth 均不在该名单。**
- **Bo Wang**：Canada CIFAR AI Chair @ Vector Institute；Assistant Professor, UofT（Medical Biophysics / LMP / CS）；个人主页与机构页（https://bowang87.github.io/ 、https://vectorinstitute.ai/team/bo-wang/ 、https://medbio.utoronto.ca/faculty/wang ）**未列任何 MICCAI/MIDL chair 或期刊编委职务**。

**限制（必须声明）**：Medical Image Analysis 的 ScienceDirect editorial board 页返回 HTTP 403，无法核；MICCAI/MIDL 的 Area Chair、reviewer 名册并非年年完整公开。因此第 3 问的答案严格说是"**在可公开核查的名单里未发现交集**"，不是"证明不存在"。

---

## 6. 回到 RADAR ↔ MedSAM 本身：作品层面也没有关系

- **RADAR 不引用 MedSAM。** *Science* 2026, https://doi.org/10.1126/science.aec6129 的 49 条参考文献（OpenAlex `referenced_works` 全量展开）里没有 MedSAM、MedSAM2 或 SAM 系列。它引的是 TotalSegmentator（https://doi.org/10.1148/ryai.230024 系）、nnU-Net、PANDA（Nat Med 2023）、PANORAMA（Lancet Oncol 2025）、以及 **Summers 2016 "Progress in Fully Automated Abdominal CT Interpretation"** —— 这是 RADAR 与 NIH-Summers 之间唯一的、且仅是引用层面的联系。
- **MedSAM 不引用 DAMO 的工作。** *Nat Commun* 2024, https://doi.org/10.1038/s41467-024-44824-z 的 40 条参考文献里，与目标名单相关的只有 MSD（Summers, Yingda Xia 在作者表里）和 Metrics Reloaded（Summers）——即引的是"共识/基准"文献，不是达摩院的模型工作。
- **RADAR 作者表里没有 Wang Lab 任何人。** PubMed 42752131 的 40 位作者：Zhang Q, Zhang J, Cao W, Lu Z, Chang W, Ding H, Chen C, Li Z, Xue X, Wang S, Zhang S, Xie Y, Xia Y, Wu Q, Shui Z, Li X, Zheng Z, Zhou Y, Mok TCW, Xia Y, Wang H, Ye X, Ma T, Peng J, Wang X, Ding J, Gao Y, Ye H, Liu Y, Chen D, Ni Z, Ning J, Zhang W, Liu J, Yu C, Ju S, Zhang J, Xiao W, **Zhang L**（Ling Zhang）, **Liang T**（梁廷波）。**注意：Le Lu 不在 RADAR 作者表上。**
- **MedSAM2 作者表 9 人**（https://arxiv.org/abs/2504.03600 ，2025-04-04 提交）：Jun Ma, Zongxin Yang, Sumin Kim, Bihui Chen, Mohammed Baharoon, Adibvafa Fallahpour, Reza Asakereh, Hongwei Lyu, Bo Wang。**没有任何达摩院/NIH 的人。**

所以你已知的那条间接连接（MedSAM2 的 CT_DeepLesion 建在 NIH DeepLesion 上，而 DeepLesion 的 Ke Yan、Xiaosong Wang、Le Lu、Summers 出自 NIH Clinical Center，前三人后来去了工业界/达摩院）**目前仍然是两者之间唯一实质性的链接，而且它是"数据继承"而非"人的合作"**。DeepLesion 原文作者表可核：https://doi.org/10.1117/1.JMI.5.3.036501 （Ke Yan, Xiaosong Wang, Le Lu, Ronald M. Summers，均署 NIH Clinical Center）。

---

## 7. 方法与局限

- 用了三个 API：**OpenAlex**（主力，全量作品遍历 + 宽松姓名匹配，绕开作者消歧失败）、**ORCID Public API**（身份锚定与本人认领作品）、**Semantic Scholar Graph API**（交叉验证，它恰好暴露了 Siemens 的那个同名 Jun Ma）、外加 **PubMed eutils** 和 **Crossref**（书籍章节归属、原始 affiliation）。
- **OpenAlex 对 "Bo Wang" 的消歧是坏的**：ID `A5100408160` 是一个 1084 篇的合并怪物（挂着哈尔滨理工、北川医学院、Florida Tech、CIFAR 等一堆无关单位），但它的 ORCID 锚 `0000-0002-9620-3413` 是多伦多这位。因此本次所有结论都不依赖该 ID 的作品集合，而是依赖"从对方 542/790/1103 篇里反向找名字"+"ORCID 本人认领"两条独立路径。
- **Semantic Scholar 对 Bo Wang 的 profile 是碎片化的**（id 2153215904 只有 10 篇），所以 S2 的"0 命中"单独不足以下结论，只作为交叉验证。
- 未覆盖：FLARE Challenge Consortium 的完整成员名单（只在 PDF 附录里），以及未公开的审稿人/AC 名册。若要把第 2、3 问做到"证明不存在"级别，需要人工读 FLARE22/23 附录和逐年 MICCAI LNCS 前言的 Program Committee 名单。

Sources: [Le Lu homepage](https://lelu007.github.io/), [MICCAI 2023 Organizing Committee](https://conferences.miccai.org/2023/en/ORGANIZING-COMMITTEE.html), [Bo Wang homepage](https://bowang87.github.io/), [Bo Wang – Vector Institute](https://vectorinstitute.ai/team/bo-wang/), [Bo Wang – UofT Medical Biophysics](https://medbio.utoronto.ca/faculty/wang), [MedSAM2 arXiv](https://arxiv.org/abs/2504.03600)