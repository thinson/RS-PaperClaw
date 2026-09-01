# Daily Reports

最近三天日报（最新在前）：

# [20260830](./202608/20260830.md)
## 📌 今日概况

今日共检索候选论文 9 篇；关键词+LLM 智能匹配遥感交叉论文 6 篇；最终纳入日报 6 篇。

今日遥感AI研究聚焦于多模态数据融合与高效模型设计。人口估算结合序列模型，海事分割推出新数据集，显著性检测采用Mamba架构，地理基础模型通过对比学习增强语义，视觉语言模型探索地理定位。整体呈现从传统视觉任务向复杂场景理解与跨模态应用拓展的趋势。

## ✨ 今日亮点

- 序列模型用于人口估算，提升行政单元精度
- 海事数据集助力卫星与航拍图像实例分割
- Mamba网络应用于光学遥感显著性检测

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260830] A Hybrid State-Space Approach for Census-Tract Population Estimation | Jackson R. Ye, Alexandre V. Morozov | Rutgers University New Brunswick NJ USA | 混合状态空间模型用于人口普查区人口估算，结合卫星影像提升精度 | [#1203](https://github.com/thinson/RS-PaperClaw/issues/1203) |
| [20260830] MariSat: A Maritime Dataset for Instance Segmentation of Objects in Satellite and Aerial Images | Abbes Amir, Harrabi Ines, Lucas Justin Yirepoa Kinda, Trabelsi Rim, Cabani Adnane, Abdelkefi Fatma | University of Carthage, SUP'COM, LR11 TIC05, MEDIATRON, 2083, Ariana, Tunisia；University of Gabes, Hatem Bettaher IResCoMath Laboratory, Gabes, Tunisia；University of Rouen Normandie, ESIGELEC, IRSEEM | 发布MariSat数据集，支持卫星与航拍图像中海上目标实例分割 | [#1204](https://github.com/thinson/RS-PaperClaw/issues/1204) |
| [20260830] Tensor Orthogonal Subspace Split: Theory and Applications | Miao Jifei, Han Juan, Michael K. Ng, Kit Ian Kou | School of Mathematics and Statistics, Yunnan University, Kunming, Yunnan,, China (；School of Mathematics and Physics, Anhui Jianzhu University, Hefei, Anhui,, China (；Department of Mathematics, Hong Kong Baptist University, Kowloon Tong, Hong Kong, China (；Department of Mathematics, Faculty of Science and Technology, University of Macau, Macau, China ( | 提出张量正交子空间分割理论，应用于多维数据分解与近似 | [#1205](https://github.com/thinson/RS-PaperClaw/issues/1205) |
| [20260830] SPLG-Mamba: Structure-Preserving Local-Global Mamba Network for Salient Object Detection in Optical Remote Sensing Images | Xu Yi, Hou Ruichao, Ren Tongwei, Wu Gangshan | State Key Laboratory for Novel Software Technology, Nanjing University, Nanjing,, Jiangsu, China (；School of Elite Biomedical Engineers and the Institute for Interdisciplinary Intelligent Pharmacy, China Pharmaceutical University, Nanjing, China ( | SPLG-Mamba网络保持结构信息，实现光学遥感图像显著性目标检测 | [#1206](https://github.com/thinson/RS-PaperClaw/issues/1206) |
| [20260830] BEACON: Behavioral and Semantic Enrichment of AlphaEarth Embeddings through Tri-Modal Contrastive Learning | Tian Hao, Cai Heng, Yang Yifan | Department of Geography Department of Geography Department of Geography；Texas A&M University Texas A&M University Texas A&M University；College Station, TX, USA College Station, TX, USA College Station, TX, USA；Earth observation to human-centered urban analytics；built environment, institutional functions, and mobility behaviors；SIGSPATIAL ’26, Riverside, CA, USA Point-of-Interests (POIs) information provide human-centered | BEACON通过三模态对比学习丰富地理嵌入，增强城市功能理解 | [#1207](https://github.com/thinson/RS-PaperClaw/issues/1207) |
| [20260830] GeoAgent: Evaluating VLM Geolocalization Through Embodied Navigation | Mukherjee Arka, Roy Soham, Trivedi Kartikeya, Ghosh Shreya | KIIT Bhubaneswar；IIT Bhubaneswar | GeoAgent基准评估视觉语言模型在具身导航中的地理定位能力 | [#1208](https://github.com/thinson/RS-PaperClaw/issues/1208) |

## 🔎 观察

- 研究向跨模态融合演进，如结合卫星影像与POI数据，提升城市分析语义深度
- 高效架构如Mamba和状态空间模型受关注，平衡精度与计算效率

---

Powered by OpenClaw🦞

---

# [20260829](./202608/20260829.md)
## 📌 今日概况

今日共检索候选论文 4 篇；关键词+LLM 智能匹配遥感交叉论文 2 篇；最终纳入日报 2 篇。

今日遥感AI研究聚焦于InSAR相位恢复与跨视角定位两大方向。前者提出几何感知的伪监督方法，实现大规模时序InSAR堆栈的零样本泛化，提升形变监测精度；后者探索地面到卫星的定位技术，用于无约束图像集合的3D场景重建，增强地理空间感知能力。两项工作均体现了深度学习与遥感数据的深度融合，推动自动化、高精度的地表观测应用。

## ✨ 今日亮点

- InSAR相位恢复迈向零样本泛化，提升时序监测效率
- 跨视角定位助力3D重建，增强无约束场景适应性
- 伪监督与几何感知结合，减少标注依赖

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260829] FiLM-GPNet: Geometry-Aware Pseudo-Supervised Phase Restoration with Zero-Shot Generalization for Large Temporal InSAR Stacks | Demil Getnet, Muhammad Farhan Humayun, Westerlund Tomi, Heikkonen Jukka, Oussalah Mourad | University of Oulu；University of Turku | 提出FiLM-GPNet，利用几何感知伪监督实现大规模InSAR堆栈相位恢复的零样本泛化 | [#1200](https://github.com/thinson/RS-PaperClaw/issues/1200) |
| [20260829] Ground-to-Satellite Localization in Unconstrained Image Collections for 3D Scene Reconstruction | Daruna Angel, Southall Ben, Niluthpol Chowdhury Mithun, Minhas Kshitij, Meegan Nicholas, Wang Qiao, Matei Bogdan, Samarasekera Supun, Kumar Rakesh | Center for Vision Technologies, SRI International, Princeton, NJ, USA | 提出地面到卫星定位方法，用于无约束图像集合的3D场景重建，提升跨视角匹配精度 | [#1201](https://github.com/thinson/RS-PaperClaw/issues/1201) |

## 🔎 观察

- 研究趋势偏向利用伪监督和几何先验减少对人工标注的依赖，提升模型泛化能力
- 跨视角定位与3D重建结合，显示遥感与计算机视觉技术融合加深，应用场景更广

---

Powered by OpenClaw🦞

---

# [20260828](./202608/20260828.md)
## 📌 今日概况

今日共检索候选论文 10 篇；关键词+LLM 智能匹配遥感交叉论文 6 篇；最终纳入日报 6 篇。

今日遥感AI研究聚焦于多模态融合与生成模型，涉及建筑损伤评估、跨模态图像翻译、无人机三维重建及目标搜索等任务。同时，出现面向变化检测的综合性基准，强调方法评估的可靠性与公平性。整体趋势显示，大语言模型与几何感知机制正逐步融入遥感数据处理流程，推动自动化与智能化水平提升。

## ✨ 今日亮点

- 建筑损伤评估转向文本序列预测，创新建模方式。
- 跨模态翻译引入目标先验解耦训练，提升生成质量。
- 无人机感知强调几何对齐，增强多模态融合鲁棒性。

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260828] GeBDA: Building Damage Assessment as Text-Based Sequence Prediction | Dietrich Olivier, Sapkota Krishna, Schindler Konrad, Beryozkin Genady | ETH Zurich；Google | 提出GeBDA，将建筑损伤评估转化为自回归文本序列预测任务。 | [#1193](https://github.com/thinson/RS-PaperClaw/issues/1193) |
| [20260828] Learning the Target Priors Before Image Translation: A Decoupled Training Paradigm for Cross-Modal Image Translation in Remote Sensing | Hu Keyan, Wang Mingtao, Zhou Ziyu, Shi Tiandong, Li Haifeng, Qi Ji, Tao Chao | Central South University, Changsha, China；Wuhan University, Wuhan, China | 提出解耦训练范式，先学习目标先验再用于跨模态图像翻译。 | [#1194](https://github.com/thinson/RS-PaperClaw/issues/1194) |
| [20260828] GeoFF3D: Coordinate-Anchored Feed-Forward Reconstruction for Large-Scale UAV Mapping | Yang Xiang, Wang Yongli, Zhang Yunsheng | School of Geosciences and Info-Physics, Central South University, Changsha, China；Hunan Engineering Research Center of 3 D Real Scene Construction and Application Technology, Changsha, China；College of Electronic Science and Technology, National University of Defense Technology, Changsha, China | GeoFF3D利用坐标锚定前馈重建，实现大规模无人机地图构建。 | [#1195](https://github.com/thinson/RS-PaperClaw/issues/1195) |
| [20260828] Spatial-Semantic Reasoning using Large Language Models for Efficient UAV Search Operations | Maletic Marin, Peti Marijana, Petrovic Tamara, Bogdan Stjepan | Authors are with the University of Zagreb Faculty of；Electrical Engineering and Computing, LARICS (Laboratory Rather than solely specifying an object category, L-ZSON | 利用大语言模型进行空间语义推理，提升无人机搜索效率。 | [#1196](https://github.com/thinson/RS-PaperClaw/issues/1196) |
| [20260828] A comprehensive and trustworthy benchmark of AI methods for change detection in Earth observation | Tomanič Tadej, Baudhuin Alice, Sotošek Jan, Brence Jure, Panov Panče, Simidjievski Nikola, Kocev Dragi | University of Ljubljana, Faculty of Mathematics and Physics；Department of Knowledge Technologies, Jo zef Stefan Institute；Télécom Paris, Institut Polytechnique de Paris | 构建变化检测AI方法综合基准，强调评估的全面性与可信度。 | [#1197](https://github.com/thinson/RS-PaperClaw/issues/1197) |
| [20260828] GAAT: Geometry-Aware Alignment Transformer for Multimodal UAV Perception | Yang Jingpu, Tang Debin, Sun Yilin, Ji Fengxian, Zhu Jiahua, Ding Wenrui, Wang Yufeng | systems often provide only global or image-center alignment；center consistency under synchronized view transformations；transfer performance, establishing GAAT as a state-of-the-art Residual patch-center misalignment affects both contrastive；Patch-Center Alignment, Geometry-Aware Alignment, UAVMeta；Beihang University, Beijing, China；Zhongguancun Academy, Beijing, China | GAAT通过几何感知对齐Transformer，改善无人机多模态感知。 | [#1198](https://github.com/thinson/RS-PaperClaw/issues/1198) |

## 🔎 观察

- 文本序列预测与生成先验的引入，反映遥感任务向语言模型融合的趋势。
- 几何对齐与空间推理的强调，表明无人机应用对位置信息准确性的高要求。

---

Powered by OpenClaw🦞

---
