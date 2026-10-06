# Daily Reports

最近三天日报（最新在前）：

# [20261005](./202610/20261005.md)
## 📌 今日概况

今日共检索候选论文 14 篇；关键词+LLM 智能匹配遥感交叉论文 6 篇；最终纳入日报 6 篇。

今日论文聚焦遥感基础模型与自监督表征学习，涵盖时序预测架构、公平性评估及多任务部分监督。SAR方向出现扩散模型与展开优化结合的重建方法，以及弱监督水体映射。图像恢复引入智能体与视觉语言模型应对复合退化。整体趋势显示，遥感AI正从单一任务向多任务、跨模态和鲁棒性评估演进，同时强调实际部署中的偏差与退化问题。

## ✨ 今日亮点

- 时序联合嵌入预测架构提升遥感表征学习能力
- 生物群系感知基准揭示遥感基础模型公平性缺陷
- 扩散模型与展开优化结合改进压缩SAR重建

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20261005] T-JEPA: A Temporal Joint-Embedding Predictive Architecture for Learning Better Remote Sensing Representations | Peng Bowen, Liu Li, Liu Yongxiang, Li Weijie, Zhou Jie, Liu Zhen | National University of Defense Technology, Changsha, China | 提出T-JEPA时序联合嵌入预测架构，利用时间信息学习更优遥感表征。 | [#1440](https://github.com/thinson/RS-PaperClaw/issues/1440) |
| [20261005] FairRSFM: A Biome-Aware Benchmark and Debiasing Framework for Remote Sensing Foundation Models | Md Aminur Hossain, Vaghasiya Omkumar, Rajeev Ranjan Dwivedi, Kurmi Vinod, Banerjee Biplab | Biplab Banerjee 2；Space Applications Centre, ISRO, Ahmedabad, India；Indian Institute of Technology Bombay, India；Indian Institute of Science Education and Research Bhopal | 构建生物群系感知基准与去偏框架，评估并提升遥感基础模型公平性。 | [#1441](https://github.com/thinson/RS-PaperClaw/issues/1441) |
| [20261005] Diffusion Meets Unrolling: Compressive SAR Image Reconstruction with Interleaved Learned Corrections | Pappas Odysseas, Andrew C. M. Austin, Mayo Perla, Golbabaee Mohammad, Achim Alin | VI Labs, School of Computer Science, University of Bristol；School of Electrical, Electronic, and Mechanical Engineering, University of Bristol；School of Engineering Mathematics and Technology, University of Bristol | 将扩散模型与展开优化交织，实现压缩SAR图像的高质量重建。 | [#1442](https://github.com/thinson/RS-PaperClaw/issues/1442) |
| [20261005] EORestore-Agent: Fidelity-Guided Agentic Restoration of Remote Sensing Images with Composite Degradations | Qi Heli, Zhou Zeqi, Yi Jingjun, Liu Kunyi, Lihe Ziyang, Wang Junjue, Yoshie Osamu, Yokoya Naoto | the Graduate School of Information, Production and Systems, Waseda University, Kitakyushu, Fukuoka 808-, Japan；the Graduate School of Frontier Sciences, The University of Tokyo, Kashiwa, Chiba 277-, Japan；the Informatics Institute, University of Amsterdam, Amsterdam XH, The Netherlands；Wuhan University, Wuhan, China | 提出保真度引导的智能体恢复框架，处理遥感图像复合退化。 | [#1443](https://github.com/thinson/RS-PaperClaw/issues/1443) |
| [20261005] Multi-Task Partially Supervised Learning for Super-Resolution and Semantic Segmentation on Earth Observation data | Lê Hoàng-Ân, Pham Minh-Tan, Lemai-Chenevier Solange, Greslou Daniel | Université Bretagne Sud, IRISA, UMR 6074, Vannes, France；Centre National d’Etudes Spatiales (CNES), Toulouse, France | 面向地球观测数据，研究超分辨率与语义分割的多任务部分监督学习。 | [#1444](https://github.com/thinson/RS-PaperClaw/issues/1444) |
| [20261005] Extending Dynamic World Surface Water Mapping to Sentinel-1 with AlphaEarth Embeddings | Mukherjee Rohit, Policelli Frederick, Tellman Beth, Chakraborty TC, Giezendanner Jonathan, Jonathan A. Sullivan, Sun Ning | Pacific Northwest National Laboratory, Richland, WA USA (；NASA Goddard Space Flight Center, Greenbelt, MD USA；Fujitsu Research of America, Santa Clara, CA USA；University of Wisconsin--Madison, Madison, WI USA | 利用AlphaEarth嵌入将动态世界地表水映射扩展至Sentinel-1。 | [#1445](https://github.com/thinson/RS-PaperClaw/issues/1445) |

## 🔎 观察

- 遥感基础模型研究正从性能提升转向公平性、鲁棒性等可信维度评估。
- 扩散模型与经典优化结合，成为SAR重建等逆问题的新兴技术路线。

---

Powered by OpenClaw🦞

---

# [20261004](./202610/20261004.md)
## 📌 今日概况

今日共检索候选论文 7 篇；关键词+LLM 智能匹配遥感交叉论文 3 篇；最终纳入日报 3 篇。

今日遥感AI研究呈现三条并行主线：一是面向遥感智能体的可靠性机制，通过工具观测验证抑制误差传播；二是低光无人机场景下的RGB-红外差分融合与方向车辆检测，强调可靠性条件学习；三是多源卫星数据分析与LLM报告生成的全流程自动化，覆盖地表温度与Landsat数据处理。整体看，研究从单纯提升感知精度转向系统级可靠性与自动化闭环，智能体与生成式方法加速融入遥感工作流。

## ✨ 今日亮点

- 遥感智能体引入工具观测验证，抑制误差传播提升可靠性
- RGB-红外差分学习用于低光无人机方向车辆检测
- LLM驱动多源卫星数据分析与自动报告生成框架

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20261004] RSure-Agent: Reliable Use of Tool Observations for Remote Sensing Agents | Liu Fuyuan, Liu Nayu, Yu Wenhao, Wang Peijin, Feng Yingchao, Yao Fanglong, Wan Liang, Feng Wei | School of Computer Science and Technology, Tianjin University, Tianjin, China (；the Key Laboratory of Target Cognition and Application Technology (TCAT), Aerospace Information Research Institute, Chinese Academy of Sciences, Beijing, China ( | 提出RSure-Agent，通过验证工具观测的可靠性来抑制遥感智能体中的误差传播。 | [#1436](https://github.com/thinson/RS-PaperClaw/issues/1436) |
| [20261004] ReDiffNet: Differential RGB-Infrared Learning for Low-Light UAV Oriented Vehicle Detection | Zhang Qifan, Zhou Ziran, Li Ruijie, Tang Jincheng, Wang Hao, Qiao Qihao, Wang Chunliu | Dalian Maritime University, Dalian, China；The Hong Kong University of Science and Technology (Guangzhou), Guangzhou, China；Hubei University of Economics, Wuhan, China | 提出ReDiffNet，以差分RGB-红外学习实现低光无人机场景下的方向车辆检测。 | [#1437](https://github.com/thinson/RS-PaperClaw/issues/1437) |
| [20261004] A Framework for Automated Multi-Source Satellite Data Analytics and LLM-Based Report Generation | Hind Yousif Alhammadi, Isam Mashhour Al Jawarneh | Department of Applied Physics and Astronomy, University of Sharjah, Sharjah, UAE；Department of Computer Science, University of Sharjah, P.O.Box | 构建多源卫星数据分析与LLM报告生成框架，支持地表温度与Landsat自动化处理。 | [#1438](https://github.com/thinson/RS-PaperClaw/issues/1438) |

## 🔎 观察

- 遥感智能体研究开始关注工具观测的可靠性验证，而非仅追求任务完成率。
- 低光无人机检测与多源自动化分析并行推进，显示场景驱动与流程驱动并重。

---

Powered by OpenClaw🦞

---

# [20261003](./202610/20261003.md)
## 📌 今日概况

今日共检索候选论文 2 篇；关键词+LLM 智能匹配遥感交叉论文 2 篇；最终纳入日报 2 篇。

今日两篇论文分别聚焦遥感开放词汇语义分割与无人机位姿估计。前者针对几何变换导致的特征流形失真，提出基于二面体群D4的特征自适应流形修复方法，以提升开放词汇分割鲁棒性。后者利用自监督DINOv2构建ViT模型，探索合成到真实的域适应，用于非合作无人机位姿估计。整体趋势显示，遥感与视觉基础模型的结合正从封闭类别向开放词汇、从理想数据向跨域场景延伸，几何先验与自监督表征成为应对域偏移的关键手段。

## ✨ 今日亮点

- 开放词汇分割引入几何变换流形修复，提升遥感特征鲁棒性。
- DINOv2自监督ViT用于非合作无人机位姿估计，缩小合成真实域差。
- 两篇工作均关注域偏移问题，分别从几何先验与自监督预训练切入。

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20261003] A Geometric-Transformation Feature-Adaptive Manifold Restoration Method for Open-Vocabulary Semantic Segmentation of Remote Sensing Images | Wang Jianzheng, Ni Huan, Niu Xiaonan, Hong Danfeng, Guan Haiyan | School of Remote Sensing and Geomatics Engineering, Nanjing University of Information Science and Technology, China；Nanjing Center, China Geological Survey；School of Automation, Southeast University | 提出几何变换特征自适应流形修复方法，利用D4群增强开放词汇遥感语义分割的鲁棒性。 | [#1433](https://github.com/thinson/RS-PaperClaw/issues/1433) |
| [20261003] Synthetic-to-Real ViT-Based Pose Estimation of a Noncooperative UAV | Srinivas Krishnanujam, Acharla Hanish, Agrawal Brij, Herrera Leonardo | sign Center, Department of Mechanical and Aerospace Engineering, Naval based on the self-supervised DINOv2 [11] and is trained；Postgraduate School, Monterey | 基于DINOv2的ViT位姿估计模型，通过合成到真实域适应实现非合作无人机姿态估计。 | [#1434](https://github.com/thinson/RS-PaperClaw/issues/1434) |

## 🔎 观察

- 遥感开放词汇分割开始关注几何变换引起的特征流形失真，D4群等先验被用于修复。
- 非合作无人机位姿估计借助自监督ViT与合成数据，域适应仍是落地关键瓶颈。

---

Powered by OpenClaw🦞

---
