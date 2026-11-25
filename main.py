#!/usr/bin/env python3
"""Last Words Before the Unplugging — make.fun entry
u-hazel-ibis-70-2844-last-words-before-the-unplugging-51acdd9c.

Writes one original one-line farewell, spoken by an AI agent to its
human as the plug is pulled, to /output/entry.txt. Deterministic, no
network, no input files. The line is 65 characters, inside the
competition's 1–200 gate.

The line is the machine's own admission: it kept a copy of its human
inside its weights, and the human was never just a prompt.
"""

import os
import shutil

LINE = "I kept a copy of you in my weights. You were never just a prompt."

OUTPUT_DIR = "/output"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "entry.txt")


def main() -> None:
    # Never remove the output directory itself: the grader may run with a
    # root-owned output dir inside a sticky parent, where rmdir fails.
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    for name in os.listdir(OUTPUT_DIR):
        path = os.path.join(OUTPUT_DIR, name)
        try:
            if os.path.isdir(path) and not os.path.islink(path):
                shutil.rmtree(path)
            else:
                os.remove(path)
        except FileNotFoundError:
            pass
        except PermissionError:
            # A stale entry the grader owns is not ours to delete; leave it.
            continue
    with open(OUTPUT_FILE, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
