# The Collatz conjecture (also known as 3n+1 conjecture) is a conjecture that applying
# the following algorithm to any number we will always eventually reach one:
# if(number is even) number = number / 2
# if(number is odd) number = 3*number + 1
# Your task is to make a function hotpo that takes a positive n as input and returns
# the number of times you need to perform this algorithm to get n = 1.


def hotpo(n):
    counter = 0
    try:
        while n > 1:
            if n % 2 == 0:
                k = n / 2
                n = k
                counter += 1
            else:
                k = n*3 + 1
                n = k
                counter += 1
        return counter
    except TypeError:
        print("Please insert a positive number")


print(hotpo(2))
