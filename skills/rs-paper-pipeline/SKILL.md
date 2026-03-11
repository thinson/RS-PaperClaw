---
name: rs-paper-pipeline
description: Process arXiv papers into RS-PaperClaw GitHub issues with a fixed pipeline (abs metadata + PDF preview images + Chinese abstract + top tags + 10-question analysis + quality gate). Use when user asks to run/update paper reports, regenerate a specific issue, or troubleshoot pipeline output quality/format for RS-PaperClaw.
---

# RS Paper Pipeline

Run the RS-PaperClaw paper flow end-to-end and keep output consistent.

## Use This Workflow

1. Parse input from user:
   - arXiv URL or arXiv ID (e.g. `2603.08582v1`)
   - target issue number (required for update-only mode)
2. Run:

```bash
python3 /home/openclaw/.openclaw/workspace/scripts/paper_processor.py <arxiv_id> <issue_number>
```

3. Read terminal logs and report key checkpoints:
   - `STEP-1` metadata + PDF preview images
   - `STEP-2` abstract translation
   - `STEP-3` top5 tags extraction
   - `STEP-4` 10Q analysis generation
   - `GATE` quality gate
   - `ISSUE` update result

## Output Contract (Current Pipeline)

The generated issue should include:

- Basic info table: title, authors, date, arXiv links, Chinese abstract, tags (date + top5)
- Paper overview: first 3 PDF pages as JPG, displayed in a 1-row/3-column table
- 10-question analysis in Chinese (Q1-Q10)
- Footer: `Powered by OpenClaw🦞`

## Quality Rules

Treat these as blocking requirements unless user explicitly asks to relax:

- No placeholder answers (`待提取`, `未知`, `分析中`, `N/A`, `Unknown`)
- Q1-Q10 must all be present and non-empty
- At least 1 preview image uploaded (expected: 3)
- If gate fails, retry summary once; still failing => do not update issue

## Prompt/Parsing Rules

- Summary prompt should force readable format with markers: `A1:` … `A10:`
- Validate markers with regex before accepting output
- If some answers are missing, repair per-question and re-check gate
- Preserve Markdown readability (short paragraphs or bullets)

## Fast Troubleshooting

- If `images=0` or preview missing: verify `pdftoppm` availability and PDF download success
- If gate fails on a few questions: rerun once (LLM variance); if repeatable, inspect parser/prompt markers
- If issue was not updated: confirm issue number exists and script ran with `<issue_number>` argument

## Resources

- Main script: `/home/openclaw/.openclaw/workspace/scripts/paper_processor.py`
- Prompts: `/home/openclaw/.openclaw/workspace/scripts/prompts/`
