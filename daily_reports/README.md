# Daily Reports

最近三天日报（最新在前）：

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

# [20261120](./202611/20261120.md)
## 📌 今日概况

今日共检索候选论文 15 篇；关键词+LLM 智能匹配遥感交叉论文 7 篇；最终纳入日报 7 篇。

今日研究呈现多模态融合与评测基准并进态势。WINSO构建大规模风机与光伏数据集，FM4SAR-Bench推动SAR基础模型公平评测，SAM-3适配分析揭示参数高效微调特性。RemoteEvolver探索智能体工具进化，机载高光谱异常检测面向野外搜救，物理驱动SAR-光学融合去云与无人机风机叶片三维重建体现方法创新。

## ✨ 今日亮点

- WINSO发布超高清遥感数据集，支撑风机检测与光伏分割。
- FM4SAR-Bench建立SAR基础模型分层公平评测框架。
- RemoteEvolver以智能体工具进化扩展对地观测能力。

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20261120] WINSO: A Large-Size Very-High-Resolution Remote Sensing Dataset for Wind Turbine Detection and Solar Panel Segmentation | Wang Di, Li Ke, Li Zhaokun, Ni Weiping, Wu Junzheng, Liu Yahu, Wang Quan, Gao Xinbo | Xidian University；Northwest Institute of Nuclear Technology；Northwestern Polytechnical University | 构建超高清遥感数据集WINSO，面向风机检测与光伏板分割任务。 | [#1762](https://github.com/thinson/RS-PaperClaw/issues/1762) |
| [20261120] FM4SAR-Bench 1.0: Towards A Fair Benchmark for Evaluating Foundation Models for SAR Image Interpretation | Chen Mingyao, Liu Yongxiang, Liu Tianpeng, Yong Yuchen, Zhou Jie, Yang Zhenhao, Huang Pinyi, Li Weijie, Zhang Jiehua, Peng Bowen, Peng Zhimao, Zhang Zhiyuan, Liu Li | College of Electronic Science and Technology, National University of Defense Technology (NUDT), Changsha, China | 提出FM4SAR-Bench基准，分层公平评测SAR图像解译基础模型。 | [#1763](https://github.com/thinson/RS-PaperClaw/issues/1763) |
| [20261120] How Does SAM-3 Adapt? Capacity, Update Geometry, and Domain Transfer | Kazakov Allan, Javat Abdurrahman, Cakir Duygu | Bahcesehir University, Istanbul, Turkey | 分析SAM-3容量、更新几何与域迁移，揭示参数高效微调特性。 | [#1764](https://github.com/thinson/RS-PaperClaw/issues/1764) |
| [20261120] RemoteEvolver: Expanding Earth Observation Capabilities through Agent Harness Evolution | Xu Shengxiang, Yao Liang, Chen Shuyi, Wang Yishu, Di Shimin, Liu Fan, Yao Bishun, Guo Hanghui, Liu Xinyu, Liang Chengye, Luo Yuyu, Zhang Min-Ling | Southeast University；Hohai University；The Hong Kong University of Science and Technology (Guangzhou) | 提出RemoteEvolver，通过智能体工具进化扩展对地观测工作流。 | [#1765](https://github.com/thinson/RS-PaperClaw/issues/1765) |
| [20261120] Real-Time On-Drone Hyperspectral Anomaly Detection for Wilderness Search and Rescue | Liu Jacqueline, Kyere Gyabaah, Liu Chengyan, Chiu Kenneth, Marie Lynn, Church, Gleason Sean, Boubin Jayson | School of Computing, Binghamton University, Binghamton, NY USA (；the Mathematics and Computer Science Department, Hampden-Sydney College, Hampden-Sydney, VA USA ( | 实现无人机机载高光谱实时异常检测，服务野外搜救任务。 | [#1766](https://github.com/thinson/RS-PaperClaw/issues/1766) |
| [20261120] PIU-CR: Physics-Informed Deep Unfolding with SAR-Optical Image Fusion for Cloud Removal | Fan Gengque, Xu Han, Li Junxi, Zhang Hao, Liu Guangcan, Ma Jiayi | School of Automation, Southeast University, Nanjing, China；School of Instrument Science and Engineering, Southeast University, Nanjing, China；Electronic Information School, Wuhan University, Wuhan, China；School of Robotics, Wuhan University, Wuhan, China | 提出物理驱动深度展开与SAR-光学融合去云方法PIU-CR。 | [#1767](https://github.com/thinson/RS-PaperClaw/issues/1767) |
| [20261120] BladeR: Scalable, Shape-Guided 3D Reconstruction of Wind Turbine Blades from UAV Imagery | Sterckx Jonathan, Vlaminck Michiel, Luong Hiep | IPI-URC-imec, Ghent University, Sint-Pietersnieuwstraat 41, Ghent, Belgium；A scalable preprocessing pipeline that uses automated segmentation and blade-centered tiling to | 提出BladeR，从无人机影像可扩展重建风机叶片三维形状。 | [#1768](https://github.com/thinson/RS-PaperClaw/issues/1768) |

## 🔎 观察

- 数据集与基准建设并行推进，反映遥感AI从模型创新转向可复现评测。
- 物理模型与智能体方法同时受关注，表明领域知识融合成为新趋势。

---

Powered by OpenClaw🦞

<!-- rs-pipeline: {"date": "20261120", "source": "oai", "checked_at": "2026-11-23T05:40:30+00:00", "source_complete": true, "candidate_count": 15, "paper_count": 7} -->

---
