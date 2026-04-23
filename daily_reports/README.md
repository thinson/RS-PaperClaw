# Daily Reports

最近三天日报（最新在前）：

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

# [20260421](./202604/20260421.md)
## 📌 今日概况

今日共检索候选论文 15 篇；关键词+LLM 智能匹配遥感交叉论文 8 篇；最终纳入日报 8 篇。

今日遥感AI研究呈现多模态融合与高效推理两大主线。高分辨率影像处理持续深化，涵盖语义分割、小目标检测与超分辨率重建；SAR任务规划与图像合成技术取得进展；农业遥感与光谱成像应用拓展。扩散模型、注意力机制与深度学习优化方法成为主要技术支撑。

## ✨ 今日亮点

- 无训练扩散模型实现卫星图像协调合成，降低域适应成本
- 结构-语义解耦调制提升地理空间基础模型高分辨率制图能力
- 自适应切片辅助超推理优化高分辨率影像小目标检测效率

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260421] Structure-Semantic Decoupled Modulation of Global Geospatial Embeddings for High-Resolution Remote Sensing Mapping | Lyu Jienan, Yang Miao, Cai Jinchen, Hu Yiwen, Lu Guanyi, Qiu Junhao, Dong Runmin | Sun Yat-Sen University；Tsinghua University | 提出结构-语义解耦调制方法，优化全球地理空间嵌入在高分辨率遥感制图中的应用。 | [#386](https://github.com/thinson/RS-PaperClaw/issues/386) |
| [20260421] An effective window framework for closed-Loop regional SAR reconnaissance with hybrid direct-relay downlink scheduling | Li Linhong, Feng Qi, Li Kebo, Liang Yangang | College of Aerospace Science and Engineering, National University of Defense Technology；State Key Laboratory of Space System Operation and Control | 构建闭环区域SAR侦察窗口框架，实现混合直传中继下行链路调度与成像质量协同优化。 | [#387](https://github.com/thinson/RS-PaperClaw/issues/387) |
| [20260421] Optimal Multispectral Imaging using RGB Cameras | Matulić Tomislav, Škrabo Ivan, Babić Dubravko, Seršić Damir | Faculty of Electrical Engineering and Computing University of Zagreb | 基于帧理论与条件数优化，开发RGB相机最优多光谱成像方法，实现光谱波段选择。 | [#388](https://github.com/thinson/RS-PaperClaw/issues/388) |
| [20260421] HarmoniDiff-RS: Training-Free Diffusion Harmonization for Satellite Image Composition | Zhuang Xiaoqi, Jefersson A. Dos Santos, Han Jungong | The University of Sheffield；Tsinghua University | 提出HarmoniDiff-RS无训练扩散协调方法，用于卫星图像合成中的域适应与图像协调。 | [#389](https://github.com/thinson/RS-PaperClaw/issues/389) |
| [20260421] Adaptive Slicing-Assisted Hyper Inference for Enhanced Small Object Detection in High-Resolution Imagery | Moretti Francesco, Jin Yi, Mario Guiqin | College of Educational Science and Technology, Polytechnic University of Turin | 设计自适应切片辅助超推理机制，提升高分辨率航空影像小目标检测性能。 | [#390](https://github.com/thinson/RS-PaperClaw/issues/390) |
| [20260421] Attention-based Multi-modal Deep Learning Model of Spatio-temporal Crop Yield Prediction with Satellite, Soil and Climate Data | Gopal Krishna Shyam, Chandrakar Ila | Presidency University；University of Europe for Applied Sciences | 构建注意力驱动多模态深度学习模型，融合卫星、土壤与气候数据实现时空作物产量预测。 | [#391](https://github.com/thinson/RS-PaperClaw/issues/391) |
| [20260421] DUSG-Tomo-Net: A Deep Unfolded Neural Network for Super-Resolving Gridless Spaceborne SAR Tomography via Learned Toeplitz-Structured Covariance Representation | Qian Kun, Xia Zhuge, Ma Qian, Zhang Qi, Liu Weijian, He Xiufeng | Wuhan Electronic Information Institute；School of Earth Sciences and Engineering, Hohai University；School of Medical Information Engineering, Guangzhou University of Chinese Medicine；Chair of Data Science in Earth Observation, Technical University of Munich | 开发深度展开神经网络DUSG-Tomo-Net，通过学习Toeplitz结构协方差表示实现无网格星载SAR层析超分辨率。 | [#392](https://github.com/thinson/RS-PaperClaw/issues/392) |
| [20260421] ExplainS2A: Explainable Spectral-Spatial Duality Model for Fast Transforming Sentinel-2 Image to AVIRIS-Level Hyperspectral Image | Lin Chia-Hsiang, Leng Zi-Chao | IEEE | 提出可解释光谱-空间对偶模型ExplainS2A，实现Sentinel-2多光谱向AVIRIS级高光谱图像快速转换。 | [#393](https://github.com/thinson/RS-PaperClaw/issues/393) |

## 🔎 观察

- 高分辨率遥感处理呈现'切片-推理'精细化趋势，自适应策略成为平衡精度与效率的关键路径
- 扩散模型在遥感域适应中向无训练方向发展，或推动实时卫星图像合成应用落地

---

Powered by OpenClaw🦞

---

# [20260420](./202604/20260420.md)
## 📌 今日概况

今日共检索候选论文 11 篇；关键词+LLM 智能匹配遥感交叉论文 4 篇；最终纳入日报 4 篇。

今日遥感AI研究聚焦多模态大模型与零样本学习两大方向。视觉语言模型在变化检测问答任务中持续优化，扩散模型与SAM基础模型分别推动零样本目标定位与SAR舰船分割。高光谱超分辨率引入高斯溅射新范式，显示生成式技术向遥感各任务渗透的趋势。

## ✨ 今日亮点

- 结构化多模态Qwen模型革新遥感变化VQA任务，LoRA微调提升效率
- DiffuSAM首创扩散引导零样本目标定位，突破遥感图像分割泛化瓶颈
- SAM基础模型经提示工程适配SAR舰船实例分割，实现零样本迁移

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260420] Revisiting Change VQA in Remote Sensing with Structured and Native Multimodal Qwen Models | Bazi Yakoub, Mohamad M. Al Rahhal, Zuair Mansour, Mohamed Faroun | King Saud University；Saudi Data and Artificial Intelligence Authority | 基于Qwen多模态大模型与LoRA微调，构建结构化遥感变化检测视觉问答框架，提升复杂场景推理能力。 | [#380](https://github.com/thinson/RS-PaperClaw/issues/380) |
| [20260420] DiffuSAM: Diffusion Guided Zero-Shot Object Grounding for Remote Sensing Imagery | Sethi Geet, Shah Panav, Gandhe Ashutosh, Soumitra Darshan Nayak | Indian Institute of Technology Bombay | 提出DiffuSAM架构，以扩散模型引导SAM实现遥感图像零样本目标定位，无需训练数据即可分割新类别。 | [#381](https://github.com/thinson/RS-PaperClaw/issues/381) |
| [20260420] Prompting Foundation Models for Zero-Shot Ship Instance Segmentation in SAR Imagery | Mansour Islam, Sica Francescopaolo, Schmitt Michael | Department of Aerospace Engineering, University of the Bundeswehr Munich | 通过提示工程将SAM适配至SAR图像，实现零样本舰船实例分割，验证基础模型在雷达遥感中的迁移潜力。 | [#382](https://github.com/thinson/RS-PaperClaw/issues/382) |
| [20260421] Voronoi-guided Bilateral 2D Gaussian Splatting for Arbitrary-Scale Hyperspectral Image Super-Resolution | Zhang Jie, You Jinkun, Chen Shi, Zhou Yicong | University of Macau | 结合Voronoi图与双向2D高斯溅射，实现任意尺度高光谱图像超分辨率，突破固定放大倍数限制。 | [#383](https://github.com/thinson/RS-PaperClaw/issues/383) |

## 🔎 观察

- 零样本学习成为遥感热点，DiffuSAM与SAM提示工程两条技术路线并行，降低对新领域标注数据的依赖。
- 生成式技术扩散明显，扩散模型与高斯溅射分别从判别与生成角度重塑遥感任务，多模态大模型成为基础设施。

---

Powered by OpenClaw🦞

---
