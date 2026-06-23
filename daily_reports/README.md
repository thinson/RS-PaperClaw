# Daily Reports

最近三天日报（最新在前）：

# [20260620](./202606/20260620.md)
## 📌 今日概况

今日共检索候选论文 5 篇；关键词+LLM 智能匹配遥感交叉论文 5 篇；最终纳入日报 5 篇。

今日遥感AI研究聚焦于场景条件植被模拟、红外小目标检测、变化检测、开放词汇语义分割及灾害评估。多篇工作引入注意力机制、知识蒸馏与多智能体流水线，强调模型可解释性与场景适应性，推动遥感分析向精细化与智能化发展。

## ✨ 今日亮点

- 植被模拟引入场景条件地理空间世界模型
- 红外小目标检测结合去噪与知识蒸馏
- 开放词汇分割通过提示校准SAM 3

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260620] VegSim: A Geospatial World Model for Scenario-Conditioned Vegetation Simulation | Iele Irene, Elena Mulero Ayllón, Soda Paolo, Tortora Matteo | Università Campus Bio-Medico di Roma Università Campus Bio-Medico di Roma；Umeå University University of Genoa；∗ Also with Università Campus Bio-Medico di Roma | VegSim提出场景条件地理空间模型用于植被动态模拟。 | [#754](https://github.com/thinson/RS-PaperClaw/issues/754) |
| [20260620] Denoising-Enhanced Coarse-to-Fine Infrared Small Target Detection with Attention Prior-Guided Knowledge Distillation | Fang Houzhang, Huang Ruixuan, Chen Qiuhuan, Wang Xiaolin, Chang Yi, Yan Luxin | Xidian University, Xi’an, China；Huazhong University of Science and Technology, Wuhan, China | 去噪增强的粗到细红外小目标检测结合注意力先验知识蒸馏。 | [#755](https://github.com/thinson/RS-PaperClaw/issues/755) |
| [20260620] CoSA: Correlation-Guided Change Attention with Learnable Residual Gating for Remote Sensing Change Detection | Omar Abdirashid, Park Jonghyuk | Department of Data Science, Graduate School of Kookmin University | CoSA利用相关引导注意力和可学习残差门控进行遥感变化检测。 | [#756](https://github.com/thinson/RS-PaperClaw/issues/756) |
| [20260620] Prompt-Calibrated SAM 3 for Open-Vocabulary Remote Sensing Semantic Segmentation | Song Yanghui, Liu Nanqing, Yin Haonan, Gao Yingjie, Yang Chengfu, Ming Qi | the School of Information Science and Technology, Yunnan Normal University, Kunming, China；the School of Computer Science and Engineering, Beihang University, Beijing, China；the College of Computer Science, Beijing University of Technology, Beijing, China | 提示校准SAM 3实现遥感图像开放词汇语义分割。 | [#757](https://github.com/thinson/RS-PaperClaw/issues/757) |
| [20260620] RAPID: A Reproducible Multi-Agent Pipeline for Interpretable Disaster Damage Assessment from Satellite and Street-View Imagery | Yang Yifan, Gong Wenjing, Zhang Kaili, Zou Lei, Tu Zhengzhong, Li Hao, Li Zongrong, Ye Xinyue | Texas A&M University Texas A&M University Texas A&M University；College Station, Texas, USA College Station, Texas, USA College Station, Texas, USA；Texas A&M University Texas A&M University National University of Singapore；College Station, Texas, USA College Station, Texas, USA Singapore, Singapore；Texas A&M University The University of Alabama；College Station, Texas, USA Tuscaloosa, Alabama, USA | RAPID构建可解释多智能体流水线用于卫星与街景灾害评估。 | [#758](https://github.com/thinson/RS-PaperClaw/issues/758) |

## 🔎 观察

- 注意力机制与知识蒸馏成为提升遥感检测精度的主流技术路径。
- 多模态数据融合（卫星+街景）在灾害评估中展现应用潜力。

---

Powered by OpenClaw🦞

---

# [20260619](./202606/20260619.md)
## 📌 今日概况

今日共检索候选论文 0 篇；关键词+LLM 智能匹配遥感交叉论文 0 篇；最终纳入日报 0 篇。

当日未检索到符合条件并纳入日报的论文。

## 🔎 观察

- 当日无成功纳入论文，建议优先检查候选筛选结果与失败原因。
- 若连续出现空日报，应复核 arXiv 日期窗口、关键词配置与 LLM 筛选输出。

---

Powered by OpenClaw🦞

---

# [20260618](./202606/20260618.md)
## 📌 今日概况

今日共检索候选论文 11 篇；关键词+LLM 智能匹配遥感交叉论文 10 篇；最终纳入日报 10 篇。

今日遥感研究聚焦多模态数据融合与智能解译，涵盖SAR-光学数据集、LiDAR建筑提取、森林结构制图及无人机视觉导航。同时，多模态大语言模型的否定理解评估、开放词汇变化检测、高光谱红外辐射模拟等前沿方向亦有突破，体现了遥感AI向精细化、鲁棒化发展的趋势。

## ✨ 今日亮点

- SARLO-80发布全球首个80cm斜距SAR-光学多模态数据集
- PCFootprint提出大规模点云建筑矢量提取基准
- ReA-OVCD实现可靠性感知的开放词汇变化检测

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260618] SARLO-80: Worldwide Slant SAR Language Optic Dataset 80cm | Debuysère Solène, Trouvé Nicolas, Letheule Nathan, Colin Elise, Channing Georgia | DEMR-ONERA – The French Aerospace Lab, Université Paris-Saclay, Palaiseau, France；DTIS-ONERA – The French Aerospace Lab, Université Paris-Saclay, Palaiseau, France | SARLO-80数据集提供80cm分辨率斜距SAR与光学影像配对，支持多模态学习。 | [#742](https://github.com/thinson/RS-PaperClaw/issues/742) |
| [20260618] PCFootprint: A Large-Scale Dataset and Benchmark for Vectorized Building Footprint Extraction from Aerial LiDAR Point Clouds | Shen Haoyuan, Wang Kuihao, Wang Ruisheng, Liu Yujun | School of Architecture and Urban Planning, Shenzhen University, Shenzhen 518060, China | PCFootprint构建大规模航空LiDAR点云数据集，用于建筑足迹矢量提取。 | [#743](https://github.com/thinson/RS-PaperClaw/issues/743) |
| [20260618] Integrating national forest inventory, airborne lidar, and satellite imagery for wall-to-wall mapping of forest structure with computer vision | Luke J. Zachmann, David D. Diaz, Vincent A. Landau, Walden-Schreiner Chelsey, Chang Tony, Nathan E. Rutenbeck, Katharyn A. Duffy, Ndegwa Kiarie, Gros Andreas, Conway Scott, Bayes Guy | Vibrant Planet Public Benefit Corporation | 融合国家森林清查、机载LiDAR与卫星影像，实现森林结构全覆盖制图。 | [#744](https://github.com/thinson/RS-PaperClaw/issues/744) |
| [20260618] Evaluating and Enhancing Negation Comprehension in Remote Sensing MLLMs | Han Haochen, Wang Jue, Alex Jinpeng Wang, Liu Fangming | Peng Cheng Laboratory, Shenzhen, China；Tsinghua University, Beijing, China；Central South University, Changsha, China | 评估并增强遥感多模态大语言模型对否定语义的理解能力。 | [#745](https://github.com/thinson/RS-PaperClaw/issues/745) |
| [20260618] See-and-Reach: Precise Vision-Language Navigation for UAVs within the Field of View | Xue Fanfu, Yu En, Shen Yantian, Hu Zhikun, Wang Hongjun, Yang Yang, Wang Xindi, Sun Jiande | the School of Information Science and Engineering, Shandong University；En Yu is with the Faculty of Engineering and Information Technol-；ogy, University of Technology Sydney, Sydney, NSW, Australia (；Zhikun Hu is with the School of Computer Science and Technology, Shan- Specifically, we posit that the search stage prioritizes；dong University, Qingdao 266237, China (；Xindi Wang is with the School of Artificial Intelligence, Shandong Univer-；Jiande Sun is with the School of Computer Science and Artificial Intelli- see-and-reach stage, necessitates an entirely distinct suite；gence, Shandong Normal University, Jinan 250358, China, and also with the；Interdisciplinary Research Center of General Artificial Intelligence, Shandong；Normal University, Jinan 250358, China ( | See-and-Reach提出视场约束下无人机视觉语言导航方法。 | [#746](https://github.com/thinson/RS-PaperClaw/issues/746) |
| [20260618] Exploring the potential of AlphaEarth and TESSERA embeddings for Fine-scale Local Climate Zone Mapping: A case study across five cities in Switzerland | Htet Yamin Ko Ko, Atzberger Clement | International Space Science Institute, Bern, Switzerland；rural regions and there is an increasing risk of hospitalization and fatality amid urban | 对比AlphaEarth与TESSERA嵌入在瑞士城市局地气候区精细制图中的表现。 | [#747](https://github.com/thinson/RS-PaperClaw/issues/747) |
| [20260618] ReA-OVCD: Reliability-Aware Open-Vocabulary Change Detection via Semantic and Spatial Refinement | Zhu Hongming, Chen Huaji, Du Bowen, Liu Sicong, Liu Qin | the School of Computer Science and Technology, Tongji University, Shanghai , China；the College of Surveying and Geo-Informatics, Tongji University, Shanghai , China | ReA-OVCD通过语义与空间精炼实现可靠性感知的开放词汇变化检测。 | [#748](https://github.com/thinson/RS-PaperClaw/issues/748) |
| [20260618] SIMBA: ABidirectional Retrieval Forward Simulation Framework for Modeling FY-4A GIIRS Hyperspectral Infrared Radiances Toward NWP Applications | Shen Jingdong, Wang* Fu, Lu Qifeng, Huang Hao, Wu Chunqiang, Yang Chi, Liu Xiaofang | School of Computer Science and Engineering, Sichuan University of Science & Engineering, Yibin 644000；State Key Laboratory of Severe Weather Meteorological Science and Technology, CMA Earth System Modeling；and Prediction Centre and Key Laboratory of Earth System Modeling and Prediction, China Meteorological | SIMBA框架双向模拟FY-4A GIIRS高光谱红外辐射，支持数值天气预报。 | [#749](https://github.com/thinson/RS-PaperClaw/issues/749) |
| [20260618] Motor Angular Speed Preintegration for Multirotor UAV State Estimation | Petrlík Matěj, Novák Filip, Pěnička Robert, Saska Martin | Department of Cybernetics, Faculty of Electrical Engineering, Czech Technical University in Prague, 166 36, Prague 6, Czech Republic | 提出电机角速度预积分方法，提升多旋翼无人机状态估计精度。 | [#750](https://github.com/thinson/RS-PaperClaw/issues/750) |
| [20260618] VFACamou: View-Fused Adversarial Camouflage for Environment-Adaptive Physical Evasion | Yan Shihui, Liu Hu, Shi Junyu, Zhu Zihui, Zhou Ziqi, Song Yufei, Geng Youming, Li Minghui, Hu Shengshan | State Key Laboratory of Intelligent Vehicle Safety Technology；School of Cyber Science and Engineering, Huazhong University of Science and Technology；School of Computer Science and Technology, Huazhong University of Science and Technology；School of Software Engineering, Huazhong University of Science and Technology；Hebei Energy College of Vocation And Technology | VFACamou利用视图融合对抗伪装实现无人机侦察物理规避。 | [#751](https://github.com/thinson/RS-PaperClaw/issues/751) |

## 🔎 观察

- 多模态数据集与基准构建成为热点，推动遥感AI从算法创新向数据驱动演进。
- 无人机相关研究从导航、状态估计到对抗伪装，呈现系统化应用趋势。

---

Powered by OpenClaw🦞

---
