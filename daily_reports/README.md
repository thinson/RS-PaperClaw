# Daily Reports

最近三天日报（最新在前）：

# [20260529](./202605/20260529.md)
## 📌 今日概况

今日共检索候选论文 8 篇；关键词+LLM 智能匹配遥感交叉论文 6 篇；最终纳入日报 4 篇。

今日遥感AI研究呈现三大趋势：量子-经典混合架构用于跨模态表征学习、异构多智能体强化学习驱动卫星自主集群、以及合成数据训练的高光谱-多光谱融合方法。此外，通用视觉计数模型拓展至遥感场景，推动少样本与跨域目标计数能力提升。

## ✨ 今日亮点

- 量子-经典混合架构用于遥感跨模态表征学习
- 异构多智能体差分Transformer实现卫星自主集群
- 合成数据训练实现高光谱-多光谱自适应融合

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260529] HQ-JEPA: Hybrid Quantum Joint-Embedding Predictive Architecture for Cross-Modal Remote Sensing Representation Learning | Md Aminur Hossain, Ayush V. Patel, Sanjay K. Singh, Banerjee Biplab | Space Applications Centre；Biplab Banerjee2 | 提出混合量子-经典联合嵌入预测架构，用于遥感跨模态表征学习。 | [#639](https://github.com/thinson/RS-PaperClaw/issues/639) |
| [20260529] HADT: A Heterogeneous Multi-Agent Differential Transformer for Autonomous Earth Observation Satellite Cluster | Mohamad A. Hady, Muhammad Anwar Masum, Hu Siyi, Pratama Mahardhika, Cao Jimmy, Kowalczyk Ryszard | School of Computer Science and Information Technology, Adelaide University；School of Electrical Engineering, Computing and Mathematical Sciences (EECMS)；Systems Research Institute, Polish Academy of Sciences, Warsaw, Poland | 设计异构多智能体差分Transformer，实现地球观测卫星集群自主决策。 | [#640](https://github.com/thinson/RS-PaperClaw/issues/640) |
| [20260529] SCALMU: Synthetically-trained Coupling of Adaptive Learned Multiplicative Updates for Hyperspectral-Multispectral Fusion | Xu Xinxin, Gousseau Yann, Kervazo Christophe, Ladjal Saïd | The authors are with LTCI, Télécom Paris, Institut Polytechnique | 基于合成数据训练自适应耦合乘法更新网络，实现高光谱-多光谱融合。 | [#641](https://github.com/thinson/RS-PaperClaw/issues/641) |
| [20260529] Count Anything | Lei Mengqi, Cheng Shuokun, Bao Wei, Du Shaoyi, Yong Jun-Hai, Li Siqi, Gao Yue | {BNRist, THUIBCS, BLBCI, School of Software}, Tsinghua University；School of Computer Science and Technology, China University of Geosciences, Wuhan；State Key Laboratory of Human-Machine Hybrid Augmented Intelligence；National Engineering Research Center for Visual Information and Applications；and Institute of Artificial Intelligence and Robotics, Xi’an Jiaotong University | 提出文本引导的通用计数模型，可跨域计数遥感图像中任意目标。 | [#642](https://github.com/thinson/RS-PaperClaw/issues/642) |

## ⚠️ 未纳入日报的匹配论文

以下论文通过关键词/LLM 筛选，但在处理过程中失败未纳入日报。点击 arXiv 链接可查看原文。

| 标题 | arXiv | 失败原因 |
|------|-------|----------|
| PolSAR Image Classification using a Hybrid Complex-Valued Network (HybridCVNet) | [2605.31137v1](https://arxiv.org/abs/2605.31137v1) | 质检未通过: 单位为空或无效 |
| Non-destructive Identification of Oyster Species is possible from Hyperspectral Images with Machine Learning | [2605.30811v1](https://arxiv.org/abs/2605.30811v1) | 质检未通过: 单位为空或无效 |


## 🔎 观察

- 量子计算与遥感表征学习的结合尚属前沿，但实际部署仍需克服硬件限制。
- 合成数据训练策略在遥感融合任务中展现出潜力，可缓解真实标注数据稀缺问题。

---

Powered by OpenClaw🦞

---

# [20260528](./202605/20260528.md)
## 📌 今日概况

今日共检索候选论文 7 篇；关键词+LLM 智能匹配遥感交叉论文 4 篇；最终纳入日报 4 篇。

今日遥感AI研究聚焦于基础框架构建与鲁棒性评估。多模态语义引导的遥感变化检测框架OmniCD被提出，旨在提升场景检索与变化检测能力。同时，针对密集城市非正规住区的建筑与道路识别发布了专用数据集与基准。此外，研究关注星上处理中的建筑损毁评估，以及面向真实世界分布偏移的鲁棒性基准EarthShift，体现了从模型设计到实际部署的全面探索。

## ✨ 今日亮点

- 多模态语义引导的变化检测基础框架OmniCD发布
- 城市非正规住区建筑与道路识别数据集及基准建立
- 面向星上处理的建筑损毁评估与鲁棒性基准EarthShift

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260528] OmniCD: A Foundational Framework for Remote Sensing Image Change Detection Guided by Multimodal Semantics | Sun Chenhao | Wuhan University | OmniCD提出多模态语义引导的遥感变化检测基础框架，提升场景检索能力。 | [#634](https://github.com/thinson/RS-PaperClaw/issues/634) |
| [20260528] Building and Road Recognition in Dense Urban Informal Settlements: A Dataset and Benchmark | Long Hongyu, Liu Jiaxuan, Cao Rui | HKUST(GZ) | 发布密集城市非正规住区建筑与道路识别数据集及基准，填补领域空白。 | [#635](https://github.com/thinson/RS-PaperClaw/issues/635) |
| [20260528] Optimizing Latent Representations for Robust Building Damage Assessment Onboard Earth Observation Satellites | Goudemant Thomas, Francesconi Benjamin | Institut de Recherche Technologique Saint Exupéry | 优化潜在表示实现星上建筑损毁评估，增强灾害响应实时性。 | [#636](https://github.com/thinson/RS-PaperClaw/issues/636) |
| [20260528] EarthShift: a benchmark for measuring robustness to real-world distribution shifts in Earth observation | Doerksen Kelsey, Kerner Hannah | School of Computing and Augmented Intelligence；Arizona State University | EarthShift基准衡量遥感模型对真实世界分布偏移的鲁棒性。 | [#637](https://github.com/thinson/RS-PaperClaw/issues/637) |

## 🔎 观察

- 多模态语义融合正成为遥感变化检测基础模型的关键技术路径。
- 星上智能处理与分布偏移鲁棒性研究，推动遥感AI向实际部署迈进。

---

Powered by OpenClaw🦞

---

# [20260527](./202605/20260527.md)
## 📌 今日概况

今日共检索候选论文 9 篇；关键词+LLM 智能匹配遥感交叉论文 3 篇；最终纳入日报 3 篇。

今日遥感AI研究聚焦于高效计算与多模态基础模型。一方面，探索在Apple Silicon上利用块浮点半精度FFT实现SAR成像，强调动态范围而非精度；另一方面，通过可训练张量分解将RGB模型迁移至高光谱图像，以及提出多模态地理空间基础模型FLORO，支持跨传感器与尺度的生态遥感。

## ✨ 今日亮点

- 块浮点半精度FFT在Apple Silicon上实现SAR成像
- 可训练张量分解迁移RGB模型至高光谱图像
- 多模态基础模型FLORO支持跨传感器生态遥感

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260527] Range, Not Precision: Block-Floating-Point Half-Precision FFT and SAR Imaging on Apple Silicon | Mohamed Amine Bergach | Illumina | 利用块浮点半精度FFT在Apple Silicon上实现高效SAR成像，侧重动态范围而非精度。 | [#630](https://github.com/thinson/RS-PaperClaw/issues/630) |
| [20260527] Transfer learning RGB models to hyperspectral images with trainable tensor decompositions | Schönfeld Mariette, Devos Laurens, Meert Wannes, Blockeel Hendrik | Leuven.AI - KU Leuven Institute for AI, B-3000 Leuven, Belgium | 通过可训练张量分解将RGB预训练模型迁移至高光谱图像，提升光谱-空间特征学习。 | [#631](https://github.com/thinson/RS-PaperClaw/issues/631) |
| [20260527] FLORO: A Multimodal Geospatial Foundation Model for Ecological Remote Sensing Across Sensors and Scales | Jorge L. Rodriguez, Victor Angulo Morales, Alwahas Areej, Mariana Elias Lara, Fida Mohammad Thoker, Johansen Kasper, Ghanem Bernard, Fernando T. Maestre, Matthew F. McCabe | King Abdullah University of Science and Technology | FLORO多模态地理空间基础模型结合掩码自编码，实现跨传感器与尺度的生态遥感。 | [#632](https://github.com/thinson/RS-PaperClaw/issues/632) |

## 🔎 观察

- 计算效率与模型泛化能力成为遥感AI研究的双重焦点。
- 多模态与跨传感器融合正推动基础模型在生态遥感中的实际应用。

---

Powered by OpenClaw🦞

---
