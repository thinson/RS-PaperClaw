# Daily Reports

最近三天日报（最新在前）：

# [20260604](./202606/20260604.md)
## 📌 今日概况

今日共检索候选论文 15 篇；关键词+LLM 智能匹配遥感交叉论文 12 篇；最终纳入日报 7 篇。

今日遥感AI研究聚焦于Transformer架构的深度应用与多模态融合。多篇工作利用Transformer改进城市绿地提取、云去除及时序异常检测，同时无人机灾害响应与目标跟踪任务中，图神经网络与强化学习方法成为热点。整体趋势显示，模型正从单一任务向自适应、动态场景的智能决策方向发展。

## ✨ 今日亮点

- Transformer与NDVI结合提升城市绿地提取精度
- 自适应三角注意力机制用于遥感影像云去除
- 图神经网络强化无人机多目标跟踪能力

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260604] GMBFormer: An NDVI-Guided Global Memory Bank Transformer for Urban Green-Space Extraction from Ultra-High-Resolution Imagery | Lei Hao, Cheng Xi, Shu Chenlu, Chen Zhiheng, Duan Zhengjie, Wang Haoyu, Shen Zhanfeng | College of Geophysics, Chengdu University of Technology, Chengdu 610059, China；National Engineering Research Center for Geomatics, Aerospace Information Research；Institute, Chinese Academy of Sciences, and University of Chinese Academy of Sciences | 提出NDVI引导的全局记忆库Transformer，用于超高分辨率影像城市绿地提取。 | [#670](https://github.com/thinson/RS-PaperClaw/issues/670) |
| [20260604] DisasterBench: A Multimodal Benchmark for UAV-Based Disaster Response in Complex Environments | Zhang Tan, Li Quanyou, Zhang Lu, Liu Jun, Zhu Xiaofeng, Hu Ping | a School of Computer Science and Engineering, University of Electronic Science and Technology of；b School of Information and Communication Engineering, Dalian University of；c School of Computing and Communications, Lancaster University, Lancaster, LA1 4YW, England；d School of Computer Science and Technology, Hainan University, Haikou, 570228, China | 发布多模态无人机灾害响应基准DisasterBench，评估复杂环境下的推理能力。 | [#671](https://github.com/thinson/RS-PaperClaw/issues/671) |
| [20260604] ATT-CR: Adaptive Triangular Transformer for Cloud Removal | Wu Yang, Deng Ye, Li Pengna, Huang Wenli, Wu Kangyi, Xin Xiaomeng, Wang Jinjun | the Xi'an Jiaotong University, Xi'an, Shaanxi , China；the School of Computing and Artificial Intelligence, Southwestern University of Finance and Economics, Chengdu, Sichuan , China；the Ningbo University of Technology, Ningbo, Zhejiang , China | 设计自适应三角Transformer，通过三角注意力机制有效去除遥感影像云层。 | [#672](https://github.com/thinson/RS-PaperClaw/issues/672) |
| [20260604] AISC deployment in dynamic UAV-assisted MEC network: a reinforcement learning method based on heterogeneous graph attention neural network | Chang Hanzhi, Bai Jing, Tang Xin, Liu Xiaomei | Hanzhi Chang, Jing Bai, Xin Tang and Xiaomei Liu are with the School of；Cyber Science and Engineering, University of International Relations, Beijing | 利用异构图注意力强化学习，优化动态无人机边缘计算网络中的AI服务链部署。 | [#673](https://github.com/thinson/RS-PaperClaw/issues/673) |
| [20260604] T-SAR-JEPA: Self-Supervised Temporal Anomaly Detection in SAR Amplitude Stacks via Latent Prediction | Woldesenbet Kerod, Woldesenbet Abem | Independent Researcher Dakota State University | 提出自监督时序SAR异常检测方法，通过潜在预测学习振幅堆栈中的变化。 | [#674](https://github.com/thinson/RS-PaperClaw/issues/674) |
| [20260604] HDST-GNN: Heterogeneous Dynamic Spatiotemporal Graph Neural Networks for Multi-Object Tracking in UAV Aerial Imagery | Jiang Phillip | Phillip Jiang | 构建异质动态时空图神经网络，提升无人机航拍多目标跟踪性能。 | [#675](https://github.com/thinson/RS-PaperClaw/issues/675) |
| [20260604] BMCR: Adaptive Backbone Module Composition via Reinforcement Learning for Remote Sensing Object Detection | Liu Wenlin, Hu Xikun, Zhong Ping | Wenlin Liu, Xikun Hu, and Ping Zhong are with the College of Elec- backbone composition, limiting their ability to exploit the；tronic Science and Technology, National University of Defense Technology | 采用强化学习自适应组合骨干模块，优化遥感目标检测模型结构。 | [#676](https://github.com/thinson/RS-PaperClaw/issues/676) |

## ⚠️ 未纳入日报的匹配论文

以下论文通过关键词/LLM 筛选，但在处理过程中失败未纳入日报。点击 arXiv 链接可查看原文。

| 标题 | arXiv | 失败原因 |
|------|-------|----------|
| In-Context Multiple Instance Learning | [2606.06458v1](https://arxiv.org/abs/2606.06458v1) | 质检未通过: 单位为空或无效 |
| Comparison of Deep Learning Frameworks For Rice Disease Mapping From UAV Multispectral Imaging | [2606.06359v1](https://arxiv.org/abs/2606.06359v1) | 质检未通过: 单位为空或无效 |
| WorldFly: A World-Model-Based Vision-Language-Action Model for UAV Navigation | [2606.06147v1](https://arxiv.org/abs/2606.06147v1) | 质检未通过: Q6 未通过质检 |
| Physics-Guided Deep Unfolding for Blind Cross-Sensor Spectral Super-Resolution via Learning the Spectral Transformation Function | [2606.05759v1](https://arxiv.org/abs/2606.05759v1) | 质检未通过: Q1 未通过质检; Q3 未通过质检; Q4 未通过质检; Q9 未通过质检 |
| Intercomparison of Machine Learning Algorithms for Remote Sensing-based In-season Crop Mapping | [2606.05731v1](https://arxiv.org/abs/2606.05731v1) | 质检未通过: 单位为空或无效 |


## 🔎 观察

- Transformer正从基础特征提取向任务特定结构（如三角注意力、记忆库）演进
- 无人机遥感研究从单一感知向多模态推理与动态决策系统集成发展

---

Powered by OpenClaw🦞

---

# [20260603](./202606/20260603.md)
## 📌 今日概况

今日共检索候选论文 6 篇；关键词+LLM 智能匹配遥感交叉论文 3 篇；最终纳入日报 1 篇。

今日研究聚焦于低空网络中的HAPs-UAV双基地ISARAC系统，提出联合三维轨迹与功率分配优化方法，旨在提升覆盖范围与续航能力。该工作体现了遥感与通信融合的趋势，为低空网络资源调度提供了新思路。

## ✨ 今日亮点

- 提出HAPs-UAV双基地ISARAC联合优化方案
- 兼顾三维轨迹与功率分配提升网络性能
- 聚焦低空网络覆盖与续航协同问题

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260603] Joint 3D Trajectory and Power Allocation for HAPs-UAV Bistatic ISARAC in Low-Altitude Networks | Huang Bang, Alouini Mohamed-Slim | and Engineering (CEMSE) division in King Abdullah University of Science much broader coverage and signiﬁcantly longer endurance | 研究HAPs-UAV双基地ISARAC中联合三维轨迹与功率分配优化。 | [#668](https://github.com/thinson/RS-PaperClaw/issues/668) |

## ⚠️ 未纳入日报的匹配论文

以下论文通过关键词/LLM 筛选，但在处理过程中失败未纳入日报。点击 arXiv 链接可查看原文。

| 标题 | arXiv | 失败原因 |
|------|-------|----------|
| Data Efficient Complex Feature Fusion Network For Hyperspectral Image Classification | [2606.04710v1](https://arxiv.org/abs/2606.04710v1) | 质检未通过: 单位为空或无效 |
| Optical-Guided Neural Collapse for SAR Few-Shot Class Incremental Learning | [2606.04528v1](https://arxiv.org/abs/2606.04528v1) | 质检未通过: 单位为空或无效 |


## 🔎 观察

- 低空网络资源调度正从单一维度向多维度联合优化演进
- 双基地ISARAC系统有望成为低空遥感与通信融合的关键架构

---

Powered by OpenClaw🦞

---

# [20260602](./202606/20260602.md)
## 📌 今日概况

今日共检索候选论文 6 篇；关键词+LLM 智能匹配遥感交叉论文 5 篇；最终纳入日报 4 篇。

今日遥感AI研究聚焦于多模态与实时处理：长波红外高光谱温度-发射率-纹理分解数据集发布，无人机ISAC系统安全增强，卫星星上甲烷快速检测，以及频域感知融合的多模态变化检测方法。

## ✨ 今日亮点

- 长波红外高光谱温度-发射率-纹理分解基准数据集发布
- 基于扩展卡尔曼滤波的无人机ISAC安全方案
- 星上快速甲烷检测管道结合Mag1c-SAS与LinkNet

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260602] TeX-1500: A Paired Real-World LWIR Hyperspectral Dataset and Benchmark for Temperature-Emissivity-Texture Decomposition | Dai Cheng, Lin Jiale, Xu Hongyi, Song Bingxuan, Xie Ziyang, Bao Fanglin | centered thermal perception；Cheng Dai, Hongyi Xu, Ziyang Xie and Fanglin Bao are with the School；of Science, Westlake University, Hangzhou 310030, China；Jiale Lin and Bingxuan Song are with the School of Engineering, Westlake；University, Hangzhou 310030, China | 提出TeX-1500长波红外高光谱数据集，用于温度-发射率-纹理分解基准。 | [#663](https://github.com/thinson/RS-PaperClaw/issues/663) |
| [20260602] On Secure EKF-enhanced UAV-ISAC Systems | Lei Hongjiang, Jin Heng, Park Ki-Hong, Ye Jia, Yang Liang, Pan Gaofeng, Li Yun | School of Communications and Information Engineering, Chongqing University of Posts and Telecommunications, Chongqing , China；the CEMSE Division, King Abdullah University of Science and Technology；State Key Laboratory of Power Transmission Equipment Technology, School of Electrical Engineering, Chongqing University, Chongqing , China；the College of Computer Science and Electronic Engineering, Hunan University, Changsha , China；the School of Cyberspace Science and Technology, Beijing Institute of Technology, Beijing , China；Chongqing Key Laboratory of Mobile Communications Technology, Chongqing , China | 设计EKF增强的无人机ISAC系统，提升物理层安全与轨迹跟踪。 | [#664](https://github.com/thinson/RS-PaperClaw/issues/664) |
| [20260602] A Fast Methane Detection Pipeline on Board Satellites Based on Mag1c-SAS and LinkNet | Herec Jonáš, Růžička Vít, Pitoňák Rado, Sedmidubsky Jan | the Faculty of Informatics, Masaryk University, Brno, Czech Republic | 提出基于Mag1c-SAS和LinkNet的卫星星上甲烷快速检测管道。 | [#665](https://github.com/thinson/RS-PaperClaw/issues/665) |
| [20260602] FAF-CD: Frequency-Aware Fusion for Change Detection under Imperfect Multimodal Remote Sensing | Wang Yufan, Makrogiannis Sokratis, Kambhamettu Chandra | University of South Florida；Delaware State University；//github.com/VimsLab/FAF-CD | 提出频域感知融合的孪生网络FAF-CD，用于多模态遥感变化检测。 | [#666](https://github.com/thinson/RS-PaperClaw/issues/666) |

## ⚠️ 未纳入日报的匹配论文

以下论文通过关键词/LLM 筛选，但在处理过程中失败未纳入日报。点击 arXiv 链接可查看原文。

| 标题 | arXiv | 失败原因 |
|------|-------|----------|
| Self-Refining Agentic Reinforcement Learning for Vision-Conditioned UAV Navigation | [2606.03963v1](https://arxiv.org/abs/2606.03963v1) | 质检未通过: 单位为空或无效 |


## 🔎 观察

- 多模态融合与星上实时处理成为遥感AI应用的重要趋势。
- 安全性与分解精度在无人机感知与高光谱分析中受到更多关注。

---

Powered by OpenClaw🦞

---
