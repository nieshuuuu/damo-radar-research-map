# DAMO RADAR ↔ MedSAM/MedSAM2：取证结论

## 一句话结论

**两边零互引、零互评。** RADAR 的参考文献里没有 SAM / MedSAM / MedSAM2 的任何一条；MedSAM 与 MedSAM2 也从未引用 RADAR（RADAR 2026-09-17 上线，至今被引 0）。唯一真实的连接是**三个共享的第三方节点**：DeepLesion、PANDA、以及浙江的一组肝病灶作者——全部是"共用数据/共引文献"，不是技术路线上的对话。

---

## 1. RADAR 正文参考文献：无 SAM / MedSAM / MedSAM2

通过 Crossref 取到 `10.1126/science.aec6129` 的完整正文参考文献表，**共 60 条**（52 条带 DOI + 8 条 unstructured），逐条解析后：

- 关键词 `segment anything` / `medsam` / `kirillov` / `sam2` 在 60 条里命中 **0 次**。
- 8 条无 DOI 的条目是：Shui et al. fVLM (ICLR 2025)、CLIP (Radford)、ViT (Dosovitskiy)、MedGemma (Sellergren)、Lingshu (LASA Team)、Qwen Technical Report、中国国家卫健委三级医院评审标准、以及自引的 Zenodo v3 存档。没有一条是 SAM 家族。
- 分割侧引用的是 **nnU-Net**（`10.1038/s41592-020-01008-z`）和 **TotalSegmentator**（Wasserthal et al., Radiology AI 2023, `10.1148/ryai.230024`）——与你背景里说的一致。

查询接口：`https://api.crossref.org/works/10.1126/science.aec6129`（`message.reference`），DOI 标题解析用 `https://api.openalex.org/works?filter=doi:...`。

代码侧同样无交集：
- RADAR README 的 Acknowledgements 只列 LAVIS / nnU-Net / MONAI / 3D-ResNets-PyTorch，无 SAM 系：https://github.com/alibaba-damo-academy/damo-radar
- `docs/PREPROCESS.md` 明确写死 **TotalSegmentator V1 (v1.5.7)** 生成 104 结构掩膜再并成 36 个主要解剖结构，重采样到 `[1,1,5]`：https://raw.githubusercontent.com/alibaba-damo-academy/damo-radar/main/docs/PREPROCESS.md
- 两个 Zenodo 存档（https://zenodo.org/records/21504519 v3 / https://zenodo.org/records/21271172 v2）的记录页均无 SAM/MedSAM 字样。

**限制声明**：Crossref 返回的是 Science 正文参考文献表。Supplementary Materials 若另有独立参考文献编号，因 Science 付费墙无法核验，我不替它下结论。

## 2. MedSAM / MedSAM2 参考文献：MedSAM 无，MedSAM2 有 DeepLesion 和 PANDA

**MedSAM (Nat Commun 2024, `10.1038/s41467-024-44824-z`)**：47 条参考文献，逐条看过——**没有** DeepLesion、**没有** PANDA、**没有**任何达摩院作品。它引的是 Meta 的 Segment Anything (Kirillov, ICCV 2023)、nnU-Net、一堆 "SAM 在医学图像上行不行" 的 2023 评测预印本。

**MedSAM2 (arXiv:2504.03600, 仅 v1, 2025-04-04)**：

- **DeepLesion 引的正是 Ke Yan 2018 那篇**。参考文献 [42] 原文："K. Yan, X. Wang, L. Lu, and R. M. Summers, *Deeplesion: automated mining of large-scale lesion annotations and universal lesion detection with deep learning*, Journal of Medical Imaging, vol. 5, no. 3, pp. 036501, 2018."（全文 https://arxiv.org/html/2504.03600v1）。README 还额外要求使用者单独引用原始 DeepLesion 论文，给的是 `https://doi.org/10.1117/1.JMI.5.3.036501`：https://github.com/bowang-lab/MedSAM2 。正文里 DeepLesion 出现三次，全是"我们用它做 5000 例 CT 病灶的 human-in-the-loop 标注"，纯数据来源，无技术评价。
- **PANDA 被引了，而且引的是达摩院那篇**。参考文献 [3] = "K. Cao, Y. Xia, J. Yao, X. Han, L. Lambert, T. Zhang, W. Tang, G. Jin, H. Jiang, X. Fang et al., *Large-scale pancreatic cancer detection via non-contrast CT and deep learning*, Nature Medicine, vol. 29, no. 12, pp. 3033–3043, 2023."（`10.1038/s41591-023-02640-w`）。
- 这条引用的分量比表面大：该文作者名单里同时有 **Ling Zhang (Alibaba Group)**、**Le Lu (Alibaba Group US)**、**Qi Zhang (浙大一院)**、**Tingbo Liang (浙大一院)**——即 RADAR 的 AI 侧资深作者、第一作者、末位通讯，四个人全在。核验：`https://api.openalex.org/works/doi:10.1038/s41591-023-02640-w`。
- 但**引用方式是纯礼节性的**：[3] 在正文只出现两次，一次是 introduction 开头列举应用场景（"treatment monitoring [3]"），一次是说 3D nnU-Net 被广泛用于 "pancreas cancer and abdominal organ segmentation in CT scans [3][10]"。没有比较、没有讨论、没有基线复现。
- MedSAM2 参考文献里**没有**其他达摩院作品（通过 Semantic Scholar `graph/v1/paper/arXiv:2504.03600/references` 拉全表逐条核对）。

## 3. 互相正面评价或批评对方技术路线：没有，一次都没有

- RADAR 侧：不可能有，它压根没引 SAM 家族任何一篇。RADAR 的对标对象是 **Merlin**（`10.1038/s41586-026-10181-8`）、**CT-CLIP/CT-RATE**（`10.1038/s41551-025-01599-y`）、**fVLM**、**MedGemma**、**Lingshu**——全是 vision-language / report-generation 路线，不是 promptable segmentation 路线。两边在做不同的事：RADAR 输出征象概率，MedSAM2 输出掩膜。
- MedSAM2 侧：对 PANDA 的两次引用都是背景陈述，没有一句评价。
- 反向补一个检查：达摩院医学 AI 核心作者是否引过 MedSAM？OpenAlex 交叉查询 `cites:W4391109864` × 作者 ID，结果是 **Ling Zhang 0 篇、Yingda Xia 0 篇、Le Lu 1 篇**。那 1 篇是 Zig-RiR (IEEE TMI 2025, `10.1109/TMI.2025.3561797`)，Le Lu (Alibaba Group US) 挂末位作者，属于 USTC 主导的合作论文，不是 RADAR 团队作品。

## 4. 第三方把两者放在一起比较：目前不存在

- **RADAR 被引 0**。OpenAlex `https://api.openalex.org/works?filter=cites:W7213447220` → `count: 0`；Semantic Scholar `DOI:10.1126/science.aec6129` → `citationCount: 0, referenceCount: 0`（S2 还没抓参考文献）。论文 2026-09-17 上线，距今 3 天，不存在任何 benchmark 或综述把 RADAR 和 MedSAM2 放一起。
- 退一步查"同时引 MedSAM2 和 PANDA"的论文：**只有 1 篇**——*Opportunistic Promptable Segmentation: Leveraging Routine Radiological Annotations to Guide 3D CT Lesion Segmentation*, `10.1007/s10278-026-02097-6` (2026)。
- "同时引 MedSAM 和 PANDA"的有 **17 篇**，主要是综述和数据集论文，例如 AbdomenAtlas (`10.1016/j.media.2024.103285`)、*A generalist foundation model and database for open-world medical image segmentation* (`10.1038/s41551-025-01497-3`)、*Foundation Model for Advancing Healthcare* (`10.1109/RBME.2024.3496744`)。这些是把"达摩院的诊断模型"和"Wang Lab 的分割模型"当作同一张 foundation model 地图上的两个点列举，不是对比评测。

---

## 额外发现（你的背景里没有，但改变解读）

**第三个共享节点：浙江的肝病灶作者群。** RADAR 引了 *A multicenter clinical AI system study for detection and diagnosis of focal liver lesions*, Nat Commun 2024, `10.1038/s41467-024-45325-9`，第一作者 **Hanning Ying（邵逸夫医院 / 浙江大学）**。而 MedSAM2 的肝脏 MRI 病灶数据集 **LLD-MMRI** 来自参考文献 [43] SDR-Former (`10.1016/j.neunet.2025.107228`)，第二作者同样是 **Hanning Ying（邵逸夫医院）**。注意：邵逸夫医院不是梁廷波的浙大一院，是浙大另一家附属医院——所以这是"同校不同院"的弱连接，不要写成直接关系。

**"SAM" 同名陷阱，写东西时务必避开。** 达摩院自己有一个叫 SAM 的东西，比 Meta 的早一年：Ke Yan et al., *SAM: Self-Supervised Learning of Pixel-Wise Anatomical Embeddings in Radiological Images*, IEEE TMI 2022, `10.1109/TMI.2022.3169003`（第一作者 Ke Yan，Alibaba Group）。这个 SAM = Self-supervised Anatomical eMbedding，和 Segment Anything Model 毫无关系。任何声称"达摩院做过 SAM"的说法都要先确认指的是哪一个。

**Ke Yan / Le Lu 的路径确认**：DeepLesion 2018 出自 NIH Clinical Center（论文共同作者 Ronald M. Summers 即该实验室 PI，见 MedSAM2 参考文献 [42] 原文作者列），二人现均在达摩院——Le Lu 的 Alibaba Group (US) 归属在 PANDA 的 OpenAlex 记录里可直接读到；Ke Yan 为 Alibaba DAMO Academy Staff Algorithm Engineer（https://www.alphaxiv.org/@ke-yan ，https://scholar.google.com/citations?user=TVGx4KgAAAAJ ）。

---

## 综合判断

RADAR 与 MedSAM/MedSAM2 是**两条互不相交的路线**，共享的只有 DeepLesion 这类公共数据遗产和 PANDA 这类被顺手引用的里程碑。你原先设想的"间接连接"（DeepLesion → Ke Yan/Le Lu → 达摩院）在文献层面是**单向的、且反向的**：是多伦多的 MedSAM2 在用达摩院两位核心人物早年在 NIH 留下的数据，而不是达摩院在用 Wang Lab 的东西。达摩院侧对 SAM 生态的引用近乎为零——RADAR 的分割预处理宁可用 2022 年的 TotalSegmentator v1.5.7，也没碰 MedSAM。

主要证据文件（本地缓存）：
- `/private/tmp/claude-501/-Users-shunie-Developer/152a37b5-0538-44e5-b0f8-ccce9c6bab33/scratchpad/radar_cr.json` — RADAR Crossref 完整元数据含 60 条参考文献
- `/private/tmp/claude-501/-Users-shunie-Developer/152a37b5-0538-44e5-b0f8-ccce9c6bab33/scratchpad/medsam2_refs.json` — MedSAM2 Semantic Scholar 参考文献全表
- `/private/tmp/claude-501/-Users-shunie-Developer/152a37b5-0538-44e5-b0f8-ccce9c6bab33/scratchpad/ms2full.txt` — MedSAM2 arXiv v1 全文纯文本
- `/private/tmp/claude-501/-Users-shunie-Developer/152a37b5-0538-44e5-b0f8-ccce9c6bab33/scratchpad/radar_readme.md`、`pre.md`、`ms2_readme.md` — 两边 GitHub 文档