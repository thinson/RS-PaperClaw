# Daily Reports

最近三天日报（最新在前）：

# [20260517](./202605/20260517.md)
## 📌 今日概况

今日共检索候选论文 7 篇；关键词+LLM 智能匹配遥感交叉论文 5 篇；最终纳入日报 4 篇。

今日遥感AI研究呈现多元化趋势：无人机系统控制与通信仿真持续深化，高光谱成像与量子机器学习成为新兴热点。多智能体编队控制、信道建模、预训练骨干网络及SAR目标检测等方向均有进展，体现算法创新与硬件约束协同优化的发展特征。

## ✨ 今日亮点

- 基于控制障碍函数的分布式无人机编队控制，解决视场约束下的安全协同问题
- HyperVision提出通道自适应动态嵌入机制，构建高光谱预训练骨干网络
- 量子退火辅助SVM实现SAR影像溢油近实时检测，探索量子-经典混合架构

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260517] Distributed 3D Leader-Follower Formation Control with Field-of-View Safety via Control Barrier Functions | Immanuel R. Santjoko, Richie R. Suganda, Pan Miao, Hu Bin | Huazhong University of Science and Technology | 提出分布式三维领导者-跟随者编队控制框架，利用控制障碍函数处理视场约束，实现多无人机安全协同。 | [#555](https://github.com/thinson/RS-PaperClaw/issues/555) |
| [20260517] UPSim: UxNB Propagation Simulator for 3D Map-Driven FR3 Deployments | Vinogradov Evgenii | NaNoNetworking Center in Catalonia (N3Cat), Universitat Politècnica de Catalunya, Spain；Department of Electrical Engineering, KU Leuven, Belgium | 开发面向FR3频段的无人机基站传播仿真器UPSim，结合射线追踪与三维地图驱动空对地信道建模。 | [#556](https://github.com/thinson/RS-PaperClaw/issues/556) |
| [20260517] HyperVision: A Channel-Adaptive Ground-Based Hyperspectral Vision Pre-trained Backbone | Fu Guanyiman, Li Jingtao, Cheng Zihang, Li Zhuanfeng, Chen Diqi, Xu Yan, Xiong Fengchao, Lu Jianfeng, Zhou Jun | Griffith University；Wuhan University；Nanjing University of Science and Technology；Huaiyin Normal University；Massey University | 构建通道自适应高光谱预训练骨干网络HyperVision，采用动态嵌入与伪标签策略提升表征能力。 | [#557](https://github.com/thinson/RS-PaperClaw/issues/557) |
| [20260517] Toward Near-Real-Time Marine Oil Spill Detection in SAR Imagery using Quantum-Assisted SVM | Strauss Joseph, Sharma Jyotsna | Louisiana State University | 将量子退火引入SAR溢油检测，设计量子辅助SVM分类器以逼近近实时处理需求。 | [#558](https://github.com/thinson/RS-PaperClaw/issues/558) |

## ⚠️ 未纳入日报的匹配论文

以下论文通过关键词/LLM 筛选，但在处理过程中失败未纳入日报。点击 arXiv 链接可查看原文。

| 标题 | arXiv | 失败原因 |
|------|-------|----------|
| Large-Scale Quantum Kernels for Hyperspectral Data Classification | [2605.17587v1](https://arxiv.org/abs/2605.17587v1) | 质检未通过: 单位为空或无效 |


## 🔎 观察

- 无人机技术链呈现全栈覆盖态势：从底层信道仿真、中层编队控制到上层智能感知，系统性研究特征明显
- 量子计算与遥感AI的交叉尚处探索期，当前以混合架构为主，实用化仍需突破量子比特规模与噪声瓶颈

---

Powered by OpenClaw🦞

---

# [20260516](./202605/20260516.md)
## 📌 今日概况

今日共检索候选论文 3 篇；关键词+LLM 智能匹配遥感交叉论文 3 篇；最终纳入日报 3 篇。

今日研究聚焦三维变化检测与多模态遥感图像分割。视觉几何基础模型与Mamba架构成为热点，分别用于无训练点云配准和光-高程图像融合。SAR变化检测领域关注全局动态上下文建模，整体呈现基础模型迁移与高效架构探索并行的趋势。

## ✨ 今日亮点

- VGGT-CD提出无训练三维变化检测框架，利用视觉几何基础模型实现鲁棒点云配准
- 轴向关系引导的Mamba融合模型，优化光-高程多模态遥感图像分割性能
- 全局动态上下文感知网络增强SAR图像变化检测的特征表达能力

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260516] VGGT-CD: Training-Free Robust Registration for 3D Change Detection | Zhang Wei, Li Songhua, Wu Yihang, Li Qiang, Wang Qi | Northwestern Polytechnical University | VGGT-CD利用视觉几何基础模型实现无需训练的三维变化检测点云配准，提升鲁棒性。 | [#551](https://github.com/thinson/RS-PaperClaw/issues/551) |
| [20260516] Axial-Relation Guided Fusion State Space Model for Optical-Elevation Sensing Image Segmentation | Gao Feng, Jin Zhilin, Gan Yanhai, Dong Junyu, Du Qian | the Department of Electrical and Computer Engineering, modeling of fine-grained local details and global contex- | 提出轴向关系引导的融合状态空间模型，用于光-高程遥感图像的语义分割任务。 | [#552](https://github.com/thinson/RS-PaperClaw/issues/552) |
| [20260516] Synthetic Aperture Radar Image Change Detection Based on Global Dynamic Context-Aware Network | Huan Baogui, Gong Chuanzheng, Chen Dezhong, Gao Feng, Dong Junyu, Du Qian | the In contemporary remote sensing research, a wide variety of；the Department of Electrical and Computer Engineering, optical, synthetic aperture radar；the In contemporary remote sensing research, a wide variety of State Key Laboratory of Physical Oceanography, Ocean University of China, sensors are employed for image change detection, including Qingdao 266100, China | 基于全局动态上下文感知网络的SAR图像变化检测方法，增强卷积神经网络的全局建模能力。 | [#553](https://github.com/thinson/RS-PaperClaw/issues/553) |

## 🔎 观察

- 视觉几何基础模型向三维点云任务迁移成为新方向，无训练范式降低数据依赖
- Mamba架构在遥感多模态融合中加速渗透，状态空间模型或成CNN/Transformer替代方案

---

Powered by OpenClaw🦞

---

# [20260515](./202605/20260515.md)
## 📌 今日概况

今日共检索候选论文 14 篇；关键词+LLM 智能匹配遥感交叉论文 6 篇；最终纳入日报 6 篇。

今日遥感AI研究呈现多模态融合与不确定性量化两大趋势。MLLM赋能农业景观分割、证据深度学习提升野火烟雾检测可靠性，同时自监督时空建模、扩散模型变化检测及文本引导图像重建等方向均有新进展，体现基础模型与任务专用方法的并行发展。

## ✨ 今日亮点

- 多模态大语言模型首次系统应用于高分辨率农业景观语义分割任务
- 证据深度学习结合CBAM注意力机制实现野火烟雾密度不确定性量化
- 发布49.2万样本长时序高光谱数据集，支撑时空自监督学习研究

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260515] MAgSeg: Segmentation of Agricultural Landscapes in High-Resolution Satellite Imagery using Multimodal Large Language Models | Tiwary Piyush, Ahuja Utkarsh, Sani Depanshu, Jayagopal Aishwarya, Gubbi Sagar, Venugopalan Subhashini, Talekar Alok, Rajan Vaibhav | Google DeepMind；Google；Indian Institute of Science | MAgSeg提出基于多模态大语言模型的农业景观分割框架，利用视觉-语言对齐提升高分辨率卫星影像的语义理解能力。 | [#544](https://github.com/thinson/RS-PaperClaw/issues/544) |
| [20260515] Uncertainty-Aware Wildfire Smoke Density Classification from Satellite Imagery via CBAM-Augmented EfficientNet with Evidential Deep Learning | Chodavarapu Ranjith | Kent State University | 该研究将CBAM增强的EfficientNet与证据深度学习结合，在野火烟雾密度分类中实现显式不确定性估计。 | [#545](https://github.com/thinson/RS-PaperClaw/issues/545) |
| [20260515] Highly Detailed and Generalizable Broadleaf Tree Crown Instance Segmentation from UAV Imagery | Nakada Mitsutaka, Ikebata Takahiko, Ikebata Kengo, Mizuno Yuji, Onoda Yusuke, Takeshige Ryuichi, Kyaw Kyaw Htoo, Kitayama Kanehiro, Ong Robert, Onishi Masanori | DeepForest Technologies Co., Ltd.；YM Lab.；Graduate School of Agriculture, Kyoto University；Graduate School of Science, Osaka Metropolitan University；Faculty of Tropical Forestry, Universiti Malaysia Sabah；Forest Research Centre, Sabah Forestry Department | 针对无人机阔叶林影像，开发高度精细且可泛化的单木树冠实例分割方法，融合多机构跨地域数据验证。 | [#546](https://github.com/thinson/RS-PaperClaw/issues/546) |
| [20260515] ChronoEarth-492K: A Large Scale and Long Horizon Spatiotemporal Hyperspectral Earth Observation Dataset and Benchmark | Si Haozhe, Wan Yuxuan, Wang Yuqing, Do Minh, Zhao Han | Department of Electrical and Computer Engineering；Siebel School of Computing and Data Science；University of Illinois Urbana-Champaign | ChronoEarth-492K构建大规模长时序高光谱地球观测数据集，为时空自监督学习提供标准化基准。 | [#547](https://github.com/thinson/RS-PaperClaw/issues/547) |
| [20260515] LDGUID: A FRAMEWORK FOR ROBUST CHANGE DETECTION VIA LATENT DIFFERENCE GUIDANCE | Zhao Jiaxuan, Bereyhi Ali | University of Toronto | LDGUID通过潜在差异引导与信息瓶颈约束，提升对抗自编码器在变化检测中的鲁棒性与语义判别能力。 | [#548](https://github.com/thinson/RS-PaperClaw/issues/548) |
| [20260515] Text-RSIR: A Text-Guided Framework for Efficient Remote Sensing Image Transmission and Reconstruction | Yang Hao, Ma Xianping, Ma Peifeng, Pun Man-On | School of Science and Engineering, The Chinese University of Hong Kong, Shenzhen；Geosciences and Engineering, Southwest Jiaotong University；Institute of Space and Earth Information Science and the Department of Geography and Resource Management, The Chinese University of Hong Kong | Text-RSIR建立文本引导的遥感图像传输重建框架，利用跨模态先验实现高效压缩与高质量恢复。 | [#549](https://github.com/thinson/RS-PaperClaw/issues/549) |

## 🔎 观察

- 基础模型下沉趋势明显：MLLM、扩散模型等通用架构正快速向遥感专用任务渗透，但领域适配机制尚待深化。
- 不确定性量化关注度提升：从野火烟雾到变化检测，可靠性建模成为遥感AI落地应用的关键瓶颈与研究方向。

---

Powered by OpenClaw🦞

---
