# Daily Reports

最近三天日报（最新在前）：

# [20260426](./202604/20260426.md)
## 📌 今日概况

今日共检索候选论文 7 篇；关键词+LLM 智能匹配遥感交叉论文 3 篇；最终纳入日报 3 篇。

今日研究聚焦深度学习在遥感图像处理中的创新应用，涵盖无监督时序制图、高光谱分类及SAR图像去噪三大方向。中山大学团队提出无需标注的油棕时序制图方法，汕头大学等探索CNN-Transformer融合架构，印度理工学院则回归数学基础比较PDE去噪模型。

## ✨ 今日亮点

- 无标注时序制图突破：利用历史噪声地图实现2020-2024年马印油棕榈动态监测
- CNN-Transformer协同：池化注意力融合机制提升高光谱图像分类精度
- PDE去噪理论对比：二阶与四阶偏微分方程在SAR及医学影像中的加权耦合研究

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260426] From Noisy Historical Maps to Time-Series Oil Palm Mapping Without Annotation in Malaysia and Indonesia (2020-2024) | Kuapanich Nuttaset, Zheng Juepeng, Shi Bohan, Liu Jiaying, Jiang Jiayin, Huang Jiatao, Tan Shenghan, Li Qingmei, Fu Haohuan | School of Artificial Intelligence, Sun Yat-Sen University；National Supercomputing Center in Shenzhen；Khoury College of Computer Sciences, Northeastern University；Tsinghua Shenzhen International Graduate School, Tsinghua University | 提出基于噪声历史地图的无监督学习方法，实现2020-2024年马来西亚和印度尼西亚油棕榈时序制图，无需人工标注。 | [#412](https://github.com/thinson/RS-PaperClaw/issues/412) |
| [20260426] A Synergistic CNN-Transformer Network with Pooling Attention Fusion for Hyperspectral Image Classification | Chen Peng, He Wenxuan, Qian Feng, Shi Guangyao, Yan Jingwen | College of Engineering, Shantou University；School of Electronic Information and Communications, Huazhong University of Science and Technology；Changchun Institute of Optics, Fine Mechanics and Physics, Chinese Academy of Sciences；School of Computer Science and Technology, Chongqing University of Posts and Telecommunications；School of Intelligent Manufacturing and Electrical Engineering, Guangzhou Institute of Science and Technology | 设计CNN-Transformer协同网络，通过池化注意力融合机制联合提取高光谱图像空谱特征以提升分类性能。 | [#413](https://github.com/thinson/RS-PaperClaw/issues/413) |
| [20260426] Comparative Study of Weighted and Coupled Second- and Fourth-Order PDEs for Image Despeckling in Grayscale, Color, SAR, and Ultrasound | Kumar Manish, Rajendra K. Ray | School of Mathematical and Statistical Sciences, Indian Institute of Technology Mandi | 系统比较加权与耦合的二阶、四阶偏微分方程模型，评估其在灰度、彩色、SAR及超声图像去噪中的效果。 | [#414](https://github.com/thinson/RS-PaperClaw/issues/414) |

## 🔎 观察

- 弱监督与无监督学习成为遥感大样本标注瓶颈的重要突破口，历史数据再利用价值凸显。
- Transformer架构持续向高光谱等细粒度任务渗透，但CNN局部特征提取仍具不可替代性。

---

Powered by OpenClaw🦞

---

# [20260425](./202604/20260425.md)
## 📌 今日概况

今日共检索候选论文 5 篇；关键词+LLM 智能匹配遥感交叉论文 4 篇；最终纳入日报 3 篇。

今日遥感AI研究聚焦三大方向：边缘计算驱动的农业精准管理、语义增强的时序变化理解，以及基础模型支撑的社会经济监测。研究呈现从通用模型向垂直场景深化、从云端向边缘部署延伸的趋势，体现遥感AI在可持续发展目标中的工具化价值。

## ✨ 今日亮点

- YOLO轻量化部署实现无人机端侧杂草实时检测，推动精准农业落地
- 语义锚定双粒度消歧机制提升遥感变化描述准确性
- 卫星基础模型自监督预训练赋能大范围财富指数预测

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260425] Resource-Constrained UAV-Based Weed Detection for Site-Specific Management on Edge Devices | Wang Linyuan, Yao Haibo, Tseng Te-Ming, Betitame Kelvin, Sun Xin, Huang Hanbo, Chen Dong | Department of Agricultural and Biological Engineering, Mississippi State University；USDA-ARS, Genetics and Sustainable Agriculture Research Unit；Department of Plant and Soil Sciences, Mississippi State University；Department of Agricultural and Biosystems Engineering, North Dakota State University；NDSU Peltier Institute for the Advancement of Agricultural Technology, North Dakota State University | 针对无人机边缘设备资源受限场景，优化YOLO模型实现田间杂草实时检测，支持变量施药等精准农业作业。 | [#408](https://github.com/thinson/RS-PaperClaw/issues/408) |
| [20260425] STAND: Semantic Anchoring Constraint with Dual-Granularity Disambiguation for Remote Sensing Image Change Captioning | Gong Yanpei, Zhang Beichen, Wang Hao, Qi Zhaobo, Liu Xinyan, Xu Yuanrong, Gao Ruiyang, Zhang Weigang | Harbin Institute of Technology | 提出语义锚定约束与双粒度消歧网络，解决遥感变化描述中语义模糊问题，提升时序变化 captioning 精度。 | [#409](https://github.com/thinson/RS-PaperClaw/issues/409) |
| [20260425] A satellite foundation model for improved wealth monitoring | Zheng Zhuo, Higuera-Mendieta Iván, Lee Richard, Newhouse David, Kilic Talip, Ermon Stefano, Burke Marshall, David B. Lobell | Department of Computer Science, Stanford University；Department of Earth System Science, Stanford University；Center on Food Security and the Environment, Stanford University；Development Economics Data Group, World Bank Group；Department of Environmental Social Science, Stanford University | 构建卫星影像基础模型，通过自监督预训练提取多尺度特征，实现无需人工标注的全球财富监测与贫困制图。 | [#410](https://github.com/thinson/RS-PaperClaw/issues/410) |

## 🔎 观察

- 农业遥感正从云端分析向端侧智能演进，边缘计算与模型压缩成为关键使能技术
- 基础模型在经济社会遥感监测中展现潜力，但跨域泛化与伦理隐私问题仍需关注

---

Powered by OpenClaw🦞

---

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
