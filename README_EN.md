# RS-PaperClaw🦞

Automated remote-sensing paper pipeline (arXiv → per-paper issue report → daily digest).

中文版本：**[README.md](./README.md)**

---

## What it does

RS-PaperClaw automates the daily workflow:

1. Fetch arXiv candidates (remote-sensing related)
2. Cross-filter with keywords + LLM
3. Generate/update per-paper reading report issues
4. Generate daily digest issue
5. Sync digest to `daily_reports/YYYYMM/YYYYMMDD.md`
6. Push digest to Feishu

---

## Key features

- **Standardized per-paper report**: metadata, TL;DR, Chinese abstract, tags, preview images, 10-question analysis
- **Daily digest**: numeric overview, highlights, one-liners, observations
- **Quality gate**: blocks placeholders and incomplete outputs
- **Traceable archive**: issue + markdown dual track

---

## Main branch structure

```text
RS-PaperClaw/
├── daily_reports/
├── papers/previews/
├── skills/rs-paper-pipeline/
│   ├── README.md
│   ├── SKILL.md
│   └── scripts/
└── README.md
```

---

## Quick start

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

## Scheduler (Weekdays 09:05)

```cron
CRON_TZ=Asia/Shanghai
5 9 * * 1-5 /usr/bin/python3 /path/to/skills/rs-paper-pipeline/scripts/run_rs_daily_workday.py >> /path/to/logs/rs_daily_workday.log 2>&1
```

---

All scripts are under `skills/rs-paper-pipeline/scripts/`.
