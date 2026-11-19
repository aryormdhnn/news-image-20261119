"""news-image-20261119: publish this entry's front page as the program output.

The repository holds entry.png (1024x1024, the world-news front page for
Thursday 19 November 2026). The grader runs this program twice in a sandbox
with no network; both runs must write the same bytes, so all this program
does is copy the image, byte for byte, into the output directory. A copy
preserves the bytes exactly, so the two grader runs agree with each other
and with the file in this repository.

Local run:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
import shutil
import sys


def main() -> int:
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, "entry.png")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(source, os.path.join(out_dir, "entry.png"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
