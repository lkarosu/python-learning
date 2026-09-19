def two_sum(nums: list[int], target: int) -> list[int] | None:
    seen = {}

    for index, number in enumerate(nums):
        complement = target - number

        # 先检查 complement 是否在 seen 中。
        # 找到则返回已有下标和当前下标。
        # 否则记录：seen[number] = index
        if complement in seen:
            return [seen[complement], index]
        seen[number] = index
        
    return None


assert two_sum([2, 7, 11, 15], 9) == [0, 1]
assert two_sum([3, 3], 6) == [0, 1]
assert two_sum([1, 2, 3], 10) is None

print("所有测试通过")