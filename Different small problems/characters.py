# Write a function that will check if two given characters are the same case.
#
# If either of the characters is not a letter, return -1
# If both characters are the same case, return 1
# If both characters are letters, but not the same case, return 0

def function(a: str, b: str):
    if a.islower() and b.islower() or a.isupper() and b.isupper():
        print(1)
    elif a.isupper() and b.islower() or a.islower() and b.isupper():
        print(0)
    else:
        print(-1)


function("a", "9")
