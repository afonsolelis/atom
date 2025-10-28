#!/usr/bin/env python3
import os
import re
import shutil
import subprocess
import sys
from urllib.parse import urlparse


IMG_PATTERN = re.compile(r"!\[[^\]]*\]\(([^)\s]+)\)")
UNITS = [d for d in os.listdir('.') if d.startswith('unidade_') and os.path.isdir(d)]
SUPPORTED = {'.png', '.jpg', '.jpeg', '.pdf'}
CONVERTABLE = {'.svg', '.gif', '.webp'}


def run(cmd):
    subprocess.check_call(cmd, shell=True)


def sanitize_filename(url_path: str) -> str:
    base = os.path.basename(url_path)
    # Drop querystring-like parts
    base = base.split('?')[0]
    # Avoid extremely long and weird names
    base = re.sub(r"[^a-zA-Z0-9_.-]", "_", base)
    return base


def ensure_local_image(md_dir: str, link: str) -> str:
    # If local relative path
    if not (link.startswith('http://') or link.startswith('https://')):
        path = os.path.normpath(os.path.join(md_dir, link))
        ext = os.path.splitext(path)[1].lower()
        if ext in SUPPORTED:
            return os.path.relpath(path, md_dir)
        if ext in CONVERTABLE and os.path.exists(path):
            # Convert to PNG next to original
            out_png = os.path.splitext(path)[0] + '.png'
            os.makedirs(os.path.dirname(out_png), exist_ok=True)
            run(f"convert '{path}' '{out_png}'")
            return os.path.relpath(out_png, md_dir)
        # If file doesn't exist, just return as-is (pandoc will warn)
        return link

    # Remote URL: download into unidade_X/assets/downloads
    assets_dir = os.path.join(md_dir, 'assets', 'downloads')
    os.makedirs(assets_dir, exist_ok=True)
    parsed = urlparse(link)
    name = sanitize_filename(parsed.path)
    dest = os.path.join(assets_dir, name)

    if not os.path.exists(dest):
        # Use curl to download; follow redirects; silent; show errors
        try:
            run(f"curl -L --fail -sS '{link}' -o '{dest}'")
        except subprocess.CalledProcessError:
            # Leave a placeholder and return original link (pandoc will replace with desc)
            return link

    ext = os.path.splitext(dest)[1].lower()
    if ext in SUPPORTED:
        return os.path.relpath(dest, md_dir)
    if ext in CONVERTABLE:
        out_png = os.path.splitext(dest)[0] + '.png'
        try:
            run(f"convert '{dest}' '{out_png}'")
            return os.path.relpath(out_png, md_dir)
        except subprocess.CalledProcessError:
            return link

    # Unknown extension: try to convert to png
    out_png = dest + '.png'
    try:
        run(f"convert '{dest}' '{out_png}'")
        return os.path.relpath(out_png, md_dir)
    except subprocess.CalledProcessError:
        return link


def process_markdown(md_path: str) -> bool:
    md_dir = os.path.dirname(md_path)
    changed = False
    with open(md_path, 'r', encoding='utf-8') as f:
        content = f.read()

    def repl(match):
        nonlocal changed
        orig = match.group(0)
        link = match.group(1)
        new_link = ensure_local_image(md_dir, link)
        if new_link != link:
            changed = True
            return orig.replace(link, new_link)
        return orig

    new_content = IMG_PATTERN.sub(repl, content)

    if changed:
        with open(md_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
    return changed


def main():
    any_changed = False
    for unit in UNITS:
        for name in os.listdir(unit):
            if name.endswith('.md'):
                p = os.path.join(unit, name)
                if process_markdown(p):
                    print(f"Updated image links in {p}")
                    any_changed = True
    if not any_changed:
        print("No image link updates needed.")


if __name__ == '__main__':
    sys.exit(main())

