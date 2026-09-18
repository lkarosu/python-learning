from collections import Counter
from pathlib import Path


def count_words(file_path: str) -> Counter:
    text = Path(file_path).read_text(encoding="utf-8")
    words = text.lower().split()
    return Counter(words)


def main():
    try:
        counts = count_words("sample.txt")
    except FileNotFoundError:
        print("找不到 sample.txt，请先创建该文件。")
        return

    for word, count in counts.most_common(10):
        print(f"{word}: {count}")


if __name__ == "__main__":
    main()