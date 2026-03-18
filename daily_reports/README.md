# Daily Reports

最近三天日报（最新在前）：

# [20260317](./202603/20260317.md)
## 📌 今日概况

今日共检索候选论文 13 篇；关键词+LLM 智能匹配遥感交叉论文 8 篇；最终纳入日报 8 篇。

今日遥感AI研究呈现多维度技术突破：深度估计与目标检测聚焦效率与精度平衡，扩散模型与多核卷积网络分别实现40倍加速与高效多尺度提取；神经符号AI、多智能体强化学习等新兴范式进入遥感应用；数据-centric方法、域泛化与3D投影等基础问题持续受到关注，高光谱处理在频域特征与光谱驱动增强方面取得进展。

## ✨ 今日亮点

- D³-RSMDE将扩散模型引入遥感单目深度估计，实现40倍加速与高保真实时处理
- PKINet-v2通过各向异性多核卷积优化遥感目标检测，兼顾强大表征与计算效率
- NeSy-Route构建神经符号路由规划基准，推动约束优化与可解释AI在遥感落地

## 🗂 今日文章列表

| 标题 | 作者 | 一句话概括 | Issue |
|---|---|---|---|
| [20260317] $D^3$-RSMDE: 40$\times$ Faster and High-Fidelity Remote Sensing Monocular Depth Estimation | Wang Ruizhi, Li Weihan, Feng Zunlei, Zhang Haofei, Song Mingli et al. | D³-RSMDE提出基于扩散模型的遥感单目深度估计方法，速度提升40倍同时保持高保真度。 | [#117](https://github.com/thinson/RS-PaperClaw/issues/117) |
| [20260317] PKINet-v2: Towards Powerful and Efficient Poly-Kernel Remote Sensing Object Detection | Cai Xinhao, Li Liulei, Pei Gensheng, Sun Zeren, Yao Yazhou et al. | PKINet-v2设计多核卷积网络，通过各向异性核实现高效多尺度特征提取用于遥感目标检测。 | [#118](https://github.com/thinson/RS-PaperClaw/issues/118) |
| [20260317] NeSy-Route: A Neuro-Symbolic Benchmark for Constrained Route Planning in Remote Sensing | Yang Ming, Zhou Zhi, Tian Shi-Yu, Yu Kun-Yang, Guo Lan-Zhe et al. | NeSy-Route建立神经符号路由规划基准数据集，支持约束优化与可解释路径推理研究。 | [#119](https://github.com/thinson/RS-PaperClaw/issues/119) |
| [20260317] Communication-Aware Multi-Agent Reinforcement Learning for Decentralized Cooperative UAV Deployment | Fan Enguang, Chen Yifan, Shan Zihan, Caesar Matthew, Kim Jae | 面向UAV集群部署，提出通信感知多智能体强化学习方法实现去中心化协同控制。 | [#125](https://github.com/thinson/RS-PaperClaw/issues/125) |
| [20260317] An assessment of data-centric methods for label noise identification in remote sensing data sets | Kröber Felix, Hoxha Genc, Roscher Ribana | 系统评估数据-centric方法在遥感数据集标签噪声识别中的有效性与适用边界。 | [#133](https://github.com/thinson/RS-PaperClaw/issues/133) |
| [20260317] Preserving Vertical Structure in 3D-to-2D Projection for Permafrost Thaw Mapping | McMillen Justin, Robert Van Alphen, Taha Sadeghi Chorsi, Shabaga Jason, Rodgers Mel et al. | 针对多年冻土融化制图，开发保留垂直结构的3D-to-2D投影方法以维持森林分层信息。 | [#134](https://github.com/thinson/RS-PaperClaw/issues/134) |
| [20260317] Spectral Property-Driven Data Augmentation for Hyperspectral Single-Source Domain Generalization | Chen Taiqin, Wang Yifeng, Feng Xiaochen, Zhu Zhilin, Sha Hao et al. | 基于光谱属性驱动设计数据增强策略，提升高光谱图像单源域泛化能力。 | [#135](https://github.com/thinson/RS-PaperClaw/issues/135) |
| [20260317] 3D Fourier-based Global Feature Extraction for Hyperspectral Image Classification | Ahmad Muhammad | 利用3D傅里叶变换提取全局特征，增强高光谱图像分类中的空谱相关性建模。 | [#136](https://github.com/thinson/RS-PaperClaw/issues/136) |

## 🔎 观察

- 扩散模型正从生成任务向判别任务渗透，D³-RSMDE表明其在实时遥感深度估计中的潜力，但需关注推理效率与模型轻量化的进一步平衡
- 神经符号AI与多智能体强化学习代表遥感智能化的新范式，前者解决可解释约束推理，后者应对动态协同决策，两者结合或成未来趋势

---

Powered by OpenClaw🦞

---

# [20260316](./202603/20260316.md)
## 📌 今日概况

今日共检索候选论文 15 篇；关键词+LLM 智能匹配遥感交叉论文 11 篇；最终纳入日报 11 篇。

今日遥感AI研究呈现多模态融合与生成式AI深化趋势。扩散模型在图像生成与压缩领域持续渗透，SAR与光学遥感技术并行发展，世界模型、KAN网络等新架构开始落地。物理感知嵌入与域自适应方法提升了模型在复杂场景下的鲁棒性。

## ✨ 今日亮点

- 量子启发的酉池化方法首次用于多光谱卫星图像分类，实现降维与特征提取
- RS-WorldModel统一遥感理解与未来场景预测，拓展时空推理新范式
- PPO强化学习驱动的扩散模型实现遥感图像自适应码率分配压缩

## 🗂 今日文章列表

| 标题 | 作者 | 一句话概括 | Issue |
|---|---|---|---|
| [20260316] Quantum-Inspired Unitary Pooling for Multispectral Satellite Image Classification | Maragkopoulos Georgios, Mandilara Aikaterini, Komini Ralntion, Syvridis Dimitris | 提出量子启发的酉池化算子，通过参数化酉矩阵实现多光谱数据降维与分类 | [#104](https://github.com/thinson/RS-PaperClaw/issues/104) |
| [20260316] Real-Time Oriented Object Detection Transformer in Remote Sensing Images | Ding Zeyu, Zhou Yong, Zhao Jiaqi, Du Wen-Liang, Li Xixi et al. | 设计实时定向目标检测Transformer，引入角度分布细化机制处理遥感旋转目标 | [#105](https://github.com/thinson/RS-PaperClaw/issues/105) |
| [20260316] RSGen: Enhancing Layout-Driven Remote Sensing Image Generation with Diverse Edge Guidance | Hou Xianbao, He Yonghao, Boukhers Zeyd, See John, Su Hu et al. | RSGen框架融合布局驱动生成与多样化边缘引导，提升遥感图像合成可控性 | [#106](https://github.com/thinson/RS-PaperClaw/issues/106) |
| [20260316] A PPO-Based Bitrate Allocation Conditional Diffusion Model for Remote Sensing Image Compression | Han Yuming, Kim Jooho, Shakya Anish | 结合近端策略优化与条件扩散模型，实现码率自适应的遥感图像压缩 | [#107](https://github.com/thinson/RS-PaperClaw/issues/107) |
| [20260316] A Tutorial on ALOS2 SAR Utilization: Dataset Preparation, Self-Supervised Pretraining, and Semantic Segmentation | Imamoglu Nevrez, Caglayan Ali, Kouyama Toru | 系统阐述ALOS-2 SAR数据准备、自监督预训练及语义分割完整技术流程 | [#108](https://github.com/thinson/RS-PaperClaw/issues/108) |
| [20260316] PAKAN: Pixel Adaptive Kolmogorov-Arnold Network Modules for Pansharpening | Zhang Haoyu, Chen Haojing, Zhong Zhen, Deng Liangjian | 将Kolmogorov-Arnold网络引入全色锐化，设计像素自适应激活模块 | [#109](https://github.com/thinson/RS-PaperClaw/issues/109) |
| [20260316] Pansharpening for Thin-Cloud Contaminated Remote Sensing Images: A Unified Framework and Benchmark Dataset | Du Songcheng, Zou Yang, Li Jiaxin, Liu Mingxuan, Li Ying et al. | 构建薄云污染遥感图像全色锐化统一框架，并发布配套基准数据集 | [#110](https://github.com/thinson/RS-PaperClaw/issues/110) |
| [20260316] RS-WorldModel: a Unified Model for Remote Sensing Understanding and Future Sense Forecasting | Xu Linrui, Wang Zhongan, Shen Fei, Xu Gang, Zhuang Huiping et al. | RS-WorldModel实现遥感图像理解、变化检测与未来场景预测的联合建模 | [#111](https://github.com/thinson/RS-PaperClaw/issues/111) |
| [20260316] PASTE: Physics-Aware Scattering Topology Embedding Framework for SAR Object Detection | Chen Jiacheng, Xiong Yuxuan, Wang Haipeng | PASTE框架嵌入物理感知的散射拓扑表征，增强SAR目标检测可解释性 | [#112](https://github.com/thinson/RS-PaperClaw/issues/112) |
| [20260316] IntegratingWeather Foundation Model and Satellite to Enable Fine-Grained Solar Irradiance Forecasting | Ma Ziqing, Ying Kai, Gu Xinyue, Zhou Tian, Zhu Tianyu et al. | 融合气象基础模型与卫星观测，实现细粒度太阳辐照度预测 | [#113](https://github.com/thinson/RS-PaperClaw/issues/113) |
| [20260316] Robust Building Damage Detection in Cross-Disaster Settings Using Domain Adaptation | Mouradi Asmae, Kshirsagar Shruti | 采用监督域自适应策略，提升跨灾害场景建筑损毁检测的泛化能力 | [#114](https://github.com/thinson/RS-PaperClaw/issues/114) |

## 🔎 观察

- 扩散模型已从生成任务向压缩、编辑等下游任务延伸，显示基础模型化趋势
- KAN、量子计算等新型计算范式开始渗透遥感领域，架构创新进入活跃期

---

Powered by OpenClaw🦞

---

# [20260315](./202603/20260315.md)
## 📌 今日概况

今日共检索候选论文 9 篇；关键词+LLM 智能匹配遥感交叉论文 8 篇；最终纳入日报 8 篇。

今日遥感AI研究呈现两大主线：一是多模态大语言模型在低空无人机视觉理解、农业场景推理及地籍空间认知中的深度渗透；二是端到端自主导航与零样本泛化技术的突破，推动无人机从感知向决策闭环演进。点云实例分割与隐式神经表示等基础技术持续支撑垂直应用创新。

## ✨ 今日亮点

- 多模态大模型成为低空遥感理解的核心引擎，UAVBench与AerialVLA分别构建评测基准与端到端导航框架
- 农业遥感进入感知-推理解耦新范式，AgroNVILA与无标签3D麦穗分割技术降低标注依赖
- 零样本泛化与结构化提示工程突破，G-ZAP实现任意尺度全色锐化，AeroGen重构无人机编程范式

## 🗂 今日文章列表

| 标题 | 作者 | 一句话概括 | Issue |
|---|---|---|---|
| [20260315] G-ZAP: A Generalizable Zero-Shot Framework for Arbitrary-Scale Pansharpening | Yang Zhiqi, Yin Shan, Liang Jingze, Deng Liang-Jian | G-ZAP提出可泛化的零样本任意尺度全色锐化框架，基于隐式神经表示实现多尺度融合 | [#82](https://github.com/thinson/RS-PaperClaw/issues/82) |
| [20260315] Seeing Where to Deploy: Metric RGB-Based Traversability Analysis for Aerial-to-Ground Hidden Space Inspection | Lee Seoyoung, Shaekh Mohammad Shithil, Pushp Durgakant, Liu Lantao, Wang Zhangyang | 基于度量RGB的多视图重建方法，实现无人机-地面机器人协同的隐蔽空间可通行性分析 | [#97](https://github.com/thinson/RS-PaperClaw/issues/97) |
| [20260315] GroundSet: A Cadastral-Grounded Dataset for Spatial Understanding with Vector Data | Ferrod Roger, Lecene Maël, Sapkota Krishna, Leifman George, Silverman Vered et al. | GroundSet构建首个地籍向量数据 grounding 数据集，支撑空间理解多模态大模型训练 | [#98](https://github.com/thinson/RS-PaperClaw/issues/98) |
| [20260315] AerialVLA: A Vision-Language-Action Model for UAV Navigation via Minimalist End-to-End Control | Xu Peng, Deng Zhengnan, Deng Jiayan, Gu Zonghua, Wan Shaohua | AerialVLA开发极简端到端控制的无人机视觉-语言-动作模型，推进自主导航实用化 | [#99](https://github.com/thinson/RS-PaperClaw/issues/99) |
| [20260315] AgroNVILA: Perception-Reasoning Decoupling for Multi-view Agricultural Multimodal Large Language Models | Zhang Jiarui, Hu Junqi, Mai Zurong, Chen Yuhang, Lou Shuohong et al. | AgroNVILA通过感知-推理解耦架构，提升农业多模态大模型的多视图空间拓扑理解能力 | [#100](https://github.com/thinson/RS-PaperClaw/issues/100) |
| [20260315] UAVBench and UAVIT-1M: Benchmarking and Enhancing MLLMs for Low-Altitude UAV Vision-Language Understanding | Zhan Yang, Yuan Yuan | UAVBench与UAVIT-1M百万级数据集系统性评测低空无人机视觉-语言理解能力瓶颈 | [#101](https://github.com/thinson/RS-PaperClaw/issues/101) |
| [20260315] In-Field 3D Wheat Head Instance Segmentation From TLS Point Clouds Using Deep Learning Without Manual Labels | Medic Tomislav, Nan Liangliang | 基于地面激光扫描点云与深度学习的无标签3D麦穗实例分割方法，助力田间表型分析 | [#102](https://github.com/thinson/RS-PaperClaw/issues/102) |
| [20260315] AeroGen: Agentic Drone Autonomy through Single-Shot Structured Prompting &amp; Drone SDK | Astu Kautuk, Simmhan Yogesh | AeroGen以单次结构化提示调用无人机SDK，实现大模型驱动的自主飞行代码生成 | [#103](https://github.com/thinson/RS-PaperClaw/issues/103) |

## 🔎 观察

- 低空经济基础设施层趋于成熟：评测基准、专用数据集、端到端控制框架同步涌现，MLLM正成为无人机系统的标准感知接口
- 农业遥感呈现'重推理轻标注'趋势：感知-解耦架构与无监督点云分割并行发展，缓解专业领域标注稀缺瓶颈

---

Powered by OpenClaw🦞

---
