# Daily Reports

最近三天日报（最新在前）：

# [20261124](./202611/20261124.md)
## 📌 今日概况

今日共检索候选论文 18 篇；关键词+LLM 智能匹配遥感交叉论文 8 篇；最终纳入日报 8 篇。

今日研究聚焦视觉语言模型与遥感任务的深度结合，涵盖建筑损毁评估、灾害时序定位与开放词汇分割，强调实例自适应与多粒度监督。同时，全色锐化领域出现基础重构与测试时参数选择新思路，超分辨助力小目标检测。零样本云分割能力边界得到系统评估，遥感与机器学习结合拓展至浸出金属危害制图。整体呈现从静态语义向动态自适应、从封闭类别向开放词汇演进的趋势。

## ✨ 今日亮点

- 视觉语言对齐从静态语义转向实例自适应，提升建筑损毁评估精细化水平。
- 全色锐化研究反思基础设定，并探索测试时实例级参数选择策略。
- 零样本开放词汇云分割能力与局限获系统评估，推动可靠应用边界认知。

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20261124] Beyond Static Semantics: Instance-Adaptive Vision-Language Alignment for Building Damage Assessment | Yin Hang, Li Jiepan, Chen Hongruixuan, Yang Guangyi, He Wei | School of Electronic Information, Wuhan University；LIESMARS, Wuhan University；University of Tokyo | 提出实例自适应视觉语言对齐方法，突破静态语义限制，提升双时相建筑损毁评估精度。 | [#1791](https://github.com/thinson/RS-PaperClaw/issues/1791) |
| [20261124] Change the Base, Change the Game: Rethinking Pan-sharpening | Do Jeonghyeok, Youk Geunhyuk, Kim Munchurl | KAIST | 重新审视全色锐化的基础设定，提出改变基座以革新融合性能的研究视角。 | [#1792](https://github.com/thinson/RS-PaperClaw/issues/1792) |
| [20261124] Beyond Before-and-After Images: Evaluating Temporal Grounding in a Lightweight VLM for Disaster Assessment | Garg Shubh, Arora Pratham, Ghosh Debabrata | Thapar Institute of Engineering \& Technology | 评估轻量视觉语言模型在灾害评估中的时序定位能力，超越简单前后图像对比。 | [#1793](https://github.com/thinson/RS-PaperClaw/issues/1793) |
| [20261124] Adaptive and Detection-Aware Super-Resolution for Small Object Detection | Luncanu Cezica-Elena, Spînu Stelian | the Faculty of Information Systems and Cyber Security, Military Technical Academy “Ferdinand I”, Bucharest, Romania ( | 设计自适应且检测感知的超分辨率方法，针对小目标检测提升特征表达。 | [#1794](https://github.com/thinson/RS-PaperClaw/issues/1794) |
| [20261124] Which Parameters to Update? An Instance-Specific Adaptation Framework for Real-World Pansharpening | Xiao Jin-Liang, Deng Liang-Jian, Zhang Yu-Xuan, Meng Hua, Zhou Zhengchun | Southwest Jiaotong University, Chengdu, China；University of Electronic Science and Technology of China, Chengdu, China | 面向真实全色锐化提出实例特定参数选择框架，实现测试时自适应更新。 | [#1795](https://github.com/thinson/RS-PaperClaw/issues/1795) |
| [20261124] An Integrated Remote Sensing and Machine Learning Framework for Mapping Hazard Associated with Leached Metals | Karim Salman, Nojabaei Bahareh, Foroutan Hosein | Department of Mining & Minerals Engineering, Virginia Tech, Blacksburg, VA, USA；Department of Civil & Environmental Engineering, Virginia Tech, Blacksburg, VA, USA | 集成遥感与机器学习框架，用于浸出金属相关危害的制图与监测。 | [#1796](https://github.com/thinson/RS-PaperClaw/issues/1796) |
| [20261124] HS-OVSeg: Multi-Granularity Open-Vocabulary Semantic Segmentation in Remote Sensing via Heterogeneous Supervision | Huang Wei, Liu Chenying, Kang Xudong, Xiao Xiang Zhu | Technical University of Munich (TUM), Germany；Hunan University, China；School Playground | 利用异构监督实现遥感多粒度开放词汇语义分割，生成伪标签辅助学习。 | [#1797](https://github.com/thinson/RS-PaperClaw/issues/1797) |
| [20261124] On the Capabilities and Limitations of Zero-Shot Open-Vocabulary Cloud Segmentation | Sosa Jose, Gillet Thomas, Sleimi Rim, Abello Albert | Hydrosat | 系统评估零样本开放词汇云分割的能力与局限，揭示视觉语言模型适用边界。 | [#1798](https://github.com/thinson/RS-PaperClaw/issues/1798) |

## 🔎 观察

- 视觉语言模型在遥感中正从通用对齐走向实例级自适应，损毁评估与灾害定位成为验证新范式的重要场景。
- 全色锐化研究同时出现基础重构与测试时自适应两条路径，反映对真实场景泛化与部署灵活性的双重追求。

---

Powered by OpenClaw🦞

<!-- rs-pipeline: {"date": "20261124", "source": "oai", "checked_at": "2026-11-25T14:50:43+00:00", "source_complete": true, "candidate_count": 18, "paper_count": 8} -->

---

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
