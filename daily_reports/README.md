# Daily Reports

最近三天日报（最新在前）：

# [20260810](./202608/20260810.md)
## 📌 今日概况

今日共检索候选论文 14 篇；关键词+LLM 智能匹配遥感交叉论文 7 篇；最终纳入日报 7 篇。

今日遥感AI研究聚焦于无人机系统设计、作物制图基准、渔船监测、跨视角地理定位、红外图像超分辨率、语义分割掩膜质量审计及建筑足迹验证。趋势显示，深度学习与系统工程方法深度融合，强调数据质量评估与多源数据应用，推动遥感智能解译向精细化、实用化发展。

## ✨ 今日亮点

- 无人机系统设计引入SysML框架，强化模型驱动。
- SwissCrop25提供多年作物制图基准，促进时序分析。
- 夜光影像结合YOLO11提升渔船监测精度。

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260810] Model-Based Systems Engineering Framework for SysML-Driven Design of Autonomous UAVs | Angadi Deekshitha, Budda Naveena, Agarwal Vikas, Samshad Mohamed, Bharath Kumar Suryadevara, Kemsaram Narsimlu | AIR Lab, UAVs Group, Autonomous Robotics Systems Limited, Hyderabad, India；Department of Microelectronics and VLSI Design, University of Hyderabad；Department of IoT, Ideabytes Software India Private Limited, Hyderabad, India；School of Computer Science, Georgia Institute of Technology, Atlanta, USA；Department of Electrical Engineering, Indian Institute of Technology, Kanpur；Department of System Engineering, Akkodis AS&D GmbH, Bremen, Germany；Department of Artificial Intelligence, Universiti Malaya, Kuala Lumpur, Malaysia | 提出基于SysML的MBSE框架，用于自主无人机系统架构设计。 | [#1076](https://github.com/thinson/RS-PaperClaw/issues/1076) |
| [20260810] SwissCrop25: A National Multi-Year Benchmark for Operational Crop Mapping | Lauber Thomas, Mehmet Ozgur Turkoglu, Ledain Sélène, Aasen Helge | Earth Observation of Agroecosystems Team, Agroscope | 发布瑞士全国多年作物制图基准数据集SwissCrop25，支持时序分析。 | [#1077](https://github.com/thinson/RS-PaperClaw/issues/1077) |
| [20260810] Deep Learning based Detection of Fishing Vessels and Fishing Monitoring using Nightlight Images | Mohanty Shantakar, Prasun Kumar Gupta, Raian Vargas Maretto | Indian Institute of Remote Sensing, ISRO, Dehradun, India；University of Twente, Faculty of Geo-Information Science and Earth | 利用SDGSAT-1夜光影像和YOLO11深度学习检测渔船，监测渔业活动。 | [#1078](https://github.com/thinson/RS-PaperClaw/issues/1078) |
| [20260810] Warp-free Cross-view Geo-localization via Feature-space Consensus Mining | Song Zhuo, Xu Lian, Jiang Runqing, Zhang Yongjian, Li Kunhong, Zhang Ye, Guo Yulan | Sun Yat-sen University, Shenzhen, China；University of Western Australia, Perth, Australia | 通过特征空间共识挖掘实现无变形跨视角地理定位，提升视角不变性。 | [#1079](https://github.com/thinson/RS-PaperClaw/issues/1079) |
| [20260810] OGG-FR: Orthogonal Gradient Gaming and Frequency Rectification for Unmanned Aerial Vehicle Infrared Image Super-Resolution | Huang Yongsong, Wang Qingzhong, Liu Xiaofeng, Miyazaki Tomo, Fan Yaohou, Omachi Shinichiro | Tohoku University；Yale University | 提出正交梯度博弈与频率校正方法，增强无人机红外图像超分辨率。 | [#1080](https://github.com/thinson/RS-PaperClaw/issues/1080) |
| [20260810] Contrastive Mask Fidelity: Reference-Free Auditing of Ground-Truth Masks in Remote Sensing Semantic Segmentation | Cao Shuaishuai, Peng Shuwei, Tang Meng, Huang Min, Wang Youjin, Chen Jie, Ouyang Jing, Zhai Zhiwei | Central South University；University of Chinese Academy of Sciences；Aberystwyth University；Jiangxi Normal University；Renmin University of China；BGI Research | 设计对比掩膜保真度指标，无需参考即可审计遥感分割标注质量。 | [#1081](https://github.com/thinson/RS-PaperClaw/issues/1081) |
| [20260810] GeoAI-based post-segmentation quality validation of building footprints via spatial feature engineering | Shah Imran Ahsan Chowdhury, Kazi Jihadur Rashid, Rajsree Das Tuli, Saha Rahul, Ahammad Bulbul | Department of Computer Science and Engineering；Jahangirnagar University；Department of Geography；Florida State University；Department of Geography and Environmental Sustainability；University of Oklahoma | 结合GeoAI与空间特征工程，对建筑足迹分割结果进行后验证。 | [#1082](https://github.com/thinson/RS-PaperClaw/issues/1082) |

## 🔎 观察

- 研究侧重数据质量与验证，如掩膜审计和足迹验证，反映对标注可靠性的关注。
- 多篇结合无人机与深度学习，应用场景向动态监测和精细农业延伸。

---

Powered by OpenClaw🦞

---

# [20260809](./202608/20260809.md)
## 📌 今日概况

今日共检索候选论文 2 篇；关键词+LLM 智能匹配遥感交叉论文 1 篇；最终纳入日报 1 篇。

今日遥感AI研究聚焦于无人机集群在间歇性连接条件下的可靠协同侦察。核心趋势是利用生成式预测与潜在状态估计，以应对通信受限环境下的感知不确定性，提升多机系统的鲁棒性与自主性。该方向融合了多智能体协同、深度学习与状态推理，为复杂动态场景下的遥感数据获取与融合提供了新思路。

## ✨ 今日亮点

- 提出潜在语义状态估计方法，增强无人机集群在弱连接下的协同可靠性。
- 结合生成式预测，应对间歇性通信导致的感知数据缺失问题。
- 研究聚焦于协同侦察场景，提升多机系统在复杂环境中的自主决策能力。

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260809] Latent Semantic State Estimation for Reliable Swarming of UAVs under Intermittent Connectivity | Paris A. Karakasis, Saad Walid | Institute for Advanced Computing and Bradley Dept. of Electrical and Computer Engineering | 提出潜在语义状态估计框架，用于间歇性连接下无人机集群的可靠协同侦察。 | [#1074](https://github.com/thinson/RS-PaperClaw/issues/1074) |

## 🔎 观察

- 间歇性连接成为多机协同遥感的核心约束，推动状态估计向生成式与潜在语义方向演进。
- 研究侧重算法鲁棒性而非硬件改进，表明软件层面补偿通信缺陷是当前技术突破口。

---

Powered by OpenClaw🦞

---

# [20260808](./202608/20260808.md)
## 📌 今日概况

今日共检索候选论文 3 篇；关键词+LLM 智能匹配遥感交叉论文 2 篇；最终纳入日报 2 篇。

今日遥感AI研究聚焦于气象预测与视觉基础模型两大方向。热带气旋预测引入潜空间修正流模型，结合卫星影像与大气场数据，提升生成式预测精度；变化检测领域则提出AdaDINO，通过冻结DINO骨干的配对感知适配，实现高效双时相分析。两项工作均强调对现有深度学习架构的优化，以应对遥感数据的时空复杂性，推动灾害监测与地表动态识别的智能化发展。

## ✨ 今日亮点

- 潜空间修正流提升热带气旋预测精度
- 冻结DINO适配实现高效变化检测
- 遥感AI聚焦生成模型与基础模型优化

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260808] Tropical Cyclone Forecasting via Latent Rectified Flow using Satellite Imagery and Atmospheric Fields | Zannat Meheru, Sk. Md. Masudul Ahsan | Department of Computer Science and Engineering；Khulna University of Engineering \& Technology | 提出潜空间修正流模型，融合卫星影像与大气场预测热带气旋 | [#1071](https://github.com/thinson/RS-PaperClaw/issues/1071) |
| [20260808] AdaDINO: Pair-Aware In-Backbone Adaptation of Frozen DINO for Efficient Remote Sensing Change Detection | Zhang Xu, Li Xinqing, Xie Jianpeng, Zhu Zeshuai, He Xin, Liu Yun | VCIP, College of Computer Science, Nankai University；School of Computer Science and Engineering, Tianjin University of Technology；Academy for Advanced Interdisciplinary Studies, Nankai University；Nankai International Advanced Research Institute, Shenzhen Futian | AdaDINO在冻结DINO骨干中引入配对感知适配，提升变化检测效率 | [#1072](https://github.com/thinson/RS-PaperClaw/issues/1072) |

## 🔎 观察

- 生成式模型在气象预测中应用渐增，但需平衡计算成本与精度
- 基础模型适配策略趋向轻量化，强调冻结骨干与任务特定模块结合

---

Powered by OpenClaw🦞

---
