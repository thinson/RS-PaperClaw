# Daily Reports

最近三天日报（最新在前）：

# [20260429](./202604/20260429.md)
## 📌 今日概况

今日共检索候选论文 14 篇；关键词+LLM 智能匹配遥感交叉论文 11 篇；最终纳入日报 10 篇。

今日遥感AI研究呈现多模态融合与基础模型迁移两大主线。无人机RGBT语义分割、开放词汇变化检测等任务聚焦跨模态对齐；高光谱基础模型跨域迁移、量子机器学习特征映射等探索新型表征学习。3D视觉与点云配准等几何任务持续受到关注，扩散模型与拓扑学习方法为降维与半监督学习提供新思路。

## ✨ 今日亮点

- MemOVCD提出免训练开放词汇变化检测，通过跨时序记忆推理实现自适应修正
- AirZoo构建大规模合成数据集，统一支撑航空几何三维视觉的地面真值研究
- 高光谱扩散框架将噪声映射至低维流形，解决退化图像分类的维度灾难问题

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260429] Graph-based Semantic Calibration Network for Unaligned UAV RGBT Image Semantic Segmentation and A Large-scale Benchmark | Fan Fangqiang, Zhao Zhicheng, Ma Xiaoliang, Li Chenglong, Tang Jin | Key Laboratory of Intelligent Comput-；the School of Computer Science and Technology, Anhui the modality gap is reduced, deriving geometric corrections；the Anhui Provincial Key Laboratory of Multimodal | 图神经网络实现无人机RGBT图像语义分割的跨模态对齐与几何校正，构建大规模基准数据集。 | [#435](https://github.com/thinson/RS-PaperClaw/issues/435) |
| [20260429] MemOVCD: Training-Free Open-Vocabulary Change Detection via Cross-Temporal Memory Reasoning and Global-Local Adaptive Rectification | Kuang Zuzheng, Chang Honghao, Liang Boqiang, Wang Haoqian, He Lijun, Li Fan, Bi Haixia | Xi'an Jiaotong University | 免训练开放词汇变化检测方法MemOVCD，利用跨时序记忆推理与全局-局部自适应修正提升检测精度。 | [#436](https://github.com/thinson/RS-PaperClaw/issues/436) |
| [20260429] Parameterized Quantum Circuits as Feature Maps: Representation Quality and Readout Effects in Multispectral Land-Cover Classification | Komini Ralntion, Mandilara Aikaterini, Maragkopoulos Georgios, Syvridis Dimitris | Department of Informatics and Telecommunications, National and Kapodistrian University of Athens；Eulambia Advanced Technologies Ltd | 参数化量子电路作为特征映射，评估多光谱土地覆盖分类中的表示质量与读出效应影响。 | [#437](https://github.com/thinson/RS-PaperClaw/issues/437) |
| [20260429] AirZoo: A Unified Large-Scale Dataset for Grounding Aerial Geometric 3D Vision | Cheng Xiaoya, Wu Rouwan, Liu Xinyi, Cui Zeyu, Liu Yan, Zhao Na, Liu Yu, Zhang Maojun, Yan Shen | National University of Defense Technology；Singapore University of Technology and Design | AirZoo统一大规模合成数据集，为航空几何三维视觉任务提供摄影测量级网格真值。 | [#438](https://github.com/thinson/RS-PaperClaw/issues/438) |
| [20260429] 3D-LENS: A 3D Lifting-based Elevated Novel-view Synthesis method for Single-View Aerial-Ground Re-Identification | Grolleau William, Sabourin Astrid, Lapouge Guillaume, Achard Catherine | Université Paris-Saclay, CEA, List；Sorbonne University, CNRS, Institute of Intelligent Systems and Robotics (ISIR) | 3D-LENS基于单视图三维提升，实现空中-地面跨视角重识别的新视角合成。 | [#439](https://github.com/thinson/RS-PaperClaw/issues/439) |
| [20260429] Cross-Domain Transfer of Hyperspectral Foundation Models | Theisen Nick, Neubert Peer | Intelligent Autonomous Systems, University of Koblenz | 高光谱基础模型跨域迁移研究，探索预训练表征在不同地理场景间的可迁移性。 | [#440](https://github.com/thinson/RS-PaperClaw/issues/440) |
| [20260429] Topology-Aware Representation Alignment for Semi-Supervised Vision-Language Learning | You Junwon, Jang Mihyun, Mo Sangwoo, Jung Jae-Hun | KAIST；POSTECH | 拓扑感知表征对齐方法，利用持续同调优化半监督视觉-语言学习的多模态表征。 | [#441](https://github.com/thinson/RS-PaperClaw/issues/441) |
| [20260429] Point Cloud Registration via Probabilistic Self-Update Local Correspondence and Line Vector Sets | Chung Kuo-Liang, Lin Yu-Cheng, Chen Wu-Chi | Department of Computer Science and Information Engineering, National Taiwan University of Science and Technology | 概率自更新局部对应与线向量集方法，提升点云配准的鲁棒性与精度。 | [#442](https://github.com/thinson/RS-PaperClaw/issues/442) |
| [20260429] High-Dimensional Noise to Low-Dimensional Manifolds: A Manifold-Space Diffusion Framework for Degraded Hyperspectral Image Classification | Yang Boxiang, Chen Ning, Yue Xia, Luo Yichang, Fan Yingbo, Zhang Haoyuan, Ma Haoyu, Yue Jun, Mao Shanjun | School of Computer Science and Engineering, Central；the Aerospace Information Research a higher-dimensional observation space, thereby introducing；the Institute of energy, Peking University, Beijing, China mation；the School of Mechanics and Engineering Science, observations away from a compact spectral manifold into a；the School of Automation, Central South University, more dispersed high-dimensional space. In such cases, directly；the data, but more fundamentally from the strong sensitivity the Institute of Remote Sensing；Geographic Information System, of its intrinsic structure to external perturbations | 流形空间扩散框架将高维噪声映射至低维流形，解决退化高光谱图像分类问题。 | [#443](https://github.com/thinson/RS-PaperClaw/issues/443) |
| [20260429] Seeking Consensus: Geometric-Semantic On-the-Fly Recalibration for Open-Vocabulary Remote Sensing Semantic Segmentation | Wang Guanchun, Wu Chenxiao, Zhang Xiangrong, Peng Zelin, Lai Jianxun, Zhang Tianyang, Tang Xu | School of Artificial Intelligence, Xidian University；MoE Key Lab of Artificial Intelligence, AI Institute, Shanghai Jiao Tong University | 几何-语义动态重校准方法，通过双重共识机制提升开放词汇遥感语义分割性能。 | [#444](https://github.com/thinson/RS-PaperClaw/issues/444) |

## 🔎 观察

- 开放词汇学习成为遥感语义分割热点方向，但几何一致性与语义一致性的联合优化仍具挑战。
- 量子机器学习在遥感领域的应用尚处探索期，其表示优势需更多实际任务验证。

---

Powered by OpenClaw🦞

---

# [20260428](./202604/20260428.md)
## 📌 今日概况

今日共检索候选论文 12 篇；关键词+LLM 智能匹配遥感交叉论文 6 篇；最终纳入日报 6 篇。

今日遥感AI研究呈现多元化趋势：卫星任务调度基准建设、量子启发式SAR分类、阴影感知图像修复、网络规模图像地理定位、边缘云协同重建及农业无人机检测等方向均有进展。计算效率与鲁棒性成为共同关注点，跨机构国际合作特征明显。

## ✨ 今日亮点

- EOS-Bench发布首个综合性地球观测卫星调度基准，覆盖敏捷卫星组合优化问题
- 量子启发张量网络方法实现SAR目标分类的模型压缩与抗数据投毒能力
- SARU框架统一阴影检测与去除任务，并构建遥感图像阴影处理新基准

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260428] EOS-Bench: A Comprehensive Benchmark for Earth Observation Satellite Scheduling | Yin Qian, Li Jiaxing, Cheng Jiaqi, Luo Qizhang, Riccardi Annalisa, Chatterjee Abhijit, Vazquez Rafael, Novara Carlo, Mavrovouniotis Michalis, Ponnuthurai Nagaratnam Suganthan, Bai Shengzhou, Hu Xiaoxuan, Xing Lining, Xu Ming, Li Shuang, Zheng Zixuan, Shen Xin, Chen Xiaoyu, Gu Yi, ..., Wang Xinwei | School of Traffic and Transportation Engineering, Central South University；School of Engineering and Materials Science, Queen Mary University of London；College of Automation, Central South University；Mechanical and Aerospace Engineering, University of Strathclyde；Department of Computer Science, University of Exeter；Department of Aerospace Engineering, Universidad de Sevilla；Department of Electronics and Telecommunications, Politecnico di Torino；ERATOSTHENES Centre of Excellence；Department of Civil Engineering and Geomatics, Cyprus University of Technology；Department of Computer Science and Engineering, College of Engineering, Qatar University；Department of Aerospace Engineering, Korea Advanced Institute of Science and Technology；School of Management, Hefei University of Technology；Key Laboratory of Collaborative Intelligence Systems, Ministry of Education, Xidian University；School of Astronautics, Beihang University；Advanced Space Technology Laboratory, College of Astronautics, Nanjing University of Aeronautics and Astronautics；National Key Laboratory of Aerospace Flight Dynamics, Northwestern Polytechnical University；State Key Laboratory of Information Engineering in Surveying, Mapping and Remote Sensing, Wuhan University；School of Computer Science, China University of Geosciences；School of Information Science and Technology, Dalian Maritime University；Department of Electrical & Computer Engineering, University of Alberta | EOS-Bench建立地球观测卫星调度综合基准，为组合优化算法提供标准化评估平台。 | [#420](https://github.com/thinson/RS-PaperClaw/issues/420) |
| [20260428] Quantum-Inspired Robust and Scalable SAR Object Classification | Scharf Maximilian, Trenti Marco, Bock Felix, Davidson Padraig, Brosch Tobias, Benjamin Rodrigues de Miranda, Huber Sigurd, Felser Timo | Tensor AI Solutions GmbH；Hensoldt Sensors GmbH；German Aerospace Center (DLR)；Ulm University | 量子启发张量网络方法在SAR目标分类中实现鲁棒性与可扩展性的双重提升。 | [#421](https://github.com/thinson/RS-PaperClaw/issues/421) |
| [20260428] SARU: A Shadow-Aware and Removal Unified Framework for Remote Sensing Images with New Benchmarks | Bo Zi-Yang, Lu Wei, Chen Hongruixuan, Chen Si-Bao, Luo Bin | Anhui University；The University of Tokyo | SARU框架将阴影检测与去除任务统一，并配套发布遥感图像阴影处理基准数据集。 | [#422](https://github.com/thinson/RS-PaperClaw/issues/422) |
| [20260428] GeoSearch: Augmenting Worldwide Geolocalization with Web-Scale Reverse Image Search and Image Matching | Le-Duc Tung-Duong, Nguyen-Son Hoang-Quoc, Dao Minh-Son | University of Science, VNU-HCM；National Institute of Information and Communications Technology | GeoSearch结合网络规模反向图像搜索与大语言模型，增强全球图像地理定位能力。 | [#423](https://github.com/thinson/RS-PaperClaw/issues/423) |
| [20260428] Edge-Cloud Collaborative Reconstruction via Structure-Aware Latent Diffusion for Downstream Remote Sensing Perception | Li Yun, Li Xianju | Chinese Academy of Sciences | 结构感知潜扩散模型支撑边缘云协同重建，服务于下游遥感感知任务。 | [#424](https://github.com/thinson/RS-PaperClaw/issues/424) |
| [20260428] Towards Robust Deep Learning-based Rumex Obtusifolius Detection from Drone Images | Fabian Dionys Schrag, Mehmet Ozgur Turkoglu, Schindler Konrad, Ralph Lukas Stoop | Agroscope NBA；Agroscope Earth Observation of Agroecosystems Team；ETH Zurich | 针对无人机图像的钝叶酸模杂草检测研究，探索CNN与ViT的域适应鲁棒性。 | [#425](https://github.com/thinson/RS-PaperClaw/issues/425) |

## 🔎 观察

- 遥感AI正从单一任务优化转向系统级基准建设，EOS-Bench等工具将加速算法公平比较与产业落地。
- 量子计算与边缘智能等新型计算范式开始渗透遥感领域，但其实际部署效益仍需工程验证。

---

Powered by OpenClaw🦞

---

# [20260427](./202604/20260427.md)
## 📌 今日概况

今日共检索候选论文 7 篇；关键词+LLM 智能匹配遥感交叉论文 4 篇；最终纳入日报 4 篇。

今日遥感AI研究呈现多模态融合与语义理解并进的趋势。西南交大团队探索开放词汇语义分割，结合目标级标签与场景级语义特征；芬兰地理空间研究所发布多光谱机载激光扫描数据集，支撑树种分类研究；哈工大等提出统一去雾网络，兼顾色彩恢复与边缘保持；印度团队则聚焦遥感图像描述生成，融合结构-语义信息。

## ✨ 今日亮点

- 开放词汇遥感分割突破：整合目标级与场景级跨模态特征，提升多模态图像泛化能力
- 多光谱激光雷达数据集发布：MS-ALS-SPECIES为树种分类提供新型数据基准
- 统一去雾网络创新：6thGrid-Net基于3D LUTs实现色彩恢复与边缘保持的联合优化

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260427] Open-Vocabulary Semantic Segmentation Network Integrating Object-Level Label and Scene-Level Semantic Features for Multimodal Remote Sensing Images | Dai Jinkun, Ye Yuanxin, Tang Peng, Tang Tengfeng, Ma Xianping, Xiao Jing, Wang Mi | Faculty of Geosciences and Engineering, Southwest Jiaotong University；State-Province Joint Engineering Laboratory of Spatial Information Technology for High-Speed Railway Safety, Southwest Jiaotong University；School of Artificial Intelligence, Wuhan University；State Key Laboratory of Information Engineering in Surveying, Mapping and Remote Sensing, Wuhan University | 西南交大等提出开放词汇语义分割网络，融合目标级标签与场景级语义特征，实现多模态遥感图像的跨模态文本监督学习。 | [#339](https://github.com/thinson/RS-PaperClaw/issues/339) |
| [20260427] Multispectral airborne laser scanning dataset for tree species classification: MS-ALS-SPECIES | Hyyppä Matti, Salolahti Klaara, Hyyppä Eric, Yu Xiaowei, Taher Josef, Matikainen Leena, Lehtomäki Matti, Litkey Paula, Hakala Teemu, Kaartinen Harri, Hyyppä Juha, Kukko Antero | Department of Remote Sensing and Photogrammetry, Finnish Geospatial Research Institute FGI, The National Land Survey of Finland | 芬兰地理空间研究所发布MS-ALS-SPECIES数据集，基于多光谱机载激光扫描技术，为深度学习树种分类研究提供数据支撑。 | [#416](https://github.com/thinson/RS-PaperClaw/issues/416) |
| [20260427] 6thGrid-Net: Unified Remote Sensing Image Dehazing Based on Color Restoration and Edge-Preserving | Bai Runci, Jiang Kui, Chen Xiang, Wu Chen, Lu Dianjie, Zhang Guijuan, Zheng Zhuoran | China Academy of Information and Communications Technology；Harbin Institute of Technology；Nanjing University of Science and Technology | 中国信通院等提出6thGrid-Net统一去雾网络，结合色彩恢复与边缘保持机制，基于3D LUTs实现遥感图像质量增强。 | [#417](https://github.com/thinson/RS-PaperClaw/issues/417) |
| [20260427] JSSFF: A Joint Structural-Semantic Fusion Framework for Remote Sensing Image Captioning | Das Swadhin, Yadav Vivek | University of Petroleum and Energy Studies | 印度石油能源大学提出JSSFF联合结构-语义融合框架，通过边缘感知融合改进编码器-解码器架构，用于遥感图像描述生成。 | [#418](https://github.com/thinson/RS-PaperClaw/issues/418) |

## 🔎 观察

- 多模态融合成为核心范式：从跨模态分割到结构-语义联合建模，异构数据协同处理能力持续增强
- 实用化数据集建设加速：多光谱激光雷达等新传感数据集的发布，正填补垂直应用领域的基准空白

---

Powered by OpenClaw🦞

---
