# Daily Reports

最近三天日报（最新在前）：

# [20260606](./202606/20260606.md)
## 📌 今日概况

今日共检索候选论文 6 篇；关键词+LLM 智能匹配遥感交叉论文 5 篇；最终纳入日报 5 篇。

今日研究聚焦于遥感与地理空间智能的交叉创新，涵盖大气校正、地理定位、三维重建及生态监测。Transformer与图神经网络成为主流方法，分别用于高光谱大气补偿和时序地理定位。同时，卫星影像辅助度量尺度恢复、OpenStreetMap对比学习表征、以及近80年海草变化检测等研究，展现了从算法到应用的广泛探索。

## ✨ 今日亮点

- Transformer用于远距离长波红外高光谱大气补偿。
- 双塔图神经网络实现时序地理定位。
- 卫星影像助力前馈重建模型恢复度量尺度。

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260606] Set-Based Transformer for Atmospheric Compensation in Standoff LWIR Hyperspectral Imaging | Perez Fabian, Quintero Nicolas, Acevedo Jeferson, Rueda-Chacon Hoover | Department of Computer Science, Universidad Industrial de Santander | 提出基于集合的Transformer模型，用于远距离长波红外高光谱成像的大气补偿。 | [#682](https://github.com/thinson/RS-PaperClaw/issues/682) |
| [20260606] GeoGNN: Time Series Geo-Localization using Two-Tower Graph Neural Networks | Tran Toan, Abebe Waqwoya, Potnis Abhishek, Chinthavali Supriya, Shahabi Cyrus, Xiong Li, Lunga Dalton | Emory University Oak Ridge National Laboratory Oak Ridge National Laboratory；Oak Ridge National Laboratory University of Southern California Emory University；Oak Ridge National Laboratory | GeoGNN采用双塔图神经网络，实现时序数据的地理定位。 | [#683](https://github.com/thinson/RS-PaperClaw/issues/683) |
| [20260606] Empowering Feed-Forward Reconstruction Models with Metric Scale via Satellite Images | Ze Xianghui, Luo Yongjian, Chao Mengjun, Song Zhenbo, Lu Jianfeng, Shi Yujiao | Nanjing University of Science and Technology；ShanghaiTech University | 利用卫星影像为前馈三维重建模型提供度量尺度信息。 | [#684](https://github.com/thinson/RS-PaperClaw/issues/684) |
| [20260606] OSMGraphCLIP: Learning Global Location Representations from OpenStreetMap Graphs | Michail Dimitrios, Saka Eleni, Giannopoulos Ioannis, Papoutsis Ioannis | National Technical University of Athens, Athens, Greece；Vienna University of Technology, Vienna, Austria | OSMGraphCLIP通过对比学习从OpenStreetMap图学习全局位置表征。 | [#685](https://github.com/thinson/RS-PaperClaw/issues/685) |
| [20260606] Feasibility to detect rapid change and disappearance of seagrass: Lessons from nearly 80 years of vegetation change in the Ako, Seto Inland Sea, Japan | Yamakita Takehisa, Igarashi Yoji, Eto Akira, Ishida Ken, Iiyama Masaaki | Japan Agency for Marine-Earth Science and Technology (JAMSTEC), Application Laboratory (APL), 3173-25, Showa-machi；The University of Tokyo, Graduate School of Agricultural and Life Sciences, 1-1-1 Yayoi, Bunkyo City, Tokyo, Japan；Tokyo University of Marine Science and Technology, 4-5-7 Kohnan, Minato-ku, Tokyo, Japan；Shiga University, Faculty of Data Science, 1-1-1 Banba, Hikone City, Shiga, Japan | 利用近80年航拍影像检测海草植被的快速变化与消失。 | [#686](https://github.com/thinson/RS-PaperClaw/issues/686) |

## 🔎 观察

- 图神经网络与Transformer在遥感任务中应用日益广泛，尤其在空间关系建模方面。
- 长时序遥感分析结合深度学习，为生态监测提供历史变迁的量化手段。

---

Powered by OpenClaw🦞

---

# [20260605](./202606/20260605.md)
## 📌 今日概况

今日共检索候选论文 8 篇；关键词+LLM 智能匹配遥感交叉论文 3 篇；最终纳入日报 3 篇。

今日遥感AI研究聚焦于SAR图像处理与无人机导航两大方向。SAR领域，一篇工作利用深度学习从检测SAR图像中提取InSAR相干性，另一篇则通过物理驱动方法理解飞机目标的语义散射结构。无人机导航方面，提出了一种模拟飞行员思维的细粒度长时程导航方法，结合视觉-语言模型实现6自由度轨迹控制。整体趋势显示，物理模型与数据驱动方法的融合日益深入。

## ✨ 今日亮点

- 深度学习提升InSAR相干性估计精度
- 物理驱动SAR飞机目标散射结构理解
- 视觉-语言模型赋能长时程无人机导航

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260605] Beyond Backscatter: InSAR coherence from detected SAR images | Sica Francescopaolo, Pulella Andrea, Schmitt Michael | Department of Aerospace Engineering, University of the Bundeswehr Munich, Neubiberg, Germany；Microwaves and Radar Institute, German Aerospace Center (DLR), Weßling, Germany | 利用残差U-Net从检测SAR图像估计InSAR相干性，超越传统后向散射方法。 | [#678](https://github.com/thinson/RS-PaperClaw/issues/678) |
| [20260605] Physics-Driven Semantic Scattering Structure Understanding of Aircraft Target in SAR Images | Yin Yifei, Yu Xiaogang, Shi Hao, Chen Liang, Li Wei | the School of Information and Electronics, Beijing Institute of Technology, Beijing , China；the National Key Laboratory of Science and Technology on Space-Born Intelligent Information Processing；the Beijing Institute of Remote Sensing Information, Beijing, China | 提出物理驱动语义散射结构理解方法，用于SAR图像飞机目标识别。 | [#679](https://github.com/thinson/RS-PaperClaw/issues/679) |
| [20260605] Think Like a Pilot: Fine-Grained Long-Horizon UAV Navigation | Zheng Xiangyi, Wang Xiangyu, Liao Qinan, Tang Zimu, Liao Yue, Lyu Dongyue, Wang Guodong, Liu Junjie, Liu Si | Colab May 2026；Colab, Beihang University 2；National University of Singapore；https://buaa-colalab.github.io/FLIGHT/；https://github.com/buaa-colalab/FLIGHT | 模拟飞行员思维，实现细粒度长时程6自由度无人机视觉语言导航。 | [#680](https://github.com/thinson/RS-PaperClaw/issues/680) |

## 🔎 观察

- SAR领域正从单一后向散射分析向多维度信息融合演进。
- 无人机导航研究向长时程、细粒度控制与语言指令结合方向发展。

---

Powered by OpenClaw🦞

---

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
