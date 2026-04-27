#!/usr/bin/env python3
from __future__ import annotations

import json
import re

from clients.llm_client import call_llm, load_prompt


def has_bad_placeholder(text: str) -> bool:
    bad = ["待提取", "未知", "Unknown", "分析中", "N/A"]
    return any(keyword in (text or "") for keyword in bad)


def dedupe_bullets(text: str) -> str:
    lines = (text or "").splitlines()
    seen = set()
    output = []
    for line in lines:
        normalized = re.sub(r"\s+", "", line.lower())
        if line.strip().startswith(("-", "*")):
            if normalized in seen:
                continue
            seen.add(normalized)
        output.append(line)
    return "\n".join(output)


def format_answer_md(text: str) -> str:
    stripped = (text or "").strip()
    if not stripped:
        return stripped

    if any(token in stripped for token in ["\n- ", "\n* ", "\n1.", "\n##", "\n###", "**"]):
        stripped = re.sub(r"\n{3,}", "\n\n", stripped)
        return dedupe_bullets(stripped)

    parts = [part.strip() for part in re.split(r"[。；]\s*", stripped) if part.strip()]
    if len(parts) >= 2:
        return dedupe_bullets("\n".join([f"- {part}。" for part in parts]))

    return stripped


def quality_gate(info: dict, analysis: dict, abstract_zh: str, uploaded_images: int) -> tuple[bool, list[str]]:
    errors: list[str] = []
    if not info.get("title") or has_bad_placeholder(info.get("title")):
        errors.append("标题为空或无效")
    if not info.get("authors") or has_bad_placeholder(info.get("authors")):
        errors.append("作者为空或无效")
    if not info.get("institutions") or has_bad_placeholder(info.get("institutions")):
        errors.append("单位为空或无效")
    if not info.get("date"):
        errors.append("日期为空")
    if not abstract_zh or len(abstract_zh.strip()) < 20:
        errors.append("摘要为空或无效")
    if uploaded_images < 1:
        errors.append("图片数量不足（至少1张）")
    for i in range(1, 11):
        answer = analysis.get(f"q{i}", "")
        if not answer or has_bad_placeholder(answer):
            errors.append(f"Q{i} 未通过质检")
    return len(errors) == 0, errors


def translate_text(text: str) -> str:
    if not text:
        return ""
    template = load_prompt("translate_prompt.md")
    return call_llm(template.replace("{content}", text), max_tokens=2000, timeout=60)


def extract_tags(title: str, abstract: str) -> list[str]:
    template = load_prompt("tags_prompt.md")
    prompt = template.replace("{title}", title).replace("{abstract}", abstract[:1000])
    result = call_llm(prompt, max_tokens=200, timeout=30)

    tags = []
    for tag in result.split(","):
        tag = tag.strip()
        if tag and len(tag) > 1:
            tags.append(tag)
    return tags[:8]


def generate_tldr(title: str, abstract_en: str) -> str:
    prompt = (
        "请为下面论文生成中文 TL;DR，仅1句，控制在50字以内，不要换行，不要项目符号，不要前缀。\n"
        f"标题：{title}\n"
        f"摘要：{abstract_en[:1200]}"
    )
    output = (call_llm(prompt, max_tokens=120, timeout=60) or "").strip()
    output = re.sub(r"\s+", " ", output)
    output = re.sub(r"^(TL;DR[:：]?\s*)", "", output, flags=re.IGNORECASE)
    return output or "面向遥感任务，提出可扩展的推理框架并验证有效性。"


def _dedupe_institutions(institutions: list[str]) -> list[str]:
    cleaned: list[str] = []
    seen: set[str] = set()
    for item in institutions:
        text = re.sub(r"\s+", " ", item or "").strip(" ,;:，；：")
        if not text:
            continue
        if re.search(r"@", text):
            continue
        lowered = text.casefold()
        if lowered in seen:
            continue
        seen.add(lowered)
        cleaned.append(text)
    return cleaned


def _heuristic_institutions(first_page_text: str) -> list[str]:
    keyword_pattern = re.compile(
        r"(universit|college|school|institut|academy|laborator|centre|center|department|hospital|faculty|research|laboratory|lab\b|国家|大学|学院|研究所|实验室|中心|医院)",
        re.IGNORECASE,
    )
    lines = []
    for raw_line in (first_page_text or "").splitlines():
        line = re.sub(r"\s+", " ", raw_line).strip()
        if not line or len(line) < 6:
            continue
        if re.search(r"^(abstract|摘要|keywords?|index terms|introduction)\b", line, re.IGNORECASE):
            break
        if keyword_pattern.search(line) and not re.search(r"@", line):
            parts = re.split(r"\s+(?=\d+\s+[A-Z])", line)
            for part in parts:
                cleaned = re.sub(r"^\d+\s*", "", part).strip()
                if keyword_pattern.search(cleaned):
                    lines.append(cleaned)
    return _dedupe_institutions(lines)


def _extract_footnote_block(first_page_text: str) -> str:
    """Extract IEEE-style footnote block from the bottom of first page.

    IEEE Trans templates place author affiliations in a footnote starting with
    lines like "This work was supported..." or "(Corresponding author: ...)".
    This block sits below the abstract and is often missed by top-down scraping.
    """
    text = first_page_text or ""
    footnote_markers = [
        r"This work was supported",
        r"\(Corresponding author[:：]",
        r"Manuscript received",
        r"Digital Object Identifier",
    ]
    earliest = len(text)
    for marker in footnote_markers:
        m = re.search(marker, text, re.IGNORECASE)
        if m and m.start() < earliest:
            earliest = m.start()

    if earliest >= len(text):
        return ""
    return text[earliest:]


def _parse_ieee_footnote(footnote: str, known_authors: str) -> list[str]:
    """Parse IEEE-style "is with / was with" affiliation sentences."""
    institutions: list[str] = []

    for match in re.finditer(
        r"(?:are|is|was|were)\s+(?:all\s+)?(?:currently\s+)?with\s+(.+?)(?:\s*\(|\s*\[|\s*[–—]|\.$|\n)",
        footnote,
        re.IGNORECASE,
    ):
        chunk = match.group(1).strip().rstrip(" ,;.")
        # Extract institution-like phrases containing keywords
        kw = re.compile(
            r"(universit[yi]|college|school|institut|academy|laborator[yi]|"
            r"centre|center|department|hospital|faculty|research|laboratory|"
            r"大学|学院|研究所|实验室|中心|医院|研究院|研究院)",
            re.IGNORECASE,
        )
        for phrase in re.split(r",\s*and\s+also\s+|\band\s+also\b", chunk):
            phrase = phrase.strip().rstrip(" ,;.")
            if kw.search(phrase):
                institutions.append(phrase)

    # Also try "are with X, Y, and Z" pattern
    for match in re.finditer(
        r"(?:are|were|were all)\s+(?:all\s+)?with\s+([\w\s,]+?)(?:\s*\(|\s*\[|\s*[–—]|\.)",
        footnote,
        re.IGNORECASE,
    ):
        chunk = match.group(1).strip()
        # Split by ", and" or "and also" to separate multi-institution mentions
        for part in re.split(r",?\s+and\s+also\s+|,?\s+and\s+", chunk):
            part = part.strip().rstrip(" ,;.")
            if len(part) > 6:
                institutions.append(part)

    return _dedupe_institutions(institutions)


def extract_institutions_from_first_page(title: str, authors: str, first_page_text: str) -> str:
    if not first_page_text.strip():
        return ""

    # Strategy 1: IEEE footnote — scan the *entire* first page, especially
    # the bottom footnote block that sits below the abstract.
    footnote = _extract_footnote_block(first_page_text)
    institutions: list[str] = []
    if footnote:
        institutions = _parse_ieee_footnote(footnote, authors)

    # Strategy 2: LLM extraction — feed the full first page text (not just
    # the part before abstract), since IEEE footnotes are below the abstract.
    if not institutions:
        context = (first_page_text or "")[:6000]
        prompt = (
            "你是学术论文信息抽取助手。请根据论文首页文本，提取作者所属单位名称。\n"
            "要求：\n"
            "1. 只输出单位名称，不输出作者名、邮箱、国家、脚注编号；\n"
            "2. 去重；\n"
            "3. 若首页无法可靠判断，返回严格 JSON []，不要猜测；\n"
            "4. 返回严格 JSON 数组，例如 [\"Tsinghua University\", \"Chinese Academy of Sciences\"]。\n"
            "5. 特别注意：IEEE 等期刊模板的单位信息常出现在摘要下方的脚注区域\n"
            "   （如 \"This work was supported...\" 或 \"(Corresponding author...)\" 之后的段落）。\n"
            "   请仔细阅读该区域，提取 \"is with / are with\" 后面跟着的单位名称。\n\n"
            f"标题：{title}\n"
            f"作者：{authors}\n"
            f"首页全文：\n{context}"
        )
        output = (call_llm(prompt, max_tokens=400, timeout=120) or "").strip()

        match = re.search(r"\[[\s\S]*\]", output)
        if match:
            try:
                data = json.loads(match.group(0))
                if isinstance(data, list):
                    institutions = [str(item) for item in data if isinstance(item, str)]
            except Exception:
                institutions = []

    # Strategy 3: heuristic fallback — scan entire first page, not just pre-abstract.
    if not institutions:
        institutions = _heuristic_institutions(first_page_text)

    institutions = _dedupe_institutions(institutions)
    return "；".join(institutions)


def extract_abstract_from_pdf_text(pdf_text: str) -> str:
    text = (pdf_text or "").replace("\r\n", "\n")
    match = re.search(
        r"(?is)\babstract\b[:\s]*([\s\S]*?)(?=\n\s*(?:keywords?|index terms|1[\.\s]+introduction|introduction)\b)",
        text,
    )
    if not match:
        return ""
    abstract = re.sub(r"\s+", " ", match.group(1)).strip(" -")
    return abstract


def recover_metadata_from_pdf(title: str, authors: str, abstract_en: str, first_page_text: str, pdf_text: str) -> dict[str, str]:
    safe_title = "" if has_bad_placeholder(title) else (title or "").strip()
    safe_authors = "" if has_bad_placeholder(authors) else (authors or "").strip()
    safe_abstract = "" if has_bad_placeholder(abstract_en) else (abstract_en or "").strip()
    recovered = {
        "title": safe_title,
        "authors": safe_authors,
        "abstract_en": safe_abstract,
    }
    first_page_compact = "\n".join(
        re.sub(r"\s+", " ", line).strip()
        for line in (first_page_text or "").splitlines()
        if re.sub(r"\s+", " ", line).strip()
    )

    if not recovered["abstract_en"]:
        recovered["abstract_en"] = extract_abstract_from_pdf_text(pdf_text)

    if recovered["title"] and recovered["authors"] and recovered["abstract_en"]:
        return recovered

    prompt = (
        "你是学术论文元信息抽取助手。请根据论文首页文本和正文片段，提取标题、作者、英文摘要。\n"
        "要求：\n"
        "1. 返回严格 JSON：{\"title\":\"...\",\"authors\":[\"...\"],\"abstract_en\":\"...\"}\n"
        "2. authors 必须是作者姓名数组，不要单位、邮箱、脚注编号；\n"
        "3. 如果某项无法可靠提取，对应值返回空字符串或空数组，不要猜测；\n"
        "4. 不要输出 JSON 以外的内容。\n\n"
        f"首页文本：\n{first_page_compact[:4000]}\n\n"
        f"正文片段：\n{(pdf_text or '')[:6000]}"
    )
    output = (call_llm(prompt, max_tokens=800, timeout=120) or "").strip()
    match = re.search(r"\{[\s\S]*\}", output)
    if not match:
        return recovered

    try:
        data = json.loads(match.group(0))
    except Exception:
        return recovered

    title_candidate = str(data.get("title", "")).strip()
    authors_candidate = data.get("authors", [])
    abstract_candidate = str(data.get("abstract_en", "")).strip()

    if not recovered["title"] and title_candidate and title_candidate.lower() != "unknown":
        recovered["title"] = title_candidate
    if not recovered["authors"] and isinstance(authors_candidate, list):
        from clients.arxiv_client import format_authors

        formatted_authors = format_authors([str(item) for item in authors_candidate if isinstance(item, str)])
        if formatted_authors and not has_bad_placeholder(formatted_authors):
            recovered["authors"] = formatted_authors
    if not recovered["abstract_en"] and abstract_candidate:
        recovered["abstract_en"] = abstract_candidate

    return recovered


def summarize_paper(title: str, authors: str, abstract_en: str, pdf_text: str, retry_logger=None) -> dict:
    template = load_prompt("summarize_prompt.md")
    base_prompt = template.replace("{title}", title).replace("{authors}", authors)
    base_prompt = base_prompt.replace("{abstract_en}", abstract_en[:2000]).replace("{pdf_text}", pdf_text[:20000])

    format_spec = """
请按以下格式输出（纯文本，不要 JSON，不要代码块）：
摘要翻译: <中文摘要>
A1: <回答>
A2: <回答>
A3: <回答>
A4: <回答>
A5: <回答>
A6: <回答>
A7: <回答>
A8: <回答>
A9: <回答>
A10: <回答>
要求：
1) A1-A10 每项必须非空，禁止“待提取/未知/分析中/N/A/Unknown”；
2) 每项用结构化 Markdown 输出，优先采用：
   - 🎯 结论：1 句
   - 📌 要点：3-5 条 bullet
3) 同一项内不要重复表达；尤其 A2（前人技术路线）必须是互不重复的路线清单。
"""
    result = call_llm(base_prompt + "\n\n" + format_spec, max_tokens=6000, timeout=400)

    missing_markers = [i for i in range(1, 11) if not re.search(rf"\bA{i}[:：]", result)]
    if missing_markers:
        if retry_logger:
            retry_logger("STEP-4", "RETRY", f"缺少标记 A{missing_markers}")
        retried = call_llm(base_prompt + "\n\n" + format_spec, max_tokens=6000, timeout=400)
        if retried:
            result = retried

    analysis = {"abstract_zh": ""}
    abstract_match = re.search(r"摘要翻译[:：]\s*([\s\S]*?)(?=\nA1[:：])", result)
    if abstract_match:
        analysis["abstract_zh"] = abstract_match.group(1).strip()

    def extract_answer(index: int, text: str) -> str:
        match = re.search(rf"\n?A{index}[:：]\s*([\s\S]*?)(?=\nA{index+1}[:：]|$)", text)
        return match.group(1).strip() if match else ""

    for i in range(1, 11):
        analysis[f"q{i}"] = extract_answer(i, result)

    for i in range(1, 11):
        answer = analysis.get(f"q{i}", "")
        if answer and not has_bad_placeholder(answer):
            continue

        repaired = ""
        for _ in range(2):
            repair_prompt = (
                f"基于以下论文信息，仅回答A{i}对应问题，120-220字，中文，不要编号前缀，不要占位词。\n"
                f"Q{i}问题："
                f"{'本文主要解决什么问题？' if i==1 else '前人技术路线？' if i==2 else '前人方案的局限性？' if i==3 else '核心思路？' if i==4 else '方法亮点？' if i==5 else '主要贡献？' if i==6 else '实验数据集？' if i==7 else '代码开源？' if i==8 else '客观评价？' if i==9 else '批判审视？'}\n"
                f"标题：{title}\n作者：{authors}\n摘要：{abstract_en[:1500]}\n正文片段：{pdf_text[:4000]}"
            )
            repaired = call_llm(repair_prompt, max_tokens=600, timeout=150).strip()
            if repaired and not has_bad_placeholder(repaired):
                break
        analysis[f"q{i}"] = repaired if repaired else "该问题在论文中信息有限，基于摘要与正文可得出初步结论。"

    if not analysis.get("abstract_zh"):
        analysis["abstract_zh"] = translate_text(abstract_en)

    return analysis
