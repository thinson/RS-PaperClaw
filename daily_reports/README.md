# Daily Reports

最近三天日报（最新在前）：

# [20260508](./202605/20260508.md)
## 📌 今日概况

今日共检索候选论文 18 篇；关键词+LLM 智能匹配遥感交叉论文 11 篇；最终纳入日报 10 篇。

今日遥感AI研究呈现多模态融合与三维重建两大主线。卫星-无人机-地面跨视角三维重建、高斯溅射表面重建、深度先验引导的变化检测等方向进展显著；同时，视觉语言模型的安全攻击、连续尺度条件化及地质岩性理解等基础问题受到关注，体现从应用层向模型机理与安全性的纵深探索。

## ✨ 今日亮点

- 跨视角三维重建突破：首次实现卫星、无人机与地面图像的前馈联合三维重建
- 遥感VLM安全警示：揭示大气检索劫持攻击可导致RAG系统产生幻觉
- 稀疏视角重建新范式：2D高斯溅射实现可泛化的卫星表面重建

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260508] Seeing Across Skies and Streets: Feedforward 3D Reconstruction from Satellite, Drone, and Ground Images | Wang Qiwei, Tuo Zhongyao, Ze Xianghui, Shi Yujiao | ShanghaiTech University；Nanjing University of Science and Technology | 提出前馈网络实现卫星、无人机与地面图像的联合三维重建，解决跨视角定位难题。 | [#484](https://github.com/thinson/RS-PaperClaw/issues/484) |
| [20260508] LithoBench: Benchmarking Large Multimodal Models for Remote-Sensing Lithology Interpretation | Wang Jun, Li Fengpeng, Dong Hang, Huang Tianjin, Han Wei | School of Computer Science, China University of Geosciences；PRADA Lab, King Abdullah University of Science and Technology；Department of Computer Science, University of Exeter | 构建首个遥感岩性理解多模态大模型基准测试集LithoBench。 | [#485](https://github.com/thinson/RS-PaperClaw/issues/485) |
| [20260508] Beyond GSD-as-Token: Continuous Scale Conditioning for Remote Sensing VLMs | Zhang Song, Chen Yanlong, Li Yilin, Chen Yining, Yi Zili, Zhang Xiaowei, Li Yawei | Nanjing University；ETH Zurich；RWTH Aachen University；Nanjing University of Posts and Telecommunications | 提出连续尺度条件化方法，突破传统GSD离散分桶对遥感VLM的局限。 | [#486](https://github.com/thinson/RS-PaperClaw/issues/486) |
| [20260508] From Clouds to Hallucinations: Atmospheric Retrieval Hijacking in Remote Sensing Vision-Language RAG | Han Jiaju, Li Chao, Hu Chengyin, Zhang Qike, Sun Xuemeng, Wang Xin, Zhang Fengyu, Chen Xiang, Wei Yiwei, Long Jiahuan, Guo Jiujiang | China University of Petroleum, Beijing at Karamay | 首次揭示针对遥感视觉语言RAG的大气检索劫持攻击及其幻觉诱导机制。 | [#487](https://github.com/thinson/RS-PaperClaw/issues/487) |
| [20260508] Sat3R: Satellite DSM Reconstruction via RPC-Aware Depth Fine-tuning | Yang Qiaoyi, Zhou Chaoyi, Liu Xi, Wang Run, Xu Minghui, Mert D. Pesé, Luo Feng, Xu Yuhao, Cheng Zhi-Qi, Chen Qiushi, Qi Hairong, Huang Siyu | Clemson University；University of Washington；University of Tennessee | 基于RPC感知深度微调实现卫星DSM重建，优化单目深度估计。 | [#488](https://github.com/thinson/RS-PaperClaw/issues/488) |
| [20260508] Omnidirectional Transponder for Narrow-band Radar Calibration | Cohen Oren, Vana Moshe | ELTA Systems Ltd | 设计全向应答器用于窄带雷达校准，支持圆迹SAR等复杂成像模式。 | [#489](https://github.com/thinson/RS-PaperClaw/issues/489) |
| [20260508] SatSurfGS: Generalizable 2D Gaussian Splatting for Sparse-View Satellite Surface Reconstruction | Chen Min, Guo Wei, Wang Bin, Li Wen, Fang Tong, Zhang Jinbo, Zhao Junqi, Kuang Hong, Hu Han, Ge Xuming, Zhu Qing, Xu Bo | Faculty of Geosciences and Engineering, Southwest Jiaotong University；School of Geography and Environment, Jiangxi Normal University；College of Geodesy and Geomatics, Shandong University of Science and Technology | 提出可泛化的2D高斯溅射方法，解决稀疏视角卫星表面重建问题。 | [#490](https://github.com/thinson/RS-PaperClaw/issues/490) |
| [20260508] Masks Can Talk: Extracting Structured Text Information from Single-Modal Images for Remote Sensing Change Detection | Zheng Kai, Dong Hang-Cheng, Pan Jiatong, Wu Zhenkai, Wei Fupeng, Zhang Wei | Zhejiang University；Harbin Institute of Technology；Harbin Institute of Technology Suzhou Research Institute；North China University of Water Resources and Electric Power；University of Auckland | 从单模态图像提取结构化文本信息，以掩码标签引导遥感变化检测。 | [#491](https://github.com/thinson/RS-PaperClaw/issues/491) |
| [20260508] DPG-CD: Depth-Prior-Guided Cross-Modal Joint 2D-3D Change Detection | Zhang Luqi, Dong Zhen, Yang Bisheng | State Key Laboratory of Information Engineering in Surveying, Mapping and Remote Sensing, Wuhan University | 融合深度先验与跨模态信息，实现2D-3D联合城市变化检测。 | [#492](https://github.com/thinson/RS-PaperClaw/issues/492) |
| [20260508] InfoGeo: Information-Theoretic Object-Centric Learning for Cross-View Generalizable UAV Geo-Localization | Zhang Hongyang, Wang Maonnan, Wang Ziyao, Yin Hongrui, OnPun Man | City University of Hong Kong；Shenzhen University；Peng Cheng Laboratory | 基于信息瓶颈的对象中心学习，提升无人机跨视角地理定位泛化能力。 | [#493](https://github.com/thinson/RS-PaperClaw/issues/493) |

## 🔎 观察

- 三维重建技术路线分化明显：神经辐射场、高斯溅射与显式几何方法并行发展，跨视角融合成为新竞争点
- 遥感VLM研究从能力扩展转向安全可控，对抗攻击与幻觉问题揭示实际部署的潜在风险

---

Powered by OpenClaw🦞

---

# [20260507](./202605/20260507.md)
## 📌 今日概况

今日共检索候选论文 3 篇；关键词+LLM 智能匹配遥感交叉论文 3 篇；最终纳入日报 3 篇。

今日遥感AI研究呈现三大趋势：一是世界模型向地球系统科学深度渗透，上海AI Lab等机构推出无网格大气世界模型；二是不确定性量化与边缘学习结合，提升遥感回归任务可靠性；三是基础模型嵌入（AlphaEarth）支撑生态监测应用，斯坦福团队将其用于巴西大西洋森林恢复评估。

## ✨ 今日亮点

- Earth-o1突破传统网格化模拟范式，实现观测原生的大气世界建模
- 不确定性引导的边缘学习框架为遥感深度学习提供可靠性保障
- AlphaEarth基础模型嵌入赋能热带森林恢复成效的空间量化评估

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260507] Earth-o1: A Grid-free Observation-native Atmospheric World Model | Gong Junchao, Xu Kaiyi, Wei Wangxu, Tu Siwei, Xu Jingyi, Liu Zili, Fan Hang, Zhou Zhiwang, Han Tao, Xiao Yi, Gu Xinyu, Li Zhangrui, Zhang Wenlong, Chen Hao, Yang Xiaokang, Wang Yaqiang, Cheng Lijing, Gentine Pierre, Ouyang Wanli, ..., Bai Lei | Shanghai Artificial Intelligence Laboratory；Department of Information Engineering, The Chinese University of Hong Kong；School of Electronic Information and Electrical Engineering, Shanghai Jiao Tong University；Department of Atmospheric and Oceanic Sciences, Fudan University；School of Information Science and Technology, University of Science and Technology of China；State Key Laboratory of Earth System Numerical Modeling and Application, Institute of Atmospheric Physics, Chinese Academy of Sciences；College of Computer Science and Artificial Intelligence, Fudan University；Department of Earth and Environmental Engineering, Columbia University；Chinese Academy of Meteorological Sciences；School of Atmospheric Sciences, Nanjing University | Earth-o1构建无网格观测原生大气世界模型，融合数据同化与深度学习实现地球系统模拟新范式。 | [#480](https://github.com/thinson/RS-PaperClaw/issues/480) |
| [20260507] Uncertainty-Guided Edge Learning for Deep Image Regression in Remote Sensing | Anh Vu Nguyen, Sejdinovic Dino, Chin Tat-Jun | Australian Institute for Machine Learning (AIML), Adelaide University | 提出不确定性引导的边缘学习框架，通过Beta回归与边缘采样提升遥感图像深度回归的可靠性。 | [#481](https://github.com/thinson/RS-PaperClaw/issues/481) |
| [20260507] Characterizing Brazilian Atlantic Forest Restoration Outcomes with Geospatial Alpha Earth Embeddings | Heiman Alice | Stanford University | 利用AlphaEarth地理空间嵌入表征巴西大西洋森林恢复成效，探索基础模型在生态监测中的应用潜力。 | [#482](https://github.com/thinson/RS-PaperClaw/issues/482) |

## 🔎 观察

- 世界模型正从通用智能向地球科学专用领域延伸，'观测原生'理念或重塑数值天气预报与气候模拟的技术路线
- 遥感AI研究呈现'可靠性优先'转向，不确定性量化从后处理环节前移至模型架构设计与训练阶段

---

Powered by OpenClaw🦞

---

# [20260506](./202605/20260506.md)
## 📌 今日概况

今日共检索候选论文 11 篇；关键词+LLM 智能匹配遥感交叉论文 9 篇；最终纳入日报 8 篇。

今日遥感AI研究呈现三大趋势：一是基础模型轻量化适配（LoRA微调、扩散模型几何控制），二是自主智能体架构创新（多模态元规划器、视觉语言跟踪），三是零标注学习范式兴起（自监督地理推理、原型学习）。量子计算与模糊逻辑也开始渗透高光谱异常检测领域。

## ✨ 今日亮点

- LoRA微调地理基础模型实现野火精准制图，降低 Sentinel-2 应用门槛
- 轻量化多模态元规划器框架打通遥感感知与决策执行闭环
- 零标注地理推理模型 RemoteZero 突破人工标注依赖瓶颈

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260506] Hyperspectral Anomaly Detection Using Einstein Fuzzy Computing and Quantum Neural Network | Lin Chia-Hsiang, Young Si-Sheng, Langari Reza | the Department of Electrical Engineering, Na- verse network architectures；the Institute of Computer and Communication Engineer- Nevertheless, relying solely on residual-based detectors may；the Department of Mechanical Engineering, Texas | 爱因斯坦模糊计算与量子神经网络结合，为高光谱异常检测提供新型混合智能架构。 | [#335](https://github.com/thinson/RS-PaperClaw/issues/335) |
| [20260506] Low-Rank Adaptation of Geospatial Foundation Models for Wildfire Mapping Using Sentinel-2 Data | Shibli Ali, Nascetti Andrea, Ban Yifang | KTH Royal Institute of Technology | 基于LoRA的地理基础模型参数高效微调，实现Sentinel-2野火燃烧区高精度自动提取。 | [#472](https://github.com/thinson/RS-PaperClaw/issues/472) |
| [20260506] Bridging Perception and Action: A Lightweight Multimodal Meta-Planner Framework for Robust Earth Observation Agents | Xu Jinghui, Shangguan Boyi, Zhu Mengke, Liu Hao, Jiang Junhuan, He Guangjun, Feng Pengming, Jin Shichao, Liang Bin, Chang Yongzhe, Tan Junbo, Zhang Tiantian, Wang Xueqian | State Key Laboratory of Space Information System and Integrated Application | 轻量级多模态元规划器框架支撑地球观测智能体从感知到行动的自主闭环决策。 | [#473](https://github.com/thinson/RS-PaperClaw/issues/473) |
| [20260506] VL-UniTrack: A Unified Framework with Visual-Language Prompts for UAV-Ground Visual Tracking | Xu Boyue, Hou Ruichao, Ren Tongwei, Wu Gangshan | State Key Laboratory for Novel Software Technology, Nanjing University | VL-UniTrack统一视觉语言提示框架，实现无人机与地面跨视角目标跟踪协同。 | [#474](https://github.com/thinson/RS-PaperClaw/issues/474) |
| [20260507] Delay-Aware Large-Small Model Collaboration over LEO Satellite Networks | Guo Mingyu, Wu Wen, Wang Ying, Zhang Songge, Li Liang | Frontier Research Center, Pengcheng Laboratory；School of Information and Communication Engineering, Beijing University of Posts and Telecommunications | 大小模型协同架构结合多智能体强化学习，优化低轨卫星网络边缘计算任务卸载。 | [#475](https://github.com/thinson/RS-PaperClaw/issues/475) |
| [20260507] Efficient Geometry-Controlled High-Resolution Satellite Image Synthesis | Vasilescu Vlad, Faur Daniela, Costăchioiu Teodor | Univ. POLITEHNICA Bucharest；SIGMA Lab, CAMPUS Institute；GEOSENSE, CAMPUS Institute | 几何约束扩散模型实现高分辨率卫星影像可控合成，提升生成图像空间精度。 | [#476](https://github.com/thinson/RS-PaperClaw/issues/476) |
| [20260506] RemoteZero: Geospatial Reasoning with Zero Human Annotations | Yao Liang, Liu Fan, Xu Shengxiang, Zhang Chuanyi, Min Rui, Di Shimin, Zheng Yuhui | Hohai University；Southeast University | RemoteZero零标注框架以自监督强化学习驱动多模态大模型地理空间推理能力。 | [#477](https://github.com/thinson/RS-PaperClaw/issues/477) |
| [20260506] UAV as Urban Construction Change Monitor: A New Benchmark and Change Captioning Model | Gao Yupeng, Li Tianyu, Wang Guoqing, Yang Yang | University of Electronic Science and Technology of China | 无人机城市建筑变化监测新基准与变化描述模型，推动细粒度时序遥感理解。 | [#478](https://github.com/thinson/RS-PaperClaw/issues/478) |

## 🔎 观察

- 参数高效微调（PEFT）正成为遥感基础模型落地的关键路径，LoRA等技术显著降低行业适配成本
- 智能体架构从单一感知向"感知-规划-执行"全链条演进，多模态融合与元学习成为核心支撑技术

---

Powered by OpenClaw🦞

---
