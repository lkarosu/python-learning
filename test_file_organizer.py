import unittest
from pathlib import Path
import json
from tempfile import TemporaryDirectory
from file_organizer import get_category, organize_files, write_report, create_status_summary



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

            results = organize_files(source_dir, apply=True)

            write_report(source_dir, apply=True, results=results)

            report_path = source_dir / "organizer_report.json"
            report = json.loads(report_path.read_text(encoding="utf-8"))
            self.assertEqual(report["summary"]["skipped"], 1)
            self.assertTrue(source_file.exists())
            self.assertEqual(target_file.read_text(encoding="utf-8"), "旧内容")

    def test_apply_moves_file(self):
        with TemporaryDirectory() as temp_dir:
            source_dir = Path(temp_dir)
            source_file = source_dir / "report.pdf"
            source_file.write_text("测试内容", encoding="utf-8")

            results = organize_files(source_dir, apply=True)

            write_report(source_dir, apply=True, results=results)

            report_path = source_dir / "organizer_report.json"
            report = json.loads(report_path.read_text(encoding="utf-8"))
            self.assertEqual(report["summary"], {"preview": 0, "moved": 1, "skipped": 0, "error": 0})
            self.assertFalse(source_file.exists())
            self.assertTrue((source_dir / "pdf" / "report.pdf").exists())

    def test_write_preview_report(self):
        with TemporaryDirectory() as temp_dir:
            source_dir = Path(temp_dir)
            results = [
                {
                    "source": "notes.txt",
                    "target": "txt/notes.txt",
                    "status": "preview",
                },
                {
                    "source": "notes.txt",
                    "target": "txt/notes.txt",
                    "status": "preview",
                },       
            ]

            write_report(source_dir, apply=False, results=results)

            report_path = source_dir / "organizer_report.json"
            report = json.loads(report_path.read_text(encoding="utf-8"))

            self.assertEqual(report["mode"], "preview")
            self.assertEqual(report["results"], results)
            self.assertEqual(report["summary"], {"preview": 2, "moved": 0, "skipped": 0, "error": 0})

    def test_create_status_summary(self):
        results = [
            {"status": "preview"},
            {"status": "moved"},
            {"status": "skipped"},
            {"status": "error"},
        ]
        expected_summary = {"preview": 1, "moved": 1, "skipped": 1, "error": 1}

        self.assertEqual(create_status_summary(results), expected_summary)

    def test_organize_files_with_existing_non_directory_target(self):
        with TemporaryDirectory() as temp_dir:
            source_dir = Path(temp_dir)

            # 创建一个普通文件而不是目录
            category_file = source_dir / "txt"
            category_file.write_text("这是一个普通文件，而不是目录。", encoding="utf-8")

            source_file = source_dir / "notes.txt"
            source_file.write_text("学习笔记", encoding="utf-8")

            results = organize_files(source_dir, apply=True)

            write_report(source_dir, apply=True, results=results)

            report_path = source_dir / "organizer_report.json"
            report = json.loads(report_path.read_text(encoding="utf-8"))

            self.assertEqual(report["summary"]["error"], 1)
            self.assertTrue(source_file.exists())
            self.assertTrue(category_file.exists())
            # 两个文件的文本内容未变
            self.assertEqual(category_file.read_text(encoding="utf-8"), "这是一个普通文件，而不是目录。")
            self.assertEqual(source_file.read_text(encoding="utf-8"), "学习笔记")

            statuses = {result["source"]: result["status"] for result in results}
            self.assertEqual(statuses, {"notes.txt": "error", "txt": "skipped"})
            self.assertEqual(
                report["summary"],
                {"preview": 0, "moved": 0, "skipped": 1, "error": 1},
            )

if __name__ == "__main__":
    unittest.main()