# Daily Reports

最近三天日报（最新在前）：

# [20260821](./202608/20260821.md)
## 📌 今日概况

今日共检索候选论文 12 篇；关键词+LLM 智能匹配遥感交叉论文 5 篇；最终纳入日报 5 篇。

今日遥感AI研究聚焦于农业、大气、城市感知、多模态检测及红外小目标检测等方向。农业杂草检测关注跨田域分布偏移下的迁移能力；大气遥感利用ADS-B干涉测量折射率时空变化；城市理解通过时空对齐提升语义感知；多模态检测引入专家引导的特征重校准；红外小目标检测提出相对退化感知网络。整体呈现从单一模态向多模态融合、从静态分析向动态感知发展的趋势。

## ✨ 今日亮点

- 农业杂草检测跨田域泛化能力受关注，无监督域适应成关键。
- ADS-B干涉测量新方法用于大气折射率时空变化遥感。
- 多模态检测引入专家引导特征重校准，提升融合精度。

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260821] On the Transferability of Agricultural Weed Detection Under Cross-Field Distribution Shift | Prabhakar Nikhilesh, Tenali Pranuthi, Wilfredo Abudeye Fernandez, Borah Shekhar, Karanam Athresh, Blasch Erik, Sundaravadivel Prabha, Natarajan Sriraam | University of Texas at Dallas；University of Texas at Tyler；Air Force Research Lab | 研究农业杂草检测在跨田域分布偏移下的迁移能力，采用无监督域适应方法。 | [#1151](https://github.com/thinson/RS-PaperClaw/issues/1151) |
| [20260821] Remote sensing of the temporal and spatial variability of atmospheric refractivity using ADS-B interferometry (ADSBi) | Lewis Ollie, Brunt Chris, Kitchen Malcolm, Neill E. Bowler, Edmund K. Stone | Department of Physics and Astronomy, University of Exeter, Exeter, United Kingdom；Institute (KNMI) (de Haan and Stoffelen 2012; de Haan et al | 利用ADS-B干涉测量遥感大气折射率，揭示其时空变异性及湿度关联。 | [#1152](https://github.com/thinson/RS-PaperClaw/issues/1152) |
| [20260821] CoST: Semantic-Aware Urban Understanding via Spatial-Temporal Alignment | Jiang Yutian, Liu Jiabo, Hao Xixuan, Liang Yuxuan | The Hong Kong University of Science and Technology (Guangzhou) Guangzhou China | 提出CoST模型，通过时空对齐实现卫星影像的语义感知城市理解。 | [#1153](https://github.com/thinson/RS-PaperClaw/issues/1153) |
| [20260821] SuppreSensing: Expert-Guided Feature Recalibration and Discrepancy Augmentation for Multimodal Object Detection | Wu Xin, Gao Zhenyu, Zhang Qiankun, Guo Shaoyong | Beijing University of Posts and Telecommunications Beijing China | SuppreSensing方法结合专家引导特征重校准与差异增强，提升多模态检测性能。 | [#1154](https://github.com/thinson/RS-PaperClaw/issues/1154) |
| [20260821] RDANet: Relative Degradation Aware Network for Infrared Small Target Detection | Liu Rui, Nie Jing, Fu Ying | School of Computer Science and Technology, Beijing Institute of Technology, Beijing, China (；School of Information and Electronics, Beijing Institute of Technology, Beijing, China ( | RDANet网络通过相对退化感知与多尺度下采样，增强红外小目标检测能力。 | [#1155](https://github.com/thinson/RS-PaperClaw/issues/1155) |

## 🔎 观察

- 跨域泛化问题在农业遥感中凸显，域适应技术成为提升模型实用性的关键。
- 多模态融合与专家知识结合，正成为提升遥感目标检测鲁棒性的新方向。

---

Powered by OpenClaw🦞

---

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
