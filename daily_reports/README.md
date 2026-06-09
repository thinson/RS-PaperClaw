# Daily Reports

最近三天日报（最新在前）：

# [20260608](./202606/20260608.md)
## 📌 今日概况

今日共检索候选论文 17 篇；关键词+LLM 智能匹配遥感交叉论文 10 篇；最终纳入日报 8 篇。

今日遥感AI研究聚焦于无人机平台的多模态融合与目标检测，同时涉及变化检测、数据管理及建筑物提取。DINOv3驱动的语义对齐、信息瓶颈融合去云、零参数几何门控等新方法涌现，体现了对高精度、高效率及跨时相一致性的追求。

## ✨ 今日亮点

- 无人机多模态融合与目标检测成为今日研究热点
- 语义变化检测引入DINOv3实现跨时相对齐
- 零参数几何门控提升无人机视频分割时域稳定性

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260608] SemDINO: A DINOv3-Driven Network for Cross-Temporal Semantic Alignment in Change Detection | Tong Xinyu, Zhou Meihua, Sun Jinxiao, Tang Yingjie, Wang Lei | the Xinjiang Institute of Ecology and Geography, Chinese Academy of Sciences, Urumqi , China；the University of Chinese Academy of Sciences, Beijing , China；the School of Computer Science, Xiangtan University, Xiangtan , China；the College of Information and Communication Engineering, Harbin Engineering University, Harbin , China | SemDINO利用DINOv3实现跨时相语义对齐的变化检测网络 | [#690](https://github.com/thinson/RS-PaperClaw/issues/690) |
| [20260608] AeroMesa: Efficient Data Management System for Multi-Dimensional Spatio-Temporal Trajectories | Zhang Yue, Ding Zizhong, Sun Lin, Chen Haopeng, Jiao Yan, Xu Yongming | Shanghai Jiao Tong University, Shanghai, China | AeroMesa提出高效管理多维时空轨迹的数据系统 | [#691](https://github.com/thinson/RS-PaperClaw/issues/691) |
| [20260608] IB-HFN: Information Bottleneck-Driven SAR-Optical Fusion Network for High-Fidelity Cloud Removal | Guo Haojun, Feng Fan, Wang Ziquan | Geospatial Information Institute, Information Engineering University, Zhengzhou, China | IB-HFN基于信息瓶颈融合SAR与光学图像实现高保真去云 | [#692](https://github.com/thinson/RS-PaperClaw/issues/692) |
| [20260608] Zero-Parameter Geometric Gating for Temporally Stable Low-Altitude UAV Video Semantic Segmentation | Yang Jingpu, Ji Fengxian, Lai Zhengzhao, Wu Juanfan, Cui Mingxuan, Wang Yufeng | Beihang University Northeastern University The Chinese University of Hong；Beijing Institute of Technology Northeastern University Beihang University | 零参数几何门控方法提升低空无人机视频语义分割时域一致性 | [#693](https://github.com/thinson/RS-PaperClaw/issues/693) |
| [20260608] CAMF-Det: Closure-Aware Multimodal Fusion for LiDAR-Camera 3D Object Detection on UAV Platforms | Jiang Yanze, Gu Yanfeng, Li Xian | a School of Electronics and Information Engineering, Harbin Institute of Technology, Harbin 150001, China | CAMF-Det实现无人机平台LiDAR-相机融合的3D目标检测 | [#694](https://github.com/thinson/RS-PaperClaw/issues/694) |
| [20260608] Illumination-Invariant Anomaly Detection for Sub-Canopy UAV Multispectral Point Clouds | Chen Likun, Gu Yanfeng, Li Xian | School of Electronics and Information School of Electronics and Information School of Electronics and Information；Harbin Institute of Technology Harbin Institute of Technology Harbin Institute of Technology | 光照不变异常检测方法用于林下无人机多光谱点云 | [#695](https://github.com/thinson/RS-PaperClaw/issues/695) |
| [20260608] Edge-Constrained UAV Small-Object Detection with P2 Enhancement and Quantum-Inspired Lightweight Structure Search | Lei Wuming, Gao Yanbin, Sun Mingyan, Li Xiaobin, Liang Xuechen | East China Jiaotong University, Nanchang, China | 边缘约束与量子启发搜索提升无人机小目标检测性能 | [#696](https://github.com/thinson/RS-PaperClaw/issues/696) |
| [20260608] PolyBuild: An End-to-End Method for Polygonal Building Contour Extraction from High-Resolution Remote Sensing Images | Zhang Yaoteng, Zhang Julin, Wang Guangshuai, Deng Jiwei, Sheng Hui, Muhammad Yasir, Wei Shiqing | the College of Oceanography and Space Informatics, China University of Petroleum | PolyBuild端到端方法从高分辨率遥感图像提取多边形建筑轮廓 | [#697](https://github.com/thinson/RS-PaperClaw/issues/697) |

## ⚠️ 未纳入日报的匹配论文

以下论文通过关键词/LLM 筛选，但在处理过程中失败未纳入日报。点击 arXiv 链接可查看原文。

| 标题 | arXiv | 失败原因 |
|------|-------|----------|
| Vision-Language Guided Hyperspectral Object Tracking via Semantics Fusion and Contextual Template Updating | [2606.09167v1](https://arxiv.org/abs/2606.09167v1) | 质检未通过: 单位为空或无效 |
| An Enhanced Geometric-Spectral Feature Learning Framework for Airborne Multispectral Point Cloud Classification | [2606.09123v1](https://arxiv.org/abs/2606.09123v1) | 质检未通过: 单位为空或无效 |


## 🔎 观察

- 无人机平台研究占比过半，多模态融合与轻量化设计成主流趋势
- 语义变化检测与建筑物提取方法向端到端、高保真方向演进

---

Powered by OpenClaw🦞

---

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
