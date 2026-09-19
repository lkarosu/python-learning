def length_of_longest_substring(text: str) -> int:
    left = 0
    window_chars = set()
    max_length = 0

    for right, char in enumerate(text):
        while char in window_chars:
            window_chars.remove(text[left])
            left += 1

        window_chars.add(char)
        max_length = max(max_length, right - left + 1)

    return max_length


assert length_of_longest_substring("abcabcbb") == 3
assert length_of_longest_substring("bbbbb") == 1
assert length_of_longest_substring("pwwkew") == 3
assert length_of_longest_substring("") == 0

print("所有测试通过")