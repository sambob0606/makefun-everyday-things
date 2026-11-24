#!/usr/bin/env python3
"""Everyday Things, Two Lines — make.fun entry.

Writes the two-line explanation to /output/entry.txt.
Stdlib only. Line 1 explains a toaster to a 10-year-old with one
concrete analogy; line 2 says what the analogy maps and what it
leaves out.
"""

import os

LINE_1 = (
    "A toaster is a tiny elevator that lowers your bread into glowing "
    "heat and pops it back up brown and crunchy."
)

LINE_2 = (
    "The elevator maps the trip down, the heating, and the pop back up, "
    "but it leaves out that the heat comes from thin electric wires, not "
    "a furnace or a fire, and that only the outside browns while the "
    "middle stays soft."
)

ENTRY = LINE_1 + "\n" + LINE_2 + "\n"


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote {path} ({len(ENTRY.encode('utf-8'))} bytes)")


if __name__ == "__main__":
    main()
