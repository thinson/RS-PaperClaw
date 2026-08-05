# Daily Reports

最近三天日报（最新在前）：

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

# [20260802](./202608/20260802.md)
## 📌 今日概况

今日共检索候选论文 7 篇；关键词+LLM 智能匹配遥感交叉论文 4 篇；最终纳入日报 4 篇。

今日研究聚焦于遥感AI的多个前沿方向：自动驾驶高精地图构建、高光谱水果成熟度预测、脉冲神经网络的分布外检测，以及跨视角地理定位。多模态融合与高效架构（如混合专家、脉冲集成）成为提升性能的关键，同时注重实际应用中的计算效率与鲁棒性。

## ✨ 今日亮点

- 高精地图构建引入人类驾驶行为模仿，提升在线建图效率。
- 脉冲伪集成方法缓解多样性坍缩，增强遥感OOD检测能力。
- 稀疏混合专家实现多尺度跨视角定位，兼顾精度与效率。

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260802] Driver2Map: Imitating Human Driving for Online High-Definition Map Construction | Yin Pan, Xia Runtian, Kuang Weisong, Li Kaiyu, Zhao Cong, Cao Xiangyong | Xi’an Jiaotong University | 模仿人类驾驶行为，利用多模态融合与相机位姿在线构建高精地图。 | [#1020](https://github.com/thinson/RS-PaperClaw/issues/1020) |
| [20260802] Fruit-HSNet: A Machine Learning Approach for Hyperspectral Image-Based Fruit Ripeness Prediction | Ahmed Baha Ben Jmaa, Chaieb Faten, Fabijańska Anna | Efrei Research Lab, Paris Panthéon-Assas University, Paris, France；Institute of Applied Computer Science, Lodz University of Technology, Łódź, Poland | 结合傅里叶变换与特征融合，基于高光谱图像预测水果成熟度。 | [#1021](https://github.com/thinson/RS-PaperClaw/issues/1021) |
| [20260802] Breaking Diversity Collapse in Spiking Pseudo-Ensembles for Efficient OOD Detection in Remote Sensing | Anumasa Srinivas, Shah Rushi, Zou Qiran, Liu Dianbo | National University of Singapore | 通过脉冲伪集成打破多样性坍缩，提升遥感分布外检测效率。 | [#1022](https://github.com/thinson/RS-PaperClaw/issues/1022) |
| [20260802] One Query, Many Scales: Sparse Mixture-of-Experts for Efficient Hierarchical Cross-View Geo-Localization | Fan Ruijie, Ye Junyan, Zhu Qi, Li Weijia | Tsinghua Shenzhen International Graduate School, Tsinghua University；School of Geospatial Engineering and Science, Sun Yat-sen University | 采用稀疏混合专家与多尺度表示，实现高效层级跨视角地理定位。 | [#1023](https://github.com/thinson/RS-PaperClaw/issues/1023) |

## 🔎 观察

- 多篇论文强调计算效率与鲁棒性，反映遥感AI向轻量化和实用化发展。
- 跨模态与跨尺度融合成为主流，但脉冲网络等新型架构仍待突破。

---

Powered by OpenClaw🦞

---
