# Daily Reports

最近三天日报（最新在前）：

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

# [20260514](./202605/20260514.md)
## 📌 今日概况

今日共检索候选论文 16 篇；关键词+LLM 智能匹配遥感交叉论文 9 篇；最终纳入日报 8 篇。

今日遥感AI研究呈现多模态融合与生成式AI双主线并进态势。视觉-语言模型向主动感知与超高分理解延伸，扩散模型在图像生成与波段修复领域持续深化，同时几何先验与语义解耦技术在定位与变化检测任务中展现新思路。

## ✨ 今日亮点

- HiSem提出层次化语义解耦框架，通过差分注意力机制优化遥感变化描述生成
- Sat3DGen实现单张卫星图像到街景级三维场景的几何优先重建
- GeoFuse利用道路地图作为免费几何先验，构建天气不变性无人机定位系统

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260514] HiSem: Hierarchical Semantic Disentangling for Remote Sensing Image Change Captioning | Wang Man, Liu Chenyang, Li Wenjun, Ni Feng, Jia Bing, Huang Baoqi, Xia Riting, Shi Zhenwei | Aerospace Information Research Institute, Chinese Academy of Sciences；School of Electronic, Electrical and Communication Engineering, University of Chinese Academy of Sciences；Key Laboratory of Network Information System Technology (NIST), Aerospace Information Research Institute, Chinese Academy of Sciences；Key Laboratory of Computational Optical Imaging Technology, Aerospace Information Research Institute, Chinese Academy of Sciences；School of Astronautics, Beihang University | HiSem通过层次化语义解耦与差分注意力机制，提升遥感图像变化描述生成的准确性与可解释性。 | [#534](https://github.com/thinson/RS-PaperClaw/issues/534) |
| [20260514] Sat3DGen: Comprehensive Street-Level 3D Scene Generation from Single Satellite Image | Qian Ming, Xia Zimin, Liu Changkun, Ma Shuailei, Wang Wen, Ke Zeran, Tan Bin, Zhang Hang, Xia Gui-Song | LIESMARS & School of Artificial Intelligence, Wuhan University；EPFL；HKUST；Northeastern University；Zhejiang University；Ant Group；Amap, Alibaba Group | Sat3DGen采用几何优先方法，从单张卫星图像生成综合街景级三维场景，实现跨视角合成。 | [#535](https://github.com/thinson/RS-PaperClaw/issues/535) |
| [20260514] Road Maps as Free Geometric Priors: Weather-Invariant Drone Geo-Localization with GeoFuse | Fang Yunsong, Wang Tingyu, Zheng Zhedong | University of Macau；Hangzhou Dianzi University | GeoFuse将道路地图作为免费几何先验融入跨模态学习，解决天气变化下的无人机地理定位难题。 | [#536](https://github.com/thinson/RS-PaperClaw/issues/536) |
| [20260514] TERRA-CD: Multi-Temporal Framework for Multi-class and Semantic Change Detection | Oak Omkar, Nazre Rukmini, Budke Rujuta, Sawant Suraj | COEP Technological University；University of Massachusetts, Amherst；North Carolina State University | TERRA-CD构建多时相框架，支持多类别语义变化检测，面向城市植被等应用场景。 | [#537](https://github.com/thinson/RS-PaperClaw/issues/537) |
| [20260514] GeoVista: Visually Grounded Active Perception for Ultra-High-Resolution Remote Sensing Understanding | Zhu Jiashun, Fu Ronghao, Hu Jiasen, Xing Nachuan, Na Xu, Yang Xiao, Lin Zhiwen, Zhang Weipeng, Sun Lang, Xue Zhiheng, Liu Haoran, Zhang Weijie, Yang Bo | College of Computer Science and Technology, Jilin University；Key Laboratory of Symbolic Computation and Knowledge Engineering of Ministry of Education | GeoVista提出视觉基础主动感知机制，针对超高分遥感图像实现高效视觉定位理解。 | [#538](https://github.com/thinson/RS-PaperClaw/issues/538) |
| [20260514] GeoViSTA: Geospatial Vision-Tabular Transformer for Multimodal Environment Representation | Liu Yuhao, Al-Kindi Sadeer, Veeraraghavan Ashok, Balakrishnan Guha | Rice University；Houston Methodist | GeoViSTA融合地理空间视觉与表格数据，基于自监督学习构建多模态环境表征模型。 | [#539](https://github.com/thinson/RS-PaperClaw/issues/539) |
| [20260514] AnyBand-Diff: A Unified Remote Sensing Image Generation and Band Repair Framework with Spectral Priors | Zhao Zuopeng, Liu Ying, Li Xiaoyu, Luo Su, Li Lu, Liu Wenwen | Tsinghua University；Chinese Academy of Sciences | AnyBand-Diff利用光谱先验统一遥感图像生成与波段修复，基于扩散模型实现灵活光谱重建。 | [#540](https://github.com/thinson/RS-PaperClaw/issues/540) |
| [20260514] D2-CDIG: Controlled Diffusion Remote Sensing Image Generation with Dual Priors of DEM and Cloud-Fog | Zhao Zuopeng, Liu Ying, Pharksuwan Kanyaphakphachsorn, Luo Su, Li Xiaoyu, Ning Maocai | the School of Computer Science and Technolo- pollution, and climate change with surface features is often not；the School of Computer Science and Technology/School of simulating different weather conditions or terrain environments | D2-CDIG引入DEM与云雾双重先验，实现可控扩散生成以模拟多样天气与地形条件。 | [#541](https://github.com/thinson/RS-PaperClaw/issues/541) |

## 🔎 观察

- 生成式扩散模型在遥感领域应用趋深，从单纯图像合成扩展至波段修复、云雾控制等精细化任务，数据增强与物理仿真价值凸显。
- 视觉-语言模型正从被动理解转向主动感知，结合超高分图像处理与视觉定位，推动遥感智能体决策能力升级。

---

Powered by OpenClaw🦞

---
