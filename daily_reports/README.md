# Daily Reports

最近三天日报（最新在前）：

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

# [20260908](./202609/20260908.md)
## 📌 今日概况

今日共检索候选论文 10 篇；关键词+LLM 智能匹配遥感交叉论文 9 篇；最终纳入日报 9 篇。

今日遥感研究呈现多方向交叉趋势：高光谱图像处理聚焦于可解释性与异常检测，通过低秩张量分解、深度展开等机制提升模型透明度；变化检测与多模态大模型结合，探索从像素级到语义级的定位能力；同时，具身智能与空地协同、星上目标检测等方向也涌现出新方法，强调模型在真实场景中的部署与推理能力。

## ✨ 今日亮点

- 高光谱处理强调可解释框架，融合物理先验与深度展开。
- 多模态大模型应用于遥感变化定位与区域选择。
- 空地协同与星上检测推动智能体向具身化发展。

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260908] Hyperspectral Anomaly Detection via Group Sparse Low-Rank Tensor Factorization With Automatic Anomaly Grouping | Yu Quan, Dai Yu-Hong, Zhang Xiongjun | School of Mathematics and Statistics, Central China Normal University, Wuhan, China；the Key Laboratory of Nonlinear Analysis and Applications (Ministry of Education), Central China Normal University (；State Key Laboratory of Mathematical Sciences, Academy of Mathematics and Systems Science, Chinese Academy of Sciences, Beijing, China；School of Mathematical Sciences, University of Chinese Academy of Sciences, Beijing, China ( | 提出群稀疏低秩张量分解，实现高光谱异常自动分组检测。 | [#335](https://github.com/thinson/RS-PaperClaw/issues/335) |
| [20260908] CoSA: Correlation-Guided Change A ttention with Learnable Residual Gating for Remote Sensing Change Detection | Omar Abdirashid, Park Jonghyuk | Department of Data Science, Graduate School of Kookmin University | 设计相关引导注意力与残差门控，提升遥感变化检测精度。 | [#756](https://github.com/thinson/RS-PaperClaw/issues/756) |
| [20260908] EgoSIS: From Factorized Visual Ego-Transitions to Motion-Canonical Spatial Evidence for UAV Reasoning | Yang Jingpu, Ji Fengxian, Cui Mingxuan, Sun Yilin, Zhang Hang, Zhu Jianhua, Wang Yufeng | Beihang University, Beijing, China；Zhongguancun Academy, Beijing, China；Northeastern University, Shenyang, China；Technology and Engineering Center for Space Utilization, Chinese Academy of Sciences | 通过因子化视觉自我转移，为无人机推理提供运动规范证据。 | [#1254](https://github.com/thinson/RS-PaperClaw/issues/1254) |
| [20260908] Interpretable Hyperspectral Unmixing Framework with Fixed Endmember Prior and Structured Residual Refinement | Guan Ziyi, Zhang Jianping, Liu Qian | of Hunan Province (No. 2025 JJ60883); the Hunan Provincial College Students’ Entrepreneurship Training Program (No. S202510530147 X); and the National College | 构建固定端元先验与结构化残差精炼的可解释高光谱解混框架。 | [#1255](https://github.com/thinson/RS-PaperClaw/issues/1255) |
| [20260908] AXS-Net: Interpretable Deep Unfolding for Hyperspectral Image Denoising via Spectral Basis Unmixing and Structured Noise Refinement | Guan Ziyi, Zhang Jianping, Yang Zheng | Xiangtan University, Xiangtan, Hunan, China | 提出深度展开网络，结合谱基分解去除高光谱结构化噪声。 | [#1256](https://github.com/thinson/RS-PaperClaw/issues/1256) |
| [20260908] TriCCOT: Tri-part Convolutional Conformal Transformer for Onboard Space Object Detection | Dorise Adrien, Bellizzi Marjorie, Cohen Julia, May Stéphane | Centre National d’Etudes Spatiales | 开发三分卷积共形Transformer，用于星上目标检测。 | [#1257](https://github.com/thinson/RS-PaperClaw/issues/1257) |
| [20260908] Towards Embodied Air-Ground Cooperative Object Search: Benchmark, Dataset and Agentic Method | Yu Boao, Chen Zimo, Rao Junreng, Hu Yue, Zhu Zhengqiu, Zhao Yong, Ju Rusheng | National University of Defense Technology；National Key Laboratory of Digital Intelligent Modeling and Simulation | 发布空地协同搜索基准数据集，并设计智能体方法。 | [#1258](https://github.com/thinson/RS-PaperClaw/issues/1258) |
| [20260908] From Coordinates to Candidate Regions: Temporal Change Localization via Region Selection in Remote Sensing Multimodal LLMs | Chung Juwan, Park Sungjune, Kim Yeongyun, Yong Man Ro | Integrated Vision Language Lab, KAIST, South Korea | 利用区域选择策略，实现遥感多模态大模型时间变化定位。 | [#1259](https://github.com/thinson/RS-PaperClaw/issues/1259) |
| [20260908] Dual-Layer Semantic-Spatial Belief Mapping for Aerial Object Goal Navigation | Xiao Jianqiang, Deng Xiang, Sun Yuexuan, Wu Yanjin, Yan Wenbiao, Nie Liqiang | observations, but their frame-level outputs are often noisy, Existing embodied navigation research has advanced along | 构建双层语义空间信念图，用于空中目标导航。 | [#1260](https://github.com/thinson/RS-PaperClaw/issues/1260) |

## 🔎 观察

- 高光谱领域正从黑盒模型转向物理引导的可解释架构，强调先验嵌入。
- 多模态大模型与具身智能结合，推动遥感从静态分析走向动态交互。

---

Powered by OpenClaw🦞

---
