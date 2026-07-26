import argparse
import sys
from pathlib import Path

from pyfiglet import figlet_format

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
