# RADAR 技术拆解 —— 源码级

> 全部结论来自**直接读代码和调 API**，不是读论文摘要或新闻稿。每条都标了出处行号或命令。
> 核对日期：2026-09-20。仓库快照：`alibaba-damo-academy/damo-radar`，最后一次 push `2026-09-18T01:50:18Z`，343 stars，Apache-2.0。

---

## 一句话

RADAR 是 **ALBEF/BLIP 式的图文对比学习**，跑在 **3D ResNet + BERT-base** 上，用 **TotalSegmentator 的器官 mask 做 anatomy-aware pooling**，监督信号是 **Qwen 解析出来的报告标签**。全部成像物理是三行代码。

---

## ① 全部的物理：三行

`RADAR_inference/inference_demo.py`，`__getitem__` 里：

```python
image[image > 400] = 400
image[image < -300] = -300
image = (image - image.min()) / (image.max() - image.min() + 1e-8)
```

==一个 [−300, 400] HU 窗，然后**逐体数据** min-max 归一化。==

> [!strategy] 先问这一步扔掉了什么，再问模型还能剩下什么
> HU 是标定过的物理量（相对水的线性衰减系数 ×1000）。min-max 用的是**这一卷自己**的 min/max，不是窗的固定边界 —— 绝对 HU 标度在进网络之前就没了。
> 实践中腹部 CT 几乎总有空气（−1000 → 钳到 −300）和骨/对比剂（>400 → 钳到 400），所以 min/max 通常就是 −300/400。但这是**巧合成立**，不是设计保证。视野裁得紧、没有空气的体数据会让映射漂移。

### 后果，逐条对到征象表

从 `inference_demo.py` 的 `self.test_items` 里数出来的（命令见 §③）：

| 被窗口毁掉的通道 | 受影响的征象数 | 例子 |
|---|---|---|
| **地板 −300 HU**：肺实质 −700～−900 HU 全部钳平 | **10 个肺征象** | 肺_气胸、肺_结节、肺_斑片影、肺_膨胀不全 |
| **天花板 400 HU**：骨与钙化全部饱和 | 至少 8 个 | 主动脉_钙化、脾_钙化、肾_肾（盂）结石、肋骨_骨折、肋骨_骨质破坏、骶骨_骨炎、肝_肝内钙化灶、胆囊_结节状致密影 |

✗ 气胸（−1000 HU 的空气）和正常肺实质在输入里**是同一个值**。模型要认出气胸，只能靠塌陷肺边缘的几何，不能靠密度。
✗ "钙化"这个征象退化成"有没有饱和体素"，密度大小的信息没有了。

> [!insight] 这不是吹毛求疵，这是这条路线的定义特征
> RADAR 把 CT 当灰度图。它能做到 0.913 的平均 AUC 恰恰说明：**大部分常见腹部征象不需要定量密度就能认出来**。反过来说，凡是需要定量密度的（脂肪分数、碘浓度、材料组成），这条路线在原理上到不了。

---

## ② 几何预处理

同一个 `__getitem__`：

```
ref_spacing = (1.0, 1.0, 5.0)        # 重采样到 1×1×5 mm
transforms.Resized(..., mode="trilinear")
→ 裁掉全零区域，d 方向外扩 5，hw 方向外扩 20
→ pad 到 [96, 256, 384]
```

- **5 mm 层厚。** 小于 5 mm 的结构在输入里不存在。任何关于小病灶的性能声明都要按这个读。
- 96 层 × 5 mm = **480 mm** 的 z 覆盖。
- 推理时用**滑窗**（`forward_test_win`），多窗结果对每个器官取平均：`np.concatenate(probs).mean(0)[1]`。

---

## ③ 146 / 18 —— 从代码数出来的，不是从摘要抄的

```bash
curl -sL "https://raw.githubusercontent.com/alibaba-damo-academy/damo-radar/main/RADAR_inference/inference_demo.py" > radar_inf.py
python3 - <<'PY'
import re, collections
src = open('radar_inf.py', encoding='utf-8').read()
m = re.search(r"self\.test_items = \[(.*?)\]\n", src, re.S)
items = re.findall(r"'([^']+)'", m.group(1))
print("n findings:", len(items))
c = collections.Counter(i.split('_')[0] for i in items)
print("n organs:", len(c))
for k, v in c.most_common(): print(f"  {k}: {v}")
PY
```

输出：

```
n findings: 146
n organs: 18
  大肠: 18   肝: 18   肾: 14   胆囊: 14   小肠: 13   肺: 10
  胰腺: 10   脾: 8    肾上腺: 6  胃: 6    膀胱: 6   十二指肠: 5
  食管: 5    主动脉: 4  肋骨: 3   门静脉: 3  心脏: 2   骶骨: 1
```

✓ 和摘要里的"18 anatomical structures and 146 imaging findings"完全对上。

⚠️ 注意 **"腹部 CT"里含 10 个肺征象、3 个肋骨、2 个心脏、1 个骶骨** —— 覆盖范围实际是胸腹，不是纯腹部。

⚠️ 征象名与英文映射都**硬编码在推理脚本里**（`self.english_mapping`，一个 146 项的中英词典）。这不是从配置读的，是写死的。想换征象表就得改代码。

---

## ④ 模型与训练配置

`RADAR_train/radar_config.yaml` 全文关键项：

```yaml
model:
  arch: radar_pretrain
  med_config_path: "../ckpt/bert-base-uncased/config.json"
  max_txt_len: 512
  queue_size: 0
  alpha: 0.4
  radar_plus: True
run:
  task: image_text_pretrain
  init_lr: 1e-4      min_lr: 1e-6     warmup_steps: 3000
  max_epoch: 30      weight_decay: 0.05
  batch_size_train: 2   # 注释：we using 24 GPU with a total batch size of 48
  amp: False         seed: 42
```

| 项 | 值 | 说明 |
|---|---|---|
| 框架 | **LAVIS**（Salesforce，BSD-3） | `arch: radar_pretrain` 是 LAVIS 的模型注册名 |
| 文本编码器 | **BERT-base-uncased**，max 512 token | 不是 LLM，是 2018 年的 BERT |
| 视觉编码器 | **3D ResNet** | `dynamic_network_architectures/architectures/resnet_vl.py` |
| `alpha: 0.4` | ALBEF 的 **momentum distillation** 权重 | 不是什么新东西 |
| `queue_size: 0` | **关掉了 MoCo 式队列** | 纯 in-batch 负样本 |
| 训练规模 | 24 张 GPU，总 batch 48，30 epoch | 以现在的标准算**很小** |
| `amp: False` | 不用混合精度 | |

> [!insight] 数学层面没有新东西
> 损失是 InfoNCE + 交叉熵。骨干全是现成的。Acknowledgements 自己列了 LAVIS / nnU-Net / MONAI / 3D-ResNets-PyTorch 四个。
> **真正的创新在监督信号怎么造出来**，不在模型。

---

## ⑤ 监督信号：这才是论文的贡献

`docs/PREPROCESS.md` 写得很直白，两条外部依赖**都不在仓库里**：

| 依赖 | 类型 | 用途 |
|---|---|---|
| **TotalSegmentator v1.5.7** | 开源分割工具 | 生成 104 个解剖结构的原始 mask |
| **DashScope / Qwen** | LLM API | 报告解析（`check_organ_mention.py`、`report_parsing.py`、`report_parsing_normal.py`）|

流程：

```
原始 CT
  → TotalSegmentator v1.5.7 出 104 类 mask
  → process_img_mask.py 合并成 36 个主要解剖结构
  → 重采样到 [1, 1, 5] mm
  → 与 Qwen 解析出的器官级报告标签配对
  → 1500 万 anatomy-wise 图文对，零人工标注
```

⚠️ 报告解析脚本里要填 `dashscope.api_key = "YOUR_DASHSCOPE_API_KEY"` —— 复现需要阿里云账号。文档说"any other LLM can be substituted"。

### ⚠️ 重要更正：TotalSegmentator 是**教师**，不是**运行时组件**

> [!strategy] 先看推理时到底调用了什么，再判断依赖有多重

读 `RADAR_inference/dynamic_network_architectures/vision_branch.py`（160 行），`VisionBranch` **自带一个分割网络**：

```python
# line 35
arch_class_name="dynamic_network_architectures.architectures.unet_lightdecoder.PlainConvUNetLightD",
# line 54
output_channels=37,          # 36 个解剖结构 + 背景
# line 63
self.organs = [ ... ]
# line 113-115  —— 推理时自己预测 mask，不读外部 mask
pred_mask = torch.softmax(pred_logit, 1)
pred_mask = pred_mask.argmax(1)
y = pred_mask
```

==**推理时 RADAR 跑的是自己这个 37 通道 U-Net，根本不调用 TotalSegmentator。**==
TotalSegmentator v1.5.7 只出现在 `docs/PREPROCESS.md` 里，用来**离线生成训练标签**。README 也明说："The pretrained masks we release already went through the TotalSegmentator step, so you only need TotalSegmentator if you want to preprocess your own images from scratch."

对应修正 §⑥ 里"真正的成本是安装"那句：

| 你要做的事 | 需要装 TotalSegmentator v1.5.7 吗 |
|---|---|
| 跑 RADAR 发布的 checkpoint 做推理 | ✗ **完全不需要** |
| 在 MERLIN 上复现他们的外部测试 | ✗ 不需要（他们发布了处理好的 mask）|
| 用**自己的**数据重新预处理 / 重训 | ✓ 需要，这时才会撞上 `nnunet-customized==1.2` 那套 2022 年的依赖 |

### 池化核决定了分割精度根本不重要

同一文件 line 138–158，预测出的 mask 被 `F.max_pool3d` 三档下采样成 token 级布尔标记：

```python
kernel_size=(2, 8, 8)      # → organ_token_flags3
kernel_size=(4, 16, 16)    # → organ_token_flags2
kernel_size=(8, 32, 32)    # → organ_token_flags1
organ_token_flags1[i][unique_values.long() - 1] = highlight_tokens1 > 0
```

最粗那一档，**一个 token 覆盖 8×32×32 个体素**。在 `[1, 1, 5]` mm 的 spacing 下就是 **40 mm(z) × 32 mm × 32 mm**。

> [!insight] RADAR 对分割的要求是"标签别搞错、大致位置别飘"，不是"边界准"
> 边界级的 Dice 改进在 max-pool 到 40×32×32 mm 之后被完全吃掉。==这解释了为什么钉住 v1.5.7 的代价比看上去还小 —— 升级分割器的收益在数学上接近零。==
> 注意 `organ_token_flags1[i][unique_values.long() - 1]` 这一行：它**直接拿 mask 的整数标签当数组下标**去对齐器官文本。所以 RADAR 需要的不是"一块区域"，是"索引为 k 的那块是肝"。这一点在 [radar-vs-medsam.md](radar-vs-medsam.md) §能不能换成 MedSAM2 里是决定性的。

---

## ⑥ TotalSegmentator 钉在 v1.5.7 —— 钉的是一条已死分支的末端

PyPI 上传时间（`curl -sL https://pypi.org/pypi/TotalSegmentator/json`）：

```
2023-05-16   1.5.6
2023-09-26   2.0.0          ← v2 主线开始
2023-10-17   1.5.7          ← RADAR 钉的这个，比 v2.0.0 晚三周
2025-01-17   2.5.0
2026-08-12   2.18.0         ← 当前 PyPI 最新
```

GitHub weights tag：`v3.0.0-weights` 发布于 **2026-09-07**，比 RADAR 仓库最后一次 push（2026-09-18）早 11 天。

> [!strategy] 先判断这是懒还是对，再判断值不值得换
> **钉住是对的。** v2 的 breaking changes 原文：「all models have been retrained」，分割结果会和 v1 不同。RADAR 用这些 mask 做 pooling 区域，42 万次检查的图文对齐全建在 v1 形状的区域上。推理时换 v2 的 mask → pooling 几何与训练分布失配。要换就得重跑全部预处理 + 重训。

**换了能赚多少？** 逐条算：

| v2 的改进 | 对 RADAR 有用吗 |
|---|---|
| 新增 33 类（颅骨、甲状腺、四肢骨、颈动脉…） | ✗ 几乎全在腹部之外，只有 prostate 沾边 |
| 104 → 117 类 | ✗ RADAR 反正要合并成 36 类 |
| 修正 liver / spleen / kidney / aorta 的标注系统误差 | ✓ **唯一真能赚到的** —— 这四个都在 36 类里 |
| 边界级 Dice 提升 | ✗ 重采样到 5 mm 层厚基本抹平 |
| colon / small_bowel 的 GT 问题 | ✗ **v2 自己把它列在 still open problems 里，没修** |

⚠️ 最后一行很要命：RADAR 四种病理确诊癌症里的**结直肠癌**，正好踩在 v2 明确没修的那条上。

**安装成本只在"用自己的数据重训"这条路上才出现**（见上一节的更正表）。v1.5.7 的 `setup.py` 依赖：

```python
'nnunet-customized==1.2',      # 2022 年的 nnU-Net v1 私有 fork
'batchgenerators==0.21',
'SimpleITK',  'fury',  'xvfbwrapper',  'rt_utils',
```

2026 年要跑起来必须单独开环境，和 RADAR 自己的 `transformers==4.25`（跟随 LAVIS 的 pin）不在一个世界。
✓ 但如果你只是跑发布的 checkpoint，这一整段与你无关。

💡 顺带：`tissue_types` 任务（`subcutaneous_fat` / `skeletal_muscle` / `torso_fat`）是 **v2 才加的**，v1 完全没有，且是 v2 里少数**非商用许可**的任务之一。做脂肪/肌肉组成的工作只能走 v2 或 v3。

---

## ⑦ 许可：代码和权重不一样

| 位置 | 许可 |
|---|---|
| GitHub 代码 | **Apache-2.0** |
| HuggingFace checkpoint（`radar-generalist`） | **CC BY-NC-SA 4.0** —— 禁商用 + 相同方式共享 |

README 顶部的 badge 写的是 CC BY-NC-SA；仓库 `LICENSE` 文件是 Apache-2.0。==研究复现没问题，进产品线不行。==

---

## ⑧ 数字的可信度分层

| 结论 | 证据强度 | 理由 |
|---|---|---|
| 四种癌病理确诊子集 AUC 0.891–0.984 | **强** | 病理是独立金标准，不是报告标签 |
| 26 位医生 / 14 个中心的 reader study | **强** | 规模真实；人机协同 sensitivity +约 10%、阅片时间 −30%+ |
| 急腹症（训练时排除）AUC 0.904 | **强** | 干净的 out-of-distribution 测试 |
| 8 个外部中心 AUC 0.895 vs 内部 0.913 | **中强** | 掉得少，泛化信号真实；但外部中心全是县区级医院（见 [grassroots-network.md](grassroots-network.md)）|
| **146 个征象平均 AUC 0.913** | **弱** | 患病率差几个数量级，均值被脂肪肝/肝囊肿/胆囊结石这类常见又一眼可见的拉高 |
| 对照基线"最好的 VLM" 0.776 | **弱** | 大概率是没在这个量级腹部 CT 上训过的域外模型（**推断**，待核实）|
| 除病理子集外的测试标签 | **存疑** | 大概率也是 LLM 从报告解析的 → AUC 衡量的是"与当班医生写了什么一致"，医生漏写 = 负例（**推断**，待核实）|

---

## 与 Shu 工作的关系

> [!insight] RADAR 的 146 个征象里有"脂肪肝"，输出是一个二值概率
> 它靠的是**与报告文字一致**。Shu 的 water/lipid material decomposition 输出的是**带误差预算的 lipid fraction**。
> ==没有任何一份放射报告会写"脂肪分数 0.62"—— 报告监督这条路在原理上到不了那里。==
> 这不是落后，是护城河：报告是定性的，物理量是定量的，两者不可互推。

值得抄的是**评估的形式**，不是模型：独立金标准子集（病理／体模真值）+ 多读者 reader study + 外部中心。这三件事在几百例的规模上照样立得住。

---

## See Also

- [authors-affiliations.md](authors-affiliations.md) —— 39 位作者的单位原文
- [damo-lineage.md](damo-lineage.md) —— 达摩院医疗 AI 的血统
- [radar-vs-medsam.md](radar-vs-medsam.md) —— 与 MedSAM 的关系
- [../README.md](../README.md)
