import pathlib
import subprocess
import unittest


QUINE = pathlib.Path(__file__).with_name("quine.py")


class QuineTest(unittest.TestCase):
    def test_prints_own_source(self) -> None:
        result = subprocess.run(
            ["python3", str(QUINE)],
            check=True,
            capture_output=True,
        )
        self.assertEqual(result.stdout, QUINE.read_bytes())
        self.assertEqual(result.stderr, b"")


if __name__ == "__main__":
    unittest.main()
