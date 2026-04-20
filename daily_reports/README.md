# Daily Reports

最近三天日报（最新在前）：

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

# [20260415](./202604/20260415.md)
## 📌 今日概况

今日共检索候选论文 7 篇；关键词+LLM 智能匹配遥感交叉论文 5 篇；最终纳入日报 5 篇。

今日遥感AI研究呈现两大主线：一是多模态大语言模型与视觉-语言模型的深度融合，覆盖无人机导航、变化检测理解及超高分辨率图像分析；二是面向实际部署的效率优化，包括扩散模型纹理感知超分与早期退出机制的轻量化网络。研究趋势从单一任务向统一理解、从实验室向边缘设备延伸。

## ✨ 今日亮点

- 视觉-语言导航为无人机具身智能开辟新方向，统一路线图厘清技术挑战
- 多模态大模型首次统一遥感变化检测与语义理解，突破时序推理瓶颈
- 预算感知Token压缩方案破解超高分辨率遥感图像的计算成本难题

## 🗂 今日文章列表

| 标题 | 作者 | 一句话概括 | Issue |
|---|---|---|---|
| [20260415] Vision-and-Language Navigation for UAVs: Progress, Challenges, and a Research Roadmap | Chen Hanxuan, Zheng Jie, Yang Siqi, Zeng Tianle, Feng Siwei et al. | 系统综述无人机视觉-语言导航进展，提出融合VLM与VLA模型的研究路线图。 | [#172](https://github.com/thinson/RS-PaperClaw/issues/172) |
| [20260415] Decoding the Delta: Unifying Remote Sensing Change Detection and Understanding with Multimodal Large Language Models | Li Xiaohe, Li Jiahao, Zhang Kaixin, Fang Yuqiang, Lin Leilei et al. | 构建多模态大语言模型统一框架，实现遥感变化检测与高层语义理解的联合推理。 | [#350](https://github.com/thinson/RS-PaperClaw/issues/350) |
| [20260415] Remote Sensing Image Super-Resolution for Imbalanced Textures: A Texture-Aware Diffusion Framework | Zhang Enzhuo, Zhao Sijie, Muhtar Dilxat, Li Zhenshi, Zhang Xueliang et al. | 提出纹理感知扩散框架，针对性解决遥感图像超分辨率中纹理不平衡问题。 | [#351](https://github.com/thinson/RS-PaperClaw/issues/351) |
| [20260415] Early Exiting U-Net for Efficient Processing on UAVs: A Case Study in Environmental Monitoring | Luca Sartori Boni, Moursi Mohamed, Wehn Norbert, Hammoud Bilal | 设计早期退出U-Net架构，在环境监测油膜检测任务中验证无人机实时处理可行性。 | [#352](https://github.com/thinson/RS-PaperClaw/issues/352) |
| [20260415] UHR-BAT: Budget-Aware Token Compression Vision-Language model for Ultra-High-Resolution Remote Sensing | Dang Yunkai, Dai Minxin, Yang Yuekun, Li Zhangnan, Li Wenbin et al. | 开发预算感知Token压缩视觉-语言模型，平衡超高分辨率遥感分析精度与计算开销。 | [#353](https://github.com/thinson/RS-PaperClaw/issues/353) |

## 🔎 观察

- 视觉-语言模型正从通用领域向遥感专用场景深度渗透，但超高分辨率带来的Token爆炸仍需硬件协同优化
- 早期退出与动态计算机制成为无人机等边缘设备部署的关键技术，效率与精度的帕累托前沿尚待突破

---

Powered by OpenClaw🦞

---
