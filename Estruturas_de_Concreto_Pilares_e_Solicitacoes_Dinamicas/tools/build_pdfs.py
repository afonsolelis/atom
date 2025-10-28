#!/usr/bin/env python3
import os
import subprocess
import sys
from pathlib import Path
import tempfile


def preprocess_math_blocks(text: str) -> str:
    # Replace standalone "$" lines with "$$" for block math
    lines = text.splitlines()
    for i, line in enumerate(lines):
        if line.strip() == "$":
            lines[i] = "$$"
    return "\n".join(lines) + ("\n" if not text.endswith("\n") else "")


def find_markdown_files(root: Path) -> list[Path]:
    files: list[Path] = []
    for unidade in sorted(p for p in root.iterdir() if p.is_dir() and p.name.startswith("unidade_")):
        for md in sorted(unidade.glob("*.md")):
            files.append(md)
    return files


def compile_to_pdf(md_path: Path, out_root: Path) -> bool:
    rel_dir = md_path.parent.name
    out_dir = out_root / rel_dir
    out_dir.mkdir(parents=True, exist_ok=True)
    out_pdf = out_dir / (md_path.stem + ".pdf")

    # Read and preprocess content
    text = md_path.read_text(encoding="utf-8")
    processed = preprocess_math_blocks(text)

    # Write to temp file
    with tempfile.NamedTemporaryFile("w", suffix=md_path.name, delete=False, encoding="utf-8") as tf:
        tf.write(processed)
        temp_path = tf.name

    # Build resource-path to find local assets
    resource_path = os.pathsep.join([
        str(md_path.parent),
        str(md_path.parent / "assets"),
        str(Path.cwd()),
        str(Path.cwd() / "assets"),
    ])

    # Try with a Unicode-capable font to avoid missing sub/superscript warnings
    pdf_engine_args = ["--pdf-engine=xelatex", "-V", "mainfont=DejaVu Serif"]

    cmd = [
        "pandoc",
        temp_path,
        "-f",
        "markdown-yaml_metadata_block+tex_math_dollars",
        "--resource-path",
        resource_path,
        "-o",
        str(out_pdf),
    ] + pdf_engine_args

    try:
        subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        ok = True
    except subprocess.CalledProcessError as e:
        # Retry without font override if it failed due to font availability
        cmd_fallback = [
            "pandoc",
            temp_path,
            "-f",
            "markdown-yaml_metadata_block+tex_math_dollars",
            "--resource-path",
            resource_path,
            "--pdf-engine=xelatex",
            "-o",
            str(out_pdf),
        ]
        try:
            subprocess.run(cmd_fallback, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            ok = True
        except subprocess.CalledProcessError:
            sys.stderr.write(f"Failed to compile {md_path}\n")
            ok = False
    finally:
        try:
            os.remove(temp_path)
        except OSError:
            pass

    return ok


def main() -> int:
    repo_root = Path.cwd()
    out_root = repo_root / "pdfs"
    out_root.mkdir(parents=True, exist_ok=True)

    md_files = find_markdown_files(repo_root)
    if not md_files:
        print("No Markdown files found under unidades.")
        return 0

    ok_all = True
    for md in md_files:
        print(f"[build] {md}")
        if not compile_to_pdf(md, out_root):
            ok_all = False

    return 0 if ok_all else 1


if __name__ == "__main__":
    raise SystemExit(main())
