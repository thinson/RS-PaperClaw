# Daily Reports

最近三天日报（最新在前）：

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

# [20260526](./202605/20260526.md)
## 📌 今日概况

今日共检索候选论文 6 篇；关键词+LLM 智能匹配遥感交叉论文 3 篇；最终纳入日报 3 篇。

今日遥感AI研究呈现多元化趋势：无人机载SAR成像优化、图像分割评估方法反思，以及面向全球泛化的道路交互式提取成为三大焦点。学术界持续关注模型泛化能力与评估指标可靠性等基础问题。

## ✨ 今日亮点

- UAV-MIMO TomoSAR通过粒子群优化实现点扩散函数优化，提升三维成像质量
- 图像阈值分割研究揭示SSIM、PSNR等常用指标对特定评价函数存在系统性偏差
- RoadGIE构建全球尺度航空道路数据集，推动交互式分割的跨域泛化研究

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260526] Point Spread Function Optimization for Communication-assisted UAV-borne MIMO TomoSAR | Fakharizadeh Pouya, Lahmeri Mohamed-Amine, Krieger Gerhard, Schober Robert | Friedrich-Alexander-Universität Erlangen-Nürnberg (FAU)；German Aerospace Center (DLR), Microwaves and Radar Institute | 该研究针对通信辅助无人机载MIMO TomoSAR系统，采用粒子群优化算法优化点扩散函数，以改善三维成像性能。 | [#620](https://github.com/thinson/RS-PaperClaw/issues/620) |
| [20260526] Image Thresholding: Understanding Bias of Evaluation Metrics towards Specific Evaluation Functions | Hegazy Eslam, Gabr Mohamed | German University in Cairo | 论文系统分析了图像阈值分割中常用评估指标（SSIM、PSNR等）对特定评价函数的偏向性问题。 | [#621](https://github.com/thinson/RS-PaperClaw/issues/621) |
| [20260526] RoadGIE: Towards A Global-Scale Aerial Benchmark for Generalizable Interactive Road Extraction | Peng Chenxu, Wang Chenxu, Dai Yimian, Liu Yongxiang, Cheng Ming-Ming, Li Xiang | NKIARI；VCIP, CS, Nankai University；AAIS, Nankai University；College of Electronic Engineering, National University of Defense Technology | RoadGIE构建了首个全球尺度航空道路交互式分割基准数据集，重点解决模型跨域泛化难题。 | [#622](https://github.com/thinson/RS-PaperClaw/issues/622) |

## 🔎 观察

- 遥感模型评估体系正从单一精度指标向多维度、抗偏差指标演进，反映领域对可靠性的重视
- 无人机平台与SAR技术的融合持续深化，优化算法从传统方法向群体智能演进

---

Powered by OpenClaw🦞

---
