# Daily Reports

最近三天日报（最新在前）：

# [20261006](./202610/20261006.md)
## 📌 今日概况

今日共检索候选论文 16 篇；关键词+LLM 智能匹配遥感交叉论文 5 篇；最终纳入日报 5 篇。

今日遥感AI研究呈现三条主线：一是跨域迁移与泛化边界，CETUS探索地球表征向土星SAR的迁移，剑桥工作则从空间依赖性出发重新审视样本独立性与泛化界；二是数据泄漏与评估可靠性，高光谱分类中patch重叠导致的泄漏被量化，提示现有精度可能被高估；三是面向实际难题的方法改进，RBMatch针对半监督建筑提取的类别不平衡提出双层重平衡，RSJEV则利用多模态大模型增强场景判别。整体看，社区对评估严谨性和跨域可靠性的关注明显上升。

## ✨ 今日亮点

- 跨域迁移从地球走向土星SAR，检验表征的普适边界
- 空间依赖与patch重叠被量化，数据泄漏问题受重视
- 半监督与多模态大模型分别应对类别不平衡和场景判别

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20261006] CETUS: How Far Do Representations Trained on Earth Transfer to Cassini SAR of Titan? | Lee Kevin | University of California at Los Angeles, Los Angeles, CA；NASA Jet Propulsion Laboratory, California Institute of Technology, Pasadena, CA | 评估地球预训练表征迁移至土星Cassini SAR的可行性，面向行星地形分类。 | [#1447](https://github.com/thinson/RS-PaperClaw/issues/1447) |
| [20261006] RBMatch: Dual-Level Class Rebalancing for Semi-Supervised Building Footprint Extraction | Akil Ahmad Taki, Shaikh Anowarul Fattah | Department of EEE, Bangladesh University of Engineering and Technology(BUET)；Department of EEE, University of Asia Pacific ( | 提出双层类别重平衡的半监督方法，缓解建筑足迹提取中的不平衡问题。 | [#1448](https://github.com/thinson/RS-PaperClaw/issues/1448) |
| [20261006] How Many Independent Samples Does a Satellite Image Contain? Generalization Bounds for Spatially Dependent Data | Young Robin | Department of Computer Science and Technology；University of Cambridge, UK | 针对空间依赖数据推导泛化界，讨论卫星图像有效独立样本数。 | [#1449](https://github.com/thinson/RS-PaperClaw/issues/1449) |
| [20261006] RSJEV: Discriminative Remote Sensing Scene Classification with Multimodal Large Language Models | Si Dongchen, Wang Di, Xu Mingzhen, Zhang Jing, Du Bo, Zhang Liangpei | School of Computer Science, Wuhan University, Wuhan, China (；State Key Laboratory of Information Engineering in Surveying, Mapping and Remote Sensing, Wuhan University, Wuhan, China ( | 利用多模态大语言模型进行遥感场景分类，强调判别性决策。 | [#1450](https://github.com/thinson/RS-PaperClaw/issues/1450) |
| [20261006] Data Leakage in Patch-Based Hyperspectral Image Classification: Quantifying the Impact of Spatial Overlap | Mohammed Q. Alkhatib | College of Engineering and IT, University of Dubai, Dubai, 14143, UAE | 量化patch空间重叠导致的数据泄漏，揭示高光谱分类评估偏差。 | [#1451](https://github.com/thinson/RS-PaperClaw/issues/1451) |

## 🔎 观察

- 多篇工作指向同一隐患：空间自相关使样本非独立，评估与泛化结论需重新校准。
- 跨域迁移与泄漏量化表明，遥感AI正从追求精度转向追问精度是否可信。

---

Powered by OpenClaw🦞

---

# [20261005](./202610/20261005.md)
## 📌 今日概况

今日共检索候选论文 14 篇；关键词+LLM 智能匹配遥感交叉论文 6 篇；最终纳入日报 6 篇。

今日论文聚焦遥感基础模型与自监督表征学习，涵盖时序预测架构、公平性评估及多任务部分监督。SAR方向出现扩散模型与展开优化结合的重建方法，以及弱监督水体映射。图像恢复引入智能体与视觉语言模型应对复合退化。整体趋势显示，遥感AI正从单一任务向多任务、跨模态和鲁棒性评估演进，同时强调实际部署中的偏差与退化问题。

## ✨ 今日亮点

- 时序联合嵌入预测架构提升遥感表征学习能力
- 生物群系感知基准揭示遥感基础模型公平性缺陷
- 扩散模型与展开优化结合改进压缩SAR重建

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20261005] T-JEPA: A Temporal Joint-Embedding Predictive Architecture for Learning Better Remote Sensing Representations | Peng Bowen, Liu Li, Liu Yongxiang, Li Weijie, Zhou Jie, Liu Zhen | National University of Defense Technology, Changsha, China | 提出T-JEPA时序联合嵌入预测架构，利用时间信息学习更优遥感表征。 | [#1440](https://github.com/thinson/RS-PaperClaw/issues/1440) |
| [20261005] FairRSFM: A Biome-Aware Benchmark and Debiasing Framework for Remote Sensing Foundation Models | Md Aminur Hossain, Vaghasiya Omkumar, Rajeev Ranjan Dwivedi, Kurmi Vinod, Banerjee Biplab | Biplab Banerjee 2；Space Applications Centre, ISRO, Ahmedabad, India；Indian Institute of Technology Bombay, India；Indian Institute of Science Education and Research Bhopal | 构建生物群系感知基准与去偏框架，评估并提升遥感基础模型公平性。 | [#1441](https://github.com/thinson/RS-PaperClaw/issues/1441) |
| [20261005] Diffusion Meets Unrolling: Compressive SAR Image Reconstruction with Interleaved Learned Corrections | Pappas Odysseas, Andrew C. M. Austin, Mayo Perla, Golbabaee Mohammad, Achim Alin | VI Labs, School of Computer Science, University of Bristol；School of Electrical, Electronic, and Mechanical Engineering, University of Bristol；School of Engineering Mathematics and Technology, University of Bristol | 将扩散模型与展开优化交织，实现压缩SAR图像的高质量重建。 | [#1442](https://github.com/thinson/RS-PaperClaw/issues/1442) |
| [20261005] EORestore-Agent: Fidelity-Guided Agentic Restoration of Remote Sensing Images with Composite Degradations | Qi Heli, Zhou Zeqi, Yi Jingjun, Liu Kunyi, Lihe Ziyang, Wang Junjue, Yoshie Osamu, Yokoya Naoto | the Graduate School of Information, Production and Systems, Waseda University, Kitakyushu, Fukuoka 808-, Japan；the Graduate School of Frontier Sciences, The University of Tokyo, Kashiwa, Chiba 277-, Japan；the Informatics Institute, University of Amsterdam, Amsterdam XH, The Netherlands；Wuhan University, Wuhan, China | 提出保真度引导的智能体恢复框架，处理遥感图像复合退化。 | [#1443](https://github.com/thinson/RS-PaperClaw/issues/1443) |
| [20261005] Multi-Task Partially Supervised Learning for Super-Resolution and Semantic Segmentation on Earth Observation data | Lê Hoàng-Ân, Pham Minh-Tan, Lemai-Chenevier Solange, Greslou Daniel | Université Bretagne Sud, IRISA, UMR 6074, Vannes, France；Centre National d’Etudes Spatiales (CNES), Toulouse, France | 面向地球观测数据，研究超分辨率与语义分割的多任务部分监督学习。 | [#1444](https://github.com/thinson/RS-PaperClaw/issues/1444) |
| [20261005] Extending Dynamic World Surface Water Mapping to Sentinel-1 with AlphaEarth Embeddings | Mukherjee Rohit, Policelli Frederick, Tellman Beth, Chakraborty TC, Giezendanner Jonathan, Jonathan A. Sullivan, Sun Ning | Pacific Northwest National Laboratory, Richland, WA USA (；NASA Goddard Space Flight Center, Greenbelt, MD USA；Fujitsu Research of America, Santa Clara, CA USA；University of Wisconsin--Madison, Madison, WI USA | 利用AlphaEarth嵌入将动态世界地表水映射扩展至Sentinel-1。 | [#1445](https://github.com/thinson/RS-PaperClaw/issues/1445) |

## 🔎 观察

- 遥感基础模型研究正从性能提升转向公平性、鲁棒性等可信维度评估。
- 扩散模型与经典优化结合，成为SAR重建等逆问题的新兴技术路线。

---

Powered by OpenClaw🦞

---

# [20261004](./202610/20261004.md)
## 📌 今日概况

今日共检索候选论文 7 篇；关键词+LLM 智能匹配遥感交叉论文 3 篇；最终纳入日报 3 篇。

今日遥感AI研究呈现三条并行主线：一是面向遥感智能体的可靠性机制，通过工具观测验证抑制误差传播；二是低光无人机场景下的RGB-红外差分融合与方向车辆检测，强调可靠性条件学习；三是多源卫星数据分析与LLM报告生成的全流程自动化，覆盖地表温度与Landsat数据处理。整体看，研究从单纯提升感知精度转向系统级可靠性与自动化闭环，智能体与生成式方法加速融入遥感工作流。

## ✨ 今日亮点

- 遥感智能体引入工具观测验证，抑制误差传播提升可靠性
- RGB-红外差分学习用于低光无人机方向车辆检测
- LLM驱动多源卫星数据分析与自动报告生成框架

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20261004] RSure-Agent: Reliable Use of Tool Observations for Remote Sensing Agents | Liu Fuyuan, Liu Nayu, Yu Wenhao, Wang Peijin, Feng Yingchao, Yao Fanglong, Wan Liang, Feng Wei | School of Computer Science and Technology, Tianjin University, Tianjin, China (；the Key Laboratory of Target Cognition and Application Technology (TCAT), Aerospace Information Research Institute, Chinese Academy of Sciences, Beijing, China ( | 提出RSure-Agent，通过验证工具观测的可靠性来抑制遥感智能体中的误差传播。 | [#1436](https://github.com/thinson/RS-PaperClaw/issues/1436) |
| [20261004] ReDiffNet: Differential RGB-Infrared Learning for Low-Light UAV Oriented Vehicle Detection | Zhang Qifan, Zhou Ziran, Li Ruijie, Tang Jincheng, Wang Hao, Qiao Qihao, Wang Chunliu | Dalian Maritime University, Dalian, China；The Hong Kong University of Science and Technology (Guangzhou), Guangzhou, China；Hubei University of Economics, Wuhan, China | 提出ReDiffNet，以差分RGB-红外学习实现低光无人机场景下的方向车辆检测。 | [#1437](https://github.com/thinson/RS-PaperClaw/issues/1437) |
| [20261004] A Framework for Automated Multi-Source Satellite Data Analytics and LLM-Based Report Generation | Hind Yousif Alhammadi, Isam Mashhour Al Jawarneh | Department of Applied Physics and Astronomy, University of Sharjah, Sharjah, UAE；Department of Computer Science, University of Sharjah, P.O.Box | 构建多源卫星数据分析与LLM报告生成框架，支持地表温度与Landsat自动化处理。 | [#1438](https://github.com/thinson/RS-PaperClaw/issues/1438) |

## 🔎 观察

- 遥感智能体研究开始关注工具观测的可靠性验证，而非仅追求任务完成率。
- 低光无人机检测与多源自动化分析并行推进，显示场景驱动与流程驱动并重。

---

Powered by OpenClaw🦞

---
