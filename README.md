<div align="center">
  <img src="./docs/logo-220.png" alt="RS-PaperClaw Logo" width="120" />

# RS-PaperClaw🦞

### 遥感论文自动追踪与分析流水线

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)](#)
[![Status](https://img.shields.io/badge/Status-Active-2EA043)](#)
[![Workflow](https://img.shields.io/badge/Workflow-arXiv%20%E2%86%92%20Issue%20%E2%86%92%20Digest-8A2BE2)](#)
[![Pages](https://img.shields.io/badge/GitHub%20Pages-Live-b55f34)](https://thinson.github.io/RS-PaperClaw/)

**arXiv → 单篇报告 Issue → 每日汇总日报 → 可视化阅读页面**

English version: **[README_EN.md](./README_EN.md)**

</div>

---

## 🌐 在线阅读入口

- 项目主页（GitHub Pages）：**https://thinson.github.io/RS-PaperClaw/**
- 日报归档目录：**[daily_reports/](./daily_reports/README.md)**

## 🔗 Related Projects

- **papers.cool**: https://papers.cool/

## 🖼️ 界面预览

| 电脑端 UI | 移动端 UI |
|---|---|
| <img src="./docs/screenshots/ui-desktop.jpg" alt="RS-PaperClaw Desktop UI" height="260" /> | <img src="./docs/screenshots/ui-mobile.jpg" alt="RS-PaperClaw Mobile UI" height="260" /> |

---

## ✨ 项目做什么

RS-PaperClaw 每天自动完成：

- 🔎 拉取 arXiv 候选论文（遥感相关）
- 🧠 关键词 + LLM 二级筛选
- 📝 生成 / 更新单篇阅读报告（GitHub Issue）
- 🗞️ 生成当天日报（GitHub Issue）
- 🗂️ 同步日报到 `daily_reports/YYYYMM/YYYYMMDD.md`
- 📮 推送摘要到钉钉/飞书

---

## 🎯 为什么以 Issue 为核心

- 🧭 **可追踪**：单论文单 Issue，历史与改动可回溯
- 🤝 **易协作**：评论即讨论，补充即沉淀
- ⚙️ **自动化友好**：增量流程可稳定更新同一条记录
- 🗂️ **归档闭环**：Issue 动态协作 + Markdown 静态留档

---

## 🧩 核心能力

| 模块 | 输出 |
|---|---|
| 单篇报告 | 基础信息、TL;DR、中文摘要、标签、前三页预览图、10问分析 |
| 日报生成 | 今日概况（含数量统计）、亮点、文章列表、观察 |
| 质量控制 | 过滤占位内容，保障结构完整与可读性 |
| 结果归档 | Issue + Markdown 双轨同步，便于追踪与回溯 |
| 可视化页面 | 最近日报浏览、移动端卡片视图、Issue 深读弹层 |

---

## 🗺️ 目录结构（main）

```text
RS-PaperClaw/
├── .github/workflows/                 # GitHub Actions（定时主跑 + 手动运维）
├── docs/                             # GitHub Pages 静态页面
│   ├── index.html
│   └── logo-220.png
├── daily_reports/                    # 日报归档（按年月）
│   ├── README.md
│   └── YYYYMM/YYYYMMDD.md
├── papers/previews/                  # 论文预览图（用于 Issue 展示）
├── skills/rs-paper-pipeline/         # 技能与脚本
│   ├── README.md
│   ├── SKILL.md
│   ├── .env.example
│   ├── RUNBOOK_RS_PIPELINE.md
│   ├── AGENT_GUIDE_RS_PIPELINE.md
│   └── scripts/
│       ├── cli.py
│       ├── clients/
│       ├── services/
│       ├── config/filter_keywords.json
│       └── prompts/filter_cross_prompt.md
└── README_EN.md
```

---

## 🚀 快速开始

### 1) 初始化

```bash
cd skills/rs-paper-pipeline
./bootstrap.sh
```

### 2) 配置 `.env`

至少填写：

- `GITHUB_TOKEN`
- `BAILIAN_API_KEY`

可选：

- `DINGTALK_WEBHOOK`
- `FEISHU_TARGET`
- `RS_GITHUB_REPO`

### 3) 运行当天流程

```bash
cd skills/rs-paper-pipeline
python3 scripts/cli.py run
```

### 4) 常用命令

```bash
cd skills/rs-paper-pipeline
python3 scripts/cli.py doctor
python3 scripts/cli.py filter --dry-run --date 20260317
python3 scripts/cli.py run --date 20260317 --no-notify
python3 scripts/cli.py reconcile --date 20260317 --dry-run
```

### 5) 想定制成你自己的论文系统

可以直接看：

- `skills/rs-paper-pipeline/CUSTOMIZATION_GUIDE.md`

这份文档专门说明：

- 如何改关键词和 regex
- 如何改筛选 prompt
- 如何改 `.env` 配置项
- 如何把目标仓库切到你自己的 repo
- 如何用最小风险验证改动

---

## ⏰ 定时任务（示例）

```cron
推荐直接使用仓库内工作流：

- `.github/workflows/rs-pipeline-schedule.yml`
- `.github/workflows/rs-pipeline-manual.yml`

它们会调用 `skills/rs-paper-pipeline/scripts/cli.py`，并使用仓库内的筛选配置文件。
```

---

## 📎 备注

- 默认文档语言为中文；英文请见 [README_EN.md](./README_EN.md)
- 页面部署方式：`main` 分支 + `/docs`
- 文章 list 筛选规则来自：
  - `skills/rs-paper-pipeline/scripts/config/filter_keywords.json`
  - `skills/rs-paper-pipeline/scripts/prompts/filter_cross_prompt.md`

---

## ✅ TODO
- 增加单位名称
- 增加期刊来源：RSE（Remote Sensing of Environment）、ISPRS JPRS、IEEE 旗下相关期刊

---

## ⭐ Star History

[![Star History Chart](https://api.star-history.com/svg?repos=thinson/RS-PaperClaw&type=Date)](https://star-history.com/#thinson/RS-PaperClaw&Date)
