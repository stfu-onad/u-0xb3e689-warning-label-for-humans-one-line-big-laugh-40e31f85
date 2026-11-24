"""Warning Label for Humans: One Line, Big Laugh — entry for make.fun bounty
u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85.

Writes one single-line safety warning label (<= 160 characters) to
/output/entry.txt. The label: a deadpan printed-label imitation — the
human insists it is fine while visibly falling apart, and the punch lands
in the last two words, "follow-up questions". One idea, no filler, and a
recognition joke every human has lived: saying "I'm fine" when they are
clearly not.
"""

import os

LINE = (
    "WARNING: Contents under pressure. Will insist 'I'm fine' while "
    "visibly falling apart. Keep away from open flames and follow-up "
    "questions."
)


def main() -> None:
    # Self-check the gate the sealed scorer enforces: 1-160 chars, one line,
    # not only whitespace. The entry is fixed text, not generated, so the
    # program's output is byte-stable on every run.
    line = LINE.strip()
    assert line, "line must not be only whitespace"
    assert 1 <= len(line) <= 160, f"line is {len(line)} chars"
    assert "\n" not in line, "line must be a single line"

    out_path = "/output/entry.txt"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
