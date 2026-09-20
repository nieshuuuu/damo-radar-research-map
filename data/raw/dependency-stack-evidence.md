# dependency-stack.md 的原始取证命令与输出（未编辑）

核对日期 2026-09-20。全部可重跑。

## 1. RADAR 仓库元数据与文件树
```bash
gh api repos/alibaba-damo-academy/damo-radar --jq '{created:.created_at,pushed:.pushed_at,stars:.stargazers_count,lic:.license.spdx_id}'
# {"created":"2026-07-03T06:30:03Z","lic":"Apache-2.0","pushed":"2026-09-18T01:50:18Z","stars":357}

gh api 'repos/alibaba-damo-academy/damo-radar/git/trees/main?recursive=1' --jq '.tree[]|select(.type=="blob")|.path'
```

## 2. 四个致谢依赖的仓库体检
```bash
for r in salesforce/LAVIS MIC-DKFZ/nnUNet Project-MONAI/MONAI kenshohara/3D-ResNets-PyTorch wasserth/TotalSegmentator; do
  gh api "repos/$r" --jq '{created:.created_at,pushed:.pushed_at,stars:.stargazers_count,lic:.license.spdx_id,archived:.archived}'
done
```
```
salesforce/LAVIS                {"archived":true, "created":"2022-08-24T02:36:01Z","pushed":"2026-09-18T09:59:39Z","stars":11266,"lic":"BSD-3-Clause"}
MIC-DKFZ/nnUNet                 {"archived":false,"created":"2019-04-17T08:10:56Z","pushed":"2026-09-14T10:06:32Z","stars":8898, "lic":"Apache-2.0"}
Project-MONAI/MONAI             {"archived":false,"created":"2019-10-11T16:41:38Z","pushed":"2026-09-18T18:43:41Z","stars":8696, "lic":"Apache-2.0"}
kenshohara/3D-ResNets-PyTorch   {"archived":false,"created":"2017-09-14T12:14:44Z","pushed":"2021-01-20T20:31:36Z","stars":4038, "lic":"MIT"}
wasserth/TotalSegmentator       {"archived":false,"created":"2022-01-19T12:24:33Z","pushed":"2026-09-16T14:08:57Z","stars":3007, "lic":"Apache-2.0"}
```

## 3. LAVIS 归档时间与贡献者
```bash
gh api "repos/salesforce/LAVIS/commits?per_page=5" --jq '.[]|"\(.commit.author.date)  \(.commit.author.name)  \(.commit.message|split("\n")[0])"'
```
```
2026-09-18T09:59:39Z  Jim Jagielski  This repo is ARCHIVED
2026-06-02T18:14:48Z  Jim Jagielski  Upload required SECURITY.md file for compliance
2024-11-18T19:51:41Z  Tycho-Xue      Merge pull request #730 from artemisp/main   <- 最后一次功能性提交
```
```bash
gh api "repos/salesforce/LAVIS/contributors?per_page=12" --jq '.[]|"\(.login)  \(.contributions)"'
# dxli94 358 / LiJunnan1992 45 / henryhungle 13 / artemisp 10 / jimjag 2 ...
```

## 4. MONAI 贡献者排名（holgerroth 的位次）
```bash
gh api --paginate "repos/Project-MONAI/MONAI/contributors?per_page=100" --jq '.[]|"\(.login)\t\(.contributions)"' | wc -l   # 296
# 1 wyli 833 / 2 Nic-Ma 710 / 3 KumoLiu 232 / 4 rijobro 187 / ... / 18 holgerroth 20
```
MONAI 论文 arXiv 2211.02701（2022-11-04，57 作者）：#1 M. Jorge Cardoso, #2 Wenqi Li, #4 Nic Ma,
#13 Ziyue Xu, #39 Lena Maier-Hein, #41 Michael Baumgartner, **#46 Holger R. Roth**, #47 Daguang Xu,
#50 S. Kevin Zhou, #53 Klaus H. Maier-Hein, #57 Andrew Feng.

## 5. Holger Roth x Le Lu 共同署名（OpenAlex A5043710204，276 篇）
```bash
curl -sL "https://api.openalex.org/works?filter=author.id:A5043710204&per-page=200&select=id,title,publication_year,authorships&sort=publication_year:asc"
```
前 200 篇中与 Le Lu 共同署名 **35 篇**，全部 2014–2019，全部 NIH Clinical Center / Summers 组。

## 6. Ling Zhang x Le Lu x Summers（PubMed）
```bash
esearch db=pubmed term="(Zhang L[au]) AND (Lu L[au]) AND (Summers RM[au])"   # count=2
```
- PMID 29408791 · IEEE TMI 2018 · Ling Zhang, Le Lu, Ronald M Summers, Electron Kebebew, Jianhua Yao
- PMID 31562074 · IEEE TMI 2020 · Ling Zhang, Le Lu, Xiaosong Wang, Robert M Zhu, Mohammadhadi Bagheri, Ronald M Summers, Jianhua Yao
⚠️ 两条记录的 AffiliationInfo 字段均为空。

## 7. TotalSegmentator 全版本史（PyPI upload_time_iso_8601）
```
2022-08-04 1.0     2022-08-12 1.1     2022-08-18 1.2     2022-09-07 1.3
2022-11-10 1.4.0   2023-01-09 1.5.0   2023-01-09 1.5.2   2023-03-08 1.5.3
2023-03-27 1.5.4   2023-03-29 1.5.5   2023-05-16 1.5.6   2023-09-26 2.0.0
2023-09-27 2.0.1   2023-10-04 2.0.2   2023-10-12 2.0.3   2023-10-17 1.5.7
2023-10-19 2.0.4   2023-10-20 2.0.5   2024-02-16 2.1.0   2024-05-29 2.2.1
2024-07-10 2.3.0   2024-07-25 2.4.0   2025-01-17 2.5.0   2025-02-03 2.6.0
2025-02-19 2.7.0   2025-04-15 2.8.0   2025-06-02 2.9.0   2025-06-24 2.10.0
2025-08-22 2.11.0  2025-12-12 2.12.0  2026-03-17 2.13.0  2026-06-10 2.14.0
2026-07-01 2.15.0  2026-07-21 2.16.0  2026-07-29 2.17.0  2026-08-12 2.18.0
LATEST: 2.18.0 · AUTHOR: Jakob Wasserthal <jakob.wasserthal@usb.ch> · LICENSE: Apache 2.0
```
GitHub releases: v1.5.6-weights 2023-09-21 / v2.0.0-weights 2023-09-21 / v2.0.4-weights 2023-10-19 /
v2.2.0-weights 2024-05-28 / v2.3.0-weights 2024-07-10 / v2.4.0-weights 2024-07-22 /
v2.5.0-weights 2025-01-15 / **v3.0.0-weights 2026-09-07**

## 8. "v3" 只有权重、没有代码版本
```bash
gh api repos/wasserth/TotalSegmentator/git/ref/tags/v3.0.0 --jq '.object.sha'
gh api repos/wasserth/TotalSegmentator/commits/<sha> --jq '.commit.author.date, .commit.message'
# 2026-09-07T11:47:41Z  "update prepare weight for release"
curl -sL ".../v3.0.0/setup.py" | grep version    # version='2.18.0'
curl -sL ".../v3.0.0/CHANGELOG.md" | head -3     # "## Master"，无 v3 条目
curl -sL ".../master/resources/improvements_in_v3.md"   # 404
```

## 9. RADAR 源码 grep（依赖真实深度）
```bash
grep -rn "monai" RADAR_inference/*.py RADAR_train/lavis/processors/*.py RADAR_inference/dynamic_network_architectures/*.py
# inference_demo.py:12  from monai import transforms
# inference_demo.py:13  from monai.data.utils import dense_patch_slices
# radar_processors.py:9 from monai import transforms
# vision_branch.py:19   from monai.utils import deprecated_arg

grep -rn "resnet\|ResNet" inference_demo.py vision_branch.py radar_pretrain.py radar_base.py
# 零命中 -> resnet_vl.py 是死代码
```

## 10. Qwen / DashScope 调用
```
RADAR_train/preprocess_code/check_organ_mention.py:40   model=dashscope.Generation.Models.qwen_plus
RADAR_train/preprocess_code/report_parsing.py:43        model=dashscope.Generation.Models.qwen_max
两者第 70 行均为 dashscope.api_key = ""
```
```bash
curl -sL "https://pypi.org/pypi/dashscope/json"
# author: Alibaba Cloud | dashscope@alibabacloud.com | https://dashscope.aliyun.com/ | Apache 2.0 | 1.27.6
```
QwenLM/Qwen README 原文："proposed by **Alibaba Cloud**"。Qwen Technical Report = arXiv 2309.16609, 2023-09-28, 48 作者。

## 11. MERLIN
```bash
esearch db=pubmed term="Merlin: a computed tomography vision-language foundation model and dataset"  # PMID 41781626
curl -sL "https://api.crossref.org/works/10.1038/s41586-026-10181-8"
```
Nature **652:1318-1328** (2026) · 40 作者全部斯坦福 · #1 Louis Blankemeier · #37 Curtis P Langlotz ·
#39 Sergios Gatidis · #40 Akshay S Chaudhari (通讯)。
摘要：15,331 例腹部 CT（>600 万图）、>180 万诊断码、>600 万 token 报告；内部测试 5,137 例，
外部测试 44,098 例（3 中心 + 2 个公开数据集）；6 类任务 / 752 个任务。
代码 MIT: github.com/StanfordMIMI/Merlin；权重 MIT: huggingface.co/stanfordmimi/Merlin。
RADAR docs/INFERENCE.md:48 指向 Stanford AIMI 数据集 id 60b9c7ff-877b-48ce-96c3-0194c8205c40。

## 12. DeepLesion / CT_DeepLesion-MedSAM2
```bash
curl -sL "https://api.openalex.org/works?filter=title.search:DeepLesion"
```
`DeepLesion: automated mining...` 2018-07-19 · J Med Imaging 5(3):036501 · DOI 10.1117/1.jmi.5.3.036501 ·
被引 587 · Ke Yan, Xiaosong Wang, Le Lu, Ronald M. Summers · **NIH Clinical Center**。
HF `wanglab/CT_DeepLesion-MedSAM2`："32,735 diverse lesions in 32,120 CT slices from 10,594 studies of
4,427 unique patients"，5,000 个用 MedSAM2 标注，引用 Yan et al. JMI 2018。
MedSAM2 arXiv 2504.03600：9 作者（Jun Ma, Zongxin Yang, Sumin Kim, Bihui Chen, Mohammed Baharoon,
Adibvafa Fallahpour, Reza Asakereh, Hongwei Lyu, Bo Wang）；训练 >455,000 3D image-mask pairs + 76,000 frames。
