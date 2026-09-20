# RADAR 是怎么做出来的 —— 设备、数据、模型、训练、推理

> 全部来自**直接读代码、读仓库文档、调 API**：`alibaba-damo-academy/damo-radar`（Apache-2.0）、HuggingFace `radar-generalist/RADAR`、PyPI、GitHub API。
> Science 正文与补充材料在付费墙后，扫描协议、设备型号、伦理批件这类**只写在 Methods 里的信息这里没有**，各处已标明。
> 核对日期：2026-09-20。

---

## 一句话

RADAR = **一个 3D U-Net 编码器 + 一个 BERT**，用**图文对比学习**对齐；对齐的单位不是"整卷 CT ↔ 整份报告"，而是"**一个器官的图像特征 ↔ 报告里写这个器官的那几句话**"。器官怎么圈出来：模型自带一个 37 通道的分割头。报告怎么拆到器官：用 Qwen 解析。
==模型零件全是现成的，新东西是监督信号的造法和损失函数里的软目标。==

---

## ① 需要什么设备

### 算力

| 环节 | 官方写明的配置 | 出处 |
|---|---|---|
| **训练** | **24 张 GPU（A100 或 H20）**，每卡 batch 2，总 batch 48，**fp32**（`amp: False`），30 epoch | `docs/TRAINING.md` + `radar_config.yaml` |
| 多卡启动 | `torchrun --nproc_per_node=8 train.py`（即 3 台 8 卡机）| `docs/TRAINING.md` |
| **推理** | **单张 A100 或 H20 即可**；大规模推理建议多卡 `torchrun --nproc_per_node=8` | `docs/INFERENCE.md` |
| 预处理（分割教师）| TotalSegmentator v1.5.7，每卷一次 GPU 推理 | `docs/PREPROCESS.md` |
| 预处理（报告解析）| **不需要本地 GPU**，调 DashScope/Qwen API（按 token 付费）| 同上 |

> [!insight] 这个量级放在今天很小
> 24 张卡 × 30 epoch、不开混合精度、batch 48。==卡点从来不是算力，是 42 万份带报告的 CT。==
> 显存占用官方没写。输入 patch 是 `96 × 256 × 384` 的单通道 3D 体，fp32、U-Net 六个 stage，A100/H20（80/96 GB 级）是他们实际用的卡；更小的卡能不能跑，仓库里没有任何说法。

### 模型体积（HuggingFace `radar-generalist/RADAR` 的实际文件）

| 文件 | 大小 | 是什么 |
|---|---:|---|
| `checkpoint_radar_pretrain.pth` | **1,566 MB** | 旗舰：RAD-CT（浙大一院 42 万例）上预训练 |
| `checkpoint_radar_plus.pth` | 1,651 MB | RADAR+：在公开的 Merlin-CT-Train 上从零训练 |
| `checkpoint_radar_plus_finetuned_on_merlin.pth` | 1,651 MB | 旗舰权重在 MERLIN 上微调 |
| `checkpoint_unet.pth` | 208 MB | 只含视觉分支（U-Net）的预训练权重，训练 RADAR+ 时用来初始化 |
| `bert-base-chinese/` | 412 MB | 旗舰用的中文文本编码器 |
| `bert-base-uncased/` | 440 MB | MERLIN 分支用的英文文本编码器 |

208 MB ÷ 4 字节 ≈ **5,200 万参数**的视觉分支（估算）；两份 BERT-base 各约 1.1 亿参数（在线一份 + 动量副本一份），这就是 checkpoint 1.5 GB 的主要来源。

### 软件环境

```
Python 3.10 · torch>=1.10 · transformers==4.25 · timm==0.4.12 · fairscale==0.4.4
monai · batchgenerators · SimpleITK · nibabel · nltk · huggingface_hub
```

`transformers==4.25` 这类老版本 pin 是跟着 LAVIS 走的。环境只需要一个 conda env：

```bash
conda create -n radar python=3.10 && conda activate radar
pip install -r requirements.txt
cd download_scripts && python download_checkpoints.py && python download_auxiliary_data.py
```

### 成像设备这一侧

- 输入是**增强腹部 CT**，NIfTI 格式。覆盖范围实际是**胸腹**：146 个征象里含 10 个肺、3 个肋骨、2 个心脏、1 个骶骨。
- 重采样到 `1 × 1 × 5 mm` 之后才进模型，所以**原始层厚 ≤5 mm 即可**，薄层重建没有额外收益。
- ==扫描仪厂商/型号、kVp、对比剂期相、重建核 —— 公开材料里全都没有==（在 Science Methods 里）。外部中心已知的只有两家：余杭一院 256 排、绩溪县医院 GE 64 排 128 层（见 [grassroots-network.md](grassroots-network.md)）。

---

## ② 数据：三个数据集各管什么

| 数据集 | 规模 | 语言 | 公开吗 | 在 RADAR 里的角色 |
|---|---|---|---|---|
| **RAD-CT** | 424,911 次检查 → 150 万图文对 → **1500 万 anatomy-wise 图文对** | 中文 | ✗ 永不公开 | 旗舰模型的训练集（浙大一院）|
| 内部真实世界评测 | 39,160 例 | 中文 | ✗ | AUC 0.913（95% CI 0.911–0.915）的来源 |
| **MERLIN** | 15,331 例腹部 CT + 报告 | 英文 | ✓ Stanford AIMI | ① 旗舰模型的**外部测试集** ② RADAR+ 的**公开训练集** |

**MERLIN 是 RADAR 全部公开可复现性的载体。** RAD-CT 放不出来，所以他们用这个公开的同任务数据集把整条流水线完整演示了一遍：发布的 TotalSegmentator mask 跑的是斯坦福的 CT，Qwen 解析的是斯坦福的英文报告，`checkpoint_radar_plus.pth` 就是在它上面从零训出来的。

MERLIN 本身：*Nature* **652:1318–1328**（2026），40 位作者全部斯坦福，一作 Louis Blankemeier，通讯 **Akshay S. Chaudhari**，代码与权重 MIT 许可。

---

## ③ 预处理：把"一卷 CT + 一份报告"变成"36 份器官级图文对"

```
┌─ 图像侧 ────────────────────────────────────────────────────────┐
│ 原始 CT (NIfTI)                                                  │
│   → TotalSegmentator v1.5.7      104 类解剖结构 mask             │
│   → process_img_mask.py          合并成 36 个主要结构            │
│   → 重采样                       图像和 mask 都到 [1, 1, 5] mm   │
└─────────────────────────────────────────────────────────────────┘
┌─ 文本侧（三步全是调 LLM）──────────────────────────────────────┐
│ 原始报告                                                         │
│   → check_organ_mention.py   (qwen_plus)  这份报告提没提这个器官 │
│   → report_parsing.py        (qwen_max)   抽出写该器官的那几句   │
│   → report_parsing_normal.py              该器官是 正常 / 异常   │
└─────────────────────────────────────────────────────────────────┘
        ↓
每个病人得到：{器官名: 描述文本} + {器官名: normal/abnormal} + 整份报告
```

**36 个解剖结构**（代码里以中文字符串写死）：肾上腺、主动脉、竖脊肌、脑、锁骨、大肠、十二指肠、食管、面部、股骨、胆囊、臀肌、心脏、髋关节、肱骨、髂动脉、髂静脉、髂腰肌、下腔静脉、肾、肝、肺、胰腺、门静脉、肺动脉、肋骨、骶骨、肩胛骨、小肠、脾、胃、气管、膀胱、颈椎、腰椎、胸椎。

**成本分两档是刻意的**：高频的"提没提"过滤用便宜的 `qwen_plus`，低频的结构化抽取用贵的 `qwen_max`。Qwen 属于阿里云而不是达摩院，RADAR 是跨事业部调商业 API；文档说可换成任何其他 LLM。

**第三步 normal/abnormal 是给损失函数用的**，专门用来压假阴性（见 ⑤）。报告里没提到的器官，文本直接填 `normal.`。

### TotalSegmentator 在这里的角色：离线教师

它**只在造训练标签时用一次**，推理时完全不调用 —— 模型自己带分割头（见 ④）。
钉在 v1.5.7（2023-10-17 发布；v2.0.0 是 2023-09-26，当前 PyPI 2.18.0）是因为训练数据全是按 v1 形状的 mask 对齐的，换版本等于换 pooling 几何，要重跑全部预处理并重训。

| 你要做的事 | 要装 TotalSegmentator v1.5.7 吗 |
|---|---|
| 跑发布的 checkpoint 推理 | ✗ 不需要 |
| 在 MERLIN 上复现 | ✗ 不需要（他们发布了处理好的 mask，HF 上分 part00/01/02）|
| 用自己的数据重新预处理/重训 | ✓ 需要。依赖 `nnunet-customized==1.2` + `batchgenerators==0.21`，必须单独开环境 |

💡 顺带：v2 才有的 `tissue_types` 任务（`subcutaneous_fat` / `skeletal_muscle` / `torso_fat`）v1 里没有，且是非商用许可。做脂肪/肌肉组成只能走 v2 以上。

---

## ④ 模型结构

```
CT patch  1 × 96 × 256 × 384          报告文本（器官级 或 整份）
      │                                      │
┌─────▼──────────────────────┐        ┌──────▼──────────────┐
│ VisionBranch                │        │ BERT-base           │
│ PlainConvUNetLightD         │        │ max 512 token       │
│ 6 stage                     │        │ 取 [CLS]            │
│ [32,64,128,256,320,320] 通道│        └──────┬──────────────┘
│                             │               │ Linear 768→256
│  ├─ 分割头: 37 通道          │               ▼
│  │   (36 器官 + 背景)        │          text_feat (256-d)
│  │   argmax → pred_mask      │
│  │                           │
│  └─ 最深三层 skip 特征        │
│      1×1×1 Conv → 256-d      │
│      展平成三组 token         │
└─────┬──────────────────────┘
      │ pred_mask 经 max_pool3d 变成"哪些 token 属于器官 k"的布尔标记
      ▼
┌────────────────────────────────────────────┐
│ 器官 k 的 ROI 池化                          │
│  query = 可学习的 query_tokens[k] (256-d)   │
│  key/value = 三个尺度里属于器官 k 的 token  │
│  MultiheadAttention(4 头, dropout 0.1)      │
│  → vision_projs[k] : Linear 256→256         │  ← 36 个器官各有自己的投影层
└─────┬──────────────────────────────────────┘
      ▼
  image_feat_k (256-d)   ←── 对比学习 ──→   text_feat
```

### 视觉分支：nnU-Net 的编码器 + 砍薄的解码器

```python
"n_stages": 6,
"features_per_stage": [32, 64, 128, 256, 320, 320],
"kernel_sizes": [[1,3,3],[1,3,3],[3,3,3],[3,3,3],[3,3,3],[3,3,3]],
"strides":      [[1,1,1],[1,2,2],[1,2,2],[2,2,2],[2,2,2],[2,2,2]],
"n_conv_per_stage":         [2,2,2,2,2,2],   # 编码器：标准 nnU-Net
"n_conv_per_stage_decoder": [1,1,1,1,1],     # 解码器：每级只留一层卷积
"norm_op": BatchNorm3d,  "nonlin": ReLU,  "deep_supervision": True
```

- 前两个 stage 的卷积核是 `[1,3,3]`、前三个 stage 的 z 向 stride 是 1 —— **专门适配 5 mm 层厚的各向异性体**：浅层只做面内卷积，z 方向等到面内降够了才开始降。
- 解码器被砍到每级一层卷积：==它不需要一个好的分割器，只需要一个能把标签贴对的粗分割器 + 一组好的编码器特征。==
- 整个 `dynamic_network_architectures/` 是从 MIC-DKFZ 的库 vendored 进来的，RADAR 自己加的只有 `unet_lightdecoder.py` 和 `unet_decoder_light.py`。

### 三个尺度的 token 与解剖标记

最深三层 skip 的累积 stride 分别是 `(2,8,8)` / `(4,16,16)` / `(8,32,32)`。预测出的 mask 用**同样大小的核**做 `max_pool3d`：

```python
F.max_pool3d(masks, kernel_size=(2, 8, 8),   stride=(2, 8, 8))     # → organ_token_flags3
F.max_pool3d(masks, kernel_size=(4, 16, 16), stride=(4, 16, 16))   # → organ_token_flags2
F.max_pool3d(masks, kernel_size=(8, 32, 32), stride=(8, 32, 32))   # → organ_token_flags1
organ_token_flags1[i][unique_values.long() - 1] = highlight_tokens1 > 0
```

池化核等于编码器的累积步长，所以**每个 token 恰好对应一块体素**；只要这块体素里有一个属于器官 k，这个 token 就算器官 k 的。最后一行直接**拿 mask 的整数标签当数组下标** —— 模型需要的不是"一块区域"，是"第 k 号器官在哪"。

在 `[1,1,5]` mm 下，最深层一个 token = **40 mm(z) × 32 mm × 32 mm**。

### 文本分支

| checkpoint | 文本编码器 |
|---|---|
| 旗舰 `checkpoint_radar_pretrain.pth`（中文报告）| **`bert-base-chinese`** |
| RADAR+（MERLIN 英文报告）| `bert-base-uncased` |

取 `[CLS]` 向量过 `Linear(768→256)`。另有一份**动量副本**（momentum 0.995），只用来算文本之间的相似度（见 ⑤），不参与图文对齐本身。

---

## ⑤ 损失函数：真正的方法贡献在这里

总损失 = **对比损失 + 分割 Dice 损失**。训练时**奇偶迭代交替**两种对比学习：

```
偶数步（radar_plus=True 时）→ 整图对比：整卷特征 ↔ 整份报告      ← RADAR+ 的"全局对齐"
奇数步                     → 器官级对比：器官 k 特征 ↔ 器官 k 的描述   ← RADAR 的核心
```

### 器官级对比：逐器官各算一次 InfoNCE

对每个器官 k，在全部 GPU 上 `all_gather` 出该器官的所有 (图像特征, 文本特征) 对，算双向相似度矩阵 `sim_i2t / sim_t2i`（除以可学习温度，初值 0.07，钳在 [0.001, 0.5]），再对 36 个器官的损失**求和**。

两个筛选条件决定一个样本进不进某个器官的损失：

1. **器官必须完整** —— 模型自己预测的 mask 不碰 patch 的六个边界面。被裁掉一半的肝不参与对齐。
2. **这个 batch 里该器官至少有一例异常** —— 全是"正常"的器官这一步不算，没有可学的对比。

### 软目标：同一器官的"正常"不互相排斥

标准 InfoNCE 把 batch 里除自己以外的样本全当负例。但两个病人的肝都写着"正常"，把他们推开是错的。RADAR 把目标矩阵改成：

```
sim_targets = 对角线 1
            + [两例都 normal]                               → 记为正例
            + [两例文本逐字相同]                             → 记为正例
            + [两例都 abnormal] × softmax(动量BERT的文本相似度)  → 按相似程度给软权重
  然后逐行归一化
```

> [!insight] 这三行才是 RADAR 在模型层面的新东西
> 报告监督天然带大量"伪负例"（绝大多数器官在绝大多数病人身上是正常的）。==normal/abnormal 标记 + 文本-文本软相似度，就是为了不让模型把"同样正常"或"同样是脂肪肝"的两个病人强行推开。==
> 预处理第三步花钱调 LLM 判 normal/abnormal，钱就花在这里。

### 分割损失

分割头的 37 通道 softmax 输出对 TotalSegmentator 的 mask（最近邻降采样到输出尺寸）算 **soft Dice**（不含背景）。它和对比损失直接相加，没有权重系数。

---

## ⑥ 训练配方

| 项 | 值 |
|---|---|
| 框架 | LAVIS 的整个子树搬进仓库后改名（`lavis/models/radar_models/`）；模型注册名 `radar_pretrain` |
| 输入 | pad 到至少 `96×256×384` → **中心裁剪** `96×256×384` → HU 钳位 → 逐体 min-max 到 [0,1] |
| HU 窗 | 旗舰（RAD-CT）**[−300, 400]**；MERLIN 分支跟随 MERLIN 的设定用 **[−1000, 1000]** |
| 优化 | `init_lr 1e-4` → cosine → `min_lr 1e-6`，warmup 3000 步（起点 1e-6），weight decay 0.05 |
| 规模 | 30 epoch，总 batch 48，fp32，seed 42 |
| 队列 | `queue_size: 0` —— ALBEF 原有的 57,600 负例队列被关掉，只用跨卡 `all_gather` 的 in-batch 负例 |
| 开关 | `radar_plus: True` 开全局对齐；`radar_ft: True` 从旗舰权重微调（只加载视觉侧，**文本编码器不加载** —— 因为中文换英文）|

微调时，全局对齐那一支的参数（`query_tokens_whole`、`attention_whole`、`vision_projs_whole`）直接**用第 0 号器官的权重初始化**。

快速验证流水线能跑（仓库自带 4 例 demo 数据，不用下全量）：

```bash
cd RADAR_train && python train.py
```

全量训练要改 `lavis/datasets/datasets/caption_datasets.py:79` 的 `vis_root`，并先用 `process_img.py` 把 MERLIN 原图重采样到 `[1,1,5]`。

---

## ⑦ 推理：零样本，靠正负提示词打分

RADAR 没有分类头。146 个征象每个都是"**这个器官的图像特征，更像阳性描述还是阴性描述**"。

```
① 整卷 → 重采样 [1,1,5] → HU 钳位 + min-max → 裁掉全零区域（z 外扩 5、面内外扩 20）
② 滑窗过分割头    roi = 96×256×384, overlap = 0.25, sw_batch_size = 1
                  各窗的 seg 概率三线性插值回原尺寸、重叠处取平均 → argmax → 全卷 mask
③ 对每个器官      以该器官 mask 为中心，裁一个 96×256×384 的窗
                  → ROI 注意力池化 → 器官特征 (256-d)
④ 对该器官的每个征象
                  text_feat = 预先算好的 [若干阴性提示词 ; 若干阳性提示词] 嵌入
                  sim = image_feat · text_featᵀ / temp
                  阳性组取均值、阴性组取均值 → softmax([neg, pos]) → 取 pos 作为该征象的分数
⑤ 写 CSV：每个征象一个阳性分数
```

- 提示词嵌入是**离线算好**的：`ckpt/infer_text_embedding_radar.pt`（旗舰）/ `infer_text_embedding_merlin.pt`，推理时不跑 BERT。每个征象是**多条提示词的集成**（prompt ensemble）。
- 任何一维超过 1000 体素的体数据会被直接跳过。
- 146 个征象名和中英对照表**硬编码在 `inference_demo.py`** 里，换征象表要改代码。

```bash
cd RADAR_inference && python inference_demo.py        # 单卡，自带一个 demo NIfTI
# → RADAR_infer_results_demo.csv
```

MERLIN 测试集上用的是 MERLIN 官方发布的提示词，保证和别的模型可比。

---

## ⑧ 146 个征象、18 个器官

从 `inference_demo.py` 的 `self.test_items` 直接数：

```
大肠 18   肝 18    肾 14    胆囊 14   小肠 13   肺 10
胰腺 10   脾 8     肾上腺 6  胃 6     膀胱 6    十二指肠 5
食管 5    主动脉 4  肋骨 3   门静脉 3  心脏 2    骶骨 1        合计 146
```

征象粒度示例：`肝_肝细胞癌`、`肝_脂肪肝`、`肝_肝内胆管扩张`、`胰腺_胰管扩张`、`大肠_阑尾炎`、`小肠_梗阻`、`主动脉_主动脉夹层`、`门静脉_栓塞`、`肺_气胸`。

---

## ⑨ 公开可查的性能数字

**仓库里能复现的（MERLIN）：**

| 模型 | 设定 | AUC |
|---|---|---:|
| RADAR（旗舰）| RAD-CT 训练，**直接**在 MERLIN 测试集上零样本 | **0.883**（21 个征象平均）|
| RADAR+ | Merlin-CT-Train 上从零训练 | 0.888（anatomy）|
| RADAR+ | 旗舰权重在 Merlin-CT-Train 上微调 | **0.918**（anatomy）/ 0.876（all）|

旗舰模型在 MERLIN 上的逐项 AUC：腹主动脉瘤 0.990、肠梗阻 0.970、脾大 0.968、胸腔积液 0.957、肾囊肿 0.943、胰腺萎缩 0.936、胆囊结石 0.919、肝脂肪变 0.892 …… 最低的两项是**肺不张 0.709** 和**骨折 0.683**。

**论文里的（内部数据，无法独立复现）：** 146 征象平均 AUC 0.913（对照视觉-语言模型 0.776）；8 个外部中心 0.895；训练时排除的急腹症 0.904；26 位放射科医生、14 个中心的 reader study，人机协同敏感度提高约 10%。

| 结论 | 证据强度 | 理由 |
|---|---|---|
| MERLIN 上 0.883 | **强** | 公开数据 + 公开权重 + 公开脚本，任何人可重跑 |
| reader study（26 人 / 14 中心）| **强** | 规模真实，Science 摘要原文 |
| 急腹症 0.904 | **强** | 训练时排除，干净的分布外测试 |
| 8 外部中心 0.895 | 中强 | 泛化信号真实；但外部中心 8/10 在浙大一院自己的体系内 |
| 146 征象平均 0.913 | 弱 | 患病率差几个数量级，均值被常见又明显的征象拉高 |

---

## ⑩ 物理层面的三条边界

```python
image[image > 400] = 400
image[image < -300] = -300
image = (image - image.min()) / (image.max() - image.min() + 1e-8)
```

| 边界 | 机制 | 后果 |
|---|---|---|
| **地板 −300 HU** | 肺实质 −700～−900 HU、空气 −1000 HU 全部钳到 −300 | 气胸与正常肺在输入里数值相同；10 个肺征象只能靠几何推 |
| **天花板 400 HU** | 钙化、骨、浓对比剂全部饱和 | "钙化"退化成"有没有饱和体素"，密度大小的信息没有了 |
| **逐体 min-max** | 归一化用的是这一卷自己的 min/max | 绝对 HU 标度不进网络 |
| **z 向各向异性** | 5 mm 层厚 + 最深 token 40×32×32 mm | 一个 8 mm 病灶 ≈ 最深 token 体积的 1/125 |

MERLIN 上最低的两项正好对上：**骨折 0.683**（天花板）、**肺不张 0.709**（地板）。

> [!insight] 这不是缺陷，是这条路线的定义
> RADAR 把 CT 当成一张**带解剖标签的灰度图**。它能到 0.913，恰恰说明大部分常见腹部征象不需要定量密度。
> ==反过来，凡是需要定量密度的（脂肪分数、碘浓度、材料组成、部分容积边界），输入里已经没有那个信息了 —— 原理上到不了，不是工程没做好。==

---

## ⑪ 依赖的健康状况

| 依赖 | 归属 | 用得多深 | 状态（2026-09-20）|
|---|---|---|---|
| **LAVIS** | Salesforce，BSD-3 | 整个子树搬进仓库改名；ALBEF 的超参原样保留 | ⚠️ **2026-09-18 已归档**，最后一次实质提交 2024-11-18 |
| **dynamic-network-architectures**（nnU-Net）| MIC-DKFZ，Apache-2.0 | 整包 vendored + 自加两个轻解码器文件 | ✅ 活跃 |
| **MONAI** | Project-MONAI，Apache-2.0 | 只用了 4 个符号：`transforms`、`dense_patch_slices` 等纯几何工具 | ✅ 活跃 |
| **3D-ResNets-PyTorch** | kenshohara，MIT | 致谢里列了，`resnet_vl.py` 在仓库里但**推理链和训练链都没有 import** | 2021-01 后无更新 |
| **TotalSegmentator v1.5.7** | 巴塞尔大学医院，Apache-2.0 | 仅离线造标签 | v1 线已停；当前 2.18.0 |
| **Qwen / DashScope** | 阿里云，商业 API | 仅离线解析报告 | 可替换为任意 LLM |

---

## ⑫ 许可

| | |
|---|---|
| GitHub 代码 | **Apache-2.0** |
| HuggingFace 权重 | **CC BY-NC-SA 4.0** —— 禁商用 + 相同方式共享 |
| MERLIN 数据 | Stanford AIMI 的数据使用协议；代码/权重 MIT |

==研究复现没问题，进产品线不行。==

---

## ⑬ 想自己跑一遍：最短路径

```
A. 只看效果（1 张 A100/H20，约 2 GB 权重）
   pip install -r requirements.txt → download_checkpoints.py → python inference_demo.py

B. 在公开数据上复现 0.883（需申请 MERLIN）
   下载 MERLIN → transform_report_to_json.py / transform_label_to_json.py
   → python inference_merlin_testset.py → python calc_metrics_merlin_testset.py

C. 在 MERLIN 上训练 RADAR+（官方用 24 卡；卡少就是慢，batch 变小会影响 in-batch 负例数量）
   下载 HF 上的 resized_masks part00-02 并合并 → process_img.py 重采样原图
   → 改 caption_datasets.py:79 → torchrun --nproc_per_node=8 train.py

D. 换成自己的数据（这一步才需要 TotalSegmentator v1.5.7 + LLM API）
   TotalSegmentator v1.5.7 → process_img_mask.py → 三个 report 解析脚本 → 同 C
```

⚠️ D 这条路对**报告语言**敏感：文本编码器要和报告语言匹配（中文 `bert-base-chinese` / 英文 `bert-base-uncased`），换语言时视觉侧权重可以继承，文本侧必须重训。

---

## 对 Shu 的工作意味着什么

**可以直接拿走的：解剖单元化。** 用现成的自动分割器把整卷 CT 切成解剖单元，所有下游量在单元上汇总 —— 这一步不含任何学习参数。几百例的材料分解数据可以照做：water/lipid/protein 分数、噪声、误差预算按解剖结构汇总，统计功效从"几百个 ROI"变成"几百 × N 个单元"，同时去掉手画 ROI 的读者间变异。

**不能拿走的：它对分割精度的态度。** RADAR 把 mask 池化到 40×32×32 mm 照样工作，因为它只要"这堆 token 属于肝"。材料分解里，==边界就是部分容积效应，边界就是信号本身==。

**值得抄的是软目标的思路。** "同样正常的两例不该互相排斥" —— 任何用弱标签做对比学习的场景都会遇到同一个问题。

**报告监督到不了定量物理量。** 146 个征象里有"脂肪肝"，输出是一个与报告文字一致的概率。没有任何一份放射报告会写"脂肪分数 0.62"。

---

## 公开材料里查不到的

- 扫描仪型号、kVp、对比剂期相、重建核、原始层厚分布
- RAD-CT 的时间跨度、来自哪几家医院、伦理批件号
- 146 个征象各自的阳性例数
- 对照的视觉-语言模型具体是哪几个
- 训练实际用时、显存占用
- 旗舰模型训练时是否开了 `radar_plus`（发布的 `radar_config.yaml` 是 MERLIN 分支的配置）

---

## See Also

- [radar-vs-medsam.md](radar-vs-medsam.md) —— 与 MedSAM 的关系
- [grassroots-network.md](grassroots-network.md) —— 外部验证中心
- [../data/raw/dependency-stack-evidence.md](../data/raw/dependency-stack-evidence.md) —— 依赖核查的原始命令与输出
- [../README.md](../README.md)
