# Daily Reports

最近三天日报（最新在前）：

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

# [20261119](./202611/20261119.md)
## 📌 今日概况

今日共检索候选论文 19 篇；关键词+LLM 智能匹配遥感交叉论文 6 篇；最终纳入日报 5 篇。

今日研究覆盖极化SAR分解、多模态树种分类、红外小目标检测、语言引导路径生成与SAR多模态持续学习。趋势上，传统极化分解方法被重新审视，深度学习继续向多模态融合与结构先验设计深入；同时，面向遥感视觉语言模型和持续学习的研究开始关注零样本迁移与灾难性遗忘问题，验证机制与知识蒸馏成为提升可靠性的关键手段。

## ✨ 今日亮点

- 极化SAR分解方法再审视，Cloude/van Zyl分解适配全极化数据。
- 多模态CNN与结构掩码Transformer融合用于亚像元树种制图。
- SAR多模态大模型持续学习引入历史在线策略蒸馏。

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20261119] A version of the Cloude/van Zyl decomposition for full/quad pol synthetic aperture radar data | Allan Aasbjerg Nielsen, Paul Jacques Connetable, Skriver Henning, Conradsen Knut | bDTU Space -- National Space Institute, Building 348；Technical University of Denmark, DK-2800 Lyngby, Denmark | 提出适用于全/四极化SAR的Cloude/van Zyl分解版本，用于散射机制与熵分析。 | [#1756](https://github.com/thinson/RS-PaperClaw/issues/1756) |
| [20261119] Fusing Multimodal CNN Features with Structurally-Masked Transformers for Hierarchical Sub-Pixel Tree Species Mapping | Ferrari Mattia, Bruzzone Lorenzo | Department of Information Engineering and Computer Science, University of Trento, Trento, Italy ( | 融合多模态CNN特征与结构掩码Transformer，实现分层亚像元树种分类。 | [#1757](https://github.com/thinson/RS-PaperClaw/issues/1757) |
| [20261119] Verifying Before Enhancing: Target Evidence Chain Verification for Infrared Small Target Detection | Zuo Jiayi, Pei Songwei, Wang Shuhuai, Wu Yifei, Wang Shangguang | Beijing University of Posts and Telecommunications | 提出目标证据链验证机制，在增强前验证红外小目标检测的可靠性。 | [#1758](https://github.com/thinson/RS-PaperClaw/issues/1758) |
| [20261119] RemoteVLPG: How to Obtain a Specific VLM for Language-Guided Path Generation on Remote Sensing Images? | Dang Junzhe, Zhang Mengmeng, Zhang Yuxiang, Li Wei | Beijing Institute of Technology, Zhuhai, Guangdong, China. (；the Jockey Club STEM Laboratory of Quantitative Remote Sensing, Department of Geography, the University of Hong Kong, Hong Kong, China. ( | 面向遥感图像语言引导路径生成，探索如何获得专用视觉语言模型。 | [#1759](https://github.com/thinson/RS-PaperClaw/issues/1759) |
| [20261119] HOPD: Historical On-Policy Distillation for SAR MLLM Continual Learning | Li Yuxuan, Derrick Goh Xin Deik, Duan Zheng-Peng, Sun Qianru, Li Weijie | Singapore Management University；Nanyang Technological University；Nankai University；Xi'an Jiaotong University | 提出历史在线策略蒸馏方法，缓解SAR多模态大模型持续学习中的遗忘。 | [#1760](https://github.com/thinson/RS-PaperClaw/issues/1760) |

## ⚠️ 未纳入日报的匹配论文

以下论文通过关键词/LLM 筛选，但在处理过程中失败未纳入日报。点击 arXiv 链接可查看原文。

| 标题 | arXiv | 失败原因 |
|------|-------|----------|
| Does It Depend on the Split? Frozen Satellite Features vs. Fine-Tuned CNNs for Tree Species Mapping | [2611.25902v1](https://arxiv.org/abs/2611.25902v1) | 质检未通过: 单位为空或无效 |


## 🔎 观察

- 极化SAR分解研究仍具活力，经典方法针对全极化数据的适配与可解释性受到关注。
- 遥感视觉语言模型与持续学习结合增多，验证与蒸馏成为提升可靠性的共性思路。

---

Powered by OpenClaw🦞

<!-- rs-pipeline: {"date": "20261119", "source": "api", "checked_at": "2026-11-20T04:30:37+00:00", "source_complete": true, "candidate_count": 19, "paper_count": 5, "partial": true, "skipped_arxiv_ids": ["2611.25902v1"]} -->

---
