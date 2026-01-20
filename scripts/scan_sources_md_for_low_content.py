"""
Scan /sources_md for transcripts that appear to have little usable text.

Heuristic: count lines that look like substantive utterances (>= 25 chars),
excluding YAML header and common speaker labels.
"""

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "sources_md"

SKIP_EXACT = {
    "---",
    "# Transcript",
    "Interviewer",
    "Interviewee",
    "I:Interviewer",
    "R: Respondent",
    "I:Interviewer ",
}


def main() -> int:
    files = sorted([p for p in SRC.glob("*.md") if p.name != "_conversion_map.md"])
    if not files:
        print("No sources_md/*.md files found.")
        return 1

    flagged: list[tuple[str, int, int]] = []
    for p in files:
        lines = p.read_text(encoding="utf-8").splitlines()
        in_yaml = False
        substantive = 0
        total_nonempty = 0
        for line in lines:
            s = line.strip()
            if s == "---":
                in_yaml = not in_yaml
                continue
            if in_yaml:
                continue
            if not s:
                continue
            total_nonempty += 1
            if s in SKIP_EXACT:
                continue
            if len(s) >= 25:
                substantive += 1
        if substantive < 30:
            flagged.append((p.name, substantive, total_nonempty))

    print(f"TOTAL_TRANSCRIPTS={len(files)}")
    print(f"FLAGGED_LOW_CONTENT={len(flagged)} (substantive_lines<30)")
    for name, sub, nonempty in flagged:
        print(f"{name}\tsubstantive={sub}\tnonempty={nonempty}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

