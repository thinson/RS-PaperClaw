# Daily Reports

最近三天日报（最新在前）：

# [20260808](./202608/20260808.md)
## 📌 今日概况

今日共检索候选论文 3 篇；关键词+LLM 智能匹配遥感交叉论文 2 篇；最终纳入日报 2 篇。

今日遥感AI研究聚焦于气象预测与视觉基础模型两大方向。热带气旋预测引入潜空间修正流模型，结合卫星影像与大气场数据，提升生成式预测精度；变化检测领域则提出AdaDINO，通过冻结DINO骨干的配对感知适配，实现高效双时相分析。两项工作均强调对现有深度学习架构的优化，以应对遥感数据的时空复杂性，推动灾害监测与地表动态识别的智能化发展。

## ✨ 今日亮点

- 潜空间修正流提升热带气旋预测精度
- 冻结DINO适配实现高效变化检测
- 遥感AI聚焦生成模型与基础模型优化

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260808] Tropical Cyclone Forecasting via Latent Rectified Flow using Satellite Imagery and Atmospheric Fields | Zannat Meheru, Sk. Md. Masudul Ahsan | Department of Computer Science and Engineering；Khulna University of Engineering \& Technology | 提出潜空间修正流模型，融合卫星影像与大气场预测热带气旋 | [#1071](https://github.com/thinson/RS-PaperClaw/issues/1071) |
| [20260808] AdaDINO: Pair-Aware In-Backbone Adaptation of Frozen DINO for Efficient Remote Sensing Change Detection | Zhang Xu, Li Xinqing, Xie Jianpeng, Zhu Zeshuai, He Xin, Liu Yun | VCIP, College of Computer Science, Nankai University；School of Computer Science and Engineering, Tianjin University of Technology；Academy for Advanced Interdisciplinary Studies, Nankai University；Nankai International Advanced Research Institute, Shenzhen Futian | AdaDINO在冻结DINO骨干中引入配对感知适配，提升变化检测效率 | [#1072](https://github.com/thinson/RS-PaperClaw/issues/1072) |

## 🔎 观察

- 生成式模型在气象预测中应用渐增，但需平衡计算成本与精度
- 基础模型适配策略趋向轻量化，强调冻结骨干与任务特定模块结合

---

Powered by OpenClaw🦞

---

# [20260807](./202608/20260807.md)
## 📌 今日概况

今日共检索候选论文 7 篇；关键词+LLM 智能匹配遥感交叉论文 3 篇；最终纳入日报 3 篇。

今日遥感AI研究聚焦星上智能处理与轻量化模型。三篇论文分别提出宽幅卫星交通检测基准、基于视觉语言模型的星上摘要生成，以及极限学习机图像压缩方法，共同指向降低卫星下行带宽压力、提升在轨实时分析能力，体现了边缘计算与遥感结合的趋势。

## ✨ 今日亮点

- 星上视觉语言模型实现先摘要后下载，大幅节省带宽。
- 宽幅卫星交通检测新基准，配套超轻量基线模型。
- 极限学习机用于星上图像压缩，提升下行效率。

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260807] SkySeaLand: A Wide-Format Satellite Transportation Benchmark with an Ultra-Lightweight Detection Baseline | Md. Zahid Hasan Riad, Md Sultanul Islam Ovi | Dept. of Computer Science and Engineering, Green University of Bangladesh, Bangladesh；Dept. of Computer Science, George Mason University, Virginia, USA | 提出宽幅卫星交通检测基准SkySeaLand及超轻量基线，推动小目标检测。 | [#1067](https://github.com/thinson/RS-PaperClaw/issues/1067) |
| [20260807] Summarize First, Download Later: Onboard VLMs for Bandwidth-Efficient Earth Observation | Park Junghwan, Sim Sangcheol, Cho Woojin, Kwon Darongsae | TelePIX | 利用星上视觉语言模型生成摘要，减少下行数据量，提高带宽效率。 | [#1068](https://github.com/thinson/RS-PaperClaw/issues/1068) |
| [20260807] ELMZip: Onboard Satellite Image Compression via Extreme Learning Machines for Efficient Downlink | Cho Woojin, Park Junghwan, Sim Sangcheol, Steve Andreas Immanuel, Heo Junhyuk, Kwon Darongsae | TelePIX | ELMZip基于极限学习机实现星上多光谱图像压缩，优化下行传输。 | [#1069](https://github.com/thinson/RS-PaperClaw/issues/1069) |

## 🔎 观察

- 星上处理成为热点，三篇均关注在轨计算，旨在减少对地面依赖。
- 轻量化模型与压缩技术结合，预示遥感小卫星星座的智能化升级。

---

Powered by OpenClaw🦞

---

# [20260806](./202608/20260806.md)
## 📌 今日概况

今日共检索候选论文 12 篇；关键词+LLM 智能匹配遥感交叉论文 11 篇；最终纳入日报 11 篇。

今日遥感AI研究聚焦多模态融合、变化检测与智能感知。多篇论文探索跨注意力机制、开放词汇变化检测及持续学习，推动模型适应性与泛化能力。高光谱图像分类与变化检测结合无监督伪标签与拓扑学习，提升标签效率。此外，低光增强、UAV路径规划及智能体AI与通感一体化等方向亦受关注，整体呈现从静态分析向动态、多时相推理演进的趋势。

## ✨ 今日亮点

- 多模态融合与持续学习成热点，提升模型适应性与泛化能力。
- 高光谱分类与变化检测探索无监督及源自由域适应方法。
- UAV导航与路径规划结合世界模型与优化算法，增强自主性。

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260806] CFGPNet: Cross-Attention-Based Fused Gradient Programmed Network Framework for Multispectral Object Detection | Hatami Nima, Faez Karim, Sharifian Saeed, Amindavar Hamidreza | Department of Electrical Engineering, Amirkabir University of Technology | 提出CFGPNet，用交叉注意力融合梯度编程网络，提升多光谱目标检测性能。 | [#1055](https://github.com/thinson/RS-PaperClaw/issues/1055) |
| [20260806] CogVis: Must Open-Vocabulary Change Detection Perceive the Scene Anew for Every Query? | Wang Zijie, Zhong Chen, He Wei | Key Laboratory of Information Engineering in Surveying, Mapping and Remote Sensing, Wuhan University；monitoring and informed decision-making (Li et al. 2026a). 2026b) summarizes existing research through the Mask- | CogVis探索开放词汇变化检测中场景感知复用，减少重复计算并保持准确性。 | [#1056](https://github.com/thinson/RS-PaperClaw/issues/1056) |
| [20260806] DARAD: Dual Adapters and Ranking-Aware Distillation for Continual Remote Sensing Image-Text Retrieval | Chen Xi, Chen Xu, Jia Xiangyang, Wang Wei, Zhang Xu, Sun Zhenyuan | School of Computer Science, Wuhan University, Wuhan 430072, China；Beijing Institute for General Artificial Intelligence (BIGAI) | DARAD采用双适配器与排序感知蒸馏，实现遥感图文检索的持续学习。 | [#1057](https://github.com/thinson/RS-PaperClaw/issues/1057) |
| [20260806] Hyperspectral Calibration Detection: A Novel Concept For Change Detection With Unsupervised Incremental Safe Pseudo-Labeling Implementation | Lin Chia-Hsiang, Hsu Shih-Min, Liang Ching-Yun, Chanussot Jocelyn, Chen Jhih-Yan | Department of Electrical Engineering；the Miin Wu School of Computing, National Cheng Kung University, Tainan, Taiwan (R.O.C.) (；Institute of Computer and Communication Engineering, Department of Electrical Engineering, National Cheng Kung University, Tainan, Taiwan (R.O.C.) (；Inria, CNRS, Grenoble INP, LJK, Université Grenoble Alpes, Grenoble, France ( | 提出高光谱校准检测概念，结合无监督增量安全伪标签用于变化检测。 | [#1058](https://github.com/thinson/RS-PaperClaw/issues/1058) |
| [20260806] Multi-Year Geospatial Reasoning using Interannually-Consistent Historical Predictions as a Free Input Modality | Syed Roshaan Ali Shah, Bonte Kasper, Bekaert David, Kristof Van Tricht, Wens Dieter | VITO Remote Sensing | 利用年际一致的历史预测作为免费输入模态，增强多时相地理空间推理。 | [#1059](https://github.com/thinson/RS-PaperClaw/issues/1059) |
| [20260806] Topology-Aware Neighborhood Learning for Source-Free Cross-Scene Hyperspectral Image Classification | Li Qingmei, Zheng Juepeng, Zhang Jiarui, Huang Jianxi, Fu Haohuan | the Tsinghua Shenzhen International Graduate School, Tsinghua University, Shenzhen, China (；School of Artificial Intelligence, Sun Yat-Sen University, Zhuhai, China ( | 拓扑感知邻域学习用于源自由跨场景高光谱图像分类，提升伪标签质量。 | [#1060](https://github.com/thinson/RS-PaperClaw/issues/1060) |
| [20260806] Shape-Aware Oriented Bounding Box (OBB) to Horizontal Bounding Box (HBB) Conversion | Badha Rathna Sabhapathy, Dahiya Gotam, Vatsal Vishesh | Hyspace Technologies | 提出形状感知的旋转框转水平框方法，改善遥感目标检测的标注效率。 | [#1061](https://github.com/thinson/RS-PaperClaw/issues/1061) |
| [20260806] Overcoming Attention Drift: Homogeneity-Heterogeneity Guided Feature Aggregation for Low-Light Remote Sensing Image Enhancement | Zhong Yaozi, Yang Xingxing, Mei Shaohui, Ma Mingyang | School of Information and Artificial Intelligence, Yunnan University of Finance and Economics, Kunming, China；Department of Computer Science, Hong Kong Baptist University, Hong Kong, China；School of Electronics and Information, Northwestern Polytechnical University, Xi'an, China | 同质-异质引导特征聚合克服注意力漂移，用于低光遥感图像增强。 | [#1062](https://github.com/thinson/RS-PaperClaw/issues/1062) |
| [20260806] When Agentic AI Meets Integrated Sensing and Communication | Li Kai, Li Conggai, Sarah Ali Siddiqui, Syed Sohail Ahmed, Yuan Xin, Li Shenghong, Ni Wei | KAI LI, Interdisciplinary Centre for Security, Reliability and Trust (SnT), University of Luxembourg, Luxembourg；SYED SOHAIL AHMED, College of Computer, Qassim University, Saudi Arabia；WEI NI, Edith Cowan University, School of Engineering, Australia；Authors’ Contact Information: Kai Li, Interdisciplinary Centre for Security, Reliability and Trust (SnT), University of Luxembourg, Luxembourg | 探讨智能体AI与通感一体化结合，提出闭环框架以增强多模态智能。 | [#1063](https://github.com/thinson/RS-PaperClaw/issues/1063) |
| [20260806] Iterative Hybrid Discrete-Continuous Viewpoint Planning for UAV Photogrammetry | Grech Alan, Pisani Daniel, Grima Andre, Carl James Debono, Formosa Saviour, Seychell Dylan | University of Malta University of Malta Stargate Studios Malta；University of Malta University of Malta University of Malta；University of Malta (Dawl AI Lab), financed by Xjenza Malta through the registration reliability, completeness, and depth accuracy [3] | 迭代混合离散连续视点规划用于UAV摄影测量，优化表面覆盖与精度。 | [#1064](https://github.com/thinson/RS-PaperClaw/issues/1064) |
| [20260806] Uncertainty-Aware World Model for Aerial Image-Goal Navigation | Zhu Deyi, Fan Haoyu, Zhu Yinan, Zhang Weichen, Ma Shilin, Chen Xinlei, Tang Yansong | Tsinghua Shenzhen International Graduate School, Tsinghua University | 不确定性感知世界模型用于航空图像目标导航，提升轨迹评分与决策鲁棒性。 | [#1065](https://github.com/thinson/RS-PaperClaw/issues/1065) |

## 🔎 观察

- 多篇工作聚焦无监督或持续学习，减少标注依赖，适应动态遥感场景。
- 跨模态与多时相融合趋势明显，推动从单帧分析向时空推理发展。

---

Powered by OpenClaw🦞

---
