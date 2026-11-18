# Daily Reports

最近三天日报（最新在前）：

# [20261117](./202611/20261117.md)
## 📌 今日概况

今日共检索候选论文 16 篇；关键词+LLM 智能匹配遥感交叉论文 8 篇；最终纳入日报 8 篇。

今日研究趋势呈现多模态融合与生成式方法在遥感中的深化应用。SWIR波段合成与高光谱-LiDAR分类均强调跨模态特征校正与可靠性驱动学习；超分辨率工作引入2D高斯泼溅实现任意尺度重建；SAR基础模型适配多模态大语言模型成为新方向。此外，无训练变化检测与事件相机海上搜救检测拓展了遥感应用边界，极化SAR统计建模与高海拔小目标数据集则夯实了基础方法与数据支撑。

## ✨ 今日亮点

- SWIR-cGAN利用条件GAN与注意力U-Net从VNIR影像合成短波红外波段，缓解数据稀缺。
- 2D高斯泼溅结合亚像素偏移帧实现任意尺度遥感超分，仅需一次编码。
- Sarvia快速适配MLLM中已有的SAR基础模型，降低SAR多模态应用门槛。

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20261117] SWIR-cGAN: Synthesizing SWIR Bands Using VNIR Imagery from CBERS and AMAZONIA-1 | Alisson Cleiton de Oliveira, Rennan de Freitas Bezerra Marujo, Thales Sehn Körting | 原文作者栏未列出单位 | 提出SWIR-cGAN，用条件GAN和注意力U-Net从CBERS与AMAZONIA-1的VNIR影像合成SWIR波段。 | [#1643](https://github.com/thinson/RS-PaperClaw/issues/1643) |
| [20261117] You Only Encode Once: Sub-Pixel-Shifted Frames for Arbitrary-Scale Remote Sensing Super-Resolution with 2D Gaussian Splatting | Liu Canjie, Wang Liuqian, Ming Qi, Lu Wei, Hao Xiaohan, Wu Yuefei, Chao Wentao, Shi Lei | Zhengzhou University；Beijing University of Technology；Anhui University | 提出仅编码一次框架，利用亚像素偏移帧与2D高斯泼溅实现任意尺度遥感多帧超分辨率。 | [#1644](https://github.com/thinson/RS-PaperClaw/issues/1644) |
| [20261117] Reliability-Driven Feature Correction for Hyperspectral and LiDAR Classification | Zhang Lianming, Wang Xiaolu, Song Qiya, Liu Jinyang, Dian Renwei, Kang Xudong | School of Information Science and Engineering, Hunan Normal University, Changsha, China | 面向高光谱与LiDAR分类，设计可靠性驱动特征校正模块与类原型库以融合跨模态信息。 | [#1645](https://github.com/thinson/RS-PaperClaw/issues/1645) |
| [20261117] SARVIA: Fast-Adapting the Strong SAR Foundation Models That Are Already in Your MLLMs | Li Yuxuan, Tian Zichen, Sun Qianru | Singapore Management University | Sarvia快速适配多模态大语言模型中已有的强SAR基础模型，实现自适应后预训练。 | [#1646](https://github.com/thinson/RS-PaperClaw/issues/1646) |
| [20261117] Event-Based Person Detection for Maritime UAV Search | Ning Zijie, Vandewalle Patrick | EAVISE-PSI, ESAT, KU Leuven | 面向海上无人机搜救，构建基于事件相机的人员检测方法以应对动态视觉挑战。 | [#1647](https://github.com/thinson/RS-PaperClaw/issues/1647) |
| [20261117] Training-Free Building Change Detection with Example-Induced Discriminants | Lu Zhi, Hong Bin, Peng Zhenming | University of Electronic Science | 提出无训练建筑物变化检测框架，利用示例诱导线性判别与特征对比实现ViT特征迁移。 | [#1648](https://github.com/thinson/RS-PaperClaw/issues/1648) |
| [20261117] Generation of Sample Complex Wishart Distributed Matrices and Change Detection in Polarimetric SAR Data | Allan A. Nielsen, Skriver Henning, Conradsen Knut | pt Technical University of Denmark；pt b DTU Space -- National Space Institute | 研究极化SAR样本复Wishart矩阵生成及基于检验统计量的变化检测方法。 | [#1649](https://github.com/thinson/RS-PaperClaw/issues/1649) |
| [20261117] A tiny object detection dataset for high-altitude open-water search and rescue | Xu Hui, Hou Chenfei, Wei Henglai, Wang Hao, Jin Yidong, Niu Xiulin, Zhang Haoyang, Zhang Hui, Xu Tianshi | School of Transportation Science and Engineering, Beihang University, Beijing 100191, China；Hangzhou International Innovation Institute of Beihang University, Beihang University | 发布高海拔开阔水域搜救小目标检测数据集，聚焦救生圈等微小目标识别。 | [#1650](https://github.com/thinson/RS-PaperClaw/issues/1650) |

## 🔎 观察

- 生成式与基础模型适配成为遥感新增长点，但合成波段与模型迁移的物理一致性仍需验证。
- 无训练与轻量化方法在变化检测和超分中兴起，反映对标注依赖和计算成本的持续关注。

---

Powered by OpenClaw🦞

<!-- rs-pipeline: {"date": "20261117", "source": "api", "checked_at": "2026-11-18T10:22:54+00:00", "source_complete": true, "candidate_count": 16, "paper_count": 8} -->

---

# [20261108](./202611/20261108.md)
## 📌 今日概况

今日共检索候选论文 4 篇；关键词+LLM 智能匹配遥感交叉论文 2 篇；最终纳入日报 2 篇。

今日研究聚焦遥感数据的高效利用与模型可解释性。一方面，利用多光谱卫星数据直接进行地表太阳辐射临近预报，结合时序注意力机制提升预测精度；另一方面，探索稀疏自编码器分解地球观测基础模型嵌入特征，以增强可解释性。两项工作分别从应用与理论层面推动遥感AI发展，体现了对实时预测与模型透明度的共同关注。

## ✨ 今日亮点

- 多光谱卫星数据直接用于地表太阳辐射临近预报，结合时序注意力提升精度。
- 稀疏自编码器分解地球嵌入特征，增强基础模型可解释性。
- 研究覆盖应用预测与理论解释，体现遥感AI多维度发展。

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20261108] Direct Multispectral Satellite Nowcasting of Gridded Surface Solar Radiation | Xie Tianyu, Zeng Zhaoliang, Liang Zhehao, Gui Ke, Zhang Xutao, Wang Yaqiang, Guan Dabo, Che Huizheng | ¹ State Key Laboratory of Severe Weather Meteorological Science and Technology, Chinese Academy；² Xiong'an Institute of Meteorological Artificial Intelligence, Xiong'an, Hebei, China；Department of Earth System Sciences, Tsinghua University, Beijing 10084, China；The Bartlett School of Sustainable Construction, University College London, London WC1 E 7 HB | 利用Himawari-8多光谱卫星数据与时序注意力，直接临近预报网格化地表太阳辐射。 | [#1626](https://github.com/thinson/RS-PaperClaw/issues/1626) |
| [20261108] Decomposing Earth Embeddings with Sparse Autoencoders | Benson Vitus, Yang Fanny, Reichstein Markus | Max Planck Institute for Biogeochemistry, Jena, Germany | 采用稀疏自编码器分解地球观测基础模型嵌入，提升特征可解释性。 | [#1627](https://github.com/thinson/RS-PaperClaw/issues/1627) |

## 🔎 观察

- 临近预报与可解释性成为遥感AI热点，分别对应实时应用与模型信任需求。
- 多光谱数据与基础模型结合，显示遥感AI向数据驱动与解释并重演进。

---

Powered by OpenClaw🦞

<!-- rs-pipeline: {"date": "20261108", "source": "api", "checked_at": "2026-11-12T04:16:17+00:00", "source_complete": true, "candidate_count": 4, "paper_count": 2} -->

---

# [20261102](./202611/20261102.md)
## 📌 今日概况

今日共检索候选论文 14 篇；关键词+LLM 智能匹配遥感交叉论文 11 篇；最终纳入日报 11 篇。

今日研究聚焦多源遥感数据融合与视觉语言模型在遥感中的应用。高光谱分类与跟踪引入测试时训练和光谱提示，多源分类强调共享模式与频率感知融合。视觉语言模型向决策与文本定位拓展，域泛化与增量变化检测受到关注。超分辨与水下图像恢复侧重数据合成与保真度评估。

## ✨ 今日亮点

- 视觉测试时训练与光谱提示用于高光谱分类和跟踪
- 多源遥感分类强调共享模式与频率感知跨层融合
- 视觉语言模型拓展至地球观测决策与阿拉伯地理文本定位

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20261102] Spectral-spatial vision test-time training for hyperspectral image classification | Zhao Xiang | College of Mathematical Sciences, Harbin Engineering University | 提出光谱-空间视觉测试时训练方法，用于高光谱图像分类。 | [#1614](https://github.com/thinson/RS-PaperClaw/issues/1614) |
| [20261102] Latent Spectral Prompting for Multimodal Hyperspectral Object Tracking | Cai Wangshu, Zhou Jun, Wang Lei, Mohammad Aminul Islam, Han Xu, Paliwal Kuldip | Griffith University, Australia；East China Normal University, China；Bangladesh Agricultural University, Bangladesh | 引入潜在光谱提示，缓解RGB与高光谱域差异以提升多模态跟踪。 | [#1615](https://github.com/thinson/RS-PaperClaw/issues/1615) |
| [20261102] Performance evaluation of super-resolution techniques for characterization and phenotyping of commodity crops using multispectral imagery | Karukayil Abhiram, João F. C. Mota, Vásquez-Guevara Mateo, Arevalo-Ramirez Tito, Fernando Auat Cheein | School of Engineering and Physical Sciences, Heriot-Watt University, Edinburgh, UK；Department of Electrical Engineering, Department of Mechanical Engineering and Metallurgy, School of Engineering, Faculty of；School of Mathematical and Computer Sciences, Heriot-Watt University, Edinburgh, UK；Harper Adams University, England, UK | 评估超分辨技术对多光谱作物表征与表型分析性能的影响。 | [#1616](https://github.com/thinson/RS-PaperClaw/issues/1616) |
| [20261102] Bridging Low-Level Image Fusion and High-Level Semantic Understanding | Dong Guangyuan, Shen Lingdong, Zhang Xudong, Jing Haodong, Wang Haoyu, Li Zihao, Ying Zonghao, Song Ziyu, Liu Shenghao, Luo Jiachen, Zhang Hao | Peking University；Xi'an Jiaotong University；Nankai University；Institute of Automation, Chinese Academy of Sciences | 连接低层图像融合与高层语义理解，结合对比学习和视觉语言模型。 | [#1617](https://github.com/thinson/RS-PaperClaw/issues/1617) |
| [20261102] Shared-Pattern Collaborative Network for Multi-Source Remote Sensing Data Classification | Yang Chenfang, Gong Chuanzheng, Gao Feng, Dong Junyu, Du Qian | State Key Laboratory of Physical Oceanography, Ocean University of China, Qingdao, China. (；Department of Electrical and Computer Engineering, Mississippi State University, Starkville, MS USA | 提出共享模式协作网络，用于多源遥感数据分类与跨模态学习。 | [#1618](https://github.com/thinson/RS-PaperClaw/issues/1618) |
| [20261102] Cross-Layer Refinement and Frequency-aware Fusion Network for Multi-Source Remote Sensing Image Classification | Xiao Wenhan, Gong Chuanzheng, Gao Feng, Dong Junyu, Du Qian | State Key Laboratory of Physical Oceanography, Ocean University of China, Qingdao, China；Department of Electrical and Computer Engineering, Mississippi State University, Starkville, MS USA. and elevation information [4] | 设计跨层细化与频率感知融合网络，提升多源遥感图像分类。 | [#1619](https://github.com/thinson/RS-PaperClaw/issues/1619) |
| [20261102] KAUSTics-Net: Diffusion-Based Through-Water UAV Restoration with a Semi-Synthetic Dataset | Scilla Dario, Omar A. Lopez, Johansen Kasper, Brian O. Nieuwenhuis, Matthew F. McCabe | and Livability Initiative, King Abdullah University of Science and Technology；Red Sea Research Center, Biological and Environmental Science and；Engineering Division, King Abdullah University of Science and Technology | 基于扩散模型和半合成数据集，恢复浅水环境无人机水下图像。 | [#1620](https://github.com/thinson/RS-PaperClaw/issues/1620) |
| [20261102] HyperFlow: Class-Incremental Semantic Change Detection via Hyperbolic Flow | Béchaz Manon, Buecher Léo, Dalsasso Emanuele, Tomoiaga Ciprian, Jayet Patrick, Detyniecki Marcin, Chapel Laetitia, Drumetz Lucas, Courty Nicolas, Tuia Devis | University of the Witwatersrand；Université de Bretagne Sud, France；Institut Agro Rennes-Angers, France；Lab-STICC | 利用双曲流实现类增量语义变化检测，建模地物覆盖转变。 | [#1621](https://github.com/thinson/RS-PaperClaw/issues/1621) |
| [20261102] EO-Jev: Decision Model for Earth Observation | Mohamed Atef Abouelhadid, Diaa Addeen Abuhani, Muhammad Akhtar Munir, Fahad Shahbaz Khan, Khan Salman | Mohamed Bin Zayed University of Artificial Intelligence；Massachusetts Institute of Technology；Australian National University；Linköping University Sweden | 构建地球观测决策模型，结合视觉语言模型与低秩微调校准。 | [#1622](https://github.com/thinson/RS-PaperClaw/issues/1622) |
| [20261102] ArabGeoText: Tool-Augmented Vision-Language Models for Arabic Geospatial Text Spotting | Bazi Yakoub, Alsaleh Sarah, Mohamad M. Al Rahhal, Mohamed A. Mekhtiche, Zuair Mansour | the Computer Engineering Department, College of Computer and Information Sciences, King Saud University, Riyadh, Saudi Arabia (；the Applied Computer Science Department, College of Applied Computer Science, King Saud University, Riyadh, Saudi Arabia ( | 提出工具增强视觉语言模型与基准数据集，用于阿拉伯地理文本定位。 | [#1623](https://github.com/thinson/RS-PaperClaw/issues/1623) |
| [20261102] ASCoR: Asymmetric Semantic-Spatial Learning for Remote Sensing Domain Generalization | Wang Zitong, Lyu Shuchang, Li Meng, Wang Qiang, Cheng Guangliang, Shi Zhenwei | Beihang University；University of Science and Technology Beijing；University of Liverpool；Guangdong Electronic Information Engineering Research Institute, University of Electronic Science and Technology of China | 采用非对称语义-空间学习，提升遥感语义分割域泛化能力。 | [#1624](https://github.com/thinson/RS-PaperClaw/issues/1624) |

## 🔎 观察

- 高光谱与多源融合研究正从单一特征提取转向测试时适应和跨模态提示，强调域差异缓解。
- 视觉语言模型在遥感中从描述生成走向决策与文本定位，工具增强和校准成为新关注点。

---

Powered by OpenClaw🦞

<!-- rs-pipeline: {"date": "20261102", "source": "oai", "checked_at": "2026-11-03T12:40:22+00:00", "source_complete": true, "candidate_count": 14, "paper_count": 11} -->

---
