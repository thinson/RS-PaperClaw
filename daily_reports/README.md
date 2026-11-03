# Daily Reports

最近三天日报（最新在前）：

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

# [20261031](./202610/20261031.md)
## 📌 今日概况

今日共检索候选论文 10 篇；关键词+LLM 智能匹配遥感交叉论文 8 篇；最终纳入日报 8 篇。

今日研究呈现多源遥感与AI深度融合趋势：高光谱与无人机平台支撑精细地物制图，微波遥感结合机器学习实现极地全天候参数反演；跨视角视觉定位与地球嵌入聚类拓展了空间推理与土地单元划分；边缘-云-太空协同推理关注能耗优化，城市功能知识迁移应对数据不均。整体上，数据驱动方法更注重不确定性、跨域泛化和硬件协同。

## ✨ 今日亮点

- 高光谱与无人机数据推动海岸带和地物精细制图
- 微波机器学习实现北极融池全天候反演
- 跨视角视觉定位与地球嵌入聚类拓展空间推理

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20261031] Spatial Uncertainty Analytics for Budget-Limited Inspection of Hyperspectral Scenes | Sharma Ritesh, Motai Yuichi | RITESH SHARMA, Virginia Commonwealth University, USA；YUICHI MOTAI, Virginia Commonwealth University, USA；Authors’ Contact Information: Ritesh Sharma, Virginia Commonwealth University, Richmond, Virginia, USA | 面向预算受限高光谱场景，提出空间不确定性分析以优化主动采样策略。 | [#1601](https://github.com/thinson/RS-PaperClaw/issues/1601) |
| [20261031] Vision-based Sensing of Urban Environment using Hardware-Software co-design at Scale | Gupta Akshit, R Venkatesha Prasad | TU Delft | 基于软硬件协同设计，实现城市环境多光谱视觉感知的大规模部署。 | [#1602](https://github.com/thinson/RS-PaperClaw/issues/1602) |
| [20261031] The MASSIMAL Dataset: UAV Hyperspectral Images and Ground Truth Observations for Coastal Habitat Mapping in Norway | Martin Hansen Skjelvareid, Rinde Eli, Hancke Kasper, Blix Katalin, Galice Guillaume Hoarau, Grometto Nicolo, Maia Røst Kile | ¹ UiT The Arctic University of Norway, Hansine Hansens veg 18；² Norwegian Institute for Water Research (NIVA), Sognsveien 72；³ Nord University, Universitetsalléen 11 | 发布挪威海岸无人机高光谱与地面真值数据集，服务海藻与海草制图。 | [#1603](https://github.com/thinson/RS-PaperClaw/issues/1603) |
| [20261031] An all-weather microwave-based AI retrieval of pan-Arctic melt pond fraction | Aparício Sara, Driscoll Simon, Mark R. Drinkwater, Flocco Daniela | CENSE - Center for Environmental and Sustainability Research & CHANGE - Global Change and；Sustainability Institute, NOVA School of Science and Technology, Universidade Nova de Lisboa, Campus de；Department of Applied Mathematics and Theoretical Physics, University of Cambridge, United Kingdom；Dipartimento di Scienze della Terra, dell’Ambiente e delle Risorse, Università degli Studi di Napoli “Federico；CoNISMA - Consorzio Nazionale Interuniversitario per le Scienze del Mare, Roma, Italy | 利用XGBoost与微波遥感实现泛北极融池分数全天候AI反演。 | [#1604](https://github.com/thinson/RS-PaperClaw/issues/1604) |
| [20261031] Adaptive Land Units from Earth Embeddings | Alonso Albert, Jamal Jokar Arsanjani, Andres R. Masegosa | Department of Computer Science, Aalborg University, Copenhagen, Denmark；Department of Sustainability and Planning, Aalborg University, Copenhagen, Denmark | 基于地球嵌入与贝叶斯层次聚类，无监督生成自适应土地单元。 | [#1605](https://github.com/thinson/RS-PaperClaw/issues/1605) |
| [20261031] Grounding Across Views: Cross-View Referring Reasoning for Visual Grounding | Gan Hao, Wang Liuqian, Li Shuang, Gao Yufei, Chao Wentao, Fu Chong, Liu Chengming, Shi Lei | Zhengzhou University, Henan, China | 提出跨视角指代推理框架，实现视觉 grounding 与目标地理定位。 | [#1606](https://github.com/thinson/RS-PaperClaw/issues/1606) |
| [20261031] STLT: A Novel System for Energy-Aware Distributed Inference in the Edge-Cloud-Space Continuum | Stanisic Andrija, Gravara Milos, Juan Luis Herrera, Nastic Stefan | University of Extremadura Spain | 设计STLT系统，在边缘-云-太空连续体中实现能耗感知分布式推理。 | [#1607](https://github.com/thinson/RS-PaperClaw/issues/1607) |
| [20261031] Urban functional knowledge transfer through global representations amid uneven data | Liu Junyuan, Wang Xinglei, Dong Guangsheng, Sha Hao, Zeng Zichao, Deng Zhicheng, Feng Jiazhuang, Wang Xiang, Cheng Tao | SpaceTimeLab, Department of Civil, Environmental and Geomatic Engineering, University；College London, London, WC1 E 6 BT, United Kingdom；State Key Laboratory of Information Engineering in Surveying, Mapping and Remote；Sensing, Wuhan University, Wuhan, 430079, China | 通过全局表示与POI对齐嵌入，实现数据不均下的城市功能知识迁移。 | [#1608](https://github.com/thinson/RS-PaperClaw/issues/1608) |

## 🔎 观察

- 高光谱与无人机数据集的开放共享正加速海岸带精细制图的可复现研究。
- 边缘-太空协同推理与不确定性采样表明，遥感AI正从精度优先转向资源约束下的系统优化。

---

Powered by OpenClaw🦞

<!-- rs-pipeline: {"date": "20261031", "source": "oai", "checked_at": "2026-11-03T12:20:24+00:00", "source_complete": true, "candidate_count": 10, "paper_count": 8} -->

---

# [20261030](./202610/20261030.md)
## 📌 今日概况

今日共检索候选论文 5 篇；关键词+LLM 智能匹配遥感交叉论文 2 篇；最终纳入日报 2 篇。

今日研究趋势聚焦于遥感数据的高效利用与领域自适应。一方面，有工作探索直接从卫星影像端到端学习屋顶太阳能潜力，绕过显式几何建模，简化流程并降低对辅助数据的依赖；另一方面，针对SAR时间序列作物分类，提出物理引导的自监督预训练方法，结合极化特征与BERT架构，提升标签稀缺场景下的分类性能。两项研究均体现了减少人工特征工程、增强模型自主表征能力的倾向。

## ✨ 今日亮点

- 端到端学习屋顶太阳能潜力，无需显式几何建模。
- 物理引导自监督预训练，融合极化特征与BERT。
- 两项研究均致力于降低对人工特征和标签的依赖。

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20261030] An Empirical Study on Learning Rooftop Solar Potential from Satellite Imagery Directly Without Explicit Geometry | Lee Joshua | Skyline High School | 实证研究直接从卫星影像端到端学习屋顶太阳能潜力，避免显式几何建模。 | [#1598](https://github.com/thinson/RS-PaperClaw/issues/1598) |
| [20261030] SAR-TS-BERT: Physics-Guided Self-Supervised Pre-Training With Polarimetric Features for SAR Time-Series Crop Classification | Wang Jieqiu, Zhang Yuhan, Zheng Bo, Zhang Shaoming | College of Surveying and Geo-Informatics, Tongji University, Shanghai, China ( | 提出物理引导自监督预训练SAR-TS-BERT，结合极化特征提升作物分类。 | [#1599](https://github.com/thinson/RS-PaperClaw/issues/1599) |

## 🔎 观察

- 端到端学习减少中间几何建模误差，但可解释性与泛化性仍需验证。
- 自监督预训练结合物理特征，有望缓解SAR作物分类标签稀缺问题。

---

Powered by OpenClaw🦞

<!-- rs-pipeline: {"date": "20261030", "source": "oai", "checked_at": "2026-11-02T12:51:57+00:00", "source_complete": true, "candidate_count": 5, "paper_count": 2} -->

---
