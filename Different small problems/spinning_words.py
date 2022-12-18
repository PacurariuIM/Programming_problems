# Write a function that takes in a string of one or more words,
# and returns the same string, but with all five or more letter words reversed
# Strings passed in will consist of only letters and spaces.
# Spaces will be included only when more than one word is present.


def spinning_words(sentence):
    lista = sentence.split()
    for i in lista:
        if len(i) > 4:
            j = i[::-1]
            lista = list(map(lambda x: x.replace(i,j), lista))
    return " ".join(lista)


print(spinning_words("How are you Pacurariu ?"))
