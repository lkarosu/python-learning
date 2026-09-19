def contains_duplicate(nums: list[int]) -> bool:
    seen = set()

    for number in nums:
        # 如果 number 已出现过，立即返回 True
        if number in seen:
            return True
        # 否则加入 seen
        seen.add(number)

    return False


assert contains_duplicate([1, 2, 3, 1]) is True
assert contains_duplicate([1, 2, 3, 4]) is False
assert contains_duplicate([]) is False

print("所有测试通过")