# Daily Reports

最近三天日报（最新在前）：

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

# [20260430](./202604/20260430.md)
## 📌 今日概况

今日共检索候选论文 15 篇；关键词+LLM 智能匹配遥感交叉论文 10 篇；最终纳入日报 8 篇。

今日遥感AI研究呈现多模态融合与高效架构两大主线。高光谱分类与超分辨率持续深化光谱-空间联合建模；扩散模型、对比学习等自监督范式向语义分割、表格数据等场景扩展；轻量化设计与预训练策略优化成为工程落地关键。

## ✨ 今日亮点

- 扩散模型Noise2Map实现语义分割与变化检测端到端统一框架
- 超光谱超分辨率引入频域动态注意力机制突破重建瓶颈
- 多源数据融合网络协同挖掘SAR、高光谱与LiDAR互补信息

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260430] Hyperspectral Image Classification via Efficient Global Spectral Supertoken Clustering | Liu Peifu, Xu Tingfa, Wang Jie, Chen Huan, Bai Huiyan, Li Jianan | Beijing Institute of Technology；Beijing Institute of Technology Chongqing Innovation Center；Key Laboratory of Photoelectronic Imaging Technology and System, Ministry of Education of China | 提出全局光谱超像素聚类方法，通过超令牌机制提升高光谱分类边界 delineation 效率。 | [#443](https://github.com/thinson/RS-PaperClaw/issues/443) |
| [20260430] Noise2Map: End-to-End Diffusion Model for Semantic Segmentation and Change Detection | Shibli Ali, Nascetti Andrea, Ban Yifang | KTH Royal Institute of Technology；Delft University of Technology | Noise2Map将扩散模型用于遥感语义分割与变化检测，实现噪声到地图的直接生成。 | [#446](https://github.com/thinson/RS-PaperClaw/issues/446) |
| [20260430] Multi-wavelength polarisation imaging with inverse designed metasurfaces | Sarah E. Dean, Li Neuton, Munro Josephine, Laudert Benjamin, Siefke Thomas, Ngo Quyet, Sharp Robert, Dragomir N. Neshev, Eilenberger Falk, Andrey A. Sukhorukov | ARC Centre of Excellence for Transformative Meta-Optical Systems (TMOS), Department of Electronic Materials Engineering, Research School of Physics, The Australian National University；Fraunhofer-Institute for Applied Optics and Precision Engineering IOF；Friedrich Schiller University Jena, Abbe Center of Photonics, Institute of Applied Physics；Ernst-Abbe-Hochschule Jena University of Applied Sciences；Research School of Astronomy & Astrophysics, The Australian National University | 逆设计超表面实现多波长偏振成像，为计算成像硬件提供新范式。 | [#447](https://github.com/thinson/RS-PaperClaw/issues/447) |
| [20260430] A generalised pre-training strategy for deep learning networks in semantic segmentation of remotely sensed images | Fang Yuan, Cai Yuanzhi, Aryal Jagannath, Zhu Qinfeng, Huang Hong, Zhang Cheng, Fan Lei | Xi'an Jiaotong-Liverpool University；CSIRO Mineral Resources；The University of Melbourne | 提出通用预训练策略缓解遥感语义分割中的域间隙问题，提升跨场景泛化能力。 | [#448](https://github.com/thinson/RS-PaperClaw/issues/448) |
| [20260430] Robust Lightweight Crack Classification for Real-Time UAV Bridge Inspection | Li Wei, Li Haisheng, Li Weijie, Wang Jiandong, Ma Kaichen, Yang Luming | Bay Area Super Bridge Maintenance Technology Center, Guangdong Provincial Highway Construction Co., Ltd.；Guangdong AIHISUN Technology Co., Ltd. | 面向无人机桥梁巡检的轻量级裂缝分类网络，兼顾实时性与鲁棒性需求。 | [#449](https://github.com/thinson/RS-PaperClaw/issues/449) |
| [20260430] ZAYAN: Disentangled Contrastive Transformer for Tabular Remote Sensing Data | Al Zadid Sultan Bin Habib, Tasnim Tanpia, Md. Ekramul Islam, Tabasum Muntasir | Lane Dept. of Computer Science and Electrical Engineering, West Virginia University；Dept. of Geology & Geography, West Virginia University；Department of Computer Science and Engineering, Green University of Bangladesh；Department of Computer Science and Engineering, Stamford University Bangladesh | ZAYAN解耦对比Transformer专为遥感表格数据设计，拓展自监督学习应用边界。 | [#450](https://github.com/thinson/RS-PaperClaw/issues/450) |
| [20260430] Spectral Dynamic Attention Network for Hyperspectral Image Super-Resolution | Zhang Tengya, Gao Feng, Qi Lin, Dong Junyu, Du Qian | the Sanya Oceanographic Institution, Ocean Univer- conventional FFN follows a simple linear；State Key Laboratory of spectral；the Department of Electrical and Computer Engineering, recover fine-grained details and leads to suboptimal recon- | 频域动态注意力网络针对高光谱超分辨率，通过通道稀疏注意力捕获光谱相关性。 | [#451](https://github.com/thinson/RS-PaperClaw/issues/451) |
| [20260430] Representative Spectral Correlation Network for Multi-source Remote Sensing Image Classification | Gong Chuanzheng, Gao Feng, Lin Junyan, Dong Junyu, Du Qian | the Department of Computing, The Hong Kong SAR/LiDAR data lacks sufficient spectral information, limit-；the Department of Electrical and Computer Engineering, ing its ability to distinguish objects with similar appearances；the State Key Laboratory of Physical Oceanography, Ocean University of China, Qingdao | 代表性光谱相关网络融合SAR、高光谱与LiDAR，解决多源遥感分类光谱选择难题。 | [#452](https://github.com/thinson/RS-PaperClaw/issues/452) |

## 🔎 观察

- 扩散模型正从生成任务向判别任务渗透，Noise2Map或预示遥感分割新范式。
- 高光谱研究密集涌现，光谱-空间联合建模与频域分析成为竞争焦点。

---

Powered by OpenClaw🦞

---
