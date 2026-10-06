# Daily Reports

最近三天日报（最新在前）：

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

# [20261001](./202610/20261001.md)
## 📌 今日概况

今日共检索候选论文 10 篇；关键词+LLM 智能匹配遥感交叉论文 3 篇；最终纳入日报 3 篇。

今日遥感AI研究呈现多维度协同优化趋势。无人机领域关注部分可观测条件下的在线规划与稀疏地面目标搜索，同时摄影测量参数对高精度测量的影响受到系统评估。卫星星座优化则引入两阶段方法与QUBO建模，兼顾经典优化与量子计算潜力。整体上，研究从单一算法创新转向任务规划、参数校准与星座设计的联合优化，强调实际部署中的精度与效率平衡。

## ✨ 今日亮点

- 无人机稀疏目标搜索引入在线规划与部分可观测建模
- 摄影测量处理参数对高精度测量影响获系统评估
- 卫星星座优化提出两阶段经典与QUBO混合方法

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20261001] Online Planning for Sparse Ground Target Search from a High-Altitude UAV under Partial Observability | Ashik E Rasul, Yoon Hyung-Jin | Department of Mechanical and Nuclear Engineering；Tennessee Technological University | 面向高空无人机部分可观测场景，提出稀疏地面目标在线搜索规划方法，结合PTZ相机主动搜索。 | [#1425](https://github.com/thinson/RS-PaperClaw/issues/1425) |
| [20261001] The Impact of Processing Parameters on High-Accuracy Measurements in UAV Photogrammetry | Ćwiąkała Paweł, Puniach Edyta, Pastucha Elżbieta, Gruszczyński Wojciech | The Mærsk Mc-Kinney Møller Institute, University of Southern Denmark, Campusvej 55, DK-5230 | 系统评估无人机摄影测量中处理参数对高精度测量的影响，涉及相机标定与光束法平差。 | [#1426](https://github.com/thinson/RS-PaperClaw/issues/1426) |
| [20261001] A two-stage approach to satellite constellation optimization: classical and QUBO formulations | Novara Carlo | Department of Electronics | 提出卫星星座优化两阶段方法，融合经典优化与QUBO建模，面向低轨对地观测覆盖。 | [#1427](https://github.com/thinson/RS-PaperClaw/issues/1427) |

## 🔎 观察

- 无人机研究正从感知算法转向任务级在线规划，部分可观测与稀疏目标成为关键约束。
- 卫星星座优化引入QUBO显示量子计算与遥感任务设计交叉，但落地仍需验证。

---

Powered by OpenClaw🦞

---
