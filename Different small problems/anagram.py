from collections import Counter


def anagram(s1, s2):
    if Counter(s1) == Counter(s2):
        print("We have an anagram")
    else:
        print("No anagram")
    return


anagram("merm", "abdc")
