# Daily Reports

最近三天日报（最新在前）：

# [20260526](./202605/20260526.md)
## 📌 今日概况

今日共检索候选论文 6 篇；关键词+LLM 智能匹配遥感交叉论文 3 篇；最终纳入日报 3 篇。

今日遥感AI研究呈现多元化趋势：无人机载SAR成像优化、图像分割评估方法反思，以及面向全球泛化的道路交互式提取成为三大焦点。学术界持续关注模型泛化能力与评估指标可靠性等基础问题。

## ✨ 今日亮点

- UAV-MIMO TomoSAR通过粒子群优化实现点扩散函数优化，提升三维成像质量
- 图像阈值分割研究揭示SSIM、PSNR等常用指标对特定评价函数存在系统性偏差
- RoadGIE构建全球尺度航空道路数据集，推动交互式分割的跨域泛化研究

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260526] Point Spread Function Optimization for Communication-assisted UAV-borne MIMO TomoSAR | Fakharizadeh Pouya, Lahmeri Mohamed-Amine, Krieger Gerhard, Schober Robert | Friedrich-Alexander-Universität Erlangen-Nürnberg (FAU)；German Aerospace Center (DLR), Microwaves and Radar Institute | 该研究针对通信辅助无人机载MIMO TomoSAR系统，采用粒子群优化算法优化点扩散函数，以改善三维成像性能。 | [#620](https://github.com/thinson/RS-PaperClaw/issues/620) |
| [20260526] Image Thresholding: Understanding Bias of Evaluation Metrics towards Specific Evaluation Functions | Hegazy Eslam, Gabr Mohamed | German University in Cairo | 论文系统分析了图像阈值分割中常用评估指标（SSIM、PSNR等）对特定评价函数的偏向性问题。 | [#621](https://github.com/thinson/RS-PaperClaw/issues/621) |
| [20260526] RoadGIE: Towards A Global-Scale Aerial Benchmark for Generalizable Interactive Road Extraction | Peng Chenxu, Wang Chenxu, Dai Yimian, Liu Yongxiang, Cheng Ming-Ming, Li Xiang | NKIARI；VCIP, CS, Nankai University；AAIS, Nankai University；College of Electronic Engineering, National University of Defense Technology | RoadGIE构建了首个全球尺度航空道路交互式分割基准数据集，重点解决模型跨域泛化难题。 | [#622](https://github.com/thinson/RS-PaperClaw/issues/622) |

## 🔎 观察

- 遥感模型评估体系正从单一精度指标向多维度、抗偏差指标演进，反映领域对可靠性的重视
- 无人机平台与SAR技术的融合持续深化，优化算法从传统方法向群体智能演进

---

Powered by OpenClaw🦞

---

# [20260525](./202605/20260525.md)
## 📌 今日概况

今日共检索候选论文 13 篇；关键词+LLM 智能匹配遥感交叉论文 6 篇；最终纳入日报 5 篇。

今日遥感AI研究聚焦三维空间智能与低空经济应用。多模态大模型开始探索高度信息消除二维歧义，无人机相关研究涵盖异常检测、动作识别与空域规划，超宽幅图像分割方法亦有新进展，体现从感知向认知与决策的延伸趋势。

## ✨ 今日亮点

- VertiCue-Bench首次系统评估MLLMs利用冠层高度模型解决二维语义歧义的能力
- SFR-Net提出尺度-视锥体表征，针对性解决超宽幅遥感图像分割中的尺度与上下文连续性难题
- AeroTSBoost结合时序统计特征与LightGBM，面向真实场景无人机遥测异常挖掘

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260525] VertiCue-Bench: Diagnosing Whether MLLMs Use Height Cues to Resolve 2D Ambiguity in Remote Sensing Natural Scenes | Huang Jing, Wang Duanchu, Yang Junjie, Cheng Zihang, Li Cheng, Cui Lin, Wu Zhouyi, Wang Di | Xi'an Jiaotong University；Xidian University；University of Chinese Academy of Sciences | VertiCue-Bench构建诊断基准，检验多模态大语言模型是否利用高度线索消解遥感自然场景的二维歧义。 | [#614](https://github.com/thinson/RS-PaperClaw/issues/614) |
| [20260525] SFR-Net: Learning Scale-Frustum Representations for Ultra-Wide Area Remote Sensing Image Segmentation | Zhong Chuyu, Chen Keyan, Yang Qinzhe, Chen Bowen, Zou Zhengxia, Shi Zhenwei | Shen Yuan Honors College, Beihang University；the College of Computing and patches. While this processing strategy can capture abun- | SFR-Net学习尺度-视锥体表征，兼顾超宽幅遥感图像的多尺度建模与上下文语义连续性。 | [#615](https://github.com/thinson/RS-PaperClaw/issues/615) |
| [20260525] AeroTSBoost: Temporal-Statistical Boosting for Real-World UAV Telemetry Anomaly Mining | Wei Junhao, Li Haochen, Li Yanxiao, Zhao Yifu, Yao Dexing, Lu Baili, Ye Xudong, Im Sio-Kei, Wang Yapeng, Yang Xu | Faculty of Applied Sciences, Macao Polytechnic University；Pazhou Lab (Huangpu)；Macao Polytechnic University | AeroTSBoost融合时序统计增强与LightGBM，提升真实世界无人机遥测数据异常检测性能。 | [#616](https://github.com/thinson/RS-PaperClaw/issues/616) |
| [20260525] UAV-OVO: Out-of-Viewpoint Generalization in UAV Action Recognition | Xia Yu, Zhang Zhengbo, Zhang Shuaihu, Tu Zhigang | Wuhan University；Singapore University of Technology and Design | UAV-OVO研究无人机动作识别中的跨视角泛化问题，提升模型对分布外视角的鲁棒性。 | [#617](https://github.com/thinson/RS-PaperClaw/issues/617) |
| [20260525] Location Prior Generation via Multi-Source Urban Data Fusion for Low-Altitude Air Mobility | Xie Xiang, Liu Xiaonan | the School of Natural and Computing Science, University of Aberdeen, Aberdeen, U.K | 通过多源城市数据融合生成位置先验，支撑低空空中交通的建筑物高度估计与空域规划。 | [#618](https://github.com/thinson/RS-PaperClaw/issues/618) |

## ⚠️ 未纳入日报的匹配论文

以下论文通过关键词/LLM 筛选，但在处理过程中失败未纳入日报。点击 arXiv 链接可查看原文。

| 标题 | arXiv | 失败原因 |
|------|-------|----------|
| Leveraging Space-Time Synchronization for Ultra-Spot Detection in mmWave/THz UAV-to-UAV Communications | [2605.25321v1](https://arxiv.org/abs/2605.25321v1) | 质检未通过: 单位为空或无效 |


## 🔎 观察

- 三维地理空间推理成为多模态大模型新考点，高度信息正从辅助数据升格为核心推理依据
- 低空经济驱动无人机研究分化：感知层（异常/动作识别）与规划层（空域/高度估计）并行发展

---

Powered by OpenClaw🦞

---

# [20260523](./202605/20260523.md)
## 📌 今日概况

今日共检索候选论文 10 篇；关键词+LLM 智能匹配遥感交叉论文 8 篇；最终纳入日报 8 篇。

今日遥感AI研究呈现多模态融合与模型可解释性并重的趋势。视觉-语言模型在遥感检索与分割任务中持续深化，知识蒸馏与域适应技术成为解决数据稀缺的主流路径。同时，物理一致性与科学对齐开始受到关注，预训练模型的跨模态迁移能力得到进一步挖掘。

## ✨ 今日亮点

- GRAIL框架实现卫星数据科学工作流的自然语言到代码自动翻译
- TC-Bench首次系统评估视觉基础模型的物理可解释性与科学对齐度
- DisDop提出域先验蒸馏策略，突破航拍开放词汇检测瓶颈

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260523] GRAIL: AI translation for scientists application workflow on satellite data | Shang Zhuocheng, Eldawy Ahmed | University of California, Riverside | GRAIL基于大语言模型构建卫星数据处理的自然语言编程接口，支持Apache Spark分布式计算工作流自动生成。 | [#605](https://github.com/thinson/RS-PaperClaw/issues/605) |
| [20260523] The Perception-Physics Paradox: Probing Scientific Alignment with TC-Bench | Yao Dingling, Polesello Andrea, Pervez Adeel, Muller Caroline, Locatello Francesco | CausalLearningAI | TC-Bench通过结构同构性分析揭示视觉基础模型感知能力与物理规律理解之间的悖论性差距。 | [#606](https://github.com/thinson/RS-PaperClaw/issues/606) |
| [20260523] Leveraging pretrained RGB denoisers for hyperspectral image restoration | Picone Daniele, Jouni Mohamad, Dalla-Mura Mauro | Univ. Grenoble Alpes, CNRS, Grenoble INP, GIPSA-Lab | 提出将预训练RGB去噪器迁移至高光谱图像复原的即插即用框架，通过光谱投影实现跨模态知识复用。 | [#607](https://github.com/thinson/RS-PaperClaw/issues/607) |
| [20260523] Analysis of Altitude-Dependent Electronic Conspicuity in Cellular-Connected UAVs | Md Sharif Hossen, Vijay K. Shah, Guvenc Ismail | North Carolina State University | 量化分析蜂窝网络连接无人机的海拔高度对电子可见性及小区间干扰的影响规律。 | [#608](https://github.com/thinson/RS-PaperClaw/issues/608) |
| [20260523] DisDop: Distillation with Domain Priors for Open-Vocabulary Aerial Object Detection | Xu Ruihao, Liu Yong, Tang Yansong, Bai Sule, Ye Xubing, Yu Bingyao, Guo Yutao, Lu Jiwen, Zhou Jie | Tsinghua Shenzhen International Graduate School, Tsinghua University；Tsinghua University | DisDop融合域先验知识与知识蒸馏，提升开放词汇航拍目标检测对新类别的泛化能力。 | [#609](https://github.com/thinson/RS-PaperClaw/issues/609) |
| [20260523] Image-Conditioned Instance Prompt Network for Referring Remote Sensing Image Segmentation | Ren Biaoyu, Wang Qingsheng, Xu Cun, Yang Dingkang, Wang Wenxuan | School of Computer Science, Northwestern Polytechnical University；College of Intelligent Robotics and Advanced Manufacturing, Fudan University；Shenzhen Research Institute of Northwestern Polytechnical University | 图像条件实例提示网络实现遥感图像的指代分割，强化跨模态实例级理解能力。 | [#610](https://github.com/thinson/RS-PaperClaw/issues/610) |
| [20260523] Coarse-to-Fine Domain Incremental Learning with Attentive Distillation for Mining Footprint Segmentation in Multispectral Imagery | Alif Tri Handoyo, Vincent C.S. Lee, Rizka Widyarini Purwanto, Alex M. Lechner, Kemp Deanna, Muhamad Risqi U. Saputra | Monash University；Northeastern University；The University of Queensland | 面向多光谱矿区足迹分割的粗到细域增量学习框架，采用注意力蒸馏缓解域漂移。 | [#611](https://github.com/thinson/RS-PaperClaw/issues/611) |
| [20260523] Benchmarking Composed Image Retrieval for Applied Earth Observation | Psomas Bill, Christopoulos Dionysis, Petropoulos Thanasis, Efthymiadis Nikos, Kakogeorgiou Ioannis, Chum Ondřej, Avrithis Yannis, Tolias Giorgos, Karantzalos Konstantinos | Visual Recognition Group, Department of Cybernetics, Czech Technical University in Prague；Remote Sensing Laboratory, School of Rural, Surveying and Geoinformatics Engineering, National Technical University of Athens；Institute of Informatics & Telecommunications, National Centre for Scientific Research "Demokritos"；Department of Informatics and Telecommunications, National and Kapodistrian University of Athens | 首个面向地球观测的组合图像检索基准测试，系统评估视觉-语言模型的复杂查询理解能力。 | [#612](https://github.com/thinson/RS-PaperClaw/issues/612) |

## 🔎 观察

- 视觉-语言模型正从通用场景向遥感专用化演进，但科学任务所需的物理可解释性仍是明显短板
- 知识蒸馏与域适应技术的密集出现，反映出遥感数据标注成本高、分布差异大的结构性困境

---

Powered by OpenClaw🦞

---
