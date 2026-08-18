# Daily Reports

最近三天日报（最新在前）：

# [20260817](./202608/20260817.md)
## 📌 今日概况

今日共检索候选论文 14 篇；关键词+LLM 智能匹配遥感交叉论文 5 篇；最终纳入日报 5 篇。

今日遥感研究聚焦于提升模型在标注数据稀缺条件下的性能，涵盖半监督语义分割、高光谱图像分类与植物性状反演。同时，合成数据增强被用于农业灾害检测，而GNSS拒止环境下的跨平台地理配准问题也得到关注。整体趋势显示，深度学习方法与数据增强策略在遥感应用中持续深化。

## ✨ 今日亮点

- 半监督学习结合特征记忆库，提升遥感分割精度。
- 光谱转图像策略增强2D-CNN植物性状反演能力。
- 扩散模型合成数据助力战损农田检测与增强。

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260817] Bridging the Gap between Labeled and Unlabeled Data via Unified Flow with Feature Memory Bank | Wang Shanwen, Sun Xin, Hong Danfeng, Dong Junyu, Patrick Le Callet | Faculty of Data Science, City University of Macau,, SAR Macao, China；School of Automation, Southeast University, Nanjing,, China；Department of Computer Science and Technology, Ocean University of China, Qingdao, China；Nantes Université, Ecole Centrale Nantes, CAPACITES SAS, CNRS, LS2 N, UMR, Nantes, France | 提出统一流与特征记忆库，弥合半监督分割中标注与未标注数据差距。 | [#1130](https://github.com/thinson/RS-PaperClaw/issues/1130) |
| [20260817] Turning spectra into images improves plant trait retrieval with 2D-CNNs | Lopatin Javier, Kattenborn Teja, Cherif Eya, Moreno Sebastián | Center for Climate Resilience Research (CR)2, University of Chile, Santiago, Chile, 8370449；Sensor-based Geoinformatics (geosense), University of Freiburg, Freiburg, Breisgau, Germany；Institute for Earth System Science and Remote Sensing, Leipzig University, Germany | 将光谱数据转为图像格式，利用2D-CNN提升植物性状反演精度。 | [#1131](https://github.com/thinson/RS-PaperClaw/issues/1131) |
| [20260817] Synthetic Data Augmentation for Satellite-Based Analysis of Battle-Damaged Agricultural Fields in Ukraine | Sumyk Marta, Kosovan Oleksandr, Voitsitska Iryna | Ukrainian Catholic University, Lviv, Ukraine | 采用扩散模型生成合成数据，增强卫星影像中战损农田的检测能力。 | [#1132](https://github.com/thinson/RS-PaperClaw/issues/1132) |
| [20260817] Marker-Constrained Pose-Graph Correction for Cross-Platform Georeferencing in GNSS-Denied Environments | Giberna Marco, Jose Luis Sanchez Lopez, Voos Holger | Automation and Robotics Research Group, Interdisciplinary Centre for Security, Reliability；and Trust (SnT), University of Luxembourg；Faculty of Science, Technology and Medicine, University of Luxembourg, 4365 | 利用标记约束的位姿图校正，实现GNSS拒止环境下的跨平台地理配准。 | [#1133](https://github.com/thinson/RS-PaperClaw/issues/1133) |
| [20260817] Convolution-Free Holistic Multivariance Decomposition Layer for Efficient Hyperspectral Image Classification Tensor Networks | Tuna Süha, Başar Ülker | aIstanbul Technical University, Informatics Institute；bIstanbul Esenyurt University, Faculty of Business and Management Sciences；Department of Management Information Systems, Esenyurt, 34517, \.Istanbul, Türkiye | 提出无卷积的多元分解层，基于张量网络高效分类高光谱图像。 | [#1134](https://github.com/thinson/RS-PaperClaw/issues/1134) |

## 🔎 观察

- 半监督与数据增强技术成为应对遥感标注稀缺的主流路径。
- 张量网络与无卷积设计开始应用于高光谱分类，追求效率与精度平衡。

---

Powered by OpenClaw🦞

---

# [20260816](./202608/20260816.md)
## 📌 今日概况

今日共检索候选论文 7 篇；关键词+LLM 智能匹配遥感交叉论文 6 篇；最终纳入日报 6 篇。

今日遥感AI研究聚焦于高效感知与智能解译，涵盖无人机影像的微小目标检测、裂缝分割及4K视频边缘计算，同时探索遥感基础模型的视觉-语言对齐与边界感知分割，并引入材料发现中的迭代反馈机制，整体呈现从模型精度向轻量化、标签高效与跨域融合发展的趋势。

## ✨ 今日亮点

- 无人机影像感知向边缘计算与标签高效方向深化
- 遥感分割注重边界感知与层次特征自适应细化
- 基础模型探索视觉-语言对齐以提升泛化能力

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260816] Synthesizing like a chemist: an iterative, feedback-driven loop for materials discovery | Sheng Fang, Steven B. Torrisi, Volk Amanda, Tran Kevin, Nakano Koki, Brian W. Anthony, Buonassisi Tonio | Department of Mechanical Engineering, Massachusetts Institute of Technology；Toyota Research Institute | 材料发现采用迭代反馈循环，结合语言模型与贝叶斯优化提升合成效率 | [#1123](https://github.com/thinson/RS-PaperClaw/issues/1123) |
| [20260816] MITE-Net: SWaP-Optimized 4K Video Tiny Target Perception for Embodied Edge SAR | Xu Mingshuo, Hua Mu, Peng Jigen, Wang Qi, Yue Shigang | School of Mathematics and Computing Science, University of Leicester, Leicester LE1 7 RH, UK；the Machine Life and Intelligence Research Center, Guangzhou University, Guangzhou, China | MITE-Net优化SWaP，实现边缘端4K视频微小目标实时感知 | [#1124](https://github.com/thinson/RS-PaperClaw/issues/1124) |
| [20260816] CrevasseSeg: A Label-Efficient UAV Crevasse Segmentation Framework | Wallace Steven, William D Harcourt, Hann Richard, Durrant Aiden, Sripada Somayajulu, Leontidis Georgios | School of Natural and Computing Sciences, University of Aberdeen, UK；Interdisciplinary Institute, University of Aberdeen, UK；School of Geosciences, University of Aberdeen, UK；Department of Engineering Cybernetics, Norwegian University of Science and Technology, Norway；School of Computing Sciences, University of East Anglia, UK；Department of Physics and Technology, UiT The Arctic University of Norway；(UAV) imagery matters for glaciological research | CrevasseSeg利用自监督学习，减少标注需求实现无人机裂缝分割 | [#1125](https://github.com/thinson/RS-PaperClaw/issues/1125) |
| [20260816] BASeg: Boundary-Aware Remote Sensing Segmentation with Structural Penalties | Song Yuexi, Sun Kailai, Wang Zhuoyu, He Mingyi, Paul Pu Liang, Wang Shenhao, Zhao Jinhua | National University of Singapore；Singapore-MIT Alliance for Research and Technology；Massachusetts Institute of Technology；University of Florida | BASeg引入结构惩罚损失，增强遥感图像边界感知分割精度 | [#1126](https://github.com/thinson/RS-PaperClaw/issues/1126) |
| [20260816] Hierarchical Adaptive Feature Refinement Network for VHR Remote Sensing Image Segmentation | Cao Shuaishuai, Tang Meng, Peng Shuwei, Liu Xuan, Huang Min, Chen Jie, Niu Jiacheng, Chen Yong, Akpokodje Edore, Lin Hui | School of Information Science and Technology, Southwest Jiaotong University；School of Computer Science and Artificial Intelligence, Wuhan University of Technology；School of Electronic and Information Engineering, Beihang University；School of Surveying and Geo-Informatics, Shandong Jianzhu University；School of Geography and Environment, Jiangxi Normal University；School of Computer Science and Engineering, University of Electronic Science and Technology of China；School of Computer Science and Technology, Harbin Institute of Technology；School of Computer Science and Engineering, Nanyang Technological University；School of Geography and Remote Sensing, Guangzhou University；Institute of Space and Earth Information Science, The Chinese University of Hong Kong | 层次自适应细化网络结合频率分析，提升超高分辨率影像分割效果 | [#1127](https://github.com/thinson/RS-PaperClaw/issues/1127) |
| [20260816] AlignJEPA: Predictive Vision-Language Alignment for Remote Sensing Foundation Models | Md Aminur Hossain, Vaghasiya Omkumar, Rajeev Ranjan Dwivedi, Kurmi Vinod, Banerjee Biplab | Vinod Kurmi3, and Biplab Banerjee2；Space Applications Centre, ISRO, Ahmedabad, India；CSRE, Indian Institute of Technology Bombay, India；Indian Institute of Science Education and Research (IISER) Bhopal, India | AlignJEPA通过预测性对齐，增强遥感基础模型的视觉-语言检索能力 | [#1128](https://github.com/thinson/RS-PaperClaw/issues/1128) |

## 🔎 观察

- 研究明显向轻量化与边缘部署倾斜，强调实际应用中的计算约束
- 标签高效与自监督方法成为热点，反映标注成本对遥感AI的制约

---

Powered by OpenClaw🦞

---

# [20260815](./202608/20260815.md)
## 📌 今日概况

今日共检索候选论文 11 篇；关键词+LLM 智能匹配遥感交叉论文 9 篇；最终纳入日报 9 篇。

今日遥感AI研究聚焦于基础模型、鲁棒性与效率优化。多篇论文探索地球观测基础模型在生态水文学中的应用，以及大语言模型在无人机导航中的潜力。同时，研究关注对抗鲁棒性、光学-SAR融合检测、视频去模糊和目标检测等任务。此外，针对大视觉语言模型的token剪枝、SAR去斑和光谱重建等效率与质量提升方法也受到关注。整体趋势显示，模型正朝着更智能、更高效、更鲁棒的方向发展。

## ✨ 今日亮点

- 基础模型与LLM驱动遥感智能分析。
- 鲁棒性研究覆盖对抗攻击与跨模态融合。
- 效率优化聚焦token剪枝与去斑算法。

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260815] Earth Observation Foundation Models for Terrestrial Ecohydrology: From Representation Learning to Process Inference | Yu Yi, Peng Jian, Lin Yucheng, Trevor F. Keenan, Thomas F. A. Bishop | the Precision Agriculture, Hydrology and Geoinformation Science Laboratory, School of Life and Environmental Sciences, The University of Sydney, Eveleigh, NSW, Australia (；Department of Remote Sensing, Helmholtz Centre for Environmental Research--UFZ, Leipzig, Germany；Institute for Earth System Science and Remote Sensing, Leipzig University, Leipzig, Germany (；School of Energy and Environment, City University of Hong Kong, Hong Kong SAR, China (；Department of Environmental Science, Policy, and Management, University of California, Berkeley, Berkeley, CA, USA；the Climate and Ecosystem Sciences Division, Lawrence Berkeley National Laboratory, Berkeley, CA, USA ( | 综述地球观测基础模型在生态水文学中的表示学习与过程推断。 | [#1113](https://github.com/thinson/RS-PaperClaw/issues/1113) |
| [20260815] On the Adversarial Robustness of Remote Sensing Semantic Change Detection | Yu Weikang, Xu Yonghao, Ghamisi Pedram | Department of Electrical Engineering, Linköping University | 研究遥感语义变化检测的对抗鲁棒性，关注时间扰动影响。 | [#1114](https://github.com/thinson/RS-PaperClaw/issues/1114) |
| [20260815] Boundary-Aligned Contribution Routing for Robust Optical--SAR Object Detection | Zhang Haifa, Wang Yijing, Wang Haoyu, Li Zheng, Zuo Zhiqiang | the Tianjin Key Laboratory of Intelligent Unmanned Swarm Technology and System, School of Electrical and Information Engineering, Tianjin University, Tianjin, China (；the Key Laboratory of System Control and Information Processing, Ministry of Education of China, Shanghai, China ( | 提出边界对齐贡献路由方法，提升光学-SAR融合检测鲁棒性。 | [#1115](https://github.com/thinson/RS-PaperClaw/issues/1115) |
| [20260815] UAV Video Deblurring via Motion-Aware Diffusion: A Path to Robust Target Detection | Hu Zhiqiang, Huang Shouren, Ishikawa Masatoshi | the Research Institute for Science \& Technology, Tokyo University of Science | 利用运动感知扩散实现无人机视频去模糊，增强目标检测。 | [#1116](https://github.com/thinson/RS-PaperClaw/issues/1116) |
| [20260815] LAPF: LLM-Agent-Based Path Finder Using the UAVScenes Dataset | Emami Yousef, Homaei Mohammadhossein, Zhou Hao, Miguel Gutiérrez Gaitán, Atefeh Hajijamali Arani, Zhang Rui | University of Vigo；University of Auckland；University of Science and Technology of China；University of Toronto；National University of Singapore | 基于LLM智能体与UAVScenes数据集实现自主路径规划。 | [#1117](https://github.com/thinson/RS-PaperClaw/issues/1117) |
| [20260815] SA-GEM: Scale-Adaptive and Geospatial Evidence-Modulated Token Pruning for Efficient Remote Sensing Large Vision-Language Models | Ma Kexin, Xiao Jing, Xing Bowen, Liao Liang, Lin Chia-Wen | School of Artificial Intelligence, Wuhan University；Hangzhou Institute of Technology, Xidian University；Department of Electrical Engineering, National Tsing Hua University | 提出尺度自适应与地理证据调制的token剪枝，加速遥感大模型。 | [#1118](https://github.com/thinson/RS-PaperClaw/issues/1118) |
| [20260815] Frequency and Edge-Guided Segment Anything Model for Remote Sensing Image Semantic Segmentation | Gao Feng, Pan Zizhe, Wang Haoting, Hua Ruzhuang, Cao Jingchao, Dong Junyu, Du Qian | State Key Laboratory of Physical Oceanography, SAM’s training data；Department of Electrical and Computer Engineering, land cover types exhibit distinct spatial distributions, leading to Mississippi State University, Starkville, MS USA | 结合频率与边缘引导的SAM模型，提升遥感图像分割精度。 | [#1119](https://github.com/thinson/RS-PaperClaw/issues/1119) |
| [20260815] Geometry-Calibrated Closed-Form Shrinkage for SAR Despeckling | Hu Xuran, Zhu Mingzhe, Stanković Djordje, Zhu Yujie, Feng Zhenpeng, Ban Yifang, Stanković Ljubiša | School of Electronic Engineering, Xidian University, Xi'an, China；the Kunshan Innovation Institute of Xidian University, Kunshan, China；the EE Department, University of Montenegro, Podgorica, Montenegro；the Division of Geoinformatics, KTH Royal Institute of Technology, Stockholm, Sweden；the Faculty of Science and Engineering, Macquarie University, Sydney, NSW, Australia | 提出几何校准闭式收缩方法，用于SAR图像去斑。 | [#1120](https://github.com/thinson/RS-PaperClaw/issues/1120) |
| [20260815] Registration-Free Hyperspectral Reconstruction from RGB via a Permutation-Invariant Gram-Matrix Principle | Zhao Jiangsan, Hirafuji Masayuki, Ninomiya Seishi, Geipel Jakob, Guo Wei | Department of Agricultural Technology, Norwegian Institute of Bioeconomy Research (NIBIO), Ås, Norway；Laboratory of Field Phenomics, Graduate School of Agriculture and Life Sciences, The University of Tokyo, Nishitokyo, Tokyo 188-0002；Plant Phenomics Research Center, Nanjing Agricultural University, Nanjing, China | 利用置换不变Gram矩阵实现无配准的高光谱重建。 | [#1121](https://github.com/thinson/RS-PaperClaw/issues/1121) |

## 🔎 观察

- 基础模型正从通用遥感向特定领域（如生态水文）深化，强调过程推断能力。
- 鲁棒性与效率并重，对抗攻击、跨模态融合及模型压缩成为研究热点。

---

Powered by OpenClaw🦞

---
