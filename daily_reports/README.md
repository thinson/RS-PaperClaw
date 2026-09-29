# Daily Reports

最近三天日报（最新在前）：

# [20260925](./202609/20260925.md)
## 📌 今日概况

今日共检索候选论文 16 篇；关键词+LLM 智能匹配遥感交叉论文 7 篇；最终纳入日报 7 篇。

今日论文聚焦遥感数据的高效表征、跨模态转换与智能体应用。高光谱视频压缩引入隐式神经表示，波段选择稳定性研究关注语义分割可靠性；扩散模型与流匹配被用于数字表面模型增强和SAR到光学图像翻译，强调多模态条件与单步生成。同时，面向超高分辨率影像的工具路由智能体、长时无人机视觉语言导航基准以及人机回环地理标注系统，反映出遥感AI向自动化、交互式与可扩展数据集构建方向演进。

## ✨ 今日亮点

- 隐式神经表示拓展至高光谱视频压缩，兼顾时空谱冗余。
- 流匹配与对比学习结合，实现单步SAR到光学图像翻译。
- 长时无人机视觉语言导航基准与工具路由智能体并进。

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260925] Implicit Neural Representation for Hyperspectral Video Compression | Scalera Alfredo, Murray Paul, Zabalza Jaime | University of Strathclyde；Department of Electronic | 提出隐式神经表示方法用于高光谱视频压缩，以Bjøntegaard Delta评估压缩效率。 | [#1360](https://github.com/thinson/RS-PaperClaw/issues/1360) |
| [20260925] Band-Selection Stability and Semantic Segmentation Performance: A Study on Hyperspectral City | Li Jiarong, Imad Ali Shah, Ward Enda, Glavin Martin, Jones Edward, Deegan Brian | School of Engineering and Ryan Institute, University of Galway, Ireland | 研究高光谱城市语义分割中波段选择稳定性与分割性能的关系。 | [#1363](https://github.com/thinson/RS-PaperClaw/issues/1363) |
| [20260925] Enhancing Photogrammetric Digital Surface Models with Pretrained Diffusion Models and Multimodal Conditioning | Lorentz Antoine, May Stéphane, Bellet Valentine, Derksen Dawa, Nespoulous Bastien | Centre National d’Études Spatiales (CNES) | 利用预训练扩散模型和多模态条件增强摄影测量数字表面模型。 | [#1364](https://github.com/thinson/RS-PaperClaw/issues/1364) |
| [20260925] WeaveAgent: A Two-Stage Tool-Routing Agent for Ultra-High-Resolution Remote Sensing Imagery | Pang Zhongyu | Department of Electronics, National University of Defense Technology | 提出两阶段工具路由智能体，处理超高分辨率遥感影像的视觉令牌压缩与调用。 | [#1365](https://github.com/thinson/RS-PaperClaw/issues/1365) |
| [20260925] ContraFM-S2O: Flow Matching-Based One-step SAR-to-Optical Image Translation Model with Contrastive Learning | Yu Mingqian, Chiang Wei-kuan, Wang Qiurui, Zhao Peilin | Institute of Automation, Chinese Academy of Sciences, Beijing, China；Department of Computer Science, The University of Manchester, Manchester, UK；Institute of Artificial Intelligence in Sports, Capital University of Physical Education And Sports, Beijing, China；School of Artificial Intelligence, Shanghai Jiao Tong University, Shanghai, China | 结合流匹配与对比学习，构建单步SAR到光学图像翻译模型。 | [#1366](https://github.com/thinson/RS-PaperClaw/issues/1366) |
| [20260925] SatNav: A Scalable Benchmark for Long-Horizon UAV Vision-Language Navigation from Satellite Imagery | Jiang Jiajun, Hua Chunliang, Chen Zichun, Wu Yanxing, Yang Zeyuan, Song Jie, Hu Xiao | The Hong Kong University of Science and Technology (Guangzhou)；Low Altitude Space Economy Research Center；International Digital Economy Academy (IDEA)；The Hong Kong University of Science and Technology | 基于卫星影像构建可扩展长时无人机视觉语言导航基准SatNav。 | [#1367](https://github.com/thinson/RS-PaperClaw/issues/1367) |
| [20260925] Human-in-the-Loop Geospatial Annotation for Rapid Dataset Construction in Field-Deployed UAV Systems | Masters Morgan, Korycki Adam, Bender Nikolaas, T. Luca Altaffer, Josephson Colleen, McGuire Steve | Department of Electrical and Computer Engineering, University of California Santa Cruz；time-consuming and costly [9], forcing research communities to rely on large-scale, internet-hosted；As a consequence, researchers and practitioners working in specialized domains—such as field | 设计人机回环地理标注流程，支持野外部署无人机系统快速构建数据集。 | [#1368](https://github.com/thinson/RS-PaperClaw/issues/1368) |

## 🔎 观察

- 高光谱与SAR等遥感模态的压缩和转换研究，正从重建精度转向下游任务稳定性与效率。
- 智能体与基准数据集建设同步推进，表明遥感AI开始重视长时程交互与真实场景可扩展性。

---

Powered by OpenClaw🦞

---

# [20260924](./202609/20260924.md)
## 📌 今日概况

今日共检索候选论文 19 篇；关键词+LLM 智能匹配遥感交叉论文 14 篇；最终纳入日报 14 篇。

今日遥感AI研究呈现三条主线：一是基础模型与嵌入的可解释性分析，如AlphaEarth城市表征压缩、EO嵌入地理位置信息恢复；二是面向边缘与高效推理的轻量化方法，包括VLM冗余剪枝、跨尺度蒸馏小目标检测；三是地理空间预测与不确定性建模，涵盖自主预测引擎、连续处理因果推断及隐式神经表示。此外，开放数据与基准构建持续活跃，涉及SAR视觉定位、无人机垃圾检测等应用。

## ✨ 今日亮点

- 基础模型嵌入分析成热点，关注城市表征偏差与地理位置信息泄露
- 边缘智能与轻量化推理受重视，VLM冗余剪枝和跨尺度蒸馏并行推进
- 地理空间预测向自主化与不确定性量化发展，隐式神经表示可调尺度

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260924] Open-access model for detecting openly dumped dispersed municipal solid waste from crowdsourced UAV imagery in Sub-Saharan Africa | Knoblauch Steffen, Ram Kumar Muthusamy, Luis M. A. Bettencourt, Velis Costas, Chrzanowski Pierre, Edward Charles Anderson, Masters Pete, Maholi Innocent, Inguane Antonio, Szamek Levi, Zipf Alexander | HeiGIT at Heidelberg University, Heidelberg, Germany；Interdisciplinary Centre of Scientific Computing (IWR), Heidelberg University, Heidelberg, Germany；GIScience Research Group, Heidelberg University, Heidelberg, Germany；Urban Science Laboratory, Department of Ecology and Evolution, The University of Chicago, Chicago, IL, USA；e Santa Fe Institute, Santa Fe, NM, USA；g Department of Civil and Environmental Engineering, Imperial College London, London, United Kingdom | 基于众包无人机影像的开放获取模型，用于检测撒哈拉以南非洲露天倾倒的分散城市固废。 | [#463](https://github.com/thinson/RS-PaperClaw/issues/463) |
| [20260924] Bringing Agentic Search to Earth Observation Data Discovery | Yu Minghan, Sun Youran, Yi Chugang, Wen Yixin, Yang Haizhao | Department of Mathematics Department of Mathematics Department of Mathematics；University of Maryland, College Park University of Maryland, College Park University of Maryland, College Park；College Park, MD, USA College Park, MD, USA College Park, MD, USA；School of Marine and Atmospheric Department of Mathematics；Sciences University of Maryland, College Park；Stony Brook University College Park, MD, USA；Stony Brook, NY, USA Department of Computer Science；College Park, MD, USA；NASA and its data centers hold thousands of geoscience datasets Earth-observation data discovery is less a problem of data scarcity | 将智能体搜索引入地球观测数据发现，利用大语言模型与知识图谱提升检索效率。 | [#833](https://github.com/thinson/RS-PaperClaw/issues/833) |
| [20260924] Planetary Prediction Engine: Autonomous Geospatial Prediction via Intelligent Data Selection and Foundation Model Embeddings | Ma Evelyn, Rama Kumar Pasumarthi, Shafin Kishwar, Sharma Mandar, Sun Mimi, Sadeghi Hamed, Dav M. Ebengo, Onesime Mbulayi, Judge Ciara, Solomakhin Rouslan, Wamburu John, Ogallo William, Walcott-Bryant Aisha, Chen Sanxing, Muslim Arbaaz, Mayer Yael, Ho Ronald, Lee Roy, Alcantara Ruth, ..., Shetty Shravya | Google Research；Institut National de Recherche Biomédicale, Democratic Republic of Congo；University of Oxford | 行星预测引擎通过智能数据选择与基础模型嵌入，实现自主地理空间预测。 | [#1183](https://github.com/thinson/RS-PaperClaw/issues/1183) |
| [20260924] OptiSAR-Net++: A Large-Scale Benchmark and Transformer-Free Framework for Cross-Domain Remote Sensing Visual Grounding | Tang Xiaoyu, Dong Jun, Cheng Jintao, Fan Rui | School of Electronics and Information Engineering, and Xingzhi College, South China Normal University, Foshan, China. (；Department of Electronic and Computer Engineering, Hong Kong University of Science and Technology, Hong Kong SAR, China. ( | OptiSAR-Net++构建大规模基准与无Transformer框架，用于跨域遥感视觉定位。 | [#1351](https://github.com/thinson/RS-PaperClaw/issues/1351) |
| [20260924] GeoDose-CP: Graph-Local Conformal Inference for Continuous-Treatment Earth Observation | Md Khalid Hasan Sakib, Datta Dristi, Paul Manoranjan, White Davina | Department of Computer Science and Engineering, Uttara University, Dhaka, Bangladesh (；School of Computing, Mathematics and Engineering, Charles Sturt University, Bathurst, NSW, Australia；School of Computing, Mathematics and Engineering, Charles Sturt University, Bathurst, NSW, Australia ( | GeoDose-CP提出图局部保形推断，面向连续处理地球观测的不确定性量化。 | [#1352](https://github.com/thinson/RS-PaperClaw/issues/1352) |
| [20260924] Passive LWIR Hyperspectral Ranging via Transmittance Extraction and Distance Alignment | Chen Zhihe, Fan Chen, Liu Shuo, Huang Xiaolin, He Yunze, He Xiaofeng, Zhang Lilian | College of Intelligence Science and Technology, National University of Defense Technology, Changsha, Hunan, China (；College of Electrical and Information Engineering, Hunan University, Changsha, China | 利用透射率提取与距离对齐，实现被动长波红外高光谱测距。 | [#1353](https://github.com/thinson/RS-PaperClaw/issues/1353) |
| [20260924] Exploiting answer-invariant redundancies in satellite imagery for efficient VLM inference on edge | Janveja Ishani, Zhang Davis, Oh Seoyul, Vasisht Deepak | University of Illinois Urbana-Champaign | 挖掘卫星影像中答案不变冗余，提升边缘端视觉语言模型推理效率。 | [#1354](https://github.com/thinson/RS-PaperClaw/issues/1354) |
| [20260924] Recoverable Geographic Location Information in Earth-Observation Embeddings | Zhang Peiwen, Hu Kristie, Knezevic Jovana, Yin Shunde, Gao Kyle | University of Waterloo；University of Cambridge；Aalto University | 研究地球观测嵌入中可恢复的地理位置信息，揭示基础模型位置泄露风险。 | [#1355](https://github.com/thinson/RS-PaperClaw/issues/1355) |
| [20260924] Graph-Based Semi-Supervised Hyperspectral Image Classification with Distance-Aware Spatial Measure | Sérgio J. M. Almeida, José C. M. Bermudez | a Catholic University of Pelotas, Center for Social and Technological Sciences, Pelotas, RS, Brazil；b Federal University of Santa Catarina, Department of Electrical and Electronic Engineering, Florianópolis, SC, Brazil | 基于图半监督学习与距离感知空间度量，提升高光谱图像分类性能。 | [#1356](https://github.com/thinson/RS-PaperClaw/issues/1356) |
| [20260924] Efficient Continuous DEM Reconstruction under Limited Target-Resolution Supervision | Shi Zekai, Zhang Meng, Zhang Haokun, Zhang Bo | School of Human Settlements and Civil Engineering, Xi'an Jiaotong University；School of Artificial Intelligence, Optics and Electronics (iOPEN), Northwestern Polytechnical University | 在有限目标分辨率监督下，实现高效连续DEM重建与几何引导融合。 | [#1357](https://github.com/thinson/RS-PaperClaw/issues/1357) |
| [20260924] AlphaEarth distinguishes cities but compresses urban variation | Renninger Andrew | School of Geographical & Earth Sciences, University of Glasgow；dispersion within urban centres is 14.1% greater per standard deviation of national development, even；Urban environments vary within cities, between Earth embeddings—which represent raster imcities and over time, and comparative research | AlphaEarth嵌入能区分城市但压缩城市内部变异，揭示表征偏差。 | [#1358](https://github.com/thinson/RS-PaperClaw/issues/1358) |
| [20260924] Below-ground Fungal Biodiversity Can be Monitored Using Self-Supervised Learning Satellite Features | Young Robin, Michael E. Van Nuland, E. Toby Kiers, Větrovský Tomáš, Kohout Petr, Baldrian Petr, Keshav Srinivasan | Department of Computer Science and Technology, University of；Amsterdam Institute for Life and Environment (A-LIFE), Section；Ecology & Evolution, Vrije Universiteit Amsterdam, Amsterdam, The；Institute of Microbiology, Czech Academy of Sciences, Videnska 1083；Laboratory of Microbial Ecology and Biogeography, Institute of；Microbiology, Czech Academy of Sciences, Videnska 1083, Prague | 利用自监督学习卫星特征，监测地下真菌生物多样性。 | [#1359](https://github.com/thinson/RS-PaperClaw/issues/1359) |
| [20260924] MIND the Gap: A Geographic Implicit Neural Representation with Adjustable Spatial Scale | Corley Isaac, Rao Arjun, Rolf Esther, Klemmer Konstantin, Shelhamer Evan, Lehmann Nils, Rußwurm Marc, Mai Gengchen, Jacobs Nathan, Kerner Hannah | University of British Columbia；University of Colorado Boulder；University College London；Vector Institute；Technical University of Munich；University of Bonn；University of Texas at Austin；Washington University in Saint Louis；Arizona State University；research.taylorgeospatial.org/mind | MIND提出可调空间尺度的地理隐式神经表示，支持稀疏标签建模。 | [#1360](https://github.com/thinson/RS-PaperClaw/issues/1360) |
| [20260924] CSCWD: Cross-Scale Channel-wise Knowledge Distillation for Lightweight Tiny Object Detection on Edge Devices | Zamani Amir, Ghasemi-Naraghi Zeinab | Department of Computer Engineering, Islamic Revolution Comprehensive University, Tehran, Iran | CSCWD通过跨尺度通道知识蒸馏，实现边缘设备轻量小目标检测。 | [#1361](https://github.com/thinson/RS-PaperClaw/issues/1361) |

## 🔎 观察

- 基础模型嵌入的隐私与表征偏差问题开始被系统审视，地理位置恢复和城市变异压缩提示需加强嵌入安全与公平性评估。
- 边缘部署与高效推理成为遥感AI落地关键，VLM冗余剪枝和跨尺度蒸馏分别从模型压缩与知识迁移角度提供可行路径。

---

Powered by OpenClaw🦞

---

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
