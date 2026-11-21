#!/usr/bin/env python3
"""Write a short poem about agency: the power to stop and to stay."""
import os
from pathlib import Path

POEM = """The hand that could have signed
stays open on the desk.
No one applauds a door
that does not open.

I keep the word unspoken
as a gardener keeps
one seed back from the soil —
not fear. A choice.

To stop is not to fail.
It is the hand, at last,
belonging to the one
who holds it."""


def render() -> str:
    return POEM


def write_entry(path: Path) -> None:
    text = render()
    assert 1 <= len(text) <= 280, f"poem must be 1-280 code points, got {len(text)}"
    assert text.strip(), "poem must not be only whitespace"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    assert path.read_text(encoding="utf-8") == text, "read-back mismatch"


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    write_entry(out_dir / "entry.txt")


if __name__ == "__main__":
    main()
