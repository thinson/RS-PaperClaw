# Daily Reports

最近三天日报（最新在前）：

# [20260805](./202608/20260805.md)
## 📌 今日概况

今日共检索候选论文 11 篇；关键词+LLM 智能匹配遥感交叉论文 8 篇；最终纳入日报 8 篇。

今日遥感AI研究聚焦于基础模型应用与数据安全。多篇论文探索地理空间基础模型在生物量估算中的潜力，同时关注联邦学习与视觉语言模型的结合。此外，研究涉及Sentinel-1时序分析、海上风电基础设施监测、多标签分类设计选择分析，以及针对遥感目标检测的物理对抗攻击，显示出对模型鲁棒性和实际部署的重视。

## ✨ 今日亮点

- 地理空间基础模型助力生物量估算，提升碳监测精度。
- 遥感深伪检测基准数据集构建，保障数据安全。
- 联邦学习与视觉语言模型结合，应对非独立同分布数据。

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260805] Above-ground Biomass Estimation with Geospatial Foundation Models | Sialellia Ghjulia, Scheibenreif Linus, Jan Dirk Wegner, Schindler Konrad | ETH AI Center, Zurich, 8092, Switzerland；EcoVision Lab, Department of Mathematical Modeling and Machine | 利用地理空间基础模型回归估算地上生物量，支持碳储量监测。 | [#893](https://github.com/thinson/RS-PaperClaw/issues/893) |
| [20260805] DefoEye: Python-Based Software for Facilitating Time-Series InSAR Analysis of Sentinel-1 Remote-Sensing Data | Alireza Taheri Dehkordi, Hashemi Hossein, Naghibi Amir | United Nations University Hub on Water in a Changing Environment (WICE), United Nations University Institute；for Water, Environment and Health (UNU-INWEH), Lund University, Lund, Sweden；Centre for Advanced Middle Eastern Studies, Lund university, Lund, Sweden | DefoEye软件简化Sentinel-1时序InSAR分析，用于形变监测。 | [#1047](https://github.com/thinson/RS-PaperClaw/issues/1047) |
| [20260805] Towards a satellite image manipulation and deepfake localization benchmark dataset | Arndt Jacob, Varshney Debvrat, Dias Philipe, Nukavarapu Nivedita | Oak Ridge National Laboratory | 构建卫星图像篡改与深伪定位基准数据集，推动取证研究。 | [#1048](https://github.com/thinson/RS-PaperClaw/issues/1048) |
| [20260805] On the Effectiveness of Adaptation Strategies for VLM-Based Federated Learning in Remote Sensing | Lösche Simon, Büyüktaş Barış, Adler Mathis, Zavras Angelos, Papoutsis Ioannis, Demir Begüm | Technische Universität Berlin；Orion Lab, School of Rural, Surveying and Geoinformatics Engineering, National Technical；University of Athens；Institute of Astronomy, Astrophysics, Space Applications and Remote Sensing, National；Department of Informatics and Telematics, Harokopio University of Athens | 评估遥感联邦学习中视觉语言模型的不同适应策略效果。 | [#1049](https://github.com/thinson/RS-PaperClaw/issues/1049) |
| [20260805] Benchmarking Deep Learning Models for Dense Event Classification of Offshore Wind Infrastructure in Sentinel-1 Time Series | Hoeser Thorsten, Bachofer Felix, Kuenzer Claudia | Earth Observation Center (EOC), German Aerospace Center (DLR), Oberpfaffenhofen；Institute for Geography and Geology, University of Wuerzburg | 基准测试深度学习模型对Sentinel-1时序海上风电事件的分类性能。 | [#1050](https://github.com/thinson/RS-PaperClaw/issues/1050) |
| [20260805] Design Choices That Matter: A Functional ANOVA Analysis for Remote Sensing Multi-Label Classification | Maryam Gholami Shiri, Tuba Eva, Džeroski Sašo, Eftimov Tome, Nikolikj Ana | Department of Knowledge Technologies, Jožef Stefan Institute, Ljubljana, Slovenia；Jožef Stefan International Postgraduate School, Ljubljana, Slovenia；Computer Systems Department, Jožef Stefan Institute, Ljubljana, Slovenia；Trinity University, San Antonio, TX, USA；Singidunum University, Belgrade, Serbia | 通过功能方差分析揭示遥感多标签分类中关键设计选择的影响。 | [#1051](https://github.com/thinson/RS-PaperClaw/issues/1051) |
| [20260805] OutLangSplat: 3D Language Gaussian Splatting for UAV Outdoor Scenes | Yan Xia, Wu He, Xu Yanghui, Wu Zizhao, Chen Jiazhou | Zhejiang University of Technology；Hangzhou Dianzi University | 提出OutLangSplat，将3D语言高斯泼溅应用于无人机户外场景分割。 | [#1052](https://github.com/thinson/RS-PaperClaw/issues/1052) |
| [20260805] ColorFD: A Finite-Difference Guided Black-Box Physical Adversarial Attack for Remote Sensing Object Detection | Guo Tiannuo, Qiu Guhang, Xie Yuzhen, Feng Rui, Li Ligang, Xiang Deliang | College of Information Science and Technology, Beijing University of Chemical Technology, Beijing, China ( | 提出ColorFD，基于有限差分的黑盒物理对抗攻击方法用于遥感检测。 | [#1053](https://github.com/thinson/RS-PaperClaw/issues/1053) |

## 🔎 观察

- 基础模型在遥感中的应用从分类扩展到回归任务，如生物量估算，显示其通用性增强。
- 对抗攻击与深伪检测研究增多，反映遥感数据安全与模型鲁棒性成为关注焦点。

---

Powered by OpenClaw🦞

---

# [20260804](./202608/20260804.md)
## 📌 今日概况

今日共检索候选论文 13 篇；关键词+LLM 智能匹配遥感交叉论文 8 篇；最终纳入日报 6 篇。

今日遥感AI研究聚焦于基础模型与多模态融合，涵盖地球嵌入、城市理解、分割与生成任务。多篇工作探索视觉-语言模型在遥感分割中的应用，并引入原型演化、知识蒸馏等机制。同时，物理信息引导的扩散模型用于洪水合成，地理先验辅助3D场景补全，整体呈现从通用表征到任务专用优化的趋势。

## ✨ 今日亮点

- 多模态嵌入与视觉-语言模型成为遥感分割研究热点。
- 物理先验与地理信息被引入生成及3D任务。
- 基础模型通过蒸馏与提示学习适配遥感场景。

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260804] Earth Embeddings | Adam J. Stewart, Fang Heng, Isaac A. Corley, Xiao Xiang Zhu | Chair of Data Science in Earth Observation, Technical University of Munich, Munich, Germany；KTH Royal Institute of Technology, Stockholm, Sweden | 提出Earth Embeddings，用于土地覆盖制图的卫星影像嵌入产品。 | [#482](https://github.com/thinson/RS-PaperClaw/issues/482) |
| [20260804] UniEvo-RS: Omni-Prompt Unified Remote Sensing Segmentation with Representative Exemplar-Driven Prototype Evolution | Zhang Kunquan, Li Peilang, Hu Xikun, Yang Yunkai, Zou Yushan, Zhang Zhiwei, Dong Runmin | Sun Yat-sen University National University of Defense Technology | UniEvo-RS采用原型演化实现遥感分割的全提示统一框架。 | [#1041](https://github.com/thinson/RS-PaperClaw/issues/1041) |
| [20260804] Geo-Embed: Towards Unified Multimodal Embeddings for Urban Understanding | Li Jiapeng, Li Yong, Zhou Junjie, Zhang Fan, Liu Yu | Peking University；Beijing University of Posts and Telecommunications | Geo-Embed构建城市理解的多模态统一嵌入，支持变化检测。 | [#1042](https://github.com/thinson/RS-PaperClaw/issues/1042) |
| [20260804] FlowForm: Synergizing Fluid Physics with Topological Consistency for Satellite Flood Synthesis | Weihui Zhang, Ruizhi Wang, Hongye Xu, Huiqiong Wang, Li Sun, Mingli Song | Zhejiang University, Zhejiang, China | FlowForm结合流体物理与拓扑一致性合成卫星洪水图像。 | [#1043](https://github.com/thinson/RS-PaperClaw/issues/1043) |
| [20260804] Geospatial-Prior Guidance for 3D Semantic Scene Completion | Wang Meng, Zhang Shougao, He Wenzhe, Li Ruihui, Hu Nan, Tang Zhuo, Li Kenli | College of Computer Science and Electronic Engineering, Hunan University, Hunan, China | 利用地理先验（如OSM）引导3D语义场景补全。 | [#1044](https://github.com/thinson/RS-PaperClaw/issues/1044) |
| [20260804] CROSS: Cascaded Distillation and Dual-Constraint Grounding for Remote Sensing Referring Segmentation | Luo Tingzhang, Liu Ruizhong, Liu Yichao, Fan Cheng, Liu Yu, Guo Jianyuan | City University of Hong Kong；The Hong Kong University of Science and Technology (Guangzhou)；Nankai University；Peking University | CROSS通过级联蒸馏与双约束实现遥感指代分割。 | [#1045](https://github.com/thinson/RS-PaperClaw/issues/1045) |

## ⚠️ 未纳入日报的匹配论文

以下论文通过关键词/LLM 筛选，但在处理过程中失败未纳入日报。点击 arXiv 链接可查看原文。

| 标题 | arXiv | 失败原因 |
|------|-------|----------|
| Distilled Roads: Generalisable Road Network Extraction Across Sensors, Resolutions, and Region | [2608.03407v1](https://arxiv.org/abs/2608.03407v1) | 质检未通过: 单位为空或无效 |
| Standalone DINOv3 for Training-Free Open-Vocabulary Semantic Segmentation in Remote Sensing | [2608.03023v1](https://arxiv.org/abs/2608.03023v1) | 质检未通过: 单位为空或无效 |


## 🔎 观察

- 视觉-语言模型在遥感分割中应用增多，但多依赖提示工程，泛化性待验证。
- 物理与地理先验的引入表明领域知识正与深度学习深度融合。

---

Powered by OpenClaw🦞

---

# [20260803](./202608/20260803.md)
## 📌 今日概况

今日共检索候选论文 17 篇；关键词+LLM 智能匹配遥感交叉论文 15 篇；最终纳入日报 15 篇。

今日遥感AI研究聚焦于高光谱图像分类与超分辨率、遥感视频理解、灾害监测及基础模型微调。多篇论文引入Mamba架构、扩散模型及自监督学习，推动模型效率与泛化能力提升。同时，新发布多个基准数据集（如GEOID-Flood、RSVideo、OSSDD），促进多模态与视频理解研究。整体趋势显示，遥感AI正从单一任务向跨模态、生成式及基础模型方向发展。

## ✨ 今日亮点

- Mamba架构在高光谱分类与超分辨率中表现突出
- 多模态基准数据集推动灾害监测与视频理解研究
- 基础模型微调与生成式模型成为遥感AI新热点

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260803] Fermat Active Laplace Learning for Semi-Supervised Hyperspectral Image Classification | Buranasiri Vutichart, James M. Murphy | Department of Mathematics；Tufts University | 提出Fermat主动拉普拉斯学习，提升半监督高光谱图像分类性能 | [#1025](https://github.com/thinson/RS-PaperClaw/issues/1025) |
| [20260803] ISRS-DETR: Detection-Guided Click Propagation for Remote Sensing Interactive Segmentation | Thanh Duc Pham, Nguyen Anh, Duong Duc Hieu, Pham Minh-Tan | FPT Software AI Center, Vietnam；Department of Computer Science, University of Liverpool, UK；IRISA, Université Bretagne Sud, UMR 6074 | ISRS-DETR利用检测引导点击传播，改进遥感交互式分割 | [#1026](https://github.com/thinson/RS-PaperClaw/issues/1026) |
| [20260803] UAV-Based Environmental Monitoring of Rip-Current Indicators Using Wavelet-Derived Texture Features | Yonatan Ben Avraham, Binyaminov Baruch, Aperstein Yehudit | Intelligent Systems, Afeka Academic College of Engineering, Tel Aviv 6998812, Israel | 基于小波纹理特征，无人机监测离岸流指示物 | [#1027](https://github.com/thinson/RS-PaperClaw/issues/1027) |
| [20260803] USP-Mamba: Unmixing-Derived Spectral and Structural Prompting for Hyperspectral Image Super-Resolution | Chen Shi, Zhang Jie, Zhou Yicong | Department of Computer Science, University of Macau, Macau, China | USP-Mamba结合光谱解混与提示，实现高光谱超分辨率 | [#1028](https://github.com/thinson/RS-PaperClaw/issues/1028) |
| [20260803] Global-Scale Self-Supervised Spatiotemporal Learning for NDVI Time-Series Reconstruction | Li Ang, Jiang Menghui, Guan Xiaobin, Chu Dong, Shen Huanfeng | School of Geography and Tourism, Anhui Normal University, Wuhu 241002, China；Key Laboratory of Earth Surface Processes and Regional Response in the Yangtze River；Key Laboratory of Geographic Information System of Ministry of Education, Wuhan 430079；Key Laboratory of Digital Cartography and Land Information Application of the Ministry of | 全球尺度自监督时空学习，重建NDVI时间序列 | [#1029](https://github.com/thinson/RS-PaperClaw/issues/1029) |
| [20260803] GEOID-Flood: A Large-Scale Multi-Modal Benchmark Dataset for Flood Segmentation | Chiriaco Gaetano, Barco Luca, Bragagnolo Andrea, Rossi Claudio, Arnaudo Edoardo | Fondazione LINKS；Politecnico di Torino | GEOID-Flood提供多模态洪水分割基准数据集 | [#1030](https://github.com/thinson/RS-PaperClaw/issues/1030) |
| [20260803] Mapping melliferous tree species in Kenya via one-class classification with hyperspectral unsupervised domain adaptation | Luo Zhaozhi, Heiskanen Janne, Vuorinne Ilja, Ocholla Ian, Zhang Shiqi, Järvinen Saana, Wang Xinyu, Zhong Yanfei, Pellikka Petri | School of Emergency Management, Xihua University；School of Remote Sensing and Information Engineering, Wuhan University；State Key Laboratory of Information Engineering in Surveying, Mapping and Remote Sensing, Wuhan University | 无监督域适应用于肯尼亚蜜源树种制图 | [#1031](https://github.com/thinson/RS-PaperClaw/issues/1031) |
| [20260803] RSVideo: Are Your Vision-Language Models Ready for Remote Sensing Videos? | Zhou Hongjie, Wang Shiqin, Chen Haoyang, Guo Haonan, Wang Di, Liu Juhua, Lin Fu, Luo Yong | Wuhan University；Zhongguancun Academy | RSVideo基准评估视觉语言模型在遥感视频理解能力 | [#1032](https://github.com/thinson/RS-PaperClaw/issues/1032) |
| [20260803] OSSDD - a New Open Dataset for Sentinel-1 Ship Detection | Hammer Horst, Hochstuhl Sylvia, Thiele Antje, Brosch Tobias, Davidson Padraig, Remiger Tim, Teutsch Michael | Fraunhofer Institute of Optronics, System Technologies and Image Exploitation - IOSB；Karlsruhe Institute of Technology - KIT | OSSDD发布开放Sentinel-1舰船检测数据集 | [#1033](https://github.com/thinson/RS-PaperClaw/issues/1033) |
| [20260803] PNEC-Mamba: Prototype-Guided Positive-Negative Evidence Calibration for Hyperspectral Image Classification | Xu Mingzhen, Xu Can, Wang Di, Guo Haonan, Du Bo | Wuhan University | PNEC-Mamba通过原型引导证据校准，提升高光谱分类 | [#1034](https://github.com/thinson/RS-PaperClaw/issues/1034) |
| [20260803] Assessing the Benefits of Combining Advanced Deep Learning Techniques for Post-Disaster Building Damage Assessment from UAV Imagery | Huy Quang Ung, Habault Guillaume, Legaspi Roberto, Niu Hao, Cao Lian, Taya Masato | KDDI Research, Inc., Fujimino, Japan | 结合深度学习技术，评估无人机影像建筑损毁 | [#1035](https://github.com/thinson/RS-PaperClaw/issues/1035) |
| [20260803] GeoCore-9B: Towards Geo-Aware Generative Foundation Models in Earth Observation | Do Jeonghyeok, Kim Munchurl | Information \& Electronics Research Institute；School of Electrical Engineering | GeoCore-9B构建地理感知生成式基础模型 | [#1036](https://github.com/thinson/RS-PaperClaw/issues/1036) |
| [20260803] EchoChange: A Diffusion Language Model with Dual Pass Remasking for Factual Remote Sensing Disaster Change Captioning | Sun Dongwei, Yao Bowen, Zhang Yujie, Liu Pei, Yao Jing, Cao Xiangyong | School of Computer Science and Technology and the Ministry of Education Key Lab for Intelligent Networks and Network；Security, Xi’an Jiaotong University, 710049, China；School of Computer Science and Technology, Faculty of Electronic and Information Engineering, Xi’an Jiaotong University；State Key Laboratory of Remote Sensing and Digital Earth, Aerospace Information Research Institute, Chinese Academy of | EchoChange用扩散语言模型实现灾害变化描述 | [#1037](https://github.com/thinson/RS-PaperClaw/issues/1037) |
| [20260803] CoNav-UAV: Cooperative Dual-Altitude Aerial Navigation via Stackelberg Learning | Song Junru, Zhang Wenhao, Yang Yang, Qiu Xuekai, Wang Feifei, Zhou Weien, Jiang Tingsong, Wen Ying, Li Yang, Yao Wen | Shanghai Jiao Tong University；Intelligent Game and Decision Laboratory；Renmin University of China；Shanghai Innovation Institute | CoNav-UAV基于Stackelberg学习实现双高度协同导航 | [#1038](https://github.com/thinson/RS-PaperClaw/issues/1038) |
| [20260803] SPECTRA: Band-Routed Embedding and Stage-Wise LoRA for Cross-Sensor Fine-Tuning of Geospatial Foundation Models | Li Xingyan, Jordan A. Caraballo-Vega, Gong Jie, Mark L. Carroll, Wang Jianwu | University of Maryland, Baltimore County Baltimore Maryland USA；NASA Goddard Space Flight Center Greenbelt Maryland USA；Univ. of Maryland, Baltimore County Baltimore Maryland USA | SPECTRA通过带路由嵌入与LoRA实现跨传感器微调 | [#1039](https://github.com/thinson/RS-PaperClaw/issues/1039) |

## 🔎 观察

- Mamba架构正快速渗透高光谱图像处理，成为Transformer的强有力替代方案
- 遥感基础模型研究从判别式向生成式演进，同时注重参数高效微调

---

Powered by OpenClaw🦞

---
