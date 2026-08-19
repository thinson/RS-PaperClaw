# Daily Reports

最近三天日报（最新在前）：

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

# [20260816](./202608/20260816.md)
## 📌 今日概况

今日共检索候选论文 7 篇；关键词+LLM 智能匹配遥感交叉论文 6 篇；最终纳入日报 6 篇。

今日遥感AI研究聚焦于高效感知与智能解译，涵盖无人机影像的微小目标检测、裂缝分割及4K视频边缘计算，同时探索遥感基础模型的视觉-语言对齐与边界感知分割，并引入材料发现中的迭代反馈机制，整体呈现从模型精度向轻量化、标签高效与跨域融合发展的趋势。

## ✨ 今日亮点

- 无人机影像感知向边缘计算与标签高效方向深化
- 遥感分割注重边界感知与层次特征自适应细化
- 基础模型探索视觉-语言对齐以提升泛化能力

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260816] Synthesizing like a chemist: an iterative, feedback-driven loop for materials discovery | Sheng Fang, Steven B. Torrisi, Volk Amanda, Tran Kevin, Nakano Koki, Brian W. Anthony, Buonassisi Tonio | Department of Mechanical Engineering, Massachusetts Institute of Technology；Toyota Research Institute | 材料发现采用迭代反馈循环，结合语言模型与贝叶斯优化提升合成效率 | [#1123](https://github.com/thinson/RS-PaperClaw/issues/1123) |
| [20260816] MITE-Net: SWaP-Optimized 4K Video Tiny Target Perception for Embodied Edge SAR | Xu Mingshuo, Hua Mu, Peng Jigen, Wang Qi, Yue Shigang | School of Mathematics and Computing Science, University of Leicester, Leicester LE1 7 RH, UK；the Machine Life and Intelligence Research Center, Guangzhou University, Guangzhou, China | MITE-Net优化SWaP，实现边缘端4K视频微小目标实时感知 | [#1124](https://github.com/thinson/RS-PaperClaw/issues/1124) |
| [20260816] CrevasseSeg: A Label-Efficient UAV Crevasse Segmentation Framework | Wallace Steven, William D Harcourt, Hann Richard, Durrant Aiden, Sripada Somayajulu, Leontidis Georgios | School of Natural and Computing Sciences, University of Aberdeen, UK；Interdisciplinary Institute, University of Aberdeen, UK；School of Geosciences, University of Aberdeen, UK；Department of Engineering Cybernetics, Norwegian University of Science and Technology, Norway；School of Computing Sciences, University of East Anglia, UK；Department of Physics and Technology, UiT The Arctic University of Norway；(UAV) imagery matters for glaciological research | CrevasseSeg利用自监督学习，减少标注需求实现无人机裂缝分割 | [#1125](https://github.com/thinson/RS-PaperClaw/issues/1125) |
| [20260816] BASeg: Boundary-Aware Remote Sensing Segmentation with Structural Penalties | Song Yuexi, Sun Kailai, Wang Zhuoyu, He Mingyi, Paul Pu Liang, Wang Shenhao, Zhao Jinhua | National University of Singapore；Singapore-MIT Alliance for Research and Technology；Massachusetts Institute of Technology；University of Florida | BASeg引入结构惩罚损失，增强遥感图像边界感知分割精度 | [#1126](https://github.com/thinson/RS-PaperClaw/issues/1126) |
| [20260816] Hierarchical Adaptive Feature Refinement Network for VHR Remote Sensing Image Segmentation | Cao Shuaishuai, Tang Meng, Peng Shuwei, Liu Xuan, Huang Min, Chen Jie, Niu Jiacheng, Chen Yong, Akpokodje Edore, Lin Hui | School of Information Science and Technology, Southwest Jiaotong University；School of Computer Science and Artificial Intelligence, Wuhan University of Technology；School of Electronic and Information Engineering, Beihang University；School of Surveying and Geo-Informatics, Shandong Jianzhu University；School of Geography and Environment, Jiangxi Normal University；School of Computer Science and Engineering, University of Electronic Science and Technology of China；School of Computer Science and Technology, Harbin Institute of Technology；School of Computer Science and Engineering, Nanyang Technological University；School of Geography and Remote Sensing, Guangzhou University；Institute of Space and Earth Information Science, The Chinese University of Hong Kong | 层次自适应细化网络结合频率分析，提升超高分辨率影像分割效果 | [#1127](https://github.com/thinson/RS-PaperClaw/issues/1127) |
| [20260816] AlignJEPA: Predictive Vision-Language Alignment for Remote Sensing Foundation Models | Md Aminur Hossain, Vaghasiya Omkumar, Rajeev Ranjan Dwivedi, Kurmi Vinod, Banerjee Biplab | Vinod Kurmi3, and Biplab Banerjee2；Space Applications Centre, ISRO, Ahmedabad, India；CSRE, Indian Institute of Technology Bombay, India；Indian Institute of Science Education and Research (IISER) Bhopal, India | AlignJEPA通过预测性对齐，增强遥感基础模型的视觉-语言检索能力 | [#1128](https://github.com/thinson/RS-PaperClaw/issues/1128) |

## 🔎 观察

- 研究明显向轻量化与边缘部署倾斜，强调实际应用中的计算约束
- 标签高效与自监督方法成为热点，反映标注成本对遥感AI的制约

---

Powered by OpenClaw🦞

---
