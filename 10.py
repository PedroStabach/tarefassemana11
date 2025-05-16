##JOGO DA VELHA
tab = [str(f"{i}") for i in range(9)]
while True:
    ##TABELA
    print(f"{tab[0]} {tab[1]} {tab[2]}")
    print(f"{tab[3]} {tab[4]} {tab[5]}")
    print(f"{tab[6]} {tab[7]} {tab[8]}")

    escolha = int(input(f"onde deseja colocar?"))
    tab[escolha] = "x"

    if ((tab[0] and tab[1] and tab[2]) == "x") or ( (tab[3] and tab[4] and tab[5]) == "x") or ( (tab[6] and tab[7] and tab[8]) == "x"):
        print("VOCE GANHOU")
        ##TABELA POS JOGO
        print(f"{tab[0]} {tab[1]} {tab[2]}")
        print(f"{tab[3]} {tab[4]} {tab[5]}")
        print(f"{tab[6]} {tab[7]} {tab[8]}")

        continuar = input("deseja continuar?")
        tab = [str(f"{i}") for i in range(9)]
        if continuar == "N":
            break


