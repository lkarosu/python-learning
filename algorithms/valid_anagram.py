def is_anagram(first: str, second: str) -> bool:
    if len(first) != len(second):
        return False

    counts = {}

    for char in first:
        # 将 char 的计数加一
        counts[char] = counts.get(char, 0) + 1

    for char in second:
        # 若 char 不存在，或对应计数已为 0，返回 False
        if char not in counts or counts[char] == 0:
            return False
        # 否则将 char 的计数减一
        counts[char] -= 1

    return True


assert is_anagram("anagram", "nagaram") is True
assert is_anagram("rat", "car") is False
assert is_anagram("", "") is True
assert is_anagram("aacc", "ccac") is False

print("所有测试通过")