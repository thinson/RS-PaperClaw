# Daily Reports

最近三天日报（最新在前）：

# [20260408](./202604/20260408.md)
## 📌 今日概况

今日共检索候选论文 11 篇；关键词+LLM 智能匹配遥感交叉论文 7 篇；最终纳入日报 7 篇。

今日遥感AI研究呈现三大趋势：一是空间智能与神经表示技术深度融合，OpenSpatial与NeRF类方法推动三维时空建模；二是星上实时处理与量子计算等新型计算范式兴起，拓展遥感系统边界；三是不确定性量化与物理约束嵌入成为提升模型可靠性的关键路径。

## ✨ 今日亮点

- OpenSpatial构建空间智能数据引擎，系统化生成3D标注数据
- 神经辐射场技术延伸至地球观测连续时空表示学习
- 量子-经典混合网络首次应用于遥感图像分割任务

## 🗂 今日文章列表

| 标题 | 作者 | 一句话概括 | Issue |
|---|---|---|---|
| [20260408] OpenSpatial: A Principled Data Engine for Empowering Spatial Intelligence | Liu Jianhui, Sun Haoze, Li Wenbo, Zhang Yanbing, Yang Rui et al. | OpenSpatial提出原则性数据引擎，通过程序化生成与人工验证结合，构建大规模3D空间理解数据集。 | [#297](https://github.com/thinson/RS-PaperClaw/issues/297) |
| [20260408] Assessing the Added Value of Onboard Earth Observation Processing with the IRIDE HEO Service Segment | Parampuneet Kaur Thind, Mwangi Charles, Varetto Giovanni, Sarti Lorenzo, Papa Andrea et al. | IRIDE高椭圆轨道服务段评估星上处理对地观测数据的增值效应，推动服务化架构在轨应用。 | [#298](https://github.com/thinson/RS-PaperClaw/issues/298) |
| [20260408] Location Is All You Need: Continuous Spatiotemporal Neural Representations of Earth Observation Data | Madadikhaljan Mojgan, Prexl Jonathan, Wittmann Isabelle, Conrad M Albrecht, Schmitt Michael | 基于位置编码的连续时空神经表示方法，将NeRF技术扩展至不规则采样的地球观测数据建模。 | [#299](https://github.com/thinson/RS-PaperClaw/issues/299) |
| [20260408] Canopy Tree Height Estimation Using Quantile Regression: Modeling and Evaluating Uncertainty in Remote Sensing | Schrödter Karsten, Pauls Jan, Gieseke Fabian | 分位数回归框架用于冠层树高估计，显式建模预测不确定性以提升遥感反演可靠性。 | [#300](https://github.com/thinson/RS-PaperClaw/issues/300) |
| [20260408] SCT-MOT: Enhancing Air-to-Air Multiple UAVs Tracking with Swarm-Coupled Motion and Trajectory Guidance | Chu Zhaochen, Song Tao, Jin Ren, He Shaoming, Lin Defu et al. | SCT-MOT利用蜂群耦合运动与轨迹引导，解决空中对空中多无人机跟踪的密集遮挡难题。 | [#301](https://github.com/thinson/RS-PaperClaw/issues/301) |
| [20260408] HQF-Net: A Hybrid Quantum-Classical Multi-Scale Fusion Network for Remote Sensing Image Segmentation | Md Aminur Hossain, Ayush V. Patel, Gole Siddhant, Sanjay K. Singh, Banerjee Biplab | HQF-Net设计混合量子-经典多尺度融合网络，探索量子机器学习在遥感语义分割中的潜力。 | [#302](https://github.com/thinson/RS-PaperClaw/issues/302) |
| [20260408] Accelerating 4D Hyperspectral Imaging through Physics-Informed Neural Representation and Adaptive Sampling | Ho Chi-Jui, Bhakta Harsh, Xiong Wei, Antipa Nicholas | 物理信息神经表示结合自适应采样，实现四维高光谱成像的高效压缩与重建加速。 | [#303](https://github.com/thinson/RS-PaperClaw/issues/303) |

## 🔎 观察

- 神经表示技术正从计算机视觉向遥感专用化演进，时空连续建模成为地学基础模型的新基座。
- 星上智能处理与量子计算等前沿范式同步涌现，暗示遥感系统架构可能面临代际变革窗口。

---

Powered by OpenClaw🦞

---

# [20260407](./202604/20260407.md)
## 📌 今日概况

今日共检索候选论文 13 篇；关键词+LLM 智能匹配遥感交叉论文 10 篇；最终纳入日报 10 篇。

今日遥感AI研究呈现多模态融合与基础模型双主线并进态势。SAR-光学异构数据融合持续深化，Vision Transformers与Mamba架构在滑坡检测、变化检测等任务中广泛应用。同时，3D Gaussian Splatting、LLM-as-Judge等新兴技术向UAV视觉定位、电力巡检等场景渗透，边缘智能与近实时监测推动星上处理能力升级。

## ✨ 今日亮点

- 多模态基础模型统一框架：单一模型实现遥感图像复原与融合的语言引导处理
- Mamba架构引入高光谱领域：物理对齐的频谱Mamba实现小样本目标检测语义-动态解耦
- LLM-as-Judge评估范式：大语言模型用于无人机电力线分割的语义级质量评判

## 🗂 今日文章列表

| 标题 | 作者 | 一句话概括 | Issue |
|---|---|---|---|
| [20260407] Multi-Modal Landslide Detection from Sentinel-1 SAR and Sentinel-2 Optical Imagery Using Multi-Encoder Vision Transformers and Ensemble Learning | Nasios Ioannis | 提出多编码器Vision Transformers与集成学习框架，融合Sentinel-1 SAR与Sentinel-2光学影像实现滑坡检测。 | [#286](https://github.com/thinson/RS-PaperClaw/issues/286) |
| [20260407] Edge Intelligence for Satellite-based Earth Observation: Scheduling Image Acquisition and Processing | Soret Beatriz, Antonio M. Mercado-Martínez, Jurado-Navas Antonio, Nicolai D. Lyholm, Moretti Marco et al. | 构建卫星对地观测边缘智能架构，联合优化星上图像获取调度与在轨处理资源分配。 | [#287](https://github.com/thinson/RS-PaperClaw/issues/287) |
| [20260407] ASSR-Net: Anisotropic Structure-Aware and Spectrally Recalibrated Network for Hyperspectral Image Fusion | Song Qiya, Zhou Hongzhi, Tan Lishan, Dian Renwei, Li Shutao | 设计各向异性结构感知与光谱重校准网络ASSR-Net，针对高光谱图像融合任务增强空间-光谱一致性。 | [#288](https://github.com/thinson/RS-PaperClaw/issues/288) |
| [20260407] A Unified Foundation Model for All-in-One Multi-Modal Remote Sensing Image Restoration and Fusion with Language Prompting | Cui Yongchuan, Liu Peng | 开发统一多模态遥感基础模型，支持语言提示驱动的图像复原与融合一体化处理。 | [#289](https://github.com/thinson/RS-PaperClaw/issues/289) |
| [20260407] Physics-Aligned Spectral Mamba: Decoupling Semantics and Dynamics for Few-Shot Hyperspectral Target Detection | Gong Luqi, Xie Qixin, Chen Yue, Chen Ziqiang, Fan Fanda et al. | 提出物理对齐的频谱Mamba模型，通过语义与动态解耦实现高光谱小样本目标检测。 | [#290](https://github.com/thinson/RS-PaperClaw/issues/290) |
| [20260407] Prior-guided Fusion of Multimodal Features for Change Detection from Optical-SAR Images | Liu Xuanguang, Ding Lei, Li Yujie, Dai Chenguang, Zhang Zhenchao et al. | 引入先验引导的多模态特征融合机制，提升光学-SAR异构影像变化检测的跨模态对齐能力。 | [#291](https://github.com/thinson/RS-PaperClaw/issues/291) |
| [20260407] LSGS-Loc: Towards Robust 3DGS-Based Visual Localization for Large-Scale UAV Scenarios | Zhang Xiang, Wang Tengfei, Xu Fang, Wang Xin, Zhan Zongqian | 构建面向大规模无人机场景的3DGS视觉定位框架LSGS-Loc，采用尺度感知初始化增强鲁棒性。 | [#292](https://github.com/thinson/RS-PaperClaw/issues/292) |
| [20260407] Near real-time monitoring of global land-ocean cover dynamics | Wang Lixing, Li Tao, Dou Xinyu, Liu Zhu | 建立全球陆-海覆盖近实时监测系统，实现土地覆盖与海冰动态的快速遥感反演。 | [#293](https://github.com/thinson/RS-PaperClaw/issues/293) |
| [20260407] UAVReason: A Unified, Large-Scale Benchmark for Multimodal Aerial Scene Reasoning and Generation | Sun Jintao, Zhang Hu, Di Donglin, Ding Gangyi, Zheng Zhedong | 发布大规模无人机多模态 aerial场景推理与生成基准UAVReason，涵盖视觉问答与场景理解任务。 | [#294](https://github.com/thinson/RS-PaperClaw/issues/294) |
| [20260407] LLM-as-Judge for Semantic Judging of Powerline Segmentation in UAV Inspection | Hossain Akram, Abdelfattah Rabab, Wang Xiaofeng, Abdelfatah Kareem | 探索LLM-as-Judge范式用于无人机巡检电力线分割的语义级自动评估，替代传统像素级指标。 | [#295](https://github.com/thinson/RS-PaperClaw/issues/295) |

## 🔎 观察

- Mamba架构正快速渗透高光谱分析领域，其线性复杂度优势或重塑长序列光谱建模范式，但物理可解释性仍需验证。
- LLM-as-Judge从NLP评估迁移至遥感分割质量判断，标志着遥感评价指标从像素精度向语义一致性跃迁，轻量化部署是关键瓶颈。

---

Powered by OpenClaw🦞

---

# [20260406](./202604/20260406.md)
## 📌 今日概况

今日共检索候选论文 7 篇；关键词+LLM 智能匹配遥感交叉论文 3 篇；最终纳入日报 3 篇。

今日研究聚焦空天信息智能处理与传输优化。三篇论文分别覆盖无人机实时深度估计、低轨卫星协同大模型推理及卫星移动性驱动的遥感数据分发，体现遥感AI向边缘智能、星上计算与高效通信融合发展的趋势。

## ✨ 今日亮点

- ZeD-MAP实现零样本深度估计与光束法平差结合，支撑无人机实时三维重建
- 面向LEO星座的LLM协同推理框架，通过模型分割与流水线并行降低通信开销
- OrbitTransit利用卫星轨道移动性优化遥感数据扩散，提升全球观测覆盖效率

## 🗂 今日文章列表

| 标题 | 作者 | 一句话概括 | Issue |
|---|---|---|---|
| [20260406] ZeD-MAP: Bundle Adjustment Guided Zero-Shot Depth Maps for Real-Time Aerial Imaging | Selim Ahmet Iz, Nex Francesco, Kerle Norman, Meissner Henry, Berger Ralf | ZeD-MAP提出光束法平差引导的零样本深度估计方法，无需训练数据即可实现无人机实时 aerial imaging 三维建图。 | [#282](https://github.com/thinson/RS-PaperClaw/issues/282) |
| [20260406] Communication-Efficient Collaborative LLM Inference over LEO Satellite Networks | Zhang Songge, Wu Wen, Li Liang, Wang Ye, Xuemin et al. | 该研究设计通信高效的协同LLM推理架构，通过模型切分与流水线并行适配低轨卫星网络带宽受限场景。 | [#283](https://github.com/thinson/RS-PaperClaw/issues/283) |
| [20260406] OrbitTransit: Traffic Delivery and Diffusion for Earth Observation via Satellite Mobility | Zhao Haoyuan, Chen Long, Yi Ching Chou, Fang Hao, Liu Jiangchuan | OrbitTransit利用低轨卫星轨道移动性构建动态流量交付网络，优化地球观测数据的全球扩散与时效性。 | [#284](https://github.com/thinson/RS-PaperClaw/issues/284) |

## 🔎 观察

- 星载智能计算成为热点，LLM推理与深度估计等重型任务正向卫星边缘迁移，需平衡算力与能耗约束
- 卫星网络研究从静态拓扑转向动态移动性利用，轨道预测驱动的数据路由或成下一代天基基础设施关键

---

Powered by OpenClaw🦞

---
