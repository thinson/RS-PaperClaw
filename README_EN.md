<div align="center">
  <img src="./docs/logo-220.png" alt="RS-PaperClaw Logo" width="120" />

# RS-PaperClaw🦞

### Automated Remote-Sensing Paper Tracking & Analysis Pipeline

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)](#)
[![Status](https://img.shields.io/badge/Status-Active-2EA043)](#)
[![Workflow](https://img.shields.io/badge/Workflow-arXiv%20%E2%86%92%20Issue%20%E2%86%92%20Digest-8A2BE2)](#)
[![Pages](https://img.shields.io/badge/GitHub%20Pages-Live-b55f34)](https://thinson.github.io/RS-PaperClaw/)

**arXiv → Per-paper Issue Report → Daily Digest → Visual Reading Portal**

中文版本：**[README.md](./README.md)**

</div>

---

## 🌐 Live Portal

- GitHub Pages: **https://thinson.github.io/RS-PaperClaw/**
- CVPR 2026 GeoAI Collection: **https://thinson.github.io/RS-PaperClaw/cvpr2026_geoai.html**
- Digest archive: **[daily_reports/](./daily_reports/README.md)**

## 🖼️ UI Preview

| Desktop UI | Mobile UI |
|---|---|
| <img src="./docs/screenshots/ui-desktop.jpg" alt="RS-PaperClaw Desktop UI" height="260" /> | <img src="./docs/screenshots/ui-mobile.jpg" alt="RS-PaperClaw Mobile UI" height="260" /> |

---

## 📰 News

- `2026-04-24`: Added a CVPR 2026 GeoAI paper collection with 139 papers (9 Oral + 20 Highlight + 110 Poster), browseable by topic tags.
- `2026-04-20`: Added a short project timeline to the README for easier maintenance tracking.
- `2026-04-19`: Completed a focused GitHub Pages frontend update, including paged archive loading, date deep links, merged `More` interaction, and multiple Papers table display fixes.
- `2026-04-17`: Added institution metadata to per-paper reports and daily digests; author rendering was also updated to stop using `et al.`.
- `2026-03-05`: The earliest traceable daily report currently archived in this repository is `20260305`, marking the start of the report archive timeline.

---

## ✨ What this project does

RS-PaperClaw automates the daily pipeline:

- 🔎 Fetch arXiv candidates (remote-sensing related)
- 🧠 Run keyword + LLM cross filtering
- 📝 Generate / update per-paper reading reports (GitHub Issues)
- 🗞️ Generate daily digest issues
- 🗂️ Sync digest markdown to `daily_reports/YYYYMM/YYYYMMDD.md`
- 📮 Deliver summaries to DingTalk / Feishu

---

## 🎯 Why issue-centric

- 🧭 **Traceable**: one paper, one issue; full history is preserved
- 🤝 **Collaborative**: comments become discussion and knowledge capture
- ⚙️ **Automation-friendly**: stable targets for incremental updates
- 🗂️ **Closed loop**: dynamic issue workflow + static markdown archive

---

## 🧩 Core capabilities

| Module | Output |
|---|---|
| Per-paper report | metadata, TL;DR, Chinese abstract, tags, first-3-page previews, 10-question analysis |
| Daily digest | numeric overview, highlights, article list, observations |
| Quality control | filters placeholders and incomplete structures |
| Archive | issue + markdown dual-track sync |
| Web portal | recent digest browser, mobile cards, issue deep-dive overlay |

---

## 🗺️ Repository layout (main)

```text
RS-PaperClaw/
├── .github/workflows/                 # GitHub Actions for scheduled and manual ops
├── docs/                             # GitHub Pages static site
│   ├── index.html
│   └── logo-220.png
├── daily_reports/                    # digest archive by month
│   ├── README.md
│   └── YYYYMM/YYYYMMDD.md
├── papers/previews/                  # preview images for issue display
├── skills/rs-paper-pipeline/         # skill and scripts
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
└── README.md
```

---

## 🚀 Quick start

### 0) Clone the repo

The repo contains many paper preview images (400MB+). If you only need the pipeline scripts, use a lightweight clone:

```bash
# Lightweight clone (skips images, ~1MB)
git clone --filter=blob:none --sparse https://github.com/thinson/RS-PaperClaw.git
cd RS-PaperClaw
git sparse-checkout set skills/rs-paper-pipeline papers/issue_index.json

# Full clone (includes all preview images, ~400MB)
git clone https://github.com/thinson/RS-PaperClaw.git
```

### 1) Bootstrap

```bash
cd skills/rs-paper-pipeline
./bootstrap.sh
```

### 2) Configure `.env`

Required:

- `GITHUB_TOKEN`
- `BAILIAN_API_KEY`

Optional:

- `DINGTALK_WEBHOOK`
- `FEISHU_TARGET`
- `RS_GITHUB_REPO`

### 3) Run today's workflow

```bash
cd skills/rs-paper-pipeline
python3 scripts/cli.py run
```

### 4) Common commands

```bash
cd skills/rs-paper-pipeline
python3 scripts/cli.py doctor
python3 scripts/cli.py filter --dry-run --date 20260317
python3 scripts/cli.py run --date 20260317 --no-notify
python3 scripts/cli.py reconcile --date 20260317 --dry-run
```

---

## ⏰ Scheduler example

```cron
Prefer the repository workflows:

- `.github/workflows/rs-pipeline-schedule.yml`
- `.github/workflows/rs-pipeline-manual.yml`

Both workflows execute `skills/rs-paper-pipeline/scripts/cli.py` and read the filter config files from the repository.
```

---

## 📎 Notes

- Chinese README is the default entry: [README.md](./README.md)
- GitHub Pages deployment source: `main` branch + `/docs`
- Article-list filtering rules come from:
  - `skills/rs-paper-pipeline/scripts/config/filter_keywords.json`
  - `skills/rs-paper-pipeline/scripts/prompts/filter_cross_prompt.md`

---

## ✅ TODO

- Add journal sources: RSE (Remote Sensing of Environment), ISPRS JPRS, and IEEE journals (as complements beyond arXiv, including ingestion and filtering).

---

## 🔗 Related Projects

- **papers.cool**: https://papers.cool/

---

## ⭐ Star History

[![Star History Chart](https://api.star-history.com/svg?repos=thinson/RS-PaperClaw&type=Date)](https://star-history.com/#thinson/RS-PaperClaw&Date)
