# Daily Reports

最近三天日报（最新在前）：

# [20260523](./202605/20260523.md)
## 📌 今日概况

今日共检索候选论文 10 篇；关键词+LLM 智能匹配遥感交叉论文 8 篇；最终纳入日报 8 篇。

今日遥感AI研究呈现多模态融合与模型可解释性并重的趋势。视觉-语言模型在遥感检索与分割任务中持续深化，知识蒸馏与域适应技术成为解决数据稀缺的主流路径。同时，物理一致性与科学对齐开始受到关注，预训练模型的跨模态迁移能力得到进一步挖掘。

## ✨ 今日亮点

- GRAIL框架实现卫星数据科学工作流的自然语言到代码自动翻译
- TC-Bench首次系统评估视觉基础模型的物理可解释性与科学对齐度
- DisDop提出域先验蒸馏策略，突破航拍开放词汇检测瓶颈

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260523] GRAIL: AI translation for scientists application workflow on satellite data | Shang Zhuocheng, Eldawy Ahmed | University of California, Riverside | GRAIL基于大语言模型构建卫星数据处理的自然语言编程接口，支持Apache Spark分布式计算工作流自动生成。 | [#605](https://github.com/thinson/RS-PaperClaw/issues/605) |
| [20260523] The Perception-Physics Paradox: Probing Scientific Alignment with TC-Bench | Yao Dingling, Polesello Andrea, Pervez Adeel, Muller Caroline, Locatello Francesco | CausalLearningAI | TC-Bench通过结构同构性分析揭示视觉基础模型感知能力与物理规律理解之间的悖论性差距。 | [#606](https://github.com/thinson/RS-PaperClaw/issues/606) |
| [20260523] Leveraging pretrained RGB denoisers for hyperspectral image restoration | Picone Daniele, Jouni Mohamad, Dalla-Mura Mauro | Univ. Grenoble Alpes, CNRS, Grenoble INP, GIPSA-Lab | 提出将预训练RGB去噪器迁移至高光谱图像复原的即插即用框架，通过光谱投影实现跨模态知识复用。 | [#607](https://github.com/thinson/RS-PaperClaw/issues/607) |
| [20260523] Analysis of Altitude-Dependent Electronic Conspicuity in Cellular-Connected UAVs | Md Sharif Hossen, Vijay K. Shah, Guvenc Ismail | North Carolina State University | 量化分析蜂窝网络连接无人机的海拔高度对电子可见性及小区间干扰的影响规律。 | [#608](https://github.com/thinson/RS-PaperClaw/issues/608) |
| [20260523] DisDop: Distillation with Domain Priors for Open-Vocabulary Aerial Object Detection | Xu Ruihao, Liu Yong, Tang Yansong, Bai Sule, Ye Xubing, Yu Bingyao, Guo Yutao, Lu Jiwen, Zhou Jie | Tsinghua Shenzhen International Graduate School, Tsinghua University；Tsinghua University | DisDop融合域先验知识与知识蒸馏，提升开放词汇航拍目标检测对新类别的泛化能力。 | [#609](https://github.com/thinson/RS-PaperClaw/issues/609) |
| [20260523] Image-Conditioned Instance Prompt Network for Referring Remote Sensing Image Segmentation | Ren Biaoyu, Wang Qingsheng, Xu Cun, Yang Dingkang, Wang Wenxuan | School of Computer Science, Northwestern Polytechnical University；College of Intelligent Robotics and Advanced Manufacturing, Fudan University；Shenzhen Research Institute of Northwestern Polytechnical University | 图像条件实例提示网络实现遥感图像的指代分割，强化跨模态实例级理解能力。 | [#610](https://github.com/thinson/RS-PaperClaw/issues/610) |
| [20260523] Coarse-to-Fine Domain Incremental Learning with Attentive Distillation for Mining Footprint Segmentation in Multispectral Imagery | Alif Tri Handoyo, Vincent C.S. Lee, Rizka Widyarini Purwanto, Alex M. Lechner, Kemp Deanna, Muhamad Risqi U. Saputra | Monash University；Northeastern University；The University of Queensland | 面向多光谱矿区足迹分割的粗到细域增量学习框架，采用注意力蒸馏缓解域漂移。 | [#611](https://github.com/thinson/RS-PaperClaw/issues/611) |
| [20260523] Benchmarking Composed Image Retrieval for Applied Earth Observation | Psomas Bill, Christopoulos Dionysis, Petropoulos Thanasis, Efthymiadis Nikos, Kakogeorgiou Ioannis, Chum Ondřej, Avrithis Yannis, Tolias Giorgos, Karantzalos Konstantinos | Visual Recognition Group, Department of Cybernetics, Czech Technical University in Prague；Remote Sensing Laboratory, School of Rural, Surveying and Geoinformatics Engineering, National Technical University of Athens；Institute of Informatics & Telecommunications, National Centre for Scientific Research "Demokritos"；Department of Informatics and Telecommunications, National and Kapodistrian University of Athens | 首个面向地球观测的组合图像检索基准测试，系统评估视觉-语言模型的复杂查询理解能力。 | [#612](https://github.com/thinson/RS-PaperClaw/issues/612) |

## 🔎 观察

- 视觉-语言模型正从通用场景向遥感专用化演进，但科学任务所需的物理可解释性仍是明显短板
- 知识蒸馏与域适应技术的密集出现，反映出遥感数据标注成本高、分布差异大的结构性困境

---

Powered by OpenClaw🦞

---

# [20260522](./202605/20260522.md)
## 📌 今日概况

今日共检索候选论文 7 篇；关键词+LLM 智能匹配遥感交叉论文 1 篇；最终纳入日报 1 篇。

今日遥感AI研究聚焦语言-图像预训练在目标检测中的创新应用。清华大学团队提出结构化属性对齐框架，通过引入遥感对象的多粒度语义描述与保形预测机制，提升细粒度检测的可靠性，反映领域正从通用视觉模型向遥感专用语义理解深化。

## ✨ 今日亮点

- 结构化属性语言-图像预训练，突破遥感目标细粒度语义对齐瓶颈
- 融合保形预测机制，为检测置信度提供理论保证
- 清华-中科院联合团队推动遥感专用视觉语言模型发展

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260522] SLIP-RS: Structured-Attribute Language-Image Pre-Training for Remote Sensing Object Detection | Wang Chenxu, Li Yuxuan, Li Yunheng, Li Xiang, Xia Jingyuan, Hou Qibin | Tsinghua University；Chinese Academy of Sciences | SLIP-RS提出结构化属性语言-图像预训练框架，通过多粒度语义描述与保形预测提升遥感目标检测的细粒度理解与可靠性。 | [#603](https://github.com/thinson/RS-PaperClaw/issues/603) |

## 🔎 观察

- 遥感目标检测正从纯视觉特征转向视觉-语言联合表征，属性级语义对齐成为新方向
- 保形预测等不确定性量化技术引入，标志遥感AI从追求精度向可信决策演进

---

Powered by OpenClaw🦞

---

# [20260521](./202605/20260521.md)
## 📌 今日概况

今日共检索候选论文 12 篇；关键词+LLM 智能匹配遥感交叉论文 8 篇；最终纳入日报 8 篇。

今日遥感AI研究聚焦无人机智能感知与三维地物分类两大主线。无人机检测与控制持续深化，涉及运动解耦、视觉伺服、通感一体化等关键技术；多光谱LiDAR与深度学习结合推动三维土地利用分类发展；生成式模型与高斯溅射技术为遥感超分辨率重建提供新路径。

## ✨ 今日亮点

- 无人机检测领域提出双区间运动线索解耦方法，分离自身运动与目标动态
- 通感一体化(ISAC)成为热点，两篇论文分别探索能效优化与多模态协同感知
- 多光谱LiDAR结合Point Transformer推动三维土地利用分类技术演进

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260521] Decoupling Ego-Motion from Target Dynamics via Dual-Interval Motion Cues for UAV Detection | Wang Liuyang, Zhang Feitian | the Robotics and Control Laboratory, Department of Robotics, School of Advanced Manufacturing and Robotics；the State Key Laboratory of Turbulence and Complex Systems, Peking University, Beijing, , China | 通过双区间运动线索解耦自身运动与目标动态，提升无人机视频目标检测性能。 | [#594](https://github.com/thinson/RS-PaperClaw/issues/594) |
| [20260521] UAV-based Energy-Efficient Data Collection in Smart Grids with ISAC QoS Guarantees | Xie Yibin, Zhao Jin, Dey Indrakshi, Marchetti Nicola | Department of Electronic and Electrical Engineering, Trinity College Dublin；Walton Institute, South East Technological University | 设计满足ISAC服务质量约束的无人机能效数据采集方案，服务于智能电网应用。 | [#595](https://github.com/thinson/RS-PaperClaw/issues/595) |
| [20260521] Terminal Constraint Model Predictive Control for Image-Based Visual Servoing of UAVs with Kalman Filter-Based Moment Loss Compensation | Wang X., Cao Y., W. L. W. Leong, Y. R. Tan, Huang S., S. H. R. Teo, Xiang C. | College of Design and Engineering, National University of Singapore | 融合终端约束模型预测控制与卡尔曼滤波矩损失补偿，实现无人机图像视觉伺服。 | [#596](https://github.com/thinson/RS-PaperClaw/issues/596) |
| [20260521] 3D LULC classification using multispectral LiDAR and deep learning: current and prospective schemes | Takhtkeshha Narges, Rizaldy Aldino, Hollaus Markus, Hyyppä Juha, Remondino Fabio, Mandlburger Gottfried | 3D Optical Metrology (3DOM) Unit, Bruno Kessler Foundation (FBK)；Department of Geodesy and Geoinformation, TU Wien；Helmholtz-Zentrum Dresden-Rossendorf (HZDR), Helmholtz Institute Freiberg for Resource Technology (HIF)；Freie Universität Berlin, Remote Sensing and Geoinformatics；Department of Remote Sensing and Photogrammetry, Finnish Geospatial Research Institute FGI, The National Land Survey of Finland | 系统综述多光谱LiDAR与深度学习在三维土地利用分类中的现状与发展方向。 | [#597](https://github.com/thinson/RS-PaperClaw/issues/597) |
| [20260521] Impact of Atmospheric Turbulence and Pointing Error on Earth Observation | Sánchez-de-Miguel Celia, Antonio M. Mercado-Martínez, Soret Beatriz, Jurado-Navas Antonio, Castillo-Vázquez Miguel | TELMA, University of Malaga | 量化分析大气湍流与指向误差对地观测图像退化的影响机制。 | [#598](https://github.com/thinson/RS-PaperClaw/issues/598) |
| [20260521] Flow-based Gaussian Splatting for Continuous-Scale Remote Sensing Image Super-Resolution | Mo Jiangwei, Lu Xi, Wu Hanlin | the School of Information Science and Technol- We then learn a conditional flow transport from noise to this | 基于流匹配的高斯溅射方法实现连续尺度遥感图像超分辨率重建。 | [#599](https://github.com/thinson/RS-PaperClaw/issues/599) |
| [20260521] A Camera-Cooperative ISAC Framework for Multimodal Non-Cooperative UAVs Sensing | Wu Wenfeng, Xiang Luping, Yang Kun | the State Key Laboratory of Novel Software Technology, Nanjing University, Nanjing, , China, Institute of Intelligent Networks and Communications | 构建相机协同通感一体化框架，实现多模态非合作无人机感知与波束跟踪。 | [#600](https://github.com/thinson/RS-PaperClaw/issues/600) |
| [20260521] Non-Contact Vibration-Based Damage Detection of Civil Structures Using a Cost-Effective Autonomous UAV | Becerril Javier, Vargas Maximiliano, Herrera Jennifer, Gutierrez Joanna, Rios Jorge, Amjadian Mohsen, Tarawneh Constantine, Yang Jinghao, Lu Qi | Department of Computer Science, The University of Texas at Rio Grande Valley (UTRGV), Edinburg, TX, USA.；Department of Electrical and Computer Engineering at UTRGV. | 开发低成本自主无人机系统，基于非接触振动分析实现土木工程结构损伤检测。 | [#601](https://github.com/thinson/RS-PaperClaw/issues/601) |

## 🔎 观察

- ISAC技术正从通信与雷达分离架构向深度融合演进，无人机作为移动节点成为关键载体。
- 三维点云语义分割从RGB点云向多光谱LiDAR扩展，光谱-几何联合特征学习将成为重点。

---

Powered by OpenClaw🦞

---
