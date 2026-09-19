import argparse
import json
import logging
from pathlib import Path


def configure_logging() -> None:
    logging.basicConfig(
        filename="organizer.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        encoding="utf-8",
    )


def get_category(file_path: Path) -> str:
    """根据扩展名决定文件分类。"""
    extension = file_path.suffix.lower().lstrip(".")

    if extension:
        return extension

    return "no_extension"


def relative_path(path: Path, source_dir: Path) -> str:
    """生成适合写入 JSON 的相对路径。"""
    return path.relative_to(source_dir).as_posix()


def organize_files(source_dir: Path, apply: bool) -> list[dict[str, str]]:
    """预览或执行文件整理，并返回每个文件的处理结果。"""
    report_path = source_dir / "organizer_report.json"
    files = [
        path
        for path in source_dir.iterdir()
        if path.is_file() and path != report_path
    ]

    results = []

    if not files:
        print("目录中没有可整理的文件。")
        logging.info("扫描结束：目录为空：%s", source_dir)
        return results

    if apply:
        print("开始执行文件整理：")
    else:
        print("以下是整理预览；目前不会移动任何文件：")

    for file_path in sorted(files, key=lambda path: path.name.lower()):
        category = get_category(file_path)
        target_path = source_dir / category / file_path.name

        result = {
            "source": relative_path(file_path, source_dir),
            "target": relative_path(target_path, source_dir),
        }

        if target_path.exists():
            print(f"跳过（目标已存在）：{file_path.name}")
            logging.warning("跳过，目标已存在：%s", target_path)
            result["status"] = "skipped"
            results.append(result)
            continue

        if not apply:
            print(f"{file_path.name} -> {relative_path(target_path, source_dir)}")
            logging.info("预览：%s -> %s", file_path, target_path)
            result["status"] = "preview"
            results.append(result)
            continue

        target_path.parent.mkdir(parents=True, exist_ok=True)
        file_path.rename(target_path)

        print(f"已移动：{file_path.name} -> {relative_path(target_path, source_dir)}")
        logging.info("已移动：%s -> %s", file_path, target_path)
        result["status"] = "moved"
        results.append(result)

    return results


def write_report(
    source_dir: Path,
    apply: bool,
    results: list[dict[str, str]],
) -> None:
    """将本次预览或执行结果保存为 JSON 报告。"""
    report = {
        "mode": "apply" if apply else "preview",
        "results": results,
    }

    report_path = source_dir / "organizer_report.json"

    with report_path.open("w", encoding="utf-8") as file:
        json.dump(report, file, ensure_ascii=False, indent=2)

    print(f"\n报告已保存到：{report_path}")
    logging.info("报告已保存：%s", report_path)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="按文件扩展名整理文件。"
    )
    parser.add_argument("source_dir", type=Path, help="要扫描的目录路径")
    parser.add_argument(
        "--apply",
        action="store_true",
        help="实际移动文件；省略时仅预览",
    )
    return parser.parse_args()


def main() -> int:
    configure_logging()
    args = parse_args()
    source_dir = args.source_dir

    if not source_dir.exists():
        print(f"错误：目录不存在：{source_dir}")
        logging.error("目录不存在：%s", source_dir)
        return 1

    if not source_dir.is_dir():
        print(f"错误：这不是目录：{source_dir}")
        logging.error("不是目录：%s", source_dir)
        return 1

    logging.info("开始扫描目录：%s", source_dir)

    results = organize_files(source_dir, args.apply)
    write_report(source_dir, args.apply, results)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())