# Daily Reports

最近三天日报（最新在前）：

# [20260814](./202608/20260814.md)
## 📌 今日概况

今日共检索候选论文 10 篇；关键词+LLM 智能匹配遥感交叉论文 4 篇；最终纳入日报 4 篇。

今日遥感AI研究聚焦于弱监督学习、时序预测与多模态理解。Sentinel-1 SAR影像中极地低压的弱监督分割方法，展示了减少标注依赖的潜力。基于Sentinel-2的作物生长预测模型，利用时序数据提升冬小麦叶面积指数预报精度。此外，针对遥感推理分割的细粒度掩码表示方法，以及结合GeoAI与空间建模的城市冠层评估，共同推动了遥感智能解译向精细化、实用化发展。

## ✨ 今日亮点

- 弱监督分割降低SAR极地低压标注成本
- 时序遥感数据助力作物生长预测
- 细粒度掩码表示提升推理分割精度

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260814] Weakly Supervised Polar Low Segmentation in Sentinel-1 SAR Imagery | Federici Andrea, Grahn Jakob, Boracchi Giacomo, Filippo Maria Bianchi | the Dept. of Mathematics and Statistics, UiT the Arctic University of Norway；NORCE, The Norwegian Research Centre AS | 利用弱监督学习实现Sentinel-1 SAR影像极地低压分割，减少像素级标注需求。 | [#1108](https://github.com/thinson/RS-PaperClaw/issues/1108) |
| [20260814] Learning to Forecast Crop Growth from Earth Observation Data | Senti Dominik, Mehmet Ozgur Turkoglu, Volpi Michele, Aasen Helge | Earth Observation of Agroecosystems Team, Agroscope, Switzerland Swiss Data Science Center, ETH Zurich and EPFL, Switzerland | 基于Sentinel-2时序数据学习预测冬小麦叶面积指数，支持作物生长监测。 | [#1109](https://github.com/thinson/RS-PaperClaw/issues/1109) |
| [20260814] FIRM: Fine-Grained Intra-Token Representation of Masks for Remote Sensing Reasoning Segmentation | Tang Weidong, Li Kaiyu, Wang Yikai, Wu Yanan, Gan Haotian, Wang Shihong, Cao Xiangyong | Xi’an Jiaotong University, Xi’an, China；Renmin University of China, Beijing, China；China Agricultural University, Beijing, China；Shaanxi University of Science and Technology, Xi’an, China | 提出FIRM方法，通过细粒度掩码标记增强遥感推理分割的视觉理解能力。 | [#1110](https://github.com/thinson/RS-PaperClaw/issues/1110) |
| [20260814] From crown candidates to neighborhood screening: integrating optical GeoAI and spatial modeling for urban-canopy assessment in Davis, California | Narimani Mohammadreza, Mitra Shreyan, Farajpoor Parastoo | a Department of Biological and Agricultural Engineering, University of California, Davis, Davis, CA, 95616, USA；b California High School, San Ramon, CA, 94583, USA；pixels and 97.4% of candidate centers agreed with the；homes, active-travel routes, schools, or hot paved surfaces | 集成光学GeoAI与空间模型，实现城市树冠候选检测与邻域筛选评估。 | [#1111](https://github.com/thinson/RS-PaperClaw/issues/1111) |

## 🔎 观察

- 弱监督与多模态方法成为降低遥感标注成本、提升解译精度的双轨趋势。
- 作物预测与城市评估等应用研究，显示遥感AI正加速落地于农业与城市管理。

---

Powered by OpenClaw🦞

---

# [20260813](./202608/20260813.md)
## 📌 今日概况

今日共检索候选论文 6 篇；关键词+LLM 智能匹配遥感交叉论文 4 篇；最终纳入日报 4 篇。

今日遥感AI研究聚焦于视觉-语言模型在地球观测与无人机导航中的应用。LongEarth-R1提出长时序推理基准，DiCoR优化指代分割效率，AirForesight与ARIES-Mission2分别探索跨空间规划与零样本任务生成，整体呈现从感知到推理、从单任务到多模态协同的趋势。

## ✨ 今日亮点

- 长时序遥感推理基准LongEarth-R1发布
- 指代分割新框架DiCoR提升效率
- 无人机视觉语言导航与任务生成受关注

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260813] LongEarth-R1: Benchmarking and Aligning Vision-Language Models for Long-Horizon Earth Observation Reasoning | Ding Yupan, Xiao Jing, Zhang Zhenyuan, Chen Chaofeng, Liao Liang, Xia Gui-Song, Wang Mi | School of Artificial Intelligence, Wuhan University, Wuhan, China；School of Computer Science, Wuhan University, Wuhan, China；Xi’an University of Electronic Science and Technology, Xi’an, China；State Key Laboratory of Information Engineering in Surveying, Mapping and Remote Sensing, Wuhan University, Wuhan | LongEarth-R1构建长时序遥感推理基准并对齐视觉语言模型 | [#1103](https://github.com/thinson/RS-PaperClaw/issues/1103) |
| [20260813] DiCoR: Decoupled Referent Disambiguation and Contour Recalibration for Efficient Referring Remote Sensing Image Segmentation | Gao Ziyang, Jiang Zhizhuo, Chang Jingjing, Yang Yixin, Pan Yuwen, Mao Yong-Qiang, Liu Yu, Chen Hai-Bao | School of Integrated Circuits, School of Information Science and Electronic Engineering, Shanghai Jiao Tong University, Shanghai, China；College of Computer Science, Nankai University, Tianjin, China；Department of Electronic Engineering, Tsinghua Shenzhen International Graduate School, Tsinghua University, Shenzhen, China；Department of Electronic Engineering, Tsinghua University, Beijing, China | DiCoR解耦指代消歧与轮廓重校准，实现高效遥感指代分割 | [#1104](https://github.com/thinson/RS-PaperClaw/issues/1104) |
| [20260813] AirForesight: Current-to-Future Spatial Map Imagination with Cross-Space Planning Consistency for UAV-VLN | Liu Yutong, Li Xiaojie, Xu Mingzhu, Wu Jianlong | Harbin Institute of Technology, Shenzhen Shenzhen China；Shandong University Jinan China；Harbin Institute of Technology, Shenzhen Shenzhen Loop Area Institute Shenzhen China | AirForesight通过跨空间规划一致性实现无人机视觉语言导航 | [#1105](https://github.com/thinson/RS-PaperClaw/issues/1105) |
| [20260813] ARIES-Mission2: A Zero-Shot Vision-Language-Action Framework for Fast Large-Scale Aerial Mission Generation | Wei Junhao, Li Yanxiao, Li Haochen, Zhao Yifu, Yao Dexing, Lu Baili, Li Zikun, Wang Yapeng, Im Sio-Kei, Yang Dingcheng, Yang Xu | Faculty of Applied Sciences；Macao Polytechnic University；School of Economics and Management；South China Normal University；Information Engineering School；Nanchang University | ARIES-Mission2零样本生成大规模无人机任务并优化路线 | [#1106](https://github.com/thinson/RS-PaperClaw/issues/1106) |

## 🔎 观察

- 研究从静态感知转向动态推理，长时序与未来预测成新焦点
- 零样本与高效框架减少标注依赖，推动遥感AI实用化

---

Powered by OpenClaw🦞

---

# [20260812](./202608/20260812.md)
## 📌 今日概况

今日共检索候选论文 14 篇；关键词+LLM 智能匹配遥感交叉论文 11 篇；最终纳入日报 11 篇。

今日研究聚焦于遥感AI的多项前沿应用，涵盖基础模型用于天气降尺度、高光谱图像在食品新鲜度评估中的少样本与轻量化方法、以及基于卫星影像的土地利用与作物检测。此外，扩散模型用于高光谱全色锐化、多模态大语言模型用于无人机图像理解、以及开放词汇变化检测等方向也取得进展。研究趋势显示，模型效率、跨模态融合与少样本学习成为关注重点。

## ✨ 今日亮点

- 基础模型嵌入用于概率天气降尺度，提升描述能力。
- 高光谱成像结合少样本学习，实现鱼类新鲜度日级估计。
- 零样本扩散模型与伪标签学习推动开放词汇变化检测。

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260812] Earth observation embeddings are effective sub-grid descriptors for probabilistic weather downscaling | Sousa Pedro, Tebbutt Will, Jaffer Sadiq, Young Robin, Madhavapeddy Anil, Richard E. Turner | Department of Computer Science, University of Cambridge；Department of Engineering, University of Cambridge | 地球观测嵌入作为亚网格描述符，改进概率天气降尺度性能。 | [#1091](https://github.com/thinson/RS-PaperClaw/issues/1091) |
| [20260812] Few-Shot Ordinal Learning for Day-Wise Freshness Estimation with Hyperspectral Fish Images | Kazi Nabiul Alam, Pooneh Bagheri Zadeh, Sheikh-Akbari Akbar | School of Built Environment, Engineering and Computing；Leeds Beckett University, Leeds, United Kingdom | 少样本序数学习用于高光谱鱼图像，实现日级新鲜度估计。 | [#1092](https://github.com/thinson/RS-PaperClaw/issues/1092) |
| [20260812] Domain-Aware Lightweight Spectral-Grouped Convolutions for Hyperspectral Fish Freshness Classification | Kazi Nabiul Alam, Pooneh Bagheri Zadeh, Sheikh-Akbari Akbar | Kazi Nabiul Alam School of Built Environment；Pooneh Bagheri Zadeh Leeds Beckett University | 轻量光谱分组卷积网络，高效分类鱼类新鲜度等级。 | [#1093](https://github.com/thinson/RS-PaperClaw/issues/1093) |
| [20260812] Remote Sensing and Machine Learning-Based Analysis of Land Use and Vegetation Change in Dhaka District, Bangladesh | Muhammad Masud Tarek, Md. Alamgir Hossain, Md. Samiul Islam, Muntasir Hasan Kanchan | Department of Computer Science and Engineering, State University of Bangladesh, Dhaka, Bangladesh；Department of Computer Science, American International University - Bangladesh, Dhaka, Bangladesh；Skill Morph Research Lab., Skill Morph, Dhaka, Bangladesh | 遥感与机器学习分析达卡地区土地利用与植被变化。 | [#1094](https://github.com/thinson/RS-PaperClaw/issues/1094) |
| [20260812] A Remote Approach to Cashew Orchard Detection: Leveraging Active Learning with Satellite Imagery in Guinea-Bissau | Miguel, Sofia, Maria, Patrícia, Luke, João | Department of Computer Science, Faculty of Sciences, University of Porto, Rua do Campo Alegre, 4169-007 Porto；Forest Research Centre, School of Agriculture, University of Lisbon, Tapada da Ajuda, 1349-017 Lisbon；CIBIO and BIOPOLIS, InBIO Associated Laboratory, Vairão Campus, University of Porto, Rua do Crasto, 4485-661 Vairão；CMUP and Department of Computer Science, Faculty of Sciences, University of Porto, Rua do Campo Alegre, 4169-007 Porto | 主动学习结合哨兵二号影像，远程检测几内亚比绍腰果果园。 | [#1095](https://github.com/thinson/RS-PaperClaw/issues/1095) |
| [20260812] Warping Earth Observations for better ice labeling in the Marginal Marginal Ice Zone | Kelly Tom, Martin S. J. Rogers | British Antarctic Survey | 图像配准扭曲地球观测，改善南极边缘冰区冰标注。 | [#1096](https://github.com/thinson/RS-PaperClaw/issues/1096) |
| [20260812] Dual Modality Prompted Diffusion Priors for Zero Shot Hyperspectral Pansharpening | Xie Pengwei, Zhu Fei, Li Jiajun, Liu Xiangyuan, Liu Xiangyuan, Shen Kangqing, Vivone Gemine | School of Artificial Intelligence, Beijing Normal University, Beijing, China (；School of GeoAI and Hinton STAI Institute, and the Key Laboratory of Geographic Information Science (Ministry of Education), East China Normal University, Shanghai, China (；Peking University, Beijing, China (；the National Center for Applied Mathematics Shenzhen (NCAMS), Southern University of Science and Technology, Shenzhen, China (；Department of Automation, Tsinghua University, Beijing, China (；the National Research Council of Italy, Institute of Integrated Methodologies for Earth Observation (CNR-IMIOT), Tito, Italy ( | 双模态提示扩散先验，实现零样本高光谱全色锐化。 | [#1097](https://github.com/thinson/RS-PaperClaw/issues/1097) |
| [20260812] Advancing MLLM-based UAV Image Understanding and Reasoning: A Benchmark and a Training-Free Multi-Agent System | Zhang Haoyu, Zhang Shuoxun, Ye Peng, Zhang Lin, Yuan Jiakang, Yi Shenghong, Wang Yuening, Chen Tao | Shanghai Innovation Institute, Shanghai, China (；The Chinese University of Hong Kong, Hong Kong (；College of Future Information Technology, Fudan University, Shanghai, China ( | 提出基准与免训练多智能体系统，提升无人机图像理解。 | [#1098](https://github.com/thinson/RS-PaperClaw/issues/1098) |
| [20260812] EGM-Det: Entropy-Guided Multimodal Adaptive Fusion for UAV RGB-IR Object Detection | Fan Cunzheng, Yan Dawei, Wang Guanlin, Yang Xingshuo, Jia Yupeng, Yang Jing, Zhang Haokui | School of Cybersecurity, Northwestern Polytechnical University, Xi’an 710072, China；School of Automation and Software Engineering, Shanxi University, Taiyuan 030006, China；Joint utilization of RGB and infrared (IR) information for object detection represents an important research | 熵引导多模态自适应融合，增强无人机RGB-IR目标检测。 | [#1099](https://github.com/thinson/RS-PaperClaw/issues/1099) |
| [20260812] Zero-OVCD: Bridging Training-Free Foundation Models and Pseudo-Label Learning for Open-Vocabulary Change Detection | Peng Daifeng, Peng Yuanke, Guan Haiyan | School of Remote Sensing and Geomatics Engineering, Nanjing University of Information Science and Technology, Nanjing, China ( | 免训练基础模型与伪标签结合，实现开放词汇变化检测。 | [#1100](https://github.com/thinson/RS-PaperClaw/issues/1100) |
| [20260812] Transferable Above-Ground Biomass (AGB) Estimation Model from Multi-Sensor Data with Sparse Field Calibration | Pann Thinzar Seint, Atwood Bryan, Chhatkuli Subas | DAI Labs, K.K. | 多传感器数据与稀疏校准，构建可迁移的地上生物量模型。 | [#1101](https://github.com/thinson/RS-PaperClaw/issues/1101) |

## 🔎 观察

- 高光谱成像在食品质量评估中应用增多，结合少样本学习提升实用性。
- 基础模型与扩散模型在遥感任务中渗透，推动零样本与开放词汇能力发展。

---

Powered by OpenClaw🦞

---
