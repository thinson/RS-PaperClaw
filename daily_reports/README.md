# Daily Reports

最近三天日报（最新在前）：

# [20260623](./202606/20260623.md)
## 📌 今日概况

今日共检索候选论文 8 篇；关键词+LLM 智能匹配遥感交叉论文 6 篇；最终纳入日报 3 篇。

今日研究聚焦于遥感数据的高分辨率应用与多源融合。Sentinel-1时间序列被用于矿区高分辨率土壤水分反演；多源生成模型MotifGen解决了卫星图像时空插值问题，应用于热带气旋监测；此外，一种渐进式像素邻域可变形交叉注意力机制被提出，用于提升多光谱目标检测中的可见光-热红外对齐与融合性能。

## ✨ 今日亮点

- Sentinel-1时间序列实现高分辨率矿区土壤水分反演
- 生成模型MotifGen解决卫星图像时空插值难题
- 可变形交叉注意力提升多光谱目标检测对齐精度

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260623] High Resolution Sediment-Specific Surface Soil Moisture Retrieval Using Sentinel-1 Time Series and Auxiliary Data | Hamedianfar Alireza, Antropov Oleg, Molinier Matthieu, Salmela Ulla, Kukkula Hanna, Seitsonen Lauri, Liwata-Kenttälä Pauliina, Middleton Maarit | b VTT Technical Research Centre of Finland, Espoo, 02150, Finland | 利用Sentinel-1时间序列与辅助数据实现高分辨率矿区土壤水分反演 | [#764](https://github.com/thinson/RS-PaperClaw/issues/764) |
| [20260623] MotifGen: Spatiotemporal interpolation of misaligned satellite images via multi-source generative modeling, in an application to tropical cyclones | Dauvilliers Clément, Monteleoni Claire | University of Colorado Boulder, Boulder, CO, USA | MotifGen通过多源生成模型对未对齐卫星图像进行时空插值 | [#765](https://github.com/thinson/RS-PaperClaw/issues/765) |
| [20260623] Progressive Pixel-Neighborhood Deformable Cross-Attention for Multispectral Object Detection | Qiu Tian, Shen Jifeng, Zuo Xin | a School of Electrical and Information Engineering, Jiangsu University, Zhenjiang, 212013, China；b School of Computer Science and Engineering, Jiangsu University of Science and Technology, Zhenjiang | 渐进式像素邻域可变形交叉注意力用于多光谱目标检测 | [#766](https://github.com/thinson/RS-PaperClaw/issues/766) |

## ⚠️ 未纳入日报的匹配论文

以下论文通过关键词/LLM 筛选，但在处理过程中失败未纳入日报。点击 arXiv 链接可查看原文。

| 标题 | arXiv | 失败原因 |
|------|-------|----------|
| Counting Trees from Satellite Imagery with Noisy Supervision | [2606.24786v1](https://arxiv.org/abs/2606.24786v1) | 质检未通过: 单位为空或无效 |
| Sat2City v2: Native 3D City Asset Generation from a Single Satellite Image | [2606.24138v1](https://arxiv.org/abs/2606.24138v1) | 质检未通过: 单位为空或无效 |
| Flood Mapping from RGB imagery using a Vision Foundation Model | [2606.24120v1](https://arxiv.org/abs/2606.24120v1) | 质检未通过: 单位为空或无效 |


## 🔎 观察

- SAR与光学数据融合仍是高分辨率地表参数反演的主流方向
- 生成模型在遥感时空插值中的应用正从理论走向实际任务

---

Powered by OpenClaw🦞

---

# [20260622](./202606/20260622.md)
## 📌 今日概况

今日共检索候选论文 9 篇；关键词+LLM 智能匹配遥感交叉论文 4 篇；最终纳入日报 2 篇。

今日遥感AI研究聚焦于提升模型对多模态、多分辨率数据的泛化能力。UniverSat提出一种与分辨率和模态无关的Transformer架构，通过自监督学习实现通用地球观测表征。另一工作则关注遥感模型在不同卫星与传感器间的模态迁移与适配问题，提出DeluluNet方法。两项研究共同推动了遥感基础模型的跨场景适应性与实用性。

## ✨ 今日亮点

- 提出分辨率与模态无关的通用遥感Transformer
- 探索遥感模型在不同卫星传感器间的迁移适配
- 自监督学习与模态迁移成为今日研究焦点

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260622] UniverSat: Resolution- and Modality-Agnostic Transformers for Earth Observation | Perron Yohann, Astruc Guillaume, Gonthier Nicolas, Mallet Clement, Landrieu Loic | LIGM, Ecole Nationale des Ponts et Chaussées, IP Paris, Univ Gustave Eiffel, CNRS；LASTIG, Univ Gustave Eiffel, IGN, ENSG；IGN；CNES；EFEO | UniverSat提出分辨率与模态无关的Transformer，用于通用地球观测表征。 | [#761](https://github.com/thinson/RS-PaperClaw/issues/761) |
| [20260622] Changing Modalities: Adapting Remote Sensing Models to New Satellites and Sensors | Tim G. Zhou, Fuller Anthony, Pleiss Geoff, Shelhamer Evan | University of British Columbia；Vector Institute；Carleton University | Changing Modalities研究遥感模型在新卫星与传感器间的模态迁移与适配。 | [#762](https://github.com/thinson/RS-PaperClaw/issues/762) |

## ⚠️ 未纳入日报的匹配论文

以下论文通过关键词/LLM 筛选，但在处理过程中失败未纳入日报。点击 arXiv 链接可查看原文。

| 标题 | arXiv | 失败原因 |
|------|-------|----------|
| Hedgementation = Hedgerow Segmentation: A Remote Sensing Benchmark | [2606.23615v1](https://arxiv.org/abs/2606.23615v1) | 质检未通过: 单位为空或无效; Q3 未通过质检 |
| AI-Empowered UAV-Assisted Backscatter Localization and ISAC for Zero-Energy IoT: A Comprehensive Survey | [2606.23125v1](https://arxiv.org/abs/2606.23125v1) | 质检未通过: 单位为空或无效 |


## 🔎 观察

- 遥感基础模型正从单一传感器向跨模态、跨分辨率通用架构演进。
- 模态迁移与传感器适配成为提升遥感模型实用性的关键挑战。

---

Powered by OpenClaw🦞

---

# [20260621](./202606/20260621.md)
## 📌 今日概况

今日共检索候选论文 1 篇；关键词+LLM 智能匹配遥感交叉论文 1 篇；最终纳入日报 0 篇。

当日筛中论文均未通过处理或质检，未纳入日报。


## ⚠️ 未纳入日报的匹配论文

以下论文通过关键词/LLM 筛选，但在处理过程中失败未纳入日报。点击 arXiv 链接可查看原文。

| 标题 | arXiv | 失败原因 |
|------|-------|----------|
| Semantic-Aware Autonomous Exploration for UAVs in Unknown Indoor Environments | [2606.22670v1](https://arxiv.org/abs/2606.22670v1) | 质检未通过: 标题为空或无效; Q1 未通过质检 |

## 🔎 观察

- 当日无成功纳入论文，建议优先检查候选筛选结果与失败原因。
- 若连续出现空日报，应复核 arXiv 日期窗口、关键词配置与 LLM 筛选输出。

---

Powered by OpenClaw🦞

---
