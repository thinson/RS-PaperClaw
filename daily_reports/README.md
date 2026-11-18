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

# [20261116](./202611/20261116.md)
## 📌 今日概况

今日共检索候选论文 22 篇；关键词+LLM 智能匹配遥感交叉论文 11 篇；最终纳入日报 11 篇。

今日研究覆盖SAR目标识别、遥感图像生成评估、灾害风险与应急响应、超高分遥感视觉语言模型、SAR层析与洪泛区监测等方向。趋势上，多篇工作反思模型可靠性：SAR识别关注背景捷径与角度缺口，生成评估引入人类偏好基准，灾害筛查开展回溯失败分析。同时，多模态融合与交互式分割推动三维场景理解，无人机影像中的冗余检测抑制与多类别重识别基准受到关注。

## ✨ 今日亮点

- SAR车辆识别研究揭示背景捷径与角度缺口对性能的影响，强调评估需控制混杂因素。
- 遥感感知相似性研究引入多层注意力评分与人类偏好基准，推动生成质量评估更贴近人眼。
- 多篇灾害相关研究聚焦应急场景：野火风险评估、洪泛区监测与无人机冗余检测抑制。

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20261116] How Much of SAR Vehicle Recognition Is the Vehicle? Background Shortcuts, Angle Gaps and Partial Libraries on MSTAR and ATRNet-STAR | Shaya Mousa | Arizona State University, Tempe, AZ, USA ( | 分析MSTAR与ATRNet-STAR上SAR车辆识别中的背景捷径、角度缺口与部分库问题，反思性能来源。 | [#1652](https://github.com/thinson/RS-PaperClaw/issues/1652) |
| [20261116] Rethinking Perceptual Similarity for Remote Sensing: Multi-Layer Attention Scoring and Human Preference Benchmarking | Underwood Eli, Bosch Marc, Joshi Neil, Wen Jeffrey, Brown Myron | Johns Hopkins University Applied Physics Laboratory；Duke University | 针对遥感图像生成提出多层注意力感知相似性评分，并构建人类偏好基准以校准评估。 | [#1653](https://github.com/thinson/RS-PaperClaw/issues/1653) |
| [20261116] Wildfire-SSR: Geolocation-Aware Multimodal Fusion for Structure-Level Wildfire Risk Assessment | Ho Yu-Hsuan, Xiao Yiming, Lai Hao-En, Mostafavi Ali, Samuel D. Brody | Urban Resilience.AI Lab, Zachry Department of Civil and Environmental Engineering；Texas A&M University, College Station, TX；Artie McFerrin Department of Chemical Engineering；Institute for Disaster Resilient Texas, Texas A&M University, Houston, TX | 提出地理定位感知的多模态融合方法，结合视觉语言模型评估建筑级野火风险。 | [#1654](https://github.com/thinson/RS-PaperClaw/issues/1654) |
| [20261116] Out of Sight, Into Memory: Compact Visual Latents Retain Local Evidence in Ultra-High-Resolution Remote Sensing | Tang Meng, Du Siyuan, Liu Yuxin, Cao Shuaishuai, Wang Di, Guo Haonan | aberAberystwyth University；njuNanjing University；pkuPeking University；csuCentral South University；whuWuhan University | 面向超高分遥感问答，提出紧凑视觉潜记忆以在压缩令牌的同时保留局部证据。 | [#1655](https://github.com/thinson/RS-PaperClaw/issues/1655) |
| [20261116] From very fine Vertical Resolution to Range Super-Resolution on BIOMASS P-BAND SAR Data | Yu Yanghai, Tebaldini Stefano, Lei Yang, Rocca Fabio | RIDE Lab, Dipartimento di Elettronica, Informazione e Bioingegneria, Politecnico di Milano；National Space Science Center, Chinese Academy of Sciences | 利用BIOMASS P波段SAR数据，从精细垂直分辨率出发实现距离向超分辨与层析分析。 | [#1656](https://github.com/thinson/RS-PaperClaw/issues/1656) |
| [20261116] Model-based neural network for global floodplains analysis | Audisio Pierre, Belletti Barbara, Pustelnik Nelly | ENS de Lyon, CNRS, Laboratoire de Physique, F-69342 Lyon, France；Université Jean Monnet, CNRS, UMR | 提出基于模型的神经网络，融合多光谱超分辨开展全球洪泛区分析。 | [#1657](https://github.com/thinson/RS-PaperClaw/issues/1657) |
| [20261116] Counting What Matters: Reducing Redundant Object Detections in Overlapping UAV Mapping Imagery for Disaster Response | Schulte Max, Surmann Hartmut, Meine Julien | Westphalian University of Applied Sciences (WH) Gelsenkirchen, Germany | 针对重叠无人机测绘影像，减少灾害响应目标检测中的冗余重复计数。 | [#1658](https://github.com/thinson/RS-PaperClaw/issues/1658) |
| [20261116] Deep Learning for Satellite-Based Mountain Hazard Screening: A Retrospective Failure Analysis on the 2021 Chamoli Rock-Ice Avalanche | Rakshit Snigdhajyoti | School of Computing Science and Engineering, VIT Bhopal University, India | 对2021 Chamoli岩冰崩开展卫星深度学习筛查的回溯失败分析，揭示筛查局限。 | [#1659](https://github.com/thinson/RS-PaperClaw/issues/1659) |
| [20261116] STARS: Stage-Adaptive Responsibility Separation for Shadow Removal in Remote Sensing Images | Song Gaoliang, Li Chengjie, Liu Pengju, Chang Chenchen, You Jinhao, Zhang Hongzhi | Harbin Institute of Technology；Northeast Forestry University | 提出阶段自适应责任分离的级联架构，用于遥感图像阴影去除。 | [#1660](https://github.com/thinson/RS-PaperClaw/issues/1660) |
| [20261116] InterRSGaussian: Interactive Multi-view Instance Segmentation for 3D Remote Sensing Scenes | Qi Zipeng, Zou Zhengxia, Shi Zhenwei | aSchool of Astronautics, Beihang University, Beijing, 100191, China；bKey Laboratory of Spacecraft Design Optimization and Dynamic Simulation Technologies, Ministry of Education, Beihang；University, Beijing, 100191, China | 基于3D高斯开展交互式多视图实例分割，面向三维遥感场景理解。 | [#1661](https://github.com/thinson/RS-PaperClaw/issues/1661) |
| [20261116] VisDrone-ReID: A Unified Multi-Category Object Re-Identification Benchmark | Asmau Lawal Bilbis, Nathanael L. Baisa, Jayavel Amudhavel | School of Computer Science and Informatics；De montfort University | 构建VisDrone-ReID统一多类别目标重识别基准，支持无人机影像留一评估。 | [#1662](https://github.com/thinson/RS-PaperClaw/issues/1662) |

## 🔎 观察

- 今日多篇工作从追求精度转向审视评估可靠性，背景捷径、失败回溯与人类偏好基准成为共同关切。
- 灾害与应急应用密集出现，方法覆盖多模态融合、冗余检测抑制与筛查失败分析，强调落地约束。

---

Powered by OpenClaw🦞

<!-- rs-pipeline: {"date": "20261116", "source": "api", "checked_at": "2026-11-18T10:28:26+00:00", "source_complete": true, "candidate_count": 22, "paper_count": 11} -->

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
