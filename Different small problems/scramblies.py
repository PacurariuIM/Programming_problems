# Complete the function scramble(str1, str2)
# that returns true if a portion of str1 characters can be rearranged to match str2,
# otherwise returns false.

def scramble(s1, s2):
    l1 = [*s1]
    l2 = [*s2]
    for ele in sorted(l2):
        if ele in sorted(l1):
            l2.remove(ele)

    if not l2:
        return True
    else:
        return False


print(scramble("abcd", "adbbb"))
