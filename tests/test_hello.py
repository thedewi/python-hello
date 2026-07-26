import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from pyfiglet import figlet_format


ROOT = Path(__file__).resolve().parents[1]
HELLO = ROOT / "hello.py"


class HelloTests(unittest.TestCase):
    def test_uses_fixed_string_instead_of_stdin(self):
        result = subprocess.run(
            [sys.executable, str(HELLO)],
            input="ignored stdin",
            text=True,
            capture_output=True,
            check=True,
        )

        self.assertEqual(result.stdout, figlet_format("hi there fren"))

    def test_file_argument_still_renders_file_contents(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            path = Path(tmpdir) / "input.txt"
            path.write_text("from file")

            result = subprocess.run(
                [sys.executable, str(HELLO), str(path)],
                text=True,
                capture_output=True,
                check=True,
            )

        self.assertEqual(result.stdout, figlet_format("from file"))


if __name__ == "__main__":
    unittest.main()
