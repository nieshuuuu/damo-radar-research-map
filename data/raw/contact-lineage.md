## DeepLesion 数据谱系核实

### 1. NIH DeepLesion 原始出处

全部核实无误，并补一个漏掉的数字。

| 项 | 核实结果 |
|---|---|
| 作者顺序 | Ke Yan → Xiaosong Wang → Le Lu → Ronald M. Summers（4 人，顺序与你给的一致） |
| 隶属 | Yan / Wang / Summers = NIH Clinical Center, **Imaging Biomarkers and Computer-Aided Diagnosis Laboratory**；Le Lu = NIH Clinical Center, **Clinical Image Processing Service, Radiology and Imaging Sciences** |
| 期刊 | *J Med Imaging* (Bellingham) **5(3):036501**，电子出版 **2018-07-20**，PMID 30035154 |
| 规模 | **32,735 lesions / 32,120 CT slices / 10,594 studies / 4,427 unique patients** — 你给的三个数字都对，但漏了病灶数 32,735（≠32,120，一张切片可含多个病灶） |
| 标注 | 从本院 PACS 的 radiologist **bookmarks** 挖掘而来的 RECIST 标记（长径 + 垂直短径），**2D、仅在最大径切片上**，转成 2D bounding box。无逐像素 mask |
| 许可 | 无正式许可证。NIH Box 直接下载、不需申请表 <https://nihcc.app.box.com/v/DeepLesion>，二手来源称使用不受限、只要求引用 JMI 论文。⚠️ NIH 官方新闻稿页返回 403，我没能一手读到原始 terms，这一条按"二手"看待 |

来源：<https://pubmed.ncbi.nlm.nih.gov/30035154/>、<https://www.spiedigitallibrary.org/journals/journal-of-medical-imaging/volume-5/issue-03/036501/DeepLesion--automated-mining-of-large-scale-lesion-annotations-and/10.1117/1.JMI.5.3.036501.full>

注意一个结构性事实：DeepLesion 的 CT **来自 NIH Clinical Center 自家 PACS**，不是多中心汇总。它是一个单中心数据集。

### 2. CT_DeepLesion-MedSAM2：他们做了什么

<https://huggingface.co/datasets/wanglab/CT_DeepLesion-MedSAM2>（最后更新 2025-08-21，12,737 次下载，53.4 GB）

- **规模**：元数据覆盖全部 32,735 个病灶；**新增的 3D mask 只有 5,000 个**。不是把 32,735 个全做了。
- **方法**（arXiv:2504.03600 正文）：人在回路、三轮迭代。① 标注者在最大径切片画 2D bbox → ② MedSAM2 出该层 2D mask → ③ 人工修正并指定病灶的上下界 slice → ④ 模型向体数据两端**双向传播** → ⑤ 人工复核。每轮用新标注微调模型，单病灶标注耗时从 **525.9 s 降到 74.3 s**。
- **许可**：⚠️ **HF 上根本没有 license 字段**。我查了 HF API，`cardData` 只有 `language / tags / size_categories`，没有 license。README 只要求同时引用 DeepLesion 原文和 MedSAM2。对照组：同系列 `wanglab/LUNA25-MedSAM2` 明确标了 `cc-by-nc-4.0`，`CT_DeepLesion-MedSAM2` 是空的 —— 大概率是因为上游 DeepLesion 本身没有许可证可继承。

**顺带修正你背景里的一条**：MedSAM2「代码与权重都是 Apache-2.0」不准确。GitHub repo 是 Apache-2.0（<https://github.com/bowang-lab/MedSAM2>，最后 push 2025-07-11 确认），但 HF 权重 `wanglab/MedSAM2` 声明的是 **cc-by-sa-4.0**，arXiv 论文本身是 CC BY-NC-ND 4.0。三者不一致。

### 3. RADAR 是否用过 DeepLesion —— 关键否证点

**公开可查的一切证据都是"没有"。**

我把 `alibaba-damo-academy/damo-radar` 整仓 clone 下来（669 MB），对全仓（排除 .git）grep：

```
deeplesion | deep lesion | " nih " | medsam | segment anything | ke yan | le lu
→ 0 命中
```

同时 grep `amos|flare|abdomenct|abdomenatlas|btcv|lits|kits|msd|decathlon|chaos|ct-rate` 也全是误命中（`train_splits` 之类）。

RADAR 公开的数据栈只有三样：
1. **RAD-CT**（内部，424,911 例增强腹部 CT + 15M anatomy-wise image–text pairs，未公开）
2. **Stanford MERLIN**（外部测试，5,137 例，zero-shot AUC 0.883 / 21 findings；也用于 RADAR+ 的 from-scratch 训练与 fine-tune）
3. **TotalSegmentator v1.5.7**（生成 104 结构 mask → 映射到 36 个主要结构 → 重采样到 spacing [1,1,5]）

来源：<https://github.com/alibaba-damo-academy/damo-radar/blob/main/docs/PREPROCESS.md>、`docs/TRAINING.md`、`docs/INFERENCE.md`；论文摘要 <https://pubmed.ncbi.nlm.nih.gov/42752131/>（Science 393(6817):eaec6129，在线 2026-09-17，40 位作者）

**诚实的边界**：Science 正文和 supplementary 在付费墙后（science.org 返回 403），Semantic Scholar 的 references 字段被出版商屏蔽（`"data": null`），所以我**没能读到 Data Availability 全文和参考文献表**。准确的结论是：*在 RADAR 公开的全部代码与数据文档里，DeepLesion 和任何 NIH 公开数据都不存在*；我不能断言论文正文连引用都没有。

**反向的一个有意思的事实**：DAMO 自己发布了 `radar-generalist/RADAR-auxiliary-data`（<https://huggingface.co/datasets/radar-generalist/RADAR-auxiliary-data>，CC BY-NC-SA 4.0），内容是**基于 Stanford Merlin 训练集跑 TotalSegmentator 得到的预处理解剖 mask**。也就是说 DAMO 对公开数据的派生贡献是向 Stanford 那条线，不是向 NIH 那条线。

### 4. MERLIN 是什么

- **论文**：*Merlin: a computed tomography vision–language foundation model and dataset*，**Nature 652(8112):1318–1328**，在线 2026-03-04，PMID 41781626，doi 10.1038/s41586-026-10181-8。预印本 arXiv:2406.06512（2024-06-10）。
- **谁发布**：Stanford。一作 Louis Blankemeier（Stanford EE），末位通讯 **Akshay S. Chaudhari**（Stanford AIMI），40 位作者，含 Curtis Langlotz、Sergios Gatidis。<https://www.nature.com/articles/s41586-026-10181-8>、<https://github.com/StanfordMIMI/Merlin>
- **模型训练数据**：15,331 例 CT（>600 万张 2D 图像）+ >180 万条 ICD 诊断码 + >600 万 token 报告。
- **公开的数据集**：**25,494 对 腹部 CT + 放射报告**（论文内部数字 25,528 scans / 18,321 patients，PHI 人工复核后放出 25,494），2012-12 至 2018-10 Stanford 医院急诊的腹盆 CT，每次检查取切片数最多的 DICOM series 转 NIfTI 并去标识。
- **许可**：**Stanford AIMI 非商业研究数据使用协议**，需在下载页签 DUA、审批后给 Azure Blob 链接。不是 CC 类开放许可。<https://stanfordaimi.azurewebsites.net/datasets/60b9c7ff-877b-48ce-96c3-0194c8205c40>
- **它和上面两条线有关系吗**：**没有**。Merlin 是完全独立的第三条线（Stanford AIMI / Langlotz–Chaudhari 生态），与 NIH Summers 实验室无人员重叠，与 Toronto Wang Lab 也无人员重叠。RADAR 用它纯粹是"拿现成的西方人群公开基准做外部验证"。

（顺带：Chaudhari 是你之前 scouting 过的 PI，评分 5.5。这条线的末端落在他手上。）

### 5. 达摩院有没有发布过公开数据集

查了 HF 两个 org：

- `Alibaba-DAMO-Academy` 的 datasets：`RynnEC-Bench`、`PixelRefer-TrainingData`、`RynnBrain-Bench`、`ClinHallu`、`InterVBench`、`ClinFusion-Eval-Data` —— **没有一个是 3D CT 影像/分割数据集**。
- `radar-generalist`：仅 `RADAR`（权重）+ `RADAR-auxiliary-data`（Merlin 的 TotalSegmentator mask）。

DAMO 的旗舰医学影像数据一律未公开：RAD-CT 的 424,911 例没公开，PANDA（Nature Medicine 2023 非增强 CT 胰腺癌筛查）的数据也没公开。他们开源的是模型和代码，不是数据。

反方向查 Wang Lab 用过的数据（<https://github.com/bowang-lab/MedSAM2> README）：DeepLesion、LUNA25、LLD-MMRI、RVENet、FLARE25 pan-cancer（`FLARE-MedFM/FLARE-Task1-PancancerRECIST-to-3D`，而 FLARE 系列挑战赛本身就是 Jun Ma 组织的）。**没有任何一个来自 DAMO。**

**结论：两个方向的数据交集都是空集。**

### 6. 最终判断：三条通路各自多强

**「RADAR 和 MedSAM 通过人而非数据相连」—— 这个说法半对，但表述需要修正。**

**(a) 数据：明确不成立。强度 ≈ 0。**
RADAR 的训练/测试/预处理栈里没有 DeepLesion、没有任何 NIH 公开数据（整仓 grep 零命中）。RADAR 用 Stanford Merlin，MedSAM2 用 NIH DeepLesion + LUNA25 + LLD-MMRI + RVENet + FLARE。**交集为空集**。这个否证点是干净的。

**(b) 人：成立，但是两跳，且不对称。强度：中等偏弱。**

三条硬事实：
1. DeepLesion 一作 **Ke Yan 现在 DAMO Academy / Hupan Lab**（ICCV 2023 Alice 论文署名，<https://github.com/alibaba-damo-academy/alice>）
2. DeepLesion 三作 **Le Lu 2021-08 至 2025-06 领导 DAMO 全球医疗 AI 研发，2025-06 转去 Ant Group**（同一 Alice 论文署名 DAMO；<https://www.cs.jhu.edu/~lelu/>）
3. ⭐ 更硬的一条，你背景里没提到：**RADAR 的 AI 侧资深作者 Ling Zhang（第 39 位，DAMO Academy, Washington DC）本人就是 NIH Clinical Center 出身的 visiting fellow**，与 **Le Lu、Ronald M. Summers 直接共同发表**（*Personalized Pancreatic Tumor Growth Prediction via Group Learning*, MICCAI 2017, <https://arxiv.org/abs/1706.00493>，单位 = Imaging Biomarkers and CAD Laboratory + Clinical Image Processing Service, NIH CC —— 就是 DeepLesion 的那两个科室）。

但关键的负面事实：**Ke Yan 和 Le Lu 都不在 RADAR 的 40 人作者名单里**（我逐条核对了 PubMed 全名单和 GitHub BibTeX）。所以是"同机构的前辈/同事 + 同一实验室谱系的师承"，不是"同一篇论文的合作者"。

而另一端更弱：**MedSAM2 团队（Bo Wang、Jun Ma @ Toronto/Vector）与 NIH Summers 实验室没有任何人员重叠**。他们只是下载了公开数据。

所以这条链的真实拓扑是：

```
RADAR ──人(DAMO/NIH 谱系)── DeepLesion ──数据(公开下载)── MedSAM2
```

**中间那一跳是数据，不是人。**「通过人相连」只覆盖了链条的左半段。准确的一句话应该是：**两条线共享的既不是人也不是数据，而是 NIH DeepLesion 这份遗产在两个方向上的分岔——DAMO 继承了做那件事的人，Wang Lab 继承了那批数据。**

**(c) 基础设施：最实在，但也最不具区分度。强度：中等。**
RADAR 依赖 **nnU-Net + MONAI**（THIRD_PARTY_LICENSES 明列，另有 LAVIS BSD-3、3D-ResNets MIT），全部解剖 mask 来自 **TotalSegmentator v1.5.7**。MedSAM2 的骨干是 Meta **SAM 2.1 hiera-tiny**，不是 nnU-Net —— 两者**不在同一条代码路径上**。它们共享的是 nnU-Net/MONAI/挑战赛这个圈层生态，而这个生态几乎覆盖了所有 3D 医学影像组，所以它解释不了任何特定的"关系"。

**一句话结论**：RADAR 与 MedSAM2 是两个互不相干的技术谱系（vision-language 诊断 vs. 可提示分割），唯一可验证的桥是 DeepLesion，而这座桥的两端性质不同——DAMO 那端是人的流动，Wang Lab 那端是数据的公开下载。把它说成"通过人相连"会高估 DAMO 与 Wang Lab 之间的关系：**这两个组之间既没有共同作者，也没有共用数据，也没有共用模型血统。**