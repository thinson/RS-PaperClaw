# Daily Reports

最近三天日报（最新在前）：

# [20260921](./202609/20260921.md)
## 📌 今日概况

今日共检索候选论文 11 篇；关键词+LLM 智能匹配遥感交叉论文 3 篇；最终纳入日报 3 篇。

今日研究趋势聚焦于遥感领域的轻量化、基础模型与跨模态定位。三篇论文分别针对SAR舰船检测的模型压缩、森林点云的基础模型构建以及基于音频的无人机定位，体现了从专用检测到通用表征、从视觉到多模态融合的演进。其中知识蒸馏与剪枝结合、自监督学习用于点云、强化学习处理时序对应，均反映了提升效率与泛化能力的共同目标。

## ✨ 今日亮点

- DTKDP框架结合双教师蒸馏与剪枝，实现轻量SAR舰船检测。
- 森林点云基础模型探索自监督学习与语义分割。
- 音频无人机定位引入强化学习实现自适应时序对应。

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260921] DTKDP: A Dual Teacher Knowledge Distillation and Pruning Framework for Lightweight Oriented SAR Ship Detection | Li Yuming, Zhang Fan, Alin M. Achim | Visual Information Labs, University of Bristol, Bristol BS1 | 提出双教师知识蒸馏与剪枝框架，用于轻量化定向SAR舰船检测。 | [#1325](https://github.com/thinson/RS-PaperClaw/issues/1325) |
| [20260921] Toward a foundation model for forest point clouds | Yue Yuanwen, Puliti Stefano, Robert Damien, Topaloğlu Atakan, Xiang Binbin, Wielgosz Maciej, Jan Dirk Wegner, Astrup Rasmus, Rupprecht Christian, Schindler Konrad | University of Oxford；Norwegian Institute of Bioeconomy Research (NIBIO)；University of Zurich | 探索森林点云基础模型，结合自监督学习与语义分割。 | [#1326](https://github.com/thinson/RS-PaperClaw/issues/1326) |
| [20260921] Audio-based UAV Localization with Adaptive Temporal Correspondence via Reinforcement Learning | Lei Haoxiang, Feng Mingzheng, Wang Daotong, Yuan Shenghai | at the window center to reduce motion-induced mismatch | 利用强化学习实现音频无人机定位中的自适应时序对应。 | [#1327](https://github.com/thinson/RS-PaperClaw/issues/1327) |

## 🔎 观察

- 轻量化与基础模型并行发展，分别应对边缘部署与通用表征需求。
- 多模态与自监督方法正渗透至遥感细分任务，提升鲁棒性。

---

Powered by OpenClaw🦞

---

# [20260920](./202609/20260920.md)
## 📌 今日概况

今日共检索候选论文 10 篇；关键词+LLM 智能匹配遥感交叉论文 4 篇；最终纳入日报 4 篇。

今日四篇论文覆盖贫困制图、火烧迹地制图、多光谱波段选择与视觉基础模型评测。整体趋势显示，遥感AI正从单纯提升精度转向面向决策的评估、多时相数据构建、成像链路优化以及退化条件下的鲁棒性基准测试。其中，社会应用与模型可靠性成为共同关注点，数据集和评测框架类工作占据主导。

## ✨ 今日亮点

- 贫困制图引入决策中心评估，强调模型对下游决策的实际影响
- 巴西塞拉多构建多时相火烧迹地数据集，服务区域监测
- RSPDBench面向物理退化评测视觉基础模型，关注鲁棒性

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260920] Decision-Centered Evaluation of Machine Learning Poverty Maps Using Mobile Phone and Satellite Data | Algama Chanuka, Chandana Merl, Dias Viren, Amarasinghe Kasun | Carnegie Mellon University | 结合手机与卫星数据，以决策为中心评估机器学习贫困地图的实际效用。 | [#1320](https://github.com/thinson/RS-PaperClaw/issues/1320) |
| [20260920] A multi-temporal dataset for mapping burned areas in the Brazilian Cerrado using time series of remote sensing imagery | Alisson Cleiton de Oliveira, Thales Sehn Körting | Earth Observation and Geoinformatics Division (DIOTG), National Institute for Space；Research (INPE), São José dos Campos, SP, Brazil；Geoinformatics Division (DIOTG), National Institute for Space Research (INPE), São José dos | 基于遥感时间序列构建巴西塞拉多火烧迹地多时相数据集，并采用随机森林制图。 | [#1321](https://github.com/thinson/RS-PaperClaw/issues/1321) |
| [20260920] HIERARCHICAL FILTER BAND SELECTION FOR MULTISPECTRAL OBJECT CLASSIFICATION | Kossira Katja, Seiler Jürgen, Kaup André | Friedrich-Alexander-Universität Erlangen-Nürnberg | 提出层次化滤波波段选择方法，用于多光谱目标分类并优化图像采集。 | [#1322](https://github.com/thinson/RS-PaperClaw/issues/1322) |
| [20260920] RSPDBench: Benchmarking Vision Foundation Models on Earth Observation Tasks Under Physically Grounded Remote-Sensing Product Degradations | Tanjim Bin Faruk, Khondaker Masfiq Reza, Pallickara Shrideep, Sangmi Lee Pallickara | Colorado State University | 构建RSPDBench，在物理退化条件下评测视觉基础模型的地球观测任务表现。 | [#1323](https://github.com/thinson/RS-PaperClaw/issues/1323) |

## 🔎 观察

- 评测类工作从精度指标转向决策效用与物理退化鲁棒性，反映应用导向增强。
- 多时相数据集与波段选择研究并行，说明数据构建和成像链路优化仍受重视。

---

Powered by OpenClaw🦞

---

# [20260919](./202609/20260919.md)
## 📌 今日概况

今日共检索候选论文 6 篇；关键词+LLM 智能匹配遥感交叉论文 3 篇；最终纳入日报 2 篇。

今日两篇论文聚焦无人机遥感感知与重建。一篇面向无人机小目标检测，将状态空间建模与YOLO框架结合，引入自适应空间语义注意力融合与多尺度特征聚合，以提升效率与精度；另一篇针对航空大场景重建，提出可见性驱动的3D高斯泼溅方法，优化大规模场景下的表示与渲染。整体趋势显示，Mamba/状态空间模型与3D高斯泼溅正加速向遥感任务渗透，强调效率、尺度适应与几何一致性。

## ✨ 今日亮点

- 状态空间模型与YOLO结合，提升无人机小目标检测效率
- 可见性驱动3D高斯泼溅，面向航空大场景重建优化
- 两篇工作均强调多尺度与几何/语义融合的协同设计

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260919] HDMamba-YOLO: Efficient State-Space Perception and Local Spatial Reconstruction for UAV Small Object Detection | Wei Linduo, Fan Junjie, Mai Yijun, Chen Xiao, Zhang Guiyang, Qi Yong | School of Economics and Management, Nanjing University of Science and Technology；School of Intellectual Property, Nanjing University of Science and Technology；School of Computer Science and Engineering, Nanjing University of Science and Technology | 提出HDMamba-YOLO，融合状态空间感知与局部空间重建，用于无人机小目标检测。 | [#1317](https://github.com/thinson/RS-PaperClaw/issues/1317) |
| [20260919] VDGS: Visibility-Driven Large-Scale 3D Gaussian Splatting for Aerial Scene Reconstruction | Yu Haolin, Tang Jiadong, Wang YiXian, Gao Yu, He Shi, Lai Zhilin, Yang Yi, Fu Mengyin | the Beijing Institute of Technology, Beijing, China, * | 提出VDGS，以可见性驱动大规模3D高斯泼溅，实现航空场景重建。 | [#1318](https://github.com/thinson/RS-PaperClaw/issues/1318) |

## ⚠️ 未纳入日报的匹配论文

以下论文通过关键词/LLM 筛选，但在处理过程中失败未纳入日报。点击 arXiv 链接可查看原文。

| 标题 | arXiv | 失败原因 |
|------|-------|----------|
| SatOV: Restoring Spatial Priors for Training-Free Open-Vocabulary Segmentation in Remote Sensing Imagery | [2609.22834v1](https://arxiv.org/abs/2609.22834v1) | 质检未通过: 单位为空或无效 |


## 🔎 观察

- 状态空间模型正从通用视觉向遥感小目标检测迁移，效率与长程建模是主要卖点。
- 3D高斯泼溅在航空大场景中需解决可见性与尺度问题，可见性驱动是合理切入点。

---

Powered by OpenClaw🦞

---
