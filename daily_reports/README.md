# Daily Reports

最近三天日报（最新在前）：

# [20260424](./202604/20260424.md)
## 📌 今日概况

今日共检索候选论文 4 篇；关键词+LLM 智能匹配遥感交叉论文 2 篇；最终纳入日报 2 篇。

今日遥感AI研究聚焦两大方向：一是灾害变化检测的语义理解升级，通过视觉-语言模型实现从像素检测到灾害语义解析的跨越；二是SAR图像的跨模态知识迁移，利用光学先验破解SAR数据标注稀缺难题，推动无监督类别发现。

## ✨ 今日亮点

- ChangeQuery构建视觉-语言框架，实现灾害变化检测的语义级理解突破
- 光谱引导知识迁移首次将光学域先验系统注入SAR广义类别发现
- 跨模态学习成为解决遥感数据异质性与标注瓶颈的核心技术路径

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260424] ChangeQuery: Advancing Remote Sensing Change Analysis for Natural and Human-Induced Disasters from Visual Detection to Semantic Understanding | Sun Dongwei, Yao Jing, Wei Kan, Cao Xiangyong, Wu Chen, Zhao Zhenghui, Ghamisi Pedram, Zhou Jun, Jón Atli Benediktsson | Chinese Academy of Sciences；University of Iceland；Technical University of Munich；German Aerospace Center；Helmholtz-Zentrum Hereon；Griffith University | ChangeQuery提出视觉-语言变化检测框架，将灾害分析从视觉检测提升至语义理解层次。 | [#405](https://github.com/thinson/RS-PaperClaw/issues/405) |
| [20260424] Unlocking Optical Prior: Spectrum-Guided Knowledge Transfer for SAR Generalized Category Discovery | Xia Jingyuan, Hu Ruikang, Li Ye, Yang Zhixiong, Lan Xu, Lu Zhejun | the State Key Laboratory of Complex System | 该研究通过频域光谱引导，实现光学到SAR的知识迁移，解决SAR广义类别发现难题。 | [#406](https://github.com/thinson/RS-PaperClaw/issues/406) |

## 🔎 观察

- 视觉-语言模型正重塑遥感变化检测范式，从像素差异比对转向可解释的灾害语义推理。
- SAR与光学数据的跨模态知识迁移或成突破SAR标注瓶颈的关键，但频域对齐的鲁棒性仍需验证。

---

Powered by OpenClaw🦞

---

# [20260423](./202604/20260423.md)
## 📌 今日概况

今日共检索候选论文 8 篇；关键词+LLM 智能匹配遥感交叉论文 4 篇；最终纳入日报 3 篇。

今日遥感AI研究聚焦图像超分辨率与精细化分割任务。合成数据集构建、无人机 beach litter 监测及红外图像超分挑战赛成为三大主线，体现从数据生成到真实场景落地的技术链条，深度学习在像素级任务中的精度提升持续受到关注。

## ✨ 今日亮点

- SyMTRS发布多任务合成数据集，同步支撑深度估计、域适应与超分辨率研究
- PLAS-Net实现无人机海滩垃圾像素级分割，推动海洋 debris 自动化监测
- NTIRE 2026首届遥感红外图像超分挑战赛公布基准结果与方法综述

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260423] SyMTRS: Benchmark Multi-Task Synthetic Dataset for Depth, Domain Adaptation and Super-Resolution in Aerial Imagery | Safouane El Ghazouali, Venturi Nicola, Rueegsegger Michael, Michelucci Umberto | TOELT LLC AI lab / HSLU；Competence Center for Artificial Intelligence and Simulation, armasuisse S+T | SyMTRS构建航空影像多任务合成数据集，为深度估计、域适应与超分辨率提供统一基准。 | [#401](https://github.com/thinson/RS-PaperClaw/issues/401) |
| [20260423] PLAS-Net: Pixel-Level Area Segmentation for UAV-Based Beach Litter Monitoring | Liu Yongying, Wang Jiaqi, Song Jian, Shao Xinlei, Chen Yijia, Xu Nan, Mizuno Katsunori, Tabeta Shigeru, Zhao Fan | Graduate School of Frontier Sciences, The University of Tokyo；Department of Urban Informatics, Shenzhen University | PLAS-Net提出像素级面积分割网络，用于无人机海滩垃圾监测，实现实例级精细化识别。 | [#402](https://github.com/thinson/RS-PaperClaw/issues/402) |
| [20260423] The First Challenge on Remote Sensing Infrared Image Super-Resolution at NTIRE 2026: Benchmark Results and Method Overview | Liu Kai, Yue Haoyang, Lin Zeli, Chen Zheng, Wang Jingkai, Gong Jue, Li Jiatong, Yan Xianglong, Zhu Libo, Li Jianze, Zhang Ziqing, Zhou Zihan, Liu Xiaoyang, Timofte Radu, Zhang Yulun, Chen Junye, Yan Zhenming, Hong Yucong, Han Ruize, ..., Gressin Adrien | NTIRE 2026 | NTIRE 2026首届遥感红外图像超分辨率挑战赛发布，汇总参赛方法与基准性能结果。 | [#403](https://github.com/thinson/RS-PaperClaw/issues/403) |

## 🔎 观察

- 合成数据与真实场景数据并重，反映遥感AI对标注成本高、样本稀缺问题的应对策略分化
- 无人机平台成为近岸环境监测主力载体，像素级分割精度直接决定 debris 量化可靠性

---

Powered by OpenClaw🦞

---

# [20260422](./202604/20260422.md)
## 📌 今日概况

今日共检索候选论文 7 篇；关键词+LLM 智能匹配遥感交叉论文 5 篇；最终纳入日报 5 篇。

今日遥感AI研究呈现多模态融合与基础模型优化并进的态势。SAR时序分析支撑海上风电基础设施监测，跨模态检索采用粗精两阶段策略提升效率，变化检测引入检索增强与Best-of-N排序构建新基准，面向对象检测探索傅里叶级数编码解决角度边界不连续问题，半监督流匹配模型推动马赛克与全色图像融合成像。

## ✨ 今日亮点

- 密集Sentinel-1时序实现全球海上风电部署动态监测
- 检索增强Best-of-N排序构建遥感区域变化理解新基准
- 傅里叶级数编码创新解决旋转目标检测角度边界不连续难题

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260422] Global Offshore Wind Infrastructure: Deployment and Operational Dynamics from Dense Sentinel-1 Time Series | Hoeser Thorsten, Bachofer Felix, Kuenzer Claudia | Earth Observation Center (EOC), German Aerospace Center (DLR)；Institute for Geography and Geology, University of Wuerzburg | 基于密集Sentinel-1时序数据，构建全球海上风电基础设施部署与运行动态监测框架。 | [#395](https://github.com/thinson/RS-PaperClaw/issues/395) |
| [20260422] RSRCC: A Remote Sensing Regional Change Comprehension Benchmark Constructed via Retrieval-Augmented Best-of-N Ranking | Kazoom Roie, Gigi Yotam, Leifman George, Shekel Tomer, Beryozkin Genady | Google Research | 提出RSRCC基准，通过检索增强与Best-of-N排序构建遥感区域变化理解评测体系。 | [#396](https://github.com/thinson/RS-PaperClaw/issues/396) |
| [20260422] Fast-then-Fine: A Two-Stage Framework with Multi-Granular Representation for Cross-Modal Retrieval in Remote Sensing | Chen Xi, Chen Xu, Jia Xiangyang, Zhang Xu, Wei Shuquan, Wang Wei | School of Computer Science, Wuhan University；Beijing Institute for General Artificial Intelligence (BIGAI) | 设计粗精两阶段跨模态检索框架，利用多粒度表征提升遥感图像-文本检索效率。 | [#397](https://github.com/thinson/RS-PaperClaw/issues/397) |
| [20260422] Fourier Series Coder: A Novel Perspective on Angle Boundary Discontinuity Problem for Oriented Object Detection | Wei Minghong, Cao Pu, Chen Zhihao, Zang Zhiyuan, Yang Lu, Song Qing | Tsinghua University；Chinese Academy of Sciences | 以傅里叶级数编码新视角解决旋转目标检测中的角度边界不连续与周期模糊问题。 | [#398](https://github.com/thinson/RS-PaperClaw/issues/398) |
| [20260422] Semi-Supervised Flow Matching for Mosaiced and Panchromatic Fusion Imaging | Luo Peiming, Wang Nan, Liu Litong, Huang Jiahan, Wu Chenxu, Dian Renwei, Hou Junming | Southeast University；Hunan University | 提出半监督流匹配方法，实现马赛克图像与全色图像的高质量融合成像。 | [#399](https://github.com/thinson/RS-PaperClaw/issues/399) |

## 🔎 观察

- 时序SAR数据正成为能源基础设施监测的核心数据源，海上风电等新兴领域需求凸显。
- 检索增强与生成模型技术向遥感基准构建渗透，反映领域对高质量评测与数据效率的双重追求。

---

Powered by OpenClaw🦞

---
