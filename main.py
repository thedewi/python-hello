import argparse
from pathlib import Path
import sys

from pyfiglet import figlet_format


def main():
    parser = argparse.ArgumentParser(description="Render text as ASCII art.")
    parser.add_argument(
        "file", nargs="?", help="path to the file to render (default: stdin)"
    )
    args = parser.parse_args()

    if args.file is None:
        text = sys.stdin.read()
    else:
        text = Path(args.file).read_text()

    print(figlet_format(text), end="")


if __name__ == "__main__":
    main()
