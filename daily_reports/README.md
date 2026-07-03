# Daily Reports

最近三天日报（最新在前）：

# [20260702](./202607/20260702.md)
## 📌 今日概况

今日共检索候选论文 8 篇；关键词+LLM 智能匹配遥感交叉论文 5 篇；最终纳入日报 5 篇。

今日遥感研究聚焦于智能解译与数据发现两大方向。云去除结合残差流与地理上下文对齐提升可解释性；多篇工作探索大语言模型与知识图谱在遥感数据检索、假设生成及无人机自主决策中的应用；持续学习框架被引入变化检测以应对域偏移问题。

## ✨ 今日亮点

- 云去除方法引入残差流与地理上下文对齐提升可解释性
- 多篇工作探索LLM与知识图谱驱动遥感数据智能发现
- 持续学习框架被用于域增量变化检测任务

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260702] Interpretation-Oriented Cloud Removal via Observation-Anchored Residual Flow with Geo-Contextual Alignment | Wang Ziyao, Wang Maonan, He Yucheng, Ma Xianping, Wang Ziyi, Zhang Hongyang, Cheng Yirong, Pun Man-on | School of Science and Engineering, The Chinese University of Hong Kong；Shanghai Ai Lab, Shanghai, China；Faculty of Geosciences and Engineering, Southwest Jiaotong University, Chengdu | 提出面向可解释的云去除方法，利用观测锚定残差流与地理上下文对齐。 | [#832](https://github.com/thinson/RS-PaperClaw/issues/832) |
| [20260702] Bringing Agentic Search to Earth Observation Data Discovery | Yu Minghan, Sun Youran, Yi Chugang, Wen Yixin, Yang Haizhao | University of Maryland, College Park University of Maryland, College Park；University of Maryland, College Park University of Florida；University of Maryland, College Park；NASA and its data centers hold thousands of geoscience datasets and tools like；metadata, tools, and access pathways. NASA and its affiliated data centers host thousands of datasets；across dozens of Distributed Active Archive Centers (DAACs), together with tools such as Worldview；domain experts to locate the data that best matches their own research question | 将智能体搜索引入地球观测数据发现，提升数据集检索效率。 | [#833](https://github.com/thinson/RS-PaperClaw/issues/833) |
| [20260702] Dual-Selective Network for Domain-Incremental Change Detection | He Yuzhi, Huang Junxi, Wu Haorui, Qu Jiahui | Xidian University, Xi'an, China | 提出双选择性网络用于域增量变化检测，结合视觉状态空间模型。 | [#834](https://github.com/thinson/RS-PaperClaw/issues/834) |
| [20260702] NEUROSYMLAND: Neuro-Symbolic Landing-Site Assessment for Robust and Edge-Deployable UAV Autonomy | Qian Weixian, Yang Tianyi, Schroder Sebastian, Deng Yao, Yao Jiaohong, Cheng Xiao, Han Richard, Zheng Xi | School of Computing, Macquarie University, Sydney, NSW, Australia；Macquarie University, when this work was conducted；Department of Computer Science, University of California, Santa Barbara, CA, USA. tianyi | 神经符号方法实现无人机着陆点评估，支持边缘部署与鲁棒自主。 | [#835](https://github.com/thinson/RS-PaperClaw/issues/835) |
| [20260702] EO-Agents: A Three-Agent LLM Pipeline for Earth Observation Hypothesis Generation | Ghazanfari Mahyar, Tabrizian Amin, Mehrabian Armin, Wei Peng | Earth-observation (EO) research is fundamentally combina-；Washington University, Washington, DC, USA；Space Flight Center, Greenbelt, MD, USA | 构建三智能体LLM流水线，自动生成地球观测科学假设。 | [#836](https://github.com/thinson/RS-PaperClaw/issues/836) |

## 🔎 观察

- 大语言模型正从辅助工具演变为遥感数据发现与假设生成的核心引擎。
- 持续学习与域适应成为变化检测研究新热点，应对多源数据分布漂移。

---

Powered by OpenClaw🦞

---

# [20260701](./202607/20260701.md)
## 📌 今日概况

今日共检索候选论文 17 篇；关键词+LLM 智能匹配遥感交叉论文 6 篇；最终纳入日报 6 篇。

今日遥感研究呈现多模态融合与精细化建模两大趋势。视觉定位任务引入过程监督与锚点引导推理，提升复杂场景理解能力。无人机图像分析聚焦质量评估与高效检测微调，结合视觉-语言模型。三维重建方面，轨道射线条件约束的3D基础模型提升了卫星多视角重建精度。此外，不确定性感知的树高变化回归与极化SAR土壤水分反演，体现了对物理过程与量测不确定性的深入建模。

## ✨ 今日亮点

- 多模态大模型在遥感视觉定位中引入过程监督机制
- 无人机图像分析结合视觉-语言模型实现质量评估与高效检测
- 卫星三维重建与森林动态监测强调物理约束与不确定性建模

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260701] GeoSearcher: Anchor-Guided Progressive Reasoning for Remote Sensing Visual Grounding with Process Supervision | Wang Dianyu, Zhang Yidan, Zhang Peirong, Li Xuyang, Liu Xiaoxuan, Wang Lei | School of Electronic, Electrical and Communication Engineering, University of Chinese Academy of Sciences, Beijing, China ( | GeoSearcher提出锚点引导渐进推理，实现遥感视觉定位的过程监督。 | [#825](https://github.com/thinson/RS-PaperClaw/issues/825) |
| [20260701] Uncertainty-aware tree height change regression | Gaber Max, Gominski Dimitri, Jaime C. Revenga, Oehmcke Stefan, Fensholt Rasmus, Brandt Martin | Department of Mathematical Sciences, University of Copenhagen；Department of Computer Science and Electrical Engineering, University of Rostock；Department of Computer Science, University of Copenhagen | 不确定性感知回归模型用于树高变化估计，提升森林动态监测可靠性。 | [#826](https://github.com/thinson/RS-PaperClaw/issues/826) |
| [20260701] EO-VGGT: Orbital Ray-Conditioned 3D Foundation Models for Satellite Multi-View Reconstruction | Luo Qiyan, Pi Yingdong, Wen Lekang, Yang Jie, Wang Xiaoyu, Zhang Haiming, Wang Mi | State Key Laboratory of Information Engineering in Surveying, Mapping and Remote Sensing, Wuhan University；Hubei Luojia Laboratory | EO-VGGT利用轨道射线条件约束，构建卫星多视角重建3D基础模型。 | [#827](https://github.com/thinson/RS-PaperClaw/issues/827) |
| [20260701] DroneIQA-VLE: Multi-Task Drone Image Quality Assessment via Vision-Language Ensemble | Sun Wei, Zhang Weixia, Zhan Hongjian, Lu Mingkai, Gao Yixuan, Zhai Guangtao | East China Normal University；Shanghai Jiao Tong University；To promote research on UAV-oriented quality modeling | DroneIQA-VLE通过视觉-语言集成实现无人机图像多任务质量评估。 | [#828](https://github.com/thinson/RS-PaperClaw/issues/828) |
| [20260701] DroneFINE: Domain-Aware Parameter-Efficient Fine-Tuning of Vision-Language Detectors for Drone Images | Wu Ke, Zhang Yanan, Gao Yingjie, Li Wenhao, Zhou Chenyu, Ma XinZhu, Chen Jiaxin, Huang Di | National College for Excellent Engineers, Beihang University, Beijing, China；School of Computer Science and Engineering, Beihang University, Beijing, China；School of Computer Science and Information Engineering, Hefei University of；State Key Laboratory of Virtual Reality Technology and Systems, Beihang；University, Beijing, China；Innovation Center for Intelligent System Cognition and Decision-Making, Beijing；Information Science Academy of China Electronics Technology Group Corporation | DroneFINE提出域感知参数高效微调，适配无人机图像的视觉语言检测。 | [#829](https://github.com/thinson/RS-PaperClaw/issues/829) |
| [20260701] Polarimetric SAR Model Fitting for Soil Moisture Retrieval: Study of PALSAR-2 data over a Heterogeneous Mine Environment in Finland | Antropov Oleg, Hamedianfar Alireza, Molinier Matthieu, Salmela Ulla, Kukkula Hanna, Seitsonen Lauri, Liwata-Kenttälä Pauliina, Middleton Maarit | VTT Technical Research Centre of Finland, Espoo, Finland | 极化SAR半经验模型用于芬兰矿区土壤水分反演，分析PALSAR-2时序数据。 | [#830](https://github.com/thinson/RS-PaperClaw/issues/830) |

## 🔎 观察

- 视觉-语言模型正从通用场景向遥感垂直领域渗透，驱动定位、检测与质量评估任务革新。
- 遥感基础模型发展更注重物理先验（如轨道几何、极化散射）与不确定性量化，提升可解释性。

---

Powered by OpenClaw🦞

---

# [20260630](./202606/20260630.md)
## 📌 今日概况

今日共检索候选论文 20 篇；关键词+LLM 智能匹配遥感交叉论文 19 篇；最终纳入日报 19 篇。

今日遥感AI研究呈现三大热点：一是Agentic AI框架在林业、植物表型、无人机自主着陆等领域的广泛应用，推动自动化与科学发现；二是无人机（UAV）相关研究密集，涵盖导航、通信、协同规划及能量优化；三是基础模型创新活跃，如Mamba架构用于SAR识别、扩散模型用于轨迹预测，以及多光谱检测与高光谱成像技术的新进展。

## ✨ 今日亮点

- Agentic AI加速遥感自动化与科学发现
- 无人机自主导航与协同任务规划研究密集
- Mamba与扩散模型等新架构推动基础模型创新

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260630] TreeAgent: A Generalizable Multi-Agent Framework for Automated Bias Labeling in Forestry via Compiled Expert Rules and Vision-Language Models | Chen Shiyi, Saban Nicholas, Hargreaves Collin, Wang Huiqi | University of California, Berkeley, California, United States | 提出TreeAgent多智能体框架，结合专家规则与视觉语言模型自动标注林业偏差。 | [#805](https://github.com/thinson/RS-PaperClaw/issues/805) |
| [20260630] An Agentic AI Framework to Accelerate Scientific Discovery in Plant Phenotyping | Souza Renan, Rosendo Daniel, Carter Kelsey, Lagergren John, Suter Frédéric, Shelaine L. Curd, Gerald A. Tuskan, Rafael Ferreira da Silva, Weston David | Oak Ridge National Laboratory, Oak Ridge, TN, USA；At Oak Ridge National Laboratory’s Advanced Plant Phenotyp-；ing Laboratory (APPL), automated stations image hundreds of；across scientific domains, and nations and institutions are；DOE 1) An end-to-end AI agentic framework for highnational laboratories, industry, and academia to harness AI；contract DE-AC05-00 OR22725 with the US Department of Energy (DOE) | 构建Agentic AI框架，加速植物表型高通量成像中的科学发现。 | [#806](https://github.com/thinson/RS-PaperClaw/issues/806) |
| [20260630] Absorption-Feature-Guided Distance-Decoupled Estimation and Band Selection for LWIR Hyperspectral Passive Ranging | Liu Shuo, Fan Chen, Chen Zhihe, Huang Xiaolin, Zhang Lilian | College of Intelligence Science and Technology, National University of Defense Technology, Changsha, China | 提出吸收特征引导的距离解耦估计与波段选择方法，用于长波红外高光谱被动测距。 | [#807](https://github.com/thinson/RS-PaperClaw/issues/807) |
| [20260630] Autonomous UAV Navigation for Individual Wildlife Re-Identification | Sun Claire, Berger-Wolf Tanya, Kline Jenna | The Ohio State University | 实现无人机自主导航对个体野生动物进行重识别，集成检测与姿态分类。 | [#808](https://github.com/thinson/RS-PaperClaw/issues/808) |
| [20260630] JL1-CC&QA: Extending the JL1-CD Benchmark with Change Captioning and Question Answering | Liu Ziyuan, Zhu Ruifei, Ma Ouqiao, Gu Yuantao | Department of Electronic Engineering, Beijing National Research Center for Information Science and Technology, Tsinghua University, Beijing, China (；College of Communications Engineering, Army Engineering University of PLA, Nanjing, China ( | 扩展JL1-CD基准，新增变化描述与问答任务，支持多任务学习。 | [#809](https://github.com/thinson/RS-PaperClaw/issues/809) |
| [20260630] SAMBA: A Scatter-Guided Masked Bidirectional Mamba Foundation Model for SAR Target Recognition | Wang Ke, Pan Xiaoyi, Gu Zhaoyu, Ai Xiaofeng, Xu Zhiming, Zhao Feng, Xiao Shunping | College of Electronic Science and Technology, National University of Defense Technology, Changsha, China ( | 提出散射引导的掩码双向Mamba基础模型SAMBA，用于SAR目标识别。 | [#810](https://github.com/thinson/RS-PaperClaw/issues/810) |
| [20260630] DynFly: Dynamic-Aware Continuous Trajectory Generation for UAV Vision-Language Navigation in Urban Environments | Jiang Wen, Liang Hanfang, Wang Li, Huang Kangyao, Xu Wang, Fan Wei, Liu Jinyuan, Liu Shaoyu, Duan Hongwei, Xu Bin, Ji Xiangyang, Liu Huaping | School of Mechanical Engineering, Beijing Institute of Technology；Department of Computer Science and Technology, Tsinghua University；Department of Automation, Tsinghua University；School of Software, Dalian University of Technology；School of Artificial Intelligence, Xidian University；School of Artificial Intelligence and Automation, Huazhong University of Science and Technology；Chongqing Innovation Center, Beijing Institute of Technology | 提出DynFly框架，实现城市环境中无人机视觉-语言导航的动态感知连续轨迹生成。 | [#811](https://github.com/thinson/RS-PaperClaw/issues/811) |
| [20260630] Robust Autonomous UAV Landing on Maritime Platforms via Multimodal Agentic AI and Active Wave Compensation | Francisco S. Neves, Pedro N. Pereira, Raul D. S. G. Campilho, Andry M. Pinto | Faculty of Engineering, University of Porto (FEUP)；Centre for Robotics and Autonomous Systems - INESC TEC；Instituto Superior de Engenharia do Porto (ISEP)；funding from the European Union’s Horizon Europe research and innova- 2) Independent Wave Mitigation via DRL: A 3-RPU | 基于多模态Agentic AI与主动波浪补偿，实现无人机在海上平台鲁棒自主着陆。 | [#812](https://github.com/thinson/RS-PaperClaw/issues/812) |
| [20260630] Energy-Optimal Spatial Iterative Learning within a Virtual Tube | Min Chen, Lv Shuli, Mao Pengda, Cao Huixin, Hong Li, Quan Quan | School of Automation Science and Electrical Engineering, Beihang University, Beijing, China；Tianmushan Laboratory, Beihang University, Hangzhou | 提出虚拟管道内能量最优空间迭代学习方法，优化无人机轨迹规划。 | [#813](https://github.com/thinson/RS-PaperClaw/issues/813) |
| [20260630] AeroVerse-SatAgent: UAV-Satellite Collaborative Spatial Reasoning Inspired by the Dual Visual Pathway Theory of Cognitive Neuroscience | Zhang Wenyi, Yao Fanglong, Liu Youzhi, Hu Peng, Zhu Zhengqiu, Gao Chen, Sun Xian, Fu Kun | the Aerospace Information Research Institute, Chinese Academy of Sciences, Beijing, China；University of Chinese Academy of Sciences, Beijing, China；School of Electronic, Electrical and Communication Engineering, University of Chinese Academy of Sciences, Beijing, China；the Key Laboratory of Target Cognition and Application Technology (TCAT), Aerospace Information Research Institute, Chinese Academy of Sciences, Beijing, China (；School of Computer Science and Engineering, Beihang University, Beijing, China (；the National Key Laboratory of Digital Intelligent Modeling and Simulation, National University of Defense Technology, Changsha, Hunan Province, China (；the Beijing National Research Center for Information Science and Technology (BNRist), Tsinghua University, Beijing, China ( | 受认知神经科学双视觉通路启发，提出无人机-卫星协同空间推理框架AeroVerse-SatAgent。 | [#814](https://github.com/thinson/RS-PaperClaw/issues/814) |
| [20260630] Sensing for Reliable UAV Communication: Robust Trajectory and Resource Optimization in Low-Altitude Networks | Jiang Yifan, Wu Qingqing, Hui Hongxun, Chen Wen, Feng Wei, Shen Shanpu | Shanghai Jiao Tong University, Shanghai, China；State Key Laboratory of Internet of Things for Smart City, University of Macau, Macao, China (；Department of Electronic Engineering, Shanghai Jiao Tong University, Shanghai, China (；State Key Laboratory of Internet of Things for Smart City and Department of Electrical and Computer Engineering, University of Macau, Macao, China (；Department of Electronic Engineering, State Key Laboratory of Space Network and Communications, Tsinghua University, Beijing, China ( | 研究低空网络中感知辅助通信的鲁棒轨迹与资源优化，保障无人机可靠通信。 | [#815](https://github.com/thinson/RS-PaperClaw/issues/815) |
| [20260630] Reconfigurable wavelength-encoded stochastic illumination for active hyperspectral imaging | Chen Yi-Jing, Liu Bao-Lei, Dong Ze-Yuan, Zhao Zhi-Hao, Zhang Yi-Ying, Yu Chun-Min, Xu Zhi-Hua, Yu Yuan-Jin, Yang Zhao-Hua | School of Instrumentation Science and Optoelectronic Engineering, Beihang；University, Beijing 100191, China；Hangzhou International Innovation Institute, Beihang University, Hangzhou；Beihang University Hospital, Beihang University, Beijing 100191, China；School of Automation, Beijing Institute of Technology, Beijing 100081, China | 提出可重构波长编码随机照明方法，用于主动高光谱成像的压缩感知。 | [#816](https://github.com/thinson/RS-PaperClaw/issues/816) |
| [20260630] Diffusion-based 4D Trajectory Prediction and Distributed Control for UAV Swarms | Li Tianshun, Lu Hongliang, Li Haoang, Zheng Xinhu | The Hong Kong University of Science and Technology (Guangzhou), China；the Southern University of Science and Technology, China and MoSense Technologies, China | 基于扩散模型进行4D轨迹预测，并实现无人机集群的分布式控制。 | [#817](https://github.com/thinson/RS-PaperClaw/issues/817) |
| [20260630] FROST: Training-Free Few-Shot Segmentation with Frozen Features and Nonparametric Statistics | Park Junghwan | TelePIX | 提出FROST方法，利用冻结特征与非参数统计实现无需训练的少样本分割。 | [#818](https://github.com/thinson/RS-PaperClaw/issues/818) |
| [20260630] PiLoT v2: Pixel-to-Orthogonal Map Alignment for Free-view UAV Geo-localization | Liu Xinyi, Cheng Xiaoya, Wu Rouwan, Wang Zhaochen, Yan Shen, Zhang Maojun, Liu Yu | National University of Defense Technology | 提出PiLoT v2方法，实现无人机自由视角与正交地图的像素级对齐定位。 | [#819](https://github.com/thinson/RS-PaperClaw/issues/819) |
| [20260630] MultiUAV-Plat: An LLM-Oriented Platform, Benchmark and Framework for Multi-UAV Collaborative Task Planning | Zhang Sheng, Li Qinglin, Zang Yuechao, Huang Xueqin, Fu Yijia, Zhu Cheng | National Key Laboratory of Information Systems Engineering, National University of Defense Technology | 发布MultiUAV-Plat平台，面向大语言模型的多无人机协同任务规划基准与框架。 | [#820](https://github.com/thinson/RS-PaperClaw/issues/820) |
| [20260630] TerraDiT-$Ω$: Unified Spatial Control for Satellite Image Synthesis with Any Geospatial Primitive | Wei Brian, Sastry Srikumar, Cher Daniel, Xing Eric, Jacobs Nathan | Any Geospatial Primitive Brian Wei⋆, Srikumar Sastry⋆, Daniel Cher⋆, Eric Xing, and Nathan Jacobs Washington University in St | 提出TerraDiT-Ω模型，实现基于任意地理基元的卫星图像合成统一空间控制。 | [#821](https://github.com/thinson/RS-PaperClaw/issues/821) |
| [20260630] Dual Sparse Aggregation Transformer for Multispectral Object Detection | Wu Wencong, Zhang Xiuwei, Yin Hanlin, Zhang Hongxi, Zhang Yanning | School of Computer Science, Northwest- ern Polytechnical University, Xi’an, China (；School of Cybersecurity, North- For instance, Fang et al. [11] constructed a cross-modality western Polytechnical University, Xi’an, China (；School of Computer Science, the Shaanxi Provincial Key Laboratory of Speech range relationships and merge non-local information | 提出双稀疏聚合Transformer，用于多光谱目标检测的跨模态融合。 | [#822](https://github.com/thinson/RS-PaperClaw/issues/822) |
| [20260630] Rate-Splitting Multiple Access Enabled Probabilistic Semantic Communication in UAV Networks | Wang Sicheng, Zhang Tiankui, Gan Xu, Xu Wenjun | School of Information and Communication Engineering, Beijing University of Posts and Telecommunications, Beijing,, China (；Department of Electrical and Electronic Engineering, The University of Hong Kong, Hong Kong ( | 提出速率分割多址接入使能的概率语义通信，应用于无人机网络。 | [#823](https://github.com/thinson/RS-PaperClaw/issues/823) |

## 🔎 观察

- Agentic AI正从概念验证走向遥感垂直应用，如林业偏差标注与植物表型发现。
- 无人机研究从单一任务向多机协同、语义通信与能量优化等系统级问题深化。

---

Powered by OpenClaw🦞

---
