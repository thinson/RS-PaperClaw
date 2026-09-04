# Daily Reports

最近三天日报（最新在前）：

# [20260903](./202609/20260903.md)
## 📌 今日概况

今日共检索候选论文 6 篇；关键词+LLM 智能匹配遥感交叉论文 4 篇；最终纳入日报 4 篇。

今日研究聚焦遥感AI与农业、导航及树种的交叉应用。农业方面，利用相机植被指数映射系统估算作物生长，结合RTK-GNSS提升精度。导航领域，提出空地协同的鸟瞰图视觉语言导航方法，增强无人系统协作。树种制图比较了光谱时序特征与地理空间基础模型嵌入的性能。此外，探索了CLIP在多源遥感数据中的潜力，推动多传感器融合与基础模型应用。整体趋势显示，基础模型与多模态数据融合正成为遥感分析的重要方向。

## ✨ 今日亮点

- 农业遥感结合相机与GNSS实现作物生长估算。
- 空地协同导航利用鸟瞰图提升视觉语言理解。
- 基础模型嵌入在树种制图中展现潜力。

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260903] Plant Growth Estimation with a Camera-Based Vegetation Index Mapping System for Agricultural Ground Vehicles | Pindl Lukas, Maier Michael, Oksanen Timo | Professorship for Agrimechatronics, Technical University of Munich；Munich Institute of Robotics and Machine Intelligence (MIRMI) | 基于相机植被指数映射系统，用于农业地面车辆作物生长估算。 | [#1238](https://github.com/thinson/RS-PaperClaw/issues/1238) |
| [20260903] Air-Ground Collaborative Vision-and-Language Navigation via Shared Bird's-Eye Maps | Zhang Shuning, Li Liang, Wang Yunheng, Wang Tao, Kang Yihang, Xu Renjing | the Robotics and Autonomous Systems Thrust, Systems Hub, The Hong Kong University of Science and Technology (Guangzhou), China；School of Communications and Information Engineering, Nanjing University of Posts and Telecommunications, China | 空地协同视觉语言导航，通过共享鸟瞰图实现无人机与地面车协作。 | [#1239](https://github.com/thinson/RS-PaperClaw/issues/1239) |
| [20260903] Tree species mapping in Denmark: A comparison of spectral-temporal features with geospatial foundation model embeddings | Koukos Alkiviadis, Kondylatos Spyros, Nord-Larsen Thomas, Nyborg Lotte, Tøttrup Christian, Grogan Kenneth | EO Centre of Excellence, DHI | 丹麦树种制图比较光谱时序特征与地理空间基础模型嵌入性能。 | [#1240](https://github.com/thinson/RS-PaperClaw/issues/1240) |
| [20260903] Exploring the Potential of Contrastive Language-Image Pre-training for Multi-Source Remote Sensing Data | Miao Xiangyang, Yao Kelu, Huang Yekai, Xu Xiaogang, Xue Junxiao, Shen Minjun, Lv Chenghui, Liu Shanji, Chen Yaying, Li Chao | School of Computer Science and Technology, Zhejiang University；Space-based Computing System Research Center, Zhejiang Lab | 探索CLIP预训练模型在多源遥感数据中的潜力，支持多传感器融合。 | [#1241](https://github.com/thinson/RS-PaperClaw/issues/1241) |

## 🔎 观察

- 基础模型嵌入正逐步替代传统手工特征，提升遥感分类精度。
- 多源数据融合与空地协同成为提升遥感系统自主性的关键趋势。

---

Powered by OpenClaw🦞

---

# [20260902](./202609/20260902.md)
## 📌 今日概况

今日共检索候选论文 12 篇；关键词+LLM 智能匹配遥感交叉论文 6 篇；最终纳入日报 5 篇。

今日研究聚焦遥感图像理解与跨模态应用，涵盖红外车辆检测、SAR超分辨率、多光谱理解、变化检测及热带气旋预测。趋势上，轻量化适配、零样本学习与物理一致性建模成为热点，旨在提升模型泛化能力与物理可靠性。

## ✨ 今日亮点

- 跨域红外车辆检测引入RGB到IR翻译，提升无人机场景泛化。
- SAR超分辨率采用语义原型离散建模，增强物理一致性。
- 零样本多模态气旋预测结合卫星与大气场，拓展预报能力。

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260902] RGB-to-IR image translation for infrared vehicle detection in unseen UAV domains | Thijs A. Eker, Ella P. Fokkinga, Jan Erik van Woerden, Elfi I. S. Hofmeijer, Sebastiaan P. Snel, Schutte Klamer, Friso G. Heslinga | TNO - Intelligent Imaging | 通过RGB到红外图像翻译，提升无人机未知域红外车辆检测性能。 | [#1232](https://github.com/thinson/RS-PaperClaw/issues/1232) |
| [20260902] ProSR: Semantic-Prototype-Guided Discrete Modeling for Physically Consistent SAR Super-Resolution | Kim Byoungwoo, Kim Munchurl | Korea Advanced Institute of Science and Technology, Daejeon, Republic of Korea | 提出语义原型引导的离散建模，实现物理一致的SAR图像超分辨率。 | [#1233](https://github.com/thinson/RS-PaperClaw/issues/1233) |
| [20260902] Lightweight Adaptation of General-Purpose VLMs for Multispectral and SAR Image Understanding | Liu Shanji, Yao Kelu, Xue Junxiao, Lv Chenghui, Miao Xiangyang, Huang Yekai, Chen Yaying, Li Chao | Zhejiang University；Zhejiang Lab | 轻量化适配通用视觉语言模型，用于多光谱与SAR图像理解。 | [#1234](https://github.com/thinson/RS-PaperClaw/issues/1234) |
| [20260902] Progressive Pseudo-Label Optimization for Point-Supervised Change Detection | Ning Hailong, Wang Hao, Wang Yimeng, Lei Tao, Dian Renwei, Asoke K. Nandi | Xi’an University of Posts and Telecommunications；Dalian Maritime University；School of Electronic Information and Artificial Intelligence, Shaanxi University of Science and Technology；School of Robotics, Hunan University；Department of Electronic and Electrical Engineering, Brunel University of London | 渐进式伪标签优化方法，用于点监督的双时相变化检测。 | [#1235](https://github.com/thinson/RS-PaperClaw/issues/1235) |
| [20260902] TC-Next: Zero-Shot Multimodal Cyclone Forecasting | Wang Zhe, Chen Sijie, Luo Yiming, Kim Daehyun, Chang Chien-Yi | Carnegie Mellon University；Seoul National University；Durham University | 零样本多模态深度学习框架，结合卫星与大气场预测热带气旋。 | [#1236](https://github.com/thinson/RS-PaperClaw/issues/1236) |

## ⚠️ 未纳入日报的匹配论文

以下论文通过关键词/LLM 筛选，但在处理过程中失败未纳入日报。点击 arXiv 链接可查看原文。

| 标题 | arXiv | 失败原因 |
|------|-------|----------|
| Genesis: A Generative Engine for Hierarchical Satellite Image Synthesis | [2609.02683v1](https://arxiv.org/abs/2609.02683v1) | 质检未通过: 单位为空或无效 |


## 🔎 观察

- 跨模态翻译与轻量化适配成为提升遥感模型泛化的主流手段。
- 物理一致性建模与零样本学习在遥感应用中日益受到重视。

---

Powered by OpenClaw🦞

---

# [20260901](./202609/20260901.md)
## 📌 今日概况

今日共检索候选论文 15 篇；关键词+LLM 智能匹配遥感交叉论文 9 篇；最终纳入日报 9 篇。

今日遥感AI研究聚焦于多模态与智能体技术，涵盖卫星降水伪影检测、野火分割、高光谱解混、SAR-EO翻译、滑坡理解等应用。同时，多篇工作探索基础模型与视觉语言模型在遥感中的适配与评估，以及事件相机与残差学习在UAV预测中的应用。研究趋势显示，模型正从专用走向通用，强调自适应与推理能力。

## ✨ 今日亮点

- 多篇工作引入视觉语言模型与智能体框架，推动遥感任务自动化。
- 研究关注模型自适应与增量学习，以应对传感器差异与动态环境。
- 基础模型评估与零样本分割成为热点，探索通用遥感智能。

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260901] A Sensor-Adaptive Incremental Learning Framework for Artifact Detection in Satellite Precipitation Data | Andres F. Monsalve, Hernan A. Moreno, Christian D. Kummerow | University of Texas at El Paso, El Paso, TX, overall scores or binary indicators, but do not identify the USA；University of Texas at El Paso, El Paso, TX, USA；Colorado State University, Fort Collins, CO, USA. an image and remain highly limited when adapting to novel | 提出传感器自适应增量学习框架，用于卫星降水数据伪影检测。 | [#1222](https://github.com/thinson/RS-PaperClaw/issues/1222) |
| [20260901] Scale-based Approach for Active Wildfire Segmentation on Satellite Imagery | Matheus F. Kovaleski, Premebida Cristiano, João Ruivo Paulo | ∗ Institute of Systems and Robotics, Department of Electrical and Computer Engineering, University of Coimbra, Portugal；detection and monitoring, recent research has also explored | 基于尺度方法实现主动野火分割，利用卫星多光谱图像。 | [#1223](https://github.com/thinson/RS-PaperClaw/issues/1223) |
| [20260901] Agentic Multimodal Models for Environmental Hyperspectral Unmixing | Cholewa Michał, Ciampi Luca, Messina Nicola, Głomb Przemysław, Amato Giuseppe | IITiS-PAS；ISTI-CNR | 智能体多模态模型用于环境高光谱解混，提取端元。 | [#1224](https://github.com/thinson/RS-PaperClaw/issues/1224) |
| [20260901] ReFlowSET: Representation-Aligned Latent Flow Matching for SAR-to-EO Image Translation | Do Jeonghyeok, Lee Seungchul, Kim Munchurl | KAIST；Stellarvision Inc. | ReFlowSET采用表示对齐潜流匹配，实现SAR到光学图像转换。 | [#1225](https://github.com/thinson/RS-PaperClaw/issues/1225) |
| [20260901] Residual Kalman Dynamics for Event-Based UAV Forecasting | Nyblom Per, Ovrén Hannes, Gustafsson David | Swedish Defence Research Agency (FOI), Linköping, Sweden；Kalman filter over a full center-size box state as a strong physical baseline, and train a residual model to predict acceleration-like corrections | 残差卡尔曼动力学用于事件相机UAV轨迹预测。 | [#1226](https://github.com/thinson/RS-PaperClaw/issues/1226) |
| [20260901] RingMoClaw: An Experience-Inspired Multi-Agent Framework for Self-Evolving Research in Remote Sensing | Kang Kaiyue, He Qixuan, Wang Peijin, Feng Yingchao, Ren Chao, Wang Kangxin, Diao Wenhui, Wang Yixiao, Zhao Liangjin, Wei Kaiwen, Liu Nayu, Sun Xian | Self-Evolving Research in Remote Sensing；toward continuous research driven model evolution in remote The capabilities of large language models (LLMs) in comsensing；Remote sensing earth observation is an essential means Squad [21], and GeoColab [22] extend the scope of agents in；Aerospace Information Research Institute, Chinese Academy of Sciences, cross modal earth observation reasoning, procedural knowl-；Beijing 100190, China, also with the School of Electronic, Electrical and；Communication Engineering, University of Chinese Academy of Sciences；Beijing 100190, China, also with the University of Chinese Academy of Sci- management, and strengthen the reasoning and scheduling；Research Institute, Chinese Academy of Sciences, Beijing 100190, China. upon the OpenClaw research agent paradigm [25], OpenEarth-；Aerospace Information Research Institute, Chinese Academy of Sciences, and enables agents to dynamically generate dedicated tools for；Beijing 100190, China, and also with the National Key Laboratory of | RingMoClaw多智能体框架驱动遥感自进化研究。 | [#1227](https://github.com/thinson/RS-PaperClaw/issues/1227) |
| [20260901] EarthLD: Towards Unified Open-World Landslide Understanding via Vision-Language Guided Diffusion Models | Su Yuanchao, Gao Lianru, Jiang Mengying, Chen Jiangyi, Cheng Jiaxin, Zhou Yicong | Department of Computer and Information Science, University of Macau, Macao 999078, China；College of Geomatics, Xi’an University of Science and Technology, Xi’an 710054, China | EarthLD利用视觉语言引导扩散模型实现开放世界滑坡理解。 | [#1228](https://github.com/thinson/RS-PaperClaw/issues/1228) |
| [20260901] Do Satellites See Commuters? A Critical Benchmark of Vision Foundation Models | Ashiq Shukoor Iqbal, Wongso Wilson, Flora D. Salim | University of New South Wales Sydney NSW Australia | 基准测试评估视觉基础模型在通勤起讫点识别中的能力。 | [#1229](https://github.com/thinson/RS-PaperClaw/issues/1229) |
| [20260901] Restrict, Don't Retrain: Inference-Time VLM Guidance for Zero-Shot Aerial Segmentation | DiMeola Teresa, Walter Charles, Xiao Hong | University of Mississippi | 推理时视觉语言模型引导实现零样本航空影像分割。 | [#1230](https://github.com/thinson/RS-PaperClaw/issues/1230) |

## 🔎 观察

- 视觉语言模型与扩散模型正加速渗透遥感解译，但评估基准尚缺。
- 智能体框架与增量学习成为应对数据动态性和传感器差异的关键。

---

Powered by OpenClaw🦞

---
