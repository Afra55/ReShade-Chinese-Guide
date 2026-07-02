#!/usr/bin/env python3
"""Download framedsc.com assets referenced by ReshadeGuides HTML and fix links."""

import os
import re
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path("/workspace")
BASE_URL = "https://framedsc.com"

HTML_GLOBS = [
    "ReshadeGuides/**/*.htm",
    "ReshadeGuidesShaderguides.htm",
    "ReshadeGuidesAddonguides.htm",
]

ASSET_PATTERNS = [
    re.compile(r'(?:src|href)=["\']([^"\']+)["\']', re.I),
    re.compile(r'url\(([^)]+)\)', re.I),
]


def collect_html_files():
    files = []
    for pattern in HTML_GLOBS:
        files.extend(ROOT.glob(pattern))
    return sorted(set(files))


def normalize_url(url: str, base_dir: str = "") -> str | None:
    url = url.strip().strip('"\'')
    if not url or url.startswith(("#", "mailto:", "javascript:")):
        return None
    if url.startswith("//"):
        url = "https:" + url
    if url.startswith("http://") or url.startswith("https://"):
        if "framedsc.com" not in url:
            return None
        parsed = urllib.parse.urlparse(url)
        path = parsed.path
    else:
        path = url.split("?")[0].split("#")[0]
        path = path.replace("\\", "/")
        if not path.startswith("/"):
            path = posix_join(base_dir, path)
    path = urllib.parse.unquote(path)
    path = path.replace("\\", "/")
    if path.startswith("/"):
        path = path[1:]
    parts = []
    for part in path.split("/"):
        if part in ("", "."):
            continue
        if part == "..":
            if parts:
                parts.pop()
            continue
        parts.append(part)
    if not parts:
        return None
    return "/".join(parts)


def posix_join(*parts: str) -> str:
    return "/".join(p.strip("/") for p in parts if p)


def download_file(rel_path: str) -> bool:
    dest = ROOT / rel_path
    if dest.exists() and dest.stat().st_size > 0:
        return True
    dest.parent.mkdir(parents=True, exist_ok=True)
    url = f"{BASE_URL}/{rel_path.replace(os.sep, '/')}"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = resp.read()
        dest.write_bytes(data)
        print(f"OK  {rel_path}")
        return True
    except Exception as exc:
        print(f"ERR {rel_path}: {exc}")
        return False


def extract_asset_paths(html: str, base_dir: str = "") -> set[str]:
    paths = set()
    for pattern in ASSET_PATTERNS:
        for match in pattern.findall(html):
            rel = normalize_url(match, base_dir)
            if rel:
                paths.add(rel)
    return paths


def rel_link(from_file: Path, target_rel: str) -> str:
    target = ROOT / target_rel
    return os.path.relpath(target, from_file.parent).replace("\\", "/")


LOCAL_ASSET_PREFIXES = (
    "css/",
    "js/",
    "Images/",
    "fontawesome/",
    "ShaderTogglers/",
)

LOCAL_HTML_FILES = {
    "ReshadeGuidesShaderguides.htm",
    "ReshadeGuidesAddonguides.htm",
}


def is_local_content(rel: str) -> bool:
    if rel == "favicon.ico" or rel in LOCAL_HTML_FILES:
        return True
    if rel.startswith("ReshadeGuides/"):
        return True
    return any(rel.startswith(prefix) for prefix in LOCAL_ASSET_PREFIXES)


EXTERNAL_NAV_PREFIXES = (
    "index.htm",
    "basics.htm",
    "Gameguides.htm",
    "GeneralGuides/",
    "PhotographyGuides/",
    "cheattablearchive.htm",
    "the_photomode_wishlist.htm",
    "inmemoriam.htm",
    "contribute.htm",
    "joinus.htm",
    "HallOfFramed",
    "HOFWallpaper",
    "framed-wrapped",
    "Docnet_search.htm",
)


def fix_external_nav_links(content: str) -> str:
    def repl(match):
        attr, url = match.group(1), match.group(2)
        if url.startswith(("http://", "https://", "#", "mailto:", "javascript:")):
            return match.group(0)
        if url.startswith("ReshadeGuides") or url in LOCAL_HTML_FILES:
            return match.group(0)
        if any(url == p or url.startswith(p) for p in EXTERNAL_NAV_PREFIXES):
            return f'{attr}="https://framedsc.com/{url.lstrip("/")}"'
        return match.group(0)

    return re.sub(r'(href|action)=["\']([^"\']+)["\']', repl, content, flags=re.I)


def rewrite_html(content: str, html_file: Path) -> str:
    base_dir = html_file.parent.relative_to(ROOT).as_posix()

    def repl_attr(match):
        attr, url = match.group(1), match.group(2)
        rel = normalize_url(url, base_dir)
        if not rel or not is_local_content(rel):
            return match.group(0)
        local = ROOT / rel
        if local.exists():
            return f'{attr}="{rel_link(html_file, rel)}"'
        return match.group(0)

    content = re.sub(
        r'(src|href)=["\']([^"\']+)["\']',
        repl_attr,
        content,
        flags=re.I,
    )

    def repl_css(match):
        url = match.group(1).strip().strip('"\'')
        rel = normalize_url(url, base_dir)
        if not rel or not is_local_content(rel):
            return match.group(0)
        local = ROOT / rel
        if local.exists():
            return f'url("{rel_link(html_file, rel)}")'
        return match.group(0)

    content = re.sub(r'url\(([^)]+)\)', repl_css, content, flags=re.I)
    if html_file.name in LOCAL_HTML_FILES:
        content = fix_external_nav_links(content)
    return content


def main():
    html_files = collect_html_files()
    all_assets: set[str] = set()

    for html_file in html_files:
        content = html_file.read_text(encoding="utf-8", errors="replace")
        base_dir = html_file.parent.relative_to(ROOT).as_posix()
        all_assets.update(extract_asset_paths(content, base_dir))

    # Always include shared site assets
    shared = [
        "css/theme_20250102.css",
        "css/theme_colors_20220814.css",
        "css/styles/vs.css",
        "fontawesome/css/brands.min.css",
        "fontawesome/css/fontawesome.min.css",
        "fontawesome/css/regular.min.css",
        "fontawesome/css/solid.min.css",
        "fontawesome/css/v4-font-face.min.css",
        "fontawesome/css/v4-shims.min.css",
        "js/jquery-2.1.1.min.js",
        "js/modernizr-2.8.3.min.js",
        "js/highlight.pack.js",
        "js/theme.js",
        "js/comparisons.js",
        "favicon.ico",
    ]
    all_assets.update(shared)

    # Filter to likely local assets only
    asset_list = sorted(
        p
        for p in all_assets
        if p
        and not p.endswith((".htm", ".html"))
        and not p.startswith("..")
        and "%5C" not in p
        and (ROOT / p).resolve().is_relative_to(ROOT.resolve())
    )

    print(f"Downloading {len(asset_list)} assets...")
    ok = 0
    for rel in asset_list:
        if download_file(rel):
            ok += 1
    print(f"Downloaded/verified {ok}/{len(asset_list)} assets")

    print("Rewriting HTML links...")
    for html_file in html_files:
        original = html_file.read_text(encoding="utf-8", errors="replace")
        updated = rewrite_html(original, html_file)
        if updated != original:
            html_file.write_text(updated, encoding="utf-8")
            print(f"Updated {html_file.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
