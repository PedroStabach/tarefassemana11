pares = []
impares = []
total = []
for i in range(10):
    j = i + 1
    if j % 2 == 0:
        pares.append(j)
    else:
        impares.append(j)

for i in range(5):
    total.append(impares[i])
    total.append(pares[i])

print(total)