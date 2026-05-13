# Daily Reports

最近三天日报（最新在前）：

# [20260512](./202605/20260512.md)
## 📌 今日概况

今日共检索候选论文 11 篇；关键词+LLM 智能匹配遥感交叉论文 8 篇；最终纳入日报 6 篇。

今日遥感AI研究呈现三大趋势：一是大语言模型与智能体技术深度渗透农业预测、灾害响应等垂直场景；二是超高分影像与跨模态（光学-SAR、视觉-语言）融合成为技术焦点；三是自监督学习与基础模型推动地理实体关系推理向精细化发展。多模态感知与具身智能成为核心驱动力。

## ✨ 今日亮点

- 智能体后修正机制革新农业产量预测范式，实现预测-解释-修正闭环
- 超高分视觉语言模型诊断分辨率幻觉问题，突破微目标空间定位瓶颈
- 文本语义驱动光学-SAR跨模态配准，破解异构影像特征对齐难题

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260512] Agent-Based Post-Hoc Correction of Agricultural Yield Forecasts | Beddows Matthew, Durrant Aiden, Leontidis Georgios | University of Aberdeen；University of East Anglia；UiT The Arctic University of Norway | 提出基于大语言模型的智能体后修正框架，通过多智能体协作对农业产量时序预测结果进行动态校正与不确定性量化。 | [#516](https://github.com/thinson/RS-PaperClaw/issues/516) |
| [20260512] NARA: Anchor-Conditioned Relation-Aware Contextualization of Heterogeneous Geoentities | Kim Jina, Mai Gengchen, Zhao Lingyi, Shafique Khurram, Chiang Yao-Yi | University of Minnesota；University of Texas at Austin；Novateur Research Solutions | 构建锚点条件化关系感知框架NARA，以自监督方式学习异构地理实体间的空间关系表征。 | [#517](https://github.com/thinson/RS-PaperClaw/issues/517) |
| [20260512] UHR-Micro: Diagnosing and Mitigating the Resolution Illusion in Earth Observation VLMs | Ni Shuo, Wang Tong, Zhang Jing, Chen He, Guo Haonan, Zhang Ning, Du Bo | National Key Laboratory of Science and Technology on Space-Born Intelligent Information Processing, Beijing Institute of Technology；School of Computer Science, Wuhan University；Zhongguancun Academy；State Key Laboratory of Information Engineering in Surveying, Mapping and Remote Sensing, Wuhan University；The Department of Computing, Hong Kong Polytechnic University | 系统诊断地球观测视觉语言模型的分辨率幻觉现象，提出多尺度空间接地机制提升微目标识别精度。 | [#518](https://github.com/thinson/RS-PaperClaw/issues/518) |
| [20260512] TAR: Text Semantic Assisted Cross-modal Image Registration Framework for Optical and SAR Images | Cai Zhuoyu, Quan Dou, Huyan Ning, He Pei, Wang Shuang, Jiao Licheng | the Department of from a wide spatial range while maintaining feature invariance | 设计文本语义辅助的跨模态配准网络TAR，利用高层语义桥接光学与SAR影像的模态差异。 | [#519](https://github.com/thinson/RS-PaperClaw/issues/519) |
| [20260512] Mobile Traffic Camera Calibration from Road Geometry for UAV-Based Traffic Surveillance | Popov Alexey, Trukhina Natalia, Vashkelis Vadim | Embedded Intelligence Lab | 基于道路几何约束实现移动交通相机自标定，为无人机交通监控提供轻量级鸟瞰视图生成方案。 | [#520](https://github.com/thinson/RS-PaperClaw/issues/520) |
| [20260512] Can LLM Agents Respond to Disasters? Benchmarking Heterogeneous Geospatial Reasoning in Emergency Operations | Wang Junjue, Xuan Weihao, Qi Heli, Dai Pengyu, Liu Kunyi, Chen Hongruixuan, Zheng Zhuo, Xia Junshi, Ermon Stefano, Yokoya Naoto | The University of Tokyo；RIKEN AIP；Waseda University；Stanford University | 构建灾害响应场景下的异构地理空间推理基准，系统评估大语言模型智能体的应急决策能力边界。 | [#521](https://github.com/thinson/RS-PaperClaw/issues/521) |

## ⚠️ 未纳入日报的匹配论文

以下论文通过关键词/LLM 筛选，但在处理过程中失败未纳入日报。点击 arXiv 链接可查看原文。

| 标题 | arXiv | 失败原因 |
|------|-------|----------|
| Large-Small Model Collaboration for Farmland Semantic Change Detection | [2605.12282v1](https://arxiv.org/abs/2605.12282v1) | 质检未通过: 单位为空或无效 |


## 🔎 观察

- 智能体架构正从通用对话向领域专用决策演进，后修正机制或成为高 stakes 预测任务的标准配置
- 跨模态融合重心已从像素级对齐转向语义级桥接，文本作为中间表征显著降低模态鸿沟

---

Powered by OpenClaw🦞

---

# [20260511](./202605/20260511.md)
## 📌 今日概况

今日共检索候选论文 18 篇；关键词+LLM 智能匹配遥感交叉论文 12 篇；最终纳入日报 10 篇。

今日遥感AI研究呈现三大趋势：多模态大语言模型持续渗透遥感任务，涵盖视觉问答、场景分割与时空理解；3D重建技术向物理约束与实时应用演进，涉及森林燃料估算与滑坡模拟；SAR领域聚焦在线处理与目标识别，主动学习与异常检测等方向亦获关注。

## ✨ 今日亮点

- 多模态大模型成为遥感主流范式，4篇论文覆盖问答、分割与时空推理
- 3D Gaussian Splatting结合物理约束，推动无人机应急测绘与灾害模拟
- SAR在线处理与视觉问答并进，状态空间模型加速实时成像

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260511] Rapid Forest Fuel Load Estimation via Virtual Remote Sensing and Metric-Scale Feed-Forward 3D Reconstruction | Wu Quanyun, Gao Kyle, Sun Wentao, Xu Zhengsen, Sun Hudson, Xu Linlin, Chen Yuhao, David A. Clausi, Li Jonathan | University of Waterloo；University of Calgary | 基于Google Earth Studio虚拟遥感与度量级前馈3D重建，实现森林可燃物负荷快速估算。 | [#504](https://github.com/thinson/RS-PaperClaw/issues/504) |
| [20260511] Towards a Large Language-Vision Question Answering Model for MSTAR Automatic Target Recognition | David F. Ramirez, Tim L. Overman, Jaskie Kristen, Kleine Marv, Spanias Andreas | SenSIP Center, School of ECEE, Arizona State University；Prime Solutions Group | 面向MSTAR数据集构建大型语言-视觉问答模型，提升合成孔径雷达自动目标识别能力。 | [#505](https://github.com/thinson/RS-PaperClaw/issues/505) |
| [20260511] MPerS: Dynamic MLLM MixExperts Perception-Guided Remote Sensing Scene Segmentation | Wang Ziyi, Ma Xianping, Wang Ziyao, Zhang Hongyang, Man On Pun | The Chinese University of Hong Kong (Shenzhen)；Southwest Jiaotong University | 提出动态混合专家感知引导的遥感场景分割方法，增强多模态大语言模型视觉理解。 | [#506](https://github.com/thinson/RS-PaperClaw/issues/506) |
| [20260511] Geospatial-Temporal Sensemaking of Remote Sensing Activity Detections with Multimodal Large Language Model | David F. Ramirez, Overman Tim, Jaskie Kristen, Spanias Andreas | Arizona State University；Prime Solutions Group Inc | 利用多模态大语言模型对Sentinel-2遥感活动检测进行地理空间-时序语义理解。 | [#507](https://github.com/thinson/RS-PaperClaw/issues/507) |
| [20260511] UAV-Assisted Scan-to-Simulation for Landslides Using Physics-Informed Gaussian Splatting | Liang Zhenyu, Jack C. P. Cheng | HKUST | 结合物理信息高斯溅射，实现无人机辅助滑坡扫描到仿真的高效重建。 | [#508](https://github.com/thinson/RS-PaperClaw/issues/508) |
| [20260511] SenseBench: A Benchmark for Remote Sensing Low-Level Visual Perception and Description in Large Vision-Language Models | Zhong Chen, An Xiao, Sun Jiaxing, Gui Zihan, Yang Guangyi, He Wei | Wuhan University；Shanghai Artificial Intelligent Laboratory | 发布SenseBench基准，系统评估大视觉语言模型在遥感低层视觉感知与描述能力。 | [#509](https://github.com/thinson/RS-PaperClaw/issues/509) |
| [20260511] AnomalyClaw: A Universal Visual Anomaly Detection Agent via Tool-Grounded Refutation | Jiang Xi, Zhao Yinjie, Yang Zesheng, Zheng Feng | Southern University of Science and Technology (SUSTech)；Nanyang Technological University (NTU)；CFAR, Agency for Science, Technology and Research (A*STAR) | AnomalyClaw通过工具锚定反驳机制，构建通用视觉异常检测智能体。 | [#510](https://github.com/thinson/RS-PaperClaw/issues/510) |
| [20260511] Learning to Focus Synthetic Aperture Radar On-line with State-Space Models | Fieldhouse Sebastian, Roberto Del Prete, Daga Gabriele, Rensly Nathaniel, Meoni Gabriele, Tang Kea-Tiong | College of Semiconductor Research, National Tsing Hua University；Φ-lab, European Space Agency (ESA)；Department of Electrical Engineering, National Tsing Hua University；Advanced Concepts and Studies Office, European Space Agency (ESA) | 基于状态空间模型实现合成孔径雷达在线聚焦学习，支持实时成像处理。 | [#511](https://github.com/thinson/RS-PaperClaw/issues/511) |
| [20260511] Active-SAOOD: Active Sparsely Annotated Oriented Object Detection in Remote Sensing Images | Lin Yu, Lin Jianghang, Ye Kai, Zhang Shengchuan, Cao Liujuan | Image-Level Active Learning | 提出主动稀疏标注定向目标检测方法，降低遥感图像标注成本并提升检测效率。 | [#512](https://github.com/thinson/RS-PaperClaw/issues/512) |
| [20260511] Lure-and-Reveal: An Exposure Framework for Stealthy Deception Attack in Multi-sensor Uncertain Systems | Tian Meiqi, Liu Yihan, Zhong Bingzhuo | The Thrust of Artificial Intelligence, Information Hub, Hong Kong University of Science and Technology (Guangzhou)；The Thrust of Intelligent Transportation, System Hub, Hong Kong University of Science and Technology (Guangzhou) | 揭示多传感器不确定系统中隐蔽欺骗攻击的暴露框架，保障融合系统安全。 | [#513](https://github.com/thinson/RS-PaperClaw/issues/513) |

## ⚠️ 未纳入日报的匹配论文

以下论文通过关键词/LLM 筛选，但在处理过程中失败未纳入日报。点击 arXiv 链接可查看原文。

| 标题 | arXiv | 失败原因 |
|------|-------|----------|
| Developing a foundation model for high-resolution remote sensing data of the Netherlands | [2605.10184v1](https://arxiv.org/abs/2605.10184v1) | 质检未通过: 单位为空或无效 |


## 🔎 观察

- 视觉-语言大模型正从通用领域向遥感专业化纵深发展，任务覆盖度与评估体系同步完善
- 3D重建技术加速与物理仿真、实时处理融合，灾害应急与生态监测成为典型落地场景

---

Powered by OpenClaw🦞

---

# [20260510](./202605/20260510.md)
## 📌 今日概况

今日共检索候选论文 5 篇；关键词+LLM 智能匹配遥感交叉论文 3 篇；最终纳入日报 2 篇。

今日遥感AI研究聚焦两大方向：一是面向地质灾害监测的高效特征选择方法，通过序列特征筛选优化滑坡分割任务；二是针对遥感图像质量提升的生成式建模，结合空间-频率域信息改进超分辨率重建。两项工作均体现轻量化设计与多源信息融合的研究趋势。

## ✨ 今日亮点

- 序列特征选择策略降低多光谱滑坡分割计算成本，提升模型效率
- 空间-频率门控Swin Transformer实现遥感单图超分辨率，兼顾全局与细节重建
- 印度多机构联合推进遥感图像增强技术，强化实际应用价值

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260510] Sequential Feature Selection for Efficient Landslide Segmentation from Multi-Spectral Data | Ahmad Arsalaan, Karakus Oktay, Paul L. Rosin | School of Computer Science and Informatics；Cardiff University | 卡迪夫大学团队提出序列特征选择方法，从多光谱数据中高效提取滑坡敏感特征，优化分割模型计算效率。 | [#500](https://github.com/thinson/RS-PaperClaw/issues/500) |
| [20260510] Spatial-Frequency Gated Swin Transformer for Remote Sensing Single-Image Super-Resolution | Md Aminur Hossain, Valkesh Parekh, Ayush V. Patel, Jethani Yogesh, Sanjay K. Singh, Banerjee Biplab | Space Applications Centre, ISRO, Ahmedabad, India；Centre of Studies in Resources Engineering, Indian Institute of Technology Bombay, India；New L J Institute of Engineering and Technology, Ahmedabad, India；Pandit Deendayal Energy University, Gandhinagar, India；GLS University, Ahmedabad, India | 印度空间应用中心等机构联合开发空间-频率门控Swin Transformer，通过频域-空域协同建模提升遥感图像超分辨率质量。 | [#501](https://github.com/thinson/RS-PaperClaw/issues/501) |

## 🔎 观察

- 特征选择技术重回遥感深度学习视野，反映边缘部署场景对模型轻量化的迫切需求
- Swin Transformer在遥感低层视觉任务中持续演进，门控机制与频域先验的结合或成为新范式

---

Powered by OpenClaw🦞

---
