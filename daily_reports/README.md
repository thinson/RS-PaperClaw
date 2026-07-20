# Daily Reports

最近三天日报（最新在前）：

# [20260717](./202607/20260717.md)
## 📌 今日概况

今日共检索候选论文 9 篇；关键词+LLM 智能匹配遥感交叉论文 7 篇；最终纳入日报 6 篇。

今日遥感研究呈现三大热点：一是多模态大语言模型（MLLMs）在无人机时空推理与遥感长时序理解中的基准构建，推动模型认知能力评估；二是高光谱与多光谱数据在工业电解槽分割及地物分类中的深度学习融合方法创新；三是结合基础模型与可解释性进行大陆尺度洪灾损失预测，体现了遥感AI向精细化、可解释化发展的趋势。

## ✨ 今日亮点

- MLLMs无人机时空推理双认知基准发布
- 高光谱与RGB多模态融合用于电解槽分割
- 大陆尺度每日洪灾损失预测模型DELUGE

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260717] Knowing the Self, Understanding the World: A Dual-Cognition Benchmark for UAV Spatio-temporal Reasoning with MLLMs | Liu Like, Xu Zhengzheng, He Haitao, Li Hongzhe, Zhang Shuchang, Shao Dian | Northwestern Polytechnical University University；University Xi’an, Shaanxi, China Xi’an, Shaanxi, China；China University of Petroleum Northwestern Polytechnical；Qingdao, Shandong, China University Northwestern Polytechnical；Xi’an, Shaanxi, China University | 提出双认知基准，评估MLLMs在无人机时空推理中的自我状态与场景理解能力。 | [#918](https://github.com/thinson/RS-PaperClaw/issues/918) |
| [20260717] Multi-Modal Semantic Segmentation of Electrolyzer Components for Sustainable Hydrogen Technologies: A Dual-Branch Deep Learning Approach | Karim Wasimul, Nur Mohammad Fahad, Abdul Hasib Siddique, Md Rafiqul Islam, Mehdizadeh-Rad Hooman, Karim Asif, Azam Sami | Applied Artificial Intelligence and INtelligent Systems (AAIINS) Laboratory, Dhaka 1217, Bangladesh；Department of Computer Science and Engineering, University of Scholars；School of Engineering and Energy, Murdoch University, Murdoch, WA 6150, Australia；Faculty of Science and Technology, Charles Darwin University, Casuarina, NT 0909, Australia | 采用双分支深度学习融合高光谱与RGB图像，实现电解槽组件语义分割。 | [#919](https://github.com/thinson/RS-PaperClaw/issues/919) |
| [20260717] DELUGE: Towards Continental-Scale Daily Pluvial Flood Damage Prediction via Interpretable Conditioning on Foundation Model Embeddings | Kawakami Yuya, Cayan Daniel, Liu Dongyu, Ma Kwan-Liu, Corringham Tom | University of California, Davis Scripps Institution of Oceanography University of California, Davis；Davis, California, USA University of California, San Diego Davis, California, USA；University of California, Davis Scripps Institution of Oceanography；Davis, California, USA University of California, San Diego | DELUGE模型利用基础模型嵌入实现大陆尺度每日暴雨洪灾损失可解释预测。 | [#920](https://github.com/thinson/RS-PaperClaw/issues/920) |
| [20260717] GeoChrono: Benchmarking and Rethinking Long-Term Temporal Understanding in Remote Sensing | Li Yujie, Pan Jiancheng, Wei Zhiwei, Wang Jiuniu, Peng Mugen, Xu Wenjia | Beijing University of Posts and Telecommunications Haidian Beijing China；Tsinghua University Haidian Beijing China；Hunan Normal University Changsha Hunan China；City University of Hong Kong Hong Kong China | GeoChrono基准重新审视遥感MLLMs在长期时序理解上的能力与局限。 | [#921](https://github.com/thinson/RS-PaperClaw/issues/921) |
| [20260717] BCG-Former: Toward Pareto-Efficient Hyperspectral Image Classification via Band-Contextual Gating | Sharma Gaurav, Lee Eungjoo | College of Information Science, University of Arizona, Tucson, AZ, USA；Department of Electrical and Computer Engineering, University of Arizona, Tucson, AZ, USA ( | BCG-Former通过波段上下文门控实现帕累托高效的高光谱图像分类。 | [#922](https://github.com/thinson/RS-PaperClaw/issues/922) |
| [20260717] MSTF-Net: A UAV-Oriented Multi-Spectral Video Segmentation Method via Modality-Robust, Scale-Adaptive, and Consistent Fusion | Wang Chenwei, Wang Zhida, Li Zelin, Ozden-Yenigun Elif, Liu Houde | Tsinghua Shenzhen International Graduate School, Tsinghua University, Shenzhen, China | MSTF-Net提出模态鲁棒、尺度自适应的多光谱无人机视频分割方法。 | [#923](https://github.com/thinson/RS-PaperClaw/issues/923) |

## ⚠️ 未纳入日报的匹配论文

以下论文通过关键词/LLM 筛选，但在处理过程中失败未纳入日报。点击 arXiv 链接可查看原文。

| 标题 | arXiv | 失败原因 |
|------|-------|----------|
| More with Less: a Large Scale Remote Sensing VLM with a Simple Recipe | [2607.15942v1](https://arxiv.org/abs/2607.15942v1) | 质检未通过: 单位为空或无效 |


## 🔎 观察

- 多模态大模型在遥感时序推理中的基准构建成为当前评估能力的关键手段。
- 高光谱与多光谱数据的轻量化融合方法正从地物分类向工业应用拓展。

---

Powered by OpenClaw🦞

---

# [20260716](./202607/20260716.md)
## 📌 今日概况

今日共检索候选论文 9 篇；关键词+LLM 智能匹配遥感交叉论文 5 篇；最终纳入日报 5 篇。

今日遥感AI研究聚焦于无人机（UAV）感知与跟踪、高光谱图像分类及可解释性分析。多篇工作引入物理引导、生成学习或视觉-语言-动作模型，提升动态环境下的感知鲁棒性。此外，针对SAR图像洪水检测的xAI方法比较研究也受到关注，体现了模型透明性与物理先验融合的趋势。

## ✨ 今日亮点

- 物理引导图扩散网络提升高光谱分类精度
- 视觉-语言-动作模型增强无人机空间感知
- 事件相机与频域跟踪实现实时空对空追踪

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260716] DAPGNet: Dynamic Adaptive Physics-Guided Graph Diffusion Network for Hyperspectral Image Classification | Wang Pengkun, Cao Weijia, Wang Ning, Yang Xiaofei | the National Engineering Laboratory for Satellite Remote Sensing Applications, Aerospace Information Research Institute, Chinese Academy of Sciences, Beijing, China；University of Chinese Academy of Sciences, Beijing, China (；the Aerospace Information Research Institute, Chinese Academy of Sciences, Beijing, China (；the National Engineering Laboratory for Satellite Remote Sensing Applications, Aerospace Information Research Institute, Chinese Academy of Sciences, Beijing, China (；Guangzhou University, Guangzhou, China ( | 提出动态自适应物理引导图扩散网络，用于高光谱图像分类。 | [#912](https://github.com/thinson/RS-PaperClaw/issues/912) |
| [20260716] CosFly-VLA: A Spatially Aware Vision-Language-Action Model for UAV Tracking | Ren Ruilong, Cheng Songsheng, Zhou Yunpeng, Chen Hanxuan, Wang Xiangyue, Zeng Tianle, Yuan Shuai, Li Binbo, Guo Hanzhong, Pei Ji, Zhang Da, Wang Kangli | Northeast Normal University；Southern University of Science and Technology；Peking University；University of Hong Kong | CosFly-VLA模型融合空间感知与视觉-语言-动作，用于无人机跟踪。 | [#913](https://github.com/thinson/RS-PaperClaw/issues/913) |
| [20260716] Conditional Generative Learning Enabled Wireless UAV Sensing and Tracking via Point Cloud Imaging | Dai Xinhong, Gao Yuan, Jiang Hao, Yuan Xiaojun, Wang Xin | Key Laboratory for Information Science of Electromagnetic Waves (MoE), College of Future Information Technology, Fudan University, Shanghai, China. (；the National Key Laboratory of Wireless Communications, the University of Electronic Science and Technology of China, Chengdu, China ( | 条件生成学习结合点云成像实现无线无人机感知与跟踪。 | [#914](https://github.com/thinson/RS-PaperClaw/issues/914) |
| [20260716] On the Disagreement in Perturbation-based xAI -- Benchmarking Perturbation Choices for Flood Detection from SAR Images | Schlegel Anastasia, Hänsch Ronny | a Microwaves and Radar Institute, German Aerospace Center (DLR), Weßling, 82234, Germany；b Chair of Remote Sensing Technology, Department of Aerospace and Geodesy, Technical University of Munich, Munich, 80333, Germany；In response to this need for transparency, research on ex- | 基准测试扰动选择对SAR图像洪水检测中xAI方法的影响。 | [#915](https://github.com/thinson/RS-PaperClaw/issues/915) |
| [20260716] AE-UAV: An Air-to-Air Event-Based UAV Tracking Benchmark and a Real-Time Frequency-Domain Tracker | Jiang Zixin, He Bing, Xiong Chaoran, Wang Zhenzhen, Zhao Xin, Pei Ling | Department of Electronic Engineering, Rocket Force University of Engineering, Xi’an, China (；Shanghai Key Laboratory of Navigation and Location Based Services, Shanghai Jiao Tong University, Shanghai, China (；State Key Laboratory of Submarine Geoscience, School of Automation and Intelligent Sensing, Shanghai Jiao Tong University, Shanghai, China | 发布空对空事件相机无人机跟踪基准及实时频域跟踪器。 | [#916](https://github.com/thinson/RS-PaperClaw/issues/916) |

## 🔎 观察

- 无人机感知领域正从单一视觉向多模态融合（语言、事件、电磁）演进。
- 物理先验与可解释性方法在遥感任务中应用增多，提升模型可信度。

---

Powered by OpenClaw🦞

---

# [20260715](./202607/20260715.md)
## 📌 今日概况

今日共检索候选论文 13 篇；关键词+LLM 智能匹配遥感交叉论文 5 篇；最终纳入日报 4 篇。

今日遥感AI研究聚焦于无人机自主导航与多模态感知、云感知地球观测及北极海冰监测。AeroMap3D提出基于视觉-几何-语义地图先验的单目6-DoF定位方法，解决GNSS拒止环境问题；M3F-UAV构建低空无线传感缺失模态多模态基础模型；RoughNet利用扩散超分辨率技术绘制海冰粗糙度图，提升气候监测能力。

## ✨ 今日亮点

- 无人机单目定位结合地图先验，突破GNSS拒止限制
- 低空无线传感缺失模态融合基础模型
- 扩散模型超分辨率用于北极海冰粗糙度制图

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260715] AeroMap3D: Anchoring Monocular UAV 6-DoF Localization to Visual-Geometric-Semantic Map Priors | Deng Zhiyun, Sentis Luis | University of Texas at Austin | AeroMap3D利用视觉-几何-语义地图先验实现无人机单目6-DoF定位 | [#899](https://github.com/thinson/RS-PaperClaw/issues/899) |
| [20260715] M3F-UAV: A Missing-Modality Multimodal Foundation Model for Low-Altitude Wireless Sensing | Gao Pengxuan, Ying Kai, Wu Botao, Mo Jianhua, Wen Qingsong | School of Electronic Information and Electrical Engineering, Shanghai Jiao Tong University, Shanghai, China ( | M3F-UAV提出缺失模态多模态基础模型用于低空无线传感 | [#900](https://github.com/thinson/RS-PaperClaw/issues/900) |
| [20260715] From Surface Forecasting to Observability Forecasting: A Latent World Model for Cloud-Aware EO Monitoring | Albughdadi Mohanad | European Centre for Medium-Range Weather Forecasts | LeWorldModel实现从地表到可观测性的云感知预报 | [#901](https://github.com/thinson/RS-PaperClaw/issues/901) |
| [20260715] RoughNet: Mapping Arctic Sea Ice Roughness Using Diffusion-Based Super-Resolution of Satellite Imagery | Cannon Tessa, Tsamados Michel, Manescu Petru, Newman Thomas, Haas Christian, Helm Veit, Chen Weibin, Scharien Randall | Department of Computer Science, University College London；Department of Earth Sciences, University College London；Alfred Wegener Institute Helmholtz Centre for Polar and；Marine Research, Bremerhaven, Germany；Department of Geography, University of Victoria | RoughNet基于扩散超分辨率卫星影像绘制海冰粗糙度图 | [#902](https://github.com/thinson/RS-PaperClaw/issues/902) |

## ⚠️ 未纳入日报的匹配论文

以下论文通过关键词/LLM 筛选，但在处理过程中失败未纳入日报。点击 arXiv 链接可查看原文。

| 标题 | arXiv | 失败原因 |
|------|-------|----------|
| Minimax Theory of Likelihood-Based Deep Learning for Speckle Regression | [2607.14064v1](https://arxiv.org/abs/2607.14064v1) | 质检未通过: 单位为空或无效 |


## 🔎 观察

- 无人机定位研究正从纯视觉向多模态地图先验融合演进
- 扩散模型在遥感超分辨率应用中展现出对复杂纹理的建模优势

---

Powered by OpenClaw🦞

---
