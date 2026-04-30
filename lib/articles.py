"""嵐海知識｜知識庫文章載入器

文章存於 content/articles/*.md，每篇 markdown 檔以 YAML frontmatter 描述：

---
title: 文章標題
slug: file-name-slug-must-match-filename-stem
category: 文獻檢索
tags: [WoS, AND-OR]
date: 2026-04-30
summary: 一句話摘要（卡片預覽用）
author: 嵐嵐
read_time: 5
---

正文（markdown）...
"""

from __future__ import annotations
import frontmatter
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


CONTENT_DIR = Path(__file__).resolve().parent.parent / "content" / "articles"


@dataclass
class Article:
    slug: str
    title: str
    category: str
    tags: list[str]
    date: str
    summary: str
    author: str
    read_time: int
    body: str

    @property
    def date_label(self) -> str:
        return self.date


def _parse(path: Path) -> Article:
    post = frontmatter.load(path)
    meta = post.metadata
    return Article(
        slug=str(meta.get("slug", path.stem)),
        title=str(meta.get("title", path.stem)),
        category=str(meta.get("category", "未分類")),
        tags=list(meta.get("tags", []) or []),
        date=str(meta.get("date", "")),
        summary=str(meta.get("summary", "")),
        author=str(meta.get("author", "嵐嵐")),
        read_time=int(meta.get("read_time", 5)),
        body=post.content,
    )


def list_articles() -> list[Article]:
    if not CONTENT_DIR.exists():
        return []
    items = [_parse(p) for p in CONTENT_DIR.glob("*.md")]
    items.sort(key=lambda a: a.date, reverse=True)
    return items


def get_article(slug: str) -> Article | None:
    for art in list_articles():
        if art.slug == slug:
            return art
    return None


def list_categories(articles: Iterable[Article] | None = None) -> list[str]:
    arts = list(articles) if articles is not None else list_articles()
    cats: list[str] = []
    for a in arts:
        if a.category not in cats:
            cats.append(a.category)
    return sorted(cats)
