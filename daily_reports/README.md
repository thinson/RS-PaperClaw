# Daily Reports

最近三天日报（最新在前）：

# [20260507](./202605/20260507.md)
## 📌 今日概况

今日共检索候选论文 8 篇；关键词+LLM 智能匹配遥感交叉论文 5 篇；最终纳入日报 3 篇。

今日研究呈现两大趋势：一是地球系统建模向无网格、观测原生范式演进，上海AI实验室联合多机构推出Earth-o1大气世界模型；二是遥感不确定性量化与地理空间嵌入技术持续深化，分别应用于图像回归与森林恢复监测场景。

## ✨ 今日亮点

- Earth-o1突破传统网格化模拟，实现观测数据直接驱动的大气世界模型
- 不确定性引导的边缘学习为遥感图像回归提供可靠置信度估计
- AlphaEarth地理空间嵌入助力巴西大西洋森林恢复成效量化评估

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260507] Earth-o1: A Grid-free Observation-native Atmospheric World Model | Gong Junchao, Xu Kaiyi, Wei Wangxu, Tu Siwei, Xu Jingyi, Liu Zili, Fan Hang, Zhou Zhiwang, Han Tao, Xiao Yi, Gu Xinyu, Li Zhangrui, Zhang Wenlong, Chen Hao, Yang Xiaokang, Wang Yaqiang, Cheng Lijing, Gentine Pierre, Ouyang Wanli, ..., Bai Lei | Shanghai Artificial Intelligence Laboratory；Department of Information Engineering, The Chinese University of Hong Kong；School of Electronic Information and Electrical Engineering, Shanghai Jiao Tong University；Department of Atmospheric and Oceanic Sciences, Fudan University；School of Information Science and Technology, University of Science and Technology of China；State Key Laboratory of Earth System Numerical Modeling and Application, Institute of Atmospheric Physics, Chinese Academy of Sciences；College of Computer Science and Artificial Intelligence, Fudan University；Department of Earth and Environmental Engineering, Columbia University；Chinese Academy of Meteorological Sciences；School of Atmospheric Sciences, Nanjing University | Earth-o1提出无网格、观测原生的大气世界模型，融合数据同化技术实现地球系统模拟新范式。 | [#480](https://github.com/thinson/RS-PaperClaw/issues/480) |
| [20260507] Uncertainty-Guided Edge Learning for Deep Image Regression in Remote Sensing | Anh Vu Nguyen, Sejdinovic Dino, Chin Tat-Jun | Australian Institute for Machine Learning (AIML), Adelaide University | 该研究引入不确定性引导的边缘学习框架，结合Beta回归提升遥感图像深度回归的可靠性。 | [#481](https://github.com/thinson/RS-PaperClaw/issues/481) |
| [20260508] Characterizing Brazilian Atlantic Forest Restoration Outcomes with Geospatial Alpha Earth Embeddings | Heiman Alice | Stanford University | 基于AlphaEarth地理空间嵌入，研究构建了巴西大西洋森林恢复成效的特征表征与评估方法。 | [#482](https://github.com/thinson/RS-PaperClaw/issues/482) |

## 🔎 观察

- 世界模型技术正从游戏与机器人领域向地球科学渗透，数据同化与观测原生学习成为关键衔接点
- 遥感不确定性量化从后处理走向训练过程嵌入，边缘学习策略有望提升高 stakes 决策场景的可信度

---

Powered by OpenClaw🦞

---

# [20260506](./202605/20260506.md)
## 📌 今日概况

今日共检索候选论文 11 篇；关键词+LLM 智能匹配遥感交叉论文 9 篇；最终纳入日报 8 篇。

今日遥感AI研究呈现三大趋势：一是基础模型轻量化适配（LoRA微调、扩散模型几何控制），二是自主智能体架构创新（多模态元规划器、视觉语言跟踪），三是零标注学习范式兴起（自监督地理推理、原型学习）。量子计算与模糊逻辑也开始渗透高光谱异常检测领域。

## ✨ 今日亮点

- LoRA微调地理基础模型实现野火精准制图，降低 Sentinel-2 应用门槛
- 轻量化多模态元规划器框架打通遥感感知与决策执行闭环
- 零标注地理推理模型 RemoteZero 突破人工标注依赖瓶颈

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260506] Hyperspectral Anomaly Detection Using Einstein Fuzzy Computing and Quantum Neural Network | Lin Chia-Hsiang, Young Si-Sheng, Langari Reza | the Department of Electrical Engineering, Na- verse network architectures；the Institute of Computer and Communication Engineer- Nevertheless, relying solely on residual-based detectors may；the Department of Mechanical Engineering, Texas | 爱因斯坦模糊计算与量子神经网络结合，为高光谱异常检测提供新型混合智能架构。 | [#335](https://github.com/thinson/RS-PaperClaw/issues/335) |
| [20260506] Low-Rank Adaptation of Geospatial Foundation Models for Wildfire Mapping Using Sentinel-2 Data | Shibli Ali, Nascetti Andrea, Ban Yifang | KTH Royal Institute of Technology | 基于LoRA的地理基础模型参数高效微调，实现Sentinel-2野火燃烧区高精度自动提取。 | [#472](https://github.com/thinson/RS-PaperClaw/issues/472) |
| [20260506] Bridging Perception and Action: A Lightweight Multimodal Meta-Planner Framework for Robust Earth Observation Agents | Xu Jinghui, Shangguan Boyi, Zhu Mengke, Liu Hao, Jiang Junhuan, He Guangjun, Feng Pengming, Jin Shichao, Liang Bin, Chang Yongzhe, Tan Junbo, Zhang Tiantian, Wang Xueqian | State Key Laboratory of Space Information System and Integrated Application | 轻量级多模态元规划器框架支撑地球观测智能体从感知到行动的自主闭环决策。 | [#473](https://github.com/thinson/RS-PaperClaw/issues/473) |
| [20260506] VL-UniTrack: A Unified Framework with Visual-Language Prompts for UAV-Ground Visual Tracking | Xu Boyue, Hou Ruichao, Ren Tongwei, Wu Gangshan | State Key Laboratory for Novel Software Technology, Nanjing University | VL-UniTrack统一视觉语言提示框架，实现无人机与地面跨视角目标跟踪协同。 | [#474](https://github.com/thinson/RS-PaperClaw/issues/474) |
| [20260507] Delay-Aware Large-Small Model Collaboration over LEO Satellite Networks | Guo Mingyu, Wu Wen, Wang Ying, Zhang Songge, Li Liang | Frontier Research Center, Pengcheng Laboratory；School of Information and Communication Engineering, Beijing University of Posts and Telecommunications | 大小模型协同架构结合多智能体强化学习，优化低轨卫星网络边缘计算任务卸载。 | [#475](https://github.com/thinson/RS-PaperClaw/issues/475) |
| [20260507] Efficient Geometry-Controlled High-Resolution Satellite Image Synthesis | Vasilescu Vlad, Faur Daniela, Costăchioiu Teodor | Univ. POLITEHNICA Bucharest；SIGMA Lab, CAMPUS Institute；GEOSENSE, CAMPUS Institute | 几何约束扩散模型实现高分辨率卫星影像可控合成，提升生成图像空间精度。 | [#476](https://github.com/thinson/RS-PaperClaw/issues/476) |
| [20260506] RemoteZero: Geospatial Reasoning with Zero Human Annotations | Yao Liang, Liu Fan, Xu Shengxiang, Zhang Chuanyi, Min Rui, Di Shimin, Zheng Yuhui | Hohai University；Southeast University | RemoteZero零标注框架以自监督强化学习驱动多模态大模型地理空间推理能力。 | [#477](https://github.com/thinson/RS-PaperClaw/issues/477) |
| [20260506] UAV as Urban Construction Change Monitor: A New Benchmark and Change Captioning Model | Gao Yupeng, Li Tianyu, Wang Guoqing, Yang Yang | University of Electronic Science and Technology of China | 无人机城市建筑变化监测新基准与变化描述模型，推动细粒度时序遥感理解。 | [#478](https://github.com/thinson/RS-PaperClaw/issues/478) |

## 🔎 观察

- 参数高效微调（PEFT）正成为遥感基础模型落地的关键路径，LoRA等技术显著降低行业适配成本
- 智能体架构从单一感知向"感知-规划-执行"全链条演进，多模态融合与元学习成为核心支撑技术

---

Powered by OpenClaw🦞

---

# [20260505](./202605/20260505.md)
## 📌 今日概况

今日共检索候选论文 6 篇；关键词+LLM 智能匹配遥感交叉论文 3 篇；最终纳入日报 1 篇。

今日遥感AI研究聚焦物理建模与数据质量提升。单篇入选论文提出物理感知的数据集构建方法，针对高分辨率卫星影像去阴影任务，强调从合成数据生成源头解决真实场景适配问题，体现领域对物理可解释性与数据工程并重的趋势。

## ✨ 今日亮点

- 物理感知合成：将大气辐射传输模型嵌入阴影数据集生成流程
- 任务针对性：专为高分辨率卫星影像阴影去除设计基准数据
- 跨机构协作：奥地利、德国、英国多所高校与研究所联合攻关

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260505] deSEO: Physics-Aware Dataset Creation for High-Resolution Satellite Image Shadow Removal | Beltrame Lorenzo, Salzinger Jules, Svoboda Filip, Fanta-Jende Phillipp, Lampert Jasmin, Timofte Radu, Körner Marco | Austrian Institute of Technology；University of Cambridge；University of Würzburg；Technical University of Munich (TUM)；Technical University of Munich (TUM), Munich Data Science Institute (MDSI)；ELLIS Unit Jena, Friedrich Schiller University of Jena | deSEO提出物理感知的高分辨率卫星影像阴影去除数据集构建方法，通过嵌入辐射传输模型提升合成数据的真实场景适配性。 | [#469](https://github.com/thinson/RS-PaperClaw/issues/469) |

## 🔎 观察

- 卫星影像去阴影任务长期受困于真实标注稀缺，物理驱动的合成数据生成或成破局关键路径
- 多机构跨国合作模式在遥感AI领域持续深化，欧洲研究网络在数据基础设施建设中表现活跃

---

Powered by OpenClaw🦞

---
