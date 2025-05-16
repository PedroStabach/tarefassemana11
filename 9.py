import random

letras = int(input("Escolha quantas letras você quer adivinhar: "))
total = []

for i in range(letras):
    escolha = input(f"Escolha a letra número {i + 1}: ")
    total.append(escolha)

for i in range(letras):
    aleatorio = random.choice(total)
    posicao_real = total.index(aleatorio)

    try:
        tentativa = int(input(f"Em que posição (0 a {letras - 1}) está a letra '{aleatorio}'? "))
        if tentativa == posicao_real:
            print("Parabéns, você acertou!")
        else:
            print(f"Eita, não foi dessa vez. A posição correta era {posicao_real}.")
    except ValueError:
        print("Você não digitou um número válido.")
