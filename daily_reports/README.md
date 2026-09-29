# Daily Reports

最近三天日报（最新在前）：

# [20260926](./202609/20260926.md)
## 📌 今日概况

今日共检索候选论文 11 篇；关键词+LLM 智能匹配遥感交叉论文 10 篇；最终纳入日报 10 篇。

今日遥感AI研究呈现三条主线：一是面向SAR与地球观测的基础模型持续深化，SARATR-X-v2强调尺度感知与散斑不变性预训练，Reuse or Relearn则从谱空间诊断基础模型微调策略；二是多模态融合与跨任务统一趋势明显，GeoCR利用SAR引导通用去云，区域Copula证据融合推进异源变化检测，统一框架尝试解决旋转目标视觉定位；三是评测基准与训练策略受到重视，USAI-Quant和PolyTopoBench分别面向定量推理与复杂多边形生成，RefineFly探索失败感知的后训练范式。

## ✨ 今日亮点

- SAR基础模型预训练引入尺度感知与散斑不变性，提升表征鲁棒性
- 地球观测基础模型微调策略获谱空间诊断，回答复用还是重学
- 遥感视觉语言模型评测向定量推理与复杂矢量生成延伸

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260926] SARATR-X-v2: Scale-Aware Structural Pre-Training for SAR Foundation Models | Li Weijie, Song Yafei, Liu Yongxiang, Peng Bowen, Zhou Jie, Xia Jingyuan, Yang Wei, Liu Tianpeng, Liu Zhen, Liu Li | College of Electronic Science and Technology, National University of Defense Technology, Changsha, China ( | 提出尺度感知结构预训练框架，增强SAR基础模型对多尺度目标与散斑噪声的鲁棒表征。 | [#964](https://github.com/thinson/RS-PaperClaw/issues/964) |
| [20260926] DiCoR: Decoupled Referent Disambiguation and Contour Recalibration for Efficient Referring Remote Sensing Image Segmentation | Gao Ziyang, Jiang Zhizhuo, Chang Jingjing, Yang Yixin, Pan Yuwen, Mao Yong-Qiang, Liu Yu, Chen Hai-Bao | School of Integrated Circuits, School of Information Science and Electronic Engineering, Shanghai Jiao Tong University, Shanghai, China (；College of Computer Science, Nankai University, Tianjin, China (；Department of Electronic Engineering, Tsinghua Shenzhen International Graduate School, Tsinghua University, Shenzhen, China (；Department of Electronic Engineering, Tsinghua University, Beijing, China ( | 解耦指代消歧与轮廓重校准，提升遥感指代图像分割的效率与边界精度。 | [#1104](https://github.com/thinson/RS-PaperClaw/issues/1104) |
| [20260926] RefineFly: Failure-Aware Post-Training for Aerial Vision-Language Navigation | Wang Boxiong, Kang Hui, Sun Geng, Li Jiahui, Yu Chao, Tian Daxin | Jilin University；Tsinghua University；Beihang University；Zhongguancun Academy | 面向空中视觉语言导航，利用失败感知后训练与PPO提升无人机导航鲁棒性。 | [#1370](https://github.com/thinson/RS-PaperClaw/issues/1370) |
| [20260926] Bandwidth, Not FLOPS: FFT Kernels, Matrix Units and SAR Imaging on Apple M6 | Mohamed Amine Bergach | Illumina | 在Apple M6上分析FFT核与矩阵单元，指出SAR成像性能瓶颈在带宽而非FLOPS。 | [#1371](https://github.com/thinson/RS-PaperClaw/issues/1371) |
| [20260926] GeoCR: Learning a Generalist Cloud Removal Prior from Heterogeneous Observations | Do Jeonghyeok, Kim Munchurl | Korea Advanced Institute of Science and Technology (KAIST) | 从异源观测中学习通用去云先验，借助SAR引导实现多光谱影像云去除。 | [#1372](https://github.com/thinson/RS-PaperClaw/issues/1372) |
| [20260926] Region-Local Copula Evidence Fusion for Heterogeneous Remote Sensing Change Detection | Ji Zhiyuan, Yin Junjun, Yang Jian | Department of Electronic Engineering, Tsinghua University, Beijing, P.R；School of Computer and Communication Engineering, University of Science and Technology Beijing, P.R | 提出区域局部Copula证据融合方法，用于异源遥感影像变化检测。 | [#1373](https://github.com/thinson/RS-PaperClaw/issues/1373) |
| [20260926] Reuse or Relearn? A Spectral View of Earth Observation Foundation Models | Mehmet Ozgur Turkoglu, Marsocci Valerio, Dominik J. Mühlematter, Senti Dominik, Schindler Konrad, Aasen Helge | ESA, -lab | 从谱空间诊断地球观测基础模型，分析微调时特征复用与重学习的选择。 | [#1374](https://github.com/thinson/RS-PaperClaw/issues/1374) |
| [20260926] A Unified Framework and Dataset for Oriented Object Visual Grounding in Remote Sensing | Ding Zeyu, Zhou Yong, Zhao Jiaqi, Du Wen-Liang, Li Xixi, Zhu Hancheng, Yao Rui, Abdulmotaleb El Saddik | representation by explicitly modeling the object center, size；Zhu, and Rui Yao are with the School of Computer Science and Existing remote sensing visual grounding (RSVG) methods；Technology/School of Artificial Intelligence, the Mine Digitization；Engineering Research Center of the Ministry of Education, and Jiangsu；and Emergency IoT in Underground Space, China University of Mining and；Computer Science, University of Ottawa, Ottawa, ON K1 N 6 N5, Canada ( | 构建统一框架与数据集，面向遥感旋转目标视觉定位建模中心与尺寸。 | [#1375](https://github.com/thinson/RS-PaperClaw/issues/1375) |
| [20260926] USAI-Quant: A Quantitative Reasoning Benchmark for Vision-Language Models in Built Environments | Wang Dongdong, Song Qingqi, Chen Yuzhou, Balakrishnan Deepak, Ravi Shankar Srinivasan, Wang Shenhao | University of Florida University of Florida University of Florida University of Florida；University of Florida University of Florida | 提出USAI-Quant基准，评估视觉语言模型在建成环境中的定量推理能力。 | [#1376](https://github.com/thinson/RS-PaperClaw/issues/1376) |
| [20260926] PolyTopoBench: A Benchmark for Complex Vector Polygon Generation from Remote Sensing Imagery | Liu Zeping, Lao Ni, Sun Weiwei, Wolff Gil, Xie Yiqun, Zhao Liang, Jiao Junfeng, Mai Gengchen | University of Texas at Austin；University of Maryland；Emory University | 发布PolyTopoBench基准，评测遥感影像生成复杂矢量多边形的拓扑保持能力。 | [#1377](https://github.com/thinson/RS-PaperClaw/issues/1377) |

## 🔎 观察

- SAR与地球观测基础模型正从通用预训练转向领域特性注入，尺度、散斑与谱诊断成为关键设计维度。
- 评测基准密集出现，反映遥感AI从模型创新向可复现、可量化的能力评估阶段过渡。

---

Powered by OpenClaw🦞

---

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
