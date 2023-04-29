n = int(input())

for i in range(n):
    jogador1 = input()
    jogador2 = input()
    if jogador1 == "papel":
        if jogador2 == "papel":
            print("Ambos venceram")
        else:
            print("Jogador 2 venceu")
    elif jogador1 == "pedra":
        if jogador2 == "papel":
            print("Jogador 1 venceu")
        elif jogador2 == "pedra":
            print("Sem ganhador")
        else:
            print("Jogador 2 venceu")
    else:
        if jogador2 == "papel" or jogador2 == "pedra":
            print("Jogador 1 venceu")
        else:
            print("Aniquilacao mutua")
