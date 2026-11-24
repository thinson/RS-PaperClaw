# Daily Reports

最近三天日报（最新在前）：

# [20261123](./202611/20261123.md)
## 📌 今日概况

今日共检索候选论文 20 篇；关键词+LLM 智能匹配遥感交叉论文 14 篇；最终纳入日报 14 篇。

今日论文覆盖高光谱分割与分类、遥感基础模型鲁棒性、跨视角定位、多模态检索与变化检测等方向。高光谱领域出现免训练开放词汇分割与不确定性感知融合方法；标签噪声与地理偏差受到关注，涉及基础模型评测和作物分类。光学计算与Mamba架构被引入卫星分类和洪水检测，UAV基准数据集与视频文本检索任务进一步丰富。整体趋势显示，研究更重视数据缺陷下的可靠性、多源信息融合以及轻量化部署。

## ✨ 今日亮点

- 高光谱分割提出免训练谱路由，降低开放词汇迁移成本。
- 基础模型评测引入校准标签错误，关注噪声下鲁棒性。
- Mamba与光学网络拓展遥感分类和变化检测范式。

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20261123] SpectralRoute: Adaptive Spectral Routing for Training-Free Open-Vocabulary Hyperspectral Segmentation | Li Qingmei, Fan Xiaoya, Zheng Juepeng, Huang Jianxi, Fu Haohuan | Tsinghua Shenzhen International Graduate School；Southwest University；Sun Yat-sen University；National Supercomputing Center in Shenzhen；Southwest Jiaotong University；China Agricultural University；Guangxi University of Science and Technology | 提出免训练谱路由框架，实现开放词汇高光谱分割。 | [#1776](https://github.com/thinson/RS-PaperClaw/issues/1776) |
| [20261123] KGLP-Net: Kalman-Reliable Global--Local Learning With Group Fisher Pruning for Hyperspectral Image Classification | Deng Wenshuai, Xie Wen, Abdel Hamid Soliman, Zhao Qianzheng | School of Communications and Information Engineering, Xi'an University of Posts and Telecommunications, Xi'an, China (；School of Digital, Technology, Innovation, and Business, University of Staffordshire, Stoke-on-Trent ST4 2 DE, U.K. ( | 结合卡尔曼可靠融合与组Fisher剪枝进行高光谱分类。 | [#1777](https://github.com/thinson/RS-PaperClaw/issues/1777) |
| [20261123] Designing Incoherent Multispectral Diffractive Optical Networks for Satellite Image Classification | Yang Xilin, Md Sadman Sakib Rahman, Lee Ryan, Ozcan Aydogan | Electrical and Computer Engineering Department, University of California, Los Angeles, CA；Bioengineering Department, University of California, Los Angeles, CA, 90095, USA；California NanoSystems Institute (CNSI), University of California, Los Angeles, CA, 90095 | 设计非相干多光谱衍射光学网络用于卫星图像分类。 | [#1778](https://github.com/thinson/RS-PaperClaw/issues/1778) |
| [20261123] Benchmarking Geospatial Foundation Models under Calibrated Label Errors | Mollah Md Saif, Rahman Showrin, Majumder Anindya, Rahman Sowad, Md. Golam Rabiul Alam | Department of Computer Science and Engineering, BRAC University, Dhaka, Bangladesh | 在校准标签错误下系统评测地理空间基础模型。 | [#1779](https://github.com/thinson/RS-PaperClaw/issues/1779) |
| [20261123] OCCA-Seg: Object and Channel Context Aggregation for Semantic Segmentation of Remote Sensing Images | Yang Gang, Chen Si, Zhou Quan, Li Jiangchuan | Beijing Key Laboratory of Urban Spatial Intelligent Sensing and Digital Governance, Beijing Institute of Survey and Mapping, Beijing, China ( | 聚合对象与通道上下文提升遥感图像语义分割。 | [#1780](https://github.com/thinson/RS-PaperClaw/issues/1780) |
| [20261123] RigidAnchor: Cross-View Geo-Localization for UAV via Iterative Planar Rigid Alignment | Wang Bo, Zhu Dekang, Li Jian, Meng Zhipeng, Wang Bo, Hu Dewen | National Innovation Institute of Defense Technology；College of Intelligence Science and Technology, National University of Defense Technology；School of Future Technology, National University of Defense Technology | 通过迭代平面刚性对齐实现UAV跨视角地理定位。 | [#1781](https://github.com/thinson/RS-PaperClaw/issues/1781) |
| [20261123] AirVT-15k: A Query-Diverse UAV Video-Text Dataset and Query-Adaptive Evidence Alignment Network for Retrieval | Chen Xi, Chen Xu, Jia Xiangyang, Gan Ting, Zhang Xu, Wei Shuquan | 原文作者栏未列出单位 | 构建查询多样UAV视频文本数据集并提出自适应对齐检索网络。 | [#1782](https://github.com/thinson/RS-PaperClaw/issues/1782) |
| [20261123] Cross-calibration of Hera/HyperScout-H with MRO/CRISM and MEx/OMEGA based on Mars observations | Farina A., Popescu M., Lazzarin M., J. de León, Prodan G., B. A. Dumitru, F. La Forgia, Poggiali G., Küppers M., Kovács G., B. V. Nagy, Grieger B., Barnouin O., Tatsumi E., Karatekin Ö., Michel P. | Dipartimento di Fisica e Astronomia, Padova University；Institute of Space Science – INFLPR Subsidiary；University of Craiova；Instituto de Astrofísica de Canarias；Department of Astrophysics, University of La Laguna；ESA, European Space Astronomy Centre (ESAC)；Department of Mechatronics, Optics and Engineering Informatics, Budapest University of Technology and Economics；Space Exploration Sector, Johns Hopkins University Applied Physics Laboratory；Royal Belgian Institute for Space Aeronomy；Université Côte d'Azur, Observatoire de la Côte d'Azur, CNRS, Laboratoire Lagrange | 基于火星观测交叉校准Hera/HyperScout-H与CRISM、OMEGA。 | [#1783](https://github.com/thinson/RS-PaperClaw/issues/1783) |
| [20261123] Field-Level Crop Classification via Similarity-Induced Supervision from Imperfect Labels | Raul Lomonte Figueiredo, João Rebouças Dorea, Dário Augusto Borges Oliveira | Animal Sciences Department, University of Wisconsin-Madison | 利用不完美标签的相似性监督进行田块级作物分类。 | [#1784](https://github.com/thinson/RS-PaperClaw/issues/1784) |
| [20261123] Seeing Is Locating: Spatial Awareness and Geographic Bias in Decision Language Models | Wongso Wilson, Hada Melino Muhammad, Lin Xiachong, Xue Hao, Flora D. Salim | University of New South Wales, Sydney, NSW, Australia；Hong Kong University of Science and Technology (Guangzhou), Guangzhou, China | 构建多模态基准揭示决策语言模型的空间意识与地理偏差。 | [#1785](https://github.com/thinson/RS-PaperClaw/issues/1785) |
| [20261123] Sequential Monitoring of Image Streams Using Energy Statistics | Bhuniya Shreetama, De Sourav, Roy Anik, Partha Sarathi Mukherjee | Indian Statistical Institute, Kolkata；Emory University, Atlanta, USA | 使用能量统计对图像流进行序贯监控与边界检测。 | [#1786](https://github.com/thinson/RS-PaperClaw/issues/1786) |
| [20261123] A High-Resolution UAV Benchmark Dataset and Baseline Evaluation for Teak Crown Segmentation in Western Ghats Tropical Forests | Anand S Sahadevan, Arya Sunita, Anup Kumar Das, Bimal Kumar Bhattacharya, S Manthira Moorthi | Space Applications Centre | 发布高分辨率UAV柚木冠层分割基准数据集与基线评估。 | [#1787](https://github.com/thinson/RS-PaperClaw/issues/1787) |
| [20261123] SIAMBA: A Pseudo-Siamese Mamba-based Deep Learning Network for Multimodal Flood Change Detection | Muhammad Fasih Ishfaq, Weikmann Giulio, Bruzzone Lorenzo | Department of Information Engineering and Computer Science, University of Trento, Via Sommarive, 5, I-38123 Trento, Italy | 提出伪孪生Mamba网络用于多模态洪水变化检测。 | [#1788](https://github.com/thinson/RS-PaperClaw/issues/1788) |
| [20261123] SRCWDNet: Semantic-Relational Cross-Window Dual-Graph Network for Multi-Label Remote Sensing Scene Classification | Amir Fareeha | Department of Computer Science, National University of Modern Languages, Islamabad, Pakistan ( | 构建语义关系跨窗口双图网络进行多标签场景分类。 | [#1789](https://github.com/thinson/RS-PaperClaw/issues/1789) |

## 🔎 观察

- 免训练与标签噪声鲁棒性成为遥感模型落地前的关键评估维度。
- 光学计算和状态空间模型开始进入遥感分类与变化检测任务。

---

Powered by OpenClaw🦞

<!-- rs-pipeline: {"date": "20261123", "source": "oai", "checked_at": "2026-11-24T15:11:02+00:00", "source_complete": true, "candidate_count": 20, "paper_count": 14} -->

---

# [20261122](./202611/20261122.md)
## 📌 今日概况

今日共检索候选论文 6 篇；关键词+LLM 智能匹配遥感交叉论文 2 篇；最终纳入日报 2 篇。

今日研究聚焦于地理定位与地理嵌入的精细化建模。一方面，针对无人机跨视角定位，提出基于神经场的连续位姿推断方法，突破离散匹配局限；另一方面，借鉴地图投影中的Tissot指示图形概念，系统刻画学习型地理嵌入的局部畸变与各向异性。两项工作均强调对空间连续性与几何保真度的关注，反映出遥感AI正从粗粒度匹配向连续、可解释的空间表示演进。

## ✨ 今日亮点

- ContinuLoc利用神经场实现无人机连续位姿推断，提升跨视角定位精度。
- 提出Tissot指示图形分析地理嵌入局部畸变，揭示各向异性特征。
- 两项工作共同关注空间连续表示与几何保真度，推动定位可解释性。

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20261122] ContinuLoc: Continuous Pose Inference over Neural Fields for UAV Geo-Localization | Zhou Weikun, Lin Jinliang, Zang Yu, Xie Lin, Fu Haiqing, Ao Sheng, Yu Shangshu, Luo Zhiming, Wang Cheng | Fujian Key Laboratory of Urban Intelligent Sensing and Computing；Xiamen University, Xiamen, China；Key Laboratory of Multimedia Trusted Perception and Efficient Computing；Ministry of Education of China, Xiamen University, Xiamen, China；The Belt and Road Research Institute, Xiamen University, Xiamen, China；School of Computer Science and Engineering, Northeastern University, Shenyang 110819, China | 提出ContinuLoc，基于神经场在语义特征空间实现无人机连续位姿推断，用于跨视角地理定位。 | [#1773](https://github.com/thinson/RS-PaperClaw/issues/1773) |
| [20261122] Tissot indicatrix for location encoders: Characterizing local distortion in learned geographic embeddings | Cao Guofeng, Mai Gengchen | aDepartment of Geography, University of Colorado Boulder, Boulder, CO, USA; bDepartment of Geography and the Environment, University of Texas at Austin, Austin, TX, USA | 将Tissot指示图形引入学习型地理嵌入分析，量化位置编码器的局部畸变与各向异性。 | [#1774](https://github.com/thinson/RS-PaperClaw/issues/1774) |

## 🔎 观察

- 连续位姿推断与嵌入畸变分析均指向对空间表示几何性质的精细刻画，或成新趋势。
- 地理嵌入的可解释性评估尚处起步，Tissot类工具为编码器设计提供几何诊断视角。

---

Powered by OpenClaw🦞

<!-- rs-pipeline: {"date": "20261122", "source": "api", "checked_at": "2026-11-24T04:33:29+00:00", "source_complete": true, "candidate_count": 6, "paper_count": 2} -->

---

# [20261121](./202611/20261121.md)
## 📌 今日概况

今日共检索候选论文 7 篇；关键词+LLM 智能匹配遥感交叉论文 2 篇；最终纳入日报 2 篇。

今日论文聚焦遥感视觉任务中的结构引导与质量感知。一篇面向无人机RGB-T微小行人检测，引入模态质量评估引导跨模态协同优化，以应对模态退化问题；另一篇利用中心线先验进行多类路面分割，将中心线特征与概率作为条件，结合分支结构处理规则路段、交叉口与立交，并估计双侧宽度。两篇均强调先验或质量信息对下游任务的引导作用，体现从单纯融合向条件化、可解释建模的转变。

## ✨ 今日亮点

- 模态质量引导协同优化用于无人机RGB-T微小行人检测
- 中心线先验条件化多类路面分割，分支处理交叉口与立交
- 两篇均以结构化先验或质量评估引导遥感视觉下游任务

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20261121] MQCODet: Modality Quality-Guided Collaborative Optimization for UAV-Based RGB-T Tiny Pedestrian Detection | Li Hui, Ma Jianbo, Luo Hui, Qi Guanglin, Wang Zhixing, Zuo Haorui, Zhang Jianlin | State Key Laboratory of Optical Field Manipulation Science and Technology, Institute of；Optics and Electronics, Chinese Academy of Sciences, Chengdu 610209, China；School of Electronic, Electrical and Communication Engineering, University of Chinese；Academy of Sciences, Beijing 100049, China | 提出MQCODet，利用模态质量评估引导RGB-T跨模态协同优化，提升无人机微小行人检测鲁棒性。 | [#1770](https://github.com/thinson/RS-PaperClaw/issues/1770) |
| [20261121] Centerline-Guided Multi-Class Road Surface Segmentation | Ouyang Xu, Gan Lin, Ma Di, Chen Sonnie, Boddhu Sanjay | Centerline-Guided Multi-Class Road Surface Segmentation；centerline features and probabilities condition regular, intersection；segmentation with our centerline-guided regular, intersection, and overpass branches, two-sided width estimation, and；centerline features and soft probabilities guide downstream；the regular branch, coupling transverse extent with centerline guidance instead of treating width as an independent | 提出中心线引导的多类路面分割方法，用中心线特征与概率条件化分支，并估计道路双侧宽度。 | [#1771](https://github.com/thinson/RS-PaperClaw/issues/1771) |

## 🔎 观察

- 两篇工作均将辅助信息作为条件引导主任务，反映遥感视觉从端到端融合转向结构化先验建模。
- 模态质量与中心线先验分别针对退化与拓扑难题，说明任务特定先验仍是提升鲁棒性的有效途径。

---

Powered by OpenClaw🦞

<!-- rs-pipeline: {"date": "20261121", "source": "api", "checked_at": "2026-11-24T04:30:33+00:00", "source_complete": true, "candidate_count": 7, "paper_count": 2} -->

---
