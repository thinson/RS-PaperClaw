# Daily Reports

最近三天日报（最新在前）：

# [20260715](./202607/20260715.md)
## 📌 今日概况

今日共检索候选论文 13 篇；关键词+LLM 智能匹配遥感交叉论文 5 篇；最终纳入日报 4 篇。

今日遥感AI研究聚焦于无人机自主导航与多模态感知、云感知地球观测及北极海冰监测。AeroMap3D提出基于视觉-几何-语义地图先验的单目6-DoF定位方法，解决GNSS拒止环境问题；M3F-UAV构建低空无线传感缺失模态多模态基础模型；RoughNet利用扩散超分辨率技术绘制海冰粗糙度图，提升气候监测能力。

## ✨ 今日亮点

- 无人机单目定位结合地图先验，突破GNSS拒止限制
- 低空无线传感缺失模态融合基础模型
- 扩散模型超分辨率用于北极海冰粗糙度制图

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260715] AeroMap3D: Anchoring Monocular UAV 6-DoF Localization to Visual-Geometric-Semantic Map Priors | Deng Zhiyun, Sentis Luis | University of Texas at Austin | AeroMap3D利用视觉-几何-语义地图先验实现无人机单目6-DoF定位 | [#899](https://github.com/thinson/RS-PaperClaw/issues/899) |
| [20260715] M3F-UAV: A Missing-Modality Multimodal Foundation Model for Low-Altitude Wireless Sensing | Gao Pengxuan, Ying Kai, Wu Botao, Mo Jianhua, Wen Qingsong | School of Electronic Information and Electrical Engineering, Shanghai Jiao Tong University, Shanghai, China ( | M3F-UAV提出缺失模态多模态基础模型用于低空无线传感 | [#900](https://github.com/thinson/RS-PaperClaw/issues/900) |
| [20260715] From Surface Forecasting to Observability Forecasting: A Latent World Model for Cloud-Aware EO Monitoring | Albughdadi Mohanad | European Centre for Medium-Range Weather Forecasts | LeWorldModel实现从地表到可观测性的云感知预报 | [#901](https://github.com/thinson/RS-PaperClaw/issues/901) |
| [20260715] RoughNet: Mapping Arctic Sea Ice Roughness Using Diffusion-Based Super-Resolution of Satellite Imagery | Cannon Tessa, Tsamados Michel, Manescu Petru, Newman Thomas, Haas Christian, Helm Veit, Chen Weibin, Scharien Randall | Department of Computer Science, University College London；Department of Earth Sciences, University College London；Alfred Wegener Institute Helmholtz Centre for Polar and；Marine Research, Bremerhaven, Germany；Department of Geography, University of Victoria | RoughNet基于扩散超分辨率卫星影像绘制海冰粗糙度图 | [#902](https://github.com/thinson/RS-PaperClaw/issues/902) |

## ⚠️ 未纳入日报的匹配论文

以下论文通过关键词/LLM 筛选，但在处理过程中失败未纳入日报。点击 arXiv 链接可查看原文。

| 标题 | arXiv | 失败原因 |
|------|-------|----------|
| Minimax Theory of Likelihood-Based Deep Learning for Speckle Regression | [2607.14064v1](https://arxiv.org/abs/2607.14064v1) | 质检未通过: 单位为空或无效 |


## 🔎 观察

- 无人机定位研究正从纯视觉向多模态地图先验融合演进
- 扩散模型在遥感超分辨率应用中展现出对复杂纹理的建模优势

---

Powered by OpenClaw🦞

---

# [20260714](./202607/20260714.md)
## 📌 今日概况

今日共检索候选论文 15 篇；关键词+LLM 智能匹配遥感交叉论文 8 篇；最终纳入日报 8 篇。

今日遥感AI研究聚焦于领域增量学习、基础模型微调与弱监督分析三大方向。多篇工作关注模型在变化检测、高光谱分类及场景理解中的泛化能力，同时涌现出针对无人机自主导航与空间认知的端到端优化及基准测试，体现了从算法到系统集成的趋势。

## ✨ 今日亮点

- 提出差异引导与频率解耦蒸馏的域增量变化检测方法
- 多分支高效微调框架用于高光谱基础模型分类
- 发布无人机具身智能自我意识与空间认知基准

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260714] Domain-Incremental Remote Sensing Change Detection via Difference-Guided Adaptation and Frequency-Decoupled Distillation | Peng Daifeng, Li Yaning, Guan Haiyan | School of Remote Sensing and Geomatics Engineering, Nanjing University of Information Science and Technology, Nanjing 210044, China | 提出差异引导适应与频率解耦蒸馏，缓解遥感变化检测中的灾难性遗忘 | [#904](https://github.com/thinson/RS-PaperClaw/issues/904) |
| [20260714] MBTI: A Multi-Branch Efficient Fine-Tuning Framework for Hyperspectral Image Classification with Foundation Models | Xu Mingzhen, Guo Haonan, Wang Di, Qu Yinghua, Zhou Zhiliang, Zhang Lei, Yao Huiwen, Zhao Rui, Wang Fengxiang, Wan Gang, Du Bo, Zhang Liangpei | School of Computer Science, Wuhan University, Wuhan, China. (；State Key Laboratory of Information Engineering in Surveying, Mapping and Remote Sensing, Wuhan University, Wuhan, China. (；Hebei Key Laboratory of Underground Energy Storage Technology, Langfang, China. (；the Faculty of Electrical Engineering and Computer Science, Ningbo University, Ningbo, China. (；College of Computer Science and Technology, National University of Defense Technology, Changsha, China. (；School of Aerospace Information, Space Engineering University, Beijing, China；the Key Laboratory of Intelligent Processing and Application Technology of Satellite Information, Beijing, China ( | 多分支框架高效微调基础模型，提升高光谱图像分类性能 | [#905](https://github.com/thinson/RS-PaperClaw/issues/905) |
| [20260714] Weakly Supervised Spatio-Temporal Candidate Discovery of Dairy Farm Sites from Seasonal Satellite Imagery | Haider Usman, Khalid Fatima, Mason Karl | School of Computer Science, University of Galway, Ireland；Faculty of Computer Science and Engineering, GIK Institute of Engineering Sciences and Technology, Pakistan | 弱监督方法利用季节性卫星影像发现奶牛场候选位置 | [#906](https://github.com/thinson/RS-PaperClaw/issues/906) |
| [20260714] Label-Decoupled Style Augmentation for Domain Generalization in Multi-Label Remote Sensing Scene Classification | Almouradi Alaa, Aptoula Erchan | Faculty of Engineering and Natural Sciences, Sabancı University | 标签解耦风格增强提升多标签遥感场景分类的域泛化能力 | [#907](https://github.com/thinson/RS-PaperClaw/issues/907) |
| [20260714] Improving Autonomous Nano-drones Performance via Automated End-to-End Optimization and Deployment of DNNs | Niculescu Vlad, Lamberti Lorenzo, Conti Francesco, Benini Luca, Palossi Daniele | Integrated Systems Laboratory - ETH Zürich, Switzerland；Department of Electrical, Electronic and Information Engineering - University of Bologna, Italy；Dalle Molle Institute for Artificial Intelligence - USI-SUPSI, Switzerland | 自动化端到端优化与部署DNN，提升自主纳米无人机性能 | [#908](https://github.com/thinson/RS-PaperClaw/issues/908) |
| [20260714] Edge-Aware Thermal Infrared UAV Swarm Tracking | Chen Yu-Hsi | University of Melbourne | 边缘感知卡尔曼滤波实现热红外无人机群实时跟踪 | [#909](https://github.com/thinson/RS-PaperClaw/issues/909) |
| [20260714] TerraLogic: A Benchmark for Hierarchical Geospatial Reasoning in Earth Observation | Yan Yuhang, Mou Linchao, Yang Bokang, Li Qingyu | The Chinese University of Hong Kong (Shenzhen) China；Technical University of Munich Germany | TerraLogic基准测试大语言模型在地理空间层次推理能力 | [#910](https://github.com/thinson/RS-PaperClaw/issues/910) |
| [20260714] Self in Space: Benchmarking Self-Awareness and Spatial Cognition in UAV Embodied Intelligence | Zou Zhishan, Sun Guoyan, Wei Zhiwei, Pan Jiancheng, Li Yujie, Peng Mugen, Xu Wenjia | Beijing University of Posts and Telecommunications；Hunan Normal University；Tsinghua University | Self in Space基准评估多模态大模型在无人机中的自我意识与空间认知 | [#911](https://github.com/thinson/RS-PaperClaw/issues/911) |

## 🔎 观察

- 域泛化与增量学习成为遥感模型部署的核心挑战，多篇工作从特征解耦角度提出解决方案
- 无人机智能体研究从单一跟踪向具身认知演进，基准测试推动多模态大模型在边缘设备落地

---

Powered by OpenClaw🦞

---

# [20260713](./202607/20260713.md)
## 📌 今日概况

今日共检索候选论文 12 篇；关键词+LLM 智能匹配遥感交叉论文 7 篇；最终纳入日报 7 篇。

今日遥感AI研究聚焦于无人机（UAV）的智能导航与安全控制，涵盖多模态人机意图调解、训练-free视觉对话导航及室内集群协同。同时，灾害响应中的建筑损伤快速评估、自监督学习在高分辨率多光谱影像中的应用，以及基于事件相机的异步目标检测与跟踪也取得进展。此外，地球观测回归任务的不确定性量化研究为建筑高度、树冠高度及生物量估算提供了新方法。

## ✨ 今日亮点

- 无人机安全控制与多模态意图调解模型
- 训练-free空中视觉对话导航方法
- 基于事件相机的异步UAV检测与跟踪

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260713] HASTE: A Platform for Rapid Post-Disaster Building Damage Assessment | Robinson Caleb, Ortiz Anthony, Simone Fobi Nsutezo, Birge Cameron, Machado Meygha, Duarte Marcelo, Joaquin Rivero Rodriguez, Anthony Cintron Roman, White Kevin, Becker-Reshef Inbal, Juan M. Lavista Ferres | AI for Good Lab；Microsoft AI for Good Research Lab | HASTE平台实现灾后建筑损伤快速评估，基于卫星影像与机器学习。 | [#890](https://github.com/thinson/RS-PaperClaw/issues/890) |
| [20260713] A Model for Mediating Multi-Modal Human Intent into Safe Maneuvers for UAVs | Nelson Sofia, Alrajeh Dalal, Pedro Antonio Alarcon Granadeno, Cleland-Huang Jane | University of Notre Dame；Imperial College London | 提出多模态人机意图调解模型，保障无人机安全机动。 | [#891](https://github.com/thinson/RS-PaperClaw/issues/891) |
| [20260713] Parse, Search, and Confirmation: Training-Free Aerial Vision-and-Dialog Navigation with Chain-of-Thought Reasoning and Structured Spatial Memory | Qi Yu, Li Hongyu, Huang Shaofei, Hui Tianrui, Wang Yaxiong, Cheng Lechao, Zhong Zhun, Liu Si, Wang Meng | School of Computer Science and Information Engineering, Hefei University of Technology；Jianghuai Advance Technology Center；Anhui Provincial Key Laboratory of Humanoid Robots；School of Artificial Intelligence, Beihang University；University of Macau | 训练-free空中视觉对话导航，结合链式推理与空间记忆。 | [#892](https://github.com/thinson/RS-PaperClaw/issues/892) |
| [20260713] Uncertainty Quantification for EO Regression Tasks: Building Height, Tree Canopy Height and Above-ground Biomass Estimation | Yadav Ritu, Nascetti Andrea, Ban Yifang | Division of Geoinformatics, KTH Royal Institute of Technology, Sweden. ( | 量化EO回归任务不确定性，提升建筑与植被高度估算可靠性。 | [#893](https://github.com/thinson/RS-PaperClaw/issues/893) |
| [20260713] From Sketch Prior to Trajectories: A Mission-Oriented Coordinated Navigation Framework for Indoor UAV Swarm | Xu Xinhang, Liu Ruiyang, Jin Haotian, Wang Yi, Shen Hongming, Li Jianping, Xie Lihua | School of Electrical and Electronic Engineering, Nanyang Technological University, 50 Nanyang Avenue, Singapore | 基于草图先验的室内无人机集群任务导向协同导航框架。 | [#894](https://github.com/thinson/RS-PaperClaw/issues/894) |
| [20260713] Self-supervised training for high-resolution close-range multispectral remote sensing imagery | Thomas Leon-Friedrich, Änäkkälä Mikael, Lajunen Antti | funded by Helsinki University Library.” | 自监督训练用于高分辨率近距多光谱遥感影像语义分割。 | [#895](https://github.com/thinson/RS-PaperClaw/issues/895) |
| [20260713] ASUMOT: Motion-Consistency-Based Asynchronous UAV Detection and Tracking with Event Cameras | Jia Baofeng, Chen Xiaoyu, Zhang Jingyuan, Wu Zongze, li Haochen, Han Jing, Bai Lianfa | State key Laboratory of Extreme Environment Optoelectronic Dynamic Testing Technology and Instrument, Nanjing；University of Science and Technology, Nanjing 210094, China；Jiangsu Key Laboratory of Visual Sensing and Intelligent Perception, Nanjing University of Science and Technology, Nanjing | ASUMOT利用事件相机实现运动一致性驱动的异步UAV检测跟踪。 | [#896](https://github.com/thinson/RS-PaperClaw/issues/896) |

## 🔎 观察

- 无人机自主性与安全性研究成为热点，多模态交互与协同导航技术并行发展。
- 自监督与不确定性量化方法在遥感应用中日益重要，推动模型鲁棒性与实用性提升。

---

Powered by OpenClaw🦞

---
