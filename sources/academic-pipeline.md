# 学术供给线：西工大 → Adelaide → MBZUAI

> 完整 URL 清单见 [../data/raw/ctx-academic-pipeline.md](../data/raw/ctx-academic-pipeline.md)。
> 核对日期：2026-09-20。

---

## 一句话

RADAR 的视觉-语言方法供给线不是三个孤立的海外单位，而是**一条以西北工业大学夏勇实验室为源头、以阿德莱德大学 AIML 为中转站的师承链**。论文里挂 Adelaide / MBZUAI / 宁波二院的 5 个人全部落在这条链上。

---

## Yong Xia 就是西工大夏勇

从 PubMed efetch 原始 XML 抽取 RADAR 的 26 个单位编号 —— ==**"西北工业大学"五个字在全文 26 个单位里一次都没出现**。==

| 编号 | 单位原文 | 挂靠者 |
|---:|---|---|
| 7 | Department of Radiology, **Ningbo No. 2 Hospital** | #4 Zilin Lu（+DAMO）· #11 Shaoteng Zhang（+DAMO）· **#13 Yong Xia（唯一单位）** |
| 9 | Australian Institute for Machine Learning, **Adelaide University** | #10 Sinuo Wang · #14 Qi Wu |
| 10 | Department of Computer Vision, **MBZUAI**, Abu Dhabi | #12 Yutong Xie |

**#13 Yong Xia = 西北工业大学计算机学院 夏勇教授，已确证。** 证据链：

| 证据 | 内容 |
|---|---|
| ⓪ **ORCID 直证** | RADAR 的 PubMed 记录里 #13 带 ORCID `0000-0001-9273-2847`；同一 ORCID 下另外 5 篇（*Nat Commun* 2025、*Radiology* 2023 等）的单位**全部是西北工业大学计算机学院** |
| ① 师承直证 | 谢雨彤（#12）第一人称自述"**2021 年在西北工业大学获得博士学位，师从夏勇教授**" |
| ② ORCID 旁证 | **Zilin Lu（#4）的 ORCID 0000-0003-2437-283X，educations 栏明写 Northwestern Polytechnical University** —— 他和夏勇共享同一个单位编号 7 |
| ③ 合著网络 | OpenAlex：Jianpeng Zhang（#2）的头号合著者就是 Yong Xia，**22 篇共著，机构标 NWPU ×21**；Yutong Xie 第 3 位，NWPU ×18 |
| ④ 宁波通道已证实 | 夏勇论文里出现过 `Ningbo Institute of Northwestern Polytechnical University`（西北工业大学宁波研究院），见 2023 DoDNet 期刊版与 2025 PICK |
| ⑤ 方向吻合 | 西工大计算机学院长聘教授、博导、**副院长**；2013 年国家"青年海外人才"回国，方向=医学影像大数据分析/CAD/深度学习 |

==所以挂"宁波二院放射科"的三个人（#4、#11、#13）其实是一条西工大线。这个单位编号是这条线的落点，不是一群放射科医生。==

⚠️ 夏勇与宁波二院放射科的**具体关系**（任命 / 兼职 / 客座）没有找到直接记载；宁波二院放射科的医生名单里没有"夏勇"。判定靠的是上面五条。

💡 RADAR 在 OpenAlex 与 PubMed 两处的 author-affiliation 记录并不完全一致（谢雨彤一处记为 MBZUAI、另一处记为 Adelaide）。用本文 affiliation 字段做推断要带这个保留。

---

## 这条链，用当事人自己的话

中国图象图形学学会（CSIG）2023 年度博士学位论文激励计划专访，**谢雨彤第一人称**：

> "我于 **2021 年在西北工业大学获得博士学位，师从夏勇教授**。**2020 年 1 月至 2021 年 4 月，我被公派到澳大利亚阿德莱德大学联合培养，师从沈春华教授和 Verjans Johan 教授**。**2021 年 4 月至今，我入职澳大利亚阿德莱德大学担任博士后研究员，师从吴琦教授**。"

一段话把三站全讲了：

```
西北工业大学（夏勇）            ← 源头，空天地海一体化大数据实验室（张艳宁）
      │ 2020-01 公派联合培养
      ▼
Adelaide AIML（沈春华 → 吴琦）  ← 中转站
      │ 2025-01（ORCID 雇佣记录）
      ▼
MBZUAI 计算机视觉系             ← 现职：助理教授（独立 PI）
```

---

## 五个人的身份卡

| # | 人 | 身份 | 在这条链上的位置 |
|---|---|---|---|
| 13 | **夏勇** Yong Xia | 西工大计算机学院长聘教授、博导、副院长 | **源头**。张建鹏、谢雨彤、Zilin Lu、Shaoteng Zhang 都出自这里 |
| 12 | **谢雨彤** Yutong Xie | MBZUAI 助理教授（2025-01 起）；此前 Adelaide AIML 博士后 | **中转站的产物，现已独立**。V3ALab 页面把她列在 Alumni |
| 14 | **吴琦** Qi Wu | Adelaide 副教授，**V3ALab（Vision, Ask, Answer, Act）Director**；AIML 视觉与语言领域主任 | **中转站的主人**。方向：Image Captioning / Visual Question Answering |
| 10 | **Sinuo Wang** | 吴琦的**博士生**（V3ALab People 页 "PhD Students" 名单直接列着） | ==**Adelaide → 达摩院的人肉管道本身**== |
| 2 | **张建鹏** Jianpeng Zhang | 达摩院 Staff Algorithm Engineer | 西工大出身，已落地达摩院 |

### Sinuo Wang 这一条最说明问题

- V3ALab People 页把她列在 PhD Students；同页 Alumni 里列着 "Yutong Xie, Postdoctoral Research Fellow"
- 论文旁证：**PairAug (CVPR 2024)** = Yutong Xie, Qi Chen, **Sinuo Wang**, …, **Yong Xia**, **Qi Wu**（放射报告图文对增强 —— 和 RADAR 同一个技术问题）；**MedCutMix (2026)** = Sinuo Wang 一作、Qi Wu 末位
- ==她 2025–2026 有两篇论文的单位**直接写 `DAMO Academy, Alibaba Group`**==（*Boosting Vision Semantic Density…*、*Rethinking the Efficiency and Effectiveness of RL for Radiology Report Generation*）
- 更早：郑州大学网络空间安全学院本科

> [!insight] 供给线是真实的，而且是双向的
> 西工大出人 → Adelaide 做博后/博士 → 回流达摩院做实习/正式岗。
> RADAR 的视觉-语言那部分，方法来自这条链，人也来自这条链。

---

## 校名细节

论文写的是 **"Adelaide University"**，不是 "The University of Adelaide"。

这不是笔误 —— **阿德莱德大学与南澳大学合并成立的新 Adelaide University 于 2026-01-29 正式开门**，RADAR 2026-09-17 上线时用的是新校名。

---

## 未解决

- 夏勇与宁波二院放射科的**具体关系**（任命/兼职/客座）无直接记载
- 吴琦的 **ARC DECRA Fellow** 身份只见于二手来源（conferences.com.au），未经官方核实
- Zilin Lu、Shaoteng Zhang 的**中文名**查不到（西工大在读博士，中文互联网无公开痕迹）
- Sinuo Wang 的**中文名**查不到

---

## See Also

- [../README.md#三条血统线](../README.md#三条血统线)
- [authors-affiliations.md](authors-affiliations.md)
- [../data/raw/ctx-academic-pipeline.md](../data/raw/ctx-academic-pipeline.md) —— 完整取证
