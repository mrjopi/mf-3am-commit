"""Entry for make.fun "The 3AM Commit Message" (u-kiencx-the-3am-commit-message-10bc7b35).

Writes the single entry line to /output/entry.txt.
The line is the whole entry: one line, under the contest's character limit.
"""
import os

LINE = 'fix: reverted my fix — the bug was load-bearing and honestly doing a better job than me'

def main() -> None:
    out_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
