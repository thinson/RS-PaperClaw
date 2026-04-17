# Daily Reports

最近三天日报（最新在前）：

# [20260416](./202604/20260416.md)
## 📌 今日概况

今日共检索候选论文 9 篇；关键词+LLM 智能匹配遥感交叉论文 7 篇；最终纳入日报 7 篇。

今日遥感AI研究呈现多模态融合与鲁棒性增强两大主线。视觉基础模型持续向垂直领域渗透，SAM适配、跨模态生成与弱监督学习成为热点；同时，恶劣天气与对抗攻击下的模型可靠性受到关注，数据集建设与物理仿真并重推进。

## ✨ 今日亮点

- Geo2Sound开创卫星影像到声景的跨模态生成新方向，拓展遥感数据应用边界
- WILD-SAM将SAM引入InSAR相位干涉图，专家混合架构适配地质灾害监测
- MapSR探索视觉基础模型驱动的土地覆盖图超分辨率，降低标注依赖

## 🗂 今日文章列表

| 标题 | 作者 | 一句话概括 | Issue |
|---|---|---|---|
| [20260416] Building Extraction from Remote Sensing Imagery under Hazy and Low-light Conditions: Benchmark and Baseline | Sang Feifei, Lu Wei, Chen Hongruixuan, Chen Sibao, Luo Bin | 构建雾霾与低光照条件下的建筑提取基准数据集，填补恶劣天气场景评估空白。 | [#355](https://github.com/thinson/RS-PaperClaw/issues/355) |
| [20260416] OmniGCD: Abstracting Generalized Category Discovery for Modality Agnosticism | Shipard Jordan, Wiliem Arnold, Kien Nguyen Thanh, Xiang Wei, Fookes Clinton | 提出模态无关的广义类别发现框架，实现跨模态零样本泛化能力统一抽象。 | [#356](https://github.com/thinson/RS-PaperClaw/issues/356) |
| [20260416] Geo2Sound: A Scalable Geo-Aligned Framework for Soundscape Generation from Satellite Imagery | Wu Kunlin, Wang Yanning, Tan Haofeng, Chen Boyi, Fei Teng, Ma Xianping, Yue Yang, Zhou Zan, Liu Xiaofeng | Geo2Sound建立地理对齐的卫星影像到声景生成框架，实现可扩展音频合成。 | [#357](https://github.com/thinson/RS-PaperClaw/issues/357) |
| [20260416] Physically-Induced Atmospheric Adversarial Perturbations: Enhancing Transferability and Robustness in Remote Sensing Image Classification | Zhuang Weiwei, Xie Wangze, Zhang Qi, Du Xia, Lin Zihan, Lin Zheng, Cai Hanlin, Zhou Jizhe, Fang Zihan, Pun Chi-man, Ni Wei, Luo Jun | 设计物理诱导的大气对抗扰动方法，增强遥感图像分类的迁移攻击鲁棒性。 | [#358](https://github.com/thinson/RS-PaperClaw/issues/358) |
| [20260416] A multi-platform LiDAR dataset for standardized forest inventory measurement at long term ecological monitoring sites | Michael R. Chang, Candotti Anna, Karl von Ellenrieder, Tomelleri Enrico, Camurri Marco | 发布多平台激光雷达森林清查数据集，支撑长期生态监测站点标准化测量。 | [#359](https://github.com/thinson/RS-PaperClaw/issues/359) |
| [20260416] MapSR: Prompt-Driven Land Cover Map Super-Resolution via Vision Foundation Models | Wang Ruiqi, Yu Qi, Ma Jie, Wu Hanlin | MapSR以提示驱动视觉基础模型实现土地覆盖图超分辨率，采用弱监督策略。 | [#360](https://github.com/thinson/RS-PaperClaw/issues/360) |
| [20260416] WILD-SAM: Phase-Aware Expert Adaptation of SAM for Landslide Detection in Wrapped InSAR Interferograms | Pan Yucheng, Li Heping, Liu Zhangle, Hussain Sajid, Pan Bin | WILD-SAM通过相位感知专家适配，将SAM扩展至缠绕InSAR干涉图的滑坡检测。 | [#361](https://github.com/thinson/RS-PaperClaw/issues/361) |

## 🔎 观察

- 视觉基础模型正从通用分割向地球科学专用任务深度适配，相位感知等物理约束融入成为差异化关键
- 跨模态生成与模态无关学习同步涌现，暗示遥感AI正突破视觉单模态局限，向多源感知融合演进

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

# [20260414](./202604/20260414.md)
## 📌 今日概况

今日共检索候选论文 12 篇；关键词+LLM 智能匹配遥感交叉论文 5 篇；最终纳入日报 5 篇。

今日遥感AI研究聚焦轻量化部署与多模态融合两大主线。星载边缘计算需求推动轻量图像修复网络发展，多智能体系统赋能卫星影像事件理解与描述。高光谱去噪、梯田地块提取及全色锐化等任务持续深化，数学物理方法（欧拉公式、全变分）与深度学习结合趋势明显。

## ✨ 今日亮点

- 星载AI轻量化：面向卫星在轨处理的轻量学习图像修复方法
- 多智能体事件感知：卫星影像新闻事件检测与描述的反馈协作系统
- 多模态农业数据：全球梯田地块边界数据集融合光学与高程信息

## 🗂 今日文章列表

| 标题 | 作者 | 一句话概括 | Issue |
|---|---|---|---|
| [20260414] Rethinking Satellite Image Restoration for Onboard AI: A Lightweight Learning-Based Approach | Dorise Adrien, Bellizzi Marjorie, Hlimi Omar | 提出轻量学习网络实现卫星图像在轨修复，降低星载AI计算资源消耗。 | [#343](https://github.com/thinson/RS-PaperClaw/issues/343) |
| [20260414] A Multi-Agent Feedback System for Detecting and Describing News Events in Satellite Imagery | Anderson Madeline, Klassen Mikhail, Hoover Ash, Cahoy Kerri | 构建多智能体反馈系统，实现卫星影像多时相变化检测与事件自动描述。 | [#344](https://github.com/thinson/RS-PaperClaw/issues/344) |
| [20260414] Spatial-Spectral Adaptive Fidelity and Noise Prior Reduction Guided Hyperspectral Image Denoising | Xie Xuelin, Lu Xiliang, Wang Zhengshan, Zhang Yang, Chen Long | 设计空间-光谱自适应保真与噪声先验降维方法，提升高光谱混合噪声去除效果。 | [#345](https://github.com/thinson/RS-PaperClaw/issues/345) |
| [20260414] GTPBD-MM: A Global Terraced Parcel and Boundary Dataset with Multi-Modality | Zhang Zhiwei, Zeng Xingyuan, Kong Xinkai, Zhang Kunquan, Liang Haoyuan et al. | 发布全球多模态梯田地块边界数据集，融合遥感影像与数字高程模型信息。 | [#347](https://github.com/thinson/RS-PaperClaw/issues/347) |
| [20260414] Euler-inspired Decoupling Neural Operator for Efficient Pansharpening | Zhu Anqi, Ma Mengting, Jiang Yizhen, Li Xiangdong, Zheng Kai et al. | 基于欧拉公式解耦神经算子，实现高效全色锐化频率域处理。 | [#349](https://github.com/thinson/RS-PaperClaw/issues/349) |

## 🔎 观察

- 星载边缘智能成为新焦点，轻量化设计从模型压缩转向任务特定的网络架构重构。
- 多智能体架构开始渗透遥感解译流程，人机协作范式或重塑卫星影像信息提取模式。

---

Powered by OpenClaw🦞

---
