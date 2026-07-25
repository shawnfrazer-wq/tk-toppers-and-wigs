#!/usr/bin/env python3
"""
Static-HTML build script for the Tatiana Karelina Toppers & Wigs site.

Reads:
- src-html/partials/     shared HTML fragments (head, nav, footer, foot)
- src-html/pages/        page source files with {{HEAD}} / {{NAV}} /
                         {{FOOTER}} / {{FOOT}} markers, and a leading
                         HTML comment block carrying title / description /
                         path metadata.
- src-html/css/          stylesheet
- src-html/fonts/        self-hosted WOFF2 files
- ../public/images/      photography (source of truth, kept from Next build)
- ../public/brand/       logo + wordmarks

Writes:
- dist/                  final static site — pure standalone HTML.
                         This folder is handed to Pontifex for WordPress
                         conversion.

Zero dependencies (stdlib only). Run:
    python3 src-html/build.py
"""

from __future__ import annotations
import re
import shutil
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent            # site/src-html
SITE_ROOT = ROOT.parent                            # site/
SRC = ROOT
DIST = SITE_ROOT / "dist"
PARTIALS = SRC / "partials"
PAGES = SRC / "pages"
CSS = SRC / "css"
FONTS = SRC / "fonts"
PUBLIC = SITE_ROOT / "public"


def read(p: Path) -> str:
    return p.read_text(encoding="utf-8")


META_RE = re.compile(
    r"<!--\s*META\s*:\s*(.*?)-->",
    re.DOTALL | re.IGNORECASE,
)


def parse_meta(html: str) -> dict:
    """Extract the leading `<!-- META: ... -->` comment block into a dict.
    Supported fields: title, description, path.
    """
    m = META_RE.search(html)
    if not m:
        return {"title": "", "description": "", "path": "/"}
    body = m.group(1)
    out: dict = {}
    for line in body.splitlines():
        line = line.strip()
        if not line or ":" not in line:
            continue
        k, _, v = line.partition(":")
        out[k.strip().lower()] = v.strip()
    out.setdefault("title", "")
    out.setdefault("description", "")
    out.setdefault("path", "/")
    return out


def strip_meta(html: str) -> str:
    return META_RE.sub("", html, count=1).lstrip()


def render(page_html: str, partials: dict) -> str:
    """Substitute {{HEAD}}, {{NAV}}, {{FOOTER}}, {{FOOT}} + META fields."""
    meta = parse_meta(page_html)
    body = strip_meta(page_html)

    year = str(date.today().year)

    head = partials["head"] \
        .replace("{{TITLE}}", meta["title"]) \
        .replace("{{DESCRIPTION}}", meta["description"]) \
        .replace("{{PATH}}", meta["path"])
    footer = partials["footer"].replace("{{YEAR}}", year)

    body = body \
        .replace("{{HEAD}}", head) \
        .replace("{{NAV}}", partials["nav"]) \
        .replace("{{FOOTER}}", footer) \
        .replace("{{FOOT}}", partials["foot"])
    return body


def load_partials() -> dict:
    return {
        "head":   read(PARTIALS / "head.html"),
        "nav":    read(PARTIALS / "nav.html"),
        "footer": read(PARTIALS / "footer.html"),
        "foot":   read(PARTIALS / "foot.html"),
    }


def build_pages(partials: dict) -> list[Path]:
    out_paths: list[Path] = []
    for page in PAGES.rglob("*.html"):
        rel = page.relative_to(PAGES)
        out = DIST / rel
        out.parent.mkdir(parents=True, exist_ok=True)
        html = render(read(page), partials)
        out.write_text(html, encoding="utf-8")
        out_paths.append(out)
    return out_paths


ABS_ATTR_RE = re.compile(r'(href|src|action)="(/[^"]*)"')


def relativize_links(dist: Path) -> int:
    """Rewrite root-absolute hrefs/srcs ("/foo/bar") into relative paths so
    every page can be opened directly via file:// (double-click index.html)
    and still navigate the whole site, with no server required.

    Directory-style links ("/", "/toppers/") get an explicit "index.html"
    appended, since file:// has no server to auto-resolve a bare directory.

    Leaves alone: protocol-relative ("//example.com/...") and anything that
    isn't a bare root-absolute path (absolute https:// URLs, mailto:, tel:,
    in-page #anchors never match this regex at all).
    """
    n = 0
    for page in dist.rglob("*.html"):
        rel = page.relative_to(dist)
        depth = len(rel.parts) - 1  # how many dirs deep this file lives
        prefix = "../" * depth

        def _sub(m: re.Match) -> str:
            attr, path = m.group(1), m.group(2)
            if path.startswith("//"):
                return m.group(0)  # protocol-relative external URL, leave it
            rel_path = path.lstrip("/")
            if path.endswith("/"):
                rel_path += "index.html"
            return f'{attr}="{prefix}{rel_path}"'

        html = read(page)
        new_html, count = ABS_ATTR_RE.subn(_sub, html)
        if count:
            page.write_text(new_html, encoding="utf-8")
            n += count
    return n


def copy_tree(src: Path, dst: Path, exclude_dirs=()) -> int:
    if not src.exists():
        return 0
    if dst.exists():
        shutil.rmtree(dst)
    ignore = shutil.ignore_patterns(*exclude_dirs) if exclude_dirs else None
    shutil.copytree(src, dst, ignore=ignore)
    return sum(1 for _ in dst.rglob("*") if _.is_file())


def main() -> int:
    if DIST.exists():
        shutil.rmtree(DIST)
    DIST.mkdir(parents=True)

    partials = load_partials()
    pages = build_pages(partials)

    copy_tree(CSS, DIST / "css")
    copy_tree(FONTS, DIST / "fonts")
    # "real" holds raw, unoptimized source photography kept for reference/re-export
    # only — no page references /images/real/*, so exclude it from the shipped bundle.
    n_images = copy_tree(PUBLIC / "images", DIST / "images", exclude_dirs=("real",))
    n_brand = copy_tree(PUBLIC / "brand", DIST / "brand")

    n_root_files = 0
    for name in ("sitemap.xml", "robots.txt", "favicon.ico"):
        src = PUBLIC / name
        if src.exists():
            shutil.copy2(src, DIST / name)
            n_root_files += 1

    n_relinked = relativize_links(DIST)

    print(f"built {len(pages)} pages, {n_images} images, {n_brand} brand assets, {n_root_files} root files → {DIST}")
    print(f"relativized {n_relinked} links so the folder opens standalone via file:// (no server needed)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
