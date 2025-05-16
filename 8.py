soma = 0
lista = []

for i in range(10):
    j = i + 1
    qrd = j * j
    lista.append(qrd)
    soma += qrd

print(soma)