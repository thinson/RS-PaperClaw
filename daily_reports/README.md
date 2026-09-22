# Daily Reports

最近三天日报（最新在前）：

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

# [20260918](./202609/20260918.md)
## 📌 今日概况

今日共检索候选论文 6 篇；关键词+LLM 智能匹配遥感交叉论文 2 篇；最终纳入日报 1 篇。

今日候选论文聚焦无人机遥感影像中的重叠植物识别问题，提出将目标检测与几何感知聚类相结合的技术路线。该方法先通过目标检测定位植物个体，再利用几何信息引导K-Means聚类以区分相互重叠的植株，试图缓解密集植被场景下检测框重叠导致的个体混淆。整体来看，研究延续了遥感AI中检测与聚类融合的思路，强调几何先验在实例区分中的作用，面向农业与植被监测的精细化管理需求。

## ✨ 今日亮点

- 目标检测与几何感知聚类结合，应对无人机影像中植物重叠难题
- 利用几何信息引导K-Means，提升重叠植株的个体区分能力
- 面向农业植被精细监测，强调实例级识别而非仅计数

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260918] Combining Object Detection with Geometry-Aware Clustering to Distinguish Overlapping Plants in UAV Imagery | Ik Jae Lee, Hieu D. Nguyen, Meenar Mahbubur, Carlos Morrison Martinez, Connelly Cameron | Department of Mathematics, Rowan University；Department of Geography, Planning, and Sustainability, Rowan University；Department of Computer Science, Rowan University | 将目标检测与几何感知聚类结合，用K-Means区分无人机影像中相互重叠的植物个体。 | [#1315](https://github.com/thinson/RS-PaperClaw/issues/1315) |

## ⚠️ 未纳入日报的匹配论文

以下论文通过关键词/LLM 筛选，但在处理过程中失败未纳入日报。点击 arXiv 链接可查看原文。

| 标题 | arXiv | 失败原因 |
|------|-------|----------|
| AgenticSwarm: Semantic Perception and Adaptive Task Allocation for Heterogeneous Multi-UAV Missions | [2609.21716v1](https://arxiv.org/abs/2609.21716v1) | 质检未通过: 单位为空或无效 |


## 🔎 观察

- 检测加聚类的两阶段思路，适合处理密集植被中检测框难以分离的实例区分问题。
- 几何先验的引入表明，单纯依赖外观特征在重叠场景下仍有局限，结构信息值得重视。

---

Powered by OpenClaw🦞

---

# [20260917](./202609/20260917.md)
## 📌 今日概况

今日共检索候选论文 15 篇；关键词+LLM 智能匹配遥感交叉论文 7 篇；最终纳入日报 7 篇。

今日论文呈现遥感智能处理向多模态信号融合与任务导向设计演进的趋势。一方面，研究关注低信噪比条件下的语义特征传输与声学信号处理，强调信号层面的预处理与通信效率；另一方面，事件视觉、持久语义记忆与主动地理定位等方向推动无人机与卫星平台在动态环境中的感知鲁棒性。此外，时序InSAR与地表异常免疫监测等研究延续了对地观测中形变与变化检测的精细化需求，整体体现从数据驱动向任务与信号协同优化的转变。

## ✨ 今日亮点

- 信号中心与任务导向通信成为低信噪比遥感的新优化路径
- 事件视觉与持久语义记忆提升无人机动态感知鲁棒性
- 主动地理定位与时序InSAR推动跨视角与形变监测精细化

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260917] Signal-Centric Remote Sensing via Alternative Preprocessing and Acoustic Processing for ML-Driven Applications | Luna Logan, Jansen-Sánchez Sirio, Demirkiran Ilteris, Ghelarducci Leo | School of Computer Science, College of Computing, Georgia Institute of Technology, Atlanta, GA USA (；Embry-Riddle Aeronautical University | 提出以信号为中心的处理框架，结合替代预处理与声学方法提升低信噪比遥感ML应用性能。 | [#1307](https://github.com/thinson/RS-PaperClaw/issues/1307) |
| [20260917] Earth Surface Immune System for Rapid Monitoring of Unknown Anomalies | Li Jingtao, Zhu Qian, Wang Xinyu, Li Deren, Zhang Liangpei, Zhong Yanfei | State Key Laboratory of Information Engineering in Surveying, Mapping and Remote Sensing, Wuhan University；School of Remote Sensing and Information Engineering, Wuhan University | 借鉴免疫系统机制构建地表异常快速监测框架，实现未知异常的即时发现与响应。 | [#1308](https://github.com/thinson/RS-PaperClaw/issues/1308) |
| [20260917] Multi-Track Time-Series Burst-Overlap Interferometry for Resolving Horizontal Deformation in Earthquake-Cycle Studies | Li Xing, Gao Zhuang, Chen Han, Ma Zhangfeng, Chen Yangkang, Savvaidis Alexandros | Bureau of Economic Geology, Jackson School of Geosciences, University of Texas at Austin；Department of Earth and Space Sciences, Southern University of Science and Technology；State Key Laboratory of Earthquake Dynamics and Forecasting, Institute of Geology, China；Earth Observatory of Singapore, Nanyang Technological University, Singapore, 639798 | 利用多轨时序burst-overlap干涉测量，解析地震周期中的水平形变信号。 | [#1309](https://github.com/thinson/RS-PaperClaw/issues/1309) |
| [20260917] Task-Oriented Semantic Feature Transmission for Multi-Task Satellite Remote Sensing over Low-SNR Channels | Sun Shuoyuan, Wang Hongyu, Peng Mugen, Xu Wenjia | State Key Laboratory of Networking and Switching Technology；Beijing University of Posts and Telecommunications | 面向多任务卫星遥感，设计低信噪比信道下的语义特征传输与任务导向通信方案。 | [#1310](https://github.com/thinson/RS-PaperClaw/issues/1310) |
| [20260917] PointEvent: Rethinking Event-based Tiny Object Detection via Serialized Motion Evidence Accumulation | Wu Zongze, Jia Baofeng, Yan Weiqi, Zhang Jingyuan, Zang Yu, Chen Xiaoyu, Han Jing | State key Lab of Extreme Environment Optoelectronic Dynamic Testing Technology and Instrument, Nanjing University of；Jiangsu Key Lab of Visual Sensing and Intelligent Perception, Nanjing University of Science and Technology, China；Fujian Key Laboratory of Urban Intelligent Sensing and Computing, Xiamen University, China | 提出PointEvent方法，通过序列化运动证据积累改进事件相机微小目标检测。 | [#1311](https://github.com/thinson/RS-PaperClaw/issues/1311) |
| [20260917] Towards Active Cross-View Object Geo-Localization | Yao Shunyu, Zhang Xiaohan, Yang Zhuoran, Lai Haoqi, Ming Qi, Hu Xiaoxi, Shen Hui-Liang, Cao Si-Yuan | College of Information Science and Electronic Engineering；Zhejiang University, Hangzhou 310027, China；College of Computer Science；Beijing University of Technology, Beijing 100124, China；State Key Laboratory of Intelligent Green Vehicle and Mobility；Tsinghua University, Beijing 100084, China；Ningbo Global Innovation Center；Zhejiang University, Ningbo 315100, China；Jinhua Institute of Zhejiang University | 构建主动跨视角目标地理定位框架，融合多视角提示保持与轨迹引导策略初始化。 | [#1312](https://github.com/thinson/RS-PaperClaw/issues/1312) |
| [20260917] PerSeM: Persistent Semantic Memory for Long-Horizon Open-Vocabulary UAV Mapping | Saurbh Singh Jamwal, Ramakrishnan Ganesh | Department of Computer Science and Engineering；Indian Institute of Technology Bombay | 提出持久语义记忆机制，支持长时程开放词汇无人机建图中的时序一致性。 | [#1313](https://github.com/thinson/RS-PaperClaw/issues/1313) |

## 🔎 观察

- 低信噪比与任务导向通信的交叉研究增多，反映遥感系统正从单纯成像向语义高效传输演进。
- 事件视觉与持久记忆机制在无人机场景中互补，有望缓解动态环境下的目标丢失与语义漂移问题。

---

Powered by OpenClaw🦞

---
