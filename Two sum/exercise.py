def twoSum(nums: list[int], target: int) -> list[int]:
    dict = {}
    for i, j in enumerate(nums):
        diff = target - j
        if diff in dict:
            return [dict[diff], i]
        dict[j] = i


print(twoSum([1, 2, 4], 6))