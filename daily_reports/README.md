# Daily Reports

最近三天日报（最新在前）：

# [20260318](./202603/20260318.md)
## 📌 今日概况

今日共检索候选论文 8 篇；关键词+LLM 智能匹配遥感交叉论文 6 篇；最终纳入日报 6 篇。

今日遥感AI研究呈现多模态融合与低空智能两大主线。视觉-语言模型向遥感开放词汇分割延伸，参数高效学习成为多模态语义分割新方向。同时，无人机检测、机群通信与柔性飞行器控制等低空技术密集涌现，频域特征提取与多智能体系统成为解决复杂场景的关键手段。

## ✨ 今日亮点

- MM-OVSeg实现光学-SAR跨模态开放词汇分割，突破遥感语义类别受限瓶颈
- Local Frequency Bridge网络引入频域桥接机制，应对复杂背景无人机伪装检测
- 多智能体系统首次用于建筑年代队列映射，支撑城市级能源规划决策

## 🗂 今日文章列表

| 标题 | 作者 | 一句话概括 | Issue |
|---|---|---|---|
| [20260318] UAV-CB: A Complex-Background RGB-T Dataset and Local Frequency Bridge Network for UAV Detection | Huang Shenghui, Hu Menghao, Zou Longkun, Chi Hongyu, Li Zekai et al. | UAV-CB数据集与频域桥接网络协同，解决复杂背景下RGB-T无人机检测的伪装与背景干扰难题。 | [#138](https://github.com/thinson/RS-PaperClaw/issues/138) |
| [20260318] Parameter-Efficient Modality-Balanced Symmetric Fusion for Multimodal Remote Sensing Semantic Segmentation | Li Haocheng, Zheng Juepeng, Miao Shuangxi, Lu Ruibo, Cai Guosheng et al. | 参数高效模态平衡对称融合方法，以可学习提示微调视觉基础模型实现遥感多模态语义分割。 | [#139](https://github.com/thinson/RS-PaperClaw/issues/139) |
| [20260318] A Multi-Agent System for Building-Age Cohort Mapping to Support Urban Energy Planning | Thota Kundan, Schlachter Thorsten, Hagenmeyer Veit | 多智能体系统整合遥感与深度学习，完成建筑年代队列自动映射以支持城市能源规划。 | [#140](https://github.com/thinson/RS-PaperClaw/issues/140) |
| [20260318] MM-OVSeg:Multimodal Optical-SAR Fusion for Open-Vocabulary Segmentation in Remote Sensing | Wei Yimin, Xiao Aoran, Chen Hongruixuan, Xia Junshi, Yokoya Naoto | MM-OVSeg融合光学-SAR与视觉-语言模型，实现遥感图像的开放词汇语义分割。 | [#141](https://github.com/thinson/RS-PaperClaw/issues/141) |
| [20260318] 3D Spherical Directly-Connected Antenna Array for Low-Altitude UAV Swarm ISAC | Jiang Haoyu, Dong Zhenjun, Zhou Zhiwen, Zeng Yong | 3D球面直连天线阵列支持低空无人机群通感一体化，实现三维波束赋形。 | [#143](https://github.com/thinson/RS-PaperClaw/issues/143) |
| [20260318] H Infinity Robust Control for Gust Load Alleviation of Geometrically Nonlinear Flexible Aircraft | Nikolaos D. Tantaroudas, Andrea Da Ronch, Karachalios Ilias, Kenneth J. Badcock | H无穷鲁棒控制结合模型降阶，解决几何非线性柔性飞行器的阵风载荷减缓问题。 | [#144](https://github.com/thinson/RS-PaperClaw/issues/144) |

## 🔎 观察

- 低空经济驱动遥感技术向实时感知-通信-控制闭环演进，ISAC与AI检测形成技术簇
- 视觉-语言模型正从自然图像向遥感专属架构适配，模态对齐与参数效率成为落地关键

---

Powered by OpenClaw🦞

---

# [20260317](./202603/20260317.md)
## 📌 今日概况

今日共检索候选论文 13 篇；关键词+LLM 智能匹配遥感交叉论文 8 篇；最终纳入日报 8 篇。

今日遥感AI研究呈现效率与精度并重趋势。单目深度估计与目标检测聚焦实时化与轻量化设计；神经符号AI、多智能体强化学习拓展应用边界；数据-centric方法、域泛化与噪声处理等基础问题持续受关注；高光谱与点云处理在特征提取与垂直结构保持方面有所推进。

## ✨ 今日亮点

- D³-RSMDE实现40倍加速的高保真单目深度估计，扩散模型与Transformer结合突破实时性瓶颈
- PKINet-v2提出各向异性多核卷积架构，在遥感目标检测中平衡精度与计算效率
- NeSy-Route构建神经符号路径规划基准，填补约束优化与深度学习融合评估空白

## 🗂 今日文章列表

| 标题 | 作者 | 一句话概括 | Issue |
|---|---|---|---|
| [20260317] $D^3$-RSMDE: 40$\times$ Faster and High-Fidelity Remote Sensing Monocular Depth Estimation | Wang Ruizhi, Li Weihan, Feng Zunlei, Zhang Haofei, Song Mingli et al. | D³-RSMDE将扩散模型与Vision Transformer结合，实现40倍速度提升的高保真遥感单目深度估计。 | [#117](https://github.com/thinson/RS-PaperClaw/issues/117) |
| [20260317] PKINet-v2: Towards Powerful and Efficient Poly-Kernel Remote Sensing Object Detection | Cai Xinhao, Li Liulei, Pei Gensheng, Sun Zeren, Yao Yazhou et al. | PKINet-v2通过各向异性多核卷积优化多尺度特征提取，提升遥感目标检测的精度与效率。 | [#118](https://github.com/thinson/RS-PaperClaw/issues/118) |
| [20260317] NeSy-Route: A Neuro-Symbolic Benchmark for Constrained Route Planning in Remote Sensing | Yang Ming, Zhou Zhi, Tian Shi-Yu, Yu Kun-Yang, Guo Lan-Zhe et al. | NeSy-Route建立首个神经符号遥感路径规划基准，评估约束优化场景下的AI推理能力。 | [#119](https://github.com/thinson/RS-PaperClaw/issues/119) |
| [20260317] Communication-Aware Multi-Agent Reinforcement Learning for Decentralized Cooperative UAV Deployment | Fan Enguang, Chen Yifan, Shan Zihan, Caesar Matthew, Kim Jae | 该研究提出通信感知的多智能体强化学习框架，实现去中心化UAV集群的协同部署控制。 | [#125](https://github.com/thinson/RS-PaperClaw/issues/125) |
| [20260317] An assessment of data-centric methods for label noise identification in remote sensing data sets | Kröber Felix, Hoxha Genc, Roscher Ribana | 系统评估数据-centric方法在遥感标签噪声识别中的有效性，为数据质量提升提供参考。 | [#133](https://github.com/thinson/RS-PaperClaw/issues/133) |
| [20260317] Preserving Vertical Structure in 3D-to-2D Projection for Permafrost Thaw Mapping | McMillen Justin, Robert Van Alphen, Taha Sadeghi Chorsi, Shabaga Jason, Rodgers Mel et al. | 针对多年冻土融化制图，提出保持垂直结构的3D-to-2D投影方法以保留森林分层信息。 | [#134](https://github.com/thinson/RS-PaperClaw/issues/134) |
| [20260317] Spectral Property-Driven Data Augmentation for Hyperspectral Single-Source Domain Generalization | Chen Taiqin, Wang Yifeng, Feng Xiaochen, Zhu Zhilin, Sha Hao et al. | 基于光谱特性驱动的高光谱数据增强方法，提升单源域泛化场景下的模型鲁棒性。 | [#135](https://github.com/thinson/RS-PaperClaw/issues/135) |
| [20260317] 3D Fourier-based Global Feature Extraction for Hyperspectral Image Classification | Ahmad Muhammad | 利用3D傅里叶变换提取高光谱图像全局特征，增强空谱相关性建模与分类性能。 | [#136](https://github.com/thinson/RS-PaperClaw/issues/136) |

## 🔎 观察

- 实时性需求正深度重构遥感模型架构，扩散模型加速与卷积核优化成为并行技术路线。
- 神经符号AI与多智能体系统进入遥感应用视野，标志着任务复杂度与系统自主性同步升级。

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
