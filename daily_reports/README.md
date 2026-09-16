# Daily Reports

最近三天日报（最新在前）：

# [20260915](./202609/20260915.md)
## 📌 今日概况

今日共检索候选论文 12 篇；关键词+LLM 智能匹配遥感交叉论文 5 篇；最终纳入日报 5 篇。

今日论文聚焦遥感基础模型与下游任务的衔接，涵盖标签效率、时序迁移与跨域泛化。多篇工作探索将预训练嵌入或语言模型迁移至农田制图、光谱时序预测和指代分割，强调独立验证与因果建模。同时，三维重建与多模态时空预测引入风险图引导和异步耦合机制，提升复杂场景下的鲁棒性。整体趋势显示，遥感AI正从单一精度追求转向可迁移、可解释与跨域基准构建。

## ✨ 今日亮点

- 基础模型嵌入用于农田制图，关注标签效率与时间迁移性。
- 光谱时序学习引入因果潜在预测，支持多视野地球表征。
- 指代遥感分割提出跨域基准，评估视觉语言模型泛化能力。

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260915] From Foundation Embeddings to Cropland Maps: Label Efficiency, Temporal Transferability and Independent Human Validation | Mohammad Ammar Mughees, Montefoschi Giovanni, Chen Zhongxin, Maria Antonia Brovelli | Department of Civil and Environmental Engineering, Politecnico di Milano, Milan, Italy | 评估基础嵌入在农田制图中的标签效率、时序迁移性，并引入独立人工验证。 | [#1271](https://github.com/thinson/RS-PaperClaw/issues/1271) |
| [20260915] SPEAR NeXT Causal Latent Forecasting Across Multiple Horizons for Spectral Temporal Earth Representation Learning | Ranjan Rajiv, Singh Udaiveer, Tamaskar Shashank, Saraswat Dharmendra | Plaksha University；Purdue University | 提出SPEAR NeXT，用因果潜在预测实现多视野光谱时序地球表征学习。 | [#1272](https://github.com/thinson/RS-PaperClaw/issues/1272) |
| [20260915] HLC-GS: Risk-Map-Guided Height-Layer Consistency Gaussian Splatting for DSM Reconstruction from Optical Satellite Imagery | Yang Jie, Pi Yingdong, Luo Qiyan, Wang Xiaoyu, Wen Lekang, Wang Mi | State Key Laboratory of Information Engineering in Surveying, Mapping and Remote Sensing, Wuhan University；Hubei Luojia Laboratory；School of Computer Science, Wuhan University | HLC-GS利用风险图引导高度层一致性高斯泼溅，从光学卫星影像重建DSM。 | [#1273](https://github.com/thinson/RS-PaperClaw/issues/1273) |
| [20260915] AsyncCouple-Flow: Asynchronous Cross-Modal Coupling and Flow Matching for Spatio-Temporal Forecasting | Wu Zhixiang, Liu Yining, Zhao Bo, Chen Szu-Yu, Duan Huiran, Lin Chu, Yang Chuanguang | Institute of Computing Technology, Chinese Academy of Sciences, China；Emory University, USA；University of California, Berkeley, USA；Yale University, USA；Stevens Institute of Technology, USA；City University of New York, USA | AsyncCouple-Flow通过异步跨模态耦合与流匹配，处理时空预测中的缺失模态。 | [#1274](https://github.com/thinson/RS-PaperClaw/issues/1274) |
| [20260915] VPRef: A Cross-Domain Benchmark for Referring Remote Sensing Image Segmentation | Liu Quanwei, Huang Tao, Yang Jiaqi, Xiang Wei | College of Science and Engineering, James Cook University, Cairns,, Australia (；College of Science and Engineering, James Cook University, Cairns QLD, Australia and the Center for AI and Data Science Innovation, James Cook University, Cairns QLD, Australia (；Department of Forest and Wildlife Ecology, University of Wisconsin-Madison, Madison, WI USA (；School of Computing, Engineering and Mathematical Sciences, La Trobe University, Melbourne, VIC, Australia ( | VPRef构建跨域基准，评估指代遥感图像分割中视觉语言模型的域适应能力。 | [#1275](https://github.com/thinson/RS-PaperClaw/issues/1275) |

## 🔎 观察

- 基础模型落地更重标签效率与迁移验证，而非单纯追求精度提升。
- 跨域基准与因果建模成为提升遥感模型泛化与可解释性的关键路径。

---

Powered by OpenClaw🦞

---

# [20260913](./202609/20260913.md)
## 📌 今日概况

今日共检索候选论文 10 篇；关键词+LLM 智能匹配遥感交叉论文 3 篇；最终纳入日报 2 篇。

今日两篇论文分别聚焦星上图像恢复与遥感变化视觉问答。前者提出无注意力机制的紧凑编码器，结合脉冲神经网络与神经形态计算，旨在降低星上处理功耗并保留信息，推动在轨实时恢复。后者面向双时相遥感影像的变化视觉问答，引入选择性工具调用策略，让视觉语言模型按需调用外部工具，提升复杂变化推理的准确性。整体看，研究趋势从单纯提升精度转向轻量化、低功耗与智能体式推理，强调在资源受限场景下的实用部署。

## ✨ 今日亮点

- 星上图像恢复探索无注意力紧凑编码器与脉冲神经网络，兼顾低功耗与信息保留。
- 遥感变化视觉问答引入选择性工具调用，让视觉语言模型按需借助外部工具推理。
- 两篇工作均关注资源受限场景，推动遥感AI向轻量化与智能体化方向发展。

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260913] LIMODENet: Attention-Free Compact Encoders for Information-Preserving Onboard Satellite Image Restoration | Le Thanh-Dung, Vu Nguyen Ha, Ti Ti Nguyen, Chatzinotas Symeon | Texas A\&M University - Corpus Christi, TX, USA；University of Luxembourg, Kirchberg, Luxembourg | 提出LIMODENet，用无注意力紧凑编码器与脉冲神经网络实现信息保留的星上卫星图像恢复。 | [#1287](https://github.com/thinson/RS-PaperClaw/issues/1287) |
| [20260913] Selective Tool Use for Agentic Change Visual Question Answering in Remote Sensing | Bazi Yakoub, Mohamad M. Al Rahhal, Mohamed A. Mekhtiche, Zuair Mansour | the Computer Engineering Department, College of Computer and Information Sciences, King Saud University, Riyadh, Saudi Arabia (；the Applied Computer Science Department, College of Applied Computer Science, King Saud University, Riyadh, Saudi Arabia ( | 面向双时相遥感变化视觉问答，提出选择性工具调用策略增强视觉语言模型的推理能力。 | [#1288](https://github.com/thinson/RS-PaperClaw/issues/1288) |

## ⚠️ 未纳入日报的匹配论文

以下论文通过关键词/LLM 筛选，但在处理过程中失败未纳入日报。点击 arXiv 链接可查看原文。

| 标题 | arXiv | 失败原因 |
|------|-------|----------|
| Small Object Detection in Drone Aerial Imagery with LAF-YOLOv10 | [2609.14560v1](https://arxiv.org/abs/2609.14560v1) | 质检未通过: 单位为空或无效 |


## 🔎 观察

- 星上处理与变化问答均强调资源约束，轻量化与按需计算成为遥感AI落地的关键方向。
- 无注意力编码器与工具调用分别代表架构精简和智能体推理两条技术路线，值得持续关注。

---

Powered by OpenClaw🦞

---

# [20260912](./202609/20260912.md)
## 📌 今日概况

今日共检索候选论文 2 篇；关键词+LLM 智能匹配遥感交叉论文 2 篇；最终纳入日报 2 篇。

今日遥感AI研究聚焦于基础模型适配与高效检测架构两个方向。一方面，针对多模态基础模型在遥感领域的迁移，研究者提出基于域感知松弛正交子空间的参数高效微调方法，试图在低秩适配框架下缓解域差异。另一方面，面向无人机航拍等场景，有工作将状态空间建模与高频增强结合到YOLO12中，以提升小目标检测效率。整体趋势显示，遥感AI正从通用大模型直接迁移转向领域定制化适配，同时轻量化与频域信息利用成为检测任务的重要优化手段。

## ✨ 今日亮点

- 多模态基础模型遥感适配引入域感知松弛正交子空间，提升参数高效微调效果。
- YOLO12-MambaScan融合高频增强与状态空间建模，面向无人机小目标检测。
- 两项工作分别代表基础模型领域适配与检测架构轻量化两条技术路线。

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260912] Multimodal Foundation Models Adaptation based on Domain-Aware Relaxed Orthogonal Subspace for Remote Sensing | Luo Han, Yang Ruoyu, Liu Yinhe, Zhong Yanfei | State Key Laboratory of Information Engineering in Surveying, Mapping and Remote Sensing, Wuhan University, Wuhan, China ( | 提出域感知松弛正交子空间方法，实现遥感多模态基础模型的参数高效领域适配。 | [#1284](https://github.com/thinson/RS-PaperClaw/issues/1284) |
| [20260912] YOLO12-MambaScan: An Efficient Object Detector with High-Frequency Enhancement and State-Space Modeling | Wang Hao | BDNRC | 设计YOLO12-MambaScan检测器，结合高频增强与状态空间建模提升无人机小目标检测。 | [#1285](https://github.com/thinson/RS-PaperClaw/issues/1285) |

## 🔎 观察

- 遥感基础模型适配正从简单微调转向结构化子空间约束，以平衡泛化与域特化。
- 状态空间模型与频域增强结合，反映检测任务对计算效率与细粒度信息保留的双重需求。

---

Powered by OpenClaw🦞

---
