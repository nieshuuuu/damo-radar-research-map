# 达摩院医疗 AI 的组建史与血统

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../figures/damo-lineage.dark.png">
  <img alt="一支队伍走过的四站：NIH Clinical Center 产出 ChestX-ray14 与 DeepLesion，被挖到隔壁的平安 PAII，2021 整队迁移到达摩院，吕乐一人去蚂蚁" src="../figures/damo-lineage.light.png">
</picture>

> 🖼 交互版 → [../figures/damo-lineage.html](../figures/damo-lineage.html)｜图源 [../figures/damo-lineage.lifecycle.json](../figures/damo-lineage.lifecycle.json)


一句话脉络：**这支队伍的根在 NIH 临床中心 Ronald Summers 的影像实验室；2018 年被平安集团的美国研究院 PAII Inc. 整建制挖到 3 公里外的 Bethesda 办公楼；2021 年 7 月又整建制转投阿里达摩院，嫁接到达摩院原有的杭州医疗线上；2025—2026 年领队吕乐离开，去了蚂蚁。**

---

## 0. 证据来源

人员流动用**论文署名单位的年度迁移**重建：PubMed E-utilities（`[Affiliation]` 精确检索）、OpenAlex（`raw_affiliation_strings`）、Wayback Machine（已关站的 PAII 官网）、当事人主页。署名单位带时间戳、第三方可复核，但**发表滞后于实际任职 6–18 个月** —— 下文的年份凡没注明出处的，都是论文年，不是入职年。数据快照在 `data/raw/evidence/`。

---

## 1. 吕乐（Le Lu）履历

主证据是他本人的主页 <https://lelu007.github.io/>。这个主页自 2022 年起没有更新过（Wayback 快照与今天逐字相同），所以 2021 年以后的事以论文署名为准。

**中文名 = 吕乐**，一手证据在他自己主页的论文列表里：

> 深度学习和医学影像在预防医学中的机会 ； **吕乐**， 吴山东, 放射学实践， 2018年10月，应邀特刊

（同一条还顺带给出 Shandong Wu = 吴山东。）

### 履历

| 时间 | 单位 · 职位 | 出处 |
|---|---|---|
| 1996-07 | 北京工业大学（旧英文名 Beijing Polytechnic University）机械工程与自动控制 本科 | 主页 |
| 1996–1999 | 中科院自动化所 NLPR 研究生，导师**胡占义** | 主页 |
| 2000–2001、2004 夏 | Microsoft Research 实习；导师沈向洋、Kentaro Toyama、张正友、权龙 | 主页 |
| 2004-05 / 2007-05 | Johns Hopkins 计算机 MSE / PhD，导师 **Gregory D. Hager** | 主页 |
| 2006-10 – 2009-10 | Siemens Corporate Research（Princeton NJ），Research Scientist | 主页 |
| 2009-11 – 2011-10 | Siemens Medical Solutions **CAD Group**（Malvern PA），Staff Scientist | 主页 |
| 2011-11 – 2013-01 | Siemens Corporate Research，Senior Staff Scientist, Image Analytics and Informatics | 主页 |
| 2013 – 2018-06 | **NIH Clinical Center** 放射与影像科学系，Clinical Image Processing Service；自述"五年多" | 主页 + DeepLesion 署名 |
| 2018-06 – 2021-07 | **PAII Inc. Bethesda Research Lab**，Research Director → Executive Director | 主页 + PAII 官网 2019 快照 |
| 2021-07 之后 – 2025/26 | **阿里巴巴达摩院**，全球医疗 AI 研发负责人 | 主页；2025-09 仍署达摩院 |
| 2026-03 起（论文署名）| **蚂蚁 Medical AI Lab**，Sunnyvale CA | *Nat Commun* 2026, PMID 42426002 |

Siemens 三段合计 6 年多，是他进达摩院之前最长的一段，而且中间那段就在 Medical Solutions 的 **CAD 产品组** —— 路径是工业界 → 政府医院 → 工业界，不是学术 → 工业。

主页里另有一句无日期的 "and from NVIDIA AI-Infra division"；时间线上没有对应的空档，也没有任何一篇署 NVIDIA 的论文。更可能的读法是"我的团队来自 NIH 和 NVIDIA" —— NVIDIA 的医学影像研究组当时也在 Bethesda（见 §5）。

他还做过香港中文大学电子工程系的访问学生。也就是说，去 JHU 之前他就已经在华人计算机视觉的核心圈里。

### 去蚂蚁

2026 年 *Nature Communications* 一篇神经母细胞瘤视觉—语言模型论文（PMID 42426002）的署名是：

> **Le Lu :: Ant Group, Sunnyvale, CA, USA.**

同篇的 Sen Yang 也署 Ant Group Sunnyvale。另外蚂蚁的医疗单位在中国侧的正式署名是 "**Ant Healthcare (AFU), Ant Group, Hangzhou, Zhejiang, China**"（*Annals of Oncology* 2026, PMID 42463045）。

两点值得注意：

- 他**人还在美国**（Sunnyvale，硅谷），不是回杭州。蚂蚁的医疗 AI 是"杭州 AFU + Sunnyvale"的双点结构，和他在达摩院时期的"杭州 + 纽约"是同一个套路。
- **他基本是一个人走的。** 蚂蚁 2025—2026 全部 1221 篇论文的署名单位里，逐篇检查是否出现达摩院/PAII 旧部（柯岩 Ke Yan、金大凯 Dakai Jin、Ling Zhang、姚佳文 Jiawen Yao、夏英达 Yingda Xia、唐有宝 Youbao Tang 等 15 人）——**零命中**。核心班底留在了达摩院。

换岗的确切月份没有公开来源：他 2025-09 的 arXiv 论文仍署达摩院，2026-03 起署蚂蚁。

---

## 2. PAII Inc. 到底是什么

**答案：平安集团的美国 AI 研究院。** 这一条有它自己官网的一手证据。官网 `www.paii-labs.com` **现已死亡**（DNS 解析失败），但 Wayback 存有全站。

### 自述（2019-08-21 与 2023-10-17 两版快照文字完全相同）

> PAII Inc. was founded in **2016**. ... PAII Inc. has two R&D laboratory offices in **Palo Alto, California** and **Bethesda, Maryland**, respectively.

<https://web.archive.org/web/20190821004426/http://www.paii-labs.com/index>

### 与平安的关系——招聘页说得最直白

招聘页的职位描述里直接写：

> "**PingAn Technology, US Research Lab at Silicon Valley**, is looking for brilliant and creative minds..."
>
> "...to accelerate **PingAn group's transition to a technology driven enterprise**."

<https://web.archive.org/web/20190821010800/http://www.paii-labs.com/jobs>

所以 PAII = 平安科技的美国研究院，没有悬念。旁证：论文邮箱域名是 `paii-labs.com`（`zhangling300@paii-labs.com`、`jindakai376@paii-labs.com`、`yaojiawen076@paii-labs.com`）；而 2023 年 *Radiology* 那篇胰腺癌论文的署名同时列出 "Ping An Technology, Shanghai, China" 与 "PAII Inc, Bethesda, Md"。

### 地址与规模

| 站点 | 地址 | 负责人（2019 年官网新闻页） |
|---|---|---|
| Palo Alto | 5 Palo Alto Square Suite 150, 3000 El Camino Real, Palo Alto, CA 94306 | Dr. **Mei Han**, Director of Silicon Valley Lab |
| Bethesda | **6720B Rockledge Drive Suite 410, Bethesda, MD 20817** | Dr. **Le Lu**, Research Director of Bethesda Lab |

<https://web.archive.org/web/20190821010049/http://www.paii-labs.com/contact>

**这个地址是整个故事的关键。** NIH 临床中心在 Building 10, 10 Center Drive, Bethesda, MD 20892（<https://irp.nih.gov/pi/ronald-summers>）。两点的直线距离**约 3.5 公里**——用 OpenStreetMap Nominatim 取坐标（Rockledge Drive 39.0242N/77.1325W，NIH 临床中心 39.0016N/77.1045W）后按球面近似算得，不是目测。

**平安没有去硅谷挖这批人，它把实验室直接开在了 NIH 步行可达的地方**，然后把 Summers 组做影像深度学习的那批人整建制搬过来。对照 PAII 另一个站点在 Palo Alto——公司完全有能力把人集中到硅谷，却专门为这支队伍在马里兰单开一个点。这个选址本身就说明：**被挖的不是几个人，是一个已经成形、不愿意搬家的组。**

### 四个研究方向

官网 ResearchAreas 页列了四块：① 金融科技（投资与保险）；② 智慧城市；③ 智慧教育；④ 医疗影像与临床信息学。医疗那条写得最具体：

> "cancer early detection through prevention imaging; emergency medicine imaging, quantitative and precision medicine and tumor modeling to support longitudinal tumor+organ oncology imaging"

<https://web.archive.org/web/20190821004644/http://www.paii-labs.com/ResearchAreas>

**注意这个方向表述和后来达摩院做的事几乎一模一样**：平扫 CT 癌症早筛（PANDA/GRAPE/COCA/LiON）、急诊影像（iAorta）。研究纲领是从 PAII 原样带走的，换了个东家继续做。

### 后来怎么了

没有任何公开的关闭声明，但**署名证据显示两个站点是分开死的**：

| | 医疗影像核心成员最后一次署 PAII | 备注 |
|---|---|---|
| **Bethesda（医疗）** | 绝大多数在 **2022** 年断档 | Harrison 2022、金大凯 2022、Dazhou Guo 2022、柯岩 2022、Yirui Wang 2022、Bowen Li 2022 |
| **Palo Alto（语音/NLP/通用 AI）** | 一直延续到 **2025—2026** | Mei Han 至 2025、Zhicheng Yang 至 2026、Peng Chang 至 2025、Ruei-Sung Lin 至 2025 |

也就是说：**Bethesda 医疗影像实验室在 2021 年领队出走后即告瓦解，硅谷实验室又活了三四年。** 官网最后一次被存档是 2023-10-17，此后域名注销。

（少量 2023 年的 PAII 医疗署名——如上海长海医院合作的胰腺癌论文——是投稿滞后造成的尾巴，不代表实验室仍在运转。）

---

## 3. 2021 年 PAII → 达摩院的迁徙名单

方法：取"最后一次署 PAII 的论文年"与"第一次署 DAMO 的论文年"，两个集合求交。证据表可在 `data/raw/evidence/oa-paii-affiliations.json` 与 `oa-damo-affiliations.json` 复算。

**再强调一次：这是论文年，不是入职年。** 2022 年首次出现 DAMO 署名，对应的实际入职就是 2021 年下半年。

| 人 | PAII 论文年 | DAMO 首次署名 | 目前（2026） | 判定 |
|---|---|---|---|---|
| **Le Lu 吕乐** | 2019–2023 | 2022 | 蚂蚁 Sunnyvale | 领队，确证 |
| **Ling Zhang** | 2019–2023 | 2022 | 达摩院 Washington DC，通讯作者 | 确证 |
| **Dakai Jin 金大凯** | 2019–2022 | 2022 | 达摩院 New York | 确证 |
| **Dazhou Guo** | 2019–2022 | 2022 | 达摩院 New York | 确证 |
| **Ke Yan 柯岩** | 2020–2022 | 2022 | 达摩院 + 湖畔实验室，**杭州** | 确证；注意他后来去了中国侧 |
| **Jiawen Yao 姚佳文** | 2019–2023 | 2022 | 达摩院 | 确证 |
| **Bowen Li** | 2020–2022 | 2022 | — | 确证 |
| **Yuxing Tang** | 2020–2022 | 2023 | 达摩院（2025 尚在） | 确证 |
| **Fakai Wang** | 2021–2022 | 2023 | — | 确证 |
| **Weijian Li** | 2020–2021 | 2023 | — | 确证 |
| **Yirui Wang** | 2019–2022 | 2024 | 达摩院 New York | 确证，但晚 |
| **Zhilin Zheng** | 2022–2023 | 2024 | 达摩院杭州 | 确证；**他是 RADAR 的第 17 作者** |

合计 12 人。

### 两个不属于这次迁徙的人

- **Yingda Xia 夏英达不是从 PAII 来的。** 他在 PAII 的名单里查无此人，但 2022 年起就有达摩院署名，此后一直是 Washington DC 组的主力（GRAPE、COCA、RADAR）。他的来路是约翰·霍普金斯（与 PAII 同城不同源），不属于这次迁徙。
- **Adam P. Harrison 没有去达摩院**，他是 PAII Bethesda 的二号人物，去向完全不同（见 §5）。

---

## 4. NIH 那条根：Summers 的实验室

### 实验室是什么

**Ronald M. Summers, M.D., Ph.D.**，NIH 临床中心 Senior Investigator，主持 **Imaging Biomarkers and Computer-Aided Diagnosis Laboratory（影像生物标志物与计算机辅助诊断实验室）**，办公室 Building 10, Room 1C224D, 10 Center Drive, Bethesda, MD 20892。

<https://irp.nih.gov/pi/ronald-summers>

该页还给出一条解决关键疑问的信息：

> He directs the Imaging Biomarkers and Computer-Aided Diagnosis (CAD) Laboratory and is the **former and founding Chief of the NIH Clinical Image Processing Service**.

### 吕乐在其中的位置

DeepLesion 论文的署名把四个人分成了两个单位：

| 作者 | 单位 |
|---|---|
| Ke Yan | NIH CC, **Imaging Biomarkers and Computer-Aided Diagnosis Laboratory** |
| Xiaosong Wang | 同上 |
| **Le Lu** | NIH CC, **Clinical Image Processing Service, Radiology and Imaging Sciences** |
| Ronald M Summers | 同 IB-CAD Laboratory |

<https://pubmed.ncbi.nlm.nih.gov/30035154/>

所以**吕乐严格说不在 Summers 的实验室编制内**，他在放射与影像科学系下的临床影像处理服务（CIPS）——而 CIPS 正是 Summers 创立并曾任首任主任的单位。两者是同一支血脉的两个编制格子。**说"吕乐是 Summers 的人"在人事上不准确，在学术谱系上完全准确。**

### 三篇奠基作与各自的去向

**① MICCAI 2014「2.5D 淋巴结检测」——真正的起点**

Holger R. Roth, **Le Lu**, Ari Seff, Kevin M. Cherry, Joanne Hoffman, Shijun Wang, Jiamin Liu, Evrim Turkbey, Ronald M. Summers，"A New 2.5D Representation for Lymph Node Detection Using Random Sets of Deep Convolutional Neural Network Observations"。2018 年获 Kitware/MICCAI **Young Scientist Publication Impact Award**。

PAII 官网的新闻页自己点明了师承关系：

> "the first Author, Dr. **Holger Roth** was a collaborating postdoc fellow with **Dr. Lu and Dr. Summers** by then at National Institutes of Health"

<https://web.archive.org/web/20230608120230/http://www.paii-labs.com/news/detail?type=1>

这篇是整条血统的方法论起点：**2.5D 表示**——用正交切片的多视图替代真 3D 卷积，绕开当年 3D CNN 的显存与样本量瓶颈。后来达摩院平扫 CT 那一整条产品线的骨架都还带着它的影子。

**② ChestX-ray8 / ChestX-ray14（CVPR 2017）**

Xiaosong Wang, Yifan Peng, **Le Lu**, Zhiyong Lu, Mohammadhadi Bagheri, Ronald M. Summers
arXiv:1705.02315（2017-05-05 提交），CVPR 2017 spotlight。
<https://arxiv.org/abs/1705.02315>

注意作者构成：Yifan Peng 与 Zhiyong Lu 来自 NIH 的 NLM/NCBI，是做生物医学 NLP 的。**"从放射报告里挖标签"这个做法在 2017 年就成型了**——而这正是 2026 年 RADAR（读 1500 万解剖级图文对）的方法学祖先。吕乐主页自称这是"IEEE CVPR 五年内被引最多的医学影像论文"。

**③ DeepLesion（JMI 2018）**

Ke Yan, Xiaosong Wang, **Le Lu**, Ronald M. Summers，*J Med Imaging* 5(3):036501，PMID 30035154。
（数据集细节与许可问题见 `data/raw/contact-lineage.md`，此前已核实。）

**两个一作现在在哪：Xiaosong Wang → 上海人工智能实验室；Ke Yan → 达摩院杭州 + 湖畔实验室。** 详见下节。

---

## 5. 散点去向（逐人给证据）

| 人 | 现职 | 证据 |
|---|---|---|
| **Holger Roth** | **NVIDIA**，Santa Clara, CA；NVIDIA FLARE（联邦学习）团队 | 个人主页自述 "Since **June 2018**, I am a Senior Applied Research Scientist at **NVIDIA's deep learning for medical imaging research group based in Bethesda, Maryland**" <https://sites.google.com/site/holgerrroth/home>；2025–2026 论文署 "NVIDIA FLARE Team, NVIDIA Corporation, Santa Clara, CA"（PubMed `Roth HR[Author] AND 2024:2026[dp]`）。之前：名古屋大学森研究室特任助教 → NIH CC 访问研究员 → UCL 博士 |
| **Xiaosong Wang** | **上海人工智能实验室**，AI4S 方向 principal researcher | 个人主页 <https://xiaosongwang.github.io/>：Shanghai AI Lab ← **Alibaba DAMO Academy（senior staff algorithm engineer）** ← NVIDIA **2018–2021** ← NIH CC **2015–2018** 访问研究员 ← 联影 2013–2015 产品经理；博士 University of Bristol 2011，导师 Majid Mirmehdi |
| **Adam P. Harrison** | **Riverain Technologies**，Miamisburg, OH（Research Division） | 2023 与 2026 论文署 "Research Division, Riverain Technologies, Miamisburg, OH 45342, USA"；2022 年另有一篇署 Q Bio Inc, San Carlos, CA；最后一次署 PAII 是 2022 |
| **Ke Yan 柯岩** | **达摩院 + 湖畔实验室，杭州**；`yanke.yan@alibaba-inc.com` | 2026 年多篇署 "Hupan Laboratory, Hangzhou" 与 "DAMO Academy, Alibaba Group, Hangzhou"；另有一篇署 DAMO New York。是 LiON 的通讯作者之一 |
| **Youbao Tang 唐有宝** | **Google**，Senior Software Engineer，美国 | 个人主页 <https://tangyoubao.github.io/>（页头直接给了中文名"唐有宝"）；最后一次署 PAII 是 2022 |
| **Ling Zhang** | **达摩院，Washington DC**；`ling.z@alibaba-inc.com` | 平扫 CT 癌症筛查主线的通讯作者：GRAPE（PMID 40555751）、COCA（PMID 42025761）、LiON（PMID 42618635）、RADAR（PMID 42752131） |
| **Yingda Xia 夏英达** | **达摩院，Washington DC** | 同上一组，GRAPE / COCA / RADAR / 脂肪肝多模态（PMID 41672973） |

**一个此前没有被注意到的发现：Xiaosong Wang 也在达摩院待过。** 他的路径是 NIH → NVIDIA → 达摩院 → 上海人工智能实验室，和吕乐那批人是**两次独立**地在 NIH 和达摩院交汇。这条线索此前在本项目的任何文件里都没出现过。

**Bethesda 的三角结构**：NIH 临床中心、平安 PAII、NVIDIA 医学影像组——**三家都在 Bethesda，都在 2015—2021 年间从同一个人才池里抓人**。Holger Roth 去了 NVIDIA、Xiaosong Wang 先 NVIDIA 后达摩院、Ke Yan 和吕乐去了 PAII 再到达摩院。这不是三次孤立的跳槽，是一个几平方公里内的人才市场。

---

## 6. 达摩院医疗 AI 在美国的实体现状

### 地址与沿革

| 站点 | 论文署名字符串 | 出现年份 |
|---|---|---|
| Seattle, WA | "Alibaba DAMO Academy, Seattle, WA" | 2021（仅 1 次，非医疗） |
| **New York** | "Alibaba DAMO Academy USA, **860 Washington Street, 8F, NY**"；"DAMO Academy, Alibaba Group, New York, NY **10014**" | 2022 → 2026，持续 |
| **Washington DC** | "DAMO Academy, Alibaba Group, Washington, DC, USA" | 2025 → 2026 |

### 两个点并存，对应两支队伍

**New York 与 Washington DC 两个地址在 2026 年同时存在**：

| | **Washington DC 组** | **New York 组** |
|---|---|---|
| 人 | Ling Zhang（通讯）、Yingda Xia | Dakai Jin、Le Lu、Ke Yan、Dazhou Guo、Yirui Wang、Zi Li、Qinji Yu、Haoshen Li |
| 方向 | **平扫 CT 癌症早筛**：GRAPE（胃癌）、COCA（结直肠癌）、LiON（肝癌）、RADAR、脂肪肝多模态 | **头颈肿瘤放疗与淋巴结**：OAR 自动勾画、DeepENE 结外侵犯（PMID 41528225） |
| 期刊面貌 | *Nature Medicine* / *Science* / *Annals of Oncology* | *Radiology* / *Nature Communications* |

代表性证据：RADAR（PMID 42752131）的末两位达摩院作者 Yingda Xia 与 Ling Zhang 均署 "Alibaba DAMO Academy, **Washington, DC**"；而 DeepENE（PMID 41528225）的八位达摩院作者全部署 "DAMO Academy, Alibaba Group, **New York, NY**"。

**一个有证据支持但尚未证实的推测**：DC 组很可能是"没搬家的 Bethesda 遗民"。Bethesda 属于华盛顿都会区，Ling Zhang 正是从 PAII Bethesda 过来的，Yingda Xia 来自同一都会区的霍普金斯。纽约那个 860 Washington Street 是达摩院美国的注册办公地址，而 DC 是这几个人实际所在地。**削弱这个推测的反例**：Dakai Jin 同样出自 PAII Bethesda，却署纽约。所以只能当假说，不能当结论。

### 吕乐离开后还剩什么

- **人还在，且是主力。** 2026 年出的 *Science*（RADAR）、*Nature Medicine*（LiON）、*Annals of Oncology*（COCA）三篇旗舰，通讯作者都是 **Ling Zhang**，不是吕乐。DC 组的产出没有因为他走而中断。
- **他没有带走任何人**（见 §1，蚂蚁 1221 篇论文零命中旧部）。
- **NY 组仍在活动**，2026 年仍有 8 人联名的 *Radiology* 论文。
- **是否还在招人：本次无法核实。** 需要访问阿里巴巴招聘系统或领英，两者在本环境都不可达。**这一条请当作未回答，不要填猜测。**

---

## 7. 组建史：2021 是嫁接，不是建院

达摩院在吕乐到来之前已经有一条医疗线，在杭州，方向完全不同：

| 时间 | 建制名称（论文署名原文） | 人 | 方向 |
|---|---|---|---|
| **2020** | "**HealthTech Division**, DAMO Academy" | Heng Guo、Xian-Sheng Hua | 脑机接口 SSVEP、生信 |
| **2021** | "**Healthcare Intelligence, AIC**（AI Center）, DAMO Academy, Alibaba Group, Hangzhou" | Ying Chi | 通用病灶检测、肿瘤新抗原（TSNAD/TSNAdb）、胃癌基因组分型 |
| **2021–2022** | "**Alibaba-Zhejiang University Joint Research Center of Future Digital Healthcare**" | Ying Chi、Xun Gu | 阿里—浙大联合，这是后来 RADAR 那条浙大关系的制度前身 |
| **2023 起** | 普遍增加 "**Hupan Lab / Hupan Laboratory（湖畔实验室）**, Hangzhou" 双署名 | 全员 | 2023/24/25/26 年分别出现 92 / 86 / 112 / 140 次 |

所以真实的组建史是**嫁接，不是从零建院**：

1. **2020 年前后**，达摩院已有 HealthTech Division / Healthcare Intelligence（AI Center 下），由 **Xian-Sheng Hua** 一线负责，做的是生信、基因组、通用病灶检测，学术面貌接近"数据挖掘 + 生物信息"。
2. **2021 年下半年**，吕乐带着 PAII Bethesda 的整支影像队伍接入，把"平扫 CT + 大规模多中心 + 癌症早筛"这套 NIH 血统的纲领移植进来。第一个旗舰产出是 2022 年 *Nature Communications* 的头颈 OAR 自动勾画（PMID 36253346，达摩院作者 Dazhou Guo / Le Lu / Dakai Jin），**三人全部来自 PAII**。
3. **2022 年**出现过一次短暂的两线合流：MP-GNN 新冠药物设计论文（PMID 35696650）的署名里 **Le Lu 与 Xian-Sheng Hua、Ying Chi 同时出现**——这是两条血脉唯一一次同框。
4. **2023 年起** Xian-Sheng Hua 的达摩院署名消失（同年他的署名转向浙江大学信息学院与新加坡国立大学），老医疗线退场；同时湖畔实验室双署名全面铺开，杭州侧的建制被重新组织。
5. **2025—2026**，吕乐去蚂蚁，Ling Zhang 的 DC 组成为学术门面。

**一句话**：达摩院医疗 AI = 杭州的本土数据挖掘线（2020 起）+ 从 NIH 经平安移植来的影像线（2021 起），后者在 2022 年之后完全主导了对外的学术面貌。

---

## 8. 论文与产品年表

主年表已在 `data/raw/damo-mode.md`，本次用 PubMed `"DAMO Academy"[Affiliation]`（80 条）复核，**年度分布为**：2019:1 / 2020:3 / 2021:4 / 2022:15 / 2023:12 / 2024:12 / 2025:13 / **2026:20**。

对原年表的两点补充与修正：

- **2022 年是拐点**。论文数从 4 跳到 15，正好对应 PAII 队伍到岗后的第一个完整产出年。
- **2021 年"Le Lu 出任负责人"那一行应改写**。原年表把 2021-08 当作达摩院医疗 AI 的起点，但 2019—2021 年达摩院已有 8 篇医疗相关论文（HealthTech Division / Healthcare Intelligence 建制）。建议改为"2021-07 后，吕乐接掌全球医疗 AI 研发；PAII Bethesda 团队整建制接入既有的杭州医疗线"。

---

## 9. 未解决

| 问题 | 状态 | 需要什么才能解决 |
|---|---|---|
| 吕乐离开达摩院的确切月份（2025-09 至 2026-03 之间）| 无公开来源 | 中文科技媒体报道 / 领英 |
| 吕乐在达摩院的确切入职月份 | 只知"2021-07 之后" | 同上 |
| 达摩院医疗 AI 美国实体是否仍在招人 | **未核实** | 阿里招聘系统 / 领英 |
| PAII Bethesda 关闭的官方说法 | **不存在公开声明**；只有署名断档（2022）与域名注销（2023-10 后）两项间接证据 | 平安财报 / 员工公开发言 |
| Xian-Sheng Hua 中文名（推定 华先胜）及离职去向 | **本次未一手核实** | — |

---

## 附：本文引用的主要 URL

- 吕乐主页 <https://lelu007.github.io/> ；2022 年快照 <https://web.archive.org/web/20220518184310/https://lelu007.github.io/>
- PAII 官网存档：首页 <https://web.archive.org/web/20190821004426/http://www.paii-labs.com/index> · 联系方式 <https://web.archive.org/web/20190821010049/http://www.paii-labs.com/contact> · 招聘 <https://web.archive.org/web/20190821010800/http://www.paii-labs.com/jobs> · 研究方向 <https://web.archive.org/web/20190821004644/http://www.paii-labs.com/ResearchAreas> · 新闻 <https://web.archive.org/web/20190821002709/http://www.paii-labs.com/news> · 新闻详情 <https://web.archive.org/web/20230608120230/http://www.paii-labs.com/news/detail?type=1>
- Ronald Summers（NIH IRP）<https://irp.nih.gov/pi/ronald-summers>
- DeepLesion <https://pubmed.ncbi.nlm.nih.gov/30035154/>
- ChestX-ray8 <https://arxiv.org/abs/1705.02315>
- Holger Roth <https://sites.google.com/site/holgerrroth/home>
- Xiaosong Wang <https://xiaosongwang.github.io/>
- Youbao Tang <https://tangyoubao.github.io/>
- 吕乐 @ 蚂蚁（Nat Commun 2026）<https://pubmed.ncbi.nlm.nih.gov/42426002/>
- 蚂蚁 Ant Healthcare (AFU)（Ann Oncol 2026）<https://pubmed.ncbi.nlm.nih.gov/42463045/>
- RADAR <https://pubmed.ncbi.nlm.nih.gov/42752131/> · DeepENE <https://pubmed.ncbi.nlm.nih.gov/41528225/> · 头颈 OAR <https://pubmed.ncbi.nlm.nih.gov/36253346/> · GRAPE <https://pubmed.ncbi.nlm.nih.gov/40555751/> · LiON <https://pubmed.ncbi.nlm.nih.gov/42618635/> · COCA <https://pubmed.ncbi.nlm.nih.gov/42025761/>
