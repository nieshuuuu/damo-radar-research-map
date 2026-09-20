已完成。以下是调查结果。

---

# 学术侧供给线：西工大 → Adelaide → MBZUAI

**一句话结论**：RADAR 的"视觉-语言方法供给线"不是三个孤立的海外单位，而是**一条以西北工业大学夏勇实验室为源头、以阿德莱德大学 AIML 为中转站的师承链**。论文里挂 Adelaide / MBZUAI / 宁波二院的 5 个人（Sinuo Wang、Zilin Lu、Yutong Xie、Yong Xia、Qi Wu）全部落在这条链上，其中 **Yong Xia = 西北工业大学 夏勇教授，已由 ORCID 确证，把握 95%+**。

---

## 0. 先把论文原文的单位钉死（SSoT）

RADAR 的 26 个单位编号，从 PubMed efetch 原始 XML 抽取，**"西北工业大学"五个字在全文 26 个单位里一次都没出现**：

| 编号 | 单位原文 | 挂靠者 |
|---:|---|---|
| 7 | Department of Radiology, Ningbo No. 2 Hospital, Ningbo, Zhejiang, China | #4 Zilin Lu(+DAMO)、#11 Shaoteng Zhang(+DAMO)、**#13 Yong Xia（唯一单位）** |
| 9 | Australian Institute for Machine Learning, **Adelaide University**, Adelaide SA | #10 Sinuo Wang、#14 Qi Wu |
| 10 | Department of Computer Vision, **Mohamed bin Zayed University of Artificial Intelligence**, Masdar City, Abu Dhabi, UAE | #12 Yutong Xie |

- PubMed XML：`https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=42752131&retmode=xml`（本地：`/Users/shunie/Developer/damo-radar-research-map/data/pubmed-42752131.xml`）
- Crossref 独立复核同一结论：`https://api.crossref.org/works/10.1126/science.aec6129`
- 顺带一个可写进 README 的细节：论文写的是 **"Adelaide University"** 而不是 "The University of Adelaide"。这不是笔误——阿德莱德大学与南澳大学合并成立的新 **Adelaide University 于 2026 年 1 月 29 日正式开门**，RADAR 2026-09-17 上线时用的是新校名。`https://en.wikipedia.org/wiki/Adelaide_University`

---

## 1. 五个人的身份卡

### ① Qi Wu = 吴琦（把握：确认）
- 阿德莱德大学**副教授**（Associate Professor），School of Computer Science and Information Technology；研究方向自述为 "cross-depictive style object modelling, object detection and Vision-to-Language problems"，尤其 Image Captioning 与 **Visual Question Answering**。2017–2018 曾任 Australian Centre for Robotic Vision (ACRV) 的 ARC Senior Research Associate。
  `https://researchers.adelaide.edu.au/profile/qi.wu01`
- 自建课题组 **V3ALab（Vision, Ask, Answer, Act）**，本人署名 Director，联系邮箱 `qi.wu01@adelaide.edu.au`。`https://v3alab.github.io/` · `https://v3alab.github.io/people/`
- 中文身份：**吴琦**，"澳大利亚阿德莱德大学副教授，现任澳大利亚机器学习研究所视觉与语言领域主任"；中国计量大学 2010 届校友。`https://lxy.cjlu.edu.cn/`（理学院《具身视觉语言导航》讲座通知 + 校友专访，Bing 可检索到快照）
- 另有第三方资料记其为 **ARC DECRA Fellow**（`https://conferences.com.au/qi-wu`）——这条是二手来源，写进仓库时建议标"待官方核实"。

### ② Sinuo Wang —— **是吴琦的博士生**（把握：确认）
- V3ALab **People 页 "PhD Students" 名单里直接列着 Sinuo Wang**，同页 Alumni 里列着 "Yutong Xie, Postdoctoral Research Fellow"。`https://v3alab.github.io/people/`
- 论文旁证：
  - **PairAug (CVPR 2024)**：Yutong Xie, Qi Chen, **Sinuo Wang**, …, Yong Xia, **Qi Wu** —— 放射报告图文对增强。
  - **MedCutMix (2026)**：**Sinuo Wang**（一作）, Yutong Xie, Yuyuan Liu, **Qi Wu**（末位）——典型的"学生一作 + 导师末位"。
  - 谢雨彤个人主页 News 多次出现 "Congrats … Sinuo …"，说明实际是**吴琦挂名、谢雨彤带**的共同指导。`https://ytongxie.github.io/`
- 她同时有**达摩院实习**痕迹：2025–2026 两篇论文她的单位直接写 `DAMO Academy, Alibaba Group`（*Boosting Vision Semantic Density…*、*Rethinking the Efficiency and Effectiveness of RL for Radiology Report Generation*）。**这就是 Adelaide→达摩院的人肉管道本身。**
- 更早：郑州大学网络空间安全学院本科（2022 年一篇 LightGBM 论文）；2024 年还挂过 CNRS 与 Adelaide 合建的 CROSSING 联合实验室（RoboCup@Home）。

### ③ Yutong Xie = 谢雨彤（把握：确认，这是本次最硬的一条链）
中国图象图形学学会（CSIG）2023 年度博士学位论文激励计划入选者专访，**她本人第一人称叙述**，把整条链讲全了：

> "我于 **2021 年在西北工业大学获得博士学位，师从夏勇教授**。**2020 年 1 月至 2021 年 4 月，我被公派到澳大利亚阿德莱德大学联合培养，师从沈春华教授和 Verjans Johan 教授**。**2021 年 4 月至今，我入职澳大利亚阿德莱德大学担任博士后研究员，师从吴琦教授**。"
> 致谢里还点名："空天地海一体化大数据实验室的领导人**张艳宁**教授"。
> `https://www.csig.org.cn/67/202404/51784.html`

- 现职：**MBZUAI 计算机视觉方向助理教授（Assistant Professor of Computer Vision, Division of Computing and Mathematical Sciences）**。`https://mbzuai.ac.ae/study/faculty/yutong-xie/`
- **转去 MBZUAI 的确切时间 = 2025 年 1 月**，来源是她自己维护的 ORCID 雇佣记录：`Mohamed bin Zayed University of Artificial Intelligence | Assistant Professor | Computer Vision | 2025-01 →（至今）`。`https://orcid.org/0000-0002-6644-1250`
- MBZUAI 官方 bio 原文："Prior to joining MBZUAI, Xie was a Research Fellow at the University of Adelaide (UoA), and a member of the Australian Institute for Machine Learning (AIML)."（官网用 **she**）
- 个人主页：`https://ytongxie.github.io/`
- **交叉验证的漂亮一笔**：UniMiSS 的 arXiv PDF 首页把 ORCID 直接印在作者名后——`Yutong Xie1[0000−0002−6644−1250]`——与 RADAR PubMed 记录里 #12 Yutong Xie 的 ORCID **完全一致**。所以 RADAR 的谢雨彤 = UniMiSS 的谢雨彤，零歧义。`https://arxiv.org/pdf/2112.09356`

### ④ Zilin Lu、Shaoteng Zhang —— 两个"被误读成放射科医生"的西工大人（把握：确认）
这是本次的意外收获，也是判定 #5 消歧问题的关键铺垫：

| RADAR 里的单位 | ORCID 记录的真实出身 |
|---|---|
| Zilin Lu：达摩院 + **宁波二院放射科** | ORCID `0000-0003-2437-283X` → **Education: Northwestern Polytechnical University** |
| Shaoteng Zhang：达摩院 + **宁波二院放射科** | ORCID `0009-0005-4976-6351`（显示名 "st zhang"）→ **Employment: Northwestern Polytechnical University** |

- `https://orcid.org/0000-0003-2437-283X` · `https://orcid.org/0009-0005-4976-6351`
- Zilin Lu 的全部 10 篇著作是医学 VQA / 半监督分割（TMI ×4、TIP、CVPR、MICCAI），合著者固定是 **Yong Xia + Yutong Xie + Qi Wu**，单位一律写 "National Engineering Laboratory for Integrated Aero-Space-Ground-Ocean Big Data Application Technology, School of Computer Science and Engineering, **Northwestern Polytechnical University**"。**他不是放射科医生，是夏勇的博士生。**
- 也就是说：==挂"宁波二院放射科"的三个人（Zilin Lu / Shaoteng Zhang / Yong Xia）全部是西工大人，没有一个是临床放射科医生。== 这把"宁波二院"从"临床合作单位"重新定性为"这支西工大队伍在浙江的落地署名"。

### ⑤ Yong Xia —— 见下节，单独判定

---

## 2. AIML（Australian Institute for Machine Learning）

| 项 | 事实 | 来源 |
|---|---|---|
| 成立 | **2018 年**，由阿德莱德大学的 Australian Centre for Visual Technologies (ACVT) 改组而成 | `https://en.wikipedia.org/wiki/Australian_Institute_for_Machine_Learning` |
| 创始所长 | **Anton van den Hengel** | 同上 |
| 现任所长 | **Simon Lucey**（2020 年 10 月上任） | 同上 |
| 规模 | "As of 2025, AIML is host to over **70 research students**"；自称澳大利亚**最大的高校机器学习研究组** | 同上 |
| 经费 | 南澳州政府 A$7.1M（2018）、Centre for Augmented Reasoning A$20M（2021）、Responsible AI Research Centre A$20M（2024）、Industrial AI Program A$12M（2024）、CommBank A$6M（2024） | 同上 |
| 地址 | Lot Fourteen, 384–392 North Terrace, Adelaide SA 5000 | `https://www.adelaide.edu.au/aiml/about` |
| 归属变更 | "In 2026, AIML became an entity of **Adelaide University** following the merger between the University of Adelaide and the University of South Australia." | Wikipedia 同上 |

**医学影像 AI 方向的核心 PI（按与本条线的相关度排）**：
1. **Johan Verjans** —— AIML **Deputy Director, Medical Machine Learning（2017–2024）**；同时是 Royal Adelaide Hospital 的 Consultant Cardiologist 和 Jones Radiology 顾问，2019 年起任南澳健康与医学研究所（SAHMRI）AI 平台负责人。**他正是谢雨彤 2020–2021 公派联培的两位导师之一。** `https://researchers.adelaide.edu.au/profile/johan.verjans`
2. **Gustavo Carneiro** —— 曾任阿德莱德大学教授、ARC Future Fellow、**AIML 医学机器学习方向主任**；现已转去英国萨里大学 CVSSP 任 Full Professor。`https://www.surrey.ac.uk/people/gustavo-carneiro`
3. **Qi Wu（吴琦）** —— 视觉-语言方向主任，医学是他 VQA/报告生成能力的应用出口（PairAug、MedCutMix 都是"通用 VLM 方法 → 放射科"的迁移）。
4. **Chunhua Shen（沈春华）** —— 见第 5 节，他是把这条线接到浙大的那个接口。

> **读法**：AIML 不是一家医学影像研究所，它是一家**通用视觉/视觉-语言研究所**，医学是它的下游应用场。RADAR 需要的恰恰是这个——把 VQA/报告生成的通用方法搬进腹部 CT。所以论文里 Adelaide 那一格只有 2 个人、且都是方法人而非临床人。

---

## 3. MBZUAI（穆罕默德·本·扎耶德人工智能大学）

来源全部为官方 About 页：`https://mbzuai.ac.ae/about/`

- **2019 年**由阿联酋决策层设立，定位为**"世界上第一所研究型、研究生层次、专攻人工智能的大学"**（the world's first graduate-level, research-based AI university），首任董事会主席 H.E. Dr. Sultan Ahmed Al Jaber。
- 2020 年 11 月宣布 **Eric Xing（邢波）** 为创校校长。
- 2021 年 1 月首批 78 名研究生入校，来自 29 个国家；2023 年 11 月授出第一个博士学位；2024 年进入 CSRankings 核心 AI 方向全球前十；2025 年 8 月才迎来第一批本科生。
- 校区在阿布扎比 **Masdar City**（与 RADAR 单位串完全一致）。
- 官方点名的应用领域含 healthcare。谢雨彤所在的建制是 **Division of Computing and Mathematical Sciences 下的 Computer Vision**。

> **读法**：MBZUAI 是一所"用钱把全球 AI 人才直接买过来"的新校——2019 年建校、2025 年才有本科生，师资只能靠挖。谢雨彤 2025 年 1 月以助理教授身份落地，正是这个模式的标准样本：**西工大出苗、阿德莱德养成、阿布扎比给教职**。

---

## 4. 西北工业大学 夏勇（Yong Xia）

**存在、职务、方向（把握：确认）**
- 个人主页首句（NWPU 官网有 JS 反爬，正文经搜索引擎快照取得）："**夏勇，男，西北工业大学长聘教授、博士生导师，国家级青年人才计划入选者，空天地海一体化大数据应用技术国家工程实验室成员**……" `https://teacher.nwpu.edu.cn/yongxia.html`
- 英文单位串（他论文里最常用的一版）："National Engineering Laboratory for Integrated Aero-Space-Ground-Ocean Big Data Application Technology, School of Computer Science and Engineering, Northwestern Polytechnical University, 1 Dongxiang Road, Chang'an District, Xi'an, Shaanxi, 710072"，邮箱 **`yxia@nwpu.edu.cn`**。
- **两个 Ningbo/Shenzhen 附属单位**（这点非常关键，见下节）：他近年论文常并列
  - `Ningbo Institute of Northwestern Polytechnical University, 218 Qingyi Road, Gao'xin District, **Ningbo**, Zhejiang, **315048**`
  - `Research & Development Institute of Northwestern Polytechnical University in Shenzhen, 518057`
  例：PMID **40618465**（Med Image Anal 2025）、PMID **39173412**（Med Image Anal 2024）、*Spot the Difference*（MICCAI 2024）、*PICK*（IJCV 2025）、*PathBot*（JBHI 2025）。
  西北工业大学宁波研究院：2019 年 9 月注册成立，宁波市人民政府与西工大合建的科研事业单位。`https://ningbo.nwpu.edu.cn/`

**与 Jianpeng Zhang / Yutong Xie 的师生关系（把握：确认）**
- **DoDNet**（CVPR 2021, arXiv 2011.10217）PDF 首页：
  ```
  Jianpeng Zhang*1,2 , Yutong Xie*1,2 , Yong Xia1 , and Chunhua Shen2
  1 School of Computer Science and Engineering, Northwestern Polytechnical University, China
  2 The University of Adelaide, Australia
  {james.zhang, xuyongxie}@mail.nwpu.edu.cn; yxia@nwpu.edu.cn; chunhua.shen@adelaide.edu.au
  ```
  ==张剑鹏(Jianpeng Zhang) 和谢雨彤两人用的都是 `@mail.nwpu.edu.cn` 学生邮箱，同时挂西工大 + 阿德莱德——标准的国家公派联合培养格式。== `https://arxiv.org/pdf/2011.10217`
- **UniMiSS**（ECCV 2022, arXiv 2112.09356）：作者 = **Yutong Xie(Adelaide), Jianpeng Zhang(NWPU), Yong Xia(NWPU), Qi Wu(Adelaide, 通讯)**。到 2022 年谢雨彤的第一单位已翻成 Adelaide。`https://arxiv.org/pdf/2112.09356` · 代码仓 `https://github.com/YtongXie/UniMiSS-code`
- **TransDoDNet / UniMiSS+**（TPAMI）沿用同一作者班底。`https://github.com/jianpengz/DoDNet`
- 顺带：**RADAR 作者表 #12→#13→#14 的排序 = Yutong Xie → Yong Xia → Qi Wu，和 UniMiSS 的 Xie–Xia–Wu 完全同序**。这不是巧合，是整块搬过来的师承组。

---

## 5. ⚠️ 关键消歧判定：#13 Yong Xia 是谁

### 结论：**是同一个人——西北工业大学 夏勇教授。把握 95%+（"极高"，只差一份他本人或宁波二院的公开说明）。**

**决定性证据：ORCID。**

RADAR 的 PubMed 记录给 #13 Yong Xia 带了 ORCID **`0000-0001-9273-2847`**（`data/pubmed-42752131.xml` 内 `<Identifier Source="ORCID">`）。拿这个号去 Crossref 反查：

```
GET https://api.crossref.org/works?filter=orcid:0000-0001-9273-2847
→ total-results: 111
```

这 111 篇里，凡是 Crossref 带了单位串的，写的全是：
- "National Engineering Laboratory for Integrated Aero-Space-Ground-Ocean Big Data Application Technology, School of Computer Science and Engineering, **Northwestern Polytechnical University**, Xi'an, China"

涵盖 IEEE-TMI、IEEE-TPAMI、IJCV、Medical Image Analysis、Pattern Recognition、IEEE-TIP 等，年份从 2017 横跨到 2026。**同一个 ORCID，既出现在 111 篇西工大医学影像 AI 论文上，也出现在 Science 这篇标着"宁波二院放射科"的论文上。** ORCID 是作者本人维护、投稿时由本人绑定的标识，不是期刊自动匹配的——这是能拿到的最强一手证据。

**四条旁证，方向一致：**

1. **合著网络完全重合。** RADAR 里与他同块的 Yutong Xie(#12)、Qi Wu(#14)、Jianpeng Zhang(#2)、Zilin Lu(#4)，正是 DoDNet / UniMiSS / PairAug / PICK / Spot-the-Difference 的固定班底。一个真·地级市医院放射科医生不会同时是这五个人的共同作者。
2. **研究方向完全重合。** 他 ORCID 名下这篇 Science 的隔壁是 TMI/TPAMI 的分割、自监督、噪声标签——RADAR 论文本身就是这套方法的产品化。
3. **同块另外两人已被证伪为"医生"。** 同挂"宁波二院放射科"的 Zilin Lu 和 Shaoteng Zhang，ORCID 记录显示一个是西工大在读/毕业博士、一个受雇于西工大。==既然 7 号单位下的另外两人都不是放射科医生，7 号单位就不是一个"临床医生栏"。==
4. **地理对得上。** 夏勇本人常年并列 **西北工业大学宁波研究院（宁波高新区，315048）**。他在宁波有实体落点，"宁波"不是天外飞来的城市。

**反向排查（找不到反证）：**
- PubMed 全库检索 `Xia Y[Author] AND "Ningbo No. 2 Hospital"[Affiliation]`，4 条命中全部是同名异人（夏尧佳/宁波大学呼吸科等），**没有任何一位宁波二院放射科的 Xia Y**。
- 中文检索 `"夏勇" 宁波市第二医院`、`宁波市第二医院 放射科 夏勇`，命中的是上海第二工业大学、济宁医学院、国务院法制办等完全无关的同名者，**宁波二院官网与各医生库（百度健康 / 好大夫 / 39 / 复禾）均查不到放射科医师夏勇**。
- 西工大主页与宁波研究院官网均**未提及**与宁波市第二医院的合作。

**那"宁波二院放射科"这个单位怎么解释？**
只能给两种并存的可能，均为**推断**，请在仓库里明确标注：
- (a) **署名压缩/错误**：西工大整块从作者单位表里消失了（26 个单位里一次都没出现），三个西工大人被统一归到了数据来源医院名下；夏勇还额外丢掉了达摩院那一格（Zilin Lu 和 Shaoteng Zhang 至少还留着"达摩院 +"）。
- (b) **真实的嵌入式安排**：这支西工大队伍通过宁波研究院落地浙江，宁波二院是其数据/临床合作点，投稿时按"实际驻点"署名。

我个人倾向 (a) 为主、(b) 为背景——因为如果是有意的临床双聘，没有理由把西工大这个主单位整个删掉。

> **给读者的一句话**：==Science 这篇论文把一位西北工业大学的长聘教授印成了宁波一家市级医院放射科的人。== 这本身就是"临床方拥有这项工作"那条叙事的一个副作用——单位表是按临床数据来源组织的，不是按学术建制组织的。

---

## 6. 这条"西工大 → Adelaide → MBZUAI/达摩院"是不是成规模通道

**是，而且有制度化的机制（国家公派联合培养），不是零星个案。** 举证：

| 人 | 西工大段 | Adelaide 段 | 出口 |
|---|---|---|---|
| **谢雨彤 Yutong Xie** | 2021 博士毕业，导师**夏勇** | 2020.01–2021.04 **国家公派联培**（沈春华 + Johan Verjans）→ 2021.04 起 AIML 博后（**吴琦**，V3ALab） | **2025.01 MBZUAI 助理教授** |
| **Jianpeng Zhang** | `james.zhang@mail.nwpu.edu.cn`，DoDNet 挂 NWPU | DoDNet/TransDoDNet 同时挂 Adelaide（沈春华） | **达摩院 + 湖畔实验室 + 浙大计算机学院**（RADAR #2）；ORCID 雇佣栏写 Zhejiang University |
| **Zilin Lu** | ORCID Education = NWPU，博士期间论文全部 NWPU（夏勇） | 与 Yutong Xie / Qi Wu 常年合著（PICK、PEFAT、Spot-the-Difference） | **达摩院**（RADAR #4） |
| **Shaoteng Zhang** | ORCID Employment = NWPU | — | **达摩院**（RADAR #11） |
| **Sinuo Wang** | 郑州大学本科 | **吴琦在读博士生**（V3ALab People 页） | **达摩院实习**（2025–2026 两篇论文单位直接写 DAMO Academy） |
| **沈春华 Chunhua Shen** | — | 阿德莱德大学正教授（谢/张二人的联培导师） | **2022 年起浙江大学求是讲席教授** `https://cshen.github.io/` |

**通道的三个结构性特征：**

1. **入口是制度，不是人情。** 谢雨彤走的是"国家公派联合培养"（CSC），这是国家级、按年招标的批量项目。夏勇实验室（挂靠张艳宁的空天地海一体化大数据应用技术国家工程实验室）常年往 Adelaide 送人，DoDNet 那种"一篇论文两个作者同时挂 NWPU+Adelaide"的格式就是批量化的痕迹。

2. **中转站会自我复制。** 谢雨彤从"被吴琦带的博后"变成"和吴琦一起带 Sinuo Wang 的准 PI"，再拿到 MBZUAI 教职后继续在 AIML 招人（她主页公开招 PhD/实习生）。V3ALab People 页上她已在 Alumni 栏、Sinuo Wang 还在 PhD 栏——**一代人带下一代人，通道自己延长了。**

3. **出口在国内收口。** 沈春华 2022 年从 Adelaide 回浙大任讲席教授，而 RADAR 的 6 号单位正是"浙江大学计算机学院"（Jianpeng Zhang、Weiwei Cao、Yanjie Zhou、Zhongyi Shui、Xi Li 五人）。==这条线出国时走的是阿德莱德，回国时落在杭州：浙大计算机学院 + 湖畔实验室 + 达摩院这三重挂名，就是出口端的接驳口。== 附带一个可查的活证据：RADAR 发表的同期还有一篇 *Rethinking the Efficiency and Effectiveness of RL for Radiology Report Generation*，作者 = Zilin Lu, Ruifeng Yuan, Weiwei Cao, Wanxing Chang, Zhongyu Wei, **Sinuo Wang**, **Yong Xia**, Ling Zhang, Jianpeng Zhang——西工大 + Adelaide + 达摩院同框，说明这不是为一篇 Science 临时拼的班子。

**克制一点的说法**：我能证明这条线在**夏勇–沈春华–吴琦**这个三角上是成规模的、持续十年的、有制度入口的；我**不能**声称它是"中国医学影像 AI 里最主要的通道"——没有做过全国范围的定量比较（OpenAlex 的机构级共著计数今天配额用尽，跑不出来）。这一条建议在 README 里留白或后续补。

---

## 7. 待办与风险提示

- **不要按拼音猜中文名。** 本次只坐实两个：**Qi Wu = 吴琦**、**Yong Xia = 夏勇**、**Yutong Xie = 谢雨彤**（三个都有中文一手来源）。Sinuo Wang / Zilin Lu / Shaoteng Zhang / Jianpeng Zhang 的中文名**没查到可引用的来源**，`Jianpeng Zhang` 我试过"张剑鹏"但检索无果，**不要写进表**。
- **骨架表需要改一处**：`sources/authors-affiliations.md` 里说"两个达摩院研究员同时挂一家地级市医院的放射科"并推测他们"本身是放射科医生被达摩院聘用"——这条已被 ORCID 证伪，Zilin Lu 与 Shaoteng Zhang 都是西工大出身的方法研究者。
- 同文件里"在那份判定出来之前，不要假设这两个是同一个人"——现在可以改为**同一人，ORCID 证据，把握 95%+**。

**本地证据文件**（我这次生成/使用的）：
- `/Users/shunie/Developer/damo-radar-research-map/data/pubmed-42752131.xml`（含全部 ORCID，是本次判定的源头）
- `/private/tmp/claude-501/-Users-shunie-Developer/152a37b5-0538-44e5-b0f8-ccce9c6bab33/scratchpad/cr-xia.json`（Crossref 反查 ORCID 0000-0001-9273-2847 的 111 篇）
- 同目录 `orcid-0000-0002-6644-1250.json`（谢雨彤 MBZUAI 任职起始月）、`orcid-0000-0003-2437-283X.json`、`orcid-0009-0005-4976-6351.json`
- 同目录 `2011.10217.pdf`（DoDNet，西工大+Adelaide 双挂的原始页）、`2112.09356.pdf`（UniMiSS，ORCID 印在作者名后）

**复现关键两步：**
```bash
# 1. 从论文原始记录取 ORCID
curl -sL "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=42752131&retmode=xml" \
  | grep -B4 '0000-0001-9273-2847'
# 2. 用 ORCID 反查该作者的全部著作单位
curl -s "https://api.crossref.org/works?filter=orcid:0000-0001-9273-2847&rows=30&select=title,author"
```

**Sources:**
- [RADAR PubMed 记录 (PMID 42752131)](https://pubmed.ncbi.nlm.nih.gov/42752131/) · [Crossref 10.1126/science.aec6129](https://api.crossref.org/works/10.1126/science.aec6129)
- [Qi Wu — Adelaide Researcher Profile](https://researchers.adelaide.edu.au/profile/qi.wu01) · [V3ALab](https://v3alab.github.io/) · [V3ALab People](https://v3alab.github.io/people/)
- [谢雨彤 CSIG 博士学位论文激励计划专访](https://www.csig.org.cn/67/202404/51784.html) · [Yutong Xie 个人主页](https://ytongxie.github.io/) · [MBZUAI 教师页](https://mbzuai.ac.ae/study/faculty/yutong-xie/) · [ORCID 0000-0002-6644-1250](https://orcid.org/0000-0002-6644-1250)
- [夏勇 西北工业大学个人主页](https://teacher.nwpu.edu.cn/yongxia.html) · [西北工业大学宁波研究院](https://ningbo.nwpu.edu.cn/) · [ORCID 0000-0001-9273-2847](https://orcid.org/0000-0001-9273-2847)
- [ORCID 0000-0003-2437-283X (Zilin Lu)](https://orcid.org/0000-0003-2437-283X) · [ORCID 0009-0005-4976-6351 (Shaoteng Zhang)](https://orcid.org/0009-0005-4976-6351)
- [DoDNet arXiv:2011.10217](https://arxiv.org/pdf/2011.10217) · [UniMiSS arXiv:2112.09356](https://arxiv.org/pdf/2112.09356) · [UniMiSS 代码仓](https://github.com/YtongXie/UniMiSS-code) · [DoDNet 代码仓](https://github.com/jianpengz/DoDNet)
- [AIML — Wikipedia](https://en.wikipedia.org/wiki/Australian_Institute_for_Machine_Learning) · [AIML About](https://www.adelaide.edu.au/aiml/about) · [Johan Verjans](https://researchers.adelaide.edu.au/profile/johan.verjans) · [Gustavo Carneiro — Surrey](https://www.surrey.ac.uk/people/gustavo-carneiro)
- [MBZUAI About us](https://mbzuai.ac.ae/about/) · [Adelaide University — Wikipedia](https://en.wikipedia.org/wiki/Adelaide_University) · [Chunhua Shen 主页](https://cshen.github.io/)