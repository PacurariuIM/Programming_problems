

fhand = open("training.txt")
counts = dict()
for lines in fhand:
    words = lines.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

lista = list()
for k, v in counts.items():
    lista.append((v, k))
lista = sorted(lista, reverse=True)

# print(sorted([(v, k) for k, v in counts.items()]))

for v, k in lista[:10]:
    print(k, v)