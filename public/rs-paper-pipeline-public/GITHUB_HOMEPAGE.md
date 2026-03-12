# RS-Paper Pipeline

> Daily remote-sensing paper intelligence pipeline: arXiv filtering → per-paper analysis issue → daily digest → repository archive.

[![Python](https://img.shields.io/badge/python-3.10%2B-blue)](#)
[![License](https://img.shields.io/badge/license-MIT-green)](#)
[![Status](https://img.shields.io/badge/status-active-success)](#)

## Why this project

Keeping up with remote-sensing + AI papers is hard:

- too many daily arXiv updates
- noisy keyword matches
- scattered notes and weak traceability

This pipeline turns daily paper tracking into a reproducible workflow with structured outputs.

## What it does

1. Pull daily arXiv candidates (keyword-based)
2. Run LLM cross-filtering (RS × AI/CV/Foundation Models)
3. Generate/update one GitHub issue per paper
4. Build a daily digest issue (`日报 YYYYMMDD`)
5. Sync digest markdown to repo (`daily_reports/YYYYMM/YYYYMMDD.md`)
6. Push digest to Feishu

## Output example

- **Per-paper issue** includes:
  - metadata table (title/authors/date/arXiv)
  - **TL;DR** (≤50 Chinese chars)
  - Chinese abstract
  - top tags
  - 3-page preview images
  - 10-question deep analysis

- **Daily digest** includes:
  - numeric overview (candidate count / LLM-selected count / included count)
  - highlights
  - one-liners for each paper
  - observations

## Architecture

```text
arXiv API
   ↓
daily_arxiv_cross_filter.py
   ↓ (selected papers)
paper_processor.py
   ↓ (paper issues)
daily_digest_llm_upgrade.py
   ↓ (digest issue)
sync_daily_reports_to_repo.py
   ↓
daily_reports/YYYYMM/YYYYMMDD.md + README.md
   ↓
Feishu push
```

## Quick start

```bash
cp .env.example .env
# fill env vars
set -a && source .env && set +a
python3 scripts/run_rs_daily_workday.py
```

## Environment variables

- `GITHUB_TOKEN`
- `GITHUB_REPO` (`owner/repo`)
- `BAILIAN_API_KEY`
- `LLM_MODEL` (optional)
- `FEISHU_TARGET` (optional)

## Scheduler

Weekdays 09:05 (Asia/Shanghai):

```cron
CRON_TZ=Asia/Shanghai
5 9 * * 1-5 /usr/bin/python3 /path/to/scripts/run_rs_daily_workday.py >> /path/to/logs/rs_daily_workday.log 2>&1
```

## Design principles

- deterministic where possible, LLM where valuable
- quality gate before issue update
- traceable outputs (issues + markdown archive)
- no hardcoded secrets in public package

## Roadmap

- [ ] optional fallback LLM provider
- [ ] richer de-dup across arXiv versions
- [ ] digest quality scoring and regression checks
- [ ] optional bilingual digest output

## License

MIT (recommended)
