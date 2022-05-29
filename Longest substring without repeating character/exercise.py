def length_of_longest_substring(s):
    letters_list = s[1:-1] # we exclude the first and last letters
    window = set()
    l = 0 # we set the left pointer
    result = 0
    for r in range(len(letters_list)): # we iterate the list with the right pointer
        while letters_list[r] in window:
            window.remove(letters_list[l])
            l += 1
        window.add(letters_list[r])
        result = max(result, r - l + 1)
    return result


print(length_of_longest_substring("abcdddca"))