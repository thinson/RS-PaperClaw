# Daily Reports

最近三天日报（最新在前）：

# [20260510](./202605/20260510.md)
## 📌 今日概况

今日共检索候选论文 5 篇；关键词+LLM 智能匹配遥感交叉论文 3 篇；最终纳入日报 2 篇。

今日遥感AI研究聚焦两大方向：一是面向地质灾害监测的高效特征选择方法，通过序列特征筛选优化滑坡分割任务；二是针对遥感图像质量提升的生成式建模，结合空间-频率域信息改进超分辨率重建。两项工作均体现轻量化设计与多源信息融合的研究趋势。

## ✨ 今日亮点

- 序列特征选择策略降低多光谱滑坡分割计算成本，提升模型效率
- 空间-频率门控Swin Transformer实现遥感单图超分辨率，兼顾全局与细节重建
- 印度多机构联合推进遥感图像增强技术，强化实际应用价值

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260510] Sequential Feature Selection for Efficient Landslide Segmentation from Multi-Spectral Data | Ahmad Arsalaan, Karakus Oktay, Paul L. Rosin | School of Computer Science and Informatics；Cardiff University | 卡迪夫大学团队提出序列特征选择方法，从多光谱数据中高效提取滑坡敏感特征，优化分割模型计算效率。 | [#500](https://github.com/thinson/RS-PaperClaw/issues/500) |
| [20260510] Spatial-Frequency Gated Swin Transformer for Remote Sensing Single-Image Super-Resolution | Md Aminur Hossain, Valkesh Parekh, Ayush V. Patel, Jethani Yogesh, Sanjay K. Singh, Banerjee Biplab | Space Applications Centre, ISRO, Ahmedabad, India；Centre of Studies in Resources Engineering, Indian Institute of Technology Bombay, India；New L J Institute of Engineering and Technology, Ahmedabad, India；Pandit Deendayal Energy University, Gandhinagar, India；GLS University, Ahmedabad, India | 印度空间应用中心等机构联合开发空间-频率门控Swin Transformer，通过频域-空域协同建模提升遥感图像超分辨率质量。 | [#501](https://github.com/thinson/RS-PaperClaw/issues/501) |

## 🔎 观察

- 特征选择技术重回遥感深度学习视野，反映边缘部署场景对模型轻量化的迫切需求
- Swin Transformer在遥感低层视觉任务中持续演进，门控机制与频域先验的结合或成为新范式

---

Powered by OpenClaw🦞

---

# [20260509](./202605/20260509.md)
## 📌 今日概况

今日共检索候选论文 5 篇；关键词+LLM 智能匹配遥感交叉论文 5 篇；最终纳入日报 4 篇。

今日遥感AI研究呈现三大趋势：一是甲烷监测与不确定性量化结合，推动多源卫星数据融合应用；二是深度学习向社会经济指标预测拓展，夜间灯光数据价值凸显；三是生成式压缩与超算结合，探索地球观测数据量级缩减新路径。工程检测领域亦见频域监督学习创新。

## ✨ 今日亮点

- HyGAS平台实现多卫星甲烷羽流反演与排放率估计，突破传感器依赖性限制
- 意大利市政收入预测研究验证夜间灯光深度学习在经济遥感中的可行性
- 生成式压缩模型借助历史先验与超算实现万倍数据缩减，重塑EO数据使用范式

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260509] HyGAS: an Open, Sensor-Agnostic Platform for Multi-Satellite Methane Plume Retrieval, Uncertainty Propagation, and Emission-Rate Estimation | Ferrari Alvise, Pampanoni Valerio, Laneve Giovanni | GMATICS S.r.l.；School of Aerospace Engineering, Sapienza University | HyGAS构建开放的多卫星甲烷反演平台，集成不确定性传播与排放率估计，支持成像光谱仪跨传感器应用。 | [#495](https://github.com/thinson/RS-PaperClaw/issues/495) |
| [20260509] Nowcasting Italian Municipal Income with Nightlights: A Deep Learning Approach | Giannini Massimo | University of Rome Tor Vergata | 基于循环神经网络利用夜间灯光数据实现意大利市政收入动态预测，拓展遥感在经济监测中的实时应用。 | [#496](https://github.com/thinson/RS-PaperClaw/issues/496) |
| [20260509] Contour-Native Bridge Defect Detection and Compact Digital Archiving with Frequency-Supervised Fourier Contours | Liu Jin, Wang Wang, Pu Hongxu, Cao Zhen, Wang Yasong, Wang Hu, Luo Kunming | State Key Laboratory of Information Engineering in Surveying, Mapping and Remote Sensing, Wuhan University；Sustainability X-Lab, The University of Hong Kong；Department of Cyber Security, Southeast University；School of Computer Science and Engineering, University of Electronic Science and Technology of China；Department of Electronic and Computer Engineering, The Hong Kong University of Science and Technology | 提出频域监督傅里叶轮廓方法，实现无人机影像桥梁缺陷检测与紧凑矢量数字存档。 | [#497](https://github.com/thinson/RS-PaperClaw/issues/497) |
| [20260509] Transforming the Use of Earth Observation Data: Exascale Training of a Generative Compression Model with Historical Priors for up to 10,000x Data Reduction | Zhang Jinxiao, Dong Runmin, Wu Xiyong, Huang Xihan, Cheng Shenggan, Yang Yunkai, Zhou Zheng, Xu Yunpu, Luo Zhaoyang, Yang Miao, Wei Fan, Chen Mengxuan, You Yang, Zheng Juepeng, Li Weijia, Lu Yutong, Fu Haohuan | Institute of Data and Information, Tsinghua Shenzhen International Graduate School；Department of Earth System Science, Tsinghua University；Sun Yat-Sen University；National University of Singapore；National Supercomputing Center in Shenzhen | 开发基于历史先验的生成式压缩模型，依托E级计算实现地球观测数据高达10000倍缩减。 | [#498](https://github.com/thinson/RS-PaperClaw/issues/498) |

## ⚠️ 未纳入日报的匹配论文

以下论文通过关键词/LLM 筛选，但在处理过程中失败未纳入日报。点击 arXiv 链接可查看原文。

| 标题 | arXiv | 失败原因 |
|------|-------|----------|
| Technical Report: A Hierarchical Dynamically Weighting Deep Reinforcement Learning Method for Multi-UAV Multi-Task Coordination | [2605.08623v1](https://arxiv.org/abs/2605.08623v1) | 质检未通过: 单位为空或无效 |


## 🔎 观察

- 生成式压缩与超算结合标志着EO数据管理从存储驱动向计算驱动转型，但历史先验的泛化性仍需跨场景验证。
- 甲烷监测平台化与传感器无关化设计反映碳监测标准化需求，不确定性量化或成为下一代遥感产品的合规门槛。

---

Powered by OpenClaw🦞

---

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
