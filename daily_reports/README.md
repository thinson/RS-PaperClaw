# Daily Reports

最近三天日报（最新在前）：

# [20260721](./202607/20260721.md)
## 📌 今日概况

今日共检索候选论文 15 篇；关键词+LLM 智能匹配遥感交叉论文 10 篇；最终纳入日报 10 篇。

今日遥感AI研究聚焦于无人机（UAV）导航与目标检测两大方向。多篇工作探索了视觉-语言模型、事件相机、跨模态融合等新范式在UAV导航与弱小红外目标检测中的应用。同时，农业遥感领域涌现出基于自监督学习与深度学习的作物胁迫检测与作物间隙制图方法。此外，变化检测与地理定位研究也取得了语义鲁棒性与无GPS环境下的新进展。整体趋势显示，模型正从单一模态向多模态、从有监督向自监督/无训练范式演进。

## ✨ 今日亮点

- UAV导航研究引入测试时缩放与层级大语言模型新范式。
- 红外弱小目标检测与跨模态跟踪方法取得显著进展。
- 自监督学习在农业遥感作物胁迫检测中展现潜力。

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260721] No Training, Better Flights: Test-Time Scaled VLMs for UAV Navigation | Cheng Feinan, Xu Dongliang, Nong Wenli, Zhang Zhiheng, Liu Ang, Wang Tianyu, Yao Yue | Institution1；Institution1 address；Institution2；First line of institution2 address；Shandong University；China University of Petroleum (East China) | 提出无需训练的测试时缩放视觉语言模型用于无人机导航。 | [#938](https://github.com/thinson/RS-PaperClaw/issues/938) |
| [20260721] Gaze-DETR: Top-Down Guidance Through Priority Maps for Infrared Weak-Small UAV Detection with DETR | Liu Nian, Yang Yuxin, Lin Shubo, Zhang Sikui, Li Liang, Cai Boyu, Wang Yizheng, Hu Weiming, Gao Jin | State Key Laboratory of Multimodal Artificial Intelligence Systems, Institute of Automation, Chinese Academy of Sciences, Beijing, China；School of Advanced Interdisciplinary Sciences, University of Chinese Academy of Sciences, Beijing, China；School of Artificial Intelligence, University of Chinese Academy of Sciences, Beijing, China；the Beijing Key Laboratory of Super Intelligent Security of Multi-Modal Information, Institute of Automation, Chinese Academy of Sciences, Beijing, China；School of Information Science and Technology, ShanghaiTech University, Shanghai, China；the Beijing Institute of Basic Medical Sciences, Beijing, China | Gaze-DETR利用优先级图实现红外弱小无人机检测。 | [#939](https://github.com/thinson/RS-PaperClaw/issues/939) |
| [20260721] Learning Semantic-Robust Change Detection via Semantic-Invariant Self-Distillation | Qu Jiuhe, Liang Yingping, Fu Ying | Beijing Institute of Technology, Beijing, China | 通过语义不变自蒸馏学习语义鲁棒的变化检测方法。 | [#940](https://github.com/thinson/RS-PaperClaw/issues/940) |
| [20260721] NGPS: GPS-Denied Aerial Geo-Localization and 2.5D Reconstruction via Deep Satellite Image Matching and Multi-Rate Sensor Fusion | Sharma Sanket | Independent Researcher | 提出无GPS环境下基于卫星图像匹配的空中地理定位与重建。 | [#941](https://github.com/thinson/RS-PaperClaw/issues/941) |
| [20260721] STS-NET: Spatio-Temporal Stress Network for Self-Supervised Crop Stress Detection using Satellite Image Time Series | Dalal Pradeep, Ranjan Rajiv, Ghildiyal Sushil, Tamaskar Shashank, Goel Neeraj | Department of Computer Science and Engineering, Indian Institute of Technology Ropar, Rupnagar, India (；Department of Robotics and Autonomous Systems, Plaksha University, Mohali, India ( | STS-NET利用卫星时序影像自监督检测作物胁迫。 | [#942](https://github.com/thinson/RS-PaperClaw/issues/942) |
| [20260721] CGMap: A Geospatially Aware Deep Learning Framework for Crop Gap Mapping Using UAV | Sharma Karan, Ranjan Rajiv, Kumar Dinesh, Tamaskar Shashank | Robotics and Autonomous Systems, Plaksha University, Mohali, India | CGMap框架结合YOLOv8实现无人机影像作物间隙制图。 | [#943](https://github.com/thinson/RS-PaperClaw/issues/943) |
| [20260721] Cross-Modal UAV Object Tracking: State-Aware Representation Learning and A Unified Benchmark | Xiao Yun, Hong Zhihong, Jin Jiandong, Li Chenglong, Tang Jin, Hussain Amir | has emerged as a popular research field with broad practical #406；of Artificial Intelligence, Anhui University, Hefei 230601, China (；Laboratory of Multimodal Cognitive Computation, School of Computer；Science and Technology, Anhui University, Hefei 230601, China (；Amir Hussain is affiliated with School of Computing, Engineering and；the Built Environment, Edinburgh Napier University, Edinburgh EH10 5 DT modality and switch between modalities for real-time tracking | 提出跨模态无人机跟踪的状态感知表示学习与统一基准。 | [#944](https://github.com/thinson/RS-PaperClaw/issues/944) |
| [20260721] SkyEV: RGB-Event UAV detection and tracking dataset and baseline | Mandula Jakub, Heusinger Sebastian, Moosmann Julian, Vogt Christian, Magno Michele | As highlighted by recent European research, detecting UAVs near sensitive infrastructure, such as airports or other no-fly zones, has become a critical priority | 发布RGB-事件双模态无人机检测跟踪数据集与基线。 | [#945](https://github.com/thinson/RS-PaperClaw/issues/945) |
| [20260721] Confidence-Gated Vision-Only Heading Alignment for UAV-UGV Cooperative Systems | Ahmari Reza, Hemmati Vahid, Kebria Parham, Odeyomi Olusola, Roy Kaushik, Homaifar Abdollah | Department of Computer Science, North Carolina Agricultural and Technical State University, Greensboro, NC, USA；Department of Electrical and Computer Engineering, North Carolina Agricultural and Technical State University, Greensboro, NC, USA | 提出置信门控纯视觉航向对齐用于无人机-无人车协同。 | [#946](https://github.com/thinson/RS-PaperClaw/issues/946) |
| [20260721] Intelligent Multi-UAV Navigation in ITNTNs: A Hierarchical LLM Approach | Yan Zijiang, Zhou Hao, Jaafar Wael, Pei Jianhua, Wang Ping, Yanikomeroglu Halim, Tabassum Hina | York University, Toronto, ON, Canada；Samsung Research America, Toronto, ON, Canada；ÉTS, University of Quebec, Montréal, QC, Canada；Carleton University, Ottawa, ON, Canada | 采用层级大语言模型实现智能多无人机导航。 | [#947](https://github.com/thinson/RS-PaperClaw/issues/947) |

## 🔎 观察

- 无人机自主能力研究正从单一视觉向多模态与语言模型协同演进。
- 农业遥感中自监督与深度学习方法的结合有效降低了标注依赖。

---

Powered by OpenClaw🦞

---

# [20260720](./202607/20260720.md)
## 📌 今日概况

今日共检索候选论文 9 篇；关键词+LLM 智能匹配遥感交叉论文 7 篇；最终纳入日报 7 篇。

今日遥感AI研究聚焦于多源异构数据融合与实时智能控制。SAR领域利用深度学习实现暗船识别与吨位估计；量子光谱技术突破高光谱成像灵敏度；无人机控制与通信网络研究强调实时性与自适应性，包括自然语言接口、塑性恢复及多智能体协同；此外，ISAC成像与卫星农业预测也取得进展。

## ✨ 今日亮点

- SAR深度学习实现暗船识别与吨位估计
- 量子傅里叶光谱实现高灵敏高光谱成像
- 无人机实时控制与自适通信网络研究突出

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260720] SAR Vessel Detection and Gross Tonnage Estimation from Heterogeneous Datasets for Dark Vessel Identification | Paltrinieri Davide, Diecidue Andrea, Basla Roberto, Casciani Daniele, Fraternali Piero, Boracchi Giacomo | Politecnico di Milano | 利用异构SAR数据集深度学习检测暗船并估计总吨位 | [#930](https://github.com/thinson/RS-PaperClaw/issues/930) |
| [20260720] Scanless quantum Fourier-transform mid-infrared spectroscopy for rapid high-sensitivity hyperspectral mapping | Gattinger Paul, Heise Bettina, Andreas W. Schell, Duswald Kristina, Brandstetter Markus, Zorin Ivan | Research Center for Non-Destructive Testing, Science Park 2, Altenberger Str. 69；Division of Light-Matter-Interaction, Johannes Kepler University, Altenberger Str. 69 | 基于纠缠光子的无扫描量子中红外光谱实现快速高光谱成像 | [#931](https://github.com/thinson/RS-PaperClaw/issues/931) |
| [20260720] RT-SHCUA: Real-Time Self-Hosted Computer-Use Agent for UAV Control | Lu Di, Zhang Bo, Li Xiyuan, Liao Yongzhi, Dong Xuewen, Shen Yulong, Liu Zhiquan, Ma Jianfeng | School of Computer Science and Technology, Xidian University, Xi’an, Shaanxi, China；the Shaanxi Key Laboratory of Network and System Security, Xi'an, Shaanxi,, China；College of Cyber Security, Jinan University, Guangzhou, China；School of Cyber Engineering, Shaanxi Key Lab of Network and System Security, Xidian University, Xi’an, Shaanxi,, China | 提出实时自托管计算机代理实现自然语言控制无人机 | [#932](https://github.com/thinson/RS-PaperClaw/issues/932) |
| [20260720] PRIME: Plasticity Recovery in Multi-Agent Environments for UAV-Assisted Emergency Communication Networks | Qiu Wen, He Zhiqiang, Zhao Wei, Masui Hiroshi | Department of Information and Communication Engineering, Kitami Institute of Technology, Japan (；the Graduate School of Informatics and Engineering, University of Electro-Communications, Japan (；School of Computer Science and Technology, Anhui University of Technology, China ( | 多智能体强化学习恢复塑性以优化无人机应急通信网络 | [#933](https://github.com/thinson/RS-PaperClaw/issues/933) |
| [20260720] Massive MIMO-OFDM ISAC for Sparse ISAR Imaging: Joint Power and Subcarrier Allocation | Hamid Reza Hashempour, Li Yanjiao, Zhang Jie, Shin Hyundong, Hien Quoc Ngo | the Centre for Wireless Innovation (CWI), Queen’s University Belfast, BT3 9 DT Belfast, U.K. (；Department of Electronic Engineering, Kyung Hee University, Yongin-si, Gyeonggi-do, Republic of Korea；Institute of Engineering Technology, University of Science and Technology Beijing, Beijing, China (；Department of Electronics and Information Convergence Engineering, Kyung Hee University, Yongin-si, Gyeonggi-do, Republic of Korea ( | 大规模MIMO-OFDM ISAC系统联合优化功率与子载波实现稀疏ISAR成像 | [#934](https://github.com/thinson/RS-PaperClaw/issues/934) |
| [20260720] Polar Coordinate-based Differential Evolution for Moving Target Search Using Vision Sensor on Unmanned Aerial Vehicles | Thu Hang Khuat, Bui Duy-Nam, Thuy Ngan Duong, Manh Duong Phung | VNU University of Engineering and Technology, Vietnam National University, Hanoi, Vietnam；Department of Electrical Engineering, Ulsan National Institute of Science and Technology, Ulsan；College of Engineering and Computer Science and Smart Green Transformation Center (GREEN-X)；VinUniversity, Hanoi, Vietnam | 基于极坐标差分进化算法引导无人机视觉搜索移动目标 | [#935](https://github.com/thinson/RS-PaperClaw/issues/935) |
| [20260720] Early Yield Prediction for Sugar Beet Fields using Satellite Data -- Learnings from Specialized Vision Transformers | Vaeth Philipp, Bhumika Laxman Sadbhave, Dejon Denise, Schorcht Gunther, Gregorova Magda | Center for Artificial Intelligence and Robotics, Technical University of Applied Sciences Wuerzburg-Schweinfurt, Franz-Horn-Strasse 2, Wuerzburg, Germany；Bielefeld University, Universitaetsstrasse 25, Bielefeld, Germany | 利用专用视觉Transformer从卫星数据早期预测甜菜产量 | [#936](https://github.com/thinson/RS-PaperClaw/issues/936) |

## 🔎 观察

- SAR与深度学习结合在海洋监控中向多任务（检测+估计）发展
- 无人机研究从单一控制向多智能体协同与自然语言交互演进

---

Powered by OpenClaw🦞

---

# [20260719](./202607/20260719.md)
## 📌 今日概况

今日共检索候选论文 2 篇；关键词+LLM 智能匹配遥感交叉论文 1 篇；最终纳入日报 1 篇。

今日遥感AI研究聚焦于无人机视频理解，提出SkyVLaM多模态大语言模型，融合视频分割与时序感知机制，推动遥感领域从静态图像分析向动态视频理解演进，体现了多模态与时空建模的融合趋势。

## ✨ 今日亮点

- 多模态大模型用于无人机视频理解
- 提出时序感知机制提升视频分割精度
- 遥感AI从静态图像向动态视频演进

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260719] SkyVLaM: Multimodal Large Language Model for UAV Video Understanding in Remote Sensing | Jing Kaiwen, Jia Ruixu, Li Bingyao, Ou Ruizhe, Wu Ming, Zhang Chuang | Beijing University of Posts and Telecommunications, Beijing, China；Peking University, Beijing, China；Beijing Wuzi University, Beijing, China | SkyVLaM利用多模态大语言模型实现无人机遥感视频理解与分割。 | [#928](https://github.com/thinson/RS-PaperClaw/issues/928) |

## 🔎 观察

- 多模态大模型正加速渗透遥感视频分析领域
- 时序感知机制成为提升动态遥感理解的关键

---

Powered by OpenClaw🦞

---
