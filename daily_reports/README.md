# Daily Reports

最近三天日报（最新在前）：

# [20260324](./202603/20260324.md)
## 📌 今日概况

今日共检索候选论文 13 篇；关键词+LLM 智能匹配遥感交叉论文 6 篇；最终纳入日报 6 篇。

今日遥感AI研究呈现多路径创新态势：基础模型层面探索模型权重融合而非数据驱动的表征学习；应用层面覆盖光伏设施普查、雪崩灾害监测等垂直场景；技术层面持续深化对比学习、时序建模与不确定性量化等核心方法。SAR与光学影像协同、检索增强生成等跨技术融合趋势显著。

## ✨ 今日亮点

- GeoSANE开创模型权重融合新范式，无需原始数据即可学习地理空间表征
- 检索增强生成技术首次应用于卫星影像光伏设施自动清分与电网规划
- LSTM-UNet与SAR深度学习双轨推进时序变化检测技术边界

## 🗂 今日文章列表

| 标题 | 作者 | 一句话概括 | Issue |
|---|---|---|---|
| [20260324] GeoSANE: Learning Geospatial Representations from Models, Not Data | Hanna Joelle, Falk Damian, Stella X. Yu, Borth Damian | GeoSANE提出从神经网络权重而非原始数据中学习地理空间表征，为基础模型融合开辟新路径。 | [#188](https://github.com/thinson/RS-PaperClaw/issues/188) |
| [20260324] Dual Contrastive Network for Few-Shot Remote Sensing Image Scene Classification | Ji Zhong, Hou Liyuan, Wang Xuan, Wang Gang, Pang Yanwei | 双对比网络通过原型与实例级对比学习，提升遥感场景小样本分类的泛化性能。 | [#189](https://github.com/thinson/RS-PaperClaw/issues/189) |
| [20260324] Retrieval-Guided Photovoltaic Inventory Estimation from Satellite Imagery for Distribution Grid Planning | Guo Muhao, Mai Lihao, Blasch Erik, Parol Jafarali, Rakan Turki et al. | 检索增强生成框架结合卫星影像与外部知识库，实现配电网规划所需的光伏设施精准估算。 | [#190](https://github.com/thinson/RS-PaperClaw/issues/190) |
| [20260324] L-UNet: An LSTM Network for Remote Sensing Image Change Detection | Sun Shuting, Mu Lin, Wang Lizhe, Liu Peng | L-UNet将LSTM嵌入UNet编码器，增强遥感影像变化检测的时序特征建模能力。 | [#191](https://github.com/thinson/RS-PaperClaw/issues/191) |
| [20260324] Predictive Photometric Uncertainty in Gaussian Splatting for Novel View Synthesis | Chamuditha Jayanga Galappaththige, Gottwald Thomas, Stehr Peter, Heinert Edgar, Suenderhauf Niko et al. | 高斯溅射光度不确定性预测方法，为三维重建新视角合成提供可靠性量化。 | [#192](https://github.com/thinson/RS-PaperClaw/issues/192) |
| [20260324] Large-Scale Avalanche Mapping from SAR Images with Deep Learning-based Change Detection | Gatti Mattia, Mariani Alberto, Gallo Ignazio, Monti Fabiano | 深度学习SAR变化检测网络实现大范围雪崩制图，支撑灾害应急响应与风险评估。 | [#193](https://github.com/thinson/RS-PaperClaw/issues/193) |

## 🔎 观察

- 模型权重融合（GeoSANE）与检索增强生成（RAG）代表遥感AI向'数据高效'与'知识驱动'双轨演进，降低对标注数据的依赖。
- 时序变化检测呈现架构分化：光学影像倾向LSTM-UNet时序建模，SAR数据则依托深度变化检测网络，模态特性驱动方法选择。

---

Powered by OpenClaw🦞

---

# [20260323](./202603/20260323.md)
## 📌 今日概况

今日共检索候选论文 19 篇；关键词+LLM 智能匹配遥感交叉论文 13 篇；最终纳入日报 13 篇。

今日遥感AI研究呈现三大趋势：一是跨视角地理定位与UAV导航技术持续升温，多篇论文聚焦实时定位与无GPS环境应用；二是基础模型可信度与自监督学习成为热点，光谱掩码与物理约束方法受关注；三是三维重建与立体匹配技术深化，NeRF与深度学习融合卫星影像处理流程。智能体工具创建与扩散模型分辨率增强亦具亮点。

## ✨ 今日亮点

- 跨视角地理定位技术突破：两篇论文分别从迭代流预测与视觉导航角度推进实时精确定位
- 遥感智能体进化：OpenEarth-Agent实现从工具调用到工具创建的自主能力跃迁
- 光谱可信学习：SpecTM提出光谱靶向掩码策略，增强基础模型物理可信度

## 🗂 今日文章列表

| 标题 | 作者 | 一句话概括 | Issue |
|---|---|---|---|
| [20260323] Riverine Land Cover Mapping through Semantic Segmentation of Multispectral Point Clouds | Thurachen Sopitta, Taher Josef, Lehtomäki Matti, Matikainen Leena, Blåfield Linnea et al. | 提出多光谱点云语义分割方法，实现河流沿岸土地覆盖精细制图 | [#174](https://github.com/thinson/RS-PaperClaw/issues/174) |
| [20260323] Beyond Matching to Tiles: Bridging Unaligned Aerial and Satellite Views for Vision-Only UAV Navigation | Liu Kejia, Zhou Haoyang, Xu Ruoyu, Wang Peicheng, Song Mingli et al. | 构建无需GPS的无人机视觉导航框架，桥接航拍与卫星影像视角差异 | [#175](https://github.com/thinson/RS-PaperClaw/issues/175) |
| [20260323] OpenEarth-Agent: From Tool Calling to Tool Creation for Open-Environment Earth Observation | Zhao Sijie, Liu Feng, Zhang Xueliang, Chen Hao, Gu Xinyu et al. | 开发开放环境地球观测智能体，支持自主工具创建与调用 | [#176](https://github.com/thinson/RS-PaperClaw/issues/176) |
| [20260323] SpecTM: Spectral Targeted Masking for Trustworthy Foundation Models | Syed Usama Imtiaz, Mitra Nasr Azadani, Alamdari Nasrin | 设计光谱靶向掩码策略，提升遥感基础模型可信度与物理一致性 | [#177](https://github.com/thinson/RS-PaperClaw/issues/177) |
| [20260323] GeoFlow: Real-Time Fine-Grained Cross-View Geolocalization via Iterative Flow Prediction | Ayesh Abu Lehyeh, Zhang Xiaohan, Arrabi Ahmad, Sultani Waqas, Chen Chen et al. | 通过迭代流预测实现实时细粒度跨视角地理定位，适用于拒止环境 | [#178](https://github.com/thinson/RS-PaperClaw/issues/178) |
| [20260323] SatGeo-NeRF: Geometrically Regularized NeRF for Satellite Imagery | Wagner Valentin, Bullinger Sebastian, Arens Michael, Stiefelhagen Rainer | 引入几何正则化约束，改进卫星影像NeRF三维重建与深度估计 | [#179](https://github.com/thinson/RS-PaperClaw/issues/179) |
| [20260323] A Latent Representation Learning Framework for Hyperspectral Image Emulation in Remote Sensing | Chedly Ben Azizi, Guilloteau Claire, Roussel Gilles, Puigt Matthieu | 基于变分自编码器学习潜层表示，实现高光谱图像仿真生成 | [#180](https://github.com/thinson/RS-PaperClaw/issues/180) |
| [20260323] Deep S2P: Integrating Learning Based Stereo Matching Into the Satellite Stereo Pipeline | Masquil Elías, Ehret Thibaud, Musé Pablo, Facciolo Gabriele | 将深度学习立体匹配集成至卫星立体处理流程，优化数字表面模型生产 | [#181](https://github.com/thinson/RS-PaperClaw/issues/181) |
| [20260323] SHARP: Spectrum-aware Highly-dynamic Adaptation for Resolution Promotion in Remote Sensing Synthesis | Zhao Bingxuan, Zhou Qing, Yang Chuang, Wang Qi | 提出频谱感知动态适配机制，结合旋转位置编码提升遥感图像分辨率 | [#182](https://github.com/thinson/RS-PaperClaw/issues/182) |
| [20260323] Rethinking SAR ATR: A Target-Aware Frequency-Spatial Enhancement Framework with Noise-Resilient Knowledge Guidance | Lin Yansong, Cheng Zihan, Wang Jielei, Lua Guoming, Cui Zongyong | 构建频域-空域联合增强框架，引入噪声鲁棒知识蒸馏改进SAR目标识别 | [#183](https://github.com/thinson/RS-PaperClaw/issues/183) |
| [20260323] Evolutionary Biparty Multiobjective UAV Path Planning: Problems and Empirical Comparisons | Chen Kesheng, Luo Wenjian, Lin Xin, Song Zhen, Chang Yatong | 设计进化双目标优化算法，解决多目标无人机路径规划问题 | [#184](https://github.com/thinson/RS-PaperClaw/issues/184) |
| [20260323] Unregistered Spectral Image Fusion: Unmixing, Adversarial Learning, and Recoverability | Song Jiahui, Shrestha Sagar, Fu Xiao | 融合解混与对抗学习，实现未配准多光谱与高光谱图像融合超分 | [#185](https://github.com/thinson/RS-PaperClaw/issues/185) |
| [20260323] EpiMask: Leveraging Epipolar Distance Based Masks in Cross-Attention for Satellite Image Matching | Deshmukh Rahul, Chauhan Aditya, Kak Avinash | 利用极线距离掩码改进交叉注意力机制，提升卫星影像匹配精度 | [#186](https://github.com/thinson/RS-PaperClaw/issues/186) |

## 🔎 观察

- 跨视角地理定位研究密集涌现，反映无人机自主导航与拒止环境应用的迫切需求，技术路线从特征匹配向端到端流预测演进
- 基础模型研究开始关注光谱物理约束与可信度问题，标志着遥感AI从性能优先向可解释、可信赖方向转型

---

Powered by OpenClaw🦞

---

# [20260322](./202603/20260322.md)
## 📌 今日概况

今日共检索候选论文 5 篇；关键词+LLM 智能匹配遥感交叉论文 2 篇；最终纳入日报 2 篇。

今日遥感AI研究聚焦视觉语言模型与空间智能的深度融合。道路提取任务引入细粒度层级分类与VLM技术，无人机导航则探索几何引导的跨模态表征对齐，体现从静态地物识别向动态环境理解的范式演进。

## ✨ 今日亮点

- 大规模道路数据集支撑VLM细粒度层级分类，提升路网语义理解能力
- 几何引导的表征对齐机制优化无人机视觉语言导航性能
- 跨模态空间推理成为城市环境智能体研究的核心方向

## 🗂 今日文章列表

| 标题 | 作者 | 一句话概括 | Issue |
|---|---|---|---|
| [20260322] A Large-Scale Remote Sensing Dataset and VLM-based Algorithm for Fine-Grained Road Hierarchy Classification | Han Ting, Xie Xiangyi, Chen Yiping, Du Yumeng, Ma Jin et al. | 论文构建大规模遥感数据集，提出基于视觉语言模型的道路细粒度层级分类方法，实现路网语义层次化解析。 | [#171](https://github.com/thinson/RS-PaperClaw/issues/171) |
| [20260322] SpatialFly: Geometry-Guided Representation Alignment for UAV Vision-and-Language Navigation in Urban Environments | Jiang Wen, Huang Kangyao, Wang Li, Xu Wang, Fan Wei et al. | 论文提出SpatialFly框架，通过几何引导的表征对齐机制，增强无人机在城市环境中的视觉语言导航能力。 | [#172](https://github.com/thinson/RS-PaperClaw/issues/172) |

## 🔎 观察

- VLM正从通用视觉任务向遥感垂直领域渗透，层级化语义标注或成为下一代道路数据集标配
- 无人机导航研究从端到端感知转向显式空间推理，几何先验与语言指令的联合建模值得持续关注

---

Powered by OpenClaw🦞

---
