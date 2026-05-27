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

# [20260524](./202605/20260524.md)
## 📌 今日概况

今日共检索候选论文 4 篇；关键词+LLM 智能匹配遥感交叉论文 2 篇；最终纳入日报 1 篇。

今日研究聚焦于无人机通信中的个性化联邦学习，提出了一种能效优化方案。通过梯度调度策略应对数据异构性，在保障模型个性化的同时降低能耗，体现了边缘智能与绿色通信的融合趋势。

## ✨ 今日亮点

- 无人机通信与联邦学习结合，提升边缘智能能效。
- 个性化联邦学习应对数据异构性，优化模型性能。
- 梯度调度策略实现能耗与精度的平衡。

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260524] Personalized Federated Learning by Energy-Efficient UAV Communications | Guo Shiqian, Liu Jianqing, Lorenzo Beatriz | the Department of Electrical and Computer Engineering, University of Massachusetts, Amherst, MA USA | 提出能效优化的个性化联邦学习框架，用于无人机通信场景。 | [#624](https://github.com/thinson/RS-PaperClaw/issues/624) |

## ⚠️ 未纳入日报的匹配论文

以下论文通过关键词/LLM 筛选，但在处理过程中失败未纳入日报。点击 arXiv 链接可查看原文。

| 标题 | arXiv | 失败原因 |
|------|-------|----------|
| Geo-Expert: Towards Expert-Level Geological Reasoning via Parameter-Efficient Fine-Tuning | [2605.24844v1](https://arxiv.org/abs/2605.24844v1) | 质检未通过: 单位为空或无效 |


## 🔎 观察

- 无人机边缘计算中，联邦学习正从通用向个性化演进。
- 能效与数据异构性是当前无人机联邦学习的关键挑战。

---

Powered by OpenClaw🦞

---
