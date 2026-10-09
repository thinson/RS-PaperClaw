# Daily Reports

最近三天日报（最新在前）：

# [20261008](./202610/20261008.md)
## 📌 今日概况

今日共检索候选论文 10 篇；关键词+LLM 智能匹配遥感交叉论文 4 篇；最终纳入日报 4 篇。

今日论文聚焦遥感视觉定位、多模态配准与星上智能处理三大方向。无人机单张斜视影像在卫星地图中的绝对定位受到关注，跨视角地理定位与位姿估计成为关键。多模态遥感影像配准综述系统梳理了深度学习方法与挑战。星上AI方面，海洋异常检测与海事目标检测均强调在轨部署与数据缩减，自监督学习与嵌入式硬件成为实现手段，显示遥感AI正从地面算法向星载实时应用加速迁移。

## ✨ 今日亮点

- 无人机单张斜视影像实现卫星地图绝对视觉定位
- 多模态遥感影像配准综述梳理深度学习进展与挑战
- 星上AI海洋异常与海事目标检测完成在轨验证

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20261008] SatFix: Absolute Visual Localization of UAVs in Satellite Maps from a Single Oblique Image | Zeng Jiarui, Shi Kun, Vong Chiman, Zheng Zhedong | Department of Computer and Information Science, Faculty of Information Science and Computing, University of Macau, Macao SAR, China；Institute of Artificial Intelligence and Brain Sciences, University of Macau, Macao SAR, China | 提出SatFix方法，利用单张无人机斜视影像在卫星地图中实现绝对视觉定位与位姿估计。 | [#1463](https://github.com/thinson/RS-PaperClaw/issues/1463) |
| [20261008] Multimodal Remote Sensing Image Registration: A Comprehensive Review, Challenges and Prospects | Han Zhiqiang, Ye Yuanxin, Wu Qiuyun, Chen Jinhao, Zhu Bai, Hao Siyuan | the Faculty of Geosciences and Engineering, Southwest Jiaotong University；School of Software Engineering, Beijing Jiaotong University | 系统综述多模态遥感影像配准的深度学习方法，归纳特征与区域方法并展望未来挑战。 | [#1464](https://github.com/thinson/RS-PaperClaw/issues/1464) |
| [20261008] Onboard Marine Anomaly Detection on $Φ$sat-2: From Simulation-Based Development to In-Orbit Demonstration | Szywala Clotilde, Goudemant Thomas, Bellizzi Marjorie, Francesconi Benjamin, Girard Adrien | Institut de Recherche Technologique Saint Exupéry | 在Φsat-2卫星上实现海洋异常检测，从仿真开发到在轨演示验证自监督学习方案。 | [#1465](https://github.com/thinson/RS-PaperClaw/issues/1465) |
| [20261008] AI-Based On-Board Maritime Object Detection for Earth Observation Payload Data Reduction on Versal Embedded Hardware | Goudemant Thomas, Bobey Aurélien, Hlimi Omar, Bellizzi Marjorie | IRT Saint Exupéry | 面向地球观测载荷数据缩减，在Versal嵌入式硬件上实现基于AI的海事目标在轨检测。 | [#1466](https://github.com/thinson/RS-PaperClaw/issues/1466) |

## 🔎 观察

- 星上AI从算法验证走向在轨部署，自监督学习与嵌入式硬件结合成为降低下行数据量的关键路径。
- 跨视角地理定位与多模态配准均面临模态差异挑战，单图绝对定位和统一配准框架是当前研究热点。

---

Powered by OpenClaw🦞

---

# [20261007](./202610/20261007.md)
## 📌 今日概况

今日共检索候选论文 14 篇；关键词+LLM 智能匹配遥感交叉论文 9 篇；最终纳入日报 9 篇。

今日论文覆盖去雾、基础模型、无人机自主搜索与调度、点云地形监测、多模态数据集及水质预测等方向。研究趋势显示：脉冲神经网络与语义监督被引入遥感底层视觉与跨模态预训练；世界模型和LLM开始用于无人机任务规划与调度；多模态数据与无监督聚类推动地表过程与语义感知；进化架构搜索则用于水质参数反演，整体呈现多任务、跨模态与自主化倾向。

## ✨ 今日亮点

- 脉冲神经网络与阈值调制用于遥感图像去雾，探索低功耗底层视觉。
- SAR-EO基础模型引入解耦语义监督，提升跨模态掩码重建表示。
- 世界模型与LLM分别用于无人机目标搜索和调度，推动自主任务规划。

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20261007] EM-SNN: Efficiently Modulated Spiking Neural Network for Remote Sensing Image Dehazing | Shao Jie, Ma Jiaqi, Min Wenwen, Song Beihang, Chen Ning, Liu Youfa, Wan Jun | Zhongnan University of Economics and Law, Wuhan, China；Mohamed bin Zayed University of Artificial Intelligence, Abu Dhabi, UAE；Yunnan University, Kunming, China；National Institute of Natural Hazards, Ministry of Emergency Management of China, Beijing, China；Wuhan University, Wuhan, China | 提出EM-SNN，用阈值调制LIF和Spike Sobel调制实现高效遥感图像去雾。 | [#1453](https://github.com/thinson/RS-PaperClaw/issues/1453) |
| [20261007] SAREO-FM: Decoupled Semantic Supervision for SAR-EO Foundation Models | Do Jeonghyeok, Kim Munchurl | Korea Advanced Institute of Science and Technology (KAIST) | SAREO-FM通过语义查询解耦监督，增强SAR与光学基础模型的跨模态表示。 | [#1454](https://github.com/thinson/RS-PaperClaw/issues/1454) |
| [20261007] SearchWorld: Spatial Value-Grounded Imagination for UAV Object Search via World Models | Ji Yatai, Zhu Zhengqiu, Zhao Yong, Hu Yue, Yao Fanglong, Gao Chen, Zhu Pengfei, Yin Quanjun | National Key Laboratory of Digital Intelligent Modeling and Simulation, National；University of Defense Technology；College of Systems Engineering, National University of Defense Technology；Aerospace Information Research Institute, Chinese Academy of Sciences；BNRist, Tsinghua University；Southeast University | SearchWorld利用空间价值引导的世界模型想象，提升无人机目标搜索效率。 | [#1455](https://github.com/thinson/RS-PaperClaw/issues/1455) |
| [20261007] IVG-UAV: An Intelligent Voice-Guided UAV System for Autonomous Ripe Fruit Harvesting with Vision-Based Classification and Adaptive Path Planning | Dinh Trung Duong | School of Computing；SUNY Binghamton University | IVG-UAV集成语音引导、视觉分类与自适应路径规划，实现自主采摘成熟果实。 | [#1456](https://github.com/thinson/RS-PaperClaw/issues/1456) |
| [20261007] LLM-Enabled UAV Dispatch: A System-Level Survey and Taxonomy | Han Xiao, Quan Aoyang, Zhao Xiangyu, Kong Xiangjie, Shen Guojiang | School of Computer Science, Zhejiang University of Technology, China ( | 系统综述LLM赋能无人机调度，提出语义编排与调度范式的分类体系。 | [#1457](https://github.com/thinson/RS-PaperClaw/issues/1457) |
| [20261007] DeepTopoClustering: Unsupervised Derivation of Surface Process Taxonomy from 4D Point Clouds for Topographic Monitoring | Wang Jiapan, Hulskemper Daan, Letard Mathilde, Lindenbergh Roderik, Anders Katharina | Remote Sensing Applications, TUM School of Engineering and Design, Technical University of Munich；Department of Geoscience \& Remote Sensing, Delft University of Technology | DeepTopoClustering从4D点云无监督推导地表过程分类，用于地形监测。 | [#1458](https://github.com/thinson/RS-PaperClaw/issues/1458) |
| [20261007] Borrowed Eyes: Markerless Nano-UAV Flight with an Active Quadruped Observer | Alejandro Lorite Mora, Arapis Dimitrios, Faíña Andrés | Helix Lab and Novo Nordisk A/S, Denmark | 借眼方案让纳米无人机在无GNSS环境下由四足机器人主动观测定位飞行。 | [#1459](https://github.com/thinson/RS-PaperClaw/issues/1459) |
| [20261007] MultiFly: A Real-World Multimodal Aerial Dataset with Annotation-Efficient Label Transfer and Cross-Modal Semantic Consistency | Gross Markus, Greiner Andreas, Kim Taehyoung, Subbiah Sivasubiramaniam, Cotič Tomaž, Sai Bharadwaj Matha, Christoph Conrad, Dhaouadi Oussema, Zieher Simon, Surya Vijaya Kumar, Elger Gordon, Meeß Henri, Wysocki Olaf, Spannaus Paul, Cremers Daniel | Autonomous Aerial Systems, Fraunhofer Institute IVI；Computer Vision Group, Technical University of Munich；Computer Vision for Digital Twins, University of Cambridge；Institute of Innovative Mobility, Univ. of Applied Sciences Ingolstadt | MultiFly发布多模态航空数据集，支持标注高效迁移与跨模态语义一致性。 | [#1460](https://github.com/thinson/RS-PaperClaw/issues/1460) |
| [20261007] Evolutionary Architecture Search for Chlorophyll-$a$ Prediction in Lakes using Sentinel-2 | Komurcu Kursat, Petkevicius Linas | Vilnius University, Institute of Computer Science, Artificial Intelligence Methods Lab；IRISA, Universite Bretagne Sud；European Commission Joint Research Center；This research has received funding from the Research Council of Lithuania (LMTLT), agreement No S-ITP-25-3 | 用进化架构搜索基于Sentinel-2预测湖泊叶绿素a，优化多层感知机结构。 | [#1461](https://github.com/thinson/RS-PaperClaw/issues/1461) |

## 🔎 观察

- 脉冲神经网络与基础模型分别从低功耗和跨模态监督切入，反映遥感底层视觉与预训练并进。
- 无人机研究从单机感知转向世界模型、LLM调度与异构协同，自主任务规划成为热点。

---

Powered by OpenClaw🦞

---

# [20261006](./202610/20261006.md)
## 📌 今日概况

今日共检索候选论文 16 篇；关键词+LLM 智能匹配遥感交叉论文 5 篇；最终纳入日报 5 篇。

今日遥感AI研究呈现三条主线：一是跨域迁移与泛化边界，CETUS探索地球表征向土星SAR的迁移，剑桥工作则从空间依赖性出发重新审视样本独立性与泛化界；二是数据泄漏与评估可靠性，高光谱分类中patch重叠导致的泄漏被量化，提示现有精度可能被高估；三是面向实际难题的方法改进，RBMatch针对半监督建筑提取的类别不平衡提出双层重平衡，RSJEV则利用多模态大模型增强场景判别。整体看，社区对评估严谨性和跨域可靠性的关注明显上升。

## ✨ 今日亮点

- 跨域迁移从地球走向土星SAR，检验表征的普适边界
- 空间依赖与patch重叠被量化，数据泄漏问题受重视
- 半监督与多模态大模型分别应对类别不平衡和场景判别

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20261006] CETUS: How Far Do Representations Trained on Earth Transfer to Cassini SAR of Titan? | Lee Kevin | University of California at Los Angeles, Los Angeles, CA；NASA Jet Propulsion Laboratory, California Institute of Technology, Pasadena, CA | 评估地球预训练表征迁移至土星Cassini SAR的可行性，面向行星地形分类。 | [#1447](https://github.com/thinson/RS-PaperClaw/issues/1447) |
| [20261006] RBMatch: Dual-Level Class Rebalancing for Semi-Supervised Building Footprint Extraction | Akil Ahmad Taki, Shaikh Anowarul Fattah | Department of EEE, Bangladesh University of Engineering and Technology(BUET)；Department of EEE, University of Asia Pacific ( | 提出双层类别重平衡的半监督方法，缓解建筑足迹提取中的不平衡问题。 | [#1448](https://github.com/thinson/RS-PaperClaw/issues/1448) |
| [20261006] How Many Independent Samples Does a Satellite Image Contain? Generalization Bounds for Spatially Dependent Data | Young Robin | Department of Computer Science and Technology；University of Cambridge, UK | 针对空间依赖数据推导泛化界，讨论卫星图像有效独立样本数。 | [#1449](https://github.com/thinson/RS-PaperClaw/issues/1449) |
| [20261006] RSJEV: Discriminative Remote Sensing Scene Classification with Multimodal Large Language Models | Si Dongchen, Wang Di, Xu Mingzhen, Zhang Jing, Du Bo, Zhang Liangpei | School of Computer Science, Wuhan University, Wuhan, China (；State Key Laboratory of Information Engineering in Surveying, Mapping and Remote Sensing, Wuhan University, Wuhan, China ( | 利用多模态大语言模型进行遥感场景分类，强调判别性决策。 | [#1450](https://github.com/thinson/RS-PaperClaw/issues/1450) |
| [20261006] Data Leakage in Patch-Based Hyperspectral Image Classification: Quantifying the Impact of Spatial Overlap | Mohammed Q. Alkhatib | College of Engineering and IT, University of Dubai, Dubai, 14143, UAE | 量化patch空间重叠导致的数据泄漏，揭示高光谱分类评估偏差。 | [#1451](https://github.com/thinson/RS-PaperClaw/issues/1451) |

## 🔎 观察

- 多篇工作指向同一隐患：空间自相关使样本非独立，评估与泛化结论需重新校准。
- 跨域迁移与泄漏量化表明，遥感AI正从追求精度转向追问精度是否可信。

---

Powered by OpenClaw🦞

---
