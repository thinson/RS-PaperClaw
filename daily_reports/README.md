# Daily Reports

最近三天日报（最新在前）：

# [20260915](./202609/20260915.md)
## 📌 今日概况

今日共检索候选论文 12 篇；关键词+LLM 智能匹配遥感交叉论文 5 篇；最终纳入日报 5 篇。

今日论文聚焦遥感基础模型与下游任务的衔接，涵盖标签效率、时序迁移与跨域泛化。多篇工作探索将预训练嵌入或语言模型迁移至农田制图、光谱时序预测和指代分割，强调独立验证与因果建模。同时，三维重建与多模态时空预测引入风险图引导和异步耦合机制，提升复杂场景下的鲁棒性。整体趋势显示，遥感AI正从单一精度追求转向可迁移、可解释与跨域基准构建。

## ✨ 今日亮点

- 基础模型嵌入用于农田制图，关注标签效率与时间迁移性。
- 光谱时序学习引入因果潜在预测，支持多视野地球表征。
- 指代遥感分割提出跨域基准，评估视觉语言模型泛化能力。

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260915] From Foundation Embeddings to Cropland Maps: Label Efficiency, Temporal Transferability and Independent Human Validation | Mohammad Ammar Mughees, Montefoschi Giovanni, Chen Zhongxin, Maria Antonia Brovelli | Department of Civil and Environmental Engineering, Politecnico di Milano, Milan, Italy | 评估基础嵌入在农田制图中的标签效率、时序迁移性，并引入独立人工验证。 | [#1271](https://github.com/thinson/RS-PaperClaw/issues/1271) |
| [20260915] SPEAR NeXT Causal Latent Forecasting Across Multiple Horizons for Spectral Temporal Earth Representation Learning | Ranjan Rajiv, Singh Udaiveer, Tamaskar Shashank, Saraswat Dharmendra | Plaksha University；Purdue University | 提出SPEAR NeXT，用因果潜在预测实现多视野光谱时序地球表征学习。 | [#1272](https://github.com/thinson/RS-PaperClaw/issues/1272) |
| [20260915] HLC-GS: Risk-Map-Guided Height-Layer Consistency Gaussian Splatting for DSM Reconstruction from Optical Satellite Imagery | Yang Jie, Pi Yingdong, Luo Qiyan, Wang Xiaoyu, Wen Lekang, Wang Mi | State Key Laboratory of Information Engineering in Surveying, Mapping and Remote Sensing, Wuhan University；Hubei Luojia Laboratory；School of Computer Science, Wuhan University | HLC-GS利用风险图引导高度层一致性高斯泼溅，从光学卫星影像重建DSM。 | [#1273](https://github.com/thinson/RS-PaperClaw/issues/1273) |
| [20260915] AsyncCouple-Flow: Asynchronous Cross-Modal Coupling and Flow Matching for Spatio-Temporal Forecasting | Wu Zhixiang, Liu Yining, Zhao Bo, Chen Szu-Yu, Duan Huiran, Lin Chu, Yang Chuanguang | Institute of Computing Technology, Chinese Academy of Sciences, China；Emory University, USA；University of California, Berkeley, USA；Yale University, USA；Stevens Institute of Technology, USA；City University of New York, USA | AsyncCouple-Flow通过异步跨模态耦合与流匹配，处理时空预测中的缺失模态。 | [#1274](https://github.com/thinson/RS-PaperClaw/issues/1274) |
| [20260915] VPRef: A Cross-Domain Benchmark for Referring Remote Sensing Image Segmentation | Liu Quanwei, Huang Tao, Yang Jiaqi, Xiang Wei | College of Science and Engineering, James Cook University, Cairns,, Australia (；College of Science and Engineering, James Cook University, Cairns QLD, Australia and the Center for AI and Data Science Innovation, James Cook University, Cairns QLD, Australia (；Department of Forest and Wildlife Ecology, University of Wisconsin-Madison, Madison, WI USA (；School of Computing, Engineering and Mathematical Sciences, La Trobe University, Melbourne, VIC, Australia ( | VPRef构建跨域基准，评估指代遥感图像分割中视觉语言模型的域适应能力。 | [#1275](https://github.com/thinson/RS-PaperClaw/issues/1275) |

## 🔎 观察

- 基础模型落地更重标签效率与迁移验证，而非单纯追求精度提升。
- 跨域基准与因果建模成为提升遥感模型泛化与可解释性的关键路径。

---

Powered by OpenClaw🦞

---

# [20260912](./202609/20260912.md)
## 📌 今日概况

今日共检索候选论文 2 篇；关键词+LLM 智能匹配遥感交叉论文 2 篇；最终纳入日报 2 篇。

今日遥感AI研究聚焦于基础模型适配与高效检测架构两个方向。一方面，针对多模态基础模型在遥感领域的迁移，研究者提出基于域感知松弛正交子空间的参数高效微调方法，试图在低秩适配框架下缓解域差异。另一方面，面向无人机航拍等场景，有工作将状态空间建模与高频增强结合到YOLO12中，以提升小目标检测效率。整体趋势显示，遥感AI正从通用大模型直接迁移转向领域定制化适配，同时轻量化与频域信息利用成为检测任务的重要优化手段。

## ✨ 今日亮点

- 多模态基础模型遥感适配引入域感知松弛正交子空间，提升参数高效微调效果。
- YOLO12-MambaScan融合高频增强与状态空间建模，面向无人机小目标检测。
- 两项工作分别代表基础模型领域适配与检测架构轻量化两条技术路线。

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260912] Multimodal Foundation Models Adaptation based on Domain-Aware Relaxed Orthogonal Subspace for Remote Sensing | Luo Han, Yang Ruoyu, Liu Yinhe, Zhong Yanfei | State Key Laboratory of Information Engineering in Surveying, Mapping and Remote Sensing, Wuhan University, Wuhan, China ( | 提出域感知松弛正交子空间方法，实现遥感多模态基础模型的参数高效领域适配。 | [#1284](https://github.com/thinson/RS-PaperClaw/issues/1284) |
| [20260912] YOLO12-MambaScan: An Efficient Object Detector with High-Frequency Enhancement and State-Space Modeling | Wang Hao | BDNRC | 设计YOLO12-MambaScan检测器，结合高频增强与状态空间建模提升无人机小目标检测。 | [#1285](https://github.com/thinson/RS-PaperClaw/issues/1285) |

## 🔎 观察

- 遥感基础模型适配正从简单微调转向结构化子空间约束，以平衡泛化与域特化。
- 状态空间模型与频域增强结合，反映检测任务对计算效率与细粒度信息保留的双重需求。

---

Powered by OpenClaw🦞

---

# [20260911](./202609/20260911.md)
## 📌 今日概况

今日共检索候选论文 10 篇；关键词+LLM 智能匹配遥感交叉论文 6 篇；最终纳入日报 6 篇。

今日论文覆盖遥感AI从平台接口、星上部署到多模态分割与智能体全链路。openEO数据立方体机器学习API降低开发门槛，Φsat-2星上浊度监测体现边缘计算趋势。火星滑坡分割与无人机RGB-热融合分别拓展多模态与跨域应用，Earth-Agent-Pro则推动大模型驱动的端到端对地观测工作流。

## ✨ 今日亮点

- openEO数据立方体机器学习API，降低遥感AI开发门槛
- Φsat-2星上AI实现海岸带浊度实时监测
- Earth-Agent-Pro探索大模型驱动全链路对地观测

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260911] A Machine Learning API for Earth Observation Data Cubes Based on openEO | Pondi Brian, Hurst Jonas, Simoes Rolf, Starke Jonas, Appel Marius, Pebesma Edzer | Institute for Geoinformatics, University of Münster, Heisenbergstr. 2, Münster, 48149；Bochum University of Applied Sciences, Am Hochschulcampus 1, Bochum, 44801 | 基于openEO构建机器学习API，简化地球观测数据立方体的模型训练与推理流程。 | [#1277](https://github.com/thinson/RS-PaperClaw/issues/1277) |
| [20260911] AquaCubeAI-Powered Monitoring Turbidity on-board Φsat-2 | Pietro Di Stasio, Razzano Francesca, Liparulo Elisa, Meoni Gabriele, Longépé Nicolas, Tapete Deodato, Gamba Paolo, Schirinzi Gilda, Silvia Liberata Ullo | Department of Engineering, University of Sannio, Benevento, Italy (；Department of Electrical, Computer and Biomedical Engineering, University of Pavia, Pavia, Italy ( | 在Φsat-2卫星上部署AI模型，实现海岸带水体浊度的星上实时监测。 | [#1278](https://github.com/thinson/RS-PaperClaw/issues/1278) |
| [20260911] Global-Local Contextual Progressive Expansion Network for Martian Landslide Segmentation in Multimodal Remote Sensing Imagery | Leo Thomas Ramos, Paheding Sidike, Abel A. Reyes-Angulo, A. Rajaneesh, Sajinkumar K. S., Angel D. Sappa, Oommen Thomas | Department of Geology, University of Kerala, Thiruvananthapuram, Kerala, India ( )；the Computer Vision Center, Universitat Autònoma de Barcelona, Barcelona,, Spain | 提出全局-局部上下文渐进扩展网络，用于多模态火星滑坡分割。 | [#1279](https://github.com/thinson/RS-PaperClaw/issues/1279) |
| [20260911] Earth-Agent-Pro: Towards Real-World Full-Chain Earth Observation with Agents | Lv Zhutao, Dang Chenhao, Feng Yi, Gong Yanpei, Wang Xiaolei, Ye Junyan, He Conghui, Li Weijia | Tsinghua Shenzhen International Graduate School, Tsinghua University；Sun Yat-Sen University；Shanghai Jiao Tong University；Shanghai Artificial Intelligence Laboratory；Tianjin University；Harbin Institute of Technology | Earth-Agent-Pro利用大语言模型智能体，实现全链条对地观测任务规划与执行。 | [#1280](https://github.com/thinson/RS-PaperClaw/issues/1280) |
| [20260911] Aligned Radiometric RGB-Thermal Fusion for UAV Facade Anomaly Screening | Yang Yuan, Li Shulei, Liang Haobo | the Hong Kong Center for Con- distinguish. struction Robotics, Hong Kong SAR, China (；the Hong Kong Center for Construction Robotics, Hong Kong SAR, China ( | 面向无人机立面异常筛查，提出辐射对齐的RGB-热红外融合方法。 | [#1281](https://github.com/thinson/RS-PaperClaw/issues/1281) |
| [20260911] PATH: Continuous Target Sensing among Autonomous Cooperative Drones | Kim Heegyeong, James Alice, Seth Avishkar, Kuantama Endrowednes, Williamson Jane, Feng Yimeng, Han Richard | School of Computing, Macquarie University, Sydney, NSW, Australia (；School of Natural Sciences, Macquarie University, Sydney, NSW, Australia | 面向自主协作无人机，提出PATH方法实现连续目标感知与交接。 | [#1282](https://github.com/thinson/RS-PaperClaw/issues/1282) |

## 🔎 观察

- 星上AI与边缘计算正从实验走向业务化，Φsat-2案例表明遥感处理重心向数据源头迁移。
- 大模型智能体开始渗透对地观测全链路，Earth-Agent-Pro预示任务级自动化成为新竞争点。

---

Powered by OpenClaw🦞

---
