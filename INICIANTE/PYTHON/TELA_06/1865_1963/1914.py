quant = int(input())
for jogos in range(quant):
    escolhas = input().split()
    valores = input().split()
    a = int(valores[0])
    b = int(valores[1])
    soma = a + b
    if soma % 2 == 0:
        if escolhas[1] == "PAR":
            print(escolhas[0])
        else:
            print(escolhas[2])
    else:
        if escolhas[1] == "IMPAR":
            print(escolhas[0])
        else:
            print(escolhas[2])
