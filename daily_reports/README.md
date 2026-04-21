# Daily Reports

最近三天日报（最新在前）：

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

# [20260419](./202604/20260419.md)
## 📌 今日概况

今日共检索候选论文 5 篇；关键词+LLM 智能匹配遥感交叉论文 4 篇；最终纳入日报 4 篇。

今日遥感AI研究聚焦模型可靠性与效率提升。超分辨率、强化学习奖励机制、多模态大模型鲁棒性及无人机集群控制成为热点，涵盖大气监测、视觉语言理解、地球观测等应用场景，体现从算法创新到系统部署的完整链条。

## ✨ 今日亮点

- 自监督超分辨率技术突破Sentinel-5P高光谱数据分辨率瓶颈
- 混合奖励机制解决遥感图像理解中的感知惯性难题
- 多模态大模型鲁棒性增强方案应对地球观测视觉扰动

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260419] Self-Supervised Super-Resolution for Sentinel-5P Hyperspectral Images | Hyam Omar Ali, Crosnier Antoine, Abraham Romain, Combelles Baptiste, Jégou Fabrice, Galerne Bruno | Université Paris-Saclay, CNRS, ENS Paris-Saclay, Centre Borelli, Gif-sur-Yvette, France；Université d'Orléans, CNRS, PRISME, Orléans, France；VITO, Remote Sensing, Boeretang, Mol, Belgium | 提出自监督超分辨率方法，针对Sentinel-5P高光谱图像实现无配对训练下的分辨率增强，服务大气监测应用。 | [#375](https://github.com/thinson/RS-PaperClaw/issues/375) |
| [20260419] RS-HyRe-R1: A Hybrid Reward Mechanism to Overcome Perceptual Inertia for Remote Sensing Images Understanding | Zhou Gaozhi, He Hu, Shen Peng, Zhang Jipeng, Zhang Liujue, Xu Linrui, Wang Zeyuan, Li Ziyu, Cui Xuezhi, Guo Wang, Li Haifeng | Chinese Academy of Sciences | 设计RS-HyRe-R1混合奖励机制，通过视觉-语言模型强化学习克服遥感图像理解中的感知惯性问题。 | [#376](https://github.com/thinson/RS-PaperClaw/issues/376) |
| [20260419] RemoteShield: Enable Robust Multimodal Large Language Models for Earth Observation | Min Rui, Yao Liang, Miao Shiyu, Xu Shengxiang, Liu Yuxuan, Zhang Chuanyi, Di Shimin, Liu Fan | Hohai University；Nanjing University；Southeast University | 构建RemoteShield框架，提升多模态大语言模型在地球观测任务中对视觉扰动的鲁棒性。 | [#377](https://github.com/thinson/RS-PaperClaw/issues/377) |
| [20260419] Shepherding UAV Swarm with Action Prediction Based on Movement Constraints | Tsunoda Yusuke, Goto Yusuke, Sato Takao | Graduate School of Engineering, University of Hyogo | 基于牧羊犬行为启发，利用运动约束动作预测实现无人机集群协同控制。 | [#378](https://github.com/thinson/RS-PaperClaw/issues/378) |

## 🔎 观察

- 遥感大模型研究正从性能优化转向可靠性保障，鲁棒性成为部署关键指标。
- 自监督与强化学习在遥感领域渗透率提升，降低标注依赖的同时增强模型适应性。

---

Powered by OpenClaw🦞

---

# [20260418](./202604/20260418.md)
## 📌 今日概况

今日共检索候选论文 8 篇；关键词+LLM 智能匹配遥感交叉论文 5 篇；最终纳入日报 3 篇。

今日遥感AI研究聚焦SAR数据智能处理与多模态融合。深度学习在积雪深度反演、多目标监视轨迹规划及异构多模态预训练三大方向取得进展，体现从单一任务优化向多源协同与高效表征学习的演进趋势。

## ✨ 今日亮点

- InSAR深度学习反演积雪深度，突破传统相位解缠限制
- DRL驱动SAR载机多目标监视轨迹规划，兼顾目标可见性约束
- 条件退化MAE实现异构多模态高效联合预训练，降低数据依赖

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260418] Deep Learning-Based Snow Depth Retrieval Using Sentinel-1 Repeat-Pass InSAR | Yadav Nayan, Oveisgharan Shadi, Jalali Shirin | Rutgers University；California Institute of Technology | 提出基于Sentinel-1重复轨道InSAR的深度学习积雪深度反演方法，利用神经网络直接学习干涉相位与雪深映射关系。 | [#372](https://github.com/thinson/RS-PaperClaw/issues/372) |
| [20260418] Multi-stage Planning for Multi-target Surveillance using Aircrafts Equipped with Synthetic Aperture Radars Aware of Target Visibility | Fuertes Daniel, Carlos R. del-Blanco, Jaureguizar Fernando, Juan José Navarro-Corcuera, García Narciso | Universidad Politécnica de Madrid | 构建多阶段深度强化学习框架，为SAR载机规划多目标监视轨迹，显式建模目标可见性以提升监视效率。 | [#373](https://github.com/thinson/RS-PaperClaw/issues/373) |
| [20260418] Better with Less: Tackling Heterogeneous Multi-Modal Image Joint Pretraining via Conditioned and Degraded Masked Autoencoder | Peng Bowen, Liu Yongxiang, Zhou Jie, Chen Xiaodong, Liu Tianpeng, Yu Xiaogang, Liu Li | National University of Defense Technology | 设计条件退化掩码自编码器，通过模态条件掩码策略实现光学与SAR异构数据的高效联合预训练。 | [#385](https://github.com/thinson/RS-PaperClaw/issues/385) |

## 🔎 观察

- SAR智能应用从静态图像分析向动态任务规划延伸，强化学习成为连接感知与决策的关键桥梁。
- 多模态预训练正从数据堆砌转向结构化掩码设计，'更少数据、更好表征'成为遥感基础模型新范式。

---

Powered by OpenClaw🦞

---
