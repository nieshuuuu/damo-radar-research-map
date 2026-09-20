# RADAR (Science 2026, 10.1126/science.aec6129) 结果可信度独立审计

**核查日期** 2026-09-20 · **审计者约束**：本会话 WebSearch 配额已耗尽（200/200），全部核查通过直接调 API（PubMed E-utilities、Crossref、Europe PMC、Semantic Scholar、Unpaywall、GitHub API、HuggingFace API、Zenodo、Science RSS）+ 直接下载并运行仓库代码完成。**Science 正文与补充材料全文付费墙，403，我没有读到**（Semantic Scholar 明确返回 `openAccessPdf.status = "CLOSED"`）。因此凡标"查不到"的，是**在无正文的条件下查不到**，不等于不存在。

---

## 一、七个数字的出处分层（逐条核实）

摘要原文我拿到了两份互相独立的副本：[PubMed 42752131](https://pubmed.ncbi.nlm.nih.gov/42752131/)（E-utilities XML）和 [Crossref](https://api.crossref.org/works/10.1126/science.aec6129) 的 JATS abstract，**逐字一致**。摘要全文只有这些数字：

> "...trained on **more than 400,000** contrast-enhanced abdominal CT examinations and **15 million** anatomy-wise image-text pairs... for **18 anatomical structures and 146 imaging findings**. In a reader study, RADAR assistance increased the diagnostic sensitivity of **26 radiologists by ~10%**."

| 你给的数字 | 在摘要里？ | 在别处核到了吗 | 判定 |
|---|---|---|---|
| 146 征象 / 18 器官 | ✓ 在 | ✓ **独立复现**：从 `inference_demo.py` 的 `self.test_items` 数出来正好 146 项 / 18 个前缀器官 | **强** |
| 训练 424,911 次检查 | ✗ 摘要只说 "more than 400,000" | ✗ README / HF 卡片 / Zenodo 全部只写 "over 400,000" | **精确数字查不到出处**（只能来自正文或新闻稿） |
| 1500 万 anatomy-wise 图文对 | ✓ 在 | ✓ README、HF 模型卡、HF 数据集卡三处一致（"15 million anatomy-aware image–text pairs"） | **强** |
| **150 万图文对** | ✗ 不在 | ✗ **任何公开材料里都没有这个数** | **查不到，建议从你的清单里划掉或标为未核实** |
| 平均 AUC 0.913 | ✗ 不在 | ✗ | 只能来自正文/新闻稿 |
| 对照 VLM 0.776 | ✗ 不在 | ✗ | 同上 |
| 8 个外部中心 0.895 | ✗ 不在（摘要只说 "internal and external evaluations across multiple centers"） | ✗ | 同上 |
| 四种癌 0.891–0.984 | ✗ 不在 | ✗ | 同上 |
| 急腹症 0.904 | ✗ 不在 | ✗ | 同上 |
| 26 位放射科医生、敏感度 +约 10% | ✓ **都在摘要里** | — | **强（作为"作者声明"）** |
| 14 个中心、阅片时间 −30%+ | ✗ 不在 | ✗ | **查不到** |

**新闻稿**：我尝试了 EurekAlert 搜索页（404）、EurekAlert 分类浏览（403）、DAMO 官网 news/events（返回 2.5 KB 的 SPA 壳）、Mojeek、Bing、DuckDuckGo（CAPTCHA，按规则不绕）。**没有定位到任何一份新闻稿**。所以我无法确认上表中"只在新闻稿里"的那几个数到底出自哪。

**一个结构性观察**：0.913 / 0.776 / 0.895 / 0.891–0.984 / 0.904 这五个数**一个都没进摘要**。Science 的摘要是作者自己写的，把 AUC 全部留在正文而只在摘要里放"26 位医生 +10% 敏感度"，说明作者自己认为最硬的卖点是 reader study，不是 AUC。这和下面第三节的判断一致。

---

## 二、测试标签是怎么来的 —— 找到了直接证据，你的怀疑成立（至少对外部测试集）

这是本次审计最实的一条。仓库里发布了外部测试的**完整评测脚本和预测结果**：

- 评测脚本 https://github.com/alibaba-damo-academy/damo-radar/blob/main/RADAR_inference/calc_metrics_merlin_testset.py
- 预测结果 https://github.com/alibaba-damo-academy/damo-radar/blob/main/results/RADAR_infer_results_MerlinTestset.csv （2.1 MB，5,125 例 × 21 个征象）

脚本里真值的来源是这一行：

```python
all_labels = json.load(open('../ckpt/merlin_labels.json'))
...
        label = float(label_json[patient_id])
        if label == -1:  # following merlin's protocal
            continue
```

`merlin_labels.json` 由 [`ckpt/transform_label_to_json.py`](https://github.com/alibaba-damo-academy/damo-radar/blob/main/ckpt/transform_label_to_json.py) 从 MERLIN 官方发布的 `zero_shot_findings_disease_cls.csv` 转换而来（见 [docs/INFERENCE.md](https://github.com/alibaba-damo-academy/damo-radar/blob/main/docs/INFERENCE.md)）。

那 MERLIN 的这份 csv 是怎么来的？Merlin 论文（Nature 2026，[10.1038/s41586-026-10181-8](https://doi.org/10.1038/s41586-026-10181-8)）是开放获取的，全文在 [PMC13082451](https://pmc.ncbi.nlm.nih.gov/articles/PMC13082451/)。其方法部分：三位放射科医生拟定 30 个征象，为每个征象写出"存在短语表"和"不存在短语表"，**用这些短语去挖报告文本**产生正负例，然后人工复核（"We manually review them to ensure that the labels are accurate"）。同一篇还说明这类 findings 标签与 ICD/EHR 表型标签是两套东西。

**结论**：在**唯一可复现的外部测试**上，真值 = **从报告文本里短语匹配出来的**（有人工复核，比纯 LLM 解析强，但仍然是"报告说了什么"，不是"病人身上有什么"）。`-1` 这个类别的存在本身也说明这是 CheXpert 式的不确定标签体系，而且 RADAR 按 MERLIN 协议**把 -1 直接丢弃**——丢掉的恰好是报告写得含糊的那批，也就是最难的那批。

**对 RADAR 自己的 146 征象内部测试集**：无直接证据。已知的是整条监督链路都是 Qwen 解析报告（[docs/PREPROCESS.md](https://github.com/alibaba-damo-academy/damo-radar/blob/main/docs/PREPROCESS.md) 三步：`check_organ_mention.py` → `report_parsing.py` → `report_parsing_normal.py`，全部调 DashScope/Qwen API）。仓库**没有**发布内部测试集的标签构造说明，也没有发布内部测试的预测结果。所以"内部测试标签也是 LLM 解析报告得来"是**合理推断但未证实**——要证实必须看正文/补充材料。

**唯一确定不受此问题影响的**：病理确诊的肝/胰/胃/结直肠四种癌（0.891–0.984）。病理是独立金标准，这一块的方法学是干净的（虽然数字本身我核不到）。

---

## 三、146 个征象的患病率 & 平均 AUC 作为聚合指标

**患病率**：公开材料里**没有**任何一个征象的阳性例数。仓库只发了外部 MERLIN 21 个征象的**预测分数**，没发标签；内部 146 个征象连预测分数都没发。→ **查不到**。

**但聚合方式我查到了，而且是最坏的那种。** 两个评测脚本都明明白白写着：

```python
all_aucs.append(diease_auc)
...
print(f'AvgAUC: {np.mean(all_aucs):.4f}')
```

——**逐征象 AUC 的无权重算术平均（macro average）**，不按例数加权。所以"平均 AUC 0.913"里，一个只有十几例阳性的罕见征象和一个几千例的脂肪肝**权重完全相同**。这种聚合数的置信区间由最稀疏的那几项主导，而单值报告把这一点完全藏住了。

另外，Merlin 论文明说其 zero-shot findings 评测集是**人为配平正负例**的（"we balance the number of positive and negative examples for each finding"）。所以外部 MERLIN 上的 0.8835 **不是连续临床队列上的表现**，是配平子集上的表现。内部 146 征象是不是也配平过——不知道。

**我自己从预测分数里算出来的一条旁证**（5,125 例，命令与数据见文末）：各征象的分数分布差异极大——

| 征象 | 分数中位数 | >0.5 的比例 | 论文给的 AUC |
|---|---|---|---|
| 肝大 hepatomegaly | 0.0008 | 3.8% | 0.8988 |
| 肝内胆管扩张 | 0.0032 | 3.6% | 0.8711 |
| 主动脉瓣钙化 | **0.5020** | **50.0%** | 0.8436 |
| 粥样硬化 | 0.2724 | 40.9% | 0.8739 |

主动脉瓣钙化的分数分布**几乎精确地居中在 0.5**——模型在绝对意义上对这个征象接近无信息，但 AUC 仍有 0.8436，因为 AUC 只看排序。**把这样 146 个标度完全不可比的分数的 AUC 做算术平均，得到的 0.913 不是一个有临床含义的量。** 仓库里没有发布任何工作点/阈值，GitHub issue #3（[链接](https://github.com/alibaba-damo-academy/damo-radar/issues/3)，标题就是 "How to convert the scores into cls result?"）就是用户在问这个，作者尚未回复。

---

## 四、0.776 那个对照基线是哪个模型 —— **查不到**，但能缩小范围

正文读不到，摘要和仓库都没提基线。但我从 Crossref 拿到了**完整的 60 条参考文献**（https://api.crossref.org/works/10.1126/science.aec6129 ），逐个解析 DOI 后，视觉-语言基线的候选只可能在这几个里：

| 参考文献 | 是什么 | 在腹部 CT 上训练过吗 |
|---|---|---|
| ref 12 · [10.1038/s41586-026-10181-8](https://doi.org/10.1038/s41586-026-10181-8) | **Merlin**（Nature 2026，Stanford） | ✓ **是，腹部 CT** |
| ref 13 · [10.1038/s41551-025-01599-y](https://doi.org/10.1038/s41551-025-01599-y) | **CT-CLIP / CT-RATE**（Nat BME 2026） | ✗ 胸部 CT |
| ref 14 · Shui et al.（无 DOI，ICLR 系） | **fVLM**，作者自己组的前作 | ✗ 胸部 CT |
| ref 28 · [10.1109/CVPR52733.2024.01068](https://doi.org/10.1109/CVPR52733.2024.01068) | **BIUD**，作者自己组（Cao, Zhang, Xia, Mok, Ye, Lu, Zhang 全是本文作者） | ✗ 胸部 CT |
| ref 34 · Sellergren et al. | Google 胸片基础模型系 | ✗ |
| ref 35 · "LASA Team" | 阿里自家医疗多模态大模型 | ✗ 通用 |
| ref 57 · Bai et al. | **Qwen** 系 VLM | ✗ 通用 |
| ref 33 · [10.1056/AIoa2400640](https://doi.org/10.1056/AIoa2400640) | BiomedCLIP（NEJM AI，1500 万图文对） | ✗ 2D 通用生物医学 |

**判断**：候选池里**只有 Merlin 一个是腹部 CT 训练的 3D 视觉-语言模型**。如果 0.776 那个"最好的对照"是 Merlin，对比相对公平；如果是 Qwen/LASA 这类通用 VLM，则 0.913 vs 0.776 这个对比基本没有信息量（拿专用模型打通用模型）。**在读到正文之前不能下结论。** 顺带提醒一个命名撞车：arXiv 上有另一篇叫 RADAR 的论文（[arXiv 2603.06681](https://arxiv.org/abs/2603.06681)，"RADAR: A Multimodal Benchmark for 3D Image-Based Radiology Report Review"），**与本文无关**，检索时别混。本文**没有** arXiv 预印本（我用 arXiv API 按标题和摘要双路检索，均无）。

---

## 五、reader study 设计细节 —— **几乎全部查不到**

公开材料里**只有两句话**：26 位放射科医生、敏感度提升约 10%（均出自摘要）。

- 读者资历分布：查不到
- 14 个中心：**连"14 个中心"这个说法本身我都没核到出处**
- 是否随机化、是否有洗脱期（washout）：查不到
- 统计方法（配对检验？multi-reader multi-case ROC / DBM-MRMC / Obuchowski-Rockette？）：查不到
- 阅片时间 −30%：查不到出处

这些必然在补充材料里。**在读到补充材料之前，reader study 的强度无法评估**——26 位医生 × 多中心的规模本身是真实的加分项，但"敏感度 +10%"如果没有配套的**特异度变化**和**假阳性率**，这个数字可以是设计出来的（降低阈值必然提敏感度）。摘要只给敏感度、不给特异度，这一点值得在正文里重点看。

---

## 六、许可：**三份不同的许可，同一个项目**（全部核实完毕）

| 渠道 | 许可 | 核实方式 |
|---|---|---|
| GitHub 仓库 LICENSE 文件 | **Apache-2.0** | GitHub API `license.spdx_id = "Apache-2.0"`，https://api.github.com/repos/alibaba-damo-academy/damo-radar |
| GitHub README **顶部 badge** | **CC BY-NC-SA 4.0** | README 原文第 6 行 |
| GitHub README **License 小节** | **Apache-2.0** | 同一份 README 的末尾 |
| HuggingFace 模型 `radar-generalist/RADAR` | **CC BY-NC-SA 4.0** | API tag `license:cc-by-nc-sa-4.0` + 模型卡 front-matter `license: cc-by-nc-sa-4.0` |
| HuggingFace 数据集 `radar-generalist/RADAR-auxiliary-data` | **CC BY-NC-SA 4.0** | 同上，且卡片末尾明写 |
| Zenodo v2 [21271172](https://zenodo.org/records/21271172)（379 MB） | **CC-BY-4.0** | Zenodo 记录元数据 |
| Zenodo v3 [21504519](https://zenodo.org/records/21504519)（2.1 MB） | **CC-BY-4.0** | Zenodo 记录元数据 |

**你原来的说法（GitHub Apache-2.0 vs HF checkpoint CC BY-NC-SA 4.0）核实为真，但不完整**：

1. README 自己就自相矛盾——顶部 badge 写 NC，末尾 License 小节写 Apache-2.0。
2. **还有第三份**：两个 Zenodo 存档都标 CC-BY-4.0（**允许商用**），与 HF 的 NC 直接冲突。而且论文正文引用的是 **v3 (21504519)**（参考文献第 60 条），README 链接的却是 **v2 (21271172)**——两个版本、两个体积（2.1 MB vs 379 MB），指向不一致。
3. 实务判断：**权重不能商用**（HF 是权重的唯一发布渠道，NC 明确）；代码 Apache-2.0 可商用；Zenodo 的 CC-BY-4.0 大概率是上传时用了默认值，不应被当作授权依据。这不是"小瑕疵"——一个 Science 正刊论文的四个发布渠道给出三种互斥许可，对任何想用它的临床团队都是法务障碍。

---

## 七、同行评议意见 / Perspective / 公开质疑 —— **目前一条都没有**

| 检查项 | 结果 | 来源 |
|---|---|---|
| Science 同期是否配 Perspective | **没有** | 我拉了 Science 393(6817) 的完整 TOC RSS（38 条），本文条目类型是 "Research Article"，同期 38 篇里没有任何一篇是针对它的 Perspective 或 editor's summary。https://www.science.org/action/showFeed?type=etoc&feed=rss&jc=science |
| 被引 | **0** | Crossref `is-referenced-by-count: 0`；Europe PMC citations `hitCount: 0`；Semantic Scholar `citationCount: 0` |
| PubMed comment/correction 链接 | **无** | PubMed XML 里无 `CommentsCorrectionsList` |
| GitHub issue 里的方法学质疑 | **无** | 3 个 issue 全是使用问题：#1 "Online tool?"、#2 Apple Silicon 推理补丁、#3 "How to convert the scores into cls result?" https://github.com/alibaba-damo-academy/damo-radar/issues |
| 预印本评论区 | **不适用**，无预印本 | arXiv API 双路检索无结果 |

论文 2026-09-17 上线，到今天第 3 天。**"没有质疑"在这个时间点上没有信息量**，不能当作正面证据。

---

## 八、我自己新做出来的证据：外部测试其实是可复现的，而且有两个方法学硬伤

这是本次审计的增量。仓库把**外部 MERLIN 测试的预测分数和评测脚本全发了**，所以这一块可以不依赖正文直接查。

### (1) 唯一可复现的外部数字是 **0.8835**，不是 0.895

[docs/INFERENCE.md](https://github.com/alibaba-damo-academy/damo-radar/blob/main/docs/INFERENCE.md) 直接贴了逐征象结果：

```
abdominal_aortic_aneurysm 0.9903   atherosclerosis 0.8739   submucosal_edema 0.8879
appendicitis 0.7621                bowel_obstruction 0.9704 aortic_valve_calcification 0.8436
cardiomegaly 0.8724                biliary_ductal_dilation 0.8711  hepatomegaly 0.8988
hepatic_steatosis 0.8917           pleural_effusion 0.9574  atelectasis 0.7091
renal_hypodensities 0.9122         renal_cyst 0.9426        hydronephrosis 0.88
gallstones 0.9193                  pancreatic_atrophy 0.9356 splenomegaly 0.9682
fracture 0.6834                    hiatal_hernia 0.8601     surgically_absent_gallbladder 0.9234
AvgAUC: 0.8835
```

注意最差的三项：**腰椎骨折 0.6834、肺膨胀不全 0.7091、阑尾炎 0.7621**。骨折和肺不张差，与该项目 HU 窗 `[-300, 400]` 把肺实质和骨/钙化全部钳平的输入设计完全一致（详见本仓库 `sources/radar-technical-teardown.md` §①）。**阑尾炎 0.7621 尤其要紧**——这是急腹症里最常见的诊断，而你清单里"急腹症 AUC 0.904"是个内部数字。同一个模型在外部数据上对阑尾炎只有 0.76。

[docs/TRAINING.md](https://github.com/alibaba-damo-academy/damo-radar/blob/main/docs/TRAINING.md) 另给两个数：RADAR+ 在 Merlin 训练集上从零训 anatomy AUC 0.888；用 RAD-CT 预训练后再 finetune 得 0.918（anatomy）/ 0.876（all）。**注意 0.918 那个不是零样本外部**——它在 MERLIN 训练集上 finetune 过，不能拿来当泛化证据。

> **所以：整个项目对外可验证的外部泛化上限是 0.8835（21 个征象，配平子集，报告派生标签）。** 0.895/8 中心、0.913/146 征象全部不可验证。

### (2) 21 个征象里有一个**根本不是模型输出**

评测脚本 `calc_metrics_merlin_testset.py` 第 46–49 行：

```python
if f'{organ}_{disease}' == '胆囊_术后胆囊缺失':  # surgically_absent_gallbladder
    model_pred = np.array(pd_scores)
    model_pred = (model_pred<1000).astype(np.float32).tolist()
    pd_scores = model_pred
```

我读了 CSV：这一列的取值范围是 **0 到 38,901**，中位数 4,213——**它是体素数（分割出来的胆囊体积），不是概率**。阈值 1000 体素在 1×1×5 mm 下 = **5 mL**。

所以 `surgically_absent_gallbladder AUC = 0.9234` 是**对一个手工阈值化的二值分割体积**算出来的。二值预测子的 "AUC" 数学上等于 (灵敏度+特异度)/2，**不是 ROC 曲线下面积**，和其余 20 项不同质，却被平均进了 0.8835。（按此规则，5,125 例里 **1,260 例（24.6%）**被判为"胆囊缺失"。）

### (3) 缺失值被填成"最确信的阴性"

同一脚本：

```python
if np.isnan(prob):
    prob = 0.  # not intact organs
```

HF 数据集卡解释了 NaN 的来源：训练/推理只用 **intact organs**（mask 完全落在 96×256×384 裁剪框内、未被边界截断的器官）。我统计了 CSV：

- **胆囊结石一项有 392 例（7.6%）是 NaN**，被填成 0 分。
- 这 392 例**全部**胆囊体积 < 1000 体素，其中 **374 例体积恰为 0** —— 也就是说，它们几乎全是**胆囊切除术后**的病人。
- 术后病人的 MERLIN 胆石症标签基本必然是阴性。把 7.6% 的确定阴性统一钉在分数排序的最底端，**会系统性抬高 gallstones 的 AUC（0.9193）**。

这不是致命错误，但它是一个**有方向的偏倚**，且没有在任何公开文档里披露。其余 20 项的 NaN 都在 1–9 例量级，影响可忽略。

---

## 九、分层结论

### 证据强（可独立验证）
1. **146 征象 / 18 器官**——从推理代码数出来，与摘要一致。附带事实：其中含 **10 个肺征象、3 个肋骨、2 个心脏、1 个骶骨**，覆盖范围实为胸腹而非纯腹部。
2. **训练规模 40 万+检查 / 1500 万 anatomy-wise 图文对**——摘要 + README + HF 模型卡 + HF 数据集卡四处一致。
3. **外部 MERLIN 零样本 21 征象 AvgAUC 0.8835**——作者自己在 docs 里贴了逐项数值，预测 CSV 和评测脚本全公开，任何人拿到 MERLIN 标签就能复跑。
4. **许可混乱**：Apache-2.0（代码）/ CC BY-NC-SA 4.0（权重与辅助数据）/ CC-BY-4.0（两个 Zenodo 存档）三套并存，README 内部自相矛盾。**权重禁商用**这一条是确定的。
5. **聚合方式是无权重 macro 平均**——代码里 `np.mean(all_aucs)`，没有按患病率加权，没有置信区间。
6. **目前零被引、零 Perspective、零公开质疑**——但论文才发表 3 天，此条无信息量。

### 证据中等（有间接证据，但不能定论）
7. **测试标签源于报告文本**：对外部 MERLIN 是**确证的**（Merlin 论文方法：放射科医生短语表挖报告 + 人工复核；RADAR 按其协议丢弃 -1 标签）。对内部 146 征象是**强推断**（整条监督链是 Qwen 解析报告），但**作者未公开内部测试标签的构造方式**。→ 你原来的判断"AUC 衡量的是与报告一致而非与真相一致"，**在外部测试上成立，在内部测试上待正文确认**。
8. **病理确诊四癌子集方法学干净**——病理是独立金标准，这个设计是对的；但 0.891–0.984 这组数字本身我核不到。
9. **26 位医生 reader study 规模真实**——写进了摘要，作者不会在摘要里编。但只报敏感度不报特异度，是需要在正文里追的。

### 证据弱 / 查不到
10. **0.913、0.776、0.895、0.891–0.984、0.904、424,911、−30% 阅片时间、14 个中心、150 万图文对**——**一个都不在摘要、README、HF 卡片、Zenodo 或任何我能访问的渠道里**。必须读 Science 正文/补充材料。其中"150 万图文对"我怀疑是转述时把 1500 万误记了。
11. **0.776 基线的身份**——查不到。参考文献里唯一在腹部 CT 上训练过的对照是 Merlin；其余候选（CT-CLIP、fVLM、BIUD 均为胸部 CT；Qwen、LASA、BiomedCLIP 为通用模型）都不是腹部 CT 专用。**如果 0.776 来自通用 VLM，这个对比不构成有意义的证据。**
12. **reader study 全部设计细节**（资历、随机化、洗脱期、统计方法、特异度变化）——查不到。
13. **每个征象的阳性例数**——完全没有公开。平均 AUC 0.913 的稳健性**无法评估**，而且已知外部基准（MERLIN）是人为配平正负例的，不是连续临床队列。
14. **新闻稿**——我没能定位到任何一份（WebSearch 配额耗尽 + EurekAlert 403/404），所以"哪些数字只在新闻稿里"这个问题我**答不了**。

### 我会怎么总结这篇的可信度
数据规模、工程完成度和开源程度是真的（357 stars、41 forks、权重+外部测试预测+评测脚本全发，这在中国团队的 Science 正刊里不常见）。**最硬的证据是病理确诊子集和 reader study 的设计形式**，不是 0.913。**0.913 这个头条数字是最弱的一环**：无权重 macro 平均、标签源于报告、患病率不公开、无置信区间、无工作点阈值。而唯一能外部验证的同类数字是 **0.8835**，且其中还混进了一个非模型输出的分割阈值项和一个有方向的缺失值填充。

**下一步要读什么**（按性价比排序）：补充材料里的 (a) 内部 146 征象测试集标签构造方法、(b) 每个征象的阳性例数表、(c) 0.776 基线的模型名与训练数据、(d) reader study 的特异度与假阳性率变化。这四项拿到，这篇的可信度就完全定了。

---

## 本次审计产出的本地文件

下载与计算脚本的落地位置（临时目录，需要保留的话要拷走）：

- `/private/tmp/claude-501/-Users-shunie-Developer/152a37b5-0538-44e5-b0f8-ccce9c6bab33/scratchpad/radar/merlin_results.csv` —— 外部 MERLIN 测试的 5,125×21 预测分数
- `/private/tmp/claude-501/-Users-shunie-Developer/152a37b5-0538-44e5-b0f8-ccce9c6bab33/scratchpad/radar/RADAR_inference/calc_metrics_merlin_testset.py` —— 评测脚本（macro 平均、NaN→0、胆囊体积阈值三处证据都在这里）
- `/private/tmp/claude-501/-Users-shunie-Developer/152a37b5-0538-44e5-b0f8-ccce9c6bab33/scratchpad/radar/docs/INFERENCE.md`、`P.md`（PREPROCESS）、`T.md`（TRAINING）
- `/Users/shunie/Developer/damo-radar-research-map/data/pubmed-42752131.xml` —— 摘要原文（本仓库已有）

本审计与本仓库已有的 `/Users/shunie/Developer/damo-radar-research-map/sources/radar-technical-teardown.md` 互补：那份是源码级架构拆解，这份是数字与出处的审计。两份的 §⑧ / §九 结论表可以合并成一张。

**Sources:**
- [PubMed 42752131](https://pubmed.ncbi.nlm.nih.gov/42752131/)
- [Crossref record (含 60 条参考文献)](https://api.crossref.org/works/10.1126/science.aec6129)
- [Europe PMC citations (0)](https://www.ebi.ac.uk/europepmc/webservices/rest/MED/42752131/citations?format=json)
- [Science 393(6817) TOC RSS](https://www.science.org/action/showFeed?type=etoc&feed=rss&jc=science)
- [GitHub: alibaba-damo-academy/damo-radar](https://github.com/alibaba-damo-academy/damo-radar)
- [docs/INFERENCE.md（逐征象外部 AUC）](https://github.com/alibaba-damo-academy/damo-radar/blob/main/docs/INFERENCE.md)
- [docs/TRAINING.md](https://github.com/alibaba-damo-academy/damo-radar/blob/main/docs/TRAINING.md)
- [docs/PREPROCESS.md](https://github.com/alibaba-damo-academy/damo-radar/blob/main/docs/PREPROCESS.md)
- [calc_metrics_merlin_testset.py](https://github.com/alibaba-damo-academy/damo-radar/blob/main/RADAR_inference/calc_metrics_merlin_testset.py)
- [results/RADAR_infer_results_MerlinTestset.csv](https://github.com/alibaba-damo-academy/damo-radar/blob/main/results/RADAR_infer_results_MerlinTestset.csv)
- [GitHub issues](https://github.com/alibaba-damo-academy/damo-radar/issues)
- [HuggingFace radar-generalist/RADAR](https://huggingface.co/radar-generalist/RADAR)
- [HuggingFace radar-generalist/RADAR-auxiliary-data](https://huggingface.co/datasets/radar-generalist/RADAR-auxiliary-data)
- [Zenodo 21271172 (v2)](https://zenodo.org/records/21271172)
- [Zenodo 21504519 (v3)](https://zenodo.org/records/21504519)
- [Merlin 论文全文 PMC13082451](https://pmc.ncbi.nlm.nih.gov/articles/PMC13082451/)
- [Merlin Nature 2026 DOI](https://doi.org/10.1038/s41586-026-10181-8)
- [CT-CLIP / CT-RATE, Nat BME](https://doi.org/10.1038/s41551-025-01599-y)
- [BIUD, CVPR 2024](https://doi.org/10.1109/CVPR52733.2024.01068)
- [arXiv 2603.06681（同名但无关的 RADAR benchmark）](https://arxiv.org/abs/2603.06681)
- [Stanford AIMI MERLIN 数据集](https://stanfordaimi.azurewebsites.net/datasets/60b9c7ff-877b-48ce-96c3-0194c8205c40)