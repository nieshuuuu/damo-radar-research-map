交付文件（已提交，commit `11cf4da`）：
- `/Users/shunie/Developer/damo-radar-research-map/sources/dependency-stack.md` —— 正文（依赖图 + 7 项审计 + 人事交叉）
- `/Users/shunie/Developer/damo-radar-research-map/data/raw/dependency-stack-evidence.md` —— 全部取证命令与原始输出，可重跑

⚠️ 仓库**没有配置 remote**（`git remote -v` 为空），本地已 commit 但未 push。

---

## 推翻的三条（都在原 `radar-technical-teardown.md` 里）

**1. 视觉编码器不是 3D ResNet。** `RADAR_inference/dynamic_network_architectures/vision_branch.py:35` 与 `RADAR_train/lavis/models/radar_models/vision_branch.py:29` 都实例化 `PlainConvUNetLightD`（nnU-Net 式，6 stage，`features_per_stage [32,64,128,256,320,320]`）。`resnet_vl.py` 确实在仓库里、确实是 kenshohara 血统，但 `grep -rn "resnet" inference_demo.py vision_branch.py radar_pretrain.py` **零命中** —— 死代码。README 第 71 行的致谢和 `THIRD_PARTY_LICENSES.md:241` 的 MIT 全文对应一个从未被调用的文件。

**2. 文本编码器有两个。** `docs/INFERENCE.md:23` 表格写 `bert-base-chinese`（配 `checkpoint_radar_pretrain.pth` = RAD-CT 旗舰）；`docs/TRAINING.md` 支持文件表写 `bert-base-uncased`（配 `checkpoint_radar_plus.pth` = Merlin 分支）。`radar_config.yaml` 的 uncased 是 MERLIN 那一支。

**3. Qwen 不属达摩院。** `QwenLM/Qwen` README 原文 "proposed by **Alibaba Cloud**"；PyPI `dashscope` 的 `author = Alibaba Cloud`，homepage `dashscope.aliyun.com`。RADAR(达摩院) 调 Qwen 是**跨事业部调商业 API**。两档成本分级：`check_organ_mention.py:40` 用 `qwen_plus`（高频过滤），`report_parsing.py:43` 用 `qwen_max`（结构化抽取）。

## 最大的新发现

**MERLIN 不是外部测试集，是 RADAR 全部公开可复现性的载体。** `docs/TRAINING.md` 第 3 行："training RADAR/RADAR+ on **Merlin-CT-Train set** from scratch"；`checkpoint_radar_plus.pth` 的说明是 "trained from scratch on Merlin-CT-Train set"。仓库里躺着 `data/merlin_data_train_demo/`、`ckpt/merlin_report_organ_*.json`、`infer_text_embedding_merlin.pt`；预处理脚本参数直接叫 `--root-dir /path/to/merlin_data_root`；他们还在 HF 上发了自己跑的 MERLIN 训练 mask（part00/01/02）。

即：DAMO 发布的那批 TotalSegmentator v1.5.7 mask 跑在**斯坦福的 CT** 上，Qwen 解析的是**斯坦福的英文报告**。RAD-CT（浙一 42 万例）不可能放出来，所以他们用一个公开的同任务美国数据集把整条流水线演示了一遍。

## 关于"NIH 链条"的裁决：过度解读，但换个说法就成立

- Holger Roth 在 MONAI 是 **18/296 贡献者（20 提交）**，MONAI 论文 **46/57 位**，不是核心。
- RADAR 对 MONAI 的依赖只有 **4 个符号**：`transforms`(×2)、`dense_patch_slices`、`deprecated_arg` —— 纯几何变换。
- **Le Lu 和 Ke Yan 根本不是 RADAR 作者。**
- ✅ 但 Roth↔Le Lu 的 NIH 关系极硬：OpenAlex 查出 **35 篇共同署名，2014–2019，全在 Summers 组**（DeepOrgan、Shin et al. IEEE TMI 2016 等）。MONAI 论文 #13 **Ziyue Xu** 也是同组出来的 —— NIH→NVIDIA 是一条小队伍。
- ✅ 真链条走人事，且新补了一条：**Ling Zhang（RADAR #39，达摩院华盛顿特区）** 与 Le Lu + Summers + Jianhua Yao 共同发表 IEEE TMI 2018（PMID 29408791）和 2020（PMID 31562074）。⚠️ 两条 PubMed 记录的 affiliation 字段为空，NIH 身份由共同作者集合推断。

## 其他核实结果

- **TotalSegmentator 五个日期全部属实**（1.5.6=2023-05-16、2.0.0=2023-09-26、1.5.7=2023-10-17、2.18.0=2026-08-12、v3.0.0-weights=2026-09-07）。Jakob Wasserthal，巴塞尔大学医院，论文 12 位作者**全部同一地址**。⚠️ **"v3" 目前只有权重**：`v3.0.0` tag 的 `setup.py` 仍写 `version='2.18.0'`，CHANGELOG 无 v3 条目，`improvements_in_v3.md` 返回 404。v1→v2 的改动有据（`resources/improvements_in_v2.md`），含"colon/small_bowel 的 GT 有时候就是错的"列在 still open problems。
- **LAVIS 已归档**，2026-09-18（Jim Jagielski，"This repo is ARCHIVED"），比 RADAR 最后一次 push 晚 8 小时；实质停更在 2024-11-18。**3D-ResNets-PyTorch 最后 push 2021-01-20**。
- **RADAR 对 nnU-Net 架构库的唯一改动是砍薄解码器**：`n_conv_per_stage [2,2,2,2,2,2]` vs `n_conv_per_stage_decoder [1,1,1,1,1]`，且自己加了 `unet_lightdecoder.py` / `unet_decoder_light.py`（上游 `MIC-DKFZ/dynamic-network-architectures` 没有）。
- **max_pool3d 的核 = 编码器自己的累积步长**：strides 逐级累乘得 (2,8,8)/(4,16,16)/(8,32,32)，与 `vision_branch.py:140/146/152` 三个 kernel **精确相等**。所以 40×32×32 mm 不是额外粗化，是编码器最深层的固有分辨率。
- **数据集零交集成立**：RADAR = RAD-CT(浙一，私有) + MERLIN(Stanford)；MedSAM2 = CT_DeepLesion-MedSAM2(NIH DeepLesion，Ke Yan 2018，JMI 5(3):036501，587 引)。三个机构互不隶属。⚠️ 唯一未排除项：MERLIN 外部测试用的 "2 public datasets" 未点名，Nature 正文付费墙 403/303。
- **MERLIN**：Nature **652:1318-1328**(2026)，40 作者**全部斯坦福**，一作 Louis Blankemeier，通讯 **Akshay S. Chaudhari**（即 Shu 之前评过 5.5 分的那位 PI），15,331 例腹部 CT，代码+权重 MIT。

已在文末列了 7 条"未解决，不要当成已知"，包括 v3 内容、MERLIN 的 DUA、Ling Zhang 单位、旗舰模型训练超参。