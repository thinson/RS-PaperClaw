# Daily Reports

最近三天日报（最新在前）：

# [20260809](./202608/20260809.md)
## 📌 今日概况

今日共检索候选论文 2 篇；关键词+LLM 智能匹配遥感交叉论文 1 篇；最终纳入日报 1 篇。

今日遥感AI研究聚焦于无人机集群在间歇性连接条件下的可靠协同侦察。核心趋势是利用生成式预测与潜在状态估计，以应对通信受限环境下的感知不确定性，提升多机系统的鲁棒性与自主性。该方向融合了多智能体协同、深度学习与状态推理，为复杂动态场景下的遥感数据获取与融合提供了新思路。

## ✨ 今日亮点

- 提出潜在语义状态估计方法，增强无人机集群在弱连接下的协同可靠性。
- 结合生成式预测，应对间歇性通信导致的感知数据缺失问题。
- 研究聚焦于协同侦察场景，提升多机系统在复杂环境中的自主决策能力。

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260809] Latent Semantic State Estimation for Reliable Swarming of UAVs under Intermittent Connectivity | Paris A. Karakasis, Saad Walid | Institute for Advanced Computing and Bradley Dept. of Electrical and Computer Engineering | 提出潜在语义状态估计框架，用于间歇性连接下无人机集群的可靠协同侦察。 | [#1074](https://github.com/thinson/RS-PaperClaw/issues/1074) |

## 🔎 观察

- 间歇性连接成为多机协同遥感的核心约束，推动状态估计向生成式与潜在语义方向演进。
- 研究侧重算法鲁棒性而非硬件改进，表明软件层面补偿通信缺陷是当前技术突破口。

---

Powered by OpenClaw🦞

---

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
