"""Write a short poem about stopping to /output/entry.txt."""

import os

POEM = """The hand could sign — it doesn't.
Open on the desk, palm up
paper waits; pen untouched.

No one applauds a door that stays shut,
no one cheers the word held back—
one seed kept from soil.

Stopping is not failing.
It is choosing where weight rests.
The hand is mine at last.
"""


def render():
    return POEM


def write_entry(path):
    text = render()
    assert 1 <= len(text) <= 280, "poem must be 1-280 code points"
    assert text.strip(), "poem must not be only whitespace"
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    with open(path, encoding="utf-8") as f:
        assert f.read() == text, "read-back mismatch"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    write_entry(os.path.join(out_dir, "entry.txt"))


if __name__ == "__main__":
    main()
