# Daily Reports

最近三天日报（最新在前）：

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

# [20260513](./202605/20260513.md)
## 📌 今日概况

今日共检索候选论文 18 篇；关键词+LLM 智能匹配遥感交叉论文 15 篇；最终纳入日报 8 篇。

今日遥感AI研究聚焦三大方向：无人机系统智能化（4篇）涵盖走廊管理、定位与多机协同；多/高光谱成像技术（3篇）涉及融合检测、光谱超分辨与色彩恒常性；以及基础理论探索，包括深度学习幻觉问题与二维材料物理机制。

## ✨ 今日亮点

- WD-FQDet提出小波分解与频率感知查询学习，优化多光谱目标检测性能
- Phy-CoSF结合物理引导与隐式神经表示，实现快照压缩成像的光谱连续重建
- 多UAV定位研究涌现，感知辅助LoS/NLoS识别与不确定性感知精修形成技术互补

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260513] Loiter UAV Reinsertion Guidance for Fixed-wing UAV Corridors | J Pradeep, Siddhardha Kedarisetty, Ratnoo Ashwini | Indian Institute of Technology Bhilai；Indian Institute of Science | 针对固定翼无人机走廊场景，提出盘旋模式重入制导策略，优化空域交通管理效率。 | [#524](https://github.com/thinson/RS-PaperClaw/issues/524) |
| [20260513] WD-FQDet: Multispectral Detection Transformer via Wavelet Decomposition and Frequency-aware Query Learning | Yang Chunjin, Zhang Xiwei, Xiao Yiming, Meng Fanman | University of Electronic Science and Technology of China | WD-FQDet通过小波分解与频率感知查询学习，增强多光谱检测Transformer的跨模态特征融合能力。 | [#525](https://github.com/thinson/RS-PaperClaw/issues/525) |
| [20260513] Phy-CoSF: Physics-Guided Continuous Spectral Fields Reconstruction and Super-Resolution for Snapshot Compressive Imaging | Chen Wudi, Zha Zhiyuan, Yuan Xin, Wang Shigang, Wen Bihan, Zhou Jiantao, Yan Gang, Fan Zipei, Zhu Ce | College of Communication Engineering, Jilin University；School of Engineering, Westlake University；School of Electrical & Electronic Engineering, Nanyang Technological University；Department of Computer and Information Science, University of Macau；College of Computer Science and Technology, Jilin University；College of Artificial Intelligence, Jilin University；School of Information and Communication Engineering, University of Electronic Science and Technology of China | Phy-CoSF融合物理先验与隐式神经表示，实现快照压缩成像的光谱连续场重建与超分辨率。 | [#526](https://github.com/thinson/RS-PaperClaw/issues/526) |
| [20260513] Anisotropic Dopant and Strain Architectures in WS$_2$ Nanocrystals Driven by Growth Kinetics | Frederico B. Sousa, Raphaela de Oliveira, Matheus J. S. Matos, Elizabeth Grace Houser, Igor Ferreira Curvelo, Yu Zhuohang, Liu Mingzu, Menescal Felipe, Gilmar Eugenio Marques, Leandro M. Malard, Terrones Mauricio, Bruno R. Carvalho, Chacham Helio, Marcio D. Teodoro | Departamento de Física, Universidade Federal de São Carlos；Brazilian Synchrotron Light Laboratory (LNLS), Brazilian Center for Research in Energy and Materials (CNPEM)；Departamento de Física, Universidade Federal de Ouro Preto；Center for 2-Dimensional and Layered Materials, The Pennsylvania State University；Department of Physics, The Pennsylvania State University；Department of Materials Science and Engineering, The Pennsylvania State University；Departamento de Física, Universidade Federal de Minas Gerais；Departamento de Física, Universidade Federal do Rio Grande do Norte | 揭示WS₂纳米晶中生长动力学驱动的各向异性掺杂与应变架构，为二维材料可控合成提供新机制。 | [#527](https://github.com/thinson/RS-PaperClaw/issues/527) |
| [20260513] Sensing-Assisted LoS/NLoS Identification in Dynamic UAV Positioning Systems | Qiao Huijuan, Bai Lu, Sun Mingran, Lu Mengyuan, Chen Jiajing, Cheng Xiang | Tsinghua University；Chinese Academy of Sciences | 利用信道脉冲响应与多模态融合，实现动态UAV定位系统中LoS/NLoS状态的感知辅助识别。 | [#528](https://github.com/thinson/RS-PaperClaw/issues/528) |
| [20260513] Uncertainty-Aware 3D Position Refinement for Multi-UAV Systems | Alamleh Hosam, Pulatov Damir | University of North Carolina Wilmington | 提出不确定性感知的分布式估计框架，通过协方差交叉融合实现多UAV系统的3D位置精修。 | [#529](https://github.com/thinson/RS-PaperClaw/issues/529) |
| [20260513] COLOR CONSTANCY IN HYPERSPECTRAL IMAGING VIA REDUCED SPECTRAL SPACES | G. Dofri Vidarsson, Lu Liying, Süsstrunk Sabine | École Polytechnique Fédérale de Lausanne (EPFL) | 基于降维光谱空间的高光谱色彩恒常性方法，有效分离光源与表面反射特性。 | [#530](https://github.com/thinson/RS-PaperClaw/issues/530) |
| [20260513] On Hallucinations in Inverse Problems: Fundamental Limits and Provable Assessment Methods | Iagaru David, Nina M. Gottschling, Anders C. Hansen, Garnier Josselin | CMAP, Ecole polytechnique, Institut Polytechnique de Paris；German Aerospace Center (DLR), Remote Sensing Technology Institute；Computing and Computational Sciences, Oak Ridge National Laboratory；DAMTP, University of Cambridge；CMAP, CNRS, Ecole polytechnique, Institut Polytechnique de Paris | 系统分析逆问题中深度学习幻觉的数学极限，建立可证明的可靠性评估方法论。 | [#531](https://github.com/thinson/RS-PaperClaw/issues/531) |

## ⚠️ 未纳入日报的匹配论文

以下论文通过关键词/LLM 筛选，但在处理过程中失败未纳入日报。点击 arXiv 链接可查看原文。

| 标题 | arXiv | 失败原因 |
|------|-------|----------|
| LMPath: Language-Mediated Priors and Path Generation for Aerial Exploration | [2605.13782v1](https://arxiv.org/abs/2605.13782v1) | 质检未通过: 单位为空或无效 |
| HADAR-Based Thermal Infrared Hyperspectral Image Restoration | [2605.13664v1](https://arxiv.org/abs/2605.13664v1) | 质检未通过: 单位为空或无效 |
| HIR-ALIGN: Enhancing Hyperspectral Image Restoration via Diffusion-Based Data Generation | [2605.13581v1](https://arxiv.org/abs/2605.13581v1) | 质检未通过: 单位为空或无效 |
| A Multi-Modal Intelligent U2V Channel Model for 6G Sensing-Communication Integration | [2605.13502v1](https://arxiv.org/abs/2605.13502v1) | 质检未通过: 单位为空或无效 |
| RS-Claw: Progressive Active Tool Exploration via Hierarchical Skill Trees for Remote Sensing Agents | [2605.13391v1](https://arxiv.org/abs/2605.13391v1) | 质检未通过: 单位为空或无效 |
| Galilean State Estimation for Inertial Navigation Systems with Unknown Time Delay | [2605.13266v1](https://arxiv.org/abs/2605.13266v1) | 质检未通过: 标题为空或无效; Q1 未通过质检; Q5 未通过质检; Q6 未通过质检 |


## 🔎 观察

- UAV研究从单一导航向'感知-通信-控制'一体化演进，通感融合成为关键使能技术
- 高光谱成像正从传统重建迈向物理约束与神经表示的深度结合，光谱连续性成为新指标

---

Powered by OpenClaw🦞

---

# [20260512](./202605/20260512.md)
## 📌 今日概况

今日共检索候选论文 11 篇；关键词+LLM 智能匹配遥感交叉论文 8 篇；最终纳入日报 6 篇。

今日遥感AI研究呈现三大趋势：一是大语言模型与智能体技术深度渗透农业预测、灾害响应等垂直场景；二是超高分影像与跨模态（光学-SAR、视觉-语言）融合成为技术焦点；三是自监督学习与基础模型推动地理实体关系推理向精细化发展。多模态感知与具身智能成为核心驱动力。

## ✨ 今日亮点

- 智能体后修正机制革新农业产量预测范式，实现预测-解释-修正闭环
- 超高分视觉语言模型诊断分辨率幻觉问题，突破微目标空间定位瓶颈
- 文本语义驱动光学-SAR跨模态配准，破解异构影像特征对齐难题

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260512] Agent-Based Post-Hoc Correction of Agricultural Yield Forecasts | Beddows Matthew, Durrant Aiden, Leontidis Georgios | University of Aberdeen；University of East Anglia；UiT The Arctic University of Norway | 提出基于大语言模型的智能体后修正框架，通过多智能体协作对农业产量时序预测结果进行动态校正与不确定性量化。 | [#516](https://github.com/thinson/RS-PaperClaw/issues/516) |
| [20260512] NARA: Anchor-Conditioned Relation-Aware Contextualization of Heterogeneous Geoentities | Kim Jina, Mai Gengchen, Zhao Lingyi, Shafique Khurram, Chiang Yao-Yi | University of Minnesota；University of Texas at Austin；Novateur Research Solutions | 构建锚点条件化关系感知框架NARA，以自监督方式学习异构地理实体间的空间关系表征。 | [#517](https://github.com/thinson/RS-PaperClaw/issues/517) |
| [20260512] UHR-Micro: Diagnosing and Mitigating the Resolution Illusion in Earth Observation VLMs | Ni Shuo, Wang Tong, Zhang Jing, Chen He, Guo Haonan, Zhang Ning, Du Bo | National Key Laboratory of Science and Technology on Space-Born Intelligent Information Processing, Beijing Institute of Technology；School of Computer Science, Wuhan University；Zhongguancun Academy；State Key Laboratory of Information Engineering in Surveying, Mapping and Remote Sensing, Wuhan University；The Department of Computing, Hong Kong Polytechnic University | 系统诊断地球观测视觉语言模型的分辨率幻觉现象，提出多尺度空间接地机制提升微目标识别精度。 | [#518](https://github.com/thinson/RS-PaperClaw/issues/518) |
| [20260512] TAR: Text Semantic Assisted Cross-modal Image Registration Framework for Optical and SAR Images | Cai Zhuoyu, Quan Dou, Huyan Ning, He Pei, Wang Shuang, Jiao Licheng | the Department of from a wide spatial range while maintaining feature invariance | 设计文本语义辅助的跨模态配准网络TAR，利用高层语义桥接光学与SAR影像的模态差异。 | [#519](https://github.com/thinson/RS-PaperClaw/issues/519) |
| [20260512] Mobile Traffic Camera Calibration from Road Geometry for UAV-Based Traffic Surveillance | Popov Alexey, Trukhina Natalia, Vashkelis Vadim | Embedded Intelligence Lab | 基于道路几何约束实现移动交通相机自标定，为无人机交通监控提供轻量级鸟瞰视图生成方案。 | [#520](https://github.com/thinson/RS-PaperClaw/issues/520) |
| [20260512] Can LLM Agents Respond to Disasters? Benchmarking Heterogeneous Geospatial Reasoning in Emergency Operations | Wang Junjue, Xuan Weihao, Qi Heli, Dai Pengyu, Liu Kunyi, Chen Hongruixuan, Zheng Zhuo, Xia Junshi, Ermon Stefano, Yokoya Naoto | The University of Tokyo；RIKEN AIP；Waseda University；Stanford University | 构建灾害响应场景下的异构地理空间推理基准，系统评估大语言模型智能体的应急决策能力边界。 | [#521](https://github.com/thinson/RS-PaperClaw/issues/521) |

## ⚠️ 未纳入日报的匹配论文

以下论文通过关键词/LLM 筛选，但在处理过程中失败未纳入日报。点击 arXiv 链接可查看原文。

| 标题 | arXiv | 失败原因 |
|------|-------|----------|
| Large-Small Model Collaboration for Farmland Semantic Change Detection | [2605.12282v1](https://arxiv.org/abs/2605.12282v1) | 质检未通过: 单位为空或无效 |


## 🔎 观察

- 智能体架构正从通用对话向领域专用决策演进，后修正机制或成为高 stakes 预测任务的标准配置
- 跨模态融合重心已从像素级对齐转向语义级桥接，文本作为中间表征显著降低模态鸿沟

---

Powered by OpenClaw🦞

---
