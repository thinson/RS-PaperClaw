# Daily Reports

最近三天日报（最新在前）：

# [20260414](./202604/20260414.md)
## 📌 今日概况

今日共检索候选论文 12 篇；关键词+LLM 智能匹配遥感交叉论文 5 篇；最终纳入日报 5 篇。

今日遥感AI研究聚焦轻量化部署与多模态融合两大主线。星载边缘计算需求推动轻量图像修复网络发展，多智能体系统赋能卫星影像事件理解与描述。高光谱去噪、梯田地块提取及全色锐化等任务持续深化，数学物理方法（欧拉公式、全变分）与深度学习结合趋势明显。

## ✨ 今日亮点

- 星载AI轻量化：面向卫星在轨处理的轻量学习图像修复方法
- 多智能体事件感知：卫星影像新闻事件检测与描述的反馈协作系统
- 多模态农业数据：全球梯田地块边界数据集融合光学与高程信息

## 🗂 今日文章列表

| 标题 | 作者 | 一句话概括 | Issue |
|---|---|---|---|
| [20260414] Rethinking Satellite Image Restoration for Onboard AI: A Lightweight Learning-Based Approach | Dorise Adrien, Bellizzi Marjorie, Hlimi Omar | 提出轻量学习网络实现卫星图像在轨修复，降低星载AI计算资源消耗。 | [#343](https://github.com/thinson/RS-PaperClaw/issues/343) |
| [20260414] A Multi-Agent Feedback System for Detecting and Describing News Events in Satellite Imagery | Anderson Madeline, Klassen Mikhail, Hoover Ash, Cahoy Kerri | 构建多智能体反馈系统，实现卫星影像多时相变化检测与事件自动描述。 | [#344](https://github.com/thinson/RS-PaperClaw/issues/344) |
| [20260414] Spatial-Spectral Adaptive Fidelity and Noise Prior Reduction Guided Hyperspectral Image Denoising | Xie Xuelin, Lu Xiliang, Wang Zhengshan, Zhang Yang, Chen Long | 设计空间-光谱自适应保真与噪声先验降维方法，提升高光谱混合噪声去除效果。 | [#345](https://github.com/thinson/RS-PaperClaw/issues/345) |
| [20260414] GTPBD-MM: A Global Terraced Parcel and Boundary Dataset with Multi-Modality | Zhang Zhiwei, Zeng Xingyuan, Kong Xinkai, Zhang Kunquan, Liang Haoyuan et al. | 发布全球多模态梯田地块边界数据集，融合遥感影像与数字高程模型信息。 | [#347](https://github.com/thinson/RS-PaperClaw/issues/347) |
| [20260414] Euler-inspired Decoupling Neural Operator for Efficient Pansharpening | Zhu Anqi, Ma Mengting, Jiang Yizhen, Li Xiangdong, Zheng Kai et al. | 基于欧拉公式解耦神经算子，实现高效全色锐化频率域处理。 | [#349](https://github.com/thinson/RS-PaperClaw/issues/349) |

## 🔎 观察

- 星载边缘智能成为新焦点，轻量化设计从模型压缩转向任务特定的网络架构重构。
- 多智能体架构开始渗透遥感解译流程，人机协作范式或重塑卫星影像信息提取模式。

---

Powered by OpenClaw🦞

---

# [20260413](./202604/20260413.md)
## 📌 今日概况

今日共检索候选论文 15 篇；关键词+LLM 智能匹配遥感交叉论文 9 篇；最终纳入日报 9 篇。

今日遥感AI研究呈现多模态融合与效率优化双主线。Mamba架构、扩散模型与联邦学习等新兴技术持续渗透，视觉-语言模型向变化检测、多光谱理解等任务延伸。同时，成本感知采样、无训练视觉令牌压缩等方向凸显对高分辨率数据高效处理的迫切需求。

## ✨ 今日亮点

- Mamba架构首次应用于爆炸冲击多尺度结构损伤评估，融合多模态数据实现快速诊断
- HuiYanEarth-SAR构建SAR基础模型，利用地理先验与散射机制实现高保真低成本影像生成
- Seg2Change将开放词汇语义分割适配于遥感变化检测，拓展视觉-语言模型应用边界

## 🗂 今日文章列表

| 标题 | 作者 | 一句话概括 | Issue |
|---|---|---|---|
| [20260413] A Mamba-Based Multimodal Network for Multiscale Blast-Induced Rapid Structural Damage Assessment | Ma Wanli, Selvakumaran Sivasakthy, Dain G. Farrimond, Adam A. Dennis, Samuel E. Rigby | 提出基于Mamba的多模态网络，融合多源数据实现爆炸荷载下结构损伤的多尺度快速评估。 | [#331](https://github.com/thinson/RS-PaperClaw/issues/331) |
| [20260413] The Impact of Federated Learning on Distributed Remote Sensing Archives | Umashankar Anand, Tomotaki-Dawoud Karam, Schneider Nicolai | 探讨联邦学习在非独立同分布遥感数据上的应用，对比FedAvg与FedProx的分布式归档性能。 | [#332](https://github.com/thinson/RS-PaperClaw/issues/332) |
| [20260413] HuiYanEarth-SAR: A Foundation Model for High-Fidelity and Low-Cost Global Remote Sensing Imagery Generation | Liu Yongxiang, Zhou Jie, Song Yafei, Liu Tianpeng, Liu Li | 构建HuiYanEarth-SAR基础模型，结合地理先验与散射机制实现全球高保真低成本SAR影像生成。 | [#333](https://github.com/thinson/RS-PaperClaw/issues/333) |
| [20260413] Observe Less, Understand More: Cost-aware Cross-scale Observation for Remote Sensing Understanding | Xie Zhenghao, Xiao Jing, Wang Zhenqi, Ma Kexin, Liao Liang et al. | 提出成本感知的跨尺度观测框架，以更少观测实现高分辨率遥感理解，优化采样效率。 | [#334](https://github.com/thinson/RS-PaperClaw/issues/334) |
| [20260413] Beyond Reconstruction: Reconstruction-to-Vector Diffusion for Hyperspectral Anomaly Detection | Xiang Jijun, Wang Jiayi, Wang Pengxiang, Chen Cheng, Wang Nian et al. | 设计重建到向量的扩散范式，通过流形净化提升高光谱异常检测的亚像元识别能力。 | [#335](https://github.com/thinson/RS-PaperClaw/issues/335) |
| [20260413] A Deep Equilibrium Network for Hyperspectral Unmixing | Wang Chentong, Gao Jincheng, Zhu Fei, Chen Jie | 构建深度均衡网络用于高光谱解混，以隐式微分联合建模光谱-空间特征与丰度估计。 | [#337](https://github.com/thinson/RS-PaperClaw/issues/337) |
| [20260413] Bridging the RGB-IR Gap: Consensus and Discrepancy Modeling for Text-Guided Multispectral Detection | Wu Jiaqi, Wang Zhen, Huang Enhao, Shen Kangqing, Wang Yulin et al. | 建立RGB-IR共识与差异建模框架，以文本引导弥合跨模态语义鸿沟实现多光谱检测。 | [#338](https://github.com/thinson/RS-PaperClaw/issues/338) |
| [20260413] Seg2Change: Adapting Open-Vocabulary Semantic Segmentation Model for Remote Sensing Change Detection | Su You, Song Yonghong, Chen Jingqi, Wen Zehan | 将开放词汇语义分割模型适配于遥感变化检测，实现无需特定训练的灵活语义迁移。 | [#339](https://github.com/thinson/RS-PaperClaw/issues/339) |
| [20260413] Semantic-Geometric Dual Compression: Training-Free Visual Token Reduction for Ultra-High-Resolution Remote Sensing Understanding | Li Yueying, Wang Fengxiang, Li Yan, Chen Mingshuo, Zhao Mengying et al. | 提出语义-几何双重压缩策略，无训练减少视觉令牌以支撑超高分辨率遥感理解。 | [#340](https://github.com/thinson/RS-PaperClaw/issues/340) |

## 🔎 观察

- 视觉-语言模型正从通用分割向遥感专属任务（变化检测、多光谱对齐）纵深渗透，零样本能力成为关键诉求。
- 高分辨率遥感数据的计算瓶颈催生效率导向研究，成本感知采样与令牌压缩或成未来部署标配。

---

Powered by OpenClaw🦞

---

# [20260412](./202604/20260412.md)
## 📌 今日概况

今日共检索候选论文 4 篇；关键词+LLM 智能匹配遥感交叉论文 4 篇；最终纳入日报 4 篇。

今日遥感AI研究聚焦多模态大模型与基础模型创新。视觉语言模型在地理定位任务中实现生成器向检索器的范式转换，遥感基础模型探索语义 grounding 新路径。同时，多光谱融合与主动式激光雷达-惯性里程计等方向亦有进展，体现从数据融合到智能交互的技术纵深。

## ✨ 今日亮点

- MLLM解锁自然语言引导的地理定位，通过参数高效微调实现生成到检索的范式跃迁
- GeoMeld构建语义 grounded 的遥感基础模型，推进多模态对比学习与地理空间AI融合
- CoFusion提出光谱坐标注意力机制，实现多光谱与高光谱图像的高效融合

## 🗂 今日文章列表

| 标题 | 作者 | 一句话概括 | Issue |
|---|---|---|---|
| [20260412] Turning Generators into Retrievers: Unlocking MLLMs for Natural Language-Guided Geo-Localization | Chen Yuqi, Zhang Xiaohan, Arrabi Ahmad, Sultani Waqas, Chen Chen et al. | Chen等提出将多模态大语言模型从生成器转化为检索器，通过参数高效微调实现自然语言引导的地理定位。 | [#327](https://github.com/thinson/RS-PaperClaw/issues/327) |
| [20260412] GeoMeld: Toward Semantically Grounded Foundation Models for Remote Sensing | Hasan Maram, Md Aminur Hossain, Roy Savitra, Bhowmik Souparna, Ayush V. Patel et al. | Hasan等构建GeoMeld框架，通过语义 grounding 与对比学习增强遥感基础模型的多模态表征能力。 | [#328](https://github.com/thinson/RS-PaperClaw/issues/328) |
| [20260412] CoFusion: Multispectral and Hyperspectral Image Fusion via Spectral Coordinate Attention | Li Baisong | Li提出CoFusion方法，利用光谱坐标注意力机制实现多光谱与高光谱图像的多尺度空谱协同融合。 | [#329](https://github.com/thinson/RS-PaperClaw/issues/329) |
| [20260412] AWARE: Adaptive Whole-body Active Rotating Control for Enhanced LiDAR-Inertial Odometry under Human-in-the-Loop Interaction | Zhang Yizhe, Li Jianping, Yin Liangliang, Dong Zhen, Yang Bisheng | Zhang等设计AWARE系统，通过人在回路交互实现无人机全身体主动旋转控制以增强激光雷达-惯性里程计。 | [#342](https://github.com/thinson/RS-PaperClaw/issues/342) |

## 🔎 观察

- 视觉语言模型正从通用领域向遥感专用场景深度渗透，生成-检索范式转换或重塑跨模态检索技术路线
- 主动感知与人机协同成为无人机导航新趋势，传统被动式状态估计向交互式智能控制演进

---

Powered by OpenClaw🦞

---
