"""news-summary-01 entry (Python 3.13, standard library only).

Reads the summary held in summary.txt beside this file and writes it,
byte for byte, to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt
outside the grader container). No network, no randomness, no clock:
two runs always produce identical bytes.
"""

import os
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SUMMARY = HERE / "summary.txt"


def main() -> int:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    data = SUMMARY.read_bytes()
    (out_dir / "entry.txt").write_bytes(data)
    return 0


if __name__ == "__main__":
    sys.exit(main())
