from collections import Counter
from pathlib import Path
import json


PUNCTUATION = ",.!?;:"


def read_and_clean_words(file_path: str) -> list[str]:
    """读取文本，转小写并去掉单词两端的常见标点。"""
    text = Path(file_path).read_text(encoding="utf-8")
    raw_words = text.lower().split()

    clean_words = []
    for word in raw_words:
        cleaned_word = word.strip(PUNCTUATION)

        if cleaned_word:
            clean_words.append(cleaned_word)

    return clean_words


def count_words(words: list[str]) -> Counter:
    """统计每个单词出现的次数。"""
    return Counter(words)


def save_counts(counts: Counter, output_path: str) -> None:
    """将统计结果保存为 JSON 文件。"""
    with Path(output_path).open("w", encoding="utf-8") as file:
        json.dump(dict(counts), file, ensure_ascii=False, indent=2)


def print_top_words(counts: Counter, top_n: int = 10) -> None:
    """在终端输出出现次数最多的若干单词。"""
    print(f"出现次数最多的前 {top_n} 个单词：")

    for word, count in counts.most_common(top_n):
        print(f"{word}: {count}")


def main() -> None:
    input_path = "sample.txt"
    output_path = "word_count.json"

    try:
        words = read_and_clean_words(input_path)
    except FileNotFoundError:
        print(f"找不到 {input_path}，请先创建该文件。")
        return
    except UnicodeDecodeError:
        print(f"无法按 UTF-8 编码读取 {input_path}。")
        return

    counts = count_words(words)
    save_counts(counts, output_path)
    print_top_words(counts)

    print(f"\n统计结果已保存到：{output_path}")


if __name__ == "__main__":
    main()