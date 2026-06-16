# Daily Reports

最近三天日报（最新在前）：

# [20260615](./202606/20260615.md)
## 📌 今日概况

今日共检索候选论文 14 篇；关键词+LLM 智能匹配遥感交叉论文 6 篇；最终纳入日报 5 篇。

今日遥感AI研究聚焦多模态融合与精细化解译。FusionRS提出首个大规模RGB-红外双模态视觉语言数据集；WaveDINO利用深度学习实现InSAR大气校正；层级细粒度目标检测与无人机去雾方法分别提升识别精度与图像质量；SAR洪水分割研究对比了CNN与Transformer的可解释性。

## ✨ 今日亮点

- 首个RGB-红外双模态遥感视觉语言数据集发布
- 深度学习InSAR大气校正方法获GNSS验证
- 无人机去雾引入几何感知深度展开网络

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260615] FusionRS: A Large-Scale RGB-Infrared Remote Sensing Dataset for Dual-Modal Vision-Language Foundation Models | Han Jiaju, Zhang Ben, Sun Xuemeng, Zhang Qike, Dong Yuxian, Hu Chengyin, Zhang Fengyu, Wei Yiwei, Guo Jiujiang | China University of Petroleum-Beijing at Karamay；University of Electronic Science and Technology of China；Tianjin University；most existing work remains centered on RGB | FusionRS发布大规模RGB-红外双模态遥感数据集，支撑视觉语言模型。 | [#726](https://github.com/thinson/RS-PaperClaw/issues/726) |
| [20260615] WaveDINO: Learning-Based Atmospheric Correction of Unwrapped InSAR Interferograms Validated by GNSS: Results at Laguna del Maule and Campi Flegrei Volcanoes | Popescu Robert, Biggs Juliet, Zhu Tianyuan, Anantrasirichai Nantheera | the University of Bristol, Bristol, U.K | WaveDINO用深度学习校正InSAR大气相位，经GNSS验证有效。 | [#727](https://github.com/thinson/RS-PaperClaw/issues/727) |
| [20260615] Hierarchical Fine-Grained Aerial Object Detection | Zhang Yan, Xu Fang, Yang Wen, Xia Gui-Song | the School of Computer Science, Wuhan University, Wuhan, , China；the School of Artificial Intelligence, Wuhan University, Wuhan, , China；the School of Electronic Information, Wuhan University, Wuhan, , China | 层级细粒度检测方法提升遥感目标属性与类别识别精度。 | [#728](https://github.com/thinson/RS-PaperClaw/issues/728) |
| [20260615] Towards UAV Image Dehazing: A UAV Atmospheric Scattering Model, Benchmark, and Geometry-Aware Deep Unfolding Network | Fang Wenxuan, Weng Jiangwei, Zheng Yu, Fan Junkai, Wang Guangfa, Chen Xiang, Yang Jian, Li Jun | School of Computer Science and Engineering, Nanjing University of Science and Technology | 提出无人机大气散射模型与几何感知深度展开去雾网络。 | [#729](https://github.com/thinson/RS-PaperClaw/issues/729) |
| [20260615] Explainable Flood Segmentation on Sentinel-1 SAR Imagery: A Comparative Study of CNN and Transformer Architectures | Banerjee Arundhuti, Daou David | United Nations University’s Institute for Environment and Human Security (UNU-EHS) | 对比CNN与Transformer在SAR洪水分割中的可解释性与性能。 | [#730](https://github.com/thinson/RS-PaperClaw/issues/730) |

## ⚠️ 未纳入日报的匹配论文

以下论文通过关键词/LLM 筛选，但在处理过程中失败未纳入日报。点击 arXiv 链接可查看原文。

| 标题 | arXiv | 失败原因 |
|------|-------|----------|
| Training-Free Open-Vocabulary Visual Grounding for Remote Sensing Images and Videos | [2606.16124v1](https://arxiv.org/abs/2606.16124v1) | 质检未通过: 单位为空或无效 |


## 🔎 观察

- 双模态视觉语言模型成为遥感基础模型新热点，数据与任务协同推进。
- 深度学习在InSAR与SAR应用中从分割向物理校正与可解释性延伸。

---

Powered by OpenClaw🦞

---

# [20260614](./202606/20260614.md)
## 📌 今日概况

今日共检索候选论文 0 篇；关键词+LLM 智能匹配遥感交叉论文 0 篇；最终纳入日报 0 篇。

当日未检索到符合条件并纳入日报的论文。

## 🔎 观察

- 当日无成功纳入论文，建议优先检查候选筛选结果与失败原因。
- 若连续出现空日报，应复核 arXiv 日期窗口、关键词配置与 LLM 筛选输出。

---

Powered by OpenClaw🦞

---

# [20260613](./202606/20260613.md)
## 📌 今日概况

今日共检索候选论文 3 篇；关键词+LLM 智能匹配遥感交叉论文 2 篇；最终纳入日报 1 篇。

今日研究聚焦于低轨卫星网络中的智能资源编排问题，提出了一种结合检索增强生成（RAG）的双层认知编排框架。该工作通过引入认知计算与RAG技术，旨在缓解卫星边缘计算中的资源碎片化问题，提升网络编排效率与智能化水平，反映了遥感与卫星通信领域对AI驱动自主决策能力的持续探索。

## ✨ 今日亮点

- 提出RAG增强的双层认知编排框架，应对资源碎片化
- 聚焦低轨卫星网络中的智能资源管理问题
- 融合认知计算与检索增强生成技术提升编排效率

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260613] A RAG-Enhanced Bi-Level Cognitive Orchestration Framework for LEO Satellite Networks | Jiang Yuhong, Shen Zhishu, Yin Tong, Zheng Qiushi, Jin Yichao, Mehmeti Fidan, Jin Jiong | Yuhong Jiang, Zhishu Shen, and Tong Yin are with the School；of Computer Science and Artificial Intelligence, Wuhan University of；of Transportation Internet of Things, Wuhan University of Technology；Qiushi Zheng, and Jiong Jin are with the School of Engineering, Swin-；burne University of Technology, Melbourne, Australia (；Yichao Jin is with School of Automation (School of Artificial Intelligence)；Hangzhou Dianzi University, Hangzhou, China (；University of Munich, Munich, Germany ( | 提出RAG增强的双层认知编排框架，用于低轨卫星网络资源管理。 | [#723](https://github.com/thinson/RS-PaperClaw/issues/723) |

## ⚠️ 未纳入日报的匹配论文

以下论文通过关键词/LLM 筛选，但在处理过程中失败未纳入日报。点击 arXiv 链接可查看原文。

| 标题 | arXiv | 失败原因 |
|------|-------|----------|
| Risk-Aware LLM Agents for Geospatial Data Retrieval: Design and Preliminary Adversarial Evaluation | [2606.15077v1](https://arxiv.org/abs/2606.15077v1) | 质检未通过: 单位为空或无效 |


## 🔎 观察

- RAG技术正从文本处理向卫星网络编排等垂直领域迁移
- 认知计算与卫星边缘计算的结合成为智能遥感新方向

---

Powered by OpenClaw🦞

---
