# Daily Reports

最近三天日报（最新在前）：

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

# [20260930](./202609/20260930.md)
## 📌 今日概况

今日共检索候选论文 15 篇；关键词+LLM 智能匹配遥感交叉论文 6 篇；最终纳入日报 6 篇。

今日论文聚焦遥感定位、计数、高程变化与高光谱处理等方向。卫星-地面定位通过几何语义约束BEV表示缓解歧义；遥感计数探索无需目标域训练的新范式；UAV摄影测量结合异方差深度学习估计垂直位移；高光谱领域涌现模型综述与跨传感器超分方法；城市区域识别则利用可见光影像与植被指数。整体趋势显示，跨域泛化、几何与语义融合、以及不确定性建模正成为遥感AI的重要关注点。

## ✨ 今日亮点

- 几何语义约束BEV学习，缓解卫星地面定位歧义。
- 源域训练目标域计数，无需目标数据的新范式。
- 异方差深度学习提升UAV垂直位移估计可靠性。

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260930] How to Reduce Localization Ambiguity? Geometry-Semantic Constrained BEV Representation Learning for Satellite-Ground Localization | Feng Junming, Xia Panwang, Wu Qiong, Lu Xudong, Jiao Zeyu, Lv Kun, Wu Zherong, Wan Yi, Ma Peifeng, Hsu Li-Ta, Zheng Zhi | The Hong Kong Polytechnic University, Hong Kong；Southern University of Science and Technology；Wuhan University, Wuhan, China；The Chinese University of Hong Kong, Hong Kong, China | 提出几何-语义约束的BEV表示学习，减少卫星-地面定位中的局部歧义。 | [#1418](https://github.com/thinson/RS-PaperClaw/issues/1418) |
| [20260930] COBICount: Separating Object and Background Responses for Remote Sensing Object Counting Without Training on Target Data | Zheng Junjing, Zhou Zhiyi, Yang Ningrui, Meng Hongying | School of International Studies, Chongqing University of Posts and Telecommunications, Chongqing, China, When training and deployment images differ in object；Brunel University London, Uxbridge UB8 3 PH, U.K. (；School of International Studies, Chongqing Uni- versity of Posts and Telecommunications, Chongqing, China；School of International Studies, Chongqing University of Posts and Telecommunications, Chongqing, China；Department of Electronic and Electri- cal Engineering, College of Engineering, Design and Physical Sciences, Brunel University of London, Uxbridge UB8 3 PH, U.K. ( | COBICount分离目标与背景响应，实现无需目标域训练的遥感目标计数。 | [#1419](https://github.com/thinson/RS-PaperClaw/issues/1419) |
| [20260930] Determining Vertical Displacement of Agricultural Areas Using UAV-Photogrammetry and a Heteroscedastic Deep Learning Model | Gruszczyński Wojciech, Puniach Edyta, Ćwiąkała Paweł, Matwij Wojciech | AGH University of Krakow, Faculty of Geo-Data Science, Geodesy, and Environmental Engineering | 结合UAV摄影测量与异方差深度学习模型，测定农业区域垂直位移。 | [#1420](https://github.com/thinson/RS-PaperClaw/issues/1420) |
| [20260930] Hyperspectral Image Models: Technical Report | Rachamalla Tanishq, Das Aryan, Kaushik Srishti, Swalpa Kumar Roy | Department of Information Technology；Siddhartha Academy of Higher Education；Department of Computer Science and Engineering；Vellore Institute of Technology；Department of Computer and Information Sciences；Indira Gandhi National Open University；Tezpur University | 综述高光谱图像模型，涵盖Mamba、ViT及光谱-空间CNN等技术。 | [#1421](https://github.com/thinson/RS-PaperClaw/issues/1421) |
| [20260930] Super-Resolving Unseen Hyperspectral Sensors at Any Scale via Spatial Operators | He Ji-Xuan, Zhuang Guohang, Junge Bo, Li Tingyi, Lingchen, Cai Miaomiao, Qiao Yanan, Liu Xiujin, Fang Junfeng | Xi'an Jiaotong University；Hefei University of Technology；National University of Singapore；University of Michigan | 利用空间算子实现跨传感器、任意尺度的高光谱图像超分辨率。 | [#1422](https://github.com/thinson/RS-PaperClaw/issues/1422) |
| [20260930] Recognition of Urbanized Areas in UAV-Derived Very-High-Resolution Visible-Light Imagery | Puniach Edyta, Gruszczyński Wojciech, Ćwiąkała Paweł, Strząbała Katarzyna, Pastucha Elżbieta | AGH University of Krakow, Faculty of Geo-Data Science, Geodesy, and Environmental Engineering, Mickiewicza 30, 30-059 Krakow, Poland；The Mærsk Mc-Kinney Møller Institute, University of Southern Denmark, Campusvej 55, DK-5230 Odense | 基于UAV可见光影像与植被指数，识别城市化区域。 | [#1423](https://github.com/thinson/RS-PaperClaw/issues/1423) |

## 🔎 观察

- 跨域泛化成为遥感AI热点，多篇工作探索无需目标域数据的迁移方法。
- 几何与语义约束、不确定性建模被用于提升定位与高程估计的可靠性。

---

Powered by OpenClaw🦞

---
