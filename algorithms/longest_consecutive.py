def longest_consecutive(nums: list[int]) -> int:
    numbers = set(nums)
    longest = 0

    for number in numbers:
        # 不是连续序列起点时跳过
        if number - 1 in numbers:
            continue

        current = number
        length = 1

        while current + 1 in numbers:
            current += 1
            length += 1

        longest = max(longest, length)

    return longest


assert longest_consecutive([100, 4, 200, 1, 3, 2]) == 4
assert longest_consecutive([]) == 0
assert longest_consecutive([1, 2, 2, 3]) == 3
assert longest_consecutive([10, 30, 50]) == 1

print("所有测试通过")