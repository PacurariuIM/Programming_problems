"""Return multiplication table of size N*N of size provided in parameter"""


def multiplication_table(size):
    final_list = []
    init_list = [ele for ele in range(1, size + 1)]
    for ele in range(1, size + 1):
        multiplied = [ele * item for item in init_list]
        final_list.append(multiplied)
    return final_list


print(multiplication_table(3))
