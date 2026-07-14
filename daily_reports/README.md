# Daily Reports

最近三天日报（最新在前）：

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

# [20260710](./202607/20260710.md)
## 📌 今日概况

今日共检索候选论文 8 篇；关键词+LLM 智能匹配遥感交叉论文 4 篇；最终纳入日报 4 篇。

今日遥感AI研究聚焦于基础模型适配与自主感知两大方向。SAM 3在遥感场景下的零样本与单样本分割能力被系统评估；多光谱差分分析用于地形识别，服务于自主导航；面向无人机野外主动目标检测的大规模数据集与基准发布；跨视角地理定位中提出稳定自训练方法，通过弹性匹配与自适应净化提升无监督学习效果。

## ✨ 今日亮点

- SAM 3遥感零样本与单样本分割能力评估
- 多光谱差分融合用于地形识别与自主导航
- 无人机野外主动目标检测数据集与基准发布

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260710] Promptable Concept Segmentation from Above: Evaluating SAM 3's Zero-Shot and One-Shot Capabilities in Remote Sensing | Dabaja Mohammad, Celik Turgay | “school” is implicitly tied to its vertical facades and windows；Both authors are affiliated with the Department of ICT, University of Agder, To resolve this ambiguity and establish a performance | 评估SAM 3在遥感中的零样本与单样本概念分割能力。 | [#877](https://github.com/thinson/RS-PaperClaw/issues/877) |
| [20260710] Differential Analysis of Multispectral Images for Terrain Identification | Kashmar Omar, Arya Hemendra, Mastrogiovanni Fulvio | University of Genoa, Italy；Indian Institute of Technology Bombay, Mumbai, India | 提出多光谱图像差分分析方法用于地形识别。 | [#878](https://github.com/thinson/RS-PaperClaw/issues/878) |
| [20260710] Toward Active Object Detection for UAVs in the Wild: A Large-Scale Dataset, Benchmark and Method | Liu Tianpeng, Jiang Xinhua, Liu Li, Shen Qinmu, Tang Siwei, Liu Zhen, Liu Yongxiang | College of Electronic Science and Technology, National University of Defense Technology, Changsha,, China | 发布面向无人机野外主动目标检测的大规模数据集与基准。 | [#879](https://github.com/thinson/RS-PaperClaw/issues/879) |
| [20260710] STEAM: Stable Self-Training with Elastic Matching and Adaptive Purification | Wang Shaoxiang, Zhang Kejia, Pan Haiwei, Zhang Lan | Harbin Engineering University, School of Computer Science and Technology；Northeast Forestry University, School of Computer and Artificial Intelligence | 提出稳定自训练方法，结合弹性匹配与自适应净化。 | [#880](https://github.com/thinson/RS-PaperClaw/issues/880) |

## 🔎 观察

- 基础模型（如SAM）向遥感垂直领域迁移仍是研究热点，零样本能力受关注。
- 无人机自主感知正从静态检测向主动目标检测演进，数据集驱动明显。

---

Powered by OpenClaw🦞

---
