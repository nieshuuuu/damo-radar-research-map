这四位都不是 RADAR 的决策者，而是真正把模型训出来、把结果评出来的那层人力。两条互不相干的来路在这里合流：#4 与 #11 来自[夏勇](13-yong-xia.md)在西北工业大学计算机学院的课题组，由已在达摩院的师兄[张建鹏](02-jianpeng-zhang.md)带进来实习；#5 是 2024 年从上海科技大学硕士毕业直接入职的算法工程师，也是 RADAR 代码仅有的三位作者之一；#17 则是 2021 年前后跟着吕乐那批人从平安整体迁进达摩院的老兵。==四人里只有 #4 和 #5 是共同第一作者，#11 与 #17 不是。== 署名上还有一处要留意：#4 与 #11 在 *Science* 上的单位串是「达摩院 + 宁波市第二医院放射科」，**一个字的西北工业大学都没有** —— 连导师夏勇本人也是同样的写法。

### #4 Zilin Lu — 西工大夏勇门下在读博士，达摩院实习期间挂上 Science 共同一作

- **论文单位**：Alibaba DAMO Academy（杭州）+ Department of Radiology, Ningbo No. 2 Hospital（宁波市第二医院放射科）。==真实学术归属是西北工业大学计算机学院，论文上一字未提。== ORCID 0000-0003-2437-283X 的教育栏只有一条 Northwestern Polytechnical University；用该 ORCID 反查 Crossref 的 7 篇里，除 RADAR 外六篇的单位字段全印西工大全称。
- **现职**：西北工业大学计算机学院在读博士研究生，导师[夏勇](13-yong-xia.md)；在达摩院医疗 AI 团队实习（arXiv:2603.04022 脚注原文："The work was done during Zilin's internship at DAMO Academy."）。
- **背景**：
  - 最早可确认的论文是 2022 年 MICCAI MMMI workshop 的 M²F（第一作者，西工大署名），据此推断入学不晚于 2021—2022 年（**推断**）。
  - 2023 CVPR PEFAT（第 3 作者，被引 105，全组最高）；2024 MICCAI 两篇；2024—2025 IEEE TMI 连发多篇、IJCV 2025 PICK（第 2 作者）、JBHI 2025 PathBot。
  - 2026：IEEE TIP 一篇；arXiv:2603.04022 第一作者，达摩院实习成果，通讯[张建鹏](02-jianpeng-zhang.md)，合作者含[曹维维](03-weiwei-cao.md)、常琬星、夏勇、[张灵](39-ling-zhang.md)。
- **研究方向**：半监督 / 弱监督医学图像分割与分类、医学视觉问答、视觉—语言对齐、放射报告生成的强化学习。从 2022 年的多模态胶质瘤诊断预后，到以文本为锚点的分割与视觉问答，再到报告生成的强化学习，主线只有一条：==用文本 / 语言信号去补医学影像标注的不足== —— 正是 RADAR 的方法论内核。
- **在 RADAR 里**：第 4 位作者，**6 位共同第一作者之一**（PubMed 的 EqualContrib 字段独立确认只有前 6 位）。*Science* 官网作者页列的 CRediT 角色为 Data curation、Formal analysis、Validation、Writing - original draft（单一来源），==没有 Software==。推断：不写训练代码主干，做数据集的整理清洗、评测分析与初稿撰写，偏报告文本与诊断评测这一侧（**推断**）。不在 PANDA 作者表内，也不在达摩院平扫 CT 早筛那条 *Nature Medicine* 系列里。
- **与其他作者的关系**：[夏勇](13-yong-xia.md) → [张建鹏](02-jianpeng-zhang.md) → 招师弟来实习的典型闭环，同一条线上还有[谢雨彤](12-yutong-xie.md)、#11 Shaoteng Zhang；参见 [academic-pipeline](../sources/academic-pipeline.md)、[damo-hiring](../sources/damo-hiring.md)。西工大同门里日常合作最紧的是 Qingjie Zeng、Mengkang Lu。
- **学术指标**：Google Scholar 总被引 601、h-index 12、i10-index 13（2026-09-20 抓取，页面列 16 条），四人里最高。OpenAlex A5100647576 把华南理工脑机接口方向与 AIAA 航空方向的同名者合并了进来，那组数字不可用。
- **对 Shu**：无直接关系。处理的是重建后图像加报告文本，不碰投影域、能谱与噪声统计，人在国内也没有招人权限。唯一可用的是那篇报告生成强化学习里「诊断多样性采样、数据质量优于数量」的做法 —— 将来给材料分解或 PVAT 结果配自动化评测时可以当参考，不作为联系对象。
- **来源**：https://www.science.org/doi/10.1126/science.aec6129 , https://orcid.org/0000-0003-2437-283X , https://scholar.google.com/citations?user=ngPgM1QAAAAJ , https://openreview.net/profile?id=~Zilin_Lu2 , https://arxiv.org/abs/2603.04022 , https://api.crossref.org/works/10.1126/science.aec6129
- **查不到**：中文名（没有任何英↔中对照来源，不做拼音反推）；本科 / 硕士院校；达摩院实习的起止时间与是否已毕业；宁波市第二医院这个署名的由来。

### #5 常琬星 Wanxing Chang — 最优传输出身的达摩院算法工程师，RADAR 仅有的三位代码作者之一

- **论文单位**：Alibaba DAMO Academy（杭州）+ [湖畔实验室](../sources/hupan-lab.md)（杭州）。
- **现职**：阿里巴巴达摩院算法工程师（职级未查实）。判据是 Google Scholar 机构栏写 Alibaba DAMO Academy、2024-12 起连续以达摩院署名发论文、个人主页自 2024-07 起停更。
- **背景**：
  - 本科：电子科技大学生物医学工程。硕士：上海科技大学信息科学与技术学院计算机科学。
  - 个人主页自述 final-year master student，该页最后一次提交为 2024-07-10，把在读末年钉在 2023—2024 学年；最早的达摩院署名见于 2024-12 的 arXiv 预印本，因此推断 2024 年下半年入职（**推断**）。
  - 导师**推断**为石野（Ye Shi，上科大 YesAI 实验室负责人）与 Jingya Wang —— 依据是两篇 NeurIPS 的固定合作者，主页无 advisor 字样。Jingya Wang 的中文名「汪婧雅」只有单一来源，不当定论。
- **研究方向**：两条并行主线。(1) 上科大时期的理论底子：最优传输 + 开放世界学习 —— 通用域自适应（NeurIPS 2022 Spotlight，被引 144）、带噪标签学习（CSOT，NeurIPS 2023）。(2) 达摩院之后：3D CT 视觉—语言预训练与评测（CT-FineBench、AtomiMed、Disease-Centric VLP、RadSight）、病理全切片分析（Pixel-Mamba，ICCV 2025），并保留与中科院计算所的图神经网络合作。==这四人里唯一从理论工具跨进医学多模态工程的。==
- **在 RADAR 里**：第 5 位作者，**6 位共同第一作者之一**。*Science* 官网作者页列的 CRediT 角色多达十项、含 Software（单一来源）；==Zenodo 代码存档只署三位 creator：张建鹏、曹维维、常琬星==，两边完全吻合 —— 主力工程实现者，不是挂名。不在 PANDA 里（时间上也不可能），但几乎出现在达摩院 2026 年所有 CT 视觉语言模型的论文上，另有 *Nature Communications* 2026 脂肪肝多模态 AI 第 3 作者。技术侧的位置见 [radar-technical-teardown](../sources/radar-technical-teardown.md)。
- **与其他作者的关系**：进达摩院后同时跨两支 —— 吕乐 / Ke Yan / Dakai Jin 的病理与影像线，和[张灵](39-ling-zhang.md) / [张建鹏](02-jianpeng-zhang.md) / [曹维维](03-weiwei-cao.md) 的 RADAR 线，两支都在的人很少；见 [damo-lineage](../sources/damo-lineage.md)。
- **学术指标**：Google Scholar 总被引 211、h-index 4、i10-index 3（2026-09-20 抓取），84% 的引用集中在那两篇 NeurIPS 上。ORCID 0009-0004-0253-1830（投稿系统里作者本人认证），DBLP pid 332/1430。
- **对 Shu**：==这四人里唯一值得看一眼的，但看的是方法不是人。== 最优传输那套「带结构约束地把两个分布对齐」，正对着材料分解里仿真标定迁移到真实 NAEOTOM / Canon 数据的域偏移问题，是目前没在用的工具，CSOT 的课程式 + 结构感知 OT 值得读一遍。另外是真正写 RADAR 代码的三人之一 —— 要复现 RADAR 或问工程细节，找这里比找通讯作者准。作为求职 / 博后去向无价值：在国内、无招人权限、不做成像物理、不碰能谱与重建。
- **来源**：https://changwxx.github.io/ , https://orcid.org/0009-0004-0253-1830 , https://scholar.google.com/citations?user=07BLeI8AAAAJ , https://dblp.org/pid/332/1430.html , https://zenodo.org/records/21271172 , https://www.science.org/doi/10.1126/science.aec6129
- **查不到**：本硕的起止年份、达摩院职级。GitHub 资料 2026-09 仍写 location = Shanghai，与杭州的达摩院不一致，不据此下任何结论。

### #11 Shaoteng Zhang — 与 Zilin Lu 同门的西工大在读博士，RADAR 的评测与作图

- **论文单位**：达摩院（杭州）+ 宁波市第二医院放射科 —— 与 #4 一字不差，同样没有西北工业大学。这个写法在自己当第一作者的 arXiv:2607.09135 上被原样重复，==不是排版事故，是课题组自己的选择==。
- **现职**：西北工业大学计算机学院在读博士研究生，导师[夏勇](13-yong-xia.md)。OpenReview 档案 2022-10 注册，推断 2021 或 2022 级（**推断**）。未见明文实习脚注，但署名模式与 #4 完全一致，推断同为达摩院实习（**推断**）。
- **背景**：2022 MICCAI MLMI workshop TransWS（第一作者，被引 16）；2023 MICCAI TPRO（第一作者，被引 43，目前引用最高的一篇）；MICCAI 2025 一篇第 3 作者（与 Xiaoyu Bai、Ziyang Chen、夏勇，归属未在 Scholar 页确认）；2026-07 arXiv:2607.09135 Super-Generalist 第一作者 —— 这是 RADAR 的直接后续工作（通才模型与专科分割模型融合），通讯为夏勇 + [张建鹏](02-jianpeng-zhang.md)。
- **研究方向**：弱监督 / 文本提示驱动的病理图像分割（TransWS、TPRO），近两年转向通用医学影像理解与「通才—专才协同」。主线是用更弱的监督信号（文本提示、图像级标签、分割专家先验）去训分割与诊断模型。==这批人里唯一从数字病理切片入手、再转到 CT 的。==
- **在 RADAR 里**：第 11 位作者，**不是共同第一作者**（PubMed 的 EqualContrib 只标前 6 位）。*Science* 官网作者页列的 CRediT 角色为 Formal analysis、Validation、Visualization 三项（单一来源）—— 没有 Data curation、没有 Software、没有 Writing，在 40 位作者里属偏后的贡献梯队。推断：做评测阶段的统计分析与图表，不参与数据构建和代码主干（**推断**）。实际收获是拿到数据与 pipeline 之后独立做出了 Super-Generalist。不在 PANDA，也不在达摩院 *Nature Medicine* 那条线上。
- **与其他作者的关系**：最早两篇的第二作者就是[张建鹏](02-jianpeng-zhang.md)，从入学第一年起就在师兄的直接带教下做课题 —— 达摩院与其说是外部实习单位，不如说是师兄的组。==西工大侧在 RADAR 作者表里的全部人力只有三人==：[夏勇](13-yong-xia.md)、Zilin Lu、本人，三人共用同一个宁波市第二医院署名；[谢雨彤](12-yutong-xie.md) 出自同一条线。
- **学术指标**：Google Scholar 总被引 59、h-index 2、i10-index 2，页面仅列 4 条（2026-09-20 抓取）。ORCID 0009-0005-4976-6351，employment 只有 Northwestern Polytechnical University 一条。四人里最低，属于刚上路的阶段 —— 第一作者的 Super-Generalist 若中稿会明显改观。OpenAlex A5024569575 混入了中国矿业大学岩石力学与中科院大学微分几何两位同名者，数字不可用。
- **对 Shu**：无直接关系 —— 方向、地理位置、职权都无交集，不做任何成像物理。勉强能说的一点：TPRO 用文本提示做弱监督分割，与 PVAT 边界问题上「没有真值标注怎么办」是同一类困境的两种答案（语言先验 vs 物理先验加仿真），属于读一篇论文的价值，不是认识一个人的价值。
- **来源**：https://www.science.org/doi/10.1126/science.aec6129 , https://orcid.org/0009-0005-4976-6351 , https://scholar.google.com/citations?user=YCdOvPcAAAAJ , https://openreview.net/profile?id=~Shaoteng_Zhang1 , https://arxiv.org/abs/2607.09135 , https://pure.nwpu.edu.cn/
- **查不到**：中文名（不做拼音反推）；本科 / 硕士背景；是否已转为达摩院正式员工、是否已毕业；宁波市第二医院署名的由来。

### #17 Zhilin Zheng — 跟吕乐从平安进达摩院的正式研究员，GRAPE 与 RADAR 之间的连接点

- **论文单位**：达摩院（杭州）+ [湖畔实验室](../sources/hupan-lab.md)（杭州）。
- **现职**：达摩院算法研究员（职级未查实）。==与 #4、#11 不同，2022 年起持续以达摩院正式署名发论文，不是实习生。==
- **背景**：
  - 硕士：华东师范大学通信与电子工程学院 / 上海市多维度信息处理重点实验室，导师孙力（Li Sun）。按学号前缀推断 2017 年入学（**推断**）；本科院校未查到。
  - 2019：CVPR 一作 Disentangling Latent Space for VAE by Label Relevant/Irrelevant Dimensions（被引 73，至今最有影响的工作）；2020 ICIP 一篇。
  - 2021（平安科技 / PAII）：ICCV 2021 一作，论文页单位明确印 PingAn Technology；同年与吕乐、Shun Miao 等做胸片骨折的半监督检测。
  - 2023 起（达摩院）：*Radiology* 2023 胰腺导管腺癌淋巴结转移预测；2025 *Nature Medicine* GRAPE（平扫 CT 胃癌大规模筛查，PMID 40555751，第 3 / 58 位）；2025 *BMC Medicine* 幽门螺杆菌内镜 AI；2026 *Radiology: Artificial Intelligence* 胃肿瘤增强 CT 检出、*Medical Image Analysis* 内镜多示例学习、arXiv RadSight 与 TumorChain。
- **研究方向**：早期做生成模型的表征解耦 —— VAE 隐空间按「标签相关 / 标签无关」维度拆分、条件 VAE 的结构与风格分离、多属性图像到图像翻译。转入产业界后全部转向医学影像诊断：胰腺癌淋巴结转移、胃癌平扫 CT 筛查、胃肿瘤检出、内镜多示例学习、放射多模态理解。==四人里唯一真正做过生成模型理论的，也是唯一横跨 CT 与内镜两种模态的。==
- **在 RADAR 里**：第 17 位作者，不是共同第一作者。*Science* 官网作者页列的 CRediT 角色为 Formal analysis、Investigation、Visualization（单一来源），与连续的第 17—20 位 Yanjie Zhou、[Tony C W Mok](19-tony-c-w-mok.md)、[夏英达](20-yingda-xia.md) 完全相同 —— 推断这是达摩院内部被抽调来做评测分析与图表的一组资深工程师，本人提供的是胃与腹部病灶检测方面的既有经验（**推断**）。不带 Software、Data curation、Writing，与代码主干和数据集构建无关。
- **与其他论文的重合**：不在 PANDA 作者表内，但==是 GRAPE（*Nat Med* 2025，平扫 CT 胃癌筛查）与 RADAR 之间的连接点==；达摩院「平扫 CT + AI」这条产品线从胰腺到胃、到内镜、再到通用腹部影像，本人是少数四条线全程常驻的人之一。
- **与其他作者的关系**：迁移轨迹与吕乐同步 —— 华东师大 → 平安 PAII → 达摩院，不是独立跳槽，而是**跟随吕乐那支人马整体迁移**的一员（**推断**：时间吻合，且 2021 年的合作者 Le Lu、Shun Miao、Yirui Wang、Kang Zheng 整体是 PAII 班底、此后也都出现在达摩院论文里；无公开来源明文陈述）。达摩院医疗 AI 因此是两支血统的合流：吕乐 / [张灵](39-ling-zhang.md) 的 PAII 系（PANDA、GRAPE、[夏英达](20-yingda-xia.md)、本人）与[夏勇](13-yong-xia.md)的西工大系（[张建鹏](02-jianpeng-zhang.md)、[曹维维](03-weiwei-cao.md)、Zilin Lu、Shaoteng Zhang），==RADAR 是两支第一次在 Science 正刊上合署的产物==。详见 [damo-lineage](../sources/damo-lineage.md)。
- **学术指标**：没有可用的个人 Google Scholar 页（四人里唯一）。ORCID 0000-0002-2439-9162，仅登记 7 条 work。==同名污染极严重==：另有浙大四院神经内科、诺丁汉大学心理系、大连海军舰艇学院流体力学、环境工程重金属浸出至少四位 Zhilin Zheng，OpenAlex A5025166983 把它们全合并了，works 47 / cited 857 / h 12 一律不可用。可核实的硬数字只有 CVPR 2019 一作被引 73 与 *Nature Medicine* 2025 的第 3 位次，真实 h-index 推断在 6—8 量级（**推断**）。
- **对 Shu**：无直接关系 —— 在杭州、企业算法工程师、没有招人权限、做的是重建后图像的诊断模型。可读的是履历本身：五年内从华东师大硕士挂上 *Nature Medicine* 第 3 作者与 *Science*，靠的不是某个算法，而是吕乐把整支 PAII 队伍搬进达摩院这件事；要理解达摩院为什么能在五年里连发四篇 *Nature Medicine* 加一篇 *Science*，本人是这支队伍里一个可验证的节点。早年的 VAE 隐空间解耦与材料分解同属「把混合信号拆成可解释分量」，但一个靠学、一个靠物理约束，借鉴价值有限。
- **来源**：https://www.science.org/doi/10.1126/science.aec6129 , https://orcid.org/0000-0002-2439-9162 , https://pubmed.ncbi.nlm.nih.gov/40555751/ , https://pure.ecnu.edu.cn/ , https://github.com/alibaba-damo-academy/damo-RadSight , https://arxiv.org/abs/2607.22293
- **查不到**：中文名（没有个人主页、没有 Google Scholar、没有 GitHub，ORCID 只填了 7 条）；本科院校；从华东师大到平安、从平安到达摩院的确切年份；达摩院职级与是否带团队。
