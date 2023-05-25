def two_sum(nums: list[int], target: int) -> list[int]:
    d = {}
    for i, j in enumerate(nums):
        diff = target - j
        if diff in d:
            return [d[diff], i]
        d[j] = i


print(two_sum([1, 2, 4], 6))

