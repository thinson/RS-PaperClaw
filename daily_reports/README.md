# Daily Reports

最近三天日报（最新在前）：

# [20260823](./202608/20260823.md)
## 📌 今日概况

今日共检索候选论文 4 篇；关键词+LLM 智能匹配遥感交叉论文 3 篇；最终纳入日报 3 篇。

今日遥感AI研究聚焦于多模态大语言模型在遥感图像理解中的应用，提出基于热扩散的语义感知分词方法；同时，光学卫星影像配准通过自校准稠密位移场提升可靠性；低空无人机视觉定位则借助深度引导的共视推理增强匹配精度。整体趋势显示，语义理解与几何配准并重，多模态融合与深度信息利用成为提升性能的关键。

## ✨ 今日亮点

- 热扩散分词提升遥感图像语义理解
- 自校准位移场优化大影像配准
- 深度引导共视推理增强无人机定位

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260823] HeatTok: Enhancing Remote Sensing Image Understanding via Thermodiffusion-based Tokenization | Yan Yingying, Tang Jiaqi, Wei Wei, Wang Qianzhou, Wu Jinjian, Geng Botong, Chen Jianmin, Xia Yuyang, Zhang Lei | Northwestern Polytechnical Hong Kong University of Science and Northwestern Polytechnical；University Technology University；University University University | 提出热扩散分词方法，增强多模态大模型对遥感图像的语义理解。 | [#1160](https://github.com/thinson/RS-PaperClaw/issues/1160) |
| [20260823] Self-Calibrating Dense Displacement Fields for Reliable Co-Registration of Large Optical Satellite Imagery | Sun Shoukun, Wang Zhe, Salati Sanaz, Zhang Jiyin, Wang Hui, Ma Xiaogang | Department of Computer Science, University of Idaho, Moscow, ID USA (；the National Center for Ecological Analysis and Synthesis (NCEAS), University of California, Santa Barbara, CA USA (；Research Computing and Data Services (RCDS), University of Idaho, Moscow, ID USA (；Department of Geography and Planning, Appalachian State University, Boone, NC USA ( | 自校准稠密位移场实现大型光学卫星影像的可靠配准。 | [#1161](https://github.com/thinson/RS-PaperClaw/issues/1161) |
| [20260823] DECO: Depth-Guided Co-Visibility Reasoning for Low-Altitude UAV Visual Localization | Ye Yibin, Teng Xichao, Chen Shuo, Song Xiaokai, Guan Dongdong, Yu Qifeng, Li Zhang | College of Aerospace Science and Engineering, National University of Defense Technology, Changsha 410073, China | 深度引导共视推理提升低空无人机视觉定位的准确性。 | [#1162](https://github.com/thinson/RS-PaperClaw/issues/1162) |

## 🔎 观察

- 语义感知分词与深度信息结合，反映多模态与几何先验融合趋势。
- 自校准机制与共视推理均强调鲁棒性，应对复杂遥感场景挑战。

---

Powered by OpenClaw🦞

---

# [20260822](./202608/20260822.md)
## 📌 今日概况

今日共检索候选论文 3 篇；关键词+LLM 智能匹配遥感交叉论文 2 篇；最终纳入日报 2 篇。

今日遥感AI研究聚焦于无人机导航与变化检测数据优化两大方向。AirAlign提出几何感知的相对位姿对齐方法，提升无人机末端导航精度；FDC框架则针对变化检测中的标签噪声问题，通过数据剪枝策略平衡保真度、多样性与一致性，以提升模型训练效率与鲁棒性。两项工作分别从感知定位与数据质量角度推动遥感AI的实用化发展。

## ✨ 今日亮点

- 无人机末端导航引入几何感知特征，提升相对位姿估计精度。
- 变化检测数据剪枝新框架，兼顾保真度、多样性与一致性。
- 两项研究分别聚焦感知定位与数据质量优化，应用导向明确。

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260822] AirAlign: Geometry-Aware Relative Pose Alignment for UAV Last-Meter Navigation | Zhou Jinyi, Feng Shuo, Wu Yufei, Li Piji | Nanjing University of Aeronautics and Astronautics Nanjing China | AirAlign利用几何感知特征对齐相对位姿，优化无人机最后阶段导航精度。 | [#1157](https://github.com/thinson/RS-PaperClaw/issues/1157) |
| [20260822] Fidelity-Diversity-Consistency (FDC): Data Pruning for Remote Sensing Change Detection | Zhu Dongyao, Ranga Raju Vatsavai | Department of Computer Science；North Carolina State University；EL2 N K-Center；National AI Research Institutes Competitive Award no. 2023-67021-39829. temporal mismatches [22], introducing substantial label noise | FDC数据剪枝方法通过平衡保真度、多样性与一致性，减少遥感变化检测标签噪声影响。 | [#1158](https://github.com/thinson/RS-PaperClaw/issues/1158) |

## 🔎 观察

- 研究趋势偏向于解决实际部署中的细粒度问题，如末端导航与数据噪声。
- 数据质量与几何信息利用成为提升遥感模型性能的关键切入点。

---

Powered by OpenClaw🦞

---

# [20260821](./202608/20260821.md)
## 📌 今日概况

今日共检索候选论文 12 篇；关键词+LLM 智能匹配遥感交叉论文 5 篇；最终纳入日报 5 篇。

今日遥感AI研究聚焦于农业、大气、城市感知、多模态检测及红外小目标检测等方向。农业杂草检测关注跨田域分布偏移下的迁移能力；大气遥感利用ADS-B干涉测量折射率时空变化；城市理解通过时空对齐提升语义感知；多模态检测引入专家引导的特征重校准；红外小目标检测提出相对退化感知网络。整体呈现从单一模态向多模态融合、从静态分析向动态感知发展的趋势。

## ✨ 今日亮点

- 农业杂草检测跨田域泛化能力受关注，无监督域适应成关键。
- ADS-B干涉测量新方法用于大气折射率时空变化遥感。
- 多模态检测引入专家引导特征重校准，提升融合精度。

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260821] On the Transferability of Agricultural Weed Detection Under Cross-Field Distribution Shift | Prabhakar Nikhilesh, Tenali Pranuthi, Wilfredo Abudeye Fernandez, Borah Shekhar, Karanam Athresh, Blasch Erik, Sundaravadivel Prabha, Natarajan Sriraam | University of Texas at Dallas；University of Texas at Tyler；Air Force Research Lab | 研究农业杂草检测在跨田域分布偏移下的迁移能力，采用无监督域适应方法。 | [#1151](https://github.com/thinson/RS-PaperClaw/issues/1151) |
| [20260821] Remote sensing of the temporal and spatial variability of atmospheric refractivity using ADS-B interferometry (ADSBi) | Lewis Ollie, Brunt Chris, Kitchen Malcolm, Neill E. Bowler, Edmund K. Stone | Department of Physics and Astronomy, University of Exeter, Exeter, United Kingdom；Institute (KNMI) (de Haan and Stoffelen 2012; de Haan et al | 利用ADS-B干涉测量遥感大气折射率，揭示其时空变异性及湿度关联。 | [#1152](https://github.com/thinson/RS-PaperClaw/issues/1152) |
| [20260821] CoST: Semantic-Aware Urban Understanding via Spatial-Temporal Alignment | Jiang Yutian, Liu Jiabo, Hao Xixuan, Liang Yuxuan | The Hong Kong University of Science and Technology (Guangzhou) Guangzhou China | 提出CoST模型，通过时空对齐实现卫星影像的语义感知城市理解。 | [#1153](https://github.com/thinson/RS-PaperClaw/issues/1153) |
| [20260821] SuppreSensing: Expert-Guided Feature Recalibration and Discrepancy Augmentation for Multimodal Object Detection | Wu Xin, Gao Zhenyu, Zhang Qiankun, Guo Shaoyong | Beijing University of Posts and Telecommunications Beijing China | SuppreSensing方法结合专家引导特征重校准与差异增强，提升多模态检测性能。 | [#1154](https://github.com/thinson/RS-PaperClaw/issues/1154) |
| [20260821] RDANet: Relative Degradation Aware Network for Infrared Small Target Detection | Liu Rui, Nie Jing, Fu Ying | School of Computer Science and Technology, Beijing Institute of Technology, Beijing, China (；School of Information and Electronics, Beijing Institute of Technology, Beijing, China ( | RDANet网络通过相对退化感知与多尺度下采样，增强红外小目标检测能力。 | [#1155](https://github.com/thinson/RS-PaperClaw/issues/1155) |

## 🔎 观察

- 跨域泛化问题在农业遥感中凸显，域适应技术成为提升模型实用性的关键。
- 多模态融合与专家知识结合，正成为提升遥感目标检测鲁棒性的新方向。

---

Powered by OpenClaw🦞

---
