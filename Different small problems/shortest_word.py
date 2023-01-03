# Simple, given a string of words, return the length of the shortest word(s).
# String will never be empty and you do not need to account for different data types


def short_word(s):
    lista = []
    for i in s.split(" "):
        lista.append(len(i))
    return min(lista)


print(short_word("this is just a random collection of words"))