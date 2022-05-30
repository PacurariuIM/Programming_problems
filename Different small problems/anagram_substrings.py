# Find all substrings of a string that are a permutation of another string
# Find all substrings of a string that contains all characters of another string.
# In other words, find all substrings of the first string that are anagrams of the second string.

from collections import Counter


def sliding_window(list1, list2):
    size = len(list2)
    for i in range(len(list1)):
        window = list1[i:i + size]
        if list2 == window:
            l1 = Counter(list2)
            l2 = Counter(window)
            return l1, l2


print(sliding_window("abcddcba", "bc"))
