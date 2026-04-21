# Daily Reports

最近三天日报（最新在前）：

# [20260418](./202604/20260418.md)
## 📌 今日概况

今日共检索候选论文 8 篇；关键词+LLM 智能匹配遥感交叉论文 5 篇；最终纳入日报 2 篇。

今日遥感AI研究呈现两大方向：一是深度学习与InSAR技术融合用于积雪参数反演，二是强化学习驱动的SAR平台智能任务规划。合成孔径雷达（SAR）成为核心传感器，深度学习方法在物理参数估计与自主决策中发挥关键作用。

## ✨ 今日亮点

- 深度学习赋能InSAR积雪深度反演，突破传统干涉测量局限性
- 多阶段强化学习实现SAR平台多目标监视轨迹智能规划
- SAR数据与AI方法深度融合，推动遥感应用从观测向自主决策演进

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260418] Deep Learning-Based Snow Depth Retrieval Using Sentinel-1 Repeat-Pass InSAR | Yadav Nayan, Oveisgharan Shadi, Jalali Shirin | Rutgers University；California Institute of Technology | 提出基于深度学习的Sentinel-1重复轨道InSAR积雪深度反演方法，利用神经网络从干涉相位中提取积雪深度信息。 | [#372](https://github.com/thinson/RS-PaperClaw/issues/372) |
| [20260418] Multi-stage Planning for Multi-target Surveillance using Aircrafts Equipped with Synthetic Aperture Radars Aware of Target Visibility | Fuertes Daniel, Carlos R. del-Blanco, Jaureguizar Fernando, Juan José Navarro-Corcuera, García Narciso | Universidad Politécnica de Madrid | 设计多阶段深度强化学习框架，为搭载SAR的无人机规划多目标监视轨迹，并显式考虑目标可见性约束。 | [#373](https://github.com/thinson/RS-PaperClaw/issues/373) |

## 🔎 观察

- InSAR与深度学习结合正成为积雪遥感的新兴方向，有望解决干雪穿透导致的信号衰减难题
- SAR平台任务规划从规则驱动转向数据驱动，强化学习为复杂监视场景提供可扩展决策方案

---

Powered by OpenClaw🦞

---

# [20260417](./202604/20260417.md)
## 📌 今日概况

今日共检索候选论文 11 篇；关键词+LLM 智能匹配遥感交叉论文 7 篇；最终纳入日报 6 篇。

今日遥感AI研究呈现多模态融合与轻量化并重的趋势。无人机导航与分割任务持续引入大语言模型能力，高光谱分类探索高效Transformer架构，知识驱动方法借助LLM实现伪标签生成。同时，开放词汇分割基准建设与阴影去除等底层视觉任务亦有新进展。

## ✨ 今日亮点

- FineCog-Nav将细粒度认知模块融入零样本多模态无人机导航，提升复杂环境决策能力
- 波兰团队利用LLM专家知识驱动伪标签生成，实现高光谱树种分类的知识增强
- SSFT提出轻量光谱-空间融合Transformer，兼顾高光谱分类精度与计算效率

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260417] FineCog-Nav: Integrating Fine-grained Cognitive Modules for Zero-shot Multimodal UAV Navigation | Shao Dian, Xu Zhengzheng, Wang Peiyang, Liu Like, Wang Yule, Shi Jieqi, Huo Jing | Northwestern Polytechnical University；Nanjing University | FineCog-Nav通过整合细粒度认知模块，实现零样本多模态无人机视觉语言导航。 | [#364](https://github.com/thinson/RS-PaperClaw/issues/364) |
| [20260417] From Articles to Canopies: Knowledge-Driven Pseudo-Labelling for Tree Species Classification using LLM Experts | Romaszewski Michał, Kopeć Dominik, Cholewa Michał, Kołodziej Katarzyna, Głomb Przemysław, Niedzielko Jan, Charyton Jakub, Wylazłowska Justyna, Jarocińska Anna | Institute of Theoretical and Applied Informatics, Polish Academy of Sciences；University of Lodz；MGGP Aero；University of Warsaw, Faculty of Geography and Regional Studies, Department of Geoinformatics, Cartography and Remote Sensing | 该研究借助大语言模型专家从文献中提取知识，驱动高光谱树种分类的伪标签生成。 | [#366](https://github.com/thinson/RS-PaperClaw/issues/366) |
| [20260417] SSFT: A Lightweight Spectral-Spatial Fusion Transformer for Generic Hyperspectral Classification | Musiat Alexander, Ebert Nikolas, Wasenmüller Oliver | Mannheim University of Applied Sciences | SSFT以轻量化设计实现光谱-空间特征融合，面向通用高光谱分类任务。 | [#367](https://github.com/thinson/RS-PaperClaw/issues/367) |
| [20260417] PixDLM: A Dual-Path Multimodal Language Model for UAV Reasoning Segmentation | Ke Shuyan, Mei Yifan, Wu Changli, Zheng Yonghan, Ji Jiayi, Cao Liujuan, Ji Rongrong | Key Laboratory of Multimedia Trusted Perception and Efficient Computing, Ministry of Education of China, Xiamen University；Shanghai Innovation Institute | PixDLM构建双路径多模态语言模型，专门处理无人机推理分割任务。 | [#368](https://github.com/thinson/RS-PaperClaw/issues/368) |
| [20260417] Towards Realistic Open-Vocabulary Remote Sensing Segmentation: Benchmark and Baseline | Li Bingyu, Huo Tao, Dong Haocheng, Zhang Da, Zhao Zhiyuan, Gao Junyu, Li Xuelong | University of Science and Technology of China | 该工作建立真实场景开放词汇遥感分割基准，并提供基线方法。 | [#369](https://github.com/thinson/RS-PaperClaw/issues/369) |
| [20260417] Winner of CVPR2026 NTIRE Challenge on Image Shadow Removal: Semantic and Geometric Guidance for Shadow Removal via Cascaded Refinement | Beltrame Lorenzo, Salzinger Jules, Svoboda Filip, Lampert Jasmin, Fanta-Jende Phillipp, Timofte Radu, Koerner Marco | Austrian Institute of Technology；Technical University of Munich；University of Cambridge；University of Würzburg | NTIRE2026阴影去除冠军方案采用语义与几何引导的级联精修策略。 | [#371](https://github.com/thinson/RS-PaperClaw/issues/371) |

## 🔎 观察

- 无人机智能体正快速吸收大语言模型的推理与泛化能力，导航与分割任务边界趋于融合
- 高光谱领域同时涌现知识驱动与轻量化架构两条技术路线，反映应用落地对效率与精度的双重诉求

---

Powered by OpenClaw🦞

---

# [20260416](./202604/20260416.md)
## 📌 今日概况

今日共检索候选论文 9 篇；关键词+LLM 智能匹配遥感交叉论文 7 篇；最终纳入日报 7 篇。

今日遥感AI研究呈现多模态融合与极端条件鲁棒性两大主线。视觉基础模型持续向垂直领域渗透，SAM适配、超分辨率重建等任务涌现新范式；同时，大气扰动、低光照等真实场景下的模型可靠性受到关注。跨模态创新显著，卫星图像驱动声景生成开辟地理-声学对齐新方向。

## ✨ 今日亮点

- Geo2Sound构建首个地理对齐声景生成框架，实现卫星影像到环境音频的跨模态合成
- MapSR利用视觉基础模型与提示工程，以弱监督方式实现土地覆盖图超分辨率重建
- WILD-SAM针对InSAR干涉图相位特性，设计专家混合机制适配SAM进行滑坡检测

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260416] Building Extraction from Remote Sensing Imagery under Hazy and Low-light Conditions: Benchmark and Baseline | Sang Feifei, Lu Wei, Chen Hongruixuan, Chen Sibao, Luo Bin | Wuhan University | 构建雾霾与低光照条件下的建筑提取基准数据集，为极端天气场景下的遥感目标识别提供评估基准与基线方法。 | [#355](https://github.com/thinson/RS-PaperClaw/issues/355) |
| [20260416] OmniGCD: Abstracting Generalized Category Discovery for Modality Agnosticism | Shipard Jordan, Wiliem Arnold, Kien Nguyen Thanh, Xiang Wei, Fookes Clinton | SAIVT, QUT；Shield AI；La Trobe University | 提出OmniGCD框架，通过模态无关学习抽象广义类别发现任务，实现跨模态零样本类别识别能力。 | [#356](https://github.com/thinson/RS-PaperClaw/issues/356) |
| [20260416] Geo2Sound: A Scalable Geo-Aligned Framework for Soundscape Generation from Satellite Imagery | Wu Kunlin, Wang Yanning, Tan Haofeng, Chen Boyi, Fei Teng, Ma Xianping, Yue Yang, Zhou Zan, Liu Xiaofeng | The Hong Kong University of Science and Technology (Guangzhou)；University of South Carolina；University of Canterbury；Southwest Jiaotong University；Beijing University of Posts and Telecommunications | Geo2Sound建立可扩展的地理对齐框架，首次实现从卫星影像到对应地理位置声景的自动化生成。 | [#357](https://github.com/thinson/RS-PaperClaw/issues/357) |
| [20260416] Physically-Induced Atmospheric Adversarial Perturbations: Enhancing Transferability and Robustness in Remote Sensing Image Classification | Zhuang Weiwei, Xie Wangze, Zhang Qi, Du Xia, Lin Zihan, Lin Zheng, Cai Hanlin, Zhou Jizhe, Fang Zihan, Pun Chi-man, Ni Wei, Luo Jun | Tsinghua University；Chinese Academy of Sciences | 设计物理诱导的大气对抗扰动攻击方法，利用雾模拟增强遥感图像分类对抗样本的迁移性与鲁棒性。 | [#358](https://github.com/thinson/RS-PaperClaw/issues/358) |
| [20260416] A multi-platform LiDAR dataset for standardized forest inventory measurement at long term ecological monitoring sites | Michael R. Chang, Candotti Anna, Karl von Ellenrieder, Tomelleri Enrico, Camurri Marco | Faculty of Engineering, Free University of Bozen-Bolzano；Department of Industrial Engineering, University of Trento；Faculty of Agricultural, Environmental and Food Sciences, Free University of Bozen-Bolzano；Competence Centre for Mountain Innovation Ecosystems, Free University of Bozen-Bolzano | 发布多平台激光雷达数据集，整合地基、移动与无人机LiDAR系统，支撑长期生态监测站的标准化森林清查。 | [#359](https://github.com/thinson/RS-PaperClaw/issues/359) |
| [20260416] MapSR: Prompt-Driven Land Cover Map Super-Resolution via Vision Foundation Models | Wang Ruiqi, Yu Qi, Ma Jie, Wu Hanlin | Chinese Academy of Sciences | MapSR基于视觉基础模型与提示驱动策略，以弱监督学习实现土地覆盖图的超分辨率重建。 | [#360](https://github.com/thinson/RS-PaperClaw/issues/360) |
| [20260416] WILD-SAM: Phase-Aware Expert Adaptation of SAM for Landslide Detection in Wrapped InSAR Interferograms | Pan Yucheng, Li Heping, Liu Zhangle, Hussain Sajid, Pan Bin | China University of Geosciences (Wuhan)；China University of Geosciences；Wuhan University；National University of Sciences and Technology (NUST) | WILD-SAM针对缠绕InSAR干涉图的相位特性，采用混合专家自适应机制扩展SAM用于滑坡检测。 | [#361](https://github.com/thinson/RS-PaperClaw/issues/361) |

## 🔎 观察

- 视觉基础模型正从通用分割向遥感专用任务深度适配，相位感知、提示工程等细粒度机制成为关键创新点
- 跨模态研究从视觉-文本向视觉-音频拓展，地理空间数据与多感官信息的联合建模或成新增长极

---

Powered by OpenClaw🦞

---
