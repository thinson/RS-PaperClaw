# Daily Reports

最近三天日报（最新在前）：

# [20260331](./202603/20260331.md)
## 📌 今日概况

今日共检索候选论文 15 篇；关键词+LLM 智能匹配遥感交叉论文 6 篇；最终纳入日报 6 篇。

今日遥感AI研究呈现多模态融合与开放词汇理解两大主线。视觉-语言模型持续向地球观测领域渗透，涵盖图文数据集构建、跨模态检索及零样本分割等方向。同时，层次化多标签分类、高光谱解混等传统任务借助图网络与几何方法获得新进展，卫星单目深度估计等实用技术亦有新数据集发布。

## ✨ 今日亮点

- BigEarthNet.txt发布大规模多传感器图文数据集，填补遥感视觉-语言基准空白
- ConInfer提出无需训练的上下文感知推理框架，推动开放词汇遥感分割实用化
- EarthEmbeddingExplorer上线全球卫星影像跨模态检索平台，降低基础模型应用门槛

## 🗂 今日文章列表

| 标题 | 作者 | 一句话概括 | Issue |
|---|---|---|---|
| [20260331] MAPLE: Multi-Path Adaptive Propagation with Level-Aware Embeddings for Hierarchical Multi-Label Image Classification | Koloski Boshko, Stoimchev Marjan, Levatić Jurica, Kocev Dragi, Džeroski Sašo | MAPLE通过层级感知嵌入与自适应图传播，解决遥感图像层次多标签分类中的标签稀疏与语义关联问题。 | [#233](https://github.com/thinson/RS-PaperClaw/issues/233) |
| [20260331] BigEarthNet.txt: A Large-Scale Multi-Sensor Image-Text Dataset and Benchmark for Earth Observation | Herzog Johann-Ludwig, Mathis Jürgen Adler, Hackel Leonard, Shu Yan, Zavras Angelos et al. | BigEarthNet.txt整合Sentinel-1/2双模态数据与人工校验文本描述，构建百万级遥感图文对齐基准。 | [#234](https://github.com/thinson/RS-PaperClaw/issues/234) |
| [20260331] EarthEmbeddingExplorer: A Web Application for Cross-Modal Retrieval of Global Satellite Images | Zheng Yijie, Wu Weijie, Wu Bingyue, Zhao Long, Li Guoqing et al. | EarthEmbeddingExplorer基于基础模型嵌入空间，实现文本-图像双向检索的交互式Web应用。 | [#235](https://github.com/thinson/RS-PaperClaw/issues/235) |
| [20260331] Polyhedral Unmixing: Bridging Semantic Segmentation with Hyperspectral Unmixing via Polyhedral-Cone Partitioning | Bottenmuller Antoine, Decencière Etienne, Dokládal Petr | Polyhedral Unmixing将多面体锥划分引入高光谱解混，建立语义分割与端元提取的统一几何框架。 | [#236](https://github.com/thinson/RS-PaperClaw/issues/236) |
| [20260331] ConInfer: Context-Aware Inference for Training-Free Open-Vocabulary Remote Sensing Segmentation | Chen Wenyang, Hu Zhanxuan, Zhang Yaping, Ning Hailong, Tai Yonghang | ConInfer利用CLIP上下文感知推理机制，无需微调即可实现遥感开放词汇语义分割。 | [#237](https://github.com/thinson/RS-PaperClaw/issues/237) |
| [20260331] Monocular Building Height Estimation from PhiSat-2 Imagery: Dataset and Method | Song Yanjiao, Cai Bowen, Balz Timo, Shao Zhenfeng, Neema Simon Sumari et al. | 基于PhiSat-2卫星影像构建单目建筑高度估计数据集，支撑城市形态学定量分析。 | [#238](https://github.com/thinson/RS-PaperClaw/issues/238) |

## 🔎 观察

- 视觉-语言基础模型正加速重塑遥感下游任务范式，但领域适配性与推理效率仍是落地瓶颈
- 多模态数据集的文本质量与传感器异质性对齐，将成为决定模型泛化能力的关键变量

---

Powered by OpenClaw🦞

---

# [20260330](./202603/20260330.md)
## 📌 今日概况

今日共检索候选论文 10 篇；关键词+LLM 智能匹配遥感交叉论文 5 篇；最终纳入日报 5 篇。

今日遥感AI研究呈现多维度交叉趋势：生成模型向显著性检测渗透，ORSIFlow将矫正流与潜扩散结合提升光学遥感目标检测精度；硬件层面，自旋三旋翼无人机通过非线性动态逆控制扩展视场；数据基建方面，PROSAIL驱动的合成高光谱植被数据集填补基准空白；多模态检索与无线通信信道推断则体现遥感向跨域应用的延伸。

## ✨ 今日亮点

- ORSIFlow首次将矫正流引入遥感显著性检测，以显著性引导生成机制优化边界感知
- 自旋三旋翼无人机采用模型预测控制与非线性动态逆，实现360°视场自主飞行
- SVH-BD基于PROSAIL辐射传输模型构建合成高光谱植被基准，支持遥感图像仿真

## 🗂 今日文章列表

| 标题 | 作者 | 一句话概括 | Issue |
|---|---|---|---|
| [20260330] ORSIFlow: Saliency-Guided Rectified Flow for Optical Remote Sensing Salient Object Detection | Chen Haojing, Li Yutong, Liu Zhihang, Tan Tao, Bian Haoyu et al. | ORSIFlow提出显著性引导矫正流，结合潜扩散模型与边界感知损失，优化光学遥感显著目标检测的生成质量与效率。 | [#225](https://github.com/thinson/RS-PaperClaw/issues/225) |
| [20260330] A Self-Rotating Tri-Rotor UAV for Field of View Expansion and Autonomous Flight | Zhou Xiaobin, Zheng Zihao, Jin Aoxu, Qiang Lei, Zhu Bo | 自旋三旋翼无人机通过模型预测控制与非线性动态逆实现自主飞行，以机械旋转扩展视场突破固定相机视角限制。 | [#226](https://github.com/thinson/RS-PaperClaw/issues/226) |
| [20260330] SVH-BD : Synthetic Vegetation Hyperspectral Benchmark Dataset for Emulation of Remote Sensing Images | Chedly Ben Azizi, Guilloteau Claire, Roussel Gilles, Puigt Matthieu | SVH-BD基于PROSAIL辐射传输模型生成合成高光谱植被数据，为遥感图像仿真与植被性状反演提供标准化基准。 | [#227](https://github.com/thinson/RS-PaperClaw/issues/227) |
| [20260330] Robust Remote Sensing Image-Text Retrieval with Noisy Correspondence | Song Qiya, Xie Yiqiang, Sun Yuan, Dian Renwei, Kang Xudong | 针对遥感图文检索中的噪声对应问题，提出自步课程学习策略，逐步过滤噪声样本以提升跨模态检索鲁棒性。 | [#228](https://github.com/thinson/RS-PaperClaw/issues/228) |
| [20260330] Deep Learning Based Site-Specific Channel Inference Using Satellite Images | Song Junzhe, He Ruisi, Yang Mi, Zhang Zhengyu, Gao Shuaiqi et al. | 利用卫星图像与深度学习进行站点级无线信道推断，构建抽头延迟线模型辅助通信网络规划与频谱管理。 | [#229](https://github.com/thinson/RS-PaperClaw/issues/229) |

## 🔎 观察

- 生成式AI正从图像合成向判别任务回流，矫正流等高效生成模型开始服务于检测任务的特征增强与边界精细化
- 遥感硬件创新与算法研究呈现并行态势，无人机平台动力学控制与上层视觉任务形成系统级闭环，但跨层协同优化尚待深入

---

Powered by OpenClaw🦞

---

# [20260329](./202603/20260329.md)
## 📌 今日概况

今日共检索候选论文 9 篇；关键词+LLM 智能匹配遥感交叉论文 5 篇；最终纳入日报 5 篇。

今日遥感AI研究呈现多模态融合与智能体应用趋势。大语言模型成为核心驱动力，赋能地理定位、变化检测、语义分割及无人机导航等任务。物理知识嵌入与开放词汇学习成为新方向，同时深度学习结合卫星影像持续支撑社会经济分析应用。

## ✨ 今日亮点

- RHO提出基于OSM的全景图像度量级跨视角地理定位方法
- OpenDPR通过扩散引导原型检索实现遥感开放词汇变化检测
- LLM驱动无人机自然语言导航，结合时序逻辑规范翻译与修复

## 🗂 今日文章列表

| 标题 | 作者 | 一句话概括 | Issue |
|---|---|---|---|
| [20260329] RHO: Robust Holistic OSM-Based Metric Cross-View Geo-Localization | Zheng Junwei, Dai Ruize, Liu Ruiping, Zeng Zichao, Chen Yufan et al. | RHO利用OpenStreetMap数据实现鲁棒的全景图像跨视角度量地理定位，提升视觉定位精度。 | [#219](https://github.com/thinson/RS-PaperClaw/issues/219) |
| [20260329] OpenDPR: Open-Vocabulary Change Detection via Vision-Centric Diffusion-Guided Prototype Retrieval for Remote Sensing Imagery | Guo Qi, Wang Jue, Liu Yinhe, Zhong Yanfei | OpenDPR提出以视觉为中心的扩散引导原型检索框架，支持遥感影像的开放词汇变化检测。 | [#220](https://github.com/thinson/RS-PaperClaw/issues/220) |
| [20260329] LLM-Enabled Low-Altitude UAV Natural Language Navigation via Signal Temporal Logic Specification Translation and Repair | Ping Yuqi, Ding Huahao, Liang Tianhao, Zhou Longyu, Lei Guangyu et al. | 该方法将大语言模型用于低空无人机自然语言导航指令的时序逻辑规范翻译与自动修复。 | [#221](https://github.com/thinson/RS-PaperClaw/issues/221) |
| [20260329] Transferring Physical Priors into Remote Sensing Segmentation via Large Language Models | Lu Yuxi, Li Kunqi, Li Zhidong, Su Xiaohan, Wu Biao et al. | 通过大语言模型将物理先验知识转化为知识图谱，增强遥感语义分割的物理可解释性。 | [#222](https://github.com/thinson/RS-PaperClaw/issues/222) |
| [20260329] Estimating the Impact of COVID-19 on Travel Demand in Houston Area Using Deep Learning and Satellite Imagery | Pachika Alekhya, Gao Lu, Song Lingguang, Lu Pan, Wang Xingju | 结合深度学习与卫星影像，量化评估COVID-19对休斯顿地区出行需求的影响。 | [#223](https://github.com/thinson/RS-PaperClaw/issues/223) |

## 🔎 观察

- 大语言模型正从通用工具向遥感专用智能体演进，覆盖感知-认知-决策全链条。
- 开放词汇与物理先验的结合，反映出遥感AI从数据驱动向知识增强的范式转变。

---

Powered by OpenClaw🦞

---
