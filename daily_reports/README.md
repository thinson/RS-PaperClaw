# Daily Reports

最近三天日报（最新在前）：

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

# [20260426](./202604/20260426.md)
## 📌 今日概况

今日共检索候选论文 7 篇；关键词+LLM 智能匹配遥感交叉论文 3 篇；最终纳入日报 3 篇。

今日研究聚焦深度学习在遥感图像处理中的创新应用，涵盖无监督时序制图、高光谱分类及SAR图像去噪三大方向。中山大学团队提出无需标注的油棕时序制图方法，汕头大学等探索CNN-Transformer融合架构，印度理工学院则回归数学基础比较PDE去噪模型。

## ✨ 今日亮点

- 无标注时序制图突破：利用历史噪声地图实现2020-2024年马印油棕榈动态监测
- CNN-Transformer协同：池化注意力融合机制提升高光谱图像分类精度
- PDE去噪理论对比：二阶与四阶偏微分方程在SAR及医学影像中的加权耦合研究

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260426] From Noisy Historical Maps to Time-Series Oil Palm Mapping Without Annotation in Malaysia and Indonesia (2020-2024) | Kuapanich Nuttaset, Zheng Juepeng, Shi Bohan, Liu Jiaying, Jiang Jiayin, Huang Jiatao, Tan Shenghan, Li Qingmei, Fu Haohuan | School of Artificial Intelligence, Sun Yat-Sen University；National Supercomputing Center in Shenzhen；Khoury College of Computer Sciences, Northeastern University；Tsinghua Shenzhen International Graduate School, Tsinghua University | 提出基于噪声历史地图的无监督学习方法，实现2020-2024年马来西亚和印度尼西亚油棕榈时序制图，无需人工标注。 | [#412](https://github.com/thinson/RS-PaperClaw/issues/412) |
| [20260426] A Synergistic CNN-Transformer Network with Pooling Attention Fusion for Hyperspectral Image Classification | Chen Peng, He Wenxuan, Qian Feng, Shi Guangyao, Yan Jingwen | College of Engineering, Shantou University；School of Electronic Information and Communications, Huazhong University of Science and Technology；Changchun Institute of Optics, Fine Mechanics and Physics, Chinese Academy of Sciences；School of Computer Science and Technology, Chongqing University of Posts and Telecommunications；School of Intelligent Manufacturing and Electrical Engineering, Guangzhou Institute of Science and Technology | 设计CNN-Transformer协同网络，通过池化注意力融合机制联合提取高光谱图像空谱特征以提升分类性能。 | [#413](https://github.com/thinson/RS-PaperClaw/issues/413) |
| [20260426] Comparative Study of Weighted and Coupled Second- and Fourth-Order PDEs for Image Despeckling in Grayscale, Color, SAR, and Ultrasound | Kumar Manish, Rajendra K. Ray | School of Mathematical and Statistical Sciences, Indian Institute of Technology Mandi | 系统比较加权与耦合的二阶、四阶偏微分方程模型，评估其在灰度、彩色、SAR及超声图像去噪中的效果。 | [#414](https://github.com/thinson/RS-PaperClaw/issues/414) |

## 🔎 观察

- 弱监督与无监督学习成为遥感大样本标注瓶颈的重要突破口，历史数据再利用价值凸显。
- Transformer架构持续向高光谱等细粒度任务渗透，但CNN局部特征提取仍具不可替代性。

---

Powered by OpenClaw🦞

---
