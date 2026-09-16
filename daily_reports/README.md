# Daily Reports

最近三天日报（最新在前）：

# [20260915](./202609/20260915.md)
## 📌 今日概况

今日共检索候选论文 12 篇；关键词+LLM 智能匹配遥感交叉论文 5 篇；最终纳入日报 5 篇。

今日论文聚焦遥感基础模型与下游任务的衔接，涵盖标签效率、时序迁移与跨域泛化。多篇工作探索将预训练嵌入或语言模型迁移至农田制图、光谱时序预测和指代分割，强调独立验证与因果建模。同时，三维重建与多模态时空预测引入风险图引导和异步耦合机制，提升复杂场景下的鲁棒性。整体趋势显示，遥感AI正从单一精度追求转向可迁移、可解释与跨域基准构建。

## ✨ 今日亮点

- 基础模型嵌入用于农田制图，关注标签效率与时间迁移性。
- 光谱时序学习引入因果潜在预测，支持多视野地球表征。
- 指代遥感分割提出跨域基准，评估视觉语言模型泛化能力。

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260915] From Foundation Embeddings to Cropland Maps: Label Efficiency, Temporal Transferability and Independent Human Validation | Mohammad Ammar Mughees, Montefoschi Giovanni, Chen Zhongxin, Maria Antonia Brovelli | Department of Civil and Environmental Engineering, Politecnico di Milano, Milan, Italy | 评估基础嵌入在农田制图中的标签效率、时序迁移性，并引入独立人工验证。 | [#1271](https://github.com/thinson/RS-PaperClaw/issues/1271) |
| [20260915] SPEAR NeXT Causal Latent Forecasting Across Multiple Horizons for Spectral Temporal Earth Representation Learning | Ranjan Rajiv, Singh Udaiveer, Tamaskar Shashank, Saraswat Dharmendra | Plaksha University；Purdue University | 提出SPEAR NeXT，用因果潜在预测实现多视野光谱时序地球表征学习。 | [#1272](https://github.com/thinson/RS-PaperClaw/issues/1272) |
| [20260915] HLC-GS: Risk-Map-Guided Height-Layer Consistency Gaussian Splatting for DSM Reconstruction from Optical Satellite Imagery | Yang Jie, Pi Yingdong, Luo Qiyan, Wang Xiaoyu, Wen Lekang, Wang Mi | State Key Laboratory of Information Engineering in Surveying, Mapping and Remote Sensing, Wuhan University；Hubei Luojia Laboratory；School of Computer Science, Wuhan University | HLC-GS利用风险图引导高度层一致性高斯泼溅，从光学卫星影像重建DSM。 | [#1273](https://github.com/thinson/RS-PaperClaw/issues/1273) |
| [20260915] AsyncCouple-Flow: Asynchronous Cross-Modal Coupling and Flow Matching for Spatio-Temporal Forecasting | Wu Zhixiang, Liu Yining, Zhao Bo, Chen Szu-Yu, Duan Huiran, Lin Chu, Yang Chuanguang | Institute of Computing Technology, Chinese Academy of Sciences, China；Emory University, USA；University of California, Berkeley, USA；Yale University, USA；Stevens Institute of Technology, USA；City University of New York, USA | AsyncCouple-Flow通过异步跨模态耦合与流匹配，处理时空预测中的缺失模态。 | [#1274](https://github.com/thinson/RS-PaperClaw/issues/1274) |
| [20260915] VPRef: A Cross-Domain Benchmark for Referring Remote Sensing Image Segmentation | Liu Quanwei, Huang Tao, Yang Jiaqi, Xiang Wei | College of Science and Engineering, James Cook University, Cairns,, Australia (；College of Science and Engineering, James Cook University, Cairns QLD, Australia and the Center for AI and Data Science Innovation, James Cook University, Cairns QLD, Australia (；Department of Forest and Wildlife Ecology, University of Wisconsin-Madison, Madison, WI USA (；School of Computing, Engineering and Mathematical Sciences, La Trobe University, Melbourne, VIC, Australia ( | VPRef构建跨域基准，评估指代遥感图像分割中视觉语言模型的域适应能力。 | [#1275](https://github.com/thinson/RS-PaperClaw/issues/1275) |

## 🔎 观察

- 基础模型落地更重标签效率与迁移验证，而非单纯追求精度提升。
- 跨域基准与因果建模成为提升遥感模型泛化与可解释性的关键路径。

---

Powered by OpenClaw🦞

---

# [20260910](./202609/20260910.md)
## 📌 今日概况

今日共检索候选论文 5 篇；关键词+LLM 智能匹配遥感交叉论文 1 篇；最终纳入日报 1 篇。

今日候选论文聚焦高光谱与LiDAR联合分类的可解释多模态融合。作者借鉴热传导建模思想，将模态间信息交互类比为热扩散过程，以提升融合机制的可解释性。该工作延续了遥感多模态分类从精度导向向机理可解释方向演进的趋势，也反映出物理启发建模在遥感AI中的持续渗透。

## ✨ 今日亮点

- 以热传导建模高光谱与LiDAR融合，探索可解释多模态分类新路径
- 物理启发式融合机制成为遥感多模态研究的新关注点
- 高光谱与LiDAR联合分类持续向可解释性方向延伸

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260910] Toward Interpretable Multimodal Fusion: Heat Conduction Modeling for Hyperspectral and LiDAR Joint Classification | Wei Kan, Cui Jiahui, Yao Jing, Zhao Xinyu, Wang Lei, Ghamisi Pedram | State Key Laboratory of Remote Sensing and Digital Earth, Aerospace Information Research Institute, Chinese Academy of Sciences, Beijing, China (；the Faculty of Electrical and Computer Engineering, University of Iceland, 101 Reykjavik, Iceland ( | 该文提出热传导建模的可解释多模态融合方法，用于高光谱与LiDAR联合分类。 | [#1269](https://github.com/thinson/RS-PaperClaw/issues/1269) |

## 🔎 观察

- 将物理过程引入融合设计，有望缓解深度模型可解释性不足的问题。
- 当前仅见单篇候选，趋势判断需结合后续更多同类工作验证。

---

Powered by OpenClaw🦞

---

# [20260909](./202609/20260909.md)
## 📌 今日概况

今日共检索候选论文 11 篇；关键词+LLM 智能匹配遥感交叉论文 6 篇；最终纳入日报 6 篇。

今日遥感AI研究覆盖弱监督分割、高光谱降维、小目标检测、视觉语言变化检测、多传感器甲烷羽流探测与开放世界目标检测等方向。趋势上，弱监督与提示引导结合提升高分辨率多光谱水体分割精度；Mamba结构被引入遥感小目标检测以扩大感知范围；四叉树掩码编码将变化检测转化为层级序列生成，衔接视觉语言模型；多传感器异构融合与部分传感器缺失场景受到关注；双曲几何被用于开放世界增量检测以建模未知类别。整体呈现多模态融合、结构化生成与几何表示学习并进的态势。

## ✨ 今日亮点

- 弱监督水体分割引入提示引导局部细化，缓解标签噪声。
- Mamba与YOLO结合，内外扩展感知范围以提升小目标检测。
- 四叉树掩码编码将变化检测转为层级序列，衔接视觉语言模型。

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260909] Beyond Weak Labels: Prompt-Guided Local Refinement for Weakly Supervised Water Segmentation in High-Resolution Multispectral Imagery | Muhammad Farhan Humayun, Imangholiloo Mohammad, Shah Afifah, Westerlund Tomi, Heikkonen Jukka | Department of Computing, University of Turku, Finland；Department of Geoinformatics and Cartography, Finnish Geospatial Research Institute | 提出提示引导局部细化方法，用于高分辨率多光谱影像弱监督水体分割，缓解弱标签噪声。 | [#1262](https://github.com/thinson/RS-PaperClaw/issues/1262) |
| [20260909] Dimensionality Reduction for Hyperspectral Image Classification | Cherifi Mohamed, Mesloub Ammar, Mohammed Nabil El Korso, Touhami Tayeb, Abdennour Hacine Gharbi | Laboratoire Traitement du Signal Laboratoire Antennes et Dispositifs Micro-Ondes Université Paris-Saclay；Laboratoire Antennes et Dispositifs Micro-Ondes Université de Bordj-Bou-Ariridj | 比较PCA与LDA等降维方法在高光谱图像分类中的效果，结合监督分类器评估性能。 | [#1263](https://github.com/thinson/RS-PaperClaw/issues/1263) |
| [20260909] ScopeMamba-YOLO: Widening the Perceptual Scope Inward and Outward for Small Object Detection in Remote Sensing Imagery | Fan Junjie, Mai Yijun, Wei Linduo, Rao Jiayu, Bao Junmin, Jin Qiushi, Li Guijia, Qi Yong | School of Intellectual Property, Nanjing University of Science and Technology, Nanjing, China (；School of Computer Science and Engineering, Nanjing University of Science and Technology, Nanjing, China (；School of Economics and Management, Nanjing University of Science and Technology, Nanjing, China ( | 提出ScopeMamba-YOLO，通过选择性扫描内外扩展感知范围，提升遥感小目标检测。 | [#1264](https://github.com/thinson/RS-PaperClaw/issues/1264) |
| [20260909] From Pixels to Hierarchical Sequences: Quadtree Mask Encoding for Vision-Language Binary Change Detection | An Xiao, Zhang Ruikang, Zhong Chen, Shen Xuli, Sun Jiaxing, Wu Jiang, He Wei | Wuhan University；Peking University；Shanghai Artificial Intelligence Laboratory | 提出四叉树掩码编码，将二值变化检测转为层级序列生成，结合视觉语言模型。 | [#1265](https://github.com/thinson/RS-PaperClaw/issues/1265) |
| [20260909] MethaneFuse: Learning from Multi-Sensor Satellite Observations for Methane Plume Detection | Wang Yuyao, Juliana Y. Leung, Niu Di | Department of Electrical and；University of Alberta；Department of Civil and | 提出MethaneFuse，融合多传感器卫星观测并应对部分传感器缺失，检测甲烷羽流。 | [#1266](https://github.com/thinson/RS-PaperClaw/issues/1266) |
| [20260909] Hyperbolic Geometry for Open-World Object Detection in Remote Sensing Imagery | Li Wuzhou, Zhou Jiawei, Wang Shenghang, Li Xiang | School of Computer Science and Artificial Intelligence, Wuhan Textile University, Wuhan, China (；the Electronic Information School, Wuhan University, Wuhan, China (；the Electrical and Computer Engineering, Ohio State University, Columbus, OH, USA (；School of Artificial Intelligence, Wuhan University, Wuhan, China ( | 将双曲几何引入开放世界遥感目标检测，支持增量学习与未知目标发现。 | [#1267](https://github.com/thinson/RS-PaperClaw/issues/1267) |

## 🔎 观察

- 弱监督与提示学习结合成为高分辨率分割的务实路径，降低像素级标注依赖。
- 多传感器融合与开放世界设定并行推进，反映遥感模型对数据缺失与未知类别的鲁棒性需求。

---

Powered by OpenClaw🦞

---
