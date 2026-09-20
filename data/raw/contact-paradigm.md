# MedSAM 路线 vs DAMO RADAR 路线：医学影像 AI 的两种理论

先说结论性的一句：**这两条线之间没有代码依赖、没有模型复用、没有共同作者**，但有一条真实的思想谱系——"从医院日常产生的、不是为 AI 准备的痕迹里榨取监督信号"。MedSAM 那边榨的是 RECIST 测量标记，RADAR 这边榨的是报告文本。这个 idea 的源头是同一批人（NIH Ronald M. Summers 实验室），而他们后来去了 DAMO。下面逐条展开。

---

## 0. 先修正三条前提（我核过原始来源）

**(a) MedSAM2 权重不是 Apache-2.0。** GitHub 仓库是 Apache-2.0（https://github.com/bowang-lab/MedSAM2），但权重在 Hugging Face 上的 YAML metadata 写的是 `license: cc-by-sa-4.0`，而同一张 model card 的正文 License 一节又写着 "The model weights can only be used for research and education purposes."（https://huggingface.co/wanglab/MedSAM2）。这两句互相矛盾：CC BY-SA 4.0 是允许商用的，"research and education only" 不允许。所以严格讲 MedSAM2 的权重授权处于**自相矛盾状态**，谁要商用都得先去问 Wang Lab。这一点削弱了"MedSAM2 完全开放 vs RADAR 半开放"的对仗，真正的差别下面第 5 节重讲。

**(b) TotalSegmentator 在 RADAR 里只用于离线造训练标签，推理时根本不调用。** 我读了仓库代码：`RADAR_inference/dynamic_network_architectures/vision_branch.py` 里的 `VisionBranch` 自带一个 `PlainConvUNetLightD`（nnU-Net 系的轻解码器 3D U-Net），`output_channels=37`（36 个解剖结构 + 背景），forward 里直接 `pred_mask = softmax(logits).argmax(1)`，然后用这个自己预测的 mask 去做 organ token 选取。TotalSegmentator v1.5.7 只出现在 `docs/PREPROCESS.md`：跑出 104 个结构的 mask → `process_img_mask.py` 合并成 36 个 → 重采样到 spacing `[1,1,5]`（https://github.com/alibaba-damo-academy/damo-radar/blob/main/docs/PREPROCESS.md）。也就是说 TotalSegmentator 是**教师**，不是**组件**。这对第 7 节"能不能换成 MedSAM2"是决定性的。

**(c) Ke Yan 和 Le Lu 都不在 RADAR 的作者名单里。** RADAR 的 BibTeX 作者列表（README 里给了全名单）中 DAMO 侧是 Jianpeng Zhang、Yingda Xia、Tony C.W. Mok、Ling Zhang 等，末位通讯 Tingbo Liang（浙大一院）（https://github.com/alibaba-damo-academy/damo-radar#citation）。所以"DeepLesion 作者进了 DAMO"是**人员流动**，不是**这篇论文的共同作者关系**。别把它说成直接连接。

---

## 1. 任务本体不同：一个是"把你指的东西描出来"，一个是"告诉我这卷片子有什么病"

MedSAM2 的定义写得非常干净：promptable segmentation foundation model，输入是 bounding box prompt，输出是 mask，架构是 image encoder + prompt encoder + memory attention + mask decoder（https://arxiv.org/abs/2504.03600）。注意 **prompt encoder 的存在本身就是一个理论承诺**：模型不负责"找"，只负责"描"。谁来找？人，或者上游的检测器。而且输出的 mask 是 **class-agnostic** 的——它不知道自己描的是肝还是脾，语义完全由你喂进去的那个框携带。

RADAR 的定义是反过来的：输入整卷增强腹部 CT，无提示，输出 18 个解剖结构上 146 个 imaging findings 的概率。Science 摘要原文（Crossref 取得，https://api.crossref.org/works/10.1126/science.aec6129）："RADAR achieved high diagnostic performance and robust generalization for 18 anatomical structures and 146 imaging findings."

**价值主张的差别不在精度，在责任边界。** MedSAM2 把"判断"留给人，所以它永远不需要为漏诊负责——它的失败模式是"你给的框我描歪了"，这是可验收的。RADAR 把"判断"吞进去了，它的失败模式是"整卷片子里那个 8 mm 的胰腺病灶我没提"，这是不可局部验收的，只能统计验收。这就是为什么两边的评价指标必然分叉（第 4 节）。

---

## 2. 监督信号从哪来：这是两条路线真正的分水岭

MedSAM2：455,000 个 3D image-mask 对 + 76,000 帧视频（arXiv 摘要原文）。**每一个 mask 归根到底都来自人手**——要么是公开数据集里前人标的，要么是这篇论文自己组织标的：5,000 个 CT 病灶、3,984 个肝 MRI 病灶、251,550 帧超声心动图，论文自称把人工成本降低 85% 以上（https://arxiv.org/abs/2504.03600）。前作 MedSAM 更彻底：1,570,263 个 image-mask 对（https://www.nature.com/articles/s41467-024-44824-z）。

RADAR：424,911 次检查，1.5 million image-text 对、超过 15 million anatomy-wise image-text 对（AAAS 官方新闻稿，https://www.eurekalert.org/news-releases/1143748），"learning directly from clinical reports without manual annotation"。报告怎么变成结构化监督？仓库里写得很直白，三步全是调 LLM：`check_organ_mention.py`（这份报告提没提这个器官）→ `report_parsing.py`（抽出该器官的描述）→ `report_parsing_normal.py`（判定正常/异常，用来压低 false negative），默认用 DashScope/Qwen API（https://github.com/alibaba-damo-academy/damo-radar/blob/main/docs/PREPROCESS.md）。

**成本结构对比：**

| | MedSAM 路线 | RADAR 路线 |
|---|---|---|
| 单位监督的边际成本 | 标一个 mask 的人力（分钟量级/例，MedSAM2 把它压到 ~15%） | 调一次 LLM 的 token 费（分钱量级/份报告） |
| 规模上限 | 标注预算 × 人的耐心 | 医院有多少份报告 |
| 天花板在哪 | **线性**：想要 10 倍数据就得 10 倍预算 | **常数**：报告已经写完了，存量就在那 |
| 信号质量 | 像素级精确，但只描述"形状" | 语义级丰富，但完全不定位 |

第三行是全篇最重要的一行。MedSAM2 的 85% 成本下降是**把线性斜率压小**，不是**把线性变成常数**。RADAR 换的是量纲。这就是为什么 RADAR 敢做 146 个 findings 而 MedSAM2 只能做"分割"——146 个 findings 如果要 mask 监督，光设计标注规范就是一个博士的四年。

代价是对称的：报告里**没有坐标**。"肝右叶见低密度灶"这句话不告诉你它在第几层第几个像素。RADAR 是怎么把无坐标的文本挂到空间上的？靠那 36 个解剖 mask——代码里 `organ_token_flags[i][unique_values.long() - 1] = ...`，把每个器官对应的 visual token 打上布尔标记，于是"肝"这段文本就只和"肝 mask 覆盖的 token"对齐。**解剖分割在这里扮演的是"报告文本的定位器"**，这是整个 anatomy-wise 设计的物理含义。

---

## 3. 数据获取模式：公开数据再加工 vs 医院深度合作

MedSAM2 的数据是**可以被别人复现和继承的**。它发布的三个派生数据集——CT_DeepLesion-MedSAM2、LLD-MMRI-MedSAM2、RVENet-MedSAM2——全部建在已公开的原始数据之上，并明确要求引用原始论文（https://github.com/bowang-lab/MedSAM2）。CT_DeepLesion-MedSAM2 的卡片写得很清楚：来自 NIH DeepLesion 的 32,735 个病灶 / 32,120 张 CT slice / 10,594 个 study / 4,427 个病人，用 MedSAM2 的 human-in-the-loop 流程把原本只有 RECIST 长径/垂直径的标注升级成 3D mask（https://huggingface.co/datasets/wanglab/CT_DeepLesion-MedSAM2）。**这是一种"数据增值"模式：别人的公开数据 + 我的模型 = 新的公开数据。**

RADAR 的数据是**结构上不可复现的**。42 万例增强腹部 CT 加配套报告，只能来自一家有几十年 PACS 存量的三甲医院及其协作网络——末位通讯是浙大一院院长 Tingbo Liang，这不是巧合，这是准入条件。约束也随之而来：外部验证只能去**别的医院**，八个外部中心 AUC 0.895（新闻稿）。而它在公开基准上的那次外部测试用的是 **MERLIN**——Stanford 的腹部 CT vision-language 数据集与模型，刚发在 Nature（https://www.nature.com/articles/s41586-026-10181-8，代码 https://github.com/StanfordMIMI/Merlin）。RADAR 仓库里专门有 `inference_merlin_testset.py`、`calc_metrics_merlin_testset.py`。

**所以两边"能做多大"的天花板是不同性质的：** MedSAM 受限于**标注预算**（可以用钱和工具缓解），RADAR 受限于**机构准入**（钱买不到，只能靠关系和伦理审批）。前者是可扩散的，后者是不可扩散的。这也解释了下面第 5 节的授权差异。

---

## 4. 验证形式：Dice 是工程验收，AUC + reader study 是临床验收

MedSAM2 报的是跨器官/跨病灶/跨模态的分割精度，加上**成本下降 85%** 这个运营指标，加上"迄今最大规模的 user study"（arXiv 摘要）。注意它的 user study 问的是：**标注员用了它以后快了多少**。这是一个生产力实验，不是一个诊断实验。

RADAR 报的是一整套临床证据链：
- 近 4 万例真实检查上 146 个 findings 平均 AUC 0.913，对照的 vision-language model 是 0.776（新闻稿）
- 急诊场景 27,000+ 例，AUC 0.904；八个外部中心 0.874–0.912（新闻稿 / 二手报道）
- Reader study：26 位放射科医生，用了 RADAR 之后诊断 sensitivity 提高约 10%（Science 摘要原文，这条是一手的）
- 病理确诊子集（肝/胰/胃/结直肠四种癌）AUC 0.891–0.984 ——**这条我只在二手媒体报道里看到**（例如 https://runtimewire.com/article/alibaba-damo-radar-open-source-abdominal-ct-ai），Science 正文付费墙我没读到，新闻稿也没写，请当作未经一手确认。

**哪一种更接近临床采纳？RADAR 这一套，而且不是因为数字好看，是因为它回答了监管和科室主任真正会问的三个问题：** (i) 换一家医院还准吗（外部中心）；(ii) 和金标准比呢（病理）；(iii) 医生用了会不会更好、会不会更慢（reader study 里阅片时间下降 30% 以上）。Dice 回答不了任何一个。Dice 只能回答"我省了你多少标注工"，而标注工不是临床科室的成本项——它是**研究组**的成本项。

这里有一个对你（Shu）直接有用的判断：**MedSAM2 的验证形式服务于"做研究的人"，RADAR 的验证形式服务于"买设备的人"。** 你写论文时该抄哪一套，取决于你要说服谁。

---

## 5. 开放程度：真正的差别是那两个字母 NC

- RADAR 代码 Apache-2.0，权重 CC BY-NC-SA 4.0（README 的 License badge 与 HF 组织页均如此，https://huggingface.co/radar-generalist）
- MedSAM2 代码 Apache-2.0，权重 CC BY-SA 4.0 + 正文一句 "research and education purposes"（见第 0 节 (a)）

**共同点比差异更说明问题：两边都对代码慷慨、对权重设限。** 代码是方法，方法拿去用无所谓——论文已经发了，引用已经拿到了。权重是**数据的压缩表示**，而数据是拿不回来的资产。RADAR 的 42 万例医院数据受伦理协议约束，DAMO 就算想给也不能给；加 NC 是在保护**医院的资产和阿里的产品线**（DAMO 的 PANDA 已经拿到 FDA breakthrough device designation，https://www.nature.com/articles/s41591-023-02640-w 是它的论文），商业化通道必须留着。MedSAM2 的 CC BY-SA 没有 NC，理论上允许商用，但正文那句"research and education only"暴露了同样的犹豫——**学术组织想开放，但没想清楚下游被商业化之后自己的位置**。

所以这一条不是"开放 vs 封闭"，是"**一个有明确商业下游、所以把边界画清楚；一个没有商业下游、所以边界画糊了**"。糊掉的边界对复用者其实更危险。

---

## 6. 可迁移性：谁更容易被别的组捡起来用

MedSAM2 明显更容易，而且这是设计目标，不是副产品：3D Slicer 插件、Gradio app、两个 Colab demo、五个不同的 checkpoint（通用 + 超声心跳 + 肝 MRI 病灶 + CT 病灶 + FLARE25 baseline）（https://huggingface.co/wanglab/MedSAM2）。跨 CT / MRI / PET / 超声 / 内镜。你今晚下载，明早就能在自己的数据上出 mask。

RADAR 几乎不可迁移，而且也是设计使然：它只吃**增强腹部 CT**，重采样到 `[1,1,5]`，36 个解剖结构写死在 `vision_branch.py` 的 `self.organs` 列表里（而且是中文字符串），文本侧绑在 LAVIS 框架上。换成非增强 CT、换成胸部、换成 photon-counting CT 的 VMI，整条链子都要重训——而重训需要你自己的 42 万份报告。

**但"可迁移性"这个词有歧义，必须拆开：**
- **权重可迁移性**：MedSAM2 完胜。
- **方法可迁移性**：RADAR 更强。"用 LLM 把存量报告解析成 anatomy-wise 监督"这个配方，任何有 PACS 的科室都能在自己的模态上复刻一遍，不需要 RADAR 的权重。而 MedSAM2 的方法（拿 SAM 2.1 微调）已经没什么可迁移的了——它本身就是迁移的终点。

---

## 7. 会不会合流：具体的技术判断

### 7a. RADAR 的上游分割换成 MedSAM2？**不行，而且换了也没用。**

三条理由，从弱到强：

1. **提示问题**：MedSAM2 需要 bounding box。36 个器官就是 36 个框（3D 的话还要每层或首层给框）。谁来给？如果上一个检测器，那你已经有了一个全自动定位模型，MedSAM2 只是给它精修边界——这时 TotalSegmentator 的位置根本没被动过。

2. **语义问题（决定性）**：MedSAM2 输出 class-agnostic mask。RADAR 需要的不是"一块区域"，是"**索引为 21 的那块是肝**"——代码里 `organ_token_flags[i][unique_values.long() - 1]`，直接拿 mask 的整数标签当数组下标去对齐"肝"这段文本。class-agnostic 的输出天然缺的就是这个整数。语义得从框那里来，框又得从别处来，MedSAM2 在这条链上不生产任何 RADAR 需要的信息。

3. **精度根本不重要（最反直觉的一条）**：看 forward 里的池化核——mask 被 `F.max_pool3d` 用 `(2,8,8)`、`(4,16,16)`、`(8,32,32)` 三档下采样成 token 级布尔标记。**最粗那一档，一个 token 覆盖 8×32×32 个体素。** 在这个尺度上，MedSAM2 相对 TotalSegmentator 多出来的那几个点 Dice 会被 max-pooling 完全吃掉。RADAR 对分割的要求是"**标签别搞错、大致位置别飘**"，不是"边界准"。花力气升级分割器，收益是零。

而且别忘第 0 节 (b)：推理时 RADAR 用的是自己那个 37 通道 U-Net，TotalSegmentator 连运行时依赖都不是。要"换"，你换的是**离线的教师标签生成器**，那就等于要重新预训练整个视觉分支。投入产出比荒谬。

### 7b. MedSAM2 接上报告监督？**可行，但得绕一圈，而且这个圈已经有人走过了。**

障碍是同一个：**报告不定位**。"肝右叶低密度灶"生成不了框。所以直接把 report loss 加到 MedSAM2 上是无效的——没有梯度路径能从文本走到 mask decoder。

可行的路线只有一条：**弱定位 → 伪框 → MedSAM2 精修**。即先训一个报告监督的分类器（RADAR 那种），用它的 anatomy token 激活或 Grad-CAM 产生候选框，再喂给 MedSAM2 出 mask，再用人筛一遍。

**而这正是 CT_DeepLesion-MedSAM2 已经做过的事，只不过"弱定位"那一步不是模型给的，是医生给的。** DeepLesion 的本体就是从 NIH 的 PACS 里挖出来的 RECIST bookmark——放射科医生日常测量时随手画的长径和垂直径，**一种为临床而非为 AI 产生的痕迹**。MedSAM2 把这个 2D 十字标记升级成 3D mask（https://huggingface.co/datasets/wanglab/CT_DeepLesion-MedSAM2）。

**这就是你问的"关系"的真正答案：**

> DeepLesion（Ke Yan, Xiaosong Wang, Le Lu, Ronald M. Summers, NIH Clinical Center, 2018，https://pubmed.ncbi.nlm.nih.gov/30035154/）提出的核心命题是"**医院日常留下的痕迹就是免费的大规模监督**"。这个命题有两个方向的展开：
> - **几何方向**：痕迹是 RECIST 标记 → 升级成 mask → MedSAM / MedSAM2（Wang Lab @ University of Toronto / Vector Institute）
> - **语义方向**：痕迹是报告文本 → 经 LLM 解析成 anatomy-wise 标签 → RADAR（DAMO）
>
> Ke Yan 和 Le Lu 后来都从 NIH 去了 DAMO（Ke Yan 现为 DAMO Academy 的 Staff Algorithm Engineer，此前在 NIH 由 Ronald Summers 与 Le Lu 指导，https://yanke23.com/）。所以**语义方向是在同一批人手上完成的第二次展开**，只是 RADAR 这篇论文他们没署名。
>
> 两条线共享祖先、不共享代码。**它们不会在模型层面合流，因为它们已经在思想层面是同一件事的两个投影了。**

如果非要预测未来形态：真正的合并点不是"RADAR 用 MedSAM2 分割"，而是"**一个模型同时输出 findings 概率和该 finding 的 mask**"——即报告监督提供"是什么"，稀疏的 RECIST/bookmark 监督提供"在哪"，两种免费痕迹互补。MERLIN 已经把 segmentation 列为 model-adapted task 之一了（https://www.nature.com/articles/s41586-026-10181-8），这是最接近的先例。

---

## 8. 对你（UCI Molloi 组，CT 成像物理，材料分解 / photon-counting CT，几百例量级）的启示

**先说哪条路线在小数据上可移植：两条都不可直接移植，但 MedSAM 那条的"方法论"可移植，RADAR 那条的"验证形式"可移植。这是两件不同的东西，别混。**

**(1) RADAR 的模型学不了，但它的 anatomy-token 技巧可以偷，而且是零成本的。**

RADAR 最值钱的工程 trick 不是 VLM，是"**用一个现成的自动分割器把整卷 CT 切成解剖单元，然后所有下游量都在解剖单元上算**"。这个 trick 不含任何学习参数——TotalSegmentator v1.5.7 是开源的、全自动的、104 个结构（https://github.com/wasserth/TotalSegmentator/tree/v1.5.7）。你几百例的材料分解数据，完全可以用它把每一例自动切成器官，然后把 water/lipid/protein 分数、噪声、误差预算全部按解剖结构汇总，而不是按手画 ROI。**这把"几百例"的统计功效从"几百个 ROI"放大到"几百 × 36 个解剖单元"**，并且消除了手画 ROI 的读者间变异——而读者间变异恰恰是你在 PVAT / FAI 那条线上反复撞到的东西。

**(2) 但注意一个反向的物理警告：RADAR 对分割精度的容忍度极高（max-pool 到 8×32×32），你的容忍度极低。**

RADAR 可以把 mask 池化到极粗还照样工作，因为它要的是"这堆 token 属于肝"。你做材料分解，**边界就是 partial volume effect，边界就是信号本身**。所以你能偷 RADAR 的"解剖单元化"，但绝不能偷它对分割质量的态度。在边界精度这件事上，MedSAM2 那种 promptable + human-in-the-loop 精修的范式才是对的：你给一个框，模型给一个可以被人一眼验收、必要时手改的 mask，改完的 mask 回流成下一轮训练数据。**几百例的量级恰好是 human-in-the-loop 最划算的区间**——太少不值得搭流程，太多人改不过来。

**(3) 监督信号这一层，你其实处在 RADAR 的反面，而且这是优势不是劣势。**

RADAR 的全部设计都是在回答"我有海量数据但没有标签"。你的处境是"我有少量数据但**有真值**"——phantom 已知浓度、已知材料、已知 keV。**已知真值在小数据上的信息密度，远高于 42 万份报告里的弱标签。** 所以任何让你放弃 phantom 真值去追"大数据自监督"的建议都是在往下走。你该做的是相反的事：把真值用到极致（per-rod refit、误差预算、noise-aware GLS），然后只在**评价形式**上学 RADAR。

**(4) 真正该抄的是 RADAR 的验证形式，而不是它的模型——和你在 Slomka EAT 那条线上得出的结论是同一条。**

RADAR 的证据链结构是：内部 → 外部多中心 → 与金标准（病理）比 → reader study 测人机协同。把这个结构平移到你的尺度上：

- "外部中心" → **换一台扫描仪**（NAEOTOM vs Canon vs GE Apex，你已经有这条线）
- "病理金标准" → **phantom 已知浓度 / 化学分析**
- "reader study" → **让放射科医生在有/无材料分解图的情况下判读，测判读一致性和时间**

第三条你大概率还没做。而它恰恰是 RADAR 这篇论文能上 Science 而不是 Medical Physics 的原因之一——**"这个方法在物理上是对的"和"这个方法让医生做得更好"是两篇不同的论文，后者贵得多。** 几百例的量级做不了前者的大 N，但完全做得了后者的小 N reader study（RADAR 的 reader study 也只有 300 例、61 个 findings）。

**(5) 授权层面的一条实际提醒。**

如果你哪天想在论文里用 RADAR 权重做对比或做上游，CC BY-NC-SA 4.0 的 **SA（ShareAlike）**比 NC 更麻烦：任何衍生模型也得用同样的许可发布。学术论文一般没事，但如果 Molloi 组的东西未来要走产业化（你们和厂商有合作史），这条会卡住。MedSAM2 那边虽然授权自相矛盾，但至少没有 SA 的传染性。**要用就在方法学层面用（读它的预处理流程、抄它的 anatomy-token 思路），别把它的权重编进你的 pipeline。**

---

## 一句话收束

MedSAM 路线赌的是"**分割是通用能力，诊断是下游的事**"；RADAR 路线赌的是"**诊断是唯一值钱的事，分割只是它的定位辅助**"。前者产出工具，后者产出证据。你做的是成像物理——物理量的可信度是你的产品，所以你的方法论该像 MedSAM（工具、可验收、边界精确、human-in-the-loop），你的论文形态该像 RADAR（外部有效性、金标准对照、人机协同）。这两件事不冲突，很多人把它们搞混，是因为他们只看模型不看证据链。

---

### 来源

- [An expert-level generalist AI for abdominal CT diagnosis | Science, 393(6817):eaec6129, 2026-09-17](https://www.science.org/doi/10.1126/science.aec6129) ·  [Crossref 摘要](https://api.crossref.org/works/10.1126/science.aec6129) · [PubMed 42752131](https://pubmed.ncbi.nlm.nih.gov/42752131/)
- [alibaba-damo-academy/damo-radar (GitHub, Apache-2.0)](https://github.com/alibaba-damo-academy/damo-radar) · [docs/PREPROCESS.md](https://github.com/alibaba-damo-academy/damo-radar/blob/main/docs/PREPROCESS.md) · [Zenodo 归档](https://zenodo.org/records/21271172) · [huggingface.co/radar-generalist (CC BY-NC-SA 4.0)](https://huggingface.co/radar-generalist)
- [AAAS/EurekAlert 官方新闻稿：424,911 exams, AUC 0.913 / 0.904 / 0.895](https://www.eurekalert.org/news-releases/1143748)
- [MedSAM2: Segment Anything in 3D Medical Images and Videos, arXiv:2504.03600](https://arxiv.org/abs/2504.03600) · [bowang-lab/MedSAM2 (GitHub, Apache-2.0)](https://github.com/bowang-lab/MedSAM2) · [huggingface.co/wanglab/MedSAM2 (权重授权自相矛盾)](https://huggingface.co/wanglab/MedSAM2) · [medsam2.github.io](https://medsam2.github.io/)
- [CT_DeepLesion-MedSAM2 数据集卡片](https://huggingface.co/datasets/wanglab/CT_DeepLesion-MedSAM2)
- [MedSAM: Segment anything in medical images, Nature Communications 15:654, 2024](https://www.nature.com/articles/s41467-024-44824-z)
- [DeepLesion, Yan/Wang/Lu/Summers, NIH Clinical Center, 2018](https://pubmed.ncbi.nlm.nih.gov/30035154/) · [Ke Yan 个人主页（DAMO 现职 + NIH 经历）](https://yanke23.com/) · [Le Lu 主页](https://lelu007.github.io/)
- [PANDA: Large-scale pancreatic cancer detection via non-contrast CT, Nature Medicine, 2023](https://www.nature.com/articles/s41591-023-02640-w)
- [Merlin: a computed tomography vision–language foundation model and dataset, Nature 652(8112), 2026](https://www.nature.com/articles/s41586-026-10181-8) · [StanfordMIMI/Merlin](https://github.com/StanfordMIMI/Merlin)
- [TotalSegmentator v1.5.7](https://github.com/wasserth/TotalSegmentator/tree/v1.5.7)
- 二手来源（未经一手确认，仅用于第 4 节的病理子集与 reader study 细节）：[runtimewire 报道](https://runtimewire.com/article/alibaba-damo-radar-open-source-abdominal-ct-ai) · [SCMP](https://www.scmp.com/tech/big-tech/article/3368055/alibaba-open-sources-medical-ai-model-can-detect-cancer-and-nearly-150-conditions)