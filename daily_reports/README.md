# Daily Reports

最近三天日报（最新在前）：

# [20260918](./202609/20260918.md)
## 📌 今日概况

今日共检索候选论文 6 篇；关键词+LLM 智能匹配遥感交叉论文 2 篇；最终纳入日报 1 篇。

今日候选论文聚焦无人机遥感影像中的重叠植物识别问题，提出将目标检测与几何感知聚类相结合的技术路线。该方法先通过目标检测定位植物个体，再利用几何信息引导K-Means聚类以区分相互重叠的植株，试图缓解密集植被场景下检测框重叠导致的个体混淆。整体来看，研究延续了遥感AI中检测与聚类融合的思路，强调几何先验在实例区分中的作用，面向农业与植被监测的精细化管理需求。

## ✨ 今日亮点

- 目标检测与几何感知聚类结合，应对无人机影像中植物重叠难题
- 利用几何信息引导K-Means，提升重叠植株的个体区分能力
- 面向农业植被精细监测，强调实例级识别而非仅计数

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260918] Combining Object Detection with Geometry-Aware Clustering to Distinguish Overlapping Plants in UAV Imagery | Ik Jae Lee, Hieu D. Nguyen, Meenar Mahbubur, Carlos Morrison Martinez, Connelly Cameron | Department of Mathematics, Rowan University；Department of Geography, Planning, and Sustainability, Rowan University；Department of Computer Science, Rowan University | 将目标检测与几何感知聚类结合，用K-Means区分无人机影像中相互重叠的植物个体。 | [#1315](https://github.com/thinson/RS-PaperClaw/issues/1315) |

## ⚠️ 未纳入日报的匹配论文

以下论文通过关键词/LLM 筛选，但在处理过程中失败未纳入日报。点击 arXiv 链接可查看原文。

| 标题 | arXiv | 失败原因 |
|------|-------|----------|
| AgenticSwarm: Semantic Perception and Adaptive Task Allocation for Heterogeneous Multi-UAV Missions | [2609.21716v1](https://arxiv.org/abs/2609.21716v1) | 质检未通过: 单位为空或无效 |


## 🔎 观察

- 检测加聚类的两阶段思路，适合处理密集植被中检测框难以分离的实例区分问题。
- 几何先验的引入表明，单纯依赖外观特征在重叠场景下仍有局限，结构信息值得重视。

---

Powered by OpenClaw🦞

---

# [20260917](./202609/20260917.md)
## 📌 今日概况

今日共检索候选论文 15 篇；关键词+LLM 智能匹配遥感交叉论文 7 篇；最终纳入日报 7 篇。

今日论文呈现遥感智能处理向多模态信号融合与任务导向设计演进的趋势。一方面，研究关注低信噪比条件下的语义特征传输与声学信号处理，强调信号层面的预处理与通信效率；另一方面，事件视觉、持久语义记忆与主动地理定位等方向推动无人机与卫星平台在动态环境中的感知鲁棒性。此外，时序InSAR与地表异常免疫监测等研究延续了对地观测中形变与变化检测的精细化需求，整体体现从数据驱动向任务与信号协同优化的转变。

## ✨ 今日亮点

- 信号中心与任务导向通信成为低信噪比遥感的新优化路径
- 事件视觉与持久语义记忆提升无人机动态感知鲁棒性
- 主动地理定位与时序InSAR推动跨视角与形变监测精细化

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260917] Signal-Centric Remote Sensing via Alternative Preprocessing and Acoustic Processing for ML-Driven Applications | Luna Logan, Jansen-Sánchez Sirio, Demirkiran Ilteris, Ghelarducci Leo | School of Computer Science, College of Computing, Georgia Institute of Technology, Atlanta, GA USA (；Embry-Riddle Aeronautical University | 提出以信号为中心的处理框架，结合替代预处理与声学方法提升低信噪比遥感ML应用性能。 | [#1307](https://github.com/thinson/RS-PaperClaw/issues/1307) |
| [20260917] Earth Surface Immune System for Rapid Monitoring of Unknown Anomalies | Li Jingtao, Zhu Qian, Wang Xinyu, Li Deren, Zhang Liangpei, Zhong Yanfei | State Key Laboratory of Information Engineering in Surveying, Mapping and Remote Sensing, Wuhan University；School of Remote Sensing and Information Engineering, Wuhan University | 借鉴免疫系统机制构建地表异常快速监测框架，实现未知异常的即时发现与响应。 | [#1308](https://github.com/thinson/RS-PaperClaw/issues/1308) |
| [20260917] Multi-Track Time-Series Burst-Overlap Interferometry for Resolving Horizontal Deformation in Earthquake-Cycle Studies | Li Xing, Gao Zhuang, Chen Han, Ma Zhangfeng, Chen Yangkang, Savvaidis Alexandros | Bureau of Economic Geology, Jackson School of Geosciences, University of Texas at Austin；Department of Earth and Space Sciences, Southern University of Science and Technology；State Key Laboratory of Earthquake Dynamics and Forecasting, Institute of Geology, China；Earth Observatory of Singapore, Nanyang Technological University, Singapore, 639798 | 利用多轨时序burst-overlap干涉测量，解析地震周期中的水平形变信号。 | [#1309](https://github.com/thinson/RS-PaperClaw/issues/1309) |
| [20260917] Task-Oriented Semantic Feature Transmission for Multi-Task Satellite Remote Sensing over Low-SNR Channels | Sun Shuoyuan, Wang Hongyu, Peng Mugen, Xu Wenjia | State Key Laboratory of Networking and Switching Technology；Beijing University of Posts and Telecommunications | 面向多任务卫星遥感，设计低信噪比信道下的语义特征传输与任务导向通信方案。 | [#1310](https://github.com/thinson/RS-PaperClaw/issues/1310) |
| [20260917] PointEvent: Rethinking Event-based Tiny Object Detection via Serialized Motion Evidence Accumulation | Wu Zongze, Jia Baofeng, Yan Weiqi, Zhang Jingyuan, Zang Yu, Chen Xiaoyu, Han Jing | State key Lab of Extreme Environment Optoelectronic Dynamic Testing Technology and Instrument, Nanjing University of；Jiangsu Key Lab of Visual Sensing and Intelligent Perception, Nanjing University of Science and Technology, China；Fujian Key Laboratory of Urban Intelligent Sensing and Computing, Xiamen University, China | 提出PointEvent方法，通过序列化运动证据积累改进事件相机微小目标检测。 | [#1311](https://github.com/thinson/RS-PaperClaw/issues/1311) |
| [20260917] Towards Active Cross-View Object Geo-Localization | Yao Shunyu, Zhang Xiaohan, Yang Zhuoran, Lai Haoqi, Ming Qi, Hu Xiaoxi, Shen Hui-Liang, Cao Si-Yuan | College of Information Science and Electronic Engineering；Zhejiang University, Hangzhou 310027, China；College of Computer Science；Beijing University of Technology, Beijing 100124, China；State Key Laboratory of Intelligent Green Vehicle and Mobility；Tsinghua University, Beijing 100084, China；Ningbo Global Innovation Center；Zhejiang University, Ningbo 315100, China；Jinhua Institute of Zhejiang University | 构建主动跨视角目标地理定位框架，融合多视角提示保持与轨迹引导策略初始化。 | [#1312](https://github.com/thinson/RS-PaperClaw/issues/1312) |
| [20260917] PerSeM: Persistent Semantic Memory for Long-Horizon Open-Vocabulary UAV Mapping | Saurbh Singh Jamwal, Ramakrishnan Ganesh | Department of Computer Science and Engineering；Indian Institute of Technology Bombay | 提出持久语义记忆机制，支持长时程开放词汇无人机建图中的时序一致性。 | [#1313](https://github.com/thinson/RS-PaperClaw/issues/1313) |

## 🔎 观察

- 低信噪比与任务导向通信的交叉研究增多，反映遥感系统正从单纯成像向语义高效传输演进。
- 事件视觉与持久记忆机制在无人机场景中互补，有望缓解动态环境下的目标丢失与语义漂移问题。

---

Powered by OpenClaw🦞

---

# [20260916](./202609/20260916.md)
## 📌 今日概况

今日共检索候选论文 21 篇；关键词+LLM 智能匹配遥感交叉论文 7 篇；最终纳入日报 6 篇。

今日研究覆盖高光谱分类、叶绿素反演、ISAC-SAR、星上烟火检测、无人机广域感知与跨视角地理定位。趋势上，可解释AI与降维结合用于高光谱分类，符号回归探索叶绿素反演所需波段，轻量化弱监督模型推动星上实时推理，多视角专家与视觉语言重排提升跨视角定位鲁棒性。整体呈现模型轻量化、任务专用化与多模态融合并进的特点。

## ✨ 今日亮点

- 可解释AI驱动高光谱降维，兼顾分类精度与特征可解释性
- 符号回归量化叶绿素反演所需高光谱信息，挑战全波段依赖
- 轻量弱监督模型实现星上烟火检测，推动在轨实时响应

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260916] Dimensionality reduction for AI based hyperspectral image classification based on XAI | Zeljković Vladimir, Stojanović Branka, Ganster Harald, Nešković Aleksandar | University of Belgrade School of Electrical Engineering；JOANNEUM RESEARCH Forschungsgesellschaft mbH；This study, as part of a large research initiative [9], uti-；This research addresses the challenge of limited mate- lizes AI for different materials classification based on hyrial recycling in wood recycling processes by leveraging | 基于可解释AI的高光谱降维方法，用于木材回收材料分类，缓解标注数据有限问题。 | [#1300](https://github.com/thinson/RS-PaperClaw/issues/1300) |
| [20260916] How Much Hyperspectral Information Does Chlorophyll Retrieval Really Need? | Hammoud Abed, Sun Xuerong, Champenois Bianca, Robert J.W. Brewin | Civil and Environmental Engineering, Princeton University, Princeton, New Jersey 08540, USA；Centre for Geography and Environmental Science, Department of Earth and Environmental Sciences；Faculty of Environment, Science and Economy, University of Exeter, Exeter, Cornwall, UK；High Meadows Environmental Institute, Princeton University, Princeton, New Jersey 08540, USA | 利用符号回归探究叶绿素反演真正需要多少高光谱信息，面向PACE等任务。 | [#1301](https://github.com/thinson/RS-PaperClaw/issues/1301) |
| [20260916] Imaging-Communication Trade-off in VLEO ISAC-SAR Using CP-OFDM | Lee In-Hyeok, Han Kawon | Ulsan National Institute of Science and Technology, Ulsan, Korea | 研究VLEO下ISAC-SAR采用CP-OFDM的成像与通信权衡关系。 | [#1302](https://github.com/thinson/RS-PaperClaw/issues/1302) |
| [20260916] WISE: A Lightweight, Weakly-Supervised Model for Onboard Fire Smoke Detection and Localization | Lu Sha, Sun Yu, Zhao Liang, Liu Jixue, Liu Lin, Li Jiuyong, A. K. Qin, Mousist Alejandro, Peters Stefan | Adelaide University, Adelaide, SA 5000, Australia；Swinburne University of Technology, Hawthorn, VIC 3122, Australia | 提出轻量弱监督WISE模型，实现星上火灾烟雾检测与定位。 | [#1303](https://github.com/thinson/RS-PaperClaw/issues/1303) |
| [20260916] Understanding Dynamic Scenes at Gigapixel Scale: Wide-Area Spatio-Temporal Perception from UAVs | Zhu Yuhang, Zhu Meiyi, Dang Yunkai, Li Zhangnan, Wang Yuxuan, Li Wenbin, Pan Hongbing | Nanjing University | 面向无人机十亿像素级广域动态场景，构建时空感知数据集与方法。 | [#1304](https://github.com/thinson/RS-PaperClaw/issues/1304) |
| [20260916] Multi-View Mixture-of-Experts with Vision-Language Reranking for Cross-View Object Geo-Localization | Fan Xuyu, Ming Qi, Han Zhu, Wang Liuqian, Cao Si-Yuan, Zhang Xiaohan, Zhao Xudong, Zhao Mingjing, Zhang Yuhan | College of Computer Science, Beijing University of Technology；Zhengzhou University；Zhejiang University；Beijing Institute of Technology；Beijing Electronic Science and Technology Institute；Intelligent Science & Technology Academy of CASIC；jing University of Technology | 多视角专家混合结合视觉语言重排，提升跨视角目标地理定位性能。 | [#1305](https://github.com/thinson/RS-PaperClaw/issues/1305) |

## ⚠️ 未纳入日报的匹配论文

以下论文通过关键词/LLM 筛选，但在处理过程中失败未纳入日报。点击 arXiv 链接可查看原文。

| 标题 | arXiv | 失败原因 |
|------|-------|----------|
| PDA++: Field-Aligned Planning and Scene-Adaptive Insertion in Remote Sensing | [2609.18329v2](https://arxiv.org/abs/2609.18329v2) | 质检未通过: 单位为空或无效 |


## 🔎 观察

- 高光谱与叶绿素研究共同指向信息冗余问题，降维与波段选择成为提升效率的关键路径。
- 星上推理与无人机广域感知强调轻量化与弱监督，反映遥感AI向边缘部署加速迁移。

---

Powered by OpenClaw🦞

---
