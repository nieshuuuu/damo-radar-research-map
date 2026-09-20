# RADAR 技术栈依赖图 × 人事血统

> 方法：**不读新闻稿、不读论文摘要**。每一条都来自直接拉仓库树、读源码行、调 PyPI/Crossref/PubMed/arXiv/GitHub API。命令与行号随文附。
> 核对日期：**2026-09-20**。RADAR 仓库快照：`alibaba-damo-academy/damo-radar`，created `2026-07-03T06:30:03Z`，last push `2026-09-18T01:50:18Z`，357 stars，Apache-2.0。
> ⚠️ 本页**推翻了** [radar-technical-teardown.md](radar-technical-teardown.md) 的两条结论（视觉编码器、文本编码器），见 §⑦。

---

## 一句话

RADAR 的技术栈是**四个国家的四个开源项目的沉积层**：加州的对比学习框架（已停更、已归档）、德国的分割架构库、瑞士的器官分割器、日本的 3D 卷积（**根本没用上**）。
而它公开发布的那条**可复现**路径，从头到尾跑在**斯坦福的数据**上。

> [!insight] 真正的发现不在依赖表里，在依赖表**背后的数据**
> 大家都以为 MERLIN 只是 RADAR 的"外部测试集"。==读 `docs/TRAINING.md` 第 3 行就会发现：RADAR 公开放出来能训的那个模型，是在 Merlin-CT-Train 上从零训的。== 中国团队发在 Science 上的腹部 CT 通才模型，其开源复现形态是一个**美国数据训练的模型**。见 §⑤。

---

## ① 依赖图（实测，不是 README 抄的）

```
                        ┌──────────────────────────────────────────┐
                        │  RADAR  (alibaba-damo-academy/damo-radar) │
                        │  Apache-2.0 代码 / CC BY-NC-SA-4.0 权重    │
                        └───────────────┬──────────────────────────┘
                                        │
   ┌────────────────┬───────────────────┼──────────────────┬─────────────────────┐
   │ 训练框架        │ 网络架构           │ 几何变换          │ 监督信号生产         │
   ▼                ▼                   ▼                  ▼                     ▼
┌────────┐   ┌───────────────┐   ┌─────────────┐   ┌──────────────┐   ┌──────────────────┐
│ LAVIS  │   │ dynamic-      │   │   MONAI     │   │ TotalSegment-│   │ DashScope/Qwen   │
│ BSD-3  │   │ network-arch  │   │ Apache-2.0  │   │ ator v1.5.7  │   │ (商业 API)        │
│        │   │ Apache-2.0    │   │             │   │ Apache-2.0   │   │                  │
│Salesf- │   │ MIC-DKFZ      │   │ MONAI 联盟   │   │ 巴塞尔大学医院 │   │ 阿里云(非达摩院)  │
│orce AI │   │ 海德堡         │   │ NVIDIA+KCL  │   │ Wasserthal   │   │ 通义千问          │
│ 🇺🇸      │   │ 🇩🇪            │   │ 🇺🇸🇬🇧         │   │ 🇨🇭           │   │ 🇨🇳               │
└───┬────┘   └───────┬───────┘   └──────┬──────┘   └──────┬───────┘   └────────┬─────────┘
    │                │                  │                 │                    │
 深度:极深         深度:整包 vendored   深度:**4 个符号**   深度:离线教师         深度:两档调用
 ALBEF 全套        + 自己加了 2 个文件   仅几何变换          不是运行时依赖        qwen_plus/qwen_max
    │                │                                     │
    │                │                                     └──► nnunet-customized==1.2
    │                │                                           = wasserth 自己 fork 的
    │                │                                             nnU-Net v1，冻结在
    │                │                                             2022-03-18
    │                │                                                   │
    │                └───────────────────────┬───────────────────────────┘
    │                                        ▼
    │                            ==DKFZ 的代码被依赖了两次==
    │                            直接一次（架构库）
    │                            间接一次（TotalSeg→nnU-Net fork）
    ▼
┌─────────────────────────────────────┐
│ 3D-ResNets-PyTorch (MIT, Kensho Hara)│
│  ❌ 在 README 里被致谢               │
│  ❌ resnet_vl.py 确实在仓库里         │
│  ✅ **但从未被 import**  → 见 §⑦     │
└─────────────────────────────────────┘
```

### 四个致谢对象的体检表

README 第 64–71 行列的四个，逐个查证：

| 项目 | 归属 | 创建 | stars | 许可 | **健康状态（2026-09-20）** |
|---|---|---|---:|---|---|
| **LAVIS** | Salesforce | 2022-08-24 | 11,266 | BSD-3 | ⚠️ ==**已归档**== 2026-09-18，最后一次真实代码提交 **2024-11-18** |
| **nnU-Net** | MIC-DKFZ（德国癌症研究中心，海德堡）| 2019-04-17 | 8,898 | Apache-2.0 | ✅ 活跃，last push 2026-09-14 |
| **MONAI** | Project-MONAI 联盟 | 2019-10-11 | 8,696 | Apache-2.0 | ✅ 活跃，last push 2026-09-18 |
| **3D-ResNets-PyTorch** | kenshohara 个人 | 2017-09-14 | 4,038 | MIT | ⚠️ ==最后一次 push **2021-01-20**==，死了 5 年 8 个月 |

```bash
gh api repos/salesforce/LAVIS --jq '{created,pushed:.pushed_at,archived,stars:.stargazers_count}'
```

> [!insight] LAVIS 归档的日期，和 RADAR 最后一次 push 是**同一天**
> ```
> 2026-09-18T01:50:18Z   damo-radar   Wanxing Chang  "Update README.md"   ← RADAR 上线
> 2026-09-18T09:59:39Z   LAVIS        Jim Jagielski  "This repo is ARCHIVED"
> ```
> 相隔 8 小时 9 分钟。==纯属巧合 —— 但这个巧合很能说明位置：== RADAR 发布的那一刻，它所建立于其上的框架被上游正式宣告停止维护。
> 更要紧的是 **LAVIS 的最后一次功能性提交是 2024-11-18**。RADAR 是把一个 2022 年的框架用到 2026 年，而这个框架在中途就已经实质性停更了。

---

## ② 每个依赖到底有多深 —— grep 出来的，不是猜的

> [!strategy] "致谢了"和"依赖"是两件事，必须用 import 来量
> 四个致谢在 README 里看起来是平级的。实测深度差三个数量级。

### LAVIS —— 最深的一条，代码里还留着 Salesforce 的版权头

`RADAR_train/lavis/models/radar_models/radar_pretrain.py` 开头原文：

```python
"""
 Copyright (c) 2022, salesforce.com, inc.
 All rights reserved.
 SPDX-License-Identifier: BSD-3-Clause
"""
```

RADAR 把整个 `lavis/` 子树搬进了自己的仓库（`common/` `datasets/` `models/` `processors/` `runners/` `tasks/` 全套），把 ALBEF 的模型文件改名成 `radar_models/`。这不是"调用一个库"，是 ==**fork 之后改名**==。

ALBEF 的全部超参都原样保留（`radar_pretrain.py` 行号）：

| 项 | 值 | 行 | 出处 |
|---|---|---|---|
| `momentum` | 0.995 | 73 | ALBEF 动量编码器默认值 |
| `temp` | `nn.Parameter(0.07 * ones)` | 94 | CLIP/ALBEF 的可学习温度 |
| `temp.clamp_` | [0.001, 0.5] | 279 | ALBEF 原样 |
| `alpha` | 0.4 | 71 / config | momentum distillation 权重 |
| `queue_size` | **代码默认 57600**，config 设成 **0** | 453 / config | 57600 是 ALBEF 原值 → ==RADAR 是主动关掉队列的== |
| `MomentumDistilationMixin` | 从 `lavis.models.base_model` 导入 | 20 | |

RADAR 自己加的是**两个对比损失并行**：

```
line 160  # define whole image contrastive learning
line 256  # --> anatomy-wise contrastive learning
```

==这两行才是论文的全部模型贡献。== 其余是 ALBEF。

### nnU-Net —— 整包 vendored，而且**动了刀**

`THIRD_PARTY_LICENSES.md` 第 47 行把这一项写成 `## nnU-Net / dynamic-network-architectures`，同时指向 `MIC-DKFZ/nnUNet` 和 `MIC-DKFZ/dynamic-network-architectures`。后者才是真依赖。

对比上游文件表（`gh api repos/MIC-DKFZ/dynamic-network-architectures/git/trees/main?recursive=1`）与 RADAR 的 vendored 副本：

| 文件 | 上游有 | RADAR 有 | 说明 |
|---|:---:|:---:|---|
| `architectures/resnet.py` `unet.py` `vgg.py` | ✓ | ✓ | 原样搬 |
| `building_blocks/*`（8 个）| ✓ | ✓ | 原样搬 |
| `architectures/unet_lightdecoder.py` | ✗ | ✅ | ==RADAR 自己加的== |
| `building_blocks/unet_decoder_light.py` | ✗ | ✅ | ==RADAR 自己加的== |
| `architectures/resnet_vl.py` | ✗ | ⚠️ | RADAR 自己加的，但**从未被 import**（§⑦）|

> [!insight] RADAR 对 nnU-Net 架构库做的唯一改动，是**把解码器砍薄**
> `vision_branch.py` 的 `arch_kwargs`：
> ```python
> "n_conv_per_stage":          [2, 2, 2, 2, 2, 2]   # 编码器：标准 nnU-Net
> "n_conv_per_stage_decoder":  [1, 1, 1, 1, 1]      # 解码器：砍到一半
> ```
> ==这是"分割精度不重要"这个判断在架构层面留下的指纹。== 他们不需要一个好的分割器，只需要一个能正确贴标签的粗分割器 + 一组好的编码器特征。于是主动放弃解码器容量换速度。
> 这条比 [radar-technical-teardown.md](radar-technical-teardown.md) §⑤ 的 max-pool 论证更早一层：**解码器在设计时就被判定为次要**。

### MONAI —— 全仓库只用了 **4 个符号**

```bash
grep -rn "monai" RADAR_inference/*.py RADAR_train/lavis/processors/*.py \
                 RADAR_inference/dynamic_network_architectures/*.py
```

全部命中：

```
inference_demo.py:12      from monai import transforms
inference_demo.py:13      from monai.data.utils import dense_patch_slices
radar_processors.py:9     from monai import transforms
vision_branch.py:19       from monai.utils import deprecated_arg
```

用到的类：`transforms.Resized`、`SpatialPadd`、`DivisiblePadd`、`dense_patch_slices`。

> [!strategy] 量一下再下结论
> ==MONAI 在 RADAR 里是一个**几何变换工具箱**，不是建模框架。== 它提供的是"重采样、补边、滑窗切片"这三件事。
> 这一点对 §④ 的"NIH 血统链"判定是**决定性的** —— 你不能用一个只被用来调 `Resized` 的库，去论证某条学术谱系。

### 3D-ResNets-PyTorch —— 致谢了，但是死代码

见 §⑦。

---

## ③ TotalSegmentator：作者、机构、版本史（全部复核）

### 人与机构

| | |
|---|---|
| 作者 | **Jakob Wasserthal**（PyPI `author` 字段：`Jakob Wasserthal <jakob.wasserthal@usb.ch>`）|
| 机构 | **巴塞尔大学医院 放射与核医学科**（University Hospital Basel, Clinic of Radiology and Nuclear Medicine, Petersgraben 4, 4031 Basel, Switzerland）|
| 论文 | *Radiology: Artificial Intelligence* **5(5)**, 2023-09, DOI [10.1148/ryai.230024](https://doi.org/10.1148/ryai.230024)，标题 "TotalSegmentator: Robust Segmentation of 104 Anatomic Structures in CT Images" |
| 作者数 | 12 人，Crossref 元数据里 **全部 12 人的 affiliation 都是同一个巴塞尔地址** —— 这是一篇纯单中心论文 |
| 仓库 | `wasserth/TotalSegmentator`，个人账号（不是机构 org），created 2022-01-19，3,007 stars，Apache-2.0 |

```bash
curl -sL "https://api.crossref.org/works/10.1148/ryai.230024"
curl -sL "https://pypi.org/pypi/TotalSegmentator/json"
```

> [!insight] 一个人的个人仓库，成了全球医学影像 AI 的公共基础设施
> RADAR（阿里，40 作者，Science）和 MedSAM 那条线的 `FastSegmentator`（多伦多）都依赖它。==而它的 bus factor 是 1：== 1022 次提交里 wasserth 占 1022 中的 1022 之下的绝对多数，第二名 `jamesobutler` 只有 14 次。

### 版本史 —— 任务里给的 5 个日期，逐个核

```bash
curl -sL "https://pypi.org/pypi/TotalSegmentator/json" | python3 -c "..."   # upload_time_iso_8601
```

| 待核日期 | PyPI 实测 | 判定 |
|---|---|:---:|
| v1.5.6 = 2023-05-16 | `2023-05-16  1.5.6` | ✅ |
| v2.0.0 = 2023-09-26 | `2023-09-26  2.0.0` | ✅ |
| v1.5.7 = 2023-10-17 | `2023-10-17  1.5.7` | ✅ |
| 当前 PyPI 2.18.0 = 2026-08-12 | `2026-08-12  2.18.0`，`info.version = 2.18.0` | ✅ |
| GitHub `v3.0.0-weights` = 2026-09-07 | release `published_at 2026-09-07` | ✅ |

**五个日期全部属实。** 完整发布序列（36 个版本）：

```
2022-08-04 1.0 …… 2023-05-16 1.5.6
2023-09-26 2.0.0   ← v2 主线开始
2023-10-17 1.5.7   ← RADAR 钉的这个，比 v2.0.0 晚 3 周，是 v1 的最后一个补丁
2023-10-19 2.0.4 …… 2025-01-17 2.5.0 …… 2026-08-12 2.18.0
```

权重 tag：`v1.5.6-weights` 与 `v2.0.0-weights` **同一天发布（2023-09-21）** —— v1 的权重是 v2 出来时才补挂的 tag。

### ⚠️ 重要更正：所谓的 "v3" 目前**只有权重，没有代码版本**

任务描述把 `v3.0.0-weights` 当成 v3 发布。实测：

```bash
gh api repos/wasserth/TotalSegmentator/git/ref/tags/v3.0.0 --jq '.object.sha'
# → a0d35d5..., commit date 2026-09-07T11:47:41Z, message "update prepare weight for release"

curl -sL ".../TotalSegmentator/v3.0.0/setup.py" | grep version
# → version='2.18.0'          ←←← v3.0.0 这个 tag 里，代码版本号还是 2.18.0

curl -sL ".../TotalSegmentator/v3.0.0/CHANGELOG.md" | head -3
# → "## Master"  ... 没有任何 v3 条目

curl -sL ".../master/resources/improvements_in_v3.md"
# → 404
```

==截至 2026-09-20，"TotalSegmentator v3" 是一组新权重 + 一个 tag，没有代码版本、没有 changelog、没有 PyPI 包、没有说明文档。== 任何关于"v3 改了什么"的描述目前都无据可依。**不要编。**

### v1 → v2 改了什么（有据：`resources/improvements_in_v2.md`）

| 类别 | 内容 |
|---|---|
| **破坏性变更** | multilabel 输出的**类别顺序变了**（`--v1_order` 可回退但拿不到新类）；==「all models have been retrained」→ 分割结果与 v1 必然不同==；heart chambers 和 face 移出 `total` 任务，`total` 只保留一个整体 `heart` 类 |
| **新增 33 类** | `total`：skull, thyroid_gland, prostate, brachiocephalic_*, common_carotid_*, atrial_appendage_left, subclavian_*, vertebrae_S1, sternum, costal_cartilages, pulmonary_vein, superior_vena_cava, kidney_cyst_*, spinal_cord；新任务 `appendicular_bones`（四肢骨 11 类）、`tissue_types`（subcutaneous_fat / skeletal_muscle / torso_fat）、`vertebrae_body` |
| **许可分叉** | ⚠️ `appendicular_bones` / `tissue_types` / `face` / `heartchambers_highres` / `vertebrae_body` **仅限非商用**；其余任务可商用 |
| **标注系统误差修正** | femur, humerus, hip, heart chambers, **aorta, liver, spleen, kidney** |
| **训练数据** | 1139 → **1559** 例（新增：全身、手足、头部、腹腔出血、GE 机器与其他机构）。⚠️ 原文注明「The public dataset does not contain these additional subjects」—— 公开数据集拿不到这批增量 |
| **公开数据集** | 104 → **117** 类，去掉心腔类，defacing 更轻，元数据更全（机器、病理）|
| **速度** | `--roi_subset` 先跑低分辨率定位再裁剪，GPU 快 5×，CPU 快 32× |
| **仍未解决（原文 still open problems）** | 肋骨近脊柱端总缺一小截；肋软骨端边界无定义；==**colon / small_bowel 的 GT 有时候就是错的**，因为结肠太乱、和小肠分不开== |

> [!strategy] 最后一行要对到 RADAR 的临床声明上
> RADAR 的 146 个征象里 **大肠占 18 个（最多）、小肠 13 个**（见 [radar-technical-teardown.md](radar-technical-teardown.md) §③），四种病理确诊癌之一是**结直肠癌**。
> ==而它的解剖定位器，官方文档在 v2 时点名承认 colon/small_bowel 的金标准本身就不可靠，且明确列为"未解决"。==
> 这不否定 RADAR 的结果（max-pool 到 40×32×32 mm 之后边界误差被吃掉，见 §⑦"池化即步长"），但它意味着：**RADAR 在结肠/小肠上的 anatomy-wise 监督，其空间归属的可靠性低于其他器官**，而这两个器官恰好占了征象表的 21%。

### v2.x 里对 Shu 有直接用处的两条（顺带）

- `2.13.0`（2026-03-17）：更新 `coronary_arteries` 任务为 **skeleton-recall 模型**，旧版降级为 `coronary_arteries_LEGACY`；新增 `liver_lesions` / `liver_lesions_mr`。→ 与 PCAT 自动中心线那条线直接相关。
- `2.15.0`（2026-07-01）：`--higher_order_resampling`（原文「This makes segmentations a lot better!」）、`--report <path.json>` 运行清单（软件/模型版本、设备、任务、类别、耗时、输出文件）。→ 后者正好是可复现流水线要的 provenance。
- `2.18.0`（2026-08-12）：加了 MCP server。

### v1.5.7 的依赖，以及它为什么在 2026 年装不上

`v1.5.7/setup.py`：

```python
'nnunet-customized==1.2',      # 注释原文：nnunet @ git+https://github.com/wasserth/nnUNet_cust@working_2022_03_18
'batchgenerators==0.21',
'SimpleITK', 'nibabel>=2.3.0', 'fury', 'xvfbwrapper', 'rt_utils', 'p_tqdm',
```

==`nnunet-customized` 是 Wasserthal **自己 fork 的 nnU-Net v1，冻结在 2022-03-18**。== 所以 DKFZ 的代码在 RADAR 的依赖树里出现了两次：一次是直接 vendored 的 `dynamic_network_architectures`（2022 年之后的新包），一次是 TotalSegmentator 内部那个 2022-03-18 的私有 fork。两个版本互不兼容，且都与 RADAR 自己 pin 的 `transformers==4.25` 不在一个环境里。

✓ 但这只影响"用自己的数据从头预处理"这条路。跑发布的 checkpoint 完全不需要装 TotalSegmentator（README 原文，见 teardown §⑤更正）。

---

## ④ MONAI × Holger Roth × NIH：链条**部分成立，但作为"依赖"论证是过度解读**

任务提出的假设：*"MONAI 的核心开发者里有 Holger Roth，他与 NIH/Le Lu 有关系 → RADAR 依赖的基础设施指回同一个 NIH 实验室。"*
逐段核，然后裁决。

### (a) Holger Roth 是不是 MONAI 核心开发者？—— **是贡献者，不是核心**

```bash
gh api --paginate repos/Project-MONAI/MONAI/contributors?per_page=100
```

296 位贡献者，排名：

```
 1. wyli            833   ← Wenqi Li (NVIDIA)
 2. Nic-Ma          710   ← Nic Ma (NVIDIA)
 3. KumoLiu         232
 4. rijobro         187   ← Richard Brown (KCL)
 5. yiheng-wang-nv  133
 …
18. holgerroth       20   ←←← 20 次提交
```

MONAI 框架论文（arXiv [2211.02701](https://arxiv.org/abs/2211.02701)，2022-11-04，**57 位作者**）里：

```
 1. M. Jorge Cardoso   ← KCL，第一作者
 2. Wenqi Li           ← NVIDIA
 4. Nic Ma
…
46. Holger R. Roth     ←←← 57 人里第 46 位
47. Daguang Xu
…
57. Andrew Feng
```

判定：==Holger Roth 在 MONAI 里是**中游贡献者**（提交排 18/296，署名排 46/57），不是架构决策者。== "核心开发者"这个说法不成立。

### (b) Roth 与 Le Lu / NIH 的关系？—— **极其扎实，比想象的更深**

```bash
curl "https://api.openalex.org/works?filter=author.id:A5043710204&per-page=200"
```

Holger R. Roth（OpenAlex `A5043710204`，276 篇，23,612 引，last known institution = **NVIDIA**）与 Le Lu 共同署名 **35 篇**，全部集中在 **2014–2019**，全部在 **NIH Clinical Center / Ronald M. Summers 组**。代表作：

| 年 | 论文 | 作者序 |
|---|---|---|
| 2015 | **DeepOrgan**: Multi-level Deep CNNs for Automated Pancreas Segmentation | Roth, **Le Lu**, Farag, Shin, Liu, Turkbey, **Summers** |
| 2016 | Deep CNNs for Computer-Aided Detection: Architectures, Dataset Characteristics and Transfer Learning（IEEE TMI）| Shin, Roth, Gao, **Le Lu**, **Ziyue Xu**, Nogues, Yao, Mollura, **Summers** |
| 2018 | Spatial aggregation of HNN for automated pancreas localization and segmentation（Med Image Anal）| Roth, **Le Lu**, Lay, **Adam P. Harrison**, Farag, Sohn, **Summers** |

> [!insight] 注意 2016 那篇里的 **Ziyue Xu**
> 他同时是 **MONAI 论文的第 13 位作者**，现在也在 NVIDIA。==所以从 NIH Clinical Center 流向 NVIDIA/MONAI 的不是一个人，是一条小队伍。==
> 而 **Adam P. Harrison** 后来去了平安 PAII，和 Le Lu 同路。同一个组，两个出口。

### (c) 这条链能不能用来论证"RADAR 的基础设施指回 NIH"？—— **不能。这是过度解读。**

三条反驳，从弱到强：

① **Roth 不是 MONAI 的架构决策者**（(a) 已证）。

② **RADAR 对 MONAI 的依赖只有 4 个符号，全是几何变换**（§② 已证）。
   ==用 `transforms.Resized` 去论证一条学术谱系，等价于说"因为我用了 numpy，所以我继承了 Travis Oliphant 的血统"。==

③ **最致命的一条：Le Lu 根本不是 RADAR 的作者。**
   RADAR 40 位作者（[authors-affiliations.md](authors-affiliations.md)）里没有 Le Lu，也没有 Ke Yan。

### (d) 但是 —— 真正的 NIH 链条存在，而且**不需要绕 MONAI**

把搜索空间从"基础设施"换成"人"，链条立刻短得多、硬得多：

```
NIH Clinical Center · Ronald M. Summers 组（2014–2020）
   ├── Holger Roth ──────► NVIDIA（MONAI / Clara）          ← 与 RADAR 无关
   ├── Ziyue Xu ─────────► NVIDIA（MONAI 论文 #13）          ← 与 RADAR 无关
   ├── Xiaosong Wang ────► （DeepLesion 二作）
   ├── Adam P. Harrison ─► 平安 PAII
   ├── Le Lu ────────────► 平安 PAII ──► 阿里达摩院
   │                                        │
   │                                        └─► Med-Query (IEEE JBHI 2024)
   │                                            Heng Guo · **Jianfeng Zhang** · Ke Yan · Le Lu · Minfeng Xu
   │                                                            │
   │                                                            └─► RADAR #37 ✅
   └── Ling Zhang ───────► 阿里达摩院（华盛顿特区）──────────────────► RADAR #39 ✅
```

**Ling Zhang 那一支是这次新查到的**（PubMed）：

```bash
esearch db=pubmed term="(Zhang L[au]) AND (Lu L[au]) AND (Summers RM[au])"
```

| PMID | 期刊/年 | 完整作者表 |
|---|---|---|
| **29408791** | IEEE TMI 2018 | **Ling Zhang** · Le Lu · Ronald M Summers · Electron Kebebew · Jianhua Yao |
| **31562074** | IEEE TMI 2020 | **Ling Zhang** · Le Lu · Xiaosong Wang · Robert M Zhu · Mohammadhadi Bagheri · Ronald M Summers · Jianhua Yao |

共同作者集合（Summers + Jianhua Yao + Xiaosong Wang + Bagheri + Kebebew）**唯一指向 NIH Clinical Center 影像组**。
⚠️ 诚实标注：PubMed 这两条记录的 `AffiliationInfo` 字段**全部为空**，所以"Ling Zhang 当时署名 NIH"是**由共同作者集合推断的**，不是直接读到的。

> [!strategy] 裁决
> ❌ **"RADAR 依赖的基础设施指回同一个 NIH 实验室" —— 过度解读。** MONAI 这条路走不通：Roth 不是核心，依赖不到 4 个符号，Le Lu 不是 RADAR 作者。
> ✅ **"RADAR 的 AI 侧资深作者出自同一个 NIH 实验室" —— 成立，且有两条独立证据。** Ling Zhang（RADAR #39，达摩院华盛顿特区）与 Summers 组直接共同发表；Jianfeng Zhang（RADAR #37）与 Le Lu、Ke Yan 在 Med-Query 上直接共同署名。
> ==把"基础设施"的说法换成"人事"的说法，论证就从站不住变成很硬。这个替换本身就是结论。==
> 💡 顺带：**RADAR #39 Ling Zhang 与 #20 Yingda Xia 的单位都写作"达摩院 · Washington DC"** —— 达摩院在美国有一个实体节点，而它的人来自 NIH 隔壁（Bethesda 到 DC 15 公里）。这不是巧合，是选址。

---

## ⑤ MERLIN：不只是外部测试集，==是 RADAR 全部公开可复现性的载体==

### 数据集身份（全部核实）

| 项 | 值 | 出处 |
|---|---|---|
| 正式名 | Merlin: a computed tomography vision–language foundation model and dataset | PubMed 41781626 |
| 期刊 | ***Nature* 652:1318–1328**，2026 | Crossref 10.1038/s41586-026-10181-8 |
| 预印本 | arXiv [2406.06512](https://arxiv.org/abs/2406.06512)（2024-06）| |
| 作者数 | **40 人，全部斯坦福** | PubMed 原始 XML |
| 一作 | **Louis Blankemeier**（Stanford EE + AIMI + Radiology）| |
| 末位通讯 | **Akshay S. Chaudhari**（AIMI / Radiology / Biomedical Data Science / Cardiovascular Institute / Weill Cancer Hub West）| |
| 其他要角 | #37 **Curtis P. Langlotz**（AIMI 主任）、#39 **Sergios Gatidis** | |
| 数据规模 | **15,331 例腹部 CT**（>600 万张图）+ **>180 万条 EHR 诊断码** + **>600 万 token 报告** | 摘要原文 |
| 测试规模 | 内部 5,137 例；外部 **44,098 例**（3 个独立中心 + 2 个公开数据集）| 摘要原文 |
| 任务面 | 6 类任务 / 752 个具体任务：30 征象零样本、692 表型、跨模态检索、5 年慢病预测（6 病）、报告生成、**20 器官 3D 分割** | 摘要原文 |
| 代码/权重许可 | **MIT**（`github.com/StanfordMIMI/Merlin`，`huggingface.co/stanfordmimi/Merlin`）| |
| 数据分发 | Stanford AIMI Shared Datasets，id `60b9c7ff-877b-48ce-96c3-0194c8205c40` | RADAR `docs/INFERENCE.md:48` |

⚠️ **未核实**：AIMI 的数据使用协议（DUA）原文我这一轮没读到（页面只返回导航壳）。CT 影像本身是否需要签署 DUA、是否限制商用，**不要当成已知**。

### ⭐ 新发现：RADAR 公开的那个可训练模型，训练集是 MERLIN

`docs/TRAINING.md` **第 3 行原文**：

> "This document covers training RADAR/RADAR+ on **Merlin-CT-Train set** from scratch or fine-tuning from pretrained checkpoint"

同文档的权重表：

| checkpoint | 说明原文 |
|---|---|
| `checkpoint_radar_pretrain.pth` | "RADAR pre-trained checkpoint on **RAD-CT**" ← 私有的浙大 42 万例中文语料 |
| `checkpoint_radar_plus.pth` | "A RADAR+'s checkpoint **trained from scratch on Merlin-CT-Train set**" ← 公开可复现的那个 |

仓库里**实际躺着的 MERLIN 产物**（`gh api .../git/trees/main?recursive=1`）：

```
data/merlin_data_train_demo/resized_images/{AC4214dbd,AC4240fff,AC4242a2f,AC4242a55}.nii.gz
data/merlin_data_train_demo/resized_masks/  同上 4 例
ckpt/merlin_report_organ_report_v1.json      ← Qwen 解析出来的器官级报告
ckpt/merlin_report_organ_normal_v1.json      ← Qwen 判的正常/异常
ckpt/infer_text_embedding_merlin.pt
RADAR_inference/inference_merlin_testset.py
RADAR_inference/calc_metrics_merlin_testset.py
RADAR_train/infer_merlin_anatomy.py
RADAR_train/infer_merlin_whole.py
results/RADAR_infer_results_MerlinTestset.csv
```

预处理脚本的参数名直接写死了 merlin（`docs/PREPROCESS.md`）：

```bash
python process_img_mask.py --src-dir /path/to/totalsegmentator_masks \
                           --root-dir /path/to/merlin_data_root
```

他们还在 HuggingFace 上发布了**自己跑出来的 MERLIN 训练 mask**，分 `part00/part01/part02` 三包。

> [!insight] 三句话把这件事说完
> ① ==RADAR 发布的那批 TotalSegmentator v1.5.7 mask，是跑在**斯坦福的 CT** 上的。==
> ② ==RADAR 用 **阿里云的 Qwen**，解析的是**斯坦福的英文放射报告**。==
> ③ ==一个中国团队发在 *Science* 上的旗舰模型，其唯一开源可复现的训练形态，建立在一个美国数据集上。==
>
> 为什么必须这样？因为 RAD-CT（浙一 + 协作网络的 42 万例）**不可能放出来**。机构准入是这条路线的护城河（[radar-vs-medsam.md](radar-vs-medsam.md) §⑥"可扩散性"那一行），而护城河的代价是**旗舰模型不可复现**。
> 于是他们做了一件很聪明的事：==用一个公开的、合法的、同任务的美国数据集，把整条流水线**演示**一遍。== 你复现不了 RADAR，但你能复现"造 RADAR 的方法"。
> 💡 这和 Slomka EAT pipeline 的教训是同一条：**他们发布的不是模型，是评估/复现的形式。**

---

## ⑥ Qwen / DashScope：==不是达摩院，是阿里云==

### 代码里的两档调用（行号）

| 脚本 | 行 | 模型 | 用途 |
|---|---:|---|---|
| `check_organ_mention.py` | 40 | `dashscope.Generation.Models.**qwen_plus**` | 判断报告有没有提到某个器官 |
| `report_parsing.py` | 43 | `dashscope.Generation.Models.**qwen_max**` | 抽取器官级描述 |

```python
# check_organ_mention.py:39-40
resp = dashscope.Generation.call(
    model=dashscope.Generation.Models.qwen_plus, prompt=prompt
)
# report_parsing.py:42-43
resp = dashscope.Generation.call(
    model=dashscope.Generation.Models.qwen_max,
```

两个脚本第 70 行都是 `dashscope.api_key = ""  # using your own key`。

> [!insight] 两档模型 = 一次成本工程，而且暴露了流水线的形状
> **第一步是过滤，第二步是理解。** 器官提及判定（36 个器官 × 42 万份报告 ≈ 1500 万次调用）用便宜的 `qwen_plus`；只有过了滤的那部分才送贵的 `qwen_max` 去做结构化抽取。
> ==这说明 LLM 标注的成本在他们的量级上是**真实约束**，不是"反正很便宜"。== [radar-vs-medsam.md](radar-vs-medsam.md) §⑥ 说 RADAR 的单位监督成本是"调一次 LLM 的 token 费"—— 这里可以补一句：他们连这个 token 费都做了分级优化。
> ⚠️ 我只核了这两个脚本。`report_parsing_normal.py` 用哪一档，本轮**未读**。

### 归属：Qwen ≠ 达摩院

任务假设里写的是"Qwen 与达摩院/阿里云的关系"。实测结果需要**纠正前半句**：

| 证据 | 原文 | 结论 |
|---|---|---|
| `QwenLM/Qwen` README | "the official repo of Qwen (通义千问) chat & pretrained large language model **proposed by Alibaba Cloud**" | 阿里云 |
| PyPI `dashscope` 元数据 | `author: Alibaba Cloud`，`author_email: dashscope@alibabacloud.com`，`home_page: https://dashscope.aliyun.com/` | 阿里云 |
| Qwen Technical Report | arXiv [2309.16609](https://arxiv.org/abs/2309.16609)，2023-09-28，48 作者 | |
| 首发 | Qwen-7B / Qwen-7B-Chat，2023-08-03 | |

```bash
curl -sL "https://pypi.org/pypi/dashscope/json"   # → Alibaba Cloud, dashscope.aliyun.com
```

> [!strategy] 这个区分对"血统"这条线很重要
> **达摩院（DAMO Academy）** 和 **阿里云通义（Tongyi / Alibaba Cloud）** 是阿里集团内的**两个不同单元**。RADAR 的作者挂的是达摩院；Qwen 挂的是阿里云。
> ==所以 RADAR 调 Qwen，在组织结构上是**跨事业部调用商业 API**，不是"自家实验室用自家模型"。== 它和 `dashscope.api_key = "YOUR_KEY"` 这行代码的含义是一致的：这是一个**外部服务接口**，文档里明说 "any other LLM can be substituted"。
> 🚩 不要把"都是阿里"简化成"都是达摩院"。这正是人事血统调查里最容易出的那类错 —— 把机构名当成实验室名。

---

## ⑦ 模型细节技术审计：7 项待核，**5 项成立、1 项需补全、1 项推翻**

| # | 待核声明 | 判定 | 证据 |
|---|---|:---:|---|
| 1 | LAVIS 的 `radar_pretrain` 架构 | ✅ | `radar_config.yaml: arch: radar_pretrain`；`RADAR_train/lavis/models/radar_models/radar_pretrain.py` 顶部 Salesforce BSD-3 版权头 |
| 2 | BERT-base 文本编码器 | ⚠️ **需补全** | 见下 (a) |
| 3 | **3D ResNet 视觉编码器** | ❌ **推翻** | 见下 (b) |
| 4 | `alpha=0.4`（ALBEF momentum distillation）| ✅ | config + `radar_pretrain.py:71,451`；配套 `momentum=0.995` (73)、`temp=0.07` 可学习 (94)、clamp [0.001,0.5] (279) |
| 5 | `queue_size=0` | ✅ 且**更强** | config 写 0；`radar_pretrain.py:453` 代码默认是 **57600**（ALBEF 原值）→ ==是主动关掉的，不是忘了设== |
| 6 | 24 GPU / batch 48 / 30 epoch | ✅ 但**有范围限定** | `radar_config.yaml`：`batch_size_train: 2  # we using 24 GPU with a total batch size of 48`，`max_epoch: 30`，`seed: 42`，`amp: False`。⚠️ ==这是 **MERLIN** 训练配置（§⑤），不一定是 RAD-CT 旗舰模型的配置== |
| 7 | HU 窗 [−300,400] → 逐体 min-max；重采样 [1,1,5] mm；pad 到 [96,256,384] | ✅ | `inference_demo.py:193-195`（窗+归一化）、`:179 ref_spacing=(1.0,1.0,5.0)`、`:136 SpatialPadd(spatial_size=(96,256,384))`、`:407 roi_size=(96,256,384)` |

### (a) ⚠️ 补全：有**两个** BERT，不是一个

| 文档 | 表格里写的 | 对应的 checkpoint |
|---|---|---|
| `docs/INFERENCE.md:23` | `bert-base-**chinese**` → `ckpt/bert-base-chinese` | `checkpoint_radar_pretrain.pth`（RAD-CT，**旗舰**）|
| `docs/TRAINING.md` 支持文件表 | `bert-base-**uncased**` → `ckpt/bert-base-uncased` | `checkpoint_radar_plus.pth`（Merlin-CT-Train）|
| `radar_config.yaml` | `med_config_path: "../ckpt/bert-base-uncased/config.json"` | ← 这是 MERLIN 那一支 |

==[radar-technical-teardown.md](radar-technical-teardown.md) §④ 说"文本编码器 = BERT-base-uncased"，对 MERLIN 分支成立，对旗舰分支不成立。== 旗舰模型读的是中文报告、输出 146 个中文征象名（推理脚本里硬编码的 `english_mapping` 词典），用的是 `bert-base-chinese`。

### (b) ❌ 推翻：视觉编码器不是 3D ResNet，是 nnU-Net 式的 PlainConvUNet

两处 `vision_branch.py` 都实例化同一个东西：

```python
# RADAR_inference/dynamic_network_architectures/vision_branch.py:35
# RADAR_train/lavis/models/radar_models/vision_branch.py:29
arch_class_name="dynamic_network_architectures.architectures.unet_lightdecoder.PlainConvUNetLightD",
arch_kwargs={
    "n_stages": 6,
    "features_per_stage": [32, 64, 128, 256, 320, 320],   # ← nnU-Net 的标准 feature 序列（320 封顶）
    "conv_op": "torch.nn.modules.conv.Conv3d",
    "kernel_sizes": [[1,3,3], [1,3,3], [3,3,3], [3,3,3], [3,3,3], [3,3,3]],
    "strides":     [[1,1,1], [1,2,2], [1,2,2], [2,2,2], [2,2,2], [2,2,2]],
    "n_conv_per_stage":         [2,2,2,2,2,2],
    "n_conv_per_stage_decoder": [1,1,1,1,1],
    "norm_op": "torch.nn.BatchNorm3d",
}
output_channels=37,        # 36 解剖结构 + 背景
```

而 `resnet_vl.py`（那个确实是 3D-ResNets-PyTorch 血统的文件，含 `downsample_basic_block(..., no_cuda)`、`shortcut_type='A'` 零填充捷径、`resnet10/18/34/50/101/152/200` 工厂函数）：

```bash
grep -rn "resnet" RADAR_inference/inference_demo.py \
                  RADAR_inference/dynamic_network_architectures/vision_branch.py \
                  RADAR_train/lavis/models/radar_models/radar_pretrain.py
# → 零命中
```

`inference_demo.py` 的全部架构 import 只有两行：

```python
# inference_demo.py:21-22
from dynamic_network_architectures.med import XBertEncoder, XBertLMHeadDecoder
from dynamic_network_architectures.vision_branch import VisionBranch
```

> [!insight] `resnet_vl.py` 是**被致谢、被打包、但从未被调用**的代码
> ==README 第 71 行郑重致谢 3D-ResNets-PyTorch (MIT)，`THIRD_PARTY_LICENSES.md` 第 241 行完整抄录了 "Copyright (c) 2017 Kensho Hara" 的 MIT 全文 —— 而对应的文件在推理与训练两条路径上都是死代码。==
> 这不是不诚实（多致谢一个比漏致谢一个好得多，法务上也对）。它是**开发史的化石**：早期版本大概真的试过 3D ResNet，后来换成了 nnU-Net 式的 UNet 编码器，清理许可文件时没人删。
> 🚩 对本次调查的方法学意义：**致谢表 ≠ 依赖图。** 必须用 `import` 重建真实依赖。

### (c) ⭐ 新洞见：max-pool 的核不是随便选的，==它就是编码器自己的累积步长==

逐级累乘 `strides`：

| stage | stride | 累积 (z, h, w) | 对应的 `F.max_pool3d` kernel | 投影 |
|---:|---|---|---|---|
| 1 | [1,1,1] | (1, 1, 1) | | |
| 2 | [1,2,2] | (1, 2, 2) | | |
| 3 | [1,2,2] | (1, 4, 4) | | |
| 4 | [2,2,2] | **(2, 8, 8)** | `kernel_size=(2,8,8)` ✅ (vision_branch.py:140) | `proj3: Conv3d(256→256)` |
| 5 | [2,2,2] | **(4,16,16)** | `kernel_size=(4,16,16)` ✅ (:146) | `proj2: Conv3d(320→256)` |
| 6 | [2,2,2] | **(8,32,32)** | `kernel_size=(8,32,32)` ✅ (:152) | `proj1: Conv3d(320→256)` |

三个池化核与第 4/5/6 stage 的累积步长**精确相等**。

> [!strategy] 这把 teardown §⑤ 的论证从"他们粗暴地降采样了 mask"升级成"他们把 mask 投到 token 网格上"
> ==40 mm(z) × 32 mm × 32 mm 不是一个**额外**的粗化步骤，而是这个编码器在最深一层的**固有分辨率**。== mask 被 max-pool，只是为了让"哪些 token 属于肝"这个布尔标记和特征图对齐。
> 结论不变（边界级 Dice 的改进在这一层被吃掉），但理由更硬：==要想让分割精度变得重要，你必须换一个分辨率更高的编码器，而不是换一个更好的分割器。==

### (d) 物理层面的三条局限（前两条见 teardown §①，第三条是新的）

| 局限 | 机制 | 受影响的征象 |
|---|---|---|
| **地板 −300 HU** | 肺实质 −700～−900 HU、气胸的空气 −1000 HU 全部钳到 −300 → ==气胸与正常肺在输入里数值完全相同== | 10 个肺征象（肺_气胸、肺_结节、肺_斑片影、肺_膨胀不全 …）|
| **天花板 400 HU** | 钙化、骨、对比剂全部饱和 → "钙化"退化成"有没有饱和体素"，密度大小消失 | ≥8 个（主动脉_钙化、脾_钙化、肾结石、肋骨_骨折/骨质破坏、骶骨_骨炎、肝内钙化灶、胆囊_结节状致密影）|
| ⭐ **z 向各向异性** | `kernel_sizes` 前两个 stage 是 `[1,3,3]`（面内卷积，z 不看）、`strides` 前三个 stage z 全是 1。最终 z 降 8×、面内降 32×。在 `[1,1,5]` mm spacing 下 → 最深 token = **40 mm(z) × 32 mm × 32 mm** | 一个 8 mm 胰腺灶 ≈ 最深 token 体积的 **1/125**。==任何关于小病灶的性能声明都必须按这个读。== |

> [!insight] 三条合起来是同一件事的三个面
> RADAR **把 CT 当成一张有解剖标签的灰度图**。它放弃了：绝对 HU 标度（逐体 min-max）、密度动态范围（两端钳位）、亚厘米空间分辨率（5 mm 层厚 + 32× 面内降采样）。
> 它能拿到 0.913 平均 AUC，正说明 ==**大部分常见腹部征象确实不需要这三样**==。
> 反过来 —— 对 Shu 的工作，这条判断是**直接可用的分界线**：凡是需要定量密度的（脂肪分数、碘浓度、材料组成、PVE 边界），这条路线在**原理上**到不了。不是工程没做好，是输入里已经没有那个信息了。

---

## ⑧ RADAR ⟂ MedSAM2：数据集**零交集**，只靠人相连

### 两边的数据集清单（各自的原始出处）

| | **RADAR** | **MedSAM2** |
|---|---|---|
| 主训练集 | **RAD-CT**：42 万检查 / 1500 万 anatomy-wise 图文对，浙一 + 协作网络，**私有** | >455,000 3D image-mask pairs + 76,000 frames（arXiv 2504.03600 摘要，**未命名聚合集**）|
| 公开可复现训练集 | **MERLIN**（Stanford，15,331 例腹部 CT）| |
| 外部/用户研究 | MERLIN 测试划分；8 个外部中心 | **CT_DeepLesion-MedSAM2**（5,000 CT 病灶）、3,984 例肝 MRI 病灶、251,550 帧超声心动 |
| 数据发源机构 | 浙江大学医学院附一院 🇨🇳 ／ 斯坦福 🇺🇸 | **NIH Clinical Center** 🇺🇸（DeepLesion）|

### CT_DeepLesion-MedSAM2 的源头

HuggingFace `wanglab/CT_DeepLesion-MedSAM2` 原文：

> "32,735 diverse lesions in 32,120 CT slices from 10,594 studies of 4,427 unique patients"，其中 5,000 个病灶用 MedSAM2 标注。
> 引用原始数据集：Yan, Ke et al., *Journal of Medical Imaging* **5(3):036501** (2018)。

DeepLesion 本体（OpenAlex 核实）：

```
DeepLesion: automated mining of large-scale lesion annotations and universal lesion detection with deep learning
2018-07-19 · J Med Imaging 5(3):036501 · DOI 10.1117/1.jmi.5.3.036501 · 被引 587
作者：Ke Yan · Xiaosong Wang · Le Lu · Ronald M. Summers
机构：**National Institutes of Health Clinical Center**（OpenAlex 里唯一的 institution 条目）
```

### 判定

```
   NIH Clinical Center (Bethesda)      Stanford (Palo Alto)      浙大一院 (杭州)
            │                                   │                       │
       DeepLesion                            MERLIN                  RAD-CT
            │                                   │                       │
            ▼                                   └──────────┬────────────┘
   CT_DeepLesion-MedSAM2                                   ▼
            │                                            RADAR
            ▼
        MedSAM2

   数据集交集 = ∅       三个互不隶属的机构，三批互不重叠的病人
```

✅ **"MedSAM2 与 RADAR 没有共用任何数据集" —— 成立。**
✅ **"两者只通过人（Ke Yan / Le Lu 从 NIH 到达摩院）相连" —— 成立，且 §④(d) 又补了 Ling Zhang 一条。**

⚠️ **一处未核实，必须标注**：MERLIN 的外部测试用了 "2 public datasets"，摘要没点名。==如果其中之一恰好是 DeepLesion，那么 MERLIN ↔ DeepLesion 会有一条间接接触。== 本轮没能读到 *Nature* 正文（付费墙 + IDP 重定向），**不能排除**。

> [!insight] 这三个机构的分工，本身就是一张"痕迹经济学"的地图
> - **NIH** 榨的是**几何痕迹**：放射科医生随手画的 RECIST 长径 → 3D mask。
> - **斯坦福** 榨的是**结构化痕迹**：EHR 诊断码（180 万条）+ 报告。
> - **达摩院** 榨的是**文本痕迹**：报告经 LLM 解析成 anatomy-wise 标签。
>
> ==三家都在做同一件事：把医院为临床（而非为 AI）留下的副产品，转成监督信号。== 差别只在榨的是哪一种副产品，而这取决于**各自能拿到什么**。
> NIH 有 PACS 的标记层；斯坦福有打通的 EHR；浙一有海量中文报告和一个能调 LLM 的母公司。**基础设施决定了方法论，不是反过来。**

---

## ⑨ 一张表：依赖 × 血统 × 风险

| 依赖 | 地理/机构 | 关键人 | 现状 | 对 RADAR 的**真实**风险 |
|---|---|---|---|---|
| LAVIS | Salesforce AI 🇺🇸 | dxli94 (Dongxu Li) 358 提交；**LiJunnan1992 (Junnan Li)** 45 提交 = ALBEF/BLIP 一作 | ==已归档 2026-09-18；实质停更 2024-11== | 低。代码已 vendored 进仓库，上游死活无所谓。但 ==RADAR 也因此永远停在 ALBEF 时代== |
| dynamic-network-architectures / nnU-Net | MIC-DKFZ 海德堡 🇩🇪 | **FabianIsensee** 1662 提交（≈95%）；`wasserth` 也是 nnU-Net 贡献者（9 提交）| 活跃 | 低。同样 vendored |
| MONAI | NVIDIA + KCL 联盟 🇺🇸🇬🇧 | wyli (Wenqi Li) 833、Nic-Ma 710；**holgerroth 排 18/296** | 活跃 | ==极低。只用了 4 个几何变换符号== |
| 3D-ResNets-PyTorch | kenshohara 个人 🇯🇵 | Kensho Hara（417/425 提交）| ==死 5 年 8 个月== | **零。代码从未被 import** |
| TotalSegmentator v1.5.7 | 巴塞尔大学医院 🇨🇭 | **Jakob Wasserthal**（1022 提交，bus factor = 1）| v1 线已废；主线 2.18.0 | 中。只在"用自己数据重训"时出现；`nnunet-customized==1.2` 依赖已不可装 |
| DashScope / Qwen | **阿里云**（非达摩院）🇨🇳 | — | 商业 API | 中。需要账号与配额；但文档明说可替换 |
| **MERLIN** | Stanford AIMI 🇺🇸 | Blankemeier / Chaudhari / Langlotz | Nature 2026，MIT 代码权重 | ==高（但不是技术风险）。整个公开复现路径建在别人的数据发布政策之上== |

---

## ⑩ 对 Shu 的三条

**① 可以直接拿走的：`totalseg_info` + `--report` 这一对。**
TotalSegmentator `2.15.0`（2026-07-01）新增：`totalseg_info`（不需要 GPU、不需要下权重，秒出任务/类别表）和 `--report <path.json>`（写出软件版本、模型版本、设备、任务、类别、耗时、输出文件的机器可读运行清单）。
==这正好是材料分解流水线缺的那一层 provenance。== 你现在在 `*.pluto-cache.toml` 里手动记的东西，分割这一步可以直接让它自己吐出来。
顺带：`2.13.0` 的 `coronary_arteries` 已换成 skeleton-recall 模型（旧版降级为 `coronary_arteries_LEGACY`）—— 与 PCAT 自动中心线那条线直接相关，值得对照一次。

**② 必须拒绝的：不要学 RADAR 处理 HU 的方式。**
逐体 min-max（`inference_demo.py:195`）把标定过的物理量变成了相对灰度。==对分类任务这是无害的；对你，HU 标度就是全部。==
更一般的教训：RADAR 的每一个设计选择（钳位、5 mm、32× 降采样、砍薄解码器、max-pool 到 40×32×32 mm）都在同一个方向上 —— **用空间与密度精度换语义覆盖广度**。你做的事在这条轴的另一端。==抄它的任何一个工程细节都是在往错误方向走；能抄的只有评估形式。==

**③ 方法学上最值钱的一条：致谢表不是依赖图。**
这一轮最硬的发现（3D-ResNets 是死代码、MONAI 只用了 4 个符号、MERLIN 是训练集而非测试集）==全部来自"别读 README，去 grep import；别读摘要，去读 TRAINING.md 第 3 行"。==
同样的方法可以直接用在你正在评估的任何一个上游工具上。

---

## 未解决 / 不要当成已知

- ⚠️ **TotalSegmentator "v3" 改了什么** —— 无据。`v3.0.0` tag 的 `setup.py` 版本号仍是 `2.18.0`，CHANGELOG 无 v3 条目，`resources/improvements_in_v3.md` 返回 404，PyPI 无 3.x 包。目前只能说"发布了一组新权重"。
- ⚠️ **MERLIN 数据集的 DUA / 商用限制** —— Stanford AIMI 页面本轮只返回导航壳，协议原文未读到。
- ⚠️ **MERLIN 外部测试用的 "2 public datasets" 是哪两个** —— 摘要未点名，正文在付费墙后（`nature.com` 303 → `idp.nature.com`）。**如果其一是 DeepLesion，§⑧ 的"零交集"需要加限定。**
- ⚠️ **Ling Zhang 在 IEEE TMI 2018/2020 两篇上的署名单位** —— PubMed `AffiliationInfo` 字段为空，NIH 身份是由共同作者集合**推断**的。
- ⚠️ **`report_parsing_normal.py` 用的是 qwen_plus 还是 qwen_max** —— 本轮未读该文件。
- ⚠️ **RAD-CT（旗舰）训练用的 GPU 数 / batch / epoch** —— `radar_config.yaml` 是 MERLIN 分支的配置。旗舰分支的训练超参未公开。
- ⚠️ **达摩院与阿里云通义的组织关系细节** —— 本页只核到"Qwen 由 Alibaba Cloud 提出、DashScope 由 Alibaba Cloud 维护"这一层。两个单元之间的隶属/沿革**未核**，不要展开讲。
- 本页所有 GitHub 数据来自 `gh api`（已认证），PyPI/Crossref/PubMed/arXiv 来自匿名 REST。OpenAlex 在调查后段触发配额上限，Semantic Scholar 429 —— 部分交叉验证只做了单源。

---

## See Also

- [radar-technical-teardown.md](radar-technical-teardown.md) —— RADAR 源码级拆解（⚠️ 其 §④ 的视觉/文本编码器结论已被本页 §⑦ 修正）
- [radar-vs-medsam.md](radar-vs-medsam.md) —— 与 MedSAM 的关系（本页 §⑧ 补充了数据集层面的正式判定）
- [authors-affiliations.md](authors-affiliations.md) —— 40 位作者单位骨架表
- [damo-lineage.md](damo-lineage.md) —— 达摩院医疗 AI 血统
- [../README.md](../README.md)
