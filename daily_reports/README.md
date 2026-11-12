# Daily Reports

最近三天日报（最新在前）：

# [20261108](./202611/20261108.md)
## 📌 今日概况

今日共检索候选论文 4 篇；关键词+LLM 智能匹配遥感交叉论文 2 篇；最终纳入日报 2 篇。

今日研究聚焦遥感数据的高效利用与模型可解释性。一方面，利用多光谱卫星数据直接进行地表太阳辐射临近预报，结合时序注意力机制提升预测精度；另一方面，探索稀疏自编码器分解地球观测基础模型嵌入特征，以增强可解释性。两项工作分别从应用与理论层面推动遥感AI发展，体现了对实时预测与模型透明度的共同关注。

## ✨ 今日亮点

- 多光谱卫星数据直接用于地表太阳辐射临近预报，结合时序注意力提升精度。
- 稀疏自编码器分解地球嵌入特征，增强基础模型可解释性。
- 研究覆盖应用预测与理论解释，体现遥感AI多维度发展。

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20261108] Direct Multispectral Satellite Nowcasting of Gridded Surface Solar Radiation | Xie Tianyu, Zeng Zhaoliang, Liang Zhehao, Gui Ke, Zhang Xutao, Wang Yaqiang, Guan Dabo, Che Huizheng | ¹ State Key Laboratory of Severe Weather Meteorological Science and Technology, Chinese Academy；² Xiong'an Institute of Meteorological Artificial Intelligence, Xiong'an, Hebei, China；Department of Earth System Sciences, Tsinghua University, Beijing 10084, China；The Bartlett School of Sustainable Construction, University College London, London WC1 E 7 HB | 利用Himawari-8多光谱卫星数据与时序注意力，直接临近预报网格化地表太阳辐射。 | [#1626](https://github.com/thinson/RS-PaperClaw/issues/1626) |
| [20261108] Decomposing Earth Embeddings with Sparse Autoencoders | Benson Vitus, Yang Fanny, Reichstein Markus | Max Planck Institute for Biogeochemistry, Jena, Germany | 采用稀疏自编码器分解地球观测基础模型嵌入，提升特征可解释性。 | [#1627](https://github.com/thinson/RS-PaperClaw/issues/1627) |

## 🔎 观察

- 临近预报与可解释性成为遥感AI热点，分别对应实时应用与模型信任需求。
- 多光谱数据与基础模型结合，显示遥感AI向数据驱动与解释并重演进。

---

Powered by OpenClaw🦞

<!-- rs-pipeline: {"date": "20261108", "source": "api", "checked_at": "2026-11-12T04:16:17+00:00", "source_complete": true, "candidate_count": 4, "paper_count": 2} -->

---

# [20261102](./202611/20261102.md)
## 📌 今日概况

今日共检索候选论文 14 篇；关键词+LLM 智能匹配遥感交叉论文 11 篇；最终纳入日报 11 篇。

今日研究聚焦多源遥感数据融合与视觉语言模型在遥感中的应用。高光谱分类与跟踪引入测试时训练和光谱提示，多源分类强调共享模式与频率感知融合。视觉语言模型向决策与文本定位拓展，域泛化与增量变化检测受到关注。超分辨与水下图像恢复侧重数据合成与保真度评估。

## ✨ 今日亮点

- 视觉测试时训练与光谱提示用于高光谱分类和跟踪
- 多源遥感分类强调共享模式与频率感知跨层融合
- 视觉语言模型拓展至地球观测决策与阿拉伯地理文本定位

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20261102] Spectral-spatial vision test-time training for hyperspectral image classification | Zhao Xiang | College of Mathematical Sciences, Harbin Engineering University | 提出光谱-空间视觉测试时训练方法，用于高光谱图像分类。 | [#1614](https://github.com/thinson/RS-PaperClaw/issues/1614) |
| [20261102] Latent Spectral Prompting for Multimodal Hyperspectral Object Tracking | Cai Wangshu, Zhou Jun, Wang Lei, Mohammad Aminul Islam, Han Xu, Paliwal Kuldip | Griffith University, Australia；East China Normal University, China；Bangladesh Agricultural University, Bangladesh | 引入潜在光谱提示，缓解RGB与高光谱域差异以提升多模态跟踪。 | [#1615](https://github.com/thinson/RS-PaperClaw/issues/1615) |
| [20261102] Performance evaluation of super-resolution techniques for characterization and phenotyping of commodity crops using multispectral imagery | Karukayil Abhiram, João F. C. Mota, Vásquez-Guevara Mateo, Arevalo-Ramirez Tito, Fernando Auat Cheein | School of Engineering and Physical Sciences, Heriot-Watt University, Edinburgh, UK；Department of Electrical Engineering, Department of Mechanical Engineering and Metallurgy, School of Engineering, Faculty of；School of Mathematical and Computer Sciences, Heriot-Watt University, Edinburgh, UK；Harper Adams University, England, UK | 评估超分辨技术对多光谱作物表征与表型分析性能的影响。 | [#1616](https://github.com/thinson/RS-PaperClaw/issues/1616) |
| [20261102] Bridging Low-Level Image Fusion and High-Level Semantic Understanding | Dong Guangyuan, Shen Lingdong, Zhang Xudong, Jing Haodong, Wang Haoyu, Li Zihao, Ying Zonghao, Song Ziyu, Liu Shenghao, Luo Jiachen, Zhang Hao | Peking University；Xi'an Jiaotong University；Nankai University；Institute of Automation, Chinese Academy of Sciences | 连接低层图像融合与高层语义理解，结合对比学习和视觉语言模型。 | [#1617](https://github.com/thinson/RS-PaperClaw/issues/1617) |
| [20261102] Shared-Pattern Collaborative Network for Multi-Source Remote Sensing Data Classification | Yang Chenfang, Gong Chuanzheng, Gao Feng, Dong Junyu, Du Qian | State Key Laboratory of Physical Oceanography, Ocean University of China, Qingdao, China. (；Department of Electrical and Computer Engineering, Mississippi State University, Starkville, MS USA | 提出共享模式协作网络，用于多源遥感数据分类与跨模态学习。 | [#1618](https://github.com/thinson/RS-PaperClaw/issues/1618) |
| [20261102] Cross-Layer Refinement and Frequency-aware Fusion Network for Multi-Source Remote Sensing Image Classification | Xiao Wenhan, Gong Chuanzheng, Gao Feng, Dong Junyu, Du Qian | State Key Laboratory of Physical Oceanography, Ocean University of China, Qingdao, China；Department of Electrical and Computer Engineering, Mississippi State University, Starkville, MS USA. and elevation information [4] | 设计跨层细化与频率感知融合网络，提升多源遥感图像分类。 | [#1619](https://github.com/thinson/RS-PaperClaw/issues/1619) |
| [20261102] KAUSTics-Net: Diffusion-Based Through-Water UAV Restoration with a Semi-Synthetic Dataset | Scilla Dario, Omar A. Lopez, Johansen Kasper, Brian O. Nieuwenhuis, Matthew F. McCabe | and Livability Initiative, King Abdullah University of Science and Technology；Red Sea Research Center, Biological and Environmental Science and；Engineering Division, King Abdullah University of Science and Technology | 基于扩散模型和半合成数据集，恢复浅水环境无人机水下图像。 | [#1620](https://github.com/thinson/RS-PaperClaw/issues/1620) |
| [20261102] HyperFlow: Class-Incremental Semantic Change Detection via Hyperbolic Flow | Béchaz Manon, Buecher Léo, Dalsasso Emanuele, Tomoiaga Ciprian, Jayet Patrick, Detyniecki Marcin, Chapel Laetitia, Drumetz Lucas, Courty Nicolas, Tuia Devis | University of the Witwatersrand；Université de Bretagne Sud, France；Institut Agro Rennes-Angers, France；Lab-STICC | 利用双曲流实现类增量语义变化检测，建模地物覆盖转变。 | [#1621](https://github.com/thinson/RS-PaperClaw/issues/1621) |
| [20261102] EO-Jev: Decision Model for Earth Observation | Mohamed Atef Abouelhadid, Diaa Addeen Abuhani, Muhammad Akhtar Munir, Fahad Shahbaz Khan, Khan Salman | Mohamed Bin Zayed University of Artificial Intelligence；Massachusetts Institute of Technology；Australian National University；Linköping University Sweden | 构建地球观测决策模型，结合视觉语言模型与低秩微调校准。 | [#1622](https://github.com/thinson/RS-PaperClaw/issues/1622) |
| [20261102] ArabGeoText: Tool-Augmented Vision-Language Models for Arabic Geospatial Text Spotting | Bazi Yakoub, Alsaleh Sarah, Mohamad M. Al Rahhal, Mohamed A. Mekhtiche, Zuair Mansour | the Computer Engineering Department, College of Computer and Information Sciences, King Saud University, Riyadh, Saudi Arabia (；the Applied Computer Science Department, College of Applied Computer Science, King Saud University, Riyadh, Saudi Arabia ( | 提出工具增强视觉语言模型与基准数据集，用于阿拉伯地理文本定位。 | [#1623](https://github.com/thinson/RS-PaperClaw/issues/1623) |
| [20261102] ASCoR: Asymmetric Semantic-Spatial Learning for Remote Sensing Domain Generalization | Wang Zitong, Lyu Shuchang, Li Meng, Wang Qiang, Cheng Guangliang, Shi Zhenwei | Beihang University；University of Science and Technology Beijing；University of Liverpool；Guangdong Electronic Information Engineering Research Institute, University of Electronic Science and Technology of China | 采用非对称语义-空间学习，提升遥感语义分割域泛化能力。 | [#1624](https://github.com/thinson/RS-PaperClaw/issues/1624) |

## 🔎 观察

- 高光谱与多源融合研究正从单一特征提取转向测试时适应和跨模态提示，强调域差异缓解。
- 视觉语言模型在遥感中从描述生成走向决策与文本定位，工具增强和校准成为新关注点。

---

Powered by OpenClaw🦞

<!-- rs-pipeline: {"date": "20261102", "source": "oai", "checked_at": "2026-11-03T12:40:22+00:00", "source_complete": true, "candidate_count": 14, "paper_count": 11} -->

---

# [20261101](./202611/20261101.md)
## 📌 今日概况

今日共检索候选论文 8 篇；关键词+LLM 智能匹配遥感交叉论文 3 篇；最终纳入日报 3 篇。

今日研究聚焦遥感基础模型与多模态推理。SpecUltra提出统一光谱图像基础模型，强调跨传感器迁移；EarthJev探索视觉语言模型在Sentinel-2土地覆盖问答中的校准非生成式回答；第三篇则转向嵌入空间预测地表变化，利用Transformer与基础模型表征。整体趋势显示，遥感AI正从单一任务模型向统一表征、跨模态对齐与可解释问答演进，同时注重模型校准与嵌入空间动态建模。

## ✨ 今日亮点

- SpecUltra统一异构光谱图像基础模型，支持跨传感器迁移。
- EarthJev实现Sentinel-2土地覆盖的自然语言校准问答。
- 嵌入空间预测地表变化，探索基础模型动态表征能力。

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20261101] SpecUltra: A Unified Foundation Model for Heterogeneous Spectral Images | Kong Weili, Liu Baisen, Bi Xiaojun, Pei Jiaming | School of Information and Communication Engineering, Harbin Engineering University, Harbin 150001, China；School of Electronic and Information Engineering, Heilongjiang Institute of Technology, Harbin 150050, China；School of Information Engineering, Minzu University of China, Beijing 100081, China；School of Computer Science, The University of Sydney, Sydney, NSW 2006, Australia | 提出SpecUltra统一基础模型，面向高光谱与多光谱异构图像，强调跨传感器迁移能力。 | [#1610](https://github.com/thinson/RS-PaperClaw/issues/1610) |
| [20261101] EarthJev: Calibrated, Non-Generative Answers to Natural-Language Questions about Sentinel-2 Land Cover | Benfenati Domenico, Antonio Maria Rinaldi, Tommasino Cristian | Department of Electrical Engineering and Information Technology (DIETI), University of Naples Federico II, Via Claudio, 21, Naples, 80125, Italy | EarthJev针对Sentinel-2土地覆盖，提供校准且非生成式的自然语言问答方法。 | [#1611](https://github.com/thinson/RS-PaperClaw/issues/1611) |
| [20261101] Forecasting Earth Surface Change in Embedding Space | Li Jingtao, Jaffer Sadiq, Madhavapeddy Anil, Sousa Pedro, Ortiz Anthony, Gao Kyle, Feng Zhengpeng, Zhong Yanfei, White Kevin, Keshav Srinivasan | Department of Computer Science, University of Cambridge；Microsoft AI for Good Research Lab；Aalto University；Wuhan University | 在嵌入空间预测地球表面变化，结合Transformer与基础模型表征进行动态建模。 | [#1612](https://github.com/thinson/RS-PaperClaw/issues/1612) |

## 🔎 观察

- 光谱基础模型趋向统一异构传感器，跨传感器迁移成为关键评估维度。
- 遥感问答强调校准与非生成式，反映对可靠性与可解释性的需求上升。

---

Powered by OpenClaw🦞

<!-- rs-pipeline: {"date": "20261101", "source": "oai", "checked_at": "2026-11-03T12:28:18+00:00", "source_complete": true, "candidate_count": 8, "paper_count": 3} -->

---
