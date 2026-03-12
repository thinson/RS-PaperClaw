<div align="center">

# RS-PaperClaw🦞

### Automated Remote-Sensing Paper Tracking & Analysis Pipeline

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)](#)
[![Status](https://img.shields.io/badge/Status-Active-2EA043)](#)
[![Workflow](https://img.shields.io/badge/Workflow-arXiv%20%E2%86%92%20Issue%20%E2%86%92%20Digest-8A2BE2)](#)

**arXiv → Per-paper Issue Report → Daily Digest**

中文版本：**[README.md](./README.md)**

</div>

---

> 📌 **Recent Daily Digests**: Browse latest summaries and archives → **[Open Digest Navigator](./daily_reports/README.md)**

## ✨ Project Positioning

RS-PaperClaw automates the daily workflow:

- 🔎 Fetch arXiv candidates (remote-sensing related)
- 🧠 Cross-filter with keywords + LLM
- 📝 Generate/update per-paper reading report issues
- 🗞️ Generate daily digest issues
- 🗂️ Sync digest markdown to `daily_reports/YYYYMM/YYYYMMDD.md`
- 📮 Push digest to Feishu

## 🎯 Why issue-centric?

- 🧭 **Traceable**: one paper, one issue; history and changes are easy to track.
- 🤝 **Collaborative**: discussion, corrections, and additions happen in-place.
- ⚙️ **Automation-friendly**: stable create/update target for incremental runs.
- 🗂️ **Closed-loop archive**: issue for dynamic work + markdown for static records.

## 🧩 Core Capabilities

| Module | Output |
|---|---|
| Per-paper report | metadata, TL;DR, Chinese abstract, tags, first-3-page previews, 10-question analysis |
| Daily digest | numeric overview, highlights, article list, observations |
| Quality control | blocks placeholders and incomplete structures |
| Archive | issue + markdown dual-track sync |

---

## 🗺️ Repository Layout (main)

```text
RS-PaperClaw/
├── daily_reports/
│   ├── README.md
│   └── YYYYMM/YYYYMMDD.md
├── papers/previews/
├── skills/rs-paper-pipeline/
│   ├── README.md
│   ├── SKILL.md
│   └── scripts/
└── README.md
```

---

## 🚀 Quick Start

### 1) Requirements

- Python 3.10+
- `pip install PyGithub`
- `poppler-utils` (`pdftoppm`, `pdftotext`)

### 2) Environment variables

```bash
export GITHUB_TOKEN="..."
export GITHUB_REPO="owner/repo"
export BAILIAN_API_KEY="..."
# optional
export FEISHU_TARGET="user:xxx"
export LLM_MODEL="MiniMax-M2.5"
```

### 3) Run today's workflow

```bash
python3 skills/rs-paper-pipeline/scripts/run_rs_daily_workday.py
```

---

## ⏰ Scheduler (Weekdays 09:05)

```cron
CRON_TZ=Asia/Shanghai
5 9 * * 1-5 /usr/bin/python3 /path/to/skills/rs-paper-pipeline/scripts/run_rs_daily_workday.py >> /path/to/logs/rs_daily_workday.log 2>&1
```

---

## 📎 Notes

- Chinese README is the default entry (`README.md`).
- All scripts are under `skills/rs-paper-pipeline/scripts/`.

---

## ⭐ Star History

[![Star History Chart](https://api.star-history.com/svg?repos=thinson/RS-PaperClaw&type=Date)](https://star-history.com/#thinson/RS-PaperClaw&Date)

---

<div align="center">

**Powered by OpenClaw🦞**

</div>
