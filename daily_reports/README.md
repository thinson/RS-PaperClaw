# Daily Reports

最近三天日报（最新在前）：

# [20260404](./202604/20260404.md)
## 📌 今日概况

今日共检索候选论文 5 篇；关键词+LLM 智能匹配遥感交叉论文 3 篇；最终纳入日报 3 篇。

今日遥感AI研究聚焦三大方向：表征学习、计算效率与成像重建。多任务学习框架优化遥感特征表示，异构计算加速SAR成像，物理驱动方法突破单像素高光谱超分辨瓶颈，体现算法创新与硬件协同的发展趋势。

## ✨ 今日亮点

- 多标注三元组学习框架通过互信息最大化实现任务导向的遥感表征学习
- Apple Silicon架构下核融合FFT流水线将SAR成像耗时从8秒压缩至370毫秒
- 物理约束无训练网络实现RGB引导的单像素高光谱超分辨重建

## 🗂 今日文章列表

| 标题 | 作者 | 一句话概括 | Issue |
|---|---|---|---|
| [20260404] Task-Guided Multi-Annotation Triplet Learning for Remote Sensing Representations | Zhou Meilun, Zare Alina | 提出任务引导的多标注三元组学习框架，利用互信息最大化优化遥感图像表征的多任务适应性。 | [#272](https://github.com/thinson/RS-PaperClaw/issues/272) |
| [20260404] From 8 Seconds to 370ms: Kernel-Fused SAR Imaging on Apple Silicon via Single-Dispatch FFT Pipelines | Mohamed Amine Bergach | 针对Apple Silicon设计单调度FFT流水线与核融合策略，实现SAR成像两个数量级的加速。 | [#273](https://github.com/thinson/RS-PaperClaw/issues/273) |
| [20260404] Physics-Informed Untrained Learning for RGB-Guided Superresolution Single-Pixel Hyperspectral Imaging | Zhang Hao, Xu Bilige, Wei Lichen, Ma Xu, Ren Wenyi | 结合物理先验与无训练神经网络，以RGB图像为引导完成单像素高光谱成像的超分辨重建。 | [#274](https://github.com/thinson/RS-PaperClaw/issues/274) |

## 🔎 观察

- 边缘端高效计算成为SAR处理新焦点，专用硬件优化正从服务器向消费级芯片迁移
- 无训练神经网络与物理模型融合为计算成像开辟新路径，降低对大规模标注数据的依赖

---

Powered by OpenClaw🦞

---

# [20260403](./202604/20260403.md)
## 📌 今日概况

今日共检索候选论文 11 篇；关键词+LLM 智能匹配遥感交叉论文 9 篇；最终纳入日报 9 篇。

今日遥感AI研究呈现多元化趋势，涵盖类增量学习、无人机导航与检测、图像复原及行星遥感等方向。其中无人机相关研究占比突出，涉及目标检测、热红外定位、自主穿越及数据增强等场景；同时，基础模型与持续学习范式在遥感领域的应用探索持续深入。

## ✨ 今日亮点

- 类增量语义分割新思路：ProtoFlow通过低曲率原型流缓解遗忘问题
- 无人机检测技术双突破：特征融合网络与扩散模型数据增强并行推进
- 行星遥感基础模型：MOMO首次针对火星轨道数据构建专用大模型

## 🗂 今日文章列表

| 标题 | 作者 | 一句话概括 | Issue |
|---|---|---|---|
| [20260403] ProtoFlow: Mitigating Forgetting in Class-Incremental Remote Sensing Segmentation via Low-Curvature Prototype Flow | Wu Jiekai, Fu Rong, Li Chuangqi, Zhang Zijian, Wu Guangxin et al. | ProtoFlow提出低曲率原型流方法，缓解遥感图像类增量分割中的灾难性遗忘问题。 | [#261](https://github.com/thinson/RS-PaperClaw/issues/261) |
| [20260403] SFFNet: Synergistic Feature Fusion Network With Dual-Domain Edge Enhancement for UAV Image Object Detection | Zhang Wenfeng, Ni Jun, Meng Yue, Pei Xiaodong, Hu Wei et al. | SFFNet构建双域边缘增强的协同特征融合网络，提升无人机图像目标检测精度。 | [#262](https://github.com/thinson/RS-PaperClaw/issues/262) |
| [20260403] SCC-Loc: A Unified Semantic Cascade Consensus Framework for UAV Thermal Geo-Localization | Zhang Xiaoran, Liu Yu, Liang Jinyu, Li Kangqiushi, Huang Zhiwei et al. | SCC-Loc设计语义级联共识框架，实现无人机热红外图像的跨模态地理定位。 | [#263](https://github.com/thinson/RS-PaperClaw/issues/263) |
| [20260403] A Data-Centric Vision Transformer Baseline for SAR Sea Ice Classification | Mike-Ewewie David, Lim Panhapiseth, Kumar Priyanka | 该研究以数据为中心构建Vision Transformer基线，用于SAR海冰分类任务。 | [#264](https://github.com/thinson/RS-PaperClaw/issues/264) |
| [20260403] Visual Prototype Conditioned Focal Region Generation for UAV-Based Object Detection | Li Wenhao, Wu Zimeng, Wu Yu, Fu Zehua, Chen Jiaxin | 基于视觉原型条件扩散模型，生成无人机检测的聚焦区域数据增强样本。 | [#265](https://github.com/thinson/RS-PaperClaw/issues/265) |
| [20260403] Ground Reflection-Aided TomoSAR Imaging with 5G NR Signals | Yang Qiuyuan, Pan Cunhua, Ren Hong, Wang Jiangzhou | 利用5G NR信号与地面反射辅助，实现多径抑制下的TomoSAR三维成像。 | [#266](https://github.com/thinson/RS-PaperClaw/issues/266) |
| [20260403] Vision-Based End-to-End Learning for UAV Traversal of Irregular Gaps via Differentiable Simulation | Zhang Linzuo, Hu Yu, Yu Feng, Deng Yang, Yu Wenxian et al. | 结合可微分仿真与端到端学习，使无人机具备基于视觉的不规则间隙穿越能力。 | [#267](https://github.com/thinson/RS-PaperClaw/issues/267) |
| [20260403] Task-Guided Prompting for Unified Remote Sensing Image Restoration | Huang Wenli, Wu Yang, Xin Xiaomeng, Liu Zhihong, Wang Jinjun et al. | 任务引导提示学习框架，统一处理遥感图像去噪、去模糊等多类型复原任务。 | [#268](https://github.com/thinson/RS-PaperClaw/issues/268) |
| [20260403] MOMO: Mars Orbital Model Foundation Model for Mars Orbital Applications | Purohit Mirali, Gajera Bimal, Mehta Irish, Tokas Bhanu, Adler Jacob et al. | MOMO融合多源火星轨道数据，构建面向行星遥感应用的专用基础模型。 | [#269](https://github.com/thinson/RS-PaperClaw/issues/269) |

## 🔎 观察

- 无人机遥感成为今日研究核心载体，检测、导航、定位等任务需求驱动算法创新密集涌现。
- 持续学习与基础模型两大范式向垂直领域渗透，反映遥感AI从通用方法向场景专用化演进。

---

Powered by OpenClaw🦞

---

# [20260402](./202604/20260402.md)
## 📌 今日概况

今日共检索候选论文 18 篇；关键词+LLM 智能匹配遥感交叉论文 13 篇；最终纳入日报 13 篇。

今日遥感AI研究呈现三大趋势：一是视觉-语言-动作模型（VLA）向无人机具身智能延伸，二是开放词汇学习持续渗透变化检测与分割任务，三是跨视角地理定位成为热点，UAV-卫星/无人机-地面视角对齐技术密集涌现。此外，KAN网络轻量化、扩散模型RFI抑制等方向亦有新进展。

## ✨ 今日亮点

- UAV-Track VLA首次将VLA模型引入无人机空中跟踪，实现语言指令驱动的具身飞行控制
- CoRegOVCD提出免训练一致性正则化策略，突破开放词汇变化检测的数据瓶颈
- LinkS²Bench构建首个UAV-卫星动态跨视角基准，系统评估VLM空间推理能力边界

## 🗂 今日文章列表

| 标题 | 作者 | 一句话概括 | Issue |
|---|---|---|---|
| [20260402] UAV-Track VLA: Embodied Aerial Tracking via Vision-Language-Action Models | Zhang Qiyao, Zheng Shuhua, Sun Jianli, Li Chengxiang, Wu Xianke et al. | UAV-Track VLA：基于视觉-语言-动作模型的无人机具身空中跟踪框架。 | [#247](https://github.com/thinson/RS-PaperClaw/issues/247) |
| [20260402] CoRegOVCD: Consistency-Regularized Open-Vocabulary Change Detection | Tang Weidong, Sun Hanbin, Li Zihan, Wang Yikai, Zhang Feifan | CoRegOVCD：一致性正则化驱动的免训练开放词汇变化检测方法。 | [#248](https://github.com/thinson/RS-PaperClaw/issues/248) |
| [20260402] Are VLMs Lost Between Sky and Space? LinkS$^2$Bench for UAV-Satellite Dynamic Cross-View Spatial Intelligence | Liu Dian, Feng Jie, Li Di, Zheng Yuhui, Li Guanbin et al. | LinkS²Bench：面向无人机-卫星跨视角空间智能的VLM评测基准。 | [#249](https://github.com/thinson/RS-PaperClaw/issues/249) |
| [20260402] Decouple and Rectify: Semantics-Preserving Structural Enhancement for Open-Vocabulary Remote Sensing Segmentation | Feng Jie, Li Fengze, Zhang Junpeng, Chen Siyu, Liang Yuping et al. | 解耦-校正框架：面向开放词汇遥感分割的语义保持结构增强策略。 | [#250](https://github.com/thinson/RS-PaperClaw/issues/250) |
| [20260402] Test-Time Adaptation for Height Completion via Self-Supervised ViT Features and Monocular Foundation Models | Rafaeli Osher, Svoray Tal, Nahlieli Ariel | 基于自监督ViT特征与单目基础模型的高程补全测试时自适应方法。 | [#251](https://github.com/thinson/RS-PaperClaw/issues/251) |
| [20260402] Light-ResKAN: A Parameter-Sharing Lightweight KAN with Gram Polynomials for Efficient SAR Image Recognition | Yi Pan, Li Weijie, Chen Xiaodong, Zhang Jiehua, Liu Li et al. | Light-ResKAN：Gram多项式参数共享的轻量KAN网络用于SAR图像识别。 | [#252](https://github.com/thinson/RS-PaperClaw/issues/252) |
| [20260402] ProVG: Progressive Visual Grounding via Language Decoupling for Remote Sensing Imagery | Li Ke, Wang Ting, Wang Di, Zhu Yongshan, Zhang Yiming et al. | ProVG：语言解耦驱动的渐进式视觉定位方法用于遥感影像。 | [#253](https://github.com/thinson/RS-PaperClaw/issues/253) |
| [20260402] GeoAI Agency Primitives | Zaytar Akram, Sawahn Rohan, Robinson Caleb, Gilles Q. Hacheme, Girmaw A. Tadesse et al. | GeoAI智能体原语：面向地理空间基础模型的人机协同能力抽象框架。 | [#254](https://github.com/thinson/RS-PaperClaw/issues/254) |
| [20260402] Cosine-Normalized Attention for Hyperspectral Image Classification | Ahmad Muhammad, Mazzara Manuel | 余弦归一化注意力机制用于高光谱图像分类。 | [#255](https://github.com/thinson/RS-PaperClaw/issues/255) |
| [20260402] Unifying UAV Cross-View Geo-Localization via 3D Geometric Perception | Li Haoyuan, Yang Wen, Xu Fang, Tan Hong, Zhang Haijian et al. | 基于3D几何感知的无人机跨视角地理定位统一框架。 | [#256](https://github.com/thinson/RS-PaperClaw/issues/256) |
| [20260402] Satellite-Free Training for Drone-View Geo-Localization | Liu Tao, Zhang Yingzhi, Ren Kan, Zhao Xiaoqi | 无卫星训练的无人机视角地理定位：纯3D场景重建驱动的跨视角检索。 | [#257](https://github.com/thinson/RS-PaperClaw/issues/257) |
| [20260402] Prototype-Based Low Altitude UAV Semantic Segmentation | Zhang Da, Junyu Gao, Zhiyuan Zhao | 原型学习驱动的低空无人机语义分割方法。 | [#258](https://github.com/thinson/RS-PaperClaw/issues/258) |
| [20260402] A Conditional Denoising Diffusion Probabilistic Model for RFI Mitigation in Synthetic Aperture Interferometric Radiometer | Luo Yuankai, Zhou Han, Hao Jinlong, Zhu Dong, Hu Fei | 条件去噪扩散概率模型用于综合孔径干涉辐射计的射频干扰抑制。 | [#259](https://github.com/thinson/RS-PaperClaw/issues/259) |

## 🔎 观察

- 跨视角地理定位（UAV-卫星/地面）今日集中出现4项研究，显示该方向正从2D图像匹配向3D几何感知演进，卫星-free训练范式或降低数据依赖
- 开放词汇学习在遥感领域加速落地，但变化检测、分割等密集预测任务仍面临语义-空间对齐难题，一致性正则化与结构增强成为新解题思路

---

Powered by OpenClaw🦞

---
