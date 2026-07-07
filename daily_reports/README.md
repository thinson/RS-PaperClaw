# Daily Reports

最近三天日报（最新在前）：

# [20260704](./202607/20260704.md)
## 📌 今日概况

今日共检索候选论文 10 篇；关键词+LLM 智能匹配遥感交叉论文 9 篇；最终纳入日报 8 篇。

今日遥感AI研究聚焦于轻量化与高精度分割、无人机多模态感知及三维重建。多篇工作提出专用数据集与训练-free方法，推动遥感目标分割与低空通信发展。扩散模型与Transformer架构在显著性检测与生物量估计中展现潜力。

## ✨ 今日亮点

- NWPU-Traffic数据集推动遥感交通目标实例分割
- SharpSplat利用边缘正则化提升无人机建筑三维重建
- GeoSAM-Lite实现轻量化星上遥感分割

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260704] A Large-Scale Dataset and a New Method for RemoteSensing Traffic Object Segmentation | Yang Zhigang, Yao Huiguang, Tian Linmao, Li Qiang, Wang Qi | a School of Artificial Intelligence, OPtics and ElectroNics (iOPEN), Northwestern Polytechnical；University, Xi’an, 710072, Shaanxi, China；b School of Computer Science, Northwestern Polytechnical University, Xi’an, 710072, Shaanxi, China；c School of Software, Northwestern Polytechnical University, Xi’an, 710072, Shaanxi, China | 提出大规模NWPU-Traffic数据集及交通目标实例分割方法 | [#839](https://github.com/thinson/RS-PaperClaw/issues/839) |
| [20260704] SharpSplat: Edge-Regularized 3D Gaussian Splatting for High Fidelity Urban Building Reconstruction from UAV images | Vaid Porus, Chopra Shivam, Kumar Vaibhav | uations across campus environments, dense urban centers, and | SharpSplat用边缘正则化3D高斯泼溅实现高保真建筑重建 | [#840](https://github.com/thinson/RS-PaperClaw/issues/840) |
| [20260704] GeoSelect: Spatial-Program Execution for Training-Free Referring Remote Sensing Image Segmentation | Jiang Yuhang, Deng Guohui, Xu Miaozhong, Ruan Chao, Zhao Jinling, Huang Linsheng | School of Internet, Anhui University, Hefei, China；the National Engineering Research Center for Agro-Ecological Big Data Analysis \& Application, Anhui University, Hefei, China；State Key Laboratory of Information Engineering in Surveying, Mapping and Remote Sensing, Wuhan University, Wuhan, China | GeoSelect通过空间程序执行实现免训练遥感图像分割 | [#841](https://github.com/thinson/RS-PaperClaw/issues/841) |
| [20260704] LAMBDA: A Low-Altitude Multimodal Base Dataset for UAV Sensing and Communication | Zhou Lin, Rao Peichuan, Zhang Chenshuo, Mo Jianhua, Sun Shu, Chen Zhiyong, Tao Meixia | Research on low-altitude integrated sensing and communication (ISAC) requires aligned；the same platforms and within the same networks, giving rise to a key research area known as；School of Information Science and Electronic Engineering, Shanghai Jiao Tong University, Shanghai, China | LAMBDA提供低空多模态数据集用于无人机感知与通信 | [#842](https://github.com/thinson/RS-PaperClaw/issues/842) |
| [20260704] TRISTAR: Triple-Signal Stair Recognition and Vision-Only Indoor Navigation for Search-and-Rescue Micro-UAVs | Gîngu Octavian, Spînu Stelian | International Student Conference, Military Technical Academy, Bucharest, Romania；Military Technical Academy ``Ferdinand I'', Bucharest, Romania | TRISTAR实现微无人机基于单目视觉的楼梯识别与导航 | [#843](https://github.com/thinson/RS-PaperClaw/issues/843) |
| [20260704] GeoSAM-Lite: A Lightweight Foundation Model for Onboard Remote Sensing Segmentation | Wang Yongcong, Zhang Jie, Jiang Rui, Yang Xubing, Yun Ting, Zhang Li | College of Information Science and Technology \& Artificial Intelligence, Nanjing Forestry University, Nanjing, China (；College of Telecommunications and Information Engineering, Nanjing University of Posts and Telecommunications, Nanjing, China | GeoSAM-Lite是面向星上分割的轻量级基础模型 | [#844](https://github.com/thinson/RS-PaperClaw/issues/844) |
| [20260704] IPDiff: Diffusion-driven ORSI Salient Object Detection with Information Reconstruction and Multi-Prior Guidance | Li Gongyang, Bai Zhen, Cong Runmin, Zeng Dan, Lin Weisi, Zhang Xiao-Ping | ing, Shanghai University, Shanghai, China；School of Control Science and Engineering, Shandong；University, Jinan, China；School of Computer Science and Engineering, Nanyang；Technological University, Singapore；Shenzhen Key Laboratory of Ubiquitous Data Enabling, Tsinghua Shenzhen International Graduate School；Tsinghua University, Shenzhen, China Optical Remote Sensing Images (ORSIs) refer to images | IPDiff用扩散模型与多先验引导进行遥感显著性检测 | [#845](https://github.com/thinson/RS-PaperClaw/issues/845) |
| [20260704] Phase-Preserving Trimodal Transformer for Tropical Forest Biomass Estimation Using Optical and PolInSAR Data | Luiz Felipe Parente Santiago, Rosiane Rodrigues de Freitas, Daniel Rodrigues dos Santos, Ferrari Felipe | Institute of Computing (IComp), Federal University of Amazonas (UFAM), Manaus, Brazil；Brazilian Army Research Institute in the Amazon (IPEAM), Manaus, Brazil；Military Institute of Engineering (IME), Rio de Janeiro, Brazil | 相位保持三模态Transformer融合光学与PolInSAR估测森林生物量 | [#846](https://github.com/thinson/RS-PaperClaw/issues/846) |

## ⚠️ 未纳入日报的匹配论文

以下论文通过关键词/LLM 筛选，但在处理过程中失败未纳入日报。点击 arXiv 链接可查看原文。

| 标题 | arXiv | 失败原因 |
|------|-------|----------|
| Exploring SAM Supervision for Fine-Grained UAV Target Segmentation under Data Scarcity | [2607.03754v1](https://arxiv.org/abs/2607.03754v1) | 质检未通过: 单位为空或无效 |


## 🔎 观察

- 轻量化与星上处理成为遥感分割模型落地的重要趋势
- 多模态数据融合（光学、SAR、通信信号）在低空与森林应用中加速

---

Powered by OpenClaw🦞

---

# [20260703](./202607/20260703.md)
## 📌 今日概况

今日共检索候选论文 0 篇；关键词+LLM 智能匹配遥感交叉论文 0 篇；最终纳入日报 0 篇。

当日未检索到符合条件并纳入日报的论文。

## 🔎 观察

- 当日无成功纳入论文，建议优先检查候选筛选结果与失败原因。
- 若连续出现空日报，应复核 arXiv 日期窗口、关键词配置与 LLM 筛选输出。

---

Powered by OpenClaw🦞

---

# [20260702](./202607/20260702.md)
## 📌 今日概况

今日共检索候选论文 8 篇；关键词+LLM 智能匹配遥感交叉论文 5 篇；最终纳入日报 5 篇。

今日遥感研究聚焦于智能解译与数据发现两大方向。云去除结合残差流与地理上下文对齐提升可解释性；多篇工作探索大语言模型与知识图谱在遥感数据检索、假设生成及无人机自主决策中的应用；持续学习框架被引入变化检测以应对域偏移问题。

## ✨ 今日亮点

- 云去除方法引入残差流与地理上下文对齐提升可解释性
- 多篇工作探索LLM与知识图谱驱动遥感数据智能发现
- 持续学习框架被用于域增量变化检测任务

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260702] Interpretation-Oriented Cloud Removal via Observation-Anchored Residual Flow with Geo-Contextual Alignment | Wang Ziyao, Wang Maonan, He Yucheng, Ma Xianping, Wang Ziyi, Zhang Hongyang, Cheng Yirong, Pun Man-on | School of Science and Engineering, The Chinese University of Hong Kong；Shanghai Ai Lab, Shanghai, China；Faculty of Geosciences and Engineering, Southwest Jiaotong University, Chengdu | 提出面向可解释的云去除方法，利用观测锚定残差流与地理上下文对齐。 | [#832](https://github.com/thinson/RS-PaperClaw/issues/832) |
| [20260702] Bringing Agentic Search to Earth Observation Data Discovery | Yu Minghan, Sun Youran, Yi Chugang, Wen Yixin, Yang Haizhao | University of Maryland, College Park University of Maryland, College Park；University of Maryland, College Park University of Florida；University of Maryland, College Park；NASA and its data centers hold thousands of geoscience datasets and tools like；metadata, tools, and access pathways. NASA and its affiliated data centers host thousands of datasets；across dozens of Distributed Active Archive Centers (DAACs), together with tools such as Worldview；domain experts to locate the data that best matches their own research question | 将智能体搜索引入地球观测数据发现，提升数据集检索效率。 | [#833](https://github.com/thinson/RS-PaperClaw/issues/833) |
| [20260702] Dual-Selective Network for Domain-Incremental Change Detection | He Yuzhi, Huang Junxi, Wu Haorui, Qu Jiahui | Xidian University, Xi'an, China | 提出双选择性网络用于域增量变化检测，结合视觉状态空间模型。 | [#834](https://github.com/thinson/RS-PaperClaw/issues/834) |
| [20260702] NEUROSYMLAND: Neuro-Symbolic Landing-Site Assessment for Robust and Edge-Deployable UAV Autonomy | Qian Weixian, Yang Tianyi, Schroder Sebastian, Deng Yao, Yao Jiaohong, Cheng Xiao, Han Richard, Zheng Xi | School of Computing, Macquarie University, Sydney, NSW, Australia；Macquarie University, when this work was conducted；Department of Computer Science, University of California, Santa Barbara, CA, USA. tianyi | 神经符号方法实现无人机着陆点评估，支持边缘部署与鲁棒自主。 | [#835](https://github.com/thinson/RS-PaperClaw/issues/835) |
| [20260702] EO-Agents: A Three-Agent LLM Pipeline for Earth Observation Hypothesis Generation | Ghazanfari Mahyar, Tabrizian Amin, Mehrabian Armin, Wei Peng | Earth-observation (EO) research is fundamentally combina-；Washington University, Washington, DC, USA；Space Flight Center, Greenbelt, MD, USA | 构建三智能体LLM流水线，自动生成地球观测科学假设。 | [#836](https://github.com/thinson/RS-PaperClaw/issues/836) |

## 🔎 观察

- 大语言模型正从辅助工具演变为遥感数据发现与假设生成的核心引擎。
- 持续学习与域适应成为变化检测研究新热点，应对多源数据分布漂移。

---

Powered by OpenClaw🦞

---
