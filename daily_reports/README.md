# Daily Reports

最近三天日报（最新在前）：

# [20260923](./202609/20260923.md)
## 📌 今日概况

今日共检索候选论文 24 篇；关键词+LLM 智能匹配遥感交叉论文 17 篇；最终纳入日报 17 篇。

今日研究聚焦遥感基础模型评测与多模态理解。多篇工作构建基准，覆盖物理退化、高光谱解混与无人机巡检，强调真实退化与分辨率公平性。视觉语言模型向统一嵌入、自然语言交互与超高分主动聚焦发展。变化检测、红外复原、SAR ATR等任务引入弱监督、解耦与频域增强。合成数据与几何定位继续支撑三维重建和GNSS拒止导航。

## ✨ 今日亮点

- 基础模型评测密集出现，强调物理退化与分辨率公平
- 视觉语言模型向统一嵌入和自然语言交互演进
- 弱监督与解耦学习用于变化检测和红外复原

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260923] RSPDBench: Benchmarking Vision Foundation Models on Earth Observation Tasks Under Physically Grounded Remote-Sensing Product Degradations | Tanjim Bin Faruk, Khondaker Masfiq Reza, Pallickara Shrideep, Sangmi Lee Pallickara | Colorado State University | 构建物理退化下地球观测任务的视觉基础模型基准，评估鲁棒性。 | [#1323](https://github.com/thinson/RS-PaperClaw/issues/1323) |
| [20260923] Tackling fluffy clouds: robust agricultural field boundary delineation from Sentinel-1 and Sentinel-2 satellite image time series | Foivos I. Diakogiannis, Zhou Zheng-Shu, Wang Jeff, Mata Gonzalo, Henry Dave, Lawes Roger, Parker Amy, Caccetta Peter, Furby Suzanne, Ibata Rodrigo, Hlinka Ondrej, Richetti Jonathan, Batchelor Kathryn, Herrmann Chris, Toovey Andrew, Taylor John | University of Strasbourg, France；Australian National University, School of Computing, ACT, Australia | 利用Sentinel-1/2时间序列与3D视觉Transformer，实现多云区农田边界稳健提取。 | [#1333](https://github.com/thinson/RS-PaperClaw/issues/1333) |
| [20260923] Strip Convolution and Direction-Aware Exclusion Loss for Oriented Ship Detection | Chen Bin, Liu Yuanyuan, Yang Peng, Lu Chao | School of Information and Software Engineering, East China Jiaotong University, Nanchang 330013, China；Jiangxi Vocational University of Foreign Studies, Nanchang 330099, China | 提出条带卷积与方向感知排除损失，抑制有向舰船检测重复框。 | [#1334](https://github.com/thinson/RS-PaperClaw/issues/1334) |
| [20260923] Breaking Weather-Content Coupling: Type-Severity Guided Progressive Disentanglement for All-in-One Infrared Restoration | Wang Xinyao, He Lijun, Ren Zhihan, Li Fan | Shaanxi Key Laboratory of Deep Space Exploration Intelligent Information Technology, School of Information and Communications Engineering, Xi’an；Jiaotong University, Xi’an, 710049, Shaanxi, China | 类型-严重度引导渐进解耦，实现红外图像全天候一体化复原。 | [#1335](https://github.com/thinson/RS-PaperClaw/issues/1335) |
| [20260923] SatUnreal: A High-Precision Synthetic Dataset for Satellite Stereo Matching via Unreal Engine | Kim Han-Gyeol, Park JaeWan, Park Junmin, Kwon Darongsae | To address these issues, research on synthetic data utiliz- | 基于虚幻引擎构建高精度卫星立体匹配合成数据集，含遮挡标签。 | [#1336](https://github.com/thinson/RS-PaperClaw/issues/1336) |
| [20260923] Beyond Balanced Accuracy: A Resolution and Parity-Controlled Benchmark for Vision-Language and Vision-Only Defect Assessment in UAV Power-Line Inspection | Zhang Linghao, Xiang Siyu, Kuang Junwei, Yi Peiyu | State Grid Sichuan Electric Power Research Institute, Chengdu 610041, China；Power System Security and Operation Key Laboratory of Sichuan Province | 面向无人机电力线巡检，构建分辨率与类别均衡受控的缺陷评估基准。 | [#1337](https://github.com/thinson/RS-PaperClaw/issues/1337) |
| [20260923] Copy-Move Forgery Detection and Question Answering for Remote Sensing Image | Zhang Ze, Zhao Enyuan, Niu Di, Nie Jie, Liang Xinyue, Huang Lei | the Faculty of Information Science and Engineering, Ocean University of China, Qingdao,, China；the Hangzhou Institute for Advanced Study, University of Chinese Academy of Sciences, Hangzhou,, China | 面向遥感图像复制-移动伪造检测，构建检测与问答联合任务。 | [#1338](https://github.com/thinson/RS-PaperClaw/issues/1338) |
| [20260923] VLM2GeoVec: Toward Universal Multimodal Embeddings for Remote Sensing | Emanuel Sánchez Aimar, Zhambulova Gulnaz, Fahad Shahbaz Khan, Xu Yonghao, Felsberg Michael | Linköping University；Mohamed bin Zayed University of AI | 提出VLM2GeoVec，学习遥感通用多模态嵌入以支持跨模态检索。 | [#1339](https://github.com/thinson/RS-PaperClaw/issues/1339) |
| [20260923] FSCE: A Target-Aware Frequency-Spatial Collaborative Enhancement Framework for Noise-Resilient SAR ATR | Lin Yansong, Cheng Zihan, Yang Ziyue, Wang Xinming, Wang Jielei, Lu Guoming, Cui Zongyong | the In- stitute of Automation, Chinese Academy of Sciences, China (wangxin- | 频率-空间协同增强框架，提升SAR自动目标识别抗斑点噪声能力。 | [#1340](https://github.com/thinson/RS-PaperClaw/issues/1340) |
| [20260923] From Change Captions to Change Detection: Semantic-Appearance Agreement Framework for Remote Sensing Change Detection | Qian Yuan, Ma Jie | School of Information Science and Technology, Beijing Foreign Studies University, Beijing, China ( | 利用变化描述作为弱监督，通过语义-外观一致性生成变化掩膜。 | [#1342](https://github.com/thinson/RS-PaperClaw/issues/1342) |
| [20260923] Geospatial embeddings detect old-growth forests but buffered spatial validation narrows their advantage over Sentinel features | Ratsakatika Thomas, Zotta Mihai, Keshav Srinivasan, Emily R. Lines | Department of Geography, University of Cambridge, Downing Place, Cambridge, CB2；Department of Computer Science and Technology, University of Cambridge | 地理空间嵌入可检测老龄林，但缓冲空间验证缩小其相对Sentinel特征优势。 | [#1343](https://github.com/thinson/RS-PaperClaw/issues/1343) |
| [20260923] Large-Scale Geometric Map-Based Localization of UAVs in GNSS-Denied Urban Environments | Terlizzi Garth, Fathian Kaveh | Department of Computer Science, Colorado School of Mines | GNSS拒止城市环境下，基于几何地图与建筑轮廓匹配实现无人机定位。 | [#1344](https://github.com/thinson/RS-PaperClaw/issues/1344) |
| [20260923] Benchmarking Hyperspectral Foundation Models for Hyperspectral Unmixing | Dabier Edgard, Kervazo Christophe, Gori Pietro, Tupin Florence | LTCI, Télécom Paris, Institut Polytechnique de Paris, Palaiseau, France；Despite this scarcity of annotated HSU images, researchers | 系统评测高光谱基础模型在解混任务中的表现，关注特征分辨率。 | [#1345](https://github.com/thinson/RS-PaperClaw/issues/1345) |
| [20260923] Spatial-Spectral Trade-offs in Metasurface-Based Snapshot Hyperspectral Imaging | Fitzpatrick Liam, Molesky Sean, Wang Kai | Department of Physics and McGill Quantum Centre, McGill University；rue University, Montréal, Québec H3 A 2 T8, Canada；Department of Engineering Physics, Polytechnique Montréal, Montréal, Québec H3 T 1 J4, Canada | 分析超表面快照高光谱成像中空间-光谱权衡关系。 | [#1346](https://github.com/thinson/RS-PaperClaw/issues/1346) |
| [20260923] Token Clustering and Semantic Sequence Mamba for Hyperspectral Image Classification | Zhu Yimin, Elahi Mahmood, Lincoln Linlin Xu | Department of Geomatics Engineering, University of Calgary, Canada (；Department of Electrical and Software Engineering, University of Calgary, Canada ( | 结合令牌聚类与语义序列Mamba，提升高光谱图像分类性能。 | [#1347](https://github.com/thinson/RS-PaperClaw/issues/1347) |
| [20260923] GeoNLI - A Natural Language Interpreter for Satellite Imagery | Gandhe Ashutosh, Rawat Anupam, Sethi Geet, Nasiruddin Kabir, Kotecha Madhav, Shah Panav, Sawarn Rakshit, Nayak Soumitra | Indian Institute of Technology, Bombay | GeoNLI构建卫星图像自然语言解释器，支持视觉定位与问答。 | [#1348](https://github.com/thinson/RS-PaperClaw/issues/1348) |
| [20260923] The Earth in One Gaze: Training-Free Active Focus for UHR Remote Sensing Understanding | Zhang Yao, Dai Pengyu, Guo Wei, Liang Jian, Song Jian, Ou Yafei, Chen Hongruixuan, Yokoya Naoto | Wuhan University；University of Tokyo | 免训练主动聚焦框架，面向超高分辨率遥感图像理解。 | [#1349](https://github.com/thinson/RS-PaperClaw/issues/1349) |

## 🔎 观察

- 评测类工作从单一精度转向物理退化与分辨率公平，推动基础模型可信评估。
- 视觉语言模型正从任务专用走向统一嵌入与免训练交互，降低标注依赖。

---

Powered by OpenClaw🦞

---

# [20260922](./202609/20260922.md)
## 📌 今日概况

今日共检索候选论文 7 篇；关键词+LLM 智能匹配遥感交叉论文 3 篇；最终纳入日报 3 篇。

今日三篇论文分别聚焦地球观测基础模型嵌入、开放提示遥感检测与三维重建。首篇验证年度嵌入对野火扰动的编码能力，推动简化火烧区制图；第二篇提出层次感知的开放提示检测框架，提升跨层级一致性；第三篇结合智能体与高斯泼溅实现可审计的城市DSM重建。整体趋势显示，遥感AI正从单一任务模型向可解释、可审计的基础表征与三维结构化理解演进。

## ✨ 今日亮点

- 年度地球观测嵌入可编码野火扰动，支持简化火烧区制图
- 层次感知开放提示检测提升遥感图像跨层级一致性
- 智能体与高斯泼溅结合实现可审计城市DSM重建

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260922] Annual Earth-observation embeddings encode wildfire disturbance and support simplified burned area mapping | Knezevic Jovana, Atzberger Clement, Feng Zhengpeng, Adam F. A. Pellegrini, Keshav Srinivasan, Coomes David | Conservation Research Institute, University of Cambridge, Cambridge, United Kingdom；Department of Plant Sciences, University of Cambridge, Cambridge, United Kingdom；Department of Computer Science and Technology, University of Cambridge, Cambridge, United Kingdom；Department of Earth System Science, Stanford University, Stanford, CA, USA | 验证年度地球观测嵌入能编码野火扰动，并支持简化火烧区制图流程。 | [#1329](https://github.com/thinson/RS-PaperClaw/issues/1329) |
| [20260922] Hi-OPD: Hierarchy-Aware Open-Prompt Detection for Remote Sensing Images | Hu Jinlong, Zhang Yi, Xia Zhiqi, Zhou Yikang, Ji Shunping | Wuhan University；Institute of Seismology, China Earthquake Administration | 提出层次感知开放提示检测框架，增强遥感图像跨层级一致性与负采样。 | [#1330](https://github.com/thinson/RS-PaperClaw/issues/1330) |
| [20260922] Agentic Building-Aware Satellite Gaussian Splatting for Auditable Urban DSM Reconstruction | Sun Wentao, Xu Zhengsen, Chen Yiping, John S. Zelek, Li Jonathan | University of Waterloo, Department of Systems Design Engineering, Waterloo, Canada；University of Calgary, Department of Geomatics Engineering, Calgary, Canada；Sun Yat-sen University, School of Geospatial Engineering and Science, Zhuhai, China | 融合智能体与卫星高斯泼溅，实现建筑感知且可审计的城市DSM重建。 | [#1331](https://github.com/thinson/RS-PaperClaw/issues/1331) |

## 🔎 观察

- 基础模型嵌入正从通用表征走向特定扰动编码，降低下游制图对标注的依赖。
- 开放提示检测与三维重建均强调可解释性，反映遥感AI向可审计方向演进。

---

Powered by OpenClaw🦞

---

# [20260921](./202609/20260921.md)
## 📌 今日概况

今日共检索候选论文 11 篇；关键词+LLM 智能匹配遥感交叉论文 3 篇；最终纳入日报 3 篇。

今日研究趋势聚焦于遥感领域的轻量化、基础模型与跨模态定位。三篇论文分别针对SAR舰船检测的模型压缩、森林点云的基础模型构建以及基于音频的无人机定位，体现了从专用检测到通用表征、从视觉到多模态融合的演进。其中知识蒸馏与剪枝结合、自监督学习用于点云、强化学习处理时序对应，均反映了提升效率与泛化能力的共同目标。

## ✨ 今日亮点

- DTKDP框架结合双教师蒸馏与剪枝，实现轻量SAR舰船检测。
- 森林点云基础模型探索自监督学习与语义分割。
- 音频无人机定位引入强化学习实现自适应时序对应。

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260921] DTKDP: A Dual Teacher Knowledge Distillation and Pruning Framework for Lightweight Oriented SAR Ship Detection | Li Yuming, Zhang Fan, Alin M. Achim | Visual Information Labs, University of Bristol, Bristol BS1 | 提出双教师知识蒸馏与剪枝框架，用于轻量化定向SAR舰船检测。 | [#1325](https://github.com/thinson/RS-PaperClaw/issues/1325) |
| [20260921] Toward a foundation model for forest point clouds | Yue Yuanwen, Puliti Stefano, Robert Damien, Topaloğlu Atakan, Xiang Binbin, Wielgosz Maciej, Jan Dirk Wegner, Astrup Rasmus, Rupprecht Christian, Schindler Konrad | University of Oxford；Norwegian Institute of Bioeconomy Research (NIBIO)；University of Zurich | 探索森林点云基础模型，结合自监督学习与语义分割。 | [#1326](https://github.com/thinson/RS-PaperClaw/issues/1326) |
| [20260921] Audio-based UAV Localization with Adaptive Temporal Correspondence via Reinforcement Learning | Lei Haoxiang, Feng Mingzheng, Wang Daotong, Yuan Shenghai | at the window center to reduce motion-induced mismatch | 利用强化学习实现音频无人机定位中的自适应时序对应。 | [#1327](https://github.com/thinson/RS-PaperClaw/issues/1327) |

## 🔎 观察

- 轻量化与基础模型并行发展，分别应对边缘部署与通用表征需求。
- 多模态与自监督方法正渗透至遥感细分任务，提升鲁棒性。

---

Powered by OpenClaw🦞

---
