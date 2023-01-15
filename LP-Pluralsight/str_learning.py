
def reverse_list(lista):
    new_list = []
    while lista:
        new_list.append(lista[-1])
        lista.remove(lista[-1])
    return new_list


print(reverse_list([1, 3, 2, 4, 1]))