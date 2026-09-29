# Daily Reports

最近三天日报（最新在前）：

# [20260928](./202609/20260928.md)
## 📌 今日概况

今日共检索候选论文 24 篇；关键词+LLM 智能匹配遥感交叉论文 18 篇；最终纳入日报 17 篇。

今日论文覆盖红外小目标检测、跨视角地理定位、多视角卫星三维重建、无人机跟踪与问答、SAR在轨分类、高光谱超分及遥感视频理解等方向。知识蒸馏、高斯泼溅、脉冲神经网络与多智能体记忆等被引入遥感任务，物理感知与任务导向通信成为新关注点。基准与数据集建设持续活跃，跨域迁移与泛化问题受到重视。

## ✨ 今日亮点

- 知识蒸馏与注意力先验结合，提升红外小目标检测的粗到细性能
- 高斯泼溅与可靠性融合被用于多视角卫星影像三维重建
- 多个新基准与数据集发布，覆盖地理推理、林下VIO与遥感视频问答

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260928] Denoising-Enhanced Coarse-to-Fine Infrared Small Target Detection with Attention Prior-Guided Knowledge Distillation | Fang Houzhang, Huang Ruixuan, Chen Qiuhuan, Wang Xiaolin, Chang Yi, Yan Luxin | Xidian University, Xi’an, China；Huazhong University of Science and Technology, Wuhan, China | 提出去噪增强的粗到细红外小目标检测框架，利用注意力先验引导知识蒸馏提升性能。 | [#755](https://github.com/thinson/RS-PaperClaw/issues/755) |
| [20260928] GeoRefer-Bench: A Benchmark from Referring Pixels to Verifiable Geospatial Reasoning | Cao Shuaishuai, Huang Min, Tang Meng, Liu Xuan, Wang Youjin, Lin Hui | Central South University；Jiangxi Normal University (；Hohai University；Renmin University of China (undergraduate student)；The Chinese University of Hong Kong (Senior Member, IEEE) | 构建从指称像素到可验证地理空间推理的基准，涵盖空间关系、指称分割与场景图。 | [#1384](https://github.com/thinson/RS-PaperClaw/issues/1384) |
| [20260928] GeoBridge++: Fact-Guided Geo-Semantic Bridging for Unified Cross-View Geo-Localization | Song Zixuan, Zhang Jing, Wang Di, Luo Zhiming, Liu Wenbin, Guo Haonan, Wang En, Du Bo, Zhang Liangpei | College of Computer Science and Technology and Key Laboratory of Symbolic Computation and Knowledge Engineering of Ministry of Education, Jilin University, Changchun, China；Zhongguancun Academy, Beijing, China (；School of Computer Science, Wuhan University, Wuhan, China；College of Computer Science and Technology and Key Laboratory of Symbolic Computation and Knowledge Engineering of Ministry of Education, Jilin University, Changchun, China. ( | 提出事实引导的地理语义桥接方法，统一跨视角地理定位与双向匹配。 | [#1385](https://github.com/thinson/RS-PaperClaw/issues/1385) |
| [20260928] Robust 3D Reconstruction from Multi-View Optical Satellite Imagery via Reliability-Aware Height-Evidence Fusion in Gaussian Splatting | Yang Jie, Pi Yingdong, Luo Qiyan, Wang Xiaoyu, Wen Lekang, Wang Mi | State Key Laboratory of Information Engineering in Surveying, Mapping and Remote Sensing, Wuhan University；Hubei Luojia Laboratory；School of Computer Science, Wuhan University | 在多视角光学卫星影像中，通过可靠性感知高度证据融合改进高斯泼溅三维重建。 | [#1386](https://github.com/thinson/RS-PaperClaw/issues/1386) |
| [20260928] SBMVTrack: Spike-Budgeted Multi-View Learning for Power-Efficient UAV Tracking | Zhong Pengzhi, Mo Jiwei, Li Haolun, Zheng Ge, Wang Jingqi, Bo Xinyi, Li Shuiwang | College of Computer Science and Engineering, Guilin University of Technology, Guilin 541004, China；School of Information Engineering, Wuhan University of Technology, Wuhan 430070, China | 面向无人机跟踪，提出脉冲预算多视角学习，兼顾能效与跟踪精度。 | [#1387](https://github.com/thinson/RS-PaperClaw/issues/1387) |
| [20260928] Stacked Intelligent Metasurface-Diffractive Deep Neural Networks for Onboard Terrain Classification from SAR Level-0 Raw Data | Liu Mengbing, Li Xin, An Jiancheng, Yuen Chau | School of Electrical and Electronics Engineering, Nanyang Technological University, Singapore (e-mails:; ) | 利用堆叠智能超表面与衍射深度神经网络，从SAR原始数据在轨进行地形分类。 | [#1388](https://github.com/thinson/RS-PaperClaw/issues/1388) |
| [20260928] Preference-Guided Adaptation for Open-Vocabulary Semantic Segmentation via Prompt Disagreement | Jang Hyun-Kurl, Kim Jihun, Yoon Kuk-Jin | Visual Intelligence Lab | 通过提示分歧实现偏好引导自适应，提升开放词汇语义分割的泛化能力。 | [#1389](https://github.com/thinson/RS-PaperClaw/issues/1389) |
| [20260928] Joint DNN Partitioning and Resource Allocation for Satellite-Terrestrial Collaborative Inference Systems | Liang Wenyu, Fei Zesong, Liu Peng, Wang Xinyi, Zeng Ming | School of Information and Electronics, Beijing Institute of Technology, Beijing, China ( | 面向卫星地面协同推理，联合优化DNN划分与资源分配以降低时延。 | [#1390](https://github.com/thinson/RS-PaperClaw/issues/1390) |
| [20260928] Temporal Modelling for Burn Scars on Sentinel-3 | Barco Luca, Arnaudo Edoardo, Bragagnolo Andrea, Rossi Claudio, Garza Paolo | Up funded by the Italian Space Agency and the Ministry of University and；Research - Contract No. 2024-5-E.0 - CUP No. I53 D24000060005 | 基于Sentinel-3 OLCI数据，采用时序建模进行火烧迹地语义分割与制图。 | [#1391](https://github.com/thinson/RS-PaperClaw/issues/1391) |
| [20260928] When local gains fail to transfer: Frozen Earth-observation embeddings across wildfires | Stark Philipp, Sopasakis Alexandros, Hall Ola | Department of Human Geography Centre for Mathematical Sciences；Lund University Lund University；Department of Human Geography；Lund University | 研究发现冻结的地球观测嵌入在野火任务间局部增益难以迁移。 | [#1392](https://github.com/thinson/RS-PaperClaw/issues/1392) |
| [20260928] Correcting Spectra Outside the Backbone: A Model-Agnostic Rectifier for Hyperspectral Image Super-Resolution | He Ji-Xuan, Zhuang Guohang, Junge Bo, Ling Chen, Li Tingyi, Qiao Yanan, Cai Miaomiao, Fang Jungfeng | Xi'an Jiaotong University；Hefei University of Technology；National University of Singapore | 提出模型无关的光谱校正器，在骨干网络外修正高光谱图像超分辨的光谱失真。 | [#1393](https://github.com/thinson/RS-PaperClaw/issues/1393) |
| [20260928] Task-Oriented Communications for Edge-Assisted Multi-View Localization | Fang Zhengru, Lou Huanhuan, Hu Senkang, Tao Yihang, Li Zongdian, Deng Yiqin, Wang Jingjing, Fang Yuguang | Department of Electronic and Computer Engineering, The Hong Kong University of Science and Technology, Hong Kong (；the Hong Kong JC STEM Lab of Smart City and the Department of Computer Science, City University of Hong Kong, Hong Kong (；Zhejiang University, Hangzhou, China (；School of Data Science, Lingnan University, Tuen Mun, Hong Kong, China (；School of Cyber Science and Technology, Beihang University, Beijing, China ( | 面向边缘辅助多视角定位，以任务导向通信和变分信息瓶颈优化信息传输。 | [#1394](https://github.com/thinson/RS-PaperClaw/issues/1394) |
| [20260928] Spectral Super-Resolution using Spatial-Spectral Residual Operator Networks | Chin Seokhyun | California Institute of Technology | 利用空间-光谱残差算子网络，实现多光谱卫星影像的零样本光谱超分辨。 | [#1395](https://github.com/thinson/RS-PaperClaw/issues/1395) |
| [20260928] Memory in the Sky: Low-Altitude Question Answering with Multi-Agent Memory Aggregation | Li Chengyang, Wan Yujie, Wang Shuai, Ye Kejiang, Yuan Weijie, Zhou Boyu, Wu Yik-Chung, Xu Chengzhong, Arslan Huseyin | University of Hong Kong, Hong Kong SAR, China；the Shenzhen Institutes of Advanced Technology, Chinese Academy of Sciences, Shenzhen, China；the Southern University of Science and Technology, Shenzhen, China；University of Macau, Macau SAR, China；the Istanbul Medipol University, Istanbul, Turkey | 面向低空问答，提出多智能体记忆聚合方法并引入生成对抗考试与记忆质量度量。 | [#1396](https://github.com/thinson/RS-PaperClaw/issues/1396) |
| [20260928] ForVis: An In-Field Dataset and Benchmark for VIO Using Under-Canopy UAV Flights in Forests | Kiani Arman, Ataei Masoud, Gyaase Elvis, Eiyike Jeffrey, Weiskittel Aaron, Chakraborty Prabuddha, Dhiman Vikas | Department of Electrical and Computer Engineering, University of Maine, Orono, ME 04469, USA | 发布林下无人机飞行VIO数据集与基准，支持森林环境视觉惯性定位评估。 | [#1397](https://github.com/thinson/RS-PaperClaw/issues/1397) |
| [20260928] ReVA: A Scene-Centric Dataset Beyond Repetition for Remote Sensing Video Question Answering | Yao Zhen, Wang Likai, Yang Yuming, Zheng Zhihao, Lang Bo, Tang Qiuyu, Sheng Jialu, Xu Jingqi, Yang Yuehai, Barker Jumal, Ying Xiaowen, Mooi Choo Chuah | Lehigh University；University of Southern California；Qualcomm AI Research | 构建场景中心的遥感视频问答数据集，超越重复模式以增强时空推理。 | [#1398](https://github.com/thinson/RS-PaperClaw/issues/1398) |
| [20260928] Remote Sensing Sparse-View 3D Gaussian Splatting via Depth Image-Based Rendering | Kang Jiaming, Zou Zhengxia, Shi Zhenwei | Beihang University | 基于深度图像渲染，实现遥感稀疏视角三维高斯泼溅的新视角合成。 | [#1399](https://github.com/thinson/RS-PaperClaw/issues/1399) |

## ⚠️ 未纳入日报的匹配论文

以下论文通过关键词/LLM 筛选，但在处理过程中失败未纳入日报。点击 arXiv 链接可查看原文。

| 标题 | arXiv | 失败原因 |
|------|-------|----------|
| HyperDAM: Hyperspectral Distractor-Aware Memory with Amodal Expansion for SAM 3 Tracking | [2609.34396](https://arxiv.org/abs/2609.34396) | 质检未通过: 单位为空或无效 |


## 🔎 观察

- 知识蒸馏、高斯泼溅与脉冲网络等通用技术正加速向遥感任务迁移，跨域适配成为关键。
- 基准与数据集建设密集，但冻结嵌入迁移失败等结果提示泛化评估仍需更严格设计。

---

Powered by OpenClaw🦞

---

# [20260927](./202609/20260927.md)
## 📌 今日概况

今日共检索候选论文 10 篇；关键词+LLM 智能匹配遥感交叉论文 5 篇；最终纳入日报 4 篇。

今日论文覆盖遥感目标检测、语义变化解析、在轨模型适配与经济遥感分析。研究趋势显示，端到端Transformer与查询引导范式正逐步替代传统类别名提示和锚框流程；同时，面向星上部署的参数高效微调与带宽约束更新受到关注。夜间灯光影像被进一步用于细粒度地方经济分析，体现遥感从地物识别向社会经济感知延伸。整体上，方法创新与资源受限场景适配并重。

## ✨ 今日亮点

- 查询引导语义变化解析突破类别名提示限制
- 端到端Transformer实现遥感旋转目标检测
- 资源感知参数高效适配面向星上高维数据

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260927] QSCP: Beyond Class-Name Prompts for Query-Guided Semantic Change Parsing | Qian Yuan, Ma Jie | School of Information Science and Technology, Beijing Foreign Studies University, Beijing, China ( | 提出查询引导语义变化解析，超越类别名提示，支持指代变化检测与意图解析。 | [#1379](https://github.com/thinson/RS-PaperClaw/issues/1379) |
| [20260927] OrientedFormer: An End-to-End Transformer-Based Oriented Object Detector in Remote Sensing Images | Ding Zeyu, Zhou Yong, Zhao Jiaqi, Zhu Hancheng, Du Wen-Liang, Yao Rui, Abdulmotaleb El Saddik | School of Electrical Engineering and Computer Science, University of Ottawa, Ottawa, ON K1 N 6 N5, Canada ( | 提出OrientedFormer，基于端到端Transformer与高斯位置编码的遥感旋转目标检测器。 | [#1380](https://github.com/thinson/RS-PaperClaw/issues/1380) |
| [20260927] Resource-Aware Parameter-Efficient Model Adaptation for Onboard High-Dimensional Data | Zhang Qiyang, Li Xinhao, Shi Lei, Lin Zheng, Wen Jinfeng, Zhou Ao, Wang Shangguang | Beijing University of Posts and Telecommunications；Wuhan University；Communication University of China；University of Luxembourg | 面向星上高维数据，研究资源感知的参数高效模型适配与带宽受限更新。 | [#1381](https://github.com/thinson/RS-PaperClaw/issues/1381) |
| [20260927] The Potential of Nighttime Light Imagery for Detailed Local Economic Analysis | Otomo Shoichi | seasonal weather patterns, regional institutional calendars (such as holiday periods), and origindestination population flows | 探讨夜间灯光影像在地方经济细粒度分析中的潜力，涉及旅游经济与空间处理。 | [#1382](https://github.com/thinson/RS-PaperClaw/issues/1382) |

## ⚠️ 未纳入日报的匹配论文

以下论文通过关键词/LLM 筛选，但在处理过程中失败未纳入日报。点击 arXiv 链接可查看原文。

| 标题 | arXiv | 失败原因 |
|------|-------|----------|
| Correlation Between Nighttime Light and Various Statistical Indicators in Japan | [2609.33861](https://arxiv.org/abs/2609.33861) | 质检未通过: 单位为空或无效 |


## 🔎 观察

- 遥感检测与变化解析正从固定类别提示转向查询引导和端到端范式，交互性增强。
- 星上部署需求推动参数高效适配研究，带宽与资源约束成为方法设计关键变量。

---

Powered by OpenClaw🦞

---

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
