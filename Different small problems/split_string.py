# Complete the solution so that it splits the string into pairs of two characters.
# If the string contains an odd number of characters then it should replace the missing
# second character of the final pair with an underscore ('_').


def solution(s):
    if len(s) % 2 != 0:
        new_s = s + "_"
    else:
        new_s = s
    my_list = [new_s[idx:idx + 2] for idx in range(0, len(new_s), 2)]
    print(my_list)


print(solution("x"))
