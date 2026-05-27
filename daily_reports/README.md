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

今日共检索候选论文 15 篇；关键词+LLM 智能匹配遥感交叉论文 7 篇；最终纳入日报 7 篇。

今日遥感AI研究聚焦于多模态融合与3D空间理解，涵盖MLLM高度线索利用、超广域分割、无人机视角泛化、低空城市数据融合、建筑多模态检测、高光谱3D成像及红外单像素成像等方向，体现了从2D到3D、从单源到多源、从可见光到红外宽谱段的技术演进趋势。

## ✨ 今日亮点

- 多模态大模型利用高度线索消除遥感场景2D歧义
- 超广域图像分割提出尺度-截锥体表示新方法
- 无人机动作识别实现跨视角泛化能力突破

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260525] VertiCue-Bench: Diagnosing Whether MLLMs Use Height Cues to Resolve 2D Ambiguity in Remote Sensing Natural Scenes | Huang Jing, Wang Duanchu, Yang Junjie, Cheng Zihang, Li Cheng, Cui Lin, Wu Zhouyi, Wang Di | Xi'an Jiaotong University；Xidian University；University of Chinese Academy of Sciences | 提出VertiCue-Bench基准，评估MLLMs利用高度线索消除遥感2D歧义的能力。 | [#614](https://github.com/thinson/RS-PaperClaw/issues/614) |
| [20260525] SFR-Net: Learning Scale-Frustum Representations for Ultra-Wide Area Remote Sensing Image Segmentation | Zhong Chuyu, Chen Keyan, Yang Qinzhe, Chen Bowen, Zou Zhengxia, Shi Zhenwei | the Department of Aerospace Intelligent Science and Technology, School of Astronautics, Beihang University, Beijing , China；the Key Laboratory of Spacecraft Design Optimization and Dynamic Simulation Technologies, Ministry of Education, Beihang University, Beijing；Shen Yuan Honors College, Beihang University, Beijing；the College of Computing and Data Science, Nanyang Technological University, Singapore | SFR-Net学习尺度-截锥体表示，实现超广域遥感图像高效分割。 | [#615](https://github.com/thinson/RS-PaperClaw/issues/615) |
| [20260525] UAV-OVO: Out-of-Viewpoint Generalization in UAV Action Recognition | Xia Yu, Zhang Zhengbo, Zhang Shuaihu, Tu Zhigang | Wuhan University；Singapore University of Technology and Design | UAV-OVO方法提升无人机动作识别在未见视角下的泛化性能。 | [#617](https://github.com/thinson/RS-PaperClaw/issues/617) |
| [20260525] Location Prior Generation via Multi-Source Urban Data Fusion for Low-Altitude Air Mobility | Xie Xiang, Liu Xiaonan | the School of Natural and Computing Science, University of Aberdeen, Aberdeen, U.K | 融合多源城市数据生成位置先验，支持低空空中交通规划。 | [#618](https://github.com/thinson/RS-PaperClaw/issues/618) |
| [20260525] Multi-Modal Building Inspection via Perceiver IO Fusion of Satellite and Street-Level Imagery | Sombekke Niels, Rob G. J. Wijnhoven, Martin R. Oswald | University of Amsterdam (UvA), Amsterdam, The Netherlands | 利用Perceiver IO融合卫星与街景图像，实现多模态建筑检测。 | [#627](https://github.com/thinson/RS-PaperClaw/issues/627) |
| [20260525] Broadband Hyperspectral 3D Imaging using Dispersed Structured Light | Shin Suhyun, Moon Yunseong, Maeda Ryota, Lindell David, Kutulacos Kyros, Baek Seung-Hwan | RYOTA MAEDA, University of Hyogo, Japan；DAVID LINDELL, University of Toronto, Canada；KYROS KUTULAKOS, University of Toronto, Canada | 基于色散结构光实现宽带高光谱3D成像，覆盖SWIR波段。 | [#628](https://github.com/thinson/RS-PaperClaw/issues/628) |
| [20260525] Infrared Single-Pixel Hyperspectral Imaging via Spatial-Temporal Multiplexing | Sun Ben, Huang Kun, Zhao Zhibin, Dong Beibei, Fang Jianan, Zeng Heping | State Key Laboratory of Precision Spectroscopy, and Hainan Institute；East China Normal University, Shanghai 200062, China；Chongqing Key Laboratory of Precision Optics, Chongqing Institute；of East China Normal University, Chongqing 401121, China；Collaborative Innovation Center of Extreme Optics；Shanxi University, Taiyuan, Shanxi 030006, China；Shanghai Research Center for Quantum Sciences, Shanghai 201315, China；Chongqing Institute for Brain and Intelligence, Guangyang Bay Laboratory, Chongqing, 400064, China | 时空复用策略实现红外单像素高光谱成像，降低采样成本。 | [#629](https://github.com/thinson/RS-PaperClaw/issues/629) |

## 🔎 观察

- 3D空间理解成为遥感多模态大模型评测与优化的关键方向。
- 超广域与低空场景推动多尺度、多源数据融合技术快速发展。

---

Powered by OpenClaw🦞

---

# [20260524](./202605/20260524.md)
## 📌 今日概况

今日共检索候选论文 4 篇；关键词+LLM 智能匹配遥感交叉论文 2 篇；最终纳入日报 2 篇。

今日遥感AI研究聚焦于无人机通信与地质推理两大方向。前者提出基于能量效率的个性化联邦学习框架，通过梯度调度应对数据异质性；后者则利用参数高效微调技术构建专家级地质推理模型，展示了大型语言模型在遥感地学领域的应用潜力。

## ✨ 今日亮点

- 无人机通信中实现能量高效的个性化联邦学习
- 参数高效微调推动地质推理达到专家水平
- 大型语言模型在遥感地学领域取得新突破

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260524] Personalized Federated Learning by Energy-Efficient UAV Communications | Guo Shiqian, Liu Jianqing, Lorenzo Beatriz | the Department of Electrical and Computer Engineering, University of Massachusetts, Amherst, MA USA | 提出能量高效的个性化联邦学习框架，优化无人机通信中的数据异质性调度。 | [#624](https://github.com/thinson/RS-PaperClaw/issues/624) |
| [20260524] Geo-Expert: Towards Expert-Level Geological Reasoning via Parameter-Efficient Fine-Tuning | Guo Chenyou, Liu Zongqi, Zhang Yizhou, Jiang Zhaorui, Liu Ze | Ocean University of China；Peking University；Monash University | Geo-Expert通过参数高效微调实现专家级地质推理，构建领域专用基准。 | [#626](https://github.com/thinson/RS-PaperClaw/issues/626) |

## 🔎 观察

- 联邦学习与无人机通信结合，正成为解决边缘计算能耗问题的关键路径。
- 大型语言模型微调技术在地学推理中展现潜力，但领域基准仍需完善。

---

Powered by OpenClaw🦞

---
