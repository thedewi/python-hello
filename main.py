import argparse
from pathlib import Path

from pyfiglet import figlet_format


def main():
    parser = argparse.ArgumentParser(
        description="Render a file's contents as ASCII art."
    )
    parser.add_argument("file", help="path to the file to render")
    args = parser.parse_args()

    print(figlet_format(Path(args.file).read_text()), end="")


if __name__ == "__main__":
    main()
