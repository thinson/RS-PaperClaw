# Daily Reports

最近三天日报（最新在前）：

# [20260504](./202605/20260504.md)
## 📌 今日概况

今日共检索候选论文 14 篇；关键词+LLM 智能匹配遥感交叉论文 9 篇；最终纳入日报 6 篇。

今日遥感AI研究呈现多元化趋势：基础模型优化与轻量化部署并进，涵盖视觉基础模型对比、扩散模型蒸馏等方向；应用场景拓展至能源监测、废弃物管理与灾害响应；多源数据融合技术持续深化，包括SAR极化融合与全色锐化等。

## ✨ 今日亮点

- SlimDiffSR通过扩散模型蒸馏实现轻量化超分辨率，兼顾性能与效率
- 撒哈拉以南非洲 crowdsourced UAV 废弃物检测开源模型，服务可持续发展
- RAFNet提出区域感知融合网络，优化全色锐化中的空间-光谱信息平衡

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260504] AI and Open-data Driven Scalable Solar Power Profiling | Zhang Shiliang, Maharjan Sabita, Turgut Damla | the Department of Computer can transfer across tasks and domains. We exploit this to；the Foundation AI models, trained on large；diverse datasets, Department of Informatics, University of Oslo, Norway | 基于基础AI模型与开放数据，构建可扩展的太阳能光伏设施识别与功率估算框架 | [#462](https://github.com/thinson/RS-PaperClaw/issues/462) |
| [20260504] Open-access model for detecting openly dumped dispersed municipal solid waste from crowdsourced UAV imagery in Sub-Saharan Africa | Knoblauch Steffen, Ram Kumar Muthusamy, Luis M. A. Bettencourt, Velis Costas, Chrzanowski Pierre, Edward Charles Anderson, Masters Pete, Maholi Innocent, Inguane Antonio, Szamek Levi, Zipf Alexander | HeiGIT at Heidelberg University；Interdisciplinary Centre of Scientific Computing (IWR), Heidelberg University；GIScience Research Group, Heidelberg University；Urban Science Laboratory, Department of Ecology and Evolution, The University of Chicago；Santa Fe Institute；Complexity Science Hub；Imperial College London；Global Facility for Disaster Reduction and Recovery (GFDRR), World Bank；Humanitarian OpenStreetMap Team；Open Map Development Tanzania；Data4Moz | 面向撒哈拉以南非洲开发开源深度学习模型，从众源无人机影像中检测露天分散垃圾堆放点 | [#463](https://github.com/thinson/RS-PaperClaw/issues/463) |
| [20260504] Rethinking Electro-Optical Vision Foundation Models for Remote Sensing Retrieval: A Controlled Comparison with Generalist VFM | Park Hyobin, Seo Minseok, Choi Dong-Geol | ANTLAB；Korea Advanced Institute of Science and Technology (KAIST)；Hanbat National University | 系统对比电光视觉基础模型与通用VFM在遥感检索任务中的跨场景泛化能力差异 | [#464](https://github.com/thinson/RS-PaperClaw/issues/464) |
| [20260504] SlimDiffSR: Toward Lightweight and Efficient Remote Sensing Image Super-Resolution via Diffusion Model Distillation | Wang Ce, Hu Zhenyu, Sun Wanjie | School of Remote Sensing and Information Engineering, Wuhan University | 提出扩散模型蒸馏策略SlimDiffSR，实现轻量高效的遥感影像超分辨率重建 | [#465](https://github.com/thinson/RS-PaperClaw/issues/465) |
| [20260504] RAFNet: Region-Aware Fusion Network for Pansharpening | Zhang Jianing, Zhou Zijian, Sun Kai | the College of Artificial domain responses of dynamically generated weights often；the School of Mathematics and Statistics, Xi’an Jiaotong to construct adaptive kernels within the Fourier domain, un- | 设计区域感知融合网络RAFNet，通过动态权重生成自适应傅里叶域核进行全色锐化 | [#466](https://github.com/thinson/RS-PaperClaw/issues/466) |
| [20260504] Cross-Polarization Fusion of VV AND VH SAR Observations for Improved Flood Mapping | Talreja Jagrati, Tewodros Syum Gebre, Leila Hashemi Beni | North Carolina A&T State University | 融合VV与VH极化SAR观测数据，提升深度学习洪水制图的空间精度与边界清晰度 | [#467](https://github.com/thinson/RS-PaperClaw/issues/467) |

## 🔎 观察

- 基础模型研究从'规模竞赛'转向'效率优化'，模型蒸馏与轻量化成为新焦点
- 遥感应用持续下沉至发展中国家本地化场景，众源数据与开放工具链降低技术门槛

---

Powered by OpenClaw🦞

---

# [20260502](./202605/20260502.md)
## 📌 今日概况

今日共检索候选论文 10 篇；关键词+LLM 智能匹配遥感交叉论文 4 篇；最终纳入日报 4 篇。

今日遥感AI研究呈现两大主线：一是智能体与仿真平台快速崛起，UAV搜救基准测试与地球观测交互环境相继发布；二是传感器融合持续深化，毫米波雷达与频域Transformer分别在农业低空感知与全色锐化领域取得进展。高校与产业界合作紧密，多模态大模型成为共性技术底座。

## ✨ 今日亮点

- ESARBench与EO-Gym双平台发布，推动遥感智能体从算法研究走向可交互、可评估的具身智能阶段
- CGFformer将K-means聚类与频域Transformer结合，为全色锐化引入自适应频率分离新范式
- 旋转毫米波雷达方案瞄准农业无人机地形感知，填补复杂农田环境下光学传感器失效的空白

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260502] CGFformer: Cluster-Guidance Frequency Transformer for Pansharpening | Zhou Zijian, Zhang Jianing, Sun Kai, Zhao Xiangyu, Zhang Chunxia, Cao Xiangyong | College of Artificial Intelligence, Xi'an Jiaotong University；School of Mathematics and Statistics, Xi'an Jiaotong University；School of Computer Science and Technology, Xi'an Jiaotong University | CGFformer提出聚类引导频域Transformer，通过K-means聚类实现自适应频率分离，优化全色锐化任务中的细节重建与光谱保真平衡。 | [#457](https://github.com/thinson/RS-PaperClaw/issues/457) |
| [20260502] ESARBench: A Benchmark for Agentic UAV Embodied Search and Rescue | Zhang Daoxuan, Chen Ping, Zhou Jianyi, Yang Shuo | Harbin Institute of Technology, Shenzhen | ESARBench构建首个面向无人机搜救的具身智能基准，集成多模态大模型评估框架，为灾难响应场景的智能体能力量化提供标准化工具。 | [#458](https://github.com/thinson/RS-PaperClaw/issues/458) |
| [20260502] Terrain Perception for Agricultural UAVs in Complex Farmland via Rotating mmWave Radar | Zhan Zhihao, Tao Le, Li Shaobin, Fang Chenxin, Yang Xingrui, Li Liang, Fan Rui, Ming Yuhang | School of Computer Science, Hangzhou Dianzi University；TopXGun Robotics；CARDC；College of Control Science and Engineering, Zhejiang University；College of Electronics and Information Engineering, Tongji University | 该研究设计旋转式毫米波雷达系统，解决农业无人机在扬尘、低光照复杂农田中的地形感知难题，支撑精准地形跟随飞行。 | [#459](https://github.com/thinson/RS-PaperClaw/issues/459) |
| [20260502] EO-Gym: A Multimodal, Interactive Environment for Earth Observation Agents | Ma Sai, Li Zhuang, Li Sichao, Xu Xinyue, Zhu Ruibiao, Boston Tony, John A. Taylor | The Australian National University；Royal Melbourne Institute of Technology；University of Sydney；The Hong Kong University of Science and Technology | EO-Gym打造多模态交互式地球观测智能体环境，支持视觉-语言-地理空间数据融合，为遥感大模型的在线决策与工具调用能力训练提供基础设施。 | [#460](https://github.com/thinson/RS-PaperClaw/issues/460) |

## 🔎 观察

- 具身智能正成为遥感AI新焦点，从ESARBench的搜救任务到EO-Gym的通用平台，学术社区开始系统性构建评估体系而非单一算法
- 毫米波雷达与农业场景的结合揭示低空经济基础设施的技术缺口，传统光学感知在复杂环境下的鲁棒性替代方案值得持续关注

---

Powered by OpenClaw🦞

---

# [20260501](./202605/20260501.md)
## 📌 今日概况

今日共检索候选论文 3 篇；关键词+LLM 智能匹配遥感交叉论文 3 篇；最终纳入日报 2 篇。

今日遥感AI研究聚焦两大方向：一是基础模型在气溶胶光学厚度反演中的创新应用，利用PACE卫星高光谱数据探索Vision Transformer的潜力；二是生成式AI技术在遥感影像超分辨率重建中的新进展，Flow Matching方法为Sentinel-2数据增强提供了新思路。

## ✨ 今日亮点

- 基础AI模型首次应用于PACE卫星气溶胶光学厚度估算，拓展高光谱遥感应用边界
- Flow Matching生成模型引入Sentinel-2超分辨率任务，为扩散模型提供高效替代方案
- 跨机构合作凸显遥感AI研究的多学科融合趋势，涵盖大气科学与精准农业领域

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260501] Foundation AI Models for Aerosol Optical Depth Estimation from PACE Satellite Data | Zahid Hassan Tushar, Purushotham Sanjay | University of Maryland, Baltimore County | 该研究基于PACE卫星高光谱数据，构建Vision Transformer基础模型实现气溶胶光学厚度精准估算。 | [#454](https://github.com/thinson/RS-PaperClaw/issues/454) |
| [20260501] Flow matching for Sentinel-2 super-resolution: implementation, application, and implications | Hester Dakota, Vitor S. Martins, Lucas B. Ferreira, Thainara M. A. Lima, Juliana A. Araújo | Department of Agricultural and Biological Engineering, Mississippi State University；North Mississippi Research and Extension Center, Mississippi State University | 该研究将Flow Matching生成模型应用于Sentinel-2影像超分辨率，系统评估其实现细节与应用效果。 | [#455](https://github.com/thinson/RS-PaperClaw/issues/455) |

## 🔎 观察

- 基础模型向地球科学专用领域渗透，高光谱卫星数据成为新的模型训练与验证资源
- 扩散模型替代方案在遥感影像生成任务中受关注，计算效率与重建质量的权衡成为关键考量

---

Powered by OpenClaw🦞

---
