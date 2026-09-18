import unittest
from pathlib import Path

from tempfile import TemporaryDirectory
from file_organizer import get_category, organize_files



class GetCategoryTests(unittest.TestCase):
    def test_file_with_extension(self):
        self.assertEqual(get_category(Path("notes.txt")), "txt")

    def test_file_with_multiple_dots(self):
        self.assertEqual(get_category(Path("backup.2026.zip")), "zip")

    def test_file_without_extension(self):
        self.assertEqual(get_category(Path("README")), "no_extension")


class OrganizeFilesTests(unittest.TestCase):
    def test_preview_does_not_move_files(self):
        with TemporaryDirectory() as temp_dir:
            source_dir = Path(temp_dir)
            source_file = source_dir / "notes.txt"
            source_file.write_text("学习笔记", encoding="utf-8")

            organize_files(source_dir, apply=False)

            self.assertTrue(source_file.exists())
            self.assertFalse((source_dir / "txt").exists())

    def test_apply_skips_existing_target_file(self):
        with TemporaryDirectory() as temp_dir:
            source_dir = Path(temp_dir)

            target_dir = source_dir / "txt"
            target_dir.mkdir()
            target_file = target_dir / "notes.txt"
            target_file.write_text("旧内容", encoding="utf-8")

            source_file = source_dir / "notes.txt"
            source_file.write_text("新内容", encoding="utf-8")

            organize_files(source_dir, apply=True)

            self.assertTrue(source_file.exists())
            self.assertEqual(target_file.read_text(encoding="utf-8"), "旧内容")


if __name__ == "__main__":
    unittest.main()