import argparse
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


def organize_files(source_dir: Path, apply: bool) -> None:
    files = [path for path in source_dir.iterdir() if path.is_file()]

    if not files:
        print("目录中没有可整理的文件。")
        logging.info("扫描结束：目录为空：%s", source_dir)
        return

    if apply:
        print("开始执行文件整理：")
    else:
        print("以下是整理预览；目前不会移动任何文件：")

    for file_path in sorted(files, key=lambda path: path.name.lower()):
        category = get_category(file_path)
        target_path = source_dir / category / file_path.name

        if target_path.exists():
            print(f"跳过（目标已存在）：{file_path.name}")
            logging.warning("跳过，目标已存在：%s", target_path)
            continue

        if not apply:
            print(f"{file_path.name} -> {target_path.relative_to(source_dir)}")
            logging.info("预览：%s -> %s", file_path, target_path)
            continue

        target_path.parent.mkdir(parents=True, exist_ok=True)
        file_path.rename(target_path)
        print(f"已移动：{file_path.name} -> {target_path.relative_to(source_dir)}")
        logging.info("已移动：%s -> %s", file_path, target_path)


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
    organize_files(source_dir, args.apply)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())