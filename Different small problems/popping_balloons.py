# Sami is practicing her aim with her bow and is shooting some balloons in the air.
# On each balloon, they have different numbers written on them which represent their size.
# She would like to pop the balloon highest in the air that also has the most balloons of the same size present.
# If there is a tie, then she will instead pop the balloon of the size highest in the air.
# Do you think you can output which balloon she pops on each shot?
#
# You will be provided an array of the balloons as integers (the integers representing the sizes)in lowest to highest order in the air.
# You will also be given an integer pops, which will be the number of pops that Sami will execute.
#
# Constraints
# 0 < pops <= number of elements in balloons
# 10 <= number of elements in balloons <= 500
# 1 <= balloon size <= 1000
#
# Example:
# pops = 4
# balloons = [5, 7, 5, 7, 4, 5]
#
# pop #1: 5
# pop #2: 7
# pop #3: 5
# pop #4: 4
#
# return: [5, 7, 5, 4]
from collections import Counter


def freq_stack(pop, balloons):
    dict1 = {}
    occurence = Counter(balloons).most_common(pop)
    print(occurence)



print(freq_stack(4, [2, 3, 4, 4, 3, 1, 1, 3, 2]))
