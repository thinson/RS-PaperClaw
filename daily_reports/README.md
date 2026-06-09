# Daily Reports

最近三天日报（最新在前）：

# [20260607](./202606/20260607.md)
## 📌 今日概况

今日共检索候选论文 4 篇；关键词+LLM 智能匹配遥感交叉论文 1 篇；最终纳入日报 1 篇。

今日遥感AI研究聚焦于超分辨率任务，提出一种结合N-Gram上下文与混合专家模型的高效方法。该方法通过轻量级Transformer架构，在保持较低计算成本的同时提升遥感图像重建质量，体现了当前遥感领域对高效、高精度模型设计的持续关注。

## ✨ 今日亮点

- 提出N-Gram上下文与混合专家模型结合的遥感超分辨率方法
- 在保持低计算成本下提升遥感图像重建质量
- 轻量级Transformer架构应用于遥感超分辨率任务

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260607] NGram-MoSE: Efficient Remote Sensing Super-Resolution via N-Gram Context and Mixture-of-Experts | Huang Yun-Hsuan, Bui Trong-An, Chuang Chih-Hung | Institute of Aerospace and Systems Engineering, National Taipei University of Technology, Taipei City, Taiwan | 提出NGram-MoSE方法，结合N-Gram上下文与混合专家模型实现高效遥感超分辨率。 | [#688](https://github.com/thinson/RS-PaperClaw/issues/688) |

## 🔎 观察

- 遥感超分辨率研究正从单纯追求精度转向效率与性能的平衡
- 混合专家模型在遥感任务中的应用显示出提升模型适应性的潜力

---

Powered by OpenClaw🦞

---

# [20260606](./202606/20260606.md)
## 📌 今日概况

今日共检索候选论文 6 篇；关键词+LLM 智能匹配遥感交叉论文 5 篇；最终纳入日报 5 篇。

今日研究聚焦于遥感与地理空间智能的交叉创新，涵盖大气校正、地理定位、三维重建及生态监测。Transformer与图神经网络成为主流方法，分别用于高光谱大气补偿和时序地理定位。同时，卫星影像辅助度量尺度恢复、OpenStreetMap对比学习表征、以及近80年海草变化检测等研究，展现了从算法到应用的广泛探索。

## ✨ 今日亮点

- Transformer用于远距离长波红外高光谱大气补偿。
- 双塔图神经网络实现时序地理定位。
- 卫星影像助力前馈重建模型恢复度量尺度。

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260606] Set-Based Transformer for Atmospheric Compensation in Standoff LWIR Hyperspectral Imaging | Perez Fabian, Quintero Nicolas, Acevedo Jeferson, Rueda-Chacon Hoover | Department of Computer Science, Universidad Industrial de Santander | 提出基于集合的Transformer模型，用于远距离长波红外高光谱成像的大气补偿。 | [#682](https://github.com/thinson/RS-PaperClaw/issues/682) |
| [20260606] GeoGNN: Time Series Geo-Localization using Two-Tower Graph Neural Networks | Tran Toan, Abebe Waqwoya, Potnis Abhishek, Chinthavali Supriya, Shahabi Cyrus, Xiong Li, Lunga Dalton | Emory University Oak Ridge National Laboratory Oak Ridge National Laboratory；Oak Ridge National Laboratory University of Southern California Emory University；Oak Ridge National Laboratory | GeoGNN采用双塔图神经网络，实现时序数据的地理定位。 | [#683](https://github.com/thinson/RS-PaperClaw/issues/683) |
| [20260606] Empowering Feed-Forward Reconstruction Models with Metric Scale via Satellite Images | Ze Xianghui, Luo Yongjian, Chao Mengjun, Song Zhenbo, Lu Jianfeng, Shi Yujiao | Nanjing University of Science and Technology；ShanghaiTech University | 利用卫星影像为前馈三维重建模型提供度量尺度信息。 | [#684](https://github.com/thinson/RS-PaperClaw/issues/684) |
| [20260606] OSMGraphCLIP: Learning Global Location Representations from OpenStreetMap Graphs | Michail Dimitrios, Saka Eleni, Giannopoulos Ioannis, Papoutsis Ioannis | National Technical University of Athens, Athens, Greece；Vienna University of Technology, Vienna, Austria | OSMGraphCLIP通过对比学习从OpenStreetMap图学习全局位置表征。 | [#685](https://github.com/thinson/RS-PaperClaw/issues/685) |
| [20260606] Feasibility to detect rapid change and disappearance of seagrass: Lessons from nearly 80 years of vegetation change in the Ako, Seto Inland Sea, Japan | Yamakita Takehisa, Igarashi Yoji, Eto Akira, Ishida Ken, Iiyama Masaaki | Japan Agency for Marine-Earth Science and Technology (JAMSTEC), Application Laboratory (APL), 3173-25, Showa-machi；The University of Tokyo, Graduate School of Agricultural and Life Sciences, 1-1-1 Yayoi, Bunkyo City, Tokyo, Japan；Tokyo University of Marine Science and Technology, 4-5-7 Kohnan, Minato-ku, Tokyo, Japan；Shiga University, Faculty of Data Science, 1-1-1 Banba, Hikone City, Shiga, Japan | 利用近80年航拍影像检测海草植被的快速变化与消失。 | [#686](https://github.com/thinson/RS-PaperClaw/issues/686) |

## 🔎 观察

- 图神经网络与Transformer在遥感任务中应用日益广泛，尤其在空间关系建模方面。
- 长时序遥感分析结合深度学习，为生态监测提供历史变迁的量化手段。

---

Powered by OpenClaw🦞

---

# [20260605](./202606/20260605.md)
## 📌 今日概况

今日共检索候选论文 8 篇；关键词+LLM 智能匹配遥感交叉论文 3 篇；最终纳入日报 3 篇。

今日遥感AI研究聚焦于SAR图像处理与无人机导航两大方向。SAR领域，一篇工作利用深度学习从检测SAR图像中提取InSAR相干性，另一篇则通过物理驱动方法理解飞机目标的语义散射结构。无人机导航方面，提出了一种模拟飞行员思维的细粒度长时程导航方法，结合视觉-语言模型实现6自由度轨迹控制。整体趋势显示，物理模型与数据驱动方法的融合日益深入。

## ✨ 今日亮点

- 深度学习提升InSAR相干性估计精度
- 物理驱动SAR飞机目标散射结构理解
- 视觉-语言模型赋能长时程无人机导航

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260605] Beyond Backscatter: InSAR coherence from detected SAR images | Sica Francescopaolo, Pulella Andrea, Schmitt Michael | Department of Aerospace Engineering, University of the Bundeswehr Munich, Neubiberg, Germany；Microwaves and Radar Institute, German Aerospace Center (DLR), Weßling, Germany | 利用残差U-Net从检测SAR图像估计InSAR相干性，超越传统后向散射方法。 | [#678](https://github.com/thinson/RS-PaperClaw/issues/678) |
| [20260605] Physics-Driven Semantic Scattering Structure Understanding of Aircraft Target in SAR Images | Yin Yifei, Yu Xiaogang, Shi Hao, Chen Liang, Li Wei | the School of Information and Electronics, Beijing Institute of Technology, Beijing , China；the National Key Laboratory of Science and Technology on Space-Born Intelligent Information Processing；the Beijing Institute of Remote Sensing Information, Beijing, China | 提出物理驱动语义散射结构理解方法，用于SAR图像飞机目标识别。 | [#679](https://github.com/thinson/RS-PaperClaw/issues/679) |
| [20260605] Think Like a Pilot: Fine-Grained Long-Horizon UAV Navigation | Zheng Xiangyi, Wang Xiangyu, Liao Qinan, Tang Zimu, Liao Yue, Lyu Dongyue, Wang Guodong, Liu Junjie, Liu Si | Colab May 2026；Colab, Beihang University 2；National University of Singapore；https://buaa-colalab.github.io/FLIGHT/；https://github.com/buaa-colalab/FLIGHT | 模拟飞行员思维，实现细粒度长时程6自由度无人机视觉语言导航。 | [#680](https://github.com/thinson/RS-PaperClaw/issues/680) |

## 🔎 观察

- SAR领域正从单一后向散射分析向多维度信息融合演进。
- 无人机导航研究向长时程、细粒度控制与语言指令结合方向发展。

---

Powered by OpenClaw🦞

---
