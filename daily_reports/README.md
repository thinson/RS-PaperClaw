# Daily Reports

最近三天日报（最新在前）：

# [20260403](./202604/20260403.md)
## 📌 今日概况

今日共检索候选论文 11 篇；关键词+LLM 智能匹配遥感交叉论文 10 篇；最终纳入日报 10 篇。

今日遥感AI研究呈现三大趋势：UAV智能感知与导航持续火热（5篇），涵盖检测、定位、导航与通感一体化；持续学习与基础模型等AI前沿方法向遥感渗透；多模态融合与物理感知增强成为技术突破口。火星遥感与SAR海冰等垂直领域亦获关注。

## ✨ 今日亮点

- 持续学习突破：ProtoFlow以低曲率原型流缓解类增量分割遗忘问题
- UAV导航创新：视觉端到端学习与可微仿真结合实现不规则间隙穿越
- 行星遥感里程碑：MOMO发布首个火星轨道基础模型，支持多传感器融合

## 🗂 今日文章列表

| 标题 | 作者 | 一句话概括 | Issue |
|---|---|---|---|
| [20260403] ProtoFlow: Mitigating Forgetting in Class-Incremental Remote Sensing Segmentation via Low-Curvature Prototype Flow | Wu Jiekai, Fu Rong, Li Chuangqi, Zhang Zijian, Wu Guangxin et al. | ProtoFlow提出低曲率原型流方法，缓解遥感图像类增量语义分割中的灾难性遗忘问题。 | [#261](https://github.com/thinson/RS-PaperClaw/issues/261) |
| [20260403] SFFNet: Synergistic Feature Fusion Network With Dual-Domain Edge Enhancement for UAV Image Object Detection | Zhang Wenfeng, Ni Jun, Meng Yue, Pei Xiaodong, Hu Wei et al. | SFFNet设计双域边缘增强的协同特征融合网络，提升无人机图像目标检测精度。 | [#262](https://github.com/thinson/RS-PaperClaw/issues/262) |
| [20260403] SCC-Loc: A Unified Semantic Cascade Consensus Framework for UAV Thermal Geo-Localization | Zhang Xiaoran, Liu Yu, Liang Jinyu, Li Kangqiushi, Huang Zhiwei et al. | SCC-Loc构建语义级联共识框架，实现无人机热红外图像的跨模态地理定位。 | [#263](https://github.com/thinson/RS-PaperClaw/issues/263) |
| [20260403] A Data-Centric Vision Transformer Baseline for SAR Sea Ice Classification | Mike-Ewewie David, Lim Panhapiseth, Kumar Priyanka | 该研究以数据为中心构建Vision Transformer基线，用于SAR海冰分类任务。 | [#264](https://github.com/thinson/RS-PaperClaw/issues/264) |
| [20260403] Visual Prototype Conditioned Focal Region Generation for UAV-Based Object Detection | Li Wenhao, Wu Zimeng, Wu Yu, Fu Zehua, Chen Jiaxin | 基于视觉原型条件扩散模型，生成无人机检测的聚焦区域数据增强样本。 | [#265](https://github.com/thinson/RS-PaperClaw/issues/265) |
| [20260403] Ground Reflection-Aided TomoSAR Imaging with 5G NR Signals | Yang Qiuyuan, Pan Cunhua, Ren Hong, Wang Jiangzhou | 利用5G NR信号地面反射辅助TomoSAR成像，结合NOMP算法抑制多径干扰。 | [#266](https://github.com/thinson/RS-PaperClaw/issues/266) |
| [20260403] Vision-Based End-to-End Learning for UAV Traversal of Irregular Gaps via Differentiable Simulation | Zhang Linzuo, Hu Yu, Yu Feng, Deng Yang, Yu Wenxian et al. | 端到端视觉学习结合可微物理仿真，使无人机自主穿越不规则间隙。 | [#267](https://github.com/thinson/RS-PaperClaw/issues/267) |
| [20260403] Task-Guided Prompting for Unified Remote Sensing Image Restoration | Huang Wenli, Wu Yang, Xin Xiaomeng, Liu Zhihong, Wang Jinjun et al. | 任务引导提示学习框架统一处理多类型遥感图像退化恢复任务。 | [#268](https://github.com/thinson/RS-PaperClaw/issues/268) |
| [20260403] MOMO: Mars Orbital Model Foundation Model for Mars Orbital Applications | Purohit Mirali, Gajera Bimal, Mehta Irish, Tokas Bhanu, Adler Jacob et al. | MOMO通过模型融合构建首个火星轨道遥感基础模型，支持多源数据应用。 | [#269](https://github.com/thinson/RS-PaperClaw/issues/269) |
| [20260403] MIMO OFDM-Enabled ISAC for Low-Altitude Non-Cooperative UAV Surveillance: A Survey | Bai Shiyu, Li Sijia, Yin Cunyi, Qu Wenqiu, Hsu Li-Ta et al. | 综述MIMO OFDM通感一体化技术在低空非合作无人机监视中的应用进展。 | [#270](https://github.com/thinson/RS-PaperClaw/issues/270) |

## 🔎 观察

- UAV研究占比过半且贯穿感知-认知-决策全链条，反映低空经济对智能遥感的强劲需求牵引。
- 持续学习、基础模型、扩散模型等通用AI方法加速向遥感迁移，领域特异性改造成为创新关键。

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

# [20260401](./202604/20260401.md)
## 📌 今日概况

今日共检索候选论文 8 篇；关键词+LLM 智能匹配遥感交叉论文 6 篇；最终纳入日报 6 篇。

今日遥感AI研究呈现多模态融合与基础模型适配两大主线。高光谱非线性解混引入生成对抗框架，作物产量预测构建多模态基准，SAR对抗攻击探索物理层安全，全景视觉惯性SLAM拓展无人机感知边界，持续学习缓解视觉语言模型灾难性遗忘，SAM变体实现高分辨率道路交互分割。

## ✨ 今日亮点

- YieldSAT构建首个高分辨率作物产量预测多模态基准数据集
- PC-SAM提出补丁约束机制优化SAM在高分辨率遥感道路分割中的交互能力
- PanoAir发布跨时段真实世界无人机全景视觉惯性SLAM数据集

## 🗂 今日文章列表

| 标题 | 作者 | 一句话概括 | Issue |
|---|---|---|---|
| [20260401] Looking into a Pixel by Nonlinear Unmixing -- A Generative Approach | Tang Maofeng, Qi Hairong | Tang等提出基于生成对抗网络与循环一致性的非线性高光谱解混方法，通过生成式建模实现像素级光谱分解。 | [#240](https://github.com/thinson/RS-PaperClaw/issues/240) |
| [20260401] YieldSAT: A Multimodal Benchmark Dataset for High-Resolution Crop Yield Prediction | Miranda Miro, Pathak Deepak, Helber Patrick, Bischke Benjamin, Najjar Hiba et al. | Miranda等发布YieldSAT数据集，融合卫星影像与多源农业数据，建立高分辨率作物产量预测的多模态评估基准。 | [#241](https://github.com/thinson/RS-PaperClaw/issues/241) |
| [20260401] Adversarial Attenuation Patch Attack for SAR Object Detection | Zhang Yiming, Qin Weibo, Wang Feng | Zhang等设计针对SAR目标检测的对抗衰减贴片攻击，模拟电子干扰场景下的物理层隐身攻击机制。 | [#242](https://github.com/thinson/RS-PaperClaw/issues/242) |
| [20260401] PanoAir: A Panoramic Visual-Inertial SLAM with Cross-Time Real-World UAV Dataset | Wu Yiyang, Zhang Xiaohu, Du Yanjin, Zhang Tongsu, Li Chujun et al. | Wu等构建PanoAir数据集，支持全景相机与IMU融合的无人机全向感知定位及跨时段SLAM研究。 | [#243](https://github.com/thinson/RS-PaperClaw/issues/243) |
| [20260401] Continual Vision-Language Learning for Remote Sensing: Benchmarking and Analysis | Weng Xingxing, Ni Ruifeng, Pang Chao, Hao XiangYu, Wang Yishan et al. | Weng等建立遥感视觉语言模型持续学习基准，系统分析增量训练中的灾难性遗忘问题与缓解策略。 | [#244](https://github.com/thinson/RS-PaperClaw/issues/244) |
| [20260401] PC-SAM: Patch-Constrained Fine-Grained Interactive Road Segmentation in High-Resolution Remote Sensing Images | Lv Chengcheng, Li Rushi, Wu Mincheng, Shi Xiufang, Wen Zhenyu et al. | Lv等提出PC-SAM框架，以补丁约束机制引导SAM实现高分辨率遥感影像的细粒度交互式道路提取。 | [#245](https://github.com/thinson/RS-PaperClaw/issues/245) |

## 🔎 观察

- SAM及其变体持续主导遥感交互式分割方向，但高分辨率适配与细粒度控制仍是待解难题
- 多模态基准数据集建设加速，反映出遥感AI从算法创新向系统评估与可重复性研究的范式转移

---

Powered by OpenClaw🦞

---
