palavras = []
qnt = int(input("escolha quantas palavras"))

for i in range(qnt):
    elem = input(f"escolha a {i + 1} palavra")
    palavras.append(elem)
def pegar_por_tamanho(lista, tipo='maior'):
    if not lista:
        return None  

    if tipo == 'maior':
        return max(lista, key=len)
    elif tipo == 'menor':
        return min(lista, key=len)
    else:
        raise ValueError("Tipo deve ser 'maior' ou 'menor'")


print(pegar_por_tamanho(palavras, 'maior'), "'e a maior palavra")  
print(pegar_por_tamanho(palavras, 'menor'), "'e a menor palavra")  
