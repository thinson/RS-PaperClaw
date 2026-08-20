# Daily Reports

最近三天日报（最新在前）：

# [20260819](./202608/20260819.md)
## 📌 今日概况

今日共检索候选论文 6 篇；关键词+LLM 智能匹配遥感交叉论文 5 篇；最终纳入日报 5 篇。

今日遥感AI研究聚焦无人机视觉感知与SAR目标检测。视觉定位方面，GrabVG引入图注意力机制提升无人机图像定位精度；SLAM与视觉里程计评估研究为高空无人机导航提供基准。SAR领域，SED-FOD通过散射感知专家分解解决跨传感器小样本检测。此外，地理空间机器学习应用于电力线资产风险建模，拓展遥感技术行业落地场景。

## ✨ 今日亮点

- 无人机视觉定位结合图注意力机制，提升目标定位精度。
- SAR跨传感器小样本检测引入散射感知专家分解。
- 电力线风险建模集成遥感与地理空间机器学习。

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260819] GrabVG: Graph-Attentive Binding for Visual Grounding in UAV Imagery | Wang Chaowei, Di Yan, Sun Jingjun, Liu Baozhe, Tian Jiaxu, Li Yuheng, Guo Guangqian, Gao Shan | Northwestern Polytechnical University；Harbin Institute of Technology；The Hong Kong Polytechnic University | 提出GrabVG，用图注意力绑定提升无人机图像视觉定位性能。 | [#1141](https://github.com/thinson/RS-PaperClaw/issues/1141) |
| [20260819] SED-FOD: Scattering-Aware Expert Decomposition for Few-Shot Cross-Sensor SAR Object Detection | Yang Shu, Chen Zhen, Jiang Zhiyu, Li Yanlei, Liang Xingdong | the National Key Laboratory of Microwave Imaging Technology, Aerospace Information Research Institute, Chinese Academy of Sciences, Beijing, China；School of Electronic, Electrical and Communication Engineering, University of Chinese Academy of Sciences, Beijing, China | SED-FOD通过散射感知专家分解，实现跨传感器SAR小样本检测。 | [#1142](https://github.com/thinson/RS-PaperClaw/issues/1142) |
| [20260819] Evaluation of Monocular SLAM Systems on High-Altitude Nadir UAV Footage | Spagnolo Gašper, Dobrevski Matej, Skočaj Danijel | Faculty of Computer and Information Science, University of Ljubljana, Večna pot 113, Ljubljana, Slovenia | 评估单目SLAM在高空正射无人机视频上的表现，提供基准。 | [#1143](https://github.com/thinson/RS-PaperClaw/issues/1143) |
| [20260819] Evaluation of Image Matching Methods for Visual Odometry on UAVs | Spagnolo Gašper, Luka Čehovin Zajc, Dobrevski Matej | Faculty of Computer and Information Science, University of Ljubljana | 对比多种图像匹配方法用于无人机视觉里程计，分析性能差异。 | [#1144](https://github.com/thinson/RS-PaperClaw/issues/1144) |
| [20260819] Scalable Geospatial Machine Learning for Power-Line Asset Risk: Integrating Remote Sensing for Lightning and Vegetation Risk Modelling | Sokolovsky Artur, Merai Bhavik, Jafari Moe, Chen Muen | SA Power Networks | 利用遥感与机器学习对电力线雷击和植被风险进行可扩展建模。 | [#1145](https://github.com/thinson/RS-PaperClaw/issues/1145) |

## 🔎 观察

- 无人机视觉研究从单一模型走向系统评估，注重实际部署性能。
- SAR检测向跨传感器泛化发展，专家分解成为小样本学习新思路。

---

Powered by OpenClaw🦞

---

# [20260818](./202608/20260818.md)
## 📌 今日概况

今日共检索候选论文 6 篇；关键词+LLM 智能匹配遥感交叉论文 4 篇；最终纳入日报 4 篇。

今日研究聚焦于高分辨率SAR与光学数据的协同应用，涵盖建筑高度估计、云覆盖下的水体分割、雷达数据压缩对目标检测的影响，以及基于卫星图像时间序列的牧场恢复监测。研究趋势显示，深度学习与地理加权方法在遥感任务中持续深化，同时任务导向的数据质量评估受到关注。

## ✨ 今日亮点

- SAR与光学数据互补用于建筑高度估计
- 云覆盖下SAR与合成NDWI融合分割水体
- 任务导向评估雷达数据压缩对检测的影响

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260818] Spatially explicit feature importance for building height estimation using research-access high-resolution SAR and optical sensors | Iablonovski Guilherme, Frison Pierre-Louis, Tatiana Silva da Silva | height estimation using research-access highresolution SAR and optical sensors；Université Gustave Eiffel, Géodata 2nd Pierre-Louis Frison 3rd Tatiana Silva da Silva；Paris, IGN, LASTIG, F-77454 Marne- Université Gustave Eiffel, Géodata Programa de Pós-Graduação em；under scientific research licenses, TerraSAR-X StripMap and；no cost through the DLR science program, and PlanetScope；backscatter and InSAR occupy complementary spatial niches, Research Program, which provide medium-high spatial | 利用高分辨率SAR和光学数据，通过空间显式特征重要性提升建筑高度估计精度。 | [#1136](https://github.com/thinson/RS-PaperClaw/issues/1136) |
| [20260818] Monitoring Pasture Restoration from Satellite Image Time Series: Caveats and Opportunities | Sartorius Linnea, Randahl Isak, Delia Fano Yela, Andersson Georg, Jamali Sadegh, Pirinen Aleksis | Lund University；RISE Research Institutes of Sweden；Swedish Centre for Impacts of Climate Extremes (CLIMES) | 基于卫星图像时间序列监测牧场恢复，探讨了数据和方法中的注意事项与机遇。 | [#1137](https://github.com/thinson/RS-PaperClaw/issues/1137) |
| [20260818] To Remove or Not to Remove Clouds: A Comparative Analysis and Fusion of Raw SAR and Synthetic NDWI for Overcast Water Segmentation | Saleh Sakib Ahmed, Nowreen Sara, M. Sohel Rahman | Computer Science and Engineering, Bangladesh University of Engineering and Technology, Palashi；Institute of Water and Flood Management, Bangladesh University of Engineering and Technology；or simply process the raw SAR directly? Focusing on water body segmentation, this research addresses this exact | 比较原始SAR与合成NDWI在阴天水体分割中的表现，提出融合策略。 | [#1138](https://github.com/thinson/RS-PaperClaw/issues/1138) |
| [20260818] Task-Based Evaluation of Raw Radar Data Compression: A Pre-Registered Study of Where Classical Codecs Fail to Preserve Target Detection, and Why | Eric Michael Chrabot | Air Force Research Laboratory (AFRL) Gotcha ground moving；Force Research Laboratory (AFRL) made this point about | 预注册研究评估原始雷达数据压缩对目标检测的影响，揭示经典编解码器的失效原因。 | [#1139](https://github.com/thinson/RS-PaperClaw/issues/1139) |

## 🔎 观察

- 多传感器融合成为提升遥感反演鲁棒性的主流路径，尤其在地形复杂或天气受限场景。
- 任务导向的数据压缩评估兴起，强调从下游应用需求出发优化数据链路，而非仅关注保真度。

---

Powered by OpenClaw🦞

---

# [20260817](./202608/20260817.md)
## 📌 今日概况

今日共检索候选论文 14 篇；关键词+LLM 智能匹配遥感交叉论文 5 篇；最终纳入日报 5 篇。

今日遥感研究聚焦于提升模型在标注数据稀缺条件下的性能，涵盖半监督语义分割、高光谱图像分类与植物性状反演。同时，合成数据增强被用于农业灾害检测，而GNSS拒止环境下的跨平台地理配准问题也得到关注。整体趋势显示，深度学习方法与数据增强策略在遥感应用中持续深化。

## ✨ 今日亮点

- 半监督学习结合特征记忆库，提升遥感分割精度。
- 光谱转图像策略增强2D-CNN植物性状反演能力。
- 扩散模型合成数据助力战损农田检测与增强。

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260817] Bridging the Gap between Labeled and Unlabeled Data via Unified Flow with Feature Memory Bank | Wang Shanwen, Sun Xin, Hong Danfeng, Dong Junyu, Patrick Le Callet | Faculty of Data Science, City University of Macau,, SAR Macao, China；School of Automation, Southeast University, Nanjing,, China；Department of Computer Science and Technology, Ocean University of China, Qingdao, China；Nantes Université, Ecole Centrale Nantes, CAPACITES SAS, CNRS, LS2 N, UMR, Nantes, France | 提出统一流与特征记忆库，弥合半监督分割中标注与未标注数据差距。 | [#1130](https://github.com/thinson/RS-PaperClaw/issues/1130) |
| [20260817] Turning spectra into images improves plant trait retrieval with 2D-CNNs | Lopatin Javier, Kattenborn Teja, Cherif Eya, Moreno Sebastián | Center for Climate Resilience Research (CR)2, University of Chile, Santiago, Chile, 8370449；Sensor-based Geoinformatics (geosense), University of Freiburg, Freiburg, Breisgau, Germany；Institute for Earth System Science and Remote Sensing, Leipzig University, Germany | 将光谱数据转为图像格式，利用2D-CNN提升植物性状反演精度。 | [#1131](https://github.com/thinson/RS-PaperClaw/issues/1131) |
| [20260817] Synthetic Data Augmentation for Satellite-Based Analysis of Battle-Damaged Agricultural Fields in Ukraine | Sumyk Marta, Kosovan Oleksandr, Voitsitska Iryna | Ukrainian Catholic University, Lviv, Ukraine | 采用扩散模型生成合成数据，增强卫星影像中战损农田的检测能力。 | [#1132](https://github.com/thinson/RS-PaperClaw/issues/1132) |
| [20260817] Marker-Constrained Pose-Graph Correction for Cross-Platform Georeferencing in GNSS-Denied Environments | Giberna Marco, Jose Luis Sanchez Lopez, Voos Holger | Automation and Robotics Research Group, Interdisciplinary Centre for Security, Reliability；and Trust (SnT), University of Luxembourg；Faculty of Science, Technology and Medicine, University of Luxembourg, 4365 | 利用标记约束的位姿图校正，实现GNSS拒止环境下的跨平台地理配准。 | [#1133](https://github.com/thinson/RS-PaperClaw/issues/1133) |
| [20260817] Convolution-Free Holistic Multivariance Decomposition Layer for Efficient Hyperspectral Image Classification Tensor Networks | Tuna Süha, Başar Ülker | aIstanbul Technical University, Informatics Institute；bIstanbul Esenyurt University, Faculty of Business and Management Sciences；Department of Management Information Systems, Esenyurt, 34517, \.Istanbul, Türkiye | 提出无卷积的多元分解层，基于张量网络高效分类高光谱图像。 | [#1134](https://github.com/thinson/RS-PaperClaw/issues/1134) |

## 🔎 观察

- 半监督与数据增强技术成为应对遥感标注稀缺的主流路径。
- 张量网络与无卷积设计开始应用于高光谱分类，追求效率与精度平衡。

---

Powered by OpenClaw🦞

---
