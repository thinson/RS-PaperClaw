# Daily Reports

最近三天日报（最新在前）：

# [20260916](./202609/20260916.md)
## 📌 今日概况

今日共检索候选论文 21 篇；关键词+LLM 智能匹配遥感交叉论文 7 篇；最终纳入日报 6 篇。

今日研究覆盖高光谱分类、叶绿素反演、ISAC-SAR、星上烟火检测、无人机广域感知与跨视角地理定位。趋势上，可解释AI与降维结合用于高光谱分类，符号回归探索叶绿素反演所需波段，轻量化弱监督模型推动星上实时推理，多视角专家与视觉语言重排提升跨视角定位鲁棒性。整体呈现模型轻量化、任务专用化与多模态融合并进的特点。

## ✨ 今日亮点

- 可解释AI驱动高光谱降维，兼顾分类精度与特征可解释性
- 符号回归量化叶绿素反演所需高光谱信息，挑战全波段依赖
- 轻量弱监督模型实现星上烟火检测，推动在轨实时响应

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260916] Dimensionality reduction for AI based hyperspectral image classification based on XAI | Zeljković Vladimir, Stojanović Branka, Ganster Harald, Nešković Aleksandar | University of Belgrade School of Electrical Engineering；JOANNEUM RESEARCH Forschungsgesellschaft mbH；This study, as part of a large research initiative [9], uti-；This research addresses the challenge of limited mate- lizes AI for different materials classification based on hyrial recycling in wood recycling processes by leveraging | 基于可解释AI的高光谱降维方法，用于木材回收材料分类，缓解标注数据有限问题。 | [#1300](https://github.com/thinson/RS-PaperClaw/issues/1300) |
| [20260916] How Much Hyperspectral Information Does Chlorophyll Retrieval Really Need? | Hammoud Abed, Sun Xuerong, Champenois Bianca, Robert J.W. Brewin | Civil and Environmental Engineering, Princeton University, Princeton, New Jersey 08540, USA；Centre for Geography and Environmental Science, Department of Earth and Environmental Sciences；Faculty of Environment, Science and Economy, University of Exeter, Exeter, Cornwall, UK；High Meadows Environmental Institute, Princeton University, Princeton, New Jersey 08540, USA | 利用符号回归探究叶绿素反演真正需要多少高光谱信息，面向PACE等任务。 | [#1301](https://github.com/thinson/RS-PaperClaw/issues/1301) |
| [20260916] Imaging-Communication Trade-off in VLEO ISAC-SAR Using CP-OFDM | Lee In-Hyeok, Han Kawon | Ulsan National Institute of Science and Technology, Ulsan, Korea | 研究VLEO下ISAC-SAR采用CP-OFDM的成像与通信权衡关系。 | [#1302](https://github.com/thinson/RS-PaperClaw/issues/1302) |
| [20260916] WISE: A Lightweight, Weakly-Supervised Model for Onboard Fire Smoke Detection and Localization | Lu Sha, Sun Yu, Zhao Liang, Liu Jixue, Liu Lin, Li Jiuyong, A. K. Qin, Mousist Alejandro, Peters Stefan | Adelaide University, Adelaide, SA 5000, Australia；Swinburne University of Technology, Hawthorn, VIC 3122, Australia | 提出轻量弱监督WISE模型，实现星上火灾烟雾检测与定位。 | [#1303](https://github.com/thinson/RS-PaperClaw/issues/1303) |
| [20260916] Understanding Dynamic Scenes at Gigapixel Scale: Wide-Area Spatio-Temporal Perception from UAVs | Zhu Yuhang, Zhu Meiyi, Dang Yunkai, Li Zhangnan, Wang Yuxuan, Li Wenbin, Pan Hongbing | Nanjing University | 面向无人机十亿像素级广域动态场景，构建时空感知数据集与方法。 | [#1304](https://github.com/thinson/RS-PaperClaw/issues/1304) |
| [20260916] Multi-View Mixture-of-Experts with Vision-Language Reranking for Cross-View Object Geo-Localization | Fan Xuyu, Ming Qi, Han Zhu, Wang Liuqian, Cao Si-Yuan, Zhang Xiaohan, Zhao Xudong, Zhao Mingjing, Zhang Yuhan | College of Computer Science, Beijing University of Technology；Zhengzhou University；Zhejiang University；Beijing Institute of Technology；Beijing Electronic Science and Technology Institute；Intelligent Science & Technology Academy of CASIC；jing University of Technology | 多视角专家混合结合视觉语言重排，提升跨视角目标地理定位性能。 | [#1305](https://github.com/thinson/RS-PaperClaw/issues/1305) |

## ⚠️ 未纳入日报的匹配论文

以下论文通过关键词/LLM 筛选，但在处理过程中失败未纳入日报。点击 arXiv 链接可查看原文。

| 标题 | arXiv | 失败原因 |
|------|-------|----------|
| PDA++: Field-Aligned Planning and Scene-Adaptive Insertion in Remote Sensing | [2609.18329v2](https://arxiv.org/abs/2609.18329v2) | 质检未通过: 单位为空或无效 |


## 🔎 观察

- 高光谱与叶绿素研究共同指向信息冗余问题，降维与波段选择成为提升效率的关键路径。
- 星上推理与无人机广域感知强调轻量化与弱监督，反映遥感AI向边缘部署加速迁移。

---

Powered by OpenClaw🦞

---

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

# [20260914](./202609/20260914.md)
## 📌 今日概况

今日共检索候选论文 11 篇；关键词+LLM 智能匹配遥感交叉论文 9 篇；最终纳入日报 9 篇。

今日论文覆盖遥感与AI交叉的多个应用方向：从海冰类型预测、野火分割与葡萄园火灾韧性分析，到屋顶光伏统计审计、海洋污染检测和雪崩活动预测。方法上，弱监督多标签比例学习、贝叶斯推断、Mamba分割框架和Transformer时序建模等被用于处理标签不完整、数据分布差异和复杂时空依赖。同时，视觉语言模型与不确定性估计开始进入无人机导航，迁移学习也被用于社会经济估计。整体呈现任务驱动、多源融合与模型适配并重的趋势。

## ✨ 今日亮点

- 弱监督与贝叶斯方法被用于海冰和光伏统计中的不完整标签问题
- Mamba与Transformer分别进入海洋污染分割和雪崩活动预测任务
- 视觉语言模型结合不确定性估计用于越野导航路径规划

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260914] UDAV: Uncertainty-Driven Adaptive VLM Waypoint Planner | Farhani Ghazal, Shabani Shabnam | the Automotive and Surface Transportation Research Centre, National Research Council Canada, London, Ontario, Canada | 提出不确定性驱动的自适应视觉语言模型航点规划器，用于无人机引导地面车辆越野导航。 | [#1290](https://github.com/thinson/RS-PaperClaw/issues/1290) |
| [20260914] Multi-Label Proportion Learning for Sea-Ice Type Prediction | Samira Alkaee Taleghan, Koo Younghyun, Andrew P. Barrett, Banaei-Kashani Farnoush | University of Colorado Denver National Snow and Ice Data Center (NSIDC), CIRES；Denver, Colorado, USA University of Colorado Boulder；National Snow and Ice Data Center (NSIDC), CIRES, University of Colorado Denver；University of Colorado Boulder Denver, Colorado, USA；atures and ERA5 reanalysis data through modality-guided auxiliary Danish Meteorological Institute (DMI) overlaid on a Sentinel-1 SAR | 面向海冰类型预测，研究多标签比例学习以应对弱监督和标签比例信息。 | [#1291](https://github.com/thinson/RS-PaperClaw/issues/1291) |
| [20260914] Nationally Consistent, Locally Incomplete: A Bayesian Remote-Sensing Audit of Rooftop Photovoltaic Registries | Kasmi Gabriel, Saint-Drenan Yves-Marie, Dubus Laurent, Blanc Philippe | Centre Observation Impacts Energie (O.I.E.), MINES Paris, Université PSL, Sophia-Antipolis, France | 用贝叶斯遥感审计方法评估法国屋顶光伏注册数据，揭示全国一致但局部缺失问题。 | [#1292](https://github.com/thinson/RS-PaperClaw/issues/1292) |
| [20260914] A Sentinel-2 benchmark dataset for deep-learning active-fire segmentation across 25 California wildfires | Mitra Shreyan, Narimani Mohammadreza, Farajpoor Parastoo | California High School；Department of Biological and Agricultural Engineering, University of California, Davis | 发布基于Sentinel-2的加州25场野火主动火线分割基准数据集，服务深度学习评测。 | [#1293](https://github.com/thinson/RS-PaperClaw/issues/1293) |
| [20260914] Multisource Remote Sensing and Geospatial Analysis of Vineyard Wildfire Impacts and Resilience: The 2019 Kincade Fire | Farajpoor Parastoo, Mahla Ardebili Pour, Mohammad Bagher Ghiasi, Narimani Mohammadreza | Department of Biological and Agricultural Engineering, University of California, Davis；Department of Civil and Environmental Engineering, University of California, Davis；Department of Electrical and Computer Engineering, University of California, Davis | 结合多源遥感和地理空间分析，评估2019年Kincade火灾对葡萄园的影响与恢复力。 | [#1294](https://github.com/thinson/RS-PaperClaw/issues/1294) |
| [20260914] Transfer Learning for Socioeconomic Estimation in Forced-Displacement Settings | Ndung'u Steven, Daoud Adel, Ismael Yacoubou Djima, Hai-Anh H. Dang, Patrick Michael Brock | Chalmers University, Sweden | 在被迫流离失所场景中探索迁移学习，利用地球观测估计社会经济状况。 | [#1295](https://github.com/thinson/RS-PaperClaw/issues/1295) |
| [20260914] MambaMPD: A Mamba-Driven Segmentation Framework for Marine Pollution Detection from Remote Sensing Imagery | Chen Shuaiyu, Han Wei, Ren Peng, Luo Chunbo, Fu Zeyu | aDepartment of Computer Science, University of Exeter, Exeter, United Kingdom；bSchool of Computer Science, China University of Geosciences, Wuhan, China；cCollege of Oceanography and Space Informatics, China University of Petroleum (East China), Qingdao, China | 提出Mamba驱动的海洋污染检测分割框架，结合频率感知增强处理遥感影像。 | [#1296](https://github.com/thinson/RS-PaperClaw/issues/1296) |
| [20260914] Data-driven Prediction of Satellite-observed Avalanche Activity from Snowpack Simulations | Grahn Jakob, Filippo Maria Bianchi, Kruyt Bert, Müller Karsten | NORCE Research, Troms, Norway；UiT The Arctic University of Norway, Troms, Norway | 利用雪包模拟数据驱动预测卫星观测的雪崩活动，采用Transformer建模时序关系。 | [#1297](https://github.com/thinson/RS-PaperClaw/issues/1297) |
| [20260914] EECTracker: Swarm Motion Prior-Guided Feature Compensation for Airborne Optical UAV Swarm Tracking | Chu Zhaochen, Song Tao, Jin Ren, Jia Mingdong, Lin Defu | China-UAE Belt and Road Joint Laboratory on Intelligent Unmanned Systems, then be guided toward these regions to supplement weakened；School of Aerospace Engineering, Beijing Institute of Technology, Beijing | 提出EECTracker，利用群体运动先验引导特征补偿，用于机载光学无人机集群跟踪。 | [#1298](https://github.com/thinson/RS-PaperClaw/issues/1298) |

## 🔎 观察

- 弱监督、标签不完整和域偏移是今日多篇论文的共同挑战，方法上倾向贝叶斯推断与迁移学习。
- 应用场景明显向灾害与能源倾斜，野火、雪崩、海冰和光伏统计占据多数，强调可操作监测。

---

Powered by OpenClaw🦞

---
