## 结论先行

**是的 —— MICCAI/FLARE 挑战赛是这两条路线唯一有文献可证的实际接触面，而且接触发生在 FLARE 2022，不是现在。** 但这个接触面比"两边碰面"要弱：它是**单向的、历史的、人员层面的**，不是机构层面的持续合作。RADAR 论文本身对 Wang Lab 的工作引用为零。

---

## 1. FLARE 系列：确实是 Jun Ma + Bo Wang 的场子

组织者稳定为 **Jun Ma**（postdoc）与 **Bo Wang**（associate professor），University of Toronto / University Health Network / Vector Institute。
https://conferences.miccai.org/2025/en/FLARE-2025-Challenge.html

| 届次 | 任务 | 规模 | 论文 |
|---|---|---|---|
| FLARE21 | Fast & Low-GPU-memory 腹部器官分割 | 511 CT | Ma et al., *Medical Image Analysis* 2022, DOI 10.1016/j.media.2022.102616 |
| FLARE22 | 半监督（50 labeled + 2000 unlabeled），13 器官 | 2300 CT，>50 medical groups | *Lancet Digital Health* 6(11):e815, 2024, DOI 10.1016/S2589-7500(24)00154-7；preprint https://arxiv.org/abs/2308.05862 |
| FLARE23 | 首个 organ + pan-cancer 联合 | 4650 CT，>40 中心 | https://arxiv.org/abs/2408.12534 |
| FLARE24 | Pan-cancer（Codabench） | >10000 CT | https://www.codabench.org/competitions/2319/ |
| FLARE25 | 六个子任务：pan-cancer、laptop 端、MRI/PET UDA、3D foundation model、multimodal VLM、agentic | — | https://conferences.miccai.org/2025/en/FLARE-2025-Challenge.html |

**FLARE 2025 Task 1 = Pan-cancer RECIST-to-3D**，MedSAM2 仓库 2025-07-05 发布了官方 baseline：

```
- 20250705: Release Efficient MedSAM2 baseline for FLARE 2025 Pan-cancer
  segmentation challenge [RECIST-to-3D]
```
https://github.com/bowang-lab/MedSAM2（README 第 36 行）

数据集 https://huggingface.co/datasets/FLARE-MedFM/FLARE-Task1-PancancerRECIST-to-3D，npz 里带 `recist`（tumor 中层的二值 RECIST 标记），推理时当作 box prompt。样例文件名是 `CT_Lesion_FLARE23Ts_0057.npz` —— FLARE23 的测试集病灶被继承进来了。

**这里是第一个真正的交汇点**：FLARE25 pan-cancer 训练数据的来源清单里同时包含 **DeepLesion** 和 **AbdomenCT-1K**（https://huggingface.co/datasets/FLARE-MedFM/PancancerCTSeg）。也就是说 Ke Yan / Le Lu 在 NIH 时期做的 DeepLesion，同时是 MedSAM2 的 `CT_DeepLesion-MedSAM2` 的底座，也是 FLARE25 RECIST-to-3D 的底座 —— 而 RECIST 标注本来就是 DeepLesion 的原生标注形式。这不是巧合，是同一份遗产的两个下游。

---

## 2. 达摩院确实参加过 FLARE —— FLARE 2022，队名 `damomia`

这是最硬的一条证据。FLARE22 awards 页面列出 10 支获奖队伍，其中一支：

```
Docker: docker pull miccaiflare/damomia
Paper: https://link.springer.com/chapter/10.1007/978-3-031-23911-3_4
Code:  https://github.com/alibaba-damo-academy/Med_Query
```
https://flare22.grand-challenge.org/awards/

- 论文：*Semi-supervised Detection, Identification and Segmentation for Abdominal Organs*，作者 **Mingze Sun, Yankai Jiang, Heng Guo**（DOI 10.1007/978-3-031-23911-3_4）
- 提交的代码库是 **Med-Query**，其论文作者为 **Heng Guo, Jianfeng Zhang, Ke Yan, Le Lu, Minfeng Xu**（https://arxiv.org/abs/2212.02014）—— 正是 DeepLesion 的 Ke Yan 和 Le Lu

FLARE22 最终的 *Lancet Digital Health* 论文作者名单里包含 **Heng Guo** 和 **Mingze Sun**（Crossref 作者表，DOI 10.1016/S2589-7500(24)00154-7）。**所以达摩院的人和 Jun Ma、Bo Wang 是同一篇挑战赛论文的共同作者。** 这是两边唯一的直接共同署名。

补充两点须诚实标注：
- 有二手来源称该文 Declaration of interests 写着 "MS is employed by Alibaba Damo Academy"，我**未能直接核实**（Lancet 站点返回 403）。Europe PMC 记录中 Sun M 的署名单位是 Tsinghua-Berkeley Shenzhen Institute。
- Yankai Jiang 当时是达摩院 intern（Zhejiang University），现在在 Shanghai AI Laboratory。

**另一条：达摩院用 FLARE 的数据。** Alice（ICCV 2023，Yankai Jiang 等）的预训练数据就是 FLARE 2022 的 2000 张无标注 CT：
```
The following datasets were used for pre-training (2,000 unlabeled CT scans) in our paper.
- Fast and Low-resource semi-supervised Abdominal oRgan sEgmentation in CT (FLARE 2022)
```
https://github.com/alibaba-damo-academy/alice

Med-Query 论文正文也直接在 **FLARE22 validation leaderboard** 上报结果，并与 TotalSegmentator、nnU-Net、Swin UNETR 对比。

**FLARE23 / 24 / 25 没有找到达摩院队伍。** FLARE23 前五名是 aladdin5、citi、blackbean、hmi306、hanglok（arXiv:2408.12534 正文），无达摩院。

**LiTS 2018**：阿里官方博客称在 lesion segmentation 与 tumor burden 两项上取得当时最好成绩（https://www.alibabacloud.com/blog/594631）。但 LiTS benchmark 正式论文（https://arxiv.org/abs/1901.04056）全文检索不到 "Alibaba" 或 "DAMO" —— 那是 codalab live leaderboard 上的成绩，不在挑战赛论文的参赛者名单内。

---

## 3. 其他挑战赛：两边基本都不在场

| 挑战赛 | 组织方 | Wang Lab | DAMO |
|---|---|---|---|
| **AMOS 2022** | SRIBD / CUHK-SZ / SYSU / HKU（Yuanfeng Ji, Ruimao Zhang, Ping Luo, Xiang Wan）https://amos22.grand-challenge.org/Organizers/ | 否 | 否 |
| **KiTS21** | Heller, Isensee 等（arXiv:2307.01984） | 否 | 否 |
| **LiTS** | TUM / Tel Aviv / MICCAI Society | 否 | 见上（仅 leaderboard） |
| **MSD** | Antonelli, Reinke, Summers 等（arXiv:2106.05735） | 否 | 否 |
| **ULS23** | Radboudumc（基于 DeepLesion 743 lesions）https://uls23.grand-challenge.org/ | 否 | 否 |
| **MELA 2022** | M3DV（SJTU 线），非达摩院 | 否 | 否 |
| **TriALS 2024/25** | HKUST + Ain Shams + SYSU（arXiv:2605.16572）| 否 | 否 |

另外：**达摩院自己没有组织过任何 MICCAI registered challenge**（核对 https://miccai.org/index.php/special-interest-groups/challenges/miccai-registered-challenges/ 全表，无 Alibaba / DAMO 条目）。他们是参赛者和数据下游用户，不是主办方。Le Lu 是 MICCAI Society board member，Dakai Jin 做 MICCAI area chair，但这是学会治理，不是挑战赛组织。

---

## 4. AbdomenCT-1K 是 Jun Ma 做的，但**不是 Wang Lab 的**

这一点值得修正一个常见误解。

- 作者：**Jun Ma**（一作）, Yao Zhang, Song Gu, ..., Jian He, **Xiaoping Yang**（末位）。**Bo Wang 不在作者列表里。** Crossref DOI 10.1109/TPAMI.2021.3100536；preprint https://arxiv.org/abs/2010.14808
- 当时 Jun Ma 的单位是 Nanjing University of Science and Technology，通讯是 Nanjing University 的 Xiaoping Yang。这是他**去 Toronto 之前**的工作，属于"Jun Ma 个人学术谱系"而非"Wang Lab 产出"。
- 数据来源：LiTS、MSD Spleen、MSD Pancreas、KiTS、**NIH Pancreas**，加 Nanjing Drum Tower Hospital。NIH Pancreas 出自 NIH Clinical Center —— 与 DeepLesion 同一个 Summers 实验室体系，但作者是 Roth / Summers，不是 Ke Yan / Le Lu。

**与达摩院的交集**：Med-Query 论文引用了 AbdomenCT-1K（ref [43]）。这是我找到的、达摩院直接使用 Jun Ma 基准的记录。反向（AbdomenCT-1K 使用达摩院数据）不存在。

---

## 5. 判断：挑战赛生态是不是唯一接触面？

**是，但需要三条限定。**

**（a）RADAR 对 Wang Lab 的引用为零。** RADAR 的 60 条参考文献（Crossref，DOI 10.1126/science.aec6129）中**不含** MedSAM、MedSAM2、FLARE 任何一届、AbdomenCT-1K、AMOS。它引用的分割工具是 **TotalSegmentator**（10.1148/ryai.230024）与 **nnU-Net**（10.1038/s41592-020-01008-z），与你已知的 v1.5.7 预处理一致。GitHub README 的致谢只列 LAVIS / nnU-Net / MONAI / 3D-ResNets-PyTorch。RADAR 的训练数据是浙大一院等机构的 424,911 例自有增强腹部 CT，不碰公开挑战赛数据。

**（b）反向引用存在，而且指向的正是 RADAR 团队。** FLARE23 论文在讨论未来方向时写道，可以扩展到多模态，因为"text data has shown potential in enhancing lesion detection and segmentation accuracy"，引用 ref [46] = *Boosting Medical Image-based Cancer Detection via Text-guided Supervision from Reports*，作者 Guangyu Guo, Jiawen Yao, **Yingda Xia**, **Tony C. W. Mok**, **Zhilin Zheng**, Junwei Han, **Le Lu**, Dingwen Zhang, Jian Zhou, **Ling Zhang**（https://arxiv.org/abs/2405.14230）。其中 Yingda Xia、Tony C.W. Mok、Zhilin Zheng、Ling Zhang **全是 RADAR 的共同作者**。也就是说：**FLARE 把达摩院这条 report-supervised 路线写进了自己的 roadmap，FLARE 2025 随后真的开了 multimodal VLM 子任务；而 RADAR 反过来一句都不提 FLARE。** 影响是单向的，从达摩院流向 FLARE。

**（c）真正的公共地基不是挑战赛，是 DeepLesion。** 三条线在这里交汇：
- MedSAM2 的 CT 病灶训练数据 = DeepLesion（MedSAM2 论文 ref [42]）
- FLARE25 RECIST-to-3D = DeepLesion（含在 PancancerCTSeg 来源清单中），且 RECIST prompt 这个任务形式本身就是 DeepLesion 的标注格式
- DeepLesion 的一作 Ke Yan 与合著 Le Lu 现在在达摩院，Le Lu 是 Med-Query 的作者，Med-Query 就是 damomia 提交 FLARE22 的代码库

所以更准确的说法是：**挑战赛是唯一有人真正同场竞技并共同署名的地方（仅 FLARE 2022），但两条路线共享的真正基础设施是 DeepLesion 和 NIH Clinical Center 的人员外流，挑战赛只是这份遗产被反复再利用的场所。**

**还有一条你不该忽略的负面证据**：FLARE23 的 tuning/testing set 病灶标注，是放射科医生用 **ITK-SNAP + MedSAM** 做的（arXiv:2408.12534 正文："all visible lesions were annotated by a senior radiologist with the assistance of ITK-SNAP [51] and MedSAM [52]"）。**MedSAM 已经是 FLARE 数据生产链的一部分。** 而 RADAR 的数据生产链里对应位置站的是 TotalSegmentator。两边在"谁来做标注工具"这一层做了不同选择，而且互不采用 —— 这本身就说明两条路线在工程上是隔离的。

---

## 未能核实的项

- FLARE22 *Lancet Digital Health* 的 Declaration of interests 全文（站点 403，二手来源称 "MS is employed by Alibaba Damo Academy"，未直证）
- FLARE 2024 / 2025 的完整参赛队伍名单（awards 页面不存在，Codabench 排行榜需登录）—— 因此"达摩院 2023 年后未再参加 FLARE"这一判断，依据是 FLARE23 论文正文的前五名与所有公开获奖名单，不能排除他们以未获奖身份参赛过