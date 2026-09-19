def group_anagrams(words: list[str]) -> list[list[str]]:
    groups = {}

    for word in words:
        key = "".join(sorted(word))

        if key not in groups:
            groups[key] = []

        groups[key].append(word)

    return list(groups.values())


def normalize(groups: list[list[str]]) -> list[list[str]]:
    return sorted(sorted(group) for group in groups)


words = ["eat", "tea", "tan", "ate", "nat", "bat"]
expected = [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]

assert normalize(group_anagrams(words)) == normalize(expected)

print("所有测试通过")