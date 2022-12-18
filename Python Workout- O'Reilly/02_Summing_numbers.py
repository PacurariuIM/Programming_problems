

def mysum(*number):
    output = 0
    for i in number:
        output += i
    return output


print(mysum(1, 2, 10))
