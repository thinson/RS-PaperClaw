# Daily Reports

最近三天日报（最新在前）：

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

# [20261002](./202610/20261002.md)
## 📌 今日概况

今日共检索候选论文 3 篇；关键词+LLM 智能匹配遥感交叉论文 3 篇；最终纳入日报 3 篇。

今日论文聚焦遥感时序异常检测与智能体系统安全。森林监测方向利用Sentinel-1 SAR时序构建两阶段级联，实现近实时异常发现；海洋环境监测则强调星上自监督异常检测，以降低下传与算力压力。同时，LLM驱动的无人机集群研究关注感知-推理接口的对抗攻击与纵深防御，体现遥感AI从单一算法向系统级鲁棒性延伸。

## ✨ 今日亮点

- SAR时序两阶段级联用于近实时森林异常检测
- 星上自监督异常检测提升海洋监测效率
- LLM无人机集群感知-推理接口纵深防御

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20261002] A Two-Stage Cascade for Near-Real-Time Forest Anomaly Detection from Sentinel-1 SAR Time Series | Pann Thinzar Seint, Chhatkuli Subas, Atwood Bryan | DAI Labs, K.K. | 基于Sentinel-1 SAR时序构建两阶段级联，实现森林异常近实时检测。 | [#1429](https://github.com/thinson/RS-PaperClaw/issues/1429) |
| [20261002] Defense-in-Depth at the Perception-Reasoning Interface of LLM-Centric Agentic UAV Swarms | Homaei Mohammadhossein, Emami Yousef, Homayoun Sajad, Taheri Rahim, Zhou Hao, Miguel Gutierrez Gaitan, Wei Bo | University of Oulu；University of Turku；University of York；University of Houston；University of Melbourne；Northumbria University | 针对LLM无人机集群感知-推理接口，提出纵深防御以抵御对抗攻击。 | [#1430](https://github.com/thinson/RS-PaperClaw/issues/1430) |
| [20261002] On-Board Anomaly Detection for Efficient Marine Environmental Monitoring | Goudemant Thomas, Szywala Clotilde, Francesconi Benjamin, Aubrun Michelle, Bobichon Yves, Bellizzi Marjorie, Girard Adrien | Institut de Recherche Technologique Saint Exupéry；Current research often targets specific threats through methods like water quality assessment [3], [4], monitoring | 利用自监督学习在星上开展异常检测，提升海洋环境监测效率。 | [#1431](https://github.com/thinson/RS-PaperClaw/issues/1431) |

## 🔎 观察

- 遥感异常检测正从离线分析转向近实时与星上处理，以降低延迟和传输压力。
- LLM智能体进入遥感任务后，感知-推理接口安全成为系统鲁棒性的新焦点。

---

Powered by OpenClaw🦞

---
