# Daily Reports

最近三天日报（最新在前）：

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

# [20260520](./202605/20260520.md)
## 📌 今日概况

今日共检索候选论文 13 篇；关键词+LLM 智能匹配遥感交叉论文 9 篇；最终纳入日报 9 篇。

今日遥感AI研究呈现三大趋势：扩散模型持续渗透图像修复与生成任务，多模态融合与基础模型成为热点，无人机检测与增量学习等应用问题受到关注。物理模型与深度学习的混合架构在森林参数反演中展现潜力。

## ✨ 今日亮点

- 扩散模型主导：从Landsat 7条带修复到SAR三维可控生成，扩散架构展现强大生成能力
- 多模态基础模型突破：SpectralEarth-FM首次将高光谱纳入多模态地球观测预训练框架
- 无人机检测双进展：多光谱数据集UAVNet-MS与RGB-红外专家路由方法同期出现

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260520] A Non-Reference Diffusion-Based Restoration Framework for Landsat 7 ETM+ SLC-off Imagery in Antarctica | Tang Leyue, Jonathan Louis Bamber, Qiao Gang, Kong Yuanhang | Center for Spatial Information Science and Sustainable；Bristol Glaciology Centre, School of observations or data from other sensors. One of the earliest；Center for Spatial Information Science and Sustainable shortly after the SLC failure, which estimates missing pixel；College of Surveying and Geo-Informatics, Tongji | 提出无参考扩散框架，无需辅助数据即可修复南极Landsat 7 ETM+ SLC-off影像条带缺失。 | [#584](https://github.com/thinson/RS-PaperClaw/issues/584) |
| [20260520] Vision Transformers and Convolutional Neural Networks for Land Use Scene Classification | Arun D. Kulkarni | University of Texas at Tyler | 系统对比Vision Transformer与CNN在土地利用场景分类中的性能表现与适用条件。 | [#585](https://github.com/thinson/RS-PaperClaw/issues/585) |
| [20260520] GeoDiff-SAR II: 3D-Driven Foundation Diffusion Models for SAR Generation via Decoupled Control | Wu Xuanting, Zhang Fan, Ma Fei, Liu Yingbing, Peng Lingxiao, Yin Qiang, Zhou Yongsheng | College of Information Science and Technology, Beijing University of Chemical Technology；Suzhou Aerospace Information Research Institute, Chinese Academy of Sciences | GeoDiff-SAR II通过解耦的几何-电磁条件控制，实现三维引导的SAR图像可控生成。 | [#586](https://github.com/thinson/RS-PaperClaw/issues/586) |
| [20260520] SpectralEarth-FM: Bringing Hyperspectral Imagery into Multimodal Earth Observation Pretraining | Nassim Ait Ali Braham, Banze Aaron, Conrad M. Albrecht, Mairal Julien, Chanussot Jocelyn, Xiao Xiang Zhu | Chair of Data Science in Earth Observation, Technical University of Munich；Remote Sensing Technology Institute, German Aerospace Center (DLR)；Department of Aerospace Engineering, University of the Bundeswehr Munich；LEAP, Columbia University；Munich Center for Machine Learning (MCML)；Univ. Grenoble Alpes, Inria, CNRS, Grenoble INP, LJK | SpectralEarth-FM构建首个融合高光谱的多模态地球观测基础模型预训练框架。 | [#587](https://github.com/thinson/RS-PaperClaw/issues/587) |
| [20260520] Hybrid Machine Learning Model for Forest Height Estimation from TanDEM-X and Landsat Data | Mansour Islam, Haensch Ronny, Hajnsek Irena, Papathanassiou Konstantinos | German Aerospace Center (DLR), Microwaves and Radar Institute, Wessling, Germany；ETH Zurich, Institute of Environmental Engineering, Zurich, Switzerland | 混合机器学习结合物理模型与TanDEM-X、Landsat数据，提升森林高度估算精度。 | [#588](https://github.com/thinson/RS-PaperClaw/issues/588) |
| [20260520] Towards UAV Detection in the Real World: A New Multispectral Dataset UAVNet-MS and a New Method | Luo Yihang, Chen Jun, Xiao Chao, Wang Yingqian, Li Zhaoxu, Ling Qiang, He Xu, Chen Nuo, Guo Gaowei, Li Hongge, Li Miao, Wang Longguang, Guo Yulan, Liu Li, An Wei, Chen Zhijie | the College of from precision mapping and logistics to surveillance；the Aviation University of Air Force；Sun Yat-sen University, China. Q. Ling, C. Xiao | 发布真实世界多光谱无人机检测数据集UAVNet-MS，配套提出专用检测方法。 | [#589](https://github.com/thinson/RS-PaperClaw/issues/589) |
| [20260520] STAR-IOD: Scale-decoupled Topology Alignment with Pseudo-label Refinement for Remote Sensing Incremental Object Detection | Zhang Yaoteng, Zhou Qing, Gao Junyu, Wang Qi | School of Computer Science, Northwestern Polytechnical University；School of Artificial Intelligence, OPtics and ElectroNics (iOPEN), Northwestern Polytechnical University | STAR-IOD通过尺度解耦拓扑对齐与伪标签精化，解决遥感增量目标检测中的尺度变化难题。 | [#590](https://github.com/thinson/RS-PaperClaw/issues/590) |
| [20260520] LER-YOLO: Reliability-Aware Expert Routing for Misaligned RGB-Infrared UAV Detection | Hou Liming, Peng Yueping, Hao Hexiang, Wang Ji, Zhang Xuekai, Tang Wei, Ye Zecong, Ying Xin, He Yubo | Engineering University of PAP；Unit Command Department, Officers College of PAP | LER-YOLO设计可靠性感知专家路由机制，实现未配准RGB-红外图像的无人机检测。 | [#591](https://github.com/thinson/RS-PaperClaw/issues/591) |
| [20260520] End-to-End Unmixing with Material Prompts for Hyperspectral Object Tracking | Han Xu, Mohammad Aminul Islam, Wang Lei, Long Zekun, Fu Guanmanyi, Cai Wangshu, Kuldip K. Paliwal, Zhou Jun | the School of pecially in challenging scenarios where appearance informa-；the School of Information and has attracted increasing attention, evolving from handcrafted；the School of Engi- issue, existing methods have primarily followed two research；the School of Environment and Science, Griffith gies | 端到端高光谱目标跟踪网络引入材料提示，联合优化光谱解混与跟踪任务。 | [#592](https://github.com/thinson/RS-PaperClaw/issues/592) |

## 🔎 观察

- 扩散模型正从自然图像向遥感专用任务快速迁移，生成式AI或重塑遥感数据补全与仿真范式
- 无人机检测研究热度攀升，多光谱与红外融合成为应对低可视条件的关键技术路线

---

Powered by OpenClaw🦞

---

# [20260519](./202605/20260519.md)
## 📌 今日概况

今日共检索候选论文 16 篇；关键词+LLM 智能匹配遥感交叉论文 14 篇；最终纳入日报 14 篇。

今日遥感AI研究呈现三大趋势：一是3D高斯溅射技术快速渗透至稀疏航空重建与跨视角合成领域；二是低空经济驱动无人机导航、协同规划与边缘智能研究爆发；三是Mamba、MoE、量子机器学习等新架构在遥感任务中加速验证，多模态统一生成与物理感知智能成为前沿焦点。

## ✨ 今日亮点

- 3D高斯溅射技术双突破：稀疏航空重建与卫星-地面跨视角合成并行推进
- 低空经济研究集群涌现：涵盖无人机导航、空地协同、边缘推理与数据生成
- 新架构遥感适配加速：Mamba视觉、MoE网络、量子机器学习集中验证

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260519] HaorFloodAlert: Deseasonalized ML Ensemble for 72-Hour Flood Prediction in Bangladesh Haor Wetlands | Salma Hoque Talukdar Koli, Fahima Haque Talukder Jely, Md. Samiul Alim, Md. Zakir Hossen | RTM Al-Kabir Technical University；North East University Bangladesh；Dhaka University of Engineering & Technology | 针对孟加拉Haor湿地季节性洪水，提出去季节化机器学习集成方法，结合SAR变化检测实现72小时洪涝预警。 | [#569](https://github.com/thinson/RS-PaperClaw/issues/569) |
| [20260519] MetaEarth-MM: Unified Multimodal Remote Sensing Image Generation with Scene-centered Joint Modeling | Yu Zhiping, Liu Chenyang, Cao Jinqi, Yang Qinzhe, Yu Siwei, Zou Zhengxia, Shi Zhenwei | the Department of Aerospace Intelligent Science and Tech- a unified generative model for diverse modalities and multi-；Shenyuan Honors College, Beihang University, Beijing construct such a unified model. Under this paradigm, pairwise | MetaEarth-MM构建以场景为中心的多模态遥感统一生成模型，支持跨模态图像翻译与联合建模。 | [#570](https://github.com/thinson/RS-PaperClaw/issues/570) |
| [20260519] Feed-Forward Gaussian Splatting from Sparse Aerial Views | Wu Dongli, Li Zhuoxiao, Hua Tongyan, Ren Yinrui, Wei Xiaobao, Qin Rongjun, Zhao Wufan | The Hong Kong University of Science and Technology (Guangzhou)；Peking University；The Ohio State University | 提出前馈式高斯溅射网络，从稀疏航空视角实现城市场景实时三维重建，无需逐场景优化。 | [#571](https://github.com/thinson/RS-PaperClaw/issues/571) |
| [20260519] StruMPL: Multi-task Dense Regression under Disjoint Partial Supervision and MNAR Labels | Reza M. Asiyabi, Juan Alberto Molina-Valero, The SEOSAW Partnership, Hancock Steven, Casey M. Ryan | School of Geosciences, University of Edinburgh；National Centre for Earth Observation (NCEO)；Department of Spatial Sciences, Faculty of Environmental Sciences, Czech University of Life Sciences Prague | StruMPL框架解决多任务密集回归中标签缺失非随机（MNAR）与部分监督 disjoint 难题，应用于森林生物量估算。 | [#572](https://github.com/thinson/RS-PaperClaw/issues/572) |
| [20260519] Deep Tech to Space: Space Data Centers and AI Revolution at the Edge | Weiss Jonas, Sagmeister Patricia, Gabriel Maiolini Capez, Verma Dinesh, Garello Roberto, Perotti Alberto, Lazaj Dawid, Musial Alicja, Nalepa Jakub, Morf Thomas, Schmatz Martin, Krawczyk Marek, Przeliorz Mateusz, Roche Kevin, Tayal Sagar, Lakshminarayanan Mahalakshmi, Longépé Nicolas, Mathieu Pierre-Philippe, Wijata Agata | IBM Research Europe；Politecnico di Torino；Vyoma GmbH；IBM Research；KP Labs；Silesian University of Technology；Meguro Space；IBM；ESA Φ-lab | 探讨近地轨道空间数据中心架构，将AI推理推向卫星边缘，支撑星座级实时数据处理。 | [#573](https://github.com/thinson/RS-PaperClaw/issues/573) |
| [20260519] GeoMamba: A Geometry-driven MambaVision Framework and Dataset for Fine-grained Optical-SAR Object Retrieval | Fang Tiantong, Wang Xiuwei, Xiao Jing, Zhou Wujie, Liao Liang, Wang Mi | Zhejiang University of Technology；Zhejiang University；Nanyang Technological University；Zhejiang Lab | GeoMamba融合几何驱动Mamba视觉与光学-SAR跨模态检索，构建细粒度遥感目标检索新框架及数据集。 | [#574](https://github.com/thinson/RS-PaperClaw/issues/574) |
| [20260519] KIO-planner: Attention-Guided Single-Stage Motion Planning with Dual Mapping for UAV Navigation | Yao Dexing, Li Haochen, Wei Junhao, Zhao Yifu, Li Yanxiao, Xu Jiahui, Hu Jinxuan, Tian Lele, Lu Baili, Li Zikun, Yang Xu, Im Sio-Kei, Yang Dingcheng, Wang Yapeng | Macao Polytechnic University；Zhongkai University of Agriculture and Engineering；South China Normal University；Nanchang University | KIO-planner采用注意力引导单阶段运动规划与双映射策略，实现无人机动力学约束下的高效导航。 | [#575](https://github.com/thinson/RS-PaperClaw/issues/575) |
| [20260519] Cross-View Splatter: Feed-Forward View Synthesis with Georeferenced Images | Turkulainen Matias, Krishnan Akshay, Aleotti Filippo, Sayed Mohamed, Garcia-Hernando Guillermo, Kannala Juho, Solin Arno, Brostow Gabriel, Turmukhambetov Daniyar | Aalto University；Georgia Tech；Niantic Spatial；University of Oulu；ELLIS Institute Finland；UCL | Cross-View Splatter实现地理参考图像的前馈新视角合成，打通卫星影像与地面级三维场景生成链路。 | [#576](https://github.com/thinson/RS-PaperClaw/issues/576) |
| [20260519] Component-Aware Structure-Preserving Style Transfer for Satellite Sim2Real 6D Pose Estimation | Zhang Yonglong | the School of Mechatronics Engineering, Harbin Institute of Technology, Harbin, China | 提出部件感知结构保持风格迁移方法，解决卫星Sim2Real域迁移中的6D位姿估计难题。 | [#577](https://github.com/thinson/RS-PaperClaw/issues/577) |
| [20260519] FlyMirage: A Fully Automated Generation Pipeline for Diverse and Scalable UAV Flight Data via Generative World Model | Li Jinhan, Huang Xijie, Wang Zhaoqi, Wang Yijin, Ge Weiqi, He Qiyi, Zhu Mo, Gao Fei, Wu Yuze, Zhou Xin | Zhejiang University；Hangzhou Dianzi University | FlyMirage基于生成式世界模型与3D高斯溅射，构建全自动多样化无人机飞行数据生成管线。 | [#578](https://github.com/thinson/RS-PaperClaw/issues/578) |
| [20260519] A novel YOLO26-MoE optimized by an LLM agent for insulator fault detection considering UAV images | João Pedro Matos-Carvalho, Laio Oriel Seman, Stefano Frizzo Stefenon, Mohammad Khalaf Mohammad Khreasat, Gabriel Villarrubia González | LASIGE, Faculdade de Ciências, Universidade de Lisboa；Department of Automation and Systems Engineering, Federal University of Santa Catarina；Instituto Superior de Engenharia de Lisboa, Instituto Politécnico de Lisboa；Expert Systems and Applications Lab, Faculty of Science, University of Salamanca | YOLO26-MoE结合大语言模型智能体优化，针对无人机图像实现绝缘子故障检测的专家混合架构。 | [#579](https://github.com/thinson/RS-PaperClaw/issues/579) |
| [20260519] Learning-Accelerated Optimization-based Trajectory Planning for Cooperative Aerial-Ground Handover Missions | Chen Jingshan, Yu Bochen, Ebel Henrik, Eberhard Peter | Institute of Engineering and Computational Mechanics, University of Stuttgart；Mechanical Engineering, LUT University | LSTM网络学习加速优化轨迹规划，为无人机-无人车协同空地交接任务提供热启动策略。 | [#580](https://github.com/thinson/RS-PaperClaw/issues/580) |
| [20260519] UAV-Assisted Cooperative Edge Inference for Low-Altitude Economy via MoE-based Hierarchical Deep Reinforcement Learning | Zhuang Wenhao, Mao Yuyi, Ivan Wang-Hei Ho, Yu Xianghao | the Department of Electrical and；the School of Computer Science and Engineering；the Department of Electrical Engineering, City University of less networks presents a fundamental conflict among compu- | 基于MoE分层深度强化学习的无人机协同边缘推理，服务低空经济场景下的计算-通信权衡。 | [#581](https://github.com/thinson/RS-PaperClaw/issues/581) |
| [20260519] Quantum Machine Learning for Cyber-Physical Anomaly Detection in Unmanned Aerial Vehicles: A Leakage-Free Evaluation with Proxy-Audited Feature Sets | Carlos A. Durán Paredes, Javier E. León Calderón, Nicolás Sánchez Perea, German Darío Díaz, Camilo Segura Quintero | Corporation for Aerospace Initiatives, Research and Innovation (CASIRI)；Universidad Nacional de Colombia；Universidad del Cauca | 量子机器学习用于无人机网络物理系统异常检测，提出无泄漏评估框架与代理审计特征集。 | [#582](https://github.com/thinson/RS-PaperClaw/issues/582) |

## 🔎 观察

- 3D高斯溅射正从神经渲染向遥感专用前馈重建演进，稀疏视角与地理参考约束成为关键适配方向
- 低空经济研究呈现全栈化特征：从数据生成、感知导航到边缘决策与量子安全，产学研协同密集

---

Powered by OpenClaw🦞

---
