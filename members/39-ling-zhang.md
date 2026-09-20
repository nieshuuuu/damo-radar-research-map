# 张灵 Ling Zhang — 达摩院「平扫 CT 查癌」这条线在美国侧的技术负责人

<img src="../photos/39-ling-zhang.jpg" width="160" align="right" alt="张灵">

> RADAR 第 39 / 40 位作者 · Alibaba DAMO Academy, Washington, DC（论文单位 11）· AI 侧资深作者（倒数第二位，末位是[梁廷波](40-tingbo-liang.md)）

## 一句话画像

达摩院资深算法专家、**多癌筛查技术负责人**，达摩院医疗 AI 实验室美国侧唯一的资深署名者。一条主线贯穿十年：**用弱标注 / 无标注的大规模真实世界 CT 做癌症筛查**，押注「平扫 CT 就够」——不打造影剂、不做人工勾画，从体检存量平扫 CT 里找早期实体瘤。PANDA（胰腺）、GRAPE（胃）都出自这条线，RADAR 是它从专病走向通用模型的下一步。==最值得记住的一点：吕乐 2025-06 离开达摩院后，RADAR 成了达摩院医疗 AI 第一篇没有吕乐的旗舰论文，张灵是留下来的那条线。==

## 在 RADAR 里的位置

- **位次 39 / 40**，倒数第二。论文标注单位为 `Alibaba DAMO Academy, Washington, DC, USA`——RADAR 全部 40 位作者里只有两人署这个地址，另一位是第 20 位[夏英达](20-yingda-xia.md)。达摩院杭州侧的作者都在前面，且多数兼挂[湖畔实验室](../sources/hupan-lab.md)，张灵没有挂。
- **身份绑定是机读级的**：AAAS 投递给 Crossref（DOI 10.1126/science.aec6129）与 Europe PMC（PMID 42752131）的元数据，都把 ORCID `0000-0001-8371-5252` 挂在第 39 位 Ling Zhang 名下，单位同为 Washington, DC。"Ling Zhang" 是极高频的重名，但这一条把人钉死了。
- **角色（推断）**：方向设定与路线把关、多中心数据合作的资源协调、投稿与审稿应对；建模与实验由杭州侧的共同一作团队执行。依据是位次、单位、以及在 PANDA / GRAPE 上的同构位置。⚠️ RADAR 全部 40 位作者在公开元数据里**无一人带通讯邮箱**，Crossref 对该 DOI 也没有 corresponding 标记，所以"AI 侧通讯作者"只是推断，不是已证实的事实。
- **中文媒体的分工很清楚**：技术细节（CT 信号稀疏、器官级细粒度对齐）由[张建鹏](02-jianpeng-zhang.md)讲；张灵讲的是路线判断——"专病模型和通用模型并不是替代的关系，而是会将长期并行存在"（雷峰网 / 网易 2026-09-18）。不过同一篇深度报道里"张建鹏"出现 9 次且是全文主角，"张灵"只出现 1 次、在结尾的行业展望段。**不要把路线发言读成项目主导。**
- **与 PANDA 的重合**：PANDA（*Nature Medicine* 2023，36 位作者）里张灵是第 35 位，**是六位带通讯邮箱的作者之一**（另五位是上海长海医院邵成伟、中国医科大学盛京医院施昱、浙一[章琦](01-qi-zhang.md)、浙一[梁廷波](40-tingbo-liang.md)、上海长海医院放射科陆建平；末位作者是陆建平）。中文报道称张灵是 PANDA 项目负责人。PANDA 时期署名地点是 New York，RADAR 改署 Washington DC。
- 其他达摩院 × 浙大一院联名论文里也基本在末位或次末位：GRAPE（胃，*Nat Med* 2025）、ICLR 2025 CT 图文预训练（RADAR 的直接前身）、ICCV 2025 解剖正常性建模、IJCV 2025 胰腺癌淋巴结转移、CVPR 2024 三篇、MICCAI 2024 三篇、*Radiology: AI* 2025。

## 背景与履历

| 时间 | 单位 · 职位 | 备注 |
|---|---|---|
| 2008-09 – 2013-03 | 浙江大学 博士 | 2012 年一作论文署"浙江大学生物医学工程系"（杭州 310027，玉泉校区）；个人主页写 2013 年获浙大博士。实际研究在**深圳大学医学超声关键技术国家地方联合工程实验室**——2014 年一作论文署名已整体换成深大。方向：产科超声标准切面自动识别、宫颈细胞学自动筛查 |
| 2013-07 – 2016-06 | University of Iowa，博士后 | Milan Sonka / Andreas Wahle 组。IVUS + virtual histology 冠脉易损斑块预测、3D 图优化配准；与布拉格查理大学心内科 Tomas Kovarnik 长期合作 |
| 2016-06 – 2018-06 | National Institutes of Health，Visiting Fellow | NIH Clinical Center 放射与影像科学部，Ronald M. Summers / Jianhua Yao 组；**吕乐（Le Lu）同期在此任 staff scientist**。产出 DeepPap 宫颈细胞分类、肿瘤生长预测、肺囊肿自学习分割 |
| 2018-07 – 2019-05 | NVIDIA，Research Scientist（Bethesda） | Daguang Xu / Ziyue Xu / Holger Roth / Dong Yang / Andriy Myronenko 组，即后来的 Clara / MONAI 班底。**这一年是张灵自己的一段**——吕乐 2018-06 已先行离开 NVIDIA 去 PAII，两人在 NVIDIA 无交集，BigAug 的 12 位作者里也没有吕乐 |
| 2019-05 – 2021-08 | PAII Inc.（平安科技美国研究院 Bethesda Research Lab） | 吕乐管理该部门（2018-06 至 2021-07）。方向：胰腺癌 CT 分割 / 预后 / 淋巴结转移，与上海长海医院、盛京医院合作 |
| 2021-08 – 至今 | 阿里巴巴达摩院（先署 New York，后署 Washington DC） | 资深算法专家（Senior Staff Algorithm Engineer / Senior Technical Expert）、**多癌筛查技术负责人**。2023 年中文报道用的头衔是"高级算法专家"，2025 年起改为"资深算法专家" |

不是教授，不带学位学生，无 adjunct professor 头衔。学术兼职：MICCAI Area Chair；IEEE TMI / *Medical Image Analysis* / TBME / JBHI / *Pattern Recognition* / *Nature Communications* / *npj Digital Medicine* 审稿人。

## 研究方向

- **平扫 CT + AI 做癌症早筛**（核心押注）。不打造影剂、不做人工勾画，靠体检人群的存量平扫 CT 发现早期实体瘤。这是整条技术路线的立身之本。
- **多癌筛查**（现在的正式职责）：胰腺 PANDA → 胃 GRAPE → 食管、结直肠，目标是一次平扫 CT 同时筛多种癌。
- **报告监督的视觉-语言预训练**：绕开人工标注，直接从临床报告学。ICLR 2025 的 CT 大规模细粒度图文预训练、CVPR 2024 从 X 光专家模型蒸馏胸部 CT 理解，都是通往 RADAR 的台阶。
- **域泛化与标注效率**：BigAug（IEEE TMI 2020）是"靠深度堆叠数据增强做跨扫描仪 / 跨域泛化"的经典引文；另有极值点弱监督分割、部分标注的多中心训练。
- **早期方向（现在基本不做）**：产科超声、宫颈细胞病理图像、IVUS 冠脉易损斑块。

## 代表作

| 论文 | 期刊 · 年份 | 作者位次 |
|---|---|---|
| An expert-level generalist AI for abdominal CT diagnosis（RADAR） | *Science* 393(6817):eaec6129, 2026 | 39 / 40 |
| Generalizing deep learning for medical image segmentation to unseen domains via deep stacked transformation（BigAug） | IEEE TMI 39(7):2531-2540, 2020 | **第一作者**（引用 898，个人最高） |
| DeepPap: deep convolutional networks for cervical cell classification | IEEE JBHI 21(6):1633-1643, 2017 | **第一作者**（引用 617，NIH 时期） |
| Large-scale pancreatic cancer detection via non-contrast CT and deep learning（PANDA） | *Nature Medicine* 29(12):3033-3043, 2023 | 35 / 36，带通讯邮箱（引用 484） |
| AI-based large-scale screening of gastric cancer from noncontrast CT imaging（GRAPE） | *Nature Medicine*, 2025 | 倒数第二位 |
| Predicting locations of high-risk plaques in coronary arteries in patients receiving statin therapy | IEEE TMI, 2018 | **第一作者**（Iowa / Sonka 组，IVUS 冠脉斑块） |
| Convolutional invasion and expansion networks for tumor growth prediction | IEEE TMI, 2018 | **第一作者**（NIH 时期） |
| Large-scale and fine-grained vision-language pre-training for enhanced CT image understanding | ICLR 2025 | 末位（RADAR 的直接前身） |
| Artificial intelligence to predict lymph node metastasis at CT in pancreatic ductal adenocarcinoma | *Radiology* 306(1):160-169, 2023 | 8 / 13（引用 147） |

MICCAI 2020 的 anatomy-aware transformer 多型胰腺癌平扫筛查（张灵末位）入选 MICCAI-MedIA Best Papers 2020 特刊。

## 师承与关系

**博士段 —— 深圳医学超声学派（==推断==）。** 学籍在浙大，2012–2014 年的一作论文全部署深圳大学医学超声国家地方联合工程实验室，合作者固定是陈思平（Siping Chen）、汪天富（Tianfu Wang）、Chien Ting Chin、李胜利（深圳市妇幼保健院超声科）。深圳大学官网写明陈思平"其他专业兼职包括：浙江大学博士生导师"，且 1987–1989 年在浙大科仪系做博士后（中国第一位生物医学工程博士后，主持研制中国第一台彩超）。==**推断**：挂浙大学籍、由兼任浙大博导的陈思平在深大实际指导。未直接证实，汪天富作为实际指导人的可能性也排除不掉。==

**博后段 —— Milan Sonka 的 Iowa 图优化学派。** 2013–2016 年合作者固定为 Sonka、Andreas Wahle、Zhi Chen，方向是 IVUS 冠脉易损斑块（TMI 2015/2018、MICCAI 2015、ISBI 2016）。Sonka 是 LOGISMOS / 图割最优表面分割学派的宗师。学派迁移的指纹很清楚：张灵把图优化带进了细胞分割（CMIG 2017，与 Sonka 共同署名）。

**最关键的一段 —— 跟着吕乐（Le Lu）走。** 2016–2018 在 NIH Clinical Center 与吕乐共事；2019-05 跟到 PAII（比吕乐晚约 11 个月）；2021-08 与吕乐同时进达摩院，吕乐领导达摩院全球医疗 AI。中间的 NVIDIA 一年是张灵自己的选择，与吕乐无关。吕乐主页把"Jiawen Yao, Ling Zhang, et al."列为 MICCAI-MedIA Best Papers 2020 的自家成果，可见当时已是麾下资深骨干。谱系全貌见[达摩院谱系](../sources/damo-lineage.md)。

**现在的谱系断口。** 吕乐 2025-06 离开达摩院去蚂蚁 Medical AI Lab（论文署名到 2025-09 仍是达摩院，2026-03 起改蚂蚁），RADAR 的作者名单里已经没有吕乐。张灵留在美国侧，成为达摩院医疗 AI 在论文署名上唯一的资深锚点；同时杭州侧冒出[张建鹏](02-jianpeng-zhang.md)（2022 年入职，RADAR 共同一作、技术发言人）这一代新人。可以理解为达摩院医疗 AI 正从"吕乐的 NIH / PAII 老班底"过渡到"浙大计算机 + 杭州本地培养"的新一代。==但不要说张灵接任了团队负责人——2026-09 的报道里头衔仍是"多癌筛查技术负责人"，不是团队负责人。==

**与本文其他作者**：[夏英达](20-yingda-xia.md)（同署 Washington DC，PANDA 与 RADAR 都在）、[章琦](01-qi-zhang.md) 与 [梁廷波](40-tingbo-liang.md)（PANDA 与 RADAR 的浙一侧核心，同为 PANDA 六位通讯之一）、[张建鹏](02-jianpeng-zhang.md)、[曹维维](03-weiwei-cao.md)（杭州侧执行层）。

## 学术指标

| 指标 | 数值（2026-09-20 抓取） |
|---|---|
| Google Scholar 总引用 | 5,778（2021 年至今 4,603） |
| h-index | 35（2021 年至今 34） |
| i10-index | 63（2021 年至今 58） |
| ORCID | 0000-0001-8371-5252 |

Google Scholar profile `-toYdm8AAAAJ`，单位行 "Alibaba DAMO Academy USA"，验证邮箱域 alibaba-inc.com。

==**同名污染提醒**：「Ling Zhang」是高频重名，本页的所有数字只取上面这一个 profile。OpenAlex 的同名作者实体（414 篇 / 11,484 引 / h=42）是多人合并的脏数据——同一实体下混进了青海大学、南京农业大学、浙江中医药大学、Montefiore 医学中心等完全无关的单位，==不可用于指标。做发表清单时，ORCID works 接口（32 个 work group，覆盖 2012 年妊娠囊超声到 2026 年 RADAR）比 Google Scholar 干净。

## 对 Shu 意味着什么

- **签证赛道上的一个具体名字。** 达摩院美国实体（Washington DC / New York）是真实存在的雇主，张灵是其中医疗影像方向的负责人级人物。对"工业界 + 需要 sponsorship"那条线，这是可以点名的去处。⚠️ 但它不公开招聘：LCA 披露里 Washington DC 的研究岗 2026 年只有一条（Senior Algorithm Engineer，2026-04 申报），"Research Scientist"头衔 2022 年后归零；吕乐已去蚂蚁。只能定向联系，且岗位语言是 LLM / VLM 而非成像物理。另见[达摩院招聘线索](../sources/damo-hiring.md)。
- **交叉点恰好是 Shu 的独门。** 这条路线的立身之本是一个物理命题——"为什么平扫 CT 里看得见胰腺癌 / 胃癌"。达摩院的回答是"模型学到了"，说不清是什么对比度在支撑；而 RADAR 达摩院侧的署名单位里没有任何成像物理背景的机构。water/lipid（乃至 water/lipid/protein）材料分解正好能把它量化成物理量而不是深度特征。这是真实的差异化切口，可以直接写进 cold email 第一段。
- **破冰点是真的，不是硬凑。** 2013–2016 年在 Iowa 做的是 IVUS + virtual histology 冠脉易损斑块预测；Shu 做 PCAT / 冠脉周围脂肪 FAI，是同一个临床问题的另一侧（管腔内 vs 管壁外）。
- **BigAug 是该引的引文，也是该批评的对象。** 做仿真到真机的迁移（NAEOTOM 无标定迁移、Canon / Oxford 数据转移）时 BigAug 是标准引文；同时可以提出自己的物理论断——数据增强是在图像域模拟域偏移，而 CT 域偏移的根源在能谱与探测器响应，物理前向模型比随机增强更可控。==这是 Shu 自己的观点，不是文献共识，写的时候要以己见提出。==
- **不建议的用法**：不要把这里当博后 / PhD 去向。达摩院不授学位、不带学生，张灵也没有任何学术教职头衔。定位是"工业界联系人 + 引用对象 + 差异化对照组"，不是导师。

## 未解决

- **博导未证实。** 陈思平只是推断，汪天富不能排除。未检索到博士学位论文，题目、答辩年份、导师姓名三项均缺。
- **本科、硕士院校无任何可靠来源。** ORCID 教育栏只有浙江大学 2008-09 → 2013-03 一条，且该条目没有院系与学位字段（"生物医学工程"来自 2012 年论文署名，"博士 / 2013"来自个人主页）。
- **RADAR 是否为通讯作者无法判定。** Crossref 对该 DOI 无 corresponding 标记，Europe PMC 的 authorNotes 为 null，40 位作者无一人带邮箱，开源仓库 README 也只有 citation 块。本页按推断处理。
- **GRAPE 的通讯作者身份只有一份通稿支撑**（新浪财经与 IT之家 2025-06-25 的报道逐字相同，是同一份达摩院通稿的两次转载，不构成独立互证），未能从 PubMed 侧核通讯邮箱。
- **中英文名从未在同一处并排出现。** 绑定靠履历指纹（浙大博士 → 爱荷华 → NIH → 达摩院平扫 CT 筛癌）+ 职务指纹（"资深算法专家 / 多癌筛查技术负责人" ↔ "Senior Technical Expert and Lead of Multi-Cancer Screening Technology"）+ 项目指纹三重吻合，不是一处字面对照。三者同时撞车的概率可忽略，但严格讲仍是推断。
- **"临床医学背景"不采信。** 雷峰网 2023 年报道有这四个字，但 ORCID、个人主页、2012 年论文署名全部指向生物医学工程，无硬证据。
- **阿里内部职级未核实**：英文两种写法（Senior Staff Algorithm Engineer / Senior Technical Expert）应是同一职级的不同译法。
- **个人主页已过时**：Updates 最后一条停在 2025-06 的 GRAPE，没有 RADAR / *Science* 条目。可作履历来源，不可作"现在在做什么"的证据。

## 来源

- https://fabiozhang0722.github.io/ （个人主页：Brief Bio、发表列表、Updates；全英文，页面上无任何中文）
- https://orcid.org/0000-0001-8371-5252 （ORCID：教育与任职年月的一手来源；`/works` 接口为最干净的发表清单）
- https://scholar.google.com/citations?user=-toYdm8AAAAJ&hl=en （Google Scholar，验证邮箱域 alibaba-inc.com）
- https://aiforgood.itu.int/speaker/ling-zhang/ （ITU AI for Good 官方讲者页：职务英文表述）
- https://api.crossref.org/works/10.1126/science.aec6129 （Crossref：RADAR 第 39 位 Ling Zhang + ORCID + Washington DC）
- https://pubmed.ncbi.nlm.nih.gov/42752131/ （RADAR，*Science* 2026，PMID 42752131）
- https://pubmed.ncbi.nlm.nih.gov/37985692/ （PANDA，含六位通讯作者的完整署名结构）
- https://github.com/alibaba-damo-academy/damo-radar （RADAR 开源代码，2026-07-03 建仓，Apache-2.0，357 stars @ 2026-09-20；README 的 citation 块给出完整 40 人作者序）
- https://m.thepaper.cn/newsDetail_forward_25484264 （澎湃 2023-11-21：PANDA 项目负责人张灵）
- https://m.leiphone.com/category/healthai/47g0E0X1dLSmTkJP.html （雷峰网 2023-11-22：爱荷华 / NIH 履历）
- https://www.163.com/dy/article/L74O5TP20511DPVD.html （雷峰网 / 网易 2026-09-18：RADAR 深度报道，"多癌筛查技术负责人张灵"）
- https://finance.sina.com.cn/tech/digi/2025-06-25/doc-infchutm4484267.shtml 与 https://www.ithome.com/0/863/646.htm （GRAPE 通稿的两次转载，计为一个来源）
- https://www.cs.jhu.edu/~lelu/ （吕乐主页：PAII 任职起止、2025-06 去蚂蚁）
- https://bme.szu.edu.cn/info/1154/1307.htm （深圳大学陈思平主页：兼任浙江大学博士生导师）
- https://pubmed.ncbi.nlm.nih.gov/22894427/ （2012 *Med Phys*，一作署浙江大学生物医学工程系）
- https://pubmed.ncbi.nlm.nih.gov/24376056/ （2014 *Cytometry A*，一作署深圳大学医学超声国家地方联合工程实验室）
- 照片：https://fabiozhang0722.github.io/
