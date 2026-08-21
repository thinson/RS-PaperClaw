# Daily Reports

最近三天日报（最新在前）：

# [20260820](./202608/20260820.md)
## 📌 今日概况

今日共检索候选论文 9 篇；关键词+LLM 智能匹配遥感交叉论文 3 篇；最终纳入日报 3 篇。

今日遥感AI研究聚焦于数据基础设施与安全认证两大方向。一是提出网络中心化的本地部署架构，以应对跨大西洋机构在EO数据访问中的带宽与存储瓶颈，强调可复制性与联邦化。二是探索量子-经典神经网络用于SAR卫星物理层认证，提升信号安全性。三是通过地理隔离策略改进自监督学习，实现可扩展的遥感表征学习，减少对大规模标注数据的依赖。

## ✨ 今日亮点

- 本地化EO数据架构强调网络中心设计，可复制性强。
- 量子-经典网络为SAR物理层认证提供新思路。
- 地理隔离自监督学习提升遥感表征可扩展性。

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260820] Design and Empirical Evaluation of a Network-Centric, On-Premises Architecture for Earth Observation Data Access | Pinelo João, Gonçalves João, Willett Denis, Ruhela Amit, Steinmoeller Derek, Mendoza Uriel, Pelumi S. Alao, Ronald Soares Lopes, Rogerio Atem de Carvalho, Mattos Pedro | AIR Centre, Azores, Portugal；North Carolina Institute for Climate Studies The dominant response has been migration to public cloud；Texas Advanced Computing Center (TACC), Copernicus Data Space Ecosystem provides cloud-based access；University of Texas at Austin, USA；University of Waterloo, Waterloo, Ontario, Canada Program (NODD) [1] provides；Laboratorio Nacional de Observación de la Tierra；National Space Research and Development Agency；Instituto Federal Fluminense (IFF), Brazil Azores connect to mainland Europe by a single submarine cable；research data federation; infrastructure procurement；exceed the transfer and storage capacity of most institutional；organisations, but institutions across the Atlantic basin face；depends on the bandwidth of the underlying network fabric, a The model is designed to be replicable: an institution that builds；GbE fabric, a of the first operational Atlantic Cloud node: the AIR Data Centre；We characterise the fabric under sustained parallel load, evaluate serve the AIR Centre’s EO programmes — including an Internal；institutions characterise the federation primitive the model | 设计并评估网络中心化本地架构，解决跨大西洋EO数据访问带宽瓶颈。 | [#1147](https://github.com/thinson/RS-PaperClaw/issues/1147) |
| [20260820] QUASAR: A Quantum-Classical Neural Network for SAR Satellite Physical-Layer Authentication | Sammartino Vincenzo, Denis Nathanael, Roberto Di Pietro | ∗ University of Pisa, Pisa, Italy；King Abdullah University of Science and Technology (KAUST), Thuwal, Saudi Arabia；research avenue for physical-layer authentication | 提出量子-经典神经网络，用于SAR卫星物理层认证，增强安全性。 | [#1148](https://github.com/thinson/RS-PaperClaw/issues/1148) |
| [20260820] Far from the Crowd: Scalable Self-Supervised Learning via Geographic Isolation | Daniele Rege Cambrin, Rossi Francesco, Varile Mattia | AIKO | 利用地理隔离策略实现可扩展自监督学习，减少标注依赖。 | [#1149](https://github.com/thinson/RS-PaperClaw/issues/1149) |

## 🔎 观察

- 研究侧重数据访问基础设施优化，反映遥感数据量增长带来的传输挑战。
- 量子计算与自监督学习引入遥感，显示跨学科融合趋势增强。

---

Powered by OpenClaw🦞

---

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
