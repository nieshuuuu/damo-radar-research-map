这四位是 RADAR 的**技术件供应商**：没有一个是通讯或共同一作，每个人往里带的是一个现成的、在 RADAR 之前就已经做完并发表过的模块 —— Sinuo Wang 与 Zhongyi Shui 带来 CT 视觉-语言预训练（fVLM 是 RADAR 方法线的直接前身），Yanjie Zhou 带来血管与胸腹急症 CT 加配准，Jianfeng Zhang 带来全身解剖结构分割的底座。四人全部**不在 PANDA 作者名单里**，属于 PANDA 之后才进这条产品线的一代；也全部不在 `damo-radar` 开源仓库的 3 位 contributor 之列。四人的中文名都没查到 —— 三位是在读学生或实习生，一位是达摩院不露面的工程师，中文互联网上没有公开痕迹。

### #10 Sinuo Wang — 吴琦门下的 Adelaide 博士生，Adelaide → 达摩院这条管道的活体样本

<img src="../photos/others/10-sinuo-wang.jpg" width="90" align="right" alt="Sinuo Wang">

- **论文单位**：Australian Institute for Machine Learning, Adelaide University（论文单位 9；全篇只给了这一条，没给达摩院）
- **现职**：Adelaide University AIML **博士生**。导师两位，V3ALab 个人页原文写明 "Under the supervision of A/Prof. Qi Wu and Dr. Yutong Xie" —— 即 [吴琦](14-qi-wu.md)（#14）与 [谢雨彤](12-yutong-xie.md)（#12），两人都在 RADAR 作者表里
- **背景**：
  - 2021 Adelaide 电气与电子工程（Autonomous Systems）荣誉学士；2023 同校人工智能与机器学习硕士；2022 获 Executive Dean's Recognition of Academic Excellence（以上四条均出自 V3ALab 官方个人页）
  - 2023：随 RoboBreizh 队在法国波尔多拿下 **RoboCup@Home SSPL 世界冠军**；同年 RoboNLU（RoboCup 2023）**第一作者**
  - 2024-04 起转医学视觉-语言：PairAug（CVPR 2024，第 3 位，与谢雨彤、夏勇、吴琦同文）
  - 2025-01 起连续三篇的署名单位**直接写 DAMO Academy**（fVLM 里单位栏只有达摩院一条，无 Adelaide）：fVLM、Boosting Vision Semantic Density（ANM）、放射报告生成的强化学习（2026-03，同篇有 Zilin Lu、曹维维、Wanxing Chang、夏勇、[张灵](39-ling-zhang.md)、[张建鹏](02-jianpeng-zhang.md)）——达摩院实习或访问身份「推断」
  - 2025-09 MedCutMix **第一作者**（合作者：谢雨彤、Yuyuan Liu 牛津、吴琦）
- **研究方向**：放射影像-报告配对数据的增广与对齐 —— 一句话，做的是「怎么把有限的影像-报告数据榨出更多监督信号」这一层，不碰成像端
- **在 RADAR 里**：「推断」视觉-语言预训练与图文数据增广的算法贡献，同时是 AIML 一侧的学生代表。位次 10 紧挨着 12 谢雨彤、13 夏勇、14 吴琦，落在「西工大—Adelaide」这个学术块里，而不是临床块。是 fVLM（第 4 位）与 ANM（第 4 位）两篇 RADAR 技术前身的合著者。不在 PANDA、GRAPE、iAorta 里
- **与其他作者的关系**：导师是 [吴琦](14-qi-wu.md) 与 [谢雨彤](12-yutong-xie.md)；顺着谢雨彤 → [夏勇](13-yong-xia.md) 这条线接上达摩院的 [张建鹏](02-jianpeng-zhang.md)。本人就是 [学术管道](../sources/academic-pipeline.md) 那条「西工大出人 → Adelaide 读博 → 回流达摩院实习」链子的当期样本
- **对 Shu**：本人是同辈博士生，不是推荐人也不是合作对象，技术上与材料分解、光子计数 CT 完全不相交。==有用的是这条线背后的机构==：Adelaide AIML 的医学影像 AI 建制完整（吴琦做视觉语言、Johan Verjans 做心脏影像、Minh-Son To 是放射科医生），澳洲对国际学生的签证与工作权限明显比美国宽，这对 2026 年 9 月毕业后的去向是一个实质备选；同一条线上的谢雨彤去了 MBZUAI，也是同类选项。要花时间就花在这两位导师的页面上
- **查不到**：中文名。另有两处同名需要隔开 —— arXiv 上 2025-09 起有一批金融 / Agent 方向的 Sinuo Wang（Flash-Searcher、GAUGE、FinResearchBench II 等），合作网络与本人毫无重合；OpenAlex 还把一篇 2022 年郑州大学网络空间安全学院的评论检测论文并进了同一个 cluster，与官方履历（2021 年在 Adelaide 读本科）对不上。两者都按不同人处理
- **来源**：<https://v3alab.github.io/author/sinuo-wang/>、<https://v3alab.github.io/people/>、<https://arxiv.org/abs/2509.16673>、<https://arxiv.org/abs/2501.14548>、<https://arxiv.org/abs/2508.03742>、<https://arxiv.org/abs/2603.04022>、<https://arxiv.org/abs/2404.04960>
  照片：<https://v3alab.github.io/author/sinuo-wang/>

### #15 Zhongyi Shui — fVLM 第一作者，RADAR 视觉-语言方法线的源头

- **论文单位**：浙江大学计算机科学与技术学院（论文单位 6；全篇只给了这一条）
- **现职**：浙大-西湖大学联合培养博士生「推断」，杨林（Lin Yang）实验室。2026-08 已出现在蚂蚁集团 UI-Venus-2 技术报告 31 人名单里（第 19 位，"Venus Team, Ant Group"），方向转到 GUI Agent
- **背景**：
  - 约 2021 入学「推断」（首篇论文 2022-07 倒推）。2022–2025 全部论文双署「浙大计算机学院 + 西湖大学工学院」，到 RADAR 只剩浙大一条
  - 计算病理主力，一作至少 6 篇：End-to-End Cell Recognition by Point Annotation（MICCAI 2022）、DPA-P2PNet、Semi-supervised Cell Recognition、Prompt-driven Nucleus Instance Segmentation、Context-aware Nucleus Detection（AAAI 2026）、NuNext（2026-03）。西湖大学官方教师页把其中几篇直接列进杨林的代表论文
  - 2024 起在达摩院实习 —— fVLM 首页脚注原文：**"The work was done during Zhongyi's internship at DAMO Academy"**，同一行写着 "Correspondence to Jianpeng Zhang"
  - 2025-01 **fVLM**（arXiv 2501.14548），**ICLR 2025 Spotlight**（OpenReview 的 venue 字段即 "ICLR 2025 Spotlight"），第一作者
  - 2026-03 NuNext 一作，合作者已换成何聪辉（上海 AI 实验室）等，说明上半年就在迁移；2026-08 进蚂蚁
- **研究方向**：点监督的细胞与细胞核检测、全切片图像多示例学习、病理视觉-语言基座；2025 横向搬到 CT 视觉-语言预训练；2026 转 GUI Agent，已离开医学影像
- **在 RADAR 里**：==方法线的源头之一，不是挂名的浙大学生==。fVLM 做的正是「把 CT 按解剖区域切开、逐个解剖做对比预训练，再把解剖级对齐带来的大量假阴性校正回来」：6.9 万例病人的图文数据、15 个主要解剖、54 个诊断任务零样本平均 AUC 81.3%。RADAR 的 1500 万解剖感知图文对是同一条路线的放大版，且 fVLM 的作者串（[张建鹏](02-jianpeng-zhang.md)、曹维维、Sinuo Wang、吕乐、杨林、[叶香华](22-xianghua-ye.md)、[梁廷波](40-tingbo-liang.md)、[章琦](01-qi-zhang.md)、[张灵](39-ling-zhang.md)）几乎就是 RADAR 班底。另合著 ANM（arXiv 2508.03742，第 3 位）。位次 15 是浙大计算机块之首。不在 PANDA、GRAPE、iAorta 里
- **与其他作者的关系**：导师杨林 —— 西湖大学工学院人工智能系终身教授、人工智能与生物医学影像实验室负责人，履历按西湖大学官方教师页是 1999 西安交大本科 → 2002 西安交大硕士 → 2006/2009 罗格斯大学硕士 / 博士 → 罗格斯（2009–2011）、肯塔基（2011–2014）、佛罗里达（2014 起，2015 拿终身副教授）→ 2020 加入西湖。杨林本人也署在 fVLM 上。达摩院一侧对口的是通讯作者张建鹏、张灵、吕乐；与曹维维（#3）在 fVLM 与 ANM 两篇上互为共同作者
- **对 Shu**：==值得精读一篇论文，不值得联系一个人。== fVLM 是「不做任何像素级标注、也不做任何物理建模，直接从几十万份临床报告里学解剖级对齐」的极端样本，正好站在 Shu 整个纲领（材料分解、误差预算、噪声即信号）的反面。面试或研究陈述里「RADAR 都到专家级了，为什么还需要 CT 成像物理」是必答题，答案就在这篇的边界上：报告里从来不写的量 —— 脂肪衰减、水脂分数、噪声结构 —— 它学不到。另外此人的履历（博士 5 年、6 篇以上一作顶会、直接进大厂）是校准工业界门槛的一个干净样本
- **学术指标**：Semantic Scholar 35 篇 / 612 次被引 / h-index 13（2026-09-20 抓取；该名在全库只有一个候选，消歧干净）。ORCID 0009-0009-8052-7972，但整份记录只登记了 Science 这一篇。OpenAlex 把此人拆成 10 个碎片 cluster，不可用
- **查不到**：中文名（Shui 是罕见姓，但没有任何来源把拼音与汉字拼起来）；本科与硕士院校；入学与毕业年份
- **来源**：<https://arxiv.org/abs/2501.14548>、<https://openreview.net/forum?id=nYpPAT4L3D>、<https://www.westlake.edu.cn/faculty/lin-yang.html>、<https://arxiv.org/abs/2508.03742>、<https://arxiv.org/abs/2603.07098>、<https://arxiv.org/abs/2609.00028>、<https://api.semanticscholar.org/graph/v1/author/search?query=Zhongyi%20Shui>

### #18 Yanjie Zhou（论文写作 Yan-Jie Zhou）— 从中科院自动化所整组迁进达摩院的血管急症 CT 主力

- **论文单位**：阿里巴巴达摩院（杭州）+ [湖畔实验室](../sources/hupan-lab.md) + 浙江大学计算机科学与技术学院（论文单位 4、5、6，三重挂靠）
- **现职**：达摩院医疗 AI 算法研究员「推断」（署名顺序是达摩院在前、湖畔在后，但没有岗位级别的公开证据）；浙大计算机学院那一挂的确切身份未查实
- **背景**：
  - 2019–2023：中国科学院自动化研究所「复杂系统管理与控制国家重点实验室」+ 国科大人工智能学院。手术机器人视觉方向：RASNet（EMBC 2019，第 6 位）、RAUNet（ICONIP 2019，第 7 位）、多导丝端点定位（IEEE TBME 2022，第 6 位）、TR-GAN（IEEE TMI 2022，第 9 位）。这一段全是中后位合著，无一作
  - 2023-07 首次以达摩院 + 湖畔署名：MICCAI 2023 early accept 的皮肤病多任务鉴别诊断，**第一作者**
  - 2024 起加挂浙大计算机学院
  - 这不是个人跳槽而是整组迁移：共同作者 Chen-Chen Fan 同时出现在自动化所一侧（arXiv 2105.06270，与侯增广同文）与达摩院一侧（arXiv 2410.18610，与徐敏丰、吕乐同文），本人在这两篇里都在
- **研究方向**：早期是手术器械分割、导丝端点定位、操作技能建模；转达摩院后是平扫与增强 CT 的血管和胸腹急症 —— 急性主动脉综合征、肺栓塞、胸部 CT 心血管风险预测，同时参与多模态配准（CVPR 2024 模态无关结构表征第 6 位、UniReg 第 5 位）与零样本多模态检索（M3Ret 第 5 位）
- **在 RADAR 里**：「推断」血管与胸腹急症病种的经验输入，加多器官分割-配准的工程支持。位次 18 紧挨 19 [Tony C W Mok](19-tony-c-w-mok.md) 与 20 [夏英达](20-yingda-xia.md)，是达摩院算法班底的连号段。不在 PANDA；但在 **iAorta**（*Nat Med* 2025，第 3 / 46 位，与 [肖文波](38-wenbo-xiao.md)、[张建鹏](02-jianpeng-zhang.md)、Tony C W Mok 同框）与 MICCAI 2024 肺栓塞（与 Bizhe Bai **并列共同第一作者**，两人都带星号）里；2026 年还有一篇关于急性主动脉综合征的评论文章。不在 GRAPE 里
- **与其他作者的关系**：自动化所时期全部论文的资深位固定是侯增广、谢晓亮、周小虎、卞桂彬（团队归属可确认，一对一的导师关系查不到）；达摩院一侧对口的是徐敏丰与吕乐，浙大一侧的接口是黄正行（iAorta 的浙大侧通讯作者）。与 [Tony C W Mok](19-tony-c-w-mok.md) 在 CVPR 2024、UniReg、iAorta、肺栓塞四篇上反复同框
- **对 Shu**：同辈对标，不是引路人。==做的事情是「同一批胸腹 CT 扫描、另一种读出方式」==：在平扫 CT 上筛主动脉夹层与肺栓塞，数据来源也是浙一。想看「工业界怎么把一批临床 CT 变成产品」，这条履历是最贴的样本；同时它提醒一件事 —— 达摩院要的是分割 / 配准 / 视觉语言的工程能力，成像物理背景在这条路上是差异化优势，但不是入场券。技术上与材料分解、水脂分解、光子计数 CT 不相交
- **学术指标**：没有可用的单人指标（2026-09-20 抓取）。OpenAlex 的同名 cluster 混进了江南大学、徐州医学院、江阴市人民医院等无关同名者，Semantic Scholar 的候选实为武汉一个神经科团队，都不可用。按逐篇核对，本人约 12–15 篇，含 Science 1 篇、*Nature Medicine* 1 篇、IEEE TMI / TBME / TNNLS 各 1 篇、MICCAI 2 篇（1 篇一作、1 篇共同一作）、CVPR 1 篇。无 ORCID
- **查不到**：中文名（拼音 Yanjie 可对应多种写法，没有来源就不猜）；是否在自动化所拿到学位；浙大那一挂到底是联培博士还是博士后
- **来源**：<https://arxiv.org/abs/2307.08308>、<https://arxiv.org/abs/2407.11529>、<https://arxiv.org/abs/2402.18933>、<https://arxiv.org/abs/2503.12868>、<https://pubmed.ncbi.nlm.nih.gov/40835970/>、<https://pubmed.ncbi.nlm.nih.gov/35148262/>

### #37 Jianfeng Zhang — 达摩院的解剖分割底座工程师；与达摩院院长张建锋同音，不是同一人

- **论文单位**：阿里巴巴达摩院（杭州）+ [湖畔实验室](../sources/hupan-lab.md)（论文单位 4、5）
- **现职**：达摩院（杭州）医学影像研究员「推断」。==注意同音不同人：阿里巴巴达摩院院长、湖畔实验室主任张建锋与此人拼音相同，履历完全不相干。==「达摩院 + 湖畔实验室」这两条单位是达摩院杭州组的标准署名，RADAR 里的 Wanxing Chang（#5）、Zhilin Zheng（#17）、[Tony C W Mok](19-tony-c-w-mok.md)（#19）署的一模一样，它不指向任何职务
- **背景**（公开痕迹只有论文轨迹，八年里**没有一篇第一作者**，固定是 Heng Guo 的第二作者或团队中后位 —— 典型的底座工程师位置）：
  - 2022-08 最早一篇：腹部多器官分割的概率 V-Net（arXiv 2208.01382，第 3 / 5 位，与徐敏丰、Heng Guo、Ke Yan、吕乐）
  - 2022-12 **Med-Query**：用 query embedding 做 9 自由度解剖实例解析，第 2 / 5 位（IEEE JBHI，2024 年录用，2025 年 29(1):383–395）
  - 2023-07 Parse and Recall 肺结节良恶性预测（MICCAI 2023，第 3 / 11 位；一作是 [张建鹏](02-jianpeng-zhang.md)，同篇还有 [叶香华](22-xianghua-ye.md)、[张灵](39-ling-zhang.md)）
  - 2024-03 **CT-SAM3D**（arXiv 2403.15063）：1204 例 CT、107 个全身解剖结构训练的可提示 3D 分割模型，第 2 / 9 位，AAAI 2025
  - 2025-03 持续学习驱动的全身精细解剖分割（arXiv 2503.12698，第 12 / 34 位，同篇有 Alan Yuille 与 Ronald Summers）
  - 2025 CT 皮下脂肪体积与椎管扩大成形术后颈椎后凸的 AI 分析（*Computer Assisted Surgery*，第 5 / 9 位，排在自己部门负责人徐敏丰之前）
  - 2025-06 GRAPE 胃癌平扫 CT 筛查（*Nat Med*，第 52 / 58 位）；2026-09 RADAR 第 37 / 40 位
- **研究方向**：3D CT 的全身解剖结构分割与实例解析。CT-SAM3D 不是把 SAM 硬改到医学图像上，而是在 3D 上重做可提示分割：渐进且空间对齐的点提示编码 + 跨 patch 提示，解决 3D patch 训练下提示响应不准、大器官要点太多次的问题。Med-Query 走的是先估 9 自由度姿态、再检测-分割的路线
- **在 RADAR 里**：「推断」解剖分割底座。RADAR 覆盖 18 个腹部器官、146 种以上病症，解剖分割与实例解析是前置步骤，而这正好是此人全部产出的内容。同一套技能也解释了出场规律 —— 出现在 GRAPE（胃癌，需要胃与周边器官分割）与 RADAR，却**不出现在 iAorta**（主动脉，*Nat Med* 2025，46 位作者里没有此人）。不在 PANDA 里
- **与其他作者的关系**：长期固定搭档是 Heng Guo（五篇共同署名里多数是 Heng Guo 一作、此人二作）、Ke Yan、徐敏丰、吕乐、Dakai Jin；与 [Tony C W Mok](19-tony-c-w-mok.md) 在 CT-SAM3D 同文，与 [张建鹏](02-jianpeng-zhang.md)、[叶香华](22-xianghua-ye.md)、[张灵](39-ling-zhang.md) 在 MICCAI 2023 同文。==此人是 [RADAR ↔ MedSAM 两跳人事链](../sources/radar-vs-medsam.md) 的终点==：Jun Ma / Bo Wang 在 FLARE22 挑战赛报告里与 Heng Guo 同一张作者表 → Heng Guo 与此人在 Med-Query 共同署名 → RADAR
- **对 Shu**：两点具体的。一是 **CT-SAM3D 是能直接拿来用的东西** —— Apache-2.0，权重与那套增强版 TotalSeg++ 数据集（107 个结构）都挂在 ModelScope 上，还带一个准实时的交互式分割工具；PCAT / 冠脉周围脂肪这类必须先把器官与脂肪腔分出来的工作，可以省掉自己训一个分割网络这一步。二是那篇颈椎后凸论文做的就是 **CT 皮下脂肪体积测量**，与 Shu 的脂肪定量是同一类读出，值得看一眼工业界这边怎么把体积当终点指标用（以及为什么这样一篇只落在一本影响力很低的外科期刊上）
- **学术指标**：无可用指标（2026-09-20 抓取）。OpenAlex 的 Jianfeng Zhang 聚类跨几十个机构、几百篇论文，污染到完全不能用。可核的口径只有两个：PubMed 里「Zhang Jianfeng[Author] AND (Alibaba OR Hupan)[Affiliation]」共 3 条（RADAR、GRAPE、*Computer Assisted Surgery*）；arXiv 上与 Heng Guo / Ke Yan / 徐敏丰 / 吕乐 / Dakai Jin 任一人共同署名的共 5 篇。无 ORCID
- **查不到**：中文名（Jianfeng 可对应建锋 / 建峰 / 剑锋 / 健峰 等多种写法，没有来源就不猜）；教育背景、入职时间、职级 —— 没有任何个人主页、机构名录或中文报道
- **来源**：<https://arxiv.org/abs/2403.15063>、<https://github.com/alibaba-damo-academy/ct-sam3d>、<https://arxiv.org/abs/2212.02014>、<https://pubmed.ncbi.nlm.nih.gov/39283775/>、<https://arxiv.org/abs/2208.01382>、<https://arxiv.org/abs/2307.10824>、<https://arxiv.org/abs/2503.12698>、<https://pubmed.ncbi.nlm.nih.gov/41389372/>、<https://pubmed.ncbi.nlm.nih.gov/40555751/>
