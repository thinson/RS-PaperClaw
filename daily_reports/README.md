# Daily Reports

最近三天日报（最新在前）：

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

# [20260929](./202609/20260929.md)
## 📌 今日概况

今日共检索候选论文 13 篇；关键词+LLM 智能匹配遥感交叉论文 8 篇；最终纳入日报 8 篇。

今日论文覆盖多模态感知、基础模型、星上处理与地物制图等方向。VesselBench-800K构建大规模多模态船舶感知基准，HyperSAM将可提示分割扩展至高光谱，Planetary Feature Fields探索可扩展地球表示。同时，星上数据缩减、多源建筑制图、像素级Transformer冠层高度回归及超高分VQA自蒸馏等研究，体现遥感AI向高效化、统一化与任务专用化并进的趋势。

## ✨ 今日亮点

- 大规模多模态船舶感知基准发布，覆盖检测、计数与密度估计
- 高光谱可提示基础模型HyperSAM，推动分割大模型跨模态适配
- 星上双时相建筑损毁评估，兼顾精度与数据缩减效率

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260929] VesselBench-800K: A Large-scale Perception Benchmark for Multimodal Vessel Detection, Counting, and Density Estimation | Hong Danfeng, Li Chenyu, Chanussot Jocelyn | School of Automation, Southeast University, Nanjing, China. (；Univ | 构建80万级多模态船舶感知基准，统一检测、计数与密度估计任务。 | [#1409](https://github.com/thinson/RS-PaperClaw/issues/1409) |
| [20260929] Embedded Bi-Temporal Building Damage Assessment for On-Board Data Reduction | Goudemant Thomas, Francesconi Benjamin, Bellizzi Marjorie, Dorise Adrien | IRT Saint Exupéry；CNES | 面向星上部署的双时相建筑损毁评估，用Siamese检测器实现数据缩减。 | [#1410](https://github.com/thinson/RS-PaperClaw/issues/1410) |
| [20260929] UniBuild: Unified Building Mapping From Multi-Source Optical Remote Sensing Imagery With Detail Decoding and Geometry Regularization | Huang Wei, Liu Chenying, Shi Yilei, Xiao Xiang Zhu | the Chair of Data Science in Earth Observation, Technical University of Munich, Munich, Germany; Chenying Liu and Xiao Xiang Zhu are also with Fig. 1 | 提出统一多源光学影像建筑制图框架，结合细节解码与几何正则化。 | [#1411](https://github.com/thinson/RS-PaperClaw/issues/1411) |
| [20260929] HyperSAM: A Promptable Foundation Model for Hyperspectral Remote Sensing | Pang Li, Wu Xinqiao, Yao Jing, Ghamisi Pedram, Zhou Jun, Chen Zhengchao, Meng Deyu, Cao Xiangyong | School of Mathematics and Statistics, Xi'an Jiaotong University, Xi'an, China (；the Faculty of Electronic and Information Engineering, Xi'an Jiaotong University, Xi'an, China (；State Key Laboratory of Remote Sensing and Digital Earth, Aerospace Information Research Institute, Chinese Academy of Sciences, Beijing, China (；Faculty of Electrical and Computer Engineering, University of Iceland, 101 Reykjavik, Iceland (；School of Information and Communication Technology, Griffith University, Nathan, QLD, Australia (；School of Computer Science and Technology, Xi'an Jiaotong University, Xi'an, China ( | 将可提示分割基础模型扩展至高光谱，引入数据合成与光谱适配。 | [#1412](https://github.com/thinson/RS-PaperClaw/issues/1412) |
| [20260929] Planetary Feature Fields are Scalable Earth Representations | Rao Arjun, Loeschcke Sebastian, Fuller Anthony, Corley Isaac, Lang Nico, Shelhamer Evan | University of British Columbia &；University of Copenhagen &；Carleton University；University of Copenhagen && Vector Institute；Vector Institute &&；University of British Columbia；&& Vector Institute | 提出行星特征场作为可扩展地球表示，探索神经场与数据压缩结合。 | [#1413](https://github.com/thinson/RS-PaperClaw/issues/1413) |
| [20260929] Pixel-Level Transformers in Remote Sensing: A Canopy Height Case Study | Ligensa Sven, Pauls Jan, Schrödter Karsten, Fayad Ibrahim, Gieseke Fabian | University of Münster University of Münster University of Münster；Laboratoire des Sciences du Climat et University of Münster | 以冠层高度为案例，系统评估像素级Transformer在遥感稠密回归中的表现。 | [#1414](https://github.com/thinson/RS-PaperClaw/issues/1414) |
| [20260929] RS-OPSD: Reliable Privileged On-Policy-Self-Distillation for Ultra-High-Resolution Remote Sensing VQA | Jiang Chengjie, Zhou Yunqi, Yan Jiafeng, Zhao Sihang, Yuan Chun, Li Jing | Tsinghua University；Zhejiang University；Central University of Finance and Economics；East China Normal University；Key Laboratory of Geographic Information Science | 面向超高分遥感VQA，提出可靠特权在线自蒸馏方法提升推理稳定性。 | [#1415](https://github.com/thinson/RS-PaperClaw/issues/1415) |
| [20260929] Cropland PAtteRNS: Parallel Dimensional Attention Networks and Attention to Dataset Disparity for Crop Segmentation in Satellite Imagery Time Series Data | Metcalfe Joseph, Sharifzadeh Sara, Caraffini Fabio | Department of Computer Science, Swansea University | 针对卫星时序作物分割，提出并行维度注意力网络并关注数据集差异。 | [#1416](https://github.com/thinson/RS-PaperClaw/issues/1416) |

## 🔎 观察

- 基础模型与可提示分割正从自然图像向高光谱、多模态遥感迁移，适配策略成为关键。
- 星上处理与数据缩减研究增多，反映遥感AI在轨部署对轻量化与实时性的迫切需求。

---

Powered by OpenClaw🦞

---

# [20260928](./202609/20260928.md)
## 📌 今日概况

今日共检索候选论文 14 篇；关键词+LLM 智能匹配遥感交叉论文 9 篇；最终纳入日报 9 篇。

今日论文呈现三条主线：一是面向星上/在轨场景的轻量化与协同推理，包括SAR Level-0原始数据直接分类、卫星-地面DNN分割与资源分配；二是遥感基础模型与迁移学习的适用边界，涉及冻结嵌入跨 wildfire 迁移失效问题；三是多模态与生成式方法向遥感任务渗透，如开放词汇分割、视频问答、稀疏视角3D高斯泼溅与高光谱跟踪。整体看，研究更强调物理约束、数据特性与部署可行性，而非单纯堆叠模型规模。

## ✨ 今日亮点

- 星上智能与协同推理成为热点，关注原始数据直接处理与资源受限部署。
- 迁移学习研究开始反思冻结嵌入的跨域失效，强调本地增益难以泛化。
- 多模态与生成式方法加速进入遥感，覆盖视频问答、3D重建与高光谱跟踪。

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260928] Stacked Intelligent Metasurface-Diffractive Deep Neural Networks for Onboard Terrain Classification from SAR Level-0 Raw Data | Liu Mengbing, Li Xin, An Jiancheng, Yuen Chau | School of Electrical and Electronics Engineering, Nanyang Technological University, Singapore (e-mails:; ) | 提出堆叠智能超表面与衍射深度神经网络，直接从SAR Level-0原始数据进行在轨地形分类。 | [#1388](https://github.com/thinson/RS-PaperClaw/issues/1388) |
| [20260928] Preference-Guided Adaptation for Open-Vocabulary Semantic Segmentation via Prompt Disagreement | Jang Hyun-Kurl, Kim Jihun, Yoon Kuk-Jin | Visual Intelligence Lab | 利用提示不一致性进行偏好引导自适应，提升开放词汇语义分割的跨域表现。 | [#1389](https://github.com/thinson/RS-PaperClaw/issues/1389) |
| [20260928] Joint DNN Partitioning and Resource Allocation for Satellite-Terrestrial Collaborative Inference Systems | Liang Wenyu, Fei Zesong, Liu Peng, Wang Xinyi, Zeng Ming | School of Information and Electronics, Beijing Institute of Technology, Beijing, China ( | 面向卫星-地面协同推理，联合优化DNN分割与资源分配以适配LEO卫星约束。 | [#1390](https://github.com/thinson/RS-PaperClaw/issues/1390) |
| [20260928] Temporal Modelling for Burn Scars on Sentinel-3 | Barco Luca, Arnaudo Edoardo, Bragagnolo Andrea, Rossi Claudio, Garza Paolo | Up funded by the Italian Space Agency and the Ministry of University and；Research - Contract No. 2024-5-E.0 - CUP No. I53 D24000060005 | 基于Sentinel-3 OLCI构建时序建模方法，用于火烧迹地语义分割与损伤评估。 | [#1391](https://github.com/thinson/RS-PaperClaw/issues/1391) |
| [20260928] When local gains fail to transfer: Frozen Earth-observation embeddings across wildfires | Stark Philipp, Sopasakis Alexandros, Hall Ola | Department of Human Geography Centre for Mathematical Sciences；Lund University Lund University；Department of Human Geography；Lund University | 发现冻结地球观测嵌入在跨wildfire任务中本地增益无法迁移，揭示迁移局限。 | [#1392](https://github.com/thinson/RS-PaperClaw/issues/1392) |
| [20260928] Spectral Super-Resolution using Spatial-Spectral Residual Operator Networks | Chin Seokhyun | California Institute of Technology | 提出空间-光谱残差算子网络，实现多光谱卫星影像的零样本光谱超分辨率。 | [#1395](https://github.com/thinson/RS-PaperClaw/issues/1395) |
| [20260928] ReVA: A Scene-Centric Dataset Beyond Repetition for Remote Sensing Video Question Answering | Yao Zhen, Wang Likai, Yang Yuming, Zheng Zhihao, Lang Bo, Tang Qiuyu, Sheng Jialu, Xu Jingqi, Yang Yuehai, Barker Jumal, Ying Xiaowen, Mooi Choo Chuah | Lehigh University；University of Southern California；Qualcomm AI Research | 发布场景中心遥感视频问答数据集ReVA，缓解重复样本并强化时空推理评测。 | [#1398](https://github.com/thinson/RS-PaperClaw/issues/1398) |
| [20260928] Remote Sensing Sparse-View 3D Gaussian Splatting via Depth Image-Based Rendering | Kang Jiaming, Zou Zhengxia, Shi Zhenwei | Beihang University | 结合深度图像渲染与3D高斯泼溅，改善遥感稀疏视角的新视角合成质量。 | [#1399](https://github.com/thinson/RS-PaperClaw/issues/1399) |
| [20260928] HyperDAM: Hyperspectral Distractor-Aware Memory with Amodal Expansion for SAM 3 Tracking | Yuzawa Ryoga, Takagi Tasuku | 原文作者栏未列出单位 | 为SAM 3跟踪引入高光谱干扰感知记忆与无模态扩展，提升高光谱视频跟踪鲁棒性。 | [#1405](https://github.com/thinson/RS-PaperClaw/issues/1405) |

## 🔎 观察

- 星上处理与协同推理研究正从算法精度转向原始数据、通信与算力约束下的系统级权衡。
- 迁移学习与基础模型应用出现反思信号：冻结特征并非通用，跨域评估需更严格。

---

Powered by OpenClaw🦞

---
