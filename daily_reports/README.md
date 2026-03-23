# Daily Reports

最近三天日报（最新在前）：

# [20260320](./202603/20260320.md)
## 📌 今日概况

今日共检索候选论文 11 篇；关键词+LLM 智能匹配遥感交叉论文 8 篇；最终纳入日报 8 篇。

今日遥感AI研究聚焦模型轻量化与星载智能两大方向。TinyML与层剪枝技术推动CubeSat等边缘设备部署；多智能体系统与视觉语言模型结合，提升灾害应急响应能力；RWKV线性复杂度架构与物理引导深度学习为变化检测开辟新路径。无人机视觉语言动作基准与夜间跟踪技术同步推进。

## ✨ 今日亮点

- TinyML赋能CubeSat任务，实现星载遥感模型优化部署
- SIMPLER提出相似度引导层剪枝，高效适配遥感基础模型
- 多智能体协同推理架构，支撑星上灾害快速应急响应

## 🗂 今日文章列表

| 标题 | 作者 | 一句话概括 | Issue |
|---|---|---|---|
| [20260320] TinyML Enhances CubeSat Mission Capabilities | Capogrosso Luigi, Magno Michele | Capogrosso等将TinyML与CNN优化技术应用于CubeSat，提升微卫星地球观测任务的边缘智能能力。 | [#156](https://github.com/thinson/RS-PaperClaw/issues/156) |
| [20260320] SIMPLER: Efficient Foundation Model Adaptation via Similarity-Guided Layer Pruning for Earth Observation | Barreiro Víctor, Jakubik Johannes, Argüello Francisco, Dora B. Heras | Barreiro等提出SIMPLER方法，通过相似度引导的层剪枝实现遥感基础模型的高效适配与压缩。 | [#157](https://github.com/thinson/RS-PaperClaw/issues/157) |
| [20260320] Beyond detection: cooperative multi-agent reasoning for rapid onboard EO crisis response | Alejandro D. Mousist, Pedro Delgado de Robles Martín, Raquel Lladró Climent, Julian Cobos Aparicio | Mousist等构建多智能体协同推理框架，结合视觉语言模型实现星上灾害快速检测与响应决策。 | [#158](https://github.com/thinson/RS-PaperClaw/issues/158) |
| [20260320] HUGE-Bench: A Benchmark for High-Level UAV Vision-Language-Action Tasks | Guo Jingyu, Chen Ziye, Li Ziwen, Gao Zhengqing, Huang Jiaxin et al. | Guo等发布HUGE-Bench基准，系统评估无人机高层视觉语言动作任务能力。 | [#159](https://github.com/thinson/RS-PaperClaw/issues/159) |
| [20260320] Offshore oil and gas platform dynamics in the North Sea, Gulf of Mexico, and Persian Gulf: Exploiting the Sentinel-1 archive | Spanier Robin, Hoeser Thorsten, Truckenbrodt John, Bachofer Felix, Kuenzer Claudia | Spanier等利用Sentinel-1档案数据与深度学习，分析北海、墨西哥湾及波斯湾海上油气平台动态变化。 | [#160](https://github.com/thinson/RS-PaperClaw/issues/160) |
| [20260320] Dual Prompt-Driven Feature Encoding for Nighttime UAV Tracking | Wang Yiheng, Fu Changhong, Yao Liangliang, Zuo Haobo, Zhang Zijie | Wang等提出双提示驱动特征编码方法，增强夜间无人机目标跟踪的照明适应能力。 | [#161](https://github.com/thinson/RS-PaperClaw/issues/161) |
| [20260320] Beyond Quadratic: Linear-Time Change Detection with RWKV | Yang Zhenyu, Pei Gensheng, Chen Tao, Yuan Xia, Zhang Haofeng et al. | Yang等将RWKV架构引入遥感变化检测，突破二次复杂度限制实现线性时间推理。 | [#162](https://github.com/thinson/RS-PaperClaw/issues/162) |
| [20260320] PhyUnfold-Net: Advancing Remote Sensing Change Detection with Physics-Guided Deep Unfolding | Lei Zelin, Ren Yaoxing, Chang Jiaming | Lei等开发PhyUnfold-Net，融合物理引导与深度展开网络提升遥感变化检测精度。 | [#163](https://github.com/thinson/RS-PaperClaw/issues/163) |

## 🔎 观察

- 模型压缩技术从传统剪枝量化向任务自适应层选择演进，SIMPLER的相似度引导策略或成为基础模型轻量化新范式
- RWKV线性复杂度架构与物理可解释性方法的涌现，反映遥感领域对高效推理与模型可信性的双重追求

---

Powered by OpenClaw🦞

---

# [20260319](./202603/20260319.md)
## 📌 今日概况

今日共检索候选论文 10 篇；关键词+LLM 智能匹配遥感交叉论文 5 篇；最终纳入日报 5 篇。

今日遥感AI研究呈现多模态融合与智能推理并进的态势。建筑变化检测、视觉语言模型、3D重建等方向持续深化，同时低轨卫星星上计算与数据路由成为新兴热点。研究从地面应用向星上智能延伸，体现空天地一体化发展趋势。

## ✨ 今日亮点

- 多模态建筑变化检测新基准发布，聚焦大规模微小变化识别难题
- TerraScope实现像素级视觉推理，推动遥感图像理解迈向细粒度分析
- SwiftGS将高斯溅射引入卫星影像，实现快速表面三维重建

## 🗂 今日文章列表

| 标题 | 作者 | 一句话概括 | Issue |
|---|---|---|---|
| [20260319] Multi-Modal Building Change Detection for Large-Scale Small Changes: Benchmark and Baseline | Wang Ye, Lu Wei, You Zhihui, Chen Keyan, Liu Tongfei et al. | Wang等构建RGB-NIR多模态建筑变化检测基准数据集，针对大场景微小变化提出基线方法。 | [#147](https://github.com/thinson/RS-PaperClaw/issues/147) |
| [20260319] TerraScope: Pixel-Grounded Visual Reasoning for Earth Observation | Shu Yan, Ren Bin, Xiong Zhitong, Xiao Xiang Zhu, Demir Begüm et al. | Shu等提出TerraScope框架，实现地球观测图像的像素级 grounding 视觉推理与多时空分析。 | [#148](https://github.com/thinson/RS-PaperClaw/issues/148) |
| [20260319] SwiftGS: Episodic Priors for Immediate Satellite Surface Recovery | Fu Rong, Wu Jiekai, Wei Haiyun, Ma Xiaowen, Lin Shiyin et al. | Fu等开发SwiftGS方法，利用元学习 episodic 先验实现卫星影像即时表面高斯溅射重建。 | [#150](https://github.com/thinson/RS-PaperClaw/issues/150) |
| [20260319] iSatCR: Graph-Empowered Joint Onboard Computing and Routing for LEO Data Delivery | Luo Jiangtao, Xu Bingbing, Xia Shaohua, Ran Yongyi | Luo等设计iSatCR系统，基于图神经网络与深度强化学习联合优化低轨卫星星上计算与数据路由。 | [#153](https://github.com/thinson/RS-PaperClaw/issues/153) |
| [20260319] &#34;You&#39;ve got a friend in me&#34;: Co-Designing a Peer Social Robot for Young Newcomers&#39; Language and Cultural Learning | Fernandes Neil, Tang Cheng, Shahbaz Tehniyat, Hauschildt Alex, Davies-Robinson Emily et al. | Fernandes等通过协同设计开发同伴社交机器人，辅助新移民儿童语言文化学习。（非遥感主题） | [#155](https://github.com/thinson/RS-PaperClaw/issues/155) |

## 🔎 观察

- 视觉语言模型向像素级 grounding 演进，遥感图像理解正从场景级分类迈向细粒度空间推理新阶段
- 星上智能成为卫星遥感新赛道，图神经网络与强化学习结合为低轨星座实时数据处理提供新范式

---

Powered by OpenClaw🦞

---

# [20260318](./202603/20260318.md)
## 📌 今日概况

今日共检索候选论文 8 篇；关键词+LLM 智能匹配遥感交叉论文 6 篇；最终纳入日报 6 篇。

今日遥感AI研究呈现多模态融合与低空智能两大主线。视觉-语言模型向遥感开放词汇分割延伸，参数高效学习成为多模态语义分割新方向。同时，无人机检测、机群通信与柔性飞行器控制等低空技术密集涌现，频域特征提取与多智能体系统成为解决复杂场景的关键手段。

## ✨ 今日亮点

- MM-OVSeg实现光学-SAR跨模态开放词汇分割，突破遥感语义类别受限瓶颈
- Local Frequency Bridge网络引入频域桥接机制，应对复杂背景无人机伪装检测
- 多智能体系统首次用于建筑年代队列映射，支撑城市级能源规划决策

## 🗂 今日文章列表

| 标题 | 作者 | 一句话概括 | Issue |
|---|---|---|---|
| [20260318] UAV-CB: A Complex-Background RGB-T Dataset and Local Frequency Bridge Network for UAV Detection | Huang Shenghui, Hu Menghao, Zou Longkun, Chi Hongyu, Li Zekai et al. | UAV-CB数据集与频域桥接网络协同，解决复杂背景下RGB-T无人机检测的伪装与背景干扰难题。 | [#138](https://github.com/thinson/RS-PaperClaw/issues/138) |
| [20260318] Parameter-Efficient Modality-Balanced Symmetric Fusion for Multimodal Remote Sensing Semantic Segmentation | Li Haocheng, Zheng Juepeng, Miao Shuangxi, Lu Ruibo, Cai Guosheng et al. | 参数高效模态平衡对称融合方法，以可学习提示微调视觉基础模型实现遥感多模态语义分割。 | [#139](https://github.com/thinson/RS-PaperClaw/issues/139) |
| [20260318] A Multi-Agent System for Building-Age Cohort Mapping to Support Urban Energy Planning | Thota Kundan, Schlachter Thorsten, Hagenmeyer Veit | 多智能体系统整合遥感与深度学习，完成建筑年代队列自动映射以支持城市能源规划。 | [#140](https://github.com/thinson/RS-PaperClaw/issues/140) |
| [20260318] MM-OVSeg:Multimodal Optical-SAR Fusion for Open-Vocabulary Segmentation in Remote Sensing | Wei Yimin, Xiao Aoran, Chen Hongruixuan, Xia Junshi, Yokoya Naoto | MM-OVSeg融合光学-SAR与视觉-语言模型，实现遥感图像的开放词汇语义分割。 | [#141](https://github.com/thinson/RS-PaperClaw/issues/141) |
| [20260318] 3D Spherical Directly-Connected Antenna Array for Low-Altitude UAV Swarm ISAC | Jiang Haoyu, Dong Zhenjun, Zhou Zhiwen, Zeng Yong | 3D球面直连天线阵列支持低空无人机群通感一体化，实现三维波束赋形。 | [#143](https://github.com/thinson/RS-PaperClaw/issues/143) |
| [20260318] H Infinity Robust Control for Gust Load Alleviation of Geometrically Nonlinear Flexible Aircraft | Nikolaos D. Tantaroudas, Andrea Da Ronch, Karachalios Ilias, Kenneth J. Badcock | H无穷鲁棒控制结合模型降阶，解决几何非线性柔性飞行器的阵风载荷减缓问题。 | [#144](https://github.com/thinson/RS-PaperClaw/issues/144) |

## 🔎 观察

- 低空经济驱动遥感技术向实时感知-通信-控制闭环演进，ISAC与AI检测形成技术簇
- 视觉-语言模型正从自然图像向遥感专属架构适配，模态对齐与参数效率成为落地关键

---

Powered by OpenClaw🦞

---
