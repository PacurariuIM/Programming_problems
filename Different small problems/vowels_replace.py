# Write a function that takes a string and outputs a strings of 1's and 0's
# where vowels become 1's and non-vowels become 0's.
# All non-vowels including non alpha characters (spaces,commas etc.) should be included.
# Example: vowelOne "aeiou, abc" -- "1111100100"

def vowels_count(word):
    lista = []
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    for letter in word:
        if letter in vowels:
            letter = "1"
            lista.append(letter)
        else:
            lista.append("0")

    return "".join(lista)


print(vowels_count("vowelonea"))