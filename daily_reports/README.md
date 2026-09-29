# Daily Reports

最近三天日报（最新在前）：

# [20260928](./202609/20260928.md)
## 📌 今日概况

今日共检索候选论文 14 篇；关键词+LLM 智能匹配遥感交叉论文 9 篇；最终纳入日报 9 篇。

今日论文呈现三条主线：一是面向星上/在轨场景的轻量化与协同推理，包括SAR Level-0原始数据直接分类、卫星-地面DNN分割与资源分配；二是遥感基础模型与迁移学习的适用边界，涉及冻结嵌入跨 wildfire 迁移失效问题；三是多模态与生成式方法向遥感任务渗透，如开放词汇分割、视频问答、稀疏视角3D高斯泼溅与高光谱跟踪。整体看，研究更强调物理约束、数据特性与部署可行性，而非单纯堆叠模型规模。

## ✨ 今日亮点

- 星上智能与协同推理成为热点，关注原始数据直接处理与资源受限部署。
- 迁移学习研究开始反思冻结嵌入的跨域失效，强调本地增益难以泛化。
- 多模态与生成式方法加速进入遥感，覆盖视频问答、3D重建与高光谱跟踪。

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260928] Stacked Intelligent Metasurface-Diffractive Deep Neural Networks for Onboard Terrain Classification from SAR Level-0 Raw Data | Liu Mengbing, Li Xin, An Jiancheng, Yuen Chau | School of Electrical and Electronics Engineering, Nanyang Technological University, Singapore (e-mails:; ) | 提出堆叠智能超表面与衍射深度神经网络，直接从SAR Level-0原始数据进行在轨地形分类。 | [#1388](https://github.com/thinson/RS-PaperClaw/issues/1388) |
| [20260928] Preference-Guided Adaptation for Open-Vocabulary Semantic Segmentation via Prompt Disagreement | Jang Hyun-Kurl, Kim Jihun, Yoon Kuk-Jin | Visual Intelligence Lab | 利用提示不一致性进行偏好引导自适应，提升开放词汇语义分割的跨域表现。 | [#1389](https://github.com/thinson/RS-PaperClaw/issues/1389) |
| [20260928] Joint DNN Partitioning and Resource Allocation for Satellite-Terrestrial Collaborative Inference Systems | Liang Wenyu, Fei Zesong, Liu Peng, Wang Xinyi, Zeng Ming | School of Information and Electronics, Beijing Institute of Technology, Beijing, China ( | 面向卫星-地面协同推理，联合优化DNN分割与资源分配以适配LEO卫星约束。 | [#1390](https://github.com/thinson/RS-PaperClaw/issues/1390) |
| [20260928] Temporal Modelling for Burn Scars on Sentinel-3 | Barco Luca, Arnaudo Edoardo, Bragagnolo Andrea, Rossi Claudio, Garza Paolo | Up funded by the Italian Space Agency and the Ministry of University and；Research - Contract No. 2024-5-E.0 - CUP No. I53 D24000060005 | 基于Sentinel-3 OLCI构建时序建模方法，用于火烧迹地语义分割与损伤评估。 | [#1391](https://github.com/thinson/RS-PaperClaw/issues/1391) |
| [20260928] When local gains fail to transfer: Frozen Earth-observation embeddings across wildfires | Stark Philipp, Sopasakis Alexandros, Hall Ola | Department of Human Geography Centre for Mathematical Sciences；Lund University Lund University；Department of Human Geography；Lund University | 发现冻结地球观测嵌入在跨wildfire任务中本地增益无法迁移，揭示迁移局限。 | [#1392](https://github.com/thinson/RS-PaperClaw/issues/1392) |
| [20260928] Spectral Super-Resolution using Spatial-Spectral Residual Operator Networks | Chin Seokhyun | California Institute of Technology | 提出空间-光谱残差算子网络，实现多光谱卫星影像的零样本光谱超分辨率。 | [#1395](https://github.com/thinson/RS-PaperClaw/issues/1395) |
| [20260928] ReVA: A Scene-Centric Dataset Beyond Repetition for Remote Sensing Video Question Answering | Yao Zhen, Wang Likai, Yang Yuming, Zheng Zhihao, Lang Bo, Tang Qiuyu, Sheng Jialu, Xu Jingqi, Yang Yuehai, Barker Jumal, Ying Xiaowen, Mooi Choo Chuah | Lehigh University；University of Southern California；Qualcomm AI Research | 发布场景中心遥感视频问答数据集ReVA，缓解重复样本并强化时空推理评测。 | [#1398](https://github.com/thinson/RS-PaperClaw/issues/1398) |
| [20260928] Remote Sensing Sparse-View 3D Gaussian Splatting via Depth Image-Based Rendering | Kang Jiaming, Zou Zhengxia, Shi Zhenwei | Beihang University | 结合深度图像渲染与3D高斯泼溅，改善遥感稀疏视角的新视角合成质量。 | [#1399](https://github.com/thinson/RS-PaperClaw/issues/1399) |
| [20260928] HyperDAM: Hyperspectral Distractor-Aware Memory with Amodal Expansion for SAM 3 Tracking | Yuzawa Ryoga, Takagi Tasuku | 原文作者栏未列出单位 | 为SAM 3跟踪引入高光谱干扰感知记忆与无模态扩展，提升高光谱视频跟踪鲁棒性。 | [#1405](https://github.com/thinson/RS-PaperClaw/issues/1405) |

## 🔎 观察

- 星上处理与协同推理研究正从算法精度转向原始数据、通信与算力约束下的系统级权衡。
- 迁移学习与基础模型应用出现反思信号：冻结特征并非通用，跨域评估需更严格。

---

Powered by OpenClaw🦞

---

# [20260927](./202609/20260927.md)
## 📌 今日概况

今日共检索候选论文 7 篇；关键词+LLM 智能匹配遥感交叉论文 5 篇；最终纳入日报 5 篇。

今日论文总体呈现出遥感与AI交叉深化趋势。

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260927] QSCP: Beyond Class-Name Prompts for Query-Guided Semantic Change Parsing | Qian Yuan, Ma Jie | School of Information Science and Technology, Beijing Foreign Studies University, Beijing, China ( | 聚焦Remote Sensing、Semantic Change Detection，给出可复现的模型与评测方案。 | [#1379](https://github.com/thinson/RS-PaperClaw/issues/1379) |
| [20260927] Resource-Aware Parameter-Efficient Model Adaptation for Onboard High-Dimensional Data | Zhang Qiyang, Li Xinhao, Shi Lei, Lin Zheng, Wen Jinfeng, Zhou Ao, Wang Shangguang | Beijing University of Posts and Telecommunications；Wuhan University；Communication University of China；University of Luxembourg | 聚焦Hyperspectral Imagery、Low-Rank Adaptation，给出可复现的模型与评测方案。 | [#1381](https://github.com/thinson/RS-PaperClaw/issues/1381) |
| [20260927] The Potential of Nighttime Light Imagery for Detailed Local Economic Analysis | Otomo Shoichi | seasonal weather patterns, regional institutional calendars (such as holiday periods), and origindestination population flows | 聚焦Remote Sensing、Nighttime Light Imagery，给出可复现的模型与评测方案。 | [#1382](https://github.com/thinson/RS-PaperClaw/issues/1382) |
| [20260927] ForeFly: A Dual-Horizon World Action Model for Aerial Vision-Language Navigation | Wang Kunhui, Zhang Xintong, Gao Junyu, Xu Changsheng | State Key Laboratory of Multimodal Artificial Intelligence Systems；Institute of Automation, Chinese Academy of Sciences, Beijing, China；School of Advanced Interdisciplinary Sciences；University of Chinese Academy of Sciences, Beijing, China；Division of Natural and Applied Sciences, Duke Kunshan University, Suzhou, China；Peng Cheng Laboratory, ShenZhen, China | 聚焦UAV、Aerial Vision-Language Navigation，给出可复现的模型与评测方案。 | [#1403](https://github.com/thinson/RS-PaperClaw/issues/1403) |
| [20260927] Correlation Between Nighttime Light and Various Statistical Indicators in Japan | Otomo Shoichi | 原文作者栏未列出单位 | 聚焦Remote Sensing、Nighttime Light，给出可复现的模型与评测方案。 | [#1404](https://github.com/thinson/RS-PaperClaw/issues/1404) |

## 🔎 观察

- 基础模型与遥感任务结合持续增强，评测与推理能力成为关键。
- 多数工作关注算法有效性与泛化，而非硬件实现。

---

Powered by OpenClaw🦞

---

# [20260926](./202609/20260926.md)
## 📌 今日概况

今日共检索候选论文 6 篇；关键词+LLM 智能匹配遥感交叉论文 5 篇；最终纳入日报 5 篇。

今日论文聚焦遥感基础模型与评测基准两大方向。一方面，云去除、变化检测等任务引入通用先验、Copula证据融合等新方法，提升异构观测下的鲁棒性；另一方面，光谱诊断分析基础模型微调策略，同时出现面向建筑环境定量推理与复杂矢量多边形生成的基准，推动视觉语言模型与拓扑保持评估。整体趋势显示，研究正从单一任务模型转向通用化、可解释与标准化评测。

## ✨ 今日亮点

- 云去除提出通用先验，利用异构观测与SAR引导提升泛化。
- 变化检测引入区域局部Copula证据融合，增强异构数据鲁棒性。
- 新基准关注视觉语言定量推理与复杂多边形拓扑生成。

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260926] GeoCR: Learning a Generalist Cloud Removal Prior from Heterogeneous Observations | Do Jeonghyeok, Kim Munchurl | Korea Advanced Institute of Science and Technology (KAIST) | 提出GeoCR，从异构观测中学习通用云去除先验，并利用SAR引导提升泛化能力。 | [#1372](https://github.com/thinson/RS-PaperClaw/issues/1372) |
| [20260926] Region-Local Copula Evidence Fusion for Heterogeneous Remote Sensing Change Detection | Ji Zhiyuan, Yin Junjun, Yang Jian | Department of Electronic Engineering, Tsinghua University, Beijing, P.R；School of Computer and Communication Engineering, University of Science and Technology Beijing, P.R | 提出区域局部Copula证据融合方法，用于异构遥感变化检测，提升融合鲁棒性。 | [#1373](https://github.com/thinson/RS-PaperClaw/issues/1373) |
| [20260926] Reuse or Relearn? A Spectral View of Earth Observation Foundation Models | Mehmet Ozgur Turkoglu, Marsocci Valerio, Dominik J. Mühlematter, Senti Dominik, Schindler Konrad, Aasen Helge | ESA, -lab | 从光谱视角诊断地球观测基础模型，分析微调与重用的奇异子空间差异。 | [#1374](https://github.com/thinson/RS-PaperClaw/issues/1374) |
| [20260926] USAI-Quant: A Quantitative Reasoning Benchmark for Vision-Language Models in Built Environments | Wang Dongdong, Song Qingqi, Chen Yuzhou, Balakrishnan Deepak, Ravi Shankar Srinivasan, Wang Shenhao | University of Florida University of Florida University of Florida University of Florida；University of Florida University of Florida | 构建USAI-Quant基准，评估视觉语言模型在建筑环境中的定量推理能力。 | [#1376](https://github.com/thinson/RS-PaperClaw/issues/1376) |
| [20260926] PolyTopoBench: A Benchmark for Complex Vector Polygon Generation from Remote Sensing Imagery | Liu Zeping, Lao Ni, Sun Weiwei, Wolff Gil, Xie Yiqun, Zhao Liang, Jiao Junfeng, Mai Gengchen | University of Texas at Austin；University of Maryland；Emory University | 提出PolyTopoBench基准，评估从遥感影像生成复杂矢量多边形的拓扑保持能力。 | [#1377](https://github.com/thinson/RS-PaperClaw/issues/1377) |

## 🔎 观察

- 通用先验与证据融合成为提升异构遥感任务鲁棒性的共同思路。
- 评测基准密集出现，反映领域对标准化定量评估的迫切需求。

---

Powered by OpenClaw🦞

---
