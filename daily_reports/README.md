# Daily Reports

最近三天日报（最新在前）：

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

# [20260925](./202609/20260925.md)
## 📌 今日概况

今日共检索候选论文 16 篇；关键词+LLM 智能匹配遥感交叉论文 7 篇；最终纳入日报 7 篇。

今日论文聚焦遥感数据的高效表征、跨模态转换与智能体应用。高光谱视频压缩引入隐式神经表示，波段选择稳定性研究关注语义分割可靠性；扩散模型与流匹配被用于数字表面模型增强和SAR到光学图像翻译，强调多模态条件与单步生成。同时，面向超高分辨率影像的工具路由智能体、长时无人机视觉语言导航基准以及人机回环地理标注系统，反映出遥感AI向自动化、交互式与可扩展数据集构建方向演进。

## ✨ 今日亮点

- 隐式神经表示拓展至高光谱视频压缩，兼顾时空谱冗余。
- 流匹配与对比学习结合，实现单步SAR到光学图像翻译。
- 长时无人机视觉语言导航基准与工具路由智能体并进。

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260925] Implicit Neural Representation for Hyperspectral Video Compression | Scalera Alfredo, Murray Paul, Zabalza Jaime | University of Strathclyde；Department of Electronic | 提出隐式神经表示方法用于高光谱视频压缩，以Bjøntegaard Delta评估压缩效率。 | [#1360](https://github.com/thinson/RS-PaperClaw/issues/1360) |
| [20260925] Band-Selection Stability and Semantic Segmentation Performance: A Study on Hyperspectral City | Li Jiarong, Imad Ali Shah, Ward Enda, Glavin Martin, Jones Edward, Deegan Brian | School of Engineering and Ryan Institute, University of Galway, Ireland | 研究高光谱城市语义分割中波段选择稳定性与分割性能的关系。 | [#1363](https://github.com/thinson/RS-PaperClaw/issues/1363) |
| [20260925] Enhancing Photogrammetric Digital Surface Models with Pretrained Diffusion Models and Multimodal Conditioning | Lorentz Antoine, May Stéphane, Bellet Valentine, Derksen Dawa, Nespoulous Bastien | Centre National d’Études Spatiales (CNES) | 利用预训练扩散模型和多模态条件增强摄影测量数字表面模型。 | [#1364](https://github.com/thinson/RS-PaperClaw/issues/1364) |
| [20260925] WeaveAgent: A Two-Stage Tool-Routing Agent for Ultra-High-Resolution Remote Sensing Imagery | Pang Zhongyu | Department of Electronics, National University of Defense Technology | 提出两阶段工具路由智能体，处理超高分辨率遥感影像的视觉令牌压缩与调用。 | [#1365](https://github.com/thinson/RS-PaperClaw/issues/1365) |
| [20260925] ContraFM-S2O: Flow Matching-Based One-step SAR-to-Optical Image Translation Model with Contrastive Learning | Yu Mingqian, Chiang Wei-kuan, Wang Qiurui, Zhao Peilin | Institute of Automation, Chinese Academy of Sciences, Beijing, China；Department of Computer Science, The University of Manchester, Manchester, UK；Institute of Artificial Intelligence in Sports, Capital University of Physical Education And Sports, Beijing, China；School of Artificial Intelligence, Shanghai Jiao Tong University, Shanghai, China | 结合流匹配与对比学习，构建单步SAR到光学图像翻译模型。 | [#1366](https://github.com/thinson/RS-PaperClaw/issues/1366) |
| [20260925] SatNav: A Scalable Benchmark for Long-Horizon UAV Vision-Language Navigation from Satellite Imagery | Jiang Jiajun, Hua Chunliang, Chen Zichun, Wu Yanxing, Yang Zeyuan, Song Jie, Hu Xiao | The Hong Kong University of Science and Technology (Guangzhou)；Low Altitude Space Economy Research Center；International Digital Economy Academy (IDEA)；The Hong Kong University of Science and Technology | 基于卫星影像构建可扩展长时无人机视觉语言导航基准SatNav。 | [#1367](https://github.com/thinson/RS-PaperClaw/issues/1367) |
| [20260925] Human-in-the-Loop Geospatial Annotation for Rapid Dataset Construction in Field-Deployed UAV Systems | Masters Morgan, Korycki Adam, Bender Nikolaas, T. Luca Altaffer, Josephson Colleen, McGuire Steve | Department of Electrical and Computer Engineering, University of California Santa Cruz；time-consuming and costly [9], forcing research communities to rely on large-scale, internet-hosted；As a consequence, researchers and practitioners working in specialized domains—such as field | 设计人机回环地理标注流程，支持野外部署无人机系统快速构建数据集。 | [#1368](https://github.com/thinson/RS-PaperClaw/issues/1368) |

## 🔎 观察

- 高光谱与SAR等遥感模态的压缩和转换研究，正从重建精度转向下游任务稳定性与效率。
- 智能体与基准数据集建设同步推进，表明遥感AI开始重视长时程交互与真实场景可扩展性。

---

Powered by OpenClaw🦞

---
