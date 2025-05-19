## JOGO DA VELHA
vitoria = [False, False]

def checar_vitoria(tab):
    combinacoes = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8], 
        [0, 3, 6],  
        [1, 4, 7], 
        [2, 5, 8],  
        [0, 4, 8],  
        [2, 4, 6],  
    ]
    for a, b, c in combinacoes:
        if tab[a] == tab[b] == tab[c] and tab[a] in ["x", "0"]:
            return tab[a]
    return None

escolha = [1, 2]
tab = ["-" for i in range(9)]

## TABELA
print("Temos as seguintes opcoes, escolhe sua opcao!")
print(f"0 1 2")
print(f"3 4 5")
print(f"6 7 8")

while True:
    for i in range(2):
        escolha[i] = int(input(f"onde o player {(i+1)} deseja colocar? "))
        
        if tab[escolha[i]] != "-":
            print("A posição escolhida já foi preenchida, escolha outra.")
            continue

        # Define o símbolo do jogador atual
        if i == 0:
            tab[escolha[i]] = "x"
        else:
            tab[escolha[i]] = "0"

        # Mostra o tabuleiro
        print(f"{tab[0]} {tab[1]} {tab[2]}")
        print(f"{tab[3]} {tab[4]} {tab[5]}")
        print(f"{tab[6]} {tab[7]} {tab[8]}")

        # Verifica vitória após a jogada
        vencedor = checar_vitoria(tab)
        if vencedor == "x":
            vitoria[0] = True
        elif vencedor == "0":
            vitoria[1] = True

        # Sai do loop se alguém vencer
        if vitoria[0] or vitoria[1]:
            break

    ## VITÓRIA
    if vitoria[0] or vitoria[1]:
        for i in range(2):
            if vitoria[i]:
                print(f"\nPLAYER {(i+1)} GANHOU")
                print(f"{tab[0]} {tab[1]} {tab[2]}")
                print(f"{tab[3]} {tab[4]} {tab[5]}")
                print(f"{tab[6]} {tab[7]} {tab[8]}")
        break
