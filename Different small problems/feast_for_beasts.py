# write a function <feast> that takes 2 arguments (beast, dish)
# return true if dish first and last letter correspond with the beast first and last letter
# no numerical allowed, all lowercase, spaces allowed only inside the name

def feast(beast: str, dish: str):
    return beast[0] == dish[0] and beast[-1] == dish[-1]


print(feast("brown bear", "bar"))