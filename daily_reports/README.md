# Daily Reports

最近三天日报（最新在前）：

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

# [20260411](./202604/20260411.md)
## 📌 今日概况

今日共检索候选论文 11 篇；关键词+LLM 智能匹配遥感交叉论文 5 篇；最终纳入日报 5 篇。

今日遥感AI研究聚焦多模态融合与轻量化部署两大方向。Vision Transformer持续渗透卫星影像分析领域，涵盖多尺度表征、SAR-光学配准及高光谱甲烷检测等场景。同时，神经架构搜索与知识蒸馏推动边缘计算应用，红外超分辨率与跨模态匹配技术亦获关注。

## ✨ 今日亮点

- ALiBi位置编码优化多模态多尺度卫星影像表征学习
- SatReg以回归驱动NAS实现轻量化卫星图像分割
- EMIT高光谱数据结合深度学习实现全球甲烷点源监测

## 🗂 今日文章列表

| 标题 | 作者 | 一句话概括 | Issue |
|---|---|---|---|
| [20260411] Multi-modal, multi-scale representation learning for satellite imagery analysis just needs a good ALiBi | Kage Patrick, Andreadis Pavlos | 提出基于ALiBi位置编码的多模态多尺度卫星影像表征学习方法，优化Vision Transformer处理多分辨率遥感数据的能力。 | [#321](https://github.com/thinson/RS-PaperClaw/issues/321) |
| [20260411] SatReg: Regression-based Neural Architecture Search for Lightweight Satellite Image Segmentation | Humes Edward, Mohsenin Tinoosh | SatReg采用回归策略引导神经架构搜索，结合知识蒸馏构建轻量化卫星图像分割模型，适配边缘计算场景。 | [#322](https://github.com/thinson/RS-PaperClaw/issues/322) |
| [20260411] Are Pretrained Image Matchers Good Enough for SAR-Optical Satellite Registration? | Corley Isaac, Stoken Alex, Berton Gabriele | 系统评估预训练图像匹配器在SAR-光学卫星配准中的零样本迁移能力，探讨跨模态遥感数据对齐的适用边界。 | [#323](https://github.com/thinson/RS-PaperClaw/issues/323) |
| [20260411] Dual-Branch Remote Sensing Infrared Image Super-Resolution | Ge Xining, Chang Gengjia, Yuan Weijun, Li Zhan, Chen Zhanglu et al. | 设计双分支网络架构针对遥感红外图像超分辨率任务，强化热成像细节重建与空间信息恢复。 | [#324](https://github.com/thinson/RS-PaperClaw/issues/324) |
| [20260411] Global monitoring of methane point sources using deep learning on hyperspectral radiance measurements from EMIT | Vishal V. Batchu, Conserva Michelangelo, Wilson Alex, Anna M. Michalak, Gulshan Varun et al. | 基于EMIT高光谱辐亮度测量数据，利用深度学习与Vision Transformer实现全球尺度甲烷点源排放的自动化监测。 | [#325](https://github.com/thinson/RS-PaperClaw/issues/325) |

## 🔎 观察

- 位置编码技术正成为提升遥感Transformer多尺度处理能力的关键切入点，ALiBi等方案或逐步替代传统方法。
- 轻量化与边缘部署需求驱动NAS-知识蒸馏联合优化范式兴起，模型效率与任务精度的平衡设计趋于精细化。

---

Powered by OpenClaw🦞

---
