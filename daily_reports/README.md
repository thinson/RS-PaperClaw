# Daily Reports

最近三天日报（最新在前）：

# [20260626](./202606/20260626.md)
## 📌 今日概况

今日共检索候选论文 7 篇；关键词+LLM 智能匹配遥感交叉论文 3 篇；最终纳入日报 3 篇。

今日遥感AI研究聚焦于多模态大语言模型在遥感变化描述中的应用、跨传感器超分辨率中的域差距量化，以及低空无人机空间智能基准构建。这些工作分别从模型微调、域适应和空间理解评估角度推进遥感智能分析能力。

## ✨ 今日亮点

- 提出RSICCLLM多模态大模型用于遥感变化描述
- 量化跨传感器超分辨率中的域差距问题
- 发布低空无人机空间智能基准SpatialUAV

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260626] RSICCLLM: A Multimodal Large Language Model for Remote Sensing Image Change Captioning | Wang Yelin, Song Zijia, Ye Shuo, Yang Chuanguang, Wang Miaoyu, Xu Yong, An Zhulin, Xu Yongjun, Yu Zitong | State Key Laboratory of AI Safety, Institute of Computing Technology, Chinese；Academy of Sciences, Beijing, China；Great Bay University, Dongguan, China；Harbin Institute of Technology, Shenzhen, China；Dongguan Key Laboratory for Intelligence and Information Technology, Dongguan | RSICCLLM通过差异感知微调实现遥感图像变化描述。 | [#787](https://github.com/thinson/RS-PaperClaw/issues/787) |
| [20260626] Mind the Gap: Quantifying the Domain Gap in Cross-Sensor Diffusion Super-Resolution | Kopeć Dawid, Jabłońska Katarzyna, Kozłowski Wojciech, Zięba Maciej | WUST；Tooploox | 研究量化跨传感器扩散超分辨率中的域差距。 | [#788](https://github.com/thinson/RS-PaperClaw/issues/788) |
| [20260626] SpatialUAV: Benchmarking Spatial Intelligence for Low-Altitude UAV Perception, Collaboration, and Motion | Zhang Haoyu, Liu Meng, Xiang Qianlong, Wang Kun, Wang Yaowei, Nie Liqiang | organizes all samples into a unified visual-input–question–answer respectively, advancing research on spatial understanding in；remains largely grounded in human-centered visual perspec- over more complex input settings and structured answer forms | SpatialUAV基准评估无人机空间感知与协作能力。 | [#789](https://github.com/thinson/RS-PaperClaw/issues/789) |

## 🔎 观察

- 多模态大模型正从通用场景向遥感变化描述等专业任务深化。
- 域差距量化与空间智能基准成为提升遥感模型泛化性的关键方向。

---

Powered by OpenClaw🦞

---

# [20260625](./202606/20260625.md)
## 📌 今日概况

今日共检索候选论文 13 篇；关键词+LLM 智能匹配遥感交叉论文 10 篇；最终纳入日报 10 篇。

今日研究聚焦于遥感智能解译与无人机系统两大方向。世界模型与视频扩散Transformer被用于概率性地球观测预报；高斯泼溅结合生成式精炼提升了卫星三维重建保真度。无人机领域涌现了野火视觉问答基准、安全通信、多会话建图及海空网络预测波束追踪等应用。此外，轻量化语义传输与对抗性数据增强也受到关注。

## ✨ 今日亮点

- 世界模型与扩散Transformer结合，提升地球观测概率预报能力
- 高斯泼溅生成式精炼，实现高保真卫星三维重建
- 无人机野火VQA基准及安全通信测试床推动实用化

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260625] EO-WM: A Physically Informed World Model for Probabilistic Earth Observation Forecasting | Luo Junwei, Yuan Shuai, Yang Zhenya, Li Yansheng, Liu Zhe, Zhao Hengshuang | University of Hong Kong；Wuhan University | 提出物理信息世界模型EO-WM，用于概率性地球观测预报 | [#776](https://github.com/thinson/RS-PaperClaw/issues/776) |
| [20260625] SatSplatDiff: Geometry-preserving generative refinement for high-fidelity satellite Gaussian Splatting | Kim Jiyong, Song Shuang, Qin Ronjgun | Department of Civil, Environmental and Geodetic Engineering, The Ohio State University；Department of Electrical and Computer Engineering, The Ohio State University | SatSplatDiff通过生成式精炼保持几何结构，提升卫星高斯泼溅质量 | [#777](https://github.com/thinson/RS-PaperClaw/issues/777) |
| [20260625] FlameVQA: A Physically-Grounded UAV Wildfire VQA Benchmark with Radiometric Thermal Supervision | Habibpour Mobin, Spodnik John, Niloufar Alipour Talemi, Afghah Fatemeh | Clemson University | FlameVQA构建基于辐射热成像的无人机野火视觉问答基准 | [#778](https://github.com/thinson/RS-PaperClaw/issues/778) |
| [20260625] Design and Performance Evaluation of Secure RF and WiFi-Based Communication in Drone Swarms via Testbed Implementation | Dixit Bhavya, Rajgor Aayushi, Kumar Subham, Patil Rushikesh, A. Ananthapadmanabhan, Gaurav S. Kasbekar, Maity Arnab | Department of Electrical Engineering, Indian Institute of Technology (IIT) Bombay, Mumbai, Maharashtra, India；Department of Aerospace Engineering, IIT Bombay | 设计并实测了基于RF和WiFi的无人机蜂群安全通信方案 | [#779](https://github.com/thinson/RS-PaperClaw/issues/779) |
| [20260625] On-board Remote-Sensing Foundation Models for Unsupervised Change Detection of Disaster Events | Ramírez-Gallego S. | Thales Alenia Space Spain | 利用遥感基础模型在轨实现无监督灾害变化检测 | [#780](https://github.com/thinson/RS-PaperClaw/issues/780) |
| [20260625] UAV-MapFusion: RTK-Aligned Uncertainty-Aware Coarse-to-Fine Multi-Session UAV Mapping | Pan Feng, Zheng Chunran, Xue Bing, Cui Yukang, Wen Jiayu, Chen Zhiyu, Wang Wei | College of Automation, Harbin Engineering University, Harbin, China. (；Department of Mechanical Engineering, University of Hong Kong, Hong Kong SAR, China. (；College of Mechatronics and Control Engineering, Shenzhen University, Shenzhen, China. ( | UAV-MapFusion融合RTK与不确定性，实现多会话无人机建图 | [#781](https://github.com/thinson/RS-PaperClaw/issues/781) |
| [20260625] Learning Adversarial Augmentation Policies for Robust Garlic Seedling Detection | Lee Soeun, Kim Chanho, Kang Yeji, Hong YoungKi, Kang Byeongkeun | School of Electrical and Electronics Engineering, Chung-Ang University；Department of Agricultural Engineering, National Institute of Agricultural Sciences | 学习对抗性增强策略，提升大蒜幼苗检测的鲁棒性 | [#782](https://github.com/thinson/RS-PaperClaw/issues/782) |
| [20260625] Calibrated Harmonic Overlaid Implicit Neural Representations for Multi-Dimensional Data | Chen Honghang, Zhang Xiujun, Sun Xiaoli, Xiao Mingqing | Shenzhen University, Shenzhen, China；Shenzhen Polytechnic University, Shenzhen, China；Southern Illinois University Carbondale, USA | 提出校准谐波叠加隐式神经表示，处理多维数据频谱偏差 | [#783](https://github.com/thinson/RS-PaperClaw/issues/783) |
| [20260625] ISAC for Sea-Air Networks: Predictive Beam Tracking under Sea Induced Disturbances | Zhang Rui, Dong Fuwang, Wang Wei, Du Zhen | College of Intelligent Systems Science and Engineering, Harbin Engineering Univer- sity, Harbin, China (；School of Electronic and Information Engineering, Nanjing University of Information Science and Technology, Nanjing, applied the integrated sensing and communication (ISAC) China ( | 面向海空网络的ISAC系统，实现海况扰动下预测波束追踪 | [#784](https://github.com/thinson/RS-PaperClaw/issues/784) |
| [20260625] SpaceRipple: Lightweight Semantic Delivery for Mission-Oriented LEO Earth Observation Satellite Networks | Yang Ziyi, Yuan Hao, Yi Yunxiang, Wang Wenbo, Zhang Xing | Beijing University of Posts and Telecommunications | SpaceRipple实现面向任务的轻量化语义传输，用于LEO卫星网络 | [#785](https://github.com/thinson/RS-PaperClaw/issues/785) |

## 🔎 观察

- 世界模型与生成式AI正从图像生成向物理约束的遥感预报演进
- 无人机遥感研究从单机感知向蜂群通信、多会话建图等系统级问题深化

---

Powered by OpenClaw🦞

---

# [20260624](./202606/20260624.md)
## 📌 今日概况

今日共检索候选论文 8 篇；关键词+LLM 智能匹配遥感交叉论文 4 篇；最终纳入日报 4 篇。

今日遥感AI研究聚焦于基础模型与高效架构的融合。一方面，大规模数据集LEVIRDet与变化描述基准C3-Bench的提出，推动了通用检测与上下文感知评估的发展；另一方面，状态空间模型（SSM）在遥感中的综述及其在实例分割中的线性时间蒸馏应用，展现了处理长程依赖与多模态数据的新范式。整体趋势向大规模、高效、上下文感知方向演进。

## ✨ 今日亮点

- LEVIRDet发布百万级159类遥感检测数据集与基础模型
- C3-Bench提出上下文感知变化描述评估框架
- SSM综述及线性时间蒸馏用于遥感实例分割

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260624] C3-Bench: A Context-Aware Change Captioning Benchmark | Kim Jae-Woo, Kim Hyeongbeom, Kim Ue-Hwan | Gwangju Institute of Science and Technology, Gwangju, Republic of Korea；GIST InnoCORE AI-Nano Convergence Institute for Early Detection of Neurodegenerative Diseases, Gwangju Institute of Science and Technology | C3-Bench提出上下文感知变化描述基准，采用LLM-as-Judge评估。 | [#772](https://github.com/thinson/RS-PaperClaw/issues/772) |
| [20260624] State Space Models Meet Remote Sensing: A Survey | Yang Qinzhe, Liu Chenyang, Xu Jia, Shi Zhenwei, Zou Zhengxia | Shen Yuan Honors College, Beihang University, Beijing 100191, China；Department of Aerospace Intelligent Science and Technology, School of Astronautics, Beihang University, Beijing 100191, China；State Key Laboratory of Virtual Reality Technology and Systems, Beihang University, Beijing 100191, China；Qian Xuesen Laboratory of Space Technology, China Academy of Space Technology, Beijing 100094, China | 综述探讨状态空间模型在遥感长程依赖与多模态数据中的应用。 | [#773](https://github.com/thinson/RS-PaperClaw/issues/773) |
| [20260624] Efficient Remote Sensing Instance Segmentation with Linear-Time State Space Distilled Visual Foundation Models | Yang Qinzhe, Chen Keyan, Xu Jia, Shi Zhenwei, Zou Zhengxia | Shen Yuan Honors College, Beihang University, Beijing, China；Department of Aerospace Intelligent Science and Technology, School of Astronautics；State Key Laboratory of Virtual Reality Technology and Systems, Beihang University, Beijing, China；Qian Xuesen Laboratory of Space Technology, China Academy of Space Technology, Beijing, China | 线性时间状态空间蒸馏视觉基础模型实现高效遥感实例分割。 | [#774](https://github.com/thinson/RS-PaperClaw/issues/774) |
| [20260624] LEVIRDet: A Million-Scale 159-Category Dataset and Foundation Model for Universal Remote Sensing Object Detection | Yang Qinzhe, Wang Dongyu, Niu Haohan, Xu Jia, Shi Zhenwei, Zou Zhengxia | Shen Yuan Honors College, Beihang University, Beijing, China；Department of Aerospace Intelligent Science and Technology, School of Astronautics；State Key Laboratory of Virtual Reality Technology and Systems, Beihang University, Beijing, China；Qian Xuesen Laboratory of Space Technology, China Academy of Space Technology, Beijing, China | LEVIRDet提供百万级159类数据集，推动通用遥感目标检测。 | [#775](https://github.com/thinson/RS-PaperClaw/issues/775) |

## 🔎 观察

- 状态空间模型正成为遥感长程依赖建模的新主流架构。
- 大规模数据集与基础模型结合，加速遥感通用检测落地。

---

Powered by OpenClaw🦞

---
