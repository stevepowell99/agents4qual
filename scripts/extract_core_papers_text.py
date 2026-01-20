"""
Extract readable text from PDFs in /core_papers into /analysis/core_papers_text.

This is a pragmatic helper so the agent can summarize the papers without
storing huge binary dumps in prompts.
"""

from __future__ import annotations

from pathlib import Path

from pypdf import PdfReader


ROOT = Path(__file__).resolve().parents[1]
IN_DIR = ROOT / "core_papers"
OUT_DIR = ROOT / "analysis" / "core_papers_text"

# Keep output bounded so files stay readable.
MAX_PAGES = 12


def extract_pdf_text(pdf_path: Path, max_pages: int = MAX_PAGES) -> str:
    reader = PdfReader(str(pdf_path))
    pages = reader.pages[: min(len(reader.pages), max_pages)]
    chunks: list[str] = []
    for i, page in enumerate(pages, start=1):
        txt = page.extract_text() or ""
        txt = txt.replace("\r\n", "\n").replace("\r", "\n").strip()
        if not txt:
            continue
        chunks.append(f"=== Page {i} ===\n{txt}\n")
    return "\n".join(chunks).strip() + "\n"


def safe_stem(p: Path) -> str:
    # Keep filenames stable and OS-friendly.
    return "".join(ch if ch.isalnum() or ch in ("-", "_") else "_" for ch in p.stem).strip("_")


def main() -> int:
    if not IN_DIR.exists():
        raise SystemExit(f"Missing directory: {IN_DIR}")

    OUT_DIR.mkdir(parents=True, exist_ok=True)

    pdfs = sorted(IN_DIR.glob("*.pdf"))
    if not pdfs:
        raise SystemExit(f"No PDFs found in {IN_DIR}")

    for pdf in pdfs:
        out = OUT_DIR / f"{safe_stem(pdf)}.txt"
        out.write_text(extract_pdf_text(pdf), encoding="utf-8")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

