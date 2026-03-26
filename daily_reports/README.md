# Daily Reports

最近三天日报（最新在前）：

# [20260325](./202603/20260325.md)
## 📌 今日概况

今日共检索候选论文 9 篇；关键词+LLM 智能匹配遥感交叉论文 7 篇；最终纳入日报 7 篇。

今日遥感AI研究呈现多模态融合与可解释性并重的趋势。时序分析持续深化，Transformer架构在卫星影像时间序列处理中占据主导；高光谱成像技术向月球探测与不确定性量化拓展；同时，空间-光谱联合建模与专家混合机制成为提升分类精度的关键路径。

## ✨ 今日亮点

- 多任务学习结合空间上下文提升Sentinel-2时序农业系统识别能力
- Aitchison几何引入贝叶斯高光谱解混实现不确定性量化
- 动态空间-光谱专家路由机制优化高光谱图像分类性能

## 🗂 今日文章列表

| 标题 | 作者 | 一句话概括 | Issue |
|---|---|---|---|
| [20260325] The role of spatial context and multitask learning in the detection of organic and conventional farming systems based on Sentinel-2 time series | Hemmerling Jan, Schwieder Marcel, Rufin Philippe, Thomas Leon-Friedrich, Tulbure Mirela et al. | 该研究探索空间上下文与多任务学习在基于Sentinel-2时序的有机与常规农业系统检测中的作用。 | [#195](https://github.com/thinson/RS-PaperClaw/issues/195) |
| [20260325] Connecting Meteorite Spectra to Lunar Surface Composition Using Hyperspectral Imaging and Machine Learning | Fatemeh Fazel Hesar, Raouf Mojtaba, Chegeni Amirmohammad, Soltani Peyman, Foing Bernard et al. | 利用高光谱成像与机器学习建立陨石光谱与月球表面成分的关联，实现矿物填图。 | [#196](https://github.com/thinson/RS-PaperClaw/issues/196) |
| [20260325] Combi-CAM: A Novel Multi-Layer Approach for Explainable Image Geolocalization | Faget David, José Luis Lisani, Colom Miguel | 提出Combi-CAM多层方法，为基于CNN的图像地理定位提供可解释性分析。 | [#197](https://github.com/thinson/RS-PaperClaw/issues/197) |
| [20260325] Comparative analysis of dual-form networks for live land monitoring using multi-modal satellite image time series | Dumeur Iris, Anger Jérémy, Facciolo Gabriele | 对比分析双形式网络在多模态卫星影像时间序列实时土地监测中的应用。 | [#198](https://github.com/thinson/RS-PaperClaw/issues/198) |
| [20260325] LGEST: Dynamic Spatial-Spectral Expert Routing for Hyperspectral Image Classification | Wen Jiawen, Qiu Suixuan, Luo Zihang, Yang Xiaofei, Shi Haotian | LGEST方法通过动态空间-光谱专家路由机制实现高光谱图像分类。 | [#199](https://github.com/thinson/RS-PaperClaw/issues/199) |
| [20260325] DB SwinT: A Dual-Branch Swin Transformer Network for Road Extraction in Optical Remote Sensing Imagery | He Zongyang, Yang Xiangli, Gao Xian, Wang Zhiguo | 构建双分支Swin Transformer网络DB SwinT用于光学遥感影像道路提取。 | [#200](https://github.com/thinson/RS-PaperClaw/issues/200) |
| [20260325] Aitchison Geometry on the Simplex for Uncertainty Quantification in Bayesian Hyperspectral Image Unmixing | Blondel Hector, Drumetz Lucas, Chonavel Thierry | 将Aitchison几何引入单纯形空间，实现贝叶斯高光谱解混中的不确定性量化。 | [#201](https://github.com/thinson/RS-PaperClaw/issues/201) |

## 🔎 观察

- Transformer变体（Swin、线性注意力）正快速渗透遥感时序与分割任务，架构同质化风险需关注
- 高光谱技术从地球观测向行星科学延伸，跨域知识迁移或成新增长点

---

Powered by OpenClaw🦞

---

# [20260324](./202603/20260324.md)
## 📌 今日概况

今日共检索候选论文 13 篇；关键词+LLM 智能匹配遥感交叉论文 6 篇；最终纳入日报 6 篇。

今日遥感AI研究呈现多技术路线并进态势：基础模型层面探索模型权重融合而非数据驱动学习；应用层面覆盖光伏设施普查、雪崩灾害监测等垂直场景；方法层面持续深化对比学习、LSTM时序建模与不确定性量化等核心技术。

## ✨ 今日亮点

- GeoSANE开创性地从神经网络权重空间学习地理表征，突破传统数据驱动范式
- 检索增强生成技术首次应用于卫星影像光伏设施清单估算，支撑配电网规划
- SAR影像深度学习变化检测实现大规模雪崩制图，拓展灾害遥感监测能力

## 🗂 今日文章列表

| 标题 | 作者 | 一句话概括 | Issue |
|---|---|---|---|
| [20260324] GeoSANE: Learning Geospatial Representations from Models, Not Data | Hanna Joelle, Falk Damian, Stella X. Yu, Borth Damian | GeoSANE提出从模型权重而非原始数据学习地理空间表征的新范式，为地理基础模型训练开辟替代路径。 | [#188](https://github.com/thinson/RS-PaperClaw/issues/188) |
| [20260324] Dual Contrastive Network for Few-Shot Remote Sensing Image Scene Classification | Ji Zhong, Hou Liyuan, Wang Xuan, Wang Gang, Pang Yanwei | 双对比网络通过全局-局部特征协同对比学习，提升小样本遥感场景分类的泛化性能。 | [#189](https://github.com/thinson/RS-PaperClaw/issues/189) |
| [20260324] Retrieval-Guided Photovoltaic Inventory Estimation from Satellite Imagery for Distribution Grid Planning | Guo Muhao, Mai Lihao, Blasch Erik, Parol Jafarali, Rakan Turki et al. | 检索增强生成框架结合卫星影像与外部知识库，实现分布式光伏设施的精准清估算。 | [#190](https://github.com/thinson/RS-PaperClaw/issues/190) |
| [20260324] L-UNet: An LSTM Network for Remote Sensing Image Change Detection | Sun Shuting, Mu Lin, Wang Lizhe, Liu Peng | L-UNet将LSTM嵌入UNet架构，强化遥感影像变化检测的时序特征建模能力。 | [#191](https://github.com/thinson/RS-PaperClaw/issues/191) |
| [20260324] Predictive Photometric Uncertainty in Gaussian Splatting for Novel View Synthesis | Chamuditha Jayanga Galappaththige, Gottwald Thomas, Stehr Peter, Heinert Edgar, Suenderhauf Niko et al. | 高斯溅射光度不确定性预测方法，为神经辐射场新视角合成提供可靠性量化。 | [#192](https://github.com/thinson/RS-PaperClaw/issues/192) |
| [20260324] Large-Scale Avalanche Mapping from SAR Images with Deep Learning-based Change Detection | Gatti Mattia, Mariani Alberto, Gallo Ignazio, Monti Fabiano | 基于SAR影像与深度学习的多时相变化检测，实现山区大范围雪崩事件的自动化制图。 | [#193](https://github.com/thinson/RS-PaperClaw/issues/193) |

## 🔎 观察

- 模型权重空间学习（GeoSANE）代表基础模型训练的新方向，可能降低对海量标注数据的依赖
- 检索增强生成与遥感结合尚处早期，光伏设施估算案例显示其在结构化知识融合方面的潜力

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
