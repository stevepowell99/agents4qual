from __future__ import annotations

import re
from pathlib import Path


def count_words(s: str) -> int:
    # Simple heuristic word tokenizer; good enough for limit checks.
    return len(re.findall(r"[A-Za-z0-9][A-Za-z0-9'-]*", s))


def main() -> int:
    t = Path("paper_submission.md").read_text(encoding="utf-8")
    print("TOTAL_WORDS", count_words(t))

    before_refs = t.split("## References", 1)[0]
    print("WORDS_BEFORE_REFERENCES", count_words(before_refs))

    if "## Author reflection" in t:
        pre_ref = t.split("## Author reflection", 1)[0]
        main_excl = pre_ref.split("## References", 1)[0]
        print("MAIN_TEXT_WORDS_EXCL_REFS_REFLECTION", count_words(main_excl))

        reflection = t.split("## Author reflection", 1)[1]
        reflection_text = reflection.split("## AI involvement checklist", 1)[0]
        print("REFLECTION_WORDS", count_words(reflection_text))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

