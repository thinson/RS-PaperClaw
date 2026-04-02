# Daily Reports

最近三天日报（最新在前）：

# [20260401](./202604/20260401.md)
## 📌 今日概况

今日共检索候选论文 8 篇；关键词+LLM 智能匹配遥感交叉论文 6 篇；最终纳入日报 6 篇。

今日遥感AI研究呈现多模态融合与实用化趋势：高光谱非线性解混引入生成对抗网络，农业遥感发布高精度产量预测基准，SAR对抗攻击探索物理层安全，无人机全景视觉-惯性SLAM构建跨时序数据集，持续学习缓解视觉语言模型灾难性遗忘，SAM改进实现高分辨率道路交互式分割。

## ✨ 今日亮点

- YieldSAT发布多模态作物产量预测基准，推动精准农业数据标准化
- PC-SAM约束SAM补丁实现高分辨率道路交互式精细分割
- 首个遥感视觉语言持续学习基准，系统评估灾难性遗忘问题

## 🗂 今日文章列表

| 标题 | 作者 | 一句话概括 | Issue |
|---|---|---|---|
| [20260401] Looking into a Pixel by Nonlinear Unmixing -- A Generative Approach | Tang Maofeng, Qi Hairong | 提出基于生成对抗网络与循环一致性的高光谱非线性解混方法，突破线性模型局限。 | [#240](https://github.com/thinson/RS-PaperClaw/issues/240) |
| [20260401] YieldSAT: A Multimodal Benchmark Dataset for High-Resolution Crop Yield Prediction | Miranda Miro, Pathak Deepak, Helber Patrick, Bischke Benjamin, Najjar Hiba et al. | 构建YieldSAT多模态基准数据集，融合卫星影像与农艺数据支持高分辨率作物产量预测。 | [#241](https://github.com/thinson/RS-PaperClaw/issues/241) |
| [20260401] Adversarial Attenuation Patch Attack for SAR Object Detection | Zhang Yiming, Qin Weibo, Wang Feng | 设计对抗衰减补丁攻击方法，针对SAR目标检测实现电子干扰层面的物理隐蔽攻击。 | [#242](https://github.com/thinson/RS-PaperClaw/issues/242) |
| [20260401] PanoAir: A Panoramic Visual-Inertial SLAM with Cross-Time Real-World UAV Dataset | Wu Yiyang, Zhang Xiaohu, Du Yanjin, Zhang Tongsu, Li Chujun et al. | 发布PanoAir全景视觉-惯性SLAM数据集，支持无人机跨时序真实场景位姿估计。 | [#243](https://github.com/thinson/RS-PaperClaw/issues/243) |
| [20260401] Continual Vision-Language Learning for Remote Sensing: Benchmarking and Analysis | Weng Xingxing, Ni Ruifeng, Pang Chao, Hao XiangYu, Wang Yishan et al. | 建立遥感视觉语言持续学习基准，量化分析模型在增量任务中的灾难性遗忘现象。 | [#244](https://github.com/thinson/RS-PaperClaw/issues/244) |
| [20260401] PC-SAM: Patch-Constrained Fine-Grained Interactive Road Segmentation in High-Resolution Remote Sensing Images | Lv Chengcheng, Li Rushi, Wu Mincheng, Shi Xiufang, Wen Zhenyu et al. | 提出PC-SAM补丁约束机制，优化SAM在高分辨率遥感图像中的道路交互式分割精度。 | [#245](https://github.com/thinson/RS-PaperClaw/issues/245) |

## 🔎 观察

- SAM架构正快速渗透遥感细分任务，但高分辨率场景下的计算效率与交互精度仍需平衡
- 物理层对抗攻击向SAR领域延伸，遥感模型安全性研究从数字空间拓展至电磁信号层面

---

Powered by OpenClaw🦞

---

# [20260331](./202603/20260331.md)
## 📌 今日概况

今日共检索候选论文 15 篇；关键词+LLM 智能匹配遥感交叉论文 6 篇；最终纳入日报 6 篇。

今日遥感AI研究呈现多模态融合与基础模型应用深化趋势。视觉-语言模型持续向地球观测领域渗透，涵盖文本-图像数据集构建、跨模态检索及开放词汇分割等方向。同时，层次化分类、高光谱解混与单目高度估计等经典任务在方法论上均有创新，体现遥感专用模型与通用AI技术的双向融合。

## ✨ 今日亮点

- BigEarthNet.txt发布大规模多传感器图文数据集，填补遥感视觉-语言基准空白
- ConInfer提出无需训练的上下文感知推理框架，推动开放词汇遥感分割实用化
- EarthEmbeddingExplorer上线全球卫星影像跨模态检索平台，加速基础模型落地

## 🗂 今日文章列表

| 标题 | 作者 | 一句话概括 | Issue |
|---|---|---|---|
| [20260331] MAPLE: Multi-Path Adaptive Propagation with Level-Aware Embeddings for Hierarchical Multi-Label Image Classification | Koloski Boshko, Stoimchev Marjan, Levatić Jurica, Kocev Dragi, Džeroski Sašo | MAPLE提出多路径自适应传播与层级感知嵌入，用于遥感图像层次化多标签分类，结合图卷积网络处理标签层级关系。 | [#233](https://github.com/thinson/RS-PaperClaw/issues/233) |
| [20260331] BigEarthNet.txt: A Large-Scale Multi-Sensor Image-Text Dataset and Benchmark for Earth Observation | Herzog Johann-Ludwig, Mathis Jürgen Adler, Hackel Leonard, Shu Yan, Zavras Angelos et al. | BigEarthNet.txt构建Sentinel-1/2多传感器图文数据集，为地球观测视觉-语言模型提供标准化训练与评测基准。 | [#234](https://github.com/thinson/RS-PaperClaw/issues/234) |
| [20260331] EarthEmbeddingExplorer: A Web Application for Cross-Modal Retrieval of Global Satellite Images | Zheng Yijie, Wu Weijie, Wu Bingyue, Zhao Long, Li Guoqing et al. | EarthEmbeddingExplorer开发Web应用，实现基于基础模型的全球卫星影像跨模态检索与交互式探索。 | [#235](https://github.com/thinson/RS-PaperClaw/issues/235) |
| [20260331] Polyhedral Unmixing: Bridging Semantic Segmentation with Hyperspectral Unmixing via Polyhedral-Cone Partitioning | Bottenmuller Antoine, Decencière Etienne, Dokládal Petr | Polyhedral Unmixing通过多面体锥分割桥接语义分割与高光谱解混，统一端元提取与亚像元丰度估计任务。 | [#236](https://github.com/thinson/RS-PaperClaw/issues/236) |
| [20260331] ConInfer: Context-Aware Inference for Training-Free Open-Vocabulary Remote Sensing Segmentation | Chen Wenyang, Hu Zhanxuan, Zhang Yaping, Ning Hailong, Tai Yonghang | ConInfer设计上下文感知推理机制，无需微调即可实现开放词汇遥感语义分割，提升类别泛化能力。 | [#237](https://github.com/thinson/RS-PaperClaw/issues/237) |
| [20260331] Monocular Building Height Estimation from PhiSat-2 Imagery: Dataset and Method | Song Yanjiao, Cai Bowen, Balz Timo, Shao Zhenfeng, Neema Simon Sumari et al. | 基于PhiSat-2卫星影像构建单目建筑高度估计数据集，提出面向城市形态分析的端到端深度估计方法。 | [#238](https://github.com/thinson/RS-PaperClaw/issues/238) |

## 🔎 观察

- 视觉-语言模型正成为遥感领域核心基础设施，数据集、算法与平台三层同步推进，生态构建加速
- 训练-free或few-shot范式在遥感任务中占比上升，反映领域对降低标注成本与提升泛化性的迫切需求

---

Powered by OpenClaw🦞

---

# [20260330](./202603/20260330.md)
## 📌 今日概况

今日共检索候选论文 10 篇；关键词+LLM 智能匹配遥感交叉论文 5 篇；最终纳入日报 5 篇。

今日遥感AI研究呈现多维度交叉趋势：生成模型向显著性检测渗透，ORSIFlow将矫正流与潜扩散结合提升光学遥感目标检测精度；硬件层面，自旋三旋翼无人机通过非线性动态逆控制扩展视场；数据基建方面，PROSAIL驱动的合成高光谱植被数据集填补基准空白；多模态检索与无线通信信道推断则体现遥感向跨域应用的延伸。

## ✨ 今日亮点

- ORSIFlow首次将矫正流引入遥感显著性检测，以显著性引导生成机制优化边界感知
- 自旋三旋翼无人机采用模型预测控制与非线性动态逆，实现360°视场自主飞行
- SVH-BD基于PROSAIL辐射传输模型构建合成高光谱植被基准，支持遥感图像仿真

## 🗂 今日文章列表

| 标题 | 作者 | 一句话概括 | Issue |
|---|---|---|---|
| [20260330] ORSIFlow: Saliency-Guided Rectified Flow for Optical Remote Sensing Salient Object Detection | Chen Haojing, Li Yutong, Liu Zhihang, Tan Tao, Bian Haoyu et al. | ORSIFlow提出显著性引导矫正流，结合潜扩散模型与边界感知损失，优化光学遥感显著目标检测的生成质量与效率。 | [#225](https://github.com/thinson/RS-PaperClaw/issues/225) |
| [20260330] A Self-Rotating Tri-Rotor UAV for Field of View Expansion and Autonomous Flight | Zhou Xiaobin, Zheng Zihao, Jin Aoxu, Qiang Lei, Zhu Bo | 自旋三旋翼无人机通过模型预测控制与非线性动态逆实现自主飞行，以机械旋转扩展视场突破固定相机视角限制。 | [#226](https://github.com/thinson/RS-PaperClaw/issues/226) |
| [20260330] SVH-BD : Synthetic Vegetation Hyperspectral Benchmark Dataset for Emulation of Remote Sensing Images | Chedly Ben Azizi, Guilloteau Claire, Roussel Gilles, Puigt Matthieu | SVH-BD基于PROSAIL辐射传输模型生成合成高光谱植被数据，为遥感图像仿真与植被性状反演提供标准化基准。 | [#227](https://github.com/thinson/RS-PaperClaw/issues/227) |
| [20260330] Robust Remote Sensing Image-Text Retrieval with Noisy Correspondence | Song Qiya, Xie Yiqiang, Sun Yuan, Dian Renwei, Kang Xudong | 针对遥感图文检索中的噪声对应问题，提出自步课程学习策略，逐步过滤噪声样本以提升跨模态检索鲁棒性。 | [#228](https://github.com/thinson/RS-PaperClaw/issues/228) |
| [20260330] Deep Learning Based Site-Specific Channel Inference Using Satellite Images | Song Junzhe, He Ruisi, Yang Mi, Zhang Zhengyu, Gao Shuaiqi et al. | 利用卫星图像与深度学习进行站点级无线信道推断，构建抽头延迟线模型辅助通信网络规划与频谱管理。 | [#229](https://github.com/thinson/RS-PaperClaw/issues/229) |

## 🔎 观察

- 生成式AI正从图像合成向判别任务回流，矫正流等高效生成模型开始服务于检测任务的特征增强与边界精细化
- 遥感硬件创新与算法研究呈现并行态势，无人机平台动力学控制与上层视觉任务形成系统级闭环，但跨层协同优化尚待深入

---

Powered by OpenClaw🦞

---
