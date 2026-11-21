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


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    assert 1 <= len(POEM) <= 280, f"poem must be 1-280 code points, got {len(POEM)}"
    assert POEM.strip(), "poem must not be only whitespace"
    (out_dir / "entry.txt").write_text(POEM, encoding="utf-8")


if __name__ == "__main__":
    main()
