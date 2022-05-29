# Given an array of integers of size ‘n’,
# Our aim is to calculate the maximum sum
# of ‘k’ consecutive elements in the array.

def max_sum(a_list, k) -> int:
    n = len(a_list)
    if n < k:
        print("Invalid")
        return -1

    window_sum = sum(a_list[:k])
    maximum_sum = window_sum

    for i in range(n - k):
        window_sum = window_sum - a_list[i] + a_list[i + k]
        maximum_sum = max(window_sum, maximum_sum)
    return maximum_sum


print(max_sum([1, 2, 4, 5, 10, 3, 1], 3))
