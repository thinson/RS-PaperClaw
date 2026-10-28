# Daily Reports

最近三天日报（最新在前）：

# [20261027](./202610/20261027.md)
## 📌 今日概况

今日共检索候选论文 10 篇；关键词+LLM 智能匹配遥感交叉论文 6 篇；最终纳入日报 6 篇。

今日研究覆盖遥感图像文本检索、作物分类、知识蒸馏、边缘推理、SAR辐射定标与卫星条件扩散生成。趋势上，高效检索与轻量化部署受关注，如无交互召回与量化边缘推理；农业遥感侧重跨区域泛化与地面-卫星知识迁移；生成式方法开始用于无重建新视角合成。整体体现从模型性能向效率、鲁棒性与实际部署的平衡。

## ✨ 今日亮点

- 无交互召回加文本引导重排，提升遥感图文检索效率。
- 评估AlphaEarth嵌入的作物可分性与跨区域迁移能力。
- 地面到卫星知识蒸馏，应对作物分类时空偏移。

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20261027] Efficient Remote Sensing Image-Text Retrieval via Interaction-Free Recall and Text-Guided Reranking | Chen Xi, Chen Xu, Jia Xiamgyang, Wang Wei, Zhang Xu, Shun Zhenyuan | XI CHEN, School of Computer Science, Wuhan University, China；XU CHEN∗, School of Computer Science, Wuhan University, China；XIANGYANG JIA, School of Computer Science, Wuhan University, China；WEI WANG, Beijing Institute for General Artificial Intelligence (BIGAI), China；XU ZHANG, School of Computer Science, Wuhan University, China；ZHENYUAN SUN, School of Computer Science, Wuhan University, China；Institute for General Artificial Intelligence (BIGAI), Beijing, China; Xu Zhang；Science, Wuhan University, Wuhan, China; Zhenyuan Sun；University, Wuhan, China | 提出无交互召回与文本引导重排的遥感图文检索流程，兼顾效率与精度。 | [#1582](https://github.com/thinson/RS-PaperClaw/issues/1582) |
| [20261027] Evaluating AlphaEarth Embeddings for Crop Classification: Separability, Temporal Dynamics, and Cross-Regional Transferability | Goyal Priyanka, Sar Maitreyee, Mitra Adway, Sinha Manjira | Department of Artificial Intelligence, Indian Institute of Technology Kharagpur, West Bengal, India；Centre for Atmospheric Sciences, Indian Institute of Technology Delhi, India | 系统评估AlphaEarth嵌入在作物分类中的可分性、时序动态与跨区域迁移性。 | [#1583](https://github.com/thinson/RS-PaperClaw/issues/1583) |
| [20261027] Ground-to-Satellite Knowledge Distillation for Crop Classification under Temporal and Geographic Shift | Miranda Miro, Sedona Rocco, Marsocci Valerio, Cavallaro Gabriele, Paris Claudia | Jülich Supercomputing Centre；University of Iceland, Iceland；University of Twente (ITC), the Netherlands | 利用地面照片到卫星时序的知识蒸馏，提升作物分类在时空偏移下的表现。 | [#1584](https://github.com/thinson/RS-PaperClaw/issues/1584) |
| [20261027] Quantized Edge Inference of a Self-Supervised SAR-Optical Encoder on Commodity x86 Hardware | Sanchez-Leon Christian, Chen Dongming | the Software College, Northeastern University, Shenyang, China ( | 在商用x86硬件上量化部署自监督SAR-光学编码器，实现边缘推理。 | [#1585](https://github.com/thinson/RS-PaperClaw/issues/1585) |
| [20261027] Assessing BIOMASS Radiometric Stability using Permanent Scatterers | Manzoni Marco, Salvaterra Francesco, Claudio Maria Prati, Tebaldini Stefano | Politecnico di Milano | 利用永久散射体评估BIOMASS任务P波段SAR的辐射稳定性。 | [#1586](https://github.com/thinson/RS-PaperClaw/issues/1586) |
| [20261027] GroundControl: Satellite-Conditioned Multi-View Diffusion for Reconstruction-Free Novel View Synthesis | Krishnan Akshay, Turkulainen Matias, Wynn Jamie, Qureshi Zawar, Sayed Mohamed, Garcia-Hernando Guillermo, Vicente Sara, Hays James, Firman Michael, Turmukhambetov Daniyar | Georgia Institute of Technology；Aalto University | 提出卫星条件多视角扩散模型，无需重建即可合成新视角。 | [#1587](https://github.com/thinson/RS-PaperClaw/issues/1587) |

## 🔎 观察

- 检索与部署研究强调效率，无交互召回和量化推理反映落地导向。
- 农业遥感关注跨区域与时空偏移，评估与蒸馏成为提升泛化的手段。

---

Powered by OpenClaw🦞

<!-- rs-pipeline: {"date": "20261027", "source": "oai", "checked_at": "2026-10-28T10:48:50+00:00", "source_complete": true, "candidate_count": 10, "paper_count": 6} -->

---

# [20261025](./202610/20261025.md)
## 📌 今日概况

今日共检索候选论文 5 篇；关键词+LLM 智能匹配遥感交叉论文 1 篇；最终纳入日报 1 篇。

今日仅一篇论文，聚焦多用户对地观测卫星调度的加权公平性问题。该研究将公平性从传统单目标优化中独立出来，引入加权机制以平衡不同用户需求，反映了卫星资源分配从效率优先向兼顾公平的精细化方向演进。由于样本单一，趋势判断受限，但可见调度研究正关注多利益相关方场景下的分配正义。

## ✨ 今日亮点

- 提出多用户对地观测卫星调度中的加权公平性建模方法
- 将公平性作为独立优化目标，区别于传统效率导向调度
- 机构合作体现法国在卫星调度与多智能体公平分配领域的积累

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20261025] Weighted Fairness in Multi-User Earth Observation Satellite Scheduling | Lucet Maxime, Benabbou Nawal, Beynier Aurélie, Maudet Nicolas, Picard Gauthier | LIP6, CNRS, Sorbonne Université, Paris, France；ONERA, DTIS, Université de Toulouse, Toulouse, France | 针对多用户对地观测卫星调度，提出加权公平性框架，在资源分配中兼顾不同用户权重与公平性。 | [#1572](https://github.com/thinson/RS-PaperClaw/issues/1572) |

## 🔎 观察

- 该研究将公平性引入卫星调度，暗示多用户共享星座场景下分配正义正成为独立研究维度。
- 仅单篇论文且偏理论建模，尚难判断加权公平性在真实星座规模下的计算可行性与收益。

---

Powered by OpenClaw🦞

<!-- rs-pipeline: {"date": "20261025", "source": "oai", "checked_at": "2026-10-27T10:04:17+00:00", "source_complete": true, "candidate_count": 5, "paper_count": 1} -->

---

# [20261024](./202610/20261024.md)
## 📌 今日概况

今日共检索候选论文 5 篇；关键词+LLM 智能匹配遥感交叉论文 3 篇；最终纳入日报 3 篇。

今日研究趋势呈现多模态与高效计算并进。少样本遥感场景分类关注方向不变性，通过组件池化与非负分解提升泛化；指代分割引入跨尺度稀疏注意力，强化视觉语言对齐与多尺度特征融合；SAR成像则聚焦开源实现，在CPU、GPU与TPU上追求高吞吐高保真。整体体现遥感AI向轻量化、跨模态与硬件适配方向发展。

## ✨ 今日亮点

- 少样本场景分类利用组件池化实现方向不变性
- 指代分割采用跨尺度稀疏注意力增强多尺度融合
- SAR成像开源实现覆盖CPU、GPU与TPU加速

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20261024] Component Pooling Trained Across Orientations for Few-Shot Remote Sensing Scene Classification | Yan Bingchen, Guo Wenheng, Zhou Yuye | School of Computer Science and Information Security；Guilin University of Electronic Technology, Guilin, 541004, China；School of Information Engineering；Institute of Disaster Prevention, Langfang, 065201, China；School of Computing & Technology；Asia Pacific University of Technology & Innovation, Kuala Lumpur, 57000, Malaysia | 提出跨方向训练的组件池化方法，结合非负分解提升少样本遥感场景分类性能。 | [#1568](https://github.com/thinson/RS-PaperClaw/issues/1568) |
| [20261024] Cross-Scale Sparse Attention for Referring Segmentation in Remote Sensing | Li Yuxi, Si Lu, Liao Xia, Shen Yidong, Wei Zheng, Zhang Jun, Yuan Xin | aWestlake Institute for Advanced Study, Hangzhou, Zhejiang, China；bSchool of Engineering, Westlake University, Hangzhou, Zhejiang, China；cBeijing National Research Center for Information Science and Technology (BNRist), Tsinghua；University, Beijing, China；dSchool of Computer Science, Beijing University of Posts and Telecommunications, Beijing, China；eDepartment of Automation, Tsinghua University, Beijing, China | 设计跨尺度稀疏注意力机制，用于遥感指代分割中的视觉语言对齐与多尺度特征融合。 | [#1569](https://github.com/thinson/RS-PaperClaw/issues/1569) |
| [20261024] FastSAR: High-Throughput, High-Fidelity Open-Source SAR Image Formation on CPUs, GPUs and TPUs | Singerman Paul, Braun Tom | Penn State University | 发布FastSAR开源SAR成像框架，在CPU、GPU和TPU上实现高吞吐高保真处理。 | [#1570](https://github.com/thinson/RS-PaperClaw/issues/1570) |

## 🔎 观察

- 少样本分类与指代分割均强调多尺度与方向适应性，反映遥感视觉任务对几何变换的持续关注。
- SAR成像开源框架适配多种硬件，表明遥感数据处理正重视可复现性与计算效率的平衡。

---

Powered by OpenClaw🦞

<!-- rs-pipeline: {"date": "20261024", "source": "oai", "checked_at": "2026-10-27T10:00:58+00:00", "source_complete": true, "candidate_count": 5, "paper_count": 3} -->

---
