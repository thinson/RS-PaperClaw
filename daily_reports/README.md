# Daily Reports

最近三天日报（最新在前）：

# [20260716](./202607/20260716.md)
## 📌 今日概况

今日共检索候选论文 9 篇；关键词+LLM 智能匹配遥感交叉论文 5 篇；最终纳入日报 5 篇。

今日遥感AI研究聚焦于无人机（UAV）感知与跟踪、高光谱图像分类及可解释性分析。多篇工作引入物理引导、生成学习或视觉-语言-动作模型，提升动态环境下的感知鲁棒性。此外，针对SAR图像洪水检测的xAI方法比较研究也受到关注，体现了模型透明性与物理先验融合的趋势。

## ✨ 今日亮点

- 物理引导图扩散网络提升高光谱分类精度
- 视觉-语言-动作模型增强无人机空间感知
- 事件相机与频域跟踪实现实时空对空追踪

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260716] DAPGNet: Dynamic Adaptive Physics-Guided Graph Diffusion Network for Hyperspectral Image Classification | Wang Pengkun, Cao Weijia, Wang Ning, Yang Xiaofei | the National Engineering Laboratory for Satellite Remote Sensing Applications, Aerospace Information Research Institute, Chinese Academy of Sciences, Beijing, China；University of Chinese Academy of Sciences, Beijing, China (；the Aerospace Information Research Institute, Chinese Academy of Sciences, Beijing, China (；the National Engineering Laboratory for Satellite Remote Sensing Applications, Aerospace Information Research Institute, Chinese Academy of Sciences, Beijing, China (；Guangzhou University, Guangzhou, China ( | 提出动态自适应物理引导图扩散网络，用于高光谱图像分类。 | [#912](https://github.com/thinson/RS-PaperClaw/issues/912) |
| [20260716] CosFly-VLA: A Spatially Aware Vision-Language-Action Model for UAV Tracking | Ren Ruilong, Cheng Songsheng, Zhou Yunpeng, Chen Hanxuan, Wang Xiangyue, Zeng Tianle, Yuan Shuai, Li Binbo, Guo Hanzhong, Pei Ji, Zhang Da, Wang Kangli | Northeast Normal University；Southern University of Science and Technology；Peking University；University of Hong Kong | CosFly-VLA模型融合空间感知与视觉-语言-动作，用于无人机跟踪。 | [#913](https://github.com/thinson/RS-PaperClaw/issues/913) |
| [20260716] Conditional Generative Learning Enabled Wireless UAV Sensing and Tracking via Point Cloud Imaging | Dai Xinhong, Gao Yuan, Jiang Hao, Yuan Xiaojun, Wang Xin | Key Laboratory for Information Science of Electromagnetic Waves (MoE), College of Future Information Technology, Fudan University, Shanghai, China. (；the National Key Laboratory of Wireless Communications, the University of Electronic Science and Technology of China, Chengdu, China ( | 条件生成学习结合点云成像实现无线无人机感知与跟踪。 | [#914](https://github.com/thinson/RS-PaperClaw/issues/914) |
| [20260716] On the Disagreement in Perturbation-based xAI -- Benchmarking Perturbation Choices for Flood Detection from SAR Images | Schlegel Anastasia, Hänsch Ronny | a Microwaves and Radar Institute, German Aerospace Center (DLR), Weßling, 82234, Germany；b Chair of Remote Sensing Technology, Department of Aerospace and Geodesy, Technical University of Munich, Munich, 80333, Germany；In response to this need for transparency, research on ex- | 基准测试扰动选择对SAR图像洪水检测中xAI方法的影响。 | [#915](https://github.com/thinson/RS-PaperClaw/issues/915) |
| [20260716] AE-UAV: An Air-to-Air Event-Based UAV Tracking Benchmark and a Real-Time Frequency-Domain Tracker | Jiang Zixin, He Bing, Xiong Chaoran, Wang Zhenzhen, Zhao Xin, Pei Ling | Department of Electronic Engineering, Rocket Force University of Engineering, Xi’an, China (；Shanghai Key Laboratory of Navigation and Location Based Services, Shanghai Jiao Tong University, Shanghai, China (；State Key Laboratory of Submarine Geoscience, School of Automation and Intelligent Sensing, Shanghai Jiao Tong University, Shanghai, China | 发布空对空事件相机无人机跟踪基准及实时频域跟踪器。 | [#916](https://github.com/thinson/RS-PaperClaw/issues/916) |

## 🔎 观察

- 无人机感知领域正从单一视觉向多模态融合（语言、事件、电磁）演进。
- 物理先验与可解释性方法在遥感任务中应用增多，提升模型可信度。

---

Powered by OpenClaw🦞

---

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
