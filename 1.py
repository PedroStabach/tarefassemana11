list = []

quant = int(input("quantos numeros voce quer? "))
for i in range(quant):
    numeros = int(input(f"escolha o {i+1} numero"))
    list.append(numeros)

print(f"os seus numeros foram {list}")