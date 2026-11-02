# Daily Reports

最近三天日报（最新在前）：

# [20261030](./202610/20261030.md)
## 📌 今日概况

今日共检索候选论文 5 篇；关键词+LLM 智能匹配遥感交叉论文 2 篇；最终纳入日报 2 篇。

今日研究趋势聚焦于遥感数据的高效利用与领域自适应。一方面，有工作探索直接从卫星影像端到端学习屋顶太阳能潜力，绕过显式几何建模，简化流程并降低对辅助数据的依赖；另一方面，针对SAR时间序列作物分类，提出物理引导的自监督预训练方法，结合极化特征与BERT架构，提升标签稀缺场景下的分类性能。两项研究均体现了减少人工特征工程、增强模型自主表征能力的倾向。

## ✨ 今日亮点

- 端到端学习屋顶太阳能潜力，无需显式几何建模。
- 物理引导自监督预训练，融合极化特征与BERT。
- 两项研究均致力于降低对人工特征和标签的依赖。

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20261030] An Empirical Study on Learning Rooftop Solar Potential from Satellite Imagery Directly Without Explicit Geometry | Lee Joshua | Skyline High School | 实证研究直接从卫星影像端到端学习屋顶太阳能潜力，避免显式几何建模。 | [#1598](https://github.com/thinson/RS-PaperClaw/issues/1598) |
| [20261030] SAR-TS-BERT: Physics-Guided Self-Supervised Pre-Training With Polarimetric Features for SAR Time-Series Crop Classification | Wang Jieqiu, Zhang Yuhan, Zheng Bo, Zhang Shaoming | College of Surveying and Geo-Informatics, Tongji University, Shanghai, China ( | 提出物理引导自监督预训练SAR-TS-BERT，结合极化特征提升作物分类。 | [#1599](https://github.com/thinson/RS-PaperClaw/issues/1599) |

## 🔎 观察

- 端到端学习减少中间几何建模误差，但可解释性与泛化性仍需验证。
- 自监督预训练结合物理特征，有望缓解SAR作物分类标签稀缺问题。

---

Powered by OpenClaw🦞

<!-- rs-pipeline: {"date": "20261030", "source": "oai", "checked_at": "2026-11-02T12:51:57+00:00", "source_complete": true, "candidate_count": 5, "paper_count": 2} -->

---

# [20261029](./202610/20261029.md)
## 📌 今日概况

今日共检索候选论文 9 篇；关键词+LLM 智能匹配遥感交叉论文 5 篇；最终纳入日报 5 篇。

今日研究呈现多学科交叉趋势：量子测量与量子启发计算被引入高光谱小目标检测和伪标签生成，提升遥感数据利用效率；无人机视角与视觉强化学习结合，推动交通信号控制的可泛化策略；计算神经科学方法用于解析地球观测嵌入的可解释性；因果推断约束深度学习，增强热带气旋快速增强预警的物理一致性。整体上，遥感AI正从单纯精度提升转向物理机理融合与可解释性增强。

## ✨ 今日亮点

- 量子测量设计突破无人机高光谱小目标检测的直接成像局限。
- 无人机鸟瞰视角结合视觉强化学习实现可泛化交通信号控制。
- 因果先验约束深度学习提升热带气旋快速增强预警可靠性。

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20261029] Beyond Direct Imaging: Quantum Measurement Design for Small-Target Detection in UAV Hyperspectral Sensing | Qian Qipeng, Jin Jialiang, Wang Shihao, Qian Yuntao | College of Artificial Intelligence, Zhejiang University, Hangzhou, China；Department of Computer Science, Whiting School of Engineering, Johns Hopkins University, Baltimore, MD, USA (；Department of Mathematics, University of Wisconsin-Madison, Madison, WI, USA (；College of Artificial Intelligence, Zhejiang University, Hangzhou, China ( | 提出量子测量设计方法，用于无人机高光谱小目标检测，超越直接成像限制。 | [#1592](https://github.com/thinson/RS-PaperClaw/issues/1592) |
| [20261029] BEVLight: Generalizable Traffic Signal Control from UAV Bird's-Eye Views | Wang Maonan, Cai Yuxin, Liu Junming, Huang Zhengyan, Yu Yi, Wang Ding, Zhang Yifeng, Chen Yirong | The Chinese University of Hong Kong, Shenzhen；Shanghai AI Lab；Nanyang Technological University；National University of Singapore | 利用无人机鸟瞰视角和视觉强化学习，学习可泛化的交通信号控制策略。 | [#1593](https://github.com/thinson/RS-PaperClaw/issues/1593) |
| [20261029] Quantum-Inspired Convolutional Networks for High-Resolution Pseudo-Label Generation from Multimodal Earth Observation Data | Singh Abhishek, Cuozzo Giovanni, Jacob Alexander, Notarnicola Claudia | Institute for Earth Observation, Eurac Research, Bolzano, Italy | 设计量子启发卷积网络，从多模态地球观测数据生成高分辨率伪标签。 | [#1594](https://github.com/thinson/RS-PaperClaw/issues/1594) |
| [20261029] NeurEO: dissecting Earth observation embeddings with computational neuroscience | Thijs L van der Plas, Jacob JW Bakermans, Ioannis N Athanasiadis | Wageningen University \& Research, NL；University College London, UK | 借鉴计算神经科学方法，解析AlphaEarth地球观测嵌入的表征机制。 | [#1595](https://github.com/thinson/RS-PaperClaw/issues/1595) |
| [20261029] Causal-prior-constrained deep learning for rapid-intensification warning of western North Pacific tropical cyclones | Li Xinrui, Jin Yijun, Dong Yifan, Shu Shoujuan | Department of Atmospheric Sciences, School of Earth Sciences, Zhejiang University, Hangzhou, 310058, China；School of Mathematical Sciences, Zhejiang University, Hangzhou, 310058, China | 引入因果先验约束深度学习，实现西北太平洋热带气旋快速增强预警。 | [#1596](https://github.com/thinson/RS-PaperClaw/issues/1596) |

## 🔎 观察

- 量子概念在遥感中从理论走向应用，但当前工作多属启发式借鉴，实际量子优势尚待验证。
- 可解释性与物理约束成为遥感AI新焦点，反映领域从黑箱精度向可信决策的范式转变。

---

Powered by OpenClaw🦞

<!-- rs-pipeline: {"date": "20261029", "source": "oai", "checked_at": "2026-10-30T11:06:04+00:00", "source_complete": true, "candidate_count": 9, "paper_count": 5} -->

---

# [20261028](./202610/20261028.md)
## 📌 今日概况

今日共检索候选论文 6 篇；关键词+LLM 智能匹配遥感交叉论文 2 篇；最终纳入日报 2 篇。

今日两篇论文分别聚焦遥感深度学习可解释性与贝叶斯统计建模。前者诊断超高分辨率建筑损毁评估中的邻域捷径问题，并提出建筑证据插件以抑制虚假关联；后者针对多类别数据构建贝叶斯差异模型，分析五大湖高维水陆转换。研究趋势显示，遥感AI正从单纯提升精度转向模型可靠性诊断与不确定性量化，同时统计方法在高维遥感数据中的应用受到关注。

## ✨ 今日亮点

- 诊断建筑损毁评估中的邻域捷径，提出证据插件抑制虚假关联。
- 构建贝叶斯差异模型，分析五大湖高维水陆转换多类别数据。
- 两篇工作分别从模型诊断与统计建模提升遥感分析可靠性。

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20261028] Neighbourhood shortcuts in building damage assessment from very-high-resolution satellite imagery: diagnosis and a building-evidence plug-in | Guo JianChong, Wan YuTing, Li Kefan, Ma AiLong, Zhong YanFei | State Key Laboratory of Information Engineering in Surveying, Mapping, and Remote Sensing；Wuhan University, 430079, China | 诊断超高分辨率建筑损毁评估中的邻域捷径问题，并提出建筑证据插件以抑制虚假关联。 | [#1589](https://github.com/thinson/RS-PaperClaw/issues/1589) |
| [20261028] An Analysis of High-Dimensional Land-Water Transitions in the Great Lakes via a Bayesian Discrepancy Model for Multinomial Data | Lee Seulki, Jonathan R. Bradley | Department of Statistics and Data Science, University of Missouri | 针对多类别数据构建贝叶斯差异模型，分析五大湖高维水陆转换的统计特征。 | [#1590](https://github.com/thinson/RS-PaperClaw/issues/1590) |

## 🔎 观察

- 遥感深度学习研究开始重视捷径学习诊断，模型可靠性正成为与精度并重的评估维度。
- 贝叶斯高维建模为遥感多类别转换分析提供不确定性量化路径，但计算扩展性仍需验证。

---

Powered by OpenClaw🦞

<!-- rs-pipeline: {"date": "20261028", "source": "oai", "checked_at": "2026-10-30T11:03:54+00:00", "source_complete": true, "candidate_count": 6, "paper_count": 2} -->

---
