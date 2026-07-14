# Daily Reports

最近三天日报（最新在前）：

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

# [20260712](./202607/20260712.md)
## 📌 今日概况

今日共检索候选论文 4 篇；关键词+LLM 智能匹配遥感交叉论文 3 篇；最终纳入日报 3 篇。

今日遥感AI研究聚焦于无监督学习与实时检测两大方向。一篇工作提出利用空间变换网络解决建筑分割中的标签错位问题，实现无监督分割。另有两篇分别关注无人机平台的人员实时检测和车辆再识别在模拟天气下的鲁棒性，体现了从算法到实际部署的全面探索。

## ✨ 今日亮点

- 无监督建筑分割方法应对标签错位问题
- 无人机实时人员检测框架基于YOLOv8
- 模拟天气下无人机车辆再识别基准测试

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260712] Align and Segment: Unsupervised Learning for Building Segmentation From Misaligned Labels | Venkanna Babu Guthula, Krause Oswin, Gominski Dimitri, Zhang Hui, Mottelson Johan, Kariryaa Ankit, Lang Nico, Igel Christian | University of Copenhagen, Copenhagen, Denmark；Royal Danish Academy, Copenhagen, Denmark | 提出无监督方法，用空间变换网络对齐错位标签实现建筑分割 | [#886](https://github.com/thinson/RS-PaperClaw/issues/886) |
| [20260712] End-to-End Real-Time Drone-Based Person Detection Framework Using Deep Learning | Sarmah Payel, Ranjan Ayush, Piyush Kaushik Bhattacharyya, Anil Kr. Shaw, Pradip Kr. Das | Centre for Drone Technology；Indian Institute of Technology Guwahati；KIIT University；Drone LAB；National Institute of Electronics and Information Technology | 基于YOLOv8的端到端无人机实时人员检测框架 | [#887](https://github.com/thinson/RS-PaperClaw/issues/887) |
| [20260712] Benchmarking UAV-based Vehicle Re-Identification under Simulated Weather Conditions | Vu Minh Tran, Nguyen Khang | University of Information Technology University of Information Technology；Vietnam National University Ho Chi Minh City Vietnam National University Ho Chi Minh City；become an important research topic in computer vision due to | 构建模拟天气条件下的无人机车辆再识别基准数据集 | [#888](https://github.com/thinson/RS-PaperClaw/issues/888) |

## 🔎 观察

- 无监督学习在遥感标注不完美场景中展现出实用潜力
- 无人机视觉任务正从检测向更复杂的再识别与鲁棒性评估延伸

---

Powered by OpenClaw🦞

---

# [20260711](./202607/20260711.md)
## 📌 今日概况

今日共检索候选论文 6 篇；关键词+LLM 智能匹配遥感交叉论文 3 篇；最终纳入日报 3 篇。

今日遥感AI研究聚焦于自监督学习、视觉语言模型与边缘智能三大方向。PhenoEmbed利用自监督多光谱时序嵌入实现单木冠层物候分析；WeaveEarth提出无训练框架，通过结构化证据构建增强超高分遥感理解；DynaFilter则探索云边协同下的动态滤波机制，优化卫星边缘推理效率。整体趋势向轻量化、无监督及多模态融合演进。

## ✨ 今日亮点

- 自监督时序嵌入用于单木冠层物候提取
- 无训练视觉语言模型提升超高分遥感理解
- 云边协同动态滤波优化卫星边缘推理

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260711] PhenoEmbed: Self-Supervised Multispectral UAV Time-Series Embeddings for Individual Tree Crown Phenology | Khan Taimur | are retained as object anchors to extract aligned crown-centered crops through time, allowing one；Helmholtz Centre for Environmental Research - UFZ, Community Ecology, Theodor-Lieser-Str. 4, 06120 | 自监督多光谱无人机时序嵌入实现单木冠层物候特征提取 | [#882](https://github.com/thinson/RS-PaperClaw/issues/882) |
| [20260711] WeaveEarth: Structured Evidence Construction and Reasoning for Training-Free UHR Remote Sensing Understanding | Ma Xianzhi, Wang Shujun, Li Xiaohan, Liu Hao, Pei Changhua, li Jianhui | School of Frontier Sciences, Nanjing School of Frontier Sciences, Nanjing School of Frontier Sciences, Nanjing；University University University；School of Frontier Sciences, Nanjing Computer Network Information School of Frontier Sciences, Nanjing；University Center, Chinese Academy of Sciences University | 无训练框架通过结构化证据与全局推理增强超高分遥感理解 | [#883](https://github.com/thinson/RS-PaperClaw/issues/883) |
| [20260711] DynaFilter: Cloud-driven Dynamic Filtering for Satellite Edge Intelligence | Zhang Ziyang, Liu Jie, Mottola Luca | Harbin Institute of Technology Shenzhen, China | 云驱动动态滤波方法优化卫星边缘智能推理效率 | [#884](https://github.com/thinson/RS-PaperClaw/issues/884) |

## 🔎 观察

- 自监督学习在遥感时序分析中的应用日益成熟，尤其针对精细物候监测
- 无训练视觉语言模型成为超高分遥感理解的新趋势，降低标注依赖

---

Powered by OpenClaw🦞

---
