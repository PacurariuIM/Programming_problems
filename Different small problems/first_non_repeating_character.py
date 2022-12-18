# Write a function named first_non_repeating_letter that takes a string input
# and returns the first character that is not repeated anywhere in the string.
# If a string contains all repeating characters, it should return an empty string ("") or None

def first_non_repeating_character(word: str):
    lower_case = word.lower()
    lista = list(lower_case)
    for i in lista:
        occurrence = lista.count(i)

        if occurrence > 1:
            continue
        else:
            return i


print(first_non_repeating_character("sTreSS"))