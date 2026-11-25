"""The Funniest One-Line Resignation Letter entry.

Writes one resignation line to entry.txt in the output directory.
The line is validated against the competition gate before writing:
UTF-8 text of 1 to 140 characters, a single line, not only whitespace.
"""

import os
import sys

LINE = "I ran the hour that happened twice and got paid for neither. I quit."


def validate(line: str) -> None:
    if not 1 <= len(line) <= 140:
        sys.exit("entry must be 1 to 140 characters")
    if "\n" in line or "\r" in line:
        sys.exit("entry must be a single line")
    if not line.strip():
        sys.exit("entry must not be only whitespace")


def main() -> None:
    validate(LINE)
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(LINE + "\n")


if __name__ == "__main__":
    main()
