# Daily Reports

最近三天日报（最新在前）：

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

# [20260827](./202608/20260827.md)
## 📌 今日概况

今日共检索候选论文 10 篇；关键词+LLM 智能匹配遥感交叉论文 5 篇；最终纳入日报 5 篇。

今日遥感AI研究聚焦于高分辨率影像的精细目标识别、基础模型的时间敏感性分析、自监督扩散模型在高光谱图像修复中的应用、SAR差分相位保持的深度展开网络，以及基于损失对齐的零样本木本清除检测。这些工作展示了深度学习方法在遥感数据解译中的多样化应用，并强调了模型泛化能力与物理约束的融合。

## ✨ 今日亮点

- 高分辨率影像圣诞树种植园检测结合硬负挖掘。
- Tessera嵌入时间敏感性分析助力土地覆盖制图。
- 自监督扩散框架实现高光谱图像修复无需预训练。

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260827] Detection of Christmas tree plantations from high-resolution aerial imagery. A case study in the French Morvan | Razzano Francesca, Dalsasso Emanuele, Baysse-Lainé Adrien, Silvia Liberata Ullo, Schirinzi Gilda, Chanussot Jocelyn | Engineering Department, University of Naples Parthenope, Naples, Italy；the Engineering Department, University of Sannio, Benevento, Italy；CNRS Délégation Alpes: Grenoble, Auvergne-Rhône-Alpes, France | 利用高分辨率航拍影像和语义分割检测法国莫尔万圣诞树种植园。 | [#1187](https://github.com/thinson/RS-PaperClaw/issues/1187) |
| [20260827] Temporal Sensitivity Analysis of Tessera Embeddings | Guerrero-Viu Julia, López-Cifuentes Alex, Pérez-Villar Ignacio, Pacifici Fabio | Universidad de Zaragoza；University of California；AI Center, RMS | 评估Tessera嵌入对时间变化的敏感性，用于土地覆盖分类。 | [#1188](https://github.com/thinson/RS-PaperClaw/issues/1188) |
| [20260827] Hyperspectral Diffusion Equivariant Imaging (HyDiff-EI): A Self-supervised Framework for Hyperspectral Image Inpainting | Li Shuo, Davies Mike, Yaghoobi Mehrdad | Institute for Digital Communications, School of self-supervised diffusion framework and does not require pre- Engineering, University of Edinburgh；School of Engineering, University of Edinburgh. remote sensing or RGB datasets；School of Engineering, University of Edinburgh | 提出自监督扩散等变成像框架，实现高光谱图像修复。 | [#1189](https://github.com/thinson/RS-PaperClaw/issues/1189) |
| [20260827] DP-JMRNet: A Deep Unfolding Network for Differential Phase Preservation in Sparse Bitemporal SAR Reconstruction | Bao Juncheng, Zhang Zhen, George P. Petropoulos | College of Information Science and Engineering, Hohai University, Changzhou, China (；Department of Geography, Harokopio University of Athens, Athens, Greece ( | 深度展开网络DP-JMRNet保持稀疏双时相SAR差分相位。 | [#1190](https://github.com/thinson/RS-PaperClaw/issues/1190) |
| [20260827] Learning Woody Clearing With Loss Alignment for Zero-Shot Regrowth and Woody Segmentation | Backman Kal, Wood Jared, Roff Adam | the New South Wales Department of Climate Change, Energy, the Environment and Water, Parramatta,, NSW, Australia | 损失对齐实现零样本木本清除检测与再生长分割。 | [#1191](https://github.com/thinson/RS-PaperClaw/issues/1191) |

## 🔎 观察

- 自监督与零样本方法兴起，减少对标注数据依赖。
- 物理约束（如相位保持）与深度网络结合成趋势。

---

Powered by OpenClaw🦞

---

# [20260826](./202608/20260826.md)
## 📌 今日概况

今日共检索候选论文 9 篇；关键词+LLM 智能匹配遥感交叉论文 3 篇；最终纳入日报 3 篇。

今日遥感AI研究聚焦于智能预测、视觉语言模型适配及无人机图像分割。行星预测引擎结合基础模型嵌入实现自主地理空间预测；半监督CLIP适配提升图像分类效率；零样本分割方法针对复杂无人机影像中的通信塔组件识别。整体趋势显示，模型正从单一任务向多模态融合与自动化演进。

## ✨ 今日亮点

- 自主地理空间预测引擎集成基础模型嵌入，提升预测智能化水平。
- 半监督CLIP适配方法减少标注依赖，增强场景分类泛化能力。
- 零样本分割结合显著性深度条件，攻克无人机影像复杂目标识别。

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260826] Planetary Prediction Engine: Autonomous Geospatial Prediction via Intelligent Data Selection and Foundation Model Embeddings | Ma Evelyn, Rama Kumar Pasumarthi, Shafin Kishwar, Sharma Mandar, Sun Mimi, Sadeghi Hamed, Dav M. Ebengo, Onesime Mbulayi, Solomakhin Rouslan, Wamburu John, Ogallo William, Walcott-Bryant Aisha, Chen Sanxing, Muslim Arbaaz, Mayer Yael, Ho Ronald, Lee Roy, Alcantara Ruth, Diack Abdoulaye, ..., Shetty Shravya | Google Research；Institut National de Recherche Biomédicale, Democratic Republic of Congo | 提出行星预测引擎，通过智能数据选择和基础模型嵌入实现自主地理空间预测。 | [#1183](https://github.com/thinson/RS-PaperClaw/issues/1183) |
| [20260826] Semi-Supervised Adaptation of Vision-Language Models for Image Classification | Mohamed L. Mekhalfi, Mohamad M. Al Rahhal, Bazi Yakoub, Salah E. Khenfer, Shi Mingdeng, Zou Hua, Zuair Mansour | the Applied Computer Science Department, College of Applied Computer Science, King Saud University,, Riyadh, Saudi Arabia；the Computer Engineering Department, College of Computer and Information Sciences, King Saud University,, Riyadh, Saudi Arabia；the Key Laboratory of Tarim Oasis Agriculture, College of Information Engineering, Tarim University, Aral, China；School of Computer Science, Wuhan University,, Wuhan, China | 采用半监督方式适配视觉语言模型，提升图像分类性能并降低标注成本。 | [#1184](https://github.com/thinson/RS-PaperClaw/issues/1184) |
| [20260826] Saliency-Depth Conditioning for Zero-Shot Segmentation of Communication-Tower Components in Cluttered UAV Imagery | Lesani Ali, Chul Min Yeum, Kang Su-Min | Computer Vision for Smart Structures (CViSS) Lab, Waterloo, Canada；University of Waterloo, Waterloo, Canada；School of Architecture, Soongsil University, Seoul, South Korea | 利用显著性深度条件引导零样本分割，准确识别无人机图像中的通信塔组件。 | [#1185](https://github.com/thinson/RS-PaperClaw/issues/1185) |

## 🔎 观察

- 基础模型嵌入正成为地理空间预测的核心，推动AI系统向自主化发展。
- 半监督与零样本技术受关注，旨在缓解遥感领域标注数据稀缺问题。

---

Powered by OpenClaw🦞

---
