import unittest
from pathlib import Path

from file_organizer import get_category


class GetCategoryTests(unittest.TestCase):
    def test_file_with_extension(self):
        self.assertEqual(get_category(Path("notes.txt")), "txt")

    def test_file_with_multiple_dots(self):
        self.assertEqual(get_category(Path("backup.2026.zip")), "zip")

    def test_file_without_extension(self):
        self.assertEqual(get_category(Path("README")), "no_extension")


if __name__ == "__main__":
    unittest.main()