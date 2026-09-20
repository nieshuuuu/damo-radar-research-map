已提交到本地仓库（`master`, commit `d30d9e9`）。报告在 **`/Users/shunie/Developer/damo-radar-research-map/sources/damo-lineage.md`**，原始证据在 `/Users/shunie/Developer/damo-radar-research-map/data/raw/evidence/`。

**⚠️ 两件需要你决定的事**

1. **没有推到 GitHub。** 这个仓库还没有 remote，而建远程库＝公开发布。考虑到里面是活人的履历追踪，而且你之前的仓库公开审计里已经有过踩线记录，我不替你决定 public/private。你说一声 `私有推到 nieshuuuu` 我就建。
2. **本次通用搜索引擎全部不可用**（Google/Bing/DDG/searx/百度/搜狗都返回验证码页，我没绕）。所有结论只来自四类可复核源：PubMed E-utilities、OpenAlex、Wayback、当事人主页。这限制了几个结论，我在报告末尾列了未解决清单。

**核心方法**：用论文署名单位字符串的年度迁移来重建人员流动——它带时间戳、第三方可复核，而人事新闻会消失、领英要登录。代价是发表滞后 6–18 个月，所以报告里所有年份都标明是"论文年"不是"入职年"。

**推翻了任务给的两条前提**

- **吕乐的 NVIDIA 一段不成立。** 主页原文只有一句无日期的残句 "...and from NVIDIA AI-Infra division"。三条反证：Siemens(→2013-01)→NIH(五年多)→PAII(2018-06)→达摩院(2021-07) 时间线没有空隙；PubMed 查不到任何他署 NVIDIA 的论文；这句话 2022 年就写下且至今一字未改（Wayback 比对）。我判断它是"我的团队来自 NIH 和 NVIDIA"的压缩表述——旁证是 **NVIDIA 的医学影像组当时也在 Bethesda**。
- **达摩院医疗 AI 不是 2021 年才有的。** 2020 年就有 "HealthTech Division, DAMO Academy"，2021 年有 "Healthcare Intelligence, AIC"，方向是生信/基因组，由 Xian-Sheng Hua 一线负责。2021 是**嫁接**不是建院。两条血脉唯一一次同框是 2022 年 MP-GNN 那篇（PMID 35696650）。

**也纠正了我自己的一个初判**：我先以为 "Washington, DC" 是 "860 Washington Street, New York" 的解析错误，逐年拆开后发现两地在 2026 年并存，对应两支队伍——DC 是 Ling Zhang + Yingda Xia 的平扫 CT 早筛线（*Nature Medicine*/*Science*），NY 是 Dakai Jin + Le Lu + Ke Yan 等 8 人的头颈放疗线（*Radiology*）。

**主要新料**

- **PAII Inc. = 平安科技美国研究院**，有它自己招聘页的原话为证："PingAn Technology, US Research Lab at Silicon Valley" / "accelerate PingAn group's transition to a technology driven enterprise"。2016 年创立，双点：Palo Alto + Bethesda（6720B Rockledge Drive）。**Bethesda 点距 NIH 临床中心 3.5 公里**（Nominatim 取坐标算的，不是目测）——公司明明有硅谷点却专门为这支队伍在马里兰单开一个，说明被挖的是一个已成形、不愿搬家的组。官网 2023-10 后域名注销；**两个站点是分开死的**：医疗影像署名 2022 年断档，硅谷线活到 2025–26。
- **迁徙名单从 4 人补到 12 人**，每人给 PAII/DAMO 署名年份。两个反例：Yingda Xia 不是 PAII 来的（霍普金斯），Adam Harrison 没去达摩院（现在 Riverain Technologies）。
- **吕乐现在蚂蚁 Ant Group Sunnyvale**（Nat Commun 2026, PMID 42426002），人还在美国。我把蚂蚁 2025–26 全部 1221 篇论文的署名扫了一遍查 15 位旧部——**零命中，他一个人走的**，核心班底留在达摩院，三篇 2026 旗舰的通讯作者都是 Ling Zhang。
- **Xiaosong Wang（ChestX-ray8 一作）也在达摩院待过**——NIH→NVIDIA(2018-21)→达摩院→上海人工智能实验室。这条线索此前在本项目任何文件里都没出现过。他和吕乐那批人在 NIH 和达摩院**两次独立交汇**。
- **Bethesda 三角**：NIH 临床中心、平安 PAII、NVIDIA 医学影像组三家都在 Bethesda，2015–2021 从同一人才池抓人。这不是三次孤立跳槽，是几平方公里内的一个人才市场。
- **吕乐在 NIH 的编制细节**：DeepLesion 论文里他署 Clinical Image Processing Service，另外三位（Ke Yan / Xiaosong Wang / Summers）署 Imaging Biomarkers and CAD Laboratory。而 CSR 页面显示 Summers 正是 CIPS 的创始主任。所以"吕乐是 Summers 的人"在人事上不准确、在学术谱系上完全准确。

**顺带确证两个中文名**：Le Lu = **吕乐**（他主页自列《放射学实践》2018 年那篇中文文章）、Youbao Tang = **唐有宝**（主页页头，现 Google 高级软件工程师）。`data/authors-table.md` 里 40 位作者的中文名仍是待填——那是另一条任务线，不在本次范围。

**未解决、请勿填猜测**：吕乐离职/入职的确切月份（传闻 2025-06 / 2021-08）、达摩院美国实体是否还在招人、PAII Bethesda 关闭的官方说法（不存在公开声明，只有署名断档+域名注销两项间接证据）。这三条都需要中文科技媒体或领英，本环境够不到。