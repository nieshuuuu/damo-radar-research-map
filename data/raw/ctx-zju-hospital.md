已完成调查。以下是结果。

---

# 浙大一院 × 梁廷波 机构生态深挖
## —— 回答「RADAR 那 424,911 例增强腹部 CT 是怎么拿到的」

> 调查日期 2026-09-20。方法：PubMed eutils 原始 XML（可复现）、机构官网直取、Google/Bing 索引。凡未查到的一律标"未查到"，不做推测填充。

---

## 0. 先确认被解释的那个数字

Science 结构化摘要原文：**"We constructed RAD-CT, a large abdominal CT dataset, consisting of 424,911 examinations and 15 million anatomy-wise pairs"**；内部真实世界评测队列 39,160 例，外部 8 家中心，AUC 0.913（95% CI 0.911–0.915）。
- https://www.science.org/doi/10.1126/science.aec6129 （Science 393(6817), eaec6129, 2026-09-17；正文 NO ACCESS，仅结构化摘要与编辑导读开放）
- 开源仓库 https://github.com/alibaba-damo-academy/damo-radar ｜ Zenodo https://zenodo.org/records/21271172 ｜ 权重 https://huggingface.co/radar-generalist

**关键限制（必须先说）**：RADAR 正文与 Methods 在付费墙后，所以"424,911 例中有多少来自浙大一院、跨几年、伦理批件号是什么"**目前无法从公开材料直接读出**。下面做的是把"谁有能力、有制度、有历史给出这个量级的数据"这条链补全，并用 PANDA 的同队伍公开伦理声明作为最强代理证据。

---

## 1. 梁廷波：履历、职务、头衔（把握：高）

### 1.1 时间线（三处独立来源互证）

| 时间 | 职务 |
|---|---|
| 1965-10 | 生于河南封丘 |
| 1981-09 ~ 1984-07 | 新乡医学院医疗系（今河南医药大学） |
| 1984-08 ~ 1989-08 | 河南省封丘县李庄人民医院 普外科住院医师 |
| 1989-09 ~ 1992-07 | 浙江医科大学 外科学硕士 |
| 1992-07 ~ 2011-11 | 浙大一院 主治→主任医师、肝胆胰外科副主任；**2005-06 起副院长** |
| 1999-09 ~ 2002-06 | 浙江大学医学院 外科学博士 |
| 2011-11 ~ 2018-12 | **浙大二院** 副院长、肝胆胰外科主任/器官移植中心主任 |
| **2018-12 ~ 2025-07** | **浙大一院 党委书记** |
| **2025-07 至今** | **浙大一院 院长、党委副书记**（前任院长王伟林；顾国煜接任党委书记） |

来源：
- 中文维基（含引文链）https://zh.wikipedia.org/wiki/%E6%A2%81%E5%BB%B7%E6%B3%A2
- 浙江大学个人主页（更新 2026-03-19，"职务：医学院附属第一医院院长，党委副书记"）https://person.zju.edu.cn/0012056
- 河南医药大学校友网《优秀校友事迹——梁廷波》（2023-07-20，逐年履历）http://www.xxmu.edu.cn/xyh/info/1038/1513.htm
- 人事调整报道 https://finance.sina.com.cn/stock/stockzmt/2025-07-28/doc-infhzpnv0158814.shtml

> **这条时间线对本案的意义**：PANDA（2023-11 Nat Med）署名时他是**党委书记**；RADAR（2026-09 Science）署名时他是**院长**。一家医院的党委书记同时是肝胆胰外科学科带头人，这是"能把全院影像+报告数据打通"的组织前提——不是科室主任能办的事。

### 1.2 头衔与学术指标

- **国家杰出青年科学基金：2009 年**（浙江大学学术委员会"国家杰出青年基金获得者"名单第 76 位：梁廷波 / 医学部 / 2009）。存档页 https://web.archive.org/web/20250120164609/http://webwescms.zju.edu.cn/redir.php?catalog_id=5481&object_id=5718
- **教育部长江学者特聘教授**：维基分类为 **2011 年度**；医院官方页写"**两次**获得教育部长江学者特聘教授"，校友网补充第二次为"**抗疫特岗学者（人文社科）**"（2020 年新冠后设立的特设岗）。
- **第十四届全国人民代表大会代表**（2023–2028）。来源：河南医药大学校友网（同上）、社科文献《中国式现代化研究数据库》人物简介 https://cpms.ssap.com.cn/
- 其他：卫生部有突出贡献中青年专家、国家百千万人才工程、吴阶平-保罗·杨森医学药学奖、白求恩奖章、全国创新争先奖（2023）、全国五一劳动奖章、谈家桢生命科学奖、何梁何利科技进步奖、浙江省特级专家、浙大求是特聘教授、**美国医学与生物工程院会士（AIMBE Fellow）**、美国外科医师协会会员（FACS）。
- 学术产出：主持国家 863、国自然重点项目（4 项）、国家重点研发计划等 30 余项；一/通讯作者 SCI 150–170 余篇；Google Scholar 被引 约 3.4 万。
  - 医院个人页 https://www.zy91.com/department/doctor/74/328
  - Google Scholar https://scholar.google.com/citations（"Cited by 34,062"，2026-09 索引）

### 1.3 一个必须写进故事的事实：两次院士落选

- 2025-08-20 中国科学院公布 2025 年院士增选**有效候选人** 639 人，梁廷波在**生命科学和医学学部**名单内，**推荐人为西湖大学校长、中科院院士施一公**；媒体明确指出"这也是梁廷波**继 2023 年之后再度入围**"。
  - 澎湃/新浪 https://finance.sina.com.cn/jjxw/ （2025-08-21）、央视网 https://news.cctv.com/2025/08/22/
  - 中科院公告 https://www.cas.cn/ （2025-08-20）；材料公示汇总表 https://yszx.casad.cas.cn/
- 2025-11-21 公布**当选**名单：中科院生命科学和医学学部新增 13 人（蔡秀军、邓宏魁、房静远、傅向东、何舜平、胡海岚、马克平、瞿礼嘉、王拥军、曾木圣、周俭、朱冰……），**梁廷波不在其中**；同为浙大系的邵逸夫医院蔡秀军当选。
  - https://www.cas.cn/ 2025-11-21 公告；健康界汇总 https://www.cn-healthcare.com/ （"医药卫生界 21 人当选"）

> **解读（我的推断，标明是推断）**：2023、2025 两轮未当选，下一轮是 2027。一篇《Science》正刊 + 全球首个开源通用医学影像模型，在 2026-09 这个时间点落地，其"简历价值"不需要多解释。这不是阴谋论，是把公开事实并排摆出来的结果。

---

## 2. 两个实验室：级别、批复、主任、资源

### 2.1 浙江省胰腺病研究重点实验室（注意：官方名是"胰腺**病研究**"，不是"胰腺疾病"）

**这是论文英文署名 "Zhejiang Provincial Key Laboratory of Pancreatic Disease" 的中文正身。**

- **级别**：浙江省重点实验室（省科技厅序列，非国家级）。
- **批复**：**浙江省科学技术厅于 2016 年批准成立**。
- **依托**：浙大一院；依托国家重点学科（普通外科学）、国家临床重点专科（普通外科学、器官移植学）、卫健委多器官联合移植研究重点实验室。
- **主任：梁廷波**；**副主任：章琦**（见 §5.4）。
- **资源（官方页原文）**：场地 2624 ㎡，分布于庆春路院区 11 号楼与大学路院区 2/4 号楼；质谱流式（Helios、Hyperion）、多色流式（Fortessa、CantoII）、MoFlo Astrios EQ 超高速分选、二代测序仪、Seahorse、激光共聚焦、单细胞显微捕获等，**大型设备总值约 9000 万元**；依托肝胆胰外科 **9 个病区、340 余张床位**；正高 20 人、副高 18 人、中级 16 人，年培养硕博及博后 50 名以上。
  - 官方页 https://www.zy91.com/research/platform/91/13
  - 团队描述（浙大癌症研究院，2020-12-08）https://zucc.zju.edu.cn/2020/1203/c54385a2223618/page.htm

**独立交叉验证（我做的）**：PubMed 中 `"Zhejiang Provincial Key Laboratory of Pancreatic Disease"[Affiliation]` 共 **669** 篇；按发表年设上界计数，**2016 年及以前 = 0 篇，2017 年 = 3 篇，2018 累计 15，2019 累计 46，2020 累计 99**。首次出现在 2017 年，与"2016 年批准"完全吻合。
复现命令：
```
curl -s "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&retmode=json&retmax=0&term=%22Zhejiang+Provincial+Key+Laboratory+of+Pancreatic+Disease%22%5BAffiliation%5D&datetype=pdat&mindate=1900&maxdate=2016"
```

### 2.2 教育部胰腺疾病国际合作联合实验室

- **级别**：教育部"国际合作联合实验室"计划（部级平台序列）。
- **主任：梁廷波**（两处独立人物页均列"教育部胰腺疾病国际合作联合实验室主任"）。
  - 美迪康会务通讲者页 https://www.sciconf.cn/cn/person-detail
  - 广东省精准医学应用学会 http://m.gdpmaa.com/
- **它是浙大一院唯一的一个**：医院《科研概况》原文——"医院牵头**全国重点实验室 1 个**（传染病重症诊治全国重点实验室）、国家自然科学基金委基础科学中心 1 个、国家临床医学研究中心 1 个，**教育部国际合作联合实验室 1 个**"。https://www.zy91.com/research
- **⚠️ 批复年份：未查到**。教育部未在可公开索引页面给出该实验室的立项批次与年份，我不编。PubMed 中带 "Ministry of Education" + "Pancreatic Disease" 的署名共 144 篇，可作为使用起点的间接线索，但不足以定年。

> **对数据来源问题的意义**：这两块牌子解释了"为什么胰腺/腹部数据集在浙大一院落地"，但**它们都是胰腺方向**。RADAR 覆盖 18 个解剖结构、146 种影像征象——数据口径远超胰腺实验室的边界。真正的数据闸门在**放射科**（见 §5.5），不在这两个实验室。

---

## 3. 浙大一院的体量

官方《医院简介》与首页数据块（数据更新于 2026-07-09）：
- **建院 1947 年 11 月 1 日**（首任院长王季午；建院时 65 张床、66 名员工、占地三亩八分，"弄堂医院"）
- **7 大院区**：总部项目（余杭文一西路 1367 号）、庆春院区、之江院区、城站院区、大学路科教基地、钱塘转化中心、浙江省公共卫生临床中心（建设中）
  - https://www.zy91.com/about/location
- **开放床位 5000 余张**；占地 519.3 亩；建筑面积 73.3 万㎡；**员工 10000 余人**
- 国家重点学科 2 个、国家临床重点专科 30 个（另一处写 28 个）
- **三级公立医院绩效考核（"国考"）：2024 年度在 1658 家三级公立综合医院中连续 7 年 A++ 等级、全国前 1%**（2026-04 国家卫健委发布）
- 中国医院科技量值（STEM）**综合排名全国第三**；传染病学连续 7 年全国第 1
- 年科研经费连续 6 年超 3 亿元；2025 年国自然立项 169 项；国家科技进步奖特等奖 1 项（建国以来卫生系统唯一）、一等奖 2 项、二等奖 9 项
- 复旦版《2023 年度中国医院排行榜》：浙大一院位列最高等级 **A++++**（同级不分先后，全国 20 家）
  - https://www.zy91.com/general ｜ https://www.zy91.com/general/detail ｜ https://rank.cn-healthcare.com/fudan/national-general/year/2023

**⚠️ 首页数据块里同时出现"国考综合排名全国第 5"和"全国第 2"两个数字**（不同年度的轮播未清理）。《医院简介》正文只写 A++ 等级、前 1%，不给名次。我按正文口径采信，不替它们调和。

**年门诊量 / 年 CT 检查量**：
- 医院官网**不公布**。
- 行业媒体《看医界》2025-09-12《总投资 39 亿元！浙医一院台州医院来了》：**"该医疗集团年门诊服务量达 608 万余人次，年住院患者约 22 万余人次，年手术量超过 11 万例"** https://kanyijie.com/
  - 口径是"**医疗集团**"（含托管/紧密帮扶单位），不是本部，且为二手来源。**不要当成本部门诊量用。**
- **年 CT 检查量：公开渠道无任何数字**。任何声称的数值都是编的。

---

## 4. 浙大一院 × 阿里/达摩院：正式关系的真相

### 4.1 一个重要的**否定性发现**

**没有查到浙大一院与阿里巴巴/达摩院之间任何公开的"共建实验室""战略合作协议"或联合签约新闻稿。** 这一点很反直觉，但多轮检索都是空的。作为对照，同城同校的其他单位**都有**：

| 时间 | 主体 | 形式 | 来源 |
|---|---|---|---|
| 2020-07-17 | **浙江省人民政府** 授牌 **湖畔实验室（数据科学与应用浙江省实验室）**，**阿里巴巴达摩院牵头建设**，5 年总投资超 100 亿 | 省实验室 | https://hznews.hangzhou.com.cn/chengshi/content/2020-07/18/content_7776502.htm |
| 2025-07-14 | **浙江大学** × 阿里巴巴集团，共建**人工智能安全联合实验室**，首批 10 个课题开题 | 校级联合实验室 | http://www.cs.zju.edu.cn/ ；央广网转载 https://www.sohu.com/ |
| 2026-05-26 | **浙大二院** × 阿里巴巴达摩院，**正式签署战略合作协议** | 院级战略合作 | https://view.inews.qq.com/ |

> **所以**：浙大一院与达摩院之间是**论文级/项目级**的长期协作，没有走"挂牌签约"这条路。而**湖畔实验室**才是那个制度性接口——它让达摩院的人可以用"**浙江省实验室**"的身份署名，而不是纯企业身份。RADAR 作者里 11 人挂"达摩院 · 湖畔实验室"，这不是修饰，是身份工程。

### 4.2 实际的合作年表（我用 PubMed 硬查出来的，不是从新闻拼的）

检索式：`Alibaba[Affiliation] AND "First Affiliated Hospital of Zhejiang"[Affiliation]` → **11 篇**。

```
2022  J Natl Cancer Cent  39036546  放疗危及器官/靶区自动勾画
2023  Cancers             36831535  FAPI PET/CT vs FDG PET/CT
2023  Nat Med   ★         37985692  PANDA：平扫CT深度学习大规模胰腺癌检出
2025  BMC Cancer          40082829  卵巢癌 SNP 脂代谢
2025  Nat Med   ★         40555751  GRAPE：平扫CT胃癌大规模筛查
2025  Nat Med   ★         40835970  iAorta：平扫CT急性主动脉综合征诊断
2025  BMC Med             41063106  内镜 AI 辅助幽门螺杆菌诊断
2026  Ann Oncol ★         42025761  平扫CT结直肠癌检出，多中心国际研究
2026  Clin Transl Med     41724912  AI 在非增强 CT 主动脉综合征中的角色
2026  Med Image Anal      42685436  内镜弱标注 MIL
2026  Radiology           41528225  喉/下咽癌淋巴结包膜外侵犯 CT 识别
（另）2026 Nat Med ★      42618635  肝脏恶性肿瘤 AI：多中心 + 单臂试验
（另）2026 Science ★      42752131  RADAR
```
复现：
```
curl -s -G "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi" \
  --data-urlencode "db=pubmed" --data-urlencode "retmode=json" --data-urlencode "retmax=60" \
  --data-urlencode 'term=Alibaba[Affiliation] AND "First Affiliated Hospital of Zhejiang"[Affiliation]'
```

**关键点：这条合作线不止肝胆胰外科。**
- **iAorta（Nat Med 2025-08，PMID 40835970）** 通讯作者是**浙大一院血管外科张鸿坤（Hongkun Zhang）**，46 位作者里浙大一院血管外科占了近一半；新华网 2025-08-27 报道"浙江首创主动脉急诊 AI 模型" http://csj.xinhuanet.com/
- **iAorta 与 RADAR 的共同作者**（我算的）：`Jianpeng Zhang`、`Tony C W Mok`、**`Wenbo Xiao`（肖文波，浙大一院放射科）**。
- 这说明浙大一院对达摩院开放的是**院级、跨科室**的通道：肝胆胰外科（梁廷波/章琦）、血管外科（张鸿坤）、放射科（肖文波）、放疗科（叶香华）、消化内科（虞朝辉）全部在内。

### 4.3 达摩院这条"平扫 CT 一扫多筛"产品线（用于定位 RADAR 的位置）

2023 胰腺（PANDA）→ 2025-06 胃（GRAPE，浙江省肿瘤医院）→ 2025-08 主动脉（iAorta，浙大一院）→ 2026-04 结直肠（Ann Oncol）→ 2026 肝脏（Nat Med，盛京+浙大一院）→ **2026-09 RADAR（从"一病一模"转向"一个模型看所有病"）**。产品落地平台：达医智影 https://damomed.com
- 人民网 2023-11-29 https://health.people.com.cn/
- 新华网 2026-04-28 http://www.news.cn/tech/
- 潮新闻 2025-06-25（GRAPE）https://tidenews.com.cn/

---

## 5. PANDA → RADAR 的连续性（这一节全部是 PubMed 原始 XML 算出来的，可复现）

### 5.1 共同作者：**恰好 4 人**

| 姓名 | RADAR 位次 | PANDA 位次 | 单位 |
|---|---:|---:|---|
| **Qi Zhang（章琦）** | **1**（第一作者） | 33（共同通讯） | 浙大一院肝胆胰外科 |
| **Yingda Xia（夏应达）** | 20 | **2**（共同一作） | 达摩院 · Washington DC / New York |
| **Ling Zhang（张灵）** | 39（AI 侧资深） | 35（共同通讯） | 达摩院 · Washington DC |
| **Tingbo Liang（梁廷波）** | **40**（末位通讯） | 34（共同通讯） | 浙大一院肝胆胰外科 |

PANDA 36 位作者、RADAR 40 位作者。复现脚本已在本轮跑过，用 `data/pubmed-37985692-panda.xml` 与 `data/pubmed-42752131.xml` 两个本地 XML 直接比对 `<Author>` 节点。

> **角色翻转是整件事的核心**：PANDA 里浙大一院是**第四方参与单位**（牵头是上海市胰腺疾病研究所，第一作者曹凯在长海医院放射科），梁廷波、章琦只是并列通讯之二；RADAR 里**章琦是第一作者、梁廷波是末位通讯，浙大一院从提供数据的"合作中心"变成了"牵头单位"**。这三年发生的事，就是浙大一院把自己从数据供应方谈成了署名主导方。

### 5.2 中间那篇被漏掉的论文

`Liang Tingbo[Author] AND Zhang Ling[Author]` 共 3 篇：42752131（RADAR）、37985692（PANDA），以及——

**PMID 42618635 ｜ Nature Medicine 2026 ｜ *Large-scale AI-guided liver malignancy diagnosis: multicenter study and a single-arm trial* ｜ doi:10.1038/s41591-026-04589-y**

- 共同通讯：**Ke Yan（达摩院/湖畔）、Qi Zhang（浙大一院）、Yang Hou（盛京）、Tingbo Liang（浙大一院）、Ling Zhang（达摩院 Washington DC）、Yu Shi（盛京）**
- 与 PANDA 重叠的还有 Xu Han（浙大一院肝胆胰外科）、Kai Cao（上海胰腺所）、Yang Hou、Yu Shi
- **这是 PANDA 与 RADAR 之间唯一的直接桥梁**，而且它已经带了单臂试验（single-arm trial）——说明这条线在 2026 年已经从"回顾性建模"推进到"前瞻性验证"。

### 5.3 合作年表

```
2022        放疗自动勾画（J Natl Cancer Cent）       ─ 浙大一院首次与达摩院同框
2023-11     PANDA（Nat Med）                        ─ 梁廷波/章琦/夏应达/张灵 四人首次同框
2025-08     iAorta（Nat Med）                       ─ 达摩院打通浙大一院血管外科+放射科
2026        肝脏恶性肿瘤 AI（Nat Med）              ─ 章琦/梁廷波/张灵 再同框，加入单臂试验
2026-09-17  RADAR（Science）                        ─ 浙大一院牵头，章琦第一作者，梁廷波末位通讯
```

### 5.4 Qi Zhang = **章琦**（把握：高；证据链见下）

- 中文学术媒体两处独立把 Qi Zhang 的论文署名对应到"章琦"：
  - 《Nature》喻国灿/梁廷波/**章琦**团队 胰腺靶向脂质纳米颗粒（2026-03）https://zhuanlan.zhihu.com/
  - 《GUT》浙江大学梁廷波/**章琦** MTFP1 驱动胰腺癌肝转移定植（2026-02）https://news.bioon.com/
- 人物页：**章琦**，浙大一院肝胆胰外科副教授/副主任医师/博导；**院长助理、科研部副主任、浙江省胰腺病研究重点实验室副主任**；国家高层次青年人才、万人计划青年拔尖人才、国家重点研发计划首席青年科学家、浙江省杰青；浙大临床医学八年制、**浙江大学外科学博士、美国 NIH 博士后**。
  - https://www.sciconf.cn/cn/person-detail ｜ https://www.haodf.com/doctor/ ｜ https://www.instrument.com.cn/
- 网大论坛 2025-02 讨论帖称其"出生于 1986 年、39 岁、浙江顶级医院最年轻院领导、历任科研部副主任→院长助理→**院党委副书记**"——**论坛来源，把握：低，仅作线索，不作为结论**。https://www.netbig.top/
- PubMed 侧：`qi.zhang@zju.edu.cn`，浙大一院肝胆胰外科，在 Gut（PMID 36113977，第一作者）、Nat Med 42618635、Science 42752131 上均与梁廷波并列通讯。

> **师承结构**：梁廷波（1965）→ 章琦（1986），差 21 岁，八年制—博士—NIH 博后—回院—科研部副主任—院长助理。RADAR 把第一作者位给章琦，是**接班安排写进 Science 署名**。这和 Larson lab / Wang lab 的传承逻辑同构，只是中国三甲医院版本里，"实验室"和"行政序列"是同一条梯子。

### 5.5 两个被低估的人

- **肖文波（Wenbo Xiao）**，浙大一院放射科，RADAR #38、iAorta #38。**他才是 424,911 例影像的实际闸门**——外科主任要不到全院放射 PACS，放射科才能。RADAR 放射科三人：李志（Zhi Li）、薛星（Xing Xue）、肖文波。
- **Yan-Jie Zhou（周彦捷）**，达摩院·湖畔·浙大计算机学院，RADAR #18、iAorta #3。达摩院侧的跨项目连接件。

### 5.6 ⭐ 最硬的一条交叉验证：基层医院名单不是达摩院的，是梁廷波的

RADAR 的 9 家基层医院（嘉兴学院附属医院、安徽绩溪县人民医院、景宁畲族自治县人民医院、嵊州市人民医院、海宁市人民医院、安吉县人民医院、兵团第一师医院……）看起来像是为了外部验证临时凑的。**不是。**

比对 **PMID 36113977 ｜ Gut 2023 ｜ *Mass cytometry-based peripheral blood analysis as a novel tool for early detection of solid tumours: a multicentre study*（章琦第一作者，梁廷波通讯，与阿里无关）**，其合作中心名单：

| Gut 2023（章琦/梁廷波自建网络） | RADAR 2026 |
|---|---|
| Xiaoguang Wang — Jiaxing Second People's Hospital | **Xiaoguang Wang — 嘉兴学院附属医院外科**（嘉兴二院即嘉兴学院附属医院） |
| Yuming Gao — Jixi County People's Hospital | **Yuming Gao — 安徽绩溪县人民医院普外科** |
| Haifeng Huang — Shengzhou People's Hospital | Yiping Liu — 嵊州市人民医院放射科 |
| Minghui Xu — Haining People's Hospital | Dongjie Chen — 海宁市人民医院普外科 |
| Chaohui Yu — 浙大一院消化内科 | **Chaohui Yu — RADAR #34** |
| 长兴、湖州中心、上虞、温州一院、浙江省人民医院… | — |

**两个人名一字不差、四家县级医院同一批**。结论：RADAR 的"基层外部验证网络"是梁廷波/章琦**至少从 2022 年就已经建好、并在自己的多中心临床研究里跑过一轮**的浙江省县域医院网络。达摩院接到的不是一堆散数据，是一张**已经通过伦理、已经磨合过数据交换流程**的现成网络。

**这就是"424,911 例是怎么拿到的"的真正答案的一半**：不是靠一次谈判，是靠十年临床多中心网络 + 院级行政权限的叠加。

---

## 6. 中国的合规框架：这种数据集要什么审批，论文怎么写

### 6.1 论文实际怎么写（PANDA 原文，可直接读，作为 RADAR 的代理）

PANDA 开放获取全文 https://pmc.ncbi.nlm.nih.gov/articles/PMC10719100/ ，**Methods → Ethics approval** 原文：

> "The retrospective collection of the patient datasets in each cohort was approved by the institutional review board (IRB) at each institution **with a waiver for informed consent**: the Shanghai Institution of Pancreatic Diseases (SIPD) IRB, Shengjing Hospital of China Medical University (SHCMU) IRB, **First Affiliated Hospital of Zhejiang University (FAHZU) IRB**, … and General University Hospital in Prague (GUHP) IRB. **All data in this study were de-identified prior to model training, testing and reader studies.**"

Data availability 原文：
> "The remaining datasets used in this study are **currently not permitted for public release by the respective institutional review boards**. Requests for access to aggregate data … **All data provided are anonymized** … in line with applicable laws and regulations."

**范式三件套**：① 各中心各自 IRB 批准；② **免除知情同意**；③ 建模前去标识化 + 原始数据不公开。RADAR 开源的是**代码与权重，不是 RAD-CT**——GitHub/HuggingFace 只给 demo NIfTI 与外部 MERLIN 测试集流程，与这个范式完全一致。

### 6.2 法规依据（每条给来源）

1. **《涉及人的生命科学和医学研究伦理审查办法》（国卫科教发〔2023〕4号）**，国家卫健委、教育部、科技部、国家中医药局 2023-02-27 联合印发，经国家科技伦理委员会审议通过、国务院同意。
   - 国家卫健委通知 https://www.nhc.gov.cn/ （2023-02-27）
   - 文件解读 http://www.natcm.gov.cn/kejisi/ （2023-02-28）
   - 上海市科委转发 https://stcsm.sh.gov.cn/ （2023-04-12）
   - 全文（北大医学部）https://research.bjmu.edu.cn/llwyh/
   - **第三十二条**规定使用人的信息数据或生物样本开展研究**可免除伦理审查**的情形；卫健委解读列出四类，其中直接相关的是：**"使用匿名化的信息数据开展研究的"**、**"使用已有的人的生物样本/信息数据开展研究，且不涉及个人隐私和商业利益"** 等。
   - ⚠️ 注意：**免除伦理审查 ≠ 免除知情同意**，二者是不同条款；PANDA 写的是"IRB 批准 + 免知情同意"，即**走了审查、豁免了同意**，这是更稳妥的做法。
2. **《个人信息保护法》（2021-11-01 施行）**：医疗健康属**敏感个人信息**，处理需单独同意；但**经匿名化处理后的信息不属于个人信息**，这是回顾性影像研究的主要出口。
3. **《数据安全法》（2021-09-01）**、**《网络数据安全管理条例》（2025-01-01 施行）**。
4. **《国家健康医疗大数据标准、安全和服务管理办法（试行）》（国卫规划发〔2018〕23号）**、**《促进和规范健康医疗大数据应用发展的指导意见》（国办发〔2016〕47号）**——确立健康医疗大数据"国家重要基础性战略资源"定位与责任单位制度。
5. **《人类遗传资源管理条例》及 2023 年实施细则**：管的是**人类遗传资源材料与基因数据**，**CT 影像与文本报告不在其管辖范围**。这点很重要——影像数据的跨境敏感度**低于**基因数据，这也是影像 AI 更容易做中外联合署名的结构性原因。
6. **跨境**：《数据出境安全评估办法》（2022-09-01）、《促进和规范数据跨境流动规定》（2024-03-22）。

### 6.3 ⚠️ 一个我无法核实、但必须指出的开放问题

RADAR 的 AI 侧资深通讯 **Ling Zhang 单位写的是"DAMO Academy, Alibaba Group, **Washington DC**"**，Yingda Xia 同样在美。PANDA 时代 Ling Zhang / Le Lu / Yingda Xia 挂 New York。

**这意味着这项研究天然触及数据出境合规问题**。常规做法是"数据不出境、模型出境"（境内训练、境外成员只接触模型与聚合结果）。**但 RADAR 正文在付费墙后，我无法验证它是否、以及如何写了这一点。** 这是本次调查最值得后续补的一个洞——建议通过机构订阅拿到全文的 Methods 与 Supplementary Materials，直接读它的 Ethics approval / Data availability 段落。

---

## 7. "院长/人大代表 + 工业界 AI"这个模式，中国还有谁在做

| 医院 / 一把手 | 身份 | 产业方 | 产物与时间 | 来源 |
|---|---|---|---|---|
| **上海交大医学院附属瑞金医院 · 宁光** | 中国工程院院士、**院长** | **华为（云）** | **RuiPath 瑞智病理大模型**：2025-02 发布（国内首个进入医院生产流程的临床级病理大模型）→ 2025-06-30 开源发布会（瑞金主办、华为协办）→ 2026-08-30 **RuiPath 2.0**（7B，诊断增至 205 项）；2026-06 华为云智慧医疗专区首批 26 家医院入驻 | https://www.huawei.com/cn/news/2025/6/ ；新华网 2026-08-31 http://www.news.cn/tech/ ；人民网财经 ；上观 https://www.jfdaily.com/ |
| **中山大学肿瘤防治中心 · 徐瑞华** | **院长/主任/所长** | **腾讯（觅影）** | 2017-08 腾讯觅影发布，中肿为"人工智能医学影像联合实验室"**首批共建单位**；2019 团队发表上消化道癌内镜 AI 云诊断平台（GRAIDS，*Lancet Oncology*） | 中山大学官网 https://www.sysu.edu.cn/info/ ；36Kr 2017-08-03 https://m.36kr.com/ ；21财经 2017-08-04 |
| **浙大二院** | 院级 | **阿里达摩院** | **2026-05-26 正式签署战略合作协议**（整合 AI 技术/临床资源/医学专业） | https://view.inews.qq.com/ ；http://www.1111job.com/ |
| **浙江省肿瘤医院** | 院级 | **阿里达摩院** | **2025-06-25 全球首个胃癌影像筛查 AI 模型 DAMO GRAPE**（Nat Med, PMID 40555751） | 潮新闻 https://tidenews.com.cn/ |
| **中国医科大学附属盛京医院 · 放射科 Yu Shi** | 科室级但产出等同 | **阿里达摩院** | 肝脏恶性肿瘤 AI（Nat Med 2026, PMID 42618635）；PANDA 外部中心 | PubMed |
| **上海市胰腺疾病研究所（长海医院）· 陆建平/邵成伟** | 研究所级 | **阿里达摩院** | **PANDA 的牵头单位**（Nat Med 2023） | PubMed 37985692 |
| **浙江大学（校级）** | 校级 | **阿里巴巴集团** | 2025-07-14 共建**人工智能安全联合实验室**，首批 10 课题 | http://www.cs.zju.edu.cn/ |

**模式归纳（我的判断）**：
- **"一把手亲自署名 + 企业提供算力与算法 + 医院提供数据与临床验证"** 已经是中国头部三甲的标准姿势，且几乎总是与**院士评选周期**、**国家医学中心创建**、**公立医院高质量发展试点**这三条行政线绑定。
- **浙大一院是其中最"论文驱动"的一个**：别人先签约挂牌再出成果，浙大一院是**先出 Nature Medicine / Science，始终不挂牌**。这在合规上更轻，在署名分配上对医院更有利（不用受联合实验室的知识产权协议约束）。

---

## 8. 达摩院侧的"血统"（用户特别问的部分）

- **Ling Zhang（张灵）**，RADAR/PANDA/肝脏三篇的 AI 侧资深通讯：**浙江大学博士（2013）**，四川大学硕士；先后为 University of Iowa 博后 → **NIH visiting fellow** → **NVIDIA research scientist** → **PAII Inc.（平安美国研究院，Bethesda）staff scientist** → **Alibaba DAMO Academy USA senior staff algorithm engineer / Medical AI Lab 多癌筛查技术负责人**。
  - 个人主页 https://fabiozhang0722.github.io ｜ https://scholar.google.com/citations ｜ ITU AI for Good 讲者页 https://aiforgood.itu.int/speaker/
  - **他是浙大博士**——这条个人纽带，比任何一份合作协议都更能解释"为什么是浙大一院"。
- **Le Lu（吕乐）**，PANDA #30、iAorta #37 的达摩院负责人：**NIH Clinical Center → PAII Inc.（领导 Bethesda Research Lab）→ 达摩院全球医疗 AI 研发负责人 → 2025 年 6 月加入蚂蚁集团（Ant Healthcare），现任 Ant Group 医疗健康 AI Lab 负责人**；IEEE Fellow (2021)、AIMBE Fellow (2026)。
  - https://www.cs.jhu.edu/~lelu/ ｜ https://lelu007.github.io
  - **⚠️ 他不在 RADAR 作者名单里，也不在 2026 年肝脏那篇里。** 时间上完全吻合他 2025-06 离开达摩院。达摩院医疗 AI 的资深署名从"吕乐+张灵"变成了"张灵+闫轲(Ke Yan)"。这是一次可见的团队更替。
- **血统总结**：达摩院医疗影像团队的技术谱系是 **NIH Clinical Center → 平安 PAII（Bethesda）→ 阿里达摩院（纽约/华盛顿 + 杭州/湖畔）**，一条从美国政府实验室经中国保险巨头再到中国电商巨头的迁移路径；而它与浙大一院的接口，是一个**浙大博士（张灵）**加一个**浙大八年制/NIH 博后（章琦）**。两边都是浙大人。

---

## 9. 回到最初的问题：424,911 例是怎么拿到的

**可证实的结构性条件（每条都有来源）：**
1. 一家 **5000 床、7 院区、万人规模、连续 7 年国考 A++** 的综合医院（§3）。
2. 主导者是这家医院的 **党委书记（2018-12 起）→ 院长（2025-07 起）**，同时是肝胆胰外科学科带头人、省重点实验室主任、教育部国际合作联合实验室主任、**第十四届全国人大代表**（§1、§2）。
3. 放射科主任级人员（肖文波）在 iAorta 与 RADAR 中连续署名——**影像闸门是打开的，而且不是一次性的**（§5.5）。
4. 一张**至少 2022 年就已建成并跑通伦理的浙江省县域医院多中心网络**，在 Gut 2023 与 RADAR 2026 中人名逐一重合（§5.6）。
5. 合规路径是成熟的行业范式：**各中心 IRB 批准 + 免除知情同意 + 建模前去标识化 + 原始数据不公开**，法源是《涉及人的生命科学和医学研究伦理审查办法》（国卫科教发〔2023〕4号）（§6）。
6. 企业方有**浙江省实验室（湖畔实验室）**的身份外衣，且核心人物是浙大博士（§4.1、§8）。

**仍未解决、需要全文才能回答的：**
- RAD-CT 的**时间跨度**、**浙大一院本部占比**、**是否含 9 家基层医院的回溯数据**。
- **伦理批件号**与是否单一中心 IRB 覆盖全部中心。
- **数据是否出境**、境外作者的数据接触边界。
- 教育部胰腺疾病国际合作联合实验室的**批复年份**（多轮检索未果）。
- 浙大一院**年 CT 检查量**（无任何公开数字，不可估算）。

---

## 附：本次调查用到的可复现命令

```bash
# PANDA / RADAR 作者比对（本地 XML）
python3 -c "..."   # 见 §5.1

# 浙大一院 × 阿里 全部共同署名论文
curl -s -G "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi" \
  --data-urlencode "db=pubmed" --data-urlencode "retmode=json" --data-urlencode "retmax=60" \
  --data-urlencode 'term=Alibaba[Affiliation] AND "First Affiliated Hospital of Zhejiang"[Affiliation]'

# 省重点实验室署名首次出现年份（逐年上界计数）
for y in 2010 2012 2014 2015 2016 2017 2018 2019 2020; do
  curl -s "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&retmode=json&retmax=0&term=%22Zhejiang+Provincial+Key+Laboratory+of+Pancreatic+Disease%22%5BAffiliation%5D&datetype=pdat&mindate=1900&maxdate=$y"
done

# 中间那篇桥梁论文
curl -s "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=42618635&retmode=xml"

# PANDA 伦理声明全文
curl -sL -A "Mozilla/5.0" "https://pmc.ncbi.nlm.nih.gov/articles/PMC10719100/"
```

新增应归档的原始数据（建议由主 agent 写入 repo）：`/tmp/ia.xml`（iAorta PMID 40835970）、`/tmp/two.xml`（PMID 42618635 肝脏 Nat Med + 36113977 Gut）、`/tmp/panda.html`（PMC 全文快照）。